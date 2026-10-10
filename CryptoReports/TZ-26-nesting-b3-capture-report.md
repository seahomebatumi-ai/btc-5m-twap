# TZ-26 report — B3's capture: the nested pair's four books, streamed

**P-START: served** — 3 requests and 1 stream session on the ETH nested pair, 7 of 7 session checks True. **The switch was made by the Boss**, because the session's classifier refused B-SWITCH. The chain book stopped at 19:30:06 UTC; the pair book started at 19:30:06 UTC as pid `746785`. **G-CB-STOP PASS**, 4 of 4.
**G-UNIT PASS** at 0 restarts (10 of 10) · **G-START PASS** (7 of 7) · **G-STREAM PASS, 4 of 4** qualifying windows complete · **G-BOOKS PASS, 28 of 28** checkpoints complete · **G-TIERC PASS**: 4 counted, fully loaded exposed intervals, each with `quotes_complete` true, and 0 failures · **G-LOAD PASS**: `0.0174` of one core, against the bound `0.25`.
**G-RESTART PASS**: the `SIGTERM` stop of `746785`, then the start of `752775` 5.480 s later; G-UNIT at 1 restart 10 of 10. **G-STILL PASS**: the recorder `4148534`, `NRestarts` 2, `active`, unchanged from 19:03:54 to 20:38:23 UTC.
**The pair book runs**, as `btc-pairbook.service`, pid `752775`, `NRestarts` 1, `active` and `enabled`. **The chain book is `inactive` and `disabled`.** This was verified by `I final` and by §3.11's `systemctl show`, `is-enabled` and `journalctl`, quoted below, not from the Boss's account.
**Two departures:** the Boss ran B-SWITCH 10 s before its band, at second 5 of the window against 15 to 420; and the Executor read the pair book's `runtime.jsonl` once with `head`, outside the instrument (§6 items 3 and 4).
**The BTC pair's measured rate**, over G-STREAM's four windows: **488.4 frames a second** — `btc-updown-15m` 214.8, `btc-updown-5m` 273.6. That is 12,755,244 stored stream bytes a window, so **6.53 days to `STREAM_CAP`**, against the 3.2 days modelled.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-26-nesting-b3-capture.md`, 3,281 lines, 186,518 bytes, SHA-256 `2f33368d63c8ffcf7906a5f9b8f6d3d03efcf17fa7ff4cb910155c204ad9db4d`, landed at `c1a59c4` |
| map revision | `2026-10-10-b`, equal; anchors 6 of 6; re-derived 4 of 4; rows 34; `frozen` equal 31 of 31 |
| executor model | Opus, as the TZ names: `get_session` read `session_context.model` and `last_served_model` as `claude-opus-5-5` |
| branch | `tz-26-nesting-b3-capture` at `e8b46a85d61e1a17841962846f6d3012046c2d70`, pushed; pull request #25, open, not merged |
| instrument | `research/tz26-nesting-b3-capture.py`, 2,492 lines, 118,466 bytes, SHA-256 `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec`, Appendix A byte for byte |
| unit | `deploy/systemd/btc-pairbook.service`, 22 lines, 761 bytes, SHA-256 `ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8`, Appendix A byte for byte; installed byte for byte as `/etc/systemd/system/btc-pairbook.service` |
| service's copy | `/root/btc-pairbook-svc/tz26-nesting-b3-capture.py`, SHA-256 `caed70d9…`; `commit.txt` `e8b46a85d61e1a17841962846f6d3012046c2d70` |
| interpreter | `/root/tz04a-env/venv/bin/python` 3.12.3 with `websockets` 17.1; every mode under `nice -n 19` and `-B` |
| requests | `prestart`: 2 ETH documents and 1 ETH book through `http_get`, and 1 stream session of 25 s on the ETH pair through `stream_window`. The unit's own requests. `git` against `origin`; `gh` for the pull request. The self-test reached `127.0.0.1` alone |
| recorder's capture | `manifest.json` only, read only: 2,016 attempted by `prestart` and 15 by each `prove` run. Outside the instrument, only §0.3's `df`, `find` and `grep -c`, at both runs, and B-RECLAIM-OWN's `df` |
| chain book | `runtime.jsonl` once, by `chainbook`, read only; §0.3's `test -d` at both runs. Nothing else under its root |
| pair book | read by the modes `prove`, `load`, `unit`, `restart` and `final` alone. Outside the instrument: §3.11's `tail` of `service.log` and `du`, and **one departure**, a `head -c 2000` of `runtime.jsonl` (§6 item 4) |
| pricer | not read, not called, not scored; `A6` `729f0bcdbee3` is stated so that what was not scored is not in doubt |

This report prints no price, size, side, book hash or outcome. Every figure below is a count, a time, a status, a token count or a SHA-256, copied from the instrument's own output. The one exception is §2.10's rate, which a short script derived from the proof file's counts (§6 item 7).

---

## 0. Fingerprint

Contract §1 steps 3 and 4 ran inside the instrument, as `I0 fingerprint` (§0.2), which asserts each step. Results:

- **Revision and anchors:** the map revision string `2026-10-10-b` and the six anchors of the TZ header were read, all equal.
- **Re-derived anchors:** `A2`, `A4`, `A5` and `A6` were re-derived as the first 12 hex characters of their files' SHA-256, 4 of 4 equal.
- **Table rows:** the table's 34 rows were hashed. Of these, 31 are `frozen`, each equal to the map in lines, bytes and SHA-256; 2 are `tracked`; 1 is `reported`.
- **`SYSTEM-MAP.md`:** 1,285 lines, 279,771 bytes, SHA-256 `c285fa45027ce65cfdb83939340ec53b129fe10cc5275dd0e129e4fbde615532`.

| anchor | required | read |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` |
| `A2` — collector | `6c5089330629` | `6c5089330629`, re-derived from `research/twap-divergence.py` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | equal |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b`, re-derived from `BTC-EXECUTOR-INSTRUCTIONS.md` |
| `A5` — recorder | `0f6c90451cbd` | `0f6c90451cbd`, re-derived from `research/recorder/recorder.py` |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3`, re-derived from `research/pfair.py` |

### 0.1 The 34 rows of the map's §0 table, and the map (V1) — `logs/02-fingerprint.log`, verbatim

`logs/02-fingerprint.log`:

```text
2026-10-10T19:02:59.721699347Z
[2026-10-10T19:02:59Z] re-derived A2 research/twap-divergence.py sha256[:12] 6c5089330629 equal
[2026-10-10T19:02:59Z] re-derived A4 BTC-EXECUTOR-INSTRUCTIONS.md sha256[:12] 437b45ea196b equal
[2026-10-10T19:02:59Z] re-derived A5 research/recorder/recorder.py sha256[:12] 0f6c90451cbd equal
[2026-10-10T19:02:59Z] re-derived A6 research/pfair.py sha256[:12] 729f0bcdbee3 equal
[2026-10-10T19:02:59Z] SYSTEM-MAP.md                                  1285 lines   279771 bytes c285fa45027ce65cfdb83939340ec53b129fe10cc5275dd0e129e4fbde615532 reported
[2026-10-10T19:02:59Z] BTC-EXECUTOR-INSTRUCTIONS.md                    234 lines    11128 bytes 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b frozen equal
[2026-10-10T19:02:59Z] research/twap-divergence.py                    1135 lines    50928 bytes 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 frozen equal
[2026-10-10T19:02:59Z] research/selftest-twap-divergence.py            376 lines    16736 bytes ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a frozen equal
[2026-10-10T19:02:59Z] research/tz02-distribution.py                   334 lines    14511 bytes f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 tracked
[2026-10-10T19:02:59Z] research/pfair.py                               441 lines    19357 bytes 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 frozen equal
[2026-10-10T19:02:59Z] research/selftest-pfair.py                      619 lines    32559 bytes b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa frozen equal
[2026-10-10T19:02:59Z] research/tz06-calibration.py                    577 lines    27138 bytes 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f frozen equal
[2026-10-10T19:02:59Z] research/tz07a-variance-time.py                 623 lines    28414 bytes 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 frozen equal
[2026-10-10T19:02:59Z] research/tz07b-settlement-dispersion.py         515 lines    24926 bytes 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc frozen equal
[2026-10-10T19:02:59Z] research/tz08a-out-of-sample.py                 745 lines    38822 bytes 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c frozen equal
[2026-10-10T19:02:59Z] research/tz09-disk-inventory.py                 894 lines    41004 bytes b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 frozen equal
[2026-10-10T19:02:59Z] research/tz10b-sigma-or-link.py                1224 lines    61018 bytes 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 frozen equal
[2026-10-10T19:02:59Z] research/tz11a-student-link.py                 1231 lines    64732 bytes 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 frozen equal
[2026-10-10T19:02:59Z] research/tz12-sized-gate.py                    1157 lines    61637 bytes d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 frozen equal
[2026-10-10T19:02:59Z] research/tz13-sized-gate-test3.py              1074 lines    53901 bytes a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd frozen equal
[2026-10-10T19:02:59Z] research/tz14-quote-inventory.py               2124 lines   109972 bytes 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 frozen equal
[2026-10-10T19:02:59Z] research/tz15-phase2-gate.py                   1517 lines    73799 bytes 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 frozen equal
[2026-10-10T19:02:59Z] research/tz16a-phase2-decisive-gate.py         2198 lines   111192 bytes 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 frozen equal
[2026-10-10T19:02:59Z] research/tz17-settlement-chain.py              1102 lines    38622 bytes e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 frozen equal
[2026-10-10T19:02:59Z] research/tz18a-chainbook-capture.py            1683 lines    69517 bytes e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae frozen equal
[2026-10-10T19:02:59Z] research/tz20-capture-under-systemd.py          771 lines    36528 bytes 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7 frozen equal
[2026-10-10T19:02:59Z] research/tz21-recorder-memory.py               1284 lines    59009 bytes d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f frozen equal
[2026-10-10T19:02:59Z] research/tz23-maker-m0.py                      1184 lines    54885 bytes 6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f frozen equal
[2026-10-10T19:02:59Z] research/tz24-nesting-b2.py                    1535 lines    76142 bytes 4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b frozen equal
[2026-10-10T19:02:59Z] research/recorder/recorder.py                   651 lines    27821 bytes 0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7 frozen equal
[2026-10-10T19:02:59Z] research/recorder/config.py                     112 lines     4773 bytes 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d frozen equal
[2026-10-10T19:02:59Z] research/recorder/manifest.py                   254 lines    10002 bytes 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 frozen equal
[2026-10-10T19:02:59Z] research/recorder/analyze.py                    813 lines    34705 bytes eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d frozen equal
[2026-10-10T19:02:59Z] research/recorder/probe.py                      227 lines     9324 bytes 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 frozen equal
[2026-10-10T19:02:59Z] research/recorder/selftest.py                   573 lines    30591 bytes c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 frozen equal
[2026-10-10T19:02:59Z] deploy/systemd/btc-recorder.service              23 lines      707 bytes 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1 frozen equal
[2026-10-10T19:02:59Z] deploy/systemd/btc-chainbook.service             22 lines      724 bytes a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2 frozen equal
[2026-10-10T19:02:59Z] .gitignore                                        5 lines      252 bytes 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b tracked
[2026-10-10T19:02:59Z] SYSTEM-MAP.md 1285 lines 279771 bytes sha256 c285fa45027ce65cfdb83939340ec53b129fe10cc5275dd0e129e4fbde615532
[2026-10-10T19:02:59Z] FINGERPRINT PASS: revision 2026-10-10-b; anchors 6 of 6, 4 re-derived; rows 34: frozen 31 of 31 equal, tracked 2, reported 1
[2026-10-10T19:02:59Z] peak memory of this run: 36405248 bytes
[2026-10-10T19:02:59Z] opens refused: 0; manifest opens attempted 0; chain book opens 0; requests 0, stream sessions 0
exit=0
```

### 0.2 §0.0 and §0.1 — the work tree, and the instrument staged

Contract §1 steps 1 and 2 came first: `git pull` of `main`, then reading the TZ and the map in full. `main` was at `73da754`. §0.0's `mkdir` then printed `exit=0`.

`logs/00-workdir.log`:

```text
2026-10-10T19:02:40.932582304Z
exit=0
```

`logs/00-pull.log`:

```text
2026-10-10T19:02:45.501372671Z
73da7541bbaa52acfaee9ba86a0520e040110763
73da7541bbaa52acfaee9ba86a0520e040110763
73da7541bbaa52acfaee9ba86a0520e040110763 2026-10-10 22:55:38 +0400 Update SYSTEM-MAP.md
c1a59c47af84507203119ad8fbf6d92831e2ed64 2026-10-10 22:47:40 +0400 Add files via upload
11a01799ceb43fe050603caf1a19233c59b68a55 2026-10-10 13:48:35 +0400 Merge pull request #24 from seahomebatumi-ai/tz-24-nesting-b2
```

§0.1's script, verbatim, with destination `/root/tz26-work/stage`: 2 of 2 hashes asserted, with lines and bytes equal to the TZ's table (V3).

`logs/01-stage.log`:

```text
2026-10-10T19:02:52.788405323Z
/root/tz26-work/stage/deploy/systemd/btc-pairbook.service 22 761 ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8
/root/tz26-work/stage/research/tz26-nesting-b3-capture.py 2492 118466 caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec
exit=0
```

### 0.3 Host gate — the opening reads, verbatim (V2)

`logs/03-host-gate.log`:

```text
Sat Oct 10 07:03:07 PM UTC 2026
1791658987
1
MemTotal:         978640 kB
MemAvailable:     240196 kB
SwapTotal:       3174396 kB
SwapFree:        2840820 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12992323584
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
1
chainbook exit=0
active
active
exit=0
enabled
enabled
exit=0
pairbook unit exit=1
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
/root/tz24-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=1
/var/lib/btc-pairbook exit=1
1725
3.12.3 17.1
/root/btc-5m-twap       73da754 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
195469323	/root/.claude
528513598	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/30ec6406-6385-5122-88dc-9ad61b1f2846/scratchpad
total 24
drwx------  6 root root 4096 Oct 10 18:59 .
drwx------ 16 root root 4096 Oct 10 18:59 ..
drwx------  4 root root 4096 Oct 10 19:01 30ec6406-6385-5122-88dc-9ad61b1f2846
drwx------  4 root root 4096 Oct 10 08:27 5c15abf7-532c-5a8a-9dfa-19c904ad993e
drwx------  3 root root 4096 Oct 10 08:27 65948b60-83f3-4efd-93cf-43514331137a
drwx------  3 root root 4096 Oct 10 18:59 d5dc7bd3-91ab-4f86-bdfc-8d305cb318f9
```

