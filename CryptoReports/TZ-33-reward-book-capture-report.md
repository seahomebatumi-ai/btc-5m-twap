# TZ-33 report — L0's capture: the reward book, the books and trades of the day's reward markets, streamed

**P-START: served** — 6 requests and 1 stream session on the listing's two richest markets of its first page, 7 of 7 session checks True, at both runs: 06:34 UTC and, after B-ENABLE's first hand-over lapsed, 11:01 UTC into `prestart-2`.
**B-ENABLE was run by the Boss**, because the session's classifier refused it; the first hand-over lapsed when the Boss's login ended before the band, and the second started the unit at 11:30:15 UTC. **G-UNIT PASS** at 0 restarts, 11 of 11 · **G-START PASS**, 8 of 8.
**G-SELECT PASS**, 1 of 1 day re-derived equal with 150 members · **G-STREAM PASS, 4 of 4** qualifying slots complete · **G-REWARDS PASS, 1800 of 1800** polls served · **G-NEIGHBORS PASS (HOLD)**: 14 recorder intervals and 5 pair book windows counted, 0 failing · **G-LOAD PASS**: `0.0262` of one core, against `0.10`.
**G-RESTART PASS**: the `SIGTERM` stop of `3119051`, then the start of `3137952` 5.831 s later; G-UNIT 11 of 11 at 1 restart · **G-RESUME PASS**: slot 13:00 UTC complete · **G-STILL PASS**: the recorder unchanged, the pair book moved by the archive's two restarts alone.
**The reward book runs**, as `btc-rewardbook.service`, pid `3137952`, `NRestarts` 1, `active` and `enabled`, verified by `I final` and by §3.11's `systemctl show`, `is-enabled` and `journalctl`, not from the Boss's account. K-33 was not run.
**Departures, all in §6:** B-RECLAIM-SCRATCH's four directories removed by the Boss with no `RECLAIM PASS` on record before the removal; B-ENABLE's lapsed first hand-over and P-START's second run; and two runs of the archive off its calendar, which B-INSTALL's `daemon-reload` and B-ENABLE's `enable` set off.
**The stream's measured rate**, over G-STREAM's four slots: **96.0 frames a second, 10,584,064 stored bytes a slot**, 1,016,070,120 a day, so **3.88 days to `STREAM_CAP`** from the store's streams at `prove`'s read.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-33-reward-book-capture.md`, 4,485 lines, 264,353 bytes, SHA-256 `fb4375198deda5198d2d4b2e0321339472150b06fc67b52d3ffe6943e077cb9d`, landed at `adba104` |
| map revision | `2026-10-27-b`, equal; anchors 6 of 6; re-derived 4 of 4; rows 44; `frozen` equal 41 of 41 |
| executor model | Opus, as the TZ names: `get_session` read `session_context.model` and `last_served_model` as `claude-opus-5-5` (`logs/06-model.log`) |
| branch | `tz-33-reward-book-capture` at `2dcd70e08b18b93c64bb67d9849ac1216ce40e41`, pushed; pull request #32, open, not merged |
| instrument | `research/tz33-reward-book-capture.py`, 3,542 lines, 175,160 bytes, SHA-256 `a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670`, Appendix A byte for byte |
| unit | `deploy/systemd/btc-rewardbook.service`, 23 lines, 817 bytes, SHA-256 `7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec`, Appendix A byte for byte; installed byte for byte as `/etc/systemd/system/btc-rewardbook.service` |
| service's copy | `/root/btc-rewardbook-svc/tz33-reward-book-capture.py`, SHA-256 `a276bbb9…`; `commit.txt` `2dcd70e08b18b93c64bb67d9849ac1216ce40e41` |
| interpreter | `/root/tz04a-env/venv/bin/python` 3.12.3 with `websockets` 17.1; every mode under `nice -n 19` and `-B` |
| requests | `prestart`: one listing page, one gamma request, two CLOB documents and two reward documents through `http_get`, and one 25 s stream session through `stream_slot`. The unit's own. `git` against `origin`; `gh` for the pull request. The self-test reached `127.0.0.1` alone |
| pricer | not read, not called, not scored; `A6` `729f0bcdbee3` is stated so that what was not scored is not in doubt |

This report prints no price, size, side, book hash, rate, competitiveness or outcome. Every figure below is a count, a
time, a status, a condition or token id, or a SHA-256, copied from the instrument's own output or from a command TZ-33
names, quoted verbatim from `/root/tz33-work/logs/`.

---

## 0. Fingerprint

`I0 fingerprint`, the staged copy, performed contract §1 steps 3 and 4 inside the instrument against `SYSTEM-MAP.md` and
the files of its §0 table in the primary checkout, at `adba104`: revision `2026-10-27-b`; the six anchors equal, `A2`,
`A4`, `A5` and `A6` re-derived; the 44 rows, 41 `frozen` equal, 2 `tracked` and 1 `reported`; and the map's own lines,
bytes and SHA-256. **FINGERPRINT PASS.**

| anchor | required | read |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | equal to the map's §0, asserted, not printed |
| `A2` — collector | `6c5089330629` | `6c5089330629`, re-derived from `research/twap-divergence.py` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | equal to the map's §0, asserted, not printed |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b`, re-derived from `BTC-EXECUTOR-INSTRUCTIONS.md` |
| `A5` — recorder | `0f6c90451cbd` | `0f6c90451cbd`, re-derived from `research/recorder/recorder.py` |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3`, re-derived from `research/pfair.py` |

### 0.1 The 44 rows of the map's §0 table, and the map (V1) — `logs/02-fingerprint.log`, verbatim

```
[2026-10-28T06:11:38Z] re-derived A2 research/twap-divergence.py sha256[:12] 6c5089330629 equal
[2026-10-28T06:11:38Z] re-derived A4 BTC-EXECUTOR-INSTRUCTIONS.md sha256[:12] 437b45ea196b equal
[2026-10-28T06:11:38Z] re-derived A5 research/recorder/recorder.py sha256[:12] 0f6c90451cbd equal
[2026-10-28T06:11:38Z] re-derived A6 research/pfair.py sha256[:12] 729f0bcdbee3 equal
[2026-10-28T06:11:38Z] SYSTEM-MAP.md                                    1685 lines   398963 bytes 01d015870baef46f071472bf323b73356bb3d6cbaae562ab8a03ecf9b0983fc7 reported
[2026-10-28T06:11:38Z] BTC-EXECUTOR-INSTRUCTIONS.md                      234 lines    11128 bytes 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b frozen equal
[2026-10-28T06:11:38Z] research/twap-divergence.py                      1135 lines    50928 bytes 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 frozen equal
[2026-10-28T06:11:38Z] research/selftest-twap-divergence.py              376 lines    16736 bytes ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a frozen equal
[2026-10-28T06:11:38Z] research/tz02-distribution.py                     334 lines    14511 bytes f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 tracked
[2026-10-28T06:11:38Z] research/pfair.py                                 441 lines    19357 bytes 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 frozen equal
[2026-10-28T06:11:38Z] research/selftest-pfair.py                        619 lines    32559 bytes b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa frozen equal
[2026-10-28T06:11:38Z] research/tz06-calibration.py                      577 lines    27138 bytes 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f frozen equal
[2026-10-28T06:11:38Z] research/tz07a-variance-time.py                   623 lines    28414 bytes 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 frozen equal
[2026-10-28T06:11:38Z] research/tz07b-settlement-dispersion.py           515 lines    24926 bytes 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc frozen equal
[2026-10-28T06:11:38Z] research/tz08a-out-of-sample.py                   745 lines    38822 bytes 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c frozen equal
[2026-10-28T06:11:38Z] research/tz09-disk-inventory.py                   894 lines    41004 bytes b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 frozen equal
[2026-10-28T06:11:38Z] research/tz10b-sigma-or-link.py                  1224 lines    61018 bytes 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 frozen equal
[2026-10-28T06:11:38Z] research/tz11a-student-link.py                   1231 lines    64732 bytes 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 frozen equal
[2026-10-28T06:11:38Z] research/tz12-sized-gate.py                      1157 lines    61637 bytes d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 frozen equal
[2026-10-28T06:11:38Z] research/tz13-sized-gate-test3.py                1074 lines    53901 bytes a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd frozen equal
[2026-10-28T06:11:38Z] research/tz14-quote-inventory.py                 2124 lines   109972 bytes 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 frozen equal
[2026-10-28T06:11:38Z] research/tz15-phase2-gate.py                     1517 lines    73799 bytes 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 frozen equal
[2026-10-28T06:11:38Z] research/tz16a-phase2-decisive-gate.py           2198 lines   111192 bytes 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 frozen equal
[2026-10-28T06:11:38Z] research/tz17-settlement-chain.py                1102 lines    38622 bytes e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 frozen equal
[2026-10-28T06:11:38Z] research/tz18a-chainbook-capture.py              1683 lines    69517 bytes e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae frozen equal
[2026-10-28T06:11:38Z] research/tz20-capture-under-systemd.py            771 lines    36528 bytes 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7 frozen equal
[2026-10-28T06:11:38Z] research/tz21-recorder-memory.py                 1284 lines    59009 bytes d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f frozen equal
[2026-10-28T06:11:38Z] research/tz23-maker-m0.py                        1184 lines    54885 bytes 6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f frozen equal
[2026-10-28T06:11:38Z] research/tz24-nesting-b2.py                      1535 lines    76142 bytes 4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b frozen equal
[2026-10-28T06:11:38Z] research/tz26-nesting-b3-capture.py              2492 lines   118466 bytes caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec frozen equal
[2026-10-28T06:11:38Z] research/tz27-pairbook-archive.py                2078 lines   106284 bytes 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673 frozen equal
[2026-10-28T06:11:38Z] research/tz28-pairbook-archive-timer.py          1438 lines    74576 bytes 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4 frozen equal
[2026-10-28T06:11:38Z] research/tz29-maker-m0-second-look.py            1225 lines    68959 bytes 18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905 frozen equal
[2026-10-28T06:11:38Z] research/tz30-nesting-b3-measure.py              2518 lines   131119 bytes 93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab frozen equal
[2026-10-28T06:11:38Z] research/tz31-who-earns.py                       1523 lines    84775 bytes 7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765 frozen equal
[2026-10-28T06:11:38Z] research/tz32-our-quoting.py                     2576 lines   138209 bytes 6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61 frozen equal
[2026-10-28T06:11:38Z] research/recorder/recorder.py                     651 lines    27821 bytes 0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7 frozen equal
[2026-10-28T06:11:38Z] research/recorder/config.py                       112 lines     4773 bytes 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d frozen equal
[2026-10-28T06:11:38Z] research/recorder/manifest.py                     254 lines    10002 bytes 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 frozen equal
[2026-10-28T06:11:38Z] research/recorder/analyze.py                      813 lines    34705 bytes eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d frozen equal
[2026-10-28T06:11:38Z] research/recorder/probe.py                        227 lines     9324 bytes 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 frozen equal
[2026-10-28T06:11:38Z] research/recorder/selftest.py                     573 lines    30591 bytes c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 frozen equal
[2026-10-28T06:11:38Z] deploy/systemd/btc-recorder.service                23 lines      707 bytes 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1 frozen equal
[2026-10-28T06:11:38Z] deploy/systemd/btc-chainbook.service               22 lines      724 bytes a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2 frozen equal
[2026-10-28T06:11:38Z] deploy/systemd/btc-pairbook.service                22 lines      761 bytes ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8 frozen equal
[2026-10-28T06:11:38Z] deploy/systemd/btc-pairbook-archive.service        17 lines      794 bytes 2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7 frozen equal
[2026-10-28T06:11:38Z] deploy/systemd/btc-pairbook-archive.timer          13 lines      417 bytes 07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913 frozen equal
[2026-10-28T06:11:38Z] .gitignore                                          5 lines      252 bytes 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b tracked
[2026-10-28T06:11:38Z] SYSTEM-MAP.md 1685 lines 398963 bytes sha256 01d015870baef46f071472bf323b73356bb3d6cbaae562ab8a03ecf9b0983fc7
[2026-10-28T06:11:38Z] FINGERPRINT PASS: revision 2026-10-27-b; anchors 6 of 6, 4 re-derived; rows 44: frozen 41 of 41 equal, tracked 2, reported 1
[2026-10-28T06:11:38Z] peak memory of this run: 40890368 bytes
[2026-10-28T06:11:38Z] opens refused: 0; manifest opens 0; window opens 0; ledger opens 0; requests 0, stream sessions 0
exit=0
```

### 0.2 §0.0 and §0.1 — the work tree, and the instrument staged

`logs/00-work-tree.log` — `mkdir` exit `0`, so neither directory existed:

```
$ mkdir /root/tz33-work /root/tz33-work/logs; echo "exit=$?"
exit=0
(run 2026-10-28T06:11:05Z after contract §1 steps 1-2: main fast-forwarded to origin/main)
adba1043e4d32011053dd6d1f1d926359af32dc4
adba1043e4d32011053dd6d1f1d926359af32dc4
```

`logs/07-tz-file.log` — the TZ as read:

```
2026-10-28T13:19:43.177764161Z
$ wc -l -c CryptoTZ/TZ-33-reward-book-capture.md; sha256sum it; the commit that added it
  4485 264353 CryptoTZ/TZ-33-reward-book-capture.md
fb4375198deda5198d2d4b2e0321339472150b06fc67b52d3ffe6943e077cb9d  CryptoTZ/TZ-33-reward-book-capture.md
adba1043e4d32011053dd6d1f1d926359af32dc4 Add files via upload
```

`logs/01-stage.log` — §0.1's script, verbatim, its argument `/root/tz33-work/stage`: both hashes asserted, lines and
bytes equal to §0.1's table:

```
/root/tz33-work/stage/deploy/systemd/btc-rewardbook.service 23 817 7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec
/root/tz33-work/stage/research/tz33-reward-book-capture.py 3542 175160 a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670
exit=0
```

### 0.3 Host gate — the opening reads, verbatim (V2)

`logs/03-host-gate.log`, §0.3's block run from `/root/btc-5m-twap` with `S` the session's scratchpad directory:

```
Wed Oct 28 06:11:51 AM UTC 2026
1793167911
1
MemTotal:         978640 kB
MemAvailable:     290100 kB
SwapTotal:       3174396 kB
SwapFree:        2801468 kB
2026-08-02 07:24:32
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
 -5 23a31fad2f064f04b9e138eac29658f3 Sat 2026-06-20 18:48:10 UTC Fri 2026-06-26 14:13:44 UTC
 -4 a38e17445ce341bc8b877be9d3d4f648 Fri 2026-06-26 14:13:52 UTC Tue 2026-07-14 16:15:10 UTC
 -3 5f4d18a6ba8041bd80e7d1e192c5ee28 Tue 2026-07-14 16:15:20 UTC Fri 2026-07-17 01:01:21 UTC
 -2 b1b399c70c6e4dcc934755f70a2ca231 Fri 2026-07-17 01:01:43 UTC Fri 2026-07-24 14:55:46 UTC
 -1 285d6962c92c407d837d1ce329b93aa4 Fri 2026-07-24 14:55:54 UTC Sun 2026-08-02 07:23:49 UTC
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-02 07:24:34 UTC Wed 2026-10-28 06:11:50 UTC
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11560394752
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
3
3.12.3 17.1
MainPID=2388318
Result=success
NRestarts=0
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC

MainPID=3055430
Result=success
NRestarts=9
Id=btc-pairbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Wed 2026-10-28 03:06:34 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-pairbook-archive.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=

Result=success
Id=btc-pairbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-11 15:08:11 UTC

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
Id=btc-rewardbook.service
ActiveState=inactive
SubState=dead
UnitFileState=
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
NEXT                        LEFT LAST                              PASSED UNIT                       ACTIVATES
Wed 2026-10-28 14:39:19 UTC   8h Tue 2026-10-27 18:26:30 UTC      11h ago apt-daily.timer            apt-daily.service
Thu 2026-10-29 03:00:20 UTC  20h Wed 2026-10-28 03:00:20 UTC 3h 11min ago btc-pairbook-archive.timer btc-pairbook-archive.service
Thu 2026-10-29 06:39:12 UTC  24h Wed 2026-10-28 06:03:25 UTC     8min ago apt-daily-upgrade.timer    apt-daily-upgrade.service

3 timers listed.
rewardbook unit exit=1
btc-recorder.service cmp exit=0
btc-pairbook.service cmp exit=0
btc-pairbook-archive.service cmp exit=0
btc-pairbook-archive.timer cmp exit=0
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
e8b46a85d61e1a17841962846f6d3012046c2d70
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
/root/tz32-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
/root/btc-pairbook-archive-svc exit=0
/var/lib/btc-pairbook-archive exit=0
/root/btc-rewardbook-svc exit=1
/var/lib/btc-rewardbook exit=1
66620 /var/lib/btc-pairbook-archive/ledger.jsonl
2044
/root/btc-5m-twap       adba104 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
279466880	/var/lib/btc-pairbook
9729921	/var/lib/btc-pairbook-archive
114493707	/root/.claude
651992164	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/0358b0b2-9811-5291-867b-b185a7307938/scratchpad
total 32
drwx------  8 root root 4096 Oct 28 06:09 .
drwx------ 32 root root 4096 Oct 28 06:09 ..
drwx------  4 root root 4096 Oct 28 06:09 0358b0b2-9811-5291-867b-b185a7307938
drwx------  3 root root 4096 Oct 27 06:55 236f3e7a-57cc-45b7-9aea-18e9a8ad59b9
drwx------  3 root root 4096 Oct 28 05:01 54afa9d7-a228-4c5e-be8c-563e1375605e
drwx------  3 root root 4096 Oct 28 06:09 621e47cc-760f-4cb1-8481-c2a8f6828d9d
drwx------  3 root root 4096 Oct 28 05:01 bda03c0e-cdeb-53c4-9287-68b3d18ca407
drwx------  4 root root 4096 Oct 27 06:55 f2adac1e-d4b2-5417-b2ba-a166434774bb
```

| condition | read | verdict |
|---|---|---|
| **H1** | `find` printed exactly one path, `/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json` | PASS |
| **H2** | `df` source `/dev/vda2`, size `31612203008`; `grep -c` `3` | PASS |
| **H3** | `3.12.3 17.1` | PASS |
| **H4** | `btc-recorder.service` and `btc-pairbook.service` `ActiveState=active`, `UnitFileState=enabled` | PASS |
| **H5** | `rewardbook unit exit=1`; `/root/btc-rewardbook-svc exit=1`, `/var/lib/btc-rewardbook exit=1` | PASS |
| **memory gate** | `MemAvailable: 290100 kB`, at least `135,569,408` bytes | PASS |
| **disk gate** | `avail` `11560394752`, at least `8,200,000,000` | PASS |

**Printed, no threshold:** one boot since 2026-08-02 07:24:34 UTC; the recorder pid `2388318`, `NRestarts=0`, active
since 2026-10-23 06:08:56 UTC, the package manager's restart of map §7 item 120; the pair book pid `3055430`,
`NRestarts=9`, active since 2026-10-28 03:06:34 UTC, the archive's calendar run of that morning; the archive's service
`inactive`, its timer `waiting`, next at 2026-10-29 03:00:20 UTC; the chain book `inactive` and `disabled`;
`btc-rewardbook.service` unknown to systemd; `apt-daily-upgrade.timer` last run 2026-10-28 06:03:25 UTC, 8 min before
the gate, which changed neither capture unit; the four installed project units `cmp` exit `0` against `main`'s;
`telemetry-watch.service` `disabled` and `inactive`; the three code trees at `e3975b5…`, `e8b46a8…` and `d8194fd…`, map
§3's; `/root/tz32-work` absent and the code and state trees present; the archive's ledger `66620` bytes; the forensic
store `2044` files, map §3's `2,044`; the worktrees two, map §3's; `du` of the pair book's store `279466880` bytes beside
`df`'s `11560394752` free; and the session directories, which §2.3 below names.

### 0.4 Free space and `MemAvailable`

Every read, with its instant and bound, is in §2.14. At the host gate: `MemAvailable` 290,100 kB against the floor
`135,569,408` bytes, and 11,560,394,752 bytes free on `/dev/vda2` against `8,200,000,000`.

### 0.5 Refs (§0.5) — `logs/05-refs.log`, verbatim

Read before §3.1's push. **74 ref lines**: map §1's 73, read by the Architect at 17:55 UTC on 2026-10-27, plus
`refs/tags/pairbook-streams-1793156420`, the archive's calendar run of 2026-10-28 03:00:20 UTC, which §0.5 names as the
first to come. `main` at `adba1043e4d32011053dd6d1f1d926359af32dc4`, the upload of this TZ; `refs/heads/tz-33-reward-book-capture` did not
exist. Three commits on `main`'s first-parent line above `61f9e51`, each with the paths it changed: `a86d032`, PR #31's
merge, `A research/tz32-our-quoting.py`; `31d5bce`, revision `2026-10-27-b`, `M SYSTEM-MAP.md`; and `adba104`, `A
CryptoTZ/TZ-33-reward-book-capture.md`. `main` carries revision `2026-10-27-b`. Nothing differs from §0.5's account.

```
adba1043e4d32011053dd6d1f1d926359af32dc4	HEAD
adba1043e4d32011053dd6d1f1d926359af32dc4	refs/heads/main
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8	refs/heads/tz-23-maker-m0
6f045cffc3601b589d3b8b7a6a9af6f73991e18b	refs/heads/tz-24-nesting-b2
e8b46a85d61e1a17841962846f6d3012046c2d70	refs/heads/tz-26-nesting-b3-capture
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/heads/tz-27-pairbook-archive
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/heads/tz-28-pairbook-archive-timer
f6425f713034724210dc120d2108bcfad63cadc6	refs/heads/tz-29-maker-m0-second-look
fcd9ca566e9b948f0426707e7c3b5684f7f03b04	refs/heads/tz-30-nesting-b3-measure
404288fb03ffd3619b2183f121d45688def8fba8	refs/heads/tz-31-who-earns
b601f756edea59adf536d7ef05226d6f06bcef13	refs/heads/tz-32-our-quoting
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
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
e299d4e45f48b7efaa8cb18bd54b139fc0627630	refs/tags/tz-27-pairbook-streams
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/tags/tz-27-pairbook-streams^{}
exit=0

