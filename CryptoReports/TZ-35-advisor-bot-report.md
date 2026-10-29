# TZ-35 report — the advisor's Telegram bot: ADV-3 on the Boss's Binance Futures coins, deployed as a system unit

**NUMBER PASS: 2 of 2** at §0.5 (14:23:35 UTC) and again at §3.1 (14:23:42 UTC): `CryptoTZ/` holds `TZ-35-advisor-bot.md` and no other `TZ-35-` file, `CryptoReports/` no `TZ-35-` report.
**G-SAME PASS**: 42 coins, 546 candles compared, the least 13 for one coin, 0 mismatches · **G-HISTORY PASS: 16 of 16 equal**, `history.json` 19,362 bytes, SHA-256 `bcee53097f9f1a5820b551c90054a3f046c027f53cff868b857be3118c74faa1`, the Architect's bytes (DETERMINISM).
**COPY PASS: 4 of 4** · **P-START: served - 5 of 5 endpoints** (`fapi.binance.com` klines, fundingRate, premiumIndex, fundingInfo; Telegram `getMe`, bot `@ClaudeCryptoSignal_bot`) · **PROPS PASS: 11 of 11** after B-INSTALL `exit=0`.
**G-CHAT PASS**: 1 private chat sent `/start`, pinned to `/etc/adv3-bot/chat-id` (`600 root`) · **G-HELLO PASS**: message ids `[5]`.
**B-ENABLE** — refused to the Executor by the session's permission classifier, run verbatim by the Boss at 14:38:10 UTC, `exit=0` · **G-UNIT PASS: 18 of 18** at 0 restarts · **G-DAILY PASS: 8 of 8** · **G-REPLY PASS: 1 of 1** · **G-LOAD PASS: 2 of 2**, 0.99 s of processor over 311.0 s, `0.003` of the core against `0.05`.
**G-RESTART PASS: 5 of 5** (pid 3290952 → 3291955, started 35.27 s after the `kill` mark) · **G-ONCE PASS: 2 of 2** · **G-UNIT PASS: 18 of 18** at 1 restart · **G-STILL PASS: 3 of 3**, the recorder (2388318, `NRestarts` 0), the pair book (3216422, 12) and the reward book (3137952, 1) unchanged from 14:23:21 to 14:56:47 UTC, the pair book's archive's ledger 31 → 31 restart records.
**The bot runs**: `adv3-bot.service` `active`, `running`, `enabled`, pid 3291955, `NRestarts` 1, verified by the checker's `unit 1` and by §3.12's `systemctl show`, `is-enabled` and `journalctl`, never from the Boss's account. K-35 and B-UNINSTALL were not run. Its first daily went to the Boss at 14:38 UTC for the close of 2026-10-28: TOP-3 XMR LONG ★ STRONG, BTW LONG, GRAM SHORT.
**ADV-2 is retired on the branch**: `ADVISOR-SKILL.md` and `.github/workflows/adv2-signal.yml` removed beside the six added files, so the merge of pull request #35 stops ADV-2's daily comment.
**Departures, all in §6**: H6 failed at the first host gate — `/etc/adv3-bot` did not exist — the Boss then did §0.6's steps and the host gate was read again, `12 of 12`; B-ENABLE handed to the Boss after the classifier's refusal, its `start` mark 2 min 41 s before his run; the Executor's log names and timing wrappers.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-35-advisor-bot.md`, 3,057 lines, 191,719 bytes, SHA-256 `76dfee243d0a4fbfa586fe0630423b0bcbe0c193976fa7b0420c8e713b8d8955`, landed at `c2d5fc0` |
| map revision | `2026-10-29-a`, equal; anchors 6 of 6; re-derived 4 of 4; rows 49; `frozen` equal 46 of 46 |
| executor model | the model the TZ header names: `get_session` read `session_context.model`, `external_metadata.last_served_model` and `configured_model` equal to it |
| branch | `tz-35-advisor-bot` at `6c74b62bfef7afad2c71c742411124387327a588`, pushed; pull request #35, open, not merged |
| service's code | `/root/adv3-bot-svc/`: `adv3.py` `7f2863a5…`, `adv3-bot.py` `e65de91c…`, `commit.txt` `6c74b62bfef7afad2c71c742411124387327a588` |
| unit | `/etc/systemd/system/adv3-bot.service`, `82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66`, byte-identical to the branch's; enabled through `multi-user.target.wants` |
| state | `/var/lib/adv3-bot/`, root's, `0700`, created empty by B-INSTALL and written by the unit alone |
| interpreter | `/root/tz04a-env/venv/bin/python` 3.12; every session mode under `nice -n 19` and `-B`; the unit under `Nice=10` |
| marks | `install` 14:35:00.231393 UTC · `start` 14:35:29.091595 UTC · `kill` 14:43:29.854466 UTC (`state.json`) |
| blocks | B-INSTALL 14:35:11.444 UTC, the Executor · B-ENABLE 14:38:10.055 UTC, the Boss · B-KILL 14:43:35.201 UTC, the Executor |

---

## 0. Fingerprint

`I0 fingerprint`, from the staged copy of the checker, against the primary checkout at `c2d5fc0` — revision
`2026-10-29-a`; anchors `A1` `229a944f2d51`, `A2` `6c5089330629`, `A3` `0-complete / 1-student-5tau-not-disqualified /
2-no-edge-4tau-240-undecidable`, `A4` `437b45ea196b`, `A5` `0f6c90451cbd`, `A6` `729f0bcdbee3`, each equal to the TZ
header's; `A2`, `A4`, `A5` and `A6` re-derived. **V1: `FINGERPRINT PASS`.** The map, the `reported` row: 1,879 lines,
444,652 bytes, SHA-256 `e14b15d36a6119cbfc49dc2acf8e42463134c75395ac9031baeee9bd35ea042f`, as §0.2 states.

### 0.1 The 49 rows of the map's §0 table, and the map (V1) — `logs/00b-fingerprint.log`, verbatim

```
2026-10-29T14:15:12.283210563Z
map 1879 lines 444652 bytes, SHA-256 e14b15d36a6119cbfc49dc2acf8e42463134c75395ac9031baeee9bd35ea042f - revision 2026-10-29-a
anchor A2 research/twap-divergence.py 6c5089330629
anchor A4 BTC-EXECUTOR-INSTRUCTIONS.md 437b45ea196b
anchor A5 research/recorder/recorder.py 0f6c90451cbd
anchor A6 research/pfair.py 729f0bcdbee3
reported SYSTEM-MAP.md                                    1879   444652 e14b15d36a6119cbfc49dc2acf8e42463134c75395ac9031baeee9bd35ea042f
frozen   BTC-EXECUTOR-INSTRUCTIONS.md                      234    11128 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b  equal
frozen   research/twap-divergence.py                      1135    50928 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473  equal
frozen   research/selftest-twap-divergence.py              376    16736 ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a  equal
tracked  research/tz02-distribution.py                     334    14511 f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4
frozen   research/pfair.py                                 441    19357 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68  equal
frozen   research/selftest-pfair.py                        619    32559 b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa  equal
frozen   research/tz06-calibration.py                      577    27138 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f  equal
frozen   research/tz07a-variance-time.py                   623    28414 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771  equal
frozen   research/tz07b-settlement-dispersion.py           515    24926 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc  equal
frozen   research/tz08a-out-of-sample.py                   745    38822 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c  equal
frozen   research/tz09-disk-inventory.py                   894    41004 b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6  equal
frozen   research/tz10b-sigma-or-link.py                  1224    61018 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088  equal
frozen   research/tz11a-student-link.py                   1231    64732 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839  equal
frozen   research/tz12-sized-gate.py                      1157    61637 d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999  equal
frozen   research/tz13-sized-gate-test3.py                1074    53901 a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd  equal
frozen   research/tz14-quote-inventory.py                 2124   109972 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02  equal
frozen   research/tz15-phase2-gate.py                     1517    73799 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3  equal
frozen   research/tz16a-phase2-decisive-gate.py           2198   111192 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125  equal
frozen   research/tz17-settlement-chain.py                1102    38622 e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92  equal
frozen   research/tz18a-chainbook-capture.py              1683    69517 e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae  equal
frozen   research/tz20-capture-under-systemd.py            771    36528 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7  equal
frozen   research/tz21-recorder-memory.py                 1284    59009 d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f  equal
frozen   research/tz23-maker-m0.py                        1184    54885 6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f  equal
frozen   research/tz24-nesting-b2.py                      1535    76142 4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b  equal
frozen   research/tz26-nesting-b3-capture.py              2492   118466 caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec  equal
frozen   research/tz27-pairbook-archive.py                2078   106284 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673  equal
frozen   research/tz28-pairbook-archive-timer.py          1438    74576 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4  equal
frozen   research/tz29-maker-m0-second-look.py            1225    68959 18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905  equal
frozen   research/tz30-nesting-b3-measure.py              2518   131119 93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab  equal
frozen   research/tz31-who-earns.py                       1523    84775 7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765  equal
frozen   research/tz32-our-quoting.py                     2576   138209 6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61  equal
frozen   research/tz33-reward-book-capture.py             3542   175160 a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670  equal
frozen   research/tz34-rewardbook-archive-timer.py        1791    99388 1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72  equal
frozen   research/recorder/recorder.py                     651    27821 0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7  equal
frozen   research/recorder/config.py                       112     4773 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d  equal
frozen   research/recorder/manifest.py                     254    10002 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045  equal
frozen   research/recorder/analyze.py                      813    34705 eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d  equal
frozen   research/recorder/probe.py                        227     9324 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2  equal
frozen   research/recorder/selftest.py                     573    30591 c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90  equal
frozen   deploy/systemd/btc-recorder.service                23      707 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1  equal
frozen   deploy/systemd/btc-chainbook.service               22      724 a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2  equal
frozen   deploy/systemd/btc-pairbook.service                22      761 ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8  equal
frozen   deploy/systemd/btc-pairbook-archive.service        17      794 2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7  equal
frozen   deploy/systemd/btc-pairbook-archive.timer          13      417 07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913  equal
frozen   deploy/systemd/btc-rewardbook.service              23      817 7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec  equal
frozen   deploy/systemd/btc-rewardbook-archive.service      17      810 a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f  equal
frozen   deploy/systemd/btc-rewardbook-archive.timer        13      428 bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f  equal
tracked  .gitignore                                          5      252 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b
FINGERPRINT PASS: revision 2026-10-29-a; anchors 6 of 6, 4 re-derived; 49 rows, 46 of 46 frozen equal, 2 tracked, 1 reported
exit=0
```

### 0.2 Contract §1, §0.0 and §0.1 — the start-up, the work tree and the checker staged (V4)

Contract §1 steps 1 and 2 ran before §0.0's `mkdir`; their log and §0.0's were written by hand after the command,
because `logs/` did not exist before it (§6).

`logs/00-startup.log`:

```
# contract section 1 steps 1 and 2, before section 0.0; transcribed from the session
# 2026-10-29 ~14:12 UTC: git fetch origin main (cfa0bf5..c2d5fc0), git merge --ff-only origin/main (fast-forward to c2d5fc0)
$ date -u +%FT%T.%NZ && git checkout main && git pull; git rev-parse HEAD origin/main; git status --short | wc -l
2026-10-29T14:14:11.190705271Z
Already on 'main'
Your branch is up to date with 'origin/main'.
Already up to date.
c2d5fc0b792b4bbb58fe963aa5491a735351915b
c2d5fc0b792b4bbb58fe963aa5491a735351915b
0
# step 2: CryptoTZ/TZ-35-advisor-bot.md read in full (3,057 lines); SYSTEM-MAP.md sections 0, 2.6, 6 and 7 items 114-131 read
# step 5: get_session read session_context.model, external_metadata.last_served_model and configured_model equal to the model the TZ header names
```

`logs/00-mkdir.log`:

```
# section 0.0, run 2026-10-29 ~14:15 UTC; transcribed from the session after the command, since logs/ did not exist before it
$ mkdir /root/tz35-work /root/tz35-work/logs; echo "exit=$?"
exit=0
```

§0.1's script, verbatim, into `/root/tz35-work/stage` — `logs/00a-stage.log`: **6 of 6 hashes asserted**, each file's
lines and bytes equal to §0.1's table.

```
2026-10-29T14:15:06.767309418Z
/root/tz35-work/stage/advisor/RULE-ADV-3.txt 33 3203 ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169
/root/tz35-work/stage/advisor/adv3-bot.py 422 19365 e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb
/root/tz35-work/stage/advisor/adv3.py 718 35479 7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb
/root/tz35-work/stage/advisor/selftest-adv3.py 155 8909 76bad371727e0d4bf13c1d009f1b8f9412133a33788c456ecd53d1f83df6f0e6
/root/tz35-work/stage/deploy/systemd/adv3-bot.service 27 863 82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66
/root/tz35-work/stage/research/tz35-advisor-deploy.py 802 42049 d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5
exit=0
```

### 0.3 Host gate — §0.3's block, verbatim (V2)

**The first reading, 14:15:26 UTC: `READING HOST: FAIL - 11 of 12`.** H6 failed: `/etc/adv3-bot` did not exist, so §0.6's
steps 1 and 2 had not been done. Nothing had been written but `/root/tz35-work/` (its stage, its logs and the checker's
`state.json`). The Executor stopped there and asked the Boss whether to file BLOCKED or have him do §0.6's steps first.
He chose the steps. His token file carries 14:21 UTC in the second reading's `ls -la`, and **the host gate
was read again in full at 14:23:21 UTC: `READING HOST: PASS - 12 of 12`.** `state.json`'s `host` record is the second
reading's. Both logs are quoted verbatim (§6 item 1).

`logs/00c-host.log`, the first reading:

