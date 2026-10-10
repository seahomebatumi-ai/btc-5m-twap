# TZ-24 report — B2: does the nesting break on executable quotes?

**B2 READING: VIOLATION.** The set covers the 1,175 windows from `1790184600`, 2026-09-23 17:30 UTC, to `1791241200`,
2026-10-05 23:00 UTC. It holds **1,079 members**. The other 96 windows are 90 the chain book never stored
(`1791018000` … `1791098100`) and 6 whose `window.json` reads `incomplete`. All 7,553 checkpoint units of the members
read valid, so **`N_clean` = 1,079**. **7 members hold a firm violation (`V_firm` = 7)**, and 9 hold a firm or a loose
one (`V_any` = 9). Among the 7,553 rows, 7 are firm, 2 loose, 3,904 none and 3,640 unquoted. A firm row is a dominated
pair whose two executable asks cost less than 1 a share after both legs' taker fees. That holds with the fee collected
either way, and the two replies were received at most 150 ms apart, with the two books' own timestamps at most 150 ms
apart. Under §4.3, `V_firm >= 1` reads **VIOLATION**, whatever `N`. Under TZ §1 item 3, VIOLATION opens B3. **A violation
measured is not an edge captured** (CANON PART II): depth, the 150 ms delay, both legs filled together, and `D` known
live are the next step's.

**Every gate before the reading passed.** The self-test passed **122 of 122** · G-REHEARSAL **10 of 10** figures equal
to the Architect's · G-SET **1,175** windows considered, every one with a status, **1,079** members · the constants
**1 of 1** file `unchanged` at the second run · the score **2 of 2** files `unchanged`, **2** ledger lines · G-STILL
PASS: the recorder `4148534` / `NRestarts` 2, the chain book `4064090` / `NRestarts` 1, both `active`, unchanged.

**The books were read once a run, by `score`, at 08:31:25 and 08:31:36 UTC.** That was after the constants
`1b27e8a9…` were on disk with their SHA-256 in `state.json` (08:31:20 UTC), and after the instrument's commit `6f045cf`
was on `origin` (pushed 08:29:52–08:30:00 UTC). **No command was refused by the session's classifier.**
B-RECLAIM-SCRATCH's `reclaim` and two `rm -rf`, and B-RECLAIM-OWN's lines, ran as the Executor's own commands, so no
block was handed to the Boss.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-24-nesting-b2.md`, 2,165 lines, 126,844 bytes, SHA-256 `ce8d8824d8ec43dbe23112c3e1222eb73aeb4e9eb46c411730f900ecfec50b37`, landed at `6108e4f` |
| map revision | `2026-10-10-a`, equal; anchors 6 of 6; re-derived 4 of 4; rows hashed 33; `frozen` equal 30 of 30 |
| executor model | Opus, as the TZ names: `get_session` read `session_context.model` and `last_served_model` `claude-opus-5-5` |
| branch | `tz-24-nesting-b2` at `6f045cffc3601b589d3b8b7a6a9af6f73991e18b`, pushed; pull request #24, open, not merged |
| instrument | `research/tz24-nesting-b2.py`, 1,535 lines, 76,142 bytes, SHA-256 `4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b`, Appendix A byte for byte |
| interpreter | `/root/tz01-env/venv/bin/python` 3.12.3 with numpy 2.5.3, every mode under `nice -n 19` and `-B` |
| requests | `gamma-api.polymarket.com/markets`, through the instrument's `http_json` alone, with `User-Agent: btc-5m-twap-b2/TZ-24` and `Accept: application/json`: 20 requests by `rehearse`, 108 by `fetch`; `git` against `origin`; `gh` for the pull request |
| chain book | read only, by the instrument alone: `window.json` 1,085 opens by `fetch`, `books.jsonl.gz` 1,079 opens by each `score`, nothing else. The one other command that touched the root was §0.3's `test -d`, at both runs |
| recorder's capture | not read. The only commands that touched its root were §0.3's `df`, `find` and `grep -c`, at both runs, and B-RECLAIM-OWN's `df`. The self-test's three deliberate opens under the two roots were refused by the audit hook before they happened, which is what they test. Every mode printed `opens refused under the capture roots: 0` |
| units | `btc-recorder.service` and `btc-chainbook.service`, read with `systemctl show` and `is-active` alone, never signalled |
| pricer | not read, not called, not scored; `A6` `729f0bcdbee3` is stated so that what was not scored is not in doubt |

This report prints no single book's or market's price, size or time except what TZ §2 item 9 exempts: every firm and
every loose row the instrument printed, with the window's two strikes, and the closest row at each `tau'` and pair.
Those come verbatim from `score`'s own output. Every other figure is a count or a sum over a set, copied from the
instrument's own output. The settled documents and the units file, which holds every row, are in §9's byte-for-byte
copies in `/root/btc-forensics/`. The books stay where the chain book stored them.

---

## 0. Fingerprint

Contract §1 steps 3 and 4 ran inside the instrument as `I0 fingerprint` (§0.2), which asserts each step. It read the
map revision string `2026-10-10-a` and the six anchors of the TZ header, all equal. It re-derived `A2`, `A4`, `A5` and
`A6` as the first 12 hex characters of their files' SHA-256, 4 of 4 equal. It hashed the table's 33 rows: 30 `frozen`,
each equal to the map in lines, bytes and SHA-256; 2 `tracked`; and 1 `reported`.

| anchor | required | read |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` |
| `A2` — collector | `6c5089330629` | `6c5089330629`, re-derived from `research/twap-divergence.py` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | equal |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b`, re-derived from `BTC-EXECUTOR-INSTRUCTIONS.md` |
| `A5` — recorder | `0f6c90451cbd` | `0f6c90451cbd`, re-derived from `research/recorder/recorder.py` |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3`, re-derived from `research/pfair.py` |

### 0.1 The 33 rows of the map's §0 table (V1)

| path | lines | bytes | SHA-256 | state | against the map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 1,205 | 259,278 | `efca3a7ecb3f67f971817ec9d7c068405751afada68fafb678a60da91603725f` | reported | reported, no expectation |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | frozen | equal |
| `research/twap-divergence.py` | 1,135 | 50,928 | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | frozen | equal |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | frozen | equal |
| `research/tz02-distribution.py` | 334 | 14,511 | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | tracked | no expectation |
| `research/pfair.py` | 441 | 19,357 | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` | frozen | equal |
| `research/selftest-pfair.py` | 619 | 32,559 | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` | frozen | equal |
| `research/tz06-calibration.py` | 577 | 27,138 | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | frozen | equal |
| `research/tz07a-variance-time.py` | 623 | 28,414 | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` | frozen | equal |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | frozen | equal |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | frozen | equal |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | frozen | equal |
| `research/tz10b-sigma-or-link.py` | 1,224 | 61,018 | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | frozen | equal |
| `research/tz11a-student-link.py` | 1,231 | 64,732 | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` | frozen | equal |
| `research/tz12-sized-gate.py` | 1,157 | 61,637 | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` | frozen | equal |
| `research/tz13-sized-gate-test3.py` | 1,074 | 53,901 | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` | frozen | equal |
| `research/tz14-quote-inventory.py` | 2,124 | 109,972 | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` | frozen | equal |
| `research/tz15-phase2-gate.py` | 1,517 | 73,799 | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` | frozen | equal |
| `research/tz16a-phase2-decisive-gate.py` | 2,198 | 111,192 | `3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125` | frozen | equal |
| `research/tz17-settlement-chain.py` | 1,102 | 38,622 | `e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92` | frozen | equal |
| `research/tz18a-chainbook-capture.py` | 1,683 | 69,517 | `e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae` | frozen | equal |
| `research/tz20-capture-under-systemd.py` | 771 | 36,528 | `104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7` | frozen | equal |
| `research/tz21-recorder-memory.py` | 1,284 | 59,009 | `d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f` | frozen | equal |
| `research/tz23-maker-m0.py` | 1,184 | 54,885 | `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` | frozen | equal |
| `research/recorder/recorder.py` | 651 | 27,821 | `0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7` | frozen | equal |
| `research/recorder/config.py` | 112 | 4,773 | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | frozen | equal |
| `research/recorder/manifest.py` | 254 | 10,002 | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | frozen | equal |
| `research/recorder/analyze.py` | 813 | 34,705 | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | frozen | equal |
| `research/recorder/probe.py` | 227 | 9,324 | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | frozen | equal |
| `research/recorder/selftest.py` | 573 | 30,591 | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | frozen | equal |
| `deploy/systemd/btc-recorder.service` | 23 | 707 | `3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1` | frozen | equal |
| `deploy/systemd/btc-chainbook.service` | 22 | 724 | `a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2` | frozen | equal |
| `.gitignore` | 5 | 252 | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | tracked | no expectation |

`logs/02-fingerprint.log`, verbatim:

```
$ I0 fingerprint   # 2026-10-10T08:29:12Z
[2026-10-10T08:29:12Z] re-derived A2 research/twap-divergence.py sha256[:12] 6c5089330629 equal
[2026-10-10T08:29:12Z] re-derived A4 BTC-EXECUTOR-INSTRUCTIONS.md sha256[:12] 437b45ea196b equal
[2026-10-10T08:29:12Z] re-derived A5 research/recorder/recorder.py sha256[:12] 0f6c90451cbd equal
[2026-10-10T08:29:12Z] re-derived A6 research/pfair.py sha256[:12] 729f0bcdbee3 equal
[2026-10-10T08:29:12Z] SYSTEM-MAP.md                                  1205 lines   259278 bytes efca3a7ecb3f67f971817ec9d7c068405751afada68fafb678a60da91603725f reported
[2026-10-10T08:29:12Z] BTC-EXECUTOR-INSTRUCTIONS.md                    234 lines    11128 bytes 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b frozen equal
[2026-10-10T08:29:12Z] research/twap-divergence.py                    1135 lines    50928 bytes 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 frozen equal
[2026-10-10T08:29:12Z] research/selftest-twap-divergence.py            376 lines    16736 bytes ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a frozen equal
[2026-10-10T08:29:12Z] research/tz02-distribution.py                   334 lines    14511 bytes f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 tracked
[2026-10-10T08:29:12Z] research/pfair.py                               441 lines    19357 bytes 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 frozen equal
[2026-10-10T08:29:12Z] research/selftest-pfair.py                      619 lines    32559 bytes b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa frozen equal
[2026-10-10T08:29:12Z] research/tz06-calibration.py                    577 lines    27138 bytes 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f frozen equal
[2026-10-10T08:29:12Z] research/tz07a-variance-time.py                 623 lines    28414 bytes 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 frozen equal
[2026-10-10T08:29:12Z] research/tz07b-settlement-dispersion.py         515 lines    24926 bytes 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc frozen equal
[2026-10-10T08:29:12Z] research/tz08a-out-of-sample.py                 745 lines    38822 bytes 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c frozen equal
[2026-10-10T08:29:12Z] research/tz09-disk-inventory.py                 894 lines    41004 bytes b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 frozen equal
[2026-10-10T08:29:12Z] research/tz10b-sigma-or-link.py                1224 lines    61018 bytes 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 frozen equal
[2026-10-10T08:29:12Z] research/tz11a-student-link.py                 1231 lines    64732 bytes 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 frozen equal
[2026-10-10T08:29:12Z] research/tz12-sized-gate.py                    1157 lines    61637 bytes d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 frozen equal
[2026-10-10T08:29:12Z] research/tz13-sized-gate-test3.py              1074 lines    53901 bytes a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd frozen equal
[2026-10-10T08:29:12Z] research/tz14-quote-inventory.py               2124 lines   109972 bytes 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 frozen equal
[2026-10-10T08:29:12Z] research/tz15-phase2-gate.py                   1517 lines    73799 bytes 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 frozen equal
[2026-10-10T08:29:12Z] research/tz16a-phase2-decisive-gate.py         2198 lines   111192 bytes 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 frozen equal
[2026-10-10T08:29:12Z] research/tz17-settlement-chain.py              1102 lines    38622 bytes e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 frozen equal
[2026-10-10T08:29:12Z] research/tz18a-chainbook-capture.py            1683 lines    69517 bytes e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae frozen equal
[2026-10-10T08:29:12Z] research/tz20-capture-under-systemd.py          771 lines    36528 bytes 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7 frozen equal
[2026-10-10T08:29:12Z] research/tz21-recorder-memory.py               1284 lines    59009 bytes d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f frozen equal
[2026-10-10T08:29:12Z] research/tz23-maker-m0.py                      1184 lines    54885 bytes 6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f frozen equal
[2026-10-10T08:29:12Z] research/recorder/recorder.py                   651 lines    27821 bytes 0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7 frozen equal
[2026-10-10T08:29:12Z] research/recorder/config.py                     112 lines     4773 bytes 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d frozen equal
[2026-10-10T08:29:12Z] research/recorder/manifest.py                   254 lines    10002 bytes 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 frozen equal
[2026-10-10T08:29:12Z] research/recorder/analyze.py                    813 lines    34705 bytes eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d frozen equal
[2026-10-10T08:29:12Z] research/recorder/probe.py                      227 lines     9324 bytes 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 frozen equal
[2026-10-10T08:29:12Z] research/recorder/selftest.py                   573 lines    30591 bytes c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 frozen equal
[2026-10-10T08:29:12Z] deploy/systemd/btc-recorder.service              23 lines      707 bytes 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1 frozen equal
[2026-10-10T08:29:12Z] deploy/systemd/btc-chainbook.service             22 lines      724 bytes a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2 frozen equal
[2026-10-10T08:29:12Z] .gitignore                                        5 lines      252 bytes 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b tracked
[2026-10-10T08:29:12Z] FINGERPRINT PASS: revision 2026-10-10-a; anchors 6 of 6, 4 re-derived; rows 33: frozen 30 of 30 equal, tracked 2, reported 1
[2026-10-10T08:29:12Z] malloc tuned: True
[2026-10-10T08:29:12Z] peak memory of this run: 27553792 bytes
[2026-10-10T08:29:12Z] opens refused under the capture roots: 0; chain book opens: window.json 0, books.jsonl.gz 0; tz14's record of opens under the recorder's root: not loaded
exit=0
```

### 0.2 §0.1 — the instrument, staged

`logs/01-stage.log`, verbatim. The script's two asserts held, and the independent `wc` and `sha256sum` agree:

```
/root/tz24-work/stage/research/tz24-nesting-b2.py 1535 76142 4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b
exit=0
$ wc -l -c stage/research/tz24-nesting-b2.py; sha256sum stage/research/tz24-nesting-b2.py
 1535 76142 stage/research/tz24-nesting-b2.py
