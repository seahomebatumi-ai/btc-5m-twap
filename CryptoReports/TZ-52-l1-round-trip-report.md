# TZ-52 — L1, the round trip on the account TZ-51 left — REPORT

**Status: BLOCKED at §3.9, G-RT. The venue took the order live, then answered the read-back of the order by its id
with `null`. The instrument does not handle that answer, so the round trip stopped with `exit=1`, its last act
`cancel_all` cancelled the order, and no record was written. G-RT was not read.**

`LC roundtrip` began at 22:50:31 UTC on 2026-11-20 (`75-roundtrip.log`, §2.1):

- The clock read NTP-synchronized.
- The market `btc-updown-5m-1795215000` read eligible, CTF, with `267` s left in its window.
- The client signs for the CTF exchange, and the wallet's allowance on chain to it reads `max`.
- **Placement 1, a post-only GTC buy of `5` Up at `0.01`, was accepted `live` in `127` ms** at 22:50:33.
- The next call, `get_order` by the order's id (`roundtrip_flow`, line 2326), raised the client's
  `UnexpectedResponseError: OpenOrder response did not match expected shape`. The cause under it is pydantic's
  `Input should be a valid dictionary or instance of OpenOrder [type=model_type, input_value=None,
  input_type=NoneType]`: the CLOB answered the read with `null`.
- `roundtrip_flow`'s `finally` ran its last act, **`cancel_all` of the key: `{'canceled': 1, 'not_canceled': 0}`**.
- The exception left `mode_roundtrip` before it writes the record (line 2381), and `main` printed the peak and
  `exit=1`.

**No record exists** (`76-record.log`), so G-RT's nine checks have nothing to read. TZ-51 §3.9 item 4 says "a round
trip that placed an order is never run again, whatever G-RT read", and TZ-52 §1.2 says "no other request to the
venue and no other attempt". The run went to TZ-51 §3.10 and §9.

- **The order:** placed once, live, and cancelled by the key's `cancel_all` within the same second. The
  venue's answer is `canceled` `1`, `not_canceled` `0`. G-READY had read no open order of the key or of the wallet at
  22:49:15, and the flow reads the key's open orders `0` before it places (line 2269). So the one order cancelled is
  this one. The read-back, the cancel by id, the read after, the open orders after and the balance after were **not
  read**: the flow never reached them. Its market's window closed at 22:55:00 UTC. **This run's loss is at most
  `0.05` pUSD**, one order of `5` at `0.01`, and only if part of it matched in the milliseconds before
  `cancel_all`. No reading shows that it did, and none shows that it did not.
- **Everything before §3.9 passed:**
  - FINGERPRINT PASS twice, revision `2026-11-21-a`, 64 of 64 `frozen` rows equal.
  - The instrument staged by §0.1's script, `created` at `a425e67c…`, then into the worktree and onto the live host
    at the same SHA-256.
  - Host gate 7 of 7. Room margin **2,758,864,077** bytes.
  - NUMBER PASS 2 of 2, twice. Refs read 200 lines, and the branch was absent before the push.
  - Access `exit=0`, the pinned host key, `vs-2348`, `root`, both trees absent.
  - Live host gate 5 of 5. **LS held:** root's keys the Executor's alone, and the nine `PATH` lines of §0.6.
  - **G-GEO PASS** at §0.6 and again at §3.9, `blocked False`, `country 'BG'`. **G-SSH 6 of 6**, before and after.
  - `SELFTEST PASS: 141 checks, 141 passed`, `refused by the hook: 5`, on both hosts.
  - `G-ENV installed PASS`. `SDK SELFTEST PASS: 32 checks, 32 passed`, `refused by the hook: 2`.
  - **G-KEY**: present, kept.
  - **G-READY PASS: 7 of 7** at 22:49:15. pUSD on chain `11.100000`, both allowances on chain `max`; the CLOB's view
    `11.100000`.
  - G-TG `getMe` PASS.
- **G-TG's chat PASS.** The Boss's `/start` sent before `EXECUTE` was not among the bot's updates: `find-chat`'s
  first read, at 22:50:36, found `0` pending. The Executor asked him once, at about 22:51 UTC. His `/start` reached
  the bot at 22:56:49, and the one private chat was pinned to `/etc/l1-bot/chat-id`, `0600`, by exclusive create.
  **G-TG's report message was not sent**: `tg-report` reads the last round trip's record, and there is none (§3
  item 4).
- **Branch** `tz-52-l1-round-trip` at `1719ff46d22444aa7a4f05e7a735cfc4856240ab`: one file, `3326 0`; **pull request
  #50**, open. **Pull request #49** was read `open`, `merged` `false`, head `bfbb104…`, and closed unmerged by
  `gh api` at 22:47; its branch is kept. The §4.2 self-check read `0`, one path, and nothing.
- **L1's paths on the live host, left as they stand** (TZ-51 §3, a BLOCK after §3.6), as `79-host-after.log` reads
  them (§2.4):
  - `/etc/l1-bot/` holds `session-key`, authorized for the wallet since TZ-51, `relayer-key`, `telegram-token`, and
    now `chat-id`, pinned by this run, each `0600` and root's.
  - `/var/lib/l1-bot/` holds `account.json`, TZ-51's kept instrument and this TZ's, `tz52-l1-account.py`, at §0.1's
    SHA-256.
  - `/root/l1-env/` is the client's environment, unchanged and read `G-ENV installed PASS`.
  - Root's `authorized_keys` holds the Executor's key alone.
- **The capture host:** no unit was started, stopped or touched, and no store was written. The recorder, the reward
  book and the advisor kept the same `MainPID`, `NRestarts` and `ActiveState` from §0.3 to the closing reads.
- **Handed to the Boss:** one ask, at about 22:51 UTC, in Russian: send `/start` to his L1 bot in Telegram (§3
  item 2). No block was handed over, and the classifier refused nothing.
- **No address of either host, of the bot's owner, wallet or session key, and no key, token, relayer key, signature,
  order id or chat id** is in this report. Of the live host's name, only its first label is given.

---

## 0. Fingerprint

`I0 fingerprint` (`logs/02-fingerprint.log`, 22:45:54 UTC) and `I fingerprint` from the branch's worktree
(`logs/12-fingerprint.log`, 22:47:20 UTC) each printed `FINGERPRINT PASS`. With the instants and the peak stripped,
their lines are equal (`diff` exit `0`).

```
[2026-11-20T22:45:54Z] FINGERPRINT PASS: revision 2026-11-21-a; anchors 6 of 6, 4 re-derived; rows 67: frozen 64 of 64 equal, tracked 2, reported 1; the signing page on main equal to TZ-50's Appendix B
```

This is §0.2's line, word for word. **Revision string:** `2026-11-21-a`. **Anchors:**

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
| `SYSTEM-MAP.md` | 1084 | 184835 | reported | `f20102a085c97a4b5297aa2c689eb8631964d7b714e93c93abc5cec5c76d5d85` |
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

**The model:** TZ-52's header names Claude Opus 5.5. The session's own record, read at the start of the run, names
the same model as configured and as last served.

---

## 1. The blocker

§3 step 12 is TZ-51 §3.9 with TZ-52 §1.2: `LC roundtrip`, G-RT (§4.8). `roundtrip_flow` places the order and, once
one placement reads `live`, reads it back by its id:

```python
        o1 = await c.get_order(order_id=oid)
```

(`research/tz52-l1-account.py`, line 2326.) The placement read `live` in `127` ms. The client's `get_order` passed the
CLOB's answer to `parse_open_order`, and pydantic refused it: `input_value=None, input_type=NoneType`. **The CLOB
answered the read of an order it had just accepted with `null`**, and the client raised `UnexpectedResponseError`. The
flow catches `RequestRejectedError` at the placement and at the read after the cancellation (lines 2310 and 2338),
not here, and not this class, so the exception left `roundtrip_flow` through its `finally`. That block ran the last
act, `cancel_all` of the key, `{'canceled': 1, 'not_canceled': 0}`, and closed the client. `mode_roundtrip` writes the
record after `asyncio.run` returns (lines 2378 to 2382), so **nothing was written and no G-RT line was printed**;
`main`'s `finally` printed the peak and the hook's counts, and the process ended with `exit=1`.

**What the venue said, and what it did not.** It said `live` to the placement, `null` to the order's read by its id
a moment after, and `canceled` `1` to `cancel_all`. So the matching engine held the order and cancelled it, while the
read by its id did not serve it at that instant. Why the read served `null` — an order store behind the engine, or
another cause — was not read: TZ-52 §1.2 allows no other request to the venue and no probe, and none was made.

**Why the self-tests passed.** The CLOB's loopback stand-in in `sdk-selftest` (`_clob`, lines 2665 to 2667) serves
`/data/order/<id>` from the order it has just stored, or `404`, which the client raises as `RequestRejectedError`. It
never answers `null`, so no check met this shape. The answer exists only at the venue.

**Why it cannot be run again in this TZ.** TZ-51 §3.9 item 4: "a round trip that placed an order is never run again,
whatever G-RT read"; TZ-52 §1.2: "no other request to the venue and no other attempt". The mode's own guard would
not stop a second run here. `mode_roundtrip` refuses a run after a record whose `placements` is not empty (line
2376), and this failure left no record. The Executor ran nothing more (§3 item 5).

**What TZ-52 §1.2 names, and what it does not.** §1.2 fixes the run's course where the CLOB refuses the placement:
the record holds the venue's words, G-RT reads FAIL, and the run is BLOCKED. Here the CLOB accepted the placement,
and the next read of the order was answered `null`. §1.2 does not name that case, and neither does TZ-51. TZ-51 §3's
rule for a BLOCK applies, with TZ-52 §1.2's "the run goes to TZ-51 §3.10 and §9".

---

## 2. The evidence

Every live host's log below is quoted whole as §3.10's copy brought it back, byte for byte (`diff exit=0`, §2.7). Its
SHA-256 is in §2.8. Its copy in the forensic store is `/root/btc-forensics/tz52-work--<path with / as -->`.

### 2.1 The round trip — `74-geoblock.log`, `75-roundtrip.log` and `76-record.log`

**`74-geoblock.log`**, whole: G-GEO immediately before the order (TZ-51 §3.9 item 1), PASS.