```
2026-10-29T14:15:26.081728906Z
printed: MemAvailable 308350976 MemTotal 1002127360 SwapFree 2811977728 | free bytes 10463903744 | archive ledger restart records 31 | chat-id present False
printed: btc-recorder.service ActiveState=active MainPID=2388318 NRestarts=0 UnitFileState=enabled
printed: btc-pairbook.service ActiveState=active MainPID=3216422 NRestarts=12 UnitFileState=enabled
printed: btc-rewardbook.service ActiveState=active MainPID=3137952 NRestarts=1 UnitFileState=enabled
printed: btc-pairbook-archive.service ActiveState=failed Result=exit-code
printed: the archive ledger, run 1793260762 records [('start', None, '2026-10-29T07:59:22.858185Z'), ('set', None, '2026-10-29T07:59:24.062054Z'), ('upload', None, '2026-10-29T08:00:56.315733Z'), ('deferred', 1, '2026-10-29T08:02:57.101110Z')] | lines that do not parse 0
HOST H1 a recorder manifest exists                                    PASS
HOST H2 the filesystem is /dev/vda2 of 31,612,203,008 bytes           PASS
HOST H2 the recorder runtime names e3975b5                            PASS
HOST H3 /root/tz04a-env runs Python 3.12                              PASS
HOST H4 btc-recorder.service active and enabled                       PASS
HOST H4 btc-pairbook.service active and enabled                       PASS
HOST H4 btc-rewardbook.service active and enabled                     PASS
HOST H5 no adv3-bot unit, file, copy or root                          PASS
HOST H5 no process under the service argv                             PASS
HOST H6 /etc/adv3-bot 700 and its token 600, one line of a bot token  FAIL
HOST the memory gate: MemAvailable at least 170,344,448 bytes         PASS
HOST the disk gate: /dev/vda2 free at least 7,400,000,000 bytes       PASS
READING HOST: FAIL - 11 of 12
Traceback (most recent call last):
  File "/root/tz35-work/stage/research/tz35-advisor-deploy.py", line 802, in <module>
    sys.exit(main(sys.argv[1:]))
             ^^^^^^^^^^^^^^^^^^
  File "/root/tz35-work/stage/research/tz35-advisor-deploy.py", line 795, in main
    table[mode]()
  File "/root/tz35-work/stage/research/tz35-advisor-deploy.py", line 393, in mode_host
    verdict('HOST', checks)
  File "/root/tz35-work/stage/research/tz35-advisor-deploy.py", line 115, in verdict
    assert not bad, f'{name} FAIL: {bad}'
           ^^^^^^^
AssertionError: HOST FAIL: ['H6 /etc/adv3-bot 700 and its token 600, one line of a bot token']
host exit=1
Thu Oct 29 02:15:26 PM UTC 2026
1793283326
2026-08-02 07:24:32
 -2 b1b399c70c6e4dcc934755f70a2ca231 Fri 2026-07-17 01:01:43 UTC Fri 2026-07-24 14:55:46 UTC
 -1 285d6962c92c407d837d1ce329b93aa4 Fri 2026-07-24 14:55:54 UTC Sun 2026-08-02 07:23:49 UTC
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-02 07:24:34 UTC Thu 2026-10-29 14:15:25 UTC
1
MemTotal:         978640 kB
MemAvailable:     337204 kB
SwapTotal:       3174396 kB
SwapFree:        2738648 kB
MainPID=2388318
Result=success
NRestarts=0
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC

MainPID=3216422
Result=success
NRestarts=12
Id=btc-pairbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Thu 2026-10-29 03:05:31 UTC

MainPID=0
Result=exit-code
NRestarts=0
Id=btc-pairbook-archive.service
ActiveState=failed
SubState=failed
UnitFileState=static
ActiveEnterTimestamp=

Result=success
Id=btc-pairbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-11 15:08:11 UTC

MainPID=3137952
Result=success
NRestarts=1
Id=btc-rewardbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Wed 2026-10-28 12:56:29 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-rewardbook-archive.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=

Result=success
Id=btc-rewardbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled
ActiveEnterTimestamp=Thu 2026-10-29 08:17:07 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-chainbook.service
ActiveState=inactive
SubState=dead
UnitFileState=disabled
ActiveEnterTimestamp=

MainPID=0
Result=success
NRestarts=0
Id=crypto-deploy.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=

MainPID=2696817
Result=success
NRestarts=0
Id=crypto-announce.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-25 12:11:15 UTC
NEXT                        LEFT LAST                              PASSED UNIT                         ACTIVATES
Fri 2026-10-30 00:47:12 UTC  10h Thu 2026-10-29 09:58:30 UTC 4h 16min ago apt-daily.timer              apt-daily.service
Fri 2026-10-30 01:30:20 UTC  11h Thu 2026-10-29 08:47:07 UTC 5h 28min ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Fri 2026-10-30 03:00:20 UTC  12h Thu 2026-10-29 07:59:22 UTC       6h ago btc-pairbook-archive.timer   btc-pairbook-archive.service
Fri 2026-10-30 06:40:01 UTC  16h Thu 2026-10-29 06:19:40 UTC       7h ago apt-daily-upgrade.timer      apt-daily-upgrade.service

4 timers listed.
btc-recorder.service cmp exit=0
btc-pairbook.service cmp exit=0
btc-pairbook-archive.service cmp exit=0
btc-pairbook-archive.timer cmp exit=0
btc-rewardbook.service cmp exit=0
btc-rewardbook-archive.service cmp exit=0
btc-rewardbook-archive.timer cmp exit=0
disabled
exit=1
inactive
exit=3
/root/tz34-work exit=1
/root/adv3-bot-svc exit=1
/var/lib/adv3-bot exit=1
/etc/adv3-bot exit=1
ls: cannot access '/etc/adv3-bot': No such file or directory
290850273	/var/lib/btc-rewardbook
1003406581	/var/lib/btc-pairbook
119554426	/root/.claude
2151
/root/btc-5m-twap       c2d5fc0 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/95f1d37e-8b62-5abb-93a1-839ff07d8cf8/scratchpad
total 24
drwx------  6 root root 4096 Oct 29 14:12 .
drwx------ 32 root root 4096 Oct 29 14:12 ..
drwx------  4 root root 4096 Oct 29 07:43 540c6c83-4413-5ceb-86a4-2d45c7f8989a
drwx------  3 root root 4096 Oct 29 07:43 57feec2d-2369-4cb0-9cad-8ac28cb7e578
drwx------  3 root root 4096 Oct 29 14:12 670d0460-3b29-4949-95f8-46f94b680ab9
drwx------  4 root root 4096 Oct 29 14:12 95f1d37e-8b62-5abb-93a1-839ff07d8cf8
```

`logs/00c-host-2.log`, the second reading, the one every later step and G-STILL rest on:

```
2026-10-29T14:23:21.961580548Z
printed: MemAvailable 300171264 MemTotal 1002127360 SwapFree 2785349632 | free bytes 10457419776 | archive ledger restart records 31 | chat-id present False
printed: btc-recorder.service ActiveState=active MainPID=2388318 NRestarts=0 UnitFileState=enabled
printed: btc-pairbook.service ActiveState=active MainPID=3216422 NRestarts=12 UnitFileState=enabled
printed: btc-rewardbook.service ActiveState=active MainPID=3137952 NRestarts=1 UnitFileState=enabled
printed: btc-pairbook-archive.service ActiveState=failed Result=exit-code
printed: the archive ledger, run 1793260762 records [('start', None, '2026-10-29T07:59:22.858185Z'), ('set', None, '2026-10-29T07:59:24.062054Z'), ('upload', None, '2026-10-29T08:00:56.315733Z'), ('deferred', 1, '2026-10-29T08:02:57.101110Z')] | lines that do not parse 0
HOST H1 a recorder manifest exists                                    PASS
HOST H2 the filesystem is /dev/vda2 of 31,612,203,008 bytes           PASS
HOST H2 the recorder runtime names e3975b5                            PASS
HOST H3 /root/tz04a-env runs Python 3.12                              PASS
HOST H4 btc-recorder.service active and enabled                       PASS
HOST H4 btc-pairbook.service active and enabled                       PASS
HOST H4 btc-rewardbook.service active and enabled                     PASS
HOST H5 no adv3-bot unit, file, copy or root                          PASS
HOST H5 no process under the service argv                             PASS
HOST H6 /etc/adv3-bot 700 and its token 600, one line of a bot token  PASS
HOST the memory gate: MemAvailable at least 170,344,448 bytes         PASS
HOST the disk gate: /dev/vda2 free at least 7,400,000,000 bytes       PASS
READING HOST: PASS - 12 of 12
host exit=0
Thu Oct 29 02:23:22 PM UTC 2026
1793283802
2026-08-02 07:24:32
 -2 b1b399c70c6e4dcc934755f70a2ca231 Fri 2026-07-17 01:01:43 UTC Fri 2026-07-24 14:55:46 UTC
 -1 285d6962c92c407d837d1ce329b93aa4 Fri 2026-07-24 14:55:54 UTC Sun 2026-08-02 07:23:49 UTC
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-02 07:24:34 UTC Thu 2026-10-29 14:23:22 UTC
1
MemTotal:         978640 kB
MemAvailable:     364760 kB
SwapTotal:       3174396 kB
SwapFree:        2696772 kB
MainPID=2388318
Result=success
NRestarts=0
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC

MainPID=3216422
Result=success
NRestarts=12
Id=btc-pairbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Thu 2026-10-29 03:05:31 UTC

MainPID=0
Result=exit-code
NRestarts=0
Id=btc-pairbook-archive.service
ActiveState=failed
SubState=failed
UnitFileState=static
ActiveEnterTimestamp=

Result=success
Id=btc-pairbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-11 15:08:11 UTC

MainPID=3137952
Result=success
NRestarts=1
Id=btc-rewardbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Wed 2026-10-28 12:56:29 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-rewardbook-archive.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=

Result=success
Id=btc-rewardbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled
ActiveEnterTimestamp=Thu 2026-10-29 08:17:07 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-chainbook.service
ActiveState=inactive
SubState=dead
UnitFileState=disabled
ActiveEnterTimestamp=

MainPID=0
Result=success
NRestarts=0
Id=crypto-deploy.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=

MainPID=2696817
Result=success
NRestarts=0
Id=crypto-announce.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-25 12:11:15 UTC
NEXT                        LEFT LAST                              PASSED UNIT                         ACTIVATES
Fri 2026-10-30 00:47:12 UTC  10h Thu 2026-10-29 09:58:30 UTC 4h 24min ago apt-daily.timer              apt-daily.service
Fri 2026-10-30 01:30:20 UTC  11h Thu 2026-10-29 08:47:07 UTC 5h 36min ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Fri 2026-10-30 03:00:20 UTC  12h Thu 2026-10-29 07:59:22 UTC       6h ago btc-pairbook-archive.timer   btc-pairbook-archive.service
Fri 2026-10-30 06:40:01 UTC  16h Thu 2026-10-29 06:19:40 UTC       8h ago apt-daily-upgrade.timer      apt-daily-upgrade.service

4 timers listed.
btc-recorder.service cmp exit=0
btc-pairbook.service cmp exit=0
btc-pairbook-archive.service cmp exit=0
btc-pairbook-archive.timer cmp exit=0
btc-rewardbook.service cmp exit=0
btc-rewardbook-archive.service cmp exit=0
btc-rewardbook-archive.timer cmp exit=0
disabled
exit=1
inactive
exit=3
/root/tz34-work exit=1
/root/adv3-bot-svc exit=1
/var/lib/adv3-bot exit=1
/etc/adv3-bot exit=0
total 20
drwx------   2 root root  4096 Oct 29 14:21 .
drwxr-xr-x 130 root root 12288 Oct 29 14:20 ..
-rw-------   1 root root    47 Oct 29 14:21 token
297351661	/var/lib/btc-rewardbook
1003406581	/var/lib/btc-pairbook
119637440	/root/.claude
2151
/root/btc-5m-twap       c2d5fc0 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/tmp/claude-0/-root-btc-5m-twap/95f1d37e-8b62-5abb-93a1-839ff07d8cf8/scratchpad
total 24
drwx------  6 root root 4096 Oct 29 14:12 .
drwx------ 32 root root 4096 Oct 29 14:12 ..
drwx------  4 root root 4096 Oct 29 07:43 540c6c83-4413-5ceb-86a4-2d45c7f8989a
drwx------  3 root root 4096 Oct 29 07:43 57feec2d-2369-4cb0-9cad-8ac28cb7e578
drwx------  3 root root 4096 Oct 29 14:12 670d0460-3b29-4949-95f8-46f94b680ab9
drwx------  4 root root 4096 Oct 29 14:12 95f1d37e-8b62-5abb-93a1-839ff07d8cf8
```

The rest, printed and carrying no threshold, from the second reading: one boot since 2026-08-02 07:24:34 UTC; the seven
installed project units `cmp`-equal to `main`'s, `exit=0` each; `telemetry-watch.service` `disabled` and `inactive`;
`/root/tz34-work`, `/root/adv3-bot-svc` and `/var/lib/adv3-bot` absent; `/etc/adv3-bot` holding `token` alone, 47
bytes, `-rw-------`, root's; `du -sb` of the reward book's store `297,351,661` and the pair book's `1,003,406,581`
bytes; the forensic store's `2,151` files, map §3's; the two worktrees, map §3's; and beside this session's own directory
`95f1d37e-8b62-5abb-93a1-839ff07d8cf8`, TZ-34's `540c6c83…` and `57feec2d…` and one more, `670d0460…`, which §3.3
names live. **The pair book's archive's deferred set `1793260762`** reads `start` 07:59:22.858, `set` 07:59:24.062,
`upload` 08:00:56.316 and `deferred` (count 1) 08:02:57.101 UTC, every ledger line parsing, at both readings — map §7 item
128's state, unchanged; that archive's service `failed`, `Result=exit-code`, its timer next at 2026-10-30 03:00:20 UTC.