$ git log --first-parent --name-status 61f9e51..origin/main
adba1043e4d32011053dd6d1f1d926359af32dc4 2026-10-28T01:53:53+04:00 Add files via upload

A	CryptoTZ/TZ-33-reward-book-capture.md
31d5bce53b41086c4cb9ac906813db6c43223754 2026-10-27T17:40:45+04:00 Update SYSTEM-MAP.md

M	SYSTEM-MAP.md
a86d032459614eae7c3759f8a8f38477b2d901a8 2026-10-27T17:36:38+04:00 Merge pull request #31 from seahomebatumi-ai/tz-32-our-quoting

A	research/tz32-our-quoting.py

$ grep -c "Revision 2026-10-27-b" via git show origin/main:SYSTEM-MAP.md
1
```

---

## 1. Input

| what | read by | size, count, hash |
|---|---|---|
| this TZ | §0.1's script, twice; `I0 fingerprint` | 4,485 lines, 264,353 bytes, `fb437519…`, added by `adba104` (`logs/07-tz-file.log`) |
| `SYSTEM-MAP.md` revision `2026-10-27-b` | `I0 fingerprint` | 1,685 lines, 398,963 bytes, `01d015870baef46f071472bf323b73356bb3d6cbaae562ab8a03ecf9b0983fc7` |
| the map's 43 file rows | `I0 fingerprint` | §0.1 |
| the venue: the reward listing's first page, one gamma batch, two CLOB documents, two reward documents, one 25 s stream session on four tokens | `prestart` | §2.6; every reply's status, bytes and SHA-256 printed; stored under `/root/tz33-work/prestart/` |
| the recorder's 2,016 `manifest.json` of the week before `prestart` | `prestart`, read only, for `quotes_complete` | §2.6 |
| the pair book's 672 `window.json` of the week before `prestart` | `prestart`, read only, once the archive's service read `inactive` | §2.6 |
| `prestart`'s second run, into `prestart-2` | `prestart` | the same six requests and one session; §2.6, `logs/51-prestart-2.log` |
| the reward book's store: `runtime.jsonl`, each slot's `slot.json`, stream and rewards files, the day's `select.0.json` and replies | `unit`, `prove`, `resume`, `restart`; §3.11's `tail` of `service.log` and `du` | counts, times, statuses, shapes and SHA-256 only; no body printed |
| the recorder's 14 and the pair book's 5 `manifest.json` and `window.json` of the proof's span | `prove`, twice, read only, once the archive's service read `inactive` | §2.9 |
| the archive's `ledger.jsonl` | `final`, once, read only | its two `restart` records, §2.13 |

**Nothing was re-collected.** The reward book's store, `/var/lib/btc-rewardbook/`, is this TZ's capture, written by its
unit alone and read by the modes §2 item 5 names; this report prints its counts and times and nothing of a body.

---

## 2. Measurements

### 2.1 §3.1 — the branch and its two files (V3)

`logs/10-branch.log` — the fetch, which brought the archive's new tag, and the worktree at `origin/main`, `adba104`:

```
$ git -C /root/btc-5m-twap fetch origin
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new tag]         pairbook-streams-1793156420 -> pairbook-streams-1793156420
exit=0
$ git -C /root/btc-5m-twap worktree add -b tz-33-reward-book-capture /root/tz33-work/wt origin/main
Preparing worktree (new branch 'tz-33-reward-book-capture')
branch 'tz-33-reward-book-capture' set up to track 'origin/main'.
HEAD is now at adba104 Add files via upload
exit=0
```

`logs/11-extract-wt.log` — §0.1's script again, verbatim but for its argument `/root/tz33-work/wt`; the same lines,
bytes and SHA-256 as at §0.1:

```
/root/tz33-work/wt/deploy/systemd/btc-rewardbook.service 23 817 7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec
/root/tz33-work/wt/research/tz33-reward-book-capture.py 3542 175160 a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670
exit=0
```

The two files committed alone, as `2dcd70e`, on the branch. `logs/12-push.log` — `git push -u origin
tz-33-reward-book-capture` **went through with the URL's own credential**, so the `gh` credential route §3.1 allows was
not needed; `origin` carried `2dcd70e…` at 06:13:45 UTC by `ls-remote`, equal to `HEAD` and its upstream; the branch's
diff against `origin/main` names exactly the two paths, both `A`:

```
$ git push -u origin tz-33-reward-book-capture
remote: 
remote: Create a pull request for 'tz-33-reward-book-capture' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-33-reward-book-capture        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-33-reward-book-capture -> tz-33-reward-book-capture
branch 'tz-33-reward-book-capture' set up to track 'origin/tz-33-reward-book-capture'.
exit=0
$ git ls-remote origin refs/heads/tz-33-reward-book-capture; git rev-parse HEAD @{u}
2dcd70e08b18b93c64bb67d9849ac1216ce40e41	refs/heads/tz-33-reward-book-capture
2dcd70e08b18b93c64bb67d9849ac1216ce40e41
2dcd70e08b18b93c64bb67d9849ac1216ce40e41
2026-10-28T06:13:45.819795934Z
$ git diff --name-status origin/main origin/tz-33-reward-book-capture
A	deploy/systemd/btc-rewardbook.service
A	research/tz33-reward-book-capture.py
```

`logs/13-pr.log` — the pull request, against `main`:

```
$ gh pr create --base main --head tz-33-reward-book-capture
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/32
exit=0
```

### 2.2 §3.2 — the self-test (V4): **99 of 99**

`logs/20-selftest.log`, verbatim. It reached `127.0.0.1` alone: its 25 requests and 3 stream sessions are the loopback
servers'.

```
[2026-10-28T06:14:04Z]   ok  day_of: 2026-10-28 00:00:00 UTC is 1793145600, the next day 1793232000
[2026-10-28T06:14:04Z]   ok  first_slot: the current slot until S+880, then the next, late after its open at S-5
[2026-10-28T06:14:04Z]   ok  selection_plan: today at once, tomorrow from 23:45:00 UTC, the next instant the plan changes
[2026-10-28T06:14:04Z]   ok  slot_schedule: the stream S-5 to S+905, the summary at S+910
[2026-10-28T06:14:04Z]   ok  poll_instants: 150 markets, three rounds 300 s apart, 1.8 s between polls, the last at S+898.2
[2026-10-28T06:14:04Z]   ok  the store's file names
[2026-10-28T06:14:04Z]   ok  iso_seconds: a zone required, Z and offsets read, fractions kept
[2026-10-28T06:14:04Z]   ok  gamma_verdict: an end at D0 + 15 days passes, a second earlier does not
[2026-10-28T06:14:04Z]   ok  gamma_verdict: every other reason named
[2026-10-28T06:14:04Z]   ok  gamma_verdict: an event start in [D0 - 1 day, D0 + 2 days) excludes, either edge exact
[2026-10-28T06:14:04Z]   ok  gamma_verdict: so does an event end in the band, on any of the market's events
[2026-10-28T06:14:04Z]   ok  clob_verdict: an open market of two tokens, no game, no delay, no excluded tag passes
[2026-10-28T06:14:04Z]   ok  clob_verdict: every other reason named
[2026-10-28T06:14:04Z]   ok  clob_verdict: 31 excluded tags, matched whole after case and space are dropped
[2026-10-28T06:14:04Z]   ok  listing_rows: identical rows once, differing rows a conflict, rows without a string id unkeyed
[2026-10-28T06:14:04Z]   ok  listing_verdict: a valid id and three positive numbers
[2026-10-28T06:14:04Z]   ok  ranking: by rate descending in exact decimals, ties by condition id ascending
[2026-10-28T06:14:04Z]   ok  walk: gamma by blocks of the batch, CLOB only after gamma passes, stopping at the k-th member
[2026-10-28T06:14:04Z]   ok  walk: never past walk_max
[2026-10-28T06:14:04Z]   proxy variables removed: 0
[2026-10-28T06:14:04Z]   ok  build_request: GET, Accept and this file's User-Agent
[2026-10-28T06:14:04Z]   ok  the wire: exactly five header fields
[2026-10-28T06:14:04Z]   ok  http_get records 200, 2 bytes, the body's SHA-256 and its stamps
[2026-10-28T06:14:04Z]   ok  a refusal is a stored reply with its status
[2026-10-28T06:14:04Z]   ok  two loopback requests counted
[2026-10-28T06:14:04Z]   ok  the selection: the first three that pass, in rank order, a rate kept as its own text
[2026-10-28T06:14:04Z]   ok  the walk disclosed in rank order, stopping at the third member
[2026-10-28T06:14:04Z]   ok  the listing: 16 rows, 13 ids, one conflict, one unkeyed, two not positive, 10 ranked
[2026-10-28T06:14:04Z]   ok  nine requests: two pages, one gamma batch, five CLOB documents and one retry after a 503
[2026-10-28T06:14:04Z]   ok  the stored replies alone re-derive the same selection, every request read, each its last try
[2026-10-28T06:14:04Z]   ok  load_selection: the day's first ok attempt
[2026-10-28T06:14:04Z]   ok  a stored reply answers only the request the attempt made, in its order
[2026-10-28T06:14:04Z]   ok  a failed attempt is written with its reason and leaves the day's first ok attempt in force
[2026-10-28T06:14:04Z]   ok  a 404 on a listing page fails the attempt
[2026-10-28T06:14:04Z]   ok  a 5xx is tried three times, every try kept, and then fails the attempt
[2026-10-28T06:14:04Z]   ok  poll_rows: 200 and a page of at most one row, of the polled market; a page without its row is served
[2026-10-28T06:14:04Z] day 1793145600 (2026-10-28T00:00:00Z): selection attempt 0 loaded, 3 members
[2026-10-28T06:14:08Z] slot 1793168046 (2026-10-28T06:14:06Z) index 0: 3 markets; stream opened, 589 frames, 2 segments, 12401 bytes; polls 6 served of 6, 4 with a row, 0 missed
[2026-10-28T06:14:08Z]   ok  a slot: a close by the venue, then one reconnect, three markets, six tokens
[2026-10-28T06:14:08Z]   ok  the subscription: the documented frame, compact, both tokens of every member in rank order
[2026-10-28T06:14:08Z]   ok  the handshake: six header fields, this file's User-Agent, no extension offered
[2026-10-28T06:14:08Z]   ok  the heartbeat: PING on its period, PONG stored
[2026-10-28T06:14:08Z]   ok  the polls: two rounds of three markets, every one served and stored, a market without its row twice
[2026-10-28T06:14:08Z]   ok  the summary names the day's selection by attempt and SHA-256
[2026-10-28T06:14:08Z]   ok  the stream file: connect, open, subscribe, frames, close, the same again, end
[2026-10-28T06:14:08Z]   ok  the venue's close is recorded with its code, the slot's end as end
[2026-10-28T06:14:08Z]   ok  every frame a line of recv_ns, mono_ns and the frame verbatim; the first the six books
[2026-10-28T06:14:08Z]   ok  the unit reads the slot back: every frame conforms, every token's book, both sessions
[2026-10-28T06:14:08Z]   ok  a slot of a few seconds reads short, and nothing else
[2026-10-28T06:14:08Z]   ok  rewards_unit reads the six polls back, each of the market its index names
[2026-10-28T06:14:08Z]   ok  a second process in the slot writes index 1
[2026-10-28T06:14:08Z] day 1793145600 (2026-10-28T00:00:00Z): selection attempt 0 loaded, 3 members
[2026-10-28T06:14:11Z] slot 1793168050 (2026-10-28T06:14:10Z) index 0: 3 markets; stream opened, 411 frames, 1 segments, 8632 bytes; polls 4 served of 6, 3 with a row, 0 missed, stopped
[2026-10-28T06:14:11Z]   ok  a stop closes the session at once, the file whole, the summary written stopped
[2026-10-28T06:14:11Z] halt in floor: free 2199999999 bytes, below the floor 2200000000
[2026-10-28T06:14:11Z] halt in floor: free 2199999999 bytes, below the floor 2200000000
[2026-10-28T06:14:11Z]   ok  free space below 2,200,000,000 bytes at a slot or a selection halts the service
[2026-10-28T06:14:11Z]   ok  a file cut after a sync flush reads to it, torn
[2026-10-28T06:14:11Z]   ok  the whole file: 60 frames and the end line
[2026-10-28T06:14:11Z]   ok  bytes past the trailer read torn
[2026-10-28T06:14:11Z]   ok  the slot maximum cuts the stream
[2026-10-28T06:14:11Z]   ok  a binary frame is stored as base64, verbatim
[2026-10-28T06:14:11Z]   ok  the stream opens only with a selection of members, free at or above the floor, the store below the cap
[2026-10-28T06:14:11Z]   ok  the cap counts the stream files alone, read again at every slot
[2026-10-28T06:14:11Z]   ok  a slot streamed from S-5 to S+905: complete, its largest gap 1 s
[2026-10-28T06:14:11Z]   ok  a subscribe after S reads late subscribe, and nothing else
[2026-10-28T06:14:11Z]   ok  no book of every token within 10 s of it reads initial books
[2026-10-28T06:14:11Z]   ok  18 s without a frame reads gap
[2026-10-28T06:14:11Z]   ok  a file without its end line and its close reads so
[2026-10-28T06:14:11Z]   ok  a stream whose last close is before S+900 reads short
[2026-10-28T06:14:11Z]   ok  an undocumented event type, a token not subscribed and a count off its summary are named
[2026-10-28T06:14:11Z]   ok  a slot joined late, with an error, or cut is no unit
[2026-10-28T06:14:11Z]   ok  a slot whose stream did not open names why; a missing summary reads so
[2026-10-28T06:14:11Z]   ok  frame_tokens: the four documented types and their token ids, nothing else
[2026-10-28T06:14:11Z]   ok  serve writes under the reward book's root and nowhere else
[2026-10-28T06:14:11Z]   ok  serve starts no process; the systemd reads may
[2026-10-28T06:14:11Z]   ok  under the recorder's root only a manifest, read only, by prestart and prove
[2026-10-28T06:14:11Z]   ok  under the pair book's root only a window's window.json, read only, by prestart and prove
[2026-10-28T06:14:11Z]   ok  the archive's ledger read by still and final alone; nothing of the chain book
[2026-10-28T06:14:11Z]   ok  no neighbour's root is ever listed
[2026-10-28T06:14:11Z]   ok  the reward book's root is written by serve alone, read and listed by the modes that judge it
[2026-10-28T06:14:11Z]   ok  the forensic store takes new files by exclusive create alone
[2026-10-28T06:14:11Z]   ok  the hook refuses /var/lib/btc-recorder/runtime.jsonl before it is opened
[2026-10-28T06:14:11Z]   ok  the hook refuses /var/lib/btc-pairbook/runtime.jsonl before it is opened
[2026-10-28T06:14:11Z]   ok  the hook refuses /var/lib/btc-pairbook-archive/ledger.jsonl before it is opened
[2026-10-28T06:14:11Z]   ok  the hook refuses /var/lib/btc-rewardbook/runtime.jsonl before it is opened
[2026-10-28T06:14:11Z]   ok  G-STREAM: 4 and 3 of 4, 2 of 4, fewer than 4
[2026-10-28T06:14:11Z]   ok  G-REWARDS: 1,782 of 1,800 served is 99 in 100, 1,781 is not
[2026-10-28T06:14:11Z]   ok  G-NEIGHBORS: a counted failure breaks it; HOLD needs 8 and 3
[2026-10-28T06:14:11Z]   ok  the neighbours' units inside a span: 12 intervals and 4 windows over four slots
[2026-10-28T06:14:11Z]   ok  G-STREAM's false failure at 1 in 100 and its power at 1 in 4 and 1 in 2
[2026-10-28T06:14:11Z]   ok  G-REWARDS' false failure at 1 poll in 200 and its power at 1 in 100 and 1 in 50
[2026-10-28T06:14:11Z]   ok  G-NEIGHBORS' power at its least count, 11 units, at 1 in 4 and 1 in 2
[2026-10-28T06:14:11Z]   ok  the neighbours' false alarm, exact
[2026-10-28T06:14:11Z]   ok  G-NEIGHBORS' false failure at both base rates over 16 intervals and 5 windows
[2026-10-28T06:14:11Z] the pair book's archive: inactive after 20 s
[2026-10-28T06:14:11Z] the pair book's archive: failed after 0 s
[2026-10-28T06:14:11Z]   ok  the archive's hold: every 10 s until its service is not running
[2026-10-28T06:14:11Z]   ok  the archive's hold stops BLOCKED past 7,200 s
[2026-10-28T06:14:11Z]   ok  decimals: half up, whole numbers included
[2026-10-28T06:14:11Z]   ok  G-STILL: unchanged, or the pair book moved by the archive's chain of restarts alone
[2026-10-28T06:14:11Z]   ok  same_service: the exact argv, never a substring
[2026-10-28T06:14:11Z]   ok  no summary's key is forbidden; a member's rate stays in the store
[2026-10-28T06:14:11Z]   ok  a forbidden key at any depth fails the output's check
[2026-10-28T06:14:11Z]   ok  imports: the standard library and websockets
[2026-10-28T06:14:12Z]   ok  exactly five endpoints in the file's text
[2026-10-28T06:14:12Z]   ok  websockets 17.1, the recorder's
[2026-10-28T06:14:12Z]   ok  glibc took the mmap threshold of 128 KiB and two arenas
[2026-10-28T06:14:12Z] 99 of 99 checks passed
[2026-10-28T06:14:12Z] peak memory of this run: 64638976 bytes
[2026-10-28T06:14:12Z] opens refused: 0; manifest opens 0; window opens 0; ledger opens 0; requests 25, stream sessions 3
exit=0
```

### 2.3 §3.3 — the units, and the directories beside this session

`logs/30-still.log` — `I still` recorded the recorder's and the pair book's `MainPID`, `NRestarts` and `ActiveState` in
`state.json`:

```
[2026-10-28T06:14:23Z] btc-pairbook.service {'MainPID': '3055430', 'NRestarts': '9', 'ActiveState': 'active'}, MemoryCurrent 13021184, MemoryPeak 132734976
[2026-10-28T06:14:23Z] btc-recorder.service {'MainPID': '2388318', 'NRestarts': '0', 'ActiveState': 'active'}, MemoryCurrent 246321152, MemoryPeak 302309376
[2026-10-28T06:14:23Z] btc-pairbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-28T06:14:23Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-28T06:14:23Z] still: recorded
[2026-10-28T06:14:23Z] peak memory of this run: 39170048 bytes
[2026-10-28T06:14:23Z] opens refused: 0; manifest opens 0; window opens 0; ledger opens 0; requests 0, stream sessions 0
exit=0
```

`logs/31-scratch.log` — `I scratch` of the directory that holds this session's own,
`0358b0b2-9811-5291-867b-b185a7307938`, which it skips. It named four directories **earlier** — TZ-32's pair,
`f2adac1e…` and `236f3e7a…`, as map §3 and §6 say, and `54afa9d7-a228-4c5e-be8c-563e1375605e` and
`bda03c0e-cdeb-53c4-9287-68b3d18ca407`, born 2026-10-28 05:01:39 and 05:01:40 UTC by sessions no report names — and one
**live**, `621e47cc-760f-4cb1-8481-c2a8f6828d9d`, born with this session's process `3071142`:

```
[2026-10-28T06:14:23Z] running 2875240 started 2026-10-26T18:11:45Z claude
[2026-10-28T06:14:23Z] running 2875250 started 2026-10-26T18:11:47Z claude
[2026-10-28T06:14:23Z] running 3071142 started 2026-10-28T06:09:21Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-10-28T06:14:23Z] 236f3e7a-57cc-45b7-9aea-18e9a8ad59b9 born 2026-10-27T06:55:19Z: earlier
[2026-10-28T06:14:23Z] 54afa9d7-a228-4c5e-be8c-563e1375605e born 2026-10-28T05:01:39Z: earlier
[2026-10-28T06:14:23Z] 621e47cc-760f-4cb1-8481-c2a8f6828d9d born 2026-10-28T06:09:21Z: live, process [3071142]
[2026-10-28T06:14:23Z] bda03c0e-cdeb-53c4-9287-68b3d18ca407 born 2026-10-28T05:01:40Z: earlier
[2026-10-28T06:14:23Z] f2adac1e-d4b2-5417-b2ba-a166434774bb born 2026-10-27T06:55:20Z: earlier
[2026-10-28T06:14:23Z] peak memory of this run: 39186432 bytes
[2026-10-28T06:14:23Z] opens refused: 0; manifest opens 0; window opens 0; ledger opens 0; requests 0, stream sessions 0
exit=0
```

### 2.4 §9 B-RECLAIM-SCRATCH — after §3.3, before §3.4 (V18, V19) — **no `RECLAIM PASS` on record before the removal**

**The session's classifier refused the block's first line**, `I reclaim` of the four earlier directories, at
06:15:13 UTC, giving no reason (`logs/32-reclaim-scratch-refused.log`); nothing of the block had run. By §3's route the
Executor printed the block for the Boss in two parts — `reclaim` first, then the four `rm -rf` and `test -e` pairs,
**to be run only if the first part printed `RECLAIM PASS` and `exit=0`**.

```
2026-10-28T06:15:13.824948096Z
B-RECLAIM-SCRATCH: its first line, I reclaim of the four directories I scratch named earlier, refused by the session's permission classifier (no reason given); handed to the Boss by TZ-33 section 3's route. Nothing of the block ran.
```

**What the record shows.** The Boss's root shell logged in twice from `45.154.88.64`, 06:28:06 to 06:28:47 and 06:30:27
to 06:32:19 UTC (`last`). The directory holding the four, `/tmp/claude-0/-root-btc-5m-twap`, was last changed at
**06:28:17.04 UTC**, inside the first login: **the four directories were removed then.** Both logs on disk are the
second login's, written at 06:30:34 and 06:30:46 UTC, each overwriting whatever the first login had written under the
same name. In it `reclaim` stopped at its first assert, `reclaimable`, because the directories it was given no longer
existed — `os.path.isdir` was false — and exited `1` before printing anything; the four `rm -rf` that followed it
removed nothing and exited `0`, and the four `test -e` exited `1`:

```
Traceback (most recent call last):
  File "/root/tz33-work/wt/research/tz33-reward-book-capture.py", line 3542, in <module>
    sys.exit(main(sys.argv[1:]))
             ^^^^^^^^^^^^^^^^^^
  File "/root/tz33-work/wt/research/tz33-reward-book-capture.py", line 3526, in main
    mode_reclaim(rest)
  File "/root/tz33-work/wt/research/tz33-reward-book-capture.py", line 2755, in mode_reclaim
    assert trees and all(reclaimable(t) for t in trees), "reclaim: %r" % (trees,)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: reclaim: ['/tmp/claude-0/-root-btc-5m-twap/236f3e7a-57cc-45b7-9aea-18e9a8ad59b9', '/tmp/claude-0/-root-btc-5m-twap/54afa9d7-a228-4c5e-be8c-563e1375605e', '/tmp/claude-0/-root-btc-5m-twap/bda03c0e-cdeb-53c4-9287-68b3d18ca407', '/tmp/claude-0/-root-btc-5m-twap/f2adac1e-d4b2-5417-b2ba-a166434774bb']