The seven blocking conditions, each read from the block above:

- **H1:** `find` printed exactly one path.
- **H2:** `/dev/vda2`, `31612203008`; `grep -c` `1`.
- **H3:** `3.12.3 17.1`.
- **H4:** `chainbook exit=0`; both units `active`, then `enabled`, `exit=0` at both reads.
- **H5:** `pairbook unit exit=1`; `/root/btc-pairbook-svc` and `/var/lib/btc-pairbook` both `exit=1`.
- **Memory gate:** `MemAvailable` 240,196 kB = `245,960,704` bytes ≥ `107,503,616`.
- **Disk gate:** avail `12,992,323,584` ≥ `5,100,000,000`.

**7 of 7 PASS.**

Printed with no threshold:

- `telemetry-watch.service` read `disabled` (exit 1) and `inactive` (exit 3).
- The recorder's tree is at `e3975b5…`.
- `/root/tz24-work` is absent; `/root/tz18a-svc` and `/root/btc-recorder-svc` are present.
- The forensic store holds `1,725` files, map §3's count.
- Two worktrees.
- `du`: `/root/.claude` `195,469,323`, `/root/PROJECT_GAMING_PS5` `528,513,598`.
- The session directories, which §2.3 below classifies.

### 0.4 Free space and `MemAvailable` — every read, its instant and its bound

| instant (UTC) | read by | free bytes on `/dev/vda2` | `MemAvailable` | bound |
|---|---|---|---|---|
| 19:03:07 | §0.3 host gate | `12,992,323,584` | `245,960,704` | disk `5,100,000,000`; memory `107,503,616` |
| 19:04:18 | `prestart` | `12,985,643,008` (at `/var/lib`) | `277,786,624` | memory `107,503,616` |
| 19:30:06 | the service's first `start` record | `12,985,090,048` | — | the stream floor `4,500,000,000` |
| 20:37:09 | `prove`, first run | — | `258,142,208` | memory `107,503,616` |
| 20:37:25 | `prove`, same `A` | — | `261,963,776` | memory `107,503,616` |
| 20:37:49 | the service's second `start` record | `12,931,923,968` | — | the stream floor `4,500,000,000` |
| 20:38:35 | §3.11, §0.3's block again | `12,931,727,360` | `248,877,056` (243,044 kB) | printed |
| about 20:38:36 | §3.11 `free -b` | — | available `286,482,432` | printed |
| 20:41:59 | B-RECLAIM-OWN's `df` | `12,931,072,000` | — | printed |


### 0.5 Refs (§0.5) — `logs/04-refs.log`, verbatim

`logs/04-refs.log`:

```text
2026-10-10T19:03:14.515976861Z
73da7541bbaa52acfaee9ba86a0520e040110763	HEAD
73da7541bbaa52acfaee9ba86a0520e040110763	refs/heads/main
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8	refs/heads/tz-23-maker-m0
6f045cffc3601b589d3b8b7a6a9af6f73991e18b	refs/heads/tz-24-nesting-b2
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
ee2f6327390ef4d0c6169d1fba1a2ed4ae936dc3	refs/pull/3/head
0e13a5c76dfa2469ff25b3b0dd282872decf6f25	refs/pull/4/head
4216c04673ced76b5b2ac60ef57c9abedc46f9b9	refs/pull/5/head
5ed667afd1b53f036b9f938fcce13c0d709cd77f	refs/pull/6/head
c44af687203d14d5d485d4297c04cfb827096af9	refs/pull/7/head
26bbb61aed774a88355dd5204d8b69fda9135a68	refs/pull/8/head
e2625ea2b5473c311d59a48f32540ce39d58e591	refs/pull/9/head
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
ref lines: 30
--- first-parent above 11a0179
73da7541bbaa52acfaee9ba86a0520e040110763 2026-10-10 22:55:38 +0400 Update SYSTEM-MAP.md
c1a59c47af84507203119ad8fbf6d92831e2ed64 2026-10-10 22:47:40 +0400 Add files via upload
== 73da7541bbaa52acfaee9ba86a0520e040110763
M	SYSTEM-MAP.md
== c1a59c47af84507203119ad8fbf6d92831e2ed64
A	CryptoTZ/TZ-26-nesting-b3-capture.md
--- revision on main
**Revision 2026-10-10-b.** Written by the Architect; the Executor never edits it. This is a
tz-26 branch lines: 0
```

**30 ref lines**, as map §1 records. `refs/heads/tz-23-maker-m0` is at `7f5ae3f` and `refs/heads/tz-24-nesting-b2` at `6f045cf`, as recorded.

**One difference, recorded and not blocking:** `main` is at `73da7541…`, not `11a0179`. The upload above `11a0179` is two first-parent commits:

- `c1a59c4` added `CryptoTZ/TZ-26-nesting-b3-capture.md`.
- `73da754` modified `SYSTEM-MAP.md`, and carries revision `2026-10-10-b`.

`refs/heads/tz-26-nesting-b3-capture` did not exist (0 lines).

---

## 1. Input

| input | read |
|---|---|
| `CryptoTZ/TZ-26-nesting-b3-capture.md` | in full; Appendix A extracted by §0.1's script, twice |
| `SYSTEM-MAP.md` and the 33 files of its §0 table | by `I0 fingerprint` |
| `/var/lib/btc-recorder/**/manifest.json` | by `prestart` (2,016 attempted, 1,864 read) and by each of the two `prove` runs (15 each), read only |
| `/var/lib/btc-chainbook/runtime.jsonl` | by `chainbook`, once, read only |
| `/var/lib/btc-pairbook/**` | by `prove` (×2), `load`, `unit 0`, `restart` and `final`; §3.11's `tail` and `du`; the departure of §6 item 4 |
| the venue | `prestart`: 2 ETH documents, 1 ETH book, 1 ETH stream session of 25 s. Everything else the unit's own |
| `CryptoReports/*.md` | by `reclaim`, for hash tokens |

Nothing was re-collected. No dataset was read.

---

## 2. Measurements

### 2.1 §3.1 — the branch and its two files (V3)

`logs/05-branch.log`:

```text
2026-10-10T19:03:25.765086697Z
exit=0
Preparing worktree (new branch 'tz-26-nesting-b3-capture')
branch 'tz-26-nesting-b3-capture' set up to track 'origin/main'.
HEAD is now at 73da754 Update SYSTEM-MAP.md
exit=0
/root/tz26-work/wt/deploy/systemd/btc-pairbook.service 22 761 ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8
/root/tz26-work/wt/research/tz26-nesting-b3-capture.py 2492 118466 caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec
exit=0
?? deploy/systemd/btc-pairbook.service
?? research/tz26-nesting-b3-capture.py
```

`logs/06-commit-push.log`:

```text
2026-10-10T19:03:33.128892938Z
commit exit=0
e8b46a85d61e1a17841962846f6d3012046c2d70
A	deploy/systemd/btc-pairbook.service
A	research/tz26-nesting-b3-capture.py
remote: 
remote: Create a pull request for 'tz-26-nesting-b3-capture' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-26-nesting-b3-capture        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-26-nesting-b3-capture -> tz-26-nesting-b3-capture
branch 'tz-26-nesting-b3-capture' set up to track 'origin/tz-26-nesting-b3-capture'.
push exit=0
e8b46a85d61e1a17841962846f6d3012046c2d70
## tz-26-nesting-b3-capture...origin/tz-26-nesting-b3-capture
```

`logs/07-pr.log`:

```text
2026-10-10T19:03:41.290643272Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/25
exit=0
```

The second extraction printed the same lines, bytes and SHA-256 as §0.1. The branch's diff against `origin/main` names exactly the two paths, both `A` (§3 below).

### 2.2 §3.2 — the self-test (V4): **74 of 74**

`logs/08-selftest.log`:

```text
2026-10-10T19:03:46.409459153Z
[2026-10-10T19:03:46Z]   ok  documents at T+545, the stream T+595 to T+905, window.json at T+910
[2026-10-10T19:03:46Z]   ok  the chain book's seven checkpoints, tau' 245 to 15
[2026-10-10T19:03:46Z]   ok  Tier C reads the same five-minute market 5 s after each checkpoint, never in its second
[2026-10-10T19:03:46Z]   ok  the stream covers the five-minute market's whole window; the documents precede the recorder's S6 at T+605
[2026-10-10T19:03:46Z]   ok  next_window: scheduled to T+545, joined late to T+880, then the next window
[2026-10-10T19:03:46Z]   ok  the stream opens only with both documents, free at or above the floor, the store below the cap
[2026-10-10T19:03:46Z]   ok  same_service: the exact argv
[2026-10-10T19:03:46Z]   ok  same_service: a shell carrying the argv as text is not the service
[2026-10-10T19:03:46Z]   ok  same_service: a sixth field, and nothing, are not the service
[2026-10-10T19:03:46Z]   ok  serve writes under the pair book's root
[2026-10-10T19:03:46Z]   ok  serve writes nowhere else
[2026-10-10T19:03:46Z]   ok  serve starts no process; the systemd reads may
[2026-10-10T19:03:46Z]   ok  under the recorder's root only a manifest, read only, by prestart and prove
[2026-10-10T19:03:46Z]   ok  no manifest is opened for writing, and the recorder's root is never listed
[2026-10-10T19:03:46Z]   ok  under the chain book's root only its runtime.jsonl, by chainbook; nothing listed
[2026-10-10T19:03:46Z]   ok  the pair book's root is written by serve alone and read by the modes that judge it
[2026-10-10T19:03:46Z]   ok  the forensic store takes new files by exclusive create alone
[2026-10-10T19:03:46Z]   ok  the hook refuses /var/lib/btc-recorder/runtime.jsonl before it is opened
[2026-10-10T19:03:46Z]   ok  the hook refuses /var/lib/btc-chainbook/runtime.jsonl before it is opened
[2026-10-10T19:03:46Z]   ok  the hook refuses /var/lib/btc-pairbook/runtime.jsonl before it is opened
[2026-10-10T19:03:46Z]   proxy variables removed: 0
[2026-10-10T19:03:46Z]   ok  build_request: GET, Accept and this file's User-Agent
[2026-10-10T19:03:46Z]   ok  the wire: exactly five header fields
[2026-10-10T19:03:46Z]   ok  http_get records 200, 2 bytes, the body's SHA-256 and both stamps
[2026-10-10T19:03:46Z]   ok  a refusal is a stored reply with its status
[2026-10-10T19:03:47Z]   ok  no reply: no status and no receive stamp
[2026-10-10T19:03:47Z]   ok  three loopback requests counted
[2026-10-10T19:03:47Z]   ok  skew over the replies that came
[2026-10-10T19:03:47Z]   ok  a checkpoint: four replies within one second
[2026-10-10T19:03:47Z]   ok  token_ids_of: two distinct ids from the JSON-in-JSON fields, or none
[2026-10-10T19:03:48Z]   ok  a close by the venue, then one reconnect
[2026-10-10T19:03:48Z]   ok  the subscription: the documented frame, compact
[2026-10-10T19:03:48Z]   ok  the handshake: six header fields, this file's User-Agent, no extension offered
[2026-10-10T19:03:48Z]   ok  the heartbeat: PING on its period, PONG stored
[2026-10-10T19:03:48Z]   ok  the file: connect, open, subscribe, frames, close, the same again, end
[2026-10-10T19:03:48Z]   ok  the venue's close is recorded with its code, the window's end as end
[2026-10-10T19:03:48Z]   ok  every frame a line of recv_ns, mono_ns and the frame verbatim; the first the four books
[2026-10-10T19:03:48Z]   ok  the unit reads the stream back: every frame conforms, both markets, both sessions
[2026-10-10T19:03:48Z]   ok  a stream that ends before its window's T+900 reads short
[2026-10-10T19:03:49Z]   ok  a stop closes the session at once and the file whole
[2026-10-10T19:03:49Z]   ok  a file cut after a sync flush reads to it, torn
[2026-10-10T19:03:49Z]   ok  the whole file: 60 frames and the end line
[2026-10-10T19:03:49Z]   ok  a file cut mid-block is torn, read to its last whole line
[2026-10-10T19:03:49Z]   ok  bytes past the trailer read torn
[2026-10-10T19:03:49Z]   ok  the window maximum cuts the stream
[2026-10-10T19:03:49Z]   ok  a binary frame is stored as base64, verbatim
[2026-10-10T19:03:49Z]   ok  the first stream file of a window
[2026-10-10T19:03:49Z]   ok  a second process writes the next name
[2026-10-10T19:03:49Z]   ok  a directory without window.json or books is joinable
[2026-10-10T19:03:49Z]   ok  a directory holding books is not rejoined
[2026-10-10T19:03:49Z]   ok  a window streamed from T+595 to T+905: complete, its largest gap 1 s
[2026-10-10T19:03:49Z]   ok  a subscription after T+600 reads late subscribe, and nothing else
[2026-10-10T19:03:49Z]   ok  no book of the four tokens within 5 s of it reads initial books
[2026-10-10T19:03:49Z]   ok  18 s without a frame reads gap
[2026-10-10T19:03:49Z]   ok  a file without its end line and its close reads so
[2026-10-10T19:03:49Z]   ok  a stream whose last close is before T+900 reads short
[2026-10-10T19:03:49Z]   ok  an undocumented event type, a token not subscribed and a count off its window.json are named
[2026-10-10T19:03:49Z]   ok  a window joined late is no unit
[2026-10-10T19:03:49Z]   ok  a window without both documents is no unit
[2026-10-10T19:03:49Z]   ok  a window whose stream did not open names why
[2026-10-10T19:03:49Z]   ok  frame_tokens: the four documented types and their token ids, nothing else
[2026-10-10T19:03:49Z]   ok  a forbidden key at any depth fails the allow-list
[2026-10-10T19:03:49Z]   ok  no allowed key is a forbidden one
[2026-10-10T19:03:49Z]   ok  G-STREAM: 4 and 3 of 4, 2 of 4, fewer than 4
[2026-10-10T19:03:49Z]   ok  G-BOOKS: 26 of 28, 25 of 28, fewer than 28
[2026-10-10T19:03:49Z]   ok  G-TIERC: two loaded, any failure, too few loaded
[2026-10-10T19:03:49Z]   ok  G-STREAM's false failure at 1 in 100
[2026-10-10T19:03:49Z]   ok  G-STREAM's power at 1 in 4 and 1 in 2
[2026-10-10T19:03:49Z]   ok  G-BOOKS' false failure at 1 in 100
[2026-10-10T19:03:49Z]   ok  G-BOOKS' power at 1 in 4 and 1 in 10
[2026-10-10T19:03:49Z]   ok  G-TIERC's false alarm, exact
[2026-10-10T19:03:49Z]   ok  decimals: half up
[2026-10-10T19:03:49Z]   ok  imports: the standard library and websockets
[2026-10-10T19:03:49Z]   ok  exactly three endpoints in the file's text
[2026-10-10T19:03:49Z]   ok  websockets 17.1, the recorder's
[2026-10-10T19:03:49Z] 74 of 74 checks passed
[2026-10-10T19:03:49Z] peak memory of this run: 53510144 bytes
[2026-10-10T19:03:49Z] opens refused: 0; manifest opens attempted 0; chain book opens 0; requests 3, stream sessions 3
exit=0
```