```
2026-11-20T22:50:21.546599437Z
[2026-11-20T22:50:21Z] MemAvailable read 1: 1424728064 bytes, floor 86426834
[2026-11-20T22:50:21Z] available on /: 16913461248 bytes, floor 2447483648
[2026-11-20T22:50:21Z] G-GEO read 1 over IPv4: status 200, 68 bytes, blocked False, country 'BG', region '22', keys ['blocked', 'country', 'ip', 'region']; the address the venue saw is the connection's own: True -> PASS
[2026-11-20T22:50:21Z] G-GEO PASS
[2026-11-20T22:50:21Z] peak memory of this run: 37687296 bytes
[2026-11-20T22:50:21Z] refused by the hook: 0; lookups 1, requests 1
exit=0
```

**`75-roundtrip.log`**, whole: the round trip, its one placement, the exception and the last act.

```
2026-11-20T22:50:31.093530272Z
[2026-11-20T22:50:31Z] MemAvailable read 1: 1425420288 bytes, floor 274917678
[2026-11-20T22:50:31Z] available on /: 16913457152 bytes, floor 2447483648
[2026-11-20T22:50:31Z] RT clock NTP-synchronized: True
[2026-11-20T22:50:32Z] RT market btc-updown-5m-1795215000: gamma status 200, eligible, CTF; 267 s left in its window
[2026-11-20T22:50:33Z] RT the client signs for the CTF exchange: True; the wallet's allowance on chain to it max pUSD
[2026-11-20T22:50:33Z] RT placement 1: BUY 5 Up at 0.01, post-only, GTC: live in 127 ms
[2026-11-20T22:50:33Z] RT the last act, cancel_all of the key: {'canceled': 1, 'not_canceled': 0}
[2026-11-20T22:50:33Z] peak memory of this run: 91828224 bytes
[2026-11-20T22:50:33Z] refused by the hook: 0; lookups 8, requests 5
Traceback (most recent call last):
  File "/root/l1-env/lib/python3.12/site-packages/polymarket/models/base.py", line 24, in parse_response
    return cls.model_validate(data)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/l1-env/lib/python3.12/site-packages/pydantic/main.py", line 792, in model_validate
    return cls.__pydantic_validator__.validate_python(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 1 validation error for OpenOrder
  Input should be a valid dictionary or instance of OpenOrder [type=model_type, input_value=None, input_type=NoneType]
    For further information visit https://errors.pydantic.dev/2.14/v/model_type

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/root/tz52-work/tz52-l1-account.py", line 3326, in <module>
    sys.exit(main(sys.argv[1:]))
             ^^^^^^^^^^^^^^^^^^
  File "/root/tz52-work/tz52-l1-account.py", line 3318, in main
    rc = table[mode]()
         ^^^^^^^^^^^^^
  File "/root/tz52-work/tz52-l1-account.py", line 2378, in mode_roundtrip
    rt = asyncio.run(roundtrip_flow(k, k.PRODUCTION, load_session_key(), acct))
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/asyncio/base_events.py", line 687, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/root/tz52-work/tz52-l1-account.py", line 2326, in roundtrip_flow
    o1 = await c.get_order(order_id=oid)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/l1-env/lib/python3.12/site-packages/polymarket/clients/async_secure.py", line 2567, in get_order
    return _account_actions.parse_open_order(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/l1-env/lib/python3.12/site-packages/polymarket/_internal/actions/account.py", line 153, in parse_open_order
    return OpenOrder.parse_response(data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/l1-env/lib/python3.12/site-packages/polymarket/models/base.py", line 26, in parse_response
    raise UnexpectedResponseError(
polymarket.errors.UnexpectedResponseError: OpenOrder response did not match expected shape
exit=1
```

**`76-record.log`**, whole (TZ-51 §3.9 item 3): no record of this TZ under `/var/lib/l1-bot/`. CANON hard rule 16's
record does not exist, and `75-roundtrip.log` above is everything the round trip printed.

```
2026-11-20T22:51:49.425881912Z
cat: '/var/lib/l1-bot/tz52-roundtrip-*.json': No such file or directory
total 196
drwx------  2 root root   4096 Nov 20 19:28 .
drwxr-xr-x 41 root root   4096 Nov 20 18:10 ..
-rw-------  1 root root    310 Nov 20 19:18 account.json
-rw-------  1 root root 187351 Nov 20 19:28 tz51-l1-account.py
```

**G-RT, check by check**, as far as the log reads them. The gate is defined over the record, and no record exists, so
**none is asserted**:

| # | check | what the log shows |
|---|---|---|
| 1 | one placement accepted live, the last | placement 1 `live` in `127` ms, the only one |
| 2 | at most two placements | one |
| 3 | every earlier one refused as crossing the book | none earlier |
| 4 | read back `LIVE` at `0.01`, `5`, `BUY`, `GTC`, nothing matched, maker the wallet, asset the token | **not read**: the read-back answered `null` |
| 5 | cancelled by its own request | **not reached**; `cancel_all` of the key cancelled `1`, `0` not cancelled |
| 6 | read back cancelled, nothing matched | **not reached** |
| 7 | no open order of the key after it | **not reached** |
| 8 | none of the wallet by the key | **not reached** |
| 9 | the wallet's pUSD on chain after equal to before | **not reached**; the balance before was read (G-READY's `11.100000` at 22:49:15), the one the flow read is not printed |

### 2.2 The account — `71-ready.log`

**`71-ready.log`**, whole: **G-READY PASS: 7 of 7**. Checks (4) and (5) read each allowance on chain at least one
order's cost, as TZ-52 §4 words them; both read `max`.

```
2026-11-20T22:49:12.778888794Z
[2026-11-20T22:49:12Z] MemAvailable read 1: 1425723392 bytes, floor 274917678
[2026-11-20T22:49:12Z] available on /: 16913477632 bytes, floor 2447483648
[2026-11-20T22:49:15Z] READY pUSD on chain 11.100000, allowances on chain {'c': 'max', 'v': 'max'}; the CLOB's view 11.100000 pUSD, allowances 4, at least one order's cost 4
[2026-11-20T22:49:15Z] G-READY a Deposit Wallet signed for by a session key: PASS
[2026-11-20T22:49:15Z] G-READY not in closed-only mode: PASS
[2026-11-20T22:49:15Z] G-READY its pUSD on chain at least one order's cost: PASS
[2026-11-20T22:49:15Z] G-READY its allowance on chain to the CTF exchange at least one order's cost: PASS
[2026-11-20T22:49:15Z] G-READY its allowance on chain to the V2 exchange at least one order's cost: PASS
[2026-11-20T22:49:15Z] G-READY no open order of the key: PASS
[2026-11-20T22:49:15Z] G-READY no open order of the wallet by the key: PASS
[2026-11-20T22:49:15Z] G-READY PASS: 7 of 7
[2026-11-20T22:49:15Z] peak memory of this run: 91697152 bytes
[2026-11-20T22:49:15Z] refused by the hook: 0; lookups 6, requests 4
exit=0
```

### 2.3 Telegram — `72-tg-probe.log` and `73-find-chat.log`

**`72-tg-probe.log`**, whole: G-TG's first check, `getMe`, PASS.

```
2026-11-20T22:49:20.601889946Z
[2026-11-20T22:49:38Z] G-TG getMe: a bot with a username - its name withheld, as a public report would publish it - 0 commands in its menu: PASS
[2026-11-20T22:49:38Z] peak memory of this run: 37556224 bytes
[2026-11-20T22:49:38Z] refused by the hook: 0; lookups 2, requests 2
exit=0
```

**`73-find-chat.log`**, whole: G-TG's second check. Its first `getUpdates` at 22:50:36 found `0` pending updates. The
Boss's `/start` sent before `EXECUTE` was not among them, so the Executor asked him once (§3 item 2). At 22:56:49 one
update came, the one private chat that sent `/start`, and it was pinned: **G-TG chat PASS**.

```
2026-11-20T22:49:46.377930020Z
[2026-11-20T22:50:36Z] G-TG chat: no /start among 0 pending updates; waiting up to 1800 s for the Boss's /start
[2026-11-20T22:56:49Z] G-TG chat: updates 1, private chats that sent /start: 1, pinned to /etc/l1-bot/chat-id
[2026-11-20T22:56:49Z] peak memory of this run: 37556224 bytes
[2026-11-20T22:56:49Z] refused by the hook: 0; lookups 9, requests 9
exit=0
```

**G-TG's third check was not read**: `tg-report` sends the last round trip's record's report, and `mode_tg_report`
asserts one exists (line 1721). None does, so it was not run (§3 item 4).

### 2.4 The live host after it — §3.10 items 1 to 3

**`79-host-after.log`**, whole: the live host gate, 5 of 5, and L1's paths. Against `host before` (§2.5), `chat-id` is
now present, `0600`, root's, `10` bytes, pinned by `find-chat`. Root's keys, the locale, the clock, every other `PATH`
line and `wheels` (absent) read the same. `tz52-l1-account.py`, which `host` does not list, is in `81-keep.log`.