### 0.4 Free space and `MemAvailable` — every read, its instant and its bound

| instant (UTC) | read by | `MemAvailable` (bytes) | `/dev/vda2` free (bytes) | bound |
|---|---|---|---|---|
| 14:15:26 | `I0 host`, first | 308,350,976 | 10,463,903,744 | `170,344,448` / `7,400,000,000` |
| 14:15:26 | §0.3's `grep` of `/proc/meminfo` | 337,204 kB | — | printed |
| 14:23:21 | `I0 host`, second | 300,171,264 | 10,457,419,776 | `170,344,448` / `7,400,000,000` |
| 14:43:21 | §3.9's `grep` after `I load` | 247,460 kB | — | printed |
| 14:57:01 | §3.12's `free -b` and `df` | 293,498,880 (`available`) | 10,355,449,856 | printed |
| 14:58:17 | B-RECLAIM-OWN's `df` | — | 10,356,695,040 | printed |

### 0.5 Refs (§0.5) — `logs/00d-number.log`, verbatim, read at 14:23:35 UTC, before §3.1's push (V3)

**83 ref lines**, the Architect's count at 10:38 UTC: `HEAD`, twelve branches with `main` at `c2d5fc0`, the two
annotated tags and their peeled lines, thirty-two `pairbook-streams-*` tags, one `rewardbook-streams-*` tag and
thirty-three pull heads; no `refs/heads/tz-35-advisor-bot`. `main`'s first-parent commits above `6785590`: `6ae312c`
(`M SYSTEM-MAP.md`), `ec5e2b3` (`D CryptoTZ/TZ-34-advisor-bot.md`) and the upload carrying this TZ, `c2d5fc0`
(`A CryptoTZ/TZ-35-advisor-bot.md`). `main` carries revision `2026-10-29-a`, `ADVISOR-SKILL.md` and
`.github/workflows/adv2-signal.yml`. No BLOCK condition.

```
2026-10-29T14:23:35.133449606Z
printed: origin/main c2d5fc0b792b4bbb58fe963aa5491a735351915b | 89 paths under CryptoTZ/ and CryptoReports/ | of the number TZ-35- ['CryptoTZ/TZ-35-advisor-bot.md']
NUMBER CryptoTZ/ holds TZ-35-advisor-bot.md and no other TZ-35- file    PASS
NUMBER CryptoReports/ holds no TZ-35- report                            PASS
READING NUMBER: PASS - 2 of 2
number exit=0
ls-remote exit=0
c2d5fc0b792b4bbb58fe963aa5491a735351915b	HEAD
c2d5fc0b792b4bbb58fe963aa5491a735351915b	refs/heads/main
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8	refs/heads/tz-23-maker-m0
6f045cffc3601b589d3b8b7a6a9af6f73991e18b	refs/heads/tz-24-nesting-b2
e8b46a85d61e1a17841962846f6d3012046c2d70	refs/heads/tz-26-nesting-b3-capture
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/heads/tz-27-pairbook-archive
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/heads/tz-28-pairbook-archive-timer
f6425f713034724210dc120d2108bcfad63cadc6	refs/heads/tz-29-maker-m0-second-look
fcd9ca566e9b948f0426707e7c3b5684f7f03b04	refs/heads/tz-30-nesting-b3-measure
404288fb03ffd3619b2183f121d45688def8fba8	refs/heads/tz-31-who-earns
b601f756edea59adf536d7ef05226d6f06bcef13	refs/heads/tz-32-our-quoting
2dcd70e08b18b93c64bb67d9849ac1216ce40e41	refs/heads/tz-33-reward-book-capture
6a615257277d3c94dafd4d39783499560a344648	refs/heads/tz-34-rewardbook-archive-timer
d9e58e8febd8548221598eed137cf40d31496047	refs/pull/1/head
e45f38e89b5ee18e64a16a654b341d74fadcac26	refs/pull/10/head
d34606ee9a592e51293eaad0996c7cae3b84dfcd	refs/pull/11/head
274651805c765bb977c635d75fd1ebdb2c8f550a	refs/pull/12/head
6dc0e24ae1542f98789967bf48057268731a2030	refs/pull/13/head
7ef972397a12bce0cc76b1f58ceda3e5caa43cdc	refs/pull/14/head
ffef5cd822e2e47ce1edd8fff706471a441e9a5f	refs/pull/15/head
f7f171a2e1e8b4b3eafa810f5022f1ca1c5a65b1	refs/pull/16/head
8f1bc93e454275ddb3f0e060bed3bb9f2f9cf31b	refs/pull/17/head
8caa0b41d5cdf9e74e92b11d4317d59a2ee7b567	refs/pull/18/head
ca4bbc1dd583cbb62f3c0c985938d229b526ce7e	refs/pull/19/head
3895356aff853f2fcb1b030b1502acb95b16f0a5	refs/pull/2/head
5076b4305c7800fc7eed0cd3fe05d9577d1b6cf7	refs/pull/20/head
0956da12bd26decbef0fd643b6f223102c7788ba	refs/pull/21/head
e3975b5da44c5328adf3bf3914634cd878842c73	refs/pull/22/head
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8	refs/pull/23/head
6f045cffc3601b589d3b8b7a6a9af6f73991e18b	refs/pull/24/head
e8b46a85d61e1a17841962846f6d3012046c2d70	refs/pull/25/head
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/pull/26/head
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/pull/27/head
f6425f713034724210dc120d2108bcfad63cadc6	refs/pull/28/head
fcd9ca566e9b948f0426707e7c3b5684f7f03b04	refs/pull/29/head
ee2f6327390ef4d0c6169d1fba1a2ed4ae936dc3	refs/pull/3/head
404288fb03ffd3619b2183f121d45688def8fba8	refs/pull/30/head
b601f756edea59adf536d7ef05226d6f06bcef13	refs/pull/31/head
2dcd70e08b18b93c64bb67d9849ac1216ce40e41	refs/pull/32/head
6a615257277d3c94dafd4d39783499560a344648	refs/pull/34/head
0e13a5c76dfa2469ff25b3b0dd282872decf6f25	refs/pull/4/head
4216c04673ced76b5b2ac60ef57c9abedc46f9b9	refs/pull/5/head
5ed667afd1b53f036b9f938fcce13c0d709cd77f	refs/pull/6/head
c44af687203d14d5d485d4297c04cfb827096af9	refs/pull/7/head
26bbb61aed774a88355dd5204d8b69fda9135a68	refs/pull/8/head
e2625ea2b5473c311d59a48f32540ce39d58e591	refs/pull/9/head
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1791731892
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1791774020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1791860420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1791946820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792033220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792045110
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792119620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792206020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792226137
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792292420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792378820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792446859
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792465220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792495417
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792551620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792618744
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792638020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792650248
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792724420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792810820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792850109
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792897220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792908757
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792930875
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792983620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793070020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793082340
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793156420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793169873
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793187616
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793242820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793260762
6a615257277d3c94dafd4d39783499560a344648	refs/tags/rewardbook-streams-1793263627
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
e299d4e45f48b7efaa8cb18bd54b139fc0627630	refs/tags/tz-27-pairbook-streams
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/tags/tz-27-pairbook-streams^{}
ref lines: 83
branches: 12  pairbook-streams tags: 32  rewardbook-streams tags: 1  pull heads: 33  pull merge refs: 0
refs/heads/tz-35-advisor-bot present: 0
--- main's first-parent commits above 6785590
c2d5fc0b792b4bbb58fe963aa5491a735351915b 2026-10-29T18:10:55+04:00 Add files via upload

A	CryptoTZ/TZ-35-advisor-bot.md
ec5e2b35d1e0bf79b6756d61690e17b3e09e49e1 2026-10-29T14:16:55+04:00 Delete CryptoTZ/TZ-34-advisor-bot.md

D	CryptoTZ/TZ-34-advisor-bot.md
6ae312c7114aec78b2e8921aa90e56d1ec77200e 2026-10-29T14:13:23+04:00 Update SYSTEM-MAP.md

M	SYSTEM-MAP.md
--- main carries
Revision 2026-10-29-a
.github/workflows/adv2-signal.yml
ADVISOR-SKILL.md
```

---

## 1. Input

- **`CryptoTZ/TZ-35-advisor-bot.md`** and **`SYSTEM-MAP.md`**, as §0 prints them; the six files of Appendix A extracted
  from the former, by §0.1's script, twice.
- **Binance's archive, `data.binance.vision`**, read by `adv3.py`'s own functions alone: for G-SAME, the daily kline file
  of each of the 14 days 2026-10-15 … 2026-10-28 for the 42 coins' perpetuals — 546 served and 42 absent, one a coin;
  for G-HISTORY, the 42 coins' monthly kline files from 2019-09, the daily files of months without one, and the monthly
  funding files, as `adv3.history` reads them. Nothing was stored but `history.json`, the derived facts, 19,362 bytes.
- **`fapi.binance.com`**, public market data alone, no key and no account endpoint: G-SAME's 42 `/fapi/v1/klines`
  requests; P-START's four; and the unit's own since 14:38:10 UTC.
- **Telegram's Bot API**: P-START's `getMe`, `--find-chat`'s `getUpdates`, `--hello`'s `sendMessage`, and the unit's own.
- **Nothing of any capture was read**: under `/var/lib/btc-recorder/` only `I0 host`'s `find`, `grep -c` and `df`; of
  `/var/lib/btc-pairbook/` and `/var/lib/btc-rewardbook/` only `du -sb`; of `/var/lib/btc-pairbook-archive/` only
  `ledger.jsonl`, read by `host` and `still`. **Nothing was re-collected.**

---

## 2. Measurements

### 2.1 §3.1 — the branch and its files (V3, V4)

`git fetch`, `I0 number` again — **`READING NUMBER: PASS - 2 of 2`** — and the worktree — `logs/01-branch.log`:

```
2026-10-29T14:23:42.991927100Z
fetch exit=0
printed: origin/main c2d5fc0b792b4bbb58fe963aa5491a735351915b | 89 paths under CryptoTZ/ and CryptoReports/ | of the number TZ-35- ['CryptoTZ/TZ-35-advisor-bot.md']
NUMBER CryptoTZ/ holds TZ-35-advisor-bot.md and no other TZ-35- file    PASS
NUMBER CryptoReports/ holds no TZ-35- report                            PASS
READING NUMBER: PASS - 2 of 2
number exit=0
Preparing worktree (new branch 'tz-35-advisor-bot')
branch 'tz-35-advisor-bot' set up to track 'origin/main'.
HEAD is now at c2d5fc0 Add files via upload
worktree exit=0
```

§0.1's script again into `/root/tz35-work/wt`, the same 6 lines, bytes and SHA-256 as at §0.1; the two removals, the
adds and **`git diff --cached --name-status`: exactly 8 lines, `D` for the two ADV-2 paths and `A` for the six** —
`logs/01a-branch-files.log`:

```
2026-10-29T14:23:58.919857279Z
/root/tz35-work/wt/advisor/RULE-ADV-3.txt 33 3203 ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169
/root/tz35-work/wt/advisor/adv3-bot.py 422 19365 e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb
/root/tz35-work/wt/advisor/adv3.py 718 35479 7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb
/root/tz35-work/wt/advisor/selftest-adv3.py 155 8909 76bad371727e0d4bf13c1d009f1b8f9412133a33788c456ecd53d1f83df6f0e6
/root/tz35-work/wt/deploy/systemd/adv3-bot.service 27 863 82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66
/root/tz35-work/wt/research/tz35-advisor-deploy.py 802 42049 d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5
exit=0
rm exit=0
add exit=0
D	.github/workflows/adv2-signal.yml
D	ADVISOR-SKILL.md
A	advisor/RULE-ADV-3.txt
A	advisor/adv3-bot.py
A	advisor/adv3.py
A	advisor/selftest-adv3.py
A	deploy/systemd/adv3-bot.service
A	research/tz35-advisor-deploy.py
diff lines: 8
D  .github/workflows/adv2-signal.yml
D  ADVISOR-SKILL.md
A  advisor/RULE-ADV-3.txt
A  advisor/adv3-bot.py
A  advisor/adv3.py
A  advisor/selftest-adv3.py
A  deploy/systemd/adv3-bot.service
A  research/tz35-advisor-deploy.py
```

The commit, alone, and `git ls-remote origin` before the push — 83 lines, equal to §0.5's — `logs/01b-commit.log`:

```
2026-10-29T14:24:23.209212435Z
commit exit=0
6c74b62bfef7afad2c71c742411124387327a588 root <root@vultr.guest> 2026-10-29T14:24:23+00:00
 .github/workflows/adv2-signal.yml |  45 ---
 ADVISOR-SKILL.md                  | 376 ------------------
 advisor/RULE-ADV-3.txt            |  33 ++
 advisor/adv3-bot.py               | 422 ++++++++++++++++++++
 advisor/adv3.py                   | 718 ++++++++++++++++++++++++++++++++++
 advisor/selftest-adv3.py          | 155 ++++++++
 deploy/systemd/adv3-bot.service   |  27 ++
 research/tz35-advisor-deploy.py   | 802 ++++++++++++++++++++++++++++++++++++++
 8 files changed, 2157 insertions(+), 421 deletions(-)
ls-remote exit=0 ref lines 83
diff against section 0.5 exit=0
```

The push, through the remote URL's own credential — `logs/01c-push.log`:

