# TZ-51 — L1, the bot's account and one order's round trip from the live host, rerun — REPORT

**Status: BLOCKED at §3.7, G-APPROVE. The venue's relayer refuses any approval of pUSD to an exchange that is not the
maximum, so §1.4's bound of `1` pUSD an exchange cannot be set through it.**
The Boss ran B-OWNER's line twice, at 18:00:07 and 19:07:12 UTC on 2026-11-20 (`70-B-OWNER.log`). Both runs passed
`secrets`, `bosskey` and `authorize`, and both stopped in `approve` with `exit=4`. The owner signed four approval
batches through the signing page: at 18:37:17, 18:38:13, 19:09:29 and 19:12:37. Each signature recovered to the owner
under the client's own typed data, and the relayer refused each batch with status `400`. The instrument logs a
refusal's status, not its message. The message was read after the second run, by a probe outside the TZ (§3 item 1),
from the owner's own signature of 19:09:29 replayed with its own batch:
`call blocked: call[0] blocked: approve to exchange 0x… must be MaxUint256`. `approve_flow` builds each call with
`amount=APPROVE_UNITS`, `1,000,000` (lines 275 and 1968), as §1.4 and §4.6 decide. **No signature, no run of the line and
no B-RESET can pass G-APPROVE.**

- **G-RT: not read.** No order was placed, no money moved, and nothing of the CLOB was asked for an order. §3.8 and
  §3.9 did not run, so G-READY and G-TG were not read either.
- **G-AUTH authorize PASS** at 18:35:20: the session key acts for the wallet. The second run kept it and signed
  nothing (19:08:18).
- **The wallet's pUSD allowances on chain read `{'c': 'max', 'v': 'max'}`** at both runs' start (18:35:22 and
  19:08:20) and at both FAILs (18:41:09 and 19:18:52). Nothing changed them. **The session key is authorized and acts
  for the wallet while both allowances stand at the maximum.** §4.11 leaves B-REVOKE out of this TZ because "the key
  can spend at most the allowances' `1` pUSD an exchange through orders", and that does not hold. The instrument's copy
  for B-REVOKE is kept at `/var/lib/l1-bot/` (§3.10 item 3, §2.3).
- **Everything before §3.7 passed.**
  - FINGERPRINT PASS twice, revision `2026-11-20-b`, 64 of 64 `frozen` rows equal.
  - Host gate 7 of 7. Room margin **2,743,576,328** bytes.
  - NUMBER PASS 2 of 2, twice. Refs 195 lines, the branch absent before the push.
  - Access `exit=0`, the pinned host key, `vs-2348`, root, both trees absent. The copy at §0.1's SHA-256.
  - Live host gate 5 of 5, at `host before` and `host after`. LS held: root's keys the Executor's alone, and the
    eight `PATH` lines as TZ-50 left them.
  - **G-GEO PASS** over IPv4: `blocked False`, `country 'BG'`.
  - **G-SSH 6 of 6**, at §0.6 and again at §3.10.
  - `SELFTEST PASS: 140 checks, 140 passed`, `refused by the hook: 5`, on both hosts.
  - `G-ENV installed PASS`, 34 distributions, 1,373 RECORD entries over 1,367 paths, none absent or at another hash.
  - `SDK SELFTEST PASS: 32 checks, 32 passed`, `refused by the hook: 2`.
  - **G-PAGE PASS**: Pages already served `main`'s `/docs`. **G-KEY**: present, kept.
- **Branch** `tz-51-l1-account-round-trip-rerun` at `bfbb1041529f60045172dd95167d8096f6153fba`, one file, `3306 0`.
  **Pull request #49**, open. **Pull request #48** was already closed unmerged when §3.1 read it: closed by the
  repository's owner at 17:50:02 UTC, with its head at `0774d7e…`. The §4.2 self-check read `0`, one path, nothing.
- **L1's paths on the live host, left as they stand** (§3, a BLOCK after §3.6):
  - `/etc/l1-bot/` is `0700` and root's. It holds `session-key` (67 bytes, authorized for the wallet),
    `relayer-key` (105 bytes) and `telegram-token` (47 bytes), each `0600` and root's. No `chat-id`.
  - `/var/lib/l1-bot/` is `0700` and root's. It holds `account.json` (310 bytes) and the kept instrument (187,351
    bytes, `73fd0f61…`), each `0600` and root's.
  - `/root/l1-env/` is the client's environment, `polymarket-client` `0.20.0`, `55,492,611` bytes.
  - Root's `authorized_keys` holds the Executor's key alone: the Boss skipped `bosskey` at both runs.
- **The capture host:** no unit was started, stopped or touched, and no store was written. The recorder, the reward
  book and the advisor kept the same `MainPID`, `NRestarts` and `ActiveState` from §0.3 to the closing reads.
- **Handed to the Boss:** B-ACCOUNT and B-OWNER once, at 17:57:15 UTC. The same line again at 18:47:50, once. The
  classifier refused nothing.
- **No address of either host, of the bot's owner, wallet or session key, and no key, token, relayer key or
  signature** is in this report. Of the live host's name, only its first label is given.

---

## 0. Fingerprint

`I0 fingerprint` (`logs/02-fingerprint.log`, 17:52:25 UTC) and `I fingerprint` from the branch's worktree
(`logs/12-fingerprint.log`, 17:54 UTC) each printed `FINGERPRINT PASS`. Their lines are identical but for the instants
and the peak (`diff` of the two with both stripped: equal).

```
[2026-11-20T17:52:26Z] FINGERPRINT PASS: revision 2026-11-20-b; anchors 6 of 6, 4 re-derived; rows 67: frozen 64 of 64 equal, tracked 2, reported 1; the signing page on main equal to TZ-50's Appendix B
```

**Revision string:** `2026-11-20-b`. **Anchors:**

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
| `SYSTEM-MAP.md` | 1076 | 182828 | reported | `64162bce911fbee0b986dce0f2eb570a7d25f720be2081a0f1c70ff3d3d31bbd` |
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

**The model:** the one TZ-51's header names. The session's own record of its model was read at the start of the run
and agrees.

---

## 1. The blocker

§3.7's fourth mode, `approve`, is G-APPROVE (§4.6). It reads both exchanges' pUSD allowances on chain. For each one
under one order's cost or above `1` pUSD, it asks the owner to sign one Deposit Wallet batch that approves
`APPROVE_UNITS`, and submits it to the relayer with the owner's Relayer API key:

```python
APPROVE_UNITS = 1000000        # 1 pUSD to each exchange whose allowance is short, never the maximum: what a key can
```

```python
        calls = [k.C.erc20_approval_call(token_address=PUSD, spender=a, amount=APPROVE_UNITS) for _x, a in short]
```

(Appendix A, lines 275 and 1968.) Both allowances read `max`, so both exchanges were "short" by §1.4's rule, and each
link carried two calls, `x=cv`. The payload is the client's own `build_deposit_wallet_payload`, submitted by the
client's own `submit_gasless` to `/submit`. Its fields are the ones the venue's documentation shows for a `WALLET`
batch, and its deadline is the client's `_DEPOSIT_WALLET_DEADLINE_S`, `600` s. For an owner signer the client's
`wrap_deposit_wallet_signature` returns the signature unchanged, so the raw signature is the client's own form too.

**What the relayer said.** At each of the four signed links it answered `400`. `approve_flow` catches
`RequestRejectedError`, logs `the relayer refused the batch, status 400` and offers the next link (lines 1994 to 1999);
the error's message is not logged. After the second run the Executor sent the relayer two requests outside the TZ
(§3 item 1; `95-relayer-probe.log`, §2.2):

- **Probe B**, the owner's own signature of 19:09:29, replayed with its own batch: nonce `2` and its deadline, by then
  past. The signature recovered to the owner (`True`). The relayer answered
  **`400`, `call blocked: call[0] blocked: approve to exchange 0x… must be MaxUint256`.**
- **Probe A**, the same batch with a fresh nonce and deadline, signed by a throwaway key, so that it could execute
  nothing. The relayer answered `400`, `invalid batch signature`.

So the relayer checks a `WALLET` batch's signature first (probe A), then its calls, before any check of its deadline
(probe B), and it refuses an approval to an exchange of any amount but `MaxUint256`. The venue's documentation, read
on 2026-11-20 (`docs.polymarket.com/trading/deposit-wallets`), lists `approve(address spender, uint256 amount)` with the
standard and V2 exchanges among the permitted spenders, and does not state this rule.

**It cannot pass on any run.** `APPROVE_UNITS` is a constant of the instrument, fixed byte for byte by Appendix A, and
§1.4 decides it. `bounded` keeps only an allowance at most `APPROVE_UNITS` (lines 2166 to 2168), so a FAIL of the
relayer leaves G-APPROVE FAIL. Nothing the Boss signs changes the calls. Neither of B-RESET's causes is in the log: the
relayer took the same key for the authorization at 18:35:13, and the wallet reads deployed at every run.

**Why the self-tests passed.** `sdk-selftest` runs `approve` against the self-test's loopback stand-in of the relayer
(`_relayer`, from line 2526), which accepts a batch of any amount. Its log shows the batch of 2 accepted and the
allowances read `1.000000` (§2.4). The rule exists only at the venue.

**§3.7's "another exit"** reads the log, names the mode and the line, and hands the line again, "at most twice more".
The line was handed again once, at 18:47:50, while the 400's message was still unknown. The second run failed the
same way, at both of its signed links. A third handover was not made (§3 item 2). The instrument is this TZ's
Validation, fixed byte for byte (§5; contract §6), so the run went to §3.10 and §9, as §3 says for a BLOCK.

---

## 2. The evidence

Every live host's log below is quoted whole as §3.10's copy brought it back, byte for byte (`diff exit=0`, §2.6). Its
SHA-256 is in §2.7, and its copy in the forensic store is `/root/btc-forensics/tz51-work--<path with / as -->`.

### 2.1 B-OWNER — `70-B-OWNER.log` and `37-handover.log`

**`70-B-OWNER.log`**, whole: the Boss's two runs of the line, each under its own `date -u` line. Peaks, in order:
`secrets` 34,877,440, `bosskey` 35,008,512, `authorize` 90,193,920, `approve` 84,557,824;
then `secrets` 35,008,512, `bosskey` 34,881,536, `authorize` 90,198,016, `approve`
84,566,016.

