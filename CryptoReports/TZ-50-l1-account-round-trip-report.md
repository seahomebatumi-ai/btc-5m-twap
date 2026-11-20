# TZ-50 — L1, the bot's account and one order's round trip from the live host — REPORT

**Status: BLOCKED at §3.7, B-OWNER — a defect of the instrument at its terminal, before any question was asked.**
The Boss ran B-OWNER's paste twice, at 07:55:10 and 08:00:57 UTC on 2026-11-20 (`70-B-OWNER.log`). Both runs
stopped in the paste's first mode, `secrets`, at the same line, `exit=1`. `Tty.__init__`, line 1446 of
`research/tz50-l1-account.py`, runs `open("/dev/tty", "r+", encoding="utf-8", errors="replace")`, and it raised
`io.UnsupportedOperation: File or stream is not seekable.` A terminal is never seekable, so this line fails on every
terminal. Every one of the Boss's modes builds its terminal through it: `secrets`, `bosskey`, `authorize`,
`approve`, and B-REVOKE's `revoke` (lines 1481, 1534 and 2029). So no run of the paste, unchanged or not, can get past
it. The instrument is fixed byte for byte by Appendix A. Nothing was asked, typed or written by either run.

- **G-RT: not read.** No order was placed, no relayer or CLOB request was made, nothing was signed, and no money
  moved. §3.8 and §3.9 did not run.
- **Everything before §3.7 passed.** FINGERPRINT PASS twice, 64 of 64 `frozen` rows equal. Host gate 7 of 7. Room
  margin **2,797,417,277** bytes. NUMBER PASS 2 of 2, twice. Refs 189 lines, the branch absent before the push.
  Live host gate 5 of 5, at `host before` and `host after`. **G-GEO PASS** over IPv4, `blocked False`, `country 'BG'`,
  before any key existed. **G-SSH 6 of 6.** `SELFTEST PASS: 135 checks, 135 passed`, `refused by the hook: 5`, on both
  hosts. **G-ENV** wheels 35 of 35, `14422773` bytes. B-ENV `exit=0`, `55,492,611` bytes. `G-ENV installed PASS`, 34
  distributions. `SDK SELFTEST PASS: 31 checks, 31 passed`, `refused by the hook: 2`. **G-PAGE PASS**, after GitHub
  Pages was turned on by `gh`. **G-KEY made.**
- **Branch** `tz-50-l1-account-round-trip` at `0774d7eefec63d7037d7f18487f0ba46919f9a1b`, one file, `3091 0`.
  **Pull request #48**, open. The §4.2 self-check read `0`, one path, nothing.
- **L1's paths on the live host, left as they stand** (§3, a BLOCK after §3.6):
  - `/root/l1-env/` is the client's environment: `polymarket-client` `0.20.0`, `55,492,611` bytes.
  - `/etc/l1-bot/` is `0700` and root's. It holds `session-key` alone, `0600`, root's, 67 bytes — a key that no owner
    ever authorized.
  - Absent: `relayer-key`, `telegram-token`, `chat-id` and `/var/lib/l1-bot/`.
  - Root's `authorized_keys` holds the Executor's key alone.
- **The capture host:** no unit was started, stopped or touched, and no store was written. The recorder, the reward
  book and the advisor kept the same `MainPID`, `NRestarts` and `ActiveState` from §0.3 to the closing reads.
- **Handed to the Boss:** B-ACCOUNT and B-OWNER, once, at 06:26:06 UTC. The classifier refused nothing.
- **No address of either host, of the bot's owner, wallet or session key, and no key, token or signature** is in this
  report. Of the live host's name, only its first label is given.

---

## 0. Fingerprint

`I0 fingerprint` (`logs/02-fingerprint.log`, 06:21:08 UTC) and `I fingerprint` from the branch's worktree
(`logs/12-fingerprint.log`, 06:22:49 UTC) each printed `FINGERPRINT PASS`. Their lines are identical but for the
instants and the peak.

```
[2026-11-20T06:21:09Z] FINGERPRINT PASS: revision 2026-11-20-a; anchors 6 of 6, 4 re-derived; rows 67: frozen 64 of 64 equal, tracked 2, reported 1; the signing page on main equal to Appendix B
```

**Revision string:** `2026-11-20-a`. **Anchors:**

| anchor | read | how |
|---|---|---|
| `A1` | `229a944f2d51` | the map |
| `A2` | `6c5089330629` | the map; re-derived from `research/twap-divergence.py` |
| `A3` | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | the map |
| `A4` | `6ac6e10aeabc` | the map; re-derived from `BTC-EXECUTOR-INSTRUCTIONS.md` |
| `A5` | `0f6c90451cbd` | the map; re-derived from `research/recorder/recorder.py` |
| `A6` | `729f0bcdbee3` | the map; re-derived from `research/pfair.py` |

**Every row of the map's §0 table**, as `fingerprint` printed it: 67 rows, 64 `frozen` and each equal, 2 `tracked`,
1 `reported`. `docs/l1-sign.html` on `main` is equal to Appendix B, `11846` bytes, `f1d92e7d…`.

| path | lines | bytes | state | SHA-256 |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 1069 | 177533 | reported | `1a81b3e707e37a787bd138f5bbf98bb4ac40714adf2d8727405d6531b3d91e56` |
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

**The model:** Claude Opus 5.5, as the TZ names it. The session's own record reads `claude-opus-5-5`, both
`session_context.model` and `last_served_model`.

---

## 1. The blocker

§3.7 hands the Boss one paste, B-OWNER. It runs four modes on the live host, each gated on the one before it:
`secrets`, `bosskey`, `authorize` and `approve`. Each asks the Boss at his terminal, through the instrument's class
`Tty` (Appendix A, lines 1442 to 1460), whose constructor is:

```python


class Tty:
    """The Boss's terminal: what he is asked and shown goes there, and to no log."""

    def __init__(self, path="/dev/tty"):
        self.fh = open(path, "r+", encoding="utf-8", errors="replace")

    def say(self, text):
        self.fh.write(text + "\n")
        self.fh.flush()

    def ask(self, prompt, hidden=False):
        if hidden:
            return getpass.getpass(prompt, stream=self.fh)
        self.fh.write(prompt)
        self.fh.flush()
        line = self.fh.readline()
        if line == "":
            raise EOFError("the terminal closed")
```

`open` with mode `"r+"` in text mode builds a `BufferedRandom` over the file, and Python's `BufferedRandom` requires a
seekable stream. `/dev/tty` is a character device and never seekable, so the constructor raises
`io.UnsupportedOperation: File or stream is not seekable.` before it returns. The log shows exactly this, twice, at
line 1446 called from line 1481 (`mode_secrets`). It was raised after `secrets`' floors and before its first word to
the terminal. `secrets` failed, so the `&&` chain ran nothing after it, and the paste wrote `exit=1`.

**It cannot pass on any run.** `Tty()` is constructed at lines 1481 (`secrets`), 1534 (`bosskey`) and 2029
(`mode_owner`, which serves `authorize`, `approve` and `revoke`), and every terminal is non-seekable. The self-tests
passed because they never construct `Tty`:

- `selftest` checks the hook's pure decision on the open `("/dev/tty", "r+", None)` in `secrets`, and allows it (line
  2929).
- `sdk-selftest` and `selftest` drive every Boss mode through `FakeTty` (line 2314).

So the self-tests passed (135 of 135 and 31 of 31), and the defect showed only at the Boss's real terminal.