```
2026-10-29T14:24:30.494300452Z
remote: 
remote: Create a pull request for 'tz-35-advisor-bot' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-35-advisor-bot        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-35-advisor-bot -> tz-35-advisor-bot
branch 'tz-35-advisor-bot' set up to track 'origin/tz-35-advisor-bot'.
push exit=0
6c74b62bfef7afad2c71c742411124387327a588
6c74b62bfef7afad2c71c742411124387327a588
6c74b62bfef7afad2c71c742411124387327a588
## tz-35-advisor-bot...origin/tz-35-advisor-bot
```

The pull request — `logs/01d-pr.log`:

```
2026-10-29T14:24:48.510933928Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/35
pr exit=0
```

### 2.2 §3.2 — the self-tests (V5): **32 of 32, 19 of 19, 24 of 24**

No network. Each wrapped in `/usr/bin/time` for its processor and peak memory (§6) — `logs/02-selftests.log`:

```
2026-10-29T14:24:58.773483585Z
SELFTEST-ADV3 PASS: 32 of 32 checks passed
elapsed 0.17 s, user 0.09 s, sys 0.01 s, max RSS 24064 kB
exit=0
SELFTEST PASS: 19 of 19 checks passed
elapsed 0.11 s, user 0.08 s, sys 0.01 s, max RSS 26880 kB
exit=0
SELFTEST PASS: 24 of 24 checks passed
elapsed 0.04 s, user 0.03 s, sys 0.00 s, max RSS 19072 kB
exit=0
wt status lines: 0
```

### 2.3 §3.3 — the directories beside this session

`I scratch "$(dirname "$S")"`, `S` the session's scratchpad: **two earlier** — TZ-34's `540c6c83-4413-5ceb-86a4-2d45c7f8989a`
and `57feec2d-2369-4cb0-9cad-8ac28cb7e578`, as map §3 expects — and **one live**, `670d0460-3b29-4949-95f8-46f94b680ab9`,
born 1 s after this session's process 3286961 started; this session's own skipped — `logs/03-scratch.log`:

```
2026-10-29T14:25:14.450744194Z
running 3114897 started 2026-10-28T10:52:23.940000Z claude
running 3114907 started 2026-10-28T10:52:25.960000Z claude
running 3286961 started 2026-10-29T14:12:19.700000Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
540c6c83-4413-5ceb-86a4-2d45c7f8989a born 2026-10-29T07:43:17.000000Z: earlier
57feec2d-2369-4cb0-9cad-8ac28cb7e578 born 2026-10-29T07:43:16.000000Z: earlier
670d0460-3b29-4949-95f8-46f94b680ab9 born 2026-10-29T14:12:20.000000Z: live, process [3286961]
exit=0
```

### 2.4 §9 B-RECLAIM-SCRATCH — after §3.3, before §3.4 (V19, V20)

One `I reclaim` naming both earlier directories: **`RECLAIM PASS`**, 4 files considered, none named by a report or
kept by name, none copied; the store `2,151 → 2,151` — `logs/03a-reclaim-scratch.log`, unfiltered:

```
2026-10-29T14:25:32.629204860Z
reclaim: 3399 report tokens; forensic store holds 2151 files
RECLAIM PASS: 4 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 2151 -> 2151 files
exit=0
```

Then one `rm -rf` and one `test -e` a directory, each `test -e` `exit=1` — no refusal — `logs/03b-rm-scratch.log`:

```
2026-10-29T14:25:47.170803360Z
exit=0
exit=1
2026-10-29T14:25:47.214324156Z
exit=0
exit=1
```

### 2.5 §3.4 — G-SAME (V6): **PASS**

42 coins, 13 candles compared and 1 archive file absent each — the file of 2026-10-28, not yet published in the
afternoon of 2026-10-29 by every sign (the per-coin count does not name the day) — 546 compared, the least 13 against
`12`, **0 mismatches**; 74.70 s elapsed, user 1.19 s, sys 0.31 s, a peak of 31,108 kB — `logs/04-g-same.log`:

```
2026-10-29T14:25:57.123935220Z
G-SAME per coin, candles compared / archive files absent: BTC 13/1 BCH 13/1 SKY 13/1 XLM 13/1 XMR 13/1 MORPHO 13/1 LIT 13/1 NEAR 13/1 HBAR 13/1 GRAM 13/1 ENA 13/1 UNI 13/1 ARB 13/1 ZEC 13/1 HYPE 13/1 SUI 13/1 ADA 13/1 RENDER 13/1 TAO 13/1 FET 13/1 YFI 13/1 XRP 13/1 SOL 13/1 ONDO 13/1 LINK 13/1 ALGO 13/1 TRX 13/1 BNB 13/1 AAVE 13/1 AVAX 13/1 ETH 13/1 INJ 13/1 LTC 13/1 XAU 13/1 DASH 13/1 PYTH 13/1 WLD 13/1 BTW 13/1 QNT 13/1 PUMP 13/1 VVV 13/1 EGLD 13/1
READING G-SAME: PASS - 42 coins, 546 candles compared, the least 13 for one coin, 0 mismatches
elapsed 74.70 s, user 1.19 s, sys 0.31 s, max RSS 31108 kB
exit=0
2026-10-29T14:27:11.828380846Z
```

### 2.6 §3.4 — G-HISTORY and DETERMINISM (V7): **16 of 16 equal**

Every fact equal to `FACTS` at its four decimals, both gates `NOT DISQUALIFIED`; the file **19,362 bytes, SHA-256
`bcee53097f9f1a5820b551c90054a3f046c027f53cff868b857be3118c74faa1`**, the Architect's bytes. 259.79 s elapsed, user 21.40 s,
sys 3.40 s, a peak of 70,344 kB, below the Architect's `85,172,224`-byte measurement from which §0.4's floor was taken —
`logs/04a-g-history.log`:

```
2026-10-29T14:27:19.359700353Z
history written: /root/tz35-work/history.json 19362 bytes, SHA-256 bcee53097f9f1a5820b551c90054a3f046c027f53cff868b857be3118c74faa1
G-HISTORY base trades          5265                   FACTS 5265       equal
G-HISTORY base wins            1708                   FACTS 1708       equal
G-HISTORY base mean R          0.15759304269466592    FACTS 0.1576     equal
G-HISTORY base median days     3                      FACTS 3          equal
G-HISTORY base share +1R       0.23247863247863249    FACTS 0.2325     equal
G-HISTORY base share +2R       0.12972459639126305    FACTS 0.1297     equal
G-HISTORY base share +3R       0.0818613485280152     FACTS 0.0819     equal
G-HISTORY strong trades        253                    FACTS 253        equal
G-HISTORY strong wins          83                     FACTS 83         equal
G-HISTORY strong mean R        0.5473377337624986     FACTS 0.5473     equal
G-HISTORY strong median days   19.0                   FACTS 19         equal
G-HISTORY strong share +1R     0.4782608695652174     FACTS 0.4783     equal
G-HISTORY strong share +2R     0.2845849802371542     FACTS 0.2846     equal
G-HISTORY strong share +3R     0.17786561264822134    FACTS 0.1779     equal
G-HISTORY gate H               NOT DISQUALIFIED       FACTS NOT DISQUALIFIED equal
G-HISTORY gate S               NOT DISQUALIFIED       FACTS NOT DISQUALIFIED equal
printed, gating nothing: base total 829.7274 R, Sharpe 0.7663, t 2.0022, p 0.022629, worst drawdown -253.7817 R
printed, gating nothing: strong total 138.4764 R, Sharpe 0.6133, t 1.6025, p 0.054523, worst drawdown -60.1030 R
READING G-HISTORY: PASS - 16 of 16 equal
elapsed 259.79 s, user 21.40 s, sys 3.40 s, max RSS 70344 kB
exit=0
2026-10-29T14:31:39.170373620Z
bcee53097f9f1a5820b551c90054a3f046c027f53cff868b857be3118c74faa1  /root/tz35-work/history.json
19362 /root/tz35-work/history.json
```

### 2.7 §3.5 — the service's copy, COPY (V8): **4 of 4**

`logs/05-copy.log`:

```
2026-10-29T14:31:53.414505686Z
exit=0
show exit=0
show exit=0
rev-parse exit=0
COPY the copy holds adv3.py, adv3-bot.py and commit.txt alone         PASS
COPY adv3.py equal to Appendix A                                      PASS
COPY adv3-bot.py equal to Appendix A                                  PASS
COPY commit.txt the branch head, 40 hex and a newline                 PASS
READING COPY: PASS - 4 of 4
copy exit=0
e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb  /root/adv3-bot-svc/adv3-bot.py
7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb  /root/adv3-bot-svc/adv3.py
c7fa5d183b09e3b3fc93d7dbf78d205361d3e8d62c4162e2298f0be998021089  /root/adv3-bot-svc/commit.txt
19365 /root/adv3-bot-svc/adv3-bot.py
35479 /root/adv3-bot-svc/adv3.py
   41 /root/adv3-bot-svc/commit.txt
54885 total
```

### 2.8 §3.6 — P-START (V9): **served - 5 of 5 endpoints**

Exit at 14:32:04.655 UTC; B-ENABLE ran at 14:38:10.055 UTC, inside §3.8's 3,600 s, so §3.6 ran once — `logs/06-probe.log`:

```
2026-10-29T14:31:59.884077047Z
P-KLINES served: 1499 closed daily candles of BTCUSDT, the last 2026-10-28
P-FUNDING served: 3 settlement days of BTCUSDT since 2026-10-27
P-MARKS served: 945 perpetuals, all 42 coins among them with a mark price
P-INTERVALS served: 820 perpetuals with an adjusted funding interval, 42 of the coins among them
P-TELEGRAM served: bot @ClaudeCryptoSignal_bot
READING P-START: served - 5 of 5 endpoints
exit=0
2026-10-29T14:32:04.654745352Z
```

### 2.9 §3.7 — G-CHAT and G-HELLO (V10)

`--find-chat` found no `/start` pending and said so at about 14:33:02 UTC; the Executor told the Boss once, at
14:33:07 UTC, to press Start in `@ClaudeCryptoSignal_bot`; his `/start` came, and **one private chat** was pinned at
14:34:35 UTC, `exit=0` — `logs/07-find-chat.log`:

```
2026-10-29T14:32:12.184261700Z
no /start among 0 pending updates; waiting up to 1800 s for the Boss's /start
updates 1 | private chats that sent /start: 1 | chat pinned to /etc/adv3-bot/chat-id
exit=0
2026-10-29T14:34:35.921748335Z
```

`logs/07-boss-told.log`:

```
# 2026-10-29T14:33:07.833148772Z the Executor told the Boss once, in the session chat, to press Start in @ClaudeCryptoSignal_bot (section 3.7)
```

`--hello` — **message ids `[5]`** — and the file **`600 root`**, 10 bytes — `logs/07a-hello.log`:

```
2026-10-29T14:34:45.923054941Z
G-HELLO sent: message ids [5]
exit=0
600 root 10 /etc/adv3-bot/chat-id
```

### 2.10 §3.8 — the band, the `install` mark, B-INSTALL and PROPS (V11)

The band, open — second `52,493` of the day — `logs/08-band.log`:

```
2026-10-29T14:34:53.547064579Z
second of the day 52493
```

`I mark install`, its own command — `logs/08-mark-install.log`:

```
mark install 2026-10-29T14:35:00.231393Z {}
exit=0
```

**B-INSTALL**, run by the Executor verbatim, no refusal: **`exit=0`**, `verify exit=0` with no finding printed —
`logs/08-b-install.log`:

```
2026-10-29T14:35:11.444342008Z
exit=0
verify exit=0
```

**PROPS: `11 of 11`**, and the timers after the reload: the reward book's archive re-armed to 15:05:11 UTC, 1,800 s
after it; the pair book's archive not re-armed, its next run its calendar's — `logs/08a-props.log`:

```
2026-10-29T14:35:17.707861586Z
printed: ActiveState=inactive FragmentPath=/etc/systemd/system/adv3-bot.service LoadState=loaded MemoryMax=134217728 Nice=10 NoNewPrivileges=yes PrivateTmp=yes ProtectSystem=strict ReadWritePaths=/var/lib/adv3-bot Restart=always RestartPreventExitStatus=3 4 RestartUSec=30s UnitFileState=disabled
PROPS LoadState loaded                                                 PASS
PROPS ActiveState inactive                                             PASS
PROPS UnitFileState disabled                                           PASS
PROPS FragmentPath /etc/systemd/system/adv3-bot.service                PASS
PROPS MemoryMax 134217728                                              PASS
PROPS Nice 10                                                          PASS
PROPS ProtectSystem strict                                             PASS
PROPS NoNewPrivileges yes                                              PASS
PROPS PrivateTmp yes                                                   PASS
PROPS Restart always                                                   PASS
PROPS ReadWritePaths /var/lib/adv3-bot                                 PASS
READING PROPS: PASS - 11 of 11
exit=0
NEXT                         LEFT LAST                              PASSED UNIT                         ACTIVATES
Thu 2026-10-29 15:05:11 UTC 29min Thu 2026-10-29 08:47:07 UTC 5h 48min ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Fri 2026-10-30 03:00:20 UTC   12h Thu 2026-10-29 07:59:22 UTC       6h ago btc-pairbook-archive.timer   btc-pairbook-archive.service

2 timers listed.
```

### 2.11 §3.9 — the `start` mark, B-ENABLE, G-UNIT at 0, G-DAILY, G-REPLY and G-LOAD (V12, V13, V14)

`I mark start`, its own command, taken immediately before the Executor ran B-ENABLE — `logs/09-mark-start.log`:

```
mark start 2026-10-29T14:35:29.091595Z {"ActiveState": "inactive", "MainPID": "0", "NRestarts": "0"}
exit=0
```