### 2.3 §3.3 — the units, and the directories beside this session

`logs/09-still.log`:

```text
2026-10-10T19:03:54.761391267Z
[2026-10-10T19:03:54Z] btc-chainbook.service {'MainPID': '4064090', 'NRestarts': '1', 'ActiveState': 'active'}, MemoryCurrent 6508544, MemoryPeak 18735104
[2026-10-10T19:03:54Z] btc-pairbook.service {'MainPID': '0', 'NRestarts': '0', 'ActiveState': 'inactive'}, MemoryCurrent [not set], MemoryPeak [not set]
[2026-10-10T19:03:54Z] btc-recorder.service {'MainPID': '4148534', 'NRestarts': '2', 'ActiveState': 'active'}, MemoryCurrent 129949696, MemoryPeak 200912896
[2026-10-10T19:03:54Z] still: the recorder recorded
[2026-10-10T19:03:54Z] peak memory of this run: 35483648 bytes
[2026-10-10T19:03:54Z] opens refused: 0; manifest opens attempted 0; chain book opens 0; requests 0, stream sessions 0
exit=0
```

`logs/10-scratch.log`:

```text
2026-10-10T19:03:54.916003533Z
[2026-10-10T19:03:55Z] running 337573 started 2026-10-07T20:05:37Z claude
[2026-10-10T19:03:55Z] running 337576 started 2026-10-07T20:05:37Z claude
[2026-10-10T19:03:55Z] running 743341 started 2026-10-10T18:59:36Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-10-10T19:03:55Z] 5c15abf7-532c-5a8a-9dfa-19c904ad993e born 2026-10-10T08:27:50Z: earlier
[2026-10-10T19:03:55Z] 65948b60-83f3-4efd-93cf-43514331137a born 2026-10-10T08:27:48Z: earlier
[2026-10-10T19:03:55Z] d5dc7bd3-91ab-4f86-bdfc-8d305cb318f9 born 2026-10-10T18:59:37Z: live, process [743341]
[2026-10-10T19:03:55Z] peak memory of this run: 35487744 bytes
[2026-10-10T19:03:55Z] opens refused: 0; manifest opens attempted 0; chain book opens 0; requests 0, stream sessions 0
exit=0
```

Three directories sit beside this session's own, `30ec6406-6385-5122-88dc-9ad61b1f2846`:

- `5c15abf7…` and `65948b60…` — TZ-24's pair, which map §3 names. **Earlier.**
- `d5dc7bd3…` — born 1 s after this session's process `743341` started. **Live**, and kept.

### 2.4 §9 B-RECLAIM-SCRATCH — after §3.3, before §3.4 (V18, V19)

One `I reclaim` named both earlier directories, as map §7 item 102 requires. It printed `RECLAIM PASS`: 0 files considered, store `1,725 -> 1,725`. Then one `rm -rf` and one `test -e` per directory. **None was refused by the classifier.**

`logs/11-reclaim-scratch.log`:

```text
2026-10-10T19:04:04.132575907Z
[2026-10-10T19:04:04Z] reclaim: 1993 report tokens; forensic store holds 1725 files
[2026-10-10T19:04:04Z] RECLAIM PASS: 0 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 1725 -> 1725 files
[2026-10-10T19:04:04Z] peak memory of this run: 37335040 bytes
[2026-10-10T19:04:04Z] opens refused: 0; manifest opens attempted 0; chain book opens 0; requests 0, stream sessions 0
exit=0
```

`logs/12-rm-scratch.log`:

```text
2026-10-10T19:04:09.521630178Z
exit=0
exit=1
2026-10-10T19:04:09.552676273Z
exit=0
exit=1
```

### 2.5 §3.4 — the service's copy (V5)

`logs/13-svc-copy.log`:

```text
2026-10-10T19:04:13.972258899Z
exit=0
caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec  /root/btc-pairbook-svc/tz26-nesting-b3-capture.py
caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec  /root/tz26-work/wt/research/tz26-nesting-b3-capture.py
e8b46a85d61e1a17841962846f6d3012046c2d70
e8b46a85d61e1a17841962846f6d3012046c2d70
```

- `mkdir` printed `exit=0`.
- Both hashes are `caed70d9…`, Appendix A's (2 of 2).
- `commit.txt` holds the 40 hex characters `e8b46a85…` and a newline (41 bytes, SHA-256 `1d683c6a5b1c87648587df5a1777c96c8bcd478d2e0aa4805857234a3e702ffe`), equal to the worktree's `HEAD`.

### 2.6 §3.5 — P-START (V6): **served**

`logs/14-prestart.log`:

```text
2026-10-10T19:04:18.537711030Z
[2026-10-10T19:04:18Z] MemAvailable 277786624 bytes, floor 107503616
[2026-10-10T19:04:18Z] file /root/btc-pairbook-svc/tz26-nesting-b3-capture.py sha256 caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec
[2026-10-10T19:04:18Z] free 12985643008 bytes at /var/lib; proxy variables in the environment: 0
[2026-10-10T19:04:18Z] processes: the service's argv [], the chain book's [4064090]
[2026-10-10T19:04:19Z] base rate: 2016 slots, 1864 manifests read, 1 without quotes_complete true; G-TIERC's false alarm 1 - (1 - f/m)^4 = 25885002655/12072122454016 = 0.0021441965
[2026-10-10T19:04:46Z] P-START one session    True
[2026-10-10T19:04:46Z] P-START 101            True
[2026-10-10T19:04:46Z] P-START subscribed     True
[2026-10-10T19:04:46Z] P-START initial books  True
[2026-10-10T19:04:46Z] P-START heartbeat      True
[2026-10-10T19:04:46Z] P-START conforming     True
[2026-10-10T19:04:46Z] P-START whole file     True
[2026-10-10T19:04:46Z] the session: 3447 frames, 2139428 frame bytes, 2 pongs, 2 pings, 274856 stored bytes, largest gap 2011740852 ns, frames m15 3443 m5 1
[2026-10-10T19:04:46Z] wrote /root/tz26-work/prestart/prestart.json sha256 02b252af1411143a0baf85096a1c5ddb9d12034192f3caf323062f9e551e9d85
[2026-10-10T19:04:46Z] wrote /root/tz26-work/prestart/stream.jsonl.gz sha256 b1cd8024d3ac3214637fcf3528618f1286b85a8b4118a47bf0a7c1428babfa9d, 274856 bytes
[2026-10-10T19:04:46Z] READING P-START: served
[2026-10-10T19:04:46Z] peak memory of this run: 43307008 bytes
[2026-10-10T19:04:46Z] opens refused: 0; manifest opens attempted 2016; chain book opens 0; requests 3, stream sessions 1
exit=0
2026-10-10T19:04:46.711947581Z
1791659086
```

- **Requests:** 3 requests, 1 stream session, and 7 of 7 session checks `True`.
- **Processes:** no process ran under the service's argv; the chain book ran as `4064090`.
- **G-TIERC's base rate:** of the 2,016 slots in the week before, `m` = **1,864** manifests were read. `f` = **1** of them lacks a true `quotes_complete`. The false alarm is `1 − (1 − f/m)^4` = `25885002655/12072122454016` = **`0.0021441965`**.
  - The 152 slots without a manifest are the ones closing before the recorder's restart of 2026-10-04 07:39 UTC that fall inside the week (map §2.3).

**Family-wise false failure:** at most `0.0033091519 + 0.0021441965 = 0.0054533484`.

P-START exited at 19:04:46 UTC, epoch `1791659086`.

### 2.7 §3.6 — B-INSTALL (V7)

`logs/15-install.log`:

```text
2026-10-10T19:04:55.730112180Z
exit=0
exit=0
exit=0
exit=0
exit=0
```

Both `install` runs, `cmp`, `daemon-reload` and `systemd-analyze verify` exited `0`, and `verify` printed no finding. The root `/var/lib/btc-pairbook` was created empty before the first start.

### 2.8 §3.7 — the switch, G-CB-STOP, G-UNIT and G-START (V8, V9)

**Marks**, each the Executor's and each in its own command, taken before the block was run or handed over:

`logs/16-mark-stop-cb.log`:

```text
2026-10-10T19:05:01.197102339Z
[2026-10-10T19:05:01Z] mark stop-cb at 2026-10-10T19:05:01Z: btc-chainbook.service {'ns': 1791659101328741066, 'unit': 'btc-chainbook.service', 'MainPID': '4064090', 'NRestarts': '1', 'ActiveState': 'active'}
[2026-10-10T19:05:01Z] peak memory of this run: 35356672 bytes
[2026-10-10T19:05:01Z] opens refused: 0; manifest opens attempted 0; chain book opens 0; requests 0, stream sessions 0
exit=0
```

`logs/17-mark-start-svc.log`:

```text
2026-10-10T19:05:01.371203424Z
[2026-10-10T19:05:01Z] mark start-svc at 2026-10-10T19:05:01Z: btc-pairbook.service {'ns': 1791659101493317797, 'unit': 'btc-pairbook.service', 'MainPID': '0', 'NRestarts': '0', 'ActiveState': 'inactive'}
[2026-10-10T19:05:01Z] peak memory of this run: 35356672 bytes
[2026-10-10T19:05:01Z] opens refused: 0; manifest opens attempted 0; chain book opens 0; requests 0, stream sessions 0
exit=0
```

**B-SWITCH was refused by the session's permission classifier**, as "[Production Deploy]", at 19:05:2x UTC, at second 316 to 326 of the window. The whole command was refused, so neither line ran. The unit states were read right after:

`logs/18-switch-refused.log`:

```text
2026-10-10T19:05:26.524733965Z
B-SWITCH refused by the session's permission classifier: [Production Deploy]; handed to the Boss
phase=326
active
inactive
exit=0
enabled
disabled
exit=0
```

**The Boss ran the block verbatim in a root shell on the VPS.** By the journal, the stop began at 19:30:05.838 UTC, the chain book was deactivated at 19:30:06.269, and the pair book started at 19:30:06.597. That is 1,519 s after P-START's exit, inside the 3,600 s, so no `prestart-2` was needed.

**The block ran at second 5 of window `1791660600`, against the band of 15 to 420** (§6 item 3). The Executor verified the outcome from the journal, `systemctl` and the instrument, not from the Boss's account:

`logs/19-switch-boss.log`:

```text
2026-10-10T19:30:39.044132866Z
B-SWITCH run by the Boss in a root shell on the VPS; his output, verbatim:
root@vultr:~# systemctl disable --now btc-chainbook.service; echo "exit=$?"
systemctl enable --now btc-pairbook.service; echo "exit=$?" 
Removed "/etc/systemd/system/multi-user.target.wants/btc-chainbook.service".
exit=0
Created symlink /etc/systemd/system/multi-user.target.wants/btc-pairbook.service → /etc/systemd/system/btc-pairbook.service.
exit=0
phase_now=39
2026-10-10T19:30:05.838122+00:00 vultr systemd[1]: Stopping btc-chainbook.service - btc-5m-twap chain book, fifteen-minute and five-minute books...
2026-10-10T19:30:06.269149+00:00 vultr systemd[1]: btc-chainbook.service: Deactivated successfully.
2026-10-10T19:30:06.269315+00:00 vultr systemd[1]: Stopped btc-chainbook.service - btc-5m-twap chain book, fifteen-minute and five-minute books.
2026-10-10T19:30:06.269718+00:00 vultr systemd[1]: btc-chainbook.service: Consumed 1min 19.672s CPU time, 17.8M memory peak, 17.4M memory swap peak.
2026-10-10T19:30:06.596681+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
```

**G-CB-STOP** ran 57 s after the block, against at least 30 s required:

`logs/20-chainbook.log`:

```text
2026-10-10T19:31:03.161281006Z
[2026-10-10T19:31:03Z] chain book: is-active inactive, is-enabled disabled, processes []; 8 runtime records, the last stop of pid 4064090 at 2026-10-10T19:30:06Z, 6 s into its window, inside its idle stretch
[2026-10-10T19:31:03Z] G-CB-STOP inactive     True
[2026-10-10T19:31:03Z] G-CB-STOP disabled     True
[2026-10-10T19:31:03Z] G-CB-STOP no process   True
[2026-10-10T19:31:03Z] G-CB-STOP stop record  True
[2026-10-10T19:31:03Z] G-CB-STOP PASS: stopped at 2026-10-10T19:30:06Z, its MainPID 4064090, the mark at 2026-10-10T19:05:01Z
[2026-10-10T19:31:03Z] peak memory of this run: 35491840 bytes
[2026-10-10T19:31:03Z] opens refused: 0; manifest opens attempted 0; chain book opens 1; requests 0, stream sessions 0
exit=0
```