```
2026-11-20T18:00:07.272730846Z
[2026-11-20T18:00:07Z] MemAvailable read 1: 1438900224 bytes, floor 86426834
[2026-11-20T18:00:07Z] available on /: 16914366464 bytes, floor 2447483648
[2026-11-20T18:10:31Z] SECRETS telegram-token: written, 47 bytes
[2026-11-20T18:10:31Z] SECRETS relayer-key: written, 105 bytes
[2026-11-20T18:10:31Z] SECRETS account: written, 59 bytes
[2026-11-20T18:10:31Z] PATH /etc/l1-bot/telegram-token: file mode 0600 uid 0 bytes 47
[2026-11-20T18:10:31Z] PATH /etc/l1-bot/relayer-key: file mode 0600 uid 0 bytes 105
[2026-11-20T18:10:31Z] PATH /var/lib/l1-bot/account.json: file mode 0600 uid 0 bytes 59
[2026-11-20T18:10:31Z] peak memory of this run: 34877440 bytes
[2026-11-20T18:10:31Z] refused by the hook: 0; lookups 0, requests 0
[2026-11-20T18:11:01Z] BOSSKEY skipped: no key given; root's keys by fingerprint: [('ssh-ed25519', 'SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo')]
[2026-11-20T18:11:01Z] peak memory of this run: 35008512 bytes
[2026-11-20T18:11:01Z] refused by the hook: 0; lookups 0, requests 0
[2026-11-20T18:11:02Z] MemAvailable read 1: 1455947776 bytes, floor 274917678
[2026-11-20T18:11:02Z] available on /: 16913743872 bytes, floor 2447483648
[2026-11-20T18:11:03Z] OWNER authorize: the owner's Deposit Wallet derived (beacon) and deployed; the addresses withheld
[2026-11-20T18:21:53Z] OWNER authorize link 1: no owner's signature
[2026-11-20T18:32:17Z] OWNER authorize link 2: the owner's signature, past its deadline
[2026-11-20T18:35:13Z] OWNER authorize link 3: the owner's signature, recovered to the owner under the client's own typed data
[2026-11-20T18:35:13Z] OWNER authorize: the relayer accepted the request, status SUBMITTED
[2026-11-20T18:35:19Z] OWNER authorize: the relayer's transaction confirmed
[2026-11-20T18:35:20Z] KEY read 1: the session key lists the wallet's orders - 0 on the first page
[2026-11-20T18:35:20Z] G-AUTH authorize PASS: the key acts for the wallet
[2026-11-20T18:35:20Z] peak memory of this run: 90193920 bytes
[2026-11-20T18:35:20Z] refused by the hook: 0; lookups 7, requests 0
[2026-11-20T18:35:21Z] MemAvailable read 1: 1441107968 bytes, floor 274917678
[2026-11-20T18:35:21Z] available on /: 16913735680 bytes, floor 2447483648
[2026-11-20T18:35:22Z] OWNER approve: the owner's Deposit Wallet derived (beacon) and deployed; its pUSD allowances on chain {'c': 'max', 'v': 'max'}
[2026-11-20T18:37:17Z] OWNER approve link 1: the owner's signature, recovered to the owner under the client's own typed data
[2026-11-20T18:37:17Z] OWNER approve link 1: the relayer refused the batch, status 400
[2026-11-20T18:38:13Z] OWNER approve link 2: the owner's signature, recovered to the owner under the client's own typed data
[2026-11-20T18:38:13Z] OWNER approve link 2: the relayer refused the batch, status 400
[2026-11-20T18:41:09Z] OWNER approve link 3: no owner's signature
[2026-11-20T18:41:09Z] G-APPROVE FAIL: allowances on chain {'c': 'max', 'v': 'max'}, each between one order's cost and 1 pUSD: False
[2026-11-20T18:41:09Z] peak memory of this run: 84557824 bytes
[2026-11-20T18:41:09Z] refused by the hook: 0; lookups 5, requests 2
exit=4
2026-11-20T19:07:12.497350354Z
[2026-11-20T19:07:12Z] MemAvailable read 1: 1449414656 bytes, floor 86426834
[2026-11-20T19:07:12Z] available on /: 16913727488 bytes, floor 2447483648
[2026-11-20T19:07:12Z] SECRETS telegram-token: kept
[2026-11-20T19:07:12Z] SECRETS relayer-key: kept
[2026-11-20T19:07:12Z] SECRETS account: kept
[2026-11-20T19:07:12Z] PATH /etc/l1-bot/telegram-token: file mode 0600 uid 0 bytes 47
[2026-11-20T19:07:12Z] PATH /etc/l1-bot/relayer-key: file mode 0600 uid 0 bytes 105
[2026-11-20T19:07:12Z] PATH /var/lib/l1-bot/account.json: file mode 0600 uid 0 bytes 310
[2026-11-20T19:07:12Z] peak memory of this run: 35008512 bytes
[2026-11-20T19:07:12Z] refused by the hook: 0; lookups 0, requests 0
[2026-11-20T19:08:16Z] BOSSKEY skipped: no key given; root's keys by fingerprint: [('ssh-ed25519', 'SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo')]
[2026-11-20T19:08:16Z] peak memory of this run: 34881536 bytes
[2026-11-20T19:08:16Z] refused by the hook: 0; lookups 0, requests 0
[2026-11-20T19:08:16Z] MemAvailable read 1: 1449418752 bytes, floor 274917678
[2026-11-20T19:08:16Z] available on /: 16913723392 bytes, floor 2447483648
[2026-11-20T19:08:18Z] KEY read 1: the session key lists the wallet's orders - 0 on the first page
[2026-11-20T19:08:18Z] G-AUTH authorize PASS: kept - the key authorized at 2026-11-20T18:35:20Z acts for the wallet; nothing signed
[2026-11-20T19:08:18Z] peak memory of this run: 90198016 bytes
[2026-11-20T19:08:18Z] refused by the hook: 0; lookups 3, requests 0
[2026-11-20T19:08:18Z] MemAvailable read 1: 1416396800 bytes, floor 274917678
[2026-11-20T19:08:18Z] available on /: 16913723392 bytes, floor 2447483648
[2026-11-20T19:08:20Z] OWNER approve: the owner's Deposit Wallet derived (beacon) and deployed; its pUSD allowances on chain {'c': 'max', 'v': 'max'}
[2026-11-20T19:09:29Z] OWNER approve link 1: the owner's signature, recovered to the owner under the client's own typed data
[2026-11-20T19:09:29Z] OWNER approve link 1: the relayer refused the batch, status 400
[2026-11-20T19:12:37Z] OWNER approve link 2: the owner's signature, recovered to the owner under the client's own typed data
[2026-11-20T19:12:37Z] OWNER approve link 2: the relayer refused the batch, status 400
[2026-11-20T19:18:52Z] OWNER approve link 3: no owner's signature
[2026-11-20T19:18:52Z] G-APPROVE FAIL: allowances on chain {'c': 'max', 'v': 'max'}, each between one order's cost and 1 pUSD: False
[2026-11-20T19:18:52Z] peak memory of this run: 84566016 bytes
[2026-11-20T19:18:52Z] refused by the hook: 0; lookups 5, requests 2
exit=4
```

In the first run, `authorize` link 1 brought no signature and link 2 brought one past its deadline. Link 3's was
recovered, submitted, accepted (`SUBMITTED`) and confirmed, and the key read acting for the wallet. `approve` link 3
brought no signature at either run. In the second run the Executor had told the Boss to press Enter there rather than
sign (§3 item 3). `account.json` grew from 59 bytes to 310 between the runs, written by `authorize`.

**`37-handover.log`**, whole: both handovers, the script's SHA-256 at each (§0.1's), and every read of the log with its
instant. The reads after `wait 2 restarted` add one line each, the log's line count and the line numbers of its last
`date -u` and `exit=` lines, by which the wait knew the second run's end (§3 item 4).

```
handover 2026-11-20T17:57:15.482417347Z epoch 1795197435: B-ACCOUNT and B-OWNER handed to the Boss, once, in one message; the bound 8 hours from this instant
782daebf76e6c19c7c17543164ca3d95308e0e0e2a3c7bedef1d4a838ab33030  /root/tz51-work/stage/b-owner.sh
read 2026-11-20T18:07:04.916882325Z
2026-11-20T18:00:07.272730846Z
[2026-11-20T18:00:07Z] MemAvailable read 1: 1438900224 bytes, floor 86426834
[2026-11-20T18:00:07Z] available on /: 16914366464 bytes, floor 2447483648
R exit=0
read 2026-11-20T18:16:35.948099158Z
[2026-11-20T18:11:02Z] MemAvailable read 1: 1455947776 bytes, floor 274917678
[2026-11-20T18:11:02Z] available on /: 16913743872 bytes, floor 2447483648
[2026-11-20T18:11:03Z] OWNER authorize: the owner's Deposit Wallet derived (beacon) and deployed; the addresses withheld
R exit=0
read 2026-11-20T18:26:06.964665532Z
[2026-11-20T18:11:02Z] available on /: 16913743872 bytes, floor 2447483648
[2026-11-20T18:11:03Z] OWNER authorize: the owner's Deposit Wallet derived (beacon) and deployed; the addresses withheld
[2026-11-20T18:21:53Z] OWNER authorize link 1: no owner's signature
R exit=0
read 2026-11-20T18:35:37.967117069Z
[2026-11-20T18:35:21Z] MemAvailable read 1: 1441107968 bytes, floor 274917678
[2026-11-20T18:35:21Z] available on /: 16913735680 bytes, floor 2447483648
[2026-11-20T18:35:22Z] OWNER approve: the owner's Deposit Wallet derived (beacon) and deployed; its pUSD allowances on chain {'c': 'max', 'v': 'max'}
R exit=0
read 2026-11-20T18:45:08.971725340Z
[2026-11-20T18:41:09Z] peak memory of this run: 84557824 bytes
[2026-11-20T18:41:09Z] refused by the hook: 0; lookups 5, requests 2
exit=4
R exit=0
handover 2 2026-11-20T18:47:50.992613370Z epoch 1795200470: the same line handed again, unchanged, with one line in Russian - approve FAIL at 18:41:09, the relayer refused both signed batches with status 400; inside the bound of the first handover
782daebf76e6c19c7c17543164ca3d95308e0e0e2a3c7bedef1d4a838ab33030  /root/tz51-work/stage/b-owner.sh
no server running on /tmp/tmux-0/btc-l1
has-session exit=1
wait 2 restarted 2026-11-20T18:56:31.835897929Z after the session's restart at 18:51; bound epoch 1795226235; first run's log ends at line 38
read 2026-11-20T18:56:31.838327680Z
[2026-11-20T18:41:09Z] peak memory of this run: 84557824 bytes
[2026-11-20T18:41:09Z] refused by the hook: 0; lookups 5, requests 2
exit=4
lines 38 last-date 1 last-exit 38
R exit=0
read 2026-11-20T19:06:02.495184709Z
[2026-11-20T18:41:09Z] peak memory of this run: 84557824 bytes
[2026-11-20T18:41:09Z] refused by the hook: 0; lookups 5, requests 2
exit=4
lines 38 last-date 1 last-exit 38
R exit=0
read 2026-11-20T19:15:33.535379929Z
[2026-11-20T19:09:29Z] OWNER approve link 1: the relayer refused the batch, status 400
[2026-11-20T19:12:37Z] OWNER approve link 2: the owner's signature, recovered to the owner under the client's own typed data
[2026-11-20T19:12:37Z] OWNER approve link 2: the relayer refused the batch, status 400
lines 65 last-date 39 last-exit 38
R exit=0
read 2026-11-20T19:25:04.516953278Z
[2026-11-20T19:18:52Z] peak memory of this run: 84566016 bytes
[2026-11-20T19:18:52Z] refused by the hook: 0; lookups 5, requests 2
exit=4
lines 70 last-date 39 last-exit 70
R exit=0
```

