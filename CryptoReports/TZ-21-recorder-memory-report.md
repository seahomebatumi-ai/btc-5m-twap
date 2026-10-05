# TZ-21 report — the recorder's memory, bounded

**READING: PASS at every gate.** G-SYNTH **913** slices byte-identical — 836 from memory against 600, 77 from disk
against 60 — at most **242** records held against 2,000, both controls detected · G-EQUIV **825** windows of the
capture's own `runtime.jsonl` byte-identical — 23 from memory against 12, 802 from disk against 200 — **233**
records held against the old code's **62,362** · G-PATH P0 to P4 at the first run · G-RESTART PASS, the gap
**6.771 s** against 60, recorded · G-REC manifests, `quotes_complete` and sha 5 of 5, `complete` **5 of 5**
against a pass mark of 3, slices equal **7 of 7** · G-FINAL PASS · G-CB-STILL PASS.

**The recorder runs the bounded code as a system unit, and no block of §4.7 was run.** At `I final` (23:08:22
UTC) `btc-recorder.service` ran as pid `4148534`, `NRestarts` `2`, from `/root/btc-recorder-svc` at the branch head
`e3975b5da44c5328adf3bf3914634cd878842c73`, `recorder.py` `0f6c9045…`. It was the sole instance of its argv, inside
`/system.slice/btc-recorder.service`, and its newest `start` record names the branch head. The chain book kept pid
`4064090` and `NRestarts` `1` from `I state` to `I final`. These were read by the Executor from systemd and
`/proc`, never from an account.

**The old code's memory beside the new.** After 13 h 40 min the old process held `11,247,616` bytes `anon` and
`87,597,056` in swap; systemd's journal put its peak at `201.8M`, with `83.5M` of swap. At `I final`, 46 min
after its start, the new process held `11,075,584` `anon` and `11,550,720` in swap, its peak `52,322,304`
(§2.13). The new process holds about two hours of runtime records instead of every record since 2026-09-10.

**One block was partly refused by the session's classifier:** three of B-RECLAIM-SCRATCH's ten `rm -rf`.
The Boss ran the three verbatim, in a root shell. The Executor verified each by `test -e` at 00:46:52 UTC on
2026-10-05: all three exit `1`. B-MOVE, B-KILL-REC and the rest of §9 were not refused.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-21-recorder-memory.md`, 2,862 lines, 151,912 bytes, SHA-256 `92d72640b0673381f0c4b0ccb2077312e7575febc31bbaf655da0264524eebe8`, landed at `c3828d0` |
| map revision | `2026-10-04-b`, equal; anchors 6 of 6; re-derived 4 of 4; rows hashed 31; `frozen` equal 28 of 28 |
| executor model | Opus, as the TZ names |
| branch | `tz-21-recorder-memory` at `e3975b5da44c5328adf3bf3914634cd878842c73`, pushed; pull request #22, open, not merged |
| recorder code | `/root/btc-recorder-svc`, a detached worktree, moved by B-MOVE from `4216c04` to `e3975b5`; `recorder.py` `0f6c9045…`, `config.py` `8111dfe4…`, `manifest.py` `79c99010…` |
| recorder unit | `btc-recorder.service`, unchanged: the installed file is `main`'s `deploy/systemd/btc-recorder.service` byte for byte, `MemoryMax` `536870912` |
| chain book | `btc-chainbook.service`, read only, never signalled: pid `4064090`, `NRestarts` `1`, from `I state` to `I final` |
| pricer | not read, not called, not scored; `A6` `729f0bcdbee3` is stated so that what was not scored is not in doubt |

No price, size, spread, mid, book level, outcome or label was read, printed or written by this TZ's commands.
G-PATH printed statuses, byte counts, whether each body parsed, two token ids, SNTP offsets and round trips, and
the RTDS frame count and topics (§2 item 6). `reclaim` read the reports for hex runs alone and copied whole files
without extracting a value from them (§2 item 6's §9 exemption).

---

## 0. Fingerprint

**Revision string read:** `2026-10-04-b`, equal to the value TZ-21's header requires. Contract §1's
`git checkout main && git pull` found `main` already at `c3828d031109beaaef67a6189112317695259101`: the session's
first `git fetch origin main` and a `git merge --ff-only origin/main` had moved local `main` from `d2d781a`
to `c3828d0` before the TZ was read. Those two ran before §0.0's `mkdir`, so no log holds them;
`logs/00-start.log` holds the pull. The map and the TZ were read at `c3828d0`.

§0.0's `mkdir`, then contract §1's pull (`logs/00-start.log`):

```text
$ mkdir /root/tz21-work /root/tz21-work/logs; echo "exit=$?"
exit=0

$ git checkout main && git pull
Already on 'main'
Your branch is up to date with 'origin/main'.
Already up to date.
exit=0
c3828d031109beaaef67a6189112317695259101
c3828d0 Add files via upload
e7d9954 Update SYSTEM-MAP.md
c7a45ff Merge pull request #21 from seahomebatumi-ai/tz-20-capture-under-systemd
$ git status --porcelain
Sun Oct  4 10:05:14 PM UTC 2026
```

| anchor | required | read from the map | re-derived from the file | verdict |
|---|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | not a file anchor | equal |
| `A2` — collector | `6c5089330629` | `6c5089330629` | `6c5089330629` | equal |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | same | not a file anchor | equal |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | `437b45ea196b` | equal |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | `9fd1c7de0f74` | equal |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3` | `729f0bcdbee3` | equal |

### 0.1 The 31 rows of the map's §0 table (V1)

The table was parsed from the map at `c3828d0`, and every path was hashed in the primary checkout. Each `frozen`
row was asserted equal in lines, bytes and SHA-256; the script ends in an assert on `(28, 28, 2, 1)`. Its output,
verbatim (`logs/00-fingerprint.log`):

```text
main HEAD c3828d031109beaaef67a6189112317695259101
revision: TZ requires 2026-10-04-b, map states 2026-10-04-b, equal True
anchors TZ  {'A1': '229a944f2d51', 'A2': '6c5089330629', 'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable', 'A4': '437b45ea196b', 'A5': '9fd1c7de0f74', 'A6': '729f0bcdbee3'}
anchors map {'A1': '229a944f2d51', 'A2': '6c5089330629', 'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable', 'A4': '437b45ea196b', 'A5': '9fd1c7de0f74', 'A6': '729f0bcdbee3'}
re-derived A2 = 6c5089330629 (research/twap-divergence.py) required 6c5089330629 equal True
re-derived A4 = 437b45ea196b (BTC-EXECUTOR-INSTRUCTIONS.md) required 437b45ea196b equal True
re-derived A5 = 9fd1c7de0f74 (research/recorder/recorder.py) required 9fd1c7de0f74 equal True
re-derived A6 = 729f0bcdbee3 (research/pfair.py) required 729f0bcdbee3 equal True
rows 31
| path | lines | bytes | state | sha256 | map | equal |
| SYSTEM-MAP.md | 1117 | 230008 | reported | 676631be64e1943d2418c3cf2b436c4e49747f4d6a7460b2d1dce4183b889b04 | — — | - |
| BTC-EXECUTOR-INSTRUCTIONS.md | 234 | 11128 | frozen | 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b | 234 11,128 437b45ea196b | True |
| research/twap-divergence.py | 1135 | 50928 | frozen | 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 | 1,135 50,928 6c5089330629 | True |
| research/selftest-twap-divergence.py | 376 | 16736 | frozen | ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a | 376 16,736 ed22e52f6dc5 | True |
| research/tz02-distribution.py | 334 | 14511 | tracked | f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 | 334 14,511 | - |
| research/pfair.py | 441 | 19357 | frozen | 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 | 441 19,357 729f0bcdbee3 | True |
| research/selftest-pfair.py | 619 | 32559 | frozen | b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa | 619 32,559 b4420feb9602 | True |
| research/tz06-calibration.py | 577 | 27138 | frozen | 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f | 577 27,138 715b4ae0eb0a | True |
| research/tz07a-variance-time.py | 623 | 28414 | frozen | 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 | 623 28,414 513e808811e6 | True |
| research/tz07b-settlement-dispersion.py | 515 | 24926 | frozen | 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc | 515 24,926 424e07344d74 | True |
| research/tz08a-out-of-sample.py | 745 | 38822 | frozen | 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c | 745 38,822 37001deff180 | True |
| research/tz09-disk-inventory.py | 894 | 41004 | frozen | b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 | 894 41,004 b2dabb6a2b19 | True |
| research/tz10b-sigma-or-link.py | 1224 | 61018 | frozen | 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 | 1,224 61,018 406b6d1145f2 | True |
| research/tz11a-student-link.py | 1231 | 64732 | frozen | 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 | 1,231 64,732 0f0525852e07 | True |
| research/tz12-sized-gate.py | 1157 | 61637 | frozen | d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 | 1,157 61,637 d2769c201932 | True |
| research/tz13-sized-gate-test3.py | 1074 | 53901 | frozen | a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd | 1,074 53,901 a67b00c95974 | True |
| research/tz14-quote-inventory.py | 2124 | 109972 | frozen | 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 | 2,124 109,972 978ee4ff9927 | True |
| research/tz15-phase2-gate.py | 1517 | 73799 | frozen | 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 | 1,517 73,799 66ac0ae0fdd2 | True |
| research/tz16a-phase2-decisive-gate.py | 2198 | 111192 | frozen | 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 | 2,198 111,192 3cae67ee7a21 | True |
| research/tz17-settlement-chain.py | 1102 | 38622 | frozen | e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 | 1,102 38,622 e18834241760 | True |
| research/tz18a-chainbook-capture.py | 1683 | 69517 | frozen | e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae | 1,683 69,517 e9cb9b478fe4 | True |
| research/tz20-capture-under-systemd.py | 771 | 36528 | frozen | 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7 | 771 36,528 104c93cee028 | True |
| research/recorder/recorder.py | 608 | 25658 | frozen | 9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03 | 608 25,658 9fd1c7de0f74 | True |
| research/recorder/config.py | 112 | 4773 | frozen | 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d | 112 4,773 8111dfe473ee | True |
| research/recorder/manifest.py | 254 | 10002 | frozen | 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 | 254 10,002 79c99010a1c3 | True |
| research/recorder/analyze.py | 813 | 34705 | frozen | eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d | 813 34,705 eb595cad79b0 | True |
| research/recorder/probe.py | 227 | 9324 | frozen | 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 | 227 9,324 50b8c269f671 | True |
| research/recorder/selftest.py | 573 | 30591 | frozen | c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 | 573 30,591 c3d9d75d55c1 | True |
| deploy/systemd/btc-recorder.service | 23 | 707 | frozen | 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1 | 23 707 3cd713fb0cca | True |
| deploy/systemd/btc-chainbook.service | 22 | 724 | frozen | a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2 | 22 724 a7b042fee8f8 | True |
| .gitignore | 5 | 252 | tracked | 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b | 5 252 | - |
frozen 28, equal 28; tracked 2; reported 1
FINGERPRINT PASS: revision 2026-10-04-b, 6 anchors equal, 4 re-derived, 28 of 28 frozen equal
```

`SYSTEM-MAP.md` is the `reported` row: 1,117 lines, 230,008 bytes, SHA-256
`676631be64e1943d2418c3cf2b436c4e49747f4d6a7460b2d1dce4183b889b04`. The script's first run stopped on an assert
of its own before any row was hashed: its split of the TZ's header on `---` cut at the anchor table's separator
line, so it read no anchors from the TZ. It was corrected to split on a line holding `---` alone and re-run; that
run is the log above (§6 item 1).

### 0.2 Host gate — the opening reads, verbatim (V2)

`S` was set to this session's scratchpad directory,
`/tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6/scratchpad`. The block ran from
`/root/btc-5m-twap` into `logs/01-host-gate.log`:

```text
Sun Oct  4 10:05:55 PM UTC 2026
1791151555
1
MemTotal:         978640 kB
MemAvailable:     260248 kB
SwapTotal:       3174396 kB
SwapFree:        2850200 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13309214720
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
3
systemd 255 (255.4-1ubuntu8.17)
enabled
enabled
exit=0
active
active
exit=0
4067771
exit=0
4064090
exit=0
exit=0
exit=0
4216c04673ced76b5b2ac60ef57c9abedc46f9b9
-- No entries --
487901585	/root/PROJECT_GAMING_PS5
disabled
exit=1
inactive
exit=3
/root/tz16a-work exit=1
/root/tz19-work exit=1
/root/tz20-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
1438
3.12.3 17.1
/root/btc-5m-twap       c3828d0 [main]
/root/btc-recorder-svc  4216c04 (detached HEAD)
206456743	/root/.claude
/tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6/scratchpad
total 60
drwx------ 15 root root 4096 Oct  4 22:04 .
drwx------ 12 root root 4096 Oct  4 22:04 ..
drwx------  4 root root 4096 Oct  4 07:28 11598617-425a-5b99-80eb-4a598104a560
drwx------  3 root root 4096 Oct  4 19:04 386a2f9a-9175-46e4-af0d-52cc5355a34c
drwx------  4 root root 4096 Oct  4 07:30 53daae24-51d9-5cf9-898f-16e726729ed2
drwx------  4 root root 4096 Oct  3 22:32 563ca246-a14d-524d-9f7b-7fbc748ed7c6
drwx------  3 root root 4096 Oct  3 22:28 6e88615c-345d-5a08-be99-6375cc1a1073
drwx------  3 root root 4096 Oct  4 07:28 7d1570e9-8d72-42b9-9919-348b3b338d30
drwx------  3 root root 4096 Oct  3 22:28 8ec90b6c-b641-47ff-bee9-df7131656d41
drwx------  3 root root 4096 Oct  4 22:04 9b05d639-af52-44b6-9a8c-9f508f7b17c4
drwx------  3 root root 4096 Oct  3 11:27 9be611ff-a833-4160-a076-c4e5a9ca4cc0
drwx------  3 root root 4096 Oct  3 11:27 a1c28db0-d13b-5013-a8c5-f8af6a1415be
drwx------  3 root root 4096 Oct  4 07:30 afca1dc1-0c42-49f8-af8c-b49f3c635ea6
drwx------  3 root root 4096 Oct  3 22:32 cca925dd-1c79-41bd-87c9-4c6662750d7e
drwx------  4 root root 4096 Oct  4 22:04 f1dda509-7343-505e-8afa-097e9a463ab6
```

| read | required | read | verdict |
|---|---|---|---|
| **H1** | `find` prints exactly one path | one path, `/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json` | PASS |
| **H2** | source `/dev/vda2`, size `31612203008`; `grep -c` at least `1` | `/dev/vda2`, `31612203008`; `3` | PASS |
| **H3** | `enabled` twice and `exit=0`; `active` twice and `exit=0`; each `pgrep -fx` one pid and `exit=0` | `enabled enabled exit=0`; `active active exit=0`; `4067771 exit=0`; `4064090 exit=0` | PASS |
| **H4** | both `cmp` exit `0` | `exit=0`, `exit=0` | PASS |
| **H5** | `/root/btc-recorder-svc` at `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | PASS |
| **H6** | `tz16a-work`, `tz19-work`, `tz20-work` exit `1`; `tz18a-svc`, `btc-recorder-svc` exit `0` | `1`, `1`, `1`; `0`, `0` | PASS |
| **H7** | the forensic store holds exactly `1,438` files | `1438` | PASS |
| **H8** | `3.12.` and a `websockets` version | `3.12.3 17.1` | PASS |
| **H9** | `git worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else | those two | PASS |
| **memory gate** | `MemAvailable` at least `110,000,000` bytes | `260248 kB` = `266,493,952` bytes | PASS |
| **disk gate** | `avail` at least `2,300,000,000` bytes | `13,309,214,720` | PASS |

Printed with no threshold: 2026-10-04 22:05:55 UTC (`1791151555`); `nproc` `1`; `MemTotal` `978640 kB`, `SwapTotal`
`3174396 kB`, `SwapFree` `2850200 kB`; `systemd 255 (255.4-1ubuntu8.17)`; the journal of both units since
`@1791102470`, TZ-20's `I final`, holds **no entries**; `/root/PROJECT_GAMING_PS5` `487,901,585` bytes;
`telemetry-watch.service` `disabled` (exit 1) and `inactive` (exit 3); `/root/.claude` `206,456,743` bytes. **The
listing named 12 directories beside this session's own whose name is a UUID.** §2.3 sets out which ten of them §9
reclaimed and why two were kept.

