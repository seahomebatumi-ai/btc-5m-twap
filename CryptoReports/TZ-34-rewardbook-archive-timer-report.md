# TZ-34 report — the reward book's archive on a timer: its closed slots' streams to a Release, once a day, unattended

**P-PATH: served**, 3 requests, each inside the idle stretch, at 07:48 UTC · **P-TOKEN: served** inside B-ENABLE, run by the Boss at 08:17:05 UTC: the source the primary checkout's remote URL, `push` true, Release `409534533`, 2 requests.
**G-INSTALL PASS: 9 of 9**, after B-INSTALL's 7 of 7 `exit=0` (`L` = 07:49:22.127 UTC) · **G-TIMER PASS, 9 of 9** at 08:17:07 UTC, 2 s after `E`, and again at `final`; **the next calendar run 2026-10-30 01:30:20 UTC**.
**The first run, `A` = `1793263627`** (2026-10-29 08:47:07 UTC), fired by the timer's 1,800 s elapse: **86 stream files of 85 closed slots, `1793187000` … `1793262600`, `890,975,956` bytes, to Release `427629503` on the lightweight tag `rewardbook-streams-1793263627` at `6a61525`**. It deferred once, in its verify, while the repository did not serve its Releases anonymously; **B-RETRY**, run once at 09:01:12 UTC after the Boss set the repository public again, resumed the same set to `complete` at 09:04:30 UTC.
**G-UPLOAD PASS**, 86 of 86 by name, bytes, state and digest · **G-DOWNLOAD PASS**, 86 of 86 downloads equal · **G-DELETE PASS**, 86 gone, 86 removals recorded, 85 slots keep their `slot.json` · **`890,975,956` bytes freed**, free space `10,304,053,248` → `11,195,334,656`.
**G-IDLE PASS**: 180 requests and 86 removals, 0 started outside the idle stretch, 0 ended outside it.
**G-NEXT PASS** over its 1 slot, 09:15 UTC, streamed by the reward book's process `3137952` · with **G-TRIGGER PASS** (by `TRIGGER_UNIT`), **G-RUN PASS** and **G-SET PASS**: **FIRST PASS: 8 of 8**.
**G-STILL PASS**: the recorder (`2388318`, `NRestarts` 0), the pair book (`3216422`, 12) and the reward book (`3137952`, 1) unchanged from 07:46:51 to 09:31:54 UTC.
**The timer, the reward book, the pair book and the recorder run** — the timer `active`, `waiting`, `enabled`; the three capture units `active` — verified by `I final` and by §3.9's `systemctl show`, `list-timers` and `journalctl`, never from the Boss's account. K-34, B-UNINSTALL and B-START-RB were not run.
**Departures, all in §6**: the repository not public from between 07:48 and 08:02 UTC to about 09:00 UTC, by the Boss's account; the pair book's archive's off-calendar run deferring (exit `75`) at 08:02:57 UTC for it; B-RETRY used; two runs of `path` beyond §3.4; B-ENABLE's `enable` setting off no run of the pair book's archive; one copy written to the session's scratchpad and removed.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-34-rewardbook-archive-timer.md`, 2,824 lines, 194,512 bytes, SHA-256 `61f24b2998e4d1b2792daed7010464d2ae6e18b21e8fbe8757587ea866da288c`, landed at `ca85b08` |
| map revision | `2026-10-28-a`, equal; anchors 6 of 6; re-derived 4 of 4; rows 46; `frozen` equal 43 of 43 |
| executor model | Opus 5.5, as the TZ names: `get_session` read `session_context.model` and `last_served_model` as `claude-opus-5-5` (`logs/06-model.log`) |
| branch | `tz-34-rewardbook-archive-timer` at `6a615257277d3c94dafd4d39783499560a344648`, pushed; pull request #34, open, not merged |
| instrument | `research/tz34-rewardbook-archive-timer.py`, 1,791 lines, 99,388 bytes, SHA-256 `1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72`, Appendix A byte for byte |
| units | `deploy/systemd/btc-rewardbook-archive.service`, 17 lines, 810 bytes, `a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f`; `deploy/systemd/btc-rewardbook-archive.timer`, 13 lines, 428 bytes, `bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f`; Appendix A byte for byte, installed byte for byte under `/etc/systemd/system/` |
| service's code | `/root/btc-rewardbook-archive-svc/`: the instrument `1d8aa514…`, TZ-28's `46a019d6…`, TZ-27's `2cba96bc…`, `commit.txt` `6a615257277d3c94dafd4d39783499560a344648` |
| state | `/var/lib/btc-rewardbook-archive/`, root's, `0700`; the ledger 9 records |
| the first run | `A` `1793263627`; invocations `957b92a52a0b4e71ba3aa47b0d3cfee4` (the timer's, deferred) and `a1eb6d29178b4815966bcd5051a3c604` (B-RETRY's, complete) |
| Release | id `427629503`, tag `rewardbook-streams-1793263627`, lightweight, at `6a615257277d3c94dafd4d39783499560a344648`; 86 assets |
| interpreter | `/root/tz04a-env/venv/bin/python` 3.12.3; every session mode under `nice -n 19` and `-B`, the unit under `Nice=19` |
| instants | the enable mark 08:15:15.765 UTC; `L` 07:49:22.127071410 UTC; `E` 08:17:05.684473573 UTC; the retry mark 09:01:01.750 UTC |

---

## 0. Fingerprint

`I0 fingerprint`, from the staged copy, against the primary checkout at `0968707` — revision `2026-10-28-a`; anchors `A1` `229a944f2d51`, `A2` `6c5089330629`, `A3` `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable`, `A4` `437b45ea196b`, `A5` `0f6c90451cbd`, `A6` `729f0bcdbee3`, each equal to the TZ header's; `A2`, `A4`, `A5` and `A6` re-derived. **V1: `FINGERPRINT PASS`.** The map: 1,808 lines, 423,732 bytes, SHA-256 `0d2d971a232be87a9b6d93bfe656950cbeef9a7824f9f5839add4b3966d49476`.

### 0.1 The 46 rows of the map's §0 table, and the map (V1) — `logs/02-fingerprint.log`, verbatim

```
2026-10-29T07:44:53.042458843Z
[2026-10-29T07:44:53Z] re-derived A2 research/twap-divergence.py sha256[:12] 6c5089330629 equal
[2026-10-29T07:44:53Z] re-derived A4 BTC-EXECUTOR-INSTRUCTIONS.md sha256[:12] 437b45ea196b equal
[2026-10-29T07:44:53Z] re-derived A5 research/recorder/recorder.py sha256[:12] 0f6c90451cbd equal
[2026-10-29T07:44:53Z] re-derived A6 research/pfair.py sha256[:12] 729f0bcdbee3 equal
[2026-10-29T07:44:53Z] SYSTEM-MAP.md                                  1808 lines   423732 bytes 0d2d971a232be87a9b6d93bfe656950cbeef9a7824f9f5839add4b3966d49476 reported
[2026-10-29T07:44:53Z] BTC-EXECUTOR-INSTRUCTIONS.md                    234 lines    11128 bytes 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b frozen equal
[2026-10-29T07:44:53Z] research/twap-divergence.py                    1135 lines    50928 bytes 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 frozen equal
[2026-10-29T07:44:53Z] research/selftest-twap-divergence.py            376 lines    16736 bytes ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a frozen equal
[2026-10-29T07:44:53Z] research/tz02-distribution.py                   334 lines    14511 bytes f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 tracked
[2026-10-29T07:44:53Z] research/pfair.py                               441 lines    19357 bytes 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 frozen equal
[2026-10-29T07:44:53Z] research/selftest-pfair.py                      619 lines    32559 bytes b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa frozen equal
[2026-10-29T07:44:53Z] research/tz06-calibration.py                    577 lines    27138 bytes 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f frozen equal
[2026-10-29T07:44:53Z] research/tz07a-variance-time.py                 623 lines    28414 bytes 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 frozen equal
[2026-10-29T07:44:53Z] research/tz07b-settlement-dispersion.py         515 lines    24926 bytes 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc frozen equal
[2026-10-29T07:44:53Z] research/tz08a-out-of-sample.py                 745 lines    38822 bytes 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c frozen equal
[2026-10-29T07:44:53Z] research/tz09-disk-inventory.py                 894 lines    41004 bytes b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 frozen equal
[2026-10-29T07:44:53Z] research/tz10b-sigma-or-link.py                1224 lines    61018 bytes 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 frozen equal
[2026-10-29T07:44:53Z] research/tz11a-student-link.py                 1231 lines    64732 bytes 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 frozen equal
[2026-10-29T07:44:53Z] research/tz12-sized-gate.py                    1157 lines    61637 bytes d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 frozen equal
[2026-10-29T07:44:53Z] research/tz13-sized-gate-test3.py              1074 lines    53901 bytes a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd frozen equal
[2026-10-29T07:44:53Z] research/tz14-quote-inventory.py               2124 lines   109972 bytes 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 frozen equal
[2026-10-29T07:44:53Z] research/tz15-phase2-gate.py                   1517 lines    73799 bytes 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 frozen equal
[2026-10-29T07:44:53Z] research/tz16a-phase2-decisive-gate.py         2198 lines   111192 bytes 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 frozen equal
[2026-10-29T07:44:53Z] research/tz17-settlement-chain.py              1102 lines    38622 bytes e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 frozen equal
[2026-10-29T07:44:53Z] research/tz18a-chainbook-capture.py            1683 lines    69517 bytes e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae frozen equal
[2026-10-29T07:44:53Z] research/tz20-capture-under-systemd.py          771 lines    36528 bytes 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7 frozen equal
[2026-10-29T07:44:53Z] research/tz21-recorder-memory.py               1284 lines    59009 bytes d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f frozen equal
[2026-10-29T07:44:53Z] research/tz23-maker-m0.py                      1184 lines    54885 bytes 6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f frozen equal
[2026-10-29T07:44:53Z] research/tz24-nesting-b2.py                    1535 lines    76142 bytes 4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b frozen equal
[2026-10-29T07:44:53Z] research/tz26-nesting-b3-capture.py            2492 lines   118466 bytes caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec frozen equal
[2026-10-29T07:44:53Z] research/tz27-pairbook-archive.py              2078 lines   106284 bytes 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673 frozen equal
[2026-10-29T07:44:53Z] research/tz28-pairbook-archive-timer.py        1438 lines    74576 bytes 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4 frozen equal
[2026-10-29T07:44:53Z] research/tz29-maker-m0-second-look.py          1225 lines    68959 bytes 18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905 frozen equal
[2026-10-29T07:44:53Z] research/tz30-nesting-b3-measure.py            2518 lines   131119 bytes 93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab frozen equal
[2026-10-29T07:44:53Z] research/tz31-who-earns.py                     1523 lines    84775 bytes 7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765 frozen equal
[2026-10-29T07:44:53Z] research/tz32-our-quoting.py                   2576 lines   138209 bytes 6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61 frozen equal
[2026-10-29T07:44:53Z] research/tz33-reward-book-capture.py           3542 lines   175160 bytes a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670 frozen equal
[2026-10-29T07:44:53Z] research/recorder/recorder.py                   651 lines    27821 bytes 0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7 frozen equal
[2026-10-29T07:44:53Z] research/recorder/config.py                     112 lines     4773 bytes 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d frozen equal
[2026-10-29T07:44:53Z] research/recorder/manifest.py                   254 lines    10002 bytes 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 frozen equal
[2026-10-29T07:44:53Z] research/recorder/analyze.py                    813 lines    34705 bytes eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d frozen equal
[2026-10-29T07:44:53Z] research/recorder/probe.py                      227 lines     9324 bytes 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 frozen equal
[2026-10-29T07:44:53Z] research/recorder/selftest.py                   573 lines    30591 bytes c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 frozen equal
[2026-10-29T07:44:53Z] deploy/systemd/btc-recorder.service              23 lines      707 bytes 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1 frozen equal
[2026-10-29T07:44:53Z] deploy/systemd/btc-chainbook.service             22 lines      724 bytes a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2 frozen equal
[2026-10-29T07:44:53Z] deploy/systemd/btc-pairbook.service              22 lines      761 bytes ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8 frozen equal
[2026-10-29T07:44:53Z] deploy/systemd/btc-pairbook-archive.service      17 lines      794 bytes 2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7 frozen equal
[2026-10-29T07:44:53Z] deploy/systemd/btc-pairbook-archive.timer        13 lines      417 bytes 07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913 frozen equal
[2026-10-29T07:44:53Z] deploy/systemd/btc-rewardbook.service            23 lines      817 bytes 7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec frozen equal
[2026-10-29T07:44:53Z] .gitignore                                        5 lines      252 bytes 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b tracked
[2026-10-29T07:44:53Z] SYSTEM-MAP.md 1808 lines 423732 bytes sha256 0d2d971a232be87a9b6d93bfe656950cbeef9a7824f9f5839add4b3966d49476
[2026-10-29T07:44:53Z] FINGERPRINT PASS: revision 2026-10-28-a; anchors 6 of 6, 4 re-derived; rows 46: frozen 43 of 43 equal, tracked 2, reported 1
[2026-10-29T07:44:53Z] peak memory of this run: 38068224 bytes
[2026-10-29T07:44:53Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

### 0.2 Contract §1, §0.0 and §0.1 — the start-up, the work tree and the instrument staged (V3)

Contract §1 step 1 was `git fetch origin main` and `git merge --ff-only origin/main` on `main`, clean, `2898160` → `0968707`; step 2 read this TZ, the map and the contract in full. Then §0.0's `mkdir`, whose output was written to its log once the directory existed (§6):

```
2026-10-29T07:44:30.809728712Z
mkdir /root/tz34-work /root/tz34-work/logs; echo "exit=$?"
exit=0
```

```
2026-10-29T07:44:36.751828548Z
main
0968707446d0bc549137b152d37be972e9f6781c
0968707446d0bc549137b152d37be972e9f6781c
0968707 Add files via upload
ca85b08 Add files via upload
5efec8f Update ADVISOR-SKILL.md
61f24b2998e4d1b2792daed7010464d2ae6e18b21e8fbe8757587ea866da288c  CryptoTZ/TZ-34-rewardbook-archive-timer.md
  2824 194512 CryptoTZ/TZ-34-rewardbook-archive-timer.md
ca85b080bb24c3ecbcbe89b83723a3beefe738e3 2026-10-29 10:25:50 +0400 Add files via upload
```

§0.1's script, verbatim, its argument `/root/tz34-work/stage`, then TZ-28's and TZ-27's files beside it — **3 of 3 hashes asserted, lines and bytes as §0.1's table; `46a019d6…` and `2cba96bc…`**:

```
2026-10-29T07:44:46.926884466Z
/root/tz34-work/stage/deploy/systemd/btc-rewardbook-archive.service 17 810 a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f
/root/tz34-work/stage/deploy/systemd/btc-rewardbook-archive.timer 13 428 bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f
/root/tz34-work/stage/research/tz34-rewardbook-archive-timer.py 1791 99388 1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72
exit=0
exit=0
46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4  /root/tz34-work/stage/research/tz28-pairbook-archive-timer.py
2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673  /root/tz34-work/stage/research/tz27-pairbook-archive.py
```

The model, read by the Executor through `get_session` — a note, not a command's output:

```
2026-10-29T07:50:56Z get_session (claude-code-remote MCP, session_id omitted), read by the Executor:
session_context.model claude-opus-5-5
external_metadata.last_served_model claude-opus-5-5
configured_model claude-opus-5-5
The TZ names: Claude Opus 5.5.
```

### 0.3 Host gate — §0.3's block, verbatim (V2)

```
Thu Oct 29 07:45:05 AM UTC 2026
1793259905
1
MemTotal:         978640 kB
MemAvailable:     303320 kB
SwapTotal:       3174396 kB
SwapFree:        2755408 kB
2026-08-02 07:24:32
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
 -5 23a31fad2f064f04b9e138eac29658f3 Sun 2026-06-21 21:37:37 UTC Fri 2026-06-26 14:13:44 UTC
 -4 a38e17445ce341bc8b877be9d3d4f648 Fri 2026-06-26 14:13:52 UTC Tue 2026-07-14 16:15:10 UTC
 -3 5f4d18a6ba8041bd80e7d1e192c5ee28 Tue 2026-07-14 16:15:20 UTC Fri 2026-07-17 01:01:21 UTC
 -2 b1b399c70c6e4dcc934755f70a2ca231 Fri 2026-07-17 01:01:43 UTC Fri 2026-07-24 14:55:46 UTC
 -1 285d6962c92c407d837d1ce329b93aa4 Fri 2026-07-24 14:55:54 UTC Sun 2026-08-02 07:23:49 UTC
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-02 07:24:34 UTC Thu 2026-10-29 07:45:04 UTC
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10491797504
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
3
3.12.3
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
NEXT                           LEFT LAST                              PASSED UNIT                       ACTIVATES
Thu 2026-10-29 09:47:27 UTC 2h 2min Wed 2026-10-28 23:40:52 UTC       8h ago apt-daily.timer            apt-daily.service
Fri 2026-10-30 03:00:20 UTC     19h Thu 2026-10-29 03:00:20 UTC 4h 44min ago btc-pairbook-archive.timer btc-pairbook-archive.service
Fri 2026-10-30 06:36:47 UTC     22h Thu 2026-10-29 06:19:40 UTC 1h 25min ago apt-daily-upgrade.timer    apt-daily-upgrade.service

3 timers listed.
btc-recorder.service cmp exit=0
btc-pairbook.service cmp exit=0
btc-pairbook-archive.service cmp exit=0
btc-pairbook-archive.timer cmp exit=0
btc-rewardbook.service cmp exit=0
2dcd70e08b18b93c64bb67d9849ac1216ce40e41
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670  /root/btc-rewardbook-svc/tz33-reward-book-capture.py
46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4  /root/btc-pairbook-archive-svc/tz28-pairbook-archive-timer.py
2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673  /root/btc-pairbook-archive-svc/tz27-pairbook-archive.py
/root/btc-rewardbook-archive-svc exit=1
/var/lib/btc-rewardbook-archive exit=1
/etc/systemd/system/btc-rewardbook-archive.service exit=1
/etc/systemd/system/btc-rewardbook-archive.timer exit=1
/root/tz33-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
/root/btc-pairbook-archive-svc exit=0
/var/lib/btc-pairbook-archive exit=0
/root/btc-rewardbook-svc exit=0
/var/lib/btc-rewardbook exit=0
73766 /var/lib/btc-pairbook-archive/ledger.jsonl
9200 /var/lib/btc-rewardbook/runtime.jsonl
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
2101
/root/btc-5m-twap       0968707 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
851259950	/var/lib/btc-rewardbook
443163444	/var/lib/btc-pairbook
11072382	/var/lib/btc-pairbook-archive
117157970	/root/.claude
659650103	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/540c6c83-4413-5ceb-86a4-2d45c7f8989a/scratchpad
total 28
drwx------  7 root root 4096 Oct 29 07:43 .
drwx------ 32 root root 4096 Oct 29 07:43 ..
drwx------  4 root root 4096 Oct 28 06:09 0358b0b2-9811-5291-867b-b185a7307938
drwx------  4 root root 4096 Oct 29 07:43 540c6c83-4413-5ceb-86a4-2d45c7f8989a
drwx------  3 root root 4096 Oct 29 07:43 57feec2d-2369-4cb0-9cad-8ac28cb7e578
drwx------  3 root root 4096 Oct 28 06:09 621e47cc-760f-4cb1-8481-c2a8f6828d9d
drwx------  3 root root 4096 Oct 28 10:56 b82e3547-dd0e-46f7-abe9-4ad9e7903328
```

| gate | reading | result |
|---|---|---|
| H1 | one path: `/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json` | PASS |
| H2 | `/dev/vda2`, `31612203008`; `grep -c` `3` | PASS |
| H3 | `3.12.3` | PASS |
| H4 | `btc-rewardbook.service` `active`, `enabled`; `cmp` `0` for `btc-rewardbook.service`, `btc-pairbook-archive.service` and `btc-pairbook-archive.timer`; `commit.txt` `2dcd70e0…` and `d8194fd5…`; `a276bbb9…`, `46a019d6…`, `2cba96bc…` | PASS |
| H5 | the four paths `exit=1` | PASS |
| memory | `MemAvailable` `303,320` kB = `310,599,680` bytes ≥ `120,676,352` | PASS |
| disk | `avail` `10,491,797,504` ≥ `2,300,000,000` | PASS |

Printed, no threshold: one boot since 2026-08-02 07:24:34 UTC; the eight units — the pair book `3216422`, `NRestarts` 12, active since today's calendar archive run at 03:05:31; the three timers — `apt-daily-upgrade.timer` last at 06:19:40 UTC today, next 2026-10-30 06:36:47; `cmp` `0` for the recorder's and the pair book's units too; the pair archive's ledger `73,766` bytes and the reward book's `runtime.jsonl` `9,200`; `telemetry-watch.service` `disabled`, `inactive`; the recorder's tree `e3975b5…`; `/root/tz33-work` absent and the code and state trees present; the forensic store `2,101` files, map §3's; two worktrees, map §3's; `du` `851,259,950` of the reward book's store, `443,163,444` of the pair book's, `11,072,382` of its archive's state, `117,157,970` of `/root/.claude`, `659,650,103` of `/root/PROJECT_GAMING_PS5`; and the five UUID directories of the session's parent, its own among them.

### 0.4 Free space and `MemAvailable` — every read, its instant and its bound

| instant (UTC) | read by | `MemAvailable`, bytes | bound | free on `/dev/vda2`, bytes | bound |
|---|---|---|---|---|---|
| 07:45:05 | §0.3 | 310,599,680 | 120,676,352 | 10,491,797,504 | 2,300,000,000 |
| 07:48:26 | `path` | 320,000,000 | 93,454,336 | — | — |
| 08:15:37 | journal read of the pair archive (§2.7) | 363,487,232 | — | 10,416,041,984 | — |
| 08:17:05 | `path-token`, in B-ENABLE | 338,145,280 | 93,454,336 | — | — |
| 08:53:42 | `path`, diagnostic | 302,534,656 | 93,454,336 | — | — |
| 08:54:02 | the read after the deferral (§2.8) | — | — | 10,337,398,784 | — |
| 09:00:51 | `path`, the re-check | 275,009,536 | 93,454,336 | — | — |
| 09:04:28 | the run's removal, before | — | — | 10,304,053,248 | 2,002,000,000 (the run's floor) |
| 09:04:30 | the run's removal, after; its `complete` | — | — | 11,195,334,656 | — |
| 09:31:54 | `final` | — | — | 11,126,837,248 | — |
| 09:32:14 | §3.9, `/proc/meminfo` and `df` | 263,163,904 | — | 11,126,423,552; 11,126,394,880 | — |
| 09:32:15 | §3.9, `free -b`, `available` | 433,721,344 | — | — | — |

The run's own reads of both against `RUN_MEM_FLOOR` `73,121,792` and `DISK_FLOOR` `2,002,000,000`, at each of its two invocations' starts, are lines of `archive.log` above §3.9's 120-line tail, which this TZ allows no other read of; both invocations proceeded past them, and the second recorded `peak_rss` `39,477,248`. **Session peaks**, each mode's own line: `fingerprint` 38,068,224; **`selftest` 61,313,024** — above the Architect's largest, 60,338,176, and below §0.4's floor, twice that, 120,676,352 (§6); `still` 38,334,464; `scratch` 38,338,560; `reclaim` 39,337,984; `path` 40,452,096 and 40,189,952; `installed` 38,203,392; `mark` 38,207,488 and 38,072,320; `path-token` 39,153,664; `timer` 38,072,320; `first` 38,072,320 to 39,141,376; `final` 37,941,248. The diagnostic `path` of 08:53 stopped at its assert before its peak line.

### 0.5 Refs (§0.5) — `logs/05-refs.log`, verbatim, read at 07:45:16 UTC, before §3.1's push

```
2026-10-29T07:45:16.451795586Z
0968707446d0bc549137b152d37be972e9f6781c	HEAD
0968707446d0bc549137b152d37be972e9f6781c	refs/heads/main
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
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
e299d4e45f48b7efaa8cb18bd54b139fc0627630	refs/tags/tz-27-pairbook-streams
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/tags/tz-27-pairbook-streams^{}
exit=0
```

**79 ref lines** against map §1's and §0.5's **78**: the one more is `refs/tags/pairbook-streams-1793242820`, the pair book's archive's calendar run of 03:00:20 UTC today. `HEAD` and `main` at `0968707`; eleven branches with `main`; the two annotated tags and their peeled lines; thirty-one `pairbook-streams-*` tags; thirty-two pull heads; no merge ref. **`main` carries revision `2026-10-28-a`; no `refs/heads/tz-34-rewardbook-archive-timer` and no `refs/tags/rewardbook-streams-*` existed** — none of §0.5's three BLOCKs. Every commit on `main`'s first-parent line above `6467d84`, with the paths it changed:

```
2026-10-29T07:45:28.560534501Z
6467d84 Update SYSTEM-MAP.md
0968707 0968707446d0bc549137b152d37be972e9f6781c 2026-10-29 10:33:02 +0400 Add files via upload
ca85b08 ca85b080bb24c3ecbcbe89b83723a3beefe738e3 2026-10-29 10:25:50 +0400 Add files via upload
5efec8f 5efec8fe25f452963fc51c87c03aa9fcc9b0e985 2026-10-28 19:04:18 +0400 Update ADVISOR-SKILL.md
d2ccfd4 d2ccfd4e6e4cdc5930ce6f4fe533ba9452e78880 2026-10-28 18:57:44 +0400 Update ADVISOR-SKILL.md
45280e6 45280e61763df94eda7611ee121a94416150de83 2026-10-28 18:33:12 +0400 Update ADVISOR-SKILL.md
69f27e4 69f27e409a96d8e7f291fcd76cfbadbdfae36bdf 2026-10-28 18:23:01 +0400 Create adv2-signal.yml
ef6184a ef6184a1534e6d6e938049c0cdd10cd60245d4cb 2026-10-28 18:17:58 +0400 Add files via upload
---
== 0968707 Add files via upload
A	CryptoTZ/TZ-34-advisor-bot.md
== ca85b08 Add files via upload
A	CryptoTZ/TZ-34-rewardbook-archive-timer.md
== 5efec8f Update ADVISOR-SKILL.md
M	ADVISOR-SKILL.md
== d2ccfd4 Update ADVISOR-SKILL.md
M	ADVISOR-SKILL.md
== 45280e6 Update ADVISOR-SKILL.md
M	ADVISOR-SKILL.md
== 69f27e4 Create adv2-signal.yml
A	.github/workflows/adv2-signal.yml
== ef6184a Add files via upload
A	ADVISOR-SKILL.md
---
3:**Revision 2026-10-28-a.** Written by the Architect; the Executor never edits it. This is a
18:**Revision string:** `2026-10-28-a`
238:**Revision `2026-10-27-b` reached `main` at `31d5bce` and is confirmed there**, as §7 item 18's rule requires of
0d2d971a232be87a9b6d93bfe656950cbeef9a7824f9f5839add4b3966d49476  -
```

The five of §0.5 — `ef6184a`, `69f27e4`, `45280e6`, `d2ccfd4`, `5efec8f` — adding or changing `ADVISOR-SKILL.md` and `.github/workflows/adv2-signal.yml`; then **two uploads**, not one: `ca85b08`, this TZ, and `0968707`, which adds `CryptoTZ/TZ-34-advisor-bot.md` — neither a row of map §0. Recorded; the branch is based on `0968707` (§2.1).

---

## 1. Input

Read: this TZ, `SYSTEM-MAP.md` and `BTC-EXECUTOR-INSTRUCTIONS.md` in full; the 46 files of map §0's table, by `fingerprint`; `research/tz28-pairbook-archive-timer.py` and `research/tz27-pairbook-archive.py`, loaded by their SHA-256 by every mode; `research/tz33-reward-book-capture.py`, read by the self-test against its SHA-256 `a276bbb9…`; the five units §0.3 compares. **Nothing was re-collected and nothing was measured** (CANON hard rule 11). The reward book's store was read by the unit's run alone — the set's 86 stream files as bytes, hashed in pieces and never decompressed, its directory entries, its `runtime.jsonl` in the removal — and by the session's `first`, 4 opens: `runtime.jsonl` and the `slot.json` of G-NEXT's slot and of the 2 slots the run spanned. Outside the instrument only §0.3's and §3.9's `stat`, `du` and `tail` of `service.log`, and one `du` at 08:54 (§6). No rewards file, selection, `service.pid` or stream body was opened by the session.

---

## 2. Measurements

### 2.1 §3.1 — the branch and its three files (V3)

```
2026-10-29T07:45:39.408152032Z
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new tag]         pairbook-streams-1793242820 -> pairbook-streams-1793242820
exit=0
Preparing worktree (new branch 'tz-34-rewardbook-archive-timer')
branch 'tz-34-rewardbook-archive-timer' set up to track 'origin/main'.
HEAD is now at 0968707 Add files via upload
exit=0
0968707446d0bc549137b152d37be972e9f6781c
```

§0.1's script again, its argument `/root/tz34-work/wt` — the same three lines but for their directory:

```
2026-10-29T07:45:48.723806296Z
/root/tz34-work/wt/deploy/systemd/btc-rewardbook-archive.service 17 810 a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f
/root/tz34-work/wt/deploy/systemd/btc-rewardbook-archive.timer 13 428 bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f
/root/tz34-work/wt/research/tz34-rewardbook-archive-timer.py 1791 99388 1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72
exit=0
?? deploy/systemd/btc-rewardbook-archive.service
?? deploy/systemd/btc-rewardbook-archive.timer
?? research/tz34-rewardbook-archive-timer.py
```

```
2026-10-29T07:46:01.991003683Z
exit=0
6a615257277d3c94dafd4d39783499560a344648 root <root@vultr.guest> 2026-10-29 07:46:01 +0000
 deploy/systemd/btc-rewardbook-archive.service |   17 +
 deploy/systemd/btc-rewardbook-archive.timer   |   13 +
 research/tz34-rewardbook-archive-timer.py     | 1791 +++++++++++++++++++++++++
 3 files changed, 1821 insertions(+)
A	deploy/systemd/btc-rewardbook-archive.service
A	deploy/systemd/btc-rewardbook-archive.timer
A	research/tz34-rewardbook-archive-timer.py
```

The push, through the remote URL's own credential; its output passed through a `sed` that would mask a credential in a URL, which masked nothing (§6):

```
2026-10-29T07:46:11.359737269Z
remote: 
remote: Create a pull request for 'tz-34-rewardbook-archive-timer' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-34-rewardbook-archive-timer        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-34-rewardbook-archive-timer -> tz-34-rewardbook-archive-timer
branch 'tz-34-rewardbook-archive-timer' set up to track 'origin/tz-34-rewardbook-archive-timer'.
exit=0
```

```
2026-10-29T07:46:30.369410294Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/34
exit=0
```

### 2.2 §3.2 — the self-test (V4): **49 of 49**

```
2026-10-29T07:46:40.157556231Z
[2026-10-29T07:46:40Z]   ok  the calendar: 01:30:20 UTC, the next after now
[2026-10-29T07:46:40Z]   ok  this TZ's tags, which TZ-27's and TZ-28's rules do not cover, and theirs, which this TZ's does not
[2026-10-29T07:46:40Z]   ok  the asset names
[2026-10-29T07:46:40Z]   ok  the day, the decision at S - 6, 128M, 6h and 30min in bytes and seconds
[2026-10-29T07:46:40Z]   ok  G-NEXT's slots: decided from the first removal to 900 s after the last
[2026-10-29T07:46:40Z]   ok  a removal waits for the day's selection 5 s old and for a process with its start record 10 s old
[2026-10-29T07:46:40Z]   ok  G-NEXT: a slot without its slot.json or with an error record fails; the worst over the slots reads
[2026-10-29T07:46:40Z]   ok  G-TRIGGER: the run's own trigger where systemd set it, else the timer's last; 1,800 s after the mark less 2
[2026-10-29T07:46:40Z]   ok  G-STILL: the recorder and the reward book unchanged, the pair book unchanged or moved by its archive's chain
[2026-10-29T07:46:40Z]   ok  a stream file is read by the set, the upload and the removal alone, and written by no mode
[2026-10-29T07:46:40Z]   ok  no rewards file or selection is read; slot.json by final alone; runtime.jsonl by delete and final
[2026-10-29T07:46:40Z]   ok  a stream file removed only by the removal, only where the run names it; the store listed by three modes
[2026-10-29T07:46:40Z]   ok  nothing of the pair book's store, its archive's ledger read by still alone, no process in the set or the removal, the run writes under its state alone
[2026-10-29T07:46:40Z]   ok  btc-rewardbook-archive.service: 9 of its lines as this file runs them
[2026-10-29T07:46:40Z]   ok  btc-rewardbook-archive.timer: 5 of its lines as this file runs them
[2026-10-29T07:46:40Z]   ok  the reward book's 13 constants this file restates, equal to its text's
[2026-10-29T07:46:40Z]   ok  this file's sum of the store's streams equals the reward book's own, run from its text
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793235620, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793235620000000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] SLOT 1793230200 2026-10-28T23:30:00Z closed   stream files 1, 70001 bytes, taken 1
[2026-10-29T07:46:40Z] SLOT 1793231100 2026-10-28T23:45:00Z closed   stream files 2, 83333 bytes, taken 2
[2026-10-29T07:46:40Z] SLOT 1793232900 2026-10-29T00:15:00Z unclosed stream files 1, 40000 bytes, taken 0
[2026-10-29T07:46:40Z] SLOT 1793233800 2026-10-29T00:30:00Z closed   stream files 1, 44444 bytes, taken 1
[2026-10-29T07:46:40Z] S 1793145600-1793230200.0.stream.jsonl.gz 70001 6737d5b9ece6f1ce7d2693ff3e74a41b5da1e31ef5de2fe2b4c37055c48454e4
[2026-10-29T07:46:40Z] S 1793145600-1793231100.0.stream.jsonl.gz 50000 e61ca5a9b4b03c03a9917e965bcd6f4352777df90a9ab1856d3bc44991801734
[2026-10-29T07:46:40Z] S 1793145600-1793231100.1.stream.jsonl.gz 33333 3b82a1a587ff215bc4118b4b8efa7afda2732f0c9e2c20fba8d3dce642688814
[2026-10-29T07:46:40Z] S 1793232000-1793233800.0.stream.jsonl.gz 44444 0e303604951834519315950b8d021ee26a2c582940c68d8dc5a1e1ba0b284584
[2026-10-29T07:46:40Z] L {"assets_n": 4, "bytes_total": 197778, "closed": 3, "deferred": 0, "event": "set", "first_S": 1793230200, "last_S": 1793233800, "open": 2, "run": 1793235620, "sha256": "5a5ecb381db4126dc689818516c793ae807d1d0585f3ac8ffeccf2c75043df86", "slots_considered": 4, "streamless": 1, "tag": "rewardbook-streams-1793235620", "unclosed": 1, "wall_ns": 1793235620000000000}
[2026-10-29T07:46:40Z] L {"event": "hold", "phase": "upload", "run": 1793235620, "waited_s": 1000, "wall_ns": 1793236620000000000}
[2026-10-29T07:46:40Z] held 1000 s before upload: the pair book's archive ran
[2026-10-29T07:46:40Z] credential: the selftest's
[2026-10-29T07:46:40Z] created the Release on rewardbook-streams-1793235620, id 100
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793145600-1793230200.0.stream.jsonl.gz", "at": "2026-10-29T01:17:00Z", "bytes": 70001, "digest": "sha256:6737d5b9ece6f1ce7d2693ff3e74a41b5da1e31ef5de2fe2b4c37055c48454e4", "id": 101, "sha256": "6737d5b9ece6f1ce7d2693ff3e74a41b5da1e31ef5de2fe2b4c37055c48454e4"}
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793145600-1793231100.0.stream.jsonl.gz", "at": "2026-10-29T01:17:00Z", "bytes": 50000, "digest": "sha256:e61ca5a9b4b03c03a9917e965bcd6f4352777df90a9ab1856d3bc44991801734", "id": 102, "sha256": "e61ca5a9b4b03c03a9917e965bcd6f4352777df90a9ab1856d3bc44991801734"}
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793145600-1793231100.1.stream.jsonl.gz", "at": "2026-10-29T01:17:00Z", "bytes": 33333, "digest": "sha256:3b82a1a587ff215bc4118b4b8efa7afda2732f0c9e2c20fba8d3dce642688814", "id": 103, "sha256": "3b82a1a587ff215bc4118b4b8efa7afda2732f0c9e2c20fba8d3dce642688814"}
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793232000-1793233800.0.stream.jsonl.gz", "at": "2026-10-29T01:17:00Z", "bytes": 44444, "digest": "sha256:0e303604951834519315950b8d021ee26a2c582940c68d8dc5a1e1ba0b284584", "id": 104, "sha256": "0e303604951834519315950b8d021ee26a2c582940c68d8dc5a1e1ba0b284584"}
[2026-10-29T07:46:40Z] U {"action": "complete", "assets": 4, "at": "2026-10-29T01:17:00Z", "credential": "the selftest's", "held": 0, "release_id": 100, "sent": 4, "wall_ns": 1793236620000000000}
[2026-10-29T07:46:40Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 100, "run": 1793235620, "sent": 4, "wall_ns": 1793236620000000000}
[2026-10-29T07:46:40Z] D 1793145600-1793230200.0.stream.jsonl.gz equal bytes 70001 sha256 6737d5b9ece6f1ce7d2693ff3e74a41b5da1e31ef5de2fe2b4c37055c48454e4
[2026-10-29T07:46:40Z] D 1793145600-1793231100.0.stream.jsonl.gz equal bytes 50000 sha256 e61ca5a9b4b03c03a9917e965bcd6f4352777df90a9ab1856d3bc44991801734
[2026-10-29T07:46:40Z] D 1793145600-1793231100.1.stream.jsonl.gz equal bytes 33333 sha256 3b82a1a587ff215bc4118b4b8efa7afda2732f0c9e2c20fba8d3dce642688814
[2026-10-29T07:46:40Z] D 1793232000-1793233800.0.stream.jsonl.gz equal bytes 44444 sha256 0e303604951834519315950b8d021ee26a2c582940c68d8dc5a1e1ba0b284584
[2026-10-29T07:46:40Z] V 1793145600-1793230200.0.stream.jsonl.gz id 101 state uploaded api True bytes 70001 digest sha256:6737d5b9ece6f1ce7d2693ff3e74a41b5da1e31ef5de2fe2b4c37055c48454e4 url True download True
[2026-10-29T07:46:40Z] V 1793145600-1793231100.0.stream.jsonl.gz id 102 state uploaded api True bytes 50000 digest sha256:e61ca5a9b4b03c03a9917e965bcd6f4352777df90a9ab1856d3bc44991801734 url True download True
[2026-10-29T07:46:40Z] V 1793145600-1793231100.1.stream.jsonl.gz id 103 state uploaded api True bytes 33333 digest sha256:3b82a1a587ff215bc4118b4b8efa7afda2732f0c9e2c20fba8d3dce642688814 url True download True
[2026-10-29T07:46:40Z] V 1793232000-1793233800.0.stream.jsonl.gz id 104 state uploaded api True bytes 44444 digest sha256:0e303604951834519315950b8d021ee26a2c582940c68d8dc5a1e1ba0b284584 url True download True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-29T07:46:40Z] L {"assets_n": 4, "bytes_total": 197778, "event": "verify", "release_id": 100, "run": 1793235620, "verify_sha256": "80447d6dafcf7b4c1a1922fa3e5e3366e0f153cd05e2ff00844c0d7a71751a2e", "wall_ns": 1793236740500000000}
[2026-10-29T07:46:40Z] X 1793145600-1793230200.0.stream.jsonl.gz 70001 6737d5b9ece6f1ce7d2693ff3e74a41b5da1e31ef5de2fe2b4c37055c48454e4 removed at second 240
[2026-10-29T07:46:40Z] X 1793145600-1793231100.0.stream.jsonl.gz 50000 e61ca5a9b4b03c03a9917e965bcd6f4352777df90a9ab1856d3bc44991801734 removed at second 240
[2026-10-29T07:46:40Z] X 1793145600-1793231100.1.stream.jsonl.gz 33333 3b82a1a587ff215bc4118b4b8efa7afda2732f0c9e2c20fba8d3dce642688814 removed at second 240
[2026-10-29T07:46:40Z] X 1793232000-1793233800.0.stream.jsonl.gz 44444 0e303604951834519315950b8d021ee26a2c582940c68d8dc5a1e1ba0b284584 removed at second 240
[2026-10-29T07:46:40Z] G-DELETE every file of the set absent         True
[2026-10-29T07:46:40Z] G-DELETE each removal recorded                True
[2026-10-29T07:46:40Z] G-DELETE each slot keeps its slot.json        True
[2026-10-29T07:46:40Z] L {"already": 0, "event": "delete", "free_after": 9600000000, "free_before": 9600000000, "freed": 197778, "gone": 4, "quiet_s": 0, "removed": 4, "run": 1793235620, "slots_kept": 3, "wall_ns": 1793236740500000000}
[2026-10-29T07:46:40Z] at the set's rate the cap stops the streams in 1053.34 days, at 2029-09-16T09:34:56Z
[2026-10-29T07:46:40Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 48.63 days, at 2026-12-16T16:24:04Z
[2026-10-29T07:46:40Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 12.01 days, at 2026-11-10T01:28:48Z
[2026-10-29T07:46:40Z] L {"assets_n": 4, "bytes_total": 197778, "ended_outside": 0, "event": "complete", "free_bytes": 9600000000, "held_s": 1000, "peak_rss": 50810880, "rate_per_day": 3797337, "removals": 4, "requests": 13, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793235620, "started_outside": 0, "stops": [["the cap", 1884245696], ["the floor, base 43500000 bytes a day", 1797438244], ["the floor, base 187760570 bytes a day", 1794274128]], "store_stream_bytes": 95678, "wall_ns": 1793236740500000000}
[2026-10-29T07:46:40Z] COMPLETE: run 1793235620, 4 files, 197778 bytes, Release rewardbook-streams-1793235620
[2026-10-29T07:46:40Z]   ok  a run: every step recorded, in order, exit 0
[2026-10-29T07:46:40Z]   ok  the set: every stream file of a closed slot due 60 s before A, under this TZ's tag
[2026-10-29T07:46:40Z]   ok  the upload held while the pair book's archive ran
[2026-10-29T07:46:40Z]   ok  the Release holds the set's four files, byte for byte
[2026-10-29T07:46:40Z]   ok  the store: the set's files gone; slot.json, rewards, selections, the unclosed and the open streams kept
[2026-10-29T07:46:40Z]   ok  every request and every removal inside the idle stretch; reads with no token, every request TZ-27's
[2026-10-29T07:46:40Z]   ok  G-SET read on the store: the unclosed slot's stream left alone, nothing of a closed or unrecorded slot
[2026-10-29T07:46:40Z]   ok  G-SET fails on a stream of a slot it does not record, a slot.json not as recorded, two sets, a deferral
[2026-10-29T07:46:40Z]   ok  the store's streams after the run: the unclosed and the open slots' alone
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 540, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793237040, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793237040500000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] SLOT 1793232900 2026-10-29T00:15:00Z unclosed stream files 1, 40000 bytes, taken 0
[2026-10-29T07:46:40Z] SLOT 1793234700 2026-10-29T00:45:00Z closed   stream files 1, 55555 bytes, taken 1
[2026-10-29T07:46:40Z] SLOT 1793235600 2026-10-29T01:00:00Z unclosed stream files 1, 123 bytes, taken 0
[2026-10-29T07:46:40Z] S 1793232000-1793234700.0.stream.jsonl.gz 55555 affd4ee5a80f0b88e5b7b33b703ae037fcef12a9a7d3b83b30ea06c52dd801d0
[2026-10-29T07:46:40Z] L {"assets_n": 1, "bytes_total": 55555, "closed": 1, "deferred": 0, "event": "set", "first_S": 1793234700, "last_S": 1793234700, "open": 0, "run": 1793237040, "sha256": "cc024511546e164b4cd4c521b3a77b40862952d9ca467900c51680e356d475db", "slots_considered": 3, "streamless": 4, "tag": "rewardbook-streams-1793237040", "unclosed": 2, "wall_ns": 1793237040500000000}
[2026-10-29T07:46:40Z] credential: the selftest's
[2026-10-29T07:46:40Z] created the Release on rewardbook-streams-1793237040, id 105
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793232000-1793234700.0.stream.jsonl.gz", "at": "2026-10-29T01:24:00Z", "bytes": 55555, "digest": "sha256:affd4ee5a80f0b88e5b7b33b703ae037fcef12a9a7d3b83b30ea06c52dd801d0", "id": 106, "sha256": "affd4ee5a80f0b88e5b7b33b703ae037fcef12a9a7d3b83b30ea06c52dd801d0"}
[2026-10-29T07:46:40Z] U {"action": "complete", "assets": 1, "at": "2026-10-29T01:24:00Z", "credential": "the selftest's", "held": 0, "release_id": 105, "sent": 1, "wall_ns": 1793237040500000000}
[2026-10-29T07:46:40Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 105, "run": 1793237040, "sent": 1, "wall_ns": 1793237040500000000}
[2026-10-29T07:46:40Z] D 1793232000-1793234700.0.stream.jsonl.gz equal bytes 55555 sha256 affd4ee5a80f0b88e5b7b33b703ae037fcef12a9a7d3b83b30ea06c52dd801d0
[2026-10-29T07:46:40Z] V 1793232000-1793234700.0.stream.jsonl.gz id 106 state uploaded api True bytes 55555 digest sha256:affd4ee5a80f0b88e5b7b33b703ae037fcef12a9a7d3b83b30ea06c52dd801d0 url True download True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-29T07:46:40Z] L {"assets_n": 1, "bytes_total": 55555, "event": "verify", "release_id": 105, "run": 1793237040, "verify_sha256": "aa50566865b81cfbae0cee278533b541b6b574daa2c5d7fa922bc34eb98127d6", "wall_ns": 1793237415000000000}
[2026-10-29T07:46:40Z] X 1793232000-1793234700.0.stream.jsonl.gz 55555 affd4ee5a80f0b88e5b7b33b703ae037fcef12a9a7d3b83b30ea06c52dd801d0 removed at second 15
[2026-10-29T07:46:40Z] G-DELETE every file of the set absent         True
[2026-10-29T07:46:40Z] G-DELETE each removal recorded                True
[2026-10-29T07:46:40Z] G-DELETE each slot keeps its slot.json        True
[2026-10-29T07:46:40Z] L {"already": 0, "event": "delete", "free_after": 9600000000, "free_before": 9600000000, "freed": 55555, "gone": 1, "quiet_s": 0, "removed": 1, "run": 1793237040, "slots_kept": 1, "wall_ns": 1793237415000000000}
[2026-10-29T07:46:40Z] at the set's rate the cap stops the streams in 750.00 days, at 2028-11-17T01:30:13Z
[2026-10-29T07:46:40Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 47.10 days, at 2026-12-15T03:52:50Z
[2026-10-29T07:46:40Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 11.91 days, at 2026-11-09T23:22:31Z
[2026-10-29T07:46:40Z] L {"assets_n": 1, "bytes_total": 55555, "ended_outside": 0, "event": "complete", "free_bytes": 9600000000, "held_s": 0, "peak_rss": 50810880, "rate_per_day": 5333280, "removals": 1, "requests": 7, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793237040, "started_outside": 0, "stops": [["the cap", 1858037413], ["the floor, base 43500000 bytes a day", 1797306770], ["the floor, base 187760570 bytes a day", 1794266551]], "store_stream_bytes": 40123, "wall_ns": 1793237415000000000}
[2026-10-29T07:46:40Z] COMPLETE: run 1793237040, 1 files, 55555 bytes, Release rewardbook-streams-1793237040
[2026-10-29T07:46:40Z]   ok  the next run completes
[2026-10-29T07:46:40Z]   ok  the next run takes the slot due after the first run's A, and only it
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 25, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793237425, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793237425000000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] SLOT 1793232900 2026-10-29T00:15:00Z unclosed stream files 1, 40000 bytes, taken 0
[2026-10-29T07:46:40Z] SLOT 1793235600 2026-10-29T01:00:00Z unclosed stream files 1, 123 bytes, taken 0
[2026-10-29T07:46:40Z] L {"closed": 0, "deferred": 0, "event": "empty", "open": 0, "run": 1793237425, "slots_considered": 2, "streamless": 5, "unclosed": 2, "wall_ns": 1793237425000000000}
[2026-10-29T07:46:40Z] EMPTY: no stream file of a closed slot as of 1793237425
[2026-10-29T07:46:40Z]   ok  a run with no stream file of a closed slot records empty, exit 0
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 588, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793236188, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793236188000000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] SLOT 1793232900 2026-10-29T00:15:00Z closed   stream files 1, 1000 bytes, taken 1
[2026-10-29T07:46:40Z] S 1793232000-1793232900.0.stream.jsonl.gz 1000 c408c7a6ca160ca7652734150c16ba6790b1dc715728f8316062fa37017ef253
[2026-10-29T07:46:40Z] L {"assets_n": 1, "bytes_total": 1000, "closed": 1, "deferred": 0, "event": "set", "first_S": 1793232900, "last_S": 1793232900, "open": 0, "run": 1793236188, "sha256": "341ddeeed24b70a26c6e226b6ac08e766bf8b04b1160a334e3a6079bf21d4c37", "slots_considered": 1, "streamless": 0, "tag": "rewardbook-streams-1793236188", "unclosed": 0, "wall_ns": 1793236188000000000}
[2026-10-29T07:46:40Z] L {"count": 1, "event": "deferred", "phase": "upload", "reason": "AssertionError: UPLOAD REFUSED: no credential (selftest)", "run": 1793236188, "wall_ns": 1793236188000000000}
[2026-10-29T07:46:40Z] DEFERRED in upload, 1 of 3: AssertionError: UPLOAD REFUSED: no credential (selftest); the next run resumes this set
[2026-10-29T07:46:40Z]   ok  a refused credential: deferred, exit 75, nothing removed
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 588, "resumed": true, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793236188, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793322588000000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] credential: the selftest's
[2026-10-29T07:46:40Z] created the Release on rewardbook-streams-1793236188, id 107
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793232000-1793232900.0.stream.jsonl.gz", "at": "2026-10-30T01:15:15Z", "bytes": 1000, "digest": "sha256:c408c7a6ca160ca7652734150c16ba6790b1dc715728f8316062fa37017ef253", "id": 108, "sha256": "c408c7a6ca160ca7652734150c16ba6790b1dc715728f8316062fa37017ef253"}
[2026-10-29T07:46:40Z] U {"action": "complete", "assets": 1, "at": "2026-10-30T01:15:15Z", "credential": "the selftest's", "held": 0, "release_id": 107, "sent": 1, "wall_ns": 1793322915000000000}
[2026-10-29T07:46:40Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 107, "run": 1793236188, "sent": 1, "wall_ns": 1793322915000000000}
[2026-10-29T07:46:40Z] D 1793232000-1793232900.0.stream.jsonl.gz equal bytes 1000 sha256 c408c7a6ca160ca7652734150c16ba6790b1dc715728f8316062fa37017ef253
[2026-10-29T07:46:40Z] V 1793232000-1793232900.0.stream.jsonl.gz id 108 state uploaded api True bytes 1000 digest sha256:c408c7a6ca160ca7652734150c16ba6790b1dc715728f8316062fa37017ef253 url True download True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-29T07:46:40Z] L {"assets_n": 1, "bytes_total": 1000, "event": "verify", "release_id": 107, "run": 1793236188, "verify_sha256": "a60987fab5dafdbc706bcae62fb9e4ed3163ec6f4f9007f958d6b8e34edda170", "wall_ns": 1793323035500000000}
[2026-10-29T07:46:40Z] X 1793232000-1793232900.0.stream.jsonl.gz 1000 c408c7a6ca160ca7652734150c16ba6790b1dc715728f8316062fa37017ef253 removed at second 135
[2026-10-29T07:46:40Z] G-DELETE every file of the set absent         True
[2026-10-29T07:46:40Z] G-DELETE each removal recorded                True
[2026-10-29T07:46:40Z] G-DELETE each slot keeps its slot.json        True
[2026-10-29T07:46:40Z] L {"already": 0, "event": "delete", "free_after": 9600000000, "free_before": 9600000000, "freed": 1000, "gone": 1, "quiet_s": 0, "removed": 1, "run": 1793236188, "slots_kept": 1, "wall_ns": 1793323035500000000}
[2026-10-29T07:46:40Z] at the set's rate the cap stops the streams in 41666.67 days, at 2140-11-27T17:17:15Z
[2026-10-29T07:46:40Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 52.76 days, at 2026-12-21T19:27:31Z
[2026-10-29T07:46:40Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 12.24 days, at 2026-11-11T07:07:43Z
[2026-10-29T07:46:40Z] L {"assets_n": 1, "bytes_total": 1000, "ended_outside": 0, "event": "complete", "free_bytes": 9600000000, "held_s": 0, "peak_rss": 50810880, "rate_per_day": 96000, "removals": 1, "requests": 7, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793236188, "started_outside": 0, "stops": [["the cap", 5393323035], ["the floor, base 43500000 bytes a day", 1797881251], ["the floor, base 187760570 bytes a day", 1794380863]], "store_stream_bytes": 0, "wall_ns": 1793323035500000000}
[2026-10-29T07:46:40Z] COMPLETE: run 1793236188, 1 files, 1000 bytes, Release rewardbook-streams-1793236188
[2026-10-29T07:46:40Z]   ok  the next run resumes the deferred set and completes it
[2026-10-29T07:46:40Z]   ok  a request due at second 588 waits for the next idle stretch
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793491220, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793491220000000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] SLOT 1793232900 2026-10-29T00:15:00Z closed   stream files 1, 1000 bytes, taken 1
[2026-10-29T07:46:40Z] S 1793232000-1793232900.0.stream.jsonl.gz 1000 c408c7a6ca160ca7652734150c16ba6790b1dc715728f8316062fa37017ef253
[2026-10-29T07:46:40Z] L {"assets_n": 1, "bytes_total": 1000, "closed": 1, "deferred": 0, "event": "set", "first_S": 1793232900, "last_S": 1793232900, "open": 0, "run": 1793491220, "sha256": "32614ad131a6ec63c13550e1217dd01845be6b6c5211e8d3f6c56c62a94f6161", "slots_considered": 1, "streamless": 0, "tag": "rewardbook-streams-1793491220", "unclosed": 0, "wall_ns": 1793491220000000000}
[2026-10-29T07:46:40Z] L {"count": 1, "event": "deferred", "phase": "upload", "reason": "AssertionError: UPLOAD REFUSED: no credential (selftest)", "run": 1793491220, "wall_ns": 1793491220000000000}
[2026-10-29T07:46:40Z] DEFERRED in upload, 1 of 3: AssertionError: UPLOAD REFUSED: no credential (selftest); the next run resumes this set
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": true, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793491220, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793491220000000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] L {"count": 2, "event": "deferred", "phase": "upload", "reason": "AssertionError: UPLOAD REFUSED: no credential (selftest)", "run": 1793491220, "wall_ns": 1793491220000000000}
[2026-10-29T07:46:40Z] DEFERRED in upload, 2 of 3: AssertionError: UPLOAD REFUSED: no credential (selftest); the next run resumes this set
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": true, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793491220, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793491220000000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] L {"event": "halt", "phase": "upload", "reason": "deferral 3 of 3: AssertionError: UPLOAD REFUSED: no credential (selftest)", "run": 1793491220, "wall_ns": 1793491220000000000}
[2026-10-29T07:46:40Z] L {"event": "timer-disabled", "exit": 0, "run": 1793491220, "wall_ns": 1793491220000000000}
[2026-10-29T07:46:40Z] HALTED in upload: deferral 3 of 3: AssertionError: UPLOAD REFUSED: no credential (selftest); the timer disabled, exit 0
[2026-10-29T07:46:40Z]   ok  the third deferral of one set halts, and the run disables its timer
[2026-10-29T07:46:40Z] HALTED since run 1793491220, upload: deferral 3 of 3: AssertionError: UPLOAD REFUSED: no credential (selftest); nothing done
[2026-10-29T07:46:40Z] L {"event": "refused", "exit": 0, "run": 1793491220, "wall_ns": 1793491220000000000}
[2026-10-29T07:46:40Z]   ok  a halted archive refuses the next run, and removes nothing
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 80, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793491280, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793491280000000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] SLOT 1793232900 2026-10-29T00:15:00Z closed   stream files 1, 1000 bytes, taken 1
[2026-10-29T07:46:40Z] S 1793232000-1793232900.0.stream.jsonl.gz 1000 c408c7a6ca160ca7652734150c16ba6790b1dc715728f8316062fa37017ef253
[2026-10-29T07:46:40Z] L {"assets_n": 1, "bytes_total": 1000, "closed": 1, "deferred": 0, "event": "set", "first_S": 1793232900, "last_S": 1793232900, "open": 0, "run": 1793491280, "sha256": "fa7bf556e80a884747f04266ca7dd036f159dd94d00c5ff5175505699eb6e8db", "slots_considered": 1, "streamless": 0, "tag": "rewardbook-streams-1793491280", "unclosed": 0, "wall_ns": 1793491280000000000}
[2026-10-29T07:46:40Z] credential: the selftest's
[2026-10-29T07:46:40Z] created the Release on rewardbook-streams-1793491280, id 109
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793232000-1793232900.0.stream.jsonl.gz", "at": "2026-11-01T00:01:20Z", "bytes": 1000, "digest": "sha256:c408c7a6ca160ca7652734150c16ba6790b1dc715728f8316062fa37017ef253", "id": 110, "sha256": "c408c7a6ca160ca7652734150c16ba6790b1dc715728f8316062fa37017ef253"}
[2026-10-29T07:46:40Z] U {"action": "complete", "assets": 1, "at": "2026-11-01T00:01:20Z", "credential": "the selftest's", "held": 0, "release_id": 109, "sent": 1, "wall_ns": 1793491280000000000}
[2026-10-29T07:46:40Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 109, "run": 1793491280, "sent": 1, "wall_ns": 1793491280000000000}
[2026-10-29T07:46:40Z] D 1793232000-1793232900.0.stream.jsonl.gz equal bytes 1000 sha256 c408c7a6ca160ca7652734150c16ba6790b1dc715728f8316062fa37017ef253
[2026-10-29T07:46:40Z] V 1793232000-1793232900.0.stream.jsonl.gz id 110 state uploaded api True bytes 1000 digest sha256:c408c7a6ca160ca7652734150c16ba6790b1dc715728f8316062fa37017ef253 url True download True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-29T07:46:40Z] L {"assets_n": 1, "bytes_total": 1000, "event": "verify", "release_id": 109, "run": 1793491280, "verify_sha256": "3d7896594bd9e8e895c13ff863796ddefa95947b365dc7e06b05eefba3a39c3b", "wall_ns": 1793491400500000000}
[2026-10-29T07:46:40Z] X 1793232000-1793232900.0.stream.jsonl.gz 1000 c408c7a6ca160ca7652734150c16ba6790b1dc715728f8316062fa37017ef253 removed at second 200
[2026-10-29T07:46:40Z] G-DELETE every file of the set absent         True
[2026-10-29T07:46:40Z] G-DELETE each removal recorded                True
[2026-10-29T07:46:40Z] G-DELETE each slot keeps its slot.json        True
[2026-10-29T07:46:40Z] L {"already": 0, "event": "delete", "free_after": 9600000000, "free_before": 9600000000, "freed": 1000, "gone": 1, "quiet_s": 0, "removed": 1, "run": 1793491280, "slots_kept": 1, "wall_ns": 1793491400500000000}
[2026-10-29T07:46:40Z] at the set's rate the cap stops the streams in 41666.67 days, at 2140-11-29T16:03:20Z
[2026-10-29T07:46:40Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 52.76 days, at 2026-12-23T18:13:36Z
[2026-10-29T07:46:40Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 12.24 days, at 2026-11-13T05:53:48Z
[2026-10-29T07:46:40Z] L {"assets_n": 1, "bytes_total": 1000, "ended_outside": 0, "event": "complete", "free_bytes": 9600000000, "held_s": 0, "peak_rss": 50810880, "rate_per_day": 96000, "removals": 1, "requests": 7, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793491280, "started_outside": 0, "stops": [["the cap", 5393491400], ["the floor, base 43500000 bytes a day", 1798049616], ["the floor, base 187760570 bytes a day", 1794549228]], "store_stream_bytes": 0, "wall_ns": 1793491400500000000}
[2026-10-29T07:46:40Z] COMPLETE: run 1793491280, 1 files, 1000 bytes, Release rewardbook-streams-1793491280
[2026-10-29T07:46:40Z]   ok  after a clear the next run takes a new set
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793664020, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793664020000000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] SLOT 1793232900 2026-10-29T00:15:00Z closed   stream files 2, 11000 bytes, taken 2
[2026-10-29T07:46:40Z] S 1793232000-1793232900.0.stream.jsonl.gz 5000 ba11bc38606d991083f54794a92cd57ade965bc13bf7ee349df4c6a5b2f7bfc0
[2026-10-29T07:46:40Z] S 1793232000-1793232900.1.stream.jsonl.gz 6000 d3360628f1ce661f9a733f28c2ffdd920c3bcb2a5fe55094d67c4e34584d4e5c
[2026-10-29T07:46:40Z] L {"assets_n": 2, "bytes_total": 11000, "closed": 1, "deferred": 0, "event": "set", "first_S": 1793232900, "last_S": 1793232900, "open": 0, "run": 1793664020, "sha256": "c059993a3a6f50996133e1e35546c75fca9f251b259e1a0ad3453b78f6326ba3", "slots_considered": 1, "streamless": 0, "tag": "rewardbook-streams-1793664020", "unclosed": 0, "wall_ns": 1793664020000000000}
[2026-10-29T07:46:40Z] credential: the selftest's
[2026-10-29T07:46:40Z] created the Release on rewardbook-streams-1793664020, id 111
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793232000-1793232900.0.stream.jsonl.gz", "at": "2026-11-03T00:00:20Z", "bytes": 5000, "digest": "sha256:ba11bc38606d991083f54794a92cd57ade965bc13bf7ee349df4c6a5b2f7bfc0", "id": 112, "sha256": "ba11bc38606d991083f54794a92cd57ade965bc13bf7ee349df4c6a5b2f7bfc0"}
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793232000-1793232900.1.stream.jsonl.gz", "at": "2026-11-03T00:00:20Z", "bytes": 6000, "digest": "sha256:d3360628f1ce661f9a733f28c2ffdd920c3bcb2a5fe55094d67c4e34584d4e5c", "id": 113, "sha256": "d3360628f1ce661f9a733f28c2ffdd920c3bcb2a5fe55094d67c4e34584d4e5c"}
[2026-10-29T07:46:40Z] U {"action": "complete", "assets": 2, "at": "2026-11-03T00:00:20Z", "credential": "the selftest's", "held": 0, "release_id": 111, "sent": 2, "wall_ns": 1793664020000000000}
[2026-10-29T07:46:40Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 111, "run": 1793664020, "sent": 2, "wall_ns": 1793664020000000000}
[2026-10-29T07:46:40Z] D 1793232000-1793232900.0.stream.jsonl.gz equal bytes 5000 sha256 ba11bc38606d991083f54794a92cd57ade965bc13bf7ee349df4c6a5b2f7bfc0
[2026-10-29T07:46:40Z] D 1793232000-1793232900.1.stream.jsonl.gz DIFFERS bytes 6000 sha256 363226d0ca90857c0aa9ccccd008129eb62b52306135811bc3b088d91c2ffc0e
[2026-10-29T07:46:40Z] V 1793232000-1793232900.0.stream.jsonl.gz id 112 state uploaded api True bytes 5000 digest sha256:ba11bc38606d991083f54794a92cd57ade965bc13bf7ee349df4c6a5b2f7bfc0 url True download True
[2026-10-29T07:46:40Z] V 1793232000-1793232900.1.stream.jsonl.gz id 113 state uploaded api True bytes 6000 digest sha256:d3360628f1ce661f9a733f28c2ffdd920c3bcb2a5fe55094d67c4e34584d4e5c url True download False
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           False
[2026-10-29T07:46:40Z] L {"count": 1, "event": "deferred", "phase": "verify", "reason": "AssertionError: VERIFY FAIL: [\"every download the set's bytes and SHA-256\"]; missing []; beyond []", "run": 1793664020, "wall_ns": 1793664140500000000}
[2026-10-29T07:46:40Z] DEFERRED in verify, 1 of 3: AssertionError: VERIFY FAIL: ["every download the set's bytes and SHA-256"]; missing []; beyond []; the next run resumes this set
[2026-10-29T07:46:40Z]   ok  a flipped bit in one asset: VERIFY FAIL, deferred, nothing removed
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 140, "resumed": true, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793664020, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793664140500000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] credential: the selftest's
[2026-10-29T07:46:40Z] U {"action": "held", "asset": "1793232000-1793232900.0.stream.jsonl.gz", "at": "2026-11-03T00:02:20Z", "id": 112}
[2026-10-29T07:46:40Z] U {"action": "held", "asset": "1793232000-1793232900.1.stream.jsonl.gz", "at": "2026-11-03T00:02:20Z", "id": 113}
[2026-10-29T07:46:40Z] U {"action": "complete", "assets": 2, "at": "2026-11-03T00:02:20Z", "credential": "the selftest's", "held": 2, "release_id": 111, "sent": 0, "wall_ns": 1793664140500000000}
[2026-10-29T07:46:40Z] L {"created": false, "credential": "the selftest's", "event": "upload", "held": 2, "release_id": 111, "run": 1793664020, "sent": 0, "wall_ns": 1793664140500000000}
[2026-10-29T07:46:40Z] D 1793232000-1793232900.0.stream.jsonl.gz equal bytes 5000 sha256 ba11bc38606d991083f54794a92cd57ade965bc13bf7ee349df4c6a5b2f7bfc0
[2026-10-29T07:46:40Z] D 1793232000-1793232900.1.stream.jsonl.gz equal bytes 6000 sha256 d3360628f1ce661f9a733f28c2ffdd920c3bcb2a5fe55094d67c4e34584d4e5c
[2026-10-29T07:46:40Z] V 1793232000-1793232900.0.stream.jsonl.gz id 112 state uploaded api True bytes 5000 digest sha256:ba11bc38606d991083f54794a92cd57ade965bc13bf7ee349df4c6a5b2f7bfc0 url True download True
[2026-10-29T07:46:40Z] V 1793232000-1793232900.1.stream.jsonl.gz id 113 state uploaded api True bytes 6000 digest sha256:d3360628f1ce661f9a733f28c2ffdd920c3bcb2a5fe55094d67c4e34584d4e5c url True download True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-29T07:46:40Z] L {"assets_n": 2, "bytes_total": 11000, "event": "verify", "release_id": 111, "run": 1793664020, "verify_sha256": "ae554e7de7b78563ad4b77ec3f19a3c4ddbc303543289d00ef24fd062f9d808c", "wall_ns": 1793664261000000000}
[2026-10-29T07:46:40Z] X 1793232000-1793232900.0.stream.jsonl.gz 5000 ba11bc38606d991083f54794a92cd57ade965bc13bf7ee349df4c6a5b2f7bfc0 removed at second 261
[2026-10-29T07:46:40Z] X 1793232000-1793232900.1.stream.jsonl.gz 6000 d3360628f1ce661f9a733f28c2ffdd920c3bcb2a5fe55094d67c4e34584d4e5c removed at second 261
[2026-10-29T07:46:40Z] G-DELETE every file of the set absent         True
[2026-10-29T07:46:40Z] G-DELETE each removal recorded                True
[2026-10-29T07:46:40Z] G-DELETE each slot keeps its slot.json        True
[2026-10-29T07:46:40Z] L {"already": 0, "event": "delete", "free_after": 9600000000, "free_before": 9600000000, "freed": 11000, "gone": 2, "quiet_s": 0, "removed": 2, "run": 1793664020, "slots_kept": 1, "wall_ns": 1793664261000000000}
[2026-10-29T07:46:40Z] at the set's rate the cap stops the streams in 3787.88 days, at 2037-03-17T21:09:48Z
[2026-10-29T07:46:40Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 51.62 days, at 2026-12-24T14:57:46Z
[2026-10-29T07:46:40Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 12.18 days, at 2026-11-15T04:25:11Z
[2026-10-29T07:46:40Z] L {"assets_n": 2, "bytes_total": 11000, "ended_outside": 0, "event": "complete", "free_bytes": 9600000000, "held_s": 0, "peak_rss": 50810880, "rate_per_day": 1056000, "removals": 2, "requests": 15, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793664020, "started_outside": 0, "stops": [["the cap", 2120936988], ["the floor, base 43500000 bytes a day", 1798124266], ["the floor, base 187760570 bytes a day", 1794716711]], "store_stream_bytes": 0, "wall_ns": 1793664261000000000}
[2026-10-29T07:46:40Z] COMPLETE: run 1793664020, 2 files, 11000 bytes, Release rewardbook-streams-1793664020
[2026-10-29T07:46:40Z]   ok  the asset mended, the next run verifies and completes
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793322020, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793322020000000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] SLOT 1793319300 2026-10-30T00:15:00Z closed   stream files 1, 7000 bytes, taken 1
[2026-10-29T07:46:40Z] S 1793318400-1793319300.0.stream.jsonl.gz 7000 6952ddf8aa966329ca26691fbcaf6803ed602f799867c8b5b087651ce2385847
[2026-10-29T07:46:40Z] L {"assets_n": 1, "bytes_total": 7000, "closed": 1, "deferred": 0, "event": "set", "first_S": 1793319300, "last_S": 1793319300, "open": 0, "run": 1793322020, "sha256": "941dbd9d15bc280d274a079a725865c0cc68c02e675255134027c366ecbc6b1b", "slots_considered": 1, "streamless": 0, "tag": "rewardbook-streams-1793322020", "unclosed": 0, "wall_ns": 1793322020000000000}
[2026-10-29T07:46:40Z] credential: the selftest's
[2026-10-29T07:46:40Z] created the Release on rewardbook-streams-1793322020, id 114
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793318400-1793319300.0.stream.jsonl.gz", "at": "2026-10-30T01:00:20Z", "bytes": 7000, "digest": "sha256:6952ddf8aa966329ca26691fbcaf6803ed602f799867c8b5b087651ce2385847", "id": 115, "sha256": "6952ddf8aa966329ca26691fbcaf6803ed602f799867c8b5b087651ce2385847"}
[2026-10-29T07:46:40Z] U {"action": "complete", "assets": 1, "at": "2026-10-30T01:00:20Z", "credential": "the selftest's", "held": 0, "release_id": 114, "sent": 1, "wall_ns": 1793322020000000000}
[2026-10-29T07:46:40Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 114, "run": 1793322020, "sent": 1, "wall_ns": 1793322020000000000}
[2026-10-29T07:46:40Z] D 1793318400-1793319300.0.stream.jsonl.gz equal bytes 7000 sha256 6952ddf8aa966329ca26691fbcaf6803ed602f799867c8b5b087651ce2385847
[2026-10-29T07:46:40Z] V 1793318400-1793319300.0.stream.jsonl.gz id 115 state uploaded api True bytes 7000 digest sha256:6952ddf8aa966329ca26691fbcaf6803ed602f799867c8b5b087651ce2385847 url True download True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-29T07:46:40Z] L {"assets_n": 1, "bytes_total": 7000, "event": "verify", "release_id": 114, "run": 1793322020, "verify_sha256": "a05bd0241fd685e24e2fa68e19617ead6617dadb02bb95537483af86395c9503", "wall_ns": 1793322140500000000}
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793318400 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793318400 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793318400 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793318400 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793318400 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793318400 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793318400 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793318400 not recorded 5 s before
[2026-10-29T07:46:40Z] X 1793318400-1793319300.0.stream.jsonl.gz 7000 6952ddf8aa966329ca26691fbcaf6803ed602f799867c8b5b087651ce2385847 removed at second 15
[2026-10-29T07:46:40Z] G-DELETE every file of the set absent         True
[2026-10-29T07:46:40Z] G-DELETE each removal recorded                True
[2026-10-29T07:46:40Z] G-DELETE each slot keeps its slot.json        True
[2026-10-29T07:46:40Z] L {"already": 0, "event": "delete", "free_after": 9600000000, "free_before": 9600000000, "freed": 7000, "gone": 1, "quiet_s": 445, "removed": 1, "run": 1793322020, "slots_kept": 1, "wall_ns": 1793322915000000000}
[2026-10-29T07:46:40Z] at the set's rate the cap stops the streams in 5952.38 days, at 2043-02-15T10:23:49Z
[2026-10-29T07:46:40Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 52.07 days, at 2026-12-21T02:54:52Z
[2026-10-29T07:46:40Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 12.21 days, at 2026-11-11T06:11:49Z
[2026-10-29T07:46:40Z] L {"assets_n": 1, "bytes_total": 7000, "ended_outside": 0, "event": "complete", "free_bytes": 9600000000, "held_s": 0, "peak_rss": 50810880, "rate_per_day": 672000, "removals": 1, "requests": 7, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793322020, "started_outside": 0, "stops": [["the cap", 2307608629], ["the floor, base 43500000 bytes a day", 1797821692], ["the floor, base 187760570 bytes a day", 1794377509]], "store_stream_bytes": 0, "wall_ns": 1793322915000000000}
[2026-10-29T07:46:40Z] COMPLETE: run 1793322020, 1 files, 7000 bytes, Release rewardbook-streams-1793322020
[2026-10-29T07:46:40Z]   ok  the removal waited for the day's selection and completed
[2026-10-29T07:46:40Z]   ok  the first removal 5 s or more after the selection's record, inside the idle stretch
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793408420, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793408420000000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] SLOT 1793405700 2026-10-31T00:15:00Z closed   stream files 2, 15000 bytes, taken 2
[2026-10-29T07:46:40Z] S 1793404800-1793405700.0.stream.jsonl.gz 7000 5b21de44806fb0ad6235ee3669afc58732445d21623ad61a21ece21ec10cc3e3
[2026-10-29T07:46:40Z] S 1793404800-1793405700.1.stream.jsonl.gz 8000 d21fb05ef58cd5255bf606d0f8a0e131beee77142e67a2d5ece5745b8e6c704e
[2026-10-29T07:46:40Z] L {"assets_n": 2, "bytes_total": 15000, "closed": 1, "deferred": 0, "event": "set", "first_S": 1793405700, "last_S": 1793405700, "open": 0, "run": 1793408420, "sha256": "a6c8161f58add3b2757cff410be606a6c6998c977713e8e08917a3833ef56043", "slots_considered": 1, "streamless": 0, "tag": "rewardbook-streams-1793408420", "unclosed": 0, "wall_ns": 1793408420000000000}
[2026-10-29T07:46:40Z] credential: the selftest's
[2026-10-29T07:46:40Z] created the Release on rewardbook-streams-1793408420, id 116
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793404800-1793405700.0.stream.jsonl.gz", "at": "2026-10-31T01:00:20Z", "bytes": 7000, "digest": "sha256:5b21de44806fb0ad6235ee3669afc58732445d21623ad61a21ece21ec10cc3e3", "id": 117, "sha256": "5b21de44806fb0ad6235ee3669afc58732445d21623ad61a21ece21ec10cc3e3"}
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793404800-1793405700.1.stream.jsonl.gz", "at": "2026-10-31T01:00:20Z", "bytes": 8000, "digest": "sha256:d21fb05ef58cd5255bf606d0f8a0e131beee77142e67a2d5ece5745b8e6c704e", "id": 118, "sha256": "d21fb05ef58cd5255bf606d0f8a0e131beee77142e67a2d5ece5745b8e6c704e"}
[2026-10-29T07:46:40Z] U {"action": "complete", "assets": 2, "at": "2026-10-31T01:00:20Z", "credential": "the selftest's", "held": 0, "release_id": 116, "sent": 2, "wall_ns": 1793408420000000000}
[2026-10-29T07:46:40Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 116, "run": 1793408420, "sent": 2, "wall_ns": 1793408420000000000}
[2026-10-29T07:46:40Z] D 1793404800-1793405700.0.stream.jsonl.gz equal bytes 7000 sha256 5b21de44806fb0ad6235ee3669afc58732445d21623ad61a21ece21ec10cc3e3
[2026-10-29T07:46:40Z] D 1793404800-1793405700.1.stream.jsonl.gz equal bytes 8000 sha256 d21fb05ef58cd5255bf606d0f8a0e131beee77142e67a2d5ece5745b8e6c704e
[2026-10-29T07:46:40Z] V 1793404800-1793405700.0.stream.jsonl.gz id 117 state uploaded api True bytes 7000 digest sha256:5b21de44806fb0ad6235ee3669afc58732445d21623ad61a21ece21ec10cc3e3 url True download True
[2026-10-29T07:46:40Z] V 1793404800-1793405700.1.stream.jsonl.gz id 118 state uploaded api True bytes 8000 digest sha256:d21fb05ef58cd5255bf606d0f8a0e131beee77142e67a2d5ece5745b8e6c704e url True download True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-29T07:46:40Z] L {"assets_n": 2, "bytes_total": 15000, "event": "verify", "release_id": 116, "run": 1793408420, "verify_sha256": "368374a4293ccc63554ddc9b8acce41a540abe8e3840ef9f764cef33b83cae56", "wall_ns": 1793408540500000000}
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] removal waits: the selection of day 1793404800 not recorded 5 s before
[2026-10-29T07:46:40Z] L {"count": 1, "event": "deferred", "phase": "delete", "reason": "QuietTimeout: the removals waited 1800 s: the selection of day 1793404800 not recorded 5 s before", "run": 1793408420, "wall_ns": 1793411330000000000}
[2026-10-29T07:46:40Z] DEFERRED in delete, 1 of 3: QuietTimeout: the removals waited 1800 s: the selection of day 1793404800 not recorded 5 s before; the next run resumes this set
[2026-10-29T07:46:40Z]   ok  the selection never recorded: the run defers in its removal, nothing removed
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 230, "resumed": true, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793408420, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793414930000000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] credential: the selftest's
[2026-10-29T07:46:40Z] U {"action": "held", "asset": "1793404800-1793405700.0.stream.jsonl.gz", "at": "2026-10-31T02:48:50Z", "id": 117}
[2026-10-29T07:46:40Z] U {"action": "held", "asset": "1793404800-1793405700.1.stream.jsonl.gz", "at": "2026-10-31T02:48:50Z", "id": 118}
[2026-10-29T07:46:40Z] U {"action": "complete", "assets": 2, "at": "2026-10-31T02:48:50Z", "credential": "the selftest's", "held": 2, "release_id": 116, "sent": 0, "wall_ns": 1793414930000000000}
[2026-10-29T07:46:40Z] L {"created": false, "credential": "the selftest's", "event": "upload", "held": 2, "release_id": 116, "run": 1793408420, "sent": 0, "wall_ns": 1793414930000000000}
[2026-10-29T07:46:40Z] D 1793404800-1793405700.0.stream.jsonl.gz equal bytes 7000 sha256 5b21de44806fb0ad6235ee3669afc58732445d21623ad61a21ece21ec10cc3e3
[2026-10-29T07:46:40Z] D 1793404800-1793405700.1.stream.jsonl.gz equal bytes 8000 sha256 d21fb05ef58cd5255bf606d0f8a0e131beee77142e67a2d5ece5745b8e6c704e
[2026-10-29T07:46:40Z] V 1793404800-1793405700.0.stream.jsonl.gz id 117 state uploaded api True bytes 7000 digest sha256:5b21de44806fb0ad6235ee3669afc58732445d21623ad61a21ece21ec10cc3e3 url True download True
[2026-10-29T07:46:40Z] V 1793404800-1793405700.1.stream.jsonl.gz id 118 state uploaded api True bytes 8000 digest sha256:d21fb05ef58cd5255bf606d0f8a0e131beee77142e67a2d5ece5745b8e6c704e url True download True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-29T07:46:40Z] L {"assets_n": 2, "bytes_total": 15000, "event": "verify", "release_id": 116, "run": 1793408420, "verify_sha256": "368374a4293ccc63554ddc9b8acce41a540abe8e3840ef9f764cef33b83cae56", "wall_ns": 1793415050500000000}
[2026-10-29T07:46:40Z] X 1793404800-1793405700.0.stream.jsonl.gz 7000 5b21de44806fb0ad6235ee3669afc58732445d21623ad61a21ece21ec10cc3e3 removed at second 350
[2026-10-29T07:46:40Z] X 1793404800-1793405700.1.stream.jsonl.gz 8000 d21fb05ef58cd5255bf606d0f8a0e131beee77142e67a2d5ece5745b8e6c704e removed at second 350
[2026-10-29T07:46:40Z] G-DELETE every file of the set absent         True
[2026-10-29T07:46:40Z] G-DELETE each removal recorded                True
[2026-10-29T07:46:40Z] G-DELETE each slot keeps its slot.json        True
[2026-10-29T07:46:40Z] L {"already": 0, "event": "delete", "free_after": 9600000000, "free_before": 9600000000, "freed": 15000, "gone": 2, "quiet_s": 0, "removed": 2, "run": 1793408420, "slots_kept": 1, "wall_ns": 1793415050500000000}
[2026-10-29T07:46:40Z] at the set's rate the cap stops the streams in 2777.78 days, at 2034-06-08T21:30:50Z
[2026-10-29T07:46:40Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 51.18 days, at 2026-12-21T07:09:05Z
[2026-10-29T07:46:40Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 12.16 days, at 2026-11-12T06:36:03Z
[2026-10-29T07:46:40Z] L {"assets_n": 2, "bytes_total": 15000, "ended_outside": 0, "event": "complete", "free_bytes": 9600000000, "held_s": 0, "peak_rss": 50810880, "rate_per_day": 1440000, "removals": 2, "requests": 15, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793408420, "started_outside": 0, "stops": [["the cap", 2033415050], ["the floor, base 43500000 bytes a day", 1797836945], ["the floor, base 187760570 bytes a day", 1794465363]], "store_stream_bytes": 0, "wall_ns": 1793415050500000000}
[2026-10-29T07:46:40Z] COMPLETE: run 1793408420, 2 files, 15000 bytes, Release rewardbook-streams-1793408420
[2026-10-29T07:46:40Z]   ok  the next run resumes the set - its uploads held, verified again - and completes the removal
[2026-10-29T07:46:40Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793494820, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793494820000000000}
[2026-10-29T07:46:40Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:40Z] SLOT 1793492100 2026-11-01T00:15:00Z closed   stream files 3, 6000 bytes, taken 3
[2026-10-29T07:46:40Z] S 1793491200-1793492100.0.stream.jsonl.gz 1000 b040c6925491fa9a68becb24a08bafdcd78029694e6a845383f280c3c3d2f7d5
[2026-10-29T07:46:40Z] S 1793491200-1793492100.1.stream.jsonl.gz 2000 98a5821a4250979f3610470ce39f507e65387ad9966a7e6dfc172935500be563
[2026-10-29T07:46:40Z] S 1793491200-1793492100.2.stream.jsonl.gz 3000 b8a1dce93312e23bab792681153ff2c4e761d096bf066d1e170752666f9a8aa2
[2026-10-29T07:46:40Z] L {"assets_n": 3, "bytes_total": 6000, "closed": 1, "deferred": 0, "event": "set", "first_S": 1793492100, "last_S": 1793492100, "open": 0, "run": 1793494820, "sha256": "6ca990d9365d8e2574b612e10fd05efa98ec539a6a6673722ba96c8cf433e0f9", "slots_considered": 1, "streamless": 0, "tag": "rewardbook-streams-1793494820", "unclosed": 0, "wall_ns": 1793494820000000000}
[2026-10-29T07:46:40Z] credential: the selftest's
[2026-10-29T07:46:40Z] created the Release on rewardbook-streams-1793494820, id 119
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793491200-1793492100.0.stream.jsonl.gz", "at": "2026-11-01T01:00:20Z", "bytes": 1000, "digest": "sha256:b040c6925491fa9a68becb24a08bafdcd78029694e6a845383f280c3c3d2f7d5", "id": 120, "sha256": "b040c6925491fa9a68becb24a08bafdcd78029694e6a845383f280c3c3d2f7d5"}
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793491200-1793492100.1.stream.jsonl.gz", "at": "2026-11-01T01:00:20Z", "bytes": 2000, "digest": "sha256:98a5821a4250979f3610470ce39f507e65387ad9966a7e6dfc172935500be563", "id": 121, "sha256": "98a5821a4250979f3610470ce39f507e65387ad9966a7e6dfc172935500be563"}
[2026-10-29T07:46:40Z] U {"action": "uploaded", "asset": "1793491200-1793492100.2.stream.jsonl.gz", "at": "2026-11-01T01:00:20Z", "bytes": 3000, "digest": "sha256:b8a1dce93312e23bab792681153ff2c4e761d096bf066d1e170752666f9a8aa2", "id": 122, "sha256": "b8a1dce93312e23bab792681153ff2c4e761d096bf066d1e170752666f9a8aa2"}
[2026-10-29T07:46:40Z] U {"action": "complete", "assets": 3, "at": "2026-11-01T01:00:20Z", "credential": "the selftest's", "held": 0, "release_id": 119, "sent": 3, "wall_ns": 1793494820000000000}
[2026-10-29T07:46:40Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 119, "run": 1793494820, "sent": 3, "wall_ns": 1793494820000000000}
[2026-10-29T07:46:40Z] D 1793491200-1793492100.0.stream.jsonl.gz equal bytes 1000 sha256 b040c6925491fa9a68becb24a08bafdcd78029694e6a845383f280c3c3d2f7d5
[2026-10-29T07:46:40Z] D 1793491200-1793492100.1.stream.jsonl.gz equal bytes 2000 sha256 98a5821a4250979f3610470ce39f507e65387ad9966a7e6dfc172935500be563
[2026-10-29T07:46:40Z] D 1793491200-1793492100.2.stream.jsonl.gz equal bytes 3000 sha256 b8a1dce93312e23bab792681153ff2c4e761d096bf066d1e170752666f9a8aa2
[2026-10-29T07:46:40Z] V 1793491200-1793492100.0.stream.jsonl.gz id 120 state uploaded api True bytes 1000 digest sha256:b040c6925491fa9a68becb24a08bafdcd78029694e6a845383f280c3c3d2f7d5 url True download True
[2026-10-29T07:46:40Z] V 1793491200-1793492100.1.stream.jsonl.gz id 121 state uploaded api True bytes 2000 digest sha256:98a5821a4250979f3610470ce39f507e65387ad9966a7e6dfc172935500be563 url True download True
[2026-10-29T07:46:40Z] V 1793491200-1793492100.2.stream.jsonl.gz id 122 state uploaded api True bytes 3000 digest sha256:b8a1dce93312e23bab792681153ff2c4e761d096bf066d1e170752666f9a8aa2 url True download True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-29T07:46:40Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-29T07:46:40Z] L {"assets_n": 3, "bytes_total": 6000, "event": "verify", "release_id": 119, "run": 1793494820, "verify_sha256": "6560144da7f3f8a077051bcab0526a9117480a83923d29dd2d82c0f27a14abd1", "wall_ns": 1793494940500000000}
[2026-10-29T07:46:40Z] X 1793491200-1793492100.0.stream.jsonl.gz 1000 b040c6925491fa9a68becb24a08bafdcd78029694e6a845383f280c3c3d2f7d5 removed at second 140
[2026-10-29T07:46:40Z] X 1793491200-1793492100.1.stream.jsonl.gz 2000 98a5821a4250979f3610470ce39f507e65387ad9966a7e6dfc172935500be563 removed at second 140
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:40Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:41Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:41Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:41Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:41Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:41Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:41Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:41Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:41Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:41Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:41Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:41Z] removal waits: a process of the reward book, [3300000], without its start record
[2026-10-29T07:46:41Z] L {"count": 1, "event": "deferred", "phase": "delete", "reason": "QuietTimeout: the removals waited 1800 s: a process of the reward book, [3300000], without its start record", "run": 1793494820, "wall_ns": 1793497730000000000}
[2026-10-29T07:46:41Z] DEFERRED in delete, 1 of 3: QuietTimeout: the removals waited 1800 s: a process of the reward book, [3300000], without its start record; the next run resumes this set
[2026-10-29T07:46:41Z]   ok  a new process without its start record: the removals wait, then defer with two of three files removed
[2026-10-29T07:46:41Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 230, "resumed": true, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793494820, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793501330000000000}
[2026-10-29T07:46:41Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:41Z] credential: the selftest's
[2026-10-29T07:46:41Z] U {"action": "held", "asset": "1793491200-1793492100.0.stream.jsonl.gz", "at": "2026-11-01T02:48:50Z", "id": 120}
[2026-10-29T07:46:41Z] U {"action": "held", "asset": "1793491200-1793492100.1.stream.jsonl.gz", "at": "2026-11-01T02:48:50Z", "id": 121}
[2026-10-29T07:46:41Z] U {"action": "held", "asset": "1793491200-1793492100.2.stream.jsonl.gz", "at": "2026-11-01T02:48:50Z", "id": 122}
[2026-10-29T07:46:41Z] U {"action": "complete", "assets": 3, "at": "2026-11-01T02:48:50Z", "credential": "the selftest's", "held": 3, "release_id": 119, "sent": 0, "wall_ns": 1793501330000000000}
[2026-10-29T07:46:41Z] L {"created": false, "credential": "the selftest's", "event": "upload", "held": 3, "release_id": 119, "run": 1793494820, "sent": 0, "wall_ns": 1793501330000000000}
[2026-10-29T07:46:41Z] D 1793491200-1793492100.0.stream.jsonl.gz equal bytes 1000 sha256 b040c6925491fa9a68becb24a08bafdcd78029694e6a845383f280c3c3d2f7d5
[2026-10-29T07:46:41Z] D 1793491200-1793492100.1.stream.jsonl.gz equal bytes 2000 sha256 98a5821a4250979f3610470ce39f507e65387ad9966a7e6dfc172935500be563
[2026-10-29T07:46:41Z] D 1793491200-1793492100.2.stream.jsonl.gz equal bytes 3000 sha256 b8a1dce93312e23bab792681153ff2c4e761d096bf066d1e170752666f9a8aa2
[2026-10-29T07:46:41Z] V 1793491200-1793492100.0.stream.jsonl.gz id 120 state uploaded api True bytes 1000 digest sha256:b040c6925491fa9a68becb24a08bafdcd78029694e6a845383f280c3c3d2f7d5 url True download True
[2026-10-29T07:46:41Z] V 1793491200-1793492100.1.stream.jsonl.gz id 121 state uploaded api True bytes 2000 digest sha256:98a5821a4250979f3610470ce39f507e65387ad9966a7e6dfc172935500be563 url True download True
[2026-10-29T07:46:41Z] V 1793491200-1793492100.2.stream.jsonl.gz id 122 state uploaded api True bytes 3000 digest sha256:b8a1dce93312e23bab792681153ff2c4e761d096bf066d1e170752666f9a8aa2 url True download True
[2026-10-29T07:46:41Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-29T07:46:41Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-29T07:46:41Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-29T07:46:41Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-29T07:46:41Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-29T07:46:41Z] L {"assets_n": 3, "bytes_total": 6000, "event": "verify", "release_id": 119, "run": 1793494820, "verify_sha256": "6560144da7f3f8a077051bcab0526a9117480a83923d29dd2d82c0f27a14abd1", "wall_ns": 1793501450500000000}
[2026-10-29T07:46:41Z] X 1793491200-1793492100.2.stream.jsonl.gz 3000 b8a1dce93312e23bab792681153ff2c4e761d096bf066d1e170752666f9a8aa2 removed at second 350
[2026-10-29T07:46:41Z] G-DELETE every file of the set absent         True
[2026-10-29T07:46:41Z] G-DELETE each removal recorded                True
[2026-10-29T07:46:41Z] G-DELETE each slot keeps its slot.json        True
[2026-10-29T07:46:41Z] L {"already": 2, "event": "delete", "free_after": 9600000000, "free_before": 9600000000, "freed": 3000, "gone": 3, "quiet_s": 0, "removed": 1, "run": 1793494820, "slots_kept": 1, "wall_ns": 1793501450500000000}
[2026-10-29T07:46:41Z] at the set's rate the cap stops the streams in 6944.44 days, at 2045-11-05T13:30:50Z
[2026-10-29T07:46:41Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 52.18 days, at 2026-12-23T07:13:46Z
[2026-10-29T07:46:41Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 12.21 days, at 2026-11-13T07:56:22Z
[2026-10-29T07:46:41Z] L {"assets_n": 3, "bytes_total": 6000, "ended_outside": 0, "event": "complete", "free_bytes": 9600000000, "held_s": 0, "peak_rss": 50810880, "rate_per_day": 576000, "removals": 3, "requests": 18, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793494820, "started_outside": 0, "stops": [["the cap", 2393501450], ["the floor, base 43500000 bytes a day", 1798010026], ["the floor, base 187760570 bytes a day", 1794556582]], "store_stream_bytes": 0, "wall_ns": 1793501450500000000}
[2026-10-29T07:46:41Z] COMPLETE: run 1793494820, 3 files, 6000 bytes, Release rewardbook-streams-1793494820
[2026-10-29T07:46:41Z]   ok  the next run resumes: two removals already recorded, the third removed
[2026-10-29T07:46:41Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793581220, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793581220000000000}
[2026-10-29T07:46:41Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:41Z] SLOT 1793578500 2026-11-02T00:15:00Z closed   stream files 1, 4000 bytes, taken 1
[2026-10-29T07:46:41Z] S 1793577600-1793578500.0.stream.jsonl.gz 4000 c614d80ea6ad267c06be5ca0f2be5340745a7a2da823ad803e77ad70a42040bb
[2026-10-29T07:46:41Z] L {"assets_n": 1, "bytes_total": 4000, "closed": 1, "deferred": 0, "event": "set", "first_S": 1793578500, "last_S": 1793578500, "open": 0, "run": 1793581220, "sha256": "103421ace784ad1de06673d5080ab7abea6cf288a8a948d06d52b627c7afc771", "slots_considered": 1, "streamless": 0, "tag": "rewardbook-streams-1793581220", "unclosed": 0, "wall_ns": 1793581220000000000}
[2026-10-29T07:46:41Z] credential: the selftest's
[2026-10-29T07:46:41Z] created the Release on rewardbook-streams-1793581220, id 123
[2026-10-29T07:46:41Z] U {"action": "uploaded", "asset": "1793577600-1793578500.0.stream.jsonl.gz", "at": "2026-11-02T01:00:20Z", "bytes": 4000, "digest": "sha256:c614d80ea6ad267c06be5ca0f2be5340745a7a2da823ad803e77ad70a42040bb", "id": 124, "sha256": "c614d80ea6ad267c06be5ca0f2be5340745a7a2da823ad803e77ad70a42040bb"}
[2026-10-29T07:46:41Z] U {"action": "complete", "assets": 1, "at": "2026-11-02T01:00:20Z", "credential": "the selftest's", "held": 0, "release_id": 123, "sent": 1, "wall_ns": 1793581220000000000}
[2026-10-29T07:46:41Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 123, "run": 1793581220, "sent": 1, "wall_ns": 1793581220000000000}
[2026-10-29T07:46:41Z] D 1793577600-1793578500.0.stream.jsonl.gz equal bytes 4000 sha256 c614d80ea6ad267c06be5ca0f2be5340745a7a2da823ad803e77ad70a42040bb
[2026-10-29T07:46:41Z] V 1793577600-1793578500.0.stream.jsonl.gz id 124 state uploaded api True bytes 4000 digest sha256:c614d80ea6ad267c06be5ca0f2be5340745a7a2da823ad803e77ad70a42040bb url True download True
[2026-10-29T07:46:41Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-29T07:46:41Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-29T07:46:41Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-29T07:46:41Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-29T07:46:41Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-29T07:46:41Z] L {"assets_n": 1, "bytes_total": 4000, "event": "verify", "release_id": 123, "run": 1793581220, "verify_sha256": "d27336400e8529941818167d01219801b913127e1871bb9e17bb001fd8b405e2", "wall_ns": 1793581340500000000}
[2026-10-29T07:46:41Z] L {"event": "halt", "phase": "delete", "reason": "AssertionError: /root/tz34-work/selftest-tmp/changed/store/1793577600/1793578500.0.stream.jsonl.gz is 4001 bytes, SHA-256 0f2026f0e85d350b66b934b674a5d823c3748882c6d42e32b24c0f30092c675e: not the set's", "run": 1793581220, "wall_ns": 1793581340500000000}
[2026-10-29T07:46:41Z] L {"event": "timer-disabled", "exit": 0, "run": 1793581220, "wall_ns": 1793581340500000000}
[2026-10-29T07:46:41Z] HALTED in delete: AssertionError: /root/tz34-work/selftest-tmp/changed/store/1793577600/1793578500.0.stream.jsonl.gz is 4001 bytes, SHA-256 0f2026f0e85d350b66b934b674a5d823c3748882c6d42e32b24c0f30092c675e: not the set's; the timer disabled, exit 0
[2026-10-29T07:46:41Z]   ok  a stream file changed after its verify: the removal refuses it and the archive halts
[2026-10-29T07:46:41Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793667620, "trigger": {"monotonic_usec": null, "realtime_usec": null, "unit": null}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793667620000000000}
[2026-10-29T07:46:41Z] MemAvailable 300000000 bytes, floor 73121792; free 9600000000 bytes, floor 2002000000
[2026-10-29T07:46:41Z] SLOT 1793664900 2026-11-03T00:15:00Z closed   stream files 1, 3000 bytes, taken 1
[2026-10-29T07:46:41Z] S 1793664000-1793664900.0.stream.jsonl.gz 3000 3425577d6df292f6e0c6050aba2032f125666e281cd8c647b2dede809d042156
[2026-10-29T07:46:41Z] L {"assets_n": 1, "bytes_total": 3000, "closed": 1, "deferred": 0, "event": "set", "first_S": 1793664900, "last_S": 1793664900, "open": 0, "run": 1793667620, "sha256": "86d69392e778a431e6bc5946aa69f956284fc8eee6705dd56b78c7d58720a10f", "slots_considered": 1, "streamless": 0, "tag": "rewardbook-streams-1793667620", "unclosed": 0, "wall_ns": 1793667620000000000}
[2026-10-29T07:46:41Z] L {"count": 1, "event": "deferred", "phase": "upload", "reason": "HoldTimeout: the pair book's archive still runs after 1800 s before upload", "run": 1793667620, "wall_ns": 1793669420000000000}
[2026-10-29T07:46:41Z] DEFERRED in upload, 1 of 3: HoldTimeout: the pair book's archive still runs after 1800 s before upload; the next run resumes this set
[2026-10-29T07:46:41Z]   ok  a hold past 1,800 s defers the run before any request
[2026-10-29T07:46:41Z]   ok  the loopback server saw no credential but the run's
[2026-10-29T07:46:41Z]   ok  the temporary stores removed
[2026-10-29T07:46:41Z]   ok  imports: the standard library alone
[2026-10-29T07:46:41Z]   ok  no endpoint in this file's text: every request is TZ-27's
[2026-10-29T07:46:41Z] 49 of 49 checks passed
[2026-10-29T07:46:41Z] peak memory of this run: 61313024 bytes
[2026-10-29T07:46:41Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 96, uploads 16, downloads 23 (330333 bytes); files removed 15
exit=0
```

### 2.3 §3.3 — the units, and the directories beside this session

```
2026-10-29T07:46:51.695642231Z
[2026-10-29T07:46:51Z] btc-pairbook.service {'MainPID': '3216422', 'NRestarts': '12', 'ActiveState': 'active'}, MemoryCurrent 8982528, MemoryPeak 76881920
[2026-10-29T07:46:51Z] btc-recorder.service {'MainPID': '2388318', 'NRestarts': '0', 'ActiveState': 'active'}, MemoryCurrent 13201408, MemoryPeak 302309376
[2026-10-29T07:46:51Z] btc-rewardbook.service {'MainPID': '3137952', 'NRestarts': '1', 'ActiveState': 'active'}, MemoryCurrent 20070400, MemoryPeak 60887040
[2026-10-29T07:46:51Z] btc-pairbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-29T07:46:51Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-29T07:46:51Z] btc-rewardbook-archive.timer {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': ''}
[2026-10-29T07:46:51Z] btc-rewardbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': ''}
[2026-10-29T07:46:51Z] still: recorded
[2026-10-29T07:46:51Z] peak memory of this run: 38334464 bytes
[2026-10-29T07:46:51Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

```
2026-10-29T07:47:05.007686279Z
[2026-10-29T07:47:05Z] running 3114897 started 2026-10-28T10:52:23Z claude
[2026-10-29T07:47:05Z] running 3114907 started 2026-10-28T10:52:25Z claude
[2026-10-29T07:47:05Z] running 3238321 started 2026-10-29T07:43:15Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-10-29T07:47:05Z] 0358b0b2-9811-5291-867b-b185a7307938 born 2026-10-28T06:09:23Z: earlier
[2026-10-29T07:47:05Z] 57feec2d-2369-4cb0-9cad-8ac28cb7e578 born 2026-10-29T07:43:16Z: live, process [3238321]
[2026-10-29T07:47:05Z] 621e47cc-760f-4cb1-8481-c2a8f6828d9d born 2026-10-28T06:09:21Z: earlier
[2026-10-29T07:47:05Z] b82e3547-dd0e-46f7-abe9-4ad9e7903328 born 2026-10-28T10:56:32Z: earlier
[2026-10-29T07:47:05Z] peak memory of this run: 38338560 bytes
[2026-10-29T07:47:05Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

The two `claude` processes started on 2026-10-28, read before any removal (§6): the remote-control daemons, the second this session's parent; TZ-33's session process `3115475` gone.

```
2026-10-29T07:47:22.357918928Z
    PID    PPID                  STARTED     ELAPSED COMMAND
3114897 3114896 Wed Oct 28 10:52:23 2026    20:54:58 claude remote-control --name Crypto Auto VPS
3114907 3114896 Wed Oct 28 10:52:25 2026    20:54:56 claude remote-control --name BTC-5M-TWAP-VPS --spawn=same-dir
3238321 3114907 Thu Oct 29 07:43:15 2026       04:06 /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe --print --sdk-url https://api.anthropic.com/v1/code/sessions/cse_01KgRjgwNZ6BNHYx7fs
pid 3114897 cwd: /root/crypto-auto
0
pid 3114907 cwd: /root/btc-5m-twap
0
3115475 running: 1
```

### 2.4 §9 B-RECLAIM-SCRATCH — after §3.3, before §3.4 (V14, V15)

`I scratch` named three directories **earlier** — map §3's three — and one **live**, `57feec2d-2369-4cb0-9cad-8ac28cb7e578`, this session's process's, which was not touched; the session's own, `540c6c83-4413-5ceb-86a4-2d45c7f8989a`, is never listed. One `I reclaim` named the three; `RECLAIM PASS`; then one `rm -rf` and one `test -e` a directory, each run by the Executor, **none refused by the classifier**:

```
2026-10-29T07:47:40.253750215Z
[2026-10-29T07:47:40Z] reclaim: 3161 report tokens; forensic store holds 2101 files
[2026-10-29T07:47:40Z] RECLAIM PASS: 4 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 2101 -> 2101 files
[2026-10-29T07:47:40Z] peak memory of this run: 39337984 bytes
[2026-10-29T07:47:40Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

```
2026-10-29T07:47:53.926457560Z
exit=0
exit=1
2026-10-29T07:48:04.474313631Z
exit=0
exit=1
2026-10-29T07:48:16.398950112Z
exit=0
exit=1
```

### 2.5 §3.4 — P-PATH (V5): **served**

```
2026-10-29T07:48:26.695618090Z
phase 206
[2026-10-29T07:48:26Z] MemAvailable 320000000 bytes, floor 93454336
[2026-10-29T07:48:27Z] P-PATH release tz-01a-dataset id 385702977; asset twap-divergence-observations.parquet state uploaded, 76818669 bytes, digest sha256:229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b, url True
[2026-10-29T07:48:30Z] P-PATH download: status 200, 76818669 bytes, sha256 229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b
[2026-10-29T07:48:30Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/tags/tz-01a-dataset: 0 bytes, budget 5 s, second 206, 0.3 s, inside True True
[2026-10-29T07:48:30Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/385702977/assets: 0 bytes, budget 5 s, second 207, 0.2 s, inside True True
[2026-10-29T07:48:30Z] T download twap-divergence-observations.parquet: 76818669 bytes, budget 44 s, second 207, 3.4 s, inside True True
[2026-10-29T07:48:30Z] READING P-PATH: served - 3 requests through the run's own path, each inside the idle stretch; the digest present and equal; 76818669 bytes downloaded and equal
[2026-10-29T07:48:30Z] peak memory of this run: 40452096 bytes
[2026-10-29T07:48:30Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 3, uploads 0, downloads 1 (76818669 bytes); files removed 0
exit=0
```

The record: `uploaded`, `76818669` bytes, `digest` `sha256:229a944f…`, the expected URL; the download `200`, `76,818,669` bytes, SHA-256 equal; 3 requests at seconds 206, 207 and 207 of their window, each inside the idle stretch and ended by second 590.

### 2.6 §3.5 — B-INSTALL and G-INSTALL (V6)

```
2026-10-29T07:49:21.747073394Z
exit=0
exit=0
exit=0
exit=0
exit=0
exit=0
2026-10-29T07:49:22.127071410Z
exit=0
```

**7 of 7 `exit=0`; `L` = 2026-10-29T07:49:22.127071410Z**, so the pair book's archive was due at `L + 600`, 07:59:22 UTC — `list-timers` read it so at 07:49:33 — and it ran then (§2.7).

```
2026-10-29T07:49:33.693541791Z
[2026-10-29T07:49:33Z] /root/btc-rewardbook-archive-svc/tz27-pairbook-archive.py sha256 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673; the branch's 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673
[2026-10-29T07:49:33Z] /root/btc-rewardbook-archive-svc/tz28-pairbook-archive-timer.py sha256 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4; the branch's 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4
[2026-10-29T07:49:33Z] /root/btc-rewardbook-archive-svc/tz34-rewardbook-archive-timer.py sha256 1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72; the branch's 1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72
[2026-10-29T07:49:33Z] commit.txt 6a615257277d3c94dafd4d39783499560a344648; the branch head 6a615257277d3c94dafd4d39783499560a344648, its upstream 6a615257277d3c94dafd4d39783499560a344648
[2026-10-29T07:49:33Z] G-INSTALL commit.txt the branch head, pushed                                           True
[2026-10-29T07:49:33Z] G-INSTALL the service's copy of this file the branch's                                 True
[2026-10-29T07:49:33Z] G-INSTALL the service's copy of TZ-28's file, 46a019d65eac                             True
[2026-10-29T07:49:33Z] G-INSTALL the service's copy of TZ-27's file, 2cba96bc9d41                             True
[2026-10-29T07:49:33Z] G-INSTALL the two units byte for byte                                                  True
[2026-10-29T07:49:33Z] G-INSTALL the state directory, root's, 0700, empty                                     True
[2026-10-29T07:49:33Z] G-INSTALL the service loaded, inactive, static                                         True
[2026-10-29T07:49:33Z] G-INSTALL the service a oneshot, Restart=no, Nice=19, 128M, 6h, its argv and directory True
[2026-10-29T07:49:33Z] G-INSTALL the timer loaded, inactive, disabled                                         True
[2026-10-29T07:49:33Z] G-INSTALL PASS: 9 of 9
[2026-10-29T07:49:33Z] peak memory of this run: 38203392 bytes
[2026-10-29T07:49:33Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

### 2.7 §3.6 — the enable mark, B-ENABLE and P-TOKEN, then G-TIMER (V7)

The band §3.6 names opens at second 15 of each window from 07:15:00 UTC. The Executor let the window of 07:45 pass and took the mark at the first second of the window of 08:15, so that the pair book's archive's run set off by `L` could end before the enable's reload (§6); a background wait took it:

```
2026-10-29T08:15:15.605624945Z
[2026-10-29T08:15:15Z] mark enable at 2026-10-29T08:15:15Z, second 15 of its window: the timer {'ActiveState': 'inactive', 'UnitFileState': 'disabled'}, the service {'Result': 'success', 'ActiveState': 'inactive'}
[2026-10-29T08:15:15Z] peak memory of this run: 38207488 bytes
[2026-10-29T08:15:15Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

**The pair book's archive's run of 07:59:22, set off by `L`, had exited `75` — deferred — at 08:02:57 UTC.** Its reason is in that archive's `archive.log`, which §2 item 4 forbids the session to open; its unit's journal, which §2 item 6 allows, names the exit alone. The pair book was not restarted:

```
2026-10-29T08:15:37.723975480Z
2026-10-29T03:00:20+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-29T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-29T03:15:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-29T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 16.034s CPU time.
2026-10-29T07:59:22+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-29T08:02:57+00:00 vultr systemd[1]: btc-pairbook-archive.service: Main process exited, code=exited, status=75/TEMPFAIL
2026-10-29T08:02:57+00:00 vultr systemd[1]: btc-pairbook-archive.service: Failed with result 'exit-code'.
2026-10-29T08:02:57+00:00 vultr systemd[1]: Failed to start btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-29T08:02:57+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 3.684s CPU time.
MainPID=3216422
NRestarts=12
ActiveState=active
MemAvailable:     354968 kB
10416041984
```

B-ENABLE was handed to the Boss at 08:16:02 UTC, second 62 of window `1793261700`, in §3.6's form and verbatim; **the Boss ran it in a root shell on the VPS**, his paste in the session matching the log line for line. It is the Boss's block by the TZ's own text — `path-token` reads the credential — and was not offered to the classifier:

```
Thu Oct 29 08:17:05 AM UTC 2026
2026-10-29T08:17:05.684473573Z
[2026-10-29T08:17:05Z] MemAvailable 338145280 bytes, floor 93454336
[2026-10-29T08:17:05Z] credential: the primary checkout's remote URL
[2026-10-29T08:17:06Z] repository: status 200, full_name 'seahomebatumi-ai/btc-5m-twap', push True
[2026-10-29T08:17:06Z] READING P-TOKEN: served - the credential from the primary checkout's remote URL reads seahomebatumi-ai/btc-5m-twap with push, and the Release 409534533; 2 requests
[2026-10-29T08:17:06Z] peak memory of this run: 39153664 bytes
[2026-10-29T08:17:06Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 2, uploads 0, downloads 0 (0 bytes); files removed 0
Created symlink /etc/systemd/system/timers.target.wants/btc-rewardbook-archive.timer → /etc/systemd/system/btc-rewardbook-archive.timer.
exit=0
```

**Its wait ended at 08:17:05.684473573 UTC — `E` — second 125 of its window and second 29,825 of the day, inside 15 to 480 and 26,100 to 68,400; `READING P-TOKEN: served`**, the credential's source the primary checkout's remote URL, `push` true, the Release `409534533`, 2 requests; the link created; `exit=0`. A background watcher of the Executor's, which waited for the log's `exit=` line and ran `I timer` where it read `served` and `exit=0` (§6), read G-TIMER 1.6 s after `E`:

```
2026-10-29T08:17:07.320652668Z
[2026-10-29T08:17:07Z] the timer: {'Unit': 'btc-rewardbook-archive.service', 'TimersMonotonic': '{ OnActiveUSec=30min ; next_elapse=2month 3w 6d 4h 22min 34.856369s }', 'TimersCalendar': '{ OnCalendar=*-*-* 01:30:20 UTC ; next_elapse=Fri 2026-10-30 01:30:20 UTC }', 'NextElapseUSecRealtime': 'Fri 2026-10-30 01:30:20 UTC', 'LastTriggerUSec': '', 'AccuracyUSec': '1s', 'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'waiting', 'FragmentPath': '/etc/systemd/system/btc-rewardbook-archive.timer', 'UnitFileState': 'enabled', 'ActiveEnterTimestamp': 'Thu 2026-10-29 08:17:07 UTC'}
[2026-10-29T08:17:07Z] G-TIMER loaded                   True
[2026-10-29T08:17:07Z] G-TIMER active                   True
[2026-10-29T08:17:07Z] G-TIMER enabled                  True
[2026-10-29T08:17:07Z] G-TIMER fragment                 True
[2026-10-29T08:17:07Z] G-TIMER its unit                 True
[2026-10-29T08:17:07Z] G-TIMER the calendar             True
[2026-10-29T08:17:07Z] G-TIMER 1,800 s after it starts  True
[2026-10-29T08:17:07Z] G-TIMER accuracy 1 s             True
[2026-10-29T08:17:07Z] G-TIMER the next calendar elapse True
[2026-10-29T08:17:07Z] G-TIMER PASS: the next calendar run at 2026-10-30T01:30:20Z, the run after the start at 2026-10-29T08:47:07Z
[2026-10-29T08:17:07Z] peak memory of this run: 38072320 bytes
[2026-10-29T08:17:07Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

**G-TIMER PASS, 9 of 9**: the next calendar run 2026-10-30 01:30:20 UTC; the first run due 08:47:07 UTC.

### 2.8 §3.7 — the first run: its deferral, B-RETRY, and `first` (V8, V9)

`I first` every 300 s from `E + 1,800`, 08:47:05 UTC, by a background loop of the Executor's (§6). Its second read found the run deferred:

```
2026-10-29T08:47:05.523315065Z
[2026-10-29T08:47:05Z] NOT YET: no run since the mark; the service inactive
[2026-10-29T08:47:05Z] peak memory of this run: 38072320 bytes
[2026-10-29T08:47:05Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=3
2026-10-29T08:52:05.445622478Z
[2026-10-29T08:52:05Z] R {"commit": "6a615257277d3c94dafd4d39783499560a344648", "event": "start", "file_sha256": "1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72", "invocation": "957b92a52a0b4e71ba3aa47b0d3cfee4", "phase_at": 127, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793263627, "trigger": {"monotonic_usec": "7608155369576", "realtime_usec": "1793263627648061", "unit": "btc-rewardbook-archive.timer"}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793263627791757143}
[2026-10-29T08:52:05Z] R {"assets_n": 86, "bytes_total": 890975956, "closed": 85, "deferred": 0, "event": "set", "first_S": 1793187000, "last_S": 1793262600, "open": 1, "run": 1793263627, "sha256": "f3450db0742d155b3e5487cdbde9d0bdf3877661c4c12fc962dcccd7981e7f3e", "slots_considered": 85, "streamless": 0, "tag": "rewardbook-streams-1793263627", "unclosed": 0, "wall_ns": 1793263629875057156}
[2026-10-29T08:52:05Z] R {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 427629503, "run": 1793263627, "sent": 86, "wall_ns": 1793263750650317431}
[2026-10-29T08:52:05Z] R {"count": 1, "event": "deferred", "phase": "verify", "reason": "AssertionError: VERIFY FAIL: [\"every asset uploaded, its bytes and digest the set's\", \"every download the set's bytes and SHA-256\", 'no asset missing', 'release published on the tag']; missing ['1793145600-1793187000.0.stream.jsonl.gz', '1793145600-1793187900.0.stream.jsonl.gz', '1793145600-1793188800.0.stream.jsonl.gz', '1793145600-1793189700.0.stream.jsonl.gz', '1793145600-1793190600.0.stream.js", "run": 1793263627, "wall_ns": 1793263871436449799}
[2026-10-29T08:52:05Z] run 1793263627: 4 records, ['start', 'set', 'upload', 'deferred']
[2026-10-29T08:52:05Z] READING G-RUN: DEFERRED - the run's last record deferred, in its phase 'verify'
[2026-10-29T08:52:05Z] peak memory of this run: 38203392 bytes
[2026-10-29T08:52:05Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=1
```

The run, `A` `1793263627`, fired by the timer at 08:47:07.648 UTC, had taken its set at 08:47:09, created Release `427629503` and sent all 86 assets with the credential by 08:49:10, and at 08:51:11 its anonymous verify found no Release on its tag — `release_by_tag` returned `404`, since a `403` or any status but `200` and `404` stops TZ-27's call at its own assert — and deferred, count 1, nothing removed. **B-RETRY was not run at once.** The session ran `path` again, its own anonymous request path, on `tz-01a-dataset`'s Release, which §3.4 had read at 07:48 (§6):

```
2026-10-29T08:53:42.846942372Z
phase 522
[2026-10-29T08:53:42Z] MemAvailable 302534656 bytes, floor 93454336
Traceback (most recent call last):
  File "/root/tz34-work/wt/research/tz34-rewardbook-archive-timer.py", line 1791, in <module>
    sys.exit(main(sys.argv[1:]))
             ^^^^^^^^^^^^^^^^^^
  File "/root/tz34-work/wt/research/tz34-rewardbook-archive-timer.py", line 1780, in main
    table[mode]()
  File "/root/tz34-work/wt/research/tz28-pairbook-archive-timer.py", line 765, in mode_path
    assert rel is not None, "P-PATH: no release on %s" % tz27.PATH_TAG
           ^^^^^^^^^^^^^^^
AssertionError: P-PATH: no release on tz-01a-dataset
exit=1
```

`no release on tz-01a-dataset`: the repository's Releases were not served without a token, while the credential's requests were — P-TOKEN at 08:17, the run's creation and uploads. The units and the store then, nothing removed:

```
2026-10-29T08:54:02.317590686Z
MainPID=0
Result=exit-code
NRestarts=0
ExecMainStatus=75
Id=btc-rewardbook-archive.service
ActiveState=failed
SubState=failed
UnitFileState=static

Result=success
Id=btc-rewardbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled

MainPID=3137952
Result=success
NRestarts=1
ExecMainStatus=0
Id=btc-rewardbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
NEXT                        LEFT LAST                          PASSED UNIT                         ACTIVATES
Fri 2026-10-30 01:30:20 UTC  16h Thu 2026-10-29 08:47:07 UTC 6min ago btc-rewardbook-archive.timer btc-rewardbook-archive.service

1 timers listed.
10337398784
915134541	/var/lib/btc-rewardbook
```

The Executor reported this to the Boss and held B-RETRY. **The Boss stated: «Репозиторий снова переведён в Public. Проверь доступ и запускай B-RETRY.»** — the repository set to public again — a routing action, recorded as his. The session verified it through its own request path:

```
2026-10-29T09:00:51.762483083Z
phase 51
[2026-10-29T09:00:51Z] MemAvailable 275009536 bytes, floor 93454336
[2026-10-29T09:00:52Z] P-PATH release tz-01a-dataset id 385702977; asset twap-divergence-observations.parquet state uploaded, 76818669 bytes, digest sha256:229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b, url True
[2026-10-29T09:00:53Z] P-PATH download: status 200, 76818669 bytes, sha256 229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b
[2026-10-29T09:00:53Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/tags/tz-01a-dataset: 0 bytes, budget 5 s, second 51, 0.3 s, inside True True
[2026-10-29T09:00:53Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/385702977/assets: 0 bytes, budget 5 s, second 52, 0.3 s, inside True True
[2026-10-29T09:00:53Z] T download twap-divergence-observations.parquet: 76818669 bytes, budget 44 s, second 52, 1.4 s, inside True True
[2026-10-29T09:00:53Z] READING P-PATH: served - 3 requests through the run's own path, each inside the idle stretch; the digest present and equal; 76818669 bytes downloaded and equal
[2026-10-29T09:00:53Z] peak memory of this run: 40189952 bytes
[2026-10-29T09:00:53Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 3, uploads 0, downloads 1 (76818669 bytes); files removed 0
exit=0
```

**B-RETRY**, once: its mark, then its line, run by the Executor, not refused:

```
2026-10-29T09:01:01.597178681Z
[2026-10-29T09:01:01Z] mark retry at 2026-10-29T09:01:01Z, second 61 of its window: the timer {'ActiveState': 'active', 'UnitFileState': 'enabled'}, the service {'Result': 'exit-code', 'ActiveState': 'failed'}
[2026-10-29T09:01:01Z] peak memory of this run: 38072320 bytes
[2026-10-29T09:01:01Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

```
2026-10-29T09:01:12.630542157Z
exit=0
```

`I first` every 300 s again, from 09:01:24 UTC; its runs before the deciding one:

```
2026-10-29T09:01:24.955736697Z
[2026-10-29T09:01:25Z] NOT YET: run 1793263627; the service activating
[2026-10-29T09:01:25Z] peak memory of this run: 38072320 bytes
[2026-10-29T09:01:25Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=3
2026-10-29T09:06:24.800098852Z
[2026-10-29T09:06:24Z] NOT YET: run 1793263627 complete; G-NEXT's last slot 1793265300 is due at 2026-10-29T09:30:40Z
[2026-10-29T09:06:24Z] peak memory of this run: 38072320 bytes
[2026-10-29T09:06:24Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=3
2026-10-29T09:11:24.606538022Z
[2026-10-29T09:11:24Z] NOT YET: run 1793263627 complete; G-NEXT's last slot 1793265300 is due at 2026-10-29T09:30:40Z
[2026-10-29T09:11:24Z] peak memory of this run: 38076416 bytes
[2026-10-29T09:11:24Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=3
2026-10-29T09:16:24.479230011Z
[2026-10-29T09:16:24Z] NOT YET: run 1793263627 complete; G-NEXT's last slot 1793265300 is due at 2026-10-29T09:30:40Z
[2026-10-29T09:16:24Z] peak memory of this run: 37941248 bytes
[2026-10-29T09:16:24Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=3
2026-10-29T09:21:24.272449374Z
[2026-10-29T09:21:24Z] NOT YET: run 1793263627 complete; G-NEXT's last slot 1793265300 is due at 2026-10-29T09:30:40Z
[2026-10-29T09:21:24Z] peak memory of this run: 37941248 bytes
[2026-10-29T09:21:24Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=3
2026-10-29T09:26:24.097814277Z
[2026-10-29T09:26:24Z] NOT YET: run 1793263627 complete; G-NEXT's last slot 1793265300 is due at 2026-10-29T09:30:40Z
[2026-10-29T09:26:24Z] peak memory of this run: 37810176 bytes
[2026-10-29T09:26:24Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=3
```

**The deciding run, 09:31:24 UTC — every `R` record of the run, the `SLOT`, `S`, `ROW`, `T`, `X`, `G-NEXT` and `ACROSS` lines** (`logs/67-first-deciding.log`, lines 31 to 588 of `logs/66-first-after-retry.log`):

```
2026-10-29T09:31:24.011412978Z
[2026-10-29T09:31:24Z] R {"commit": "6a615257277d3c94dafd4d39783499560a344648", "event": "start", "file_sha256": "1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72", "invocation": "957b92a52a0b4e71ba3aa47b0d3cfee4", "phase_at": 127, "resumed": false, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793263627, "trigger": {"monotonic_usec": "7608155369576", "realtime_usec": "1793263627648061", "unit": "btc-rewardbook-archive.timer"}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793263627791757143}
[2026-10-29T09:31:24Z] R {"assets_n": 86, "bytes_total": 890975956, "closed": 85, "deferred": 0, "event": "set", "first_S": 1793187000, "last_S": 1793262600, "open": 1, "run": 1793263627, "sha256": "f3450db0742d155b3e5487cdbde9d0bdf3877661c4c12fc962dcccd7981e7f3e", "slots_considered": 85, "streamless": 0, "tag": "rewardbook-streams-1793263627", "unclosed": 0, "wall_ns": 1793263629875057156}
[2026-10-29T09:31:24Z] R {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 427629503, "run": 1793263627, "sent": 86, "wall_ns": 1793263750650317431}
[2026-10-29T09:31:24Z] R {"count": 1, "event": "deferred", "phase": "verify", "reason": "AssertionError: VERIFY FAIL: [\"every asset uploaded, its bytes and digest the set's\", \"every download the set's bytes and SHA-256\", 'no asset missing', 'release published on the tag']; missing ['1793145600-1793187000.0.stream.jsonl.gz', '1793145600-1793187900.0.stream.jsonl.gz', '1793145600-1793188800.0.stream.jsonl.gz', '1793145600-1793189700.0.stream.jsonl.gz', '1793145600-1793190600.0.stream.js", "run": 1793263627, "wall_ns": 1793263871436449799}
[2026-10-29T09:31:24Z] R {"commit": "6a615257277d3c94dafd4d39783499560a344648", "event": "start", "file_sha256": "1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72", "invocation": "a1eb6d29178b4815966bcd5051a3c604", "phase_at": 72, "resumed": true, "rewardbook": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793263627, "trigger": {"monotonic_usec": "7608155369576", "realtime_usec": "1793263627648061", "unit": "btc-rewardbook-archive.timer"}, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "tz28_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "wall_ns": 1793264472875136224}
[2026-10-29T09:31:24Z] R {"created": false, "credential": "the primary checkout's remote URL", "event": "upload", "held": 86, "release_id": 427629503, "run": 1793263627, "sent": 0, "wall_ns": 1793264473954003336}
[2026-10-29T09:31:24Z] R {"assets_n": 86, "bytes_total": 890975956, "event": "verify", "release_id": 427629503, "run": 1793263627, "verify_sha256": "dad6b5783342c244dcc7fb8d5540b8c6176c809c4a1dd9204a3cc2eb6c6c4379", "wall_ns": 1793264668099816309}
[2026-10-29T09:31:24Z] R {"already": 0, "event": "delete", "free_after": 11195334656, "free_before": 10304053248, "freed": 890975956, "gone": 86, "quiet_s": 0, "removed": 86, "run": 1793263627, "slots_kept": 85, "wall_ns": 1793264670943221111}
[2026-10-29T09:31:24Z] R {"assets_n": 86, "bytes_total": 890975956, "ended_outside": 0, "event": "complete", "free_bytes": 11195334656, "held_s": 0, "peak_rss": 39477248, "rate_per_day": 1006278726, "removals": 86, "requests": 180, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793263627, "started_outside": 0, "stops": [["the cap", 1793606667], ["the floor, base 43500000 bytes a day", 1793585267], ["the floor, base 187760570 bytes a day", 1793546534]], "store_stream_bytes": 16842458, "wall_ns": 1793264670967510113}
[2026-10-29T09:31:24Z] run 1793263627: 9 records, ['start', 'set', 'upload', 'deferred', 'start', 'upload', 'verify', 'delete', 'complete']
[2026-10-29T09:31:24Z] G-TRIGGER, by TRIGGER_UNIT btc-rewardbook-archive.timer: the enable mark 2026-10-29T08:15:15Z, the timer started 2026-10-29T08:17:07Z, the run's trigger 2026-10-29T08:47:07Z - 112 s after the mark plus 1800 - the run's first record 2026-10-29T08:47:07Z; the timer's last trigger 2026-10-29T08:47:07Z
[2026-10-29T09:31:24Z] G-RUN: the run complete; the service's last invocation a1eb6d29178b4815966bcd5051a3c604, Result success, ExecMainStatus 0, Thu 2026-10-29 09:01:12 UTC to Thu 2026-10-29 09:04:31 UTC
[2026-10-29T09:31:24Z] SLOT 1793187000 2026-10-28T11:30:00Z closed   stream files 1, 9629579 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793187900 2026-10-28T11:45:00Z closed   stream files 1, 9639138 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793188800 2026-10-28T12:00:00Z closed   stream files 1, 10430786 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793189700 2026-10-28T12:15:00Z closed   stream files 1, 10844068 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793190600 2026-10-28T12:30:00Z closed   stream files 1, 11422263 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793191500 2026-10-28T12:45:00Z closed   stream files 2, 11493632 bytes, taken 2
[2026-10-29T09:31:24Z] SLOT 1793192400 2026-10-28T13:00:00Z closed   stream files 1, 11723039 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793193300 2026-10-28T13:15:00Z closed   stream files 1, 10919554 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793194200 2026-10-28T13:30:00Z closed   stream files 1, 9958510 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793195100 2026-10-28T13:45:00Z closed   stream files 1, 10225257 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793196000 2026-10-28T14:00:00Z closed   stream files 1, 9759422 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793196900 2026-10-28T14:15:00Z closed   stream files 1, 9780710 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793197800 2026-10-28T14:30:00Z closed   stream files 1, 9880467 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793198700 2026-10-28T14:45:00Z closed   stream files 1, 11208381 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793199600 2026-10-28T15:00:00Z closed   stream files 1, 12025155 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793200500 2026-10-28T15:15:00Z closed   stream files 1, 10028151 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793201400 2026-10-28T15:30:00Z closed   stream files 1, 10684034 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793202300 2026-10-28T15:45:00Z closed   stream files 1, 10156189 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793203200 2026-10-28T16:00:00Z closed   stream files 1, 10279670 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793204100 2026-10-28T16:15:00Z closed   stream files 1, 9536875 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793205000 2026-10-28T16:30:00Z closed   stream files 1, 10141202 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793205900 2026-10-28T16:45:00Z closed   stream files 1, 9715061 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793206800 2026-10-28T17:00:00Z closed   stream files 1, 11001064 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793207700 2026-10-28T17:15:00Z closed   stream files 1, 9835502 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793208600 2026-10-28T17:30:00Z closed   stream files 1, 9874421 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793209500 2026-10-28T17:45:00Z closed   stream files 1, 9385489 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793210400 2026-10-28T18:00:00Z closed   stream files 1, 10966063 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793211300 2026-10-28T18:15:00Z closed   stream files 1, 10551024 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793212200 2026-10-28T18:30:00Z closed   stream files 1, 12372196 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793213100 2026-10-28T18:45:00Z closed   stream files 1, 11112191 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793214000 2026-10-28T19:00:00Z closed   stream files 1, 10918172 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793214900 2026-10-28T19:15:00Z closed   stream files 1, 10956690 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793215800 2026-10-28T19:30:00Z closed   stream files 1, 10464479 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793216700 2026-10-28T19:45:00Z closed   stream files 1, 11797234 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793217600 2026-10-28T20:00:00Z closed   stream files 1, 9947721 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793218500 2026-10-28T20:15:00Z closed   stream files 1, 9342830 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793219400 2026-10-28T20:30:00Z closed   stream files 1, 8879554 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793220300 2026-10-28T20:45:00Z closed   stream files 1, 9062207 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793221200 2026-10-28T21:00:00Z closed   stream files 1, 9372847 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793222100 2026-10-28T21:15:00Z closed   stream files 1, 8001926 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793223000 2026-10-28T21:30:00Z closed   stream files 1, 8114414 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793223900 2026-10-28T21:45:00Z closed   stream files 1, 9006052 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793224800 2026-10-28T22:00:00Z closed   stream files 1, 8661025 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793225700 2026-10-28T22:15:00Z closed   stream files 1, 8132267 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793226600 2026-10-28T22:30:00Z closed   stream files 1, 9326449 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793227500 2026-10-28T22:45:00Z closed   stream files 1, 9815975 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793228400 2026-10-28T23:00:00Z closed   stream files 1, 9231800 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793229300 2026-10-28T23:15:00Z closed   stream files 1, 8160699 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793230200 2026-10-28T23:30:00Z closed   stream files 1, 8889088 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793231100 2026-10-28T23:45:00Z closed   stream files 1, 9143917 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793232000 2026-10-29T00:00:00Z closed   stream files 1, 11579610 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793232900 2026-10-29T00:15:00Z closed   stream files 1, 10715152 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793233800 2026-10-29T00:30:00Z closed   stream files 1, 11443056 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793234700 2026-10-29T00:45:00Z closed   stream files 1, 13592154 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793235600 2026-10-29T01:00:00Z closed   stream files 1, 11481990 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793236500 2026-10-29T01:15:00Z closed   stream files 1, 11586307 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793237400 2026-10-29T01:30:00Z closed   stream files 1, 10660664 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793238300 2026-10-29T01:45:00Z closed   stream files 1, 10776660 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793239200 2026-10-29T02:00:00Z closed   stream files 1, 10626770 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793240100 2026-10-29T02:15:00Z closed   stream files 1, 9792424 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793241000 2026-10-29T02:30:00Z closed   stream files 1, 10745728 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793241900 2026-10-29T02:45:00Z closed   stream files 1, 11272730 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793242800 2026-10-29T03:00:00Z closed   stream files 1, 9774209 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793243700 2026-10-29T03:15:00Z closed   stream files 1, 9321701 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793244600 2026-10-29T03:30:00Z closed   stream files 1, 10295145 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793245500 2026-10-29T03:45:00Z closed   stream files 1, 10434441 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793246400 2026-10-29T04:00:00Z closed   stream files 1, 11156773 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793247300 2026-10-29T04:15:00Z closed   stream files 1, 11456592 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793248200 2026-10-29T04:30:00Z closed   stream files 1, 11804877 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793249100 2026-10-29T04:45:00Z closed   stream files 1, 11704215 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793250000 2026-10-29T05:00:00Z closed   stream files 1, 9914992 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793250900 2026-10-29T05:15:00Z closed   stream files 1, 10553162 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793251800 2026-10-29T05:30:00Z closed   stream files 1, 6547939 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793252700 2026-10-29T05:45:00Z closed   stream files 1, 6710655 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793253600 2026-10-29T06:00:00Z closed   stream files 1, 10468900 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793254500 2026-10-29T06:15:00Z closed   stream files 1, 11330444 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793255400 2026-10-29T06:30:00Z closed   stream files 1, 10581288 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793256300 2026-10-29T06:45:00Z closed   stream files 1, 9852787 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793257200 2026-10-29T07:00:00Z closed   stream files 1, 12148871 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793258100 2026-10-29T07:15:00Z closed   stream files 1, 13568827 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793259000 2026-10-29T07:30:00Z closed   stream files 1, 11991341 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793259900 2026-10-29T07:45:00Z closed   stream files 1, 12726821 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793260800 2026-10-29T08:00:00Z closed   stream files 1, 14804505 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793261700 2026-10-29T08:15:00Z closed   stream files 1, 12815998 bytes, taken 1
[2026-10-29T09:31:24Z] SLOT 1793262600 2026-10-29T08:30:00Z closed   stream files 1, 14933789 bytes, taken 1
[2026-10-29T09:31:24Z] S 1793145600-1793187000.0.stream.jsonl.gz 9629579 121ae8ad5aaffa260737f6d5ea469e4792e7d7793f7db604e4f6152bc7504916
[2026-10-29T09:31:24Z] S 1793145600-1793187900.0.stream.jsonl.gz 9639138 37ad0796a091fb6a9b088c0c266d0cbbd88e104c670d8efd33c670c4abf2a823
[2026-10-29T09:31:24Z] S 1793145600-1793188800.0.stream.jsonl.gz 10430786 ad85da3abf58feedae79d68ebfb8d0a402f25acd40459d96f28ea9a47c70bb96
[2026-10-29T09:31:24Z] S 1793145600-1793189700.0.stream.jsonl.gz 10844068 c91f3297a636a3e239bfa529c3804cf626f66765c5b3256afe04c1a301061039
[2026-10-29T09:31:24Z] S 1793145600-1793190600.0.stream.jsonl.gz 11422263 ab9b26074465807668fd298a824ec53d5bf3678ea7452b37ab44ea2f3d145d5f
[2026-10-29T09:31:24Z] S 1793145600-1793191500.0.stream.jsonl.gz 8669289 4aff733af5bc9e08e2996011967bab6fc0a58bb5230961f7fcc3f488d4fc7f6e
[2026-10-29T09:31:24Z] S 1793145600-1793191500.1.stream.jsonl.gz 2824343 7bfe046788a1f35db8bf621b1608b3262bb7405340ca88931bd74b821c501f1f
[2026-10-29T09:31:24Z] S 1793145600-1793192400.0.stream.jsonl.gz 11723039 8028f8a9d828d6c1e94d383faae0d68af94675d1f2ba57a568ec34962bd6e06b
[2026-10-29T09:31:24Z] S 1793145600-1793193300.0.stream.jsonl.gz 10919554 0d49767ed12888f2994c6e6e8a8ecdd6a2d540713db437bb46c8c73a97718275
[2026-10-29T09:31:24Z] S 1793145600-1793194200.0.stream.jsonl.gz 9958510 a61297412d0223c0dd827965661a609463b26136d71bc0bb403723491b871d9a
[2026-10-29T09:31:24Z] S 1793145600-1793195100.0.stream.jsonl.gz 10225257 10fd14580576dcf7d2ba5b34377db1c0ab94909089504afdf4e3b831958fe731
[2026-10-29T09:31:24Z] S 1793145600-1793196000.0.stream.jsonl.gz 9759422 e8765455d1f1f783288f086027d3b198cf31741944bd5a188b22565345983481
[2026-10-29T09:31:24Z] S 1793145600-1793196900.0.stream.jsonl.gz 9780710 88c2c84708ab437c4fe5fce3f84776211e62fd1dd5af70fdba40f1894897bdd0
[2026-10-29T09:31:24Z] S 1793145600-1793197800.0.stream.jsonl.gz 9880467 a5d99308e054693a039d9ee64579ca5015652f140ff1fdd9dac8e9cb72e4eb3a
[2026-10-29T09:31:24Z] S 1793145600-1793198700.0.stream.jsonl.gz 11208381 075da9e7c5a711a1c555cf14c07cdadc4121ac49e6355d05b7f9e7875094af61
[2026-10-29T09:31:24Z] S 1793145600-1793199600.0.stream.jsonl.gz 12025155 c70cf12a975796105a875b8f8d7a73682ec557cd30ffd0dd0f051ae2ea90adc3
[2026-10-29T09:31:24Z] S 1793145600-1793200500.0.stream.jsonl.gz 10028151 8a2b4f911f7467b3ce3c5088829e499cc72a6d647128f7587c2d1f700ebf0558
[2026-10-29T09:31:24Z] S 1793145600-1793201400.0.stream.jsonl.gz 10684034 99341832a61bf589521a253a863d94db68526d8a53114d0a855917b354e8a896
[2026-10-29T09:31:24Z] S 1793145600-1793202300.0.stream.jsonl.gz 10156189 ec78fb31112d645c9c08ded59c6befd6277bdfb7e260723c9340467f5b3fcea7
[2026-10-29T09:31:24Z] S 1793145600-1793203200.0.stream.jsonl.gz 10279670 5c10b99de3ca84f6d0cd4fd556fa530483c301e1bf3c7bb80114eef519ebd1bc
[2026-10-29T09:31:24Z] S 1793145600-1793204100.0.stream.jsonl.gz 9536875 ffbc1876095b1ca7ca17b218892d8b42c3bb918183eca7b7827d7de25ec768f5
[2026-10-29T09:31:24Z] S 1793145600-1793205000.0.stream.jsonl.gz 10141202 b38c8fd1d01f0fa20fe38b26a94255344e296c83b509640bee279dcad5deff16
[2026-10-29T09:31:24Z] S 1793145600-1793205900.0.stream.jsonl.gz 9715061 0afde34b6cf80083b9cdda7bef5baacfa1dc946f61e68886265cb3633f3a3538
[2026-10-29T09:31:24Z] S 1793145600-1793206800.0.stream.jsonl.gz 11001064 e9f2f8a8ff6cef04b36b04cbffaaed9b5accf26873d26eed74b85d8dc6199378
[2026-10-29T09:31:24Z] S 1793145600-1793207700.0.stream.jsonl.gz 9835502 6eec69739f70d0ac95fa8735d2154567794477b47cc5d9d43f2bfac27bedcc99
[2026-10-29T09:31:24Z] S 1793145600-1793208600.0.stream.jsonl.gz 9874421 1084bd093c165ef45f8cbce038465b4a5fcb395d435ef7556d05d85f08169ce5
[2026-10-29T09:31:24Z] S 1793145600-1793209500.0.stream.jsonl.gz 9385489 09177e12607a802d3aac38cdf988ec17229af4238b4a87a55224d75117561d73
[2026-10-29T09:31:24Z] S 1793145600-1793210400.0.stream.jsonl.gz 10966063 b10381fa9dc7552d8d16e2b480baeb4f6ff30651921c3b89323a0659d8955d58
[2026-10-29T09:31:24Z] S 1793145600-1793211300.0.stream.jsonl.gz 10551024 fd8659f6bf0eaba31206970e69ba9f5b0a915c804e73a0dba9815a35dbb90bd7
[2026-10-29T09:31:24Z] S 1793145600-1793212200.0.stream.jsonl.gz 12372196 a4e4aa901676ac2ad3585b6cbc7edc0349ed0fffa7e41a744ab602c954738485
[2026-10-29T09:31:24Z] S 1793145600-1793213100.0.stream.jsonl.gz 11112191 17b2340abe0d5466dc70c8584c970feb094a07f2ca5d534aae2d4459520efd65
[2026-10-29T09:31:24Z] S 1793145600-1793214000.0.stream.jsonl.gz 10918172 9e3d0b9f03b4cbd00834375385767f370ee4a479fd0c1ca54c40052213cce5a5
[2026-10-29T09:31:24Z] S 1793145600-1793214900.0.stream.jsonl.gz 10956690 d70fe0f958eb08281fb8c3cf74567121bafeffadc272afebb3b973938eedeba9
[2026-10-29T09:31:24Z] S 1793145600-1793215800.0.stream.jsonl.gz 10464479 7f48547a7aa076d1133ab3ffc013aa90a2f0f464eefd55f474c6de7482af44b0
[2026-10-29T09:31:24Z] S 1793145600-1793216700.0.stream.jsonl.gz 11797234 87f3efd83e33c5ffe9e9b035a4c5b090b645462a68b0f96645818f91f2997faf
[2026-10-29T09:31:24Z] S 1793145600-1793217600.0.stream.jsonl.gz 9947721 1ca2fac80bb178ad476eb69bcf3a26f90fc6c25af5715df82672dd8de84107c0
[2026-10-29T09:31:24Z] S 1793145600-1793218500.0.stream.jsonl.gz 9342830 70c9bd544e19d236188538cc43cd89663cd327d6bd516ef442e01ff89f59508a
[2026-10-29T09:31:24Z] S 1793145600-1793219400.0.stream.jsonl.gz 8879554 07b12705033d39a7a84982ea7e311d31522b0e4ab09580a5868c83f17c054186
[2026-10-29T09:31:24Z] S 1793145600-1793220300.0.stream.jsonl.gz 9062207 0154c6a783d139f1532ec09d9060da71cfd1254552aacfb75ed385f7799d4006
[2026-10-29T09:31:24Z] S 1793145600-1793221200.0.stream.jsonl.gz 9372847 57bf808b26b559fdf9f211e59a761fac1f9b8c2dfda86bc3723f984eb5914a08
[2026-10-29T09:31:24Z] S 1793145600-1793222100.0.stream.jsonl.gz 8001926 18c0bdb9008b4b40471b5b99a4ddc854c5e6b1f39d9659f479b252a69a8884be
[2026-10-29T09:31:24Z] S 1793145600-1793223000.0.stream.jsonl.gz 8114414 f6101c8eb420b9eda97f353d7adcebdc355fbec4bb93ff6a69b6cab57adcaed6
[2026-10-29T09:31:24Z] S 1793145600-1793223900.0.stream.jsonl.gz 9006052 86ef7ae2e14ac60b9b57edc530427e2fb33d0a481aa315799106c43e59c0e0e0
[2026-10-29T09:31:24Z] S 1793145600-1793224800.0.stream.jsonl.gz 8661025 752e54df1a8237873fa10a40e759b042763c89cb5b87d745b89949d3f20b2e0e
[2026-10-29T09:31:24Z] S 1793145600-1793225700.0.stream.jsonl.gz 8132267 9485eb5864c99e37e00d178bd4312b6ef4dc779694a5e4de480941b41bb88297
[2026-10-29T09:31:24Z] S 1793145600-1793226600.0.stream.jsonl.gz 9326449 2cdeb8ca3f85fca93e521e3a2151e6d95c5a24d19c61d58e87cec47b18696819
[2026-10-29T09:31:24Z] S 1793145600-1793227500.0.stream.jsonl.gz 9815975 ec2d3c0868e6d21c3754d1c290895c080a46c58048103ecb37ede7d4b8edfc3e
[2026-10-29T09:31:24Z] S 1793145600-1793228400.0.stream.jsonl.gz 9231800 fef35a594b2704d0984f9bc737782ea2bc46b5f264d0712d9df2c10ffa97924b
[2026-10-29T09:31:24Z] S 1793145600-1793229300.0.stream.jsonl.gz 8160699 7ef7d872fc56eeeb309f156a13f8ae10ed68aeeb1b545a566ca7f3a4e4e5e994
[2026-10-29T09:31:24Z] S 1793145600-1793230200.0.stream.jsonl.gz 8889088 c2b14f9702d26b6853601d83b685113b6f5650d2b86c644724e87d1f619eec17
[2026-10-29T09:31:24Z] S 1793145600-1793231100.0.stream.jsonl.gz 9143917 e177b5e38f162522be08df4692d8789e36a8a8a83ee5cf9856940a05dbaf955a
[2026-10-29T09:31:24Z] S 1793232000-1793232000.0.stream.jsonl.gz 11579610 bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f
[2026-10-29T09:31:24Z] S 1793232000-1793232900.0.stream.jsonl.gz 10715152 46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370
[2026-10-29T09:31:24Z] S 1793232000-1793233800.0.stream.jsonl.gz 11443056 2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9
[2026-10-29T09:31:24Z] S 1793232000-1793234700.0.stream.jsonl.gz 13592154 ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496
[2026-10-29T09:31:24Z] S 1793232000-1793235600.0.stream.jsonl.gz 11481990 13cfa07ef0b2a4b17c6dfd8a73acb7124fcaaab9efcc0630e3b35075c6a68806
[2026-10-29T09:31:24Z] S 1793232000-1793236500.0.stream.jsonl.gz 11586307 4b674d438d19c52d763fcd8a3dafd852a7d509db0dce8aea6cb31b7723e193a1
[2026-10-29T09:31:24Z] S 1793232000-1793237400.0.stream.jsonl.gz 10660664 a165ef62af692053180e8b84920e9b63dbdda4f2599c4e62531e5f6ca379f125
[2026-10-29T09:31:24Z] S 1793232000-1793238300.0.stream.jsonl.gz 10776660 b412acf84336b17ffd7722035c2ea162dd1d40cf0199e27e74e97ea939f77f6f
[2026-10-29T09:31:24Z] S 1793232000-1793239200.0.stream.jsonl.gz 10626770 10a349f090734e3edfa6b57293ab0792e3be068f003fd282cd21d016f1191329
[2026-10-29T09:31:24Z] S 1793232000-1793240100.0.stream.jsonl.gz 9792424 9af6e8ce44bfb351dec406b7238800bcfd9e1c923eda19108ee90f932d1ccd77
[2026-10-29T09:31:24Z] S 1793232000-1793241000.0.stream.jsonl.gz 10745728 97af9463ab66cb91cb988edb643ed299242b31b1a178a127a329bc519553656c
[2026-10-29T09:31:24Z] S 1793232000-1793241900.0.stream.jsonl.gz 11272730 56523b9b4864aa1d68356887683b08e62cc114356a412b912d0a48f1cb71cce9
[2026-10-29T09:31:24Z] S 1793232000-1793242800.0.stream.jsonl.gz 9774209 0ea58656eab189fc7fe4c12f19565ae1f8e78a16914e4556077ee7357dd66bf8
[2026-10-29T09:31:24Z] S 1793232000-1793243700.0.stream.jsonl.gz 9321701 351bc4fb1ecaddc7a7d7706b8c0bdf9dae2c923bff1587739c0b25b84dc27dce
[2026-10-29T09:31:24Z] S 1793232000-1793244600.0.stream.jsonl.gz 10295145 4c5ea876926595b876b57674ed22ac762dee89bd562b31b41ca1b46c8d8f0941
[2026-10-29T09:31:24Z] S 1793232000-1793245500.0.stream.jsonl.gz 10434441 965536189680879129c4b791b2ce4e3f2d6f7b4afc652e3667f4f26badfffe5c
[2026-10-29T09:31:24Z] S 1793232000-1793246400.0.stream.jsonl.gz 11156773 aa32bc8025e820129068a744811070c5d22a99fbee05f075c224ebdd6acdbee0
[2026-10-29T09:31:24Z] S 1793232000-1793247300.0.stream.jsonl.gz 11456592 01702655f10a63f295b19dfeb9d0ba9b88c3c9ce31d44a9a8f2c08fe62cd00dd
[2026-10-29T09:31:24Z] S 1793232000-1793248200.0.stream.jsonl.gz 11804877 2aae850163314c07ec63ef9432003a577595c5d8d9e14fe6477a3dd22aa6b1ac
[2026-10-29T09:31:24Z] S 1793232000-1793249100.0.stream.jsonl.gz 11704215 7956e72362c84c21af181ca4735693b0a46f140ffd8bb873cac388937b2d990f
[2026-10-29T09:31:24Z] S 1793232000-1793250000.0.stream.jsonl.gz 9914992 c7a1c8ac59d83e2c523000877d723b086dcea022249cc5ac8473b01e29328402
[2026-10-29T09:31:24Z] S 1793232000-1793250900.0.stream.jsonl.gz 10553162 2881a9c50f4ed4779dd38d087a5bdf08c0a0b615388d99903d3f521f41eff5d8
[2026-10-29T09:31:24Z] S 1793232000-1793251800.0.stream.jsonl.gz 6547939 665482155d2c89d4d90d723481ade034d3fa140f3fecb1c9f763955265058b0e
[2026-10-29T09:31:24Z] S 1793232000-1793252700.0.stream.jsonl.gz 6710655 1ae001465bda15ecb0baac234006e6a6caeb300d3b4af38e03836ad74911d9b6
[2026-10-29T09:31:24Z] S 1793232000-1793253600.0.stream.jsonl.gz 10468900 abacdc803e50c358dcbb303c389571da57f2ee9f9d53e15b2d55c97ad40f3c3f
[2026-10-29T09:31:24Z] S 1793232000-1793254500.0.stream.jsonl.gz 11330444 ecbbccb1a14d1930a4896d80cdaf1ab6d2b7fd1acfe89d44890f217520eaff7b
[2026-10-29T09:31:24Z] S 1793232000-1793255400.0.stream.jsonl.gz 10581288 e4639bf5a1fa0c5cf5e34da606963fe376f9c1c151c944c01ca5456a8b6cc496
[2026-10-29T09:31:24Z] S 1793232000-1793256300.0.stream.jsonl.gz 9852787 86979d6d01fbf239cbc6e10601b10b55cff7ef99c19ed624b395f459fce20c96
[2026-10-29T09:31:24Z] S 1793232000-1793257200.0.stream.jsonl.gz 12148871 ab604e14fa82be607598b858b7cd069d9c79fc1ecbbb38c80b0b104556062abd
[2026-10-29T09:31:24Z] S 1793232000-1793258100.0.stream.jsonl.gz 13568827 ff1db96bb157f72ab0c6d2a33fc8b950d9cda13c2cdbc95cd748b4175652bfe4
[2026-10-29T09:31:24Z] S 1793232000-1793259000.0.stream.jsonl.gz 11991341 6897e0b6bb2b55df7d152556adf5134ea8e5365034dcc15ddbca00bcef9f701b
[2026-10-29T09:31:24Z] S 1793232000-1793259900.0.stream.jsonl.gz 12726821 0d22a5647d7636d7caa05eec6d0fb692b5d68cff96459799bfa2acb8579644e3
[2026-10-29T09:31:24Z] S 1793232000-1793260800.0.stream.jsonl.gz 14804505 b839cd4c19f7851e7493c2cabe48e8c40b8bf08a97fc1a3363c52d92c176efdf
[2026-10-29T09:31:24Z] S 1793232000-1793261700.0.stream.jsonl.gz 12815998 8f724133bc113ff6d30bc03d266711ca940aa0ccb4f244674566f14623556a08
[2026-10-29T09:31:24Z] S 1793232000-1793262600.0.stream.jsonl.gz 14933789 9c3aa5375f8405416226c860be5b8af5904b3a786c390271296e034260e5af25
[2026-10-29T09:31:24Z] G-SET: 86 files, 890975956 bytes, slots 1793187000 to 1793262600, as of 1793263627, deferred 0; set.json sha256 f3450db0742d155b3e5487cdbde9d0bdf3877661c4c12fc962dcccd7981e7f3e; the store after the run holds 0 stream files of slots due by A - 0 of slots the set records closed, 0 of slots it does not record; slots whose slot.json is not as recorded []
[2026-10-29T09:31:25Z] G-UPLOAD: Release 427629503, 86 of 86 assets by name, bytes, state and digest, 0 missing, 0 beyond; the tag rewardbook-streams-1793263627 at 6a615257277d3c94dafd4d39783499560a344648
[2026-10-29T09:31:25Z] G-DOWNLOAD: verify.json sha256 dad6b5783342c244dcc7fb8d5540b8c6176c809c4a1dd9204a3cc2eb6c6c4379, 86 of 86 downloads equal, 890975956 bytes
[2026-10-29T09:31:25Z] ROW 1793145600-1793187000.0.stream.jsonl.gz 9629579 121ae8ad5aaffa260737f6d5ea469e4792e7d7793f7db604e4f6152bc7504916 digest sha256:121ae8ad5aaffa260737f6d5ea469e4792e7d7793f7db604e4f6152bc7504916 download 121ae8ad5aaffa260737f6d5ea469e4792e7d7793f7db604e4f6152bc7504916 removed 121ae8ad5aaffa260737f6d5ea469e4792e7d7793f7db604e4f6152bc7504916
[2026-10-29T09:31:25Z] ROW 1793145600-1793187900.0.stream.jsonl.gz 9639138 37ad0796a091fb6a9b088c0c266d0cbbd88e104c670d8efd33c670c4abf2a823 digest sha256:37ad0796a091fb6a9b088c0c266d0cbbd88e104c670d8efd33c670c4abf2a823 download 37ad0796a091fb6a9b088c0c266d0cbbd88e104c670d8efd33c670c4abf2a823 removed 37ad0796a091fb6a9b088c0c266d0cbbd88e104c670d8efd33c670c4abf2a823
[2026-10-29T09:31:25Z] ROW 1793145600-1793188800.0.stream.jsonl.gz 10430786 ad85da3abf58feedae79d68ebfb8d0a402f25acd40459d96f28ea9a47c70bb96 digest sha256:ad85da3abf58feedae79d68ebfb8d0a402f25acd40459d96f28ea9a47c70bb96 download ad85da3abf58feedae79d68ebfb8d0a402f25acd40459d96f28ea9a47c70bb96 removed ad85da3abf58feedae79d68ebfb8d0a402f25acd40459d96f28ea9a47c70bb96
[2026-10-29T09:31:25Z] ROW 1793145600-1793189700.0.stream.jsonl.gz 10844068 c91f3297a636a3e239bfa529c3804cf626f66765c5b3256afe04c1a301061039 digest sha256:c91f3297a636a3e239bfa529c3804cf626f66765c5b3256afe04c1a301061039 download c91f3297a636a3e239bfa529c3804cf626f66765c5b3256afe04c1a301061039 removed c91f3297a636a3e239bfa529c3804cf626f66765c5b3256afe04c1a301061039
[2026-10-29T09:31:25Z] ROW 1793145600-1793190600.0.stream.jsonl.gz 11422263 ab9b26074465807668fd298a824ec53d5bf3678ea7452b37ab44ea2f3d145d5f digest sha256:ab9b26074465807668fd298a824ec53d5bf3678ea7452b37ab44ea2f3d145d5f download ab9b26074465807668fd298a824ec53d5bf3678ea7452b37ab44ea2f3d145d5f removed ab9b26074465807668fd298a824ec53d5bf3678ea7452b37ab44ea2f3d145d5f
[2026-10-29T09:31:25Z] ROW 1793145600-1793191500.0.stream.jsonl.gz 8669289 4aff733af5bc9e08e2996011967bab6fc0a58bb5230961f7fcc3f488d4fc7f6e digest sha256:4aff733af5bc9e08e2996011967bab6fc0a58bb5230961f7fcc3f488d4fc7f6e download 4aff733af5bc9e08e2996011967bab6fc0a58bb5230961f7fcc3f488d4fc7f6e removed 4aff733af5bc9e08e2996011967bab6fc0a58bb5230961f7fcc3f488d4fc7f6e
[2026-10-29T09:31:25Z] ROW 1793145600-1793191500.1.stream.jsonl.gz 2824343 7bfe046788a1f35db8bf621b1608b3262bb7405340ca88931bd74b821c501f1f digest sha256:7bfe046788a1f35db8bf621b1608b3262bb7405340ca88931bd74b821c501f1f download 7bfe046788a1f35db8bf621b1608b3262bb7405340ca88931bd74b821c501f1f removed 7bfe046788a1f35db8bf621b1608b3262bb7405340ca88931bd74b821c501f1f
[2026-10-29T09:31:25Z] ROW 1793145600-1793192400.0.stream.jsonl.gz 11723039 8028f8a9d828d6c1e94d383faae0d68af94675d1f2ba57a568ec34962bd6e06b digest sha256:8028f8a9d828d6c1e94d383faae0d68af94675d1f2ba57a568ec34962bd6e06b download 8028f8a9d828d6c1e94d383faae0d68af94675d1f2ba57a568ec34962bd6e06b removed 8028f8a9d828d6c1e94d383faae0d68af94675d1f2ba57a568ec34962bd6e06b
[2026-10-29T09:31:25Z] ROW 1793145600-1793193300.0.stream.jsonl.gz 10919554 0d49767ed12888f2994c6e6e8a8ecdd6a2d540713db437bb46c8c73a97718275 digest sha256:0d49767ed12888f2994c6e6e8a8ecdd6a2d540713db437bb46c8c73a97718275 download 0d49767ed12888f2994c6e6e8a8ecdd6a2d540713db437bb46c8c73a97718275 removed 0d49767ed12888f2994c6e6e8a8ecdd6a2d540713db437bb46c8c73a97718275
[2026-10-29T09:31:25Z] ROW 1793145600-1793194200.0.stream.jsonl.gz 9958510 a61297412d0223c0dd827965661a609463b26136d71bc0bb403723491b871d9a digest sha256:a61297412d0223c0dd827965661a609463b26136d71bc0bb403723491b871d9a download a61297412d0223c0dd827965661a609463b26136d71bc0bb403723491b871d9a removed a61297412d0223c0dd827965661a609463b26136d71bc0bb403723491b871d9a
[2026-10-29T09:31:25Z] ROW 1793145600-1793195100.0.stream.jsonl.gz 10225257 10fd14580576dcf7d2ba5b34377db1c0ab94909089504afdf4e3b831958fe731 digest sha256:10fd14580576dcf7d2ba5b34377db1c0ab94909089504afdf4e3b831958fe731 download 10fd14580576dcf7d2ba5b34377db1c0ab94909089504afdf4e3b831958fe731 removed 10fd14580576dcf7d2ba5b34377db1c0ab94909089504afdf4e3b831958fe731
[2026-10-29T09:31:25Z] ROW 1793145600-1793196000.0.stream.jsonl.gz 9759422 e8765455d1f1f783288f086027d3b198cf31741944bd5a188b22565345983481 digest sha256:e8765455d1f1f783288f086027d3b198cf31741944bd5a188b22565345983481 download e8765455d1f1f783288f086027d3b198cf31741944bd5a188b22565345983481 removed e8765455d1f1f783288f086027d3b198cf31741944bd5a188b22565345983481
[2026-10-29T09:31:25Z] ROW 1793145600-1793196900.0.stream.jsonl.gz 9780710 88c2c84708ab437c4fe5fce3f84776211e62fd1dd5af70fdba40f1894897bdd0 digest sha256:88c2c84708ab437c4fe5fce3f84776211e62fd1dd5af70fdba40f1894897bdd0 download 88c2c84708ab437c4fe5fce3f84776211e62fd1dd5af70fdba40f1894897bdd0 removed 88c2c84708ab437c4fe5fce3f84776211e62fd1dd5af70fdba40f1894897bdd0
[2026-10-29T09:31:25Z] ROW 1793145600-1793197800.0.stream.jsonl.gz 9880467 a5d99308e054693a039d9ee64579ca5015652f140ff1fdd9dac8e9cb72e4eb3a digest sha256:a5d99308e054693a039d9ee64579ca5015652f140ff1fdd9dac8e9cb72e4eb3a download a5d99308e054693a039d9ee64579ca5015652f140ff1fdd9dac8e9cb72e4eb3a removed a5d99308e054693a039d9ee64579ca5015652f140ff1fdd9dac8e9cb72e4eb3a
[2026-10-29T09:31:25Z] ROW 1793145600-1793198700.0.stream.jsonl.gz 11208381 075da9e7c5a711a1c555cf14c07cdadc4121ac49e6355d05b7f9e7875094af61 digest sha256:075da9e7c5a711a1c555cf14c07cdadc4121ac49e6355d05b7f9e7875094af61 download 075da9e7c5a711a1c555cf14c07cdadc4121ac49e6355d05b7f9e7875094af61 removed 075da9e7c5a711a1c555cf14c07cdadc4121ac49e6355d05b7f9e7875094af61
[2026-10-29T09:31:25Z] ROW 1793145600-1793199600.0.stream.jsonl.gz 12025155 c70cf12a975796105a875b8f8d7a73682ec557cd30ffd0dd0f051ae2ea90adc3 digest sha256:c70cf12a975796105a875b8f8d7a73682ec557cd30ffd0dd0f051ae2ea90adc3 download c70cf12a975796105a875b8f8d7a73682ec557cd30ffd0dd0f051ae2ea90adc3 removed c70cf12a975796105a875b8f8d7a73682ec557cd30ffd0dd0f051ae2ea90adc3
[2026-10-29T09:31:25Z] ROW 1793145600-1793200500.0.stream.jsonl.gz 10028151 8a2b4f911f7467b3ce3c5088829e499cc72a6d647128f7587c2d1f700ebf0558 digest sha256:8a2b4f911f7467b3ce3c5088829e499cc72a6d647128f7587c2d1f700ebf0558 download 8a2b4f911f7467b3ce3c5088829e499cc72a6d647128f7587c2d1f700ebf0558 removed 8a2b4f911f7467b3ce3c5088829e499cc72a6d647128f7587c2d1f700ebf0558
[2026-10-29T09:31:25Z] ROW 1793145600-1793201400.0.stream.jsonl.gz 10684034 99341832a61bf589521a253a863d94db68526d8a53114d0a855917b354e8a896 digest sha256:99341832a61bf589521a253a863d94db68526d8a53114d0a855917b354e8a896 download 99341832a61bf589521a253a863d94db68526d8a53114d0a855917b354e8a896 removed 99341832a61bf589521a253a863d94db68526d8a53114d0a855917b354e8a896
[2026-10-29T09:31:25Z] ROW 1793145600-1793202300.0.stream.jsonl.gz 10156189 ec78fb31112d645c9c08ded59c6befd6277bdfb7e260723c9340467f5b3fcea7 digest sha256:ec78fb31112d645c9c08ded59c6befd6277bdfb7e260723c9340467f5b3fcea7 download ec78fb31112d645c9c08ded59c6befd6277bdfb7e260723c9340467f5b3fcea7 removed ec78fb31112d645c9c08ded59c6befd6277bdfb7e260723c9340467f5b3fcea7
[2026-10-29T09:31:25Z] ROW 1793145600-1793203200.0.stream.jsonl.gz 10279670 5c10b99de3ca84f6d0cd4fd556fa530483c301e1bf3c7bb80114eef519ebd1bc digest sha256:5c10b99de3ca84f6d0cd4fd556fa530483c301e1bf3c7bb80114eef519ebd1bc download 5c10b99de3ca84f6d0cd4fd556fa530483c301e1bf3c7bb80114eef519ebd1bc removed 5c10b99de3ca84f6d0cd4fd556fa530483c301e1bf3c7bb80114eef519ebd1bc
[2026-10-29T09:31:25Z] ROW 1793145600-1793204100.0.stream.jsonl.gz 9536875 ffbc1876095b1ca7ca17b218892d8b42c3bb918183eca7b7827d7de25ec768f5 digest sha256:ffbc1876095b1ca7ca17b218892d8b42c3bb918183eca7b7827d7de25ec768f5 download ffbc1876095b1ca7ca17b218892d8b42c3bb918183eca7b7827d7de25ec768f5 removed ffbc1876095b1ca7ca17b218892d8b42c3bb918183eca7b7827d7de25ec768f5
[2026-10-29T09:31:25Z] ROW 1793145600-1793205000.0.stream.jsonl.gz 10141202 b38c8fd1d01f0fa20fe38b26a94255344e296c83b509640bee279dcad5deff16 digest sha256:b38c8fd1d01f0fa20fe38b26a94255344e296c83b509640bee279dcad5deff16 download b38c8fd1d01f0fa20fe38b26a94255344e296c83b509640bee279dcad5deff16 removed b38c8fd1d01f0fa20fe38b26a94255344e296c83b509640bee279dcad5deff16
[2026-10-29T09:31:25Z] ROW 1793145600-1793205900.0.stream.jsonl.gz 9715061 0afde34b6cf80083b9cdda7bef5baacfa1dc946f61e68886265cb3633f3a3538 digest sha256:0afde34b6cf80083b9cdda7bef5baacfa1dc946f61e68886265cb3633f3a3538 download 0afde34b6cf80083b9cdda7bef5baacfa1dc946f61e68886265cb3633f3a3538 removed 0afde34b6cf80083b9cdda7bef5baacfa1dc946f61e68886265cb3633f3a3538
[2026-10-29T09:31:25Z] ROW 1793145600-1793206800.0.stream.jsonl.gz 11001064 e9f2f8a8ff6cef04b36b04cbffaaed9b5accf26873d26eed74b85d8dc6199378 digest sha256:e9f2f8a8ff6cef04b36b04cbffaaed9b5accf26873d26eed74b85d8dc6199378 download e9f2f8a8ff6cef04b36b04cbffaaed9b5accf26873d26eed74b85d8dc6199378 removed e9f2f8a8ff6cef04b36b04cbffaaed9b5accf26873d26eed74b85d8dc6199378
[2026-10-29T09:31:25Z] ROW 1793145600-1793207700.0.stream.jsonl.gz 9835502 6eec69739f70d0ac95fa8735d2154567794477b47cc5d9d43f2bfac27bedcc99 digest sha256:6eec69739f70d0ac95fa8735d2154567794477b47cc5d9d43f2bfac27bedcc99 download 6eec69739f70d0ac95fa8735d2154567794477b47cc5d9d43f2bfac27bedcc99 removed 6eec69739f70d0ac95fa8735d2154567794477b47cc5d9d43f2bfac27bedcc99
[2026-10-29T09:31:25Z] ROW 1793145600-1793208600.0.stream.jsonl.gz 9874421 1084bd093c165ef45f8cbce038465b4a5fcb395d435ef7556d05d85f08169ce5 digest sha256:1084bd093c165ef45f8cbce038465b4a5fcb395d435ef7556d05d85f08169ce5 download 1084bd093c165ef45f8cbce038465b4a5fcb395d435ef7556d05d85f08169ce5 removed 1084bd093c165ef45f8cbce038465b4a5fcb395d435ef7556d05d85f08169ce5
[2026-10-29T09:31:25Z] ROW 1793145600-1793209500.0.stream.jsonl.gz 9385489 09177e12607a802d3aac38cdf988ec17229af4238b4a87a55224d75117561d73 digest sha256:09177e12607a802d3aac38cdf988ec17229af4238b4a87a55224d75117561d73 download 09177e12607a802d3aac38cdf988ec17229af4238b4a87a55224d75117561d73 removed 09177e12607a802d3aac38cdf988ec17229af4238b4a87a55224d75117561d73
[2026-10-29T09:31:25Z] ROW 1793145600-1793210400.0.stream.jsonl.gz 10966063 b10381fa9dc7552d8d16e2b480baeb4f6ff30651921c3b89323a0659d8955d58 digest sha256:b10381fa9dc7552d8d16e2b480baeb4f6ff30651921c3b89323a0659d8955d58 download b10381fa9dc7552d8d16e2b480baeb4f6ff30651921c3b89323a0659d8955d58 removed b10381fa9dc7552d8d16e2b480baeb4f6ff30651921c3b89323a0659d8955d58
[2026-10-29T09:31:25Z] ROW 1793145600-1793211300.0.stream.jsonl.gz 10551024 fd8659f6bf0eaba31206970e69ba9f5b0a915c804e73a0dba9815a35dbb90bd7 digest sha256:fd8659f6bf0eaba31206970e69ba9f5b0a915c804e73a0dba9815a35dbb90bd7 download fd8659f6bf0eaba31206970e69ba9f5b0a915c804e73a0dba9815a35dbb90bd7 removed fd8659f6bf0eaba31206970e69ba9f5b0a915c804e73a0dba9815a35dbb90bd7
[2026-10-29T09:31:25Z] ROW 1793145600-1793212200.0.stream.jsonl.gz 12372196 a4e4aa901676ac2ad3585b6cbc7edc0349ed0fffa7e41a744ab602c954738485 digest sha256:a4e4aa901676ac2ad3585b6cbc7edc0349ed0fffa7e41a744ab602c954738485 download a4e4aa901676ac2ad3585b6cbc7edc0349ed0fffa7e41a744ab602c954738485 removed a4e4aa901676ac2ad3585b6cbc7edc0349ed0fffa7e41a744ab602c954738485
[2026-10-29T09:31:25Z] ROW 1793145600-1793213100.0.stream.jsonl.gz 11112191 17b2340abe0d5466dc70c8584c970feb094a07f2ca5d534aae2d4459520efd65 digest sha256:17b2340abe0d5466dc70c8584c970feb094a07f2ca5d534aae2d4459520efd65 download 17b2340abe0d5466dc70c8584c970feb094a07f2ca5d534aae2d4459520efd65 removed 17b2340abe0d5466dc70c8584c970feb094a07f2ca5d534aae2d4459520efd65
[2026-10-29T09:31:25Z] ROW 1793145600-1793214000.0.stream.jsonl.gz 10918172 9e3d0b9f03b4cbd00834375385767f370ee4a479fd0c1ca54c40052213cce5a5 digest sha256:9e3d0b9f03b4cbd00834375385767f370ee4a479fd0c1ca54c40052213cce5a5 download 9e3d0b9f03b4cbd00834375385767f370ee4a479fd0c1ca54c40052213cce5a5 removed 9e3d0b9f03b4cbd00834375385767f370ee4a479fd0c1ca54c40052213cce5a5
[2026-10-29T09:31:25Z] ROW 1793145600-1793214900.0.stream.jsonl.gz 10956690 d70fe0f958eb08281fb8c3cf74567121bafeffadc272afebb3b973938eedeba9 digest sha256:d70fe0f958eb08281fb8c3cf74567121bafeffadc272afebb3b973938eedeba9 download d70fe0f958eb08281fb8c3cf74567121bafeffadc272afebb3b973938eedeba9 removed d70fe0f958eb08281fb8c3cf74567121bafeffadc272afebb3b973938eedeba9
[2026-10-29T09:31:25Z] ROW 1793145600-1793215800.0.stream.jsonl.gz 10464479 7f48547a7aa076d1133ab3ffc013aa90a2f0f464eefd55f474c6de7482af44b0 digest sha256:7f48547a7aa076d1133ab3ffc013aa90a2f0f464eefd55f474c6de7482af44b0 download 7f48547a7aa076d1133ab3ffc013aa90a2f0f464eefd55f474c6de7482af44b0 removed 7f48547a7aa076d1133ab3ffc013aa90a2f0f464eefd55f474c6de7482af44b0
[2026-10-29T09:31:25Z] ROW 1793145600-1793216700.0.stream.jsonl.gz 11797234 87f3efd83e33c5ffe9e9b035a4c5b090b645462a68b0f96645818f91f2997faf digest sha256:87f3efd83e33c5ffe9e9b035a4c5b090b645462a68b0f96645818f91f2997faf download 87f3efd83e33c5ffe9e9b035a4c5b090b645462a68b0f96645818f91f2997faf removed 87f3efd83e33c5ffe9e9b035a4c5b090b645462a68b0f96645818f91f2997faf
[2026-10-29T09:31:25Z] ROW 1793145600-1793217600.0.stream.jsonl.gz 9947721 1ca2fac80bb178ad476eb69bcf3a26f90fc6c25af5715df82672dd8de84107c0 digest sha256:1ca2fac80bb178ad476eb69bcf3a26f90fc6c25af5715df82672dd8de84107c0 download 1ca2fac80bb178ad476eb69bcf3a26f90fc6c25af5715df82672dd8de84107c0 removed 1ca2fac80bb178ad476eb69bcf3a26f90fc6c25af5715df82672dd8de84107c0
[2026-10-29T09:31:25Z] ROW 1793145600-1793218500.0.stream.jsonl.gz 9342830 70c9bd544e19d236188538cc43cd89663cd327d6bd516ef442e01ff89f59508a digest sha256:70c9bd544e19d236188538cc43cd89663cd327d6bd516ef442e01ff89f59508a download 70c9bd544e19d236188538cc43cd89663cd327d6bd516ef442e01ff89f59508a removed 70c9bd544e19d236188538cc43cd89663cd327d6bd516ef442e01ff89f59508a
[2026-10-29T09:31:25Z] ROW 1793145600-1793219400.0.stream.jsonl.gz 8879554 07b12705033d39a7a84982ea7e311d31522b0e4ab09580a5868c83f17c054186 digest sha256:07b12705033d39a7a84982ea7e311d31522b0e4ab09580a5868c83f17c054186 download 07b12705033d39a7a84982ea7e311d31522b0e4ab09580a5868c83f17c054186 removed 07b12705033d39a7a84982ea7e311d31522b0e4ab09580a5868c83f17c054186
[2026-10-29T09:31:25Z] ROW 1793145600-1793220300.0.stream.jsonl.gz 9062207 0154c6a783d139f1532ec09d9060da71cfd1254552aacfb75ed385f7799d4006 digest sha256:0154c6a783d139f1532ec09d9060da71cfd1254552aacfb75ed385f7799d4006 download 0154c6a783d139f1532ec09d9060da71cfd1254552aacfb75ed385f7799d4006 removed 0154c6a783d139f1532ec09d9060da71cfd1254552aacfb75ed385f7799d4006
[2026-10-29T09:31:25Z] ROW 1793145600-1793221200.0.stream.jsonl.gz 9372847 57bf808b26b559fdf9f211e59a761fac1f9b8c2dfda86bc3723f984eb5914a08 digest sha256:57bf808b26b559fdf9f211e59a761fac1f9b8c2dfda86bc3723f984eb5914a08 download 57bf808b26b559fdf9f211e59a761fac1f9b8c2dfda86bc3723f984eb5914a08 removed 57bf808b26b559fdf9f211e59a761fac1f9b8c2dfda86bc3723f984eb5914a08
[2026-10-29T09:31:25Z] ROW 1793145600-1793222100.0.stream.jsonl.gz 8001926 18c0bdb9008b4b40471b5b99a4ddc854c5e6b1f39d9659f479b252a69a8884be digest sha256:18c0bdb9008b4b40471b5b99a4ddc854c5e6b1f39d9659f479b252a69a8884be download 18c0bdb9008b4b40471b5b99a4ddc854c5e6b1f39d9659f479b252a69a8884be removed 18c0bdb9008b4b40471b5b99a4ddc854c5e6b1f39d9659f479b252a69a8884be
[2026-10-29T09:31:25Z] ROW 1793145600-1793223000.0.stream.jsonl.gz 8114414 f6101c8eb420b9eda97f353d7adcebdc355fbec4bb93ff6a69b6cab57adcaed6 digest sha256:f6101c8eb420b9eda97f353d7adcebdc355fbec4bb93ff6a69b6cab57adcaed6 download f6101c8eb420b9eda97f353d7adcebdc355fbec4bb93ff6a69b6cab57adcaed6 removed f6101c8eb420b9eda97f353d7adcebdc355fbec4bb93ff6a69b6cab57adcaed6
[2026-10-29T09:31:25Z] ROW 1793145600-1793223900.0.stream.jsonl.gz 9006052 86ef7ae2e14ac60b9b57edc530427e2fb33d0a481aa315799106c43e59c0e0e0 digest sha256:86ef7ae2e14ac60b9b57edc530427e2fb33d0a481aa315799106c43e59c0e0e0 download 86ef7ae2e14ac60b9b57edc530427e2fb33d0a481aa315799106c43e59c0e0e0 removed 86ef7ae2e14ac60b9b57edc530427e2fb33d0a481aa315799106c43e59c0e0e0
[2026-10-29T09:31:25Z] ROW 1793145600-1793224800.0.stream.jsonl.gz 8661025 752e54df1a8237873fa10a40e759b042763c89cb5b87d745b89949d3f20b2e0e digest sha256:752e54df1a8237873fa10a40e759b042763c89cb5b87d745b89949d3f20b2e0e download 752e54df1a8237873fa10a40e759b042763c89cb5b87d745b89949d3f20b2e0e removed 752e54df1a8237873fa10a40e759b042763c89cb5b87d745b89949d3f20b2e0e
[2026-10-29T09:31:25Z] ROW 1793145600-1793225700.0.stream.jsonl.gz 8132267 9485eb5864c99e37e00d178bd4312b6ef4dc779694a5e4de480941b41bb88297 digest sha256:9485eb5864c99e37e00d178bd4312b6ef4dc779694a5e4de480941b41bb88297 download 9485eb5864c99e37e00d178bd4312b6ef4dc779694a5e4de480941b41bb88297 removed 9485eb5864c99e37e00d178bd4312b6ef4dc779694a5e4de480941b41bb88297
[2026-10-29T09:31:25Z] ROW 1793145600-1793226600.0.stream.jsonl.gz 9326449 2cdeb8ca3f85fca93e521e3a2151e6d95c5a24d19c61d58e87cec47b18696819 digest sha256:2cdeb8ca3f85fca93e521e3a2151e6d95c5a24d19c61d58e87cec47b18696819 download 2cdeb8ca3f85fca93e521e3a2151e6d95c5a24d19c61d58e87cec47b18696819 removed 2cdeb8ca3f85fca93e521e3a2151e6d95c5a24d19c61d58e87cec47b18696819
[2026-10-29T09:31:25Z] ROW 1793145600-1793227500.0.stream.jsonl.gz 9815975 ec2d3c0868e6d21c3754d1c290895c080a46c58048103ecb37ede7d4b8edfc3e digest sha256:ec2d3c0868e6d21c3754d1c290895c080a46c58048103ecb37ede7d4b8edfc3e download ec2d3c0868e6d21c3754d1c290895c080a46c58048103ecb37ede7d4b8edfc3e removed ec2d3c0868e6d21c3754d1c290895c080a46c58048103ecb37ede7d4b8edfc3e
[2026-10-29T09:31:25Z] ROW 1793145600-1793228400.0.stream.jsonl.gz 9231800 fef35a594b2704d0984f9bc737782ea2bc46b5f264d0712d9df2c10ffa97924b digest sha256:fef35a594b2704d0984f9bc737782ea2bc46b5f264d0712d9df2c10ffa97924b download fef35a594b2704d0984f9bc737782ea2bc46b5f264d0712d9df2c10ffa97924b removed fef35a594b2704d0984f9bc737782ea2bc46b5f264d0712d9df2c10ffa97924b
[2026-10-29T09:31:25Z] ROW 1793145600-1793229300.0.stream.jsonl.gz 8160699 7ef7d872fc56eeeb309f156a13f8ae10ed68aeeb1b545a566ca7f3a4e4e5e994 digest sha256:7ef7d872fc56eeeb309f156a13f8ae10ed68aeeb1b545a566ca7f3a4e4e5e994 download 7ef7d872fc56eeeb309f156a13f8ae10ed68aeeb1b545a566ca7f3a4e4e5e994 removed 7ef7d872fc56eeeb309f156a13f8ae10ed68aeeb1b545a566ca7f3a4e4e5e994
[2026-10-29T09:31:25Z] ROW 1793145600-1793230200.0.stream.jsonl.gz 8889088 c2b14f9702d26b6853601d83b685113b6f5650d2b86c644724e87d1f619eec17 digest sha256:c2b14f9702d26b6853601d83b685113b6f5650d2b86c644724e87d1f619eec17 download c2b14f9702d26b6853601d83b685113b6f5650d2b86c644724e87d1f619eec17 removed c2b14f9702d26b6853601d83b685113b6f5650d2b86c644724e87d1f619eec17
[2026-10-29T09:31:25Z] ROW 1793145600-1793231100.0.stream.jsonl.gz 9143917 e177b5e38f162522be08df4692d8789e36a8a8a83ee5cf9856940a05dbaf955a digest sha256:e177b5e38f162522be08df4692d8789e36a8a8a83ee5cf9856940a05dbaf955a download e177b5e38f162522be08df4692d8789e36a8a8a83ee5cf9856940a05dbaf955a removed e177b5e38f162522be08df4692d8789e36a8a8a83ee5cf9856940a05dbaf955a
[2026-10-29T09:31:25Z] ROW 1793232000-1793232000.0.stream.jsonl.gz 11579610 bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f digest sha256:bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f download bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f removed bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f
[2026-10-29T09:31:25Z] ROW 1793232000-1793232900.0.stream.jsonl.gz 10715152 46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370 digest sha256:46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370 download 46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370 removed 46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370
[2026-10-29T09:31:25Z] ROW 1793232000-1793233800.0.stream.jsonl.gz 11443056 2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9 digest sha256:2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9 download 2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9 removed 2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9
[2026-10-29T09:31:25Z] ROW 1793232000-1793234700.0.stream.jsonl.gz 13592154 ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496 digest sha256:ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496 download ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496 removed ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496
[2026-10-29T09:31:25Z] ROW 1793232000-1793235600.0.stream.jsonl.gz 11481990 13cfa07ef0b2a4b17c6dfd8a73acb7124fcaaab9efcc0630e3b35075c6a68806 digest sha256:13cfa07ef0b2a4b17c6dfd8a73acb7124fcaaab9efcc0630e3b35075c6a68806 download 13cfa07ef0b2a4b17c6dfd8a73acb7124fcaaab9efcc0630e3b35075c6a68806 removed 13cfa07ef0b2a4b17c6dfd8a73acb7124fcaaab9efcc0630e3b35075c6a68806
[2026-10-29T09:31:25Z] ROW 1793232000-1793236500.0.stream.jsonl.gz 11586307 4b674d438d19c52d763fcd8a3dafd852a7d509db0dce8aea6cb31b7723e193a1 digest sha256:4b674d438d19c52d763fcd8a3dafd852a7d509db0dce8aea6cb31b7723e193a1 download 4b674d438d19c52d763fcd8a3dafd852a7d509db0dce8aea6cb31b7723e193a1 removed 4b674d438d19c52d763fcd8a3dafd852a7d509db0dce8aea6cb31b7723e193a1
[2026-10-29T09:31:25Z] ROW 1793232000-1793237400.0.stream.jsonl.gz 10660664 a165ef62af692053180e8b84920e9b63dbdda4f2599c4e62531e5f6ca379f125 digest sha256:a165ef62af692053180e8b84920e9b63dbdda4f2599c4e62531e5f6ca379f125 download a165ef62af692053180e8b84920e9b63dbdda4f2599c4e62531e5f6ca379f125 removed a165ef62af692053180e8b84920e9b63dbdda4f2599c4e62531e5f6ca379f125
[2026-10-29T09:31:25Z] ROW 1793232000-1793238300.0.stream.jsonl.gz 10776660 b412acf84336b17ffd7722035c2ea162dd1d40cf0199e27e74e97ea939f77f6f digest sha256:b412acf84336b17ffd7722035c2ea162dd1d40cf0199e27e74e97ea939f77f6f download b412acf84336b17ffd7722035c2ea162dd1d40cf0199e27e74e97ea939f77f6f removed b412acf84336b17ffd7722035c2ea162dd1d40cf0199e27e74e97ea939f77f6f
[2026-10-29T09:31:25Z] ROW 1793232000-1793239200.0.stream.jsonl.gz 10626770 10a349f090734e3edfa6b57293ab0792e3be068f003fd282cd21d016f1191329 digest sha256:10a349f090734e3edfa6b57293ab0792e3be068f003fd282cd21d016f1191329 download 10a349f090734e3edfa6b57293ab0792e3be068f003fd282cd21d016f1191329 removed 10a349f090734e3edfa6b57293ab0792e3be068f003fd282cd21d016f1191329
[2026-10-29T09:31:25Z] ROW 1793232000-1793240100.0.stream.jsonl.gz 9792424 9af6e8ce44bfb351dec406b7238800bcfd9e1c923eda19108ee90f932d1ccd77 digest sha256:9af6e8ce44bfb351dec406b7238800bcfd9e1c923eda19108ee90f932d1ccd77 download 9af6e8ce44bfb351dec406b7238800bcfd9e1c923eda19108ee90f932d1ccd77 removed 9af6e8ce44bfb351dec406b7238800bcfd9e1c923eda19108ee90f932d1ccd77
[2026-10-29T09:31:25Z] ROW 1793232000-1793241000.0.stream.jsonl.gz 10745728 97af9463ab66cb91cb988edb643ed299242b31b1a178a127a329bc519553656c digest sha256:97af9463ab66cb91cb988edb643ed299242b31b1a178a127a329bc519553656c download 97af9463ab66cb91cb988edb643ed299242b31b1a178a127a329bc519553656c removed 97af9463ab66cb91cb988edb643ed299242b31b1a178a127a329bc519553656c
[2026-10-29T09:31:25Z] ROW 1793232000-1793241900.0.stream.jsonl.gz 11272730 56523b9b4864aa1d68356887683b08e62cc114356a412b912d0a48f1cb71cce9 digest sha256:56523b9b4864aa1d68356887683b08e62cc114356a412b912d0a48f1cb71cce9 download 56523b9b4864aa1d68356887683b08e62cc114356a412b912d0a48f1cb71cce9 removed 56523b9b4864aa1d68356887683b08e62cc114356a412b912d0a48f1cb71cce9
[2026-10-29T09:31:25Z] ROW 1793232000-1793242800.0.stream.jsonl.gz 9774209 0ea58656eab189fc7fe4c12f19565ae1f8e78a16914e4556077ee7357dd66bf8 digest sha256:0ea58656eab189fc7fe4c12f19565ae1f8e78a16914e4556077ee7357dd66bf8 download 0ea58656eab189fc7fe4c12f19565ae1f8e78a16914e4556077ee7357dd66bf8 removed 0ea58656eab189fc7fe4c12f19565ae1f8e78a16914e4556077ee7357dd66bf8
[2026-10-29T09:31:25Z] ROW 1793232000-1793243700.0.stream.jsonl.gz 9321701 351bc4fb1ecaddc7a7d7706b8c0bdf9dae2c923bff1587739c0b25b84dc27dce digest sha256:351bc4fb1ecaddc7a7d7706b8c0bdf9dae2c923bff1587739c0b25b84dc27dce download 351bc4fb1ecaddc7a7d7706b8c0bdf9dae2c923bff1587739c0b25b84dc27dce removed 351bc4fb1ecaddc7a7d7706b8c0bdf9dae2c923bff1587739c0b25b84dc27dce
[2026-10-29T09:31:25Z] ROW 1793232000-1793244600.0.stream.jsonl.gz 10295145 4c5ea876926595b876b57674ed22ac762dee89bd562b31b41ca1b46c8d8f0941 digest sha256:4c5ea876926595b876b57674ed22ac762dee89bd562b31b41ca1b46c8d8f0941 download 4c5ea876926595b876b57674ed22ac762dee89bd562b31b41ca1b46c8d8f0941 removed 4c5ea876926595b876b57674ed22ac762dee89bd562b31b41ca1b46c8d8f0941
[2026-10-29T09:31:25Z] ROW 1793232000-1793245500.0.stream.jsonl.gz 10434441 965536189680879129c4b791b2ce4e3f2d6f7b4afc652e3667f4f26badfffe5c digest sha256:965536189680879129c4b791b2ce4e3f2d6f7b4afc652e3667f4f26badfffe5c download 965536189680879129c4b791b2ce4e3f2d6f7b4afc652e3667f4f26badfffe5c removed 965536189680879129c4b791b2ce4e3f2d6f7b4afc652e3667f4f26badfffe5c
[2026-10-29T09:31:25Z] ROW 1793232000-1793246400.0.stream.jsonl.gz 11156773 aa32bc8025e820129068a744811070c5d22a99fbee05f075c224ebdd6acdbee0 digest sha256:aa32bc8025e820129068a744811070c5d22a99fbee05f075c224ebdd6acdbee0 download aa32bc8025e820129068a744811070c5d22a99fbee05f075c224ebdd6acdbee0 removed aa32bc8025e820129068a744811070c5d22a99fbee05f075c224ebdd6acdbee0
[2026-10-29T09:31:25Z] ROW 1793232000-1793247300.0.stream.jsonl.gz 11456592 01702655f10a63f295b19dfeb9d0ba9b88c3c9ce31d44a9a8f2c08fe62cd00dd digest sha256:01702655f10a63f295b19dfeb9d0ba9b88c3c9ce31d44a9a8f2c08fe62cd00dd download 01702655f10a63f295b19dfeb9d0ba9b88c3c9ce31d44a9a8f2c08fe62cd00dd removed 01702655f10a63f295b19dfeb9d0ba9b88c3c9ce31d44a9a8f2c08fe62cd00dd
[2026-10-29T09:31:25Z] ROW 1793232000-1793248200.0.stream.jsonl.gz 11804877 2aae850163314c07ec63ef9432003a577595c5d8d9e14fe6477a3dd22aa6b1ac digest sha256:2aae850163314c07ec63ef9432003a577595c5d8d9e14fe6477a3dd22aa6b1ac download 2aae850163314c07ec63ef9432003a577595c5d8d9e14fe6477a3dd22aa6b1ac removed 2aae850163314c07ec63ef9432003a577595c5d8d9e14fe6477a3dd22aa6b1ac
[2026-10-29T09:31:25Z] ROW 1793232000-1793249100.0.stream.jsonl.gz 11704215 7956e72362c84c21af181ca4735693b0a46f140ffd8bb873cac388937b2d990f digest sha256:7956e72362c84c21af181ca4735693b0a46f140ffd8bb873cac388937b2d990f download 7956e72362c84c21af181ca4735693b0a46f140ffd8bb873cac388937b2d990f removed 7956e72362c84c21af181ca4735693b0a46f140ffd8bb873cac388937b2d990f
[2026-10-29T09:31:25Z] ROW 1793232000-1793250000.0.stream.jsonl.gz 9914992 c7a1c8ac59d83e2c523000877d723b086dcea022249cc5ac8473b01e29328402 digest sha256:c7a1c8ac59d83e2c523000877d723b086dcea022249cc5ac8473b01e29328402 download c7a1c8ac59d83e2c523000877d723b086dcea022249cc5ac8473b01e29328402 removed c7a1c8ac59d83e2c523000877d723b086dcea022249cc5ac8473b01e29328402
[2026-10-29T09:31:25Z] ROW 1793232000-1793250900.0.stream.jsonl.gz 10553162 2881a9c50f4ed4779dd38d087a5bdf08c0a0b615388d99903d3f521f41eff5d8 digest sha256:2881a9c50f4ed4779dd38d087a5bdf08c0a0b615388d99903d3f521f41eff5d8 download 2881a9c50f4ed4779dd38d087a5bdf08c0a0b615388d99903d3f521f41eff5d8 removed 2881a9c50f4ed4779dd38d087a5bdf08c0a0b615388d99903d3f521f41eff5d8
[2026-10-29T09:31:25Z] ROW 1793232000-1793251800.0.stream.jsonl.gz 6547939 665482155d2c89d4d90d723481ade034d3fa140f3fecb1c9f763955265058b0e digest sha256:665482155d2c89d4d90d723481ade034d3fa140f3fecb1c9f763955265058b0e download 665482155d2c89d4d90d723481ade034d3fa140f3fecb1c9f763955265058b0e removed 665482155d2c89d4d90d723481ade034d3fa140f3fecb1c9f763955265058b0e
[2026-10-29T09:31:25Z] ROW 1793232000-1793252700.0.stream.jsonl.gz 6710655 1ae001465bda15ecb0baac234006e6a6caeb300d3b4af38e03836ad74911d9b6 digest sha256:1ae001465bda15ecb0baac234006e6a6caeb300d3b4af38e03836ad74911d9b6 download 1ae001465bda15ecb0baac234006e6a6caeb300d3b4af38e03836ad74911d9b6 removed 1ae001465bda15ecb0baac234006e6a6caeb300d3b4af38e03836ad74911d9b6
[2026-10-29T09:31:25Z] ROW 1793232000-1793253600.0.stream.jsonl.gz 10468900 abacdc803e50c358dcbb303c389571da57f2ee9f9d53e15b2d55c97ad40f3c3f digest sha256:abacdc803e50c358dcbb303c389571da57f2ee9f9d53e15b2d55c97ad40f3c3f download abacdc803e50c358dcbb303c389571da57f2ee9f9d53e15b2d55c97ad40f3c3f removed abacdc803e50c358dcbb303c389571da57f2ee9f9d53e15b2d55c97ad40f3c3f
[2026-10-29T09:31:25Z] ROW 1793232000-1793254500.0.stream.jsonl.gz 11330444 ecbbccb1a14d1930a4896d80cdaf1ab6d2b7fd1acfe89d44890f217520eaff7b digest sha256:ecbbccb1a14d1930a4896d80cdaf1ab6d2b7fd1acfe89d44890f217520eaff7b download ecbbccb1a14d1930a4896d80cdaf1ab6d2b7fd1acfe89d44890f217520eaff7b removed ecbbccb1a14d1930a4896d80cdaf1ab6d2b7fd1acfe89d44890f217520eaff7b
[2026-10-29T09:31:25Z] ROW 1793232000-1793255400.0.stream.jsonl.gz 10581288 e4639bf5a1fa0c5cf5e34da606963fe376f9c1c151c944c01ca5456a8b6cc496 digest sha256:e4639bf5a1fa0c5cf5e34da606963fe376f9c1c151c944c01ca5456a8b6cc496 download e4639bf5a1fa0c5cf5e34da606963fe376f9c1c151c944c01ca5456a8b6cc496 removed e4639bf5a1fa0c5cf5e34da606963fe376f9c1c151c944c01ca5456a8b6cc496
[2026-10-29T09:31:25Z] ROW 1793232000-1793256300.0.stream.jsonl.gz 9852787 86979d6d01fbf239cbc6e10601b10b55cff7ef99c19ed624b395f459fce20c96 digest sha256:86979d6d01fbf239cbc6e10601b10b55cff7ef99c19ed624b395f459fce20c96 download 86979d6d01fbf239cbc6e10601b10b55cff7ef99c19ed624b395f459fce20c96 removed 86979d6d01fbf239cbc6e10601b10b55cff7ef99c19ed624b395f459fce20c96
[2026-10-29T09:31:25Z] ROW 1793232000-1793257200.0.stream.jsonl.gz 12148871 ab604e14fa82be607598b858b7cd069d9c79fc1ecbbb38c80b0b104556062abd digest sha256:ab604e14fa82be607598b858b7cd069d9c79fc1ecbbb38c80b0b104556062abd download ab604e14fa82be607598b858b7cd069d9c79fc1ecbbb38c80b0b104556062abd removed ab604e14fa82be607598b858b7cd069d9c79fc1ecbbb38c80b0b104556062abd
[2026-10-29T09:31:25Z] ROW 1793232000-1793258100.0.stream.jsonl.gz 13568827 ff1db96bb157f72ab0c6d2a33fc8b950d9cda13c2cdbc95cd748b4175652bfe4 digest sha256:ff1db96bb157f72ab0c6d2a33fc8b950d9cda13c2cdbc95cd748b4175652bfe4 download ff1db96bb157f72ab0c6d2a33fc8b950d9cda13c2cdbc95cd748b4175652bfe4 removed ff1db96bb157f72ab0c6d2a33fc8b950d9cda13c2cdbc95cd748b4175652bfe4
[2026-10-29T09:31:25Z] ROW 1793232000-1793259000.0.stream.jsonl.gz 11991341 6897e0b6bb2b55df7d152556adf5134ea8e5365034dcc15ddbca00bcef9f701b digest sha256:6897e0b6bb2b55df7d152556adf5134ea8e5365034dcc15ddbca00bcef9f701b download 6897e0b6bb2b55df7d152556adf5134ea8e5365034dcc15ddbca00bcef9f701b removed 6897e0b6bb2b55df7d152556adf5134ea8e5365034dcc15ddbca00bcef9f701b
[2026-10-29T09:31:25Z] ROW 1793232000-1793259900.0.stream.jsonl.gz 12726821 0d22a5647d7636d7caa05eec6d0fb692b5d68cff96459799bfa2acb8579644e3 digest sha256:0d22a5647d7636d7caa05eec6d0fb692b5d68cff96459799bfa2acb8579644e3 download 0d22a5647d7636d7caa05eec6d0fb692b5d68cff96459799bfa2acb8579644e3 removed 0d22a5647d7636d7caa05eec6d0fb692b5d68cff96459799bfa2acb8579644e3
[2026-10-29T09:31:25Z] ROW 1793232000-1793260800.0.stream.jsonl.gz 14804505 b839cd4c19f7851e7493c2cabe48e8c40b8bf08a97fc1a3363c52d92c176efdf digest sha256:b839cd4c19f7851e7493c2cabe48e8c40b8bf08a97fc1a3363c52d92c176efdf download b839cd4c19f7851e7493c2cabe48e8c40b8bf08a97fc1a3363c52d92c176efdf removed b839cd4c19f7851e7493c2cabe48e8c40b8bf08a97fc1a3363c52d92c176efdf
[2026-10-29T09:31:25Z] ROW 1793232000-1793261700.0.stream.jsonl.gz 12815998 8f724133bc113ff6d30bc03d266711ca940aa0ccb4f244674566f14623556a08 digest sha256:8f724133bc113ff6d30bc03d266711ca940aa0ccb4f244674566f14623556a08 download 8f724133bc113ff6d30bc03d266711ca940aa0ccb4f244674566f14623556a08 removed 8f724133bc113ff6d30bc03d266711ca940aa0ccb4f244674566f14623556a08
[2026-10-29T09:31:25Z] ROW 1793232000-1793262600.0.stream.jsonl.gz 14933789 9c3aa5375f8405416226c860be5b8af5904b3a786c390271296e034260e5af25 digest sha256:9c3aa5375f8405416226c860be5b8af5904b3a786c390271296e034260e5af25 download 9c3aa5375f8405416226c860be5b8af5904b3a786c390271296e034260e5af25 removed 9c3aa5375f8405416226c860be5b8af5904b3a786c390271296e034260e5af25
[2026-10-29T09:31:25Z] G-DELETE: {'every file of the set absent': True, 'each removal recorded': True, 'each slot keeps its slot.json': True}; 86 gone, 86 removals recorded, 85 slots keep their slot.json
[2026-10-29T09:31:25Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/tags/rewardbook-streams-1793263627: 0 bytes, budget 5 s, second 129, 0.3 s, inside True True
[2026-10-29T09:31:25Z] T api POST /repos/seahomebatumi-ai/btc-5m-twap/releases: 0 bytes, budget 5 s, second 130, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/427629503/assets: 0 bytes, budget 5 s, second 131, 0.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793187000.0.stream.jsonl.gz: 9629579 bytes, budget 10 s, second 131, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793187900.0.stream.jsonl.gz: 9639138 bytes, budget 10 s, second 133, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793188800.0.stream.jsonl.gz: 10430786 bytes, budget 11 s, second 134, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793189700.0.stream.jsonl.gz: 10844068 bytes, budget 11 s, second 135, 2.5 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793190600.0.stream.jsonl.gz: 11422263 bytes, budget 11 s, second 138, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793191500.0.stream.jsonl.gz: 8669289 bytes, budget 10 s, second 139, 1.5 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793191500.1.stream.jsonl.gz: 2824343 bytes, budget 7 s, second 140, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793192400.0.stream.jsonl.gz: 11723039 bytes, budget 11 s, second 142, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793193300.0.stream.jsonl.gz: 10919554 bytes, budget 11 s, second 143, 1.5 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793194200.0.stream.jsonl.gz: 9958510 bytes, budget 10 s, second 144, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793195100.0.stream.jsonl.gz: 10225257 bytes, budget 11 s, second 146, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793196000.0.stream.jsonl.gz: 9759422 bytes, budget 10 s, second 147, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793196900.0.stream.jsonl.gz: 9780710 bytes, budget 10 s, second 148, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793197800.0.stream.jsonl.gz: 9880467 bytes, budget 10 s, second 150, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793198700.0.stream.jsonl.gz: 11208381 bytes, budget 11 s, second 151, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793199600.0.stream.jsonl.gz: 12025155 bytes, budget 12 s, second 152, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793200500.0.stream.jsonl.gz: 10028151 bytes, budget 11 s, second 154, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793201400.0.stream.jsonl.gz: 10684034 bytes, budget 11 s, second 155, 1.6 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793202300.0.stream.jsonl.gz: 10156189 bytes, budget 11 s, second 157, 1.7 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793203200.0.stream.jsonl.gz: 10279670 bytes, budget 11 s, second 158, 1.5 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793204100.0.stream.jsonl.gz: 9536875 bytes, budget 10 s, second 160, 1.5 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793205000.0.stream.jsonl.gz: 10141202 bytes, budget 11 s, second 161, 1.5 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793205900.0.stream.jsonl.gz: 9715061 bytes, budget 10 s, second 163, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793206800.0.stream.jsonl.gz: 11001064 bytes, budget 11 s, second 164, 1.6 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793207700.0.stream.jsonl.gz: 9835502 bytes, budget 10 s, second 166, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793208600.0.stream.jsonl.gz: 9874421 bytes, budget 10 s, second 167, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793209500.0.stream.jsonl.gz: 9385489 bytes, budget 10 s, second 168, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793210400.0.stream.jsonl.gz: 10966063 bytes, budget 11 s, second 169, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793211300.0.stream.jsonl.gz: 10551024 bytes, budget 11 s, second 171, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793212200.0.stream.jsonl.gz: 12372196 bytes, budget 12 s, second 172, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793213100.0.stream.jsonl.gz: 11112191 bytes, budget 11 s, second 173, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793214000.0.stream.jsonl.gz: 10918172 bytes, budget 11 s, second 174, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793214900.0.stream.jsonl.gz: 10956690 bytes, budget 11 s, second 176, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793215800.0.stream.jsonl.gz: 10464479 bytes, budget 11 s, second 177, 1.5 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793216700.0.stream.jsonl.gz: 11797234 bytes, budget 11 s, second 179, 1.6 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793217600.0.stream.jsonl.gz: 9947721 bytes, budget 10 s, second 180, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793218500.0.stream.jsonl.gz: 9342830 bytes, budget 10 s, second 181, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793219400.0.stream.jsonl.gz: 8879554 bytes, budget 10 s, second 183, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793220300.0.stream.jsonl.gz: 9062207 bytes, budget 10 s, second 184, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793221200.0.stream.jsonl.gz: 9372847 bytes, budget 10 s, second 186, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793222100.0.stream.jsonl.gz: 8001926 bytes, budget 10 s, second 187, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793223000.0.stream.jsonl.gz: 8114414 bytes, budget 10 s, second 188, 1.1 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793223900.0.stream.jsonl.gz: 9006052 bytes, budget 10 s, second 189, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793224800.0.stream.jsonl.gz: 8661025 bytes, budget 10 s, second 190, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793225700.0.stream.jsonl.gz: 8132267 bytes, budget 10 s, second 192, 1.5 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793226600.0.stream.jsonl.gz: 9326449 bytes, budget 10 s, second 193, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793227500.0.stream.jsonl.gz: 9815975 bytes, budget 10 s, second 195, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793228400.0.stream.jsonl.gz: 9231800 bytes, budget 10 s, second 196, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793229300.0.stream.jsonl.gz: 8160699 bytes, budget 10 s, second 197, 1.1 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793230200.0.stream.jsonl.gz: 8889088 bytes, budget 10 s, second 198, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793145600-1793231100.0.stream.jsonl.gz: 9143917 bytes, budget 10 s, second 199, 1.6 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793232000.0.stream.jsonl.gz: 11579610 bytes, budget 11 s, second 201, 1.9 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793232900.0.stream.jsonl.gz: 10715152 bytes, budget 11 s, second 203, 1.5 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793233800.0.stream.jsonl.gz: 11443056 bytes, budget 11 s, second 204, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793234700.0.stream.jsonl.gz: 13592154 bytes, budget 12 s, second 206, 1.6 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793235600.0.stream.jsonl.gz: 11481990 bytes, budget 11 s, second 207, 1.6 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793236500.0.stream.jsonl.gz: 11586307 bytes, budget 11 s, second 209, 1.6 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793237400.0.stream.jsonl.gz: 10660664 bytes, budget 11 s, second 210, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793238300.0.stream.jsonl.gz: 10776660 bytes, budget 11 s, second 212, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793239200.0.stream.jsonl.gz: 10626770 bytes, budget 11 s, second 213, 1.9 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793240100.0.stream.jsonl.gz: 9792424 bytes, budget 10 s, second 215, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793241000.0.stream.jsonl.gz: 10745728 bytes, budget 11 s, second 216, 1.5 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793241900.0.stream.jsonl.gz: 11272730 bytes, budget 11 s, second 218, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793242800.0.stream.jsonl.gz: 9774209 bytes, budget 10 s, second 219, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793243700.0.stream.jsonl.gz: 9321701 bytes, budget 10 s, second 220, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793244600.0.stream.jsonl.gz: 10295145 bytes, budget 11 s, second 222, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793245500.0.stream.jsonl.gz: 10434441 bytes, budget 11 s, second 223, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793246400.0.stream.jsonl.gz: 11156773 bytes, budget 11 s, second 224, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793247300.0.stream.jsonl.gz: 11456592 bytes, budget 11 s, second 226, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793248200.0.stream.jsonl.gz: 11804877 bytes, budget 11 s, second 227, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793249100.0.stream.jsonl.gz: 11704215 bytes, budget 11 s, second 228, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793250000.0.stream.jsonl.gz: 9914992 bytes, budget 10 s, second 230, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793250900.0.stream.jsonl.gz: 10553162 bytes, budget 11 s, second 231, 1.5 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793251800.0.stream.jsonl.gz: 6547939 bytes, budget 9 s, second 233, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793252700.0.stream.jsonl.gz: 6710655 bytes, budget 9 s, second 234, 1.1 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793253600.0.stream.jsonl.gz: 10468900 bytes, budget 11 s, second 235, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793254500.0.stream.jsonl.gz: 11330444 bytes, budget 11 s, second 236, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793255400.0.stream.jsonl.gz: 10581288 bytes, budget 11 s, second 237, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793256300.0.stream.jsonl.gz: 9852787 bytes, budget 10 s, second 239, 1.5 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793257200.0.stream.jsonl.gz: 12148871 bytes, budget 12 s, second 240, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793258100.0.stream.jsonl.gz: 13568827 bytes, budget 12 s, second 242, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793259000.0.stream.jsonl.gz: 11991341 bytes, budget 11 s, second 243, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793259900.0.stream.jsonl.gz: 12726821 bytes, budget 12 s, second 244, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793260800.0.stream.jsonl.gz: 14804505 bytes, budget 13 s, second 246, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793261700.0.stream.jsonl.gz: 12815998 bytes, budget 12 s, second 247, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T upload 1793232000-1793262600.0.stream.jsonl.gz: 14933789 bytes, budget 13 s, second 248, 1.9 s, inside True True
[2026-10-29T09:31:25Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/tags/rewardbook-streams-1793263627: 0 bytes, budget 5 s, second 371, 0.3 s, inside True True
[2026-10-29T09:31:25Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/tags/rewardbook-streams-1793263627: 0 bytes, budget 5 s, second 72, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/427629503/assets: 0 bytes, budget 5 s, second 73, 0.4 s, inside True True
[2026-10-29T09:31:25Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/tags/rewardbook-streams-1793263627: 0 bytes, budget 5 s, second 194, 0.4 s, inside True True
[2026-10-29T09:31:25Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/427629503/assets: 0 bytes, budget 5 s, second 194, 0.4 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793187000.0.stream.jsonl.gz: 9629579 bytes, budget 10 s, second 195, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793187900.0.stream.jsonl.gz: 9639138 bytes, budget 10 s, second 196, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793188800.0.stream.jsonl.gz: 10430786 bytes, budget 11 s, second 197, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793189700.0.stream.jsonl.gz: 10844068 bytes, budget 11 s, second 198, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793190600.0.stream.jsonl.gz: 11422263 bytes, budget 11 s, second 198, 1.4 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793191500.0.stream.jsonl.gz: 8669289 bytes, budget 10 s, second 200, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793191500.1.stream.jsonl.gz: 2824343 bytes, budget 7 s, second 200, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793192400.0.stream.jsonl.gz: 11723039 bytes, budget 11 s, second 201, 0.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793193300.0.stream.jsonl.gz: 10919554 bytes, budget 11 s, second 202, 0.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793194200.0.stream.jsonl.gz: 9958510 bytes, budget 10 s, second 203, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793195100.0.stream.jsonl.gz: 10225257 bytes, budget 11 s, second 203, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793196000.0.stream.jsonl.gz: 9759422 bytes, budget 10 s, second 204, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793196900.0.stream.jsonl.gz: 9780710 bytes, budget 10 s, second 205, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793197800.0.stream.jsonl.gz: 9880467 bytes, budget 10 s, second 205, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793198700.0.stream.jsonl.gz: 11208381 bytes, budget 11 s, second 206, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793199600.0.stream.jsonl.gz: 12025155 bytes, budget 12 s, second 207, 0.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793200500.0.stream.jsonl.gz: 10028151 bytes, budget 11 s, second 208, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793201400.0.stream.jsonl.gz: 10684034 bytes, budget 11 s, second 209, 0.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793202300.0.stream.jsonl.gz: 10156189 bytes, budget 11 s, second 210, 0.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793203200.0.stream.jsonl.gz: 10279670 bytes, budget 11 s, second 211, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793204100.0.stream.jsonl.gz: 9536875 bytes, budget 10 s, second 212, 1.1 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793205000.0.stream.jsonl.gz: 10141202 bytes, budget 11 s, second 213, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793205900.0.stream.jsonl.gz: 9715061 bytes, budget 10 s, second 214, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793206800.0.stream.jsonl.gz: 11001064 bytes, budget 11 s, second 215, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793207700.0.stream.jsonl.gz: 9835502 bytes, budget 10 s, second 216, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793208600.0.stream.jsonl.gz: 9874421 bytes, budget 10 s, second 216, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793209500.0.stream.jsonl.gz: 9385489 bytes, budget 10 s, second 217, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793210400.0.stream.jsonl.gz: 10966063 bytes, budget 11 s, second 218, 0.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793211300.0.stream.jsonl.gz: 10551024 bytes, budget 11 s, second 218, 0.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793212200.0.stream.jsonl.gz: 12372196 bytes, budget 12 s, second 219, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793213100.0.stream.jsonl.gz: 11112191 bytes, budget 11 s, second 220, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793214000.0.stream.jsonl.gz: 10918172 bytes, budget 11 s, second 221, 0.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793214900.0.stream.jsonl.gz: 10956690 bytes, budget 11 s, second 222, 0.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793215800.0.stream.jsonl.gz: 10464479 bytes, budget 11 s, second 223, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793216700.0.stream.jsonl.gz: 11797234 bytes, budget 11 s, second 223, 1.0 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793217600.0.stream.jsonl.gz: 9947721 bytes, budget 10 s, second 224, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793218500.0.stream.jsonl.gz: 9342830 bytes, budget 10 s, second 225, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793219400.0.stream.jsonl.gz: 8879554 bytes, budget 10 s, second 226, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793220300.0.stream.jsonl.gz: 9062207 bytes, budget 10 s, second 226, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793221200.0.stream.jsonl.gz: 9372847 bytes, budget 10 s, second 227, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793222100.0.stream.jsonl.gz: 8001926 bytes, budget 10 s, second 228, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793223000.0.stream.jsonl.gz: 8114414 bytes, budget 10 s, second 228, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793223900.0.stream.jsonl.gz: 9006052 bytes, budget 10 s, second 229, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793224800.0.stream.jsonl.gz: 8661025 bytes, budget 10 s, second 230, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793225700.0.stream.jsonl.gz: 8132267 bytes, budget 10 s, second 230, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793226600.0.stream.jsonl.gz: 9326449 bytes, budget 10 s, second 231, 0.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793227500.0.stream.jsonl.gz: 9815975 bytes, budget 10 s, second 232, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793228400.0.stream.jsonl.gz: 9231800 bytes, budget 10 s, second 233, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793229300.0.stream.jsonl.gz: 8160699 bytes, budget 10 s, second 233, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793230200.0.stream.jsonl.gz: 8889088 bytes, budget 10 s, second 234, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793145600-1793231100.0.stream.jsonl.gz: 9143917 bytes, budget 10 s, second 234, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793232000.0.stream.jsonl.gz: 11579610 bytes, budget 11 s, second 235, 1.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793232900.0.stream.jsonl.gz: 10715152 bytes, budget 11 s, second 237, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793233800.0.stream.jsonl.gz: 11443056 bytes, budget 11 s, second 238, 0.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793234700.0.stream.jsonl.gz: 13592154 bytes, budget 12 s, second 239, 1.0 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793235600.0.stream.jsonl.gz: 11481990 bytes, budget 11 s, second 240, 0.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793236500.0.stream.jsonl.gz: 11586307 bytes, budget 11 s, second 241, 1.0 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793237400.0.stream.jsonl.gz: 10660664 bytes, budget 11 s, second 242, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793238300.0.stream.jsonl.gz: 10776660 bytes, budget 11 s, second 243, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793239200.0.stream.jsonl.gz: 10626770 bytes, budget 11 s, second 244, 1.0 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793240100.0.stream.jsonl.gz: 9792424 bytes, budget 10 s, second 245, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793241000.0.stream.jsonl.gz: 10745728 bytes, budget 11 s, second 246, 1.0 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793241900.0.stream.jsonl.gz: 11272730 bytes, budget 11 s, second 247, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793242800.0.stream.jsonl.gz: 9774209 bytes, budget 10 s, second 247, 1.1 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793243700.0.stream.jsonl.gz: 9321701 bytes, budget 10 s, second 249, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793244600.0.stream.jsonl.gz: 10295145 bytes, budget 11 s, second 249, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793245500.0.stream.jsonl.gz: 10434441 bytes, budget 11 s, second 250, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793246400.0.stream.jsonl.gz: 11156773 bytes, budget 11 s, second 251, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793247300.0.stream.jsonl.gz: 11456592 bytes, budget 11 s, second 251, 0.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793248200.0.stream.jsonl.gz: 11804877 bytes, budget 11 s, second 252, 1.2 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793249100.0.stream.jsonl.gz: 11704215 bytes, budget 11 s, second 253, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793250000.0.stream.jsonl.gz: 9914992 bytes, budget 10 s, second 254, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793250900.0.stream.jsonl.gz: 10553162 bytes, budget 11 s, second 255, 0.9 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793251800.0.stream.jsonl.gz: 6547939 bytes, budget 9 s, second 256, 1.3 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793252700.0.stream.jsonl.gz: 6710655 bytes, budget 9 s, second 257, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793253600.0.stream.jsonl.gz: 10468900 bytes, budget 11 s, second 258, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793254500.0.stream.jsonl.gz: 11330444 bytes, budget 11 s, second 259, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793255400.0.stream.jsonl.gz: 10581288 bytes, budget 11 s, second 259, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793256300.0.stream.jsonl.gz: 9852787 bytes, budget 10 s, second 260, 0.6 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793257200.0.stream.jsonl.gz: 12148871 bytes, budget 12 s, second 261, 1.5 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793258100.0.stream.jsonl.gz: 13568827 bytes, budget 12 s, second 262, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793259000.0.stream.jsonl.gz: 11991341 bytes, budget 11 s, second 263, 0.8 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793259900.0.stream.jsonl.gz: 12726821 bytes, budget 12 s, second 264, 1.0 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793260800.0.stream.jsonl.gz: 14804505 bytes, budget 13 s, second 265, 1.0 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793261700.0.stream.jsonl.gz: 12815998 bytes, budget 12 s, second 266, 0.7 s, inside True True
[2026-10-29T09:31:25Z] T download 1793232000-1793262600.0.stream.jsonl.gz: 14933789 bytes, budget 13 s, second 267, 0.9 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793187000.0.stream.jsonl.gz: 9629579 bytes, second 268, 0.030 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793187900.0.stream.jsonl.gz: 9639138 bytes, second 268, 0.026 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793188800.0.stream.jsonl.gz: 10430786 bytes, second 268, 0.027 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793189700.0.stream.jsonl.gz: 10844068 bytes, second 268, 0.028 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793190600.0.stream.jsonl.gz: 11422263 bytes, second 268, 0.029 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793191500.0.stream.jsonl.gz: 8669289 bytes, second 268, 0.025 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793191500.1.stream.jsonl.gz: 2824343 bytes, second 268, 0.011 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793192400.0.stream.jsonl.gz: 11723039 bytes, second 268, 0.036 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793193300.0.stream.jsonl.gz: 10919554 bytes, second 268, 0.027 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793194200.0.stream.jsonl.gz: 9958510 bytes, second 268, 0.026 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793195100.0.stream.jsonl.gz: 10225257 bytes, second 268, 0.028 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793196000.0.stream.jsonl.gz: 9759422 bytes, second 268, 0.025 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793196900.0.stream.jsonl.gz: 9780710 bytes, second 268, 0.026 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793197800.0.stream.jsonl.gz: 9880467 bytes, second 268, 0.026 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793198700.0.stream.jsonl.gz: 11208381 bytes, second 268, 0.031 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793199600.0.stream.jsonl.gz: 12025155 bytes, second 268, 0.031 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793200500.0.stream.jsonl.gz: 10028151 bytes, second 268, 0.026 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793201400.0.stream.jsonl.gz: 10684034 bytes, second 268, 0.027 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793202300.0.stream.jsonl.gz: 10156189 bytes, second 268, 0.026 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793203200.0.stream.jsonl.gz: 10279670 bytes, second 268, 0.026 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793204100.0.stream.jsonl.gz: 9536875 bytes, second 268, 0.024 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793205000.0.stream.jsonl.gz: 10141202 bytes, second 268, 0.025 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793205900.0.stream.jsonl.gz: 9715061 bytes, second 268, 0.025 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793206800.0.stream.jsonl.gz: 11001064 bytes, second 268, 0.029 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793207700.0.stream.jsonl.gz: 9835502 bytes, second 268, 0.028 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793208600.0.stream.jsonl.gz: 9874421 bytes, second 268, 0.026 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793209500.0.stream.jsonl.gz: 9385489 bytes, second 268, 0.025 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793210400.0.stream.jsonl.gz: 10966063 bytes, second 268, 0.029 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793211300.0.stream.jsonl.gz: 10551024 bytes, second 268, 0.026 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793212200.0.stream.jsonl.gz: 12372196 bytes, second 268, 0.034 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793213100.0.stream.jsonl.gz: 11112191 bytes, second 269, 0.030 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793214000.0.stream.jsonl.gz: 10918172 bytes, second 269, 0.029 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793214900.0.stream.jsonl.gz: 10956690 bytes, second 269, 0.030 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793215800.0.stream.jsonl.gz: 10464479 bytes, second 269, 0.028 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793216700.0.stream.jsonl.gz: 11797234 bytes, second 269, 0.030 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793217600.0.stream.jsonl.gz: 9947721 bytes, second 269, 0.026 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793218500.0.stream.jsonl.gz: 9342830 bytes, second 269, 0.025 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793219400.0.stream.jsonl.gz: 8879554 bytes, second 269, 0.024 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793220300.0.stream.jsonl.gz: 9062207 bytes, second 269, 0.024 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793221200.0.stream.jsonl.gz: 9372847 bytes, second 269, 0.026 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793222100.0.stream.jsonl.gz: 8001926 bytes, second 269, 0.023 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793223000.0.stream.jsonl.gz: 8114414 bytes, second 269, 0.022 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793223900.0.stream.jsonl.gz: 9006052 bytes, second 269, 0.029 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793224800.0.stream.jsonl.gz: 8661025 bytes, second 269, 0.023 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793225700.0.stream.jsonl.gz: 8132267 bytes, second 269, 0.022 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793226600.0.stream.jsonl.gz: 9326449 bytes, second 269, 0.024 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793227500.0.stream.jsonl.gz: 9815975 bytes, second 269, 0.024 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793228400.0.stream.jsonl.gz: 9231800 bytes, second 269, 0.028 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793229300.0.stream.jsonl.gz: 8160699 bytes, second 269, 0.023 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793230200.0.stream.jsonl.gz: 8889088 bytes, second 269, 0.023 s, inside True True
[2026-10-29T09:31:25Z] X 1793145600-1793231100.0.stream.jsonl.gz: 9143917 bytes, second 269, 0.023 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793232000.0.stream.jsonl.gz: 11579610 bytes, second 269, 0.030 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793232900.0.stream.jsonl.gz: 10715152 bytes, second 269, 0.028 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793233800.0.stream.jsonl.gz: 11443056 bytes, second 269, 0.029 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793234700.0.stream.jsonl.gz: 13592154 bytes, second 269, 0.035 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793235600.0.stream.jsonl.gz: 11481990 bytes, second 269, 0.029 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793236500.0.stream.jsonl.gz: 11586307 bytes, second 269, 0.029 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793237400.0.stream.jsonl.gz: 10660664 bytes, second 269, 0.029 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793238300.0.stream.jsonl.gz: 10776660 bytes, second 269, 0.028 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793239200.0.stream.jsonl.gz: 10626770 bytes, second 269, 0.026 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793240100.0.stream.jsonl.gz: 9792424 bytes, second 269, 0.026 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793241000.0.stream.jsonl.gz: 10745728 bytes, second 269, 0.030 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793241900.0.stream.jsonl.gz: 11272730 bytes, second 270, 0.031 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793242800.0.stream.jsonl.gz: 9774209 bytes, second 270, 0.027 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793243700.0.stream.jsonl.gz: 9321701 bytes, second 270, 0.024 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793244600.0.stream.jsonl.gz: 10295145 bytes, second 270, 0.028 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793245500.0.stream.jsonl.gz: 10434441 bytes, second 270, 0.053 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793246400.0.stream.jsonl.gz: 11156773 bytes, second 270, 0.071 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793247300.0.stream.jsonl.gz: 11456592 bytes, second 270, 0.057 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793248200.0.stream.jsonl.gz: 11804877 bytes, second 270, 0.062 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793249100.0.stream.jsonl.gz: 11704215 bytes, second 270, 0.039 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793250000.0.stream.jsonl.gz: 9914992 bytes, second 270, 0.025 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793250900.0.stream.jsonl.gz: 10553162 bytes, second 270, 0.026 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793251800.0.stream.jsonl.gz: 6547939 bytes, second 270, 0.018 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793252700.0.stream.jsonl.gz: 6710655 bytes, second 270, 0.019 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793253600.0.stream.jsonl.gz: 10468900 bytes, second 270, 0.029 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793254500.0.stream.jsonl.gz: 11330444 bytes, second 270, 0.029 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793255400.0.stream.jsonl.gz: 10581288 bytes, second 270, 0.027 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793256300.0.stream.jsonl.gz: 9852787 bytes, second 270, 0.025 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793257200.0.stream.jsonl.gz: 12148871 bytes, second 270, 0.029 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793258100.0.stream.jsonl.gz: 13568827 bytes, second 270, 0.033 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793259000.0.stream.jsonl.gz: 11991341 bytes, second 270, 0.031 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793259900.0.stream.jsonl.gz: 12726821 bytes, second 270, 0.032 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793260800.0.stream.jsonl.gz: 14804505 bytes, second 270, 0.037 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793261700.0.stream.jsonl.gz: 12815998 bytes, second 270, 0.033 s, inside True True
[2026-10-29T09:31:25Z] X 1793232000-1793262600.0.stream.jsonl.gz: 14933789 bytes, second 270, 0.037 s, inside True True
[2026-10-29T09:31:25Z] G-IDLE: 180 requests and 86 removals, 0 started outside, 0 ended outside
[2026-10-29T09:31:25Z] G-NEXT slot 1793265300 2026-10-29T09:15:00Z, decided at 2026-10-29T09:14:54Z: PASS - index 0 streamed by 3137952
[2026-10-29T09:31:25Z] READING G-NEXT: PASS over 1 slots, the reward book's process at the run's start 3137952
[2026-10-29T09:31:25Z] ACROSS slot 1793263500 2026-10-29T08:45:00Z: index 0 pid 3137952 joined_late False stopped False opened True off None segments 1 frames 105795 max_gap_ns 373046700 stored_bytes 12813807 error None
[2026-10-29T09:31:25Z] ACROSS slot 1793264400 2026-10-29T09:00:00Z: index 0 pid 3137952 joined_late False stopped False opened True off None segments 1 frames 100264 max_gap_ns 394079223 stored_bytes 12248012 error None
[2026-10-29T09:31:25Z] the run's own record: {"assets_n": 86, "bytes_total": 890975956, "ended_outside": 0, "event": "complete", "free_bytes": 11195334656, "held_s": 0, "peak_rss": 39477248, "rate_per_day": 1006278726, "removals": 86, "requests": 180, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793263627, "started_outside": 0, "stops": [["the cap", 1793606667], ["the floor, base 43500000 bytes a day", 1793585267], ["the floor, base 187760570 bytes a day", 1793546534]], "store_stream_bytes": 16842458, "wall_ns": 1793264670967510113}
[2026-10-29T09:31:25Z] READING G-TRIGGER   PASS
[2026-10-29T09:31:25Z] READING G-RUN       PASS
[2026-10-29T09:31:25Z] READING G-SET       PASS
[2026-10-29T09:31:25Z] READING G-UPLOAD    PASS
[2026-10-29T09:31:25Z] READING G-DOWNLOAD  PASS
[2026-10-29T09:31:25Z] READING G-DELETE    PASS
[2026-10-29T09:31:25Z] READING G-IDLE      PASS
[2026-10-29T09:31:25Z] READING G-NEXT      PASS
[2026-10-29T09:31:25Z] FIRST PASS: 8 of 8
[2026-10-29T09:31:25Z] peak memory of this run: 39141376 bytes
[2026-10-29T09:31:25Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 4; requests 2, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

| reading | read | PASS |
|---|---|---|
| G-TRIGGER | by `TRIGGER_UNIT` `btc-rewardbook-archive.timer`; its elapse 08:47:07, the mark 08:15:15 plus 1,800 s plus 112 s; the run's first record 08:47:07; the timer's `LastTriggerUSec` 08:47:07 | PASS |
| G-RUN | `complete`; the service's last invocation `a1eb6d29…`, `Result` `success`, `ExecMainStatus` `0`, 09:01:12 to 09:04:31 | PASS |
| G-SET | 1 set record; `set.json` `f3450db0742d155b3e5487cdbde9d0bdf3877661c4c12fc962dcccd7981e7f3e`, rebuilt equal; 85 slots considered, 85 closed, 0 unclosed, 1 open, 0 streamless, deferred 0, 86 taken; the store after it 0 stream files of slots due by `A`, none flipped | PASS |
| G-UPLOAD | Release `427629503`, 86 of 86 by name, bytes, state and digest, 0 missing, 0 beyond; the tag at `6a61525…`, lightweight | PASS |
| G-DOWNLOAD | `verify.json` `dad6b5783342c244dcc7fb8d5540b8c6176c809c4a1dd9204a3cc2eb6c6c4379`, 86 of 86 downloads equal, 890,975,956 bytes | PASS |
| G-DELETE | 86 gone, 86 removals recorded, 85 slots keep their `slot.json` | PASS |
| G-IDLE | 180 requests and 86 removals, 0 started outside, 0 ended outside | PASS |
| G-NEXT | 1 slot, `1793265300` (09:15 UTC), decided at 09:14:54: PASS, index 0 streamed by `3137952`; the reading PASS | PASS |

**FIRST PASS: 8 of 8.** The 180 `T` lines are the run's requests over both invocations — 8 API requests, 86 uploads, 86 downloads; the 86 `X` lines its removals, at seconds 268 to 271 of window `1793264400`, 0.026 to 0.04 s each. The run held 0 s for the pair book's archive (no `HOLD` line) and waited 0 s for the reward book's quiet (`quiet_s` 0). Two `ACROSS` slots, 08:45 and 09:00 UTC, each one segment, streamed by `3137952`, no off reason.

### 2.9 The per-asset table — the 86 `ROW` lines, read again by the session

Each row from the deciding `first`'s `ROW` line: the set's bytes and SHA-256, the Release's `digest` as read anonymously, the downloaded SHA-256 from `verify.json`, and the removed file's from `delete.jsonl`.

| # | asset | bytes | set SHA-256 | Release digest | downloaded SHA-256 | removed file's SHA-256 | equal |
|---|---|---|---|---|---|---|---|
| 1 | `1793145600-1793187000.0.stream.jsonl.gz` | 9,629,579 | `121ae8ad5aaffa260737f6d5ea469e4792e7d7793f7db604e4f6152bc7504916` | `121ae8ad5aaffa260737f6d5ea469e4792e7d7793f7db604e4f6152bc7504916` | `121ae8ad5aaffa260737f6d5ea469e4792e7d7793f7db604e4f6152bc7504916` | `121ae8ad5aaffa260737f6d5ea469e4792e7d7793f7db604e4f6152bc7504916` | yes |
| 2 | `1793145600-1793187900.0.stream.jsonl.gz` | 9,639,138 | `37ad0796a091fb6a9b088c0c266d0cbbd88e104c670d8efd33c670c4abf2a823` | `37ad0796a091fb6a9b088c0c266d0cbbd88e104c670d8efd33c670c4abf2a823` | `37ad0796a091fb6a9b088c0c266d0cbbd88e104c670d8efd33c670c4abf2a823` | `37ad0796a091fb6a9b088c0c266d0cbbd88e104c670d8efd33c670c4abf2a823` | yes |
| 3 | `1793145600-1793188800.0.stream.jsonl.gz` | 10,430,786 | `ad85da3abf58feedae79d68ebfb8d0a402f25acd40459d96f28ea9a47c70bb96` | `ad85da3abf58feedae79d68ebfb8d0a402f25acd40459d96f28ea9a47c70bb96` | `ad85da3abf58feedae79d68ebfb8d0a402f25acd40459d96f28ea9a47c70bb96` | `ad85da3abf58feedae79d68ebfb8d0a402f25acd40459d96f28ea9a47c70bb96` | yes |
| 4 | `1793145600-1793189700.0.stream.jsonl.gz` | 10,844,068 | `c91f3297a636a3e239bfa529c3804cf626f66765c5b3256afe04c1a301061039` | `c91f3297a636a3e239bfa529c3804cf626f66765c5b3256afe04c1a301061039` | `c91f3297a636a3e239bfa529c3804cf626f66765c5b3256afe04c1a301061039` | `c91f3297a636a3e239bfa529c3804cf626f66765c5b3256afe04c1a301061039` | yes |
| 5 | `1793145600-1793190600.0.stream.jsonl.gz` | 11,422,263 | `ab9b26074465807668fd298a824ec53d5bf3678ea7452b37ab44ea2f3d145d5f` | `ab9b26074465807668fd298a824ec53d5bf3678ea7452b37ab44ea2f3d145d5f` | `ab9b26074465807668fd298a824ec53d5bf3678ea7452b37ab44ea2f3d145d5f` | `ab9b26074465807668fd298a824ec53d5bf3678ea7452b37ab44ea2f3d145d5f` | yes |
| 6 | `1793145600-1793191500.0.stream.jsonl.gz` | 8,669,289 | `4aff733af5bc9e08e2996011967bab6fc0a58bb5230961f7fcc3f488d4fc7f6e` | `4aff733af5bc9e08e2996011967bab6fc0a58bb5230961f7fcc3f488d4fc7f6e` | `4aff733af5bc9e08e2996011967bab6fc0a58bb5230961f7fcc3f488d4fc7f6e` | `4aff733af5bc9e08e2996011967bab6fc0a58bb5230961f7fcc3f488d4fc7f6e` | yes |
| 7 | `1793145600-1793191500.1.stream.jsonl.gz` | 2,824,343 | `7bfe046788a1f35db8bf621b1608b3262bb7405340ca88931bd74b821c501f1f` | `7bfe046788a1f35db8bf621b1608b3262bb7405340ca88931bd74b821c501f1f` | `7bfe046788a1f35db8bf621b1608b3262bb7405340ca88931bd74b821c501f1f` | `7bfe046788a1f35db8bf621b1608b3262bb7405340ca88931bd74b821c501f1f` | yes |
| 8 | `1793145600-1793192400.0.stream.jsonl.gz` | 11,723,039 | `8028f8a9d828d6c1e94d383faae0d68af94675d1f2ba57a568ec34962bd6e06b` | `8028f8a9d828d6c1e94d383faae0d68af94675d1f2ba57a568ec34962bd6e06b` | `8028f8a9d828d6c1e94d383faae0d68af94675d1f2ba57a568ec34962bd6e06b` | `8028f8a9d828d6c1e94d383faae0d68af94675d1f2ba57a568ec34962bd6e06b` | yes |
| 9 | `1793145600-1793193300.0.stream.jsonl.gz` | 10,919,554 | `0d49767ed12888f2994c6e6e8a8ecdd6a2d540713db437bb46c8c73a97718275` | `0d49767ed12888f2994c6e6e8a8ecdd6a2d540713db437bb46c8c73a97718275` | `0d49767ed12888f2994c6e6e8a8ecdd6a2d540713db437bb46c8c73a97718275` | `0d49767ed12888f2994c6e6e8a8ecdd6a2d540713db437bb46c8c73a97718275` | yes |
| 10 | `1793145600-1793194200.0.stream.jsonl.gz` | 9,958,510 | `a61297412d0223c0dd827965661a609463b26136d71bc0bb403723491b871d9a` | `a61297412d0223c0dd827965661a609463b26136d71bc0bb403723491b871d9a` | `a61297412d0223c0dd827965661a609463b26136d71bc0bb403723491b871d9a` | `a61297412d0223c0dd827965661a609463b26136d71bc0bb403723491b871d9a` | yes |
| 11 | `1793145600-1793195100.0.stream.jsonl.gz` | 10,225,257 | `10fd14580576dcf7d2ba5b34377db1c0ab94909089504afdf4e3b831958fe731` | `10fd14580576dcf7d2ba5b34377db1c0ab94909089504afdf4e3b831958fe731` | `10fd14580576dcf7d2ba5b34377db1c0ab94909089504afdf4e3b831958fe731` | `10fd14580576dcf7d2ba5b34377db1c0ab94909089504afdf4e3b831958fe731` | yes |
| 12 | `1793145600-1793196000.0.stream.jsonl.gz` | 9,759,422 | `e8765455d1f1f783288f086027d3b198cf31741944bd5a188b22565345983481` | `e8765455d1f1f783288f086027d3b198cf31741944bd5a188b22565345983481` | `e8765455d1f1f783288f086027d3b198cf31741944bd5a188b22565345983481` | `e8765455d1f1f783288f086027d3b198cf31741944bd5a188b22565345983481` | yes |
| 13 | `1793145600-1793196900.0.stream.jsonl.gz` | 9,780,710 | `88c2c84708ab437c4fe5fce3f84776211e62fd1dd5af70fdba40f1894897bdd0` | `88c2c84708ab437c4fe5fce3f84776211e62fd1dd5af70fdba40f1894897bdd0` | `88c2c84708ab437c4fe5fce3f84776211e62fd1dd5af70fdba40f1894897bdd0` | `88c2c84708ab437c4fe5fce3f84776211e62fd1dd5af70fdba40f1894897bdd0` | yes |
| 14 | `1793145600-1793197800.0.stream.jsonl.gz` | 9,880,467 | `a5d99308e054693a039d9ee64579ca5015652f140ff1fdd9dac8e9cb72e4eb3a` | `a5d99308e054693a039d9ee64579ca5015652f140ff1fdd9dac8e9cb72e4eb3a` | `a5d99308e054693a039d9ee64579ca5015652f140ff1fdd9dac8e9cb72e4eb3a` | `a5d99308e054693a039d9ee64579ca5015652f140ff1fdd9dac8e9cb72e4eb3a` | yes |
| 15 | `1793145600-1793198700.0.stream.jsonl.gz` | 11,208,381 | `075da9e7c5a711a1c555cf14c07cdadc4121ac49e6355d05b7f9e7875094af61` | `075da9e7c5a711a1c555cf14c07cdadc4121ac49e6355d05b7f9e7875094af61` | `075da9e7c5a711a1c555cf14c07cdadc4121ac49e6355d05b7f9e7875094af61` | `075da9e7c5a711a1c555cf14c07cdadc4121ac49e6355d05b7f9e7875094af61` | yes |
| 16 | `1793145600-1793199600.0.stream.jsonl.gz` | 12,025,155 | `c70cf12a975796105a875b8f8d7a73682ec557cd30ffd0dd0f051ae2ea90adc3` | `c70cf12a975796105a875b8f8d7a73682ec557cd30ffd0dd0f051ae2ea90adc3` | `c70cf12a975796105a875b8f8d7a73682ec557cd30ffd0dd0f051ae2ea90adc3` | `c70cf12a975796105a875b8f8d7a73682ec557cd30ffd0dd0f051ae2ea90adc3` | yes |
| 17 | `1793145600-1793200500.0.stream.jsonl.gz` | 10,028,151 | `8a2b4f911f7467b3ce3c5088829e499cc72a6d647128f7587c2d1f700ebf0558` | `8a2b4f911f7467b3ce3c5088829e499cc72a6d647128f7587c2d1f700ebf0558` | `8a2b4f911f7467b3ce3c5088829e499cc72a6d647128f7587c2d1f700ebf0558` | `8a2b4f911f7467b3ce3c5088829e499cc72a6d647128f7587c2d1f700ebf0558` | yes |
| 18 | `1793145600-1793201400.0.stream.jsonl.gz` | 10,684,034 | `99341832a61bf589521a253a863d94db68526d8a53114d0a855917b354e8a896` | `99341832a61bf589521a253a863d94db68526d8a53114d0a855917b354e8a896` | `99341832a61bf589521a253a863d94db68526d8a53114d0a855917b354e8a896` | `99341832a61bf589521a253a863d94db68526d8a53114d0a855917b354e8a896` | yes |
| 19 | `1793145600-1793202300.0.stream.jsonl.gz` | 10,156,189 | `ec78fb31112d645c9c08ded59c6befd6277bdfb7e260723c9340467f5b3fcea7` | `ec78fb31112d645c9c08ded59c6befd6277bdfb7e260723c9340467f5b3fcea7` | `ec78fb31112d645c9c08ded59c6befd6277bdfb7e260723c9340467f5b3fcea7` | `ec78fb31112d645c9c08ded59c6befd6277bdfb7e260723c9340467f5b3fcea7` | yes |
| 20 | `1793145600-1793203200.0.stream.jsonl.gz` | 10,279,670 | `5c10b99de3ca84f6d0cd4fd556fa530483c301e1bf3c7bb80114eef519ebd1bc` | `5c10b99de3ca84f6d0cd4fd556fa530483c301e1bf3c7bb80114eef519ebd1bc` | `5c10b99de3ca84f6d0cd4fd556fa530483c301e1bf3c7bb80114eef519ebd1bc` | `5c10b99de3ca84f6d0cd4fd556fa530483c301e1bf3c7bb80114eef519ebd1bc` | yes |
| 21 | `1793145600-1793204100.0.stream.jsonl.gz` | 9,536,875 | `ffbc1876095b1ca7ca17b218892d8b42c3bb918183eca7b7827d7de25ec768f5` | `ffbc1876095b1ca7ca17b218892d8b42c3bb918183eca7b7827d7de25ec768f5` | `ffbc1876095b1ca7ca17b218892d8b42c3bb918183eca7b7827d7de25ec768f5` | `ffbc1876095b1ca7ca17b218892d8b42c3bb918183eca7b7827d7de25ec768f5` | yes |
| 22 | `1793145600-1793205000.0.stream.jsonl.gz` | 10,141,202 | `b38c8fd1d01f0fa20fe38b26a94255344e296c83b509640bee279dcad5deff16` | `b38c8fd1d01f0fa20fe38b26a94255344e296c83b509640bee279dcad5deff16` | `b38c8fd1d01f0fa20fe38b26a94255344e296c83b509640bee279dcad5deff16` | `b38c8fd1d01f0fa20fe38b26a94255344e296c83b509640bee279dcad5deff16` | yes |
| 23 | `1793145600-1793205900.0.stream.jsonl.gz` | 9,715,061 | `0afde34b6cf80083b9cdda7bef5baacfa1dc946f61e68886265cb3633f3a3538` | `0afde34b6cf80083b9cdda7bef5baacfa1dc946f61e68886265cb3633f3a3538` | `0afde34b6cf80083b9cdda7bef5baacfa1dc946f61e68886265cb3633f3a3538` | `0afde34b6cf80083b9cdda7bef5baacfa1dc946f61e68886265cb3633f3a3538` | yes |
| 24 | `1793145600-1793206800.0.stream.jsonl.gz` | 11,001,064 | `e9f2f8a8ff6cef04b36b04cbffaaed9b5accf26873d26eed74b85d8dc6199378` | `e9f2f8a8ff6cef04b36b04cbffaaed9b5accf26873d26eed74b85d8dc6199378` | `e9f2f8a8ff6cef04b36b04cbffaaed9b5accf26873d26eed74b85d8dc6199378` | `e9f2f8a8ff6cef04b36b04cbffaaed9b5accf26873d26eed74b85d8dc6199378` | yes |
| 25 | `1793145600-1793207700.0.stream.jsonl.gz` | 9,835,502 | `6eec69739f70d0ac95fa8735d2154567794477b47cc5d9d43f2bfac27bedcc99` | `6eec69739f70d0ac95fa8735d2154567794477b47cc5d9d43f2bfac27bedcc99` | `6eec69739f70d0ac95fa8735d2154567794477b47cc5d9d43f2bfac27bedcc99` | `6eec69739f70d0ac95fa8735d2154567794477b47cc5d9d43f2bfac27bedcc99` | yes |
| 26 | `1793145600-1793208600.0.stream.jsonl.gz` | 9,874,421 | `1084bd093c165ef45f8cbce038465b4a5fcb395d435ef7556d05d85f08169ce5` | `1084bd093c165ef45f8cbce038465b4a5fcb395d435ef7556d05d85f08169ce5` | `1084bd093c165ef45f8cbce038465b4a5fcb395d435ef7556d05d85f08169ce5` | `1084bd093c165ef45f8cbce038465b4a5fcb395d435ef7556d05d85f08169ce5` | yes |
| 27 | `1793145600-1793209500.0.stream.jsonl.gz` | 9,385,489 | `09177e12607a802d3aac38cdf988ec17229af4238b4a87a55224d75117561d73` | `09177e12607a802d3aac38cdf988ec17229af4238b4a87a55224d75117561d73` | `09177e12607a802d3aac38cdf988ec17229af4238b4a87a55224d75117561d73` | `09177e12607a802d3aac38cdf988ec17229af4238b4a87a55224d75117561d73` | yes |
| 28 | `1793145600-1793210400.0.stream.jsonl.gz` | 10,966,063 | `b10381fa9dc7552d8d16e2b480baeb4f6ff30651921c3b89323a0659d8955d58` | `b10381fa9dc7552d8d16e2b480baeb4f6ff30651921c3b89323a0659d8955d58` | `b10381fa9dc7552d8d16e2b480baeb4f6ff30651921c3b89323a0659d8955d58` | `b10381fa9dc7552d8d16e2b480baeb4f6ff30651921c3b89323a0659d8955d58` | yes |
| 29 | `1793145600-1793211300.0.stream.jsonl.gz` | 10,551,024 | `fd8659f6bf0eaba31206970e69ba9f5b0a915c804e73a0dba9815a35dbb90bd7` | `fd8659f6bf0eaba31206970e69ba9f5b0a915c804e73a0dba9815a35dbb90bd7` | `fd8659f6bf0eaba31206970e69ba9f5b0a915c804e73a0dba9815a35dbb90bd7` | `fd8659f6bf0eaba31206970e69ba9f5b0a915c804e73a0dba9815a35dbb90bd7` | yes |
| 30 | `1793145600-1793212200.0.stream.jsonl.gz` | 12,372,196 | `a4e4aa901676ac2ad3585b6cbc7edc0349ed0fffa7e41a744ab602c954738485` | `a4e4aa901676ac2ad3585b6cbc7edc0349ed0fffa7e41a744ab602c954738485` | `a4e4aa901676ac2ad3585b6cbc7edc0349ed0fffa7e41a744ab602c954738485` | `a4e4aa901676ac2ad3585b6cbc7edc0349ed0fffa7e41a744ab602c954738485` | yes |
| 31 | `1793145600-1793213100.0.stream.jsonl.gz` | 11,112,191 | `17b2340abe0d5466dc70c8584c970feb094a07f2ca5d534aae2d4459520efd65` | `17b2340abe0d5466dc70c8584c970feb094a07f2ca5d534aae2d4459520efd65` | `17b2340abe0d5466dc70c8584c970feb094a07f2ca5d534aae2d4459520efd65` | `17b2340abe0d5466dc70c8584c970feb094a07f2ca5d534aae2d4459520efd65` | yes |
| 32 | `1793145600-1793214000.0.stream.jsonl.gz` | 10,918,172 | `9e3d0b9f03b4cbd00834375385767f370ee4a479fd0c1ca54c40052213cce5a5` | `9e3d0b9f03b4cbd00834375385767f370ee4a479fd0c1ca54c40052213cce5a5` | `9e3d0b9f03b4cbd00834375385767f370ee4a479fd0c1ca54c40052213cce5a5` | `9e3d0b9f03b4cbd00834375385767f370ee4a479fd0c1ca54c40052213cce5a5` | yes |
| 33 | `1793145600-1793214900.0.stream.jsonl.gz` | 10,956,690 | `d70fe0f958eb08281fb8c3cf74567121bafeffadc272afebb3b973938eedeba9` | `d70fe0f958eb08281fb8c3cf74567121bafeffadc272afebb3b973938eedeba9` | `d70fe0f958eb08281fb8c3cf74567121bafeffadc272afebb3b973938eedeba9` | `d70fe0f958eb08281fb8c3cf74567121bafeffadc272afebb3b973938eedeba9` | yes |
| 34 | `1793145600-1793215800.0.stream.jsonl.gz` | 10,464,479 | `7f48547a7aa076d1133ab3ffc013aa90a2f0f464eefd55f474c6de7482af44b0` | `7f48547a7aa076d1133ab3ffc013aa90a2f0f464eefd55f474c6de7482af44b0` | `7f48547a7aa076d1133ab3ffc013aa90a2f0f464eefd55f474c6de7482af44b0` | `7f48547a7aa076d1133ab3ffc013aa90a2f0f464eefd55f474c6de7482af44b0` | yes |
| 35 | `1793145600-1793216700.0.stream.jsonl.gz` | 11,797,234 | `87f3efd83e33c5ffe9e9b035a4c5b090b645462a68b0f96645818f91f2997faf` | `87f3efd83e33c5ffe9e9b035a4c5b090b645462a68b0f96645818f91f2997faf` | `87f3efd83e33c5ffe9e9b035a4c5b090b645462a68b0f96645818f91f2997faf` | `87f3efd83e33c5ffe9e9b035a4c5b090b645462a68b0f96645818f91f2997faf` | yes |
| 36 | `1793145600-1793217600.0.stream.jsonl.gz` | 9,947,721 | `1ca2fac80bb178ad476eb69bcf3a26f90fc6c25af5715df82672dd8de84107c0` | `1ca2fac80bb178ad476eb69bcf3a26f90fc6c25af5715df82672dd8de84107c0` | `1ca2fac80bb178ad476eb69bcf3a26f90fc6c25af5715df82672dd8de84107c0` | `1ca2fac80bb178ad476eb69bcf3a26f90fc6c25af5715df82672dd8de84107c0` | yes |
| 37 | `1793145600-1793218500.0.stream.jsonl.gz` | 9,342,830 | `70c9bd544e19d236188538cc43cd89663cd327d6bd516ef442e01ff89f59508a` | `70c9bd544e19d236188538cc43cd89663cd327d6bd516ef442e01ff89f59508a` | `70c9bd544e19d236188538cc43cd89663cd327d6bd516ef442e01ff89f59508a` | `70c9bd544e19d236188538cc43cd89663cd327d6bd516ef442e01ff89f59508a` | yes |
| 38 | `1793145600-1793219400.0.stream.jsonl.gz` | 8,879,554 | `07b12705033d39a7a84982ea7e311d31522b0e4ab09580a5868c83f17c054186` | `07b12705033d39a7a84982ea7e311d31522b0e4ab09580a5868c83f17c054186` | `07b12705033d39a7a84982ea7e311d31522b0e4ab09580a5868c83f17c054186` | `07b12705033d39a7a84982ea7e311d31522b0e4ab09580a5868c83f17c054186` | yes |
| 39 | `1793145600-1793220300.0.stream.jsonl.gz` | 9,062,207 | `0154c6a783d139f1532ec09d9060da71cfd1254552aacfb75ed385f7799d4006` | `0154c6a783d139f1532ec09d9060da71cfd1254552aacfb75ed385f7799d4006` | `0154c6a783d139f1532ec09d9060da71cfd1254552aacfb75ed385f7799d4006` | `0154c6a783d139f1532ec09d9060da71cfd1254552aacfb75ed385f7799d4006` | yes |
| 40 | `1793145600-1793221200.0.stream.jsonl.gz` | 9,372,847 | `57bf808b26b559fdf9f211e59a761fac1f9b8c2dfda86bc3723f984eb5914a08` | `57bf808b26b559fdf9f211e59a761fac1f9b8c2dfda86bc3723f984eb5914a08` | `57bf808b26b559fdf9f211e59a761fac1f9b8c2dfda86bc3723f984eb5914a08` | `57bf808b26b559fdf9f211e59a761fac1f9b8c2dfda86bc3723f984eb5914a08` | yes |
| 41 | `1793145600-1793222100.0.stream.jsonl.gz` | 8,001,926 | `18c0bdb9008b4b40471b5b99a4ddc854c5e6b1f39d9659f479b252a69a8884be` | `18c0bdb9008b4b40471b5b99a4ddc854c5e6b1f39d9659f479b252a69a8884be` | `18c0bdb9008b4b40471b5b99a4ddc854c5e6b1f39d9659f479b252a69a8884be` | `18c0bdb9008b4b40471b5b99a4ddc854c5e6b1f39d9659f479b252a69a8884be` | yes |
| 42 | `1793145600-1793223000.0.stream.jsonl.gz` | 8,114,414 | `f6101c8eb420b9eda97f353d7adcebdc355fbec4bb93ff6a69b6cab57adcaed6` | `f6101c8eb420b9eda97f353d7adcebdc355fbec4bb93ff6a69b6cab57adcaed6` | `f6101c8eb420b9eda97f353d7adcebdc355fbec4bb93ff6a69b6cab57adcaed6` | `f6101c8eb420b9eda97f353d7adcebdc355fbec4bb93ff6a69b6cab57adcaed6` | yes |
| 43 | `1793145600-1793223900.0.stream.jsonl.gz` | 9,006,052 | `86ef7ae2e14ac60b9b57edc530427e2fb33d0a481aa315799106c43e59c0e0e0` | `86ef7ae2e14ac60b9b57edc530427e2fb33d0a481aa315799106c43e59c0e0e0` | `86ef7ae2e14ac60b9b57edc530427e2fb33d0a481aa315799106c43e59c0e0e0` | `86ef7ae2e14ac60b9b57edc530427e2fb33d0a481aa315799106c43e59c0e0e0` | yes |
| 44 | `1793145600-1793224800.0.stream.jsonl.gz` | 8,661,025 | `752e54df1a8237873fa10a40e759b042763c89cb5b87d745b89949d3f20b2e0e` | `752e54df1a8237873fa10a40e759b042763c89cb5b87d745b89949d3f20b2e0e` | `752e54df1a8237873fa10a40e759b042763c89cb5b87d745b89949d3f20b2e0e` | `752e54df1a8237873fa10a40e759b042763c89cb5b87d745b89949d3f20b2e0e` | yes |
| 45 | `1793145600-1793225700.0.stream.jsonl.gz` | 8,132,267 | `9485eb5864c99e37e00d178bd4312b6ef4dc779694a5e4de480941b41bb88297` | `9485eb5864c99e37e00d178bd4312b6ef4dc779694a5e4de480941b41bb88297` | `9485eb5864c99e37e00d178bd4312b6ef4dc779694a5e4de480941b41bb88297` | `9485eb5864c99e37e00d178bd4312b6ef4dc779694a5e4de480941b41bb88297` | yes |
| 46 | `1793145600-1793226600.0.stream.jsonl.gz` | 9,326,449 | `2cdeb8ca3f85fca93e521e3a2151e6d95c5a24d19c61d58e87cec47b18696819` | `2cdeb8ca3f85fca93e521e3a2151e6d95c5a24d19c61d58e87cec47b18696819` | `2cdeb8ca3f85fca93e521e3a2151e6d95c5a24d19c61d58e87cec47b18696819` | `2cdeb8ca3f85fca93e521e3a2151e6d95c5a24d19c61d58e87cec47b18696819` | yes |
| 47 | `1793145600-1793227500.0.stream.jsonl.gz` | 9,815,975 | `ec2d3c0868e6d21c3754d1c290895c080a46c58048103ecb37ede7d4b8edfc3e` | `ec2d3c0868e6d21c3754d1c290895c080a46c58048103ecb37ede7d4b8edfc3e` | `ec2d3c0868e6d21c3754d1c290895c080a46c58048103ecb37ede7d4b8edfc3e` | `ec2d3c0868e6d21c3754d1c290895c080a46c58048103ecb37ede7d4b8edfc3e` | yes |
| 48 | `1793145600-1793228400.0.stream.jsonl.gz` | 9,231,800 | `fef35a594b2704d0984f9bc737782ea2bc46b5f264d0712d9df2c10ffa97924b` | `fef35a594b2704d0984f9bc737782ea2bc46b5f264d0712d9df2c10ffa97924b` | `fef35a594b2704d0984f9bc737782ea2bc46b5f264d0712d9df2c10ffa97924b` | `fef35a594b2704d0984f9bc737782ea2bc46b5f264d0712d9df2c10ffa97924b` | yes |
| 49 | `1793145600-1793229300.0.stream.jsonl.gz` | 8,160,699 | `7ef7d872fc56eeeb309f156a13f8ae10ed68aeeb1b545a566ca7f3a4e4e5e994` | `7ef7d872fc56eeeb309f156a13f8ae10ed68aeeb1b545a566ca7f3a4e4e5e994` | `7ef7d872fc56eeeb309f156a13f8ae10ed68aeeb1b545a566ca7f3a4e4e5e994` | `7ef7d872fc56eeeb309f156a13f8ae10ed68aeeb1b545a566ca7f3a4e4e5e994` | yes |
| 50 | `1793145600-1793230200.0.stream.jsonl.gz` | 8,889,088 | `c2b14f9702d26b6853601d83b685113b6f5650d2b86c644724e87d1f619eec17` | `c2b14f9702d26b6853601d83b685113b6f5650d2b86c644724e87d1f619eec17` | `c2b14f9702d26b6853601d83b685113b6f5650d2b86c644724e87d1f619eec17` | `c2b14f9702d26b6853601d83b685113b6f5650d2b86c644724e87d1f619eec17` | yes |
| 51 | `1793145600-1793231100.0.stream.jsonl.gz` | 9,143,917 | `e177b5e38f162522be08df4692d8789e36a8a8a83ee5cf9856940a05dbaf955a` | `e177b5e38f162522be08df4692d8789e36a8a8a83ee5cf9856940a05dbaf955a` | `e177b5e38f162522be08df4692d8789e36a8a8a83ee5cf9856940a05dbaf955a` | `e177b5e38f162522be08df4692d8789e36a8a8a83ee5cf9856940a05dbaf955a` | yes |
| 52 | `1793232000-1793232000.0.stream.jsonl.gz` | 11,579,610 | `bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f` | `bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f` | `bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f` | `bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f` | yes |
| 53 | `1793232000-1793232900.0.stream.jsonl.gz` | 10,715,152 | `46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370` | `46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370` | `46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370` | `46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370` | yes |
| 54 | `1793232000-1793233800.0.stream.jsonl.gz` | 11,443,056 | `2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9` | `2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9` | `2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9` | `2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9` | yes |
| 55 | `1793232000-1793234700.0.stream.jsonl.gz` | 13,592,154 | `ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496` | `ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496` | `ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496` | `ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496` | yes |
| 56 | `1793232000-1793235600.0.stream.jsonl.gz` | 11,481,990 | `13cfa07ef0b2a4b17c6dfd8a73acb7124fcaaab9efcc0630e3b35075c6a68806` | `13cfa07ef0b2a4b17c6dfd8a73acb7124fcaaab9efcc0630e3b35075c6a68806` | `13cfa07ef0b2a4b17c6dfd8a73acb7124fcaaab9efcc0630e3b35075c6a68806` | `13cfa07ef0b2a4b17c6dfd8a73acb7124fcaaab9efcc0630e3b35075c6a68806` | yes |
| 57 | `1793232000-1793236500.0.stream.jsonl.gz` | 11,586,307 | `4b674d438d19c52d763fcd8a3dafd852a7d509db0dce8aea6cb31b7723e193a1` | `4b674d438d19c52d763fcd8a3dafd852a7d509db0dce8aea6cb31b7723e193a1` | `4b674d438d19c52d763fcd8a3dafd852a7d509db0dce8aea6cb31b7723e193a1` | `4b674d438d19c52d763fcd8a3dafd852a7d509db0dce8aea6cb31b7723e193a1` | yes |
| 58 | `1793232000-1793237400.0.stream.jsonl.gz` | 10,660,664 | `a165ef62af692053180e8b84920e9b63dbdda4f2599c4e62531e5f6ca379f125` | `a165ef62af692053180e8b84920e9b63dbdda4f2599c4e62531e5f6ca379f125` | `a165ef62af692053180e8b84920e9b63dbdda4f2599c4e62531e5f6ca379f125` | `a165ef62af692053180e8b84920e9b63dbdda4f2599c4e62531e5f6ca379f125` | yes |
| 59 | `1793232000-1793238300.0.stream.jsonl.gz` | 10,776,660 | `b412acf84336b17ffd7722035c2ea162dd1d40cf0199e27e74e97ea939f77f6f` | `b412acf84336b17ffd7722035c2ea162dd1d40cf0199e27e74e97ea939f77f6f` | `b412acf84336b17ffd7722035c2ea162dd1d40cf0199e27e74e97ea939f77f6f` | `b412acf84336b17ffd7722035c2ea162dd1d40cf0199e27e74e97ea939f77f6f` | yes |
| 60 | `1793232000-1793239200.0.stream.jsonl.gz` | 10,626,770 | `10a349f090734e3edfa6b57293ab0792e3be068f003fd282cd21d016f1191329` | `10a349f090734e3edfa6b57293ab0792e3be068f003fd282cd21d016f1191329` | `10a349f090734e3edfa6b57293ab0792e3be068f003fd282cd21d016f1191329` | `10a349f090734e3edfa6b57293ab0792e3be068f003fd282cd21d016f1191329` | yes |
| 61 | `1793232000-1793240100.0.stream.jsonl.gz` | 9,792,424 | `9af6e8ce44bfb351dec406b7238800bcfd9e1c923eda19108ee90f932d1ccd77` | `9af6e8ce44bfb351dec406b7238800bcfd9e1c923eda19108ee90f932d1ccd77` | `9af6e8ce44bfb351dec406b7238800bcfd9e1c923eda19108ee90f932d1ccd77` | `9af6e8ce44bfb351dec406b7238800bcfd9e1c923eda19108ee90f932d1ccd77` | yes |
| 62 | `1793232000-1793241000.0.stream.jsonl.gz` | 10,745,728 | `97af9463ab66cb91cb988edb643ed299242b31b1a178a127a329bc519553656c` | `97af9463ab66cb91cb988edb643ed299242b31b1a178a127a329bc519553656c` | `97af9463ab66cb91cb988edb643ed299242b31b1a178a127a329bc519553656c` | `97af9463ab66cb91cb988edb643ed299242b31b1a178a127a329bc519553656c` | yes |
| 63 | `1793232000-1793241900.0.stream.jsonl.gz` | 11,272,730 | `56523b9b4864aa1d68356887683b08e62cc114356a412b912d0a48f1cb71cce9` | `56523b9b4864aa1d68356887683b08e62cc114356a412b912d0a48f1cb71cce9` | `56523b9b4864aa1d68356887683b08e62cc114356a412b912d0a48f1cb71cce9` | `56523b9b4864aa1d68356887683b08e62cc114356a412b912d0a48f1cb71cce9` | yes |
| 64 | `1793232000-1793242800.0.stream.jsonl.gz` | 9,774,209 | `0ea58656eab189fc7fe4c12f19565ae1f8e78a16914e4556077ee7357dd66bf8` | `0ea58656eab189fc7fe4c12f19565ae1f8e78a16914e4556077ee7357dd66bf8` | `0ea58656eab189fc7fe4c12f19565ae1f8e78a16914e4556077ee7357dd66bf8` | `0ea58656eab189fc7fe4c12f19565ae1f8e78a16914e4556077ee7357dd66bf8` | yes |
| 65 | `1793232000-1793243700.0.stream.jsonl.gz` | 9,321,701 | `351bc4fb1ecaddc7a7d7706b8c0bdf9dae2c923bff1587739c0b25b84dc27dce` | `351bc4fb1ecaddc7a7d7706b8c0bdf9dae2c923bff1587739c0b25b84dc27dce` | `351bc4fb1ecaddc7a7d7706b8c0bdf9dae2c923bff1587739c0b25b84dc27dce` | `351bc4fb1ecaddc7a7d7706b8c0bdf9dae2c923bff1587739c0b25b84dc27dce` | yes |
| 66 | `1793232000-1793244600.0.stream.jsonl.gz` | 10,295,145 | `4c5ea876926595b876b57674ed22ac762dee89bd562b31b41ca1b46c8d8f0941` | `4c5ea876926595b876b57674ed22ac762dee89bd562b31b41ca1b46c8d8f0941` | `4c5ea876926595b876b57674ed22ac762dee89bd562b31b41ca1b46c8d8f0941` | `4c5ea876926595b876b57674ed22ac762dee89bd562b31b41ca1b46c8d8f0941` | yes |
| 67 | `1793232000-1793245500.0.stream.jsonl.gz` | 10,434,441 | `965536189680879129c4b791b2ce4e3f2d6f7b4afc652e3667f4f26badfffe5c` | `965536189680879129c4b791b2ce4e3f2d6f7b4afc652e3667f4f26badfffe5c` | `965536189680879129c4b791b2ce4e3f2d6f7b4afc652e3667f4f26badfffe5c` | `965536189680879129c4b791b2ce4e3f2d6f7b4afc652e3667f4f26badfffe5c` | yes |
| 68 | `1793232000-1793246400.0.stream.jsonl.gz` | 11,156,773 | `aa32bc8025e820129068a744811070c5d22a99fbee05f075c224ebdd6acdbee0` | `aa32bc8025e820129068a744811070c5d22a99fbee05f075c224ebdd6acdbee0` | `aa32bc8025e820129068a744811070c5d22a99fbee05f075c224ebdd6acdbee0` | `aa32bc8025e820129068a744811070c5d22a99fbee05f075c224ebdd6acdbee0` | yes |
| 69 | `1793232000-1793247300.0.stream.jsonl.gz` | 11,456,592 | `01702655f10a63f295b19dfeb9d0ba9b88c3c9ce31d44a9a8f2c08fe62cd00dd` | `01702655f10a63f295b19dfeb9d0ba9b88c3c9ce31d44a9a8f2c08fe62cd00dd` | `01702655f10a63f295b19dfeb9d0ba9b88c3c9ce31d44a9a8f2c08fe62cd00dd` | `01702655f10a63f295b19dfeb9d0ba9b88c3c9ce31d44a9a8f2c08fe62cd00dd` | yes |
| 70 | `1793232000-1793248200.0.stream.jsonl.gz` | 11,804,877 | `2aae850163314c07ec63ef9432003a577595c5d8d9e14fe6477a3dd22aa6b1ac` | `2aae850163314c07ec63ef9432003a577595c5d8d9e14fe6477a3dd22aa6b1ac` | `2aae850163314c07ec63ef9432003a577595c5d8d9e14fe6477a3dd22aa6b1ac` | `2aae850163314c07ec63ef9432003a577595c5d8d9e14fe6477a3dd22aa6b1ac` | yes |
| 71 | `1793232000-1793249100.0.stream.jsonl.gz` | 11,704,215 | `7956e72362c84c21af181ca4735693b0a46f140ffd8bb873cac388937b2d990f` | `7956e72362c84c21af181ca4735693b0a46f140ffd8bb873cac388937b2d990f` | `7956e72362c84c21af181ca4735693b0a46f140ffd8bb873cac388937b2d990f` | `7956e72362c84c21af181ca4735693b0a46f140ffd8bb873cac388937b2d990f` | yes |
| 72 | `1793232000-1793250000.0.stream.jsonl.gz` | 9,914,992 | `c7a1c8ac59d83e2c523000877d723b086dcea022249cc5ac8473b01e29328402` | `c7a1c8ac59d83e2c523000877d723b086dcea022249cc5ac8473b01e29328402` | `c7a1c8ac59d83e2c523000877d723b086dcea022249cc5ac8473b01e29328402` | `c7a1c8ac59d83e2c523000877d723b086dcea022249cc5ac8473b01e29328402` | yes |
| 73 | `1793232000-1793250900.0.stream.jsonl.gz` | 10,553,162 | `2881a9c50f4ed4779dd38d087a5bdf08c0a0b615388d99903d3f521f41eff5d8` | `2881a9c50f4ed4779dd38d087a5bdf08c0a0b615388d99903d3f521f41eff5d8` | `2881a9c50f4ed4779dd38d087a5bdf08c0a0b615388d99903d3f521f41eff5d8` | `2881a9c50f4ed4779dd38d087a5bdf08c0a0b615388d99903d3f521f41eff5d8` | yes |
| 74 | `1793232000-1793251800.0.stream.jsonl.gz` | 6,547,939 | `665482155d2c89d4d90d723481ade034d3fa140f3fecb1c9f763955265058b0e` | `665482155d2c89d4d90d723481ade034d3fa140f3fecb1c9f763955265058b0e` | `665482155d2c89d4d90d723481ade034d3fa140f3fecb1c9f763955265058b0e` | `665482155d2c89d4d90d723481ade034d3fa140f3fecb1c9f763955265058b0e` | yes |
| 75 | `1793232000-1793252700.0.stream.jsonl.gz` | 6,710,655 | `1ae001465bda15ecb0baac234006e6a6caeb300d3b4af38e03836ad74911d9b6` | `1ae001465bda15ecb0baac234006e6a6caeb300d3b4af38e03836ad74911d9b6` | `1ae001465bda15ecb0baac234006e6a6caeb300d3b4af38e03836ad74911d9b6` | `1ae001465bda15ecb0baac234006e6a6caeb300d3b4af38e03836ad74911d9b6` | yes |
| 76 | `1793232000-1793253600.0.stream.jsonl.gz` | 10,468,900 | `abacdc803e50c358dcbb303c389571da57f2ee9f9d53e15b2d55c97ad40f3c3f` | `abacdc803e50c358dcbb303c389571da57f2ee9f9d53e15b2d55c97ad40f3c3f` | `abacdc803e50c358dcbb303c389571da57f2ee9f9d53e15b2d55c97ad40f3c3f` | `abacdc803e50c358dcbb303c389571da57f2ee9f9d53e15b2d55c97ad40f3c3f` | yes |
| 77 | `1793232000-1793254500.0.stream.jsonl.gz` | 11,330,444 | `ecbbccb1a14d1930a4896d80cdaf1ab6d2b7fd1acfe89d44890f217520eaff7b` | `ecbbccb1a14d1930a4896d80cdaf1ab6d2b7fd1acfe89d44890f217520eaff7b` | `ecbbccb1a14d1930a4896d80cdaf1ab6d2b7fd1acfe89d44890f217520eaff7b` | `ecbbccb1a14d1930a4896d80cdaf1ab6d2b7fd1acfe89d44890f217520eaff7b` | yes |
| 78 | `1793232000-1793255400.0.stream.jsonl.gz` | 10,581,288 | `e4639bf5a1fa0c5cf5e34da606963fe376f9c1c151c944c01ca5456a8b6cc496` | `e4639bf5a1fa0c5cf5e34da606963fe376f9c1c151c944c01ca5456a8b6cc496` | `e4639bf5a1fa0c5cf5e34da606963fe376f9c1c151c944c01ca5456a8b6cc496` | `e4639bf5a1fa0c5cf5e34da606963fe376f9c1c151c944c01ca5456a8b6cc496` | yes |
| 79 | `1793232000-1793256300.0.stream.jsonl.gz` | 9,852,787 | `86979d6d01fbf239cbc6e10601b10b55cff7ef99c19ed624b395f459fce20c96` | `86979d6d01fbf239cbc6e10601b10b55cff7ef99c19ed624b395f459fce20c96` | `86979d6d01fbf239cbc6e10601b10b55cff7ef99c19ed624b395f459fce20c96` | `86979d6d01fbf239cbc6e10601b10b55cff7ef99c19ed624b395f459fce20c96` | yes |
| 80 | `1793232000-1793257200.0.stream.jsonl.gz` | 12,148,871 | `ab604e14fa82be607598b858b7cd069d9c79fc1ecbbb38c80b0b104556062abd` | `ab604e14fa82be607598b858b7cd069d9c79fc1ecbbb38c80b0b104556062abd` | `ab604e14fa82be607598b858b7cd069d9c79fc1ecbbb38c80b0b104556062abd` | `ab604e14fa82be607598b858b7cd069d9c79fc1ecbbb38c80b0b104556062abd` | yes |
| 81 | `1793232000-1793258100.0.stream.jsonl.gz` | 13,568,827 | `ff1db96bb157f72ab0c6d2a33fc8b950d9cda13c2cdbc95cd748b4175652bfe4` | `ff1db96bb157f72ab0c6d2a33fc8b950d9cda13c2cdbc95cd748b4175652bfe4` | `ff1db96bb157f72ab0c6d2a33fc8b950d9cda13c2cdbc95cd748b4175652bfe4` | `ff1db96bb157f72ab0c6d2a33fc8b950d9cda13c2cdbc95cd748b4175652bfe4` | yes |
| 82 | `1793232000-1793259000.0.stream.jsonl.gz` | 11,991,341 | `6897e0b6bb2b55df7d152556adf5134ea8e5365034dcc15ddbca00bcef9f701b` | `6897e0b6bb2b55df7d152556adf5134ea8e5365034dcc15ddbca00bcef9f701b` | `6897e0b6bb2b55df7d152556adf5134ea8e5365034dcc15ddbca00bcef9f701b` | `6897e0b6bb2b55df7d152556adf5134ea8e5365034dcc15ddbca00bcef9f701b` | yes |
| 83 | `1793232000-1793259900.0.stream.jsonl.gz` | 12,726,821 | `0d22a5647d7636d7caa05eec6d0fb692b5d68cff96459799bfa2acb8579644e3` | `0d22a5647d7636d7caa05eec6d0fb692b5d68cff96459799bfa2acb8579644e3` | `0d22a5647d7636d7caa05eec6d0fb692b5d68cff96459799bfa2acb8579644e3` | `0d22a5647d7636d7caa05eec6d0fb692b5d68cff96459799bfa2acb8579644e3` | yes |
| 84 | `1793232000-1793260800.0.stream.jsonl.gz` | 14,804,505 | `b839cd4c19f7851e7493c2cabe48e8c40b8bf08a97fc1a3363c52d92c176efdf` | `b839cd4c19f7851e7493c2cabe48e8c40b8bf08a97fc1a3363c52d92c176efdf` | `b839cd4c19f7851e7493c2cabe48e8c40b8bf08a97fc1a3363c52d92c176efdf` | `b839cd4c19f7851e7493c2cabe48e8c40b8bf08a97fc1a3363c52d92c176efdf` | yes |
| 85 | `1793232000-1793261700.0.stream.jsonl.gz` | 12,815,998 | `8f724133bc113ff6d30bc03d266711ca940aa0ccb4f244674566f14623556a08` | `8f724133bc113ff6d30bc03d266711ca940aa0ccb4f244674566f14623556a08` | `8f724133bc113ff6d30bc03d266711ca940aa0ccb4f244674566f14623556a08` | `8f724133bc113ff6d30bc03d266711ca940aa0ccb4f244674566f14623556a08` | yes |
| 86 | `1793232000-1793262600.0.stream.jsonl.gz` | 14,933,789 | `9c3aa5375f8405416226c860be5b8af5904b3a786c390271296e034260e5af25` | `9c3aa5375f8405416226c860be5b8af5904b3a786c390271296e034260e5af25` | `9c3aa5375f8405416226c860be5b8af5904b3a786c390271296e034260e5af25` | `9c3aa5375f8405416226c860be5b8af5904b3a786c390271296e034260e5af25` | yes |

**86 of 86 rows equal in all four hashes; 890,975,956 bytes in all.**

### 2.10 §3.8 — final: G-TIMER and G-STILL (V10)

```
2026-10-29T09:31:53.874043037Z
[2026-10-29T09:31:54Z] G-TIMER loaded                   True
[2026-10-29T09:31:54Z] G-TIMER active                   True
[2026-10-29T09:31:54Z] G-TIMER enabled                  True
[2026-10-29T09:31:54Z] G-TIMER fragment                 True
[2026-10-29T09:31:54Z] G-TIMER its unit                 True
[2026-10-29T09:31:54Z] G-TIMER the calendar             True
[2026-10-29T09:31:54Z] G-TIMER 1,800 s after it starts  True
[2026-10-29T09:31:54Z] G-TIMER accuracy 1 s             True
[2026-10-29T09:31:54Z] G-TIMER the next calendar elapse True
[2026-10-29T09:31:54Z] btc-pairbook.service {'MainPID': '3216422', 'NRestarts': '12', 'ActiveState': 'active'}, MemoryCurrent 20373504, MemoryPeak 76881920
[2026-10-29T09:31:54Z] btc-recorder.service {'MainPID': '2388318', 'NRestarts': '0', 'ActiveState': 'active'}, MemoryCurrent 56430592, MemoryPeak 302309376
[2026-10-29T09:31:54Z] btc-rewardbook.service {'MainPID': '3137952', 'NRestarts': '1', 'ActiveState': 'active'}, MemoryCurrent 19312640, MemoryPeak 60887040
[2026-10-29T09:31:54Z] btc-pairbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-29T09:31:54Z] btc-pairbook-archive.service {'Result': 'exit-code', 'ActiveState': 'failed', 'SubState': 'failed', 'UnitFileState': 'static'}
[2026-10-29T09:31:54Z] btc-rewardbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-29T09:31:54Z] btc-rewardbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-29T09:31:54Z] G-STILL PASS: unchanged since 2026-10-29T07:46:51Z
[2026-10-29T09:31:54Z] the store: 2 day directories, 1793145600 to 1793232000; its stream files 38055420 bytes; free 11126837248 bytes
[2026-10-29T09:31:54Z] the last set's rate: 1006278727 bytes a day
[2026-10-29T09:31:54Z] at that rate the cap stops the streams in 3.94 days, at 2026-11-02T08:01:30Z
[2026-10-29T09:31:54Z] at that rate the floor, base 43500000 bytes a day stops the streams in 3.65 days, at 2026-11-02T01:01:14Z
[2026-10-29T09:31:54Z] at that rate the floor, base 187760570 bytes a day stops the streams in 3.20 days, at 2026-11-01T14:27:01Z
[2026-10-29T09:31:54Z] the next run at 2026-10-30T01:30:20Z; the ledger 9 records
[2026-10-29T09:31:54Z] FINAL PASS
[2026-10-29T09:31:54Z] peak memory of this run: 37941248 bytes
[2026-10-29T09:31:54Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

**FINAL PASS**: G-TIMER 9 of 9; **G-STILL PASS, `unchanged since 2026-10-29T07:46:51Z`** — the pair book's archive restarted nothing, its one run in the span having deferred before its removal. The projection at the last set's rate, `1,006,278,727` bytes a day: the cap stops the streams at 2026-11-02 08:01:30 UTC, the floor at 2026-11-02 01:01:14 at the slowest base drain and 2026-11-01 14:27:01 at the fastest — each beyond the next calendar run, 2026-10-30 01:30:20 UTC.

### 2.11 Each unit's memory, at every read

| instant (UTC) | read by | `btc-recorder` current / peak | `btc-pairbook` current / peak | `btc-rewardbook` current / peak | `btc-rewardbook-archive.service` peak |
|---|---|---|---|---|---|
| 07:46:51 | `still` | 13,201,408 / 302,309,376 | 8,982,528 / 76,881,920 | 20,070,400 / 60,887,040 | — |
| 09:31:54 | `final` | 56,430,592 / 302,309,376 | 20,373,504 / 76,881,920 | 19,312,640 / 60,887,040 | — |
| 09:32:14 | §3.9 | 5,578,752 / 302,309,376 | 3,227,648 / 76,881,920 | 14,614,528 / 60,887,040 | 28,647,424 |

The archive's journal: the second invocation `Consumed 6.318s CPU time, 27.3M memory peak`; the first `Consumed 8.245s CPU time`; under `MemoryMax=128M`.

### 2.12 The runs of the pair book's archive that this session's reloads set off

| reload | instant | the archive's run | result |
|---|---|---|---|
| B-INSTALL's `daemon-reload`, `L` | 07:49:22.127 UTC | 07:59:22 UTC, `L + 600`, the tag `pairbook-streams-1793260762` | **exit `75`, deferred, at 08:02:57 UTC**; the pair book not restarted |
| B-ENABLE's `systemctl enable`, `E` | 08:17:05–07 UTC | **none**: `list-timers` read its next elapse 2026-10-30 03:00:20 UTC at 08:17:38 and at 09:32:14, its last 07:59:22 | — |

K-34 and B-UNINSTALL did not run, so no other reload. The archive's deferred set is resumed by its calendar run of 2026-10-30 03:00:20 UTC; its tag `pairbook-streams-1793260762` reads at `d8194fd…` in the refs of §2.13.

### 2.13 §3.9 — the closing reads (V13), contract §4.2's self-check (V12) and the refs at the end

§0.3's block again — H5 now reads the archive installed, each path `exit=0` — then §3.9's own reads:

```
Thu Oct 29 09:32:14 AM UTC 2026
1793266334
1
MemTotal:         978640 kB
MemAvailable:     256996 kB
SwapTotal:       3174396 kB
SwapFree:        2683808 kB
2026-08-02 07:24:32
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
 -5 23a31fad2f064f04b9e138eac29658f3 Sun 2026-06-21 21:37:37 UTC Fri 2026-06-26 14:13:44 UTC
 -4 a38e17445ce341bc8b877be9d3d4f648 Fri 2026-06-26 14:13:52 UTC Tue 2026-07-14 16:15:10 UTC
 -3 5f4d18a6ba8041bd80e7d1e192c5ee28 Tue 2026-07-14 16:15:20 UTC Fri 2026-07-17 01:01:21 UTC
 -2 b1b399c70c6e4dcc934755f70a2ca231 Fri 2026-07-17 01:01:43 UTC Fri 2026-07-24 14:55:46 UTC
 -1 285d6962c92c407d837d1ce329b93aa4 Fri 2026-07-24 14:55:54 UTC Sun 2026-08-02 07:23:49 UTC
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-02 07:24:34 UTC Thu 2026-10-29 09:32:00 UTC
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11126423552
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
3
3.12.3
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
NEXT                         LEFT LAST                              PASSED UNIT                       ACTIVATES
Thu 2026-10-29 09:58:23 UTC 26min Wed 2026-10-28 23:40:52 UTC       9h ago apt-daily.timer            apt-daily.service
Fri 2026-10-30 03:00:20 UTC   17h Thu 2026-10-29 07:59:22 UTC 1h 32min ago btc-pairbook-archive.timer btc-pairbook-archive.service
Fri 2026-10-30 06:40:01 UTC   21h Thu 2026-10-29 06:19:40 UTC 3h 12min ago apt-daily-upgrade.timer    apt-daily-upgrade.service

3 timers listed.
btc-recorder.service cmp exit=0
btc-pairbook.service cmp exit=0
btc-pairbook-archive.service cmp exit=0
btc-pairbook-archive.timer cmp exit=0
btc-rewardbook.service cmp exit=0
2dcd70e08b18b93c64bb67d9849ac1216ce40e41
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670  /root/btc-rewardbook-svc/tz33-reward-book-capture.py
46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4  /root/btc-pairbook-archive-svc/tz28-pairbook-archive-timer.py
2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673  /root/btc-pairbook-archive-svc/tz27-pairbook-archive.py
/root/btc-rewardbook-archive-svc exit=0
/var/lib/btc-rewardbook-archive exit=0
/etc/systemd/system/btc-rewardbook-archive.service exit=0
/etc/systemd/system/btc-rewardbook-archive.timer exit=0
/root/tz33-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
/root/btc-pairbook-archive-svc exit=0
/var/lib/btc-pairbook-archive exit=0
/root/btc-rewardbook-svc exit=0
/var/lib/btc-rewardbook exit=0
75160 /var/lib/btc-pairbook-archive/ledger.jsonl
9200 /var/lib/btc-rewardbook/runtime.jsonl
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
2101
/root/btc-5m-twap       0968707 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/root/tz34-work/wt      6a61525 [tz-34-rewardbook-archive-timer]
54736039	/var/lib/btc-rewardbook
588648341	/var/lib/btc-pairbook
11472150	/var/lib/btc-pairbook-archive
117941762	/root/.claude
660035157	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/540c6c83-4413-5ceb-86a4-2d45c7f8989a/scratchpad
total 16
drwx------  4 root root 4096 Oct 29 07:48 .
drwx------ 32 root root 4096 Oct 29 07:43 ..
drwx------  4 root root 4096 Oct 29 07:43 540c6c83-4413-5ceb-86a4-2d45c7f8989a
drwx------  3 root root 4096 Oct 29 07:43 57feec2d-2369-4cb0-9cad-8ac28cb7e578
===== section 3.9 =====
MainPID=2388318
NRestarts=0
MemoryCurrent=5578752
MemoryPeak=302309376
Id=btc-recorder.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC

MainPID=3216422
NRestarts=12
MemoryCurrent=3227648
MemoryPeak=76881920
Id=btc-pairbook.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Thu 2026-10-29 03:05:31 UTC

MainPID=3137952
NRestarts=1
MemoryCurrent=14614528
MemoryPeak=60887040
Id=btc-rewardbook.service
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Wed 2026-10-28 12:56:29 UTC

MainPID=0
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=[not set]
Id=btc-pairbook-archive.service
ActiveState=failed
UnitFileState=static
ActiveEnterTimestamp=

Id=btc-pairbook-archive.timer
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-11 15:08:11 UTC

MainPID=0
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=28647424
Id=btc-rewardbook-archive.service
ActiveState=inactive
UnitFileState=static
ActiveEnterTimestamp=

Id=btc-rewardbook-archive.timer
ActiveState=active
UnitFileState=enabled
ActiveEnterTimestamp=Thu 2026-10-29 08:17:07 UTC
NEXT                        LEFT LAST                              PASSED UNIT                         ACTIVATES
Fri 2026-10-30 01:30:20 UTC  15h Thu 2026-10-29 08:47:07 UTC    45min ago btc-rewardbook-archive.timer btc-rewardbook-archive.service
Fri 2026-10-30 03:00:20 UTC  17h Thu 2026-10-29 07:59:22 UTC 1h 32min ago btc-pairbook-archive.timer   btc-pairbook-archive.service

2 timers listed.
2026-10-29T08:17:07+00:00 vultr systemd[1]: Started btc-rewardbook-archive.timer - btc-5m-twap reward book archive, once a day.
2026-10-29T08:47:07+00:00 vultr systemd[1]: Starting btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release...
2026-10-29T08:51:11+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Main process exited, code=exited, status=75/TEMPFAIL
2026-10-29T08:51:11+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Failed with result 'exit-code'.
2026-10-29T08:51:11+00:00 vultr systemd[1]: Failed to start btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release.
2026-10-29T08:51:11+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Consumed 8.245s CPU time.
2026-10-29T09:01:12+00:00 vultr systemd[1]: Starting btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release...
2026-10-29T09:04:31+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Deactivated successfully.
2026-10-29T09:04:31+00:00 vultr systemd[1]: Finished btc-rewardbook-archive.service - btc-5m-twap reward book archive, the stream files of closed slots to a Release.
2026-10-29T09:04:31+00:00 vultr systemd[1]: btc-rewardbook-archive.service: Consumed 6.318s CPU time, 27.3M memory peak, 0B memory swap peak.
-- No entries --
[2026-10-29T09:04:28Z] V 1793232000-1793248200.0.stream.jsonl.gz id 687923367 state uploaded api True bytes 11804877 digest sha256:2aae850163314c07ec63ef9432003a577595c5d8d9e14fe6477a3dd22aa6b1ac url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793249100.0.stream.jsonl.gz id 687923404 state uploaded api True bytes 11704215 digest sha256:7956e72362c84c21af181ca4735693b0a46f140ffd8bb873cac388937b2d990f url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793250000.0.stream.jsonl.gz id 687923453 state uploaded api True bytes 9914992 digest sha256:c7a1c8ac59d83e2c523000877d723b086dcea022249cc5ac8473b01e29328402 url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793250900.0.stream.jsonl.gz id 687923493 state uploaded api True bytes 10553162 digest sha256:2881a9c50f4ed4779dd38d087a5bdf08c0a0b615388d99903d3f521f41eff5d8 url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793251800.0.stream.jsonl.gz id 687923547 state uploaded api True bytes 6547939 digest sha256:665482155d2c89d4d90d723481ade034d3fa140f3fecb1c9f763955265058b0e url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793252700.0.stream.jsonl.gz id 687923594 state uploaded api True bytes 6710655 digest sha256:1ae001465bda15ecb0baac234006e6a6caeb300d3b4af38e03836ad74911d9b6 url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793253600.0.stream.jsonl.gz id 687923627 state uploaded api True bytes 10468900 digest sha256:abacdc803e50c358dcbb303c389571da57f2ee9f9d53e15b2d55c97ad40f3c3f url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793254500.0.stream.jsonl.gz id 687923661 state uploaded api True bytes 11330444 digest sha256:ecbbccb1a14d1930a4896d80cdaf1ab6d2b7fd1acfe89d44890f217520eaff7b url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793255400.0.stream.jsonl.gz id 687923701 state uploaded api True bytes 10581288 digest sha256:e4639bf5a1fa0c5cf5e34da606963fe376f9c1c151c944c01ca5456a8b6cc496 url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793256300.0.stream.jsonl.gz id 687923728 state uploaded api True bytes 9852787 digest sha256:86979d6d01fbf239cbc6e10601b10b55cff7ef99c19ed624b395f459fce20c96 url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793257200.0.stream.jsonl.gz id 687923760 state uploaded api True bytes 12148871 digest sha256:ab604e14fa82be607598b858b7cd069d9c79fc1ecbbb38c80b0b104556062abd url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793258100.0.stream.jsonl.gz id 687923823 state uploaded api True bytes 13568827 digest sha256:ff1db96bb157f72ab0c6d2a33fc8b950d9cda13c2cdbc95cd748b4175652bfe4 url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793259000.0.stream.jsonl.gz id 687923913 state uploaded api True bytes 11991341 digest sha256:6897e0b6bb2b55df7d152556adf5134ea8e5365034dcc15ddbca00bcef9f701b url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793259900.0.stream.jsonl.gz id 687923970 state uploaded api True bytes 12726821 digest sha256:0d22a5647d7636d7caa05eec6d0fb692b5d68cff96459799bfa2acb8579644e3 url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793260800.0.stream.jsonl.gz id 687924031 state uploaded api True bytes 14804505 digest sha256:b839cd4c19f7851e7493c2cabe48e8c40b8bf08a97fc1a3363c52d92c176efdf url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793261700.0.stream.jsonl.gz id 687924077 state uploaded api True bytes 12815998 digest sha256:8f724133bc113ff6d30bc03d266711ca940aa0ccb4f244674566f14623556a08 url True download True
[2026-10-29T09:04:28Z] V 1793232000-1793262600.0.stream.jsonl.gz id 687924110 state uploaded api True bytes 14933789 digest sha256:9c3aa5375f8405416226c860be5b8af5904b3a786c390271296e034260e5af25 url True download True
[2026-10-29T09:04:28Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-29T09:04:28Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-29T09:04:28Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-29T09:04:28Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-29T09:04:28Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-29T09:04:28Z] L {"assets_n": 86, "bytes_total": 890975956, "event": "verify", "release_id": 427629503, "run": 1793263627, "verify_sha256": "dad6b5783342c244dcc7fb8d5540b8c6176c809c4a1dd9204a3cc2eb6c6c4379", "wall_ns": 1793264668099816309}
[2026-10-29T09:04:28Z] X 1793145600-1793187000.0.stream.jsonl.gz 9629579 121ae8ad5aaffa260737f6d5ea469e4792e7d7793f7db604e4f6152bc7504916 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793187900.0.stream.jsonl.gz 9639138 37ad0796a091fb6a9b088c0c266d0cbbd88e104c670d8efd33c670c4abf2a823 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793188800.0.stream.jsonl.gz 10430786 ad85da3abf58feedae79d68ebfb8d0a402f25acd40459d96f28ea9a47c70bb96 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793189700.0.stream.jsonl.gz 10844068 c91f3297a636a3e239bfa529c3804cf626f66765c5b3256afe04c1a301061039 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793190600.0.stream.jsonl.gz 11422263 ab9b26074465807668fd298a824ec53d5bf3678ea7452b37ab44ea2f3d145d5f removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793191500.0.stream.jsonl.gz 8669289 4aff733af5bc9e08e2996011967bab6fc0a58bb5230961f7fcc3f488d4fc7f6e removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793191500.1.stream.jsonl.gz 2824343 7bfe046788a1f35db8bf621b1608b3262bb7405340ca88931bd74b821c501f1f removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793192400.0.stream.jsonl.gz 11723039 8028f8a9d828d6c1e94d383faae0d68af94675d1f2ba57a568ec34962bd6e06b removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793193300.0.stream.jsonl.gz 10919554 0d49767ed12888f2994c6e6e8a8ecdd6a2d540713db437bb46c8c73a97718275 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793194200.0.stream.jsonl.gz 9958510 a61297412d0223c0dd827965661a609463b26136d71bc0bb403723491b871d9a removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793195100.0.stream.jsonl.gz 10225257 10fd14580576dcf7d2ba5b34377db1c0ab94909089504afdf4e3b831958fe731 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793196000.0.stream.jsonl.gz 9759422 e8765455d1f1f783288f086027d3b198cf31741944bd5a188b22565345983481 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793196900.0.stream.jsonl.gz 9780710 88c2c84708ab437c4fe5fce3f84776211e62fd1dd5af70fdba40f1894897bdd0 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793197800.0.stream.jsonl.gz 9880467 a5d99308e054693a039d9ee64579ca5015652f140ff1fdd9dac8e9cb72e4eb3a removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793198700.0.stream.jsonl.gz 11208381 075da9e7c5a711a1c555cf14c07cdadc4121ac49e6355d05b7f9e7875094af61 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793199600.0.stream.jsonl.gz 12025155 c70cf12a975796105a875b8f8d7a73682ec557cd30ffd0dd0f051ae2ea90adc3 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793200500.0.stream.jsonl.gz 10028151 8a2b4f911f7467b3ce3c5088829e499cc72a6d647128f7587c2d1f700ebf0558 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793201400.0.stream.jsonl.gz 10684034 99341832a61bf589521a253a863d94db68526d8a53114d0a855917b354e8a896 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793202300.0.stream.jsonl.gz 10156189 ec78fb31112d645c9c08ded59c6befd6277bdfb7e260723c9340467f5b3fcea7 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793203200.0.stream.jsonl.gz 10279670 5c10b99de3ca84f6d0cd4fd556fa530483c301e1bf3c7bb80114eef519ebd1bc removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793204100.0.stream.jsonl.gz 9536875 ffbc1876095b1ca7ca17b218892d8b42c3bb918183eca7b7827d7de25ec768f5 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793205000.0.stream.jsonl.gz 10141202 b38c8fd1d01f0fa20fe38b26a94255344e296c83b509640bee279dcad5deff16 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793205900.0.stream.jsonl.gz 9715061 0afde34b6cf80083b9cdda7bef5baacfa1dc946f61e68886265cb3633f3a3538 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793206800.0.stream.jsonl.gz 11001064 e9f2f8a8ff6cef04b36b04cbffaaed9b5accf26873d26eed74b85d8dc6199378 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793207700.0.stream.jsonl.gz 9835502 6eec69739f70d0ac95fa8735d2154567794477b47cc5d9d43f2bfac27bedcc99 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793208600.0.stream.jsonl.gz 9874421 1084bd093c165ef45f8cbce038465b4a5fcb395d435ef7556d05d85f08169ce5 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793209500.0.stream.jsonl.gz 9385489 09177e12607a802d3aac38cdf988ec17229af4238b4a87a55224d75117561d73 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793210400.0.stream.jsonl.gz 10966063 b10381fa9dc7552d8d16e2b480baeb4f6ff30651921c3b89323a0659d8955d58 removed at second 268
[2026-10-29T09:04:28Z] X 1793145600-1793211300.0.stream.jsonl.gz 10551024 fd8659f6bf0eaba31206970e69ba9f5b0a915c804e73a0dba9815a35dbb90bd7 removed at second 268
[2026-10-29T09:04:29Z] X 1793145600-1793212200.0.stream.jsonl.gz 12372196 a4e4aa901676ac2ad3585b6cbc7edc0349ed0fffa7e41a744ab602c954738485 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793213100.0.stream.jsonl.gz 11112191 17b2340abe0d5466dc70c8584c970feb094a07f2ca5d534aae2d4459520efd65 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793214000.0.stream.jsonl.gz 10918172 9e3d0b9f03b4cbd00834375385767f370ee4a479fd0c1ca54c40052213cce5a5 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793214900.0.stream.jsonl.gz 10956690 d70fe0f958eb08281fb8c3cf74567121bafeffadc272afebb3b973938eedeba9 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793215800.0.stream.jsonl.gz 10464479 7f48547a7aa076d1133ab3ffc013aa90a2f0f464eefd55f474c6de7482af44b0 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793216700.0.stream.jsonl.gz 11797234 87f3efd83e33c5ffe9e9b035a4c5b090b645462a68b0f96645818f91f2997faf removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793217600.0.stream.jsonl.gz 9947721 1ca2fac80bb178ad476eb69bcf3a26f90fc6c25af5715df82672dd8de84107c0 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793218500.0.stream.jsonl.gz 9342830 70c9bd544e19d236188538cc43cd89663cd327d6bd516ef442e01ff89f59508a removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793219400.0.stream.jsonl.gz 8879554 07b12705033d39a7a84982ea7e311d31522b0e4ab09580a5868c83f17c054186 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793220300.0.stream.jsonl.gz 9062207 0154c6a783d139f1532ec09d9060da71cfd1254552aacfb75ed385f7799d4006 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793221200.0.stream.jsonl.gz 9372847 57bf808b26b559fdf9f211e59a761fac1f9b8c2dfda86bc3723f984eb5914a08 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793222100.0.stream.jsonl.gz 8001926 18c0bdb9008b4b40471b5b99a4ddc854c5e6b1f39d9659f479b252a69a8884be removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793223000.0.stream.jsonl.gz 8114414 f6101c8eb420b9eda97f353d7adcebdc355fbec4bb93ff6a69b6cab57adcaed6 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793223900.0.stream.jsonl.gz 9006052 86ef7ae2e14ac60b9b57edc530427e2fb33d0a481aa315799106c43e59c0e0e0 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793224800.0.stream.jsonl.gz 8661025 752e54df1a8237873fa10a40e759b042763c89cb5b87d745b89949d3f20b2e0e removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793225700.0.stream.jsonl.gz 8132267 9485eb5864c99e37e00d178bd4312b6ef4dc779694a5e4de480941b41bb88297 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793226600.0.stream.jsonl.gz 9326449 2cdeb8ca3f85fca93e521e3a2151e6d95c5a24d19c61d58e87cec47b18696819 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793227500.0.stream.jsonl.gz 9815975 ec2d3c0868e6d21c3754d1c290895c080a46c58048103ecb37ede7d4b8edfc3e removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793228400.0.stream.jsonl.gz 9231800 fef35a594b2704d0984f9bc737782ea2bc46b5f264d0712d9df2c10ffa97924b removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793229300.0.stream.jsonl.gz 8160699 7ef7d872fc56eeeb309f156a13f8ae10ed68aeeb1b545a566ca7f3a4e4e5e994 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793230200.0.stream.jsonl.gz 8889088 c2b14f9702d26b6853601d83b685113b6f5650d2b86c644724e87d1f619eec17 removed at second 269
[2026-10-29T09:04:29Z] X 1793145600-1793231100.0.stream.jsonl.gz 9143917 e177b5e38f162522be08df4692d8789e36a8a8a83ee5cf9856940a05dbaf955a removed at second 269
[2026-10-29T09:04:29Z] X 1793232000-1793232000.0.stream.jsonl.gz 11579610 bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f removed at second 269
[2026-10-29T09:04:29Z] X 1793232000-1793232900.0.stream.jsonl.gz 10715152 46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370 removed at second 269
[2026-10-29T09:04:29Z] X 1793232000-1793233800.0.stream.jsonl.gz 11443056 2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9 removed at second 269
[2026-10-29T09:04:29Z] X 1793232000-1793234700.0.stream.jsonl.gz 13592154 ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496 removed at second 269
[2026-10-29T09:04:29Z] X 1793232000-1793235600.0.stream.jsonl.gz 11481990 13cfa07ef0b2a4b17c6dfd8a73acb7124fcaaab9efcc0630e3b35075c6a68806 removed at second 269
[2026-10-29T09:04:29Z] X 1793232000-1793236500.0.stream.jsonl.gz 11586307 4b674d438d19c52d763fcd8a3dafd852a7d509db0dce8aea6cb31b7723e193a1 removed at second 269
[2026-10-29T09:04:29Z] X 1793232000-1793237400.0.stream.jsonl.gz 10660664 a165ef62af692053180e8b84920e9b63dbdda4f2599c4e62531e5f6ca379f125 removed at second 269
[2026-10-29T09:04:29Z] X 1793232000-1793238300.0.stream.jsonl.gz 10776660 b412acf84336b17ffd7722035c2ea162dd1d40cf0199e27e74e97ea939f77f6f removed at second 269
[2026-10-29T09:04:29Z] X 1793232000-1793239200.0.stream.jsonl.gz 10626770 10a349f090734e3edfa6b57293ab0792e3be068f003fd282cd21d016f1191329 removed at second 269
[2026-10-29T09:04:29Z] X 1793232000-1793240100.0.stream.jsonl.gz 9792424 9af6e8ce44bfb351dec406b7238800bcfd9e1c923eda19108ee90f932d1ccd77 removed at second 269
[2026-10-29T09:04:30Z] X 1793232000-1793241000.0.stream.jsonl.gz 10745728 97af9463ab66cb91cb988edb643ed299242b31b1a178a127a329bc519553656c removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793241900.0.stream.jsonl.gz 11272730 56523b9b4864aa1d68356887683b08e62cc114356a412b912d0a48f1cb71cce9 removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793242800.0.stream.jsonl.gz 9774209 0ea58656eab189fc7fe4c12f19565ae1f8e78a16914e4556077ee7357dd66bf8 removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793243700.0.stream.jsonl.gz 9321701 351bc4fb1ecaddc7a7d7706b8c0bdf9dae2c923bff1587739c0b25b84dc27dce removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793244600.0.stream.jsonl.gz 10295145 4c5ea876926595b876b57674ed22ac762dee89bd562b31b41ca1b46c8d8f0941 removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793245500.0.stream.jsonl.gz 10434441 965536189680879129c4b791b2ce4e3f2d6f7b4afc652e3667f4f26badfffe5c removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793246400.0.stream.jsonl.gz 11156773 aa32bc8025e820129068a744811070c5d22a99fbee05f075c224ebdd6acdbee0 removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793247300.0.stream.jsonl.gz 11456592 01702655f10a63f295b19dfeb9d0ba9b88c3c9ce31d44a9a8f2c08fe62cd00dd removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793248200.0.stream.jsonl.gz 11804877 2aae850163314c07ec63ef9432003a577595c5d8d9e14fe6477a3dd22aa6b1ac removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793249100.0.stream.jsonl.gz 11704215 7956e72362c84c21af181ca4735693b0a46f140ffd8bb873cac388937b2d990f removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793250000.0.stream.jsonl.gz 9914992 c7a1c8ac59d83e2c523000877d723b086dcea022249cc5ac8473b01e29328402 removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793250900.0.stream.jsonl.gz 10553162 2881a9c50f4ed4779dd38d087a5bdf08c0a0b615388d99903d3f521f41eff5d8 removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793251800.0.stream.jsonl.gz 6547939 665482155d2c89d4d90d723481ade034d3fa140f3fecb1c9f763955265058b0e removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793252700.0.stream.jsonl.gz 6710655 1ae001465bda15ecb0baac234006e6a6caeb300d3b4af38e03836ad74911d9b6 removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793253600.0.stream.jsonl.gz 10468900 abacdc803e50c358dcbb303c389571da57f2ee9f9d53e15b2d55c97ad40f3c3f removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793254500.0.stream.jsonl.gz 11330444 ecbbccb1a14d1930a4896d80cdaf1ab6d2b7fd1acfe89d44890f217520eaff7b removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793255400.0.stream.jsonl.gz 10581288 e4639bf5a1fa0c5cf5e34da606963fe376f9c1c151c944c01ca5456a8b6cc496 removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793256300.0.stream.jsonl.gz 9852787 86979d6d01fbf239cbc6e10601b10b55cff7ef99c19ed624b395f459fce20c96 removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793257200.0.stream.jsonl.gz 12148871 ab604e14fa82be607598b858b7cd069d9c79fc1ecbbb38c80b0b104556062abd removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793258100.0.stream.jsonl.gz 13568827 ff1db96bb157f72ab0c6d2a33fc8b950d9cda13c2cdbc95cd748b4175652bfe4 removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793259000.0.stream.jsonl.gz 11991341 6897e0b6bb2b55df7d152556adf5134ea8e5365034dcc15ddbca00bcef9f701b removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793259900.0.stream.jsonl.gz 12726821 0d22a5647d7636d7caa05eec6d0fb692b5d68cff96459799bfa2acb8579644e3 removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793260800.0.stream.jsonl.gz 14804505 b839cd4c19f7851e7493c2cabe48e8c40b8bf08a97fc1a3363c52d92c176efdf removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793261700.0.stream.jsonl.gz 12815998 8f724133bc113ff6d30bc03d266711ca940aa0ccb4f244674566f14623556a08 removed at second 270
[2026-10-29T09:04:30Z] X 1793232000-1793262600.0.stream.jsonl.gz 14933789 9c3aa5375f8405416226c860be5b8af5904b3a786c390271296e034260e5af25 removed at second 270
[2026-10-29T09:04:30Z] G-DELETE every file of the set absent         True
[2026-10-29T09:04:30Z] G-DELETE each removal recorded                True
[2026-10-29T09:04:30Z] G-DELETE each slot keeps its slot.json        True
[2026-10-29T09:04:30Z] L {"already": 0, "event": "delete", "free_after": 11195334656, "free_before": 10304053248, "freed": 890975956, "gone": 86, "quiet_s": 0, "removed": 86, "run": 1793263627, "slots_kept": 85, "wall_ns": 1793264670943221111}
[2026-10-29T09:04:30Z] at the set's rate the cap stops the streams in 3.96 days, at 2026-11-02T08:04:27Z
[2026-10-29T09:04:30Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 3.71 days, at 2026-11-02T02:07:47Z
[2026-10-29T09:04:30Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 3.26 days, at 2026-11-01T15:22:14Z
[2026-10-29T09:04:30Z] L {"assets_n": 86, "bytes_total": 890975956, "ended_outside": 0, "event": "complete", "free_bytes": 11195334656, "held_s": 0, "peak_rss": 39477248, "rate_per_day": 1006278726, "removals": 86, "requests": 180, "rewardbook_at_end": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "rewardbook_at_start": {"ActiveState": "active", "MainPID": "3137952", "NRestarts": "1"}, "run": 1793263627, "started_outside": 0, "stops": [["the cap", 1793606667], ["the floor, base 43500000 bytes a day", 1793585267], ["the floor, base 187760570 bytes a day", 1793546534]], "store_stream_bytes": 16842458, "wall_ns": 1793264670967510113}
[2026-10-29T09:04:30Z] COMPLETE: run 1793263627, 86 files, 890975956 bytes, Release rewardbook-streams-1793263627
[2026-10-29T09:04:30Z] peak memory of this run: 39477248 bytes
[2026-10-29T09:04:30Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 87; requests 90, uploads 0, downloads 86 (890975956 bytes); files removed 86
ed02a1307c0e323db4f91dc09ceeaaf7909966ae636074a73f25ed3913582a64  /var/lib/btc-rewardbook-archive/archive.log
fa21d421d8f775db27128d17221b878ebb788eabb9ad18788c37078c4150bcc5  /var/lib/btc-rewardbook-archive/ledger.jsonl
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/btc-rewardbook-archive/run.lock
f3450db0742d155b3e5487cdbde9d0bdf3877661c4c12fc962dcccd7981e7f3e  /var/lib/btc-rewardbook-archive/runs/1793263627/set.json
31ea06e63582413a9f659c9a85ac0ba3edb610b68ef9fb9aebdc789c5ff927ee  /var/lib/btc-rewardbook-archive/runs/1793263627/transfers.jsonl
9bd4defb5d8abd7ba87c2af5bedc185db5581c44df53ec03133ef0975306bee4  /var/lib/btc-rewardbook-archive/runs/1793263627/upload.jsonl
1ce543da50bd61afcf5c927ac563b2150bdb9204a07c3df35f959d8faf158503  /var/lib/btc-rewardbook-archive/runs/1793263627/delete.jsonl
dad6b5783342c244dcc7fb8d5540b8c6176c809c4a1dd9204a3cc2eb6c6c4379  /var/lib/btc-rewardbook-archive/runs/1793263627/verify.json
[2026-10-29T04:45:10Z] slot 1793248200 (2026-10-29T04:30:00Z) index 0: 150 markets; stream opened, 98357 frames, 1 segments, 11804877 bytes; polls 450 served of 450, 429 with a row, 0 missed
[2026-10-29T05:00:09Z] slot 1793249100 (2026-10-29T04:45:00Z) index 0: 150 markets; stream opened, 94756 frames, 1 segments, 11704215 bytes; polls 450 served of 450, 427 with a row, 0 missed
[2026-10-29T05:15:09Z] slot 1793250000 (2026-10-29T05:00:00Z) index 0: 150 markets; stream opened, 80840 frames, 1 segments, 9914992 bytes; polls 450 served of 450, 426 with a row, 0 missed
[2026-10-29T05:30:10Z] slot 1793250900 (2026-10-29T05:15:00Z) index 0: 150 markets; stream opened, 90589 frames, 1 segments, 10553162 bytes; polls 449 served of 450, 428 with a row, 0 missed
[2026-10-29T05:45:10Z] slot 1793251800 (2026-10-29T05:30:00Z) index 0: 150 markets; stream opened, 53756 frames, 1 segments, 6547939 bytes; polls 450 served of 450, 429 with a row, 0 missed
[2026-10-29T06:00:10Z] slot 1793252700 (2026-10-29T05:45:00Z) index 0: 150 markets; stream opened, 56190 frames, 1 segments, 6710655 bytes; polls 450 served of 450, 432 with a row, 0 missed
[2026-10-29T06:15:10Z] slot 1793253600 (2026-10-29T06:00:00Z) index 0: 150 markets; stream opened, 87136 frames, 1 segments, 10468900 bytes; polls 450 served of 450, 432 with a row, 0 missed
[2026-10-29T06:30:10Z] slot 1793254500 (2026-10-29T06:15:00Z) index 0: 150 markets; stream opened, 94141 frames, 1 segments, 11330444 bytes; polls 450 served of 450, 432 with a row, 0 missed
[2026-10-29T06:45:09Z] slot 1793255400 (2026-10-29T06:30:00Z) index 0: 150 markets; stream opened, 88530 frames, 1 segments, 10581288 bytes; polls 450 served of 450, 431 with a row, 0 missed
[2026-10-29T07:00:10Z] slot 1793256300 (2026-10-29T06:45:00Z) index 0: 150 markets; stream opened, 81977 frames, 1 segments, 9852787 bytes; polls 450 served of 450, 428 with a row, 0 missed
[2026-10-29T07:15:09Z] slot 1793257200 (2026-10-29T07:00:00Z) index 0: 150 markets; stream opened, 100166 frames, 1 segments, 12148871 bytes; polls 450 served of 450, 426 with a row, 0 missed
[2026-10-29T07:30:10Z] slot 1793258100 (2026-10-29T07:15:00Z) index 0: 150 markets; stream opened, 114680 frames, 1 segments, 13568827 bytes; polls 450 served of 450, 426 with a row, 0 missed
[2026-10-29T07:45:10Z] slot 1793259000 (2026-10-29T07:30:00Z) index 0: 150 markets; stream opened, 99036 frames, 1 segments, 11991341 bytes; polls 450 served of 450, 428 with a row, 0 missed
[2026-10-29T08:00:10Z] slot 1793259900 (2026-10-29T07:45:00Z) index 0: 150 markets; stream opened, 106075 frames, 1 segments, 12726821 bytes; polls 450 served of 450, 427 with a row, 0 missed
[2026-10-29T08:15:10Z] slot 1793260800 (2026-10-29T08:00:00Z) index 0: 150 markets; stream opened, 127793 frames, 1 segments, 14804505 bytes; polls 450 served of 450, 432 with a row, 0 missed
[2026-10-29T08:30:10Z] slot 1793261700 (2026-10-29T08:15:00Z) index 0: 150 markets; stream opened, 106157 frames, 1 segments, 12815998 bytes; polls 450 served of 450, 430 with a row, 0 missed
[2026-10-29T08:45:10Z] slot 1793262600 (2026-10-29T08:30:00Z) index 0: 150 markets; stream opened, 130336 frames, 1 segments, 14933789 bytes; polls 450 served of 450, 427 with a row, 0 missed
[2026-10-29T09:00:10Z] slot 1793263500 (2026-10-29T08:45:00Z) index 0: 150 markets; stream opened, 105795 frames, 1 segments, 12813807 bytes; polls 450 served of 450, 428 with a row, 0 missed
[2026-10-29T09:15:10Z] slot 1793264400 (2026-10-29T09:00:00Z) index 0: 150 markets; stream opened, 100264 frames, 1 segments, 12248012 bytes; polls 450 served of 450, 426 with a row, 0 missed
[2026-10-29T09:30:10Z] slot 1793265300 (2026-10-29T09:15:00Z) index 0: 150 markets; stream opened, 93267 frames, 1 segments, 11311657 bytes; polls 450 served of 450, 426 with a row, 0 missed
               total        used        free      shared  buff/cache   available
Mem:      1002127360   568406016    96030720       32768   523493376   433721344
Swap:     3250581504   557432832  2693148672
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11126394880
10463932	/root/tz34-work
54736039	/var/lib/btc-rewardbook
291318	/var/lib/btc-rewardbook-archive
588648341	/var/lib/btc-pairbook
117941762	/root/.claude
{
 "marks34": {
  "enable": {
   "ns": 1793261715765408186,
   "service": {
    "ActiveState": "inactive",
    "Result": "success"
   },
   "timer": {
    "ActiveState": "inactive",
    "UnitFileState": "disabled"
   }
  },
  "retry": {
   "ns": 1793264461750230508,
   "service": {
    "ActiveState": "failed",
    "Result": "exit-code"
   },
   "timer": {
    "ActiveState": "active",
    "UnitFileState": "enabled"
   }
  }
 },
 "still34": {
  "at": "2026-10-29T07:46:51Z",
  "at_ns": 1793260011848935087,
  "units": {
   "pairbook": {
    "ActiveState": "active",
    "MainPID": "3216422",
    "NRestarts": "12"
   },
   "recorder": {
    "ActiveState": "active",
    "MainPID": "2388318",
    "NRestarts": "0"
   },
   "rewardbook": {
    "ActiveState": "active",
    "MainPID": "3137952",
    "NRestarts": "1"
   }
  }
 }
}
```

Contract §4.2's three lines and V12's fourth, after a `git fetch`:

```
2026-10-29T09:32:48.329678494Z
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new tag]         pairbook-streams-1793260762 -> pairbook-streams-1793260762
 * [new tag]         rewardbook-streams-1793263627 -> rewardbook-streams-1793263627
fetch exit=0
0968707446d0bc549137b152d37be972e9f6781c
6a615257277d3c94dafd4d39783499560a344648
$ git rev-list origin/main | grep -c 6a615257277d3c94dafd4d39783499560a344648
0
$ git diff --name-only origin/main origin/tz-34-rewardbook-archive-timer
deploy/systemd/btc-rewardbook-archive.service
deploy/systemd/btc-rewardbook-archive.timer
research/tz34-rewardbook-archive-timer.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
grep exit=1
$ git ls-tree -r --name-only origin/main | grep -c -e '\.gz$' -e '\.jsonl$'
0
$ git diff --name-status origin/main origin/tz-34-rewardbook-archive-timer
A	deploy/systemd/btc-rewardbook-archive.service
A	deploy/systemd/btc-rewardbook-archive.timer
A	research/tz34-rewardbook-archive-timer.py
```

**V12: the first line `0`; the diff names the three paths alone, each `A`; nothing `.parquet` or `.zip`; the further line `0`.** The refs, read again at 09:33 UTC (§6) — **84 lines**: §0.5's 79, the branch, PR #34's head and merge refs, `pairbook-streams-1793260762` and `rewardbook-streams-1793263627`, with no peeled line, lightweight, at `6a61525…`:

```
2026-10-29T09:32:58.001259007Z
0968707446d0bc549137b152d37be972e9f6781c	HEAD
0968707446d0bc549137b152d37be972e9f6781c	refs/heads/main
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
7144100bc96c2c7b6c5c950674753f085b149c41	refs/pull/34/merge
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
exit=0
```

### 2.14 Every file the run and the session wrote, by SHA-256, but a Release's assets

The session's, under `/root/tz34-work` but the branch worktree, and B-INSTALL's six, read at assembly:

| path | bytes | SHA-256 |
|---|---|---|
| `/root/tz34-work/build-report.py` | 3,902 | `f33217a574efb94a969c70bd6a80c306c22bb91bde3b2e2c66a85cb9966beb84` |
| `/root/tz34-work/logs/00-mkdir.log` | 97 | `d6d91203b630106d8d8eee835b5546110369dd4a71972c325b7f45ddce05d14a` |
| `/root/tz34-work/logs/00-startup.log` | 462 | `05ab1f81db000f9086c3413525577ad6f761f6be3726912213acfb4032d72f37` |
| `/root/tz34-work/logs/01-stage.log` | 713 | `ccd1d7b1301faa6f89b99b040eb7c76c43e181018d861263a080eb39968c0683` |
| `/root/tz34-work/logs/02-fingerprint.log` | 8,901 | `84c3731a4d25998b81bae886ea19f5665f8c4a1c6a93dba59cf6d7b011a99d63` |
| `/root/tz34-work/logs/03-host-gate.log` | 4,824 | `6dd303718c46576b12cb3ac59cc72ce86f70128f1de577efebfdaba962c03156` |
| `/root/tz34-work/logs/05-refs-commits.log` | 1,494 | `b99f6cf70f24b97e907a34701dc33c0a652c41a9edbdb1d3e2ef7c338009add8` |
| `/root/tz34-work/logs/05-refs.log` | 5,496 | `a3bb7aa27ffa7df21e113ded1866661c83100d732e32adb7ee0a5e1d9a551471` |
| `/root/tz34-work/logs/06-model.log` | 255 | `730d3b44472604e4b3685c7db09a03b03ebe98ffb52e5a6b72371c173073d911` |
| `/root/tz34-work/logs/10-branch.log` | 399 | `9c073dfbdcec8c4071ce9366f8ecbbcf4cada30944407a881c28100f27005d11` |
| `/root/tz34-work/logs/11-branch-files.log` | 588 | `da6555567e4e17074f0d95b4184ce9cf90f91c09aa1932d0f80572b2438859e6` |
| `/root/tz34-work/logs/12-commit.log` | 496 | `10e44c63a3c67bfe14f569c012b5a641a41cd710dfc5d8bd1bd46e687b8f76b4` |
| `/root/tz34-work/logs/13-push.log` | 501 | `bdf340cff1ecf3bd82ee894e2e2410fb6913998813f9e26f70854b3814b658c7` |
| `/root/tz34-work/logs/14-pr.log` | 94 | `4709f84ce76e3321a5f4dcaa2a90de38aaba258288e49ce6f5576a6614650124` |
| `/root/tz34-work/logs/20-selftest.log` | 82,254 | `d1559a4a399f5f0ebf7d8d24d5f79f34862af4b84671c1dc56f1acaf3e0897bc` |
| `/root/tz34-work/logs/30-still.log` | 1,342 | `186473f5e0731c9e816423bd5626aac4548e975fbddffadc9ac61771bc8a46ef` |
| `/root/tz34-work/logs/31-scratch-procs.log` | 599 | `b6b5a669a036c89f2314dde804048090fea50d4252881bfcbe1686937ca828ad` |
| `/root/tz34-work/logs/31-scratch.log` | 930 | `be4125953d38fe7eea4d7d803e8368f3e38e253d7f9f9c09d3dbaa1016bb6592` |
| `/root/tz34-work/logs/32-reclaim-scratch.log` | 491 | `bfccd1b6a7de8d85541a2247447f54a1d7edd5b5656e0072547b472aa2dd6e55` |
| `/root/tz34-work/logs/33-rm-scratch.log` | 135 | `f770acbd1e781170985b86f7af93166d5eb95313fc740660bb17149e9080fbd8` |
| `/root/tz34-work/logs/40-path.log` | 1,338 | `45bec4675e0edb9d100dce2b4f56f08d091fe658ba627d922b1d386aa4a962cf` |
| `/root/tz34-work/logs/50-B-INSTALL.log` | 111 | `a81e5ce454c56a9fc51c975a7be83a12267d4e2dcce21b9be07edb2fee860d28` |
| `/root/tz34-work/logs/51-installed.log` | 2,232 | `cdeb8c723451e7ccad90afc9383b54042f2c9ddf5f5d01d7519f759cc602c48f` |
| `/root/tz34-work/logs/52-mark-enable.log` | 467 | `70f2d37f421d8b3ae949b10f86fb12a60b8d53ee1e4ec6b5eb120706b54f03bc` |
| `/root/tz34-work/logs/52a-pairarchive-deferred.log` | 1,320 | `baf1155dff9414480ec090d3d66b1d1a34386ac88e7660bf500ed26928ae8f5c` |
| `/root/tz34-work/logs/53-timer.log` | 1,524 | `eee0875661ad86c650a5bc198e2f40b50dd1a413f08b8165cc1a5d1795f0b2b1` |
| `/root/tz34-work/logs/60-first-watch.log` | 25 | `14086e48d31f546ac2846cfe12decd7a03169c080e9c621ef88f7015eb8a7cb1` |
| `/root/tz34-work/logs/60-first.log` | 2,616 | `b0b7504c0fcc37ce0a3066016b75881174218e29688ab037f1bc8ecadf5d268e` |
| `/root/tz34-work/logs/61-path-diagnostic.log` | 661 | `4d0dcb7702a01c5c6c45a04b5ab36e925df7dd561fabe4f070b7389305c05e8c` |
| `/root/tz34-work/logs/62-after-deferral.log` | 732 | `505ac04751bfff95dc0a4216eed8877ff652139b4b336e894ad512d978689571` |
| `/root/tz34-work/logs/63-path-recheck.log` | 1,334 | `29b2d9c6dab6b35b948715197965d3a19ce676eb85ac258ef0063396fbf8492a` |
| `/root/tz34-work/logs/64-mark-retry.log` | 463 | `49ea6318d95153db3379f578b3ce145c56c3a8d5b4c74131608f5f53bb224245` |
| `/root/tz34-work/logs/65-B-RETRY.log` | 38 | `31be06e3688e0c7dd778845acb632540ec24d724508009faf9896cdcbcf1fc11` |
| `/root/tz34-work/logs/66-first-after-retry.log` | 97,897 | `728c6f6850786c73709c56a2ff862b6ad843093ab0e25a539a235212e24c3800` |
| `/root/tz34-work/logs/66-first-watch.log` | 25 | `557b4bd5f1adba25b7f2ab5893893999b567230062ca2672f2bbaa6b8516b875` |
| `/root/tz34-work/logs/67-first-deciding.log` | 95,718 | `69bd81d11fb0852377ebac8f8dcfa816f1aec15061c61b0f3dd6b0709cfeaeee` |
| `/root/tz34-work/logs/70-final.log` | 2,620 | `bbc54d3b3f9489091d06a938ae88decb3f6eb471c9967a1a85f2d20e13db83ee` |
| `/root/tz34-work/logs/80-closing-reads.log` | 33,775 | `296cb746da07b648050ff0c86ae0a4c7eb37782e88defee8f068df6d336f29bf` |
| `/root/tz34-work/logs/81-selfcheck.log` | 1,000 | `292db4b1acd99bfe410b31203b1a8dbbb51556353f3e5b0d855d15916201e063` |
| `/root/tz34-work/logs/82-refs-end.log` | 5,858 | `b6e6ae561bebff256f5797240c26aa04c005db7e049edc7267f32839a98b5205` |
| `/root/tz34-work/logs/B-ENABLE.log` | 847 | `d6806631c4c53b51ae2433d7adc7b0f38d768808c7d16424df864d5696cc5a3c` |
| `/root/tz34-work/report.tmpl.md` | 34,399 | `5fe5ec58a9204f00b4045ef7f743e7e0fc01a15576c683bc060f00bfdbe711d2` |
| `/root/tz34-work/stage/deploy/systemd/btc-rewardbook-archive.service` | 810 | `a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f` |
| `/root/tz34-work/stage/deploy/systemd/btc-rewardbook-archive.timer` | 428 | `bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f` |
| `/root/tz34-work/stage/research/tz27-pairbook-archive.py` | 106,284 | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` |
| `/root/tz34-work/stage/research/tz28-pairbook-archive-timer.py` | 74,576 | `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4` |
| `/root/tz34-work/stage/research/tz34-rewardbook-archive-timer.py` | 99,388 | `1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72` |
| `/root/tz34-work/state.json` | 830 | `8aeb173312847b9efc66899c13b74a07a3aa5a7927c6d77f0d589bd37f2b74bf` |
| `/root/tz34-work/watch-first.sh` | 1,114 | `7c15f564de64f8fa55f6e53bda753d5edff49e777034192da3b4af5509017172` |
| `/root/tz34-work/watch-timer.sh` | 802 | `7802c5b8e6beddf68d8ee4e5149e357767209653ec44d6a725771ed71d88cd78` |
| `/root/btc-rewardbook-archive-svc/tz34-rewardbook-archive-timer.py` | 99,388 | `1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72` |
| `/root/btc-rewardbook-archive-svc/tz28-pairbook-archive-timer.py` | 74,576 | `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4` |
| `/root/btc-rewardbook-archive-svc/tz27-pairbook-archive.py` | 106,284 | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` |
| `/root/btc-rewardbook-archive-svc/commit.txt` | 41 | `37b91e776d8870494da3f660ec1f29e694acae1100406a5b0df9082354e70bbe` |
| `/etc/systemd/system/btc-rewardbook-archive.service` | 810 | `a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f` |
| `/etc/systemd/system/btc-rewardbook-archive.timer` | 428 | `bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f` |

The unit's, under `/var/lib/btc-rewardbook-archive/`, as §3.9's `find … -exec sha256sum` printed them: `archive.log` `ed02a1307c0e323db4f91dc09ceeaaf7909966ae636074a73f25ed3913582a64`, `ledger.jsonl` `fa21d421d8f775db27128d17221b878ebb788eabb9ad18788c37078c4150bcc5`, `run.lock` `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, `runs/1793263627/set.json` `f3450db0742d155b3e5487cdbde9d0bdf3877661c4c12fc962dcccd7981e7f3e`, `transfers.jsonl` `31ea06e63582413a9f659c9a85ac0ba3edb610b68ef9fb9aebdc789c5ff927ee`, `upload.jsonl` `9bd4defb5d8abd7ba87c2af5bedc185db5581c44df53ec03133ef0975306bee4`, `delete.jsonl` `1ce543da50bd61afcf5c927ac563b2150bdb9204a07c3df35f959d8faf158503`, `verify.json` `dad6b5783342c244dcc7fb8d5540b8c6176c809c4a1dd9204a3cc2eb6c6c4379`. They stay: the archive's state, not scratch (§9). The branch's three files are §0's, and `/root/btc-5m-twap/.git` holds the branch and the worktree's metadata.

### 2.15 §9 B-RECLAIM-OWN — last, after §3.9, with this report drafted (V14, V15)

Run by the Executor in four calls, each with a `date -u` line added before it (§6); none refused by the classifier; the output quoted from the session, unfiltered, written to no file.

```
$ cd /root/tz34-work && date -u +%FT%T.%NZ && I reclaim /root/tz34-work; echo "exit=$?"
2026-10-29T09:38:27.525062614Z
[2026-10-29T09:38:27Z] reclaim: 3399 report tokens; forensic store holds 2101 files
[2026-10-29T09:38:27Z] reclaim: /root/tz34-work/wt skipped: no file but its HEAD's, and HEAD 6a615257277d3c94dafd4d39783499560a344648 is its upstream's
[2026-10-29T09:38:27Z] R copied f33217a574efb94a969c70bd6a80c306c22bb91bde3b2e2c66a85cb9966beb84 /root/btc-forensics/tz34-work--build-report.py
[2026-10-29T09:38:27Z] R copied 5fe5ec58a9204f00b4045ef7f743e7e0fc01a15576c683bc060f00bfdbe711d2 /root/btc-forensics/tz34-work--report.tmpl.md
[2026-10-29T09:38:27Z] R copied 8aeb173312847b9efc66899c13b74a07a3aa5a7927c6d77f0d589bd37f2b74bf /root/btc-forensics/tz34-work--state.json
[2026-10-29T09:38:27Z] R copied 7c15f564de64f8fa55f6e53bda753d5edff49e777034192da3b4af5509017172 /root/btc-forensics/tz34-work--watch-first.sh
[2026-10-29T09:38:27Z] R copied 7802c5b8e6beddf68d8ee4e5149e357767209653ec44d6a725771ed71d88cd78 /root/btc-forensics/tz34-work--watch-timer.sh
[2026-10-29T09:38:27Z] R copied d6d91203b630106d8d8eee835b5546110369dd4a71972c325b7f45ddce05d14a /root/btc-forensics/tz34-work--logs--00-mkdir.log
[2026-10-29T09:38:27Z] R copied 05ab1f81db000f9086c3413525577ad6f761f6be3726912213acfb4032d72f37 /root/btc-forensics/tz34-work--logs--00-startup.log
[2026-10-29T09:38:27Z] R copied ccd1d7b1301faa6f89b99b040eb7c76c43e181018d861263a080eb39968c0683 /root/btc-forensics/tz34-work--logs--01-stage.log
[2026-10-29T09:38:27Z] R copied 84c3731a4d25998b81bae886ea19f5665f8c4a1c6a93dba59cf6d7b011a99d63 /root/btc-forensics/tz34-work--logs--02-fingerprint.log
[2026-10-29T09:38:27Z] R copied 6dd303718c46576b12cb3ac59cc72ce86f70128f1de577efebfdaba962c03156 /root/btc-forensics/tz34-work--logs--03-host-gate.log
[2026-10-29T09:38:27Z] R copied b99f6cf70f24b97e907a34701dc33c0a652c41a9edbdb1d3e2ef7c338009add8 /root/btc-forensics/tz34-work--logs--05-refs-commits.log
[2026-10-29T09:38:27Z] R copied a3bb7aa27ffa7df21e113ded1866661c83100d732e32adb7ee0a5e1d9a551471 /root/btc-forensics/tz34-work--logs--05-refs.log
[2026-10-29T09:38:27Z] R copied 730d3b44472604e4b3685c7db09a03b03ebe98ffb52e5a6b72371c173073d911 /root/btc-forensics/tz34-work--logs--06-model.log
[2026-10-29T09:38:27Z] R copied 9c073dfbdcec8c4071ce9366f8ecbbcf4cada30944407a881c28100f27005d11 /root/btc-forensics/tz34-work--logs--10-branch.log
[2026-10-29T09:38:27Z] R copied da6555567e4e17074f0d95b4184ce9cf90f91c09aa1932d0f80572b2438859e6 /root/btc-forensics/tz34-work--logs--11-branch-files.log
[2026-10-29T09:38:27Z] R copied 10e44c63a3c67bfe14f569c012b5a641a41cd710dfc5d8bd1bd46e687b8f76b4 /root/btc-forensics/tz34-work--logs--12-commit.log
[2026-10-29T09:38:27Z] R copied bdf340cff1ecf3bd82ee894e2e2410fb6913998813f9e26f70854b3814b658c7 /root/btc-forensics/tz34-work--logs--13-push.log
[2026-10-29T09:38:27Z] R copied 4709f84ce76e3321a5f4dcaa2a90de38aaba258288e49ce6f5576a6614650124 /root/btc-forensics/tz34-work--logs--14-pr.log
[2026-10-29T09:38:27Z] R copied d1559a4a399f5f0ebf7d8d24d5f79f34862af4b84671c1dc56f1acaf3e0897bc /root/btc-forensics/tz34-work--logs--20-selftest.log
[2026-10-29T09:38:27Z] R copied 186473f5e0731c9e816423bd5626aac4548e975fbddffadc9ac61771bc8a46ef /root/btc-forensics/tz34-work--logs--30-still.log
[2026-10-29T09:38:27Z] R copied b6b5a669a036c89f2314dde804048090fea50d4252881bfcbe1686937ca828ad /root/btc-forensics/tz34-work--logs--31-scratch-procs.log
[2026-10-29T09:38:27Z] R copied be4125953d38fe7eea4d7d803e8368f3e38e253d7f9f9c09d3dbaa1016bb6592 /root/btc-forensics/tz34-work--logs--31-scratch.log
[2026-10-29T09:38:27Z] R copied bfccd1b6a7de8d85541a2247447f54a1d7edd5b5656e0072547b472aa2dd6e55 /root/btc-forensics/tz34-work--logs--32-reclaim-scratch.log
[2026-10-29T09:38:27Z] R copied f770acbd1e781170985b86f7af93166d5eb95313fc740660bb17149e9080fbd8 /root/btc-forensics/tz34-work--logs--33-rm-scratch.log
[2026-10-29T09:38:27Z] R copied 45bec4675e0edb9d100dce2b4f56f08d091fe658ba627d922b1d386aa4a962cf /root/btc-forensics/tz34-work--logs--40-path.log
[2026-10-29T09:38:27Z] R copied a81e5ce454c56a9fc51c975a7be83a12267d4e2dcce21b9be07edb2fee860d28 /root/btc-forensics/tz34-work--logs--50-B-INSTALL.log
[2026-10-29T09:38:27Z] R copied cdeb8c723451e7ccad90afc9383b54042f2c9ddf5f5d01d7519f759cc602c48f /root/btc-forensics/tz34-work--logs--51-installed.log
[2026-10-29T09:38:27Z] R copied 70f2d37f421d8b3ae949b10f86fb12a60b8d53ee1e4ec6b5eb120706b54f03bc /root/btc-forensics/tz34-work--logs--52-mark-enable.log
[2026-10-29T09:38:27Z] R copied baf1155dff9414480ec090d3d66b1d1a34386ac88e7660bf500ed26928ae8f5c /root/btc-forensics/tz34-work--logs--52a-pairarchive-deferred.log
[2026-10-29T09:38:27Z] R copied eee0875661ad86c650a5bc198e2f40b50dd1a413f08b8165cc1a5d1795f0b2b1 /root/btc-forensics/tz34-work--logs--53-timer.log
[2026-10-29T09:38:27Z] R copied 14086e48d31f546ac2846cfe12decd7a03169c080e9c621ef88f7015eb8a7cb1 /root/btc-forensics/tz34-work--logs--60-first-watch.log
[2026-10-29T09:38:27Z] R copied b0b7504c0fcc37ce0a3066016b75881174218e29688ab037f1bc8ecadf5d268e /root/btc-forensics/tz34-work--logs--60-first.log
[2026-10-29T09:38:27Z] R copied 4d0dcb7702a01c5c6c45a04b5ab36e925df7dd561fabe4f070b7389305c05e8c /root/btc-forensics/tz34-work--logs--61-path-diagnostic.log
[2026-10-29T09:38:27Z] R copied 505ac04751bfff95dc0a4216eed8877ff652139b4b336e894ad512d978689571 /root/btc-forensics/tz34-work--logs--62-after-deferral.log
[2026-10-29T09:38:27Z] R copied 29b2d9c6dab6b35b948715197965d3a19ce676eb85ac258ef0063396fbf8492a /root/btc-forensics/tz34-work--logs--63-path-recheck.log
[2026-10-29T09:38:27Z] R copied 49ea6318d95153db3379f578b3ce145c56c3a8d5b4c74131608f5f53bb224245 /root/btc-forensics/tz34-work--logs--64-mark-retry.log
[2026-10-29T09:38:27Z] R copied 31be06e3688e0c7dd778845acb632540ec24d724508009faf9896cdcbcf1fc11 /root/btc-forensics/tz34-work--logs--65-B-RETRY.log
[2026-10-29T09:38:27Z] R copied 728c6f6850786c73709c56a2ff862b6ad843093ab0e25a539a235212e24c3800 /root/btc-forensics/tz34-work--logs--66-first-after-retry.log
[2026-10-29T09:38:27Z] R copied 557b4bd5f1adba25b7f2ab5893893999b567230062ca2672f2bbaa6b8516b875 /root/btc-forensics/tz34-work--logs--66-first-watch.log
[2026-10-29T09:38:27Z] R copied 69bd81d11fb0852377ebac8f8dcfa816f1aec15061c61b0f3dd6b0709cfeaeee /root/btc-forensics/tz34-work--logs--67-first-deciding.log
[2026-10-29T09:38:27Z] R copied bbc54d3b3f9489091d06a938ae88decb3f6eb471c9967a1a85f2d20e13db83ee /root/btc-forensics/tz34-work--logs--70-final.log
[2026-10-29T09:38:27Z] R copied 296cb746da07b648050ff0c86ae0a4c7eb37782e88defee8f068df6d336f29bf /root/btc-forensics/tz34-work--logs--80-closing-reads.log
[2026-10-29T09:38:27Z] R copied 292db4b1acd99bfe410b31203b1a8dbbb51556353f3e5b0d855d15916201e063 /root/btc-forensics/tz34-work--logs--81-selfcheck.log
[2026-10-29T09:38:27Z] R copied b6e6ae561bebff256f5797240c26aa04c005db7e049edc7267f32839a98b5205 /root/btc-forensics/tz34-work--logs--82-refs-end.log
[2026-10-29T09:38:27Z] R copied d6806631c4c53b51ae2433d7adc7b0f38d768808c7d16424df864d5696cc5a3c /root/btc-forensics/tz34-work--logs--B-ENABLE.log
[2026-10-29T09:38:27Z] R copied a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f /root/btc-forensics/tz34-work--stage--deploy--systemd--btc-rewardbook-archive.service
[2026-10-29T09:38:27Z] R copied bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f /root/btc-forensics/tz34-work--stage--deploy--systemd--btc-rewardbook-archive.timer
[2026-10-29T09:38:27Z] R copied 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673 /root/btc-forensics/tz34-work--stage--research--tz27-pairbook-archive.py
[2026-10-29T09:38:27Z] R copied 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4 /root/btc-forensics/tz34-work--stage--research--tz28-pairbook-archive-timer.py
[2026-10-29T09:38:27Z] R copied 1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72 /root/btc-forensics/tz34-work--stage--research--tz34-rewardbook-archive-timer.py
[2026-10-29T09:38:27Z] RECLAIM PASS: 50 files considered, 50 named by a report, 0 kept by name, 50 copied, 0 already held; forensic store 2101 -> 2151 files
[2026-10-29T09:38:27Z] peak memory of this run: 38879232 bytes
[2026-10-29T09:38:27Z] opens refused: 0 by TZ-27's hook, 0 by this file's; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
$ date -u +%FT%T.%NZ; git -C /root/btc-5m-twap worktree remove /root/tz34-work/wt; echo "exit=$?"
2026-10-29T09:38:31.958064894Z
exit=0
$ date -u +%FT%T.%NZ; rm -rf /root/tz34-work; echo "exit=$?"
2026-10-29T09:38:37.000854050Z
exit=0
$ date -u +%FT%T.%NZ; test -e /root/tz34-work; echo "exit=$?"; git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list; find /root/btc-forensics -type f | wc -l; df -B1 --output=source,size,avail /var/lib
2026-10-29T09:38:40.597558858Z
exit=1
/root/btc-5m-twap       0968707 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
2151
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11130118144
```

**V14: `RECLAIM PASS`, 50 files considered, 50 named by this report, 0 kept by name — every one also named by its hash — 50 copied, 0 already held; the store 2,101 → 2,151, equal to before plus the copies.** The worktree was not copied: `git status --porcelain --ignored` empty and its `HEAD` its upstream's. **V15: `git worktree remove` without `--force` `exit=0`; `rm -rf` `exit=0`; `test -e /root/tz34-work` `exit=1`; `git worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else.** `I` here is `nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz34-work/wt/research/tz34-rewardbook-archive-timer.py`, as §3 writes it; the branch stays on `origin` and as a local ref, and the tag and Release stay.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-34-rewardbook-archive-timer` at `6a615257277d3c94dafd4d39783499560a344648`, on `origin` and as a local ref |
| pull request | #34, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/34`, open, not merged |
| the first run's Release | id `427629503`, on the lightweight tag `rewardbook-streams-1793263627` at `6a615257…`, 86 assets, `890,975,956` bytes — created and filled by the unit alone, under the credential the unit reads |
| the report | `CryptoReports/TZ-34-rewardbook-archive-timer-report.md`, straight to `main`, one commit |

**Contract §5.1, here the unit's:** the local hash of every asset is the set's, hashed by the run before upload and again before each removal; the downloaded hash is the run's full anonymous download of every asset; **and they are equal at 86 of 86** — §2.9's table, from `first`, which read the Release's record again anonymously from the session. The contract's `curl … | sha256sum` is the run's own download through TZ-27's `download`, with no token. Contract §4.2's self-check, §2.13: `0`; the three paths; nothing.

---

## 4. Gate

| gate | PASS, as §4 fixes it | read | result |
|---|---|---|---|
| P-PATH | `tz-01a-dataset`'s Release through `Gh28`: 2 API requests and 1 download, each inside the idle stretch | 3 of 3, record and download equal | **PASS** |
| P-TOKEN | the credential from the primary checkout's remote URL, `push` true, Release `409534533`: 2 requests | served | **PASS** |
| G-INSTALL | nine checks | 9 of 9 | **PASS** |
| G-TIMER | nine checks, after B-ENABLE and at `final` | 9 of 9, twice | **PASS** |
| G-TRIGGER | the first run after the enable mark, fired by the timer's 1,800 s elapse | `TRIGGER_UNIT` the timer; 1,912 s after the mark | **PASS** |
| G-RUN | the run `complete`, `Result` `success`, `ExecMainStatus` `0` | after one deferral and B-RETRY | **PASS** |
| G-SET | the set this TZ's rule rebuilds, one set record, the store after it | 86 files, 85 slots, 0 left | **PASS** |
| G-UPLOAD | the Release read anonymously, every asset by name, bytes, state and digest; the tag lightweight at the run's commit | 86 of 86 | **PASS** |
| G-DOWNLOAD | `verify.json`, every download equal | 86 of 86 | **PASS** |
| G-DELETE | every file of the set absent, recorded, every `slot.json` kept | 86 / 86 / 85 | **PASS** |
| G-IDLE | every request and every removal inside the idle stretch | 266 of 266 | **PASS** |
| G-NEXT | the slots decided from the first removal to 900 s after the last, none FAIL | 1 of 1 PASS | **PASS** |
| G-STILL | the three capture units, §3.3 to §3.8 | unchanged | **PASS** |

Every gate is exact; there is no fraction to three decimals. Nothing was tuned and no gate reinterpreted.

---

## 5. Validation

| # | check | count | asserted |
|---|---|---|---|
| V1 | §0.2's fingerprint | `FINGERPRINT PASS`: revision `2026-10-28-a`; anchors 6 of 6, 4 re-derived; rows 46: frozen 43 of 43 equal, tracked 2, reported 1 | asserted, by the instrument |
| V2 | §0.3's host gate | H1 to H5, the memory and the disk gate, 7 of 7; the rest printed | read by the Executor against §0.3's literals (§0.3's table) |
| V3 | §0.1's and §3.1's files | 3 of 3 hashes at each, lines and bytes; `46a019d6…` and `2cba96bc…`; the diff names the three paths, each `A` | asserted by §0.1's script; the diff read |
| V4 | the self-test | `49 of 49 checks passed` | asserted |
| V5 | P-PATH | `READING P-PATH: served`, 3 requests inside the idle stretch; `uploaded`, `76818669`, `sha256:229a944f…`, URL true; `200`, `76818669`, SHA-256 equal | asserted |
| V6 | B-INSTALL and G-INSTALL | 7 of 7 `exit=0`; `G-INSTALL PASS: 9 of 9` | the exits read; G-INSTALL asserted |
| V7 | B-ENABLE, P-TOKEN and G-TIMER | second 125 of 15 to 480, second 29,825 of 26,100 to 68,400; `READING P-TOKEN: served`, the primary checkout's remote URL, push true, Release `409534533`, 2 requests; `exit=0`; `G-TIMER PASS`, 9 checks, at §3.6 (1.6 s after `E`) and at `final` | the band by the block's own loop; P-TOKEN and G-TIMER asserted |
| V8 | the first run | `FIRST PASS: 8 of 8`; 9 `R` records; 85 `SLOT` and 86 `S` lines; `ROW` 86 of 86; 180 `T`, 86 `X`, 1 `G-NEXT` and 2 `ACROSS` lines | asserted |
| V9 | B-RETRY | run once: its mark at 09:01:01.750 UTC, `exit=0` at 09:01:12 | the exit read |
| V10 | final | `FINAL PASS`: G-TIMER 9 checks, G-STILL; the projection | asserted |
| V11 | the hooks and the counters | opens refused `0` by either hook at every mode that printed its line — every mode but the diagnostic `path` of 08:53, which stopped at its assert; requests `3` at each served `path`, `2` at `path-token`, `2` at the deciding `first` — 1 + ⌊86/100⌋ + 1, inside `2` to `6`; store opens `0` at every mode but `first`, `4` at the deciding one; files removed `0` at every session mode but `selftest`, `15` | each printed by the instrument; the counts read |
| V12 | contract §4.2's self-check, and the line below | `0`; the three paths; nothing; `0` | read |
| V13 | §3.9's closing reads | every read printed, §2.13 | — |
| V14 | §9's `reclaim` runs | B-RECLAIM-SCRATCH: 4 considered, 0 named, 0 kept, 0 copied, 0 held, 2,101 → 2,101; B-RECLAIM-OWN: §2.15 | asserted by `reclaim` |
| V15 | §9's removals | B-RECLAIM-SCRATCH: 3 `rm -rf` `exit=0`, 3 `test -e` `exit=1`; B-RECLAIM-OWN: §2.15 | read |

---

## 6. What could not be implemented as written

1. **The repository did not serve its Releases without a token from between 07:48:30 and 08:02 UTC to about 09:00 UTC.** §3.4's `path` read `tz-01a-dataset`'s Release anonymously at 07:48:27–30; the diagnostic `path` of 08:53:42 found `no release on tz-01a-dataset`; the re-check of 09:00:51 was served. The Boss stated that the repository had been set to public again; that it had been private, and when, is his account and is not measured here. Two consequences follow, both below. Neither moves a reading: every gate of the first run was read after the repository served anonymously again, by the instrument's own modes.
2. **The first run deferred once** (count 1, in `verify`, at 08:51:11 UTC, nothing removed), and **B-RETRY was used**, at 09:01:12 UTC, nine minutes after `first` read `DEFERRED` at 08:52:05, held while the Executor asked the Boss and he restored the repository's visibility; §3.7 fixes no instant for B-RETRY. Its invocation resumed the same set — 86 assets held, none sent again — verified 86 of 86 and removed 86.
3. **The pair book's archive's run set off by B-INSTALL's reload deferred** — exit `75` at 08:02:57 UTC, its tag `pairbook-streams-1793260762` created — by every sign of the same cause; its reason sits in its own `archive.log`, which §2 item 4 forbids the session to open, so it is not confirmed. The pair book was not restarted. Its set is resumed by its calendar run of 2026-10-30 03:00:20 UTC; under TZ-28's rule a third deferral of that set would halt that archive and disable its timer.
4. **B-ENABLE's `systemctl enable` set off no run of the pair book's archive**, against §3's timeline and map §7 item 115: no run at `E + 600`, `list-timers` reading its next elapse at 2026-10-30 03:00:20 UTC at 08:17:38 and 09:32:14. Recorded; it moves no gate.
5. **Two runs of `path` beyond §3.4's**, at 08:53:42 and 09:00:51 UTC, to find whether B-RETRY could pass and then that it could: anonymous reads of `api.github.com` and one download through `github.com`'s redirect, the class §2 item 9 names as `path`'s, 1 request at the first by its code, which stopped at its assert before its counters printed, and 3 at the second.
6. **Reads no step names**, none under a capture's store but one `du`: `ps` and `/proc/<pid>/cwd` and `fd` of the two older `claude` processes before B-RECLAIM-SCRATCH (`logs/31-scratch-procs.log`); `journalctl -u` of the pair book's archive, `systemctl show`, `/proc/meminfo` and `df` at 08:15:37 (`logs/52a-pairarchive-deferred.log`); `systemctl show`, `list-timers`, `df` and **`du -sb /var/lib/btc-rewardbook` at 08:54:02** (`logs/62-after-deferral.log`), beyond §2 item 5's two `du`s — directory sizes, no content; `list-timers` at 08:17:38; `git ls-remote origin` again at 09:33 (`logs/82-refs-end.log`); and `get_session` for the model.
7. **One copy written to the session's scratchpad**, against §0.0: at 09:31 the deciding `first`'s output, already in `logs/66-first-after-retry.log`, was copied to `<scratchpad>/decide.txt` to be read, then removed with `rm` at 09:31:53, `exit=0`, the directory listed empty. The same lines are `logs/67-first-deciding.log`, cut from `logs/66-first-after-retry.log` for this report.
8. **The timing of B-ENABLE**: the band was open at 07:49:40, second 280, after G-INSTALL; the Executor took the mark at 08:15:15 instead, so that the pair book's archive's run of `L + 600` could end before the enable's own reload, and handed the block over at 08:16:02, second 62. The mark was taken by a background `until` loop of the Executor's, its own command.
9. **Background scripts of the Executor's**, each disclosed and kept by its hash (§2.14): `watch-timer.sh`, which waited for B-ENABLE's `exit=` line and ran `I timer` 1.6 s after `E`, within §3.6's 300 s; and `watch-first.sh`, which ran `I first` every 300 s from `E + 1,800` and again from B-RETRY, appending each run to its log, and would have stopped on G-TRIGGER's `E + 5,400`.
10. **The self-test's peak, 61,313,024 bytes, exceeds the Architect's largest measured, 60,338,176**, by 974,848 bytes; §0.4's floor, twice the latter, held: `MemAvailable` never read below 263,163,904.
11. **Logs written after their command, or by hand**: `logs/00-mkdir.log`, written once the directory it names existed; `logs/06-model.log`, the Executor's note of `get_session`, its first line corrected once for a doubled date. The push's output passed through a `sed` that masks a credential in a URL; it masked nothing.
12. **The branch is based on `0968707`**, `origin/main` at §3.1, one upload above this TZ's — `CryptoTZ/TZ-34-advisor-bot.md`; the diff against `origin/main` names the three paths alone.
13. **The report was assembled by a script from a template** — `build-report.py` and `report.tmpl.md`, with each log quoted verbatim — both kept in the forensic store by their hashes (§2.14). §2.15's block was inserted after B-RECLAIM-OWN ran, by a script in the session: its prose and lines as the session printed them, its 50 `copied` lines rebuilt from the forensic copies in `reclaim`'s order and each asserted equal to §2.14's hash of the same path.
14. Contract §1 step 1 was `git fetch origin main` and a fast-forward merge, which is `git pull` on a clean `main`; before §0.0's `mkdir` the Executor also read its memory notes, listed `/root` and searched the checkout for this TZ — no capture root.
15. **B-RECLAIM-OWN ran in four calls, each with a `date -u` line added before it**; §9's seven lines are otherwise verbatim, and none was refused.