exit=1
```

```
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
```

**Verified by the Executor**, from this session and not from the Boss's account (`logs/34-reclaim-scratch-verify.log`):
`test -e` exit `1` for each of the four; the parent's mtime; the two logins; the forensic store at `2044` files, **none
newer than 06:00 UTC that day**, so no `reclaim` copied anything into it; and the two logs' times:

```
2026-10-28T06:33:27.211356838Z
B-RECLAIM-SCRATCH, verified by the Executor after the Boss's runs:
test -e /tmp/claude-0/-root-btc-5m-twap/236f3e7a-57cc-45b7-9aea-18e9a8ad59b9 exit=1
test -e /tmp/claude-0/-root-btc-5m-twap/54afa9d7-a228-4c5e-be8c-563e1375605e exit=1
test -e /tmp/claude-0/-root-btc-5m-twap/bda03c0e-cdeb-53c4-9287-68b3d18ca407 exit=1
test -e /tmp/claude-0/-root-btc-5m-twap/f2adac1e-d4b2-5417-b2ba-a166434774bb exit=1
/tmp/claude-0/-root-btc-5m-twap mtime 2026-10-28 06:28:17.043938900 +0000
total 16
drwx------  4 root root 4096 Oct 28 06:28 .
drwx------ 32 root root 4096 Oct 28 06:09 ..
drwx------  4 root root 4096 Oct 28 06:09 0358b0b2-9811-5291-867b-b185a7307938
drwx------  3 root root 4096 Oct 28 06:09 621e47cc-760f-4cb1-8481-c2a8f6828d9d
$ last -F -n 5
root     pts/0        45.154.88.64     Wed Oct 28 06:30:27 2026 - Wed Oct 28 06:32:19 2026  (00:01)
root     pts/0        45.154.88.64     Wed Oct 28 06:28:06 2026 - Wed Oct 28 06:28:47 2026  (00:00)
root     pts/2        tmux(2875239).%1 Mon Oct 26 18:11:48 2026   still logged in
root     pts/1        tmux(2875239).%0 Mon Oct 26 18:11:46 2026   still logged in
root     pts/0        45.154.88.75     Mon Oct 26 18:10:12 2026 - Mon Oct 26 18:21:44 2026  (00:11)