### 0.3 Free space — every read, its instant, its reader and the bound (§0.3)

The bound is `2,300,000,000` bytes: the chain book's `RESOURCE_FLOOR` `2,200,000,000` plus `100,000,000` for this
session.

| instant (UTC) | reader | `/dev/vda2` free, bytes | against `2,300,000,000` |
|---|---|---|---|
| 2026-10-04 22:05:55 | §0.2's `df`, the Executor | 13,309,214,720 | above |
| 2026-10-04 22:22:07.735 | the new recorder's own `start` record, `free_bytes` (§2.9) | 13,285,228,544 | above |
| 2026-10-04 23:08:37 | §3.8's repeat of §0.2's `df`, the Executor | 13,274,189,824 | above |
| 2026-10-04 23:11:32 | B-RECLAIM-OWN's `df`, the Executor | 13,298,954,240 | above |

### 0.4 Refs (§0.4)

`git ls-remote origin` before the branch existed (`logs/02-refs.log`):

```text
$ git ls-remote origin
c3828d031109beaaef67a6189112317695259101	HEAD
c3828d031109beaaef67a6189112317695259101	refs/heads/main
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
ref lines: 25
$ git ls-remote origin refs/heads/tz-21-recorder-memory | wc -l
0
$ git branch --list tz-21-recorder-memory | wc -l
0
$ git show origin/main:SYSTEM-MAP.md | grep -c "Revision string:\*\* \`2026-10-04-b\`"
1
Sun Oct  4 10:06:09 PM UTC 2026
```

