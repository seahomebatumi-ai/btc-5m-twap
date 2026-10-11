# TZ-27 report — the pair book's streams, moved to a Release before the cap stops them

**P-PATH: served** — 3 requests with no token: the Release `tz-01a-dataset`'s record carries `digest` `sha256:229a944f…` equal, and the download returned `200`, 76,818,669 bytes, SHA-256 equal. **G-SET PASS** — **51 files from 51 windows, 678,739,504 bytes**, windows `1791660600` to `1791705600`, 0 deferred, as of `A` = `1791706862` (2026-10-11 08:21:02 UTC). Both runs exited `0` and the second printed `unchanged`.
**The tag** `tz-27-pairbook-streams` is an annotated tag, object `e299d4e45f48b7efaa8cb18bd54b139fc0627630`, on the branch head `bce5a85be7850a33f95192265b916cc9c5e0aaf1`. **The Release** id is `409534533`, created by the Boss's B-UPLOAD in one run: 51 sent, 0 kept from an earlier run.
**G-UPLOAD PASS and G-DOWNLOAD PASS** (`VERIFY PASS`). By the Release's own record, 51 of 51 assets read `uploaded`, with the set's bytes, the set's `sha256:` digest and the expected URL. 51 of 51 anonymous downloads were equal: 678,739,504 bytes, every SHA-256 the set's.
**G-DELETE PASS** — `DELETE PASS` 51 of 51 removed, each hashed equal immediately before its removal; `REMOVED PASS` 3 of 3. **Freed:** `du` of the store fell by exactly 678,739,504 bytes, from 690,132,167 to 11,392,663. `delete`'s own free-space reads rose by 678,916,096 bytes. **The Boss ran B-DELETE**, because the session's classifier refused `I delete`.
**G-RESTART PASS** — the `SIGTERM` at phase 426 stopped pid `752775`, and pid `815823` started 5.647 s later on the same code. **G-COUNTER PASS** — the start record's `stream_bytes` reads `10,095,699`, equal to the store and below `8,000,000,000`. **G-UNIT PASS** at 2 restarts, 10 of 10, read at both `restart` and `final`.
**G-RESUME PASS** — window `1791707400`, run by pid `815823`: the stream opened, no reason kept it off, 1 stream file, 142,057 frames.
**G-STILL PASS** — the recorder unit was unchanged from 08:20:14 to 08:46:03 UTC: pid `4148534`, `NRestarts` 2, `active`.
**The pair book runs and streams.** It is `btc-pairbook.service`, pid `815823`, `NRestarts` 2, `active` and `enabled`. This was verified by `I restart`, `I resume` and `I final`, and by §3.12's `systemctl show`, `journalctl` and `service.log`, quoted below — not from the Boss's account.
**Free space after:** `12,964,560,896` bytes on `/dev/vda2`, at 08:46:16 UTC, before B-RECLAIM-OWN; `12,970,258,432` bytes at B-RECLAIM-OWN's `df`, about 08:50 UTC after it. `final` projects the next stop at the set's own rate, 1,277,627,302 bytes a day: the cap at 2026-10-17 14:38:02 UTC, the floor at 03:24:00 to 18:32:17 UTC the same day.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-27-pairbook-archive.md`, 2,870 lines, 176,552 bytes, SHA-256 `2e79e204200c6162b730ee2b3fb0ad9a51296a4d0fc838e202c25aaeee2d8db8`, landed at `c8352f5` |
| map revision | `2026-10-11-a`, equal; anchors 6 of 6; re-derived 4 of 4; rows 36; `frozen` equal 33 of 33 |
| executor model | Opus, as the TZ names: `get_session` read `session_context.model` and `last_served_model` as `claude-opus-5-5` |
| branch | `tz-27-pairbook-archive` at `bce5a85be7850a33f95192265b916cc9c5e0aaf1`, pushed; pull request #26, open, not merged |
| instrument | `research/tz27-pairbook-archive.py`, 2,078 lines, 106,284 bytes, SHA-256 `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673`, Appendix A byte for byte |
| tag | `tz-27-pairbook-streams`, object `e299d4e45f48b7efaa8cb18bd54b139fc0627630`, peels to `bce5a85…`, pushed by B-TAG |
| Release | id `409534533` on `tz-27-pairbook-streams`, published and not a draft, 51 assets `application/gzip`, `https://github.com/seahomebatumi-ai/btc-5m-twap/releases/tag/tz-27-pairbook-streams` |
| interpreter | `/root/tz04a-env/venv/bin/python` 3.12.3; every mode under `nice -n 19` and `-B` |
| requests | `path`: 3, anonymous. B-UPLOAD, run by the Boss: 54, under the credential from the primary checkout's remote URL. `verify`: 53, anonymous, with 51 downloads. Self-test: 39, all to `127.0.0.1`. Also `git` against `origin` and `gh` for the pull request. None to a venue host |
| credential | read by `upload` alone, in the Boss's shell, which printed only its source: `the primary checkout's remote URL`. The Executor never read, printed or stored it |
| recorder's capture | §0.3's `df`, `find` and `grep -c` at both runs; nothing else |
| chain book | nothing under its root was opened or listed. Its unit was read by `systemctl` alone: `inactive`, `disabled` |
| pair book | read by `inventory`, `upload`, `delete`, `removed`, `restart`, `resume` and `final` alone. Outside the instrument: `du -sb` at §0.3, §3.8 and §3.12; §0.3's `test -s`; and §3.12's `tail -n 20 service.log`. **Nothing was decompressed** |
| pricer | not read, not called, not scored; `A6` `729f0bcdbee3` is stated so that what was not scored is not in doubt |

This report prints no price, size, side, book hash or outcome. Every figure below is a count, a time, a status, a byte count or a file's SHA-256, copied from the instrument's own output. The one exception is §3's per-asset table, which a short script assembled from the instrument's four archive files by string comparison alone (§6 item 5).

---

## 0. Fingerprint

Contract §1 steps 3 and 4 ran inside the instrument, as `I0 fingerprint` (§0.2), which asserts each step. Results:

- **Revision and anchors:** the map revision string `2026-10-11-a` and the six anchors of the TZ header were read, all equal.
- **Re-derived anchors:** `A2`, `A4`, `A5` and `A6` were re-derived, 4 of 4 equal.
- **Table rows:** the table has 36 rows. 33 are `frozen`, each equal to the map in lines, bytes and SHA-256; 2 are `tracked`; 1 is `reported`.
- **`SYSTEM-MAP.md`:** 1,358 lines, 302,505 bytes, SHA-256 `f5084ea08cfe52477d264bfcbec102cef3984cab7aaea93b4bab75026c974294`.

| anchor | required | read |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` |
| `A2` — collector | `6c5089330629` | `6c5089330629`, re-derived |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | equal |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b`, re-derived |
| `A5` — recorder | `0f6c90451cbd` | `0f6c90451cbd`, re-derived |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3`, re-derived |

### 0.1 The 36 rows of the map's §0 table, and the map (V1) — `logs/02-fingerprint.log`, verbatim

```
Sun Oct 11 08:19:03 AM UTC 2026
[2026-10-11T08:19:03Z] re-derived A2 research/twap-divergence.py sha256[:12] 6c5089330629 equal
[2026-10-11T08:19:03Z] re-derived A4 BTC-EXECUTOR-INSTRUCTIONS.md sha256[:12] 437b45ea196b equal
[2026-10-11T08:19:03Z] re-derived A5 research/recorder/recorder.py sha256[:12] 0f6c90451cbd equal
[2026-10-11T08:19:03Z] re-derived A6 research/pfair.py sha256[:12] 729f0bcdbee3 equal
[2026-10-11T08:19:03Z] SYSTEM-MAP.md                                  1358 lines   302505 bytes f5084ea08cfe52477d264bfcbec102cef3984cab7aaea93b4bab75026c974294 reported
[2026-10-11T08:19:03Z] BTC-EXECUTOR-INSTRUCTIONS.md                    234 lines    11128 bytes 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b frozen equal
[2026-10-11T08:19:03Z] research/twap-divergence.py                    1135 lines    50928 bytes 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 frozen equal
[2026-10-11T08:19:03Z] research/selftest-twap-divergence.py            376 lines    16736 bytes ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a frozen equal
[2026-10-11T08:19:03Z] research/tz02-distribution.py                   334 lines    14511 bytes f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 tracked
[2026-10-11T08:19:03Z] research/pfair.py                               441 lines    19357 bytes 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 frozen equal
[2026-10-11T08:19:03Z] research/selftest-pfair.py                      619 lines    32559 bytes b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa frozen equal
[2026-10-11T08:19:03Z] research/tz06-calibration.py                    577 lines    27138 bytes 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f frozen equal
[2026-10-11T08:19:03Z] research/tz07a-variance-time.py                 623 lines    28414 bytes 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 frozen equal
[2026-10-11T08:19:03Z] research/tz07b-settlement-dispersion.py         515 lines    24926 bytes 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc frozen equal
[2026-10-11T08:19:03Z] research/tz08a-out-of-sample.py                 745 lines    38822 bytes 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c frozen equal
[2026-10-11T08:19:03Z] research/tz09-disk-inventory.py                 894 lines    41004 bytes b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 frozen equal
[2026-10-11T08:19:03Z] research/tz10b-sigma-or-link.py                1224 lines    61018 bytes 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 frozen equal
[2026-10-11T08:19:03Z] research/tz11a-student-link.py                 1231 lines    64732 bytes 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 frozen equal
[2026-10-11T08:19:03Z] research/tz12-sized-gate.py                    1157 lines    61637 bytes d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 frozen equal
[2026-10-11T08:19:03Z] research/tz13-sized-gate-test3.py              1074 lines    53901 bytes a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd frozen equal
[2026-10-11T08:19:03Z] research/tz14-quote-inventory.py               2124 lines   109972 bytes 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 frozen equal
[2026-10-11T08:19:03Z] research/tz15-phase2-gate.py                   1517 lines    73799 bytes 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 frozen equal
[2026-10-11T08:19:03Z] research/tz16a-phase2-decisive-gate.py         2198 lines   111192 bytes 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 frozen equal
[2026-10-11T08:19:03Z] research/tz17-settlement-chain.py              1102 lines    38622 bytes e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 frozen equal
[2026-10-11T08:19:03Z] research/tz18a-chainbook-capture.py            1683 lines    69517 bytes e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae frozen equal
[2026-10-11T08:19:03Z] research/tz20-capture-under-systemd.py          771 lines    36528 bytes 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7 frozen equal
[2026-10-11T08:19:03Z] research/tz21-recorder-memory.py               1284 lines    59009 bytes d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f frozen equal
[2026-10-11T08:19:03Z] research/tz23-maker-m0.py                      1184 lines    54885 bytes 6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f frozen equal
[2026-10-11T08:19:03Z] research/tz24-nesting-b2.py                    1535 lines    76142 bytes 4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b frozen equal
[2026-10-11T08:19:03Z] research/tz26-nesting-b3-capture.py            2492 lines   118466 bytes caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec frozen equal
[2026-10-11T08:19:03Z] research/recorder/recorder.py                   651 lines    27821 bytes 0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7 frozen equal
[2026-10-11T08:19:03Z] research/recorder/config.py                     112 lines     4773 bytes 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d frozen equal
[2026-10-11T08:19:03Z] research/recorder/manifest.py                   254 lines    10002 bytes 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 frozen equal
[2026-10-11T08:19:03Z] research/recorder/analyze.py                    813 lines    34705 bytes eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d frozen equal
[2026-10-11T08:19:03Z] research/recorder/probe.py                      227 lines     9324 bytes 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 frozen equal
[2026-10-11T08:19:03Z] research/recorder/selftest.py                   573 lines    30591 bytes c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 frozen equal
[2026-10-11T08:19:03Z] deploy/systemd/btc-recorder.service              23 lines      707 bytes 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1 frozen equal
[2026-10-11T08:19:03Z] deploy/systemd/btc-chainbook.service             22 lines      724 bytes a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2 frozen equal
[2026-10-11T08:19:03Z] deploy/systemd/btc-pairbook.service              22 lines      761 bytes ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8 frozen equal
[2026-10-11T08:19:03Z] .gitignore                                        5 lines      252 bytes 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b tracked
[2026-10-11T08:19:03Z] SYSTEM-MAP.md 1358 lines 302505 bytes sha256 f5084ea08cfe52477d264bfcbec102cef3984cab7aaea93b4bab75026c974294
[2026-10-11T08:19:03Z] FINGERPRINT PASS: revision 2026-10-11-a; anchors 6 of 6, 4 re-derived; rows 36: frozen 33 of 33 equal, tracked 2, reported 1
[2026-10-11T08:19:03Z] peak memory of this run: 29634560 bytes
[2026-10-11T08:19:03Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

### 0.2 §0.0 and §0.1 — the work tree, and the instrument staged

```
Sun Oct 11 08:18:40 AM UTC 2026
Already on 'main'
Your branch is up to date with 'origin/main'.
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * branch            main       -> FETCH_HEAD
Already up to date.
c8352f5 Add files via upload
mkdir /root/tz27-work /root/tz27-work/logs -> exit=0
/root/tz27-work/stage/research/tz27-pairbook-archive.py 2078 106284 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673
exit=0
```

`mkdir` printed `exit=0`, so neither directory existed. The staged copy's line matches §0.1's table: 2,078 lines, 106,284 bytes, `2cba96bc…`.

### 0.3 Host gate — the opening reads, verbatim (V2) — `logs/03-host-gate.log`

```
Sun Oct 11 08:19:12 AM UTC 2026
1791706752
1
MemTotal:         978640 kB
MemAvailable:     304112 kB
SwapTotal:       3174396 kB
SwapFree:        2801356 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12315709440
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
1
active
exit=0
enabled
exit=0
cmp exit=0
runtime exit=0
e8b46a85d61e1a17841962846f6d3012046c2d70
caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec  /root/btc-pairbook-svc/tz26-nesting-b3-capture.py
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
/root/tz26-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
1766
/root/btc-5m-twap       c8352f5 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
680011772	/var/lib/btc-pairbook
196710085	/root/.claude
532185008	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/70b5ba7a-7e9e-5c10-a353-278a1431d82a/scratchpad
total 24
drwx------  6 root root 4096 Oct 11 08:17 .
drwx------ 16 root root 4096 Oct 11 08:17 ..
drwx------  4 root root 4096 Oct 10 19:01 30ec6406-6385-5122-88dc-9ad61b1f2846
drwx------  4 root root 4096 Oct 11 08:17 70b5ba7a-7e9e-5c10-a353-278a1431d82a
drwx------  3 root root 4096 Oct 11 08:17 952e88f3-b9a6-4bd2-b674-b9deebd16088
drwx------  3 root root 4096 Oct 10 18:59 d5dc7bd3-91ab-4f86-bdfc-8d305cb318f9
```

| condition | required | read | |
|---|---|---|---|
| H1 | one path | `/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json` | PASS |
| H2 | `/dev/vda2`, `31612203008`; `grep -c` ≥ 1 | `/dev/vda2`, `31612203008`; `1` | PASS |
| H3 | `active`/0, `enabled`/0, `cmp` 0, `runtime` 0, `e8b46a85…`, `caed70d9…` | all as required | PASS |
| H4 | `3.12.` | `3.12.3` | PASS |
| memory | `MemAvailable` ≥ 93,454,336 | 304,112 kB = 311,410,688 | PASS |
| disk | `avail` ≥ 2,300,000,000 | 12,315,709,440 | PASS |

**Printed, no threshold:** the recorder `active`/`enabled` and the chain book `inactive`/`disabled`, as map §6 says. `telemetry-watch.service` read `disabled` (1) and `inactive` (3). The recorder's tree is at `e3975b5…`. `/root/tz26-work` is absent and the three code trees are present. The forensic store held `1,766` files, as map §3 says. There were 2 worktrees, as map §3 says. The store's `du` read 680,011,772. `I scratch` names the UUID directories (§2.3).

### 0.4 Free space and `MemAvailable` — every read, its instant and its bound

| instant (UTC) | read | free bytes (`/dev/vda2`) | `MemAvailable` | bound |
|---|---|---|---|---|
| 08:19:12 | §0.3 host gate | 12,315,709,440 | 311,410,688 | disk 2,300,000,000; memory 93,454,336 |
| 08:20:54 | `path` floor | — | 308,252,672 | 93,454,336 |
| 08:21:06 | `inventory` 1 | 12,309,204,992 | 262,303,744 | 93,454,336 |
| 08:21:16 | `inventory` 2 | 12,309,114,880 | 252,850,176 | 93,454,336 |
| 08:24:29 | `upload` (Boss) | — | 313,114,624 | 93,454,336 |
| 08:27:46 | `verify` | — | 266,764,288 | 93,454,336 |
| 08:35:53 | B-DELETE's `df` (Boss) | 12,298,158,080 | — | — |
| 08:35:53 | `delete` floor and before | 12,298,153,984 | 276,144,128 | 93,454,336 |
| 08:35:54 | `delete` after | 12,977,070,080 | — | — |
| 08:36:53 | §3.8 `df` after | 12,977,340,416 | — | — |
| 08:37:11 | the restarted process's `start` record | 12,977,250,304 | — | — |
| 08:46:03 | `final` | 12,964,605,952 | — | — |
| 08:46:16 | §3.12 closing reads | 12,964,564,992 / 12,964,560,896 | 305,389,568; `free -b` available 322,220,032 | — |
| about 08:50 | B-RECLAIM-OWN `df` | 12,970,258,432 | — | — |

Every floor held: the lowest `MemAvailable` was 252,850,176, and the lowest free space 12,298,153,984.

### 0.5 Refs (§0.5) — `logs/04-refs.log`, verbatim

```
Sun Oct 11 08:19:20 AM UTC 2026
c8352f51e7acb3060b519d2bc4afdc43f9d98b7c	HEAD
c8352f51e7acb3060b519d2bc4afdc43f9d98b7c	refs/heads/main
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8	refs/heads/tz-23-maker-m0
6f045cffc3601b589d3b8b7a6a9af6f73991e18b	refs/heads/tz-24-nesting-b2
e8b46a85d61e1a17841962846f6d3012046c2d70	refs/heads/tz-26-nesting-b3-capture
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
ee2f6327390ef4d0c6169d1fba1a2ed4ae936dc3	refs/pull/3/head
0e13a5c76dfa2469ff25b3b0dd282872decf6f25	refs/pull/4/head
4216c04673ced76b5b2ac60ef57c9abedc46f9b9	refs/pull/5/head
5ed667afd1b53f036b9f938fcce13c0d709cd77f	refs/pull/6/head
c44af687203d14d5d485d4297c04cfb827096af9	refs/pull/7/head
26bbb61aed774a88355dd5204d8b69fda9135a68	refs/pull/8/head
e2625ea2b5473c311d59a48f32540ce39d58e591	refs/pull/9/head
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
ref lines: 32
--- first-parent commits above 2122705
c8352f51e7acb3060b519d2bc4afdc43f9d98b7c Add files via upload

A	CryptoTZ/TZ-27-pairbook-archive.md
397043a6777ce7a8e70a301c5fb4f7434c80f838 Update SYSTEM-MAP.md