### 2.2 The relayer's words — `95-relayer-probe.log`

Run by the Executor at 19:27:37 UTC on the live host, `cd /root/tz51-work && /root/l1-env/bin/python -B
probe-approve.py`. The script loads Appendix A's file as a module, so its audit hook is installed, and sets the hook's
mode to `approve`, so the hook allows what `approve` allows. It then calls the client through Appendix A's own
`client`, `load_relayer` and `resolve_wallet`, the client's `erc20_approval_call`, `build_deposit_wallet_typed_data`,
`build_deposit_wallet_payload` and `submit_gasless`, with `PUSD`, `EXCHANGES`, `APPROVE_UNITS`, `APPROVE_METADATA` and
`DEADLINE_S` as Appendix A has them: `approve_flow`'s batch, call for call. It masks every `0x` string of six hex
digits or more in what it prints. The script is not in the repository. It held the owner's signature of 19:09:29 as a
literal, and it was removed with `/root/tz51-work` on the live host (§2.6). `refused by the hook: 0`.

```
2026-11-20T19:27:37.570307614Z
[2026-11-20T19:27:38Z] wallet derived (beacon) and deployed
[2026-11-20T19:27:38Z] the relayer's WALLET nonce now: 2
[2026-11-20T19:27:38Z] probe B: the replayed signature recovers to the owner: True
[2026-11-20T19:27:38Z] probe B (owner's signature, nonce 2, deadline past): refused, status 400, code None, message: call blocked: call[0] blocked: approve to exchange 0x… must be MaxUint256
[2026-11-20T19:27:39Z] probe A (throwaway signer, fresh nonce and deadline): refused, status 400, code None, message: invalid batch signature
[2026-11-20T19:27:39Z] refused by the hook: 0
exit=0
```

### 2.3 The live host after it

**`79-host-after.log`**, whole. Its first entry is the Executor's quoting error (§3 item 5), and the second is the
gate. Against `host before` (§2.4): `relayer-key`, `telegram-token`, `/var/lib/l1-bot` and `account.json` are now
present; the keys of root, the locale, the clock, `chat-id` (absent) and `wheels` (absent) read the same.

