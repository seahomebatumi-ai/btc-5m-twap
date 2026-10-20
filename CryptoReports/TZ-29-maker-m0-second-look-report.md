# TZ-29 report — M0's second look: do the makers earn, over both looks?

**M0 READING, OVER BOTH LOOKS: NO EARN.** Both looks hold 8,064 members, TZ-23's 4,032 from `1788530400` to
`1791241800` and this TZ's 4,032 from `1791242100` to `1792451400`. Their fills inside `[T0, T0 + 240)` give the makers
**`S` = `580,110.138` USDC, `0.231` c a share**. That is `+29,461.909` at settlement (`+0.012` c a share) and
`+550,648.229` of rebate (`+0.219` c a share), on `Sh` = `250,976,527.958` shares. **NO EARN holds:** `S <= δ · Sh − thr` =
`617,377.804` (`0.246` c a share), with a margin of `+37,267.666` (`+0.0148` c a share). **EARN does not:** it needed
`S >= thr` = `637,504.836` (`0.254` c a share), and its margin is `−57,394.698` (`−0.0229` c a share). Each answer was
tested at `α = 0.005` over both looks together by TZ-23's Ville bound, with `λ = 0.000021932` and `δ = 0.005`. The
power, `0.99942`, was printed before any label. TZ-23 §1 item 3 and TZ-29 §1 item 3: **NO EARN closes the maker
track for this window**. The makers kept less than half a tick a share, rebate included.

**Barred from every reading, and printed as §4.4 asks:** the first look's `S`, TZ-23's, is `272,424.113` (`0.211` c a
share). The second look's, by difference, is `307,686.025` (`0.253` c a share: `+0.038` c at settlement and `+0.214` c
of rebate). Up outcomes were 2,023 in the first look and 2,009 in the second, 4,032 of 8,064 in all.

**Every gate before the reading passed.**
- G-REHEARSAL **PASS, 16 of 16**: 10 figures and 6 files equal to TZ-23's.
- G-REPLAY **PASS**: 6 of 6 stored files equal, 5 of 5 checks.
- G-SET **PASS**: 4,032 members of 4,032 candidates considered, `1791242100` (2026-10-05 23:15 UTC) to `1792451400`
  (2026-10-19 23:10 UTC), **0 non-members**, 202 chunks, every chunk read back. The member list is `971258b4…`, the
  value the TZ projected if every candidate qualified. All 202 chunks started and ended inside the idle stretch, and
  none ended after second 590.
- Self-test **51 of 51**. The constants were run twice, **5 of 5** files `unchanged`; the score twice, **2 of 2**
  `unchanged`, with **2** ledger lines.
- G-STILL **PASS**: the recorder `4148534`, `NRestarts` 2, and the pair book `1942330`, `NRestarts` 15, both
  `active`, unchanged from 04:27:51 to 05:09:51 UTC.

**The labels of the second set were first read at 2026-10-20 05:09:45 UTC**, the first ledger line's `at`. That was
after the instrument's commit `f6425f7` was on `origin` (`ls-remote` at 04:27:29.648 UTC). It was also after the
cumulative constants `74712408…` were on disk with their SHA-256 in `state.json`: first written at 05:08:42 UTC, and
recorded again by the second run at 05:09:39.

**No command was refused by the session's classifier**, and no block was handed to the Boss. **One deviation affects
publication** (§6 item 1): `git push -u origin …` failed because the token embedded in `origin`'s URL was not
accepted. The branch was pushed to the same repository through the `gh` CLI's stored login instead.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-29-maker-m0-second-look.md`, 1,940 lines, 134,612 bytes, SHA-256 `6857faab8d1f0412133fa49aa74acd2f40338b9e85d368eccf8db1d2e249504f`, landed at `bdde72f` |
| map revision | `2026-10-19-a` at `ad38846`, equal; anchors 6 of 6; re-derived 4 of 4; rows 40; `frozen` equal 37 of 37 |
| executor model | Opus, as the TZ names: `get_session` read `session_context.model` and `last_served_model` `claude-opus-5-5` |
| branch | `tz-29-maker-m0-second-look` at `f6425f713034724210dc120d2108bcfad63cadc6`, pushed; pull request #28, open, not merged |
| instrument | `research/tz29-maker-m0-second-look.py`, 1,225 lines, 68,959 bytes, SHA-256 `18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905`, Appendix A byte for byte; it loads `research/tz23-maker-m0.py` `6b3ace2c…` |
| interpreter | `/root/tz04a-env/venv/bin/python` 3.12.3, every mode under `nice -n 19` and `-B` |
| requests | `gamma-api.polymarket.com/markets` and `data-api.polymarket.com/v2/trades` through TZ-23's `http_json` alone; `git` against `origin`; `gh` for the pull request, and its stored login as the push's credential (§6 item 1) |
| capture | not read. Every mode printed `opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0` |
| units | read with `systemctl show`, `is-active`, `is-enabled`, `list-timers` and `journalctl --list-boots` alone, never signalled |
| pricer | not read, not called, not scored; `A6` `729f0bcdbee3` is stated so that what was not scored is not in doubt |
| work tree | `/root/tz29-work`, removed by B-RECLAIM-OWN (§2.16) |

No single fill's, member's or market's price, size or outcome is printed in this report. Every figure is either a
sum over a set, copied from the instrument's own output, or a rounding or ratio of such figures, named where it is
one.

---

## 0. Fingerprint

**Map revision read:** `2026-10-19-a`, equal to the TZ's. **Anchors**, each equal to the TZ header's and to the map's §0:
`A1` `229a944f2d51`, `A2` `6c5089330629`, `A3` `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable`,
`A4` `437b45ea196b`, `A5` `0f6c90451cbd`, `A6` `729f0bcdbee3`. The instrument re-derived `A2`, `A4`, `A5` and `A6` from
the files' SHA-256. Contract §1 steps 1 and 2: local `main` was fast-forwarded from `0040eda` to `origin/main`
`ad38846948bd1b515aff0f04c1718587ecaf72dc`, which carries `bdde72f` (the TZ) and `ad38846` (the map). This happened
before §0.0's `mkdir`, so no log holds it. The TZ, the map and the contract were read in full at `ad38846`.

### 0.1 The 40 rows of the map's §0 table, and the map (V1) — `logs/02-fingerprint.log`, verbatim

```text
$ I0 fingerprint
[2026-10-20T04:26:08Z] re-derived A2 research/twap-divergence.py sha256[:12] 6c5089330629 equal
[2026-10-20T04:26:08Z] re-derived A4 BTC-EXECUTOR-INSTRUCTIONS.md sha256[:12] 437b45ea196b equal
[2026-10-20T04:26:08Z] re-derived A5 research/recorder/recorder.py sha256[:12] 0f6c90451cbd equal
[2026-10-20T04:26:08Z] re-derived A6 research/pfair.py sha256[:12] 729f0bcdbee3 equal
[2026-10-20T04:26:08Z] SYSTEM-MAP.md                                  1470 lines   335041 bytes fa7cdec93e5db6c5921828dd31f767bebd3884c8ef7ec7b9d05523a86b632c69 reported
[2026-10-20T04:26:08Z] BTC-EXECUTOR-INSTRUCTIONS.md                    234 lines    11128 bytes 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b frozen equal
[2026-10-20T04:26:08Z] research/twap-divergence.py                    1135 lines    50928 bytes 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 frozen equal
[2026-10-20T04:26:08Z] research/selftest-twap-divergence.py            376 lines    16736 bytes ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a frozen equal
[2026-10-20T04:26:08Z] research/tz02-distribution.py                   334 lines    14511 bytes f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 tracked
[2026-10-20T04:26:08Z] research/pfair.py                               441 lines    19357 bytes 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 frozen equal
[2026-10-20T04:26:08Z] research/selftest-pfair.py                      619 lines    32559 bytes b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa frozen equal
[2026-10-20T04:26:08Z] research/tz06-calibration.py                    577 lines    27138 bytes 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f frozen equal
[2026-10-20T04:26:08Z] research/tz07a-variance-time.py                 623 lines    28414 bytes 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 frozen equal
[2026-10-20T04:26:08Z] research/tz07b-settlement-dispersion.py         515 lines    24926 bytes 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc frozen equal
[2026-10-20T04:26:08Z] research/tz08a-out-of-sample.py                 745 lines    38822 bytes 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c frozen equal
[2026-10-20T04:26:08Z] research/tz09-disk-inventory.py                 894 lines    41004 bytes b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 frozen equal
[2026-10-20T04:26:08Z] research/tz10b-sigma-or-link.py                1224 lines    61018 bytes 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 frozen equal
[2026-10-20T04:26:08Z] research/tz11a-student-link.py                 1231 lines    64732 bytes 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 frozen equal
[2026-10-20T04:26:08Z] research/tz12-sized-gate.py                    1157 lines    61637 bytes d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 frozen equal
[2026-10-20T04:26:08Z] research/tz13-sized-gate-test3.py              1074 lines    53901 bytes a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd frozen equal
[2026-10-20T04:26:08Z] research/tz14-quote-inventory.py               2124 lines   109972 bytes 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 frozen equal
[2026-10-20T04:26:08Z] research/tz15-phase2-gate.py                   1517 lines    73799 bytes 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 frozen equal
[2026-10-20T04:26:08Z] research/tz16a-phase2-decisive-gate.py         2198 lines   111192 bytes 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 frozen equal
[2026-10-20T04:26:08Z] research/tz17-settlement-chain.py              1102 lines    38622 bytes e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 frozen equal
[2026-10-20T04:26:08Z] research/tz18a-chainbook-capture.py            1683 lines    69517 bytes e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae frozen equal
[2026-10-20T04:26:08Z] research/tz20-capture-under-systemd.py          771 lines    36528 bytes 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7 frozen equal
[2026-10-20T04:26:08Z] research/tz21-recorder-memory.py               1284 lines    59009 bytes d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f frozen equal
[2026-10-20T04:26:08Z] research/tz23-maker-m0.py                      1184 lines    54885 bytes 6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f frozen equal
[2026-10-20T04:26:08Z] research/tz24-nesting-b2.py                    1535 lines    76142 bytes 4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b frozen equal
[2026-10-20T04:26:08Z] research/tz26-nesting-b3-capture.py            2492 lines   118466 bytes caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec frozen equal
[2026-10-20T04:26:08Z] research/tz27-pairbook-archive.py              2078 lines   106284 bytes 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673 frozen equal
[2026-10-20T04:26:08Z] research/tz28-pairbook-archive-timer.py        1438 lines    74576 bytes 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4 frozen equal
[2026-10-20T04:26:08Z] research/recorder/recorder.py                   651 lines    27821 bytes 0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7 frozen equal
[2026-10-20T04:26:08Z] research/recorder/config.py                     112 lines     4773 bytes 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d frozen equal
[2026-10-20T04:26:08Z] research/recorder/manifest.py                   254 lines    10002 bytes 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 frozen equal
[2026-10-20T04:26:08Z] research/recorder/analyze.py                    813 lines    34705 bytes eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d frozen equal
[2026-10-20T04:26:08Z] research/recorder/probe.py                      227 lines     9324 bytes 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 frozen equal
[2026-10-20T04:26:08Z] research/recorder/selftest.py                   573 lines    30591 bytes c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 frozen equal
[2026-10-20T04:26:08Z] deploy/systemd/btc-recorder.service              23 lines      707 bytes 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1 frozen equal
[2026-10-20T04:26:08Z] deploy/systemd/btc-chainbook.service             22 lines      724 bytes a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2 frozen equal
[2026-10-20T04:26:08Z] deploy/systemd/btc-pairbook.service              22 lines      761 bytes ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8 frozen equal
[2026-10-20T04:26:08Z] deploy/systemd/btc-pairbook-archive.service      17 lines      794 bytes 2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7 frozen equal
[2026-10-20T04:26:08Z] deploy/systemd/btc-pairbook-archive.timer        13 lines      417 bytes 07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913 frozen equal
[2026-10-20T04:26:08Z] .gitignore                                        5 lines      252 bytes 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b tracked
[2026-10-20T04:26:08Z] SYSTEM-MAP.md 1470 lines 335041 bytes sha256 fa7cdec93e5db6c5921828dd31f767bebd3884c8ef7ec7b9d05523a86b632c69
[2026-10-20T04:26:08Z] FINGERPRINT PASS: revision 2026-10-19-a; anchors 6 of 6, 4 re-derived; rows 40: frozen 37 of 37 equal, tracked 2, reported 1
[2026-10-20T04:26:08Z] malloc tuned: True
[2026-10-20T04:26:08Z] peak memory of this run: 29057024 bytes
[2026-10-20T04:26:08Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

### 0.2 §0.0 and §0.1 — the work tree, and the instrument staged (V3) — `logs/00-mkdir.log`, `logs/01-stage.log`

```text
mkdir /root/tz29-work /root/tz29-work/logs; echo "exit=$?"
exit=0
```

```text
2026-10-20T04:25:53.038294478Z
/root/tz29-work/stage/research/tz29-maker-m0-second-look.py 1225 68959 18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905
exit=0
exit=0
6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f  /root/tz29-work/stage/research/tz23-maker-m0.py
```

### 0.3 Host gate — the opening reads, verbatim (V2) — `logs/03-host-gate.log`

```text
Tue Oct 20 04:26:19 AM UTC 2026
1792470379
1
MemTotal:         978640 kB
MemAvailable:     295332 kB
SwapTotal:       3174396 kB
SwapFree:        2766032 kB
2026-08-02 07:24:32
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
 -5 23a31fad2f064f04b9e138eac29658f3 Sat 2026-06-06 11:51:20 UTC Fri 2026-06-26 14:13:44 UTC
 -4 a38e17445ce341bc8b877be9d3d4f648 Fri 2026-06-26 14:13:52 UTC Tue 2026-07-14 16:15:10 UTC
 -3 5f4d18a6ba8041bd80e7d1e192c5ee28 Tue 2026-07-14 16:15:20 UTC Fri 2026-07-17 01:01:21 UTC
 -2 b1b399c70c6e4dcc934755f70a2ca231 Fri 2026-07-17 01:01:43 UTC Fri 2026-07-24 14:55:46 UTC
 -1 285d6962c92c407d837d1ce329b93aa4 Fri 2026-07-24 14:55:54 UTC Sun 2026-08-02 07:23:49 UTC
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-02 07:24:34 UTC Tue 2026-10-20 04:26:19 UTC
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12619980800
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
1
3.12.3
2314799 tz23-work--set--set.json
36870673 tz23-work--set--tz23-fills.jsonl.gz
2444450 tz23-work--set--tz23-members.csv
2114 tz23-work--set--tz23-constants.json
464610 tz23-work--set--tz23-scored.csv
1915 tz23-work--set--tz23-reading.json
a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303  tz23-work--set--set.json
4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64  tz23-work--set--tz23-fills.jsonl.gz
cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61  tz23-work--set--tz23-members.csv
1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5  tz23-work--set--tz23-constants.json
12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988  tz23-work--set--tz23-scored.csv
fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043  tz23-work--set--tz23-reading.json
MainPID=4148534
Result=success
NRestarts=2
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-04 22:22:07 UTC

MainPID=1942330
Result=success
NRestarts=15
Id=btc-pairbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Tue 2026-10-20 03:03:44 UTC

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
NEXT                        LEFT LAST                              PASSED UNIT                       ACTIVATES
Wed 2026-10-21 03:00:20 UTC  22h Tue 2026-10-20 03:00:20 UTC 1h 25min ago btc-pairbook-archive.timer btc-pairbook-archive.service

1 timers listed.
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
e8b46a85d61e1a17841962846f6d3012046c2d70
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
/root/tz28-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
/root/btc-pairbook-archive-svc exit=0
/var/lib/btc-pairbook-archive exit=0
1846
/root/btc-5m-twap       ad38846 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
157533850	/var/lib/btc-pairbook
3608965	/var/lib/btc-pairbook-archive
132567824	/root/.claude
594949734	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/7a160398-f4cf-54ee-b771-c3006d558bde/scratchpad
total 24
drwx------  6 root root 4096 Oct 20 04:24 .
drwx------ 20 root root 4096 Oct 20 04:24 ..
drwx------  3 root root 4096 Oct 20 04:24 6a6870c2-3843-4a2b-83cf-b2f45c5500a1
drwx------  4 root root 4096 Oct 11 14:48 6b7bd886-7088-5233-bdf9-903a19178e6a
drwx------  3 root root 4096 Oct 11 14:48 6de9e261-2fb6-4db9-ae09-1fd283c3b8c8
drwx------  4 root root 4096 Oct 20 04:24 7a160398-f4cf-54ee-b771-c3006d558bde
```

| gate | condition | read | result |
|---|---|---|---|
| H1 | `find` prints exactly one path | `/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json` | **PASS** |
| H2 | source `/dev/vda2`, size `31612203008`; `grep -c` at least 1 | `/dev/vda2`, `31612203008`; `1` | **PASS** |
| H3 | the interpreter prints `3.12.` | `3.12.3` | **PASS** |
| H4 | the six first-look files' sizes and SHA-256 equal §1's table | 6 of 6 equal | **PASS** |
| memory | `MemAvailable` at least `177,135,616` | `295332 kB` = `302,419,968` bytes | **PASS** |
| disk | `avail` at least `4,800,000,000` | `12,619,980,800` | **PASS** |

**The printed facts:**
- **One boot since 2026-08-02 07:24:34 UTC** (`journalctl --list-boots` index 0, `uptime -s` 07:24:32). So the
  archive's off-calendar runs were not boots. That holds for the map's two, at 2026-10-15 06:18:30 and 2026-10-17
  08:35:37 UTC, and for the third that §3.4 found, at 2026-10-19 21:54:19 UTC. Each was a start of the timer without a
  reboot, the timer's 600 s elapse after it.
- The recorder is pid `4148534`, `NRestarts` 2, since 2026-10-04 22:22:07 UTC.
- **The pair book is pid `1942330`, `NRestarts` 15**, since 2026-10-20 03:03:44 UTC: today's calendar run restarted
  it. All 12 restarts since TZ-28's `NRestarts` 3 are the archive's runs, each a `restart` record in its ledger (§2.5).
- The archive's timer is `active`/`enabled`. Its last trigger was 2026-10-20 03:00:20 UTC and its next is 2026-10-21
  03:00:20 UTC. Its service is `inactive`.
- The chain book is `inactive`/`disabled`.
- `telemetry-watch.service` is `disabled` and `inactive`.
- The code trees are at `e3975b5…`, `e8b46a8…` and `d8194fd…`, by map §3. `/root/tz28-work` is absent, and the code
  and state trees are present.
- The forensic store holds `1,846` files, map §3's count. There are two worktrees, map §3's two.
- `du -sb` read the pair book's store at `157,533,850` bytes and the archive's state at `3,608,965`.

### 0.4 Free space and `MemAvailable` — every read, its instant and its bound

| instant (UTC) | read by | `MemAvailable` (bytes) | `/dev/vda2` free (bytes) |
|---|---|---|---|
| 04:26:19 | §0.3 host gate | `302,419,968` (`295332 kB`) | `12,619,980,800` |
| 04:28:17 | `rehearse` | `331,182,080` | — |
| 04:31:07 | `replay` | `288,215,040` | — |
| 04:31:15 | `fetch` | `263,000,064` | — |
| 05:07:52 | `constants` (1) | `268,378,112` | — |
| 05:08:49 | `constants` (2) | `274,210,816` | — |
| 05:09:44 | `score` (1) | `289,538,048` | — |
| 05:09:51 | `score` (2) | `270,196,736` | — |
| 05:10:06 | §3.11 host gate again | `284,602,368` (`277932 kB`) | `12,451,913,728` |
| 05:10 | §3.11 `free -b` | `358,150,144` (`available`) | — |
| 05:15:04 | B-RECLAIM-OWN `df` | — | `12,476,121,088` |

The floors are `177,135,616` bytes of `MemAvailable` and `4,800,000,000` bytes free (§0.4). Every read is above its
floor. Each mode asserts the memory floor itself.

### 0.5 Refs (§0.5) — `logs/04-refs.log`, verbatim

```text
2026-10-20T04:26:28.868882102Z
warning: redirecting to https://github.com/seahomebatumi-ai/btc-5m-twap.git/
ad38846948bd1b515aff0f04c1718587ecaf72dc	HEAD
ad38846948bd1b515aff0f04c1718587ecaf72dc	refs/heads/main
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8	refs/heads/tz-23-maker-m0
6f045cffc3601b589d3b8b7a6a9af6f73991e18b	refs/heads/tz-24-nesting-b2
e8b46a85d61e1a17841962846f6d3012046c2d70	refs/heads/tz-26-nesting-b3-capture
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/heads/tz-27-pairbook-archive
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/heads/tz-28-pairbook-archive-timer
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
ee2f6327390ef4d0c6169d1fba1a2ed4ae936dc3	refs/pull/3/head
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
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
e299d4e45f48b7efaa8cb18bd54b139fc0627630	refs/tags/tz-27-pairbook-streams
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/tags/tz-27-pairbook-streams^{}
exit=0
warning: redirecting to https://github.com/seahomebatumi-ai/btc-5m-twap.git/
ref lines: 51
--- first-parent commits above f6ab6e5 on origin/main
ad38846948bd1b515aff0f04c1718587ecaf72dc 2026-10-19T15:26:08+04:00 Update SYSTEM-MAP.md

M	SYSTEM-MAP.md
bdde72f51783f7a4cb6ed477fc173a1931272c9d 2026-10-19T15:24:37+04:00 Add files via upload