wtmp begins Wed Apr  1 20:16:20 2026
$ find /root/btc-forensics -type f | wc -l
2044
$ find /root/btc-forensics -type f -newermt 2026-10-28T06:00:00Z | wc -l
0
logs/32-reclaim-scratch.log 849 bytes mtime 2026-10-28 06:30:34.737126067 +0000
logs/33-rm-scratch.log 56 bytes mtime 2026-10-28 06:30:46.510227586 +0000
```

**The Boss's statement**, received in the session after the second B-ENABLE, recorded verbatim as the Boss's and not
as a verification (contract §2): *"In the 06:28 session, the automated reclaim routine printed RECLAIM PASS before
removing the four scratch directories. Everything executed normally as part of host maintenance."* **The host's record
neither confirms nor refutes it.** No artifact names an automated reclaim routine on this host; the removal fell inside
the root login of 06:28:06 to 06:28:47 UTC; that run's output, if it was written to `logs/32-reclaim-scratch.log`, was
overwritten at 06:30:34; no file reached the forensic store, which TZ-31's and TZ-32's runs on such directories also
copied none into; and the reports' access times cannot show a `reclaim`'s read of them — every one of the 42 was last
read on 2026-10-27, after its own mtime and ctime and less than 24 h before 06:28, so under the root's `relatime` a read
at 06:28 would have left them as they are (`logs/35-reclaim-scratch-boss-statement.log`):

```
2026-10-28T11:38:19.128205415Z
The Boss's statement, received in the session after the second B-ENABLE: "In the 06:28 session, the automated reclaim routine printed RECLAIM PASS before removing the four scratch directories. Everything executed normally as part of host maintenance."
The Executor's check: a reclaim past its first assert reads every committed report (report_tokens); under relatime a read leaves a new atime only where the old one is older than 24 h or not after the mtime.
$ findmnt -n -o TARGET,SOURCE,OPTIONS /
/      /dev/vda2 rw,relatime
$ TZ=UTC stat -c "%x %y %n" /root/btc-5m-twap/CryptoReports/*.md
2026-10-27 06:58:55.863996399 +0000 | 2026-09-09 09:43:36.209263716 +0000 | /root/btc-5m-twap/CryptoReports/TZ-01a-twap-divergence-corrected-report.md
2026-10-27 06:58:55.862996391 +0000 | 2026-09-09 05:46:16.758389920 +0000 | /root/btc-5m-twap/CryptoReports/TZ-01-twap-divergence-report.md
2026-10-27 06:58:55.864996406 +0000 | 2026-09-09 17:20:01.790035988 +0000 | /root/btc-5m-twap/CryptoReports/TZ-02-divergence-distribution-report.md
2026-10-27 06:58:55.866996422 +0000 | 2026-09-09 21:19:44.862777895 +0000 | /root/btc-5m-twap/CryptoReports/TZ-03-repo-hygiene-report.md
2026-10-27 06:58:55.867996430 +0000 | 2026-09-12 08:56:05.689796493 +0000 | /root/btc-5m-twap/CryptoReports/TZ-04a-market-recorder-corrected-report.md
2026-10-27 06:58:55.867996430 +0000 | 2026-09-12 08:56:05.689796493 +0000 | /root/btc-5m-twap/CryptoReports/TZ-04b-market-recorder-scoring-report.md
2026-10-27 06:58:55.866996422 +0000 | 2026-09-10 08:55:11.504594447 +0000 | /root/btc-5m-twap/CryptoReports/TZ-04-market-recorder-report.md
2026-10-27 06:58:55.869996445 +0000 | 2026-09-12 11:53:06.638569436 +0000 | /root/btc-5m-twap/CryptoReports/TZ-05a-quote-capture-deploy-report.md
2026-10-27 06:58:55.869996445 +0000 | 2026-09-12 08:56:06.143799981 +0000 | /root/btc-5m-twap/CryptoReports/TZ-05-quote-capture-report.md
2026-10-27 06:58:55.870996453 +0000 | 2026-09-14 05:12:55.672596520 +0000 | /root/btc-5m-twap/CryptoReports/TZ-06-pfair-calibration-report.md
2026-10-27 06:58:55.872996468 +0000 | 2026-09-14 05:12:55.673596528 +0000 | /root/btc-5m-twap/CryptoReports/TZ-07a-variance-time-report.md
2026-10-27 06:58:55.873996476 +0000 | 2026-09-14 05:12:55.674596537 +0000 | /root/btc-5m-twap/CryptoReports/TZ-07b-settlement-dispersion-report.md
2026-10-27 06:58:55.871996461 +0000 | 2026-09-14 05:12:55.673596528 +0000 | /root/btc-5m-twap/CryptoReports/TZ-07-variance-time-report.md
2026-10-27 06:58:55.876996499 +0000 | 2026-09-14 05:12:55.675596546 +0000 | /root/btc-5m-twap/CryptoReports/TZ-08a-out-of-sample-report.md
2026-10-27 06:58:55.875996491 +0000 | 2026-09-14 05:12:55.674596537 +0000 | /root/btc-5m-twap/CryptoReports/TZ-08-out-of-sample-report.md
2026-10-27 06:58:55.878996515 +0000 | 2026-09-14 05:12:56.409602903 +0000 | /root/btc-5m-twap/CryptoReports/TZ-09-disk-inventory-report.md
2026-10-27 06:58:55.880996530 +0000 | 2026-09-14 06:30:01.491751942 +0000 | /root/btc-5m-twap/CryptoReports/TZ-10a-sigma-or-link-report.md
2026-10-27 06:58:55.881996538 +0000 | 2026-09-14 11:14:04.120342684 +0000 | /root/btc-5m-twap/CryptoReports/TZ-10b-sigma-or-link-report.md
2026-10-27 06:58:55.880996530 +0000 | 2026-09-14 05:42:20.918554926 +0000 | /root/btc-5m-twap/CryptoReports/TZ-10-sigma-or-link-report.md
2026-10-27 06:58:55.888996592 +0000 | 2026-09-15 05:06:01.029843486 +0000 | /root/btc-5m-twap/CryptoReports/TZ-11a-student-link-and-domain-report.md
2026-10-27 06:58:55.886996576 +0000 | 2026-09-14 15:56:07.255601902 +0000 | /root/btc-5m-twap/CryptoReports/TZ-11-student-link-and-domain-report.md
2026-10-27 06:58:55.895996646 +0000 | 2026-09-15 21:13:14.013419367 +0000 | /root/btc-5m-twap/CryptoReports/TZ-12-sized-gate-report.md
2026-10-27 06:58:55.897996661 +0000 | 2026-09-18 04:39:57.960527535 +0000 | /root/btc-5m-twap/CryptoReports/TZ-13-sized-gate-test3-report.md
2026-10-27 06:58:55.899996677 +0000 | 2026-09-18 20:18:36.011271903 +0000 | /root/btc-5m-twap/CryptoReports/TZ-14-quote-inventory-report.md
2026-10-27 06:58:55.902996700 +0000 | 2026-09-22 13:41:42.960346029 +0000 | /root/btc-5m-twap/CryptoReports/TZ-15-phase2-gate-report.md
2026-10-27 06:58:55.905996723 +0000 | 2026-10-03 22:32:36.949643607 +0000 | /root/btc-5m-twap/CryptoReports/TZ-16a-phase2-decisive-gate-report.md
2026-10-27 06:58:55.903996708 +0000 | 2026-09-27 12:03:58.048375353 +0000 | /root/btc-5m-twap/CryptoReports/TZ-16-phase2-decisive-gate-report.md
2026-10-27 06:58:55.908996746 +0000 | 2026-09-22 14:07:35.920340794 +0000 | /root/btc-5m-twap/CryptoReports/TZ-17-settlement-chain-report.md
2026-10-27 06:58:55.912996777 +0000 | 2026-09-27 07:45:02.760306232 +0000 | /root/btc-5m-twap/CryptoReports/TZ-18a-chainbook-capture-redeploy-report.md
2026-10-27 06:58:55.910996762 +0000 | 2026-09-23 17:19:19.213718865 +0000 | /root/btc-5m-twap/CryptoReports/TZ-18-chainbook-capture-deploy-report.md
2026-10-27 06:58:55.913996785 +0000 | 2026-10-03 22:45:43.404346952 +0000 | /root/btc-5m-twap/CryptoReports/TZ-19-phase2-second-look-report.md
2026-10-27 06:58:55.914996793 +0000 | 2026-10-04 08:35:40.601914139 +0000 | /root/btc-5m-twap/CryptoReports/TZ-20-capture-under-systemd-report.md
2026-10-27 06:58:55.917996816 +0000 | 2026-10-05 00:48:00.181110381 +0000 | /root/btc-5m-twap/CryptoReports/TZ-21-recorder-memory-report.md
2026-10-27 06:58:55.921996847 +0000 | 2026-10-09 19:25:25.357833750 +0000 | /root/btc-5m-twap/CryptoReports/TZ-23-maker-m0-report.md
2026-10-27 06:58:55.924996870 +0000 | 2026-10-10 08:42:03.039309362 +0000 | /root/btc-5m-twap/CryptoReports/TZ-24-nesting-b2-report.md
2026-10-27 06:58:55.927996893 +0000 | 2026-10-10 20:42:56.473215353 +0000 | /root/btc-5m-twap/CryptoReports/TZ-26-nesting-b3-capture-report.md
2026-10-27 06:58:55.930996916 +0000 | 2026-10-11 08:51:34.359652731 +0000 | /root/btc-5m-twap/CryptoReports/TZ-27-pairbook-archive-report.md
2026-10-27 06:58:55.934996947 +0000 | 2026-10-11 15:39:31.936930274 +0000 | /root/btc-5m-twap/CryptoReports/TZ-28-pairbook-archive-timer-report.md
2026-10-27 06:58:55.938996978 +0000 | 2026-10-20 05:16:26.790747325 +0000 | /root/btc-5m-twap/CryptoReports/TZ-29-maker-m0-second-look-report.md
2026-10-27 06:58:55.944997025 +0000 | 2026-10-22 04:56:44.767718930 +0000 | /root/btc-5m-twap/CryptoReports/TZ-30-nesting-b3-measure-report.md
2026-10-27 06:58:55.947997048 +0000 | 2026-10-23 13:08:59.383666181 +0000 | /root/btc-5m-twap/CryptoReports/TZ-31-who-earns-report.md
2026-10-27 07:53:58.495369205 +0000 | 2026-10-27 07:53:58.488369126 +0000 | /root/btc-5m-twap/CryptoReports/TZ-32-our-quoting-report.md
Every report's atime is 2026-10-27, within 24 h of 06:28 UTC on 2026-10-28 and after its mtime, so a read at 06:28 would not have moved it: the record neither confirms nor refutes the statement.
$ for f in CryptoReports/*.md: atime (s) not after mtime (s)?
atime not after mtime at whole seconds: TZ-32-our-quoting-report.md 1793087638 1793087638
$ TZ=UTC stat -c "atime %x / mtime %y / ctime %z" TZ-32-our-quoting-report.md
atime 2026-10-27 07:53:58.495369205 +0000 / mtime 2026-10-27 07:53:58.488369126 +0000 / ctime 2026-10-27 07:53:58.488369126 +0000
TZ-32's report: atime 7 ms after its mtime and ctime, so the premise holds at all 43 reports.
$ ls /root/btc-5m-twap/CryptoReports/*.md | wc -l
42
Correction to the line above: the premise holds at all 42 reports, not 43.
```

B-RECLAIM-SCRATCH's outcome is therefore what §9 asks — the four earlier directories gone, `test -e` exit `1` at each,
none live and not this session's own — **but its order is not on record: no `RECLAIM PASS` was printed in any output this
session holds before the removal** (§6).

### 2.5 §3.4 — the service's copy (V5)

`logs/40-copy.log` — `mkdir` exit `0`; the copy's SHA-256 and the worktree's both Appendix A's `a276bbb9…`;
`commit.txt` 41 bytes, the branch head's 40 hex characters and a newline, equal to the worktree's `HEAD`:

```
$ mkdir /root/btc-rewardbook-svc
exit=0
show exit=0
rev-parse exit=0
a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670  /root/btc-rewardbook-svc/tz33-reward-book-capture.py
a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670  /root/tz33-work/wt/research/tz33-reward-book-capture.py
2dcd70e08b18b93c64bb67d9849ac1216ce40e41
2dcd70e08b18b93c64bb67d9849ac1216ce40e41
41 /root/btc-rewardbook-svc/commit.txt
```

### 2.6 §3.5 — P-START (V6): **served**

`logs/50-prestart.log`, the copy itself, run from `/root/tz33-work`, verbatim. `MemAvailable` `288186368` at its start,
above the floor; no process under the service's argv; the archive's service `inactive` after 0 s; **6 requests**, every
one `200` and parsing as JSON; each market's gamma and CLOB verdicts printed, not gated; **1 stream session**, the seven
checks `True`; `READING P-START: served`.

```
[2026-10-28T06:33:45Z] MemAvailable 288186368 bytes, floor 135569408
[2026-10-28T06:33:45Z] file /root/btc-rewardbook-svc/tz33-reward-book-capture.py sha256 a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670
[2026-10-28T06:33:45Z] free 11519152128 bytes at /var/lib; proxy variables in the environment: 0
[2026-10-28T06:33:45Z] processes under the service's argv: []
[2026-10-28T06:33:45Z] the pair book's archive: inactive after 0 s
[2026-10-28T06:33:46Z] base rate recorder: 2016 units, 2016 read, 2 failing
[2026-10-28T06:33:46Z] base rate pairbook: 672 units, 672 read, 2 failing
[2026-10-28T06:33:46Z] G-NEIGHBORS' false failure at the base rates over 16 intervals and 5 windows: 0.0303150318
[2026-10-28T06:33:47Z] market 0x002341871854e39158ec683fd0583a3000210a5f31ce5cc4a4b3cc7aec1ed900: gamma verdict ends within 14 days of the day's end, CLOB verdict pass
[2026-10-28T06:33:47Z] market 0x0038a19c5f1633b76e9fe194ac391959811cceb05652ba5c6796e37f045e573f: gamma verdict ends within 14 days of the day's end, CLOB verdict tag oil
[2026-10-28T06:33:47Z] request listing https://clob.polymarket.com/rewards/markets/current?next_cursor=MA==: status 200, 175550 bytes, sha256 bbbbf63b4a66106fe260e995ab1ed2db0db3d8c2c27a38ed8a16b6039ffdef26, JSON True, 638357895 ns
[2026-10-28T06:33:47Z] request gamma https://gamma-api.polymarket.com/markets?limit=100&condition_ids=0x002341871854e39158ec683fd0583a3000210a5f31ce5cc4a4b3cc7aec1ed900&condition_ids=0x0038a19c5f1633b76e9fe194ac391959811cceb05652ba5c6796e37f045e573f: status 200, 17384 bytes, sha256 568bdbba8d9378f42927bcae7a7b10e2b1a3e1bd9eb8969eb1f3d4b12c734a9b, JSON True, 57684253 ns
[2026-10-28T06:33:47Z] request clob https://clob.polymarket.com/markets/0x002341871854e39158ec683fd0583a3000210a5f31ce5cc4a4b3cc7aec1ed900: status 200, 3109 bytes, sha256 232c74190ad305f9eb3adbfdc3f451751dc9aa547ff4b187beaf390540f677b6, JSON True, 43482528 ns
[2026-10-28T06:33:47Z] request clob https://clob.polymarket.com/markets/0x0038a19c5f1633b76e9fe194ac391959811cceb05652ba5c6796e37f045e573f: status 200, 4398 bytes, sha256 37194afc1813258a133c7c03db1f972a5eb423a5198d3bcd009a69d9717ff90a, JSON True, 45314891 ns
[2026-10-28T06:33:47Z] request rewards https://clob.polymarket.com/rewards/markets/0x002341871854e39158ec683fd0583a3000210a5f31ce5cc4a4b3cc7aec1ed900: status 200, 985 bytes, sha256 7914cfa2975e2e383bcf38f653197836cc965749ffba5db3060068eb064b0887, JSON True, 58471588 ns
[2026-10-28T06:33:47Z] request rewards https://clob.polymarket.com/rewards/markets/0x0038a19c5f1633b76e9fe194ac391959811cceb05652ba5c6796e37f045e573f: status 200, 991 bytes, sha256 3751a86144bdd273b8cac4093065119bebdf6e71a1e984b34db21e0b2ffd6b41, JSON True, 80222781 ns
[2026-10-28T06:34:13Z] P-START one session    True
[2026-10-28T06:34:13Z] P-START 101            True
[2026-10-28T06:34:13Z] P-START subscribed     True
[2026-10-28T06:34:13Z] P-START initial books  True
[2026-10-28T06:34:13Z] P-START heartbeat      True
[2026-10-28T06:34:13Z] P-START conforming     True
[2026-10-28T06:34:13Z] P-START whole file     True
[2026-10-28T06:34:13Z] the session: 483 frames, 309460 frame bytes, 2 pongs, 2 pings, 43276 stored bytes, largest gap 938830485 ns
[2026-10-28T06:34:13Z] wrote /root/tz33-work/prestart/prestart.json sha256 86f5f2853cafc9919b5a6a71a30d407972a6451e78802e5f2a5927960a8b1892
[2026-10-28T06:34:13Z] wrote /root/tz33-work/prestart/stream.jsonl.gz sha256 609c81fe54d984033b7dc3ed965c31c64bff0a24d870f190c4a255e84f607f6e, 43276 bytes
[2026-10-28T06:34:13Z] READING P-START: served
[2026-10-28T06:34:13Z] peak memory of this run: 45084672 bytes
[2026-10-28T06:34:13Z] opens refused: 0; manifest opens 2016; window opens 672; ledger opens 0; requests 6, stream sessions 1
exit=0
2026-10-28T06:34:13.780337212Z
```

**The neighbours' base rates**, as `prestart` printed them: the recorder's 2,016 five-minute intervals closed by 600 s
before it, **`m_r` = 2016 read, `f_r` = 2 failing**; the pair book's 672 windows whose `window.json` was due by 60 s
before it, **`m_p` = 672 read, `f_p` = 2 failing**; **G-NEIGHBORS' false failure at those rates over 16 intervals and
5 windows, `0.0303150318`**, to ten decimals — the family-wise false failure is at most `0.0129537856`, G-STREAM's, G-REWARDS' and
G-RESUME's, plus that figure (§4). The manifest and window opens, `2016` and `672`, are V15's.

| file | SHA-256 | bytes |
|---|---|---|
| `/root/tz33-work/prestart/prestart.json` | `86f5f2853cafc9919b5a6a71a30d407972a6451e78802e5f2a5927960a8b1892` | 3,796 |
| `/root/tz33-work/prestart/stream.jsonl.gz` | `609c81fe54d984033b7dc3ed965c31c64bff0a24d870f190c4a255e84f607f6e` | 43,276 |

P-START exited at 06:34:13.78 UTC; B-ENABLE's block started at 06:37:45.18, inside §3.7's 3,600 s, so `prestart-2` was
not needed.

### 2.7 §3.6 — B-INSTALL (V7)

`logs/60-install.log` — both `install`, `cmp`, `daemon-reload` and `systemd-analyze verify` exit `0`; `verify` printed no
finding. None of the five lines was refused.

```
2026-10-28T06:34:32.320891810Z
exit=0
exit=0
exit=0
exit=0
exit=0
2026-10-28T06:34:32.789228000Z
```

### 2.8 §3.7 — the start, B-ENABLE, then G-UNIT and G-START (V8)

`I mark start-svc` at 06:34:54 UTC, before the block was run or handed over (`logs/70-mark-start-svc.log`):

```
[2026-10-28T06:34:54Z] mark start-svc at 2026-10-28T06:34:54Z: btc-rewardbook.service {'ns': 1793169294271237150, 'unit': 'btc-rewardbook.service', 'MainPID': '0', 'NRestarts': '0', 'ActiveState': 'inactive'}
[2026-10-28T06:34:54Z] peak memory of this run: 39317504 bytes
[2026-10-28T06:34:54Z] opens refused: 0; manifest opens 0; window opens 0; ledger opens 0; requests 0, stream sessions 0
exit=0
```

**The session's classifier refused B-ENABLE** at 06:35:17 UTC as "[Unauthorized Persistence]", as it refused `enable
--now` at TZ-20, TZ-26 and TZ-28; nothing of the block ran (`logs/71-enable-refused.log`). It was handed to the Boss,
verbatim but for its log's name and one `date` line before the wait, which records the block's own start against §3.7's
3,600 s:

```
2026-10-28T06:35:17.487280264Z
B-ENABLE: refused by the session's permission classifier as [Unauthorized Persistence]; nothing of the block ran (the start-svc mark was taken at 2026-10-28T06:34:54Z). Handed to the Boss by TZ-33 section 3's route; the block must start by 2026-10-28T07:34:13Z, 3,600 s after P-START's exit at 06:34:13.78, or section 3.5 runs again into prestart-2.
```

**The first hand-over lapsed.** The Boss's block started at 06:37:45 UTC, inside §3.7's 3,600 s after P-START's exit, in a root login
from 06:37:39 to 06:54:08 UTC; the login ended before the band opened at 07:15:15, and the block's wait ended with it,
so `systemctl enable --now` never ran — `logs/71-enable.log` holds the start line alone:

```
2026-10-28T06:37:45.178747279Z
```

Between the two hand-overs the session's container was restarted, and the Executor read the units at 11:00:54 UTC
(`logs/72-after-container-restart.log`): `btc-rewardbook.service` `inactive`, `dead`, `UnitFileState=disabled`,
`NRestarts=0`, no `ActiveEnterTimestamp` — never started; the recorder unchanged; **the pair book restarted by the
archive's run off its calendar at 06:44:33 UTC** (§2.13), pid `3078426`, `NRestarts=10`, active since 06:48:06:

```
2026-10-28T11:00:54.157918993Z
MainPID=0
NRestarts=0
Id=btc-rewardbook.service
ActiveState=inactive
SubState=dead
UnitFileState=disabled
ActiveEnterTimestamp=
InactiveEnterTimestamp=

MainPID=2388318
NRestarts=0
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC
InactiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC

MainPID=3078426
NRestarts=10
Id=btc-pairbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Wed 2026-10-28 06:48:06 UTC
InactiveEnterTimestamp=Wed 2026-10-28 06:48:01 UTC

MainPID=0
NRestarts=0
Id=btc-pairbook-archive.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=
InactiveEnterTimestamp=Wed 2026-10-28 07:00:41 UTC

LastTriggerUSec=Wed 2026-10-28 06:44:33 UTC
Id=btc-pairbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-11 15:08:11 UTC
InactiveEnterTimestamp=
disabled
exit=1
root     pts/2        tmux(3114896).%1 Wed Oct 28 10:52:26 2026   still logged in
root     pts/1        tmux(3114896).%0 Wed Oct 28 10:52:24 2026   still logged in
root     pts/0        45.154.88.66     Wed Oct 28 10:49:33 2026 - Wed Oct 28 10:58:47 2026  (00:09)
root     pts/0        45.154.88.66     Wed Oct 28 10:49:06 2026 - Wed Oct 28 10:49:28 2026  (00:00)
root     pts/0        45.154.88.64     Wed Oct 28 06:37:39 2026 - Wed Oct 28 06:54:08 2026  (00:16)
root     pts/0        45.154.88.64     Wed Oct 28 06:30:27 2026 - Wed Oct 28 06:32:19 2026  (00:01)
root     pts/0        45.154.88.64     Wed Oct 28 06:28:06 2026 - Wed Oct 28 06:28:47 2026  (00:00)
root     pts/2        tmux(2875239).%1 Mon Oct 26 18:11:48 2026 - Wed Oct 28 10:51:18 2026 (1+16:39)

wtmp begins Wed Apr  1 20:16:20 2026
```

More than 3,600 s had then passed after P-START's exit, so **§3.5 ran again once, into `prestart-2`**, served, exit
11:01:53.06 UTC (§2.6 and `logs/51-prestart-2.log`). `mark` refuses a second `start-svc`, so the 06:34:54 mark stands
(`logs/73-enable-first-handover-lapsed.log`; §6):

```
2026-10-28T11:02:05.865271406Z
B-ENABLE, first hand-over: the Boss's block started at 2026-10-28T06:37:45.178747279Z (its first line, logs/71-enable.log) in the root login 06:37:39-06:54:08 UTC (last); that login ended before the band opened at 07:15:15, and the until-loop ended with it: logs/71-enable.log holds no band instant and no exit line, and at 11:00:54 btc-rewardbook.service read inactive, dead, UnitFileState disabled, NRestarts 0, no ActiveEnterTimestamp (logs/72-after-container-restart.log). systemctl enable --now never ran; the unit never started; /var/lib/btc-rewardbook holds no start record by that reading. More than 3,600 s then passed after P-START's exit (06:34:13.78), so section 3.5 ran again once, into prestart-2 (logs/51-prestart-2.log), served, exit 11:01:53.06. The start-svc mark of 06:34:54 stands: mode mark refuses a second start-svc (assert name not in marks). The block is handed to the Boss again, unretried by the Executor (the classifier refused it at 06:35:17 as [Unauthorized Persistence]).
```

**The second hand-over, run by the Boss in a root shell** — `logs/74-enable.log`, written into the work tree by the
block itself: started 11:30:02.65 UTC, inside 3,600 s of `prestart-2`'s exit; the band reached at **11:30:15.68**, second 15
of the quarter hour, inside 07:15:00 to 00:55:00 UTC; `systemctl enable --now` exit `0`, the enable link created:

```
2026-10-28T11:30:02.645265276Z
2026-10-28T11:30:15.679400342Z
Created symlink /etc/systemd/system/multi-user.target.wants/btc-rewardbook.service → /etc/systemd/system/btc-rewardbook.service.
exit=0
```

**`I unit 0`, at 11:31:17 UTC, at least 60 s after the block** — **G-UNIT PASS at 0 restarts, 11 of 11; G-START PASS, 8 of 8** — the one `start`
record, of pid `3119051` at 11:30:16 UTC, after the mark, its commit `commit.txt`'s, its file the copy's, its argv the
file and `serve`, its headers P-START's two, glibc tuned (`logs/75-unit-0.log`):

```
[2026-10-28T11:31:17Z] G-START: the start record of pid 3119051 at 2026-10-28T11:30:16Z, commit 2dcd70e08b18b93c64bb67d9849ac1216ce40e41, file a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670
[2026-10-28T11:31:17Z] G-UNIT active           True
[2026-10-28T11:31:17Z] G-UNIT enabled          True
[2026-10-28T11:31:17Z] G-UNIT fragment         True
[2026-10-28T11:31:17Z] G-UNIT control group    True
[2026-10-28T11:31:17Z] G-UNIT ceiling          True
[2026-10-28T11:31:17Z] G-UNIT nice             True
[2026-10-28T11:31:17Z] G-UNIT restarts         True
[2026-10-28T11:31:17Z] G-UNIT argv             True
[2026-10-28T11:31:17Z] G-UNIT cwd              True
[2026-10-28T11:31:17Z] G-UNIT cgroup           True
[2026-10-28T11:31:17Z] G-UNIT sole instance    True
[2026-10-28T11:31:17Z] G-UNIT one start        True
[2026-10-28T11:31:17Z] G-UNIT start pid        True
[2026-10-28T11:31:17Z] G-UNIT start after mark True
[2026-10-28T11:31:17Z] G-UNIT commit           True
[2026-10-28T11:31:17Z] G-UNIT file             True
[2026-10-28T11:31:17Z] G-UNIT start argv       True
[2026-10-28T11:31:17Z] G-UNIT headers          True
[2026-10-28T11:31:17Z] G-UNIT malloc           True
[2026-10-28T11:31:17Z] btc-rewardbook.service MainPID 3119051, NRestarts 0, MemoryMax 201326592, MemoryCurrent 48291840, MemoryPeak 50339840
[2026-10-28T11:31:17Z] G-UNIT PASS at 0 restarts; G-START PASS
[2026-10-28T11:31:17Z] peak memory of this run: 39448576 bytes
[2026-10-28T11:31:17Z] opens refused: 0; manifest opens 0; window opens 0; ledger opens 0; requests 0, stream sessions 0
exit=0
```

`logs/76-health-1.log`, the three units at 11:32:11 UTC, `systemctl show` alone:

```
2026-10-28T11:32:11.286064859Z
MainPID=3119051
NRestarts=0
MemoryCurrent=48881664
MemoryPeak=50339840
Id=btc-rewardbook.service
ActiveState=active
SubState=running

MainPID=2388318
NRestarts=0
MemoryCurrent=108384256
MemoryPeak=302309376
Id=btc-recorder.service
ActiveState=active
SubState=running

MainPID=3078426
NRestarts=10
MemoryCurrent=21716992
MemoryPeak=83824640
Id=btc-pairbook.service
ActiveState=active
SubState=running
```

### 2.9 §3.8 — the proof: G-SELECT, G-STREAM, G-REWARDS and G-NEIGHBORS (V9, V10)

`s`, the first `start` record's instant, is 11:30:16 UTC. **`T1`**, the first slot whose `S − 5` lies at least 300 s
after it, is **`1793187900`, 11:45:00 UTC**, so the first deciding run was due at `T1 + 4,210`, `1793192110`, 12:55:10
UTC. The Executor's background wait started `I prove A` at that second, `A` = `1793192110`; it decided at its first
run, so no run printed NOT YET. `logs/80-prove-first.log`, verbatim:

```
A=1793192110
[2026-10-28T12:55:10Z] MemAvailable 276922368 bytes, floor 135569408
[2026-10-28T12:55:10Z] the service's first start: pid 3119051 at 2026-10-28T11:30:16Z
[2026-10-28T12:55:19Z] the pair book's archive: inactive after 0 s
[2026-10-28T12:55:19Z] G-SELECT day 1793145600 (2026-10-28T00:00:00Z): re-derived equal; attempt 0, 0 failed before it, 218 requests; members 150; listing {"conflicts": 0, "distinct": 14171, "dropped": {"rewards_min_size not positive": 68}, "pages": 29, "ranked": 14103, "rows": 14188}; walked 582; verdicts {"end date unreadable": 7, "ends within 14 days of the day's end": 387, "event end near the day": 11, "member": 150, "tag commodities": 1, "tag crypto": 5, "tag esports": 10, "tag gold": 1, "tag oil": 6, "tag sports": 2, "tag stocks": 1, "tag weather": 1}
[2026-10-28T12:55:19Z] slot 1793187000 2026-10-28T11:30:00Z qualifying False: ['joined late', 'late subscribe']; indices [{"error": null, "frames": 77804, "index": 0, "joined_late": true, "markets": 150, "segments": 1, "slot_json": true, "stopped": false, "stream_off": null, "stream_opened": true}]; stream {"bad_lines": 0, "closes": 1, "foreign": 0, "frames": 77804, "initial_tokens": 300, "lag_ms": {"max": 2336, "median": 15, "min": 12, "n": 77497, "p99": 62}, "last_close_offset_ms": 906030, "max_gap_ns": 1151734876, "nonconforming": 0, "pings": 84, "pongs": 84, "stored_bytes": 9629579, "subscribe_offset_ms": 64640, "subscribes": 1, "torn": 0, "types": [["book", 448], ["last_trade_price", 74], ["price_change", 77497]]}; polls {"lines": 430, "mismatched": 0, "rows": 430, "scheduled": 450, "served": 430, "statuses": {"200": 430}, "unreadable": 0}
[2026-10-28T12:55:19Z] slot 1793187900 2026-10-28T11:45:00Z qualifying True: complete; indices [{"error": null, "frames": 78151, "index": 0, "joined_late": false, "markets": 150, "segments": 1, "slot_json": true, "stopped": false, "stream_off": null, "stream_opened": true}]; stream {"bad_lines": 0, "closes": 1, "foreign": 0, "frames": 78151, "initial_tokens": 300, "lag_ms": {"max": 411, "median": 19, "min": 17, "n": 77808, "p99": 61}, "last_close_offset_ms": 906035, "max_gap_ns": 1070579837, "nonconforming": 0, "pings": 90, "pongs": 90, "stored_bytes": 9639138, "subscribe_offset_ms": -4837, "subscribes": 1, "torn": 0, "types": [["book", 468], ["last_trade_price", 84], ["price_change", 77808]]}; polls {"lines": 450, "mismatched": 0, "rows": 450, "scheduled": 450, "served": 450, "statuses": {"200": 450}, "unreadable": 0}
[2026-10-28T12:55:19Z] slot 1793188800 2026-10-28T12:00:00Z qualifying True: complete; indices [{"error": null, "frames": 85321, "index": 0, "joined_late": false, "markets": 150, "segments": 1, "slot_json": true, "stopped": false, "stream_off": null, "stream_opened": true}]; stream {"bad_lines": 0, "closes": 1, "foreign": 0, "frames": 85321, "initial_tokens": 300, "lag_ms": {"max": 1655, "median": 20, "min": 18, "n": 85002, "p99": 59}, "last_close_offset_ms": 906033, "max_gap_ns": 1393102033, "nonconforming": 0, "pings": 90, "pongs": 90, "stored_bytes": 10430786, "subscribe_offset_ms": -4834, "subscribes": 1, "torn": 0, "types": [["book", 452], ["last_trade_price", 76], ["price_change", 85002]]}; polls {"lines": 450, "mismatched": 0, "rows": 450, "scheduled": 450, "served": 450, "statuses": {"200": 450}, "unreadable": 0}
[2026-10-28T12:55:19Z] slot 1793189700 2026-10-28T12:15:00Z qualifying True: complete; indices [{"error": null, "frames": 88928, "index": 0, "joined_late": false, "markets": 150, "segments": 1, "slot_json": true, "stopped": false, "stream_off": null, "stream_opened": true}]; stream {"bad_lines": 0, "closes": 1, "foreign": 0, "frames": 88928, "initial_tokens": 300, "lag_ms": {"max": 1626, "median": 15, "min": 13, "n": 88588, "p99": 84}, "last_close_offset_ms": 906040, "max_gap_ns": 1062596056, "nonconforming": 0, "pings": 90, "pongs": 90, "stored_bytes": 10844068, "subscribe_offset_ms": -4857, "subscribes": 1, "torn": 0, "types": [["book", 466], ["last_trade_price", 83], ["price_change", 88588]]}; polls {"lines": 450, "mismatched": 0, "rows": 450, "scheduled": 450, "served": 450, "statuses": {"200": 450}, "unreadable": 0}
[2026-10-28T12:55:19Z] slot 1793190600 2026-10-28T12:30:00Z qualifying True: complete; indices [{"error": null, "frames": 96873, "index": 0, "joined_late": false, "markets": 150, "segments": 1, "slot_json": true, "stopped": false, "stream_off": null, "stream_opened": true}]; stream {"bad_lines": 0, "closes": 1, "foreign": 0, "frames": 96873, "initial_tokens": 300, "lag_ms": {"max": 911, "median": 24, "min": 22, "n": 96557, "p99": 96}, "last_close_offset_ms": 906049, "max_gap_ns": 1410278970, "nonconforming": 0, "pings": 90, "pongs": 90, "stored_bytes": 11422263, "subscribe_offset_ms": -4829, "subscribes": 1, "torn": 0, "types": [["book", 450], ["last_trade_price", 75], ["price_change", 96557]]}; polls {"lines": 450, "mismatched": 0, "rows": 450, "scheduled": 450, "served": 450, "statuses": {"200": 450}, "unreadable": 0}
[2026-10-28T12:55:19Z] neighbour recorder 1793187300 2026-10-28T11:35:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour recorder 1793187600 2026-10-28T11:40:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour recorder 1793187900 2026-10-28T11:45:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour recorder 1793188200 2026-10-28T11:50:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour recorder 1793188500 2026-10-28T11:55:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour recorder 1793188800 2026-10-28T12:00:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour recorder 1793189100 2026-10-28T12:05:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour recorder 1793189400 2026-10-28T12:10:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour recorder 1793189700 2026-10-28T12:15:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour recorder 1793190000 2026-10-28T12:20:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour recorder 1793190300 2026-10-28T12:25:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour recorder 1793190600 2026-10-28T12:30:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour recorder 1793190900 2026-10-28T12:35:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour recorder 1793191200 2026-10-28T12:40:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour pairbook 1793187000 2026-10-28T11:30:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour pairbook 1793187900 2026-10-28T11:45:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour pairbook 1793188800 2026-10-28T12:00:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour pairbook 1793189700 2026-10-28T12:15:00Z: counted True, ok True
[2026-10-28T12:55:19Z] neighbour pairbook 1793190600 2026-10-28T12:30:00Z: counted True, ok True
[2026-10-28T12:55:19Z] wrote /root/tz33-work/proof/proof-1793192110.json sha256 70ba7291b122421743c0287dd623fc268cb6be3dc0f5282879effe4b1fa73abf, 5799 bytes
[2026-10-28T12:55:19Z] STREAM RATE, barred: 4 qualifying slots, 349273 frames, 96.0 a second over their streams' 910 s; 42336255 stored bytes, 10584064 a slot, 1016070120 a day of 96 slots; the store's streams now 59752055 bytes, the cap 4000000000 in 3.88 days at that rate
[2026-10-28T12:55:19Z] READING G-SELECT: PASS, 1 of 1 days re-derived equal with 150 members
[2026-10-28T12:55:19Z] READING G-STREAM: PASS, 4 of 4 complete
[2026-10-28T12:55:19Z] READING G-REWARDS: PASS, 1800 of 1800 polls served
[2026-10-28T12:55:19Z] READING G-NEIGHBORS: HOLD, recorder 14 counted of 14, 0 failing, pairbook 5 counted of 5, 0 failing
[2026-10-28T12:55:19Z] peak memory of this run: 55386112 bytes
[2026-10-28T12:55:19Z] opens refused: 0; manifest opens 14; window opens 5; ledger opens 0; requests 0, stream sessions 0
exit=0
```

**The readings.**

| gate | population | count | PASS at | reading |
|---|---|---|---|---|
| **G-SELECT** | the one day holding a qualifying slot, `1793145600` (2026-10-28) | its first `ok` attempt, `0`, 0 failed before it, 218 requests, re-derived equal through `StoredFetch`; 150 members | every day re-derived equal with 150 | **PASS**, 1 of 1 |
| **G-STREAM** | the first 4 qualifying slots, 11:45, 12:00, 12:15 and 12:30 UTC | 4 complete | at least 3 of 4 | **PASS**, 4 of 4 |
| **G-REWARDS** | their 1,800 scheduled polls | 1,800 served | at least 1,782 | **PASS**, 1800 of 1800 |
| **G-NEIGHBORS** | the recorder's intervals and the pair book's windows inside `[s↑, H]`, `H` the fourth slot's `S + 905`, 12:45:05 UTC | recorder 14 counted of 14, 0 failing; pair book 5 counted of 5, 0 failing | none failing, at least 8 and 3 counted | **PASS (HOLD)** |

**G-SELECT's day**, as `prove` printed it, counts only: the listing 29 pages, 14,188 rows, 14,171 distinct, 0
conflicts, 14,103 ranked, 68 dropped for `rewards_min_size not positive`; 582 candidates walked; their verdicts —
150 members, 387 ending within 14 days of the day's end, 11 with an event end near the day, 7 with an end date
unreadable, 10 `esports`, 6 `oil`, 5 `crypto`, 2 `sports`, and one each `commodities`, `gold`, `stocks` and `weather`.

**Every considered slot**, from the printed rows — barred from every reading but its own gate:

| slot `S` | UTC | qualifying | reasons | frames | stored bytes | subscribe offset ms | largest gap ns | last close offset ms | `price_change` lag ms min / median / p99 / max | polls served of scheduled |
|---|---|---|---|---|---|---|---|---|---|---|
| `1793187000` | 11:30:00 | False | `joined late`, `late subscribe` | 77,804 | 9,629,579 | 64640 | 1151734876 | 906030 | 12 / 15 / 62 / 2336 | 430 of 450 |
| `1793187900` | 11:45:00 | True | complete | 78,151 | 9,639,138 | -4837 | 1070579837 | 906035 | 17 / 19 / 61 / 411 | 450 of 450 |
| `1793188800` | 12:00:00 | True | complete | 85,321 | 10,430,786 | -4834 | 1393102033 | 906033 | 18 / 20 / 59 / 1655 | 450 of 450 |
| `1793189700` | 12:15:00 | True | complete | 88,928 | 10,844,068 | -4857 | 1062596056 | 906040 | 13 / 15 / 84 / 1626 | 450 of 450 |
| `1793190600` | 12:30:00 | True | complete | 96,873 | 11,422,263 | -4829 | 1410278970 | 906049 | 22 / 24 / 96 / 911 | 450 of 450 |

Each slot held one index, `0`, one session segment, one `subscribe` and one `close`, 0 bad lines, 0 torn, 0 foreign and 0
nonconforming frames, and 300 initial tokens; the event types and the `PING`/`PONG` counts are in the log. The slot the
start joined, `1793187000`, is considered and not qualifying — its `S − 5` lies before `s + 300` — and is disclosed with
its two reasons as §4.3 asks; its 430 polls of 450 are its own, outside G-REWARDS. **The neighbours**, every one counted
and none failing: the recorder's 14 intervals `1793187300` … `1793191200`, 11:35 to 12:40 UTC, and the pair book's 5
windows `1793187000` … `1793190600`, 11:30 to 12:30 UTC.

**Determinism (V10)** — `I prove 1793192110` again, `logs/81-prove-second.log`: **`unchanged`**, `proof-1793192110.json`
SHA-256 `70ba7291b122421743c0287dd623fc268cb6be3dc0f5282879effe4b1fa73abf`, 5,799 bytes, the same four readings. Its
lines differ from the first run's in their stamps, its `MemAvailable` and peak, and one figure: the store's streams,
`60230433` bytes against `59752055`, a live count of the running store that the proof file does not carry.

```
A=1793192110
[2026-10-28T12:55:48Z] MemAvailable 274137088 bytes, floor 135569408
[2026-10-28T12:55:48Z] the service's first start: pid 3119051 at 2026-10-28T11:30:16Z
[2026-10-28T12:55:57Z] the pair book's archive: inactive after 0 s
[2026-10-28T12:55:57Z] G-SELECT day 1793145600 (2026-10-28T00:00:00Z): re-derived equal; attempt 0, 0 failed before it, 218 requests; members 150; listing {"conflicts": 0, "distinct": 14171, "dropped": {"rewards_min_size not positive": 68}, "pages": 29, "ranked": 14103, "rows": 14188}; walked 582; verdicts {"end date unreadable": 7, "ends within 14 days of the day's end": 387, "event end near the day": 11, "member": 150, "tag commodities": 1, "tag crypto": 5, "tag esports": 10, "tag gold": 1, "tag oil": 6, "tag sports": 2, "tag stocks": 1, "tag weather": 1}
[2026-10-28T12:55:57Z] slot 1793187000 2026-10-28T11:30:00Z qualifying False: ['joined late', 'late subscribe']; indices [{"error": null, "frames": 77804, "index": 0, "joined_late": true, "markets": 150, "segments": 1, "slot_json": true, "stopped": false, "stream_off": null, "stream_opened": true}]; stream {"bad_lines": 0, "closes": 1, "foreign": 0, "frames": 77804, "initial_tokens": 300, "lag_ms": {"max": 2336, "median": 15, "min": 12, "n": 77497, "p99": 62}, "last_close_offset_ms": 906030, "max_gap_ns": 1151734876, "nonconforming": 0, "pings": 84, "pongs": 84, "stored_bytes": 9629579, "subscribe_offset_ms": 64640, "subscribes": 1, "torn": 0, "types": [["book", 448], ["last_trade_price", 74], ["price_change", 77497]]}; polls {"lines": 430, "mismatched": 0, "rows": 430, "scheduled": 450, "served": 430, "statuses": {"200": 430}, "unreadable": 0}
[2026-10-28T12:55:57Z] slot 1793187900 2026-10-28T11:45:00Z qualifying True: complete; indices [{"error": null, "frames": 78151, "index": 0, "joined_late": false, "markets": 150, "segments": 1, "slot_json": true, "stopped": false, "stream_off": null, "stream_opened": true}]; stream {"bad_lines": 0, "closes": 1, "foreign": 0, "frames": 78151, "initial_tokens": 300, "lag_ms": {"max": 411, "median": 19, "min": 17, "n": 77808, "p99": 61}, "last_close_offset_ms": 906035, "max_gap_ns": 1070579837, "nonconforming": 0, "pings": 90, "pongs": 90, "stored_bytes": 9639138, "subscribe_offset_ms": -4837, "subscribes": 1, "torn": 0, "types": [["book", 468], ["last_trade_price", 84], ["price_change", 77808]]}; polls {"lines": 450, "mismatched": 0, "rows": 450, "scheduled": 450, "served": 450, "statuses": {"200": 450}, "unreadable": 0}
[2026-10-28T12:55:57Z] slot 1793188800 2026-10-28T12:00:00Z qualifying True: complete; indices [{"error": null, "frames": 85321, "index": 0, "joined_late": false, "markets": 150, "segments": 1, "slot_json": true, "stopped": false, "stream_off": null, "stream_opened": true}]; stream {"bad_lines": 0, "closes": 1, "foreign": 0, "frames": 85321, "initial_tokens": 300, "lag_ms": {"max": 1655, "median": 20, "min": 18, "n": 85002, "p99": 59}, "last_close_offset_ms": 906033, "max_gap_ns": 1393102033, "nonconforming": 0, "pings": 90, "pongs": 90, "stored_bytes": 10430786, "subscribe_offset_ms": -4834, "subscribes": 1, "torn": 0, "types": [["book", 452], ["last_trade_price", 76], ["price_change", 85002]]}; polls {"lines": 450, "mismatched": 0, "rows": 450, "scheduled": 450, "served": 450, "statuses": {"200": 450}, "unreadable": 0}
[2026-10-28T12:55:57Z] slot 1793189700 2026-10-28T12:15:00Z qualifying True: complete; indices [{"error": null, "frames": 88928, "index": 0, "joined_late": false, "markets": 150, "segments": 1, "slot_json": true, "stopped": false, "stream_off": null, "stream_opened": true}]; stream {"bad_lines": 0, "closes": 1, "foreign": 0, "frames": 88928, "initial_tokens": 300, "lag_ms": {"max": 1626, "median": 15, "min": 13, "n": 88588, "p99": 84}, "last_close_offset_ms": 906040, "max_gap_ns": 1062596056, "nonconforming": 0, "pings": 90, "pongs": 90, "stored_bytes": 10844068, "subscribe_offset_ms": -4857, "subscribes": 1, "torn": 0, "types": [["book", 466], ["last_trade_price", 83], ["price_change", 88588]]}; polls {"lines": 450, "mismatched": 0, "rows": 450, "scheduled": 450, "served": 450, "statuses": {"200": 450}, "unreadable": 0}
[2026-10-28T12:55:57Z] slot 1793190600 2026-10-28T12:30:00Z qualifying True: complete; indices [{"error": null, "frames": 96873, "index": 0, "joined_late": false, "markets": 150, "segments": 1, "slot_json": true, "stopped": false, "stream_off": null, "stream_opened": true}]; stream {"bad_lines": 0, "closes": 1, "foreign": 0, "frames": 96873, "initial_tokens": 300, "lag_ms": {"max": 911, "median": 24, "min": 22, "n": 96557, "p99": 96}, "last_close_offset_ms": 906049, "max_gap_ns": 1410278970, "nonconforming": 0, "pings": 90, "pongs": 90, "stored_bytes": 11422263, "subscribe_offset_ms": -4829, "subscribes": 1, "torn": 0, "types": [["book", 450], ["last_trade_price", 75], ["price_change", 96557]]}; polls {"lines": 450, "mismatched": 0, "rows": 450, "scheduled": 450, "served": 450, "statuses": {"200": 450}, "unreadable": 0}
[2026-10-28T12:55:57Z] neighbour recorder 1793187300 2026-10-28T11:35:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour recorder 1793187600 2026-10-28T11:40:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour recorder 1793187900 2026-10-28T11:45:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour recorder 1793188200 2026-10-28T11:50:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour recorder 1793188500 2026-10-28T11:55:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour recorder 1793188800 2026-10-28T12:00:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour recorder 1793189100 2026-10-28T12:05:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour recorder 1793189400 2026-10-28T12:10:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour recorder 1793189700 2026-10-28T12:15:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour recorder 1793190000 2026-10-28T12:20:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour recorder 1793190300 2026-10-28T12:25:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour recorder 1793190600 2026-10-28T12:30:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour recorder 1793190900 2026-10-28T12:35:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour recorder 1793191200 2026-10-28T12:40:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour pairbook 1793187000 2026-10-28T11:30:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour pairbook 1793187900 2026-10-28T11:45:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour pairbook 1793188800 2026-10-28T12:00:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour pairbook 1793189700 2026-10-28T12:15:00Z: counted True, ok True
[2026-10-28T12:55:57Z] neighbour pairbook 1793190600 2026-10-28T12:30:00Z: counted True, ok True
[2026-10-28T12:55:57Z] unchanged /root/tz33-work/proof/proof-1793192110.json sha256 70ba7291b122421743c0287dd623fc268cb6be3dc0f5282879effe4b1fa73abf
[2026-10-28T12:55:57Z] STREAM RATE, barred: 4 qualifying slots, 349273 frames, 96.0 a second over their streams' 910 s; 42336255 stored bytes, 10584064 a slot, 1016070120 a day of 96 slots; the store's streams now 60230433 bytes, the cap 4000000000 in 3.88 days at that rate
[2026-10-28T12:55:57Z] READING G-SELECT: PASS, 1 of 1 days re-derived equal with 150 members
[2026-10-28T12:55:57Z] READING G-STREAM: PASS, 4 of 4 complete
[2026-10-28T12:55:57Z] READING G-REWARDS: PASS, 1800 of 1800 polls served
[2026-10-28T12:55:57Z] READING G-NEIGHBORS: HOLD, recorder 14 counted of 14, 0 failing, pairbook 5 counted of 5, 0 failing
[2026-10-28T12:55:57Z] peak memory of this run: 55783424 bytes
[2026-10-28T12:55:57Z] opens refused: 0; manifest opens 14; window opens 5; ledger opens 0; requests 0, stream sessions 0
exit=0
```

### 2.10 The stream's measured rate, over G-STREAM's four slots (TZ §8)

As `prove` printed it, barred from every reading: **4 qualifying slots, 349,273 frames, 96.0 a second over their
streams' 910 s; 42,336,255 stored bytes, 10,584,064 a slot, 1,016,070,120 a day of 96 slots; the store's streams
59,752,055 bytes at the first run, the cap `4000000000` in 3.88 days at that rate.** It lies inside the Architect's
ranges of §1 — `68.1` to `99.1` frames a second and `8,108,877` to `10,869,869` stored bytes a slot — on a Wednesday
midday UTC. §1's modelled order of the bounds stands: the stream floor binds first at the pair book's daily peak, and
moving this store's streams to Release assets is due before the third day.

### 2.11 G-LOAD (V11)

`logs/82-load.log`, at 12:56:09 UTC: **`0.0262` of one core, 135.24 s of processor over 5,153.8 s since 11:30:15 UTC,
against the bound `0.10` — PASS.** The unit's `memory.current` `21725184`, `memory.peak` `50339840`, swap `31629312`;
`anon` `15724544`, `file` `5287936`, `kernel` `634880`, `sock` `0`, `file_dirty` `77824`, `file_writeback` `0`; the
process's `VmRSS` 23,704 kB, `VmHWM` 57,456 kB, `VmSwap` 30,024 kB, 2 threads.

```
[2026-10-28T12:56:09Z] memory.current 21725184
[2026-10-28T12:56:09Z] memory.peak 50339840
[2026-10-28T12:56:09Z] memory.swap.current 31629312
[2026-10-28T12:56:09Z] memory.swap.peak 31629312
[2026-10-28T12:56:09Z] stat.anon 15724544
[2026-10-28T12:56:09Z] stat.file 5287936
[2026-10-28T12:56:09Z] stat.kernel 634880
[2026-10-28T12:56:09Z] stat.sock 0
[2026-10-28T12:56:09Z] stat.file_dirty 77824
[2026-10-28T12:56:09Z] stat.file_writeback 0
[2026-10-28T12:56:09Z] process 3119051 VmHWM:	   57456 kB
[2026-10-28T12:56:09Z] process 3119051 VmRSS:	   23704 kB
[2026-10-28T12:56:09Z] process 3119051 VmSwap:	   30024 kB
[2026-10-28T12:56:09Z] process 3119051 Threads:	2
[2026-10-28T12:56:09Z] G-LOAD: process 3119051, processor 135.24 s over 5153.8 s since 2026-10-28T11:30:15Z: 0.0262 of one core, bound 0.10
[2026-10-28T12:56:09Z] G-LOAD PASS
[2026-10-28T12:56:09Z] peak memory of this run: 39186432 bytes
[2026-10-28T12:56:09Z] opens refused: 0; manifest opens 0; window opens 0; ledger opens 0; requests 0, stream sessions 0
exit=0
```

### 2.12 §3.9 — the restart: G-RESTART and G-RESUME (V12, V13)

Only after every reading of §3.7 and §3.8 read PASS. `I mark kill-svc` at 12:56:17 UTC, `MainPID` `3119051`
(`logs/90-mark-kill-svc.log`):

```
[2026-10-28T12:56:17Z] mark kill-svc at 2026-10-28T12:56:17Z: btc-rewardbook.service {'ns': 1793192177982816393, 'unit': 'btc-rewardbook.service', 'MainPID': '3119051', 'NRestarts': '0', 'ActiveState': 'active'}
[2026-10-28T12:56:17Z] peak memory of this run: 39186432 bytes
[2026-10-28T12:56:17Z] opens refused: 0; manifest opens 0; window opens 0; ledger opens 0; requests 0, stream sessions 0
exit=0
```

**B-KILL-SVC, run by the Executor, not refused** (`logs/91-kill-svc.log`): its band reached at once, **12:56:22.65 UTC,
second 682** of the quarter hour, inside 15 to 780; `systemctl kill --signal=SIGTERM` exit `0`.

```
2026-10-28T12:56:22.651210899Z
exit=0
```

**`I restart`**, 30 s after it (`logs/92-restart.log`) — **G-RESTART PASS:** since the mark, exactly the `stop` of
`3119051` at 12:56:23 UTC and the `start` of `3137952` at 12:56:29, **5.831 s later**, on the first start's commit and
file; **G-UNIT PASS at 1 restart, 11 of 11.**

```
[2026-10-28T12:56:53Z] record stop pid 3119051 at 2026-10-28T12:56:23Z
[2026-10-28T12:56:53Z] record start pid 3137952 at 2026-10-28T12:56:29Z
[2026-10-28T12:56:53Z] G-RESTART: the stop of 3119051, the start of 3137952 5.831 s later
[2026-10-28T12:56:53Z] G-UNIT active           True
[2026-10-28T12:56:53Z] G-UNIT enabled          True
[2026-10-28T12:56:53Z] G-UNIT fragment         True
[2026-10-28T12:56:53Z] G-UNIT control group    True
[2026-10-28T12:56:53Z] G-UNIT ceiling          True
[2026-10-28T12:56:53Z] G-UNIT nice             True
[2026-10-28T12:56:53Z] G-UNIT restarts         True
[2026-10-28T12:56:53Z] G-UNIT argv             True
[2026-10-28T12:56:53Z] G-UNIT cwd              True
[2026-10-28T12:56:53Z] G-UNIT cgroup           True
[2026-10-28T12:56:53Z] G-UNIT sole instance    True
[2026-10-28T12:56:53Z] btc-rewardbook.service MainPID 3137952, NRestarts 1, MemoryMax 201326592, MemoryCurrent 32690176, MemoryPeak 33869824
[2026-10-28T12:56:53Z] G-UNIT PASS at 1 restarts
[2026-10-28T12:56:53Z] G-RESTART PASS
[2026-10-28T12:56:53Z] peak memory of this run: 39190528 bytes
[2026-10-28T12:56:53Z] opens refused: 0; manifest opens 0; window opens 0; ledger opens 0; requests 0, stream sessions 0
exit=0
```

**`I resume A`** — `logs/93-resume-1.log`, `A` `1793192223`: NOT YET, exit `3`, G-RESUME's slot `1793192400`, 13:00:00
UTC, the first whose `S − 5` lies at least 60 s after the restarted process's start, closing at `1793193310`:

```
A=1793192223
[2026-10-28T12:57:03Z] MemAvailable 225431552 bytes, floor 135569408
[2026-10-28T12:57:03Z] NOT YET: slot 1793192400 (2026-10-28T13:00:00Z) closes at 1793193310; run again at or after it
[2026-10-28T12:57:03Z] peak memory of this run: 39186432 bytes
[2026-10-28T12:57:03Z] opens refused: 0; manifest opens 0; window opens 0; ledger opens 0; requests 0, stream sessions 0
exit=3
```

**`I resume A` again at the instant it named**, by the Executor's background wait — `logs/94-resume-2.log`, `A`
`1793193313`: **G-RESUME PASS** — slot `1793192400`, 13:00:00 UTC, complete: 97,727 frames, 11,723,039 stored bytes,
one `subscribe` at −4,848 ms, one `close`, the largest gap 1,080,041,238 ns, 0 bad lines, 300 initial tokens, 450 of
450 polls served. **The kill's slot**, `1793191500`, 12:45:00 UTC: index `0` `stopped`, 72,907 frames; index `1`
`joined_late`, 22,510 frames — each with its `slot.json` and one segment.

```
A=1793193313
[2026-10-28T13:15:13Z] MemAvailable 296611840 bytes, floor 135569408
[2026-10-28T13:15:16Z] the kill's slot 1793191500 2026-10-28T12:45:00Z: indices [{"error": null, "frames": 72907, "index": 0, "joined_late": false, "markets": 150, "segments": 1, "slot_json": true, "stopped": true, "stream_off": null, "stream_opened": true}, {"error": null, "frames": 22510, "index": 1, "joined_late": true, "markets": 150, "segments": 1, "slot_json": true, "stopped": false, "stream_off": null, "stream_opened": true}]
[2026-10-28T13:15:16Z] slot 1793192400 2026-10-28T13:00:00Z: complete; stream {"bad_lines": 0, "closes": 1, "foreign": 0, "frames": 97727, "initial_tokens": 300, "lag_ms": {"max": 835, "median": 15, "min": 12, "n": 97288, "p99": 137}, "last_close_offset_ms": 906031, "max_gap_ns": 1080041238, "nonconforming": 0, "pings": 90, "pongs": 90, "stored_bytes": 11723039, "subscribe_offset_ms": -4848, "subscribes": 1, "torn": 0, "types": [["book", 532], ["last_trade_price", 116], ["price_change", 97288]]}; polls {"lines": 450, "mismatched": 0, "rows": 450, "scheduled": 450, "served": 450, "statuses": {"200": 450}, "unreadable": 0}
[2026-10-28T13:15:16Z] wrote /root/tz33-work/resume/resume-1793193313.json sha256 70a3e33e2e684b0edc420f977be9129d8f1de973852745d0bbeb9c78bd52e683, 1752 bytes
[2026-10-28T13:15:16Z] READING G-RESUME: PASS
[2026-10-28T13:15:16Z] peak memory of this run: 49332224 bytes
[2026-10-28T13:15:16Z] opens refused: 0; manifest opens 0; window opens 0; ledger opens 0; requests 0, stream sessions 0
exit=0
```

| file | SHA-256 | bytes |
|---|---|---|
| `/root/tz33-work/resume/resume-1793193313.json` | `70a3e33e2e684b0edc420f977be9129d8f1de973852745d0bbeb9c78bd52e683` | 1,752 |

### 2.13 §3.10 — final: G-UNIT at one restart, and G-STILL (V8, V14)

`logs/95-final.log` — **FINAL PASS: G-UNIT PASS at 1 restart, 11 of 11; G-STILL PASS.** The recorder `2388318`,
`NRestarts` `0`, `active`, unchanged since `I still` at 06:14:23 UTC; the pair book `3121425`, `NRestarts` `11`, moved
from `3055430` and `9` **by the archive's own restarts alone**, a chain of two `restart` records in its ledger —
06:48:30 UTC, run `1793169873`, `3078426` after `3055430`, `NRestarts` `10`; and 11:48:48 UTC, run `1793187616`,
`3121425` after `3078426`, `NRestarts` `11` — the unit `active`. The ledger was opened once, by `final`.

```
[2026-10-28T13:15:27Z] G-UNIT active           True
[2026-10-28T13:15:27Z] G-UNIT enabled          True
[2026-10-28T13:15:27Z] G-UNIT fragment         True
[2026-10-28T13:15:27Z] G-UNIT control group    True
[2026-10-28T13:15:27Z] G-UNIT ceiling          True
[2026-10-28T13:15:27Z] G-UNIT nice             True
[2026-10-28T13:15:27Z] G-UNIT restarts         True
[2026-10-28T13:15:27Z] G-UNIT argv             True
[2026-10-28T13:15:27Z] G-UNIT cwd              True
[2026-10-28T13:15:27Z] G-UNIT cgroup           True
[2026-10-28T13:15:27Z] G-UNIT sole instance    True
[2026-10-28T13:15:27Z] btc-rewardbook.service MainPID 3137952, NRestarts 1, MemoryMax 201326592, MemoryCurrent 15650816, MemoryPeak 35823616
[2026-10-28T13:15:27Z] G-UNIT PASS at 1 restarts
[2026-10-28T13:15:27Z] btc-pairbook.service {'MainPID': '3121425', 'NRestarts': '11', 'ActiveState': 'active'}, MemoryCurrent 19230720, MemoryPeak 53665792
[2026-10-28T13:15:27Z] btc-recorder.service {'MainPID': '2388318', 'NRestarts': '0', 'ActiveState': 'active'}, MemoryCurrent 180559872, MemoryPeak 302309376
[2026-10-28T13:15:27Z] btc-pairbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-28T13:15:27Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-28T13:15:27Z] the archive's restart record 2026-10-28T06:48:30Z: run 1793169873, window 1793169900, pid 3078426 after 3055430, NRestarts 10
[2026-10-28T13:15:27Z] the archive's restart record 2026-10-28T11:48:48Z: run 1793187616, window 1793187900, pid 3121425 after 3078426, NRestarts 11
[2026-10-28T13:15:27Z] G-STILL PASS: changed by the archive's own restarts alone: 2 since 2026-10-28T06:14:23Z
[2026-10-28T13:15:27Z] memory.current 15646720
[2026-10-28T13:15:27Z] memory.peak 35823616
[2026-10-28T13:15:27Z] memory.swap.current 21889024
[2026-10-28T13:15:27Z] memory.swap.peak 21889024
[2026-10-28T13:15:27Z] stat.anon 14229504
[2026-10-28T13:15:27Z] stat.file 323584
[2026-10-28T13:15:27Z] stat.kernel 315392
[2026-10-28T13:15:27Z] stat.sock 0
[2026-10-28T13:15:27Z] stat.file_dirty 61440
[2026-10-28T13:15:27Z] stat.file_writeback 0
[2026-10-28T13:15:27Z] FINAL PASS: G-UNIT at one restart; G-STILL PASS
[2026-10-28T13:15:27Z] peak memory of this run: 39452672 bytes
[2026-10-28T13:15:27Z] opens refused: 0; manifest opens 0; window opens 0; ledger opens 1; requests 0, stream sessions 0
exit=0
```

**Both archive runs were off its calendar, and this TZ's own systemd steps set them off** — map §7 item 115's hypothesis,
observed here with its instants. B-INSTALL's `daemon-reload` ran at 06:34:32 UTC, and at 06:42:20 the timer's next
elapse read **06:44:32**, exactly 600 s later (`logs/62-archive-after-reload.log`), against its calendar's next of
03:00:20 the day after; it fired at 06:44:33, run `1793169873`. B-ENABLE's `systemctl enable --now`, which reloads
systemd's units too, ran at 11:30:15.68, and the archive's run `1793187616` began at **11:40:16**, 600 s after it. Each
restarted the pair book inside its own band — 06:48:00 to 06:48:06 and 11:48:18 to 11:48:24 UTC by the journal — and
each tagged a Release: `refs/tags/pairbook-streams-1793169873` and `pairbook-streams-1793187616`, which `logs/96-separation.log`'s
fetch brought. **None cost a window this TZ reads:** the second fell in window `1793187900`'s idle stretch, before its
stream opened at `T+595`, and G-NEIGHBORS counted that window complete. **G-STILL is PASS under §4.7's rule**, which
counts the archive's restarts as its own; its cause is named from both units' journal (§2.15).

```
2026-10-28T06:42:20.468689215Z
MainPID=0
NRestarts=0
Id=btc-pairbook-archive.service
ActiveState=inactive
SubState=dead
ActiveEnterTimestamp=
InactiveEnterTimestamp=Wed 2026-10-28 03:15:41 UTC

NextElapseUSecMonotonic=2month 3w 5d 2h 20min 404.339ms
LastTriggerUSec=Wed 2026-10-28 03:00:20 UTC
Id=btc-pairbook-archive.timer
ActiveState=active
SubState=waiting
ActiveEnterTimestamp=Sun 2026-10-11 15:08:11 UTC
InactiveEnterTimestamp=

MainPID=3055430
NRestarts=9
Id=btc-pairbook.service
ActiveState=active
SubState=running
ActiveEnterTimestamp=Wed 2026-10-28 03:06:34 UTC
InactiveEnterTimestamp=Wed 2026-10-28 03:06:29 UTC
NEXT                            LEFT LAST                              PASSED UNIT                       ACTIVATES
Wed 2026-10-28 06:44:32 UTC 2min 12s Wed 2026-10-28 03:00:20 UTC 3h 42min ago btc-pairbook-archive.timer btc-pairbook-archive.service

1 timers listed.
```

### 2.14 Memory and free space — every read, its instant and its bound

| instant (UTC) | read by | `MemAvailable` | free on `/dev/vda2` | bound |
|---|---|---|---|---|
| 06:11:51 | §0.3, host gate | 290,100 kB | 11,560,394,752 | memory `135,569,408`; disk `8,200,000,000` |
| 06:33:45 | `prestart` | 288,186,368 | 11,519,152,128 | memory `135,569,408` |
| 11:01:25 | `prestart` into `prestart-2` | 336,314,368 | 11,503,321,088 | memory `135,569,408` |
| 11:30:16 | the service's `start` record (`service.log`) | — | 11,463,892,992 | `RESOURCE_FLOOR` `2,200,000,000`; `STREAM_FLOOR` `7,300,000,000` |
| 12:55:10 | `prove`, first | 276,922,368 | — | memory `135,569,408` |
| 12:55:57 | `prove`, second | 274,137,088 | — | memory `135,569,408` |
| 12:56:29 | the restarted service's `start` record | — | 11,660,480,512 | `RESOURCE_FLOOR` |
| 12:57:03 | `resume`, NOT YET | 225,431,552 | — | memory `135,569,408` |
| 13:15:13 | `resume`, deciding | 296,611,840 | — | memory `135,569,408` |
| 13:15:44 | §3.11, §0.3's block again | 297,520 kB | 11,606,761,472 | none at close |
| after §3.11 | B-RECLAIM-OWN's `df` | — | §2.17 | none |

**The units' memory at every read, in bytes** — `MemoryCurrent` / `MemoryPeak`, page cache included:

| instant (UTC) | read by | recorder | pair book | reward book |
|---|---|---|---|---|
| 06:14:23 | `still` | 246,321,152 / 302,309,376 | 13,021,184 / 132,734,976 | — |
| 11:31:17 | `unit 0` | — | — | 48,291,840 / 50,339,840 |
| 11:32:11 | `logs/76-health-1.log` | 108,384,256 / 302,309,376 | 21,716,992 / 83,824,640 | 48,881,664 / 50,339,840 |
| 12:56:09 | `load`, the control group's own files | — | — | 21,725,184 / 50,339,840; swap 31,629,312; `anon` 15,724,544 |
| 12:56:53 | `restart` | — | — | 32,690,176 / 33,869,824 |
| 13:15:27 | `final` | 180,559,872 / 302,309,376 | 19,230,720 / 53,665,792 | 15,650,816 / 35,823,616; swap 21,889,024; `anon` 14,229,504 |
| 13:15:44 | §3.11's `systemctl show` | 45,154,304 / 302,309,376 | 18,898,944 / 53,665,792 | 15,560,704 / 35,823,616 |

systemd's own account at the kill, from the journal: the first process "Consumed 2min 15.712s CPU time, 48.0M memory
peak, 30.1M memory swap peak". The service runs under `MemoryMax=201326592`.

**Every mode's peak, and its opens under the capture roots (V15)** — from each log's last two lines:

| log | mode | peak bytes | refused | manifest | window | ledger | requests | sessions |
|---|---|---|---|---|---|---|---|---|
| `02` | `fingerprint`, the staged copy | 40,890,368 | 0 | 0 | 0 | 0 | 0 | 0 |
| `20` | `selftest` | 64,638,976 | 0 | 0 | 0 | 0 | 25, loopback | 3, loopback |
| `30` | `still` | 39,170,048 | 0 | 0 | 0 | 0 | 0 | 0 |
| `31` | `scratch` | 39,186,432 | 0 | 0 | 0 | 0 | 0 | 0 |
| `50` | `prestart` | 45,084,672 | 0 | 2016 | 672 | 0 | 6 | 1 |
| `51` | `prestart`, into `prestart-2` | 44,539,904 | 0 | 2016 | 672 | 0 | 6 | 1 |
| `70` | `mark start-svc` | 39,317,504 | 0 | 0 | 0 | 0 | 0 | 0 |
| `75` | `unit 0` | 39,448,576 | 0 | 0 | 0 | 0 | 0 | 0 |
| `80` | `prove`, deciding | 55,386,112 | 0 | 14 | 5 | 0 | 0 | 0 |
| `81` | `prove`, same `A` | 55,783,424 | 0 | 14 | 5 | 0 | 0 | 0 |
| `82` | `load` | 39,186,432 | 0 | 0 | 0 | 0 | 0 | 0 |
| `90` | `mark kill-svc` | 39,186,432 | 0 | 0 | 0 | 0 | 0 | 0 |
| `92` | `restart` | 39,190,528 | 0 | 0 | 0 | 0 | 0 | 0 |
| `93` | `resume`, NOT YET | 39,186,432 | 0 | 0 | 0 | 0 | 0 | 0 |
| `94` | `resume`, deciding | 49,332,224 | 0 | 0 | 0 | 0 | 0 | 0 |
| `95` | `final` | 39,452,672 | 0 | 0 | 0 | 1 | 0 | 0 |

Every peak is below the Architect's largest, `selftest`'s `67,784,704`, and every `MemAvailable` read above the floor.
Two `reclaim` runs printed no summary: the classifier refused the first before it started, and the Boss's of 06:30 stopped
at its first assert (§2.4); B-RECLAIM-OWN's prints its own (§2.17).

### 2.15 §3.11 — the closing reads (V17), and contract §4.2's self-check (V16)

`logs/97-closing.log` — §0.3's block again, then §3.11's. H4 and H5 now read the reward book's start: `rewardbook unit
exit=0`, `/root/btc-rewardbook-svc exit=0`, `/var/lib/btc-rewardbook exit=0`; `btc-rewardbook.service` `active`,
`running`, `enabled`, `MainPID=3137952`, `NRestarts=1`, `Nice=10`; the recorder and the pair book `Nice=0`. The journal
holds systemd's own lines for the three units from 5 s before the `start-svc` mark: the pair book's two stops and
starts by the archive (§2.13), the reward book's start at 11:30:16, the `SIGTERM` "on client request" at 12:56:22 and
the restart at 12:56:29, `restart counter is at 1`. **No line names the package manager**: neither capture unit was
stopped by it in the span. `service.log`'s tail: the two `start` records, the day's selection — attempt 0 ok, 150
members, 218 requests, 48.1 s — one line a slot, the `stop` record, and the restarted process's load of the day's
selection. `du`: the reward book's store `78628152` bytes, the pair book's `169154382`.

```
Wed Oct 28 01:15:44 PM UTC 2026
1793193344
1
MemTotal:         978640 kB
MemAvailable:     297520 kB
SwapTotal:       3174396 kB
SwapFree:        2782676 kB
2026-08-02 07:24:32
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
 -5 23a31fad2f064f04b9e138eac29658f3 Sun 2026-06-21 21:37:37 UTC Fri 2026-06-26 14:13:44 UTC
 -4 a38e17445ce341bc8b877be9d3d4f648 Fri 2026-06-26 14:13:52 UTC Tue 2026-07-14 16:15:10 UTC
 -3 5f4d18a6ba8041bd80e7d1e192c5ee28 Tue 2026-07-14 16:15:20 UTC Fri 2026-07-17 01:01:21 UTC
 -2 b1b399c70c6e4dcc934755f70a2ca231 Fri 2026-07-17 01:01:43 UTC Fri 2026-07-24 14:55:46 UTC
 -1 285d6962c92c407d837d1ce329b93aa4 Fri 2026-07-24 14:55:54 UTC Sun 2026-08-02 07:23:49 UTC
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-02 07:24:34 UTC Wed 2026-10-28 13:15:38 UTC
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11606761472
/var/lib/btc-recorder/btc-updown-5m/1792953900/manifest.json
3
3.12.3 17.1
MainPID=2388318
Result=success
NRestarts=0
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC

MainPID=3121425
Result=success
NRestarts=11
Id=btc-pairbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Wed 2026-10-28 11:48:24 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-pairbook-archive.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=

Result=success
Id=btc-pairbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-11 15:08:11 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-chainbook.service
ActiveState=inactive
SubState=dead
UnitFileState=disabled
ActiveEnterTimestamp=

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
NEXT                        LEFT LAST                              PASSED UNIT                       ACTIVATES
Wed 2026-10-28 23:40:42 UTC  10h Wed 2026-10-28 06:41:48 UTC       6h ago apt-daily.timer            apt-daily.service
Thu 2026-10-29 03:00:20 UTC  13h Wed 2026-10-28 11:40:16 UTC 1h 35min ago btc-pairbook-archive.timer btc-pairbook-archive.service
Thu 2026-10-29 06:19:38 UTC  17h Wed 2026-10-28 06:03:25 UTC       7h ago apt-daily-upgrade.timer    apt-daily-upgrade.service

3 timers listed.
rewardbook unit exit=0
btc-recorder.service cmp exit=0
btc-pairbook.service cmp exit=0
btc-pairbook-archive.service cmp exit=0
btc-pairbook-archive.timer cmp exit=0
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
e8b46a85d61e1a17841962846f6d3012046c2d70
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
/root/tz32-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
/root/btc-pairbook-archive-svc exit=0
/var/lib/btc-pairbook-archive exit=0
/root/btc-rewardbook-svc exit=0
/var/lib/btc-rewardbook exit=0
71381 /var/lib/btc-pairbook-archive/ledger.jsonl
2044
/root/btc-5m-twap       adba104 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/root/tz33-work/wt      2dcd70e [tz-33-reward-book-capture]
169154382	/var/lib/btc-pairbook
10542879	/var/lib/btc-pairbook-archive
115642308	/root/.claude
654321537	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/0358b0b2-9811-5291-867b-b185a7307938/scratchpad
total 20
drwx------  5 root root 4096 Oct 28 10:56 .
drwx------ 32 root root 4096 Oct 28 10:56 ..
drwx------  4 root root 4096 Oct 28 06:09 0358b0b2-9811-5291-867b-b185a7307938
drwx------  3 root root 4096 Oct 28 06:09 621e47cc-760f-4cb1-8481-c2a8f6828d9d
drwx------  3 root root 4096 Oct 28 10:56 b82e3547-dd0e-46f7-abe9-4ad9e7903328
---- section 3.11 ----
MainPID=2388318
NRestarts=0
MemoryCurrent=45154304
MemoryPeak=302309376
Nice=0
ActiveState=active

MainPID=3121425
NRestarts=11
MemoryCurrent=18898944
MemoryPeak=53665792
Nice=0
ActiveState=active

MainPID=3137952
NRestarts=1
MemoryCurrent=15560704
MemoryPeak=35823616
Nice=10
ActiveState=active
enabled
exit=0
2026-10-28T06:48:00+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 3055430 (python) on client request.
2026-10-28T06:48:01+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-28T06:48:01+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 5min 52.477s CPU time, 126.5M memory peak, 37.0M memory swap peak.
2026-10-28T06:48:06+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 10.
2026-10-28T06:48:06+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-28T11:30:16+00:00 vultr systemd[1]: Started btc-rewardbook.service - btc-5m-twap reward book, the books and trades of the day's reward markets streamed.
2026-10-28T11:48:18+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 3078426 (python) on client request.
2026-10-28T11:48:19+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-28T11:48:19+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 7min 33.235s CPU time, 79.9M memory peak, 36.3M memory swap peak.
2026-10-28T11:48:24+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 11.
2026-10-28T11:48:24+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-28T12:56:22+00:00 vultr systemd[1]: btc-rewardbook.service: Sent signal SIGTERM to main process 3119051 (python) on client request.
2026-10-28T12:56:24+00:00 vultr systemd[1]: btc-rewardbook.service: Deactivated successfully.
2026-10-28T12:56:24+00:00 vultr systemd[1]: btc-rewardbook.service: Consumed 2min 15.712s CPU time, 48.0M memory peak, 30.1M memory swap peak.
2026-10-28T12:56:29+00:00 vultr systemd[1]: btc-rewardbook.service: Scheduled restart job, restart counter is at 1.
2026-10-28T12:56:29+00:00 vultr systemd[1]: Started btc-rewardbook.service - btc-5m-twap reward book, the books and trades of the day's reward markets streamed.
[2026-10-28T11:30:16Z] start record: pid 3119051 commit 2dcd70e08b18b93c64bb67d9849ac1216ce40e41 file_sha256 a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670; free 11463892992 bytes, streams 0 bytes
[2026-10-28T11:31:04Z] day 1793145600 (2026-10-28T00:00:00Z): selection attempt 0 ok, 150 members, 218 requests, 48.1 s
[2026-10-28T11:45:10Z] slot 1793187000 (2026-10-28T11:30:00Z) index 0: 150 markets; stream opened, 77804 frames, 1 segments, 9629579 bytes; polls 430 served of 450, 430 with a row, 20 missed
[2026-10-28T12:00:10Z] slot 1793187900 (2026-10-28T11:45:00Z) index 0: 150 markets; stream opened, 78151 frames, 1 segments, 9639138 bytes; polls 450 served of 450, 450 with a row, 0 missed
[2026-10-28T12:15:09Z] slot 1793188800 (2026-10-28T12:00:00Z) index 0: 150 markets; stream opened, 85321 frames, 1 segments, 10430786 bytes; polls 450 served of 450, 450 with a row, 0 missed
[2026-10-28T12:30:09Z] slot 1793189700 (2026-10-28T12:15:00Z) index 0: 150 markets; stream opened, 88928 frames, 1 segments, 10844068 bytes; polls 450 served of 450, 450 with a row, 0 missed
[2026-10-28T12:45:10Z] slot 1793190600 (2026-10-28T12:30:00Z) index 0: 150 markets; stream opened, 96873 frames, 1 segments, 11422263 bytes; polls 450 served of 450, 450 with a row, 0 missed
[2026-10-28T12:56:23Z] slot 1793191500 (2026-10-28T12:45:00Z) index 0: 150 markets; stream opened, 72907 frames, 1 segments, 8669289 bytes; polls 330 served of 450, 330 with a row, 0 missed, stopped
[2026-10-28T12:56:23Z] stop record written; requests 2778, sessions 6, frames 499984, stream bytes 60635123, other bytes 2513116
[2026-10-28T12:56:29Z] stale pid file (pid 3119051) replaced
[2026-10-28T12:56:29Z] start record: pid 3137952 commit 2dcd70e08b18b93c64bb67d9849ac1216ce40e41 file_sha256 a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670; free 11660480512 bytes, streams 60635123 bytes
[2026-10-28T12:56:29Z] day 1793145600 (2026-10-28T00:00:00Z): selection attempt 0 loaded, 150 members
[2026-10-28T13:00:10Z] slot 1793191500 (2026-10-28T12:45:00Z) index 1: 150 markets; stream opened, 22510 frames, 1 segments, 2824343 bytes; polls 116 served of 450, 116 with a row, 334 missed
[2026-10-28T13:15:10Z] slot 1793192400 (2026-10-28T13:00:00Z) index 0: 150 markets; stream opened, 97727 frames, 1 segments, 11723039 bytes; polls 450 served of 450, 450 with a row, 0 missed
               total        used        free      shared  buff/cache   available
Mem:      1002127360   606695424    75100160       40960   472543232   395431936
Swap:     3250581504   428929024  2821652480
9614757	/root/tz33-work
175201	/root/btc-rewardbook-svc
78628152	/var/lib/btc-rewardbook
169154382	/var/lib/btc-pairbook
115642308	/root/.claude
{
 "marks": {
  "kill-svc": {
   "ActiveState": "active",
   "MainPID": "3119051",
   "NRestarts": "0",
   "ns": 1793192177982816393,
   "unit": "btc-rewardbook.service"
  },
  "start-svc": {
   "ActiveState": "inactive",
   "MainPID": "0",
   "NRestarts": "0",
   "ns": 1793169294271237150,
   "unit": "btc-rewardbook.service"
  }
 },
 "still": {
  "at": "2026-10-28T06:14:23Z",
  "at_ns": 1793168063701434367,
  "units": {
   "pairbook": {
    "ActiveState": "active",
    "MainPID": "3055430",
    "NRestarts": "9"
   },
   "recorder": {
    "ActiveState": "active",
    "MainPID": "2388318",
    "NRestarts": "0"
   }
  }
 }
}
```

**Contract §4.2's separation self-check, verbatim** (`logs/96-separation.log`), run after the push and the pull request
and before the report's commit: the implementation commit on `origin/main` `0` times; the branch's diff the two
implementation files alone; no `.parquet` or `.zip` on `main`; `origin` carrying `main` at `adba104` and the branch at
`2dcd70e`; PR #32 `OPEN`, not merged.

```
$ git fetch origin
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new tag]         pairbook-streams-1793169873 -> pairbook-streams-1793169873
 * [new tag]         pairbook-streams-1793187616 -> pairbook-streams-1793187616
exit=0
$ git rev-list origin/main | grep -c 2dcd70e08b18b93c64bb67d9849ac1216ce40e41
0
$ git diff --name-only origin/main origin/tz-33-reward-book-capture
deploy/systemd/btc-rewardbook.service
research/tz33-reward-book-capture.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
grep exit=1
$ git ls-remote origin refs/heads/main refs/heads/tz-33-reward-book-capture
adba1043e4d32011053dd6d1f1d926359af32dc4	refs/heads/main
2dcd70e08b18b93c64bb67d9849ac1216ce40e41	refs/heads/tz-33-reward-book-capture
$ gh pr view 32 --repo seahomebatumi-ai/btc-5m-twap --json number,state,headRefOid,baseRefName,mergedAt
{"baseRefName":"main","headRefOid":"2dcd70e08b18b93c64bb67d9849ac1216ce40e41","mergedAt":null,"number":32,"state":"OPEN"}
```

`logs/98-sessions-at-close.log` — the `claude` processes at the close and the directory beside this session's own:
the session's process is now `3115475`, started at 10:56:31 UTC when the session's container was restarted, and
`b82e3547-dd0e-46f7-abe9-4ad9e7903328` was born with it; `621e47cc…` was born with `3071142`, which no longer runs. **This
session's three directories — `0358b0b2-9811-5291-867b-b185a7307938`, `621e47cc-760f-4cb1-8481-c2a8f6828d9d` and
`b82e3547-dd0e-46f7-abe9-4ad9e7903328` — are the next TZ's to reclaim**, unless a reboot of the host empties `/tmp`.

```
2026-10-28T13:16:58.743268143Z
$ ps -eo pid,lstart,args | grep -E "(^| )(claude|[^ ]*/claude\.exe)( |$)" | grep -v grep
3114896 Wed Oct 28 10:52:23 2026 tmux new-session -d -s crypto-rc -c /root/crypto-auto claude remote-control --name "Crypto Auto VPS"
3114897 Wed Oct 28 10:52:23 2026 claude remote-control --name Crypto Auto VPS
3114907 Wed Oct 28 10:52:25 2026 claude remote-control --name BTC-5M-TWAP-VPS --spawn=same-dir
3115475 Wed Oct 28 10:56:31 2026 /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe --print --sdk-url https://api.anthropic.com/v1/code/sessions/cse
$ ls -la --time-style=full-iso /tmp/claude-0/-root-btc-5m-twap
total 20
drwx------  5 root root 4096 2026-10-28 10:56:32.423570871 +0000 .
drwx------ 32 root root 4096 2026-10-28 10:56:33.854584306 +0000 ..
drwx------  4 root root 4096 2026-10-28 06:09:29.941244665 +0000 0358b0b2-9811-5291-867b-b185a7307938
drwx------  3 root root 4096 2026-10-28 06:09:21.975175825 +0000 621e47cc-760f-4cb1-8481-c2a8f6828d9d
drwx------  3 root root 4096 2026-10-28 10:56:32.423570871 +0000 b82e3547-dd0e-46f7-abe9-4ad9e7903328
```

### 2.16 Every file the run wrote, by SHA-256, but the capture's own

`logs/99-files-written.log` — `sha256sum` and `wc -c` of every file under `/root/tz33-work` but the worktree's checkout
of `main` and that log itself, of the two files the branch adds in the worktree, of `/root/btc-rewardbook-svc/`, and of
the installed unit with its enable link. The worktree's other files are `main`'s at `adba104`, written by `git worktree
add`. The report builder — `report/build.py`, `report/template.md` and `report/closing.sh` — is listed with them; its
template is final before the list is taken, and the report it builds is `CryptoReports/TZ-33-reward-book-capture-report.md`
itself, completed after B-RECLAIM-OWN by quoting that block's output in §2.17.

```
2026-10-28T13:20:45.425873635Z
$ sha256sum and wc -c of every file under /root/tz33-work but wt/ and this log; wt/'s two branch files; /root/btc-rewardbook-svc/*; the installed unit and its enable link
4eb290df4a1eb20316b25645468c8ccf81490b8404c98050c54401d4c6f8c3a7        242 /root/tz33-work/logs/00-work-tree.log
8eaef70a18e3662793a8148c862a56b4ae73a77a15b7c2bfa8bd3e50399f22cd        275 /root/tz33-work/logs/01-stage.log
53273a907c11aaa25fb07d4fa4e1787fcd2d5e3be37ae709d5e5ff35c3aa9fce       8579 /root/tz33-work/logs/02-fingerprint.log
3ef40740328f1c6d77e270bfa83ff7fa02a5bcd082b88b814e8cc0d98846d734       4203 /root/tz33-work/logs/03-host-gate.log
efc0b6d9d43c5765af32385a21ed417525a91f08fb9fbc8444b81ddb268a116e       5624 /root/tz33-work/logs/05-refs.log
baad702ac39c0207ef35043a9d149a484a4b623359ded7e02fe5f30061f14e93        229 /root/tz33-work/logs/06-model.log
afc2b303ea43eb23c6d1d0bd7bdeb3f7dd22c3c02529506ec79282243f88aa89        338 /root/tz33-work/logs/07-tz-file.log
089b98ff2f1c6acc14438efdbdbc9318ed8ae02bdfe3fefacd734fe2e0ba991e        457 /root/tz33-work/logs/10-branch.log
f1206dc5b7f6aa6561ef3640e1c657e58557636f0fdcf19f7a9d734b17f80d16        269 /root/tz33-work/logs/11-extract-wt.log
5f68c8327b5a021b9903fdce60fb207a196614ce18bcfbb0dfb9a0eb66990ab3        912 /root/tz33-work/logs/12-push.log
634143fccabd9d49a088829a78e7da3935324aac36d618606f5bf45cae6654f5        123 /root/tz33-work/logs/13-pr.log
1261e8d34124b0ec9621d5bd52f6ba05f2e3208b69ed9435bb968d11d1908458      10499 /root/tz33-work/logs/20-selftest.log
6b154347b62b31383667eb9a3e6e03c30eeaead7b1652620282f8387edcfdd99        839 /root/tz33-work/logs/30-still.log
fc50f8ca0253dd4357b8c2c286d015967642299d866a9a8f351bbeb8e067b1e9        963 /root/tz33-work/logs/31-scratch.log
f82c76281859e40d0a5fe66a75092965cc568ca70ff6327c81f316a2b7bddfd2        849 /root/tz33-work/logs/32-reclaim-scratch.log
27c8005ab085f5b30be5d829a22b87cbb959ffc370a96a6ab72c6df20acef0c1        264 /root/tz33-work/logs/32-reclaim-scratch-refused.log
21f9788ce6c240936479a56ddf57eb2864c974e4445b153dfa41d6c986997828         56 /root/tz33-work/logs/33-rm-scratch.log
e1269c4db87e16ed1bc1a3130463cd4d4fcff4deacdb34d7aa7c288df768f196       1558 /root/tz33-work/logs/34-reclaim-scratch-verify.log
7e25a1f58b2a8c37a160777e30d328dafbe9cdc01ce0abf0a827a90dd3030835       7367 /root/tz33-work/logs/35-reclaim-scratch-boss-statement.log
655b9588afc42e32b894939af5a9f85f8028465c393cd4a3f70c355e24d69e73        431 /root/tz33-work/logs/40-copy.log
0ec4cbd3b5c6f0f2eabe502d740949b9962e5421e05358fec982a2e0f37b3078       3772 /root/tz33-work/logs/50-prestart.log
01cb3b301e2a5d22d6a8ab3ff7663a24a7b822c4aadbc28b490db4716da4514e       3775 /root/tz33-work/logs/51-prestart-2.log
813a9a93a91b315d41746d711cc1ae9db80e1533c2fbcb440a14da300c03148f         97 /root/tz33-work/logs/60-install.log
3166c4de966014c3d1a4519ad3c864298f411f4eaab86c605e9b352b1a1c6104        889 /root/tz33-work/logs/62-archive-after-reload.log
3ef67404f54b5d2688c4802b50951e28ea2318faba13023db39bbca6bbb44d1f        400 /root/tz33-work/logs/70-mark-start-svc.log
86a0838ba884daf1259ae8bba5216edb1f506b671426e74f81181bf07b696162         31 /root/tz33-work/logs/71-enable.log
f109ade972fafd1fdad12bde324f21470d0a314e2e3f17899228e2825b7e3241        381 /root/tz33-work/logs/71-enable-refused.log
3c5a885f2544efbd79823dc16627e1a7a9c256278ecf4bee140e927789d6d57a       1815 /root/tz33-work/logs/72-after-container-restart.log
2497c4ae5dffa265398706cd8cdcbcb5d028a17a05a995414d2af9a272745ab5       1034 /root/tz33-work/logs/73-enable-first-handover-lapsed.log
48cdc1f0c09fda1d60f49bba16fe80df49398b70b92107c9fc19b72f3cffdc02        200 /root/tz33-work/logs/74-enable.log
d504ad48f6477f28eb6fbb031e4f8c59790500888143424efcd5abf41ebdbe4a       1591 /root/tz33-work/logs/75-unit-0.log
372108cd989d2fdc9de541ff4f8611a408e417100292df020f13f5fe75cbb769        431 /root/tz33-work/logs/76-health-1.log
d4990084c1cb03b394df5aba995305bec99f613ed481e29fa45ace2337fd3338       7805 /root/tz33-work/logs/80-prove-first.log
2d7c69de1e49fc2d265f3faffd5afceda6d89cce6543f3d6df58e4f1e147b674       7797 /root/tz33-work/logs/81-prove-second.log
ecb1e9434ecf81f5e4952f50075c9ee849b102b994effd79267a8fdeb611c2f1       1033 /root/tz33-work/logs/82-load.log
ff80aab221452857c3ea3779f97c10f76763957b7e1c5ec1b6b94b0608d60597        403 /root/tz33-work/logs/90-mark-kill-svc.log
b7adeae7b09011ad438ea3f5b10b93a2c9f1f96508f3e83c7d4d3a16f5c5c1c5         38 /root/tz33-work/logs/91-kill-svc.log
2371872689c321a32aead567dbebc36661e43f71c5450beaff70726f53c17a4d       1224 /root/tz33-work/logs/92-restart.log
d44a4a5d2e55d764d911fca28264ea800b93f9d1f94eca0dd38ad7eed10c32d3        391 /root/tz33-work/logs/93-resume-1.log
8fd684758a22df9f58ed17f93c9d0f4366a476780098d60e85b94410df6c2cc2       1544 /root/tz33-work/logs/94-resume-2.log
206e35ba3d435c30fc4fea8a7c437fc3d2180777785d4a11be903382408106d0       2483 /root/tz33-work/logs/95-final.log
8af57d45c919b61ef7af74f29306711693e280b4e44b83de4e2189f9cff6d4f2        980 /root/tz33-work/logs/96-separation.log
9196e3c76283a2d687b7db77f4f8c5a46384d4d7697ab248e64fb8ba04d46934       9833 /root/tz33-work/logs/97-closing.log
f535ad3ff92b9fae81567b23913282f4ea419dd4a6f66753b6a035abecb3708d       1101 /root/tz33-work/logs/98-sessions-at-close.log
e61f0a283f692ae42407097a4465e9049e5055591e3149a8017c45fc419642db       3795 /root/tz33-work/prestart-2/prestart.json
e92d0c0ce2d77e6285b2ad65a88e77aebb5b1dd2bd2029662c1a7c1cb446e0f4      10378 /root/tz33-work/prestart-2/stream.jsonl.gz
86f5f2853cafc9919b5a6a71a30d407972a6451e78802e5f2a5927960a8b1892       3796 /root/tz33-work/prestart/prestart.json
609c81fe54d984033b7dc3ed965c31c64bff0a24d870f190c4a255e84f607f6e      43276 /root/tz33-work/prestart/stream.jsonl.gz
70ba7291b122421743c0287dd623fc268cb6be3dc0f5282879effe4b1fa73abf       5799 /root/tz33-work/proof/proof-1793192110.json
bbe12deec060ee9e71dbe1d7bc78e0fa15bf8648840442711c87ce5ed3b1218b       2056 /root/tz33-work/report/build.py
189f28b5eb846eab03cd230d13b1516853f6e1a979769fac197398fbef449482       3000 /root/tz33-work/report/closing.sh
3e2309223343729a7ede1963b4e1f95878355e70f4f4c8ebbb6e28ebba65fba1      47028 /root/tz33-work/report/template.md
70a3e33e2e684b0edc420f977be9129d8f1de973852745d0bbeb9c78bd52e683       1752 /root/tz33-work/resume/resume-1793193313.json
7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec        817 /root/tz33-work/stage/deploy/systemd/btc-rewardbook.service
a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670     175160 /root/tz33-work/stage/research/tz33-reward-book-capture.py
be133c668b04c823abb44e8f2a33c29717cf7f1a41ee36ba4e3bbd89850ec698        631 /root/tz33-work/state.json
a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670     175160 /root/tz33-work/wt/research/tz33-reward-book-capture.py
7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec        817 /root/tz33-work/wt/deploy/systemd/btc-rewardbook.service
a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670     175160 /root/btc-rewardbook-svc/tz33-reward-book-capture.py
2922592480b3dc9675f0355bbaae33eb4623952d41dcc68a5a40f66721fca080         41 /root/btc-rewardbook-svc/commit.txt
7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec        817 /etc/systemd/system/btc-rewardbook.service
$ readlink /etc/systemd/system/multi-user.target.wants/btc-rewardbook.service
/etc/systemd/system/btc-rewardbook.service
```

### 2.17 §9 B-RECLAIM-OWN — last, after §3.11, with this report drafted

B-RECLAIM-OWN, run by the Executor after §3.11 with this report drafted in the primary checkout, in four calls — the
`reclaim` alone, then `git worktree remove`, then `rm -rf`, then the last four lines in one call — **none refused by the
session's classifier**. Its output was written to no file; it is quoted here whole, from the session, each call's
commands on `$` lines before their output:

```
$ cd /root/tz33-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz33-work/wt/research/tz33-reward-book-capture.py reclaim /root/tz33-work 2>&1; echo "exit=$?"
[2026-10-28T13:21:00Z] reclaim: 3160 report tokens; forensic store holds 2044 files
[2026-10-28T13:21:00Z] reclaim: /root/tz33-work/wt skipped: no file but its HEAD's, and HEAD 2dcd70e08b18b93c64bb67d9849ac1216ce40e41 is its upstream's
[2026-10-28T13:21:00Z] R copied be133c668b04c823abb44e8f2a33c29717cf7f1a41ee36ba4e3bbd89850ec698 /root/btc-forensics/tz33-work--state.json
[2026-10-28T13:21:00Z] R copied 4eb290df4a1eb20316b25645468c8ccf81490b8404c98050c54401d4c6f8c3a7 /root/btc-forensics/tz33-work--logs--00-work-tree.log
[2026-10-28T13:21:00Z] R copied 8eaef70a18e3662793a8148c862a56b4ae73a77a15b7c2bfa8bd3e50399f22cd /root/btc-forensics/tz33-work--logs--01-stage.log
[2026-10-28T13:21:00Z] R copied 53273a907c11aaa25fb07d4fa4e1787fcd2d5e3be37ae709d5e5ff35c3aa9fce /root/btc-forensics/tz33-work--logs--02-fingerprint.log
[2026-10-28T13:21:00Z] R copied 3ef40740328f1c6d77e270bfa83ff7fa02a5bcd082b88b814e8cc0d98846d734 /root/btc-forensics/tz33-work--logs--03-host-gate.log
[2026-10-28T13:21:00Z] R copied efc0b6d9d43c5765af32385a21ed417525a91f08fb9fbc8444b81ddb268a116e /root/btc-forensics/tz33-work--logs--05-refs.log
[2026-10-28T13:21:00Z] R copied baad702ac39c0207ef35043a9d149a484a4b623359ded7e02fe5f30061f14e93 /root/btc-forensics/tz33-work--logs--06-model.log
[2026-10-28T13:21:00Z] R copied afc2b303ea43eb23c6d1d0bd7bdeb3f7dd22c3c02529506ec79282243f88aa89 /root/btc-forensics/tz33-work--logs--07-tz-file.log
[2026-10-28T13:21:00Z] R copied 089b98ff2f1c6acc14438efdbdbc9318ed8ae02bdfe3fefacd734fe2e0ba991e /root/btc-forensics/tz33-work--logs--10-branch.log
[2026-10-28T13:21:00Z] R copied f1206dc5b7f6aa6561ef3640e1c657e58557636f0fdcf19f7a9d734b17f80d16 /root/btc-forensics/tz33-work--logs--11-extract-wt.log
[2026-10-28T13:21:00Z] R copied 5f68c8327b5a021b9903fdce60fb207a196614ce18bcfbb0dfb9a0eb66990ab3 /root/btc-forensics/tz33-work--logs--12-push.log
[2026-10-28T13:21:00Z] R copied 634143fccabd9d49a088829a78e7da3935324aac36d618606f5bf45cae6654f5 /root/btc-forensics/tz33-work--logs--13-pr.log
[2026-10-28T13:21:00Z] R copied 1261e8d34124b0ec9621d5bd52f6ba05f2e3208b69ed9435bb968d11d1908458 /root/btc-forensics/tz33-work--logs--20-selftest.log
[2026-10-28T13:21:00Z] R copied 6b154347b62b31383667eb9a3e6e03c30eeaead7b1652620282f8387edcfdd99 /root/btc-forensics/tz33-work--logs--30-still.log
[2026-10-28T13:21:00Z] R copied fc50f8ca0253dd4357b8c2c286d015967642299d866a9a8f351bbeb8e067b1e9 /root/btc-forensics/tz33-work--logs--31-scratch.log
[2026-10-28T13:21:00Z] R copied 27c8005ab085f5b30be5d829a22b87cbb959ffc370a96a6ab72c6df20acef0c1 /root/btc-forensics/tz33-work--logs--32-reclaim-scratch-refused.log
[2026-10-28T13:21:00Z] R copied f82c76281859e40d0a5fe66a75092965cc568ca70ff6327c81f316a2b7bddfd2 /root/btc-forensics/tz33-work--logs--32-reclaim-scratch.log
[2026-10-28T13:21:00Z] R copied 21f9788ce6c240936479a56ddf57eb2864c974e4445b153dfa41d6c986997828 /root/btc-forensics/tz33-work--logs--33-rm-scratch.log
[2026-10-28T13:21:00Z] R copied e1269c4db87e16ed1bc1a3130463cd4d4fcff4deacdb34d7aa7c288df768f196 /root/btc-forensics/tz33-work--logs--34-reclaim-scratch-verify.log
[2026-10-28T13:21:00Z] R copied 7e25a1f58b2a8c37a160777e30d328dafbe9cdc01ce0abf0a827a90dd3030835 /root/btc-forensics/tz33-work--logs--35-reclaim-scratch-boss-statement.log
[2026-10-28T13:21:00Z] R copied 655b9588afc42e32b894939af5a9f85f8028465c393cd4a3f70c355e24d69e73 /root/btc-forensics/tz33-work--logs--40-copy.log
[2026-10-28T13:21:00Z] R copied 0ec4cbd3b5c6f0f2eabe502d740949b9962e5421e05358fec982a2e0f37b3078 /root/btc-forensics/tz33-work--logs--50-prestart.log
[2026-10-28T13:21:00Z] R copied 01cb3b301e2a5d22d6a8ab3ff7663a24a7b822c4aadbc28b490db4716da4514e /root/btc-forensics/tz33-work--logs--51-prestart-2.log
[2026-10-28T13:21:00Z] R copied 813a9a93a91b315d41746d711cc1ae9db80e1533c2fbcb440a14da300c03148f /root/btc-forensics/tz33-work--logs--60-install.log
[2026-10-28T13:21:00Z] R copied 3166c4de966014c3d1a4519ad3c864298f411f4eaab86c605e9b352b1a1c6104 /root/btc-forensics/tz33-work--logs--62-archive-after-reload.log
[2026-10-28T13:21:00Z] R copied 3ef67404f54b5d2688c4802b50951e28ea2318faba13023db39bbca6bbb44d1f /root/btc-forensics/tz33-work--logs--70-mark-start-svc.log
[2026-10-28T13:21:00Z] R copied f109ade972fafd1fdad12bde324f21470d0a314e2e3f17899228e2825b7e3241 /root/btc-forensics/tz33-work--logs--71-enable-refused.log
[2026-10-28T13:21:00Z] R copied 86a0838ba884daf1259ae8bba5216edb1f506b671426e74f81181bf07b696162 /root/btc-forensics/tz33-work--logs--71-enable.log
[2026-10-28T13:21:00Z] R copied 3c5a885f2544efbd79823dc16627e1a7a9c256278ecf4bee140e927789d6d57a /root/btc-forensics/tz33-work--logs--72-after-container-restart.log
[2026-10-28T13:21:00Z] R copied 2497c4ae5dffa265398706cd8cdcbcb5d028a17a05a995414d2af9a272745ab5 /root/btc-forensics/tz33-work--logs--73-enable-first-handover-lapsed.log
[2026-10-28T13:21:00Z] R copied 48cdc1f0c09fda1d60f49bba16fe80df49398b70b92107c9fc19b72f3cffdc02 /root/btc-forensics/tz33-work--logs--74-enable.log
[2026-10-28T13:21:00Z] R copied d504ad48f6477f28eb6fbb031e4f8c59790500888143424efcd5abf41ebdbe4a /root/btc-forensics/tz33-work--logs--75-unit-0.log
[2026-10-28T13:21:00Z] R copied 372108cd989d2fdc9de541ff4f8611a408e417100292df020f13f5fe75cbb769 /root/btc-forensics/tz33-work--logs--76-health-1.log
[2026-10-28T13:21:00Z] R copied d4990084c1cb03b394df5aba995305bec99f613ed481e29fa45ace2337fd3338 /root/btc-forensics/tz33-work--logs--80-prove-first.log
[2026-10-28T13:21:00Z] R copied 2d7c69de1e49fc2d265f3faffd5afceda6d89cce6543f3d6df58e4f1e147b674 /root/btc-forensics/tz33-work--logs--81-prove-second.log
[2026-10-28T13:21:00Z] R copied ecb1e9434ecf81f5e4952f50075c9ee849b102b994effd79267a8fdeb611c2f1 /root/btc-forensics/tz33-work--logs--82-load.log
[2026-10-28T13:21:00Z] R copied ff80aab221452857c3ea3779f97c10f76763957b7e1c5ec1b6b94b0608d60597 /root/btc-forensics/tz33-work--logs--90-mark-kill-svc.log
[2026-10-28T13:21:00Z] R copied b7adeae7b09011ad438ea3f5b10b93a2c9f1f96508f3e83c7d4d3a16f5c5c1c5 /root/btc-forensics/tz33-work--logs--91-kill-svc.log
[2026-10-28T13:21:00Z] R copied 2371872689c321a32aead567dbebc36661e43f71c5450beaff70726f53c17a4d /root/btc-forensics/tz33-work--logs--92-restart.log
[2026-10-28T13:21:00Z] R copied d44a4a5d2e55d764d911fca28264ea800b93f9d1f94eca0dd38ad7eed10c32d3 /root/btc-forensics/tz33-work--logs--93-resume-1.log
[2026-10-28T13:21:00Z] R copied 8fd684758a22df9f58ed17f93c9d0f4366a476780098d60e85b94410df6c2cc2 /root/btc-forensics/tz33-work--logs--94-resume-2.log
[2026-10-28T13:21:00Z] R copied 206e35ba3d435c30fc4fea8a7c437fc3d2180777785d4a11be903382408106d0 /root/btc-forensics/tz33-work--logs--95-final.log
[2026-10-28T13:21:00Z] R copied 8af57d45c919b61ef7af74f29306711693e280b4e44b83de4e2189f9cff6d4f2 /root/btc-forensics/tz33-work--logs--96-separation.log
[2026-10-28T13:21:00Z] R copied 9196e3c76283a2d687b7db77f4f8c5a46384d4d7697ab248e64fb8ba04d46934 /root/btc-forensics/tz33-work--logs--97-closing.log
[2026-10-28T13:21:00Z] R copied f535ad3ff92b9fae81567b23913282f4ea419dd4a6f66753b6a035abecb3708d /root/btc-forensics/tz33-work--logs--98-sessions-at-close.log
[2026-10-28T13:21:00Z] R copied 27bcadebdb5ec084c68f4f3ede62b5549cb7cff1e6512dca6538b4bce35bc56f /root/btc-forensics/tz33-work--logs--99-files-written.log
[2026-10-28T13:21:00Z] R copied 86f5f2853cafc9919b5a6a71a30d407972a6451e78802e5f2a5927960a8b1892 /root/btc-forensics/tz33-work--prestart--prestart.json
[2026-10-28T13:21:00Z] R copied 609c81fe54d984033b7dc3ed965c31c64bff0a24d870f190c4a255e84f607f6e /root/btc-forensics/tz33-work--prestart--stream.jsonl.gz
[2026-10-28T13:21:00Z] R copied e61f0a283f692ae42407097a4465e9049e5055591e3149a8017c45fc419642db /root/btc-forensics/tz33-work--prestart-2--prestart.json
[2026-10-28T13:21:00Z] R copied e92d0c0ce2d77e6285b2ad65a88e77aebb5b1dd2bd2029662c1a7c1cb446e0f4 /root/btc-forensics/tz33-work--prestart-2--stream.jsonl.gz
[2026-10-28T13:21:00Z] R copied 70ba7291b122421743c0287dd623fc268cb6be3dc0f5282879effe4b1fa73abf /root/btc-forensics/tz33-work--proof--proof-1793192110.json
[2026-10-28T13:21:00Z] R copied bbe12deec060ee9e71dbe1d7bc78e0fa15bf8648840442711c87ce5ed3b1218b /root/btc-forensics/tz33-work--report--build.py
[2026-10-28T13:21:00Z] R copied 189f28b5eb846eab03cd230d13b1516853f6e1a979769fac197398fbef449482 /root/btc-forensics/tz33-work--report--closing.sh
[2026-10-28T13:21:00Z] R copied 3e2309223343729a7ede1963b4e1f95878355e70f4f4c8ebbb6e28ebba65fba1 /root/btc-forensics/tz33-work--report--template.md
[2026-10-28T13:21:00Z] R copied 70a3e33e2e684b0edc420f977be9129d8f1de973852745d0bbeb9c78bd52e683 /root/btc-forensics/tz33-work--resume--resume-1793193313.json
[2026-10-28T13:21:00Z] R copied 7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec /root/btc-forensics/tz33-work--stage--deploy--systemd--btc-rewardbook.service
[2026-10-28T13:21:00Z] R copied a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670 /root/btc-forensics/tz33-work--stage--research--tz33-reward-book-capture.py
[2026-10-28T13:21:00Z] RECLAIM PASS: 57 files considered, 56 named by a report, 1 kept by name, 57 copied, 0 already held; forensic store 2044 -> 2101 files
[2026-10-28T13:21:00Z] peak memory of this run: 41840640 bytes
[2026-10-28T13:21:00Z] opens refused: 0; manifest opens 0; window opens 0; ledger opens 0; requests 0, stream sessions 0
exit=0
$ cd /root && git -C /root/btc-5m-twap worktree remove /root/tz33-work/wt; echo "exit=$?"
exit=0
$ cd /root && rm -rf /root/tz33-work; echo "exit=$?"
exit=0
$ test -e /root/tz33-work; echo "exit=$?"
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
$ find /root/btc-forensics -type f | wc -l
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
exit=1
/root/btc-5m-twap       adba104 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
2101
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11611832320
```

**`RECLAIM PASS`: 57 files considered, 56 named by a report and 1 kept by name — `logs/99-files-written.log`, whose own
hash no report prints — 57 copied, 0 already held; the forensic store 2,044 → 2,101**, equal to before plus the copies.
The branch worktree held exactly its pushed `HEAD`, `2dcd70e…`, and was copied nothing of; `git worktree remove` without
`--force` exit `0`; `rm -rf /root/tz33-work` exit `0`; `test -e` exit `1`; **the worktrees two**, the primary checkout and
`/root/btc-recorder-svc`, as map §3 has them; free on `/dev/vda2` 11,611,832,320 bytes. **Kept:** `/root/btc-rewardbook-svc/`,
the reward book's running code, with `/root/btc-recorder-svc/`, `/root/btc-pairbook-svc/`,
`/root/btc-pairbook-archive-svc/` and `/root/tz18a-svc/`; the four capture roots, the archive's state and the forensic
store. The branch `tz-33-reward-book-capture` stays on `origin` and as a local ref.

---

## 3. Publication

| step | result |
|---|---|
| branch | `tz-33-reward-book-capture`, one commit `2dcd70e08b18b93c64bb67d9849ac1216ce40e41` on `adba104`: `research/tz33-reward-book-capture.py` and `deploy/systemd/btc-rewardbook.service`, both `A`, Appendix A byte for byte |
| push | `git push -u origin tz-33-reward-book-capture`, `exit=0`, with the URL's own credential; `origin` carried it at 2026-10-28 06:13:45.819795934 UTC by `ls-remote`, equal to the worktree's `HEAD` |
| pull request | **#32**, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/32`, against `main`, `OPEN`; **not merged by the Executor** |
| the service's copy | `/root/btc-rewardbook-svc/tz33-reward-book-capture.py` `a276bbb9…` and `commit.txt` `2dcd70e…` |
| the unit | `/etc/systemd/system/btc-rewardbook.service`, `cmp` exit `0` against the branch's; enabled, the link `/etc/systemd/system/multi-user.target.wants/btc-rewardbook.service` |
| the report | `CryptoReports/TZ-33-reward-book-capture-report.md`, straight to `main` in one commit, the one path pushed to `main` |
| Release | none: TZ-33 creates none |
| separation self-check | §2.15, verbatim: `0`; the two implementation files; nothing |