4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b  stage/research/tz24-nesting-b2.py
```

### 0.3 Host gate — the opening reads, verbatim (V2)

`logs/03-host-gate.log`, run from `/root/btc-5m-twap` with
`S=/tmp/claude-0/-root-btc-5m-twap/5c15abf7-532c-5a8a-9dfa-19c904ad993e/scratchpad`, the scratchpad directory the
session's system prompt names:

```
Sat Oct 10 08:29:19 AM UTC 2026
1791620959
1
MemTotal:         978640 kB
MemAvailable:     255312 kB
SwapTotal:       3174396 kB
SwapFree:        2837548 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13007122432
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
1
chainbook exit=0
active
active
exit=0
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
/root/tz23-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
1561
3.12.3 2.5.3
/root/btc-5m-twap       6108e4f [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
193677986	/root/.claude
525289080	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/5c15abf7-532c-5a8a-9dfa-19c904ad993e/scratchpad
total 24
drwx------  6 root root 4096 Oct 10 08:27 .
drwx------ 16 root root 4096 Oct 10 08:27 ..
drwx------  4 root root 4096 Oct 10 08:27 5c15abf7-532c-5a8a-9dfa-19c904ad993e
drwx------  4 root root 4096 Oct  9 18:39 5ce9f787-ea2c-5497-8888-63b97cb927e8
drwx------  3 root root 4096 Oct 10 08:27 65948b60-83f3-4efd-93cf-43514331137a
drwx------  3 root root 4096 Oct  9 18:39 750b3996-3a2d-49fb-823d-1321cd631528
```

| gate | condition | read | result |
|---|---|---|---|
| **H1** | `find` prints exactly one path | one path, `/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json` | PASS |
| **H2** | `df` source `/dev/vda2`, size `31612203008`; `grep -c` at least `1` | `/dev/vda2`, `31612203008`; `1` | PASS |
| **H3** | `3.12.` and a numpy version | `3.12.3 2.5.3` | PASS |
| **H4** | `chainbook exit=0` | `chainbook exit=0` | PASS |
| memory | `MemAvailable` at least `141,189,120` bytes | `255312 kB` = `261,439,488` bytes | PASS |
| disk | `avail` at least `2,400,000,000` bytes | `13,007,122,432` | PASS |

The six were read by the Executor from the verbatim output above: the block is shell reads, and no code asserts them.
**Printed, no threshold:** both units `active` (`exit=0`); `telemetry-watch.service` `disabled` (`exit=1`) and
`inactive` (`exit=3`), so map §6's headroom condition holds; the recorder's tree at
`e3975b5da44c5328adf3bf3914634cd878842c73`, as map §6 records; `/root/tz23-work` absent (`exit=1`), as map §3 records,
and `/root/tz18a-svc` and `/root/btc-recorder-svc` present; the forensic store at **1,561** files, map §3's figure;
two worktrees, the primary checkout and `/root/btc-recorder-svc`; `du` `/root/.claude` `193,677,986` and
`/root/PROJECT_GAMING_PS5` `525,289,080` bytes; and beside this session's own directory `5c15abf7…`, three UUID
directories, which §2.3's `I scratch` names.

### 0.4 Free space and `MemAvailable` — every read, its instant and its bound

| instant (UTC) | read by | `MemAvailable`, bytes | bound | `/dev/vda2` avail, bytes | bound |
|---|---|---|---|---|---|
| 08:29:19 | §0.3 host gate | `261,439,488` (`255312 kB`) | `141,189,120` | `13,007,122,432` | `2,400,000,000` |
| 08:30:56 | `rehearse`'s `floor_check` | `299,229,184` | `141,189,120` | — | — |
| 08:31:02 | `fetch`'s `floor_check` | `293,261,312` | `141,189,120` | — | — |
| 08:31:20 | `constants` run 1 | `300,302,336` | `141,189,120` | — | — |
| 08:31:20 | `constants` run 2 | `297,205,760` | `141,189,120` | — | — |
| 08:31:25 | `score` run 1 | `295,440,384` | `141,189,120` | — | — |
| 08:31:36 | `score` run 2 | `285,106,176` | `141,189,120` | — | — |
| 08:32:01 | §3.9's §0.3 block | `289,312,768` (`282532 kB`) | `141,189,120` | `12,997,709,824` | `2,400,000,000` |
| 08:32:01 | §3.9's `free -b`, available | `298,385,408` | — | — | — |
| 08:39:36 | B-RECLAIM-OWN's `df`, and an added `MemAvailable` read | `295,284,736` (`288364 kB`) | — | `13,002,625,024` | — |

The lowest `MemAvailable` read is `261,439,488`, `1.85` times the floor. The lowest free space is
`12,997,709,824` before B-RECLAIM-OWN. Across the session, from 08:29:19 to 08:32:01, free space fell `9,412,608`
bytes, while `/root/tz24-work` held `8,485,133` bytes at 08:32:01. `/root/.claude` grew `238,884` bytes and
`/root/PROJECT_GAMING_PS5` `138,388`.

### 0.5 Refs (§0.5)

`logs/05-refs.log`, verbatim. `git ls-remote origin` ran before §3.1's push and printed **28** ref lines. `main`
is at `6108e4f`, not map §1's `d4857c3`: the upload that carries revision `2026-10-10-a` and this TZ is the two
commits above it on `main`'s first-parent line. They are `51c97ad` (`M SYSTEM-MAP.md`) and `6108e4f`
(`A CryptoTZ/TZ-24-nesting-b2.md`). `tz-23-maker-m0` is at `7f5ae3f`, as map §1 records. `main` carries revision
`2026-10-10-a`, and `refs/heads/tz-24-nesting-b2` did not exist on `origin` or locally, so neither BLOCK condition holds.
The difference in `main`'s head is recorded, not BLOCKING.

```
$ git ls-remote origin   # 2026-10-10T08:29:28Z
6108e4f743f9fdca3e10fbe594c1268e12ebdfb2	HEAD
6108e4f743f9fdca3e10fbe594c1268e12ebdfb2	refs/heads/main
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8	refs/heads/tz-23-maker-m0
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
ee2f6327390ef4d0c6169d1fba1a2ed4ae936dc3	refs/pull/3/head
0e13a5c76dfa2469ff25b3b0dd282872decf6f25	refs/pull/4/head
4216c04673ced76b5b2ac60ef57c9abedc46f9b9	refs/pull/5/head
5ed667afd1b53f036b9f938fcce13c0d709cd77f	refs/pull/6/head
c44af687203d14d5d485d4297c04cfb827096af9	refs/pull/7/head
26bbb61aed774a88355dd5204d8b69fda9135a68	refs/pull/8/head
e2625ea2b5473c311d59a48f32540ce39d58e591	refs/pull/9/head
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
exit=0
ref lines: 28

$ git log --first-parent --format="%H %cI %s" --name-status d4857c3..origin/main
6108e4f743f9fdca3e10fbe594c1268e12ebdfb2 2026-10-10T12:18:31+04:00 Add files via upload

A	CryptoTZ/TZ-24-nesting-b2.md
51c97ad86e63de8d2d13b034e56e72c1b04b4a70 2026-10-10T12:17:50+04:00 Update SYSTEM-MAP.md

M	SYSTEM-MAP.md

$ grep -c revision string / rev-parse checks
18:**Revision string:** `2026-10-10-a`
tz-24 branch lines: 0
local branch exit=1
```

---

## 1. Input

| input | read by | count | identity |
|---|---|---|---|
| `SYSTEM-MAP.md` | the Executor, in full; `I0 fingerprint` | 1,205 lines, 259,278 bytes | SHA-256 `efca3a7ecb3f67f971817ec9d7c068405751afada68fafb678a60da91603725f`, revision `2026-10-10-a`, landed at `51c97ad` |
| `CryptoTZ/TZ-24-nesting-b2.md` | the Executor, in full; §0.1's script, twice | 2,165 lines, 126,844 bytes | SHA-256 `ce8d8824d8ec43dbe23112c3e1222eb73aeb4e9eb46c411730f900ecfec50b37`, landed at `6108e4f` |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | the Executor, in full | 234 lines, 11,128 bytes | `A4`, `frozen`, equal |
| the 33 files of map §0 | `I0 fingerprint` | §0.1 above | 30 `frozen` equal |
| `research/tz14-quote-inventory.py` | loaded by the instrument's `tz14()`, for `book_of`, `touch_of` and `fee_pp` | 2,124 lines, 109,972 bytes | `978ee4ff…`, `frozen`, equal |
| `CryptoReports/*.md` | `reclaim`'s `report_tokens` | 1,786 tokens at B-RECLAIM-SCRATCH | — |
| the venue's settled documents, rehearsal | `rehearse`, `/markets?slug=…&closed=true` | 20 requests, 400 documents, 200 windows | stored gzip as served, `rehearsal/docs/`, 20 files, 188,098 bytes |
| the venue's settled documents, the set | `fetch`, the same route | 108 requests, the 2,158 documents of the 1,079 windows whose `window.json` qualified | stored gzip as served, `set/docs/`, 108 files, 1,027,354 bytes |
| the chain book's `window.json` | `fetch` | 1,085 opens: the 1,175 considered less the 90 without a directory | read only |
| the chain book's `books.jsonl.gz` | `score`, each of two runs | 1,079 opens a run, one a member; at each of the 7 checkpoints of every member exactly 4 lines, every one valid | read only |

**What was collected.** The settled documents of the 1,079 qualifying windows and the 200 rehearsal windows were
fetched from the venue for this TZ. The rehearsal's 200 windows are TZ-17's, whose documents TZ-17 also fetched.
Nothing of the chain book was re-collected: its books were read as stored. No CLOB request was made.

---

## 2. Measurements

### 2.1 §3.1 — the branch and its file (V3)

`logs/31-branch.log`, verbatim. The second extraction printed the same 1,535 lines, 76,142 bytes and SHA-256 as §0.1.
The file was committed alone as `6f045cf` and pushed, and pull request #24 was opened against `main`. The branch's diff
against `origin/main` names exactly one path, `A research/tz24-nesting-b2.py`, `1535` insertions and `0` deletions.

```
$ git -C /root/btc-5m-twap fetch origin   # 2026-10-10T08:29:44Z
exit=0
$ git -C /root/btc-5m-twap worktree add -b tz-24-nesting-b2 /root/tz24-work/wt origin/main
Preparing worktree (new branch 'tz-24-nesting-b2')
branch 'tz-24-nesting-b2' set up to track 'origin/main'.
HEAD is now at 6108e4f Add files via upload
exit=0
$ §0.1 script, argument /root/tz24-work/wt
/root/tz24-work/wt/research/tz24-nesting-b2.py 1535 76142 4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b
exit=0
$ git -C wt status --porcelain; wc; sha256sum
?? research/tz24-nesting-b2.py
 1535 76142 wt/research/tz24-nesting-b2.py
4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b  wt/research/tz24-nesting-b2.py
$ git -C wt add research/tz24-nesting-b2.py; git -C wt commit   # 2026-10-10T08:29:52Z
exit=0
6f045cffc3601b589d3b8b7a6a9af6f73991e18b 2026-10-10T08:29:52+00:00 TZ-24: B2, does the nesting break on executable quotes - research/tz24-nesting-b2.py
 research/tz24-nesting-b2.py | 1535 +++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 1535 insertions(+)
$ git -C wt push -u origin tz-24-nesting-b2
remote: 
remote: Create a pull request for 'tz-24-nesting-b2' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-24-nesting-b2        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-24-nesting-b2 -> tz-24-nesting-b2
branch 'tz-24-nesting-b2' set up to track 'origin/tz-24-nesting-b2'.
exit=0
$ git -C wt diff --stat --name-status origin/main origin/tz-24-nesting-b2
A	research/tz24-nesting-b2.py
1535	0	research/tz24-nesting-b2.py
6f045cffc3601b589d3b8b7a6a9af6f73991e18b
6f045cffc3601b589d3b8b7a6a9af6f73991e18b
$ gh pr create --base main --head tz-24-nesting-b2   # 2026-10-10T08:30:00Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/24
exit=0
```

### 2.2 §3.2 — the self-test (V4)

`I selftest` printed **`122 of 122 checks passed`**, exit 0 (`logs/32-selftest.log`, verbatim). Its synthetic chain
book read V_firm 1 and V_any 4, VIOLATION; 49 rows, one invalid unit by its hash; the classes firm 1, loose 3, none
43, unquoted 1; and the negative control moved the score when one book moved. Its three deliberate opens, of
`/var/lib/btc-recorder/runtime.jsonl`, `/var/lib/btc-chainbook/runtime.jsonl` and
`/var/lib/btc-chainbook/1790184600/books.jsonl.gz`, were refused by the hook before any open. The run was wrapped in
`/usr/bin/time -v` (§6 item 3), whose output is `logs/32-selftest.time`.

```
$ I selftest   # 2026-10-10T08:30:10Z
[2026-10-10T08:30:11Z]   ok  glibc took the 128 KiB mmap threshold and the two arenas
[2026-10-10T08:30:11Z]   ok  Decimal arithmetic at 60 digits in the thread that does every sum
[2026-10-10T08:30:11Z]   ok  tz14.fee_pp at CANON section 1.1's three points
[2026-10-10T08:30:11Z]   ok  loading tz14 leaves the precision at 60 digits
[2026-10-10T08:30:11Z]   ok  0.95 + 0.04 after both fees on top: 0.996013, firm
[2026-10-10T08:30:11Z]   ok  0.95 + 0.04 with the fee in shares: 1157525/1161919
[2026-10-10T08:30:11Z]   ok  0.480 + 0.485: 0.99995625 on top, below 1; in shares above 1: loose, convention
[2026-10-10T08:30:11Z]   ok  0.480 + 0.485 with the fee in shares: 1.0012701345...
[2026-10-10T08:30:11Z]   ok  0.97 + 0.02 received 400 ms apart: loose, apart
[2026-10-10T08:30:11Z]   ok  received 150 ms apart, books 150 ms apart: firm
[2026-10-10T08:30:11Z]   ok  received 150 ms and 1 ns apart: loose
[2026-10-10T08:30:11Z]   ok  books 151 ms apart by their own clocks: loose
[2026-10-10T08:30:11Z]   ok  a leg without a receive time is not firm
[2026-10-10T08:30:11Z]   ok  a book without its own time is not firm
[2026-10-10T08:30:11Z]   ok  a one-tick inversion at the 0.001 tick: 0.99948825, firm
[2026-10-10T08:30:11Z]   ok  0.50 + 0.50 costs 1.035: none
[2026-10-10T08:30:11Z]   ok  a leg without an ask is unquoted
[2026-10-10T08:30:11Z]   ok  the fee in shares costs at least the fee on top, at 0.001
[2026-10-10T08:30:11Z]   ok  the fee in shares costs at least the fee on top, at 0.01
[2026-10-10T08:30:11Z]   ok  the fee in shares costs at least the fee on top, at 0.3333
[2026-10-10T08:30:11Z]   ok  the fee in shares costs at least the fee on top, at 0.5
[2026-10-10T08:30:11Z]   ok  the fee in shares costs at least the fee on top, at 0.99
[2026-10-10T08:30:11Z]   ok  the fee in shares costs at least the fee on top, at 0.999
[2026-10-10T08:30:11Z]   ok  the pairs by the sign of D
[2026-10-10T08:30:11Z]   ok  A buys 15m Up and 5m Down; B buys 5m Up and 15m Down
[2026-10-10T08:30:11Z]   ok  pair A pays at least 1: R0 78000.5, R600 78010.25, R900 77980
[2026-10-10T08:30:11Z]   ok  pair A pays at least 1: R0 78000.5, R600 78010.25, R900 77990.75
[2026-10-10T08:30:11Z]   ok  pair A pays at least 1: R0 78000.5, R600 78010.25, R900 77995
[2026-10-10T08:30:11Z]   ok  pair A pays at least 1: R0 78000.5, R600 78010.25, R900 78000.5
[2026-10-10T08:30:11Z]   ok  pair A pays at least 1: R0 78000.5, R600 78010.25, R900 78005
[2026-10-10T08:30:11Z]   ok  pair A pays at least 1: R0 78000.5, R600 78010.25, R900 78010.25
[2026-10-10T08:30:11Z]   ok  pair A pays at least 1: R0 78000.5, R600 78010.25, R900 78020
[2026-10-10T08:30:11Z]   ok  pair B pays at least 1: R0 78000.5, R600 77990.75, R900 77980
[2026-10-10T08:30:11Z]   ok  pair B pays at least 1: R0 78000.5, R600 77990.75, R900 77990.75
[2026-10-10T08:30:11Z]   ok  pair B pays at least 1: R0 78000.5, R600 77990.75, R900 77995
[2026-10-10T08:30:11Z]   ok  pair B pays at least 1: R0 78000.5, R600 77990.75, R900 78000.5
[2026-10-10T08:30:11Z]   ok  pair B pays at least 1: R0 78000.5, R600 77990.75, R900 78005
[2026-10-10T08:30:11Z]   ok  pair B pays at least 1: R0 78000.5, R600 77990.75, R900 78010.25
[2026-10-10T08:30:11Z]   ok  pair B pays at least 1: R0 78000.5, R600 77990.75, R900 78020
[2026-10-10T08:30:11Z]   ok  pair A pays at least 1: R0 78000.5, R600 78000.5, R900 77980
[2026-10-10T08:30:11Z]   ok  pair B pays at least 1: R0 78000.5, R600 78000.5, R900 77980
[2026-10-10T08:30:11Z]   ok  pair A pays at least 1: R0 78000.5, R600 78000.5, R900 77990.75
[2026-10-10T08:30:11Z]   ok  pair B pays at least 1: R0 78000.5, R600 78000.5, R900 77990.75
[2026-10-10T08:30:11Z]   ok  pair A pays at least 1: R0 78000.5, R600 78000.5, R900 77995
[2026-10-10T08:30:11Z]   ok  pair B pays at least 1: R0 78000.5, R600 78000.5, R900 77995
[2026-10-10T08:30:11Z]   ok  pair A pays at least 1: R0 78000.5, R600 78000.5, R900 78000.5
[2026-10-10T08:30:11Z]   ok  pair B pays at least 1: R0 78000.5, R600 78000.5, R900 78000.5
[2026-10-10T08:30:11Z]   ok  pair A pays at least 1: R0 78000.5, R600 78000.5, R900 78005
[2026-10-10T08:30:11Z]   ok  pair B pays at least 1: R0 78000.5, R600 78000.5, R900 78005
[2026-10-10T08:30:11Z]   ok  pair A pays at least 1: R0 78000.5, R600 78000.5, R900 78010.25
[2026-10-10T08:30:11Z]   ok  pair B pays at least 1: R0 78000.5, R600 78000.5, R900 78010.25
[2026-10-10T08:30:11Z]   ok  pair A pays at least 1: R0 78000.5, R600 78000.5, R900 78020
[2026-10-10T08:30:11Z]   ok  pair B pays at least 1: R0 78000.5, R600 78000.5, R900 78020
[2026-10-10T08:30:11Z]   ok  between the strikes pair A pays 2
[2026-10-10T08:30:11Z]   ok  pair A is not dominated where D < 0
[2026-10-10T08:30:11Z]   ok  N_MIN = 528 is the fewest members with theta1 <= 1%
[2026-10-10T08:30:11Z]   ok  theta1(528) = 0.009984512446...
[2026-10-10T08:30:11Z]   ok  (1 - theta1(528))^528 = alpha
[2026-10-10T08:30:11Z]   ok  (1 - theta1(1000))^1000 = alpha
[2026-10-10T08:30:11Z]   ok  (1 - theta1(1084))^1084 = alpha
[2026-10-10T08:30:11Z]   ok  (1 - theta1(1175))^1175 = alpha
[2026-10-10T08:30:11Z]   ok  power(1000, 0.01) = 1 - 0.99^1000
[2026-10-10T08:30:11Z]   ok  the reading table, by clean members, firm windows and any windows
[2026-10-10T08:30:11Z]   ok  1,175 windows of seven checkpoints
[2026-10-10T08:30:11Z]   ok  the span: 2026-09-23 17:30 to the window whose five-minute market opens 2026-10-05 23:10
[2026-10-10T08:30:11Z]   ok  window.json read: allowed
[2026-10-10T08:30:11Z]   ok  books in score: allowed
[2026-10-10T08:30:11Z]   ok  books before score: refused
[2026-10-10T08:30:11Z]   ok  a window after the span: refused
[2026-10-10T08:30:11Z]   ok  a window before the span: refused
[2026-10-10T08:30:11Z]   ok  off the grid: refused
[2026-10-10T08:30:11Z]   ok  a write mode: refused
[2026-10-10T08:30:11Z]   ok  os.open RDWR: refused
[2026-10-10T08:30:11Z]   ok  os.open RDONLY: allowed
[2026-10-10T08:30:11Z]   ok  runtime.jsonl: refused
[2026-10-10T08:30:11Z]   ok  documents.jsonl: refused
[2026-10-10T08:30:11Z]   ok  the hook refuses /var/lib/btc-recorder/runtime.jsonl before it is opened
[2026-10-10T08:30:11Z]   ok  the hook refuses /var/lib/btc-chainbook/runtime.jsonl before it is opened
[2026-10-10T08:30:11Z]   ok  the hook refuses /var/lib/btc-chainbook/1790184600/books.jsonl.gz before it is opened
[2026-10-10T08:30:11Z]   ok  a complete window.json yields the chain book's token map
[2026-10-10T08:30:11Z]   ok  checkpoints_complete=6 reads incomplete
[2026-10-10T08:30:11Z]   ok  missed=1 reads incomplete
[2026-10-10T08:30:11Z]   ok  documents_ok=False reads documents
[2026-10-10T08:30:11Z]   ok  T=1790185500 reads window T
[2026-10-10T08:30:11Z]   ok  two settled documents that conform
[2026-10-10T08:30:11Z]   ok  E1, E2 and E3 hold
[2026-10-10T08:30:11Z]   ok  a document of another window reads start
[2026-10-10T08:30:11Z]   ok  an open document
[2026-10-10T08:30:11Z]   ok  unresolved
[2026-10-10T08:30:11Z]   ok  another rebate rate reads fee
[2026-10-10T08:30:11Z]   ok  tokens swapped against the chain book's read so
[2026-10-10T08:30:11Z]   ok  a document without finalPrice reads readings
[2026-10-10T08:30:11Z]   ok  no document reads absent
[2026-10-10T08:30:11Z]   ok  E2 at equality: Up
[2026-10-10T08:30:11Z]   ok  E1 compares literals: 78020.250 is not 78020.25
[2026-10-10T08:30:11Z]   ok  E2 fails on the wrong outcome
[2026-10-10T08:30:11Z]   ok  a stored line as the chain book writes it reads valid
[2026-10-10T08:30:11Z]   ok  a body that is not UTF-8 text reads raw
[2026-10-10T08:30:11Z]   ok  a body that does not parse reads body
[2026-10-10T08:30:11Z]   ok  a token that is not text reads token
[2026-10-10T08:30:11Z]   ok  a label against the map reads token
[2026-10-10T08:30:11Z]   ok  a refused read reads status
[2026-10-10T08:30:11Z]   ok  a line without the chain book's keys reads keys
[2026-10-10T08:30:11Z]   ok  a book time is a run of ASCII digits or nothing
[2026-10-10T08:30:11Z] the set formed in 0.0 s: 10 considered, 6 members, 1 document requests, /root/tz24-work/selftest-tmp/set/set.json sha256 b358d2e85d0707b7eb9024d357895065660ee5a3884e32807e3bd0ac9280da68
[2026-10-10T08:30:11Z]   ok  ten windows: six members, and four non-members with their reasons
[2026-10-10T08:30:11Z]   ok  eight windows' documents in one request of sixteen slugs
[2026-10-10T08:30:11Z]   ok  constants: six members, pairs A 3, B 2, AB 1; NONE impossible below 528
[2026-10-10T08:30:11Z] books: 6 members, 42 units, 49 rows, invalid {'hash': 1}
[2026-10-10T08:30:11Z] rows by class: {'firm': 1, 'loose': 3, 'none': 43, 'unquoted': 1}; loose by reason: {'convention': 1, 'apart': 2, 'no time': 0}
[2026-10-10T08:30:11Z] tau' 245: {'firm': 0, 'loose': 0, 'none': 6, 'unquoted': 1}
[2026-10-10T08:30:11Z] tau' 185: {'firm': 0, 'loose': 0, 'none': 7, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau' 125: {'firm': 0, 'loose': 0, 'none': 6, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau'  95: {'firm': 0, 'loose': 1, 'none': 6, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau'  65: {'firm': 0, 'loose': 1, 'none': 6, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau'  35: {'firm': 1, 'loose': 0, 'none': 6, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau'  15: {'firm': 0, 'loose': 1, 'none': 6, 'unquoted': 0}
[2026-10-10T08:30:11Z] by pair: {'A': {'firm': 1, 'loose': 2, 'none': 23, 'unquoted': 1}, 'B': {'firm': 0, 'loose': 1, 'none': 20, 'unquoted': 0}}
[2026-10-10T08:30:11Z] windows with a firm violation V_firm 1 of 6; with any V_any 4 of 6; clean members 5
[2026-10-10T08:30:11Z] NONE possible: False; its alternative at the clean members, theta1 = 0.653427578422426803558874074240464311659953174971785519254457 a window
[2026-10-10T08:30:11Z] ROW columns: class,reason,T,tau',pair,ask_x,ask_y,k_top,k_shares,skew_ns,ts_x,ts_y,dt_ms,q_x,q_y,R0,R600
[2026-10-10T08:30:11Z] ROW firm,,1790184600,35,A,0.95,0.04,0.996013,0.996218325029541646190483157603929361685280987745273121448225,0,1790185465020,1790185465020,0,50,20,78000.5,78010.25
[2026-10-10T08:30:11Z] ROW loose,convention,1790186400,65,A,0.480,0.485,0.99995625,1.00127013455235589192119365130384999402817782813903228834089,0,1790187235020,1790187235020,0,9,9,78000.5,78010.25
[2026-10-10T08:30:11Z] ROW loose,apart,1790187300,15,B,0.97,0.02,0.993409,0.993514338022667012364358969597374155040594912188690516780536,400000000,1790188185020,1790188185020,0,7,8,78000.5,77990.75
[2026-10-10T08:30:11Z] ROW loose,apart,1790189100,95,A,0.95,0.04,0.996013,0.996218325029541646190483157603929361685280987745273121448225,0,1790189905020,1790189905320,300,50,20,78000.5,78000.5
[2026-10-10T08:30:11Z] closest tau' 245 A: T 1790184600 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 245 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 185 A: T 1790184600 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 185 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 125 A: T 1790184600 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 125 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 95 A: T 1790189100 ask_x 0.95 ask_y 0.04 k_top 0.996013 k_shares 0.996218325029541646190483157603929361685280987745273121448225 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 95 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 65 A: T 1790186400 ask_x 0.480 ask_y 0.485 k_top 0.99995625 k_shares 1.00127013455235589192119365130384999402817782813903228834089 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 65 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 35 A: T 1790184600 ask_x 0.95 ask_y 0.04 k_top 0.996013 k_shares 0.996218325029541646190483157603929361685280987745273121448225 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 35 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 15 A: T 1790184600 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 15 B: T 1790187300 ask_x 0.97 ask_y 0.02 k_top 0.993409 k_shares 0.993514338022667012364358969597374155040594912188690516780536 skew_ns 400000000 - barred
[2026-10-10T08:30:11Z] pre-fee inversions, ask_x + ask_y < 1: 4 rows - barred
[2026-10-10T08:30:11Z] firm_margin_shares: n 1, min 0.003781674970458353809516842396070638314719012254726878551775, median 0.003781674970458353809516842396070638314719012254726878551775, max 0.003781674970458353809516842396070638314719012254726878551775 - barred
[2026-10-10T08:30:11Z] firm_skew_ns: n 1, min 0, median 0, max 0 - barred
[2026-10-10T08:30:11Z] firm_dt_ms: n 1, min 0, median 0, max 0 - barred
[2026-10-10T08:30:11Z] firm_lag_ms: n 2, min 25, median 25, max 25 - barred
[2026-10-10T08:30:11Z] firm_q: n 1, min 20, median 20, max 20 - barred
[2026-10-10T08:30:11Z] loose_margin_top: n 3, min 0.00004375, median 0.003987, max 0.006591 - barred
[2026-10-10T08:30:11Z] firm profit at the touch, the best unit a window: 0.075633499409167076190336847921412766294380245094537571035500 USDC, 1.21013599054667321904538956674260426071008392151260113656800 a day of members - barred
[2026-10-10T08:30:11Z] members by |D| in USD: {'1-10': {'members': 5, 'firm': 1, 'any': 3}, '<1': {'members': 1, 'firm': 0, 'any': 1}} - barred
[2026-10-10T08:30:11Z] wrote t-units.csv sha256 fa89f54a8fd0020bf7f0525734570af7461fc7ddf80c7ae0f621c80c1e96edc5 and t-reading.json sha256 c75b2ab559112066f5d29bbd18101009f2878b877285a8a4e95dec9e22075653
[2026-10-10T08:30:11Z]   ok  V_firm 1 and V_any 4: VIOLATION
[2026-10-10T08:30:11Z]   ok  five clean members: the sixth has an invalid unit
[2026-10-10T08:30:11Z]   ok  49 rows, one invalid unit, by its hash
[2026-10-10T08:30:11Z]   ok  classes: firm 1, loose 3, none 43, unquoted 1
[2026-10-10T08:30:11Z]   ok  loose: convention 1, apart 2 - received 400 ms apart, and books 300 ms apart by their own clocks
[2026-10-10T08:30:11Z]   ok  the firm unit's profit at the touch: its margin, 0.0037816749..., times 20 shares
[2026-10-10T08:30:11Z]   ok  four rows whose asks sum below 1 before any fee
[2026-10-10T08:30:11Z] unchanged /root/tz24-work/selftest-tmp/set/t-units.csv sha256 fa89f54a8fd0020bf7f0525734570af7461fc7ddf80c7ae0f621c80c1e96edc5
[2026-10-10T08:30:11Z] unchanged /root/tz24-work/selftest-tmp/set/t-reading.json sha256 c75b2ab559112066f5d29bbd18101009f2878b877285a8a4e95dec9e22075653
[2026-10-10T08:30:11Z] books: 6 members, 42 units, 49 rows, invalid {'hash': 1}
[2026-10-10T08:30:11Z] rows by class: {'firm': 1, 'loose': 3, 'none': 43, 'unquoted': 1}; loose by reason: {'convention': 1, 'apart': 2, 'no time': 0}
[2026-10-10T08:30:11Z] tau' 245: {'firm': 0, 'loose': 0, 'none': 6, 'unquoted': 1}
[2026-10-10T08:30:11Z] tau' 185: {'firm': 0, 'loose': 0, 'none': 7, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau' 125: {'firm': 0, 'loose': 0, 'none': 6, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau'  95: {'firm': 0, 'loose': 1, 'none': 6, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau'  65: {'firm': 0, 'loose': 1, 'none': 6, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau'  35: {'firm': 1, 'loose': 0, 'none': 6, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau'  15: {'firm': 0, 'loose': 1, 'none': 6, 'unquoted': 0}
[2026-10-10T08:30:11Z] by pair: {'A': {'firm': 1, 'loose': 2, 'none': 23, 'unquoted': 1}, 'B': {'firm': 0, 'loose': 1, 'none': 20, 'unquoted': 0}}
[2026-10-10T08:30:11Z] windows with a firm violation V_firm 1 of 6; with any V_any 4 of 6; clean members 5
[2026-10-10T08:30:11Z] NONE possible: False; its alternative at the clean members, theta1 = 0.653427578422426803558874074240464311659953174971785519254457 a window
[2026-10-10T08:30:11Z] ROW columns: class,reason,T,tau',pair,ask_x,ask_y,k_top,k_shares,skew_ns,ts_x,ts_y,dt_ms,q_x,q_y,R0,R600
[2026-10-10T08:30:11Z] ROW firm,,1790184600,35,A,0.95,0.04,0.996013,0.996218325029541646190483157603929361685280987745273121448225,0,1790185465020,1790185465020,0,50,20,78000.5,78010.25
[2026-10-10T08:30:11Z] ROW loose,convention,1790186400,65,A,0.480,0.485,0.99995625,1.00127013455235589192119365130384999402817782813903228834089,0,1790187235020,1790187235020,0,9,9,78000.5,78010.25
[2026-10-10T08:30:11Z] ROW loose,apart,1790187300,15,B,0.97,0.02,0.993409,0.993514338022667012364358969597374155040594912188690516780536,400000000,1790188185020,1790188185020,0,7,8,78000.5,77990.75
[2026-10-10T08:30:11Z] ROW loose,apart,1790189100,95,A,0.95,0.04,0.996013,0.996218325029541646190483157603929361685280987745273121448225,0,1790189905020,1790189905320,300,50,20,78000.5,78000.5
[2026-10-10T08:30:11Z] closest tau' 245 A: T 1790184600 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 245 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 185 A: T 1790184600 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 185 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 125 A: T 1790184600 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 125 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 95 A: T 1790189100 ask_x 0.95 ask_y 0.04 k_top 0.996013 k_shares 0.996218325029541646190483157603929361685280987745273121448225 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 95 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 65 A: T 1790186400 ask_x 0.480 ask_y 0.485 k_top 0.99995625 k_shares 1.00127013455235589192119365130384999402817782813903228834089 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 65 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 35 A: T 1790184600 ask_x 0.95 ask_y 0.04 k_top 0.996013 k_shares 0.996218325029541646190483157603929361685280987745273121448225 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 35 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 15 A: T 1790184600 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 15 B: T 1790187300 ask_x 0.97 ask_y 0.02 k_top 0.993409 k_shares 0.993514338022667012364358969597374155040594912188690516780536 skew_ns 400000000 - barred
[2026-10-10T08:30:11Z] pre-fee inversions, ask_x + ask_y < 1: 4 rows - barred
[2026-10-10T08:30:11Z] firm_margin_shares: n 1, min 0.003781674970458353809516842396070638314719012254726878551775, median 0.003781674970458353809516842396070638314719012254726878551775, max 0.003781674970458353809516842396070638314719012254726878551775 - barred
[2026-10-10T08:30:11Z] firm_skew_ns: n 1, min 0, median 0, max 0 - barred
[2026-10-10T08:30:11Z] firm_dt_ms: n 1, min 0, median 0, max 0 - barred
[2026-10-10T08:30:11Z] firm_lag_ms: n 2, min 25, median 25, max 25 - barred
[2026-10-10T08:30:11Z] firm_q: n 1, min 20, median 20, max 20 - barred
[2026-10-10T08:30:11Z] loose_margin_top: n 3, min 0.00004375, median 0.003987, max 0.006591 - barred
[2026-10-10T08:30:11Z] firm profit at the touch, the best unit a window: 0.075633499409167076190336847921412766294380245094537571035500 USDC, 1.21013599054667321904538956674260426071008392151260113656800 a day of members - barred
[2026-10-10T08:30:11Z] members by |D| in USD: {'1-10': {'members': 5, 'firm': 1, 'any': 3}, '<1': {'members': 1, 'firm': 0, 'any': 1}} - barred
[2026-10-10T08:30:11Z] wrote t-units.csv sha256 fa89f54a8fd0020bf7f0525734570af7461fc7ddf80c7ae0f621c80c1e96edc5 and t-reading.json sha256 c75b2ab559112066f5d29bbd18101009f2878b877285a8a4e95dec9e22075653
[2026-10-10T08:30:11Z]   ok  a second score writes and returns the same
[2026-10-10T08:30:11Z]   ok  the constants file is byte-identical with a book changed
[2026-10-10T08:30:11Z] books: 6 members, 42 units, 49 rows, invalid {'hash': 1}
[2026-10-10T08:30:11Z] rows by class: {'firm': 0, 'loose': 3, 'none': 44, 'unquoted': 1}; loose by reason: {'convention': 1, 'apart': 2, 'no time': 0}
[2026-10-10T08:30:11Z] tau' 245: {'firm': 0, 'loose': 0, 'none': 6, 'unquoted': 1}
[2026-10-10T08:30:11Z] tau' 185: {'firm': 0, 'loose': 0, 'none': 7, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau' 125: {'firm': 0, 'loose': 0, 'none': 6, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau'  95: {'firm': 0, 'loose': 1, 'none': 6, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau'  65: {'firm': 0, 'loose': 1, 'none': 6, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau'  35: {'firm': 0, 'loose': 0, 'none': 7, 'unquoted': 0}
[2026-10-10T08:30:11Z] tau'  15: {'firm': 0, 'loose': 1, 'none': 6, 'unquoted': 0}
[2026-10-10T08:30:11Z] by pair: {'A': {'firm': 0, 'loose': 2, 'none': 24, 'unquoted': 1}, 'B': {'firm': 0, 'loose': 1, 'none': 20, 'unquoted': 0}}
[2026-10-10T08:30:11Z] windows with a firm violation V_firm 0 of 6; with any V_any 3 of 6; clean members 5
[2026-10-10T08:30:11Z] NONE possible: False; its alternative at the clean members, theta1 = 0.653427578422426803558874074240464311659953174971785519254457 a window
[2026-10-10T08:30:11Z] ROW columns: class,reason,T,tau',pair,ask_x,ask_y,k_top,k_shares,skew_ns,ts_x,ts_y,dt_ms,q_x,q_y,R0,R600
[2026-10-10T08:30:11Z] ROW loose,convention,1790186400,65,A,0.480,0.485,0.99995625,1.00127013455235589192119365130384999402817782813903228834089,0,1790187235020,1790187235020,0,9,9,78000.5,78010.25
[2026-10-10T08:30:11Z] ROW loose,apart,1790187300,15,B,0.97,0.02,0.993409,0.993514338022667012364358969597374155040594912188690516780536,400000000,1790188185020,1790188185020,0,7,8,78000.5,77990.75
[2026-10-10T08:30:11Z] ROW loose,apart,1790189100,95,A,0.95,0.04,0.996013,0.996218325029541646190483157603929361685280987745273121448225,0,1790189905020,1790189905320,300,50,20,78000.5,78000.5
[2026-10-10T08:30:11Z] closest tau' 245 A: T 1790184600 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 245 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 185 A: T 1790184600 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 185 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 125 A: T 1790184600 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 125 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 95 A: T 1790189100 ask_x 0.95 ask_y 0.04 k_top 0.996013 k_shares 0.996218325029541646190483157603929361685280987745273121448225 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 95 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 65 A: T 1790186400 ask_x 0.480 ask_y 0.485 k_top 0.99995625 k_shares 1.00127013455235589192119365130384999402817782813903228834089 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 65 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 35 A: T 1790184600 ask_x 0.96 ask_y 0.04 k_top 1.005376 k_shares 1.00557719418832422033838831059728818737060682432251126481765 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 35 B: T 1790185500 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 15 A: T 1790184600 ask_x 0.52 ask_y 0.52 k_top 1.074944 k_shares 1.07615894039735099337748344370860927152317880794701986754967 skew_ns 0 - barred
[2026-10-10T08:30:11Z] closest tau' 15 B: T 1790187300 ask_x 0.97 ask_y 0.02 k_top 0.993409 k_shares 0.993514338022667012364358969597374155040594912188690516780536 skew_ns 400000000 - barred
[2026-10-10T08:30:11Z] pre-fee inversions, ask_x + ask_y < 1: 3 rows - barred
[2026-10-10T08:30:11Z] firm_margin_shares: none - barred
[2026-10-10T08:30:11Z] firm_skew_ns: none - barred
[2026-10-10T08:30:11Z] firm_dt_ms: none - barred
[2026-10-10T08:30:11Z] firm_lag_ms: none - barred
[2026-10-10T08:30:11Z] firm_q: none - barred
[2026-10-10T08:30:11Z] loose_margin_top: n 3, min 0.00004375, median 0.003987, max 0.006591 - barred
[2026-10-10T08:30:11Z] firm profit at the touch, the best unit a window: 0 USDC, 0 a day of members - barred
[2026-10-10T08:30:11Z] members by |D| in USD: {'1-10': {'members': 5, 'firm': 0, 'any': 2}, '<1': {'members': 1, 'firm': 0, 'any': 1}} - barred
[2026-10-10T08:30:11Z] wrote t-units.csv sha256 e9ed8b1f47d54c955d95985510f17f872f1d264d877c4bfeb1cc12f5acf716ca and t-reading.json sha256 546a035a5d08208fa3d27f05da46d7f713f0402e6088a347d6682a0c30cd0385
[2026-10-10T08:30:11Z]   ok  the score moves when the book moves: 0.96 + 0.04 is no violation
[2026-10-10T08:30:11Z]   ok  the synthetic book stands
[2026-10-10T08:30:11Z]   ok  gzip is deterministic
[2026-10-10T08:30:11Z]   ok  JSON is sorted with Decimals as text
[2026-10-10T08:30:11Z]   ok  no exponent form
[2026-10-10T08:30:11Z]   ok  tz14's own hook recorded no open under the recorder's root
[2026-10-10T08:30:11Z] 122 of 122 checks passed
[2026-10-10T08:30:11Z] malloc tuned: True
[2026-10-10T08:30:11Z] peak memory of this run: 46964736 bytes
[2026-10-10T08:30:11Z] opens refused under the capture roots: 0; chain book opens: window.json 0, books.jsonl.gz 0; tz14's record of opens under the recorder's root: 0
exit=0
```

### 2.3 §3.3 — the units, and the directories beside this session

`I still` recorded both units in `state.json` (`logs/33-still.log`). Then `I scratch` listed the UUID directories
beside this session's own `5c15abf7-532c-5a8a-9dfa-19c904ad993e` (`logs/33-scratch.log`). It named **2 earlier**:
`5ce9f787…` and `750b3996…`, TZ-23's session pair, born 2026-10-09 18:39, whose process is gone. It named **1 live**:
`65948b60…`, born 2026-10-10 08:27:48 UTC, when pid `687007`, the `claude.exe` of this session, started. The two `claude` processes running since
2026-10-07 20:05:37 UTC, pids `337573` and `337576`, made none of the three.

```
$ I still   # 2026-10-10T08:30:21Z
[2026-10-10T08:30:21Z] btc-recorder.service {'MainPID': '4148534', 'NRestarts': '2', 'ActiveState': 'active'}, MemoryCurrent 16203776, MemoryPeak 200912896
[2026-10-10T08:30:21Z] btc-chainbook.service {'MainPID': '4064090', 'NRestarts': '1', 'ActiveState': 'active'}, MemoryCurrent 7090176, MemoryPeak 18735104
[2026-10-10T08:30:21Z] still: recorded
[2026-10-10T08:30:21Z] malloc tuned: True
[2026-10-10T08:30:21Z] peak memory of this run: 26636288 bytes
[2026-10-10T08:30:21Z] opens refused under the capture roots: 0; chain book opens: window.json 0, books.jsonl.gz 0; tz14's record of opens under the recorder's root: not loaded
exit=0
```

```
$ I scratch "$(dirname "$S")"   # S=/tmp/claude-0/-root-btc-5m-twap/5c15abf7-532c-5a8a-9dfa-19c904ad993e/scratchpad  2026-10-10T08:30:21Z
[2026-10-10T08:30:21Z] running 337573 started 2026-10-07T20:05:37Z claude
[2026-10-10T08:30:21Z] running 337576 started 2026-10-07T20:05:37Z claude
[2026-10-10T08:30:21Z] running 687007 started 2026-10-10T08:27:48Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-10-10T08:30:21Z] 5ce9f787-ea2c-5497-8888-63b97cb927e8 born 2026-10-09T18:39:09Z: earlier
[2026-10-10T08:30:21Z] 65948b60-83f3-4efd-93cf-43514331137a born 2026-10-10T08:27:48Z: live, process [687007]
[2026-10-10T08:30:21Z] 750b3996-3a2d-49fb-823d-1321cd631528 born 2026-10-09T18:39:07Z: earlier
[2026-10-10T08:30:21Z] malloc tuned: True
[2026-10-10T08:30:21Z] peak memory of this run: 26509312 bytes
[2026-10-10T08:30:21Z] opens refused under the capture roots: 0; chain book opens: window.json 0, books.jsonl.gz 0; tz14's record of opens under the recorder's root: not loaded
exit=0
```

### 2.4 §9 B-RECLAIM-SCRATCH — after §3.3, before §3.4

Before removing anything the Executor looked at both targets (`logs/33-scratch-targets.log`, §6 item 2).
`5ce9f787…` held 1,929 bytes in 4 files, the harness's `tasks/` output of TZ-23's session, and an empty scratchpad.
`750b3996…` held an empty scratchpad. `I reclaim` named both and printed `RECLAIM PASS`: 4 files considered, 0 named by a
report, 0 kept by name, 0 copied, 0 already held, store 1,561 → 1,561. Then came one `rm -rf` per directory, each
`exit=0`, and `test -e` `exit=1` for both. **Neither was refused** (`logs/33b-reclaim-scratch.log`). The live
`65948b60…` and this session's own directory were kept.

```
$ du -sb; find -type f | wc -l; find -maxdepth 2 (look before removing)   # 2026-10-10T08:30:30Z
1929	/tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8
files: 4
/tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8
/tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8/scratchpad
/tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8/tasks
/tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8/tasks/b3c43ghl6.output
/tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8/tasks/bgx1pcf6d.output
/tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8/tasks/bi5vh7nxz.output
/tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8/tasks/bmqy0r0ch.output
0	/tmp/claude-0/-root-btc-5m-twap/750b3996-3a2d-49fb-823d-1321cd631528
files: 0
/tmp/claude-0/-root-btc-5m-twap/750b3996-3a2d-49fb-823d-1321cd631528
/tmp/claude-0/-root-btc-5m-twap/750b3996-3a2d-49fb-823d-1321cd631528/scratchpad
```

```
$ I reclaim /tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8 /tmp/claude-0/-root-btc-5m-twap/750b3996-3a2d-49fb-823d-1321cd631528   # 2026-10-10T08:30:34Z
[2026-10-10T08:30:34Z] reclaim: 1786 report tokens; forensic store holds 1561 files
[2026-10-10T08:30:34Z] RECLAIM PASS: 4 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 1561 -> 1561 files
[2026-10-10T08:30:34Z] malloc tuned: True
[2026-10-10T08:30:34Z] peak memory of this run: 27938816 bytes
[2026-10-10T08:30:34Z] opens refused under the capture roots: 0; chain book opens: window.json 0, books.jsonl.gz 0; tz14's record of opens under the recorder's root: not loaded
exit=0
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8   # 2026-10-10T08:30:48Z
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8
exit=1
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/750b3996-3a2d-49fb-823d-1321cd631528   # 2026-10-10T08:30:52Z
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/750b3996-3a2d-49fb-823d-1321cd631528
exit=1
```

### 2.5 §3.4 — G-REHEARSAL (V5)

`I rehearse` read TZ-17's 200 windows, `1788998400` … `1789177500`, by 20 requests. **G-REHEARSAL PASS: 10 of 10
figures equal** to the Architect's `REF` (`logs/34-rehearse.log`). Its `set.json` hashed
`4635cb07fce5f998da23cca5bc376160f704df2e1772e542ba8d52883dd6320a`, the value §4.1 records and judges by nothing.

| figure | instrument | the Architect's | |
|---|---|---|---|
| windows considered | `200` | `200` | equal |
| members | `200` | `200` | equal |
| `D > 0` | `102` | `102` | equal |
| `D < 0` | `98` | `98` | equal |
| `D = 0` | `0` | `0` | equal |
| fifteen-minute Up | `98` | `98` | equal |
| five-minute Up | `102` | `102` | equal |
| `Σ D` | `-2198.32154130825` | `-2198.32154130825` | equal |
| `Σ \|D\|` | `19953.70645914237` | `19953.70645914237` | equal |
| digest | `a9b57a6ea03fa6d57d964afcf1aa17da463547a5bf216069430d25d99cf1b3ee` | `a9b57a6ea03fa6d57d964afcf1aa17da463547a5bf216069430d25d99cf1b3ee` | equal |

```
$ I rehearse   # 2026-10-10T08:30:56Z
[2026-10-10T08:30:56Z] MemAvailable 299229184 bytes, floor 141189120
[2026-10-10T08:30:58Z] the set formed in 2.0 s: 200 considered, 200 members, 20 document requests, /root/tz24-work/rehearsal/set.json sha256 4635cb07fce5f998da23cca5bc376160f704df2e1772e542ba8d52883dd6320a
[2026-10-10T08:30:58Z] G-REHEARSAL windows   instrument 200, the Architect's 200, equal
[2026-10-10T08:30:58Z] G-REHEARSAL members   instrument 200, the Architect's 200, equal
[2026-10-10T08:30:58Z] G-REHEARSAL d_pos     instrument 102, the Architect's 102, equal
[2026-10-10T08:30:58Z] G-REHEARSAL d_neg     instrument 98, the Architect's 98, equal
[2026-10-10T08:30:58Z] G-REHEARSAL d_zero    instrument 0, the Architect's 0, equal
[2026-10-10T08:30:58Z] G-REHEARSAL up15      instrument 98, the Architect's 98, equal
[2026-10-10T08:30:58Z] G-REHEARSAL up5       instrument 102, the Architect's 102, equal
[2026-10-10T08:30:58Z] G-REHEARSAL sum_d     instrument -2198.32154130825, the Architect's -2198.32154130825, equal
[2026-10-10T08:30:58Z] G-REHEARSAL sum_abs_d instrument 19953.70645914237, the Architect's 19953.70645914237, equal
[2026-10-10T08:30:58Z] G-REHEARSAL digest    instrument a9b57a6ea03fa6d57d964afcf1aa17da463547a5bf216069430d25d99cf1b3ee, the Architect's a9b57a6ea03fa6d57d964afcf1aa17da463547a5bf216069430d25d99cf1b3ee, equal
[2026-10-10T08:30:58Z] G-REHEARSAL PASS: 10 of 10 figures equal; 20 document requests
[2026-10-10T08:30:58Z] malloc tuned: True
[2026-10-10T08:30:58Z] peak memory of this run: 30982144 bytes
[2026-10-10T08:30:58Z] opens refused under the capture roots: 0; chain book opens: window.json 0, books.jsonl.gz 0; tz14's record of opens under the recorder's root: not loaded
exit=0
```

### 2.6 §3.5 — the set, G-SET (V6)

`I fetch` opened the 1,175 windows' `window.json` where a directory existed, 1,085 of them. It then requested the
settled documents of the 1,079 that qualified, ten windows a request, **108 requests**. After its first 20 it
projected `11` s, against the `900` s fail-fast bound. The set formed in `11.1` s. **G-SET PASS**: every one of the
1,175 windows has a status, the members are exactly the windows whose status is `member`, in order, and `set.json`'s
SHA-256 `239fcbe8704da6290c832fea2e2fe537ee58768236de79d74e823f259cb0d377` is in `state.json`. No network failure
occurred, so `fetch` ran once.

| status | windows |
|---|---|
| `member` | 1,079 |
| `no directory` | 90 |
| `incomplete` | 6 |
| **considered** | **1,175** |

No window failed on its documents or on E1, E2 or E3: every window whose `window.json` qualified became a member.

```
$ I fetch   # 2026-10-10T08:31:02Z
[2026-10-10T08:31:02Z] MemAvailable 293261312 bytes, floor 141189120
[2026-10-10T08:31:05Z] projected 11 s for 108 document requests after 20
[2026-10-10T08:31:14Z] the set formed in 11.1 s: 1175 considered, 1079 members, 108 document requests, /root/tz24-work/set/set.json sha256 239fcbe8704da6290c832fea2e2fe537ee58768236de79d74e823f259cb0d377
[2026-10-10T08:31:14Z] G-SET PASS: 1175 considered, 1079 members; statuses {'incomplete': 6, 'member': 1079, 'no directory': 90}; set.json sha256 239fcbe8704da6290c832fea2e2fe537ee58768236de79d74e823f259cb0d377
[2026-10-10T08:31:14Z] malloc tuned: True
[2026-10-10T08:31:14Z] peak memory of this run: 37625856 bytes
[2026-10-10T08:31:14Z] opens refused under the capture roots: 0; chain book opens: window.json 1085, books.jsonl.gz 0; tz14's record of opens under the recorder's root: not loaded
exit=0
```

**The members.** The first is `1790184600`, 2026-09-23 17:30 UTC, and the last `1791241200`, 2026-10-05 23:00 UTC.

| split | count |
|---|---|
| members | 1,079 |
| span 1, before the chain book's gap (`T < 1791099000`) | 920 |
| span 2, after it | 159 |
| weekend | 292 |
| weekday (1,079 − 292) | 787 |
| pair A (`D > 0`) | 546 |
| pair B (`D < 0`) | 533 |
| both (`D = 0`) | 0 |

Member list SHA-256 `385c917fd8bf250b43b04aa278a212684b0e3ec52dd804a511aee8ecabd2d8df`; set file SHA-256
`239fcbe8704da6290c832fea2e2fe537ee58768236de79d74e823f259cb0d377`.

**Against §1's recorded expectation.** §1 expected 1,084 members if every window but the 90 lost and `1791017100`
qualified: 791 weekday and 293 weekend, 925 before the gap and 159 after. It asserts nothing. Five more windows read
`incomplete`: `1790193600`, `1790328600`, `1790550900`, `1790820900` and `1790833500`, all before the gap. One of them,
`1790550900`, falls on a Sunday. `window.json` reads `incomplete` where `checkpoints_complete` is not `7` or `missed` is
not `0`, and the instrument prints no finer reason. Nothing else under the chain book's root was opened to find one
(§2 item 3).

### 2.7 §3.6 — the constants, twice (V7)

`I constants` wrote `set/tz24-constants.json`, SHA-256
`1b27e8a9f4093c3bab113d67eda7893d3f0526ebdb5948c172fb5d3219e0cf46`, and recorded it in `state.json`. The second run
printed `unchanged` for it: **1 of 1**.

| constant | value |
|---|---|
| `N` | 1,079 |
| NONE possible (`N >= 528`) | True |
| `θ1` at `N` | `0.004898359790725944136001184241744509178557100705137292214062` |
| power of VIOLATION at `θ = 0.001` | `0.660248176891766708521835314864333087541961318254534830788946` |
| power at `θ = 0.005` | `0.995521793410759332193484305680646866638596520931065221796568` |
| power at `θ = 0.01` | `0.999980484711733928908205366309888486084467410293513828125869` |

Every non-member with its reason, 96 lines, is in run 1's output, verbatim (`logs/36-constants-1.log`):

```
$ I constants   # run 1, 2026-10-10T08:31:20Z
[2026-10-10T08:31:20Z] MemAvailable 300302336 bytes, floor 141189120
[2026-10-10T08:31:20Z] considered 1175, members 1079, first 1790184600 2026-09-23T17:30:00Z, last 1791241200 2026-10-05T23:00:00Z, weekend members 292, by span {'1': 920, '2': 159}
[2026-10-10T08:31:20Z] member list sha 385c917fd8bf250b43b04aa278a212684b0e3ec52dd804a511aee8ecabd2d8df; set sha 239fcbe8704da6290c832fea2e2fe537ee58768236de79d74e823f259cb0d377
[2026-10-10T08:31:20Z] members by pair: {'A': 546, 'B': 533, 'AB': 0}
[2026-10-10T08:31:20Z] non-member 1790193600 2026-09-23T20:00:00Z: incomplete
[2026-10-10T08:31:20Z] non-member 1790328600 2026-09-25T09:30:00Z: incomplete
[2026-10-10T08:31:20Z] non-member 1790550900 2026-09-27T23:15:00Z: incomplete
[2026-10-10T08:31:20Z] non-member 1790820900 2026-10-01T02:15:00Z: incomplete
[2026-10-10T08:31:20Z] non-member 1790833500 2026-10-01T05:45:00Z: incomplete
[2026-10-10T08:31:20Z] non-member 1791017100 2026-10-03T08:45:00Z: incomplete
[2026-10-10T08:31:20Z] non-member 1791018000 2026-10-03T09:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791018900 2026-10-03T09:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791019800 2026-10-03T09:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791020700 2026-10-03T09:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791021600 2026-10-03T10:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791022500 2026-10-03T10:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791023400 2026-10-03T10:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791024300 2026-10-03T10:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791025200 2026-10-03T11:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791026100 2026-10-03T11:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791027000 2026-10-03T11:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791027900 2026-10-03T11:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791028800 2026-10-03T12:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791029700 2026-10-03T12:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791030600 2026-10-03T12:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791031500 2026-10-03T12:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791032400 2026-10-03T13:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791033300 2026-10-03T13:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791034200 2026-10-03T13:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791035100 2026-10-03T13:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791036000 2026-10-03T14:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791036900 2026-10-03T14:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791037800 2026-10-03T14:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791038700 2026-10-03T14:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791039600 2026-10-03T15:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791040500 2026-10-03T15:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791041400 2026-10-03T15:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791042300 2026-10-03T15:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791043200 2026-10-03T16:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791044100 2026-10-03T16:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791045000 2026-10-03T16:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791045900 2026-10-03T16:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791046800 2026-10-03T17:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791047700 2026-10-03T17:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791048600 2026-10-03T17:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791049500 2026-10-03T17:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791050400 2026-10-03T18:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791051300 2026-10-03T18:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791052200 2026-10-03T18:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791053100 2026-10-03T18:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791054000 2026-10-03T19:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791054900 2026-10-03T19:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791055800 2026-10-03T19:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791056700 2026-10-03T19:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791057600 2026-10-03T20:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791058500 2026-10-03T20:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791059400 2026-10-03T20:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791060300 2026-10-03T20:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791061200 2026-10-03T21:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791062100 2026-10-03T21:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791063000 2026-10-03T21:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791063900 2026-10-03T21:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791064800 2026-10-03T22:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791065700 2026-10-03T22:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791066600 2026-10-03T22:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791067500 2026-10-03T22:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791068400 2026-10-03T23:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791069300 2026-10-03T23:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791070200 2026-10-03T23:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791071100 2026-10-03T23:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791072000 2026-10-04T00:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791072900 2026-10-04T00:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791073800 2026-10-04T00:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791074700 2026-10-04T00:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791075600 2026-10-04T01:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791076500 2026-10-04T01:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791077400 2026-10-04T01:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791078300 2026-10-04T01:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791079200 2026-10-04T02:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791080100 2026-10-04T02:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791081000 2026-10-04T02:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791081900 2026-10-04T02:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791082800 2026-10-04T03:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791083700 2026-10-04T03:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791084600 2026-10-04T03:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791085500 2026-10-04T03:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791086400 2026-10-04T04:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791087300 2026-10-04T04:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791088200 2026-10-04T04:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791089100 2026-10-04T04:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791090000 2026-10-04T05:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791090900 2026-10-04T05:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791091800 2026-10-04T05:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791092700 2026-10-04T05:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791093600 2026-10-04T06:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791094500 2026-10-04T06:15:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791095400 2026-10-04T06:30:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791096300 2026-10-04T06:45:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791097200 2026-10-04T07:00:00Z: no directory
[2026-10-10T08:31:20Z] non-member 1791098100 2026-10-04T07:15:00Z: no directory
[2026-10-10T08:31:20Z] NONE possible: True (N 1079, N_MIN 528); its alternative theta1 = 0.004898359790725944136001184241744509178557100705137292214062 a window
[2026-10-10T08:31:20Z] power of VIOLATION against a firm-violation probability of 0.001 a window: 0.660248176891766708521835314864333087541961318254534830788946
[2026-10-10T08:31:20Z] power of VIOLATION against a firm-violation probability of 0.005 a window: 0.995521793410759332193484305680646866638596520931065221796568
[2026-10-10T08:31:20Z] power of VIOLATION against a firm-violation probability of 0.01 a window: 0.999980484711733928908205366309888486084467410293513828125869
[2026-10-10T08:31:20Z] wrote /root/tz24-work/set/tz24-constants.json sha256 1b27e8a9f4093c3bab113d67eda7893d3f0526ebdb5948c172fb5d3219e0cf46
[2026-10-10T08:31:20Z] malloc tuned: True
[2026-10-10T08:31:20Z] peak memory of this run: 29745152 bytes
[2026-10-10T08:31:20Z] opens refused under the capture roots: 0; chain book opens: window.json 0, books.jsonl.gz 0; tz14's record of opens under the recorder's root: not loaded
exit=0
```

Run 2 (`logs/36-constants-2.log`) printed the same lines but three. Its `MemAvailable` and peak differ, and it printed
one more line, `unchanged`:

```
$ I constants   # run 2, 2026-10-10T08:31:20Z
[2026-10-10T08:31:20Z] MemAvailable 297205760 bytes, floor 141189120
[2026-10-10T08:31:20Z] unchanged /root/tz24-work/set/tz24-constants.json sha256 1b27e8a9f4093c3bab113d67eda7893d3f0526ebdb5948c172fb5d3219e0cf46
[2026-10-10T08:31:20Z] peak memory of this run: 29741056 bytes
[2026-10-10T08:31:20Z] opens refused under the capture roots: 0; chain book opens: window.json 0, books.jsonl.gz 0; tz14's record of opens under the recorder's root: not loaded
exit=0
```

### 2.8 §3.7 — the score, twice (V8)

**B2 READING: VIOLATION.** Each `score` checked its preconditions: the constants' SHA-256 against `state.json`, the
set's against the constants, and `HEAD` `6f045cf` in `origin/tz-24-nesting-b2`. It wrote its ledger line, and only then
opened the books, 1,079 of them, one a member. The second run printed `unchanged` for both files: **2 of 2**.

| figure | value |
|---|---|
| members `N` | 1,079 |
| units, member × `tau'` | 7,553 |
| rows | 7,553 |
| invalid units | 0 — `invalid {}` |
| `N_clean`, every unit valid | 1,079 |
| `V_firm`, members with a firm row | **7** |
| `V_any`, members with a firm or a loose row | **9** |
| `θ1` at `N_clean` | `0.004898359790725944136001184241744509178557100705137292214062` |
| NONE possible | True |
| **reading** | **VIOLATION** |
| `tz24-units.csv` | SHA-256 `1c77a6323c38996a234aa47af430f1a6d42555a8e94881d49ba9a92e11e6eafe`, 964,508 bytes |
| `tz24-reading.json` | SHA-256 `c03c642eb687c4dcd7125a62186143c42d76fee6698306ec33712c1427eac621`, 3,944 bytes |

`N = N_clean`, so `θ1` is the same at both, as the two runs printed.

**Rows by class, `tau'` and pair** — the members' valid rows. No member has `D = 0`, so each valid unit is one row.

| `tau'` | firm | loose | none | unquoted | rows |
|---|---|---|---|---|---|
| 245 | 0 | 0 | 1,037 | 42 | 1,079 |
| 185 | 0 | 1 | 997 | 81 | 1,079 |
| 125 | 4 | 0 | 814 | 261 | 1,079 |
| 95 | 1 | 0 | 625 | 453 | 1,079 |
| 65 | 1 | 0 | 377 | 701 | 1,079 |
| 35 | 1 | 1 | 52 | 1,025 | 1,079 |
| 15 | 0 | 0 | 2 | 1,077 | 1,079 |
| **all** | **7** | **2** | **3,904** | **3,640** | **7,553** |

| pair | firm | loose | none | unquoted |
|---|---|---|---|---|
| A | 2 | 1 | 1,962 | 1,857 |
| B | 5 | 1 | 1,942 | 1,783 |

Loose by reason: `convention` 1, `apart` 1, `no time` 0. **Invalid checkpoints by reason: none.** All 7,553 units read
valid.

**Every firm and loose row the instrument printed, verbatim** — all 7 firm and both loose, under 40 a class, so none
is held back in `tz24-units.csv` alone:

```
[2026-10-10T08:31:31Z] ROW columns: class,reason,T,tau',pair,ask_x,ask_y,k_top,k_shares,skew_ns,ts_x,ts_y,dt_ms,q_x,q_y,R0,R600
[2026-10-10T08:31:31Z] ROW firm,,1790236800,125,B,0.03,0.96,0.994725,0.994880935367016058223405322479382567293991247588516594452882,3446997,1790237575033,1790237575028,5,668.81,8.98,84507.51638636478,84495.06896426226
[2026-10-10T08:31:31Z] ROW firm,,1790402400,35,B,0.02,0.97,0.993409,0.993514338022667012364358969597374155040594912188690516780536,6919036,1790403265027,1790403265027,0,60,1126.71,83909.05664084994,83902.15899068376
[2026-10-10T08:31:31Z] ROW firm,,1790405100,125,A,0.7,0.27,0.998497,0.999555315433783820005121784473630076048488379265233837233823,2950074,1790405875024,1790405875027,3,10,207.05,83900.35761667673,83901.10804754133
[2026-10-10T08:31:31Z] ROW firm,,1790844300,95,B,0.98,0.01,0.992065,0.992118524330968911434641785272778257885957069240441506903045,263381,1790845105029,1790845105030,1,300.16,17,83457.91629079662,83457.2739774078
[2026-10-10T08:31:31Z] ROW firm,,1790900100,125,B,0.03,0.96,0.994725,0.994880935367016058223405322479382567293991247588516594452882,660025,1790900875103,1790900875104,1,757.1,80,84878.22819159337,84865.13435796826
[2026-10-10T08:31:31Z] ROW firm,,1791016200,65,A,0.97,0.02,0.993409,0.993514338022667012364358969597374155040594912188690516780536,54992132,1791017035097,1791017035044,53,118.83,405,84592.51432442821,84595.46638578862
[2026-10-10T08:31:31Z] ROW firm,,1791238500,125,B,0.1,0.88,0.993692,0.994178204710389039543693169905756917337222853398644666425294,1991692,1791239275033,1791239275035,2,775.26,22.61,85958.03633436719,85932.91454821207
[2026-10-10T08:31:31Z] ROW loose,apart,1790390700,35,B,0.01,0.98,0.992065,0.992118524330968911434641785272778257885957069240441506903045,1978486,1790391565020,1790391564837,183,958.08,236.47,84016.4572713479,84016.11141113528
[2026-10-10T08:31:31Z] ROW loose,convention,1790427600,185,A,0.07,0.92,0.999709,1.00005533178547754902047680509623815282363780759804375031786,15332009,1790428315034,1790428315029,5,16,65,84048.25534062492,84067.75060321136
```

The seven firm rows are in seven windows, so `V_firm` = 7. In each, both replies were received within `54,992,132` ns,
under `150,000,000`, and both books' own timestamps were within `53` ms, under `150`. The loose `apart` row's books
are `183` ms apart by their own clocks. The loose `convention` row costs `0.999709` with the fee on top and
`1.00005533…` with the fee in shares.

**Barred from every reading** (§4.3), printed by `score`:

```
[2026-10-10T08:31:31Z] closest tau' 245 A: T 1791139500 ask_x 0.74 ask_y 0.25 k_top 1.016593 k_shares 1.01756990418223810555272180599845956299102773377851568735686 skew_ns 1964683 - barred
[2026-10-10T08:31:31Z] closest tau' 245 B: T 1790257500 ask_x 0.91 ask_y 0.09 k_top 1.011466 k_shares 1.01189238437336250096208484487194025984335727128329172279433 skew_ns 1233712 - barred
[2026-10-10T08:31:31Z] closest tau' 185 A: T 1790427600 ask_x 0.07 ask_y 0.92 k_top 0.999709 k_shares 1.00005533178547754902047680509623815282363780759804375031786 skew_ns 15332009 - barred
[2026-10-10T08:31:31Z] closest tau' 185 B: T 1790391600 ask_x 0.03 ask_y 0.97 k_top 1.004074 k_shares 1.00422667453599775492486587459671102685449550267341268611300 skew_ns 5038731 - barred
[2026-10-10T08:31:31Z] closest tau' 125 A: T 1790405100 ask_x 0.7 ask_y 0.27 k_top 0.998497 k_shares 0.999555315433783820005121784473630076048488379265233837233823 skew_ns 2950074 - barred
[2026-10-10T08:31:31Z] closest tau' 125 B: T 1791238500 ask_x 0.1 ask_y 0.88 k_top 0.993692 k_shares 0.994178204710389039543693169905756917337222853398644666425294 skew_ns 1991692 - barred
[2026-10-10T08:31:31Z] closest tau' 95 A: T 1790551800 ask_x 0.01 ask_y 0.99 k_top 1.001386 k_shares 1.00143808627788673087600559674032486757061736489422471092395 skew_ns 14851879 - barred
[2026-10-10T08:31:31Z] closest tau' 95 B: T 1790844300 ask_x 0.98 ask_y 0.01 k_top 0.992065 k_shares 0.992118524330968911434641785272778257885957069240441506903045 skew_ns 263381 - barred
[2026-10-10T08:31:31Z] closest tau' 65 A: T 1791016200 ask_x 0.97 ask_y 0.02 k_top 0.993409 k_shares 0.993514338022667012364358969597374155040594912188690516780536 skew_ns 54992132 - barred
[2026-10-10T08:31:31Z] closest tau' 65 B: T 1790308800 ask_x 0.001 ask_y 0.999 k_top 1.00013986 k_shares 1.00014512278452629834980316976183193425429960406237435943148 skew_ns 1619821 - barred
[2026-10-10T08:31:31Z] closest tau' 35 A: T 1791137700 ask_x 0.98 ask_y 0.04 k_top 1.024060 k_shares 1.02425557014812160695642853682977781243655354202573139273199 skew_ns 8081588 - barred
[2026-10-10T08:31:31Z] closest tau' 35 B: T 1790390700 ask_x 0.01 ask_y 0.98 k_top 0.992065 k_shares 0.992118524330968911434641785272778257885957069240441506903045 skew_ns 1978486 - barred
[2026-10-10T08:31:31Z] closest tau' 15 A: T 1790434800 ask_x 0.95 ask_y 0.18 k_top 1.143657 k_shares 1.14429784960282695353533675949847381174658727570685815376095 skew_ns 9344803 - barred
[2026-10-10T08:31:31Z] pre-fee inversions, ask_x + ask_y < 1: 19 rows - barred
[2026-10-10T08:31:31Z] firm_margin_shares: n 7, min 0.000444684566216179994878215526369923951511620734766162766177, median 0.005821795289610960456306830094243082662777146601355333574706, max 0.007881475669031088565358214727221742114042930759558493096955 - barred
[2026-10-10T08:31:31Z] firm_skew_ns: n 7, min 263381, median 2950074, max 54992132 - barred
[2026-10-10T08:31:31Z] firm_dt_ms: n 7, min 0, median 2, max 53 - barred
[2026-10-10T08:31:31Z] firm_lag_ms: n 14, min 17, median 21, max 38 - barred
[2026-10-10T08:31:31Z] firm_q: n 7, min 8.98, median 22.61, max 118.83 - barred
[2026-10-10T08:31:31Z] loose_margin_top: n 2, min 0.000291, median 0.000291, max 0.007935 - barred
[2026-10-10T08:31:31Z] members by |D| in USD: {'10-100': {'members': 673, 'firm': 3, 'any': 4}, '>=100': {'members': 300, 'firm': 0, 'any': 0}, '<1': {'members': 11, 'firm': 2, 'any': 3}, '1-10': {'members': 95, 'firm': 2, 'any': 2}} - barred
```

`logs/37-score-1.log`, verbatim:

```
$ I score   # run 1, 2026-10-10T08:31:25Z
[2026-10-10T08:31:25Z] MemAvailable 295440384 bytes, floor 141189120
[2026-10-10T08:31:31Z] books: 1079 members, 7553 units, 7553 rows, invalid {}
[2026-10-10T08:31:31Z] rows by class: {'firm': 7, 'loose': 2, 'none': 3904, 'unquoted': 3640}; loose by reason: {'convention': 1, 'apart': 1, 'no time': 0}
[2026-10-10T08:31:31Z] tau' 245: {'firm': 0, 'loose': 0, 'none': 1037, 'unquoted': 42}
[2026-10-10T08:31:31Z] tau' 185: {'firm': 0, 'loose': 1, 'none': 997, 'unquoted': 81}
[2026-10-10T08:31:31Z] tau' 125: {'firm': 4, 'loose': 0, 'none': 814, 'unquoted': 261}
[2026-10-10T08:31:31Z] tau'  95: {'firm': 1, 'loose': 0, 'none': 625, 'unquoted': 453}
[2026-10-10T08:31:31Z] tau'  65: {'firm': 1, 'loose': 0, 'none': 377, 'unquoted': 701}
[2026-10-10T08:31:31Z] tau'  35: {'firm': 1, 'loose': 1, 'none': 52, 'unquoted': 1025}
[2026-10-10T08:31:31Z] tau'  15: {'firm': 0, 'loose': 0, 'none': 2, 'unquoted': 1077}
[2026-10-10T08:31:31Z] by pair: {'A': {'firm': 2, 'loose': 1, 'none': 1962, 'unquoted': 1857}, 'B': {'firm': 5, 'loose': 1, 'none': 1942, 'unquoted': 1783}}
[2026-10-10T08:31:31Z] windows with a firm violation V_firm 7 of 1079; with any V_any 9 of 1079; clean members 1079
[2026-10-10T08:31:31Z] NONE possible: True; its alternative at the clean members, theta1 = 0.004898359790725944136001184241744509178557100705137292214062 a window
[2026-10-10T08:31:31Z] ROW columns: class,reason,T,tau',pair,ask_x,ask_y,k_top,k_shares,skew_ns,ts_x,ts_y,dt_ms,q_x,q_y,R0,R600
[2026-10-10T08:31:31Z] ROW firm,,1790236800,125,B,0.03,0.96,0.994725,0.994880935367016058223405322479382567293991247588516594452882,3446997,1790237575033,1790237575028,5,668.81,8.98,84507.51638636478,84495.06896426226
[2026-10-10T08:31:31Z] ROW firm,,1790402400,35,B,0.02,0.97,0.993409,0.993514338022667012364358969597374155040594912188690516780536,6919036,1790403265027,1790403265027,0,60,1126.71,83909.05664084994,83902.15899068376
[2026-10-10T08:31:31Z] ROW firm,,1790405100,125,A,0.7,0.27,0.998497,0.999555315433783820005121784473630076048488379265233837233823,2950074,1790405875024,1790405875027,3,10,207.05,83900.35761667673,83901.10804754133
[2026-10-10T08:31:31Z] ROW firm,,1790844300,95,B,0.98,0.01,0.992065,0.992118524330968911434641785272778257885957069240441506903045,263381,1790845105029,1790845105030,1,300.16,17,83457.91629079662,83457.2739774078
[2026-10-10T08:31:31Z] ROW firm,,1790900100,125,B,0.03,0.96,0.994725,0.994880935367016058223405322479382567293991247588516594452882,660025,1790900875103,1790900875104,1,757.1,80,84878.22819159337,84865.13435796826
[2026-10-10T08:31:31Z] ROW firm,,1791016200,65,A,0.97,0.02,0.993409,0.993514338022667012364358969597374155040594912188690516780536,54992132,1791017035097,1791017035044,53,118.83,405,84592.51432442821,84595.46638578862
[2026-10-10T08:31:31Z] ROW firm,,1791238500,125,B,0.1,0.88,0.993692,0.994178204710389039543693169905756917337222853398644666425294,1991692,1791239275033,1791239275035,2,775.26,22.61,85958.03633436719,85932.91454821207
[2026-10-10T08:31:31Z] ROW loose,apart,1790390700,35,B,0.01,0.98,0.992065,0.992118524330968911434641785272778257885957069240441506903045,1978486,1790391565020,1790391564837,183,958.08,236.47,84016.4572713479,84016.11141113528
[2026-10-10T08:31:31Z] ROW loose,convention,1790427600,185,A,0.07,0.92,0.999709,1.00005533178547754902047680509623815282363780759804375031786,15332009,1790428315034,1790428315029,5,16,65,84048.25534062492,84067.75060321136
[2026-10-10T08:31:31Z] closest tau' 245 A: T 1791139500 ask_x 0.74 ask_y 0.25 k_top 1.016593 k_shares 1.01756990418223810555272180599845956299102773377851568735686 skew_ns 1964683 - barred
[2026-10-10T08:31:31Z] closest tau' 245 B: T 1790257500 ask_x 0.91 ask_y 0.09 k_top 1.011466 k_shares 1.01189238437336250096208484487194025984335727128329172279433 skew_ns 1233712 - barred
[2026-10-10T08:31:31Z] closest tau' 185 A: T 1790427600 ask_x 0.07 ask_y 0.92 k_top 0.999709 k_shares 1.00005533178547754902047680509623815282363780759804375031786 skew_ns 15332009 - barred
[2026-10-10T08:31:31Z] closest tau' 185 B: T 1790391600 ask_x 0.03 ask_y 0.97 k_top 1.004074 k_shares 1.00422667453599775492486587459671102685449550267341268611300 skew_ns 5038731 - barred
[2026-10-10T08:31:31Z] closest tau' 125 A: T 1790405100 ask_x 0.7 ask_y 0.27 k_top 0.998497 k_shares 0.999555315433783820005121784473630076048488379265233837233823 skew_ns 2950074 - barred
[2026-10-10T08:31:31Z] closest tau' 125 B: T 1791238500 ask_x 0.1 ask_y 0.88 k_top 0.993692 k_shares 0.994178204710389039543693169905756917337222853398644666425294 skew_ns 1991692 - barred
[2026-10-10T08:31:31Z] closest tau' 95 A: T 1790551800 ask_x 0.01 ask_y 0.99 k_top 1.001386 k_shares 1.00143808627788673087600559674032486757061736489422471092395 skew_ns 14851879 - barred
[2026-10-10T08:31:31Z] closest tau' 95 B: T 1790844300 ask_x 0.98 ask_y 0.01 k_top 0.992065 k_shares 0.992118524330968911434641785272778257885957069240441506903045 skew_ns 263381 - barred
[2026-10-10T08:31:31Z] closest tau' 65 A: T 1791016200 ask_x 0.97 ask_y 0.02 k_top 0.993409 k_shares 0.993514338022667012364358969597374155040594912188690516780536 skew_ns 54992132 - barred
[2026-10-10T08:31:31Z] closest tau' 65 B: T 1790308800 ask_x 0.001 ask_y 0.999 k_top 1.00013986 k_shares 1.00014512278452629834980316976183193425429960406237435943148 skew_ns 1619821 - barred
[2026-10-10T08:31:31Z] closest tau' 35 A: T 1791137700 ask_x 0.98 ask_y 0.04 k_top 1.024060 k_shares 1.02425557014812160695642853682977781243655354202573139273199 skew_ns 8081588 - barred
[2026-10-10T08:31:31Z] closest tau' 35 B: T 1790390700 ask_x 0.01 ask_y 0.98 k_top 0.992065 k_shares 0.992118524330968911434641785272778257885957069240441506903045 skew_ns 1978486 - barred
[2026-10-10T08:31:31Z] closest tau' 15 A: T 1790434800 ask_x 0.95 ask_y 0.18 k_top 1.143657 k_shares 1.14429784960282695353533675949847381174658727570685815376095 skew_ns 9344803 - barred
[2026-10-10T08:31:31Z] pre-fee inversions, ask_x + ask_y < 1: 19 rows - barred
[2026-10-10T08:31:31Z] firm_margin_shares: n 7, min 0.000444684566216179994878215526369923951511620734766162766177, median 0.005821795289610960456306830094243082662777146601355333574706, max 0.007881475669031088565358214727221742114042930759558493096955 - barred
[2026-10-10T08:31:31Z] firm_skew_ns: n 7, min 263381, median 2950074, max 54992132 - barred
[2026-10-10T08:31:31Z] firm_dt_ms: n 7, min 0, median 2, max 53 - barred
[2026-10-10T08:31:31Z] firm_lag_ms: n 14, min 17, median 21, max 38 - barred
[2026-10-10T08:31:31Z] firm_q: n 7, min 8.98, median 22.61, max 118.83 - barred
[2026-10-10T08:31:31Z] loose_margin_top: n 2, min 0.000291, median 0.000291, max 0.007935 - barred
[2026-10-10T08:31:31Z] firm profit at the touch, the best unit a window: 1.88538802598316343964004910674342397073030795778706841215341 USDC, 0.167745366537890352368345425623140594244772533779016281340804 a day of members - barred
[2026-10-10T08:31:31Z] members by |D| in USD: {'10-100': {'members': 673, 'firm': 3, 'any': 4}, '>=100': {'members': 300, 'firm': 0, 'any': 0}, '<1': {'members': 11, 'firm': 2, 'any': 3}, '1-10': {'members': 95, 'firm': 2, 'any': 2}} - barred
[2026-10-10T08:31:31Z] wrote tz24-units.csv sha256 1c77a6323c38996a234aa47af430f1a6d42555a8e94881d49ba9a92e11e6eafe and tz24-reading.json sha256 c03c642eb687c4dcd7125a62186143c42d76fee6698306ec33712c1427eac621
[2026-10-10T08:31:31Z] B2 READING: VIOLATION
[2026-10-10T08:31:31Z] malloc tuned: True
[2026-10-10T08:31:31Z] peak memory of this run: 62242816 bytes
[2026-10-10T08:31:31Z] opens refused under the capture roots: 0; chain book opens: window.json 0, books.jsonl.gz 1079; tz14's record of opens under the recorder's root: 0
exit=0
```

Run 2 (`logs/37-score-2.log`) printed the same lines as run 1 but its first line, its `MemAvailable` and its peak,
and two more lines, `unchanged` for both files:

```
$ I score   # run 2, 2026-10-10T08:31:36Z
[2026-10-10T08:31:36Z] MemAvailable 285106176 bytes, floor 141189120
[2026-10-10T08:31:42Z] unchanged /root/tz24-work/set/tz24-units.csv sha256 1c77a6323c38996a234aa47af430f1a6d42555a8e94881d49ba9a92e11e6eafe
[2026-10-10T08:31:42Z] unchanged /root/tz24-work/set/tz24-reading.json sha256 c03c642eb687c4dcd7125a62186143c42d76fee6698306ec33712c1427eac621
[2026-10-10T08:31:42Z] B2 READING: VIOLATION
[2026-10-10T08:31:42Z] peak memory of this run: 62386176 bytes
[2026-10-10T08:31:42Z] opens refused under the capture roots: 0; chain book opens: window.json 0, books.jsonl.gz 1079; tz14's record of opens under the recorder's root: 0
exit=0
```

**The ledger**, `book-ledger.jsonl`, 2 lines, one a `score` run:

```
{"at":"2026-10-10T08:31:25Z","constants_sha":"1b27e8a9f4093c3bab113d67eda7893d3f0526ebdb5948c172fb5d3219e0cf46","head":"6f045cffc3601b589d3b8b7a6a9af6f73991e18b","member_list_sha":"385c917fd8bf250b43b04aa278a212684b0e3ec52dd804a511aee8ecabd2d8df","members":1079}
{"at":"2026-10-10T08:31:36Z","constants_sha":"1b27e8a9f4093c3bab113d67eda7893d3f0526ebdb5948c172fb5d3219e0cf46","head":"6f045cffc3601b589d3b8b7a6a9af6f73991e18b","member_list_sha":"385c917fd8bf250b43b04aa278a212684b0e3ec52dd804a511aee8ecabd2d8df","members":1079}
```

### 2.9 §3.8 — G-STILL (V9)

**G-STILL PASS**: from 08:30:21 to 08:31:45 UTC both units kept their `MainPID`, `NRestarts` and `ActiveState`
(`logs/38-still.log`).

| unit | read | `MainPID` | `NRestarts` | `ActiveState` | `MemoryCurrent` | `MemoryPeak` |
|---|---|---|---|---|---|---|
| `btc-recorder.service` | §3.3, 08:30:21 | `4148534` | `2` | `active` | `16,203,776` | `200,912,896` |
| `btc-recorder.service` | §3.8, 08:31:45 | `4148534` | `2` | `active` | `125,329,408` | `200,912,896` |
| `btc-recorder.service` | §3.9, 08:32:01 | `4148534` | `2` | — | `125,366,272` | `200,912,896` |
| `btc-chainbook.service` | §3.3, 08:30:21 | `4064090` | `1` | `active` | `7,090,176` | `18,735,104` |
| `btc-chainbook.service` | §3.8, 08:31:45 | `4064090` | `1` | `active` | `6,778,880` | `18,735,104` |
| `btc-chainbook.service` | §3.9, 08:32:01 | `4064090` | `1` | — | `6,778,880` | `18,735,104` |

`MemoryCurrent` and `MemoryPeak` include page cache (map §6). The recorder's `MemoryPeak` reads `200,912,896`, above
the `191,582,208` TZ-23 read on 2026-10-09, and its `MemoryCurrent` moved from `16,203,776` to `125,329,408` within 84 s.
Both are printed for TZ-22 and judge nothing here.

```
$ I still   # 2026-10-10T08:31:45Z
[2026-10-10T08:31:45Z] btc-recorder.service {'MainPID': '4148534', 'NRestarts': '2', 'ActiveState': 'active'}, MemoryCurrent 125329408, MemoryPeak 200912896
[2026-10-10T08:31:45Z] btc-chainbook.service {'MainPID': '4064090', 'NRestarts': '1', 'ActiveState': 'active'}, MemoryCurrent 6778880, MemoryPeak 18735104
[2026-10-10T08:31:45Z] G-STILL PASS: unchanged since 2026-10-10T08:30:21Z
[2026-10-10T08:31:45Z] malloc tuned: True
[2026-10-10T08:31:45Z] peak memory of this run: 26636288 bytes
[2026-10-10T08:31:45Z] opens refused under the capture roots: 0; chain book opens: window.json 0, books.jsonl.gz 0; tz14's record of opens under the recorder's root: not loaded
exit=0
```

### 2.10 Memory and the capture roots — every mode (V10, V11)

| run | instant (UTC) | peak memory, bytes | `malloc tuned` | refused | `window.json` opens | `books.jsonl.gz` opens |
|---|---|---|---|---|---|---|
| `I0 fingerprint` | 08:29:12 | `27,553,792` | True | 0 | 0 | 0 |
| `I selftest` | 08:30:11 | `46,964,736` | True | 0 | 0 | 0 |
| `I still` | 08:30:21 | `26,636,288` | True | 0 | 0 | 0 |
| `I scratch` | 08:30:21 | `26,509,312` | True | 0 | 0 | 0 |
| `I reclaim`, B-RECLAIM-SCRATCH | 08:30:34 | `27,938,816` | True | 0 | 0 | 0 |
| `I rehearse` | 08:30:58 | `30,982,144` | True | 0 | 0 | 0 |
| `I fetch` | 08:31:14 | `37,625,856` | True | 0 | **1,085** | 0 |
| `I constants`, run 1 | 08:31:20 | `29,745,152` | True | 0 | 0 | 0 |
| `I constants`, run 2 | 08:31:20 | `29,741,056` | True | 0 | 0 | 0 |
| `I score`, run 1 | 08:31:31 | `62,242,816` | True | 0 | 0 | **1,079** |
| `I score`, run 2 | 08:31:42 | `62,386,176` | True | 0 | 0 | **1,079** |
| `I still`, G-STILL | 08:31:45 | `26,636,288` | True | 0 | 0 | 0 |
| `I reclaim`, B-RECLAIM-OWN | 08:39:26 | `28,540,928` | True | 0 | 0 | 0 |

**V10.** No open was refused at any mode. `fetch`'s `window.json` opens, 1,085, equal the 1,175 considered windows
less those whose status is `no directory` (90), `no window.json` (0) or `no books` (0). Its `books.jsonl.gz` opens are
0. Each `score`'s `books.jsonl.gz` opens, 1,079, equal `N`, and its `window.json` opens are 0. Every other mode
printed 0 and 0. `tz14`'s own hook, loaded by `selftest` and `score`, recorded 0 opens under the recorder's root.
**V11.** The largest peak is `62,386,176` bytes, `score` run 2, under half of §0.4's floor, `141,189,120`.
`malloc tuned: True` was printed at every mode. `floor_check` asserted glibc's two settings and the floor at
`rehearse`, `fetch`, `constants` and `score`.

### 2.11 §3.9 — the closing reads (V13), and contract §4.2's self-check (V12)

`logs/39-closing.log`, verbatim: §0.3's block again, then §3.9's four reads. Every §0.3 condition read as at the
opening. H1 to H4 held; `MemAvailable` was `282532 kB`; avail was `12,997,709,824`; the store was still at 1,561; and a
third worktree, `/root/tz24-work/wt` at `6f045cf`, was registered. Beside this session's directory only the live
`65948b60…` remains.

```
$ §0.3 block again
Sat Oct 10 08:32:01 AM UTC 2026
1791621121
1
MemTotal:         978640 kB
MemAvailable:     282532 kB
SwapTotal:       3174396 kB
SwapFree:        2815672 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12997709824
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
1
chainbook exit=0
active
active
exit=0
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
/root/tz23-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
1561
3.12.3 2.5.3
/root/btc-5m-twap       6108e4f [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/root/tz24-work/wt      6f045cf [tz-24-nesting-b2]
193916870	/root/.claude
525427468	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/5c15abf7-532c-5a8a-9dfa-19c904ad993e/scratchpad
total 16
drwx------  4 root root 4096 Oct 10 08:30 .
drwx------ 16 root root 4096 Oct 10 08:27 ..
drwx------  4 root root 4096 Oct 10 08:27 5c15abf7-532c-5a8a-9dfa-19c904ad993e
drwx------  3 root root 4096 Oct 10 08:27 65948b60-83f3-4efd-93cf-43514331137a
$ §3.9 reads
MainPID=4148534
NRestarts=2
MemoryCurrent=125366272
MemoryPeak=200912896

MainPID=4064090
NRestarts=1
MemoryCurrent=6778880
MemoryPeak=18735104
               total        used        free      shared  buff/cache   available
Mem:      1002127360   703741952    74657792      180224   408539136   298385408
Swap:     3250581504   367333376  2883248128
8485133	/root/tz24-work
193916870	/root/.claude
{
 "constants_at": "2026-10-10T08:31:20Z",
 "constants_sha": "1b27e8a9f4093c3bab113d67eda7893d3f0526ebdb5948c172fb5d3219e0cf46",
 "set_sha": "239fcbe8704da6290c832fea2e2fe537ee58768236de79d74e823f259cb0d377",
 "still": {
  "at": "2026-10-10T08:30:21Z",
  "units": {
   "chainbook": {
    "ActiveState": "active",
    "MainPID": "4064090",
    "NRestarts": "1"
   },
   "recorder": {
    "ActiveState": "active",
    "MainPID": "4148534",
    "NRestarts": "2"
   }
  }
 }
}
{"at":"2026-10-10T08:31:25Z","constants_sha":"1b27e8a9f4093c3bab113d67eda7893d3f0526ebdb5948c172fb5d3219e0cf46","head":"6f045cffc3601b589d3b8b7a6a9af6f73991e18b","member_list_sha":"385c917fd8bf250b43b04aa278a212684b0e3ec52dd804a511aee8ecabd2d8df","members":1079}
{"at":"2026-10-10T08:31:36Z","constants_sha":"1b27e8a9f4093c3bab113d67eda7893d3f0526ebdb5948c172fb5d3219e0cf46","head":"6f045cffc3601b589d3b8b7a6a9af6f73991e18b","member_list_sha":"385c917fd8bf250b43b04aa278a212684b0e3ec52dd804a511aee8ecabd2d8df","members":1079}
```

`logs/39a-separation.log`, verbatim. It ran after the push and the pull request and before the report's commit:

```
$ git fetch origin; contract §4.2 self-check   # 2026-10-10T08:31:53Z
fetch exit=0
$ git rev-list origin/main | grep -c 6f045cffc3601b589d3b8b7a6a9af6f73991e18b
0
$ git diff --name-only origin/main origin/tz-24-nesting-b2
research/tz24-nesting-b2.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
grep exit=1
$ gh pr view 24 --json number,state,headRefOid,baseRefName,url
{"baseRefName":"main","headRefOid":"6f045cffc3601b589d3b8b7a6a9af6f73991e18b","number":24,"state":"OPEN","url":"https://github.com/seahomebatumi-ai/btc-5m-twap/pull/24"}
```

### 2.12 Every file the run wrote, by SHA-256

Under `/root/tz24-work/`, outside the worktree `wt/`, as `logs/40-inventory.log` hashed them at 08:32:45 UTC.
`logs/40-inventory.log` hashed itself while it was being written, so its own line there is the partial file's. The
final SHA-256 of every file under `logs/`, of `state.json` and of `book-ledger.jsonl` is B-RECLAIM-OWN's `R copied` line
for it, in §2.13.

| path under `/root/tz24-work/` | bytes | SHA-256 at 08:32:45 UTC | kept by §9 |
|---|---|---|---|
| `book-ledger.jsonl` | 526 | `8acf7297894dd7a5e8393c935df4aa0cfcced8ef6f976c9bccde7f95fd23d874` | by name |
| `logs/00-pull.log` | 269 | `21c7551d80774bde35d1be6011518b3312372893f55e7c0b5088d276d11c49a6` | by name |
| `logs/00-work-tree.log` | 89 | `6df87d0acf3e7fe1ededd631c74e7e35037e73f8e7e4dc5c051d98c4aa58c95c` | by name |
| `logs/01-stage.log` | 369 | `178c3ea43010edc2eea88a4911a5f19ab01006f1b774ca138f08c9df8f96fd84` | by name |
| `logs/02-fingerprint.log` | 6,584 | `f579b25d78f268efdcb1c1e52377ea39b59ea20fc72dfc857ad889b1187c3b17` | by name |
| `logs/03-host-gate.log` | 1,143 | `d50911897c3c9a7d0963c843c265aa7f94eaf37e17321e8ea0173a4e253e918c` | by name |
| `logs/05-refs.log` | 2,156 | `88ccd75adca7fccd0f8c4f871e407ea5fb94f929603e70a5cd4d19108e7ff0e3` | by name |
| `logs/31-branch.log` | 1,865 | `aa005b3c2d53a8f38e8a7db513dc3d52df517325e933fbfe8a23c24142bdc8cf` | by name |
| `logs/32-selftest.log` | 27,682 | `b5aa1402db2042aaad6fbd8e612dc2ceaf41b422cf4207b7093ba755a574a6dc` | by name |
| `logs/32-selftest.time` | 821 | `659059fe7f2b1a59333cc6b5d62b60306fb0dd89c196a2e9f72698c79be85137` | by name |
| `logs/33b-reclaim-scratch.log` | 1,094 | `f260a4ccea75106620f1c31e4a51660c196ed5ffaffe47e32084cfa485578281` | by name |
| `logs/33-scratch.log` | 1,005 | `f7876a7eb08741cda459f82d1611f15718556a5148fa66496d50c6f3c15e9d7e` | by name |
| `logs/33-scratch-targets.log` | 1,001 | `89940a1c2284a6714ca4e57c9b93ed057fbae065e2f2b6da61291f8453015ed2` | by name |
| `logs/33-still.log` | 674 | `1d4f5808c1aca64ef792862041e77f9b23faa6d0c9fd7140120e317447161879` | by name |
| `logs/34-rehearse.log` | 1,738 | `562d7aa0d511ce82cfef97e523bc9013b572340deb47cc754e986d052cd3dca7` | by name |
| `logs/35-fetch.log` | 884 | `d778fe75185c4ea023d1ce0e2c2974d70dc826d1d1f2f1a548e0b9b1326a0606` | by name |
| `logs/36-constants-1.log` | 9,285 | `8d59c183b9271e70e67343843a3406f5eb059317c837878bcb735411e8530cf7` | by name |
| `logs/36-constants-2.log` | 9,430 | `1148f0f69a96ca805dfd60d5d9be52c4ffd9d91cca5875a9fe1efc6b0d1f8c0c` | by name |
| `logs/37-score-1.log` | 7,710 | `96a1cb22e6e19e49992735bd943692f8fca26c1dc5049ee813ae3ba5ba7bc3b6` | by name |
| `logs/37-score-2.log` | 7,993 | `25addcf9247e5b0b2ef62277db81b22bff54aa5400447d60b1cf03662db470db` | by name |
| `logs/38-still.log` | 710 | `1b28f90a11e9c582052aaddbf100aff62c921a38942ce7880f88b8cc00cc2a9f` | by name |
| `logs/39a-separation.log` | 565 | `af4cb22a766bb5a8241bca0b79fb0b3c91628ff3cde89c2f8a723b00ec7c5b61` | by name |
| `logs/39-closing.log` | 2,468 | `d881194fddf7d4dd9c1e9a24c3d9890bb71f5d882eeea109805980014aac56a8` | by name |
| `logs/40-inventory.log` | 2,214 | `442f42ad3df5757670def913212c6af3112592d433b324430f3b283d3852ced5` — partial: hashed while being written, see §2.13 | by name |
| `rehearsal/set.json` | 141,120 | `4635cb07fce5f998da23cca5bc376160f704df2e1772e542ba8d52883dd6320a` | named by this report |
| `set/set.json` | 763,850 | `239fcbe8704da6290c832fea2e2fe537ee58768236de79d74e823f259cb0d377` | named by this report |
| `set/tz24-constants.json` | 3,443 | `1b27e8a9f4093c3bab113d67eda7893d3f0526ebdb5948c172fb5d3219e0cf46` | named by this report |
| `set/tz24-reading.json` | 3,944 | `c03c642eb687c4dcd7125a62186143c42d76fee6698306ec33712c1427eac621` | named by this report |
| `set/tz24-units.csv` | 964,508 | `1c77a6323c38996a234aa47af430f1a6d42555a8e94881d49ba9a92e11e6eafe` | named by this report |
| `stage/research/tz24-nesting-b2.py` | 76,142 | `4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b` | named by this report |
| `state.json` | 473 | `600b4dca1242eaef5e488a6cbebfa1b3e54e3ef4d70ff3f94f250a68593e06af` | by name |

**The two document caches**, kept by name and not hashed here: `set/docs/`, **108** files, **1,027,354** bytes; and
`rehearsal/docs/`, **20** files, **188,098** bytes. Each file is one gamma response, gzip, verbatim as served, named by
its first slug.

**The worktree** `/root/tz24-work/wt` held exactly its pushed `HEAD`, `6f045cf`: `git status --porcelain --ignored`
printed nothing, and `HEAD` equals its upstream. The one file the run added to it is `research/tz24-nesting-b2.py`,
SHA-256 `4e4022e6…`, committed.

**Written after 08:32:45 UTC**, in `logs/`: `41-input-hashes.log`, `00c-model.log`, `42-checks.log`,
`43-report-fill.log` and `44-report-check.log`. Their hashes are B-RECLAIM-OWN's. `00c-model.log` was written by hand
from the `get_session` tool's return, because that tool is not a shell command.

### 2.13 §9 B-RECLAIM-OWN — last, after §3.9, with this report drafted

B-RECLAIM-OWN ran as four commands of the Executor, none refused, each beginning with `date -u +%FT%TZ` (§6 item 9).
Its output was written to no file, as §9 orders, and is quoted here from the session. The 164 `R copied` lines were set
into this report from the forensic store after the run: each line's SHA-256 is the stored copy's, and the order is
`reclaim`'s own walk. The Executor compared them with the session's output.

```
$ cd /root/tz24-work && date -u +%FT%TZ && I reclaim /root/tz24-work; echo "exit=$?"
2026-10-10T08:39:25Z
[2026-10-10T08:39:25Z] reclaim: 1859 report tokens; forensic store holds 1561 files
[2026-10-10T08:39:25Z] reclaim: /root/tz24-work/wt skipped: no file but its HEAD's, and HEAD 6f045cffc3601b589d3b8b7a6a9af6f73991e18b is its upstream's
[2026-10-10T08:39:25Z] R copied 8acf7297894dd7a5e8393c935df4aa0cfcced8ef6f976c9bccde7f95fd23d874 /root/btc-forensics/tz24-work--book-ledger.jsonl
[2026-10-10T08:39:25Z] R copied 600b4dca1242eaef5e488a6cbebfa1b3e54e3ef4d70ff3f94f250a68593e06af /root/btc-forensics/tz24-work--state.json
[2026-10-10T08:39:25Z] R copied 21c7551d80774bde35d1be6011518b3312372893f55e7c0b5088d276d11c49a6 /root/btc-forensics/tz24-work--logs--00-pull.log
[2026-10-10T08:39:25Z] R copied 6df87d0acf3e7fe1ededd631c74e7e35037e73f8e7e4dc5c051d98c4aa58c95c /root/btc-forensics/tz24-work--logs--00-work-tree.log
[2026-10-10T08:39:25Z] R copied 55c815ee694f1d6971f2427194a5788ac0c7a896c9b2f500d899dd7d1097bafb /root/btc-forensics/tz24-work--logs--00c-model.log
[2026-10-10T08:39:25Z] R copied 178c3ea43010edc2eea88a4911a5f19ab01006f1b774ca138f08c9df8f96fd84 /root/btc-forensics/tz24-work--logs--01-stage.log
[2026-10-10T08:39:25Z] R copied f579b25d78f268efdcb1c1e52377ea39b59ea20fc72dfc857ad889b1187c3b17 /root/btc-forensics/tz24-work--logs--02-fingerprint.log
[2026-10-10T08:39:25Z] R copied d50911897c3c9a7d0963c843c265aa7f94eaf37e17321e8ea0173a4e253e918c /root/btc-forensics/tz24-work--logs--03-host-gate.log
[2026-10-10T08:39:25Z] R copied 88ccd75adca7fccd0f8c4f871e407ea5fb94f929603e70a5cd4d19108e7ff0e3 /root/btc-forensics/tz24-work--logs--05-refs.log
[2026-10-10T08:39:25Z] R copied aa005b3c2d53a8f38e8a7db513dc3d52df517325e933fbfe8a23c24142bdc8cf /root/btc-forensics/tz24-work--logs--31-branch.log
[2026-10-10T08:39:25Z] R copied b5aa1402db2042aaad6fbd8e612dc2ceaf41b422cf4207b7093ba755a574a6dc /root/btc-forensics/tz24-work--logs--32-selftest.log
[2026-10-10T08:39:25Z] R copied 659059fe7f2b1a59333cc6b5d62b60306fb0dd89c196a2e9f72698c79be85137 /root/btc-forensics/tz24-work--logs--32-selftest.time
[2026-10-10T08:39:25Z] R copied 89940a1c2284a6714ca4e57c9b93ed057fbae065e2f2b6da61291f8453015ed2 /root/btc-forensics/tz24-work--logs--33-scratch-targets.log
[2026-10-10T08:39:25Z] R copied f7876a7eb08741cda459f82d1611f15718556a5148fa66496d50c6f3c15e9d7e /root/btc-forensics/tz24-work--logs--33-scratch.log
[2026-10-10T08:39:25Z] R copied 1d4f5808c1aca64ef792862041e77f9b23faa6d0c9fd7140120e317447161879 /root/btc-forensics/tz24-work--logs--33-still.log
[2026-10-10T08:39:25Z] R copied f260a4ccea75106620f1c31e4a51660c196ed5ffaffe47e32084cfa485578281 /root/btc-forensics/tz24-work--logs--33b-reclaim-scratch.log
[2026-10-10T08:39:25Z] R copied 562d7aa0d511ce82cfef97e523bc9013b572340deb47cc754e986d052cd3dca7 /root/btc-forensics/tz24-work--logs--34-rehearse.log
[2026-10-10T08:39:25Z] R copied d778fe75185c4ea023d1ce0e2c2974d70dc826d1d1f2f1a548e0b9b1326a0606 /root/btc-forensics/tz24-work--logs--35-fetch.log
[2026-10-10T08:39:25Z] R copied 8d59c183b9271e70e67343843a3406f5eb059317c837878bcb735411e8530cf7 /root/btc-forensics/tz24-work--logs--36-constants-1.log
[2026-10-10T08:39:25Z] R copied 1148f0f69a96ca805dfd60d5d9be52c4ffd9d91cca5875a9fe1efc6b0d1f8c0c /root/btc-forensics/tz24-work--logs--36-constants-2.log
[2026-10-10T08:39:25Z] R copied 96a1cb22e6e19e49992735bd943692f8fca26c1dc5049ee813ae3ba5ba7bc3b6 /root/btc-forensics/tz24-work--logs--37-score-1.log
[2026-10-10T08:39:25Z] R copied 25addcf9247e5b0b2ef62277db81b22bff54aa5400447d60b1cf03662db470db /root/btc-forensics/tz24-work--logs--37-score-2.log
[2026-10-10T08:39:25Z] R copied 1b28f90a11e9c582052aaddbf100aff62c921a38942ce7880f88b8cc00cc2a9f /root/btc-forensics/tz24-work--logs--38-still.log
[2026-10-10T08:39:25Z] R copied d881194fddf7d4dd9c1e9a24c3d9890bb71f5d882eeea109805980014aac56a8 /root/btc-forensics/tz24-work--logs--39-closing.log
[2026-10-10T08:39:25Z] R copied af4cb22a766bb5a8241bca0b79fb0b3c91628ff3cde89c2f8a723b00ec7c5b61 /root/btc-forensics/tz24-work--logs--39a-separation.log
[2026-10-10T08:39:25Z] R copied 9beaca0494a1efedf4694921a8bad6b7a2b4ba1316897335c5f7986956ca65bf /root/btc-forensics/tz24-work--logs--40-inventory.log
[2026-10-10T08:39:25Z] R copied 4a7c83e239303e95b109a27c280cc8665a6109e1dd8f7640bb5146d8ba06ceac /root/btc-forensics/tz24-work--logs--41-input-hashes.log
[2026-10-10T08:39:25Z] R copied 9e2ce4bdc6954748efc4353086fcd7c3a7556bcced57fe061599ce0394bcc0f0 /root/btc-forensics/tz24-work--logs--42-checks.log
[2026-10-10T08:39:25Z] R copied 085ea5bb6470355955c5d157c8ba6ece9b4daf59e33a457be155179877589669 /root/btc-forensics/tz24-work--logs--43-report-fill.log
[2026-10-10T08:39:25Z] R copied e29c8b830ad530e641d55ab094136ea0769317fc5a67611a6b01df56df40c66c /root/btc-forensics/tz24-work--logs--44-report-check.log
[2026-10-10T08:39:25Z] R copied 4635cb07fce5f998da23cca5bc376160f704df2e1772e542ba8d52883dd6320a /root/btc-forensics/tz24-work--rehearsal--set.json
[2026-10-10T08:39:25Z] R copied 0a7a32b14382eb91baddbc0400b8a544f736fdbf93377fd36c6d0fa8389f23ef /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1788998400.json.gz
[2026-10-10T08:39:25Z] R copied ce410c276e065aeaf564a2c0aa1e5047a3691c4c3455b77b8cb5206db3490b35 /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789007400.json.gz
[2026-10-10T08:39:25Z] R copied 7fe5c8028a154a7599f33e90101b466d0d66da8e76a5f2845ffea0977f9a9a39 /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789016400.json.gz
[2026-10-10T08:39:25Z] R copied b27a1d0584bfbaa45a346583ed38cc522d240a613d9d015b89b42b0480b44876 /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789025400.json.gz
[2026-10-10T08:39:25Z] R copied 6ec1ca1e701de16dcaa298229044e2a24ce225f412cce7f28ba8a7572b30ecaa /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789034400.json.gz
[2026-10-10T08:39:25Z] R copied 39537d4848cd61b31ff10ea1e429afcd9ecc3d342cf27071119e22318acb4238 /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789043400.json.gz
[2026-10-10T08:39:25Z] R copied 4d7427781bc332b462a947aecbc3b64cd72f0bfd08e777bdda6a8b92f311bc2f /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789052400.json.gz
[2026-10-10T08:39:25Z] R copied 26007d1f660c0f1dec4ce9f9acf8f25ee804321aba9b547fe36b6f66371047e9 /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789061400.json.gz
[2026-10-10T08:39:25Z] R copied 44fae476b0b91ba7990a6dcd2414d374ede0dfa2e275139681a0c804bb72cda7 /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789070400.json.gz
[2026-10-10T08:39:25Z] R copied 82138da15c79a21ba212b33b1125fd1ed381a52e89529fb09d3ca58ea0674018 /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789079400.json.gz
[2026-10-10T08:39:25Z] R copied 319a41c175d70559b60b40fb2ab96ddff6665a99117b715e4a0fd245622272c7 /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789088400.json.gz
[2026-10-10T08:39:25Z] R copied 78f0abce6e60588bed7332b2fa47898ecec8a3bf68185f7e5b574546917656f6 /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789097400.json.gz
[2026-10-10T08:39:25Z] R copied ce223699a213b7cc9dbdd0e3281b31a465ebe18df4d4e5929536978f180f972f /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789106400.json.gz
[2026-10-10T08:39:25Z] R copied 682f4a1034b65b302a27d32a670526fe12d577e2411b2c6e878e683e36eb1a42 /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789115400.json.gz
[2026-10-10T08:39:25Z] R copied e37112855e8ac9275be3fe63ccbdc92fb6884a604a242476e098b9e9a35e1eef /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789124400.json.gz
[2026-10-10T08:39:25Z] R copied 182fd85d718b6cd3a559cf7e4dd43674a45d353db2bac43d9fad246ccdce0692 /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789133400.json.gz
[2026-10-10T08:39:25Z] R copied 457c0e159e615c314aa166d0c8a5c9faef87dfb224cc6e4452eca35afff41a0e /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789142400.json.gz
[2026-10-10T08:39:25Z] R copied d5d5e7b0810f6e0d1a6df229eb2f4ce325d80bc1cc7bd85a95b10babcbaa52ea /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789151400.json.gz
[2026-10-10T08:39:25Z] R copied c16c4ebd0e0c56c85386278a6168a42b6c5157110f309e06559c8feef50d6273 /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789160400.json.gz
[2026-10-10T08:39:25Z] R copied 44b36f65d2640430cdd97d67c3f4a72a9cf236a25d5fb20b5854832dcfe2e7a4 /root/btc-forensics/tz24-work--rehearsal--docs--btc-updown-15m-1789169400.json.gz
[2026-10-10T08:39:25Z] R copied 239fcbe8704da6290c832fea2e2fe537ee58768236de79d74e823f259cb0d377 /root/btc-forensics/tz24-work--set--set.json
[2026-10-10T08:39:25Z] R copied 1b27e8a9f4093c3bab113d67eda7893d3f0526ebdb5948c172fb5d3219e0cf46 /root/btc-forensics/tz24-work--set--tz24-constants.json
[2026-10-10T08:39:25Z] R copied c03c642eb687c4dcd7125a62186143c42d76fee6698306ec33712c1427eac621 /root/btc-forensics/tz24-work--set--tz24-reading.json
[2026-10-10T08:39:25Z] R copied 1c77a6323c38996a234aa47af430f1a6d42555a8e94881d49ba9a92e11e6eafe /root/btc-forensics/tz24-work--set--tz24-units.csv
[2026-10-10T08:39:25Z] R copied 8b469625b42f65ba45558261ce5a7cd14725bf7d9788230d598d3eab741b6eb4 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790184600.json.gz
[2026-10-10T08:39:25Z] R copied 0ef4461fd1a71c501ecbd9b00782250e20be88c1aee6a04bffc0d2742cbf2690 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790194500.json.gz
[2026-10-10T08:39:25Z] R copied 7c889e0d3c69f5227e7426bb35fc222ca3f511eb1e63f98698f1fd2bb33c8f2c /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790203500.json.gz
[2026-10-10T08:39:25Z] R copied cf92947fd43ea022862a5e6b45cf99078dd7f6c6103eb1f1024447ce21a42cae /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790212500.json.gz
[2026-10-10T08:39:25Z] R copied 688978de9ecb0b29c2a40aef6e68ad03901610bb90acad079bb0b232dbcd0329 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790221500.json.gz
[2026-10-10T08:39:25Z] R copied d63644b09e9dc6bf2f32f9d5215274fde60efdf71b2a1b9a33c73bb716793451 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790230500.json.gz
[2026-10-10T08:39:25Z] R copied aa7fad54cb45d00db07a01c12f7567f61490b924947e8166da9c0cbbb7ad97ee /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790239500.json.gz
[2026-10-10T08:39:25Z] R copied a8fe67db66837b4aa3eab36a40f1d8ce50f259a50a714fd1972532b460a82c75 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790248500.json.gz
[2026-10-10T08:39:25Z] R copied 0e9584999eb48fb04b1ffd9dcaf140eb97081ea53318d456ba621c77883a77fb /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790257500.json.gz
[2026-10-10T08:39:25Z] R copied b66beec2bb516711068452c2bc85aa206683d6bc4fe308c41ffbae3605175b27 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790266500.json.gz
[2026-10-10T08:39:25Z] R copied 4f5a0c1b6fd53e95f33e2c5fc78208ab2de5d27882486de5c183e17ce1fe061f /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790275500.json.gz
[2026-10-10T08:39:25Z] R copied 90a66c3e3448205688e85171410332fb0bfd3a01948bcde32d06421cc77dad46 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790284500.json.gz
[2026-10-10T08:39:25Z] R copied b49522ff0c1b5aabcf2a729bb3c532c8123e1b39a5a8c22ce333f777a1aa2ba5 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790293500.json.gz
[2026-10-10T08:39:25Z] R copied 680a414471428ff3bbe3c8e1c53ef9212201e1ebfbeb63f1ab5cb83f2a3bad49 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790302500.json.gz
[2026-10-10T08:39:25Z] R copied e0eab075dba232ea397b4705715f2cdd7042786325ac4639949b0ffc2bf529af /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790311500.json.gz
[2026-10-10T08:39:25Z] R copied 610a3bdbe65ccaa4340c799ca974e3ec718f96bffee60ee4b6fd4df69cf03c68 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790320500.json.gz
[2026-10-10T08:39:25Z] R copied 1619b217deb26093b3e2f5f8f2827f5aa731901acd789b7409afc773db53649f /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790330400.json.gz
[2026-10-10T08:39:25Z] R copied a58470829d3e7351b480f9f70ed541dd180f66c824a3c3465e28e376e5ae475f /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790339400.json.gz
[2026-10-10T08:39:25Z] R copied 0f8c439ad669bb5e901ec1ba6f72859b4c64f3dc002e9b4107e530d99b3771fe /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790348400.json.gz
[2026-10-10T08:39:25Z] R copied fff4e78035b0d2c795412e341edbb175969647d2832ed6f2b63dc9a90263f77a /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790357400.json.gz
[2026-10-10T08:39:25Z] R copied 410834b9a251bb25cd387c6dd2a4d17143e11e343524bb1707dc41d263154698 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790366400.json.gz
[2026-10-10T08:39:26Z] R copied 25641d13085d8c2ad8871929f5377ccaf6c97bfa4491523d0f610dc426a72962 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790375400.json.gz
[2026-10-10T08:39:26Z] R copied e5e623f38ad54a2df6e8d7e568342eb8d26ad74ff51c38ac9f8333c8803bc640 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790384400.json.gz
[2026-10-10T08:39:26Z] R copied c0aaa954b4b2822ce36e2056d09a004ee77755ac18090a531422368d31e67c10 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790393400.json.gz
[2026-10-10T08:39:26Z] R copied d6de28d9719337977b6cb80e3871a11bcaa153b2987be1335b56315b718e95e5 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790402400.json.gz
[2026-10-10T08:39:26Z] R copied fdde58a2367e7337541d2c965fd4694533d1103c3140e0f9f5f73777f5446860 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790411400.json.gz
[2026-10-10T08:39:26Z] R copied 8f9f90ad808f68b0f0bc9318b042230a3084d259e128351d469b679d78204c13 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790420400.json.gz
[2026-10-10T08:39:26Z] R copied 7e3633fff138701711fa04c6a35001090d4d15c0a4bd11d7aa20097af5293943 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790429400.json.gz
[2026-10-10T08:39:26Z] R copied 1e868e8d89e850820370c700c37e298d1b159e0fb1cbd19b78444a8d6d867852 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790438400.json.gz
[2026-10-10T08:39:26Z] R copied 7bf0c92148e3893a44a13d8aef7cd286daf6d57a895643cf5f17073b425e6b7a /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790447400.json.gz
[2026-10-10T08:39:26Z] R copied 543e102906e0e0937575987dccfc44c4bf946534fe7c366b764a1d807cee6a15 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790456400.json.gz
[2026-10-10T08:39:26Z] R copied c9211bd88a39f5ebbe2b1c02ca4f2f735025b1df6d95655208a300bd4beac206 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790465400.json.gz
[2026-10-10T08:39:26Z] R copied 3d65be25d96e4bf983924cb9e8d765cf2ebe03d58d0cde7698d836fe2738a7c2 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790474400.json.gz
[2026-10-10T08:39:26Z] R copied 58caf209ac23e04beb47d5ae23fe331934a37325425857dc94f81115578a86f1 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790483400.json.gz
[2026-10-10T08:39:26Z] R copied f0422965cc59b5beb93315a4ca17f16c9ba55f8e2c6299efebca4210b125df99 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790492400.json.gz
[2026-10-10T08:39:26Z] R copied 97e225f9bc57ff5dc7a862155d56da87deafd8761e38d9be0c3e8a8e5908edb8 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790501400.json.gz
[2026-10-10T08:39:26Z] R copied e610c308ae5d96f6107e85ae4a63f48996fad45317d0f3f66775ee54e2fc47a7 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790510400.json.gz
[2026-10-10T08:39:26Z] R copied 4729d624d2de2ebb655593909f3f9eec90a0c502cd202b0191b457297c9f635f /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790519400.json.gz
[2026-10-10T08:39:26Z] R copied 71b7ea0f798a05bb7aec7f792ba7faef6eedaf1263353a4ad62dcc5c1d9716f0 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790528400.json.gz
[2026-10-10T08:39:26Z] R copied ea1197f599191da69af6c414eeaec5689ccce3627ceafa47e3e25271035fc235 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790537400.json.gz
[2026-10-10T08:39:26Z] R copied ba279b0abbccef14212097bc3c3b2fda8e5cf7e04c79509e5f193e8c9684b854 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790546400.json.gz
[2026-10-10T08:39:26Z] R copied 09462205de79676a6d6c4c4a2e6c3a212b13349527c84b7db947d87ce566fdc2 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790556300.json.gz
[2026-10-10T08:39:26Z] R copied b0b57dc4960a43c62dc5f80d4197a2c5d1bce8c32df54c708480fbb68ca8f96d /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790565300.json.gz
[2026-10-10T08:39:26Z] R copied 9351770459b44786aeba9d9c0d57c755fa78ea291139b15d21f7635d5756a50c /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790574300.json.gz
[2026-10-10T08:39:26Z] R copied dcb05d6318460209f45f624e7469f5f0a530bd7b76acc5f219f54f16338aeaf5 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790583300.json.gz
[2026-10-10T08:39:26Z] R copied 47910bc1ef84b84caea12b0c4e47041285efd49a4b644a91778d891cc66d6dc9 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790592300.json.gz
[2026-10-10T08:39:26Z] R copied 685eefe75c61c4a132ca66594fed4ba8de3587690c81e03ac0487f5ac73190b5 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790601300.json.gz
[2026-10-10T08:39:26Z] R copied 58a4b757be15dc86ec54a0904ff12029cbd00148cefd0e5583c41b7f0a21abdc /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790610300.json.gz
[2026-10-10T08:39:26Z] R copied 0e0c84e76b957572d63b303f8a13cc6461ef3dacd4164d2f1972b19b427729c6 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790619300.json.gz
[2026-10-10T08:39:26Z] R copied 164da0aa9eda4b48c167eee5ba631fd0ec39e102df65b50e2926352e0732ec4b /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790628300.json.gz
[2026-10-10T08:39:26Z] R copied 58147833592f3ae087dcaf45382b1010e689ee645cbb8ca3a9dd9cb0eb1f8eae /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790637300.json.gz
[2026-10-10T08:39:26Z] R copied 58e1947e4ae48c1f2ac63c4640eb51ac34214079418ade7e48f18d65174091b8 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790646300.json.gz
[2026-10-10T08:39:26Z] R copied a61b2cc2b6faa2fe2fd7af515161fec26058d19c539cf461a8d8226cb8f5c8d1 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790655300.json.gz
[2026-10-10T08:39:26Z] R copied a552af616f476d9c3a8ca4c78b35f27512aeb1b0289f6b4d29d3d69d5e6be6da /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790664300.json.gz
[2026-10-10T08:39:26Z] R copied 0758e227a4419959302ba391dcd53b96f81da5137594be74e6c58c0d50cd1891 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790673300.json.gz
[2026-10-10T08:39:26Z] R copied f8a4b755301d155cdc7f38bac0bee24f6d8a8cff5fc84795a1022f99099a2306 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790682300.json.gz
[2026-10-10T08:39:26Z] R copied 30486446463ac625ab7be4fc1ab058a7b9935cebf3dcae8b1810c231b941b4d1 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790691300.json.gz
[2026-10-10T08:39:26Z] R copied 58ccd99c324d6fbc5472626d7f0fcd6bb646b5909b02bf726c0172a046618e95 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790700300.json.gz
[2026-10-10T08:39:26Z] R copied 69ff231ccf6d43caf3ca3c0df62d1220e1d5309c4f2c4c85faa207bf1b54d802 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790709300.json.gz
[2026-10-10T08:39:26Z] R copied 72240e35b3c65642a01ce8e7db44220f8b6650a5f6aae5b5f3b3a43483c6c26b /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790718300.json.gz
[2026-10-10T08:39:26Z] R copied 2da958223b3c7b136e8c227b9206c5d799c8d61e4f1281a0e1bf5c027de8cc8f /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790727300.json.gz
[2026-10-10T08:39:26Z] R copied db0fed65b840a45b842a3dfeae684220f7598909b8548930662343fcc5193f1d /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790736300.json.gz
[2026-10-10T08:39:26Z] R copied cfc85fbbfcf79d0609d879e449904882741b6de68993d19e643a538e487cde39 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790745300.json.gz
[2026-10-10T08:39:26Z] R copied 835b596090de3c856d2ab7e53e5a45770390a537cbf88393e517fc916dc7e4fd /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790754300.json.gz
[2026-10-10T08:39:26Z] R copied f35a395b7068450f7fea5103e39348451486dfc4fd1da7207117dfbb6a99490b /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790763300.json.gz
[2026-10-10T08:39:26Z] R copied cf30422f63f72eb8322bf57743183a6fa068dc4b3da5a14f88ac78d62d66ded1 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790772300.json.gz
[2026-10-10T08:39:26Z] R copied 6c88f1b7f29925740fa97221e0f0d611cf9dd707ae716c43688a9499e783faa9 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790781300.json.gz
[2026-10-10T08:39:26Z] R copied ca359b8951c79e1d2df865c719d19b334d2c155090a5d412893192a3c37448d4 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790790300.json.gz
[2026-10-10T08:39:26Z] R copied c53ebb3f34239e8efc3cc50a98aa667594bbe5dbffc1f90e264e43778dec5be4 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790799300.json.gz
[2026-10-10T08:39:26Z] R copied 6b9ec3542fce212a7fa00c8262acce53b919bc9284e235065ec66b9e677eff95 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790808300.json.gz
[2026-10-10T08:39:26Z] R copied ca0419be39d6efb757a63410af14606b8b1c0c5302a387000b4f5ca98a49d9e5 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790817300.json.gz
[2026-10-10T08:39:26Z] R copied 3af14f71ee5f7c18c5636d8eabb091f9785f6d669e250904d85b29bd579c699a /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790827200.json.gz
[2026-10-10T08:39:26Z] R copied 17cfa342023b172fdffbeb5079e6a7be720bde9ca6f6251cab58ed347af780ce /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790837100.json.gz
[2026-10-10T08:39:26Z] R copied 0a1dc7f8395792a9c440271f3c3891716a62f81a39a9fdf9ba0797765b09b86a /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790846100.json.gz
[2026-10-10T08:39:26Z] R copied a716713736436c94c474ec5a7313f8fab8735290aa49fcb0462557930bfa24aa /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790855100.json.gz
[2026-10-10T08:39:26Z] R copied 9332a5d048fefc0f7375860ba3a513da6b7a1252f719b796f7073d95f75d14db /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790864100.json.gz
[2026-10-10T08:39:26Z] R copied 909e4a387d74c51cdadaf7463c93275cab24abf6207375b29cf06d210222d6dd /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790873100.json.gz
[2026-10-10T08:39:26Z] R copied b15cb40efdfe12a19d768007a444e2e37ac7f59386297fea53a3f74127b14501 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790882100.json.gz
[2026-10-10T08:39:26Z] R copied 7be9b3b71a1118d9140e1943257eab41fd75ea18ad342b0fa71b3f6a04829030 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790891100.json.gz
[2026-10-10T08:39:26Z] R copied 7eefe1cc2382a1914745f8a656e06f443d1eab8c4fb7b29fe1bac1cdde5d7d3e /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790900100.json.gz
[2026-10-10T08:39:26Z] R copied 1b4ff9fd56982e130e7ac31983eb5ebe3a82eefd6eb10640e04bed2ec204e28f /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790909100.json.gz
[2026-10-10T08:39:26Z] R copied 201c5346003401ad6a4631408733cbee1ab68ada40d7752536bef82a262e8372 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790918100.json.gz
[2026-10-10T08:39:26Z] R copied 8b694f29a299df4f7b35dce72b3826a89102320775a21a2c4a5017a3eaeadb5d /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790927100.json.gz
[2026-10-10T08:39:26Z] R copied c98e61d2d62255d65d887250966ff7a60c0a2aaf00a7ae5a4af9beb514060dcb /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790936100.json.gz
[2026-10-10T08:39:26Z] R copied f4a8f71b777a3933c4c136fe24d4c6521149f20d7b2efd6dd799bb62786ce521 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790945100.json.gz
[2026-10-10T08:39:26Z] R copied 7c9d0baacecacb3d301998b8186d7dbd3c075fd8e5e7e429f22dad716137fd94 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790954100.json.gz
[2026-10-10T08:39:26Z] R copied 5a34fb434731216974f854a76974d212fdd0a95b501521468f919246bb08820e /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790963100.json.gz
[2026-10-10T08:39:26Z] R copied eb76915c97e8cfb0764825fb306ce702b6faa20c706f490833a520656a807af0 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790972100.json.gz
[2026-10-10T08:39:26Z] R copied ab1d265bde90493f2f82feec276bc3a8001b7b769253f42a040060dcaf7d4538 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790981100.json.gz
[2026-10-10T08:39:26Z] R copied d9ffaec6d471d14905966c6897dda86fad2330e8bd1423d773c0f51ad31f9395 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790990100.json.gz
[2026-10-10T08:39:26Z] R copied 16b97d7920d5e865505407e110709d45bc4f503c4408eb0e44d4239c73ae729f /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1790999100.json.gz
[2026-10-10T08:39:26Z] R copied b267733af2c5caf53f645b1c12fba0dad964ecea82e967ee61761e868c3c5688 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791008100.json.gz
[2026-10-10T08:39:26Z] R copied 5791270578a8398f0a62550e8ce97e03e84f8f3cfd676102de4e5189b746f501 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791099000.json.gz
[2026-10-10T08:39:26Z] R copied 0f90016e66f43099565ae1c17bb03847fe21fb8a550576a9664603802f9861de /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791108000.json.gz
[2026-10-10T08:39:26Z] R copied 98edf87a284d6884cde5aa542b89136f9b881a200f8791fcceb731100346d192 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791117000.json.gz
[2026-10-10T08:39:26Z] R copied 3f42f8e72c51f85a9df33512672f57774a7e60537bca1c7307cf1d4b8d2751f2 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791126000.json.gz
[2026-10-10T08:39:26Z] R copied f8db87653e4a9af05ec4643737bb7233bae2ebb3ec3b056b68a4ffe9bb90c581 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791135000.json.gz
[2026-10-10T08:39:26Z] R copied 6eac89baf5c8dbe6050e12113bdb3309a90f3402c7625b011e5fd40f39772c6e /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791144000.json.gz
[2026-10-10T08:39:26Z] R copied eb9831182699e9b66624d9b2a13fb6dfde55fcda5e01c6fc33d4029f1756323c /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791153000.json.gz
[2026-10-10T08:39:26Z] R copied e8d3e110446ad5ec81758e732a3f13a2f33880b0010a1b10fde0d3c388e8813c /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791162000.json.gz
[2026-10-10T08:39:26Z] R copied b61dc2d57b99680f7deba16a887723f5bff89ce915b3e0a9bbb87bc44eb63cab /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791171000.json.gz
[2026-10-10T08:39:26Z] R copied 84241e669d18e6fa99e31e39fe7db59b856a91ac01047f7acade9aaa6da21d6c /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791180000.json.gz
[2026-10-10T08:39:26Z] R copied 7e880d8de4b0dcdd1e94f8f1a1f0ba956228d3b8e13b767795873e55e409b0ce /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791189000.json.gz
[2026-10-10T08:39:26Z] R copied e91aa65c2e9c4b30ba6137f3553307210041ce9c02a067e085b94d6e5c1dbe06 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791198000.json.gz
[2026-10-10T08:39:26Z] R copied b6a3d0b7c883de49cdaffe140ab820d831310620eeeba8962f6720c29262f94c /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791207000.json.gz
[2026-10-10T08:39:26Z] R copied 90c77e3ea35ca27f5a36de8583d728461201e9c0f6405cd2200285e921c5dba8 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791216000.json.gz
[2026-10-10T08:39:26Z] R copied e6cb91adaedae7353b57bb1c4ba55353303107fb001dd1bd8e7b4e742d46d184 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791225000.json.gz
[2026-10-10T08:39:26Z] R copied 656315b19a23a96601b6ef19f74235cbf463d18d406d46a3ee9a53516ebbca77 /root/btc-forensics/tz24-work--set--docs--btc-updown-15m-1791234000.json.gz
[2026-10-10T08:39:26Z] R copied 4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b /root/btc-forensics/tz24-work--stage--research--tz24-nesting-b2.py
[2026-10-10T08:39:26Z] RECLAIM PASS: 164 files considered, 30 named by a report, 134 kept by name, 164 copied, 0 already held; forensic store 1561 -> 1725 files
[2026-10-10T08:39:26Z] malloc tuned: True
[2026-10-10T08:39:26Z] peak memory of this run: 28540928 bytes
[2026-10-10T08:39:26Z] opens refused under the capture roots: 0; chain book opens: window.json 0, books.jsonl.gz 0; tz14's record of opens under the recorder's root: not loaded
exit=0
```

```
$ date -u +%FT%TZ; git -C /root/btc-5m-twap worktree remove /root/tz24-work/wt; echo "exit=$?"
2026-10-10T08:39:31Z
exit=0
```

```
$ date -u +%FT%TZ; rm -rf /root/tz24-work; echo "exit=$?"
2026-10-10T08:39:33Z
exit=0
```

```
$ date -u +%FT%TZ; test -e /root/tz24-work; echo "exit=$?"; git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list; find /root/btc-forensics -type f | wc -l; df -B1 --output=source,size,avail /var/lib/btc-recorder; grep MemAvailable /proc/meminfo
2026-10-10T08:39:36Z
exit=1
/root/btc-5m-twap       6108e4f [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
1725
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13002625024
MemAvailable:     288364 kB
```

**`RECLAIM PASS`.** It considered 164 files: 30 named by a report, 134 kept by name, 164 copied, 0 already held. The
store went from 1,561 to **1,725** files, `1,561 + 164`, and `reclaim` asserts that equality. The 134 kept by name are
the 128 documents of the two caches and the six files under `logs/` whose hashes no report printed:
`00c-model.log`, `40-inventory.log` in its final form, `41-input-hashes.log`, `42-checks.log`, `43-report-fill.log`
and `44-report-check.log`. The 30 named are the six outputs of §2.12 and 24 files whose hashes this draft printed:
22 logs, `state.json` and `book-ledger.jsonl`. The worktree was skipped as pristine: it held only its `HEAD`
`6f045cf`, its upstream's. `git worktree remove` ran without `--force`, `exit=0`. `rm -rf /root/tz24-work` printed
`exit=0`, and `test -e` printed `exit=1`. Two worktrees remain, the primary checkout and `/root/btc-recorder-svc`. The
branch `tz-24-nesting-b2` stays on `origin` and as a local ref.

---

## 3. Publication

| step | result |
|---|---|
| branch | `tz-24-nesting-b2`, pushed to `origin` at `6f045cffc3601b589d3b8b7a6a9af6f73991e18b`, one commit above `origin/main` `6108e4f` |
| implementation commit | `6f045cf` — `research/tz24-nesting-b2.py`, 1,535 lines, 76,142 bytes, SHA-256 `4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b`; no other path |
| pull request | #24, https://github.com/seahomebatumi-ai/btc-5m-twap/pull/24, base `main`, head `6f045cf`, **open, not merged** |
| Release | none: this TZ creates no Release, and no dataset, archive or binary enters git history |
| report | `CryptoReports/TZ-24-nesting-b2-report.md`, straight to `main` in one commit, the one path pushed to `main` |

**Contract §4.2's separation self-check**, verbatim from `logs/39a-separation.log`:

```
$ git rev-list origin/main | grep -c 6f045cffc3601b589d3b8b7a6a9af6f73991e18b
0
$ git diff --name-only origin/main origin/tz-24-nesting-b2
research/tz24-nesting-b2.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
grep exit=1
```

The first line prints `0`: the implementation is not on `main`. The second names the implementation file alone. The
third prints nothing.

---

## 4. Gate

**B2's reading, TZ-24 §4.3, quoted:**

| condition | reading |
|---|---|
| `V_firm >= 1` | **VIOLATION** — whatever `N` |
| `V_any = 0` and `N_clean >= 528` | **NONE** |
| otherwise | **UNDECIDABLE** |

**The deciding number: `V_firm` = 7**, a count, at least `1`. **VIOLATION.** Under the containment, the fee and the
touch, a firm row's false-reading probability is `0` (§1). `V_any` = 9 and `N_clean` = 1,079 are printed, and NONE's
condition does not hold.

| gate | PASS, or the reading | result |
|---|---|---|
| **G-REHEARSAL** | §4.1's 10 figures equal, exactly | **PASS**, 10 of 10 |
| **G-SET** | every window a status; the members in order; `set.json`'s SHA-256 in `state.json` | **PASS**, 1,175 considered, 1,079 members |
| **B2** | §4.3 | **VIOLATION** — `V_firm` 7 |
| **G-STILL** | `MainPID`, `NRestarts` and `ActiveState` unchanged from §3.3 to §3.8 | **PASS** |

Nothing was tuned to reach the reading, and no gate was reinterpreted.

---

## 5. Validation

| # | check | count | asserted? |
|---|---|---|---|
| **V1** | §0.2's fingerprint | `FINGERPRINT PASS`: revision `2026-10-10-a`; anchors 6 of 6, 4 re-derived; 33 rows, 30 of 30 `frozen` equal (§0.1) | yes — every comparison is an `assert` in `mode_fingerprint` |
| **V2** | §0.3's host gate | H1 to H4, memory and disk, 6 of 6 PASS at the opening read, and again at §3.9; the rest printed (§0.3) | read by the Executor from the verbatim output; the block is shell reads and no code asserts it |
| **V3** | §0.1's and §3.1's file | 1 of 1 hash asserted at each, 1,535 lines and 76,142 bytes at both; the branch's diff against `origin/main` names exactly one path, `A`, 1,535 insertions (§0.2, §2.1) | the hash by the script's `assert`; lines, bytes and the diff read by the Executor |
| **V4** | the self-test | `122 of 122` (§2.2) | yes — each check is an `assert` |
| **V5** | G-REHEARSAL | 10 of 10 figures equal (§2.5) | yes — `assert not bad` |
| **V6** | G-SET | 1,175 considered; 96 non-members, each with its reason; the members by span 920 / 159, weekend 292, pair A 546 / B 533 / both 0 (§2.6, §2.7) | G-SET's three conditions asserted in `mode_fetch`; the splits are printed, not asserted |
| **V7** | the constants, twice | 1 of 1 file `unchanged` at the second run (§2.7) | yes — `write_once` asserts equality |
| **V8** | the score, twice | **VIOLATION**; 2 of 2 files `unchanged`; 2 ledger lines (§2.8) | `unchanged` asserted by `write_once`; the ledger's line count read by the Executor |
| **V9** | G-STILL | both units unchanged, PASS (§2.9) | computed and printed by `still`, not asserted: §4.4 has a FAIL run no block |
| **V10** | opens under the capture roots | refused 0 at every mode; `fetch` `window.json` 1,085 = 1,175 − 90 − 0 − 0 and `books.jsonl.gz` 0; each `score` `books.jsonl.gz` 1,079 = `N` and `window.json` 0; every other mode 0 and 0 (§2.10) | a refusal raises in the hook; the counts are printed and compared by the Executor |
| **V11** | memory | largest peak `62,386,176` against the floor `141,189,120`; `malloc tuned: True` at every mode (§2.10) | the floor and glibc's settings asserted by `floor_check` at `rehearse`, `fetch`, `constants` and `score`; the peaks printed |
| **V12** | contract §4.2's self-check | `0`; one path; nothing (§3) | run after the push and the pull request and before the report's commit; read by the Executor |
| **V13** | §3.9's closing reads | every read printed (§2.11) | printed |
| **V14** | §9's `reclaim` runs | B-RECLAIM-SCRATCH: 4 considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held, store 1,561 → 1,561. B-RECLAIM-OWN: 164 considered, 30 named, 134 kept by name, 164 copied, 0 already held, store 1,561 → 1,725 = 1,561 + 164 (§2.4, §2.13) | yes — `reclaim` asserts each copy's SHA-256 and the store's count after |
| **V15** | §9's removals | `git worktree remove` without `--force` `exit=0`; `test -e` `exit=1` for `/root/tz24-work`, `5ce9f787…` and `750b3996…`; `git worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else (§2.4, §2.13) | read by the Executor; `reclaim` asserted the worktree pristine before its removal |

---

## 6. What could not be implemented as written

1. **Contract §1 steps 1 and 2 ran before §0.0's `mkdir`, as §0.0 orders, so their output is in no log.** The
   session's first `git fetch origin main` and `git merge --ff-only origin/main` moved local `main` from `d567d8e` to
   `6108e4f`. That is the contract's `git checkout main && git pull` in two commands; the session was already on `main`.
   After the `mkdir`, `logs/00-pull.log` recorded `HEAD` and `origin/main` both at `6108e4f`.
2. **Reads the TZ does not name, none under a capture root.**
   - Before §0.0: `git log`, `git show --stat` and `git diff --stat d567d8e origin/main`, of the upload; the
     Executor's own memory notes; and the reads of the TZ, the map and the contract in full, with `grep`s of the
     map's headings and of its §7 items.
   - After §0.0, logged: `logs/00-pull.log`; before B-RECLAIM-SCRATCH, `du -sb` and `find` of the two earlier
     directories, to look at what it would remove (`logs/33-scratch-targets.log`); `logs/40-inventory.log`, which
     hashes every file the run wrote, for §8; `logs/41-input-hashes.log`, the TZ's and the map's `wc` and `sha256sum`
     for §1; and `logs/42-checks.log`, the head and tail of `score` run 2's log and a listing of this session's own
     directory, for §2.10 and item 8 below. The model, read with the session's `get_session` tool, is in
     `logs/00c-model.log`.
   - After §0.0, printed to the session only: `git log -3` of `7f5ae3f`, `git config user.name` and `user.email`,
     `ls .github`, and `gh pr view 23`, to follow the repository's commit and pull-request form; the headings and
     §6 of the TZ-23 report, for the report's form; `cat` and `tail` of this run's logs; `logs/32-selftest.time`;
     the report draft itself, by `grep` and `awk`; and the keys and values of `tz24-reading.json` and
     `tz24-constants.json`. Those files' values are all in
     `score`'s and `constants`' printed output, quoted above. None of these reads printed a book's or a document's
     price beyond what `score` printed.
3. **`I selftest` ran under `/usr/bin/time -v`.** The Executor's own wrapper sat around §3.2's command, which was
   otherwise `I selftest` unchanged. Its report went to `logs/32-selftest.time`: wall clock `0:00.24`, maximum
   resident set `45864` kB, exit status `0`. No other mode was wrapped.
4. **`I reclaim` ran once, with both earlier directories as its arguments.** §9's block writes
   `I reclaim <each earlier directory, by its full path>`, then one `rm -rf` per directory. The Executor read it as
   one `reclaim` naming each directory, which `reclaim TREE...` takes, as TZ-23's Executor did (map §7 item 98, upheld).
   It printed `RECLAIM PASS` before the first removal.
5. **A shell slip in §3.1, with no effect.** The `gh pr create` command ran `cd /root/tz24-work/wt` inside its group,
   so the trailing relative `tail` failed with `No such file or directory`. The pull request had been created, and its
   output, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/24` and `exit=0`, is in `logs/31-branch.log`. Nothing
   was re-run.
6. **The member count is 1,079, not the 1,084 §1 recorded.** Five more windows read `incomplete` (§2.6). §1 records
   1,084 "if every other window qualifies", and asserts nothing. NONE's floor of 528 is far below either count, and the
   reading rests on `V_firm`.
7. **`reclaim` read this report's draft as well as the committed reports.** §8 orders the report drafted in the primary
   checkout before B-RECLAIM-OWN. `report_tokens` reads every `.md` in `CryptoReports/`, committed or not, so the
   draft's hashes named this run's six outputs for the forensic store. Those are the staged copy, the two `set.json`,
   and the constants, units and reading files. The draft was filled by script from the logs
   (`logs/43-report-fill.log`) and checked by a second script against `tz24-reading.json`, `tz24-constants.json` and the
   logs (`logs/44-report-check.log`, 37 of 37). The fill's first attempt stopped at its own row-count assert before
   writing anything, and the checker's first two runs stopped on its own tokenizer, which joined the fields of a `ROW`
   line. Both logs keep every attempt. After B-RECLAIM-OWN the draft was changed in one way only: its placeholders were
   filled from B-RECLAIM-OWN's output. Those were §0.4's last row, §2.10's last row, §2.13, V14 and V15, and the rest of
   this item. The first command's quote and item 9 were then reworded, and the sentence on where the documents are kept,
   item 8 and the list of logs written after 08:32:45 were corrected. Every block in §0 to §2.12 quoted from a log was
   filled before B-RECLAIM-OWN: 17 whole logs, 4 filtered by a pattern, and the ledger. All 22 equal their copies in the
   forensic store byte for byte. That was checked after B-RECLAIM-OWN, along with every SHA-256 in §2.12 and §2.13,
   against the store. Those checks, the report's commit and its push ran after `/root/tz24-work` was gone, so their
   output is in no log; it is printed in the session only.
8. **Where the session's harness keeps output.** From §0.0 to §3.9 every command of the TZ wrote its output to
   `/root/tz24-work/logs/` first, and so did the reads of item 2 marked logged. B-RECLAIM-OWN's output went to no file,
   as §9 orders, and §2.13 quotes it. The checks, the commit and the push after it went to the session only (item 7).
   Nothing was written to the scratchpad, which is empty. No command ran in the background. At 08:37:32 UTC the
   harness's own `tasks/` directory beside the scratchpad held one file, `byqukvqep.output`, of 0 bytes
   (`logs/42-checks.log`, map §7 item 95). The next TZ's B-RECLAIM-SCRATCH removes this session's pair, `5c15abf7…`
   and `65948b60…`.
9. **B-RECLAIM-OWN ran as four commands, not one block.** `I reclaim` ran first. The block's second line ran next,
   then its third, then its fourth to seventh lines together, each as a command of its own, so that a refusal by the
   classifier could not discard what ran before it. Each of the four began with `date -u +%FT%TZ`. The last added
   `grep MemAvailable /proc/meminfo`, which §0.4 and §2.13 quote. Nothing was refused.
