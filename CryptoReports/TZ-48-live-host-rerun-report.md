# TZ-48 — the live host, TZ-47 corrected at its gate — REPORT

**Status: BLOCKED at §0.6, the geoblock — G-GEO UNREAD.** `L geoblock 41-geoblock` (`41-geoblock.log`, 08:24:20 to
08:25:20 UTC on 2026-11-19) stopped on its own assert, `exit=1`:
`AssertionError: BLOCKED: G-GEO UNREAD - the venue did not read this address`. Over IPv4 the venue read the live host's
address at the first read: status `200`, `blocked False`, `country 'BG'`, `region '22'`, and the address it saw was the
connection's own — PASS. The host has one global IPv6 address and `polymarket.com` resolved over IPv6, so G-GEO read
IPv6 too (§4.1). Each of its three reads, 30 s apart, ended in `OSError` before any status — UNREAD. One family read
UNREAD makes G-GEO UNREAD (`geo_overall`), and §4.1 makes UNREAD this TZ's BLOCK.

- **The live host gate passed:** LH1 to LH5, **5 of 5** — `vs-2348` by its first label, Ubuntu 24.04, Python 3.12,
  not the capture host, and TZ-47's pinned key `SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw` among the host's
  three SSH host keys — and both its floors; `G-SPEC PASS: 2 of 2` (§2.2).
- **Not read:** G-NET, G-LAT, the disk, G-SWAP and G-LOG. No self-test ran, and there is no branch, commit of the
  instrument or pull request: the BLOCK came before §3.1. **§4.8 names G-GEO UNREAD among its REFUND readings.**
- **Nothing on the live host was configured:** no swap, no drop-in, no sysctl, no unit touched. It carries root's one
  `authorized_keys` line, TZ-47's. Its work tree `/root/tz48-work` was made by §0.6's copy and removed by §9's
  B-RECLAIM-LIVE, `exit=1`.
- **The capture host:** no unit was started, stopped or touched, and no store was written. The access TZ-47 made
  stood: `R true` read `exit=0` at its first read, so B-ACCESS was not handed over.
- **No block was handed to the Boss, and the classifier refused nothing.**
- **No address of either host, no password and no private key** is in this report, and of the live host's name only
  its first label.

---

## 0. Fingerprint

`I0 fingerprint` (`logs/02-fingerprint.log`, 08:22:17 UTC) printed:

```
[2026-11-19T08:22:17Z] FINGERPRINT PASS: revision 2026-11-18-a; anchors 6 of 6, 4 re-derived; rows 65: frozen 62 of 62 equal, tracked 2, reported 1
```

**Revision string:** `2026-11-18-a`, equal to TZ-48's header. **Anchors**, map §0 against TZ-48's header, 6 of 6 equal;
`A2`, `A4`, `A5` and `A6` re-derived by the instrument as the first 12 hex characters of their files' SHA-256, 4 of 4
equal:

| anchor | TZ-48 and map §0 | re-derived |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | — |
| `A2` — collector | `6c5089330629` | `research/twap-divergence.py` `6c5089330629`, equal |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | — |
| `A4` — executor contract | `6ac6e10aeabc` | `BTC-EXECUTOR-INSTRUCTIONS.md` `6ac6e10aeabc`, equal |
| `A5` — recorder | `0f6c90451cbd` | `research/recorder/recorder.py` `0f6c90451cbd`, equal |
| `A6` — pricer | `729f0bcdbee3` | `research/pfair.py` `729f0bcdbee3`, equal |

**Every row of map §0's table, 65 of 65, as `fingerprint` printed it:** 62 `frozen`, each equal to the map in lines,
bytes and SHA-256; 2 `tracked`; 1 `reported`. The tree is the primary checkout `/root/btc-5m-twap`, `main` at
`bea33af77591431deff3c624102706408d99ec07`, which is `11cf0e2` plus the upload of TZ-48.

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

**The model:** TZ-48 names Claude Opus 5.5. The session's own record read `claude-opus-5-5` as both the configured and
the last served model.

---

## 1. The blocker