4 of 4 checks. The stop fell **6 s into its window**, which the instrument reads as **inside its idle stretch**.

**G-UNIT and G-START** ran 68 s after the block, against at least 60 s required:

`logs/21-unit0.log`:

```text
2026-10-10T19:31:14.157214276Z
[2026-10-10T19:31:14Z] G-START: the start record of pid 746785 at 2026-10-10T19:30:06Z, commit e8b46a85d61e1a17841962846f6d3012046c2d70, file caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec
[2026-10-10T19:31:14Z] G-UNIT active           True
[2026-10-10T19:31:14Z] G-UNIT enabled          True
[2026-10-10T19:31:14Z] G-UNIT fragment         True
[2026-10-10T19:31:14Z] G-UNIT control group    True
[2026-10-10T19:31:14Z] G-UNIT ceiling          True
[2026-10-10T19:31:14Z] G-UNIT restarts         True
[2026-10-10T19:31:14Z] G-UNIT argv             True
[2026-10-10T19:31:14Z] G-UNIT cwd              True
[2026-10-10T19:31:14Z] G-UNIT cgroup           True
[2026-10-10T19:31:14Z] G-UNIT sole instance    True
[2026-10-10T19:31:14Z] G-UNIT one start        True
[2026-10-10T19:31:14Z] G-UNIT start pid        True
[2026-10-10T19:31:14Z] G-UNIT start after mark True
[2026-10-10T19:31:14Z] G-UNIT commit           True
[2026-10-10T19:31:14Z] G-UNIT file             True
[2026-10-10T19:31:14Z] G-UNIT start argv       True
[2026-10-10T19:31:14Z] G-UNIT headers          True
[2026-10-10T19:31:14Z] btc-pairbook.service MainPID 746785, NRestarts 0, MemoryMax 134217728, MemoryCurrent 25161728, MemoryPeak 26984448
[2026-10-10T19:31:14Z] G-UNIT PASS at 0 restarts; G-START PASS
[2026-10-10T19:31:14Z] peak memory of this run: 35487744 bytes
[2026-10-10T19:31:14Z] opens refused: 0; manifest opens attempted 0; chain book opens 0; requests 0, stream sessions 0
exit=0
```

G-UNIT 10 of 10 at 0 restarts, and G-START 7 of 7 more.

### 2.9 §3.8 — the proof: G-STREAM, G-BOOKS and G-TIERC (V10, V11)

The service's first `start` record is `s` = `1791660606`, 19:30:06 UTC.

- **The first qualifying window:** `T1` = `1791660600`. Its `T + 545` = `s + 539` ≥ `s + 60`.
- **The first `prove` instant:** `T1 + 4,020` = `1791664620`, 20:37:00 UTC.
- **The run:** `A` = `1791664629`. It decided at once; **no NOT YET run occurred.**

`logs/22-prove-1791664629.log`:

```text
2026-10-10T20:37:09.643285373Z
A=1791664629
[2026-10-10T20:37:09Z] MemAvailable 258142208 bytes, floor 107503616
[2026-10-10T20:37:09Z] the service's first start: pid 746785 at 2026-10-10T19:30:06Z
[2026-10-10T20:37:19Z] window 1791660600 2026-10-10T19:30:00Z qualifying True: complete; stream {"bad_lines": 0, "bytes_m15": 16174672, "bytes_m5": 90118125, "closes": 2, "files": 1, "foreign": 0, "frames": 160911, "frames_m15": 25525, "frames_m5": 135354, "lag_ms": {"max": 988, "median": 11, "min": 7, "n": 156068, "p99": 546}, "last_close_offset_ms": 905032, "max_gap_ns": 1679126473, "nonconforming": 0, "pings": 30, "pongs": 30, "stored_bytes": 13423467, "subscribe_offset_ms": 595197, "subscribes": 2, "torn": 0}
[2026-10-10T20:37:19Z]   checkpoint tau' 245: True complete statuses [200, 200, 200, 200] skew_ns 21445409
[2026-10-10T20:37:19Z]   checkpoint tau' 185: True complete statuses [200, 200, 200, 200] skew_ns 14235963
[2026-10-10T20:37:19Z]   checkpoint tau' 125: True complete statuses [200, 200, 200, 200] skew_ns 17278596
[2026-10-10T20:37:19Z]   checkpoint tau'  95: True complete statuses [200, 200, 200, 200] skew_ns 8051493
[2026-10-10T20:37:19Z]   checkpoint tau'  65: True complete statuses [200, 200, 200, 200] skew_ns 16608343
[2026-10-10T20:37:19Z]   checkpoint tau'  35: True complete statuses [200, 200, 200, 200] skew_ns 15435896
[2026-10-10T20:37:19Z]   checkpoint tau'  15: True complete statuses [200, 200, 200, 200] skew_ns 26032340
[2026-10-10T20:37:19Z] window 1791661500 2026-10-10T19:45:00Z qualifying True: complete; stream {"bad_lines": 0, "bytes_m15": 63733868, "bytes_m5": 41556858, "closes": 1, "files": 1, "foreign": 0, "frames": 160886, "frames_m15": 99408, "frames_m5": 61447, "lag_ms": {"max": 542, "median": 12, "min": 9, "n": 156563, "p99": 46}, "last_close_offset_ms": 906034, "max_gap_ns": 1619531602, "nonconforming": 0, "pings": 30, "pongs": 30, "stored_bytes": 13439976, "subscribe_offset_ms": 595134, "subscribes": 1, "torn": 0}
[2026-10-10T20:37:19Z]   checkpoint tau' 245: True complete statuses [200, 200, 200, 200] skew_ns 13379531
[2026-10-10T20:37:19Z]   checkpoint tau' 185: True complete statuses [200, 200, 200, 200] skew_ns 12289734
[2026-10-10T20:37:19Z]   checkpoint tau' 125: True complete statuses [200, 200, 200, 200] skew_ns 20765329
[2026-10-10T20:37:19Z]   checkpoint tau'  95: True complete statuses [200, 200, 200, 200] skew_ns 6164582
[2026-10-10T20:37:19Z]   checkpoint tau'  65: True complete statuses [200, 200, 200, 200] skew_ns 41987492
[2026-10-10T20:37:19Z]   checkpoint tau'  35: True complete statuses [200, 200, 200, 200] skew_ns 9823593
[2026-10-10T20:37:19Z]   checkpoint tau'  15: True complete statuses [200, 200, 200, 200] skew_ns 5913660
[2026-10-10T20:37:19Z] window 1791662400 2026-10-10T20:00:00Z qualifying True: complete; stream {"bad_lines": 0, "bytes_m15": 46964755, "bytes_m5": 32261835, "closes": 1, "files": 1, "foreign": 0, "frames": 111731, "frames_m15": 65085, "frames_m5": 46615, "lag_ms": {"max": 636, "median": 16, "min": 13, "n": 105089, "p99": 278}, "last_close_offset_ms": 905030, "max_gap_ns": 1188226456, "nonconforming": 0, "pings": 30, "pongs": 30, "stored_bytes": 9568261, "subscribe_offset_ms": 595133, "subscribes": 1, "torn": 0}
[2026-10-10T20:37:19Z]   checkpoint tau' 245: True complete statuses [200, 200, 200, 200] skew_ns 17367779
[2026-10-10T20:37:19Z]   checkpoint tau' 185: True complete statuses [200, 200, 200, 200] skew_ns 2488852
[2026-10-10T20:37:19Z]   checkpoint tau' 125: True complete statuses [200, 200, 200, 200] skew_ns 23413262
[2026-10-10T20:37:19Z]   checkpoint tau'  95: True complete statuses [200, 200, 200, 200] skew_ns 16710050
[2026-10-10T20:37:19Z]   checkpoint tau'  65: True complete statuses [200, 200, 200, 200] skew_ns 22881791
[2026-10-10T20:37:19Z]   checkpoint tau'  35: True complete statuses [200, 200, 200, 200] skew_ns 28506569
[2026-10-10T20:37:19Z]   checkpoint tau'  15: True complete statuses [200, 200, 200, 200] skew_ns 20491047
[2026-10-10T20:37:19Z] window 1791663300 2026-10-10T20:15:00Z qualifying True: complete; stream {"bad_lines": 0, "bytes_m15": 51236612, "bytes_m5": 66900145, "closes": 1, "files": 1, "foreign": 0, "frames": 172398, "frames_m15": 76403, "frames_m5": 95964, "lag_ms": {"max": 2370, "median": 23, "min": 20, "n": 163582, "p99": 2246}, "last_close_offset_ms": 905036, "max_gap_ns": 1953127672, "nonconforming": 0, "pings": 30, "pongs": 30, "stored_bytes": 14589273, "subscribe_offset_ms": 595140, "subscribes": 1, "torn": 0}
[2026-10-10T20:37:19Z]   checkpoint tau' 245: True complete statuses [200, 200, 200, 200] skew_ns 24862893
[2026-10-10T20:37:19Z]   checkpoint tau' 185: True complete statuses [200, 200, 200, 200] skew_ns 9813021
[2026-10-10T20:37:19Z]   checkpoint tau' 125: True complete statuses [200, 200, 200, 200] skew_ns 8352661
[2026-10-10T20:37:19Z]   checkpoint tau'  95: True complete statuses [200, 200, 200, 200] skew_ns 11116960
[2026-10-10T20:37:19Z]   checkpoint tau'  65: True complete statuses [200, 200, 200, 200] skew_ns 18003769
[2026-10-10T20:37:19Z]   checkpoint tau'  35: True complete statuses [200, 200, 200, 200] skew_ns 16085089
[2026-10-10T20:37:19Z]   checkpoint tau'  15: True complete statuses [200, 200, 200, 200] skew_ns 10644710
[2026-10-10T20:37:19Z] exposed 1791661200 2026-10-10T19:40:00Z: fully loaded True, counted True, quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 44.64088, 'median': 52.482622, 'p99': 62.791797, 'max': 62.791797}
[2026-10-10T20:37:19Z] exposed 1791662100 2026-10-10T19:55:00Z: fully loaded True, counted True, quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 47.436552, 'median': 49.860219, 'p99': 97.835526, 'max': 97.835526}
[2026-10-10T20:37:19Z] exposed 1791663000 2026-10-10T20:10:00Z: fully loaded True, counted True, quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 42.243197, 'median': 51.02979, 'p99': 115.589806, 'max': 115.589806}
[2026-10-10T20:37:19Z] exposed 1791663900 2026-10-10T20:25:00Z: fully loaded True, counted True, quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 45.603927, 'median': 58.761972, 'p99': 73.53779, 'max': 73.53779}
[2026-10-10T20:37:19Z] control 1791660900 2026-10-10T19:35:00Z: quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 43.823185, 'median': 51.46184, 'p99': 69.171405, 'max': 69.171405}
[2026-10-10T20:37:19Z] control 1791661500 2026-10-10T19:45:00Z: quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 47.342721, 'median': 53.988766, 'p99': 82.018863, 'max': 82.018863}
[2026-10-10T20:37:19Z] control 1791661800 2026-10-10T19:50:00Z: quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 46.089993, 'median': 49.716741, 'p99': 59.206163, 'max': 59.206163}
[2026-10-10T20:37:19Z] control 1791662400 2026-10-10T20:00:00Z: quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 45.334925, 'median': 50.903832, 'p99': 87.686085, 'max': 87.686085}
[2026-10-10T20:37:19Z] control 1791662700 2026-10-10T20:05:00Z: quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 46.157281, 'median': 49.309817, 'p99': 52.470561, 'max': 52.470561}
[2026-10-10T20:37:19Z] control 1791663300 2026-10-10T20:15:00Z: quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 46.582051, 'median': 56.311897, 'p99': 91.775566, 'max': 91.775566}
[2026-10-10T20:37:19Z] control 1791663600 2026-10-10T20:20:00Z: quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 46.008309, 'median': 54.569755, 'p99': 143.239206, 'max': 143.239206}
[2026-10-10T20:37:19Z] wrote /root/tz26-work/proof/proof-1791664629.json sha256 33813e2d36f28381b1072a5743c957fd798ecd3c5fc98558b44941f4f022aedb, 7387 bytes
[2026-10-10T20:37:19Z] READING G-STREAM: PASS, 4 of 4 complete
[2026-10-10T20:37:19Z] READING G-BOOKS: PASS, 28 of 28 checkpoints complete
[2026-10-10T20:37:19Z] READING G-TIERC: PASS, 4 counted fully loaded exposed intervals with quotes_complete true
[2026-10-10T20:37:19Z] peak memory of this run: 41746432 bytes
[2026-10-10T20:37:19Z] opens refused: 0; manifest opens attempted 15; chain book opens 0; requests 0, stream sessions 0
exit=0
```

**V11 — determinism.** The second run with the same `A` printed **`unchanged`**. The proof file `proof/proof-1791664629.json` is 7,387 bytes, SHA-256 `33813e2d36f28381b1072a5743c957fd798ecd3c5fc98558b44941f4f022aedb`.

`logs/23-prove-again.log`:

```text
2026-10-10T20:37:25.695232161Z
A=1791664629
[2026-10-10T20:37:25Z] MemAvailable 261963776 bytes, floor 107503616
[2026-10-10T20:37:25Z] the service's first start: pid 746785 at 2026-10-10T19:30:06Z
[2026-10-10T20:37:34Z] window 1791660600 2026-10-10T19:30:00Z qualifying True: complete; stream {"bad_lines": 0, "bytes_m15": 16174672, "bytes_m5": 90118125, "closes": 2, "files": 1, "foreign": 0, "frames": 160911, "frames_m15": 25525, "frames_m5": 135354, "lag_ms": {"max": 988, "median": 11, "min": 7, "n": 156068, "p99": 546}, "last_close_offset_ms": 905032, "max_gap_ns": 1679126473, "nonconforming": 0, "pings": 30, "pongs": 30, "stored_bytes": 13423467, "subscribe_offset_ms": 595197, "subscribes": 2, "torn": 0}
[2026-10-10T20:37:34Z]   checkpoint tau' 245: True complete statuses [200, 200, 200, 200] skew_ns 21445409
[2026-10-10T20:37:34Z]   checkpoint tau' 185: True complete statuses [200, 200, 200, 200] skew_ns 14235963
[2026-10-10T20:37:34Z]   checkpoint tau' 125: True complete statuses [200, 200, 200, 200] skew_ns 17278596
[2026-10-10T20:37:34Z]   checkpoint tau'  95: True complete statuses [200, 200, 200, 200] skew_ns 8051493
[2026-10-10T20:37:34Z]   checkpoint tau'  65: True complete statuses [200, 200, 200, 200] skew_ns 16608343
[2026-10-10T20:37:34Z]   checkpoint tau'  35: True complete statuses [200, 200, 200, 200] skew_ns 15435896
[2026-10-10T20:37:34Z]   checkpoint tau'  15: True complete statuses [200, 200, 200, 200] skew_ns 26032340
[2026-10-10T20:37:34Z] window 1791661500 2026-10-10T19:45:00Z qualifying True: complete; stream {"bad_lines": 0, "bytes_m15": 63733868, "bytes_m5": 41556858, "closes": 1, "files": 1, "foreign": 0, "frames": 160886, "frames_m15": 99408, "frames_m5": 61447, "lag_ms": {"max": 542, "median": 12, "min": 9, "n": 156563, "p99": 46}, "last_close_offset_ms": 906034, "max_gap_ns": 1619531602, "nonconforming": 0, "pings": 30, "pongs": 30, "stored_bytes": 13439976, "subscribe_offset_ms": 595134, "subscribes": 1, "torn": 0}
[2026-10-10T20:37:34Z]   checkpoint tau' 245: True complete statuses [200, 200, 200, 200] skew_ns 13379531
[2026-10-10T20:37:34Z]   checkpoint tau' 185: True complete statuses [200, 200, 200, 200] skew_ns 12289734
[2026-10-10T20:37:34Z]   checkpoint tau' 125: True complete statuses [200, 200, 200, 200] skew_ns 20765329
[2026-10-10T20:37:34Z]   checkpoint tau'  95: True complete statuses [200, 200, 200, 200] skew_ns 6164582
[2026-10-10T20:37:34Z]   checkpoint tau'  65: True complete statuses [200, 200, 200, 200] skew_ns 41987492
[2026-10-10T20:37:34Z]   checkpoint tau'  35: True complete statuses [200, 200, 200, 200] skew_ns 9823593
[2026-10-10T20:37:34Z]   checkpoint tau'  15: True complete statuses [200, 200, 200, 200] skew_ns 5913660
[2026-10-10T20:37:34Z] window 1791662400 2026-10-10T20:00:00Z qualifying True: complete; stream {"bad_lines": 0, "bytes_m15": 46964755, "bytes_m5": 32261835, "closes": 1, "files": 1, "foreign": 0, "frames": 111731, "frames_m15": 65085, "frames_m5": 46615, "lag_ms": {"max": 636, "median": 16, "min": 13, "n": 105089, "p99": 278}, "last_close_offset_ms": 905030, "max_gap_ns": 1188226456, "nonconforming": 0, "pings": 30, "pongs": 30, "stored_bytes": 9568261, "subscribe_offset_ms": 595133, "subscribes": 1, "torn": 0}
[2026-10-10T20:37:34Z]   checkpoint tau' 245: True complete statuses [200, 200, 200, 200] skew_ns 17367779
[2026-10-10T20:37:34Z]   checkpoint tau' 185: True complete statuses [200, 200, 200, 200] skew_ns 2488852
[2026-10-10T20:37:34Z]   checkpoint tau' 125: True complete statuses [200, 200, 200, 200] skew_ns 23413262
[2026-10-10T20:37:34Z]   checkpoint tau'  95: True complete statuses [200, 200, 200, 200] skew_ns 16710050
[2026-10-10T20:37:34Z]   checkpoint tau'  65: True complete statuses [200, 200, 200, 200] skew_ns 22881791
[2026-10-10T20:37:34Z]   checkpoint tau'  35: True complete statuses [200, 200, 200, 200] skew_ns 28506569
[2026-10-10T20:37:34Z]   checkpoint tau'  15: True complete statuses [200, 200, 200, 200] skew_ns 20491047
[2026-10-10T20:37:34Z] window 1791663300 2026-10-10T20:15:00Z qualifying True: complete; stream {"bad_lines": 0, "bytes_m15": 51236612, "bytes_m5": 66900145, "closes": 1, "files": 1, "foreign": 0, "frames": 172398, "frames_m15": 76403, "frames_m5": 95964, "lag_ms": {"max": 2370, "median": 23, "min": 20, "n": 163582, "p99": 2246}, "last_close_offset_ms": 905036, "max_gap_ns": 1953127672, "nonconforming": 0, "pings": 30, "pongs": 30, "stored_bytes": 14589273, "subscribe_offset_ms": 595140, "subscribes": 1, "torn": 0}
[2026-10-10T20:37:34Z]   checkpoint tau' 245: True complete statuses [200, 200, 200, 200] skew_ns 24862893
[2026-10-10T20:37:34Z]   checkpoint tau' 185: True complete statuses [200, 200, 200, 200] skew_ns 9813021
[2026-10-10T20:37:34Z]   checkpoint tau' 125: True complete statuses [200, 200, 200, 200] skew_ns 8352661
[2026-10-10T20:37:34Z]   checkpoint tau'  95: True complete statuses [200, 200, 200, 200] skew_ns 11116960
[2026-10-10T20:37:34Z]   checkpoint tau'  65: True complete statuses [200, 200, 200, 200] skew_ns 18003769
[2026-10-10T20:37:34Z]   checkpoint tau'  35: True complete statuses [200, 200, 200, 200] skew_ns 16085089
[2026-10-10T20:37:34Z]   checkpoint tau'  15: True complete statuses [200, 200, 200, 200] skew_ns 10644710
[2026-10-10T20:37:34Z] exposed 1791661200 2026-10-10T19:40:00Z: fully loaded True, counted True, quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 44.64088, 'median': 52.482622, 'p99': 62.791797, 'max': 62.791797}
[2026-10-10T20:37:34Z] exposed 1791662100 2026-10-10T19:55:00Z: fully loaded True, counted True, quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 47.436552, 'median': 49.860219, 'p99': 97.835526, 'max': 97.835526}
[2026-10-10T20:37:34Z] exposed 1791663000 2026-10-10T20:10:00Z: fully loaded True, counted True, quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 42.243197, 'median': 51.02979, 'p99': 115.589806, 'max': 115.589806}
[2026-10-10T20:37:34Z] exposed 1791663900 2026-10-10T20:25:00Z: fully loaded True, counted True, quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 45.603927, 'median': 58.761972, 'p99': 73.53779, 'max': 73.53779}
[2026-10-10T20:37:34Z] control 1791660900 2026-10-10T19:35:00Z: quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 43.823185, 'median': 51.46184, 'p99': 69.171405, 'max': 69.171405}
[2026-10-10T20:37:34Z] control 1791661500 2026-10-10T19:45:00Z: quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 47.342721, 'median': 53.988766, 'p99': 82.018863, 'max': 82.018863}
[2026-10-10T20:37:34Z] control 1791661800 2026-10-10T19:50:00Z: quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 46.089993, 'median': 49.716741, 'p99': 59.206163, 'max': 59.206163}
[2026-10-10T20:37:34Z] control 1791662400 2026-10-10T20:00:00Z: quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 45.334925, 'median': 50.903832, 'p99': 87.686085, 'max': 87.686085}
[2026-10-10T20:37:34Z] control 1791662700 2026-10-10T20:05:00Z: quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 46.157281, 'median': 49.309817, 'p99': 52.470561, 'max': 52.470561}
[2026-10-10T20:37:34Z] control 1791663300 2026-10-10T20:15:00Z: quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 46.582051, 'median': 56.311897, 'p99': 91.775566, 'max': 91.775566}
[2026-10-10T20:37:34Z] control 1791663600 2026-10-10T20:20:00Z: quotes_complete True, complete True, Tier C offsets {'n': 14, 'min': 46.008309, 'median': 54.569755, 'p99': 143.239206, 'max': 143.239206}
[2026-10-10T20:37:34Z] unchanged /root/tz26-work/proof/proof-1791664629.json sha256 33813e2d36f28381b1072a5743c957fd798ecd3c5fc98558b44941f4f022aedb
[2026-10-10T20:37:34Z] READING G-STREAM: PASS, 4 of 4 complete
[2026-10-10T20:37:34Z] READING G-BOOKS: PASS, 28 of 28 checkpoints complete
[2026-10-10T20:37:34Z] READING G-TIERC: PASS, 4 counted fully loaded exposed intervals with quotes_complete true
[2026-10-10T20:37:34Z] peak memory of this run: 41750528 bytes
[2026-10-10T20:37:34Z] opens refused: 0; manifest opens attempted 15; chain book opens 0; requests 0, stream sessions 0
exit=0
```

**Considered windows:** four, every one qualifying and complete. The window `1791664200` was open at `A`, and its `T + 910` was not yet reached, so it was not considered.

**Window `1791660600`'s stream** held 2 subscribes and 2 closes in one file. That is one reconnect inside the window: the service log reads "2 segments". Its largest gap, 1.679 s, stayed below the 15 s bound. Why the first session closed is in the stored file and was not read.

**Exposed intervals:** four — `1791661200`, `1791662100`, `1791663000` and `1791663900`. Each was fully loaded and counted, with `quotes_complete` true and `complete` true.

**Control intervals:** seven, every one with `quotes_complete` true.

### 2.10 The BTC pair's measured rate, over G-STREAM's four windows (TZ §8)

A script under `/root/tz04a-env` derived this from the proof file's counts (§6 item 7). The span is each window's last close less its first subscribe.

`logs/31-rate.log`:

```text
2026-10-10T20:38:54.132702219Z
T 1791660600: span 309835 ms; frames m15 25525 m5 135354 all 160911; per s m15 82.4 m5 436.9 all 519.3; stream stored 13423467 bytes, 83.4 bytes/frame; window stored 13447895
T 1791661500: span 310900 ms; frames m15 99408 m5 61447 all 160886; per s m15 319.7 m5 197.6 all 517.5; stream stored 13439976 bytes, 83.5 bytes/frame; window stored 13465271
T 1791662400: span 309897 ms; frames m15 65085 m5 46615 all 111731; per s m15 210.0 m5 150.4 all 360.5; stream stored 9568261 bytes, 85.6 bytes/frame; window stored 9592063
T 1791663300: span 309896 ms; frames m15 76403 m5 95964 all 172398; per s m15 246.5 m5 309.7 all 556.3; stream stored 14589273 bytes, 84.6 bytes/frame; window stored 14614206
four windows: 1240528 ms; frames/s m15 214.8 m5 273.6 all 488.4
stream stored bytes a window, mean 12755244.2; a day (96 windows) 1224503448
days to STREAM_CAP 8,000,000,000 at that rate: 6.53
window stored bytes (stream + rest), mean 12779858.8
```

| quantity | measured | modelled in TZ §1 |
|---|---|---|
| frames a second, `btc-updown-15m` | `214.8` (82.4 to 319.7 a window) | `140.5` |
| frames a second, `btc-updown-5m` | `273.6` (150.4 to 436.9) | — |
| frames a second, the pair | **`488.4`** (360.5 to 556.3) | `1,032` |
| stored stream bytes a window | **`12,755,244.2`** mean (9,568,261 to 14,589,273); `83.4` to `85.6` bytes a frame | `26.2` MB |
| days to `STREAM_CAP`, `8,000,000,000` bytes | **`6.53`**, at 96 windows a day | `3.2` |

These are four windows on a Saturday evening, and they bound no other day.

### 2.11 G-LOAD (V12)

`logs/24-load.log`:

```text
2026-10-10T20:37:34.752139576Z
[2026-10-10T20:37:34Z] memory.current 32374784
[2026-10-10T20:37:34Z] memory.peak 79376384
[2026-10-10T20:37:34Z] memory.swap.current 21716992
[2026-10-10T20:37:34Z] memory.swap.peak 21934080
[2026-10-10T20:37:34Z] stat.anon 23019520
[2026-10-10T20:37:34Z] stat.file 8257536
[2026-10-10T20:37:34Z] stat.kernel 618496
[2026-10-10T20:37:34Z] stat.sock 0
[2026-10-10T20:37:34Z] stat.file_dirty 0
[2026-10-10T20:37:34Z] stat.file_writeback 0
[2026-10-10T20:37:34Z] process 746785 VmHWM:	   34888 kB
[2026-10-10T20:37:34Z] process 746785 VmRSS:	   32572 kB
[2026-10-10T20:37:34Z] process 746785 VmSwap:	   12256 kB
[2026-10-10T20:37:34Z] process 746785 Threads:	2
[2026-10-10T20:37:34Z] G-LOAD: process 746785, processor 70.42 s over 4048.6 s since 2026-10-10T19:30:06Z: 0.0174 of one core, bound 0.25
[2026-10-10T20:37:34Z] G-LOAD PASS
[2026-10-10T20:37:34Z] peak memory of this run: 35483648 bytes
[2026-10-10T20:37:34Z] opens refused: 0; manifest opens attempted 0; chain book opens 0; requests 0, stream sessions 0
exit=0
```

**`0.0174` of one core, against `0.25`: PASS.**

The control group's `memory.peak` reads `79,376,384`, and the journal reports a 75.6M peak for the first process. Both include page cache: `anon` read `23,019,520` and the process's `VmHWM` 34,888 kB.

### 2.12 §3.9 and §3.10 — G-RESTART, G-UNIT at one restart, G-STILL (V13, V14)

The mark was taken at second 459 of window `1791664200`. B-KILL-SVC ran at second **464**, inside the band of 15 to 480, behind a phase guard (§6 item 6). **It was not refused.**

`logs/25-mark-kill-svc.log`:

```text
2026-10-10T20:37:39.488309645Z
phase=459
[2026-10-10T20:37:39Z] mark kill-svc at 2026-10-10T20:37:39Z: btc-pairbook.service {'ns': 1791664659610418836, 'unit': 'btc-pairbook.service', 'MainPID': '746785', 'NRestarts': '0', 'ActiveState': 'active'}
[2026-10-10T20:37:39Z] peak memory of this run: 35225600 bytes
[2026-10-10T20:37:39Z] opens refused: 0; manifest opens attempted 0; chain book opens 0; requests 0, stream sessions 0
exit=0
```

`logs/26-kill-svc.log`:

```text
2026-10-10T20:37:44.038477585Z
phase=464
exit=0
2026-10-10T20:37:44.045271528Z
```

`restart` ran 31 s after the kill:

`logs/27-restart.log`:

```text
2026-10-10T20:38:15.536142548Z
[2026-10-10T20:38:15Z] record stop pid 746785 at 2026-10-10T20:37:44Z
[2026-10-10T20:38:15Z] record start pid 752775 at 2026-10-10T20:37:49Z
[2026-10-10T20:38:15Z] G-RESTART: the stop of 746785, the start of 752775 5.480 s later
[2026-10-10T20:38:15Z] G-UNIT active           True
[2026-10-10T20:38:15Z] G-UNIT enabled          True
[2026-10-10T20:38:15Z] G-UNIT fragment         True
[2026-10-10T20:38:15Z] G-UNIT control group    True
[2026-10-10T20:38:15Z] G-UNIT ceiling          True
[2026-10-10T20:38:15Z] G-UNIT restarts         True
[2026-10-10T20:38:15Z] G-UNIT argv             True
[2026-10-10T20:38:15Z] G-UNIT cwd              True
[2026-10-10T20:38:15Z] G-UNIT cgroup           True
[2026-10-10T20:38:15Z] G-UNIT sole instance    True
[2026-10-10T20:38:15Z] btc-pairbook.service MainPID 752775, NRestarts 1, MemoryMax 134217728, MemoryCurrent 24780800, MemoryPeak 25038848
[2026-10-10T20:38:15Z] G-UNIT PASS at 1 restarts
[2026-10-10T20:38:15Z] G-RESTART PASS
[2026-10-10T20:38:15Z] peak memory of this run: 35356672 bytes
[2026-10-10T20:38:15Z] opens refused: 0; manifest opens attempted 0; chain book opens 0; requests 0, stream sessions 0
exit=0
```

`logs/28-final.log`:

```text
2026-10-10T20:38:23.489844525Z
[2026-10-10T20:38:23Z] G-UNIT active           True
[2026-10-10T20:38:23Z] G-UNIT enabled          True
[2026-10-10T20:38:23Z] G-UNIT fragment         True
[2026-10-10T20:38:23Z] G-UNIT control group    True
[2026-10-10T20:38:23Z] G-UNIT ceiling          True
[2026-10-10T20:38:23Z] G-UNIT restarts         True
[2026-10-10T20:38:23Z] G-UNIT argv             True
[2026-10-10T20:38:23Z] G-UNIT cwd              True
[2026-10-10T20:38:23Z] G-UNIT cgroup           True
[2026-10-10T20:38:23Z] G-UNIT sole instance    True
[2026-10-10T20:38:23Z] btc-pairbook.service MainPID 752775, NRestarts 1, MemoryMax 134217728, MemoryCurrent 24780800, MemoryPeak 25038848
[2026-10-10T20:38:23Z] G-UNIT PASS at 1 restarts
[2026-10-10T20:38:23Z] btc-chainbook.service {'MainPID': '0', 'NRestarts': '0', 'ActiveState': 'inactive'}, MemoryCurrent [not set], MemoryPeak [not set]
[2026-10-10T20:38:23Z] btc-pairbook.service {'MainPID': '752775', 'NRestarts': '1', 'ActiveState': 'active'}, MemoryCurrent 24780800, MemoryPeak 25038848
[2026-10-10T20:38:23Z] btc-recorder.service {'MainPID': '4148534', 'NRestarts': '2', 'ActiveState': 'active'}, MemoryCurrent 121360384, MemoryPeak 200912896
[2026-10-10T20:38:23Z] G-STILL PASS: the recorder unchanged since 2026-10-10T19:03:54Z
[2026-10-10T20:38:23Z] memory.current 24780800
[2026-10-10T20:38:23Z] memory.peak 25038848
[2026-10-10T20:38:23Z] memory.swap.current 0
[2026-10-10T20:38:23Z] memory.swap.peak 0
[2026-10-10T20:38:23Z] stat.anon 24166400
[2026-10-10T20:38:23Z] stat.file 417792
[2026-10-10T20:38:23Z] stat.kernel 196608
[2026-10-10T20:38:23Z] stat.sock 0
[2026-10-10T20:38:23Z] stat.file_dirty 0
[2026-10-10T20:38:23Z] stat.file_writeback 0
[2026-10-10T20:38:23Z] FINAL PASS
[2026-10-10T20:38:23Z] peak memory of this run: 35483648 bytes
[2026-10-10T20:38:23Z] opens refused: 0; manifest opens attempted 0; chain book opens 0; requests 0, stream sessions 0
exit=0
```

### 2.13 Units' memory at every read

| instant (UTC) | unit | `MemoryCurrent` | `MemoryPeak` |
|---|---|---|---|
| 19:03:54 (`still`) | recorder `4148534` | `129,949,696` | `200,912,896` |
| 19:03:54 | chain book `4064090` | `6,508,544` | `18,735,104` |
| 19:30:06 (journal, at its stop) | chain book | — | 17.8M, 17.4M swap peak |
| 19:31:14 (`unit 0`) | pair book `746785` | `25,161,728` | `26,984,448` |
| 20:37:34 (`load`) | pair book `746785` | `32,374,784` | `79,376,384`; swap `21,716,992` |
| 20:37:44 (journal, at its stop) | pair book `746785` | — | 75.6M, 20.9M swap peak |
| 20:38:15 (`restart`), 20:38:23 (`final`) | pair book `752775` | `24,780,800` | `25,038,848` |
| 20:38:23 (`final`) | recorder | `121,360,384` | `200,912,896` |
| 20:38:35 (§3.11) | recorder | `113,192,960` | `200,912,896` |

### 2.14 Memory and the capture roots — every mode (V15)

| mode | peak memory, bytes | refused | manifest opens | chain book opens | requests / sessions |
|---|---|---|---|---|---|
| `fingerprint` (staged) | 36,405,248 | 0 | 0 | 0 | 0 / 0 |
| `selftest` | 53,510,144 | 0 | 0 | 0 | 3 / 3, loopback |
| `still` | 35,483,648 | 0 | 0 | 0 | 0 / 0 |
| `scratch` | 35,487,744 | 0 | 0 | 0 | 0 / 0 |
| `reclaim` (scratch) | 37,335,040 | 0 | 0 | 0 | 0 / 0 |
| `prestart` | 43,307,008 | 0 | **2,016** | 0 | 3 / 1 |
| `mark stop-cb`, `mark start-svc` | 35,356,672 each | 0 | 0 | 0 | 0 / 0 |
| `chainbook` | 35,491,840 | 0 | 0 | **1** | 0 / 0 |
| `unit 0` | 35,487,744 | 0 | 0 | 0 | 0 / 0 |
| `prove`, deciding | 41,746,432 | 0 | **15** (≤ 25) | 0 | 0 / 0 |
| `prove`, same `A` | 41,750,528 | 0 | **15** (≤ 25) | 0 | 0 / 0 |
| `load` | 35,483,648 | 0 | 0 | 0 | 0 / 0 |
| `mark kill-svc` | 35,225,600 | 0 | 0 | 0 | 0 / 0 |
| `restart` | 35,356,672 | 0 | 0 | 0 | 0 / 0 |
| `final` | 35,483,648 | 0 | 0 | 0 | 0 / 0 |
| `reclaim` (own) | 37,085,184 | 0 | 0 | 0 | 0 / 0 |

Every peak is below the `107,503,616` floor's half, `53,751,808`.

The self-test printed `opens refused: 0` at its end, as each mode does. Its own checks of the audit hook passed inside the 74.

### 2.15 §3.11 — the closing reads (V17), and contract §4.2's self-check (V16)

`logs/29-closing.log`:

```text
Sat Oct 10 08:38:35 PM UTC 2026
1791664715
1
MemTotal:         978640 kB
MemAvailable:     243044 kB
SwapTotal:       3174396 kB
SwapFree:        2844564 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12931727360
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
1
chainbook exit=0
active
inactive
exit=0
enabled
disabled
exit=0
pairbook unit exit=0
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
/root/tz24-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
/var/lib/btc-pairbook exit=0
1725
3.12.3 17.1
/root/btc-5m-twap       73da754 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/root/tz26-work/wt      e8b46a8 [tz-26-nesting-b3-capture]
195236495	/root/.claude
528768307	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/30ec6406-6385-5122-88dc-9ad61b1f2846/scratchpad
total 16
drwx------  4 root root 4096 Oct 10 19:04 .
drwx------ 16 root root 4096 Oct 10 18:59 ..
drwx------  4 root root 4096 Oct 10 19:01 30ec6406-6385-5122-88dc-9ad61b1f2846
drwx------  3 root root 4096 Oct 10 18:59 d5dc7bd3-91ab-4f86-bdfc-8d305cb318f9
=== closing reads
MainPID=4148534
NRestarts=2
MemoryCurrent=113192960
MemoryPeak=200912896
ActiveState=active

MainPID=0
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=[not set]
ActiveState=inactive

MainPID=752775
NRestarts=1
MemoryCurrent=24780800
MemoryPeak=25038848
ActiveState=active
enabled
disabled
exit=0
2026-10-10T19:30:05+00:00 vultr systemd[1]: Stopping btc-chainbook.service - btc-5m-twap chain book, fifteen-minute and five-minute books...
2026-10-10T19:30:06+00:00 vultr systemd[1]: btc-chainbook.service: Deactivated successfully.
2026-10-10T19:30:06+00:00 vultr systemd[1]: Stopped btc-chainbook.service - btc-5m-twap chain book, fifteen-minute and five-minute books.
2026-10-10T19:30:06+00:00 vultr systemd[1]: btc-chainbook.service: Consumed 1min 19.672s CPU time, 17.8M memory peak, 17.4M memory swap peak.
2026-10-10T19:30:06+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-10T20:37:44+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 746785 (python) on client request.
2026-10-10T20:37:44+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-10T20:37:44+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 1min 10.479s CPU time, 75.6M memory peak, 20.9M memory swap peak.
2026-10-10T20:37:49+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 1.
2026-10-10T20:37:49+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
[2026-10-10T19:30:06Z] start record: pid 746785 commit e8b46a85d61e1a17841962846f6d3012046c2d70 file_sha256 caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec; free 12985090048 bytes, streams 0 bytes
[2026-10-10T19:30:06Z] window 1791660600 (2026-10-10T19:30:00Z): documents from 2026-10-10T19:39:05Z
[2026-10-10T19:45:10Z] window 1791660600 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 160911 frames, 2 segments, 13423467 bytes stored
[2026-10-10T19:45:10Z] window 1791661500 (2026-10-10T19:45:00Z): documents from 2026-10-10T19:54:05Z
[2026-10-10T20:00:10Z] window 1791661500 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 160886 frames, 1 segments, 13439976 bytes stored
[2026-10-10T20:00:10Z] window 1791662400 (2026-10-10T20:00:00Z): documents from 2026-10-10T20:09:05Z
[2026-10-10T20:15:10Z] window 1791662400 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 111731 frames, 1 segments, 9568261 bytes stored
[2026-10-10T20:15:10Z] window 1791663300 (2026-10-10T20:15:00Z): documents from 2026-10-10T20:24:05Z
[2026-10-10T20:30:10Z] window 1791663300 closed: documents True in 2 attempts; checkpoints 7 of 7, missed 0; stream opened, 172398 frames, 1 segments, 14589273 bytes stored
[2026-10-10T20:30:10Z] window 1791664200 (2026-10-10T20:30:00Z): documents from 2026-10-10T20:39:05Z
[2026-10-10T20:37:44Z] stop record written; requests 120, sessions 5, frames 605926, stream bytes 51020977, other bytes 100424
[2026-10-10T20:37:49Z] stale pid file (pid 746785) replaced
[2026-10-10T20:37:49Z] start record: pid 752775 commit e8b46a85d61e1a17841962846f6d3012046c2d70 file_sha256 caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec; free 12931923968 bytes, streams 51020977 bytes
[2026-10-10T20:37:49Z] window 1791664200 (2026-10-10T20:30:00Z): documents from 2026-10-10T20:39:05Z
               total        used        free      shared  buff/cache   available
Mem:      1002127360   715644928    76939264      348160   379420672   286482432
Swap:     3250581504   337747968  2912833536
6166658	/root/tz26-work
118507	/root/btc-pairbook-svc
51124272	/var/lib/btc-pairbook
195236495	/root/.claude
{
 "marks": {
  "kill-svc": {
   "ActiveState": "active",
   "MainPID": "746785",
   "NRestarts": "0",
   "ns": 1791664659610418836,
   "unit": "btc-pairbook.service"
  },
  "start-svc": {
   "ActiveState": "inactive",
   "MainPID": "0",
   "NRestarts": "0",
   "ns": 1791659101493317797,
   "unit": "btc-pairbook.service"
  },
  "stop-cb": {
   "ActiveState": "active",
   "MainPID": "4064090",
   "NRestarts": "1",
   "ns": 1791659101328741066,
   "unit": "btc-chainbook.service"
  }
 },
 "still": {
  "at": "2026-10-10T19:03:54Z",
  "recorder": {
   "ActiveState": "active",
   "MainPID": "4148534",
   "NRestarts": "2"
  }
 }
}
```

The closing reads of H4 and H5 now read the switch: the chain book is `inactive` and `disabled`; the pair book's unit exists, and its copy and root are present. The forensic store is still `1,725`.

**Contract §4.2's self-check** ran after the push and the pull request, and before the report's commit:

`logs/30-selfcheck.log`:

```text
2026-10-10T20:38:44.673604327Z
$ git rev-list origin/main | grep -c e8b46a85d61e1a17841962846f6d3012046c2d70
0
$ git diff --name-only origin/main origin/tz-26-nesting-b3-capture
deploy/systemd/btc-pairbook.service
research/tz26-nesting-b3-capture.py
$ git diff --name-status origin/main origin/tz-26-nesting-b3-capture
A	deploy/systemd/btc-pairbook.service
A	research/tz26-nesting-b3-capture.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
grep exit=1
```