---

## 4. Gate

The gates as TZ-33 §4 fixes them, and their readings. Nothing was tuned to reach them and no gate is reinterpreted.

| gate | PASS when | deciding number | reading |
|---|---|---|---|
| **P-START** | §4.1: 6 requests, 1 session, the seven session checks | 6 requests, 1 session, 7 of 7 — at both runs | **served** |
| **G-UNIT**, 0 restarts | 11 checks | 11 of 11 | **PASS** |
| **G-START** | 8 more | 8 of 8 | **PASS** |
| **G-SELECT** | every day re-derived equal with 150 members | 1 of 1 day, 150 members | **PASS** |
| **G-STREAM** | at least 3 of 4 qualifying slots complete | 4 of 4, `1.000` | **PASS** |
| **G-REWARDS** | at least 1,782 of 1,800 polls served | 1800 of 1800, `1.000` | **PASS** |
| **G-NEIGHBORS** | no counted failure, at least 8 intervals and 3 windows counted | 14 and 5 counted, 0 failing | **PASS (HOLD)** |
| **G-LOAD** | processor at most `1/10` of one core since the start | `0.0262` | **PASS** |
| **G-RESTART** | a `stop` of the marked pid and a `start` of another within 60 s, same commit and file; G-UNIT at 1 restart | 5.831 s; 11 of 11 | **PASS** |
| **G-RESUME** | the first slot opening at least 60 s after the restart complete | slot `1793192400` complete | **PASS** |
| **G-UNIT**, 1 restart, at `final` | 11 checks | 11 of 11 | **PASS** |
| **G-STILL** | the recorder unchanged; the pair book unchanged or moved by the archive's own restarts alone | recorder unchanged; pair book moved by 2 restarts of the archive's ledger | **PASS** |