TZ-48 §0.6 runs `L geoblock 41-geoblock` before anything on the live host changes. `mode_geoblock` (Appendix A, lines
1242 to 1258) reads IPv4. It reads IPv6 as well where `has_global_ipv6` finds a global address in `/proc/net/if_inet6`
and `polymarket.com` resolves over IPv6. Both held here: `host before` printed `NETWORK global IPv6 addresses: 1`, and
the IPv6 lookup returned. `geo_read` over IPv4 read PASS at its first read. Over IPv6 each of its three reads raised
`OSError` before any status. The instrument prints `type(exc).__name__`, and the name was `OSError` itself: not
`TimeoutError`, not an `SSLError`. The three reads are stamped exactly 30 s apart, the gap between them, so none
waited on its timeout of 10 s. The
mode's counts, `lookups 5, requests 1`, say every lookup returned — one IPv6 lookup in `mode_geoblock` and one in each
of the four reads — and only IPv4's request was made: what failed was the IPv6 connection to the venue's address. So
`geo_reading` read UNREAD for IPv6, `geo_overall(["PASS", "UNREAD"])` read UNREAD, and `mode_geoblock` asserted, `exit=1`.
§0.6: "**`exit=1` is BLOCKED** — the venue blocks this address or did not read it". §4.1: "**Both BLOCKED and UNREAD
are this TZ's BLOCK**". The run went to §3.9's copy and §9, as §3 says for a BLOCK before §3.1.

---

## 2. The evidence

Every log below is quoted whole, as written. Its SHA-256 is in §2.7, and its copy in the forensic store is
`/root/btc-forensics/tz48-work--<path with / as -->`.

### 2.1 The geoblock — `41-geoblock.log`, as the live host wrote it and §3.9's copy brought it back

```
2026-11-19T08:24:20.254117920Z
[2026-11-19T08:24:20Z] GEOBLOCK IPv4 read 1: https://polymarket.com/api/geoblock, status 200; blocked False, country 'BG', region '22'; reply keys ['blocked', 'country', 'ip', 'region']; the address the venue saw is this connection's own: True - PASS
[2026-11-19T08:24:20Z] GEOBLOCK IPv6 read 1: https://polymarket.com/api/geoblock, status None; blocked None, country None, region None; reply keys None; the address the venue saw is this connection's own: None, OSError - UNREAD
[2026-11-19T08:24:50Z] GEOBLOCK IPv6 read 2: https://polymarket.com/api/geoblock, status None; blocked None, country None, region None; reply keys None; the address the venue saw is this connection's own: None, OSError - UNREAD
[2026-11-19T08:25:20Z] GEOBLOCK IPv6 read 3: https://polymarket.com/api/geoblock, status None; blocked None, country None, region None; reply keys None; the address the venue saw is this connection's own: None, OSError - UNREAD
[2026-11-19T08:25:20Z] G-GEO UNREAD over ['IPv4', 'IPv6']
[2026-11-19T08:25:20Z] RECORD geoblock {"reading":"UNREAD","readings":["PASS","UNREAD"]}
[2026-11-19T08:25:20Z] peak memory of this run: 29990912 bytes
[2026-11-19T08:25:20Z] refused by the hook: 0; lookups 5, requests 1, handshakes 0, TCP connects 0
Traceback (most recent call last):
  File "/root/tz48-work/tz48-live-host.py", line 1855, in <module>
    sys.exit(main(sys.argv[1:]))
             ^^^^^^^^^^^^^^^^^^
  File "/root/tz48-work/tz48-live-host.py", line 1846, in main
    rc = table[mode]()
         ^^^^^^^^^^^^^
  File "/root/tz48-work/tz48-live-host.py", line 1256, in mode_geoblock
    assert g == "PASS", "BLOCKED: G-GEO %s - the venue %s this address" % (
           ^^^^^^^^^^^
AssertionError: BLOCKED: G-GEO UNREAD - the venue did not read this address
exit=1
```

### 2.2 The live host gate — `40-host-before.log`, as the live host wrote it and §3.9's copy brought it back