M	SYSTEM-MAP.md
--- revision on main
1
0
```

There are **32** ref lines, as map §1 says. `tz-23-maker-m0` reads `7f5ae3f`, `tz-24-nesting-b2` `6f045cf` and `tz-26-nesting-b3-capture` `e8b46a8`, as map §1 says. **One recorded difference, not BLOCKING:** `main` reads `c8352f5`, not `2122705`, because the upload that carries this TZ sits above it in two first-parent commits. They are `397043a` (`M SYSTEM-MAP.md`) and `c8352f5` (`A CryptoTZ/TZ-27-pairbook-archive.md`). `main` carries revision `2026-10-11-a` (count `1`). Neither `refs/heads/tz-27-pairbook-archive` nor `refs/tags/tz-27-pairbook-streams` existed (count `0`).

---

## 1. Input

- **Read:** `CryptoTZ/TZ-27-pairbook-archive.md`, `SYSTEM-MAP.md` and `BTC-EXECUTOR-INSTRUCTIONS.md`, in full. `SYSTEM-MAP.md` and its 35 table files were read by `fingerprint`.
- **The store** `/var/lib/btc-pairbook/`, as of `A` = `1791706862`: 51 window directories, every one considered (`T + 970 <= A`) and closed, 0 unclosed, 0 still open. Each window holds one stream file, `stream.jsonl.gz`, for 51 stream files and 678,739,504 bytes. That is the whole of the store's stream bytes at `inventory`'s start, `678,739,504`. **Each file was read as bytes for its SHA-256 alone, with its size and modification time equal before and after, and nothing was decompressed.**
- **`tz-01a-dataset`'s Release** was read by `path` alone, through the API and one download.
- **The pair book's `runtime.jsonl`** was read by `restart`. Of `window.json`, `resume` read window `1791707400`'s `pid`, `documents_ok` and stream counts alone.
- **Nothing was re-collected.** The unit's own requests are the unit's.

---

## 2. Measurements

### 2.1 §3.1 — the branch and its file (V3)

```
Sun Oct 11 08:19:35 AM UTC 2026
fetch exit=0
Preparing worktree (new branch 'tz-27-pairbook-archive')
branch 'tz-27-pairbook-archive' set up to track 'origin/main'.
HEAD is now at c8352f5 Add files via upload
worktree exit=0
/root/tz27-work/wt/research/tz27-pairbook-archive.py 2078 106284 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673
extract exit=0
Sun Oct 11 08:19:44 AM UTC 2026
commit exit=0
bce5a85 TZ-27: the pair book's streams archived to a Release - research/tz27-pairbook-archive.py
remote: 
remote: Create a pull request for 'tz-27-pairbook-archive' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-27-pairbook-archive        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-27-pairbook-archive -> tz-27-pairbook-archive
branch 'tz-27-pairbook-archive' set up to track 'origin/tz-27-pairbook-archive'.
push exit=0
bce5a85be7850a33f95192265b916cc9c5e0aaf1
bce5a85be7850a33f95192265b916cc9c5e0aaf1
A	research/tz27-pairbook-archive.py
Sun Oct 11 08:19:53 AM UTC 2026
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/26
exit=0
```

§0.1's script ran again into the worktree and printed the same line as at §0.1, 1 of 1 hash asserted. The branch's diff against `origin/main` names exactly `A research/tz27-pairbook-archive.py`.

### 2.2 §3.2 — the self-test (V4): **63 of 63** — `logs/08-selftest.log`, verbatim

```
Sun Oct 11 08:20:00 AM UTC 2026
[2026-10-11T08:20:00Z]   ok  the band: seconds 15 to 480 of the 900 s window, both included; TZ-26's kill at second 464
[2026-10-11T08:20:00Z]   ok  the service's stream predicate and next_stream_path's names
[2026-10-11T08:20:00Z]   ok  a stream file outside next_stream_path's names stops the run
[2026-10-11T08:20:00Z]   ok  asset, tag and work-tree names
[2026-10-11T08:20:00Z]   ok  the store is read by the modes that need its bytes, and by no other
[2026-10-11T08:20:00Z]   ok  nothing is written under the pair book's root, in any mode
[2026-10-11T08:20:00Z]   ok  only delete removes, only a file it has verified, and nothing is moved or removed whole
[2026-10-11T08:20:00Z]   ok  nothing under the recorder's or the chain book's root is opened or listed
[2026-10-11T08:20:00Z]   ok  the store is listed by inventory, delete, restart and final alone
[2026-10-11T08:20:00Z]   ok  writes go to the work tree, and to the forensic store by reclaim's exclusive create alone
[2026-10-11T08:20:00Z]   ok  inventory and delete start no process
[2026-10-11T08:20:00Z]   ok  the hook refuses /var/lib/btc-recorder/runtime.jsonl before it is opened
[2026-10-11T08:20:00Z]   ok  the hook refuses /var/lib/btc-chainbook/runtime.jsonl before it is opened
[2026-10-11T08:20:00Z]   ok  the hook refuses /var/lib/btc-pairbook/runtime.jsonl before it is opened
[2026-10-11T08:20:00Z]   ok  the hook refuses a removal under the pair book's root outside delete
[2026-10-11T08:20:00Z]   ok  inventory: the stream files of the closed windows, in order, each the bytes written
[2026-10-11T08:20:00Z]   ok  inventory: closed, unclosed without window.json, and the open window counted and not listed
[2026-10-11T08:20:00Z]   ok  a window is taken from T+970, 60 s after its window.json was due
[2026-10-11T08:20:00Z]   ok  the first max_assets taken, the rest deferred and counted
[2026-10-11T08:20:00Z]   ok  a file above a Release asset's limit stops the run
[2026-10-11T08:20:00Z]   ok  stream_bytes_view: the service's counter, whole and over the windows closed before a start
[2026-10-11T08:20:00Z]   ok  the set document, and a second run byte-identical while the open windows grow
[2026-10-11T08:20:00Z]   ok  an empty set stops the run: nothing to archive
[2026-10-11T08:20:00Z]   ok  a numeric directory that is not a window stops the run
[2026-10-11T08:20:00Z]   ok  token_of: both forms of the remote, and None where it carries no credential
[2026-10-11T08:20:00Z]   ok  a remote on another host, repository or scheme stops the run, and no message names the token
[2026-10-11T08:20:00Z]   ok  every header of every request, fixed
[2026-10-11T08:20:00Z]   ok  verify reads the Release only after upload's completion record for the whole set, and 120 s after it
[2026-10-11T08:20:00Z]   ok  a refused upload waits as the reply asks, at least a minute doubling, bounded; 401 and 404 stop
[2026-10-11T08:20:00Z]   ok  a request carrying the token follows no redirect
[2026-10-11T08:20:00Z]   ok  no Release before the first upload
[2026-10-11T08:20:00Z]   ok  upload: three sent, every request under this file's User-Agent
[2026-10-11T08:20:00Z]   ok  upload again: the three kept, nothing sent
[2026-10-11T08:20:00Z] 1791661500-stream.1.jsonl.gz: status 429, attempt 1 of 4; waiting 0 s
[2026-10-11T08:20:00Z]   ok  upload resumes: a partial asset removed and sent again, a refusal waited out, the rest kept
[2026-10-11T08:20:00Z] D 1791660600-stream.jsonl.gz equal bytes 70001 sha256 91a2a8cb7e62e64fb97240214543e1f6e9da9abaa61ee063acfb0e4991230005
[2026-10-11T08:20:00Z] D 1791661500-stream.jsonl.gz equal bytes 50000 sha256 42e65bcfd8f5988fbe0e25da856d343ba9bd4ae706f0ba637edef4700cc1c966
[2026-10-11T08:20:00Z] D 1791661500-stream.1.jsonl.gz equal bytes 33333 sha256 3cacd464d73d72fe584f8a7b3ed76aa18f878d207a8480bc619cd2cfa394e63e
[2026-10-11T08:20:00Z]   ok  verify: every asset by name, bytes, state and digest, three downloads equal, no token sent
[2026-10-11T08:20:00Z] D 1791660600-stream.jsonl.gz DIFFERS bytes 70001 sha256 7d326833ed007736b31715ae1d48b4578bf6ced36c449a67ac3de4768c8a532d
[2026-10-11T08:20:00Z] D 1791661500-stream.jsonl.gz equal bytes 50000 sha256 42e65bcfd8f5988fbe0e25da856d343ba9bd4ae706f0ba637edef4700cc1c966
[2026-10-11T08:20:00Z] D 1791661500-stream.1.jsonl.gz equal bytes 33333 sha256 3cacd464d73d72fe584f8a7b3ed76aa18f878d207a8480bc619cd2cfa394e63e
[2026-10-11T08:20:00Z]   ok  verify: one flipped bit in one asset's bytes reads FAIL
[2026-10-11T08:20:00Z]   ok  verify: an asset without a digest reads FAIL, and nothing is downloaded
[2026-10-11T08:20:00Z]   ok  verify: an asset beyond the set reads FAIL
[2026-10-11T08:20:00Z]   ok  upload refuses a Release holding an asset beyond the set
[2026-10-11T08:20:00Z]   ok  verify: a missing asset reads FAIL
[2026-10-11T08:20:00Z] D 1791660600-stream.jsonl.gz equal bytes 70001 sha256 91a2a8cb7e62e64fb97240214543e1f6e9da9abaa61ee063acfb0e4991230005
[2026-10-11T08:20:00Z] D 1791661500-stream.jsonl.gz equal bytes 50000 sha256 42e65bcfd8f5988fbe0e25da856d343ba9bd4ae706f0ba637edef4700cc1c966
[2026-10-11T08:20:00Z] D 1791661500-stream.1.jsonl.gz equal bytes 33333 sha256 3cacd464d73d72fe584f8a7b3ed76aa18f878d207a8480bc619cd2cfa394e63e
[2026-10-11T08:20:00Z]   ok  upload sends the missing asset again, and verify then reads PASS
[2026-10-11T08:20:00Z]   ok  the asset removed was the file's bytes
[2026-10-11T08:20:00Z]   ok  the loopback server refuses a wrong token, as the venue of every upload would
[2026-10-11T08:20:01Z]   ok  delete: a file changed since the set stops the run, and nothing is removed
[2026-10-11T08:20:01Z]   ok  delete: a window not closed by the instant given stops the run there, each removal before it logged
[2026-10-11T08:20:01Z]   ok  removed reads FAIL before delete
[2026-10-11T08:20:01Z]   ok  removed reads PASS after delete, and FAIL where a removal is not recorded
[2026-10-11T08:20:01Z]   ok  delete: the three files of the set, and every other entry kept
[2026-10-11T08:20:01Z]   ok  the counter a restart reads afterwards: the windows not in the set
[2026-10-11T08:20:01Z]   ok  delete again: each absent file counted where this mode recorded its removal
[2026-10-11T08:20:01Z]   ok  delete: an absent file with no recorded removal stops the run
[2026-10-11T08:20:01Z]   ok  G-RESTART on TZ-26's own records
[2026-10-11T08:20:01Z]   ok  G-RESTART reads FAIL outside the band, after 60 s, on other code, without a start and without a stop
[2026-10-11T08:20:01Z]   ok  G-RESTART reads the first stop after the mark, past an error record
[2026-10-11T08:20:01Z]   ok  G-COUNTER: a start in window W counts the windows up to W - 900, and the set is gone
[2026-10-11T08:20:01Z]   ok  G-COUNTER reads FAIL on a counter that is not the store's, and on a start after its window's documents
[2026-10-11T08:20:01Z]   ok  G-RESUME: the restart's window from T+940; the next window where its documents were not served
[2026-10-11T08:20:01Z]   ok  G-RESUME: the restart's window streamed by the restarted process; the cap or another process reads FAIL
[2026-10-11T08:20:01Z]   ok  the projection: two days of streams at TZ-26's measured rate, the cap and the floor at both bases
[2026-10-11T08:20:01Z]   ok  decimals: half up
[2026-10-11T08:20:01Z]   ok  the temporary store removed
[2026-10-11T08:20:01Z]   ok  imports: the standard library alone
[2026-10-11T08:20:01Z]   ok  exactly three endpoints in the file's text
[2026-10-11T08:20:01Z] 63 of 63 checks passed
[2026-10-11T08:20:01Z] peak memory of this run: 46411776 bytes
[2026-10-11T08:20:01Z] opens refused: 0; store opens 0; requests 39, uploads 7, downloads 9 (460002 bytes); files removed 4
exit=0
Sun Oct 11 08:20:01 AM UTC 2026
```

### 2.3 §3.3 — the units, and the directories beside this session

```
Sun Oct 11 08:20:14 AM UTC 2026
[2026-10-11T08:20:14Z] btc-chainbook.service {'MainPID': '0', 'NRestarts': '0', 'ActiveState': 'inactive'}, MemoryCurrent [not set], MemoryPeak [not set]
[2026-10-11T08:20:14Z] btc-pairbook.service {'MainPID': '752775', 'NRestarts': '1', 'ActiveState': 'active'}, MemoryCurrent 2396160, MemoryPeak 84992000
[2026-10-11T08:20:14Z] btc-recorder.service {'MainPID': '4148534', 'NRestarts': '2', 'ActiveState': 'active'}, MemoryCurrent 112386048, MemoryPeak 206311424
[2026-10-11T08:20:14Z] still: the recorder recorded
[2026-10-11T08:20:14Z] peak memory of this run: 28581888 bytes
[2026-10-11T08:20:14Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
Sun Oct 11 08:20:14 AM UTC 2026
[2026-10-11T08:20:14Z] running 337573 started 2026-10-07T20:05:37Z claude
[2026-10-11T08:20:14Z] running 337576 started 2026-10-07T20:05:37Z claude
[2026-10-11T08:20:14Z] running 813378 started 2026-10-11T08:17:32Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-10-11T08:20:14Z] 30ec6406-6385-5122-88dc-9ad61b1f2846 born 2026-10-10T18:59:38Z: earlier
[2026-10-11T08:20:14Z] 952e88f3-b9a6-4bd2-b674-b9deebd16088 born 2026-10-11T08:17:32Z: live, process [813378]
[2026-10-11T08:20:14Z] d5dc7bd3-91ab-4f86-bdfc-8d305cb318f9 born 2026-10-10T18:59:37Z: earlier
[2026-10-11T08:20:14Z] peak memory of this run: 28717056 bytes
[2026-10-11T08:20:14Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

`I scratch` named `30ec6406…` and `d5dc7bd3…` **earlier**: TZ-26's pair, as map §3 says. It named `952e88f3…` **live**, made by this session's running process `813378`. This session's own directory `70b5ba7a…` is excluded by `scratch` itself.

### 2.4 §9 B-RECLAIM-SCRATCH — after §3.3, before §3.4 (V19, V20)

```
Sun Oct 11 08:20:21 AM UTC 2026
[2026-10-11T08:20:21Z] reclaim: 2044 report tokens; forensic store holds 1766 files
[2026-10-11T08:20:21Z] RECLAIM PASS: 1 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 1766 -> 1766 files
[2026-10-11T08:20:21Z] peak memory of this run: 30523392 bytes
[2026-10-11T08:20:21Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
Sun Oct 11 08:20:47 AM UTC 2026
exit=0
exit=1
Sun Oct 11 08:20:54 AM UTC 2026
rm -rf /tmp/claude-0/-root-btc-5m-twap/d5dc7bd3-91ab-4f86-bdfc-8d305cb318f9 refused by the session's permission classifier: [Irreversible Local Destruction]; handed to the Boss by section 3's route
Sun Oct 11 08:27:24 AM UTC 2026
Boss ran B-UPLOAD at 08:24:29Z-08:25:42Z; his terminal printed exit=0 after the tee'd lines below (logs/B-UPLOAD.log holds the tee)
Boss ran: rm -rf /tmp/claude-0/-root-btc-5m-twap/d5dc7bd3-91ab-4f86-bdfc-8d305cb318f9 -> his terminal printed exit=0
Executor test -e exit=1
   58 logs/B-UPLOAD.log
   52 archive/upload.jsonl
  110 total
{"action": "complete", "assets": 51, "at": "2026-10-11T08:25:42Z", "credential": "the primary checkout's remote URL", "held": 0, "release_id": 409534533, "sent": 51, "wall_ns": 1791707142266702069}
```

`RECLAIM PASS` came first: 1 file considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held, and the store at 1,766 → 1,766. **`30ec6406…`** was removed by the Executor at 08:20:47 UTC; `rm -rf` exit 0 and `test -e` exit 1. **`d5dc7bd3…`**: the Executor's `rm -rf` was refused by the session's classifier ("[Irreversible Local Destruction]"). The Boss ran it verbatim in a root shell after B-UPLOAD, at about 08:26 UTC, and his terminal printed `exit=0`. The Executor verified it with `test -e`, exit `1`, at 08:27:24 UTC.

### 2.5 §3.4 — P-PATH (V5): **served** — `logs/14-path.log`, verbatim

```
Sun Oct 11 08:20:54 AM UTC 2026
[2026-10-11T08:20:54Z] MemAvailable 308252672 bytes, floor 93454336
[2026-10-11T08:20:54Z] P-PATH release tz-01a-dataset id 385702977; asset twap-divergence-observations.parquet state uploaded, 76818669 bytes, digest sha256:229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b, url True
[2026-10-11T08:20:57Z] P-PATH download: status 200, 76818669 bytes, sha256 229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b
[2026-10-11T08:20:57Z] READING P-PATH: served - 3 requests, the digest field present and equal, 76818669 bytes downloaded and equal
[2026-10-11T08:20:57Z] peak memory of this run: 33300480 bytes
[2026-10-11T08:20:57Z] opens refused: 0; store opens 0; requests 3, uploads 0, downloads 1 (76818669 bytes); files removed 0
exit=0
Sun Oct 11 08:20:57 AM UTC 2026
```

- **Requests:** 3 — the Release by tag, one page of its assets, and the download.
- **The record:** Release `385702977`; `state` `uploaded`, `size` `76818669`, `digest` `sha256:229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b`; `browser_download_url` equal (`url True`).
- **The download:** `200`, 76,818,669 bytes, SHA-256 equal, from 08:20:54 to 08:20:57 UTC.

### 2.6 §3.5 — G-SET (V6): **PASS**

`A` was read once, `logs/15-A.log`:

```
A read at: Sun Oct 11 08:21:02 AM UTC 2026
1791706862
```

The first run, `logs/16-inventory-1.log`, verbatim:

```
1791706866
[2026-10-11T08:21:06Z] MemAvailable 262303744 bytes, floor 93454336
[2026-10-11T08:21:06Z] free 12309204992 bytes on /var/lib; the store's stream files 678739504 bytes, the cap 8000000000
[2026-10-11T08:21:08Z] W 1791660600 2026-10-10T19:30:00Z closed   stream files 1, 13423467 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791661500 2026-10-10T19:45:00Z closed   stream files 1, 13439976 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791662400 2026-10-10T20:00:00Z closed   stream files 1, 9568261 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791663300 2026-10-10T20:15:00Z closed   stream files 1, 14589273 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791664200 2026-10-10T20:30:00Z closed   stream files 1, 13421235 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791665100 2026-10-10T20:45:00Z closed   stream files 1, 11129213 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791666000 2026-10-10T21:00:00Z closed   stream files 1, 25488448 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791666900 2026-10-10T21:15:00Z closed   stream files 1, 12837545 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791667800 2026-10-10T21:30:00Z closed   stream files 1, 17449667 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791668700 2026-10-10T21:45:00Z closed   stream files 1, 18821724 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791669600 2026-10-10T22:00:00Z closed   stream files 1, 18782634 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791670500 2026-10-10T22:15:00Z closed   stream files 1, 13835617 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791671400 2026-10-10T22:30:00Z closed   stream files 1, 22778515 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791672300 2026-10-10T22:45:00Z closed   stream files 1, 11020668 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791673200 2026-10-10T23:00:00Z closed   stream files 1, 17935756 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791674100 2026-10-10T23:15:00Z closed   stream files 1, 16755227 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791675000 2026-10-10T23:30:00Z closed   stream files 1, 17246512 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791675900 2026-10-10T23:45:00Z closed   stream files 1, 11174283 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791676800 2026-10-11T00:00:00Z closed   stream files 1, 14095311 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791677700 2026-10-11T00:15:00Z closed   stream files 1, 9762989 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791678600 2026-10-11T00:30:00Z closed   stream files 1, 14290425 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791679500 2026-10-11T00:45:00Z closed   stream files 1, 15182911 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791680400 2026-10-11T01:00:00Z closed   stream files 1, 13039899 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791681300 2026-10-11T01:15:00Z closed   stream files 1, 15944520 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791682200 2026-10-11T01:30:00Z closed   stream files 1, 12105846 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791683100 2026-10-11T01:45:00Z closed   stream files 1, 14736000 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791684000 2026-10-11T02:00:00Z closed   stream files 1, 12587712 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791684900 2026-10-11T02:15:00Z closed   stream files 1, 18090382 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791685800 2026-10-11T02:30:00Z closed   stream files 1, 5691840 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791686700 2026-10-11T02:45:00Z closed   stream files 1, 10296232 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791687600 2026-10-11T03:00:00Z closed   stream files 1, 4761970 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791688500 2026-10-11T03:15:00Z closed   stream files 1, 11715539 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791689400 2026-10-11T03:30:00Z closed   stream files 1, 11045964 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791690300 2026-10-11T03:45:00Z closed   stream files 1, 9320326 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791691200 2026-10-11T04:00:00Z closed   stream files 1, 15738124 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791692100 2026-10-11T04:15:00Z closed   stream files 1, 7204207 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791693000 2026-10-11T04:30:00Z closed   stream files 1, 11830926 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791693900 2026-10-11T04:45:00Z closed   stream files 1, 10615743 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791694800 2026-10-11T05:00:00Z closed   stream files 1, 12732416 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791695700 2026-10-11T05:15:00Z closed   stream files 1, 12435463 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791696600 2026-10-11T05:30:00Z closed   stream files 1, 21533515 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791697500 2026-10-11T05:45:00Z closed   stream files 1, 8946297 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791698400 2026-10-11T06:00:00Z closed   stream files 1, 17931091 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791699300 2026-10-11T06:15:00Z closed   stream files 1, 10168130 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791700200 2026-10-11T06:30:00Z closed   stream files 1, 5672037 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791701100 2026-10-11T06:45:00Z closed   stream files 1, 7932326 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791702000 2026-10-11T07:00:00Z closed   stream files 1, 9990431 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791702900 2026-10-11T07:15:00Z closed   stream files 1, 10963207 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791703800 2026-10-11T07:30:00Z closed   stream files 1, 9651372 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791704700 2026-10-11T07:45:00Z closed   stream files 1, 24968352 bytes, taken 1
[2026-10-11T08:21:08Z] W 1791705600 2026-10-11T08:00:00Z closed   stream files 1, 8059980 bytes, taken 1
[2026-10-11T08:21:08Z] S 1791660600-stream.jsonl.gz 13423467 02673b7227ce9c9d44451e3b9415fb8e84b37ab0b280aeeb15117d7776a14095
[2026-10-11T08:21:08Z] S 1791661500-stream.jsonl.gz 13439976 8d1153a600c626bb9914f5fc18cd68e36b0fe53f3cd95cfe58746cc7025e7b51
[2026-10-11T08:21:08Z] S 1791662400-stream.jsonl.gz 9568261 6cd316eea7ee397141e858c3b8061afbfc65f1363275b9f4810fba199e6ca60e
[2026-10-11T08:21:08Z] S 1791663300-stream.jsonl.gz 14589273 e05ff3f11a3788498a2a3a0beb72259b4297b844a071bfa7fef2d642ee3c0dde
[2026-10-11T08:21:08Z] S 1791664200-stream.jsonl.gz 13421235 30e3ffcd0035c928ddb9cf3beadc047b13e351a090829df46e92718a5b277e04
[2026-10-11T08:21:08Z] S 1791665100-stream.jsonl.gz 11129213 cd6d078247cd399ffcc827355b28114711fe8c4dbf7a35f8ac8e16194a52b3f5
[2026-10-11T08:21:08Z] S 1791666000-stream.jsonl.gz 25488448 f033da5ad81a8e5eafcc5e5867a85a86a54bb996f073178099999e63d1a7bfdd
[2026-10-11T08:21:08Z] S 1791666900-stream.jsonl.gz 12837545 b5ab1e59d30cc64a990a9b94ed7f6d24e0807d6c3819ff52f05b1d9558440d91
[2026-10-11T08:21:08Z] S 1791667800-stream.jsonl.gz 17449667 1f38535d92c7201e82d646644430752ffbb43777112e96747848011fcba795f8
[2026-10-11T08:21:08Z] S 1791668700-stream.jsonl.gz 18821724 26fa1060e3dd5cc863b9d71abef1a4b682326a0911424eb761c1b71800c1187b
[2026-10-11T08:21:08Z] S 1791669600-stream.jsonl.gz 18782634 ac057cae7f0835e3a0814f680377b7ade08b82c8daec056f0f586ab565414934
[2026-10-11T08:21:08Z] S 1791670500-stream.jsonl.gz 13835617 3fba28fc972a067f1252d95027062a34555a364d49d97b6d7e0fc9d0fe05cc1d
[2026-10-11T08:21:08Z] S 1791671400-stream.jsonl.gz 22778515 53ac058c216842bbe55730243450705cf4b0c57450c5994a9377e28979a8a037
[2026-10-11T08:21:08Z] S 1791672300-stream.jsonl.gz 11020668 be47f4c6107086fdbdfa9e50322fd077779ff71ea3ee21fba510a83b0ef20f99
[2026-10-11T08:21:08Z] S 1791673200-stream.jsonl.gz 17935756 91f62a49534c1cdaa11c960c7a1e054b50797291b972b93103b3d4304201f4d7
[2026-10-11T08:21:08Z] S 1791674100-stream.jsonl.gz 16755227 821a3b25ca7b894ef70f74ac32067c656568c977b00672946ee7147a698cf61d
[2026-10-11T08:21:08Z] S 1791675000-stream.jsonl.gz 17246512 5f4ddb59abb34d187de3be12baf33aeb79e2c9be9191a93e2bc2fe22eaef7d3b
[2026-10-11T08:21:08Z] S 1791675900-stream.jsonl.gz 11174283 3ddc73de13809d435f3abe0e3ee6eadad721a363e9dc20fa0d47f52eb19bb1c9
[2026-10-11T08:21:08Z] S 1791676800-stream.jsonl.gz 14095311 93973541db575dcf5a9497d73f61172f59299f54a5bfd764c82daf90174f651a
[2026-10-11T08:21:08Z] S 1791677700-stream.jsonl.gz 9762989 e99255d6c6f008c761028db6d9ee077bf2045ac378a773e3c5a75c4e131501d3
[2026-10-11T08:21:08Z] S 1791678600-stream.jsonl.gz 14290425 65716063fcea58dc0744bbcdf0c6499e60be2d64a9fd7ed94dac2132d64853bf
[2026-10-11T08:21:08Z] S 1791679500-stream.jsonl.gz 15182911 f44fd640415c3508b37e552448bc6a901a5eb5a529478e940eff0a2823fa670a
[2026-10-11T08:21:08Z] S 1791680400-stream.jsonl.gz 13039899 d6efb02da1c816fd51cd780b608326a90bde01ba337c78988da57d14ff241ed2
[2026-10-11T08:21:08Z] S 1791681300-stream.jsonl.gz 15944520 e3f47ea555e0449c05b181f862340f2fbfcfb67612ea9a58be2229f465667eb1
[2026-10-11T08:21:08Z] S 1791682200-stream.jsonl.gz 12105846 d773a167b99f70b8da2db2d13e534b26f3ca72f8d3d28437c618ab52c9fa405f
[2026-10-11T08:21:08Z] S 1791683100-stream.jsonl.gz 14736000 27ac9a8c957e66a7d30b447303536ebc3ee5f3cd915b2dd01cec72eb2f5c81cf
[2026-10-11T08:21:08Z] S 1791684000-stream.jsonl.gz 12587712 960a7bc878478e68425395ae4764e9e72fa2a4a7d5fdd90ccd7f12bbf9136736
[2026-10-11T08:21:08Z] S 1791684900-stream.jsonl.gz 18090382 6ef8c2d62603ff442f5ac0f0d11d2a26a28ba1cfefc4b4ea1af27e26f5a7e050
[2026-10-11T08:21:08Z] S 1791685800-stream.jsonl.gz 5691840 93b2387191bdbea4199ba39fe42c1266b2476d7ba9d75912552fdb01b53beb76
[2026-10-11T08:21:08Z] S 1791686700-stream.jsonl.gz 10296232 3904d031288bbf14ea9a3f269f4260d8e0ad0f28fa8ab91f51e95fba98cdb8aa
[2026-10-11T08:21:08Z] S 1791687600-stream.jsonl.gz 4761970 22fe211139a1475883d617bcd15861d2da59d552deb9db89c9138012f21b5365
[2026-10-11T08:21:08Z] S 1791688500-stream.jsonl.gz 11715539 15b3ab4e3cb1fccd2a7e77f71f606f8de8894f32cc3437a6b5f016537d0bc8ef
[2026-10-11T08:21:08Z] S 1791689400-stream.jsonl.gz 11045964 e45ae87c4d50ad67fc0f300ab9b9d123fc95deab16a30937c9ab4729adf698c6
[2026-10-11T08:21:08Z] S 1791690300-stream.jsonl.gz 9320326 50bc2a033d3a8dc4b0aa2291563f442291e62e532a7c9698738cc7b3165dbb97
[2026-10-11T08:21:08Z] S 1791691200-stream.jsonl.gz 15738124 53604f4792e7f198c6f95dc7061de06d65a18660e2ceedbca8f6797d3123f76f
[2026-10-11T08:21:08Z] S 1791692100-stream.jsonl.gz 7204207 24bf61060b7b44e334467817cd71afe227e62b6edad3a139ea8142715365730c
[2026-10-11T08:21:08Z] S 1791693000-stream.jsonl.gz 11830926 fda5ecba6aa24ea471e86853596d7840918ec4f79541a3d3d968b1afff5dbccf
[2026-10-11T08:21:08Z] S 1791693900-stream.jsonl.gz 10615743 a66ee84f868e6874204419f8462943cead9edc18561398936d995fa4a393d287
[2026-10-11T08:21:08Z] S 1791694800-stream.jsonl.gz 12732416 cca4f7fd1511849c336ee64318d21e1ddbc74b9acd7f436c386b424ed801b5d4
[2026-10-11T08:21:08Z] S 1791695700-stream.jsonl.gz 12435463 259f6b40c19d3ef2faf993ae6d9a28c32480355cc3fca75276546156228d70b7
[2026-10-11T08:21:08Z] S 1791696600-stream.jsonl.gz 21533515 8a600a6750338c9072aa29811a6ac16971123573b6537eb54e816df3969447b6
[2026-10-11T08:21:08Z] S 1791697500-stream.jsonl.gz 8946297 efbc615ed1bba78b2aa4872a9f5780bc0f46c3614443a45b29b802bfa931873c
[2026-10-11T08:21:08Z] S 1791698400-stream.jsonl.gz 17931091 eaa000dd2664e3013f33318df6a4f9a6e58085a2c66262374e2dcec6ab960e69
[2026-10-11T08:21:08Z] S 1791699300-stream.jsonl.gz 10168130 a6b417a805200d2a36f156a2809c7c09cf41a45890558432218d81b292855715
[2026-10-11T08:21:08Z] S 1791700200-stream.jsonl.gz 5672037 268e31d2c217dacbce44f02128e9949b5a3551e9b8e441caf9776507d7feff67
[2026-10-11T08:21:08Z] S 1791701100-stream.jsonl.gz 7932326 49e14ae788bc6c6d63947cd584a50b3983b7be6f7d6aa4065b01f9d42e87b1fb
[2026-10-11T08:21:08Z] S 1791702000-stream.jsonl.gz 9990431 2d12f225b94db6e563d3fc4ac68a329d7537bdbaac67eb16e518c5a02689612a
[2026-10-11T08:21:08Z] S 1791702900-stream.jsonl.gz 10963207 bd299f639f39b9954d9590d0c0178d3ee10aadae36902ff32b21849508294730
[2026-10-11T08:21:08Z] S 1791703800-stream.jsonl.gz 9651372 9960707372625ab632458eacc4a1d003dd553256a1822e55610a5516ad9eb785
[2026-10-11T08:21:08Z] S 1791704700-stream.jsonl.gz 24968352 7dff7b4da4db3d94b655a0433346eab280f465eae99e42de0d03d20397d1447d
[2026-10-11T08:21:08Z] S 1791705600-stream.jsonl.gz 8059980 1df39ae5f1709395ed1c4d24c654762bd972097b47d87e5e43f007d36e404401
[2026-10-11T08:21:08Z] wrote /root/tz27-work/archive/set.json sha256 ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd, 16570 bytes
[2026-10-11T08:21:08Z] READING G-SET: 51 files of 51 windows, 678739504 bytes, windows 1791660600 to 1791705600, as of 1791706862 (2026-10-11T08:21:02Z); windows considered 51 - closed 51, unclosed 0 - and 0 still open; deferred 0; the largest file 25488448 bytes, the limit 2147483647; assets 51, the limit 400
[2026-10-11T08:21:08Z] peak memory of this run: 30646272 bytes
[2026-10-11T08:21:08Z] opens refused: 0; store opens 51; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
1791706868
```

The second run, `logs/17-inventory-2.log`, verbatim:

```
1791706876
[2026-10-11T08:21:16Z] MemAvailable 252850176 bytes, floor 93454336
[2026-10-11T08:21:16Z] free 12309114880 bytes on /var/lib; the store's stream files 678739504 bytes, the cap 8000000000
[2026-10-11T08:21:18Z] W 1791660600 2026-10-10T19:30:00Z closed   stream files 1, 13423467 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791661500 2026-10-10T19:45:00Z closed   stream files 1, 13439976 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791662400 2026-10-10T20:00:00Z closed   stream files 1, 9568261 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791663300 2026-10-10T20:15:00Z closed   stream files 1, 14589273 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791664200 2026-10-10T20:30:00Z closed   stream files 1, 13421235 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791665100 2026-10-10T20:45:00Z closed   stream files 1, 11129213 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791666000 2026-10-10T21:00:00Z closed   stream files 1, 25488448 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791666900 2026-10-10T21:15:00Z closed   stream files 1, 12837545 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791667800 2026-10-10T21:30:00Z closed   stream files 1, 17449667 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791668700 2026-10-10T21:45:00Z closed   stream files 1, 18821724 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791669600 2026-10-10T22:00:00Z closed   stream files 1, 18782634 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791670500 2026-10-10T22:15:00Z closed   stream files 1, 13835617 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791671400 2026-10-10T22:30:00Z closed   stream files 1, 22778515 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791672300 2026-10-10T22:45:00Z closed   stream files 1, 11020668 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791673200 2026-10-10T23:00:00Z closed   stream files 1, 17935756 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791674100 2026-10-10T23:15:00Z closed   stream files 1, 16755227 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791675000 2026-10-10T23:30:00Z closed   stream files 1, 17246512 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791675900 2026-10-10T23:45:00Z closed   stream files 1, 11174283 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791676800 2026-10-11T00:00:00Z closed   stream files 1, 14095311 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791677700 2026-10-11T00:15:00Z closed   stream files 1, 9762989 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791678600 2026-10-11T00:30:00Z closed   stream files 1, 14290425 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791679500 2026-10-11T00:45:00Z closed   stream files 1, 15182911 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791680400 2026-10-11T01:00:00Z closed   stream files 1, 13039899 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791681300 2026-10-11T01:15:00Z closed   stream files 1, 15944520 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791682200 2026-10-11T01:30:00Z closed   stream files 1, 12105846 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791683100 2026-10-11T01:45:00Z closed   stream files 1, 14736000 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791684000 2026-10-11T02:00:00Z closed   stream files 1, 12587712 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791684900 2026-10-11T02:15:00Z closed   stream files 1, 18090382 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791685800 2026-10-11T02:30:00Z closed   stream files 1, 5691840 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791686700 2026-10-11T02:45:00Z closed   stream files 1, 10296232 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791687600 2026-10-11T03:00:00Z closed   stream files 1, 4761970 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791688500 2026-10-11T03:15:00Z closed   stream files 1, 11715539 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791689400 2026-10-11T03:30:00Z closed   stream files 1, 11045964 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791690300 2026-10-11T03:45:00Z closed   stream files 1, 9320326 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791691200 2026-10-11T04:00:00Z closed   stream files 1, 15738124 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791692100 2026-10-11T04:15:00Z closed   stream files 1, 7204207 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791693000 2026-10-11T04:30:00Z closed   stream files 1, 11830926 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791693900 2026-10-11T04:45:00Z closed   stream files 1, 10615743 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791694800 2026-10-11T05:00:00Z closed   stream files 1, 12732416 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791695700 2026-10-11T05:15:00Z closed   stream files 1, 12435463 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791696600 2026-10-11T05:30:00Z closed   stream files 1, 21533515 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791697500 2026-10-11T05:45:00Z closed   stream files 1, 8946297 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791698400 2026-10-11T06:00:00Z closed   stream files 1, 17931091 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791699300 2026-10-11T06:15:00Z closed   stream files 1, 10168130 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791700200 2026-10-11T06:30:00Z closed   stream files 1, 5672037 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791701100 2026-10-11T06:45:00Z closed   stream files 1, 7932326 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791702000 2026-10-11T07:00:00Z closed   stream files 1, 9990431 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791702900 2026-10-11T07:15:00Z closed   stream files 1, 10963207 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791703800 2026-10-11T07:30:00Z closed   stream files 1, 9651372 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791704700 2026-10-11T07:45:00Z closed   stream files 1, 24968352 bytes, taken 1
[2026-10-11T08:21:18Z] W 1791705600 2026-10-11T08:00:00Z closed   stream files 1, 8059980 bytes, taken 1
[2026-10-11T08:21:18Z] S 1791660600-stream.jsonl.gz 13423467 02673b7227ce9c9d44451e3b9415fb8e84b37ab0b280aeeb15117d7776a14095
[2026-10-11T08:21:18Z] S 1791661500-stream.jsonl.gz 13439976 8d1153a600c626bb9914f5fc18cd68e36b0fe53f3cd95cfe58746cc7025e7b51
[2026-10-11T08:21:18Z] S 1791662400-stream.jsonl.gz 9568261 6cd316eea7ee397141e858c3b8061afbfc65f1363275b9f4810fba199e6ca60e
[2026-10-11T08:21:18Z] S 1791663300-stream.jsonl.gz 14589273 e05ff3f11a3788498a2a3a0beb72259b4297b844a071bfa7fef2d642ee3c0dde
[2026-10-11T08:21:18Z] S 1791664200-stream.jsonl.gz 13421235 30e3ffcd0035c928ddb9cf3beadc047b13e351a090829df46e92718a5b277e04
[2026-10-11T08:21:18Z] S 1791665100-stream.jsonl.gz 11129213 cd6d078247cd399ffcc827355b28114711fe8c4dbf7a35f8ac8e16194a52b3f5
[2026-10-11T08:21:18Z] S 1791666000-stream.jsonl.gz 25488448 f033da5ad81a8e5eafcc5e5867a85a86a54bb996f073178099999e63d1a7bfdd
[2026-10-11T08:21:18Z] S 1791666900-stream.jsonl.gz 12837545 b5ab1e59d30cc64a990a9b94ed7f6d24e0807d6c3819ff52f05b1d9558440d91
[2026-10-11T08:21:18Z] S 1791667800-stream.jsonl.gz 17449667 1f38535d92c7201e82d646644430752ffbb43777112e96747848011fcba795f8
[2026-10-11T08:21:18Z] S 1791668700-stream.jsonl.gz 18821724 26fa1060e3dd5cc863b9d71abef1a4b682326a0911424eb761c1b71800c1187b
[2026-10-11T08:21:18Z] S 1791669600-stream.jsonl.gz 18782634 ac057cae7f0835e3a0814f680377b7ade08b82c8daec056f0f586ab565414934
[2026-10-11T08:21:18Z] S 1791670500-stream.jsonl.gz 13835617 3fba28fc972a067f1252d95027062a34555a364d49d97b6d7e0fc9d0fe05cc1d
[2026-10-11T08:21:18Z] S 1791671400-stream.jsonl.gz 22778515 53ac058c216842bbe55730243450705cf4b0c57450c5994a9377e28979a8a037
[2026-10-11T08:21:18Z] S 1791672300-stream.jsonl.gz 11020668 be47f4c6107086fdbdfa9e50322fd077779ff71ea3ee21fba510a83b0ef20f99
[2026-10-11T08:21:18Z] S 1791673200-stream.jsonl.gz 17935756 91f62a49534c1cdaa11c960c7a1e054b50797291b972b93103b3d4304201f4d7
[2026-10-11T08:21:18Z] S 1791674100-stream.jsonl.gz 16755227 821a3b25ca7b894ef70f74ac32067c656568c977b00672946ee7147a698cf61d
[2026-10-11T08:21:18Z] S 1791675000-stream.jsonl.gz 17246512 5f4ddb59abb34d187de3be12baf33aeb79e2c9be9191a93e2bc2fe22eaef7d3b
[2026-10-11T08:21:18Z] S 1791675900-stream.jsonl.gz 11174283 3ddc73de13809d435f3abe0e3ee6eadad721a363e9dc20fa0d47f52eb19bb1c9
[2026-10-11T08:21:18Z] S 1791676800-stream.jsonl.gz 14095311 93973541db575dcf5a9497d73f61172f59299f54a5bfd764c82daf90174f651a
[2026-10-11T08:21:18Z] S 1791677700-stream.jsonl.gz 9762989 e99255d6c6f008c761028db6d9ee077bf2045ac378a773e3c5a75c4e131501d3
[2026-10-11T08:21:18Z] S 1791678600-stream.jsonl.gz 14290425 65716063fcea58dc0744bbcdf0c6499e60be2d64a9fd7ed94dac2132d64853bf
[2026-10-11T08:21:18Z] S 1791679500-stream.jsonl.gz 15182911 f44fd640415c3508b37e552448bc6a901a5eb5a529478e940eff0a2823fa670a
[2026-10-11T08:21:18Z] S 1791680400-stream.jsonl.gz 13039899 d6efb02da1c816fd51cd780b608326a90bde01ba337c78988da57d14ff241ed2
[2026-10-11T08:21:18Z] S 1791681300-stream.jsonl.gz 15944520 e3f47ea555e0449c05b181f862340f2fbfcfb67612ea9a58be2229f465667eb1
[2026-10-11T08:21:18Z] S 1791682200-stream.jsonl.gz 12105846 d773a167b99f70b8da2db2d13e534b26f3ca72f8d3d28437c618ab52c9fa405f
[2026-10-11T08:21:18Z] S 1791683100-stream.jsonl.gz 14736000 27ac9a8c957e66a7d30b447303536ebc3ee5f3cd915b2dd01cec72eb2f5c81cf
[2026-10-11T08:21:18Z] S 1791684000-stream.jsonl.gz 12587712 960a7bc878478e68425395ae4764e9e72fa2a4a7d5fdd90ccd7f12bbf9136736
[2026-10-11T08:21:18Z] S 1791684900-stream.jsonl.gz 18090382 6ef8c2d62603ff442f5ac0f0d11d2a26a28ba1cfefc4b4ea1af27e26f5a7e050
[2026-10-11T08:21:18Z] S 1791685800-stream.jsonl.gz 5691840 93b2387191bdbea4199ba39fe42c1266b2476d7ba9d75912552fdb01b53beb76
[2026-10-11T08:21:18Z] S 1791686700-stream.jsonl.gz 10296232 3904d031288bbf14ea9a3f269f4260d8e0ad0f28fa8ab91f51e95fba98cdb8aa
[2026-10-11T08:21:18Z] S 1791687600-stream.jsonl.gz 4761970 22fe211139a1475883d617bcd15861d2da59d552deb9db89c9138012f21b5365
[2026-10-11T08:21:18Z] S 1791688500-stream.jsonl.gz 11715539 15b3ab4e3cb1fccd2a7e77f71f606f8de8894f32cc3437a6b5f016537d0bc8ef
[2026-10-11T08:21:18Z] S 1791689400-stream.jsonl.gz 11045964 e45ae87c4d50ad67fc0f300ab9b9d123fc95deab16a30937c9ab4729adf698c6
[2026-10-11T08:21:18Z] S 1791690300-stream.jsonl.gz 9320326 50bc2a033d3a8dc4b0aa2291563f442291e62e532a7c9698738cc7b3165dbb97
[2026-10-11T08:21:18Z] S 1791691200-stream.jsonl.gz 15738124 53604f4792e7f198c6f95dc7061de06d65a18660e2ceedbca8f6797d3123f76f
[2026-10-11T08:21:18Z] S 1791692100-stream.jsonl.gz 7204207 24bf61060b7b44e334467817cd71afe227e62b6edad3a139ea8142715365730c
[2026-10-11T08:21:18Z] S 1791693000-stream.jsonl.gz 11830926 fda5ecba6aa24ea471e86853596d7840918ec4f79541a3d3d968b1afff5dbccf
[2026-10-11T08:21:18Z] S 1791693900-stream.jsonl.gz 10615743 a66ee84f868e6874204419f8462943cead9edc18561398936d995fa4a393d287
[2026-10-11T08:21:18Z] S 1791694800-stream.jsonl.gz 12732416 cca4f7fd1511849c336ee64318d21e1ddbc74b9acd7f436c386b424ed801b5d4
[2026-10-11T08:21:18Z] S 1791695700-stream.jsonl.gz 12435463 259f6b40c19d3ef2faf993ae6d9a28c32480355cc3fca75276546156228d70b7
[2026-10-11T08:21:18Z] S 1791696600-stream.jsonl.gz 21533515 8a600a6750338c9072aa29811a6ac16971123573b6537eb54e816df3969447b6
[2026-10-11T08:21:18Z] S 1791697500-stream.jsonl.gz 8946297 efbc615ed1bba78b2aa4872a9f5780bc0f46c3614443a45b29b802bfa931873c
[2026-10-11T08:21:18Z] S 1791698400-stream.jsonl.gz 17931091 eaa000dd2664e3013f33318df6a4f9a6e58085a2c66262374e2dcec6ab960e69
[2026-10-11T08:21:18Z] S 1791699300-stream.jsonl.gz 10168130 a6b417a805200d2a36f156a2809c7c09cf41a45890558432218d81b292855715
[2026-10-11T08:21:18Z] S 1791700200-stream.jsonl.gz 5672037 268e31d2c217dacbce44f02128e9949b5a3551e9b8e441caf9776507d7feff67
[2026-10-11T08:21:18Z] S 1791701100-stream.jsonl.gz 7932326 49e14ae788bc6c6d63947cd584a50b3983b7be6f7d6aa4065b01f9d42e87b1fb
[2026-10-11T08:21:18Z] S 1791702000-stream.jsonl.gz 9990431 2d12f225b94db6e563d3fc4ac68a329d7537bdbaac67eb16e518c5a02689612a
[2026-10-11T08:21:18Z] S 1791702900-stream.jsonl.gz 10963207 bd299f639f39b9954d9590d0c0178d3ee10aadae36902ff32b21849508294730
[2026-10-11T08:21:18Z] S 1791703800-stream.jsonl.gz 9651372 9960707372625ab632458eacc4a1d003dd553256a1822e55610a5516ad9eb785
[2026-10-11T08:21:18Z] S 1791704700-stream.jsonl.gz 24968352 7dff7b4da4db3d94b655a0433346eab280f465eae99e42de0d03d20397d1447d
[2026-10-11T08:21:18Z] S 1791705600-stream.jsonl.gz 8059980 1df39ae5f1709395ed1c4d24c654762bd972097b47d87e5e43f007d36e404401
[2026-10-11T08:21:18Z] unchanged /root/tz27-work/archive/set.json sha256 ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd
[2026-10-11T08:21:18Z] READING G-SET: 51 files of 51 windows, 678739504 bytes, windows 1791660600 to 1791705600, as of 1791706862 (2026-10-11T08:21:02Z); windows considered 51 - closed 51, unclosed 0 - and 0 still open; deferred 0; the largest file 25488448 bytes, the limit 2147483647; assets 51, the limit 400
[2026-10-11T08:21:18Z] peak memory of this run: 30777344 bytes
[2026-10-11T08:21:18Z] opens refused: 0; store opens 51; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
1791706878
```

- **Exit codes:** both runs exited `0`, and the second printed `unchanged`, with `set.json` SHA-256 `ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd` (16,570 bytes).
- **The first run's seconds:** its two stamps are `1791706866` and `1791706868`, so it took **2 s**, against the 500 s fail-fast.
- **Coverage:** every considered window (51 of 51) and every taken file (51 of 51) is printed above. Their `W` and `S` lines are identical across the two runs; `diff` exited 0, `W/S lines identical`.
- **Limits and counts:** the largest file is 25,488,448 bytes, against 2,147,483,647. There are 51 assets, against 400. Deferred is `0`.

### 2.7 §3.6 — B-TAG (V7)

```
Sun Oct 11 08:21:23 AM UTC 2026
exit=0
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new tag]         tz-27-pairbook-streams -> tz-27-pairbook-streams
exit=0
Sun Oct 11 08:21:25 AM UTC 2026
[2026-10-11T08:21:25Z] tag tz-27-pairbook-streams: object e299d4e45f48b7efaa8cb18bd54b139fc0627630, commit bce5a85be7850a33f95192265b916cc9c5e0aaf1; the branch head bce5a85be7850a33f95192265b916cc9c5e0aaf1, its upstream bce5a85be7850a33f95192265b916cc9c5e0aaf1
[2026-10-11T08:21:25Z] TAGGED: tz-27-pairbook-streams -> bce5a85be7850a33f95192265b916cc9c5e0aaf1
[2026-10-11T08:21:25Z] peak memory of this run: 28712960 bytes
[2026-10-11T08:21:25Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

### 2.8 §3.7 — B-UPLOAD (V8), run by the Boss — `logs/B-UPLOAD.log`, verbatim, as `tee` wrote it

The Executor printed G-SET's count and bytes, 51 files and 678,739,504 bytes, and handed the block over verbatim. **B-UPLOAD ran once**, in the Boss's root shell, from 08:24:29 to 08:25:42 UTC. His terminal printed `exit=0` after the last line (`logs/20-boss-blocks.log`).

```
[2026-10-11T08:24:29Z] MemAvailable 313114624 bytes, floor 93454336
[2026-10-11T08:24:29Z] credential: the primary checkout's remote URL
[2026-10-11T08:24:30Z] created the Release on tz-27-pairbook-streams, id 409534533
[2026-10-11T08:24:32Z] U {"action": "uploaded", "asset": "1791660600-stream.jsonl.gz", "at": "2026-10-11T08:24:32Z", "bytes": 13423467, "digest": "sha256:02673b7227ce9c9d44451e3b9415fb8e84b37ab0b280aeeb15117d7776a14095", "id": 630207636, "sha256": "02673b7227ce9c9d44451e3b9415fb8e84b37ab0b280aeeb15117d7776a14095"}
[2026-10-11T08:24:33Z] U {"action": "uploaded", "asset": "1791661500-stream.jsonl.gz", "at": "2026-10-11T08:24:33Z", "bytes": 13439976, "digest": "sha256:8d1153a600c626bb9914f5fc18cd68e36b0fe53f3cd95cfe58746cc7025e7b51", "id": 630207676, "sha256": "8d1153a600c626bb9914f5fc18cd68e36b0fe53f3cd95cfe58746cc7025e7b51"}
[2026-10-11T08:24:34Z] U {"action": "uploaded", "asset": "1791662400-stream.jsonl.gz", "at": "2026-10-11T08:24:34Z", "bytes": 9568261, "digest": "sha256:6cd316eea7ee397141e858c3b8061afbfc65f1363275b9f4810fba199e6ca60e", "id": 630207710, "sha256": "6cd316eea7ee397141e858c3b8061afbfc65f1363275b9f4810fba199e6ca60e"}
[2026-10-11T08:24:35Z] U {"action": "uploaded", "asset": "1791663300-stream.jsonl.gz", "at": "2026-10-11T08:24:35Z", "bytes": 14589273, "digest": "sha256:e05ff3f11a3788498a2a3a0beb72259b4297b844a071bfa7fef2d642ee3c0dde", "id": 630207741, "sha256": "e05ff3f11a3788498a2a3a0beb72259b4297b844a071bfa7fef2d642ee3c0dde"}
[2026-10-11T08:24:37Z] U {"action": "uploaded", "asset": "1791664200-stream.jsonl.gz", "at": "2026-10-11T08:24:37Z", "bytes": 13421235, "digest": "sha256:30e3ffcd0035c928ddb9cf3beadc047b13e351a090829df46e92718a5b277e04", "id": 630207859, "sha256": "30e3ffcd0035c928ddb9cf3beadc047b13e351a090829df46e92718a5b277e04"}
[2026-10-11T08:24:38Z] U {"action": "uploaded", "asset": "1791665100-stream.jsonl.gz", "at": "2026-10-11T08:24:38Z", "bytes": 11129213, "digest": "sha256:cd6d078247cd399ffcc827355b28114711fe8c4dbf7a35f8ac8e16194a52b3f5", "id": 630207911, "sha256": "cd6d078247cd399ffcc827355b28114711fe8c4dbf7a35f8ac8e16194a52b3f5"}
[2026-10-11T08:24:40Z] U {"action": "uploaded", "asset": "1791666000-stream.jsonl.gz", "at": "2026-10-11T08:24:40Z", "bytes": 25488448, "digest": "sha256:f033da5ad81a8e5eafcc5e5867a85a86a54bb996f073178099999e63d1a7bfdd", "id": 630207960, "sha256": "f033da5ad81a8e5eafcc5e5867a85a86a54bb996f073178099999e63d1a7bfdd"}
[2026-10-11T08:24:42Z] U {"action": "uploaded", "asset": "1791666900-stream.jsonl.gz", "at": "2026-10-11T08:24:42Z", "bytes": 12837545, "digest": "sha256:b5ab1e59d30cc64a990a9b94ed7f6d24e0807d6c3819ff52f05b1d9558440d91", "id": 630208010, "sha256": "b5ab1e59d30cc64a990a9b94ed7f6d24e0807d6c3819ff52f05b1d9558440d91"}
[2026-10-11T08:24:43Z] U {"action": "uploaded", "asset": "1791667800-stream.jsonl.gz", "at": "2026-10-11T08:24:43Z", "bytes": 17449667, "digest": "sha256:1f38535d92c7201e82d646644430752ffbb43777112e96747848011fcba795f8", "id": 630208048, "sha256": "1f38535d92c7201e82d646644430752ffbb43777112e96747848011fcba795f8"}
[2026-10-11T08:24:45Z] U {"action": "uploaded", "asset": "1791668700-stream.jsonl.gz", "at": "2026-10-11T08:24:45Z", "bytes": 18821724, "digest": "sha256:26fa1060e3dd5cc863b9d71abef1a4b682326a0911424eb761c1b71800c1187b", "id": 630208087, "sha256": "26fa1060e3dd5cc863b9d71abef1a4b682326a0911424eb761c1b71800c1187b"}
[2026-10-11T08:24:46Z] U {"action": "uploaded", "asset": "1791669600-stream.jsonl.gz", "at": "2026-10-11T08:24:46Z", "bytes": 18782634, "digest": "sha256:ac057cae7f0835e3a0814f680377b7ade08b82c8daec056f0f586ab565414934", "id": 630208141, "sha256": "ac057cae7f0835e3a0814f680377b7ade08b82c8daec056f0f586ab565414934"}
[2026-10-11T08:24:48Z] U {"action": "uploaded", "asset": "1791670500-stream.jsonl.gz", "at": "2026-10-11T08:24:48Z", "bytes": 13835617, "digest": "sha256:3fba28fc972a067f1252d95027062a34555a364d49d97b6d7e0fc9d0fe05cc1d", "id": 630208181, "sha256": "3fba28fc972a067f1252d95027062a34555a364d49d97b6d7e0fc9d0fe05cc1d"}
[2026-10-11T08:24:49Z] U {"action": "uploaded", "asset": "1791671400-stream.jsonl.gz", "at": "2026-10-11T08:24:49Z", "bytes": 22778515, "digest": "sha256:53ac058c216842bbe55730243450705cf4b0c57450c5994a9377e28979a8a037", "id": 630208215, "sha256": "53ac058c216842bbe55730243450705cf4b0c57450c5994a9377e28979a8a037"}
[2026-10-11T08:24:51Z] U {"action": "uploaded", "asset": "1791672300-stream.jsonl.gz", "at": "2026-10-11T08:24:51Z", "bytes": 11020668, "digest": "sha256:be47f4c6107086fdbdfa9e50322fd077779ff71ea3ee21fba510a83b0ef20f99", "id": 630208259, "sha256": "be47f4c6107086fdbdfa9e50322fd077779ff71ea3ee21fba510a83b0ef20f99"}
[2026-10-11T08:24:52Z] U {"action": "uploaded", "asset": "1791673200-stream.jsonl.gz", "at": "2026-10-11T08:24:52Z", "bytes": 17935756, "digest": "sha256:91f62a49534c1cdaa11c960c7a1e054b50797291b972b93103b3d4304201f4d7", "id": 630208292, "sha256": "91f62a49534c1cdaa11c960c7a1e054b50797291b972b93103b3d4304201f4d7"}
[2026-10-11T08:24:54Z] U {"action": "uploaded", "asset": "1791674100-stream.jsonl.gz", "at": "2026-10-11T08:24:54Z", "bytes": 16755227, "digest": "sha256:821a3b25ca7b894ef70f74ac32067c656568c977b00672946ee7147a698cf61d", "id": 630208335, "sha256": "821a3b25ca7b894ef70f74ac32067c656568c977b00672946ee7147a698cf61d"}
[2026-10-11T08:24:56Z] U {"action": "uploaded", "asset": "1791675000-stream.jsonl.gz", "at": "2026-10-11T08:24:56Z", "bytes": 17246512, "digest": "sha256:5f4ddb59abb34d187de3be12baf33aeb79e2c9be9191a93e2bc2fe22eaef7d3b", "id": 630208365, "sha256": "5f4ddb59abb34d187de3be12baf33aeb79e2c9be9191a93e2bc2fe22eaef7d3b"}
[2026-10-11T08:24:57Z] U {"action": "uploaded", "asset": "1791675900-stream.jsonl.gz", "at": "2026-10-11T08:24:57Z", "bytes": 11174283, "digest": "sha256:3ddc73de13809d435f3abe0e3ee6eadad721a363e9dc20fa0d47f52eb19bb1c9", "id": 630208422, "sha256": "3ddc73de13809d435f3abe0e3ee6eadad721a363e9dc20fa0d47f52eb19bb1c9"}
[2026-10-11T08:24:58Z] U {"action": "uploaded", "asset": "1791676800-stream.jsonl.gz", "at": "2026-10-11T08:24:58Z", "bytes": 14095311, "digest": "sha256:93973541db575dcf5a9497d73f61172f59299f54a5bfd764c82daf90174f651a", "id": 630208452, "sha256": "93973541db575dcf5a9497d73f61172f59299f54a5bfd764c82daf90174f651a"}
[2026-10-11T08:25:01Z] U {"action": "uploaded", "asset": "1791677700-stream.jsonl.gz", "at": "2026-10-11T08:25:01Z", "bytes": 9762989, "digest": "sha256:e99255d6c6f008c761028db6d9ee077bf2045ac378a773e3c5a75c4e131501d3", "id": 630208489, "sha256": "e99255d6c6f008c761028db6d9ee077bf2045ac378a773e3c5a75c4e131501d3"}
[2026-10-11T08:25:02Z] U {"action": "uploaded", "asset": "1791678600-stream.jsonl.gz", "at": "2026-10-11T08:25:02Z", "bytes": 14290425, "digest": "sha256:65716063fcea58dc0744bbcdf0c6499e60be2d64a9fd7ed94dac2132d64853bf", "id": 630208544, "sha256": "65716063fcea58dc0744bbcdf0c6499e60be2d64a9fd7ed94dac2132d64853bf"}
[2026-10-11T08:25:04Z] U {"action": "uploaded", "asset": "1791679500-stream.jsonl.gz", "at": "2026-10-11T08:25:04Z", "bytes": 15182911, "digest": "sha256:f44fd640415c3508b37e552448bc6a901a5eb5a529478e940eff0a2823fa670a", "id": 630208568, "sha256": "f44fd640415c3508b37e552448bc6a901a5eb5a529478e940eff0a2823fa670a"}
[2026-10-11T08:25:05Z] U {"action": "uploaded", "asset": "1791680400-stream.jsonl.gz", "at": "2026-10-11T08:25:05Z", "bytes": 13039899, "digest": "sha256:d6efb02da1c816fd51cd780b608326a90bde01ba337c78988da57d14ff241ed2", "id": 630208604, "sha256": "d6efb02da1c816fd51cd780b608326a90bde01ba337c78988da57d14ff241ed2"}
[2026-10-11T08:25:07Z] U {"action": "uploaded", "asset": "1791681300-stream.jsonl.gz", "at": "2026-10-11T08:25:07Z", "bytes": 15944520, "digest": "sha256:e3f47ea555e0449c05b181f862340f2fbfcfb67612ea9a58be2229f465667eb1", "id": 630208643, "sha256": "e3f47ea555e0449c05b181f862340f2fbfcfb67612ea9a58be2229f465667eb1"}
[2026-10-11T08:25:08Z] U {"action": "uploaded", "asset": "1791682200-stream.jsonl.gz", "at": "2026-10-11T08:25:08Z", "bytes": 12105846, "digest": "sha256:d773a167b99f70b8da2db2d13e534b26f3ca72f8d3d28437c618ab52c9fa405f", "id": 630208675, "sha256": "d773a167b99f70b8da2db2d13e534b26f3ca72f8d3d28437c618ab52c9fa405f"}
[2026-10-11T08:25:10Z] U {"action": "uploaded", "asset": "1791683100-stream.jsonl.gz", "at": "2026-10-11T08:25:10Z", "bytes": 14736000, "digest": "sha256:27ac9a8c957e66a7d30b447303536ebc3ee5f3cd915b2dd01cec72eb2f5c81cf", "id": 630208720, "sha256": "27ac9a8c957e66a7d30b447303536ebc3ee5f3cd915b2dd01cec72eb2f5c81cf"}
[2026-10-11T08:25:11Z] U {"action": "uploaded", "asset": "1791684000-stream.jsonl.gz", "at": "2026-10-11T08:25:11Z", "bytes": 12587712, "digest": "sha256:960a7bc878478e68425395ae4764e9e72fa2a4a7d5fdd90ccd7f12bbf9136736", "id": 630208759, "sha256": "960a7bc878478e68425395ae4764e9e72fa2a4a7d5fdd90ccd7f12bbf9136736"}
[2026-10-11T08:25:12Z] U {"action": "uploaded", "asset": "1791684900-stream.jsonl.gz", "at": "2026-10-11T08:25:12Z", "bytes": 18090382, "digest": "sha256:6ef8c2d62603ff442f5ac0f0d11d2a26a28ba1cfefc4b4ea1af27e26f5a7e050", "id": 630208781, "sha256": "6ef8c2d62603ff442f5ac0f0d11d2a26a28ba1cfefc4b4ea1af27e26f5a7e050"}
[2026-10-11T08:25:14Z] U {"action": "uploaded", "asset": "1791685800-stream.jsonl.gz", "at": "2026-10-11T08:25:14Z", "bytes": 5691840, "digest": "sha256:93b2387191bdbea4199ba39fe42c1266b2476d7ba9d75912552fdb01b53beb76", "id": 630208842, "sha256": "93b2387191bdbea4199ba39fe42c1266b2476d7ba9d75912552fdb01b53beb76"}
[2026-10-11T08:25:15Z] U {"action": "uploaded", "asset": "1791686700-stream.jsonl.gz", "at": "2026-10-11T08:25:15Z", "bytes": 10296232, "digest": "sha256:3904d031288bbf14ea9a3f269f4260d8e0ad0f28fa8ab91f51e95fba98cdb8aa", "id": 630208866, "sha256": "3904d031288bbf14ea9a3f269f4260d8e0ad0f28fa8ab91f51e95fba98cdb8aa"}
[2026-10-11T08:25:16Z] U {"action": "uploaded", "asset": "1791687600-stream.jsonl.gz", "at": "2026-10-11T08:25:16Z", "bytes": 4761970, "digest": "sha256:22fe211139a1475883d617bcd15861d2da59d552deb9db89c9138012f21b5365", "id": 630208906, "sha256": "22fe211139a1475883d617bcd15861d2da59d552deb9db89c9138012f21b5365"}
[2026-10-11T08:25:17Z] U {"action": "uploaded", "asset": "1791688500-stream.jsonl.gz", "at": "2026-10-11T08:25:17Z", "bytes": 11715539, "digest": "sha256:15b3ab4e3cb1fccd2a7e77f71f606f8de8894f32cc3437a6b5f016537d0bc8ef", "id": 630208929, "sha256": "15b3ab4e3cb1fccd2a7e77f71f606f8de8894f32cc3437a6b5f016537d0bc8ef"}
[2026-10-11T08:25:19Z] U {"action": "uploaded", "asset": "1791689400-stream.jsonl.gz", "at": "2026-10-11T08:25:19Z", "bytes": 11045964, "digest": "sha256:e45ae87c4d50ad67fc0f300ab9b9d123fc95deab16a30937c9ab4729adf698c6", "id": 630208961, "sha256": "e45ae87c4d50ad67fc0f300ab9b9d123fc95deab16a30937c9ab4729adf698c6"}
[2026-10-11T08:25:20Z] U {"action": "uploaded", "asset": "1791690300-stream.jsonl.gz", "at": "2026-10-11T08:25:20Z", "bytes": 9320326, "digest": "sha256:50bc2a033d3a8dc4b0aa2291563f442291e62e532a7c9698738cc7b3165dbb97", "id": 630209005, "sha256": "50bc2a033d3a8dc4b0aa2291563f442291e62e532a7c9698738cc7b3165dbb97"}
[2026-10-11T08:25:22Z] U {"action": "uploaded", "asset": "1791691200-stream.jsonl.gz", "at": "2026-10-11T08:25:22Z", "bytes": 15738124, "digest": "sha256:53604f4792e7f198c6f95dc7061de06d65a18660e2ceedbca8f6797d3123f76f", "id": 630209056, "sha256": "53604f4792e7f198c6f95dc7061de06d65a18660e2ceedbca8f6797d3123f76f"}
[2026-10-11T08:25:23Z] U {"action": "uploaded", "asset": "1791692100-stream.jsonl.gz", "at": "2026-10-11T08:25:23Z", "bytes": 7204207, "digest": "sha256:24bf61060b7b44e334467817cd71afe227e62b6edad3a139ea8142715365730c", "id": 630209085, "sha256": "24bf61060b7b44e334467817cd71afe227e62b6edad3a139ea8142715365730c"}
[2026-10-11T08:25:24Z] U {"action": "uploaded", "asset": "1791693000-stream.jsonl.gz", "at": "2026-10-11T08:25:24Z", "bytes": 11830926, "digest": "sha256:fda5ecba6aa24ea471e86853596d7840918ec4f79541a3d3d968b1afff5dbccf", "id": 630209120, "sha256": "fda5ecba6aa24ea471e86853596d7840918ec4f79541a3d3d968b1afff5dbccf"}
[2026-10-11T08:25:25Z] U {"action": "uploaded", "asset": "1791693900-stream.jsonl.gz", "at": "2026-10-11T08:25:25Z", "bytes": 10615743, "digest": "sha256:a66ee84f868e6874204419f8462943cead9edc18561398936d995fa4a393d287", "id": 630209150, "sha256": "a66ee84f868e6874204419f8462943cead9edc18561398936d995fa4a393d287"}
[2026-10-11T08:25:26Z] U {"action": "uploaded", "asset": "1791694800-stream.jsonl.gz", "at": "2026-10-11T08:25:26Z", "bytes": 12732416, "digest": "sha256:cca4f7fd1511849c336ee64318d21e1ddbc74b9acd7f436c386b424ed801b5d4", "id": 630209181, "sha256": "cca4f7fd1511849c336ee64318d21e1ddbc74b9acd7f436c386b424ed801b5d4"}
[2026-10-11T08:25:27Z] U {"action": "uploaded", "asset": "1791695700-stream.jsonl.gz", "at": "2026-10-11T08:25:27Z", "bytes": 12435463, "digest": "sha256:259f6b40c19d3ef2faf993ae6d9a28c32480355cc3fca75276546156228d70b7", "id": 630209240, "sha256": "259f6b40c19d3ef2faf993ae6d9a28c32480355cc3fca75276546156228d70b7"}
[2026-10-11T08:25:29Z] U {"action": "uploaded", "asset": "1791696600-stream.jsonl.gz", "at": "2026-10-11T08:25:29Z", "bytes": 21533515, "digest": "sha256:8a600a6750338c9072aa29811a6ac16971123573b6537eb54e816df3969447b6", "id": 630209282, "sha256": "8a600a6750338c9072aa29811a6ac16971123573b6537eb54e816df3969447b6"}
[2026-10-11T08:25:30Z] U {"action": "uploaded", "asset": "1791697500-stream.jsonl.gz", "at": "2026-10-11T08:25:30Z", "bytes": 8946297, "digest": "sha256:efbc615ed1bba78b2aa4872a9f5780bc0f46c3614443a45b29b802bfa931873c", "id": 630209360, "sha256": "efbc615ed1bba78b2aa4872a9f5780bc0f46c3614443a45b29b802bfa931873c"}
[2026-10-11T08:25:32Z] U {"action": "uploaded", "asset": "1791698400-stream.jsonl.gz", "at": "2026-10-11T08:25:32Z", "bytes": 17931091, "digest": "sha256:eaa000dd2664e3013f33318df6a4f9a6e58085a2c66262374e2dcec6ab960e69", "id": 630209426, "sha256": "eaa000dd2664e3013f33318df6a4f9a6e58085a2c66262374e2dcec6ab960e69"}
[2026-10-11T08:25:33Z] U {"action": "uploaded", "asset": "1791699300-stream.jsonl.gz", "at": "2026-10-11T08:25:33Z", "bytes": 10168130, "digest": "sha256:a6b417a805200d2a36f156a2809c7c09cf41a45890558432218d81b292855715", "id": 630209478, "sha256": "a6b417a805200d2a36f156a2809c7c09cf41a45890558432218d81b292855715"}
[2026-10-11T08:25:34Z] U {"action": "uploaded", "asset": "1791700200-stream.jsonl.gz", "at": "2026-10-11T08:25:34Z", "bytes": 5672037, "digest": "sha256:268e31d2c217dacbce44f02128e9949b5a3551e9b8e441caf9776507d7feff67", "id": 630209519, "sha256": "268e31d2c217dacbce44f02128e9949b5a3551e9b8e441caf9776507d7feff67"}
[2026-10-11T08:25:35Z] U {"action": "uploaded", "asset": "1791701100-stream.jsonl.gz", "at": "2026-10-11T08:25:35Z", "bytes": 7932326, "digest": "sha256:49e14ae788bc6c6d63947cd584a50b3983b7be6f7d6aa4065b01f9d42e87b1fb", "id": 630209557, "sha256": "49e14ae788bc6c6d63947cd584a50b3983b7be6f7d6aa4065b01f9d42e87b1fb"}
[2026-10-11T08:25:36Z] U {"action": "uploaded", "asset": "1791702000-stream.jsonl.gz", "at": "2026-10-11T08:25:36Z", "bytes": 9990431, "digest": "sha256:2d12f225b94db6e563d3fc4ac68a329d7537bdbaac67eb16e518c5a02689612a", "id": 630209602, "sha256": "2d12f225b94db6e563d3fc4ac68a329d7537bdbaac67eb16e518c5a02689612a"}
[2026-10-11T08:25:38Z] U {"action": "uploaded", "asset": "1791702900-stream.jsonl.gz", "at": "2026-10-11T08:25:38Z", "bytes": 10963207, "digest": "sha256:bd299f639f39b9954d9590d0c0178d3ee10aadae36902ff32b21849508294730", "id": 630209655, "sha256": "bd299f639f39b9954d9590d0c0178d3ee10aadae36902ff32b21849508294730"}
[2026-10-11T08:25:39Z] U {"action": "uploaded", "asset": "1791703800-stream.jsonl.gz", "at": "2026-10-11T08:25:39Z", "bytes": 9651372, "digest": "sha256:9960707372625ab632458eacc4a1d003dd553256a1822e55610a5516ad9eb785", "id": 630209730, "sha256": "9960707372625ab632458eacc4a1d003dd553256a1822e55610a5516ad9eb785"}
[2026-10-11T08:25:41Z] U {"action": "uploaded", "asset": "1791704700-stream.jsonl.gz", "at": "2026-10-11T08:25:41Z", "bytes": 24968352, "digest": "sha256:7dff7b4da4db3d94b655a0433346eab280f465eae99e42de0d03d20397d1447d", "id": 630209811, "sha256": "7dff7b4da4db3d94b655a0433346eab280f465eae99e42de0d03d20397d1447d"}
[2026-10-11T08:25:42Z] U {"action": "uploaded", "asset": "1791705600-stream.jsonl.gz", "at": "2026-10-11T08:25:42Z", "bytes": 8059980, "digest": "sha256:1df39ae5f1709395ed1c4d24c654762bd972097b47d87e5e43f007d36e404401", "id": 630209913, "sha256": "1df39ae5f1709395ed1c4d24c654762bd972097b47d87e5e43f007d36e404401"}
[2026-10-11T08:25:42Z] U {"action": "complete", "assets": 51, "at": "2026-10-11T08:25:42Z", "credential": "the primary checkout's remote URL", "held": 0, "release_id": 409534533, "sent": 51, "wall_ns": 1791707142266702069}
[2026-10-11T08:25:42Z] UPLOAD COMPLETE: 51 of 51 assets in the Release on tz-27-pairbook-streams, 51 sent by this run, 0 kept from an earlier one; 678739504 bytes
[2026-10-11T08:25:42Z] peak memory of this run: 31326208 bytes
[2026-10-11T08:25:42Z] opens refused: 0; store opens 51; requests 54, uploads 51, downloads 0 (0 bytes); files removed 0
```

`UPLOAD COMPLETE` reads 51 of 51, sent 51, kept 0. `archive/upload.jsonl` holds 52 records: 51 `uploaded`, each with `sha256` equal to its `digest` and to the set's, and one `complete`, `wall_ns` `1791707142266702069`. SHA-256 `1e5fd981281ee7070c87b1bdb3c83b576e537eae30863d7511472a75378d370a`, 15,027 bytes.

### 2.9 §3.7 — G-UPLOAD and G-DOWNLOAD (V9): **VERIFY PASS**

At 08:27:33 UTC, before the 120 s settle, `verify` printed `NOT YET` and exited `3` (`logs/21-verify-notyet.log`):

```
Sun Oct 11 08:27:32 AM UTC 2026
[2026-10-11T08:27:33Z] NOT YET: upload completed at 2026-10-11T08:25:42Z; verify reads the Release from 2026-10-11T08:27:42Z
[2026-10-11T08:27:33Z] peak memory of this run: 28712960 bytes
[2026-10-11T08:27:33Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=3
```

From 08:27:46 UTC (`logs/22-verify.log`, verbatim):

```
Sun Oct 11 08:27:46 AM UTC 2026
[2026-10-11T08:27:46Z] MemAvailable 266764288 bytes, floor 93454336
[2026-10-11T08:27:48Z] D 1791660600-stream.jsonl.gz equal bytes 13423467 sha256 02673b7227ce9c9d44451e3b9415fb8e84b37ab0b280aeeb15117d7776a14095
[2026-10-11T08:27:49Z] D 1791661500-stream.jsonl.gz equal bytes 13439976 sha256 8d1153a600c626bb9914f5fc18cd68e36b0fe53f3cd95cfe58746cc7025e7b51
[2026-10-11T08:27:50Z] D 1791662400-stream.jsonl.gz equal bytes 9568261 sha256 6cd316eea7ee397141e858c3b8061afbfc65f1363275b9f4810fba199e6ca60e
[2026-10-11T08:27:50Z] D 1791663300-stream.jsonl.gz equal bytes 14589273 sha256 e05ff3f11a3788498a2a3a0beb72259b4297b844a071bfa7fef2d642ee3c0dde
[2026-10-11T08:27:51Z] D 1791664200-stream.jsonl.gz equal bytes 13421235 sha256 30e3ffcd0035c928ddb9cf3beadc047b13e351a090829df46e92718a5b277e04
[2026-10-11T08:27:52Z] D 1791665100-stream.jsonl.gz equal bytes 11129213 sha256 cd6d078247cd399ffcc827355b28114711fe8c4dbf7a35f8ac8e16194a52b3f5
[2026-10-11T08:27:54Z] D 1791666000-stream.jsonl.gz equal bytes 25488448 sha256 f033da5ad81a8e5eafcc5e5867a85a86a54bb996f073178099999e63d1a7bfdd
[2026-10-11T08:27:55Z] D 1791666900-stream.jsonl.gz equal bytes 12837545 sha256 b5ab1e59d30cc64a990a9b94ed7f6d24e0807d6c3819ff52f05b1d9558440d91
[2026-10-11T08:27:56Z] D 1791667800-stream.jsonl.gz equal bytes 17449667 sha256 1f38535d92c7201e82d646644430752ffbb43777112e96747848011fcba795f8
[2026-10-11T08:27:57Z] D 1791668700-stream.jsonl.gz equal bytes 18821724 sha256 26fa1060e3dd5cc863b9d71abef1a4b682326a0911424eb761c1b71800c1187b
[2026-10-11T08:27:58Z] D 1791669600-stream.jsonl.gz equal bytes 18782634 sha256 ac057cae7f0835e3a0814f680377b7ade08b82c8daec056f0f586ab565414934
[2026-10-11T08:27:59Z] D 1791670500-stream.jsonl.gz equal bytes 13835617 sha256 3fba28fc972a067f1252d95027062a34555a364d49d97b6d7e0fc9d0fe05cc1d
[2026-10-11T08:28:01Z] D 1791671400-stream.jsonl.gz equal bytes 22778515 sha256 53ac058c216842bbe55730243450705cf4b0c57450c5994a9377e28979a8a037
[2026-10-11T08:28:01Z] D 1791672300-stream.jsonl.gz equal bytes 11020668 sha256 be47f4c6107086fdbdfa9e50322fd077779ff71ea3ee21fba510a83b0ef20f99
[2026-10-11T08:28:02Z] D 1791673200-stream.jsonl.gz equal bytes 17935756 sha256 91f62a49534c1cdaa11c960c7a1e054b50797291b972b93103b3d4304201f4d7
[2026-10-11T08:28:03Z] D 1791674100-stream.jsonl.gz equal bytes 16755227 sha256 821a3b25ca7b894ef70f74ac32067c656568c977b00672946ee7147a698cf61d
[2026-10-11T08:28:04Z] D 1791675000-stream.jsonl.gz equal bytes 17246512 sha256 5f4ddb59abb34d187de3be12baf33aeb79e2c9be9191a93e2bc2fe22eaef7d3b
[2026-10-11T08:28:05Z] D 1791675900-stream.jsonl.gz equal bytes 11174283 sha256 3ddc73de13809d435f3abe0e3ee6eadad721a363e9dc20fa0d47f52eb19bb1c9
[2026-10-11T08:28:06Z] D 1791676800-stream.jsonl.gz equal bytes 14095311 sha256 93973541db575dcf5a9497d73f61172f59299f54a5bfd764c82daf90174f651a
[2026-10-11T08:28:07Z] D 1791677700-stream.jsonl.gz equal bytes 9762989 sha256 e99255d6c6f008c761028db6d9ee077bf2045ac378a773e3c5a75c4e131501d3
[2026-10-11T08:28:07Z] D 1791678600-stream.jsonl.gz equal bytes 14290425 sha256 65716063fcea58dc0744bbcdf0c6499e60be2d64a9fd7ed94dac2132d64853bf
[2026-10-11T08:28:09Z] D 1791679500-stream.jsonl.gz equal bytes 15182911 sha256 f44fd640415c3508b37e552448bc6a901a5eb5a529478e940eff0a2823fa670a
[2026-10-11T08:28:09Z] D 1791680400-stream.jsonl.gz equal bytes 13039899 sha256 d6efb02da1c816fd51cd780b608326a90bde01ba337c78988da57d14ff241ed2
[2026-10-11T08:28:10Z] D 1791681300-stream.jsonl.gz equal bytes 15944520 sha256 e3f47ea555e0449c05b181f862340f2fbfcfb67612ea9a58be2229f465667eb1
[2026-10-11T08:28:11Z] D 1791682200-stream.jsonl.gz equal bytes 12105846 sha256 d773a167b99f70b8da2db2d13e534b26f3ca72f8d3d28437c618ab52c9fa405f
[2026-10-11T08:28:12Z] D 1791683100-stream.jsonl.gz equal bytes 14736000 sha256 27ac9a8c957e66a7d30b447303536ebc3ee5f3cd915b2dd01cec72eb2f5c81cf
[2026-10-11T08:28:13Z] D 1791684000-stream.jsonl.gz equal bytes 12587712 sha256 960a7bc878478e68425395ae4764e9e72fa2a4a7d5fdd90ccd7f12bbf9136736
[2026-10-11T08:28:14Z] D 1791684900-stream.jsonl.gz equal bytes 18090382 sha256 6ef8c2d62603ff442f5ac0f0d11d2a26a28ba1cfefc4b4ea1af27e26f5a7e050
[2026-10-11T08:28:15Z] D 1791685800-stream.jsonl.gz equal bytes 5691840 sha256 93b2387191bdbea4199ba39fe42c1266b2476d7ba9d75912552fdb01b53beb76
[2026-10-11T08:28:16Z] D 1791686700-stream.jsonl.gz equal bytes 10296232 sha256 3904d031288bbf14ea9a3f269f4260d8e0ad0f28fa8ab91f51e95fba98cdb8aa
[2026-10-11T08:28:16Z] D 1791687600-stream.jsonl.gz equal bytes 4761970 sha256 22fe211139a1475883d617bcd15861d2da59d552deb9db89c9138012f21b5365
[2026-10-11T08:28:17Z] D 1791688500-stream.jsonl.gz equal bytes 11715539 sha256 15b3ab4e3cb1fccd2a7e77f71f606f8de8894f32cc3437a6b5f016537d0bc8ef
[2026-10-11T08:28:18Z] D 1791689400-stream.jsonl.gz equal bytes 11045964 sha256 e45ae87c4d50ad67fc0f300ab9b9d123fc95deab16a30937c9ab4729adf698c6
[2026-10-11T08:28:19Z] D 1791690300-stream.jsonl.gz equal bytes 9320326 sha256 50bc2a033d3a8dc4b0aa2291563f442291e62e532a7c9698738cc7b3165dbb97
[2026-10-11T08:28:20Z] D 1791691200-stream.jsonl.gz equal bytes 15738124 sha256 53604f4792e7f198c6f95dc7061de06d65a18660e2ceedbca8f6797d3123f76f
[2026-10-11T08:28:21Z] D 1791692100-stream.jsonl.gz equal bytes 7204207 sha256 24bf61060b7b44e334467817cd71afe227e62b6edad3a139ea8142715365730c
[2026-10-11T08:28:22Z] D 1791693000-stream.jsonl.gz equal bytes 11830926 sha256 fda5ecba6aa24ea471e86853596d7840918ec4f79541a3d3d968b1afff5dbccf
[2026-10-11T08:28:23Z] D 1791693900-stream.jsonl.gz equal bytes 10615743 sha256 a66ee84f868e6874204419f8462943cead9edc18561398936d995fa4a393d287
[2026-10-11T08:28:23Z] D 1791694800-stream.jsonl.gz equal bytes 12732416 sha256 cca4f7fd1511849c336ee64318d21e1ddbc74b9acd7f436c386b424ed801b5d4
[2026-10-11T08:28:25Z] D 1791695700-stream.jsonl.gz equal bytes 12435463 sha256 259f6b40c19d3ef2faf993ae6d9a28c32480355cc3fca75276546156228d70b7
[2026-10-11T08:28:26Z] D 1791696600-stream.jsonl.gz equal bytes 21533515 sha256 8a600a6750338c9072aa29811a6ac16971123573b6537eb54e816df3969447b6
[2026-10-11T08:28:27Z] D 1791697500-stream.jsonl.gz equal bytes 8946297 sha256 efbc615ed1bba78b2aa4872a9f5780bc0f46c3614443a45b29b802bfa931873c
[2026-10-11T08:28:28Z] D 1791698400-stream.jsonl.gz equal bytes 17931091 sha256 eaa000dd2664e3013f33318df6a4f9a6e58085a2c66262374e2dcec6ab960e69
[2026-10-11T08:28:28Z] D 1791699300-stream.jsonl.gz equal bytes 10168130 sha256 a6b417a805200d2a36f156a2809c7c09cf41a45890558432218d81b292855715
[2026-10-11T08:28:29Z] D 1791700200-stream.jsonl.gz equal bytes 5672037 sha256 268e31d2c217dacbce44f02128e9949b5a3551e9b8e441caf9776507d7feff67
[2026-10-11T08:28:29Z] D 1791701100-stream.jsonl.gz equal bytes 7932326 sha256 49e14ae788bc6c6d63947cd584a50b3983b7be6f7d6aa4065b01f9d42e87b1fb
[2026-10-11T08:28:30Z] D 1791702000-stream.jsonl.gz equal bytes 9990431 sha256 2d12f225b94db6e563d3fc4ac68a329d7537bdbaac67eb16e518c5a02689612a
[2026-10-11T08:28:31Z] D 1791702900-stream.jsonl.gz equal bytes 10963207 sha256 bd299f639f39b9954d9590d0c0178d3ee10aadae36902ff32b21849508294730
[2026-10-11T08:28:32Z] D 1791703800-stream.jsonl.gz equal bytes 9651372 sha256 9960707372625ab632458eacc4a1d003dd553256a1822e55610a5516ad9eb785
[2026-10-11T08:28:34Z] D 1791704700-stream.jsonl.gz equal bytes 24968352 sha256 7dff7b4da4db3d94b655a0433346eab280f465eae99e42de0d03d20397d1447d
[2026-10-11T08:28:34Z] D 1791705600-stream.jsonl.gz equal bytes 8059980 sha256 1df39ae5f1709395ed1c4d24c654762bd972097b47d87e5e43f007d36e404401
[2026-10-11T08:28:34Z] V 1791660600-stream.jsonl.gz id 630207636 state uploaded api True bytes 13423467 digest sha256:02673b7227ce9c9d44451e3b9415fb8e84b37ab0b280aeeb15117d7776a14095 url True
[2026-10-11T08:28:34Z] V 1791661500-stream.jsonl.gz id 630207676 state uploaded api True bytes 13439976 digest sha256:8d1153a600c626bb9914f5fc18cd68e36b0fe53f3cd95cfe58746cc7025e7b51 url True
[2026-10-11T08:28:34Z] V 1791662400-stream.jsonl.gz id 630207710 state uploaded api True bytes 9568261 digest sha256:6cd316eea7ee397141e858c3b8061afbfc65f1363275b9f4810fba199e6ca60e url True
[2026-10-11T08:28:34Z] V 1791663300-stream.jsonl.gz id 630207741 state uploaded api True bytes 14589273 digest sha256:e05ff3f11a3788498a2a3a0beb72259b4297b844a071bfa7fef2d642ee3c0dde url True
[2026-10-11T08:28:34Z] V 1791664200-stream.jsonl.gz id 630207859 state uploaded api True bytes 13421235 digest sha256:30e3ffcd0035c928ddb9cf3beadc047b13e351a090829df46e92718a5b277e04 url True
[2026-10-11T08:28:34Z] V 1791665100-stream.jsonl.gz id 630207911 state uploaded api True bytes 11129213 digest sha256:cd6d078247cd399ffcc827355b28114711fe8c4dbf7a35f8ac8e16194a52b3f5 url True
[2026-10-11T08:28:34Z] V 1791666000-stream.jsonl.gz id 630207960 state uploaded api True bytes 25488448 digest sha256:f033da5ad81a8e5eafcc5e5867a85a86a54bb996f073178099999e63d1a7bfdd url True
[2026-10-11T08:28:34Z] V 1791666900-stream.jsonl.gz id 630208010 state uploaded api True bytes 12837545 digest sha256:b5ab1e59d30cc64a990a9b94ed7f6d24e0807d6c3819ff52f05b1d9558440d91 url True
[2026-10-11T08:28:34Z] V 1791667800-stream.jsonl.gz id 630208048 state uploaded api True bytes 17449667 digest sha256:1f38535d92c7201e82d646644430752ffbb43777112e96747848011fcba795f8 url True
[2026-10-11T08:28:34Z] V 1791668700-stream.jsonl.gz id 630208087 state uploaded api True bytes 18821724 digest sha256:26fa1060e3dd5cc863b9d71abef1a4b682326a0911424eb761c1b71800c1187b url True
[2026-10-11T08:28:34Z] V 1791669600-stream.jsonl.gz id 630208141 state uploaded api True bytes 18782634 digest sha256:ac057cae7f0835e3a0814f680377b7ade08b82c8daec056f0f586ab565414934 url True
[2026-10-11T08:28:34Z] V 1791670500-stream.jsonl.gz id 630208181 state uploaded api True bytes 13835617 digest sha256:3fba28fc972a067f1252d95027062a34555a364d49d97b6d7e0fc9d0fe05cc1d url True
[2026-10-11T08:28:34Z] V 1791671400-stream.jsonl.gz id 630208215 state uploaded api True bytes 22778515 digest sha256:53ac058c216842bbe55730243450705cf4b0c57450c5994a9377e28979a8a037 url True
[2026-10-11T08:28:34Z] V 1791672300-stream.jsonl.gz id 630208259 state uploaded api True bytes 11020668 digest sha256:be47f4c6107086fdbdfa9e50322fd077779ff71ea3ee21fba510a83b0ef20f99 url True
[2026-10-11T08:28:34Z] V 1791673200-stream.jsonl.gz id 630208292 state uploaded api True bytes 17935756 digest sha256:91f62a49534c1cdaa11c960c7a1e054b50797291b972b93103b3d4304201f4d7 url True
[2026-10-11T08:28:34Z] V 1791674100-stream.jsonl.gz id 630208335 state uploaded api True bytes 16755227 digest sha256:821a3b25ca7b894ef70f74ac32067c656568c977b00672946ee7147a698cf61d url True
[2026-10-11T08:28:34Z] V 1791675000-stream.jsonl.gz id 630208365 state uploaded api True bytes 17246512 digest sha256:5f4ddb59abb34d187de3be12baf33aeb79e2c9be9191a93e2bc2fe22eaef7d3b url True
[2026-10-11T08:28:34Z] V 1791675900-stream.jsonl.gz id 630208422 state uploaded api True bytes 11174283 digest sha256:3ddc73de13809d435f3abe0e3ee6eadad721a363e9dc20fa0d47f52eb19bb1c9 url True
[2026-10-11T08:28:34Z] V 1791676800-stream.jsonl.gz id 630208452 state uploaded api True bytes 14095311 digest sha256:93973541db575dcf5a9497d73f61172f59299f54a5bfd764c82daf90174f651a url True
[2026-10-11T08:28:34Z] V 1791677700-stream.jsonl.gz id 630208489 state uploaded api True bytes 9762989 digest sha256:e99255d6c6f008c761028db6d9ee077bf2045ac378a773e3c5a75c4e131501d3 url True
[2026-10-11T08:28:34Z] V 1791678600-stream.jsonl.gz id 630208544 state uploaded api True bytes 14290425 digest sha256:65716063fcea58dc0744bbcdf0c6499e60be2d64a9fd7ed94dac2132d64853bf url True
[2026-10-11T08:28:34Z] V 1791679500-stream.jsonl.gz id 630208568 state uploaded api True bytes 15182911 digest sha256:f44fd640415c3508b37e552448bc6a901a5eb5a529478e940eff0a2823fa670a url True
[2026-10-11T08:28:34Z] V 1791680400-stream.jsonl.gz id 630208604 state uploaded api True bytes 13039899 digest sha256:d6efb02da1c816fd51cd780b608326a90bde01ba337c78988da57d14ff241ed2 url True
[2026-10-11T08:28:34Z] V 1791681300-stream.jsonl.gz id 630208643 state uploaded api True bytes 15944520 digest sha256:e3f47ea555e0449c05b181f862340f2fbfcfb67612ea9a58be2229f465667eb1 url True
[2026-10-11T08:28:34Z] V 1791682200-stream.jsonl.gz id 630208675 state uploaded api True bytes 12105846 digest sha256:d773a167b99f70b8da2db2d13e534b26f3ca72f8d3d28437c618ab52c9fa405f url True
[2026-10-11T08:28:34Z] V 1791683100-stream.jsonl.gz id 630208720 state uploaded api True bytes 14736000 digest sha256:27ac9a8c957e66a7d30b447303536ebc3ee5f3cd915b2dd01cec72eb2f5c81cf url True
[2026-10-11T08:28:34Z] V 1791684000-stream.jsonl.gz id 630208759 state uploaded api True bytes 12587712 digest sha256:960a7bc878478e68425395ae4764e9e72fa2a4a7d5fdd90ccd7f12bbf9136736 url True
[2026-10-11T08:28:34Z] V 1791684900-stream.jsonl.gz id 630208781 state uploaded api True bytes 18090382 digest sha256:6ef8c2d62603ff442f5ac0f0d11d2a26a28ba1cfefc4b4ea1af27e26f5a7e050 url True
[2026-10-11T08:28:34Z] V 1791685800-stream.jsonl.gz id 630208842 state uploaded api True bytes 5691840 digest sha256:93b2387191bdbea4199ba39fe42c1266b2476d7ba9d75912552fdb01b53beb76 url True
[2026-10-11T08:28:34Z] V 1791686700-stream.jsonl.gz id 630208866 state uploaded api True bytes 10296232 digest sha256:3904d031288bbf14ea9a3f269f4260d8e0ad0f28fa8ab91f51e95fba98cdb8aa url True
[2026-10-11T08:28:34Z] V 1791687600-stream.jsonl.gz id 630208906 state uploaded api True bytes 4761970 digest sha256:22fe211139a1475883d617bcd15861d2da59d552deb9db89c9138012f21b5365 url True
[2026-10-11T08:28:34Z] V 1791688500-stream.jsonl.gz id 630208929 state uploaded api True bytes 11715539 digest sha256:15b3ab4e3cb1fccd2a7e77f71f606f8de8894f32cc3437a6b5f016537d0bc8ef url True
[2026-10-11T08:28:34Z] V 1791689400-stream.jsonl.gz id 630208961 state uploaded api True bytes 11045964 digest sha256:e45ae87c4d50ad67fc0f300ab9b9d123fc95deab16a30937c9ab4729adf698c6 url True
[2026-10-11T08:28:34Z] V 1791690300-stream.jsonl.gz id 630209005 state uploaded api True bytes 9320326 digest sha256:50bc2a033d3a8dc4b0aa2291563f442291e62e532a7c9698738cc7b3165dbb97 url True
[2026-10-11T08:28:34Z] V 1791691200-stream.jsonl.gz id 630209056 state uploaded api True bytes 15738124 digest sha256:53604f4792e7f198c6f95dc7061de06d65a18660e2ceedbca8f6797d3123f76f url True
[2026-10-11T08:28:34Z] V 1791692100-stream.jsonl.gz id 630209085 state uploaded api True bytes 7204207 digest sha256:24bf61060b7b44e334467817cd71afe227e62b6edad3a139ea8142715365730c url True
[2026-10-11T08:28:34Z] V 1791693000-stream.jsonl.gz id 630209120 state uploaded api True bytes 11830926 digest sha256:fda5ecba6aa24ea471e86853596d7840918ec4f79541a3d3d968b1afff5dbccf url True
[2026-10-11T08:28:34Z] V 1791693900-stream.jsonl.gz id 630209150 state uploaded api True bytes 10615743 digest sha256:a66ee84f868e6874204419f8462943cead9edc18561398936d995fa4a393d287 url True
[2026-10-11T08:28:34Z] V 1791694800-stream.jsonl.gz id 630209181 state uploaded api True bytes 12732416 digest sha256:cca4f7fd1511849c336ee64318d21e1ddbc74b9acd7f436c386b424ed801b5d4 url True
[2026-10-11T08:28:34Z] V 1791695700-stream.jsonl.gz id 630209240 state uploaded api True bytes 12435463 digest sha256:259f6b40c19d3ef2faf993ae6d9a28c32480355cc3fca75276546156228d70b7 url True
[2026-10-11T08:28:34Z] V 1791696600-stream.jsonl.gz id 630209282 state uploaded api True bytes 21533515 digest sha256:8a600a6750338c9072aa29811a6ac16971123573b6537eb54e816df3969447b6 url True
[2026-10-11T08:28:34Z] V 1791697500-stream.jsonl.gz id 630209360 state uploaded api True bytes 8946297 digest sha256:efbc615ed1bba78b2aa4872a9f5780bc0f46c3614443a45b29b802bfa931873c url True
[2026-10-11T08:28:34Z] V 1791698400-stream.jsonl.gz id 630209426 state uploaded api True bytes 17931091 digest sha256:eaa000dd2664e3013f33318df6a4f9a6e58085a2c66262374e2dcec6ab960e69 url True
[2026-10-11T08:28:34Z] V 1791699300-stream.jsonl.gz id 630209478 state uploaded api True bytes 10168130 digest sha256:a6b417a805200d2a36f156a2809c7c09cf41a45890558432218d81b292855715 url True
[2026-10-11T08:28:34Z] V 1791700200-stream.jsonl.gz id 630209519 state uploaded api True bytes 5672037 digest sha256:268e31d2c217dacbce44f02128e9949b5a3551e9b8e441caf9776507d7feff67 url True
[2026-10-11T08:28:34Z] V 1791701100-stream.jsonl.gz id 630209557 state uploaded api True bytes 7932326 digest sha256:49e14ae788bc6c6d63947cd584a50b3983b7be6f7d6aa4065b01f9d42e87b1fb url True
[2026-10-11T08:28:34Z] V 1791702000-stream.jsonl.gz id 630209602 state uploaded api True bytes 9990431 digest sha256:2d12f225b94db6e563d3fc4ac68a329d7537bdbaac67eb16e518c5a02689612a url True
[2026-10-11T08:28:34Z] V 1791702900-stream.jsonl.gz id 630209655 state uploaded api True bytes 10963207 digest sha256:bd299f639f39b9954d9590d0c0178d3ee10aadae36902ff32b21849508294730 url True
[2026-10-11T08:28:34Z] V 1791703800-stream.jsonl.gz id 630209730 state uploaded api True bytes 9651372 digest sha256:9960707372625ab632458eacc4a1d003dd553256a1822e55610a5516ad9eb785 url True
[2026-10-11T08:28:34Z] V 1791704700-stream.jsonl.gz id 630209811 state uploaded api True bytes 24968352 digest sha256:7dff7b4da4db3d94b655a0433346eab280f465eae99e42de0d03d20397d1447d url True
[2026-10-11T08:28:34Z] V 1791705600-stream.jsonl.gz id 630209913 state uploaded api True bytes 8059980 digest sha256:1df39ae5f1709395ed1c4d24c654762bd972097b47d87e5e43f007d36e404401 url True
[2026-10-11T08:28:34Z] G-UPLOAD/G-DOWNLOAD release published on the tag                         True
[2026-10-11T08:28:34Z] G-UPLOAD/G-DOWNLOAD no asset missing                                     True
[2026-10-11T08:28:34Z] G-UPLOAD/G-DOWNLOAD no asset beyond the set                              True
[2026-10-11T08:28:34Z] G-UPLOAD/G-DOWNLOAD every asset uploaded, its bytes and digest the set's True
[2026-10-11T08:28:34Z] G-UPLOAD/G-DOWNLOAD every download the set's bytes and SHA-256           True
[2026-10-11T08:28:34Z] wrote /root/tz27-work/archive/verify.json sha256 6eeb9bb3f414c032f62a0a766cfb28fb465661921b555ba6be308e299e8c411d
[2026-10-11T08:28:34Z] VERIFY PASS: 51 of 51 assets by name, bytes, state and digest; 51 of 51 downloads equal, 678739504 bytes
[2026-10-11T08:28:34Z] peak memory of this run: 33857536 bytes
[2026-10-11T08:28:34Z] opens refused: 0; store opens 0; requests 53, uploads 0, downloads 51 (678739504 bytes); files removed 0
exit=0
Sun Oct 11 08:28:34 AM UTC 2026
```

`VERIFY PASS` holds all five checks:

| check | |
|---|---|
| release published on the tag | True |
| no asset missing | True |
| no asset beyond the set | True |
| every asset uploaded, its bytes and digest the set's | True, 51 of 51 |
| every download the set's bytes and SHA-256 | True, 51 of 51, 678,739,504 bytes |

The Release's id is `409534533`. `verify.json` SHA-256 is `6eeb9bb3f414c032f62a0a766cfb28fb465661921b555ba6be308e299e8c411d`, 25,364 bytes. The downloads ran from 08:27:48 to 08:28:34 UTC through `github.com`'s redirect.

### 2.10 §3.8 — G-DELETE (V10): **PASS**

The Executor's `I delete` was refused by the session's classifier ("[Irreversible Local Destruction]"). That refusal discarded the `df`/`du` line in the same command. A later standalone `df`/`du` was refused as "[Auto-Mode Bypass]", so no Executor read exists before the removal. The Boss ran §3.8's block at 08:35:53 UTC, with the `df`/`du` line before it, and his terminal printed `exit=0` (`logs/25-boss-delete.log`).

`logs/B-DELETE-df-before.log`, verbatim:

```
Sun Oct 11 08:35:53 AM UTC 2026
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12298158080
690132167	/var/lib/btc-pairbook
```

`logs/B-DELETE.log`, verbatim:

```
[2026-10-11T08:35:53Z] MemAvailable 276144128 bytes, floor 93454336
[2026-10-11T08:35:53Z] X 1791660600-stream.jsonl.gz 13423467 02673b7227ce9c9d44451e3b9415fb8e84b37ab0b280aeeb15117d7776a14095 removed
[2026-10-11T08:35:53Z] X 1791661500-stream.jsonl.gz 13439976 8d1153a600c626bb9914f5fc18cd68e36b0fe53f3cd95cfe58746cc7025e7b51 removed
[2026-10-11T08:35:53Z] X 1791662400-stream.jsonl.gz 9568261 6cd316eea7ee397141e858c3b8061afbfc65f1363275b9f4810fba199e6ca60e removed
[2026-10-11T08:35:53Z] X 1791663300-stream.jsonl.gz 14589273 e05ff3f11a3788498a2a3a0beb72259b4297b844a071bfa7fef2d642ee3c0dde removed
[2026-10-11T08:35:53Z] X 1791664200-stream.jsonl.gz 13421235 30e3ffcd0035c928ddb9cf3beadc047b13e351a090829df46e92718a5b277e04 removed
[2026-10-11T08:35:53Z] X 1791665100-stream.jsonl.gz 11129213 cd6d078247cd399ffcc827355b28114711fe8c4dbf7a35f8ac8e16194a52b3f5 removed
[2026-10-11T08:35:53Z] X 1791666000-stream.jsonl.gz 25488448 f033da5ad81a8e5eafcc5e5867a85a86a54bb996f073178099999e63d1a7bfdd removed
[2026-10-11T08:35:53Z] X 1791666900-stream.jsonl.gz 12837545 b5ab1e59d30cc64a990a9b94ed7f6d24e0807d6c3819ff52f05b1d9558440d91 removed
[2026-10-11T08:35:53Z] X 1791667800-stream.jsonl.gz 17449667 1f38535d92c7201e82d646644430752ffbb43777112e96747848011fcba795f8 removed
[2026-10-11T08:35:53Z] X 1791668700-stream.jsonl.gz 18821724 26fa1060e3dd5cc863b9d71abef1a4b682326a0911424eb761c1b71800c1187b removed
[2026-10-11T08:35:53Z] X 1791669600-stream.jsonl.gz 18782634 ac057cae7f0835e3a0814f680377b7ade08b82c8daec056f0f586ab565414934 removed
[2026-10-11T08:35:53Z] X 1791670500-stream.jsonl.gz 13835617 3fba28fc972a067f1252d95027062a34555a364d49d97b6d7e0fc9d0fe05cc1d removed
[2026-10-11T08:35:53Z] X 1791671400-stream.jsonl.gz 22778515 53ac058c216842bbe55730243450705cf4b0c57450c5994a9377e28979a8a037 removed
[2026-10-11T08:35:53Z] X 1791672300-stream.jsonl.gz 11020668 be47f4c6107086fdbdfa9e50322fd077779ff71ea3ee21fba510a83b0ef20f99 removed
[2026-10-11T08:35:53Z] X 1791673200-stream.jsonl.gz 17935756 91f62a49534c1cdaa11c960c7a1e054b50797291b972b93103b3d4304201f4d7 removed
[2026-10-11T08:35:53Z] X 1791674100-stream.jsonl.gz 16755227 821a3b25ca7b894ef70f74ac32067c656568c977b00672946ee7147a698cf61d removed
[2026-10-11T08:35:53Z] X 1791675000-stream.jsonl.gz 17246512 5f4ddb59abb34d187de3be12baf33aeb79e2c9be9191a93e2bc2fe22eaef7d3b removed
[2026-10-11T08:35:53Z] X 1791675900-stream.jsonl.gz 11174283 3ddc73de13809d435f3abe0e3ee6eadad721a363e9dc20fa0d47f52eb19bb1c9 removed
[2026-10-11T08:35:53Z] X 1791676800-stream.jsonl.gz 14095311 93973541db575dcf5a9497d73f61172f59299f54a5bfd764c82daf90174f651a removed
[2026-10-11T08:35:54Z] X 1791677700-stream.jsonl.gz 9762989 e99255d6c6f008c761028db6d9ee077bf2045ac378a773e3c5a75c4e131501d3 removed
[2026-10-11T08:35:54Z] X 1791678600-stream.jsonl.gz 14290425 65716063fcea58dc0744bbcdf0c6499e60be2d64a9fd7ed94dac2132d64853bf removed
[2026-10-11T08:35:54Z] X 1791679500-stream.jsonl.gz 15182911 f44fd640415c3508b37e552448bc6a901a5eb5a529478e940eff0a2823fa670a removed
[2026-10-11T08:35:54Z] X 1791680400-stream.jsonl.gz 13039899 d6efb02da1c816fd51cd780b608326a90bde01ba337c78988da57d14ff241ed2 removed
[2026-10-11T08:35:54Z] X 1791681300-stream.jsonl.gz 15944520 e3f47ea555e0449c05b181f862340f2fbfcfb67612ea9a58be2229f465667eb1 removed
[2026-10-11T08:35:54Z] X 1791682200-stream.jsonl.gz 12105846 d773a167b99f70b8da2db2d13e534b26f3ca72f8d3d28437c618ab52c9fa405f removed
[2026-10-11T08:35:54Z] X 1791683100-stream.jsonl.gz 14736000 27ac9a8c957e66a7d30b447303536ebc3ee5f3cd915b2dd01cec72eb2f5c81cf removed
[2026-10-11T08:35:54Z] X 1791684000-stream.jsonl.gz 12587712 960a7bc878478e68425395ae4764e9e72fa2a4a7d5fdd90ccd7f12bbf9136736 removed
[2026-10-11T08:35:54Z] X 1791684900-stream.jsonl.gz 18090382 6ef8c2d62603ff442f5ac0f0d11d2a26a28ba1cfefc4b4ea1af27e26f5a7e050 removed
[2026-10-11T08:35:54Z] X 1791685800-stream.jsonl.gz 5691840 93b2387191bdbea4199ba39fe42c1266b2476d7ba9d75912552fdb01b53beb76 removed
[2026-10-11T08:35:54Z] X 1791686700-stream.jsonl.gz 10296232 3904d031288bbf14ea9a3f269f4260d8e0ad0f28fa8ab91f51e95fba98cdb8aa removed
[2026-10-11T08:35:54Z] X 1791687600-stream.jsonl.gz 4761970 22fe211139a1475883d617bcd15861d2da59d552deb9db89c9138012f21b5365 removed
[2026-10-11T08:35:54Z] X 1791688500-stream.jsonl.gz 11715539 15b3ab4e3cb1fccd2a7e77f71f606f8de8894f32cc3437a6b5f016537d0bc8ef removed
[2026-10-11T08:35:54Z] X 1791689400-stream.jsonl.gz 11045964 e45ae87c4d50ad67fc0f300ab9b9d123fc95deab16a30937c9ab4729adf698c6 removed
[2026-10-11T08:35:54Z] X 1791690300-stream.jsonl.gz 9320326 50bc2a033d3a8dc4b0aa2291563f442291e62e532a7c9698738cc7b3165dbb97 removed
[2026-10-11T08:35:54Z] X 1791691200-stream.jsonl.gz 15738124 53604f4792e7f198c6f95dc7061de06d65a18660e2ceedbca8f6797d3123f76f removed
[2026-10-11T08:35:54Z] X 1791692100-stream.jsonl.gz 7204207 24bf61060b7b44e334467817cd71afe227e62b6edad3a139ea8142715365730c removed
[2026-10-11T08:35:54Z] X 1791693000-stream.jsonl.gz 11830926 fda5ecba6aa24ea471e86853596d7840918ec4f79541a3d3d968b1afff5dbccf removed
[2026-10-11T08:35:54Z] X 1791693900-stream.jsonl.gz 10615743 a66ee84f868e6874204419f8462943cead9edc18561398936d995fa4a393d287 removed
[2026-10-11T08:35:54Z] X 1791694800-stream.jsonl.gz 12732416 cca4f7fd1511849c336ee64318d21e1ddbc74b9acd7f436c386b424ed801b5d4 removed
[2026-10-11T08:35:54Z] X 1791695700-stream.jsonl.gz 12435463 259f6b40c19d3ef2faf993ae6d9a28c32480355cc3fca75276546156228d70b7 removed
[2026-10-11T08:35:54Z] X 1791696600-stream.jsonl.gz 21533515 8a600a6750338c9072aa29811a6ac16971123573b6537eb54e816df3969447b6 removed
[2026-10-11T08:35:54Z] X 1791697500-stream.jsonl.gz 8946297 efbc615ed1bba78b2aa4872a9f5780bc0f46c3614443a45b29b802bfa931873c removed
[2026-10-11T08:35:54Z] X 1791698400-stream.jsonl.gz 17931091 eaa000dd2664e3013f33318df6a4f9a6e58085a2c66262374e2dcec6ab960e69 removed
[2026-10-11T08:35:54Z] X 1791699300-stream.jsonl.gz 10168130 a6b417a805200d2a36f156a2809c7c09cf41a45890558432218d81b292855715 removed
[2026-10-11T08:35:54Z] X 1791700200-stream.jsonl.gz 5672037 268e31d2c217dacbce44f02128e9949b5a3551e9b8e441caf9776507d7feff67 removed
[2026-10-11T08:35:54Z] X 1791701100-stream.jsonl.gz 7932326 49e14ae788bc6c6d63947cd584a50b3983b7be6f7d6aa4065b01f9d42e87b1fb removed
[2026-10-11T08:35:54Z] X 1791702000-stream.jsonl.gz 9990431 2d12f225b94db6e563d3fc4ac68a329d7537bdbaac67eb16e518c5a02689612a removed
[2026-10-11T08:35:54Z] X 1791702900-stream.jsonl.gz 10963207 bd299f639f39b9954d9590d0c0178d3ee10aadae36902ff32b21849508294730 removed
[2026-10-11T08:35:54Z] X 1791703800-stream.jsonl.gz 9651372 9960707372625ab632458eacc4a1d003dd553256a1822e55610a5516ad9eb785 removed
[2026-10-11T08:35:54Z] X 1791704700-stream.jsonl.gz 24968352 7dff7b4da4db3d94b655a0433346eab280f465eae99e42de0d03d20397d1447d removed
[2026-10-11T08:35:54Z] X 1791705600-stream.jsonl.gz 8059980 1df39ae5f1709395ed1c4d24c654762bd972097b47d87e5e43f007d36e404401 removed
[2026-10-11T08:35:54Z] free 12298153984 bytes before, 12977070080 after: +678916096; the store's stream files now 10095699 bytes
[2026-10-11T08:35:54Z] DELETE PASS: 51 of 51 files removed, 51 by this run (678739504 bytes) and 0 by an earlier one; every window kept its other entries
[2026-10-11T08:35:54Z] peak memory of this run: 30818304 bytes
[2026-10-11T08:35:54Z] opens refused: 0; store opens 51; requests 0, uploads 0, downloads 0 (0 bytes); files removed 51
```

Then the Executor's `I removed` (`logs/26-removed.log`) and the `df`/`du` line again (`logs/27-df-after-delete.log`):

```
Sun Oct 11 08:36:53 AM UTC 2026
[2026-10-11T08:36:53Z] G-DELETE every file of the set absent         True
[2026-10-11T08:36:53Z] G-DELETE each removal recorded by delete      True
[2026-10-11T08:36:53Z] G-DELETE each window keeps its window.json    True
[2026-10-11T08:36:53Z] REMOVED PASS: 51 of 51 files gone, 51 removals recorded, 51 windows kept
[2026-10-11T08:36:53Z] peak memory of this run: 28717056 bytes
[2026-10-11T08:36:53Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
Sun Oct 11 08:36:53 AM UTC 2026
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12977340416
11392663	/var/lib/btc-pairbook
```

- **`DELETE PASS`:** 51 of 51 removed by this run, 678,739,504 bytes, 0 by an earlier run. Every window kept its other entries.
- **`REMOVED PASS`:** 3 of 3 checks — 51 of 51 files gone, 51 removals recorded, 51 windows keep their `window.json`.
- **Free space and `du`, before → after:** free 12,298,158,080 → 12,977,340,416, `du` 690,132,167 → 11,392,663, a difference of exactly 678,739,504.
- **`archive/delete.jsonl`:** SHA-256 `aa83822608e4f4d7159dfe38525cda3275167a2eccee7eaf99bdabf3f69bf0c4`, 11,259 bytes, 51 records.

### 2.11 §3.9 — B-KILL-SVC; G-RESTART, G-COUNTER and G-UNIT (V11, V12, V13): **PASS**

The mark was taken as its own command (`logs/28-mark-kill-svc.log`); then B-KILL-SVC ran as the TZ prints it (`logs/29-B-KILL-SVC.log`). Neither was refused.

```
Sun Oct 11 08:37:01 AM UTC 2026
[2026-10-11T08:37:01Z] mark kill-svc at 2026-10-11T08:37:01Z, 421 s into its window: btc-pairbook.service {'ns': 1791707821341925020, 'unit': 'btc-pairbook.service', 'MainPID': '752775', 'NRestarts': '1', 'ActiveState': 'active'}
[2026-10-11T08:37:01Z] peak memory of this run: 28712960 bytes
[2026-10-11T08:37:01Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
Sun Oct 11 08:37:06 AM UTC 2026
phase=426
exit=0
1791707826.130363600
```

`I restart`, at 08:37:41 UTC, 35 s after the signal (`logs/30-restart.log`, verbatim):

```
Sun Oct 11 08:37:41 AM UTC 2026
[2026-10-11T08:37:41Z] record stop pid 752775 at 2026-10-11T08:37:06Z, 426 s into its window
[2026-10-11T08:37:41Z] record start pid 815823 at 2026-10-11T08:37:11Z, 431 s into its window
[2026-10-11T08:37:41Z] G-RESTART a stop of the marked process   True
[2026-10-11T08:37:41Z] G-RESTART stopped inside the band        True
[2026-10-11T08:37:41Z] G-RESTART a start of another process     True
[2026-10-11T08:37:41Z] G-RESTART within 60 s                    True
[2026-10-11T08:37:41Z] G-RESTART the same code                  True
[2026-10-11T08:37:41Z] G-RESTART PASS: the stop of 752775, the start of 815823 5.647 s later
[2026-10-11T08:37:41Z] the start record: stream_bytes 10095699, free_bytes 12977250304; its window 1791707400 (2026-10-11T08:30:00Z); the store's streams of the windows closed before it 10095699 bytes
[2026-10-11T08:37:41Z] G-COUNTER started before its window's documents    True
[2026-10-11T08:37:41Z] G-COUNTER the counter equals the store             True
[2026-10-11T08:37:41Z] G-COUNTER the counter below the cap                True
[2026-10-11T08:37:41Z] G-COUNTER no file of the set left                  True
[2026-10-11T08:37:41Z] G-COUNTER PASS: 10095699 bytes, below the cap 8000000000
[2026-10-11T08:37:41Z] G-UNIT active           True
[2026-10-11T08:37:41Z] G-UNIT enabled          True
[2026-10-11T08:37:41Z] G-UNIT fragment         True
[2026-10-11T08:37:41Z] G-UNIT control group    True
[2026-10-11T08:37:41Z] G-UNIT ceiling          True
[2026-10-11T08:37:41Z] G-UNIT argv             True
[2026-10-11T08:37:41Z] G-UNIT cwd              True
[2026-10-11T08:37:41Z] G-UNIT cgroup           True
[2026-10-11T08:37:41Z] G-UNIT sole instance    True
[2026-10-11T08:37:41Z] G-UNIT restarts         True
[2026-10-11T08:37:41Z] btc-pairbook.service MainPID 815823, NRestarts 2, MemoryMax 134217728, MemoryCurrent 25423872, MemoryPeak 25681920
[2026-10-11T08:37:41Z] G-UNIT PASS at 2 restarts
[2026-10-11T08:37:41Z] peak memory of this run: 28848128 bytes
[2026-10-11T08:37:41Z] opens refused: 0; store opens 1; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

| | pid | instant (UTC) | phase |
|---|---|---|---|
| mark `kill-svc` | `752775`, `NRestarts` 1 | 08:37:01.342 | 421 |
| B-KILL-SVC signal | — | 08:37:06 | 426 (`phase=426`) |
| `stop` record | `752775` | 08:37:06 | 426 |
| `start` record | `815823` | 08:37:11.780 | 431 |

- **G-RESTART:** the gap was 5.647 s; 5 of 5 checks.
- **G-COUNTER:** `stream_bytes` `10095699` equals the store's sum over windows `T <= 1791706500`, 10,095,699, which is below `8,000,000,000`. The start fell before `W + 545` of `W` = `1791707400`, and no file of the set was left; 4 of 4 checks.
- **G-UNIT:** 10 of 10 at 2 restarts.

### 2.12 §3.10 — G-RESUME (V14): **PASS** — `logs/31-resume-1.log`, verbatim

```
Sun Oct 11 08:45:41 AM UTC 2026
[2026-10-11T08:45:42Z] window 1791707400: pid 815823, documents True; stream opened True, off_reason None, files ['stream.jsonl.gz'], segments 1, frames 142057, stored_bytes 11832348, cut False
[2026-10-11T08:45:42Z] G-RESUME run by the restarted process   True
[2026-10-11T08:45:42Z] G-RESUME the stream opened              True
[2026-10-11T08:45:42Z] G-RESUME no reason to keep it off       True
[2026-10-11T08:45:42Z] G-RESUME a stream file                  True
[2026-10-11T08:45:42Z] READING G-RESUME: PASS, window 1791707400
[2026-10-11T08:45:42Z] peak memory of this run: 28581888 bytes
[2026-10-11T08:45:42Z] opens refused: 0; store opens 1; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

The first read came at 08:45:41 UTC, `W + 941`, and decided; no `NOT YET` occurred. Window `1791707400` reads `pid` 815823, `documents_ok` True, stream opened True, `off_reason` None and files `['stream.jsonl.gz']`, 4 of 4. Beside them: 1 segment, 142,057 frames, 11,832,348 stored bytes, cut False.

### 2.13 §3.11 — `final`: G-UNIT (V13) and G-STILL (V15): **PASS** — `logs/33-final.log`, verbatim

```
Sun Oct 11 08:46:03 AM UTC 2026
[2026-10-11T08:46:03Z] G-UNIT active           True
[2026-10-11T08:46:03Z] G-UNIT enabled          True
[2026-10-11T08:46:03Z] G-UNIT fragment         True
[2026-10-11T08:46:03Z] G-UNIT control group    True
[2026-10-11T08:46:03Z] G-UNIT ceiling          True
[2026-10-11T08:46:03Z] G-UNIT argv             True
[2026-10-11T08:46:03Z] G-UNIT cwd              True
[2026-10-11T08:46:03Z] G-UNIT cgroup           True
[2026-10-11T08:46:03Z] G-UNIT sole instance    True
[2026-10-11T08:46:03Z] G-UNIT restarts         True
[2026-10-11T08:46:03Z] btc-pairbook.service MainPID 815823, NRestarts 2, MemoryMax 134217728, MemoryCurrent 29798400, MemoryPeak 45137920
[2026-10-11T08:46:03Z] G-UNIT PASS at 2 restarts
[2026-10-11T08:46:03Z] btc-chainbook.service {'MainPID': '0', 'NRestarts': '0', 'ActiveState': 'inactive'}, MemoryCurrent [not set], MemoryPeak [not set]
[2026-10-11T08:46:03Z] btc-pairbook.service {'MainPID': '815823', 'NRestarts': '2', 'ActiveState': 'active'}, MemoryCurrent 25640960, MemoryPeak 45137920
[2026-10-11T08:46:03Z] btc-recorder.service {'MainPID': '4148534', 'NRestarts': '2', 'ActiveState': 'active'}, MemoryCurrent 183881728, MemoryPeak 206311424
[2026-10-11T08:46:03Z] G-STILL PASS: the recorder unchanged since 2026-10-11T08:20:14Z
[2026-10-11T08:46:03Z] btc-pairbook.service MemoryCurrent 25640960, MemoryPeak 45137920
[2026-10-11T08:46:03Z] the store: 53 window directories, 1791660600 to 1791707400; its stream files 21928047 bytes; free 12964605952 bytes
[2026-10-11T08:46:03Z] the set's rate: 1277627302 bytes a day over windows 1791660600 to 1791705600
[2026-10-11T08:46:03Z] at that rate the cap stops the streams in 6.24 days, at 2026-10-17T14:38:02Z
[2026-10-11T08:46:03Z] at that rate the floor, base 43500000 bytes a day stops the streams in 6.41 days, at 2026-10-17T18:32:17Z
[2026-10-11T08:46:03Z] at that rate the floor, base 187760570 bytes a day stops the streams in 5.78 days, at 2026-10-17T03:24:00Z
[2026-10-11T08:46:03Z] FINAL PASS
[2026-10-11T08:46:03Z] peak memory of this run: 28844032 bytes
[2026-10-11T08:46:03Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
exit=0
```

**The projection, printed and not gated:** the set's rate is 1,277,627,302 bytes a day over windows `1791660600` to `1791705600`.
- **The cap:** 6.24 days, at 2026-10-17 14:38:02 UTC.
- **The floor:** at the base of 43,500,000 bytes a day, 6.41 days, at 18:32:17 UTC. At the base of 187,760,570 bytes a day, 5.78 days, at 03:24:00 UTC.

### 2.14 Units' memory at every read

| instant (UTC) | read | recorder `MemoryCurrent` / `MemoryPeak` | pair book `MemoryCurrent` / `MemoryPeak` | chain book |
|---|---|---|---|---|
| 08:20:14 | `still` | 112,386,048 / 206,311,424 | 2,396,160 / 84,992,000 (pid 752775) | `[not set]` |
| 08:37:41 | `restart` | — | 25,423,872 / 25,681,920 (pid 815823) | — |
| 08:46:03 | `final` (G-UNIT) | — | 29,798,400 / 45,137,920 | — |
| 08:46:03 | `final` (`still`) | 183,881,728 / 206,311,424 | 25,640,960 / 45,137,920 | `[not set]` |
| 08:46:16 | §3.12 `systemctl show` | 183,898,112 / 206,311,424 | 25,640,960 / 45,137,920 | `[not set]` |

`journalctl` records the old pair book process's whole-life peak: `81.0M memory peak, 36.5M memory swap peak`.

### 2.15 Each pass's first and last stamped line — for B3's measurement's lag

| pass | first stamped line | last stamped line |
|---|---|---|
| `inventory` 1 | `[2026-10-11T08:21:06Z] MemAvailable 262303744 bytes, floor 93454336` | `[2026-10-11T08:21:08Z] opens refused: 0; store opens 51; …` |
| `inventory` 2 | `[2026-10-11T08:21:16Z] MemAvailable 252850176 bytes, floor 93454336` | `[2026-10-11T08:21:18Z] opens refused: 0; store opens 51; …` |
| `upload` (one run) | `[2026-10-11T08:24:29Z] MemAvailable 313114624 bytes, floor 93454336` | `[2026-10-11T08:25:42Z] opens refused: 0; store opens 51; requests 54, uploads 51, …` |
| `verify` | `[2026-10-11T08:27:46Z] MemAvailable 266764288 bytes, floor 93454336` | `[2026-10-11T08:28:34Z] opens refused: 0; store opens 0; requests 53, uploads 0, downloads 51 (678739504 bytes); …` |
| `delete` | `[2026-10-11T08:35:53Z] MemAvailable 276144128 bytes, floor 93454336` | `[2026-10-11T08:35:54Z] opens refused: 0; store opens 51; …; files removed 51` |

Window `1791706500`'s stream ran from `T+595` to `T+905`, 08:24:55 to 08:30:05 UTC. Two passes overlap it: `upload` from 08:24:55 to its end at 08:25:42, and the whole of `verify`, 08:27:46 to 08:28:34. Both `inventory` runs (08:21) fall before it. Window `1791707400`'s stream opened at 08:39:55. `delete` (08:35:53 to 08:35:54) and the `SIGTERM` restart (08:37:06 to 08:37:11) fall between the two streams, outside both.

### 2.16 Memory, the hook and the counters — every mode (V16)

| mode | instant | peak memory | opens refused | store opens | requests | files removed |
|---|---|---|---|---|---|---|
| `fingerprint` (`I0`) | 08:19:03 | 29,634,560 | 0 | 0 | 0 | 0 |
| `selftest` | 08:20:01 | 46,411,776 | 0 | 0 | 39 (loopback), 7 uploads, 9 downloads | 4 (§6 item 3) |
| `still` | 08:20:14 | 28,581,888 | 0 | 0 | 0 | 0 |
| `scratch` | 08:20:14 | 28,717,056 | 0 | 0 | 0 | 0 |
| `reclaim` (scratch) | 08:20:21 | 30,523,392 | 0 | 0 | 0 | 0 |
| `path` | 08:20:57 | 33,300,480 | 0 | 0 | 3 | 0 |
| `inventory` 1 | 08:21:08 | 30,646,272 | 0 | 51 | 0 | 0 |
| `inventory` 2 | 08:21:18 | 30,777,344 | 0 | 51 | 0 | 0 |
| `tagged` | 08:21:25 | 28,712,960 | 0 | 0 | 0 | 0 |
| `upload` (Boss) | 08:25:42 | 31,326,208 | 0 | 51 | 54, 51 uploads | 0 |
| `verify` (`NOT YET`) | 08:27:33 | 28,712,960 | 0 | 0 | 0 | 0 |
| `verify` | 08:28:34 | 33,857,536 | 0 | 0 | 53, 51 downloads | 0 |
| `delete` (Boss) | 08:35:54 | 30,818,304 | 0 | 51 | 0 | 51 |
| `removed` | 08:36:53 | 28,717,056 | 0 | 0 | 0 | 0 |
| `mark kill-svc` | 08:37:01 | 28,712,960 | 0 | 0 | 0 | 0 |
| `restart` | 08:37:41 | 28,848,128 | 0 | 1 | 0 | 0 |
| `resume` | 08:45:42 | 28,581,888 | 0 | 1 | 0 | 0 |
| `final` | 08:46:03 | 28,844,032 | 0 | 0 | 0 | 0 |
| `reclaim` (own) | 08:49:54 | 30,642,176 | 0 | 0 | 0 | 0 |

Opens refused are `0` at every mode. Store opens are n = 51 at each `inventory` and at `delete`; one for each upload attempt, 51 for 51; `1` at `restart`; `1` at `resume`; and `0` elsewhere. Requests are `3` at `path`. Files removed: 51 by `delete`, and 0 by every other mode but the self-test (§6 item 3). The largest peak, 46,411,776 at `selftest`, is below half the memory floor.

### 2.17 §3.12 — the closing reads (V18) — `logs/34-closing-reads.log`, verbatim

```
Sun Oct 11 08:46:16 AM UTC 2026
1791708376
1
MemTotal:         978640 kB
MemAvailable:     298232 kB
SwapTotal:       3174396 kB
SwapFree:        2799840 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12964564992
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
1
active
exit=0
enabled
exit=0
cmp exit=0
runtime exit=0
e8b46a85d61e1a17841962846f6d3012046c2d70
caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec  /root/btc-pairbook-svc/tz26-nesting-b3-capture.py
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
/root/tz26-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
1766
/root/btc-5m-twap       c8352f5 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/root/tz27-work/wt      bce5a85 [tz-27-pairbook-archive]
23251959	/var/lib/btc-pairbook
197095127	/root/.claude
532642977	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/70b5ba7a-7e9e-5c10-a353-278a1431d82a/scratchpad
total 16
drwx------  4 root root 4096 Oct 11 08:25 .
drwx------ 16 root root 4096 Oct 11 08:17 ..
drwx------  4 root root 4096 Oct 11 08:17 70b5ba7a-7e9e-5c10-a353-278a1431d82a
drwx------  3 root root 4096 Oct 11 08:17 952e88f3-b9a6-4bd2-b674-b9deebd16088
=== section 3.12
MainPID=4148534
NRestarts=2
MemoryCurrent=183898112
MemoryPeak=206311424
ActiveState=active

MainPID=815823
NRestarts=2
MemoryCurrent=25640960
MemoryPeak=45137920
ActiveState=active

MainPID=0
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=[not set]
ActiveState=inactive
2026-10-11T08:37:06+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 752775 (python) on client request.
2026-10-11T08:37:06+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-11T08:37:06+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 14min 10.543s CPU time, 81.0M memory peak, 36.5M memory swap peak.
2026-10-11T08:37:11+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 2.
2026-10-11T08:37:11+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
[2026-10-11T07:00:10Z] window 1791701100 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 95067 frames, 1 segments, 7932326 bytes stored
[2026-10-11T07:00:10Z] window 1791702000 (2026-10-11T07:00:00Z): documents from 2026-10-11T07:09:05Z
[2026-10-11T07:15:10Z] window 1791702000 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 119893 frames, 1 segments, 9990431 bytes stored
[2026-10-11T07:15:10Z] window 1791702900 (2026-10-11T07:15:00Z): documents from 2026-10-11T07:24:05Z
[2026-10-11T07:30:10Z] window 1791702900 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 130567 frames, 1 segments, 10963207 bytes stored
[2026-10-11T07:30:10Z] window 1791703800 (2026-10-11T07:30:00Z): documents from 2026-10-11T07:39:05Z
[2026-10-11T07:45:09Z] window 1791703800 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 115104 frames, 1 segments, 9651372 bytes stored
[2026-10-11T07:45:09Z] window 1791704700 (2026-10-11T07:45:00Z): documents from 2026-10-11T07:54:05Z
[2026-10-11T08:00:09Z] window 1791704700 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 289375 frames, 1 segments, 24968352 bytes stored
[2026-10-11T08:00:09Z] window 1791705600 (2026-10-11T08:00:00Z): documents from 2026-10-11T08:09:05Z
[2026-10-11T08:15:10Z] window 1791705600 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 96209 frames, 1 segments, 8059980 bytes stored
[2026-10-11T08:15:10Z] window 1791706500 (2026-10-11T08:15:00Z): documents from 2026-10-11T08:24:05Z
[2026-10-11T08:30:10Z] window 1791706500 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 118386 frames, 2 segments, 10095699 bytes stored
[2026-10-11T08:30:10Z] window 1791707400 (2026-10-11T08:30:00Z): documents from 2026-10-11T08:39:05Z
[2026-10-11T08:37:06Z] stop record written; requests 1440, sessions 66, frames 7608796, stream bytes 637814226, other bytes 1182513
[2026-10-11T08:37:11Z] stale pid file (pid 752775) replaced
[2026-10-11T08:37:11Z] start record: pid 815823 commit e8b46a85d61e1a17841962846f6d3012046c2d70 file_sha256 caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec; free 12977250304 bytes, streams 10095699 bytes
[2026-10-11T08:37:11Z] window 1791707400 (2026-10-11T08:30:00Z): documents from 2026-10-11T08:39:05Z
[2026-10-11T08:45:10Z] window 1791707400 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 142057 frames, 1 segments, 11832348 bytes stored
[2026-10-11T08:45:10Z] window 1791708300 (2026-10-11T08:45:00Z): documents from 2026-10-11T08:54:05Z
               total        used        free      shared  buff/cache   available
Mem:      1002127360   679907328    81248256      237568   426999808   322220032
Swap:     3250581504   385118208  2865463296
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12964560896
6399821	/root/tz27-work
23251959	/var/lib/btc-pairbook
197095127	/root/.claude
{
 "delete": {
  "at": "2026-10-11T08:35:54Z",
  "bytes": 678739504,
  "removed": 51
 },
 "marks": {
  "kill-svc": {
   "ActiveState": "active",
   "MainPID": "752775",
   "NRestarts": "1",
   "ns": 1791707821341925020,
   "unit": "btc-pairbook.service"
  }
 },
 "restart": {
  "W": 1791707400,
  "free_bytes": 12977250304,
  "pid": 815823,
  "start_wall_ns": 1791707831780232926,
  "stream_bytes": 10095699
 },
 "set": {
  "as_of": 1791706862,
  "assets_n": 51,
  "bytes_total": 678739504,
  "first_T": 1791660600,
  "last_T": 1791705600,
  "sha256": "ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd",
  "tag": "tz-27-pairbook-streams"
 },
 "still": {
  "at": "2026-10-11T08:20:14Z",
  "recorder": {
   "ActiveState": "active",
   "MainPID": "4148534",
   "NRestarts": "2"
  }
 },
 "tag": {
  "commit": "bce5a85be7850a33f95192265b916cc9c5e0aaf1",
  "name": "tz-27-pairbook-streams",
  "object": "e299d4e45f48b7efaa8cb18bd54b139fc0627630"
 },
 "verify": {
  "assets_n": 51,
  "at": "2026-10-11T08:28:34Z",
  "pass": true,
  "release_id": 409534533,
  "set_sha256": "ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd",
  "verify_sha256": "6eeb9bb3f414c032f62a0a766cfb28fb465661921b555ba6be308e299e8c411d"
 }
}
```

`journalctl` shows the `SIGTERM` to `752775` at 08:37:06, "Deactivated successfully", and the restart job at counter 2 with the start at 08:37:11. `service.log` shows the `stop` record, the stale pid file replaced, and the start record of `815823` with `streams 10095699 bytes`. Window `1791707400` closed with its stream opened.

### 2.18 Every file the run wrote, by SHA-256, but the Release's assets

Hashed at 08:46:27 UTC (`logs/36-files-written.log`, verbatim). Its own line is a hash of that file taken while it was being written (§6 item 4). Every logs/, archive/ and state file is hashed again, final, by B-RECLAIM-OWN's `R` lines in §2.19.

```
aa83822608e4f4d7159dfe38525cda3275167a2eccee7eaf99bdabf3f69bf0c4  ./archive/delete.jsonl
ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd  ./archive/set.json
1e5fd981281ee7070c87b1bdb3c83b576e537eae30863d7511472a75378d370a  ./archive/upload.jsonl
6eeb9bb3f414c032f62a0a766cfb28fb465661921b555ba6be308e299e8c411d  ./archive/verify.json
ee4374f13c4e6f1b37fbfbf9a065290a45225a56e75fe90fdc08eacc5e58b88b  ./logs/00-start.log
9f7cab1c642938776991d8fff2ccab3c68f124b616381f4067320697899d9615  ./logs/01-stage.log
aa5fc8d705008e6384f964e2b0fb335a621e975c9f949931636c78f397b2ecf0  ./logs/02-fingerprint.log
33502d21e98048fa522f952fdb58a9ba02b09b3bb30e962801578e8ab282e600  ./logs/03-host-gate.log
1c9ff0d894db74e09a60a60f083d4eb26c17b9c441459d19cf3b9058a403438a  ./logs/04-refs.log
e99cc74fa8553d782e9e8f9ee9d16f0c65db34e12dabdaf62e18a80b3a94081d  ./logs/05-branch.log
7da94f24f9dc9457a5d55c5ab827370c82809d2afdb65e8daa46a16c41c57423  ./logs/06-commit-push.log
e236edae2917957294edb5c1425d7936970218183e4ecd102c1e7118c4f0d35f  ./logs/07-pr.log
f91a33bfbe7337192301b120cb75b7faefc8f70a635cd70a484f720956b0203f  ./logs/08-selftest.log
0a42ce79ea8e440941a0aac61c7db4aa903084b4584b24d31c94df2c91ec4982  ./logs/09-still.log
7df866e89d80b5cc6f219a47a91390ae11f50e9f5f53332582d048b3374071f4  ./logs/10-scratch.log
281a9ed6984324937000f881329de74b86af900a858f3df138a4f5691aa96ce4  ./logs/11-reclaim-scratch.log
cd1ac58617d49c0ab830bd960cc621431359fe2c31eca3c74937c41ce0f3fcd6  ./logs/12-rm-30ec6406.log
34c5d66b13755113e04ebfcce49e80af8aef6aa4dd010114bcae1cf6362a2b09  ./logs/13-rm-d5dc7bd3-refused.log
36f92fca408f9d9a14bebda7e3468cd11b83edfc686eadb27b79ed896ebf857d  ./logs/14-path.log
a2345f35589f80df0b2f5b459e341425d662966970349468be9549a068186135  ./logs/15-A.log
48a4e7c4b60f2bd8a649ec9f0c6015362bab5bc4f9be28d2abc013469c27c319  ./logs/16-inventory-1.log
3d6c2b82cc5fd0735ae47afc5af35232d1724aa28dca224fb20f42d49994631a  ./logs/17-inventory-2.log
60a8d62b6638ce04973d424c0bcb9364555a5f4b1f68f4fcd65273afc6713b1e  ./logs/18-tag.log
087a34724239a3bf294fb4a70c1c3e59ecfc86db8e38e9127d482b87803d4665  ./logs/19-tagged.log
a5c8558cc404c3cbda612f77901ccc747cca7ac022ad242a03a26e12091be5c2  ./logs/20-boss-blocks.log
e092db0f7333872aa77d2e2938542140d1758a7dd9a1a1f60e3ddf0e033a570c  ./logs/21-verify-notyet.log
b8a544146d18dfd468cb6638d625f4d1a3be36bc253693882e881a15003a6bba  ./logs/22-verify.log
8c4926c8bb3aed161d2c56aa21149132345c022f379df0e8c5c119555f4b4e6d  ./logs/25-boss-delete.log
5ac25a3f405490d971a6c418c1882a77b73331fb72087799eda2af227e328c85  ./logs/26-removed.log
7bfe5d8a48ce48219cabfdfdda02357038b0639f5ea31d1040638020ac20e7b5  ./logs/27-df-after-delete.log
5b86da2b88202678278d1e1ac33aeb79f23128ae4454b56091a2c5ce5e399037  ./logs/28-mark-kill-svc.log
8201a2bc70e452ae23f55c937e028ad70cb4fb5c1a391fb5b61231df3f0d59fd  ./logs/29-B-KILL-SVC.log
1c3a75cdaeec4d411f34d39cf0ad9aa97f0821ccbb150c7ed5483435254ce1f4  ./logs/30-restart.log
4b1b45359b74091e271b194149dff68329faece84fcbf8832ac6520cf78a55c9  ./logs/31-resume-1.log
7f05f21313953ff34d05f9319749ddab2495bcf69caeeaa1dbf827b6df547b2c  ./logs/32-asset-table.log
3680e6571319f5283629d08eb7a99fedabebdc758aa06554d901676a8ea6cd39  ./logs/33-final.log
4c3e53422593848cf1d2509c4cb022342c017b78dbb1eb06e99b4621b3a95e9d  ./logs/34-closing-reads.log
0e07354efd0122822a54b66df1cf64e06a76d179f6d70bf3ab0be5214b6d3920  ./logs/35-separation.log
3473e020d4ced89dce22d73af379d01323c34aae641a14a0968ba80fe743773b  ./logs/36-files-written.log
42c90b9e768207f449ec318f603b04dd010396dcbebecfd4733a97a0387a27c5  ./logs/B-DELETE-df-before.log
e175803f49122fe11f2ee17e2a914d4bcdd36eee6070a10a98c2278a17129109  ./logs/B-DELETE.log
6993c6b673b69f99142ca7a109c15190f0e8afe2257d82ca0a41e9bd62f2904e  ./logs/B-UPLOAD.log
2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673  ./stage/research/tz27-pairbook-archive.py
fb2c847d63c2a20a75c20f44a2791e89a1c9f029dfb84746b82086b6695d29b8  ./state.json
```

Also written, outside the work tree: the branch commit `bce5a85`, the pull request #26, the tag object `e299d4e…`, the Release `409534533` with its 51 assets (§3), and this report. The unit wrote its own records at its restart.

### 2.19 §9 B-RECLAIM-OWN — last, after §3.12, with this report drafted

Its output was written to no file. Quoted verbatim from the session:

```
$ cd /root/tz27-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz27-work/wt/research/tz27-pairbook-archive.py reclaim /root/tz27-work
[2026-10-11T08:49:54Z] reclaim: 2152 report tokens; forensic store holds 1766 files
[2026-10-11T08:49:54Z] reclaim: /root/tz27-work/wt skipped: no file but its HEAD's, and HEAD bce5a85be7850a33f95192265b916cc9c5e0aaf1 is its upstream's
[2026-10-11T08:49:54Z] R copied fb2c847d63c2a20a75c20f44a2791e89a1c9f029dfb84746b82086b6695d29b8 /root/btc-forensics/tz27-work--state.json
[2026-10-11T08:49:54Z] R copied aa83822608e4f4d7159dfe38525cda3275167a2eccee7eaf99bdabf3f69bf0c4 /root/btc-forensics/tz27-work--archive--delete.jsonl
[2026-10-11T08:49:54Z] R copied ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd /root/btc-forensics/tz27-work--archive--set.json
[2026-10-11T08:49:54Z] R copied 1e5fd981281ee7070c87b1bdb3c83b576e537eae30863d7511472a75378d370a /root/btc-forensics/tz27-work--archive--upload.jsonl
[2026-10-11T08:49:54Z] R copied 6eeb9bb3f414c032f62a0a766cfb28fb465661921b555ba6be308e299e8c411d /root/btc-forensics/tz27-work--archive--verify.json
[2026-10-11T08:49:54Z] R copied ee4374f13c4e6f1b37fbfbf9a065290a45225a56e75fe90fdc08eacc5e58b88b /root/btc-forensics/tz27-work--logs--00-start.log
[2026-10-11T08:49:54Z] R copied 9f7cab1c642938776991d8fff2ccab3c68f124b616381f4067320697899d9615 /root/btc-forensics/tz27-work--logs--01-stage.log
[2026-10-11T08:49:54Z] R copied aa5fc8d705008e6384f964e2b0fb335a621e975c9f949931636c78f397b2ecf0 /root/btc-forensics/tz27-work--logs--02-fingerprint.log
[2026-10-11T08:49:54Z] R copied 33502d21e98048fa522f952fdb58a9ba02b09b3bb30e962801578e8ab282e600 /root/btc-forensics/tz27-work--logs--03-host-gate.log
[2026-10-11T08:49:54Z] R copied 1c9ff0d894db74e09a60a60f083d4eb26c17b9c441459d19cf3b9058a403438a /root/btc-forensics/tz27-work--logs--04-refs.log
[2026-10-11T08:49:54Z] R copied e99cc74fa8553d782e9e8f9ee9d16f0c65db34e12dabdaf62e18a80b3a94081d /root/btc-forensics/tz27-work--logs--05-branch.log
[2026-10-11T08:49:54Z] R copied 7da94f24f9dc9457a5d55c5ab827370c82809d2afdb65e8daa46a16c41c57423 /root/btc-forensics/tz27-work--logs--06-commit-push.log
[2026-10-11T08:49:54Z] R copied e236edae2917957294edb5c1425d7936970218183e4ecd102c1e7118c4f0d35f /root/btc-forensics/tz27-work--logs--07-pr.log
[2026-10-11T08:49:54Z] R copied f91a33bfbe7337192301b120cb75b7faefc8f70a635cd70a484f720956b0203f /root/btc-forensics/tz27-work--logs--08-selftest.log
[2026-10-11T08:49:54Z] R copied 0a42ce79ea8e440941a0aac61c7db4aa903084b4584b24d31c94df2c91ec4982 /root/btc-forensics/tz27-work--logs--09-still.log
[2026-10-11T08:49:54Z] R copied 7df866e89d80b5cc6f219a47a91390ae11f50e9f5f53332582d048b3374071f4 /root/btc-forensics/tz27-work--logs--10-scratch.log
[2026-10-11T08:49:54Z] R copied 281a9ed6984324937000f881329de74b86af900a858f3df138a4f5691aa96ce4 /root/btc-forensics/tz27-work--logs--11-reclaim-scratch.log
[2026-10-11T08:49:54Z] R copied cd1ac58617d49c0ab830bd960cc621431359fe2c31eca3c74937c41ce0f3fcd6 /root/btc-forensics/tz27-work--logs--12-rm-30ec6406.log
[2026-10-11T08:49:54Z] R copied 34c5d66b13755113e04ebfcce49e80af8aef6aa4dd010114bcae1cf6362a2b09 /root/btc-forensics/tz27-work--logs--13-rm-d5dc7bd3-refused.log
[2026-10-11T08:49:54Z] R copied 36f92fca408f9d9a14bebda7e3468cd11b83edfc686eadb27b79ed896ebf857d /root/btc-forensics/tz27-work--logs--14-path.log
[2026-10-11T08:49:54Z] R copied a2345f35589f80df0b2f5b459e341425d662966970349468be9549a068186135 /root/btc-forensics/tz27-work--logs--15-A.log
[2026-10-11T08:49:54Z] R copied 48a4e7c4b60f2bd8a649ec9f0c6015362bab5bc4f9be28d2abc013469c27c319 /root/btc-forensics/tz27-work--logs--16-inventory-1.log
[2026-10-11T08:49:54Z] R copied 3d6c2b82cc5fd0735ae47afc5af35232d1724aa28dca224fb20f42d49994631a /root/btc-forensics/tz27-work--logs--17-inventory-2.log
[2026-10-11T08:49:54Z] R copied 60a8d62b6638ce04973d424c0bcb9364555a5f4b1f68f4fcd65273afc6713b1e /root/btc-forensics/tz27-work--logs--18-tag.log
[2026-10-11T08:49:54Z] R copied 087a34724239a3bf294fb4a70c1c3e59ecfc86db8e38e9127d482b87803d4665 /root/btc-forensics/tz27-work--logs--19-tagged.log
[2026-10-11T08:49:54Z] R copied a5c8558cc404c3cbda612f77901ccc747cca7ac022ad242a03a26e12091be5c2 /root/btc-forensics/tz27-work--logs--20-boss-blocks.log
[2026-10-11T08:49:54Z] R copied e092db0f7333872aa77d2e2938542140d1758a7dd9a1a1f60e3ddf0e033a570c /root/btc-forensics/tz27-work--logs--21-verify-notyet.log
[2026-10-11T08:49:54Z] R copied b8a544146d18dfd468cb6638d625f4d1a3be36bc253693882e881a15003a6bba /root/btc-forensics/tz27-work--logs--22-verify.log
[2026-10-11T08:49:54Z] R copied 8c4926c8bb3aed161d2c56aa21149132345c022f379df0e8c5c119555f4b4e6d /root/btc-forensics/tz27-work--logs--25-boss-delete.log
[2026-10-11T08:49:54Z] R copied 5ac25a3f405490d971a6c418c1882a77b73331fb72087799eda2af227e328c85 /root/btc-forensics/tz27-work--logs--26-removed.log
[2026-10-11T08:49:54Z] R copied 7bfe5d8a48ce48219cabfdfdda02357038b0639f5ea31d1040638020ac20e7b5 /root/btc-forensics/tz27-work--logs--27-df-after-delete.log
[2026-10-11T08:49:54Z] R copied 5b86da2b88202678278d1e1ac33aeb79f23128ae4454b56091a2c5ce5e399037 /root/btc-forensics/tz27-work--logs--28-mark-kill-svc.log
[2026-10-11T08:49:54Z] R copied 8201a2bc70e452ae23f55c937e028ad70cb4fb5c1a391fb5b61231df3f0d59fd /root/btc-forensics/tz27-work--logs--29-B-KILL-SVC.log
[2026-10-11T08:49:54Z] R copied 1c3a75cdaeec4d411f34d39cf0ad9aa97f0821ccbb150c7ed5483435254ce1f4 /root/btc-forensics/tz27-work--logs--30-restart.log
[2026-10-11T08:49:54Z] R copied 4b1b45359b74091e271b194149dff68329faece84fcbf8832ac6520cf78a55c9 /root/btc-forensics/tz27-work--logs--31-resume-1.log
[2026-10-11T08:49:54Z] R copied 7f05f21313953ff34d05f9319749ddab2495bcf69caeeaa1dbf827b6df547b2c /root/btc-forensics/tz27-work--logs--32-asset-table.log
[2026-10-11T08:49:54Z] R copied 3680e6571319f5283629d08eb7a99fedabebdc758aa06554d901676a8ea6cd39 /root/btc-forensics/tz27-work--logs--33-final.log
[2026-10-11T08:49:54Z] R copied 4c3e53422593848cf1d2509c4cb022342c017b78dbb1eb06e99b4621b3a95e9d /root/btc-forensics/tz27-work--logs--34-closing-reads.log
[2026-10-11T08:49:54Z] R copied 0e07354efd0122822a54b66df1cf64e06a76d179f6d70bf3ab0be5214b6d3920 /root/btc-forensics/tz27-work--logs--35-separation.log
[2026-10-11T08:49:54Z] R copied ceb8e2036f25ae186f10827b15916f32300b59907933f079542bbcd3ee308294 /root/btc-forensics/tz27-work--logs--36-files-written.log
[2026-10-11T08:49:54Z] R copied 42c90b9e768207f449ec318f603b04dd010396dcbebecfd4733a97a0387a27c5 /root/btc-forensics/tz27-work--logs--B-DELETE-df-before.log
[2026-10-11T08:49:54Z] R copied e175803f49122fe11f2ee17e2a914d4bcdd36eee6070a10a98c2278a17129109 /root/btc-forensics/tz27-work--logs--B-DELETE.log
[2026-10-11T08:49:54Z] R copied 6993c6b673b69f99142ca7a109c15190f0e8afe2257d82ca0a41e9bd62f2904e /root/btc-forensics/tz27-work--logs--B-UPLOAD.log
[2026-10-11T08:49:54Z] R copied 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673 /root/btc-forensics/tz27-work--stage--research--tz27-pairbook-archive.py
[2026-10-11T08:49:54Z] RECLAIM PASS: 46 files considered, 43 named by a report, 1 kept by name, 44 copied, 0 already held; forensic store 1766 -> 1810 files
[2026-10-11T08:49:54Z] peak memory of this run: 30642176 bytes
[2026-10-11T08:49:54Z] opens refused: 0; store opens 0; requests 0, uploads 0, downloads 0 (0 bytes); files removed 0
$ git -C /root/btc-5m-twap worktree remove /root/tz27-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz27-work; echo "exit=$?"
exit=0
$ test -e /root/tz27-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       c8352f5 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
1810
$ df -B1 --output=source,size,avail /var/lib
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12970258432
```

**`RECLAIM PASS`** — 46 files considered, 43 named by a report (this draft included), 1 kept by name, 44 copied, 0 already held; the forensic store went from **1,766 to 1,810**, equal to before plus the copies (V19). The worktree was skipped as pristine at its upstream `bce5a85…`. The two files not copied are the report's template and the short script that filled it from the logs, neither named by a report. **None of the removals was refused** (V20): `git worktree remove` without `--force` exit 0; `rm -rf` exit 0; `test -e` exit 1. `git worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else. Afterwards the Executor hashed the 44 store copies against the `R` lines above, 44 of 44 equal, from the session's scratchpad, where this output was kept until it was placed here.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-27-pairbook-archive`, commit `bce5a85be7850a33f95192265b916cc9c5e0aaf1`, pushed to `origin` |
| pull request | #26, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/26`, open, not merged |
| tag | `tz-27-pairbook-streams`, annotated, object `e299d4e45f48b7efaa8cb18bd54b139fc0627630`, peels to `bce5a85…` |
| Release | id `409534533`, `https://github.com/seahomebatumi-ai/btc-5m-twap/releases/tag/tz-27-pairbook-streams`, published, not a draft; created by B-UPLOAD, run by the Boss |
| assets | 51, `application/gzip`, 678,739,504 bytes, each `https://github.com/seahomebatumi-ai/btc-5m-twap/releases/download/tz-27-pairbook-streams/<asset>` |
| report | `CryptoReports/TZ-27-pairbook-archive-report.md`, straight to `main` |

**Every asset — contract §5.1's local hash, the Release's digest, the downloaded hash, and that they are equal.** The table compares five values for each asset:

1. `set.json`'s SHA-256 and bytes — the local hash.
2. `upload.jsonl`'s hash of the bytes as sent.
3. The Release's `digest`, read by `verify`.
4. The anonymous download's SHA-256 and bytes, read by `verify`.
5. `delete.jsonl`'s re-hash immediately before removal.

`logs/32-asset-table.log`, verbatim:

| # | asset | bytes | SHA-256 (set.json) | sent | Release digest | downloaded | equal | removed |
|---|---|---|---|---|---|---|---|---|
| 1 | `1791660600-stream.jsonl.gz` | 13423467 | `02673b7227ce9c9d44451e3b9415fb8e84b37ab0b280aeeb15117d7776a14095` | equal | equal | equal | yes | yes |
| 2 | `1791661500-stream.jsonl.gz` | 13439976 | `8d1153a600c626bb9914f5fc18cd68e36b0fe53f3cd95cfe58746cc7025e7b51` | equal | equal | equal | yes | yes |
| 3 | `1791662400-stream.jsonl.gz` | 9568261 | `6cd316eea7ee397141e858c3b8061afbfc65f1363275b9f4810fba199e6ca60e` | equal | equal | equal | yes | yes |
| 4 | `1791663300-stream.jsonl.gz` | 14589273 | `e05ff3f11a3788498a2a3a0beb72259b4297b844a071bfa7fef2d642ee3c0dde` | equal | equal | equal | yes | yes |
| 5 | `1791664200-stream.jsonl.gz` | 13421235 | `30e3ffcd0035c928ddb9cf3beadc047b13e351a090829df46e92718a5b277e04` | equal | equal | equal | yes | yes |
| 6 | `1791665100-stream.jsonl.gz` | 11129213 | `cd6d078247cd399ffcc827355b28114711fe8c4dbf7a35f8ac8e16194a52b3f5` | equal | equal | equal | yes | yes |
| 7 | `1791666000-stream.jsonl.gz` | 25488448 | `f033da5ad81a8e5eafcc5e5867a85a86a54bb996f073178099999e63d1a7bfdd` | equal | equal | equal | yes | yes |
| 8 | `1791666900-stream.jsonl.gz` | 12837545 | `b5ab1e59d30cc64a990a9b94ed7f6d24e0807d6c3819ff52f05b1d9558440d91` | equal | equal | equal | yes | yes |
| 9 | `1791667800-stream.jsonl.gz` | 17449667 | `1f38535d92c7201e82d646644430752ffbb43777112e96747848011fcba795f8` | equal | equal | equal | yes | yes |
| 10 | `1791668700-stream.jsonl.gz` | 18821724 | `26fa1060e3dd5cc863b9d71abef1a4b682326a0911424eb761c1b71800c1187b` | equal | equal | equal | yes | yes |
| 11 | `1791669600-stream.jsonl.gz` | 18782634 | `ac057cae7f0835e3a0814f680377b7ade08b82c8daec056f0f586ab565414934` | equal | equal | equal | yes | yes |
| 12 | `1791670500-stream.jsonl.gz` | 13835617 | `3fba28fc972a067f1252d95027062a34555a364d49d97b6d7e0fc9d0fe05cc1d` | equal | equal | equal | yes | yes |
| 13 | `1791671400-stream.jsonl.gz` | 22778515 | `53ac058c216842bbe55730243450705cf4b0c57450c5994a9377e28979a8a037` | equal | equal | equal | yes | yes |
| 14 | `1791672300-stream.jsonl.gz` | 11020668 | `be47f4c6107086fdbdfa9e50322fd077779ff71ea3ee21fba510a83b0ef20f99` | equal | equal | equal | yes | yes |
| 15 | `1791673200-stream.jsonl.gz` | 17935756 | `91f62a49534c1cdaa11c960c7a1e054b50797291b972b93103b3d4304201f4d7` | equal | equal | equal | yes | yes |
| 16 | `1791674100-stream.jsonl.gz` | 16755227 | `821a3b25ca7b894ef70f74ac32067c656568c977b00672946ee7147a698cf61d` | equal | equal | equal | yes | yes |
| 17 | `1791675000-stream.jsonl.gz` | 17246512 | `5f4ddb59abb34d187de3be12baf33aeb79e2c9be9191a93e2bc2fe22eaef7d3b` | equal | equal | equal | yes | yes |
| 18 | `1791675900-stream.jsonl.gz` | 11174283 | `3ddc73de13809d435f3abe0e3ee6eadad721a363e9dc20fa0d47f52eb19bb1c9` | equal | equal | equal | yes | yes |
| 19 | `1791676800-stream.jsonl.gz` | 14095311 | `93973541db575dcf5a9497d73f61172f59299f54a5bfd764c82daf90174f651a` | equal | equal | equal | yes | yes |
| 20 | `1791677700-stream.jsonl.gz` | 9762989 | `e99255d6c6f008c761028db6d9ee077bf2045ac378a773e3c5a75c4e131501d3` | equal | equal | equal | yes | yes |
| 21 | `1791678600-stream.jsonl.gz` | 14290425 | `65716063fcea58dc0744bbcdf0c6499e60be2d64a9fd7ed94dac2132d64853bf` | equal | equal | equal | yes | yes |
| 22 | `1791679500-stream.jsonl.gz` | 15182911 | `f44fd640415c3508b37e552448bc6a901a5eb5a529478e940eff0a2823fa670a` | equal | equal | equal | yes | yes |
| 23 | `1791680400-stream.jsonl.gz` | 13039899 | `d6efb02da1c816fd51cd780b608326a90bde01ba337c78988da57d14ff241ed2` | equal | equal | equal | yes | yes |
| 24 | `1791681300-stream.jsonl.gz` | 15944520 | `e3f47ea555e0449c05b181f862340f2fbfcfb67612ea9a58be2229f465667eb1` | equal | equal | equal | yes | yes |
| 25 | `1791682200-stream.jsonl.gz` | 12105846 | `d773a167b99f70b8da2db2d13e534b26f3ca72f8d3d28437c618ab52c9fa405f` | equal | equal | equal | yes | yes |
| 26 | `1791683100-stream.jsonl.gz` | 14736000 | `27ac9a8c957e66a7d30b447303536ebc3ee5f3cd915b2dd01cec72eb2f5c81cf` | equal | equal | equal | yes | yes |
| 27 | `1791684000-stream.jsonl.gz` | 12587712 | `960a7bc878478e68425395ae4764e9e72fa2a4a7d5fdd90ccd7f12bbf9136736` | equal | equal | equal | yes | yes |
| 28 | `1791684900-stream.jsonl.gz` | 18090382 | `6ef8c2d62603ff442f5ac0f0d11d2a26a28ba1cfefc4b4ea1af27e26f5a7e050` | equal | equal | equal | yes | yes |
| 29 | `1791685800-stream.jsonl.gz` | 5691840 | `93b2387191bdbea4199ba39fe42c1266b2476d7ba9d75912552fdb01b53beb76` | equal | equal | equal | yes | yes |
| 30 | `1791686700-stream.jsonl.gz` | 10296232 | `3904d031288bbf14ea9a3f269f4260d8e0ad0f28fa8ab91f51e95fba98cdb8aa` | equal | equal | equal | yes | yes |
| 31 | `1791687600-stream.jsonl.gz` | 4761970 | `22fe211139a1475883d617bcd15861d2da59d552deb9db89c9138012f21b5365` | equal | equal | equal | yes | yes |
| 32 | `1791688500-stream.jsonl.gz` | 11715539 | `15b3ab4e3cb1fccd2a7e77f71f606f8de8894f32cc3437a6b5f016537d0bc8ef` | equal | equal | equal | yes | yes |
| 33 | `1791689400-stream.jsonl.gz` | 11045964 | `e45ae87c4d50ad67fc0f300ab9b9d123fc95deab16a30937c9ab4729adf698c6` | equal | equal | equal | yes | yes |
| 34 | `1791690300-stream.jsonl.gz` | 9320326 | `50bc2a033d3a8dc4b0aa2291563f442291e62e532a7c9698738cc7b3165dbb97` | equal | equal | equal | yes | yes |
| 35 | `1791691200-stream.jsonl.gz` | 15738124 | `53604f4792e7f198c6f95dc7061de06d65a18660e2ceedbca8f6797d3123f76f` | equal | equal | equal | yes | yes |
| 36 | `1791692100-stream.jsonl.gz` | 7204207 | `24bf61060b7b44e334467817cd71afe227e62b6edad3a139ea8142715365730c` | equal | equal | equal | yes | yes |
| 37 | `1791693000-stream.jsonl.gz` | 11830926 | `fda5ecba6aa24ea471e86853596d7840918ec4f79541a3d3d968b1afff5dbccf` | equal | equal | equal | yes | yes |
| 38 | `1791693900-stream.jsonl.gz` | 10615743 | `a66ee84f868e6874204419f8462943cead9edc18561398936d995fa4a393d287` | equal | equal | equal | yes | yes |
| 39 | `1791694800-stream.jsonl.gz` | 12732416 | `cca4f7fd1511849c336ee64318d21e1ddbc74b9acd7f436c386b424ed801b5d4` | equal | equal | equal | yes | yes |
| 40 | `1791695700-stream.jsonl.gz` | 12435463 | `259f6b40c19d3ef2faf993ae6d9a28c32480355cc3fca75276546156228d70b7` | equal | equal | equal | yes | yes |
| 41 | `1791696600-stream.jsonl.gz` | 21533515 | `8a600a6750338c9072aa29811a6ac16971123573b6537eb54e816df3969447b6` | equal | equal | equal | yes | yes |
| 42 | `1791697500-stream.jsonl.gz` | 8946297 | `efbc615ed1bba78b2aa4872a9f5780bc0f46c3614443a45b29b802bfa931873c` | equal | equal | equal | yes | yes |
| 43 | `1791698400-stream.jsonl.gz` | 17931091 | `eaa000dd2664e3013f33318df6a4f9a6e58085a2c66262374e2dcec6ab960e69` | equal | equal | equal | yes | yes |
| 44 | `1791699300-stream.jsonl.gz` | 10168130 | `a6b417a805200d2a36f156a2809c7c09cf41a45890558432218d81b292855715` | equal | equal | equal | yes | yes |
| 45 | `1791700200-stream.jsonl.gz` | 5672037 | `268e31d2c217dacbce44f02128e9949b5a3551e9b8e441caf9776507d7feff67` | equal | equal | equal | yes | yes |
| 46 | `1791701100-stream.jsonl.gz` | 7932326 | `49e14ae788bc6c6d63947cd584a50b3983b7be6f7d6aa4065b01f9d42e87b1fb` | equal | equal | equal | yes | yes |
| 47 | `1791702000-stream.jsonl.gz` | 9990431 | `2d12f225b94db6e563d3fc4ac68a329d7537bdbaac67eb16e518c5a02689612a` | equal | equal | equal | yes | yes |
| 48 | `1791702900-stream.jsonl.gz` | 10963207 | `bd299f639f39b9954d9590d0c0178d3ee10aadae36902ff32b21849508294730` | equal | equal | equal | yes | yes |
| 49 | `1791703800-stream.jsonl.gz` | 9651372 | `9960707372625ab632458eacc4a1d003dd553256a1822e55610a5516ad9eb785` | equal | equal | equal | yes | yes |
| 50 | `1791704700-stream.jsonl.gz` | 24968352 | `7dff7b4da4db3d94b655a0433346eab280f465eae99e42de0d03d20397d1447d` | equal | equal | equal | yes | yes |
| 51 | `1791705600-stream.jsonl.gz` | 8059980 | `1df39ae5f1709395ed1c4d24c654762bd972097b47d87e5e43f007d36e404401` | equal | equal | equal | yes | yes |
rows equal at every column: 51 of 51; bytes 678739504; release_id 409534533

**Contract §4.2's separation self-check, and V17's further line** — `logs/35-separation.log`, verbatim:

```
Sun Oct 11 08:46:27 AM UTC 2026
0
research/tz27-pairbook-archive.py
A	research/tz27-pairbook-archive.py
grep exit=1
0
```

The first line is `0`: the implementation commit is not on `main`. The diff names the instrument alone, `A`. Nothing on `main` is `.parquet` or `.zip` (`grep exit=1`, nothing printed). V17's line reads `0`: no `.gz` and no `.jsonl` on `main`.

---

## 4. Gate

| gate | PASS condition (TZ §4) | read | |
|---|---|---|---|
| **P-PATH** | §4.1: the record `uploaded`, `76818669`, `sha256:229a944f…`, the URL; the download `200`, 76,818,669 bytes, SHA-256 equal; 3 requests | as required | **PASS** (served) |
| **G-SET** | §4.2: both runs exit `0`, the second `unchanged` | 51 files, 678,739,504 bytes; `unchanged` | **PASS** |
| **G-UPLOAD** | §4.3: published, none missing, none beyond, each `uploaded` with the set's size, digest and URL | 51 of 51 | **PASS** |
| **G-DOWNLOAD** | §4.3: each downloaded whole, `200`, the set's bytes and SHA-256 | 51 of 51 | **PASS** |
| **G-DELETE** | §4.4: each file hashed equal, removed, logged; then every file absent, every removal recorded, every `window.json` kept | 51 of 51; 3 of 3 | **PASS** |
| **G-RESTART** | §4.5: the marked pid's `stop` at phase 15 to 481; a `start` of another pid within 60 s on the same code | phase 426; 5.647 s; same `commit` and `file_sha256` | **PASS** |
| **G-COUNTER** | §4.5: the start before `W + 545`; `stream_bytes` equal to the store over `T <= W − 900`; below `STREAM_CAP`; no set file left | 10,095,699 = 10,095,699 < 8,000,000,000 | **PASS** |
| **G-UNIT** | §4.5: 10 checks at the mark's `NRestarts` plus 1 | 10 of 10 at 2, at `restart` and at `final` | **PASS** |
| **G-RESUME** | §4.6: window `W`'s `window.json` by the restarted pid, stream opened, no off reason, a stream file | 4 of 4, window `1791707400` | **PASS** |
| **G-STILL** | the recorder's `MainPID`, `NRestarts`, `ActiveState` unchanged, §3.3 to §3.11 | `4148534`, `2`, `active` at both | **PASS** |

Every gate is exact; no number is tuned and no gate is reinterpreted. Under PASS no block of §4.7 was run: neither K-26 nor B-RESTORE-CB, nor B-START-SVC.

---

## 5. Validation

| # | check | count | asserted |
|---|---|---|---|
| V1 | §0.2's fingerprint | `FINGERPRINT PASS`; 6 of 6 anchors, 4 re-derived; 36 rows, 33 of 33 `frozen` equal | yes, by `fingerprint` |
| V2 | §0.3's host gate | H1 to H4, memory, disk: 6 of 6 | read against the TZ's literals by the Executor; the rest printed |
| V3 | §0.1's and §3.1's file | 1 of 1 hash asserted at each, 2,078 lines, 106,284 bytes; the diff `A research/tz27-pairbook-archive.py` alone | yes, by §0.1's script |
| V4 | the self-test | `63 of 63` | yes |
| V5 | P-PATH | `served`, 3 requests; state, size, digest, URL; `200`, 76,818,669, SHA-256 | yes |
| V6 | G-SET | both `READING G-SET` lines, exit `0` twice; the second `unchanged`, `ec71b1a7…`; 51 of 51 windows and 51 of 51 files printed; 2 s against 500 | yes; the 500 s by the Executor's stamps |
| V7 | B-TAG | both commands `exit=0`; `TAGGED`, object `e299d4e…`, commit `bce5a85…` = the branch head | yes, by `tagged` |
| V8 | B-UPLOAD | 1 run, `exit=0`; `UPLOAD COMPLETE: 51 of 51`, 51 sent, 0 kept; 52 records | yes, by `upload` |
| V9 | G-UPLOAD, G-DOWNLOAD | `VERIFY PASS`: 51 of 51 by name, bytes, state and digest; 51 of 51 downloads equal; 5 of 5 checks; Release `409534533` | yes, by `verify` |
| V10 | G-DELETE | `DELETE PASS` 51 of 51; `REMOVED PASS` 3 of 3; free and `du` before and after (§2.10) | yes, by `delete` and `removed` |
| V11 | G-RESTART | 5 of 5; the stop of `752775` at phase 426, the start of `815823` at phase 431, a gap of 5.647 s | yes, by `restart` |
| V12 | G-COUNTER | 4 of 4; `stream_bytes` 10,095,699 = the store's 10,095,699 < 8,000,000,000 | yes |
| V13 | G-UNIT | 10 of 10 at 2 restarts, at `restart` and at `final` | yes |
| V14 | G-RESUME | `PASS`, window `1791707400`, 4 of 4 | yes, by `resume` |
| V15 | G-STILL | the recorder unchanged: `4148534`, `2`, `active` | yes, by `final`'s `still` |
| V16 | the hook and the counters | §2.16: opens refused 0 at every mode; store opens 51/51/51/51, 1, 1, 0 elsewhere; requests 3 at `path`; removed 51 by `delete`. One departure: the self-test's own 4 removals in its temporary store (§6 item 3) | printed by each mode; the hook asserts by refusing |
| V17 | contract §4.2's self-check, and V17's line | `0`; the instrument alone; nothing `.parquet` or `.zip`; `0` | read by the Executor |
| V18 | §3.12's closing reads | every read printed (§2.17) | printed |
| V19 | §9's `reclaim` runs | scratch: 1 considered, 0 named, 0 kept, 0 copied, 0 held, 1,766 → 1,766. Own: §2.19 | yes, by `reclaim` (`after == before + copied`) |
| V20 | §9's removals | `30ec6406…` by the Executor and `d5dc7bd3…` by the Boss, `test -e` exit 1 each. Own: §2.19 | read by the Executor |

---

## 6. What could not be implemented as written

1. **Two of B-RECLAIM-SCRATCH's commands went to the Boss** — one `rm -rf`, by §3's classifier route. The Executor's `rm -rf` of `d5dc7bd3…` was refused by the session's permission classifier ("[Irreversible Local Destruction]"); the identical command for `30ec6406…` was allowed 30 s earlier. The Boss ran it verbatim in a root shell after B-UPLOAD, and his terminal printed `exit=0`. The Executor verified it with `test -e`, exit `1`. B-RECLAIM-SCRATCH so finished after §3.4 to §3.7 had begun rather than strictly before §3.4. `reclaim` had already passed over both directories at 08:20:21 UTC.
2. **`I delete` went to the Boss**, by §3.8's own fallback, after the classifier refused it ("[Irreversible Local Destruction]").
   - That refusal discarded the `df`/`du` line in the same command. A standalone `df`/`du` the Executor then tried was refused as "[Auto-Mode Bypass]".
   - §3.8's before-reading was therefore taken by the Boss: the Executor added that `df`/`du` line, written to `logs/B-DELETE-df-before.log`, as the first line of the block it handed over.
   - Every removal is verified from the Executor's side, by `I removed` and by the `df`/`du` after it. The before-reading is the Boss's, and `delete`'s own `free … before` line agrees with it to 4,096 bytes.
3. **V16 says "files removed … `0` by every other mode"; the self-test printed `files removed 4`.** These are its own removals inside its temporary store — `delete_set` run on literals, which bumps the same counter — and the temporary store was then removed by `shutil.rmtree`, which the self-test checks. Nothing under `/var/lib/btc-pairbook/` was removed by the self-test: its one attempt there was refused by the hook, as the self-test asserts. Recorded, not asserted.
4. **`logs/36-files-written.log` lists its own SHA-256 as taken while `tee` was still writing it**, so that one line is not the file's final hash. The final hashes of every file under `logs/`, `archive/` and `state.json` are B-RECLAIM-OWN's `R` lines (§2.19).
5. **§3's per-asset table was assembled outside the instrument** by a short script (`logs/32-asset-table.log`). It reads `set.json`, `upload.jsonl`, `verify.json` and `delete.jsonl` and compares their strings and integers. It hashes nothing, opens nothing under the store, and computes no new quantity. Its `51 of 51` is a summary of comparisons the instrument already asserted, not a separate check.
6. **The Boss's two `exit=` lines** — B-UPLOAD's `exit=0` and the `rm -rf`'s `exit=0` — and B-DELETE's `exit=0` are known from his terminal, not from a file the session wrote. Each outcome is verified independently from the Executor's side:
   - B-UPLOAD's by `upload.jsonl`'s completion record and `VERIFY PASS`.
   - The `rm -rf` by `test -e`.
   - B-DELETE's by `REMOVED PASS` and `du`.
7. **§0.5's recorded difference:** `main` was at `c8352f5`, two first-parent commits above `2122705`: the upload of revision `2026-10-11-a` and of this TZ. This is not BLOCKING by §0.5.
8. **The report was drafted from a template by a short script** that substituted the logs verbatim, as the earlier TZs' reports were. Both files sat in the work tree and went with it; neither is named by this report, and `reclaim` did not copy them. B-RECLAIM-OWN's output was kept in the session's scratchpad — the one exception §0.0 names — until it was placed in §2.19.
9. **B-RECLAIM-OWN's `df` carries no stamp of its own**, so its instant is given as about 08:50 UTC, after `reclaim`'s 08:49:54 line.