**K-33 was not run**: no gate read FAIL. **The reward book runs on after the session**, as `btc-rewardbook.service`, pid
`3137952`, `NRestarts` `1`, `active` and `enabled` — verified by `I final` and by §3.11's `systemctl show`, `is-enabled`
and `journalctl`, not from the Boss's account.

---

## 5. Validation

| # | check | count | asserted |
|---|---|---|---|
| **V1** | §0.2's fingerprint | `FINGERPRINT PASS`: revision `2026-10-27-b`; anchors 6 of 6, 4 re-derived; 44 rows, 41 of 41 `frozen` equal, 2 `tracked`, 1 `reported`; the map 1,685 lines, 398,963 bytes, `01d01587…` | asserted by `fingerprint` |
| **V2** | §0.3's host gate | H1 to H5, memory and disk: 7 of 7 PASS (§0.3); the rest printed | read by the Executor against §0.3's conditions; the shell block asserts nothing |
| **V3** | §0.1's and §3.1's files | 2 of 2 hashes asserted at each run of the script, lines and bytes equal to §0.1's table; the branch's diff names exactly the two paths, both `A` | asserted by the script; the diff read |
| **V4** | the self-test | `99 of 99 checks passed` | asserted |
| **V5** | §3.4's copy | 2 of 2 hashes Appendix A's; `commit.txt` the branch head, 41 bytes | read by the Executor; the block asserts nothing |
| **V6** | P-START | `READING P-START: served` at both runs; 6 requests, 1 session, 7 of 7; `m_r` 2016, `f_r` 2, `m_p` 672, `f_p` 2; the false failure `0.0303150318` | asserted by `prestart` |
| **V7** | B-INSTALL | `cmp` exit `0`; `daemon-reload` exit `0`; `verify` exit `0`, no finding | exits read |
| **V8** | G-UNIT and G-START at `unit 0`; G-UNIT at 1 restart | 11 of 11 and 8 of 8; 11 of 11 at `restart` and at `final` | asserted |
| **V9** | G-SELECT, G-STREAM, G-REWARDS, G-NEIGHBORS | PASS 1 of 1; PASS 4 of 4; PASS 1800 of 1800; PASS (HOLD) 14 and 5 counted, 0 failing; 5 considered slots disclosed with their reasons, indices and counts; 19 neighbouring units with whether each counted and failed | asserted per check and printed; the readings computed by `prove` |
| **V10** | determinism | `unchanged`, `proof-1793192110.json` `70ba7291b122421743c0287dd623fc268cb6be3dc0f5282879effe4b1fa73abf` | asserted by `prove`'s second run |
| **V11** | G-LOAD | `0.0262` against `0.10`; the memory reads | asserted |
| **V12** | G-RESTART | `stop` of `3119051` at 12:56:23, `start` of `3137952` at 12:56:29, 5.831 s | asserted |
| **V13** | G-RESUME | slot `1793192400` complete; the kill's slot `1793191500` indices `0` (stopped) and `1` (joined late) | asserted |
| **V14** | G-STILL | the recorder unchanged; the pair book moved by the archive's two restarts alone, named by its ledger and its journal | asserted by `final` |
| **V15** | opens under the capture roots | refused `0` at every mode; manifest opens `2016` by each `prestart` and `14` by each deciding `prove`, at most `16`; window opens `672` by each `prestart` and `5` by each `prove`, at most `5`; ledger opens `0` by `still` and `1` by `final`; `0` of each elsewhere | counted by the audit hook, printed |
| **V16** | contract §4.2's self-check | `0`; two implementation paths; nothing — after the push and the PR, before the report's commit | read |
| **V17** | §3.11's closing reads | every read printed, §2.15 | printed |
| **V18** | §9's `reclaim` runs | B-RECLAIM-SCRATCH: no `reclaim` summary on record (§2.4); B-RECLAIM-OWN: §2.17 | asserted by `reclaim` where it ran |
| **V19** | §9's removals | §2.4: `test -e` exit `1` for each of the four earlier directories; §2.17: `git worktree remove` without `--force`, `test -e /root/tz33-work`, `git worktree list` | exits read |