```
2026-11-19T08:23:42.148903900Z
[2026-11-19T08:23:42Z] LH1 hostname vs-2348: PASS
[2026-11-19T08:23:42Z] LH2 Ubuntu 24.04: PASS
[2026-11-19T08:23:42Z] LH3 Python 3.12: PASS
[2026-11-19T08:23:42Z] LH4 not the capture host: PASS
[2026-11-19T08:23:42Z] LH5 the host key pinned at TZ-47's first connection: PASS
[2026-11-19T08:23:42Z] HOST its SSH host keys: [('ecdsa-sha2-nistp256', 'SHA256:717ijbIvj026Fy6VpHg2IBIeCLa2aPu/IsGNHneAITA'), ('ssh-ed25519', 'SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw'), ('ssh-rsa', 'SHA256:LzqPSbHCa+VWhcazHny+A19sCqjzuUUGf9nWWTTfYAY')]
[2026-11-19T08:23:42Z] MemAvailable read 1: 1508622336 bytes, floor 70779836
[2026-11-19T08:23:42Z] available on /: 16989290496 bytes, floor 3589660928
[2026-11-19T08:23:42Z] HOST vs-2348; Ubuntu 24.04.5 LTS; kernel 6.8.0-138-generic x86_64; Python 3.12.3; processors 1, Intel(R) Xeon(R) Gold 6248R CPU @ 3.00GHz
[2026-11-19T08:23:42Z] HOST vendor 'VMware, Inc.', product 'VMware20,1'
[2026-11-19T08:23:42Z] HOST booted 2026-11-18T16:57:40Z, up 55562 s
[2026-11-19T08:23:42Z] MEMORY MemTotal 1944465408, MemAvailable 1508622336, MemFree 956661760, Buffers 65146880, Cached 606875648, SwapTotal 1073737728, SwapFree 1073737728
[2026-11-19T08:23:42Z] DISK / /dev/mapper/lvm-root ext4: total 20779339776, available 16989290496, free 17218088960 bytes; inodes 1294336, free 1208073
[2026-11-19T08:23:42Z] SWAP /proc/swaps [('/swap.img', 'file', 1048572, 0)]; /swapfile absent; fstab lines of swap [('/swap.img', 'none', 'swap', 'sw', '0', '0')]
[2026-11-19T08:23:42Z] SWAP vm.swappiness 60; set in []
[2026-11-19T08:23:42Z] JOURNALD /etc/systemd/journald.conf.d: ['cap.conf']
[2026-11-19T08:23:42Z] JOURNALD /usr/lib/systemd/journald.conf.d: ['syslog.conf']
[2026-11-19T08:23:42Z] JOURNALD journald.conf, set: ['[Journal]']
[2026-11-19T08:23:42Z] JOURNALD in force, by `systemd-analyze cat-config` exit 0: {'SystemMaxUse': ('200M', '/etc/systemd/journald.conf.d/cap.conf'), 'ForwardToSyslog': ('yes', '/usr/lib/systemd/journald.conf.d/syslog.conf')}
[2026-11-19T08:23:42Z] JOURNALD disk usage: Archived and active journals take up 42.2M in the file system.
[2026-11-19T08:23:42Z] LOGS /var/log: 33 files, 78526341 bytes apparent, 55767040 on disk; the largest on disk [(9900032, 'journal/ef7f4459e2364097b06322e174690e1c/system@cdcaa05a03bc459cad6b13a19ceb7601-000000000000187a-0006608fe8d3dc1d.journal'), (9625600, 'journal/ef7f4459e2364097b06322e174690e1c/system@cdcaa05a03bc459cad6b13a19ceb7601-0000000000004cb1-0006609449653fc7.journal'), (9613312, 'journal/ef7f4459e2364097b06322e174690e1c/system@cdcaa05a03bc459cad6b13a19ceb7601-0000000000007d03-00066097fbd2be99.journal'), (8388608, 'journal/ef7f4459e2364097b06322e174690e1c/system.journal'), (6750208, 'journal/ef7f4459e2364097b06322e174690e1c/system@7e96aa5e1c8641b4a9dfcabd6f967967-0000000000000464-00066089ee97e00c.journal'), (5222400, 'btmp'), (4542464, 'auth.log'), (704512, 'syslog')]
[2026-11-19T08:23:42Z] UNIT rsyslog.service {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'}
[2026-11-19T08:23:42Z] UNIT syslog.socket {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'static'}
[2026-11-19T08:23:42Z] UNIT systemd-journald.service {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'static'}
[2026-11-19T08:23:42Z] UNIT systemd-timesyncd.service {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'}
[2026-11-19T08:23:42Z] UNIT chrony.service {'LoadState': 'not-found', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': ''}
[2026-11-19T08:23:42Z] UNIT ssh.service {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'disabled'}
[2026-11-19T08:23:42Z] UNIT ssh.socket {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'}
[2026-11-19T08:23:42Z] UNIT unattended-upgrades.service {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'}
[2026-11-19T08:23:42Z] UNIT apt-daily.timer {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-19T08:23:42Z] UNIT apt-daily-upgrade.timer {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-19T08:23:42Z] CLOCK {'Timezone': 'Etc/UTC', 'LocalRTC': 'no', 'CanNTP': 'yes', 'NTP': 'yes', 'NTPSynchronized': 'yes'}
[2026-11-19T08:23:42Z] CLOCK timesync-status exit 0: Server: 185.125.190.57 (ntp.ubuntu.com) | Poll interval: 34min 8s (min: 32s; max 34min 8s) | Leap: normal | Version: 4 | Stratum: 2 | Reference: 91EE5050 | Precision: 1us (-25) | Root distance: 5.050ms (max: 5s) | Offset: -1.947ms | Delay: 35.180ms | Jitter: 1.544ms | Packet count: 33 | Frequency: +33.489ppm
[2026-11-19T08:23:42Z] SSHD -T exit 0: ['port 22', 'permitrootlogin yes', 'pubkeyauthentication yes', 'passwordauthentication yes', 'kbdinteractiveauthentication no']
[2026-11-19T08:23:42Z] SSHD set in its files: ['/etc/ssh/sshd_config: PermitRootLogin yes', '/etc/ssh/sshd_config: KbdInteractiveAuthentication no', '/etc/ssh/sshd_config.d/01-xserver.conf: PermitRootLogin yes']
[2026-11-19T08:23:42Z] SSHD authorized keys of root: [('ssh-ed25519', 'SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo')]
[2026-11-19T08:23:42Z] SOCKETS listening or bound: ['tcp any:22 systemd', 'tcp loopback:53 systemd-resolve', 'tcp6 any:22 systemd', 'udp any:57775 ?', 'udp loopback:53 systemd-resolve', 'udp6 any:57775 ?']
[2026-11-19T08:23:42Z] NETWORK global IPv6 addresses: 1
[2026-11-19T08:23:42Z] PROCESSES by resident memory: ['multipathd 363 27987968', 'python3 21881 26894336', 'unattended-upgr 712 23896064', 'systemd-journal 303 22347776', 'udisksd 692 13885440', 'systemd 1 13627392', 'systemd-resolve 534 13320192', 'ModemManager 730 13234176', 'VGAuthService 626 12578816', 'systemd 1316 11841536']
[2026-11-19T08:23:42Z] UPGRADES Automatic-Reboot set: nowhere - the package's default
[2026-11-19T08:23:42Z] G-SPEC MemTotal at least 1800000000: 1944465408, PASS
[2026-11-19T08:23:42Z] G-SPEC the root file system at least 18000000000: 20779339776, PASS
[2026-11-19T08:23:42Z] G-SPEC PASS: 2 of 2
[2026-11-19T08:23:42Z] RECORD host-before {"disk_available":16989290496,"disk_total":20779339776,"mem_available":1508622336,"mem_total":1944465408,"spec":true,"swap_total":1073737728,"swaps":[["/swap.img","file",1048572,0]]}
[2026-11-19T08:23:42Z] peak memory of this run: 26714112 bytes
[2026-11-19T08:23:42Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

LH1 to LH5 PASS, 5 of 5 (V7). `MemAvailable` `1,508,622,336` against `70,779,836` at its first read, and
`16,989,290,496` bytes available on `/` against `3,589,660,928`. `G-SPEC PASS: 2 of 2` — `MemTotal` `1,944,465,408`
against `1,800,000,000`, the root file system `20,779,339,776` against `18,000,000,000` (V11, its first of two reads;
`host after` did not run). The host's SSH host keys are three, by type and fingerprint; root's authorized keys are one,
the Executor's `SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo`.

### 2.3 The access — `06-access.log`

```
2026-11-19T08:23:03.103106595Z
exit=0
2026-11-19T08:23:15.081776749Z
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
```

`R true` read `exit=0` at its first read, 08:23:03 UTC: the access TZ-47 made stood, and B-ACCESS and B-ACCESS-KEY were
not handed over. The Executor's key is TZ-47's, `SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo`; the alias's
settings are printed without their `hostname` line; the live host's key pinned under `live-host` is TZ-47's, `ED25519`
`SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw`; and the last three lines read `vs-2348`, `root` and
`work tree exit=1`, as §0.6 requires (V6).

### 2.4 The copy — `07-copy.log`

```
2026-11-19T08:23:28.890924439Z
exit=0
scp exit=0
b3b2cd4b595e79dcfba2a2b5ca5955348417cd11069f1ee096589dedd474250f  /root/tz48-work/tz48-live-host.py
 1855 94715 /root/tz48-work/tz48-live-host.py
