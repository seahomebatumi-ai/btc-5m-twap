# TZ-49 — the live host, IPv4 alone and root by key alone — REPORT

**Status: executed as written. §4.9: KEEP** — G-GEO, G-SPEC and G-NET read PASS. Every gate of §4 read PASS:

- **G-GEO PASS over IPv4 alone** (`41-geoblock.log`, 13:56:54 UTC on 2026-11-19), at the first read. Status `200`,
  `blocked False`, `country 'BG'`, `region '22'`, and the address the venue saw was the connection's own. IPv6's state
  was printed beside it and read by no gate: 1 global address, 2 default routes, 0 usable. The process opened no IPv6
  socket.
- **G-SSH PASS, 6 of 6.** B-SSH was run by the Executor at 13:57:19 UTC. C-SSH read `CONFIRMED` at 13:57:30 UTC, at
  its first read, so **B-SSH was kept**. `sshd -T` reads `passwordauthentication no`, `kbdinteractiveauthentication
  no`, `permitrootlogin without-password` and `pubkeyauthentication yes`. From outside, the methods offered to a
  connection that offers no key went from `publickey,password` to `publickey`. **Root on the live host now logs in
  over SSH by key alone.**
- **G-SPEC PASS: 2 of 2**, before and after the changes.
- **G-NET PASS: 3 of 3**, each check at its first read, through Cloudflare's Sofia data centre, `SOF`. All 60 TCP
  handshakes with the CLOB's edge completed, with a median of 0.917 ms.
- **G-LAT PASS:** 600 of 600 counted replies valid. Their nearest-rank median time to the first byte was
  **56.296 ms**, against the bound of 100.000 ms, so the one-way bound is **28.148 ms against 50.000 ms**.
- **G-SWAP PASS: 7 of 7** — the host's own `/swap.img` adopted, no swap file written. **G-LOG PASS: 6 of 6** — the
  journal bounded at 512 MiB with 2 GiB kept free, rsyslog disabled and stopped.
- **The self-test passed on both hosts**, 51 of 51, `refused by the hook: 4` each. FINGERPRINT PASS, 62 of 62
  `frozen` rows; host gate 7 of 7; room margin **2,874,778,827** bytes; NUMBER PASS 2 of 2; refs 182 lines.
- **Branch** `tz-49-live-host-ipv4-keys` at `9515874e613de4987d490f8c4f5cd16fbca9b345`, one file, `2127 0`.
  **Pull request #47.** The §4.2 self-check read `0`, one path, nothing.
- **Kept on the live host — this TZ's deployment:** `/etc/ssh/sshd_config.d/00-btc-5m-twap.conf`,
  `/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf` and `/etc/sysctl.d/zz-btc-5m-twap-swap.conf`;
  `vm.swappiness` `10`; rsyslog disabled and stopped, its socket stopped. `/swap.img` was already `0600` and root's,
  so its mode and owner were not changed. The guard `tz49-ssh-revert.timer` was stopped by C-SSH; its timer and its
  service read `inactive` at the closing reads.
- **The capture host:** no unit started, stopped or touched, and no store written. The recorder, the reward book and
  the advisor kept the same `MainPID`, `NRestarts` and `ActiveState` from §0.3 to §3.9. The access TZ-47 made stood:
  `R true` read `exit=0` at its first read.
- **No block was handed to the Boss, and the classifier refused nothing.** Every command of the run, B-SSH,
  B-CONFIGURE, B-RECLAIM-SCRATCH's removals and §9's included, was run by the Executor.
- **No order, no key of any venue, no authenticated request, no money moved.** No address of either host, no password
  and no private key is in this report, and of the live host's name only its first label.

---

## 0. Fingerprint

`I0 fingerprint` (`logs/02-fingerprint.log`, 13:55:36 UTC) and `I fingerprint` from the branch's worktree
(`logs/12-fingerprint.log`, 13:57:55 UTC) each printed:

```
FINGERPRINT PASS: revision 2026-11-19-a; anchors 6 of 6, 4 re-derived; rows 65: frozen 62 of 62 equal, tracked 2, reported 1
```

**Revision string:** `2026-11-19-a`, equal to TZ-49's header. **Anchors**, map §0 against TZ-49's header, 6 of 6
equal; `A2`, `A4`, `A5` and `A6` re-derived by the instrument as the first 12 hex characters of their files' SHA-256,
4 of 4 equal:

| anchor | TZ-49 and map §0 | re-derived |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | — |
| `A2` — collector | `6c5089330629` | `research/twap-divergence.py` `6c5089330629`, equal |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | — |
| `A4` — executor contract | `6ac6e10aeabc` | `BTC-EXECUTOR-INSTRUCTIONS.md` `6ac6e10aeabc`, equal |
| `A5` — recorder | `0f6c90451cbd` | `research/recorder/recorder.py` `0f6c90451cbd`, equal |
| `A6` — pricer | `729f0bcdbee3` | `research/pfair.py` `729f0bcdbee3`, equal |

**Every row of map §0's table, 65 of 65, as `fingerprint` printed it** (`logs/02-fingerprint.log`): 62 `frozen`, each
equal to the map in lines, bytes and SHA-256; 2 `tracked`; 1 `reported`. The tree is the primary checkout
`/root/btc-5m-twap`, `main` at `a76d79f8ddb0a530a9dc6563d7e9cbd440520322`, which is `6e9e580` plus the upload of
TZ-49.

| path | `wc -l` | bytes | `sha256sum` | state |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 1,049 | 166,027 | `55c50ed23c506b614f93a7253fed0899237f0ab7d565739d72f801abd3e77d65` | reported |
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

**The model:** TZ-49 names Claude Opus 5.5. The session's own record read `claude-opus-5-5` as both the configured and
the last served model.

---

## 1. Input

- **Read:** `CryptoTZ/TZ-49-live-host-ipv4-keys.md`, 2,736 lines, 240,965 bytes, at `main` `a76d79f`. Its Appendix A
  was extracted by §0.1's script into the stage and again into the branch's worktree. Both copies are 2,127 lines,
  113,254 bytes, SHA-256 `efcc5ead077b396fe18d243f3c65fa9824baca56e6db5312058971e0dfe6049b` (`01-stage.log`,
  `11-worktree.log`), and so is the live host's copy (`07-copy.log`). Also read: `SYSTEM-MAP.md`'s §0 and every
  section, row and item TZ-49's header names; `BTC-EXECUTOR-INSTRUCTIONS.md`; and TZ-48's report.
- **Measured, nothing re-collected from a store:** the live host's state, the venue's geoblock from its address, the
  venue's CLOB, `/time` and market websocket, the latency and the disk. The reward book's store was read by the names
  and sizes of its directory entries alone, while its archive read `inactive` (`04-room.log`). The recorder's store was
  read only by §0.3's `find` and `grep -c`. No file of any capture store was opened, and no outcome, price, size or
  book of any market was read.
- **Requests made from the live host, all over IPv4 with `User-Agent: btc-5m-twap-tz49`:** 1 geoblock request, 2 for
  G-NET and 1 websocket handshake, 605 latency requests and 60 TCP handshakes. These are the modes' own counts:
  `requests 1`, `requests 2, handshakes 1, TCP connects 60` and `requests 605`. No other host was looked up, and the
  hook refused nothing in any live mode.

---

## 2. Measurements

Every log is quoted whole, as written. The live host's logs are quoted as §3.9's copy brought them back, byte for
byte (`diff exit=0`). Each log's SHA-256 is in §9's `reclaim` output (§2.12), and its copy in the forensic store is
`/root/btc-forensics/tz49-work--<path with / as -->`.

### 2.1 The geoblock — `41-geoblock.log`

```
2026-11-19T13:56:54.605104376Z
[2026-11-19T13:56:54Z] GEOBLOCK IPv4 read 1: https://polymarket.com/api/geoblock, status 200; blocked False, country 'BG', region '22'; reply keys ['blocked', 'country', 'ip', 'region']; the address the venue saw is this connection's own: True - PASS
[2026-11-19T13:56:54Z] GEOBLOCK IPv6, beside G-GEO and read by no gate - this process opens no IPv6 socket: {'global addresses': 1, 'their flags': ['80'], 'default routes': 2, 'usable': 0, 'usable via': []}
[2026-11-19T13:56:54Z] G-GEO PASS over IPv4 alone
[2026-11-19T13:56:54Z] RECORD geoblock {"ipv6":{"default routes":2,"global addresses":1,"their flags":["80"],"usable":0,"usable via":[]},"reading":"PASS"}
[2026-11-19T13:56:54Z] peak memory of this run: 30117888 bytes
[2026-11-19T13:56:54Z] refused by the hook: 0; lookups 1, requests 1, handshakes 0, TCP connects 0
exit=0
```

G-GEO PASS over IPv4 alone at the first read (V8). Of the reply the instrument printed `blocked`, `country`, `region`,
its keys and the comparison of the address the venue saw with the connection's own source address, which read `True`.
It printed nothing of the address itself. IPv6 was read from the kernel's tables and printed beside the reading: 1
global address with flags `80`, 2 default routes and 0 usable — no IPv6 route is up and not a reject route. No IPv6
socket was opened: `lookups 1, requests 1`.

### 2.2 Root by key alone — §0.7

**Who ran B-SSH and when:** the Executor, as `R 'bash /root/tz49-work/files/b-ssh.sh'`. Its log opens at
13:57:19.333 UTC and its `R` returned `exit=0`. C-SSH was run at once after it, read `CONFIRMED` at its first read at
13:57:30.897 UTC, and stopped the guard. No paste was handed over.

**The methods, from outside** — `08-methods.log`, both reads, before B-SSH and after it:

```
2026-11-19T13:57:00.545291965Z
[2026-11-19T13:57:01Z] METHODS before B-SSH: the methods the live host's sshd offers root, from outside: ['publickey,password']; ssh exit 255
[2026-11-19T13:57:01Z] RECORD methods-before {"exit":255,"methods":["publickey,password"]}
[2026-11-19T13:57:01Z] peak memory of this run: 26939392 bytes
[2026-11-19T13:57:01Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
2026-11-19T13:57:39.840662198Z
[2026-11-19T13:57:40Z] METHODS after B-SSH: the methods the live host's sshd offers root, from outside: ['publickey']; ssh exit 255
[2026-11-19T13:57:40Z] RECORD methods-after {"exit":255,"methods":["publickey"]}
[2026-11-19T13:57:40Z] G-SSH K6 publickey alone, from outside: PASS
[2026-11-19T13:57:40Z] peak memory of this run: 26546176 bytes
[2026-11-19T13:57:40Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

**`files`** — `42-files.log`. The four files were each asserted to their SHA-256 before and after the write: the sshd
drop-in, `94fff8f1…`, 340 bytes; the journald file, `91c7364c…`, 448 bytes; the sysctl file, `3b31709b…`, 210 bytes;
and B-SSH, `906a6cb2…`, 35 lines, 1,746 bytes.

```
2026-11-19T13:57:07.381460356Z
[2026-11-19T13:57:07Z] MemAvailable read 1: 1497681920 bytes, floor 72439812
[2026-11-19T13:57:07Z] available on /: 16987742208 bytes, floor 2515919104
[2026-11-19T13:57:07Z] FILES sshd.conf 6 lines 340 bytes sha256 94fff8f1f044b31d393eecf24700dabc5b7316c70a37d0f3984cbc5957563624
[2026-11-19T13:57:07Z] FILES journald.conf 11 lines 448 bytes sha256 91c7364c9ee1dec70c1651e7c976546d86a46f95b39ea8dd369ef83589439200
[2026-11-19T13:57:07Z] FILES sysctl.conf 3 lines 210 bytes sha256 3b31709b0c1c7026c71013150868a982296a36daa7b3635fd9eabe4929331a04
[2026-11-19T13:57:07Z] FILES b-ssh.sh 35 lines 1746 bytes sha256 906a6cb2685aea2575eff6538906aa02a21d9591a6d9aa3505f84b644693ede1
[2026-11-19T13:57:07Z] peak memory of this run: 27496448 bytes
[2026-11-19T13:57:07Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

**B-SSH** — `43-B-SSH.log`, whole. `sshd_config.d` held the provider's `01-xserver.conf` alone. `sshd_config` includes
the directory at its line 12, before its own `PermitRootLogin yes` at line 42, so the drop-in, sorted first, wins.

```
2026-11-19T13:57:19.333470763Z
total 12
drwxr-xr-x 2 root root 4096 ноя 18 09:49 .
drwxr-xr-x 4 root root 4096 ноя 18 09:49 ..
-rw-r--r-- 1 root root   20 ноя 18 09:49 01-xserver.conf
12:Include /etc/ssh/sshd_config.d/*.conf
42:PermitRootLogin yes
71:KbdInteractiveAuthentication no
files/sshd.conf: OK
guard armed: 300 s from now the drop-in is removed and sshd reloaded, unless a new connection stops it
port 22
permitrootlogin without-password
pubkeyauthentication yes
passwordauthentication no
kbdinteractiveauthentication no
B-SSH exit=0
```

**C-SSH** — `09-B-SSH-confirm.log`, whole: one read, `CONFIRMED`. **B-SSH kept.**

```
2026-11-19T13:57:30.896828751Z
CONFIRMED: a new connection by the key reached the host after the reload; the guard stopped, exit=0; the drop-in present
R exit=0
```

**G-SSH on the live host** — `44-sshd.log`, whole: K1 to K5, 5 of 5.

```
2026-11-19T13:57:39.712143191Z
[2026-11-19T13:57:39Z] SSHD /etc/ssh/sshd_config.d/00-btc-5m-twap.conf ('94fff8f1f044b31d393eecf24700dabc5b7316c70a37d0f3984cbc5957563624', '0o644'); sshd -T exit 0: ['passwordauthentication no', 'kbdinteractiveauthentication no', 'permitrootlogin without-password', 'pubkeyauthentication yes']
[2026-11-19T13:57:39Z] SSHD set in its files, in the order sshd reads them: ['/etc/ssh/sshd_config:12: Include /etc/ssh/sshd_config.d/*.conf', '/etc/ssh/sshd_config:42: PermitRootLogin yes', '/etc/ssh/sshd_config:71: KbdInteractiveAuthentication no', '/etc/ssh/sshd_config.d/00-btc-5m-twap.conf:4: PasswordAuthentication no', '/etc/ssh/sshd_config.d/00-btc-5m-twap.conf:5: KbdInteractiveAuthentication no', '/etc/ssh/sshd_config.d/00-btc-5m-twap.conf:6: PermitRootLogin prohibit-password', '/etc/ssh/sshd_config.d/01-xserver.conf:1: PermitRootLogin yes']
[2026-11-19T13:57:39Z] G-SSH K1 the sshd drop-in: PASS
[2026-11-19T13:57:39Z] G-SSH K2 passwordauthentication no: PASS
[2026-11-19T13:57:39Z] G-SSH K3 kbdinteractiveauthentication no: PASS
[2026-11-19T13:57:39Z] G-SSH K4 permitrootlogin without-password: PASS
[2026-11-19T13:57:39Z] G-SSH K5 pubkeyauthentication yes: PASS
[2026-11-19T13:57:39Z] G-SSH on the live host PASS: 5 of 5
[2026-11-19T13:57:39Z] RECORD sshd {"in force":{"kbdinteractiveauthentication":"no","passwordauthentication":"no","permitrootlogin":"without-password","pubkeyauthentication":"yes"},"reading":true}
[2026-11-19T13:57:39Z] peak memory of this run: 27496448 bytes
[2026-11-19T13:57:39Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

**G-SSH:** K1 to K5 PASS on the live host, and K6 `publickey` alone from outside: **PASS, 6 of 6** (V19). After
`CONFIRMED`, every `R` of the run was itself a new connection by the key under the new configuration, and every one
returned.

### 2.3 The live host — `host before` and `host after`

**`40-host-before.log`**, whole — the live host gate and its floors:

```
2026-11-19T13:56:44.419447372Z
[2026-11-19T13:56:44Z] LH1 hostname vs-2348: PASS
[2026-11-19T13:56:44Z] LH2 Ubuntu 24.04: PASS
[2026-11-19T13:56:44Z] LH3 Python 3.12: PASS
[2026-11-19T13:56:44Z] LH4 not the capture host: PASS
[2026-11-19T13:56:44Z] LH5 the host key pinned at TZ-47's first connection: PASS
[2026-11-19T13:56:44Z] HOST its SSH host keys: [('ecdsa-sha2-nistp256', 'SHA256:717ijbIvj026Fy6VpHg2IBIeCLa2aPu/IsGNHneAITA'), ('ssh-ed25519', 'SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw'), ('ssh-rsa', 'SHA256:LzqPSbHCa+VWhcazHny+A19sCqjzuUUGf9nWWTTfYAY')]
[2026-11-19T13:56:44Z] MemAvailable read 1: 1502191616 bytes, floor 72439812
[2026-11-19T13:56:44Z] available on /: 16987779072 bytes, floor 2515919104
[2026-11-19T13:56:44Z] HOST vs-2348; Ubuntu 24.04.5 LTS; kernel 6.8.0-138-generic x86_64; Python 3.12.3; processors 1, Intel(R) Xeon(R) Gold 6248R CPU @ 3.00GHz
[2026-11-19T13:56:44Z] HOST vendor 'VMware, Inc.', product 'VMware20,1'
[2026-11-19T13:56:44Z] HOST booted 2026-11-18T16:57:40Z, up 75544 s
[2026-11-19T13:56:44Z] MEMORY MemTotal 1944465408, MemAvailable 1502199808, MemFree 935780352, Buffers 70688768, Cached 614973440, SwapTotal 1073737728, SwapFree 1073737728
[2026-11-19T13:56:44Z] DISK / /dev/mapper/lvm-root ext4: total 20779339776, available 16987779072, free 17216577536 bytes; inodes 1294336, free 1208073
[2026-11-19T13:56:44Z] SWAP /proc/swaps [('/swap.img', 'file', 1048572, 0)]; /swap.img (regular, bytes, mode, uid) (True, 1073741824, '0o600', 0); fstab lines of swap [('/swap.img', 'none', 'swap', 'sw', '0', '0')]
[2026-11-19T13:56:44Z] SWAP swap.img.swap {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'active', 'SourcePath': '/etc/fstab'}
[2026-11-19T13:56:44Z] SWAP vm.swappiness 60; set in []
[2026-11-19T13:56:44Z] JOURNALD /etc/systemd/journald.conf.d: ['cap.conf']
[2026-11-19T13:56:44Z] JOURNALD /usr/lib/systemd/journald.conf.d: ['syslog.conf']
[2026-11-19T13:56:44Z] JOURNALD journald.conf, set: ['[Journal]']
[2026-11-19T13:56:44Z] JOURNALD in force, by `systemd-analyze cat-config` exit 0: {'SystemMaxUse': ('200M', '/etc/systemd/journald.conf.d/cap.conf'), 'ForwardToSyslog': ('yes', '/usr/lib/systemd/journald.conf.d/syslog.conf')}
[2026-11-19T13:56:44Z] JOURNALD disk usage: Archived and active journals take up 42.2M in the file system.
[2026-11-19T13:56:44Z] LOGS /var/log: 33 files, 80011934 bytes apparent, 57257984 on disk; the largest on disk [(9900032, 'journal/ef7f4459e2364097b06322e174690e1c/system@cdcaa05a03bc459cad6b13a19ceb7601-000000000000187a-0006608fe8d3dc1d.journal'), (9625600, 'journal/ef7f4459e2364097b06322e174690e1c/system@cdcaa05a03bc459cad6b13a19ceb7601-0000000000004cb1-0006609449653fc7.journal'), (9613312, 'journal/ef7f4459e2364097b06322e174690e1c/system@cdcaa05a03bc459cad6b13a19ceb7601-0000000000007d03-00066097fbd2be99.journal'), (8392704, 'journal/ef7f4459e2364097b06322e174690e1c/system.journal'), (6750208, 'journal/ef7f4459e2364097b06322e174690e1c/system@7e96aa5e1c8641b4a9dfcabd6f967967-0000000000000464-00066089ee97e00c.journal'), (5976064, 'btmp'), (5185536, 'auth.log'), (737280, 'syslog')]
[2026-11-19T13:56:44Z] UNIT rsyslog.service {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'}
[2026-11-19T13:56:44Z] UNIT syslog.socket {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'static'}
[2026-11-19T13:56:44Z] UNIT systemd-journald.service {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'static'}
[2026-11-19T13:56:44Z] UNIT systemd-timesyncd.service {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'}
[2026-11-19T13:56:44Z] UNIT chrony.service {'LoadState': 'not-found', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': ''}
[2026-11-19T13:56:44Z] UNIT ssh.service {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'disabled'}
[2026-11-19T13:56:44Z] UNIT ssh.socket {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'}
[2026-11-19T13:56:44Z] UNIT unattended-upgrades.service {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'}
[2026-11-19T13:56:44Z] UNIT apt-daily.timer {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-19T13:56:44Z] UNIT apt-daily-upgrade.timer {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-19T13:56:44Z] CLOCK {'Timezone': 'Etc/UTC', 'LocalRTC': 'no', 'CanNTP': 'yes', 'NTP': 'yes', 'NTPSynchronized': 'yes'}
[2026-11-19T13:56:44Z] CLOCK timesync-status exit 0: Server: 185.125.190.57 (ntp.ubuntu.com) | Poll interval: 34min 8s (min: 32s; max 34min 8s) | Leap: normal | Version: 4 | Stratum: 2 | Reference: 91EE5050 | Precision: 1us (-25) | Root distance: 5.668ms (max: 5s) | Offset: -1.783ms | Delay: 38.022ms | Jitter: 1.281ms | Packet count: 42 | Frequency: +33.194ppm
[2026-11-19T13:56:44Z] SSHD -T exit 0: ['port 22', 'permitrootlogin yes', 'pubkeyauthentication yes', 'passwordauthentication yes', 'kbdinteractiveauthentication no']
[2026-11-19T13:56:44Z] SSHD set in its files, in the order sshd reads them: ['/etc/ssh/sshd_config:12: Include /etc/ssh/sshd_config.d/*.conf', '/etc/ssh/sshd_config:42: PermitRootLogin yes', '/etc/ssh/sshd_config:71: KbdInteractiveAuthentication no', '/etc/ssh/sshd_config.d/01-xserver.conf:1: PermitRootLogin yes']
[2026-11-19T13:56:44Z] SSHD authorized keys of root: [('ssh-ed25519', 'SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo')]
[2026-11-19T13:56:44Z] SOCKETS listening or bound: ['tcp any:22 systemd', 'tcp loopback:53 systemd-resolve', 'tcp6 any:22 systemd', 'udp any:57775 ?', 'udp loopback:53 systemd-resolve', 'udp6 any:57775 ?']
[2026-11-19T13:56:44Z] NETWORK IPv6, never an address: {'global addresses': 1, 'their flags': ['80'], 'default routes': 2, 'usable': 0, 'usable via': []}
[2026-11-19T13:56:44Z] PROCESSES by resident memory: ['multipathd 363 27987968', 'python3 25367 27738112', 'systemd-journal 303 25784320', 'unattended-upgr 712 23896064', 'udisksd 692 13889536', 'systemd 1 13627392', 'systemd-resolve 534 13320192', 'ModemManager 730 13238272', 'VGAuthService 626 12578816', 'systemd 1316 11841536']
[2026-11-19T13:56:44Z] UPGRADES Automatic-Reboot set: nowhere - the package's default
[2026-11-19T13:56:44Z] G-SPEC MemTotal at least 1800000000: 1944465408, PASS
[2026-11-19T13:56:44Z] G-SPEC the root file system at least 18000000000: 20779339776, PASS
[2026-11-19T13:56:44Z] G-SPEC PASS: 2 of 2
[2026-11-19T13:56:44Z] RECORD host-before {"disk_available":16987779072,"disk_total":20779339776,"mem_available":1502199808,"mem_total":1944465408,"spec":true,"swap_total":1073737728,"swaps":[["/swap.img","file",1048572,0]]}
[2026-11-19T13:56:44Z] peak memory of this run: 27635712 bytes
[2026-11-19T13:56:44Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

**`62-host-after.log`**, whole:

```
2026-11-19T14:08:34.203950494Z
[2026-11-19T14:08:34Z] LH1 hostname vs-2348: PASS
[2026-11-19T14:08:34Z] LH2 Ubuntu 24.04: PASS
[2026-11-19T14:08:34Z] LH3 Python 3.12: PASS
[2026-11-19T14:08:34Z] LH4 not the capture host: PASS
[2026-11-19T14:08:34Z] LH5 the host key pinned at TZ-47's first connection: PASS
[2026-11-19T14:08:34Z] HOST its SSH host keys: [('ecdsa-sha2-nistp256', 'SHA256:717ijbIvj026Fy6VpHg2IBIeCLa2aPu/IsGNHneAITA'), ('ssh-ed25519', 'SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw'), ('ssh-rsa', 'SHA256:LzqPSbHCa+VWhcazHny+A19sCqjzuUUGf9nWWTTfYAY')]
[2026-11-19T14:08:34Z] HOST vs-2348; Ubuntu 24.04.5 LTS; kernel 6.8.0-138-generic x86_64; Python 3.12.3; processors 1, Intel(R) Xeon(R) Gold 6248R CPU @ 3.00GHz
[2026-11-19T14:08:34Z] HOST vendor 'VMware, Inc.', product 'VMware20,1'
[2026-11-19T14:08:34Z] HOST booted 2026-11-18T16:57:40Z, up 76254 s
[2026-11-19T14:08:34Z] MEMORY MemTotal 1944465408, MemAvailable 1500663808, MemFree 931774464, Buffers 71815168, Cached 616128512, SwapTotal 1073737728, SwapFree 1073737728
[2026-11-19T14:08:34Z] DISK / /dev/mapper/lvm-root ext4: total 20779339776, available 16987541504, free 17216339968 bytes; inodes 1294336, free 1208055
[2026-11-19T14:08:34Z] SWAP /proc/swaps [('/swap.img', 'file', 1048572, 0)]; /swap.img (regular, bytes, mode, uid) (True, 1073741824, '0o600', 0); fstab lines of swap [('/swap.img', 'none', 'swap', 'sw', '0', '0')]
[2026-11-19T14:08:34Z] SWAP swap.img.swap {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'active', 'SourcePath': '/etc/fstab'}
[2026-11-19T14:08:34Z] SWAP vm.swappiness 10; set in ['/etc/sysctl.d/zz-btc-5m-twap-swap.conf: vm.swappiness = 10']
[2026-11-19T14:08:34Z] JOURNALD /etc/systemd/journald.conf.d: ['cap.conf', 'zz-btc-5m-twap-limits.conf']
[2026-11-19T14:08:34Z] JOURNALD /usr/lib/systemd/journald.conf.d: ['syslog.conf']
[2026-11-19T14:08:34Z] JOURNALD journald.conf, set: ['[Journal]']
[2026-11-19T14:08:34Z] JOURNALD in force, by `systemd-analyze cat-config` exit 0: {'SystemMaxUse': ('512M', '/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf'), 'ForwardToSyslog': ('no', '/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf'), 'Storage': ('persistent', '/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf'), 'SystemKeepFree': ('2G', '/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf'), 'SystemMaxFileSize': ('64M', '/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf'), 'RuntimeMaxUse': ('64M', '/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf')}
[2026-11-19T14:08:34Z] JOURNALD disk usage: Archived and active journals take up 42.2M in the file system.
[2026-11-19T14:08:34Z] LOGS /var/log: 33 files, 80095224 bytes apparent, 57339904 on disk; the largest on disk [(9900032, 'journal/ef7f4459e2364097b06322e174690e1c/system@cdcaa05a03bc459cad6b13a19ceb7601-000000000000187a-0006608fe8d3dc1d.journal'), (9625600, 'journal/ef7f4459e2364097b06322e174690e1c/system@cdcaa05a03bc459cad6b13a19ceb7601-0000000000004cb1-0006609449653fc7.journal'), (9613312, 'journal/ef7f4459e2364097b06322e174690e1c/system@cdcaa05a03bc459cad6b13a19ceb7601-0000000000007d03-00066097fbd2be99.journal'), (8392704, 'journal/ef7f4459e2364097b06322e174690e1c/system.journal'), (6750208, 'journal/ef7f4459e2364097b06322e174690e1c/system@7e96aa5e1c8641b4a9dfcabd6f967967-0000000000000464-00066089ee97e00c.journal'), (6012928, 'btmp'), (5226496, 'auth.log'), (741376, 'syslog')]
[2026-11-19T14:08:34Z] UNIT rsyslog.service {'LoadState': 'loaded', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'disabled'}
[2026-11-19T14:08:34Z] UNIT syslog.socket {'LoadState': 'loaded', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-11-19T14:08:34Z] UNIT systemd-journald.service {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'static'}
[2026-11-19T14:08:34Z] UNIT systemd-timesyncd.service {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'}
[2026-11-19T14:08:34Z] UNIT chrony.service {'LoadState': 'not-found', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': ''}
[2026-11-19T14:08:34Z] UNIT ssh.service {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'disabled'}
[2026-11-19T14:08:34Z] UNIT ssh.socket {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'}
[2026-11-19T14:08:34Z] UNIT unattended-upgrades.service {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'}
[2026-11-19T14:08:34Z] UNIT apt-daily.timer {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-19T14:08:34Z] UNIT apt-daily-upgrade.timer {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-19T14:08:34Z] CLOCK {'Timezone': 'Etc/UTC', 'LocalRTC': 'no', 'CanNTP': 'yes', 'NTP': 'yes', 'NTPSynchronized': 'yes'}
[2026-11-19T14:08:34Z] CLOCK timesync-status exit 0: Server: 185.125.190.57 (ntp.ubuntu.com) | Poll interval: 34min 8s (min: 32s; max 34min 8s) | Leap: normal | Version: 4 | Stratum: 2 | Reference: 91EE5050 | Precision: 1us (-25) | Root distance: 5.156ms (max: 5s) | Offset: +1.852ms | Delay: 35.306ms | Jitter: 1.540ms | Packet count: 43 | Frequency: +33.646ppm
[2026-11-19T14:08:34Z] SSHD -T exit 0: ['port 22', 'permitrootlogin without-password', 'pubkeyauthentication yes', 'passwordauthentication no', 'kbdinteractiveauthentication no']
[2026-11-19T14:08:34Z] SSHD set in its files, in the order sshd reads them: ['/etc/ssh/sshd_config:12: Include /etc/ssh/sshd_config.d/*.conf', '/etc/ssh/sshd_config:42: PermitRootLogin yes', '/etc/ssh/sshd_config:71: KbdInteractiveAuthentication no', '/etc/ssh/sshd_config.d/00-btc-5m-twap.conf:4: PasswordAuthentication no', '/etc/ssh/sshd_config.d/00-btc-5m-twap.conf:5: KbdInteractiveAuthentication no', '/etc/ssh/sshd_config.d/00-btc-5m-twap.conf:6: PermitRootLogin prohibit-password', '/etc/ssh/sshd_config.d/01-xserver.conf:1: PermitRootLogin yes']
[2026-11-19T14:08:34Z] SSHD authorized keys of root: [('ssh-ed25519', 'SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo')]
[2026-11-19T14:08:34Z] SOCKETS listening or bound: ['tcp any:22 systemd', 'tcp loopback:53 systemd-resolve', 'tcp6 any:22 systemd', 'udp any:57775 ?', 'udp loopback:53 systemd-resolve', 'udp6 any:57775 ?']
[2026-11-19T14:08:34Z] NETWORK IPv6, never an address: {'global addresses': 1, 'their flags': ['80'], 'default routes': 2, 'usable': 0, 'usable via': []}
[2026-11-19T14:08:34Z] PROCESSES by resident memory: ['multipathd 363 27987968', 'python3 26571 27754496', 'unattended-upgr 712 23896064', 'systemd 1 13938688', 'udisksd 692 13889536', 'systemd-resolve 534 13320192', 'ModemManager 730 13238272', 'VGAuthService 626 12578816', 'systemd-journal 26407 12337152', 'systemd 1316 11841536']
[2026-11-19T14:08:34Z] UPGRADES Automatic-Reboot set: nowhere - the package's default
[2026-11-19T14:08:34Z] G-SPEC MemTotal at least 1800000000: 1944465408, PASS
[2026-11-19T14:08:34Z] G-SPEC the root file system at least 18000000000: 20779339776, PASS
[2026-11-19T14:08:34Z] G-SPEC PASS: 2 of 2
[2026-11-19T14:08:34Z] RECORD host-after {"disk_available":16987541504,"disk_total":20779339776,"mem_available":1500663808,"mem_total":1944465408,"spec":true,"swap_total":1073737728,"swaps":[["/swap.img","file",1048572,0]]}
[2026-11-19T14:08:34Z] peak memory of this run: 27631616 bytes
[2026-11-19T14:08:34Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

**Side by side, where they differ** — every other line is equal. The five gate checks, the host keys, the host's
kernel, processors and vendor, the boot, the swap's lines, the units but rsyslog's two, the clock's NTP state, root's
authorized key, the sockets, IPv6's state, `Automatic-Reboot` and G-SPEC all read the same:

| line | `host before`, 13:56:44 UTC | `host after`, 14:08:34 UTC |
|---|---|---|
| the floors | `MemAvailable` `1,502,191,616` against `72,439,812`; `/` `16,987,779,072` available against `2,515,919,104` | not read: `host after` reads no floors |
| up | `75544 s` | `76254 s` |
| `MemAvailable` | `1,502,199,808` | `1,500,663,808` |
| `/` available; inodes free | `16,987,779,072`; `1,208,073` | `16,987,541,504`; `1,208,055` |
| `vm.swappiness` | `60`, set in no file | `10`, from `/etc/sysctl.d/zz-btc-5m-twap-swap.conf` |
| `journald.conf.d` under `/etc` | `cap.conf` | `cap.conf`, `zz-btc-5m-twap-limits.conf` |
| journald in force | `SystemMaxUse` `200M` from `cap.conf`; `ForwardToSyslog` `yes` from `syslog.conf` | all six keys from `zz-btc-5m-twap-limits.conf`: `SystemMaxUse` `512M`, `ForwardToSyslog` `no`, `Storage` `persistent`, `SystemKeepFree` `2G`, `SystemMaxFileSize` `64M`, `RuntimeMaxUse` `64M` |
| `/var/log` | `80,011,934` bytes apparent, `57,257,984` on disk; `btmp` `5,976,064`; `auth.log` `5,185,536`; `syslog` `737,280` | `80,095,224`, `57,339,904`; `btmp` `6,012,928`; `auth.log` `5,226,496`; `syslog` `741,376` |
| `rsyslog.service` | `active`, `running`, `enabled` | `inactive`, `dead`, `disabled` |
| `syslog.socket` | `active`, `running` | `inactive`, `dead` |
| the clock's offset | `-1.783ms` | `+1.852ms` |
| `sshd -T` | `permitrootlogin yes`, `passwordauthentication yes` | `permitrootlogin without-password`, `passwordauthentication no` |
| `sshd`'s files | `Include` at line 12, `PermitRootLogin yes` at 42, `KbdInteractiveAuthentication no` at 71, `01-xserver.conf`'s `PermitRootLogin yes` | the same, with `00-btc-5m-twap.conf`'s lines 4 to 6 before `01-xserver.conf`'s |
| journald's process | `systemd-journal 303` | `systemd-journal 26407` — restarted by B-CONFIGURE |

### 2.4 The network — `51-net.log`

The package manager's read first: `apt-daily.service` and `apt-daily-upgrade.service` both read `inactive` at
13:59:22 UTC. Then `net`:

```
2026-11-19T13:59:22.751101775Z
inactive
inactive
2026-11-19T13:59:32.859761152Z
[2026-11-19T13:59:32Z] DNS clob.polymarket.com IPv4: ['104.18.34.205', '172.64.153.51']; ws-subscriptions-clob.polymarket.com IPv4: ['18.165.72.103', '18.165.72.14', '18.165.72.48', '18.165.72.52']
[2026-11-19T13:59:33Z] N1 read 1: GET https://clob.polymarket.com/: status 200, body b'"OK"', data centre 'SOF', 64.292 ms - PASS
[2026-11-19T13:59:33Z] N2 read 1: GET https://clob.polymarket.com/time: status 200, ten digits True, data centre 'SOF', cache 'DYNAMIC', the venue's seconds less this host's 0 - PASS
[2026-11-19T13:59:33Z] N3 read 1: wss://ws-subscriptions-clob.polymarket.com/ws/market handshake: status 101, accept key valid, data centre '' - PASS
[2026-11-19T13:59:33Z] G-NET N1 the CLOB's root: PASS
[2026-11-19T13:59:33Z] G-NET N2 the CLOB's time: PASS
[2026-11-19T13:59:33Z] G-NET N3 the market websocket: PASS
[2026-11-19T13:59:33Z] G-NET PASS: 3 of 3
[2026-11-19T14:00:03Z] EDGE 60 TCP handshakes with clob.polymarket.com:443, 0.5 s apart, after G-NET's PASS alone: 60 completed; median 0.917 ms, p95 1.354 ms, max 1.933 ms
[2026-11-19T14:00:03Z] RECORD net {"edge_ns":[807307,1064757,996925,1228310,755790,917420,666796,754614,1196631,795402,981834,1313084,955208,785129,813778,682178,843157,1142151,982241,1034215,1353686,664570,1067812,730538,1933159,790014,846393,1372328,755262,659955,1136422,1055138,1124918,848954,741552,1051182,832565,1228863,746257,783786,1072149,986589,1032030,964259,906579,826986,1297619,889747,1399065,809114,815800,770612,965208,1164475,991041,755809,988479,858029,685048,1145917],"reading":true,"results":{"N1 the CLOB's root":true,"N2 the CLOB's time":true,"N3 the market websocket":true}}
[2026-11-19T14:00:03Z] peak memory of this run: 30248960 bytes
[2026-11-19T14:00:03Z] refused by the hook: 0; lookups 2, requests 2, handshakes 1, TCP connects 60
exit=0
```

**G-NET PASS: 3 of 3**, each check at its first read (V12). N1: the CLOB's root, status `200`, body `"OK"`, data centre
`SOF`. N2: `/time`, status `200`, ten digits, `SOF`, cache `DYNAMIC`, the venue's seconds less the host's `0`. N3: the
market websocket's handshake, status `101`, accept key valid. **The 60 handshakes:** 60 completed, median `0.917` ms,
95th percentile `1.354` ms, maximum `1.933` ms. The `DNS` line prints the venue's own IPv4 addresses, as the mode
prints them — the venue's, not either host's.

### 2.5 The latency — `52-latency.log`

The package manager read `inactive` and `inactive` at 14:00:13 UTC. **G-LAT's summary lines, whole:**

```
[2026-11-19T14:07:52Z] LATENCY counted 600, valid 600 (fresh 0, errors 0, non-200 0, cache not the origin's 0); data centres {'SOF': 600}
[2026-11-19T14:07:52Z] LATENCY time to the first byte, ms: p5 53.804, p50 56.296, p95 63.941, p99 90.518, max 225.146; p50 of the first half 56.628, of the second 55.950; the venue's seconds less this host's (-1, 0)
[2026-11-19T14:07:52Z] LATENCY one-way bound, half the median: 28.148 ms, against 50.000 ms
[2026-11-19T14:07:52Z] G-LAT PASS
[2026-11-19T14:07:52Z] RECORD latency {"reading":"PASS","stats":{"cache other":0,"counted":600,"errors":0,"fresh":0,"max":225146255,"non-200":0,"p5":53804006,"p50":56295867,"p50 first half":56627786,"p50 second half":55949730,"p95":63941115,"p99":90518256,"valid":600,"venue less host, s":[-1,0]}}
[2026-11-19T14:07:52Z] peak memory of this run: 30519296 bytes
[2026-11-19T14:07:52Z] refused by the hook: 0; lookups 1, requests 605, handshakes 0, TCP connects 0
exit=0
```

**G-LAT PASS** (V13): 600 counted replies, 600 valid — fresh 0, errors 0, non-200 0, cache not the origin's 0 — every
one through `SOF`. The nearest-rank median time to the first byte was **56.296 ms**, against 100.000 ms. The 5th,
95th and 99th percentiles were 53.804, 63.941 and 90.518 ms, and the maximum 225.146 ms. The median of the first half
of the valid replies was 56.628 ms and of the second 55.950 ms. The venue's seconds less the host's ran from `-1` to
`0`. **The one-way bound, half the median: 28.148 ms, against 50.000 ms.** The 605 requests began at 14:00:19 and the
mode ended at 14:07:52 UTC.

**Every line of `52-latency.log`, verbatim** — the package manager's read, the floors, every request's own line and
the summary — so that the reading can be re-derived from the repository (CANON hard rule 16):

```
2026-11-19T14:00:13.336873977Z
inactive
inactive
2026-11-19T14:00:19.558771413Z
[2026-11-19T14:00:19Z] MemAvailable read 1: 1500540928 bytes, floor 72439812
[2026-11-19T14:00:19Z] available on /: 16987672576 bytes, floor 100000000
[2026-11-19T14:00:19Z] LATENCY https://clob.polymarket.com/time over one kept IPv4 connection: 5 warm-up and 600 counted requests, one every 0.75 s, none begun after 540 s
[2026-11-19T14:07:52Z] S 0 warm fresh status 200 ttfb_us 66130 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 1 warm status 200 ttfb_us 58483 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 2 warm status 200 ttfb_us 56598 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 3 warm status 200 ttfb_us 62406 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 4 warm status 200 ttfb_us 58542 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 5 count status 200 ttfb_us 55810 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 6 count status 200 ttfb_us 141599 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 7 count status 200 ttfb_us 71941 pop SOF cache DYNAMIC body ok venue-host -1
[2026-11-19T14:07:52Z] S 8 count status 200 ttfb_us 56194 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 9 count status 200 ttfb_us 58881 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 10 count status 200 ttfb_us 54462 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 11 count status 200 ttfb_us 66944 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 12 count status 200 ttfb_us 54892 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 13 count status 200 ttfb_us 58595 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 14 count status 200 ttfb_us 58168 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 15 count status 200 ttfb_us 58820 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 16 count status 200 ttfb_us 56728 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 17 count status 200 ttfb_us 57548 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 18 count status 200 ttfb_us 53833 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 19 count status 200 ttfb_us 62238 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 20 count status 200 ttfb_us 55253 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 21 count status 200 ttfb_us 68438 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 22 count status 200 ttfb_us 55522 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 23 count status 200 ttfb_us 56088 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 24 count status 200 ttfb_us 60698 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 25 count status 200 ttfb_us 57625 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 26 count status 200 ttfb_us 54902 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 27 count status 200 ttfb_us 55513 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 28 count status 200 ttfb_us 56809 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 29 count status 200 ttfb_us 57961 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 30 count status 200 ttfb_us 64284 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 31 count status 200 ttfb_us 56855 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 32 count status 200 ttfb_us 55340 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 33 count status 200 ttfb_us 55147 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 34 count status 200 ttfb_us 54729 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 35 count status 200 ttfb_us 57395 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 36 count status 200 ttfb_us 54996 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 37 count status 200 ttfb_us 58280 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 38 count status 200 ttfb_us 56093 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 39 count status 200 ttfb_us 54224 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 40 count status 200 ttfb_us 138931 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 41 count status 200 ttfb_us 54044 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 42 count status 200 ttfb_us 56687 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 43 count status 200 ttfb_us 53602 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 44 count status 200 ttfb_us 53807 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 45 count status 200 ttfb_us 69338 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 46 count status 200 ttfb_us 55450 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 47 count status 200 ttfb_us 63109 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 48 count status 200 ttfb_us 62629 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 49 count status 200 ttfb_us 59574 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 50 count status 200 ttfb_us 57518 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 51 count status 200 ttfb_us 57713 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 52 count status 200 ttfb_us 55669 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 53 count status 200 ttfb_us 53681 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 54 count status 200 ttfb_us 56578 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 55 count status 200 ttfb_us 53701 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 56 count status 200 ttfb_us 54720 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 57 count status 200 ttfb_us 59653 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 58 count status 200 ttfb_us 55369 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 59 count status 200 ttfb_us 66896 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 60 count status 200 ttfb_us 60334 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 61 count status 200 ttfb_us 59128 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 62 count status 200 ttfb_us 56828 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 63 count status 200 ttfb_us 56102 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 64 count status 200 ttfb_us 57437 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 65 count status 200 ttfb_us 59628 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 66 count status 200 ttfb_us 55160 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 67 count status 200 ttfb_us 56977 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 68 count status 200 ttfb_us 58761 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 69 count status 200 ttfb_us 58102 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 70 count status 200 ttfb_us 55111 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 71 count status 200 ttfb_us 56277 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 72 count status 200 ttfb_us 57995 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 73 count status 200 ttfb_us 62812 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 74 count status 200 ttfb_us 54344 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 75 count status 200 ttfb_us 54045 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 76 count status 200 ttfb_us 55609 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 77 count status 200 ttfb_us 54893 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 78 count status 200 ttfb_us 54732 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 79 count status 200 ttfb_us 54727 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 80 count status 200 ttfb_us 57554 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 81 count status 200 ttfb_us 55831 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 82 count status 200 ttfb_us 55183 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 83 count status 200 ttfb_us 55384 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 84 count status 200 ttfb_us 61044 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 85 count status 200 ttfb_us 58746 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 86 count status 200 ttfb_us 55130 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 87 count status 200 ttfb_us 55711 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 88 count status 200 ttfb_us 55029 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 89 count status 200 ttfb_us 56066 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 90 count status 200 ttfb_us 55673 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 91 count status 200 ttfb_us 57059 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 92 count status 200 ttfb_us 55966 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 93 count status 200 ttfb_us 55440 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 94 count status 200 ttfb_us 56253 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 95 count status 200 ttfb_us 54128 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 96 count status 200 ttfb_us 55058 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 97 count status 200 ttfb_us 56295 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 98 count status 200 ttfb_us 57483 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 99 count status 200 ttfb_us 55072 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 100 count status 200 ttfb_us 54069 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 101 count status 200 ttfb_us 54071 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 102 count status 200 ttfb_us 58442 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 103 count status 200 ttfb_us 54229 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 104 count status 200 ttfb_us 57471 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 105 count status 200 ttfb_us 55664 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 106 count status 200 ttfb_us 55307 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 107 count status 200 ttfb_us 58262 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 108 count status 200 ttfb_us 56990 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 109 count status 200 ttfb_us 55907 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 110 count status 200 ttfb_us 57458 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 111 count status 200 ttfb_us 54602 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 112 count status 200 ttfb_us 56671 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 113 count status 200 ttfb_us 54874 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 114 count status 200 ttfb_us 60833 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 115 count status 200 ttfb_us 56130 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 116 count status 200 ttfb_us 54551 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 117 count status 200 ttfb_us 54439 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 118 count status 200 ttfb_us 55357 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 119 count status 200 ttfb_us 59898 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 120 count status 200 ttfb_us 53066 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 121 count status 200 ttfb_us 57233 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 122 count status 200 ttfb_us 56550 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 123 count status 200 ttfb_us 56649 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 124 count status 200 ttfb_us 57576 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 125 count status 200 ttfb_us 57055 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 126 count status 200 ttfb_us 53692 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 127 count status 200 ttfb_us 56982 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 128 count status 200 ttfb_us 56757 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 129 count status 200 ttfb_us 61706 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 130 count status 200 ttfb_us 57674 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 131 count status 200 ttfb_us 56335 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 132 count status 200 ttfb_us 56015 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 133 count status 200 ttfb_us 55365 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 134 count status 200 ttfb_us 57644 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 135 count status 200 ttfb_us 54803 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 136 count status 200 ttfb_us 56362 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 137 count status 200 ttfb_us 53944 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 138 count status 200 ttfb_us 59370 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 139 count status 200 ttfb_us 55561 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 140 count status 200 ttfb_us 63332 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 141 count status 200 ttfb_us 57028 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 142 count status 200 ttfb_us 57152 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 143 count status 200 ttfb_us 54400 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 144 count status 200 ttfb_us 57592 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 145 count status 200 ttfb_us 56904 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 146 count status 200 ttfb_us 53525 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 147 count status 200 ttfb_us 57152 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 148 count status 200 ttfb_us 54904 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 149 count status 200 ttfb_us 55536 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 150 count status 200 ttfb_us 53752 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 151 count status 200 ttfb_us 56012 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 152 count status 200 ttfb_us 53481 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 153 count status 200 ttfb_us 65883 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 154 count status 200 ttfb_us 54604 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 155 count status 200 ttfb_us 56986 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 156 count status 200 ttfb_us 56541 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 157 count status 200 ttfb_us 56689 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 158 count status 200 ttfb_us 53835 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 159 count status 200 ttfb_us 54195 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 160 count status 200 ttfb_us 54337 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 161 count status 200 ttfb_us 61019 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 162 count status 200 ttfb_us 53951 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 163 count status 200 ttfb_us 52913 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 164 count status 200 ttfb_us 55406 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 165 count status 200 ttfb_us 56627 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 166 count status 200 ttfb_us 55925 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 167 count status 200 ttfb_us 58123 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 168 count status 200 ttfb_us 55859 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 169 count status 200 ttfb_us 56175 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 170 count status 200 ttfb_us 53653 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 171 count status 200 ttfb_us 56860 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 172 count status 200 ttfb_us 55113 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 173 count status 200 ttfb_us 54079 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 174 count status 200 ttfb_us 56721 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 175 count status 200 ttfb_us 57728 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 176 count status 200 ttfb_us 54997 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 177 count status 200 ttfb_us 56742 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 178 count status 200 ttfb_us 57369 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 179 count status 200 ttfb_us 56356 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 180 count status 200 ttfb_us 55831 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 181 count status 200 ttfb_us 56262 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 182 count status 200 ttfb_us 54130 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 183 count status 200 ttfb_us 56057 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 184 count status 200 ttfb_us 58465 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 185 count status 200 ttfb_us 225146 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 186 count status 200 ttfb_us 69883 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 187 count status 200 ttfb_us 67642 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 188 count status 200 ttfb_us 65522 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 189 count status 200 ttfb_us 58633 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 190 count status 200 ttfb_us 58447 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 191 count status 200 ttfb_us 57397 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 192 count status 200 ttfb_us 82629 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 193 count status 200 ttfb_us 58596 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 194 count status 200 ttfb_us 55782 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 195 count status 200 ttfb_us 57573 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 196 count status 200 ttfb_us 56729 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 197 count status 200 ttfb_us 55072 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 198 count status 200 ttfb_us 59103 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 199 count status 200 ttfb_us 54399 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 200 count status 200 ttfb_us 54655 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 201 count status 200 ttfb_us 55421 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 202 count status 200 ttfb_us 55428 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 203 count status 200 ttfb_us 55906 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 204 count status 200 ttfb_us 56453 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 205 count status 200 ttfb_us 55401 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 206 count status 200 ttfb_us 54096 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 207 count status 200 ttfb_us 54601 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 208 count status 200 ttfb_us 54583 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 209 count status 200 ttfb_us 56241 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 210 count status 200 ttfb_us 55129 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 211 count status 200 ttfb_us 54364 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 212 count status 200 ttfb_us 54836 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 213 count status 200 ttfb_us 56916 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 214 count status 200 ttfb_us 58255 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 215 count status 200 ttfb_us 62790 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 216 count status 200 ttfb_us 55612 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 217 count status 200 ttfb_us 55072 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 218 count status 200 ttfb_us 59388 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 219 count status 200 ttfb_us 55505 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 220 count status 200 ttfb_us 55666 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 221 count status 200 ttfb_us 59497 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 222 count status 200 ttfb_us 65773 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 223 count status 200 ttfb_us 59187 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 224 count status 200 ttfb_us 57569 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 225 count status 200 ttfb_us 56607 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 226 count status 200 ttfb_us 59289 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 227 count status 200 ttfb_us 59166 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 228 count status 200 ttfb_us 61914 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 229 count status 200 ttfb_us 57869 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 230 count status 200 ttfb_us 59764 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 231 count status 200 ttfb_us 56598 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 232 count status 200 ttfb_us 59777 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 233 count status 200 ttfb_us 58803 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 234 count status 200 ttfb_us 56031 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 235 count status 200 ttfb_us 53949 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 236 count status 200 ttfb_us 54500 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 237 count status 200 ttfb_us 63941 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 238 count status 200 ttfb_us 65263 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 239 count status 200 ttfb_us 61920 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 240 count status 200 ttfb_us 60024 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 241 count status 200 ttfb_us 55288 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 242 count status 200 ttfb_us 57854 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 243 count status 200 ttfb_us 57571 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 244 count status 200 ttfb_us 55120 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 245 count status 200 ttfb_us 54181 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 246 count status 200 ttfb_us 54037 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 247 count status 200 ttfb_us 57900 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 248 count status 200 ttfb_us 58870 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 249 count status 200 ttfb_us 57675 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 250 count status 200 ttfb_us 89791 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 251 count status 200 ttfb_us 58452 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 252 count status 200 ttfb_us 55837 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 253 count status 200 ttfb_us 55561 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 254 count status 200 ttfb_us 56937 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 255 count status 200 ttfb_us 57433 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 256 count status 200 ttfb_us 57517 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 257 count status 200 ttfb_us 59045 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 258 count status 200 ttfb_us 56958 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 259 count status 200 ttfb_us 62503 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 260 count status 200 ttfb_us 63579 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 261 count status 200 ttfb_us 62244 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 262 count status 200 ttfb_us 56403 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 263 count status 200 ttfb_us 59092 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 264 count status 200 ttfb_us 57268 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 265 count status 200 ttfb_us 57506 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 266 count status 200 ttfb_us 64334 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 267 count status 200 ttfb_us 113625 pop SOF cache DYNAMIC body ok venue-host -1
[2026-11-19T14:07:52Z] S 268 count status 200 ttfb_us 61588 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 269 count status 200 ttfb_us 59860 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 270 count status 200 ttfb_us 55218 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 271 count status 200 ttfb_us 60713 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 272 count status 200 ttfb_us 56036 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 273 count status 200 ttfb_us 59991 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 274 count status 200 ttfb_us 59394 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 275 count status 200 ttfb_us 55478 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 276 count status 200 ttfb_us 57926 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 277 count status 200 ttfb_us 53370 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 278 count status 200 ttfb_us 56384 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 279 count status 200 ttfb_us 59064 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 280 count status 200 ttfb_us 57164 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 281 count status 200 ttfb_us 56036 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 282 count status 200 ttfb_us 58001 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 283 count status 200 ttfb_us 53859 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 284 count status 200 ttfb_us 57076 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 285 count status 200 ttfb_us 55184 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 286 count status 200 ttfb_us 57245 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 287 count status 200 ttfb_us 56529 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 288 count status 200 ttfb_us 54778 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 289 count status 200 ttfb_us 57396 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 290 count status 200 ttfb_us 61310 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 291 count status 200 ttfb_us 56319 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 292 count status 200 ttfb_us 54554 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 293 count status 200 ttfb_us 59249 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 294 count status 200 ttfb_us 56820 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 295 count status 200 ttfb_us 56536 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 296 count status 200 ttfb_us 54906 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 297 count status 200 ttfb_us 59808 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 298 count status 200 ttfb_us 55189 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 299 count status 200 ttfb_us 62413 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 300 count status 200 ttfb_us 58232 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 301 count status 200 ttfb_us 56208 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 302 count status 200 ttfb_us 90518 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 303 count status 200 ttfb_us 57237 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 304 count status 200 ttfb_us 56171 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 305 count status 200 ttfb_us 54874 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 306 count status 200 ttfb_us 54748 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 307 count status 200 ttfb_us 55467 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 308 count status 200 ttfb_us 69284 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 309 count status 200 ttfb_us 68458 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 310 count status 200 ttfb_us 60783 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 311 count status 200 ttfb_us 58122 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 312 count status 200 ttfb_us 56420 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 313 count status 200 ttfb_us 55401 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 314 count status 200 ttfb_us 55643 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 315 count status 200 ttfb_us 54021 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 316 count status 200 ttfb_us 57687 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 317 count status 200 ttfb_us 56506 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 318 count status 200 ttfb_us 59794 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 319 count status 200 ttfb_us 55715 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 320 count status 200 ttfb_us 54486 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 321 count status 200 ttfb_us 56616 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 322 count status 200 ttfb_us 55649 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 323 count status 200 ttfb_us 54059 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 324 count status 200 ttfb_us 64551 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 325 count status 200 ttfb_us 56505 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 326 count status 200 ttfb_us 56879 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 327 count status 200 ttfb_us 53804 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 328 count status 200 ttfb_us 55331 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 329 count status 200 ttfb_us 92326 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 330 count status 200 ttfb_us 55822 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 331 count status 200 ttfb_us 56221 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 332 count status 200 ttfb_us 55949 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 333 count status 200 ttfb_us 58881 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 334 count status 200 ttfb_us 54250 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 335 count status 200 ttfb_us 55064 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 336 count status 200 ttfb_us 56913 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 337 count status 200 ttfb_us 58251 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 338 count status 200 ttfb_us 57591 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 339 count status 200 ttfb_us 57129 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 340 count status 200 ttfb_us 54343 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 341 count status 200 ttfb_us 55195 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 342 count status 200 ttfb_us 55477 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 343 count status 200 ttfb_us 58798 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 344 count status 200 ttfb_us 54429 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 345 count status 200 ttfb_us 56728 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 346 count status 200 ttfb_us 60623 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 347 count status 200 ttfb_us 55524 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 348 count status 200 ttfb_us 54614 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 349 count status 200 ttfb_us 53837 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 350 count status 200 ttfb_us 53785 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 351 count status 200 ttfb_us 58680 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 352 count status 200 ttfb_us 54696 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 353 count status 200 ttfb_us 53719 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 354 count status 200 ttfb_us 53576 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 355 count status 200 ttfb_us 53571 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 356 count status 200 ttfb_us 54501 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 357 count status 200 ttfb_us 53391 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 358 count status 200 ttfb_us 55258 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 359 count status 200 ttfb_us 55599 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 360 count status 200 ttfb_us 55583 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 361 count status 200 ttfb_us 55568 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 362 count status 200 ttfb_us 53651 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 363 count status 200 ttfb_us 56180 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 364 count status 200 ttfb_us 55238 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 365 count status 200 ttfb_us 53986 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 366 count status 200 ttfb_us 53326 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 367 count status 200 ttfb_us 56641 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 368 count status 200 ttfb_us 57192 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 369 count status 200 ttfb_us 54342 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 370 count status 200 ttfb_us 57292 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 371 count status 200 ttfb_us 54347 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 372 count status 200 ttfb_us 55614 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 373 count status 200 ttfb_us 54348 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 374 count status 200 ttfb_us 55081 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 375 count status 200 ttfb_us 65299 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 376 count status 200 ttfb_us 55589 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 377 count status 200 ttfb_us 60276 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 378 count status 200 ttfb_us 55047 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 379 count status 200 ttfb_us 64158 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 380 count status 200 ttfb_us 54090 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 381 count status 200 ttfb_us 55883 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 382 count status 200 ttfb_us 57037 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 383 count status 200 ttfb_us 58819 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 384 count status 200 ttfb_us 53734 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 385 count status 200 ttfb_us 54992 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 386 count status 200 ttfb_us 54782 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 387 count status 200 ttfb_us 53527 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 388 count status 200 ttfb_us 54591 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 389 count status 200 ttfb_us 55019 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 390 count status 200 ttfb_us 54434 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 391 count status 200 ttfb_us 54989 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 392 count status 200 ttfb_us 58987 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 393 count status 200 ttfb_us 59776 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 394 count status 200 ttfb_us 55644 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 395 count status 200 ttfb_us 61212 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 396 count status 200 ttfb_us 63279 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 397 count status 200 ttfb_us 58702 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 398 count status 200 ttfb_us 58861 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 399 count status 200 ttfb_us 56719 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 400 count status 200 ttfb_us 56254 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 401 count status 200 ttfb_us 57583 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 402 count status 200 ttfb_us 56161 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 403 count status 200 ttfb_us 56859 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 404 count status 200 ttfb_us 54201 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 405 count status 200 ttfb_us 55909 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 406 count status 200 ttfb_us 54635 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 407 count status 200 ttfb_us 53869 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 408 count status 200 ttfb_us 55051 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 409 count status 200 ttfb_us 57963 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 410 count status 200 ttfb_us 62762 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 411 count status 200 ttfb_us 54708 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 412 count status 200 ttfb_us 56907 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 413 count status 200 ttfb_us 54418 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 414 count status 200 ttfb_us 53658 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 415 count status 200 ttfb_us 56777 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 416 count status 200 ttfb_us 55404 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 417 count status 200 ttfb_us 55515 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 418 count status 200 ttfb_us 55095 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 419 count status 200 ttfb_us 54558 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 420 count status 200 ttfb_us 54942 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 421 count status 200 ttfb_us 54308 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 422 count status 200 ttfb_us 55589 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 423 count status 200 ttfb_us 57334 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 424 count status 200 ttfb_us 56082 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 425 count status 200 ttfb_us 54977 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 426 count status 200 ttfb_us 55242 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 427 count status 200 ttfb_us 55283 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 428 count status 200 ttfb_us 54423 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 429 count status 200 ttfb_us 54516 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 430 count status 200 ttfb_us 56633 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 431 count status 200 ttfb_us 56257 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 432 count status 200 ttfb_us 53496 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 433 count status 200 ttfb_us 54100 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 434 count status 200 ttfb_us 56602 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 435 count status 200 ttfb_us 55276 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 436 count status 200 ttfb_us 54554 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 437 count status 200 ttfb_us 54963 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 438 count status 200 ttfb_us 54464 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 439 count status 200 ttfb_us 54646 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 440 count status 200 ttfb_us 56271 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 441 count status 200 ttfb_us 58712 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 442 count status 200 ttfb_us 54586 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 443 count status 200 ttfb_us 56763 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 444 count status 200 ttfb_us 56847 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 445 count status 200 ttfb_us 54467 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 446 count status 200 ttfb_us 64229 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 447 count status 200 ttfb_us 59699 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 448 count status 200 ttfb_us 55897 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 449 count status 200 ttfb_us 56287 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 450 count status 200 ttfb_us 56756 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 451 count status 200 ttfb_us 57111 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 452 count status 200 ttfb_us 56945 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 453 count status 200 ttfb_us 54916 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 454 count status 200 ttfb_us 59726 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 455 count status 200 ttfb_us 57368 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 456 count status 200 ttfb_us 56796 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 457 count status 200 ttfb_us 56929 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 458 count status 200 ttfb_us 57167 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 459 count status 200 ttfb_us 142576 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 460 count status 200 ttfb_us 58462 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 461 count status 200 ttfb_us 54938 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 462 count status 200 ttfb_us 53112 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 463 count status 200 ttfb_us 63429 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 464 count status 200 ttfb_us 54543 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 465 count status 200 ttfb_us 55433 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 466 count status 200 ttfb_us 53637 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 467 count status 200 ttfb_us 55435 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 468 count status 200 ttfb_us 56547 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 469 count status 200 ttfb_us 55802 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 470 count status 200 ttfb_us 59748 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 471 count status 200 ttfb_us 54319 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 472 count status 200 ttfb_us 56350 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 473 count status 200 ttfb_us 55201 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 474 count status 200 ttfb_us 55333 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 475 count status 200 ttfb_us 59211 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 476 count status 200 ttfb_us 55788 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 477 count status 200 ttfb_us 57622 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 478 count status 200 ttfb_us 57207 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 479 count status 200 ttfb_us 57157 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 480 count status 200 ttfb_us 52966 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 481 count status 200 ttfb_us 54728 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 482 count status 200 ttfb_us 57513 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 483 count status 200 ttfb_us 62223 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 484 count status 200 ttfb_us 55241 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 485 count status 200 ttfb_us 54788 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 486 count status 200 ttfb_us 53402 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 487 count status 200 ttfb_us 58674 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 488 count status 200 ttfb_us 57439 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 489 count status 200 ttfb_us 59753 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 490 count status 200 ttfb_us 56691 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 491 count status 200 ttfb_us 57447 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 492 count status 200 ttfb_us 58851 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 493 count status 200 ttfb_us 54790 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 494 count status 200 ttfb_us 54445 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 495 count status 200 ttfb_us 55873 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 496 count status 200 ttfb_us 55380 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 497 count status 200 ttfb_us 61875 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 498 count status 200 ttfb_us 55629 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 499 count status 200 ttfb_us 57149 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 500 count status 200 ttfb_us 53201 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 501 count status 200 ttfb_us 57437 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 502 count status 200 ttfb_us 54920 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 503 count status 200 ttfb_us 58496 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 504 count status 200 ttfb_us 57601 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 505 count status 200 ttfb_us 60065 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 506 count status 200 ttfb_us 58050 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 507 count status 200 ttfb_us 57372 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 508 count status 200 ttfb_us 57373 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 509 count status 200 ttfb_us 54343 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 510 count status 200 ttfb_us 54949 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 511 count status 200 ttfb_us 57029 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 512 count status 200 ttfb_us 56827 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 513 count status 200 ttfb_us 55227 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 514 count status 200 ttfb_us 57779 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 515 count status 200 ttfb_us 53769 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 516 count status 200 ttfb_us 54829 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 517 count status 200 ttfb_us 56588 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 518 count status 200 ttfb_us 55218 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 519 count status 200 ttfb_us 57415 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 520 count status 200 ttfb_us 54625 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 521 count status 200 ttfb_us 54450 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 522 count status 200 ttfb_us 59340 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 523 count status 200 ttfb_us 54213 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 524 count status 200 ttfb_us 56538 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 525 count status 200 ttfb_us 54864 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 526 count status 200 ttfb_us 55472 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 527 count status 200 ttfb_us 62724 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 528 count status 200 ttfb_us 56890 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 529 count status 200 ttfb_us 55583 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 530 count status 200 ttfb_us 54879 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 531 count status 200 ttfb_us 56060 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 532 count status 200 ttfb_us 53619 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 533 count status 200 ttfb_us 55471 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 534 count status 200 ttfb_us 55685 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 535 count status 200 ttfb_us 56593 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 536 count status 200 ttfb_us 56302 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 537 count status 200 ttfb_us 56587 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 538 count status 200 ttfb_us 56798 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 539 count status 200 ttfb_us 55474 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 540 count status 200 ttfb_us 57107 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 541 count status 200 ttfb_us 56402 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 542 count status 200 ttfb_us 54702 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 543 count status 200 ttfb_us 56988 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 544 count status 200 ttfb_us 54637 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 545 count status 200 ttfb_us 55566 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 546 count status 200 ttfb_us 61153 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 547 count status 200 ttfb_us 55184 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 548 count status 200 ttfb_us 55292 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 549 count status 200 ttfb_us 54546 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 550 count status 200 ttfb_us 56460 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 551 count status 200 ttfb_us 56191 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 552 count status 200 ttfb_us 57807 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 553 count status 200 ttfb_us 58900 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 554 count status 200 ttfb_us 57070 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 555 count status 200 ttfb_us 57266 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 556 count status 200 ttfb_us 56190 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 557 count status 200 ttfb_us 54011 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 558 count status 200 ttfb_us 55602 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 559 count status 200 ttfb_us 55551 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 560 count status 200 ttfb_us 58432 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 561 count status 200 ttfb_us 55686 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 562 count status 200 ttfb_us 56387 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 563 count status 200 ttfb_us 62979 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 564 count status 200 ttfb_us 56822 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 565 count status 200 ttfb_us 59306 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 566 count status 200 ttfb_us 55618 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 567 count status 200 ttfb_us 60432 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 568 count status 200 ttfb_us 55211 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 569 count status 200 ttfb_us 56970 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 570 count status 200 ttfb_us 58734 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 571 count status 200 ttfb_us 56327 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 572 count status 200 ttfb_us 58391 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 573 count status 200 ttfb_us 55987 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 574 count status 200 ttfb_us 56775 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 575 count status 200 ttfb_us 56552 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 576 count status 200 ttfb_us 57189 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 577 count status 200 ttfb_us 59660 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 578 count status 200 ttfb_us 59662 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 579 count status 200 ttfb_us 64132 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 580 count status 200 ttfb_us 56708 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 581 count status 200 ttfb_us 61682 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 582 count status 200 ttfb_us 61416 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 583 count status 200 ttfb_us 55988 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 584 count status 200 ttfb_us 56781 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 585 count status 200 ttfb_us 57783 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 586 count status 200 ttfb_us 56027 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 587 count status 200 ttfb_us 75809 pop SOF cache DYNAMIC body ok venue-host -1
[2026-11-19T14:07:52Z] S 588 count status 200 ttfb_us 59569 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 589 count status 200 ttfb_us 55678 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 590 count status 200 ttfb_us 54996 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 591 count status 200 ttfb_us 57782 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 592 count status 200 ttfb_us 54286 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 593 count status 200 ttfb_us 54973 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 594 count status 200 ttfb_us 56232 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 595 count status 200 ttfb_us 54479 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 596 count status 200 ttfb_us 54634 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 597 count status 200 ttfb_us 55156 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 598 count status 200 ttfb_us 56450 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 599 count status 200 ttfb_us 56397 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 600 count status 200 ttfb_us 54976 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 601 count status 200 ttfb_us 55239 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 602 count status 200 ttfb_us 58768 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 603 count status 200 ttfb_us 55757 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] S 604 count status 200 ttfb_us 54848 pop SOF cache DYNAMIC body ok venue-host 0
[2026-11-19T14:07:52Z] LATENCY counted 600, valid 600 (fresh 0, errors 0, non-200 0, cache not the origin's 0); data centres {'SOF': 600}
[2026-11-19T14:07:52Z] LATENCY time to the first byte, ms: p5 53.804, p50 56.296, p95 63.941, p99 90.518, max 225.146; p50 of the first half 56.628, of the second 55.950; the venue's seconds less this host's (-1, 0)
[2026-11-19T14:07:52Z] LATENCY one-way bound, half the median: 28.148 ms, against 50.000 ms
[2026-11-19T14:07:52Z] G-LAT PASS
[2026-11-19T14:07:52Z] RECORD latency {"reading":"PASS","stats":{"cache other":0,"counted":600,"errors":0,"fresh":0,"max":225146255,"non-200":0,"p5":53804006,"p50":56295867,"p50 first half":56627786,"p50 second half":55949730,"p95":63941115,"p99":90518256,"valid":600,"venue less host, s":[-1,0]}}
[2026-11-19T14:07:52Z] peak memory of this run: 30519296 bytes
[2026-11-19T14:07:52Z] refused by the hook: 0; lookups 1, requests 605, handshakes 0, TCP connects 0
exit=0
```

### 2.6 The disk — `53-disk.log`

The package manager read `inactive` and `inactive` at 14:07:58 UTC.

```
2026-11-19T14:07:58.611218346Z
inactive
inactive
2026-11-19T14:08:04.705779300Z
[2026-11-19T14:08:04Z] MemAvailable read 1: 1499525120 bytes, floor 72439812
[2026-11-19T14:08:04Z] available on /: 16987566080 bytes, floor 2515919104
[2026-11-19T14:08:05Z] DISK write 268435456 bytes in 256 chunks and fsync: 221.941 ms, 1209487627 bytes a second
[2026-11-19T14:08:05Z] DISK 200 appends of 4096 bytes, each with fsync: p50 0.501 ms, p99 1.005 ms, max 1.716 ms
[2026-11-19T14:08:05Z] DISK available before 16987566080, after 16987566080 bytes; the test files removed: True
[2026-11-19T14:08:05Z] RECORD disk {"fsync_ns":[380710,385259,388107,395930,400462,407416,408936,409183,411947,412959,416541,420087,427370,427826,428177,429527,429891,430504,430716,431538,431715,432283,433840,434188,436243,437028,438548,439024,440292,440814,440861,443309,443429,443572,444350,445639,445912,446628,447289,447867,449279,449862,451269,452466,453790,454580,454768,454873,454925,456453,456768,456989,457283,457831,459062,460688,462534,462666,462710,464238,464325,464364,465256,466464,467731,469836,469864,470896,471222,473092,473742,476892,477254,477516,478118,479004,479734,479837,480384,481003,481085,482660,483753,483787,484110,485310,485428,486530,488971,489659,490056,491152,491524,492610,493506,495064,495372,496010,500322,501439,501439,502227,502786,503013,503369,507568,512858,513819,519059,519810,520354,521148,521839,522298,524209,525015,528380,528737,528915,532723,532892,535883,537617,539614,541425,541684,541788,542032,544666,545910,550935,552430,554595,556009,558383,560243,561949,564766,567549,573244,573553,573556,576611,579265,579806,580429,582177,585058,588075,589425,590657,594144,594377,595398,596060,596653,601523,604416,605047,607068,607469,610517,613488,614707,615427,616064,617714,619390,619747,620676,620793,622741,623704,629613,639401,652314,655344,668163,669321,674210,676002,703497,706775,713336,736128,744103,760446,760967,765162,766831,794083,810394,820385,852415,898606,910202,933648,1005472,1226024,1716420],"write_bytes":268435456,"write_ns":221941465}
[2026-11-19T14:08:05Z] peak memory of this run: 28553216 bytes
[2026-11-19T14:08:05Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

256 MiB were written in 1 MiB pieces and synced in 221.941 ms: **1,209,487,627 bytes a second**. 200 appends of
4 KiB, each followed by `fsync`, took a median of **0.501 ms**, a 99th percentile of 1.005 ms and a maximum of
1.716 ms. Both test files were removed: `True` (V14, recorded, not asserted).

### 2.7 B-CONFIGURE and `verify`

**B-CONFIGURE** — run by the Executor as `R 'bash -s'` with §3.7's block on its standard input, at 14:08:20 UTC.
`60-B-CONFIGURE.log`, whole:

```
2026-11-19T14:08:20.508939750Z
/etc/sysctl.d:
total 56
drwxr-xr-x   2 root root 4096 ноя 18 15:11 .
drwxr-xr-x 106 root root 4096 ноя 19 06:48 ..
-rw-r--r--   1 root root  481 июл 13 14:43 10-bufferbloat.conf
-rw-r--r--   1 root root   77 мар 31  2024 10-console-messages.conf
-rw-r--r--   1 root root  490 мар 31  2024 10-ipv6-privacy.conf
-rw-r--r--   1 root root 1229 мар 31  2024 10-kernel-hardening.conf
-rw-r--r--   1 root root 1184 мар 31  2024 10-magic-sysrq.conf
-rw-r--r--   1 root root  164 мар 31  2024 10-map-count.conf
-rw-r--r--   1 root root  158 мар 31  2024 10-network-security.conf
-rw-r--r--   1 root root 1292 мар 31  2024 10-ptrace.conf
-rw-r--r--   1 root root  506 мар 31  2024 10-zeropage.conf
-rw-r--r--   1 root root  185 авг 26 12:57 99-cloudimg-ipv6.conf
-rw-r--r--   1 root root  114 ноя 18 15:11 99-gaming.conf
lrwxrwxrwx   1 root root   14 окт 12 07:36 99-sysctl.conf -> ../sysctl.conf
-rw-r--r--   1 root root  798 мар 24  2024 README.sysctl

/etc/systemd/journald.conf.d:
total 12
drwxr-xr-x 2 root root 4096 ноя 18 15:11 .
drwxr-xr-x 7 root root 4096 ноя 18 15:11 ..
-rw-r--r-- 1 root root   28 ноя 18 15:11 cap.conf
/swap.img regular file 1073741824 600 0 0
Filename				Type		Size		Used		Priority
/swap.img                               file		1048572		0		-2
3:/swap.img  none  swap  sw  0  0
files/journald.conf: OK
files/sysctl.conf: OK
vm.swappiness = 10
files exit=0
Removed "/etc/systemd/system/syslog.service".
Removed "/etc/systemd/system/multi-user.target.wants/rsyslog.service".
rsyslog exit=0
/swap.img regular file 1073741824 600 0 0
swap exit=0
```

`files exit=0`, `rsyslog exit=0`, `swap exit=0`. Before anything changed, `/swap.img` read as a regular file of
`1,073,741,824` bytes, mode `600`, owner `0` and group `0`, the one active swap with its one `fstab` line, line 3. It
read the same after: the file's mode and owner were already `0600` and root's, so no `chmod` or `chown` ran. No swap
file was written, `fstab` was not touched, and no swap was turned off or on.

**`verify`** — `61-verify.log`, every line:

```
2026-11-19T14:08:28.520141314Z
[2026-11-19T14:08:28Z] SWAP /swap.img (True, 1073741824, '0o600', 0); /proc/swaps [('/swap.img', 'file', 1048572, 0)]; fstab's swap lines [('/swap.img', 'none', 'swap', 'sw', '0', '0')]; SwapTotal 1073737728; vm.swappiness 10; /etc/sysctl.d/zz-btc-5m-twap-swap.conf ('3b31709b0c1c7026c71013150868a982296a36daa7b3635fd9eabe4929331a04', '0o644'); page 4096; swap.img.swap {'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'active', 'SourcePath': '/etc/fstab'}
[2026-11-19T14:08:28Z] G-SWAP S1 /swap.img, 1073741824 bytes, 0600, root's: PASS
[2026-11-19T14:08:28Z] G-SWAP S2 one active swap, this file: PASS
[2026-11-19T14:08:28Z] G-SWAP S3 one fstab line: PASS
[2026-11-19T14:08:28Z] G-SWAP S4 SwapTotal: PASS
[2026-11-19T14:08:28Z] G-SWAP S5 vm.swappiness 10: PASS
[2026-11-19T14:08:28Z] G-SWAP S6 the sysctl file: PASS
[2026-11-19T14:08:28Z] G-SWAP S7 swap.img.swap active, made of /etc/fstab: PASS
[2026-11-19T14:08:28Z] G-SWAP PASS: 7 of 7
[2026-11-19T14:08:28Z] JOURNALD /etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf ('91c7364c9ee1dec70c1651e7c976546d86a46f95b39ea8dd369ef83589439200', '0o644'), changed 1795097300521051 us; journald active since Thu 2026-11-19 14:08:20 UTC, pid 26407; its usage message {'realtime_us': 1795097300574117, 'max_use': 536870912, 'keep_free': 2147483648, 'message': 'System Journal (/var/log/journal/ef7f4459e2364097b06322e174690e1c) is 42.2M, max 512.0M, 469.7M free.'}
[2026-11-19T14:08:28Z] JOURNALD the probe tz49-probe-84b0fabb4584f10b: in the journal True, in /var/log/syslog False; rsyslog {'LoadState': 'loaded', 'ActiveState': 'inactive', 'UnitFileState': 'disabled'}; syslog.socket {'LoadState': 'loaded', 'ActiveState': 'inactive', 'UnitFileState': 'static'}; Archived and active journals take up 42.2M in the file system.
[2026-11-19T14:08:28Z] JOURNALD in force, by `systemd-analyze cat-config` exit 0: {'SystemMaxUse': ('512M', '/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf'), 'ForwardToSyslog': ('no', '/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf'), 'Storage': ('persistent', '/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf'), 'SystemKeepFree': ('2G', '/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf'), 'SystemMaxFileSize': ('64M', '/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf'), 'RuntimeMaxUse': ('64M', '/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf')}
[2026-11-19T14:08:28Z] G-LOG G1 the journald file: PASS
[2026-11-19T14:08:28Z] G-LOG G2 the running journald started after it: PASS
[2026-11-19T14:08:28Z] G-LOG G3 journald's own MAX_USE 536870912 and DISK_KEEP_FREE 2147483648: PASS
[2026-11-19T14:08:28Z] G-LOG G4 the probe in the journal alone: PASS
[2026-11-19T14:08:28Z] G-LOG G5 rsyslog and its socket off: PASS
[2026-11-19T14:08:28Z] G-LOG G6 every key of the journald file in force from it: PASS
[2026-11-19T14:08:28Z] G-LOG PASS: 6 of 6
[2026-11-19T14:08:28Z] RECORD verify {"log":true,"swap":true}
[2026-11-19T14:08:28Z] peak memory of this run: 28151808 bytes
[2026-11-19T14:08:28Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

**G-SWAP PASS: 7 of 7** and **G-LOG PASS: 6 of 6** (V15). journald restarted at 14:08:20 UTC, pid `26407`. Its own
usage message, stamped `1795097300574117` µs, after the drop-in's change at `1795097300521051` µs, reads
`MAX_USE` `536,870,912` and `DISK_KEEP_FREE` `2,147,483,648`. The probe `tz49-probe-84b0fabb4584f10b` was in the
journal and not in the last MiB of `/var/log/syslog`.

### 2.8 The access — `06-access.log` and `07-copy.log`

```
2026-11-19T13:56:11.704728017Z
exit=0
2026-11-19T13:56:19.513417550Z
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

`R true` read `exit=0` at its first read, 13:56:11 UTC: the access TZ-47 made stood. **B-ACCESS and B-ACCESS-KEY were
not handed over**, and nobody ran them. The Executor's key is TZ-47's, `SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo`.
The alias's settings are printed without their `hostname` line. The live host's key pinned under `live-host` is
TZ-47's, `ED25519` `SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw`. The last three lines read `vs-2348`, `root`
and `work tree exit=1` (V6).

```
2026-11-19T13:56:30.397399688Z
exit=0
scp exit=0
efcc5ead077b396fe18d243f3c65fa9824baca56e6db5312058971e0dfe6049b  /root/tz49-work/tz49-live-host.py
  2127 113254 /root/tz49-work/tz49-live-host.py
```

`exit=0` and `scp exit=0`; the live host's copy has §0.1's 2,127 lines, 113,254 bytes and SHA-256 `efcc5ead…` (V3).

### 2.9 The capture host — §0.0 to §0.5, and §3.9

**§0.0** — the session's own read, at 13:54:50 UTC, before the work tree existed:

```
ready=1: second 50090 of the day, outside 10800 to 27000; 10565148672 bytes free on /var/lib, 7795535636 needed; MemAvailable 250109952, 72439812 needed; at 1795096490 2026-11-19T13:54:50Z
```

`mkdir /root/tz49-work /root/tz49-work/logs; echo "exit=$?"` printed `exit=0`. Then `00-ready.log`:

```
2026-11-19T13:55:06.361005168Z
ready=1: second 50106 of the day, outside 10800 to 27000; 10564816896 bytes free on /var/lib, 7795535636 needed; MemAvailable 239890432, 72439812 needed; at 1795096506 2026-11-19T13:55:06Z
```

**§0.1** — `01-stage.log`:

```
2026-11-19T13:55:06.375776857Z
/root/tz49-work/stage/research/tz49-live-host.py 2127 113254 efcc5ead077b396fe18d243f3c65fa9824baca56e6db5312058971e0dfe6049b created
exit=0
```

**§0.3** — `03-host-gate.log`, whole. H1: one path. H2: `/dev/vda2`, `31612203008`, and `grep -c` `4`. H3: `3.12.3`.
H4: four paths. Memory gate: `271,249,408` against `72,439,812` at the first read. Disk gate: `avail`
`10,563,932,160` against `7,795,535,636`. **7 of 7** (V5). The consumer, `telemetry-watch.service`, read `disabled`
(exit 1) and `inactive` (exit 3). `/root/tz48-work` is gone, as TZ-48's report read it, and the Executor's key is
present.

```
2026-11-19T13:55:47.045430762Z
Thu Nov 19 01:55:47 PM UTC 2026
1795096547
2026-08-02 07:24:32
1
MemTotal:         978640 kB
MemAvailable:     250844 kB
SwapTotal:       3174396 kB
SwapFree:        2597764 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10563932160
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
405225096	/var/lib/btc-rewardbook
356513705	/root/btc-forensics
24704103	/root/.claude-8j
2592
disabled
exit=1
inactive
exit=3
/root/tz48-work exit=1
/root/.ssh/live-host exit=0
/root/btc-5m-twap       a76d79f [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/51f223d3-deb1-5de5-80aa-0eb16a447b53/scratchpad
total 40
drwx------ 10 root root 4096 Nov 19 13:53 .
drwx------ 40 root root 4096 Nov 19 13:53 ..
drwx------  4 root root 4096 Nov 19 13:53 51f223d3-deb1-5de5-80aa-0eb16a447b53
drwx------  3 root root 4096 Nov 19 13:53 6ce33308-8331-4563-bb79-d8486968f8ad
drwx------  3 root root 4096 Nov 19 08:19 91e07016-bfd8-431a-8738-d3dd14c17827
drwx------  3 root root 4096 Nov 15 10:28 95cf58d2-1ec6-4c73-a622-38d04665f5ae
drwx------  3 root root 4096 Nov 18 22:07 badf0ac4-2f71-4a1a-9c42-85675441c8ae
drwx------  4 root root 4096 Nov 19 08:19 bec9e390-46e1-55e5-81f0-1562edfe0238
drwx------  4 root root 4096 Nov 17 14:14 ccca2df8-e51d-56bc-8205-06299775095a
drwx------  4 root root 4096 Nov 18 22:07 dd42fdcf-137f-5b9f-8a10-6f720861ab64
MemAvailable read 1 13:55:47: 271249408
```

**§0.3, the room** — `04-room.log`, run in the background as §0.3 says. The archive's service read `inactive` at its
first read. **The margin over `STREAM_FLOOR` and `PEAK`: `2,874,778,827` bytes**, above `1,000,000,000`; TZ-48 read
`2,844,579,254`.

```
2026-11-19T13:55:53.680053845Z
[2026-11-19T13:55:53Z] btc-rewardbook-archive.service read 1: inactive
[2026-11-19T13:55:53Z] MemAvailable read 1: 247984128 bytes, floor 72439812
[2026-11-19T13:55:53Z] available on /var/lib: 10563772416 bytes, floor 7795535636
[2026-11-19T13:55:53Z] ROOM: 10563772416 bytes available on /var/lib; the reward book's stream files 56542047 bytes in 3 files under 23 day directories; the room 10620314463; its margin over STREAM_FLOOR 7300000000 and PEAK 445535636: 2874778827 bytes
[2026-11-19T13:55:53Z] peak memory of this run: 26939392 bytes
[2026-11-19T13:55:53Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

**§0.5** — `05-number.log`: `NUMBER PASS - 2 of 2`. `05-refs.log`: 182 lines, `refs/heads/tz-49-live-host-ipv4-keys`
absent (V2). **Against the Architect's 182 lines of 2026-11-19 at 13:40 UTC, one kind differs:** `HEAD` and
`refs/heads/main` stand at `a76d79f`, the upload of TZ-49, where the Architect read `6e9e580`. Every other kind's
count is equal: `tz-*` 22, pull heads 45, `pairbook-streams-*` 59, `rewardbook-streams-*` 48, the two annotated tags
with their peeled lines, and the two lightweight tags. No archive run had added a tag since the Architect's read.
Recorded, not BLOCKING (§0.5).

```
2026-11-19T13:56:05.259657078Z
[2026-11-19T13:56:05Z] origin/main a76d79f8ddb0a530a9dc6563d7e9cbd440520322: 117 paths under CryptoTZ/ and CryptoReports/; of the number TZ-49-: ['CryptoTZ/TZ-49-live-host-ipv4-keys.md'] and []
[2026-11-19T13:56:05Z] NUMBER PASS - 2 of 2
[2026-11-19T13:56:05Z] peak memory of this run: 26939392 bytes
[2026-11-19T13:56:05Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

```
2026-11-19T13:56:05.340760143Z
[2026-11-19T13:56:05Z] REF a76d79f8ddb0a530a9dc6563d7e9cbd440520322	HEAD
[2026-11-19T13:56:05Z] REF a76d79f8ddb0a530a9dc6563d7e9cbd440520322	refs/heads/main
[2026-11-19T13:56:05Z] REFS HEAD                                     1
[2026-11-19T13:56:05Z] REFS refs/heads/main                          1
[2026-11-19T13:56:05Z] REFS refs/heads/tz-*                          22
[2026-11-19T13:56:05Z] REFS refs/pull/*/head                         45
[2026-11-19T13:56:05Z] REFS refs/tags/pairbook-streams-*             59
[2026-11-19T13:56:05Z] REFS refs/tags/rewardbook-streams-*           48
[2026-11-19T13:56:05Z] REFS refs/tags/tz-01a-dataset                 1
[2026-11-19T13:56:05Z] REFS refs/tags/tz-01a-dataset^{}              1
[2026-11-19T13:56:05Z] REFS refs/tags/tz-27-pairbook-streams         1
[2026-11-19T13:56:05Z] REFS refs/tags/tz-27-pairbook-streams^{}      1
[2026-11-19T13:56:05Z] REFS refs/tags/tz-44-l0-inputs                1
[2026-11-19T13:56:05Z] REFS refs/tags/tz-45-l0-rule-w-inputs         1
[2026-11-19T13:56:05Z] REFS 182 lines; refs/heads/tz-49-live-host-ipv4-keys absent
[2026-11-19T13:56:05Z] peak memory of this run: 26939392 bytes
[2026-11-19T13:56:05Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

**§3.9, the copy** — `80-live-copy.log`: every log of the live host is on the capture host, byte for byte. `scp exit=0`
and `diff exit=0`.

```
2026-11-19T14:08:40.384618136Z
scp exit=0
diff exit=0
total 128
drwxr-xr-x 2 root root  4096 Nov 19 14:08 .
drwxr-xr-x 6 root root  4096 Nov 19 14:08 ..
-rw-r--r-- 1 root root  7054 Nov 19 14:08 40-host-before.log
-rw-r--r-- 1 root root   863 Nov 19 14:08 41-geoblock.log
-rw-r--r-- 1 root root   876 Nov 19 14:08 42-files.log
-rw-r--r-- 1 root root   552 Nov 19 14:08 43-B-SSH.log
-rw-r--r-- 1 root root  1629 Nov 19 14:08 44-sshd.log
-rw-r--r-- 1 root root  6076 Nov 19 14:08 50-selftest.log
-rw-r--r-- 1 root root  1892 Nov 19 14:08 51-net.log
-rw-r--r-- 1 root root 63566 Nov 19 14:08 52-latency.log
-rw-r--r-- 1 root root  2237 Nov 19 14:08 53-disk.log
-rw-r--r-- 1 root root  1646 Nov 19 14:08 60-B-CONFIGURE.log
-rw-r--r-- 1 root root  3145 Nov 19 14:08 61-verify.log
-rw-r--r-- 1 root root  7616 Nov 19 14:08 62-host-after.log
```

**§3.9, the closing reads** — `90-closing.log`, every line. On the live host, the guard reads `inactive` twice, its
timer and its service, and `rsyslog.service` is `inactive` and `disabled`, with `syslog.socket` `inactive`. The three
drop-ins are in place, and `sshd -T` prints the four keywords K2 to K5 read. On the capture host, the recorder,
`1555954`, the reward book, `1556307`, and the advisor, `1555970`, read `NRestarts` `0` and `active`, as at §0.3, and
the reward book's archive's service reads `inactive`. The branch is on `origin` at `9515874`.

```
2026-11-19T14:08:50.520295157Z
Чт 19 ноя 2026 14:08:51 UTC
NAME      TYPE       SIZE USED PRIO
/swap.img file 1073737728    0   -2
               total        used        free      shared  buff/cache   available
Mem:      1944465408   431394816   943951872     1462272   739082240  1513070592
Swap:     1073737728           0  1073737728
Filesystem             1B-blocks       Avail
/dev/mapper/lvm-root 20779339776 16987521024
active
inactive
inactive
active
inactive
inactive
disabled
Archived and active journals take up 42.2M in the file system.
-rw-r--r-- 1 root root  210 ноя 19 14:08 /etc/sysctl.d/zz-btc-5m-twap-swap.conf

/etc/ssh/sshd_config.d:
total 16
drwxr-xr-x 2 root root 4096 ноя 19 13:57 .
drwxr-xr-x 4 root root 4096 ноя 18 09:49 ..
-rw-r--r-- 1 root root  340 ноя 19 13:57 00-btc-5m-twap.conf
-rw-r--r-- 1 root root   20 ноя 18 09:49 01-xserver.conf

/etc/systemd/journald.conf.d:
total 16
drwxr-xr-x 2 root root 4096 ноя 19 14:08 .
drwxr-xr-x 7 root root 4096 ноя 18 15:11 ..
-rw-r--r-- 1 root root   28 ноя 18 15:11 cap.conf
-rw-r--r-- 1 root root  448 ноя 19 14:08 zz-btc-5m-twap-limits.conf
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
/dev/vda2      31612203008 10529345536
16516176	/root/tz49-work
421554573	/var/lib/btc-rewardbook
               total        used        free      shared  buff/cache   available
Mem:      1002127360   750739456    79937536      118784   357400576   251387904
Swap:     3250581504   632320000  2618261504
9515874e613de4987d490f8c4f5cd16fbca9b345	refs/heads/tz-49-live-host-ipv4-keys
```

### 2.10 The self-tests — `20-selftest.log` and `50-selftest.log`

**On the capture host**, `I selftest`:

```
2026-11-19T13:58:33.018852259Z
[2026-11-19T13:58:33Z] ok   nearest rank: 5, 50, 95, 99 and 100 of 1..100; of 600 values the median is the 300th smallest
[2026-11-19T13:58:33Z] ok   G-LAT PASS where the median is 100,000,000 ns exactly; the warm-up not counted
[2026-11-19T13:58:33Z] ok   G-LAT FAIL where the median is 100,000,001 ns
[2026-11-19T13:58:33Z] ok   G-LAT UNDECIDABLE at 569 valid of 600: a cached reply is not the origin's
[2026-11-19T13:58:33Z] ok   a fresh, a 503, a body not ten digits, no data centre, an error and no cache status: none valid
[2026-11-19T13:58:33Z] ok   milliseconds to three decimals; the data centre from a cf-ray header, and none from a malformed one
[2026-11-19T13:58:33Z] ok   G-GEO: PASS, BLOCKED, and UNREAD on a 403, a string, three letters, no body, no blocked and no reply
[2026-11-19T13:58:33Z] ok   the geoblock's printed fields carry its keys and never the address
[2026-11-19T13:58:33Z] ok   an error printed by its type, errno and the C library's message, or its type alone
[2026-11-19T13:58:33Z] ok   IPv6's state: one global address; a reject route is no usable default, a gateway route is; no address
[2026-11-19T13:58:33Z] ok   G-SPEC at its bounds, and a byte under each
[2026-11-19T13:58:33Z] ok   the live host gate: five checks, each failing alone; the pinned key among the host's keys, or alone
[2026-11-19T13:58:33Z] ok   the host name's first label: vs-2348 with and without its provider's domain, and no other name
[2026-11-19T13:58:33Z] ok   /proc/swaps parsed: the host's own file of 1,048,572 KiB; a header alone is no swap
[2026-11-19T13:58:33Z] ok   fstab: comments and blank lines left out
[2026-11-19T13:58:33Z] ok   G-SWAP PASS on literals: the host's own file, one swap, one fstab line, SwapTotal, swappiness, the sysctl file, its unit made of fstab
[2026-11-19T13:58:33Z] ok   G-SWAP FAIL on fourteen wrong readings, each alone: /swapfile, the path TZ-48 assumed, among them
[2026-11-19T13:58:33Z] ok   journald's usage message: the System Journal's of this process alone, the last one; none of another
[2026-11-19T13:58:33Z] ok   the merged configuration: each key's last value and its file, ours after cap.conf and syslog.conf; a comment beginning '# /' no header
[2026-11-19T13:58:33Z] ok   G-LOG PASS on literals, rsyslog disabled or not installed
[2026-11-19T13:58:33Z] ok   G-LOG FAIL on twelve wrong readings, each alone: cap.conf's bound in force among them
[2026-11-19T13:58:33Z] ok   the four files: their SHA-256 and bytes
[2026-11-19T13:58:33Z] ok   the journald file sets six keys under [Journal]; the sysctl file one; the sshd file three; B-SSH names the drop-in, its SHA-256, its guard and its log
[2026-11-19T13:58:33Z] ok   G-SSH on the live host PASS on sshd -T as OpenSSH 9.6 prints it after the drop-in, FAIL before it
[2026-11-19T13:58:33Z] ok   G-SSH FAIL on seven wrong readings, each alone: no sshd -T among them
[2026-11-19T13:58:33Z] ok   the methods an sshd offered, from ssh -v's text: each list once, and never the address
[2026-11-19T13:58:33Z] ok   a swap file's state: regular, bytes, mode, owner; None where it is absent
[2026-11-19T13:58:33Z] ok   NUMBER: this TZ's file alone, TZ-48's files beside it; absent, a second of the number, a report of it
[2026-11-19T13:58:33Z] ok   refs by kind, eight lines; this TZ's branch found where it exists
[2026-11-19T13:58:33Z] ok   the room and its margin; the floors 7,795,535,636 and 2,515,919,104; PEAK fourteen slots
[2026-11-19T13:58:33Z] ok   listening sockets: ports and classes, an established one left out, no address printed
[2026-11-19T13:58:33Z] ok   authorized keys: type and SHA256 fingerprint, options skipped, comments never printed
[2026-11-19T13:58:33Z] ok   a key's fingerprint as OpenSSH prints it: GitHub's published Ed25519 key and its published fingerprint
[2026-11-19T13:58:33Z] ok   reclaim's predicate: the work tree; nothing outside /tmp or beside another project's sessions
[2026-11-19T13:58:33Z] ok   the hook's files: writes under the work tree alone; no store or credential opened; the reward book listed by room alone; the forensic store by reclaim's exclusive create alone
[2026-11-19T13:58:33Z] ok   the hook's network: each mode's hosts alone, and no connection to an address it did not resolve
[2026-11-19T13:58:33Z] ok   IPv4 alone, in every mode: an AF_INET6 or AF_UNIX socket, a lookup in AF_INET6 or AF_UNSPEC and a connection to an IPv6 address refused, a resolved one included; an AF_INET socket allowed
[2026-11-19T13:58:33Z] ok   the hook's commands: each mode's read-only commands alone; nothing changes the host but the blocks
[2026-11-19T13:58:33Z] ok   the hook refuses, live, a write outside the work tree
[2026-11-19T13:58:33Z] ok   the hook refuses, live, an AF_INET6 socket, a lookup in AF_INET6 and one in AF_UNSPEC
[2026-11-19T13:58:34Z] ok   the probe over one kept loopback connection: the first exchange fresh, 30 counted, every request with this TZ's agent
[2026-11-19T13:58:34Z] ok   a server that closes every connection: every exchange fresh, G-LAT UNDECIDABLE
[2026-11-19T13:58:34Z] ok   a cached reply: G-LAT UNDECIDABLE
[2026-11-19T13:58:35Z] ok   no request begun after the budget
[2026-11-19T13:58:35Z] ok   a request through connect4: status, body, headers, fresh and the connection's own source address
[2026-11-19T13:58:35Z] ok   TCP handshakes with a closed port: each None
[2026-11-19T13:58:35Z] ok   the websocket handshake: 101, its accept key valid, this TZ's agent, closed with a masked frame of status 1000
[2026-11-19T13:58:35Z] ok   a wrong accept key: the handshake not valid
[2026-11-19T13:58:35Z] ok   the disk's write rate and fsync times on a stand-in of 4 MiB and 5 appends, its file removed
[2026-11-19T13:58:35Z] ok   meminfo in bytes, a count left a count
[2026-11-19T13:58:35Z] ok   systemctl's stamp under TZ=UTC
[2026-11-19T13:58:35Z] SELFTEST PASS: 51 checks, 51 passed
[2026-11-19T13:58:35Z] peak memory of this run: 29298688 bytes
[2026-11-19T13:58:35Z] refused by the hook: 4; lookups 0, requests 61, handshakes 2, TCP connects 3
exit=0
```

**On the live host**, `L selftest 50-selftest`:

```
2026-11-19T13:58:41.850425503Z
[2026-11-19T13:58:41Z] ok   nearest rank: 5, 50, 95, 99 and 100 of 1..100; of 600 values the median is the 300th smallest
[2026-11-19T13:58:41Z] ok   G-LAT PASS where the median is 100,000,000 ns exactly; the warm-up not counted
[2026-11-19T13:58:41Z] ok   G-LAT FAIL where the median is 100,000,001 ns
[2026-11-19T13:58:41Z] ok   G-LAT UNDECIDABLE at 569 valid of 600: a cached reply is not the origin's
[2026-11-19T13:58:41Z] ok   a fresh, a 503, a body not ten digits, no data centre, an error and no cache status: none valid
[2026-11-19T13:58:41Z] ok   milliseconds to three decimals; the data centre from a cf-ray header, and none from a malformed one
[2026-11-19T13:58:41Z] ok   G-GEO: PASS, BLOCKED, and UNREAD on a 403, a string, three letters, no body, no blocked and no reply
[2026-11-19T13:58:41Z] ok   the geoblock's printed fields carry its keys and never the address
[2026-11-19T13:58:41Z] ok   an error printed by its type, errno and the C library's message, or its type alone
[2026-11-19T13:58:41Z] ok   IPv6's state: one global address; a reject route is no usable default, a gateway route is; no address
[2026-11-19T13:58:41Z] ok   G-SPEC at its bounds, and a byte under each
[2026-11-19T13:58:41Z] ok   the live host gate: five checks, each failing alone; the pinned key among the host's keys, or alone
[2026-11-19T13:58:41Z] ok   the host name's first label: vs-2348 with and without its provider's domain, and no other name
[2026-11-19T13:58:41Z] ok   /proc/swaps parsed: the host's own file of 1,048,572 KiB; a header alone is no swap
[2026-11-19T13:58:41Z] ok   fstab: comments and blank lines left out
[2026-11-19T13:58:41Z] ok   G-SWAP PASS on literals: the host's own file, one swap, one fstab line, SwapTotal, swappiness, the sysctl file, its unit made of fstab
[2026-11-19T13:58:41Z] ok   G-SWAP FAIL on fourteen wrong readings, each alone: /swapfile, the path TZ-48 assumed, among them
[2026-11-19T13:58:41Z] ok   journald's usage message: the System Journal's of this process alone, the last one; none of another
[2026-11-19T13:58:41Z] ok   the merged configuration: each key's last value and its file, ours after cap.conf and syslog.conf; a comment beginning '# /' no header
[2026-11-19T13:58:41Z] ok   G-LOG PASS on literals, rsyslog disabled or not installed
[2026-11-19T13:58:41Z] ok   G-LOG FAIL on twelve wrong readings, each alone: cap.conf's bound in force among them
[2026-11-19T13:58:41Z] ok   the four files: their SHA-256 and bytes
[2026-11-19T13:58:41Z] ok   the journald file sets six keys under [Journal]; the sysctl file one; the sshd file three; B-SSH names the drop-in, its SHA-256, its guard and its log
[2026-11-19T13:58:41Z] ok   G-SSH on the live host PASS on sshd -T as OpenSSH 9.6 prints it after the drop-in, FAIL before it
[2026-11-19T13:58:41Z] ok   G-SSH FAIL on seven wrong readings, each alone: no sshd -T among them
[2026-11-19T13:58:41Z] ok   the methods an sshd offered, from ssh -v's text: each list once, and never the address
[2026-11-19T13:58:41Z] ok   a swap file's state: regular, bytes, mode, owner; None where it is absent
[2026-11-19T13:58:41Z] ok   NUMBER: this TZ's file alone, TZ-48's files beside it; absent, a second of the number, a report of it
[2026-11-19T13:58:41Z] ok   refs by kind, eight lines; this TZ's branch found where it exists
[2026-11-19T13:58:41Z] ok   the room and its margin; the floors 7,795,535,636 and 2,515,919,104; PEAK fourteen slots
[2026-11-19T13:58:41Z] ok   listening sockets: ports and classes, an established one left out, no address printed
[2026-11-19T13:58:41Z] ok   authorized keys: type and SHA256 fingerprint, options skipped, comments never printed
[2026-11-19T13:58:41Z] ok   a key's fingerprint as OpenSSH prints it: GitHub's published Ed25519 key and its published fingerprint
[2026-11-19T13:58:41Z] ok   reclaim's predicate: the work tree; nothing outside /tmp or beside another project's sessions
[2026-11-19T13:58:41Z] ok   the hook's files: writes under the work tree alone; no store or credential opened; the reward book listed by room alone; the forensic store by reclaim's exclusive create alone
[2026-11-19T13:58:41Z] ok   the hook's network: each mode's hosts alone, and no connection to an address it did not resolve
[2026-11-19T13:58:41Z] ok   IPv4 alone, in every mode: an AF_INET6 or AF_UNIX socket, a lookup in AF_INET6 or AF_UNSPEC and a connection to an IPv6 address refused, a resolved one included; an AF_INET socket allowed
[2026-11-19T13:58:41Z] ok   the hook's commands: each mode's read-only commands alone; nothing changes the host but the blocks
[2026-11-19T13:58:41Z] ok   the hook refuses, live, a write outside the work tree
[2026-11-19T13:58:41Z] ok   the hook refuses, live, an AF_INET6 socket, a lookup in AF_INET6 and one in AF_UNSPEC
[2026-11-19T13:58:43Z] ok   the probe over one kept loopback connection: the first exchange fresh, 30 counted, every request with this TZ's agent
[2026-11-19T13:58:43Z] ok   a server that closes every connection: every exchange fresh, G-LAT UNDECIDABLE
[2026-11-19T13:58:43Z] ok   a cached reply: G-LAT UNDECIDABLE
[2026-11-19T13:58:44Z] ok   no request begun after the budget
[2026-11-19T13:58:44Z] ok   a request through connect4: status, body, headers, fresh and the connection's own source address
[2026-11-19T13:58:44Z] ok   TCP handshakes with a closed port: each None
[2026-11-19T13:58:44Z] ok   the websocket handshake: 101, its accept key valid, this TZ's agent, closed with a masked frame of status 1000
[2026-11-19T13:58:44Z] ok   a wrong accept key: the handshake not valid
[2026-11-19T13:58:44Z] ok   the disk's write rate and fsync times on a stand-in of 4 MiB and 5 appends, its file removed
[2026-11-19T13:58:44Z] ok   meminfo in bytes, a count left a count
[2026-11-19T13:58:44Z] ok   systemctl's stamp under TZ=UTC
[2026-11-19T13:58:44Z] SELFTEST PASS: 51 checks, 51 passed
[2026-11-19T13:58:44Z] peak memory of this run: 29995008 bytes
[2026-11-19T13:58:44Z] refused by the hook: 4; lookups 0, requests 61, handshakes 2, TCP connects 3
exit=0
```

`SELFTEST PASS: 51 checks, 51 passed` on both, and `refused by the hook: 4` on both — the self-test's own live
refusals (V9).

### 2.11 The directories beside this session — `30-scratch.log` and `32-reclaim-scratch.log`

```
2026-11-19T13:58:49.876861953Z
[2026-11-19T13:58:49Z] running 1738600 started 2026-11-15T10:28:51Z claude
[2026-11-19T13:58:49Z] running 1738611 started 2026-11-15T10:28:53Z claude
[2026-11-19T13:58:49Z] running 1738619 started 2026-11-15T10:28:53Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-19T13:58:49Z] running 2385301 started 2026-11-19T13:53:23Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-19T13:58:49Z] 6ce33308-8331-4563-bb79-d8486968f8ad born 2026-11-19T13:53:23Z: live, process [2385301]
[2026-11-19T13:58:49Z] 91e07016-bfd8-431a-8738-d3dd14c17827 born 2026-11-19T08:19:41Z: earlier
[2026-11-19T13:58:49Z] 95cf58d2-1ec6-4c73-a622-38d04665f5ae born 2026-11-15T10:28:56Z: live, process [1738600, 1738611, 1738619]
[2026-11-19T13:58:49Z] badf0ac4-2f71-4a1a-9c42-85675441c8ae born 2026-11-18T22:07:09Z: earlier
[2026-11-19T13:58:49Z] bec9e390-46e1-55e5-81f0-1562edfe0238 born 2026-11-19T08:19:43Z: earlier
[2026-11-19T13:58:49Z] ccca2df8-e51d-56bc-8205-06299775095a born 2026-11-15T10:28:57Z: live, process [1738600, 1738611, 1738619]
[2026-11-19T13:58:49Z] dd42fdcf-137f-5b9f-8a10-6f720861ab64 born 2026-11-18T22:07:10Z: earlier
[2026-11-19T13:58:49Z] peak memory of this run: 26808320 bytes
[2026-11-19T13:58:49Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

`scratch` named four directories **earlier**: TZ-47's pair, `badf0ac4-…` and `dd42fdcf-…`, and TZ-48's pair,
`91e07016-…` and `bec9e390-…`. It named three **live**. `95cf58d2-…` and `ccca2df8-…` were each born within 60 s of
the start of the running `claude` processes of 2026-11-15 10:28:51 to 10:28:53 UTC. `6ce33308-…` was born with the
start of process `2385301`, at 13:53:23 UTC, the same minute as this session's own directory, `51f223d3-…`, which
`scratch` leaves out. By the rule alone, the four earlier directories were reclaimed (V10):

```
2026-11-19T13:59:05.396474115Z
[2026-11-19T13:59:05Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/91e07016-bfd8-431a-8738-d3dd14c17827, an earlier session's directory of 0 files: nothing of it is kept
[2026-11-19T13:59:05Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/badf0ac4-2f71-4a1a-9c42-85675441c8ae, an earlier session's directory of 0 files: nothing of it is kept
[2026-11-19T13:59:05Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/bec9e390-46e1-55e5-81f0-1562edfe0238, an earlier session's directory of 1 files: nothing of it is kept
[2026-11-19T13:59:05Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/dd42fdcf-137f-5b9f-8a10-6f720861ab64, an earlier session's directory of 6 files: nothing of it is kept
[2026-11-19T13:59:05Z] RECLAIM PASS: 0 files considered, 0 copied, 0 already held; the forensic store 2592 -> 2592 files
[2026-11-19T13:59:05Z] peak memory of this run: 27078656 bytes
[2026-11-19T13:59:05Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
2026-11-19T13:59:17.363985402Z
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
```

One `reclaim` named the four and printed `RECLAIM PASS` before any removal; then one `rm -rf` and one `test -e` a
directory, each `rm -rf` `exit=0` and each `test -e` `exit=1`.

### 2.12 §9 — B-RECLAIM-LIVE and B-RECLAIM-OWN

**B-RECLAIM-LIVE**, the Executor's, after §3.9's `diff exit=0`. Its instant was read in the same call, after it:

```
$ ssh -T -o BatchMode=yes -o ConnectTimeout=20 -o LogLevel=QUIET live-host 'rm -rf /root/tz49-work; test -e /root/tz49-work; echo "exit=$?"'; echo "R exit=$?"; date -u +%FT%T.%NZ
exit=1
R exit=0
2026-11-19T14:09:11.614335680Z
```

**B-RECLAIM-OWN**, last, with this report drafted. Its output was written to no file and is quoted from the session,
every line:

```
$ (cd /root/tz49-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz49-work/wt/research/tz49-live-host.py reclaim /root/tz49-work); echo "reclaim exit=$?"
[2026-11-19T14:13:16Z] reclaim: /root/tz49-work/wt skipped: no file but its HEAD's, and HEAD 9515874e613de4987d490f8c4f5cd16fbca9b345 is its upstream's
[2026-11-19T14:13:16Z] R copied ee9f041045a85f2a5b09188a4ed13fb39bac3f901c772b8e7c945299ae42fc3a /root/btc-forensics/tz49-work--live-logs--40-host-before.log
[2026-11-19T14:13:16Z] R copied 0aad72bb5e257bc755da9c3a7d3acb1ee37cd7aeb71312129589f16ab5867daf /root/btc-forensics/tz49-work--live-logs--41-geoblock.log
[2026-11-19T14:13:16Z] R copied 2b723f6296b41ffdd7eed6dc46cda36fa09d5ab00c77f98b0263b64075b49419 /root/btc-forensics/tz49-work--live-logs--42-files.log
[2026-11-19T14:13:16Z] R copied 474632ec1517a54077b899eccb4eed3a402966899d2771b23ef271d5de433b4c /root/btc-forensics/tz49-work--live-logs--43-B-SSH.log
[2026-11-19T14:13:16Z] R copied 348a7c0677e37f6085de9fcaa6c636c6ff6dafa0cb4e900675b95f0478e20a50 /root/btc-forensics/tz49-work--live-logs--44-sshd.log
[2026-11-19T14:13:16Z] R copied ce2efcc3848502ef3f74d377a08edfed374f5bbecf929a5e55ee6cf57571587b /root/btc-forensics/tz49-work--live-logs--50-selftest.log
[2026-11-19T14:13:16Z] R copied 50cc8ab11ed7d665fd1effbb6c50497e01fef856a700796bf7d013ec942ddac9 /root/btc-forensics/tz49-work--live-logs--51-net.log
[2026-11-19T14:13:16Z] R copied dbc363474d0c5c6b8f8308e511299594d270839c6a5779c2a09e9f842483111c /root/btc-forensics/tz49-work--live-logs--52-latency.log
[2026-11-19T14:13:16Z] R copied 034862217a4bda9718210c371c1152f1535df2eb2b72b91cd7a52764af032854 /root/btc-forensics/tz49-work--live-logs--53-disk.log
[2026-11-19T14:13:16Z] R copied 395879fa4892f30947c61412d99abb5ec24eb26a308b6aa621462231a0fed33e /root/btc-forensics/tz49-work--live-logs--60-B-CONFIGURE.log
[2026-11-19T14:13:16Z] R copied 0d8d438423cb0e9d9cf29b8a832279a04919234fd6c8ab10793c90e68a507fed /root/btc-forensics/tz49-work--live-logs--61-verify.log
[2026-11-19T14:13:16Z] R copied 300c057281e84633aa27d45384e88168496d7b4d20dfa5abc5c0cb05a2c1292d /root/btc-forensics/tz49-work--live-logs--62-host-after.log
[2026-11-19T14:13:16Z] R copied 4eac3a6121897f44f85bebbbbaf9b43bdc705240c44cc044ed1776e904ca35ff /root/btc-forensics/tz49-work--logs--00-ready.log
[2026-11-19T14:13:16Z] R copied 5cfaaea2c2e9e81908450d7ddb8f5644d0d77820ac52ee064f1f7be01a1cb979 /root/btc-forensics/tz49-work--logs--01-stage.log
[2026-11-19T14:13:16Z] R copied 3965cdbcf59a4ce9f236cd3a0986e2c5bc84e829fedda381f4ac76e95734c6b3 /root/btc-forensics/tz49-work--logs--02-fingerprint.log
[2026-11-19T14:13:16Z] R copied 425c6005cb543418d6e3ed04dec688b894667e127f3a087c93d25977570bf90c /root/btc-forensics/tz49-work--logs--03-host-gate.log
[2026-11-19T14:13:16Z] R copied 9da97d135bae2fa1fd1a54a2a22de8b947514a258cd3013f63702d973c62ce48 /root/btc-forensics/tz49-work--logs--04-room.log
[2026-11-19T14:13:16Z] R copied 84d285ab37853c89ee171c1636881c943d311ed9ac0696738c774d23439b4e1c /root/btc-forensics/tz49-work--logs--05-number.log
[2026-11-19T14:13:16Z] R copied 62d65ca1a09cbcc9a3132744e02ded9a7f9447f41f6b68f031639116f22eb67e /root/btc-forensics/tz49-work--logs--05-refs.log
[2026-11-19T14:13:16Z] R copied 457bfafeb157a7bb4da1d93af82e79f6603019f91698f0020accd1c465978d0b /root/btc-forensics/tz49-work--logs--06-access.log
[2026-11-19T14:13:16Z] R copied c3b4d8faf4e28ca3150b41173fdbc6d2bc1ab159f66d9b558ef79fd84d299645 /root/btc-forensics/tz49-work--logs--07-copy.log
[2026-11-19T14:13:16Z] R copied 6d4dd3d9fa9a715fb2f947aa189c9fa75c26a7087d0c2252e9d39ef120d328d0 /root/btc-forensics/tz49-work--logs--08-methods.log
[2026-11-19T14:13:16Z] R copied f27b5871cd5421fcd12688a5a643b05319463293843bd14470740e7c1d9aa05c /root/btc-forensics/tz49-work--logs--09-B-SSH-confirm.log
[2026-11-19T14:13:16Z] R copied d82022d7d4208f8363d10638cf6901ef2f09823dfb873198dbb4055328da961e /root/btc-forensics/tz49-work--logs--10-number.log
[2026-11-19T14:13:16Z] R copied 77e141c80a3eff9c01d27d8adca099808af6174dec3975e67f21a413c488b6b6 /root/btc-forensics/tz49-work--logs--11-worktree.log
[2026-11-19T14:13:16Z] R copied 49c462c5bc6aa39d5d0f6eb70e51df715720fb4ed6d03fcb6e1aa1823e98098c /root/btc-forensics/tz49-work--logs--12-fingerprint.log
[2026-11-19T14:13:16Z] R copied 4a01de51b57524eee651e7724c3efca095cac3e4c023ab19231ee0b3bf76f158 /root/btc-forensics/tz49-work--logs--13-push.log
[2026-11-19T14:13:16Z] R copied 80c712c4fd391117b78fe426ebfa775d2e6d9951887e053769966d458d36672b /root/btc-forensics/tz49-work--logs--14-pr.log
[2026-11-19T14:13:16Z] R copied 94d677173345dfd32e4b8d8b00b9268a264f89161d27efabe09957421f331992 /root/btc-forensics/tz49-work--logs--20-selftest.log
[2026-11-19T14:13:16Z] R copied 897dd91d92e4fb1407e7f10fb44dbdc37b94cabfb731798f74ab6d7bada0235f /root/btc-forensics/tz49-work--logs--30-scratch.log
[2026-11-19T14:13:16Z] R copied 2697f022dfef64cc446282900dc02ce7acbe1288c9d81770027b5f6ffaa07859 /root/btc-forensics/tz49-work--logs--32-reclaim-scratch.log
[2026-11-19T14:13:16Z] R copied 21ad890e77b329aafab1976dfc148ac14b1ecb6779b20b3cbbd86e31a0df7f42 /root/btc-forensics/tz49-work--logs--80-live-copy.log
[2026-11-19T14:13:16Z] R copied 645fbb348ff8ae981e3321f67f011801623b9c7c60d62f93cdab3ca6b33d46e1 /root/btc-forensics/tz49-work--logs--90-closing.log
[2026-11-19T14:13:16Z] R copied e06a2db1d642321fe9ad5eeb3bccb569d56394f1c83107807a43cf927483438c /root/btc-forensics/tz49-work--logs--99-selfcheck.log
[2026-11-19T14:13:16Z] R copied efcc5ead077b396fe18d243f3c65fa9824baca56e6db5312058971e0dfe6049b /root/btc-forensics/tz49-work--stage--research--tz49-live-host.py
[2026-11-19T14:13:16Z] RECLAIM PASS: 35 files considered, 35 copied, 0 already held; the forensic store 2592 -> 2627 files
[2026-11-19T14:13:16Z] peak memory of this run: 27201536 bytes
[2026-11-19T14:13:16Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
reclaim exit=0
$ cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz49-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz49-work; echo "exit=$?"
exit=0
$ test -e /root/tz49-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       a76d79f [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
2627
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10539978752
```

`reclaim` printed `RECLAIM PASS`, 35 of 35 files copied, before the removals. The worktree was skipped by
`pristine`, at its pushed `HEAD`, and removed without `--force`. `/root/tz49-work` is gone on both hosts,
`test -e` `exit=1` each. The worktrees are map §3's two, the primary checkout and `/root/btc-recorder-svc`. The
forensic store holds 2,627 files: 2,592 at §0.3 plus these 35, by exclusive create, each hash checked. 10,539,978,752
bytes are free on `/var/lib`. No line was refused by the classifier. The branch `tz-49-live-host-ipv4-keys` stays on
`origin` and as a local ref. **Kept on the capture host:** the Executor's key, the alias and the pinned host
key — the access — and the forensic store.

### 2.13 Every free-space and `MemAvailable` read, and every peak

| instant (UTC) | host | read | value | bound |
|---|---|---|---|---|
| 13:54:50 | capture | §0.0, `/var/lib` free; `MemAvailable` | `10,565,148,672`; `250,109,952` | `7,795,535,636`; `72,439,812` |
| 13:55:06 | capture | `00-ready.log`, the same | `10,564,816,896`; `239,890,432` | `7,795,535,636`; `72,439,812` |
| 13:55:47 | capture | §0.3, `df` `avail`; `MemAvailable` read 1 | `10,563,932,160`; `271,249,408` | `7,795,535,636`; `72,439,812` |
| 13:55:53 | capture | `room`, `MemAvailable` read 1; `/var/lib` available | `247,984,128`; `10,563,772,416` | `72,439,812`; `7,795,535,636` |
| 13:56:44 | live | `host before`, `MemAvailable` read 1; `/` available | `1,502,191,616`; `16,987,779,072` | `72,439,812`; `2,515,919,104` |
| 13:57:07 | live | `files`, the same | `1,497,681,920`; `16,987,742,208` | `72,439,812`; `2,515,919,104` |
| 14:00:19 | live | `latency`, the same | `1,500,540,928`; `16,987,672,576` | `72,439,812`; `100,000,000` |
| 14:08:04 | live | `disk`, the same | `1,499,525,120`; `16,987,566,080` | `72,439,812`; `2,515,919,104` |
| 14:08:50 | capture | §3.9, `df` `avail`; `free -b` available | `10,529,345,536`; `251,387,904` | printed |
| 14:08:51 | live | §3.9, `df` `avail`; `free -b` available | `16,987,521,024`; `1,513,070,592` | printed |

**Every mode's printed peak** (V17, recorded), against `36,219,906`, half of `MEM_FLOOR`:

| mode | host | log | instant (UTC) | peak, bytes |
|---|---|---|---|---|
| `fingerprint` | capture | `02-fingerprint.log` | 13:55:36 | `27,860,992` |
| `room` | capture | `04-room.log` | 13:55:53 | `26,939,392` |
| `number` | capture | `05-number.log` | 13:56:05 | `26,939,392` |
| `refs` | capture | `05-refs.log` | 13:56:05 | `26,939,392` |
| `methods before` | capture | `08-methods.log` | 13:57:01 | `26,939,392` |
| `methods after` | capture | `08-methods.log` | 13:57:40 | `26,546,176` |
| `number` | capture | `10-number.log` | 13:57:46 | `26,677,248` |
| `fingerprint` | capture | `12-fingerprint.log` | 13:57:55 | `27,725,824` |
| `refs` | capture | `13-push.log` | 13:58:08 | `26,677,248` |
| `selftest` | capture | `20-selftest.log` | 13:58:35 | `29,298,688` |
| `scratch` | capture | `30-scratch.log` | 13:58:49 | `26,808,320` |
| `reclaim` | capture | `32-reclaim-scratch.log` | 13:59:05 | `27,078,656` |
| `host before` | live | `40-host-before.log` | 13:56:44 | `27,635,712` |
| `geoblock` | live | `41-geoblock.log` | 13:56:54 | `30,117,888` |
| `files` | live | `42-files.log` | 13:57:07 | `27,496,448` |
| `sshd` | live | `44-sshd.log` | 13:57:39 | `27,496,448` |
| `selftest` | live | `50-selftest.log` | 13:58:44 | `29,995,008` |
| `net` | live | `51-net.log` | 14:00:03 | `30,248,960` |
| `latency` | live | `52-latency.log` | 14:07:52 | `30,519,296` |
| `disk` | live | `53-disk.log` | 14:08:05 | `28,553,216` |
| `verify` | live | `61-verify.log` | 14:08:28 | `28,151,808` |
| `host after` | live | `62-host-after.log` | 14:08:34 | `27,631,616` |
| `reclaim`, §9 | capture | none — B-RECLAIM-OWN, quoted from the session (§2.12) | 14:13:16 | `27,201,536` |

23 peaks, each under `36,219,906`.

The largest, `latency`'s `30,519,296` bytes on the live host, is above the Architect's `30,208,000`, from which
`MEM_FLOOR` was derived, and under the modelled host peak `36,219,906`. Every peak is under it.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-49-live-host-ipv4-keys`, from `origin/main` `a76d79f` |
| commit | `9515874e613de4987d490f8c4f5cd16fbca9b345` — `research/tz49-live-host.py`, new, 2,127 lines, SHA-256 `efcc5ead077b396fe18d243f3c65fa9824baca56e6db5312058971e0dfe6049b` |
| on `origin` | at 13:58:13 UTC, `ls-remote` `9515874…`, the worktree's `HEAD` |
| pull request | #47, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/47`, against `main`, opened 13:58:25 UTC with `gh pr create` |
| push route | the remote URL's own credential; `gh`'s fallback was not needed |
| Release | none — no file of this run is held by a Release (§9) |

**§3.1** — `10-number.log`, `11-worktree.log` and `12-fingerprint.log`'s last lines:

```
2026-11-19T13:57:45.912430371Z
fetch exit=0
[2026-11-19T13:57:46Z] origin/main a76d79f8ddb0a530a9dc6563d7e9cbd440520322: 117 paths under CryptoTZ/ and CryptoReports/; of the number TZ-49-: ['CryptoTZ/TZ-49-live-host-ipv4-keys.md'] and []
[2026-11-19T13:57:46Z] NUMBER PASS - 2 of 2
[2026-11-19T13:57:46Z] peak memory of this run: 26677248 bytes
[2026-11-19T13:57:46Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

```
2026-11-19T13:57:55.451124601Z
Preparing worktree (new branch 'tz-49-live-host-ipv4-keys')
branch 'tz-49-live-host-ipv4-keys' set up to track 'origin/main'.
HEAD is now at a76d79f Add files via upload
worktree exit=0
/root/tz49-work/wt/research/tz49-live-host.py 2127 113254 efcc5ead077b396fe18d243f3c65fa9824baca56e6db5312058971e0dfe6049b created
exit=0
```

```
[2026-11-19T13:57:55Z] FINGERPRINT PASS: revision 2026-11-19-a; anchors 6 of 6, 4 re-derived; rows 65: frozen 62 of 62 equal, tracked 2, reported 1
[2026-11-19T13:57:55Z] peak memory of this run: 27725824 bytes
[2026-11-19T13:57:55Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
```

**`13-push.log`**, whole — `I0 refs`, the commit, the push, then the instant, the hash on `origin`, the worktree's
`HEAD` and the diff:

```
2026-11-19T13:58:07.678063244Z
[2026-11-19T13:58:08Z] REF a76d79f8ddb0a530a9dc6563d7e9cbd440520322	HEAD
[2026-11-19T13:58:08Z] REF a76d79f8ddb0a530a9dc6563d7e9cbd440520322	refs/heads/main
[2026-11-19T13:58:08Z] REFS HEAD                                     1
[2026-11-19T13:58:08Z] REFS refs/heads/main                          1
[2026-11-19T13:58:08Z] REFS refs/heads/tz-*                          22
[2026-11-19T13:58:08Z] REFS refs/pull/*/head                         45
[2026-11-19T13:58:08Z] REFS refs/tags/pairbook-streams-*             59
[2026-11-19T13:58:08Z] REFS refs/tags/rewardbook-streams-*           48
[2026-11-19T13:58:08Z] REFS refs/tags/tz-01a-dataset                 1
[2026-11-19T13:58:08Z] REFS refs/tags/tz-01a-dataset^{}              1
[2026-11-19T13:58:08Z] REFS refs/tags/tz-27-pairbook-streams         1
[2026-11-19T13:58:08Z] REFS refs/tags/tz-27-pairbook-streams^{}      1
[2026-11-19T13:58:08Z] REFS refs/tags/tz-44-l0-inputs                1
[2026-11-19T13:58:08Z] REFS refs/tags/tz-45-l0-rule-w-inputs         1
[2026-11-19T13:58:08Z] REFS 182 lines; refs/heads/tz-49-live-host-ipv4-keys absent
[2026-11-19T13:58:08Z] peak memory of this run: 26677248 bytes
[2026-11-19T13:58:08Z] refused by the hook: 0; lookups 0, requests 0, handshakes 0, TCP connects 0
exit=0
commit exit=0
remote: 
remote: Create a pull request for 'tz-49-live-host-ipv4-keys' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-49-live-host-ipv4-keys        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-49-live-host-ipv4-keys -> tz-49-live-host-ipv4-keys
branch 'tz-49-live-host-ipv4-keys' set up to track 'origin/tz-49-live-host-ipv4-keys'.
push exit=0
2026-11-19T13:58:13.835366604Z
9515874e613de4987d490f8c4f5cd16fbca9b345	refs/heads/tz-49-live-host-ipv4-keys
9515874e613de4987d490f8c4f5cd16fbca9b345
2127	0	research/tz49-live-host.py
```

**`14-pr.log`**:

```
2026-11-19T13:58:25.272532911Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/47
exit=0
```

**Contract §4.2's self-check** — `99-selfcheck.log`, `C` = `9515874e613de4987d490f8c4f5cd16fbca9b345`. `grep -c`
prints `0`; the diff names one path, `2127 0`; and the `.parquet`/`.zip` search prints nothing, its `grep` exiting
`1`:

```
2026-11-19T14:08:57.859459309Z
fetch exit=0
0
research/tz49-live-host.py
2127	0	research/tz49-live-host.py
grep exit=1
```

---

## 4. Gate

**§4.9: KEEP.** G-GEO, G-SPEC and G-NET read PASS. G-LAT does not decide the host; it read PASS, so L1's replay keeps
50 ms one way (§1.8 item 6).

| gate | the TZ's PASS | deciding number | reading |
|---|---|---|---|
| **G-GEO** | status 200, `blocked` the boolean `false`, `country` two capital letters | status `200`, `blocked False`, `country 'BG'`, at read 1 of 3 | **PASS** |
| **G-SPEC** | `MemTotal` at least `1,800,000,000`; root file system at least `18,000,000,000` | `1,944,465,408`; `20,779,339,776` — before and after | **PASS, 2 of 2** |
| **G-NET** | N1, N2 and N3 each pass at one of at most three reads 30 s apart | each at read 1 | **PASS, 3 of 3** |
| **G-LAT** | at least 570 valid, nearest-rank median at most `100,000,000` ns | 600 valid; median `56,295,867` ns = **56.296 ms**; one-way bound **28.148 ms** against 50.000 ms | **PASS** |
| **G-SWAP** | seven checks, §4.5 | S1 to S7 | **PASS, 7 of 7** |
| **G-LOG** | six checks, §4.6 | G1 to G6 | **PASS, 6 of 6** |
| **G-SSH** | six checks, §4.7 | K1 to K5 on the live host; K6 `['publickey']` from outside | **PASS, 6 of 6** |

Nothing was tuned to reach any gate, and no gate was reinterpreted. Every reading is the first read of its mode.

---

## 5. Validation

- **V1 — asserted.** `FINGERPRINT PASS` at §0.2, 13:55:36 UTC, and at §3.1, 13:57:55 UTC from the worktree's file:
  revision `2026-11-19-a`; anchors 6, 4 re-derived; rows `65` = `62` + `2` + `1`, 62 `frozen` equal.
- **V2 — asserted.** `NUMBER PASS - 2 of 2` at §0.5, 13:56:05 UTC, and at §3.1, 13:57:46 UTC. `refs` 182 lines at
  13:56:05 and 13:58:08 UTC, the branch absent before the push. Against §0.5's 182 lines, only `HEAD` and
  `refs/heads/main` differ, at `a76d79f`, the upload of TZ-49 (§2.9).
- **V3 — asserted by the script and by §0.6's reads.** §0.1's script created the one file, 2,127 lines, 113,254 bytes,
  `efcc5ead…`, at §0.1 and again at §3.1. The live host's copy has the same SHA-256, lines and bytes.
- **V4 — asserted by §3.1's reads.** One path, `--numstat` `2127 0`; the commit on `origin`, `9515874…`, is the
  worktree's `HEAD`.
- **V5 — asserted.** The capture host gate, 7 of 7: H1, H2 (two), H3, H4, the memory gate `271,249,408` and the disk
  gate `10,563,932,160`. The room's margin `2,874,778,827`, printed.
- **V6 — asserted by §0.6's reads.** `R true` `exit=0` at its first read, 13:56:11 UTC. The key's fingerprint, the
  alias's settings without its address, the pinned key TZ-47's, `vs-2348`, `root`, `work tree exit=1`. B-ACCESS and
  B-ACCESS-KEY were not handed over.
- **V7 — asserted.** The live host gate, LH1 to LH5, 5 of 5, at `host before`, again at `host after`, and at the start
  of every live mode (`assert_live`). Its floors: `MemAvailable` `1,502,191,616` against `72,439,812`; `/`
  `16,987,779,072` against `2,515,919,104`.
- **V8 — asserted.** `G-GEO PASS over IPv4 alone`, one read, `blocked False`, `country 'BG'`. IPv6's state beside it:
  1 global address, 2 default routes, 0 usable.
- **V9 — asserted.** `SELFTEST PASS: 51 checks, 51 passed` on the capture host at 13:58:35 UTC and on the live host at
  13:58:44 UTC, each with `refused by the hook: 4`, its own.
- **V10 — asserted where it ran.** `scratch` listed seven directories beside this session's own: four earlier, three
  live. `RECLAIM PASS` named the four earlier, and each removal's `test -e` read `exit=1`.
- **V11 — printed, exit `0`.** `G-SPEC PASS: 2 of 2` at `host before` and at `host after`.
- **V12 — printed, exit `0`.** The package manager read `inactive` `inactive` at 13:59:22, 14:00:13 and 14:07:58 UTC,
  each at its first read. `G-NET PASS: 3 of 3`, every read's line in §2.4. The 60 handshakes all completed, with a
  median of `0.917` ms.
- **V13 — printed, exit `0`.** `G-LAT PASS`: counted 600, valid 600; p5 `53.804`, p50 `56.296`, p95 `63.941`, p99
  `90.518`, max `225.146` ms; the halves' medians `56.628` and `55.950` ms; the one-way bound `28.148` ms against
  `50.000`. Every request's line is in §2.5.
- **V14 — recorded, not asserted.** The disk wrote `1,209,487,627` bytes a second; its fsyncs had a median of 0.501 ms,
  a 99th percentile of 1.005 ms and a maximum of 1.716 ms. Its test files were removed: `True`.
- **V15 — printed, exit `0`.** B-CONFIGURE: `files exit=0`, `rsyslog exit=0`, `swap exit=0`, the swap file `600 0 0`
  before and after. Then `G-SWAP PASS: 7 of 7` and `G-LOG PASS: 6 of 6`.
- **V16 — asserted where a command asserts it.** §3.9: `scp exit=0` and `diff exit=0`. The guard read `inactive`
  twice, its timer and its service. The capture host's units read as at §0.3: the same `MainPID`, `NRestarts` and
  `ActiveState`. Contract §4.2's self-check: `0`, one path, `2127 0`, nothing.
- **V17 — recorded.** Every mode's peak is in §2.13: the largest `30,519,296`, each under `36,219,906`. Every memory
  and free-space read is listed there with its instant and its floor.
- **V18 — asserted where a command asserts it.** §9: `RECLAIM PASS`, 35 of 35 copied, the forensic store 2,592 → 2,627 files. `/root/tz49-work` is gone on both hosts, `test -e` `exit=1` each. The capture host's worktrees are the primary checkout and `/root/btc-recorder-svc`.
- **V19 — B-SSH and C-SSH asserted by their own lines; G-SSH printed, exit `0`.** The methods before:
  `['publickey,password']`. `files`' four lines at their SHA-256. B-SSH's log whole, its last line `B-SSH exit=0`. One
  C-SSH read, at 13:57:30.897 UTC, `CONFIRMED` — B-SSH kept. Then `G-SSH on the live host PASS: 5 of 5` and
  `G-SSH K6 publickey alone, from outside: PASS`.

---

## 6. What could not be implemented as written

Nothing of TZ-49 was left out or replaced. Every step ran in §3's order, the Executor ran every block itself, and the
classifier refused nothing, so **no block was handed to the Boss**. Named plainly:

1. **The session directories, by the rule alone.** Map §3 names `ccca2df8-e51d-56bc-8205-06299775095a` TZ-46's own.
   `scratch` read it born 2026-11-15T10:28:57Z, within 60 s of the start of the three running `claude` processes of
   10:28:51 to 10:28:53 UTC, so it named it **live**. It was not reclaimed: §3.3's rule decides, not the map's naming.
   `95cf58d2-…` read live, as map §3 says. `6ce33308-…`, born with this session's process `2385301` at 13:53:23 UTC,
   read live too.
2. **`/swap.img` was already `0600` and root's** at `host before` and at B-CONFIGURE's first `stat`. The block's
   `chmod`/`chown` branch did not run, and the file's state reads `600 0 0` before and after. Nothing of the swap
   changed but `vm.swappiness`.
3. **The refs read** differs from the Architect's in one kind alone: `HEAD` and `refs/heads/main` are at `a76d79f`,
   the upload of this TZ, where §0.5 read `6e9e580`. §0.5 asks for this to be recorded, not BLOCKED.
4. **`latency`'s peak, `30,519,296` bytes on the live host, is above the `30,208,000` the Architect measured**, from
   which `MEM_FLOOR` was derived, and under the modelled host peak `36,219,906` (§0.4). V17 records it and asserts
   nothing.
5. **B-RECLAIM-LIVE's instant** was read by a `date -u` after its command, in the same call. Its output is quoted from
   the session (§2.12), because §3's table names no log for it.
6. **Prints:** `net`'s `DNS` line prints the venue's own IPv4 addresses, as the mode was written to print them. They
   are the venue's, not either host's, and are quoted whole.
7. **`/var/log/btmp` on the live host** read `5,976,064` bytes at `host before` and `6,012,928` at `host after`, twelve
   minutes later and eleven minutes after B-SSH. That is the record of failed logins, printed by size and not
   counted. No reading uses it.