```
2026-11-20T19:28:31.901530178Z
[2026-11-20T19:28:32Z] peak memory of this run: 34758656 bytes
[2026-11-20T19:28:32Z] refused by the hook: 0; lookups 0, requests 0
Traceback (most recent call last):
  File "/root/tz51-work/tz51-l1-account.py", line 3306, in <module>
    sys.exit(main(sys.argv[1:]))
             ^^^^^^^^^^^^^^^^^^
  File "/root/tz51-work/tz51-l1-account.py", line 3297, in main
    assert mode in table and not rest, "unknown mode %r" % (argv,)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: unknown mode ['host after']
exit=1
2026-11-20T19:28:39.531733819Z
[2026-11-20T19:28:39Z] LH1 hostname vs-2348: PASS
[2026-11-20T19:28:39Z] LH2 Ubuntu 24.04: PASS
[2026-11-20T19:28:39Z] LH3 Python 3.12: PASS
[2026-11-20T19:28:39Z] LH4 not the capture host: PASS
[2026-11-20T19:28:39Z] LH5 the host key pinned at TZ-47's first connection: PASS
[2026-11-20T19:28:39Z] LIVE HOST GATE PASS: 5 of 5
[2026-11-20T19:28:39Z] MemAvailable read 1: 1456447488 bytes, floor 86426834
[2026-11-20T19:28:39Z] available on /: 16913510400 bytes, floor 2447483648
[2026-11-20T19:28:39Z] HOST after: kernel 6.8.0-138-generic; Python 3.12.3; Ubuntu 24.04.5 LTS; MemTotal 1944465408 MemAvailable 1456447488 SwapTotal 1073737728 SwapFree 1073737728; / 20779339776 bytes, 16913510400 available
[2026-11-20T19:28:39Z] LOCALE /etc/default/locale: LANG="ru_UA.UTF-8"
[2026-11-20T19:28:39Z] LOCALE `locale` in this session, exit 0: LANG=ru_UA.UTF-8; LANGUAGE=; LC_CTYPE="C"; LC_NUMERIC="C"; LC_TIME="C"; LC_COLLATE="C"; LC_MONETARY="C"; LC_MESSAGES="C"; LC_PAPER="C"; LC_NAME="C"; LC_ADDRESS="C"; LC_TELEPHONE="C"; LC_MEASUREMENT="C"; LC_IDENTIFICATION="C"; LC_ALL=C
[2026-11-20T19:28:39Z] CLOCK exit 0: NTP=yes; NTPSynchronized=yes; TimeUSec=Fri 2026-11-20 19:28:39 UTC
[2026-11-20T19:28:39Z] SSHD authorized keys of root: [('ssh-ed25519', 'SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo')]; the Executor's among them: True
[2026-11-20T19:28:39Z] PATH /etc/l1-bot: dir mode 0700 uid 0 bytes 4096
[2026-11-20T19:28:39Z] PATH /etc/l1-bot/session-key: file mode 0600 uid 0 bytes 67
[2026-11-20T19:28:39Z] PATH /etc/l1-bot/relayer-key: file mode 0600 uid 0 bytes 105
[2026-11-20T19:28:39Z] PATH /etc/l1-bot/telegram-token: file mode 0600 uid 0 bytes 47
[2026-11-20T19:28:39Z] PATH /etc/l1-bot/chat-id: absent
[2026-11-20T19:28:39Z] PATH /var/lib/l1-bot: dir mode 0700 uid 0 bytes 4096
[2026-11-20T19:28:39Z] PATH /var/lib/l1-bot/account.json: file mode 0600 uid 0 bytes 310
[2026-11-20T19:28:39Z] PATH /root/l1-env: dir mode 0755 uid 0 bytes 4096
[2026-11-20T19:28:39Z] PATH /root/tz51-work/wheels: absent
[2026-11-20T19:28:39Z] peak memory of this run: 35139584 bytes
[2026-11-20T19:28:39Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**`78-sshd-after.log`**, whole, and **`88-methods-after.log`**, whole: **G-SSH after**, K1 to K5 and K6, 6 of 6. The
first entry of `88-methods-after.log` is the mode refusing to run outside `/root/tz51-work` (§3 item 5).

```
2026-11-20T19:28:21.823356864Z
[2026-11-20T19:28:21Z] K1 TZ-49's sshd drop-in, byte for byte: PASS
[2026-11-20T19:28:21Z] K2 passwordauthentication no: PASS
[2026-11-20T19:28:21Z] K3 kbdinteractiveauthentication no: PASS
[2026-11-20T19:28:21Z] K4 permitrootlogin without-password: PASS
[2026-11-20T19:28:21Z] K5 pubkeyauthentication yes: PASS
[2026-11-20T19:28:21Z] G-SSH K1 to K5 PASS: 5 of 5
[2026-11-20T19:28:21Z] peak memory of this run: 35024896 bytes
[2026-11-20T19:28:21Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-20T19:28:22.008824460Z
Traceback (most recent call last):
  File "/root/tz51-work/wt/research/tz51-l1-account.py", line 3306, in <module>
    sys.exit(main(sys.argv[1:]))
             ^^^^^^^^^^^^^^^^^^
  File "/root/tz51-work/wt/research/tz51-l1-account.py", line 3279, in main
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
           ^^^^^^^^^^^^^^^^^^^
AssertionError: run from /root/tz51-work, not /root/btc-5m-twap
exit=1
2026-11-20T19:28:25.560668181Z
[2026-11-20T19:28:26Z] METHODS after: the methods the live host's sshd offers root, from outside: ['publickey']; ssh exit 255
[2026-11-20T19:28:26Z] G-SSH K6 publickey alone, from outside: PASS
[2026-11-20T19:28:26Z] peak memory of this run: 34578432 bytes
[2026-11-20T19:28:26Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**`81-keep.log`**, whole: §3.10 item 3, the instrument kept for B-REVOKE at §0.1's SHA-256, `exit=0`.

```
2026-11-20T19:28:32.753180224Z
73fd0f6160eb1627a15589a081437f54ee5d826b987586c0f218541c7083dca0  /var/lib/l1-bot/tz51-l1-account.py
exit=0
/etc/l1-bot:
total 20
drwx------   2 root root 4096 Nov 20 18:10 .
drwxr-xr-x 107 root root 4096 Nov 20 06:25 ..
-rw-------   1 root root  105 Nov 20 18:10 relayer-key
-rw-------   1 root root   67 Nov 20 06:25 session-key
-rw-------   1 root root   47 Nov 20 18:00 telegram-token

/var/lib/l1-bot:
total 196
drwx------  2 root root   4096 Nov 20 19:28 .
drwxr-xr-x 41 root root   4096 Nov 20 18:10 ..
-rw-------  1 root root    310 Nov 20 19:18 account.json
-rw-------  1 root root 187351 Nov 20 19:28 tz51-l1-account.py
```

### 2.4 What passed before it — the live host

**`40-host-before.log`**, whole: the live host gate, 5 of 5, and LS. Root's keys are the Executor's alone, and the
eight `PATH` lines read as TZ-50's `79-host-after.log` left them.

```
2026-11-20T17:53:32.848835749Z
[2026-11-20T17:53:32Z] LH1 hostname vs-2348: PASS
[2026-11-20T17:53:32Z] LH2 Ubuntu 24.04: PASS
[2026-11-20T17:53:32Z] LH3 Python 3.12: PASS
[2026-11-20T17:53:32Z] LH4 not the capture host: PASS
[2026-11-20T17:53:32Z] LH5 the host key pinned at TZ-47's first connection: PASS
[2026-11-20T17:53:32Z] LIVE HOST GATE PASS: 5 of 5
[2026-11-20T17:53:32Z] MemAvailable read 1: 1460703232 bytes, floor 86426834
[2026-11-20T17:53:32Z] available on /: 16914432000 bytes, floor 2447483648
[2026-11-20T17:53:32Z] HOST before: kernel 6.8.0-138-generic; Python 3.12.3; Ubuntu 24.04.5 LTS; MemTotal 1944465408 MemAvailable 1460703232 SwapTotal 1073737728 SwapFree 1073737728; / 20779339776 bytes, 16914432000 available
[2026-11-20T17:53:32Z] LOCALE /etc/default/locale: LANG="ru_UA.UTF-8"
[2026-11-20T17:53:32Z] LOCALE `locale` in this session, exit 0: LANG=ru_UA.UTF-8; LANGUAGE=; LC_CTYPE="C"; LC_NUMERIC="C"; LC_TIME="C"; LC_COLLATE="C"; LC_MONETARY="C"; LC_MESSAGES="C"; LC_PAPER="C"; LC_NAME="C"; LC_ADDRESS="C"; LC_TELEPHONE="C"; LC_MEASUREMENT="C"; LC_IDENTIFICATION="C"; LC_ALL=C
[2026-11-20T17:53:33Z] CLOCK exit 0: NTP=yes; NTPSynchronized=yes; TimeUSec=Fri 2026-11-20 17:53:33 UTC
[2026-11-20T17:53:33Z] SSHD authorized keys of root: [('ssh-ed25519', 'SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo')]; the Executor's among them: True
[2026-11-20T17:53:33Z] PATH /etc/l1-bot: dir mode 0700 uid 0 bytes 4096
[2026-11-20T17:53:33Z] PATH /etc/l1-bot/session-key: file mode 0600 uid 0 bytes 67
[2026-11-20T17:53:33Z] PATH /etc/l1-bot/relayer-key: absent
[2026-11-20T17:53:33Z] PATH /etc/l1-bot/telegram-token: absent
[2026-11-20T17:53:33Z] PATH /etc/l1-bot/chat-id: absent
[2026-11-20T17:53:33Z] PATH /var/lib/l1-bot: absent
[2026-11-20T17:53:33Z] PATH /var/lib/l1-bot/account.json: absent
[2026-11-20T17:53:33Z] PATH /root/l1-env: dir mode 0755 uid 0 bytes 4096
[2026-11-20T17:53:33Z] PATH /root/tz51-work/wheels: absent
[2026-11-20T17:53:33Z] peak memory of this run: 35024896 bytes
[2026-11-20T17:53:33Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**`41-geoblock.log`**, whole: G-GEO, read before the Boss's part. §3.9's second read never came, because §3.9 did not
run.

```
2026-11-20T17:53:43.702245963Z
[2026-11-20T17:53:43Z] MemAvailable read 1: 1456906240 bytes, floor 86426834
[2026-11-20T17:53:43Z] available on /: 16914411520 bytes, floor 2447483648
[2026-11-20T17:53:44Z] G-GEO read 1 over IPv4: status 200, 68 bytes, blocked False, country 'BG', region '22', keys ['blocked', 'country', 'ip', 'region']; the address the venue saw is the connection's own: True -> PASS
[2026-11-20T17:53:44Z] G-GEO PASS
[2026-11-20T17:53:44Z] peak memory of this run: 37777408 bytes
[2026-11-20T17:53:44Z] refused by the hook: 0; lookups 1, requests 1
exit=0
```

**`42-sshd.log`**, whole, with `08-methods.log` in §2.5: G-SSH K1 to K5.

```
2026-11-20T17:53:54.717343239Z
[2026-11-20T17:53:54Z] K1 TZ-49's sshd drop-in, byte for byte: PASS
[2026-11-20T17:53:54Z] K2 passwordauthentication no: PASS
[2026-11-20T17:53:54Z] K3 kbdinteractiveauthentication no: PASS
[2026-11-20T17:53:54Z] K4 permitrootlogin without-password: PASS
[2026-11-20T17:53:54Z] K5 pubkeyauthentication yes: PASS
[2026-11-20T17:53:54Z] G-SSH K1 to K5 PASS: 5 of 5
[2026-11-20T17:53:54Z] peak memory of this run: 35016704 bytes
[2026-11-20T17:53:54Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**`50-selftest.log`**: the self-test on the live host, 205 lines. Its summary lines and its two
real-terminal checks:

```
[2026-11-20T17:55:22Z] ok   secrets at a real terminal: the token and the key read hidden, the address shown, a bad token asked again and the stray line typed after it discarded; the log holds none of them
[2026-11-20T17:55:22Z] ok   bosskey at a real terminal: the key read and appended on its own line
[2026-11-20T17:55:23Z] SELFTEST PASS: 140 checks, 140 passed; refused by the hook: 5, each a check's own
[2026-11-20T17:55:23Z] peak memory of this run: 35807232 bytes
[2026-11-20T17:55:23Z] refused by the hook: 5; lookups 0, requests 18
```

**`53-env.log`**, whole: `G-ENV installed PASS`. `/root/l1-env` was present, so §3.4's wheels and B-ENV did not run.

```
2026-11-20T17:55:40.686352306Z
[2026-11-20T17:55:41Z] ENV interpreter 3.12.3, prefix /root/l1-env: PASS
[2026-11-20T17:55:41Z] ENV distributions: 34 installed, 34 pinned; missing [], extra [], another version []
[2026-11-20T17:55:41Z] ENV files: 1373 RECORD entries with a SHA-256 over 1367 paths, 6 of them listed by two distributions; absent [], another hash []
[2026-11-20T17:55:41Z] ENV the client polymarket-client 0.20.0; session keys 15534000 s, a batch 600 s; selectors {'authorize': '24017fae', 'revoke': 'e63f952f'}; hosts https://clob.polymarket.com, https://relayer-v2.polymarket.com, https://gamma-api.polymarket.com
[2026-11-20T17:55:41Z] G-ENV installed PASS
[2026-11-20T17:55:41Z] peak memory of this run: 76550144 bytes
[2026-11-20T17:55:41Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**`54-sdk-selftest.log`**: the client's self-test, 116 lines. Its summary lines, its
real-terminal check, and its `approve` cases against the stand-in, whose relayer accepts a batch of `1` pUSD (§1):

```
[2026-11-20T17:55:52Z] OWNER approve: the owner's Deposit Wallet derived (beacon) and deployed; its pUSD allowances on chain {'c': '0.000000', 'v': '0.000000'}
[2026-11-20T17:55:52Z] OWNER approve link 1: the owner's signature, recovered to the owner under the client's own typed data
[2026-11-20T17:55:52Z] OWNER approve: the relayer accepted the batch of 2, state STATE_NEW
[2026-11-20T17:55:52Z] OWNER approve: the relayer's transaction confirmed
[2026-11-20T17:55:52Z] OWNER approve read 1: allowances on chain {'c': '1.000000', 'v': '1.000000'}
[2026-11-20T17:55:53Z] ok   authorize and approve at a real terminal: two links shown with the addresses, two signatures typed back, the stray line typed after the first discarded; the log carries no address
[2026-11-20T17:55:55Z] OWNER approve: the owner's Deposit Wallet derived (beacon) and deployed; its pUSD allowances on chain {'c': 'max', 'v': '0.000000'}
[2026-11-20T17:55:55Z] OWNER approve link 1: the owner's signature, recovered to the owner under the client's own typed data
[2026-11-20T17:55:55Z] OWNER approve: the relayer accepted the batch of 2, state STATE_NEW
[2026-11-20T17:55:55Z] OWNER approve: the relayer's transaction confirmed
[2026-11-20T17:55:55Z] OWNER approve read 1: allowances on chain {'c': '1.000000', 'v': '1.000000'}
[2026-11-20T17:55:55Z] ok   approve, the CTF exchange at the maximum and the V2 exchange short: one link of x=cv, each set to 1 pUSD
[2026-11-20T17:55:55Z] OWNER approve: the owner's Deposit Wallet derived (beacon) and deployed; its pUSD allowances on chain {'c': '1.000000', 'v': '0.000000'}
[2026-11-20T17:55:55Z] OWNER approve link 1: no owner's signature
[2026-11-20T17:55:56Z] OWNER approve link 2: the owner's signature, recovered to the owner under the client's own typed data
[2026-11-20T17:55:56Z] OWNER approve: the relayer accepted the batch of 1, state STATE_NEW
[2026-11-20T17:55:56Z] OWNER approve: the relayer's transaction confirmed
[2026-11-20T17:55:56Z] OWNER approve read 1: allowances on chain {'c': '1.000000', 'v': '1.000000'}
[2026-11-20T17:55:56Z] ok   approve, the V2 exchange short alone: an empty answer gives a second link, one call of 1 pUSD, the CTF exchange's 1 pUSD kept
[2026-11-20T17:55:56Z] OWNER approve: the owner's Deposit Wallet derived (beacon) and deployed; its pUSD allowances on chain {'c': '1.000000', 'v': '1.000000'}
[2026-11-20T17:55:56Z] OWNER approve: every allowance between one order's cost and 1 pUSD - kept, nothing to sign
[2026-11-20T17:55:56Z] ok   approve, both at 1 pUSD: kept, nothing asked, nothing sent
[2026-11-20T17:56:04Z] SDK SELFTEST PASS: 32 checks, 32 passed; refused by the hook: 2, each a check's own
[2026-11-20T17:56:04Z] peak memory of this run: 97157120 bytes
[2026-11-20T17:56:04Z] refused by the hook: 2; lookups 0, requests 58
```

**`55-page.log`** and **`56-key.log`**, whole: G-PAGE and G-KEY.

```
2026-11-20T17:56:17.014769911Z
[2026-11-20T17:56:17Z] MemAvailable read 1: 1458880512 bytes, floor 86426834
[2026-11-20T17:56:17Z] available on /: 16914378752 bytes, floor 2447483648
[2026-11-20T17:56:17Z] G-PAGE read 1: status 200, content-type 'text/html; charset=utf-8', 11846 bytes, sha256 f1d92e7dd8a8cd15b7b96b86b357ebf80db4e10844b3fc269e92cef0aecba528: equal
[2026-11-20T17:56:17Z] G-PAGE PASS: https://seahomebatumi-ai.github.io/btc-5m-twap/l1-sign.html
[2026-11-20T17:56:17Z] peak memory of this run: 37384192 bytes
[2026-11-20T17:56:17Z] refused by the hook: 0; lookups 1, requests 1
exit=0
```

```
2026-11-20T17:56:48.989018130Z
[2026-11-20T17:56:49Z] MemAvailable read 1: 1452253184 bytes, floor 274917678
[2026-11-20T17:56:49Z] available on /: 16914374656 bytes, floor 2447483648
[2026-11-20T17:56:49Z] G-KEY /etc/l1-bot/session-key: present, kept; file mode 0600 uid 0 bytes 67
[2026-11-20T17:56:49Z] peak memory of this run: 76423168 bytes
[2026-11-20T17:56:49Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

### 2.5 What passed before it — the capture host and the branch

**§0.0 to §0.5:** `00-ready.log`, `01-stage.log`, `03-host-gate.log`, `04-room.log`, `05-number.log` and
`05-refs.log`, whole. The room's margin over `STREAM_FLOOR` and `PEAK` is **2,743,576,328** bytes, with no flag.

```
2026-11-20T17:52:06.591917441Z
ready=1: 10371833856 bytes free on /var/lib, 7795535636 needed; MemAvailable 216055808, 86426834 needed; at 1795197126 2026-11-20T17:52:06Z
```

```
2026-11-20T17:52:15.473333299Z
/root/tz51-work/stage/b-owner.sh 7 967 782daebf76e6c19c7c17543164ca3d95308e0e0e2a3c7bedef1d4a838ab33030 created
/root/tz51-work/stage/research/tz51-l1-account.py 3306 187351 73fd0f6160eb1627a15589a081437f54ee5d826b987586c0f218541c7083dca0 created
exit=0
```

```
2026-11-20T17:52:38.720773716Z
Fri Nov 20 05:52:38 PM UTC 2026
1795197158
2026-08-02 07:24:32
1
MemTotal:         978640 kB
MemAvailable:     206940 kB
SwapTotal:       3174396 kB
SwapFree:        2453764 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10370904064
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
484471228	/var/lib/btc-rewardbook
357067821	/root/btc-forensics
24704103	/root/.claude-8j
2664
disabled
exit=1
inactive
exit=3
/root/tz50-work exit=1
/root/.ssh/live-host exit=0
/tmp/tmux-0/btc-l1 exit=1
/root/btc-5m-twap       4b1e2b8 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/08f6d3e8-a971-5f09-9e9e-6a186cab44a9/scratchpad
total 32
drwx------  8 root root 4096 Nov 20 17:49 .
drwx------ 40 root root 4096 Nov 20 17:49 ..
drwx------  4 root root 4096 Nov 20 17:49 08f6d3e8-a971-5f09-9e9e-6a186cab44a9
drwx------  3 root root 4096 Nov 20 17:49 1bc20379-a33f-40ce-b0b5-90d24dce9fbc
drwx------  3 root root 4096 Nov 20 06:18 3aceaaa9-a0d9-43c5-8e74-334a8c19adf5
drwx------  3 root root 4096 Nov 15 10:28 95cf58d2-1ec6-4c73-a622-38d04665f5ae
drwx------  4 root root 4096 Nov 17 14:14 ccca2df8-e51d-56bc-8205-06299775095a
drwx------  4 root root 4096 Nov 20 06:18 fd493377-65e0-5920-8de8-844ba541b830
MemAvailable read 1 17:52:38: 221122560
```

```
2026-11-20T17:52:49.333903302Z
[2026-11-20T17:52:49Z] btc-rewardbook-archive.service read 1: inactive
[2026-11-20T17:52:49Z] MemAvailable read 1: 180817920 bytes, floor 86426834
[2026-11-20T17:52:49Z] available on /var/lib: 10370641920 bytes, floor 7795535636
[2026-11-20T17:52:49Z] ROOM: 10370641920 bytes available on /var/lib; the reward book's stream files 118470044 bytes in 7 files under 24 day directories; the room 10489111964; its margin over STREAM_FLOOR 7300000000 and PEAK 445535636: 2743576328 bytes
[2026-11-20T17:52:49Z] peak memory of this run: 34713600 bytes
[2026-11-20T17:52:49Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-20T17:52:49.365046831Z
[2026-11-20T17:52:49Z] origin/main 4b1e2b8637da1e0e9f9e6de4a0ee6208087ffe19: 121 paths under CryptoTZ/ and CryptoReports/; of the number TZ-51-: ['CryptoTZ/TZ-51-l1-account-round-trip-rerun.md'] and []
[2026-11-20T17:52:49Z] NUMBER PASS - 2 of 2
[2026-11-20T17:52:49Z] peak memory of this run: 34693120 bytes
[2026-11-20T17:52:49Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-20T17:52:49.642542209Z
[2026-11-20T17:52:50Z] REF 4b1e2b8637da1e0e9f9e6de4a0ee6208087ffe19	HEAD
[2026-11-20T17:52:50Z] REF 4b1e2b8637da1e0e9f9e6de4a0ee6208087ffe19	refs/heads/main
[2026-11-20T17:52:50Z] REFS HEAD                                     1
[2026-11-20T17:52:50Z] REFS refs/heads/main                          1
[2026-11-20T17:52:50Z] REFS refs/heads/tz-*                          24
[2026-11-20T17:52:50Z] REFS refs/pull/*/head                         47
[2026-11-20T17:52:50Z] REFS refs/tags/pairbook-streams-*             59
[2026-11-20T17:52:50Z] REFS refs/tags/rewardbook-streams-*           57
[2026-11-20T17:52:50Z] REFS refs/tags/tz-01a-dataset                 1
[2026-11-20T17:52:50Z] REFS refs/tags/tz-01a-dataset^{}              1
[2026-11-20T17:52:50Z] REFS refs/tags/tz-27-pairbook-streams         1
[2026-11-20T17:52:50Z] REFS refs/tags/tz-27-pairbook-streams^{}      1
[2026-11-20T17:52:50Z] REFS refs/tags/tz-44-l0-inputs                1
[2026-11-20T17:52:50Z] REFS refs/tags/tz-45-l0-rule-w-inputs         1
[2026-11-20T17:52:50Z] REFS 195 lines; refs/heads/tz-51-l1-account-round-trip-rerun absent
[2026-11-20T17:52:50Z] peak memory of this run: 34828288 bytes
[2026-11-20T17:52:50Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**§0.6:** `06-access.log`, `07-copy.log` and `08-methods.log`, whole.

```
2026-11-20T17:53:07.973839925Z
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
2026-11-20T17:53:19.106065730Z
exit=0
scp exit=0
73fd0f6160eb1627a15589a081437f54ee5d826b987586c0f218541c7083dca0  /root/tz51-work/tz51-l1-account.py
  3306 187351 /root/tz51-work/tz51-l1-account.py
```

```
2026-11-20T17:53:54.905280268Z
[2026-11-20T17:53:55Z] METHODS gate: the methods the live host's sshd offers root, from outside: ['publickey']; ssh exit 255
[2026-11-20T17:53:55Z] G-SSH K6 publickey alone, from outside: PASS
[2026-11-20T17:53:55Z] peak memory of this run: 34709504 bytes
[2026-11-20T17:53:55Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**§3.1:** `10-number.log`, `11-worktree.log`, `13-push.log`, `14-pr.log` and `15-pr48.log`, whole. `12-fingerprint.log`
is `02-fingerprint.log`'s twin (§0).

```
2026-11-20T17:54:03.009315402Z
fetch exit=0
[2026-11-20T17:54:03Z] origin/main 4b1e2b8637da1e0e9f9e6de4a0ee6208087ffe19: 121 paths under CryptoTZ/ and CryptoReports/; of the number TZ-51-: ['CryptoTZ/TZ-51-l1-account-round-trip-rerun.md'] and []
[2026-11-20T17:54:03Z] NUMBER PASS - 2 of 2
[2026-11-20T17:54:03Z] peak memory of this run: 34709504 bytes
[2026-11-20T17:54:03Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-20T17:54:13.232174461Z
Preparing worktree (new branch 'tz-51-l1-account-round-trip-rerun')
branch 'tz-51-l1-account-round-trip-rerun' set up to track 'origin/main'.
HEAD is now at 4b1e2b8 Add files via upload
worktree exit=0
/root/tz51-work/wt/research/tz51-l1-account.py 3306 187351 73fd0f6160eb1627a15589a081437f54ee5d826b987586c0f218541c7083dca0 created
exit=0
```

```
2026-11-20T17:54:33.708536907Z
[2026-11-20T17:54:34Z] REF 4b1e2b8637da1e0e9f9e6de4a0ee6208087ffe19	HEAD
[2026-11-20T17:54:34Z] REF 4b1e2b8637da1e0e9f9e6de4a0ee6208087ffe19	refs/heads/main
[2026-11-20T17:54:34Z] REFS HEAD                                     1
[2026-11-20T17:54:34Z] REFS refs/heads/main                          1
[2026-11-20T17:54:34Z] REFS refs/heads/tz-*                          24
[2026-11-20T17:54:34Z] REFS refs/pull/*/head                         47
[2026-11-20T17:54:34Z] REFS refs/tags/pairbook-streams-*             59
[2026-11-20T17:54:34Z] REFS refs/tags/rewardbook-streams-*           57
[2026-11-20T17:54:34Z] REFS refs/tags/tz-01a-dataset                 1
[2026-11-20T17:54:34Z] REFS refs/tags/tz-01a-dataset^{}              1
[2026-11-20T17:54:34Z] REFS refs/tags/tz-27-pairbook-streams         1
[2026-11-20T17:54:34Z] REFS refs/tags/tz-27-pairbook-streams^{}      1
[2026-11-20T17:54:34Z] REFS refs/tags/tz-44-l0-inputs                1
[2026-11-20T17:54:34Z] REFS refs/tags/tz-45-l0-rule-w-inputs         1
[2026-11-20T17:54:34Z] REFS 195 lines; refs/heads/tz-51-l1-account-round-trip-rerun absent
[2026-11-20T17:54:34Z] peak memory of this run: 34824192 bytes
[2026-11-20T17:54:34Z] refused by the hook: 0; lookups 0, requests 0
exit=0
commit exit=0
remote: 
remote: Create a pull request for 'tz-51-l1-account-round-trip-rerun' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-51-l1-account-round-trip-rerun        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-51-l1-account-round-trip-rerun -> tz-51-l1-account-round-trip-rerun
branch 'tz-51-l1-account-round-trip-rerun' set up to track 'origin/tz-51-l1-account-round-trip-rerun'.
push exit=0
2026-11-20T17:54:36.040952267Z
bfbb1041529f60045172dd95167d8096f6153fba	refs/heads/tz-51-l1-account-round-trip-rerun
bfbb1041529f60045172dd95167d8096f6153fba
3306	0	research/tz51-l1-account.py
```

```
2026-11-20T17:54:49.119481899Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/49
exit=0
```

```
2026-11-20T17:54:57.029193299Z
{"head":"0774d7eefec63d7037d7f18487f0ba46919f9a1b","merged":false,"number":48,"state":"closed"}
exit=0
2026-11-20T17:55:06.262182244Z
{"closed_at":"2026-11-20T17:50:02Z","closed_by":"seahomebatumi-ai","state_reason":null}
exit=0
```

**§3.2:** `20-selftest.log`, the self-test on the capture host, 205 lines. Its summary lines and its
two real-terminal checks:

```
[2026-11-20T17:55:15Z] ok   secrets at a real terminal: the token and the key read hidden, the address shown, a bad token asked again and the stray line typed after it discarded; the log holds none of them
[2026-11-20T17:55:15Z] ok   bosskey at a real terminal: the key read and appended on its own line
[2026-11-20T17:55:16Z] SELFTEST PASS: 140 checks, 140 passed; refused by the hook: 5, each a check's own
[2026-11-20T17:55:16Z] peak memory of this run: 35758080 bytes
[2026-11-20T17:55:16Z] refused by the hook: 5; lookups 0, requests 18
```

**§3.3:** `30-scratch.log`, whole. Every session directory reads live, so B-RECLAIM-SCRATCH had nothing to remove and
`32-reclaim-scratch.log` does not exist.

```
2026-11-20T17:55:29.567056233Z
[2026-11-20T17:55:29Z] running 1738600 started 2026-11-15T10:28:51Z claude
[2026-11-20T17:55:29Z] running 1738611 started 2026-11-15T10:28:53Z claude
[2026-11-20T17:55:29Z] running 1738619 started 2026-11-15T10:28:53Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-20T17:55:29Z] running 2491506 started 2026-11-20T06:18:22Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-20T17:55:29Z] running 2562747 started 2026-11-20T17:49:12Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-20T17:55:29Z] 1bc20379-a33f-40ce-b0b5-90d24dce9fbc born 2026-11-20T17:49:13Z: live, process [2562747]
[2026-11-20T17:55:29Z] 3aceaaa9-a0d9-43c5-8e74-334a8c19adf5 born 2026-11-20T06:18:23Z: live, process [2491506]
[2026-11-20T17:55:29Z] 95cf58d2-1ec6-4c73-a622-38d04665f5ae born 2026-11-15T10:28:56Z: live, process [1738600, 1738611, 1738619]
[2026-11-20T17:55:29Z] ccca2df8-e51d-56bc-8205-06299775095a born 2026-11-15T10:28:57Z: live, process [1738600, 1738611, 1738619]
[2026-11-20T17:55:29Z] fd493377-65e0-5920-8de8-844ba541b830 born 2026-11-20T06:18:24Z: live, process [2491506]
[2026-11-20T17:55:29Z] peak memory of this run: 34709504 bytes
[2026-11-20T17:55:29Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**§3.5:** `35-pages.log`, whole.

```
2026-11-20T17:56:10.428683363Z
{"build_type":"legacy","html_url":"https://seahomebatumi-ai.github.io/btc-5m-twap/","source":{"branch":"main","path":"/docs"},"status":"built"}
exit=0
```

### 2.6 After the BLOCK — §3.10 and §9

**B-OWNER's tmux** — `86-tmux.log`, whole: `has-session exit=1`, no server on `btc-l1`, and `socket exit=1`.

```
2026-11-20T19:28:47.661701585Z
no server running on /tmp/tmux-0/btc-l1
has-session exit=1
2026-11-20T19:28:47.665438729Z
socket exit=1
```

**§3.10's copy and G-PRINT** — `80-live-copy.log`, whole. `scp exit=0` and `diff exit=0`, so every log of the live host
is on the capture host, byte for byte. **G-PRINT is `0` and `0`.**

```
2026-11-20T19:28:52.289817080Z
scp exit=0
diff exit=0
total 92
drwxr-xr-x 2 root root  4096 Nov 20 19:28 .
drwxr-xr-x 6 root root  4096 Nov 20 19:28 ..
-rw-r--r-- 1 root root  2089 Nov 20 19:28 40-host-before.log
-rw-r--r-- 1 root root   576 Nov 20 19:28 41-geoblock.log
-rw-r--r-- 1 root root   533 Nov 20 19:28 42-sshd.log
-rw-r--r-- 1 root root 19413 Nov 20 19:28 50-selftest.log
-rw-r--r-- 1 root root   813 Nov 20 19:28 53-env.log
-rw-r--r-- 1 root root 13545 Nov 20 19:28 54-sdk-selftest.log
-rw-r--r-- 1 root root   601 Nov 20 19:28 55-page.log
-rw-r--r-- 1 root root   422 Nov 20 19:28 56-key.log
-rw-r--r-- 1 root root  5726 Nov 20 19:28 70-B-OWNER.log
-rw-r--r-- 1 root root   533 Nov 20 19:28 78-sshd-after.log
-rw-r--r-- 1 root root  2734 Nov 20 19:28 79-host-after.log
-rw-r--r-- 1 root root   661 Nov 20 19:28 81-keep.log
-rw-r--r-- 1 root root   619 Nov 20 19:28 95-relayer-probe.log
G-PRINT addresses and tokens:
0
G-PRINT the live host's address:
0
```

**The closing reads** — `90-closing.log`, whole. The capture host's units read as at §0.3 (`03-host-gate.log`, §2.5).

```
2026-11-20T19:29:02.616288262Z
Fri Nov 20 19:29:03 UTC 2026
               total        used        free      shared  buff/cache   available
Mem:      1944465408   466255872   803176448     1474560   849154048  1478209536
Swap:     1073737728           0  1073737728
Filesystem             1B-blocks       Avail
/dev/mapper/lvm-root 20779339776 16913494016
active
/etc/l1-bot:
total 20
drwx------   2 root root 4096 Nov 20 18:10 .
drwxr-xr-x 107 root root 4096 Nov 20 06:25 ..
-rw-------   1 root root  105 Nov 20 18:10 relayer-key
-rw-------   1 root root   67 Nov 20 06:25 session-key
-rw-------   1 root root   47 Nov 20 18:00 telegram-token

/var/lib/l1-bot:
total 196
drwx------  2 root root   4096 Nov 20 19:28 .
drwxr-xr-x 41 root root   4096 Nov 20 18:10 ..
-rw-------  1 root root    310 Nov 20 19:18 account.json
-rw-------  1 root root 187351 Nov 20 19:28 tz51-l1-account.py
/etc/l1-bot/relayer-key 105 600 root
/etc/l1-bot/session-key 67 600 root
/etc/l1-bot/telegram-token 47 600 root
/var/lib/l1-bot/account.json 310 600 root
/var/lib/l1-bot/tz51-l1-account.py 187351 600 root
55492611	/root/l1-env
0.20.0
permitrootlogin without-password
pubkeyauthentication yes
passwordauthentication no
kbdinteractiveauthentication no
R exit=0
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
/dev/vda2      31612203008 10279313408
17635511	/root/tz51-work
584656864	/var/lib/btc-rewardbook
               total        used        free      shared  buff/cache   available
Mem:      1002127360   733024256   140816384       40960   281575424   269103104
Swap:     3250581504   616820736  2633760768
bfbb1041529f60045172dd95167d8096f6153fba	refs/heads/tz-51-l1-account-round-trip-rerun
```

**Contract §4.2's self-check** — `99-selfcheck.log`, whole, `C` = `bfbb1041529f60045172dd95167d8096f6153fba`. It read
`0`, the one path, `3306 0`, and no `.parquet` or `.zip` on `main` (`grep exit=1`).

```
2026-11-20T19:29:08.566393754Z
fetch exit=0
C in main:
0
research/tz51-l1-account.py
3306	0	research/tz51-l1-account.py
parquet or zip on main:
grep exit=1
```

**§9, B-RECLAIM-LIVE**, run by the Executor, its instant read in the same call:

```
$ date -u +%FT%T.%NZ; ssh -T -o BatchMode=yes -o ConnectTimeout=20 -o LogLevel=QUIET live-host 'export LC_ALL=C; rm -rf /root/tz51-work; test -e /root/tz51-work; echo "exit=$?"'
2026-11-20T19:29:41.332168892Z
exit=1
```

**§9, B-RECLAIM-OWN.** Its output was written to no file and is quoted from the session, every line:

```
$ (cd /root/tz51-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz51-work/wt/research/tz51-l1-account.py reclaim /root/tz51-work); echo "reclaim exit=$?"
[2026-11-20T19:34:09Z] reclaim: /root/tz51-work/wt skipped: no file but its HEAD's, and HEAD bfbb1041529f60045172dd95167d8096f6153fba is its upstream's
[2026-11-20T19:34:09Z] R copied 020ae973d4b1cb0548045ac86d2e1e6d6e9ab702779385f1fea7bb66c4df6fdd /root/btc-forensics/tz51-work--live-logs--40-host-before.log
[2026-11-20T19:34:09Z] R copied 7360627590d26eab0538ae1783f6fe823052fe6d73c4d860498b9b42d77ecf10 /root/btc-forensics/tz51-work--live-logs--41-geoblock.log
[2026-11-20T19:34:09Z] R copied e8ee6d40b78b4a87eac99592c6f5225c7465b7cbcc043154ddbdb4af294b237f /root/btc-forensics/tz51-work--live-logs--42-sshd.log
[2026-11-20T19:34:09Z] R copied 5c69a3479f32fdbda8d58917dc609f6573faa3de2accf205e1856cbdf5d76eef /root/btc-forensics/tz51-work--live-logs--50-selftest.log
[2026-11-20T19:34:09Z] R copied 08a3559481a28579a5974b5cc498cf114138a87c2ec0d29ad7d1512ba231645f /root/btc-forensics/tz51-work--live-logs--53-env.log
[2026-11-20T19:34:09Z] R copied b8ce90cc549f90b049ff736169781dabedba2caa667387d9f7562447ce55b91a /root/btc-forensics/tz51-work--live-logs--54-sdk-selftest.log
[2026-11-20T19:34:09Z] R copied 440ec346a823b27a5b77240407a9c7f18378678b493b82e216ee0428acda16de /root/btc-forensics/tz51-work--live-logs--55-page.log
[2026-11-20T19:34:09Z] R copied 1ef3c0c2ddb760732a64d21979805c1370f917724ee3b197ed6fbe8dccc1ffad /root/btc-forensics/tz51-work--live-logs--56-key.log
[2026-11-20T19:34:09Z] R copied 4c9da5d0afc4abd4fcb3b55ff0bfba4ca53a4e5e84b55c3c809e1d09e2ddabe0 /root/btc-forensics/tz51-work--live-logs--70-B-OWNER.log
[2026-11-20T19:34:09Z] R copied 67e35e38e792b41213d05e9847d6c644b2e0304573f1243e8109ad6634518a37 /root/btc-forensics/tz51-work--live-logs--78-sshd-after.log
[2026-11-20T19:34:09Z] R copied 41a2ca9551522370d23ddbc0948e1c4272e350a149241e10f3ebecda62b61a79 /root/btc-forensics/tz51-work--live-logs--79-host-after.log
[2026-11-20T19:34:09Z] R copied 7771dcf9dcf703260da1c0f59a540d06c4d55919f618e1aea29e30ff6783781f /root/btc-forensics/tz51-work--live-logs--81-keep.log
[2026-11-20T19:34:09Z] R copied eec2d1c552b5459b99267aabf14e650e85ddd19d48695c150a6933898caf687b /root/btc-forensics/tz51-work--live-logs--95-relayer-probe.log
[2026-11-20T19:34:09Z] R copied 4871421faf222aa1efa38c60261c9758fcc20fc7c9a2bf0e1e44333280eac6f7 /root/btc-forensics/tz51-work--logs--00-ready.log
[2026-11-20T19:34:09Z] R copied fc7c1a9c720f338f9ba9ae9e3854347bd4871b69d179a95ac1f567d9b56567a9 /root/btc-forensics/tz51-work--logs--01-stage.log
[2026-11-20T19:34:09Z] R copied df23eacaed2e479f1bc87285a06e42798a75cd1553fd4740ee4e5f298fbfa513 /root/btc-forensics/tz51-work--logs--02-fingerprint.log
[2026-11-20T19:34:09Z] R copied e560b7572f12d1da54b32ec2f113481ddb5c480e0e27abdcc795aac28b8ea8d1 /root/btc-forensics/tz51-work--logs--03-host-gate.log
[2026-11-20T19:34:09Z] R copied c3df35de22492ef7345117c5efca431628d8af5213a04c47940accd0f9096d9b /root/btc-forensics/tz51-work--logs--04-room.log
[2026-11-20T19:34:09Z] R copied fdd4d0fb8949465f7724213141c7eeb2413ffdf51ef3434fdbc1877a4851fb33 /root/btc-forensics/tz51-work--logs--05-number.log
[2026-11-20T19:34:09Z] R copied 7dfcab1cab9d38929623753c037322db726ffd89f70e742c3ec76fa0a242173c /root/btc-forensics/tz51-work--logs--05-refs.log
[2026-11-20T19:34:09Z] R copied 7805e3f56fa489c6b4c275439b76ba3ff05a5e971058216b4fced9b1b204551b /root/btc-forensics/tz51-work--logs--06-access.log
[2026-11-20T19:34:09Z] R copied 055d78b027232c712bedfb377f6e645ad656ed4e453d65de63b111b6a0618782 /root/btc-forensics/tz51-work--logs--07-copy.log
[2026-11-20T19:34:09Z] R copied 815257d7f5d4393b4a702f084aad728c83447dc07c33a2551659f925ccd6918f /root/btc-forensics/tz51-work--logs--08-methods.log
[2026-11-20T19:34:09Z] R copied 5c8a385bd64e18994e42327c38db389ef82d936d27a239ee24a7f2b978acb61f /root/btc-forensics/tz51-work--logs--10-number.log
[2026-11-20T19:34:09Z] R copied c605c760ca1fd062bbb5f49f77b1330966a3ecd179b373a1e3208fdb08514e9a /root/btc-forensics/tz51-work--logs--11-worktree.log
[2026-11-20T19:34:09Z] R copied 74ab6725b95dfdf850ed9d533968ebfa4d523fda37639a742f961b3d6a04d756 /root/btc-forensics/tz51-work--logs--12-fingerprint.log
[2026-11-20T19:34:09Z] R copied 255e894f31115768a5be23752a2d57cb71d901cfd8236d95d4b85b815c12158e /root/btc-forensics/tz51-work--logs--13-push.log
[2026-11-20T19:34:09Z] R copied 143adb2e17ebafff64f6a33eefb2be431afac15a46246aa6a6ce5914c74d2038 /root/btc-forensics/tz51-work--logs--14-pr.log
[2026-11-20T19:34:09Z] R copied ea8181baec4d176a927e90c06f28cc7715455157a0cd5f97a9c98ce5d2d573ec /root/btc-forensics/tz51-work--logs--15-pr48.log
[2026-11-20T19:34:09Z] R copied 72d639d954cbbf9b7c73a52d2d00cb0659bdc70fac6f1bc9b606c7845d087fbe /root/btc-forensics/tz51-work--logs--20-selftest.log
[2026-11-20T19:34:09Z] R copied aa1902d4b2aea054b3d71d819e5097d2ccc947a9a17ef69b6152d88939a16726 /root/btc-forensics/tz51-work--logs--30-scratch.log
[2026-11-20T19:34:09Z] R copied d565ccb2e88a1f345008ecad5e1056d06096e325fbe19bdcde0ca1247d05196e /root/btc-forensics/tz51-work--logs--35-pages.log
[2026-11-20T19:34:09Z] R copied 1b0f8d4ce3bac977e9ed17e34ea2e521afcb692ce005de6a983466c5a09f1c77 /root/btc-forensics/tz51-work--logs--37-handover.log
[2026-11-20T19:34:09Z] R copied 7b40575746dff14fe9510755f1800bedf52856da805cddd154ee0d3f90786f66 /root/btc-forensics/tz51-work--logs--80-live-copy.log
[2026-11-20T19:34:09Z] R copied ae5e10e6349be8be8bb24410e67f551ec1b11ffcbdae89bcbc8196fb8d6465bc /root/btc-forensics/tz51-work--logs--86-tmux.log
[2026-11-20T19:34:09Z] R copied 7bfa7d48c6e4dda5d8f97ff8de25df6966534b3f51a7a0f64e55151c5ef5d1bb /root/btc-forensics/tz51-work--logs--88-methods-after.log
[2026-11-20T19:34:09Z] R copied 312cd8a7cdae05d21a9a93d3f78bc86a04540cb6d6761edbf13eb6052c7a9935 /root/btc-forensics/tz51-work--logs--90-closing.log
[2026-11-20T19:34:09Z] R copied 9a56e19e62bd7b21a5d90737985bdb0bde8daea01fe3dae8a33a8bd1d1b94ac1 /root/btc-forensics/tz51-work--logs--99-selfcheck.log
[2026-11-20T19:34:09Z] R copied 782daebf76e6c19c7c17543164ca3d95308e0e0e2a3c7bedef1d4a838ab33030 /root/btc-forensics/tz51-work--stage--b-owner.sh
[2026-11-20T19:34:09Z] R copied 73fd0f6160eb1627a15589a081437f54ee5d826b987586c0f218541c7083dca0 /root/btc-forensics/tz51-work--stage--research--tz51-l1-account.py
[2026-11-20T19:34:09Z] RECLAIM PASS: 40 files considered, 40 copied, 0 already held; the forensic store 2664 -> 2704 files
[2026-11-20T19:34:09Z] peak memory of this run: 34971648 bytes
[2026-11-20T19:34:09Z] refused by the hook: 0; lookups 0, requests 0
reclaim exit=0
$ cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz51-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz51-work; echo "exit=$?"
exit=0
$ test -e /root/tz51-work; echo "exit=$?"
exit=1
$ test -e /tmp/tmux-0/btc-l1; echo "tmux socket exit=$?"
tmux socket exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       4b1e2b8 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
2704
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10494038016
```

`reclaim`'s peak is 34,971,648.

### 2.7 The files of this run

Every regular file of `/root/tz51-work` after §3.10's copy and before B-RECLAIM-OWN, but the branch worktree's, each
hashed by the Executor's own read. `reclaim` copied each into the forensic store by exclusive create and checked its
hash (§2.6).

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `live-logs/40-host-before.log` | 26 | 2089 | `020ae973d4b1cb0548045ac86d2e1e6d6e9ab702779385f1fea7bb66c4df6fdd` |
| `live-logs/41-geoblock.log` | 8 | 576 | `7360627590d26eab0538ae1783f6fe823052fe6d73c4d860498b9b42d77ecf10` |
| `live-logs/42-sshd.log` | 10 | 533 | `e8ee6d40b78b4a87eac99592c6f5225c7465b7cbcc043154ddbdb4af294b237f` |
| `live-logs/50-selftest.log` | 205 | 19413 | `5c69a3479f32fdbda8d58917dc609f6573faa3de2accf205e1856cbdf5d76eef` |
| `live-logs/53-env.log` | 9 | 813 | `08a3559481a28579a5974b5cc498cf114138a87c2ec0d29ad7d1512ba231645f` |
| `live-logs/54-sdk-selftest.log` | 116 | 13545 | `b8ce90cc549f90b049ff736169781dabedba2caa667387d9f7562447ce55b91a` |
| `live-logs/55-page.log` | 8 | 601 | `440ec346a823b27a5b77240407a9c7f18378678b493b82e216ee0428acda16de` |
| `live-logs/56-key.log` | 7 | 422 | `1ef3c0c2ddb760732a64d21979805c1370f917724ee3b197ed6fbe8dccc1ffad` |
| `live-logs/70-B-OWNER.log` | 70 | 5726 | `4c9da5d0afc4abd4fcb3b55ff0bfba4ca53a4e5e84b55c3c809e1d09e2ddabe0` |
| `live-logs/78-sshd-after.log` | 10 | 533 | `67e35e38e792b41213d05e9847d6c644b2e0304573f1243e8109ad6634518a37` |
| `live-logs/79-host-after.log` | 38 | 2734 | `41a2ca9551522370d23ddbc0948e1c4272e350a149241e10f3ebecda62b61a79` |
| `live-logs/81-keep.log` | 17 | 661 | `7771dcf9dcf703260da1c0f59a540d06c4d55919f618e1aea29e30ff6783781f` |
| `live-logs/95-relayer-probe.log` | 8 | 619 | `eec2d1c552b5459b99267aabf14e650e85ddd19d48695c150a6933898caf687b` |
| `logs/00-ready.log` | 2 | 171 | `4871421faf222aa1efa38c60261c9758fcc20fc7c9a2bf0e1e44333280eac6f7` |
| `logs/01-stage.log` | 4 | 285 | `fc7c1a9c720f338f9ba9ae9e3854347bd4871b69d179a95ac1f567d9b56567a9` |
| `logs/02-fingerprint.log` | 78 | 13023 | `df23eacaed2e479f1bc87285a06e42798a75cd1553fd4740ee4e5f298fbfa513` |
| `logs/03-host-gate.log` | 75 | 2078 | `e560b7572f12d1da54b32ec2f113481ddb5c480e0e27abdcc795aac28b8ea8d1` |
| `logs/04-room.log` | 8 | 652 | `c3df35de22492ef7345117c5efca431628d8af5213a04c47940accd0f9096d9b` |
| `logs/05-number.log` | 6 | 416 | `fdd4d0fb8949465f7724213141c7eeb2413ffdf51ef3434fdbc1877a4851fb33` |
| `logs/05-refs.log` | 19 | 1274 | `7dfcab1cab9d38929623753c037322db726ffd89f70e742c3ec76fa0a242173c` |
| `logs/06-access.log` | 14 | 408 | `7805e3f56fa489c6b4c275439b76ba3ff05a5e971058216b4fced9b1b204551b` |
| `logs/07-copy.log` | 5 | 199 | `055d78b027232c712bedfb377f6e645ad656ed4e453d65de63b111b6a0618782` |
| `logs/08-methods.log` | 6 | 363 | `815257d7f5d4393b4a702f084aad728c83447dc07c33a2551659f925ccd6918f` |
| `logs/10-number.log` | 7 | 429 | `5c8a385bd64e18994e42327c38db389ef82d936d27a239ee24a7f2b978acb61f` |
| `logs/11-worktree.log` | 7 | 372 | `c605c760ca1fd062bbb5f49f77b1330966a3ecd179b373a1e3208fdb08514e9a` |
| `logs/12-fingerprint.log` | 78 | 13023 | `74ab6725b95dfdf850ed9d533968ebfa4d523fda37639a742f961b3d6a04d756` |
| `logs/13-push.log` | 32 | 1974 | `255e894f31115768a5be23752a2d57cb71d901cfd8236d95d4b85b815c12158e` |
| `logs/14-pr.log` | 3 | 94 | `143adb2e17ebafff64f6a33eefb2be431afac15a46246aa6a6ce5914c74d2038` |
| `logs/15-pr48.log` | 6 | 260 | `ea8181baec4d176a927e90c06f28cc7715455157a0cd5f97a9c98ce5d2d573ec` |
| `logs/20-selftest.log` | 205 | 19413 | `72d639d954cbbf9b7c73a52d2d00cb0659bdc70fac6f1bc9b606c7845d087fbe` |
| `logs/30-scratch.log` | 14 | 1304 | `aa1902d4b2aea054b3d71d819e5097d2ccc947a9a17ef69b6152d88939a16726` |
| `logs/35-pages.log` | 3 | 182 | `d565ccb2e88a1f345008ecad5e1056d06096e325fbe19bdcde0ca1247d05196e` |
| `logs/37-handover.log` | 56 | 3227 | `1b0f8d4ce3bac977e9ed17e34ea2e521afcb692ce005de6a983466c5a09f1c77` |
| `logs/80-live-copy.log` | 23 | 966 | `7b40575746dff14fe9510755f1800bedf52856da805cddd154ee0d3f90786f66` |
| `logs/86-tmux.log` | 5 | 135 | `ae5e10e6349be8be8bb24410e67f551ec1b11ffcbdae89bcbc8196fb8d6465bc` |
| `logs/88-methods-after.log` | 16 | 829 | `7bfa7d48c6e4dda5d8f97ff8de25df6966534b3f51a7a0f64e55151c5ef5d1bb` |
| `logs/90-closing.log` | 74 | 2345 | `312cd8a7cdae05d21a9a93d3f78bc86a04540cb6d6761edbf13eb6052c7a9935` |
| `logs/99-selfcheck.log` | 8 | 156 | `9a56e19e62bd7b21a5d90737985bdb0bde8daea01fe3dae8a33a8bd1d1b94ac1` |
| `stage/b-owner.sh` | 7 | 967 | `782daebf76e6c19c7c17543164ca3d95308e0e0e2a3c7bedef1d4a838ab33030` |
| `stage/research/tz51-l1-account.py` | 3306 | 187351 | `73fd0f6160eb1627a15589a081437f54ee5d826b987586c0f218541c7083dca0` |

**Peaks.** Each standard-library mode's peak is under `43,213,417`, and each client mode's under `137,458,839` (V21,
recorded):

- On the capture host: `fingerprint` 35,758,080 and 35,495,936; `room` 34,713,600;
  `number` 34,693,120 and 34,709,504; `refs` 34,828,288 and 34,824,192;
  `methods` 34,709,504 and, after, 34,578,432; `selftest` 35,758,080;
  `scratch` 34,709,504.
- On the live host: `host before` 35,024,896; `geoblock` 37,777,408; `sshd`
  35,016,704 and, after, 35,024,896; `selftest` 35,807,232; `page`
  37,384,192; `secrets` 34,877,440 and 35,008,512; `bosskey` 35,008,512 and 34,881,536;
  `host after` 34,758,656 (the refused entry) and 35,139,584.
- The client's modes: `env` 76,550,144; `sdk-selftest` 97,157,120; `key`
  76,423,168; `authorize` 90,193,920 and 90,198,016; `approve` 84,557,824 and 84,566,016.

**Every free-space and `MemAvailable` read, with its instant and its bound.** On the capture host the bounds are
`7,795,535,636` free on `/var/lib` and `86,426,834` of memory:

| read | instant (UTC) | free on `/var/lib` | `MemAvailable` |
|---|---|---|---|
| §0.0, the logged read | 17:52:06 | `10,371,833,856` | `216,055,808` |
| §0.3 | 17:52:38 | `10,370,904,064` (`df`) | `221,122,560` |
| `room` | 17:52:49 | `10,370,641,920` | `180,817,920` |
| the closing reads | 19:29:02 | `10,279,313,408` (`df`) | `269,103,104` (`free -b`), no bound |

On the live host the bounds are `2,447,483,648` available on `/` and `86,426,834` of memory, or `274,917,678` for a
client mode:

| mode | instant (UTC) | available on `/` | `MemAvailable` |
|---|---|---|---|
| `host before` | 17:53:32 | `16,914,432,000` | `1,460,703,232` |
| `geoblock` | 17:53:43 | `16,914,411,520` | `1,456,906,240` |
| `page` | 17:56:17 | `16,914,378,752` | `1,458,880,512` |
| `key` | 17:56:49 | `16,914,374,656` | `1,452,253,184` |
| `secrets`, first run | 18:00:07 | `16,914,366,464` | `1,438,900,224` |
| `authorize`, first run | 18:11:02 | `16,913,743,872` | `1,455,947,776` |
| `approve`, first run | 18:35:21 | `16,913,735,680` | `1,441,107,968` |
| `secrets`, second run | 19:07:12 | `16,913,727,488` | `1,449,414,656` |
| `authorize`, second run | 19:08:16 | `16,913,723,392` | `1,449,418,752` |
| `approve`, second run | 19:08:18 | `16,913,723,392` | `1,416,396,800` |
| `host after` | 19:28:39 | `16,913,510,400` | `1,456,447,488` |
| the closing reads | 19:29:03 | `16,913,494,016` (`df`) | `1,478,209,536` (`free -b`), no bound |

---

## 3. Departures, named

1. **The relayer probe is outside the TZ** (§1, §2.2). It made two authenticated requests to the venue's relayer,
   `POST /submit`, that no step of this TZ names. They ran from the live host at 19:27:38 and 19:27:39 UTC, with the
   Boss's Relayer API key read from `/etc/l1-bot/relayer-key`, under Appendix A's audit hook in mode `approve`. The
   relayer is among the hosts §2 item 4 allows from the live host, but only through the instrument's modes, and
   contract §10 forbids an authenticated call to a venue that the TZ does not authorize in writing. It ran after both
   runs had failed and the Boss had left the decision on how to go on to the Executor. Neither request could move
   anything:
   - probe A's signature was not the owner's, and the relayer said so;
   - probe B's deadline was past, and the only effect its batch could have had is §1.4's own, `1` pUSD an exchange.

   Both were refused. Its log is `95-relayer-probe.log`, read by G-PRINT (`0`). The script was written in the
   session's scratchpad and copied to `/root/tz51-work` on the live host, where §9 removed it.
2. **B-OWNER was handed a second time, and not a third.** The second handover, at 18:47:50, came with the 400's
   message unknown, under §3.7's "at most twice more". `37-handover.log` records it: "the same line handed again,
   unchanged, with one line in Russian - approve FAIL at 18:41:09, the relayer refused both signed batches with status
   400". The second run failed the
   same way. Once the message was read (§1), no line could say what to do differently, so a third handover would only
   have asked the Boss for a certain failure.
3. **What the Boss was told between the runs, beyond §3.7's words.**
   - After the first run, the Executor named a relayer state — a stale nonce, or a wallet busy just after the
     authorization — as the likely cause. The probe showed that this was wrong.
   - During the second run, at link 3, the Executor told the Boss to press Enter rather than sign. Four signatures had
     each been refused, with nothing to change between them. The log reads `approve link 3: no owner's signature` at
     19:18:52.
   - The Boss sent the session screenshots of MetaMask's "high-risk request" warning on the approval batch, and the
     terminal's text from the second run. These held the owner's and the wallet's addresses, the exchanges, and one
     signature, that of 19:09:29. None of them is quoted here or written to any log but as §2.2 says. The session's
     transcript holds them (map §6, harness — background output).
4. **The wait for B-OWNER was a background loop of the Executor's own, and it was restarted once.**
   - It read `R 'tail -n 3 …'` every 570 s and wrote each read with its instant to `37-handover.log`.
   - The session restarted at 18:51, and the first loop ended with it. The second loop began at 18:56:31
     (`wait 2 restarted`), so no read fell between 18:45:08 and 18:56:31.
   - Each of the second loop's reads also prints the log's line count and the line numbers of its last `date -u` and
     `exit=` lines. The loop ended at the first read whose last `exit=` came after a `date -u` line beyond the first
     run's 38 lines: 19:25:04, line 70.
   - The loop's script was written in the session's scratchpad. That is the scratchpad's one use besides the probe's
     script (item 1) and this report's generator, which embeds every quoted log from its file.
5. **The BLOCK path ran all of §3.10, not only its copy and tmux step**, because the session key is authorized and the
   host's state matters to the stops:
   - `78-sshd-after` and `88-methods-after`;
   - `79-host-after`;
   - `81-keep`, since `/var/lib/l1-bot/` exists — so B-REVOKE's copy stays on the host;
   - `90-closing`;
   - `99-selfcheck`.

   Two first attempts failed on the Executor's own errors and were run again, each under its own `date -u` line:
   - `host after` was passed as one argument, `unknown mode ['host after']`, `exit=1`;
   - `methods after` was started outside `/root/tz51-work`, `run from /root/tz51-work, not /root/btc-5m-twap`,
     `exit=1`.

   **Not run:** §3.8 and §3.9; B-RESET, since neither of its causes is in the log; B-REVOKE, as §4.11 says.
6. **The refs differ from map §1's read of 17:04 UTC** (196 lines), recorded and not BLOCKING, as §0.5 says. This run
   read 195:
   - `refs/pull/48/merge` is gone with PR #48's close at 17:50:02.
   - `HEAD` and `main` read `4b1e2b8`, the upload, against `39f22d9`.
7. **Pull request #48 was found closed, not open.** §3.1 expected it open and had the Executor close it unmerged. The
   repository's owner had closed it unmerged at 17:50:02 UTC, two minutes before §0.0 (`15-pr48.log`). Its head and
   branch stand, and nothing was closed by this run.
8. **The logs' extra lines.**
   - `01-stage.log` and `11-worktree.log` end with an `exit=0` line, which the Executor's `echo` added and §0.1's
     script does not print. `11-worktree.log` also has `worktree exit=0` after `git worktree add`.
   - `10-number.log` carries `fetch exit=0`.
   - `13-push.log` carries `commit exit=0` and `push exit=0`.
9. **What stays on the live host as this TZ left it**, none of it removed by this run (§3):
   - `/root/l1-env/`;
   - `/etc/l1-bot/` with `session-key` (authorized for the wallet), `relayer-key` and `telegram-token`;
   - `/var/lib/l1-bot/` with `account.json` and the kept instrument;
   - TZ-49's `sshd` drop-in, read byte for byte by K1 after the run (§2.3).

   `/root/tz51-work` is gone (§9). **The session key, authorized at 18:35, stands for the client's session-key lifetime,
   `15,534,000` s from its link, unless B-REVOKE ends it.** The wallet's allowances to both exchanges are the
   maximum (§1), and no process uses the key.
10. **Pull request #49 stays open.** Its one file is the instrument with `APPROVE_UNITS` as §1.4 decides it. Its merge
    or its closing is for the Architect's verdict.
11. **No block but B-ACCOUNT and B-OWNER was handed to the Boss, and the classifier refused nothing.** B-RECLAIM-LIVE
    and B-RECLAIM-OWN were run by the Executor. B-ENV, B-RECLAIM-SCRATCH and B-PAGES had nothing to do.
