# TZ-28 report — the pair book's archive on a timer: TZ-27's steps, once a day, unattended

**G-TZ27 PASS** — TZ-27's Release `409534533` on `tz-27-pairbook-streams`, read with no token: 51 of 51 assets `uploaded`, each with the set's bytes and `sha256:` digest, none missing and none beyond the set, in 2 requests. **P-PATH: served** — 3 requests with no token, each inside the idle stretch, started at seconds 375, 375 and 376; the 76,818,669-byte download hashed equal. **P-TOKEN: served** — the credential's source is the primary checkout's remote URL, `push` is true, and Release `409534533` read back, in 2 requests; the Boss ran this block.
**G-INSTALL PASS: 8 of 8** — the service's three files, the two units and the empty state directory `0700`, all at the branch head `d8194fd`. **G-TIMER PASS**, 9 of 9 checks at 15:08:34 UTC, 23 s after B-ENABLE, and again at `final`. **The next calendar run is 2026-10-12 03:00:20 UTC.**
**The first run, fired by the timer at 15:18:12 UTC, on its 600 s elapse after it started at 15:08:11 (601 s by systemd's whole-second stamps):** `A` = `1791731892`; **28 stream files from 28 windows, 430,047,476 bytes**, windows `1791706500` to `1791730800` (79 windows considered, all closed, 0 deferred). **It went to Release `409746510` on the lightweight tag `pairbook-streams-1791731892`**, which points at `d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3`. The run ended `complete` at 15:30:41 UTC with exit `0`, `Result` `success`, and no deferral and no retry.
**G-UPLOAD PASS, G-DOWNLOAD PASS, G-DELETE PASS** — 28 of 28 assets read back by the Release's own record, with the set's bytes and digest. 28 of 28 full anonymous downloads were equal. 28 of 28 files were hashed again and removed, and every window kept its `window.json`. **Freed: 430,047,476 bytes** by the run's own count; its free-space reads went from 12,538,937,344 to 12,969,091,072.
**G-RESTART PASS, G-COUNTER PASS, G-UNIT PASS, G-RESUME PASS** — the `SIGTERM` came at second 391 of window `1791731700`. Pid `815823` stopped, and pid `851381` started on the same code 5.548 s later, `NRestarts` 3. Its start record's `stream_bytes` is `0`, equal to the store, and G-UNIT read 10 of 10 at 3 restarts at the run, at `first` and at `final`. Window `1791731700` then streamed (237,078 frames) with no reason to keep it off.
**G-IDLE PASS** — 61 of 61 requests started inside seconds 15 to `590 − budget` of their window and ended by second 590: 0 started outside and 0 ended outside. All 61 fell in window `1791731700`: the upload's requests started at seconds 193 to 235, the verify's at 357 to 390.
**G-STILL PASS** — the recorder was unchanged from 14:50:56 to 15:33:55 UTC: pid `4148534`, `NRestarts` 2, `active`. **FIRST PASS: 11 of 11; FINAL PASS.** No block of §4.8 was run, and neither B-RETRY nor B-START-SVC was needed.
**The timer, the pair book and the recorder all run.** The timer is `active`/`enabled`, waiting for 2026-10-12 03:00:20 UTC. `btc-pairbook.service` is pid `851381`, `active`/`enabled`. `btc-recorder.service` is pid `4148534`, `active`/`enabled`. This was verified from the session by `I first`, `I final` and §3.10's `systemctl show`, `list-timers`, `journalctl` and log tails, not from the Boss's account.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-28-pairbook-archive-timer.md`, 2,359 lines, 158,218 bytes, SHA-256 `331a291fec8a7ae6f07612bfb96a9f21f41f2f590fd8ee230c8b40d5bd1d025d`, landed at `82c5ddc` |
| map revision | `2026-10-11-b`, equal; anchors 6 of 6; re-derived 4 of 4; rows 37; `frozen` equal 34 of 34 |
| executor model | Opus, as the TZ names. `get_session` read `session_context.model` and `last_served_model` as `claude-opus-5-5` |
| branch | `tz-28-pairbook-archive-timer` at `d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3`, pushed; pull request #27, open, not merged |
| service code | `/root/btc-pairbook-archive-svc/`: `tz28-pairbook-archive-timer.py` `46a019d6…`, `tz27-pairbook-archive.py` `2cba96bc…`, `commit.txt` `d8194fd…` |
| units | `/etc/systemd/system/btc-pairbook-archive.service` `2e7fd453…`, `btc-pairbook-archive.timer` `07581f4f…`, byte for byte the branch's |
| first run | `A` `1791731892`, invocation `2a4b998acb9f4883b26999bb278624bf`, 15:18:12 to 15:30:41 UTC, `complete` |
| first run's Release | id `409746510`, tag `pairbook-streams-1791731892` (lightweight, at `d8194fd…`), 28 assets, 430,047,476 bytes |
| work tree | `/root/tz28-work`, removed by B-RECLAIM-OWN (§2.19) |

---

## 0. Fingerprint

**Map revision read:** `2026-10-11-b`, equal to the TZ's. **Anchors**, each equal to the TZ header's and the map's §0:
`A1` `229a944f2d51`, `A2` `6c5089330629`, `A3` `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable`, `A4` `437b45ea196b`, `A5` `0f6c90451cbd`, `A6` `729f0bcdbee3`. `A2`, `A4`, `A5` and `A6` were re-derived by the instrument from the files' SHA-256.

### 0.1 The 37 rows of the map's §0 table, and the map (V1) — `logs/02-fingerprint.log`, verbatim

`I0 fingerprint`, the staged copy, from `/root/tz28-work`:

```
[2026-10-11T14:49:52Z] re-derived A2 research/twap-divergence.py sha256[:12] 6c5089330629 equal
[2026-10-11T14:49:52Z] re-derived A4 BTC-EXECUTOR-INSTRUCTIONS.md sha256[:12] 437b45ea196b equal
[2026-10-11T14:49:52Z] re-derived A5 research/recorder/recorder.py sha256[:12] 0f6c90451cbd equal
[2026-10-11T14:49:52Z] re-derived A6 research/pfair.py sha256[:12] 729f0bcdbee3 equal
[2026-10-11T14:49:52Z] SYSTEM-MAP.md                                  1406 lines   317476 bytes 1e050baf540142ccf9046b75f409e9f5d52170e64cf9d01c698fc1d84946576c reported
[2026-10-11T14:49:52Z] BTC-EXECUTOR-INSTRUCTIONS.md                    234 lines    11128 bytes 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b frozen equal
[2026-10-11T14:49:52Z] research/twap-divergence.py                    1135 lines    50928 bytes 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 frozen equal
[2026-10-11T14:49:52Z] research/selftest-twap-divergence.py            376 lines    16736 bytes ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a frozen equal
[2026-10-11T14:49:52Z] research/tz02-distribution.py                   334 lines    14511 bytes f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 tracked
[2026-10-11T14:49:52Z] research/pfair.py                               441 lines    19357 bytes 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 frozen equal
[2026-10-11T14:49:52Z] research/selftest-pfair.py                      619 lines    32559 bytes b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa frozen equal
[2026-10-11T14:49:52Z] research/tz06-calibration.py                    577 lines    27138 bytes 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f frozen equal
[2026-10-11T14:49:52Z] research/tz07a-variance-time.py                 623 lines    28414 bytes 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 frozen equal
[2026-10-11T14:49:52Z] research/tz07b-settlement-dispersion.py         515 lines    24926 bytes 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc frozen equal
[2026-10-11T14:49:52Z] research/tz08a-out-of-sample.py                 745 lines    38822 bytes 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c frozen equal
[2026-10-11T14:49:52Z] research/tz09-disk-inventory.py                 894 lines    41004 bytes b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 frozen equal
[2026-10-11T14:49:52Z] research/tz10b-sigma-or-link.py                1224 lines    61018 bytes 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 frozen equal
[2026-10-11T14:49:52Z] research/tz11a-student-link.py                 1231 lines    64732 bytes 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 frozen equal
[2026-10-11T14:49:52Z] research/tz12-sized-gate.py                    1157 lines    61637 bytes d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 frozen equal
[2026-10-11T14:49:52Z] research/tz13-sized-gate-test3.py              1074 lines    53901 bytes a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd frozen equal
[2026-10-11T14:49:52Z] research/tz14-quote-inventory.py               2124 lines   109972 bytes 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 frozen equal
[2026-10-11T14:49:52Z] research/tz15-phase2-gate.py                   1517 lines    73799 bytes 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 frozen equal
[2026-10-11T14:49:52Z] research/tz16a-phase2-decisive-gate.py         2198 lines   111192 bytes 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 frozen equal
[2026-10-11T14:49:52Z] research/tz17-settlement-chain.py              1102 lines    38622 bytes e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 frozen equal
[2026-10-11T14:49:52Z] research/tz18a-chainbook-capture.py            1683 lines    69517 bytes e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae frozen equal
[2026-10-11T14:49:52Z] research/tz20-capture-under-systemd.py          771 lines    36528 bytes 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7 frozen equal
[2026-10-11T14:49:52Z] research/tz21-recorder-memory.py               1284 lines    59009 bytes d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f frozen equal
[2026-10-11T14:49:52Z] research/tz23-maker-m0.py                      1184 lines    54885 bytes 6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f frozen equal
[2026-10-11T14:49:52Z] research/tz24-nesting-b2.py                    1535 lines    76142 bytes 4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b frozen equal
[2026-10-11T14:49:52Z] research/tz26-nesting-b3-capture.py            2492 lines   118466 bytes caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec frozen equal
[2026-10-11T14:49:52Z] research/tz27-pairbook-archive.py              2078 lines   106284 bytes 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673 frozen equal
[2026-10-11T14:49:52Z] research/recorder/recorder.py                   651 lines    27821 bytes 0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7 frozen equal
[2026-10-11T14:49:52Z] research/recorder/config.py                     112 lines     4773 bytes 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d frozen equal
[2026-10-11T14:49:52Z] research/recorder/manifest.py                   254 lines    10002 bytes 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 frozen equal
[2026-10-11T14:49:52Z] research/recorder/analyze.py                    813 lines    34705 bytes eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d frozen equal
[2026-10-11T14:49:52Z] research/recorder/probe.py                      227 lines     9324 bytes 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 frozen equal
[2026-10-11T14:49:52Z] research/recorder/selftest.py                   573 lines    30591 bytes c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 frozen equal
[2026-10-11T14:49:52Z] deploy/systemd/btc-recorder.service              23 lines      707 bytes 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1 frozen equal
[2026-10-11T14:49:52Z] deploy/systemd/btc-chainbook.service             22 lines      724 bytes a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2 frozen equal
[2026-10-11T14:49:52Z] deploy/systemd/btc-pairbook.service              22 lines      761 bytes ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8 frozen equal
[2026-10-11T14:49:52Z] .gitignore                                        5 lines      252 bytes 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b tracked
[2026-10-11T14:49:52Z] SYSTEM-MAP.md 1406 lines 317476 bytes sha256 1e050baf540142ccf9046b75f409e9f5d52170e64cf9d01c698fc1d84946576c
[2026-10-11T14:49:52Z] FINGERPRINT PASS: revision 2026-10-11-b; anchors 6 of 6, 4 re-derived; rows 37: frozen 34 of 34 equal, tracked 2, reported 1
[2026-10-11T14:49:52Z] peak memory of this run: 35803136 bytes
[2026-10-11T14:49:52Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

### 0.2 §0.0 and §0.1 — the work tree, and the instrument staged (V3)

`logs/00-worktree.log`:

```
mkdir /root/tz28-work /root/tz28-work/logs; echo "exit=$?"
exit=0
at 2026-10-11T14:49:42Z
82c5ddc1445e39c0b1ca2e6778a2fbd482b588e3
```

`logs/01-stage.log` — §0.1's script, verbatim, then TZ-27's file installed beside it:

```
/root/tz28-work/stage/deploy/systemd/btc-pairbook-archive.service 17 794 2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7
/root/tz28-work/stage/deploy/systemd/btc-pairbook-archive.timer 13 417 07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913
/root/tz28-work/stage/research/tz28-pairbook-archive-timer.py 1438 74576 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4
exit=0
exit=0
2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673  /root/tz28-work/stage/research/tz27-pairbook-archive.py
```

### 0.3 Host gate — the opening reads, verbatim (V2) — `logs/03-host-gate.log`

```
Sun Oct 11 02:50:02 PM UTC 2026
1791730202
1
MemTotal:         978640 kB
MemAvailable:     286812 kB
SwapTotal:       3174396 kB
SwapFree:        2807848 kB
systemd 255 (255.4-1ubuntu8.17)
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12582281216
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
1
active
exit=0
enabled
exit=0
cmp exit=0
e8b46a85d61e1a17841962846f6d3012046c2d70
caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec  /root/btc-pairbook-svc/tz26-nesting-b3-capture.py
MainPID=815823
NRestarts=2
3.12.3
active
inactive
exit=0
enabled
disabled
exit=0
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
/root/btc-pairbook-archive-svc exit=1
/var/lib/btc-pairbook-archive exit=1
/etc/systemd/system/btc-pairbook-archive.service exit=1
/etc/systemd/system/btc-pairbook-archive.timer exit=1
/root/tz27-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd  /root/btc-forensics/tz27-work--archive--set.json
1810
/root/btc-5m-twap       82c5ddc [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
396936979	/var/lib/btc-pairbook
198406283	/root/.claude
534106552	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/6b7bd886-7088-5233-bdf9-903a19178e6a/scratchpad
total 24
drwx------  6 root root 4096 Oct 11 14:48 .
drwx------ 16 root root 4096 Oct 11 14:48 ..
drwx------  4 root root 4096 Oct 11 14:48 6b7bd886-7088-5233-bdf9-903a19178e6a
drwx------  3 root root 4096 Oct 11 14:48 6de9e261-2fb6-4db9-ae09-1fd283c3b8c8
drwx------  4 root root 4096 Oct 11 08:17 70b5ba7a-7e9e-5c10-a353-278a1431d82a
drwx------  3 root root 4096 Oct 11 08:17 952e88f3-b9a6-4bd2-b674-b9deebd16088
```

| condition | read | result |
|---|---|---|
| H1 | one path, `/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json` | PASS |
| H2 | `/dev/vda2`, `31612203008`; `grep -c` `1` | PASS |
| H3 | `active` exit 0; `enabled` exit 0; `cmp exit=0`; `commit.txt` `e8b46a85…`; `caed70d9…` | PASS |
| H4 | `3.12.3` | PASS |
| H5 | the four archive paths `exit=1`; `ec71b1a7…` | PASS |
| memory gate | `MemAvailable` 286,812 kB = 293,695,488 bytes ≥ 106,086,400 | PASS |
| disk gate | `avail` 12,582,281,216 ≥ 2,300,000,000 | PASS |

**Printed, with no threshold:** systemd 255. The pair book was `MainPID` `815823`, `NRestarts` 2, as map §6 states. The recorder was `active`/`enabled`, the chain book `inactive`/`disabled`, and `telemetry-watch.service` `disabled` (exit 1) and `inactive` (exit 3). The recorder's tree was at `e3975b5…`. `/root/tz27-work` was absent and the three code trees present. The forensic store held 1,810 files, as map §3 says. There were two worktrees. `du` read `/var/lib/btc-pairbook` 396,936,979, `/root/.claude` 198,406,283 and `/root/PROJECT_GAMING_PS5` 534,106,552 bytes. Beside this session's own directory, the listing showed `6de9e261…`, `70b5ba7a…` and `952e88f3…`.

### 0.4 Free space and `MemAvailable` — every read, its instant and its bound

| instant (UTC) | read by | free on `/dev/vda2` | `MemAvailable` | bound |
|---|---|---|---|---|
| 14:50:02 | §0.3 host gate | 12,582,281,216 | 293,695,488 (286,812 kB) | disk 2,300,000,000; memory 106,086,400 |
| 14:50:15 | `I0 tz27-release` | — | 259,641,344 | 93,454,336 |
| 14:51:15 | `I path` | — | 305,045,504 | 93,454,336 |
| 15:04:49 | `I path-token` (the Boss) | — | 299,114,496 | 93,454,336 |
| 15:18:12 | the run's `floors` | not read by the session (§6 item 5) | not read by the session (§6 item 5) | 2,001,000,000; 106,086,400 |
| 15:21:30 | the run, before its removal (`delete` record) | 12,538,937,344 | — | — |
| 15:21:31 | the run, after its removal (`delete` record) | 12,969,091,072 | — | — |
| 15:21:37 | the pair book's start record (`restart` record) | 12,969,062,400 | — | — |
| 15:30:41 | the run's `complete` record | 12,949,487,616 | — | — |
| 15:33:56 | `I final` | 12,940,468,224 | — | — |
| 15:34:08 | §3.10 (§0.3's block again) | 12,940,390,400 | 265,424,896 (259,204 kB) | — |
| 15:34:08 | §3.10, `free -b` and `df` | 12,940,374,016 | `available` 275,247,104 | — |

The self-test's own `MemAvailable 300000000 … free 12931072000` lines in `logs/13-selftest.log` belong to its simulated world, not the host.

### 0.5 Refs (§0.5) — `logs/05-refs.log`, verbatim

```
2026-10-11T14:50:09Z
82c5ddc1445e39c0b1ca2e6778a2fbd482b588e3	HEAD
82c5ddc1445e39c0b1ca2e6778a2fbd482b588e3	refs/heads/main
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8	refs/heads/tz-23-maker-m0
6f045cffc3601b589d3b8b7a6a9af6f73991e18b	refs/heads/tz-24-nesting-b2
e8b46a85d61e1a17841962846f6d3012046c2d70	refs/heads/tz-26-nesting-b3-capture
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/heads/tz-27-pairbook-archive
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
ee2f6327390ef4d0c6169d1fba1a2ed4ae936dc3	refs/pull/3/head
0e13a5c76dfa2469ff25b3b0dd282872decf6f25	refs/pull/4/head
4216c04673ced76b5b2ac60ef57c9abedc46f9b9	refs/pull/5/head
5ed667afd1b53f036b9f938fcce13c0d709cd77f	refs/pull/6/head
c44af687203d14d5d485d4297c04cfb827096af9	refs/pull/7/head
26bbb61aed774a88355dd5204d8b69fda9135a68	refs/pull/8/head
e2625ea2b5473c311d59a48f32540ce39d58e591	refs/pull/9/head
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
e299d4e45f48b7efaa8cb18bd54b139fc0627630	refs/tags/tz-27-pairbook-streams
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/tags/tz-27-pairbook-streams^{}
ref lines=36
--- first-parent commits above 2c1fcd0 on main
82c5ddc1445e39c0b1ca2e6778a2fbd482b588e3 2026-10-11T18:47:36+04:00 Add files via upload
56208738e337f4853890702cffeac32a57a808a8 2026-10-11T18:45:59+04:00 Update SYSTEM-MAP.md
== 82c5ddc1445e39c0b1ca2e6778a2fbd482b588e3
A	CryptoTZ/TZ-28-pairbook-archive-timer.md
== 56208738e337f4853890702cffeac32a57a808a8
M	SYSTEM-MAP.md
--- forbidden refs
0
1
```

**36 ref lines**, as map §1 says. The ref set equals map §1's apart from `main`: five branches, two tags, `refs/pull/1…26/head`. `main` was at `82c5ddc`, two first-parent commits above `2c1fcd0`: `5620873`, which modified `SYSTEM-MAP.md` (revision `2026-10-11-b`), and `82c5ddc`, which added `CryptoTZ/TZ-28-pairbook-archive-timer.md`. Before the push, `main` carried revision `2026-10-11-b`, and neither `refs/heads/tz-28-pairbook-archive-timer` nor any `refs/tags/pairbook-streams-*` existed. Nothing here BLOCKS.

### 0.6 G-TZ27 (V5): **PASS** — `logs/06-tz27-release.log`, verbatim

```
[2026-10-11T14:50:15Z] MemAvailable 259641344 bytes, floor 93454336
[2026-10-11T14:50:16Z] V 1791660600-stream.jsonl.gz id 630207636 state uploaded bytes 13423467 digest sha256:02673b7227ce9c9d44451e3b9415fb8e84b37ab0b280aeeb15117d7776a14095 url True: True
[2026-10-11T14:50:16Z] V 1791661500-stream.jsonl.gz id 630207676 state uploaded bytes 13439976 digest sha256:8d1153a600c626bb9914f5fc18cd68e36b0fe53f3cd95cfe58746cc7025e7b51 url True: True
[2026-10-11T14:50:16Z] V 1791662400-stream.jsonl.gz id 630207710 state uploaded bytes 9568261 digest sha256:6cd316eea7ee397141e858c3b8061afbfc65f1363275b9f4810fba199e6ca60e url True: True
[2026-10-11T14:50:16Z] V 1791663300-stream.jsonl.gz id 630207741 state uploaded bytes 14589273 digest sha256:e05ff3f11a3788498a2a3a0beb72259b4297b844a071bfa7fef2d642ee3c0dde url True: True
[2026-10-11T14:50:16Z] V 1791664200-stream.jsonl.gz id 630207859 state uploaded bytes 13421235 digest sha256:30e3ffcd0035c928ddb9cf3beadc047b13e351a090829df46e92718a5b277e04 url True: True
[2026-10-11T14:50:16Z] V 1791665100-stream.jsonl.gz id 630207911 state uploaded bytes 11129213 digest sha256:cd6d078247cd399ffcc827355b28114711fe8c4dbf7a35f8ac8e16194a52b3f5 url True: True
[2026-10-11T14:50:16Z] V 1791666000-stream.jsonl.gz id 630207960 state uploaded bytes 25488448 digest sha256:f033da5ad81a8e5eafcc5e5867a85a86a54bb996f073178099999e63d1a7bfdd url True: True
[2026-10-11T14:50:16Z] V 1791666900-stream.jsonl.gz id 630208010 state uploaded bytes 12837545 digest sha256:b5ab1e59d30cc64a990a9b94ed7f6d24e0807d6c3819ff52f05b1d9558440d91 url True: True
[2026-10-11T14:50:16Z] V 1791667800-stream.jsonl.gz id 630208048 state uploaded bytes 17449667 digest sha256:1f38535d92c7201e82d646644430752ffbb43777112e96747848011fcba795f8 url True: True
[2026-10-11T14:50:16Z] V 1791668700-stream.jsonl.gz id 630208087 state uploaded bytes 18821724 digest sha256:26fa1060e3dd5cc863b9d71abef1a4b682326a0911424eb761c1b71800c1187b url True: True
[2026-10-11T14:50:16Z] V 1791669600-stream.jsonl.gz id 630208141 state uploaded bytes 18782634 digest sha256:ac057cae7f0835e3a0814f680377b7ade08b82c8daec056f0f586ab565414934 url True: True
[2026-10-11T14:50:16Z] V 1791670500-stream.jsonl.gz id 630208181 state uploaded bytes 13835617 digest sha256:3fba28fc972a067f1252d95027062a34555a364d49d97b6d7e0fc9d0fe05cc1d url True: True
[2026-10-11T14:50:16Z] V 1791671400-stream.jsonl.gz id 630208215 state uploaded bytes 22778515 digest sha256:53ac058c216842bbe55730243450705cf4b0c57450c5994a9377e28979a8a037 url True: True
[2026-10-11T14:50:16Z] V 1791672300-stream.jsonl.gz id 630208259 state uploaded bytes 11020668 digest sha256:be47f4c6107086fdbdfa9e50322fd077779ff71ea3ee21fba510a83b0ef20f99 url True: True
[2026-10-11T14:50:16Z] V 1791673200-stream.jsonl.gz id 630208292 state uploaded bytes 17935756 digest sha256:91f62a49534c1cdaa11c960c7a1e054b50797291b972b93103b3d4304201f4d7 url True: True
[2026-10-11T14:50:16Z] V 1791674100-stream.jsonl.gz id 630208335 state uploaded bytes 16755227 digest sha256:821a3b25ca7b894ef70f74ac32067c656568c977b00672946ee7147a698cf61d url True: True
[2026-10-11T14:50:16Z] V 1791675000-stream.jsonl.gz id 630208365 state uploaded bytes 17246512 digest sha256:5f4ddb59abb34d187de3be12baf33aeb79e2c9be9191a93e2bc2fe22eaef7d3b url True: True
[2026-10-11T14:50:16Z] V 1791675900-stream.jsonl.gz id 630208422 state uploaded bytes 11174283 digest sha256:3ddc73de13809d435f3abe0e3ee6eadad721a363e9dc20fa0d47f52eb19bb1c9 url True: True
[2026-10-11T14:50:16Z] V 1791676800-stream.jsonl.gz id 630208452 state uploaded bytes 14095311 digest sha256:93973541db575dcf5a9497d73f61172f59299f54a5bfd764c82daf90174f651a url True: True
[2026-10-11T14:50:16Z] V 1791677700-stream.jsonl.gz id 630208489 state uploaded bytes 9762989 digest sha256:e99255d6c6f008c761028db6d9ee077bf2045ac378a773e3c5a75c4e131501d3 url True: True
[2026-10-11T14:50:16Z] V 1791678600-stream.jsonl.gz id 630208544 state uploaded bytes 14290425 digest sha256:65716063fcea58dc0744bbcdf0c6499e60be2d64a9fd7ed94dac2132d64853bf url True: True
[2026-10-11T14:50:16Z] V 1791679500-stream.jsonl.gz id 630208568 state uploaded bytes 15182911 digest sha256:f44fd640415c3508b37e552448bc6a901a5eb5a529478e940eff0a2823fa670a url True: True
[2026-10-11T14:50:16Z] V 1791680400-stream.jsonl.gz id 630208604 state uploaded bytes 13039899 digest sha256:d6efb02da1c816fd51cd780b608326a90bde01ba337c78988da57d14ff241ed2 url True: True
[2026-10-11T14:50:16Z] V 1791681300-stream.jsonl.gz id 630208643 state uploaded bytes 15944520 digest sha256:e3f47ea555e0449c05b181f862340f2fbfcfb67612ea9a58be2229f465667eb1 url True: True
[2026-10-11T14:50:16Z] V 1791682200-stream.jsonl.gz id 630208675 state uploaded bytes 12105846 digest sha256:d773a167b99f70b8da2db2d13e534b26f3ca72f8d3d28437c618ab52c9fa405f url True: True
[2026-10-11T14:50:16Z] V 1791683100-stream.jsonl.gz id 630208720 state uploaded bytes 14736000 digest sha256:27ac9a8c957e66a7d30b447303536ebc3ee5f3cd915b2dd01cec72eb2f5c81cf url True: True
[2026-10-11T14:50:16Z] V 1791684000-stream.jsonl.gz id 630208759 state uploaded bytes 12587712 digest sha256:960a7bc878478e68425395ae4764e9e72fa2a4a7d5fdd90ccd7f12bbf9136736 url True: True
[2026-10-11T14:50:16Z] V 1791684900-stream.jsonl.gz id 630208781 state uploaded bytes 18090382 digest sha256:6ef8c2d62603ff442f5ac0f0d11d2a26a28ba1cfefc4b4ea1af27e26f5a7e050 url True: True
[2026-10-11T14:50:16Z] V 1791685800-stream.jsonl.gz id 630208842 state uploaded bytes 5691840 digest sha256:93b2387191bdbea4199ba39fe42c1266b2476d7ba9d75912552fdb01b53beb76 url True: True
[2026-10-11T14:50:16Z] V 1791686700-stream.jsonl.gz id 630208866 state uploaded bytes 10296232 digest sha256:3904d031288bbf14ea9a3f269f4260d8e0ad0f28fa8ab91f51e95fba98cdb8aa url True: True
[2026-10-11T14:50:16Z] V 1791687600-stream.jsonl.gz id 630208906 state uploaded bytes 4761970 digest sha256:22fe211139a1475883d617bcd15861d2da59d552deb9db89c9138012f21b5365 url True: True
[2026-10-11T14:50:16Z] V 1791688500-stream.jsonl.gz id 630208929 state uploaded bytes 11715539 digest sha256:15b3ab4e3cb1fccd2a7e77f71f606f8de8894f32cc3437a6b5f016537d0bc8ef url True: True
[2026-10-11T14:50:16Z] V 1791689400-stream.jsonl.gz id 630208961 state uploaded bytes 11045964 digest sha256:e45ae87c4d50ad67fc0f300ab9b9d123fc95deab16a30937c9ab4729adf698c6 url True: True
[2026-10-11T14:50:16Z] V 1791690300-stream.jsonl.gz id 630209005 state uploaded bytes 9320326 digest sha256:50bc2a033d3a8dc4b0aa2291563f442291e62e532a7c9698738cc7b3165dbb97 url True: True
[2026-10-11T14:50:16Z] V 1791691200-stream.jsonl.gz id 630209056 state uploaded bytes 15738124 digest sha256:53604f4792e7f198c6f95dc7061de06d65a18660e2ceedbca8f6797d3123f76f url True: True
[2026-10-11T14:50:16Z] V 1791692100-stream.jsonl.gz id 630209085 state uploaded bytes 7204207 digest sha256:24bf61060b7b44e334467817cd71afe227e62b6edad3a139ea8142715365730c url True: True
[2026-10-11T14:50:16Z] V 1791693000-stream.jsonl.gz id 630209120 state uploaded bytes 11830926 digest sha256:fda5ecba6aa24ea471e86853596d7840918ec4f79541a3d3d968b1afff5dbccf url True: True
[2026-10-11T14:50:16Z] V 1791693900-stream.jsonl.gz id 630209150 state uploaded bytes 10615743 digest sha256:a66ee84f868e6874204419f8462943cead9edc18561398936d995fa4a393d287 url True: True
[2026-10-11T14:50:16Z] V 1791694800-stream.jsonl.gz id 630209181 state uploaded bytes 12732416 digest sha256:cca4f7fd1511849c336ee64318d21e1ddbc74b9acd7f436c386b424ed801b5d4 url True: True
[2026-10-11T14:50:16Z] V 1791695700-stream.jsonl.gz id 630209240 state uploaded bytes 12435463 digest sha256:259f6b40c19d3ef2faf993ae6d9a28c32480355cc3fca75276546156228d70b7 url True: True
[2026-10-11T14:50:16Z] V 1791696600-stream.jsonl.gz id 630209282 state uploaded bytes 21533515 digest sha256:8a600a6750338c9072aa29811a6ac16971123573b6537eb54e816df3969447b6 url True: True
[2026-10-11T14:50:16Z] V 1791697500-stream.jsonl.gz id 630209360 state uploaded bytes 8946297 digest sha256:efbc615ed1bba78b2aa4872a9f5780bc0f46c3614443a45b29b802bfa931873c url True: True
[2026-10-11T14:50:16Z] V 1791698400-stream.jsonl.gz id 630209426 state uploaded bytes 17931091 digest sha256:eaa000dd2664e3013f33318df6a4f9a6e58085a2c66262374e2dcec6ab960e69 url True: True
[2026-10-11T14:50:16Z] V 1791699300-stream.jsonl.gz id 630209478 state uploaded bytes 10168130 digest sha256:a6b417a805200d2a36f156a2809c7c09cf41a45890558432218d81b292855715 url True: True
[2026-10-11T14:50:16Z] V 1791700200-stream.jsonl.gz id 630209519 state uploaded bytes 5672037 digest sha256:268e31d2c217dacbce44f02128e9949b5a3551e9b8e441caf9776507d7feff67 url True: True
[2026-10-11T14:50:16Z] V 1791701100-stream.jsonl.gz id 630209557 state uploaded bytes 7932326 digest sha256:49e14ae788bc6c6d63947cd584a50b3983b7be6f7d6aa4065b01f9d42e87b1fb url True: True
[2026-10-11T14:50:16Z] V 1791702000-stream.jsonl.gz id 630209602 state uploaded bytes 9990431 digest sha256:2d12f225b94db6e563d3fc4ac68a329d7537bdbaac67eb16e518c5a02689612a url True: True
[2026-10-11T14:50:16Z] V 1791702900-stream.jsonl.gz id 630209655 state uploaded bytes 10963207 digest sha256:bd299f639f39b9954d9590d0c0178d3ee10aadae36902ff32b21849508294730 url True: True
[2026-10-11T14:50:16Z] V 1791703800-stream.jsonl.gz id 630209730 state uploaded bytes 9651372 digest sha256:9960707372625ab632458eacc4a1d003dd553256a1822e55610a5516ad9eb785 url True: True
[2026-10-11T14:50:16Z] V 1791704700-stream.jsonl.gz id 630209811 state uploaded bytes 24968352 digest sha256:7dff7b4da4db3d94b655a0433346eab280f465eae99e42de0d03d20397d1447d url True: True
[2026-10-11T14:50:16Z] V 1791705600-stream.jsonl.gz id 630209913 state uploaded bytes 8059980 digest sha256:1df39ae5f1709395ed1c4d24c654762bd972097b47d87e5e43f007d36e404401 url True: True
[2026-10-11T14:50:16Z] G-TZ27 release published on the tag                         True
[2026-10-11T14:50:16Z] G-TZ27 no asset missing                                     True
[2026-10-11T14:50:16Z] G-TZ27 no asset beyond the set                              True
[2026-10-11T14:50:16Z] G-TZ27 every asset uploaded, its bytes and digest the set's True
[2026-10-11T14:50:16Z] G-TZ27 the Release TZ-27 created                            True
[2026-10-11T14:50:16Z] G-TZ27 PASS: Release 409534533 on tz-27-pairbook-streams, 51 of 51 assets uploaded with the set's bytes and digest, nothing beyond the set; 2 requests
[2026-10-11T14:50:16Z] peak memory of this run: 37154816 bytes
[2026-10-11T14:50:16Z] opens refused: 0; store opens 0; requests 2, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

---

## 1. Input

- `CryptoTZ/TZ-28-pairbook-archive-timer.md` at `82c5ddc`, 2,359 lines, 158,218 bytes, `331a291f…`, read in full. Appendix A was extracted by §0.1's script twice, to `stage/` and to the worktree, and both extractions produced three of three identical hashes.
- `SYSTEM-MAP.md` revision `2026-10-11-b`, 1,406 lines, 317,476 bytes, `1e050baf540142ccf9046b75f409e9f5d52170e64cf9d01c698fc1d84946576c`, read in full, with its 37 rows hashed by `fingerprint`.
- `research/tz27-pairbook-archive.py` at `main`, `2cba96bc…`, staged, installed, and loaded by its bytes in every mode and in the run.
- `/root/btc-forensics/tz27-work--archive--set.json`, 16,570 bytes, `ec71b1a7…`, read by `tz27-release`.
- **The first run's set** was taken by the unit's own run as of `A` = `1791731892`: every window directory of `/var/lib/btc-pairbook/`, 79 considered and all closed, with 28 stream files taken. The run hashed, sent and downloaded these files and decompressed none. **Nothing was re-collected**, and no price, size, side, book hash or outcome was read or printed (§2 item 10).
- GitHub, read with no token: TZ-27's Release (2 requests); `tz-01a-dataset`'s Release and its asset (3); and the first run's Release, read again by `first` (2). The Boss's `path-token` made 2 more requests under the credential.

---

## 2. Measurements

### 2.1 §3.1 — the branch and its files (V3) — `logs/10-branch.log`, `logs/11-commit-push.log`, `logs/12-pr.log`

```
2026-10-11T14:50:28Z
fetch exit=0
Preparing worktree (new branch 'tz-28-pairbook-archive-timer')
branch 'tz-28-pairbook-archive-timer' set up to track 'origin/main'.
HEAD is now at 82c5ddc Add files via upload
worktree exit=0
/root/tz28-work/wt/deploy/systemd/btc-pairbook-archive.service 17 794 2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7
/root/tz28-work/wt/deploy/systemd/btc-pairbook-archive.timer 13 417 07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913
/root/tz28-work/wt/research/tz28-pairbook-archive-timer.py 1438 74576 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4
extract exit=0
 1438 74576 research/tz28-pairbook-archive-timer.py
   17   794 deploy/systemd/btc-pairbook-archive.service
   13   417 deploy/systemd/btc-pairbook-archive.timer
 1468 75787 total
46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4  research/tz28-pairbook-archive-timer.py
2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7  deploy/systemd/btc-pairbook-archive.service
07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913  deploy/systemd/btc-pairbook-archive.timer
2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673  research/tz27-pairbook-archive.py
?? deploy/systemd/btc-pairbook-archive.service
?? deploy/systemd/btc-pairbook-archive.timer
?? research/tz28-pairbook-archive-timer.py
```

```
commit exit=0
d8194fd TZ-28: the pair book's archive on a timer - research/tz28-pairbook-archive-timer.py and its two units
 deploy/systemd/btc-pairbook-archive.service |   17 +
 deploy/systemd/btc-pairbook-archive.timer   |   13 +
 research/tz28-pairbook-archive-timer.py     | 1438 +++++++++++++++++++++++++++
 3 files changed, 1468 insertions(+)
remote: 
remote: Create a pull request for 'tz-28-pairbook-archive-timer' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-28-pairbook-archive-timer        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-28-pairbook-archive-timer -> tz-28-pairbook-archive-timer
branch 'tz-28-pairbook-archive-timer' set up to track 'origin/tz-28-pairbook-archive-timer'.
push exit=0
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
A	deploy/systemd/btc-pairbook-archive.service
A	deploy/systemd/btc-pairbook-archive.timer
A	research/tz28-pairbook-archive-timer.py
```

```
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/27
exit=0
```

The branch's diff against `origin/main` names exactly the three paths, each `A`. Each file's hash, lines and bytes are equal at §0.1 and §3.1: 1,438 / 74,576 `46a019d6…`; 17 / 794 `2e7fd453…`; 13 / 417 `07581f4f…`.

### 2.2 §3.2 — the self-test (V4): **34 of 34** — `logs/13-selftest.log`, verbatim

```
[2026-10-11T14:50:50Z]   ok  the budget: 5 s and the bytes at 2,000,000 a second, rounded up
[2026-10-11T14:50:50Z]   ok  the calendar: 03:00:20 UTC, the next after now
[2026-10-11T14:50:50Z]   ok  systemctl's stamps, read in UTC alone
[2026-10-11T14:50:50Z]   ok  G-IDLE: a request starts at second 15 to 590 less its budget, and ends by second 590
[2026-10-11T14:50:50Z]   ok  idle_wait and band_wait: now where the second allows, else the next allowed second
[2026-10-11T14:50:50Z]   ok  a request longer than the idle stretch stops the run
[2026-10-11T14:50:50Z]   ok  this TZ's tags, which TZ-27's rule does not cover
[2026-10-11T14:50:50Z]   ok  the Release is created at the run's commit, published, never the latest
[2026-10-11T14:50:50Z]   ok  the ledger: a run without a terminal record is resumed; a halt holds until a clear
[2026-10-11T14:50:50Z]   ok  the run writes under its state alone, reads the store where TZ-27 did, and starts no process in inventory or delete
[2026-10-11T14:50:50Z]   ok  btc-pairbook-archive.service: 9 of its lines as this file runs them
[2026-10-11T14:50:50Z]   ok  btc-pairbook-archive.timer: 5 of its lines as this file runs them
[2026-10-11T14:50:50Z]   ok  128M and 6h in bytes and seconds
[2026-10-11T14:50:50Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 80, "resumed": false, "run": 1791750680, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791750680000000000}
[2026-10-11T14:50:50Z] MemAvailable 300000000 bytes, floor 106086400; free 12931072000 bytes, floor 2001000000
[2026-10-11T14:50:50Z] W 1791747000 2026-10-11T19:30:00Z closed   stream files 1, 70001 bytes, taken 1
[2026-10-11T14:50:50Z] W 1791747900 2026-10-11T19:45:00Z closed   stream files 2, 83333 bytes, taken 2
[2026-10-11T14:50:50Z] W 1791748800 2026-10-11T20:00:00Z closed   stream files 1, 40000 bytes, taken 1
[2026-10-11T14:50:50Z] W 1791749700 2026-10-11T20:15:00Z unclosed stream files 1, 777 bytes, taken 0
[2026-10-11T14:50:50Z] S 1791747000-stream.jsonl.gz 70001 6d28a73c9429e5dcf2525e673882c74c846b1dbcfa31bb30eacd33a17749983d
[2026-10-11T14:50:50Z] S 1791747900-stream.jsonl.gz 50000 9bf005593c42ea8192b21fdc8fc1cf597c59a85b21c1dbef75235b6e9c91c09c
[2026-10-11T14:50:50Z] S 1791747900-stream.1.jsonl.gz 33333 dbd714a8c02f30b93b24be83fb2594005e6f4718c3fb5e6edd080e1b02d1c608
[2026-10-11T14:50:50Z] S 1791748800-stream.jsonl.gz 40000 e184f63a14502d190239d902248c83c9743305068e6b6fbf90a61978cca2fe7c
[2026-10-11T14:50:50Z] L {"assets_n": 4, "bytes_total": 193334, "closed": 3, "deferred": 0, "event": "set", "first_T": 1791747000, "last_T": 1791748800, "open": 0, "run": 1791750680, "sha256": "abc29447f3a7358fd71a67765d2259a7a0bc6d145fdb33987c58f416f104232a", "tag": "pairbook-streams-1791750680", "unclosed": 1, "wall_ns": 1791750680000000000, "windows_considered": 4}
[2026-10-11T14:50:50Z] credential: the selftest's
[2026-10-11T14:50:50Z] created the Release on pairbook-streams-1791750680, id 100
[2026-10-11T14:50:50Z] U {"action": "uploaded", "asset": "1791747000-stream.jsonl.gz", "at": "2026-10-11T20:31:20Z", "bytes": 70001, "digest": "sha256:6d28a73c9429e5dcf2525e673882c74c846b1dbcfa31bb30eacd33a17749983d", "id": 101, "sha256": "6d28a73c9429e5dcf2525e673882c74c846b1dbcfa31bb30eacd33a17749983d"}
[2026-10-11T14:50:50Z] U {"action": "uploaded", "asset": "1791747900-stream.jsonl.gz", "at": "2026-10-11T20:31:20Z", "bytes": 50000, "digest": "sha256:9bf005593c42ea8192b21fdc8fc1cf597c59a85b21c1dbef75235b6e9c91c09c", "id": 102, "sha256": "9bf005593c42ea8192b21fdc8fc1cf597c59a85b21c1dbef75235b6e9c91c09c"}
[2026-10-11T14:50:50Z] U {"action": "uploaded", "asset": "1791747900-stream.1.jsonl.gz", "at": "2026-10-11T20:31:20Z", "bytes": 33333, "digest": "sha256:dbd714a8c02f30b93b24be83fb2594005e6f4718c3fb5e6edd080e1b02d1c608", "id": 103, "sha256": "dbd714a8c02f30b93b24be83fb2594005e6f4718c3fb5e6edd080e1b02d1c608"}
[2026-10-11T14:50:50Z] U {"action": "uploaded", "asset": "1791748800-stream.jsonl.gz", "at": "2026-10-11T20:31:20Z", "bytes": 40000, "digest": "sha256:e184f63a14502d190239d902248c83c9743305068e6b6fbf90a61978cca2fe7c", "id": 104, "sha256": "e184f63a14502d190239d902248c83c9743305068e6b6fbf90a61978cca2fe7c"}
[2026-10-11T14:50:50Z] U {"action": "complete", "assets": 4, "at": "2026-10-11T20:31:20Z", "credential": "the selftest's", "held": 0, "release_id": 100, "sent": 4, "wall_ns": 1791750680000000000}
[2026-10-11T14:50:50Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 100, "run": 1791750680, "sent": 4, "wall_ns": 1791750680000000000}
[2026-10-11T14:50:50Z] D 1791747000-stream.jsonl.gz equal bytes 70001 sha256 6d28a73c9429e5dcf2525e673882c74c846b1dbcfa31bb30eacd33a17749983d
[2026-10-11T14:50:50Z] D 1791747900-stream.jsonl.gz equal bytes 50000 sha256 9bf005593c42ea8192b21fdc8fc1cf597c59a85b21c1dbef75235b6e9c91c09c
[2026-10-11T14:50:50Z] D 1791747900-stream.1.jsonl.gz equal bytes 33333 sha256 dbd714a8c02f30b93b24be83fb2594005e6f4718c3fb5e6edd080e1b02d1c608
[2026-10-11T14:50:50Z] D 1791748800-stream.jsonl.gz equal bytes 40000 sha256 e184f63a14502d190239d902248c83c9743305068e6b6fbf90a61978cca2fe7c
[2026-10-11T14:50:50Z] V 1791747000-stream.jsonl.gz id 101 state uploaded api True bytes 70001 digest sha256:6d28a73c9429e5dcf2525e673882c74c846b1dbcfa31bb30eacd33a17749983d url True download True
[2026-10-11T14:50:50Z] V 1791747900-stream.jsonl.gz id 102 state uploaded api True bytes 50000 digest sha256:9bf005593c42ea8192b21fdc8fc1cf597c59a85b21c1dbef75235b6e9c91c09c url True download True
[2026-10-11T14:50:50Z] V 1791747900-stream.1.jsonl.gz id 103 state uploaded api True bytes 33333 digest sha256:dbd714a8c02f30b93b24be83fb2594005e6f4718c3fb5e6edd080e1b02d1c608 url True download True
[2026-10-11T14:50:50Z] V 1791748800-stream.jsonl.gz id 104 state uploaded api True bytes 40000 digest sha256:e184f63a14502d190239d902248c83c9743305068e6b6fbf90a61978cca2fe7c url True download True
[2026-10-11T14:50:50Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-11T14:50:50Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-11T14:50:50Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-11T14:50:50Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-11T14:50:50Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-11T14:50:50Z] L {"assets_n": 4, "bytes_total": 193334, "event": "verify", "release_id": 100, "run": 1791750680, "verify_sha256": "5cddecf2f42b94df92671827f03f48f873f94220ae0ead9e9c2bbad34beeb65f", "wall_ns": 1791750800500000000}
[2026-10-11T14:50:50Z] X 1791747000-stream.jsonl.gz 70001 6d28a73c9429e5dcf2525e673882c74c846b1dbcfa31bb30eacd33a17749983d removed
[2026-10-11T14:50:50Z] X 1791747900-stream.jsonl.gz 50000 9bf005593c42ea8192b21fdc8fc1cf597c59a85b21c1dbef75235b6e9c91c09c removed
[2026-10-11T14:50:50Z] X 1791747900-stream.1.jsonl.gz 33333 dbd714a8c02f30b93b24be83fb2594005e6f4718c3fb5e6edd080e1b02d1c608 removed
[2026-10-11T14:50:50Z] X 1791748800-stream.jsonl.gz 40000 e184f63a14502d190239d902248c83c9743305068e6b6fbf90a61978cca2fe7c removed
[2026-10-11T14:50:50Z] G-DELETE every file of the set absent         True
[2026-10-11T14:50:50Z] G-DELETE each removal recorded by delete      True
[2026-10-11T14:50:50Z] G-DELETE each window keeps its window.json    True
[2026-10-11T14:50:50Z] L {"already": 0, "event": "delete", "free_after": 12931072000, "free_before": 12931072000, "freed": 193334, "gone": 4, "removed": 4, "run": 1791750680, "wall_ns": 1791750800500000000, "windows_kept": 3}
[2026-10-11T14:50:50Z] L {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "815823", "NRestarts": "2", "ns": 1791750800500000000}, "phase": 200, "run": 1791750680, "wall_ns": 1791750800500000000}
[2026-10-11T14:50:50Z] L {"event": "kill", "exit": 0, "phase": 200, "run": 1791750680, "wall_ns": 1791750800500000000}
[2026-10-11T14:50:50Z] G-RESTART a stop of the marked process   True
[2026-10-11T14:50:50Z] G-RESTART stopped inside the band        True
[2026-10-11T14:50:50Z] G-RESTART a start of another process     True
[2026-10-11T14:50:50Z] G-RESTART within 60 s                    True
[2026-10-11T14:50:50Z] G-RESTART the same code                  True
[2026-10-11T14:50:50Z] G-COUNTER started before its window's documents    True
[2026-10-11T14:50:50Z] G-COUNTER the counter equals the store             True
[2026-10-11T14:50:50Z] G-COUNTER the counter below the cap                True
[2026-10-11T14:50:50Z] G-COUNTER no file of the set left                  True
[2026-10-11T14:50:50Z] G-UNIT active                   True
[2026-10-11T14:50:50Z] G-UNIT argv                     True
[2026-10-11T14:50:50Z] G-UNIT sole instance            True
[2026-10-11T14:50:50Z] G-UNIT restarts                 True
[2026-10-11T14:50:50Z] G-UNIT the new start's process  True
[2026-10-11T14:50:50Z] L {"NRestarts": "3", "W": 1791750600, "event": "restart", "free_bytes": 12931072000, "gap_ns": 5400000000, "pid": 815824, "run": 1791750680, "stopped": 815823, "stream_bytes": 777, "wall_ns": 1791750830500000000}
[2026-10-11T14:50:50Z] window 1791750600: pid 815824, documents True; stream opened True, off_reason None, files ['stream.jsonl.gz'], segments None, frames None, stored_bytes None
[2026-10-11T14:50:50Z] G-RESUME run by the restarted process   True
[2026-10-11T14:50:50Z] G-RESUME the stream opened              True
[2026-10-11T14:50:50Z] G-RESUME no reason to keep it off       True
[2026-10-11T14:50:50Z] G-RESUME a stream file                  True
[2026-10-11T14:50:50Z] L {"T": 1791750600, "event": "resume", "reading": "PASS", "run": 1791750680, "wall_ns": 1791751541000000000}
[2026-10-11T14:50:50Z] at the set's rate the cap stops the streams in 1293.10 days, at 2030-04-26T23:08:02Z
[2026-10-11T14:50:50Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 169.68 days, at 2027-03-30T13:11:41Z
[2026-10-11T14:50:50Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 43.47 days, at 2026-11-24T08:03:51Z
[2026-10-11T14:50:50Z] L {"assets_n": 4, "bytes_total": 193334, "ended_outside": 0, "event": "complete", "free_bytes": 12931072000, "peak_rss": 37154816, "rate_per_day": 6186688, "requests": 13, "run": 1791750680, "started_outside": 0, "stops": [["the cap", 1903475282], ["the floor, base 43500000 bytes a day", 1806412301], ["the floor, base 187760570 bytes a day", 1795507431]], "store_stream_bytes": 777, "wall_ns": 1791751541000000000}
[2026-10-11T14:50:50Z] COMPLETE: run 1791750680, 4 files, 193334 bytes, Release pairbook-streams-1791750680
[2026-10-11T14:50:50Z]   ok  a run: every step recorded, in order, exit 0
[2026-10-11T14:50:50Z]   ok  the set: TZ-27's rule as of the run's start, under this TZ's tag
[2026-10-11T14:50:50Z]   ok  the Release holds the set's four files, byte for byte
[2026-10-11T14:50:50Z]   ok  the store: the set's files gone, every other entry kept
[2026-10-11T14:50:50Z]   ok  the restart inside its band, its counter the store's, and the stream resumed
[2026-10-11T14:50:50Z]   ok  every request timed and inside the idle stretch; reads with no token, every request under TZ-27's agent
[2026-10-11T14:50:50Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 341, "resumed": false, "run": 1791751841, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791751841000000000}
[2026-10-11T14:50:50Z] MemAvailable 300000000 bytes, floor 106086400; free 12931072000 bytes, floor 2001000000
[2026-10-11T14:50:50Z] W 1791747000 2026-10-11T19:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T14:50:50Z] W 1791747900 2026-10-11T19:45:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T14:50:50Z] W 1791748800 2026-10-11T20:00:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T14:50:50Z] W 1791749700 2026-10-11T20:15:00Z unclosed stream files 1, 777 bytes, taken 0
[2026-10-11T14:50:50Z] W 1791750600 2026-10-11T20:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T14:50:50Z] L {"closed": 4, "deferred": 0, "event": "empty", "open": 0, "run": 1791751841, "unclosed": 1, "wall_ns": 1791751841000000000, "windows_considered": 5}
[2026-10-11T14:50:50Z] EMPTY: no stream file of a closed window as of 1791751841
[2026-10-11T14:50:50Z]   ok  a run with nothing closed records empty and exits 0
[2026-10-11T14:50:50Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 588, "resumed": false, "run": 1791837588, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791837588000000000}
[2026-10-11T14:50:50Z] MemAvailable 300000000 bytes, floor 106086400; free 12931072000 bytes, floor 2001000000
[2026-10-11T14:50:50Z] W 1791747000 2026-10-11T19:30:00Z closed   stream files 1, 1000 bytes, taken 1
[2026-10-11T14:50:50Z] S 1791747000-stream.jsonl.gz 1000 24e3b9c19c0cfc60ff878b5f6be44b2c45d01fe79978ec4127247716eb0707e0
[2026-10-11T14:50:50Z] L {"assets_n": 1, "bytes_total": 1000, "closed": 1, "deferred": 0, "event": "set", "first_T": 1791747000, "last_T": 1791747000, "open": 0, "run": 1791837588, "sha256": "16923572f299594b6294f3586bfaa9e02fae973445455597e39353aad784d02a", "tag": "pairbook-streams-1791837588", "unclosed": 0, "wall_ns": 1791837588000000000, "windows_considered": 1}
[2026-10-11T14:50:50Z] L {"count": 1, "event": "deferred", "phase": "upload", "reason": "AssertionError: UPLOAD REFUSED: no credential (selftest)", "run": 1791837588, "wall_ns": 1791837588000000000}
[2026-10-11T14:50:50Z] DEFERRED in upload, 1 of 3: AssertionError: UPLOAD REFUSED: no credential (selftest); nothing removed, the next run resumes this set
[2026-10-11T14:50:50Z]   ok  a refused credential: deferred, exit 75, nothing removed
[2026-10-11T14:50:50Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 588, "resumed": true, "run": 1791837588, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791923988000000000}
[2026-10-11T14:50:50Z] MemAvailable 300000000 bytes, floor 106086400; free 12931072000 bytes, floor 2001000000
[2026-10-11T14:50:50Z] credential: the selftest's
[2026-10-11T14:50:50Z] created the Release on pairbook-streams-1791837588, id 105
[2026-10-11T14:50:50Z] U {"action": "uploaded", "asset": "1791747000-stream.jsonl.gz", "at": "2026-10-13T20:45:15Z", "bytes": 1000, "digest": "sha256:24e3b9c19c0cfc60ff878b5f6be44b2c45d01fe79978ec4127247716eb0707e0", "id": 106, "sha256": "24e3b9c19c0cfc60ff878b5f6be44b2c45d01fe79978ec4127247716eb0707e0"}
[2026-10-11T14:50:50Z] U {"action": "complete", "assets": 1, "at": "2026-10-13T20:45:15Z", "credential": "the selftest's", "held": 0, "release_id": 105, "sent": 1, "wall_ns": 1791924315000000000}
[2026-10-11T14:50:50Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 105, "run": 1791837588, "sent": 1, "wall_ns": 1791924315000000000}
[2026-10-11T14:50:50Z] D 1791747000-stream.jsonl.gz equal bytes 1000 sha256 24e3b9c19c0cfc60ff878b5f6be44b2c45d01fe79978ec4127247716eb0707e0
[2026-10-11T14:50:50Z] V 1791747000-stream.jsonl.gz id 106 state uploaded api True bytes 1000 digest sha256:24e3b9c19c0cfc60ff878b5f6be44b2c45d01fe79978ec4127247716eb0707e0 url True download True
[2026-10-11T14:50:50Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-11T14:50:50Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-11T14:50:50Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-11T14:50:50Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-11T14:50:50Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-11T14:50:50Z] L {"assets_n": 1, "bytes_total": 1000, "event": "verify", "release_id": 105, "run": 1791837588, "verify_sha256": "611cba00695b7d2dc701d40ad2a67a811cc64ee037ae5850b16e1427f60da2c7", "wall_ns": 1791924435500000000}
[2026-10-11T14:50:50Z] X 1791747000-stream.jsonl.gz 1000 24e3b9c19c0cfc60ff878b5f6be44b2c45d01fe79978ec4127247716eb0707e0 removed
[2026-10-11T14:50:50Z] G-DELETE every file of the set absent         True
[2026-10-11T14:50:50Z] G-DELETE each removal recorded by delete      True
[2026-10-11T14:50:50Z] G-DELETE each window keeps its window.json    True
[2026-10-11T14:50:50Z] L {"already": 0, "event": "delete", "free_after": 12931072000, "free_before": 12931072000, "freed": 1000, "gone": 1, "removed": 1, "run": 1791837588, "wall_ns": 1791924435500000000, "windows_kept": 1}
[2026-10-11T14:50:50Z] L {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "815823", "NRestarts": "2", "ns": 1791924435500000000}, "phase": 135, "run": 1791837588, "wall_ns": 1791924435500000000}
[2026-10-11T14:50:50Z] L {"event": "kill", "exit": 0, "phase": 135, "run": 1791837588, "wall_ns": 1791924435500000000}
[2026-10-11T14:50:50Z] G-RESTART a stop of the marked process   True
[2026-10-11T14:50:50Z] G-RESTART stopped inside the band        True
[2026-10-11T14:50:50Z] G-RESTART a start of another process     True
[2026-10-11T14:50:50Z] G-RESTART within 60 s                    True
[2026-10-11T14:50:50Z] G-RESTART the same code                  True
[2026-10-11T14:50:50Z] G-COUNTER started before its window's documents    True
[2026-10-11T14:50:50Z] G-COUNTER the counter equals the store             True
[2026-10-11T14:50:50Z] G-COUNTER the counter below the cap                True
[2026-10-11T14:50:50Z] G-COUNTER no file of the set left                  True
[2026-10-11T14:50:50Z] G-UNIT active                   True
[2026-10-11T14:50:50Z] G-UNIT argv                     True
[2026-10-11T14:50:50Z] G-UNIT sole instance            True
[2026-10-11T14:50:50Z] G-UNIT restarts                 True
[2026-10-11T14:50:50Z] G-UNIT the new start's process  True
[2026-10-11T14:50:50Z] L {"NRestarts": "3", "W": 1791924300, "event": "restart", "free_bytes": 12931072000, "gap_ns": 5400000000, "pid": 815824, "run": 1791837588, "stopped": 815823, "stream_bytes": 0, "wall_ns": 1791924465500000000}
[2026-10-11T14:50:50Z] window 1791924300: pid 815824, documents True; stream opened True, off_reason None, files ['stream.jsonl.gz'], segments None, frames None, stored_bytes None
[2026-10-11T14:50:50Z] G-RESUME run by the restarted process   True
[2026-10-11T14:50:50Z] G-RESUME the stream opened              True
[2026-10-11T14:50:50Z] G-RESUME no reason to keep it off       True
[2026-10-11T14:50:50Z] G-RESUME a stream file                  True
[2026-10-11T14:50:50Z] L {"T": 1791924300, "event": "resume", "reading": "PASS", "run": 1791837588, "wall_ns": 1791925241000000000}
[2026-10-11T14:50:50Z] at the set's rate the cap stops the streams in 83333.33 days, at 2254-12-11T05:00:41Z
[2026-10-11T14:50:50Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 193.39 days, at 2027-04-25T06:23:39Z
[2026-10-11T14:50:50Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 44.88 days, at 2026-11-27T18:08:24Z
[2026-10-11T14:50:50Z] L {"assets_n": 1, "bytes_total": 1000, "ended_outside": 0, "event": "complete", "free_bytes": 12931072000, "peak_rss": 37154816, "rate_per_day": 96000, "requests": 7, "run": 1791837588, "started_outside": 0, "stops": [["the cap", 8991925241], ["the floor, base 43500000 bytes a day", 1808634219], ["the floor, base 187760570 bytes a day", 1795802904]], "store_stream_bytes": 0, "wall_ns": 1791925241000000000}
[2026-10-11T14:50:50Z] COMPLETE: run 1791837588, 1 files, 1000 bytes, Release pairbook-streams-1791837588
[2026-10-11T14:50:50Z]   ok  the next run resumes the deferred set and completes it
[2026-10-11T14:50:50Z]   ok  a request due at second 588 waits for the next idle stretch
[2026-10-11T14:50:50Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": false, "run": 1792009820, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792009820000000000}
[2026-10-11T14:50:50Z] MemAvailable 300000000 bytes, floor 106086400; free 12931072000 bytes, floor 2001000000
[2026-10-11T14:50:50Z] W 1791747000 2026-10-11T19:30:00Z closed   stream files 1, 1000 bytes, taken 1
[2026-10-11T14:50:50Z] S 1791747000-stream.jsonl.gz 1000 24e3b9c19c0cfc60ff878b5f6be44b2c45d01fe79978ec4127247716eb0707e0
[2026-10-11T14:50:50Z] L {"assets_n": 1, "bytes_total": 1000, "closed": 1, "deferred": 0, "event": "set", "first_T": 1791747000, "last_T": 1791747000, "open": 0, "run": 1792009820, "sha256": "36ebb89e7316139b9b54a00f066bb79f56e6d372c38441b936c56ab6310de545", "tag": "pairbook-streams-1792009820", "unclosed": 0, "wall_ns": 1792009820000000000, "windows_considered": 1}
[2026-10-11T14:50:50Z] L {"count": 1, "event": "deferred", "phase": "upload", "reason": "AssertionError: UPLOAD REFUSED: no credential (selftest)", "run": 1792009820, "wall_ns": 1792009820000000000}
[2026-10-11T14:50:50Z] DEFERRED in upload, 1 of 3: AssertionError: UPLOAD REFUSED: no credential (selftest); nothing removed, the next run resumes this set
[2026-10-11T14:50:50Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": true, "run": 1792009820, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792009820000000000}
[2026-10-11T14:50:50Z] MemAvailable 300000000 bytes, floor 106086400; free 12931072000 bytes, floor 2001000000
[2026-10-11T14:50:50Z] L {"count": 2, "event": "deferred", "phase": "upload", "reason": "AssertionError: UPLOAD REFUSED: no credential (selftest)", "run": 1792009820, "wall_ns": 1792009820000000000}
[2026-10-11T14:50:50Z] DEFERRED in upload, 2 of 3: AssertionError: UPLOAD REFUSED: no credential (selftest); nothing removed, the next run resumes this set
[2026-10-11T14:50:50Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": true, "run": 1792009820, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792009820000000000}
[2026-10-11T14:50:50Z] MemAvailable 300000000 bytes, floor 106086400; free 12931072000 bytes, floor 2001000000
[2026-10-11T14:50:50Z] L {"event": "halt", "phase": "upload", "reason": "deferral 3 of 3: AssertionError: UPLOAD REFUSED: no credential (selftest)", "run": 1792009820, "wall_ns": 1792009820000000000}
[2026-10-11T14:50:50Z] L {"event": "timer-disabled", "exit": 0, "run": 1792009820, "wall_ns": 1792009820000000000}
[2026-10-11T14:50:50Z] HALTED in upload: deferral 3 of 3: AssertionError: UPLOAD REFUSED: no credential (selftest); the timer disabled, exit 0
[2026-10-11T14:50:50Z]   ok  the third deferral of one set halts, and the run disables its timer
[2026-10-11T14:50:50Z] HALTED since run 1792009820, upload: deferral 3 of 3: AssertionError: UPLOAD REFUSED: no credential (selftest); nothing done
[2026-10-11T14:50:50Z] L {"event": "refused", "exit": 0, "run": 1792009820, "wall_ns": 1792009820000000000}
[2026-10-11T14:50:50Z]   ok  a halted archive refuses the next run, and removes nothing
[2026-10-11T14:50:50Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 80, "resumed": false, "run": 1792009880, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792009880000000000}
[2026-10-11T14:50:50Z] MemAvailable 300000000 bytes, floor 106086400; free 12931072000 bytes, floor 2001000000
[2026-10-11T14:50:50Z] W 1791747000 2026-10-11T19:30:00Z closed   stream files 1, 1000 bytes, taken 1
[2026-10-11T14:50:50Z] S 1791747000-stream.jsonl.gz 1000 24e3b9c19c0cfc60ff878b5f6be44b2c45d01fe79978ec4127247716eb0707e0
[2026-10-11T14:50:50Z] L {"assets_n": 1, "bytes_total": 1000, "closed": 1, "deferred": 0, "event": "set", "first_T": 1791747000, "last_T": 1791747000, "open": 0, "run": 1792009880, "sha256": "e635adda595d15180295d887bb58fc0492e0e5f09f3fd06aaa8644c900fb5b54", "tag": "pairbook-streams-1792009880", "unclosed": 0, "wall_ns": 1792009880000000000, "windows_considered": 1}
[2026-10-11T14:50:50Z] credential: the selftest's
[2026-10-11T14:50:50Z] created the Release on pairbook-streams-1792009880, id 107
[2026-10-11T14:50:50Z] U {"action": "uploaded", "asset": "1791747000-stream.jsonl.gz", "at": "2026-10-14T20:31:20Z", "bytes": 1000, "digest": "sha256:24e3b9c19c0cfc60ff878b5f6be44b2c45d01fe79978ec4127247716eb0707e0", "id": 108, "sha256": "24e3b9c19c0cfc60ff878b5f6be44b2c45d01fe79978ec4127247716eb0707e0"}
[2026-10-11T14:50:50Z] U {"action": "complete", "assets": 1, "at": "2026-10-14T20:31:20Z", "credential": "the selftest's", "held": 0, "release_id": 107, "sent": 1, "wall_ns": 1792009880000000000}
[2026-10-11T14:50:50Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 107, "run": 1792009880, "sent": 1, "wall_ns": 1792009880000000000}
[2026-10-11T14:50:51Z] D 1791747000-stream.jsonl.gz equal bytes 1000 sha256 24e3b9c19c0cfc60ff878b5f6be44b2c45d01fe79978ec4127247716eb0707e0
[2026-10-11T14:50:51Z] V 1791747000-stream.jsonl.gz id 108 state uploaded api True bytes 1000 digest sha256:24e3b9c19c0cfc60ff878b5f6be44b2c45d01fe79978ec4127247716eb0707e0 url True download True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-11T14:50:51Z] L {"assets_n": 1, "bytes_total": 1000, "event": "verify", "release_id": 107, "run": 1792009880, "verify_sha256": "af9106973220214fcb66757222049a8647ead4b465ac67b46483577174771876", "wall_ns": 1792010000500000000}
[2026-10-11T14:50:51Z] X 1791747000-stream.jsonl.gz 1000 24e3b9c19c0cfc60ff878b5f6be44b2c45d01fe79978ec4127247716eb0707e0 removed
[2026-10-11T14:50:51Z] G-DELETE every file of the set absent         True
[2026-10-11T14:50:51Z] G-DELETE each removal recorded by delete      True
[2026-10-11T14:50:51Z] G-DELETE each window keeps its window.json    True
[2026-10-11T14:50:51Z] L {"already": 0, "event": "delete", "free_after": 12931072000, "free_before": 12931072000, "freed": 1000, "gone": 1, "removed": 1, "run": 1792009880, "wall_ns": 1792010000500000000, "windows_kept": 1}
[2026-10-11T14:50:51Z] L {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "815823", "NRestarts": "2", "ns": 1792010000500000000}, "phase": 200, "run": 1792009880, "wall_ns": 1792010000500000000}
[2026-10-11T14:50:51Z] L {"event": "kill", "exit": 0, "phase": 200, "run": 1792009880, "wall_ns": 1792010000500000000}
[2026-10-11T14:50:51Z] G-RESTART a stop of the marked process   True
[2026-10-11T14:50:51Z] G-RESTART stopped inside the band        True
[2026-10-11T14:50:51Z] G-RESTART a start of another process     True
[2026-10-11T14:50:51Z] G-RESTART within 60 s                    True
[2026-10-11T14:50:51Z] G-RESTART the same code                  True
[2026-10-11T14:50:51Z] G-COUNTER started before its window's documents    True
[2026-10-11T14:50:51Z] G-COUNTER the counter equals the store             True
[2026-10-11T14:50:51Z] G-COUNTER the counter below the cap                True
[2026-10-11T14:50:51Z] G-COUNTER no file of the set left                  True
[2026-10-11T14:50:51Z] G-UNIT active                   True
[2026-10-11T14:50:51Z] G-UNIT argv                     True
[2026-10-11T14:50:51Z] G-UNIT sole instance            True
[2026-10-11T14:50:51Z] G-UNIT restarts                 True
[2026-10-11T14:50:51Z] G-UNIT the new start's process  True
[2026-10-11T14:50:51Z] L {"NRestarts": "3", "W": 1792009800, "event": "restart", "free_bytes": 12931072000, "gap_ns": 5400000000, "pid": 815824, "run": 1792009880, "stopped": 815823, "stream_bytes": 0, "wall_ns": 1792010030500000000}
[2026-10-11T14:50:51Z] window 1792009800: pid 815824, documents True; stream opened True, off_reason None, files ['stream.jsonl.gz'], segments None, frames None, stored_bytes None
[2026-10-11T14:50:51Z] G-RESUME run by the restarted process   True
[2026-10-11T14:50:51Z] G-RESUME the stream opened              True
[2026-10-11T14:50:51Z] G-RESUME no reason to keep it off       True
[2026-10-11T14:50:51Z] G-RESUME a stream file                  True
[2026-10-11T14:50:51Z] L {"T": 1792009800, "event": "resume", "reading": "PASS", "run": 1792009880, "wall_ns": 1792010741000000000}
[2026-10-11T14:50:51Z] at the set's rate the cap stops the streams in 83333.33 days, at 2254-12-12T04:45:41Z
[2026-10-11T14:50:51Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 193.39 days, at 2027-04-26T06:08:39Z
[2026-10-11T14:50:51Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 44.88 days, at 2026-11-28T17:53:24Z
[2026-10-11T14:50:51Z] L {"assets_n": 1, "bytes_total": 1000, "ended_outside": 0, "event": "complete", "free_bytes": 12931072000, "peak_rss": 37154816, "rate_per_day": 96000, "requests": 7, "run": 1792009880, "started_outside": 0, "stops": [["the cap", 8992010741], ["the floor, base 43500000 bytes a day", 1808719719], ["the floor, base 187760570 bytes a day", 1795888404]], "store_stream_bytes": 0, "wall_ns": 1792010741000000000}
[2026-10-11T14:50:51Z] COMPLETE: run 1792009880, 1 files, 1000 bytes, Release pairbook-streams-1792009880
[2026-10-11T14:50:51Z]   ok  after a clear the next run takes a new set
[2026-10-11T14:50:51Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": false, "run": 1792182620, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792182620000000000}
[2026-10-11T14:50:51Z] MemAvailable 300000000 bytes, floor 106086400; free 12931072000 bytes, floor 2001000000
[2026-10-11T14:50:51Z] W 1791747000 2026-10-11T19:30:00Z closed   stream files 2, 11000 bytes, taken 2
[2026-10-11T14:50:51Z] S 1791747000-stream.jsonl.gz 5000 a8e60280ae2b067cb50e53a600ea127d88dda70b75321de845deb479e3214f07
[2026-10-11T14:50:51Z] S 1791747000-stream.1.jsonl.gz 6000 af80e8d9825534706193b0672292751598d55e35a6976b184ac2e028cfef5f5e
[2026-10-11T14:50:51Z] L {"assets_n": 2, "bytes_total": 11000, "closed": 1, "deferred": 0, "event": "set", "first_T": 1791747000, "last_T": 1791747000, "open": 0, "run": 1792182620, "sha256": "a287371bd08949cfd2483ae4c2dd0b90180fd92b2f401b8661670e906dce589e", "tag": "pairbook-streams-1792182620", "unclosed": 0, "wall_ns": 1792182620000000000, "windows_considered": 1}
[2026-10-11T14:50:51Z] credential: the selftest's
[2026-10-11T14:50:51Z] created the Release on pairbook-streams-1792182620, id 109
[2026-10-11T14:50:51Z] U {"action": "uploaded", "asset": "1791747000-stream.jsonl.gz", "at": "2026-10-16T20:30:20Z", "bytes": 5000, "digest": "sha256:a8e60280ae2b067cb50e53a600ea127d88dda70b75321de845deb479e3214f07", "id": 110, "sha256": "a8e60280ae2b067cb50e53a600ea127d88dda70b75321de845deb479e3214f07"}
[2026-10-11T14:50:51Z] U {"action": "uploaded", "asset": "1791747000-stream.1.jsonl.gz", "at": "2026-10-16T20:30:20Z", "bytes": 6000, "digest": "sha256:af80e8d9825534706193b0672292751598d55e35a6976b184ac2e028cfef5f5e", "id": 111, "sha256": "af80e8d9825534706193b0672292751598d55e35a6976b184ac2e028cfef5f5e"}
[2026-10-11T14:50:51Z] U {"action": "complete", "assets": 2, "at": "2026-10-16T20:30:20Z", "credential": "the selftest's", "held": 0, "release_id": 109, "sent": 2, "wall_ns": 1792182620000000000}
[2026-10-11T14:50:51Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 109, "run": 1792182620, "sent": 2, "wall_ns": 1792182620000000000}
[2026-10-11T14:50:51Z] D 1791747000-stream.jsonl.gz equal bytes 5000 sha256 a8e60280ae2b067cb50e53a600ea127d88dda70b75321de845deb479e3214f07
[2026-10-11T14:50:51Z] D 1791747000-stream.1.jsonl.gz DIFFERS bytes 6000 sha256 f617a3529d841297ff8d75fa564fe02d8fb92564ab609c437260b7c2086727f0
[2026-10-11T14:50:51Z] V 1791747000-stream.jsonl.gz id 110 state uploaded api True bytes 5000 digest sha256:a8e60280ae2b067cb50e53a600ea127d88dda70b75321de845deb479e3214f07 url True download True
[2026-10-11T14:50:51Z] V 1791747000-stream.1.jsonl.gz id 111 state uploaded api True bytes 6000 digest sha256:af80e8d9825534706193b0672292751598d55e35a6976b184ac2e028cfef5f5e url True download False
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           False
[2026-10-11T14:50:51Z] L {"count": 1, "event": "deferred", "phase": "verify", "reason": "AssertionError: VERIFY FAIL: [\"every download the set's bytes and SHA-256\"]; missing []; beyond []", "run": 1792182620, "wall_ns": 1792182740500000000}
[2026-10-11T14:50:51Z] DEFERRED in verify, 1 of 3: AssertionError: VERIFY FAIL: ["every download the set's bytes and SHA-256"]; missing []; beyond []; nothing removed, the next run resumes this set
[2026-10-11T14:50:51Z]   ok  a flipped bit in one asset: VERIFY FAIL, deferred, nothing removed
[2026-10-11T14:50:51Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 140, "resumed": true, "run": 1792182620, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792182740500000000}
[2026-10-11T14:50:51Z] MemAvailable 300000000 bytes, floor 106086400; free 12931072000 bytes, floor 2001000000
[2026-10-11T14:50:51Z] credential: the selftest's
[2026-10-11T14:50:51Z] U {"action": "held", "asset": "1791747000-stream.jsonl.gz", "at": "2026-10-16T20:32:20Z", "id": 110}
[2026-10-11T14:50:51Z] U {"action": "held", "asset": "1791747000-stream.1.jsonl.gz", "at": "2026-10-16T20:32:20Z", "id": 111}
[2026-10-11T14:50:51Z] U {"action": "complete", "assets": 2, "at": "2026-10-16T20:32:20Z", "credential": "the selftest's", "held": 2, "release_id": 109, "sent": 0, "wall_ns": 1792182740500000000}
[2026-10-11T14:50:51Z] L {"created": false, "credential": "the selftest's", "event": "upload", "held": 2, "release_id": 109, "run": 1792182620, "sent": 0, "wall_ns": 1792182740500000000}
[2026-10-11T14:50:51Z] D 1791747000-stream.jsonl.gz equal bytes 5000 sha256 a8e60280ae2b067cb50e53a600ea127d88dda70b75321de845deb479e3214f07
[2026-10-11T14:50:51Z] D 1791747000-stream.1.jsonl.gz equal bytes 6000 sha256 af80e8d9825534706193b0672292751598d55e35a6976b184ac2e028cfef5f5e
[2026-10-11T14:50:51Z] V 1791747000-stream.jsonl.gz id 110 state uploaded api True bytes 5000 digest sha256:a8e60280ae2b067cb50e53a600ea127d88dda70b75321de845deb479e3214f07 url True download True
[2026-10-11T14:50:51Z] V 1791747000-stream.1.jsonl.gz id 111 state uploaded api True bytes 6000 digest sha256:af80e8d9825534706193b0672292751598d55e35a6976b184ac2e028cfef5f5e url True download True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-11T14:50:51Z] L {"assets_n": 2, "bytes_total": 11000, "event": "verify", "release_id": 109, "run": 1792182620, "verify_sha256": "e39d8815ccf679bddb4b9121e80a697e341d3db54edd34bc28001a31cc10155a", "wall_ns": 1792182861000000000}
[2026-10-11T14:50:51Z] X 1791747000-stream.jsonl.gz 5000 a8e60280ae2b067cb50e53a600ea127d88dda70b75321de845deb479e3214f07 removed
[2026-10-11T14:50:51Z] X 1791747000-stream.1.jsonl.gz 6000 af80e8d9825534706193b0672292751598d55e35a6976b184ac2e028cfef5f5e removed
[2026-10-11T14:50:51Z] G-DELETE every file of the set absent         True
[2026-10-11T14:50:51Z] G-DELETE each removal recorded by delete      True
[2026-10-11T14:50:51Z] G-DELETE each window keeps its window.json    True
[2026-10-11T14:50:51Z] L {"already": 0, "event": "delete", "free_after": 12931072000, "free_before": 12931072000, "freed": 11000, "gone": 2, "removed": 2, "run": 1792182620, "wall_ns": 1792182861000000000, "windows_kept": 1}
[2026-10-11T14:50:51Z] L {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "815823", "NRestarts": "2", "ns": 1792182861000000000}, "phase": 261, "run": 1792182620, "wall_ns": 1792182861000000000}
[2026-10-11T14:50:51Z] L {"event": "kill", "exit": 0, "phase": 261, "run": 1792182620, "wall_ns": 1792182861000000000}
[2026-10-11T14:50:51Z] G-RESTART a stop of the marked process   True
[2026-10-11T14:50:51Z] G-RESTART stopped inside the band        True
[2026-10-11T14:50:51Z] G-RESTART a start of another process     True
[2026-10-11T14:50:51Z] G-RESTART within 60 s                    True
[2026-10-11T14:50:51Z] G-RESTART the same code                  True
[2026-10-11T14:50:51Z] G-COUNTER started before its window's documents    True
[2026-10-11T14:50:51Z] G-COUNTER the counter equals the store             True
[2026-10-11T14:50:51Z] G-COUNTER the counter below the cap                True
[2026-10-11T14:50:51Z] G-COUNTER no file of the set left                  True
[2026-10-11T14:50:51Z] G-UNIT active                   True
[2026-10-11T14:50:51Z] G-UNIT argv                     True
[2026-10-11T14:50:51Z] G-UNIT sole instance            True
[2026-10-11T14:50:51Z] G-UNIT restarts                 True
[2026-10-11T14:50:51Z] G-UNIT the new start's process  True
[2026-10-11T14:50:51Z] L {"NRestarts": "3", "W": 1792182600, "event": "restart", "free_bytes": 12931072000, "gap_ns": 5400000000, "pid": 815824, "run": 1792182620, "stopped": 815823, "stream_bytes": 0, "wall_ns": 1792182891000000000}
[2026-10-11T14:50:51Z] window 1792182600: pid 815824, documents True; stream opened True, off_reason None, files ['stream.jsonl.gz'], segments None, frames None, stored_bytes None
[2026-10-11T14:50:51Z] G-RESUME run by the restarted process   True
[2026-10-11T14:50:51Z] G-RESUME the stream opened              True
[2026-10-11T14:50:51Z] G-RESUME no reason to keep it off       True
[2026-10-11T14:50:51Z] G-RESUME a stream file                  True
[2026-10-11T14:50:51Z] L {"T": 1792182600, "event": "resume", "reading": "PASS", "run": 1792182620, "wall_ns": 1792183541000000000}
[2026-10-11T14:50:51Z] at the set's rate the cap stops the streams in 7575.76 days, at 2047-07-14T14:56:35Z
[2026-10-11T14:50:51Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 189.22 days, at 2027-04-24T02:08:29Z
[2026-10-11T14:50:51Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 44.65 days, at 2026-11-30T12:24:49Z
[2026-10-11T14:50:51Z] L {"assets_n": 2, "bytes_total": 11000, "ended_outside": 0, "event": "complete", "free_bytes": 12931072000, "peak_rss": 37154816, "rate_per_day": 1056000, "requests": 15, "run": 1792182620, "started_outside": 0, "stops": [["the cap", 2446728995], ["the floor, base 43500000 bytes a day", 1808532509], ["the floor, base 187760570 bytes a day", 1796041489]], "store_stream_bytes": 0, "wall_ns": 1792183541000000000}
[2026-10-11T14:50:51Z] COMPLETE: run 1792182620, 2 files, 11000 bytes, Release pairbook-streams-1792182620
[2026-10-11T14:50:51Z]   ok  the asset mended, the next run verifies and completes
[2026-10-11T14:50:51Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": false, "run": 1792269020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792269020000000000}
[2026-10-11T14:50:51Z] MemAvailable 300000000 bytes, floor 106086400; free 12931072000 bytes, floor 2001000000
[2026-10-11T14:50:51Z] W 1791747000 2026-10-11T19:30:00Z closed   stream files 1, 2000 bytes, taken 1
[2026-10-11T14:50:51Z] S 1791747000-stream.jsonl.gz 2000 3881efecb6e5658814b161282056c454558bb0e2c5653a5f4a6b12245eb370f0
[2026-10-11T14:50:51Z] L {"assets_n": 1, "bytes_total": 2000, "closed": 1, "deferred": 0, "event": "set", "first_T": 1791747000, "last_T": 1791747000, "open": 0, "run": 1792269020, "sha256": "46c3cbfeebce28523780e60be17f1bb1dcbcd589be79544904067c1cfc4478bf", "tag": "pairbook-streams-1792269020", "unclosed": 0, "wall_ns": 1792269020000000000, "windows_considered": 1}
[2026-10-11T14:50:51Z] credential: the selftest's
[2026-10-11T14:50:51Z] created the Release on pairbook-streams-1792269020, id 112
[2026-10-11T14:50:51Z] U {"action": "uploaded", "asset": "1791747000-stream.jsonl.gz", "at": "2026-10-17T20:30:20Z", "bytes": 2000, "digest": "sha256:3881efecb6e5658814b161282056c454558bb0e2c5653a5f4a6b12245eb370f0", "id": 113, "sha256": "3881efecb6e5658814b161282056c454558bb0e2c5653a5f4a6b12245eb370f0"}
[2026-10-11T14:50:51Z] U {"action": "complete", "assets": 1, "at": "2026-10-17T20:30:20Z", "credential": "the selftest's", "held": 0, "release_id": 112, "sent": 1, "wall_ns": 1792269020000000000}
[2026-10-11T14:50:51Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 112, "run": 1792269020, "sent": 1, "wall_ns": 1792269020000000000}
[2026-10-11T14:50:51Z] D 1791747000-stream.jsonl.gz equal bytes 2000 sha256 3881efecb6e5658814b161282056c454558bb0e2c5653a5f4a6b12245eb370f0
[2026-10-11T14:50:51Z] V 1791747000-stream.jsonl.gz id 113 state uploaded api True bytes 2000 digest sha256:3881efecb6e5658814b161282056c454558bb0e2c5653a5f4a6b12245eb370f0 url True download True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-11T14:50:51Z] L {"assets_n": 1, "bytes_total": 2000, "event": "verify", "release_id": 112, "run": 1792269020, "verify_sha256": "c980ff7371f870f82206655423d2ab68e270437befe2d7ec160b56254b3ed75c", "wall_ns": 1792269140500000000}
[2026-10-11T14:50:51Z] X 1791747000-stream.jsonl.gz 2000 3881efecb6e5658814b161282056c454558bb0e2c5653a5f4a6b12245eb370f0 removed
[2026-10-11T14:50:51Z] G-DELETE every file of the set absent         True
[2026-10-11T14:50:51Z] G-DELETE each removal recorded by delete      True
[2026-10-11T14:50:51Z] G-DELETE each window keeps its window.json    True
[2026-10-11T14:50:51Z] L {"already": 0, "event": "delete", "free_after": 12931072000, "free_before": 12931072000, "freed": 2000, "gone": 1, "removed": 1, "run": 1792269020, "wall_ns": 1792269140500000000, "windows_kept": 1}
[2026-10-11T14:50:51Z] L {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "815823", "NRestarts": "2", "ns": 1792269140500000000}, "phase": 140, "run": 1792269020, "wall_ns": 1792269140500000000}
[2026-10-11T14:50:51Z] L {"event": "kill", "exit": 0, "phase": 140, "run": 1792269020, "wall_ns": 1792269140500000000}
[2026-10-11T14:50:51Z] G-RESTART a stop of the marked process   True
[2026-10-11T14:50:51Z] G-RESTART stopped inside the band        True
[2026-10-11T14:50:51Z] G-RESTART a start of another process     True
[2026-10-11T14:50:51Z] G-RESTART within 60 s                    True
[2026-10-11T14:50:51Z] G-RESTART the same code                  True
[2026-10-11T14:50:51Z] G-COUNTER started before its window's documents    True
[2026-10-11T14:50:51Z] G-COUNTER the counter equals the store             False
[2026-10-11T14:50:51Z] G-COUNTER the counter below the cap                True
[2026-10-11T14:50:51Z] G-COUNTER no file of the set left                  True
[2026-10-11T14:50:51Z] L {"event": "halt", "phase": "restart", "reason": "AssertionError: G-COUNTER FAIL: ['the counter equals the store']; left []", "run": 1792269020, "wall_ns": 1792269170500000000}
[2026-10-11T14:50:51Z] L {"event": "timer-disabled", "exit": 0, "run": 1792269020, "wall_ns": 1792269170500000000}
[2026-10-11T14:50:51Z] HALTED in restart: AssertionError: G-COUNTER FAIL: ['the counter equals the store']; left []; the timer disabled, exit 0
[2026-10-11T14:50:51Z]   ok  G-COUNTER FAIL after the removal: halted, the files already archived, the timer disabled
[2026-10-11T14:50:51Z] L {"commit": "cccccccccccccccccccccccccccccccccccccccc", "event": "start", "file_sha256": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", "invocation": "selftest", "phase_at": 20, "resumed": false, "run": 1792355420, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792355420000000000}
[2026-10-11T14:50:51Z] MemAvailable 300000000 bytes, floor 106086400; free 12931072000 bytes, floor 2001000000
[2026-10-11T14:50:51Z] W 1791747000 2026-10-11T19:30:00Z closed   stream files 1, 2000 bytes, taken 1
[2026-10-11T14:50:51Z] S 1791747000-stream.jsonl.gz 2000 3881efecb6e5658814b161282056c454558bb0e2c5653a5f4a6b12245eb370f0
[2026-10-11T14:50:51Z] L {"assets_n": 1, "bytes_total": 2000, "closed": 1, "deferred": 0, "event": "set", "first_T": 1791747000, "last_T": 1791747000, "open": 0, "run": 1792355420, "sha256": "918e685ec7cd27468d5c505471ddfbdbb2aa9b7ad18d3e201e26f50765bb8403", "tag": "pairbook-streams-1792355420", "unclosed": 0, "wall_ns": 1792355420000000000, "windows_considered": 1}
[2026-10-11T14:50:51Z] credential: the selftest's
[2026-10-11T14:50:51Z] created the Release on pairbook-streams-1792355420, id 114
[2026-10-11T14:50:51Z] U {"action": "uploaded", "asset": "1791747000-stream.jsonl.gz", "at": "2026-10-18T20:30:20Z", "bytes": 2000, "digest": "sha256:3881efecb6e5658814b161282056c454558bb0e2c5653a5f4a6b12245eb370f0", "id": 115, "sha256": "3881efecb6e5658814b161282056c454558bb0e2c5653a5f4a6b12245eb370f0"}
[2026-10-11T14:50:51Z] U {"action": "complete", "assets": 1, "at": "2026-10-18T20:30:20Z", "credential": "the selftest's", "held": 0, "release_id": 114, "sent": 1, "wall_ns": 1792355420000000000}
[2026-10-11T14:50:51Z] L {"created": true, "credential": "the selftest's", "event": "upload", "held": 0, "release_id": 114, "run": 1792355420, "sent": 1, "wall_ns": 1792355420000000000}
[2026-10-11T14:50:51Z] D 1791747000-stream.jsonl.gz equal bytes 2000 sha256 3881efecb6e5658814b161282056c454558bb0e2c5653a5f4a6b12245eb370f0
[2026-10-11T14:50:51Z] V 1791747000-stream.jsonl.gz id 115 state uploaded api True bytes 2000 digest sha256:3881efecb6e5658814b161282056c454558bb0e2c5653a5f4a6b12245eb370f0 url True download True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-11T14:50:51Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-11T14:50:51Z] L {"assets_n": 1, "bytes_total": 2000, "event": "verify", "release_id": 114, "run": 1792355420, "verify_sha256": "ee0d1065ed26a6d5c6fc70b59d4e950641b4e2d5d2f342596cb91de43c953d77", "wall_ns": 1792355540500000000}
[2026-10-11T14:50:51Z] X 1791747000-stream.jsonl.gz 2000 3881efecb6e5658814b161282056c454558bb0e2c5653a5f4a6b12245eb370f0 removed
[2026-10-11T14:50:51Z] G-DELETE every file of the set absent         True
[2026-10-11T14:50:51Z] G-DELETE each removal recorded by delete      True
[2026-10-11T14:50:51Z] G-DELETE each window keeps its window.json    True
[2026-10-11T14:50:51Z] L {"already": 0, "event": "delete", "free_after": 12931072000, "free_before": 12931072000, "freed": 2000, "gone": 1, "removed": 1, "run": 1792355420, "wall_ns": 1792355540500000000, "windows_kept": 1}
[2026-10-11T14:50:51Z] L {"event": "halt", "phase": "restart", "reason": "AssertionError: the pair book is 'failed': not restarted", "run": 1792355420, "wall_ns": 1792355540500000000}
[2026-10-11T14:50:51Z] L {"event": "timer-disabled", "exit": 0, "run": 1792355420, "wall_ns": 1792355540500000000}
[2026-10-11T14:50:51Z] HALTED in restart: AssertionError: the pair book is 'failed': not restarted; the timer disabled, exit 0
[2026-10-11T14:50:51Z]   ok  a pair book not active: the archive halts after its removal and signals nothing
[2026-10-11T14:50:51Z]   ok  the loopback server saw no credential but the run's
[2026-10-11T14:50:51Z]   ok  the temporary stores removed
[2026-10-11T14:50:51Z]   ok  imports: the standard library alone
[2026-10-11T14:50:51Z]   ok  no endpoint in this file's text: every request is TZ-27's
[2026-10-11T14:50:51Z] 34 of 34 checks passed
[2026-10-11T14:50:51Z] peak memory of this run: 41611264 bytes
[2026-10-11T14:50:51Z] opens refused: 0; store opens 0; requests 56, uploads 10, downloads 12 (221334 bytes); files removed 10
exit=0
```

### 2.3 §3.3 — the units, and the directories beside this session — `logs/14-still.log`, `logs/15-scratch.log`

```
[2026-10-11T14:50:56Z] btc-chainbook.service {'MainPID': '0', 'NRestarts': '0', 'ActiveState': 'inactive'}, MemoryCurrent [not set], MemoryPeak [not set]
[2026-10-11T14:50:56Z] btc-pairbook.service {'MainPID': '815823', 'NRestarts': '2', 'ActiveState': 'active'}, MemoryCurrent 2015232, MemoryPeak 76058624
[2026-10-11T14:50:56Z] btc-recorder.service {'MainPID': '4148534', 'NRestarts': '2', 'ActiveState': 'active'}, MemoryCurrent 112680960, MemoryPeak 206311424
[2026-10-11T14:50:56Z] still: the recorder recorded
[2026-10-11T14:50:56Z] peak memory of this run: 35983360 bytes
[2026-10-11T14:50:56Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

```
[2026-10-11T14:50:56Z] running 337573 started 2026-10-07T20:05:37Z claude
[2026-10-11T14:50:56Z] running 337576 started 2026-10-07T20:05:37Z claude
[2026-10-11T14:50:56Z] running 847634 started 2026-10-11T14:48:44Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-10-11T14:50:56Z] 6de9e261-2fb6-4db9-ae09-1fd283c3b8c8 born 2026-10-11T14:48:45Z: live, process [847634]
[2026-10-11T14:50:56Z] 70b5ba7a-7e9e-5c10-a353-278a1431d82a born 2026-10-11T08:17:34Z: earlier
[2026-10-11T14:50:56Z] 952e88f3-b9a6-4bd2-b674-b9deebd16088 born 2026-10-11T08:17:32Z: earlier
[2026-10-11T14:50:56Z] peak memory of this run: 35934208 bytes
[2026-10-11T14:50:56Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

### 2.4 §9 B-RECLAIM-SCRATCH — after §3.3, before §3.4 (V16, V17) — `logs/16-reclaim-scratch.log`, `logs/17-rm-scratch.log`

`I scratch` named two directories **earlier**: `70b5ba7a…` and `952e88f3…`, the TZ-27 pair map §3 names. It named one **live**: `6de9e261…`, born with process `847634`, which runs this session. The live directory was kept. One `I reclaim` named both earlier directories; then came one `rm -rf` and one `test -e` per directory. **The classifier refused neither.**

```
[2026-10-11T14:51:03Z] reclaim: 2153 report tokens; forensic store holds 1810 files
[2026-10-11T14:51:03Z] RECLAIM PASS: 4 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 1810 -> 1810 files
[2026-10-11T14:51:03Z] peak memory of this run: 35938304 bytes
[2026-10-11T14:51:03Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

```
2026-10-11T14:51:06Z
exit=0
exit=1
2026-10-11T14:51:09Z
exit=0
exit=1
```

### 2.5 §3.4 — P-PATH (V6): **served** — `logs/18-path.log`, verbatim

```
[2026-10-11T14:51:15Z] MemAvailable 305045504 bytes, floor 93454336
[2026-10-11T14:51:16Z] P-PATH release tz-01a-dataset id 385702977; asset twap-divergence-observations.parquet state uploaded, 76818669 bytes, digest sha256:229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b, url True
[2026-10-11T14:51:17Z] P-PATH download: status 200, 76818669 bytes, sha256 229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b
[2026-10-11T14:51:17Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/tags/tz-01a-dataset: 0 bytes, budget 5 s, second 375, 0.3 s, inside True True
[2026-10-11T14:51:17Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/385702977/assets: 0 bytes, budget 5 s, second 375, 0.2 s, inside True True
[2026-10-11T14:51:17Z] T download twap-divergence-observations.parquet: 76818669 bytes, budget 44 s, second 376, 1.4 s, inside True True
[2026-10-11T14:51:17Z] READING P-PATH: served - 3 requests through the run's own path, each inside the idle stretch; the digest present and equal; 76818669 bytes downloaded and equal
[2026-10-11T14:51:17Z] peak memory of this run: 38338560 bytes
[2026-10-11T14:51:17Z] opens refused: 0; store opens 0; requests 3, uploads 0, downloads 1 (76818669 bytes); files removed 0
exit=0
```

### 2.6 §3.5 — B-PATH-TOKEN (V7): **served**, run by the Boss — `logs/B-PATH-TOKEN.log`, verbatim, as `tee` wrote it

```
[2026-10-11T15:04:49Z] MemAvailable 299114496 bytes, floor 93454336
[2026-10-11T15:04:49Z] credential: the primary checkout's remote URL
[2026-10-11T15:04:49Z] repository: status 200, full_name 'seahomebatumi-ai/btc-5m-twap', push True
[2026-10-11T15:04:49Z] READING P-TOKEN: served - the credential from the primary checkout's remote URL reads seahomebatumi-ai/btc-5m-twap with push, and the Release 409534533; 2 requests
[2026-10-11T15:04:49Z] peak memory of this run: 37150720 bytes
[2026-10-11T15:04:49Z] opens refused: 0; store opens 0; requests 2, uploads 0, downloads 0 (0 bytes); files removed 0
```

The Boss ran this block in a root shell on the VPS at 15:04:49 UTC; it was his from the start (§3.5). His terminal printed the same six lines and then `exit=0`, which `tee` does not capture. The session read the log, which holds `READING P-TOKEN: served`. That line is printed only after every assert of the mode has held. The session never read, printed or stored the credential.

### 2.7 §3.6 — B-INSTALL and G-INSTALL (V8) — `logs/20-B-INSTALL.log`, `logs/21-installed.log`

B-INSTALL was run from the session at 15:05:24 UTC. **The classifier did not refuse it.** All seven commands printed `exit=0`.

```
2026-10-11T15:05:24Z
exit=0
exit=0
exit=0
exit=0
exit=0
exit=0
exit=0
```

```
[2026-10-11T15:05:34Z] /root/btc-pairbook-archive-svc/tz27-pairbook-archive.py sha256 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673; the branch's 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673
[2026-10-11T15:05:34Z] /root/btc-pairbook-archive-svc/tz28-pairbook-archive-timer.py sha256 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4; the branch's 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4
[2026-10-11T15:05:34Z] commit.txt d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3; the branch head d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3, its upstream d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
[2026-10-11T15:05:34Z] G-INSTALL commit.txt the branch head, pushed                                 True
[2026-10-11T15:05:34Z] G-INSTALL the service's copy of this file the branch's                       True
[2026-10-11T15:05:34Z] G-INSTALL the service's copy of TZ-27's file, 2cba96bc9d41                   True
[2026-10-11T15:05:34Z] G-INSTALL the two units byte for byte                                        True
[2026-10-11T15:05:34Z] G-INSTALL the state directory, root's, 0700, empty                           True
[2026-10-11T15:05:34Z] G-INSTALL the service loaded, inactive, static                               True
[2026-10-11T15:05:34Z] G-INSTALL the service a oneshot, Restart=no, 128M, 6h, its argv and directory True
[2026-10-11T15:05:34Z] G-INSTALL the timer loaded, inactive, disabled                               True
[2026-10-11T15:05:34Z] G-INSTALL PASS: 8 of 8
[2026-10-11T15:05:34Z] peak memory of this run: 35934208 bytes
[2026-10-11T15:05:34Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

### 2.8 §3.7 — the enable mark, B-ENABLE and G-TIMER (V9) — `logs/22-mark-enable.log`, `logs/23-B-ENABLE.log`, `logs/24-timer.log`

**The enable mark: 2026-10-11 15:05:39 UTC**, `ns` `1791731139112477547`. It was taken by the Executor before B-ENABLE was run or handed over.

```
[2026-10-11T15:05:39Z] mark enable at 2026-10-11T15:05:39Z: the timer {'ActiveState': 'inactive', 'UnitFileState': 'disabled'}, the service {'Result': 'success', 'ActiveState': 'inactive'}
[2026-10-11T15:05:39Z] peak memory of this run: 35979264 bytes
[2026-10-11T15:05:39Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

**B-ENABLE was refused by the session's classifier** ("[Auto-Mode Bypass]") at about 15:06 UTC, so nothing ran. **The Boss ran it verbatim** in a root shell on the VPS. Its band check printed `second of the day=54491`, which is 15:08:11 UTC, inside 11,100 to 73,200. The output below is his terminal output as pasted into the session. The timer's own `ActiveEnterTimestamp`, `Sun 2026-10-11 15:08:11 UTC`, read by `I timer`, verifies it.

```
B-ENABLE, run by the Boss in a root shell on the VPS (the session's classifier refused it as [Auto-Mode Bypass]); his terminal output, pasted into the session:
second of the day=54491
Created symlink /etc/systemd/system/timers.target.wants/btc-pairbook-archive.timer → /etc/systemd/system/btc-pairbook-archive.timer.
exit=0
```

`I timer` ran 23 s after B-ENABLE, within the 300 s bound:

```
[2026-10-11T15:08:34Z] the timer: {'Unit': 'btc-pairbook-archive.service', 'TimersMonotonic': '{ OnActiveUSec=10min ; next_elapse=2month 1w 2d 10h 53min 39.572424s }', 'TimersCalendar': '{ OnCalendar=*-*-* 03:00:20 UTC ; next_elapse=Mon 2026-10-12 03:00:20 UTC }', 'NextElapseUSecRealtime': 'Mon 2026-10-12 03:00:20 UTC', 'LastTriggerUSec': '', 'AccuracyUSec': '1s', 'LoadState': 'loaded', 'ActiveState': 'active', 'SubState': 'waiting', 'FragmentPath': '/etc/systemd/system/btc-pairbook-archive.timer', 'UnitFileState': 'enabled', 'ActiveEnterTimestamp': 'Sun 2026-10-11 15:08:11 UTC'}
[2026-10-11T15:08:34Z] G-TIMER loaded                   True
[2026-10-11T15:08:34Z] G-TIMER active                   True
[2026-10-11T15:08:34Z] G-TIMER enabled                  True
[2026-10-11T15:08:34Z] G-TIMER fragment                 True
[2026-10-11T15:08:34Z] G-TIMER its unit                 True
[2026-10-11T15:08:34Z] G-TIMER the calendar             True
[2026-10-11T15:08:34Z] G-TIMER 600 s after it starts    True
[2026-10-11T15:08:34Z] G-TIMER accuracy 1 s             True
[2026-10-11T15:08:34Z] G-TIMER the next calendar elapse True
[2026-10-11T15:08:34Z] G-TIMER PASS: the next calendar run at 2026-10-12T03:00:20Z, the run after the start at 2026-10-11T15:18:11Z
[2026-10-11T15:08:34Z] peak memory of this run: 35979264 bytes
[2026-10-11T15:08:34Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
NEXT                        LEFT LAST PASSED UNIT                       ACTIVATES
Sun 2026-10-11 15:18:11 UTC 9min -         - btc-pairbook-archive.timer btc-pairbook-archive.service

1 timers listed.
```

### 2.9 §3.8 — the first run: G-TRIGGER, G-RUN and its readings (V10): **FIRST PASS: 11 of 11**

`I first` ran every 300 s from 15:18:41 UTC, 630 s after B-ENABLE, from a background loop `/root/tz28-work/poll-first.sh` (§6 item 3). Polls 1 to 3 printed `NOT YET` with exit 3. **Poll 1 already found the run**, so G-TRIGGER's `no run since the mark` never printed. Poll 4 decided. **B-RETRY was not run (V11).** `logs/30-first-poll.log`:

```
2026-10-11T15:18:41Z poll 1 exit=3: [2026-10-11T15:18:41Z] NOT YET: run 1791731892; the service activating
2026-10-11T15:23:42Z poll 2 exit=3: [2026-10-11T15:23:42Z] NOT YET: run 1791731892; the service activating
2026-10-11T15:28:41Z poll 3 exit=3: [2026-10-11T15:28:41Z] NOT YET: run 1791731892; the service activating
2026-10-11T15:33:42Z poll 4 exit=0: [2026-10-11T15:33:42Z] READING G-RUN       PASS
```

Polls 1 to 3 — `logs/30-first-01.log`, `-02`, `-03`:

```
[2026-10-11T15:18:41Z] NOT YET: run 1791731892; the service activating
[2026-10-11T15:18:41Z] peak memory of this run: 35934208 bytes
[2026-10-11T15:18:41Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=3
```

```
[2026-10-11T15:23:42Z] NOT YET: run 1791731892; the service activating
[2026-10-11T15:23:42Z] peak memory of this run: 35934208 bytes
[2026-10-11T15:23:42Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=3
```

```
[2026-10-11T15:28:41Z] NOT YET: run 1791731892; the service activating
[2026-10-11T15:28:41Z] peak memory of this run: 35938304 bytes
[2026-10-11T15:28:41Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=3
```

**The deciding `first`, `logs/30-first-04.log`, verbatim.** It contains every `R` record of the run; the `W` lines (79), the `S` lines (28), the `ROW` lines (28 of 28) and the `T` lines (61); and the eleven readings:

```
[2026-10-11T15:33:41Z] R {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "2a4b998acb9f4883b26999bb278624bf", "phase_at": 192, "resumed": false, "run": 1791731892, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791731892810556801}
[2026-10-11T15:33:41Z] R {"assets_n": 28, "bytes_total": 430047476, "closed": 79, "deferred": 0, "event": "set", "first_T": 1791706500, "last_T": 1791730800, "open": 0, "run": 1791731892, "sha256": "ec3983419485fa67317468917eb7b60e2d0e529be4334c7297831ff562471ad0", "tag": "pairbook-streams-1791731892", "unclosed": 0, "wall_ns": 1791731893762719408, "windows_considered": 79}
[2026-10-11T15:33:41Z] R {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 409746510, "run": 1791731892, "sent": 28, "wall_ns": 1791731937181037882}
[2026-10-11T15:33:41Z] R {"assets_n": 28, "bytes_total": 430047476, "event": "verify", "release_id": 409746510, "run": 1791731892, "verify_sha256": "032adfdbaea0b81d7ea5063eb43130c09396908f05d74be0f1818d2bb2342f64", "wall_ns": 1791732090814504593}
[2026-10-11T15:33:41Z] R {"already": 0, "event": "delete", "free_after": 12969091072, "free_before": 12538937344, "freed": 430047476, "gone": 28, "removed": 28, "run": 1791731892, "wall_ns": 1791732091732399708, "windows_kept": 28}
[2026-10-11T15:33:41Z] R {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "815823", "NRestarts": "2", "ns": 1791732091741955625}, "phase": 391, "run": 1791731892, "wall_ns": 1791732091741960838}
[2026-10-11T15:33:41Z] R {"event": "kill", "exit": 0, "phase": 391, "run": 1791731892, "wall_ns": 1791732091746593097}
[2026-10-11T15:33:41Z] R {"NRestarts": "3", "W": 1791731700, "event": "restart", "free_bytes": 12969062400, "gap_ns": 5548461176, "pid": 851381, "run": 1791731892, "stopped": 815823, "stream_bytes": 0, "wall_ns": 1791732121761569347}
[2026-10-11T15:33:41Z] R {"T": 1791731700, "event": "resume", "reading": "PASS", "run": 1791731892, "wall_ns": 1791732641000772037}
[2026-10-11T15:33:41Z] R {"assets_n": 28, "bytes_total": 430047476, "ended_outside": 0, "event": "complete", "free_bytes": 12949487616, "peak_rss": 36884480, "rate_per_day": 1474448489, "requests": 61, "run": 1791731892, "started_outside": 0, "stops": [["the cap", 1792200292], ["the floor, base 43500000 bytes a day", 1792213576], ["the floor, base 187760570 bytes a day", 1792171837]], "store_stream_bytes": 19346486, "wall_ns": 1791732641002785194}
[2026-10-11T15:33:41Z] run 1791731892: 10 records, ['start', 'set', 'upload', 'verify', 'delete', 'mark', 'kill', 'restart', 'resume', 'complete']
[2026-10-11T15:33:41Z] G-TRIGGER: the timer started 2026-10-11T15:08:11Z, triggered 2026-10-11T15:18:12Z, the run's first record 2026-10-11T15:18:12Z
[2026-10-11T15:33:41Z] G-RUN: the run complete; the service's last invocation 2a4b998acb9f4883b26999bb278624bf, Result success, ExecMainStatus 0, Sun 2026-10-11 15:18:12 UTC to Sun 2026-10-11 15:30:41 UTC
[2026-10-11T15:33:41Z] W 1791660600 2026-10-10T19:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791661500 2026-10-10T19:45:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791662400 2026-10-10T20:00:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791663300 2026-10-10T20:15:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791664200 2026-10-10T20:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791665100 2026-10-10T20:45:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791666000 2026-10-10T21:00:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791666900 2026-10-10T21:15:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791667800 2026-10-10T21:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791668700 2026-10-10T21:45:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791669600 2026-10-10T22:00:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791670500 2026-10-10T22:15:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791671400 2026-10-10T22:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791672300 2026-10-10T22:45:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791673200 2026-10-10T23:00:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791674100 2026-10-10T23:15:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791675000 2026-10-10T23:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791675900 2026-10-10T23:45:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791676800 2026-10-11T00:00:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791677700 2026-10-11T00:15:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791678600 2026-10-11T00:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791679500 2026-10-11T00:45:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791680400 2026-10-11T01:00:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791681300 2026-10-11T01:15:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791682200 2026-10-11T01:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791683100 2026-10-11T01:45:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791684000 2026-10-11T02:00:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791684900 2026-10-11T02:15:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791685800 2026-10-11T02:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791686700 2026-10-11T02:45:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791687600 2026-10-11T03:00:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791688500 2026-10-11T03:15:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791689400 2026-10-11T03:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791690300 2026-10-11T03:45:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791691200 2026-10-11T04:00:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791692100 2026-10-11T04:15:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791693000 2026-10-11T04:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791693900 2026-10-11T04:45:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791694800 2026-10-11T05:00:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791695700 2026-10-11T05:15:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791696600 2026-10-11T05:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791697500 2026-10-11T05:45:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791698400 2026-10-11T06:00:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791699300 2026-10-11T06:15:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791700200 2026-10-11T06:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791701100 2026-10-11T06:45:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791702000 2026-10-11T07:00:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791702900 2026-10-11T07:15:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791703800 2026-10-11T07:30:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791704700 2026-10-11T07:45:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791705600 2026-10-11T08:00:00Z closed   stream files 0, 0 bytes, taken 0
[2026-10-11T15:33:41Z] W 1791706500 2026-10-11T08:15:00Z closed   stream files 1, 10095699 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791707400 2026-10-11T08:30:00Z closed   stream files 1, 11832348 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791708300 2026-10-11T08:45:00Z closed   stream files 1, 13211251 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791709200 2026-10-11T09:00:00Z closed   stream files 1, 13411606 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791710100 2026-10-11T09:15:00Z closed   stream files 1, 18371683 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791711000 2026-10-11T09:30:00Z closed   stream files 1, 14156803 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791711900 2026-10-11T09:45:00Z closed   stream files 1, 14389992 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791712800 2026-10-11T10:00:00Z closed   stream files 1, 13225521 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791713700 2026-10-11T10:15:00Z closed   stream files 1, 12494685 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791714600 2026-10-11T10:30:00Z closed   stream files 1, 17326950 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791715500 2026-10-11T10:45:00Z closed   stream files 1, 11540484 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791716400 2026-10-11T11:00:00Z closed   stream files 1, 16012398 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791717300 2026-10-11T11:15:00Z closed   stream files 1, 14949740 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791718200 2026-10-11T11:30:00Z closed   stream files 1, 13295331 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791719100 2026-10-11T11:45:00Z closed   stream files 1, 15090064 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791720000 2026-10-11T12:00:00Z closed   stream files 1, 14563101 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791720900 2026-10-11T12:15:00Z closed   stream files 1, 14057421 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791721800 2026-10-11T12:30:00Z closed   stream files 1, 13298734 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791722700 2026-10-11T12:45:00Z closed   stream files 1, 13411812 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791723600 2026-10-11T13:00:00Z closed   stream files 1, 14202184 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791724500 2026-10-11T13:15:00Z closed   stream files 1, 25796663 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791725400 2026-10-11T13:30:00Z closed   stream files 1, 17156590 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791726300 2026-10-11T13:45:00Z closed   stream files 1, 18986113 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791727200 2026-10-11T14:00:00Z closed   stream files 1, 26477771 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791728100 2026-10-11T14:15:00Z closed   stream files 1, 13402371 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791729000 2026-10-11T14:30:00Z closed   stream files 1, 14249655 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791729900 2026-10-11T14:45:00Z closed   stream files 1, 19926659 bytes, taken 1
[2026-10-11T15:33:41Z] W 1791730800 2026-10-11T15:00:00Z closed   stream files 1, 15113847 bytes, taken 1
[2026-10-11T15:33:41Z] S 1791706500-stream.jsonl.gz 10095699 f358b90465f20b188bab7ede9ee6f530251bcd8f14801ae47c1d600f9b266db6
[2026-10-11T15:33:41Z] S 1791707400-stream.jsonl.gz 11832348 e918ce4e7dfc25f2384dd666fae937be6c866509c1e12c71d2e33b1dee6801e1
[2026-10-11T15:33:41Z] S 1791708300-stream.jsonl.gz 13211251 0369a1b1a3c40c39728aa8e98336a9c4d2eed76474c657bacfa8f006edf9fa12
[2026-10-11T15:33:41Z] S 1791709200-stream.jsonl.gz 13411606 a28bd92475e3b0e78449d1dfc1b7909715776f49951470ae39767488ace5843f
[2026-10-11T15:33:41Z] S 1791710100-stream.jsonl.gz 18371683 a8df4b6d3573730d523dbe6c2b34b5f60f6de36dd7011b87ed08e85107998c27
[2026-10-11T15:33:41Z] S 1791711000-stream.jsonl.gz 14156803 64fdf6f7ef2e7bbb3ebd154199da3facb4325b216f2fb477cb43e928a88b9e30
[2026-10-11T15:33:41Z] S 1791711900-stream.jsonl.gz 14389992 3206e5fd0228b365df4d6c4c647e6c5b18b6f59f88c2bbadced96a77d4c637e9
[2026-10-11T15:33:41Z] S 1791712800-stream.jsonl.gz 13225521 7e88d67513f95c71080d3bc9980a04b26e4587619d2e095f1033d6eb9f62d935
[2026-10-11T15:33:41Z] S 1791713700-stream.jsonl.gz 12494685 ce65c49f450863a0b64db14f0026711da8ca96757d32bb192580799cd84d597b
[2026-10-11T15:33:41Z] S 1791714600-stream.jsonl.gz 17326950 ae0aa14b66b5182dc89097bbcbb6cec0d7d714f89098ed110f302fc8a9d0faa3
[2026-10-11T15:33:41Z] S 1791715500-stream.jsonl.gz 11540484 400613f975b563ada9ffd6cbdc9961de6230134ab50e6fbf3875ee7dd9ec82a9
[2026-10-11T15:33:41Z] S 1791716400-stream.jsonl.gz 16012398 5fddd6baf9206d4b05d86760712173a042d855e73cad761a2828d1cdccd0fcfa
[2026-10-11T15:33:41Z] S 1791717300-stream.jsonl.gz 14949740 578e165ec258dc443856c457b052d3d2ec1565f0eb9edcb37e074ef7c9a81b4f
[2026-10-11T15:33:41Z] S 1791718200-stream.jsonl.gz 13295331 61f6cc2df7c2013906745aee0bfd14c4d5ac43536245285a33ef1b08265f95a3
[2026-10-11T15:33:41Z] S 1791719100-stream.jsonl.gz 15090064 e60b01408ea889c124e14757297e67ee735c43c1351746955f9906334a0d0e60
[2026-10-11T15:33:41Z] S 1791720000-stream.jsonl.gz 14563101 ee7b93b3e29d69c3ec716b32130e8e53d764df45c87c07f001e0732ea20289f4
[2026-10-11T15:33:41Z] S 1791720900-stream.jsonl.gz 14057421 321c45dfaf6697914e35594bd17a104a12d1b1fa6c02fed8883d8884e4a893c3
[2026-10-11T15:33:41Z] S 1791721800-stream.jsonl.gz 13298734 019e4f3c7febb45a63b9f1102df97f5b0d0bf0e7e9fa37a7ee560fe0d0cd7d6d
[2026-10-11T15:33:41Z] S 1791722700-stream.jsonl.gz 13411812 a29e3b6989e6d6b79abe173f53578f6d66032a5a10f500959939c033f77d766a
[2026-10-11T15:33:41Z] S 1791723600-stream.jsonl.gz 14202184 d3e168396e20bf4da2104c2f2cd63e3bacb8b6bd62b94a83c186638005f61a1f
[2026-10-11T15:33:41Z] S 1791724500-stream.jsonl.gz 25796663 a9fd2a97440257bac81a0f5e15710c6a58f9641c5d479a5a96a1d3f464dbd5d2
[2026-10-11T15:33:41Z] S 1791725400-stream.jsonl.gz 17156590 9d3ae93cebfe71903f568e9cf46bdd40d59fbacee62ae6e328783ccff7257720
[2026-10-11T15:33:41Z] S 1791726300-stream.jsonl.gz 18986113 4d2846a58de2c86bdb47f38f9344cd1e406946148b55f798fdb1e6688ac6366c
[2026-10-11T15:33:41Z] S 1791727200-stream.jsonl.gz 26477771 70cf67b099f95b6bc54010e65902a0546d4ba240c8b7bfb9a95d40765f7367fa
[2026-10-11T15:33:41Z] S 1791728100-stream.jsonl.gz 13402371 8104b837473a07859c2f30a7654c50f243baa0a1376d763d5e341ac63f99a497
[2026-10-11T15:33:41Z] S 1791729000-stream.jsonl.gz 14249655 5731669734a1400fbc74201ace72897316dc8c201eea655394addcf664362767
[2026-10-11T15:33:41Z] S 1791729900-stream.jsonl.gz 19926659 b26db937b1bf4e0abf5b86eeaceb2f799f8c96b5140d71d62f7b0fea02ead959
[2026-10-11T15:33:41Z] S 1791730800-stream.jsonl.gz 15113847 8db51c478756879bf4768d379063bf6be1e7b3e53131f5deff977d1b9a8695ed
[2026-10-11T15:33:41Z] G-SET: 28 files, 430047476 bytes, windows 1791706500 to 1791730800, as of 1791731892, deferred 0; set.json sha256 ec3983419485fa67317468917eb7b60e2d0e529be4334c7297831ff562471ad0
[2026-10-11T15:33:42Z] G-UPLOAD: Release 409746510, 28 of 28 assets by name, bytes, state and digest, 0 missing, 0 beyond; the tag pairbook-streams-1791731892 at d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
[2026-10-11T15:33:42Z] G-DOWNLOAD: verify.json sha256 032adfdbaea0b81d7ea5063eb43130c09396908f05d74be0f1818d2bb2342f64, 28 of 28 downloads equal, 430047476 bytes
[2026-10-11T15:33:42Z] ROW 1791706500-stream.jsonl.gz 10095699 f358b90465f20b188bab7ede9ee6f530251bcd8f14801ae47c1d600f9b266db6 digest sha256:f358b90465f20b188bab7ede9ee6f530251bcd8f14801ae47c1d600f9b266db6 download f358b90465f20b188bab7ede9ee6f530251bcd8f14801ae47c1d600f9b266db6 removed f358b90465f20b188bab7ede9ee6f530251bcd8f14801ae47c1d600f9b266db6
[2026-10-11T15:33:42Z] ROW 1791707400-stream.jsonl.gz 11832348 e918ce4e7dfc25f2384dd666fae937be6c866509c1e12c71d2e33b1dee6801e1 digest sha256:e918ce4e7dfc25f2384dd666fae937be6c866509c1e12c71d2e33b1dee6801e1 download e918ce4e7dfc25f2384dd666fae937be6c866509c1e12c71d2e33b1dee6801e1 removed e918ce4e7dfc25f2384dd666fae937be6c866509c1e12c71d2e33b1dee6801e1
[2026-10-11T15:33:42Z] ROW 1791708300-stream.jsonl.gz 13211251 0369a1b1a3c40c39728aa8e98336a9c4d2eed76474c657bacfa8f006edf9fa12 digest sha256:0369a1b1a3c40c39728aa8e98336a9c4d2eed76474c657bacfa8f006edf9fa12 download 0369a1b1a3c40c39728aa8e98336a9c4d2eed76474c657bacfa8f006edf9fa12 removed 0369a1b1a3c40c39728aa8e98336a9c4d2eed76474c657bacfa8f006edf9fa12
[2026-10-11T15:33:42Z] ROW 1791709200-stream.jsonl.gz 13411606 a28bd92475e3b0e78449d1dfc1b7909715776f49951470ae39767488ace5843f digest sha256:a28bd92475e3b0e78449d1dfc1b7909715776f49951470ae39767488ace5843f download a28bd92475e3b0e78449d1dfc1b7909715776f49951470ae39767488ace5843f removed a28bd92475e3b0e78449d1dfc1b7909715776f49951470ae39767488ace5843f
[2026-10-11T15:33:42Z] ROW 1791710100-stream.jsonl.gz 18371683 a8df4b6d3573730d523dbe6c2b34b5f60f6de36dd7011b87ed08e85107998c27 digest sha256:a8df4b6d3573730d523dbe6c2b34b5f60f6de36dd7011b87ed08e85107998c27 download a8df4b6d3573730d523dbe6c2b34b5f60f6de36dd7011b87ed08e85107998c27 removed a8df4b6d3573730d523dbe6c2b34b5f60f6de36dd7011b87ed08e85107998c27
[2026-10-11T15:33:42Z] ROW 1791711000-stream.jsonl.gz 14156803 64fdf6f7ef2e7bbb3ebd154199da3facb4325b216f2fb477cb43e928a88b9e30 digest sha256:64fdf6f7ef2e7bbb3ebd154199da3facb4325b216f2fb477cb43e928a88b9e30 download 64fdf6f7ef2e7bbb3ebd154199da3facb4325b216f2fb477cb43e928a88b9e30 removed 64fdf6f7ef2e7bbb3ebd154199da3facb4325b216f2fb477cb43e928a88b9e30
[2026-10-11T15:33:42Z] ROW 1791711900-stream.jsonl.gz 14389992 3206e5fd0228b365df4d6c4c647e6c5b18b6f59f88c2bbadced96a77d4c637e9 digest sha256:3206e5fd0228b365df4d6c4c647e6c5b18b6f59f88c2bbadced96a77d4c637e9 download 3206e5fd0228b365df4d6c4c647e6c5b18b6f59f88c2bbadced96a77d4c637e9 removed 3206e5fd0228b365df4d6c4c647e6c5b18b6f59f88c2bbadced96a77d4c637e9
[2026-10-11T15:33:42Z] ROW 1791712800-stream.jsonl.gz 13225521 7e88d67513f95c71080d3bc9980a04b26e4587619d2e095f1033d6eb9f62d935 digest sha256:7e88d67513f95c71080d3bc9980a04b26e4587619d2e095f1033d6eb9f62d935 download 7e88d67513f95c71080d3bc9980a04b26e4587619d2e095f1033d6eb9f62d935 removed 7e88d67513f95c71080d3bc9980a04b26e4587619d2e095f1033d6eb9f62d935
[2026-10-11T15:33:42Z] ROW 1791713700-stream.jsonl.gz 12494685 ce65c49f450863a0b64db14f0026711da8ca96757d32bb192580799cd84d597b digest sha256:ce65c49f450863a0b64db14f0026711da8ca96757d32bb192580799cd84d597b download ce65c49f450863a0b64db14f0026711da8ca96757d32bb192580799cd84d597b removed ce65c49f450863a0b64db14f0026711da8ca96757d32bb192580799cd84d597b
[2026-10-11T15:33:42Z] ROW 1791714600-stream.jsonl.gz 17326950 ae0aa14b66b5182dc89097bbcbb6cec0d7d714f89098ed110f302fc8a9d0faa3 digest sha256:ae0aa14b66b5182dc89097bbcbb6cec0d7d714f89098ed110f302fc8a9d0faa3 download ae0aa14b66b5182dc89097bbcbb6cec0d7d714f89098ed110f302fc8a9d0faa3 removed ae0aa14b66b5182dc89097bbcbb6cec0d7d714f89098ed110f302fc8a9d0faa3
[2026-10-11T15:33:42Z] ROW 1791715500-stream.jsonl.gz 11540484 400613f975b563ada9ffd6cbdc9961de6230134ab50e6fbf3875ee7dd9ec82a9 digest sha256:400613f975b563ada9ffd6cbdc9961de6230134ab50e6fbf3875ee7dd9ec82a9 download 400613f975b563ada9ffd6cbdc9961de6230134ab50e6fbf3875ee7dd9ec82a9 removed 400613f975b563ada9ffd6cbdc9961de6230134ab50e6fbf3875ee7dd9ec82a9
[2026-10-11T15:33:42Z] ROW 1791716400-stream.jsonl.gz 16012398 5fddd6baf9206d4b05d86760712173a042d855e73cad761a2828d1cdccd0fcfa digest sha256:5fddd6baf9206d4b05d86760712173a042d855e73cad761a2828d1cdccd0fcfa download 5fddd6baf9206d4b05d86760712173a042d855e73cad761a2828d1cdccd0fcfa removed 5fddd6baf9206d4b05d86760712173a042d855e73cad761a2828d1cdccd0fcfa
[2026-10-11T15:33:42Z] ROW 1791717300-stream.jsonl.gz 14949740 578e165ec258dc443856c457b052d3d2ec1565f0eb9edcb37e074ef7c9a81b4f digest sha256:578e165ec258dc443856c457b052d3d2ec1565f0eb9edcb37e074ef7c9a81b4f download 578e165ec258dc443856c457b052d3d2ec1565f0eb9edcb37e074ef7c9a81b4f removed 578e165ec258dc443856c457b052d3d2ec1565f0eb9edcb37e074ef7c9a81b4f
[2026-10-11T15:33:42Z] ROW 1791718200-stream.jsonl.gz 13295331 61f6cc2df7c2013906745aee0bfd14c4d5ac43536245285a33ef1b08265f95a3 digest sha256:61f6cc2df7c2013906745aee0bfd14c4d5ac43536245285a33ef1b08265f95a3 download 61f6cc2df7c2013906745aee0bfd14c4d5ac43536245285a33ef1b08265f95a3 removed 61f6cc2df7c2013906745aee0bfd14c4d5ac43536245285a33ef1b08265f95a3
[2026-10-11T15:33:42Z] ROW 1791719100-stream.jsonl.gz 15090064 e60b01408ea889c124e14757297e67ee735c43c1351746955f9906334a0d0e60 digest sha256:e60b01408ea889c124e14757297e67ee735c43c1351746955f9906334a0d0e60 download e60b01408ea889c124e14757297e67ee735c43c1351746955f9906334a0d0e60 removed e60b01408ea889c124e14757297e67ee735c43c1351746955f9906334a0d0e60
[2026-10-11T15:33:42Z] ROW 1791720000-stream.jsonl.gz 14563101 ee7b93b3e29d69c3ec716b32130e8e53d764df45c87c07f001e0732ea20289f4 digest sha256:ee7b93b3e29d69c3ec716b32130e8e53d764df45c87c07f001e0732ea20289f4 download ee7b93b3e29d69c3ec716b32130e8e53d764df45c87c07f001e0732ea20289f4 removed ee7b93b3e29d69c3ec716b32130e8e53d764df45c87c07f001e0732ea20289f4
[2026-10-11T15:33:42Z] ROW 1791720900-stream.jsonl.gz 14057421 321c45dfaf6697914e35594bd17a104a12d1b1fa6c02fed8883d8884e4a893c3 digest sha256:321c45dfaf6697914e35594bd17a104a12d1b1fa6c02fed8883d8884e4a893c3 download 321c45dfaf6697914e35594bd17a104a12d1b1fa6c02fed8883d8884e4a893c3 removed 321c45dfaf6697914e35594bd17a104a12d1b1fa6c02fed8883d8884e4a893c3
[2026-10-11T15:33:42Z] ROW 1791721800-stream.jsonl.gz 13298734 019e4f3c7febb45a63b9f1102df97f5b0d0bf0e7e9fa37a7ee560fe0d0cd7d6d digest sha256:019e4f3c7febb45a63b9f1102df97f5b0d0bf0e7e9fa37a7ee560fe0d0cd7d6d download 019e4f3c7febb45a63b9f1102df97f5b0d0bf0e7e9fa37a7ee560fe0d0cd7d6d removed 019e4f3c7febb45a63b9f1102df97f5b0d0bf0e7e9fa37a7ee560fe0d0cd7d6d
[2026-10-11T15:33:42Z] ROW 1791722700-stream.jsonl.gz 13411812 a29e3b6989e6d6b79abe173f53578f6d66032a5a10f500959939c033f77d766a digest sha256:a29e3b6989e6d6b79abe173f53578f6d66032a5a10f500959939c033f77d766a download a29e3b6989e6d6b79abe173f53578f6d66032a5a10f500959939c033f77d766a removed a29e3b6989e6d6b79abe173f53578f6d66032a5a10f500959939c033f77d766a
[2026-10-11T15:33:42Z] ROW 1791723600-stream.jsonl.gz 14202184 d3e168396e20bf4da2104c2f2cd63e3bacb8b6bd62b94a83c186638005f61a1f digest sha256:d3e168396e20bf4da2104c2f2cd63e3bacb8b6bd62b94a83c186638005f61a1f download d3e168396e20bf4da2104c2f2cd63e3bacb8b6bd62b94a83c186638005f61a1f removed d3e168396e20bf4da2104c2f2cd63e3bacb8b6bd62b94a83c186638005f61a1f
[2026-10-11T15:33:42Z] ROW 1791724500-stream.jsonl.gz 25796663 a9fd2a97440257bac81a0f5e15710c6a58f9641c5d479a5a96a1d3f464dbd5d2 digest sha256:a9fd2a97440257bac81a0f5e15710c6a58f9641c5d479a5a96a1d3f464dbd5d2 download a9fd2a97440257bac81a0f5e15710c6a58f9641c5d479a5a96a1d3f464dbd5d2 removed a9fd2a97440257bac81a0f5e15710c6a58f9641c5d479a5a96a1d3f464dbd5d2
[2026-10-11T15:33:42Z] ROW 1791725400-stream.jsonl.gz 17156590 9d3ae93cebfe71903f568e9cf46bdd40d59fbacee62ae6e328783ccff7257720 digest sha256:9d3ae93cebfe71903f568e9cf46bdd40d59fbacee62ae6e328783ccff7257720 download 9d3ae93cebfe71903f568e9cf46bdd40d59fbacee62ae6e328783ccff7257720 removed 9d3ae93cebfe71903f568e9cf46bdd40d59fbacee62ae6e328783ccff7257720
[2026-10-11T15:33:42Z] ROW 1791726300-stream.jsonl.gz 18986113 4d2846a58de2c86bdb47f38f9344cd1e406946148b55f798fdb1e6688ac6366c digest sha256:4d2846a58de2c86bdb47f38f9344cd1e406946148b55f798fdb1e6688ac6366c download 4d2846a58de2c86bdb47f38f9344cd1e406946148b55f798fdb1e6688ac6366c removed 4d2846a58de2c86bdb47f38f9344cd1e406946148b55f798fdb1e6688ac6366c
[2026-10-11T15:33:42Z] ROW 1791727200-stream.jsonl.gz 26477771 70cf67b099f95b6bc54010e65902a0546d4ba240c8b7bfb9a95d40765f7367fa digest sha256:70cf67b099f95b6bc54010e65902a0546d4ba240c8b7bfb9a95d40765f7367fa download 70cf67b099f95b6bc54010e65902a0546d4ba240c8b7bfb9a95d40765f7367fa removed 70cf67b099f95b6bc54010e65902a0546d4ba240c8b7bfb9a95d40765f7367fa
[2026-10-11T15:33:42Z] ROW 1791728100-stream.jsonl.gz 13402371 8104b837473a07859c2f30a7654c50f243baa0a1376d763d5e341ac63f99a497 digest sha256:8104b837473a07859c2f30a7654c50f243baa0a1376d763d5e341ac63f99a497 download 8104b837473a07859c2f30a7654c50f243baa0a1376d763d5e341ac63f99a497 removed 8104b837473a07859c2f30a7654c50f243baa0a1376d763d5e341ac63f99a497
[2026-10-11T15:33:42Z] ROW 1791729000-stream.jsonl.gz 14249655 5731669734a1400fbc74201ace72897316dc8c201eea655394addcf664362767 digest sha256:5731669734a1400fbc74201ace72897316dc8c201eea655394addcf664362767 download 5731669734a1400fbc74201ace72897316dc8c201eea655394addcf664362767 removed 5731669734a1400fbc74201ace72897316dc8c201eea655394addcf664362767
[2026-10-11T15:33:42Z] ROW 1791729900-stream.jsonl.gz 19926659 b26db937b1bf4e0abf5b86eeaceb2f799f8c96b5140d71d62f7b0fea02ead959 digest sha256:b26db937b1bf4e0abf5b86eeaceb2f799f8c96b5140d71d62f7b0fea02ead959 download b26db937b1bf4e0abf5b86eeaceb2f799f8c96b5140d71d62f7b0fea02ead959 removed b26db937b1bf4e0abf5b86eeaceb2f799f8c96b5140d71d62f7b0fea02ead959
[2026-10-11T15:33:42Z] ROW 1791730800-stream.jsonl.gz 15113847 8db51c478756879bf4768d379063bf6be1e7b3e53131f5deff977d1b9a8695ed digest sha256:8db51c478756879bf4768d379063bf6be1e7b3e53131f5deff977d1b9a8695ed download 8db51c478756879bf4768d379063bf6be1e7b3e53131f5deff977d1b9a8695ed removed 8db51c478756879bf4768d379063bf6be1e7b3e53131f5deff977d1b9a8695ed
[2026-10-11T15:33:42Z] G-DELETE: {'every file of the set absent': True, 'each removal recorded by delete': True, 'each window keeps its window.json': True}; 28 gone, 28 removals recorded, 28 windows kept
[2026-10-11T15:33:42Z] G-RESTART: {'a stop of the marked process': True, 'stopped inside the band': True, 'a start of another process': True, 'within 60 s': True, 'the same code': True}; the stop of 815823 at second 391, the start of 851381 5.548 s later
[2026-10-11T15:33:42Z] G-COUNTER: {"started before its window's documents": True, 'the counter equals the store': True, 'the counter below the cap': True, 'no file of the set left': True}; stream_bytes 0, the store's windows up to 1791730800 0 bytes
[2026-10-11T15:33:42Z] G-UNIT: {'active': True, 'enabled': True, 'fragment': True, 'control group': True, 'ceiling': True, 'argv': True, 'cwd': True, 'cgroup': True, 'sole instance': True, 'restarts': True}; MainPID 851381
[2026-10-11T15:33:42Z] window 1791731700: pid 851381, documents True; stream opened True, off_reason None, files ['stream.jsonl.gz'], segments 2, frames 237078, stored_bytes 19346486
[2026-10-11T15:33:42Z] READING G-RESUME: PASS, window 1791731700
[2026-10-11T15:33:42Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/tags/pairbook-streams-1791731892: 0 bytes, budget 5 s, second 193, 0.3 s, inside True True
[2026-10-11T15:33:42Z] T api POST /repos/seahomebatumi-ai/btc-5m-twap/releases: 0 bytes, budget 5 s, second 194, 0.9 s, inside True True
[2026-10-11T15:33:42Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/409746510/assets: 0 bytes, budget 5 s, second 194, 0.3 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791706500-stream.jsonl.gz: 10095699 bytes, budget 11 s, second 195, 1.3 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791707400-stream.jsonl.gz: 11832348 bytes, budget 11 s, second 196, 1.7 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791708300-stream.jsonl.gz: 13211251 bytes, budget 12 s, second 198, 1.6 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791709200-stream.jsonl.gz: 13411606 bytes, budget 12 s, second 199, 1.1 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791710100-stream.jsonl.gz: 18371683 bytes, budget 15 s, second 200, 1.5 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791711000-stream.jsonl.gz: 14156803 bytes, budget 13 s, second 202, 1.3 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791711900-stream.jsonl.gz: 14389992 bytes, budget 13 s, second 203, 1.5 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791712800-stream.jsonl.gz: 13225521 bytes, budget 12 s, second 205, 1.5 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791713700-stream.jsonl.gz: 12494685 bytes, budget 12 s, second 206, 1.2 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791714600-stream.jsonl.gz: 17326950 bytes, budget 14 s, second 207, 1.4 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791715500-stream.jsonl.gz: 11540484 bytes, budget 11 s, second 209, 1.3 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791716400-stream.jsonl.gz: 16012398 bytes, budget 14 s, second 210, 1.4 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791717300-stream.jsonl.gz: 14949740 bytes, budget 13 s, second 211, 1.4 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791718200-stream.jsonl.gz: 13295331 bytes, budget 12 s, second 213, 1.9 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791719100-stream.jsonl.gz: 15090064 bytes, budget 13 s, second 215, 2.0 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791720000-stream.jsonl.gz: 14563101 bytes, budget 13 s, second 217, 1.4 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791720900-stream.jsonl.gz: 14057421 bytes, budget 13 s, second 218, 1.4 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791721800-stream.jsonl.gz: 13298734 bytes, budget 12 s, second 220, 1.3 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791722700-stream.jsonl.gz: 13411812 bytes, budget 12 s, second 221, 1.3 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791723600-stream.jsonl.gz: 14202184 bytes, budget 13 s, second 222, 1.4 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791724500-stream.jsonl.gz: 25796663 bytes, budget 18 s, second 224, 1.7 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791725400-stream.jsonl.gz: 17156590 bytes, budget 14 s, second 225, 1.5 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791726300-stream.jsonl.gz: 18986113 bytes, budget 15 s, second 227, 1.9 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791727200-stream.jsonl.gz: 26477771 bytes, budget 19 s, second 229, 1.9 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791728100-stream.jsonl.gz: 13402371 bytes, budget 12 s, second 231, 1.4 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791729000-stream.jsonl.gz: 14249655 bytes, budget 13 s, second 232, 1.5 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791729900-stream.jsonl.gz: 19926659 bytes, budget 15 s, second 234, 1.6 s, inside True True
[2026-10-11T15:33:42Z] T upload 1791730800-stream.jsonl.gz: 15113847 bytes, budget 13 s, second 235, 1.4 s, inside True True
[2026-10-11T15:33:42Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/tags/pairbook-streams-1791731892: 0 bytes, budget 5 s, second 357, 0.3 s, inside True True
[2026-10-11T15:33:42Z] T api GET /repos/seahomebatumi-ai/btc-5m-twap/releases/409746510/assets: 0 bytes, budget 5 s, second 358, 0.3 s, inside True True
[2026-10-11T15:33:42Z] T download 1791706500-stream.jsonl.gz: 10095699 bytes, budget 11 s, second 358, 0.7 s, inside True True
[2026-10-11T15:33:42Z] T download 1791707400-stream.jsonl.gz: 11832348 bytes, budget 11 s, second 358, 0.8 s, inside True True
[2026-10-11T15:33:42Z] T download 1791708300-stream.jsonl.gz: 13211251 bytes, budget 12 s, second 359, 1.7 s, inside True True
[2026-10-11T15:33:42Z] T download 1791709200-stream.jsonl.gz: 13411606 bytes, budget 12 s, second 361, 1.0 s, inside True True
[2026-10-11T15:33:42Z] T download 1791710100-stream.jsonl.gz: 18371683 bytes, budget 15 s, second 362, 1.2 s, inside True True
[2026-10-11T15:33:42Z] T download 1791711000-stream.jsonl.gz: 14156803 bytes, budget 13 s, second 363, 0.9 s, inside True True
[2026-10-11T15:33:42Z] T download 1791711900-stream.jsonl.gz: 14389992 bytes, budget 13 s, second 364, 0.8 s, inside True True
[2026-10-11T15:33:42Z] T download 1791712800-stream.jsonl.gz: 13225521 bytes, budget 12 s, second 365, 0.9 s, inside True True
[2026-10-11T15:33:42Z] T download 1791713700-stream.jsonl.gz: 12494685 bytes, budget 12 s, second 366, 0.8 s, inside True True
[2026-10-11T15:33:42Z] T download 1791714600-stream.jsonl.gz: 17326950 bytes, budget 14 s, second 366, 1.1 s, inside True True
[2026-10-11T15:33:42Z] T download 1791715500-stream.jsonl.gz: 11540484 bytes, budget 11 s, second 368, 0.9 s, inside True True
[2026-10-11T15:33:42Z] T download 1791716400-stream.jsonl.gz: 16012398 bytes, budget 14 s, second 368, 1.0 s, inside True True
[2026-10-11T15:33:42Z] T download 1791717300-stream.jsonl.gz: 14949740 bytes, budget 13 s, second 369, 2.1 s, inside True True
[2026-10-11T15:33:42Z] T download 1791718200-stream.jsonl.gz: 13295331 bytes, budget 12 s, second 372, 0.8 s, inside True True
[2026-10-11T15:33:42Z] T download 1791719100-stream.jsonl.gz: 15090064 bytes, budget 13 s, second 372, 0.9 s, inside True True
[2026-10-11T15:33:42Z] T download 1791720000-stream.jsonl.gz: 14563101 bytes, budget 13 s, second 373, 4.8 s, inside True True
[2026-10-11T15:33:42Z] T download 1791720900-stream.jsonl.gz: 14057421 bytes, budget 13 s, second 378, 0.9 s, inside True True
[2026-10-11T15:33:42Z] T download 1791721800-stream.jsonl.gz: 13298734 bytes, budget 12 s, second 379, 0.7 s, inside True True
[2026-10-11T15:33:42Z] T download 1791722700-stream.jsonl.gz: 13411812 bytes, budget 12 s, second 380, 0.9 s, inside True True
[2026-10-11T15:33:42Z] T download 1791723600-stream.jsonl.gz: 14202184 bytes, budget 13 s, second 381, 1.0 s, inside True True
[2026-10-11T15:33:42Z] T download 1791724500-stream.jsonl.gz: 25796663 bytes, budget 18 s, second 382, 1.7 s, inside True True
[2026-10-11T15:33:42Z] T download 1791725400-stream.jsonl.gz: 17156590 bytes, budget 14 s, second 383, 0.9 s, inside True True
[2026-10-11T15:33:42Z] T download 1791726300-stream.jsonl.gz: 18986113 bytes, budget 15 s, second 384, 1.0 s, inside True True
[2026-10-11T15:33:42Z] T download 1791727200-stream.jsonl.gz: 26477771 bytes, budget 19 s, second 385, 1.4 s, inside True True
[2026-10-11T15:33:42Z] T download 1791728100-stream.jsonl.gz: 13402371 bytes, budget 12 s, second 387, 0.9 s, inside True True
[2026-10-11T15:33:42Z] T download 1791729000-stream.jsonl.gz: 14249655 bytes, budget 13 s, second 388, 1.1 s, inside True True
[2026-10-11T15:33:42Z] T download 1791729900-stream.jsonl.gz: 19926659 bytes, budget 15 s, second 389, 0.9 s, inside True True
[2026-10-11T15:33:42Z] T download 1791730800-stream.jsonl.gz: 15113847 bytes, budget 13 s, second 390, 0.8 s, inside True True
[2026-10-11T15:33:42Z] G-IDLE: 61 requests, 0 started outside, 0 ended outside
[2026-10-11T15:33:42Z] the run's own record: {"assets_n": 28, "bytes_total": 430047476, "ended_outside": 0, "event": "complete", "free_bytes": 12949487616, "peak_rss": 36884480, "rate_per_day": 1474448489, "requests": 61, "run": 1791731892, "started_outside": 0, "stops": [["the cap", 1792200292], ["the floor, base 43500000 bytes a day", 1792213576], ["the floor, base 187760570 bytes a day", 1792171837]], "store_stream_bytes": 19346486, "wall_ns": 1791732641002785194}
[2026-10-11T15:33:42Z] READING G-TRIGGER   PASS
[2026-10-11T15:33:42Z] READING G-RUN       PASS
[2026-10-11T15:33:42Z] READING G-SET       PASS
[2026-10-11T15:33:42Z] READING G-UPLOAD    PASS
[2026-10-11T15:33:42Z] READING G-DOWNLOAD  PASS
[2026-10-11T15:33:42Z] READING G-DELETE    PASS
[2026-10-11T15:33:42Z] READING G-RESTART   PASS
[2026-10-11T15:33:42Z] READING G-COUNTER   PASS
[2026-10-11T15:33:42Z] READING G-UNIT      PASS
[2026-10-11T15:33:42Z] READING G-RESUME    PASS
[2026-10-11T15:33:42Z] READING G-IDLE      PASS
[2026-10-11T15:33:42Z] FIRST PASS: 11 of 11
[2026-10-11T15:33:42Z] peak memory of this run: 37158912 bytes
[2026-10-11T15:33:42Z] opens refused: 0; store opens 2; requests 2, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

### 2.10 The run's steps — first and last stamp of each, for B3's measurement (map §7 item 109)

Each step's ledger record (`L` in `archive.log`, `R` in `first`) is that step's last stamped line. Each step's first stamped line is either the record before it or, for the request steps, its first request's start. Those starts come from the `T` lines, as seconds of window `1791731700` (`T` = 15:15:00 UTC).

| step | first stamp (UTC) | last stamp, its record (UTC) | note |
|---|---|---|---|
| start | — | 15:18:12.810 | `phase_at` 192 |
| set | 15:18:12.810 | 15:18:13.762 | 28 files hashed |
| upload | second 193 (15:18:13) | 15:18:57.181 | 31 requests, seconds 193 to 235; last lasted 1.4 s |
| verify | second 357 (15:20:57) | 15:21:30.814 | 30 requests, seconds 357 to 390; 120 s settle after the upload record |
| delete | 15:21:30.814 | 15:21:31.732 | 28 removed |
| restart: mark | 15:21:31.732 | 15:21:31.741 | second 391 of the window |
| restart: kill | 15:21:31.741 | 15:21:31.746 | second 391, exit 0 |
| restart: readings | 15:21:31.746 | 15:22:01.761 | pid 851381, gap 5.548 s |
| resume | 15:22:01.761 | 15:30:41.000 | window 1791731700, PASS |
| complete | 15:30:41.000 | 15:30:41.002 | 61 requests, 0 / 0 outside |

**The pair book's stream in window `1791731700`** opened at second 595, under pid `851381`, 204 s after the restart's `SIGTERM` at second 391 and about 204 s after the run's last request, which started at second 390 and lasted 0.8 s, ended. It streamed in **2 segments**, 237,078 frames and 19,346,486 stored bytes (G-RESUME's `window.json`, and `service.log` below). No request of the run fell inside its seconds 595 to 905. `service.log`'s tail, §2.13, also shows window `1791725400`, from 13:30 UTC, streamed in 2 segments before any step of this TZ ran; the six windows it shows between them, `1791726300` to `1791730800`, streamed in 1 each. This is recorded and not interpreted: B3's measurement reads segments against request times (§4.9).

### 2.11 §3.9 — `final`: G-UNIT, G-STILL and G-TIMER (V12): **FINAL PASS** — `logs/40-final.log`, verbatim

G-UNIT read **10 checks** at the run's mark's `NRestarts` plus 1 = 3. B-START-SVC was not run.

```
[2026-10-11T15:33:55Z] G-UNIT active           True
[2026-10-11T15:33:55Z] G-UNIT enabled          True
[2026-10-11T15:33:55Z] G-UNIT fragment         True
[2026-10-11T15:33:55Z] G-UNIT control group    True
[2026-10-11T15:33:55Z] G-UNIT ceiling          True
[2026-10-11T15:33:55Z] G-UNIT argv             True
[2026-10-11T15:33:55Z] G-UNIT cwd              True
[2026-10-11T15:33:55Z] G-UNIT cgroup           True
[2026-10-11T15:33:55Z] G-UNIT sole instance    True
[2026-10-11T15:33:55Z] G-UNIT restarts         True
[2026-10-11T15:33:55Z] btc-pairbook.service MainPID 851381, NRestarts 3, MemoryMax 134217728, MemoryCurrent 39620608, MemoryPeak 48504832
[2026-10-11T15:33:55Z] G-UNIT PASS at 3 restarts
[2026-10-11T15:33:55Z] btc-chainbook.service {'MainPID': '0', 'NRestarts': '0', 'ActiveState': 'inactive'}, MemoryCurrent [not set], MemoryPeak [not set]
[2026-10-11T15:33:55Z] btc-pairbook.service {'MainPID': '851381', 'NRestarts': '3', 'ActiveState': 'active'}, MemoryCurrent 39620608, MemoryPeak 48504832
[2026-10-11T15:33:55Z] btc-recorder.service {'MainPID': '4148534', 'NRestarts': '2', 'ActiveState': 'active'}, MemoryCurrent 187318272, MemoryPeak 206311424
[2026-10-11T15:33:55Z] G-STILL PASS: the recorder unchanged since 2026-10-11T14:50:56Z
[2026-10-11T15:33:56Z] G-TIMER loaded                   True
[2026-10-11T15:33:56Z] G-TIMER active                   True
[2026-10-11T15:33:56Z] G-TIMER enabled                  True
[2026-10-11T15:33:56Z] G-TIMER fragment                 True
[2026-10-11T15:33:56Z] G-TIMER its unit                 True
[2026-10-11T15:33:56Z] G-TIMER the calendar             True
[2026-10-11T15:33:56Z] G-TIMER 600 s after it starts    True
[2026-10-11T15:33:56Z] G-TIMER accuracy 1 s             True
[2026-10-11T15:33:56Z] G-TIMER the next calendar elapse True
[2026-10-11T15:33:56Z] the store: 80 window directories, 1791660600 to 1791731700; its stream files 19346486 bytes; free 12940468224 bytes
[2026-10-11T15:33:56Z] the last set's rate: 1474448489 bytes a day
[2026-10-11T15:33:56Z] at that rate the cap stops the streams in 5.41 days, at 2026-10-17T01:28:06Z
[2026-10-11T15:33:56Z] at that rate the floor, base 43500000 bytes a day stops the streams in 5.56 days, at 2026-10-17T05:00:57Z
[2026-10-11T15:33:56Z] at that rate the floor, base 187760570 bytes a day stops the streams in 5.08 days, at 2026-10-16T17:26:02Z
[2026-10-11T15:33:56Z] the next run at 2026-10-12T03:00:20Z; the ledger 10 records
[2026-10-11T15:33:56Z] FINAL PASS
[2026-10-11T15:33:56Z] peak memory of this run: 35979264 bytes
[2026-10-11T15:33:56Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

**The projection at the run's set's rate**, 1,474,448,489 bytes a day: the cap at 2026-10-17 01:28:06 UTC, the floor at 2026-10-17 05:00:57 or 2026-10-16 17:26:02 UTC on its two bases. The daily run resets the count each day (§1), so these are the stops if no further run happened.

### 2.12 Units' memory at every read

| instant (UTC) | read by | recorder `MemoryCurrent` / `MemoryPeak` | pair book `MemoryCurrent` / `MemoryPeak` | archive service |
|---|---|---|---|---|
| 14:50:56 | `I still` | 112,680,960 / 206,311,424 | 2,015,232 / 76,058,624 (pid `815823`) | not installed |
| 15:33:55 | `I final` | 187,318,272 / 206,311,424 | 39,620,608 / 48,504,832 (pid `851381`) | — |
| 15:34:08 | §3.10 `systemctl show` | 166,608,896 / 206,311,424 | 29,429,760 / 48,504,832 | `MemoryPeak` 63,209,472; journal "60.2M memory peak, 0B memory swap peak", 6.552 s CPU |

**The run's `peak_rss`: 36,884,480 bytes**, from its `complete` record. That is under the unit's `MemoryMax` of 134,217,728 and under the TZ's measured 53,043,200.

### 2.13 §3.10 — the closing reads (V15) — `logs/50-closing-reads.log`, verbatim

```
Sun Oct 11 03:34:08 PM UTC 2026
1791732848
1
MemTotal:         978640 kB
MemAvailable:     259204 kB
SwapTotal:       3174396 kB
SwapFree:        2813484 kB
systemd 255 (255.4-1ubuntu8.17)
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12940390400
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
1
active
exit=0
enabled
exit=0
cmp exit=0
e8b46a85d61e1a17841962846f6d3012046c2d70
caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec  /root/btc-pairbook-svc/tz26-nesting-b3-capture.py
MainPID=851381
NRestarts=3
3.12.3
active
inactive
exit=0
enabled
disabled
exit=0
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
/root/btc-pairbook-archive-svc exit=0
/var/lib/btc-pairbook-archive exit=0
/etc/systemd/system/btc-pairbook-archive.service exit=0
/etc/systemd/system/btc-pairbook-archive.timer exit=0
/root/tz27-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd  /root/btc-forensics/tz27-work--archive--set.json
1810
/root/btc-5m-twap       82c5ddc [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/root/tz28-work/wt      d8194fd [tz-28-pairbook-archive-timer]
21356752	/var/lib/btc-pairbook
198757176	/root/.claude
534509162	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/6b7bd886-7088-5233-bdf9-903a19178e6a/scratchpad
total 16
drwx------  4 root root 4096 Oct 11 14:51 .
drwx------ 16 root root 4096 Oct 11 14:48 ..
drwx------  4 root root 4096 Oct 11 14:48 6b7bd886-7088-5233-bdf9-903a19178e6a
drwx------  3 root root 4096 Oct 11 14:48 6de9e261-2fb6-4db9-ae09-1fd283c3b8c8
=== §3.10
MainPID=4148534
NRestarts=2
MemoryCurrent=166608896
MemoryPeak=206311424
ActiveState=active
UnitFileState=enabled

MainPID=851381
NRestarts=3
MemoryCurrent=29429760
MemoryPeak=48504832
ActiveState=active
UnitFileState=enabled

MainPID=0
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=[not set]
ActiveState=inactive
UnitFileState=disabled

MainPID=0
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=63209472
ActiveState=inactive
UnitFileState=static

ActiveState=active
UnitFileState=enabled
NEXT                        LEFT LAST                           PASSED UNIT                       ACTIVATES
Mon 2026-10-12 03:00:20 UTC  11h Sun 2026-10-11 15:18:12 UTC 15min ago btc-pairbook-archive.timer btc-pairbook-archive.service

1 timers listed.
2026-10-11T15:18:12+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-11T15:30:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-11T15:30:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-11T15:30:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 6.552s CPU time, 60.2M memory peak, 0B memory swap peak.
[2026-10-11T15:21:30Z] V 1791726300-stream.jsonl.gz id 631066868 state uploaded api True bytes 18986113 digest sha256:4d2846a58de2c86bdb47f38f9344cd1e406946148b55f798fdb1e6688ac6366c url True download True
[2026-10-11T15:21:30Z] V 1791727200-stream.jsonl.gz id 631066931 state uploaded api True bytes 26477771 digest sha256:70cf67b099f95b6bc54010e65902a0546d4ba240c8b7bfb9a95d40765f7367fa url True download True
[2026-10-11T15:21:30Z] V 1791728100-stream.jsonl.gz id 631067026 state uploaded api True bytes 13402371 digest sha256:8104b837473a07859c2f30a7654c50f243baa0a1376d763d5e341ac63f99a497 url True download True
[2026-10-11T15:21:30Z] V 1791729000-stream.jsonl.gz id 631067091 state uploaded api True bytes 14249655 digest sha256:5731669734a1400fbc74201ace72897316dc8c201eea655394addcf664362767 url True download True
[2026-10-11T15:21:30Z] V 1791729900-stream.jsonl.gz id 631067147 state uploaded api True bytes 19926659 digest sha256:b26db937b1bf4e0abf5b86eeaceb2f799f8c96b5140d71d62f7b0fea02ead959 url True download True
[2026-10-11T15:21:30Z] V 1791730800-stream.jsonl.gz id 631067199 state uploaded api True bytes 15113847 digest sha256:8db51c478756879bf4768d379063bf6be1e7b3e53131f5deff977d1b9a8695ed url True download True
[2026-10-11T15:21:30Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-11T15:21:30Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-11T15:21:30Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-11T15:21:30Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-11T15:21:30Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-11T15:21:30Z] L {"assets_n": 28, "bytes_total": 430047476, "event": "verify", "release_id": 409746510, "run": 1791731892, "verify_sha256": "032adfdbaea0b81d7ea5063eb43130c09396908f05d74be0f1818d2bb2342f64", "wall_ns": 1791732090814504593}
[2026-10-11T15:21:30Z] X 1791706500-stream.jsonl.gz 10095699 f358b90465f20b188bab7ede9ee6f530251bcd8f14801ae47c1d600f9b266db6 removed
[2026-10-11T15:21:30Z] X 1791707400-stream.jsonl.gz 11832348 e918ce4e7dfc25f2384dd666fae937be6c866509c1e12c71d2e33b1dee6801e1 removed
[2026-10-11T15:21:30Z] X 1791708300-stream.jsonl.gz 13211251 0369a1b1a3c40c39728aa8e98336a9c4d2eed76474c657bacfa8f006edf9fa12 removed
[2026-10-11T15:21:30Z] X 1791709200-stream.jsonl.gz 13411606 a28bd92475e3b0e78449d1dfc1b7909715776f49951470ae39767488ace5843f removed
[2026-10-11T15:21:30Z] X 1791710100-stream.jsonl.gz 18371683 a8df4b6d3573730d523dbe6c2b34b5f60f6de36dd7011b87ed08e85107998c27 removed
[2026-10-11T15:21:30Z] X 1791711000-stream.jsonl.gz 14156803 64fdf6f7ef2e7bbb3ebd154199da3facb4325b216f2fb477cb43e928a88b9e30 removed
[2026-10-11T15:21:31Z] X 1791711900-stream.jsonl.gz 14389992 3206e5fd0228b365df4d6c4c647e6c5b18b6f59f88c2bbadced96a77d4c637e9 removed
[2026-10-11T15:21:31Z] X 1791712800-stream.jsonl.gz 13225521 7e88d67513f95c71080d3bc9980a04b26e4587619d2e095f1033d6eb9f62d935 removed
[2026-10-11T15:21:31Z] X 1791713700-stream.jsonl.gz 12494685 ce65c49f450863a0b64db14f0026711da8ca96757d32bb192580799cd84d597b removed
[2026-10-11T15:21:31Z] X 1791714600-stream.jsonl.gz 17326950 ae0aa14b66b5182dc89097bbcbb6cec0d7d714f89098ed110f302fc8a9d0faa3 removed
[2026-10-11T15:21:31Z] X 1791715500-stream.jsonl.gz 11540484 400613f975b563ada9ffd6cbdc9961de6230134ab50e6fbf3875ee7dd9ec82a9 removed
[2026-10-11T15:21:31Z] X 1791716400-stream.jsonl.gz 16012398 5fddd6baf9206d4b05d86760712173a042d855e73cad761a2828d1cdccd0fcfa removed
[2026-10-11T15:21:31Z] X 1791717300-stream.jsonl.gz 14949740 578e165ec258dc443856c457b052d3d2ec1565f0eb9edcb37e074ef7c9a81b4f removed
[2026-10-11T15:21:31Z] X 1791718200-stream.jsonl.gz 13295331 61f6cc2df7c2013906745aee0bfd14c4d5ac43536245285a33ef1b08265f95a3 removed
[2026-10-11T15:21:31Z] X 1791719100-stream.jsonl.gz 15090064 e60b01408ea889c124e14757297e67ee735c43c1351746955f9906334a0d0e60 removed
[2026-10-11T15:21:31Z] X 1791720000-stream.jsonl.gz 14563101 ee7b93b3e29d69c3ec716b32130e8e53d764df45c87c07f001e0732ea20289f4 removed
[2026-10-11T15:21:31Z] X 1791720900-stream.jsonl.gz 14057421 321c45dfaf6697914e35594bd17a104a12d1b1fa6c02fed8883d8884e4a893c3 removed
[2026-10-11T15:21:31Z] X 1791721800-stream.jsonl.gz 13298734 019e4f3c7febb45a63b9f1102df97f5b0d0bf0e7e9fa37a7ee560fe0d0cd7d6d removed
[2026-10-11T15:21:31Z] X 1791722700-stream.jsonl.gz 13411812 a29e3b6989e6d6b79abe173f53578f6d66032a5a10f500959939c033f77d766a removed
[2026-10-11T15:21:31Z] X 1791723600-stream.jsonl.gz 14202184 d3e168396e20bf4da2104c2f2cd63e3bacb8b6bd62b94a83c186638005f61a1f removed
[2026-10-11T15:21:31Z] X 1791724500-stream.jsonl.gz 25796663 a9fd2a97440257bac81a0f5e15710c6a58f9641c5d479a5a96a1d3f464dbd5d2 removed
[2026-10-11T15:21:31Z] X 1791725400-stream.jsonl.gz 17156590 9d3ae93cebfe71903f568e9cf46bdd40d59fbacee62ae6e328783ccff7257720 removed
[2026-10-11T15:21:31Z] X 1791726300-stream.jsonl.gz 18986113 4d2846a58de2c86bdb47f38f9344cd1e406946148b55f798fdb1e6688ac6366c removed
[2026-10-11T15:21:31Z] X 1791727200-stream.jsonl.gz 26477771 70cf67b099f95b6bc54010e65902a0546d4ba240c8b7bfb9a95d40765f7367fa removed
[2026-10-11T15:21:31Z] X 1791728100-stream.jsonl.gz 13402371 8104b837473a07859c2f30a7654c50f243baa0a1376d763d5e341ac63f99a497 removed
[2026-10-11T15:21:31Z] X 1791729000-stream.jsonl.gz 14249655 5731669734a1400fbc74201ace72897316dc8c201eea655394addcf664362767 removed
[2026-10-11T15:21:31Z] X 1791729900-stream.jsonl.gz 19926659 b26db937b1bf4e0abf5b86eeaceb2f799f8c96b5140d71d62f7b0fea02ead959 removed
[2026-10-11T15:21:31Z] X 1791730800-stream.jsonl.gz 15113847 8db51c478756879bf4768d379063bf6be1e7b3e53131f5deff977d1b9a8695ed removed
[2026-10-11T15:21:31Z] G-DELETE every file of the set absent         True
[2026-10-11T15:21:31Z] G-DELETE each removal recorded by delete      True
[2026-10-11T15:21:31Z] G-DELETE each window keeps its window.json    True
[2026-10-11T15:21:31Z] L {"already": 0, "event": "delete", "free_after": 12969091072, "free_before": 12538937344, "freed": 430047476, "gone": 28, "removed": 28, "run": 1791731892, "wall_ns": 1791732091732399708, "windows_kept": 28}
[2026-10-11T15:21:31Z] L {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "815823", "NRestarts": "2", "ns": 1791732091741955625}, "phase": 391, "run": 1791731892, "wall_ns": 1791732091741960838}
[2026-10-11T15:21:31Z] L {"event": "kill", "exit": 0, "phase": 391, "run": 1791731892, "wall_ns": 1791732091746593097}
[2026-10-11T15:22:01Z] G-RESTART a stop of the marked process   True
[2026-10-11T15:22:01Z] G-RESTART stopped inside the band        True
[2026-10-11T15:22:01Z] G-RESTART a start of another process     True
[2026-10-11T15:22:01Z] G-RESTART within 60 s                    True
[2026-10-11T15:22:01Z] G-RESTART the same code                  True
[2026-10-11T15:22:01Z] G-COUNTER started before its window's documents    True
[2026-10-11T15:22:01Z] G-COUNTER the counter equals the store             True
[2026-10-11T15:22:01Z] G-COUNTER the counter below the cap                True
[2026-10-11T15:22:01Z] G-COUNTER no file of the set left                  True
[2026-10-11T15:22:01Z] G-UNIT active                   True
[2026-10-11T15:22:01Z] G-UNIT enabled                  True
[2026-10-11T15:22:01Z] G-UNIT fragment                 True
[2026-10-11T15:22:01Z] G-UNIT control group            True
[2026-10-11T15:22:01Z] G-UNIT ceiling                  True
[2026-10-11T15:22:01Z] G-UNIT argv                     True
[2026-10-11T15:22:01Z] G-UNIT cwd                      True
[2026-10-11T15:22:01Z] G-UNIT cgroup                   True
[2026-10-11T15:22:01Z] G-UNIT sole instance            True
[2026-10-11T15:22:01Z] G-UNIT restarts                 True
[2026-10-11T15:22:01Z] G-UNIT the new start's process  True
[2026-10-11T15:22:01Z] L {"NRestarts": "3", "W": 1791731700, "event": "restart", "free_bytes": 12969062400, "gap_ns": 5548461176, "pid": 851381, "run": 1791731892, "stopped": 815823, "stream_bytes": 0, "wall_ns": 1791732121761569347}
[2026-10-11T15:30:40Z] window 1791731700: pid 851381, documents True; stream opened True, off_reason None, files ['stream.jsonl.gz'], segments 2, frames 237078, stored_bytes 19346486
[2026-10-11T15:30:41Z] G-RESUME run by the restarted process   True
[2026-10-11T15:30:41Z] G-RESUME the stream opened              True
[2026-10-11T15:30:41Z] G-RESUME no reason to keep it off       True
[2026-10-11T15:30:41Z] G-RESUME a stream file                  True
[2026-10-11T15:30:41Z] L {"T": 1791731700, "event": "resume", "reading": "PASS", "run": 1791731892, "wall_ns": 1791732641000772037}
[2026-10-11T15:30:41Z] at the set's rate the cap stops the streams in 5.41 days, at 2026-10-17T01:24:52Z
[2026-10-11T15:30:41Z] at the set's rate the floor, base 43500000 bytes a day stops the streams in 5.57 days, at 2026-10-17T05:06:16Z
[2026-10-11T15:30:41Z] at the set's rate the floor, base 187760570 bytes a day stops the streams in 5.08 days, at 2026-10-16T17:30:37Z
[2026-10-11T15:30:41Z] L {"assets_n": 28, "bytes_total": 430047476, "ended_outside": 0, "event": "complete", "free_bytes": 12949487616, "peak_rss": 36884480, "rate_per_day": 1474448489, "requests": 61, "run": 1791731892, "started_outside": 0, "stops": [["the cap", 1792200292], ["the floor, base 43500000 bytes a day", 1792213576], ["the floor, base 187760570 bytes a day", 1792171837]], "store_stream_bytes": 19346486, "wall_ns": 1791732641002785194}
[2026-10-11T15:30:41Z] COMPLETE: run 1791731892, 28 files, 430047476 bytes, Release pairbook-streams-1791731892
[2026-10-11T15:30:41Z] peak memory of this run: 36884480 bytes
[2026-10-11T15:30:41Z] opens refused: 0; store opens 86; requests 61, uploads 28, downloads 28 (430047476 bytes); files removed 28
[2026-10-11T13:45:10Z] window 1791725400 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 201576 frames, 2 segments, 17156590 bytes stored
[2026-10-11T13:45:10Z] window 1791726300 (2026-10-11T13:45:00Z): documents from 2026-10-11T13:54:05Z
[2026-10-11T14:00:09Z] window 1791726300 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 225478 frames, 1 segments, 18986113 bytes stored
[2026-10-11T14:00:10Z] window 1791727200 (2026-10-11T14:00:00Z): documents from 2026-10-11T14:09:05Z
[2026-10-11T14:15:10Z] window 1791727200 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 311255 frames, 1 segments, 26477771 bytes stored
[2026-10-11T14:15:10Z] window 1791728100 (2026-10-11T14:15:00Z): documents from 2026-10-11T14:24:05Z
[2026-10-11T14:30:10Z] window 1791728100 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 159936 frames, 1 segments, 13402371 bytes stored
[2026-10-11T14:30:10Z] window 1791729000 (2026-10-11T14:30:00Z): documents from 2026-10-11T14:39:05Z
[2026-10-11T14:45:09Z] window 1791729000 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 171704 frames, 1 segments, 14249655 bytes stored
[2026-10-11T14:45:10Z] window 1791729900 (2026-10-11T14:45:00Z): documents from 2026-10-11T14:54:05Z
[2026-10-11T15:00:10Z] window 1791729900 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 235772 frames, 1 segments, 19926659 bytes stored
[2026-10-11T15:00:10Z] window 1791730800 (2026-10-11T15:00:00Z): documents from 2026-10-11T15:09:05Z
[2026-10-11T15:15:10Z] window 1791730800 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 178484 frames, 1 segments, 15113847 bytes stored
[2026-10-11T15:15:10Z] window 1791731700 (2026-10-11T15:15:00Z): documents from 2026-10-11T15:24:05Z
[2026-10-11T15:21:31Z] stop record written; requests 810, sessions 33, frames 5011302, stream bytes 419951777, other bytes 677949
[2026-10-11T15:21:37Z] stale pid file (pid 815823) replaced
[2026-10-11T15:21:37Z] start record: pid 851381 commit e8b46a85d61e1a17841962846f6d3012046c2d70 file_sha256 caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec; free 12969062400 bytes, streams 0 bytes
[2026-10-11T15:21:37Z] window 1791731700 (2026-10-11T15:15:00Z): documents from 2026-10-11T15:24:05Z
[2026-10-11T15:30:10Z] window 1791731700 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 237078 frames, 2 segments, 19346486 bytes stored
[2026-10-11T15:30:10Z] window 1791732600 (2026-10-11T15:30:00Z): documents from 2026-10-11T15:39:05Z
               total        used        free      shared  buff/cache   available
Mem:      1002127360   726880256    80576512      245760   380649472   275247104
Swap:     3250581504   375492608  2875088896
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12940374016
6842252	/root/tz28-work
21356752	/var/lib/btc-pairbook
96724	/var/lib/btc-pairbook-archive
198757176	/root/.claude
{
 "marks28": {
  "enable": {
   "ns": 1791731139112477547,
   "service": {
    "ActiveState": "inactive",
    "Result": "success"
   },
   "timer": {
    "ActiveState": "inactive",
    "UnitFileState": "disabled"
   }
  }
 },
 "still": {
  "at": "2026-10-11T14:50:56Z",
  "recorder": {
   "ActiveState": "active",
   "MainPID": "4148534",
   "NRestarts": "2"
  }
 }
}
```

In §0.3's block re-read here, the four archive paths now print `exit=0` (installed) and the worktree list shows `/root/tz28-work/wt`. `archive.log` and `service.log` hold counts, names, times, statuses and SHA-256 of files only.

### 2.14 Memory, the hook and the counters — every mode (V13)

| mode | log | peak memory | opens refused | store opens | requests | uploads | downloads (bytes) | files removed |
|---|---|---|---|---|---|---|---|---|
| fingerprint (I0) | `logs/02-fingerprint.log` | 35803136 | 0 | 0 | 0 | 0 | 0 (0) | 0 |
| tz27-release (I0) | `logs/06-tz27-release.log` | 37154816 | 0 | 0 | 2 | 0 | 0 (0) | 0 |
| selftest | `logs/13-selftest.log` | 41611264 | 0 | 0 | 56 | 10 | 12 (221334) | 10 |
| still | `logs/14-still.log` | 35983360 | 0 | 0 | 0 | 0 | 0 (0) | 0 |
| scratch | `logs/15-scratch.log` | 35934208 | 0 | 0 | 0 | 0 | 0 (0) | 0 |
| reclaim, scratch | `logs/16-reclaim-scratch.log` | 35938304 | 0 | 0 | 0 | 0 | 0 (0) | 0 |
| path | `logs/18-path.log` | 38338560 | 0 | 0 | 3 | 0 | 1 (76818669) | 0 |
| path-token (the Boss) | `logs/B-PATH-TOKEN.log` | 37150720 | 0 | 0 | 2 | 0 | 0 (0) | 0 |
| installed | `logs/21-installed.log` | 35934208 | 0 | 0 | 0 | 0 | 0 (0) | 0 |
| mark enable | `logs/22-mark-enable.log` | 35979264 | 0 | 0 | 0 | 0 | 0 (0) | 0 |
| timer | `logs/24-timer.log` | 35979264 | 0 | 0 | 0 | 0 | 0 (0) | 0 |
| first, poll 1 | `logs/30-first-01.log` | 35934208 | 0 | 0 | 0 | 0 | 0 (0) | 0 |
| first, poll 2 | `logs/30-first-02.log` | 35934208 | 0 | 0 | 0 | 0 | 0 (0) | 0 |
| first, poll 3 | `logs/30-first-03.log` | 35938304 | 0 | 0 | 0 | 0 | 0 (0) | 0 |
| first, poll 4 (deciding) | `logs/30-first-04.log` | 37158912 | 0 | 2 | 2 | 0 | 0 (0) | 0 |
| final | `logs/40-final.log` | 35979264 | 0 | 0 | 0 | 0 | 0 (0) | 0 |

The run itself (`archive.log` tail, §2.13): opens refused 0; store opens 86; requests 61, uploads 28, downloads 28 (430,047,476 bytes); files removed 28. The deciding `first` made **2** requests, which is `2 + ⌊28/100⌋`, with **2** store opens: `runtime.jsonl` once and `window.json` once. `selftest`'s **10** removals are in its own temporary stores. `started` was not run.

### 2.15 Every file the session wrote, by SHA-256 — `logs/61-files-written.log`

```
2026-10-11T15:34:54Z
--- the session's files under /root/tz28-work (logs hashed as they stand at this read)
3e12e414f8bbe996226157da901381c85b0ce239be909dcb1764c58a9556ec8a  ./logs/00-worktree.log
e5ca8e817c93f62f5defc56b03016efe0fc9bf60064d0036e9ee6e6858bd904b  ./logs/01-stage.log
4e4a81faf096d802d0b1c418069945b4857ae05b106ebb4ec22303bef0e88d92  ./logs/02-fingerprint.log
6e88fdd45bc4f17683f5e3fe413c12be99d2c33355dba07e080b4d3d97478b18  ./logs/03-host-gate.log
de7f4821888143391a588207f403817b04f355a71df73f3d6d32f6ef8f297da7  ./logs/05-refs.log
f083c693b6fac21399574ef1fd4051f3389f8dedc5f3479117c73d1b6d9be64e  ./logs/06-tz27-release.log
5f4e87cf235979aee7782ad6ce111a8e0d4038bba3c32b64d23875434a962788  ./logs/10-branch.log
e35a72fe8db3d07212ebee51855d0bd46e6c5fda1e6ccf39010b830c17de2c46  ./logs/11-commit-push.log
9f8ae1e385d5264e67c727229778fa65c035977b6ace4615217bf873bb7710d6  ./logs/12-pr.log
7b6e5e2d3cf836d28bd1e44d3ffb9c32d8f2fdaffa515240a1ad01157eb4841b  ./logs/13-selftest.log
a8f53c4bee2d39c8af75a5526903f53da48e91411fbe211e988153c118188c37  ./logs/14-still.log
30a1a040e9f58bda7916a9c9ea4c532175a344fb594ef02aef2d9e162edad9bf  ./logs/15-scratch.log
cfeeeb757b7bbd45f7b1e9c42bded5ddba81aec351fe3db62d003604ec6191f8  ./logs/16-reclaim-scratch.log
d891425c960ca731d27a9561063359df52a4fe2136e0db75b423c1fa898c93d1  ./logs/17-rm-scratch.log
67d55977b68e5f99a375e4348f4127891a473491abfee5abefec61d671abea8b  ./logs/18-path.log
a45b6ea27efa55e65d37368668fd28407f66eaf7d5bde3d59bb291d232d3d778  ./logs/20-B-INSTALL.log
25be54c949932e5ef83c0b94a1dfdd2457c7d33e3ff0943456156bbc91c07fd0  ./logs/21-installed.log
cc57f876bee1691a2cdc1f38ad18ea86b2501d2a41c10111e1b5942798fe7a11  ./logs/22-mark-enable.log
cf7152aaafb53906d1b0f2322d2c499615079e343b0d605b79388b5865dcb546  ./logs/23-B-ENABLE.log
370af193fd90cb27bbc87cdd30613d7744a041349f3bb96ad5460879569c16be  ./logs/24-timer.log
48bddd3f6d59e2f7feea78424f15fdfc754028732dc9ded02748e942743a36af  ./logs/30-first-01.log
a4eb85e39f5721c60af33e696733e09758f72766ecfeca726176272409fae61a  ./logs/30-first-02.log
a29112944d68294551377c53cb8438eb9c686b8892ef269f374d5ed66be347c3  ./logs/30-first-03.log
36e3b21084201dda720222f995a4ee010fe7be911afe7b8b64671cb15886b306  ./logs/30-first-04.log
200e82c98efcbe3aa2e6337389cc92c37e525695a9b29be5934cb306eb904781  ./logs/30-first-poll.log
f9b56b1228dfbd658940a3e682beef59e383fae8c613854e0735c6b653300383  ./logs/40-final.log
565bef39c723d1296f6d7cb07f1e9a200d76577b109ad0763a1c90dd40dc02ed  ./logs/50-closing-reads.log
9d604c0a8220c1df8ea19071ceba60334ee275ee3d17faaf37782008a63e1169  ./logs/60-selfcheck.log
1ea28911f806bdf90bcfbae6bfdad78fbc4d5f286bce93bd0758ae6fe70cdc0e  ./logs/B-PATH-TOKEN.log
14b484f0df0b95be0ea97c12371937c76ac4e05ff3a39e2993ca8a1e13ad3c98  ./poll-first.sh
2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7  ./stage/deploy/systemd/btc-pairbook-archive.service
07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913  ./stage/deploy/systemd/btc-pairbook-archive.timer
2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673  ./stage/research/tz27-pairbook-archive.py
46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4  ./stage/research/tz28-pairbook-archive-timer.py
75a781ea3d1500bbf978d5943a295216bc22bff89b3a39828b48267c794fde8d  ./state.json
--- B-INSTALL's files
a6350dda7d53a8790d2cba98380678efbe758e58f81449c3750de65c2107556b  /root/btc-pairbook-archive-svc/commit.txt
2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673  /root/btc-pairbook-archive-svc/tz27-pairbook-archive.py
46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4  /root/btc-pairbook-archive-svc/tz28-pairbook-archive-timer.py
2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7  /etc/systemd/system/btc-pairbook-archive.service
07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913  /etc/systemd/system/btc-pairbook-archive.timer
total 192
drwxr-xr-x  2 root root   4096 Oct 11 15:05 .
drwx------ 27 root root   4096 Oct 11 15:08 ..
-rw-r--r--  1 root root     41 Oct 11 15:05 commit.txt
-rw-r--r--  1 root root 106284 Oct 11 15:05 tz27-pairbook-archive.py
-rw-r--r--  1 root root  74576 Oct 11 15:05 tz28-pairbook-archive-timer.py
--- the branch worktree
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
```

**The run's files under `/var/lib/btc-pairbook-archive/`.** By the instrument: `runs/1791731892/set.json` `ec3983419485fa67317468917eb7b60e2d0e529be4334c7297831ff562471ad0` and `runs/1791731892/verify.json` `032adfdbaea0b81d7ea5063eb43130c09396908f05d74be0f1818d2bb2342f64`, each asserted by `first` against its ledger record. `du -sb` of the directory read 96,724 bytes at 15:34:08. `ledger.jsonl`, `upload.jsonl`, `delete.jsonl`, `transfers.jsonl`, `run.lock` and `archive.log` were not hashed (§6 item 5).

### 2.16 §9 B-RECLAIM-OWN — last, after §3.10, with this report drafted (V16, V17)

Run from the session at 15:38:13 to 15:38:25 UTC. **The classifier refused none of its commands.** Each command ran on its own, and its output is quoted as the session received it.

`I reclaim /root/tz28-work` (`exit` from `${PIPESTATUS[0]}`; the display filtered out the mode's indented per-file lines, §6 item 10):

```
[2026-10-11T15:38:13Z] reclaim: 2286 report tokens; forensic store holds 1810 files
[2026-10-11T15:38:13Z] reclaim: /root/tz28-work/wt skipped: no file but its HEAD's, and HEAD d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3 is its upstream's
[2026-10-11T15:38:13Z] R copied 14b484f0df0b95be0ea97c12371937c76ac4e05ff3a39e2993ca8a1e13ad3c98 /root/btc-forensics/tz28-work--poll-first.sh
[2026-10-11T15:38:13Z] R copied 75a781ea3d1500bbf978d5943a295216bc22bff89b3a39828b48267c794fde8d /root/btc-forensics/tz28-work--state.json
[2026-10-11T15:38:13Z] R copied 3e12e414f8bbe996226157da901381c85b0ce239be909dcb1764c58a9556ec8a /root/btc-forensics/tz28-work--logs--00-worktree.log
[2026-10-11T15:38:13Z] R copied e5ca8e817c93f62f5defc56b03016efe0fc9bf60064d0036e9ee6e6858bd904b /root/btc-forensics/tz28-work--logs--01-stage.log
[2026-10-11T15:38:13Z] R copied 4e4a81faf096d802d0b1c418069945b4857ae05b106ebb4ec22303bef0e88d92 /root/btc-forensics/tz28-work--logs--02-fingerprint.log
[2026-10-11T15:38:13Z] R copied 6e88fdd45bc4f17683f5e3fe413c12be99d2c33355dba07e080b4d3d97478b18 /root/btc-forensics/tz28-work--logs--03-host-gate.log
[2026-10-11T15:38:13Z] R copied de7f4821888143391a588207f403817b04f355a71df73f3d6d32f6ef8f297da7 /root/btc-forensics/tz28-work--logs--05-refs.log
[2026-10-11T15:38:13Z] R copied f083c693b6fac21399574ef1fd4051f3389f8dedc5f3479117c73d1b6d9be64e /root/btc-forensics/tz28-work--logs--06-tz27-release.log
[2026-10-11T15:38:13Z] R copied 5f4e87cf235979aee7782ad6ce111a8e0d4038bba3c32b64d23875434a962788 /root/btc-forensics/tz28-work--logs--10-branch.log
[2026-10-11T15:38:13Z] R copied e35a72fe8db3d07212ebee51855d0bd46e6c5fda1e6ccf39010b830c17de2c46 /root/btc-forensics/tz28-work--logs--11-commit-push.log
[2026-10-11T15:38:13Z] R copied 9f8ae1e385d5264e67c727229778fa65c035977b6ace4615217bf873bb7710d6 /root/btc-forensics/tz28-work--logs--12-pr.log
[2026-10-11T15:38:13Z] R copied 7b6e5e2d3cf836d28bd1e44d3ffb9c32d8f2fdaffa515240a1ad01157eb4841b /root/btc-forensics/tz28-work--logs--13-selftest.log
[2026-10-11T15:38:13Z] R copied a8f53c4bee2d39c8af75a5526903f53da48e91411fbe211e988153c118188c37 /root/btc-forensics/tz28-work--logs--14-still.log
[2026-10-11T15:38:13Z] R copied 30a1a040e9f58bda7916a9c9ea4c532175a344fb594ef02aef2d9e162edad9bf /root/btc-forensics/tz28-work--logs--15-scratch.log
[2026-10-11T15:38:13Z] R copied cfeeeb757b7bbd45f7b1e9c42bded5ddba81aec351fe3db62d003604ec6191f8 /root/btc-forensics/tz28-work--logs--16-reclaim-scratch.log
[2026-10-11T15:38:13Z] R copied d891425c960ca731d27a9561063359df52a4fe2136e0db75b423c1fa898c93d1 /root/btc-forensics/tz28-work--logs--17-rm-scratch.log
[2026-10-11T15:38:13Z] R copied 67d55977b68e5f99a375e4348f4127891a473491abfee5abefec61d671abea8b /root/btc-forensics/tz28-work--logs--18-path.log
[2026-10-11T15:38:13Z] R copied a45b6ea27efa55e65d37368668fd28407f66eaf7d5bde3d59bb291d232d3d778 /root/btc-forensics/tz28-work--logs--20-B-INSTALL.log
[2026-10-11T15:38:13Z] R copied 25be54c949932e5ef83c0b94a1dfdd2457c7d33e3ff0943456156bbc91c07fd0 /root/btc-forensics/tz28-work--logs--21-installed.log
[2026-10-11T15:38:13Z] R copied cc57f876bee1691a2cdc1f38ad18ea86b2501d2a41c10111e1b5942798fe7a11 /root/btc-forensics/tz28-work--logs--22-mark-enable.log
[2026-10-11T15:38:13Z] R copied cf7152aaafb53906d1b0f2322d2c499615079e343b0d605b79388b5865dcb546 /root/btc-forensics/tz28-work--logs--23-B-ENABLE.log
[2026-10-11T15:38:13Z] R copied 370af193fd90cb27bbc87cdd30613d7744a041349f3bb96ad5460879569c16be /root/btc-forensics/tz28-work--logs--24-timer.log
[2026-10-11T15:38:13Z] R copied 48bddd3f6d59e2f7feea78424f15fdfc754028732dc9ded02748e942743a36af /root/btc-forensics/tz28-work--logs--30-first-01.log
[2026-10-11T15:38:13Z] R copied a4eb85e39f5721c60af33e696733e09758f72766ecfeca726176272409fae61a /root/btc-forensics/tz28-work--logs--30-first-02.log
[2026-10-11T15:38:13Z] R copied a29112944d68294551377c53cb8438eb9c686b8892ef269f374d5ed66be347c3 /root/btc-forensics/tz28-work--logs--30-first-03.log
[2026-10-11T15:38:13Z] R copied 36e3b21084201dda720222f995a4ee010fe7be911afe7b8b64671cb15886b306 /root/btc-forensics/tz28-work--logs--30-first-04.log
[2026-10-11T15:38:13Z] R copied 200e82c98efcbe3aa2e6337389cc92c37e525695a9b29be5934cb306eb904781 /root/btc-forensics/tz28-work--logs--30-first-poll.log
[2026-10-11T15:38:13Z] R copied f9b56b1228dfbd658940a3e682beef59e383fae8c613854e0735c6b653300383 /root/btc-forensics/tz28-work--logs--40-final.log
[2026-10-11T15:38:13Z] R copied 565bef39c723d1296f6d7cb07f1e9a200d76577b109ad0763a1c90dd40dc02ed /root/btc-forensics/tz28-work--logs--50-closing-reads.log
[2026-10-11T15:38:13Z] R copied 9d604c0a8220c1df8ea19071ceba60334ee275ee3d17faaf37782008a63e1169 /root/btc-forensics/tz28-work--logs--60-selfcheck.log
[2026-10-11T15:38:13Z] R copied 304026d3afb8448c42e8b19315cff2804491915b2d34dfdb518de6646383b5e5 /root/btc-forensics/tz28-work--logs--61-files-written.log
[2026-10-11T15:38:13Z] R copied 1ea28911f806bdf90bcfbae6bfdad78fbc4d5f286bce93bd0758ae6fe70cdc0e /root/btc-forensics/tz28-work--logs--B-PATH-TOKEN.log
[2026-10-11T15:38:13Z] R copied 2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7 /root/btc-forensics/tz28-work--stage--deploy--systemd--btc-pairbook-archive.service
[2026-10-11T15:38:13Z] R copied 07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913 /root/btc-forensics/tz28-work--stage--deploy--systemd--btc-pairbook-archive.timer
[2026-10-11T15:38:13Z] R copied 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673 /root/btc-forensics/tz28-work--stage--research--tz27-pairbook-archive.py
[2026-10-11T15:38:13Z] R copied 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4 /root/btc-forensics/tz28-work--stage--research--tz28-pairbook-archive-timer.py
[2026-10-11T15:38:13Z] RECLAIM PASS: 38 files considered, 35 named by a report, 1 kept by name, 36 copied, 0 already held; forensic store 1810 -> 1846 files
[2026-10-11T15:38:13Z] peak memory of this run: 35713024 bytes
[2026-10-11T15:38:13Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

Of the 38 files considered, the two not copied are `build-report.py` and `report-template.md`, which no report names and which are not kept by name. The worktree was skipped, as §9 says: it is clean, and its `HEAD` is its upstream's.

```
$ git -C /root/btc-5m-twap worktree remove /root/tz28-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz28-work; echo "exit=$?"
exit=0
$ test -e /root/tz28-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       82c5ddc [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
1846
$ df -B1 --output=source,size,avail /var/lib
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12947021824
```

(`df` was read at 15:38:25 UTC.) **V16:** 38 considered, 35 named by a report, 1 kept by name, 36 copied, 0 already held; the store went from 1,810 to 1,846, which is 1,810 + 36. **V17:** `git worktree remove` without `--force` exited `0`; `test -e /root/tz28-work` exited `1`; the worktree list names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else. In §2.4, both earlier directories gave `test -e` exit `1`. **Kept:** `/root/btc-pairbook-archive-svc/`, `/var/lib/btc-pairbook-archive/`, `/root/btc-pairbook-svc/`, `/root/btc-recorder-svc/` and `/root/tz18a-svc/`; the branch `tz-28-pairbook-archive-timer`, on `origin` and as a local ref; and the run's tag and Release.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-28-pairbook-archive-timer`, commit `d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3`, pushed; its upstream equals its head |
| pull request | #27, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/27`, open, not merged by the Executor |
| first run's tag | `pairbook-streams-1791731892`, lightweight: `git ls-remote` prints `d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3 refs/tags/pairbook-streams-1791731892` with no peeled line |
| first run's Release | id `409746510`, created by the unit's run under the credential the unit reads, published and not the latest; 28 assets, 430,047,476 bytes |
| report | `CryptoReports/TZ-28-pairbook-archive-timer-report.md`, to `main` in one commit |

**Contract §5.1, per asset — every `ROW` line `first` printed**: the set's SHA-256 (the local hash), the Release's `digest`, the downloaded SHA-256, and the SHA-256 of the file hashed again before its removal. **All four are equal in 28 of 28 rows** (the checker asserts this):

| asset | bytes | set SHA-256 = digest = download = removed |
|---|---|---|
| `1791706500-stream.jsonl.gz` | 10,095,699 | `f358b90465f20b188bab7ede9ee6f530251bcd8f14801ae47c1d600f9b266db6` |
| `1791707400-stream.jsonl.gz` | 11,832,348 | `e918ce4e7dfc25f2384dd666fae937be6c866509c1e12c71d2e33b1dee6801e1` |
| `1791708300-stream.jsonl.gz` | 13,211,251 | `0369a1b1a3c40c39728aa8e98336a9c4d2eed76474c657bacfa8f006edf9fa12` |
| `1791709200-stream.jsonl.gz` | 13,411,606 | `a28bd92475e3b0e78449d1dfc1b7909715776f49951470ae39767488ace5843f` |
| `1791710100-stream.jsonl.gz` | 18,371,683 | `a8df4b6d3573730d523dbe6c2b34b5f60f6de36dd7011b87ed08e85107998c27` |
| `1791711000-stream.jsonl.gz` | 14,156,803 | `64fdf6f7ef2e7bbb3ebd154199da3facb4325b216f2fb477cb43e928a88b9e30` |
| `1791711900-stream.jsonl.gz` | 14,389,992 | `3206e5fd0228b365df4d6c4c647e6c5b18b6f59f88c2bbadced96a77d4c637e9` |
| `1791712800-stream.jsonl.gz` | 13,225,521 | `7e88d67513f95c71080d3bc9980a04b26e4587619d2e095f1033d6eb9f62d935` |
| `1791713700-stream.jsonl.gz` | 12,494,685 | `ce65c49f450863a0b64db14f0026711da8ca96757d32bb192580799cd84d597b` |
| `1791714600-stream.jsonl.gz` | 17,326,950 | `ae0aa14b66b5182dc89097bbcbb6cec0d7d714f89098ed110f302fc8a9d0faa3` |
| `1791715500-stream.jsonl.gz` | 11,540,484 | `400613f975b563ada9ffd6cbdc9961de6230134ab50e6fbf3875ee7dd9ec82a9` |
| `1791716400-stream.jsonl.gz` | 16,012,398 | `5fddd6baf9206d4b05d86760712173a042d855e73cad761a2828d1cdccd0fcfa` |
| `1791717300-stream.jsonl.gz` | 14,949,740 | `578e165ec258dc443856c457b052d3d2ec1565f0eb9edcb37e074ef7c9a81b4f` |
| `1791718200-stream.jsonl.gz` | 13,295,331 | `61f6cc2df7c2013906745aee0bfd14c4d5ac43536245285a33ef1b08265f95a3` |
| `1791719100-stream.jsonl.gz` | 15,090,064 | `e60b01408ea889c124e14757297e67ee735c43c1351746955f9906334a0d0e60` |
| `1791720000-stream.jsonl.gz` | 14,563,101 | `ee7b93b3e29d69c3ec716b32130e8e53d764df45c87c07f001e0732ea20289f4` |
| `1791720900-stream.jsonl.gz` | 14,057,421 | `321c45dfaf6697914e35594bd17a104a12d1b1fa6c02fed8883d8884e4a893c3` |
| `1791721800-stream.jsonl.gz` | 13,298,734 | `019e4f3c7febb45a63b9f1102df97f5b0d0bf0e7e9fa37a7ee560fe0d0cd7d6d` |
| `1791722700-stream.jsonl.gz` | 13,411,812 | `a29e3b6989e6d6b79abe173f53578f6d66032a5a10f500959939c033f77d766a` |
| `1791723600-stream.jsonl.gz` | 14,202,184 | `d3e168396e20bf4da2104c2f2cd63e3bacb8b6bd62b94a83c186638005f61a1f` |
| `1791724500-stream.jsonl.gz` | 25,796,663 | `a9fd2a97440257bac81a0f5e15710c6a58f9641c5d479a5a96a1d3f464dbd5d2` |
| `1791725400-stream.jsonl.gz` | 17,156,590 | `9d3ae93cebfe71903f568e9cf46bdd40d59fbacee62ae6e328783ccff7257720` |
| `1791726300-stream.jsonl.gz` | 18,986,113 | `4d2846a58de2c86bdb47f38f9344cd1e406946148b55f798fdb1e6688ac6366c` |
| `1791727200-stream.jsonl.gz` | 26,477,771 | `70cf67b099f95b6bc54010e65902a0546d4ba240c8b7bfb9a95d40765f7367fa` |
| `1791728100-stream.jsonl.gz` | 13,402,371 | `8104b837473a07859c2f30a7654c50f243baa0a1376d763d5e341ac63f99a497` |
| `1791729000-stream.jsonl.gz` | 14,249,655 | `5731669734a1400fbc74201ace72897316dc8c201eea655394addcf664362767` |
| `1791729900-stream.jsonl.gz` | 19,926,659 | `b26db937b1bf4e0abf5b86eeaceb2f799f8c96b5140d71d62f7b0fea02ead959` |
| `1791730800-stream.jsonl.gz` | 15,113,847 | `8db51c478756879bf4768d379063bf6be1e7b3e53131f5deff977d1b9a8695ed` |

**Contract §4.2's self-check, and V14's further line** — `logs/60-selfcheck.log`, verbatim:

```
$ git rev-list origin/main | grep -c d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
0
$ git diff --name-only origin/main origin/tz-28-pairbook-archive-timer
deploy/systemd/btc-pairbook-archive.service
deploy/systemd/btc-pairbook-archive.timer
research/tz28-pairbook-archive-timer.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
$ git ls-tree -r --name-only origin/main | grep -c -e '\.gz$' -e '\.jsonl$'
0
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1791731892
```

The first line is `0`. The diff names only the three paths. Nothing matches `.parquet` or `.zip`. The `.gz`/`.jsonl` count is `0`. The last line is the tag's `ls-remote`.

---

## 4. Gate

| gate | TZ's PASS condition | deciding read | result |
|---|---|---|---|
| G-TZ27 | §0.6: `G-TZ27 PASS` | 51 of 51 assets, Release `409534533`, 2 requests | **PASS** |
| P-PATH | §4.1: `READING P-PATH: served` | 3 of 3 requests inside the idle stretch; 76,818,669 bytes equal | **PASS** |
| P-TOKEN | §4.2: `READING P-TOKEN: served` and `exit=0` | the remote URL's credential, push true, Release `409534533`, 2 requests | **PASS** |
| G-INSTALL | §4.4: `G-INSTALL PASS: 8 of 8` | 8 of 8 | **PASS** |
| G-TIMER | §4.5: nine checks | 9 of 9 at §3.7 and at `final` | **PASS** |
| G-TRIGGER | `LastTriggerUSec` within 2 s of `ActiveEnterTimestamp` + 600, and the first record within 60 s | started 15:08:11, triggered 15:18:12: 601 s, within 2 s of 600; the run's first record at 15:18:12, 0 s after | **PASS** |
| G-RUN | `complete`, `Result` `success`, `ExecMainStatus` `0` | as stated | **PASS** |
| G-SET | one set record, its SHA-256, rebuilt equal | `ec398341…`, 28 files | **PASS** |
| G-UPLOAD | Release by its record; lightweight tag at the run's commit | 28 of 28, 0 missing, 0 beyond; tag at `d8194fd…`, no peel | **PASS** |
| G-DOWNLOAD | `verify.json`, every download equal | 28 of 28, 430,047,476 bytes | **PASS** |
| G-DELETE | `tz27.removed_reading` | 3 of 3: 28 gone, 28 recorded, 28 windows kept | **PASS** |
| G-RESTART | TZ-27 §4.5's five checks | 5 of 5, stop at second 391, start 5.548 s later | **PASS** |
| G-COUNTER | four checks, and `stream_bytes` the store's | 4 of 4; `0` = `0` | **PASS** |
| G-UNIT | ten checks at `NRestarts` 3, `MainPID` the start record's | 10 of 10 at the run, `first` and `final`; `851381` | **PASS** |
| G-RESUME | PASS or UNDECIDABLE | PASS, window `1791731700` | **PASS** |
| G-IDLE | every request inside its stretch | 61 of 61; 0 started outside, 0 ended outside | **PASS** |
| G-STILL | the recorder unchanged | `4148534`, `NRestarts` 2, `active`, 14:50:56 to 15:33:55 | **PASS** |

Nothing was tuned, and no gate was reinterpreted. No stop of §4.8 was authorized, so none was run.

---

## 5. Validation

| # | check | count | asserted |
|---|---|---|---|
| V1 | §0.2's fingerprint | `FINGERPRINT PASS`: revision `2026-10-11-b`; anchors 6 of 6, 4 re-derived; 37 rows, 34 of 34 `frozen` equal, 2 tracked, 1 reported | asserted, in `fingerprint` |
| V2 | §0.3's host gate | H1 to H5, memory and disk: 7 of 7; the rest printed | read and compared by the Executor against the TZ's literals (§0.3 table); recorded, not asserted by a script |
| V3 | §0.1's and §3.1's files | 3 of 3 hashes asserted at each, with lines and bytes; TZ-27's staged copy `2cba96bc…`; the branch's diff names three paths, each `A` | hashes asserted by the extraction script; the diff recorded, not asserted |
| V4 | the self-test | `34 of 34 checks passed` | asserted |
| V5 | G-TZ27 | `G-TZ27 PASS`, 51 of 51, Release `409534533`, 2 requests | asserted |
| V6 | P-PATH | `READING P-PATH: served`, 3 requests, each inside the stretch; `uploaded`, 76,818,669, `sha256:229a944f…`, URL; `200`, 76,818,669, equal | asserted |
| V7 | P-TOKEN | `READING P-TOKEN: served`, the source the primary checkout's remote URL, push true, Release `409534533`, 2 requests; `exit=0` (the Boss's terminal) | asserted |
| V8 | B-INSTALL and G-INSTALL | 7 of 7 `exit=0`; `G-INSTALL PASS: 8 of 8` | G-INSTALL asserted; the exits recorded |
| V9 | B-ENABLE and G-TIMER | second of the day 54,491 in 11,100 to 73,200, `exit=0`; `G-TIMER PASS`, 9 checks, at §3.7 and at `final` | the band in the block's own text; G-TIMER asserted |
| V10 | the first run | `FIRST PASS: 11 of 11`; 10 `R` records; 79 `W`; 28 `S`; `ROW` 28 of 28; 61 `T` | asserted, in `first` |
| V11 | B-RETRY | not run | — |
| V12 | final | `FINAL PASS`: G-UNIT 10 checks at 3 restarts; G-STILL; G-TIMER 9; the projection | asserted, in `final` |
| V13 | the hook and the counters | opens refused 0 at every mode; requests 2 / 3 / 2 / 2 at `tz27-release` / `path` / `path-token` / deciding `first`; store opens 0 at every mode but `first`, 2 there (`started` not run); files removed 0 at every session mode but `selftest`, 10 | printed by every mode (§2.14); the counts recorded, not asserted |
| V14 | contract §4.2 and the line below | `0`; three paths; nothing; `0` | recorded, not asserted |
| V15 | §3.10's closing reads | every read printed (§2.13) | recorded |
| V16 | §9's `reclaim` runs | see §2.4 and §2.16 | asserted, in `reclaim` |
| V17 | §9's removals | see §2.4 and §2.16 | recorded |

---

## 6. What could not be implemented as written

1. **B-ENABLE was refused by the session's classifier** ("[Auto-Mode Bypass]") and run by the Boss, verbatim, at 15:08:11 UTC (`second of the day=54491`), as §3 routes it. `logs/23-B-ENABLE.log` was written by the Executor from the Boss's pasted terminal output, with a header saying so. The enable itself was verified from the session through the timer's `ActiveEnterTimestamp` and G-TIMER. No other block was refused. B-INSTALL, B-RECLAIM-SCRATCH's two `rm -rf` and B-RECLAIM-OWN (§2.16) ran from the session.
2. **B-PATH-TOKEN's `exit=0`** comes from the Boss's terminal, because `tee` does not capture the `echo` after the pipe. The log holds the `READING P-TOKEN: served` line, which prints only after every assert has held.
3. **`first` was polled by a background shell loop**, `/root/tz28-work/poll-first.sh` (SHA-256 `14b484f0…`, §2.15), which ran `I first` at 15:18:41 and every 300 s after while it exited 3. It wrote each run's output to `logs/30-first-NN.log` and a summary line to `logs/30-first-poll.log`. The harness also tailed `logs/30-first-poll.log` to notify the session. Neither touched `/var/lib/`.
4. **The run's own `MemAvailable` and free-space floor line** (`floors`, written at 15:18:12) is not quoted. It is in `archive.log` above §3.10's `tail -n 80`, and §2 item 3 allows the session no other read of that file. The run's free-space reads quoted in §0.4 come from its ledger records, as `first` printed them. For the same reason, §8's "first and last stamped line of each step — its `L` records in `archive.log`" is given in §2.10 from the `R` records' `wall_ns` and the `T` lines. `archive.log`'s lines from the verify's `V` lines onward are quoted verbatim in §2.13.
5. **§8 asks for "every file the run … wrote, by SHA-256"; §2 item 3 restricts the session's reads under `/var/lib/btc-pairbook-archive/`** to the instrument's reads, §3.10's `tail` and `du`, and §4.8's `tail` of the ledger. The instrument prints the SHA-256 of `set.json` and `verify.json` and asserts both. `ledger.jsonl`, `upload.jsonl`, `delete.jsonl`, `transfers.jsonl`, `run.lock` and `archive.log` were not hashed, because hashing them would open them outside the reads §2 names. The prohibition was kept over the report item.
6. **The store's `du` does not equal the freed bytes:** it fell from 396,936,979 bytes (14:50:02) to 21,356,752 (15:34:08), 375,580,227 bytes, while the run removed 430,047,476. The pair book kept writing in between, so the two are not comparable. The freed figure is the run's own sum of the removed files, asserted by `removed_reading`.
7. **The opening refs log is `logs/05-refs.log`, and there is no `logs/04-…`.** This is a naming choice only, with one file per step.
8. **The report was drafted from a template by a script** (`/root/tz28-work/build-report.py`) that embeds each log verbatim and computes §2.10's and §2.14's tables and §3's rows from the logs. A checker in the same script asserted the typed figures against the logs before B-RECLAIM-OWN. The script and template were reclaimed with the tree. §2.16 was pasted in by hand after B-RECLAIM-OWN, from the session's output.
9. **`I scratch` named `6de9e261…` live**: it was born with process `847634`, which runs this session. It was kept, together with this session's own `6b7bd886…`. Both are the next TZ's to reclaim.

10. **B-RECLAIM-OWN's `reclaim` output, as quoted in §2.16, omits the mode's indented per-file lines.** The session ran it through a `grep -v` that hid lines beginning with three spaces after the stamp. Those lines were not saved anywhere, as §9 requires. Every `R copied` line, the `RECLAIM PASS` counts and the counters line are quoted whole. Re-running the mode after the removal was not possible.