**B-ENABLE was refused to the Executor** by the session's permission classifier, `[Unauthorized Persistence]`, at
about 14:35:35 UTC; nothing of it ran. It was handed to the Boss verbatim, its band open, as one line — `logs/09-b-enable-refused.log`:

```
# 2026-10-29T14:36:00.210169385Z B-ENABLE as written was refused by the session's permission classifier ([Unauthorized Persistence]) when the Executor ran it at about 14:35:35 UTC; nothing of it ran (09-b-enable.log not created by it). Handed to the Boss verbatim, section 3.
```

**The Boss ran it in a root shell on the VPS at 14:38:10 UTC: `exit=0`**, the enable link created. Verified by the
Executor through `systemctl show` at 14:38:36 UTC — `active`, `running`, `enabled`, `MainPID` 3290952, `NRestarts` 0,
`ExecMainStartTimestamp` 14:38:10 UTC — and the checker's `unit 0` — `logs/09-b-enable.log`, the block's own:

```
2026-10-29T14:38:10.055458647Z
Created symlink /etc/systemd/system/multi-user.target.wants/adv3-bot.service → /etc/systemd/system/adv3-bot.service.
exit=0
```

**G-UNIT at 0 restarts: `18 of 18`**, 65 s after the block — `logs/09a-unit-0.log`:

```
2026-10-29T14:39:15.524923197Z
printed: ActiveState=active ControlGroup=/system.slice/adv3-bot.service FragmentPath=/etc/systemd/system/adv3-bot.service Id=adv3-bot.service MainPID=3290952 MemoryMax=134217728 NRestarts=0 Nice=10 NoNewPrivileges=yes ProtectSystem=strict ReadWritePaths=/var/lib/adv3-bot Restart=always RestartPreventExitStatus=3 4 RestartUSec=30s SubState=running UnitFileState=enabled
G-UNIT-0 ActiveState active                                               PASS
G-UNIT-0 SubState running                                                 PASS
G-UNIT-0 UnitFileState enabled                                            PASS
G-UNIT-0 FragmentPath /etc/systemd/system/adv3-bot.service                PASS
G-UNIT-0 ControlGroup /system.slice/adv3-bot.service                      PASS
G-UNIT-0 MemoryMax 134217728                                              PASS
G-UNIT-0 Nice 10                                                          PASS
G-UNIT-0 NRestarts 0                                                      PASS
G-UNIT-0 ProtectSystem strict                                             PASS
G-UNIT-0 NoNewPrivileges yes                                              PASS
G-UNIT-0 Restart always                                                   PASS
G-UNIT-0 ReadWritePaths /var/lib/adv3-bot                                 PASS
G-UNIT-0 the MainPID runs the exact argv                                  PASS
G-UNIT-0 its cwd /root/adv3-bot-svc                                       PASS
G-UNIT-0 its cgroup the unit, outside every user slice                    PASS
G-UNIT-0 its NoNewPrivs 1                                                 PASS
G-UNIT-0 the MainPID the only process under the argv                      PASS
G-UNIT-0 the installed unit equal to Appendix A                           PASS
READING G-UNIT-0: PASS - 18 of 18
exit=0
```

**G-DAILY `8 of 8` and G-REPLY `1 of 1`** at the first `I daily`, 72 s after the block, no `NOT YET`: one daily record,
of the close of 2026-10-28, rule `ee206e7c…`, 10,000 USDT and 0.5%, its message ids, 42 signals, three cards; TOP-3
`XMR`, `BTW`, `GRAM`, STRONG `XMR`; the cards XMR LONG at market, BTW LONG at market, GRAM SHORT at market; no line
naming a failure — `logs/09b-daily.log`:

```
2026-10-29T14:39:22.612404302Z
printed: journal records 1 torn 0 | log lines since the start 4
printed: the daily record - top ['XMR', 'BTW', 'GRAM'] strong ['XMR'] cards [('XMR', 1, 'market'), ('BTW', 1, 'market'), ('GRAM', -1, 'market')]
G-DAILY the service logged its start under the unit MainPID              PASS
G-DAILY its candles refreshed to the close of the day before, 42 of 42 served PASS
G-DAILY its daily sent once, for the close of the day before             PASS
G-DAILY exactly one daily record, made today                             PASS
G-DAILY the record: the close of the day before, rule ADV-3              PASS
G-DAILY the record: 10,000 USDT, 0.5% a trade                            PASS
G-DAILY the record: Telegram message ids                                 PASS
G-DAILY the record: 42 signals, at most 3 cards, STRONG among TOP-3      PASS
READING G-DAILY: PASS - 8 of 8
G-REPLY the service answered the pinned chat                             PASS
READING G-REPLY: PASS - 1 of 1
exit=0
```

**G-LOAD: `0.99 s` over `311.0 s`, `0.003` of the core against `0.05`**; `MemoryPeak` 39,378,944 bytes, `VmHWM`
50,084 kB, no swap, one thread — `logs/09c-load.log`:

```
2026-10-29T14:43:21.063674789Z
printed: MemoryCurrent=37404672 MemoryPeak=39378944 MemorySwapCurrent=0 | VmRSS=48328 kB VmHWM=50084 kB VmSwap=0 kB Threads=1
printed: processor 0.99 s over 311.0 s of wall time since the process started
G-LOAD at least 300 s since the start                                   PASS
G-LOAD processor at most 0.05 of the core                               PASS
READING G-LOAD: PASS - 2 of 2
exit=0
MemAvailable:     247460 kB
```

### 2.12 §3.10 — the `kill` mark, B-KILL, G-RESTART, G-ONCE and G-UNIT at 1 (V12, V15)

`I mark kill` — `logs/10-mark-kill.log`:

```
mark kill 2026-10-29T14:43:29.854466Z {"ActiveState": "active", "MainPID": "3290952", "NRestarts": "0"}
exit=0
```

**B-KILL**, run by the Executor verbatim, no refusal — `logs/10-b-kill.log`:

```
2026-10-29T14:43:35.200555138Z
exit=0
```

**G-RESTART `5 of 5` and G-ONCE `2 of 2`**, 50 s after the block: pid 3290952 → 3291955, started at 14:44:05.12 UTC,
35.27 s after the mark and 29.92 s after the block, `RestartSec=30` — `logs/10a-restart.log`:

```
2026-10-29T14:44:25.261650807Z
printed: old MainPID 3290952 new 3291955 started 2026-10-29T14:44:05.120000Z
G-RESTART a new MainPID                                                    PASS
G-RESTART started after the kill and at most 60 s later                    PASS
G-RESTART NRestarts 1                                                      PASS
G-RESTART active and running                                               PASS
G-RESTART the new process logged its start, the daily read as sent today   PASS
READING G-RESTART: PASS - 5 of 5
G-ONCE still exactly one daily record for today                         PASS
G-ONCE no daily sent after the kill                                     PASS
READING G-ONCE: PASS - 2 of 2
exit=0
```

**G-UNIT at 1 restart: `18 of 18`** — `logs/10b-unit-1.log`:

```
2026-10-29T14:44:30.839371667Z
printed: ActiveState=active ControlGroup=/system.slice/adv3-bot.service FragmentPath=/etc/systemd/system/adv3-bot.service Id=adv3-bot.service MainPID=3291955 MemoryMax=134217728 NRestarts=1 Nice=10 NoNewPrivileges=yes ProtectSystem=strict ReadWritePaths=/var/lib/adv3-bot Restart=always RestartPreventExitStatus=3 4 RestartUSec=30s SubState=running UnitFileState=enabled
G-UNIT-1 ActiveState active                                               PASS
G-UNIT-1 SubState running                                                 PASS
G-UNIT-1 UnitFileState enabled                                            PASS
G-UNIT-1 FragmentPath /etc/systemd/system/adv3-bot.service                PASS
G-UNIT-1 ControlGroup /system.slice/adv3-bot.service                      PASS
G-UNIT-1 MemoryMax 134217728                                              PASS
G-UNIT-1 Nice 10                                                          PASS
G-UNIT-1 NRestarts 1                                                      PASS
G-UNIT-1 ProtectSystem strict                                             PASS
G-UNIT-1 NoNewPrivileges yes                                              PASS
G-UNIT-1 Restart always                                                   PASS
G-UNIT-1 ReadWritePaths /var/lib/adv3-bot                                 PASS
G-UNIT-1 the MainPID runs the exact argv                                  PASS
G-UNIT-1 its cwd /root/adv3-bot-svc                                       PASS
G-UNIT-1 its cgroup the unit, outside every user slice                    PASS
G-UNIT-1 its NoNewPrivs 1                                                 PASS
G-UNIT-1 the MainPID the only process under the argv                      PASS
G-UNIT-1 the installed unit equal to Appendix A                           PASS
READING G-UNIT-1: PASS - 18 of 18
exit=0
```

### 2.13 §3.11 — G-STILL (V16)

Six `I still` runs printed `NOT YET` and exited `3`, from 14:44:47 to 14:54:47 UTC: the pair book's archive was `failed`, its
07:59 run's deferral, and no run of it had started after the `start` mark. At 14:56:47 UTC, 1,279 s after the mark with
no run started, it read the three units before (the host gate, 14:23:21 UTC) and after: the recorder `2388318`,
`NRestarts` 0; the pair book `3216422`, 12; the reward book `3137952`, 1; each `active`. The pair book's archive's ledger
held 31 restart records, then 31. The deferred set `1793260762`'s four records were unchanged from §0.3. **`READING
G-STILL: PASS - 3 of 3`.** The reward book's archive's run re-armed by the enable's reload, due at 15:08:10 UTC, falls
after this reading, and it restarts nothing (map §2.6).

`logs/11-still.log`, every run:

```
2026-10-29T14:44:47.195832170Z
NOT YET: archive failed, a run since the last reload False, 558 s after it
exit=3
2026-10-29T14:46:47.337055528Z
NOT YET: archive failed, a run since the last reload False, 678 s after it
exit=3
2026-10-29T14:48:47.387093522Z
NOT YET: archive failed, a run since the last reload False, 798 s after it
exit=3
2026-10-29T14:50:47.435328536Z
NOT YET: archive failed, a run since the last reload False, 918 s after it
exit=3
2026-10-29T14:52:47.485132329Z
NOT YET: archive failed, a run since the last reload False, 1038 s after it
exit=3
2026-10-29T14:54:47.532878620Z
NOT YET: archive failed, a run since the last reload False, 1158 s after it
exit=3
2026-10-29T14:56:47.579108413Z
printed: btc-recorder.service before {"ActiveState": "active", "MainPID": "2388318", "NRestarts": "0", "UnitFileState": "enabled"} after {"ActiveState": "active", "MainPID": "2388318", "NRestarts": "0", "UnitFileState": "enabled"}
printed: btc-pairbook.service before {"ActiveState": "active", "MainPID": "3216422", "NRestarts": "12", "UnitFileState": "enabled"} after {"ActiveState": "active", "MainPID": "3216422", "NRestarts": "12", "UnitFileState": "enabled"}
printed: btc-rewardbook.service before {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1", "UnitFileState": "enabled"} after {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1", "UnitFileState": "enabled"}
printed: the archive ledger restart records 31 -> 31 | archive failed | a run since the last reload False | 1279 s after it
printed: the archive ledger, run 1793260762 records [('start', None, '2026-10-29T07:59:22.858185Z'), ('set', None, '2026-10-29T07:59:24.062054Z'), ('upload', None, '2026-10-29T08:00:56.315733Z'), ('deferred', 1, '2026-10-29T08:02:57.101110Z')] | lines that do not parse 0
G-STILL btc-recorder.service kept MainPID, NRestarts and active          PASS
G-STILL btc-rewardbook.service kept MainPID, NRestarts and active        PASS
G-STILL btc-pairbook.service active, restarted only by the archive       PASS
READING G-STILL: PASS - 3 of 3
exit=0
```

### 2.14 §3.12 — the closing reads (V18)

`adv3-bot.service` `active`, pid `3291955`, `NRestarts` 1, `Nice` 10, `Result=success`, `MemoryCurrent` 13,459,456 and
`MemoryPeak` 21,184,512 bytes, the second process's; `is-enabled` `enabled`. The three capture units as G-STILL read them; the
pair book's archive `failed` from its 07:59 deferral, the reward book's archive `inactive`; the timers next at 15:08:10 UTC
(the reward book's archive) and 2026-10-30 03:00:20 UTC (the pair book's). The unit's journal holds systemd's five lines:
the start at 14:38:10, the `SIGTERM` at 14:43:35, the deactivation, the restart job and the start at 14:44:05 UTC.
`service.log` holds the service's own five lines: the first process's start, its candles refreshed to the close of 2026-10-28
with none missing, the daily sent, the help sent in answer to the Boss's `/start`, and the second process's start reading
`daily-sent 2026-10-29`. There is no failure, no token and no chat id. `/var/lib/adv3-bot/` holds `daily-sent`, `journal.jsonl`,
`offset` and `service.log`, 1,640 bytes; `/etc/adv3-bot/` holds `chat-id` (10 bytes) and `token` (47 bytes), both `600`, root's.
`MemAvailable` 293,498,880 bytes; `/dev/vda2` 10,355,449,856 bytes free.

`logs/12-closing.log`, verbatim:

```
2026-10-29T14:57:01.670978217Z
MainPID=3291955
Result=success
NRestarts=1
MemoryCurrent=13459456
MemoryPeak=21184512
Nice=10
Id=adv3-bot.service
ActiveState=active
ActiveEnterTimestamp=Thu 2026-10-29 14:44:05 UTC

MainPID=2388318
Result=success
NRestarts=0
MemoryCurrent=171040768
MemoryPeak=303964160
Nice=0
Id=btc-recorder.service
ActiveState=active
ActiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC

