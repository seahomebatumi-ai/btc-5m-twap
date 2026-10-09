# TZ-23 report — M0: do the makers earn?

**M0 READING: UNDECIDABLE.** The set is the first 4,032 qualifying five-minute markets from `1788530400`,
2026-09-04 14:00 UTC, to `1791241800`, 2026-10-05 23:10 UTC. Every candidate qualified, 1,329 members fall on a
weekend, and the member list is `699cab9a…`. The window `[T0, T0 + 240)` holds `4,820,537` taker fills and
`129,225,737.55` shares. On those fills the makers' result at settlement, with the 20% rebate, is
**`S` = `272,424.113` USDC**, `0.211` c a share. It splits into `−17,171.507` at settlement (`−0.013` c a share) and
`+289,595.620` of rebate (`+0.224` c a share). EARN needed `S >= 432,484.391` (`0.335` c a share), and NO EARN needed
`S <= 213,644.297` (`0.165` c a share). **Neither holds.** Each answer was tested at `α = 0.005` by Ville's
inequality, with the power `0.947` printed before any label. TZ §1 item 3: UNDECIDABLE opens the second look.

**Every gate before the reading passed.** The self-test passed **59 of 59** · G-REHEARSAL **10 of 10** figures equal
to the Architect's · G-SET **4,032** members of 4,032 considered, 202 chunks read back · the constants **3 of 3** files
`unchanged` at the second run · the rebate check **64 of 64** sampled members' taker rows equal to the cache · the
score **2 of 2** files `unchanged`, **2** ledger lines · G-STILL PASS: the recorder `4148534` / `NRestarts` 2, the
chain book `4064090` / `NRestarts` 1, unchanged.

**The labels were read once a run, by `score`, at 19:16:41 and 19:16:52 UTC.** That was after the constants
`1b28df43…` were on disk with their SHA-256 in `state.json` (19:13:16 UTC) and after the instrument's commit
`7f5ae3f` was on `origin` (before 18:43:54 UTC). **No command was refused by the session's classifier.**
B-RECLAIM-SCRATCH's `reclaim` and three `rm -rf`, and B-RECLAIM-OWN's lines, ran as the Executor's own commands, so
no block was handed to the Boss.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-23-maker-m0.md`, 1,811 lines, 101,194 bytes, SHA-256 `1aedbba8991453f2a07b978e391b8c03c77cd4c76d6d780d6f4c27d51d28dec0`, landed at `3561850` |
| map revision | `2026-10-05-a`, equal; anchors 6 of 6; re-derived 4 of 4; rows hashed 32; `frozen` equal 29 of 29 |
| executor model | Opus, as the TZ names: `get_session` read `session_context.model` and `last_served_model` `claude-opus-5-5` |
| branch | `tz-23-maker-m0` at `7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8`, pushed; pull request #23, open, not merged |
| instrument | `research/tz23-maker-m0.py`, 1,184 lines, 54,885 bytes, SHA-256 `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f`, Appendix A byte for byte |
| interpreter | `/root/tz04a-env/venv/bin/python` 3.12.3, every mode under `nice -n 19` and `-B` |
| requests | `gamma-api.polymarket.com/markets` and `data-api.polymarket.com/v2/trades`, through the instrument's `http_json` alone, with `User-Agent: btc-5m-twap-m0/TZ-23` and `Accept: application/json`; `git` against `origin`; `gh` for the pull request |
| capture | not read. The only commands that touched a capture root were §0.2's `df`, `find` and `grep -c`, at both runs, and B-RECLAIM-OWN's `df`. The self-test's one attempted open of `/var/lib/btc-recorder/runtime.jsonl` was refused by the audit hook before it happened, which is that check's purpose. Every mode printed `opens under the capture roots: 0` |
| units | `btc-recorder.service` and `btc-chainbook.service`, read with `systemctl show` and `is-active` alone, never signalled |
| pricer | not read, not called, not scored; `A6` `729f0bcdbee3` is stated so that what was not scored is not in doubt |

No single fill's, member's or market's price, size or outcome is printed in this report or anywhere outside
`/root/tz23-work/`, except in §9's byte-for-byte copies into `/root/btc-forensics/`. Every figure below is a sum
over a set copied from the instrument's own output, or a rounding or a ratio of such figures, named where it
is one.

---

## 0. Fingerprint

**Revision string read:** `2026-10-05-a`, equal to the value TZ-23's header requires. The session's first
`git fetch origin main` and `git merge --ff-only origin/main` moved local `main` from `c8636f7` to
`3561850d31eb6f9ed30c097a63d251a1709c4442` before the TZ was read, and before §0.0's `mkdir`, so no log holds them.
Contract §1's `git checkout main && git pull` was run again for the record after the `mkdir`
(`logs/00d-pull.log`). The map and the TZ were read at `3561850`.

§0.0's `mkdir` (`logs/00a-worktree.log`):

```text
$ mkdir /root/tz23-work /root/tz23-work/logs; echo "exit=$?"
exit=0
(run at 2026-10-09T18:40:36Z, after contract §1 steps 1-2: local main fast-forwarded to origin/main)
HEAD 3561850d31eb6f9ed30c097a63d251a1709c4442 2026-10-09T22:35:52+04:00
0
```

Contract §1 step 1, re-run (`logs/00d-pull.log`):

```text
$ git checkout main && git pull   (2026-10-09T18:45:44Z; contract §1 step 1, re-run for the record - the session's first git fetch origin main and git merge --ff-only origin/main had moved local main from c8636f7 to 3561850 before the TZ was read, before §0.0's mkdir)
Already on 'main'
Your branch is up to date with 'origin/main'.
Already up to date.
exit=0
3561850d31eb6f9ed30c097a63d251a1709c4442
```

Contract §1 step 5, the model (`logs/00c-model.log`):

```text
contract §1 step 5 - the model the TZ names: Opus
get_session (claude-code-remote), 2026-10-09T18:41:24Z: session_context.model claude-opus-5-5, external_metadata.last_served_model claude-opus-5-5, configured_model claude-opus-5-5
CLAUDE_CODE_SESSION_ID=5ce9f787-ea2c-5497-8888-63b97cb927e8 CLAUDE_PID=618175
1aedbba8991453f2a07b978e391b8c03c77cd4c76d6d780d6f4c27d51d28dec0  /root/btc-5m-twap/CryptoTZ/TZ-23-maker-m0.md
  1811 101194 /root/btc-5m-twap/CryptoTZ/TZ-23-maker-m0.md
```

| anchor | required | read from the map | re-derived from the file | verdict |
|---|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | not a file anchor | equal |
| `A2` — collector | `6c5089330629` | `6c5089330629` | `6c5089330629` | equal |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | same | not a file anchor | equal |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | `437b45ea196b` | equal |
| `A5` — recorder | `0f6c90451cbd` | `0f6c90451cbd` | `0f6c90451cbd` | equal |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3` | `729f0bcdbee3` | equal |

### 0.1 The 32 rows of the map's §0 table (V1)

The table was parsed from the map at `3561850`, and every path was hashed in the primary checkout. Each `frozen`
row was compared in lines, bytes and SHA-256 against the map. The script prints `PASS` only when there are 32 rows,
29 `frozen` / 2 `tracked` / 1 `reported`, the revision is `2026-10-05-a` and nothing mismatches. Its output,
verbatim (`logs/00b-fingerprint.log`):

```text
$ fingerprint, TZ-23 §0.1, from /root/btc-5m-twap at 3561850d31eb6f9ed30c097a63d251a1709c4442
revision string: 2026-10-05-a required 2026-10-05-a EQUAL
anchor A1 map 229a944f2d51 TZ 229a944f2d51 EQUAL
anchor A2 map 6c5089330629 TZ 6c5089330629 EQUAL
anchor A3 map 0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable TZ 0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable EQUAL
anchor A4 map 437b45ea196b TZ 437b45ea196b EQUAL
anchor A5 map 0f6c90451cbd TZ 0f6c90451cbd EQUAL
anchor A6 map 729f0bcdbee3 TZ 729f0bcdbee3 EQUAL
re-derived A2 research/twap-divergence.py sha256[:12] 6c5089330629 EQUAL
re-derived A4 BTC-EXECUTOR-INSTRUCTIONS.md sha256[:12] 437b45ea196b EQUAL
re-derived A5 research/recorder/recorder.py sha256[:12] 0f6c90451cbd EQUAL
re-derived A6 research/pfair.py sha256[:12] 729f0bcdbee3 EQUAL
rows in the §0 table: 32
SYSTEM-MAP.md                                  1160 lines  246032 bytes 7cc5a49181ea0b4f5162bc55d320d18268aa107d75c45e5f10c0bc24c4e464fe reported (map: — lines, — bytes, self-reference; report the value you compute)
BTC-EXECUTOR-INSTRUCTIONS.md                    234 lines   11128 bytes 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b frozen EQUAL
research/twap-divergence.py                    1135 lines   50928 bytes 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 frozen EQUAL
research/selftest-twap-divergence.py            376 lines   16736 bytes ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a frozen EQUAL
research/tz02-distribution.py                   334 lines   14511 bytes f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 tracked (map: 334 lines, 14,511 bytes, `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4`)
research/pfair.py                               441 lines   19357 bytes 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 frozen EQUAL
research/selftest-pfair.py                      619 lines   32559 bytes b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa frozen EQUAL
research/tz06-calibration.py                    577 lines   27138 bytes 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f frozen EQUAL
research/tz07a-variance-time.py                 623 lines   28414 bytes 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 frozen EQUAL
research/tz07b-settlement-dispersion.py         515 lines   24926 bytes 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc frozen EQUAL
research/tz08a-out-of-sample.py                 745 lines   38822 bytes 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c frozen EQUAL
research/tz09-disk-inventory.py                 894 lines   41004 bytes b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 frozen EQUAL
research/tz10b-sigma-or-link.py                1224 lines   61018 bytes 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 frozen EQUAL
research/tz11a-student-link.py                 1231 lines   64732 bytes 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 frozen EQUAL
research/tz12-sized-gate.py                    1157 lines   61637 bytes d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 frozen EQUAL
research/tz13-sized-gate-test3.py              1074 lines   53901 bytes a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd frozen EQUAL
research/tz14-quote-inventory.py               2124 lines  109972 bytes 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 frozen EQUAL
research/tz15-phase2-gate.py                   1517 lines   73799 bytes 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 frozen EQUAL
research/tz16a-phase2-decisive-gate.py         2198 lines  111192 bytes 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 frozen EQUAL
research/tz17-settlement-chain.py              1102 lines   38622 bytes e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 frozen EQUAL
research/tz18a-chainbook-capture.py            1683 lines   69517 bytes e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae frozen EQUAL
research/tz20-capture-under-systemd.py          771 lines   36528 bytes 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7 frozen EQUAL
research/tz21-recorder-memory.py               1284 lines   59009 bytes d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f frozen EQUAL
research/recorder/recorder.py                   651 lines   27821 bytes 0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7 frozen EQUAL
research/recorder/config.py                     112 lines    4773 bytes 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d frozen EQUAL
research/recorder/manifest.py                   254 lines   10002 bytes 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 frozen EQUAL
research/recorder/analyze.py                    813 lines   34705 bytes eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d frozen EQUAL
research/recorder/probe.py                      227 lines    9324 bytes 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 frozen EQUAL
research/recorder/selftest.py                   573 lines   30591 bytes c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 frozen EQUAL
deploy/systemd/btc-recorder.service              23 lines     707 bytes 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1 frozen EQUAL
deploy/systemd/btc-chainbook.service             22 lines     724 bytes a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2 frozen EQUAL
.gitignore                                        5 lines     252 bytes 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b tracked (map: 5 lines, 252 bytes, `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b`)
states: {'frozen': 29, 'tracked': 2, 'reported': 1} ; frozen equal 29 of 29
FINGERPRINT PASS - mismatches: 0
```

`SYSTEM-MAP.md` is the `reported` row: 1,160 lines, 246,032 bytes, SHA-256
`7cc5a49181ea0b4f5162bc55d320d18268aa107d75c45e5f10c0bc24c4e464fe`. The two `tracked` rows equal the map's printed
values as well.

### 0.2 Host gate — the opening reads, verbatim (V2)

`S` was set to this session's scratchpad directory,
`/tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8/scratchpad`, as the session's system prompt
names it. No environment variable names it; `CLAUDE_CODE_SESSION_ID` is `5ce9f787-ea2c-5497-8888-63b97cb927e8`,
the same directory (§6 item 2). The block ran from `/root/btc-5m-twap` (`logs/01-host-gate.log`):