The first line prints `0`. The diff names the two implementation files, both `A`. No `.parquet` or `.zip` file is on `main`.

### 2.16 Every file the run wrote, by SHA-256, but the capture's own

| path under `/root/tz26-work` | bytes | SHA-256 |
|---|---|---|
| `report-template.md` | 27687 | `da16e11e8a5fc2e154c3fe57a8af6fe5dc3c8f3614650e9c4eb51d22268c75f2` |
| `state.json` | 632 | `6898b11a9bd15bda549de02238083db01ef9c97d7be1f9bc35beba4971b28d02` |
| `logs/00-pull.log` | 418 | `e01b8f69eb4f0a5d3812c6718aee7d7947ceef8ca1b3ecb629757a43f711a9c8` |
| `logs/00-workdir.log` | 38 | `3b90e59e4a5fcd9d4363b2b2687ad9c154bbdf5efe55879fde30a5bd71b1e765` |
| `logs/01-stage.log` | 303 | `83358d4b8d6bbb16a75a7dfa2542c11553b7e6dc1b9792d1423bd815d5472121` |
| `logs/02-fingerprint.log` | 6780 | `4228258b92d0153e03d97adbedaf4d0ab32da3136234087b80807faa9adec9d8` |
| `logs/03-host-gate.log` | 1245 | `feaea71fe87714114c80b82f5c2c755d9652bf6b1d077a66a27566970db37020` |
| `logs/04-refs.log` | 2311 | `a3c3dbb7cb91f0c2e7bd5db4b6087590139610487d64dcfad509a49672d7885b` |
| `logs/05-branch.log` | 557 | `212d04f408d3fa0a26eeb9100d0a45e0c05a82783494985a51f6d5dbfac1f2dd` |
| `logs/06-commit-push.log` | 704 | `c4c779646d5e44a24ee0d65745460c67044f2a76f9005368c58001e302a7ecd4` |
| `logs/07-pr.log` | 94 | `8acca31e166d6ce46436a2f1a12eb9b3ef5ce23d135127e2baa9b1d946c08075` |
| `logs/08-selftest.log` | 6456 | `16a36ef4b36a19b724fceb21000008773cd9af085922f6943eef36ceaae93838` |
| `logs/09-still.log` | 737 | `d5e809b9e7e13b09e652845c159293950156e311b9f8ee156648a50b714dd0a0` |
| `logs/10-scratch.log` | 798 | `c3f5ce6c3f2b08fa7c94464400dce69358f9f240f169a07efefb98294de08bfd` |
| `logs/11-reclaim-scratch.log` | 458 | `baded2cb623a0e28e37bb890a6c12d56e95cabfc683544c6a52fc1c136c31f22` |
| `logs/12-rm-scratch.log` | 90 | `5d521001543da460d9fc77c525a9ead9efc687fd8fe83c833d4720ae0e611d08` |
| `logs/13-svc-copy.log` | 357 | `cedec51c34d44b39ad0d16efe0ceeea45470c80beb4ec5f51ee1c7031af4d71d` |
| `logs/14-prestart.log` | 1703 | `17e42247b6f3d63ae916d3b052a1c7f61e9f100f82219b9c80dd7ab8974c5e30` |
| `logs/15-install.log` | 66 | `1c070fae1d4a826897e527dd9f59aa9da6399fc7c1eb7e73862586a95c1c2399` |
| `logs/16-mark-stop-cb.log` | 429 | `448680d3d269e6b8c2a770bb33e968ee6d3c479ad855fa6c682dc06499c3bbad` |
| `logs/17-mark-start-svc.log` | 425 | `e4a1f638339eda36ec0fc99626abf9971f4ccc0fdfadc9411bb3e0cd719656bc` |
| `logs/18-switch-refused.log` | 185 | `e1d962c241dbaa71583631e18b22e4832cddf96a242396ff5296fb1ab75236e0` |
| `logs/19-switch-boss.log` | 1160 | `4b42224892905cd3b02d1f36abc288de5acbd393ff3b940d4861bb3d82e6049e` |
| `logs/20-chainbook.log` | 758 | `82268be880cb8bae8803c72810d8b4dee7b3a16c27fff63cc7cf699b9bddf12d` |
| `logs/21-unit0.log` | 1512 | `26280e48b17d588340a895a755f951d3084857ba1ea8547908f5c4538a9dbddf` |
| `logs/22-prove-1791664629.log` | 8203 | `390e5c61aa11d7bfa8d7d53b62f621b0508d8c95fafdb078df1ccf96756b7411` |
| `logs/23-prove-again.log` | 8195 | `202b032f0b8f990f4b46732cb96a3e9adeb1b5ea1ac4e55e6188959a12a64beb` |
| `logs/24-load.log` | 1052 | `897c3ec1bca24da3c8937e8d2780d468b9a7e70600265c9ca2f98e29c9a76cae` |
| `logs/25-mark-kill-svc.log` | 437 | `3eaf494c037073ccc7a40cf2eae88a75d2de7bc46e8dc51bf9d6b77985cb3a72` |
| `logs/26-kill-svc.log` | 79 | `bf19c89300c786345241b24e4e40da948cafbed18ac89c5be25726118cb7844f` |
| `logs/27-restart.log` | 1194 | `268665a1f3efae1f0c1aab7fe2a5aa5078668c432561813ec954d9de82005745` |
| `logs/28-final.log` | 1936 | `9aea7d22da56d86610398e66a56fd50afe922f518cf325f8a7997b69b2868502` |
| `logs/29-closing.log` | 5601 | `1434e993c95c3692d3a7776d9b189397d13e8dc281e6189ab427e5716954b1b0` |
| `logs/30-selfcheck.log` | 476 | `4b84e23ab265b010e50d7d64bf127e3cae301bc4e6bda5ca0557746bdc25096f` |
| `logs/31-rate.log` | 975 | `051b9b45666c3bc69925fd66a1f9c135d17325fbe2fde96815e0380f48ce3dcc` |
| `logs/32-files.log` | 5187 | `9858cb8640441585a9272112b733667d77dacf16144754892454fbce3632d163` |
| `prestart/prestart.json` | 2619 | `02b252af1411143a0baf85096a1c5ddb9d12034192f3caf323062f9e551e9d85` |
| `prestart/stream.jsonl.gz` | 274856 | `b1cd8024d3ac3214637fcf3528618f1286b85a8b4118a47bf0a7c1428babfa9d` |
| `proof/proof-1791664629.json` | 7387 | `33813e2d36f28381b1072a5743c957fd798ecd3c5fc98558b44941f4f022aedb` |
| `stage/deploy/systemd/btc-pairbook.service` | 761 | `ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8` |
| `stage/research/tz26-nesting-b3-capture.py` | 118466 | `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec` |
| `wt/research/tz26-nesting-b3-capture.py` | 118466 | `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec` |
| `wt/deploy/systemd/btc-pairbook.service` | 761 | `ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8` |

Outside `/root/tz26-work`:

- `/root/btc-pairbook-svc/tz26-nesting-b3-capture.py`, `caed70d9…`.
- `/root/btc-pairbook-svc/commit.txt`, `1d683c6a5b1c87648587df5a1777c96c8bcd478d2e0aa4805857234a3e702ffe`.
- `/etc/systemd/system/btc-pairbook.service`, `ba02fe41…`, and the link `multi-user.target.wants/btc-pairbook.service` that `systemctl enable` made. The link that `disable` removed was the chain book's.
- `/var/lib/btc-pairbook/`, created empty by B-INSTALL. Since then the unit alone writes it.
- `/root/btc-forensics/`: §2.17's copies.

### 2.17 §9 B-RECLAIM-OWN — last, after §3.11, with this report drafted

B-RECLAIM-OWN ran from `/root`, as four commands in four tool calls (§6 item 9). Its output was written to no file. Each command and its output, verbatim from the session:

```text
$ date -u +%FT%T.%NZ; nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz26-work/wt/research/tz26-nesting-b3-capture.py reclaim /root/tz26-work; echo "exit=$?"
2026-10-10T20:41:53.134089606Z
[2026-10-10T20:41:53Z] reclaim: 2044 report tokens; forensic store holds 1725 files
[2026-10-10T20:41:53Z] reclaim: /root/tz26-work/wt skipped: no file but its HEAD's, and HEAD e8b46a85d61e1a17841962846f6d3012046c2d70 is its upstream's
[2026-10-10T20:41:53Z] R copied da16e11e8a5fc2e154c3fe57a8af6fe5dc3c8f3614650e9c4eb51d22268c75f2 /root/btc-forensics/tz26-work--report-template.md
[2026-10-10T20:41:53Z] R copied 6898b11a9bd15bda549de02238083db01ef9c97d7be1f9bc35beba4971b28d02 /root/btc-forensics/tz26-work--state.json
[2026-10-10T20:41:53Z] R copied e01b8f69eb4f0a5d3812c6718aee7d7947ceef8ca1b3ecb629757a43f711a9c8 /root/btc-forensics/tz26-work--logs--00-pull.log
[2026-10-10T20:41:53Z] R copied 3b90e59e4a5fcd9d4363b2b2687ad9c154bbdf5efe55879fde30a5bd71b1e765 /root/btc-forensics/tz26-work--logs--00-workdir.log
[2026-10-10T20:41:53Z] R copied 83358d4b8d6bbb16a75a7dfa2542c11553b7e6dc1b9792d1423bd815d5472121 /root/btc-forensics/tz26-work--logs--01-stage.log
[2026-10-10T20:41:53Z] R copied 4228258b92d0153e03d97adbedaf4d0ab32da3136234087b80807faa9adec9d8 /root/btc-forensics/tz26-work--logs--02-fingerprint.log
[2026-10-10T20:41:53Z] R copied feaea71fe87714114c80b82f5c2c755d9652bf6b1d077a66a27566970db37020 /root/btc-forensics/tz26-work--logs--03-host-gate.log
[2026-10-10T20:41:53Z] R copied a3c3dbb7cb91f0c2e7bd5db4b6087590139610487d64dcfad509a49672d7885b /root/btc-forensics/tz26-work--logs--04-refs.log
[2026-10-10T20:41:53Z] R copied 212d04f408d3fa0a26eeb9100d0a45e0c05a82783494985a51f6d5dbfac1f2dd /root/btc-forensics/tz26-work--logs--05-branch.log
[2026-10-10T20:41:53Z] R copied c4c779646d5e44a24ee0d65745460c67044f2a76f9005368c58001e302a7ecd4 /root/btc-forensics/tz26-work--logs--06-commit-push.log
[2026-10-10T20:41:53Z] R copied 8acca31e166d6ce46436a2f1a12eb9b3ef5ce23d135127e2baa9b1d946c08075 /root/btc-forensics/tz26-work--logs--07-pr.log
[2026-10-10T20:41:53Z] R copied 16a36ef4b36a19b724fceb21000008773cd9af085922f6943eef36ceaae93838 /root/btc-forensics/tz26-work--logs--08-selftest.log
[2026-10-10T20:41:53Z] R copied d5e809b9e7e13b09e652845c159293950156e311b9f8ee156648a50b714dd0a0 /root/btc-forensics/tz26-work--logs--09-still.log
[2026-10-10T20:41:53Z] R copied c3f5ce6c3f2b08fa7c94464400dce69358f9f240f169a07efefb98294de08bfd /root/btc-forensics/tz26-work--logs--10-scratch.log
[2026-10-10T20:41:53Z] R copied baded2cb623a0e28e37bb890a6c12d56e95cabfc683544c6a52fc1c136c31f22 /root/btc-forensics/tz26-work--logs--11-reclaim-scratch.log
[2026-10-10T20:41:53Z] R copied 5d521001543da460d9fc77c525a9ead9efc687fd8fe83c833d4720ae0e611d08 /root/btc-forensics/tz26-work--logs--12-rm-scratch.log
[2026-10-10T20:41:53Z] R copied cedec51c34d44b39ad0d16efe0ceeea45470c80beb4ec5f51ee1c7031af4d71d /root/btc-forensics/tz26-work--logs--13-svc-copy.log
[2026-10-10T20:41:53Z] R copied 17e42247b6f3d63ae916d3b052a1c7f61e9f100f82219b9c80dd7ab8974c5e30 /root/btc-forensics/tz26-work--logs--14-prestart.log
[2026-10-10T20:41:53Z] R copied 1c070fae1d4a826897e527dd9f59aa9da6399fc7c1eb7e73862586a95c1c2399 /root/btc-forensics/tz26-work--logs--15-install.log
[2026-10-10T20:41:53Z] R copied 448680d3d269e6b8c2a770bb33e968ee6d3c479ad855fa6c682dc06499c3bbad /root/btc-forensics/tz26-work--logs--16-mark-stop-cb.log
[2026-10-10T20:41:53Z] R copied e4a1f638339eda36ec0fc99626abf9971f4ccc0fdfadc9411bb3e0cd719656bc /root/btc-forensics/tz26-work--logs--17-mark-start-svc.log
[2026-10-10T20:41:53Z] R copied e1d962c241dbaa71583631e18b22e4832cddf96a242396ff5296fb1ab75236e0 /root/btc-forensics/tz26-work--logs--18-switch-refused.log
[2026-10-10T20:41:53Z] R copied 4b42224892905cd3b02d1f36abc288de5acbd393ff3b940d4861bb3d82e6049e /root/btc-forensics/tz26-work--logs--19-switch-boss.log
[2026-10-10T20:41:53Z] R copied 82268be880cb8bae8803c72810d8b4dee7b3a16c27fff63cc7cf699b9bddf12d /root/btc-forensics/tz26-work--logs--20-chainbook.log
[2026-10-10T20:41:53Z] R copied 26280e48b17d588340a895a755f951d3084857ba1ea8547908f5c4538a9dbddf /root/btc-forensics/tz26-work--logs--21-unit0.log
[2026-10-10T20:41:53Z] R copied 390e5c61aa11d7bfa8d7d53b62f621b0508d8c95fafdb078df1ccf96756b7411 /root/btc-forensics/tz26-work--logs--22-prove-1791664629.log
[2026-10-10T20:41:53Z] R copied 202b032f0b8f990f4b46732cb96a3e9adeb1b5ea1ac4e55e6188959a12a64beb /root/btc-forensics/tz26-work--logs--23-prove-again.log
[2026-10-10T20:41:53Z] R copied 897c3ec1bca24da3c8937e8d2780d468b9a7e70600265c9ca2f98e29c9a76cae /root/btc-forensics/tz26-work--logs--24-load.log
[2026-10-10T20:41:53Z] R copied 3eaf494c037073ccc7a40cf2eae88a75d2de7bc46e8dc51bf9d6b77985cb3a72 /root/btc-forensics/tz26-work--logs--25-mark-kill-svc.log
[2026-10-10T20:41:53Z] R copied bf19c89300c786345241b24e4e40da948cafbed18ac89c5be25726118cb7844f /root/btc-forensics/tz26-work--logs--26-kill-svc.log
[2026-10-10T20:41:53Z] R copied 268665a1f3efae1f0c1aab7fe2a5aa5078668c432561813ec954d9de82005745 /root/btc-forensics/tz26-work--logs--27-restart.log
[2026-10-10T20:41:53Z] R copied 9aea7d22da56d86610398e66a56fd50afe922f518cf325f8a7997b69b2868502 /root/btc-forensics/tz26-work--logs--28-final.log
[2026-10-10T20:41:53Z] R copied 1434e993c95c3692d3a7776d9b189397d13e8dc281e6189ab427e5716954b1b0 /root/btc-forensics/tz26-work--logs--29-closing.log
[2026-10-10T20:41:53Z] R copied 4b84e23ab265b010e50d7d64bf127e3cae301bc4e6bda5ca0557746bdc25096f /root/btc-forensics/tz26-work--logs--30-selfcheck.log
[2026-10-10T20:41:53Z] R copied 051b9b45666c3bc69925fd66a1f9c135d17325fbe2fde96815e0380f48ce3dcc /root/btc-forensics/tz26-work--logs--31-rate.log
[2026-10-10T20:41:53Z] R copied 9858cb8640441585a9272112b733667d77dacf16144754892454fbce3632d163 /root/btc-forensics/tz26-work--logs--32-files.log
[2026-10-10T20:41:53Z] R copied 02b252af1411143a0baf85096a1c5ddb9d12034192f3caf323062f9e551e9d85 /root/btc-forensics/tz26-work--prestart--prestart.json
[2026-10-10T20:41:53Z] R copied b1cd8024d3ac3214637fcf3528618f1286b85a8b4118a47bf0a7c1428babfa9d /root/btc-forensics/tz26-work--prestart--stream.jsonl.gz
[2026-10-10T20:41:53Z] R copied 33813e2d36f28381b1072a5743c957fd798ecd3c5fc98558b44941f4f022aedb /root/btc-forensics/tz26-work--proof--proof-1791664629.json
[2026-10-10T20:41:53Z] R copied ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8 /root/btc-forensics/tz26-work--stage--deploy--systemd--btc-pairbook.service
[2026-10-10T20:41:53Z] R copied caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec /root/btc-forensics/tz26-work--stage--research--tz26-nesting-b3-capture.py
[2026-10-10T20:41:53Z] RECLAIM PASS: 41 files considered, 41 named by a report, 0 kept by name, 41 copied, 0 already held; forensic store 1725 -> 1766 files
[2026-10-10T20:41:53Z] peak memory of this run: 37085184 bytes
[2026-10-10T20:41:53Z] opens refused: 0; manifest opens attempted 0; chain book opens 0; requests 0, stream sessions 0
exit=0
```