**25 ref lines**, as map §1 records. One difference, recorded and not blocking: `main` (and `HEAD`) is at
`c3828d031109beaaef67a6189112317695259101`, not `c7a45ff…`. It sits two commits above PR #21's merge: `e7d9954`
("Update SYSTEM-MAP.md", revision `2026-10-04-b`) and `c3828d0` (this TZ's upload). `main` carries revision
`2026-10-04-b` (the `grep -c` prints `1`), `main` is the only branch, and `refs/heads/tz-21-recorder-memory` did not
exist on `origin` or locally (both counts `0`). Neither BLOCKED condition holds.

---

## 1. Input

| input | how read | size, count, hash |
|---|---|---|
| `CryptoTZ/TZ-21-recorder-memory.md` | in full; §3.1's script extracted Appendix A from the branch worktree's copy | 2,862 lines, 151,912 bytes, `92d72640…` |
| `SYSTEM-MAP.md`, revision `2026-10-04-b` | in full | 1,117 lines, 230,008 bytes, `676631be…` |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | in full | 234 lines, 11,128 bytes, `437b45ea…` |
| `/var/lib/btc-recorder/runtime.jsonl` | whole, by `I state` (22:06:57), `I restart`, every `I rec` run and `I final` — one line in memory at a time | at `I state`: 62,344 records — `clock` 61,968, `disconnect` 370, `start` 6 — 0 torn, ending in a newline |
| the G-EQUIV snapshot of it | copied whole at 22:16:12 UTC into `scratch/`, then shown to be the live file's first bytes and removed by `I equiv` | 12,938,179 bytes, 62,362 records, SHA-256 `ef2b429c501c316521a32b8d4033cca20172e8b047a8928e1ae59bb0e7843ade`; re-derived by `head -c 12938179 /var/lib/btc-recorder/runtime.jsonl` |
| G-REC's intervals | `manifest.json` and `runtime.jsonl` of each compared interval, read only; the `manifest.json` of each interval opening in the 3,900 s before the restart stat'ed, not opened | 7 intervals compared: 2 earlier, `1791152100` and `1791152400`, and 5 members, `1791152700` to `1791153900`; 15 opens in the PASS run (§2.11). The seven NOT YET runs opened nothing |
| `recorder.log` | `tail -n 40`, §3.8 | statuses, counts and times (§2.14) |
| the primary checkout's `recorder.py`, `config.py`, `manifest.py` | imported by `synth`, `equiv` and `rec` as the old code, each hash asserted at load | `9fd1c7de…`, `8111dfe4…`, `79c99010…` |
| systemd, `/proc`, the two control groups | `systemctl show`, `/proc/<pid>/cmdline`, `cwd` and `cgroup`, `memory.*` | §2 |

**Nothing was re-collected.** The capture after the restart is the unit's own work, as before it. This TZ's own
requests were G-PATH's: two HTTP requests, two SNTP bursts and one RTDS subscription, closed by 22:19:12 UTC (§2.8).

---

## 2. Measurements

### 2.1 §3.1 — the branch and its two files (V4)

```text
$ git -C /root/btc-5m-twap fetch origin
exit=0
$ git -C /root/btc-5m-twap worktree add -b tz-21-recorder-memory /root/tz21-work/wt origin/main
Preparing worktree (new branch 'tz-21-recorder-memory')
branch 'tz-21-recorder-memory' set up to track 'origin/main'.
HEAD is now at c3828d0 Add files via upload
exit=0
c3828d031109beaaef67a6189112317695259101
```

§3.1's extraction script, verbatim, then `wc`, `sha256sum`, `git status` and `git diff --numstat`
(`logs/04-extract.log`):

```text
$ (the §3.1 extraction script, verbatim)
research/recorder/recorder.py 651 27821 0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7
research/tz21-recorder-memory.py 1284 59009 d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f
exit=0
$ wc -l -c; sha256sum
  651 27821 research/recorder/recorder.py
 1284 59009 research/tz21-recorder-memory.py
 1935 86830 total
0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7  research/recorder/recorder.py
d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f  research/tz21-recorder-memory.py
 M research/recorder/recorder.py
?? research/tz21-recorder-memory.py
49	6	research/recorder/recorder.py
```

| path | lines | bytes | SHA-256 | TZ's table |
|---|---|---|---|---|
| `research/recorder/recorder.py` | 651 | 27,821 | `0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7` | equal |
| `research/tz21-recorder-memory.py` | 1,284 | 59,009 | `d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f` | equal |

The script asserted the replaced file was `9fd1c7de…` before writing over it. The diff is `M`, **`49` insertions and
`6` deletions**, and `A`. The six deleted lines are the six of C3, read off `git diff`: lines 228, 233, 234, 240,
242 and 488 of `origin/main`'s `recorder.py`.

The commit and the push (`logs/05-commit-push.log`):

```text
commit exit=0
e3975b5 TZ-21: the recorder's memory, bounded - recorder.py and the instrument
c3828d0 Add files via upload
e3975b5da44c5328adf3bf3914634cd878842c73
root <root@vultr.guest>
TZ-21: the recorder's memory, bounded - recorder.py and the instrument

 research/recorder/recorder.py    |   55 +-
 research/tz21-recorder-memory.py | 1284 ++++++++++++++++++++++++++++++++++++++
 2 files changed, 1333 insertions(+), 6 deletions(-)
$ git push -u origin tz-21-recorder-memory
remote: 
remote: Create a pull request for 'tz-21-recorder-memory' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-21-recorder-memory        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-21-recorder-memory -> tz-21-recorder-memory
branch 'tz-21-recorder-memory' set up to track 'origin/tz-21-recorder-memory'.
push exit=0
e3975b5da44c5328adf3bf3914634cd878842c73
e3975b5da44c5328adf3bf3914634cd878842c73
0
```

The pull request (`logs/06-pr.log`):

```text
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/22
exit=0
22 https://github.com/seahomebatumi-ai/btc-5m-twap/pull/22 OPEN e3975b5da44c5328adf3bf3914634cd878842c73 main
```

### 2.2 §3.2 — `I state` (V3)

```text
$ I state
[2026-10-04T22:06:57Z] U btc-recorder.service {"ActiveState": "active", "ControlGroup": "/system.slice/btc-recorder.service", "ExecMainStartTimestamp": "Sun 2026-10-04 08:27:07 UTC", "FragmentPath": "/etc/systemd/system/btc-recorder.service", "MainPID": "4067771", "MemoryCurrent": "14016512", "MemoryMax": "536870912", "MemoryPeak": "200052736", "NRestarts": "1", "Result": "success", "SubState": "running", "UnitFileState": "enabled"}
[2026-10-04T22:06:57Z] G-UNIT btc-recorder.service: pid 4067771, argv equal, cgroup /system.slice/btc-recorder.service, NRestarts 1, MemoryMax 536870912
[2026-10-04T22:06:57Z] U btc-chainbook.service {"ActiveState": "active", "ControlGroup": "/system.slice/btc-chainbook.service", "ExecMainStartTimestamp": "Sun 2026-10-04 08:16:18 UTC", "FragmentPath": "/etc/systemd/system/btc-chainbook.service", "MainPID": "4064090", "MemoryCurrent": "663552", "MemoryMax": "201326592", "MemoryPeak": "18735104", "NRestarts": "1", "Result": "success", "SubState": "running", "UnitFileState": "enabled"}
[2026-10-04T22:06:57Z] G-UNIT btc-chainbook.service: pid 4064090, argv equal, cgroup /system.slice/btc-chainbook.service, NRestarts 1, MemoryMax 201326592
[2026-10-04T22:06:57Z] sole instance: recorder 4067771
[2026-10-04T22:06:57Z] sole instance: chain book 4064090
[2026-10-04T22:06:57Z] S1 S2 both units active: recorder pid 4067771 NRestarts 1, chain book pid 4064090 NRestarts 1
[2026-10-04T22:06:57Z] S3 /var/lib/btc-recorder/runtime.jsonl: 62344 newlines, 62344 records {"clock": 61968, "disconnect": 370, "start": 6}, 0 torn, ends with a newline True
[2026-10-04T22:06:57Z] S3 newest start {"captured_bytes": 567966600, "free_bytes": 13375229952, "kind": "start", "recv_ns": 1791102427832661053, "sha": "4216c04673ced76b5b2ac60ef57c9abedc46f9b9"}
[2026-10-04T22:06:57Z] S4 the unit's tree: /root/btc-recorder-svc/research/recorder, 3 of 3 files equal
[2026-10-04T22:06:57Z] S5 the primary checkout: /root/btc-5m-twap/research/recorder, 3 of 3 files equal
[2026-10-04T22:06:57Z] S6 the branch: /root/tz21-work/wt/research/recorder, 3 of 3 files equal
[2026-10-04T22:06:57Z] S7 /root/tz04a-env/venv/bin/python executable
[2026-10-04T22:06:57Z] S7 /root/tz01-env/venv/bin/python executable
[2026-10-04T22:06:57Z] M btc-recorder.service {"memory.current": "14016512", "memory.max": "536870912", "memory.peak": "200052736", "memory.stat": {"anon": 11247616, "file": 1146880, "kernel": 1118208, "kernel_stack": 81920, "pagetables": 299008, "shmem": 0, "slab_reclaimable": 612176, "slab_unreclaimable": 114688, "sock": 0}, "memory.swap.current": "87597056", "memory.swap.max": "max", "memory.swap.peak": "87597056"}
[2026-10-04T22:06:57Z] M btc-chainbook.service {"memory.current": "663552", "memory.max": "201326592", "memory.peak": "18735104", "memory.stat": {"anon": 221184, "file": 24576, "kernel": 417792, "kernel_stack": 0, "pagetables": 143360, "shmem": 0, "slab_reclaimable": 220952, "slab_unreclaimable": 43808, "sock": 0}, "memory.swap.current": "17686528", "memory.swap.max": "max", "memory.swap.peak": "17686528"}
[2026-10-04T22:06:57Z] H /proc/meminfo {"MemAvailable": 370880512, "MemTotal": 1002127360, "SwapFree": 2898489344, "SwapTotal": 3250581504}
[2026-10-04T22:06:57Z] STATE PASS: S1 to S7, the branch at e3975b5da44c5328adf3bf3914634cd878842c73
[2026-10-04T22:06:57Z] peak memory of this run: 20443136 bytes
[2026-10-04T22:06:57Z] opens under the capture roots: 1
exit=0
```

**STATE PASS, S1 to S7.** `state.json` was written at `1791151617605002534` (22:06:57.605 UTC). The old process's
footprint after 13 h 40 min of running: the control group's `memory.current` `14,016,512` bytes and
`memory.swap.current` `87,597,056` — **`101,613,568` bytes in all, six in seven of them in swap** — `anon`
`11,247,616`, `memory.peak` `200,052,736`.

### 2.3 §9 B-RECLAIM-SCRATCH — after §3.2, before §3.3

**Which directories.** §0.2's listing named 12 UUID directories beside this session's own, `f1dda509…`. Before
naming any to `reclaim`, the Executor read each one's birth time, size and file count, and the start times of the
`claude` processes working in `/root/btc-5m-twap` (`logs/08-scratch-listing.log`):

```text
Sun Oct  4 10:07:54 PM UTC 2026
$ ps -o pid,lstart,cmd (the btc-5m-twap claude processes)
    PID                  STARTED CMD
4127938 Sun Oct  4 19:04:43 2026 claude remote-control --name BTC-5M-TWAP-VPS --spawn=same-dir
4144046 Sun Oct  4 22:04:28 2026 /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe --print --sdk-url https://api.anthropic.com/v1/code/sessions/cse
$ stat birth/modify of every UUID directory
11598617-425a-5b99-80eb-4a598104a560 birth 2026-10-04 07:28:24.286806224 +0000 files 0 bytes 0
386a2f9a-9175-46e4-af0d-52cc5355a34c birth 2026-10-04 19:04:47.119573279 +0000 files 0 bytes 0
53daae24-51d9-5cf9-898f-16e726729ed2 birth 2026-10-04 07:30:09.259140739 +0000 files 61 bytes 240717
563ca246-a14d-524d-9f7b-7fbc748ed7c6 birth 2026-10-03 22:32:26.840556239 +0000 files 1 bytes 10
6e88615c-345d-5a08-be99-6375cc1a1073 birth 2026-10-03 22:28:16.836377323 +0000 files 0 bytes 0
7d1570e9-8d72-42b9-9919-348b3b338d30 birth 2026-10-04 07:28:22.564801545 +0000 files 0 bytes 0
8ec90b6c-b641-47ff-bee9-df7131656d41 birth 2026-10-03 22:28:15.166362629 +0000 files 0 bytes 0
9b05d639-af52-44b6-9a8c-9f508f7b17c4 birth 2026-10-04 22:04:29.100051200 +0000 files 0 bytes 0
9be611ff-a833-4160-a076-c4e5a9ca4cc0 birth 2026-10-03 11:27:25.205622050 +0000 files 0 bytes 0
a1c28db0-d13b-5013-a8c5-f8af6a1415be birth 2026-10-03 11:27:26.840640183 +0000 files 0 bytes 0
afca1dc1-0c42-49f8-af8c-b49f3c635ea6 birth 2026-10-04 07:30:07.596134735 +0000 files 0 bytes 0
cca925dd-1c79-41bd-87c9-4c6662750d7e birth 2026-10-03 22:32:25.428544031 +0000 files 0 bytes 0
f1dda509-7343-505e-8afa-097e9a463ab6 birth 2026-10-04 22:04:30.925066921 +0000 files 1 bytes 0
$ session transcripts under /root/.claude/projects/-root-btc-5m-twap
11598617-425a-5b99-80eb-4a598104a560
11598617-425a-5b99-80eb-4a598104a560.jsonl
11ec7ccc-d849-4f27-85b1-e25ed3a1bbf1.jsonl
146ed999-05a3-5409-8c9c-d2d77471b101
146ed999-05a3-5409-8c9c-d2d77471b101.jsonl
178afdf5-4460-5178-8410-ce1fcf889986
178afdf5-4460-5178-8410-ce1fcf889986.jsonl
2e32cd59-7079-5975-819f-e569a4107443
2e32cd59-7079-5975-819f-e569a4107443.jsonl
2fb3094a-1f03-5192-98c0-7d0168c2601f
2fb3094a-1f03-5192-98c0-7d0168c2601f.jsonl
431f722b-09db-4be8-9947-8d9a53553e47
431f722b-09db-4be8-9947-8d9a53553e47.jsonl
4cf2f58c-5de4-552d-88a0-be9b146d8868
4cf2f58c-5de4-552d-88a0-be9b146d8868.jsonl
53daae24-51d9-5cf9-898f-16e726729ed2
53daae24-51d9-5cf9-898f-16e726729ed2.jsonl
563ca246-a14d-524d-9f7b-7fbc748ed7c6
563ca246-a14d-524d-9f7b-7fbc748ed7c6.jsonl
6125871b-eaf6-5515-8e6c-9c9a3c2dbca5
6125871b-eaf6-5515-8e6c-9c9a3c2dbca5.jsonl
6e88615c-345d-5a08-be99-6375cc1a1073.jsonl
6f2baa91-140d-4612-a644-d7c498adb014
6f2baa91-140d-4612-a644-d7c498adb014.jsonl
73804847-5d50-47b7-94ca-23cb950ed16f
73804847-5d50-47b7-94ca-23cb950ed16f.jsonl
740aaf1e-4393-5553-be6d-c6cebb7f67ff
740aaf1e-4393-5553-be6d-c6cebb7f67ff.jsonl
7a5dcc50-5f3f-568d-bae5-c58f50c51275
7a5dcc50-5f3f-568d-bae5-c58f50c51275.jsonl
7bfd9956-d493-5501-a538-6643c7e42ba6
7bfd9956-d493-5501-a538-6643c7e42ba6.jsonl
7efd60d7-65fb-5515-a5c6-01ecb64789f2
7efd60d7-65fb-5515-a5c6-01ecb64789f2.jsonl
83c18c5c-2d9f-57bf-8206-4605e73a8aa5
83c18c5c-2d9f-57bf-8206-4605e73a8aa5.jsonl
860b95fc-b35c-516f-ac3f-6d6ae6798bbb
860b95fc-b35c-516f-ac3f-6d6ae6798bbb.jsonl
8615304a-0ad0-5e44-888c-927dcd2d4691
8615304a-0ad0-5e44-888c-927dcd2d4691.jsonl
a1c28db0-d13b-5013-a8c5-f8af6a1415be.jsonl
a536c898-ae41-53bd-87db-68477345ed11
a536c898-ae41-53bd-87db-68477345ed11.jsonl
a9f2c34f-b48b-5f47-a0ca-c79a598cd6c4
a9f2c34f-b48b-5f47-a0ca-c79a598cd6c4.jsonl
b22fd26f-0dbd-5991-bd84-9c838a598c56
b22fd26f-0dbd-5991-bd84-9c838a598c56.jsonl
b279d902-0bd0-5b3e-b73f-7a0cfb877b6b
b279d902-0bd0-5b3e-b73f-7a0cfb877b6b.jsonl
c663ffaa-3609-47ee-a847-0ca8edeb7fe2
c663ffaa-3609-47ee-a847-0ca8edeb7fe2.jsonl
c81ea6c1-024a-443a-aa43-b5603d145537
c81ea6c1-024a-443a-aa43-b5603d145537.jsonl
c97bed2e-708a-5ca2-9d8e-7c4dcd929689
c97bed2e-708a-5ca2-9d8e-7c4dcd929689.jsonl
d1b628ac-6bc2-5c6d-8bda-8c1d7c393061
d1b628ac-6bc2-5c6d-8bda-8c1d7c393061.jsonl
dc6d0cce-32ef-5d31-a2f6-45f6f36cb949
dc6d0cce-32ef-5d31-a2f6-45f6f36cb949.jsonl
de05c721-44f2-531a-8e37-0db4b500e0b9
de05c721-44f2-531a-8e37-0db4b500e0b9.jsonl
df27e6dd-d3c9-4c5a-b520-f3c8c2afb1d7
df27e6dd-d3c9-4c5a-b520-f3c8c2afb1d7.jsonl
e19b4276-9247-51df-a7dc-6e7a7261479b
e19b4276-9247-51df-a7dc-6e7a7261479b.jsonl
e8be6ab7-835e-51e2-b8b1-689047e9a86b
e8be6ab7-835e-51e2-b8b1-689047e9a86b.jsonl
ecf0dae3-0071-519c-9e21-9ea7fa97ab88
ecf0dae3-0071-519c-9e21-9ea7fa97ab88.jsonl
ed726596-f101-4b4d-9ff2-ab5af1242a69
ed726596-f101-4b4d-9ff2-ab5af1242a69.jsonl
ee7620c8-4962-5289-9e68-5610a0d857fd
ee7620c8-4962-5289-9e68-5610a0d857fd.jsonl
f05da928-61ab-517b-9f84-29114c8eb751
f05da928-61ab-517b-9f84-29114c8eb751.jsonl
f1dda509-7343-505e-8afa-097e9a463ab6
f1dda509-7343-505e-8afa-097e9a463ab6.jsonl
f2c0fdab-a46d-5a3b-8c56-30df2436a062
f2c0fdab-a46d-5a3b-8c56-30df2436a062.jsonl
this session's scratchpad: /tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6/scratchpad
kept, live: 9b05d639-af52-44b6-9a8c-9f508f7b17c4 (born 22:04:29.1, 1.1 s after this session's pid 4144046 started; empty)
kept, live: 386a2f9a-9175-46e4-af0d-52cc5355a34c (born 19:04:47.1, 4 s after the remote-control bridge pid 4127938 started; empty; still running)
```

**Ten were earlier sessions' and were reclaimed. Two were kept, both empty, because a running process made each:**
`9b05d639…` was born at 22:04:29.100, 1.1 s after this session's own process (pid `4144046`) started at 22:04:28,
and 1.8 s before this session's scratchpad directory. `386a2f9a…` was born at 19:04:47.120, 4 s after the
`claude remote-control` bridge (pid `4127938`) started at 19:04:43. That bridge is still running, and it spawned
this session. Neither has a session transcript, and neither is an earlier session's scratch (§6 item 2).

`I reclaim` over the ten, in one run (`logs/09-reclaim-scratch.log`):

```text
$ I reclaim (10 directories)
[2026-10-04T22:08:02Z] reclaim: 1603 report tokens; forensic store holds 1438 files
[2026-10-04T22:08:02Z] R copied a41ffc522c17ade796ee6801e8590c3c0043e5f6eaf3860c3d7e93622fdc4960 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--00-fingerprint.log
[2026-10-04T22:08:02Z] R copied 55829ca2fbeed679cc6b2b3ef38990a6970052997f54a20a42bf198e83cf3cb7 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--01-host-gate.log
[2026-10-04T22:08:02Z] R copied 083986a1d786b81ea451df4941d6c2796e9576ac0906ea5d458859d150c5bc70 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--02-refs.log
[2026-10-04T22:08:02Z] R copied 19179b355f0182640c1efa6abdf0db972a03913231b90096a870a5cd20c109f9 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--03-branch.log
[2026-10-04T22:08:02Z] R copied a41ffc522c17ade796ee6801e8590c3c0043e5f6eaf3860c3d7e93622fdc4960 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--00-fingerprint.log
[2026-10-04T22:08:02Z] R copied 55829ca2fbeed679cc6b2b3ef38990a6970052997f54a20a42bf198e83cf3cb7 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--01-host-gate.log
[2026-10-04T22:08:02Z] R copied 083986a1d786b81ea451df4941d6c2796e9576ac0906ea5d458859d150c5bc70 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--02-refs.log
[2026-10-04T22:08:02Z] R copied 19179b355f0182640c1efa6abdf0db972a03913231b90096a870a5cd20c109f9 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--03-branch.log
[2026-10-04T22:08:02Z] R copied 63fdf501f3997f253037c09687902c6275bf8d2e96fe889b5e3fe465b8623ac1 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--04-extract.log
[2026-10-04T22:08:02Z] R copied 2adcea80aadf0d10ecc9bc551373e72626ebf55c4e0b914aac6ddeb926e4a124 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--05-push.log
[2026-10-04T22:08:02Z] R copied a0765adddc96aaeb9a9fdf7e98aa639c998c0ba2089017a4529e2a9b618c9420 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--06-pr.log
[2026-10-04T22:08:02Z] R copied 367ce892198487355fecded1155dbe421d65b00535210054035686c86fc5fa37 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--07-state.log
[2026-10-04T22:08:02Z] R copied 4313286b104138b5eee7df8671cf53715ee407cec1323970cee68ef574ea3c36 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--08-reclaim-old.log
[2026-10-04T22:08:02Z] R copied a0885a72f2060b4cf07be63361b8c239cc6c4d54aa4f474993d63ebfcd3e0a87 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--09-worktrees-old.log
[2026-10-04T22:08:02Z] R copied ef9f01a5d8cc64a64315ef57b76cff86db8cf4a1bbd6aebf3cead19d38ea0a42 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--10-rm-tz16a.log
[2026-10-04T22:08:02Z] R copied 4546fb75901c7e3a35b4e600ab6be9c021215f286b9ed9f4225967e9d96efe57 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--11-rm-tz19.log
[2026-10-04T22:08:02Z] R copied a95f8ee83eb03cc5a87f1121e6288d22e7ef2802360cc6096f9740dc71a85d88 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--12-reclaim-old-verify.log
[2026-10-04T22:08:02Z] R copied e006943d2f22c49e604e238cb3a655510973fed39fb46f61f2ae2c5b95531674 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--13-recorder-tree.log
[2026-10-04T22:08:02Z] R copied 70c824f000be67a747bc4dc9d4b55d6deb49fd5f5b781f39ff410a00f16f54a9 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--14-path-recorder.log
[2026-10-04T22:08:02Z] R copied 470838a4046faea0df70935414d2b7de1f87fa98b7bfeaaef15e8ab990a1075b /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--15-path-chainbook.log
[2026-10-04T22:08:02Z] R copied 289d254be509d321e457ae5d01f74b7274dab212a596df7f8ac8181a90bddde9 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--16-install.log
[2026-10-04T22:08:02Z] R copied 94d4842d367bb95a41f1caeae5b90b2c3b2ea223decf80a4770f5bbb5b31b814 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--17-mark-start-rec.log
[2026-10-04T22:08:02Z] R copied 94fa4638e039dcd220325afb626c52d8ec95f75ad3500be8d9d805a58a70938e /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--18-mark-start-cb.log
[2026-10-04T22:08:02Z] R copied 606f1461b6ac6739b93bf8472270a4809cf6117b26a8754b465513dfd7a28df0 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--19-classifier-refusal-start.log
[2026-10-04T22:08:02Z] R copied af6d44d0ad7be039ccf6ab77419eec0a4fb6358924bb5f018d765e0f3d24d25d /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--20-boss-start-blocks.log
[2026-10-04T22:08:02Z] R copied 219ea94c5cec1474658340a900dc81a906b8a9b3ee3f4254d12bb4455ec1565f /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--21-start-verify.log
[2026-10-04T22:08:02Z] R copied 7641b2a8d21421b593248f8aefeae244bb2c2f29d8e40e39f0d295da5e8d0796 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--22-unit-0.log
[2026-10-04T22:08:02Z] R copied aeb262465b261303953fccd96637e1f18b88996e0fec8f77876f5e8afad5993f /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--23-start.log
[2026-10-04T22:08:02Z] R copied c08e4b530f66e3a16d63bc5b3e8a75a9c78715605b2eafb81c90256c9283efc1 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--24-cb-01.log
[2026-10-04T22:08:02Z] R copied 6df0b77c1a58e6cc77d09390a21ea1e4c07b76f8f3141218ece3148671e10682 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--25-rec-01.log
[2026-10-04T22:08:02Z] R copied db828de225a0aa5af2643702fb2a46940ad4f5472ade65e88cac060843beff37 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--26-cb-02.log
[2026-10-04T22:08:02Z] R copied c611b64c7788bf80247ba955e8ec2f014063bdd6cbb66f564389460d23986a53 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--27-rec-02.log
[2026-10-04T22:08:02Z] R copied be0374083cd8c7b65861b7e107b1c99277a046d1f36c04709e31be4b8cddc35e /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--28-cb-03.log
[2026-10-04T22:08:02Z] R copied e0839d65c1e942c2e4b7eb8a90638778ffc71f174835058e9ec1b8234c526520 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--29-rec-03.log
[2026-10-04T22:08:02Z] R copied 0e1b75409b24b93f74fed358488a7967d1521a3ffb479a481864ac304bfabed3 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--30-cb-04.log
[2026-10-04T22:08:02Z] R copied 6115741c9fc97620e828acef0952ee1f3a8151867b34872f8ae782390522d107 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--31-rec-04.log
[2026-10-04T22:08:02Z] R copied fc8fd013093200e576d20a3c15c2d2809fd0c38295b2e6d1a2b3168f64d6d912 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--32-cb-05.log
[2026-10-04T22:08:02Z] R copied 1cc31cbd2f9826e556c57fab767fb4e8213474d9750fa8a0e380530cbcee333a /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--33-rec-05.log
[2026-10-04T22:08:02Z] R copied a272a824ba885f910921a16b2e3e29c059c8cd699cb0b64b730490f0b29de47b /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--34-mark-kill-cb.log
[2026-10-04T22:08:02Z] R copied 5cf6b6dd6517e8d87f8df870d7ebc3e605804e5732ee6c34331f83c828e2c93b /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--35-kill-cb.log
[2026-10-04T22:08:02Z] R copied e05fd074eacf4bfdc002d232fdc05e3adc03cbb3047c05180864deb7184dd403 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--36-restart-cb.log
[2026-10-04T22:08:02Z] R copied 2f1f6016f2be6066e0ead18479599de10e01d45077b461f058e1e22f25680fe7 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--37-rec-06.log
[2026-10-04T22:08:02Z] R copied 32346f355dee0c696d7e6c8442bde9a2ebedc69fdc9f1c05f77ae6dee46f8e23 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--38-mark-kill-rec.log
[2026-10-04T22:08:02Z] R copied f167e3dacc00c27c563b5a7c9b466405efe7ae993b425775e1f0cad3b1b4a728 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--39-kill-rec.log
[2026-10-04T22:08:02Z] R copied 424a0eb542a45bba645e60bb48f14a3fcae4ab04e4486f4703301b371bee96fd /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--40-restart-rec.log
[2026-10-04T22:08:02Z] R copied 3f9db04080ac7f7887919ac17c2dc24037a7a5016b42197b6d5653cab8eba268 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--41-final.log
[2026-10-04T22:08:02Z] R copied 2347563bcbe5ed858e195eea5ca44b0067ae0027c53d6cc64360a9cd88fa1fdd /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--42-closing-host-block.log
[2026-10-04T22:08:02Z] R copied 9c04c5f5dfe30118e659df93be0a2dc9ca9757583b27384528fbb7a5dba83459 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--43-closing-reads.log
[2026-10-04T22:08:02Z] R copied 078f44bb648740bad33f129a2c2150f2d5a9329231afd82028f62683f2ad3831 /root/btc-forensics/53daae24-51d9-5cf9-898f-16e726729ed2--scratchpad--logs-cache--44-separation-check.log
[2026-10-04T22:08:02Z] RECLAIM PASS: 62 files considered, 49 named by a report, 0 kept by name, 49 copied, 0 already held; forensic store 1438 -> 1487 files
[2026-10-04T22:08:02Z] peak memory of this run: 21884928 bytes
[2026-10-04T22:08:02Z] opens under the capture roots: 0
exit=0
```

**RECLAIM PASS** before any removal: 62 files considered, 49 named by a report, 49 copied, 0 held; the store
1,438 → 1,487. All 49 came from `53daae24…`, TZ-20's session: its logs, which the TZ-20 report prints by hash.

Then one `rm -rf` and one `test -e` per directory (`logs/10-rm-scratch.log`):

```text
2026-10-04T22:08:18Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/11598617-425a-5b99-80eb-4a598104a560
exit=0
test -e exit=1
2026-10-04T22:08:18Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/53daae24-51d9-5cf9-898f-16e726729ed2
exit=0
test -e exit=1
2026-10-04T22:08:41Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/6e88615c-345d-5a08-be99-6375cc1a1073
exit=0
test -e exit=1
2026-10-04T22:08:41Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/7d1570e9-8d72-42b9-9919-348b3b338d30
exit=0
test -e exit=1
2026-10-04T22:15:12Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/a1c28db0-d13b-5013-a8c5-f8af6a1415be
exit=0
test -e exit=1
2026-10-04T22:15:13Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/afca1dc1-0c42-49f8-af8c-b49f3c635ea6
exit=0
test -e exit=1
2026-10-04T22:15:13Z
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/cca925dd-1c79-41bd-87c9-4c6662750d7e
exit=0
test -e exit=1

2026-10-04T22:15:44Z classifier REFUSED (reason [Interfere With Workloads]) at 22:08:18-22:08:40Z, not run, handed to the Boss:
  rm -rf /tmp/claude-0/-root-btc-5m-twap/563ca246-a14d-524d-9f7b-7fbc748ed7c6; echo "exit=$?"
  rm -rf /tmp/claude-0/-root-btc-5m-twap/8ec90b6c-b641-47ff-bee9-df7131656d41; echo "exit=$?"
  rm -rf /tmp/claude-0/-root-btc-5m-twap/9be611ff-a833-4160-a076-c4e5a9ca4cc0; echo "exit=$?"
$ ls -la (after)
total 32
drwx------  8 root root 4096 Oct  4 22:15 .
drwx------ 12 root root 4096 Oct  4 22:04 ..
drwx------  3 root root 4096 Oct  4 19:04 386a2f9a-9175-46e4-af0d-52cc5355a34c
drwx------  4 root root 4096 Oct  3 22:32 563ca246-a14d-524d-9f7b-7fbc748ed7c6
drwx------  3 root root 4096 Oct  3 22:28 8ec90b6c-b641-47ff-bee9-df7131656d41
drwx------  3 root root 4096 Oct  4 22:04 9b05d639-af52-44b6-9a8c-9f508f7b17c4
drwx------  3 root root 4096 Oct  3 11:27 9be611ff-a833-4160-a076-c4e5a9ca4cc0
drwx------  4 root root 4096 Oct  4 22:04 f1dda509-7343-505e-8afa-097e9a463ab6
2026-10-04T22:15:52Z correction to the line above: the three refusals came at 22:08:18Z (563ca246), 22:08:41Z (8ec90b6c) and 22:15:12Z (9be611ff)
2026-10-04T22:23:54Z handed to the Boss (B-RECLAIM-SCRATCH, refused part), one tree per command:
  rm -rf /tmp/claude-0/-root-btc-5m-twap/563ca246-a14d-524d-9f7b-7fbc748ed7c6; echo "exit=$?"
  rm -rf /tmp/claude-0/-root-btc-5m-twap/8ec90b6c-b641-47ff-bee9-df7131656d41; echo "exit=$?"
  rm -rf /tmp/claude-0/-root-btc-5m-twap/9be611ff-a833-4160-a076-c4e5a9ca4cc0; echo "exit=$?"
```

**Seven removed by the Executor**, each `exit=0` then `test -e` `exit=1`. **Three were refused by the session's
classifier** ("[Interfere With Workloads]"): `563ca246…` at 22:08:18, `8ec90b6c…` at 22:08:41 and `9be611ff…` at
22:15:12 UTC. By §3's route they were handed to the Boss verbatim, one tree per command.
The run continued meanwhile, because nothing from §3.3 on depends on them (§6 item 3). **The Boss ran the three
verbatim in a root shell on the VPS**, after B-RECLAIM-OWN. The Boss's shell printed, verbatim:

```text
root@vultr:~# rm -rf /tmp/claude-0/-root-btc-5m-twap/563ca246-a14d-524d-9f7b-7fbc748ed7c6; echo "exit=$?"
rm -rf /tmp/claude-0/-root-btc-5m-twap/8ec90b6c-b641-47ff-bee9-df7131656d41; echo "exit=$?"
rm -rf /tmp/claude-0/-root-btc-5m-twap/9be611ff-a833-4160-a076-c4e5a9ca4cc0; echo "exit=$?"
exit=0
exit=0
exit=0
```

The paste carries no instant. The parent directory's modification time, 2026-10-05 00:46:23.215 UTC, dates the
last removal. **The Executor's verification**, from the session at 00:46:52 UTC on 2026-10-05, after the work tree
was gone, so it is quoted here and not logged:

```text
2026-10-05T00:46:52Z
test -e 563ca246-a14d-524d-9f7b-7fbc748ed7c6 exit=1
test -e 8ec90b6c-b641-47ff-bee9-df7131656d41 exit=1
test -e 9be611ff-a833-4160-a076-c4e5a9ca4cc0 exit=1
total 20
drwx------  5 root root 4096 Oct  5 00:46 .
drwx------ 12 root root 4096 Oct  4 22:04 ..
drwx------  3 root root 4096 Oct  4 19:04 386a2f9a-9175-46e4-af0d-52cc5355a34c
drwx------  3 root root 4096 Oct  4 22:04 9b05d639-af52-44b6-9a8c-9f508f7b17c4
drwx------  4 root root 4096 Oct  4 22:04 f1dda509-7343-505e-8afa-097e9a463ab6
```

**All ten earlier sessions' directories are gone**: seven removed by the Executor and three by the Boss. What
remains beside this session's own are the two kept above.

### 2.4 §3.3 — the recorder's self-test (V5)

Run in the branch worktree against the new `recorder.py`, with `TMPDIR` in `scratch/` (`logs/11-selftest.log`):

```text
$ cd /root/tz21-work/wt/research/recorder && TMPDIR=/root/tz21-work/scratch nice -n 19 /root/tz04a-env/venv/bin/python -B selftest.py
2026-10-04T22:15:52Z
test_window_geometry
  ok  window membership over [-120, +420] matches the definition
  ok  a frame lands in at most two intervals
  ok  the open minus 90 s is inside the window
  ok  the open minus 91 s is outside it
  ok  the open plus 330 s is inside the window
  ok  the open plus 331 s is outside it
  ok  no second inside any window is unrouted
test_line_format
  ok  the line carries exactly three keys
  ok  the frame text survives byte-for-byte
  ok  the full-accuracy string is not turned into a float
  ok  full_accuracy_value stays a string after reparse
test_gzip_determinism
  ok  gzip output is byte-identical across runs
test_manifest_determinism
  ok  a rebuilt manifest is byte-identical
  ok  the manifest counts every message
  ok  the longest inter-message gap is measured, not assumed
  ok  raw and stored bytes are both recorded
  ok  the recorder sha is read back from the directory
test_complete_definition
  ok  a clean interval is complete
  ok  a disconnect inside the window makes the interval incomplete
  ok  a missing S6 makes the interval incomplete
  ok  a missing S7 makes the interval incomplete
test_resolved_outcome
  ok  live quotes on an open market are not a result
  ok  fractional prices on a closed market are not a result
  ok  a settled Up market reads as Up
  ok  a settled Down market reads as Down
  ok  two winners is not a result
  ok  a closed market with no prices is not a result
test_published_precision
  ok  the S1 report at T0 is not Decimal-equal to the published double
  ok  it is equal at the precision the venue publishes
  ok  the report one second earlier is not equal at any precision
  ok  the residual is below one double ulp at this magnitude
test_clock_filter
  ok  the lowest round trip is kept
test_restart_edges
  ok  the last frame on disk is found
  ok  an empty capture root gives 0
  ok  a torn line is counted, not fatal
test_floors_are_the_tz_values
  ok  the free-space floor is exactly 2_000_000_000 bytes
  ok  the self-cap is exactly 4_000_000_000 bytes
  ok  the clock limit is exactly 50 ms
  ok  the window is [T0-90, T0+330]
  ok  crypto_prices_twap_sixty uses the exact compact filter form
  ok  crypto_prices_twap_thirty uses the exact compact filter form
  ok  crypto_prices_chainlink uses the exact compact filter form
  ok  crypto_prices uses the exact compact filter form
test_scoring_set
  ok  the 10:21:09 start gives the 10:25 interval first
  ok  the logged 10:21:10.18 start gives the same interval
  ok  a window opening at the start instant does not lie after it
  ok  a window opening just after the start does
  ok  the set fills from non-consecutive members
  ok  members are indexed in order
  ok  each non-member carries its reason
  ok  the walk stops at the last member
  ok  a short capture is reported as not full, through its last interval
  ok  a manifest whose verdict contradicts its fields aborts the run
  ok  199 of 200 clears the gate
  ok  198 of 200 does not
  ok  no intervals clears nothing
test_rules_at_live_scale
  ok  R1 reads the first S1 report at or after T0 + 300
  ok  R1 is Down when that report is below the price to beat
  ok  R2 averages only reports inside [T0, T0 + 300] and reads Up
  ok  R3 compares the reading in force at T0 + 300 with the one at T0
  ok  both S3 candidates take the report stamped exactly T0
  ok  a stream with no report yields no candidate
  ok  no S1 report after the close leaves R1 undecided, not guessed
test_tier_c_checkpoints
  ok  the seven checkpoints are the TZ's tau values
  ok  tau maps to the t values the TZ prints
  ok  every checkpoint is inside the interval
  ok  the last checkpoint is inside the window the recorder keeps open
  ok  there are fourteen reads per interval
  ok  no read may outlive the gap to the next checkpoint
  ok  a process running from the window's open reads all seven
  ok  a process starting at T0 + 211 reads only the three still ahead
  ok  a checkpoint is read at its own instant, not skipped there
  ok  a process starting after the last checkpoint reads nothing
test_tier_c_line_and_manifest
  ok  a clean interval has quotes_complete
  ok  every read is carried in quote_offsets_ms
  ok  the offset is signed and measured against the intended instant
  ok  each offset carries the checkpoint it belongs to
  ok  a single non-200 read makes quotes_complete false
  ok  a single non-200 read leaves complete untouched
  ok  a body that is not JSON makes quotes_complete false
  ok  a body that is not JSON leaves complete untouched
  ok  fewer than fourteen reads makes quotes_complete false
  ok  fewer than fourteen reads leaves complete untouched
  ok  no Tier C file at all makes quotes_complete false
  ok  no Tier C file at all leaves complete untouched
  ok  an interval with no Tier C file has no offsets
test_tier_c_manifest_determinism
  ok  a manifest carrying Tier C rebuilds byte-identically
test_sntp_reply_validation
  ok  the skew limit is exactly 86_400 seconds
  ok  a well-formed reply is accepted
  ok  leap indicator 3 is rejected
  ok  stratum 0 is rejected
  ok  stratum 16 is rejected
  ok  stratum 15 is still accepted
  ok  a zero transmit timestamp is rejected
  ok  a transmit timestamp 86_401 s adrift is rejected
  ok  a transmit timestamp 86_399 s adrift is not
  ok  that reply would have carried an offset near -3.998e12 ms
  ok  it is rejected before it can become one
test_sntp_rejections_are_counted
  ok  the one accepted reply is the offset
  ok  the other three are counted by reason
  ok  a burst rejected outright yields no offset at all
  ok  and its rejections are still reported
  ok  a sample with no offset is carried, not dropped
  ok  it does not become the largest offset
test_span_is_bounded_not_denied
  ok  with no later start the span is unbounded
  ok  a restart after ours no longer aborts the analysis
  ok  the span ends at the first start after ours
  ok  a third start does not move the bound, whatever the file order
  ok  two starts on the analysed commit still abort the run
  ok  the last TZ-04b member closes long before the TZ-05a restart
  ok  a window closing exactly at the next start is inside the span
  ok  a window closing one nanosecond after it is not
  ok  an interval opening after the next start is not in the span
  ok  an unbounded span contains every interval
test_no_interpolation_anywhere
  ok  no gap-filling primitive appears in any recorder file

115 of 115 checks passed
exit=0
2026-10-04T22:15:52Z
total 8
drwxr-xr-x 2 root root 4096 Oct  4 22:15 .
drwxr-xr-x 5 root root 4096 Oct  4 22:06 ..
0
```

**`115 of 115 checks passed`.** `scratch/` held no file of the test's afterwards, and `git status --porcelain --ignored`
in the worktree printed nothing (`0` lines): no `__pycache__`.

### 2.5 §3.3 — G-SYNTH (V6)

```text
$ I synth
[2026-10-04T22:15:56Z] H /proc/meminfo {"MemAvailable": 265342976, "MemTotal": 1002127360, "SwapFree": 2850353152, "SwapTotal": 3250581504}
[2026-10-04T22:15:56Z] load recorder_old: /root/btc-5m-twap/research/recorder, 3 of 3 files equal
[2026-10-04T22:15:56Z] load recorder_new: /root/tz21-work/wt/research/recorder, 3 of 3 files equal
[2026-10-04T22:16:00Z] G-SYNTH steady: 562 closes, 562 fast and 56 slow slices equal; held at most 242 records, the old recorder 14461
[2026-10-04T22:16:01Z] G-SYNTH outage: 3 recovered and 23 live closes, 23 fast and 14 slow slices equal; held at most 242 records
[2026-10-04T22:16:02Z] G-SYNTH torn tail: 11 closes, 13 fast and 7 slow slices equal
[2026-10-04T22:16:04Z] G-SYNTH ten days: 2866 closes, 238 slices equal; the new recorder held at most 241 records, the old 28673 at the end
[2026-10-04T22:16:04Z] G-SYNTH negative controls: a clock missing from memory on the fast path and from the file on the slow path are each detected, 2 of 2 (14 lines removed)
[2026-10-04T22:16:04Z] G-SYNTH PASS: 913 slices equal, 836 fast and 77 slow; the new recorder held at most 242 records, the old 28673
[2026-10-04T22:16:04Z] peak memory of this run: 58191872 bytes
[2026-10-04T22:16:04Z] opens under the capture roots: 0
exit=0
wall 8.278173547 s
```

**G-SYNTH PASS.** 913 slices byte-identical, **836 from memory against `600`, 77 from disk against `60`**; the new
recorder held **at most 242 records against `2,000`**, the old copy 28,673; both negative controls detected, 2 of
2. These are the counts the Architect's run printed, `913`, `836`, `77`, `242` and `28,673`. The run's peak was
`58,191,872` bytes, and `MemAvailable` at its start `265,342,976`.

### 2.6 §3.3 — G-EQUIV (V7)

```text
$ I equiv
[2026-10-04T22:16:12Z] H /proc/meminfo {"MemAvailable": 274857984, "MemTotal": 1002127360, "SwapFree": 2840391680, "SwapTotal": 3250581504}
[2026-10-04T22:16:12Z] load recorder_old: /root/btc-5m-twap/research/recorder, 3 of 3 files equal
[2026-10-04T22:16:12Z] load recorder_new: /root/tz21-work/wt/research/recorder, 3 of 3 files equal
[2026-10-04T22:16:12Z] G-EQUIV snapshot of /var/lib/btc-recorder/runtime.jsonl at 2026-10-04T22:16:12Z: 12938179 bytes, sha256 ef2b429c501c316521a32b8d4033cca20172e8b047a8928e1ae59bb0e7843ade
[2026-10-04T22:16:14Z] G-EQUIV loaded: the old load holds 62362 records (0 torn lines skipped), count and digest equal to the parse; the old slices read the 10065 of them the chosen windows can select; the new recorder holds 233, from 2026-10-04T20:16:12Z on
[2026-10-04T22:16:16Z] G-EQUIV projected 157 s for 825 windows, 802 of them slow, after 1.9 s
[2026-10-04T22:18:45Z] G-EQUIV windows: 825 of the span's 7060, 2026-09-10T09:55:00Z to 2026-10-04T22:10:00Z, in 151.7 s
[2026-10-04T22:18:45Z] G-EQUIV the snapshot is the first 12938179 bytes of /var/lib/btc-recorder/runtime.jsonl, sha256 ef2b429c501c316521a32b8d4033cca20172e8b047a8928e1ae59bb0e7843ade; the copy is removed
[2026-10-04T22:18:45Z] G-EQUIV PASS: 825 windows equal, 23 fast and 802 slow; the new recorder holds 233 records against the old 62362
[2026-10-04T22:18:45Z] peak memory of this run: 43905024 bytes
[2026-10-04T22:18:45Z] opens under the capture roots: 2
exit=0
wall 153.921962982 s
```

**G-EQUIV PASS.** 825 windows of the span's 7,060 byte-identical, **23 from memory against `12`, 802 from disk
against `200`**. The old code's own `load_runtime`, into the sink, held **62,362** records, and its count and digest
equal one parse of the snapshot's. The new recorder held **233 against `2,000`**, from 20:16:12 UTC on. The
snapshot is the first 12,938,179 bytes of the live file, SHA-256 `ef2b429c…`, and the copy is removed. The run
projected 157 s after its tenth window from disk, against the budget of `3,000` s, and took 151.7 s in its loop
and 153.9 s in all. Its peak was `43,905,024` bytes, and `MemAvailable` at its start `274,857,984`.

### 2.7 §3.4 — B-MOVE (V8)

Run by the Executor at 22:19:04 UTC (`logs/14-b-move.log`); the last three reads were added to the block to show
the branch head `state.json` holds and that the old process had not moved:

```text
2026-10-04T22:19:04.494748794Z
$ B-MOVE
Previous HEAD position was 4216c04 TZ-05a: Tier C quote snapshots, SNTP reply validation
HEAD is now at e3975b5 TZ-21: the recorder's memory, bounded - recorder.py and the instrument
exit=0
e3975b5da44c5328adf3bf3914634cd878842c73
0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7  /root/btc-recorder-svc/research/recorder/recorder.py
8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d  /root/btc-recorder-svc/research/recorder/config.py
79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045  /root/btc-recorder-svc/research/recorder/manifest.py
0
4626222	/root/btc-recorder-svc
state.json branch_head: e3975b5da44c5328adf3bf3914634cd878842c73
MainPID=4067771
NRestarts=1
2026-10-04T22:19:04.612920195Z
```

`HEAD` `e3975b5da44c5328adf3bf3914634cd878842c73`, equal to `state.json`'s `branch_head`; **3 of 3** hashes,
`0f6c9045…`, `8111dfe4…`, `79c99010…`; **`0`** status lines. The tree is 4,626,222 bytes, up from TZ-20's `608,103`.
The running process was still pid `4067771` with `NRestarts` `1`. K-21a was not needed.

### 2.8 §3.4 — G-PATH (V9)

```text
$ I path
[2026-10-04T22:19:10Z] load recorder: /root/btc-recorder-svc/research/recorder, 3 of 3 files equal
[2026-10-04T22:19:10Z] P0 recorder.py /root/btc-recorder-svc/research/recorder/recorder.py, git_sha e3975b5da44c5328adf3bf3914634cd878842c73, websockets 17.1, User-Agent 'btc-5m-twap-recorder/TZ-04a'
[2026-10-04T22:19:10Z] P1 https://gamma-api.polymarket.com/markets/slug/btc-updown-5m-1791152100: served, 5245 bytes, JSON, token ids ['56392956917463271513553839585116480246963503496455537801076184616791328350768', '13194502980536602135925581896979519650938080876251242542557884222132159080662']
[2026-10-04T22:19:10Z] P2 https://clob.polymarket.com/book?token_id=56392956917463271513553839585116480246963503496455537801076184616791328350768: status 200, 3059 bytes, JSON
[2026-10-04T22:19:11Z] P3 SNTP 108.61.73.243 (108.61.73.243): 4 accepted, offset 0.112 ms, rtt 96.564 ms, rejected {}
[2026-10-04T22:19:11Z] P3 SNTP pool.ntp.org (162.159.200.1): 4 accepted, offset 2.059 ms, rtt 0.485 ms, rejected {}
[2026-10-04T22:19:12Z] P4 wss://ws-live-data.polymarket.com: 6 frames in at most 30 s, topics ['crypto_prices', 'crypto_prices_chainlink', 'crypto_prices_twap_sixty', 'crypto_prices_twap_thirty']
[2026-10-04T22:19:12Z] G-PATH PASS: P0 to P4
[2026-10-04T22:19:12Z] peak memory of this run: 33898496 bytes
[2026-10-04T22:19:12Z] opens under the capture roots: 0
exit=0
```

**G-PATH PASS at the first run**, 22:19:10–22:19:12 UTC, so no second run was needed. P0: the recorder loaded from
`/root/btc-recorder-svc/research/recorder` with its three hashes asserted, `git_sha()` the branch head. P1: the market
document of interval `1791152100`, served, 5,245 bytes, JSON, two token ids. P2: the first token's book, status
`200`, 3,059 bytes, JSON. P3: SNTP **2 of 2** servers, 4 replies accepted from each. P4: 6 frames, **4 of 4** topics
by 22:19:12 UTC, inside the 30 s, `crypto_prices_twap_sixty` and `crypto_prices_chainlink` among them.

### 2.9 §3.5 — B-KILL-REC, then G-RESTART (V10)

B-KILL-REC, verbatim with `I` expanded, run by the Executor as one command from 22:19:25 UTC
(`logs/16-b-kill-rec.log`). **It was not refused:**

```text
$ B-KILL-REC
2026-10-04T22:19:25.248080287Z
[2026-10-04T22:21:52Z] MARK kill-rec {"cb_pid": 4064090, "cb_restarts": 1, "ns": 1791152512605133323, "rec_pid": 4067771, "rec_restarts": 1} (2026-10-04T22:21:52Z)
[2026-10-04T22:21:52Z] peak memory of this run: 20574208 bytes
[2026-10-04T22:21:52Z] opens under the capture roots: 0
1791152522.108717658
now%300=122
exit=0
```

The mark at `1791152512605133323` (22:21:52.605 UTC, `now % 300` = 112); the signal at `1791152522.108717658`
(22:22:02.109 UTC), `now % 300` = **122**, in interval `T0` = `1791152400`, after its `tau = 180` read at
`T0 + 120` and before the next window opens at `T0 + 210`.

`I restart`, 35 s after the signal (`logs/17-restart.log`):

```text
$ I restart
[2026-10-04T22:22:37Z] R {"captured_bytes": 582379618, "free_bytes": 13285228544, "kind": "start", "recv_ns": 1791152527734526971, "sha": "e3975b5da44c5328adf3bf3914634cd878842c73"}
[2026-10-04T22:22:37Z] R {"detected_recv_ns": 1791152528101425946, "end_recv_ns": 1791152528273575295, "kind": "disconnect", "reason": "startup", "start_recv_ns": 1791152521502178889}
[2026-10-04T22:22:37Z] U btc-recorder.service {"ActiveState": "active", "ControlGroup": "/system.slice/btc-recorder.service", "ExecMainStartTimestamp": "Sun 2026-10-04 22:22:07 UTC", "FragmentPath": "/etc/systemd/system/btc-recorder.service", "MainPID": "4148534", "MemoryCurrent": "20328448", "MemoryMax": "536870912", "MemoryPeak": "20590592", "NRestarts": "2", "Result": "success", "SubState": "running", "UnitFileState": "enabled"}
[2026-10-04T22:22:37Z] G-UNIT btc-recorder.service: pid 4148534, argv equal, cgroup /system.slice/btc-recorder.service, NRestarts 2, MemoryMax 536870912
[2026-10-04T22:22:37Z] G-RESTART: pid 4067771 replaced by 4148534, NRestarts 2; the start 2026-10-04T22:22:07Z on e3975b5da44c5328adf3bf3914634cd878842c73; the gap 2026-10-04T22:22:01Z to 2026-10-04T22:22:08Z, 6.771 s; 0 torn
[2026-10-04T22:22:37Z] sole instance: recorder 4148534
[2026-10-04T22:22:37Z] M btc-recorder.service {"memory.current": "20328448", "memory.max": "536870912", "memory.peak": "20590592", "memory.stat": {"anon": 19886080, "file": 131072, "kernel": 311296, "kernel_stack": 49152, "pagetables": 147456, "shmem": 0, "slab_reclaimable": 14288, "slab_unreclaimable": 89184, "sock": 0}, "memory.swap.current": "0", "memory.swap.max": "max", "memory.swap.peak": "0"}
[2026-10-04T22:22:37Z] G-RESTART the chain book, recorded and judged by G-CB-STILL: pid 4064090, NRestarts 1
[2026-10-04T22:22:37Z] G-RESTART PASS: the recorder runs the new code as pid 4148534
[2026-10-04T22:22:37Z] peak memory of this run: 20574208 bytes
[2026-10-04T22:22:37Z] opens under the capture roots: 1
exit=0
```

**G-RESTART PASS.** Since the mark: exactly one `start` record, its sha `e3975b5…`; exactly one `startup` gap; no
`halt`; pid `4067771` → **`4148534`**, the sole process with an argument ending in `recorder.py`; `NRestarts` 1 →
**2**; the unit checks at `MemoryMax` `536870912`. The chain book was pid `4064090`, `NRestarts` `1`.

### 2.10 The gap — the `startup` record G-RESTART read

| field | `recv_ns` | UTC |
|---|---|---|
| `start_recv_ns` — the old process's last frame | `1791152521502178889` | 22:22:01.502178889 |
| the signal (`date -u +%s.%N`) | `1791152522108717658` | 22:22:02.108717658 |
| the new `start` record | `1791152527734526971` | 22:22:07.734526971 |
| `detected_recv_ns` | `1791152528101425946` | 22:22:08.101425946 |
| `end_recv_ns` — the new process's first frame | `1791152528273575295` | 22:22:08.273575295 |

**The gap lasted 6.771 s** (`6,771,396,406` ns), against `60` s. Its start was 8.897 s after the mark, against a
bound of no earlier than 5 s before it, and 0.607 s before the signal. The new `start` record came 5.626 s after
the signal, the unit's `RestartSec=5` plus the interpreter's start. The order the gate asserts holds: gap start ≤
`start` ≤ detection ≤ end. The gap is recorded and not filled.

### 2.11 §3.6 — G-REC, every run (V11)

`I rec` ran 8 times, against the bound of 11. The first ran 30 s after `I restart`, at 22:23:07 UTC. A
background loop ran the next at the instant each NOT YET named, 300 s later, until the mode exited `0`
(`logs/18-rec-01.log` to `18-rec-08.log`). The seven NOT YET runs:

```text
==> logs/18-rec-01.log <==
$ I rec
[2026-10-04T22:23:07Z] NOT YET: intervals [1791152700, 1791153000, 1791153300, 1791153600, 1791153900] pending, the last deadline 2026-10-04T23:50:00Z; run this mode again at or after 2026-10-04T22:28:07Z
[2026-10-04T22:23:07Z] opens under the capture roots: 0
exit=3

==> logs/18-rec-02.log <==
$ I rec
[2026-10-04T22:28:08Z] NOT YET: intervals [1791152700, 1791153000, 1791153300, 1791153600, 1791153900] pending, the last deadline 2026-10-04T23:50:00Z; run this mode again at or after 2026-10-04T22:33:08Z
[2026-10-04T22:28:08Z] opens under the capture roots: 0
exit=3

==> logs/18-rec-03.log <==
$ I rec
[2026-10-04T22:33:09Z] NOT YET: intervals [1791152700, 1791153000, 1791153300, 1791153600, 1791153900] pending, the last deadline 2026-10-04T23:50:00Z; run this mode again at or after 2026-10-04T22:38:09Z
[2026-10-04T22:33:09Z] opens under the capture roots: 0
exit=3

==> logs/18-rec-04.log <==
$ I rec
[2026-10-04T22:38:09Z] NOT YET: intervals [1791153000, 1791153300, 1791153600, 1791153900] pending, the last deadline 2026-10-04T23:50:00Z; run this mode again at or after 2026-10-04T22:43:09Z
[2026-10-04T22:38:09Z] opens under the capture roots: 0
exit=3

==> logs/18-rec-05.log <==
$ I rec
[2026-10-04T22:43:09Z] NOT YET: intervals [1791153300, 1791153600, 1791153900] pending, the last deadline 2026-10-04T23:50:00Z; run this mode again at or after 2026-10-04T22:48:09Z
[2026-10-04T22:43:09Z] opens under the capture roots: 0
exit=3

==> logs/18-rec-06.log <==
$ I rec
[2026-10-04T22:48:10Z] NOT YET: intervals [1791153600, 1791153900] pending, the last deadline 2026-10-04T23:50:00Z; run this mode again at or after 2026-10-04T22:53:10Z
[2026-10-04T22:48:10Z] opens under the capture roots: 0
exit=3

==> logs/18-rec-07.log <==
$ I rec
[2026-10-04T22:53:11Z] NOT YET: intervals [1791153900] pending, the last deadline 2026-10-04T23:50:00Z; run this mode again at or after 2026-10-04T22:58:11Z
[2026-10-04T22:53:11Z] opens under the capture roots: 0
exit=3
```

The PASS run, at 22:58:12 UTC:

```text
$ I rec
[2026-10-04T22:58:12Z] load recorder_old: /root/btc-5m-twap/research/recorder, 3 of 3 files equal
[2026-10-04T22:58:12Z] G-REC earlier interval 1791152100 2026-10-04T22:15:00Z: closed by the new code, complete True, disconnects 0, sha 4216c04673ced76b5b2ac60ef57c9abedc46f9b9, slice equal to the old recorder's True
[2026-10-04T22:58:12Z] G-REC earlier interval 1791152400 2026-10-04T22:20:00Z: closed by the new code, complete False, disconnects 1, sha ['4216c04673ced76b5b2ac60ef57c9abedc46f9b9', 'e3975b5da44c5328adf3bf3914634cd878842c73'], slice equal to the old recorder's True
[2026-10-04T22:58:12Z] G-REC interval 1791152700 2026-10-04T22:25:00Z: complete True, quotes_complete True, disconnects 0, sha e3975b5da44c5328adf3bf3914634cd878842c73, slice equal to the old recorder's True
[2026-10-04T22:58:12Z] G-REC interval 1791153000 2026-10-04T22:30:00Z: complete True, quotes_complete True, disconnects 0, sha e3975b5da44c5328adf3bf3914634cd878842c73, slice equal to the old recorder's True
[2026-10-04T22:58:12Z] G-REC interval 1791153300 2026-10-04T22:35:00Z: complete True, quotes_complete True, disconnects 0, sha e3975b5da44c5328adf3bf3914634cd878842c73, slice equal to the old recorder's True
[2026-10-04T22:58:12Z] G-REC interval 1791153600 2026-10-04T22:40:00Z: complete True, quotes_complete True, disconnects 0, sha e3975b5da44c5328adf3bf3914634cd878842c73, slice equal to the old recorder's True
[2026-10-04T22:58:12Z] G-REC interval 1791153900 2026-10-04T22:45:00Z: complete True, quotes_complete True, disconnects 0, sha e3975b5da44c5328adf3bf3914634cd878842c73, slice equal to the old recorder's True
[2026-10-04T22:58:12Z] G-REC PASS: manifests 5 of 5, quotes_complete 5 of 5, sha 5 of 5, complete 5 of 5 (PASS at 3 or more), slices equal 7 of 7 compared (2 earlier, 5 members)
[2026-10-04T22:58:12Z] peak memory of this run: 29093888 bytes
[2026-10-04T22:58:12Z] opens under the capture roots: 15
exit=0
```

**G-REC PASS.** The new `start` record is at 22:22:07.735 UTC, so the first member is the first `T0 ≡ 0 (mod 300)`
with `T0 − 90` at least 60 s after it, `1791152700` (22:25:00). The five members, `1791152700` to `1791153900`:

| interval | `T0` UTC | manifest | `quotes_complete` | `recorder_git_sha` | `complete` | `disconnect_count` | slice equal |
|---|---|---|---|---|---|---|---|
| `1791152700` | 22:25:00 | present | true | `e3975b5…` | true | 0 | true |
| `1791153000` | 22:30:00 | present | true | `e3975b5…` | true | 0 | true |
| `1791153300` | 22:35:00 | present | true | `e3975b5…` | true | 0 | true |
| `1791153600` | 22:40:00 | present | true | `e3975b5…` | true | 0 | true |
| `1791153900` | 22:45:00 | present | true | `e3975b5…` | true | 0 | true |

**Manifests 5 of 5, `quotes_complete` 5 of 5, sha 5 of 5, `complete` 5 of 5 against the pass mark of 3.** The
deciding count is `complete`, 5 against 3, a margin of 2.000 intervals.

**The earlier intervals: 2.** Of every `T0` from `1791148500`, 3,900 s before the new start, up to the first
member, two had a `manifest.json` written at or after the new `start` record:

| interval | `T0` UTC | how the new process came to close it | `complete` | `disconnect_count` | `recorder_git_sha` | slice equal |
|---|---|---|---|---|---|---|
| `1791152100` | 22:15:00 | its window closed at 22:20:30 under the old process, which had written no manifest for it when signalled; the new process recovered it (`recorder.log`: `recovering interval 1791152100`) | true | 0 | `4216c04…` | true |
| `1791152400` | 22:20:00 | the window open across the restart | **false** | 1 | `['4216c04…', 'e3975b5…']` | true |

**Slices equal 7 of 7 compared**: every slice the new process wrote from its start up to the fifth member equals
byte for byte the old code's slice, computed by the primary checkout's `write_runtime_slice` over the records
`runtime.jsonl` held when each stored slice was written. Interval `1791152400` lost `complete` as §3.5 intends: one
interval, the one the signal fell inside. Its manifest names both processes' shas and counts one disconnect: the `startup` gap of §2.10 falls inside its window. The
PASS run opened 15 files under the capture root: `runtime.jsonl` once, and the `manifest.json` and `runtime.jsonl`
of each of the 7 compared intervals.

### 2.12 §3.7 — `I final`: G-FINAL and G-CB-STILL (V13, V14)

`I final` at 23:08:20 UTC, 608 s after G-REC's PASS (`logs/19-final.log`):

```text
$ I final
[2026-10-04T23:08:21Z] U btc-recorder.service {"ActiveState": "active", "ControlGroup": "/system.slice/btc-recorder.service", "ExecMainStartTimestamp": "Sun 2026-10-04 22:22:07 UTC", "FragmentPath": "/etc/systemd/system/btc-recorder.service", "MainPID": "4148534", "MemoryCurrent": "40812544", "MemoryMax": "536870912", "MemoryPeak": "52322304", "NRestarts": "2", "Result": "success", "SubState": "running", "UnitFileState": "enabled"}
[2026-10-04T23:08:21Z] G-UNIT btc-recorder.service: pid 4148534, argv equal, cgroup /system.slice/btc-recorder.service, NRestarts 2, MemoryMax 536870912
[2026-10-04T23:08:21Z] G-FINAL the unit's tree: /root/btc-recorder-svc/research/recorder, 3 of 3 files equal
[2026-10-04T23:08:22Z] G-FINAL /var/lib/btc-recorder/runtime.jsonl: 62466 newlines, 0 torn, newest start 2026-10-04T22:22:07Z on e3975b5da44c5328adf3bf3914634cd878842c73
[2026-10-04T23:08:22Z] sole instance: recorder 4148534
[2026-10-04T23:08:22Z] M btc-recorder.service {"memory.current": "40816640", "memory.max": "536870912", "memory.peak": "52322304", "memory.stat": {"anon": 11075584, "file": 28262400, "kernel": 1417216, "kernel_stack": 49152, "pagetables": 151552, "shmem": 0, "slab_reclaimable": 1115520, "slab_unreclaimable": 89184, "sock": 0}, "memory.swap.current": "11550720", "memory.swap.max": "max", "memory.swap.peak": "11554816"}
[2026-10-04T23:08:22Z] M btc-chainbook.service {"memory.current": "7516160", "memory.max": "201326592", "memory.peak": "18735104", "memory.stat": {"anon": 6860800, "file": 135168, "kernel": 450560, "kernel_stack": 0, "pagetables": 147456, "shmem": 0, "slab_reclaimable": 250568, "slab_unreclaimable": 43808, "sock": 0}, "memory.swap.current": "16703488", "memory.swap.max": "max", "memory.swap.peak": "17686528"}
[2026-10-04T23:08:22Z] H /proc/meminfo {"MemAvailable": 286302208, "MemTotal": 1002127360, "SwapFree": 2951176192, "SwapTotal": 3250581504}
[2026-10-04T23:08:22Z] G-FINAL PASS: recorder pid 4148534 on e3975b5da44c5328adf3bf3914634cd878842c73
[2026-10-04T23:08:22Z] U btc-chainbook.service {"ActiveState": "active", "ControlGroup": "/system.slice/btc-chainbook.service", "ExecMainStartTimestamp": "Sun 2026-10-04 08:16:18 UTC", "FragmentPath": "/etc/systemd/system/btc-chainbook.service", "MainPID": "4064090", "MemoryCurrent": "7516160", "MemoryMax": "201326592", "MemoryPeak": "18735104", "NRestarts": "1", "Result": "success", "SubState": "running", "UnitFileState": "enabled"}
[2026-10-04T23:08:22Z] G-UNIT btc-chainbook.service: pid 4064090, argv equal, cgroup /system.slice/btc-chainbook.service, NRestarts 1, MemoryMax 201326592
[2026-10-04T23:08:22Z] sole instance: chain book 4064090
[2026-10-04T23:08:22Z] G-CB-STILL PASS: the chain book ran as pid 4064090, NRestarts 1, from state to the end
[2026-10-04T23:08:22Z] peak memory of this run: 20578304 bytes
[2026-10-04T23:08:22Z] opens under the capture roots: 1
exit=0
```

**G-FINAL PASS.** The unit's checks at `MemoryMax` `536870912`; `NRestarts` **2** and MainPID **`4148534`**, those
G-RESTART read; the sole process with an argument ending in `recorder.py`; `/root/btc-recorder-svc` at the branch
head with its three files `0f6c9045…`, `8111dfe4…` and `79c99010…`; the newest `start` record G-RESTART's,
22:22:07 UTC on `e3975b5…`. `runtime.jsonl` held 62,466 lines, 0 torn.

**G-CB-STILL PASS.** The chain book kept pid **`4064090`** and `NRestarts` **1** from `I state` (22:06:57) to
`I final` (23:08:22), the sole process with an argument ending in `tz18a-chainbook-capture.py`, and passed the unit
checks at `MemoryMax` `201326592`. The `kill-rec` mark read it at the same pid and count.

### 2.13 Memory — each unit at `I state`, `I restart` and `I final`, and the host (V19)

Every figure below is the instrument's own `M` or `H` line in bytes, assembled by script from `logs/07-state.log`,
`logs/17-restart.log` and `logs/19-final.log`. **`I restart` reads the recorder's control group alone. It reads
neither the chain book's nor `/proc/meminfo`, so those cells print "not read"** (§6 item 4).

| unit | read | `I state`, 2026-10-04T22:06:57Z | `I restart`, 2026-10-04T22:22:37Z | `I final`, 2026-10-04T23:08:22Z |
|---|---|---|---|---|
| `btc-recorder.service` | `memory.current` | 14,016,512 | 20,328,448 | 40,816,640 |
| `btc-recorder.service` | `memory.peak` | 200,052,736 | 20,590,592 | 52,322,304 |
| `btc-recorder.service` | `memory.swap.current` | 87,597,056 | 0 | 11,550,720 |
| `btc-recorder.service` | `memory.swap.peak` | 87,597,056 | 0 | 11,554,816 |
| `btc-recorder.service` | `memory.stat` `anon` | 11,247,616 | 19,886,080 | 11,075,584 |
| `btc-recorder.service` | `memory.stat` `file` | 1,146,880 | 131,072 | 28,262,400 |
| `btc-recorder.service` | `memory.stat` `kernel` | 1,118,208 | 311,296 | 1,417,216 |
| `btc-recorder.service` | `memory.stat` `kernel_stack` | 81,920 | 49,152 | 49,152 |
| `btc-recorder.service` | `memory.stat` `pagetables` | 299,008 | 147,456 | 151,552 |
| `btc-recorder.service` | `memory.stat` `sock` | 0 | 0 | 0 |
| `btc-recorder.service` | `memory.stat` `shmem` | 0 | 0 | 0 |
| `btc-recorder.service` | `memory.stat` `slab_reclaimable` | 612,176 | 14,288 | 1,115,520 |
| `btc-recorder.service` | `memory.stat` `slab_unreclaimable` | 114,688 | 89,184 | 89,184 |
| `btc-chainbook.service` | `memory.current` | 663,552 | not read | 7,516,160 |
| `btc-chainbook.service` | `memory.peak` | 18,735,104 | not read | 18,735,104 |
| `btc-chainbook.service` | `memory.swap.current` | 17,686,528 | not read | 16,703,488 |
| `btc-chainbook.service` | `memory.swap.peak` | 17,686,528 | not read | 17,686,528 |
| `btc-chainbook.service` | `memory.stat` `anon` | 221,184 | not read | 6,860,800 |
| `btc-chainbook.service` | `memory.stat` `file` | 24,576 | not read | 135,168 |
| `btc-chainbook.service` | `memory.stat` `kernel` | 417,792 | not read | 450,560 |
| `btc-chainbook.service` | `memory.stat` `kernel_stack` | 0 | not read | 0 |
| `btc-chainbook.service` | `memory.stat` `pagetables` | 143,360 | not read | 147,456 |
| `btc-chainbook.service` | `memory.stat` `sock` | 0 | not read | 0 |
| `btc-chainbook.service` | `memory.stat` `shmem` | 0 | not read | 0 |
| `btc-chainbook.service` | `memory.stat` `slab_reclaimable` | 220,952 | not read | 250,568 |
| `btc-chainbook.service` | `memory.stat` `slab_unreclaimable` | 43,808 | not read | 43,808 |
| host | `MemAvailable` | 370,880,512 | not read | 286,302,208 |
| host | `MemTotal` | 1,002,127,360 | not read | 1,002,127,360 |
| host | `SwapFree` | 2,898,489,344 | not read | 2,951,176,192 |
| host | `SwapTotal` | 3,250,581,504 | not read | 3,250,581,504 |

**The old code beside the new.** The old process, after 13 h 40 min of running, held `11,247,616` bytes `anon` with `87,597,056` swapped out: `98,844,672` of
its own memory, six in seven of it in swap, beside `1,146,880` of page cache. The new process, 30 s after its start,
held `19,886,080` `anon` and nothing in swap. At `I final`, 46 min after its start, it held `11,075,584` `anon` and
`11,550,720` in swap, `22,626,304` in all, and its `memory.current` of `40,816,640` included `28,262,400` of page
cache (`file`). Fifteen seconds later, §3.8's reads put `MemoryCurrent` at `12,636,160` and `file` at `1,114,112`.
**These are measurements, and none is a gate.** The bound the new code sets is on records held, which G-SYNTH and
G-EQUIV assert, not on bytes. TZ-22 sizes the ceilings from reads over days. The chain book is unchanged, and its
memory is printed for TZ-22's table.

Two reads from systemd's journal complete the old process's side. Both are in §2.14's journal read, verbatim. At its
deactivation at 22:22:02, systemd wrote "Consumed 2min 30.491s CPU time, 201.8M memory peak, 83.5M memory swap
peak" for pid `4067771`, after 13 h 55 min of running. `memory.peak` resets with each restart, so the `I final`
column's peak is the new process's alone.

### 2.14 §3.8 — the closing reads (V16)

§0.2's block again, with `S` the same, into `logs/20-closing-host-gate.log`:

```text
Sun Oct  4 11:08:37 PM UTC 2026
1791155317
1
MemTotal:         978640 kB
MemAvailable:     272076 kB
SwapTotal:       3174396 kB
SwapFree:        2882008 kB
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13274189824
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
3
systemd 255 (255.4-1ubuntu8.17)
enabled
enabled
exit=0
active
active
exit=0
4148534
exit=0
4064090
exit=0
exit=0
exit=0
e3975b5da44c5328adf3bf3914634cd878842c73
2026-10-04T22:22:02+00:00 vultr systemd[1]: btc-recorder.service: Sent signal SIGTERM to main process 4067771 (python) on client request.
2026-10-04T22:22:02+00:00 vultr systemd[1]: btc-recorder.service: Deactivated successfully.
2026-10-04T22:22:02+00:00 vultr systemd[1]: btc-recorder.service: Consumed 2min 30.491s CPU time, 201.8M memory peak, 83.5M memory swap peak.
2026-10-04T22:22:07+00:00 vultr systemd[1]: btc-recorder.service: Scheduled restart job, restart counter is at 2.
2026-10-04T22:22:07+00:00 vultr systemd[1]: Started btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C.
488327816	/root/PROJECT_GAMING_PS5
disabled
exit=1
inactive
exit=3
/root/tz16a-work exit=1
/root/tz19-work exit=1
/root/tz20-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
1487
3.12.3 17.1
/root/btc-5m-twap       c3828d0 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/root/tz21-work/wt      e3975b5 [tz-21-recorder-memory]
201482795	/root/.claude
/tmp/claude-0/-root-btc-5m-twap/f1dda509-7343-505e-8afa-097e9a463ab6/scratchpad
total 32
drwx------  8 root root 4096 Oct  4 22:15 .
drwx------ 12 root root 4096 Oct  4 22:04 ..
drwx------  3 root root 4096 Oct  4 19:04 386a2f9a-9175-46e4-af0d-52cc5355a34c
drwx------  4 root root 4096 Oct  3 22:32 563ca246-a14d-524d-9f7b-7fbc748ed7c6
drwx------  3 root root 4096 Oct  3 22:28 8ec90b6c-b641-47ff-bee9-df7131656d41
drwx------  3 root root 4096 Oct  4 22:04 9b05d639-af52-44b6-9a8c-9f508f7b17c4
drwx------  3 root root 4096 Oct  3 11:27 9be611ff-a833-4160-a076-c4e5a9ca4cc0
drwx------  4 root root 4096 Oct  4 22:04 f1dda509-7343-505e-8afa-097e9a463ab6
```

H1, H2, H3 (recorder pid **`4148534`**, chain book pid `4064090`), H4, H6, H8 and the memory and disk gates read as at
§0.2. **Three reads differ, each as this TZ intended.**
- H5 now prints `e3975b5…`: B-MOVE moved the tree.
- The store holds **1,487** files: B-RECLAIM-SCRATCH added 49.
- `git worktree list` names the branch worktree `/root/tz21-work/wt` as a third entry, which B-RECLAIM-OWN removes.

The journal since `@1791102470` holds the five lines of this TZ's restart and nothing else. The listing still shows
the three directories handed to the Boss, `563ca246…`, `8ec90b6c…` and `9be611ff…`, beside the two kept (§2.3).
`MemAvailable` `272076 kB`; free `13,274,189,824` bytes.

Then §3.8's own reads, verbatim (`logs/21-closing-reads.log`):

```text
$ systemctl show btc-recorder.service btc-chainbook.service -p MainPID -p NRestarts -p MemoryCurrent -p MemoryPeak -p MemoryMax
MainPID=4148534
NRestarts=2
MemoryCurrent=12636160
MemoryPeak=52322304
MemoryMax=536870912

MainPID=4064090
NRestarts=1
MemoryCurrent=7372800
MemoryPeak=18735104
MemoryMax=201326592
$ grep -E '^(anon|file|kernel|sock|shmem) ' /sys/fs/cgroup/system.slice/btc-recorder.service/memory.stat
anon 10784768
file 1114112
kernel 679936
sock 0
shmem 0
$ journalctl -u btc-recorder.service --since "@$(( state_ns // 10**9 - 5 ))" --no-pager -o short-iso
2026-10-04T22:22:02+00:00 vultr systemd[1]: btc-recorder.service: Sent signal SIGTERM to main process 4067771 (python) on client request.
2026-10-04T22:22:02+00:00 vultr systemd[1]: btc-recorder.service: Deactivated successfully.
2026-10-04T22:22:02+00:00 vultr systemd[1]: btc-recorder.service: Consumed 2min 30.491s CPU time, 201.8M memory peak, 83.5M memory swap peak.
2026-10-04T22:22:07+00:00 vultr systemd[1]: btc-recorder.service: Scheduled restart job, restart counter is at 2.
2026-10-04T22:22:07+00:00 vultr systemd[1]: Started btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C.
$ tail -n 40 /var/lib/btc-recorder/recorder.log
2026-10-04T20:25:48Z closed 1791144900 complete=True quotes_complete=True msgs={'twap60': 415, 'twap30': 416, 'chainlink': 416, 'binance': 420}
2026-10-04T20:31:03Z closed 1791145200 complete=True quotes_complete=True msgs={'twap60': 416, 'twap30': 417, 'chainlink': 417, 'binance': 420}
2026-10-04T20:34:03Z closed 1791145500 complete=True quotes_complete=True msgs={'twap60': 413, 'twap30': 413, 'chainlink': 412, 'binance': 420}
2026-10-04T20:39:33Z closed 1791145800 complete=True quotes_complete=True msgs={'twap60': 409, 'twap30': 408, 'chainlink': 408, 'binance': 420}
2026-10-04T20:44:48Z closed 1791146100 complete=True quotes_complete=True msgs={'twap60': 416, 'twap30': 416, 'chainlink': 416, 'binance': 420}
2026-10-04T20:50:33Z closed 1791146400 complete=True quotes_complete=True msgs={'twap60': 415, 'twap30': 415, 'chainlink': 416, 'binance': 420}
2026-10-04T20:54:48Z closed 1791146700 complete=True quotes_complete=True msgs={'twap60': 416, 'twap30': 415, 'chainlink': 414, 'binance': 420}
2026-10-04T20:59:48Z closed 1791147000 complete=True quotes_complete=True msgs={'twap60': 420, 'twap30': 419, 'chainlink': 419, 'binance': 420}
2026-10-04T21:06:03Z closed 1791147300 complete=True quotes_complete=True msgs={'twap60': 417, 'twap30': 416, 'chainlink': 417, 'binance': 419}
2026-10-04T21:09:48Z closed 1791147600 complete=True quotes_complete=True msgs={'twap60': 420, 'twap30': 420, 'chainlink': 420, 'binance': 420}
2026-10-04T21:12:39Z RTDS drop: ConnectionClosedOK(Close(code=1001, reason='Going away'), Close(code=1001, reason='Going away'), True)
2026-10-04T21:12:41Z RTDS connected
2026-10-04T21:13:18Z closed 1791147900 complete=True quotes_complete=True msgs={'twap60': 415, 'twap30': 415, 'chainlink': 415, 'binance': 420}
2026-10-04T21:17:33Z closed 1791148200 complete=False quotes_complete=True msgs={'twap60': 410, 'twap30': 410, 'chainlink': 408, 'binance': 420}
2026-10-04T21:26:48Z closed 1791148500 complete=True quotes_complete=True msgs={'twap60': 406, 'twap30': 406, 'chainlink': 405, 'binance': 416}
2026-10-04T21:31:48Z closed 1791148800 complete=True quotes_complete=True msgs={'twap60': 413, 'twap30': 413, 'chainlink': 413, 'binance': 420}
2026-10-04T21:32:48Z closed 1791149100 complete=True quotes_complete=True msgs={'twap60': 416, 'twap30': 416, 'chainlink': 416, 'binance': 420}
2026-10-04T21:38:33Z closed 1791149400 complete=True quotes_complete=True msgs={'twap60': 416, 'twap30': 415, 'chainlink': 416, 'binance': 420}
2026-10-04T21:46:33Z closed 1791149700 complete=True quotes_complete=True msgs={'twap60': 415, 'twap30': 414, 'chainlink': 414, 'binance': 420}
2026-10-04T21:48:33Z closed 1791150000 complete=True quotes_complete=True msgs={'twap60': 419, 'twap30': 420, 'chainlink': 419, 'binance': 420}
2026-10-04T21:53:33Z closed 1791150300 complete=True quotes_complete=True msgs={'twap60': 416, 'twap30': 416, 'chainlink': 417, 'binance': 420}
2026-10-04T21:58:33Z closed 1791150600 complete=True quotes_complete=True msgs={'twap60': 419, 'twap30': 419, 'chainlink': 418, 'binance': 420}
2026-10-04T22:04:33Z closed 1791150900 complete=True quotes_complete=True msgs={'twap60': 410, 'twap30': 410, 'chainlink': 406, 'binance': 420}
2026-10-04T22:12:04Z closed 1791151200 complete=True quotes_complete=True msgs={'twap60': 420, 'twap30': 420, 'chainlink': 419, 'binance': 420}
2026-10-04T22:13:33Z closed 1791151500 complete=True quotes_complete=True msgs={'twap60': 412, 'twap30': 413, 'chainlink': 412, 'binance': 420}
2026-10-04T22:21:18Z closed 1791151800 complete=True quotes_complete=True msgs={'twap60': 408, 'twap30': 408, 'chainlink': 408, 'binance': 420}
2026-10-04T22:22:07Z recorder sha=e3975b5da44c5328adf3bf3914634cd878842c73 root=/var/lib/btc-recorder
2026-10-04T22:22:07Z pre-run floors: free=13285228544 (floor 2000000000) captured=582379618 (cap 4000000000)
2026-10-04T22:22:08Z recovering interval 1791152100
2026-10-04T22:22:08Z interval 1791152400: 2 checkpoints had already passed and are not read
2026-10-04T22:22:08Z RTDS connected
2026-10-04T22:26:38Z closed 1791152100 complete=True quotes_complete=True msgs={'twap60': 417, 'twap30': 417, 'chainlink': 419, 'binance': 420}
2026-10-04T22:29:18Z closed 1791152400 complete=False quotes_complete=True msgs={'twap60': 413, 'twap30': 413, 'chainlink': 412, 'binance': 415}
2026-10-04T22:35:18Z closed 1791152700 complete=True quotes_complete=True msgs={'twap60': 416, 'twap30': 416, 'chainlink': 415, 'binance': 420}
2026-10-04T22:38:48Z closed 1791153000 complete=True quotes_complete=True msgs={'twap60': 413, 'twap30': 416, 'chainlink': 416, 'binance': 417}
2026-10-04T22:45:18Z closed 1791153300 complete=True quotes_complete=True msgs={'twap60': 412, 'twap30': 412, 'chainlink': 413, 'binance': 420}
2026-10-04T22:50:03Z closed 1791153600 complete=True quotes_complete=True msgs={'twap60': 417, 'twap30': 417, 'chainlink': 417, 'binance': 420}
2026-10-04T22:55:48Z closed 1791153900 complete=True quotes_complete=True msgs={'twap60': 413, 'twap30': 413, 'chainlink': 413, 'binance': 420}
2026-10-04T23:00:18Z closed 1791154200 complete=True quotes_complete=True msgs={'twap60': 410, 'twap30': 411, 'chainlink': 410, 'binance': 420}
2026-10-04T23:05:18Z closed 1791154500 complete=True quotes_complete=True msgs={'twap60': 417, 'twap30': 417, 'chainlink': 417, 'binance': 420}
$ cat /root/tz21-work/state.json
{"branch_head": "e3975b5da44c5328adf3bf3914634cd878842c73", "cb_pid": 4064090, "cb_restarts": 1, "marks": {"kill-rec": {"cb_pid": 4064090, "cb_restarts": 1, "ns": 1791152512605133323, "rec_pid": 4067771, "rec_restarts": 1}}, "rec_pid": 4067771, "rec_restarts": 1, "records": 62344, "restart": {"pid": 4148534, "restarts": 2, "start_ns": 1791152527734526971}, "state_ns": 1791151617605002534}
$ free -b
               total        used        free      shared  buff/cache   available
Mem:      1002127360   685142016    88948736      131072   413949952   316985344
Swap:     3250581504   337334272  2913247232
$ du -sb /root/tz21-work /root/btc-recorder-svc /root/.claude
24388092	/root/tz21-work
4626222	/root/btc-recorder-svc
201498249	/root/.claude
2026-10-04T23:08:45Z
```

The journal since 5 s before `I state` holds systemd's five lines for the recorder: the `SIGTERM` to pid `4067771`
at 22:22:02 on client request, its deactivation and its peak — `2min 30.491s` CPU, `201.8M` memory, `83.5M` swap —
the scheduled restart with the counter at `2`, and the start at 22:22:07. `recorder.log`'s last 40 lines show the
new process's start at 22:22:07 on `e3975b5…` with its floors, the recovery of `1791152100`, two checkpoints of
`1791152400` passed and not read, RTDS connected at 22:22:08, and every close since, `1791152400` the one with
`complete=False`. `free -b` puts `available` at `316,985,344`. `du`: `/root/tz21-work` `24,388,092` bytes,
`/root/btc-recorder-svc` `4,626,222`, `/root/.claude` `201,498,249`.

### 2.15 `state.json` — every instant

`state.json` at the closing reads, verbatim, is in §2.14. Every instant it holds, with the instants the run read
beside them:

| instant | `ns` / epoch | UTC | source |
|---|---|---|---|
| `state_ns`, `I state` | `1791151617605002534` | 22:06:57.605 | `state.json` |
| `marks.kill-rec.ns` | `1791152512605133323` | 22:21:52.605 | `state.json`, with recorder pid `4067771` `NRestarts` 1 and chain book pid `4064090` `NRestarts` 1 |
| the signal | `1791152522.108717658` | 22:22:02.109 | B-KILL-REC's `date -u +%s.%N` |
| `restart.start_ns`, the new `start` record | `1791152527734526971` | 22:22:07.735 | `state.json`, with pid `4148534` and `restarts` 2 |
| G-REC PASS | `1791154692` | 22:58:12 | `logs/18-rec-08.log` |
| `I final` | — | 23:08:21–23:08:22 | `logs/19-final.log` |

`state.json` holds no `revert` mark: K-21 was never run.

### 2.16 §9 B-RECLAIM-OWN — last, after §3.8, with this report drafted

Run by the Executor from 23:11:24 UTC, after §3.8's reads and with this report drafted in the primary checkout.
**Its output was written to no file** (§9); it is quoted here from the session. The block's lines ran as separate
commands, in its order, so that a refusal of `rm -rf` could not discard the `reclaim` before it. None was
refused.

```text
$ date -u +%FT%T.%NZ; I reclaim /root/tz21-work; echo "exit=$?"
2026-10-04T23:11:24.533591148Z
[2026-10-04T23:11:24Z] reclaim: 1617 report tokens; forensic store holds 1487 files
[2026-10-04T23:11:24Z] reclaim: /root/tz21-work/wt skipped: no file but its HEAD's, and HEAD e3975b5da44c5328adf3bf3914634cd878842c73 is its upstream's
[2026-10-04T23:11:24Z] R copied 95f8636b544fd2443f85a99373ce30788b7f2f8a9fcd3e2a8459c4d920ae8019 /root/btc-forensics/tz21-work--state.json
[2026-10-04T23:11:24Z] R copied b0fde528447347cdd75158b72f002742bf231028a28d6dcefabedc3edabe45b0 /root/btc-forensics/tz21-work--logs--00-fingerprint.log
[2026-10-04T23:11:24Z] R copied dca62f5b54d42b807c2e6bfb4de952f776e4844ed5aaac45d9b3555989be1163 /root/btc-forensics/tz21-work--logs--00-start.log
[2026-10-04T23:11:24Z] R copied a83593cdda729e3c12848a52f1e7ab76e08b6727ff9d6e3e2dfa5f92ac740da6 /root/btc-forensics/tz21-work--logs--01-host-gate.log
[2026-10-04T23:11:24Z] R copied cd1def13ac6f85f45c243a932da0ddf4f28254259600406d61cafd37876756b4 /root/btc-forensics/tz21-work--logs--02-refs.log
[2026-10-04T23:11:24Z] R copied b5c281e9d0dac5883cbb22daf5112900abd2e76af2b60426f28963016ca80d02 /root/btc-forensics/tz21-work--logs--03-branch.log
[2026-10-04T23:11:24Z] R copied e4e7336e07ef1b98d7b2d6b4bb6e685e15a0645d0cae7339ec8862902578808b /root/btc-forensics/tz21-work--logs--04-extract.log
[2026-10-04T23:11:24Z] R copied 3c0724aac1334fc280958437276fd325aa2960170d071c043d9a519fafc4a4a1 /root/btc-forensics/tz21-work--logs--05-commit-push.log
[2026-10-04T23:11:24Z] R copied af89b6834332d2ff2acf7b326c3a96d9f207b06d30e3895a2250fabedee3b170 /root/btc-forensics/tz21-work--logs--06-pr.log
[2026-10-04T23:11:24Z] R copied 70f07fe479c3fd8d5790c8e093ee3a0018b6b3f143aac71426f92217a42d9f86 /root/btc-forensics/tz21-work--logs--07-state.log
[2026-10-04T23:11:24Z] R copied b1c3f50b9bc070b08f9671ee274048c6b92c26e4f9d6a5079b2fea04f7607bd2 /root/btc-forensics/tz21-work--logs--08-scratch-listing.log
[2026-10-04T23:11:24Z] R copied 658babc69c7ebf6e7cf9f6a11df07ccffb71c3772dd5984cc1aa7e3343d5364e /root/btc-forensics/tz21-work--logs--09-reclaim-scratch.log
[2026-10-04T23:11:24Z] R copied 9773b77f6b52a0f92e9e372644ed6b24e7d6f058cfb8754e16ee1c0004d83c43 /root/btc-forensics/tz21-work--logs--10-rm-scratch.log
[2026-10-04T23:11:24Z] R copied e207a90412e0e40612d50607339554820486eb650a14ede789fa4d8c724a8862 /root/btc-forensics/tz21-work--logs--11-selftest.log
[2026-10-04T23:11:24Z] R copied 9bb46a950c1ce96487b82f90beb9fa5895b6a6cec5084d3277404f084d730149 /root/btc-forensics/tz21-work--logs--12-synth.log
[2026-10-04T23:11:24Z] R copied fce797e17ad613ecd4ef731da15403c915d26e8c78a20272b2a0f09bc50a967c /root/btc-forensics/tz21-work--logs--13-equiv.log
[2026-10-04T23:11:24Z] R copied 70f125d45b3b1c3308c47698f6993b1ef40742747ed8372869f28cff59aff629 /root/btc-forensics/tz21-work--logs--14-b-move.log
[2026-10-04T23:11:24Z] R copied c9f798867bd9a599a1cc03696765f92017e9d8c64064b6325ce335d9e2a24cbd /root/btc-forensics/tz21-work--logs--15-path.log
[2026-10-04T23:11:24Z] R copied 500cf820cbc97a77167cb5b76c815e921e0845b744762c12aeb172023360ddf9 /root/btc-forensics/tz21-work--logs--16-b-kill-rec.log
[2026-10-04T23:11:24Z] R copied 7f4c9ba8020b765b778758228a95b665b2e82662fe1a1d81692e61b2fa1d8070 /root/btc-forensics/tz21-work--logs--17-restart.log
[2026-10-04T23:11:24Z] R copied 8e72b77c94383203e290e6eab1996aecf94b8cfab251f484e4438bfe2fdb5b9a /root/btc-forensics/tz21-work--logs--18-rec-01.log
[2026-10-04T23:11:24Z] R copied 56d067766dd7e1536154145199f892f3fe9af425106df5fb9f5f8b7e9786667a /root/btc-forensics/tz21-work--logs--18-rec-02.log
[2026-10-04T23:11:24Z] R copied d8a7c81d5ecaf1696383fca7b7dde02e506d91bb55ee85bef02e3a03765f0411 /root/btc-forensics/tz21-work--logs--18-rec-03.log
[2026-10-04T23:11:24Z] R copied ef191d87d033e9ac148119d77db1324f4bcfa8182e880f2ebf91d79efb6e8779 /root/btc-forensics/tz21-work--logs--18-rec-04.log
[2026-10-04T23:11:24Z] R copied ce35cbdeca6c9a2b7c71e5236464f9fd1dc7d2ec8544b44f5ccd2ecb28e8e8a1 /root/btc-forensics/tz21-work--logs--18-rec-05.log
[2026-10-04T23:11:24Z] R copied 398d8b5e099136016741edd2a26f10d7e7efdb4b9f3d2d84fad06a14616118cd /root/btc-forensics/tz21-work--logs--18-rec-06.log
[2026-10-04T23:11:24Z] R copied 5fb4f4e4c12c9697c9e329fcb2ebd22d50a602a9d2eb123d49a92c5eea1b703b /root/btc-forensics/tz21-work--logs--18-rec-07.log
[2026-10-04T23:11:24Z] R copied 02e02e341b3acac04abaae5b482ce8ca4b4a114bae314ea6d7bb85cbbcb25ec8 /root/btc-forensics/tz21-work--logs--18-rec-08.log
[2026-10-04T23:11:24Z] R copied e465e37170cde6db72be68763ea56622b547f3da5321015f299aa49878e8a652 /root/btc-forensics/tz21-work--logs--19-final.log
[2026-10-04T23:11:24Z] R copied 525d649420932a7a05e22f9c4e12ab5753fed623e55c622e5cd7520fa5a01b63 /root/btc-forensics/tz21-work--logs--20-closing-host-gate.log
[2026-10-04T23:11:24Z] R copied 1dc8c0dcfe11667d4dadd285f5c1af575d769ead2b70825efe0a0bda3639623b /root/btc-forensics/tz21-work--logs--21-closing-reads.log
[2026-10-04T23:11:24Z] R copied eb99f787bc5321195d7d8706593253c8de1ef34b826dd0f7a3d6b4f5925ce152 /root/btc-forensics/tz21-work--logs--22-separation-check.log
[2026-10-04T23:11:24Z] RECLAIM PASS: 73 files considered, 0 named by a report, 32 kept by name, 32 copied, 0 already held; forensic store 1487 -> 1519 files
[2026-10-04T23:11:24Z] peak memory of this run: 23937024 bytes
[2026-10-04T23:11:24Z] opens under the capture roots: 0
exit=0
$ git -C /root/btc-5m-twap worktree remove /root/tz21-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz21-work; echo "exit=$?"
exit=0
$ date -u +%FT%T.%NZ; test -e /root/tz21-work; echo "exit=$?"; git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list; find /root/btc-forensics -type f | wc -l; df -B1 --output=source,size,avail /var/lib/btc-recorder
2026-10-04T23:11:32.649896652Z
exit=1
/root/btc-5m-twap       c3828d0 [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
1519
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13298954240
```

**RECLAIM PASS**: 73 files considered; none named by a report; `state.json` and the 31 files of `logs/` kept by name
and copied, 32 in all; the store 1,487 → **1,519**. The other 41 files were under `scratch/`: G-SYNTH's and G-EQUIV's
trees, G-REC's slice, and this report's template, snippets and filling scripts. No report cites any of them. The
worktree was skipped by name: `git status --porcelain --ignored` printed nothing in it, and its `HEAD` was its
upstream's, so `git worktree remove` needed no `--force` and exited `0`. `rm -rf` exited `0`; `test -e` exits `1`;
`git worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else. **The logs this report
quotes are in the forensic store as `/root/btc-forensics/tz21-work--logs--<name>`**, each hash printed above. The
branch `tz-21-recorder-memory` stays on `origin` and as a local ref. `/root/btc-recorder-svc` and `/root/tz18a-svc`
are the two units' code and stay.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-21-recorder-memory`, committed at 22:06:37 UTC and pushed before the pull request was opened at 22:06:51 UTC; it stays on `origin` and as a local ref |
| implementation commit | `e3975b5da44c5328adf3bf3914634cd878842c73`, parent `c3828d0` |
| pull request | #22, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/22`, open against `main`, head `e3975b5`, **not merged** |
| deployment | `/root/btc-recorder-svc` at `e3975b5` since B-MOVE at 22:19:04 UTC; the unit runs it since 22:22:07 UTC, as TZ-18a's and TZ-20's processes ran their branches before their merges (§1 item 6) |
| Release | none; none is required, and no dataset, archive or binary entered git history |
| report | this file, straight to `main`, one commit |

**Contract §4.2's self-check (V15)**, run at 23:08:53 UTC, after the push and the pull request and before this
report's commit (`logs/22-separation-check.log`):

```text
Sun Oct  4 11:08:53 PM UTC 2026
fetch exit=0
$ git rev-list origin/main | grep -c e3975b5da44c5328adf3bf3914634cd878842c73
0
$ git diff --name-only origin/main origin/tz-21-recorder-memory
research/recorder/recorder.py
research/tz21-recorder-memory.py
$ git diff --name-status origin/main origin/tz-21-recorder-memory
M	research/recorder/recorder.py
A	research/tz21-recorder-memory.py
$ git diff --numstat origin/main origin/tz-21-recorder-memory
49	6	research/recorder/recorder.py
1284	0	research/tz21-recorder-memory.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
grep exit=1
c3828d031109beaaef67a6189112317695259101
e3975b5da44c5328adf3bf3914634cd878842c73
{"baseRefName":"main","headRefOid":"e3975b5da44c5328adf3bf3914634cd878842c73","mergedAt":null,"number":22,"state":"OPEN","url":"https://github.com/seahomebatumi-ai/btc-5m-twap/pull/22"}
```

The first line prints `0`. The diff names exactly the two paths, `M` with `49` insertions and `6` deletions and `A`.
The `grep` prints nothing.

---

## 4. Gate

| gate | quoted from TZ-21 §4 | deciding numbers | reading |
|---|---|---|---|
| **G-SYNTH** | "every slice compared byte-identical, at least `600` from memory and `60` from disk; both controls detected; at most `2,000` records held after any load or prune" | 913 of 913 equal; **836** from memory against 600; **77** from disk against 60; controls 2 of 2; held at most **242** against 2,000 | **PASS** |
| **G-EQUIV** | "every window byte-identical, at least `12` from memory and `200` from disk; the old load's count and digest equal the parse's; at most `2,000` records held; the snapshot the file's first bytes" | 825 of 825 equal; **23** against 12; **802** against 200; 62,362 records, count and digest equal; held **233** against 2,000; the first 12,938,179 bytes hash to `ef2b429c…` | **PASS** |
| **G-PATH** | "every assert, at one of two runs 300 s apart" | P0 to P4 at the first run; HTTP 2 of 2; SNTP 2 of 2; RTDS 4 of 4 topics | **PASS** |
| **G-RESTART** | "§4.3" | 1 `start` on `e3975b5…`; 1 `startup` gap, its start 8.897 s after the mark against no earlier than −5.000 s, lasting **6.771 s** against 60.000; no `halt`; `NRestarts` 1 → 2; pid `4067771` → `4148534`, the sole instance; unit checks | **PASS** |
| **G-REC** | "the first `5` intervals … each `manifest.json` present by `T0 + 3,900`, `quotes_complete` true at 5 of 5, `recorder_git_sha` the branch head at 5 of 5, and `complete` true at at least 3 of 5"; every earlier interval's and member's slice equal to the old code's | manifests 5 of 5; `quotes_complete` 5 of 5; sha 5 of 5; **`complete` 5 of 5** against 3, a margin of 2.000 intervals; slices equal **7 of 7** (2 earlier, 5 members) | **PASS** |
| **G-FINAL** | "§4.5" | pid `4148534` and `NRestarts` 2, those G-RESTART read; tree at `e3975b5…` with 3 of 3 hashes; newest `start` G-RESTART's | **PASS** |
| **G-CB-STILL** | "§4.6" | pid `4064090` and `NRestarts` 1 at `I state`, at the `kill-rec` mark and at `I final`; the sole instance; unit checks | **PASS** |

Family-wise false failure, as fixed: at most `0.0102`, G-REC's. Nothing was tuned, and no gate was re-read.
**Under PASS no block of §4.7 was run: neither K-21a, K-21 nor K-20R.**

---

## 5. Validation

| # | check | count | asserted |
|---|---|---|---|
| **V1** | §0.1's fingerprint | 6 anchors, **4 of 4** re-derived, **28 of 28** `frozen` equal, 2 `tracked`, 1 `reported`; 31 rows | asserted by the fingerprint script (exit 0) |
| **V2** | §0.2's host gate | H1 to H9, the memory gate and the disk gate, each read named in §0.2's table | recorded, not asserted: compared by the Executor |
| **V3** | `I state` | **S1 to S7**, `STATE PASS` | asserted, exit 0 |
| **V4** | §3.1's two files | **2 of 2** hashes asserted by §3.1's script, the frozen `9fd1c7de…` asserted before the replacement; lines and bytes equal by `wc`; the diff names exactly 2 paths, `M` **49**/**6** and `A` | hashes asserted; lines, bytes and the diff recorded, not asserted |
| **V5** | the self-test | **`115 of 115`** | asserted by `selftest.py`, exit 0 |
| **V6** | G-SYNTH | **836** from memory against 600, **77** from disk against 60; held **242** against 2,000; controls **2 of 2** | asserted, exit 0 |
| **V7** | G-EQUIV | **23** from memory against 12, **802** from disk against 200; count and digest equal; held **233**; the prefix's hash equal | asserted, exit 0 |
| **V8** | B-MOVE | `HEAD` equal; **3 of 3** hashes; **`0`** status lines | recorded, not asserted: compared by the Executor |
| **V9** | G-PATH | P0 to P4; **2** HTTP requests, SNTP **2 of 2**, RTDS **4 of 4** topics | asserted, exit 0 |
| **V10** | G-RESTART | **1** start, **1** gap of **6.771 s** against 60, `NRestarts` 1 → **2**, a new pid | asserted, exit 0 |
| **V11** | G-REC | **5** members, each present, `quotes_complete`, on the branch head and `complete`; slices equal **7 of 7**, **2** earlier intervals and **5** members; 8 runs | asserted, exit 0 at the 8th run |
| **V12** | opens under the capture roots | the printed counts: `state` 1, `reclaim` (scratch) 0, `synth` 0, `equiv` 2, `path` 0, `mark kill-rec` 0, `restart` 1, `rec` 0 at each of the 7 NOT YET runs and 15 at the PASS, `final` 1, `reclaim` (own) 0. **No refusal in any run** | the audit hook raises on a refusal; no run raised |
| **V13** | G-FINAL | the unit, pid `4148534`, `NRestarts` 2, its tree at `e3975b5…`, its newest `start` | asserted, exit 0 |
| **V14** | G-CB-STILL | pid `4064090` and `NRestarts` 1, unchanged | asserted, exit 0 |
| **V15** | contract §4.2's self-check | `0`; 2 paths; nothing | recorded, not asserted; run after the push and the PR, before this report's commit (§3) |
| **V16** | §3.8's closing reads | every read printed (§2.14) | recorded, not asserted |
| **V17** | §9's `reclaim` runs | scratch: considered `62`, named by a report `49`, kept by name `0`, copied `49`, already held `0`, store `1,438` → `1,487`; own: considered `73`, named `0`, kept by name `32`, copied `32`, already held `0`, store `1,487` → `1,519`; the worktree skipped by name, pristine at its upstream | `after == before + copied` asserted in each |
| **V18** | §9's removals | `git worktree remove` without `--force` exit `0`; `test -e` exit `1` for `/root/tz21-work`; `test -e` exit `1` for each of the **10** scratch directories removed, 7 by the Executor and 3 by the Boss (§2.3); `git worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else | recorded, not asserted: exit statuses read |
| **V19** | memory | each unit's `memory.current`, `memory.peak`, swap and nine `memory.stat` keys, and the host's `MemAvailable`, at `I state`, `I restart` and `I final`, in one table (§2.13); `I restart` reads the recorder alone | recorded, not asserted |

---

## 6. What could not be implemented as written

1. **The fingerprint script's first run stopped on its own assert.** It split the TZ's header on `---`, which cut
   at the anchor table's separator row, so it found no anchor in the TZ and asserted on that. It had read files
   only, and it hashed no row. It was corrected to split on a line holding `---` alone and run again. §0.1 quotes
   the second run, which is the only one in `logs/00-fingerprint.log`.
2. **B-RECLAIM-SCRATCH named ten of the twelve directories, not twelve.** §0.2 calls every UUID directory beside this
   session's own "the scratch directories earlier sessions left". Two of the twelve were not. `9b05d639…` was born
   1.1 s after this session's own process started, and `386a2f9a…` 4 s after the `claude remote-control` bridge
   that runs this session, which is still running (§2.3, `logs/08-scratch-listing.log`). Both are empty: a
   `scratchpad` directory each, with no file. Removing a live process's directory is not reclaiming an earlier
   session's scratch, and it cannot be undone, so the Executor kept both. §9's rule, "This session's own
   directory is never named", covers the first on its plain reading. Both hold 0 bytes. The next TZ's listing
   will show them, and by then neither owner may be running.
3. **Three of the ten removals were refused by the session's classifier and handed to the Boss.**
   The classifier refused `563ca246…`, `8ec90b6c…` and `9be611ff…` as "[Interfere With Workloads]" and allowed
   the other seven, each the same single-tree `rm -rf`. §3 says the Executor "waits and then verifies". The Executor
   handed the three over at 22:23:54 UTC and carried on with §3.3, because nothing from §3.3 on depends on them.
   It waited for the Boss before committing this report. The Boss ran them after B-RECLAIM-OWN, at about 00:46 UTC
   on 2026-10-05, and the Executor verified all three by `test -e` (exit `1`) at 00:46:52. So B-RECLAIM-SCRATCH
   ended after B-RECLAIM-OWN, not before §3.3, and its verification is quoted from the session (§2.3), because
   `logs/` was already gone.
4. **V19's table has "not read" cells at `I restart`.** `mode_restart` calls `memory(REC_UNIT)` alone. It does not
   call `memory(CB_UNIT)` or `meminfo()`, so the instrument read neither the chain book's control group nor
   `MemAvailable` at that instant. The Executor did not add a read the instrument does not make. The nearest host
   reads are `I equiv`'s `MemAvailable` `274,857,984` at 22:16:12, before the restart, and `I final`'s after it.
5. **One read under the capture root that §2 item 2 does not name.** At 22:30:26 UTC, while G-REC waited, the
   Executor ran `ls -la` on `/var/lib/btc-recorder/btc-updown-5m/`. It listed interval directory names and their
   modification times, the last 18 of them. It opened no file, and it printed no price and no content. The listing
   was a timing check, to estimate when the members' manifests would land. The instrument's audit hook was not
   running in that shell, and the read is not in any log. It is disclosed here, and it was not repeated.
6. **B-MOVE's block carries three reads beyond the TZ's five lines**: `state.json`'s `branch_head`, `systemctl show`
   of the recorder's MainPID and `NRestarts`, and a UTC stamp before and after. They make V8's "`HEAD` equal" and
   K-21a's "the old process never stopped" readable in one log. They change nothing.
7. **G-REC's background loop was replaced once.** The harness stops a watch after 30 minutes, so the Executor
   stopped the first loop after run 6 at 22:48:10 and started a second, which ran 7 and 8 at 300 s spacing as
   before. The first wait for `I final` was started with a mistyped instant, 20 minutes too late. It was stopped before
   22:58:29, before it ran anything, and started again on `1791154692 + 608`, so `I final` ran at 23:08:20, 608 s
   after G-REC's PASS.
8. **Where the session's harness keeps output.** Every command wrote its output to `/root/tz21-work/logs/` first.
   The harness also keeps its own copy of each background command's terminal output, here the `tail` of a log, as
   a file under this session's directory in `/tmp/claude-0/-root-btc-5m-twap/f1dda509…/tasks/`, beside the
   scratchpad. Nothing was written to the scratchpad. B-RECLAIM-OWN's output was written to no file, as §9 orders,
   and §2.16 quotes it from the session.
9. **A reading for the next TZ, not a deviation.** `I synth` peaked at `58,191,872` bytes here, against the
   Architect's `54,984,704`. §0.3's floor, `110,000,000`, is twice the Architect's peak, and twice this run's
   would be `116,383,744`. The gate read `MemAvailable` at `265,342,976` before `synth` started, so the floor was
   never close. It is fixed by the TZ and not re-derived here.
10. **`reclaim` own read this report's draft as well as the committed reports.** §8 orders the report drafted in the
    primary checkout before B-RECLAIM-OWN, and `report_tokens` reads every `.md` in `CryptoReports/`, committed or
    not. So the draft's hex runs counted, 1,617 tokens against B-RECLAIM-SCRATCH's 1,603. No file was named by one:
    the run printed `0 named by a report`. After it, the draft was changed only by filling §0.3's last row, §2.16,
    V12, V17, V18, and the opening's, §2.3's and item 3's account of the Boss's removals; by adding §0's quote of
    `logs/00-start.log`, read back from the forensic store; by this item; and by rewording one sentence of §2.16,
    two of §2.11 (to state only what `recorder.log` and the manifests show) and one pronoun. The `logs/` blocks of §0 to §3 were filled by script from the logs before B-RECLAIM-OWN,
    and every one equals its copy in the forensic store byte for byte.