```text
$ S=/tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8/scratchpad
$ date -u; date -u +%s
Fri Oct  9 06:41:39 PM UTC 2026
1791571299
$ nproc; grep -E ... /proc/meminfo
1
MemTotal:         978640 kB
MemAvailable:     249084 kB
SwapTotal:       3174396 kB
SwapFree:        2877660 kB
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13089144832
$ find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
$ grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
1
$ systemctl is-active btc-recorder.service btc-chainbook.service; echo "exit=$?"
active
active
exit=0
$ systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1
$ systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3
$ git -C /root/btc-recorder-svc rev-parse HEAD
e3975b5da44c5328adf3bf3914634cd878842c73
$ for d in /root/tz21-work /root/tz18a-svc /root/btc-recorder-svc; do test -e "$d"; echo "$d exit=$?"; done
/root/tz21-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
$ find /root/btc-forensics -type f | wc -l
1519
$ /root/tz04a-env/venv/bin/python -c ...
3.12.3
$ git worktree list
/root/btc-5m-twap       3561850 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ du -sb /root/.claude /root/PROJECT_GAMING_PS5
191315041	/root/.claude
521397062	/root/PROJECT_GAMING_PS5
$ echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
/tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8/scratchpad
total 28
drwx------  7 root root 4096 Oct  9 18:39 .
drwx------ 16 root root 4096 Oct  9 18:39 ..
drwx------  3 root root 4096 Oct  4 19:04 386a2f9a-9175-46e4-af0d-52cc5355a34c
drwx------  4 root root 4096 Oct  9 18:39 5ce9f787-ea2c-5497-8888-63b97cb927e8
drwx------  3 root root 4096 Oct  9 18:39 750b3996-3a2d-49fb-823d-1321cd631528
drwx------  3 root root 4096 Oct  4 22:04 9b05d639-af52-44b6-9a8c-9f508f7b17c4
drwx------  4 root root 4096 Oct  4 22:04 f1dda509-7343-505e-8afa-097e9a463ab6
```

| gate | required | read | verdict |
|---|---|---|---|
| **H1** | `find` prints exactly one path | one path, `/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json` | PASS |
| **H2** | source `/dev/vda2`, size `31612203008`; `grep -c` at least `1` | `/dev/vda2`, `31612203008`; `1` | PASS |
| **H3** | the interpreter prints `3.12.` | `3.12.3` | PASS |
| **memory gate** | `MemAvailable` at least `147,152,896` bytes | `249,084` kB = `255,062,016` bytes | PASS |
| **disk gate** | `avail` at least `2,400,000,000` bytes | `13,089,144,832` | PASS |

**Printed, no threshold:** both capture units `active` (exit 0); `telemetry-watch.service` `disabled` (exit 1) and
`inactive` (exit 3), so map §6's headroom condition holds; the recorder's tree at
`e3975b5da44c5328adf3bf3914634cd878842c73`, as map §6 has it; `/root/tz21-work` absent (exit 1),
`/root/tz18a-svc` and `/root/btc-recorder-svc` present (exit 0); the forensic store at `1,519` files, map §3's
count; two worktrees, the primary checkout and `/root/btc-recorder-svc`; `/root/.claude` at `191,315,041` bytes and
`/root/PROJECT_GAMING_PS5` at `521,397,062`; and five UUID directories in `S`'s parent, which `I scratch` named
(§2.3).

### 0.3 Free space and `MemAvailable` — every read, its instant and its bound (§0.3)

**Free space on `/dev/vda2`**, bound `2,400,000,000` bytes (§0.3):

| read | instant, UTC | `avail`, bytes | against the bound |
|---|---|---|---|
| §0.2 host gate | 2026-10-09 18:41:39 | `13,089,144,832` | above |
| §3.10 closing reads | 2026-10-09 19:17:15 | `12,999,884,800` | above |
| B-RECLAIM-OWN's `df` | 2026-10-09 19:23:06 | `13,043,306,496` | above |

From the first read to the second, free space fell `89,260,032` bytes. `/root/tz23-work` held `86,613,760` at the
second, against §0.3's estimate of at most about `97,500,000`.

**`MemAvailable`**, floor `147,152,896` bytes (§0.3):

| read | instant, UTC | bytes | against the floor |
|---|---|---|---|
| §0.2 host gate, `/proc/meminfo` | 18:41:39 | `255,062,016` (`249,084` kB) | above |
| `rehearse`'s `floor_check` | 18:45:04 | `284,483,584` | above |
| `fetch`'s `floor_check` | 18:45:30 | `272,838,656` | above |
| `constants`'s `floor_check`, first run | 19:12:26 | `294,424,576` | above |
| `constants`'s `floor_check`, second run | 19:13:27 | `295,604,224` | above |
| `rebate`'s `floor_check` | 19:14:28 | `316,141,568` | above |
| §3.10, `/proc/meminfo` | 19:17:15 | `317,898,752` (`310,448` kB) | above |
| §3.10, `free -b` `available` | just after 19:17:15 | `327,110,656` | above |

The lowest read, `255,062,016`, was the opening one, `1.73` times the floor. Each figure is as it was printed.

### 0.4 Refs (§0.4)

Run before the branch of §3.1 existed (`logs/02-refs.log`):

```text
$ git ls-remote origin   (2026-10-09T18:41:53Z)
3561850d31eb6f9ed30c097a63d251a1709c4442	HEAD
3561850d31eb6f9ed30c097a63d251a1709c4442	refs/heads/main
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
ee2f6327390ef4d0c6169d1fba1a2ed4ae936dc3	refs/pull/3/head
0e13a5c76dfa2469ff25b3b0dd282872decf6f25	refs/pull/4/head
4216c04673ced76b5b2ac60ef57c9abedc46f9b9	refs/pull/5/head
5ed667afd1b53f036b9f938fcce13c0d709cd77f	refs/pull/6/head
c44af687203d14d5d485d4297c04cfb827096af9	refs/pull/7/head
26bbb61aed774a88355dd5204d8b69fda9135a68	refs/pull/8/head
e2625ea2b5473c311d59a48f32540ce39d58e591	refs/pull/9/head
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
ref lines: 26

$ git ls-remote origin refs/heads/tz-23-maker-m0 | wc -l
0

$ main first-parent line above e1095b4, with paths
3561850d31eb6f9ed30c097a63d251a1709c4442 2026-10-09T22:35:52+04:00 𝒜𝒱777𝒮𝒜 Add files via upload
0e8734334b52134fe474a960f7776bfca21dd71a 2026-10-09T22:35:17+04:00 𝒜𝒱777𝒮𝒜 Update SYSTEM-MAP.md
-- 3561850d31eb6f9ed30c097a63d251a1709c4442
A	CryptoTZ/TZ-23-maker-m0.md
-- 0e8734334b52134fe474a960f7776bfca21dd71a
M	SYSTEM-MAP.md

$ revision string on origin/main
**Revision string:** `2026-10-05-a`
$ local branch tz-23-maker-m0
exit=1
```

**26 ref lines**, as map §1 records. **Recorded, not BLOCKING:** `main` is at
`3561850d31eb6f9ed30c097a63d251a1709c4442`, not map §1's `e1095b44d3d1391f9f352ad11f1356e7b1678d1d`. The two
commits above `e1095b4` on `main`'s first-parent line are the Architect's upload: `0e87343` changes `SYSTEM-MAP.md`
alone (revision `2026-10-05-a`), and `3561850` adds `CryptoTZ/TZ-23-maker-m0.md` alone. `main` carries revision
`2026-10-05-a`, and `refs/heads/tz-23-maker-m0` did not exist on `origin` or locally. Neither BLOCK condition holds.

---

## 1. Input

| input | what | size | hash |
|---|---|---|---|
| the specification | `CryptoTZ/TZ-23-maker-m0.md` at `3561850` | 1,811 lines, 101,194 bytes | `1aedbba8991453f2a07b978e391b8c03c77cd4c76d6d780d6f4c27d51d28dec0` |
| the map | `SYSTEM-MAP.md`, revision `2026-10-05-a` | 1,160 lines, 246,032 bytes | `7cc5a49181ea0b4f5162bc55d320d18268aa107d75c45e5f10c0bc24c4e464fe` |
| the contract | `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 lines, 11,128 bytes | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` |
| the set's documents | gamma `/markets?slug=…&closed=true`, 202 requests of at most 20 slugs — ⌈4,032 / 20⌉, every candidate a member, so the walk's chunks were never cut short (the instrument prints no request count): 4,032 candidates, each kept as `kept_doc`'s nine fields | `set/set.json`, 2,314,799 bytes | `a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303` |
| the set's taker fills | `/v2/trades?condition=…&taker_only=true&limit=1000`, 202 chunks of at most 20 condition ids, every page re-sending both filters; `6,013,558` rows over the seven bands (the sum of §2.7's band counts), `4,820,537` of them in the window | `set/tz23-fills.jsonl.gz`, 36,870,673 bytes; the cache, 202 files, 37,239,598 bytes | `4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64` |
| the rehearsal's documents | 8 gamma requests: the 144 markets `1791050100` … `1791093000` | `rehearsal/set.json`, 82,728 bytes | `83a53bd3fb13829173282487833ef0398280d358377e0f09d0beb414c7829cbc` |
| the rehearsal's taker fills | 8 chunks; `165,315` rows over the seven bands, `128,031` in the window | `rehearsal/rehearsal-fills.jsonl.gz`, 1,055,371 bytes; the cache, 8 files, 1,068,929 bytes | `3ce50a85f84068a4cac15ece53d2ea1b16184b9080d69228b0baae8f887c8116` |
| the rebate sample | 64 members, both feeds again — `taker_only=true` and `false`, with transaction and wallet — read and summed in memory | not kept | — |

The instrument prints no count of pages or HTTP requests for the fills, so none is given here. The rehearsal's
`165,315` rows equal TZ §6's figure for the same span.

**Collected, not re-collected.** Every document and fill was read from the venue's public endpoints during this
session, through the instrument. The rehearsal span was read before by the Architect, on 2026-10-05 and 2026-10-09
(TZ §1, data hygiene). No member of the set had been read by anyone (TZ §1), and no read of a member's document or
fills was made by any command but the instrument's modes. **Nothing under `/var/lib/btc-recorder/` or
`/var/lib/btc-chainbook/` was opened**, and no committed report's data was reused.

---

## 2. Measurements

### 2.1 §3.1 — the branch and its file (V3)

`logs/03-branch.log`:

```text
$ git -C /root/btc-5m-twap fetch origin
exit=0
$ git -C /root/btc-5m-twap worktree add -b tz-23-maker-m0 /root/tz23-work/wt origin/main
Preparing worktree (new branch 'tz-23-maker-m0')
branch 'tz-23-maker-m0' set up to track 'origin/main'.
HEAD is now at 3561850 Add files via upload
exit=0
wt HEAD 3561850d31eb6f9ed30c097a63d251a1709c4442
```

§3.1's extraction script, verbatim from the TZ, run as `/root/tz04a-env/venv/bin/python -B -` (`logs/04-extract.log`):

```text
$ (TZ-23 §3.1 extraction script, verbatim)
research/tz23-maker-m0.py 1184 54885 6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f
exit=0
$ wc -l -c; sha256sum
 1184 54885 /root/tz23-work/wt/research/tz23-maker-m0.py
6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f  /root/tz23-work/wt/research/tz23-maker-m0.py
```

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/tz23-maker-m0.py` | 1,184 | 54,885 | `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` |

The script asserted the one hash; `wc` reads the TZ's 1,184 lines and 54,885 bytes. The commit, the diff against
`origin/main` and the push (`logs/05-commit-push.log`):

```text
$ git add research/tz23-maker-m0.py && git commit
exit=0
commit 7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8 2026-10-09T18:43:30+00:00
$ git diff --stat origin/main HEAD
 research/tz23-maker-m0.py | 1184 +++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 1184 insertions(+)