---

## 6. What could not be implemented as written

1. **B-RECLAIM-SCRATCH was run by the Boss, and its order is not on record** (§2.4). The classifier refused `I reclaim`
   at 06:15:13 UTC. The Executor handed the block over in two parts, the four `rm -rf` to be run only after `RECLAIM PASS`.
   The four earlier directories were removed at 06:28:17 UTC, in a root login whose output survives nowhere. The second
   login's `reclaim` stopped at its first assert because the directories were already gone, and its `rm -rf` removed
   nothing. The Boss states that `RECLAIM PASS` printed before the removal; the host's record neither confirms nor refutes
   it. The outcome is §9's — the four gone, none live, not this session's own, the forensic store unchanged at 2,044 —
   and the order §9 requires is not established.
2. **B-ENABLE was refused and handed over twice** (§2.8). The first hand-over lapsed: the Boss's login ended at 06:54:08
   UTC, before the band, and the unit stayed installed and never started until 11:30:15. By §3.7's own rule §3.5 ran
   again, into `prestart-2`, served. **The `start-svc` mark of 06:34:54 stands for the second hand-over**, because `mark`
   refuses a second `start-svc`; it precedes the block and the one `start` record, as G-START reads it.
3. **The blocks as handed over carried small additions:** B-ENABLE's one `date -u` before its wait, recording the
   block's start against §3.7's 3,600 s, and its output to `logs/71-enable.log` and, the second time,
   `logs/74-enable.log`; B-RECLAIM-SCRATCH in two parts, with its output to `logs/32-reclaim-scratch.log` and
   `logs/33-rm-scratch.log`. §3.4's block was run with three lines more: the exits of `git show` and `git rev-parse`, and
   `wc -c` of `commit.txt`.