```text
$ git -C /root/btc-5m-twap worktree remove /root/tz26-work/wt; echo "exit=$?"
exit=0
```

```text
$ rm -rf /root/tz26-work; echo "exit=$?"
exit=0
```

```text
$ test -e /root/tz26-work; echo "exit=$?"
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
$ find /root/btc-forensics -type f | wc -l
$ df -B1 --output=source,size,avail /var/lib/btc-recorder; date -u +%FT%T.%NZ
exit=1
/root/btc-5m-twap       73da754 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
1766
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12931072000
2026-10-10T20:41:59.028833693Z
```

- **`reclaim`:** `RECLAIM PASS`, 41 files considered and 41 named by this report's draft. All 41 were copied and 0 already held. The store went from `1,725` to **`1,766`**, which is the 1,725 before plus the 41 copies (V18).
- **The worktree:** `/root/tz26-work/wt` was pristine, so `reclaim` skipped it, and `git worktree remove` without `--force` exited `0`.
- **The tree:** `rm -rf /root/tz26-work` exited `0` and was **not refused by the classifier**. `test -e` then reads `exit=1`.
- **Worktrees left:** `/root/btc-5m-twap` and `/root/btc-recorder-svc`, and nothing else (V19).
- **Free space:** `12,931,072,000` bytes at 20:41:59 UTC.

**Kept:** `/root/btc-pairbook-svc/`, `/root/btc-recorder-svc/` and `/root/tz18a-svc/`; the three capture roots; the forensic store. This session's own directory, `30ec6406…`, and the live `d5dc7bd3…` are the next TZ's.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-26-nesting-b3-capture` at `e8b46a85d61e1a17841962846f6d3012046c2d70`, on `origin` and kept as a local ref |
| commit | one, holding the two files of Appendix A and nothing else |
| pull request | #25, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/25`, open, not merged |
| Release | none; TZ-26 creates none |
| report | `CryptoReports/TZ-26-nesting-b3-capture-report.md`, straight to `main`, one commit |
| deployment | `btc-pairbook.service`, enabled and running from `/root/btc-pairbook-svc/` at `e8b46a8`; `btc-chainbook.service` disabled, and its unit file and `/root/tz18a-svc/` kept |

Contract §4.2's self-check, verbatim: §2.15 (`0`; the two paths; nothing).

---

## 4. Gate

| gate | PASS when (TZ §4) | read | deciding number | reading |
|---|---|---|---|---|
| P-START | §4.1 | 3 requests, 1 session, 7 of 7 | 7/7 = `1.000` | **served** |
| G-CB-STOP | §4.1 | 4 of 4 | `1.000` | **PASS** |
| G-UNIT, 0 restarts | §4.1 | 10 of 10 | `1.000` | **PASS** |
| G-START | §4.1 | 7 of 7 | `1.000` | **PASS** |
| G-STREAM | at least 3 of 4 complete | 4 of 4 | `1.000` | **PASS** |
| G-BOOKS | at least 26 of 28 complete | 28 of 28 | `1.000` | **PASS** |
| G-TIERC | no counted failure, and at least 2 counted fully loaded | 0 failures, 4 counted fully loaded | 4 ≥ 2 | **PASS** |
| G-LOAD | at most 1/4 of a core | `0.0174` | `0.017` | **PASS** |
| G-RESTART | a stop of the marked pid, and a start within 60 s | 5.480 s | `5.480` | **PASS** |
| G-UNIT, 1 restart | §4.1 | 10 of 10 | `1.000` | **PASS** |
| G-STILL | the recorder unchanged | `4148534` / 2 / `active` at both reads | — | **PASS** |

No threshold was tuned and no gate was reinterpreted. **Under PASS, neither K-26 nor B-RESTORE-CB ran**, and `restored` did not run.

---

## 5. Validation

| # | check | count | asserted |
|---|---|---|---|
| V1 | §0.2's fingerprint | `FINGERPRINT PASS`; anchors 6 of 6, 4 re-derived; 34 rows, 31 of 31 `frozen` equal | asserted by the instrument |
| V2 | §0.3's host gate | H1 to H5, memory and disk, 7 of 7; the rest printed | read by the Executor against the TZ's conditions from the verbatim log; the commands assert nothing themselves |
| V3 | §0.1's and §3.1's files | 2 of 2 hashes at each, lines and bytes equal; the diff names exactly these two paths, both `A` | the hashes asserted by the script; the diff read from `git diff --name-status` |
| V4 | the self-test | `74 of 74` | asserted |
| V5 | §3.4's copy | 2 of 2 hashes equal; `commit.txt` equal to `HEAD` | read from `sha256sum` and `rev-parse`, not asserted |
| V6 | P-START | `READING P-START: served`; 3 requests, 1 session; 7 of 7; `m` 1,864, `f` 1, false alarm `0.0021441965` | asserted |
| V7 | B-INSTALL | `cmp` exit 0; `daemon-reload` exit 0; `verify` exit 0, no finding | exit codes read |
| V8 | G-CB-STOP | 4 of 4; the stop at 19:30:06 UTC, 6 s into its window, inside its idle stretch | asserted |
| V9 | G-UNIT and G-START at `unit 0`; G-UNIT at `unit 1` | 10 of 10 and 7 of 7; 10 of 10 (at `restart` and at `final`) | asserted |
| V10 | G-STREAM, G-BOOKS, G-TIERC | 4 of 4; 28 of 28; 4 counted fully loaded, 0 failures; every considered window, every checkpoint, 4 exposed and 7 control intervals printed | asserted |
| V11 | determinism | `unchanged`; `33813e2d36f28381b1072a5743c957fd798ecd3c5fc98558b44941f4f022aedb` | asserted |
| V12 | G-LOAD | `0.0174` against `0.25`; the memory reads | asserted |
| V13 | G-RESTART | stop `746785` at 20:37:44, start `752775` at 20:37:49, 5.480 s | asserted |
| V14 | G-STILL | the recorder unchanged | asserted |
| V15 | opens under the capture roots | refused 0 at every mode. Manifest opens: `prestart` 2,016; each deciding `prove` 15, within 25; 0 NOT YET runs. Chain book opens: 1 by `chainbook`, 0 elsewhere; `restored` did not run | counted by the audit hook, printed |
| V16 | contract §4.2's self-check | `0`; two paths; nothing — after the push and the pull request, before the report's commit | printed |
| V17 | §3.11's closing reads | every read printed, §2.15 | printed |
| V18 | §9's `reclaim` runs | scratch: 0 considered, store 1,725 → 1,725; own: 41 considered, 41 named, 41 copied, 0 held, store 1,725 → 1,766 | asserted by `reclaim` (`RECLAIM PASS`) |
| V19 | §9's removals | two scratch directories, `rm -rf` exit 0 and `test -e` exit 1 each; own: `worktree remove` exit 0, `rm -rf` exit 0, `test -e` exit 1, worktrees `/root/btc-5m-twap` and `/root/btc-recorder-svc` only | read from exit codes |

---

## 6. What could not be implemented as written

1. **Contract §1's pull ran before §0.0**, as in TZ-21, TZ-23 and TZ-24 (map §7 item 102). It moved `main` from `2cd8fcd` to `73da754`. The Executor also read the remote's state before §0.0, with `git fetch`, `git branch -a`, `git worktree list` and a listing of `/root`, `/tmp` and the session directories. That was to find where an earlier, interrupted start of this session had stopped. That start had written nothing: no tree, no branch, no file.
2. **§0.0's output was first written to the session's scratchpad**, because `logs/` did not exist until that `mkdir` ran. It was moved into `logs/00-workdir.log` 5 s later. `logs/00-pull.log` records `main`'s state after the pull, a step the TZ does not name.
3. **B-SWITCH ran 10 s before its band.** The classifier refused the block ("[Production Deploy]"). The Executor handed it to the Boss with the band as UTC clock ranges, the first one at 19:30:15 for this window. The Boss ran it at 19:30:05.8 UTC, second 5 of window `1791660600`.
   - **What §3.7 requires:** a second between 15 and 420. **Where the stop fell:** at the chain book's `T + 905` for window `1791659700`, which is when it writes `window.json`. The instrument reads the stop as inside the chain book's idle stretch, 6 s into its window, and G-CB-STOP passed 4 of 4.
   - **Unread:** whether the chain book wrote `window.json` for `1791659700` before it stopped. §2 item 3 forbids listing its root.
   - **The pair book's first window was unaffected:** its documents were 539 s ahead.
   - No gate reads the band, and the Executor does not read it as a FAIL; it is disclosed for the Architect.
4. **The Executor read `/var/lib/btc-pairbook/runtime.jsonl` with `head -c 2000`**, outside the instrument, at 19:30:39 UTC, to see the service's start. §2 item 4 allows reads there only by the named modes and §3.11's `tail` and `du`. What printed was the service's first `start` record — `argv`, `commit`, `config`, `file_sha256`, `free_bytes`, `pid`, times — a file §1 excepts from the reserve. No price, size, side, book hash or outcome was read or printed.
5. **Other reads the TZ does not name**, none under a capture root:
   - `ps -eo pid,lstart,args | grep claude`, after `I scratch`.
   - `journalctl -u` of both units at 19:30:39, which §2 item 5 allows, to find when the Boss's block ran.
   - `get_session`, for the model.
   - Reads of the instrument's source and of the TZ-24 report's structure.
6. **B-KILL-SVC ran inside a phase guard:** `if` the window's second lay between 15 and 480, run the block's line verbatim, `else` print and skip. The guard was added because the mark was taken at second 459 and the band closed at 480. The line ran at second 464.
7. **§2.10's rate and days to the cap come from a short script, not from the instrument.** TZ §8 asks for them, and the instrument prints the counts but no rate. The script reads `proof/proof-1791664629.json`, which is the instrument's own output, and its output is `logs/31-rate.log`. Its arithmetic:
   - frames divided by each window's span from first subscribe to last close;
   - stored stream bytes averaged over the four windows;
   - `8,000,000,000 / (mean × 96)`.
8. **The report is assembled** from a template in `/root/tz26-work/` and the `logs/` files, inserted verbatim by a script, before B-RECLAIM-OWN. B-RECLAIM-OWN's output is then inserted verbatim from the session, as §9 requires.
9. **B-RECLAIM-OWN ran as four commands in four tool calls**, as TZ-24's did (map §7 item 102). The checks after the removal ran as one command. Every output is quoted verbatim in §2.17. **No command of B-RECLAIM-SCRATCH or B-RECLAIM-OWN was refused by the classifier.** The only refused block was B-SWITCH, run by the Boss (item 3).