A	research/tz23-maker-m0.py
$ git push -u origin tz-23-maker-m0
remote: 
remote: Create a pull request for 'tz-23-maker-m0' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-23-maker-m0        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-23-maker-m0 -> tz-23-maker-m0
branch 'tz-23-maker-m0' set up to track 'origin/tz-23-maker-m0'.
exit=0
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8
```

The pull request (`logs/06-pr.log`):

```text
$ gh pr create --base main --head tz-23-maker-m0
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/23
exit=0
PR #23 https://github.com/seahomebatumi-ai/btc-5m-twap/pull/23 head 7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8 OPEN base main
```

The diff names exactly one path, `A`, 1,184 insertions.

### 2.2 §3.2 — the self-test (V4)

`I selftest` (`logs/07-selftest.log`):

```text
$ I selftest
[2026-10-09T18:43:53Z]   ok  glibc took the 128 KiB mmap threshold and the two arenas
[2026-10-09T18:43:53Z]   ok  makers' result is minus the taker's: B U up=0
[2026-10-09T18:43:53Z]   ok  makers' result is minus the taker's: B U up=1
[2026-10-09T18:43:53Z]   ok  makers' result is minus the taker's: S U up=0
[2026-10-09T18:43:53Z]   ok  makers' result is minus the taker's: S U up=1
[2026-10-09T18:43:53Z]   ok  makers' result is minus the taker's: B D up=0
[2026-10-09T18:43:53Z]   ok  makers' result is minus the taker's: B D up=1
[2026-10-09T18:43:53Z]   ok  makers' result is minus the taker's: S D up=0
[2026-10-09T18:43:53Z]   ok  makers' result is minus the taker's: S D up=1
[2026-10-09T18:43:53Z]   ok  a taker buying Down at 0.01 leaves makers long 100 Up at 0.99
[2026-10-09T18:43:53Z]   ok  a taker selling Down at 0.01 leaves makers short 10 Up at 0.99
[2026-10-09T18:43:53Z]   ok  a 100-share Down purchase at 0.01: makers +1.00 on Up and -99.00 on Down
[2026-10-09T18:43:53Z]   ok  rebate of 100 shares at 0.50 is 0.35 USDC
[2026-10-09T18:43:53Z]   ok  rebate of 100 shares at 0.99 is 0.01386 USDC
[2026-10-09T18:43:53Z]   ok  the rebate is symmetric in p
[2026-10-09T18:43:53Z]   ok  0.014 = 0.07 * 0.2
[2026-10-09T18:43:53Z]   ok  band edges
[2026-10-09T18:43:53Z]   ok  the window is [T0, T0+240)
[2026-10-09T18:43:53Z]   ok  the window takes T0+239 and not T0+240
[2026-10-09T18:43:53Z]   ok  a Down sale before T0 leaves makers short 4 Up at 0.75
[2026-10-09T18:43:53Z]   ok  T0+240 is the last minute
[2026-10-09T18:43:53Z]   ok  the window is the sum of w0..w3
[2026-10-09T18:43:53Z]   ok  a resolved, fee-schedule-conforming market qualifies
[2026-10-09T18:43:53Z]   ok  outcomePrices='["0.5", "0.5"]' reads unresolved
[2026-10-09T18:43:53Z]   ok  closed=False reads open
[2026-10-09T18:43:53Z]   ok  feeType='crypto_fees' reads fee
[2026-10-09T18:43:53Z]   ok  eventStartTime='2026-09-04T14:05:00Z' reads start
[2026-10-09T18:43:53Z]   ok  conditionId='0x12' reads condition
[2026-10-09T18:43:53Z]   ok  outcomes='["Yes", "No"]' reads outcomes
[2026-10-09T18:43:53Z]   ok  clobTokenIds='["123"]' reads tokens
[2026-10-09T18:43:53Z]   ok  a 25% rebate is not this TZ's schedule
[2026-10-09T18:43:53Z]   ok  no document reads absent
[2026-10-09T18:43:53Z]   ok  labels
[2026-10-09T18:43:53Z]   ok  the walk takes the five members around the excluded span, past one unresolved
[2026-10-09T18:43:53Z]   ok  1791098400 reads unresolved
[2026-10-09T18:43:53Z]   ok  no candidate of the explored span is considered
[2026-10-09T18:43:53Z]   ok  every document requested is a candidate considered, the last the 5th member's
[2026-10-09T18:43:53Z]   ok  nothing is considered after the 5th member
[2026-10-09T18:43:53Z]   ok  the 2026-09-02/04 span is excluded, its next market is not
[2026-10-09T18:43:53Z]   ok  the 2026-10-03/04 span ends at 1791097800
[2026-10-09T18:43:53Z]   ok  the labelled span 1788998400 ... 1790452200 is excluded, its neighbours are not
[2026-10-09T18:43:53Z]   ok  the walk steps over the labelled span
[2026-10-09T18:43:53Z]   ok  the set starts at 2026-09-04 14:00 UTC
[2026-10-09T18:43:53Z]   ok  thr = L/lambda + lambda V/8
[2026-10-09T18:43:53Z]   ok  at the projected V the threshold is Hoeffding's sqrt(V ln(1/alpha) / 2)
[2026-10-09T18:43:53Z]   ok  the projected threshold is 0.31 c a share
[2026-10-09T18:43:53Z]   ok  the projected power is 0.979
[2026-10-09T18:43:53Z]   ok  S at the EARN threshold reads EARN
[2026-10-09T18:43:53Z]   ok  just below it does not
[2026-10-09T18:43:53Z]   ok  S at the NO EARN threshold reads NO EARN
[2026-10-09T18:43:53Z]   ok  just above it does not
[2026-10-09T18:43:54Z]   ok  400 null runs at fair coins: 0 read EARN, at most 2 expected at alpha 0.005
[2026-10-09T18:43:54Z] labels: 2 members, 2 Up
[2026-10-09T18:43:54Z] S -18.40757080 = settlement -19.190 + rebate 0.78242920; per share -0.0781637825902335456475583864118895966029723991507430997876858 = -0.0814861995753715498938428874734607218683651804670912951167728 + 0.00332241698513800424628450106157112526539278131634819532908705
[2026-10-09T18:43:54Z] EARN False (margin -241597.800627746914187179237225374110125738788601942422313849); NO EARN False (margin -241559.807986146914187179237225374110125738788601942422313849)
[2026-10-09T18:43:54Z] band pre  makers per share 0.50350, of it rebate 0.00350 - barred from every reading
[2026-10-09T18:43:54Z] band w0   makers per share -0.4465350, of it rebate 0.0034650 - barred from every reading
[2026-10-09T18:43:54Z] band w1   makers per share 0.304559560173160173160173160173160173160173160173160173160173, of it rebate 0.00317427878787878787878787878787878787878787878787878787878788 - barred from every reading
[2026-10-09T18:43:54Z] wrote t-scored.csv sha256 b4c0a9b3fb355ad7f6bdaac13a2aa175c40189f720e3ebb54b8cb7fb90edc475 and t-reading.json sha256 4e91bb1462c5a0cc8cc75358a22e842539df0b5454cacf8ed51e75a5832b406f
[2026-10-09T18:43:54Z] labels: 2 members, 0 Up
[2026-10-09T18:43:54Z] S 66.09242920 = settlement 65.310 + rebate 0.78242920; per share 0.280647257749469214437367303609341825902335456475583864118896 = 0.277324840764331210191082802547770700636942675159235668789809 + 0.00332241698513800424628450106157112526539278131634819532908705
[2026-10-09T18:43:54Z] EARN False (margin -241513.300627746914187179237225374110125738788601942422313849); NO EARN False (margin -241644.307986146914187179237225374110125738788601942422313849)
[2026-10-09T18:43:54Z] band pre  makers per share -0.49650, of it rebate 0.00350 - barred from every reading
[2026-10-09T18:43:54Z] band w0   makers per share 0.5534650, of it rebate 0.0034650 - barred from every reading
[2026-10-09T18:43:54Z] band w1   makers per share -0.00279974718614718614718614718614718614718614718614718614718615, of it rebate 0.00317427878787878787878787878787878787878787878787878787878788 - barred from every reading
[2026-10-09T18:43:54Z] wrote t-scored.csv sha256 4fbad759ab6b5e96c4528643ba33014bb5dcd1f6e705195159ac5cf13d89611e and t-reading.json sha256 48a1928f730f0a4af02fe1ff8726ff8e49a853072285775b2867a04da6ea516a
[2026-10-09T18:43:54Z]   ok  the constants file is byte-identical with every label flipped
[2026-10-09T18:43:54Z]   ok  the score moves when the labels flip (negative control)
[2026-10-09T18:43:54Z]   ok  the score moves by the window's X, -160 + 75.5 = -84.5, by hand
[2026-10-09T18:43:54Z]   ok  gzip is deterministic
[2026-10-09T18:43:54Z]   ok  JSON is sorted with Decimals as text
[2026-10-09T18:43:54Z]   ok  no exponent form
[2026-10-09T18:43:54Z]   ok  an open under the recorder's root is refused before it happens
[2026-10-09T18:43:54Z] 59 of 59 checks passed
[2026-10-09T18:43:54Z] malloc tuned: True
[2026-10-09T18:43:54Z] peak memory of this run: 25690112 bytes
[2026-10-09T18:43:54Z] opens under the capture roots: 0
exit=0
```

**`59 of 59 checks passed`**, exit 0.

### 2.3 §3.3 — the units, and the directories beside this session

`I still`, the first run, which records both units in `state.json` (`logs/08-still-1.log`):

```text
$ I still
[2026-10-09T18:44:00Z] btc-recorder.service {'MainPID': '4148534', 'NRestarts': '2', 'ActiveState': 'active'}, MemoryCurrent 170082304, MemoryPeak 191582208
[2026-10-09T18:44:00Z] btc-chainbook.service {'MainPID': '4064090', 'NRestarts': '1', 'ActiveState': 'active'}, MemoryCurrent 7098368, MemoryPeak 18735104
[2026-10-09T18:44:00Z] still: recorded
[2026-10-09T18:44:00Z] malloc tuned: True
[2026-10-09T18:44:00Z] peak memory of this run: 25296896 bytes
[2026-10-09T18:44:00Z] opens under the capture roots: 0
exit=0
```

`I scratch "$(dirname "$S")"` (`logs/09-scratch.log`):

```text
$ I scratch "$(dirname "$S")"   # /tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8
[2026-10-09T18:44:07Z] running 337573 started 2026-10-07T20:05:37Z claude
[2026-10-09T18:44:07Z] running 337576 started 2026-10-07T20:05:37Z claude
[2026-10-09T18:44:07Z] running 618175 started 2026-10-09T18:39:07Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-10-09T18:44:07Z] 386a2f9a-9175-46e4-af0d-52cc5355a34c born 2026-10-04T19:04:47Z: earlier
[2026-10-09T18:44:07Z] 750b3996-3a2d-49fb-823d-1321cd631528 born 2026-10-09T18:39:07Z: live, process [618175]
[2026-10-09T18:44:07Z] 9b05d639-af52-44b6-9a8c-9f508f7b17c4 born 2026-10-04T22:04:29Z: earlier
[2026-10-09T18:44:07Z] f1dda509-7343-505e-8afa-097e9a463ab6 born 2026-10-04T22:04:30Z: earlier
[2026-10-09T18:44:07Z] malloc tuned: True
[2026-10-09T18:44:07Z] peak memory of this run: 25296896 bytes
[2026-10-09T18:44:07Z] opens under the capture roots: 0
exit=0
```

Three running processes match the rule: the two `claude` processes started 2026-10-07 20:05:37 UTC, and this
session's own, `618175`, started 2026-10-09 18:39:07 UTC. Of the four UUID directories beside this session's own,
`750b3996…` is **live**: it was born in the same second as process `618175`. The other three are **earlier**:
`386a2f9a…` (born 2026-10-04 19:04:47 UTC, 4 s after the `claude remote-control` bridge that TZ-21 kept it for,
map §7 item 91; that process no longer runs), and `9b05d639…` and `f1dda509…` (TZ-21's session pair, born
2026-10-04 22:04:29 and 22:04:30 UTC).

### 2.4 §9 B-RECLAIM-SCRATCH — after §3.3, before §3.4

Before the removal the Executor looked at each target (`logs/10-scratch-targets.log`, a read §9 does not list,
§6 item 3):

```text
$ du -sb and find -type f | wc -l of each earlier directory (2026-10-09T18:44:19Z)
0	/tmp/claude-0/-root-btc-5m-twap/386a2f9a-9175-46e4-af0d-52cc5355a34c
files: 0, dirs: 2
/tmp/claude-0/-root-btc-5m-twap/386a2f9a-9175-46e4-af0d-52cc5355a34c
/tmp/claude-0/-root-btc-5m-twap/386a2f9a-9175-46e4-af0d-52cc5355a34c/scratchpad
0	/tmp/claude-0/-root-btc-5m-twap/9b05d639-af52-44b6-9a8c-9f508f7b17c4
files: 0, dirs: 2
/tmp/claude-0/-root-btc-5m-twap/9b05d639-af52-44b6-9a8c-9f508f7b17c4
/tmp/claude-0/-root-btc-5m-twap/9b05d639-af52-44b6-9a8c-9f508f7b17c4/scratchpad
5531	/tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6
files: 7, dirs: 3
/tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6
/tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6/tasks
/tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6/scratchpad
/tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6/tasks/b7d8zcdgf.output
/tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6/tasks/b36gwwn9j.output
/tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6/tasks/ba2txhmiu.output
/tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6/tasks/burskqr5y.output
/tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6/tasks/b2653qf59.output
```

`I reclaim`, once, with the three earlier directories as its arguments (`logs/11-reclaim-scratch.log`):

```text
$ I reclaim /tmp/claude-0/-root-btc-5m-twap/386a2f9a-9175-46e4-af0d-52cc5355a34c /tmp/claude-0/-root-btc-5m-twap/9b05d639-af52-44b6-9a8c-9f508f7b17c4 /tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6
[2026-10-09T18:44:26Z] reclaim: 1659 report tokens; forensic store holds 1519 files
[2026-10-09T18:44:26Z] RECLAIM PASS: 7 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 1519 -> 1519 files
[2026-10-09T18:44:26Z] malloc tuned: True
[2026-10-09T18:44:26Z] peak memory of this run: 26587136 bytes
[2026-10-09T18:44:26Z] opens under the capture roots: 0
exit=0
```

`RECLAIM PASS` printed before any removal: 7 files considered, none named by a report and none kept by name, so 0
copied; the store `1,519` → `1,519`. Then one `rm -rf` per directory, each in its own command, each followed by
`test -e` (`logs/12-rm-scratch.log`):

```text
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/386a2f9a-9175-46e4-af0d-52cc5355a34c; echo "exit=$?"   (2026-10-09T18:44:49Z)
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/386a2f9a-9175-46e4-af0d-52cc5355a34c; echo "exit=$?"
exit=1
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/9b05d639-af52-44b6-9a8c-9f508f7b17c4; echo "exit=$?"   (2026-10-09T18:44:53Z)
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/9b05d639-af52-44b6-9a8c-9f508f7b17c4; echo "exit=$?"
exit=1
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6; echo "exit=$?"   (2026-10-09T18:44:58Z)
exit=0
$ test -e /tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6; echo "exit=$?"
exit=1
```

**None was refused by the session's classifier.** Each `rm -rf` exit `0`, each `test -e` exit `1`. The live
directory `750b3996…` and this session's own `5ce9f787…` were not named and not touched.

### 2.5 §3.4 — G-REHEARSAL (V5)

`I rehearse` (`logs/13-rehearse.log`):

```text
$ I rehearse
[2026-10-09T18:45:04Z] MemAvailable 284483584 bytes, floor 147152896
[2026-10-09T18:45:05Z] the set formed in 0.9 s: 144 considered, 144 members, /root/tz23-work/rehearsal/set.json sha256 83a53bd3fb13829173282487833ef0398280d358377e0f09d0beb414c7829cbc
[2026-10-09T18:45:18Z] chunks 8 of 8, 14 s
[2026-10-09T18:45:20Z] members 144, considered 144, first 1791050100 2026-10-03T17:55:00Z, last 1791093000 2026-10-04T05:50:00Z, weekend members 144
[2026-10-09T18:45:20Z] member list sha 6441dba6604897a0146f39f8e6a153818083f2a5678f6c6484e77487d7968ce6
[2026-10-09T18:45:20Z] members by the number of excluded spans ending below them: 2: 144
[2026-10-09T18:45:20Z] window fills 128031, shares 3509409.854401, X -44336.003951, C -108894.2181475504884399, R 8015.91427290719561009665372913342
[2026-10-09T18:45:20Z] band pre  fills 8091, shares 322581.311616
[2026-10-09T18:45:20Z] band w0   fills 34282, shares 858622.027230
[2026-10-09T18:45:20Z] band w1   fills 30134, shares 822002.256141
[2026-10-09T18:45:20Z] band w2   fills 30036, shares 833324.447472
[2026-10-09T18:45:20Z] band w3   fills 33579, shares 995461.123558
[2026-10-09T18:45:20Z] band last fills 28463, shares 978970.671146
[2026-10-09T18:45:20Z] band post fills 730, shares 192218.999951
[2026-10-09T18:45:20Z] V 2140569358.582178867947; lambda 0.000021932; L 5.29831736654803667745321503082690498327770311161780120618734
[2026-10-09T18:45:20Z] EARN at S >= 247447.678143864582553655937725374110125738788601942422313849 (0.0705097689953628782357990790416292822747757197155682685069209 a share); NO EARN at S <= -229900.628871859582553655937725374110125738788601942422313849 (-0.0655097689953628782357990790416292822747757197155682685069209 a share)
[2026-10-09T18:45:20Z] power of either answer against the other's alternative, normal, variance V/4: 0.0
[2026-10-09T18:45:20Z] wrote /root/tz23-work/rehearsal/rehearsal-constants.json sha256 9f521a23b3a5b48ac7569f68a9c42bf6da1bb8ef09f5a71c0c8e091fbf5098e3
[2026-10-09T18:45:20Z] wrote /root/tz23-work/rehearsal/rehearsal-fills.jsonl.gz sha256 3ce50a85f84068a4cac15ece53d2ea1b16184b9080d69228b0baae8f887c8116
[2026-10-09T18:45:20Z] wrote /root/tz23-work/rehearsal/rehearsal-members.csv sha256 2676af1dee730001abf560555c1c0eb9b88901209a94598dcb966495e20131d1
[2026-10-09T18:45:20Z] labels: 144 members, 75 Up
[2026-10-09T18:45:20Z] S 28056.96630645768404999665372913342 = settlement 20041.0520335504884399 + rebate 8015.91427290719561009665372913342; per share 0.00799478187800511502094750845984644263428388279200750286615141 = 0.00571066158272105687921991461742582040359548327015047220206206 + 0.00228412029528405814172759384242062223068839952185703066408935
[2026-10-09T18:45:20Z] EARN False (margin -219390.711837406898503659283996240690125738788601942422313849); NO EARN False (margin -257957.595178317266603652591454507530125738788601942422313849)
[2026-10-09T18:45:20Z] band pre  makers per share -0.0194439458710785748295304005216177364927488757104923929158955, of it rebate 0.00343449235380714512022328037575989418845131167538094607088176 - barred from every reading
[2026-10-09T18:45:20Z] band w0   makers per share 0.00809668994246333164669906247241946849255885936724456097087031, of it rebate 0.00298702379163527017651557524881741438572713752576808557588209 - barred from every reading
[2026-10-09T18:45:20Z] band w1   makers per share 0.00216533860931846166363481784032051450296117855798497203069005, of it rebate 0.00253549451390923610592868522313286130876296105380083347534521 - barred from every reading
[2026-10-09T18:45:20Z] band w2   makers per share 0.0169475211352226561899886758769244471548446735331566650802338, of it rebate 0.00217930627249097667478222079878301204209651407974407518415309 - barred from every reading
[2026-10-09T18:45:20Z] band w3   makers per share 0.00522599320344578533877668254227426131378006832207622223362456, of it rebate 0.00155801005843739214150129623276759217257315589581711772196858 - barred from every reading
[2026-10-09T18:45:20Z] band last makers per share -0.0145412285056932672794855950031652205947831483024700954987439, of it rebate 0.000758816301907631239250794001755731940353158074036355805383154 - barred from every reading
[2026-10-09T18:45:20Z] band post makers per share 0.00300205633772118880223190142216078103457971517224835236600008, of it rebate 0.0000652987480229926338239312826220749917983220940599929383096346 - barred from every reading
[2026-10-09T18:45:20Z] wrote rehearsal-scored.csv sha256 d31eb18fa58f8a26f12979f733fcead3b2482a480ba97a17c1145c1eef99bda2 and rehearsal-reading.json sha256 4cdf1a1179c0d58f048d091e0a719951cb3af38c822d49a2e9343bea5f502d1f
[2026-10-09T18:45:20Z] G-REHEARSAL members instrument 144, the Architect's 144, equal
[2026-10-09T18:45:20Z] G-REHEARSAL ups     instrument 75, the Architect's 75, equal
[2026-10-09T18:45:20Z] G-REHEARSAL n       instrument 128031, the Architect's 128031, equal
[2026-10-09T18:45:20Z] G-REHEARSAL sh      instrument 3509409.854401, the Architect's 3509409.854401, equal
[2026-10-09T18:45:20Z] G-REHEARSAL X       instrument -44336.003951, the Architect's -44336.003951, equal
[2026-10-09T18:45:20Z] G-REHEARSAL C       instrument -108894.2181475504884399, the Architect's -108894.2181475504884399, equal
[2026-10-09T18:45:20Z] G-REHEARSAL R       instrument 8015.91427290719561009665372913342, the Architect's 8015.91427290719561009665372913342, equal
[2026-10-09T18:45:20Z] G-REHEARSAL V       instrument 2140569358.582178867947, the Architect's 2140569358.582178867947, equal
[2026-10-09T18:45:20Z] G-REHEARSAL XU      instrument -88853.166114, the Architect's -88853.166114, equal
[2026-10-09T18:45:20Z] G-REHEARSAL S       instrument 28056.96630645768404999665372913342, the Architect's 28056.96630645768404999665372913342, equal
[2026-10-09T18:45:20Z] G-REHEARSAL PASS: 10 of 10 figures equal
[2026-10-09T18:45:20Z] malloc tuned: True
[2026-10-09T18:45:20Z] peak memory of this run: 55083008 bytes
[2026-10-09T18:45:20Z] opens under the capture roots: 0
exit=0
```

**G-REHEARSAL PASS: 10 of 10 figures equal**, each as a value. The four files TZ §4.1 records beside the gate
hash to the Architect's prefixes: `set.json` `83a53bd3fb13…`, the fills file `3ce50a85f840…`, the members file
`2676af1dee73…`, the scored file `d31eb18fa58f…` (recorded, judged by none). The rehearsal's own power line reads
`0.0`: 144 markets give no power, and the rehearsal reads no answer.

### 2.6 §3.5 — the set, G-SET (V6)

`I fetch`, run in the background with its output to `logs/` and read until it printed `G-SET PASS`
(`logs/14-fetch.log`):

```text
$ I fetch   (started 2026-10-09T18:45:30Z, in the background)
[2026-10-09T18:45:30Z] MemAvailable 272838656 bytes, floor 147152896
[2026-10-09T18:45:53Z] the set formed in 23.0 s: 4032 considered, 4032 members, /root/tz23-work/set/set.json sha256 a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303
[2026-10-09T18:49:44Z] chunks 25 of 202, 231 s
[2026-10-09T18:50:19Z] projected 1789 s for 202 chunks after 30 fetched
[2026-10-09T18:53:33Z] chunks 50 of 202, 460 s
[2026-10-09T18:57:47Z] chunks 75 of 202, 714 s
[2026-10-09T19:00:22Z] chunks 100 of 202, 869 s
[2026-10-09T19:03:45Z] chunks 125 of 202, 1071 s
[2026-10-09T19:06:49Z] chunks 150 of 202, 1256 s
[2026-10-09T19:09:38Z] chunks 175 of 202, 1424 s
[2026-10-09T19:11:51Z] chunks 200 of 202, 1558 s
[2026-10-09T19:11:58Z] chunks 202 of 202, 1565 s
[2026-10-09T19:12:03Z] G-SET PASS: 4032 members, 202 chunks, every chunk read back
[2026-10-09T19:12:03Z] malloc tuned: True
[2026-10-09T19:12:03Z] peak memory of this run: 79794176 bytes
[2026-10-09T19:12:03Z] opens under the capture roots: 0
exit=0
```

**G-SET PASS** at the first run: no network failure, so no resume was needed. The walk formed the set in 23.0 s
from 202 gamma requests: **4,032 candidates considered, 4,032 members**. Every chunk's feed ended with no cursor,
every row belonged to its chunk's markets and carried its market's token for its outcome (asserted per row by
`trades`), and every chunk read back to its members in order. After its first 30 fresh chunks the fetch projected
**1,789 s** for 202 chunks, under the 7,200 s fail-fast bound and under §6's 2,620 s; it took 1,565 s for the chunks.

### 2.7 §3.6 — the constants, twice (V7)

The first run (`logs/15-constants-1.log`):

```text
$ I constants   (first run)
[2026-10-09T19:12:26Z] MemAvailable 294424576 bytes, floor 147152896
[2026-10-09T19:13:16Z] members 4032, considered 4032, first 1788530400 2026-09-04T14:00:00Z, last 1791241800 2026-10-05T23:10:00Z, weekend members 1329
[2026-10-09T19:13:16Z] member list sha 699cab9aa3f540b6cdfe2ae8a295b1fa4bca96921238106dad4b243bc4ecce4f
[2026-10-09T19:13:16Z] members by the number of excluded spans ending below them: 1: 1560, 2: 1992, 3: 480
[2026-10-09T19:13:16Z] window fills 4820537, shares 129225737.554660, X 14980.119286, C -2182836.1232161653311455, R 289595.61967909269156966797439628522
[2026-10-09T19:13:16Z] band pre  fills 323889, shares 10865028.265881
[2026-10-09T19:13:16Z] band w0   fills 1276375, shares 31154232.039099
[2026-10-09T19:13:16Z] band w1   fills 1119269, shares 27382021.016632
[2026-10-09T19:13:16Z] band w2   fills 1151584, shares 30379847.119050
[2026-10-09T19:13:16Z] band w3   fills 1273309, shares 40309637.379879
[2026-10-09T19:13:16Z] band last fills 846516, shares 34044120.950806
[2026-10-09T19:13:16Z] band post fills 22616, shares 4695157.159079
[2026-10-09T19:13:16Z] V 69635266807.031814646570; lambda 0.000021932; L 5.29831736654803667745321503082690498327770311161780120618734
[2026-10-09T19:13:16Z] EARN at S >= 432484.391198789259040750892225374110125738788601942422313849 (0.00334673571521196917020701590023317623564727866661594537540652 a share); NO EARN at S <= 213644.296574510740959249107774625889874261211398057577686151 (0.00165326428478803082979298409976682376435272133338405462459348 a share)
[2026-10-09T19:13:16Z] power of either answer against the other's alternative, normal, variance V/4: 0.9473003597229505
[2026-10-09T19:13:16Z] wrote /root/tz23-work/set/tz23-constants.json sha256 1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5
[2026-10-09T19:13:16Z] wrote /root/tz23-work/set/tz23-fills.jsonl.gz sha256 4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64
[2026-10-09T19:13:16Z] wrote /root/tz23-work/set/tz23-members.csv sha256 cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61
[2026-10-09T19:13:16Z] malloc tuned: True
[2026-10-09T19:13:16Z] peak memory of this run: 69562368 bytes
[2026-10-09T19:13:16Z] opens under the capture roots: 0
exit=0
```

The second run (`logs/16-constants-2.log`):

```text
$ I constants   (second run, contract §6 determinism)
[2026-10-09T19:13:27Z] MemAvailable 295604224 bytes, floor 147152896
[2026-10-09T19:14:20Z] unchanged /root/tz23-work/set/tz23-fills.jsonl.gz sha256 4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64
[2026-10-09T19:14:20Z] unchanged /root/tz23-work/set/tz23-members.csv sha256 cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61
[2026-10-09T19:14:20Z] unchanged /root/tz23-work/set/tz23-constants.json sha256 1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5
[2026-10-09T19:14:20Z] members 4032, considered 4032, first 1788530400 2026-09-04T14:00:00Z, last 1791241800 2026-10-05T23:10:00Z, weekend members 1329
[2026-10-09T19:14:20Z] member list sha 699cab9aa3f540b6cdfe2ae8a295b1fa4bca96921238106dad4b243bc4ecce4f
[2026-10-09T19:14:20Z] members by the number of excluded spans ending below them: 1: 1560, 2: 1992, 3: 480
[2026-10-09T19:14:20Z] window fills 4820537, shares 129225737.554660, X 14980.119286, C -2182836.1232161653311455, R 289595.61967909269156966797439628522
[2026-10-09T19:14:20Z] band pre  fills 323889, shares 10865028.265881
[2026-10-09T19:14:20Z] band w0   fills 1276375, shares 31154232.039099
[2026-10-09T19:14:20Z] band w1   fills 1119269, shares 27382021.016632
[2026-10-09T19:14:20Z] band w2   fills 1151584, shares 30379847.119050
[2026-10-09T19:14:20Z] band w3   fills 1273309, shares 40309637.379879
[2026-10-09T19:14:20Z] band last fills 846516, shares 34044120.950806
[2026-10-09T19:14:20Z] band post fills 22616, shares 4695157.159079
[2026-10-09T19:14:20Z] V 69635266807.031814646570; lambda 0.000021932; L 5.29831736654803667745321503082690498327770311161780120618734
[2026-10-09T19:14:20Z] EARN at S >= 432484.391198789259040750892225374110125738788601942422313849 (0.00334673571521196917020701590023317623564727866661594537540652 a share); NO EARN at S <= 213644.296574510740959249107774625889874261211398057577686151 (0.00165326428478803082979298409976682376435272133338405462459348 a share)
[2026-10-09T19:14:20Z] power of either answer against the other's alternative, normal, variance V/4: 0.9473003597229505
[2026-10-09T19:14:20Z] wrote /root/tz23-work/set/tz23-constants.json sha256 1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5
[2026-10-09T19:14:20Z] wrote /root/tz23-work/set/tz23-fills.jsonl.gz sha256 4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64
[2026-10-09T19:14:20Z] wrote /root/tz23-work/set/tz23-members.csv sha256 cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61
[2026-10-09T19:14:20Z] malloc tuned: True
[2026-10-09T19:14:20Z] peak memory of this run: 69562368 bytes
[2026-10-09T19:14:20Z] opens under the capture roots: 0
exit=0
```

**3 of 3 files `unchanged`** at the second run — the fills, members and constants files — and every other line of
the two runs equal but the time stamps and the memory reads. The constants file's SHA-256,
`1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5`, is in `state.json` as `constants_sha`, written
19:13:16 UTC and rewritten with the same value at 19:14:20 UTC. The instrument's commit `7f5ae3f`, committed at 18:43:30
UTC, had reached `origin` before the self-test's first line at 18:43:54 UTC. **Both preconditions of §2 item 6 held from 19:13:16 UTC; no label of the set was read
before §3.8.**

**The set.**

| quantity | value |
|---|---|
| candidates considered | `4,032` — the walk requested no document after the 4,032nd member |
| members | `4,032` — every candidate qualified |
| non-members | **none**: the constants file's `non_members` list is empty, and no `non-member` line printed |
| first member | `1788530400`, 2026-09-04 14:00:00 UTC |
| last member | `1791241800`, 2026-10-05 23:10:00 UTC |
| members by segment | `1: 1560, 2: 1992, 3: 480` — `1788530400` … `1788998100`, `1790452500` … `1791049800`, `1791098100` … `1791241800` |
| weekend members | `1,329` |
| member list SHA-256 | `699cab9aa3f540b6cdfe2ae8a295b1fa4bca96921238106dad4b243bc4ecce4f`, equal to the value TZ §1 records for "every candidate qualifies" (recorded there and asserted by nothing) |
| set file | `/root/tz23-work/set/set.json`, SHA-256 `a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303` |

**The window's fills, `[T0, T0 + 240)`, label-free.**

| quantity | value |
|---|---|
| fills `n` | `4,820,537` taker rows |
| shares `Sh` | `129225737.554660` |
| `X`, the makers' net Up position | `14980.119286` |
| `C`, its cost | `-2182836.1232161653311455` |
| `R`, the rebate counted | `289595.61967909269156966797439628522` |
| `V = Σ X_m²` | `69635266807.031814646570` |
| `λ`, `L = ln 200` | `0.000021932`, `5.29831736654803667745321503082690498327770311161780120618734` |

**Every band, fills and shares** (the window is `w0` … `w3`):

| band | `T − T0` | fills | shares |
|---|---|---|---|
| `pre` | below 0 | `323,889` | `10865028.265881` |
| `w0` | `[0, 60)` | `1,276,375` | `31154232.039099` |
| `w1` | `[60, 120)` | `1,119,269` | `27382021.016632` |
| `w2` | `[120, 180)` | `1,151,584` | `30379847.119050` |
| `w3` | `[180, 240)` | `1,273,309` | `40309637.379879` |
| `last` | `[240, 300)` | `846,516` | `34044120.950806` |
| `post` | `300` on | `22,616` | `4695157.159079` |

**The thresholds and the power, before any label.**

| quantity | value |
|---|---|
| `thr = L/λ + λV/8` — EARN at `S >=` | `432484.391198789259040750892225374110125738788601942422313849` |
| the same per share | `0.00334673571521196917020701590023317623564727866661594537540652` |
| NO EARN at `S <= δ·Sh − thr` | `213644.296574510740959249107774625889874261211398057577686151` |
| the same per share | `0.00165326428478803082979298409976682376435272133338405462459348` |
| power of either answer against the other's alternative, normal, variance `V/4` | `0.9473003597229505` |

`thr / Sh` is `0.335` c a share against TZ §1's projected `0.307`, and the power `0.947` against the projected
`0.979`: the measured `V` is 21% below the projection `V̂` and `Sh` is lower too, so the threshold per share is
higher. The power is printed before any label and decides nothing (TZ §4.3: "No row reads a power"). `2 thr / Sh` is
`0.669` c, above `δ` = `0.5` c, so EARN and NO EARN cannot both hold.

### 2.8 §3.7 — the rebate check (V8)

`I rebate`, label-free: members `62`, `125`, … `4,031`, every 63rd, read again through both feeds
(`logs/17-rebate.log`):

```text
$ I rebate
[2026-10-09T19:14:28Z] MemAvailable 316141568 bytes, floor 147152896
[2026-10-09T19:16:30Z] rebate check: 64 members, 73170 window transactions, 12251 at several prices, 0 transactions with other than one taker row skipped
[2026-10-09T19:16:30Z] transactions whose taker size differs from its makers' sum: 7, 0.042328 shares in all
[2026-10-09T19:16:30Z] fee-equivalent at the reported price 312509.17831289659209929766339987, at each maker's own price 312433.82894541944351689680610967, ratio 0.999758889105645064269955027965738023156843900909950603520888
[2026-10-09T19:16:30Z] the rebate counted above the venue's, per share of the sample's window: 0.000000544492927810179387318138600954659775940235203423452375693612
[2026-10-09T19:16:30Z] malloc tuned: True
[2026-10-09T19:16:30Z] peak memory of this run: 76279808 bytes
[2026-10-09T19:16:30Z] opens under the capture roots: 0
exit=0
```

**Asserted, 64 of 64:** each sampled member's taker rows, re-read, equal the cache's (`rebate: the taker feed of
%d changed` never fired; exit 0). Every taker row of a window transaction was found among that transaction's rows
in the second feed (asserted as well).

**Recorded, not asserted** — over the 64 members' window transactions with exactly one taker row:

| figure | value |
|---|---|
| window transactions | `73,170`; `0` transactions with other than one taker row skipped |
| filled at several prices | `12,251` |
| taker size different from its makers' sum | `7` transactions, `0.042328` shares in all |
| fee-equivalent `Σ s p (1 − p)` at the reported price | `312509.17831289659209929766339987` |
| the same at each maker's own price | `312433.82894541944351689680610967` |
| ratio, exact over reported | `0.999758889105645064269955027965738023156843900909950603520888` |
| the rebate counted above the venue's, per share of the sample's window | `0.000000544492927810179387318138600954659775940235203423452375693612` USDC |

The rebate counted from reported prices exceeds the one from each maker's own price by `0.0241%` of the latter
here, against `0.014%` on the Architect's 64 weekday markets (TZ §1). It runs in the direction TZ §1 states, since
`p (1 − p)` is concave and a reported price is its fills' mean. Per share it is `0.0000544` c, against the
`0.335` c threshold per share. The size gap is 7 transactions and `0.042328` shares, against the Architect's 6 of
90,509 and `0.050340`.

### 2.9 §3.8 — the score, twice (V9)

**The labels were read once a run, by `score` alone, after §2 item 6's two preconditions held** (§2.7). The first
run (`logs/18-score-1.log`):

```text
$ I score   (first run: the labels, read once)
[2026-10-09T19:16:42Z] labels: 4032 members, 2023 Up
[2026-10-09T19:16:42Z] S 272424.11263025802271516797439628522 = settlement -17171.5070488346688545 + rebate 289595.61967909269156966797439628522; per share 0.00210812580980648584769071608480091420491821166475579642487587 = -0.000132879930683865912108413304618626214221032332128716794716256 + 0.00224100574049035175979912938941954041913924399688451321959213
[2026-10-09T19:16:42Z] EARN False (margin -160060.278568531236325582917829088890125738788601942422313849); NO EARN False (margin -58779.816055747281755918866621659330125738788601942422313849)
[2026-10-09T19:16:42Z] band pre  makers per share 0.00578304081952413057952022352980629664935718900791247195931976, of it rebate 0.00345012399769891100803924850470126430613185212420594087415147 - barred from every reading
[2026-10-09T19:16:42Z] band w0   makers per share 0.00322455954748439770877692265458851757694567952305808329115454, of it rebate 0.00304907563482741327856453398896113778589080525912034696196823 - barred from every reading
[2026-10-09T19:16:42Z] band w1   makers per share 0.00537342902056019379690494463906948507427542781610791564883005, of it rebate 0.00259433618094249559600229966912416186895506872175502666584656 - barred from every reading
[2026-10-09T19:16:42Z] band w2   makers per share 0.00233536554312248819680313753205740097402618301672759944638889, of it rebate 0.00211313274742361729393620015038819425576058608365283165320518 - barred from every reading
[2026-10-09T19:16:42Z] band w3   makers per share -0.00114409261092735982843879619885996043013925160772673885672486, of it rebate 0.00147282873442040320431779069075803660016903189588108502253665 - barred from every reading
[2026-10-09T19:16:42Z] band last makers per share 0.00209141444924695550009797726018697540575766571006026582212843, of it rebate 0.000820733005138050399449513535090341996059592320041265996913536 - barred from every reading
[2026-10-09T19:16:42Z] band post makers per share 0.00383884093149174464961136665680377112039339556460817539811684, of it rebate 0.0000708535922763116122394261981760652136552029840416336454011999 - barred from every reading
[2026-10-09T19:16:42Z] wrote tz23-scored.csv sha256 12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988 and tz23-reading.json sha256 fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043
[2026-10-09T19:16:42Z] M0 READING: UNDECIDABLE
[2026-10-09T19:16:42Z] malloc tuned: True
[2026-10-09T19:16:42Z] peak memory of this run: 47501312 bytes
[2026-10-09T19:16:42Z] opens under the capture roots: 0
exit=0
```

The second run (`logs/19-score-2.log`):

```text
$ I score   (second run, contract §6 determinism)
[2026-10-09T19:16:52Z] unchanged /root/tz23-work/set/tz23-scored.csv sha256 12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988
[2026-10-09T19:16:52Z] unchanged /root/tz23-work/set/tz23-reading.json sha256 fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043
[2026-10-09T19:16:52Z] labels: 4032 members, 2023 Up
[2026-10-09T19:16:52Z] S 272424.11263025802271516797439628522 = settlement -17171.5070488346688545 + rebate 289595.61967909269156966797439628522; per share 0.00210812580980648584769071608480091420491821166475579642487587 = -0.000132879930683865912108413304618626214221032332128716794716256 + 0.00224100574049035175979912938941954041913924399688451321959213
[2026-10-09T19:16:52Z] EARN False (margin -160060.278568531236325582917829088890125738788601942422313849); NO EARN False (margin -58779.816055747281755918866621659330125738788601942422313849)
[2026-10-09T19:16:52Z] band pre  makers per share 0.00578304081952413057952022352980629664935718900791247195931976, of it rebate 0.00345012399769891100803924850470126430613185212420594087415147 - barred from every reading
[2026-10-09T19:16:52Z] band w0   makers per share 0.00322455954748439770877692265458851757694567952305808329115454, of it rebate 0.00304907563482741327856453398896113778589080525912034696196823 - barred from every reading
[2026-10-09T19:16:52Z] band w1   makers per share 0.00537342902056019379690494463906948507427542781610791564883005, of it rebate 0.00259433618094249559600229966912416186895506872175502666584656 - barred from every reading
[2026-10-09T19:16:52Z] band w2   makers per share 0.00233536554312248819680313753205740097402618301672759944638889, of it rebate 0.00211313274742361729393620015038819425576058608365283165320518 - barred from every reading
[2026-10-09T19:16:52Z] band w3   makers per share -0.00114409261092735982843879619885996043013925160772673885672486, of it rebate 0.00147282873442040320431779069075803660016903189588108502253665 - barred from every reading
[2026-10-09T19:16:52Z] band last makers per share 0.00209141444924695550009797726018697540575766571006026582212843, of it rebate 0.000820733005138050399449513535090341996059592320041265996913536 - barred from every reading
[2026-10-09T19:16:52Z] band post makers per share 0.00383884093149174464961136665680377112039339556460817539811684, of it rebate 0.0000708535922763116122394261981760652136552029840416336454011999 - barred from every reading
[2026-10-09T19:16:52Z] wrote tz23-scored.csv sha256 12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988 and tz23-reading.json sha256 fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043
[2026-10-09T19:16:52Z] M0 READING: UNDECIDABLE
[2026-10-09T19:16:52Z] malloc tuned: True
[2026-10-09T19:16:52Z] peak memory of this run: 47894528 bytes
[2026-10-09T19:16:52Z] opens under the capture roots: 0
exit=0
```

**2 of 2 files `unchanged`** at the second run, the scored file and the reading file, and every other line equal
but the time stamps and the memory read. **The ledger holds two lines**, one a `score` run, each naming the head
`7f5ae3f…` that `origin` carries and the member list `699cab9a…`:

```text
{"at":"2026-10-09T19:16:41Z","head":"7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8","member_list_sha":"699cab9aa3f540b6cdfe2ae8a295b1fa4bca96921238106dad4b243bc4ecce4f","members":4032}
{"at":"2026-10-09T19:16:52Z","head":"7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8","member_list_sha":"699cab9aa3f540b6cdfe2ae8a295b1fa4bca96921238106dad4b243bc4ecce4f","members":4032}
```

**The reading** — from `tz23-reading.json`, `fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043`:

| quantity | total, USDC | per share of the window |
|---|---|---|
| **`S`**, the makers' result at settlement with the rebate | **`272424.11263025802271516797439628522`** | **`0.00210812580980648584769071608480091420491821166475579642487587`** |
| its settlement part, `Σ X·up − C` | `-17171.5070488346688545` | `-0.000132879930683865912108413304618626214221032332128716794716256` |
| its rebate part, `R` | `289595.61967909269156966797439628522` | `0.00224100574049035175979912938941954041913924399688451321959213` |
| `Σ X · up` | `-2200007.630265` | — |
| Up outcomes | `2,023` of `4,032` | — |
| EARN's bound, `S >= thr` | `432484.391198789259040750892225374110125738788601942422313849` | `0.00334673571521196917020701590023317623564727866661594537540652` |
| NO EARN's bound, `S <= δ·Sh − thr` | `213644.296574510740959249107774625889874261211398057577686151` | `0.00165326428478803082979298409976682376435272133338405462459348` |
| EARN's margin, `S − thr` | `-160060.278568531236325582917829088890125738788601942422313849` | — |
| NO EARN's margin, `(δ·Sh − thr) − S` | `-58779.816055747281755918866621659330125738788601942422313849` | — |

`S` is `160,060.28` USDC short of EARN's bound and `58,779.82` USDC above NO EARN's: **neither holds, and the reading
is UNDECIDABLE**. Per share the makers kept `0.211` c, of which `−0.013` c at settlement and `+0.224` c rebate;
EARN needed `0.335` c and NO EARN `0.165` c or less.

**The bands, barred from every reading** — the makers' result per share in each band, and the rebate inside it:

| band | makers per share, USDC | of it rebate |
|---|---|---|
| `pre` | `0.00578304081952413057952022352980629664935718900791247195931976` | `0.00345012399769891100803924850470126430613185212420594087415147` |
| `w0` | `0.00322455954748439770877692265458851757694567952305808329115454` | `0.00304907563482741327856453398896113778589080525912034696196823` |
| `w1` | `0.00537342902056019379690494463906948507427542781610791564883005` | `0.00259433618094249559600229966912416186895506872175502666584656` |
| `w2` | `0.00233536554312248819680313753205740097402618301672759944638889` | `0.00211313274742361729393620015038819425576058608365283165320518` |
| `w3` | `-0.00114409261092735982843879619885996043013925160772673885672486` | `0.00147282873442040320431779069075803660016903189588108502253665` |
| `last` | `0.00209141444924695550009797726018697540575766571006026582212843` | `0.000820733005138050399449513535090341996059592320041265996913536` |
| `post` | `0.00383884093149174464961136665680377112039339556460817539811684` | `0.0000708535922763116122394261981760652136552029840416336454011999` |

### 2.10 §3.9 — G-STILL (V10)

`I still`, the second run (`logs/20-still-2.log`):

```text
$ I still   (second run, G-STILL)
[2026-10-09T19:16:58Z] btc-recorder.service {'MainPID': '4148534', 'NRestarts': '2', 'ActiveState': 'active'}, MemoryCurrent 140091392, MemoryPeak 191582208
[2026-10-09T19:16:58Z] btc-chainbook.service {'MainPID': '4064090', 'NRestarts': '1', 'ActiveState': 'active'}, MemoryCurrent 7573504, MemoryPeak 18735104
[2026-10-09T19:16:58Z] G-STILL PASS: unchanged since 2026-10-09T18:44:00Z
[2026-10-09T19:16:58Z] malloc tuned: True
[2026-10-09T19:16:58Z] peak memory of this run: 25165824 bytes
[2026-10-09T19:16:58Z] opens under the capture roots: 0
exit=0
```

| unit | read | `MainPID` | `NRestarts` | `ActiveState` | `MemoryCurrent` | `MemoryPeak` |
|---|---|---|---|---|---|---|
| `btc-recorder.service` | §3.3, 18:44:00 UTC | `4148534` | `2` | `active` | `170,082,304` | `191,582,208` |
| `btc-recorder.service` | §3.9, 19:16:58 UTC | `4148534` | `2` | `active` | `140,091,392` | `191,582,208` |
| `btc-recorder.service` | §3.10, after 19:17:15 UTC | `4148534` | `2` | — | `135,249,920` | `191,582,208` |
| `btc-chainbook.service` | §3.3, 18:44:00 UTC | `4064090` | `1` | `active` | `7,098,368` | `18,735,104` |
| `btc-chainbook.service` | §3.9, 19:16:58 UTC | `4064090` | `1` | `active` | `7,573,504` | `18,735,104` |
| `btc-chainbook.service` | §3.10, after 19:17:15 UTC | `4064090` | `1` | — | `7,573,504` | `18,735,104` |

**G-STILL PASS:** both units kept `MainPID`, `NRestarts` and `ActiveState` from §3.3 to §3.9. The recorder is the
process TZ-21 left, pid `4148534`, `NRestarts` 2, and the chain book TZ-20's, pid `4064090`, `NRestarts` 1. Both
memory figures are each control group's charge, page cache included (map §6), and are recorded for TZ-22.

### 2.11 Memory and the capture roots — every mode (V11, V12)

| mode | log | `MemAvailable` at its start | peak memory | `malloc tuned` | opens under the capture roots |
|---|---|---|---|---|---|
| `selftest` | `07` | — | `25,690,112` | `True` | `0` |
| `still` (first) | `08` | — | `25,296,896` | `True` | `0` |
| `scratch` | `09` | — | `25,296,896` | `True` | `0` |
| `reclaim` (scratch) | `11` | — | `26,587,136` | `True` | `0` |
| `rehearse` | `13` | `284,483,584` | `55,083,008` | `True` | `0` |
| `fetch` | `14` | `272,838,656` | `79,794,176` | `True` | `0` |
| `constants` (first) | `15` | `294,424,576` | `69,562,368` | `True` | `0` |
| `constants` (second) | `16` | `295,604,224` | `69,562,368` | `True` | `0` |
| `rebate` | `17` | `316,141,568` | `76,279,808` | `True` | `0` |
| `score` (first) | `18` | — | `47,501,312` | `True` | `0` |
| `score` (second) | `19` | — | `47,894,528` | `True` | `0` |
| `still` (second) | `20` | — | `25,165,824` | `True` | `0` |
| `reclaim` (own) | not written to a file | — | `28,426,240` | `True` | `0` |

Each peak is `ru_maxrss` as the mode printed it. **Every mode printed `malloc tuned: True` and `opens under the
capture roots: 0`.** `rehearse`, `fetch`, `constants` and `rebate` each re-read `MemAvailable` at their start
through `floor_check`, and each read was above the floor `147,152,896`. **The largest peak, `fetch`'s `79,794,176`,
is above the Architect's largest, `rebate`'s `73,576,448`, from which §0.3 derived the floor**, and `rebate`'s
`76,279,808` here is above it as well. The floor is `1.84` times the largest peak this run reached, not 2 (§6 item 6).

### 2.12 §3.10 — the closing reads (V14)

§0.2's block again, then §3.10's four reads (`logs/21-closing-reads.log`):

```text
$ (§3.10: §0.2's block again)
$ S=/tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8/scratchpad
$ date -u; date -u +%s
Fri Oct  9 07:17:15 PM UTC 2026
1791573435
$ nproc; grep -E ... /proc/meminfo
1
MemTotal:         978640 kB
MemAvailable:     310448 kB
SwapTotal:       3174396 kB
SwapFree:        2799964 kB
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 12999884800
$ find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
$ grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
1
$ systemctl is-active btc-recorder.service btc-chainbook.service; echo "exit=$?"
active
active
exit=0
$ systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1
$ systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3
$ git -C /root/btc-recorder-svc rev-parse HEAD
e3975b5da44c5328adf3bf3914634cd878842c73
$ for d in /root/tz21-work /root/tz18a-svc /root/btc-recorder-svc; do test -e "$d"; echo "$d exit=$?"; done
/root/tz21-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
$ find /root/btc-forensics -type f | wc -l
1519
$ /root/tz04a-env/venv/bin/python -c ...
3.12.3
$ git worktree list
/root/btc-5m-twap       3561850 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/root/tz23-work/wt      7f5ae3f [tz-23-maker-m0]
$ du -sb /root/.claude /root/PROJECT_GAMING_PS5
191949515	/root/.claude
521368074	/root/PROJECT_GAMING_PS5
$ echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
/tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8/scratchpad
total 16
drwx------  4 root root 4096 Oct  9 18:44 .
drwx------ 16 root root 4096 Oct  9 18:39 ..
drwx------  4 root root 4096 Oct  9 18:39 5ce9f787-ea2c-5497-8888-63b97cb927e8
drwx------  3 root root 4096 Oct  9 18:39 750b3996-3a2d-49fb-823d-1321cd631528
$ systemctl show btc-recorder.service btc-chainbook.service -p MainPID -p NRestarts -p MemoryCurrent -p MemoryPeak
MainPID=4148534
NRestarts=2
MemoryCurrent=135249920
MemoryPeak=191582208

MainPID=4064090
NRestarts=1
MemoryCurrent=7573504
MemoryPeak=18735104
$ free -b
               total        used        free      shared  buff/cache   available
Mem:      1002127360   675016704   104001536      159744   409022464   327110656
Swap:     3250581504   383418368  2867163136
$ du -sb /root/tz23-work /root/.claude
86613760	/root/tz23-work
191949515	/root/.claude
$ cat /root/tz23-work/state.json /root/tz23-work/label-ledger.jsonl
{
 "constants_at": "2026-10-09T19:14:20Z",
 "constants_sha": "1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5",
 "still": {
  "at": "2026-10-09T18:44:00Z",
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
{"at":"2026-10-09T19:16:41Z","head":"7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8","member_list_sha":"699cab9aa3f540b6cdfe2ae8a295b1fa4bca96921238106dad4b243bc4ecce4f","members":4032}
{"at":"2026-10-09T19:16:52Z","head":"7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8","member_list_sha":"699cab9aa3f540b6cdfe2ae8a295b1fa4bca96921238106dad4b243bc4ecce4f","members":4032}
```

H1, H2 and H3 read as at §0.2, and both units are `active`. `telemetry-watch.service` still reads `disabled` (exit 1)
and `inactive` (exit 3). The forensic store still holds `1,519` files, because B-RECLAIM-SCRATCH copied none. The
worktree list adds this TZ's branch worktree `/root/tz23-work/wt` at `7f5ae3f`. `S`'s parent now holds this
session's own directory and the live `750b3996…`, and nothing else. `/root/tz23-work` holds `86,613,760` bytes.

The frozen rows again, at run end (`logs/23-fingerprint-end.log`) — **29 of 29 `frozen` rows byte-identical**
(§2 item 1). The primary checkout's status lists the report's draft and two ignored paths that predate this
session: `.claude/` (2026-09-19) and `research/out/` (2026-09-09):

```text
$ the §0 table's frozen rows again, at run end (§2 item 1), 2026-10-09T19:17:41Z, primary checkout at 3561850d31eb6f9ed30c097a63d251a1709c4442
reported SYSTEM-MAP.md 1160 246032 7cc5a49181ea0b4f5162bc55d320d18268aa107d75c45e5f10c0bc24c4e464fe
tracked research/tz02-distribution.py 334 14511 f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4
tracked .gitignore 5 252 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b
rows 32; frozen equal 29 of 29
CryptoTZ/TZ-23-maker-m0.md 1aedbba8991453f2a07b978e391b8c03c77cd4c76d6d780d6f4c27d51d28dec0
$ git status --porcelain --ignored   (primary checkout)
?? CryptoReports/TZ-23-maker-m0-report.md
!! .claude/
!! research/out/
```

### 2.13 Every file the run wrote, by SHA-256

`logs/24-files.log`, written after every other step but B-RECLAIM-OWN. It lists every file under `/root/tz23-work`
but the branch worktree and the two chunk caches, which §8 and §9 let go with the tree:

```text
$ every file under /root/tz23-work but the worktree and the two chunk caches, 2026-10-09T19:17:57Z
3d853dac59f8f4fd69bf14eae53c5ef080227281674ec4a85d9d5894f36f15aa         360  label-ledger.jsonl
f82854287eb69b0cdb28d0d0a279b3b825eb8e535c3f0edb8e3989c53cdbdb9c         393  state.json
332103587baa9193c2f5789529d1080cadd586223cc3b58c0d8594a2b245befc         244  logs/00a-worktree.log
ebde6bf7338de031a16c48e4281a9c88909dc48377663cb264002ecca8890fb2        6050  logs/00b-fingerprint.log
afb1aa1266933884fbfbcae8c5c5216e16fdc82a9a9e0ae83293b27db29091d4         480  logs/00c-model.log
66218c9dc6f03422ae31937021f2edf7c294e82baa07940f3904731ff15af5ea         403  logs/00d-pull.log
3d58fb058c5f0cf960b0e04e45e0ad394d8b5056d04b08c3ec0629b4ecd86a58        2136  logs/01-host-gate.log
7130056f8c6fd6608f243d9a0da5183faa9b5ffd43193fbc9e4ac8740ee1b00f        2157  logs/02-refs.log
99cf3aee6cfa5a86f5810208db2ede58d4db6aed4e254c417950a2c161077519         340  logs/03-branch.log
4bacc9e2bf9c88de3d1746cce1b9da652b0c59a1f03cf6ef83d647925f432031         343  logs/04-extract.log
8fbe1a5bc8527229e494bb4418d8fcfde1453f0a4c56ee7faabc9d3476066272         802  logs/05-commit-push.log
6835133932fdb4060aace8366d5766a789ac9b5977deba3fcf6a8d0321546bec         236  logs/06-pr.log
21230a3aeac0149d5f4c14d5b629d821a96a7fe2251bffbd4da0b254526960bc        6845  logs/07-selftest.log
83ae4e0dcc76ee07c60d0853557e17c6974af56ac13c972f5843d7f7a329d36d         529  logs/08-still-1.log
03b8b52d7ff75634ee624c0fa25bf847ff09f79fefc3c2754dee9a2bc22e1fbc         944  logs/09-scratch.log
02811655783890eda62e9b12c47ca5d09422c5eccb7c55111a553a9ddb001b86        1335  logs/10-scratch-targets.log
1d1adacfb7919c15d17a8eb152a621b78de1a742f6627b5e7f2d95dad96ae62b         625  logs/11-reclaim-scratch.log
a4337e7a0773c5c4faf99008005cf3e267df12e30ea1030517e15cb3cbda8210         684  logs/12-rm-scratch.log
e32e9c22ac577677ec0067698bdd90e50877e7609f2ed379cf6af49fe41d50a4        6022  logs/13-rehearse.log
2025d7397e24a3e4edeed43a87a59e4c312213af724db8200c8bf57e60353d94        1069  logs/14-fetch.log
d7de89ad8f646e483705dbda6ef1af23047e170cbc42731f950b874b55be7853        2276  logs/15-constants-1.log
60d3b54d315b35b1d04bd5df5172abd532a84e95f22f1a604931835ec9b1d339        2735  logs/16-constants-2.log
8b955eff52f460b9033afe56eea8fdd433eaae9d299d3473cd8a8de8c9540e89         900  logs/17-rebate.log
a5933702733a28d6524671b0f8c04f4f9f24a6b6e0f74ee08870541c40ce273d        2633  logs/18-score-1.log
d94adecf0b442dd5a494fbfca24e63dffdf92a2ce14253be45a912af103225e7        2921  logs/19-score-2.log
3ab786077bc9f3525fddbe936ad1c9fff7095f023cae91044d6d98854b6ecb20         588  logs/20-still-2.log
a6c049664c2347483735572ef3bbe4fcde20c0b84d6962a4ffc0f0dc209e28be        3365  logs/21-closing-reads.log
982d59b58b71ac20a65801e5eedea374188f6cf92dd59ae79462ab43364a4ed2         732  logs/22-separation-check.log
27af263ca874ddef2f8f758fe59d1ca8d05d13ad7413fc582d8976836894dfe2         698  logs/23-fingerprint-end.log
9f521a23b3a5b48ac7569f68a9c42bf6da1bb8ef09f5a71c0c8e091fbf5098e3        2025  rehearsal/rehearsal-constants.json
3ce50a85f84068a4cac15ece53d2ea1b16184b9080d69228b0baae8f887c8116     1055371  rehearsal/rehearsal-fills.jsonl.gz
2676af1dee730001abf560555c1c0eb9b88901209a94598dcb966495e20131d1       88078  rehearsal/rehearsal-members.csv
4cdf1a1179c0d58f048d091e0a719951cb3af38c822d49a2e9343bea5f502d1f        1906  rehearsal/rehearsal-reading.json
d31eb18fa58f8a26f12979f733fcead3b2482a480ba97a17c1145c1eef99bda2       16570  rehearsal/rehearsal-scored.csv
83a53bd3fb13829173282487833ef0398280d358377e0f09d0beb414c7829cbc       82728  rehearsal/set.json
a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303     2314799  set/set.json
1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5        2114  set/tz23-constants.json
4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64    36870673  set/tz23-fills.jsonl.gz
cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61     2444450  set/tz23-members.csv
fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043        1915  set/tz23-reading.json
12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988      464610  set/tz23-scored.csv
chunk cache rehearsal/cache: 8 files, 1068929 bytes (not named, goes with the tree)
chunk cache set/cache: 202 files, 37239598 bytes (not named, goes with the tree)
worktree wt/: 0 status lines; HEAD 7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8 upstream 7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8
```

`logs/24-files.log` itself: 4,517 bytes, SHA-256 `64c60596f4eac4fb21a15cf91cf8fc0a4e09b267d2d3f961d09e77a586c802ae`. The branch worktree held exactly its pushed `HEAD`, with no status line:
its one written file is `research/tz23-maker-m0.py`, `6b3ace2c…` (§2.1), in git. The self-test's transient tree
`/root/tz23-work/selftest-tmp` was removed by the self-test itself. In the primary checkout the run wrote this report
and, in `.git`, the branch `tz-23-maker-m0` and the worktree's registration.

### 2.14 §9 B-RECLAIM-OWN — last, after §3.10, with this report drafted

B-RECLAIM-OWN ran after §3.10 and after this report was drafted in the primary checkout. Its output was written to
no file, as §9 orders. Each line ran as its own command, so that a refusal of one would not discard the others, and
**none was refused by the session's classifier**. The output below is quoted from the session, with each command's
UTC stamp printed in front of it:

```text
2026-10-09T19:22:49Z
$ I reclaim /root/tz23-work
[2026-10-09T19:22:49Z] reclaim: 1786 report tokens; forensic store holds 1519 files
[2026-10-09T19:22:49Z] reclaim: /root/tz23-work/wt skipped: no file but its HEAD's, and HEAD 7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8 is its upstream's
[2026-10-09T19:22:49Z] R copied 3d853dac59f8f4fd69bf14eae53c5ef080227281674ec4a85d9d5894f36f15aa /root/btc-forensics/tz23-work--label-ledger.jsonl
[2026-10-09T19:22:49Z] R copied f82854287eb69b0cdb28d0d0a279b3b825eb8e535c3f0edb8e3989c53cdbdb9c /root/btc-forensics/tz23-work--state.json
[2026-10-09T19:22:49Z] R copied 332103587baa9193c2f5789529d1080cadd586223cc3b58c0d8594a2b245befc /root/btc-forensics/tz23-work--logs--00a-worktree.log
[2026-10-09T19:22:49Z] R copied ebde6bf7338de031a16c48e4281a9c88909dc48377663cb264002ecca8890fb2 /root/btc-forensics/tz23-work--logs--00b-fingerprint.log
[2026-10-09T19:22:49Z] R copied afb1aa1266933884fbfbcae8c5c5216e16fdc82a9a9e0ae83293b27db29091d4 /root/btc-forensics/tz23-work--logs--00c-model.log
[2026-10-09T19:22:49Z] R copied 66218c9dc6f03422ae31937021f2edf7c294e82baa07940f3904731ff15af5ea /root/btc-forensics/tz23-work--logs--00d-pull.log
[2026-10-09T19:22:49Z] R copied 3d58fb058c5f0cf960b0e04e45e0ad394d8b5056d04b08c3ec0629b4ecd86a58 /root/btc-forensics/tz23-work--logs--01-host-gate.log
[2026-10-09T19:22:49Z] R copied 7130056f8c6fd6608f243d9a0da5183faa9b5ffd43193fbc9e4ac8740ee1b00f /root/btc-forensics/tz23-work--logs--02-refs.log
[2026-10-09T19:22:49Z] R copied 99cf3aee6cfa5a86f5810208db2ede58d4db6aed4e254c417950a2c161077519 /root/btc-forensics/tz23-work--logs--03-branch.log
[2026-10-09T19:22:49Z] R copied 4bacc9e2bf9c88de3d1746cce1b9da652b0c59a1f03cf6ef83d647925f432031 /root/btc-forensics/tz23-work--logs--04-extract.log
[2026-10-09T19:22:49Z] R copied 8fbe1a5bc8527229e494bb4418d8fcfde1453f0a4c56ee7faabc9d3476066272 /root/btc-forensics/tz23-work--logs--05-commit-push.log
[2026-10-09T19:22:49Z] R copied 6835133932fdb4060aace8366d5766a789ac9b5977deba3fcf6a8d0321546bec /root/btc-forensics/tz23-work--logs--06-pr.log
[2026-10-09T19:22:49Z] R copied 21230a3aeac0149d5f4c14d5b629d821a96a7fe2251bffbd4da0b254526960bc /root/btc-forensics/tz23-work--logs--07-selftest.log
[2026-10-09T19:22:49Z] R copied 83ae4e0dcc76ee07c60d0853557e17c6974af56ac13c972f5843d7f7a329d36d /root/btc-forensics/tz23-work--logs--08-still-1.log
[2026-10-09T19:22:49Z] R copied 03b8b52d7ff75634ee624c0fa25bf847ff09f79fefc3c2754dee9a2bc22e1fbc /root/btc-forensics/tz23-work--logs--09-scratch.log
[2026-10-09T19:22:49Z] R copied 02811655783890eda62e9b12c47ca5d09422c5eccb7c55111a553a9ddb001b86 /root/btc-forensics/tz23-work--logs--10-scratch-targets.log
[2026-10-09T19:22:49Z] R copied 1d1adacfb7919c15d17a8eb152a621b78de1a742f6627b5e7f2d95dad96ae62b /root/btc-forensics/tz23-work--logs--11-reclaim-scratch.log
[2026-10-09T19:22:49Z] R copied a4337e7a0773c5c4faf99008005cf3e267df12e30ea1030517e15cb3cbda8210 /root/btc-forensics/tz23-work--logs--12-rm-scratch.log
[2026-10-09T19:22:49Z] R copied e32e9c22ac577677ec0067698bdd90e50877e7609f2ed379cf6af49fe41d50a4 /root/btc-forensics/tz23-work--logs--13-rehearse.log
[2026-10-09T19:22:49Z] R copied 2025d7397e24a3e4edeed43a87a59e4c312213af724db8200c8bf57e60353d94 /root/btc-forensics/tz23-work--logs--14-fetch.log
[2026-10-09T19:22:49Z] R copied d7de89ad8f646e483705dbda6ef1af23047e170cbc42731f950b874b55be7853 /root/btc-forensics/tz23-work--logs--15-constants-1.log
[2026-10-09T19:22:49Z] R copied 60d3b54d315b35b1d04bd5df5172abd532a84e95f22f1a604931835ec9b1d339 /root/btc-forensics/tz23-work--logs--16-constants-2.log
[2026-10-09T19:22:49Z] R copied 8b955eff52f460b9033afe56eea8fdd433eaae9d299d3473cd8a8de8c9540e89 /root/btc-forensics/tz23-work--logs--17-rebate.log
[2026-10-09T19:22:49Z] R copied a5933702733a28d6524671b0f8c04f4f9f24a6b6e0f74ee08870541c40ce273d /root/btc-forensics/tz23-work--logs--18-score-1.log
[2026-10-09T19:22:49Z] R copied d94adecf0b442dd5a494fbfca24e63dffdf92a2ce14253be45a912af103225e7 /root/btc-forensics/tz23-work--logs--19-score-2.log
[2026-10-09T19:22:49Z] R copied 3ab786077bc9f3525fddbe936ad1c9fff7095f023cae91044d6d98854b6ecb20 /root/btc-forensics/tz23-work--logs--20-still-2.log
[2026-10-09T19:22:49Z] R copied a6c049664c2347483735572ef3bbe4fcde20c0b84d6962a4ffc0f0dc209e28be /root/btc-forensics/tz23-work--logs--21-closing-reads.log
[2026-10-09T19:22:49Z] R copied 982d59b58b71ac20a65801e5eedea374188f6cf92dd59ae79462ab43364a4ed2 /root/btc-forensics/tz23-work--logs--22-separation-check.log
[2026-10-09T19:22:49Z] R copied 27af263ca874ddef2f8f758fe59d1ca8d05d13ad7413fc582d8976836894dfe2 /root/btc-forensics/tz23-work--logs--23-fingerprint-end.log
[2026-10-09T19:22:49Z] R copied 64c60596f4eac4fb21a15cf91cf8fc0a4e09b267d2d3f961d09e77a586c802ae /root/btc-forensics/tz23-work--logs--24-files.log
[2026-10-09T19:22:49Z] R copied 9f521a23b3a5b48ac7569f68a9c42bf6da1bb8ef09f5a71c0c8e091fbf5098e3 /root/btc-forensics/tz23-work--rehearsal--rehearsal-constants.json
[2026-10-09T19:22:49Z] R copied 3ce50a85f84068a4cac15ece53d2ea1b16184b9080d69228b0baae8f887c8116 /root/btc-forensics/tz23-work--rehearsal--rehearsal-fills.jsonl.gz
[2026-10-09T19:22:49Z] R copied 2676af1dee730001abf560555c1c0eb9b88901209a94598dcb966495e20131d1 /root/btc-forensics/tz23-work--rehearsal--rehearsal-members.csv
[2026-10-09T19:22:49Z] R copied 4cdf1a1179c0d58f048d091e0a719951cb3af38c822d49a2e9343bea5f502d1f /root/btc-forensics/tz23-work--rehearsal--rehearsal-reading.json
[2026-10-09T19:22:49Z] R copied d31eb18fa58f8a26f12979f733fcead3b2482a480ba97a17c1145c1eef99bda2 /root/btc-forensics/tz23-work--rehearsal--rehearsal-scored.csv
[2026-10-09T19:22:49Z] R copied 83a53bd3fb13829173282487833ef0398280d358377e0f09d0beb414c7829cbc /root/btc-forensics/tz23-work--rehearsal--set.json
[2026-10-09T19:22:49Z] R copied a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303 /root/btc-forensics/tz23-work--set--set.json
[2026-10-09T19:22:49Z] R copied 1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5 /root/btc-forensics/tz23-work--set--tz23-constants.json
[2026-10-09T19:22:49Z] R copied 4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64 /root/btc-forensics/tz23-work--set--tz23-fills.jsonl.gz
[2026-10-09T19:22:49Z] R copied cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61 /root/btc-forensics/tz23-work--set--tz23-members.csv
[2026-10-09T19:22:49Z] R copied fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043 /root/btc-forensics/tz23-work--set--tz23-reading.json
[2026-10-09T19:22:49Z] R copied 12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988 /root/btc-forensics/tz23-work--set--tz23-scored.csv
[2026-10-09T19:22:50Z] RECLAIM PASS: 252 files considered, 42 named by a report, 0 kept by name, 42 copied, 0 already held; forensic store 1519 -> 1561 files
[2026-10-09T19:22:50Z] malloc tuned: True
[2026-10-09T19:22:50Z] peak memory of this run: 28426240 bytes
[2026-10-09T19:22:50Z] opens under the capture roots: 0
exit=0

2026-10-09T19:22:56Z
$ git -C /root/btc-5m-twap worktree remove /root/tz23-work/wt; echo "exit=$?"
exit=0

2026-10-09T19:23:00Z
$ rm -rf /root/tz23-work; echo "exit=$?"
exit=0

2026-10-09T19:23:06Z
$ test -e /root/tz23-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       3561850 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
1561
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13043306496
2026-10-09T19:23:06Z
```

**RECLAIM PASS: 252 files considered, 42 named by a report, 0 kept by name, 42 copied, 0 already held; the forensic
store `1,519` → `1,561`.** The 42 are every file of §2.13's list: `state.json`, `label-ledger.jsonl`, the 28 logs and
the 12 output files of the set and the rehearsal. `reclaim` counts a file "kept by name" only where no report names
its hash, and this draft named all 42, so the count is 0. The other 210 files considered are the two chunk caches,
8 + 202, which no report names and which went with the tree. The worktree was skipped as pristine at its upstream
`7f5ae3f`, and `git worktree remove` needed no `--force`. Every copy was re-hashed by `reclaim` at its destination.
The list above was then re-checked against the store by SHA-256, 42 of 42. The branch `tz-23-maker-m0` stays on
`origin` and as a local ref at `7f5ae3f`; only its working tree went.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-23-maker-m0`, committed at 18:43:30 UTC and pushed before the pull request was opened; it stays on `origin` and as a local ref |
| implementation commit | `7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8`, parent `3561850` |
| pull request | #23, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/23`, open against `main`, head `7f5ae3f`, **not merged** |
| Release | none; none is required, and no dataset, archive or binary entered git history |
| report | this file, straight to `main`, one commit |

**Contract §4.2's self-check (V13)**, run at 19:17:25 UTC, after the push and the pull request and before this
report's commit (`logs/22-separation-check.log`):

```text
Fri Oct  9 07:17:25 PM UTC 2026
fetch exit=0
$ git rev-list origin/main | grep -c 7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8
0
$ git diff --name-only origin/main origin/tz-23-maker-m0
research/tz23-maker-m0.py
$ git diff --name-status origin/main origin/tz-23-maker-m0
A	research/tz23-maker-m0.py
$ git diff --numstat origin/main origin/tz-23-maker-m0
1184	0	research/tz23-maker-m0.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
grep exit=1
3561850d31eb6f9ed30c097a63d251a1709c4442
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8
{"baseRefName":"main","headRefOid":"7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8","mergedAt":null,"number":23,"state":"OPEN","url":"https://github.com/seahomebatumi-ai/btc-5m-twap/pull/23"}
```

The first line prints `0`. The diff names exactly one path, `A`, 1,184 insertions. The `grep` prints nothing.

---

## 4. Gate

| gate | quoted from TZ-23 §4 | deciding numbers | reading |
|---|---|---|---|
| **G-REHEARSAL** | "§4.1's 10 figures equal, exactly" | 10 of 10 equal as values: members `144`, Up `75`, `n` `128,031`, shares `3509409.854401`, `X` `-44336.003951`, `C` `-108894.2181475504884399`, `R` `8015.91427290719561009665372913342`, `V` `2140569358.582178867947`, `Σ X·up` `-88853.166114`, `S` `28056.96630645768404999665372913342` | **PASS** |
| **G-SET** | "4,032 members; every chunk fetched, every row on its market and its token, every chunk read back" | `4,032` members of `4,032` considered; `202` chunks, each fed to its end and read back | **PASS** |
| **M0** | "`S >= thr`: EARN … `S <= δ · Sh − thr`: NO EARN … otherwise UNDECIDABLE" | `S` = **`272424.113`**; `thr` = `432484.391`; `δ·Sh − thr` = `213644.297`; margins `-160060.279` and `-58779.816` | **UNDECIDABLE** |
| **G-STILL** | "`MainPID`, `NRestarts` and `ActiveState` unchanged" | recorder `4148534` / `2` / `active`, chain book `4064090` / `1` / `active`, at both reads | **PASS** |

**M0 reads UNDECIDABLE.** Each answer was tested at `α = 0.005`, `δ = 0.005`, `λ = 0.000021932`, as fixed. To three
decimals, `S` is `272,424.113` USDC, below EARN's `432,484.391` and above NO EARN's `213,644.297`. Per share, at three
significant figures, it is `0.00211`, against `0.00335` and `0.00165`. The power before any label was `0.947`, and no
row reads it. Nothing was tuned, and no gate was re-read. **TZ §1 item 3: UNDECIDABLE opens the second look.** A
later TZ may extend the same sum over the qualifying markets after `1791241800` with this `α`, `λ` and `δ` (TZ §1).

---

## 5. Validation

| # | check | count | asserted |
|---|---|---|---|
| **V1** | §0.1's fingerprint | 6 anchors equal, **4 of 4** re-derived, **29 of 29** `frozen` equal, 2 `tracked`, 1 `reported`; 32 rows | compared by the fingerprint script, which prints PASS only on all of them; recorded, not asserted (no `assert`) |
| **V2** | §0.2's host gate | H1, H2, H3, the memory gate and the disk gate, PASS; the rest printed (§0.2) | recorded, not asserted: compared by the Executor |
| **V3** | §3.1's file | **1 of 1** hash asserted by §3.1's script; 1,184 lines and 54,885 bytes by `wc`; the diff against `origin/main` names exactly one path, `A`, 1,184 lines | the hash asserted; lines, bytes and the diff recorded |
| **V4** | the self-test | **`59 of 59`** | asserted, exit 0 |
| **V5** | G-REHEARSAL | **10 of 10** figures equal | asserted, exit 0 |
| **V6** | G-SET | **4,032** members; **4,032** candidates considered; **0** non-members, so none with a reason; by segment `1: 1560, 2: 1992, 3: 480` | asserted, exit 0 (`G-SET PASS`); the set's figures printed by `constants` |
| **V7** | the constants, twice | **3 of 3** files `unchanged` at the second run | asserted by `write_once` and the fills comparison, exit 0 |
| **V8** | the rebate check | **64 of 64** sampled members' taker rows equal to the cache; the four recorded figures (§2.8) | the equality asserted; the four figures recorded, not asserted |
| **V9** | the score, twice | the reading **UNDECIDABLE**; **2 of 2** files `unchanged`; **2** ledger lines | asserted by `write_once`, exit 0 |
| **V10** | G-STILL | both units unchanged: **PASS** | printed by `still`; recorded, not asserted (the mode prints FAIL rather than raising) |
| **V11** | opens under the capture roots | `0` printed by every mode, **13 of 13** runs (§2.11) | the audit hook raises on a refusal; no run raised |
| **V12** | memory | every mode's printed peak in §2.11, the largest `79,794,176` against the floor `147,152,896`; `malloc tuned: True` at **13 of 13** runs | the floor and the settings asserted at the start of the four reading modes; the peaks recorded |
| **V13** | contract §4.2's self-check | `0`; 1 path; nothing | recorded; run after the push and the pull request, before this report's commit (§3) |
| **V14** | §3.10's closing reads | every read printed (§2.12) | recorded, not asserted |
| **V15** | §9's `reclaim` runs | scratch: considered `7`, named by a report `0`, kept by name `0`, copied `0`, already held `0`, store `1,519` → `1,519`; own: considered `252`, named `42`, kept by name `0`, copied `42`, already held `0`, store `1,519` → `1,561`; the worktree skipped, pristine at its upstream | `after == before + copied` asserted in each |
| **V16** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz23-work` and for each of the **3** scratch directories removed (§2.4); `git worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else | recorded, not asserted: exit statuses read |

---

## 6. What could not be implemented as written

1. **Contract §1 steps 1 and 2 ran before §0.0's `mkdir`, so their first run is in no log.** The session's
   first `git fetch origin main` and `git merge --ff-only origin/main` moved local `main` from `c8636f7` to
   `3561850` before the TZ was read. After the `mkdir`, `git checkout main && git pull` was run again for the
   record (`logs/00d-pull.log`): `Already up to date`.
2. **`S` was taken from the session's system prompt.** §0.2 sets `S` to "this session's scratchpad directory as
   the session's own environment names it". No environment variable of the session names a scratchpad. The system
   prompt names `/tmp/claude-0/-root-btc-5m-twap/5ce9f787-ea2c-5497-8888-63b97cb927e8/scratchpad`, and
   `CLAUDE_CODE_SESSION_ID` is `5ce9f787-ea2c-5497-8888-63b97cb927e8`, the same directory. The model was read with the
   session's `get_session` tool, not a shell command, and `logs/00c-model.log` records what it returned.
3. **Reads the TZ does not name, none under a capture root.**
   - Contract §1 steps 3 and 4 fix no command. The fingerprint was taken by the Executor's own script, which
     compares and prints PASS or BLOCKED but does not `assert` (`logs/00b-fingerprint.log`). It was repeated at run
     end for §2 item 1 (`logs/23-fingerprint-end.log`).
   - Before B-RECLAIM-SCRATCH the Executor ran `du -sb` and `find` on the three earlier directories, to look at what
     it would remove (`logs/10-scratch-targets.log`).
   - `logs/24-files.log` hashes every file the run wrote, for §8.
   - Some reads printed to the session only and are in no log: one `ls -la /root/tz23-work` before §3.3; during the
     fetch, the log's tail, `MemAvailable` from `/proc/meminfo`, the fetch process's `ps` line and the cache's
     `du -sb`; and, after the score, the key names and sums of `tz23-reading.json` and `tz23-constants.json`,
     which §2.9 quotes. None of them printed a single fill's, member's or market's price, size or outcome.
4. **`I reclaim` ran once, with the three earlier directories as its arguments.** §9's block writes
   `I reclaim <each earlier directory, by its full path>` and then one `rm -rf` per directory. The Executor read it
   as one `reclaim` naming each directory, which `reclaim TREE...` takes. That run printed `RECLAIM PASS` before
   the first removal.
5. **Where the session's harness keeps output.** Every command wrote its output to `/root/tz23-work/logs/` first, and
   nothing was written to the scratchpad, which is empty. The harness also keeps its own copy of each background
   command's and each watch's terminal output, as files under `/tmp/claude-0/-root-btc-5m-twap/5ce9f787…/tasks/`,
   beside the scratchpad (map §7 item 95). Here that is: the fetch's (22 bytes, its output went to the log); a
   watch's matching lines of the fetch log (chunk counts and `G-SET PASS`); two waits' tails of that log; and the
   rebate run's `cat` of its own log, sums only. The next TZ's B-RECLAIM-SCRATCH removes them with this session's
   directory. B-RECLAIM-OWN's output was written to no file, as §9 orders, and §2.14 quotes it from the session.
6. **A reading for the next TZ, not a deviation: two modes peaked above the Architect's largest peak.** §0.3 sets the
   floor `147,152,896` at twice `rebate`'s `73,576,448`. Here `fetch` peaked at `79,794,176` over the 4,032 members,
   where the Architect measured `fetch`, `constants` and `score` together at `64,159,744` over 576, and `rebate` at
   `76,279,808`. The floor is `1.84` times the
   largest, not 2 (map §7 item 93's rule). Every `MemAvailable` read was at least `255,062,016`, so the floor was
   never close. The floor is fixed by the TZ and not re-derived here.
7. **`reclaim` own read this report's draft as well as the committed reports.** §8 orders the report drafted in the
   primary checkout before B-RECLAIM-OWN, and `report_tokens` reads every `.md` in `CryptoReports/`, committed or
   not, so the draft's hashes are what named this run's outputs for the forensic store. After B-RECLAIM-OWN the
   draft was changed in two ways. First, §2.14, §0.3's last row, §2.11's last row, V15, V16 and the opening's last
   sentence were filled from B-RECLAIM-OWN's output. Second, three passages were reworded: the opening table's
   capture row, the sentence below that table, and that last sentence's line breaks. Every `logs/` block in §0 to §3
   was filled by script from the logs before B-RECLAIM-OWN, and all 29 equal their copies in the forensic store byte
   for byte, checked after B-RECLAIM-OWN.