MainPID=3216422
Result=success
NRestarts=12
MemoryCurrent=24285184
MemoryPeak=76881920
Nice=0
Id=btc-pairbook.service
ActiveState=active
ActiveEnterTimestamp=Thu 2026-10-29 03:05:31 UTC

MainPID=3137952
Result=success
NRestarts=1
MemoryCurrent=16125952
MemoryPeak=60887040
Nice=10
Id=btc-rewardbook.service
ActiveState=active
ActiveEnterTimestamp=Wed 2026-10-28 12:56:29 UTC

MainPID=0
Result=exit-code
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=[not set]
Nice=19
Id=btc-pairbook-archive.service
ActiveState=failed
ActiveEnterTimestamp=

MainPID=0
Result=success
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=28647424
Nice=19
Id=btc-rewardbook-archive.service
ActiveState=inactive
ActiveEnterTimestamp=
NEXT                         LEFT LAST                        PASSED UNIT                         ACTIVATES
Thu 2026-10-29 15:08:10 UTC 11min Thu 2026-10-29 08:47:07 UTC 6h ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Fri 2026-10-30 03:00:20 UTC   12h Thu 2026-10-29 07:59:22 UTC 6h ago btc-pairbook-archive.timer   btc-pairbook-archive.service

2 timers listed.
enabled
exit=0
2026-10-29T14:38:10+00:00 vultr systemd[1]: Started adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
2026-10-29T14:43:35+00:00 vultr systemd[1]: adv3-bot.service: Sent signal SIGTERM to main process 3290952 (python) on client request.
2026-10-29T14:43:35+00:00 vultr systemd[1]: adv3-bot.service: Deactivated successfully.
2026-10-29T14:44:05+00:00 vultr systemd[1]: adv3-bot.service: Scheduled restart job, restart counter is at 1.
2026-10-29T14:44:05+00:00 vultr systemd[1]: Started adv3-bot.service - ADV-3 advisor, the Boss's Binance Futures signals over Telegram.
2026-10-29T14:38:10Z serving the pinned chat: pid 3290952 offset 0 daily-sent -
2026-10-29T14:38:16Z candles refreshed to the close of 2026-10-28 | missing -
2026-10-29T14:38:17Z daily sent for the close of 2026-10-28
2026-10-29T14:38:17Z help sent
2026-10-29T14:44:05Z serving the pinned chat: pid 3291955 offset 685120810 daily-sent 2026-10-29
/etc/adv3-bot:
total 24
drwx------   2 root root  4096 Oct 29 14:34 .
drwxr-xr-x 130 root root 12288 Oct 29 14:20 ..
-rw-------   1 root root    10 Oct 29 14:34 chat-id
-rw-------   1 root root    47 Oct 29 14:21 token

/root/adv3-bot-svc:
total 68
drwxr-xr-x  2 root root  4096 Oct 29 14:31 .
drwx------ 30 root root  4096 Oct 29 14:31 ..
-rw-r--r--  1 root root 19365 Oct 29 14:31 adv3-bot.py
-rw-r--r--  1 root root 35479 Oct 29 14:31 adv3.py
-rw-r--r--  1 root root    41 Oct 29 14:31 commit.txt

/var/lib/adv3-bot:
total 24
drwx------  2 root root 4096 Oct 29 14:38 .
drwxr-xr-x 65 root root 4096 Oct 29 14:35 ..
-rw-r--r--  1 root root   10 Oct 29 14:38 daily-sent
-rw-r--r--  1 root root 1275 Oct 29 14:38 journal.jsonl
-rw-r--r--  1 root root    9 Oct 29 14:38 offset
-rw-r--r--  1 root root  346 Oct 29 14:44 service.log
               total        used        free      shared  buff/cache   available