```
2026-11-20T22:57:01.674988715Z
[2026-11-20T22:57:01Z] LH1 hostname vs-2348: PASS
[2026-11-20T22:57:01Z] LH2 Ubuntu 24.04: PASS
[2026-11-20T22:57:01Z] LH3 Python 3.12: PASS
[2026-11-20T22:57:01Z] LH4 not the capture host: PASS
[2026-11-20T22:57:01Z] LH5 the host key pinned at TZ-47's first connection: PASS
[2026-11-20T22:57:01Z] LIVE HOST GATE PASS: 5 of 5
[2026-11-20T22:57:01Z] MemAvailable read 1: 1452183552 bytes, floor 86426834
[2026-11-20T22:57:01Z] available on /: 16913440768 bytes, floor 2447483648
[2026-11-20T22:57:01Z] HOST after: kernel 6.8.0-138-generic; Python 3.12.3; Ubuntu 24.04.5 LTS; MemTotal 1944465408 MemAvailable 1452183552 SwapTotal 1073737728 SwapFree 1073737728; / 20779339776 bytes, 16913440768 available
[2026-11-20T22:57:01Z] LOCALE /etc/default/locale: LANG="ru_UA.UTF-8"
[2026-11-20T22:57:01Z] LOCALE `locale` in this session, exit 0: LANG=ru_UA.UTF-8; LANGUAGE=; LC_CTYPE="C"; LC_NUMERIC="C"; LC_TIME="C"; LC_COLLATE="C"; LC_MONETARY="C"; LC_MESSAGES="C"; LC_PAPER="C"; LC_NAME="C"; LC_ADDRESS="C"; LC_TELEPHONE="C"; LC_MEASUREMENT="C"; LC_IDENTIFICATION="C"; LC_ALL=C
[2026-11-20T22:57:01Z] CLOCK exit 0: NTP=yes; NTPSynchronized=yes; TimeUSec=Fri 2026-11-20 22:57:01 UTC
[2026-11-20T22:57:01Z] SSHD authorized keys of root: [('ssh-ed25519', 'SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo')]; the Executor's among them: True
[2026-11-20T22:57:01Z] PATH /etc/l1-bot: dir mode 0700 uid 0 bytes 4096
[2026-11-20T22:57:01Z] PATH /etc/l1-bot/session-key: file mode 0600 uid 0 bytes 67
[2026-11-20T22:57:01Z] PATH /etc/l1-bot/relayer-key: file mode 0600 uid 0 bytes 105
[2026-11-20T22:57:01Z] PATH /etc/l1-bot/telegram-token: file mode 0600 uid 0 bytes 47
[2026-11-20T22:57:01Z] PATH /etc/l1-bot/chat-id: file mode 0600 uid 0 bytes 10
[2026-11-20T22:57:01Z] PATH /var/lib/l1-bot: dir mode 0700 uid 0 bytes 4096
[2026-11-20T22:57:01Z] PATH /var/lib/l1-bot/account.json: file mode 0600 uid 0 bytes 310
[2026-11-20T22:57:01Z] PATH /root/l1-env: dir mode 0755 uid 0 bytes 4096
[2026-11-20T22:57:01Z] PATH /root/tz52-work/wheels: absent
[2026-11-20T22:57:01Z] peak memory of this run: 35049472 bytes
[2026-11-20T22:57:01Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**`78-sshd-after.log`** and **`88-methods-after.log`**, whole: **G-SSH after**, K1 to K5 and K6, 6 of 6.

```
2026-11-20T22:51:56.652639221Z
[2026-11-20T22:51:56Z] K1 TZ-49's sshd drop-in, byte for byte: PASS
[2026-11-20T22:51:56Z] K2 passwordauthentication no: PASS
[2026-11-20T22:51:56Z] K3 kbdinteractiveauthentication no: PASS
[2026-11-20T22:51:56Z] K4 permitrootlogin without-password: PASS
[2026-11-20T22:51:56Z] K5 pubkeyauthentication yes: PASS
[2026-11-20T22:51:56Z] G-SSH K1 to K5 PASS: 5 of 5
[2026-11-20T22:51:56Z] peak memory of this run: 35069952 bytes
[2026-11-20T22:51:56Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-20T22:51:56.848287687Z
[2026-11-20T22:51:57Z] METHODS after: the methods the live host's sshd offers root, from outside: ['publickey']; ssh exit 255
[2026-11-20T22:51:57Z] G-SSH K6 publickey alone, from outside: PASS
[2026-11-20T22:51:57Z] peak memory of this run: 34484224 bytes
[2026-11-20T22:51:57Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**`81-keep.log`**, whole: §3.10 item 3, this TZ's instrument kept at `/var/lib/l1-bot/tz52-l1-account.py`, beside
TZ-51's copy, at §0.1's SHA-256.

```
2026-11-20T22:57:02.573552814Z
a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366  /var/lib/l1-bot/tz52-l1-account.py
exit=0
/etc/l1-bot:
total 24
drwx------   2 root root 4096 Nov 20 22:56 .
drwxr-xr-x 107 root root 4096 Nov 20 06:25 ..
-rw-------   1 root root   10 Nov 20 22:56 chat-id
-rw-------   1 root root  105 Nov 20 18:10 relayer-key
-rw-------   1 root root   67 Nov 20 06:25 session-key
-rw-------   1 root root   47 Nov 20 18:00 telegram-token

/var/lib/l1-bot:
total 384
drwx------  2 root root   4096 Nov 20 22:57 .
drwxr-xr-x 41 root root   4096 Nov 20 18:10 ..
-rw-------  1 root root    310 Nov 20 19:18 account.json
-rw-------  1 root root 187351 Nov 20 19:28 tz51-l1-account.py
-rw-------  1 root root 188720 Nov 20 22:57 tz52-l1-account.py
```

### 2.5 What passed before it — the live host

**`06-access.log`** and **`07-copy.log`**, whole: the access, TZ-47's pinned key, `vs-2348`, `root`, both trees
absent; the copy at §0.1's lines, bytes and SHA-256.

```
2026-11-20T22:46:27.813565597Z
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
2026-11-20T22:46:36.007476149Z
exit=0
scp exit=0
a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366  /root/tz52-work/tz52-l1-account.py
  3326 188720 /root/tz52-work/tz52-l1-account.py
```

**`40-host-before.log`**, whole: the live host gate, 5 of 5, and **LS**. Root's keys are the Executor's alone, and
the nine `PATH` lines are TZ-52 §0.6's, line for line.

```
2026-11-20T22:46:45.215704343Z
[2026-11-20T22:46:45Z] LH1 hostname vs-2348: PASS
[2026-11-20T22:46:45Z] LH2 Ubuntu 24.04: PASS
[2026-11-20T22:46:45Z] LH3 Python 3.12: PASS
[2026-11-20T22:46:45Z] LH4 not the capture host: PASS
[2026-11-20T22:46:45Z] LH5 the host key pinned at TZ-47's first connection: PASS
[2026-11-20T22:46:45Z] LIVE HOST GATE PASS: 5 of 5
[2026-11-20T22:46:45Z] MemAvailable read 1: 1455169536 bytes, floor 86426834
[2026-11-20T22:46:45Z] available on /: 16913534976 bytes, floor 2447483648
[2026-11-20T22:46:45Z] HOST before: kernel 6.8.0-138-generic; Python 3.12.3; Ubuntu 24.04.5 LTS; MemTotal 1944465408 MemAvailable 1455169536 SwapTotal 1073737728 SwapFree 1073737728; / 20779339776 bytes, 16913534976 available
[2026-11-20T22:46:45Z] LOCALE /etc/default/locale: LANG="ru_UA.UTF-8"
[2026-11-20T22:46:45Z] LOCALE `locale` in this session, exit 0: LANG=ru_UA.UTF-8; LANGUAGE=; LC_CTYPE="C"; LC_NUMERIC="C"; LC_TIME="C"; LC_COLLATE="C"; LC_MONETARY="C"; LC_MESSAGES="C"; LC_PAPER="C"; LC_NAME="C"; LC_ADDRESS="C"; LC_TELEPHONE="C"; LC_MEASUREMENT="C"; LC_IDENTIFICATION="C"; LC_ALL=C
[2026-11-20T22:46:45Z] CLOCK exit 0: NTP=yes; NTPSynchronized=yes; TimeUSec=Fri 2026-11-20 22:46:45 UTC
[2026-11-20T22:46:45Z] SSHD authorized keys of root: [('ssh-ed25519', 'SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo')]; the Executor's among them: True
[2026-11-20T22:46:45Z] PATH /etc/l1-bot: dir mode 0700 uid 0 bytes 4096
[2026-11-20T22:46:45Z] PATH /etc/l1-bot/session-key: file mode 0600 uid 0 bytes 67
[2026-11-20T22:46:45Z] PATH /etc/l1-bot/relayer-key: file mode 0600 uid 0 bytes 105
[2026-11-20T22:46:45Z] PATH /etc/l1-bot/telegram-token: file mode 0600 uid 0 bytes 47
[2026-11-20T22:46:45Z] PATH /etc/l1-bot/chat-id: absent
[2026-11-20T22:46:45Z] PATH /var/lib/l1-bot: dir mode 0700 uid 0 bytes 4096
[2026-11-20T22:46:45Z] PATH /var/lib/l1-bot/account.json: file mode 0600 uid 0 bytes 310
[2026-11-20T22:46:45Z] PATH /root/l1-env: dir mode 0755 uid 0 bytes 4096
[2026-11-20T22:46:45Z] PATH /root/tz52-work/wheels: absent
[2026-11-20T22:46:45Z] peak memory of this run: 35201024 bytes
[2026-11-20T22:46:45Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**`41-geoblock.log`**, whole: G-GEO at §0.6, PASS.

```
2026-11-20T22:46:51.858449505Z
[2026-11-20T22:46:51Z] MemAvailable read 1: 1454276608 bytes, floor 86426834
[2026-11-20T22:46:51Z] available on /: 16913514496 bytes, floor 2447483648
[2026-11-20T22:46:52Z] G-GEO read 1 over IPv4: status 200, 68 bytes, blocked False, country 'BG', region '22', keys ['blocked', 'country', 'ip', 'region']; the address the venue saw is the connection's own: True -> PASS
[2026-11-20T22:46:52Z] G-GEO PASS
[2026-11-20T22:46:52Z] peak memory of this run: 37691392 bytes
[2026-11-20T22:46:52Z] refused by the hook: 0; lookups 1, requests 1
exit=0
```

**`42-sshd.log`**, whole, with `08-methods.log` in §2.6: G-SSH K1 to K5.

```
2026-11-20T22:46:52.873131575Z
[2026-11-20T22:46:53Z] K1 TZ-49's sshd drop-in, byte for byte: PASS
[2026-11-20T22:46:53Z] K2 passwordauthentication no: PASS
[2026-11-20T22:46:53Z] K3 kbdinteractiveauthentication no: PASS
[2026-11-20T22:46:53Z] K4 permitrootlogin without-password: PASS
[2026-11-20T22:46:53Z] K5 pubkeyauthentication yes: PASS
[2026-11-20T22:46:53Z] G-SSH K1 to K5 PASS: 5 of 5
[2026-11-20T22:46:53Z] peak memory of this run: 35069952 bytes
[2026-11-20T22:46:53Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**`50-selftest.log`**: the self-test on the live host, 206 lines, SHA-256 in §2.8. Its new and
rewritten checks and its summary lines:

```
2026-11-20T22:47:54.202482275Z
[2026-11-20T22:47:54Z] ok   an allowance kept: at least one order's cost, the maximum the venue sets in, nothing above it
[2026-11-20T22:47:54Z] ok   a refusal in the venue's words: addresses, ids and keys masked, one line
[2026-11-20T22:47:54Z] ok   secrets at a real terminal: the token and the key read hidden, the address shown, a bad token asked again and the stray line typed after it discarded; the log holds none of them
[2026-11-20T22:47:54Z] ok   bosskey at a real terminal: the key read and appended on its own line
[2026-11-20T22:47:54Z] SELFTEST PASS: 141 checks, 141 passed; refused by the hook: 5, each a check's own
[2026-11-20T22:47:54Z] peak memory of this run: 35983360 bytes
[2026-11-20T22:47:54Z] refused by the hook: 5; lookups 0, requests 18
exit=0
```

**`53-env.log`**, whole: `G-ENV installed PASS`. `/root/l1-env` was present, and TZ-52 §3 step 7 runs no wheels and
no B-ENV.

```
2026-11-20T22:48:39.290463304Z
[2026-11-20T22:48:40Z] ENV interpreter 3.12.3, prefix /root/l1-env: PASS
[2026-11-20T22:48:40Z] ENV distributions: 34 installed, 34 pinned; missing [], extra [], another version []
[2026-11-20T22:48:40Z] ENV files: 1373 RECORD entries with a SHA-256 over 1367 paths, 6 of them listed by two distributions; absent [], another hash []
[2026-11-20T22:48:40Z] ENV the client polymarket-client 0.20.0; session keys 15534000 s, a batch 600 s; selectors {'authorize': '24017fae', 'revoke': 'e63f952f'}; hosts https://clob.polymarket.com, https://relayer-v2.polymarket.com, https://gamma-api.polymarket.com
[2026-11-20T22:48:40Z] G-ENV installed PASS
[2026-11-20T22:48:40Z] peak memory of this run: 76623872 bytes
[2026-11-20T22:48:40Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**`54-sdk-selftest.log`**: the client's self-test, 116 lines. Its `approve` cases, each now at
the maximum, against a stand-in relayer that refuses an approval of any other amount, its real-terminal check and its
summary lines:

```
2026-11-20T22:48:45.292948765Z
[2026-11-20T22:48:46Z] OWNER approve: the owner's Deposit Wallet derived (beacon) and deployed; its pUSD allowances on chain {'c': '0.000000', 'v': '0.000000'}
[2026-11-20T22:48:46Z] OWNER approve link 1: the owner's signature, recovered to the owner under the client's own typed data
[2026-11-20T22:48:46Z] OWNER approve: the relayer accepted the batch of 2, state STATE_NEW
[2026-11-20T22:48:46Z] OWNER approve: the relayer's transaction confirmed
[2026-11-20T22:48:46Z] OWNER approve read 1: allowances on chain {'c': 'max', 'v': 'max'}
[2026-11-20T22:48:47Z] ok   authorize and approve at a real terminal: two links shown with the addresses, two signatures typed back, the stray line typed after the first discarded; the log carries no address
[2026-11-20T22:48:49Z] OWNER approve: the owner's Deposit Wallet derived (beacon) and deployed; its pUSD allowances on chain {'c': 'max', 'v': '0.000000'}
[2026-11-20T22:48:49Z] OWNER approve link 1: the owner's signature, recovered to the owner under the client's own typed data
[2026-11-20T22:48:49Z] OWNER approve: the relayer accepted the batch of 1, state STATE_NEW
[2026-11-20T22:48:50Z] OWNER approve: the relayer's transaction confirmed
[2026-11-20T22:48:50Z] OWNER approve read 1: allowances on chain {'c': 'max', 'v': 'max'}
[2026-11-20T22:48:50Z] ok   approve, the CTF exchange at the maximum kept and the V2 exchange short: one link of x=v, set to the maximum
[2026-11-20T22:48:50Z] OWNER approve: the owner's Deposit Wallet derived (beacon) and deployed; its pUSD allowances on chain {'c': 'max', 'v': '0.000000'}
[2026-11-20T22:48:50Z] OWNER approve link 1: no owner's signature
[2026-11-20T22:48:50Z] OWNER approve link 2: the owner's signature, recovered to the owner under the client's own typed data
[2026-11-20T22:48:50Z] OWNER approve: the relayer accepted the batch of 1, state STATE_NEW
[2026-11-20T22:48:50Z] OWNER approve: the relayer's transaction confirmed
[2026-11-20T22:48:50Z] OWNER approve read 1: allowances on chain {'c': 'max', 'v': 'max'}
[2026-11-20T22:48:50Z] ok   approve, the V2 exchange short alone: an empty answer gives a second link, one call at the maximum, the CTF exchange's maximum kept
[2026-11-20T22:48:50Z] OWNER approve: the owner's Deposit Wallet derived (beacon) and deployed; its pUSD allowances on chain {'c': 'max', 'v': 'max'}
[2026-11-20T22:48:50Z] OWNER approve: every allowance at least one order's cost - kept, nothing to sign
[2026-11-20T22:48:50Z] ok   approve, both at the maximum: kept, nothing asked, nothing sent
[2026-11-20T22:48:59Z] SDK SELFTEST PASS: 32 checks, 32 passed; refused by the hook: 2, each a check's own
[2026-11-20T22:48:59Z] peak memory of this run: 97202176 bytes
[2026-11-20T22:48:59Z] refused by the hook: 2; lookups 0, requests 58
exit=0
```

**`56-key.log`**, whole: **G-KEY**, present and kept.

```
2026-11-20T22:49:04.556172103Z
[2026-11-20T22:49:04Z] MemAvailable read 1: 1448378368 bytes, floor 274917678
[2026-11-20T22:49:04Z] available on /: 16913481728 bytes, floor 2447483648
[2026-11-20T22:49:05Z] G-KEY /etc/l1-bot/session-key: present, kept; file mode 0600 uid 0 bytes 67
[2026-11-20T22:49:05Z] peak memory of this run: 76750848 bytes
[2026-11-20T22:49:05Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

### 2.6 What passed before it — the capture host and the branch

**§0.0 to §0.5:** `00-ready.log`, `01-stage.log`, `03-host-gate.log`, `04-room.log`, `05-number.log` and
`05-refs.log`, whole. The host gate holds its seven checks: one manifest path (H1); `/dev/vda2`, `31612203008`, and
`grep -c` `4` (H2); `3.12.3` (H3); five paths (H4); `MemAvailable` `240,349,184` at the first read (memory); `avail`
`10,466,246,656` (disk). The room's margin over `STREAM_FLOOR` and `PEAK` is **2,758,864,077** bytes, with no flag.

```
2026-11-20T22:45:35.239631660Z
ready=1: 10467246080 bytes free on /var/lib, 7795535636 needed; MemAvailable 279240704, 86426834 needed; at 1795214735 2026-11-20T22:45:35Z
```

```
/root/tz52-work/stage/research/tz52-l1-account.py 3326 188720 a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366 created
```

```
Fri Nov 20 10:46:08 PM UTC 2026
1795214768
2026-08-02 07:24:32
1
MemTotal:         978640 kB
MemAvailable:     213760 kB
SwapTotal:       3174396 kB
SwapFree:        2374136 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10466246656
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
407427110	/var/lib/btc-rewardbook
357367982	/root/btc-forensics
28793864	/root/.claude-8j
2704
disabled
exit=1
inactive
exit=3
/root/tz50-work exit=1
/root/.ssh/live-host exit=0
/tmp/tmux-0/btc-l1 exit=1
/root/btc-5m-twap       0a73d30 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/162a9fb6-80c1-5fc2-8efb-0d715f44d283/scratchpad
total 56
drwx------ 14 root root 4096 Nov 20 22:44 .
drwx------ 40 root root 4096 Nov 20 22:44 ..
drwx------  3 root root 4096 Nov 20 18:51 0736470b-13a0-4e8d-931f-5ecf4df19205
drwx------  4 root root 4096 Nov 20 17:49 08f6d3e8-a971-5f09-9e9e-6a186cab44a9
drwx------  4 root root 4096 Nov 20 22:44 162a9fb6-80c1-5fc2-8efb-0d715f44d283
drwx------  3 root root 4096 Nov 20 17:49 1bc20379-a33f-40ce-b0b5-90d24dce9fbc
drwx------  3 root root 4096 Nov 20 06:18 3aceaaa9-a0d9-43c5-8e74-334a8c19adf5
drwx------  5 root root 4096 Nov 20 19:13 450e33c9-580a-5524-ad84-641183f6ef0c
drwx------  3 root root 4096 Nov 20 22:44 5b734feb-443a-4557-9e38-5fb2090365b2
drwx------  3 root root 4096 Nov 20 18:51 6f0f41a7-6da7-5e8a-80e1-a2a85a4a8e5c
drwx------  3 root root 4096 Nov 15 10:28 95cf58d2-1ec6-4c73-a622-38d04665f5ae
drwx------  4 root root 4096 Nov 17 14:14 ccca2df8-e51d-56bc-8205-06299775095a
drwx------  3 root root 4096 Nov 20 18:55 dc25b96c-1173-470f-9a05-e5fdd91952fe
drwx------  4 root root 4096 Nov 20 06:18 fd493377-65e0-5920-8de8-844ba541b830
MemAvailable read 1 22:46:08: 240349184
```

```
2026-11-20T22:46:13.922879699Z
[2026-11-20T22:46:14Z] btc-rewardbook-archive.service read 1: inactive
[2026-11-20T22:46:14Z] MemAvailable read 1: 212832256 bytes, floor 86426834
[2026-11-20T22:46:14Z] available on /var/lib: 10466091008 bytes, floor 7795535636
[2026-11-20T22:46:14Z] ROOM: 10466091008 bytes available on /var/lib; the reward book's stream files 38308705 bytes in 3 files under 24 day directories; the room 10504399713; its margin over STREAM_FLOOR 7300000000 and PEAK 445535636: 2758864077 bytes
[2026-11-20T22:46:14Z] peak memory of this run: 34762752 bytes
[2026-11-20T22:46:14Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-20T22:46:17.831721076Z
[2026-11-20T22:46:17Z] origin/main 0a73d30fd07ba49f0853b875174b207371e52b6e: 123 paths under CryptoTZ/ and CryptoReports/; of the number TZ-52-: ['CryptoTZ/TZ-52-l1-round-trip.md'] and []
[2026-11-20T22:46:17Z] NUMBER PASS - 2 of 2
[2026-11-20T22:46:17Z] peak memory of this run: 34631680 bytes
[2026-11-20T22:46:17Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-20T22:46:17.962996164Z
[2026-11-20T22:46:18Z] REF 0a73d30fd07ba49f0853b875174b207371e52b6e	HEAD
[2026-11-20T22:46:18Z] REF 0a73d30fd07ba49f0853b875174b207371e52b6e	refs/heads/main
[2026-11-20T22:46:18Z] REFS HEAD                                     1
[2026-11-20T22:46:18Z] REFS refs/heads/main                          1
[2026-11-20T22:46:18Z] REFS refs/heads/tz-*                          25
[2026-11-20T22:46:18Z] REFS refs/pull/*/head                         48
[2026-11-20T22:46:18Z] REFS refs/pull/*/merge                        1
[2026-11-20T22:46:18Z] REFS refs/tags/pairbook-streams-*             59
[2026-11-20T22:46:18Z] REFS refs/tags/rewardbook-streams-*           59
[2026-11-20T22:46:18Z] REFS refs/tags/tz-01a-dataset                 1
[2026-11-20T22:46:18Z] REFS refs/tags/tz-01a-dataset^{}              1
[2026-11-20T22:46:18Z] REFS refs/tags/tz-27-pairbook-streams         1
[2026-11-20T22:46:18Z] REFS refs/tags/tz-27-pairbook-streams^{}      1
[2026-11-20T22:46:18Z] REFS refs/tags/tz-44-l0-inputs                1
[2026-11-20T22:46:18Z] REFS refs/tags/tz-45-l0-rule-w-inputs         1
[2026-11-20T22:46:18Z] REFS 200 lines; refs/heads/tz-52-l1-round-trip absent
[2026-11-20T22:46:18Z] peak memory of this run: 34762752 bytes
[2026-11-20T22:46:18Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**`08-methods.log`**, whole: G-SSH K6 at §0.6.

```
2026-11-20T22:46:56.886589700Z
[2026-11-20T22:46:57Z] METHODS gate: the methods the live host's sshd offers root, from outside: ['publickey']; ssh exit 255
[2026-11-20T22:46:57Z] G-SSH K6 publickey alone, from outside: PASS
[2026-11-20T22:46:57Z] peak memory of this run: 34750464 bytes
[2026-11-20T22:46:57Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**§3.1:** `10-number.log`, `11-worktree.log`, `13-push.log`, `14-pr.log` and `15-pr49.log`, whole. NUMBER PASS
again; the worktree's file `created` by §0.1's script at its SHA-256; the commit on `origin` the worktree's `HEAD`;
`--numstat` `3326 0`, one path; pull request #50 opened; pull request #49 read open and closed unmerged.
`12-fingerprint.log` is §0's second PASS.

```
2026-11-20T22:47:10.062960870Z
fetch exit=0
[2026-11-20T22:47:10Z] origin/main 0a73d30fd07ba49f0853b875174b207371e52b6e: 123 paths under CryptoTZ/ and CryptoReports/; of the number TZ-52-: ['CryptoTZ/TZ-52-l1-round-trip.md'] and []
[2026-11-20T22:47:10Z] NUMBER PASS - 2 of 2
[2026-11-20T22:47:10Z] peak memory of this run: 34746368 bytes
[2026-11-20T22:47:10Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-20T22:47:15.221081507Z
Preparing worktree (new branch 'tz-52-l1-round-trip')
branch 'tz-52-l1-round-trip' set up to track 'origin/main'.
HEAD is now at 0a73d30 Add files via upload
worktree exit=0
/root/tz52-work/wt/research/tz52-l1-account.py 3326 188720 a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366 created
exit=0
```

```
2026-11-20T22:47:26.001963263Z
[2026-11-20T22:47:26Z] REF 0a73d30fd07ba49f0853b875174b207371e52b6e	HEAD
[2026-11-20T22:47:26Z] REF 0a73d30fd07ba49f0853b875174b207371e52b6e	refs/heads/main
[2026-11-20T22:47:26Z] REFS HEAD                                     1
[2026-11-20T22:47:26Z] REFS refs/heads/main                          1
[2026-11-20T22:47:26Z] REFS refs/heads/tz-*                          25
[2026-11-20T22:47:26Z] REFS refs/pull/*/head                         48
[2026-11-20T22:47:26Z] REFS refs/pull/*/merge                        1
[2026-11-20T22:47:26Z] REFS refs/tags/pairbook-streams-*             59
[2026-11-20T22:47:26Z] REFS refs/tags/rewardbook-streams-*           59
[2026-11-20T22:47:26Z] REFS refs/tags/tz-01a-dataset                 1
[2026-11-20T22:47:26Z] REFS refs/tags/tz-01a-dataset^{}              1
[2026-11-20T22:47:26Z] REFS refs/tags/tz-27-pairbook-streams         1
[2026-11-20T22:47:26Z] REFS refs/tags/tz-27-pairbook-streams^{}      1
[2026-11-20T22:47:26Z] REFS refs/tags/tz-44-l0-inputs                1
[2026-11-20T22:47:26Z] REFS refs/tags/tz-45-l0-rule-w-inputs         1
[2026-11-20T22:47:26Z] REFS 200 lines; refs/heads/tz-52-l1-round-trip absent
[2026-11-20T22:47:26Z] peak memory of this run: 34762752 bytes
[2026-11-20T22:47:26Z] refused by the hook: 0; lookups 0, requests 0
exit=0
commit exit=0
remote: 
remote: Create a pull request for 'tz-52-l1-round-trip' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-52-l1-round-trip        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-52-l1-round-trip -> tz-52-l1-round-trip
branch 'tz-52-l1-round-trip' set up to track 'origin/tz-52-l1-round-trip'.
push exit=0
2026-11-20T22:47:28.428087390Z
1719ff46d22444aa7a4f05e7a735cfc4856240ab	refs/heads/tz-52-l1-round-trip
1719ff46d22444aa7a4f05e7a735cfc4856240ab
3326	0	research/tz52-l1-account.py
```

```
2026-11-20T22:47:32.607292913Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/50
exit=0
```

```
2026-11-20T22:47:37.280290144Z
{"head":"bfbb1041529f60045172dd95167d8096f6153fba","merged":false,"number":49,"state":"open"}
exit=0
{"head":"bfbb1041529f60045172dd95167d8096f6153fba","merged":false,"number":49,"state":"closed"}
exit=0
```

**§3.2:** `20-selftest.log`, the self-test on the capture host, 206 lines. Its summary lines:

```
2026-11-20T22:47:52.555907526Z
[2026-11-20T22:47:52Z] ok   an allowance kept: at least one order's cost, the maximum the venue sets in, nothing above it
[2026-11-20T22:47:52Z] ok   a refusal in the venue's words: addresses, ids and keys masked, one line
[2026-11-20T22:47:52Z] ok   secrets at a real terminal: the token and the key read hidden, the address shown, a bad token asked again and the stray line typed after it discarded; the log holds none of them
[2026-11-20T22:47:52Z] ok   bosskey at a real terminal: the key read and appended on its own line
[2026-11-20T22:47:53Z] SELFTEST PASS: 141 checks, 141 passed; refused by the hook: 5, each a check's own
[2026-11-20T22:47:53Z] peak memory of this run: 35794944 bytes
[2026-11-20T22:47:53Z] refused by the hook: 5; lookups 0, requests 18
exit=0
```

**§3.3:** `30-scratch.log` and `32-reclaim-scratch.log`, whole. `scratch` names six directories **earlier** and five
**live**, this session's own not among them. B-RECLAIM-SCRATCH ran for the six: `RECLAIM PASS`, then one `rm -rf` and
one `test -e` a directory, each `test -e` `exit=1`.

```
2026-11-20T22:47:58.984844907Z
[2026-11-20T22:47:59Z] running 2569924 started 2026-11-20T18:51:37Z claude
[2026-11-20T22:47:59Z] running 2569934 started 2026-11-20T18:51:39Z claude
[2026-11-20T22:47:59Z] running 2569943 started 2026-11-20T18:51:39Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-20T22:47:59Z] running 2569966 started 2026-11-20T18:51:41Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-20T22:47:59Z] running 2570476 started 2026-11-20T18:55:31Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-20T22:47:59Z] running 2593738 started 2026-11-20T22:44:37Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-20T22:47:59Z] 0736470b-13a0-4e8d-931f-5ecf4df19205 born 2026-11-20T18:51:41Z: live, process [2569924, 2569934, 2569943, 2569966]
[2026-11-20T22:47:59Z] 08f6d3e8-a971-5f09-9e9e-6a186cab44a9 born 2026-11-20T17:49:14Z: earlier
[2026-11-20T22:47:59Z] 1bc20379-a33f-40ce-b0b5-90d24dce9fbc born 2026-11-20T17:49:13Z: earlier
[2026-11-20T22:47:59Z] 3aceaaa9-a0d9-43c5-8e74-334a8c19adf5 born 2026-11-20T06:18:23Z: earlier
[2026-11-20T22:47:59Z] 450e33c9-580a-5524-ad84-641183f6ef0c born 2026-11-20T18:55:32Z: live, process [2570476]
[2026-11-20T22:47:59Z] 5b734feb-443a-4557-9e38-5fb2090365b2 born 2026-11-20T22:44:38Z: live, process [2593738]
[2026-11-20T22:47:59Z] 6f0f41a7-6da7-5e8a-80e1-a2a85a4a8e5c born 2026-11-20T18:51:42Z: live, process [2569924, 2569934, 2569943, 2569966]
[2026-11-20T22:47:59Z] 95cf58d2-1ec6-4c73-a622-38d04665f5ae born 2026-11-15T10:28:56Z: earlier
[2026-11-20T22:47:59Z] ccca2df8-e51d-56bc-8205-06299775095a born 2026-11-15T10:28:57Z: earlier
[2026-11-20T22:47:59Z] dc25b96c-1173-470f-9a05-e5fdd91952fe born 2026-11-20T18:55:31Z: live, process [2570476]
[2026-11-20T22:47:59Z] fd493377-65e0-5920-8de8-844ba541b830 born 2026-11-20T06:18:24Z: earlier
[2026-11-20T22:47:59Z] peak memory of this run: 35016704 bytes
[2026-11-20T22:47:59Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-20T22:48:22.128551201Z
[2026-11-20T22:48:22Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/08f6d3e8-a971-5f09-9e9e-6a186cab44a9, an earlier session's directory of 7 files: nothing of it is kept
[2026-11-20T22:48:22Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/1bc20379-a33f-40ce-b0b5-90d24dce9fbc, an earlier session's directory of 0 files: nothing of it is kept
[2026-11-20T22:48:22Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/3aceaaa9-a0d9-43c5-8e74-334a8c19adf5, an earlier session's directory of 0 files: nothing of it is kept
[2026-11-20T22:48:22Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/95cf58d2-1ec6-4c73-a622-38d04665f5ae, an earlier session's directory of 0 files: nothing of it is kept
[2026-11-20T22:48:22Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/ccca2df8-e51d-56bc-8205-06299775095a, an earlier session's directory of 3 files: nothing of it is kept
[2026-11-20T22:48:22Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/fd493377-65e0-5920-8de8-844ba541b830, an earlier session's directory of 10 files: nothing of it is kept
[2026-11-20T22:48:22Z] RECLAIM PASS: 0 files considered, 0 copied, 0 already held; the forensic store 2704 -> 2704 files
[2026-11-20T22:48:22Z] peak memory of this run: 35147776 bytes
[2026-11-20T22:48:22Z] refused by the hook: 0; lookups 0, requests 0
exit=0
2026-11-20T22:48:33.779087249Z
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
```

### 2.7 After the BLOCK — §3.10 items 5 to 7 and §9

**`80-live-copy.log`**, whole: every live host's log on the capture host, byte for byte, and **G-PRINT**.

```
2026-11-20T22:57:07.854573844Z
scp exit=0
diff exit=0
total 100
drwxr-xr-x 2 root root  4096 Nov 20 22:57 .
drwxr-xr-x 6 root root  4096 Nov 20 22:57 ..
-rw-r--r-- 1 root root  2184 Nov 20 22:57 40-host-before.log
-rw-r--r-- 1 root root   576 Nov 20 22:57 41-geoblock.log
-rw-r--r-- 1 root root   533 Nov 20 22:57 42-sshd.log
-rw-r--r-- 1 root root 19535 Nov 20 22:57 50-selftest.log
-rw-r--r-- 1 root root   813 Nov 20 22:57 53-env.log
-rw-r--r-- 1 root root 13600 Nov 20 22:57 54-sdk-selftest.log
-rw-r--r-- 1 root root   422 Nov 20 22:57 56-key.log
-rw-r--r-- 1 root root  1114 Nov 20 22:57 71-ready.log
-rw-r--r-- 1 root root   315 Nov 20 22:57 72-tg-probe.log
-rw-r--r-- 1 root root   392 Nov 20 22:57 73-find-chat.log
-rw-r--r-- 1 root root   576 Nov 20 22:57 74-geoblock.log
-rw-r--r-- 1 root root  3296 Nov 20 22:57 75-roundtrip.log
-rw-r--r-- 1 root root   326 Nov 20 22:57 76-record.log
-rw-r--r-- 1 root root   533 Nov 20 22:57 78-sshd-after.log
-rw-r--r-- 1 root root  2206 Nov 20 22:57 79-host-after.log
-rw-r--r-- 1 root root   775 Nov 20 22:57 81-keep.log
0
0
```

**`90-closing.log`**, whole: the closing reads of both hosts.

```
2026-11-20T22:57:17.680897249Z
Fri Nov 20 22:57:18 UTC 2026
               total        used        free      shared  buff/cache   available
Mem:      1944465408   469315584   798404608     1466368   850898944  1475149824
Swap:     1073737728           0  1073737728
Filesystem             1B-blocks       Avail
/dev/mapper/lvm-root 20779339776 16913227776
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
total 384
drwx------  2 root root   4096 Nov 20 22:57 .
drwxr-xr-x 41 root root   4096 Nov 20 18:10 ..
-rw-------  1 root root    310 Nov 20 19:18 account.json
-rw-------  1 root root 187351 Nov 20 19:28 tz51-l1-account.py
-rw-------  1 root root 188720 Nov 20 22:57 tz52-l1-account.py
/etc/l1-bot/chat-id 10 600 root
/etc/l1-bot/relayer-key 105 600 root
/etc/l1-bot/session-key 67 600 root
/etc/l1-bot/telegram-token 47 600 root
/var/lib/l1-bot/account.json 310 600 root
/var/lib/l1-bot/tz51-l1-account.py 187351 600 root
/var/lib/l1-bot/tz52-l1-account.py 188720 600 root
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
/dev/vda2      31612203008 10424528896
17760159	/root/tz52-work
421639344	/var/lib/btc-rewardbook
               total        used        free      shared  buff/cache   available
Mem:      1002127360   821137408   171708416       32768   153739264   180989952
Swap:     3250581504   970002432  2280579072
1719ff46d22444aa7a4f05e7a735cfc4856240ab	refs/heads/tz-52-l1-round-trip
```

**`99-selfcheck.log`**, whole: contract §4.2's self-check, `C` = `1719ff46d22444aa7a4f05e7a735cfc4856240ab`.

```
2026-11-20T22:57:22.489817830Z
0
research/tz52-l1-account.py
3326	0	research/tz52-l1-account.py
```

**§9, B-RECLAIM-LIVE**, run by the Executor, its instant read in the same call:

```
$ date -u +%FT%T.%NZ; ssh -T -o BatchMode=yes -o ConnectTimeout=20 -o LogLevel=QUIET live-host 'export LC_ALL=C; rm -rf /root/tz52-work; test -e /root/tz52-work; echo "exit=$?"'
2026-11-20T22:57:31.433622800Z
exit=1
```

**§9, B-RECLAIM-OWN.** Its output was written to no file and is quoted from the session, every line:

```
$ (cd /root/tz52-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz52-work/wt/research/tz52-l1-account.py reclaim /root/tz52-work); echo "reclaim exit=$?"
[2026-11-20T22:59:13Z] reclaim: /root/tz52-work/wt skipped: no file but its HEAD's, and HEAD 1719ff46d22444aa7a4f05e7a735cfc4856240ab is its upstream's
[2026-11-20T22:59:13Z] R copied f757f3e44ecf7debce87fbbb37950f029a69d6b2a7485286fbed7a2b5dd44046 /root/btc-forensics/tz52-work--live-logs--40-host-before.log
[2026-11-20T22:59:13Z] R copied 05cdf1c9f93247fbd525058804055c32d7c9116b1601aee4ef8af8fdd661337d /root/btc-forensics/tz52-work--live-logs--41-geoblock.log
[2026-11-20T22:59:13Z] R copied 35fe389c167056748ac028ebb3d9112f9ce05f526bb74a7d42c9dcec11297a5a /root/btc-forensics/tz52-work--live-logs--42-sshd.log
[2026-11-20T22:59:13Z] R copied 785a344959e4fd5f1a01a32aec9a723378ac5624e834897998a2f799b82e3e64 /root/btc-forensics/tz52-work--live-logs--50-selftest.log
[2026-11-20T22:59:13Z] R copied 4cf071773dc86ff395cb26c532d989f59894537d02736f9621a92f7ec4ab9337 /root/btc-forensics/tz52-work--live-logs--53-env.log
[2026-11-20T22:59:13Z] R copied 2820b3ef853f28c4be1150607535d457b6f63741f6066319307a8f8a61a3bcce /root/btc-forensics/tz52-work--live-logs--54-sdk-selftest.log
[2026-11-20T22:59:13Z] R copied f73f042c086666ac34a057cdfbdd9101bee5afbd2c5093395126f54ff3660b42 /root/btc-forensics/tz52-work--live-logs--56-key.log
[2026-11-20T22:59:13Z] R copied 986d9a42e54ce48c1bfd998058d6fdedca50edf5e02f2d8141d54b878d53dda1 /root/btc-forensics/tz52-work--live-logs--71-ready.log
[2026-11-20T22:59:13Z] R copied 06be1dbb53f9f186cfe93969b5ee1729a3f732a6b6840643597e68671c240701 /root/btc-forensics/tz52-work--live-logs--72-tg-probe.log
[2026-11-20T22:59:13Z] R copied 846506b8031a63bf5839e40e822030ca87a250de0c8edecd3a658d4f68230140 /root/btc-forensics/tz52-work--live-logs--73-find-chat.log
[2026-11-20T22:59:13Z] R copied e48a5861abc02120ed97b8624236ddf2b2987a4a678c0036cd2ae7fb2810c8ce /root/btc-forensics/tz52-work--live-logs--74-geoblock.log
[2026-11-20T22:59:13Z] R copied beafd3e4b56f4ff89d0ba39e52405cec0ec57a10491f48ed8ad0671a5ff6055c /root/btc-forensics/tz52-work--live-logs--75-roundtrip.log
[2026-11-20T22:59:13Z] R copied 9ca4e91359fc0d3e9ab2e39288c07dca484f50ec1bee62a770e8f538a1db7d92 /root/btc-forensics/tz52-work--live-logs--76-record.log
[2026-11-20T22:59:13Z] R copied b75d7931de34d73d74a073aecef8fe34b33d4248b753db2ed00d6b9575d53cd2 /root/btc-forensics/tz52-work--live-logs--78-sshd-after.log
[2026-11-20T22:59:13Z] R copied 8125f7e7bd00285f4476d1d979c79ccc1f2de334da4084bea0b3848a8e51177b /root/btc-forensics/tz52-work--live-logs--79-host-after.log
[2026-11-20T22:59:13Z] R copied 4c172e1d0a05c4aecd1a23c2132bc9a98b3c5ac87c3a46c2ad7bc71fc0d8a3d6 /root/btc-forensics/tz52-work--live-logs--81-keep.log
[2026-11-20T22:59:13Z] R copied accd4e03fc0135de1942f2fcf801d778cb09791fc7738e189c87247d42871be3 /root/btc-forensics/tz52-work--logs--00-ready.log
[2026-11-20T22:59:13Z] R copied 73acab2d723b3c4c49725e84cab672067423a07dfa2a263fcc5453ee8e40eb1c /root/btc-forensics/tz52-work--logs--01-stage.log
[2026-11-20T22:59:13Z] R copied 9ffc82f62241538a13bacf8e34e86f7caa0c7f19e50bf9755ecc492cb946681c /root/btc-forensics/tz52-work--logs--02-fingerprint.log
[2026-11-20T22:59:13Z] R copied ec3c1bd84cde80b2c323e40088bc26810cd5755b099a8efbad92f02e9f1b3e52 /root/btc-forensics/tz52-work--logs--03-host-gate.log
[2026-11-20T22:59:13Z] R copied f654a15cd9263bebcc6c82df69953e602b1ce23676e319af64dfb56c3ed2a630 /root/btc-forensics/tz52-work--logs--04-room.log
[2026-11-20T22:59:13Z] R copied 8652c2967622a607e778ce470bc53723d9df8f7f6f206e990ff447c44d01ce5b /root/btc-forensics/tz52-work--logs--05-number.log
[2026-11-20T22:59:13Z] R copied 622322b7fe9a0610fa2af7bcafedd3702c252749be79518e34654ca5fc0d958e /root/btc-forensics/tz52-work--logs--05-refs.log
[2026-11-20T22:59:13Z] R copied c58f49e7712712ec58d7d0a4e91e90c467e8469b1fd5c9c402b44e74e6537fde /root/btc-forensics/tz52-work--logs--06-access.log
[2026-11-20T22:59:13Z] R copied c5a3a800943dcceff903392c029198bd87d8aa282999c728d0470273030f3c31 /root/btc-forensics/tz52-work--logs--07-copy.log
[2026-11-20T22:59:13Z] R copied 9ca3723599ac8009fa7e7e93921e93a13f59dc138ed25c5f5f5a105c32b01b1d /root/btc-forensics/tz52-work--logs--08-methods.log
[2026-11-20T22:59:13Z] R copied 14e60547e8b0be945fa89afc717c4ee549671bca4da9e2f39fbc92030c7e3ba6 /root/btc-forensics/tz52-work--logs--10-number.log
[2026-11-20T22:59:13Z] R copied 7bcc891603174efe4cdd25478bdb456e5bcd8e38413e03824426341283764037 /root/btc-forensics/tz52-work--logs--11-worktree.log
[2026-11-20T22:59:13Z] R copied f76345680a2c891b9dcccab01c44fb11b6d551e79a50135d8127f0a680a247aa /root/btc-forensics/tz52-work--logs--12-fingerprint.log
[2026-11-20T22:59:13Z] R copied 283e0ed6384fb10b4cf62f880e1d67e2d0cfd8538ac3f2902126df8c28990932 /root/btc-forensics/tz52-work--logs--13-push.log
[2026-11-20T22:59:13Z] R copied fac01948a97e6ae08b7e018428f92150023156df00f8d1aee32b2967b1e6682a /root/btc-forensics/tz52-work--logs--14-pr.log
[2026-11-20T22:59:13Z] R copied df9f232973df8e7b12b7b9487adafd046f5c41f2ab42f35a55f62c5256f85e0f /root/btc-forensics/tz52-work--logs--15-pr49.log
[2026-11-20T22:59:13Z] R copied c2920b7a9c432d0754c341550f70aee3297ae4afe1401a394ae9a5ba90858bb0 /root/btc-forensics/tz52-work--logs--20-selftest.log
[2026-11-20T22:59:13Z] R copied 6431a8b85133dfeac43bb788c23410b1ba0bb2ae1d46853924283947c04de08d /root/btc-forensics/tz52-work--logs--30-scratch.log
[2026-11-20T22:59:13Z] R copied f1a50862d4053c51899f4a8d814b4d4a7ba0b04fda1126dbed5ac339b587ae08 /root/btc-forensics/tz52-work--logs--32-reclaim-scratch.log
[2026-11-20T22:59:13Z] R copied 4c3a02c43bf721f963f8c19cafe662b7cc6d7b758241f67b94880d5d23c46bcb /root/btc-forensics/tz52-work--logs--80-live-copy.log
[2026-11-20T22:59:13Z] R copied 51089762d0e3abcf81b22b0c9c2172585e6325024cb87590b84ed26512192467 /root/btc-forensics/tz52-work--logs--88-methods-after.log
[2026-11-20T22:59:13Z] R copied bccc42b5e439aadc38a1e19a4457e4f8cc21491e62142ced2c7a2e7afc04e392 /root/btc-forensics/tz52-work--logs--90-closing.log
[2026-11-20T22:59:13Z] R copied e1e7ecf1a888be040528bca826c2a0a7363ea5b92c7fd2ba4181f946b605ddb1 /root/btc-forensics/tz52-work--logs--99-selfcheck.log
[2026-11-20T22:59:13Z] R copied a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366 /root/btc-forensics/tz52-work--stage--research--tz52-l1-account.py
[2026-11-20T22:59:13Z] RECLAIM PASS: 40 files considered, 40 copied, 0 already held; the forensic store 2704 -> 2744 files
[2026-11-20T22:59:13Z] peak memory of this run: 35139584 bytes
[2026-11-20T22:59:13Z] refused by the hook: 0; lookups 0, requests 0
reclaim exit=0
$ cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz52-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz52-work; echo "exit=$?"
exit=0
$ test -e /root/tz52-work; echo "exit=$?"
exit=1
$ test -e /tmp/tmux-0/btc-l1; echo "tmux socket exit=$?"
tmux socket exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       0a73d30 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
2744
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10439651328
```

`RECLAIM PASS` came before the removals. `/root/tz52-work` is gone on both hosts (`exit=1` each), and the worktrees
are the primary checkout and `/root/btc-recorder-svc`, map §3's two. The 40 hashes `reclaim` printed are the ones in
§2.8, each re-read from its forensic copy after the reclaim: 40 of 40 equal.

### 2.8 The files of this run

Every log of both hosts, and the stage's instrument, as `reclaim` copied them into the forensic store as
`/root/btc-forensics/tz52-work--<path with / as -->` (§2.7):

| file under `/root/tz52-work/` | lines | bytes | SHA-256 |
|---|---|---|---|
| `logs/00-ready.log` | 2 | 171 | `accd4e03fc0135de1942f2fcf801d778cb09791fc7738e189c87247d42871be3` |
| `logs/01-stage.log` | 1 | 135 | `73acab2d723b3c4c49725e84cab672067423a07dfa2a263fcc5453ee8e40eb1c` |
| `logs/02-fingerprint.log` | 78 | 13023 | `9ffc82f62241538a13bacf8e34e86f7caa0c7f19e50bf9755ecc492cb946681c` |
| `logs/03-host-gate.log` | 80 | 2521 | `ec3c1bd84cde80b2c323e40088bc26810cd5755b099a8efbad92f02e9f1b3e52` |
| `logs/04-room.log` | 8 | 651 | `f654a15cd9263bebcc6c82df69953e602b1ce23676e319af64dfb56c3ed2a630` |
| `logs/05-number.log` | 6 | 402 | `8652c2967622a607e778ce470bc53723d9df8f7f6f206e990ff447c44d01ce5b` |
| `logs/05-refs.log` | 20 | 1331 | `622322b7fe9a0610fa2af7bcafedd3702c252749be79518e34654ca5fc0d958e` |
| `logs/06-access.log` | 14 | 408 | `c58f49e7712712ec58d7d0a4e91e90c467e8469b1fd5c9c402b44e74e6537fde` |
| `logs/07-copy.log` | 5 | 199 | `c5a3a800943dcceff903392c029198bd87d8aa282999c728d0470273030f3c31` |
| `logs/08-methods.log` | 6 | 363 | `9ca3723599ac8009fa7e7e93921e93a13f59dc138ed25c5f5f5a105c32b01b1d` |
| `logs/10-number.log` | 7 | 415 | `14e60547e8b0be945fa89afc717c4ee549671bca4da9e2f39fbc92030c7e3ba6` |
| `logs/11-worktree.log` | 7 | 344 | `7bcc891603174efe4cdd25478bdb456e5bcd8e38413e03824426341283764037` |
| `logs/12-fingerprint.log` | 78 | 13023 | `f76345680a2c891b9dcccab01c44fb11b6d551e79a50135d8127f0a680a247aa` |
| `logs/13-push.log` | 33 | 1933 | `283e0ed6384fb10b4cf62f880e1d67e2d0cfd8538ac3f2902126df8c28990932` |
| `logs/14-pr.log` | 3 | 94 | `fac01948a97e6ae08b7e018428f92150023156df00f8d1aee32b2967b1e6682a` |
| `logs/15-pr49.log` | 5 | 235 | `df9f232973df8e7b12b7b9487adafd046f5c41f2ab42f35a55f62c5256f85e0f` |
| `logs/20-selftest.log` | 206 | 19535 | `c2920b7a9c432d0754c341550f70aee3297ae4afe1401a394ae9a5ba90858bb0` |
| `logs/30-scratch.log` | 21 | 2023 | `6431a8b85133dfeac43bb788c23410b1ba0bb2ae1d46853924283947c04de08d` |
| `logs/32-reclaim-scratch.log` | 24 | 1409 | `f1a50862d4053c51899f4a8d814b4d4a7ba0b04fda1126dbed5ac339b587ae08` |
| `logs/80-live-copy.log` | 24 | 1075 | `4c3a02c43bf721f963f8c19cafe662b7cc6d7b758241f67b94880d5d23c46bcb` |
| `logs/88-methods-after.log` | 6 | 364 | `51089762d0e3abcf81b22b0c9c2172585e6325024cb87590b84ed26512192467` |
| `logs/90-closing.log` | 77 | 2519 | `bccc42b5e439aadc38a1e19a4457e4f8cc21491e62142ced2c7a2e7afc04e392` |
| `logs/99-selfcheck.log` | 4 | 96 | `e1e7ecf1a888be040528bca826c2a0a7363ea5b92c7fd2ba4181f946b605ddb1` |
| `live-logs/40-host-before.log` | 26 | 2184 | `f757f3e44ecf7debce87fbbb37950f029a69d6b2a7485286fbed7a2b5dd44046` |
| `live-logs/41-geoblock.log` | 8 | 576 | `05cdf1c9f93247fbd525058804055c32d7c9116b1601aee4ef8af8fdd661337d` |
| `live-logs/42-sshd.log` | 10 | 533 | `35fe389c167056748ac028ebb3d9112f9ce05f526bb74a7d42c9dcec11297a5a` |
| `live-logs/50-selftest.log` | 206 | 19535 | `785a344959e4fd5f1a01a32aec9a723378ac5624e834897998a2f799b82e3e64` |
| `live-logs/53-env.log` | 9 | 813 | `4cf071773dc86ff395cb26c532d989f59894537d02736f9621a92f7ec4ab9337` |
| `live-logs/54-sdk-selftest.log` | 116 | 13600 | `2820b3ef853f28c4be1150607535d457b6f63741f6066319307a8f8a61a3bcce` |
| `live-logs/56-key.log` | 7 | 422 | `f73f042c086666ac34a057cdfbdd9101bee5afbd2c5093395126f54ff3660b42` |
| `live-logs/71-ready.log` | 15 | 1114 | `986d9a42e54ce48c1bfd998058d6fdedca50edf5e02f2d8141d54b878d53dda1` |
| `live-logs/72-tg-probe.log` | 5 | 315 | `06be1dbb53f9f186cfe93969b5ee1729a3f732a6b6840643597e68671c240701` |
| `live-logs/73-find-chat.log` | 6 | 392 | `846506b8031a63bf5839e40e822030ca87a250de0c8edecd3a658d4f68230140` |
| `live-logs/74-geoblock.log` | 8 | 576 | `e48a5861abc02120ed97b8624236ddf2b2987a4a678c0036cd2ae7fb2810c8ce` |
| `live-logs/75-roundtrip.log` | 55 | 3296 | `beafd3e4b56f4ff89d0ba39e52405cec0ec57a10491f48ed8ad0671a5ff6055c` |
| `live-logs/76-record.log` | 7 | 326 | `9ca4e91359fc0d3e9ab2e39288c07dca484f50ec1bee62a770e8f538a1db7d92` |
| `live-logs/78-sshd-after.log` | 10 | 533 | `b75d7931de34d73d74a073aecef8fe34b33d4248b753db2ed00d6b9575d53cd2` |
| `live-logs/79-host-after.log` | 26 | 2206 | `8125f7e7bd00285f4476d1d979c79ccc1f2de334da4084bea0b3848a8e51177b` |
| `live-logs/81-keep.log` | 19 | 775 | `4c172e1d0a05c4aecd1a23c2132bc9a98b3c5ac87c3a46c2ad7bc71fc0d8a3d6` |
| `stage/research/tz52-l1-account.py` | 3326 | 188720 | `a425e67cce7178e425b04f899ad245cf31a38848bd2553dfacdbbbcdf3a73366` |

### 2.9 Every mode's peak — V19

Every peak each log printed, against its model (TZ-51 §0.4): the standard library's under `43,213,417` bytes, the
client's (`env`, `sdk-selftest`, `key`, `ready`, `roundtrip`) under `137,458,839`. Each holds. Recorded. The floors
were asserted at each mode's start, and every read of them is in the logs above.

| host | log | runs | peaks, bytes | under |
|---|---|---|---|---|
| capture | `02-fingerprint.log` | 1 | 35,663,872 | `43,213,417` |
| capture | `04-room.log` | 1 | 34,762,752 | `43,213,417` |
| capture | `05-number.log` | 1 | 34,631,680 | `43,213,417` |
| capture | `05-refs.log` | 1 | 34,762,752 | `43,213,417` |
| capture | `08-methods.log` | 1 | 34,750,464 | `43,213,417` |
| capture | `10-number.log` | 1 | 34,746,368 | `43,213,417` |
| capture | `12-fingerprint.log` | 1 | 35,680,256 | `43,213,417` |
| capture | `13-push.log` | 1 | 34,762,752 | `43,213,417` |
| capture | `20-selftest.log` | 1 | 35,794,944 | `43,213,417` |
| capture | `30-scratch.log` | 1 | 35,016,704 | `43,213,417` |
| capture | `32-reclaim-scratch.log` | 1 | 35,147,776 | `43,213,417` |
| capture | `88-methods-after.log` | 1 | 34,484,224 | `43,213,417` |
| live | `40-host-before.log` | 1 | 35,201,024 | `43,213,417` |
| live | `41-geoblock.log` | 1 | 37,691,392 | `43,213,417` |
| live | `42-sshd.log` | 1 | 35,069,952 | `43,213,417` |
| live | `50-selftest.log` | 1 | 35,983,360 | `43,213,417` |
| live | `53-env.log` | 1 | 76,623,872 | `137,458,839` |
| live | `54-sdk-selftest.log` | 1 | 97,202,176 | `137,458,839` |
| live | `56-key.log` | 1 | 76,750,848 | `137,458,839` |
| live | `71-ready.log` | 1 | 91,697,152 | `137,458,839` |
| live | `72-tg-probe.log` | 1 | 37,556,224 | `43,213,417` |
| live | `73-find-chat.log` | 1 | 37,556,224 | `43,213,417` |
| live | `74-geoblock.log` | 1 | 37,687,296 | `43,213,417` |
| live | `75-roundtrip.log` | 1 | 91,828,224 | `137,458,839` |
| live | `78-sshd-after.log` | 1 | 35,069,952 | `43,213,417` |
| live | `79-host-after.log` | 1 | 35,049,472 | `43,213,417` |

---

## 3. Departures, named

1. **The round trip stopped at an answer of the venue that TZ-52 does not name** (§1). §1.2 fixes the run's course
   for a refused placement. This placement was accepted, and the read of the order after it was answered `null`.
   The run took TZ-51 §3's course for a BLOCK, with §1.2's "the run goes to TZ-51 §3.10 and §9".
2. **The Boss was asked for `/start` before `find-chat` ended.** TZ-52 §3 step 11 says to tell him once where
   `find-chat` *ends* with no chat, then run it once more. Its first read, at 22:50:36, found no pending update at
   all: the `/start` the header asks for before `EXECUTE` was not among the bot's updates. At about 22:51 UTC, while
   the same run of `find-chat` still waited, the Executor gave him §3 step 11's ask once, in Russian, in the session,
   rather than spend its `1,800` s first. The words were «В Telegram отправьте /start вашему боту L1 (тому, чей
   токен вводили 20.11). Больше ничего не нужно, отвечать мне не надо.», in place of the TZ's «Отправьте /start
   вашему боту в Telegram». His `/start` reached the bot at 22:56:49, and that run pinned the
   chat. `find-chat` ran once, and the second run §3 step 11 allows was not needed.
3. **§3.9 ran while §3.8's `find-chat` still waited in the background.** G-GEO at 22:50:21 and `roundtrip` at
   22:50:31 came after `find-chat`'s start at 22:49:46 and before its end at 22:56:49. TZ-51 §3.8 runs it in the
   background, and "G-TG decides nothing of the order path". Of §3.9, only `tg-report` reads the chat it pins.
4. **`tg-report` was not run**, so G-TG's third check was not read. Its message is built from the last round trip's
   record, and `mode_tg_report` asserts that a record exists (line 1721). No record was written (§1).
5. **No request was made to the venue after the round trip.** `ready` is a mode of TZ-52 §1.3. Run again, it would
   have read the key's and the wallet's open orders and the wallet's pUSD after the order. It was not run: TZ-52 §1.2
   says "no other request to the venue and no other attempt" after a failed round trip, and the header says "no
   probe". So G-RT's checks (4) to (9) stay unread, and with them whether any part of the order matched before
   `cancel_all`. The venue's answer to `cancel_all`, `canceled` `1`, `not_canceled` `0`, is the one reading of the
   order after its placement. **The round trip was not run again.** TZ-51 §3.9 item 4 forbids it. `mode_roundtrip`'s
   own guard would not have refused it: it reads the `placements` of earlier records, and this failure wrote none.
6. **All of TZ-51 §3.10 was run, without its tmux step**, as TZ-52 §1.2 and §3 step 13 say. TZ-51 §3's rule for a
   BLOCK names only the copy, the tmux step and §9. Item 3's `install` keeps `/var/lib/l1-bot/tz52-l1-account.py`
   beside TZ-51's copy, at §0.1's SHA-256.
7. **Pull request #49's log is named `15-pr49.log`.** Under R, TZ-51's name for it stays `15-pr48.log`. TZ-52 §3
   step 4 reads "pull request #49 in place of #48", and the log is named for the pull request it reads.
8. **The logs' extra lines.**
   - `10-number.log` carries `fetch exit=0`.
   - `11-worktree.log` carries `worktree exit=0` after `git worktree add`, and `exit=0` after §0.1's script.
   - `13-push.log` carries `commit exit=0` and `push exit=0`.
   - `15-pr49.log` opens with a `date -u` line.

   `01-stage.log` holds the script's own line alone: its exit, `0`, was printed to the session only. §0.1's script
   ran from a copy of TZ-52's lines 41 to 169, extracted into the session's scratchpad and asserted equal to them by
   `diff` before it ran. For the worktree, the copy's first line named `/root/tz52-work/wt` in place of the stage.
9. **The refs differ from map §1's read of 2026-11-21** (199 lines), which is recorded and not BLOCKING (TZ-51 §0.5).
   This run read 200 lines, at §0.5 and at §3.1:
   - `HEAD` and `main` read `0a73d30`, the Boss's upload, against `b941123`;
   - `refs/tags/rewardbook-streams-*` read 59, against 58: one more run of the reward book's archive,
     `rewardbook-streams-1795213820`;
   - `refs/pull/49/merge` was still present at both reads, which came before #49 was closed.
10. **Two session directories that map §3 names live were reclaimed as earlier**, as the rule decides (map §7
    item 95): `95cf58d2-…` and `ccca2df8-…`, born at 10:28:56 and 10:28:57 UTC on 2026-11-15. The remote-control
    `claude` processes they were born with are no longer running. Those running now, pids `2569924` and `2569934`,
    started at 18:51:37 and 18:51:39 UTC on 2026-11-20 (`30-scratch.log`). The other four directories reclaimed were:
    - `08f6d3e8-…`, TZ-51's;
    - `3aceaaa9-…`, TZ-50's;
    - `1bc20379-…` and `fd493377-…`, born beside them at 17:49:13 and 06:18:24.

    Five live directories were left untouched:
    - `0736470b-…` and `6f0f41a7-…`, of the remote-control processes;
    - `450e33c9-…` and `dc25b96c-…`, of a session process started at 18:55:31;
    - `5b734feb-…`, of this session's process.

    The classifier refused nothing, `reclaim` and the six `rm -rf` included.
11. **The session's scratchpad** holds §0.1's script's copy (item 8) and this report's generator, which embeds
    every quoted log whole from its file. Nothing else was written there.
12. **What stays on the live host as this TZ left it**, none of it removed by this run (TZ-51 §3):
    - `/root/l1-env/`;
    - `/etc/l1-bot/` with `session-key` (authorized for the wallet since TZ-51), `relayer-key`, `telegram-token` and
      `chat-id` (pinned by this run);
    - `/var/lib/l1-bot/` with `account.json` and the two kept instruments.

    **The session key stands authorized**, and both allowances stand at the maximum: TZ-52 §1.1 kept them. The
    wallet held `11.100000` pUSD before the order. No process uses the key. The stops are the Boss's, as TZ-52 §4
    says: withdraw on polymarket.com, and B-REVOKE, TZ-51 §4.11's line, word for word, with TZ-51's kept copy. Neither
    was run, and no FAIL of this TZ calls for either.
13. **Pull request #50 stays open.** Its one file is the instrument whose `roundtrip_flow` does not handle the
    venue's `null` (§1). Merging or closing it is for the Architect's verdict.
14. **Every block was run by the Executor, and the classifier refused none:** B-RECLAIM-SCRATCH, B-RECLAIM-LIVE and
    B-RECLAIM-OWN. B-ENV, B-PAGES, B-ACCOUNT, B-OWNER, B-RESET and B-PR48 are not steps of this TZ, or had nothing to
    do. No paste was handed to the Boss.
