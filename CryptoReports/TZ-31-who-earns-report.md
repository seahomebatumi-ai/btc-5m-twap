# TZ-31 report — W0, who earns: do the makers who earned most keep earning on markets whose fills no one has read?

**W0 READING, THE MAKERS: W-EARN.** On the set's 1,008 members, `1792451700` (2026-10-19 23:15 UTC) to `1792753800`
(2026-10-23 11:10 UTC), the ten named makers' fills before `T0 + 300` give **`S` = `26,777.413` USDC on
`Sh` = `3,233,296.886` shares, `0.828` c a share**. That is `+19,067.647` at settlement (`+0.590` c a share) and
`+7,709.766` of rebate (`+0.238` c a share). **W-EARN holds:** `S >= thr` = `16,811.245` (`0.520` c a share), with a margin
of `+9,966.168` (`+0.308` c a share). **W-NO-EARN does not:** it needed `S <= δ · Sh − thr` = `−644.760` (`−0.020` c a
share), and its margin is `−27,422.173` (`−0.848` c a share). Only W-EARN holds, so TZ-31 §4.3's "both hold" clause does
not apply. Each answer was tested at `α = 0.005` by TZ-23's Ville bound, with `λ = 0.00099017` and `δ = 0.005`.
TZ-31 §1 item 3: **W-EARN opens W1.** On these 1,008 markets, the named makers' fills before each market's reading were
priced in their favour, given what was public, by more than the outcomes' noise explains, rebate included. It says
nothing about a quote of ours (TZ-31 §4.3).

**The power at the set's own `V` and `Sh` was `0.447`**, printed by `constants` before any label was read. The TZ
projected `0.962` at the formation's per-member rates. The set's makers carried `V` = `92,592,808.872`, `4.28` times the
projection's `21,616,327.488`, and `Sh` `1.33` times its `2,432,740.862`. So `thr` was `0.520` c a share against the
projected `0.330` c. Here `2 thr / Sh` is `1.040` c, above `δ`, so UNDECIDABLE could have occurred. **No row of §4.3
reads a power**, and W-EARN was read whatever the power.

**Barred from every reading, as §4.3 asks:** the ten named takers' `S` is `3,171.117` USDC on `3,439,148.178` shares,
`0.092` c a share. That is `+41,499.830` at settlement less `38,328.713` of fee. Every maker of the set together:
`S` `101,101.193` on `47,815,937.160` shares, `0.211` c a share. Every taker together: `−484,249.987`, `−1.013` c a
share. Labels: 504 Up of 1,008.

**Every gate before the reading passed.**
- G-REHEARSAL **PASS, 18 of 18** figures equal to the Architect's, over the formation's last 144 markets.
- G-SET **PASS**: 1,008 members of **1,008 candidates considered, 0 non-members**, `1792451700` … `1792753800`. The
  member list is `e3d77b0a36847b1ef628f79ec78ed6b7d597bdc39a16d6ecf87786e91ed3f658`, the value TZ-31 §1 gave for the
  case where every candidate qualifies. 336 chunks, every one read back. All 336 started and ended inside the idle
  stretch, and none ended after second 590.
- Self-test **58 of 58**. The constants were run twice, **8 of 8** files `unchanged`. The score was run twice, **3 of
  3** files `unchanged`, with **2** ledger lines.
- G-STILL **PASS**: the recorder `2388318` and the pair book `2388406`, both `NRestarts` `0` and `active`, unchanged
  from 12:23:31 to 13:02:26 UTC.

**The set's labels were first read at 2026-10-23 13:02:18 UTC**, the first ledger line's `at`. That was after the
instrument's commit `404288f` was on `origin` (`ls-remote` at 2026-10-23 12:23:07.134 UTC). It was also after the
constants `983edb35…` were on disk with their SHA-256 in `state.json`: first written at 13:01:45 UTC, and recorded again
by the second run at 13:02:10, which is `state.json`'s `constants_at`.

**No command was refused by the session's classifier**, and no block was handed to the Boss. The push went through
`gh`'s stored login, as TZ-31 §3.1 prescribes.

**Both capture units were restarted before this run, by nothing this TZ did** (§2.9). systemd's journal shows a stop
and start of `btc-recorder.service` and `btc-pairbook.service` at 2026-10-22 06:14:07–06:14:10 UTC and again at
2026-10-23 06:08:56–06:08:58 UTC. Each coincided with an `unattended-upgrade` run in the package history (liblzma/xz at
06:14:05, zlib at 06:08:55). The recorder no longer runs as map §3's pid `4148534`, and both units read `NRestarts` `0`.
G-STILL is measured from §3.3's read and passed.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-31-who-earns.md`, 2,297 lines, 157,773 bytes, SHA-256 `711a59cbafb94fe13ad7c5281d3e49fb373445fcc5f5c7a37f8016be37d5809a`, landed at `334cd7c` |
| map revision | `2026-10-22-a` at `efae20d`, equal; anchors 6 of 6; re-derived 4 of 4; rows 42; `frozen` equal 39 of 39 |
| executor model | Opus, as the TZ names: `get_session` read `session_context.model` and `last_served_model` `claude-opus-5-5` |
| branch | `tz-31-who-earns` at `404288fb03ffd3619b2183f121d45688def8fba8`, pushed; pull request #30, open, not merged |
| instrument | `research/tz31-who-earns.py`, 1,523 lines, 84,775 bytes, SHA-256 `7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765`, Appendix A byte for byte; it loads `research/tz23-maker-m0.py` `6b3ace2c…` |
| interpreter | `/root/tz04a-env/venv/bin/python` 3.12.3, every mode under `nice -n 19` and `-B` |
| requests | `gamma-api.polymarket.com/markets` and `data-api.polymarket.com/v2/trades` through TZ-23's `http_json` alone; `git` against `origin`; `gh` for the pull request and as git's credential |
| capture | not read. Every mode printed `opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0` |
| units | read with `systemctl show`, `is-active`, `is-enabled`, `list-timers` and `journalctl` alone, never signalled |
| pricer | not read, not called, not scored; `A6` `729f0bcdbee3` is stated so that what was not scored is not in doubt |
| work tree | `/root/tz31-work`, removed by B-RECLAIM-OWN (§5.16) |

No single fill's, member's or market's price, size or outcome is printed in this report, and no wallet's figure in one
market. Every figure is a sum over the set, a group, a wallet or a band, copied from the instrument's own output, or a
rounding or ratio of such figures, named where it is one.

---

## 0. Fingerprint

**Map revision read:** `2026-10-22-a`, equal to the TZ's. **Anchors**, each equal to the TZ header's and to the map's §0:
`A1` `229a944f2d51`, `A2` `6c5089330629`, `A3` `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable`,
`A4` `437b45ea196b`, `A5` `0f6c90451cbd`, `A6` `729f0bcdbee3`. The instrument re-derived `A2`, `A4`, `A5` and `A6` from
the files' SHA-256. **Contract §1 steps 1 and 2:** local `main` was fast-forwarded from `5e384de` to `origin/main`
`334cd7cba383bc27e5482615c95a6a42ead12b8e`, which carries `efae20d` (the map) and `334cd7c` (the TZ). This happened
before §0.0's `mkdir`, so no log holds it. The TZ, the map and the contract were read in full at `334cd7c`. The model
the TZ names, Opus, is the session's (`get_session`: `claude-opus-5-5`).

### 0.1 The 42 rows of the map's §0 table, and the map (V1) — `logs/02-fingerprint-I0.log`, verbatim