```

`exit=0`, `scp exit=0`, and the live host's copy has §0.1's 1,855 lines, 94,715 bytes and SHA-256
`b3b2cd4b595e79dcfba2a2b5ca5955348417cd11069f1ee096589dedd474250f` (V3).

### 2.5 What passed before it — §0.0 to §0.5, the capture host

**§0.0** — the session's own read, at 08:21:55 UTC, before the work tree existed:

```
ready=1: second 30115 of the day, outside 10800 to 27000; 10512760832 bytes free on /var/lib, 7795535636 needed; MemAvailable 274083840, 70779836 needed; at 1795076515 2026-11-19T08:21:55Z
```

`mkdir /root/tz48-work /root/tz48-work/logs; echo "exit=$?"` printed `exit=0`. Then `00-ready.log`:

```
2026-11-19T08:22:10.714434076Z
ready=1: second 30130 of the day, outside 10800 to 27000; 10512429056 bytes free on /var/lib, 7795535636 needed; MemAvailable 270249984, 70779836 needed; at 1795076530 2026-11-19T08:22:10Z
```

**§0.1** — `01-stage.log`. The instrument was extracted at Appendix A's SHA-256 (V3).

```
2026-11-19T08:22:10.730775064Z
/root/tz48-work/stage/research/tz48-live-host.py 1855 94715 b3b2cd4b595e79dcfba2a2b5ca5955348417cd11069f1ee096589dedd474250f created
exit=0
```

**§0.2** — `FINGERPRINT PASS`, §0 above (V1, the first of its two reads; the second, §3.1's, did not run).

**§0.3** — `03-host-gate.log`. H1 one path; H2 `/dev/vda2`, `31612203008`, and `grep -c` `4`; H3 `3.12.3`; H4 four
paths. The memory gate's first read was `298,237,952` against `70,779,836`. The disk gate read `avail`
`10,511,978,496` against `7,795,535,636`. **7 of 7** (V5). The consumer, `telemetry-watch.service`, read `disabled`
(exit 1) and `inactive` (exit 3).

```
2026-11-19T08:22:27.422971390Z
Thu Nov 19 08:22:27 AM UTC 2026
1795076547
2026-08-02 07:24:32
1
MemTotal:         978640 kB
MemAvailable:     269448 kB
SwapTotal:       3174396 kB
SwapFree:        2579696 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10511978496
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
423773583	/var/lib/btc-rewardbook
356392380	/root/btc-forensics
24704103	/root/.claude-8j
2579
disabled
exit=1
inactive
exit=3
/root/tz47-work exit=1
/root/.ssh/live-host exit=0
/root/btc-5m-twap       bea33af [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/bec9e390-46e1-55e5-81f0-1562edfe0238/scratchpad
total 32
drwx------  8 root root 4096 Nov 19 08:19 .
drwx------ 40 root root 4096 Nov 19 08:19 ..
drwx------  3 root root 4096 Nov 19 08:19 91e07016-bfd8-431a-8738-d3dd14c17827
drwx------  3 root root 4096 Nov 15 10:28 95cf58d2-1ec6-4c73-a622-38d04665f5ae
drwx------  3 root root 4096 Nov 18 22:07 badf0ac4-2f71-4a1a-9c42-85675441c8ae
drwx------  4 root root 4096 Nov 19 08:19 bec9e390-46e1-55e5-81f0-1562edfe0238
drwx------  4 root root 4096 Nov 17 14:14 ccca2df8-e51d-56bc-8205-06299775095a
drwx------  4 root root 4096 Nov 18 22:07 dd42fdcf-137f-5b9f-8a10-6f720861ab64
MemAvailable read 1 08:22:27: 298237952
```

**§0.3, the room** — `04-room.log`, run in the background as §0.3 says. The archive's service read `inactive` at its
first read. The margin over `STREAM_FLOOR` and `PEAK` was **`2,844,579,254`** bytes, above `1,000,000,000`.

```
2026-11-19T08:22:36.380906492Z
[2026-11-19T08:22:36Z] btc-rewardbook-archive.service read 1: inactive
[2026-11-19T08:22:36Z] MemAvailable read 1: 283869184 bytes, floor 70779836
[2026-11-19T08:22:36Z] available on /var/lib: 10511769600 bytes, floor 7795535636
[2026-11-19T08:22:36Z] ROOM: 10511769600 bytes available on /var/lib; the reward book's stream files 78345290 bytes in 5 files under 23 day directories; the room 10590114890; its margin over STREAM_FLOOR 7300000000 and PEAK 445535636: 2844579254 bytes
[2026-11-19T08:22:36Z] peak memory of this run: 26021888 bytes
[2026-11-19T08:22:36Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

**§0.5** — `05-number.log`: `NUMBER PASS - 2 of 2`. `05-refs.log`: 180 lines, `refs/heads/tz-48-live-host-rerun`
absent (V2, the first of its two reads). **Against the Architect's 177 lines of 2026-11-18 at 22:52 UTC, two kinds
differ:** `refs/tags/rewardbook-streams-*` reads `46`, where the Architect read `43`. The session's `git fetch` at
contract §1 step 1 printed the three new tags, `rewardbook-streams-1795051820`, `-1795062620` and `-1795073420`. And
`HEAD` and `refs/heads/main` stand at `bea33af`, the upload of TZ-48, where the Architect read `11cf0e2`. Every other
kind's count is equal: `tz-*` 22, pull heads 45, `pairbook-streams-*` 59, and the four annotated-tag lines and two
lightweight tags 1 each. Recorded, not BLOCKING (§0.5).

```
2026-11-19T08:22:51.696371609Z
[2026-11-19T08:22:51Z] origin/main bea33af77591431deff3c624102706408d99ec07: 115 paths under CryptoTZ/ and CryptoReports/; of the number TZ-48-: ['CryptoTZ/TZ-48-live-host-rerun.md'] and []
[2026-11-19T08:22:51Z] NUMBER PASS - 2 of 2
[2026-11-19T08:22:51Z] peak memory of this run: 26152960 bytes
[2026-11-19T08:22:51Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

```
2026-11-19T08:22:51.784583453Z
[2026-11-19T08:22:52Z] REF bea33af77591431deff3c624102706408d99ec07	HEAD
[2026-11-19T08:22:52Z] REF bea33af77591431deff3c624102706408d99ec07	refs/heads/main
[2026-11-19T08:22:52Z] REFS HEAD                                     1
[2026-11-19T08:22:52Z] REFS refs/heads/main                          1
[2026-11-19T08:22:52Z] REFS refs/heads/tz-*                          22
[2026-11-19T08:22:52Z] REFS refs/pull/*/head                         45
[2026-11-19T08:22:52Z] REFS refs/tags/pairbook-streams-*             59
[2026-11-19T08:22:52Z] REFS refs/tags/rewardbook-streams-*           46
[2026-11-19T08:22:52Z] REFS refs/tags/tz-01a-dataset                 1
[2026-11-19T08:22:52Z] REFS refs/tags/tz-01a-dataset^{}              1
[2026-11-19T08:22:52Z] REFS refs/tags/tz-27-pairbook-streams         1
[2026-11-19T08:22:52Z] REFS refs/tags/tz-27-pairbook-streams^{}      1
[2026-11-19T08:22:52Z] REFS refs/tags/tz-44-l0-inputs                1
[2026-11-19T08:22:52Z] REFS refs/tags/tz-45-l0-rule-w-inputs         1
[2026-11-19T08:22:52Z] REFS 180 lines; refs/heads/tz-48-live-host-rerun absent
[2026-11-19T08:22:52Z] peak memory of this run: 26021888 bytes
[2026-11-19T08:22:52Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

### 2.6 After the BLOCK — §3.9's copy and §9

**§3.9's copy** — `80-live-copy.log`. Every log of the live host is on the capture host, byte for byte: `scp exit=0`,
`diff exit=0`.

```
2026-11-19T08:25:59.521225762Z
scp exit=0
diff exit=0
total 20
drwxr-xr-x 2 root root 4096 Nov 19 08:26 .
drwxr-xr-x 5 root root 4096 Nov 19 08:26 ..
-rw-r--r-- 1 root root 6659 Nov 19 08:26 40-host-before.log
-rw-r--r-- 1 root root 1805 Nov 19 08:26 41-geoblock.log
```

**§9, B-RECLAIM-LIVE**, run by the Executor, its instant read in the same call:

```
$ date -u +%FT%T.%NZ; ssh -T -o BatchMode=yes -o ConnectTimeout=20 -o LogLevel=QUIET live-host 'rm -rf /root/tz48-work; test -e /root/tz48-work; echo "exit=$?"'
2026-11-19T08:26:39.681933346Z
exit=1
```

**§9, B-RECLAIM-OWN**, with `I0` in place of `I` and without its `git worktree remove` line, as §3 says for a BLOCK
before §3.1. Its output was written to no file and is quoted from the session, every line:

```
$ (cd /root/tz48-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz48-work/stage/research/tz48-live-host.py reclaim /root/tz48-work); echo "reclaim exit=$?"
[2026-11-19T08:28:30Z] R copied 7ae150e33f0be941cdcf0bbdc19dd4d402b40f1e4072f90ed8e14e7ec9035e86 /root/btc-forensics/tz48-work--live-logs--40-host-before.log
[2026-11-19T08:28:30Z] R copied 7e4566e7b0d22d2061a3ec9048ff7cbe368e9b041ed9d5393976441789854a0e /root/btc-forensics/tz48-work--live-logs--41-geoblock.log
[2026-11-19T08:28:30Z] R copied cf6bf23680b9fd3b2582ba09d5b1cfeaaa14982fb4ebe409539e6f4c92258541 /root/btc-forensics/tz48-work--logs--00-ready.log
[2026-11-19T08:28:30Z] R copied 5345fb96d5818b8d47a18b3763feebff2f66f24b794387ded522089ce1e10bab /root/btc-forensics/tz48-work--logs--01-stage.log
[2026-11-19T08:28:30Z] R copied e380bbd9c8e449b6cdf23cbd1e5eac065dd08d0ed2e5481bb63a778427fc73ef /root/btc-forensics/tz48-work--logs--02-fingerprint.log
[2026-11-19T08:28:30Z] R copied 8ce578e28f81e1ca70ed8761bc454e1d2f4b2c61fd0e4a1b837ed23ef55c85f7 /root/btc-forensics/tz48-work--logs--03-host-gate.log
[2026-11-19T08:28:30Z] R copied 18ef05129b76a9a0503f361357bef255a56315368560c5f4246b0bf5f19f3877 /root/btc-forensics/tz48-work--logs--04-room.log
[2026-11-19T08:28:30Z] R copied 07481fd6fa846e5895db098857737daee2d344776773a79147e352149843c054 /root/btc-forensics/tz48-work--logs--05-number.log
[2026-11-19T08:28:30Z] R copied 0b8a1f41de450353f7ff1e8e2aba08f01ac4648e777f8e479a4f2868ef1a9243 /root/btc-forensics/tz48-work--logs--05-refs.log
[2026-11-19T08:28:30Z] R copied f4cf0bba419df66461032860a741994159d48dd0ddd625a91417b1a6aa3090c8 /root/btc-forensics/tz48-work--logs--06-access.log
[2026-11-19T08:28:30Z] R copied 9b1cab0d61ae41aa73391beda432846cdbbc874cdb2980ade6934eca1c88e5a8 /root/btc-forensics/tz48-work--logs--07-copy.log
[2026-11-19T08:28:30Z] R copied a75306e6981ccf637abf75cabc998e8b478137b5fadb8af148176807adb7aa9b /root/btc-forensics/tz48-work--logs--80-live-copy.log
[2026-11-19T08:28:30Z] R copied b3b2cd4b595e79dcfba2a2b5ca5955348417cd11069f1ee096589dedd474250f /root/btc-forensics/tz48-work--stage--research--tz48-live-host.py
[2026-11-19T08:28:30Z] RECLAIM PASS: 13 files considered, 13 copied, 0 already held; the forensic store 2579 -> 2592 files
[2026-11-19T08:28:30Z] peak memory of this run: 26419200 bytes
[2026-11-19T08:28:30Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
reclaim exit=0
$ cd /root/btc-5m-twap; rm -rf /root/tz48-work; echo "exit=$?"
exit=0
$ test -e /root/tz48-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       bea33af [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
2592
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10503544832
```

`RECLAIM PASS`, 13 of 13 copied, before the removals; `/root/tz48-work` gone, `test -e` `exit=1`, on both hosts
(V18). The worktrees are map §3's two, the primary checkout and `/root/btc-recorder-svc`. The forensic store holds
2,592 files, 2,579 at §0.3 plus these 13. 10,503,544,832 bytes are free on `/var/lib`. No line was refused by the
classifier.

### 2.7 The files of this run

Every regular file of `/root/tz48-work` after §3.9's copy, its last write at 08:26 UTC, and before B-RECLAIM-OWN, each
hashed by the Executor's own read; `reclaim` copied each one into the forensic
store by exclusive create and checked its hash (§2.6):

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `live-logs/40-host-before.log` | 48 | 6,659 | `7ae150e33f0be941cdcf0bbdc19dd4d402b40f1e4072f90ed8e14e7ec9035e86` |
| `live-logs/41-geoblock.log` | 21 | 1,805 | `7e4566e7b0d22d2061a3ec9048ff7cbe368e9b041ed9d5393976441789854a0e` |
| `logs/00-ready.log` | 2 | 220 | `cf6bf23680b9fd3b2582ba09d5b1cfeaaa14982fb4ebe409539e6f4c92258541` |
| `logs/01-stage.log` | 3 | 171 | `5345fb96d5818b8d47a18b3763feebff2f66f24b794387ded522089ce1e10bab` |
| `logs/02-fingerprint.log` | 75 | 12,414 | `e380bbd9c8e449b6cdf23cbd1e5eac065dd08d0ed2e5481bb63a778427fc73ef` |
| `logs/03-host-gate.log` | 73 | 2,050 | `8ce578e28f81e1ca70ed8761bc454e1d2f4b2c61fd0e4a1b837ed23ef55c85f7` |
| `logs/04-room.log` | 8 | 681 | `18ef05129b76a9a0503f361357bef255a56315368560c5f4246b0bf5f19f3877` |
| `logs/05-number.log` | 6 | 434 | `07481fd6fa846e5895db098857737daee2d344776773a79147e352149843c054` |
| `logs/05-refs.log` | 19 | 1,292 | `0b8a1f41de450353f7ff1e8e2aba08f01ac4648e777f8e479a4f2868ef1a9243` |
| `logs/06-access.log` | 14 | 422 | `f4cf0bba419df66461032860a741994159d48dd0ddd625a91417b1a6aa3090c8` |
| `logs/07-copy.log` | 5 | 195 | `9b1cab0d61ae41aa73391beda432846cdbbc874cdb2980ade6934eca1c88e5a8` |
| `logs/80-live-copy.log` | 8 | 267 | `a75306e6981ccf637abf75cabc998e8b478137b5fadb8af148176807adb7aa9b` |
| `stage/research/tz48-live-host.py` | 1,855 | 94,715 | `b3b2cd4b595e79dcfba2a2b5ca5955348417cd11069f1ee096589dedd474250f` |

**Peaks**, each under `35,389,918` (V17): `fingerprint` 26,939,392; `room` 26,021,888; `number` 26,152,960; `refs`
26,021,888; `host before` 26,714,112 and `geoblock` 29,990,912 on the live host; `reclaim` 26,419,200.
**Every free-space and `MemAvailable` read, with its instant and its bound:** §0.0's session read at 08:21:55,
`10,512,760,832` and `274,083,840`, and its logged read at 08:22:10, `10,512,429,056` and `270,249,984`, against
`7,795,535,636` and `70,779,836`; §0.3 at 08:22:27, `10,511,978,496` and `298,237,952`, the same bounds; `room` at
08:22:36, `10,511,769,600` and `283,869,184`, the same bounds; `host before` at 08:23:42, `16,989,290,496` on the live
host's `/` against `3,589,660,928` and `1,508,622,336` against `70,779,836`; and §9's last `df`, after 08:28:30, `10,503,544,832` (§2.6).

---

## 3. Departures, named

1. **G-GEO's IPv6 error is known by its type alone.** `geo_read` prints `type(exc).__name__`, so the errno and its
   message are not in the log. The host's IPv6 routes and addresses were not read: they are the host's address, which
   §2 item 5 keeps out of every print.
2. **The refs differ from §0.5's read in two kinds**, named in §2.5: `rewardbook-streams-*` 46 against 43, and `main` at
   `bea33af` against `11cf0e2`. Recorded, not BLOCKING, as §0.5 says.
3. **`host before` printed state that no gate of this run read, because none after G-GEO ran** (§2.2). A swap that
   existed before this TZ: `/swap.img`, `file`, `1,048,572` KiB, with its own `fstab` line
   `/swap.img none swap sw 0 0`, and `/swapfile` absent. `vm.swappiness` `60`. A journald drop-in that existed
   before it: `/etc/systemd/journald.conf.d/cap.conf`, with `SystemMaxUse` `200M` in force from it, and
   `ForwardToSyslog` `yes` from Ubuntu's `syslog.conf`. rsyslog active and enabled. `sshd` with
   `permitrootlogin yes` and `passwordauthentication yes`.
4. **One address is in this report, and it belongs to neither host.** `40-host-before.log`'s `CLOCK timesync-status`
   line prints `timedatectl timesync-status`'s `Server:` line: the NTP server's address beside its name,
   `ntp.ubuntu.com`. It is quoted as written. §2 item 5 forbids an address of either host.
5. **Steps that did not run, as §3 says for a BLOCK:** §3.1 to §3.8 — so no branch, no self-test, §3.3's `scratch`
   and B-RECLAIM-SCRATCH, G-NET, G-LAT, the disk, B-CONFIGURE, `verify` and `host after` — and §3.9's closing reads and
   contract §4.2's self-check. §3 sends a BLOCK to §3.9's copy and §9 alone. The session directories beside this
   session's own are left as they were, for the next TZ's `scratch`.
6. **§9's two blocks are quoted from the session.** B-RECLAIM-OWN's output goes to no file, as §9 says. B-RECLAIM-LIVE
   has no log in §3's table either. B-RECLAIM-OWN ran with `I0` in place of `I` and without its `git worktree remove`
   line, because no worktree was made. Its removal line ran after `cd /root/btc-5m-twap`, the first half of the
   line left out, so that `rm -rf` did not run from inside the tree it removes.