Mem:      1002127360   708628480    77344768      385024   402305024   293498880
Swap:     3250581504   482930688  2767650816
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10355449856
10617884	/root/tz35-work
54885	/root/adv3-bot-svc
1640	/var/lib/adv3-bot
327493824	/var/lib/btc-rewardbook
1061817967	/var/lib/btc-pairbook
120266051	/root/.claude
{
 "host": {
  "free_bytes": 10457419776,
  "ledger_restarts": 31,
  "mem_available": 300171264,
  "ns": 1793283802130873653,
  "units": {
   "btc-pairbook.service": {
    "ActiveState": "active",
    "MainPID": "3216422",
    "NRestarts": "12",
    "UnitFileState": "enabled"
   },
   "btc-recorder.service": {
    "ActiveState": "active",
    "MainPID": "2388318",
    "NRestarts": "0",
    "UnitFileState": "enabled"
   },
   "btc-rewardbook.service": {
    "ActiveState": "active",
    "MainPID": "3137952",
    "NRestarts": "1",
    "UnitFileState": "enabled"
   }
  }
 },
 "marks": {
  "install": {
   "mono_ns": 7629027952907162,
   "ns": 1793284500231393034
  },
  "kill": {
   "mono_ns": 7629537575980097,
   "ns": 1793285009854466299,
   "unit": {
    "ActiveState": "active",
    "MainPID": "3290952",
    "NRestarts": "0"
   }
  },
  "start": {
   "mono_ns": 7629056813108981,
   "ns": 1793284529091595127,
   "unit": {
    "ActiveState": "inactive",
    "MainPID": "0",
    "NRestarts": "0"
   }
  }
 }
}
```

### 2.15 Contract §4.2's self-check (V17) — after the push and the pull request, before the report's commit

`logs/13-selfcheck.log`:

```
2026-10-29T14:57:13.561799975Z
fetch exit=0
$ git rev-list origin/main | grep -c 6c74b62bfef7afad2c71c742411124387327a588
0
$ git diff --name-only origin/main origin/tz-35-advisor-bot
.github/workflows/adv2-signal.yml
ADVISOR-SKILL.md
advisor/RULE-ADV-3.txt
advisor/adv3-bot.py
advisor/adv3.py
advisor/selftest-adv3.py
deploy/systemd/adv3-bot.service
research/tz35-advisor-deploy.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
grep exit=1
c2d5fc0b792b4bbb58fe963aa5491a735351915b
6c74b62bfef7afad2c71c742411124387327a588
pr 35 OPEN main <- tz-35-advisor-bot 6c74b62bfef7afad2c71c742411124387327a588 MERGEABLE
```

The first line prints `0`: the branch's commit is not on `main`. The second names the eight paths of the branch and
nothing else. The third prints nothing.

### 2.16 Every file the run and the session wrote, by SHA-256, but the bot's own root

Under `/root/tz35-work/`, its branch worktree aside — whose six files are Appendix A's, by §2.1's hashes — and the
service's copy and the installed unit. **Not listed:** `/var/lib/adv3-bot/`, the bot's root (§8); `/etc/adv3-bot/chat-id`,
written by `--find-chat`, whose hash would print the chat id in another form (§2 item 5) — its mode, owner and size
alone are in §2.9; the enable link, a symlink to the unit; and the forensic store's copies, §2.17's, each equal to its
source by `reclaim`'s own hash. The builder `report/build.py` assembles this report from `report/template.md` and the
logs.

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `/root/tz35-work/commit-msg.txt` | 14 | 1,274 | `d324fa51eba5a4a0e2e80e76e517e526d17c4b1ef23fdc84b08b92be501276fb` |
| `/root/tz35-work/history.json` | 838 | 19,362 | `bcee53097f9f1a5820b551c90054a3f046c027f53cff868b857be3118c74faa1` |
| `/root/tz35-work/ls-remote-0.txt` | 83 | 5,760 | `ef68b731a7fcd15d97635aab64aa24bf97d3ac9b5034ece2165a48c1af0d6402` |
| `/root/tz35-work/ls-remote-1.txt` | 83 | 5,760 | `ef68b731a7fcd15d97635aab64aa24bf97d3ac9b5034ece2165a48c1af0d6402` |
| `/root/tz35-work/pr-body.md` | 18 | 1,278 | `519983deb454a14f384034272395b02fab0f2ae49f6a57a46fb8e4d6fe4b97d4` |
| `/root/tz35-work/state.json` | 52 | 1,018 | `3f2fbf8128ae0d56fac3eaf5269bd0339484f404917ffc7adcf60e264918d206` |
| `/root/tz35-work/logs/00-mkdir.log` | 3 | 194 | `e597ed52c552437ea3efdafb9f0b880c9dd0b6d9364d940b52d84f70aaf5e54f` |
| `/root/tz35-work/logs/00-startup.log` | 12 | 795 | `92d7e7c4f87fe163737a3679a6768844b946534fd4b124894fe7980a50b5de65` |
| `/root/tz35-work/logs/00a-stage.log` | 8 | 762 | `0ffa3d2d5d9a2c93e8f6c2acdeaa3e2815ee941ab08adde8669c1f2314de026c` |
| `/root/tz35-work/logs/00b-fingerprint.log` | 57 | 7,521 | `bd9d902881e8b408a571a3e684fa8b50518a6ec68361f3ad714216f8af1a84e6` |
| `/root/tz35-work/logs/00c-host-2.log` | 157 | 5,690 | `d6410e2973c799762fa5296bbf9f7cb2f4abae2fcf9737677d369a7fafece4a8` |
| `/root/tz35-work/logs/00c-host.log` | 166 | 6,241 | `f6c3f3bb88fd8d621e3d1c90e0c0c680722b661fa849076e40c8d8a3a1b579d6` |
| `/root/tz35-work/logs/00d-number.log` | 107 | 6,828 | `452464f780cab9b1664f55e1e86e210f423fe2170fcaf6de342e1c2504ac4723` |
| `/root/tz35-work/logs/01-branch.log` | 11 | 577 | `7853f63f5d276290e004993f8274b35a418ada64d1c9ef6edcd8d94aad5d5547` |
| `/root/tz35-work/logs/01a-branch-files.log` | 27 | 1,217 | `0115fab0d9f7ea0b29222adef3fe2f511ff8ee806145b014e4dc2261a4a9da98` |
| `/root/tz35-work/logs/01b-commit.log` | 14 | 714 | `d82db2f136ddfb71c97306190835b3dc9b1f6e3e7633fe6bbfb1168ee48063e9` |
| `/root/tz35-work/logs/01c-push.log` | 13 | 599 | `eb399320f69a9b8cac76afacfe5d189d3dd77d61c5134baa1ce4301f41ecead9` |
| `/root/tz35-work/logs/01d-pr.log` | 3 | 97 | `81ba8116a9c65b298ba5455cb7b4b08e0d17e68864ab7fdb94a5cedae355db45` |
| `/root/tz35-work/logs/02-selftests.log` | 11 | 364 | `ef3fb99ae9d9d9cf9dd92268d30ca6de50e5a1b9a846a4a0b8905678d4718aaf` |
| `/root/tz35-work/logs/03-scratch.log` | 8 | 524 | `b378c9ce0a5a4d29c0beb3b959dcec5fac5371bb780f5793c9d189fee29ab116` |
| `/root/tz35-work/logs/03a-reclaim-scratch.log` | 4 | 230 | `7b9c2ba49cfb1223a0f16c2b7bbc3f53d6c6ea0a4b80340a4381e507b3cea3d6` |
| `/root/tz35-work/logs/03b-rm-scratch.log` | 6 | 90 | `74fcbe41ad3418913c6a3d91794c83888dcf0b56f0e7c679bb3e59020c225318` |
| `/root/tz35-work/logs/04-g-same.log` | 6 | 678 | `d7a6909b0d1907a49fdf82b7557f6cc2a3c1c4577949146d3dd0adef81c3a4d4` |
| `/root/tz35-work/logs/04a-g-history.log` | 26 | 1,902 | `a67f4de9cb07e26bfc13d7531d3e6d0fc9af6461050cbcb7fa7a3eba2619d4d3` |
| `/root/tz35-work/logs/05-copy.log` | 18 | 823 | `994777e8ebab4be3771da845879c548c68d27a9098c7236cbdfcd97bd835fb76` |
| `/root/tz35-work/logs/06-probe.log` | 9 | 469 | `351c549e22073bae94d3211e4ab157895e7e73646d10078bda169c777f199e4e` |
| `/root/tz35-work/logs/07-boss-told.log` | 1 | 143 | `8d9739a13b8363eb7efcbed0c5a6825971a84349ebcd48be9d337e3d0b0970ee` |
| `/root/tz35-work/logs/07-find-chat.log` | 5 | 232 | `3000485ea23e132e4205449506dc8ed4e7049939bd8d32d65a5eef19f86d6f01` |
| `/root/tz35-work/logs/07a-hello.log` | 4 | 102 | `14ef7d5a86cc639e5871d5e0e660c3ef6d035f1a7befbf6b3d242a57d00ca9b8` |
| `/root/tz35-work/logs/08-b-install.log` | 3 | 52 | `d14a2b28fbd02d28835ce42c484109c05b42878c8c27c33e9efe0e4f67f1156f` |
| `/root/tz35-work/logs/08-band.log` | 2 | 55 | `d5ae35b9846aacd6854c68abb1c695fae801dfad8bd61bcc171881dcc2d541a3` |
| `/root/tz35-work/logs/08-mark-install.log` | 2 | 51 | `1818eeabe5f30a8443c67fd036e100aa468fa2691620dde04a62fd07243f440f` |
| `/root/tz35-work/logs/08a-props.log` | 20 | 1,602 | `c997eccbf11574b2cff3bc934bd889f96b1637233eeede53180bc1b62da89e45` |
| `/root/tz35-work/logs/09-b-enable-refused.log` | 1 | 276 | `719d212cfee58c7049ba0f8c9d6c733bc4abac126697224989f73bb41e0db1e0` |
| `/root/tz35-work/logs/09-b-enable.log` | 3 | 157 | `fa2a9b09dadc17ad3a0c9ccde7abb8bb7a817887d75fb52927ba27db17962fd9` |
| `/root/tz35-work/logs/09-mark-start.log` | 2 | 108 | `11c5ecb3a89535ff7d4b8a498d2924caf49feced28041f2717144ede4fd3ee14` |
| `/root/tz35-work/logs/09a-unit-0.log` | 22 | 1,865 | `bdd6c9972126b55577034bd5b9e766ece7d4152b690d76009abd52c886dcb037` |
| `/root/tz35-work/logs/09b-daily.log` | 15 | 1,016 | `ae58147ac229a1737d4747248f762f46d1c7188110b349bf38d21bd716c7fbb3` |
| `/root/tz35-work/logs/09c-load.log` | 8 | 454 | `18d30ffe76dda3cbd747595c9b73b8e3ce7d4d1cfc00dfc051bc197fdb45f3bf` |
| `/root/tz35-work/logs/10-b-kill.log` | 2 | 38 | `9ac78ad79e33feb17ab2db9c9873c3bd8b36dcc635d41cf4c2fa1f99fb8304e7` |
| `/root/tz35-work/logs/10-mark-kill.log` | 2 | 111 | `eb2b1e945de3c7816a04a3c3af79c7d59fe3599787c9ab7e146bb0efe0572b90` |
| `/root/tz35-work/logs/10a-restart.log` | 12 | 732 | `d7a126b45b03001eaed104454f24a1e2d9916e7b9aac75da584034dea942d4d1` |
| `/root/tz35-work/logs/10b-unit-1.log` | 22 | 1,865 | `be98778aa93ff18477695ca4f96fa5f20ea88e7d664c1f741a74dd0ff0906c87` |
| `/root/tz35-work/logs/11-still.log` | 29 | 2,076 | `06d0ca83e897d91b4dd8a0c4754e781ebd2ae788d1fef90486c7bdc8c3ecd03e` |
| `/root/tz35-work/logs/12-closing.log` | 163 | 4,754 | `824b002494ceb0900917b533faeab63ce67a20a09119db068c916f47ca91df78` |
| `/root/tz35-work/logs/13-selfcheck.log` | 18 | 634 | `7aa36eb8d018daa63351ba91c3ba9a562dabe339ec4fb622c1d9c07f1043c294` |
| `/root/tz35-work/report/build.py` | 64 | 2,560 | `43a8cd46f6cd57712d7a833452850ad9f2a90abdfa5fc6c37b46dd69345438b4` |
| `/root/tz35-work/report/template.md` | 540 | 30,211 | `211bab9af5454bd0fc713332209b0f6197d7aeff2df5b15bfa1d3221f3c0736c` |
| `/root/tz35-work/stage/advisor/RULE-ADV-3.txt` | 33 | 3,203 | `ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169` |
| `/root/tz35-work/stage/advisor/adv3-bot.py` | 422 | 19,365 | `e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb` |
| `/root/tz35-work/stage/advisor/adv3.py` | 718 | 35,479 | `7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb` |
| `/root/tz35-work/stage/advisor/selftest-adv3.py` | 155 | 8,909 | `76bad371727e0d4bf13c1d009f1b8f9412133a33788c456ecd53d1f83df6f0e6` |
| `/root/tz35-work/stage/deploy/systemd/adv3-bot.service` | 27 | 863 | `82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66` |
| `/root/tz35-work/stage/research/tz35-advisor-deploy.py` | 802 | 42,049 | `d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5` |
| `/root/adv3-bot-svc/adv3.py` | 718 | 35,479 | `7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb` |
| `/root/adv3-bot-svc/adv3-bot.py` | 422 | 19,365 | `e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb` |
| `/root/adv3-bot-svc/commit.txt` | 1 | 41 | `c7fa5d183b09e3b3fc93d7dbf78d205361d3e8d62c4162e2298f0be998021089` |
| `/etc/systemd/system/adv3-bot.service` | 27 | 863 | `82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66` |

### 2.17 §9 B-RECLAIM-OWN — last, after §3.12, with this report drafted (V19, V20)

Run from the session, its output written to no file and quoted here verbatim, every line:

```
$ cd /root/tz35-work && date -u +%FT%T.%NZ && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz35-work/wt/research/tz35-advisor-deploy.py reclaim /root/tz35-work; echo "exit=$?"
2026-10-29T14:58:03.481768809Z
reclaim: 3474 report tokens; forensic store holds 2151 files
reclaim: /root/tz35-work/wt skipped: no file but its HEAD's, and HEAD 6c74b62bfef7afad2c71c742411124387327a588 is its upstream's
R copied d324fa51eba5a4a0e2e80e76e517e526d17c4b1ef23fdc84b08b92be501276fb /root/btc-forensics/tz35-work--commit-msg.txt
R copied bcee53097f9f1a5820b551c90054a3f046c027f53cff868b857be3118c74faa1 /root/btc-forensics/tz35-work--history.json
R copied ef68b731a7fcd15d97635aab64aa24bf97d3ac9b5034ece2165a48c1af0d6402 /root/btc-forensics/tz35-work--ls-remote-0.txt
R copied ef68b731a7fcd15d97635aab64aa24bf97d3ac9b5034ece2165a48c1af0d6402 /root/btc-forensics/tz35-work--ls-remote-1.txt
R copied 519983deb454a14f384034272395b02fab0f2ae49f6a57a46fb8e4d6fe4b97d4 /root/btc-forensics/tz35-work--pr-body.md
R copied 3f2fbf8128ae0d56fac3eaf5269bd0339484f404917ffc7adcf60e264918d206 /root/btc-forensics/tz35-work--state.json
R copied e597ed52c552437ea3efdafb9f0b880c9dd0b6d9364d940b52d84f70aaf5e54f /root/btc-forensics/tz35-work--logs--00-mkdir.log
R copied 92d7e7c4f87fe163737a3679a6768844b946534fd4b124894fe7980a50b5de65 /root/btc-forensics/tz35-work--logs--00-startup.log
R copied 0ffa3d2d5d9a2c93e8f6c2acdeaa3e2815ee941ab08adde8669c1f2314de026c /root/btc-forensics/tz35-work--logs--00a-stage.log
R copied bd9d902881e8b408a571a3e684fa8b50518a6ec68361f3ad714216f8af1a84e6 /root/btc-forensics/tz35-work--logs--00b-fingerprint.log
R copied d6410e2973c799762fa5296bbf9f7cb2f4abae2fcf9737677d369a7fafece4a8 /root/btc-forensics/tz35-work--logs--00c-host-2.log
R copied f6c3f3bb88fd8d621e3d1c90e0c0c680722b661fa849076e40c8d8a3a1b579d6 /root/btc-forensics/tz35-work--logs--00c-host.log
R copied 452464f780cab9b1664f55e1e86e210f423fe2170fcaf6de342e1c2504ac4723 /root/btc-forensics/tz35-work--logs--00d-number.log
R copied 7853f63f5d276290e004993f8274b35a418ada64d1c9ef6edcd8d94aad5d5547 /root/btc-forensics/tz35-work--logs--01-branch.log
R copied 0115fab0d9f7ea0b29222adef3fe2f511ff8ee806145b014e4dc2261a4a9da98 /root/btc-forensics/tz35-work--logs--01a-branch-files.log
R copied d82db2f136ddfb71c97306190835b3dc9b1f6e3e7633fe6bbfb1168ee48063e9 /root/btc-forensics/tz35-work--logs--01b-commit.log
R copied eb399320f69a9b8cac76afacfe5d189d3dd77d61c5134baa1ce4301f41ecead9 /root/btc-forensics/tz35-work--logs--01c-push.log
R copied 81ba8116a9c65b298ba5455cb7b4b08e0d17e68864ab7fdb94a5cedae355db45 /root/btc-forensics/tz35-work--logs--01d-pr.log
R copied ef3fb99ae9d9d9cf9dd92268d30ca6de50e5a1b9a846a4a0b8905678d4718aaf /root/btc-forensics/tz35-work--logs--02-selftests.log
R copied b378c9ce0a5a4d29c0beb3b959dcec5fac5371bb780f5793c9d189fee29ab116 /root/btc-forensics/tz35-work--logs--03-scratch.log
R copied 7b9c2ba49cfb1223a0f16c2b7bbc3f53d6c6ea0a4b80340a4381e507b3cea3d6 /root/btc-forensics/tz35-work--logs--03a-reclaim-scratch.log
R copied 74fcbe41ad3418913c6a3d91794c83888dcf0b56f0e7c679bb3e59020c225318 /root/btc-forensics/tz35-work--logs--03b-rm-scratch.log
R copied d7a6909b0d1907a49fdf82b7557f6cc2a3c1c4577949146d3dd0adef81c3a4d4 /root/btc-forensics/tz35-work--logs--04-g-same.log
R copied a67f4de9cb07e26bfc13d7531d3e6d0fc9af6461050cbcb7fa7a3eba2619d4d3 /root/btc-forensics/tz35-work--logs--04a-g-history.log
R copied 994777e8ebab4be3771da845879c548c68d27a9098c7236cbdfcd97bd835fb76 /root/btc-forensics/tz35-work--logs--05-copy.log
R copied 351c549e22073bae94d3211e4ab157895e7e73646d10078bda169c777f199e4e /root/btc-forensics/tz35-work--logs--06-probe.log
R copied 8d9739a13b8363eb7efcbed0c5a6825971a84349ebcd48be9d337e3d0b0970ee /root/btc-forensics/tz35-work--logs--07-boss-told.log
R copied 3000485ea23e132e4205449506dc8ed4e7049939bd8d32d65a5eef19f86d6f01 /root/btc-forensics/tz35-work--logs--07-find-chat.log
R copied 14ef7d5a86cc639e5871d5e0e660c3ef6d035f1a7befbf6b3d242a57d00ca9b8 /root/btc-forensics/tz35-work--logs--07a-hello.log
R copied d14a2b28fbd02d28835ce42c484109c05b42878c8c27c33e9efe0e4f67f1156f /root/btc-forensics/tz35-work--logs--08-b-install.log
R copied d5ae35b9846aacd6854c68abb1c695fae801dfad8bd61bcc171881dcc2d541a3 /root/btc-forensics/tz35-work--logs--08-band.log
R copied 1818eeabe5f30a8443c67fd036e100aa468fa2691620dde04a62fd07243f440f /root/btc-forensics/tz35-work--logs--08-mark-install.log
R copied c997eccbf11574b2cff3bc934bd889f96b1637233eeede53180bc1b62da89e45 /root/btc-forensics/tz35-work--logs--08a-props.log
R copied 719d212cfee58c7049ba0f8c9d6c733bc4abac126697224989f73bb41e0db1e0 /root/btc-forensics/tz35-work--logs--09-b-enable-refused.log
R copied fa2a9b09dadc17ad3a0c9ccde7abb8bb7a817887d75fb52927ba27db17962fd9 /root/btc-forensics/tz35-work--logs--09-b-enable.log
R copied 11c5ecb3a89535ff7d4b8a498d2924caf49feced28041f2717144ede4fd3ee14 /root/btc-forensics/tz35-work--logs--09-mark-start.log
R copied bdd6c9972126b55577034bd5b9e766ece7d4152b690d76009abd52c886dcb037 /root/btc-forensics/tz35-work--logs--09a-unit-0.log
R copied ae58147ac229a1737d4747248f762f46d1c7188110b349bf38d21bd716c7fbb3 /root/btc-forensics/tz35-work--logs--09b-daily.log
R copied 18d30ffe76dda3cbd747595c9b73b8e3ce7d4d1cfc00dfc051bc197fdb45f3bf /root/btc-forensics/tz35-work--logs--09c-load.log
R copied 9ac78ad79e33feb17ab2db9c9873c3bd8b36dcc635d41cf4c2fa1f99fb8304e7 /root/btc-forensics/tz35-work--logs--10-b-kill.log
R copied eb2b1e945de3c7816a04a3c3af79c7d59fe3599787c9ab7e146bb0efe0572b90 /root/btc-forensics/tz35-work--logs--10-mark-kill.log
R copied d7a126b45b03001eaed104454f24a1e2d9916e7b9aac75da584034dea942d4d1 /root/btc-forensics/tz35-work--logs--10a-restart.log
R copied be98778aa93ff18477695ca4f96fa5f20ea88e7d664c1f741a74dd0ff0906c87 /root/btc-forensics/tz35-work--logs--10b-unit-1.log
R copied 06d0ca83e897d91b4dd8a0c4754e781ebd2ae788d1fef90486c7bdc8c3ecd03e /root/btc-forensics/tz35-work--logs--11-still.log
R copied 824b002494ceb0900917b533faeab63ce67a20a09119db068c916f47ca91df78 /root/btc-forensics/tz35-work--logs--12-closing.log
R copied 7aa36eb8d018daa63351ba91c3ba9a562dabe339ec4fb622c1d9c07f1043c294 /root/btc-forensics/tz35-work--logs--13-selfcheck.log
R copied 43a8cd46f6cd57712d7a833452850ad9f2a90abdfa5fc6c37b46dd69345438b4 /root/btc-forensics/tz35-work--report--build.py
R copied 211bab9af5454bd0fc713332209b0f6197d7aeff2df5b15bfa1d3221f3c0736c /root/btc-forensics/tz35-work--report--template.md
R copied ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169 /root/btc-forensics/tz35-work--stage--advisor--RULE-ADV-3.txt
R copied e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb /root/btc-forensics/tz35-work--stage--advisor--adv3-bot.py
R copied 7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb /root/btc-forensics/tz35-work--stage--advisor--adv3.py
R copied 76bad371727e0d4bf13c1d009f1b8f9412133a33788c456ecd53d1f83df6f0e6 /root/btc-forensics/tz35-work--stage--advisor--selftest-adv3.py
R copied 82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66 /root/btc-forensics/tz35-work--stage--deploy--systemd--adv3-bot.service
R copied d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5 /root/btc-forensics/tz35-work--stage--research--tz35-advisor-deploy.py
RECLAIM PASS: 54 files considered, 54 named by a report, 0 kept by name, 54 copied, 0 already held; forensic store 2151 -> 2205 files
exit=0