```text
$ I0 fingerprint
[2026-10-23T12:22:03Z] re-derived A2 research/twap-divergence.py sha256[:12] 6c5089330629 equal
[2026-10-23T12:22:03Z] re-derived A4 BTC-EXECUTOR-INSTRUCTIONS.md sha256[:12] 437b45ea196b equal
[2026-10-23T12:22:03Z] re-derived A5 research/recorder/recorder.py sha256[:12] 0f6c90451cbd equal
[2026-10-23T12:22:03Z] re-derived A6 research/pfair.py sha256[:12] 729f0bcdbee3 equal
[2026-10-23T12:22:03Z] SYSTEM-MAP.md                                  1580 lines   371311 bytes 0e6636b453ed842401dc2013475d23c59cffd36aa9d9fb9934b7dbd82a5f8bfe reported
[2026-10-23T12:22:03Z] BTC-EXECUTOR-INSTRUCTIONS.md                    234 lines    11128 bytes 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b frozen equal
[2026-10-23T12:22:03Z] research/twap-divergence.py                    1135 lines    50928 bytes 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 frozen equal
[2026-10-23T12:22:03Z] research/selftest-twap-divergence.py            376 lines    16736 bytes ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a frozen equal
[2026-10-23T12:22:03Z] research/tz02-distribution.py                   334 lines    14511 bytes f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 tracked
[2026-10-23T12:22:03Z] research/pfair.py                               441 lines    19357 bytes 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 frozen equal
[2026-10-23T12:22:03Z] research/selftest-pfair.py                      619 lines    32559 bytes b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa frozen equal
[2026-10-23T12:22:03Z] research/tz06-calibration.py                    577 lines    27138 bytes 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f frozen equal
[2026-10-23T12:22:03Z] research/tz07a-variance-time.py                 623 lines    28414 bytes 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 frozen equal
[2026-10-23T12:22:03Z] research/tz07b-settlement-dispersion.py         515 lines    24926 bytes 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc frozen equal
[2026-10-23T12:22:03Z] research/tz08a-out-of-sample.py                 745 lines    38822 bytes 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c frozen equal
[2026-10-23T12:22:03Z] research/tz09-disk-inventory.py                 894 lines    41004 bytes b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 frozen equal
[2026-10-23T12:22:03Z] research/tz10b-sigma-or-link.py                1224 lines    61018 bytes 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 frozen equal
[2026-10-23T12:22:03Z] research/tz11a-student-link.py                 1231 lines    64732 bytes 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 frozen equal
[2026-10-23T12:22:03Z] research/tz12-sized-gate.py                    1157 lines    61637 bytes d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 frozen equal
[2026-10-23T12:22:03Z] research/tz13-sized-gate-test3.py              1074 lines    53901 bytes a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd frozen equal
[2026-10-23T12:22:03Z] research/tz14-quote-inventory.py               2124 lines   109972 bytes 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 frozen equal
[2026-10-23T12:22:03Z] research/tz15-phase2-gate.py                   1517 lines    73799 bytes 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 frozen equal
[2026-10-23T12:22:03Z] research/tz16a-phase2-decisive-gate.py         2198 lines   111192 bytes 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 frozen equal
[2026-10-23T12:22:03Z] research/tz17-settlement-chain.py              1102 lines    38622 bytes e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 frozen equal
[2026-10-23T12:22:03Z] research/tz18a-chainbook-capture.py            1683 lines    69517 bytes e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae frozen equal
[2026-10-23T12:22:03Z] research/tz20-capture-under-systemd.py          771 lines    36528 bytes 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7 frozen equal
[2026-10-23T12:22:03Z] research/tz21-recorder-memory.py               1284 lines    59009 bytes d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f frozen equal
[2026-10-23T12:22:03Z] research/tz23-maker-m0.py                      1184 lines    54885 bytes 6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f frozen equal
[2026-10-23T12:22:03Z] research/tz24-nesting-b2.py                    1535 lines    76142 bytes 4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b frozen equal
[2026-10-23T12:22:03Z] research/tz26-nesting-b3-capture.py            2492 lines   118466 bytes caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec frozen equal
[2026-10-23T12:22:03Z] research/tz27-pairbook-archive.py              2078 lines   106284 bytes 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673 frozen equal
[2026-10-23T12:22:03Z] research/tz28-pairbook-archive-timer.py        1438 lines    74576 bytes 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4 frozen equal
[2026-10-23T12:22:03Z] research/tz29-maker-m0-second-look.py          1225 lines    68959 bytes 18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905 frozen equal
[2026-10-23T12:22:03Z] research/tz30-nesting-b3-measure.py            2518 lines   131119 bytes 93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab frozen equal
[2026-10-23T12:22:03Z] research/recorder/recorder.py                   651 lines    27821 bytes 0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7 frozen equal
[2026-10-23T12:22:03Z] research/recorder/config.py                     112 lines     4773 bytes 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d frozen equal
[2026-10-23T12:22:03Z] research/recorder/manifest.py                   254 lines    10002 bytes 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 frozen equal
[2026-10-23T12:22:03Z] research/recorder/analyze.py                    813 lines    34705 bytes eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d frozen equal
[2026-10-23T12:22:03Z] research/recorder/probe.py                      227 lines     9324 bytes 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 frozen equal
[2026-10-23T12:22:03Z] research/recorder/selftest.py                   573 lines    30591 bytes c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 frozen equal
[2026-10-23T12:22:03Z] deploy/systemd/btc-recorder.service              23 lines      707 bytes 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1 frozen equal
[2026-10-23T12:22:03Z] deploy/systemd/btc-chainbook.service             22 lines      724 bytes a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2 frozen equal
[2026-10-23T12:22:03Z] deploy/systemd/btc-pairbook.service              22 lines      761 bytes ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8 frozen equal
[2026-10-23T12:22:03Z] deploy/systemd/btc-pairbook-archive.service      17 lines      794 bytes 2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7 frozen equal
[2026-10-23T12:22:03Z] deploy/systemd/btc-pairbook-archive.timer        13 lines      417 bytes 07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913 frozen equal
[2026-10-23T12:22:03Z] .gitignore                                        5 lines      252 bytes 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b tracked
[2026-10-23T12:22:03Z] SYSTEM-MAP.md 1580 lines 371311 bytes sha256 0e6636b453ed842401dc2013475d23c59cffd36aa9d9fb9934b7dbd82a5f8bfe
[2026-10-23T12:22:03Z] FINGERPRINT PASS: revision 2026-10-22-a; anchors 6 of 6, 4 re-derived; rows 42: frozen 39 of 39 equal, tracked 2, reported 1; tz23-maker-m0.py is the file this instrument loads
[2026-10-23T12:22:03Z] malloc tuned: True
[2026-10-23T12:22:03Z] peak memory of this run: 31244288 bytes
[2026-10-23T12:22:03Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

`I fingerprint` from the worktree at §3.1, `logs/06-fingerprint-I.log`, printed the same 47 row and anchor lines and
`FINGERPRINT PASS` at 12:22:56 UTC, its peak `31,371,264` bytes. Its lines differ from the above in their stamps and
that one peak alone.

---

## 1. Input

### 1.1 What was read

| input | read by | what |
|---|---|---|
| `SYSTEM-MAP.md`, the contract and the 42 files of map §0 | `fingerprint`, twice | lines, bytes, SHA-256 |
| gamma `/markets` | `fetch`'s and `rehearse`'s walks, TZ-23's `form_set` | the documents of the 1,008 candidates from `1792451700`, in 51 requests, and of the rehearsal's 144 from `1792408500` |
| Data API v2 `/v2/trades` | `fetch_chunk2`, through TZ-23's `trades`, `taker_only` `false` and `true` | both feeds of every fill of the 1,008 members, 336 chunks of three; and of the rehearsal's 144, 48 chunks |
| `/var/lib/btc-pairbook-archive/ledger.jsonl` | `archive` twice, `still` | 45,201 bytes, SHA-256 `0a15983e495c88587af9c60afc0a6ea5dac1f5363885ba1275d598e62b7d0446`, 190 complete records, at both reads |
| systemd | `systemctl show`, `is-active`, `is-enabled`, `list-timers`; `journalctl` | the units, the boots, the timer's journal, systemd's reload records, and the capture units' stop and start records (§2.9) |
| `/root/btc-forensics/tz27-work--archive--set.json` | §0.3's `stat` and `sha256sum` | H4 |

**Nothing was re-collected that an earlier TZ had collected**, beyond the rehearsal: its 144 markets are the formation's
last, every one read by TZ-29, and G-REHEARSAL is that re-read. **No fill of any member of the set had been read before
this run** (TZ-31 §1, data hygiene). No file under `/var/lib/btc-recorder/`, `/var/lib/btc-chainbook/` or
`/var/lib/btc-pairbook/` was opened or listed. The only reads under those roots were §0.3's `df`, `find` and `grep -c`
(recorder root) and its `du -sb` (pair book store), at both runs.

### 1.2 The set (G-SET, V7)

| field | value |
|---|---|
| walk | from `1792451700`, TZ-23's `candidates` past its three excluded spans, all ending below it |
| candidates considered | **1,008** |
| members | **1,008**, `1792451700` (2026-10-19 23:15 UTC) to `1792753800` (2026-10-23 11:10 UTC) |
| non-members | **0**. `constants` printed no `non-member` line, and `tz31-constants.json`'s `non_members` is empty |
| members by weekday | Monday 9, Tuesday 288, Wednesday 288, Thursday 288, Friday 135; none on a weekend. Computed from the epochs `1792451700 + 300 k`, `k` = 0 … 1,007. The member list's hash equals that grid's, so the split is the members' |
| member list SHA-256 | `e3d77b0a36847b1ef628f79ec78ed6b7d597bdc39a16d6ecf87786e91ed3f658` (`constants`), equal to TZ-31 §1's value for every candidate qualifying |
| `set.json` | 578,750 bytes, SHA-256 `16fba05fe5b49a4e6ca1f0a31740fe2531419fa718d0a50e5a91524db2730f0f` |
| the walk | started at second 157 of window `1792758600` (12:30 UTC); `the set formed in 4.2 s`; ended by second 162, before second 590 |
| the instant | `fetch` started at 12:32:37 UTC, after TZ-31's `1792757700` (12:15:00 UTC); §3.6's wait printed `instant reached: 1792758757` |

### 1.3 The rehearsal span

144 considered and 144 members, `1792408500` (2026-10-19 11:15 UTC) to `1792451400` (2026-10-19 23:10 UTC). Member list
`fb1a21ba994986742d3a1d086ad816d06405cc27e8bedf45551d28fb31067bac`; `set.json`
`138a70af9a7b4a86914a9ca3179dd1702b83485d658a322a70944d63bc7b8153`, 82,710 bytes. Its walk started at second 15 of window
`1792758600`, after a hold from second 565 of the window before, and formed in 0.9 s.

---

## 2. Measurements

### 2.1 The constants, label-free (§3.7) — `logs/19-constants-1.log`, verbatim

```text
$ I constants
[2026-10-23T13:01:20Z] MemAvailable 313843712 bytes, floor 172064768
[2026-10-23T13:01:45Z] members 1008, considered 1008, first 1792451700 2026-10-19T23:15:00Z, last 1792753800 2026-10-23T11:10:00Z; member list sha e3d77b0a36847b1ef628f79ec78ed6b7d597bdc39a16d6ecf87786e91ed3f658
[2026-10-23T13:01:45Z] makers (maker rows of 10 wallets, 10 of them with a fill): members with a fill 1008; fills 247942, shares 3233296.885950, X 31656.656386, C -32269.6229014638713180, R 7709.76552580864758430019840922940
[2026-10-23T13:01:45Z] makers: V 92592808.871725414860; Sh 3233296.885950; lambda 0.00099017; L 5.298317366548; thr 16811.244574537803 (0.005199412602 a share)
[2026-10-23T13:01:45Z] makers: W-EARN at S >= 16811.244574537803 (0.005199412602 a share); W-NO-EARN at S <= -644.760144787803 (-0.000199412602 a share); power of either answer against the other's alternative 0.4466970475876927
[2026-10-23T13:01:45Z] takers (taker rows of 10 wallets, 10 of them with a fill): members with a fill 1007; fills 62062, shares 3439148.178239, X 41899.657517, C 166566.4211998413512639, R 7665.74255352260762600299818181526
[2026-10-23T13:01:45Z] takers: V 931903250.969297938379; Sh 3439148.178239; lambda 0.00022256; L 5.298317366548; thr 49731.791102587888 (0.014460496764 a share)
[2026-10-23T13:01:45Z] takers, barred from every reading: W-EARN at S >= 49731.791102587888 (0.014460496764 a share); W-NO-EARN at S <= -32536.050211392888 (-0.009460496764 a share); power of either answer against the other's alternative 0.016519124727650103
[2026-10-23T13:01:45Z] wrote /root/tz31-work/set/tz31-constants.json sha256 983edb35895f23ca97feb66638b15b58b9ff9014092fb088d6318d2f5df8173c
[2026-10-23T13:01:45Z] wrote /root/tz31-work/set/tz31-makers-fills.jsonl.gz sha256 33b3f44b855330f3fea9834985925d238a0b63214831bc392bfae5762e4cd882
[2026-10-23T13:01:45Z] wrote /root/tz31-work/set/tz31-makers-members.csv sha256 93179e932d1d31eb2f34f27c18ca6523968c4bc3f44970cb4b980739e0d65f55
[2026-10-23T13:01:45Z] wrote /root/tz31-work/set/tz31-makers-wallets.csv sha256 46d794fddcee1463bb774f0b28cd97b377a7c6080ca821a14f7c66b3e910f3a4
[2026-10-23T13:01:45Z] wrote /root/tz31-work/set/tz31-pool.csv sha256 c92fc59e4126959ed0ff15eab5de43c9825e195ad0284f738ea9439014bbfef4
[2026-10-23T13:01:45Z] wrote /root/tz31-work/set/tz31-takers-fills.jsonl.gz sha256 2d70895d19dc08e15e700fde70df8f4c026dc0d197d04d1d7aa6265f9391bdac
[2026-10-23T13:01:45Z] wrote /root/tz31-work/set/tz31-takers-members.csv sha256 cca6c0fc376a7ea67eb0a3898c6f8c1053968cfea300a603c9c4b7019820874d
[2026-10-23T13:01:45Z] wrote /root/tz31-work/set/tz31-takers-wallets.csv sha256 b359aa051e124147456dd31fae46cfd39ce21310f57c7f96d8ca4daeaafbfa86
[2026-10-23T13:01:45Z] malloc tuned: True
[2026-10-23T13:01:45Z] peak memory of this run: 68632576 bytes
[2026-10-23T13:01:45Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

| group | fills | members with a fill | wallets with a fill | shares `Sh` | `X` | `C` | `R` | `V` |
|---|---|---|---|---|---|---|---|---|
| makers | 247,942 | 1,008 | 10 of 10 | `3,233,296.885950` | `31,656.656386` | `−32,269.6229014638713180` | `7,709.76552580864758430019840922940` | `92,592,808.871725414860` |
| takers, barred | 62,062 | 1,007 | 10 of 10 | `3,439,148.178239` | `41,899.657517` | `166,566.4211998413512639` | `7,665.74255352260762600299818181526` | `931,903,250.969297938379` |

| group | `λ` | `thr` | W-EARN at `S >=` | W-NO-EARN at `S <=` | power, printed before any label |
|---|---|---|---|---|---|
| makers | `0.00099017` | `16,811.244574537803` (`0.519941` c a share) | `16,811.244574537803` | `−644.760144787803` (`−0.019941` c a share) | `0.4466970475876927` |
| takers, barred | `0.00022256` | `49,731.791102587888` (`1.4460` c a share) | `49,731.791102587888` | `−32,536.050211392888` (`−0.9460` c a share) | `0.016519124727650103` |

`L` = `5.298317366548` for both. The c-a-share figures are each `thr` or bound over `Sh`, times 100, computed from the
printed figures at 60 digits. **The projection** (TZ-31 §1) rested on two quantities, the set's `V` and `Sh` per member.
At the formation's rates they were `21,616,327.488` and `2,432,740.862` for the makers, with `thr` `0.330` c and power
`0.962`. The set's own figures are `4.28` and `1.33` times those, giving `thr` `0.520` c and power `0.447`.

### 2.2 The reading (§3.8) — `logs/21-score-1.log`, verbatim

```text
$ I score
[2026-10-23T13:02:18Z] MemAvailable 357089280 bytes, floor 172064768
[2026-10-23T13:02:18Z] labels: 1008 members, 504 Up
[2026-10-23T13:02:18Z] makers: S 26777.41259327251890230019840922940 = settlement 19067.6470674638713180 + rebate 7709.76552580864758430019840922940; per share 0.008281767353 = 0.005897276910 + 0.002384490444
[2026-10-23T13:02:18Z] makers: W-EARN True (margin 9966.168018734716); W-NO-EARN False (margin -27422.172738060322)
[2026-10-23T13:02:18Z] makers barred: wallet 0x18c18e0c8c3154360b4f730ec8b9d8013ceb2183, 888 members, shares 766690.227163, S 4046.382542908080, per share 0.005277728083
[2026-10-23T13:02:18Z] makers barred: wallet 0x1dd2a69e73ba444ecd5d87f0073d51a670ad51c2, 968 members, shares 126529.138017, S 639.423987597721, per share 0.005053571040
[2026-10-23T13:02:18Z] makers barred: wallet 0x32c4922da31d9f90232ea40748846e5ccc48b175, 968 members, shares 144880.376200, S 841.681686845522, per share 0.005809494073
[2026-10-23T13:02:18Z] makers barred: wallet 0x373b2d17d78c27bbdbcb034dae71d26b8094c855, 943 members, shares 103465.221227, S 910.359788286153, per share 0.008798703347
[2026-10-23T13:02:18Z] makers barred: wallet 0x764fd57b0b885cbeada5a119cdf0a113ee4ec347, 973 members, shares 1481797.601735, S 16989.713554913711, per share 0.011465610104
[2026-10-23T13:02:18Z] makers barred: wallet 0x809f275254e21f720a4e6c50c28c669c721f2ef0, 958 members, shares 123921.799378, S 654.368004818334, per share 0.005280491472
[2026-10-23T13:02:18Z] makers barred: wallet 0xbfa0ed0c199c00aec969d822818f789ca35acd6d, 948 members, shares 99660.824197, S 797.394042429833, per share 0.008001078145
[2026-10-23T13:02:18Z] makers barred: wallet 0xd8f1fbe130e2b33f32633bf568a08b85058e74a9, 882 members, shares 56915.646773, S 758.838530983921, per share 0.013332687477
[2026-10-23T13:02:18Z] makers barred: wallet 0xf548517cbefe7636bef51ee31a1817f021e7c20e, 587 members, shares 55850.170040, S 882.107903256072, per share 0.015794184738
[2026-10-23T13:02:18Z] makers barred: wallet 0xf79dccd12edb1e599dc3f9bff979b95987609fe9, 1006 members, shares 273585.881220, S 257.142551233172, per share 0.000939897008
[2026-10-23T13:02:18Z] makers barred: band w0   shares 771546.115919, S 5292.999724290807, per share 0.006860250625
[2026-10-23T13:02:18Z] makers barred: band w1   shares 695919.978309, S 7408.014086986076, per share 0.010644922287
[2026-10-23T13:02:18Z] makers barred: band w2   shares 700429.045126, S 5496.240206435395, per share 0.007846962151
[2026-10-23T13:02:18Z] makers barred: band w3   shares 695953.005393, S 4356.576109721352, per share 0.006259871106
[2026-10-23T13:02:18Z] makers barred: band last shares 369448.741203, S 4223.582465838889, per share 0.011432120332
[2026-10-23T13:02:18Z] makers barred: band post shares 4907.589613, S -536.172923462042, per share -0.109253822292
[2026-10-23T13:02:18Z] takers: S 3171.1174995456106060850090909237 = settlement 41499.8302671586487361 + fee -38328.7127676130381300149909090763; per share 0.000922064807 = 0.012066892183 + -0.011144827376
[2026-10-23T13:02:18Z] takers, barred from every reading: W-EARN False (margin -46560.673603042278); W-NO-EARN False (margin -35707.167710938499)
[2026-10-23T13:02:18Z] takers barred: wallet 0x129246beaac356e104c397f0985c11b7469be5a6, 700 members, shares 79587.011039, S 3274.300661947054, per share 0.041141143752
[2026-10-23T13:02:18Z] takers barred: wallet 0x14ea1c239393f7c1ad68c72e34e250e0679583b5, 354 members, shares 107719.430210, S 563.420699695483, per share 0.005230446342
[2026-10-23T13:02:18Z] takers barred: wallet 0x19b3823092892c026517fd0ff58df4889abe0b9b, 698 members, shares 431484.72, S 2835.526544336595, per share 0.006571557260
[2026-10-23T13:02:18Z] takers barred: wallet 0x20d2309cd92b797ae7ca175ed828ed8a27fbe29d, 850 members, shares 113310.080119, S 670.374958468310, per share 0.005916287040
[2026-10-23T13:02:18Z] takers barred: wallet 0x3c58ef422754ff22c7e806336feba0064d8b776b, 775 members, shares 114076.01, S 2193.972613924009, per share 0.019232550419
[2026-10-23T13:02:18Z] takers barred: wallet 0x41e2e1ccf1e4940029af02259a31c6b89b9fa354, 459 members, shares 617121.302310, S -3193.764285062822, per share -0.005175261773
[2026-10-23T13:02:18Z] takers barred: wallet 0x5a06acbaee263540a16a0109d584f6672101ffa2, 523 members, shares 297770.216178, S -170.938829709785, per share -0.000574062886
[2026-10-23T13:02:18Z] takers barred: wallet 0x5e2b9261b0c4f697b55bf921ff2bc227183d9101, 955 members, shares 78816.748383, S 856.075817894907, per share 0.010861597763
[2026-10-23T13:02:18Z] takers barred: wallet 0xd84403efd50b49a1d8a7181627e00307e6ea5908, 893 members, shares 357896.71, S 2099.263596514204, per share 0.005865557123
[2026-10-23T13:02:18Z] takers barred: wallet 0xeebde7a0e019a63e6b476eb425505b7b3e6eba30, 809 members, shares 1241365.95, S -5957.114278462345, per share -0.004798838150
[2026-10-23T13:02:18Z] takers barred: band pre  shares 127015.303138, S -3357.876047578449, per share -0.026436783322
[2026-10-23T13:02:18Z] takers barred: band w0   shares 560110.171461, S -2839.665110280934, per share -0.005069833142
[2026-10-23T13:02:18Z] takers barred: band w1   shares 587799.004792, S -1316.100393513709, per share -0.002239031340
[2026-10-23T13:02:18Z] takers barred: band w2   shares 750898.164328, S -621.893110535316, per share -0.000828199002
[2026-10-23T13:02:18Z] takers barred: band w3   shares 900027.915576, S 4392.418612098723, per share 0.004880313750
[2026-10-23T13:02:18Z] takers barred: band last shares 513297.618944, S 6914.233549355296, per share 0.013470223305
[2026-10-23T13:02:18Z] takers barred: band post shares 122.45, S -17.249765165227, per share -0.140871908250
[2026-10-23T13:02:18Z] barred: every maker together: S 101101.193069263939 on 47815937.159942 shares, 0.002114382758 a share
[2026-10-23T13:02:18Z] barred: every taker together: S -484249.986895316530 on 47815937.734319 shares, -0.010127376139 a share
[2026-10-23T13:02:18Z] the feeds: 1512605 transactions, makers' and takers' sizes differ at 81, one side only at 0
[2026-10-23T13:02:18Z] wrote tz31-makers-scored.csv sha256 4de2f3e8dcaf135f415c0726d6fb3710ba91516029e257382bef6f6a353f7eb7
[2026-10-23T13:02:18Z] wrote tz31-takers-scored.csv sha256 29b2b5e9ba8c3ac4ed9166c3492fe0de3db2b8a85588b66c4faca058c485b4c0
[2026-10-23T13:02:18Z] wrote tz31-reading.json sha256 d7dd8ee278c4f58bbf56ec9759ec3b2558cc49cc28725407d72d89c5471bd187
[2026-10-23T13:02:18Z] W0 READING, THE MAKERS: W-EARN
[2026-10-23T13:02:18Z] malloc tuned: True
[2026-10-23T13:02:18Z] peak memory of this run: 45056000 bytes
[2026-10-23T13:02:18Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

**The makers** (gated):

| quantity | USDC | c a share |
|---|---|---|
| `S` | `26,777.41259327251890230019840922940` | `0.828177` |
| settlement `Σ (X · up − C)` | `19,067.6470674638713180` | `0.589728` |
| rebate `Σ R` | `7,709.76552580864758430019840922940` | `0.238449` |
| W-EARN bound `thr` | `16,811.244574537803` | `0.519941` |
| W-NO-EARN bound `δ · Sh − thr` | `−644.760144787803` | `−0.019941` |
| margin to W-EARN, `S − thr` | `+9,966.168018734716` | `+0.308235` |
| margin to W-NO-EARN, `(δ · Sh − thr) − S` | `−27,422.172738060322` | `−0.848118` |
| **reading** | **W-EARN** | |

The c-a-share column is each USDC figure over `Sh` `3,233,296.885950`, times 100, at 60 digits, rounded to six places.
The instrument printed the first three as `0.008281767353`, `0.005897276910` and `0.002384490444` USDC a share.

**Barred from every reading:** each named maker's `S`, shares and `S` a share, as the score printed them above. All ten
are positive, from `0.094` c a share (`0xf79dccd1…`, 273,585.881 shares) to `1.579` c (`0xf548517c…`, 55,850.170
shares). The largest by shares, `0x764fd57b…`, holds `1,481,797.602` of the group's `3,233,296.886` and `16,989.714` of
its `26,777.413` USDC. The makers' bands, as printed: `w0` `0.686` c, `w1` `1.064` c, `w2` `0.785` c, `w3` `0.626` c,
`last` `1.143` c a share, and no fill in `pre`. `post`, after the reading, is `4,907.590` shares and `−536.173` USDC,
outside `S`.

**The takers** (barred): `S` `3,171.1174995456106060850090909237` = settlement `41,499.8302671586487361` less fee
`38,328.7127676130381300149909090763`, `0.0922` c a share (`1.2067` c at settlement, `−1.1145` c of fee). Neither of
their bounds holds: W-EARN margin `−46,560.674`, W-NO-EARN margin `−35,707.168`. Their wallets and bands are printed
above.

**The pools** (barred): every maker together `S` `101,101.193069263939` on `47,815,937.159942` shares,
`0.211438` c a share; every taker together `−484,249.986895316530` on `47,815,937.734319` shares, `−1.012738` c a share.

**The feeds:** `1,512,605` transactions over the 1,008 members. Makers' and takers' sizes differ at `81`, and `0` have
one side only.

The second run, `logs/22-score-2.log`, printed the same lines but its `MemAvailable`, and `unchanged` for
`tz31-makers-scored.csv` `4de2f3e8…`, `tz31-takers-scored.csv` `29b2b5e9…` and `tz31-reading.json` `d7dd8ee2…`. The
ledger:

```text
{"at":"2026-10-23T13:02:18Z","head":"404288fb03ffd3619b2183f121d45688def8fba8","member_list_sha":"e3d77b0a36847b1ef628f79ec78ed6b7d597bdc39a16d6ecf87786e91ed3f658","members":1008}
{"at":"2026-10-23T13:02:18Z","head":"404288fb03ffd3619b2183f121d45688def8fba8","member_list_sha":"e3d77b0a36847b1ef628f79ec78ed6b7d597bdc39a16d6ecf87786e91ed3f658","members":1008}
```

### 2.3 The fetch's timing (§8)

`logs/18-fetch.log`, verbatim but for its 14 `chunks N of 336` progress lines:

```text
[2026-10-23T12:32:37Z] MemAvailable 298909696 bytes, floor 172064768
[2026-10-23T12:32:37Z] the walk starts at second 157 of window 1792758600
[2026-10-23T12:32:41Z] the set formed in 4.2 s: 1008 considered, 1008 members, /root/tz31-work/set/set.json sha256 16fba05fe5b49a4e6ca1f0a31740fe2531419fa718d0a50e5a91524db2730f0f
[2026-10-23T12:33:54Z] projected 817 s of fetching for 336 chunks after 30 fetched; 73 s of wall clock so far
[2026-10-23T13:01:04Z] chunks fetched fresh 336: inside the idle stretch 336, ending after second 590 0; longest 9.3 s; waited 1780 s; windows 3, from 2026-10-23T12:30:00Z to 2026-10-23T13:00:00Z
[2026-10-23T13:01:04Z] G-SET PASS: 1008 members, 1008 considered, 1792451700 to 1792753800, 336 chunks, every chunk read back
[2026-10-23T13:01:04Z] malloc tuned: True
[2026-10-23T13:01:04Z] peak memory of this run: 84865024 bytes
[2026-10-23T13:01:04Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

| file | lines | SHA-256 |
|---|---|---|
| `set/fetch-timing.jsonl` | 336 | `34a1740fec9f933a03f14a44518c6d7ef7009296e81ac188d174d24d1ff7c61f` |
| `rehearsal/rehearsal-timing.jsonl` | 48 | `121d4baeb92cee5acb1fb4bd2eea04959368291877a642ec0b079fe877c135bf` |

**Every chunk that ended after second 590: none**, in either fetch. The set's fetch ran from 12:32:41 to 13:01:04 UTC,
1,703 s of wall clock. The two workers together waited 1,780 s in holds, and the projection after 30 fresh chunks was
817 s of fetching against the 7,200 s bound. The rehearsal's 48 chunks all fell inside one idle stretch, the longest
8.0 s, with 134 s projected.

### 2.4 G-REHEARSAL (§3.5) — `logs/15-rehearse.log`, verbatim

```text
$ I rehearse
[2026-10-23T12:24:25Z] MemAvailable 371773440 bytes, floor 172064768
[2026-10-23T12:30:15Z] the walk starts at second 15 of window 1792758600
[2026-10-23T12:30:16Z] the set formed in 0.9 s: 144 considered, 144 members, /root/tz31-work/rehearsal/set.json sha256 138a70af9a7b4a86914a9ca3179dd1702b83485d658a322a70944d63bc7b8153
[2026-10-23T12:31:31Z] chunks 25 of 48, 74 s
[2026-10-23T12:31:41Z] projected 134 s of fetching for 48 chunks after 30 fetched; 85 s of wall clock so far
[2026-10-23T12:32:23Z] chunks 48 of 48, 127 s
[2026-10-23T12:32:23Z] chunks fetched fresh 48: inside the idle stretch 48, ending after second 590 0; longest 8.0 s; waited 0 s; windows 1, from 2026-10-23T12:30:00Z to 2026-10-23T12:30:00Z
[2026-10-23T12:32:26Z] members 144, considered 144, first 1792408500 2026-10-19T11:15:00Z, last 1792451400 2026-10-19T23:10:00Z; member list sha fb1a21ba994986742d3a1d086ad816d06405cc27e8bedf45551d28fb31067bac
[2026-10-23T12:32:26Z] makers (maker rows of 10 wallets, 10 of them with a fill): members with a fill 144; fills 32911, shares 414244.819465, X -6778.530163, C -6531.4184270423230341, R 957.39614134740118920440492969386
[2026-10-23T12:32:26Z] makers: V 4897801.198403732397; Sh 414244.819465; lambda 0.00099017; L 5.298317366548; thr 5957.123856051187 (0.014380684021 a share)
[2026-10-23T12:32:26Z] makers: W-EARN at S >= 5957.123856051187 (0.014380684021 a share); W-NO-EARN at S <= -3885.899758726187 (-0.009380684021 a share); power of either answer against the other's alternative 0.0002226007368003602
[2026-10-23T12:32:26Z] takers (taker rows of 10 wallets, 10 of them with a fill): members with a fill 144; fills 8326, shares 412423.876637, X -831.786637, C 14859.1622011511058812, R 984.45142398558404651653052080920
[2026-10-23T12:32:26Z] takers: V 60301555.497845147905; Sh 412423.876637; lambda 0.00022256; L 5.298317366548; thr 25483.831934572072 (0.061790389398 a share)
[2026-10-23T12:32:26Z] takers, barred from every reading: W-EARN at S >= 25483.831934572072 (0.061790389398 a share); W-NO-EARN at S <= -23421.712551387072 (-0.056790389398 a share); power of either answer against the other's alternative 0.0000000008081107449875446
[2026-10-23T12:32:26Z] wrote /root/tz31-work/rehearsal/rehearsal-constants.json sha256 3da68c766a697137cd4248ef31b1c16d03fa5cfcae7913de3db7147ed2a1caef
[2026-10-23T12:32:26Z] wrote /root/tz31-work/rehearsal/rehearsal-makers-fills.jsonl.gz sha256 4e738994ef75c9f1e243d26810285d2dc7e1a440ed6fcbc8c2a67b2311c3920c
[2026-10-23T12:32:26Z] wrote /root/tz31-work/rehearsal/rehearsal-makers-members.csv sha256 0189b0d0484becc2ee0e94283f8be80b2e3a5701e171778068d2559a615f3d51
[2026-10-23T12:32:26Z] wrote /root/tz31-work/rehearsal/rehearsal-makers-wallets.csv sha256 8e334f4b2217955260ff57ddeee230541c6632939b4657b6dca08dfbd3efe3b3
[2026-10-23T12:32:26Z] wrote /root/tz31-work/rehearsal/rehearsal-pool.csv sha256 6436a601be7664e81087992e8e4502e9bc38e9df4d5e3f0691fd928de81d2644
[2026-10-23T12:32:26Z] wrote /root/tz31-work/rehearsal/rehearsal-takers-fills.jsonl.gz sha256 49dd0d3748542e4c5976f4eea1e24aa06c2a6d3f6fa8034ab0bf3c4f2518b814
[2026-10-23T12:32:26Z] wrote /root/tz31-work/rehearsal/rehearsal-takers-members.csv sha256 af75e308edb7a0edb430bfee8f12944b2bd84b53a951c22b5a01f1e7c790ea48
[2026-10-23T12:32:26Z] wrote /root/tz31-work/rehearsal/rehearsal-takers-wallets.csv sha256 f379916ab1c5e697fe14094c00f9dda071dc74e64bca49e88f031a1d88c2d63e
[2026-10-23T12:32:26Z] labels: 144 members, 71 Up
[2026-10-23T12:32:26Z] makers: S 3364.82661038972422330440492969386 = settlement 2407.4304690423230341 + rebate 957.39614134740118920440492969386; per share 0.008122797081 = 0.005811612737 + 0.002311184344
[2026-10-23T12:32:26Z] makers: W-EARN False (margin -2592.297245661463); W-NO-EARN False (margin -7250.726369115911)
[2026-10-23T12:32:26Z] makers barred: wallet 0x18c18e0c8c3154360b4f730ec8b9d8013ceb2183, 131 members, shares 158859.739106, S 791.336282344163, per share 0.004981352020
[2026-10-23T12:32:26Z] makers barred: wallet 0x1dd2a69e73ba444ecd5d87f0073d51a670ad51c2, 140 members, shares 16602.965051, S 73.451342522676, per share 0.004423989468
[2026-10-23T12:32:26Z] makers barred: wallet 0x32c4922da31d9f90232ea40748846e5ccc48b175, 137 members, shares 18406.400414, S 37.905834740728, per share 0.002059383361
[2026-10-23T12:32:26Z] makers barred: wallet 0x373b2d17d78c27bbdbcb034dae71d26b8094c855, 134 members, shares 13111.594307, S 64.989230863796, per share 0.004956623073
[2026-10-23T12:32:26Z] makers barred: wallet 0x764fd57b0b885cbeada5a119cdf0a113ee4ec347, 144 members, shares 125747.992560, S 1849.232051723510, per share 0.014705857438
[2026-10-23T12:32:26Z] makers barred: wallet 0x809f275254e21f720a4e6c50c28c669c721f2ef0, 140 members, shares 17024.921909, S 52.697184821939, per share 0.003095296713
[2026-10-23T12:32:26Z] makers barred: wallet 0xbfa0ed0c199c00aec969d822818f789ca35acd6d, 138 members, shares 12661.167168, S 119.944848809074, per share 0.009473443263
[2026-10-23T12:32:26Z] makers barred: wallet 0xd8f1fbe130e2b33f32633bf568a08b85058e74a9, 121 members, shares 7554.252601, S 238.589715306322, per share 0.031583497125
[2026-10-23T12:32:26Z] makers barred: wallet 0xf548517cbefe7636bef51ee31a1817f021e7c20e, 96 members, shares 7121.964073, S 56.810037028673, per share 0.007976737378
[2026-10-23T12:32:26Z] makers barred: wallet 0xf79dccd12edb1e599dc3f9bff979b95987609fe9, 144 members, shares 37153.822276, S 79.870082228845, per share 0.002149713740
[2026-10-23T12:32:26Z] makers barred: band w0   shares 96947.453858, S 835.987435038523, per share 0.008623098408
[2026-10-23T12:32:26Z] makers barred: band w1   shares 85586.951512, S 528.542241563832, per share 0.006175500263
[2026-10-23T12:32:26Z] makers barred: band w2   shares 88578.191663, S -366.836570472088, per share -0.004141386989
[2026-10-23T12:32:26Z] makers barred: band w3   shares 89575.280542, S 447.194069304063, per share 0.004992382570
[2026-10-23T12:32:26Z] makers barred: band last shares 53556.941890, S 1919.939434955394, per share 0.035848563551
[2026-10-23T12:32:26Z] makers barred: band post shares 17.965899, S -2.129347214120, per share -0.118521606635
[2026-10-23T12:32:26Z] takers: S 3323.3805709209738862173473959540 = settlement 8245.6376908488941188 + fee -4922.2571199279202325826526040460; per share 0.008058167238 = 0.019993114264 + -0.011934947026
[2026-10-23T12:32:26Z] takers, barred from every reading: W-EARN False (margin -22160.451363651098); W-NO-EARN False (margin -26745.093122308045)
[2026-10-23T12:32:26Z] takers barred: wallet 0x129246beaac356e104c397f0985c11b7469be5a6, 97 members, shares 8293.849206, S 463.674027613241, per share 0.055905770179
[2026-10-23T12:32:26Z] takers barred: wallet 0x14ea1c239393f7c1ad68c72e34e250e0679583b5, 79 members, shares 20378.390501, S 220.009231656731, per share 0.010796202558
[2026-10-23T12:32:26Z] takers barred: wallet 0x19b3823092892c026517fd0ff58df4889abe0b9b, 17 members, shares 2695.36, S 10.875155592149, per share 0.004034769230
[2026-10-23T12:32:26Z] takers barred: wallet 0x20d2309cd92b797ae7ca175ed828ed8a27fbe29d, 121 members, shares 10604.311328, S 430.546889888150, per share 0.040601117467
[2026-10-23T12:32:26Z] takers barred: wallet 0x3c58ef422754ff22c7e806336feba0064d8b776b, 105 members, shares 7386.77, S -31.193743091933, per share -0.004222920585
[2026-10-23T12:32:26Z] takers barred: wallet 0x41e2e1ccf1e4940029af02259a31c6b89b9fa354, 144 members, shares 169917.830434, S 267.820986444199, per share 0.001576179414
[2026-10-23T12:32:26Z] takers barred: wallet 0x5a06acbaee263540a16a0109d584f6672101ffa2, 139 members, shares 76284.382433, S 392.935221704921, per share 0.005150926168
[2026-10-23T12:32:26Z] takers barred: wallet 0x5e2b9261b0c4f697b55bf921ff2bc227183d9101, 140 members, shares 10787.682735, S 136.358350627436, per share 0.012640189184
[2026-10-23T12:32:26Z] takers barred: wallet 0xd84403efd50b49a1d8a7181627e00307e6ea5908, 115 members, shares 38071.10, S 1333.639059435151, per share 0.035030221334
[2026-10-23T12:32:26Z] takers barred: wallet 0xeebde7a0e019a63e6b476eb425505b7b3e6eba30, 28 members, shares 68004.20, S 98.715391050929, per share 0.001451607269
[2026-10-23T12:32:26Z] takers barred: band pre  shares 2800.66, S 157.087733543203, per share 0.056089540874
[2026-10-23T12:32:26Z] takers barred: band w0   shares 63709.533053, S -174.105742772509, per share -0.002732805193
[2026-10-23T12:32:26Z] takers barred: band w1   shares 80832.481610, S 610.856878170049, per share 0.007557071934
[2026-10-23T12:32:26Z] takers barred: band w2   shares 100155.059372, S 931.388302131038, per share 0.009299463332
[2026-10-23T12:32:26Z] takers barred: band w3   shares 104642.081308, S 1613.709080878510, per share 0.015421225005
[2026-10-23T12:32:26Z] takers barred: band last shares 60284.061294, S 184.444318970682, per share 0.003059586813
[2026-10-23T12:32:26Z] barred: every maker together: S -731.635459551195 on 6246637.454569 shares, -0.000117124687 a share
[2026-10-23T12:32:26Z] barred: every taker together: S -47827.421936213283 on 6246637.534676 shares, -0.007656506668 a share
[2026-10-23T12:32:26Z] the feeds: 207886 transactions, makers' and takers' sizes differ at 14, one side only at 0
[2026-10-23T12:32:26Z] wrote rehearsal-makers-scored.csv sha256 c644fe98ef5461356ac99a0b012c585776e33b79db5366e5d516230c1a614ae2
[2026-10-23T12:32:26Z] wrote rehearsal-takers-scored.csv sha256 3d2945659bf530e301c7ea79eab6ea4da47421e9b2fc722930a2d4c40bc76021
[2026-10-23T12:32:26Z] wrote rehearsal-reading.json sha256 b500df7c8fc80148894fe3da329129c804b073fd385cfa904fabf3c4b1535673
[2026-10-23T12:32:26Z] G-REHEARSAL members      instrument 144, the Architect's 144, equal
[2026-10-23T12:32:26Z] G-REHEARSAL ups          instrument 71, the Architect's 71, equal
[2026-10-23T12:32:26Z] G-REHEARSAL makers n     instrument 32911, the Architect's 32911, equal
[2026-10-23T12:32:26Z] G-REHEARSAL makers sh    instrument 414244.819465, the Architect's 414244.819465, equal
[2026-10-23T12:32:26Z] G-REHEARSAL makers X     instrument -6778.530163, the Architect's -6778.530163, equal
[2026-10-23T12:32:26Z] G-REHEARSAL makers C     instrument -6531.4184270423230341, the Architect's -6531.4184270423230341, equal
[2026-10-23T12:32:26Z] G-REHEARSAL makers R     instrument 957.39614134740118920440492969386, the Architect's 957.39614134740118920440492969386, equal
[2026-10-23T12:32:26Z] G-REHEARSAL makers V     instrument 4897801.198403732397, the Architect's 4897801.198403732397, equal
[2026-10-23T12:32:26Z] G-REHEARSAL makers P     instrument 2407.4304690423230341, the Architect's 2407.4304690423230341, equal
[2026-10-23T12:32:26Z] G-REHEARSAL makers S     instrument 3364.82661038972422330440492969386, the Architect's 3364.82661038972422330440492969386, equal
[2026-10-23T12:32:26Z] G-REHEARSAL takers n     instrument 8326, the Architect's 8326, equal
[2026-10-23T12:32:26Z] G-REHEARSAL takers sh    instrument 412423.876637, the Architect's 412423.876637, equal
[2026-10-23T12:32:26Z] G-REHEARSAL takers X     instrument -831.786637, the Architect's -831.786637, equal
[2026-10-23T12:32:26Z] G-REHEARSAL takers C     instrument 14859.1622011511058812, the Architect's 14859.1622011511058812, equal
[2026-10-23T12:32:26Z] G-REHEARSAL takers R     instrument 984.45142398558404651653052080920, the Architect's 984.45142398558404651653052080920, equal
[2026-10-23T12:32:26Z] G-REHEARSAL takers V     instrument 60301555.497845147905, the Architect's 60301555.497845147905, equal
[2026-10-23T12:32:26Z] G-REHEARSAL takers P     instrument 8245.6376908488941188, the Architect's 8245.6376908488941188, equal
[2026-10-23T12:32:26Z] G-REHEARSAL takers S     instrument 3323.3805709209738862173473959540, the Architect's 3323.3805709209738862173473959540, equal
[2026-10-23T12:32:26Z] G-REHEARSAL PASS: 18 of 18 figures equal to the Architect's
[2026-10-23T12:32:26Z] malloc tuned: True
[2026-10-23T12:32:26Z] peak memory of this run: 69427200 bytes
[2026-10-23T12:32:26Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

### 2.5 The archive's record (§3.4, V5) — `logs/14-archive-1.log`, verbatim

```text
$ I archive
[2026-10-23T12:24:05Z] btc-pairbook-archive.timer {'NextElapseUSecRealtime': 'Sat 2026-10-24 03:00:20 UTC', 'LastTriggerUSec': 'Fri 2026-10-23 03:00:20 UTC', 'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-23T12:24:05Z] btc-pairbook-archive.service {'Result': 'success', 'ExecMainStatus': '0', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-23T12:24:05Z] ledger /var/lib/btc-pairbook-archive/ledger.jsonl: 45201 bytes sha256 0a15983e495c88587af9c60afc0a6ea5dac1f5363885ba1275d598e62b7d0446, 190 complete records, 0 bytes of a line still written
[2026-10-23T12:24:05Z] L 2026-10-11T15:18:12Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "2a4b998acb9f4883b26999bb278624bf", "phase_at": 192, "resumed": false, "run": 1791731892, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791731892810556801}
[2026-10-23T12:24:05Z] L 2026-10-11T15:18:13Z {"assets_n": 28, "bytes_total": 430047476, "closed": 79, "deferred": 0, "event": "set", "first_T": 1791706500, "last_T": 1791730800, "open": 0, "run": 1791731892, "sha256": "ec3983419485fa67317468917eb7b60e2d0e529be4334c7297831ff562471ad0", "tag": "pairbook-streams-1791731892", "unclosed": 0, "wall_ns": 1791731893762719408, "windows_considered": 79}
[2026-10-23T12:24:05Z] L 2026-10-11T15:18:57Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 409746510, "run": 1791731892, "sent": 28, "wall_ns": 1791731937181037882}
[2026-10-23T12:24:05Z] L 2026-10-11T15:21:30Z {"assets_n": 28, "bytes_total": 430047476, "event": "verify", "release_id": 409746510, "run": 1791731892, "verify_sha256": "032adfdbaea0b81d7ea5063eb43130c09396908f05d74be0f1818d2bb2342f64", "wall_ns": 1791732090814504593}
[2026-10-23T12:24:05Z] L 2026-10-11T15:21:31Z {"already": 0, "event": "delete", "free_after": 12969091072, "free_before": 12538937344, "freed": 430047476, "gone": 28, "removed": 28, "run": 1791731892, "wall_ns": 1791732091732399708, "windows_kept": 28}
[2026-10-23T12:24:05Z] L 2026-10-11T15:21:31Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "815823", "NRestarts": "2", "ns": 1791732091741955625}, "phase": 391, "run": 1791731892, "wall_ns": 1791732091741960838}
[2026-10-23T12:24:05Z] L 2026-10-11T15:21:31Z {"event": "kill", "exit": 0, "phase": 391, "run": 1791731892, "wall_ns": 1791732091746593097}
[2026-10-23T12:24:05Z] L 2026-10-11T15:22:01Z {"NRestarts": "3", "W": 1791731700, "event": "restart", "free_bytes": 12969062400, "gap_ns": 5548461176, "pid": 851381, "run": 1791731892, "stopped": 815823, "stream_bytes": 0, "wall_ns": 1791732121761569347}
[2026-10-23T12:24:05Z] L 2026-10-11T15:30:41Z {"T": 1791731700, "event": "resume", "reading": "PASS", "run": 1791731892, "wall_ns": 1791732641000772037}
[2026-10-23T12:24:05Z] L 2026-10-11T15:30:41Z {"assets_n": 28, "bytes_total": 430047476, "ended_outside": 0, "event": "complete", "free_bytes": 12949487616, "peak_rss": 36884480, "rate_per_day": 1474448489, "requests": 61, "run": 1791731892, "started_outside": 0, "stops": [["the cap", 1792200292], ["the floor, base 43500000 bytes a day", 1792213576], ["the floor, base 187760570 bytes a day", 1792171837]], "store_stream_bytes": 19346486, "wall_ns": 1791732641002785194}
[2026-10-23T12:24:05Z] L 2026-10-12T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "b458725447bd4a0c865999eab0a904ad", "phase_at": 20, "resumed": false, "run": 1791774020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791774020508107799}
[2026-10-23T12:24:05Z] L 2026-10-12T03:00:22Z {"assets_n": 46, "bytes_total": 794522712, "closed": 125, "deferred": 0, "event": "set", "first_T": 1791731700, "last_T": 1791772200, "open": 1, "run": 1791774020, "sha256": "c8f02de3fbed47c4cfa91e66d774427f20990f634d271237bf3c6f25887ffb99", "tag": "pairbook-streams-1791774020", "unclosed": 0, "wall_ns": 1791774022193879442, "windows_considered": 125}
[2026-10-23T12:24:05Z] L 2026-10-12T03:01:35Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 410101186, "run": 1791774020, "sent": 46, "wall_ns": 1791774095014644950}
[2026-10-23T12:24:05Z] L 2026-10-12T03:04:44Z {"assets_n": 46, "bytes_total": 794522712, "event": "verify", "release_id": 410101186, "run": 1791774020, "verify_sha256": "0f86d9494743193ae4dd5ddb59e37a08eebc8bb7318ea4d98def44406d025aec", "wall_ns": 1791774284631917592}
[2026-10-23T12:24:05Z] L 2026-10-12T03:04:46Z {"already": 0, "event": "delete", "free_after": 12960145408, "free_before": 12165431296, "freed": 794522712, "gone": 46, "removed": 46, "run": 1791774020, "wall_ns": 1791774286328338970, "windows_kept": 46}
[2026-10-23T12:24:05Z] L 2026-10-12T03:04:46Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "851381", "NRestarts": "3", "ns": 1791774286341020683}, "phase": 286, "run": 1791774020, "wall_ns": 1791774286341025663}
[2026-10-23T12:24:05Z] L 2026-10-12T03:04:46Z {"event": "kill", "exit": 0, "phase": 286, "run": 1791774020, "wall_ns": 1791774286345765034}
[2026-10-23T12:24:05Z] L 2026-10-12T03:05:16Z {"NRestarts": "4", "W": 1791774000, "event": "restart", "free_bytes": 12960112640, "gap_ns": 5455854888, "pid": 911226, "run": 1791774020, "stopped": 851381, "stream_bytes": 25646773, "wall_ns": 1791774316361306454}
[2026-10-23T12:24:05Z] L 2026-10-12T03:15:41Z {"T": 1791774000, "event": "resume", "reading": "PASS", "run": 1791774020, "wall_ns": 1791774941000362333}
[2026-10-23T12:24:05Z] L 2026-10-12T03:15:41Z {"assets_n": 46, "bytes_total": 794522712, "ended_outside": 0, "event": "complete", "free_bytes": 12948570112, "peak_rss": 37670912, "rate_per_day": 1658134355, "requests": 97, "run": 1791774020, "started_outside": 0, "stops": [["the cap", 1792189855], ["the floor, base 43500000 bytes a day", 1792203914], ["the floor, base 187760570 bytes a day", 1792170389]], "store_stream_bytes": 37220758, "wall_ns": 1791774941002570067}
[2026-10-23T12:24:05Z] L 2026-10-13T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "5e59db817b3d42ef91641fbb34bc17cc", "phase_at": 20, "resumed": false, "run": 1791860420, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791860420531436360}
[2026-10-23T12:24:05Z] L 2026-10-13T03:00:24Z {"assets_n": 96, "bytes_total": 1925987888, "closed": 221, "deferred": 0, "event": "set", "first_T": 1791773100, "last_T": 1791858600, "open": 1, "run": 1791860420, "sha256": "de9209f2e76e5c42bd1395ea6e9c17ab0fc4c497be6a9311cd1e07c101f9b777", "tag": "pairbook-streams-1791860420", "unclosed": 0, "wall_ns": 1791860424671646762, "windows_considered": 221}
[2026-10-23T12:24:05Z] L 2026-10-13T03:03:13Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 411210796, "run": 1791860420, "sent": 96, "wall_ns": 1791860593421247948}
[2026-10-23T12:24:05Z] L 2026-10-13T03:07:31Z {"assets_n": 96, "bytes_total": 1925987888, "event": "verify", "release_id": 411210796, "run": 1791860420, "verify_sha256": "a5969978f8bfb614451c41257e7eb70a13c12126932ef03d4cfbd2f2c41ad022", "wall_ns": 1791860851109946296}
[2026-10-23T12:24:05Z] L 2026-10-13T03:07:35Z {"already": 0, "event": "delete", "free_after": 12876316672, "free_before": 10949902336, "freed": 1925987888, "gone": 96, "removed": 96, "run": 1791860420, "wall_ns": 1791860855219206873, "windows_kept": 96}
[2026-10-23T12:24:05Z] L 2026-10-13T03:07:35Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "911226", "NRestarts": "4", "ns": 1791860855230756130}, "phase": 455, "run": 1791860420, "wall_ns": 1791860855230762191}
[2026-10-23T12:24:05Z] L 2026-10-13T03:07:35Z {"event": "kill", "exit": 0, "phase": 455, "run": 1791860420, "wall_ns": 1791860855235973960}
[2026-10-23T12:24:05Z] L 2026-10-13T03:08:05Z {"NRestarts": "5", "W": 1791860400, "event": "restart", "free_bytes": 12876300288, "gap_ns": 5561093708, "pid": 1027378, "run": 1791860420, "stopped": 911226, "stream_bytes": 23131514, "wall_ns": 1791860885252051875}
[2026-10-23T12:24:05Z] L 2026-10-13T03:15:41Z {"T": 1791860400, "event": "resume", "reading": "PASS", "run": 1791860420, "wall_ns": 1791861341000349433}
[2026-10-23T12:24:05Z] L 2026-10-13T03:15:41Z {"assets_n": 96, "bytes_total": 1925987888, "ended_outside": 0, "event": "complete", "free_bytes": 12857700352, "peak_rss": 37941248, "rate_per_day": 1925987888, "requests": 197, "run": 1791860420, "started_outside": 0, "stops": [["the cap", 1792218357], ["the floor, base 43500000 bytes a day", 1792227987], ["the floor, base 187760570 bytes a day", 1792202964]], "store_stream_bytes": 41556131, "wall_ns": 1791861341004126797}
[2026-10-23T12:24:05Z] L 2026-10-14T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "f4f5335f60584baeab0eabd568d20823", "phase_at": 20, "resumed": false, "run": 1791946820, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791946820511249708}
[2026-10-23T12:24:05Z] L 2026-10-14T03:00:24Z {"assets_n": 96, "bytes_total": 2039544263, "closed": 317, "deferred": 0, "event": "set", "first_T": 1791859500, "last_T": 1791945000, "open": 1, "run": 1791946820, "sha256": "9c78ba5221e0bc8d9d8699d920e17c58d76b6052fce7c0e86af4948bdc38aa1e", "tag": "pairbook-streams-1791946820", "unclosed": 0, "wall_ns": 1791946824807088559, "windows_considered": 317}
[2026-10-23T12:24:05Z] L 2026-10-14T03:03:21Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 412296623, "run": 1791946820, "sent": 96, "wall_ns": 1791947001852058175}
[2026-10-23T12:24:05Z] L 2026-10-14T03:07:45Z {"assets_n": 96, "bytes_total": 2039544263, "event": "verify", "release_id": 412296623, "run": 1791946820, "verify_sha256": "086fc6331ec202ef5c6b56257a52cbc12673053f82408a3cd4b3cf203ae44c95", "wall_ns": 1791947265299596860}
[2026-10-23T12:24:05Z] L 2026-10-14T03:07:49Z {"already": 0, "event": "delete", "free_after": 12842123264, "free_before": 10802130944, "freed": 2039544263, "gone": 96, "removed": 96, "run": 1791946820, "wall_ns": 1791947269716703785, "windows_kept": 96}
[2026-10-23T12:24:05Z] L 2026-10-14T03:07:49Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1027378", "NRestarts": "5", "ns": 1791947269728675162}, "phase": 469, "run": 1791946820, "wall_ns": 1791947269728680763}
[2026-10-23T12:24:05Z] L 2026-10-14T03:07:49Z {"event": "kill", "exit": 0, "phase": 469, "run": 1791946820, "wall_ns": 1791947269733842747}
[2026-10-23T12:24:05Z] L 2026-10-14T03:08:19Z {"NRestarts": "6", "W": 1791946800, "event": "restart", "free_bytes": 12842098688, "gap_ns": 5560847791, "pid": 1155982, "run": 1791946820, "stopped": 1027378, "stream_bytes": 17222124, "wall_ns": 1791947299751305660}
[2026-10-23T12:24:05Z] L 2026-10-14T03:15:41Z {"T": 1791946800, "event": "resume", "reading": "PASS", "run": 1791946820, "wall_ns": 1791947741000324294}
[2026-10-23T12:24:05Z] L 2026-10-14T03:15:41Z {"assets_n": 96, "bytes_total": 2039544263, "ended_outside": 0, "event": "complete", "free_bytes": 12820799488, "peak_rss": 38072320, "rate_per_day": 2039544263, "requests": 197, "run": 1791946820, "started_outside": 0, "stops": [["the cap", 1792285007], ["the floor, base 43500000 bytes a day", 1792292869], ["the floor, base 187760570 bytes a day", 1792270515]], "store_stream_bytes": 38533208, "wall_ns": 1791947741004939814}
[2026-10-23T12:24:05Z] L 2026-10-15T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "08fd4972db8347a4897a6ecd018049e4", "phase_at": 20, "resumed": false, "run": 1792033220, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792033220507675615}
[2026-10-23T12:24:05Z] L 2026-10-15T03:00:25Z {"assets_n": 96, "bytes_total": 2103892072, "closed": 413, "deferred": 0, "event": "set", "first_T": 1791945900, "last_T": 1792031400, "open": 1, "run": 1792033220, "sha256": "3272c87234da82333365144d0c39bb0f75e895943e7e34ec7ff1e559c1ad8715", "tag": "pairbook-streams-1792033220", "unclosed": 0, "wall_ns": 1792033225025238523, "windows_considered": 413}
[2026-10-23T12:24:05Z] L 2026-10-15T03:03:26Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 413374764, "run": 1792033220, "sent": 96, "wall_ns": 1792033406364376177}
[2026-10-23T12:24:05Z] L 2026-10-15T03:07:54Z {"assets_n": 96, "bytes_total": 2103892072, "event": "verify", "release_id": 413374764, "run": 1792033220, "verify_sha256": "ff1dbc619728c35ab3732813ed23e83065603970c79ae62379097e59b1f13fa0", "wall_ns": 1792033674329218632}
[2026-10-23T12:24:05Z] L 2026-10-15T03:07:58Z {"already": 0, "event": "delete", "free_after": 12590329856, "free_before": 10485972992, "freed": 2103892072, "gone": 96, "removed": 96, "run": 1792033220, "wall_ns": 1792033678892316224, "windows_kept": 96}
[2026-10-23T12:24:05Z] L 2026-10-15T03:15:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1155982", "NRestarts": "6", "ns": 1792034115012851485}, "phase": 15, "run": 1792033220, "wall_ns": 1792034115012856996}
[2026-10-23T12:24:05Z] L 2026-10-15T03:15:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792033220, "wall_ns": 1792034115018137811}
[2026-10-23T12:24:05Z] L 2026-10-15T03:15:45Z {"NRestarts": "7", "W": 1792034100, "event": "restart", "free_bytes": 12572676096, "gap_ns": 5531970911, "pid": 1284485, "run": 1792033220, "stopped": 1155982, "stream_bytes": 29667971, "wall_ns": 1792034145058520440}
[2026-10-23T12:24:05Z] L 2026-10-15T03:30:41Z {"T": 1792034100, "event": "resume", "reading": "PASS", "run": 1792033220, "wall_ns": 1792035041000365330}
[2026-10-23T12:24:05Z] L 2026-10-15T03:30:41Z {"assets_n": 96, "bytes_total": 2103892072, "ended_outside": 0, "event": "complete", "free_bytes": 12548313088, "peak_rss": 38199296, "rate_per_day": 2103892072, "requests": 197, "run": 1792033220, "started_outside": 0, "stops": [["the cap", 1792361344], ["the floor, base 43500000 bytes a day", 1792358863], ["the floor, base 187760570 bytes a day", 1792338478]], "store_stream_bytes": 54308421, "wall_ns": 1792035041006683547}
[2026-10-23T12:24:05Z] L 2026-10-15T06:18:30Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "1fd2e68b26a04a328b7551cbafc2eabe", "phase_at": 210, "resumed": false, "run": 1792045110, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792045110608854708}
[2026-10-23T12:24:05Z] L 2026-10-15T06:18:31Z {"assets_n": 14, "bytes_total": 352241341, "closed": 427, "deferred": 0, "event": "set", "first_T": 1792032300, "last_T": 1792044000, "open": 0, "run": 1792045110, "sha256": "0337b76512886f5dd78d71cfb303a343631f73624e2eb539ed79ed7f32cc0b8e", "tag": "pairbook-streams-1792045110", "unclosed": 0, "wall_ns": 1792045111425201892, "windows_considered": 427}
[2026-10-23T12:24:05Z] L 2026-10-15T06:19:00Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 413477311, "run": 1792045110, "sent": 14, "wall_ns": 1792045140771279777}
[2026-10-23T12:24:05Z] L 2026-10-15T06:21:20Z {"assets_n": 14, "bytes_total": 352241341, "event": "verify", "release_id": 413477311, "run": 1792045110, "verify_sha256": "52fc16f3058d99f3207b8fe2e61473302a0f89a9e1a2e0f5c8eb71f413e8e379", "wall_ns": 1792045280782420614}
[2026-10-23T12:24:05Z] L 2026-10-15T06:21:21Z {"already": 0, "event": "delete", "free_after": 12826914816, "free_before": 12474617856, "freed": 352241341, "gone": 14, "removed": 14, "run": 1792045110, "wall_ns": 1792045281527345757, "windows_kept": 14}
[2026-10-23T12:24:05Z] L 2026-10-15T06:21:21Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1284485", "NRestarts": "7", "ns": 1792045281539516731}, "phase": 381, "run": 1792045110, "wall_ns": 1792045281539522189}
[2026-10-23T12:24:05Z] L 2026-10-15T06:21:21Z {"event": "kill", "exit": 0, "phase": 381, "run": 1792045110, "wall_ns": 1792045281543696309}
[2026-10-23T12:24:05Z] L 2026-10-15T06:21:51Z {"NRestarts": "8", "W": 1792044900, "event": "restart", "free_bytes": 12826902528, "gap_ns": 5495918230, "pid": 1312748, "run": 1792045110, "stopped": 1284485, "stream_bytes": 0, "wall_ns": 1792045311558979330}
[2026-10-23T12:24:05Z] L 2026-10-15T06:30:41Z {"T": 1792044900, "event": "resume", "reading": "PASS", "run": 1792045110, "wall_ns": 1792045841024547052}
[2026-10-23T12:24:05Z] L 2026-10-15T06:30:41Z {"assets_n": 14, "bytes_total": 352241341, "ended_outside": 0, "event": "complete", "free_bytes": 12813713408, "peak_rss": 37543936, "rate_per_day": 2415369195, "requests": 33, "run": 1792045110, "started_outside": 0, "stops": [["the cap", 1792331549], ["the floor, base 43500000 bytes a day", 1792337969], ["the floor, base 187760570 bytes a day", 1792321779]], "store_stream_bytes": 12817136, "wall_ns": 1792045841098825002}
[2026-10-23T12:24:05Z] L 2026-10-16T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "5fd01e0598954380beeca3f3ac4c3f62", "phase_at": 20, "resumed": false, "run": 1792119620, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792119620165748278}
[2026-10-23T12:24:05Z] L 2026-10-16T03:00:24Z {"assets_n": 82, "bytes_total": 1804368058, "closed": 509, "deferred": 0, "event": "set", "first_T": 1792044900, "last_T": 1792117800, "open": 1, "run": 1792119620, "sha256": "adc52d666ace24c2145e55ef9d62602717d7726c791319304613be33c58459b6", "tag": "pairbook-streams-1792119620", "unclosed": 0, "wall_ns": 1792119624014812901, "windows_considered": 509}
[2026-10-23T12:24:05Z] L 2026-10-16T03:02:57Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 414488168, "run": 1792119620, "sent": 82, "wall_ns": 1792119777429141022}
[2026-10-23T12:24:05Z] L 2026-10-16T03:07:24Z {"assets_n": 82, "bytes_total": 1804368058, "event": "verify", "release_id": 414488168, "run": 1792119620, "verify_sha256": "96164ee15cef51426beba1050e8a4f47856762d5800a75fe9966f68164302e2a", "wall_ns": 1792120044830268724}
[2026-10-23T12:24:05Z] L 2026-10-16T03:07:28Z {"already": 0, "event": "delete", "free_after": 12728901632, "free_before": 10924134400, "freed": 1804368058, "gone": 82, "removed": 82, "run": 1792119620, "wall_ns": 1792120048628416638, "windows_kept": 82}
[2026-10-23T12:24:05Z] L 2026-10-16T03:07:28Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1312748", "NRestarts": "8", "ns": 1792120048640224099}, "phase": 448, "run": 1792119620, "wall_ns": 1792120048640229054}
[2026-10-23T12:24:05Z] L 2026-10-16T03:07:28Z {"event": "kill", "exit": 0, "phase": 448, "run": 1792119620, "wall_ns": 1792120048645966122}
[2026-10-23T12:24:05Z] L 2026-10-16T03:07:58Z {"NRestarts": "9", "W": 1792119600, "event": "restart", "free_bytes": 12728885248, "gap_ns": 5420693633, "pid": 1420617, "run": 1792119620, "stopped": 1312748, "stream_bytes": 12133793, "wall_ns": 1792120078665650185}
[2026-10-23T12:24:05Z] L 2026-10-16T03:15:41Z {"T": 1792119600, "event": "resume", "reading": "PASS", "run": 1792119620, "wall_ns": 1792120541000363636}
[2026-10-23T12:24:05Z] L 2026-10-16T03:15:41Z {"assets_n": 82, "bytes_total": 1804368058, "ended_outside": 0, "event": "complete", "free_bytes": 12710682624, "peak_rss": 38199296, "rate_per_day": 2112430897, "requests": 169, "run": 1792119620, "started_outside": 0, "stops": [["the cap", 1792446508], ["the floor, base 43500000 bytes a day", 1792449588], ["the floor, base 187760570 bytes a day", 1792428951]], "store_stream_bytes": 30286238, "wall_ns": 1792120541008367106}
[2026-10-23T12:24:05Z] L 2026-10-17T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "df3acd4ed1af4d05bc9ec4fa5085ebee", "phase_at": 20, "resumed": false, "run": 1792206020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792206020485538925}
[2026-10-23T12:24:05Z] L 2026-10-17T03:00:24Z {"assets_n": 96, "bytes_total": 2048827436, "closed": 605, "deferred": 0, "event": "set", "first_T": 1792118700, "last_T": 1792204200, "open": 1, "run": 1792206020, "sha256": "0915abd5810c2b901012aa6d34388eabcc76d7be8b327d651632ac9335bbe188", "tag": "pairbook-streams-1792206020", "unclosed": 0, "wall_ns": 1792206024973916528, "windows_considered": 605}
[2026-10-23T12:24:05Z] L 2026-10-17T03:03:23Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 415548049, "run": 1792206020, "sent": 96, "wall_ns": 1792206203238800300}
[2026-10-23T12:24:05Z] L 2026-10-17T03:07:35Z {"assets_n": 96, "bytes_total": 2048827436, "event": "verify", "release_id": 415548049, "run": 1792206020, "verify_sha256": "747508e351bb13bb1aa11a99791ab87d1ea798e92c66dd1ec6126aad4f67f97c", "wall_ns": 1792206455599715552}
[2026-10-23T12:24:05Z] L 2026-10-17T03:07:40Z {"already": 0, "event": "delete", "free_after": 12725805056, "free_before": 10676551680, "freed": 2048827436, "gone": 96, "removed": 96, "run": 1792206020, "wall_ns": 1792206460092686139, "windows_kept": 96}
[2026-10-23T12:24:05Z] L 2026-10-17T03:07:40Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1420617", "NRestarts": "9", "ns": 1792206460108197241}, "phase": 460, "run": 1792206020, "wall_ns": 1792206460108202947}
[2026-10-23T12:24:05Z] L 2026-10-17T03:07:40Z {"event": "kill", "exit": 0, "phase": 460, "run": 1792206020, "wall_ns": 1792206460112982086}
[2026-10-23T12:24:05Z] L 2026-10-17T03:08:10Z {"NRestarts": "10", "W": 1792206000, "event": "restart", "free_bytes": 12725788672, "gap_ns": 5487288436, "pid": 1560378, "run": 1792206020, "stopped": 1420617, "stream_bytes": 10686101, "wall_ns": 1792206490133956812}
[2026-10-23T12:24:05Z] L 2026-10-17T03:15:41Z {"T": 1792206000, "event": "resume", "reading": "PASS", "run": 1792206020, "wall_ns": 1792206941000351565}
[2026-10-23T12:24:05Z] L 2026-10-17T03:15:41Z {"assets_n": 96, "bytes_total": 2048827436, "ended_outside": 0, "event": "complete", "free_bytes": 12715110400, "peak_rss": 38330368, "rate_per_day": 2048827436, "requests": 197, "run": 1792206020, "started_outside": 0, "stops": [["the cap", 1792543404], ["the floor, base 43500000 bytes a day", 1792546173], ["the floor, base 187760570 bytes a day", 1792524292]], "store_stream_bytes": 21346173, "wall_ns": 1792206941009261301}
[2026-10-23T12:24:05Z] L 2026-10-17T08:35:37Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "ab6b527c633847f79ce14ed1afdf3623", "phase_at": 337, "resumed": false, "run": 1792226137, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792226137790990342}
[2026-10-23T12:24:05Z] L 2026-10-17T08:35:38Z {"assets_n": 23, "bytes_total": 397545662, "closed": 628, "deferred": 0, "event": "set", "first_T": 1792205100, "last_T": 1792224900, "open": 0, "run": 1792226137, "sha256": "3db64b34a3949064d28cadc5a023e4402ebacc5cf7a2adab2fe09d13971312c4", "tag": "pairbook-streams-1792226137", "unclosed": 0, "wall_ns": 1792226138787331150, "windows_considered": 628}
[2026-10-23T12:24:05Z] L 2026-10-17T08:36:15Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 415679936, "run": 1792226137, "sent": 23, "wall_ns": 1792226175895145126}
[2026-10-23T12:24:05Z] L 2026-10-17T08:38:40Z {"assets_n": 23, "bytes_total": 397545662, "event": "verify", "release_id": 415679936, "run": 1792226137, "verify_sha256": "f26e295363dadaea4d9a2de3d5e86de06da641bf85ecec538e4a36b7e89de14f", "wall_ns": 1792226320606064836}
[2026-10-23T12:24:05Z] L 2026-10-17T08:38:41Z {"already": 0, "event": "delete", "free_after": 12799180800, "free_before": 12401537024, "freed": 397545662, "gone": 23, "removed": 23, "run": 1792226137, "wall_ns": 1792226321481880383, "windows_kept": 23}
[2026-10-23T12:24:05Z] L 2026-10-17T08:45:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1560378", "NRestarts": "10", "ns": 1792226715015188081}, "phase": 15, "run": 1792226137, "wall_ns": 1792226715015194823}
[2026-10-23T12:24:05Z] L 2026-10-17T08:45:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792226137, "wall_ns": 1792226715020774740}
[2026-10-23T12:24:05Z] L 2026-10-17T08:45:45Z {"NRestarts": "11", "W": 1792226700, "event": "restart", "free_bytes": 12783226880, "gap_ns": 5530075996, "pid": 1595407, "run": 1792226137, "stopped": 1560378, "stream_bytes": 15521838, "wall_ns": 1792226745041554142}
[2026-10-23T12:24:05Z] L 2026-10-17T09:00:41Z {"T": 1792226700, "event": "resume", "reading": "PASS", "run": 1792226137, "wall_ns": 1792227641000413386}
[2026-10-23T12:24:05Z] L 2026-10-17T09:00:41Z {"assets_n": 23, "bytes_total": 397545662, "ended_outside": 0, "event": "complete", "free_bytes": 12773187584, "peak_rss": 37543936, "rate_per_day": 1659321024, "requests": 51, "run": 1792226137, "started_outside": 0, "stops": [["the cap", 1792642879], ["the floor, base 43500000 bytes a day", 1792647417], ["the floor, base 187760570 bytes a day", 1792614631]], "store_stream_bytes": 25293180, "wall_ns": 1792227641009539425}
[2026-10-23T12:24:05Z] L 2026-10-18T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "15934402892b403b858ea4b973f03c89", "phase_at": 20, "resumed": false, "run": 1792292420, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792292420527428655}
[2026-10-23T12:24:05Z] L 2026-10-18T03:00:23Z {"assets_n": 73, "bytes_total": 1197040692, "closed": 701, "deferred": 0, "event": "set", "first_T": 1792225800, "last_T": 1792290600, "open": 1, "run": 1792292420, "sha256": "7ddfeae4a937bc90c14d8047d3ab843035a2be145d8d407738f9620b098c0b08", "tag": "pairbook-streams-1792292420", "unclosed": 0, "wall_ns": 1792292423275187616, "windows_considered": 701}
[2026-10-23T12:24:05Z] L 2026-10-18T03:02:20Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 416201489, "run": 1792292420, "sent": 73, "wall_ns": 1792292540828362894}
[2026-10-23T12:24:05Z] L 2026-10-18T03:05:48Z {"assets_n": 73, "bytes_total": 1197040692, "event": "verify", "release_id": 416201489, "run": 1792292420, "verify_sha256": "a3eb29ead036c8a97f023ecb53572112300e5b22defa9d984ba1887dcddf95e3", "wall_ns": 1792292748968235081}
[2026-10-23T12:24:05Z] L 2026-10-18T03:05:51Z {"already": 0, "event": "delete", "free_after": 12776620032, "free_before": 11579240448, "freed": 1197040692, "gone": 73, "removed": 73, "run": 1792292420, "wall_ns": 1792292751530232000, "windows_kept": 73}
[2026-10-23T12:24:05Z] L 2026-10-18T03:05:51Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1595407", "NRestarts": "11", "ns": 1792292751542647421}, "phase": 351, "run": 1792292420, "wall_ns": 1792292751542652085}
[2026-10-23T12:24:05Z] L 2026-10-18T03:05:51Z {"event": "kill", "exit": 0, "phase": 351, "run": 1792292420, "wall_ns": 1792292751546822604}
[2026-10-23T12:24:05Z] L 2026-10-18T03:06:21Z {"NRestarts": "12", "W": 1792292400, "event": "restart", "free_bytes": 12776607744, "gap_ns": 5504206730, "pid": 1692402, "run": 1792292420, "stopped": 1595407, "stream_bytes": 12437717, "wall_ns": 1792292781569460854}
[2026-10-23T12:24:05Z] L 2026-10-18T03:15:41Z {"T": 1792292400, "event": "resume", "reading": "PASS", "run": 1792292420, "wall_ns": 1792293341000328710}
[2026-10-23T12:24:05Z] L 2026-10-18T03:15:41Z {"assets_n": 73, "bytes_total": 1197040692, "ended_outside": 0, "event": "complete", "free_bytes": 12764577792, "peak_rss": 37937152, "rate_per_day": 1574190499, "requests": 151, "run": 1792292420, "started_outside": 0, "stops": [["the cap", 1792731097], ["the floor, base 43500000 bytes a day", 1792734747], ["the floor, base 187760570 bytes a day", 1792698607]], "store_stream_bytes": 24161003, "wall_ns": 1792293341010228074}
[2026-10-23T12:24:05Z] L 2026-10-19T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "b6aa8a5cde4c4cc392165b8f31b1bec0", "phase_at": 20, "resumed": false, "run": 1792378820, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792378820477080166}
[2026-10-23T12:24:05Z] L 2026-10-19T03:00:24Z {"assets_n": 96, "bytes_total": 1755430954, "closed": 797, "deferred": 0, "event": "set", "first_T": 1792291500, "last_T": 1792377000, "open": 1, "run": 1792378820, "sha256": "948f4d39cca953e07be1c1c561f5115f6200f5aa8330fe78434c058d6e607528", "tag": "pairbook-streams-1792378820", "unclosed": 0, "wall_ns": 1792378824458122339, "windows_considered": 797}
[2026-10-23T12:24:05Z] L 2026-10-19T03:03:08Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 416860290, "run": 1792378820, "sent": 96, "wall_ns": 1792378988043909754}
[2026-10-23T12:24:05Z] L 2026-10-19T03:07:11Z {"assets_n": 96, "bytes_total": 1755430954, "event": "verify", "release_id": 416860290, "run": 1792378820, "verify_sha256": "86b0b971d6eaeb1c8fd7dd87f44b2f739282eec95c52919b65b79ea293db2551", "wall_ns": 1792379231626951320}
[2026-10-23T12:24:05Z] L 2026-10-19T03:07:15Z {"already": 0, "event": "delete", "free_after": 12737359872, "free_before": 10981560320, "freed": 1755430954, "gone": 96, "removed": 96, "run": 1792378820, "wall_ns": 1792379235366652736, "windows_kept": 96}
[2026-10-23T12:24:05Z] L 2026-10-19T03:07:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1692402", "NRestarts": "12", "ns": 1792379235374600961}, "phase": 435, "run": 1792378820, "wall_ns": 1792379235374606661}
[2026-10-23T12:24:05Z] L 2026-10-19T03:07:15Z {"event": "kill", "exit": 0, "phase": 435, "run": 1792378820, "wall_ns": 1792379235379253859}
[2026-10-23T12:24:05Z] L 2026-10-19T03:07:45Z {"NRestarts": "13", "W": 1792378800, "event": "restart", "free_bytes": 12737351680, "gap_ns": 5404558972, "pid": 1814768, "run": 1792378820, "stopped": 1692402, "stream_bytes": 20988190, "wall_ns": 1792379265403200749}
[2026-10-23T12:24:05Z] L 2026-10-19T03:15:41Z {"T": 1792378800, "event": "resume", "reading": "PASS", "run": 1792378820, "wall_ns": 1792379741000400500}
[2026-10-23T12:24:05Z] L 2026-10-19T03:15:41Z {"assets_n": 96, "bytes_total": 1755430954, "ended_outside": 0, "event": "complete", "free_bytes": 12720193536, "peak_rss": 38592512, "rate_per_day": 1755430954, "requests": 197, "run": 1792378820, "started_outside": 0, "stops": [["the cap", 1792771618], ["the floor, base 43500000 bytes a day", 1792774544], ["the floor, base 187760570 bytes a day", 1792745234]], "store_stream_bytes": 38026457, "wall_ns": 1792379741011807328}
[2026-10-23T12:24:05Z] L 2026-10-19T21:54:19Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "7efdb0d05f6f4814b803f423a1351eae", "phase_at": 559, "resumed": false, "run": 1792446859, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792446859827562789}
[2026-10-23T12:24:05Z] L 2026-10-19T21:54:23Z {"assets_n": 76, "bytes_total": 1702929677, "closed": 873, "deferred": 0, "event": "set", "first_T": 1792377900, "last_T": 1792445400, "open": 1, "run": 1792446859, "sha256": "8491aab13dd6df082e8a4e847bd4e676a5edbeabd050e9a1767a79d7ecfb72d3", "tag": "pairbook-streams-1792446859", "unclosed": 0, "wall_ns": 1792446863665163186, "windows_considered": 873}
[2026-10-23T12:24:05Z] L 2026-10-19T22:02:33Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 417794290, "run": 1792446859, "sent": 76, "wall_ns": 1792447353191732798}
[2026-10-23T12:24:05Z] L 2026-10-19T22:09:37Z {"assets_n": 76, "bytes_total": 1702929677, "event": "verify", "release_id": 417794290, "run": 1792446859, "verify_sha256": "dfa62b04b0291467b86d37271e00e2242c0fea6b9e1caa987e7a9b31fafd3f6b", "wall_ns": 1792447777762252351}
[2026-10-23T12:24:05Z] L 2026-10-19T22:09:41Z {"already": 0, "event": "delete", "free_after": 12726702080, "free_before": 11023396864, "freed": 1702929677, "gone": 76, "removed": 76, "run": 1792446859, "wall_ns": 1792447781500420485, "windows_kept": 76}
[2026-10-23T12:24:05Z] L 2026-10-19T22:15:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1814768", "NRestarts": "13", "ns": 1792448115017795294}, "phase": 15, "run": 1792446859, "wall_ns": 1792448115017801355}
[2026-10-23T12:24:05Z] L 2026-10-19T22:15:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792446859, "wall_ns": 1792448115024251292}
[2026-10-23T12:24:05Z] L 2026-10-19T22:15:45Z {"NRestarts": "14", "W": 1792448100, "event": "restart", "free_bytes": 12707540992, "gap_ns": 5638947193, "pid": 1915093, "run": 1792446859, "stopped": 1814768, "stream_bytes": 30931694, "wall_ns": 1792448145064395857}
[2026-10-23T12:24:05Z] L 2026-10-19T22:30:41Z {"T": 1792448100, "event": "resume", "reading": "PASS", "run": 1792446859, "wall_ns": 1792449041000625272}
[2026-10-23T12:24:05Z] L 2026-10-19T22:30:41Z {"assets_n": 76, "bytes_total": 1702929677, "ended_outside": 0, "event": "complete", "free_bytes": 12678688768, "peak_rss": 37539840, "rate_per_day": 2151069065, "requests": 157, "run": 1792446859, "started_outside": 0, "stops": [["the cap", 1792767956], ["the floor, base 43500000 bytes a day", 1792771035], ["the floor, base 187760570 bytes a day", 1792751174]], "store_stream_bytes": 60078470, "wall_ns": 1792449041020984137}
[2026-10-23T12:24:05Z] L 2026-10-20T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "39b80e28726849c6b2c7c78015f76beb", "phase_at": 20, "resumed": false, "run": 1792465220, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792465220508369328}
[2026-10-23T12:24:05Z] L 2026-10-20T03:00:21Z {"assets_n": 20, "bytes_total": 428604581, "closed": 893, "deferred": 0, "event": "set", "first_T": 1792446300, "last_T": 1792463400, "open": 1, "run": 1792465220, "sha256": "08a4bf67291e8988351d7b031e9a6250ded7ec726fb2a80a1c28559d6b827e6b", "tag": "pairbook-streams-1792465220", "unclosed": 0, "wall_ns": 1792465221560132886, "windows_considered": 893}
[2026-10-23T12:24:05Z] L 2026-10-20T03:01:05Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 417955485, "run": 1792465220, "sent": 20, "wall_ns": 1792465265840619699}
[2026-10-23T12:24:05Z] L 2026-10-20T03:03:38Z {"assets_n": 20, "bytes_total": 428604581, "event": "verify", "release_id": 417955485, "run": 1792465220, "verify_sha256": "1417b0845ea746c17a126d8311895714cd28b5cdbefbb3f27cc38e7b2d8a516a", "wall_ns": 1792465418377004134}
[2026-10-23T12:24:05Z] L 2026-10-20T03:03:39Z {"already": 0, "event": "delete", "free_after": 12736249856, "free_before": 12307550208, "freed": 428604581, "gone": 20, "removed": 20, "run": 1792465220, "wall_ns": 1792465419274331805, "windows_kept": 20}
[2026-10-23T12:24:05Z] L 2026-10-20T03:03:39Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1915093", "NRestarts": "14", "ns": 1792465419285640926}, "phase": 219, "run": 1792465220, "wall_ns": 1792465419285646173}
[2026-10-23T12:24:05Z] L 2026-10-20T03:03:39Z {"event": "kill", "exit": 0, "phase": 219, "run": 1792465220, "wall_ns": 1792465419290626015}
[2026-10-23T12:24:05Z] L 2026-10-20T03:04:09Z {"NRestarts": "15", "W": 1792465200, "event": "restart", "free_bytes": 12736208896, "gap_ns": 5521442701, "pid": 1942330, "run": 1792465220, "stopped": 1915093, "stream_bytes": 21234976, "wall_ns": 1792465449314599186}
[2026-10-23T12:24:05Z] L 2026-10-20T03:15:41Z {"T": 1792465200, "event": "resume", "reading": "PASS", "run": 1792465220, "wall_ns": 1792466141000339712}
[2026-10-23T12:24:05Z] L 2026-10-20T03:15:41Z {"assets_n": 20, "bytes_total": 428604581, "ended_outside": 0, "event": "complete", "free_bytes": 12714721280, "peak_rss": 37937152, "rate_per_day": 2057301988, "requests": 45, "run": 1792465220, "started_outside": 0, "stops": [["the cap", 1792800340], ["the floor, base 43500000 bytes a day", 1792803989], ["the floor, base 187760570 bytes a day", 1792782280]], "store_stream_bytes": 42260469, "wall_ns": 1792466141012853604}
[2026-10-23T12:24:05Z] L 2026-10-20T11:23:37Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "8b75ff2677d249a6a9fe69e50db1c2ae", "phase_at": 517, "resumed": false, "run": 1792495417, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792495417844843187}
[2026-10-23T12:24:05Z] L 2026-10-20T11:23:39Z {"assets_n": 34, "bytes_total": 764815296, "closed": 927, "deferred": 0, "event": "set", "first_T": 1792464300, "last_T": 1792494000, "open": 0, "run": 1792495417, "sha256": "e323ee33788d09b6cc52062cea9cd4914bc06d83a423f00e8704115f5ee8077e", "tag": "pairbook-streams-1792495417", "unclosed": 0, "wall_ns": 1792495419680991102, "windows_considered": 927}
[2026-10-23T12:24:05Z] L 2026-10-20T11:30:29Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 418317989, "run": 1792495417, "sent": 34, "wall_ns": 1792495829134879887}
[2026-10-23T12:24:05Z] L 2026-10-20T11:33:19Z {"assets_n": 34, "bytes_total": 764815296, "event": "verify", "release_id": 418317989, "run": 1792495417, "verify_sha256": "c2b18808ac9dd1fa1af41eb8e9b6f3b616698bb12dcfc8910b97f44dc91c36ac", "wall_ns": 1792495999645679199}
[2026-10-23T12:24:05Z] L 2026-10-20T11:33:21Z {"already": 0, "event": "delete", "free_after": 12638756864, "free_before": 11873771520, "freed": 764815296, "gone": 34, "removed": 34, "run": 1792495417, "wall_ns": 1792496001362671467, "windows_kept": 34}
[2026-10-23T12:24:05Z] L 2026-10-20T11:33:21Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1942330", "NRestarts": "15", "ns": 1792496001380557653}, "phase": 201, "run": 1792495417, "wall_ns": 1792496001380565155}
[2026-10-23T12:24:05Z] L 2026-10-20T11:33:21Z {"event": "kill", "exit": 0, "phase": 201, "run": 1792495417, "wall_ns": 1792496001386376172}
[2026-10-23T12:24:05Z] L 2026-10-20T11:33:51Z {"NRestarts": "16", "W": 1792495800, "event": "restart", "free_bytes": 12638744576, "gap_ns": 5668185588, "pid": 1997029, "run": 1792495417, "stopped": 1942330, "stream_bytes": 20135691, "wall_ns": 1792496031413213462}
[2026-10-23T12:24:05Z] L 2026-10-20T11:45:41Z {"T": 1792495800, "event": "resume", "reading": "PASS", "run": 1792495417, "wall_ns": 1792496741000411804}
[2026-10-23T12:24:05Z] L 2026-10-20T11:45:41Z {"assets_n": 34, "bytes_total": 764815296, "ended_outside": 0, "event": "complete", "free_bytes": 12627136512, "peak_rss": 37408768, "rate_per_day": 2159478482, "requests": 73, "run": 1792495417, "started_outside": 0, "stops": [["the cap", 1792815561], ["the floor, base 43500000 bytes a day", 1792815484], ["the floor, base 187760570 bytes a day", 1792795894]], "store_stream_bytes": 31416312, "wall_ns": 1792496741014150948}
[2026-10-23T12:24:05Z] L 2026-10-21T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "b930c6730bf241b99c68a735c088800c", "phase_at": 20, "resumed": false, "run": 1792551620, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792551620436317477}
[2026-10-23T12:24:05Z] L 2026-10-21T03:00:23Z {"assets_n": 62, "bytes_total": 1362902551, "closed": 989, "deferred": 0, "event": "set", "first_T": 1792494900, "last_T": 1792549800, "open": 1, "run": 1792551620, "sha256": "86c50466510f2054e4aa0455af33787059c1cc16b6a2f3dc81b5ef002ecb9ae5", "tag": "pairbook-streams-1792551620", "unclosed": 0, "wall_ns": 1792551623641943166, "windows_considered": 989}
[2026-10-23T12:24:05Z] L 2026-10-21T03:02:34Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 419096475, "run": 1792551620, "sent": 62, "wall_ns": 1792551754079483237}
[2026-10-23T12:24:05Z] L 2026-10-21T03:06:11Z {"assets_n": 62, "bytes_total": 1362902551, "event": "verify", "release_id": 419096475, "run": 1792551620, "verify_sha256": "fcd57c3250da0c73a0a463197880ede0b4caba30b2d3531b5e67c74d89101b77", "wall_ns": 1792551971026358089}
[2026-10-23T12:24:05Z] L 2026-10-21T03:06:13Z {"already": 0, "event": "delete", "free_after": 12585439232, "free_before": 11222228992, "freed": 1362902551, "gone": 62, "removed": 62, "run": 1792551620, "wall_ns": 1792551973979858662, "windows_kept": 62}
[2026-10-23T12:24:05Z] L 2026-10-21T03:06:13Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1997029", "NRestarts": "16", "ns": 1792551973992391945}, "phase": 373, "run": 1792551620, "wall_ns": 1792551973992396231}
[2026-10-23T12:24:05Z] L 2026-10-21T03:06:13Z {"event": "kill", "exit": 0, "phase": 373, "run": 1792551620, "wall_ns": 1792551973997452972}
[2026-10-23T12:24:05Z] L 2026-10-21T03:06:44Z {"NRestarts": "17", "W": 1792551600, "event": "restart", "free_bytes": 12585414656, "gap_ns": 5552861113, "pid": 2076364, "run": 1792551620, "stopped": 1997029, "stream_bytes": 21344325, "wall_ns": 1792552004023624781}
[2026-10-23T12:24:05Z] L 2026-10-21T03:15:41Z {"T": 1792551600, "event": "resume", "reading": "PASS", "run": 1792551620, "wall_ns": 1792552541000652508}
[2026-10-23T12:24:05Z] L 2026-10-21T03:15:41Z {"assets_n": 62, "bytes_total": 1362902551, "ended_outside": 0, "event": "complete", "free_bytes": 12568043520, "peak_rss": 38330368, "rate_per_day": 2110300724, "requests": 129, "run": 1792551620, "started_outside": 0, "stops": [["the cap", 1792878503], ["the floor, base 43500000 bytes a day", 1792876191], ["the floor, base 187760570 bytes a day", 1792855874]], "store_stream_bytes": 38435764, "wall_ns": 1792552541015556785}
[2026-10-23T12:24:05Z] L 2026-10-21T21:39:04Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "ddf646820072487fbca10fe0ea1d6d9d", "phase_at": 544, "resumed": false, "run": 1792618744, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792618744805106316}
[2026-10-23T12:24:05Z] L 2026-10-21T21:39:08Z {"assets_n": 75, "bytes_total": 1697351287, "closed": 1064, "deferred": 0, "event": "set", "first_T": 1792550700, "last_T": 1792617300, "open": 0, "run": 1792618744, "sha256": "14628f1239ce9548ab9a88bfae0a8017382eac3a6c54f823b79c7acf8e9f2d70", "tag": "pairbook-streams-1792618744", "unclosed": 0, "wall_ns": 1792618748723134556, "windows_considered": 1064}
[2026-10-23T12:24:05Z] L 2026-10-21T21:47:16Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 420082380, "run": 1792618744, "sent": 75, "wall_ns": 1792619236058059430}
[2026-10-23T12:24:05Z] L 2026-10-21T21:51:01Z {"assets_n": 75, "bytes_total": 1697351287, "event": "verify", "release_id": 420082380, "run": 1792618744, "verify_sha256": "954d28907c55dac360cea2a28a7781c4ca0500ef6c8313c3c86a6853539dbbce", "wall_ns": 1792619461695303474}
[2026-10-23T12:24:05Z] L 2026-10-21T21:51:05Z {"already": 0, "event": "delete", "free_after": 12533227520, "free_before": 10835509248, "freed": 1697351287, "gone": 75, "removed": 75, "run": 1792618744, "wall_ns": 1792619465416013472, "windows_kept": 75}
[2026-10-23T12:24:05Z] L 2026-10-21T21:51:05Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2076364", "NRestarts": "17", "ns": 1792619465433993359}, "phase": 365, "run": 1792618744, "wall_ns": 1792619465433999513}
[2026-10-23T12:24:05Z] L 2026-10-21T21:51:05Z {"event": "kill", "exit": 0, "phase": 365, "run": 1792618744, "wall_ns": 1792619465439433263}
[2026-10-23T12:24:05Z] L 2026-10-21T21:51:35Z {"NRestarts": "18", "W": 1792619100, "event": "restart", "free_bytes": 12533202944, "gap_ns": 5745862259, "pid": 2192943, "run": 1792618744, "stopped": 2076364, "stream_bytes": 28722461, "wall_ns": 1792619495470455301}
[2026-10-23T12:24:05Z] L 2026-10-21T22:00:41Z {"T": 1792619100, "event": "resume", "reading": "PASS", "run": 1792618744, "wall_ns": 1792620041000434452}
[2026-10-23T12:24:05Z] L 2026-10-21T22:00:41Z {"assets_n": 75, "bytes_total": 1697351287, "ended_outside": 0, "event": "complete", "free_bytes": 12508360704, "peak_rss": 37806080, "rate_per_day": 2172609647, "requests": 155, "run": 1792618744, "started_outside": 0, "stops": [["the cap", 1792936072], ["the floor, base 43500000 bytes a day", 1792932264], ["the floor, base 187760570 bytes a day", 1792913182]], "store_stream_bytes": 53078752, "wall_ns": 1792620041014703750}
[2026-10-23T12:24:05Z] L 2026-10-22T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "2ead70f2934e426f9db2802c9f366424", "phase_at": 20, "resumed": false, "run": 1792638020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792638020509862222}
[2026-10-23T12:24:05Z] L 2026-10-22T03:00:21Z {"assets_n": 21, "bytes_total": 391495954, "closed": 1085, "deferred": 0, "event": "set", "first_T": 1792618200, "last_T": 1792636200, "open": 1, "run": 1792638020, "sha256": "bcccbdcea9b48dfb0ce8b98e2ce6eb1faeb741091d2f4b96a260cd633af8810d", "tag": "pairbook-streams-1792638020", "unclosed": 0, "wall_ns": 1792638021492965919, "windows_considered": 1085}
[2026-10-23T12:24:05Z] L 2026-10-22T03:01:03Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 420262131, "run": 1792638020, "sent": 21, "wall_ns": 1792638063331313560}
[2026-10-23T12:24:05Z] L 2026-10-22T03:03:31Z {"assets_n": 21, "bytes_total": 391495954, "event": "verify", "release_id": 420262131, "run": 1792638020, "verify_sha256": "c53531cd81ef4f93c4a7a970b2c0c542146e78ed84d309d0afb42f14ab7123c9", "wall_ns": 1792638211785126344}
[2026-10-23T12:24:05Z] L 2026-10-22T03:03:32Z {"already": 0, "event": "delete", "free_after": 12514353152, "free_before": 12122759168, "freed": 391495954, "gone": 21, "removed": 21, "run": 1792638020, "wall_ns": 1792638212641898392, "windows_kept": 21}
[2026-10-23T12:24:05Z] L 2026-10-22T03:03:32Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2192943", "NRestarts": "18", "ns": 1792638212654633160}, "phase": 212, "run": 1792638020, "wall_ns": 1792638212654637695}
[2026-10-23T12:24:05Z] L 2026-10-22T03:03:32Z {"event": "kill", "exit": 0, "phase": 212, "run": 1792638020, "wall_ns": 1792638212659732496}
[2026-10-23T12:24:05Z] L 2026-10-22T03:04:02Z {"NRestarts": "19", "W": 1792638000, "event": "restart", "free_bytes": 12514340864, "gap_ns": 5643787804, "pid": 2221487, "run": 1792638020, "stopped": 2192943, "stream_bytes": 27860091, "wall_ns": 1792638242689438971}
[2026-10-23T12:24:05Z] L 2026-10-22T03:15:41Z {"T": 1792638000, "event": "resume", "reading": "PASS", "run": 1792638020, "wall_ns": 1792638941000342309}
[2026-10-23T12:24:05Z] L 2026-10-22T03:15:41Z {"assets_n": 21, "bytes_total": 391495954, "ended_outside": 0, "event": "complete", "free_bytes": 12499591168, "peak_rss": 38195200, "rate_per_day": 1789695789, "requests": 47, "run": 1792638020, "started_outside": 0, "stops": [["the cap", 1793023110], ["the floor, base 43500000 bytes a day", 1793015968], ["the floor, base 187760570 bytes a day", 1792988463]], "store_stream_bytes": 42282498, "wall_ns": 1792638941017392845}
[2026-10-23T12:24:05Z] L 2026-10-22T06:24:08Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "bf696abbc7a746dea3a0966d716d3074", "phase_at": 548, "resumed": false, "run": 1792650248, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792650248784202770}
[2026-10-23T12:24:05Z] L 2026-10-22T06:24:09Z {"assets_n": 14, "bytes_total": 280783691, "closed": 1099, "deferred": 0, "event": "set", "first_T": 1792637100, "last_T": 1792648800, "open": 1, "run": 1792650248, "sha256": "6204f5ff7868ba1bc1a8e10697a44aa9a3b4ede37177620d9dbef69d51672bb0", "tag": "pairbook-streams-1792650248", "unclosed": 0, "wall_ns": 1792650249586883942, "windows_considered": 1099}
[2026-10-23T12:24:05Z] L 2026-10-22T06:24:34Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 420372582, "run": 1792650248, "sent": 14, "wall_ns": 1792650274824220554}
[2026-10-23T12:24:05Z] L 2026-10-22T06:30:32Z {"assets_n": 14, "bytes_total": 280783691, "event": "verify", "release_id": 420372582, "run": 1792650248, "verify_sha256": "ea788ba4bf4c34150b9250af70414689f3546b3a92564a84e1dfcf1b1d5e6a02", "wall_ns": 1792650632675548955}
[2026-10-23T12:24:05Z] L 2026-10-22T06:30:33Z {"already": 0, "event": "delete", "free_after": 12560494592, "free_before": 12279042048, "freed": 280783691, "gone": 14, "removed": 14, "run": 1792650248, "wall_ns": 1792650633320590752, "windows_kept": 14}
[2026-10-23T12:24:05Z] L 2026-10-22T06:30:33Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2241902", "NRestarts": "0", "ns": 1792650633339559233}, "phase": 33, "run": 1792650248, "wall_ns": 1792650633339564607}
[2026-10-23T12:24:05Z] L 2026-10-22T06:30:33Z {"event": "kill", "exit": 0, "phase": 33, "run": 1792650248, "wall_ns": 1792650633345250000}
[2026-10-23T12:24:05Z] L 2026-10-22T06:31:03Z {"NRestarts": "1", "W": 1792650600, "event": "restart", "free_bytes": 12560482304, "gap_ns": 5601500879, "pid": 2250075, "run": 1792650248, "stopped": 2241902, "stream_bytes": 10010022, "wall_ns": 1792650663375238922}
[2026-10-23T12:24:05Z] L 2026-10-22T06:45:41Z {"T": 1792650600, "event": "resume", "reading": "PASS", "run": 1792650248, "wall_ns": 1792651541015238752}
[2026-10-23T12:24:05Z] L 2026-10-22T06:45:41Z {"assets_n": 14, "bytes_total": 280783691, "ended_outside": 0, "event": "complete", "free_bytes": 12529709056, "peak_rss": 37797888, "rate_per_day": 1925373881, "requests": 33, "run": 1792650248, "started_outside": 0, "stops": [["the cap", 1793008800], ["the floor, base 43500000 bytes a day", 1793003908], ["the floor, base 187760570 bytes a day", 1792979852]], "store_stream_bytes": 38684086, "wall_ns": 1792651541166549306}
[2026-10-23T12:24:05Z] L 2026-10-23T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "1172b5c756384074a57a896b4356ec16", "phase_at": 20, "resumed": false, "run": 1792724420, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792724420512050478}
[2026-10-23T12:24:05Z] L 2026-10-23T03:00:24Z {"assets_n": 82, "bytes_total": 1595061931, "closed": 1181, "deferred": 0, "event": "set", "first_T": 1792649700, "last_T": 1792722600, "open": 1, "run": 1792724420, "sha256": "d0e560a3669a7231dea88f79bea44078c0e31e7cff8a374af08de1b5b280bf5c", "tag": "pairbook-streams-1792724420", "unclosed": 0, "wall_ns": 1792724424121884436, "windows_considered": 1181}
[2026-10-23T12:24:05Z] L 2026-10-23T03:03:06Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 421406556, "run": 1792724420, "sent": 82, "wall_ns": 1792724586787024019}
[2026-10-23T12:24:05Z] L 2026-10-23T03:07:00Z {"assets_n": 82, "bytes_total": 1595061931, "event": "verify", "release_id": 421406556, "run": 1792724420, "verify_sha256": "3e232f5ac1bfe06b39f3befa0e17f7f3e616fd37cc7ab297e6d27128a336c9a0", "wall_ns": 1792724820430388300}
[2026-10-23T12:24:05Z] L 2026-10-23T03:07:04Z {"already": 0, "event": "delete", "free_after": 12469579776, "free_before": 10874122240, "freed": 1595061931, "gone": 82, "removed": 82, "run": 1792724420, "wall_ns": 1792724824480858054, "windows_kept": 82}
[2026-10-23T12:24:05Z] L 2026-10-23T03:07:04Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2250075", "NRestarts": "1", "ns": 1792724824494779066}, "phase": 424, "run": 1792724420, "wall_ns": 1792724824494785255}
[2026-10-23T12:24:05Z] L 2026-10-23T03:07:04Z {"event": "kill", "exit": 0, "phase": 424, "run": 1792724420, "wall_ns": 1792724824500348742}
[2026-10-23T12:24:05Z] L 2026-10-23T03:07:34Z {"NRestarts": "2", "W": 1792724400, "event": "restart", "free_bytes": 12469559296, "gap_ns": 5549775487, "pid": 2371078, "run": 1792724420, "stopped": 2250075, "stream_bytes": 21412011, "wall_ns": 1792724854530097535}
[2026-10-23T12:24:05Z] L 2026-10-23T03:15:41Z {"T": 1792724400, "event": "resume", "reading": "PASS", "run": 1792724420, "wall_ns": 1792725341000373070}
[2026-10-23T12:24:05Z] L 2026-10-23T03:15:41Z {"assets_n": 82, "bytes_total": 1595061931, "ended_outside": 0, "event": "complete", "free_bytes": 12451762176, "peak_rss": 38195200, "rate_per_day": 1867389577, "requests": 169, "run": 1792724420, "started_outside": 0, "stops": [["the cap", 1793093683], ["the floor, base 43500000 bytes a day", 1793084876], ["the floor, base 187760570 bytes a day", 1793059638]], "store_stream_bytes": 38897268, "wall_ns": 1792725341016615809}
[2026-10-23T12:24:05Z] run 1791731892 2026-10-11T15:18:12Z, off-calendar, second 55092 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1791731892: 28 files, 430047476 bytes, windows 1791706500 to 1791730800 of 79 considered; Release 409746510: sent 28, held 0, credential the primary checkout's remote URL; removed 28, freed 430047476 bytes, free after 12969091072; restart: window 1791731700, pid 851381 after 815823, NRestarts 3; resume PASS at window 1791731700; complete: requests 61, started outside 0, ended outside 0, store 19346486 bytes, free 12949487616, rate 1474448489 a day
[2026-10-23T12:24:05Z] run 1791774020 2026-10-12T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1791774020: 46 files, 794522712 bytes, windows 1791731700 to 1791772200 of 125 considered; Release 410101186: sent 46, held 0, credential the primary checkout's remote URL; removed 46, freed 794522712 bytes, free after 12960145408; restart: window 1791774000, pid 911226 after 851381, NRestarts 4; resume PASS at window 1791774000; complete: requests 97, started outside 0, ended outside 0, store 37220758 bytes, free 12948570112, rate 1658134355 a day
[2026-10-23T12:24:05Z] run 1791860420 2026-10-13T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1791860420: 96 files, 1925987888 bytes, windows 1791773100 to 1791858600 of 221 considered; Release 411210796: sent 96, held 0, credential the primary checkout's remote URL; removed 96, freed 1925987888 bytes, free after 12876316672; restart: window 1791860400, pid 1027378 after 911226, NRestarts 5; resume PASS at window 1791860400; complete: requests 197, started outside 0, ended outside 0, store 41556131 bytes, free 12857700352, rate 1925987888 a day
[2026-10-23T12:24:05Z] run 1791946820 2026-10-14T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1791946820: 96 files, 2039544263 bytes, windows 1791859500 to 1791945000 of 317 considered; Release 412296623: sent 96, held 0, credential the primary checkout's remote URL; removed 96, freed 2039544263 bytes, free after 12842123264; restart: window 1791946800, pid 1155982 after 1027378, NRestarts 6; resume PASS at window 1791946800; complete: requests 197, started outside 0, ended outside 0, store 38533208 bytes, free 12820799488, rate 2039544263 a day
[2026-10-23T12:24:05Z] run 1792033220 2026-10-15T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792033220: 96 files, 2103892072 bytes, windows 1791945900 to 1792031400 of 413 considered; Release 413374764: sent 96, held 0, credential the primary checkout's remote URL; removed 96, freed 2103892072 bytes, free after 12590329856; restart: window 1792034100, pid 1284485 after 1155982, NRestarts 7; resume PASS at window 1792034100; complete: requests 197, started outside 0, ended outside 0, store 54308421 bytes, free 12548313088, rate 2103892072 a day
[2026-10-23T12:24:05Z] run 1792045110 2026-10-15T06:18:30Z, off-calendar, second 22710 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792045110: 14 files, 352241341 bytes, windows 1792032300 to 1792044000 of 427 considered; Release 413477311: sent 14, held 0, credential the primary checkout's remote URL; removed 14, freed 352241341 bytes, free after 12826914816; restart: window 1792044900, pid 1312748 after 1284485, NRestarts 8; resume PASS at window 1792044900; complete: requests 33, started outside 0, ended outside 0, store 12817136 bytes, free 12813713408, rate 2415369195 a day
[2026-10-23T12:24:05Z] run 1792119620 2026-10-16T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792119620: 82 files, 1804368058 bytes, windows 1792044900 to 1792117800 of 509 considered; Release 414488168: sent 82, held 0, credential the primary checkout's remote URL; removed 82, freed 1804368058 bytes, free after 12728901632; restart: window 1792119600, pid 1420617 after 1312748, NRestarts 9; resume PASS at window 1792119600; complete: requests 169, started outside 0, ended outside 0, store 30286238 bytes, free 12710682624, rate 2112430897 a day
[2026-10-23T12:24:05Z] run 1792206020 2026-10-17T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792206020: 96 files, 2048827436 bytes, windows 1792118700 to 1792204200 of 605 considered; Release 415548049: sent 96, held 0, credential the primary checkout's remote URL; removed 96, freed 2048827436 bytes, free after 12725805056; restart: window 1792206000, pid 1560378 after 1420617, NRestarts 10; resume PASS at window 1792206000; complete: requests 197, started outside 0, ended outside 0, store 21346173 bytes, free 12715110400, rate 2048827436 a day
[2026-10-23T12:24:05Z] run 1792226137 2026-10-17T08:35:37Z, off-calendar, second 30937 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792226137: 23 files, 397545662 bytes, windows 1792205100 to 1792224900 of 628 considered; Release 415679936: sent 23, held 0, credential the primary checkout's remote URL; removed 23, freed 397545662 bytes, free after 12799180800; restart: window 1792226700, pid 1595407 after 1560378, NRestarts 11; resume PASS at window 1792226700; complete: requests 51, started outside 0, ended outside 0, store 25293180 bytes, free 12773187584, rate 1659321024 a day
[2026-10-23T12:24:05Z] run 1792292420 2026-10-18T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792292420: 73 files, 1197040692 bytes, windows 1792225800 to 1792290600 of 701 considered; Release 416201489: sent 73, held 0, credential the primary checkout's remote URL; removed 73, freed 1197040692 bytes, free after 12776620032; restart: window 1792292400, pid 1692402 after 1595407, NRestarts 12; resume PASS at window 1792292400; complete: requests 151, started outside 0, ended outside 0, store 24161003 bytes, free 12764577792, rate 1574190499 a day
[2026-10-23T12:24:05Z] run 1792378820 2026-10-19T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792378820: 96 files, 1755430954 bytes, windows 1792291500 to 1792377000 of 797 considered; Release 416860290: sent 96, held 0, credential the primary checkout's remote URL; removed 96, freed 1755430954 bytes, free after 12737359872; restart: window 1792378800, pid 1814768 after 1692402, NRestarts 13; resume PASS at window 1792378800; complete: requests 197, started outside 0, ended outside 0, store 38026457 bytes, free 12720193536, rate 1755430954 a day
[2026-10-23T12:24:05Z] run 1792446859 2026-10-19T21:54:19Z, off-calendar, second 78859 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792446859: 76 files, 1702929677 bytes, windows 1792377900 to 1792445400 of 873 considered; Release 417794290: sent 76, held 0, credential the primary checkout's remote URL; removed 76, freed 1702929677 bytes, free after 12726702080; restart: window 1792448100, pid 1915093 after 1814768, NRestarts 14; resume PASS at window 1792448100; complete: requests 157, started outside 0, ended outside 0, store 60078470 bytes, free 12678688768, rate 2151069065 a day
[2026-10-23T12:24:05Z] run 1792465220 2026-10-20T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792465220: 20 files, 428604581 bytes, windows 1792446300 to 1792463400 of 893 considered; Release 417955485: sent 20, held 0, credential the primary checkout's remote URL; removed 20, freed 428604581 bytes, free after 12736249856; restart: window 1792465200, pid 1942330 after 1915093, NRestarts 15; resume PASS at window 1792465200; complete: requests 45, started outside 0, ended outside 0, store 42260469 bytes, free 12714721280, rate 2057301988 a day
[2026-10-23T12:24:05Z] run 1792495417 2026-10-20T11:23:37Z, off-calendar, second 41017 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792495417: 34 files, 764815296 bytes, windows 1792464300 to 1792494000 of 927 considered; Release 418317989: sent 34, held 0, credential the primary checkout's remote URL; removed 34, freed 764815296 bytes, free after 12638756864; restart: window 1792495800, pid 1997029 after 1942330, NRestarts 16; resume PASS at window 1792495800; complete: requests 73, started outside 0, ended outside 0, store 31416312 bytes, free 12627136512, rate 2159478482 a day
[2026-10-23T12:24:05Z] run 1792551620 2026-10-21T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792551620: 62 files, 1362902551 bytes, windows 1792494900 to 1792549800 of 989 considered; Release 419096475: sent 62, held 0, credential the primary checkout's remote URL; removed 62, freed 1362902551 bytes, free after 12585439232; restart: window 1792551600, pid 2076364 after 1997029, NRestarts 17; resume PASS at window 1792551600; complete: requests 129, started outside 0, ended outside 0, store 38435764 bytes, free 12568043520, rate 2110300724 a day
[2026-10-23T12:24:05Z] run 1792618744 2026-10-21T21:39:04Z, off-calendar, second 77944 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792618744: 75 files, 1697351287 bytes, windows 1792550700 to 1792617300 of 1064 considered; Release 420082380: sent 75, held 0, credential the primary checkout's remote URL; removed 75, freed 1697351287 bytes, free after 12533227520; restart: window 1792619100, pid 2192943 after 2076364, NRestarts 18; resume PASS at window 1792619100; complete: requests 155, started outside 0, ended outside 0, store 53078752 bytes, free 12508360704, rate 2172609647 a day
[2026-10-23T12:24:05Z] run 1792638020 2026-10-22T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792638020: 21 files, 391495954 bytes, windows 1792618200 to 1792636200 of 1085 considered; Release 420262131: sent 21, held 0, credential the primary checkout's remote URL; removed 21, freed 391495954 bytes, free after 12514353152; restart: window 1792638000, pid 2221487 after 2192943, NRestarts 19; resume PASS at window 1792638000; complete: requests 47, started outside 0, ended outside 0, store 42282498 bytes, free 12499591168, rate 1789695789 a day
[2026-10-23T12:24:05Z] run 1792650248 2026-10-22T06:24:08Z, off-calendar, second 23048 of the day: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792650248: 14 files, 280783691 bytes, windows 1792637100 to 1792648800 of 1099 considered; Release 420372582: sent 14, held 0, credential the primary checkout's remote URL; removed 14, freed 280783691 bytes, free after 12560494592; restart: window 1792650600, pid 2250075 after 2241902, NRestarts 1; resume PASS at window 1792650600; complete: requests 33, started outside 0, ended outside 0, store 38684086 bytes, free 12529709056, rate 1925373881 a day
[2026-10-23T12:24:05Z] run 1792724420 2026-10-23T03:00:20Z, calendar: 10 records ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']; terminal complete; set pairbook-streams-1792724420: 82 files, 1595061931 bytes, windows 1792649700 to 1792722600 of 1181 considered; Release 421406556: sent 82, held 0, credential the primary checkout's remote URL; removed 82, freed 1595061931 bytes, free after 12469579776; restart: window 1792724400, pid 2371078 after 2250075, NRestarts 2; resume PASS at window 1792724400; complete: requests 169, started outside 0, ended outside 0, store 38897268 bytes, free 12451762176, rate 1867389577 a day
[2026-10-23T12:24:06Z] tags on origin 19: ['pairbook-streams-1791731892', 'pairbook-streams-1791774020', 'pairbook-streams-1791860420', 'pairbook-streams-1791946820', 'pairbook-streams-1792033220', 'pairbook-streams-1792045110', 'pairbook-streams-1792119620', 'pairbook-streams-1792206020', 'pairbook-streams-1792226137', 'pairbook-streams-1792292420', 'pairbook-streams-1792378820', 'pairbook-streams-1792446859', 'pairbook-streams-1792465220', 'pairbook-streams-1792495417', 'pairbook-streams-1792551620', 'pairbook-streams-1792618744', 'pairbook-streams-1792638020', 'pairbook-streams-1792650248', 'pairbook-streams-1792724420']
[2026-10-23T12:24:06Z] the ledger's sets 19, 1130 files, 23073393522 bytes; their tags not on origin []; tags on origin without a set []
[2026-10-23T12:24:06Z] runs 19; without a terminal record []; windows skipped between consecutive sets []; halted False
[2026-10-23T12:24:06Z] malloc tuned: True
[2026-10-23T12:24:06Z] peak memory of this run: 30593024 bytes
[2026-10-23T12:24:06Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

The second read at §3.10, `logs/25-archive-2.log`, is identical line for line once the stamps are removed, except its
peak (`30,330,880` bytes). The ledger was `0a15983e…`, 45,201 bytes and 190 records at both reads, with no run between
them.

**Since map §2.5's account:** two runs, `1792650248` and `1792724420`. `1792650248`, off the calendar at 2026-10-22
06:24:08 UTC, was read by the map from its tag alone. Its ledger records a set of 14 files, windows `1792637100` …
`1792648800`, exactly the map's conditional, and a restart from pid `2241902` to `2250075` at `NRestarts` 1. The pair book's
`NRestarts` had reset from 19, the count after the 03:00:20 run, which had restarted it to pid `2221487`.
`1792724420` is the calendar run of 2026-10-23 03:00:20 UTC: 82 files, a restart to pid `2371078` at `NRestarts` 2.
Its tag makes the 61 ref lines §0.5 projected. All 19 runs are `complete`, no window was skipped between sets, no
request started or ended outside the idle stretch, and the archive is not halted.

**Each run off the calendar, set beside §0.3's reads** (map §7 item 115). The boots: one, since 2026-08-02 07:24:34
UTC, at both runs. The timer's journal since 2026-10-14: `-- No entries --`. Systemd's reload records and the package
history, `logs/03-host-gate.log`. Its `tail -n 80` reaches back to 2026-10-20 11:13:34, so the three earlier off-calendar
runs fall outside it:

| run | start, UTC | nearest record before it, from §0.3's reads and §2.9's journal | gap |
|---|---|---|---|
| `1792495417` | 2026-10-20 11:23:37 | a burst of systemd reloads requested by `crypto-deploy.service`, ending 11:13:37 | 600 s |
| `1792618744` | 2026-10-21 21:39:04 | a burst of systemd reloads requested by `crypto-deploy.service`, ending 21:29:03 | 601 s |
| `1792650248` | 2026-10-22 06:24:08 | `unattended-upgrade` of liblzma5/xz-utils from 06:14:05; the recorder and the pair book stopped and started by systemd at 06:14:07–06:14:10 | 601 s from the units' restart |
| `1792045110`, `1792226137`, `1792446859` | 2026-10-15 06:18:30, 10-17 08:35:37, 10-19 21:54:19 | outside this tail; the package history's 40 lines begin at 2026-10-16 | — |

Each listed run started about 600 s, the timer's `OnActiveSec`, after another unit's reloads or after a package
upgrade that restarted the capture units. This is a coincidence of printed records, not a measured cause. Not every such restart was followed by a run: the units'
stop and start at 2026-10-23 06:08:56 UTC had no run 600 s later. No TZ ran at any of them.

### 2.6 The units, at both reads (§3.3, §3.9; V10)

```text
$ I still            # §3.3
[2026-10-23T12:23:31Z] btc-pairbook.service {'MainPID': '2388406', 'NRestarts': '0', 'ActiveState': 'active'}, MemoryCurrent 1601536, MemoryPeak 100466688
[2026-10-23T12:23:31Z] btc-recorder.service {'MainPID': '2388318', 'NRestarts': '0', 'ActiveState': 'active'}, MemoryCurrent 11984896, MemoryPeak 256856064
[2026-10-23T12:23:31Z] btc-pairbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-23T12:23:31Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-23T12:23:31Z] still: recorded
[2026-10-23T12:23:31Z] malloc tuned: True
[2026-10-23T12:23:31Z] peak memory of this run: 30322688 bytes
[2026-10-23T12:23:31Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
$ I still            # §3.9
[2026-10-23T13:02:26Z] btc-pairbook.service {'MainPID': '2388406', 'NRestarts': '0', 'ActiveState': 'active'}, MemoryCurrent 10612736, MemoryPeak 100466688
[2026-10-23T13:02:26Z] btc-recorder.service {'MainPID': '2388318', 'NRestarts': '0', 'ActiveState': 'active'}, MemoryCurrent 53993472, MemoryPeak 267509760
[2026-10-23T13:02:26Z] btc-pairbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-23T13:02:26Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-23T13:02:26Z] G-STILL PASS: unchanged since 2026-10-23T12:23:31Z
[2026-10-23T13:02:26Z] malloc tuned: True
[2026-10-23T13:02:26Z] peak memory of this run: 30322688 bytes
[2026-10-23T13:02:26Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

§3.10's `systemctl show` at 13:02:50 UTC: the recorder `2388318`, `NRestarts` 0, `active`, `MemoryCurrent` `9,105,408`,
`MemoryPeak` `267,509,760`; the pair book `2388406`, `NRestarts` 0, `active`, `MemoryCurrent` `1,630,208`, `MemoryPeak`
`100,466,688`; the archive's service `inactive`.

### 2.7 Free space and memory

| instant (UTC) | read | value | bound |
|---|---|---|---|
| 12:22:13 | `df` `/dev/vda2` avail (§0.3) | `11,694,059,520` | `5,250,000,000` |
| 12:22:13 | `MemAvailable` (§0.3) | `265,348` kB = `271,716,352` | `172,064,768` |
| 12:24:25 | `MemAvailable` (`rehearse`) | `371,773,440` | `172,064,768` |
| 12:32:37 | `MemAvailable` (`fetch`) | `298,909,696` | `172,064,768` |
| 13:01:20 | `MemAvailable` (`constants` 1) | `313,843,712` | `172,064,768` |
| 13:01:45 | `MemAvailable` (`constants` 2) | `341,110,784` | `172,064,768` |
| 13:02:18 | `MemAvailable` (`score` 1) | `357,089,280` | `172,064,768` |
| 13:02:18 | `MemAvailable` (`score` 2) | `355,270,656` | `172,064,768` |
| 13:02:40 | `df` avail (§3.10) | `11,365,556,224` | `5,250,000,000` |
| 13:02:40 | `MemAvailable` (§3.10) | `351,216` kB = `359,645,184` | `172,064,768` |
| 13:02:50 | `free -b` available | `515,624,960` | — |
| 13:07:22 | `df` avail, after B-RECLAIM-OWN | `11,603,329,024` | — |

`du -sb` at 13:02:50: `/root/tz31-work` `257,187,697` bytes, `/root/.claude` `129,865,081`. At §0.3 and §3.10,
`/var/lib/btc-pairbook` was `827,217,954` and `895,445,658`, `/var/lib/btc-pairbook-archive` `5,715,071` and `5,715,071`,
and `/root/PROJECT_GAMING_PS5` `618,421,011` and `618,640,274`. `telemetry-watch.service` read `disabled` (exit 1) and
`inactive` (exit 3) at both.

### 2.8 Memory peaks (V12)

| mode | log | peak bytes | malloc tuned |
|---|---|---|---|
| `fingerprint` (I0) | 02 | `31,244,288` | True |
| `fingerprint` (I) | 06 | `31,371,264` | True |
| `selftest` | 09 | `31,641,600` | True |
| `still` | 10, 23 | `30,322,688`, `30,322,688` | True |
| `scratch` | 11 | `30,351,360` | True |
| `reclaim` (scratch) | 12 | `31,166,464` | True |
| `archive` | 14, 25 | `30,593,024`, `30,330,880` | True |
| `rehearse` | 15 | `69,427,200` | True |
| `fetch` | 18 | `84,865,024` | True |
| `constants` | 19, 20 | `68,632,576`, `68,747,264` | True |
| `score` | 21, 22 | `45,056,000`, `45,056,000` | True |

The largest, `fetch`'s `84,865,024`, is below half of §0.4's floor (`86,032,384`), the Architect's measured peak. `score`
peaked at `45,056,000` against the Architect's `42,106,880` (+7.0%); `constants` at `68,747,264` against `62,832,640`
(+9.4%). Both are under half the floor.

### 2.9 Restarts of the capture units outside this TZ — `logs/16-units-journal.log`, verbatim

This is a `journalctl` read, one of §2 item 5's permitted reads, which no §3 step names (§6 item 4):

```text
2026-10-21T03:06:14+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-21T03:06:14+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 26min 51.873s CPU time, 80.5M memory peak, 36.5M memory swap peak.
2026-10-21T03:06:19+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 17.
2026-10-21T03:06:19+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-21T21:51:05+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-21T21:51:05+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 32min 40.014s CPU time, 128.1M memory peak, 38.3M memory swap peak.
2026-10-21T21:51:10+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 18.
2026-10-21T21:51:10+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-22T03:03:32+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-22T03:03:32+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 8min 30.042s CPU time, 104.0M memory peak, 36.8M memory swap peak.
2026-10-22T03:03:38+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 19.
2026-10-22T03:03:38+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-22T06:14:07+00:00 vultr systemd[1]: Stopping btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed...
2026-10-22T06:14:07+00:00 vultr systemd[1]: Stopping btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C...
2026-10-22T06:14:10+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-22T06:14:10+00:00 vultr systemd[1]: Stopped btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-22T06:14:10+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 5min 26.481s CPU time, 47.2M memory peak, 33.7M memory swap peak.
2026-10-22T06:14:10+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-22T06:30:33+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-22T06:30:33+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 15.020s CPU time, 31.9M memory peak, 16.6M memory swap peak.
2026-10-22T06:30:38+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 1.
2026-10-22T06:30:38+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-23T03:07:04+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-23T03:07:04+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 33min 40.645s CPU time, 107.0M memory peak, 36.2M memory swap peak.
2026-10-23T03:07:09+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 2.
2026-10-23T03:07:09+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-23T06:08:56+00:00 vultr systemd[1]: Stopping btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed...
2026-10-23T06:08:56+00:00 vultr systemd[1]: Stopping btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C...
2026-10-23T06:08:56+00:00 vultr systemd[1]: btc-recorder.service: Deactivated successfully.
2026-10-23T06:08:56+00:00 vultr systemd[1]: Stopped btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C.
2026-10-23T06:08:56+00:00 vultr systemd[1]: btc-recorder.service: Consumed 5min 10.023s CPU time, 262.8M memory peak, 23.4M memory swap peak.
2026-10-23T06:08:56+00:00 vultr systemd[1]: Started btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C.
2026-10-23T06:08:58+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-23T06:08:58+00:00 vultr systemd[1]: Stopped btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-23T06:08:58+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 4min 56.161s CPU time, 128.0M memory peak, 19.7M memory swap peak.
2026-10-23T06:08:58+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
---
2026-10-23T06:08:56+00:00 vultr systemd[1]: Stopping btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed...
2026-10-23T06:08:56+00:00 vultr systemd[1]: Stopping btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C...
2026-10-23T06:08:56+00:00 vultr systemd[1]: btc-recorder.service: Deactivated successfully.
2026-10-23T06:08:56+00:00 vultr systemd[1]: Stopped btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C.
2026-10-23T06:08:56+00:00 vultr systemd[1]: btc-recorder.service: Consumed 5min 10.023s CPU time, 262.8M memory peak, 23.4M memory swap peak.
2026-10-23T06:08:56+00:00 vultr systemd[1]: Started btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C.
2026-10-23T06:08:58+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-23T06:08:58+00:00 vultr systemd[1]: Stopped btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-23T06:08:58+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 4min 56.161s CPU time, 128.0M memory peak, 19.7M memory swap peak.
2026-10-23T06:08:58+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
---
2026-10-22T06:14:07+00:00 vultr systemd[1]: Stopping btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed...
2026-10-22T06:14:07+00:00 vultr systemd[1]: Stopping btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C...
2026-10-22T06:14:08+00:00 vultr systemd[1]: btc-recorder.service: Deactivated successfully.
2026-10-22T06:14:08+00:00 vultr systemd[1]: Stopped btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C.
2026-10-22T06:14:08+00:00 vultr systemd[1]: btc-recorder.service: Consumed 1h 20min 51.525s CPU time, 259.2M memory peak, 27.6M memory swap peak.
2026-10-22T06:14:08+00:00 vultr systemd[1]: Started btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C.
2026-10-22T06:14:10+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-22T06:14:10+00:00 vultr systemd[1]: Stopped btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-22T06:14:10+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 5min 26.481s CPU time, 47.2M memory peak, 33.7M memory swap peak.
2026-10-22T06:14:10+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-22T06:14:24+00:00 vultr systemd[1]: crypto-announce.service: Scheduled restart job, restart counter is at 1.
2026-10-22T06:24:08+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
```

Map §3 and §6 record the recorder as pid `4148534`, `NRestarts` 2, since TZ-21. It is now pid `2388318`, `NRestarts` 0,
since 2026-10-23 06:08:56 UTC, and was stopped and started by systemd once before that, at 2026-10-22 06:14:07. Each
stop came in the second of an `unattended-upgrade` run in `/var/log/apt/history.log`. A `systemctl` stop and start
resets `NRestarts`, and so does the pair book's restart at both instants.

---

## 3. Publication

| step | outcome |
|---|---|
| branch | `tz-31-who-earns`, one commit `404288fb03ffd3619b2183f121d45688def8fba8` above `origin/main` `334cd7c`, adding `research/tz31-who-earns.py` alone |
| push | through `gh`'s stored login, `credential.helper=!gh auth git-credential` (TZ-31 §3.1), `exit=0`; `origin` carried it at **2026-10-23 12:23:07.134371788 UTC** by `ls-remote`, equal to the worktree's `HEAD` |
| pull request | **#30**, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/30`, open, head `404288f`, not merged |
| Release | none: TZ-31 §2 item 11 |
| report | this file, straight to `main` in one commit |

`logs/07-commit-push.log`, verbatim:

```text
commit exit=0
404288fb03ffd3619b2183f121d45688def8fba8 root <root@vultr.guest> 2026-10-23T12:23:04+00:00
 research/tz31-who-earns.py | 1523 ++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 1523 insertions(+)
remote: 
remote: Create a pull request for 'tz-31-who-earns' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-31-who-earns        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-31-who-earns -> tz-31-who-earns
exit=0
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new branch]      tz-31-who-earns -> origin/tz-31-who-earns
exit=0
branch 'tz-31-who-earns' set up to track 'origin/tz-31-who-earns'.
exit=0
2026-10-23T12:23:07.134371788Z
404288fb03ffd3619b2183f121d45688def8fba8	refs/heads/tz-31-who-earns
404288fb03ffd3619b2183f121d45688def8fba8
```

### 3.1 Contract §4.2's separation self-check (V13) — `logs/27-separation.log`, verbatim

Run after the push and the pull request and before this report's commit:

```text
2026-10-23T13:02:58Z
$ git rev-list origin/main | grep -c 404288fb03ffd3619b2183f121d45688def8fba8
0
$ git diff --name-only origin/main origin/tz-31-who-earns
research/tz31-who-earns.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
exit=1
$ git diff --name-status --numstat origin/main origin/tz-31-who-earns
A	research/tz31-who-earns.py
1523	0	research/tz31-who-earns.py
{"headRefOid":"404288fb03ffd3619b2183f121d45688def8fba8","mergedAt":null,"number":30,"state":"OPEN","url":"https://github.com/seahomebatumi-ai/btc-5m-twap/pull/30"}
```

The first line prints `0`: the implementation commit is not on `main`. The branch's diff against `origin/main` names
exactly one path, `A`, 1,523 lines. No `.parquet` or `.zip` is on `main`.

### 3.2 The refs (§0.5) — `logs/04-refs.log`

Read at 12:22:41 UTC, before §3.1's push: **61 ref lines**. These are `HEAD`, `main` at `334cd7c`, seven `tz-*`
branches, nineteen lightweight `pairbook-streams-*` tags, two annotated tags with their peeled lines, and 29
`refs/pull/*/head`. The map's 60 plus the tag of the archive's calendar run of 2026-10-23 03:00:20 UTC,
`pairbook-streams-1792724420`, is the count §0.5 projected. `main` carries revision `2026-10-22-a`, and
`refs/heads/tz-31-who-earns` did not exist. The commits on `main`'s first-parent line above `d973ff1`:
`efae20d65a6189a6f1e4008d98c39a4ae1eec260` (2026-10-22 15:05:17 UTC, "Update SYSTEM-MAP.md", `M SYSTEM-MAP.md`) and
`334cd7cba383bc27e5482615c95a6a42ead12b8e` (2026-10-22 15:06:15 UTC, "Add files via upload",
`A CryptoTZ/TZ-31-who-earns.md`).

---

## 4. Gate

| gate | quoted from TZ-31 §4 | deciding number | reading |
|---|---|---|---|
| **G-REHEARSAL** | §4.1's 18 figures equal, exactly | 18 of 18 equal | **PASS** |
| **G-SET** | 1,008 members, every chunk read back | 1,008 members; 336 of 336 chunks read back | **PASS** |
| **W0** | §4.3: `S >= thr` → W-EARN; `S <= δ · Sh − thr` → W-NO-EARN; otherwise UNDECIDABLE | `S` `26,777.413` against `thr` `16,811.245` and `δ · Sh − thr` `−644.760` | **W-EARN** |
| **G-STILL** | unchanged, or the pair book moved by the archive's own restarts alone | both units unchanged, 0 restart records since §3.3 | **PASS** |

W-EARN rests on a margin of `+9,966.168` USDC, `0.308` c a share, which is `0.59 thr`. The power the reading was not
allowed to consult was `0.447`. Nothing was tuned, and no gate was reinterpreted.

---

## 5. Validation

### 5.1 V1 — fingerprint (asserted)

`FINGERPRINT PASS` at §0.2 (12:22:03) and at §3.1 (12:22:56). Revision `2026-10-22-a`; anchors 6 of 6, 4 re-derived;
42 rows, 39 of 39 `frozen` equal, 2 `tracked`, 1 `reported`. §0.1 holds the lines.

### 5.2 V2 — the host gate (checked by the Executor against the printed values, not asserted by a script; any failure would have been BLOCKED) — `logs/03-host-gate.log`, verbatim

```text
Fri Oct 23 12:22:13 PM UTC 2026
1792758133
1
MemTotal:         978640 kB
MemAvailable:     265348 kB
SwapTotal:       3174396 kB
SwapFree:        2848628 kB
2026-08-02 07:24:32
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
 -5 23a31fad2f064f04b9e138eac29658f3 Sun 2026-06-14 19:50:27 UTC Fri 2026-06-26 14:13:44 UTC
 -4 a38e17445ce341bc8b877be9d3d4f648 Fri 2026-06-26 14:13:52 UTC Tue 2026-07-14 16:15:10 UTC
 -3 5f4d18a6ba8041bd80e7d1e192c5ee28 Tue 2026-07-14 16:15:20 UTC Fri 2026-07-17 01:01:21 UTC
 -2 b1b399c70c6e4dcc934755f70a2ca231 Fri 2026-07-17 01:01:43 UTC Fri 2026-07-24 14:55:46 UTC
 -1 285d6962c92c407d837d1ce329b93aa4 Fri 2026-07-24 14:55:54 UTC Sun 2026-08-02 07:23:49 UTC
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-02 07:24:34 UTC Fri 2026-10-23 12:22:13 UTC
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11694059520
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
3
3.12.3
16570 /root/btc-forensics/tz27-work--archive--set.json
ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd  /root/btc-forensics/tz27-work--archive--set.json
MainPID=2388318
Result=success
NRestarts=0
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC

MainPID=2388406
Result=success
NRestarts=0
Id=btc-pairbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-10-23 06:08:58 UTC

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
NEXT                        LEFT LAST                        PASSED UNIT                       ACTIVATES
Sat 2026-10-24 03:00:20 UTC  14h Fri 2026-10-23 03:00:20 UTC 9h ago btc-pairbook-archive.timer btc-pairbook-archive.service

1 timers listed.
-- No entries --
2026-10-20T11:13:34+00:00 vultr systemd[1]: Reloading...
2026-10-20T11:13:34+00:00 vultr systemd[1]: Reloading finished in 331 ms.
2026-10-20T11:13:34+00:00 vultr systemd[1]: Reloading requested from client PID 1994559 ('systemctl') (unit crypto-deploy.service)...
2026-10-20T11:13:34+00:00 vultr systemd[1]: Reloading...
2026-10-20T11:13:34+00:00 vultr systemd[1]: Reloading finished in 466 ms.
2026-10-20T11:13:35+00:00 vultr systemd[1]: Reloading requested from client PID 1994629 ('systemctl') (unit crypto-deploy.service)...
2026-10-20T11:13:35+00:00 vultr systemd[1]: Reloading...
2026-10-20T11:13:35+00:00 vultr systemd[1]: Reloading finished in 339 ms.
2026-10-20T11:13:35+00:00 vultr systemd[1]: Reloading requested from client PID 1994685 ('systemctl') (unit crypto-deploy.service)...
2026-10-20T11:13:35+00:00 vultr systemd[1]: Reloading...
2026-10-20T11:13:35+00:00 vultr systemd[1]: Reloading finished in 370 ms.
2026-10-20T11:13:35+00:00 vultr systemd[1]: Reloading requested from client PID 1994752 ('systemctl') (unit crypto-deploy.service)...
2026-10-20T11:13:35+00:00 vultr systemd[1]: Reloading...
2026-10-20T11:13:36+00:00 vultr systemd[1]: Reloading finished in 340 ms.
2026-10-20T11:13:36+00:00 vultr systemd[1]: Reloading requested from client PID 1994804 ('systemctl') (unit crypto-deploy.service)...
2026-10-20T11:13:36+00:00 vultr systemd[1]: Reloading...
2026-10-20T11:13:36+00:00 vultr systemd[1]: Reloading finished in 291 ms.
2026-10-20T11:13:36+00:00 vultr systemd[1]: Reloading requested from client PID 1994857 ('systemctl') (unit crypto-deploy.service)...
2026-10-20T11:13:36+00:00 vultr systemd[1]: Reloading...
2026-10-20T11:13:36+00:00 vultr systemd[1]: Reloading finished in 354 ms.
2026-10-20T11:13:36+00:00 vultr systemd[1]: Reloading requested from client PID 1994915 ('systemctl') (unit crypto-deploy.service)...
2026-10-20T11:13:36+00:00 vultr systemd[1]: Reloading...
2026-10-20T11:13:37+00:00 vultr systemd[1]: Reloading finished in 300 ms.
2026-10-20T11:13:37+00:00 vultr systemd[1]: Reloading requested from client PID 1994967 ('systemctl') (unit crypto-deploy.service)...
2026-10-20T11:13:37+00:00 vultr systemd[1]: Reloading...
2026-10-20T11:13:37+00:00 vultr systemd[1]: Reloading finished in 302 ms.
2026-10-20T11:23:37+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-20T11:45:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-20T11:45:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-20T11:45:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 11.759s CPU time.
2026-10-21T03:00:20+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-21T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-21T03:15:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-21T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 20.219s CPU time.
2026-10-21T21:29:00+00:00 vultr systemd[1]: Reloading requested from client PID 2190056 ('systemctl') (unit crypto-deploy.service)...
2026-10-21T21:29:00+00:00 vultr systemd[1]: Reloading...
2026-10-21T21:29:00+00:00 vultr systemd[1]: Reloading finished in 322 ms.
2026-10-21T21:29:00+00:00 vultr systemd[1]: Reloading requested from client PID 2190108 ('systemctl') (unit crypto-deploy.service)...
2026-10-21T21:29:00+00:00 vultr systemd[1]: Reloading...
2026-10-21T21:29:01+00:00 vultr systemd[1]: Reloading finished in 498 ms.
2026-10-21T21:29:01+00:00 vultr systemd[1]: Reloading requested from client PID 2190178 ('systemctl') (unit crypto-deploy.service)...
2026-10-21T21:29:01+00:00 vultr systemd[1]: Reloading...
2026-10-21T21:29:01+00:00 vultr systemd[1]: Reloading finished in 314 ms.
2026-10-21T21:29:01+00:00 vultr systemd[1]: Reloading requested from client PID 2190234 ('systemctl') (unit crypto-deploy.service)...
2026-10-21T21:29:01+00:00 vultr systemd[1]: Reloading...
2026-10-21T21:29:01+00:00 vultr systemd[1]: Reloading finished in 297 ms.
2026-10-21T21:29:02+00:00 vultr systemd[1]: Reloading requested from client PID 2190301 ('systemctl') (unit crypto-deploy.service)...
2026-10-21T21:29:02+00:00 vultr systemd[1]: Reloading...
2026-10-21T21:29:02+00:00 vultr systemd[1]: Reloading finished in 245 ms.
2026-10-21T21:29:02+00:00 vultr systemd[1]: Reloading requested from client PID 2190353 ('systemctl') (unit crypto-deploy.service)...
2026-10-21T21:29:02+00:00 vultr systemd[1]: Reloading...
2026-10-21T21:29:02+00:00 vultr systemd[1]: Reloading finished in 260 ms.
2026-10-21T21:29:02+00:00 vultr systemd[1]: Reloading requested from client PID 2190406 ('systemctl') (unit crypto-deploy.service)...
2026-10-21T21:29:02+00:00 vultr systemd[1]: Reloading...
2026-10-21T21:29:02+00:00 vultr systemd[1]: Reloading finished in 265 ms.
2026-10-21T21:29:02+00:00 vultr systemd[1]: Reloading requested from client PID 2190458 ('systemctl') (unit crypto-deploy.service)...
2026-10-21T21:29:02+00:00 vultr systemd[1]: Reloading...
2026-10-21T21:29:03+00:00 vultr systemd[1]: Reloading finished in 265 ms.
2026-10-21T21:29:03+00:00 vultr systemd[1]: Reloading requested from client PID 2190510 ('systemctl') (unit crypto-deploy.service)...
2026-10-21T21:29:03+00:00 vultr systemd[1]: Reloading...
2026-10-21T21:29:03+00:00 vultr systemd[1]: Reloading finished in 264 ms.
2026-10-21T21:29:03+00:00 vultr systemd[1]: Reloading requested from client PID 2190562 ('systemctl') (unit crypto-deploy.service)...
2026-10-21T21:29:03+00:00 vultr systemd[1]: Reloading...
2026-10-21T21:29:03+00:00 vultr systemd[1]: Reloading finished in 265 ms.
2026-10-21T21:39:04+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-21T22:00:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-21T22:00:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-21T22:00:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 25.465s CPU time.
2026-10-22T03:00:20+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-22T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-22T03:15:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-22T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 6.122s CPU time.
2026-10-22T06:24:08+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-22T06:45:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-22T06:45:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-22T06:45:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 4.377s CPU time.
2026-10-23T03:00:20+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-23T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-23T03:15:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-23T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 23.646s CPU time.
Start-Date: 2026-10-16  06:08:09
Commandline: /usr/bin/unattended-upgrade
Upgrade: apache2-utils:amd64 (2.4.58-1ubuntu8.16, 2.4.58-1ubuntu8.17)
End-Date: 2026-10-16  06:08:10
Start-Date: 2026-10-20  06:28:05
Commandline: /usr/bin/unattended-upgrade
Upgrade: git:amd64 (1:2.43.0-1ubuntu7.3, 1:2.43.0-1ubuntu7.4), git-man:amd64 (1:2.43.0-1ubuntu7.3, 1:2.43.0-1ubuntu7.4)
End-Date: 2026-10-20  06:28:07
Start-Date: 2026-10-20  06:28:11
Commandline: /usr/bin/unattended-upgrade
Upgrade: libxtst6:amd64 (2:1.2.3-1.1build1, 2:1.2.3-1.1ubuntu0.1)
End-Date: 2026-10-20  06:28:11
Start-Date: 2026-10-21  06:12:47
Commandline: /usr/bin/unattended-upgrade
Upgrade: tzdata:amd64 (2026c-0ubuntu0.24.04.1, 2026e-0ubuntu0.24.04.1)
End-Date: 2026-10-21  06:12:48
Start-Date: 2026-10-21  06:12:51
Commandline: /usr/bin/unattended-upgrade
Upgrade: python3-jwt:amd64 (2.7.0-1ubuntu0.3, 2.7.0-1ubuntu0.4)
End-Date: 2026-10-21  06:12:52
Start-Date: 2026-10-22  06:14:05
Commandline: /usr/bin/unattended-upgrade
Upgrade: liblzma5:amd64 (5.6.1+really5.4.5-1ubuntu0.3, 5.6.1+really5.4.5-1ubuntu0.4), xz-utils:amd64 (5.6.1+really5.4.5-1ubuntu0.3, 5.6.1+really5.4.5-1ubuntu0.4)
End-Date: 2026-10-22  06:14:06
Start-Date: 2026-10-22  06:14:16
Commandline: /usr/bin/unattended-upgrade
Upgrade: ca-certificates:amd64 (20260601~24.04.1, 20260816ubuntu0.24.04.1)
End-Date: 2026-10-22  06:14:19
Start-Date: 2026-10-23  06:08:55
Commandline: /usr/bin/unattended-upgrade
Upgrade: zlib1g-dev:amd64 (1:1.3.dfsg-3.1ubuntu2.2, 1:1.3.dfsg-3.1ubuntu2.3), zlib1g:amd64 (1:1.3.dfsg-3.1ubuntu2.2, 1:1.3.dfsg-3.1ubuntu2.3)
End-Date: 2026-10-23  06:08:55
Start-Date: 2026-10-23  06:09:02
Commandline: /usr/bin/unattended-upgrade
Upgrade: distro-info-data:amd64 (0.72-0ubuntu0.24.04.1, 2026.10.12-0ubuntu0.24.04.1)
End-Date: 2026-10-23  06:09:03
Start-Date: 2026-10-23  06:09:07
Commandline: /usr/bin/unattended-upgrade
Upgrade: libnss3:amd64 (2:3.98-1ubuntu0.2, 2:3.98-1ubuntu0.3)
End-Date: 2026-10-23  06:09:08
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
e8b46a85d61e1a17841962846f6d3012046c2d70
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
/root/tz30-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
/root/btc-pairbook-archive-svc exit=0
/var/lib/btc-pairbook-archive exit=0
1938
/root/btc-5m-twap       334cd7c [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
827217954	/var/lib/btc-pairbook
5715071	/var/lib/btc-pairbook-archive
129468861	/root/.claude
618421011	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/917cd7ac-51fd-50da-a0d7-5b331470eff3/scratchpad
total 28
drwx------  7 root root 4096 Oct 23 12:20 .
drwx------ 25 root root 4096 Oct 23 12:20 ..
drwx------  3 root root 4096 Oct 23 12:20 19ca9482-c685-4646-b5db-a89314b67236
drwx------  4 root root 4096 Oct 22 03:22 2f1eadf7-1958-5f4f-857d-ccf68aa47272
drwx------  4 root root 4096 Oct 23 12:20 917cd7ac-51fd-50da-a0d7-5b331470eff3
drwx------  3 root root 4096 Oct 22 03:22 c498ebed-32dd-4005-9ebd-4fcce8ce6682
drwx------  3 root root 4096 Oct 21 09:37 eff3ddd1-cb45-4950-82cd-35b28b9c2c61
```

- **H1** — `find` printed one path. **PASS**.
- **H2** — `/dev/vda2`, `31612203008`; `grep -c` printed `3`, at least 1. **PASS**.
- **H3** — `3.12.3`. **PASS**.
- **H4** — `16570` bytes, `ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd`. **PASS**.
- **Memory** — `MemAvailable` `271,716,352` bytes ≥ `172,064,768`. **PASS**.
- **Disk** — avail `11,694,059,520` ≥ `5,250,000,000`. **PASS**.

Printed, no threshold: the three code trees at `e3975b5…`, `e8b46a8…` and `d8194fd…` as map §3 states. `/root/tz30-work`
was absent and the code and state trees present. The forensic store held `1,938` files, map §3's count. The worktrees
were the primary checkout and `/root/btc-recorder-svc`, map §3's two. The units: the recorder and the pair book
`active`, each at `NRestarts` 0 since 2026-10-23 06:08:56/58 UTC (§2.9); the archive's service `inactive`; its timer
`active`, `enabled`, next 2026-10-24 03:00:20 UTC; the chain book `disabled`. The §3.10 run of the same block,
`logs/24-host-gate-2.log`, differs from this one only in its instants, `MemAvailable` `351,216` kB, `SwapFree`, `df`
avail `11,365,556,224`, the `list-timers` line, the worktree list (adding `/root/tz31-work/wt 404288f`), the `du` figures
of §2.7, and the scratch directory's listing (only `19ca9482…` and this session's own remaining).