**§3.7 says**, for another exit: "the Executor reads the log whole, names the mode and the line that stopped it, and
hands the same paste again, unchanged, with one line in Russian saying what to do differently — at most twice more".
The mode is `secrets` and the line is 1446. **No line can say what to do differently**, because nothing the Boss does
changes the outcome. Neither B-RESET's causes appear in the log, a relayer refusing the key or `the owner's Deposit
Wallet is not deployed`. The paste was therefore not handed again (§3 item 2). The instrument is this TZ's
Validation, fixed byte for byte (§5; contract §6). A product defect stops the run, and its correction is a new TZ.
The run went to §3.10's copy and §9, as §3 says for a BLOCK.

---

## 2. The evidence

Every live host's log below is quoted whole as §3.10's copy brought it back, byte for byte (`diff exit=0`, §2.5). Its
SHA-256 is in §2.6, and its copy in the forensic store is `/root/btc-forensics/tz50-work--<path with / as -->`.

### 2.1 B-OWNER — `70-B-OWNER.log` and `37-handover.log`

**`70-B-OWNER.log`**, whole: the Boss's two runs of the paste, each under its own `date -u` line.

```
2026-11-20T07:55:10.406386065Z
[2026-11-20T07:55:10Z] MemAvailable read 1: 1455759360 bytes, floor 85051706
[2026-11-20T07:55:10Z] available on /: 16909746176 bytes, floor 2447483648
[2026-11-20T07:55:10Z] peak memory of this run: 34271232 bytes
[2026-11-20T07:55:10Z] refused by the hook: 0; lookups 0, requests 0
Traceback (most recent call last):
  File "/root/tz50-work/tz50-l1-account.py", line 3091, in <module>
    sys.exit(main(sys.argv[1:]))
             ^^^^^^^^^^^^^^^^^^
  File "/root/tz50-work/tz50-l1-account.py", line 3083, in main
    rc = table[mode]()
         ^^^^^^^^^^^^^
  File "/root/tz50-work/tz50-l1-account.py", line 1481, in mode_secrets
    tty = Tty()
          ^^^^^
  File "/root/tz50-work/tz50-l1-account.py", line 1446, in __init__
    self.fh = open(path, "r+", encoding="utf-8", errors="replace")
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
io.UnsupportedOperation: File or stream is not seekable.
exit=1
2026-11-20T08:00:57.132465941Z
[2026-11-20T08:00:57Z] MemAvailable read 1: 1462894592 bytes, floor 85051706
[2026-11-20T08:00:57Z] available on /: 16909758464 bytes, floor 2447483648
[2026-11-20T08:00:57Z] peak memory of this run: 34271232 bytes
[2026-11-20T08:00:57Z] refused by the hook: 0; lookups 0, requests 0
Traceback (most recent call last):
  File "/root/tz50-work/tz50-l1-account.py", line 3091, in <module>
    sys.exit(main(sys.argv[1:]))
             ^^^^^^^^^^^^^^^^^^
  File "/root/tz50-work/tz50-l1-account.py", line 3083, in main
    rc = table[mode]()
         ^^^^^^^^^^^^^
  File "/root/tz50-work/tz50-l1-account.py", line 1481, in mode_secrets
    tty = Tty()
          ^^^^^
  File "/root/tz50-work/tz50-l1-account.py", line 1446, in __init__
    self.fh = open(path, "r+", encoding="utf-8", errors="replace")
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
io.UnsupportedOperation: File or stream is not seekable.
exit=1
```

**`37-handover.log`**, whole. The handover's instant comes first. Then come the Executor's reads of the log above with
`R 'tail -n 3 …'`, every 570 s, by a background loop that ended at the first read whose last line was `exit=`. The
reads before the Boss's first run found no log, so `tail` printed its error and `R` read `exit=1`. The last read came
at 08:01:21, after both runs.

```
handover 2026-11-20T06:26:06.351436670Z epoch 1795155966: B-ACCOUNT and B-OWNER handed to the Boss, once, in one message; the bound 8 hours from this instant
read 2026-11-20T06:35:42.471552898Z
tail: cannot open '/root/tz50-work/logs/70-B-OWNER.log' for reading: No such file or directory
R exit=1
read 2026-11-20T06:45:13.545127186Z
tail: cannot open '/root/tz50-work/logs/70-B-OWNER.log' for reading: No such file or directory
R exit=1
read 2026-11-20T06:54:44.565945709Z
tail: cannot open '/root/tz50-work/logs/70-B-OWNER.log' for reading: No such file or directory
R exit=1
read 2026-11-20T07:04:15.593370971Z
tail: cannot open '/root/tz50-work/logs/70-B-OWNER.log' for reading: No such file or directory
R exit=1
read 2026-11-20T07:13:46.607013398Z
tail: cannot open '/root/tz50-work/logs/70-B-OWNER.log' for reading: No such file or directory
R exit=1
read 2026-11-20T07:23:17.625075564Z
tail: cannot open '/root/tz50-work/logs/70-B-OWNER.log' for reading: No such file or directory
R exit=1
read 2026-11-20T07:32:48.645916444Z
tail: cannot open '/root/tz50-work/logs/70-B-OWNER.log' for reading: No such file or directory
R exit=1
read 2026-11-20T07:42:19.709514469Z
tail: cannot open '/root/tz50-work/logs/70-B-OWNER.log' for reading: No such file or directory
R exit=1
read 2026-11-20T07:51:50.750205209Z
tail: cannot open '/root/tz50-work/logs/70-B-OWNER.log' for reading: No such file or directory
R exit=1
read 2026-11-20T08:01:21.787296845Z
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
io.UnsupportedOperation: File or stream is not seekable.
exit=1
R exit=0
```

The Boss also pasted his terminal into the session after the second run: the paste's line, then `ssh`'s line that
the connection closed. It showed nothing else, as the log shows. That text carried two addresses, which are not
repeated here (§3 item 7).

### 2.2 The live host after it — `79-host-after.log`

`L 'host after' 79-host-after`, before the copy, is the read §3 asks for to name L1's paths by their state. The live
host gate read 5 of 5 and both floors held. Root's authorized keys are the Executor's alone. The paths:

- `/etc/l1-bot` is `0700` with `session-key` alone, `0600`, 67 bytes.
- `relayer-key`, `telegram-token`, `chat-id` and `/var/lib/l1-bot` are absent.
- `/root/l1-env` is present.

```
2026-11-20T08:02:45.562368101Z
[2026-11-20T08:02:45Z] LH1 hostname vs-2348: PASS
[2026-11-20T08:02:45Z] LH2 Ubuntu 24.04: PASS
[2026-11-20T08:02:45Z] LH3 Python 3.12: PASS
[2026-11-20T08:02:45Z] LH4 not the capture host: PASS
[2026-11-20T08:02:45Z] LH5 the host key pinned at TZ-47's first connection: PASS
[2026-11-20T08:02:45Z] LIVE HOST GATE PASS: 5 of 5
[2026-11-20T08:02:45Z] MemAvailable read 1: 1462820864 bytes, floor 85051706
[2026-11-20T08:02:45Z] available on /: 16909754368 bytes, floor 2447483648
[2026-11-20T08:02:45Z] HOST after: kernel 6.8.0-138-generic; Python 3.12.3; Ubuntu 24.04.5 LTS; MemTotal 1944465408 MemAvailable 1462820864 SwapTotal 1073737728 SwapFree 1073737728; / 20779339776 bytes, 16909754368 available
[2026-11-20T08:02:45Z] LOCALE /etc/default/locale: LANG="ru_UA.UTF-8"
[2026-11-20T08:02:45Z] LOCALE `locale` in this session, exit 0: LANG=ru_UA.UTF-8; LANGUAGE=; LC_CTYPE="C"; LC_NUMERIC="C"; LC_TIME="C"; LC_COLLATE="C"; LC_MONETARY="C"; LC_MESSAGES="C"; LC_PAPER="C"; LC_NAME="C"; LC_ADDRESS="C"; LC_TELEPHONE="C"; LC_MEASUREMENT="C"; LC_IDENTIFICATION="C"; LC_ALL=C
[2026-11-20T08:02:45Z] CLOCK exit 0: NTP=yes; NTPSynchronized=yes; TimeUSec=Fri 2026-11-20 08:02:45 UTC
[2026-11-20T08:02:45Z] SSHD authorized keys of root: [('ssh-ed25519', 'SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo')]; the Executor's among them: True
[2026-11-20T08:02:45Z] PATH /etc/l1-bot: dir mode 0700 uid 0 bytes 4096
[2026-11-20T08:02:45Z] PATH /etc/l1-bot/session-key: file mode 0600 uid 0 bytes 67
[2026-11-20T08:02:45Z] PATH /etc/l1-bot/relayer-key: absent
[2026-11-20T08:02:45Z] PATH /etc/l1-bot/telegram-token: absent
[2026-11-20T08:02:45Z] PATH /etc/l1-bot/chat-id: absent
[2026-11-20T08:02:45Z] PATH /var/lib/l1-bot: absent
[2026-11-20T08:02:45Z] PATH /var/lib/l1-bot/account.json: absent
[2026-11-20T08:02:45Z] PATH /root/l1-env: dir mode 0755 uid 0 bytes 4096
[2026-11-20T08:02:45Z] PATH /root/tz50-work/wheels: dir mode 0755 uid 0 bytes 4096
[2026-11-20T08:02:45Z] peak memory of this run: 34279424 bytes
[2026-11-20T08:02:45Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

### 2.3 What passed before it — the live host

**`40-host-before.log`**, whole. LH1 to LH5, 5 of 5. Every L1 path is absent. The locale is printed once, as map §7
item 185 asks: `/etc/default/locale` reads `LANG="ru_UA.UTF-8"`, and the session runs under `LC_ALL=C`.

```
2026-11-20T06:22:14.184199793Z
[2026-11-20T06:22:14Z] LH1 hostname vs-2348: PASS
[2026-11-20T06:22:14Z] LH2 Ubuntu 24.04: PASS
[2026-11-20T06:22:14Z] LH3 Python 3.12: PASS
[2026-11-20T06:22:14Z] LH4 not the capture host: PASS
[2026-11-20T06:22:14Z] LH5 the host key pinned at TZ-47's first connection: PASS
[2026-11-20T06:22:14Z] LIVE HOST GATE PASS: 5 of 5
[2026-11-20T06:22:14Z] MemAvailable read 1: 1475223552 bytes, floor 85051706
[2026-11-20T06:22:14Z] available on /: 16986615808 bytes, floor 2447483648
[2026-11-20T06:22:14Z] HOST before: kernel 6.8.0-138-generic; Python 3.12.3; Ubuntu 24.04.5 LTS; MemTotal 1944465408 MemAvailable 1475223552 SwapTotal 1073737728 SwapFree 1073737728; / 20779339776 bytes, 16986615808 available
[2026-11-20T06:22:14Z] LOCALE /etc/default/locale: LANG="ru_UA.UTF-8"
[2026-11-20T06:22:14Z] LOCALE `locale` in this session, exit 0: LANG=ru_UA.UTF-8; LANGUAGE=; LC_CTYPE="C"; LC_NUMERIC="C"; LC_TIME="C"; LC_COLLATE="C"; LC_MONETARY="C"; LC_MESSAGES="C"; LC_PAPER="C"; LC_NAME="C"; LC_ADDRESS="C"; LC_TELEPHONE="C"; LC_MEASUREMENT="C"; LC_IDENTIFICATION="C"; LC_ALL=C
[2026-11-20T06:22:14Z] CLOCK exit 0: NTP=yes; NTPSynchronized=yes; TimeUSec=Fri 2026-11-20 06:22:14 UTC
[2026-11-20T06:22:14Z] SSHD authorized keys of root: [('ssh-ed25519', 'SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo')]; the Executor's among them: True
[2026-11-20T06:22:14Z] PATH /etc/l1-bot: absent
[2026-11-20T06:22:14Z] PATH /etc/l1-bot/session-key: absent
[2026-11-20T06:22:14Z] PATH /etc/l1-bot/relayer-key: absent
[2026-11-20T06:22:14Z] PATH /etc/l1-bot/telegram-token: absent
[2026-11-20T06:22:14Z] PATH /etc/l1-bot/chat-id: absent
[2026-11-20T06:22:14Z] PATH /var/lib/l1-bot: absent
[2026-11-20T06:22:14Z] PATH /var/lib/l1-bot/account.json: absent
[2026-11-20T06:22:14Z] PATH /root/l1-env: absent
[2026-11-20T06:22:14Z] PATH /root/tz50-work/wheels: absent
[2026-11-20T06:22:14Z] peak memory of this run: 34287616 bytes
[2026-11-20T06:22:14Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**`41-geoblock.log`**, whole — **G-GEO PASS** at the first read, before any key of a venue existed:

```
2026-11-20T06:22:21.460209644Z
[2026-11-20T06:22:21Z] MemAvailable read 1: 1472978944 bytes, floor 85051706
[2026-11-20T06:22:21Z] available on /: 16986595328 bytes, floor 2447483648
[2026-11-20T06:22:21Z] G-GEO read 1 over IPv4: status 200, 68 bytes, blocked False, country 'BG', region '22', keys ['blocked', 'country', 'ip', 'region']; the address the venue saw is the connection's own: True -> PASS
[2026-11-20T06:22:21Z] G-GEO PASS
[2026-11-20T06:22:21Z] peak memory of this run: 37036032 bytes
[2026-11-20T06:22:21Z] refused by the hook: 0; lookups 1, requests 1
exit=0
```

**`42-sshd.log`** and **`08-methods.log`**, whole — **G-SSH K1 to K5 and K6, 6 of 6**:

```
2026-11-20T06:22:31.815606625Z
[2026-11-20T06:22:31Z] K1 TZ-49's sshd drop-in, byte for byte: PASS
[2026-11-20T06:22:31Z] K2 passwordauthentication no: PASS
[2026-11-20T06:22:31Z] K3 kbdinteractiveauthentication no: PASS
[2026-11-20T06:22:31Z] K4 permitrootlogin without-password: PASS
[2026-11-20T06:22:31Z] K5 pubkeyauthentication yes: PASS
[2026-11-20T06:22:31Z] G-SSH K1 to K5 PASS: 5 of 5
[2026-11-20T06:22:31Z] peak memory of this run: 34287616 bytes
[2026-11-20T06:22:31Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-20T06:22:32.000629951Z
[2026-11-20T06:22:32Z] METHODS gate: the methods the live host's sshd offers root, from outside: ['publickey']; ssh exit 255
[2026-11-20T06:22:32Z] G-SSH K6 publickey alone, from outside: PASS
[2026-11-20T06:22:32Z] peak memory of this run: 34095104 bytes
[2026-11-20T06:22:32Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**The self-test on the live host** — `50-selftest.log`, its last lines (193 lines in all, §2.6):

```
[2026-11-20T06:23:26Z] ok   the temporary tree removed
[2026-11-20T06:23:26Z] SELFTEST PASS: 135 checks, 135 passed; refused by the hook: 5, each a check's own
[2026-11-20T06:23:26Z] peak memory of this run: 35074048 bytes
[2026-11-20T06:23:26Z] refused by the hook: 5; lookups 0, requests 18
exit=0
```

**G-ENV.** `51-wheels.log`'s summary lines: 35 `WHEEL downloaded` lines, each at the set's size and SHA-256, then:

```
[2026-11-20T06:24:06Z] WHEEL downloaded pip-24.0-py3-none-any.whl                                          2110226 ba0d021a166865d2265246961bec0152ff124de910c5cc39f1156ce3fa7c69dc
[2026-11-20T06:24:06Z] WHEELS requirements.txt: 34 lines, 3266 bytes, sha256 2020f3842a8cb276d7326e3ec2f60424266da0f53ba0056210e338268913b65c
[2026-11-20T06:24:06Z] G-ENV wheels PASS: 35 of 35, 14422773 bytes in all
[2026-11-20T06:24:06Z] peak memory of this run: 42151936 bytes
[2026-11-20T06:24:06Z] refused by the hook: 0; lookups 35, requests 35
exit=0
```

`52-B-ENV.log`, whole — B-ENV, run by the Executor: `exit=0`, `du` `55492611` against `200,000,000`:

```
2026-11-20T06:24:37.196667285Z
Looking in links: /root/tz50-work/wheels
Processing ./wheels/annotated_types-0.8.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 1))
Processing ./wheels/anyio-4.16.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 2))
Processing ./wheels/bitarray-3.12.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (from -r /root/tz50-work/wheels/requirements.txt (line 3))
Processing ./wheels/certifi-2026.10.23-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 4))
Processing ./wheels/ckzg-2.1.8-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (from -r /root/tz50-work/wheels/requirements.txt (line 5))
Processing ./wheels/cytoolz-1.2.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (from -r /root/tz50-work/wheels/requirements.txt (line 6))
Processing ./wheels/eth_abi-5.2.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 7))
Processing ./wheels/eth_account-0.13.7-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 8))
Processing ./wheels/eth_hash-0.8.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 9))
Processing ./wheels/eth_keyfile-0.8.1-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 10))
Processing ./wheels/eth_keys-0.8.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 11))
Processing ./wheels/eth_rlp-3.0.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 12))
Processing ./wheels/eth_typing-6.0.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 13))
Processing ./wheels/eth_utils-5.3.1-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 14))
Processing ./wheels/h11-0.16.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 15))
Processing ./wheels/h2-4.4.1-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 16))
Processing ./wheels/hexbytes-2.0.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 17))
Processing ./wheels/hpack-4.2.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 18))
Processing ./wheels/httpcore-1.0.9-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 19))
Processing ./wheels/httpx-0.28.1-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 20))
Processing ./wheels/hyperframe-6.1.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 21))
Processing ./wheels/idna-3.20-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 22))
Processing ./wheels/msgpack-1.2.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (from -r /root/tz50-work/wheels/requirements.txt (line 23))
Processing ./wheels/parsimonious-0.10.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 24))
Processing ./wheels/polymarket_client-0.20.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 25))
Processing ./wheels/pycryptodome-3.24.1-cp37-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (from -r /root/tz50-work/wheels/requirements.txt (line 26))
Processing ./wheels/pydantic_core-2.50.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (from -r /root/tz50-work/wheels/requirements.txt (line 27))
Processing ./wheels/pydantic-2.14.3-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 28))
Processing ./wheels/regex-2026.11.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (from -r /root/tz50-work/wheels/requirements.txt (line 29))
Processing ./wheels/rlp-5.0.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 30))
Processing ./wheels/toolz-1.2.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 31))
Processing ./wheels/typing_extensions-4.16.0-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 32))
Processing ./wheels/typing_inspection-0.4.5-py3-none-any.whl (from -r /root/tz50-work/wheels/requirements.txt (line 33))
Processing ./wheels/websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (from -r /root/tz50-work/wheels/requirements.txt (line 34))
Installing collected packages: parsimonious, ckzg, websockets, typing-inspection, typing-extensions, toolz, rlp, regex, pydantic-core, pydantic, pycryptodome, polymarket-client, msgpack, idna, hyperframe, httpx, httpcore, hpack, hexbytes, h2, h11, eth-utils, eth-typing, eth-rlp, eth-keys, eth-keyfile, eth-hash, eth-account, eth-abi, cytoolz, certifi, bitarray, anyio, annotated-types
Successfully installed annotated-types-0.8.0 anyio-4.16.0 bitarray-3.12.3 certifi-2026.10.23 ckzg-2.1.8 cytoolz-1.2.0 eth-abi-5.2.0 eth-account-0.13.7 eth-hash-0.8.0 eth-keyfile-0.8.1 eth-keys-0.8.0 eth-rlp-3.0.0 eth-typing-6.0.0 eth-utils-5.3.1 h11-0.16.0 h2-4.4.1 hexbytes-2.0.0 hpack-4.2.0 httpcore-1.0.9 httpx-0.28.1 hyperframe-6.1.0 idna-3.20 msgpack-1.2.4 parsimonious-0.10.0 polymarket-client-0.20.0 pycryptodome-3.24.1 pydantic-2.14.3 pydantic-core-2.50.4 regex-2026.11.9 rlp-5.0.0 toolz-1.2.0 typing-extensions-4.16.0 typing-inspection-0.4.5 websockets-15.0.1
exit=0
55492611	/root/l1-env
lrwxrwxrwx 1 root root 7 Nov 20 06:24 /root/l1-env/bin/python -> python3
```

`53-env.log`, whole — **G-ENV installed PASS**:

```
2026-11-20T06:24:49.129810463Z
[2026-11-20T06:24:50Z] ENV interpreter 3.12.3, prefix /root/l1-env: PASS
[2026-11-20T06:24:50Z] ENV distributions: 34 installed, 34 pinned; missing [], extra [], another version []
[2026-11-20T06:24:50Z] ENV the client polymarket-client 0.20.0; session keys 15534000 s, a batch 600 s; selectors {'authorize': '24017fae', 'revoke': 'e63f952f'}; hosts https://clob.polymarket.com, https://relayer-v2.polymarket.com, https://gamma-api.polymarket.com
[2026-11-20T06:24:50Z] G-ENV installed PASS
[2026-11-20T06:24:50Z] peak memory of this run: 75837440 bytes
[2026-11-20T06:24:50Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

`54-sdk-selftest.log`, its last lines (105 lines in all, §2.6) — **31 of 31**, `refused by the hook: 2`, every one of
228 requests with this TZ's agent:

```
[2026-11-20T06:25:09Z] ok   authorize: the relayer's FAILED raises TransactionFailedError
[2026-11-20T06:25:09Z] ok   every one of 228 requests carried the agent btc-5m-twap-tz50
[2026-11-20T06:25:10Z] SDK SELFTEST PASS: 31 checks, 31 passed; refused by the hook: 2, each a check's own
[2026-11-20T06:25:10Z] peak memory of this run: 96661504 bytes
[2026-11-20T06:25:10Z] refused by the hook: 2; lookups 0, requests 58
exit=0
```

**G-PAGE.** `35-pages.log`, whole. Pages read not found. The Executor turned it on once, by `gh api -X POST`, at
06:24:19 UTC, `source` `main` and `/docs`.

```
2026-11-20T06:24:08.529087701Z
{"message":"Not Found","documentation_url":"https://docs.github.com/rest/pages/pages#get-a-apiname-pages-site","status":"404"}gh: Not Found (HTTP 404)
exit=1
2026-11-20T06:24:19.922254801Z
{"html_url":"https://seahomebatumi-ai.github.io/btc-5m-twap/","source":{"branch":"main","path":"/docs"},"status":null}
exit=0
```

`55-page.log`, whole — **G-PAGE PASS** at its second read. The first read, 18 s after Pages was turned on, met
GitHub's own `404` page.

```
2026-11-20T06:24:37.185746248Z
[2026-11-20T06:24:37Z] MemAvailable read 1: 1466241024 bytes, floor 85051706
[2026-11-20T06:24:37Z] available on /: 16972021760 bytes, floor 2447483648
[2026-11-20T06:24:37Z] G-PAGE read 1: status 404, content-type 'text/html; charset=utf-8', 9115 bytes, sha256 70d613e3acfba24fd2876fcbacaf639e1e111ef4d54baf70761c47673f37d6a3: not this TZ's page
[2026-11-20T06:25:07Z] G-PAGE read 2: status 200, content-type 'text/html; charset=utf-8', 11846 bytes, sha256 f1d92e7dd8a8cd15b7b96b86b357ebf80db4e10844b3fc269e92cef0aecba528: equal
[2026-11-20T06:25:07Z] G-PAGE PASS: https://seahomebatumi-ai.github.io/btc-5m-twap/l1-sign.html
[2026-11-20T06:25:07Z] peak memory of this run: 36777984 bytes
[2026-11-20T06:25:07Z] refused by the hook: 0; lookups 2, requests 2
exit=0
```

**G-KEY** — `56-key.log`, whole:

```
2026-11-20T06:25:24.679113715Z
[2026-11-20T06:25:24Z] MemAvailable read 1: 1474002944 bytes, floor 275045368
[2026-11-20T06:25:24Z] available on /: 16909803520 bytes, floor 2447483648
[2026-11-20T06:25:25Z] G-KEY /etc/l1-bot/session-key: made; file mode 0600 uid 0 bytes 67; read back and its address re-derived equal; address withheld
[2026-11-20T06:25:25Z] peak memory of this run: 75948032 bytes
[2026-11-20T06:25:25Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

### 2.4 What passed before it — the capture host and the branch

**§0.0** — `00-ready.log`, whole. The session's own read at 06:20:49 printed
`ready=1: 10455166976 bytes free on /var/lib, 7795535636 needed; MemAvailable 259735552, 85051706 needed; at 1795155649 2026-11-20T06:20:49Z`.
`mkdir` then read `exit=0`.

```
ready=1: 10455048192 bytes free on /var/lib, 7795535636 needed; MemAvailable 249425920, 85051706 needed; at 1795155663 2026-11-20T06:21:03Z
```

**§0.1** — `01-stage.log`, whole: both files `created` at §0.1's lines, bytes and SHA-256.

```
/root/tz50-work/stage/docs/l1-sign.html 218 11846 f1d92e7dd8a8cd15b7b96b86b357ebf80db4e10844b3fc269e92cef0aecba528 created
/root/tz50-work/stage/research/tz50-l1-account.py 3091 174674 6943b54d5fb7824b9dbd467b53f8f7568ecb9851ff707399c9fe759a584617a4 created
exit=0
```

**§0.3** — `03-host-gate.log`, whole. **H1** prints one path. **H2** reads `/dev/vda2`, `31612203008`, and `grep -c`
`4`. **H3** reads `3.12.3`. **H4** prints three paths. **Memory** reads `281980928` at the first read. **Disk**
reads `10454667264`. **7 of 7.**

```
Fri Nov 20 06:21:18 AM UTC 2026
1795155678
2026-08-02 07:24:32
1
MemTotal:         978640 kB
MemAvailable:     262812 kB
SwapTotal:       3174396 kB
SwapFree:        2567196 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10454667264
/var/lib/btc-recorder/btc-updown-5m/1794396600/manifest.json
4
3.12.3
/usr/bin/ssh
/usr/bin/scp
/usr/bin/gh
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
447566349	/var/lib/btc-rewardbook
356770308	/root/btc-forensics
24704103	/root/.claude-8j
2627
disabled
exit=1
inactive
exit=3
/root/tz49-work exit=1
/root/.ssh/live-host exit=0
/root/btc-5m-twap       a9a6c82 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/fd493377-65e0-5920-8de8-844ba541b830/scratchpad
total 32
drwx------  8 root root 4096 Nov 20 06:18 .
drwx------ 40 root root 4096 Nov 20 06:18 ..
drwx------  3 root root 4096 Nov 20 06:18 3aceaaa9-a0d9-43c5-8e74-334a8c19adf5
drwx------  4 root root 4096 Nov 19 13:53 51f223d3-deb1-5de5-80aa-0eb16a447b53
drwx------  3 root root 4096 Nov 19 13:53 6ce33308-8331-4563-bb79-d8486968f8ad
drwx------  3 root root 4096 Nov 15 10:28 95cf58d2-1ec6-4c73-a622-38d04665f5ae
drwx------  4 root root 4096 Nov 17 14:14 ccca2df8-e51d-56bc-8205-06299775095a
drwx------  4 root root 4096 Nov 20 06:18 fd493377-65e0-5920-8de8-844ba541b830
MemAvailable read 1 06:21:18: 281980928
```

**§0.3's room** — `04-room.log`, whole. The archive read `inactive` at the first read. **The margin is
`2,797,417,277` bytes**, above `1,000,000,000`, so it is not flagged.

```
2026-11-20T06:21:25.473054686Z
[2026-11-20T06:21:25Z] btc-rewardbook-archive.service read 1: inactive
[2026-11-20T06:21:25Z] MemAvailable read 1: 254930944 bytes, floor 85051706
[2026-11-20T06:21:25Z] available on /var/lib: 10454573056 bytes, floor 7795535636
[2026-11-20T06:21:25Z] ROOM: 10454573056 bytes available on /var/lib; the reward book's stream files 88379857 bytes in 9 files under 24 day directories; the room 10542952913; its margin over STREAM_FLOOR 7300000000 and PEAK 445535636: 2797417277 bytes
[2026-11-20T06:21:25Z] peak memory of this run: 34095104 bytes
[2026-11-20T06:21:25Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**§0.5** — `05-number.log` and `05-refs.log`, whole. `10-number.log` read `NUMBER PASS - 2 of 2` again after the fetch,
and `13-push.log`'s `refs` read the same 189 lines before the push.

```
2026-11-20T06:21:39.777074668Z
[2026-11-20T06:21:39Z] origin/main a9a6c824daf117ab6b64dcee1b62d7c873f17c12: 119 paths under CryptoTZ/ and CryptoReports/; of the number TZ-50-: ['CryptoTZ/TZ-50-l1-account-round-trip.md'] and []
[2026-11-20T06:21:39Z] NUMBER PASS - 2 of 2
[2026-11-20T06:21:39Z] peak memory of this run: 34095104 bytes
[2026-11-20T06:21:39Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-20T06:21:39.904148788Z
[2026-11-20T06:21:40Z] REF a9a6c824daf117ab6b64dcee1b62d7c873f17c12	HEAD
[2026-11-20T06:21:40Z] REF a9a6c824daf117ab6b64dcee1b62d7c873f17c12	refs/heads/main
[2026-11-20T06:21:40Z] REFS HEAD                                     1
[2026-11-20T06:21:40Z] REFS refs/heads/main                          1
[2026-11-20T06:21:40Z] REFS refs/heads/tz-*                          23
[2026-11-20T06:21:40Z] REFS refs/pull/*/head                         46
[2026-11-20T06:21:40Z] REFS refs/tags/pairbook-streams-*             59
[2026-11-20T06:21:40Z] REFS refs/tags/rewardbook-streams-*           53
[2026-11-20T06:21:40Z] REFS refs/tags/tz-01a-dataset                 1
[2026-11-20T06:21:40Z] REFS refs/tags/tz-01a-dataset^{}              1
[2026-11-20T06:21:40Z] REFS refs/tags/tz-27-pairbook-streams         1
[2026-11-20T06:21:40Z] REFS refs/tags/tz-27-pairbook-streams^{}      1
[2026-11-20T06:21:40Z] REFS refs/tags/tz-44-l0-inputs                1
[2026-11-20T06:21:40Z] REFS refs/tags/tz-45-l0-rule-w-inputs         1
[2026-11-20T06:21:40Z] REFS 189 lines; refs/heads/tz-50-l1-account-round-trip absent
[2026-11-20T06:21:40Z] peak memory of this run: 34099200 bytes
[2026-11-20T06:21:40Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

**§0.6** — `06-access.log` and `07-copy.log`, whole. `R true` read `exit=0` at its first read. TZ-47's pinned key
`SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw` is the alias's. `vs-2348`, `root`, and both trees absent. The
live host's copy is at §0.1's SHA-256. The alias's `hostname` line is left out of the `ssh -G` read.

```
2026-11-20T06:21:48.133063346Z
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
tz49 tree exit=1
```

```
2026-11-20T06:21:59.123252005Z
exit=0
scp exit=0
6943b54d5fb7824b9dbd467b53f8f7568ecb9851ff707399c9fe759a584617a4  /root/tz50-work/tz50-l1-account.py
  3091 174674 /root/tz50-work/tz50-l1-account.py
```

**§3.1** — `11-worktree.log`, `13-push.log` and `14-pr.log`, whole. The instrument is `created` and the page `equal,
kept`. The commit on `origin` is the worktree's `HEAD`, and the diff is `3091 0`, one path. The push went through the
URL's own credential.

```
2026-11-20T06:22:39.443522367Z
Preparing worktree (new branch 'tz-50-l1-account-round-trip')
branch 'tz-50-l1-account-round-trip' set up to track 'origin/main'.
HEAD is now at a9a6c82 Create l1-sign.html
worktree exit=0
/root/tz50-work/wt/docs/l1-sign.html 218 11846 f1d92e7dd8a8cd15b7b96b86b357ebf80db4e10844b3fc269e92cef0aecba528 equal, kept
/root/tz50-work/wt/research/tz50-l1-account.py 3091 174674 6943b54d5fb7824b9dbd467b53f8f7568ecb9851ff707399c9fe759a584617a4 created
exit=0
```

```
2026-11-20T06:22:57.962720032Z
[2026-11-20T06:22:58Z] REF a9a6c824daf117ab6b64dcee1b62d7c873f17c12	HEAD
[2026-11-20T06:22:58Z] REF a9a6c824daf117ab6b64dcee1b62d7c873f17c12	refs/heads/main
[2026-11-20T06:22:58Z] REFS HEAD                                     1
[2026-11-20T06:22:58Z] REFS refs/heads/main                          1
[2026-11-20T06:22:58Z] REFS refs/heads/tz-*                          23
[2026-11-20T06:22:58Z] REFS refs/pull/*/head                         46
[2026-11-20T06:22:58Z] REFS refs/tags/pairbook-streams-*             59
[2026-11-20T06:22:58Z] REFS refs/tags/rewardbook-streams-*           53
[2026-11-20T06:22:58Z] REFS refs/tags/tz-01a-dataset                 1
[2026-11-20T06:22:58Z] REFS refs/tags/tz-01a-dataset^{}              1
[2026-11-20T06:22:58Z] REFS refs/tags/tz-27-pairbook-streams         1
[2026-11-20T06:22:58Z] REFS refs/tags/tz-27-pairbook-streams^{}      1
[2026-11-20T06:22:58Z] REFS refs/tags/tz-44-l0-inputs                1
[2026-11-20T06:22:58Z] REFS refs/tags/tz-45-l0-rule-w-inputs         1
[2026-11-20T06:22:58Z] REFS 189 lines; refs/heads/tz-50-l1-account-round-trip absent
[2026-11-20T06:22:58Z] peak memory of this run: 34099200 bytes
[2026-11-20T06:22:58Z] refused by the hook: 0; lookups 0, requests 0
exit=0
commit exit=0
remote: 
remote: Create a pull request for 'tz-50-l1-account-round-trip' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-50-l1-account-round-trip        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-50-l1-account-round-trip -> tz-50-l1-account-round-trip
branch 'tz-50-l1-account-round-trip' set up to track 'origin/tz-50-l1-account-round-trip'.
push exit=0
2026-11-20T06:23:00.102039984Z
0774d7eefec63d7037d7f18487f0ba46919f9a1b	refs/heads/tz-50-l1-account-round-trip
0774d7eefec63d7037d7f18487f0ba46919f9a1b
3091	0	research/tz50-l1-account.py
```

```
2026-11-20T06:23:11.156373080Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/48
exit=0
```

**§3.2** — `20-selftest.log`, its last lines (193 lines in all):

```
[2026-11-20T06:23:18Z] ok   the temporary tree removed
[2026-11-20T06:23:18Z] SELFTEST PASS: 135 checks, 135 passed; refused by the hook: 5, each a check's own
[2026-11-20T06:23:18Z] peak memory of this run: 35012608 bytes
[2026-11-20T06:23:18Z] refused by the hook: 5; lookups 0, requests 18
exit=0
```

**§3.3** — `30-scratch.log` and `32-reclaim-scratch.log`, whole. TZ-49's pair read **earlier**. `3aceaaa9-…`, born
with this session's spawning process, and `95cf58d2-…` and `ccca2df8-…`, born with the remote-control processes,
read **live** and were not touched. B-RECLAIM-SCRATCH was run by the Executor: `RECLAIM PASS`, then one `rm -rf` and
one `test -e` for each directory, each `test -e` reading `exit=1`.

```
2026-11-20T06:23:32.564614668Z
[2026-11-20T06:23:32Z] running 1738600 started 2026-11-15T10:28:51Z claude
[2026-11-20T06:23:32Z] running 1738611 started 2026-11-15T10:28:53Z claude
[2026-11-20T06:23:32Z] running 1738619 started 2026-11-15T10:28:53Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-20T06:23:32Z] running 2491506 started 2026-11-20T06:18:22Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-20T06:23:32Z] 3aceaaa9-a0d9-43c5-8e74-334a8c19adf5 born 2026-11-20T06:18:23Z: live, process [2491506]
[2026-11-20T06:23:32Z] 51f223d3-deb1-5de5-80aa-0eb16a447b53 born 2026-11-19T13:53:25Z: earlier
[2026-11-20T06:23:32Z] 6ce33308-8331-4563-bb79-d8486968f8ad born 2026-11-19T13:53:23Z: earlier
[2026-11-20T06:23:32Z] 95cf58d2-1ec6-4c73-a622-38d04665f5ae born 2026-11-15T10:28:56Z: live, process [1738600, 1738611, 1738619]
[2026-11-20T06:23:32Z] ccca2df8-e51d-56bc-8205-06299775095a born 2026-11-15T10:28:57Z: live, process [1738600, 1738611, 1738619]
[2026-11-20T06:23:32Z] peak memory of this run: 34099200 bytes
[2026-11-20T06:23:32Z] refused by the hook: 0; lookups 0, requests 0
exit=0
```

```
2026-11-20T06:23:44.899938949Z
[2026-11-20T06:23:45Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/51f223d3-deb1-5de5-80aa-0eb16a447b53, an earlier session's directory of 1 files: nothing of it is kept
[2026-11-20T06:23:45Z] reclaim: /tmp/claude-0/-root-btc-5m-twap/6ce33308-8331-4563-bb79-d8486968f8ad, an earlier session's directory of 0 files: nothing of it is kept
[2026-11-20T06:23:45Z] RECLAIM PASS: 0 files considered, 0 copied, 0 already held; the forensic store 2627 -> 2627 files
[2026-11-20T06:23:45Z] peak memory of this run: 33968128 bytes
[2026-11-20T06:23:45Z] refused by the hook: 0; lookups 0, requests 0
exit=0
2026-11-20T06:23:58.244250187Z
exit=0
exit=1
2026-11-20T06:23:58.281937417Z
exit=0
exit=1
```

### 2.5 After the BLOCK — §3.10's copy, the closing reads and §9

**§3.10's copy and G-PRINT** — `80-live-copy.log`, whole. `scp exit=0` and `diff exit=0`, so every log of the live host
is on the capture host, byte for byte. **G-PRINT is `0` and `0`:** no line of any log of either host holds an `0x`
address of forty hex digits or a bot token's form, and no file holds the live host's address.

```
2026-11-20T08:02:53.397130672Z
scp exit=0
diff exit=0
total 88
drwxr-xr-x 2 root root  4096 Nov 20 08:02 .
drwxr-xr-x 6 root root  4096 Nov 20 08:02 ..
-rw-r--r-- 1 root root  2018 Nov 20 08:02 40-host-before.log
-rw-r--r-- 1 root root   576 Nov 20 08:02 41-geoblock.log
-rw-r--r-- 1 root root   533 Nov 20 08:02 42-sshd.log
-rw-r--r-- 1 root root 17953 Nov 20 08:02 50-selftest.log
-rw-r--r-- 1 root root  6840 Nov 20 08:02 51-wheels.log
-rw-r--r-- 1 root root  5447 Nov 20 08:02 52-B-ENV.log
-rw-r--r-- 1 root root   661 Nov 20 08:02 53-env.log
-rw-r--r-- 1 root root 12261 Nov 20 08:02 54-sdk-selftest.log
-rw-r--r-- 1 root root   796 Nov 20 08:02 55-page.log
-rw-r--r-- 1 root root   475 Nov 20 08:02 56-key.log
-rw-r--r-- 1 root root  1926 Nov 20 08:02 70-B-OWNER.log
-rw-r--r-- 1 root root  2112 Nov 20 08:02 79-host-after.log
0
0
```

**The closing reads** — `90-closing.log`, whole. The capture host's units read as at §0.3: the same `MainPID`,
`NRestarts` and `ActiveState`. On the live host `sshd -T` reads root by key alone, `/root/l1-env` is `55,492,611`
bytes with the client at `0.20.0`, and `/var/lib/l1-bot` is absent.

```
2026-11-20T08:03:08.093472803Z
Fri Nov 20 08:03:08 UTC 2026
               total        used        free      shared  buff/cache   available
Mem:      1944465408   451698688   828076032     1470464   838332416  1492766720
Swap:     1073737728           0  1073737728
Filesystem             1B-blocks       Avail
/dev/mapper/lvm-root 20779339776 16909737984
active
ls: /etc/l1-bot:
total 12
drwx------   2 root root 4096 Nov 20 06:25 .
drwxr-xr-x 107 root root 4096 Nov 20 06:25 ..
-rw-------   1 root root   67 Nov 20 06:25 session-key
cannot access '/var/lib/l1-bot': No such file or directory
/etc/l1-bot/session-key 67 600 root
stat: cannot statx '/var/lib/l1-bot/*'55492611	/root/l1-env
: No such file or directory
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
/dev/vda2      31612203008 10477932544
17220568	/root/tz50-work
404065191	/var/lib/btc-rewardbook
               total        used        free      shared  buff/cache   available
Mem:      1002127360   752271360    74268672       73728   361422848   249856000
Swap:     3250581504   709054464  2541527040
0774d7eefec63d7037d7f18487f0ba46919f9a1b	refs/heads/tz-50-l1-account-round-trip
```

**Contract §4.2's self-check** — `99-selfcheck.log`, whole, `C` = `0774d7eefec63d7037d7f18487f0ba46919f9a1b`. It read
`0`, the one path, `3091 0`, and no `.parquet` or `.zip` on `main` (`grep exit=1`).

```
2026-11-20T08:03:09.362084609Z
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new tag]         rewardbook-streams-1795159820 -> rewardbook-streams-1795159820
0
research/tz50-l1-account.py
3091	0	research/tz50-l1-account.py
grep exit=1
```

**§9, B-RECLAIM-LIVE**, run by the Executor, its instant read in the same call:

```
$ date -u +%FT%T.%NZ; ssh -T -o BatchMode=yes -o ConnectTimeout=20 -o LogLevel=QUIET live-host 'export LC_ALL=C; rm -rf /root/tz50-work; test -e /root/tz50-work; echo "exit=$?"'
2026-11-20T08:03:16.534146574Z
exit=1
```

**§9, B-RECLAIM-OWN.** Its output was written to no file and is quoted from the session, every line:

```
$ (cd /root/tz50-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz50-work/wt/research/tz50-l1-account.py reclaim /root/tz50-work); echo "reclaim exit=$?"
[2026-11-20T08:06:12Z] reclaim: /root/tz50-work/wt skipped: no file but its HEAD's, and HEAD 0774d7eefec63d7037d7f18487f0ba46919f9a1b is its upstream's
[2026-11-20T08:06:12Z] R copied 179fa6513203411a7fd56637f97c6baa517c803d229248e52e62c8196094af82 /root/btc-forensics/tz50-work--live-logs--40-host-before.log
[2026-11-20T08:06:12Z] R copied 4bcdd9f2a2b1b92f7ceda3f85ff383d5044c59965bcb047cd32f6559b613b3f2 /root/btc-forensics/tz50-work--live-logs--41-geoblock.log
[2026-11-20T08:06:12Z] R copied 5efc137a4857f77740fb3aab937700e442dac59864927da6f283c6a0becebf03 /root/btc-forensics/tz50-work--live-logs--42-sshd.log
[2026-11-20T08:06:12Z] R copied 1164de8d88a6d330cbb08310efa722682996d6ecfc5c4a6f4a5ae6c6ecd5c736 /root/btc-forensics/tz50-work--live-logs--50-selftest.log
[2026-11-20T08:06:12Z] R copied bbba6ebc37330d7488404a9288a15d4637de42844bbda4e8085b649ea6e7820d /root/btc-forensics/tz50-work--live-logs--51-wheels.log
[2026-11-20T08:06:12Z] R copied 294c11a6ba6d2a7495f4c9327e5626f9b60f0c20587bf51ed75c688d99433d9c /root/btc-forensics/tz50-work--live-logs--52-B-ENV.log
[2026-11-20T08:06:12Z] R copied 6b3e28005829873cfc08c1203df174d6cca31ca03d607477c6703b3d2de94ad8 /root/btc-forensics/tz50-work--live-logs--53-env.log
[2026-11-20T08:06:12Z] R copied 52e8c41cc522aeae76a075a57114994ac8ae87f1b212015480550fe81f19fb4b /root/btc-forensics/tz50-work--live-logs--54-sdk-selftest.log
[2026-11-20T08:06:12Z] R copied ff78db0ce95f65a214f12ed5115a5c809182c788d3dd53c54a67916123669bd9 /root/btc-forensics/tz50-work--live-logs--55-page.log
[2026-11-20T08:06:12Z] R copied e0ce69a96f0b841bdf48351704938b27e0096e42f474cd9362ef73e615d03381 /root/btc-forensics/tz50-work--live-logs--56-key.log
[2026-11-20T08:06:12Z] R copied be0c6e633dbd2c83f71202c99a84902d9139befba02858a5c33e449a913b430a /root/btc-forensics/tz50-work--live-logs--70-B-OWNER.log
[2026-11-20T08:06:12Z] R copied e695f43c855b3df5cdf90c76da8a8012831196164c702dc7b9de880a11285bcd /root/btc-forensics/tz50-work--live-logs--79-host-after.log
[2026-11-20T08:06:12Z] R copied d18e0404698889ef02bc3f6a1dacb7a68115d727a932c81776fcc117358fe540 /root/btc-forensics/tz50-work--logs--00-ready.log
[2026-11-20T08:06:12Z] R copied 2ff596543acd24c6cf9f94937026ab4b32f4f08db933a9b543c25f56494aba34 /root/btc-forensics/tz50-work--logs--01-stage.log
[2026-11-20T08:06:12Z] R copied 484b1011ad8fa732f2e47b270453adcb7c5e9988a6ca7cb508297058f634c0ae /root/btc-forensics/tz50-work--logs--02-fingerprint.log
[2026-11-20T08:06:12Z] R copied ae9a8afc170cd32c9c7178483dadaa537236b1967ac613d649a8d263050a2a18 /root/btc-forensics/tz50-work--logs--03-host-gate.log
[2026-11-20T08:06:12Z] R copied 12379d112e1c1e1857e30e3df82aa1ef30f19f736351f76318e5767c03e97a2a /root/btc-forensics/tz50-work--logs--04-room.log
[2026-11-20T08:06:12Z] R copied 67fbde3e76c8e4fb5f8d6857b86db1a29869a846ff8eafdf6c75620ed051093d /root/btc-forensics/tz50-work--logs--05-number.log
[2026-11-20T08:06:12Z] R copied c7914912dee3969d777fdc07641690c475e10a12fcfb7d925e36410267af9afc /root/btc-forensics/tz50-work--logs--05-refs.log
[2026-11-20T08:06:12Z] R copied 827ed7dbbea2de6eef5e99e541b7ea800b5bdf01c3f3efed191c90c92f778a18 /root/btc-forensics/tz50-work--logs--06-access.log
[2026-11-20T08:06:12Z] R copied edc1e5a5e57b0c1f9234e1cd63285a1714907b0ad440aa8ca2f24998cb13efdb /root/btc-forensics/tz50-work--logs--07-copy.log
[2026-11-20T08:06:12Z] R copied 2d5e12633598b7403278f4d24f29808c84204a8a514ce86709131e0c2fbc08d5 /root/btc-forensics/tz50-work--logs--08-methods.log
[2026-11-20T08:06:12Z] R copied fc8cfc7047a5c13a2cc74ae2859a68b7ecdf7ccdae6c31a1b90166fcfa1fdca3 /root/btc-forensics/tz50-work--logs--10-number.log
[2026-11-20T08:06:12Z] R copied 2cc417da5741f9f7667c8b26dfb9b03568c3ab617fc2dbc6dcfabc47e20fbe8d /root/btc-forensics/tz50-work--logs--11-worktree.log
[2026-11-20T08:06:12Z] R copied a1e773044ef5d9b152185b4a454147c30139bcdc97d986f3d086713e3cdf6b7b /root/btc-forensics/tz50-work--logs--12-fingerprint.log
[2026-11-20T08:06:12Z] R copied 8c8330c8e0ff780b62895e3d4459aba6f379e93837d7ca1432ba6b4c7c54e704 /root/btc-forensics/tz50-work--logs--13-push.log
[2026-11-20T08:06:12Z] R copied 5bd840410f9dc14f64dd861e1b884bec007a8beef4a714e9109dc95f3c2d3d08 /root/btc-forensics/tz50-work--logs--14-pr.log
[2026-11-20T08:06:12Z] R copied a6de6193a319aabf2387f7cb7985f3b788d3abcd37e80daf52f6fa9bbd686166 /root/btc-forensics/tz50-work--logs--20-selftest.log
[2026-11-20T08:06:12Z] R copied bb8d5750077210998f2fec1d57d1d27564a91c6d2879dca9ef9d06ade6adb92e /root/btc-forensics/tz50-work--logs--30-scratch.log
[2026-11-20T08:06:12Z] R copied 27a2a4df16a57f7f23bcfba4bdc21eb7cf07d3546d02ab455cbbc10443455d3e /root/btc-forensics/tz50-work--logs--32-reclaim-scratch.log
[2026-11-20T08:06:12Z] R copied e61d79110ba13481fd6430cff5039bc09cfc8477c02bef875597327d382104c2 /root/btc-forensics/tz50-work--logs--35-pages.log
[2026-11-20T08:06:12Z] R copied b458c916e25bce0889bcdb19d81e5fd23b5420b2874ee6aa80d81349e2965325 /root/btc-forensics/tz50-work--logs--37-handover.log
[2026-11-20T08:06:12Z] R copied 0af873b0ddee3eae846ce75c7c97a669f1ce2779f09057f8a23a03372ae5d0e5 /root/btc-forensics/tz50-work--logs--80-live-copy.log
[2026-11-20T08:06:12Z] R copied abe06704d56ca6b2a150c7c4c7bbb60a53e9f3ff0e742bdc6e35e088e8d3227a /root/btc-forensics/tz50-work--logs--90-closing.log
[2026-11-20T08:06:12Z] R copied badab4e31d9bab97c2f54a463672c8200da4ec5915e2764327aadc2b2db14620 /root/btc-forensics/tz50-work--logs--99-selfcheck.log
[2026-11-20T08:06:12Z] R copied f1d92e7dd8a8cd15b7b96b86b357ebf80db4e10844b3fc269e92cef0aecba528 /root/btc-forensics/tz50-work--stage--docs--l1-sign.html
[2026-11-20T08:06:12Z] R copied 6943b54d5fb7824b9dbd467b53f8f7568ecb9851ff707399c9fe759a584617a4 /root/btc-forensics/tz50-work--stage--research--tz50-l1-account.py
[2026-11-20T08:06:12Z] RECLAIM PASS: 37 files considered, 37 copied, 0 already held; the forensic store 2627 -> 2664 files
[2026-11-20T08:06:12Z] peak memory of this run: 34357248 bytes
[2026-11-20T08:06:12Z] refused by the hook: 0; lookups 0, requests 0
reclaim exit=0
$ cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz50-work/wt; echo "exit=$?"
exit=0
$ cd /root/btc-5m-twap && rm -rf /root/tz50-work; echo "exit=$?"
exit=0
$ test -e /root/tz50-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       a9a6c82 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
2664
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10492223488
```

### 2.6 The files of this run

Every regular file of `/root/tz50-work` after §3.10's copy and before B-RECLAIM-OWN, but the branch worktree's, each
hashed by the Executor's own read. `reclaim` copied each into the forensic store by exclusive create and checked its
hash (§2.5).

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `live-logs/40-host-before.log` | 26 | 2018 | `179fa6513203411a7fd56637f97c6baa517c803d229248e52e62c8196094af82` |
| `live-logs/41-geoblock.log` | 8 | 576 | `4bcdd9f2a2b1b92f7ceda3f85ff383d5044c59965bcb047cd32f6559b613b3f2` |
| `live-logs/42-sshd.log` | 10 | 533 | `5efc137a4857f77740fb3aab937700e442dac59864927da6f283c6a0becebf03` |
| `live-logs/50-selftest.log` | 193 | 17953 | `1164de8d88a6d330cbb08310efa722682996d6ecfc5c4a6f4a5ae6c6ecd5c736` |
| `live-logs/51-wheels.log` | 43 | 6840 | `bbba6ebc37330d7488404a9288a15d4637de42844bbda4e8085b649ea6e7820d` |
| `live-logs/52-B-ENV.log` | 41 | 5447 | `294c11a6ba6d2a7495f4c9327e5626f9b60f0c20587bf51ed75c688d99433d9c` |
| `live-logs/53-env.log` | 8 | 661 | `6b3e28005829873cfc08c1203df174d6cca31ca03d607477c6703b3d2de94ad8` |
| `live-logs/54-sdk-selftest.log` | 105 | 12261 | `52e8c41cc522aeae76a075a57114994ac8ae87f1b212015480550fe81f19fb4b` |
| `live-logs/55-page.log` | 9 | 796 | `ff78db0ce95f65a214f12ed5115a5c809182c788d3dd53c54a67916123669bd9` |
| `live-logs/56-key.log` | 7 | 475 | `e0ce69a96f0b841bdf48351704938b27e0096e42f474cd9362ef73e615d03381` |
| `live-logs/70-B-OWNER.log` | 40 | 1926 | `be0c6e633dbd2c83f71202c99a84902d9139befba02858a5c33e449a913b430a` |
| `live-logs/79-host-after.log` | 26 | 2112 | `e695f43c855b3df5cdf90c76da8a8012831196164c702dc7b9de880a11285bcd` |
| `logs/00-ready.log` | 1 | 140 | `d18e0404698889ef02bc3f6a1dacb7a68115d727a932c81776fcc117358fe540` |
| `logs/01-stage.log` | 3 | 265 | `2ff596543acd24c6cf9f94937026ab4b32f4f08db933a9b543c25f56494aba34` |
| `logs/02-fingerprint.log` | 78 | 13004 | `484b1011ad8fa732f2e47b270453adcb7c5e9988a6ca7cb508297058f634c0ae` |
| `logs/03-host-gate.log` | 71 | 1990 | `ae9a8afc170cd32c9c7178483dadaa537236b1967ac613d649a8d263050a2a18` |
| `logs/04-room.log` | 8 | 651 | `12379d112e1c1e1857e30e3df82aa1ef30f19f736351f76318e5767c03e97a2a` |
| `logs/05-number.log` | 6 | 410 | `67fbde3e76c8e4fb5f8d6857b86db1a29869a846ff8eafdf6c75620ed051093d` |
| `logs/05-refs.log` | 19 | 1268 | `c7914912dee3969d777fdc07641690c475e10a12fcfb7d925e36410267af9afc` |
| `logs/06-access.log` | 14 | 408 | `827ed7dbbea2de6eef5e99e541b7ea800b5bdf01c3f3efed191c90c92f778a18` |
| `logs/07-copy.log` | 5 | 199 | `edc1e5a5e57b0c1f9234e1cd63285a1714907b0ad440aa8ca2f24998cb13efdb` |
| `logs/08-methods.log` | 6 | 363 | `2d5e12633598b7403278f4d24f29808c84204a8a514ce86709131e0c2fbc08d5` |
| `logs/10-number.log` | 7 | 423 | `fc8cfc7047a5c13a2cc74ae2859a68b7ecdf7ccdae6c31a1b90166fcfa1fdca3` |
| `logs/11-worktree.log` | 8 | 483 | `2cc417da5741f9f7667c8b26dfb9b03568c3ab617fc2dbc6dcfabc47e20fbe8d` |
| `logs/12-fingerprint.log` | 78 | 13004 | `a1e773044ef5d9b152185b4a454147c30139bcdc97d986f3d086713e3cdf6b7b` |
| `logs/13-push.log` | 32 | 1926 | `8c8330c8e0ff780b62895e3d4459aba6f379e93837d7ca1432ba6b4c7c54e704` |
| `logs/14-pr.log` | 3 | 94 | `5bd840410f9dc14f64dd861e1b884bec007a8beef4a714e9109dc95f3c2d3d08` |
| `logs/20-selftest.log` | 193 | 17953 | `a6de6193a319aabf2387f7cb7985f3b788d3abcd37e80daf52f6fa9bbd686166` |
| `logs/30-scratch.log` | 13 | 1141 | `bb8d5750077210998f2fec1d57d1d27564a91c6d2879dca9ef9d06ade6adb92e` |
| `logs/32-reclaim-scratch.log` | 13 | 715 | `27a2a4df16a57f7f23bcfba4bdc21eb7cf07d3546d02ab455cbbc10443455d3e` |
| `logs/35-pages.log` | 6 | 346 | `e61d79110ba13481fd6430cff5039bc09cfc8477c02bef875597327d382104c2` |
| `logs/37-handover.log` | 33 | 1594 | `b458c916e25bce0889bcdb19d81e5fd23b5420b2874ee6aa80d81349e2965325` |
| `logs/80-live-copy.log` | 20 | 837 | `0af873b0ddee3eae846ce75c7c97a669f1ce2779f09057f8a23a03372ae5d0e5` |
| `logs/90-closing.log` | 62 | 1936 | `abe06704d56ca6b2a150c7c4c7bbb60a53e9f3ff0e742bdc6e35e088e8d3227a` |
| `logs/99-selfcheck.log` | 7 | 245 | `badab4e31d9bab97c2f54a463672c8200da4ec5915e2764327aadc2b2db14620` |
| `stage/docs/l1-sign.html` | 218 | 11846 | `f1d92e7dd8a8cd15b7b96b86b357ebf80db4e10844b3fc269e92cef0aecba528` |
| `stage/research/tz50-l1-account.py` | 3091 | 174674 | `6943b54d5fb7824b9dbd467b53f8f7568ecb9851ff707399c9fe759a584617a4` |

**Peaks.** Each standard-library mode's peak is under `42,525,853`, and each client mode's under `137,522,684` (V21,
recorded):

- On the capture host: `fingerprint` 35,147,776 and 35,016,704; `room`, `number` and `methods` 34,095,104; `refs`
  34,099,200; `selftest` 35,012,608; `scratch` 34,099,200; `reclaim` 33,968,128.
- On the live host: `host before` 34,287,616; `geoblock` 37,036,032; `sshd` 34,287,616; `selftest` 35,074,048;
  `wheels` 42,151,936; `page` 36,777,984; `secrets` 34,271,232 at each run; `host after` 34,279,424.
- The client's modes: `env` 75,837,440; `sdk-selftest` 96,661,504; `key` 75,948,032.

**Every free-space and `MemAvailable` read, with its instant and its bound.** On the capture host the bounds are
`7,795,535,636` free on `/var/lib` and `85,051,706` of memory:

| read | instant (UTC) | free on `/var/lib` | `MemAvailable` |
|---|---|---|---|
| §0.0, the session's read | 06:20:49 | `10,455,166,976` | `259,735,552` |
| §0.0, the logged read | 06:21:03 | `10,455,048,192` | `249,425,920` |
| §0.3 | 06:21:18 | `10,454,667,264` (`df`) | `281,980,928` |
| `room` | 06:21:25 | `10,454,573,056` | `254,930,944` |
| the closing reads | 08:03:08 | `10,477,932,544` (`df`) | `249,856,000` (`free -b`), no bound |

On the live host the bounds are `2,447,483,648` available on `/` and `85,051,706` of memory, or `275,045,368` for
`key`:

| mode | instant (UTC) | available on `/` | `MemAvailable` |
|---|---|---|---|
| `host before` | 06:22:14 | `16,986,615,808` | `1,475,223,552` |
| `geoblock` | 06:22:21 | `16,986,595,328` | `1,472,978,944` |
| `wheels` | 06:24:04 | `16,986,583,040` | `1,475,944,448` |
| `page` | 06:24:37 | `16,972,021,760` | `1,466,241,024` |
| `key` | 06:25:24 | `16,909,803,520` | `1,474,002,944` |
| `secrets`, first run | 07:55:10 | `16,909,746,176` | `1,455,759,360` |
| `secrets`, second run | 08:00:57 | `16,909,758,464` | `1,462,894,592` |
| `host after` | 08:02:45 | `16,909,754,368` | `1,462,820,864` |
| the closing reads | 08:03:08 | `16,909,737,984` (`df`) | `1,492,766,720` (`free -b`), no bound |

---

## 3. Departures, named

1. **The upload arrived in five commits, not one.**
   - `401a816` — `SYSTEM-MAP.md`.
   - `2781624` — this TZ.
   - `c40b6a4` — `l1-sign.html` at the repository's root.
   - `b07d7bb` — its deletion.
   - `a9a6c82` — `docs/l1-sign.html`.

   `git diff --stat 234a6e8 a9a6c82` names three files: `CryptoTZ/TZ-50-l1-account-round-trip.md`, `SYSTEM-MAP.md` and
   `docs/l1-sign.html`. No page remains at the root. The fingerprint, which reads the map, the page on `main` and the
   67 rows, passed. NUMBER passed too, so the run went on.
2. **B-OWNER was not handed a second time** (§1). §3.7 hands the same paste again with one line in Russian saying what
   to do differently. No such line exists: the failure is a fixed line of the instrument, and no action of the Boss
   changes it. A second handover would have asked him for a certain failure inside the run's 8-hour bound, so the run
   went to the BLOCK at once. The same line stops `bosskey`, `authorize`, `approve` and B-REVOKE's `revoke` (§1). **So
   §4.11's B-REVOKE cannot run either**, but nothing needs revoking: the session key was never authorized.
3. **The BLOCK path read more than "§3.10's copy, then §9", all of it read-only:**
   - `L 'host after' 79-host-after` before the copy, to name L1's paths by their state as §3 asks of a BLOCK after
     §3.6.
   - The closing reads, `90-closing.log`.
   - Contract §4.2's self-check, `99-selfcheck.log`, because a branch and a pull request exist.

   **Not run:**
   - `78-sshd-after` and `88-methods-after`: `bosskey` never ran, and nothing changed `sshd`.
   - `81-keep`: §3.10 item 3 runs only where `/var/lib/l1-bot/` exists, and it does not.
   - §3.8 and §3.9.
   - B-RESET: neither of its causes is in the log.

   No kept copy of the instrument is on the live host for B-REVOKE.
4. **The wait for B-OWNER was a background loop of the Executor's own.** It read `R 'tail -n 3 …'` every 570 s and
   wrote each read with its instant to `37-handover.log` (§2.1). It ended at the first read whose last line was
   `exit=`, which came at 08:01:21. The Boss's first run began at 07:55:10 and his second at 08:00:57, so the loop's
   one read after them shows the second run's end.
5. **`00-ready.log` and `01-stage.log`.**
   - `00-ready.log` was written with `>`, without a `date -u` line. The read prints its own instant.
   - `01-stage.log` ends with an `exit=0` line, which the Executor's `echo` added and §0.1's script does not print.
   - `11-worktree.log` carries the same `exit=` line after the script, and a `worktree exit=0` line after `git worktree
     add`.
   - `10-number.log` carries `fetch exit=0`.
6. **The refs differ from map §1's read of 2026-11-19** (186 lines), recorded and not BLOCKING, as §0.5 says. This
   run read 189:
   - `refs/pull/47/merge` is gone with PR #47's merge.
   - `rewardbook-streams-*` reads 53 against 49.
   - `HEAD` and `main` read `a9a6c82` against `96d0ec1`.

   The self-check's fetch at 08:03:09 brought one more tag, `rewardbook-streams-1795159820`, from the archive's run of
   07:30:20 UTC. That run took the reward book's store from `447,566,349` bytes (§0.3) to `404,065,191` (the closing
   reads).
7. **The Boss's message to the session carried two addresses**: his terminal pasted whole, which held the live
   host's address in `ssh`'s closing line and the capture host's last-login source address. Neither is quoted here or
   written to any log. G-PRINT counted 0 files holding the live host's address. The session's transcript holds that
   message (map §6, harness — background output).
8. **GitHub Pages stays on**, the one repository setting this run changed (§2 item 1). It was turned on by the
   Executor at 06:24:19 UTC for `main`'s `/docs`, and it serves the page at Appendix B's bytes (G-PAGE PASS). B-PAGES
   was not handed over.
9. **What stays on the live host as this TZ left it**, none of it removed by this run (§3):
   - `/root/l1-env/`.
   - `/etc/l1-bot/` with `session-key`. This key was never authorized for any wallet: no owner signed for it and no
     relayer request was made.
   - TZ-49's three drop-ins, untouched.

   `/root/tz50-work` is gone (§9). **Whether the Boss made B-ACCOUNT's steps** on polymarket.com and in Telegram — the
   allowlist, the Relayer API key, the deposit and `/start` — **is not read by this run.** Nothing of the bot's
   account was read, and nothing he would have typed reached the host.
10. **Pull request #48 stays open.** Its one file is the instrument with this defect at line 1446. Its merge, or its
    closing, is for the Architect's verdict.
11. **No block but B-ACCOUNT and B-OWNER was handed to the Boss, and the classifier refused nothing.** B-ENV,
    B-RECLAIM-SCRATCH, B-RECLAIM-LIVE and B-RECLAIM-OWN were run by the Executor.