4. **This TZ's own systemd steps set off two runs of the archive off its calendar** (§2.13): B-INSTALL's `daemon-reload`
   at 06:34:32 UTC re-armed the timer for 06:44:32, and B-ENABLE's `enable --now` at 11:30:15 for 11:40:16 — map §7
   item 115's hypothesis, observed. §3.7 placed B-ENABLE away from the archive's calendar run and did not foresee these.
   Each restarted the pair book inside its band and cost no window this TZ reads; G-STILL counts both as the archive's;
   they add two tags beyond §0.5's projection, `pairbook-streams-1793169873` and `pairbook-streams-1793187616`.
5. **The session's container was restarted** at about 10:56 UTC, between the two hand-overs. The session's background
   wait on B-ENABLE's log was lost, and nothing on the host depended on it. The session's process changed from `3071142`
   to `3115475`, so this session leaves three directories beside its own for the next TZ (§2.15), not one pair.
6. **Reads no step names**, each of systemd's units, a login record or file metadata, none under a capture root:
   `logs/34-…` (`test -e`, `stat`, `last`, the forensic store's count and newest files), `logs/35-…` (`findmnt` and the
   reports' `stat`), `logs/62-…` and `logs/72-…` (`systemctl show`, `list-timers`, `last`), `logs/76-…` (`systemctl show`),
   `logs/98-…` (`ps` and `ls` of the session directories), and in `logs/96-…` an `ls-remote` of the two branches and `gh
   pr view`.
7. **The push's output was passed through `grep -v -E 'ghp_|@github'`**, so that no credential could reach the log; its
   exit is git's own, through `PIPESTATUS`. The push went through with the URL's own credential, where TZ-29 to TZ-32
   used `gh`'s (map §7 item 114).
8. **One line of `logs/35-reclaim-scratch-boss-statement.log` miscounted the reports as 43**; a line appended to the same
   log, from `ls | wc -l`, corrects it to 42. No log was edited.
9. **This report was assembled by a script**, `report/build.py`, from `report/template.md` and the logs, each log quoted
   whole; the script also checked that every figure typed in the narrative appears in a log or in TZ-33 itself, and
   found 12 that do not: nine section numbers, `1.000` — §4's deciding numbers to three decimals — and three instants
   shortened to hundredths of a second. Its three files are in §2.16's list, so B-RECLAIM-OWN copies them.

None moves a reading: the instrument's and the unit's bytes were fixed by Appendix A's hashes, every gate was read by
the instrument's own modes, and the proof's second run printed `unchanged`.