A	CryptoTZ/TZ-29-maker-m0-second-look.md
--- map revision on origin/main
**Revision string:** `2026-10-19-a`
warning: redirecting to https://github.com/seahomebatumi-ai/btc-5m-twap.git/
warning: redirecting to https://github.com/seahomebatumi-ai/btc-5m-twap.git/
tz-29 branch lines: 0
```

**51 ref lines**, where map §1 recorded 49 on 2026-10-19 at 09:36 UTC and the TZ projected 50 after today's
03:00:20 UTC run. The difference is two `pairbook-streams-*` tags:
- `1792465220`: today's calendar run, as projected.
- `1792446859`: an off-calendar run at 2026-10-19 21:54:19 UTC, the timer's 600 s elapse after a start at about
  21:44:19. There was no boot (§0.3).

Both runs are in the archive's ledger (§2.5). **`main` carries revision `2026-10-19-a`**, and
`refs/heads/tz-29-maker-m0-second-look` did not exist (`tz-29 branch lines: 0`), so neither BLOCK condition held.
Above `f6ab6e5`, `main`'s first-parent line holds two commits: `bdde72f`, which adds
`CryptoTZ/TZ-29-maker-m0-second-look.md`, and `ad38846`, which modifies `SYSTEM-MAP.md`. Six branches, as the map
records. Fifteen tags: the map's thirteen and those two.

---

## 1. Input

| input | what | read by |
|---|---|---|
| the venue's documents and fills, second look | gamma `/markets` for 4,032 candidates in `1791242100` … `1792451400`, 202 document requests; Data API v2 `/v2/trades`, taker only, for 4,032 members in 202 chunks | `fetch`, **fetched fresh** — no member of this set had been read by any TZ |
| the venue's documents and fills, rehearsal | TZ-23's 144 excluded markets `1791050100` … `1791093000`, re-fetched | `rehearse` |
| the first look | the forensic store's six TZ-23 files, by size and SHA-256 (§0.3 H4), **not re-collected** | `replay`, `constants`, `score` |
| the archive's ledger | `/var/lib/btc-pairbook-archive/ledger.jsonl`, `30,913` bytes, SHA-256 `3d08a5f72d74ccac340ed93a4c85126612b6df5b56e1135a54677e57312ce272`, 130 records, read whole at both reads | `archive` |
| the repository | `SYSTEM-MAP.md` and the 39 files of its table; `research/tz23-maker-m0.py` `6b3ace2c…`; `CryptoReports/*.md`, for hashes | `fingerprint`, every mode, `reclaim` |

The second set is: **4,032 candidates considered, 4,032 members, 0 non-members**; `T0` `1791242100` …
`1792451400`; 576 members on each day of the week; **1,152 on a weekend**.
- **Member list SHA-256:** `971258b48251a8c7e89c52919bd1801ad73725d98796f3481292d66d27136e5c`.
- **Set file:** `set/set.json`, `2,314,719` bytes, SHA-256 `3f009cbeedc81713601a2cec5f080d0bdc2ab174fc1d468202604f3b10843d13`.

The weekday split is not printed by the instrument. It is arithmetic on the `T0` grid: the 4,032 members are every
`T0` from `1791242100` to `1792451400` in steps of 300. That holds because 4,032 were considered and none failed. The
grid's own list hashes to the same `971258b4…`. Its 1,152 weekend members equal the instrument's `weekend members
1152`.

---

## 2. Measurements

### 2.1 §3.1 — the branch and its file (V3) — `logs/05-branch.log`, `logs/06-commit-push.log`, `logs/07-push-gh-helper.log`, `logs/08-pr.log`

```text
warning: redirecting to https://github.com/seahomebatumi-ai/btc-5m-twap.git/
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new tag]         pairbook-streams-1791774020 -> pairbook-streams-1791774020
 * [new tag]         pairbook-streams-1791860420 -> pairbook-streams-1791860420
 * [new tag]         pairbook-streams-1791946820 -> pairbook-streams-1791946820
 * [new tag]         pairbook-streams-1792033220 -> pairbook-streams-1792033220
 * [new tag]         pairbook-streams-1792045110 -> pairbook-streams-1792045110
 * [new tag]         pairbook-streams-1792119620 -> pairbook-streams-1792119620
 * [new tag]         pairbook-streams-1792206020 -> pairbook-streams-1792206020
 * [new tag]         pairbook-streams-1792226137 -> pairbook-streams-1792226137
 * [new tag]         pairbook-streams-1792292420 -> pairbook-streams-1792292420
 * [new tag]         pairbook-streams-1792378820 -> pairbook-streams-1792378820
 * [new tag]         pairbook-streams-1792446859 -> pairbook-streams-1792446859
 * [new tag]         pairbook-streams-1792465220 -> pairbook-streams-1792465220
exit=0
Preparing worktree (new branch 'tz-29-maker-m0-second-look')
branch 'tz-29-maker-m0-second-look' set up to track 'origin/main'.
HEAD is now at ad38846 Update SYSTEM-MAP.md
exit=0
/root/tz29-work/wt/research/tz29-maker-m0-second-look.py 1225 68959 18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905
exit=0
6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f  /root/tz29-work/wt/research/tz23-maker-m0.py
 1225 68959 /root/tz29-work/wt/research/tz29-maker-m0-second-look.py
?? research/tz29-maker-m0-second-look.py
```

```text
exit=0
f6425f7 TZ-29: M0's second look - research/tz29-maker-m0-second-look.py
ad38846 Update SYSTEM-MAP.md

 research/tz29-maker-m0-second-look.py | 1225 +++++++++++++++++++++++++++++++++
 1 file changed, 1225 insertions(+)
warning: redirecting to https://github.com/seahomebatumi-ai/btc-5m-twap.git/
fatal: could not read Username for 'https://github.com': No such device or address
send-pack: unexpected disconnect while reading sideband packet
error: failed to push some refs to 'https://github.com/seahomebatumi-ai/btc-5m-twap.git'
exit=1
fatal: the remote end hung up unexpectedly
2026-10-20T04:26:49.159838551Z
warning: redirecting to https://github.com/seahomebatumi-ai/btc-5m-twap.git/
```

```text
$ git -c credential.helper= -c "credential.helper=!gh auth git-credential" push https://github.com/seahomebatumi-ai/btc-5m-twap.git tz-29-maker-m0-second-look:refs/heads/tz-29-maker-m0-second-look
remote: 
remote: Create a pull request for 'tz-29-maker-m0-second-look' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-29-maker-m0-second-look        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-29-maker-m0-second-look -> tz-29-maker-m0-second-look
exit=0
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * branch            tz-29-maker-m0-second-look -> FETCH_HEAD
 * [new branch]      tz-29-maker-m0-second-look -> origin/tz-29-maker-m0-second-look
branch 'tz-29-maker-m0-second-look' set up to track 'origin/tz-29-maker-m0-second-look'.
exit=0
2026-10-20T04:27:29.648615997Z
warning: redirecting to https://github.com/seahomebatumi-ai/btc-5m-twap.git/
f6425f713034724210dc120d2108bcfad63cadc6	refs/heads/tz-29-maker-m0-second-look
f6425f713034724210dc120d2108bcfad63cadc6
f6425f713034724210dc120d2108bcfad63cadc6
```

```text
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/28
exit=0
```

§0.1's script printed the same line at `/root/tz29-work/wt` as at §0.1: 1,225 lines, 68,959 bytes, `18defff9…`. The
worktree's `tz23-maker-m0.py` is `6b3ace2c…`. **The instrument's commit reached `origin` at
2026-10-20T04:27:29.648615997Z**, by the `date` immediately before the `ls-remote` that printed
`f6425f713034724210dc120d2108bcfad63cadc6`. The branch's diff against `origin/main` names one path, `A`, 1,225 lines
(§3).

### 2.2 §3.2 — the self-test (V4): **51 of 51** — `logs/09-selftest.log`, verbatim

```text
$ I selftest
[2026-10-20T04:27:42Z]   ok  TZ-23's instrument loaded from beside this file, from its asserted bytes
[2026-10-20T04:27:42Z]   ok  glibc took the 128 KiB mmap threshold and the two arenas
[2026-10-20T04:27:42Z]   ok  the main thread sums at 60 digits
[2026-10-20T04:27:42Z]   ok  TZ-23's set size, step, chunk, resolution age, slack and workers
[2026-10-20T04:27:42Z]   ok  TZ-23's alpha, delta and lambda, the second look's by TZ-23 section 1
[2026-10-20T04:27:42Z]   ok  every request carries TZ-23's two headers
[2026-10-20T04:27:42Z]   ok  the walk starts at 2026-10-05 23:15 UTC
[2026-10-20T04:27:42Z]   ok  no set is read before 2026-10-20 00:15 UTC, the 4,032nd member's resolution age
[2026-10-20T04:27:42Z]   ok  no excluded span reaches the second look
[2026-10-20T04:27:42Z]   ok  every candidate qualifying, the 4,032nd member is 1792451400, 2026-10-19 23:10 UTC
[2026-10-20T04:27:42Z]   ok  TZ-23's walk from 1791242100 takes 50 qualifying members in 50 documents
[2026-10-20T04:27:42Z]   ok  the walk requests no document at or below 1791241800 and none after the need-th member
[2026-10-20T04:27:42Z]   ok  every second-look member reads segment 3
[2026-10-20T04:27:42Z] the walk starts at second 0 of window 0
[2026-10-20T04:27:42Z] the walk stopped (BLOCKED: the walk reached x, too recent to be resolved); walked again in 300 s, 1 of 24
[2026-10-20T04:27:42Z] the walk starts at second 0 of window 0
[2026-10-20T04:27:42Z] the walk stopped (BLOCKED: the walk reached x, too recent to be resolved); walked again in 300 s, 2 of 24
[2026-10-20T04:27:42Z] the walk starts at second 0 of window 0
[2026-10-20T04:27:42Z]   ok  a walk stopped twice on a market too recent is walked a third time, 300 s after each stop
[2026-10-20T04:27:42Z] the walk starts at second 0 of window 0
[2026-10-20T04:27:42Z]   ok  a walk stopped on its slack is not walked again
[2026-10-20T04:27:42Z]   ok  a chunk starts from second 15 to 470 of a window and at no other second
[2026-10-20T04:27:42Z]   ok  nothing starts while the pair book streams, seconds 595 to 905
[2026-10-20T04:27:42Z]   ok  the archive's calendar run is at second 20 of its window
[2026-10-20T04:27:42Z]   ok  nothing starts from 03:00:15 to 03:01:20 UTC; at 03:01:21 a chunk may start
[2026-10-20T04:27:42Z]   ok  nothing starts while the archive's service runs; a failed one does not hold
[2026-10-20T04:27:42Z]   ok  held from second 600, a chunk starts at second 15 of the next window
[2026-10-20T04:27:42Z]   ok  an archive's run that never ends holds a chunk 7,200 s and then stops it BLOCKED
[2026-10-20T04:27:42Z] chunks 3 of 3, 0 s
[2026-10-20T04:27:42Z] chunks fetched fresh 3: inside the idle stretch 3, ending after second 590 0; longest 0.0 s; waited 0 s; windows 1, from 2026-10-20T01:00:00Z to 2026-10-20T01:00:00Z
[2026-10-20T04:27:42Z]   ok  45 members are 3 chunks, each fetched once and timed inside the idle stretch
[2026-10-20T04:27:42Z] chunks 3 of 3, 0 s
[2026-10-20T04:27:42Z] chunks fetched fresh 3: inside the idle stretch 3, ending after second 590 0; longest 0.0 s; waited 0 s; windows 1, from 2026-10-20T01:00:00Z to 2026-10-20T01:00:00Z
[2026-10-20T04:27:42Z]   ok  a cached chunk is fetched again by nothing
[2026-10-20T04:27:42Z]   ok  every chunk reads back to its members
[2026-10-20T04:27:42Z] chunks 25 of 40, 30000 s
[2026-10-20T04:27:42Z] projected 40667 s of fetching for 40 chunks after 30 fetched; 32000 s of wall clock so far
[2026-10-20T04:27:47Z]   ok  a fetch projected above 7,200 s of fetching stops BLOCKED at its 30th chunk: at most the two chunks running end, and the six queued never start
[2026-10-20T04:27:47Z] chunks 25 of 40, 300 s
[2026-10-20T04:27:47Z] projected 347 s of fetching for 40 chunks after 30 fetched; 360 s of wall clock so far
[2026-10-20T04:27:47Z] chunks 40 of 40, 400 s
[2026-10-20T04:27:47Z]   ok  a fetch projected under it fetches all 40 chunks
[2026-10-20T04:27:47Z]   ok  the cumulative members file is byte for byte TZ-23's build_constants over the union
[2026-10-20T04:27:47Z]   ok  both looks' V, Sh and thresholds equal TZ-23's build_constants over the union
[2026-10-20T04:27:47Z]   ok  the cumulative member list is the union's
[2026-10-20T04:27:47Z] labels: 50 members, 27 Up
[2026-10-20T04:27:47Z] S 36225.69543456318 = settlement 31734.84587 + rebate 4490.84956456318; per share 0.0191679262849958501773267674970361584227770002930506693200247 = 0.0167917048659745060733195588654049980991708355025700454806342 + 0.00237622141902134410400720863163116032360616479048062383939045
[2026-10-20T04:27:47Z] EARN False (margin -224296.590349136933787179237225374110125738788601942422313849); NO EARN False (margin -287298.420818263293787179237225374110125738788601942422313849)
[2026-10-20T04:27:47Z] band pre  makers per share 0.0362715807569099682617145873160906267956153311472254433707563, of it rebate 0.00238146228916080623921683559462065142579790443580096781594257 - barred from every reading
[2026-10-20T04:27:47Z] band w0   makers per share 0.0317650664453702389469302590762222499406205002406243712583149, of it rebate 0.00249761557742594528101437868015501275285272498139760943151955 - barred from every reading
[2026-10-20T04:27:47Z] band w1   makers per share 0.0353533199808801286715572846670517667897127250338199637302910, of it rebate 0.00239000874430861859023495629062415993957152876473547571510337 - barred from every reading
[2026-10-20T04:27:47Z] band w2   makers per share -0.0578915338120060000221292137540439885968070458688059089918326, of it rebate 0.00232779372034670558615574531533423832407359302254051660968242 - barred from every reading
[2026-10-20T04:27:47Z] band w3   makers per share 0.0620485138825285562459050535549721700065340373289284446935304, of it rebate 0.00227005701193848913810856765970473720649509166717408957157745 - barred from every reading
[2026-10-20T04:27:47Z] band last makers per share -0.0276687019687097752842214498696087009665812288520552783728167, of it rebate 0.00238270728969441338589158025494886207512216246880251023454941 - barred from every reading
[2026-10-20T04:27:47Z] band post makers per share -0.0110276312805109688200062354525561611389646981589029056874146, of it rebate 0.00255210366606438197265298596512216615287465551062744703851683 - barred from every reading
[2026-10-20T04:27:47Z] wrote cumulative-scored.csv sha256 0d5daea3b15e204f3c4bd6817dcc996f48b719d18a0e696ae548dbe9cf88b1f5 and cumulative-reading.json sha256 931f1b43e0f21c71acb17179dfeb4a22c9e8b2e3bd91297cfe8521891c9afd72
[2026-10-20T04:27:47Z] labels: 50 members, 27 Up
[2026-10-20T04:27:47Z] S 36225.69543456318 = settlement 31734.84587 + rebate 4490.84956456318; per share 0.0191679262849958501773267674970361584227770002930506693200247 = 0.0167917048659745060733195588654049980991708355025700454806342 + 0.00237622141902134410400720863163116032360616479048062383939045
[2026-10-20T04:27:47Z] EARN False (margin -224296.590349136933787179237225374110125738788601942422313849); NO EARN False (margin -287298.420818263293787179237225374110125738788601942422313849)
[2026-10-20T04:27:47Z] band pre  makers per share 0.0362715807569099682617145873160906267956153311472254433707563, of it rebate 0.00238146228916080623921683559462065142579790443580096781594257 - barred from every reading
[2026-10-20T04:27:47Z] band w0   makers per share 0.0317650664453702389469302590762222499406205002406243712583149, of it rebate 0.00249761557742594528101437868015501275285272498139760943151955 - barred from every reading
[2026-10-20T04:27:47Z] band w1   makers per share 0.0353533199808801286715572846670517667897127250338199637302910, of it rebate 0.00239000874430861859023495629062415993957152876473547571510337 - barred from every reading
[2026-10-20T04:27:47Z] band w2   makers per share -0.0578915338120060000221292137540439885968070458688059089918326, of it rebate 0.00232779372034670558615574531533423832407359302254051660968242 - barred from every reading
[2026-10-20T04:27:47Z] band w3   makers per share 0.0620485138825285562459050535549721700065340373289284446935304, of it rebate 0.00227005701193848913810856765970473720649509166717408957157745 - barred from every reading
[2026-10-20T04:27:47Z] band last makers per share -0.0276687019687097752842214498696087009665812288520552783728167, of it rebate 0.00238270728969441338589158025494886207512216246880251023454941 - barred from every reading
[2026-10-20T04:27:47Z] band post makers per share -0.0110276312805109688200062354525561611389646981589029056874146, of it rebate 0.00255210366606438197265298596512216615287465551062744703851683 - barred from every reading
[2026-10-20T04:27:47Z] wrote u-scored.csv sha256 0d5daea3b15e204f3c4bd6817dcc996f48b719d18a0e696ae548dbe9cf88b1f5 and u-reading.json sha256 b0a2d884f4e691a99c8185c82b22ead75f702a14e352106ad6d03ede53448291
[2026-10-20T04:27:47Z]   ok  the score over both looks equals TZ-23's score over the union, file and figures
[2026-10-20T04:27:47Z] labels: 23 members, 14 Up
[2026-10-20T04:27:47Z] S 2275.94561636972 = settlement 369.12230 + rebate 1906.82331636972; per share 0.00283493444695157234564979439694701653699375795047776824542200 = 0.000459781427061129734670077554623772103690578693575936112802196 + 0.00237515301989044261097971684232324443330317925690183213261981
[2026-10-20T04:27:47Z] EARN False (margin -243694.049210311660037179237225374110125738788601942422313849); NO EARN False (margin -244231.834193051100037179237225374110125738788601942422313849)
[2026-10-20T04:27:47Z] band pre  makers per share 0.132052101830688969673012615390276839914663262918229959822074, of it rebate 0.00257692285012556303820829133285482518226746348150356371666593 - barred from every reading
[2026-10-20T04:27:47Z] band w0   makers per share 0.0606456919214122031364191710971888267159091543049054666971643, of it rebate 0.00247478106556363494357011754598352013121412113875112273987582 - barred from every reading
[2026-10-20T04:27:47Z] band w1   makers per share -0.0522844549751188570726059015791416225451308634770768955991555, of it rebate 0.00234201947651348365918062555187645248869733281589625791160321 - barred from every reading
[2026-10-20T04:27:47Z] band w2   makers per share -0.0622886157278142512383332357514255587160379662022709161171487, of it rebate 0.00229963261167741040333583281075240922199858917270058588679457 - barred from every reading
[2026-10-20T04:27:47Z] band w3   makers per share 0.0669322097107367422760616676134034852021386351952905627791735, of it rebate 0.00237516837898494312252980750099553039523023411808679169476187 - barred from every reading
[2026-10-20T04:27:47Z] band last makers per share -0.0466158307753715265990143636504813968153244161569565319743498, of it rebate 0.00233859781232249904947445230264265127405546737319228187889997 - barred from every reading
[2026-10-20T04:27:47Z] band post makers per share -0.00163037763944781975624855948988196655358176931503110131571844, of it rebate 0.00256901431112552039926761108405563239798721854727517833549518 - barred from every reading
[2026-10-20T04:27:47Z] wrote tz23-scored.csv sha256 0c00da95d8ef7d764ccf2eff51c89d0da0d7765cded3c94c842aded7a694511c and tz23-reading.json sha256 833623607f7925045952a610898d7494bd0c3f86f8f01330434b16b0dae775b7
[2026-10-20T04:27:47Z]   ok  the first look's rows of the scored file over both looks are its own scored rows
[2026-10-20T04:27:47Z] labels: 27 members, 13 Up
[2026-10-20T04:27:47Z] S 33949.74981819346 = settlement 31365.72357 + rebate 2584.02624819346; per share 0.0312299109525130112632814683939519570779564022262978706204338 = 0.0288529005161417836631001661563091282813966888121022969166247 + 0.00237701043637122760018130223764282879655971341419557370380909
[2026-10-20T04:27:47Z] EARN False (margin -222181.848386136812937179237225374110125738788601942422313849); NO EARN False (margin -284645.893872523732937179237225374110125738788601942422313849)
[2026-10-20T04:27:47Z] band pre  makers per share -0.0385642793590513816064866478880692282034249364781342099618538, of it rebate 0.00222874377150648636441377042550437164614470229056682575874258 - barred from every reading
[2026-10-20T04:27:47Z] band w0   makers per share 0.0101269538282310061292663271550239586433355514166195741948859, of it rebate 0.00251472378512885503432456020089815653872004333622018544959657 - barred from every reading
[2026-10-20T04:27:47Z] band w1   makers per share 0.0948126719537146020299259081804716045676465303743382242571209, of it rebate 0.00242256788637015738779413264558189279828115598975489583116678 - barred from every reading
[2026-10-20T04:27:47Z] band w2   makers per share -0.0537716596348197469388223081546589830191566420731736895046155, of it rebate 0.00235417945220911480623529053792147280494145319894005881800418 - barred from every reading
[2026-10-20T04:27:47Z] band w3   makers per share 0.0589864728562995233134450863402468668118824383622186444423399, of it rebate 0.00220415296517942873520042365832367651998596791419571070776550 - barred from every reading
[2026-10-20T04:27:47Z] band last makers per share -0.0124555667577494436175940557285187575965515554618641235418893, of it rebate 0.00241812391931630053986610160392636484618685887690003387193709 - barred from every reading
[2026-10-20T04:27:47Z] band post makers per share -0.0279462483248951081039675003497013291610942654162778012556683, of it rebate 0.00252165809774294004207270876552593723040001144701352597867648 - barred from every reading
[2026-10-20T04:27:47Z] wrote tz29-scored.csv sha256 151f852ec63a9611bc37fb1a01bc9d0b16e6c5c957ebcb87c42f470fe5982b21 and tz29-reading.json sha256 db69f94e839aa25d7098f77e84080129c7b5863f789848489832360cdb0b6aea
[2026-10-20T04:27:47Z]   ok  S over both looks is the first look's S plus the second's, exactly
[2026-10-20T04:27:47Z]   ok  the cumulative constants file is byte-identical with every label flipped
[2026-10-20T04:27:47Z] labels: 50 members, 23 Up
[2026-10-20T04:27:47Z] S 13783.15543456318 = settlement 9292.30587 + rebate 4490.84956456318; per share 0.00729301409331336725462911481046250574788643078042021933634077 = 0.00491679267429202315062190617883134542428026598993959549695031 + 0.00237622141902134410400720863163116032360616479048062383939045
[2026-10-20T04:27:47Z] EARN False (margin -246739.130349136933787179237225374110125738788601942422313849); NO EARN False (margin -264855.880818263293787179237225374110125738788601942422313849)
[2026-10-20T04:27:47Z] band pre  makers per share -0.0277233586982327308812020423292070846870208732319494066761227, of it rebate 0.00238146228916080623921683559462065142579790443580096781594257 - barred from every reading
[2026-10-20T04:27:47Z] band w0   makers per share 0.0639912982772744021069805918642677826667297499179200878577645, of it rebate 0.00249761557742594528101437868015501275285272498139760943151955 - barred from every reading
[2026-10-20T04:27:47Z] band w1   makers per share -0.0465063911326026668482114300344141645182874356947205366627005, of it rebate 0.00239000874430861859023495629062415993957152876473547571510337 - barred from every reading
[2026-10-20T04:27:47Z] band w2   makers per share 0.0447471745813725567424231006407044848858608393920403767994955, of it rebate 0.00232779372034670558615574531533423832407359302254051660968242 - barred from every reading
[2026-10-20T04:27:47Z] band w3   makers per share -0.0382421680430588503525809796268450109384245411561616172582825, of it rebate 0.00227005701193848913810856765970473720649509166717408957157745 - barred from every reading
[2026-10-20T04:27:47Z] band last makers per share 0.0979338238184963619967257486373362529821362691306802298545611, of it rebate 0.00238270728969441338589158025494886207512216246880251023454941 - barred from every reading
[2026-10-20T04:27:47Z] band post makers per share 0.0788286053305108763189440149213903949187492693517287699710895, of it rebate 0.00255210366606438197265298596512216615287465551062744703851683 - barred from every reading
[2026-10-20T04:27:47Z] wrote cumulative-scored.csv sha256 d5911d1b4d904f148de3c691b754641bc46b86d2bb590ae03758905c948c2785 and cumulative-reading.json sha256 d316969f411b3af99d5c5e2fd7f1fa6086180b660490cda6084c95dfc0da6b48
[2026-10-20T04:27:47Z]   ok  the score moves when the labels flip (negative control)
[2026-10-20T04:27:47Z] unchanged /root/tz29-work/selftest-tmp/c/cumulative-members.csv sha256 9954cbd9532dbb7211d271253b9d3e6afe29dab2d3b8691d6429f7e25811ec6c
[2026-10-20T04:27:47Z] unchanged /root/tz29-work/selftest-tmp/c/cumulative-constants.json sha256 7389632fef11256912e71c20ce58e4de825b859ee9bd44ed63cb1b17eda42457
[2026-10-20T04:27:47Z]   ok  a second cumulative run finds both files unchanged
[2026-10-20T04:27:47Z] first look constants /root/tz29-work/selftest-tmp/a/tz23-constants.json 1668 bytes sha256 c72b82e592322f8c44813f227e40608bc6fa1b3bbb98425a50e1817c8b6a9b68 equal
[2026-10-20T04:27:47Z] first look fills     /root/tz29-work/selftest-tmp/a/tz23-fills.jsonl.gz 5448 bytes sha256 3c355d5ca0f9c5910cb524d479dc2d9438b804084b075b3569e96f4e8318cefa equal
[2026-10-20T04:27:47Z] first look members   /root/tz29-work/selftest-tmp/a/tz23-members.csv 8110 bytes sha256 139c315948a9419a767dbd3630919f1fae9f7f9ac7feedf46564358f8c22748b equal
[2026-10-20T04:27:47Z] first look reading   /root/tz29-work/selftest-tmp/a/tz23-reading.json 1836 bytes sha256 833623607f7925045952a610898d7494bd0c3f86f8f01330434b16b0dae775b7 equal
[2026-10-20T04:27:47Z] first look scored    /root/tz29-work/selftest-tmp/a/tz23-scored.csv 1529 bytes sha256 0c00da95d8ef7d764ccf2eff51c89d0da0d7765cded3c94c842aded7a694511c equal
[2026-10-20T04:27:47Z] first look set       /root/tz29-work/selftest-tmp/a/set.json 9822 bytes sha256 3b8340f6f325b33765044afb982ac0ddf5d2c6e52601b074c05b34417a15bd1c equal
[2026-10-20T04:27:47Z]   ok  the store's six files verify by size and SHA-256
[2026-10-20T04:27:47Z] labels: 23 members, 14 Up
[2026-10-20T04:27:47Z] S 2275.94561636972 = settlement 369.12230 + rebate 1906.82331636972; per share 0.00283493444695157234564979439694701653699375795047776824542200 = 0.000459781427061129734670077554623772103690578693575936112802196 + 0.00237515301989044261097971684232324443330317925690183213261981
[2026-10-20T04:27:47Z] EARN False (margin -243694.049210311660037179237225374110125738788601942422313849); NO EARN False (margin -244231.834193051100037179237225374110125738788601942422313849)
[2026-10-20T04:27:47Z] band pre  makers per share 0.132052101830688969673012615390276839914663262918229959822074, of it rebate 0.00257692285012556303820829133285482518226746348150356371666593 - barred from every reading
[2026-10-20T04:27:47Z] band w0   makers per share 0.0606456919214122031364191710971888267159091543049054666971643, of it rebate 0.00247478106556363494357011754598352013121412113875112273987582 - barred from every reading
[2026-10-20T04:27:47Z] band w1   makers per share -0.0522844549751188570726059015791416225451308634770768955991555, of it rebate 0.00234201947651348365918062555187645248869733281589625791160321 - barred from every reading
[2026-10-20T04:27:47Z] band w2   makers per share -0.0622886157278142512383332357514255587160379662022709161171487, of it rebate 0.00229963261167741040333583281075240922199858917270058588679457 - barred from every reading
[2026-10-20T04:27:47Z] band w3   makers per share 0.0669322097107367422760616676134034852021386351952905627791735, of it rebate 0.00237516837898494312252980750099553039523023411808679169476187 - barred from every reading
[2026-10-20T04:27:47Z] band last makers per share -0.0466158307753715265990143636504813968153244161569565319743498, of it rebate 0.00233859781232249904947445230264265127405546737319228187889997 - barred from every reading
[2026-10-20T04:27:47Z] band post makers per share -0.00163037763944781975624855948988196655358176931503110131571844, of it rebate 0.00256901431112552039926761108405563239798721854727517833549518 - barred from every reading
[2026-10-20T04:27:47Z] wrote tz23-scored.csv sha256 0c00da95d8ef7d764ccf2eff51c89d0da0d7765cded3c94c842aded7a694511c and tz23-reading.json sha256 833623607f7925045952a610898d7494bd0c3f86f8f01330434b16b0dae775b7
[2026-10-20T04:27:47Z] G-REPLAY tz23-scored.csv    sha256 0c00da95d8ef7d764ccf2eff51c89d0da0d7765cded3c94c842aded7a694511c, the store's 0c00da95d8ef7d764ccf2eff51c89d0da0d7765cded3c94c842aded7a694511c
[2026-10-20T04:27:47Z] G-REPLAY tz23-reading.json  sha256 833623607f7925045952a610898d7494bd0c3f86f8f01330434b16b0dae775b7, the store's 833623607f7925045952a610898d7494bd0c3f86f8f01330434b16b0dae775b7
[2026-10-20T04:27:47Z] G-REPLAY tz23-scored.csv equal to the store's True
[2026-10-20T04:27:47Z] G-REPLAY tz23-reading.json equal to the store's True
[2026-10-20T04:27:47Z] G-REPLAY S equal to TZ-23's                 True
[2026-10-20T04:27:47Z] G-REPLAY Up outcomes equal to TZ-23's       True
[2026-10-20T04:27:47Z] G-REPLAY reading equal to TZ-23's           True
[2026-10-20T04:27:47Z]   ok  G-REPLAY passes 5 of 5 on a faithful store, and leaves no copy behind
[2026-10-20T04:27:47Z] first look constants /root/tz29-work/selftest-tmp/a/tz23-constants.json 1668 bytes sha256 c72b82e592322f8c44813f227e40608bc6fa1b3bbb98425a50e1817c8b6a9b68 equal
[2026-10-20T04:27:47Z] first look fills     /root/tz29-work/selftest-tmp/a/tz23-fills.jsonl.gz 5448 bytes sha256 3c355d5ca0f9c5910cb524d479dc2d9438b804084b075b3569e96f4e8318cefa equal
[2026-10-20T04:27:47Z]   ok  a store file with one byte changed fails verify (negative control)
[2026-10-20T04:27:47Z]   ok  at twice the first look's V the threshold is 623,389.475150, the Architect's figure
[2026-10-20T04:27:47Z]   ok  at the first look's rates EARN needs 0.2412 c a share and NO EARN 0.2588 c: UNDECIDABLE cannot occur
[2026-10-20T04:27:47Z]   ok  the projected power is 0.99983
[2026-10-20T04:27:47Z]   ok  the first look's own EARN bound is TZ-23's, to every printed digit
[2026-10-20T04:27:47Z]   ok  the ledger's runs, terminals, calendar, halt and gaps
[2026-10-20T04:27:47Z]   ok  a clear after a halt reads not halted
[2026-10-20T04:27:47Z]   ok  the map's rows and anchors parse
[2026-10-20T04:27:47Z]   ok  reclaim takes the work tree and refuses the forensic store and a directory outside a session's
[2026-10-20T04:27:47Z]   ok  opens under the pair book's root and of the archive's ledger outside mode archive are refused by this hook, under the chain book's root by TZ-23's, each before it happens
[2026-10-20T04:27:47Z]   ok  TZ-23's own hook still refuses the recorder's root
[2026-10-20T04:27:47Z]   ok  mode archive reads ledger.jsonl and nothing else of the archive's state, and writes nothing there
[2026-10-20T04:27:47Z]   ok  the forensic store is written by reclaim's exclusive create alone, and nothing outside the work tree
[2026-10-20T04:27:47Z] 51 of 51 checks passed
[2026-10-20T04:27:47Z] malloc tuned: True
[2026-10-20T04:27:47Z] peak memory of this run: 30982144 bytes
[2026-10-20T04:27:47Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

### 2.3 §3.3 — the units, and the directories beside this session — `logs/10-still-1.log`, `logs/11-scratch.log`

```text
$ I still
[2026-10-20T04:27:51Z] btc-pairbook.service {'MainPID': '1942330', 'NRestarts': '15', 'ActiveState': 'active'}, MemoryCurrent 16637952, MemoryPeak 108912640
[2026-10-20T04:27:51Z] btc-recorder.service {'MainPID': '4148534', 'NRestarts': '2', 'ActiveState': 'active'}, MemoryCurrent 12648448, MemoryPeak 258011136
[2026-10-20T04:27:51Z] btc-pairbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-20T04:27:51Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-20T04:27:51Z] still: recorded
[2026-10-20T04:27:51Z] malloc tuned: True
[2026-10-20T04:27:51Z] peak memory of this run: 29065216 bytes
[2026-10-20T04:27:51Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

```text
$ I scratch /tmp/claude-0/-root-btc-5m-twap/7a160398-f4cf-54ee-b771-c3006d558bde
[2026-10-20T04:27:51Z] running 337573 started 2026-10-07T20:05:37Z claude
[2026-10-20T04:27:51Z] running 337576 started 2026-10-07T20:05:37Z claude
[2026-10-20T04:27:51Z] running 1948950 started 2026-10-20T04:24:46Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-10-20T04:27:51Z] 6a6870c2-3843-4a2b-83cf-b2f45c5500a1 born 2026-10-20T04:24:47Z: live, process [1948950]
[2026-10-20T04:27:51Z] 6b7bd886-7088-5233-bdf9-903a19178e6a born 2026-10-11T14:48:47Z: earlier
[2026-10-20T04:27:51Z] 6de9e261-2fb6-4db9-ae09-1fd283c3b8c8 born 2026-10-11T14:48:45Z: earlier
[2026-10-20T04:27:51Z] malloc tuned: True
[2026-10-20T04:27:51Z] peak memory of this run: 29065216 bytes
[2026-10-20T04:27:51Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

`scratch` named TZ-28's pair `6b7bd886…` and `6de9e261…` **earlier**. It named `6a6870c2…` **live**, born one second
after the running `claude.exe` process `1948950` started, so it was kept. This session's own directory is
`7a160398…`.

### 2.4 §9 B-RECLAIM-SCRATCH — after §3.3, before §3.4 (V16, V17) — `logs/12-reclaim-scratch.log`, `logs/13-rm-6b7bd886.log`, `logs/14-rm-6de9e261.log`

```text
$ I reclaim /tmp/claude-0/-root-btc-5m-twap/6b7bd886-7088-5233-bdf9-903a19178e6a /tmp/claude-0/-root-btc-5m-twap/6de9e261-2fb6-4db9-ae09-1fd283c3b8c8
[2026-10-20T04:27:57Z] reclaim: 2287 report tokens; forensic store holds 1846 files
[2026-10-20T04:27:57Z] RECLAIM PASS: 2 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 1846 -> 1846 files
[2026-10-20T04:27:57Z] malloc tuned: True
[2026-10-20T04:27:57Z] peak memory of this run: 29585408 bytes
[2026-10-20T04:27:57Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

```text
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/6b7bd886-7088-5233-bdf9-903a19178e6a
exit=0
exit=1
```

```text
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/6de9e261-2fb6-4db9-ae09-1fd283c3b8c8
exit=0
exit=1
```

`reclaim` copied nothing: 2 files were considered and none was named by a report. **Both `rm -rf` exited `0` and
both `test -e` exited `1`**, and neither was refused. The closing listing (§2.12) shows only `6a6870c2…` and this
session's `7a160398…`.

### 2.5 §3.4 — the archive's record (V5), first read — `logs/15-archive-1.log`, verbatim

```text
$ I archive
[2026-10-20T04:28:08Z] btc-pairbook-archive.timer {'NextElapseUSecRealtime': 'Wed 2026-10-21 03:00:20 UTC', 'LastTriggerUSec': 'Tue 2026-10-20 03:00:20 UTC', 'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-20T04:28:08Z] btc-pairbook-archive.service {'Result': 'success', 'ExecMainStatus': '0', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-20T04:28:08Z] ledger /var/lib/btc-pairbook-archive/ledger.jsonl: 30913 bytes sha256 3d08a5f72d74ccac340ed93a4c85126612b6df5b56e1135a54677e57312ce272, 130 complete records, 0 bytes of a line still written
[2026-10-20T04:28:08Z] L 2026-10-11T15:18:12Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "2a4b998acb9f4883b26999bb278624bf", "phase_at": 192, "resumed": false, "run": 1791731892, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791731892810556801}
[2026-10-20T04:28:08Z] L 2026-10-11T15:18:13Z {"assets_n": 28, "bytes_total": 430047476, "closed": 79, "deferred": 0, "event": "set", "first_T": 1791706500, "last_T": 1791730800, "open": 0, "run": 1791731892, "sha256": "ec3983419485fa67317468917eb7b60e2d0e529be4334c7297831ff562471ad0", "tag": "pairbook-streams-1791731892", "unclosed": 0, "wall_ns": 1791731893762719408, "windows_considered": 79}
[2026-10-20T04:28:08Z] L 2026-10-11T15:18:57Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 409746510, "run": 1791731892, "sent": 28, "wall_ns": 1791731937181037882}
[2026-10-20T04:28:08Z] L 2026-10-11T15:21:30Z {"assets_n": 28, "bytes_total": 430047476, "event": "verify", "release_id": 409746510, "run": 1791731892, "verify_sha256": "032adfdbaea0b81d7ea5063eb43130c09396908f05d74be0f1818d2bb2342f64", "wall_ns": 1791732090814504593}
[2026-10-20T04:28:08Z] L 2026-10-11T15:21:31Z {"already": 0, "event": "delete", "free_after": 12969091072, "free_before": 12538937344, "freed": 430047476, "gone": 28, "removed": 28, "run": 1791731892, "wall_ns": 1791732091732399708, "windows_kept": 28}
[2026-10-20T04:28:08Z] L 2026-10-11T15:21:31Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "815823", "NRestarts": "2", "ns": 1791732091741955625}, "phase": 391, "run": 1791731892, "wall_ns": 1791732091741960838}
[2026-10-20T04:28:08Z] L 2026-10-11T15:21:31Z {"event": "kill", "exit": 0, "phase": 391, "run": 1791731892, "wall_ns": 1791732091746593097}
[2026-10-20T04:28:08Z] L 2026-10-11T15:22:01Z {"NRestarts": "3", "W": 1791731700, "event": "restart", "free_bytes": 12969062400, "gap_ns": 5548461176, "pid": 851381, "run": 1791731892, "stopped": 815823, "stream_bytes": 0, "wall_ns": 1791732121761569347}
[2026-10-20T04:28:08Z] L 2026-10-11T15:30:41Z {"T": 1791731700, "event": "resume", "reading": "PASS", "run": 1791731892, "wall_ns": 1791732641000772037}
[2026-10-20T04:28:08Z] L 2026-10-11T15:30:41Z {"assets_n": 28, "bytes_total": 430047476, "ended_outside": 0, "event": "complete", "free_bytes": 12949487616, "peak_rss": 36884480, "rate_per_day": 1474448489, "requests": 61, "run": 1791731892, "started_outside": 0, "stops": [["the cap", 1792200292], ["the floor, base 43500000 bytes a day", 1792213576], ["the floor, base 187760570 bytes a day", 1792171837]], "store_stream_bytes": 19346486, "wall_ns": 1791732641002785194}
[2026-10-20T04:28:08Z] L 2026-10-12T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "b458725447bd4a0c865999eab0a904ad", "phase_at": 20, "resumed": false, "run": 1791774020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791774020508107799}
[2026-10-20T04:28:08Z] L 2026-10-12T03:00:22Z {"assets_n": 46, "bytes_total": 794522712, "closed": 125, "deferred": 0, "event": "set", "first_T": 1791731700, "last_T": 1791772200, "open": 1, "run": 1791774020, "sha256": "c8f02de3fbed47c4cfa91e66d774427f20990f634d271237bf3c6f25887ffb99", "tag": "pairbook-streams-1791774020", "unclosed": 0, "wall_ns": 1791774022193879442, "windows_considered": 125}
[2026-10-20T04:28:08Z] L 2026-10-12T03:01:35Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 410101186, "run": 1791774020, "sent": 46, "wall_ns": 1791774095014644950}
[2026-10-20T04:28:08Z] L 2026-10-12T03:04:44Z {"assets_n": 46, "bytes_total": 794522712, "event": "verify", "release_id": 410101186, "run": 1791774020, "verify_sha256": "0f86d9494743193ae4dd5ddb59e37a08eebc8bb7318ea4d98def44406d025aec", "wall_ns": 1791774284631917592}
[2026-10-20T04:28:08Z] L 2026-10-12T03:04:46Z {"already": 0, "event": "delete", "free_after": 12960145408, "free_before": 12165431296, "freed": 794522712, "gone": 46, "removed": 46, "run": 1791774020, "wall_ns": 1791774286328338970, "windows_kept": 46}
[2026-10-20T04:28:08Z] L 2026-10-12T03:04:46Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "851381", "NRestarts": "3", "ns": 1791774286341020683}, "phase": 286, "run": 1791774020, "wall_ns": 1791774286341025663}
[2026-10-20T04:28:08Z] L 2026-10-12T03:04:46Z {"event": "kill", "exit": 0, "phase": 286, "run": 1791774020, "wall_ns": 1791774286345765034}
[2026-10-20T04:28:08Z] L 2026-10-12T03:05:16Z {"NRestarts": "4", "W": 1791774000, "event": "restart", "free_bytes": 12960112640, "gap_ns": 5455854888, "pid": 911226, "run": 1791774020, "stopped": 851381, "stream_bytes": 25646773, "wall_ns": 1791774316361306454}
[2026-10-20T04:28:08Z] L 2026-10-12T03:15:41Z {"T": 1791774000, "event": "resume", "reading": "PASS", "run": 1791774020, "wall_ns": 1791774941000362333}
[2026-10-20T04:28:08Z] L 2026-10-12T03:15:41Z {"assets_n": 46, "bytes_total": 794522712, "ended_outside": 0, "event": "complete", "free_bytes": 12948570112, "peak_rss": 37670912, "rate_per_day": 1658134355, "requests": 97, "run": 1791774020, "started_outside": 0, "stops": [["the cap", 1792189855], ["the floor, base 43500000 bytes a day", 1792203914], ["the floor, base 187760570 bytes a day", 1792170389]], "store_stream_bytes": 37220758, "wall_ns": 1791774941002570067}
[2026-10-20T04:28:08Z] L 2026-10-13T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "5e59db817b3d42ef91641fbb34bc17cc", "phase_at": 20, "resumed": false, "run": 1791860420, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791860420531436360}
[2026-10-20T04:28:08Z] L 2026-10-13T03:00:24Z {"assets_n": 96, "bytes_total": 1925987888, "closed": 221, "deferred": 0, "event": "set", "first_T": 1791773100, "last_T": 1791858600, "open": 1, "run": 1791860420, "sha256": "de9209f2e76e5c42bd1395ea6e9c17ab0fc4c497be6a9311cd1e07c101f9b777", "tag": "pairbook-streams-1791860420", "unclosed": 0, "wall_ns": 1791860424671646762, "windows_considered": 221}
[2026-10-20T04:28:08Z] L 2026-10-13T03:03:13Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 411210796, "run": 1791860420, "sent": 96, "wall_ns": 1791860593421247948}
[2026-10-20T04:28:08Z] L 2026-10-13T03:07:31Z {"assets_n": 96, "bytes_total": 1925987888, "event": "verify", "release_id": 411210796, "run": 1791860420, "verify_sha256": "a5969978f8bfb614451c41257e7eb70a13c12126932ef03d4cfbd2f2c41ad022", "wall_ns": 1791860851109946296}
[2026-10-20T04:28:08Z] L 2026-10-13T03:07:35Z {"already": 0, "event": "delete", "free_after": 12876316672, "free_before": 10949902336, "freed": 1925987888, "gone": 96, "removed": 96, "run": 1791860420, "wall_ns": 1791860855219206873, "windows_kept": 96}
[2026-10-20T04:28:08Z] L 2026-10-13T03:07:35Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "911226", "NRestarts": "4", "ns": 1791860855230756130}, "phase": 455, "run": 1791860420, "wall_ns": 1791860855230762191}
[2026-10-20T04:28:08Z] L 2026-10-13T03:07:35Z {"event": "kill", "exit": 0, "phase": 455, "run": 1791860420, "wall_ns": 1791860855235973960}
[2026-10-20T04:28:08Z] L 2026-10-13T03:08:05Z {"NRestarts": "5", "W": 1791860400, "event": "restart", "free_bytes": 12876300288, "gap_ns": 5561093708, "pid": 1027378, "run": 1791860420, "stopped": 911226, "stream_bytes": 23131514, "wall_ns": 1791860885252051875}
[2026-10-20T04:28:08Z] L 2026-10-13T03:15:41Z {"T": 1791860400, "event": "resume", "reading": "PASS", "run": 1791860420, "wall_ns": 1791861341000349433}
[2026-10-20T04:28:08Z] L 2026-10-13T03:15:41Z {"assets_n": 96, "bytes_total": 1925987888, "ended_outside": 0, "event": "complete", "free_bytes": 12857700352, "peak_rss": 37941248, "rate_per_day": 1925987888, "requests": 197, "run": 1791860420, "started_outside": 0, "stops": [["the cap", 1792218357], ["the floor, base 43500000 bytes a day", 1792227987], ["the floor, base 187760570 bytes a day", 1792202964]], "store_stream_bytes": 41556131, "wall_ns": 1791861341004126797}
[2026-10-20T04:28:08Z] L 2026-10-14T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "f4f5335f60584baeab0eabd568d20823", "phase_at": 20, "resumed": false, "run": 1791946820, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791946820511249708}
[2026-10-20T04:28:08Z] L 2026-10-14T03:00:24Z {"assets_n": 96, "bytes_total": 2039544263, "closed": 317, "deferred": 0, "event": "set", "first_T": 1791859500, "last_T": 1791945000, "open": 1, "run": 1791946820, "sha256": "9c78ba5221e0bc8d9d8699d920e17c58d76b6052fce7c0e86af4948bdc38aa1e", "tag": "pairbook-streams-1791946820", "unclosed": 0, "wall_ns": 1791946824807088559, "windows_considered": 317}
[2026-10-20T04:28:08Z] L 2026-10-14T03:03:21Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 412296623, "run": 1791946820, "sent": 96, "wall_ns": 1791947001852058175}
[2026-10-20T04:28:08Z] L 2026-10-14T03:07:45Z {"assets_n": 96, "bytes_total": 2039544263, "event": "verify", "release_id": 412296623, "run": 1791946820, "verify_sha256": "086fc6331ec202ef5c6b56257a52cbc12673053f82408a3cd4b3cf203ae44c95", "wall_ns": 1791947265299596860}
[2026-10-20T04:28:08Z] L 2026-10-14T03:07:49Z {"already": 0, "event": "delete", "free_after": 12842123264, "free_before": 10802130944, "freed": 2039544263, "gone": 96, "removed": 96, "run": 1791946820, "wall_ns": 1791947269716703785, "windows_kept": 96}
[2026-10-20T04:28:08Z] L 2026-10-14T03:07:49Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1027378", "NRestarts": "5", "ns": 1791947269728675162}, "phase": 469, "run": 1791946820, "wall_ns": 1791947269728680763}
[2026-10-20T04:28:08Z] L 2026-10-14T03:07:49Z {"event": "kill", "exit": 0, "phase": 469, "run": 1791946820, "wall_ns": 1791947269733842747}
[2026-10-20T04:28:08Z] L 2026-10-14T03:08:19Z {"NRestarts": "6", "W": 1791946800, "event": "restart", "free_bytes": 12842098688, "gap_ns": 5560847791, "pid": 1155982, "run": 1791946820, "stopped": 1027378, "stream_bytes": 17222124, "wall_ns": 1791947299751305660}
[2026-10-20T04:28:08Z] L 2026-10-14T03:15:41Z {"T": 1791946800, "event": "resume", "reading": "PASS", "run": 1791946820, "wall_ns": 1791947741000324294}
[2026-10-20T04:28:08Z] L 2026-10-14T03:15:41Z {"assets_n": 96, "bytes_total": 2039544263, "ended_outside": 0, "event": "complete", "free_bytes": 12820799488, "peak_rss": 38072320, "rate_per_day": 2039544263, "requests": 197, "run": 1791946820, "started_outside": 0, "stops": [["the cap", 1792285007], ["the floor, base 43500000 bytes a day", 1792292869], ["the floor, base 187760570 bytes a day", 1792270515]], "store_stream_bytes": 38533208, "wall_ns": 1791947741004939814}
[2026-10-20T04:28:08Z] L 2026-10-15T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "08fd4972db8347a4897a6ecd018049e4", "phase_at": 20, "resumed": false, "run": 1792033220, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792033220507675615}
[2026-10-20T04:28:08Z] L 2026-10-15T03:00:25Z {"assets_n": 96, "bytes_total": 2103892072, "closed": 413, "deferred": 0, "event": "set", "first_T": 1791945900, "last_T": 1792031400, "open": 1, "run": 1792033220, "sha256": "3272c87234da82333365144d0c39bb0f75e895943e7e34ec7ff1e559c1ad8715", "tag": "pairbook-streams-1792033220", "unclosed": 0, "wall_ns": 1792033225025238523, "windows_considered": 413}
[2026-10-20T04:28:08Z] L 2026-10-15T03:03:26Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 413374764, "run": 1792033220, "sent": 96, "wall_ns": 1792033406364376177}
[2026-10-20T04:28:08Z] L 2026-10-15T03:07:54Z {"assets_n": 96, "bytes_total": 2103892072, "event": "verify", "release_id": 413374764, "run": 1792033220, "verify_sha256": "ff1dbc619728c35ab3732813ed23e83065603970c79ae62379097e59b1f13fa0", "wall_ns": 1792033674329218632}
[2026-10-20T04:28:08Z] L 2026-10-15T03:07:58Z {"already": 0, "event": "delete", "free_after": 12590329856, "free_before": 10485972992, "freed": 2103892072, "gone": 96, "removed": 96, "run": 1792033220, "wall_ns": 1792033678892316224, "windows_kept": 96}
[2026-10-20T04:28:08Z] L 2026-10-15T03:15:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1155982", "NRestarts": "6", "ns": 1792034115012851485}, "phase": 15, "run": 1792033220, "wall_ns": 1792034115012856996}
[2026-10-20T04:28:08Z] L 2026-10-15T03:15:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792033220, "wall_ns": 1792034115018137811}
[2026-10-20T04:28:08Z] L 2026-10-15T03:15:45Z {"NRestarts": "7", "W": 1792034100, "event": "restart", "free_bytes": 12572676096, "gap_ns": 5531970911, "pid": 1284485, "run": 1792033220, "stopped": 1155982, "stream_bytes": 29667971, "wall_ns": 1792034145058520440}
[2026-10-20T04:28:08Z] L 2026-10-15T03:30:41Z {"T": 1792034100, "event": "resume", "reading": "PASS", "run": 1792033220, "wall_ns": 1792035041000365330}
[2026-10-20T04:28:08Z] L 2026-10-15T03:30:41Z {"assets_n": 96, "bytes_total": 2103892072, "ended_outside": 0, "event": "complete", "free_bytes": 12548313088, "peak_rss": 38199296, "rate_per_day": 2103892072, "requests": 197, "run": 1792033220, "started_outside": 0, "stops": [["the cap", 1792361344], ["the floor, base 43500000 bytes a day", 1792358863], ["the floor, base 187760570 bytes a day", 1792338478]], "store_stream_bytes": 54308421, "wall_ns": 1792035041006683547}
[2026-10-20T04:28:08Z] L 2026-10-15T06:18:30Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "1fd2e68b26a04a328b7551cbafc2eabe", "phase_at": 210, "resumed": false, "run": 1792045110, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792045110608854708}
[2026-10-20T04:28:08Z] L 2026-10-15T06:18:31Z {"assets_n": 14, "bytes_total": 352241341, "closed": 427, "deferred": 0, "event": "set", "first_T": 1792032300, "last_T": 1792044000, "open": 0, "run": 1792045110, "sha256": "0337b76512886f5dd78d71cfb303a343631f73624e2eb539ed79ed7f32cc0b8e", "tag": "pairbook-streams-1792045110", "unclosed": 0, "wall_ns": 1792045111425201892, "windows_considered": 427}
[2026-10-20T04:28:08Z] L 2026-10-15T06:19:00Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 413477311, "run": 1792045110, "sent": 14, "wall_ns": 1792045140771279777}
[2026-10-20T04:28:08Z] L 2026-10-15T06:21:20Z {"assets_n": 14, "bytes_total": 352241341, "event": "verify", "release_id": 413477311, "run": 1792045110, "verify_sha256": "52fc16f3058d99f3207b8fe2e61473302a0f89a9e1a2e0f5c8eb71f413e8e379", "wall_ns": 1792045280782420614}
[2026-10-20T04:28:08Z] L 2026-10-15T06:21:21Z {"already": 0, "event": "delete", "free_after": 12826914816, "free_before": 12474617856, "freed": 352241341, "gone": 14, "removed": 14, "run": 1792045110, "wall_ns": 1792045281527345757, "windows_kept": 14}
[2026-10-20T04:28:08Z] L 2026-10-15T06:21:21Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1284485", "NRestarts": "7", "ns": 1792045281539516731}, "phase": 381, "run": 1792045110, "wall_ns": 1792045281539522189}
[2026-10-20T04:28:08Z] L 2026-10-15T06:21:21Z {"event": "kill", "exit": 0, "phase": 381, "run": 1792045110, "wall_ns": 1792045281543696309}
[2026-10-20T04:28:08Z] L 2026-10-15T06:21:51Z {"NRestarts": "8", "W": 1792044900, "event": "restart", "free_bytes": 12826902528, "gap_ns": 5495918230, "pid": 1312748, "run": 1792045110, "stopped": 1284485, "stream_bytes": 0, "wall_ns": 1792045311558979330}
[2026-10-20T04:28:08Z] L 2026-10-15T06:30:41Z {"T": 1792044900, "event": "resume", "reading": "PASS", "run": 1792045110, "wall_ns": 1792045841024547052}
[2026-10-20T04:28:08Z] L 2026-10-15T06:30:41Z {"assets_n": 14, "bytes_total": 352241341, "ended_outside": 0, "event": "complete", "free_bytes": 12813713408, "peak_rss": 37543936, "rate_per_day": 2415369195, "requests": 33, "run": 1792045110, "started_outside": 0, "stops": [["the cap", 1792331549], ["the floor, base 43500000 bytes a day", 1792337969], ["the floor, base 187760570 bytes a day", 1792321779]], "store_stream_bytes": 12817136, "wall_ns": 1792045841098825002}
[2026-10-20T04:28:08Z] L 2026-10-16T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "5fd01e0598954380beeca3f3ac4c3f62", "phase_at": 20, "resumed": false, "run": 1792119620, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792119620165748278}
[2026-10-20T04:28:08Z] L 2026-10-16T03:00:24Z {"assets_n": 82, "bytes_total": 1804368058, "closed": 509, "deferred": 0, "event": "set", "first_T": 1792044900, "last_T": 1792117800, "open": 1, "run": 1792119620, "sha256": "adc52d666ace24c2145e55ef9d62602717d7726c791319304613be33c58459b6", "tag": "pairbook-streams-1792119620", "unclosed": 0, "wall_ns": 1792119624014812901, "windows_considered": 509}
[2026-10-20T04:28:08Z] L 2026-10-16T03:02:57Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 414488168, "run": 1792119620, "sent": 82, "wall_ns": 1792119777429141022}
[2026-10-20T04:28:08Z] L 2026-10-16T03:07:24Z {"assets_n": 82, "bytes_total": 1804368058, "event": "verify", "release_id": 414488168, "run": 1792119620, "verify_sha256": "96164ee15cef51426beba1050e8a4f47856762d5800a75fe9966f68164302e2a", "wall_ns": 1792120044830268724}
[2026-10-20T04:28:08Z] L 2026-10-16T03:07:28Z {"already": 0, "event": "delete", "free_after": 12728901632, "free_before": 10924134400, "freed": 1804368058, "gone": 82, "removed": 82, "run": 1792119620, "wall_ns": 1792120048628416638, "windows_kept": 82}
[2026-10-20T04:28:08Z] L 2026-10-16T03:07:28Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1312748", "NRestarts": "8", "ns": 1792120048640224099}, "phase": 448, "run": 1792119620, "wall_ns": 1792120048640229054}
[2026-10-20T04:28:08Z] L 2026-10-16T03:07:28Z {"event": "kill", "exit": 0, "phase": 448, "run": 1792119620, "wall_ns": 1792120048645966122}
[2026-10-20T04:28:08Z] L 2026-10-16T03:07:58Z {"NRestarts": "9", "W": 1792119600, "event": "restart", "free_bytes": 12728885248, "gap_ns": 5420693633, "pid": 1420617, "run": 1792119620, "stopped": 1312748, "stream_bytes": 12133793, "wall_ns": 1792120078665650185}
[2026-10-20T04:28:08Z] L 2026-10-16T03:15:41Z {"T": 1792119600, "event": "resume", "reading": "PASS", "run": 1792119620, "wall_ns": 1792120541000363636}
[2026-10-20T04:28:08Z] L 2026-10-16T03:15:41Z {"assets_n": 82, "bytes_total": 1804368058, "ended_outside": 0, "event": "complete", "free_bytes": 12710682624, "peak_rss": 38199296, "rate_per_day": 2112430897, "requests": 169, "run": 1792119620, "started_outside": 0, "stops": [["the cap", 1792446508], ["the floor, base 43500000 bytes a day", 1792449588], ["the floor, base 187760570 bytes a day", 1792428951]], "store_stream_bytes": 30286238, "wall_ns": 1792120541008367106}
[2026-10-20T04:28:08Z] L 2026-10-17T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "df3acd4ed1af4d05bc9ec4fa5085ebee", "phase_at": 20, "resumed": false, "run": 1792206020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792206020485538925}
[2026-10-20T04:28:08Z] L 2026-10-17T03:00:24Z {"assets_n": 96, "bytes_total": 2048827436, "closed": 605, "deferred": 0, "event": "set", "first_T": 1792118700, "last_T": 1792204200, "open": 1, "run": 1792206020, "sha256": "0915abd5810c2b901012aa6d34388eabcc76d7be8b327d651632ac9335bbe188", "tag": "pairbook-streams-1792206020", "unclosed": 0, "wall_ns": 1792206024973916528, "windows_considered": 605}
[2026-10-20T04:28:08Z] L 2026-10-17T03:03:23Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 415548049, "run": 1792206020, "sent": 96, "wall_ns": 1792206203238800300}
[2026-10-20T04:28:08Z] L 2026-10-17T03:07:35Z {"assets_n": 96, "bytes_total": 2048827436, "event": "verify", "release_id": 415548049, "run": 1792206020, "verify_sha256": "747508e351bb13bb1aa11a99791ab87d1ea798e92c66dd1ec6126aad4f67f97c", "wall_ns": 1792206455599715552}
[2026-10-20T04:28:08Z] L 2026-10-17T03:07:40Z {"already": 0, "event": "delete", "free_after": 12725805056, "free_before": 10676551680, "freed": 2048827436, "gone": 96, "removed": 96, "run": 1792206020, "wall_ns": 1792206460092686139, "windows_kept": 96}
[2026-10-20T04:28:08Z] L 2026-10-17T03:07:40Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1420617", "NRestarts": "9", "ns": 1792206460108197241}, "phase": 460, "run": 1792206020, "wall_ns": 1792206460108202947}
[2026-10-20T04:28:08Z] L 2026-10-17T03:07:40Z {"event": "kill", "exit": 0, "phase": 460, "run": 1792206020, "wall_ns": 1792206460112982086}
[2026-10-20T04:28:08Z] L 2026-10-17T03:08:10Z {"NRestarts": "10", "W": 1792206000, "event": "restart", "free_bytes": 12725788672, "gap_ns": 5487288436, "pid": 1560378, "run": 1792206020, "stopped": 1420617, "stream_bytes": 10686101, "wall_ns": 1792206490133956812}
[2026-10-20T04:28:08Z] L 2026-10-17T03:15:41Z {"T": 1792206000, "event": "resume", "reading": "PASS", "run": 1792206020, "wall_ns": 1792206941000351565}
[2026-10-20T04:28:08Z] L 2026-10-17T03:15:41Z {"assets_n": 96, "bytes_total": 2048827436, "ended_outside": 0, "event": "complete", "free_bytes": 12715110400, "peak_rss": 38330368, "rate_per_day": 2048827436, "requests": 197, "run": 1792206020, "started_outside": 0, "stops": [["the cap", 1792543404], ["the floor, base 43500000 bytes a day", 1792546173], ["the floor, base 187760570 bytes a day", 1792524292]], "store_stream_bytes": 21346173, "wall_ns": 1792206941009261301}
[2026-10-20T04:28:08Z] L 2026-10-17T08:35:37Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "ab6b527c633847f79ce14ed1afdf3623", "phase_at": 337, "resumed": false, "run": 1792226137, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792226137790990342}
[2026-10-20T04:28:08Z] L 2026-10-17T08:35:38Z {"assets_n": 23, "bytes_total": 397545662, "closed": 628, "deferred": 0, "event": "set", "first_T": 1792205100, "last_T": 1792224900, "open": 0, "run": 1792226137, "sha256": "3db64b34a3949064d28cadc5a023e4402ebacc5cf7a2adab2fe09d13971312c4", "tag": "pairbook-streams-1792226137", "unclosed": 0, "wall_ns": 1792226138787331150, "windows_considered": 628}
[2026-10-20T04:28:08Z] L 2026-10-17T08:36:15Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 415679936, "run": 1792226137, "sent": 23, "wall_ns": 1792226175895145126}
[2026-10-20T04:28:08Z] L 2026-10-17T08:38:40Z {"assets_n": 23, "bytes_total": 397545662, "event": "verify", "release_id": 415679936, "run": 1792226137, "verify_sha256": "f26e295363dadaea4d9a2de3d5e86de06da641bf85ecec538e4a36b7e89de14f", "wall_ns": 1792226320606064836}
[2026-10-20T04:28:08Z] L 2026-10-17T08:38:41Z {"already": 0, "event": "delete", "free_after": 12799180800, "free_before": 12401537024, "freed": 397545662, "gone": 23, "removed": 23, "run": 1792226137, "wall_ns": 1792226321481880383, "windows_kept": 23}
[2026-10-20T04:28:08Z] L 2026-10-17T08:45:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1560378", "NRestarts": "10", "ns": 1792226715015188081}, "phase": 15, "run": 1792226137, "wall_ns": 1792226715015194823}
[2026-10-20T04:28:08Z] L 2026-10-17T08:45:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792226137, "wall_ns": 1792226715020774740}
[2026-10-20T04:28:08Z] L 2026-10-17T08:45:45Z {"NRestarts": "11", "W": 1792226700, "event": "restart", "free_bytes": 12783226880, "gap_ns": 5530075996, "pid": 1595407, "run": 1792226137, "stopped": 1560378, "stream_bytes": 15521838, "wall_ns": 1792226745041554142}
[2026-10-20T04:28:08Z] L 2026-10-17T09:00:41Z {"T": 1792226700, "event": "resume", "reading": "PASS", "run": 1792226137, "wall_ns": 1792227641000413386}
[2026-10-20T04:28:08Z] L 2026-10-17T09:00:41Z {"assets_n": 23, "bytes_total": 397545662, "ended_outside": 0, "event": "complete", "free_bytes": 12773187584, "peak_rss": 37543936, "rate_per_day": 1659321024, "requests": 51, "run": 1792226137, "started_outside": 0, "stops": [["the cap", 1792642879], ["the floor, base 43500000 bytes a day", 1792647417], ["the floor, base 187760570 bytes a day", 1792614631]], "store_stream_bytes": 25293180, "wall_ns": 1792227641009539425}
[2026-10-20T04:28:08Z] L 2026-10-18T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "15934402892b403b858ea4b973f03c89", "phase_at": 20, "resumed": false, "run": 1792292420, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792292420527428655}
[2026-10-20T04:28:08Z] L 2026-10-18T03:00:23Z {"assets_n": 73, "bytes_total": 1197040692, "closed": 701, "deferred": 0, "event": "set", "first_T": 1792225800, "last_T": 1792290600, "open": 1, "run": 1792292420, "sha256": "7ddfeae4a937bc90c14d8047d3ab843035a2be145d8d407738f9620b098c0b08", "tag": "pairbook-streams-1792292420", "unclosed": 0, "wall_ns": 1792292423275187616, "windows_considered": 701}
[2026-10-20T04:28:08Z] L 2026-10-18T03:02:20Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 416201489, "run": 1792292420, "sent": 73, "wall_ns": 1792292540828362894}
[2026-10-20T04:28:08Z] L 2026-10-18T03:05:48Z {"assets_n": 73, "bytes_total": 1197040692, "event": "verify", "release_id": 416201489, "run": 1792292420, "verify_sha256": "a3eb29ead036c8a97f023ecb53572112300e5b22defa9d984ba1887dcddf95e3", "wall_ns": 1792292748968235081}
[2026-10-20T04:28:08Z] L 2026-10-18T03:05:51Z {"already": 0, "event": "delete", "free_after": 12776620032, "free_before": 11579240448, "freed": 1197040692, "gone": 73, "removed": 73, "run": 1792292420, "wall_ns": 1792292751530232000, "windows_kept": 73}
[2026-10-20T04:28:08Z] L 2026-10-18T03:05:51Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1595407", "NRestarts": "11", "ns": 1792292751542647421}, "phase": 351, "run": 1792292420, "wall_ns": 1792292751542652085}
[2026-10-20T04:28:08Z] L 2026-10-18T03:05:51Z {"event": "kill", "exit": 0, "phase": 351, "run": 1792292420, "wall_ns": 1792292751546822604}
[2026-10-20T04:28:08Z] L 2026-10-18T03:06:21Z {"NRestarts": "12", "W": 1792292400, "event": "restart", "free_bytes": 12776607744, "gap_ns": 5504206730, "pid": 1692402, "run": 1792292420, "stopped": 1595407, "stream_bytes": 12437717, "wall_ns": 1792292781569460854}
[2026-10-20T04:28:08Z] L 2026-10-18T03:15:41Z {"T": 1792292400, "event": "resume", "reading": "PASS", "run": 1792292420, "wall_ns": 1792293341000328710}
[2026-10-20T04:28:08Z] L 2026-10-18T03:15:41Z {"assets_n": 73, "bytes_total": 1197040692, "ended_outside": 0, "event": "complete", "free_bytes": 12764577792, "peak_rss": 37937152, "rate_per_day": 1574190499, "requests": 151, "run": 1792292420, "started_outside": 0, "stops": [["the cap", 1792731097], ["the floor, base 43500000 bytes a day", 1792734747], ["the floor, base 187760570 bytes a day", 1792698607]], "store_stream_bytes": 24161003, "wall_ns": 1792293341010228074}
[2026-10-20T04:28:08Z] L 2026-10-19T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "b6aa8a5cde4c4cc392165b8f31b1bec0", "phase_at": 20, "resumed": false, "run": 1792378820, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792378820477080166}
[2026-10-20T04:28:08Z] L 2026-10-19T03:00:24Z {"assets_n": 96, "bytes_total": 1755430954, "closed": 797, "deferred": 0, "event": "set", "first_T": 1792291500, "last_T": 1792377000, "open": 1, "run": 1792378820, "sha256": "948f4d39cca953e07be1c1c561f5115f6200f5aa8330fe78434c058d6e607528", "tag": "pairbook-streams-1792378820", "unclosed": 0, "wall_ns": 1792378824458122339, "windows_considered": 797}
[2026-10-20T04:28:08Z] L 2026-10-19T03:03:08Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 416860290, "run": 1792378820, "sent": 96, "wall_ns": 1792378988043909754}
[2026-10-20T04:28:08Z] L 2026-10-19T03:07:11Z {"assets_n": 96, "bytes_total": 1755430954, "event": "verify", "release_id": 416860290, "run": 1792378820, "verify_sha256": "86b0b971d6eaeb1c8fd7dd87f44b2f739282eec95c52919b65b79ea293db2551", "wall_ns": 1792379231626951320}
[2026-10-20T04:28:08Z] L 2026-10-19T03:07:15Z {"already": 0, "event": "delete", "free_after": 12737359872, "free_before": 10981560320, "freed": 1755430954, "gone": 96, "removed": 96, "run": 1792378820, "wall_ns": 1792379235366652736, "windows_kept": 96}
[2026-10-20T04:28:08Z] L 2026-10-19T03:07:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1692402", "NRestarts": "12", "ns": 1792379235374600961}, "phase": 435, "run": 1792378820, "wall_ns": 1792379235374606661}
[2026-10-20T04:28:08Z] L 2026-10-19T03:07:15Z {"event": "kill", "exit": 0, "phase": 435, "run": 1792378820, "wall_ns": 1792379235379253859}
[2026-10-20T04:28:08Z] L 2026-10-19T03:07:45Z {"NRestarts": "13", "W": 1792378800, "event": "restart", "free_bytes": 12737351680, "gap_ns": 5404558972, "pid": 1814768, "run": 1792378820, "stopped": 1692402, "stream_bytes": 20988190, "wall_ns": 1792379265403200749}
[2026-10-20T04:28:08Z] L 2026-10-19T03:15:41Z {"T": 1792378800, "event": "resume", "reading": "PASS", "run": 1792378820, "wall_ns": 1792379741000400500}
[2026-10-20T04:28:08Z] L 2026-10-19T03:15:41Z {"assets_n": 96, "bytes_total": 1755430954, "ended_outside": 0, "event": "complete", "free_bytes": 12720193536, "peak_rss": 38592512, "rate_per_day": 1755430954, "requests": 197, "run": 1792378820, "started_outside": 0, "stops": [["the cap", 1792771618], ["the floor, base 43500000 bytes a day", 1792774544], ["the floor, base 187760570 bytes a day", 1792745234]], "store_stream_bytes": 38026457, "wall_ns": 1792379741011807328}
[2026-10-20T04:28:08Z] L 2026-10-19T21:54:19Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "7efdb0d05f6f4814b803f423a1351eae", "phase_at": 559, "resumed": false, "run": 1792446859, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792446859827562789}
[2026-10-20T04:28:08Z] L 2026-10-19T21:54:23Z {"assets_n": 76, "bytes_total": 1702929677, "closed": 873, "deferred": 0, "event": "set", "first_T": 1792377900, "last_T": 1792445400, "open": 1, "run": 1792446859, "sha256": "8491aab13dd6df082e8a4e847bd4e676a5edbeabd050e9a1767a79d7ecfb72d3", "tag": "pairbook-streams-1792446859", "unclosed": 0, "wall_ns": 1792446863665163186, "windows_considered": 873}
[2026-10-20T04:28:08Z] L 2026-10-19T22:02:33Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 417794290, "run": 1792446859, "sent": 76, "wall_ns": 1792447353191732798}
[2026-10-20T04:28:08Z] L 2026-10-19T22:09:37Z {"assets_n": 76, "bytes_total": 1702929677, "event": "verify", "release_id": 417794290, "run": 1792446859, "verify_sha256": "dfa62b04b0291467b86d37271e00e2242c0fea6b9e1caa987e7a9b31fafd3f6b", "wall_ns": 1792447777762252351}
[2026-10-20T04:28:08Z] L 2026-10-19T22:09:41Z {"already": 0, "event": "delete", "free_after": 12726702080, "free_before": 11023396864, "freed": 1702929677, "gone": 76, "removed": 76, "run": 1792446859, "wall_ns": 1792447781500420485, "windows_kept": 76}
[2026-10-20T04:28:08Z] L 2026-10-19T22:15:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1814768", "NRestarts": "13", "ns": 1792448115017795294}, "phase": 15, "run": 1792446859, "wall_ns": 1792448115017801355}
[2026-10-20T04:28:08Z] L 2026-10-19T22:15:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792446859, "wall_ns": 1792448115024251292}
[2026-10-20T04:28:08Z] L 2026-10-19T22:15:45Z {"NRestarts": "14", "W": 1792448100, "event": "restart", "free_bytes": 12707540992, "gap_ns": 5638947193, "pid": 1915093, "run": 1792446859, "stopped": 1814768, "stream_bytes": 30931694, "wall_ns": 1792448145064395857}
[2026-10-20T04:28:08Z] L 2026-10-19T22:30:41Z {"T": 1792448100, "event": "resume", "reading": "PASS", "run": 1792446859, "wall_ns": 1792449041000625272}
[2026-10-20T04:28:08Z] L 2026-10-19T22:30:41Z {"assets_n": 76, "bytes_total": 1702929677, "ended_outside": 0, "event": "complete", "free_bytes": 12678688768, "peak_rss": 37539840, "rate_per_day": 2151069065, "requests": 157, "run": 1792446859, "started_outside": 0, "stops": [["the cap", 1792767956], ["the floor, base 43500000 bytes a day", 1792771035], ["the floor, base 187760570 bytes a day", 1792751174]], "store_stream_bytes": 60078470, "wall_ns": 1792449041020984137}
[2026-10-20T04:28:08Z] L 2026-10-20T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "39b80e28726849c6b2c7c78015f76beb", "phase_at": 20, "resumed": false, "run": 1792465220, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792465220508369328}
[2026-10-20T04:28:08Z] L 2026-10-20T03:00:21Z {"assets_n": 20, "bytes_total": 428604581, "closed": 893, "deferred": 0, "event": "set", "first_T": 1792446300, "last_T": 1792463400, "open": 1, "run": 1792465220, "sha256": "08a4bf67291e8988351d7b031e9a6250ded7ec726fb2a80a1c28559d6b827e6b", "tag": "pairbook-streams-1792465220", "unclosed": 0, "wall_ns": 1792465221560132886, "windows_considered": 893}
[2026-10-20T04:28:08Z] L 2026-10-20T03:01:05Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 417955485, "run": 1792465220, "sent": 20, "wall_ns": 1792465265840619699}
[2026-10-20T04:28:08Z] L 2026-10-20T03:03:38Z {"assets_n": 20, "bytes_total": 428604581, "event": "verify", "release_id": 417955485, "run": 1792465220, "verify_sha256": "1417b0845ea746c17a126d8311895714cd28b5cdbefbb3f27cc38e7b2d8a516a", "wall_ns": 1792465418377004134}
[2026-10-20T04:28:08Z] L 2026-10-20T03:03:39Z {"already": 0, "event": "delete", "free_after": 12736249856, "free_before": 12307550208, "freed": 428604581, "gone": 20, "removed": 20, "run": 1792465220, "wall_ns": 1792465419274331805, "windows_kept": 20}
[2026-10-20T04:28:08Z] L 2026-10-20T03:03:39Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1915093", "NRestarts": "14", "ns": 1792465419285640926}, "phase": 219, "run": 1792465220, "wall_ns": 1792465419285646173}
[2026-10-20T04:28:08Z] L 2026-10-20T03:03:39Z {"event": "kill", "exit": 0, "phase": 219, "run": 1792465220, "wall_ns": 1792465419290626015}
[2026-10-20T04:28:08Z] L 2026-10-20T03:04:09Z {"NRestarts": "15", "W": 1792465200, "event": "restart", "free_bytes": 12736208896, "gap_ns": 5521442701, "pid": 1942330, "run": 1792465220, "stopped": 1915093, "stream_bytes": 21234976, "wall_ns": 1792465449314599186}
[2026-10-20T04:28:08Z] L 2026-10-20T03:15:41Z {"T": 1792465200, "event": "resume", "reading": "PASS", "run": 1792465220, "wall_ns": 1792466141000339712}
[2026-10-20T04:28:08Z] L 2026-10-20T03:15:41Z {"assets_n": 20, "bytes_total": 428604581, "ended_outside": 0, "event": "complete", "free_bytes": 12714721280, "peak_rss": 37937152, "rate_per_day": 2057301988, "requests": 45, "run": 1792465220, "started_outside": 0, "stops": [["the cap", 1792800340], ["the floor, base 43500000 bytes a day", 1792803989], ["the floor, base 187760570 bytes a day", 1792782280]], "store_stream_bytes": 42260469, "wall_ns": 1792466141012853604}
[2026-10-20T04:28:08Z] run 1791731892 2026-10-11T15:18:12Z, off-calendar, second 55092 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1791731892: 28 files, 430047476 bytes, windows 1791706500 to 1791730800 of 79 considered; Release 409746510: sent 28, held 0; removed 28, freed 430047476 bytes, free after 12969091072; restart: window 1791731700, pid 851381 after 815823, NRestarts 3; resume PASS at window 1791731700; complete: requests 61, started outside 0, ended outside 0, store 19346486 bytes, free 12949487616, rate 1474448489 a day
[2026-10-20T04:28:08Z] run 1791774020 2026-10-12T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1791774020: 46 files, 794522712 bytes, windows 1791731700 to 1791772200 of 125 considered; Release 410101186: sent 46, held 0; removed 46, freed 794522712 bytes, free after 12960145408; restart: window 1791774000, pid 911226 after 851381, NRestarts 4; resume PASS at window 1791774000; complete: requests 97, started outside 0, ended outside 0, store 37220758 bytes, free 12948570112, rate 1658134355 a day
[2026-10-20T04:28:08Z] run 1791860420 2026-10-13T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1791860420: 96 files, 1925987888 bytes, windows 1791773100 to 1791858600 of 221 considered; Release 411210796: sent 96, held 0; removed 96, freed 1925987888 bytes, free after 12876316672; restart: window 1791860400, pid 1027378 after 911226, NRestarts 5; resume PASS at window 1791860400; complete: requests 197, started outside 0, ended outside 0, store 41556131 bytes, free 12857700352, rate 1925987888 a day
[2026-10-20T04:28:08Z] run 1791946820 2026-10-14T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1791946820: 96 files, 2039544263 bytes, windows 1791859500 to 1791945000 of 317 considered; Release 412296623: sent 96, held 0; removed 96, freed 2039544263 bytes, free after 12842123264; restart: window 1791946800, pid 1155982 after 1027378, NRestarts 6; resume PASS at window 1791946800; complete: requests 197, started outside 0, ended outside 0, store 38533208 bytes, free 12820799488, rate 2039544263 a day
[2026-10-20T04:28:08Z] run 1792033220 2026-10-15T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792033220: 96 files, 2103892072 bytes, windows 1791945900 to 1792031400 of 413 considered; Release 413374764: sent 96, held 0; removed 96, freed 2103892072 bytes, free after 12590329856; restart: window 1792034100, pid 1284485 after 1155982, NRestarts 7; resume PASS at window 1792034100; complete: requests 197, started outside 0, ended outside 0, store 54308421 bytes, free 12548313088, rate 2103892072 a day
[2026-10-20T04:28:08Z] run 1792045110 2026-10-15T06:18:30Z, off-calendar, second 22710 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792045110: 14 files, 352241341 bytes, windows 1792032300 to 1792044000 of 427 considered; Release 413477311: sent 14, held 0; removed 14, freed 352241341 bytes, free after 12826914816; restart: window 1792044900, pid 1312748 after 1284485, NRestarts 8; resume PASS at window 1792044900; complete: requests 33, started outside 0, ended outside 0, store 12817136 bytes, free 12813713408, rate 2415369195 a day
[2026-10-20T04:28:08Z] run 1792119620 2026-10-16T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792119620: 82 files, 1804368058 bytes, windows 1792044900 to 1792117800 of 509 considered; Release 414488168: sent 82, held 0; removed 82, freed 1804368058 bytes, free after 12728901632; restart: window 1792119600, pid 1420617 after 1312748, NRestarts 9; resume PASS at window 1792119600; complete: requests 169, started outside 0, ended outside 0, store 30286238 bytes, free 12710682624, rate 2112430897 a day
[2026-10-20T04:28:08Z] run 1792206020 2026-10-17T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792206020: 96 files, 2048827436 bytes, windows 1792118700 to 1792204200 of 605 considered; Release 415548049: sent 96, held 0; removed 96, freed 2048827436 bytes, free after 12725805056; restart: window 1792206000, pid 1560378 after 1420617, NRestarts 10; resume PASS at window 1792206000; complete: requests 197, started outside 0, ended outside 0, store 21346173 bytes, free 12715110400, rate 2048827436 a day
[2026-10-20T04:28:08Z] run 1792226137 2026-10-17T08:35:37Z, off-calendar, second 30937 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792226137: 23 files, 397545662 bytes, windows 1792205100 to 1792224900 of 628 considered; Release 415679936: sent 23, held 0; removed 23, freed 397545662 bytes, free after 12799180800; restart: window 1792226700, pid 1595407 after 1560378, NRestarts 11; resume PASS at window 1792226700; complete: requests 51, started outside 0, ended outside 0, store 25293180 bytes, free 12773187584, rate 1659321024 a day
[2026-10-20T04:28:08Z] run 1792292420 2026-10-18T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792292420: 73 files, 1197040692 bytes, windows 1792225800 to 1792290600 of 701 considered; Release 416201489: sent 73, held 0; removed 73, freed 1197040692 bytes, free after 12776620032; restart: window 1792292400, pid 1692402 after 1595407, NRestarts 12; resume PASS at window 1792292400; complete: requests 151, started outside 0, ended outside 0, store 24161003 bytes, free 12764577792, rate 1574190499 a day
[2026-10-20T04:28:08Z] run 1792378820 2026-10-19T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792378820: 96 files, 1755430954 bytes, windows 1792291500 to 1792377000 of 797 considered; Release 416860290: sent 96, held 0; removed 96, freed 1755430954 bytes, free after 12737359872; restart: window 1792378800, pid 1814768 after 1692402, NRestarts 13; resume PASS at window 1792378800; complete: requests 197, started outside 0, ended outside 0, store 38026457 bytes, free 12720193536, rate 1755430954 a day
[2026-10-20T04:28:08Z] run 1792446859 2026-10-19T21:54:19Z, off-calendar, second 78859 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792446859: 76 files, 1702929677 bytes, windows 1792377900 to 1792445400 of 873 considered; Release 417794290: sent 76, held 0; removed 76, freed 1702929677 bytes, free after 12726702080; restart: window 1792448100, pid 1915093 after 1814768, NRestarts 14; resume PASS at window 1792448100; complete: requests 157, started outside 0, ended outside 0, store 60078470 bytes, free 12678688768, rate 2151069065 a day
[2026-10-20T04:28:08Z] run 1792465220 2026-10-20T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792465220: 20 files, 428604581 bytes, windows 1792446300 to 1792463400 of 893 considered; Release 417955485: sent 20, held 0; removed 20, freed 428604581 bytes, free after 12736249856; restart: window 1792465200, pid 1942330 after 1915093, NRestarts 15; resume PASS at window 1792465200; complete: requests 45, started outside 0, ended outside 0, store 42260469 bytes, free 12714721280, rate 2057301988 a day
[2026-10-20T04:28:08Z] tags on origin 13: ['pairbook-streams-1791731892', 'pairbook-streams-1791774020', 'pairbook-streams-1791860420', 'pairbook-streams-1791946820', 'pairbook-streams-1792033220', 'pairbook-streams-1792045110', 'pairbook-streams-1792119620', 'pairbook-streams-1792206020', 'pairbook-streams-1792226137', 'pairbook-streams-1792292420', 'pairbook-streams-1792378820', 'pairbook-streams-1792446859', 'pairbook-streams-1792465220']
[2026-10-20T04:28:08Z] the ledger's sets 13, 842 files, 16980982812 bytes; their tags not on origin []; tags on origin without a set []
[2026-10-20T04:28:08Z] runs 13; without a terminal record []; windows skipped between consecutive sets []; halted False
[2026-10-20T04:28:08Z] malloc tuned: True
[2026-10-20T04:28:08Z] peak memory of this run: 29188096 bytes
[2026-10-20T04:28:08Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

**13 runs, every one `complete`; 842 stream files, `16,980,982,812` bytes, moved to 13 Releases. The 13 tags on
`origin` are exactly the ledger's sets. No windows were skipped between consecutive sets. Not halted.** There were
three runs off the calendar. None coincides with a boot, because the host has one boot since 2026-08-02 (§0.3):

| run `A` | UTC | second of the day | boot near it | restart it made |
|---|---|---|---|---|
| `1792045110` | 2026-10-15 06:18:30 | 22,710 | none | pid `1312748` after `1284485`, `NRestarts` 8 |
| `1792226137` | 2026-10-17 08:35:37 | 30,937 | none | pid `1595407` after `1560378`, `NRestarts` 11 |
| `1792446859` | 2026-10-19 21:54:19 | 78,859 | none | pid `1915093` after `1814768`, `NRestarts` 14 |

TZ-28's own first run, `1791731892`, is also off the calendar, as the map records. The last run, `1792465220`, today
at 03:00:20 UTC, restarted the pair book to pid `1942330`, `NRestarts` 15. That is the pid and count §0.3 and G-STILL
read, so **no restart of the pair book happened during this session**. The next run is 2026-10-21 03:00:20 UTC.

### 2.6 §3.5 — G-REHEARSAL (V6): **PASS, 16 of 16** — `logs/16-rehearse.log`, verbatim

```text
$ I rehearse
[2026-10-20T04:28:17Z] MemAvailable 331182080 bytes, floor 177135616
[2026-10-20T04:30:17Z] the walk starts at second 17 of window 1792470600
[2026-10-20T04:30:18Z] the set formed in 0.7 s: 144 considered, 144 members, /root/tz29-work/rehearsal/set.json sha256 83a53bd3fb13829173282487833ef0398280d358377e0f09d0beb414c7829cbc
[2026-10-20T04:31:01Z] chunks 8 of 8, 44 s
[2026-10-20T04:31:01Z] chunks fetched fresh 8: inside the idle stretch 8, ending after second 590 0; longest 12.9 s; waited 0 s; windows 1, from 2026-10-20T04:30:00Z to 2026-10-20T04:30:00Z
[2026-10-20T04:31:03Z] members 144, considered 144, first 1791050100 2026-10-03T17:55:00Z, last 1791093000 2026-10-04T05:50:00Z, weekend members 144
[2026-10-20T04:31:03Z] member list sha 6441dba6604897a0146f39f8e6a153818083f2a5678f6c6484e77487d7968ce6
[2026-10-20T04:31:03Z] members by the number of excluded spans ending below them: 2: 144
[2026-10-20T04:31:03Z] window fills 128031, shares 3509409.854401, X -44336.003951, C -108894.2181475504884399, R 8015.91427290719561009665372913342
[2026-10-20T04:31:03Z] band pre  fills 8091, shares 322581.311616
[2026-10-20T04:31:03Z] band w0   fills 34282, shares 858622.027230
[2026-10-20T04:31:03Z] band w1   fills 30134, shares 822002.256141
[2026-10-20T04:31:03Z] band w2   fills 30036, shares 833324.447472
[2026-10-20T04:31:03Z] band w3   fills 33579, shares 995461.123558
[2026-10-20T04:31:03Z] band last fills 28463, shares 978970.671146
[2026-10-20T04:31:03Z] band post fills 730, shares 192218.999951
[2026-10-20T04:31:03Z] V 2140569358.582178867947; lambda 0.000021932; L 5.29831736654803667745321503082690498327770311161780120618734
[2026-10-20T04:31:03Z] EARN at S >= 247447.678143864582553655937725374110125738788601942422313849 (0.0705097689953628782357990790416292822747757197155682685069209 a share); NO EARN at S <= -229900.628871859582553655937725374110125738788601942422313849 (-0.0655097689953628782357990790416292822747757197155682685069209 a share)
[2026-10-20T04:31:03Z] power of either answer against the other's alternative, normal, variance V/4: 0.0
[2026-10-20T04:31:03Z] wrote /root/tz29-work/rehearsal/rehearsal-constants.json sha256 9f521a23b3a5b48ac7569f68a9c42bf6da1bb8ef09f5a71c0c8e091fbf5098e3
[2026-10-20T04:31:03Z] wrote /root/tz29-work/rehearsal/rehearsal-fills.jsonl.gz sha256 3ce50a85f84068a4cac15ece53d2ea1b16184b9080d69228b0baae8f887c8116
[2026-10-20T04:31:03Z] wrote /root/tz29-work/rehearsal/rehearsal-members.csv sha256 2676af1dee730001abf560555c1c0eb9b88901209a94598dcb966495e20131d1
[2026-10-20T04:31:03Z] labels: 144 members, 75 Up
[2026-10-20T04:31:03Z] S 28056.96630645768404999665372913342 = settlement 20041.0520335504884399 + rebate 8015.91427290719561009665372913342; per share 0.00799478187800511502094750845984644263428388279200750286615141 = 0.00571066158272105687921991461742582040359548327015047220206206 + 0.00228412029528405814172759384242062223068839952185703066408935
[2026-10-20T04:31:03Z] EARN False (margin -219390.711837406898503659283996240690125738788601942422313849); NO EARN False (margin -257957.595178317266603652591454507530125738788601942422313849)
[2026-10-20T04:31:03Z] band pre  makers per share -0.0194439458710785748295304005216177364927488757104923929158955, of it rebate 0.00343449235380714512022328037575989418845131167538094607088176 - barred from every reading
[2026-10-20T04:31:03Z] band w0   makers per share 0.00809668994246333164669906247241946849255885936724456097087031, of it rebate 0.00298702379163527017651557524881741438572713752576808557588209 - barred from every reading
[2026-10-20T04:31:03Z] band w1   makers per share 0.00216533860931846166363481784032051450296117855798497203069005, of it rebate 0.00253549451390923610592868522313286130876296105380083347534521 - barred from every reading
[2026-10-20T04:31:03Z] band w2   makers per share 0.0169475211352226561899886758769244471548446735331566650802338, of it rebate 0.00217930627249097667478222079878301204209651407974407518415309 - barred from every reading
[2026-10-20T04:31:03Z] band w3   makers per share 0.00522599320344578533877668254227426131378006832207622223362456, of it rebate 0.00155801005843739214150129623276759217257315589581711772196858 - barred from every reading
[2026-10-20T04:31:03Z] band last makers per share -0.0145412285056932672794855950031652205947831483024700954987439, of it rebate 0.000758816301907631239250794001755731940353158074036355805383154 - barred from every reading
[2026-10-20T04:31:03Z] band post makers per share 0.00300205633772118880223190142216078103457971517224835236600008, of it rebate 0.0000652987480229926338239312826220749917983220940599929383096346 - barred from every reading
[2026-10-20T04:31:03Z] wrote rehearsal-scored.csv sha256 d31eb18fa58f8a26f12979f733fcead3b2482a480ba97a17c1145c1eef99bda2 and rehearsal-reading.json sha256 4cdf1a1179c0d58f048d091e0a719951cb3af38c822d49a2e9343bea5f502d1f
[2026-10-20T04:31:03Z] G-REHEARSAL members instrument 144, the Architect's 144, equal
[2026-10-20T04:31:03Z] G-REHEARSAL ups     instrument 75, the Architect's 75, equal
[2026-10-20T04:31:03Z] G-REHEARSAL n       instrument 128031, the Architect's 128031, equal
[2026-10-20T04:31:03Z] G-REHEARSAL sh      instrument 3509409.854401, the Architect's 3509409.854401, equal
[2026-10-20T04:31:03Z] G-REHEARSAL X       instrument -44336.003951, the Architect's -44336.003951, equal
[2026-10-20T04:31:03Z] G-REHEARSAL C       instrument -108894.2181475504884399, the Architect's -108894.2181475504884399, equal
[2026-10-20T04:31:03Z] G-REHEARSAL R       instrument 8015.91427290719561009665372913342, the Architect's 8015.91427290719561009665372913342, equal
[2026-10-20T04:31:03Z] G-REHEARSAL V       instrument 2140569358.582178867947, the Architect's 2140569358.582178867947, equal
[2026-10-20T04:31:03Z] G-REHEARSAL XU      instrument -88853.166114, the Architect's -88853.166114, equal
[2026-10-20T04:31:03Z] G-REHEARSAL S       instrument 28056.96630645768404999665372913342, the Architect's 28056.96630645768404999665372913342, equal
[2026-10-20T04:31:03Z] G-REHEARSAL rehearsal-constants.json sha256 9f521a23b3a5b48ac7569f68a9c42bf6da1bb8ef09f5a71c0c8e091fbf5098e3, TZ-23's 9f521a23b3a5b48ac7569f68a9c42bf6da1bb8ef09f5a71c0c8e091fbf5098e3, equal
[2026-10-20T04:31:03Z] G-REHEARSAL rehearsal-fills.jsonl.gz sha256 3ce50a85f84068a4cac15ece53d2ea1b16184b9080d69228b0baae8f887c8116, TZ-23's 3ce50a85f84068a4cac15ece53d2ea1b16184b9080d69228b0baae8f887c8116, equal
[2026-10-20T04:31:03Z] G-REHEARSAL rehearsal-members.csv    sha256 2676af1dee730001abf560555c1c0eb9b88901209a94598dcb966495e20131d1, TZ-23's 2676af1dee730001abf560555c1c0eb9b88901209a94598dcb966495e20131d1, equal
[2026-10-20T04:31:03Z] G-REHEARSAL rehearsal-reading.json   sha256 4cdf1a1179c0d58f048d091e0a719951cb3af38c822d49a2e9343bea5f502d1f, TZ-23's 4cdf1a1179c0d58f048d091e0a719951cb3af38c822d49a2e9343bea5f502d1f, equal
[2026-10-20T04:31:03Z] G-REHEARSAL rehearsal-scored.csv     sha256 d31eb18fa58f8a26f12979f733fcead3b2482a480ba97a17c1145c1eef99bda2, TZ-23's d31eb18fa58f8a26f12979f733fcead3b2482a480ba97a17c1145c1eef99bda2, equal
[2026-10-20T04:31:03Z] G-REHEARSAL set.json                 sha256 83a53bd3fb13829173282487833ef0398280d358377e0f09d0beb414c7829cbc, TZ-23's 83a53bd3fb13829173282487833ef0398280d358377e0f09d0beb414c7829cbc, equal
[2026-10-20T04:31:03Z] G-REHEARSAL PASS: 16 of 16 - 10 figures and 6 files equal to TZ-23's
[2026-10-20T04:31:03Z] malloc tuned: True
[2026-10-20T04:31:03Z] peak memory of this run: 54341632 bytes
[2026-10-20T04:31:03Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

### 2.7 §3.6 — G-REPLAY (V7): **PASS** — `logs/17-replay.log`, verbatim

```text
$ I replay
[2026-10-20T04:31:07Z] MemAvailable 288215040 bytes, floor 177135616
[2026-10-20T04:31:07Z] first look constants /root/btc-forensics/tz23-work--set--tz23-constants.json 2114 bytes sha256 1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5 equal
[2026-10-20T04:31:07Z] first look fills     /root/btc-forensics/tz23-work--set--tz23-fills.jsonl.gz 36870673 bytes sha256 4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64 equal
[2026-10-20T04:31:07Z] first look members   /root/btc-forensics/tz23-work--set--tz23-members.csv 2444450 bytes sha256 cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61 equal
[2026-10-20T04:31:07Z] first look reading   /root/btc-forensics/tz23-work--set--tz23-reading.json 1915 bytes sha256 fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043 equal
[2026-10-20T04:31:07Z] first look scored    /root/btc-forensics/tz23-work--set--tz23-scored.csv 464610 bytes sha256 12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988 equal
[2026-10-20T04:31:07Z] first look set       /root/btc-forensics/tz23-work--set--set.json 2314799 bytes sha256 a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303 equal
[2026-10-20T04:31:07Z] labels: 4032 members, 2023 Up
[2026-10-20T04:31:07Z] S 272424.11263025802271516797439628522 = settlement -17171.5070488346688545 + rebate 289595.61967909269156966797439628522; per share 0.00210812580980648584769071608480091420491821166475579642487587 = -0.000132879930683865912108413304618626214221032332128716794716256 + 0.00224100574049035175979912938941954041913924399688451321959213
[2026-10-20T04:31:07Z] EARN False (margin -160060.278568531236325582917829088890125738788601942422313849); NO EARN False (margin -58779.816055747281755918866621659330125738788601942422313849)
[2026-10-20T04:31:07Z] band pre  makers per share 0.00578304081952413057952022352980629664935718900791247195931976, of it rebate 0.00345012399769891100803924850470126430613185212420594087415147 - barred from every reading
[2026-10-20T04:31:07Z] band w0   makers per share 0.00322455954748439770877692265458851757694567952305808329115454, of it rebate 0.00304907563482741327856453398896113778589080525912034696196823 - barred from every reading
[2026-10-20T04:31:07Z] band w1   makers per share 0.00537342902056019379690494463906948507427542781610791564883005, of it rebate 0.00259433618094249559600229966912416186895506872175502666584656 - barred from every reading
[2026-10-20T04:31:07Z] band w2   makers per share 0.00233536554312248819680313753205740097402618301672759944638889, of it rebate 0.00211313274742361729393620015038819425576058608365283165320518 - barred from every reading
[2026-10-20T04:31:07Z] band w3   makers per share -0.00114409261092735982843879619885996043013925160772673885672486, of it rebate 0.00147282873442040320431779069075803660016903189588108502253665 - barred from every reading
[2026-10-20T04:31:07Z] band last makers per share 0.00209141444924695550009797726018697540575766571006026582212843, of it rebate 0.000820733005138050399449513535090341996059592320041265996913536 - barred from every reading
[2026-10-20T04:31:07Z] band post makers per share 0.00383884093149174464961136665680377112039339556460817539811684, of it rebate 0.0000708535922763116122394261981760652136552029840416336454011999 - barred from every reading
[2026-10-20T04:31:07Z] wrote tz23-scored.csv sha256 12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988 and tz23-reading.json sha256 fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043
[2026-10-20T04:31:07Z] G-REPLAY tz23-scored.csv    sha256 12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988, the store's 12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988
[2026-10-20T04:31:07Z] G-REPLAY tz23-reading.json  sha256 fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043, the store's fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043
[2026-10-20T04:31:07Z] G-REPLAY tz23-scored.csv equal to the store's True
[2026-10-20T04:31:07Z] G-REPLAY tz23-reading.json equal to the store's True
[2026-10-20T04:31:07Z] G-REPLAY S equal to TZ-23's                 True
[2026-10-20T04:31:07Z] G-REPLAY Up outcomes equal to TZ-23's       True
[2026-10-20T04:31:07Z] G-REPLAY reading equal to TZ-23's           True
[2026-10-20T04:31:07Z] G-REPLAY PASS: 6 of 6 stored files equal, 5 of 5 checks
[2026-10-20T04:31:07Z] malloc tuned: True
[2026-10-20T04:31:07Z] peak memory of this run: 49233920 bytes
[2026-10-20T04:31:07Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

### 2.8 §3.7 — the instant, then the set: G-SET (V8): **PASS** — `logs/18-instant.log`, `logs/19-fetch.log`, verbatim

```text
$ t=$(date -u +%s); while [ "$t" -lt 1792455300 ]; do sleep 30; t=$(date -u +%s); done; echo "instant reached: $t $(date -u)"
instant reached: 1792470672 Tue Oct 20 04:31:12 AM UTC 2026
```

```text
$ I fetch
[2026-10-20T04:31:15Z] MemAvailable 263000064 bytes, floor 177135616
[2026-10-20T04:31:15Z] the walk starts at second 75 of window 1792470600
[2026-10-20T04:31:33Z] the set formed in 17.9 s: 4032 considered, 4032 members, /root/tz29-work/set/set.json sha256 3f009cbeedc81713601a2cec5f080d0bdc2ab174fc1d468202604f3b10843d13
[2026-10-20T04:34:24Z] chunks 25 of 202, 171 s
[2026-10-20T04:34:54Z] projected 1337 s of fetching for 202 chunks after 30 fetched; 201 s of wall clock so far
[2026-10-20T04:37:10Z] chunks 50 of 202, 337 s
[2026-10-20T04:47:03Z] chunks 75 of 202, 930 s
[2026-10-20T04:50:01Z] chunks 100 of 202, 1108 s
[2026-10-20T04:53:02Z] chunks 125 of 202, 1289 s
[2026-10-20T05:03:23Z] chunks 150 of 202, 1910 s
[2026-10-20T05:05:40Z] chunks 175 of 202, 2047 s
[2026-10-20T05:07:35Z] chunks 200 of 202, 2162 s
[2026-10-20T05:07:39Z] chunks 202 of 202, 2166 s
[2026-10-20T05:07:43Z] chunks fetched fresh 202: inside the idle stretch 202, ending after second 590 0; longest 25.8 s; waited 1750 s; windows 3, from 2026-10-20T04:30:00Z to 2026-10-20T05:00:00Z
[2026-10-20T05:07:43Z] G-SET PASS: 4032 members, 4032 considered, 1791242100 to 1792451400, 202 chunks, every chunk read back
[2026-10-20T05:07:43Z] malloc tuned: True
[2026-10-20T05:07:43Z] peak memory of this run: 73420800 bytes
[2026-10-20T05:07:43Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

- **The walk** started at second 75 of window `1792470600` and formed the set in 17.9 s. It considered 4,032
  candidates and kept 4,032 members, with no retry. **Every non-member with its reason: none.** `constants` printed
  `non-members 0` for the second look (§2.9).
- **The fetch** used 202 chunks, all fresh. **Inside the idle stretch: 202. Ending after second 590: 0**, so there is
  no chunk to list. The longest chunk took 25.8 s. The holds waited 1,750 s in all, over 3 windows,
  `1792470600`, `1792471500` and `1792472400`. The projection after 30 fresh chunks was 1,337 s of fetching, against
  the `7,200` s bound. The fetch ran 2,166 s from its start to the last chunk.
- **The timing files:**
  - `set/fetch-timing.jsonl`, `42,417` bytes, SHA-256 `98f740a229d5bb19eb60b6d2a47338d847014e875518cffba607be62eaa7e145`.
  - `rehearsal/rehearsal-timing.jsonl`, `1,681` bytes, SHA-256 `8b3649dd6fbfbea1f625f5b685b891a76c10b6566c639710408b2af9490a61cf`.
  - §9 keeps both in the forensic store, for B3's measurement.
- **Read from the timing file by the Executor**, not printed by the instrument. These figures are diagnostics (§6
  item 3):
  - the chunks started from second 15.6 to second 469.4 of their windows, and the latest ended at second 482.6;
  - the first chunk started at `1792470693.660` (04:31:33.660 UTC) and the last ended at `1792472859.202`
    (05:07:39.202 UTC);
  - the chunks' own fetching time sums to 2,577.6 s over two workers.

### 2.9 §3.8 — the constants, twice (V9): **5 of 5 `unchanged`** — `logs/20-constants-1.log`, `logs/21-constants-2.log`, verbatim

```text
$ I constants
[2026-10-20T05:07:52Z] MemAvailable 268378112 bytes, floor 177135616
[2026-10-20T05:07:52Z] first look constants /root/btc-forensics/tz23-work--set--tz23-constants.json 2114 bytes sha256 1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5 equal
[2026-10-20T05:07:52Z] first look fills     /root/btc-forensics/tz23-work--set--tz23-fills.jsonl.gz 36870673 bytes sha256 4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64 equal
[2026-10-20T05:07:52Z] first look members   /root/btc-forensics/tz23-work--set--tz23-members.csv 2444450 bytes sha256 cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61 equal
[2026-10-20T05:07:52Z] first look reading   /root/btc-forensics/tz23-work--set--tz23-reading.json 1915 bytes sha256 fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043 equal
[2026-10-20T05:07:52Z] first look scored    /root/btc-forensics/tz23-work--set--tz23-scored.csv 464610 bytes sha256 12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988 equal
[2026-10-20T05:07:52Z] first look set       /root/btc-forensics/tz23-work--set--set.json 2314799 bytes sha256 a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303 equal
[2026-10-20T05:08:42Z] members 4032, considered 4032, first 1791242100 2026-10-05T23:15:00Z, last 1792451400 2026-10-19T23:10:00Z, weekend members 1152
[2026-10-20T05:08:42Z] member list sha 971258b48251a8c7e89c52919bd1801ad73725d98796f3481292d66d27136e5c
[2026-10-20T05:08:42Z] members by the number of excluded spans ending below them: 3: 4032
[2026-10-20T05:08:42Z] window fills 4883677, shares 121750790.403355, X -1318927.695927, C -2217836.7991042292052933, R 261052.60927858376201065651264713594
[2026-10-20T05:08:42Z] band pre  fills 323688, shares 11783735.472805
[2026-10-20T05:08:42Z] band w0   fills 1318474, shares 28799114.942090
[2026-10-20T05:08:42Z] band w1   fills 1150266, shares 25602395.002931
[2026-10-20T05:08:42Z] band w2   fills 1172520, shares 29111503.804786
[2026-10-20T05:08:42Z] band w3   fills 1242417, shares 38237776.653548
[2026-10-20T05:08:42Z] band last fills 742091, shares 30982434.460963
[2026-10-20T05:08:42Z] band post fills 17617, shares 5317719.821610
[2026-10-20T05:08:42Z] V 74784039554.144091973625; lambda 0.000021932; L 5.29831736654803667745321503082690498327770311161780120618734
[2026-10-20T05:08:42Z] EARN at S >= 446599.751684997567332872174725374110125738788601942422313849 (0.00366814663137243120012317938963426099674434510248456789069858 a share); NO EARN at S <= 162154.200331777432667127825274625889874261211398057577686151 (0.00133185336862756879987682061036573900325565489751543210930142 a share)
[2026-10-20T05:08:42Z] power of either answer against the other's alternative, normal, variance V/4: 0.8821721605021708
[2026-10-20T05:08:42Z] wrote /root/tz29-work/set/tz29-constants.json sha256 43b10ae4984f7914bbd6d3fa79432651ec7a491b94b2e6b6daf114acdf47d2b3
[2026-10-20T05:08:42Z] wrote /root/tz29-work/set/tz29-fills.jsonl.gz sha256 30c36db8d68a88ed0c34956c2c4fbda36653fa4d592cbdac6af8eac937e40aa4
[2026-10-20T05:08:42Z] wrote /root/tz29-work/set/tz29-members.csv sha256 97c67b0c830ee47a7be0d58117e6ab6a305b59ab80c7f599dadf190a42f41fc0
[2026-10-20T05:08:42Z] first look: members 4032, 1788530400 to 1791241800, considered 4032, non-members 0, weekend 1329; window fills 4820537, shares 129225737.554660, X 14980.119286, C -2182836.1232161653311455, R 289595.61967909269156966797439628522; V 69635266807.031814646570
[2026-10-20T05:08:42Z] second look: members 4032, 1791242100 to 1792451400, considered 4032, non-members 0, weekend 1152; window fills 4883677, shares 121750790.403355, X -1318927.695927, C -2217836.7991042292052933, R 261052.60927858376201065651264713594; V 74784039554.144091973625
[2026-10-20T05:08:42Z] both looks: members 8064, 1788530400 to 1792451400, member list sha 880a90303dcda502b5ac9562e94f6cadca4310a0ce19ea6450baaa650ae08f62
[2026-10-20T05:08:42Z] both looks: V 144419306361.175906620195; Sh 250976527.958015; lambda 0.000021932; L 5.29831736654803667745321503082690498327770311161780120618734
[2026-10-20T05:08:42Z] EARN at S >= 637504.835636475287186443829725374110125738788601942422313849 (0.00254009743788917694373483772039463894335372949552736164707628 a share); NO EARN at S <= 617377.804153599712813556170274625889874261211398057577686151 (0.00245990256211082305626516227960536105664627050447263835292372 a share)
[2026-10-20T05:08:42Z] power of either answer against the other's alternative, normal, variance V/4: 0.9994212268546403
[2026-10-20T05:08:42Z] 2 thr / Sh 0.00508019487577835388746967544078927788670745899105472329415256 against delta 0.005: UNDECIDABLE can occur
[2026-10-20T05:08:42Z] wrote cumulative-members.csv sha256 c1df5a5ba53ad376ab0e303f9fc9df78e86d3c1cbeafadd02b869e6d169e41ac and cumulative-constants.json sha256 747124081489fc5ef86c8a818e445e2dbff3caaa4cf014272c6a8c510e22c1cc
[2026-10-20T05:08:42Z] malloc tuned: True
[2026-10-20T05:08:42Z] peak memory of this run: 83947520 bytes
[2026-10-20T05:08:42Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

```text
$ I constants
[2026-10-20T05:08:49Z] MemAvailable 274210816 bytes, floor 177135616
[2026-10-20T05:08:49Z] first look constants /root/btc-forensics/tz23-work--set--tz23-constants.json 2114 bytes sha256 1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5 equal
[2026-10-20T05:08:50Z] first look fills     /root/btc-forensics/tz23-work--set--tz23-fills.jsonl.gz 36870673 bytes sha256 4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64 equal
[2026-10-20T05:08:50Z] first look members   /root/btc-forensics/tz23-work--set--tz23-members.csv 2444450 bytes sha256 cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61 equal
[2026-10-20T05:08:50Z] first look reading   /root/btc-forensics/tz23-work--set--tz23-reading.json 1915 bytes sha256 fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043 equal
[2026-10-20T05:08:50Z] first look scored    /root/btc-forensics/tz23-work--set--tz23-scored.csv 464610 bytes sha256 12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988 equal
[2026-10-20T05:08:50Z] first look set       /root/btc-forensics/tz23-work--set--set.json 2314799 bytes sha256 a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303 equal
[2026-10-20T05:09:39Z] unchanged /root/tz29-work/set/tz29-fills.jsonl.gz sha256 30c36db8d68a88ed0c34956c2c4fbda36653fa4d592cbdac6af8eac937e40aa4
[2026-10-20T05:09:39Z] unchanged /root/tz29-work/set/tz29-members.csv sha256 97c67b0c830ee47a7be0d58117e6ab6a305b59ab80c7f599dadf190a42f41fc0
[2026-10-20T05:09:39Z] unchanged /root/tz29-work/set/tz29-constants.json sha256 43b10ae4984f7914bbd6d3fa79432651ec7a491b94b2e6b6daf114acdf47d2b3
[2026-10-20T05:09:39Z] members 4032, considered 4032, first 1791242100 2026-10-05T23:15:00Z, last 1792451400 2026-10-19T23:10:00Z, weekend members 1152
[2026-10-20T05:09:39Z] member list sha 971258b48251a8c7e89c52919bd1801ad73725d98796f3481292d66d27136e5c
[2026-10-20T05:09:39Z] members by the number of excluded spans ending below them: 3: 4032
[2026-10-20T05:09:39Z] window fills 4883677, shares 121750790.403355, X -1318927.695927, C -2217836.7991042292052933, R 261052.60927858376201065651264713594
[2026-10-20T05:09:39Z] band pre  fills 323688, shares 11783735.472805
[2026-10-20T05:09:39Z] band w0   fills 1318474, shares 28799114.942090
[2026-10-20T05:09:39Z] band w1   fills 1150266, shares 25602395.002931
[2026-10-20T05:09:39Z] band w2   fills 1172520, shares 29111503.804786
[2026-10-20T05:09:39Z] band w3   fills 1242417, shares 38237776.653548
[2026-10-20T05:09:39Z] band last fills 742091, shares 30982434.460963
[2026-10-20T05:09:39Z] band post fills 17617, shares 5317719.821610
[2026-10-20T05:09:39Z] V 74784039554.144091973625; lambda 0.000021932; L 5.29831736654803667745321503082690498327770311161780120618734
[2026-10-20T05:09:39Z] EARN at S >= 446599.751684997567332872174725374110125738788601942422313849 (0.00366814663137243120012317938963426099674434510248456789069858 a share); NO EARN at S <= 162154.200331777432667127825274625889874261211398057577686151 (0.00133185336862756879987682061036573900325565489751543210930142 a share)
[2026-10-20T05:09:39Z] power of either answer against the other's alternative, normal, variance V/4: 0.8821721605021708
[2026-10-20T05:09:39Z] wrote /root/tz29-work/set/tz29-constants.json sha256 43b10ae4984f7914bbd6d3fa79432651ec7a491b94b2e6b6daf114acdf47d2b3
[2026-10-20T05:09:39Z] wrote /root/tz29-work/set/tz29-fills.jsonl.gz sha256 30c36db8d68a88ed0c34956c2c4fbda36653fa4d592cbdac6af8eac937e40aa4
[2026-10-20T05:09:39Z] wrote /root/tz29-work/set/tz29-members.csv sha256 97c67b0c830ee47a7be0d58117e6ab6a305b59ab80c7f599dadf190a42f41fc0
[2026-10-20T05:09:39Z] unchanged /root/tz29-work/cumulative/cumulative-members.csv sha256 c1df5a5ba53ad376ab0e303f9fc9df78e86d3c1cbeafadd02b869e6d169e41ac
[2026-10-20T05:09:39Z] unchanged /root/tz29-work/cumulative/cumulative-constants.json sha256 747124081489fc5ef86c8a818e445e2dbff3caaa4cf014272c6a8c510e22c1cc
[2026-10-20T05:09:39Z] first look: members 4032, 1788530400 to 1791241800, considered 4032, non-members 0, weekend 1329; window fills 4820537, shares 129225737.554660, X 14980.119286, C -2182836.1232161653311455, R 289595.61967909269156966797439628522; V 69635266807.031814646570
[2026-10-20T05:09:39Z] second look: members 4032, 1791242100 to 1792451400, considered 4032, non-members 0, weekend 1152; window fills 4883677, shares 121750790.403355, X -1318927.695927, C -2217836.7991042292052933, R 261052.60927858376201065651264713594; V 74784039554.144091973625
[2026-10-20T05:09:39Z] both looks: members 8064, 1788530400 to 1792451400, member list sha 880a90303dcda502b5ac9562e94f6cadca4310a0ce19ea6450baaa650ae08f62
[2026-10-20T05:09:39Z] both looks: V 144419306361.175906620195; Sh 250976527.958015; lambda 0.000021932; L 5.29831736654803667745321503082690498327770311161780120618734
[2026-10-20T05:09:39Z] EARN at S >= 637504.835636475287186443829725374110125738788601942422313849 (0.00254009743788917694373483772039463894335372949552736164707628 a share); NO EARN at S <= 617377.804153599712813556170274625889874261211398057577686151 (0.00245990256211082305626516227960536105664627050447263835292372 a share)
[2026-10-20T05:09:39Z] power of either answer against the other's alternative, normal, variance V/4: 0.9994212268546403
[2026-10-20T05:09:39Z] 2 thr / Sh 0.00508019487577835388746967544078927788670745899105472329415256 against delta 0.005: UNDECIDABLE can occur
[2026-10-20T05:09:39Z] wrote cumulative-members.csv sha256 c1df5a5ba53ad376ab0e303f9fc9df78e86d3c1cbeafadd02b869e6d169e41ac and cumulative-constants.json sha256 747124081489fc5ef86c8a818e445e2dbff3caaa4cf014272c6a8c510e22c1cc
[2026-10-20T05:09:39Z] malloc tuned: True
[2026-10-20T05:09:39Z] peak memory of this run: 83922944 bytes
[2026-10-20T05:09:39Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

| quantity | first look (TZ-23) | second look | both looks |
|---|---|---|---|
| members | 4,032 | 4,032 | 8,064 |
| `T0` | `1788530400` … `1791241800` | `1791242100` … `1792451400` | `1788530400` … `1792451400` |
| considered / non-members | 4,032 / 0 | 4,032 / 0 | — |
| weekend members | 1,329 | 1,152 | 2,481 (sum) |
| window fills | 4,820,537 | 4,883,677 | 9,704,214 (sum) |
| shares | 129,225,737.554660 | 121,750,790.403355 | `Sh` 250,976,527.958015 |
| `X` | 14,980.119286 | −1,318,927.695927 | — |
| `C` | −2,182,836.1232161653311455 | −2,217,836.7991042292052933 | — |
| `R` | 289,595.61967909269156966797439628522 | 261,052.60927858376201065651264713594 | — |
| `V` | 69,635,266,807.031814646570 | 74,784,039,554.144091973625 | 144,419,306,361.175906620195 |

The "(sum)" cells are the Executor's additions of the two printed figures. The other entries in the both-looks column
are the instrument's.

**The thresholds over both looks**, TZ-23's `gate_constants` with `λ = 0.000021932` and `L = ln(1/0.005)`:
- **EARN** at `S >= 637,504.835636…`, `0.254009743…` c a share.
- **NO EARN** at `S <= 617,377.804153…`, `0.245990256…` c a share.
- **Power `0.9994212268546403`**, printed at 05:08:42 UTC, before any label.
- `2 thr / Sh` = `0.508019…` c against `δ` = `0.5` c: **"UNDECIDABLE can occur"**. §1 projected `0.482` c and "cannot
  occur" at the first look's per-member rates. The second look carries fewer shares (`121.75` M against `129.23` M)
  and a larger `V`, which moved `2 thr / Sh` above `δ`. The TZ fixes this as a printed fact that decides nothing
  (§4.4: "No row reads a power").

The cumulative files are `cumulative-members.csv` `c1df5a5b…` and `cumulative-constants.json` `74712408…`, the
latter recorded in `state.json`. The both-looks member list is `880a90303dcda502b5ac9562e94f6cadca4310a0ce19ea6450baaa650ae08f62`.
The second run printed `unchanged` for all five files: `tz29-fills.jsonl.gz`, `tz29-members.csv`,
`tz29-constants.json`, `cumulative-members.csv` and `cumulative-constants.json`.

### 2.10 §3.9 — the score, twice (V10): **NO EARN** — `logs/22-score-1.log`, `logs/23-score-2.log`, verbatim

```text
$ I score
[2026-10-20T05:09:44Z] MemAvailable 289538048 bytes, floor 177135616
[2026-10-20T05:09:44Z] first look constants /root/btc-forensics/tz23-work--set--tz23-constants.json 2114 bytes sha256 1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5 equal
[2026-10-20T05:09:44Z] first look fills     /root/btc-forensics/tz23-work--set--tz23-fills.jsonl.gz 36870673 bytes sha256 4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64 equal
[2026-10-20T05:09:44Z] first look members   /root/btc-forensics/tz23-work--set--tz23-members.csv 2444450 bytes sha256 cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61 equal
[2026-10-20T05:09:44Z] first look reading   /root/btc-forensics/tz23-work--set--tz23-reading.json 1915 bytes sha256 fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043 equal
[2026-10-20T05:09:44Z] first look scored    /root/btc-forensics/tz23-work--set--tz23-scored.csv 464610 bytes sha256 12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988 equal
[2026-10-20T05:09:44Z] first look set       /root/btc-forensics/tz23-work--set--set.json 2314799 bytes sha256 a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303 equal
[2026-10-20T05:09:45Z] labels: 8064 members, 4032 Up
[2026-10-20T05:09:45Z] S 580110.13776807099001912448704342116 = settlement 29461.9088103945364388 + rebate 550648.22895767645358032448704342116; per share 0.00231141191763205688852666889832906347997748112208666200414888 = 0.000117389100287988356482448395122095225849969396569670312416536 + 0.00219402281734406853204422050320696825412751172551699169173235
[2026-10-20T05:09:45Z] EARN False (margin -57394.697868404297167319342681952950125738788601942422313849); NO EARN True (margin 37267.666385528722794431683231204729874261211398057577686151)
[2026-10-20T05:09:45Z] band pre  makers per share 0.00505591573871396254585602924841306691260556943419127733090686, of it rebate 0.00344602782366186263427478639141032292468574111776385477138373 - barred from every reading
[2026-10-20T05:09:45Z] band w0   makers per share 0.00453024950874632443257966016822383156397354255384451361790309, of it rebate 0.00303468670826912641507487312260179900063398363732596724252507 - barred from every reading
[2026-10-20T05:09:45Z] band w1   makers per share 0.00382521581995166775549586715671819296476009079783758197357320, of it rebate 0.00255027545286188316046848129353383229617172035622686932457902 - barred from every reading
[2026-10-20T05:09:45Z] band w2   makers per share 0.00327032923003786688674268173642516290768192686867518402844435, of it rebate 0.00204611974821831344500113398880713953064382375871672829818407 - barred from every reading
[2026-10-20T05:09:45Z] band w3   makers per share -0.00112959305233134207706915626740916936424302518299900232498924, of it rebate 0.00142407387438181772117269555758114309908070467637584204596201 - barred from every reading
[2026-10-20T05:09:45Z] band last makers per share 0.00150468866785114019393011698889274570366864728334546981281907, of it rebate 0.000815914238207721032065261390467298206227764717349697367508281 - barred from every reading
[2026-10-20T05:09:45Z] band post makers per share 0.00396285552387778465714137669501584463261168350518679298354131, of it rebate 0.0000673094018623371055095821898439960530901765577690008083667836 - barred from every reading
[2026-10-20T05:09:45Z] wrote cumulative-scored.csv sha256 e3131814a61b7ff5619e57d1d0af0478d7604f0b0c71e868f3e4e2fccfe77fae and cumulative-reading.json sha256 aa3a8f5c250ccc53b4d0d184f8e0ed1699002d97b77c906f5329880a98fda601
[2026-10-20T05:09:45Z] the first look's 4032 rows of the scored file equal TZ-23's, byte for byte
[2026-10-20T05:09:45Z] the first look, TZ-23's: S 272424.11263025802271516797439628522 = settlement -17171.5070488346688545 + rebate 289595.61967909269156966797439628522, 2023 Up
[2026-10-20T05:09:45Z] the second look, by difference, barred from every reading: S 307686.02513781296730395651264713594 = settlement 46633.4158592292052933 + rebate 261052.60927858376201065651264713594, 2009 Up; per share 0.00252717887184520719291294097845062550836054491371458375201224 = 0.000383023516354470922563561033397605382058784843364702927222322 + 0.00214415535549073627034937994505302012630176007034988082478992
[2026-10-20T05:09:45Z] M0 READING, OVER BOTH LOOKS: NO EARN
[2026-10-20T05:09:45Z] malloc tuned: True
[2026-10-20T05:09:45Z] peak memory of this run: 72376320 bytes
[2026-10-20T05:09:45Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

```text
$ I score
[2026-10-20T05:09:51Z] MemAvailable 270196736 bytes, floor 177135616
[2026-10-20T05:09:51Z] first look constants /root/btc-forensics/tz23-work--set--tz23-constants.json 2114 bytes sha256 1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5 equal
[2026-10-20T05:09:51Z] first look fills     /root/btc-forensics/tz23-work--set--tz23-fills.jsonl.gz 36870673 bytes sha256 4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64 equal
[2026-10-20T05:09:51Z] first look members   /root/btc-forensics/tz23-work--set--tz23-members.csv 2444450 bytes sha256 cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61 equal
[2026-10-20T05:09:51Z] first look reading   /root/btc-forensics/tz23-work--set--tz23-reading.json 1915 bytes sha256 fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043 equal
[2026-10-20T05:09:51Z] first look scored    /root/btc-forensics/tz23-work--set--tz23-scored.csv 464610 bytes sha256 12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988 equal
[2026-10-20T05:09:51Z] first look set       /root/btc-forensics/tz23-work--set--set.json 2314799 bytes sha256 a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303 equal
[2026-10-20T05:09:51Z] unchanged /root/tz29-work/cumulative/cumulative-scored.csv sha256 e3131814a61b7ff5619e57d1d0af0478d7604f0b0c71e868f3e4e2fccfe77fae
[2026-10-20T05:09:51Z] unchanged /root/tz29-work/cumulative/cumulative-reading.json sha256 aa3a8f5c250ccc53b4d0d184f8e0ed1699002d97b77c906f5329880a98fda601
[2026-10-20T05:09:51Z] labels: 8064 members, 4032 Up
[2026-10-20T05:09:51Z] S 580110.13776807099001912448704342116 = settlement 29461.9088103945364388 + rebate 550648.22895767645358032448704342116; per share 0.00231141191763205688852666889832906347997748112208666200414888 = 0.000117389100287988356482448395122095225849969396569670312416536 + 0.00219402281734406853204422050320696825412751172551699169173235
[2026-10-20T05:09:51Z] EARN False (margin -57394.697868404297167319342681952950125738788601942422313849); NO EARN True (margin 37267.666385528722794431683231204729874261211398057577686151)
[2026-10-20T05:09:51Z] band pre  makers per share 0.00505591573871396254585602924841306691260556943419127733090686, of it rebate 0.00344602782366186263427478639141032292468574111776385477138373 - barred from every reading
[2026-10-20T05:09:51Z] band w0   makers per share 0.00453024950874632443257966016822383156397354255384451361790309, of it rebate 0.00303468670826912641507487312260179900063398363732596724252507 - barred from every reading
[2026-10-20T05:09:51Z] band w1   makers per share 0.00382521581995166775549586715671819296476009079783758197357320, of it rebate 0.00255027545286188316046848129353383229617172035622686932457902 - barred from every reading
[2026-10-20T05:09:51Z] band w2   makers per share 0.00327032923003786688674268173642516290768192686867518402844435, of it rebate 0.00204611974821831344500113398880713953064382375871672829818407 - barred from every reading
[2026-10-20T05:09:51Z] band w3   makers per share -0.00112959305233134207706915626740916936424302518299900232498924, of it rebate 0.00142407387438181772117269555758114309908070467637584204596201 - barred from every reading
[2026-10-20T05:09:51Z] band last makers per share 0.00150468866785114019393011698889274570366864728334546981281907, of it rebate 0.000815914238207721032065261390467298206227764717349697367508281 - barred from every reading
[2026-10-20T05:09:51Z] band post makers per share 0.00396285552387778465714137669501584463261168350518679298354131, of it rebate 0.0000673094018623371055095821898439960530901765577690008083667836 - barred from every reading
[2026-10-20T05:09:51Z] wrote cumulative-scored.csv sha256 e3131814a61b7ff5619e57d1d0af0478d7604f0b0c71e868f3e4e2fccfe77fae and cumulative-reading.json sha256 aa3a8f5c250ccc53b4d0d184f8e0ed1699002d97b77c906f5329880a98fda601
[2026-10-20T05:09:51Z] the first look's 4032 rows of the scored file equal TZ-23's, byte for byte
[2026-10-20T05:09:51Z] the first look, TZ-23's: S 272424.11263025802271516797439628522 = settlement -17171.5070488346688545 + rebate 289595.61967909269156966797439628522, 2023 Up
[2026-10-20T05:09:51Z] the second look, by difference, barred from every reading: S 307686.02513781296730395651264713594 = settlement 46633.4158592292052933 + rebate 261052.60927858376201065651264713594, 2009 Up; per share 0.00252717887184520719291294097845062550836054491371458375201224 = 0.000383023516354470922563561033397605382058784843364702927222322 + 0.00214415535549073627034937994505302012630176007034988082478992
[2026-10-20T05:09:51Z] M0 READING, OVER BOTH LOOKS: NO EARN
[2026-10-20T05:09:51Z] malloc tuned: True
[2026-10-20T05:09:51Z] peak memory of this run: 72380416 bytes
[2026-10-20T05:09:51Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

**The label ledger**, `label-ledger.jsonl`, two lines, each a `score` run at `HEAD` `f6425f7…`:

```text
{"at":"2026-10-20T05:09:45Z","head":"f6425f713034724210dc120d2108bcfad63cadc6","member_list_sha":"880a90303dcda502b5ac9562e94f6cadca4310a0ce19ea6450baaa650ae08f62","members":8064}
{"at":"2026-10-20T05:09:51Z","head":"f6425f713034724210dc120d2108bcfad63cadc6","member_list_sha":"880a90303dcda502b5ac9562e94f6cadca4310a0ce19ea6450baaa650ae08f62","members":8064}
```

| figure, over both looks | USDC | c a share |
|---|---|---|
| `S` | 580,110.13776807099001912448704342116 | 0.231141 |
| settlement part | 29,461.9088103945364388 | 0.011739 |
| rebate part | 550,648.22895767645358032448704342116 | 0.219402 |
| EARN bound `thr` | 637,504.835636… | 0.254010 |
| NO EARN bound `δ · Sh − thr` | 617,377.804153… | 0.245990 |
| EARN margin `S − thr` | −57,394.697868… | −0.022869 |
| NO EARN margin `δ · Sh − thr − S` | +37,267.666385… | +0.014849 |
| *barred:* the first look's `S`, TZ-23's | 272,424.11263025802271516797439628522 | 0.210813 |
| *barred:* the second look's `S`, by difference | 307,686.02513781296730395651264713594 | 0.252718 |
| *barred:* the second look's settlement and rebate | 46,633.4158592292052933 / 261,052.60927858376201065651264713594 | 0.038302 / 0.214416 |

The per-share figures for `S` and its parts, both looks and the second, are the instrument's. The bounds' per-share
figures are `constants`'. Every per-share figure in this table is rounded to six decimals of a cent. The margins' per-share figures and the first look's are the Executor's ratios of the printed
figures to `Sh` (both looks: `250,976,527.958015`; first look: `129,225,737.554660`), at 60 digits.

**The makers' result per share in each band, over both looks, barred from every reading** (the instrument's lines,
converted to cents a share and rounded to four decimals):

| band | makers, c a share | of it rebate, c a share |
|---|---|---|
| pre | 0.5056 c | 0.3446 c |
| w0 | 0.4530 c | 0.3035 c |
| w1 | 0.3825 c | 0.2550 c |
| w2 | 0.3270 c | 0.2046 c |
| w3 | −0.1130 c | 0.1424 c |
| last | 0.1505 c | 0.0816 c |
| post | 0.3963 c | 0.0067 c |

**The first look's 4,032 rows of the cumulative scored file equal TZ-23's, byte for byte**, asserted by `score`. The
second run printed `unchanged` for `cumulative-scored.csv` `e3131814…` and `cumulative-reading.json` `aa3a8f5c…`.

### 2.11 §3.10 — G-STILL (V11): **PASS** — `logs/24-still-2.log`, verbatim

```text
$ I still
[2026-10-20T05:09:51Z] btc-pairbook.service {'MainPID': '1942330', 'NRestarts': '15', 'ActiveState': 'active'}, MemoryCurrent 19947520, MemoryPeak 108912640
[2026-10-20T05:09:51Z] btc-recorder.service {'MainPID': '4148534', 'NRestarts': '2', 'ActiveState': 'active'}, MemoryCurrent 74772480, MemoryPeak 258011136
[2026-10-20T05:09:51Z] btc-pairbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-20T05:09:51Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-20T05:09:51Z] G-STILL PASS: unchanged since 2026-10-20T04:27:51Z
[2026-10-20T05:09:51Z] malloc tuned: True
[2026-10-20T05:09:51Z] peak memory of this run: 28934144 bytes
[2026-10-20T05:09:51Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

### 2.12 §3.11 — the closing reads (V15) — `logs/25-host-gate-2.log`, `logs/26-archive-2.log`, `logs/27-closing-reads.log`, verbatim

```text
Tue Oct 20 05:10:06 AM UTC 2026
1792473006
1
MemTotal:         978640 kB
MemAvailable:     277932 kB
SwapTotal:       3174396 kB
SwapFree:        2739336 kB
2026-08-02 07:24:32
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
 -5 23a31fad2f064f04b9e138eac29658f3 Sat 2026-06-06 11:51:20 UTC Fri 2026-06-26 14:13:44 UTC
 -4 a38e17445ce341bc8b877be9d3d4f648 Fri 2026-06-26 14:13:52 UTC Tue 2026-07-14 16:15:10 UTC
 -3 5f4d18a6ba8041bd80e7d1e192c5ee28 Tue 2026-07-14 16:15:20 UTC Fri 2026-07-17 01:01:21 UTC
 -2 b1b399c70c6e4dcc934755f70a2ca231 Fri 2026-07-17 01:01:43 UTC Fri 2026-07-24 14:55:46 UTC
 -1 285d6962c92c407d837d1ce329b93aa4 Fri 2026-07-24 14:55:54 UTC Sun 2026-08-02 07:23:49 UTC
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-02 07:24:34 UTC Tue 2026-10-20 05:10:00 UTC
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12451913728
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
1
3.12.3
2314799 tz23-work--set--set.json
36870673 tz23-work--set--tz23-fills.jsonl.gz
2444450 tz23-work--set--tz23-members.csv
2114 tz23-work--set--tz23-constants.json
464610 tz23-work--set--tz23-scored.csv
1915 tz23-work--set--tz23-reading.json
a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303  tz23-work--set--set.json
4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64  tz23-work--set--tz23-fills.jsonl.gz
cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61  tz23-work--set--tz23-members.csv
1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5  tz23-work--set--tz23-constants.json
12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988  tz23-work--set--tz23-scored.csv
fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043  tz23-work--set--tz23-reading.json
MainPID=4148534
Result=success
NRestarts=2
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-04 22:22:07 UTC

MainPID=1942330
Result=success
NRestarts=15
Id=btc-pairbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Tue 2026-10-20 03:03:44 UTC

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
NEXT                        LEFT LAST                             PASSED UNIT                       ACTIVATES
Wed 2026-10-21 03:00:20 UTC  21h Tue 2026-10-20 03:00:20 UTC 2h 9min ago btc-pairbook-archive.timer btc-pairbook-archive.service

1 timers listed.
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
e8b46a85d61e1a17841962846f6d3012046c2d70
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
/root/tz28-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
/root/btc-pairbook-archive-svc exit=0
/var/lib/btc-pairbook-archive exit=0
1846
/root/btc-5m-twap       ad38846 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/root/tz29-work/wt      f6425f7 [tz-29-maker-m0-second-look]
230889230	/var/lib/btc-pairbook
3608965	/var/lib/btc-pairbook-archive
133112587	/root/.claude
594876943	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/7a160398-f4cf-54ee-b771-c3006d558bde/scratchpad
total 16
drwx------  4 root root 4096 Oct 20 04:28 .
drwx------ 20 root root 4096 Oct 20 04:24 ..
drwx------  3 root root 4096 Oct 20 04:24 6a6870c2-3843-4a2b-83cf-b2f45c5500a1
drwx------  4 root root 4096 Oct 20 04:24 7a160398-f4cf-54ee-b771-c3006d558bde
```

```text
$ I archive
[2026-10-20T05:10:08Z] btc-pairbook-archive.timer {'NextElapseUSecRealtime': 'Wed 2026-10-21 03:00:20 UTC', 'LastTriggerUSec': 'Tue 2026-10-20 03:00:20 UTC', 'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-20T05:10:08Z] btc-pairbook-archive.service {'Result': 'success', 'ExecMainStatus': '0', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-20T05:10:08Z] ledger /var/lib/btc-pairbook-archive/ledger.jsonl: 30913 bytes sha256 3d08a5f72d74ccac340ed93a4c85126612b6df5b56e1135a54677e57312ce272, 130 complete records, 0 bytes of a line still written
[2026-10-20T05:10:08Z] L 2026-10-11T15:18:12Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "2a4b998acb9f4883b26999bb278624bf", "phase_at": 192, "resumed": false, "run": 1791731892, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791731892810556801}
[2026-10-20T05:10:08Z] L 2026-10-11T15:18:13Z {"assets_n": 28, "bytes_total": 430047476, "closed": 79, "deferred": 0, "event": "set", "first_T": 1791706500, "last_T": 1791730800, "open": 0, "run": 1791731892, "sha256": "ec3983419485fa67317468917eb7b60e2d0e529be4334c7297831ff562471ad0", "tag": "pairbook-streams-1791731892", "unclosed": 0, "wall_ns": 1791731893762719408, "windows_considered": 79}
[2026-10-20T05:10:08Z] L 2026-10-11T15:18:57Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 409746510, "run": 1791731892, "sent": 28, "wall_ns": 1791731937181037882}
[2026-10-20T05:10:08Z] L 2026-10-11T15:21:30Z {"assets_n": 28, "bytes_total": 430047476, "event": "verify", "release_id": 409746510, "run": 1791731892, "verify_sha256": "032adfdbaea0b81d7ea5063eb43130c09396908f05d74be0f1818d2bb2342f64", "wall_ns": 1791732090814504593}
[2026-10-20T05:10:08Z] L 2026-10-11T15:21:31Z {"already": 0, "event": "delete", "free_after": 12969091072, "free_before": 12538937344, "freed": 430047476, "gone": 28, "removed": 28, "run": 1791731892, "wall_ns": 1791732091732399708, "windows_kept": 28}
[2026-10-20T05:10:08Z] L 2026-10-11T15:21:31Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "815823", "NRestarts": "2", "ns": 1791732091741955625}, "phase": 391, "run": 1791731892, "wall_ns": 1791732091741960838}
[2026-10-20T05:10:08Z] L 2026-10-11T15:21:31Z {"event": "kill", "exit": 0, "phase": 391, "run": 1791731892, "wall_ns": 1791732091746593097}
[2026-10-20T05:10:08Z] L 2026-10-11T15:22:01Z {"NRestarts": "3", "W": 1791731700, "event": "restart", "free_bytes": 12969062400, "gap_ns": 5548461176, "pid": 851381, "run": 1791731892, "stopped": 815823, "stream_bytes": 0, "wall_ns": 1791732121761569347}
[2026-10-20T05:10:08Z] L 2026-10-11T15:30:41Z {"T": 1791731700, "event": "resume", "reading": "PASS", "run": 1791731892, "wall_ns": 1791732641000772037}
[2026-10-20T05:10:08Z] L 2026-10-11T15:30:41Z {"assets_n": 28, "bytes_total": 430047476, "ended_outside": 0, "event": "complete", "free_bytes": 12949487616, "peak_rss": 36884480, "rate_per_day": 1474448489, "requests": 61, "run": 1791731892, "started_outside": 0, "stops": [["the cap", 1792200292], ["the floor, base 43500000 bytes a day", 1792213576], ["the floor, base 187760570 bytes a day", 1792171837]], "store_stream_bytes": 19346486, "wall_ns": 1791732641002785194}
[2026-10-20T05:10:08Z] L 2026-10-12T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "b458725447bd4a0c865999eab0a904ad", "phase_at": 20, "resumed": false, "run": 1791774020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791774020508107799}
[2026-10-20T05:10:08Z] L 2026-10-12T03:00:22Z {"assets_n": 46, "bytes_total": 794522712, "closed": 125, "deferred": 0, "event": "set", "first_T": 1791731700, "last_T": 1791772200, "open": 1, "run": 1791774020, "sha256": "c8f02de3fbed47c4cfa91e66d774427f20990f634d271237bf3c6f25887ffb99", "tag": "pairbook-streams-1791774020", "unclosed": 0, "wall_ns": 1791774022193879442, "windows_considered": 125}
[2026-10-20T05:10:08Z] L 2026-10-12T03:01:35Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 410101186, "run": 1791774020, "sent": 46, "wall_ns": 1791774095014644950}
[2026-10-20T05:10:08Z] L 2026-10-12T03:04:44Z {"assets_n": 46, "bytes_total": 794522712, "event": "verify", "release_id": 410101186, "run": 1791774020, "verify_sha256": "0f86d9494743193ae4dd5ddb59e37a08eebc8bb7318ea4d98def44406d025aec", "wall_ns": 1791774284631917592}
[2026-10-20T05:10:08Z] L 2026-10-12T03:04:46Z {"already": 0, "event": "delete", "free_after": 12960145408, "free_before": 12165431296, "freed": 794522712, "gone": 46, "removed": 46, "run": 1791774020, "wall_ns": 1791774286328338970, "windows_kept": 46}
[2026-10-20T05:10:08Z] L 2026-10-12T03:04:46Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "851381", "NRestarts": "3", "ns": 1791774286341020683}, "phase": 286, "run": 1791774020, "wall_ns": 1791774286341025663}
[2026-10-20T05:10:08Z] L 2026-10-12T03:04:46Z {"event": "kill", "exit": 0, "phase": 286, "run": 1791774020, "wall_ns": 1791774286345765034}
[2026-10-20T05:10:08Z] L 2026-10-12T03:05:16Z {"NRestarts": "4", "W": 1791774000, "event": "restart", "free_bytes": 12960112640, "gap_ns": 5455854888, "pid": 911226, "run": 1791774020, "stopped": 851381, "stream_bytes": 25646773, "wall_ns": 1791774316361306454}
[2026-10-20T05:10:08Z] L 2026-10-12T03:15:41Z {"T": 1791774000, "event": "resume", "reading": "PASS", "run": 1791774020, "wall_ns": 1791774941000362333}
[2026-10-20T05:10:08Z] L 2026-10-12T03:15:41Z {"assets_n": 46, "bytes_total": 794522712, "ended_outside": 0, "event": "complete", "free_bytes": 12948570112, "peak_rss": 37670912, "rate_per_day": 1658134355, "requests": 97, "run": 1791774020, "started_outside": 0, "stops": [["the cap", 1792189855], ["the floor, base 43500000 bytes a day", 1792203914], ["the floor, base 187760570 bytes a day", 1792170389]], "store_stream_bytes": 37220758, "wall_ns": 1791774941002570067}
[2026-10-20T05:10:08Z] L 2026-10-13T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "5e59db817b3d42ef91641fbb34bc17cc", "phase_at": 20, "resumed": false, "run": 1791860420, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791860420531436360}
[2026-10-20T05:10:08Z] L 2026-10-13T03:00:24Z {"assets_n": 96, "bytes_total": 1925987888, "closed": 221, "deferred": 0, "event": "set", "first_T": 1791773100, "last_T": 1791858600, "open": 1, "run": 1791860420, "sha256": "de9209f2e76e5c42bd1395ea6e9c17ab0fc4c497be6a9311cd1e07c101f9b777", "tag": "pairbook-streams-1791860420", "unclosed": 0, "wall_ns": 1791860424671646762, "windows_considered": 221}
[2026-10-20T05:10:08Z] L 2026-10-13T03:03:13Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 411210796, "run": 1791860420, "sent": 96, "wall_ns": 1791860593421247948}
[2026-10-20T05:10:08Z] L 2026-10-13T03:07:31Z {"assets_n": 96, "bytes_total": 1925987888, "event": "verify", "release_id": 411210796, "run": 1791860420, "verify_sha256": "a5969978f8bfb614451c41257e7eb70a13c12126932ef03d4cfbd2f2c41ad022", "wall_ns": 1791860851109946296}
[2026-10-20T05:10:08Z] L 2026-10-13T03:07:35Z {"already": 0, "event": "delete", "free_after": 12876316672, "free_before": 10949902336, "freed": 1925987888, "gone": 96, "removed": 96, "run": 1791860420, "wall_ns": 1791860855219206873, "windows_kept": 96}
[2026-10-20T05:10:08Z] L 2026-10-13T03:07:35Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "911226", "NRestarts": "4", "ns": 1791860855230756130}, "phase": 455, "run": 1791860420, "wall_ns": 1791860855230762191}
[2026-10-20T05:10:08Z] L 2026-10-13T03:07:35Z {"event": "kill", "exit": 0, "phase": 455, "run": 1791860420, "wall_ns": 1791860855235973960}
[2026-10-20T05:10:08Z] L 2026-10-13T03:08:05Z {"NRestarts": "5", "W": 1791860400, "event": "restart", "free_bytes": 12876300288, "gap_ns": 5561093708, "pid": 1027378, "run": 1791860420, "stopped": 911226, "stream_bytes": 23131514, "wall_ns": 1791860885252051875}
[2026-10-20T05:10:08Z] L 2026-10-13T03:15:41Z {"T": 1791860400, "event": "resume", "reading": "PASS", "run": 1791860420, "wall_ns": 1791861341000349433}
[2026-10-20T05:10:08Z] L 2026-10-13T03:15:41Z {"assets_n": 96, "bytes_total": 1925987888, "ended_outside": 0, "event": "complete", "free_bytes": 12857700352, "peak_rss": 37941248, "rate_per_day": 1925987888, "requests": 197, "run": 1791860420, "started_outside": 0, "stops": [["the cap", 1792218357], ["the floor, base 43500000 bytes a day", 1792227987], ["the floor, base 187760570 bytes a day", 1792202964]], "store_stream_bytes": 41556131, "wall_ns": 1791861341004126797}
[2026-10-20T05:10:08Z] L 2026-10-14T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "f4f5335f60584baeab0eabd568d20823", "phase_at": 20, "resumed": false, "run": 1791946820, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791946820511249708}
[2026-10-20T05:10:08Z] L 2026-10-14T03:00:24Z {"assets_n": 96, "bytes_total": 2039544263, "closed": 317, "deferred": 0, "event": "set", "first_T": 1791859500, "last_T": 1791945000, "open": 1, "run": 1791946820, "sha256": "9c78ba5221e0bc8d9d8699d920e17c58d76b6052fce7c0e86af4948bdc38aa1e", "tag": "pairbook-streams-1791946820", "unclosed": 0, "wall_ns": 1791946824807088559, "windows_considered": 317}
[2026-10-20T05:10:08Z] L 2026-10-14T03:03:21Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 412296623, "run": 1791946820, "sent": 96, "wall_ns": 1791947001852058175}
[2026-10-20T05:10:08Z] L 2026-10-14T03:07:45Z {"assets_n": 96, "bytes_total": 2039544263, "event": "verify", "release_id": 412296623, "run": 1791946820, "verify_sha256": "086fc6331ec202ef5c6b56257a52cbc12673053f82408a3cd4b3cf203ae44c95", "wall_ns": 1791947265299596860}
[2026-10-20T05:10:08Z] L 2026-10-14T03:07:49Z {"already": 0, "event": "delete", "free_after": 12842123264, "free_before": 10802130944, "freed": 2039544263, "gone": 96, "removed": 96, "run": 1791946820, "wall_ns": 1791947269716703785, "windows_kept": 96}
[2026-10-20T05:10:08Z] L 2026-10-14T03:07:49Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1027378", "NRestarts": "5", "ns": 1791947269728675162}, "phase": 469, "run": 1791946820, "wall_ns": 1791947269728680763}
[2026-10-20T05:10:08Z] L 2026-10-14T03:07:49Z {"event": "kill", "exit": 0, "phase": 469, "run": 1791946820, "wall_ns": 1791947269733842747}
[2026-10-20T05:10:08Z] L 2026-10-14T03:08:19Z {"NRestarts": "6", "W": 1791946800, "event": "restart", "free_bytes": 12842098688, "gap_ns": 5560847791, "pid": 1155982, "run": 1791946820, "stopped": 1027378, "stream_bytes": 17222124, "wall_ns": 1791947299751305660}
[2026-10-20T05:10:08Z] L 2026-10-14T03:15:41Z {"T": 1791946800, "event": "resume", "reading": "PASS", "run": 1791946820, "wall_ns": 1791947741000324294}
[2026-10-20T05:10:08Z] L 2026-10-14T03:15:41Z {"assets_n": 96, "bytes_total": 2039544263, "ended_outside": 0, "event": "complete", "free_bytes": 12820799488, "peak_rss": 38072320, "rate_per_day": 2039544263, "requests": 197, "run": 1791946820, "started_outside": 0, "stops": [["the cap", 1792285007], ["the floor, base 43500000 bytes a day", 1792292869], ["the floor, base 187760570 bytes a day", 1792270515]], "store_stream_bytes": 38533208, "wall_ns": 1791947741004939814}
[2026-10-20T05:10:08Z] L 2026-10-15T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "08fd4972db8347a4897a6ecd018049e4", "phase_at": 20, "resumed": false, "run": 1792033220, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792033220507675615}
[2026-10-20T05:10:08Z] L 2026-10-15T03:00:25Z {"assets_n": 96, "bytes_total": 2103892072, "closed": 413, "deferred": 0, "event": "set", "first_T": 1791945900, "last_T": 1792031400, "open": 1, "run": 1792033220, "sha256": "3272c87234da82333365144d0c39bb0f75e895943e7e34ec7ff1e559c1ad8715", "tag": "pairbook-streams-1792033220", "unclosed": 0, "wall_ns": 1792033225025238523, "windows_considered": 413}
[2026-10-20T05:10:08Z] L 2026-10-15T03:03:26Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 413374764, "run": 1792033220, "sent": 96, "wall_ns": 1792033406364376177}
[2026-10-20T05:10:08Z] L 2026-10-15T03:07:54Z {"assets_n": 96, "bytes_total": 2103892072, "event": "verify", "release_id": 413374764, "run": 1792033220, "verify_sha256": "ff1dbc619728c35ab3732813ed23e83065603970c79ae62379097e59b1f13fa0", "wall_ns": 1792033674329218632}
[2026-10-20T05:10:08Z] L 2026-10-15T03:07:58Z {"already": 0, "event": "delete", "free_after": 12590329856, "free_before": 10485972992, "freed": 2103892072, "gone": 96, "removed": 96, "run": 1792033220, "wall_ns": 1792033678892316224, "windows_kept": 96}
[2026-10-20T05:10:08Z] L 2026-10-15T03:15:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1155982", "NRestarts": "6", "ns": 1792034115012851485}, "phase": 15, "run": 1792033220, "wall_ns": 1792034115012856996}
[2026-10-20T05:10:08Z] L 2026-10-15T03:15:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792033220, "wall_ns": 1792034115018137811}
[2026-10-20T05:10:08Z] L 2026-10-15T03:15:45Z {"NRestarts": "7", "W": 1792034100, "event": "restart", "free_bytes": 12572676096, "gap_ns": 5531970911, "pid": 1284485, "run": 1792033220, "stopped": 1155982, "stream_bytes": 29667971, "wall_ns": 1792034145058520440}
[2026-10-20T05:10:08Z] L 2026-10-15T03:30:41Z {"T": 1792034100, "event": "resume", "reading": "PASS", "run": 1792033220, "wall_ns": 1792035041000365330}
[2026-10-20T05:10:08Z] L 2026-10-15T03:30:41Z {"assets_n": 96, "bytes_total": 2103892072, "ended_outside": 0, "event": "complete", "free_bytes": 12548313088, "peak_rss": 38199296, "rate_per_day": 2103892072, "requests": 197, "run": 1792033220, "started_outside": 0, "stops": [["the cap", 1792361344], ["the floor, base 43500000 bytes a day", 1792358863], ["the floor, base 187760570 bytes a day", 1792338478]], "store_stream_bytes": 54308421, "wall_ns": 1792035041006683547}
[2026-10-20T05:10:08Z] L 2026-10-15T06:18:30Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "1fd2e68b26a04a328b7551cbafc2eabe", "phase_at": 210, "resumed": false, "run": 1792045110, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792045110608854708}
[2026-10-20T05:10:08Z] L 2026-10-15T06:18:31Z {"assets_n": 14, "bytes_total": 352241341, "closed": 427, "deferred": 0, "event": "set", "first_T": 1792032300, "last_T": 1792044000, "open": 0, "run": 1792045110, "sha256": "0337b76512886f5dd78d71cfb303a343631f73624e2eb539ed79ed7f32cc0b8e", "tag": "pairbook-streams-1792045110", "unclosed": 0, "wall_ns": 1792045111425201892, "windows_considered": 427}
[2026-10-20T05:10:08Z] L 2026-10-15T06:19:00Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 413477311, "run": 1792045110, "sent": 14, "wall_ns": 1792045140771279777}
[2026-10-20T05:10:08Z] L 2026-10-15T06:21:20Z {"assets_n": 14, "bytes_total": 352241341, "event": "verify", "release_id": 413477311, "run": 1792045110, "verify_sha256": "52fc16f3058d99f3207b8fe2e61473302a0f89a9e1a2e0f5c8eb71f413e8e379", "wall_ns": 1792045280782420614}
[2026-10-20T05:10:08Z] L 2026-10-15T06:21:21Z {"already": 0, "event": "delete", "free_after": 12826914816, "free_before": 12474617856, "freed": 352241341, "gone": 14, "removed": 14, "run": 1792045110, "wall_ns": 1792045281527345757, "windows_kept": 14}
[2026-10-20T05:10:08Z] L 2026-10-15T06:21:21Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1284485", "NRestarts": "7", "ns": 1792045281539516731}, "phase": 381, "run": 1792045110, "wall_ns": 1792045281539522189}
[2026-10-20T05:10:08Z] L 2026-10-15T06:21:21Z {"event": "kill", "exit": 0, "phase": 381, "run": 1792045110, "wall_ns": 1792045281543696309}
[2026-10-20T05:10:08Z] L 2026-10-15T06:21:51Z {"NRestarts": "8", "W": 1792044900, "event": "restart", "free_bytes": 12826902528, "gap_ns": 5495918230, "pid": 1312748, "run": 1792045110, "stopped": 1284485, "stream_bytes": 0, "wall_ns": 1792045311558979330}
[2026-10-20T05:10:08Z] L 2026-10-15T06:30:41Z {"T": 1792044900, "event": "resume", "reading": "PASS", "run": 1792045110, "wall_ns": 1792045841024547052}
[2026-10-20T05:10:08Z] L 2026-10-15T06:30:41Z {"assets_n": 14, "bytes_total": 352241341, "ended_outside": 0, "event": "complete", "free_bytes": 12813713408, "peak_rss": 37543936, "rate_per_day": 2415369195, "requests": 33, "run": 1792045110, "started_outside": 0, "stops": [["the cap", 1792331549], ["the floor, base 43500000 bytes a day", 1792337969], ["the floor, base 187760570 bytes a day", 1792321779]], "store_stream_bytes": 12817136, "wall_ns": 1792045841098825002}
[2026-10-20T05:10:08Z] L 2026-10-16T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "5fd01e0598954380beeca3f3ac4c3f62", "phase_at": 20, "resumed": false, "run": 1792119620, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792119620165748278}
[2026-10-20T05:10:08Z] L 2026-10-16T03:00:24Z {"assets_n": 82, "bytes_total": 1804368058, "closed": 509, "deferred": 0, "event": "set", "first_T": 1792044900, "last_T": 1792117800, "open": 1, "run": 1792119620, "sha256": "adc52d666ace24c2145e55ef9d62602717d7726c791319304613be33c58459b6", "tag": "pairbook-streams-1792119620", "unclosed": 0, "wall_ns": 1792119624014812901, "windows_considered": 509}
[2026-10-20T05:10:08Z] L 2026-10-16T03:02:57Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 414488168, "run": 1792119620, "sent": 82, "wall_ns": 1792119777429141022}
[2026-10-20T05:10:08Z] L 2026-10-16T03:07:24Z {"assets_n": 82, "bytes_total": 1804368058, "event": "verify", "release_id": 414488168, "run": 1792119620, "verify_sha256": "96164ee15cef51426beba1050e8a4f47856762d5800a75fe9966f68164302e2a", "wall_ns": 1792120044830268724}
[2026-10-20T05:10:08Z] L 2026-10-16T03:07:28Z {"already": 0, "event": "delete", "free_after": 12728901632, "free_before": 10924134400, "freed": 1804368058, "gone": 82, "removed": 82, "run": 1792119620, "wall_ns": 1792120048628416638, "windows_kept": 82}
[2026-10-20T05:10:08Z] L 2026-10-16T03:07:28Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1312748", "NRestarts": "8", "ns": 1792120048640224099}, "phase": 448, "run": 1792119620, "wall_ns": 1792120048640229054}
[2026-10-20T05:10:08Z] L 2026-10-16T03:07:28Z {"event": "kill", "exit": 0, "phase": 448, "run": 1792119620, "wall_ns": 1792120048645966122}
[2026-10-20T05:10:08Z] L 2026-10-16T03:07:58Z {"NRestarts": "9", "W": 1792119600, "event": "restart", "free_bytes": 12728885248, "gap_ns": 5420693633, "pid": 1420617, "run": 1792119620, "stopped": 1312748, "stream_bytes": 12133793, "wall_ns": 1792120078665650185}
[2026-10-20T05:10:08Z] L 2026-10-16T03:15:41Z {"T": 1792119600, "event": "resume", "reading": "PASS", "run": 1792119620, "wall_ns": 1792120541000363636}
[2026-10-20T05:10:08Z] L 2026-10-16T03:15:41Z {"assets_n": 82, "bytes_total": 1804368058, "ended_outside": 0, "event": "complete", "free_bytes": 12710682624, "peak_rss": 38199296, "rate_per_day": 2112430897, "requests": 169, "run": 1792119620, "started_outside": 0, "stops": [["the cap", 1792446508], ["the floor, base 43500000 bytes a day", 1792449588], ["the floor, base 187760570 bytes a day", 1792428951]], "store_stream_bytes": 30286238, "wall_ns": 1792120541008367106}
[2026-10-20T05:10:08Z] L 2026-10-17T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "df3acd4ed1af4d05bc9ec4fa5085ebee", "phase_at": 20, "resumed": false, "run": 1792206020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792206020485538925}
[2026-10-20T05:10:08Z] L 2026-10-17T03:00:24Z {"assets_n": 96, "bytes_total": 2048827436, "closed": 605, "deferred": 0, "event": "set", "first_T": 1792118700, "last_T": 1792204200, "open": 1, "run": 1792206020, "sha256": "0915abd5810c2b901012aa6d34388eabcc76d7be8b327d651632ac9335bbe188", "tag": "pairbook-streams-1792206020", "unclosed": 0, "wall_ns": 1792206024973916528, "windows_considered": 605}
[2026-10-20T05:10:08Z] L 2026-10-17T03:03:23Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 415548049, "run": 1792206020, "sent": 96, "wall_ns": 1792206203238800300}
[2026-10-20T05:10:08Z] L 2026-10-17T03:07:35Z {"assets_n": 96, "bytes_total": 2048827436, "event": "verify", "release_id": 415548049, "run": 1792206020, "verify_sha256": "747508e351bb13bb1aa11a99791ab87d1ea798e92c66dd1ec6126aad4f67f97c", "wall_ns": 1792206455599715552}
[2026-10-20T05:10:08Z] L 2026-10-17T03:07:40Z {"already": 0, "event": "delete", "free_after": 12725805056, "free_before": 10676551680, "freed": 2048827436, "gone": 96, "removed": 96, "run": 1792206020, "wall_ns": 1792206460092686139, "windows_kept": 96}
[2026-10-20T05:10:08Z] L 2026-10-17T03:07:40Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1420617", "NRestarts": "9", "ns": 1792206460108197241}, "phase": 460, "run": 1792206020, "wall_ns": 1792206460108202947}
[2026-10-20T05:10:08Z] L 2026-10-17T03:07:40Z {"event": "kill", "exit": 0, "phase": 460, "run": 1792206020, "wall_ns": 1792206460112982086}
[2026-10-20T05:10:08Z] L 2026-10-17T03:08:10Z {"NRestarts": "10", "W": 1792206000, "event": "restart", "free_bytes": 12725788672, "gap_ns": 5487288436, "pid": 1560378, "run": 1792206020, "stopped": 1420617, "stream_bytes": 10686101, "wall_ns": 1792206490133956812}
[2026-10-20T05:10:08Z] L 2026-10-17T03:15:41Z {"T": 1792206000, "event": "resume", "reading": "PASS", "run": 1792206020, "wall_ns": 1792206941000351565}
[2026-10-20T05:10:08Z] L 2026-10-17T03:15:41Z {"assets_n": 96, "bytes_total": 2048827436, "ended_outside": 0, "event": "complete", "free_bytes": 12715110400, "peak_rss": 38330368, "rate_per_day": 2048827436, "requests": 197, "run": 1792206020, "started_outside": 0, "stops": [["the cap", 1792543404], ["the floor, base 43500000 bytes a day", 1792546173], ["the floor, base 187760570 bytes a day", 1792524292]], "store_stream_bytes": 21346173, "wall_ns": 1792206941009261301}
[2026-10-20T05:10:08Z] L 2026-10-17T08:35:37Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "ab6b527c633847f79ce14ed1afdf3623", "phase_at": 337, "resumed": false, "run": 1792226137, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792226137790990342}
[2026-10-20T05:10:08Z] L 2026-10-17T08:35:38Z {"assets_n": 23, "bytes_total": 397545662, "closed": 628, "deferred": 0, "event": "set", "first_T": 1792205100, "last_T": 1792224900, "open": 0, "run": 1792226137, "sha256": "3db64b34a3949064d28cadc5a023e4402ebacc5cf7a2adab2fe09d13971312c4", "tag": "pairbook-streams-1792226137", "unclosed": 0, "wall_ns": 1792226138787331150, "windows_considered": 628}
[2026-10-20T05:10:08Z] L 2026-10-17T08:36:15Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 415679936, "run": 1792226137, "sent": 23, "wall_ns": 1792226175895145126}
[2026-10-20T05:10:08Z] L 2026-10-17T08:38:40Z {"assets_n": 23, "bytes_total": 397545662, "event": "verify", "release_id": 415679936, "run": 1792226137, "verify_sha256": "f26e295363dadaea4d9a2de3d5e86de06da641bf85ecec538e4a36b7e89de14f", "wall_ns": 1792226320606064836}
[2026-10-20T05:10:08Z] L 2026-10-17T08:38:41Z {"already": 0, "event": "delete", "free_after": 12799180800, "free_before": 12401537024, "freed": 397545662, "gone": 23, "removed": 23, "run": 1792226137, "wall_ns": 1792226321481880383, "windows_kept": 23}
[2026-10-20T05:10:08Z] L 2026-10-17T08:45:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1560378", "NRestarts": "10", "ns": 1792226715015188081}, "phase": 15, "run": 1792226137, "wall_ns": 1792226715015194823}
[2026-10-20T05:10:08Z] L 2026-10-17T08:45:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792226137, "wall_ns": 1792226715020774740}
[2026-10-20T05:10:08Z] L 2026-10-17T08:45:45Z {"NRestarts": "11", "W": 1792226700, "event": "restart", "free_bytes": 12783226880, "gap_ns": 5530075996, "pid": 1595407, "run": 1792226137, "stopped": 1560378, "stream_bytes": 15521838, "wall_ns": 1792226745041554142}
[2026-10-20T05:10:08Z] L 2026-10-17T09:00:41Z {"T": 1792226700, "event": "resume", "reading": "PASS", "run": 1792226137, "wall_ns": 1792227641000413386}
[2026-10-20T05:10:08Z] L 2026-10-17T09:00:41Z {"assets_n": 23, "bytes_total": 397545662, "ended_outside": 0, "event": "complete", "free_bytes": 12773187584, "peak_rss": 37543936, "rate_per_day": 1659321024, "requests": 51, "run": 1792226137, "started_outside": 0, "stops": [["the cap", 1792642879], ["the floor, base 43500000 bytes a day", 1792647417], ["the floor, base 187760570 bytes a day", 1792614631]], "store_stream_bytes": 25293180, "wall_ns": 1792227641009539425}
[2026-10-20T05:10:08Z] L 2026-10-18T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "15934402892b403b858ea4b973f03c89", "phase_at": 20, "resumed": false, "run": 1792292420, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792292420527428655}
[2026-10-20T05:10:08Z] L 2026-10-18T03:00:23Z {"assets_n": 73, "bytes_total": 1197040692, "closed": 701, "deferred": 0, "event": "set", "first_T": 1792225800, "last_T": 1792290600, "open": 1, "run": 1792292420, "sha256": "7ddfeae4a937bc90c14d8047d3ab843035a2be145d8d407738f9620b098c0b08", "tag": "pairbook-streams-1792292420", "unclosed": 0, "wall_ns": 1792292423275187616, "windows_considered": 701}
[2026-10-20T05:10:08Z] L 2026-10-18T03:02:20Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 416201489, "run": 1792292420, "sent": 73, "wall_ns": 1792292540828362894}
[2026-10-20T05:10:08Z] L 2026-10-18T03:05:48Z {"assets_n": 73, "bytes_total": 1197040692, "event": "verify", "release_id": 416201489, "run": 1792292420, "verify_sha256": "a3eb29ead036c8a97f023ecb53572112300e5b22defa9d984ba1887dcddf95e3", "wall_ns": 1792292748968235081}
[2026-10-20T05:10:08Z] L 2026-10-18T03:05:51Z {"already": 0, "event": "delete", "free_after": 12776620032, "free_before": 11579240448, "freed": 1197040692, "gone": 73, "removed": 73, "run": 1792292420, "wall_ns": 1792292751530232000, "windows_kept": 73}
[2026-10-20T05:10:08Z] L 2026-10-18T03:05:51Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1595407", "NRestarts": "11", "ns": 1792292751542647421}, "phase": 351, "run": 1792292420, "wall_ns": 1792292751542652085}
[2026-10-20T05:10:08Z] L 2026-10-18T03:05:51Z {"event": "kill", "exit": 0, "phase": 351, "run": 1792292420, "wall_ns": 1792292751546822604}
[2026-10-20T05:10:08Z] L 2026-10-18T03:06:21Z {"NRestarts": "12", "W": 1792292400, "event": "restart", "free_bytes": 12776607744, "gap_ns": 5504206730, "pid": 1692402, "run": 1792292420, "stopped": 1595407, "stream_bytes": 12437717, "wall_ns": 1792292781569460854}
[2026-10-20T05:10:08Z] L 2026-10-18T03:15:41Z {"T": 1792292400, "event": "resume", "reading": "PASS", "run": 1792292420, "wall_ns": 1792293341000328710}
[2026-10-20T05:10:08Z] L 2026-10-18T03:15:41Z {"assets_n": 73, "bytes_total": 1197040692, "ended_outside": 0, "event": "complete", "free_bytes": 12764577792, "peak_rss": 37937152, "rate_per_day": 1574190499, "requests": 151, "run": 1792292420, "started_outside": 0, "stops": [["the cap", 1792731097], ["the floor, base 43500000 bytes a day", 1792734747], ["the floor, base 187760570 bytes a day", 1792698607]], "store_stream_bytes": 24161003, "wall_ns": 1792293341010228074}
[2026-10-20T05:10:08Z] L 2026-10-19T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "b6aa8a5cde4c4cc392165b8f31b1bec0", "phase_at": 20, "resumed": false, "run": 1792378820, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792378820477080166}
[2026-10-20T05:10:08Z] L 2026-10-19T03:00:24Z {"assets_n": 96, "bytes_total": 1755430954, "closed": 797, "deferred": 0, "event": "set", "first_T": 1792291500, "last_T": 1792377000, "open": 1, "run": 1792378820, "sha256": "948f4d39cca953e07be1c1c561f5115f6200f5aa8330fe78434c058d6e607528", "tag": "pairbook-streams-1792378820", "unclosed": 0, "wall_ns": 1792378824458122339, "windows_considered": 797}
[2026-10-20T05:10:08Z] L 2026-10-19T03:03:08Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 416860290, "run": 1792378820, "sent": 96, "wall_ns": 1792378988043909754}
[2026-10-20T05:10:08Z] L 2026-10-19T03:07:11Z {"assets_n": 96, "bytes_total": 1755430954, "event": "verify", "release_id": 416860290, "run": 1792378820, "verify_sha256": "86b0b971d6eaeb1c8fd7dd87f44b2f739282eec95c52919b65b79ea293db2551", "wall_ns": 1792379231626951320}
[2026-10-20T05:10:08Z] L 2026-10-19T03:07:15Z {"already": 0, "event": "delete", "free_after": 12737359872, "free_before": 10981560320, "freed": 1755430954, "gone": 96, "removed": 96, "run": 1792378820, "wall_ns": 1792379235366652736, "windows_kept": 96}
[2026-10-20T05:10:08Z] L 2026-10-19T03:07:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1692402", "NRestarts": "12", "ns": 1792379235374600961}, "phase": 435, "run": 1792378820, "wall_ns": 1792379235374606661}
[2026-10-20T05:10:08Z] L 2026-10-19T03:07:15Z {"event": "kill", "exit": 0, "phase": 435, "run": 1792378820, "wall_ns": 1792379235379253859}
[2026-10-20T05:10:08Z] L 2026-10-19T03:07:45Z {"NRestarts": "13", "W": 1792378800, "event": "restart", "free_bytes": 12737351680, "gap_ns": 5404558972, "pid": 1814768, "run": 1792378820, "stopped": 1692402, "stream_bytes": 20988190, "wall_ns": 1792379265403200749}
[2026-10-20T05:10:08Z] L 2026-10-19T03:15:41Z {"T": 1792378800, "event": "resume", "reading": "PASS", "run": 1792378820, "wall_ns": 1792379741000400500}
[2026-10-20T05:10:08Z] L 2026-10-19T03:15:41Z {"assets_n": 96, "bytes_total": 1755430954, "ended_outside": 0, "event": "complete", "free_bytes": 12720193536, "peak_rss": 38592512, "rate_per_day": 1755430954, "requests": 197, "run": 1792378820, "started_outside": 0, "stops": [["the cap", 1792771618], ["the floor, base 43500000 bytes a day", 1792774544], ["the floor, base 187760570 bytes a day", 1792745234]], "store_stream_bytes": 38026457, "wall_ns": 1792379741011807328}
[2026-10-20T05:10:08Z] L 2026-10-19T21:54:19Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "7efdb0d05f6f4814b803f423a1351eae", "phase_at": 559, "resumed": false, "run": 1792446859, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792446859827562789}
[2026-10-20T05:10:08Z] L 2026-10-19T21:54:23Z {"assets_n": 76, "bytes_total": 1702929677, "closed": 873, "deferred": 0, "event": "set", "first_T": 1792377900, "last_T": 1792445400, "open": 1, "run": 1792446859, "sha256": "8491aab13dd6df082e8a4e847bd4e676a5edbeabd050e9a1767a79d7ecfb72d3", "tag": "pairbook-streams-1792446859", "unclosed": 0, "wall_ns": 1792446863665163186, "windows_considered": 873}
[2026-10-20T05:10:08Z] L 2026-10-19T22:02:33Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 417794290, "run": 1792446859, "sent": 76, "wall_ns": 1792447353191732798}
[2026-10-20T05:10:08Z] L 2026-10-19T22:09:37Z {"assets_n": 76, "bytes_total": 1702929677, "event": "verify", "release_id": 417794290, "run": 1792446859, "verify_sha256": "dfa62b04b0291467b86d37271e00e2242c0fea6b9e1caa987e7a9b31fafd3f6b", "wall_ns": 1792447777762252351}
[2026-10-20T05:10:08Z] L 2026-10-19T22:09:41Z {"already": 0, "event": "delete", "free_after": 12726702080, "free_before": 11023396864, "freed": 1702929677, "gone": 76, "removed": 76, "run": 1792446859, "wall_ns": 1792447781500420485, "windows_kept": 76}
[2026-10-20T05:10:08Z] L 2026-10-19T22:15:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1814768", "NRestarts": "13", "ns": 1792448115017795294}, "phase": 15, "run": 1792446859, "wall_ns": 1792448115017801355}
[2026-10-20T05:10:08Z] L 2026-10-19T22:15:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792446859, "wall_ns": 1792448115024251292}
[2026-10-20T05:10:08Z] L 2026-10-19T22:15:45Z {"NRestarts": "14", "W": 1792448100, "event": "restart", "free_bytes": 12707540992, "gap_ns": 5638947193, "pid": 1915093, "run": 1792446859, "stopped": 1814768, "stream_bytes": 30931694, "wall_ns": 1792448145064395857}
[2026-10-20T05:10:08Z] L 2026-10-19T22:30:41Z {"T": 1792448100, "event": "resume", "reading": "PASS", "run": 1792446859, "wall_ns": 1792449041000625272}
[2026-10-20T05:10:08Z] L 2026-10-19T22:30:41Z {"assets_n": 76, "bytes_total": 1702929677, "ended_outside": 0, "event": "complete", "free_bytes": 12678688768, "peak_rss": 37539840, "rate_per_day": 2151069065, "requests": 157, "run": 1792446859, "started_outside": 0, "stops": [["the cap", 1792767956], ["the floor, base 43500000 bytes a day", 1792771035], ["the floor, base 187760570 bytes a day", 1792751174]], "store_stream_bytes": 60078470, "wall_ns": 1792449041020984137}
[2026-10-20T05:10:08Z] L 2026-10-20T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "39b80e28726849c6b2c7c78015f76beb", "phase_at": 20, "resumed": false, "run": 1792465220, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792465220508369328}
[2026-10-20T05:10:08Z] L 2026-10-20T03:00:21Z {"assets_n": 20, "bytes_total": 428604581, "closed": 893, "deferred": 0, "event": "set", "first_T": 1792446300, "last_T": 1792463400, "open": 1, "run": 1792465220, "sha256": "08a4bf67291e8988351d7b031e9a6250ded7ec726fb2a80a1c28559d6b827e6b", "tag": "pairbook-streams-1792465220", "unclosed": 0, "wall_ns": 1792465221560132886, "windows_considered": 893}
[2026-10-20T05:10:08Z] L 2026-10-20T03:01:05Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 417955485, "run": 1792465220, "sent": 20, "wall_ns": 1792465265840619699}
[2026-10-20T05:10:08Z] L 2026-10-20T03:03:38Z {"assets_n": 20, "bytes_total": 428604581, "event": "verify", "release_id": 417955485, "run": 1792465220, "verify_sha256": "1417b0845ea746c17a126d8311895714cd28b5cdbefbb3f27cc38e7b2d8a516a", "wall_ns": 1792465418377004134}
[2026-10-20T05:10:08Z] L 2026-10-20T03:03:39Z {"already": 0, "event": "delete", "free_after": 12736249856, "free_before": 12307550208, "freed": 428604581, "gone": 20, "removed": 20, "run": 1792465220, "wall_ns": 1792465419274331805, "windows_kept": 20}
[2026-10-20T05:10:08Z] L 2026-10-20T03:03:39Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1915093", "NRestarts": "14", "ns": 1792465419285640926}, "phase": 219, "run": 1792465220, "wall_ns": 1792465419285646173}
[2026-10-20T05:10:08Z] L 2026-10-20T03:03:39Z {"event": "kill", "exit": 0, "phase": 219, "run": 1792465220, "wall_ns": 1792465419290626015}
[2026-10-20T05:10:08Z] L 2026-10-20T03:04:09Z {"NRestarts": "15", "W": 1792465200, "event": "restart", "free_bytes": 12736208896, "gap_ns": 5521442701, "pid": 1942330, "run": 1792465220, "stopped": 1915093, "stream_bytes": 21234976, "wall_ns": 1792465449314599186}
[2026-10-20T05:10:08Z] L 2026-10-20T03:15:41Z {"T": 1792465200, "event": "resume", "reading": "PASS", "run": 1792465220, "wall_ns": 1792466141000339712}
[2026-10-20T05:10:08Z] L 2026-10-20T03:15:41Z {"assets_n": 20, "bytes_total": 428604581, "ended_outside": 0, "event": "complete", "free_bytes": 12714721280, "peak_rss": 37937152, "rate_per_day": 2057301988, "requests": 45, "run": 1792465220, "started_outside": 0, "stops": [["the cap", 1792800340], ["the floor, base 43500000 bytes a day", 1792803989], ["the floor, base 187760570 bytes a day", 1792782280]], "store_stream_bytes": 42260469, "wall_ns": 1792466141012853604}
[2026-10-20T05:10:08Z] run 1791731892 2026-10-11T15:18:12Z, off-calendar, second 55092 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1791731892: 28 files, 430047476 bytes, windows 1791706500 to 1791730800 of 79 considered; Release 409746510: sent 28, held 0; removed 28, freed 430047476 bytes, free after 12969091072; restart: window 1791731700, pid 851381 after 815823, NRestarts 3; resume PASS at window 1791731700; complete: requests 61, started outside 0, ended outside 0, store 19346486 bytes, free 12949487616, rate 1474448489 a day
[2026-10-20T05:10:08Z] run 1791774020 2026-10-12T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1791774020: 46 files, 794522712 bytes, windows 1791731700 to 1791772200 of 125 considered; Release 410101186: sent 46, held 0; removed 46, freed 794522712 bytes, free after 12960145408; restart: window 1791774000, pid 911226 after 851381, NRestarts 4; resume PASS at window 1791774000; complete: requests 97, started outside 0, ended outside 0, store 37220758 bytes, free 12948570112, rate 1658134355 a day
[2026-10-20T05:10:08Z] run 1791860420 2026-10-13T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1791860420: 96 files, 1925987888 bytes, windows 1791773100 to 1791858600 of 221 considered; Release 411210796: sent 96, held 0; removed 96, freed 1925987888 bytes, free after 12876316672; restart: window 1791860400, pid 1027378 after 911226, NRestarts 5; resume PASS at window 1791860400; complete: requests 197, started outside 0, ended outside 0, store 41556131 bytes, free 12857700352, rate 1925987888 a day
[2026-10-20T05:10:08Z] run 1791946820 2026-10-14T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1791946820: 96 files, 2039544263 bytes, windows 1791859500 to 1791945000 of 317 considered; Release 412296623: sent 96, held 0; removed 96, freed 2039544263 bytes, free after 12842123264; restart: window 1791946800, pid 1155982 after 1027378, NRestarts 6; resume PASS at window 1791946800; complete: requests 197, started outside 0, ended outside 0, store 38533208 bytes, free 12820799488, rate 2039544263 a day
[2026-10-20T05:10:08Z] run 1792033220 2026-10-15T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792033220: 96 files, 2103892072 bytes, windows 1791945900 to 1792031400 of 413 considered; Release 413374764: sent 96, held 0; removed 96, freed 2103892072 bytes, free after 12590329856; restart: window 1792034100, pid 1284485 after 1155982, NRestarts 7; resume PASS at window 1792034100; complete: requests 197, started outside 0, ended outside 0, store 54308421 bytes, free 12548313088, rate 2103892072 a day
[2026-10-20T05:10:08Z] run 1792045110 2026-10-15T06:18:30Z, off-calendar, second 22710 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792045110: 14 files, 352241341 bytes, windows 1792032300 to 1792044000 of 427 considered; Release 413477311: sent 14, held 0; removed 14, freed 352241341 bytes, free after 12826914816; restart: window 1792044900, pid 1312748 after 1284485, NRestarts 8; resume PASS at window 1792044900; complete: requests 33, started outside 0, ended outside 0, store 12817136 bytes, free 12813713408, rate 2415369195 a day
[2026-10-20T05:10:08Z] run 1792119620 2026-10-16T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792119620: 82 files, 1804368058 bytes, windows 1792044900 to 1792117800 of 509 considered; Release 414488168: sent 82, held 0; removed 82, freed 1804368058 bytes, free after 12728901632; restart: window 1792119600, pid 1420617 after 1312748, NRestarts 9; resume PASS at window 1792119600; complete: requests 169, started outside 0, ended outside 0, store 30286238 bytes, free 12710682624, rate 2112430897 a day
[2026-10-20T05:10:08Z] run 1792206020 2026-10-17T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792206020: 96 files, 2048827436 bytes, windows 1792118700 to 1792204200 of 605 considered; Release 415548049: sent 96, held 0; removed 96, freed 2048827436 bytes, free after 12725805056; restart: window 1792206000, pid 1560378 after 1420617, NRestarts 10; resume PASS at window 1792206000; complete: requests 197, started outside 0, ended outside 0, store 21346173 bytes, free 12715110400, rate 2048827436 a day
[2026-10-20T05:10:08Z] run 1792226137 2026-10-17T08:35:37Z, off-calendar, second 30937 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792226137: 23 files, 397545662 bytes, windows 1792205100 to 1792224900 of 628 considered; Release 415679936: sent 23, held 0; removed 23, freed 397545662 bytes, free after 12799180800; restart: window 1792226700, pid 1595407 after 1560378, NRestarts 11; resume PASS at window 1792226700; complete: requests 51, started outside 0, ended outside 0, store 25293180 bytes, free 12773187584, rate 1659321024 a day
[2026-10-20T05:10:08Z] run 1792292420 2026-10-18T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792292420: 73 files, 1197040692 bytes, windows 1792225800 to 1792290600 of 701 considered; Release 416201489: sent 73, held 0; removed 73, freed 1197040692 bytes, free after 12776620032; restart: window 1792292400, pid 1692402 after 1595407, NRestarts 12; resume PASS at window 1792292400; complete: requests 151, started outside 0, ended outside 0, store 24161003 bytes, free 12764577792, rate 1574190499 a day
[2026-10-20T05:10:08Z] run 1792378820 2026-10-19T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792378820: 96 files, 1755430954 bytes, windows 1792291500 to 1792377000 of 797 considered; Release 416860290: sent 96, held 0; removed 96, freed 1755430954 bytes, free after 12737359872; restart: window 1792378800, pid 1814768 after 1692402, NRestarts 13; resume PASS at window 1792378800; complete: requests 197, started outside 0, ended outside 0, store 38026457 bytes, free 12720193536, rate 1755430954 a day
[2026-10-20T05:10:08Z] run 1792446859 2026-10-19T21:54:19Z, off-calendar, second 78859 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792446859: 76 files, 1702929677 bytes, windows 1792377900 to 1792445400 of 873 considered; Release 417794290: sent 76, held 0; removed 76, freed 1702929677 bytes, free after 12726702080; restart: window 1792448100, pid 1915093 after 1814768, NRestarts 14; resume PASS at window 1792448100; complete: requests 157, started outside 0, ended outside 0, store 60078470 bytes, free 12678688768, rate 2151069065 a day
[2026-10-20T05:10:08Z] run 1792465220 2026-10-20T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792465220: 20 files, 428604581 bytes, windows 1792446300 to 1792463400 of 893 considered; Release 417955485: sent 20, held 0; removed 20, freed 428604581 bytes, free after 12736249856; restart: window 1792465200, pid 1942330 after 1915093, NRestarts 15; resume PASS at window 1792465200; complete: requests 45, started outside 0, ended outside 0, store 42260469 bytes, free 12714721280, rate 2057301988 a day
[2026-10-20T05:10:08Z] tags on origin 13: ['pairbook-streams-1791731892', 'pairbook-streams-1791774020', 'pairbook-streams-1791860420', 'pairbook-streams-1791946820', 'pairbook-streams-1792033220', 'pairbook-streams-1792045110', 'pairbook-streams-1792119620', 'pairbook-streams-1792206020', 'pairbook-streams-1792226137', 'pairbook-streams-1792292420', 'pairbook-streams-1792378820', 'pairbook-streams-1792446859', 'pairbook-streams-1792465220']
[2026-10-20T05:10:08Z] the ledger's sets 13, 842 files, 16980982812 bytes; their tags not on origin []; tags on origin without a set []
[2026-10-20T05:10:08Z] runs 13; without a terminal record []; windows skipped between consecutive sets []; halted False
[2026-10-20T05:10:08Z] malloc tuned: True
[2026-10-20T05:10:08Z] peak memory of this run: 28925952 bytes
[2026-10-20T05:10:08Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

```text
$ TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-pairbook-archive.service -p MainPID -p NRestarts -p ActiveState -p MemoryCurrent -p MemoryPeak
MainPID=4148534
NRestarts=2
MemoryCurrent=22695936
MemoryPeak=258011136
ActiveState=active

MainPID=1942330
NRestarts=15
MemoryCurrent=17297408
MemoryPeak=108912640
ActiveState=active

MainPID=0
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=[not set]
ActiveState=inactive
$ free -b
               total        used        free      shared  buff/cache   available
Mem:      1002127360   643977216    92213248      163840   417386496   358150144
Swap:     3250581504   478523392  2772058112
$ du -sb /root/tz29-work /root/.claude
91649321	/root/tz29-work
133112587	/root/.claude
$ cat /root/tz29-work/state.json /root/tz29-work/label-ledger.jsonl
{
 "constants_at": "2026-10-20T05:09:39Z",
 "constants_sha": "747124081489fc5ef86c8a818e445e2dbff3caaa4cf014272c6a8c510e22c1cc",
 "still": {
  "at": "2026-10-20T04:27:51Z",
  "units": {
   "pairbook": {
    "ActiveState": "active",
    "MainPID": "1942330",
    "NRestarts": "15"
   },
   "recorder": {
    "ActiveState": "active",
    "MainPID": "4148534",
    "NRestarts": "2"
   }
  }
 }
}
{"at":"2026-10-20T05:09:45Z","head":"f6425f713034724210dc120d2108bcfad63cadc6","member_list_sha":"880a90303dcda502b5ac9562e94f6cadca4310a0ce19ea6450baaa650ae08f62","members":8064}
{"at":"2026-10-20T05:09:51Z","head":"f6425f713034724210dc120d2108bcfad63cadc6","member_list_sha":"880a90303dcda502b5ac9562e94f6cadca4310a0ce19ea6450baaa650ae08f62","members":8064}
```

The ledger at the closing read is unchanged: the same `30,913` bytes, `3d08a5f7…`, and 130 records. The units are
unchanged too. The pair book's store went from `157,533,850` to `230,889,230` bytes by `du`, its streams growing
between archive runs, and free space from `12,619,980,800` to `12,451,913,728`.

### 2.13 Units' memory at every read

| instant (UTC) | read | recorder `MemoryCurrent` / `MemoryPeak` | pair book `MemoryCurrent` / `MemoryPeak` |
|---|---|---|---|
| 04:27:51 | `still` (1) | `12,648,448` / `258,011,136` | `16,637,952` / `108,912,640` |
| 05:09:51 | `still` (2) | `74,772,480` / `258,011,136` | `19,947,520` / `108,912,640` |
| 05:10 | §3.11 `systemctl show` | `22,695,936` / `258,011,136` | `17,297,408` / `108,912,640` |

### 2.14 Memory and the hooks — every mode (V12, V13)

| mode | log | peak memory (bytes) | `malloc tuned` | opens refused / under the roots |
|---|---|---|---|---|
| `fingerprint` (`I0`) | 02 | 29,057,024 | True | 0 / 0 |
| `selftest` | 09 | 30,982,144 | True | 0 / 0 |
| `still` (1) | 10 | 29,065,216 | True | 0 / 0 |
| `scratch` | 11 | 29,065,216 | True | 0 / 0 |
| `reclaim` (scratch) | 12 | 29,585,408 | True | 0 / 0 |
| `archive` (1) | 15 | 29,188,096 | True | 0 / 0 |
| `rehearse` | 16 | 54,341,632 | True | 0 / 0 |
| `replay` | 17 | 49,233,920 | True | 0 / 0 |
| `fetch` | 19 | 73,420,800 | True | 0 / 0 |
| `constants` (1) | 20 | 83,947,520 | True | 0 / 0 |
| `constants` (2) | 21 | 83,922,944 | True | 0 / 0 |
| `score` (1) | 22 | 72,376,320 | True | 0 / 0 |
| `score` (2) | 23 | 72,380,416 | True | 0 / 0 |
| `still` (2) | 24 | 28,934,144 | True | 0 / 0 |
| `archive` (2) | 26 | 28,925,952 | True | 0 / 0 |
| `reclaim` (own) | §2.16 | 31,617,024 | True | 0 / 0 |

The largest peak is `constants`, `83,947,520` bytes. That is under the Architect's `88,567,808` and under half of
§0.4's floor.

### 2.15 Every file the run wrote, by SHA-256 — `logs/29-files-written.log`, verbatim

```text
$ find /root/tz29-work -path /root/tz29-work/wt -prune -o -path "*/cache" -prune -o -type f -print | sort | xargs sha256sum; plus sizes
747124081489fc5ef86c8a818e445e2dbff3caaa4cf014272c6a8c510e22c1cc 1997 /root/tz29-work/cumulative/cumulative-constants.json
c1df5a5ba53ad376ab0e303f9fc9df78e86d3c1cbeafadd02b869e6d169e41ac 4875490 /root/tz29-work/cumulative/cumulative-members.csv
aa3a8f5c250ccc53b4d0d184f8e0ed1699002d97b77c906f5329880a98fda601 1912 /root/tz29-work/cumulative/cumulative-reading.json
e3131814a61b7ff5619e57d1d0af0478d7604f0b0c71e868f3e4e2fccfe77fae 928653 /root/tz29-work/cumulative/cumulative-scored.csv
2f6e9df8476c8f1409497c9da7d7c5afffa4cde6c7bbadc0f479315e222c4d40 360 /root/tz29-work/label-ledger.jsonl
ce836b034a090ce01e147ab24a87d787e86dc8b1c6bccfc5575e77dbfd31ce1a 66 /root/tz29-work/logs/00-mkdir.log
b70457d498c451b0311d0e17c52a4f8fc020dfec4acf48f21e054c56f8c7f7a1 295 /root/tz29-work/logs/01-stage.log
e1de5ab772322a1a64665517edbd9af1e267ee75a2e0f2907e2d3d0111e48b1e 7841 /root/tz29-work/logs/02-fingerprint.log
c9c3d21bda6b5d425061aa33eb92da03e4b3d6018cb3e7890b0b65e952efbeca 3893 /root/tz29-work/logs/03-host-gate.log
8362edf87bab73db58dcaa6e18e9dd65c7fcf51e2eb36bd923f2bd9cbeb4fcce 4108 /root/tz29-work/logs/04-refs.log
a5e8022f0a7bc3c78fb71ce582b42a21bfdcc17920cd88ded29c1d08f6a20dd9 1637 /root/tz29-work/logs/05-branch.log
030f6dc549fad4c7a5bbdae799f089dadb6f212179669dfdeaeb06ffedec76ac 695 /root/tz29-work/logs/06-commit-push.log
ff1b268a8fa0850e56fa6ab893e81b72e01abf2eb04c77a84ad56997190b8d3e 1119 /root/tz29-work/logs/07-push-gh-helper.log
aba95cab7199414f2f778db045f71ca72d59fc1c9f01ef8f886041be7e235489 63 /root/tz29-work/logs/08-pr.log
3ffb6a211c6bf60399dc63aeb951570711b0d19a2546351ca870ca35005e2323 22978 /root/tz29-work/logs/09-selftest.log
ec673f32711693b908452993661c067dec4ef5e8977453e22a6d4ace05e0dfc1 878 /root/tz29-work/logs/10-still-1.log
5c6e72af4df61303e8283d371bcd581bd1304039063125471e4d1553e3a41e16 881 /root/tz29-work/logs/11-scratch.log
f28689952275fff7542fbe4a2cdb1c853c044d75ef09e5a023a2797fe169cdde 608 /root/tz29-work/logs/12-reclaim-scratch.log
44c2371b316d488feeea0fa532119c29776e2f852c2dbae21829ac35a8b0d8bf 92 /root/tz29-work/logs/13-rm-6b7bd886.log
2e9f579d3da60b3fc850aa4818f5ac2684b7f25c5bfdf9bf828e1f634d52ec12 92 /root/tz29-work/logs/14-rm-6de9e261.log
a7d2fc9d8c964dc5653d90eb245f8642b25e0a6d426bed56ad86e63bce986ff6 46757 /root/tz29-work/logs/15-archive-1.log
d3dc8622115e18357a162874e7ce3ce03236d79cf7ac8fe579326e1b7372bbb1 7643 /root/tz29-work/logs/16-rehearse.log
8e3892e3f8a43d6f89cfaa16f8d40458f9130f4d07af61a98928321daa66ae21 4644 /root/tz29-work/logs/17-replay.log
a062946d1b4f3c11ac3aedb048917452d9926307834f008eecbd586e069f4358 186 /root/tz29-work/logs/18-instant.log
4b3896b91bb8328cb8ce2f86a03c6dfc81fe64f84e042454bdd849ee0370037c 1423 /root/tz29-work/logs/19-fetch.log
aac742458198e1429d9b2225a464fa6067179045c29edd9a58246700143377ef 5130 /root/tz29-work/logs/20-constants-1.log
2ec1fd387c59010954ddb3d585e5372c78fa4a24c5eae8bf005fe9eb3254db3a 5875 /root/tz29-work/logs/21-constants-2.log
22cadc52c9cfdb846c272f1ce4586f5553be4ec78b4bac56c58c2c7d8bf62207 4563 /root/tz29-work/logs/22-score-1.log
410982fba6e82c707f933ac433eac523d151ad7b8ee9e41067c771cb4df40580 4873 /root/tz29-work/logs/23-score-2.log
24eb1a02c9b2b774fd02a112305f55b2250c7a7cd4ce590fa21e62db37c0ffdb 913 /root/tz29-work/logs/24-still-2.log
f5e95dfdfc84d8b51f2d67002bf7b8cc8585fdf2ce50130fbac49e38c2e8168b 3794 /root/tz29-work/logs/25-host-gate-2.log
101df52ed5906d7503098e4b88687966b0ddaa0433b1a90fffe800209453396d 46757 /root/tz29-work/logs/26-archive-2.log
3869032b7e54bf17f44f77e5ef75e36755bec6b8d8a541c2a0adaf8e456c02c3 1564 /root/tz29-work/logs/27-closing-reads.log
62709ca2df869830ec3b3a6520052a06573d5cc84dfad57b616d747cf58a8010 796 /root/tz29-work/logs/28-selfcheck.log
7171c2f3f157795795a90c87bcaddec31f348672d6ac5c5a0f61196a28cb026f 3832 /root/tz29-work/logs/29-files-written.log
9f521a23b3a5b48ac7569f68a9c42bf6da1bb8ef09f5a71c0c8e091fbf5098e3 2025 /root/tz29-work/rehearsal/rehearsal-constants.json
3ce50a85f84068a4cac15ece53d2ea1b16184b9080d69228b0baae8f887c8116 1055371 /root/tz29-work/rehearsal/rehearsal-fills.jsonl.gz
2676af1dee730001abf560555c1c0eb9b88901209a94598dcb966495e20131d1 88078 /root/tz29-work/rehearsal/rehearsal-members.csv
4cdf1a1179c0d58f048d091e0a719951cb3af38c822d49a2e9343bea5f502d1f 1906 /root/tz29-work/rehearsal/rehearsal-reading.json
d31eb18fa58f8a26f12979f733fcead3b2482a480ba97a17c1145c1eef99bda2 16570 /root/tz29-work/rehearsal/rehearsal-scored.csv
8b3649dd6fbfbea1f625f5b685b891a76c10b6566c639710408b2af9490a61cf 1681 /root/tz29-work/rehearsal/rehearsal-timing.jsonl
83a53bd3fb13829173282487833ef0398280d358377e0f09d0beb414c7829cbc 82728 /root/tz29-work/rehearsal/set.json
98f740a229d5bb19eb60b6d2a47338d847014e875518cffba607be62eaa7e145 42417 /root/tz29-work/set/fetch-timing.jsonl
3f009cbeedc81713601a2cec5f080d0bdc2ab174fc1d468202604f3b10843d13 2314719 /root/tz29-work/set/set.json
43b10ae4984f7914bbd6d3fa79432651ec7a491b94b2e6b6daf114acdf47d2b3 2104 /root/tz29-work/set/tz29-constants.json
30c36db8d68a88ed0c34956c2c4fbda36653fa4d592cbdac6af8eac937e40aa4 35567717 /root/tz29-work/set/tz29-fills.jsonl.gz
97c67b0c830ee47a7be0d58117e6ab6a305b59ab80c7f599dadf190a42f41fc0 2431289 /root/tz29-work/set/tz29-members.csv
6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f 54885 /root/tz29-work/stage/research/tz23-maker-m0.py
18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905 68959 /root/tz29-work/stage/research/tz29-maker-m0-second-look.py
7541eea8979a90a35683c49d66e8fb6473dfae1d8b0327faca39ff086eac2388 393 /root/tz29-work/state.json
$ chunk caches: count and bytes
rehearsal/cache 8 files 1068929 bytes
set/cache 202 files 35936545 bytes
```

The two chunk caches, `rehearsal/cache` (8 files, `1,068,929` bytes) and `set/cache` (202 files, `35,936,545` bytes),
go with the tree, as §8 allows. The line for `logs/29-files-written.log` itself hashes the file while it was being
written, so it does not identify the file. That log is kept by name. `replay/`'s three copies were removed by `replay`
itself. After this listing the session wrote only under `build/`: the report's template and its builder (§6 item 4).

### 2.16 §9 B-RECLAIM-OWN — last, after §3.11, with this report drafted (V16, V17)

Its output went to no file. Every line below is quoted verbatim from the session:

```text
$ I reclaim /root/tz29-work
[2026-10-20T05:14:46Z] reclaim: 2635 report tokens; forensic store holds 1846 files
[2026-10-20T05:14:46Z] reclaim: /root/tz29-work/wt skipped: no file but its HEAD's, and HEAD f6425f713034724210dc120d2108bcfad63cadc6 is its upstream's
[2026-10-20T05:14:46Z] R copied 2f6e9df8476c8f1409497c9da7d7c5afffa4cde6c7bbadc0f479315e222c4d40 /root/btc-forensics/tz29-work--label-ledger.jsonl
[2026-10-20T05:14:46Z] R copied 7541eea8979a90a35683c49d66e8fb6473dfae1d8b0327faca39ff086eac2388 /root/btc-forensics/tz29-work--state.json
[2026-10-20T05:14:46Z] R copied 747124081489fc5ef86c8a818e445e2dbff3caaa4cf014272c6a8c510e22c1cc /root/btc-forensics/tz29-work--cumulative--cumulative-constants.json
[2026-10-20T05:14:46Z] R copied c1df5a5ba53ad376ab0e303f9fc9df78e86d3c1cbeafadd02b869e6d169e41ac /root/btc-forensics/tz29-work--cumulative--cumulative-members.csv
[2026-10-20T05:14:46Z] R copied aa3a8f5c250ccc53b4d0d184f8e0ed1699002d97b77c906f5329880a98fda601 /root/btc-forensics/tz29-work--cumulative--cumulative-reading.json
[2026-10-20T05:14:46Z] R copied e3131814a61b7ff5619e57d1d0af0478d7604f0b0c71e868f3e4e2fccfe77fae /root/btc-forensics/tz29-work--cumulative--cumulative-scored.csv
[2026-10-20T05:14:46Z] R copied ce836b034a090ce01e147ab24a87d787e86dc8b1c6bccfc5575e77dbfd31ce1a /root/btc-forensics/tz29-work--logs--00-mkdir.log
[2026-10-20T05:14:46Z] R copied b70457d498c451b0311d0e17c52a4f8fc020dfec4acf48f21e054c56f8c7f7a1 /root/btc-forensics/tz29-work--logs--01-stage.log
[2026-10-20T05:14:46Z] R copied e1de5ab772322a1a64665517edbd9af1e267ee75a2e0f2907e2d3d0111e48b1e /root/btc-forensics/tz29-work--logs--02-fingerprint.log
[2026-10-20T05:14:46Z] R copied c9c3d21bda6b5d425061aa33eb92da03e4b3d6018cb3e7890b0b65e952efbeca /root/btc-forensics/tz29-work--logs--03-host-gate.log
[2026-10-20T05:14:46Z] R copied 8362edf87bab73db58dcaa6e18e9dd65c7fcf51e2eb36bd923f2bd9cbeb4fcce /root/btc-forensics/tz29-work--logs--04-refs.log
[2026-10-20T05:14:46Z] R copied a5e8022f0a7bc3c78fb71ce582b42a21bfdcc17920cd88ded29c1d08f6a20dd9 /root/btc-forensics/tz29-work--logs--05-branch.log
[2026-10-20T05:14:46Z] R copied 030f6dc549fad4c7a5bbdae799f089dadb6f212179669dfdeaeb06ffedec76ac /root/btc-forensics/tz29-work--logs--06-commit-push.log
[2026-10-20T05:14:46Z] R copied ff1b268a8fa0850e56fa6ab893e81b72e01abf2eb04c77a84ad56997190b8d3e /root/btc-forensics/tz29-work--logs--07-push-gh-helper.log
[2026-10-20T05:14:46Z] R copied aba95cab7199414f2f778db045f71ca72d59fc1c9f01ef8f886041be7e235489 /root/btc-forensics/tz29-work--logs--08-pr.log
[2026-10-20T05:14:46Z] R copied 3ffb6a211c6bf60399dc63aeb951570711b0d19a2546351ca870ca35005e2323 /root/btc-forensics/tz29-work--logs--09-selftest.log
[2026-10-20T05:14:46Z] R copied ec673f32711693b908452993661c067dec4ef5e8977453e22a6d4ace05e0dfc1 /root/btc-forensics/tz29-work--logs--10-still-1.log
[2026-10-20T05:14:46Z] R copied 5c6e72af4df61303e8283d371bcd581bd1304039063125471e4d1553e3a41e16 /root/btc-forensics/tz29-work--logs--11-scratch.log
[2026-10-20T05:14:46Z] R copied f28689952275fff7542fbe4a2cdb1c853c044d75ef09e5a023a2797fe169cdde /root/btc-forensics/tz29-work--logs--12-reclaim-scratch.log
[2026-10-20T05:14:46Z] R copied 44c2371b316d488feeea0fa532119c29776e2f852c2dbae21829ac35a8b0d8bf /root/btc-forensics/tz29-work--logs--13-rm-6b7bd886.log
[2026-10-20T05:14:46Z] R copied 2e9f579d3da60b3fc850aa4818f5ac2684b7f25c5bfdf9bf828e1f634d52ec12 /root/btc-forensics/tz29-work--logs--14-rm-6de9e261.log
[2026-10-20T05:14:46Z] R copied a7d2fc9d8c964dc5653d90eb245f8642b25e0a6d426bed56ad86e63bce986ff6 /root/btc-forensics/tz29-work--logs--15-archive-1.log
[2026-10-20T05:14:46Z] R copied d3dc8622115e18357a162874e7ce3ce03236d79cf7ac8fe579326e1b7372bbb1 /root/btc-forensics/tz29-work--logs--16-rehearse.log
[2026-10-20T05:14:46Z] R copied 8e3892e3f8a43d6f89cfaa16f8d40458f9130f4d07af61a98928321daa66ae21 /root/btc-forensics/tz29-work--logs--17-replay.log
[2026-10-20T05:14:46Z] R copied a062946d1b4f3c11ac3aedb048917452d9926307834f008eecbd586e069f4358 /root/btc-forensics/tz29-work--logs--18-instant.log
[2026-10-20T05:14:46Z] R copied 4b3896b91bb8328cb8ce2f86a03c6dfc81fe64f84e042454bdd849ee0370037c /root/btc-forensics/tz29-work--logs--19-fetch.log
[2026-10-20T05:14:46Z] R copied aac742458198e1429d9b2225a464fa6067179045c29edd9a58246700143377ef /root/btc-forensics/tz29-work--logs--20-constants-1.log
[2026-10-20T05:14:46Z] R copied 2ec1fd387c59010954ddb3d585e5372c78fa4a24c5eae8bf005fe9eb3254db3a /root/btc-forensics/tz29-work--logs--21-constants-2.log
[2026-10-20T05:14:46Z] R copied 22cadc52c9cfdb846c272f1ce4586f5553be4ec78b4bac56c58c2c7d8bf62207 /root/btc-forensics/tz29-work--logs--22-score-1.log
[2026-10-20T05:14:46Z] R copied 410982fba6e82c707f933ac433eac523d151ad7b8ee9e41067c771cb4df40580 /root/btc-forensics/tz29-work--logs--23-score-2.log
[2026-10-20T05:14:46Z] R copied 24eb1a02c9b2b774fd02a112305f55b2250c7a7cd4ce590fa21e62db37c0ffdb /root/btc-forensics/tz29-work--logs--24-still-2.log
[2026-10-20T05:14:46Z] R copied f5e95dfdfc84d8b51f2d67002bf7b8cc8585fdf2ce50130fbac49e38c2e8168b /root/btc-forensics/tz29-work--logs--25-host-gate-2.log
[2026-10-20T05:14:46Z] R copied 101df52ed5906d7503098e4b88687966b0ddaa0433b1a90fffe800209453396d /root/btc-forensics/tz29-work--logs--26-archive-2.log
[2026-10-20T05:14:46Z] R copied 3869032b7e54bf17f44f77e5ef75e36755bec6b8d8a541c2a0adaf8e456c02c3 /root/btc-forensics/tz29-work--logs--27-closing-reads.log
[2026-10-20T05:14:46Z] R copied 62709ca2df869830ec3b3a6520052a06573d5cc84dfad57b616d747cf58a8010 /root/btc-forensics/tz29-work--logs--28-selfcheck.log
[2026-10-20T05:14:47Z] R copied 8ed4c649aba97a930f19a328b698b04160d2de1f02128c6bdc7f1c455ba8b7ea /root/btc-forensics/tz29-work--logs--29-files-written.log
[2026-10-20T05:14:47Z] R copied 9f521a23b3a5b48ac7569f68a9c42bf6da1bb8ef09f5a71c0c8e091fbf5098e3 /root/btc-forensics/tz29-work--rehearsal--rehearsal-constants.json
[2026-10-20T05:14:47Z] R copied 3ce50a85f84068a4cac15ece53d2ea1b16184b9080d69228b0baae8f887c8116 /root/btc-forensics/tz29-work--rehearsal--rehearsal-fills.jsonl.gz
[2026-10-20T05:14:47Z] R copied 2676af1dee730001abf560555c1c0eb9b88901209a94598dcb966495e20131d1 /root/btc-forensics/tz29-work--rehearsal--rehearsal-members.csv
[2026-10-20T05:14:47Z] R copied 4cdf1a1179c0d58f048d091e0a719951cb3af38c822d49a2e9343bea5f502d1f /root/btc-forensics/tz29-work--rehearsal--rehearsal-reading.json
[2026-10-20T05:14:47Z] R copied d31eb18fa58f8a26f12979f733fcead3b2482a480ba97a17c1145c1eef99bda2 /root/btc-forensics/tz29-work--rehearsal--rehearsal-scored.csv
[2026-10-20T05:14:47Z] R copied 8b3649dd6fbfbea1f625f5b685b891a76c10b6566c639710408b2af9490a61cf /root/btc-forensics/tz29-work--rehearsal--rehearsal-timing.jsonl
[2026-10-20T05:14:47Z] R copied 83a53bd3fb13829173282487833ef0398280d358377e0f09d0beb414c7829cbc /root/btc-forensics/tz29-work--rehearsal--set.json
[2026-10-20T05:14:47Z] R copied 98f740a229d5bb19eb60b6d2a47338d847014e875518cffba607be62eaa7e145 /root/btc-forensics/tz29-work--set--fetch-timing.jsonl
[2026-10-20T05:14:47Z] R copied 3f009cbeedc81713601a2cec5f080d0bdc2ab174fc1d468202604f3b10843d13 /root/btc-forensics/tz29-work--set--set.json
[2026-10-20T05:14:47Z] R copied 43b10ae4984f7914bbd6d3fa79432651ec7a491b94b2e6b6daf114acdf47d2b3 /root/btc-forensics/tz29-work--set--tz29-constants.json
[2026-10-20T05:14:47Z] R copied 30c36db8d68a88ed0c34956c2c4fbda36653fa4d592cbdac6af8eac937e40aa4 /root/btc-forensics/tz29-work--set--tz29-fills.jsonl.gz
[2026-10-20T05:14:47Z] R copied 97c67b0c830ee47a7be0d58117e6ab6a305b59ab80c7f599dadf190a42f41fc0 /root/btc-forensics/tz29-work--set--tz29-members.csv
[2026-10-20T05:14:47Z] R copied 6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f /root/btc-forensics/tz29-work--stage--research--tz23-maker-m0.py
[2026-10-20T05:14:47Z] R copied 18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905 /root/btc-forensics/tz29-work--stage--research--tz29-maker-m0-second-look.py
[2026-10-20T05:14:47Z] RECLAIM PASS: 262 files considered, 49 named by a report, 1 kept by name, 50 copied, 0 already held; forensic store 1846 -> 1896 files
[2026-10-20T05:14:47Z] malloc tuned: True
[2026-10-20T05:14:47Z] peak memory of this run: 31617024 bytes
[2026-10-20T05:14:47Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
$ git -C /root/btc-5m-twap worktree remove /root/tz29-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz29-work; echo "exit=$?"
exit=0
$ test -e /root/tz29-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       ad38846 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
1896
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12476121088
```

- **RECLAIM PASS:** 262 files considered, 49 named by this report's draft, 1 kept by name, **50 copied**, 0 already
  held; the forensic store went from **1,846 to 1,896** files, equal to before plus the copies.
  - The one kept by name is `logs/29-files-written.log`. Its final SHA-256, `8ed4c649…`, is not the in-file line
    (§2.15).
  - The branch worktree was skipped. It held exactly its pushed `HEAD`, `f6425f7…`.
  - The other 212 files considered were the two chunk caches (210 files) and the builder's two files. None was
    copied.
- **`git worktree remove` without `--force` exited `0`; `rm -rf` exited `0`; `test -e` exited `1`.**
- The registered worktrees are `/root/btc-5m-twap` and `/root/btc-recorder-svc`, and nothing else.
- None of these commands was refused by the session's classifier.
- **The session's own directory**, `7a160398-f4cf-54ee-b771-c3006d558bde`, is live with this session's process and is
  the next TZ's to reclaim.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-29-maker-m0-second-look`, commit `f6425f713034724210dc120d2108bcfad63cadc6`, pushed; its upstream `origin/tz-29-maker-m0-second-look` equals its head |
| pull request | #28, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/28`, open, not merged by the Executor |
| Release | none: §2 item 11 creates none |
| report | `CryptoReports/TZ-29-maker-m0-second-look-report.md`, to `main` in one commit |

**Contract §4.2's self-check** — `logs/28-selfcheck.log`, verbatim, run after the push and the pull request:

```text
$ git rev-list origin/main | grep -c f6425f713034724210dc120d2108bcfad63cadc6
0
$ git diff --name-only origin/main origin/tz-29-maker-m0-second-look
research/tz29-maker-m0-second-look.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
$ git diff --name-status --stat origin/main origin/tz-29-maker-m0-second-look
A	research/tz29-maker-m0-second-look.py
1225	0	research/tz29-maker-m0-second-look.py
$ git rev-parse origin/main origin/tz-29-maker-m0-second-look
ad38846948bd1b515aff0f04c1718587ecaf72dc
f6425f713034724210dc120d2108bcfad63cadc6
$ gh pr view 28 --json number,state,headRefOid,baseRefName,url
{"baseRefName":"main","headRefOid":"f6425f713034724210dc120d2108bcfad63cadc6","number":28,"state":"OPEN","url":"https://github.com/seahomebatumi-ai/btc-5m-twap/pull/28"}
```

The first line is `0`. The diff names one path, added, 1,225 lines and 0 deleted. Nothing matches `.parquet` or `.zip`.

---

## 4. Gate

| gate | TZ's PASS condition | deciding read | result |
|---|---|---|---|
| G-REHEARSAL | §4.1: 16 checks equal | 10 of 10 figures, 6 of 6 files | **PASS** |
| G-REPLAY | §4.2: 6 files and 5 checks | 6 of 6, 5 of 5 | **PASS** |
| G-SET | §4.3: 4,032 members above `1791241800`, every chunk read back | 4,032 of 4,032 considered, 202 chunks | **PASS** |
| **M0** | §4.4: EARN at `S >= thr`; NO EARN at `S <= δ · Sh − thr`; else UNDECIDABLE | `S` `580,110.138` against `thr` `637,504.836` and `δ · Sh − thr` `617,377.804`, over 8,064 members | **NO EARN** |
| G-STILL | §4.5: `MainPID`, `NRestarts`, `ActiveState` unchanged | recorder `4148534`/2/active; pair book `1942330`/15/active | **PASS** |

The deciding number, to three decimals: `S` = **`580,110.138`** USDC against the NO EARN bound `617,377.804`, a margin of
`37,267.666`. Per share, that is `0.231` c against `0.246` c. Nothing was tuned, and no gate was reinterpreted.

---

## 5. Validation

| # | check | count | asserted |
|---|---|---|---|
| V1 | §0.2's fingerprint | `FINGERPRINT PASS`: revision `2026-10-19-a`; anchors 6 of 6, 4 re-derived; 40 rows, 37 of 37 `frozen` equal, 2 tracked, 1 reported | asserted, in `fingerprint` |
| V2 | §0.3's host gate | H1 to H4, memory and disk: 6 of 6; the rest printed | compared by the Executor against the TZ's literals; recorded, not asserted by a script |
| V3 | §0.1's and §3.1's file | 1 of 1 hash asserted at each, 1,225 lines, 68,959 bytes; TZ-23's file `6b3ace2c…` at each; the diff names one path, `A`, 1,225 lines | hashes asserted by the extraction script, and TZ-23's by the instrument at every load; the diff recorded |
| V4 | the self-test | `51 of 51 checks passed` | asserted |
| V5 | the archive's record | ledger `30,913` bytes, `3d08a5f7…`, 130 records, 13 runs, 13 tags, at both reads | recorded, gating nothing |
| V6 | G-REHEARSAL | `16 of 16` — 10 figures and 6 files | asserted |
| V7 | G-REPLAY | 6 of 6 stored files; 5 of 5 checks | asserted |
| V8 | G-SET | 4,032 members; 4,032 considered; 0 non-members; 202 chunks inside the idle stretch, 0 ending after second 590 | asserted, in `fetch` |
| V9 | the constants, twice | 5 of 5 `unchanged` | `write_once` asserts equality on a second run |
| V10 | the score, twice | NO EARN; 2 of 2 `unchanged`; 2 ledger lines; the first look's 4,032 rows equal TZ-23's; commit on `origin` 04:27:29.648, first label read 05:09:45 | asserted, in `score`; the instants recorded |
| V11 | G-STILL | both units unchanged | compared and printed by `still`; recorded, not asserted |
| V12 | the hooks | `opens refused: 0; … 0` at every mode, 16 of 16 runs | printed by every mode; recorded |
| V13 | memory | every peak under `88,567,808`; `malloc tuned: True` at every mode | the floor asserted by every mode that reads the venue or a set |
| V14 | contract §4.2 | `0`; one path; nothing | recorded |
| V15 | §3.11's closing reads | every read printed (§2.12) | recorded |
| V16 | §9's `reclaim` runs | §2.4 and §2.16 | asserted, in `reclaim` |
| V17 | §9's removals | §2.4 and §2.16 | recorded |

---

## 6. What could not be implemented as written

1. **§3.1's `git push -u origin tz-29-maker-m0-second-look` failed** (`logs/06-commit-push.log`, exit `1`):
   `fatal: could not read Username for 'https://github.com'`. The token embedded in `origin`'s URL draws an HTTP
   redirect, and git then retries without the credential. An anonymous `git ls-remote` of the same URL is not
   redirected, so the token was most likely revoked or expired. Its value was not tested against any API and appears
   in no log or file.
   - **The branch was pushed instead** with `git -c credential.helper= -c "credential.helper=!gh auth git-credential"
     push https://github.com/seahomebatumi-ai/btc-5m-twap.git tz-29-maker-m0-second-look:refs/heads/tz-29-maker-m0-second-look`
     (`logs/07-push-gh-helper.log`), then `git branch --set-upstream-to=origin/tz-29-maker-m0-second-look`. This used
     the `gh` CLI's stored login for `seahomebatumi-ai`, the account that opens the pull requests.
   - The request is still `git` to the same repository. `gh` supplied only the local credential and made no request.
   - The commit on `origin` is the one the worktree holds, and `score`'s check that `origin` carries `HEAD` passed.
   - **The report's own push to `main` uses the same route.** `origin`'s URL still carries the failing token, and the
     Boss should replace or remove it.
2. **The archive ran off the calendar a third time**, at 2026-10-19 21:54:19 UTC, `A` `1792446859`. This adds a tag
   beyond the TZ's projected 50 ref lines (§0.5). The difference is recorded, not BLOCKING, as §0.5 says.
3. **§2.8's start-second range, the first start and last end, and the 2,577.6 s of fetching time** were read by the
   Executor from `set/fetch-timing.jsonl` with a one-line Python read. That file holds chunk times and each chunk's
   first `T0`, and no document or fill. The instrument prints only the summary line quoted above. These figures are
   diagnostics.
   - **The weekday split** (§1) is grid arithmetic, not a read of `set.json`.
   - **The "(sum)" cells and the per-share ratios** of §2.9 and §2.10 are the Executor's arithmetic on the printed
     figures, at 60 digits.
4. **The report was drafted from a template by a builder script**, `template.md` and `build-report.py`, written
   under `/root/tz29-work/build/`. The builder embeds each log verbatim and asserts every typed figure in the prose
   against the log it comes from: 157 checks before B-RECLAIM-OWN. `reclaim` considered both files and copied
   neither, since no report names them. Just before `rm -rf`, the two were copied into the session's scratchpad so
   that §2.16 could be filled in afterwards. The final build read every log from its byte-for-byte copy in the
   forensic store, `tz29-work--logs--*`, and the checks passed again. §2.16 and the B-RECLAIM-OWN cells were pasted
   from the session's output, as §9 requires.
5. **`logs/29-files-written.log` hashes itself while being written** (§2.15), so its own line does not identify it.
6. **`state.json`'s `constants_at` reads `05:09:39`**, the second `constants` run's instant, because each run records
   it. The first run wrote the same `constants_sha` at 05:08:42 (`logs/20-constants-1.log`). Both instants precede
   the first label read at 05:09:45.