### 5.3 V3 — the file (asserted)

`logs/01-stage.log` at §0.1, and `logs/05-branch.log` at §3.1:

```text
/root/tz31-work/stage/research/tz31-who-earns.py 1523 84775 7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765
exit=0
exit=0
6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f  /root/tz31-work/stage/research/tz23-maker-m0.py
---
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new tag]         pairbook-streams-1792650248 -> pairbook-streams-1792650248
 * [new tag]         pairbook-streams-1792724420 -> pairbook-streams-1792724420
exit=0
Preparing worktree (new branch 'tz-31-who-earns')
branch 'tz-31-who-earns' set up to track 'origin/main'.
HEAD is now at 334cd7c Add files via upload
exit=0
/root/tz31-work/wt/research/tz31-who-earns.py 1523 84775 7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765
exit=0
6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f  /root/tz31-work/wt/research/tz23-maker-m0.py
```

1 of 1 hash asserted at each, 1,523 lines and 84,775 bytes. TZ-23's file was `6b3ace2c…` at each. The branch's diff
against `origin/main` names exactly one path, `A`, 1,523 lines (§3.1).

### 5.4 V4 — the self-test (asserted): **58 of 58** — `logs/09-selftest.log`, verbatim

```text
$ I selftest
[2026-10-23T12:23:21Z]   ok  TZ-23's instrument loaded from beside this file, from its asserted bytes
[2026-10-23T12:23:21Z]   ok  glibc took the 128 KiB mmap threshold and the two arenas
[2026-10-23T12:23:21Z]   ok  the main thread sums at 60 digits
[2026-10-23T12:23:21Z]   ok  TZ-23's step, document chunk, resolution age, slack and workers
[2026-10-23T12:23:21Z]   ok  half a tick a share; the fee 0.07 s p (1 - p), the rebate a fifth of it, as the documents must state
[2026-10-23T12:23:21Z]   ok  every request carries TZ-23's two headers
[2026-10-23T12:23:21Z]   ok  a market's life is every fill before T0 + 300: TZ-23's bands but post
[2026-10-23T12:23:21Z]   ok  the walk starts at 2026-10-19 23:15 UTC, the market after M0's last
[2026-10-23T12:23:21Z]   ok  no set is read before 2026-10-23T12:15:00Z, the last member's resolution age if every candidate qualifies
[2026-10-23T12:23:21Z]   ok  no excluded span reaches the set
[2026-10-23T12:23:21Z]   ok  the formation is M0's last 864 markets and the rehearsal its last 144
[2026-10-23T12:23:21Z]   ok  TZ-23's walk from 1792451700 takes 50 members in 50 documents and requests none at or below M0's last
[2026-10-23T12:23:21Z]   ok  the set's members are 336 chunks of fills
[2026-10-23T12:23:21Z]   ok  each group names 10 distinct wallets: the makers' rows, gated; the takers', barred
[2026-10-23T12:23:21Z]   ok  the makers' rows are the full feed less the takers', as multisets; a transaction whose sizes differ counted
[2026-10-23T12:23:21Z]   ok  sizes 4 + 6 against 10 are equal; a transaction with the takers' rows alone is counted
[2026-10-23T12:23:21Z]   ok  a takers' row absent from the full feed is a failed assert
[2026-10-23T12:23:21Z]   ok  own rows: BUY Up +s at p, SELL Up -s at p, BUY Down -s at 1 - p, SELL Down +s at 1 - p
[2026-10-23T12:23:21Z]   ok  maker, Up 0: X up - C plus the rebate or less the fee equals the row-by-row money
[2026-10-23T12:23:21Z]   ok  taker, Up 0: X up - C plus the rebate or less the fee equals the row-by-row money
[2026-10-23T12:23:21Z]   ok  maker, Up 1: X up - C plus the rebate or less the fee equals the row-by-row money
[2026-10-23T12:23:21Z]   ok  taker, Up 1: X up - C plus the rebate or less the fee equals the row-by-row money
[2026-10-23T12:23:21Z]   ok  a fill at T0 + 300 is post: outside every life sum
[2026-10-23T12:23:21Z] labels: 23 members, 16 Up
[2026-10-23T12:23:21Z] makers: S -509.77546109972 = settlement -552.52084 + rebate 42.74537890028; per share -0.027004194438 = -0.029268533567 + 0.002264339128
[2026-10-23T12:23:21Z] makers: W-EARN False (margin -6385.548569299217); W-NO-EARN False (margin -5271.609447099777)
[2026-10-23T12:23:21Z] makers barred: wallet 0x0000000000000000000000000000000000000001, 13 members, shares 4520.55, S 785.312863800840, per share 0.173720645453
[2026-10-23T12:23:21Z] makers barred: wallet 0x0000000000000000000000000000000000000002, 16 members, shares 6690.08, S -512.720325212500, per share -0.076638892990
[2026-10-23T12:23:21Z] makers barred: wallet 0x0000000000000000000000000000000000000003, 14 members, shares 7667.01, S -782.367999688060, per share -0.102043430188
[2026-10-23T12:23:21Z] makers barred: band pre  shares 3436.27, S 689.942320455440, per share 0.200782336794
[2026-10-23T12:23:21Z] makers barred: band w0   shares 2615.22, S 78.769622267400, per share 0.030119692518
[2026-10-23T12:23:21Z] makers barred: band w1   shares 1684.62, S 410.442805671820, per share 0.243641180606
[2026-10-23T12:23:21Z] makers barred: band w2   shares 4644.36, S -218.707871743920, per share -0.047091067821
[2026-10-23T12:23:21Z] makers barred: band w3   shares 3305.95, S -1141.803827449440, per share -0.345378432054
[2026-10-23T12:23:21Z] makers barred: band last shares 3191.22, S -328.418510301020, per share -0.102913152431
[2026-10-23T12:23:21Z] makers barred: band post shares 3682.31, S -1067.915498769940, per share -0.290012383197
[2026-10-23T12:23:21Z] takers: S -694.8824544238 = settlement -445.20450 + fee -249.6779544238; per share -0.029943879316 = -0.019184755255 + -0.010759124061
[2026-10-23T12:23:21Z] takers, barred from every reading: W-EARN False (margin -24799.788377776380); W-NO-EARN False (margin -23293.992668928780)
[2026-10-23T12:23:21Z] takers barred: wallet 0x0000000000000000000000000000000000000003, 16 members, shares 7884.31, S -640.741729684000, per share -0.081267952387
[2026-10-23T12:23:21Z] takers barred: wallet 0x0000000000000000000000000000000000000004, 17 members, shares 7921.92, S -589.316320211100, per share -0.074390592206
[2026-10-23T12:23:21Z] takers barred: wallet 0x0000000000000000000000000000000000000005, 16 members, shares 7399.93, S 535.175595471300, per share 0.072321710539
[2026-10-23T12:23:21Z] takers barred: band pre  shares 2920.46, S 243.799435316800, per share 0.083479806372
[2026-10-23T12:23:21Z] takers barred: band w0   shares 4097.08, S -767.712939222500, per share -0.187380509832
[2026-10-23T12:23:21Z] takers barred: band w1   shares 4348.65, S 227.458954192700, per share 0.052305647544
[2026-10-23T12:23:21Z] takers barred: band w2   shares 3779.99, S -797.167974487700, per share -0.210891556456
[2026-10-23T12:23:21Z] takers barred: band w3   shares 3764.68, S -545.894608218300, per share -0.145004252212
[2026-10-23T12:23:21Z] takers barred: band last shares 4295.30, S 944.634677995200, per share 0.219922864060
[2026-10-23T12:23:21Z] takers barred: band post shares 2212.14, S -167.316872577800, per share -0.075635752067
[2026-10-23T12:23:21Z] barred: every maker together: S -422.680679209280 on 61040.93 shares, -0.006924545206 a share
[2026-10-23T12:23:21Z] barred: every taker together: S -2219.844382162900 on 60676.56 shares, -0.036584875315 a share
[2026-10-23T12:23:21Z] the feeds: 530 transactions, makers' and takers' sizes differ at 0, one side only at 530
[2026-10-23T12:23:21Z] wrote x-makers-scored.csv sha256 2b262942bbd204d1dc35ab114e1db56a68d70812c21dc3d9441cedaa1dcbc693
[2026-10-23T12:23:21Z] wrote x-takers-scored.csv sha256 d04413412ec7db1b8e79b9acd765302caf21dc7c044d80a8d046be7763c534f0
[2026-10-23T12:23:21Z] wrote x-reading.json sha256 651821fa21b8ec6418aa7b300c32d098853a0b249505561bf6da9dc4c9da1837
[2026-10-23T12:23:21Z]   ok  makers: S over the synthetic set equals the row-by-row money of every fill before T0 + 300
[2026-10-23T12:23:21Z]   ok  makers: the wallets' sums add to S, and the bands' to S with post beside it
[2026-10-23T12:23:21Z]   ok  takers: S over the synthetic set equals the row-by-row money of every fill before T0 + 300
[2026-10-23T12:23:21Z]   ok  takers: the wallets' sums add to S, and the bands' to S with post beside it
[2026-10-23T12:23:21Z]   ok  every constants file is byte-identical with every label flipped
[2026-10-23T12:23:21Z] labels: 23 members, 7 Up
[2026-10-23T12:23:21Z] makers: S -1026.51546109972 = settlement -1069.26084 + rebate 42.74537890028; per share -0.054377319469 = -0.056641658597 + 0.002264339128
[2026-10-23T12:23:21Z] makers: W-EARN False (margin -6902.288569299217); W-NO-EARN False (margin -4754.869447099777)
[2026-10-23T12:23:21Z] makers barred: wallet 0x0000000000000000000000000000000000000001, 13 members, shares 4520.55, S -385.877136199160, per share -0.085360661026
[2026-10-23T12:23:21Z] makers barred: wallet 0x0000000000000000000000000000000000000002, 16 members, shares 6690.08, S -871.760325212500, per share -0.130306412661
[2026-10-23T12:23:21Z] makers barred: wallet 0x0000000000000000000000000000000000000003, 14 members, shares 7667.01, S 231.122000311940, per share 0.030144997895
[2026-10-23T12:23:21Z] makers barred: band pre  shares 3436.27, S 213.212320455440, per share 0.062047604075
[2026-10-23T12:23:21Z] makers barred: band w0   shares 2615.22, S -557.830377732600, per share -0.213301511052
[2026-10-23T12:23:21Z] makers barred: band w1   shares 1684.62, S -682.697194328180, per share -0.405252932013
[2026-10-23T12:23:21Z] makers barred: band w2   shares 4644.36, S -922.567871743920, per share -0.198642627131
[2026-10-23T12:23:21Z] makers barred: band w3   shares 3305.95, S 189.626172550560, per share 0.057359056414
[2026-10-23T12:23:21Z] makers barred: band last shares 3191.22, S 733.741489698980, per share 0.229925072448
[2026-10-23T12:23:21Z] makers barred: band post shares 3682.31, S 1164.054501230060, per share 0.316120723467
[2026-10-23T12:23:21Z] takers: S -2283.9424544238 = settlement -2034.26450 + fee -249.6779544238; per share -0.098419663332 = -0.087660539271 + -0.010759124061
[2026-10-23T12:23:21Z] takers, barred from every reading: W-EARN False (margin -26388.848377776380); W-NO-EARN False (margin -21704.932668928780)
[2026-10-23T12:23:21Z] takers barred: wallet 0x0000000000000000000000000000000000000003, 16 members, shares 7884.31, S -1099.231729684000, per share -0.139420155941
[2026-10-23T12:23:21Z] takers barred: wallet 0x0000000000000000000000000000000000000004, 17 members, shares 7921.92, S 1006.883679788900, per share 0.127100965396
[2026-10-23T12:23:21Z] takers barred: wallet 0x0000000000000000000000000000000000000005, 16 members, shares 7399.93, S -2191.594404528700, per share -0.296164207571
[2026-10-23T12:23:21Z] takers barred: band pre  shares 2920.46, S -332.920564683200, per share -0.113995933751
[2026-10-23T12:23:21Z] takers barred: band w0   shares 4097.08, S -99.492939222500, per share -0.024283865393
[2026-10-23T12:23:21Z] takers barred: band w1   shares 4348.65, S -770.811045807300, per share -0.177252951101
[2026-10-23T12:23:21Z] takers barred: band w2   shares 3779.99, S 489.542025512300, per share 0.129508814974
[2026-10-23T12:23:21Z] takers barred: band w3   shares 3764.68, S -286.214608218300, per share -0.076026277989
[2026-10-23T12:23:21Z] takers barred: band last shares 4295.30, S -1284.045322004800, per share -0.298941941658
[2026-10-23T12:23:21Z] takers barred: band post shares 2212.14, S 14.363127422200, per share 0.006492865471
[2026-10-23T12:23:21Z] barred: every maker together: S -1314.410679209280 on 61040.93 shares, -0.021533267583 a share
[2026-10-23T12:23:21Z] barred: every taker together: S -2880.324382162900 on 60676.56 shares, -0.047470133148 a share
[2026-10-23T12:23:21Z] the feeds: 530 transactions, makers' and takers' sizes differ at 0, one side only at 530
[2026-10-23T12:23:21Z] wrote x-makers-scored.csv sha256 9e3c6acf505407b592ac3c16ba63e9b6019d240629958a4346d773a367017383
[2026-10-23T12:23:21Z] wrote x-takers-scored.csv sha256 bb37322eee48eb0154b78f02f86dd08f6f4788ea2607058ff475357de680a935
[2026-10-23T12:23:21Z] wrote x-reading.json sha256 a601fdceba63856c0adf346e2507722d93a5ca73811cd6fb78af2aaf78c9d48b
[2026-10-23T12:23:21Z]   ok  the score moves when the labels flip (negative control)
[2026-10-23T12:23:21Z] unchanged /root/tz31-work/selftest-tmp/a/x-makers-fills.jsonl.gz sha256 2bef207f804927104f0f6b4e2cb7a01712f9936ff7f2a0321e2e4a60f58611be
[2026-10-23T12:23:21Z] unchanged /root/tz31-work/selftest-tmp/a/x-makers-members.csv sha256 04af32032086994c6f84212b21f857a814f4062ef9bb77982c727b88a81c59be
[2026-10-23T12:23:21Z] unchanged /root/tz31-work/selftest-tmp/a/x-makers-wallets.csv sha256 e67956293e32b0b63e3be79f2e43a1b3066cf1607102c301ea2d033c2f7bfe6b
[2026-10-23T12:23:21Z] unchanged /root/tz31-work/selftest-tmp/a/x-takers-fills.jsonl.gz sha256 895bfbf563c377e19a0442288fe45219afbb49d237f377ccdbdf9ec0b437b2e0
[2026-10-23T12:23:21Z] unchanged /root/tz31-work/selftest-tmp/a/x-takers-members.csv sha256 facb25ca7965b40ea2e0cc83738772000dd490f2ada2fdb56611bb4f328c6d12
[2026-10-23T12:23:21Z] unchanged /root/tz31-work/selftest-tmp/a/x-takers-wallets.csv sha256 340d19261d26354b757c5a8ff1a24f49071b7fb2494ae0513fbf448fbabe25e9
[2026-10-23T12:23:21Z] unchanged /root/tz31-work/selftest-tmp/a/x-pool.csv sha256 244c0b657548eec37f881ad4d88f115afc8466ff0c67f4e361dcca3b062630e2
[2026-10-23T12:23:21Z] unchanged /root/tz31-work/selftest-tmp/a/x-constants.json sha256 11aa978c0d9286687080754433e567b775015173370602eb7d826891805022b0
[2026-10-23T12:23:21Z]   ok  a second constants run finds every file unchanged
[2026-10-23T12:23:21Z]   ok  W-EARN at S >= thr, W-NO-EARN at S <= delta Sh - thr, W-EARN first where both hold
[2026-10-23T12:23:21Z]   ok  UNDECIDABLE between the bounds where they part
[2026-10-23T12:23:21Z]   ok  makers: at the projected V and Sh the threshold is 8026.39675309200283047593171014597323349 and the power between 0.9624 and 0.9625, the Architect's
[2026-10-23T12:23:21Z]   ok  takers: at the projected V and Sh the threshold is 35708.8558101879212986317691272476559876 and the power between 0.0225 and 0.0226, the Architect's
[2026-10-23T12:23:21Z]   ok  the rehearsal's 18 figures compare equal to themselves
[2026-10-23T12:23:21Z]   ok  one figure off by 1e-30 fails alone
[2026-10-23T12:23:21Z]   ok  a chunk starts from second 15 to 470 of a window and at no other second
[2026-10-23T12:23:21Z]   ok  nothing starts while the pair book streams, seconds 595 to 905
[2026-10-23T12:23:21Z]   ok  nothing starts from 03:00:15 to 03:01:20 UTC; at 03:01:21 a chunk may start
[2026-10-23T12:23:21Z]   ok  nothing starts while the archive's service runs; a failed one does not hold
[2026-10-23T12:23:21Z]   ok  held from second 600, a chunk starts at second 15 of the next window
[2026-10-23T12:23:21Z]   ok  an archive's run that never ends holds a chunk 7,200 s and then stops it BLOCKED
[2026-10-23T12:23:21Z] the walk starts at second 0 of window 0
[2026-10-23T12:23:21Z] the walk stopped (BLOCKED: the walk reached x, too recent to be resolved); walked again in 300 s, 1 of 24
[2026-10-23T12:23:21Z] the walk starts at second 0 of window 0
[2026-10-23T12:23:21Z] the walk stopped (BLOCKED: the walk reached x, too recent to be resolved); walked again in 300 s, 2 of 24
[2026-10-23T12:23:21Z] the walk starts at second 0 of window 0
[2026-10-23T12:23:21Z]   ok  a walk stopped twice on a market too recent is walked a third time, 300 s after each stop
[2026-10-23T12:23:21Z] the walk starts at second 0 of window 0
[2026-10-23T12:23:21Z]   ok  a walk stopped on its slack is not walked again
[2026-10-23T12:23:21Z] chunks 5 of 5, 0 s
[2026-10-23T12:23:21Z] chunks fetched fresh 5: inside the idle stretch 5, ending after second 590 0; longest 0.0 s; waited 0 s; windows 1, from 2026-10-20T01:00:00Z to 2026-10-20T01:00:00Z
[2026-10-23T12:23:21Z]   ok  14 members are 5 chunks of at most 3, each fetched once and timed inside the idle stretch
[2026-10-23T12:23:21Z] chunks 5 of 5, 0 s
[2026-10-23T12:23:21Z] chunks fetched fresh 5: inside the idle stretch 5, ending after second 590 0; longest 0.0 s; waited 0 s; windows 1, from 2026-10-20T01:00:00Z to 2026-10-20T01:00:00Z
[2026-10-23T12:23:21Z]   ok  a cached chunk is fetched again by nothing
[2026-10-23T12:23:21Z]   ok  every chunk reads back to its members
[2026-10-23T12:23:21Z] chunks 25 of 67, 31000 s
[2026-10-23T12:23:21Z] projected 61417 s of fetching for 67 chunks after 30 fetched; 32000 s of wall clock so far
[2026-10-23T12:23:26Z]   ok  a fetch projected above 7,200 s of fetching stops BLOCKED at its 30th chunk: at most the two chunks running end, and the 33 queued never start
[2026-10-23T12:23:26Z] chunks 25 of 67, 410 s
[2026-10-23T12:23:26Z] projected 726 s of fetching for 67 chunks after 30 fetched; 410 s of wall clock so far
[2026-10-23T12:23:26Z] chunks 50 of 67, 670 s
[2026-10-23T12:23:26Z] chunks 67 of 67, 670 s
[2026-10-23T12:23:26Z]   ok  a fetch projected under it fetches all 67 chunks
[2026-10-23T12:23:26Z]   ok  the ledger's runs, terminals, calendar, halt and gaps
[2026-10-23T12:23:26Z]   ok  a clear after a halt reads not halted
[2026-10-23T12:23:26Z]   ok  G-STILL: unchanged, or the pair book moved by a chain of the archive's restart records, each one NRestarts higher; a broken, reversed or missing chain or a changed recorder fails
[2026-10-23T12:23:26Z]   ok  the map's rows and anchors parse
[2026-10-23T12:23:26Z]   ok  reclaim takes the work tree and refuses the forensic store and a directory outside a session's
[2026-10-23T12:23:26Z]   ok  opens under the pair book's root and of the archive's ledger outside modes archive and still are refused by this hook, under the chain book's root by TZ-23's, each before it happens
[2026-10-23T12:23:26Z]   ok  TZ-23's own hook still refuses the recorder's root
[2026-10-23T12:23:26Z]   ok  modes archive and still read ledger.jsonl and nothing else of the archive's state, and write nothing there; no other mode reads it
[2026-10-23T12:23:26Z]   ok  the forensic store is written by reclaim's exclusive create alone, and nothing outside the work tree
[2026-10-23T12:23:26Z] 58 of 58 checks passed
[2026-10-23T12:23:26Z] malloc tuned: True
[2026-10-23T12:23:26Z] peak memory of this run: 31641600 bytes
[2026-10-23T12:23:26Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

`test -e /root/tz31-work/selftest-tmp` printed exit `1` after it: the self-test removed its temporary trees.

### 5.5 V5 — the archive's record (recorded, not asserted, gating nothing)

§2.5: the ledger's 45,201 bytes, SHA-256 `0a15983e…` and 190 records at both reads; 19 runs, each line printed; 19 tags
on `origin`, each with a set in the ledger and each set with its tag. The instrument's own exit was `0` at both.

### 5.6 V6 — G-REHEARSAL (asserted): **18 of 18**

§2.4. Every figure equal to the Architect's `REF` as a value: the members 144, the Up count 71, and for each group `n`,
`sh`, `X`, `C`, `R`, `V`, `P` and `S`.

### 5.7 V7 — G-SET (asserted)

1,008 members of 1,008 candidates considered, `1792451700` … `1792753800`, every non-member listed with its reason (0
of them), 336 chunks read back in order. The chunks: 336 inside the idle stretch and 0 ending after second 590 (§2.3).

### 5.8 V8 — the constants, twice (asserted): **8 of 8 `unchanged`** — `logs/20-constants-2.log`, verbatim

```text
$ I constants
[2026-10-23T13:01:45Z] MemAvailable 341110784 bytes, floor 172064768
[2026-10-23T13:02:10Z] unchanged /root/tz31-work/set/tz31-makers-fills.jsonl.gz sha256 33b3f44b855330f3fea9834985925d238a0b63214831bc392bfae5762e4cd882
[2026-10-23T13:02:10Z] unchanged /root/tz31-work/set/tz31-makers-members.csv sha256 93179e932d1d31eb2f34f27c18ca6523968c4bc3f44970cb4b980739e0d65f55
[2026-10-23T13:02:10Z] unchanged /root/tz31-work/set/tz31-makers-wallets.csv sha256 46d794fddcee1463bb774f0b28cd97b377a7c6080ca821a14f7c66b3e910f3a4
[2026-10-23T13:02:10Z] unchanged /root/tz31-work/set/tz31-takers-fills.jsonl.gz sha256 2d70895d19dc08e15e700fde70df8f4c026dc0d197d04d1d7aa6265f9391bdac
[2026-10-23T13:02:10Z] unchanged /root/tz31-work/set/tz31-takers-members.csv sha256 cca6c0fc376a7ea67eb0a3898c6f8c1053968cfea300a603c9c4b7019820874d
[2026-10-23T13:02:10Z] unchanged /root/tz31-work/set/tz31-takers-wallets.csv sha256 b359aa051e124147456dd31fae46cfd39ce21310f57c7f96d8ca4daeaafbfa86
[2026-10-23T13:02:10Z] unchanged /root/tz31-work/set/tz31-pool.csv sha256 c92fc59e4126959ed0ff15eab5de43c9825e195ad0284f738ea9439014bbfef4
[2026-10-23T13:02:10Z] unchanged /root/tz31-work/set/tz31-constants.json sha256 983edb35895f23ca97feb66638b15b58b9ff9014092fb088d6318d2f5df8173c
[2026-10-23T13:02:10Z] members 1008, considered 1008, first 1792451700 2026-10-19T23:15:00Z, last 1792753800 2026-10-23T11:10:00Z; member list sha e3d77b0a36847b1ef628f79ec78ed6b7d597bdc39a16d6ecf87786e91ed3f658
[2026-10-23T13:02:10Z] makers (maker rows of 10 wallets, 10 of them with a fill): members with a fill 1008; fills 247942, shares 3233296.885950, X 31656.656386, C -32269.6229014638713180, R 7709.76552580864758430019840922940
[2026-10-23T13:02:10Z] makers: V 92592808.871725414860; Sh 3233296.885950; lambda 0.00099017; L 5.298317366548; thr 16811.244574537803 (0.005199412602 a share)
[2026-10-23T13:02:10Z] makers: W-EARN at S >= 16811.244574537803 (0.005199412602 a share); W-NO-EARN at S <= -644.760144787803 (-0.000199412602 a share); power of either answer against the other's alternative 0.4466970475876927
[2026-10-23T13:02:10Z] takers (taker rows of 10 wallets, 10 of them with a fill): members with a fill 1007; fills 62062, shares 3439148.178239, X 41899.657517, C 166566.4211998413512639, R 7665.74255352260762600299818181526
[2026-10-23T13:02:10Z] takers: V 931903250.969297938379; Sh 3439148.178239; lambda 0.00022256; L 5.298317366548; thr 49731.791102587888 (0.014460496764 a share)
[2026-10-23T13:02:10Z] takers, barred from every reading: W-EARN at S >= 49731.791102587888 (0.014460496764 a share); W-NO-EARN at S <= -32536.050211392888 (-0.009460496764 a share); power of either answer against the other's alternative 0.016519124727650103
[2026-10-23T13:02:10Z] wrote /root/tz31-work/set/tz31-constants.json sha256 983edb35895f23ca97feb66638b15b58b9ff9014092fb088d6318d2f5df8173c
[2026-10-23T13:02:10Z] wrote /root/tz31-work/set/tz31-makers-fills.jsonl.gz sha256 33b3f44b855330f3fea9834985925d238a0b63214831bc392bfae5762e4cd882
[2026-10-23T13:02:10Z] wrote /root/tz31-work/set/tz31-makers-members.csv sha256 93179e932d1d31eb2f34f27c18ca6523968c4bc3f44970cb4b980739e0d65f55
[2026-10-23T13:02:10Z] wrote /root/tz31-work/set/tz31-makers-wallets.csv sha256 46d794fddcee1463bb774f0b28cd97b377a7c6080ca821a14f7c66b3e910f3a4
[2026-10-23T13:02:10Z] wrote /root/tz31-work/set/tz31-pool.csv sha256 c92fc59e4126959ed0ff15eab5de43c9825e195ad0284f738ea9439014bbfef4
[2026-10-23T13:02:10Z] wrote /root/tz31-work/set/tz31-takers-fills.jsonl.gz sha256 2d70895d19dc08e15e700fde70df8f4c026dc0d197d04d1d7aa6265f9391bdac
[2026-10-23T13:02:10Z] wrote /root/tz31-work/set/tz31-takers-members.csv sha256 cca6c0fc376a7ea67eb0a3898c6f8c1053968cfea300a603c9c4b7019820874d
[2026-10-23T13:02:10Z] wrote /root/tz31-work/set/tz31-takers-wallets.csv sha256 b359aa051e124147456dd31fae46cfd39ce21310f57c7f96d8ca4daeaafbfa86
[2026-10-23T13:02:10Z] malloc tuned: True
[2026-10-23T13:02:10Z] peak memory of this run: 68747264 bytes
[2026-10-23T13:02:10Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

`state.json` records `constants_sha` `983edb35895f23ca97feb66638b15b58b9ff9014092fb088d6318d2f5df8173c` and
`constants_at` `2026-10-23T13:02:10Z`, the second run's instant (§6 item 5).

### 5.9 V9 — the score, twice (asserted): the reading **W-EARN**; **3 of 3 `unchanged`**; **2 ledger lines**

`logs/22-score-2.log`, verbatim:

```text
$ I score
[2026-10-23T13:02:18Z] MemAvailable 355270656 bytes, floor 172064768
[2026-10-23T13:02:18Z] unchanged /root/tz31-work/set/tz31-makers-scored.csv sha256 4de2f3e8dcaf135f415c0726d6fb3710ba91516029e257382bef6f6a353f7eb7
[2026-10-23T13:02:18Z] unchanged /root/tz31-work/set/tz31-takers-scored.csv sha256 29b2b5e9ba8c3ac4ed9166c3492fe0de3db2b8a85588b66c4faca058c485b4c0
[2026-10-23T13:02:18Z] unchanged /root/tz31-work/set/tz31-reading.json sha256 d7dd8ee278c4f58bbf56ec9759ec3b2558cc49cc28725407d72d89c5471bd187
[2026-10-23T13:02:18Z] labels: 1008 members, 504 Up
[2026-10-23T13:02:18Z] makers: S 26777.41259327251890230019840922940 = settlement 19067.6470674638713180 + rebate 7709.76552580864758430019840922940; per share 0.008281767353 = 0.005897276910 + 0.002384490444
[2026-10-23T13:02:18Z] makers: W-EARN True (margin 9966.168018734716); W-NO-EARN False (margin -27422.172738060322)
[2026-10-23T13:02:18Z] makers barred: wallet 0x18c18e0c8c3154360b4f730ec8b9d8013ceb2183, 888 members, shares 766690.227163, S 4046.382542908080, per share 0.005277728083
[2026-10-23T13:02:18Z] makers barred: wallet 0x1dd2a69e73ba444ecd5d87f0073d51a670ad51c2, 968 members, shares 126529.138017, S 639.423987597721, per share 0.005053571040
[2026-10-23T13:02:18Z] makers barred: wallet 0x32c4922da31d9f90232ea40748846e5ccc48b175, 968 members, shares 144880.376200, S 841.681686845522, per share 0.005809494073
[2026-10-23T13:02:18Z] makers barred: wallet 0x373b2d17d78c27bbdbcb034dae71d26b8094c855, 943 members, shares 103465.221227, S 910.359788286153, per share 0.008798703347
[2026-10-23T13:02:18Z] makers barred: wallet 0x764fd57b0b885cbeada5a119cdf0a113ee4ec347, 973 members, shares 1481797.601735, S 16989.713554913711, per share 0.011465610104
[2026-10-23T13:02:18Z] makers barred: wallet 0x809f275254e21f720a4e6c50c28c669c721f2ef0, 958 members, shares 123921.799378, S 654.368004818334, per share 0.005280491472
[2026-10-23T13:02:18Z] makers barred: wallet 0xbfa0ed0c199c00aec969d822818f789ca35acd6d, 948 members, shares 99660.824197, S 797.394042429833, per share 0.008001078145
[2026-10-23T13:02:18Z] makers barred: wallet 0xd8f1fbe130e2b33f32633bf568a08b85058e74a9, 882 members, shares 56915.646773, S 758.838530983921, per share 0.013332687477
[2026-10-23T13:02:18Z] makers barred: wallet 0xf548517cbefe7636bef51ee31a1817f021e7c20e, 587 members, shares 55850.170040, S 882.107903256072, per share 0.015794184738
[2026-10-23T13:02:18Z] makers barred: wallet 0xf79dccd12edb1e599dc3f9bff979b95987609fe9, 1006 members, shares 273585.881220, S 257.142551233172, per share 0.000939897008
[2026-10-23T13:02:18Z] makers barred: band w0   shares 771546.115919, S 5292.999724290807, per share 0.006860250625
[2026-10-23T13:02:18Z] makers barred: band w1   shares 695919.978309, S 7408.014086986076, per share 0.010644922287
[2026-10-23T13:02:18Z] makers barred: band w2   shares 700429.045126, S 5496.240206435395, per share 0.007846962151
[2026-10-23T13:02:18Z] makers barred: band w3   shares 695953.005393, S 4356.576109721352, per share 0.006259871106
[2026-10-23T13:02:18Z] makers barred: band last shares 369448.741203, S 4223.582465838889, per share 0.011432120332
[2026-10-23T13:02:18Z] makers barred: band post shares 4907.589613, S -536.172923462042, per share -0.109253822292
[2026-10-23T13:02:18Z] takers: S 3171.1174995456106060850090909237 = settlement 41499.8302671586487361 + fee -38328.7127676130381300149909090763; per share 0.000922064807 = 0.012066892183 + -0.011144827376
[2026-10-23T13:02:18Z] takers, barred from every reading: W-EARN False (margin -46560.673603042278); W-NO-EARN False (margin -35707.167710938499)
[2026-10-23T13:02:18Z] takers barred: wallet 0x129246beaac356e104c397f0985c11b7469be5a6, 700 members, shares 79587.011039, S 3274.300661947054, per share 0.041141143752
[2026-10-23T13:02:18Z] takers barred: wallet 0x14ea1c239393f7c1ad68c72e34e250e0679583b5, 354 members, shares 107719.430210, S 563.420699695483, per share 0.005230446342
[2026-10-23T13:02:18Z] takers barred: wallet 0x19b3823092892c026517fd0ff58df4889abe0b9b, 698 members, shares 431484.72, S 2835.526544336595, per share 0.006571557260
[2026-10-23T13:02:18Z] takers barred: wallet 0x20d2309cd92b797ae7ca175ed828ed8a27fbe29d, 850 members, shares 113310.080119, S 670.374958468310, per share 0.005916287040
[2026-10-23T13:02:18Z] takers barred: wallet 0x3c58ef422754ff22c7e806336feba0064d8b776b, 775 members, shares 114076.01, S 2193.972613924009, per share 0.019232550419
[2026-10-23T13:02:18Z] takers barred: wallet 0x41e2e1ccf1e4940029af02259a31c6b89b9fa354, 459 members, shares 617121.302310, S -3193.764285062822, per share -0.005175261773
[2026-10-23T13:02:18Z] takers barred: wallet 0x5a06acbaee263540a16a0109d584f6672101ffa2, 523 members, shares 297770.216178, S -170.938829709785, per share -0.000574062886
[2026-10-23T13:02:18Z] takers barred: wallet 0x5e2b9261b0c4f697b55bf921ff2bc227183d9101, 955 members, shares 78816.748383, S 856.075817894907, per share 0.010861597763
[2026-10-23T13:02:18Z] takers barred: wallet 0xd84403efd50b49a1d8a7181627e00307e6ea5908, 893 members, shares 357896.71, S 2099.263596514204, per share 0.005865557123
[2026-10-23T13:02:18Z] takers barred: wallet 0xeebde7a0e019a63e6b476eb425505b7b3e6eba30, 809 members, shares 1241365.95, S -5957.114278462345, per share -0.004798838150
[2026-10-23T13:02:18Z] takers barred: band pre  shares 127015.303138, S -3357.876047578449, per share -0.026436783322
[2026-10-23T13:02:18Z] takers barred: band w0   shares 560110.171461, S -2839.665110280934, per share -0.005069833142
[2026-10-23T13:02:18Z] takers barred: band w1   shares 587799.004792, S -1316.100393513709, per share -0.002239031340
[2026-10-23T13:02:18Z] takers barred: band w2   shares 750898.164328, S -621.893110535316, per share -0.000828199002
[2026-10-23T13:02:18Z] takers barred: band w3   shares 900027.915576, S 4392.418612098723, per share 0.004880313750
[2026-10-23T13:02:18Z] takers barred: band last shares 513297.618944, S 6914.233549355296, per share 0.013470223305
[2026-10-23T13:02:18Z] takers barred: band post shares 122.45, S -17.249765165227, per share -0.140871908250
[2026-10-23T13:02:18Z] barred: every maker together: S 101101.193069263939 on 47815937.159942 shares, 0.002114382758 a share
[2026-10-23T13:02:18Z] barred: every taker together: S -484249.986895316530 on 47815937.734319 shares, -0.010127376139 a share
[2026-10-23T13:02:18Z] the feeds: 1512605 transactions, makers' and takers' sizes differ at 81, one side only at 0
[2026-10-23T13:02:18Z] wrote tz31-makers-scored.csv sha256 4de2f3e8dcaf135f415c0726d6fb3710ba91516029e257382bef6f6a353f7eb7
[2026-10-23T13:02:18Z] wrote tz31-takers-scored.csv sha256 29b2b5e9ba8c3ac4ed9166c3492fe0de3db2b8a85588b66c4faca058c485b4c0
[2026-10-23T13:02:18Z] wrote tz31-reading.json sha256 d7dd8ee278c4f58bbf56ec9759ec3b2558cc49cc28725407d72d89c5471bd187
[2026-10-23T13:02:18Z] W0 READING, THE MAKERS: W-EARN
[2026-10-23T13:02:18Z] malloc tuned: True
[2026-10-23T13:02:18Z] peak memory of this run: 45056000 bytes
[2026-10-23T13:02:18Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

| instant (UTC) | event |
|---|---|
| 12:23:07.134 | `ls-remote` prints `404288f` on `origin` (§3.1) |
| 13:01:45 | `tz31-constants.json` `983edb35…` first written (`constants` 1) |
| 13:02:10 | `state.json` records it again (`constants` 2) |
| **13:02:18** | **the first ledger line's `at`: the first label of the set read** |

`score` asserted that `state.json`'s `constants_sha` equals the file's hash, and that `origin/tz-31-who-earns` contains
`HEAD` `404288f`, before writing the ledger line and reading a label.

### 5.10 V10 — G-STILL (asserted): **PASS**, unchanged since 12:23:31 UTC (§2.6)

### 5.11 V11 — the hooks (asserted at every mode)

Every one of the 15 mode runs in `logs/` printed `opens refused: 0; under the recorder's and the chain book's roots by
TZ-23's hook: 0`: fingerprint ×2, selftest, still ×2, scratch, reclaim, archive ×2, rehearse, fetch, constants ×2 and
score ×2. B-RECLAIM-OWN's two `reclaim` runs in §5.16 printed the same.

### 5.12 V12 — memory (printed)

§2.8: every mode's peak below §0.4's floor of `172,064,768`, and `malloc tuned: True` at every mode run. Every
`MemAvailable` read at or above the floor (§2.7).

### 5.13 V13 — contract §4.2's self-check: §3.1, run after the push and the pull request and before this report's commit

### 5.14 V14 — §3.10's closing reads — `logs/26-closing.log`, verbatim

```text
2026-10-23T13:02:50Z
MainPID=2388318
NRestarts=0
MemoryCurrent=9105408
MemoryPeak=267509760
ActiveState=active

MainPID=2388406
NRestarts=0
MemoryCurrent=1630208
MemoryPeak=100466688
ActiveState=active

MainPID=0
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=[not set]
ActiveState=inactive
               total        used        free      shared  buff/cache   available
Mem:      1002127360   486502400    85786624       69632   577335296   515624960
Swap:     3250581504   549883904  2700697600
257187697	/root/tz31-work
129865081	/root/.claude
{
 "constants_at": "2026-10-23T13:02:10Z",
 "constants_sha": "983edb35895f23ca97feb66638b15b58b9ff9014092fb088d6318d2f5df8173c",
 "still": {
  "at": "2026-10-23T12:23:31Z",
  "at_ns": 1792758211119616570,
  "units": {
   "pairbook": {
    "ActiveState": "active",
    "MainPID": "2388406",
    "NRestarts": "0"
   },
   "recorder": {
    "ActiveState": "active",
    "MainPID": "2388318",
    "NRestarts": "0"
   }
  }
 }
}
{"at":"2026-10-23T13:02:18Z","head":"404288fb03ffd3619b2183f121d45688def8fba8","member_list_sha":"e3d77b0a36847b1ef628f79ec78ed6b7d597bdc39a16d6ecf87786e91ed3f658","members":1008}
{"at":"2026-10-23T13:02:18Z","head":"404288fb03ffd3619b2183f121d45688def8fba8","member_list_sha":"e3d77b0a36847b1ef628f79ec78ed6b7d597bdc39a16d6ecf87786e91ed3f658","members":1008}
```

The §0.3 block's second run is `logs/24-host-gate-2.log` (§5.2), and `I archive`'s is `logs/25-archive-2.log` (§2.5).

### 5.15 V15 — B-RECLAIM-SCRATCH, and the directories beside this session

`logs/11-scratch.log`, verbatim:

```text
$ I scratch /tmp/claude-0/-root-btc-5m-twap
[2026-10-23T12:23:31Z] running 2287221 started 2026-10-22T13:11:35Z claude
[2026-10-23T12:23:31Z] running 2287231 started 2026-10-22T13:11:37Z claude
[2026-10-23T12:23:31Z] running 2427892 started 2026-10-23T12:20:34Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-10-23T12:23:31Z] 19ca9482-c685-4646-b5db-a89314b67236 born 2026-10-23T12:20:35Z: live, process [2427892]
[2026-10-23T12:23:31Z] 2f1eadf7-1958-5f4f-857d-ccf68aa47272 born 2026-10-22T03:22:19Z: earlier
[2026-10-23T12:23:31Z] c498ebed-32dd-4005-9ebd-4fcce8ce6682 born 2026-10-22T03:22:17Z: earlier
[2026-10-23T12:23:31Z] eff3ddd1-cb45-4950-82cd-35b28b9c2c61 born 2026-10-21T09:37:21Z: earlier
[2026-10-23T12:23:31Z] malloc tuned: True
[2026-10-23T12:23:31Z] peak memory of this run: 30351360 bytes
[2026-10-23T12:23:31Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

`logs/12-reclaim-scratch.log` and `logs/13-rm-scratch.log`, verbatim:

```text
$ I reclaim /tmp/claude-0/-root-btc-5m-twap/2f1eadf7-1958-5f4f-857d-ccf68aa47272 /tmp/claude-0/-root-btc-5m-twap/c498ebed-32dd-4005-9ebd-4fcce8ce6682 /tmp/claude-0/-root-btc-5m-twap/eff3ddd1-cb45-4950-82cd-35b28b9c2c61
[2026-10-23T12:23:54Z] reclaim: 2746 report tokens; forensic store holds 1938 files
[2026-10-23T12:23:54Z] RECLAIM PASS: 8 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 1938 -> 1938 files
[2026-10-23T12:23:54Z] malloc tuned: True
[2026-10-23T12:23:54Z] peak memory of this run: 31166464 bytes
[2026-10-23T12:23:54Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
$ rm -rf <dir>; echo "exit=$?"; test -e <dir>; echo "exit=$?"     # one command per directory, in the order above
2026-10-23T12:24:02Z
exit=0
exit=1
2026-10-23T12:24:02Z
exit=0
exit=1
2026-10-23T12:24:02Z
exit=0
exit=1
```

8 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; the store `1,938 → 1,938`, after =
before + 0. Three directories removed, each `rm -rf` exit `0` and `test -e` exit `1`, **none refused**. `19ca9482…`,
born with this session's process `2427892`, was named live and kept.

### 5.16 V15 and V16 — B-RECLAIM-OWN, verbatim from the session

Run from `/root/tz31-work` with this report's draft in `CryptoReports/`. The block ran as two commands: the `reclaim`
line, then the other six lines. **The first `I reclaim`'s output was piped through `grep -v` of its `R copied`/`R held`
lines by the Executor's error** (§6 item 8), so the session shows its other lines alone:

```text
$ I reclaim /root/tz31-work 2>&1 | grep -v '^\[.*\] R \(copied\|held\) '; echo "reclaim exit=${PIPESTATUS[0]}"
[2026-10-23T13:07:05Z] reclaim: 2903 report tokens; forensic store holds 1938 files
[2026-10-23T13:07:05Z] reclaim: /root/tz31-work/wt skipped: no file but its HEAD's, and HEAD 404288fb03ffd3619b2183f121d45688def8fba8 is its upstream's
[2026-10-23T13:07:06Z] RECLAIM PASS: 445 files considered, 58 named by a report, 1 kept by name, 59 copied, 0 already held; forensic store 1938 -> 1997 files
[2026-10-23T13:07:06Z] malloc tuned: True
[2026-10-23T13:07:06Z] peak memory of this run: 32878592 bytes
[2026-10-23T13:07:06Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
reclaim exit=0
```

`I reclaim /root/tz31-work` was then run again, unfiltered, before any removal, so that every file is named with its
hash and destination. Each of the 59 is `R held`, its copy in the store equal to its source:

```text
$ I reclaim /root/tz31-work; echo "exit=$?"
[2026-10-23T13:07:16Z] reclaim: 2903 report tokens; forensic store holds 1997 files
[2026-10-23T13:07:16Z] reclaim: /root/tz31-work/wt skipped: no file but its HEAD's, and HEAD 404288fb03ffd3619b2183f121d45688def8fba8 is its upstream's
[2026-10-23T13:07:16Z] R held   61996c7e18a8548a944ad4f2cfb8fe5d482bef5f289d7d0302831204c4988fb2 /root/btc-forensics/tz31-work--label-ledger.jsonl
[2026-10-23T13:07:16Z] R held   40b0c5a7809beb9c61a407d286634a1d20000b1835d1d189ee1285f8b9768487 /root/btc-forensics/tz31-work--state.json
[2026-10-23T13:07:16Z] R held   395e6d9c4997df8035f004735431718bf25ec90d4b8226a9ec75abc29ad371f6 /root/btc-forensics/tz31-work--logs--00-workdir.log
[2026-10-23T13:07:16Z] R held   1421e46cf1b4973a96fe508675e6b98cf9c71ecb43711f29556266c04b94b795 /root/btc-forensics/tz31-work--logs--01-stage.log
[2026-10-23T13:07:16Z] R held   1d05a1c237e5f9573e1ad2bac13e0f1d52f04b36db3afdd8ce1c15dd41c90792 /root/btc-forensics/tz31-work--logs--02-fingerprint-I0.log
[2026-10-23T13:07:16Z] R held   72790b5ddbfde689555054174a15e41401dc42edc418618bb38837658b1d85e3 /root/btc-forensics/tz31-work--logs--03-host-gate.log
[2026-10-23T13:07:16Z] R held   08c9fcb50ff12986cb990d12fcc3a43f172021ab3f5ecd45cf491379d9e4b1ad /root/btc-forensics/tz31-work--logs--04-refs.log
[2026-10-23T13:07:16Z] R held   24029f9a6cf23a9260675f216df740097fc68a5de482297ead0e853546c3b68c /root/btc-forensics/tz31-work--logs--05-branch.log
[2026-10-23T13:07:16Z] R held   6eddae9be458084bf2033267e0b74898547df8975a29c1ca6e276c51d5b87a1c /root/btc-forensics/tz31-work--logs--06-fingerprint-I.log
[2026-10-23T13:07:16Z] R held   607d3290a9c9ee5491bba17e7c0701dd11798de28f504d5f1295e8f156c6bf41 /root/btc-forensics/tz31-work--logs--07-commit-push.log
[2026-10-23T13:07:16Z] R held   b8acdc729f8cac2823aa0357a4283f9c8828028af8aad5ca252308bfe6159281 /root/btc-forensics/tz31-work--logs--08-pr.log
[2026-10-23T13:07:16Z] R held   a2dab5712435a536d7b31713c9f6330244c9b60056fcb9b99a207bea88ed3524 /root/btc-forensics/tz31-work--logs--09-selftest.log
[2026-10-23T13:07:16Z] R held   f2cb4ade0ff5bd3a10c98f6d0610a259a90ce562b6dde1b152135d66ab6c87f8 /root/btc-forensics/tz31-work--logs--10-still-1.log
[2026-10-23T13:07:16Z] R held   6b31ee2fa137cfa6d90e7426f8b00408cb77eca405ab1cd52c2f44e3f0656152 /root/btc-forensics/tz31-work--logs--11-scratch.log
[2026-10-23T13:07:16Z] R held   1f62ba5d2015efabdf04427c7571a48fe25b363b096e623ade9b5d80f1460809 /root/btc-forensics/tz31-work--logs--12-reclaim-scratch.log
[2026-10-23T13:07:16Z] R held   ea89436a640458f6e8ccbb9a3dc7fd972308104780e91a72af5c76afcf9e3bbc /root/btc-forensics/tz31-work--logs--13-rm-scratch.log
[2026-10-23T13:07:16Z] R held   2fa6989335b7257ff659c7f16f88aac797d057c86ec00548cc1efe119abee8d7 /root/btc-forensics/tz31-work--logs--14-archive-1.log
[2026-10-23T13:07:16Z] R held   bd50b299d8e9a1b84ece2afdd9b3a4f9ddcaefbd8cd867c0e845ae24ee7c481f /root/btc-forensics/tz31-work--logs--15-rehearse.log
[2026-10-23T13:07:16Z] R held   4d58bfc97eb2e059c13d96722efc6ae72976ac44c439abb7d55cf1f700f4b8bd /root/btc-forensics/tz31-work--logs--16-units-journal.log
[2026-10-23T13:07:16Z] R held   32be17cc86bb8a68ccebc8e0b67adca52f1f8ff1469e80a68447aa77e6778700 /root/btc-forensics/tz31-work--logs--17-instant.log
[2026-10-23T13:07:16Z] R held   131e1eed189078c8c8d7b5237ac996a860a04bae9cd46080c88eddc566c2e18f /root/btc-forensics/tz31-work--logs--18-fetch.log
[2026-10-23T13:07:16Z] R held   050ff5a4fc977a435b6934ea8d3e7fdd1b5ef8effc238abfe265097f4b5d2d3b /root/btc-forensics/tz31-work--logs--19-constants-1.log
[2026-10-23T13:07:16Z] R held   4066e8e29c91ac8fb3b701b190fec0a94d393efe4724d40beb46f0253749e403 /root/btc-forensics/tz31-work--logs--20-constants-2.log
[2026-10-23T13:07:16Z] R held   7bd4d49de5ef3ffb7a57f443c968a7d3c445ace1c5f225b177a76ba03a43406b /root/btc-forensics/tz31-work--logs--21-score-1.log
[2026-10-23T13:07:16Z] R held   5c6f98129f38186ed8c12ba3a961eedcc24445026668e02f10b912eb736a8c89 /root/btc-forensics/tz31-work--logs--22-score-2.log
[2026-10-23T13:07:16Z] R held   9616f7a08a9c8e3b446bef5ca89a090a0052aa5903d9e8702f63fc6fc7ca9168 /root/btc-forensics/tz31-work--logs--23-still-2.log
[2026-10-23T13:07:16Z] R held   a13fc5477c659cd58859bd01c5618eabbe07043187b5a2277b2100127e8bb64f /root/btc-forensics/tz31-work--logs--24-host-gate-2.log
[2026-10-23T13:07:16Z] R held   49d3ca30b0a9b5569fa5c68cc79da8ffc8eb48a6d592e81b5cb741b12855f310 /root/btc-forensics/tz31-work--logs--25-archive-2.log
[2026-10-23T13:07:16Z] R held   41f12368031f50282bf94d63405c3a3609bb2b3c7088667b49741727d1c88063 /root/btc-forensics/tz31-work--logs--26-closing.log
[2026-10-23T13:07:16Z] R held   ba2698366d6494660ebd50bcdc5680d0db15217e25cbad82747696fa3b1f1bf7 /root/btc-forensics/tz31-work--logs--27-separation.log
[2026-10-23T13:07:16Z] R held   2ad073078efbc5ef3e7c08a2ea580e52dc590ba8fa0039ebb752d84a092ce4ee /root/btc-forensics/tz31-work--logs--28-files-written.log
[2026-10-23T13:07:16Z] R held   3da68c766a697137cd4248ef31b1c16d03fa5cfcae7913de3db7147ed2a1caef /root/btc-forensics/tz31-work--rehearsal--rehearsal-constants.json
[2026-10-23T13:07:16Z] R held   4e738994ef75c9f1e243d26810285d2dc7e1a440ed6fcbc8c2a67b2311c3920c /root/btc-forensics/tz31-work--rehearsal--rehearsal-makers-fills.jsonl.gz
[2026-10-23T13:07:16Z] R held   0189b0d0484becc2ee0e94283f8be80b2e3a5701e171778068d2559a615f3d51 /root/btc-forensics/tz31-work--rehearsal--rehearsal-makers-members.csv
[2026-10-23T13:07:16Z] R held   c644fe98ef5461356ac99a0b012c585776e33b79db5366e5d516230c1a614ae2 /root/btc-forensics/tz31-work--rehearsal--rehearsal-makers-scored.csv
[2026-10-23T13:07:16Z] R held   8e334f4b2217955260ff57ddeee230541c6632939b4657b6dca08dfbd3efe3b3 /root/btc-forensics/tz31-work--rehearsal--rehearsal-makers-wallets.csv
[2026-10-23T13:07:16Z] R held   6436a601be7664e81087992e8e4502e9bc38e9df4d5e3f0691fd928de81d2644 /root/btc-forensics/tz31-work--rehearsal--rehearsal-pool.csv
[2026-10-23T13:07:16Z] R held   b500df7c8fc80148894fe3da329129c804b073fd385cfa904fabf3c4b1535673 /root/btc-forensics/tz31-work--rehearsal--rehearsal-reading.json
[2026-10-23T13:07:16Z] R held   49dd0d3748542e4c5976f4eea1e24aa06c2a6d3f6fa8034ab0bf3c4f2518b814 /root/btc-forensics/tz31-work--rehearsal--rehearsal-takers-fills.jsonl.gz
[2026-10-23T13:07:16Z] R held   af75e308edb7a0edb430bfee8f12944b2bd84b53a951c22b5a01f1e7c790ea48 /root/btc-forensics/tz31-work--rehearsal--rehearsal-takers-members.csv
[2026-10-23T13:07:16Z] R held   3d2945659bf530e301c7ea79eab6ea4da47421e9b2fc722930a2d4c40bc76021 /root/btc-forensics/tz31-work--rehearsal--rehearsal-takers-scored.csv
[2026-10-23T13:07:16Z] R held   f379916ab1c5e697fe14094c00f9dda071dc74e64bca49e88f031a1d88c2d63e /root/btc-forensics/tz31-work--rehearsal--rehearsal-takers-wallets.csv
[2026-10-23T13:07:16Z] R held   121d4baeb92cee5acb1fb4bd2eea04959368291877a642ec0b079fe877c135bf /root/btc-forensics/tz31-work--rehearsal--rehearsal-timing.jsonl
[2026-10-23T13:07:16Z] R held   138a70af9a7b4a86914a9ca3179dd1702b83485d658a322a70944d63bc7b8153 /root/btc-forensics/tz31-work--rehearsal--set.json
[2026-10-23T13:07:16Z] R held   34a1740fec9f933a03f14a44518c6d7ef7009296e81ac188d174d24d1ff7c61f /root/btc-forensics/tz31-work--set--fetch-timing.jsonl
[2026-10-23T13:07:16Z] R held   16fba05fe5b49a4e6ca1f0a31740fe2531419fa718d0a50e5a91524db2730f0f /root/btc-forensics/tz31-work--set--set.json
[2026-10-23T13:07:16Z] R held   983edb35895f23ca97feb66638b15b58b9ff9014092fb088d6318d2f5df8173c /root/btc-forensics/tz31-work--set--tz31-constants.json
[2026-10-23T13:07:16Z] R held   33b3f44b855330f3fea9834985925d238a0b63214831bc392bfae5762e4cd882 /root/btc-forensics/tz31-work--set--tz31-makers-fills.jsonl.gz
[2026-10-23T13:07:16Z] R held   93179e932d1d31eb2f34f27c18ca6523968c4bc3f44970cb4b980739e0d65f55 /root/btc-forensics/tz31-work--set--tz31-makers-members.csv
[2026-10-23T13:07:16Z] R held   4de2f3e8dcaf135f415c0726d6fb3710ba91516029e257382bef6f6a353f7eb7 /root/btc-forensics/tz31-work--set--tz31-makers-scored.csv
[2026-10-23T13:07:16Z] R held   46d794fddcee1463bb774f0b28cd97b377a7c6080ca821a14f7c66b3e910f3a4 /root/btc-forensics/tz31-work--set--tz31-makers-wallets.csv
[2026-10-23T13:07:16Z] R held   c92fc59e4126959ed0ff15eab5de43c9825e195ad0284f738ea9439014bbfef4 /root/btc-forensics/tz31-work--set--tz31-pool.csv
[2026-10-23T13:07:16Z] R held   d7dd8ee278c4f58bbf56ec9759ec3b2558cc49cc28725407d72d89c5471bd187 /root/btc-forensics/tz31-work--set--tz31-reading.json
[2026-10-23T13:07:16Z] R held   2d70895d19dc08e15e700fde70df8f4c026dc0d197d04d1d7aa6265f9391bdac /root/btc-forensics/tz31-work--set--tz31-takers-fills.jsonl.gz
[2026-10-23T13:07:16Z] R held   cca6c0fc376a7ea67eb0a3898c6f8c1053968cfea300a603c9c4b7019820874d /root/btc-forensics/tz31-work--set--tz31-takers-members.csv
[2026-10-23T13:07:16Z] R held   29b2b5e9ba8c3ac4ed9166c3492fe0de3db2b8a85588b66c4faca058c485b4c0 /root/btc-forensics/tz31-work--set--tz31-takers-scored.csv
[2026-10-23T13:07:16Z] R held   b359aa051e124147456dd31fae46cfd39ce21310f57c7f96d8ca4daeaafbfa86 /root/btc-forensics/tz31-work--set--tz31-takers-wallets.csv
[2026-10-23T13:07:17Z] R held   6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f /root/btc-forensics/tz31-work--stage--research--tz23-maker-m0.py
[2026-10-23T13:07:17Z] R held   7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765 /root/btc-forensics/tz31-work--stage--research--tz31-who-earns.py
[2026-10-23T13:07:17Z] RECLAIM PASS: 445 files considered, 58 named by a report, 1 kept by name, 0 copied, 59 already held; forensic store 1997 -> 1997 files
[2026-10-23T13:07:17Z] malloc tuned: True
[2026-10-23T13:07:17Z] peak memory of this run: 32882688 bytes
[2026-10-23T13:07:17Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

The other six lines, run as one command:

```text
$ git -C /root/btc-5m-twap worktree remove /root/tz31-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz31-work; echo "exit=$?"
exit=0
$ test -e /root/tz31-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       334cd7c [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
1997
$ df -B1 --output=source,size,avail /var/lib/btc-recorder; date -u +%FT%TZ
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11603329024
2026-10-23T13:07:22Z
```

**V15:** 445 files considered: the tree but the worktree, the chunk caches' 384 files among them. 58 were named by a
report and 1 kept by name, `logs/28-files-written.log`, whose hash no report printed. All 59 were copied at the first
run and held at the second. The store went `1,938 → 1,997`, after = before + 59 copied. The worktree was skipped:
`git status --porcelain --ignored` printed nothing, and its `HEAD` `404288f` is its upstream's. **V16:** `git worktree
remove` without `--force`, exit `0`. `rm -rf /root/tz31-work`, exit `0`, **not refused**, and `test -e` exit `1`. `git
worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else. Free space after:
`11,603,329,024` bytes at 13:07:22 UTC. The branch `tz-31-who-earns` stays on `origin` and as a local ref. **This
session's own directory, `917cd7ac-51fd-50da-a0d7-5b331470eff3`, and its sibling `19ca9482-c685-4646-b5db-a89314b67236`,
born with its process `2427892`, are the next TZ's to reclaim.**

---

## 6. What could not be implemented as written

1. **Contract §1's pull and the first reads ran before §0.0's `mkdir`**, as in every TZ since TZ-21. They were `git
   fetch` and `git merge --ff-only origin/main` (local `main` `5e384de` → `334cd7c`), reading the TZ, the map and the
   contract, and splitting the map into two parts in the session's scratchpad to read it whole. That copy is of a
   committed file and went with the scratchpad. **The `mkdir` itself printed `exit=0` to the session**, before
   `logs/` existed. `logs/00-workdir.log` records it after the fact, with its output as printed.
2. **The power at the set's own figures was `0.447`, against `0.962` projected.** The set's makers carried 4.28 times
   the projected `V` and 1.33 times the `Sh`. TZ-31 §1 named both quantities as the ones the projection rests on, and
   `constants` printed both, and the power, before any label (map §7 item 116's rule). This is not a departure, since
   §4.3 reads no power. It is recorded here because the reading was W-EARN with UNDECIDABLE possible.
3. **`eff3ddd1-cb45-4950-82cd-35b28b9c2c61` was reclaimed.** Map §3 called it live, made by `claude` pids `2113303`
   and `2113313`, and said "they are not a TZ's, and no TZ touches them". At §3.3 neither process was running.
   `I scratch` named the directory **earlier**: born 2026-10-21 09:37:21 UTC, empty, no file newer than its birth.
   TZ-31 §9's B-RECLAIM-SCRATCH removes every directory `I scratch` names earlier, so it was removed with TZ-30's
   pair. Before that, the Executor read `/proc/<pid>/cmdline`, `cwd` and `fd` of the three running `claude`
   processes, outside the instrument: none held a file under any of the three directories. The two older `claude`
   processes, started 2026-10-22 13:11:35/37 UTC, are `remote-control` bridges with working directories
   `/root/crypto-auto` and `/root/btc-5m-twap`. No directory beside this session's was born with them.
4. **One read no step names:** `logs/16-units-journal.log`, three `journalctl` reads of the capture units' and PID 1's
   records near 2026-10-21 to 2026-10-23, to say what moved the units' `NRestarts` to 0 (§2.9). `journalctl` is among
   §2 item 5's permitted reads, and nothing under a capture root was opened.
5. **`state.json`'s `constants_at` is the second `constants` run's instant**, 13:02:10 UTC. Both runs preceded the
   first label read, 13:02:18. This is the instrument's behaviour, as in TZ-29.
6. **The report was assembled by a script** from a hand-written template and the logs. The script substituted each
   quoted log verbatim, removed only `18-fetch.log`'s 14 progress lines where §2.3 says so, and asserted every
   substituted file present. The template and the script lived in `/root/tz31-work/report/`. No report names their
   hashes, so they went with the tree. **`logs/28-files-written.log` does not list itself**, because it is the file
   being written. Its hash is in B-RECLAIM-OWN's output.
7. **The capture units' restarts before this run** (§2.9) are not this TZ's and moved no gate. They are recorded
   because map §3 and §6 state a recorder pid that no longer runs, and because the package manager's restarts sit
   beside the archive's runs off its calendar (§2.5).

8. **B-RECLAIM-OWN's first `I reclaim` was piped through `grep -v` by the Executor**, which hid its per-file `R` lines
   from the session. That breaks TZ-31 §9's "every line of it" for that run. The run itself was unchanged: its
   counts, `RECLAIM PASS` and exit `0` are quoted above. Before any removal, `I reclaim /root/tz31-work` was run again
   unfiltered. Its output names all 59 files with their SHA-256 and destinations as `R held`, which proves each copy
   equal to its source. §5.16 quotes both runs verbatim.

Nothing else.

### 6.1 Every file the run wrote, by SHA-256 (§8) — `logs/28-files-written.log`, verbatim

The chunk caches are excepted, as §8 allows: the set's 336 files (`201,116,058` bytes) and the rehearsal's 48
(`28,030,242`).

```text
2026-10-23T13:03:11Z
61996c7e18a8548a944ad4f2cfb8fe5d482bef5f289d7d0302831204c4988fb2 360 ./label-ledger.jsonl
395e6d9c4997df8035f004735431718bf25ec90d4b8226a9ec75abc29ad371f6 211 ./logs/00-workdir.log
1421e46cf1b4973a96fe508675e6b98cf9c71ecb43711f29556266c04b94b795 253 ./logs/01-stage.log
1d05a1c237e5f9573e1ad2bac13e0f1d52f04b36db3afdd8ce1c15dd41c90792 8224 ./logs/02-fingerprint-I0.log
72790b5ddbfde689555054174a15e41401dc42edc418618bb38837658b1d85e3 13368 ./logs/03-host-gate.log
08c9fcb50ff12986cb990d12fcc3a43f172021ab3f5ecd45cf491379d9e4b1ad 4533 ./logs/04-refs.log
24029f9a6cf23a9260675f216df740097fc68a5de482297ead0e853546c3b68c 617 ./logs/05-branch.log
6eddae9be458084bf2033267e0b74898547df8975a29c1ca6e276c51d5b87a1c 8224 ./logs/06-fingerprint-I.log
607d3290a9c9ee5491bba17e7c0701dd11798de28f504d5f1295e8f156c6bf41 871 ./logs/07-commit-push.log
b8acdc729f8cac2823aa0357a4283f9c8828028af8aad5ca252308bfe6159281 63 ./logs/08-pr.log
a2dab5712435a536d7b31713c9f6330244c9b60056fcb9b99a207bea88ed3524 16790 ./logs/09-selftest.log
f2cb4ade0ff5bd3a10c98f6d0610a259a90ce562b6dde1b152135d66ab6c87f8 866 ./logs/10-still-1.log
6b31ee2fa137cfa6d90e7426f8b00408cb77eca405ab1cd52c2f44e3f0656152 897 ./logs/11-scratch.log
1f62ba5d2015efabdf04427c7571a48fe25b363b096e623ade9b5d80f1460809 458 ./logs/12-reclaim-scratch.log
ea89436a640458f6e8ccbb9a3dc7fd972308104780e91a72af5c76afcf9e3bbc 105 ./logs/13-rm-scratch.log
2fa6989335b7257ff659c7f16f88aac797d057c86ec00548cc1efe119abee8d7 68720 ./logs/14-archive-1.log
bd50b299d8e9a1b84ece2afdd9b3a4f9ddcaefbd8cd867c0e845ae24ee7c481f 12064 ./logs/15-rehearse.log
4d58bfc97eb2e059c13d96722efc6ae72976ac44c439abb7d55cf1f700f4b8bd 7183 ./logs/16-units-journal.log
32be17cc86bb8a68ccebc8e0b67adca52f1f8ff1469e80a68447aa77e6778700 186 ./logs/17-instant.log
131e1eed189078c8c8d7b5237ac996a860a04bae9cd46080c88eddc566c2e18f 1649 ./logs/18-fetch.log
050ff5a4fc977a435b6934ea8d3e7fdd1b5ef8effc238abfe265097f4b5d2d3b 2910 ./logs/19-constants-1.log
4066e8e29c91ac8fb3b701b190fec0a94d393efe4724d40beb46f0253749e403 4094 ./logs/20-constants-2.log
7bd4d49de5ef3ffb7a57f443c968a7d3c445ace1c5f225b177a76ba03a43406b 6690 ./logs/21-score-1.log
5c6f98129f38186ed8c12ba3a961eedcc24445026668e02f10b912eb736a8c89 7129 ./logs/22-score-2.log
9616f7a08a9c8e3b446bef5ca89a090a0052aa5903d9e8702f63fc6fc7ca9168 902 ./logs/23-still-2.log
a13fc5477c659cd58859bd01c5618eabbe07043187b5a2277b2100127e8bb64f 13190 ./logs/24-host-gate-2.log
49d3ca30b0a9b5569fa5c68cc79da8ffc8eb48a6d592e81b5cb741b12855f310 68720 ./logs/25-archive-2.log
41f12368031f50282bf94d63405c3a3609bb2b3c7088667b49741727d1c88063 1332 ./logs/26-closing.log
ba2698366d6494660ebd50bcdc5680d0db15217e25cbad82747696fa3b1f1bf7 560 ./logs/27-separation.log
3da68c766a697137cd4248ef31b1c16d03fa5cfcae7913de3db7147ed2a1caef 3349 ./rehearsal/rehearsal-constants.json
4e738994ef75c9f1e243d26810285d2dc7e1a440ed6fcbc8c2a67b2311c3920c 1366518 ./rehearsal/rehearsal-makers-fills.jsonl.gz
0189b0d0484becc2ee0e94283f8be80b2e3a5701e171778068d2559a615f3d51 64618 ./rehearsal/rehearsal-makers-members.csv
c644fe98ef5461356ac99a0b012c585776e33b79db5366e5d516230c1a614ae2 15947 ./rehearsal/rehearsal-makers-scored.csv
8e334f4b2217955260ff57ddeee230541c6632939b4657b6dca08dfbd3efe3b3 155810 ./rehearsal/rehearsal-makers-wallets.csv
6436a601be7664e81087992e8e4502e9bc38e9df4d5e3f0691fd928de81d2644 27688 ./rehearsal/rehearsal-pool.csv
b500df7c8fc80148894fe3da329129c804b073fd385cfa904fabf3c4b1535673 7595 ./rehearsal/rehearsal-reading.json
49dd0d3748542e4c5976f4eea1e24aa06c2a6d3f6fa8034ab0bf3c4f2518b814 437871 ./rehearsal/rehearsal-takers-fills.jsonl.gz
af75e308edb7a0edb430bfee8f12944b2bd84b53a951c22b5a01f1e7c790ea48 51779 ./rehearsal/rehearsal-takers-members.csv
3d2945659bf530e301c7ea79eab6ea4da47421e9b2fc722930a2d4c40bc76021 15084 ./rehearsal/rehearsal-takers-scored.csv
f379916ab1c5e697fe14094c00f9dda071dc74e64bca49e88f031a1d88c2d63e 100585 ./rehearsal/rehearsal-takers-wallets.csv
121d4baeb92cee5acb1fb4bd2eea04959368291877a642ec0b079fe877c135bf 10067 ./rehearsal/rehearsal-timing.jsonl
138a70af9a7b4a86914a9ca3179dd1702b83485d658a322a70944d63bc7b8153 82710 ./rehearsal/set.json
34a1740fec9f933a03f14a44518c6d7ef7009296e81ac188d174d24d1ff7c61f 70531 ./set/fetch-timing.jsonl
16fba05fe5b49a4e6ca1f0a31740fe2531419fa718d0a50e5a91524db2730f0f 578750 ./set/set.json
983edb35895f23ca97feb66638b15b58b9ff9014092fb088d6318d2f5df8173c 3351 ./set/tz31-constants.json
33b3f44b855330f3fea9834985925d238a0b63214831bc392bfae5762e4cd882 10357462 ./set/tz31-makers-fills.jsonl.gz
93179e932d1d31eb2f34f27c18ca6523968c4bc3f44970cb4b980739e0d65f55 452982 ./set/tz31-makers-members.csv
4de2f3e8dcaf135f415c0726d6fb3710ba91516029e257382bef6f6a353f7eb7 111791 ./set/tz31-makers-scored.csv
46d794fddcee1463bb774f0b28cd97b377a7c6080ca821a14f7c66b3e910f3a4 1088980 ./set/tz31-makers-wallets.csv
c92fc59e4126959ed0ff15eab5de43c9825e195ad0284f738ea9439014bbfef4 193194 ./set/tz31-pool.csv
d7dd8ee278c4f58bbf56ec9759ec3b2558cc49cc28725407d72d89c5471bd187 7771 ./set/tz31-reading.json
2d70895d19dc08e15e700fde70df8f4c026dc0d197d04d1d7aa6265f9391bdac 3279842 ./set/tz31-takers-fills.jsonl.gz
cca6c0fc376a7ea67eb0a3898c6f8c1053968cfea300a603c9c4b7019820874d 401776 ./set/tz31-takers-members.csv
29b2b5e9ba8c3ac4ed9166c3492fe0de3db2b8a85588b66c4faca058c485b4c0 108808 ./set/tz31-takers-scored.csv
b359aa051e124147456dd31fae46cfd39ce21310f57c7f96d8ca4daeaafbfa86 739227 ./set/tz31-takers-wallets.csv
6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f 54885 ./stage/research/tz23-maker-m0.py
7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765 84775 ./stage/research/tz31-who-earns.py
40b0c5a7809beb9c61a407d286634a1d20000b1835d1d189ee1285f8b9768487 424 ./state.json
chunk caches: set 336 files 201116058 bytes; rehearsal 48 files 28030242 bytes
  336 set/fetch-timing.jsonl
   48 rehearsal/rehearsal-timing.jsonl
  384 total
```