$ date -u +%FT%T.%NZ; git -C /root/btc-5m-twap worktree remove /root/tz35-work/wt; echo "exit=$?"
2026-10-29T14:58:08.234409897Z
exit=0

$ date -u +%FT%T.%NZ; rm -rf /root/tz35-work; echo "exit=$?"; test -e /root/tz35-work; echo "exit=$?"
2026-10-29T14:58:13.224041685Z
exit=0
exit=1

$ date -u +%FT%T.%NZ; git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list; find /root/btc-forensics -type f | wc -l; df -B1 --output=source,size,avail /var/lib/btc-recorder
2026-10-29T14:58:17.101310724Z
/root/btc-5m-twap       c2d5fc0 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
2205
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10356695040
```

**`RECLAIM PASS`: 54 files considered, 54 named by this report, 0 kept by name alone, 54 copied, 0 already held; the
store `2,151 → 2,205`, its count after equal to before plus the 54 copies.** The worktree removed without `--force`,
`exit=0`; `rm -rf /root/tz35-work` `exit=0` and `test -e` `exit=1`, no refusal; `git worktree list` names
`/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else; `/dev/vda2` 10,356,695,040 bytes free at 14:58:17 UTC.
The branch `tz-35-advisor-bot` stays on `origin` and as a local ref. **Kept:** `/root/adv3-bot-svc/`, the running unit's
code; `/var/lib/adv3-bot/`, its record; `/etc/adv3-bot/`, the Boss's token and the pinned chat.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-35-advisor-bot` at `6c74b62bfef7afad2c71c742411124387327a588`, pushed to `origin` through the remote URL's own credential |
| pull request | #35, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/35`, against `main`, open, not merged |
| the branch's diff | 8 paths: `A` `advisor/RULE-ADV-3.txt`, `advisor/adv3.py`, `advisor/adv3-bot.py`, `advisor/selftest-adv3.py`, `deploy/systemd/adv3-bot.service`, `research/tz35-advisor-deploy.py`; `D` `ADVISOR-SKILL.md`, `.github/workflows/adv2-signal.yml` |
| Release | none — none is created by this TZ (§2 item 8) |
| report | this file, `CryptoReports/TZ-35-advisor-bot-report.md`, the one path pushed to `main`, in one commit |
| separation self-check | §2.15: `0`; the eight paths; nothing |

---

## 4. Gate

| gate | PASS, as §4 fixes it | read | verdict |
|---|---|---|---|
| **NUMBER** | 2 of 2, at §0.5 and at §3.1 | 2 of 2, 2 of 2 | **PASS** |
| **G-SAME** | no candle differs, at least 12 compared a coin | 0 mismatches of 546; the least `13.000` | **PASS** |
| **G-HISTORY** | 16 of 16 equal, the file's bytes the Architect's | 16 of 16; 19,362 bytes, `bcee5309…` | **PASS** |
| **COPY** | 4 of 4 | 4 of 4 | **PASS** |
| **P-START** | 5 endpoints served and parsed | 5 of 5 | **PASS** |
| **G-CHAT**, **G-HELLO** | one private chat; a message id | 1; `[5]` | **PASS** |
| **PROPS** | 11 of 11 | 11 of 11 | **PASS** |
| **G-UNIT** | 18 of 18 at 0 and at 1 restart | 18 of 18, 18 of 18 | **PASS** |
| **G-DAILY**, **G-REPLY** | 8 of 8 and 1 of 1 | 8 of 8, 1 of 1 | **PASS** |
| **G-LOAD** | processor at most `0.050` of the wall time, at least 300 s | `0.003` over 311.0 s | **PASS** |
| **G-RESTART**, **G-ONCE** | 5 of 5 and 2 of 2 | 5 of 5, 2 of 2; the restart `35.266` s after the mark against `60` | **PASS** |
| **G-STILL** | 3 of 3 | 3 of 3; the ledger's restart records 31 → 31 | **PASS** |

Nothing was tuned to reach any gate, and no gate is read otherwise than §4 writes it. **Under PASS K-35 is not run, and
the bot runs on after the session.**

---

## 5. Validation

| # | check | count | asserted |
|---|---|---|---|
| **V1** | §0.2's fingerprint | `FINGERPRINT PASS`: revision `2026-10-29-a`; anchors 6 of 6, 4 re-derived; 49 rows, 46 of 46 `frozen` equal, 2 `tracked`, 1 `reported` (§0.1) | asserted, `mode_fingerprint` |
| **V2** | §0.3's host gate | `READING HOST: PASS - 12 of 12` at the second reading; the first `FAIL - 11 of 12`, H6 (§0.3, §6 item 1) | asserted, `verdict` |
| **V3** | NUMBER at §0.5 and at §3.1 | `READING NUMBER: PASS - 2 of 2` each, the one `TZ-35-` path `CryptoTZ/TZ-35-advisor-bot.md` printed | asserted, `verdict` |
| **V4** | §0.1's and §3.1's files | 6 of 6 hashes asserted at each, lines and bytes equal; the branch's diff exactly 6 `A` and 2 `D` paths, 8 lines | the hashes asserted by §0.1's script; the 8 lines read against §3.1 by the Executor |
| **V5** | the self-tests | `32 of 32`, `19 of 19`, `24 of 24` | asserted, each test's `check` |
| **V6** | G-SAME | `READING G-SAME: PASS`, 42 coins, 13 compared each, the least 13, 1 file absent each, 0 mismatches | exit `0` only on PASS |
| **V7** | G-HISTORY and DETERMINISM | `16 of 16 equal`; 19,362 bytes, SHA-256 `bcee5309…` | the 16 by exit `0`; the bytes read against §3.4 by the Executor from `sha256sum` and `wc -c` |
| **V8** | COPY | 4 of 4 | asserted, `verdict` |
| **V9** | P-START | `served - 5 of 5 endpoints`, each line printed | asserted, `probe` |
| **V10** | G-CHAT, G-HELLO | one private chat pinned; message ids `[5]`; the file `600 root` | `find_chat` exits 1 otherwise; `hello` asserts the ids; the mode read by the Executor from `stat` |
| **V11** | B-INSTALL and PROPS | `exit=0`; `verify exit=0`, no finding; `11 of 11` | PROPS asserted; the exits read by the Executor |
| **V12** | G-UNIT at `0` and at `1` | 18 of 18 each | asserted, `verdict` |
| **V13** | G-DAILY, G-REPLY | 8 of 8, 1 of 1; TOP-3 XMR, BTW, GRAM; STRONG XMR; the cards printed | asserted, `verdict` |
| **V14** | G-LOAD | `0.003` against `0.05`, over 311.0 s; `MemoryCurrent` 37,404,672, `MemoryPeak` 39,378,944, `VmRSS` 48,328 kB, `VmHWM` 50,084 kB, no swap | asserted, `verdict` |
| **V15** | G-RESTART, G-ONCE | 5 of 5, 2 of 2; pids 3290952 and 3291955 | asserted, `verdict` |
| **V16** | G-STILL | 3 of 3; each unit before (14:23:21 UTC) and after (14:56:47 UTC) printed; the ledger's restart records 31 → 31; the deferred set's four records at §0.3 and §3.11 equal | asserted, `verdict` |
| **V17** | contract §4.2's self-check | §2.15, after the push and the pull request and before the report's commit | the three lines read by the Executor |
| **V18** | §3.12's closing reads | every read printed, §2.14 | recorded, not asserted |
| **V19** | §9's `reclaim` runs | B-RECLAIM-SCRATCH §2.4: 4 considered, 0 named, 0 kept by name, 0 copied, 0 held, 2,151 → 2,151; B-RECLAIM-OWN §2.17 | asserted, `mode_reclaim` |
| **V20** | §9's removals | §2.4's two `rm -rf`, `test -e` `exit=1` each; §2.17's `git worktree remove` without `--force`, `rm -rf /root/tz35-work`, `test -e`, `git worktree list` | the exits read by the Executor |

---

## 6. What could not be implemented as written

1. **H6 failed at the first host gate, and the host gate was read twice.** §0.6 has the Boss create the bot, write its
   token to `/etc/adv3-bot/token` and press Start before `EXECUTE TZ-35`. At 14:15:26 UTC `/etc/adv3-bot` did not exist,
   and `I0 host` printed `READING HOST: FAIL - 11 of 12`, which §0.3 makes BLOCKED. Contract §5.3 says missing credentials
   are resolved before the run, not reported after it. Nothing but `/root/tz35-work/` had been written. So the Executor
   gave the Boss §0.6's command verbatim, told him never to paste the token into the chat, and asked whether to file
   BLOCKED or wait for the steps. He chose the steps. The Executor then waited in a background loop for the token file to
   exist, reading its mode, owner, size and type alone, never its content. It saw the file by 14:22:30 UTC: the directory
   `700 root`, the token a `600 root` regular file of 47 bytes. §0.3's whole block then ran again into `logs/00c-host-2.log` at
   14:23:21 UTC, `PASS - 12 of 12`. Both readings are quoted. The second `I0 host` overwrote `state.json`'s `host`
   record, so G-STILL counts from 14:23:21 UTC; the three capture units read the same pids and `NRestarts` at both. The
   Boss's `/start` came after §3.7's `--find-chat` began waiting, as §3.7 provides for.
2. **B-ENABLE was refused to the Executor and run by the Boss**, as §3 provides: `[Unauthorized Persistence]`, the fifth
   refusal of `systemctl enable --now` (map §6). The `start` mark was taken at 14:35:29.092 UTC, immediately before the
   Executor's attempt, as §3 asks of the attempt. It could not be taken again (`mark` refuses a second), so it stands
   2 min 41 s before the Boss's run at 14:38:10.055 UTC. G-DAILY and G-REPLY read from that mark less 1 s, a span the
   unit had not started in. `still` measures its 1,200 s from that mark, so the wait ended 1,039 s after the enable's
   reload rather than 1,200 s; `list-timers` at 14:44:39 UTC and every `I still` show the pair book's archive not re-armed
   by it. The block was handed over as one line, its band open, with the log it appends to. The Boss reported "done",
   and the Executor verified it through `systemctl show` and the checker, never from his account.
3. **The logs' names.** §3 fixes `08-b-install.log`, `09-b-enable.log`, `10-b-kill.log`, `k35.log` and
   `b-uninstall.log`, so §3.N's steps are numbered `NN` = N, with letter suffixes for the steps inside one section.
   §0's steps are `00-…` and `00a` to `00d`. `00-startup.log` and `00-mkdir.log` were written by hand after their
   commands, `logs/` not existing before §0.0. `07-boss-told.log` and `09-b-enable-refused.log` are the Executor's notes,
   written by hand.
4. **Timing wrappers.** The three self-tests, G-SAME and G-HISTORY ran under `/usr/bin/time` to print their processor
   time and peak memory beside their output (map §7 item 131 asks for host peaks). The commands are otherwise
   verbatim, `timeout` and `nice` included. G-HISTORY's host peak, 70,344 kB, is below the Architect's 85,172,224 bytes.
5. **Contract §1 steps 1 and 2.** `git fetch origin main` and `git merge --ff-only origin/main` ran first, at about
   14:12 UTC, then `git checkout main && git pull`, recorded in `00-startup.log`. The TZ and the contract were read in
   full. `SYSTEM-MAP.md` was read in the sections this TZ rests on: §0, the head of §1, §2.6, §6, §7 items 114 to 131 and
   the head of §8, not every line. The fingerprint read every row of §0's table.
6. **Reads no step names**, none under a capture's store: `git config`, `gh auth status`, `git log` of earlier commits'
   authors, the TZ file's `wc` and `sha256sum`, and `state.json` printed. One `systemctl show adv3-bot.service` at
   14:38:36 UTC to verify B-ENABLE, and one `list-timers` of both archives at 14:44:39 UTC. `stat` of `/etc/adv3-bot`
   and its token while waiting for the Boss, mode, owner, size and type alone.
7. **Files in the work tree beyond the TZ's list**, each kept by hash in §2.16: `ls-remote-0.txt` and `ls-remote-1.txt`,
   the two ref reads; `commit-msg.txt` and `pr-body.md`, the commit's message and the pull request's body; and
   `report/build.py` and `report/template.md`, which built this report. The harness kept its own records of the
   session's background commands under the session's directory in `/tmp`, outside its scratchpad. The Executor wrote
   nothing to the scratchpad.
8. **The commit message and the pull request's text** are the Executor's own wording. The commit's author is git's
   default on this host, `root <root@vultr.guest>`, as for TZ-34's.
9. **B-RECLAIM-OWN in four calls**, each after a `date -u`: `reclaim`; `git worktree remove`; `rm -rf` and `test -e`;
   then `prune`, `list`, the store's count and `df`. In order, none refused, every line quoted in §2.17. A refusal of one
   call would not discard the others. Two scratch files in `/dev/shm` served the paste: the quoted block itself, and its
   54 `R copied` lines checked by `sha256sum -c` against the store's copies (`check exit=0`, 54 `tz35-work--` files).
   Both were removed after.

None moves a reading: the code under test, the checker and the unit are fixed by Appendix A's hashes, and every gate
was read by the checker's or the bot's own modes.
