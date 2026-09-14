# TZ-09 — Disk inventory, bounded reclamation and the retention rule: report

**Consumer, by the §3 M3 rule: `/root`, at `43,490,744` bytes/day.** Over the deciding window its delta of `1,843,200` bytes is the only one below `/` that exceeds half the `3,657,728`-byte fall in `df` available. **Free space at run end:** `14,416,265,216` bytes, at 2026-09-14 00:03:15 UTC. **`D` = `86,304,964` bytes/day. `A` = `2,258,914,892` bytes. Days to `F` at `D`: `143.87`.**

That paragraph is exactly what §3 and §5.4 define, and it names this run rather than the drain §6 describes. Three facts from the same files qualify it.

1. **What the named consumer is made of.** `/root`'s delta is `/root/tz09-work` `1,159,168`, `/root/PROJECT_GAMING_PS5` `348,160`, `/root/.claude` `331,776`, and `4,096` in files directly under `/root`. `/root/tz09-work` is this TZ's own scratch and `/root/.claude` is the Executor's session store.
2. **The deciding window was quiet.** `D` is `0.086` of §6's `1,001,128,762` bytes/day, and `0.103` of its `839,142,243`.
3. **A read the TZ did not ask for found the drain.** It is disclosed in §6 item 2 and is not the deciding measurement. Over `11,440` s after `t1`, free space fell `367,521,792` bytes, which is `2,775,683,706` bytes/day. `337,338,368` of those bytes went into `/root/PROJECT_GAMING_PS5/netaudit/telemetry/captures`, and the same rule applied to that window names that directory. It belongs to `PROJECT_GAMING_PS5`, not to this project, so this TZ named it and did nothing to it.

Between that read and R4, free space rose to `14,251,536,384` bytes. The Boss reports that another project's engineer cleared those captures. A read-only `du` at 2026-09-14 00:01:51 UTC measured the directory at `40,960` bytes. This TZ performed none of that. The run-end free space and the days to `F` above include it; `D` does not.

---

## 1. Measurement — TZ-09 §3

Every size below is in exact bytes and every reading carries its UTC timestamp. `t0` and `t1` are the two M3 runs. `t0b` is V3's immediate re-run.

### 1.1 M1 — baseline

| read | UTC | total | used | available | inodes total | inodes used |
|---|---|---|---|---|---|---|
| `t0` | 2026-09-13T17:55:36Z | 31,612,203,008 | 23,605,805,056 | 6,570,528,768 | 8,205,120 | 237,533 |
| `t1` | 2026-09-13T18:56:38Z | 31,612,203,008 | 23,609,462,784 | 6,566,871,040 | 8,205,120 | 237,669 |

The source is `/dev/vda2` for both, read with `df -B1 --output=source,size,used,avail /var/lib/btc-recorder` and `df --output=itotal,iused,iavail`.

### 1.2 M2 — size inventory

The commands, as run at `t0`, in this order:

- `du -x -B1 --max-depth=1 /`: 2026-09-13T17:55:36Z, 4.882 s, exit 0, 18 rows, 0 stderr lines
- `du -x -B1 --max-depth=2 /var`: 2026-09-13T17:55:41Z, 0.1 s, exit 0, 105 rows, 0 stderr lines
- `du -x -B1 --max-depth=2 /root`: 2026-09-13T17:55:41Z, 0.324 s, exit 0, 95 rows, 0 stderr lines
- `du -x -B1 --max-depth=2 /home`: 2026-09-13T17:55:42Z, 0.004 s, exit 0, 10 rows, 0 stderr lines
- `du -x -B1 --max-depth=2 /srv`: 2026-09-13T17:55:42Z, 0.001 s, exit 0, 1 rows, 0 stderr lines
- `du -x -B1 --max-depth=2 /opt`: 2026-09-13T17:55:42Z, 0.002 s, exit 0, 7 rows, 0 stderr lines
- `du -x -B1 --max-depth=2 /usr`: 2026-09-13T17:55:42Z, 3.016 s, exit 0, 306 rows, 0 stderr lines
- `du -x -B1 --max-depth=2 /tmp`: 2026-09-13T17:55:45Z, 0.07 s, exit 0, 573 rows, 0 stderr lines
- `du -x -B1 --max-depth=3 /root/PROJECT_GAMING_PS5`: 2026-09-13T17:55:45Z, 0.031 s, exit 0, 49 rows, 0 stderr lines
- `du -x -B1 --max-depth=3 /var/log`: 2026-09-13T17:55:45Z, 0.002 s, exit 0, 14 rows, 0 stderr lines
- `du -x -B1 --max-depth=3 /usr/lib`: 2026-09-13T17:55:45Z, 0.133 s, exit 0, 781 rows, 0 stderr lines

The three largest subtrees that are not this project's were chosen as the three largest depth-2 directories from the seven `--max-depth=2` runs, excluding this project's own paths: `/root/PROJECT_GAMING_PS5`, `/var/log`, `/usr/lib`. Each was drilled with `du -x -B1 --max-depth=3 <subtree>`. Where one directory appears in several commands, the value given is the one from the most specific command covering it.

Every directory at or above `100,000,000` bytes at `t0`, in descending order:

| # | directory | bytes | this project's |
|---|---|---|---|
| 1 | `/` | 23,577,714,688 | — |
| 2 | `/root` | 10,594,541,568 | — |
| 3 | `/root/PROJECT_GAMING_PS5` | 8,471,851,008 | — |
| 4 | `/root/PROJECT_GAMING_PS5/netaudit` | 8,462,696,448 | — |
| 5 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry` | 8,372,269,056 | — |
| 6 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry/captures` | 6,896,218,112 | — |
| 7 | `/usr` | 4,588,097,536 | — |
| 8 | `/var` | 4,205,408,256 | — |
| 9 | `/var/log` | 3,160,764,416 | — |
| 10 | `/var/log/journal` | 3,019,530,240 | — |
| 11 | `/var/log/journal/1c53327a4d7a4405a156a1989a76a001` | 3,002,740,736 | — |
| 12 | `/usr/lib` | 2,669,535,232 | — |
| 13 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry/logs` | 1,007,222,784 | — |
| 14 | `/usr/lib/x86_64-linux-gnu` | 780,701,696 | — |
| 15 | `/usr/lib/firmware` | 674,009,088 | — |
| 16 | `/usr/bin` | 622,911,488 | — |
| 17 | `/root/tz01-env` | 540,434,432 | yes |
| 18 | `/usr/share` | 533,917,696 | — |
| 19 | `/root/tz01-env/venv` | 471,957,504 | yes |
| 20 | `/var/www` | 470,327,296 | — |
| 21 | `/var/www/adjarabot` | 469,594,112 | — |
| 22 | `/tmp` | 453,599,232 | — |
| 23 | `/var/lib` | 419,340,288 | — |
| 24 | `/usr/lib/modules` | 332,951,552 | — |
| 25 | `/usr/src` | 325,926,912 | — |
| 26 | `/root/btc-5m-twap` | 313,143,296 | yes |
| 27 | `/root/.npm` | 301,248,512 | — |
| 28 | `/root/.npm/_cacache` | 301,178,880 | — |
| 29 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry/line-monitor` | 294,944,768 | — |
| 30 | `/root/crypto-auto` | 292,741,120 | — |
| 31 | `/home` | 266,657,792 | — |
| 32 | `/home/ai_developer` | 266,620,928 | — |
| 33 | `/root/crypto-auto/.claude` | 265,330,688 | — |
| 34 | `/home/ai_developer/.local` | 259,440,640 | — |
| 35 | `/usr/lib/node_modules` | 233,283,584 | — |
| 36 | `/usr/lib/node_modules/@anthropic-ai` | 216,178,688 | — |
| 37 | `/usr/lib/node_modules/@anthropic-ai/claude-code` | 216,174,592 | — |
| 38 | `/root/my_real_estate_bot` | 210,751,488 | — |
| 39 | `/boot` | 210,616,320 | — |
| 40 | `/var/lib/apt` | 205,623,296 | — |
| 41 | `/usr/lib/llvm-18` | 188,022,784 | — |
| 42 | `/usr/lib/llvm-18/lib` | 188,018,688 | — |
| 43 | `/usr/local` | 167,690,240 | — |
| 44 | `/usr/local/lib` | 167,575,552 | — |
| 45 | `/usr/lib/modules/6.8.0-136-generic` | 161,607,680 | — |
| 46 | `/usr/lib/modules/6.8.0-139-generic` | 161,509,376 | — |
| 47 | `/root/btc-5m-twap/.git` | 157,184,000 | yes |
| 48 | `/root/btc-5m-twap/research` | 155,439,104 | yes |
| 49 | `/root/tz01-out-archive` | 155,107,328 | yes |
| 50 | `/root/tz01-out-archive/tz01-out` | 155,103,232 | yes |
| 51 | `/usr/lib/modules/6.8.0-136-generic/kernel` | 154,103,808 | — |
| 52 | `/usr/lib/modules/6.8.0-139-generic/kernel` | 154,005,504 | — |
| 53 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry/burst` | 152,842,240 | — |
| 54 | `/var/cache` | 152,223,744 | — |
| 55 | `/usr/lib/python3` | 147,832,832 | — |
| 56 | `/usr/lib/python3/dist-packages` | 147,828,736 | — |
| 57 | `/usr/src/linux-headers-6.8.0-136` | 133,316,608 | — |
| 58 | `/usr/src/linux-headers-6.8.0-139` | 133,312,512 | — |
| 59 | `/root/.cache` | 118,599,680 | — |
| 60 | `/root/.cache/pip` | 117,706,752 | — |
| 61 | `/usr/libexec` | 115,503,104 | — |
| 62 | `/var/cache/apt` | 114,532,352 | — |
| 63 | `/usr/lib/firmware/nvidia` | 109,867,008 | — |
| 64 | `/usr/share/dict` | 109,350,912 | — |
| 65 | `/usr/lib/snapd` | 109,244,416 | — |
| 66 | `/var/lib/btc-recorder` | 108,896,256 | yes |
| 67 | `/usr/lib/x86_64-linux-gnu/openblas-pthread` | 106,729,472 | — |
| 68 | `/root/my_real_estate_bot/data` | 103,161,856 | — |
| 69 | `/usr/include` | 102,174,720 | — |

### 1.3 M3 — rate inventory, the deciding measurement

| instant | M2 set started | M2 set finished | `df` available |
|---|---|---|---|
| `t0` | 2026-09-13T17:55:36Z | 2026-09-13T17:55:45Z | 6,570,528,768 |
| `t1` | 2026-09-13T18:56:38Z | 2026-09-13T18:56:46Z | 6,566,871,040 |

Window: `3661.756` s start to start. The fall in `df` available is `3,657,728` bytes, which is `86,304,964` bytes/day. The two runs are one command set, asserted.

`1848` directories were measured at both instants. `16` changed, and all of them are listed here in descending order of delta. The other `1832` have a delta of exactly 0 and are in `m3.json`, whose hash Appendix B gives.

| directory | bytes at `t0` | bytes at `t1` | delta | delta, bytes/day |
|---|---|---|---|---|
| `/` | 23,577,714,688 | 23,581,347,840 | 3,633,152 | 85,725,088 |
| `/root` | 10,594,541,568 | 10,596,384,768 | 1,843,200 | 43,490,744 |
| `/var` | 4,205,408,256 | 4,207,194,112 | 1,785,856 | 42,137,698 |
| `/var/lib` | 419,340,288 | 420,753,408 | 1,413,120 | 33,342,903 |
| `/var/lib/btc-recorder` | 108,896,256 | 110,309,376 | 1,413,120 | 33,342,903 |
| `/root/tz09-work` | 1,327,104 | 2,486,272 | 1,159,168 | 27,350,845 |
| `/var/log` | 3,160,764,416 | 3,161,137,152 | 372,736 | 8,794,795 |
| `/root/PROJECT_GAMING_PS5` | 8,471,851,008 | 8,472,199,168 | 348,160 | 8,214,918 |
| `/root/PROJECT_GAMING_PS5/netaudit` | 8,462,696,448 | 8,463,044,608 | 348,160 | 8,214,918 |
| `/root/.claude` | 99,336,192 | 99,667,968 | 331,776 | 7,828,334 |
| `/root/.claude/projects` | 89,407,488 | 89,739,264 | 331,776 | 7,828,334 |
| `/root/PROJECT_GAMING_PS5/netaudit/telemetry` | 8,372,269,056 | 8,372,576,256 | 307,200 | 7,248,457 |
| `/root/PROJECT_GAMING_PS5/netaudit/telemetry/line-monitor` | 294,944,768 | 295,235,584 | 290,816 | 6,861,873 |
| `/root/PROJECT_GAMING_PS5/netaudit/cake-autorate-logs` | 757,760 | 798,720 | 40,960 | 966,461 |
| `/var/log/sysstat` | 6,709,248 | 6,721,536 | 12,288 | 289,938 |
| `/var/log/nginx` | 1,761,280 | 1,765,376 | 4,096 | 96,646 |

**The rule.** Half the fall is `1,828,864.0`. The directories whose delta alone exceeds it are `/`, `/root`. `/` contains every other directory, so the deepest of them is named: **`/root`**.

The five largest deltas below `/`: `/root` `1,843,200`; `/var` `1,785,856`; `/var/lib` `1,413,120`; `/var/lib/btc-recorder` `1,413,120`; `/root/tz09-work` `1,159,168`.

### 1.4 M4 — space held by unlinked open files

| read | `df` used | du `/` total | difference | descriptors | files | size | allocated |
|---|---|---|---|---|---|---|---|
| `t0` | 23,605,805,056 | 23,577,714,688 | 28,090,368 | 2 | 2 | 139,400 | 147,456 |
| `t1` | 23,609,462,784 | 23,581,347,840 | 28,114,944 | 2 | 2 | 139,400 | 147,456 |
| `t2` | 23,976,984,576 | 23,948,869,632 | 28,114,944 | 2 | 2 | 139,400 | 147,456 |

The difference never exceeds `100,000,000` bytes, so M4's enumeration was not required. V5 needs the change in unlinked-open bytes, so it was run anyway. At every read the same two files turned up:

| pid | process | fd | file | size | allocated |
|---|---|---|---|---|---|
| 185836 | `python3` | 15 | `/var/tmp/etilqs_2f82adfec17bfd0e (deleted)` | 69,700 | 73,728 |
| 185836 | `python3` | 16 | `/var/tmp/etilqs_8f0dca1dbf40eff (deleted)` | 69,700 | 73,728 |

Nothing was killed.

### 1.5 M5 — capture accounting

| read | interval directories | holding `quotes.jsonl.gz` | oldest T0 | newest T0 | tree, on disk | tree, apparent | intervals, apparent |
|---|---|---|---|---|---|---|---|
| `t0` | 962 | 385 | `1789033800` | `1789322100` | 108,900,352 | 88,306,419 | 86,448,026 |
| `t1` | 974 | 397 | `1789033800` | `1789325700` | 110,325,760 | 89,441,566 | 87,557,382 |

`du -x -B1 --max-depth=2 /var/lib/btc-recorder/` at `t0`, down to the interval directories:

| directory | bytes |
|---|---|
| `/var/lib/btc-recorder/btc-updown-5m` | 107,020,288 |
| `/var/lib/btc-recorder` | 108,900,352 |

The `962` interval-directory rows sum to `106,979,328`. The smallest is `61,440`, the median `98,304` and the largest `9,846,784`. The three largest are `1789034400` `9,846,784`, `1789322100` `221,184`, `1789209600` `110,592`. Every row is in `t0.json`.

Growth over the M3 window:

| measure | `t0` | `t1` | delta | bytes/day | §6's `23,850,461` | difference |
|---|---|---|---|---|---|---|
| on disk (`du -B1`) | 108,900,352 | 110,325,760 | 1,425,408 | 33,632,842 | 23,850,461 | 9,782,381 |
| apparent size | 88,306,419 | 89,441,566 | 1,135,147 | 26,784,064 | 23,850,461 | 2,933,603 |

The tree includes `runtime.jsonl` and `recorder.log` as well as the interval directories. The on-disk figure counts whole 4,096-byte blocks, and every interval directory holds eight or nine small files.

### 1.6 M6 — compressibility, for the retention decision only

The command, verbatim, from `/root/tz09-work`, at 2026-09-13 22:06 UTC:

```
cd /root/tz09-work && mkdir sample && for t in $(ls /var/lib/btc-recorder/btc-updown-5m | grep -E '^[0-9]+$' | sort -n | head -20); do cp -a "/var/lib/btc-recorder/btc-updown-5m/$t" sample/; done && ls sample | tr '\n' ' ' && echo && tar -C sample -cf - . | zstd -19 -q -c > sample.tar.zst && sleep 3 && python3 -B wt/research/tz09-disk-inventory.py m6 m6 /root/tz09-work/sample /root/tz09-work/sample.tar.zst t1 > m6.md; echo "m6 exit $?"; cat m6.md; rm -rf -- /root/tz09-work/sample /root/tz09-work/sample.tar.zst; echo "rm exit $?"
```

Output: the twenty T0s 1789033800 1789034100 1789034400 1789034700 1789035000 1789035300 1789035600 1789035900 1789036200 1789036500 1789036800 1789037100 1789037400 1789037700 1789038000 1789038300 1789038600 1789038900 1789039200 1789039500, then `m6 exit 0`, the table below, then `rm exit 0`. `zstd` was present at `/usr/bin/zstd`, so `xz` was not used.

The sample holds `161` files. `161` of `161` are byte-identical to their originals by SHA-256, asserted. `0` of the twenty hold `quotes.jsonl.gz`, because all of them predate Tier C. `397` of `974` capture directories held one at `t1`.

| quantity | bytes |
|---|---|
| sample, on disk (`du -B1`) | 11,608,064 |
| sample, apparent | 11,223,282 |
| archive, size | 10,817,073 |
| archive, allocated | 10,817,536 |
| capture intervals at `t1`, on disk | 108,417,024 |
| capture intervals at `t1`, apparent | 87,557,382 |
| projected saving over the whole capture, on disk | 7,383,375 |
| projected saving over the whole capture, apparent | 3,169,001 |

Ratio of archive to sample: `0.931898` on disk, `0.963807` apparent. The projection is the capture's interval bytes times `(1 − ratio)`, rounded down. The streams are already gzipped, so the saving is mostly block rounding and tar overhead. The copy and the archive were deleted, as M6 directs. The originals were read and not written. The mount is `rw,relatime`, so reading may have updated their access times, but not their mtimes. **This authorizes no archiving.**

### 1.7 M7 — log accounting, read-only

`journalctl --disk-usage` at `t0`: `Archived and active journals take up 2.7G in the file system.` At `t1`: `Archived and active journals take up 2.7G in the file system.`

`du -x -B1 --max-depth=2 /var/log` at `t0`:

| directory | bytes |
|---|---|
| `/var/log` | 3,160,764,416 |
| `/var/log/journal` | 3,019,530,240 |
| `/var/log/journal/1c53327a4d7a4405a156a1989a76a001` | 3,002,740,736 |
| `/var/log/journal/96f3acf576df40dc912fbf919ad23c48` | 16,785,408 |
| `/var/log/sysstat` | 6,709,248 |
| `/var/log/nginx` | 1,761,280 |
| `/var/log/apt` | 180,224 |
| `/var/log/unattended-upgrades` | 135,168 |
| `/var/log/letsencrypt` | 86,016 |
| `/var/log/netmon` | 36,864 |
| `/var/log/dist-upgrade` | 4,096 |
| `/var/log/landscape` | 4,096 |
| `/var/log/private` | 4,096 |
| `/var/log/watchdog` | 4,096 |

The ten largest files under `/var/log` at `t0`:

| file | bytes | allocated | mtime |
|---|---|---|---|
| `/var/log/journal/1c53327a4d7a4405a156a1989a76a001/system@5676b75d6ddd44df88a3ad155454f36e-000000000020d81e-000654e5c3187797.journal` | 92,274,688 | 81,002,496 | 2026-06-25T13:38:31Z |
| `/var/log/journal/1c53327a4d7a4405a156a1989a76a001/system@1ef9e550ee264dcc80007c9906c2934c-00000000002790a8-0006575c91bf7b6b.journal` | 75,497,472 | 62,341,120 | 2026-07-29T07:04:05Z |
| `/var/log/journal/1c53327a4d7a4405a156a1989a76a001/system@1ef9e550ee264dcc80007c9906c2934c-00000000002948a7-000657ba8f9f088d.journal` | 75,497,472 | 61,345,792 | 2026-08-02T01:32:53Z |
| `/var/log/journal/1c53327a4d7a4405a156a1989a76a001/system@5676b75d6ddd44df88a3ad155454f36e-00000000001a73d5-00065498ad1928c7.journal` | 75,497,472 | 63,729,664 | 2026-06-20T18:48:11Z |
| `/var/log/journal/1c53327a4d7a4405a156a1989a76a001/system@5676b75d6ddd44df88a3ad155454f36e-00000000001f286d-000654d5e9428808.journal` | 75,497,472 | 61,284,352 | 2026-06-23T06:20:58Z |
| `/var/log/journal/1c53327a4d7a4405a156a1989a76a001/system@d6d05aa2ec0945838cb35ff130891b3c-00000000002e56ed-000658759305862a.journal` | 75,497,472 | 62,423,040 | 2026-08-09T20:46:11Z |
| `/var/log/journal/1c53327a4d7a4405a156a1989a76a001/system@d6d05aa2ec0945838cb35ff130891b3c-00000000002ff1c8-000658a353f1da91.journal` | 75,497,472 | 62,750,720 | 2026-08-12T07:06:59Z |
| `/var/log/journal/1c53327a4d7a4405a156a1989a76a001/system@d6d05aa2ec0945838cb35ff130891b3c-0000000000319307-000658d43bcadc88.journal` | 75,497,472 | 63,397,888 | 2026-08-14T22:16:00Z |
| `/var/log/journal/1c53327a4d7a4405a156a1989a76a001/system@d6d05aa2ec0945838cb35ff130891b3c-0000000000333e7a-000659092a59e54a.journal` | 75,497,472 | 63,660,032 | 2026-08-17T17:47:30Z |
| `/var/log/journal/1c53327a4d7a4405a156a1989a76a001/system@d6d05aa2ec0945838cb35ff130891b3c-000000000034ecfb-00065941c3a4ea61.journal` | 75,497,472 | 64,475,136 | 2026-08-20T13:59:00Z |

Nothing under `/var/log` was deleted, rotated or vacuumed.

### 1.8 Where a measurement contradicts the System Map

Every row below is from revision `2026-09-13-c`. The Architect writes any repair; none is proposed here.

| map row | the map | measured | by how much |
|---|---|---|---|
| §6 total drain | `1,268,154,368` over 30.4 h, `1,001,128,762` bytes/day; `28,495,872` over 48.9 min, `839,142,243` bytes/day | `D` = `86,304,964` bytes/day over `3662` s | `0.086` and `0.103` of the map's figures. Over the supplementary window, `2,775,683,706` bytes/day: `2.77` and `3.31` times them |
| §6 unidentified consumer | about `815,000,000` bytes/day, never identified | M3: `D` minus the capture's on-disk growth is `52,672,122` bytes/day. Supplementary: `/root/PROJECT_GAMING_PS5/netaudit/telemetry/captures` at `2,547,725,419` bytes/day | no rate of that size appears in the M3 window; the supplementary read names it at `3.13` times the map's estimate |
| §6 capture cost | `23,850,461` bytes/day | `33,632,842` on disk, `26,784,064` apparent | `9,782,381` and `2,933,603` bytes/day more |
| §6 disk | free `6,574,706,688` at 2026-09-13 17:06:04 UTC | free `6,570,545,152` at 2026-09-13T17:55:36Z; `14,416,265,216` at run end | `-4,161,536` at run start; `7,841,558,528` at run end, after another party's cleanup |
| §6 headroom | 4.6 to 5.7 days to the floor | `52.96` days at `D` from run-start free space; `1.51` days at the supplementary rate from free space at `t2`; `143.87` at `D` from run-end free space | outside the map's range on every reading |
| §3 scratch paths | `/root/tz01-out-archive/`, `/root/tz06-work/tz06-observations.csv`, `/root/tz07-work/`, `/root/tz07b-work/` and `/root/tz08a-work/` hold what the map says | none of the five exists. The two observation files the map names by hash are now `/root/btc-forensics/tz06-work--tz06-observations.csv` and `/root/btc-forensics/tz08a-work--tz08a-observations.csv` | five paths |
| §6 not yet decided | capture retention policy | fixed by TZ-09 §5, stated in §3 below | — |

## 2. Reclamation — TZ-09 §4

### 2.1 R1 — enumerate

| tree | regular files | bytes | allocated | `du -B1` | non-regular entries | preserved |
|---|---|---|---|---|---|---|
| `/root/tz01-out-archive/` | 51 | 154,998,670 | 155,090,944 | 155,107,328 | 0 | 4 |
| `/root/tz06-work/` | 15 | 2,232,322 | 2,269,184 | 2,273,280 | 0 | 6 |
| `/root/tz07-work/` | 21 | 313,097 | 356,352 | 360,448 | 0 | 2 |
| `/root/tz07b-work/` | 111 | 2,065,906 | 2,301,952 | 2,347,008 | 0 | 41 |
| `/root/tz08a-work/` | 71 | 3,741,250 | 3,891,200 | 3,923,968 | 0 | 38 |
| total | 269 | 163,351,245 | 163,909,632 | 164,012,032 | | 91 |

Every regular file, with its exact size and SHA-256, is listed in Appendix A. R1 ran twice at 2026-09-13 22:07:31 UTC. Both runs were byte-identical: `r1.json` has SHA-256 `3424b043bcd8a562dabeaed88201916bf99f77838d77f5ccb01760fc397c21a9` and `r1-run2.json` matches it.

### 2.2 R2 — preservation by hash

The artifacts searched were `SYSTEM-MAP.md` and the `15` files in `CryptoReports/` on `origin/main` at `c23e18c86b33924979581c25be97c08cc2fbff23`. Each file's lower-case SHA-256 was searched for in each artifact, lower-cased. A second rule ran alongside it, as §6 item 4 explains: a run of at least eight hex characters closed by an ellipsis names the file whose hash it begins. The two paths §4 preserves unconditionally were asserted present.

`91` files are preserved. Naming artifacts are abbreviated: `map` is `SYSTEM-MAP.md`, and `TZ-06` is `CryptoReports/TZ-06-…-report.md`.

| source | bytes | SHA-256 | named by | destination in `/root/btc-forensics/` |
|---|---|---|---|---|
| `/root/tz01-out-archive/tz01-out/twap-divergence-observations.parquet` | 76,810,985 | `0dc121291b897857ff87d9a1f85a3fc29a340d7c62829f2b21cf371d3c380f1e` | TZ-01 | `tz01-out-archive--tz01-out--twap-divergence-observations.parquet` |
| `/root/tz01-out-archive/tz01-out/twap-divergence-summary.md` | 41,445 | `170c4c666e0dcee6c2b2eff51bc8702c6314cbda979cb24edbb89e6252d5b0c6` | TZ-01 | `tz01-out-archive--tz01-out--twap-divergence-summary.md` |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2026-08.parquet` | 3,253,357 | `2570ed2ea4e6c48d687496160522c4eb4b5c27928824a3611bcca35d3a7e914d` | TZ-01 (abbreviated) | `tz01-out-archive--tz01-out--partitions--twap-divergence-2026-08.parquet` |
| `/root/tz01-out-archive/tz01-out/state/coverage.json` | 10,293 | `83de2b2a778a8ba2960b413b12af413af4f405b1966e92ce8de7330f8fc38d13` | TZ-01 | `tz01-out-archive--tz01-out--state--coverage.json` |
| `/root/tz06-work/results-1.json` | 90,457 | `15d0b0cfa699d11c87123807b7d8c979a34a554d8ae7e5f14f13f16172dee48d` | TZ-06 | `tz06-work--results-1.json` |
| `/root/tz06-work/results-2.json` | 90,457 | `15d0b0cfa699d11c87123807b7d8c979a34a554d8ae7e5f14f13f16172dee48d` | TZ-06 | `tz06-work--results-2.json` |
| `/root/tz06-work/tables-1.md` | 33,976 | `6827cd348262d1a4080a7ef75353f539585a6a211b28d7bc96567eb34ef1ebc6` | TZ-06 | `tz06-work--tables-1.md` |
| `/root/tz06-work/tables-2.md` | 33,976 | `6827cd348262d1a4080a7ef75353f539585a6a211b28d7bc96567eb34ef1ebc6` | TZ-06 | `tz06-work--tables-2.md` |
| `/root/tz06-work/tz06-observations-2.csv` | 843,788 | `4e20c4fafbe60fe64c48ce1833a8da55f7fce2c0bad87e93b55ba95a2a4f85bb` | map, TZ-06 | `tz06-work--tz06-observations-2.csv` |
| `/root/tz06-work/tz06-observations.csv` | 843,788 | `4e20c4fafbe60fe64c48ce1833a8da55f7fce2c0bad87e93b55ba95a2a4f85bb` | map, TZ-06; unconditional | `tz06-work--tz06-observations.csv` |
| `/root/tz07-work/run-1.json` | 64,052 | `1aab3a00b2a8617342d53d082e0f75c3c6cd50f17ac47510545715f4f22697e7` | TZ-07a | `tz07-work--run-1.json` |
| `/root/tz07-work/run-2.json` | 64,052 | `1aab3a00b2a8617342d53d082e0f75c3c6cd50f17ac47510545715f4f22697e7` | TZ-07a | `tz07-work--run-2.json` |
| `/root/tz07b-work/results-0.json` | 13,222 | `7f661c78cbeee11eb3cb62e1d9038d2772d7d66c479cc1d75d38077f617a7185` | TZ-07b | `tz07b-work--results-0.json` |
| `/root/tz07b-work/run-1.json` | 13,222 | `7f661c78cbeee11eb3cb62e1d9038d2772d7d66c479cc1d75d38077f617a7185` | TZ-07b | `tz07b-work--run-1.json` |
| `/root/tz07b-work/run-2.json` | 13,222 | `7f661c78cbeee11eb3cb62e1d9038d2772d7d66c479cc1d75d38077f617a7185` | TZ-07b | `tz07b-work--run-2.json` |
| `/root/tz07b-work/wt/.gitignore` | 252 | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | map, TZ-01a, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--.gitignore` |
| `/root/tz07b-work/wt/BTC-EXECUTOR-INSTRUCTIONS.md` | 11,128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | map, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--BTC-EXECUTOR-INSTRUCTIONS.md` |
| `/root/tz07b-work/wt/SYSTEM-MAP.md` | 33,309 | `09f71ca07e1b2329f21bccd1523ed4607b122af5c54a2ba20e83fb3239fb9dac` | TZ-07b | `tz07b-work--wt--SYSTEM-MAP.md` |
| `/root/tz07b-work/wt/CryptoTZ/TZ-07a-variance-time.md` | 14,260 | `0e4852301c493ed7e4cb98d8d880a2c6b42b55f01811976ca9131fc62e61c4e3` | TZ-08, TZ-08a | `tz07b-work--wt--CryptoTZ--TZ-07a-variance-time.md` |
| `/root/tz07b-work/wt/research/pfair.py` | 12,499 | `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` | map, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--research--pfair.py` |
| `/root/tz07b-work/wt/research/selftest-pfair.py` | 15,647 | `97de9782d319c82ee6a7d81ddbd8e00d590d85ffe2daa41abe3d71ae92712c94` | map, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--research--selftest-pfair.py` |
| `/root/tz07b-work/wt/research/selftest-twap-divergence.py` | 16,736 | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | map, TZ-01a, TZ-02, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--research--selftest-twap-divergence.py` |
| `/root/tz07b-work/wt/research/twap-divergence.py` | 50,928 | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | map, TZ-01a, TZ-02, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--research--twap-divergence.py` |
| `/root/tz07b-work/wt/research/tz02-distribution.py` | 14,511 | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | map, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--research--tz02-distribution.py` |
| `/root/tz07b-work/wt/research/tz06-calibration.py` | 26,548 | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` | TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--research--tz06-calibration.py` |
| `/root/tz07b-work/wt/research/tz07a-variance-time.py` | 28,219 | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` | map, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--research--tz07a-variance-time.py` |
| `/root/tz07b-work/wt/research/tz07b-settlement-dispersion.py` | 24,926 | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | map, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--research--tz07b-settlement-dispersion.py` |
| `/root/tz07b-work/wt/research/recorder/analyze.py` | 34,705 | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--research--recorder--analyze.py` |
| `/root/tz07b-work/wt/research/recorder/config.py` | 4,773 | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--research--recorder--config.py` |
| `/root/tz07b-work/wt/research/recorder/manifest.py` | 10,002 | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--research--recorder--manifest.py` |
| `/root/tz07b-work/wt/research/recorder/probe.py` | 9,324 | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | map, TZ-04b, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--research--recorder--probe.py` |
| `/root/tz07b-work/wt/research/recorder/recorder.py` | 25,658 | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--research--recorder--recorder.py` |
| `/root/tz07b-work/wt/research/recorder/selftest.py` | 30,591 | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt--research--recorder--selftest.py` |
| `/root/tz07b-work/wt-report/.gitignore` | 252 | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | map, TZ-01a, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--.gitignore` |
| `/root/tz07b-work/wt-report/BTC-EXECUTOR-INSTRUCTIONS.md` | 11,128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | map, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--BTC-EXECUTOR-INSTRUCTIONS.md` |
| `/root/tz07b-work/wt-report/SYSTEM-MAP.md` | 40,605 | `00bf58174de8bd83de4d2be31b531b1273ba716d2b510cba664f4780d8db52b8` | TZ-08, TZ-08a | `tz07b-work--wt-report--SYSTEM-MAP.md` |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-07a-variance-time.md` | 14,260 | `0e4852301c493ed7e4cb98d8d880a2c6b42b55f01811976ca9131fc62e61c4e3` | TZ-08, TZ-08a | `tz07b-work--wt-report--CryptoTZ--TZ-07a-variance-time.md` |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-08-out-of-sample.md` | 14,465 | `bacb45ec2c0a3ed824972fe0b536a99f5ef3bad68e78a5c07fbf0c1a09d77d00` | TZ-08 | `tz07b-work--wt-report--CryptoTZ--TZ-08-out-of-sample.md` |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-08a-out-of-sample.md` | 17,231 | `3c6ea77fabe9716b6bde98cdba728b67cb62a14f8172ac59bffd47dd04f5e687` | TZ-08a | `tz07b-work--wt-report--CryptoTZ--TZ-08a-out-of-sample.md` |
| `/root/tz07b-work/wt-report/research/pfair.py` | 12,499 | `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` | map, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--research--pfair.py` |
| `/root/tz07b-work/wt-report/research/selftest-pfair.py` | 15,647 | `97de9782d319c82ee6a7d81ddbd8e00d590d85ffe2daa41abe3d71ae92712c94` | map, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--research--selftest-pfair.py` |
| `/root/tz07b-work/wt-report/research/selftest-twap-divergence.py` | 16,736 | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | map, TZ-01a, TZ-02, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--research--selftest-twap-divergence.py` |
| `/root/tz07b-work/wt-report/research/twap-divergence.py` | 50,928 | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | map, TZ-01a, TZ-02, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--research--twap-divergence.py` |
| `/root/tz07b-work/wt-report/research/tz02-distribution.py` | 14,511 | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | map, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--research--tz02-distribution.py` |
| `/root/tz07b-work/wt-report/research/tz06-calibration.py` | 26,548 | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` | TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--research--tz06-calibration.py` |
| `/root/tz07b-work/wt-report/research/tz07a-variance-time.py` | 28,219 | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` | map, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--research--tz07a-variance-time.py` |
| `/root/tz07b-work/wt-report/research/tz07b-settlement-dispersion.py` | 24,926 | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | map, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--research--tz07b-settlement-dispersion.py` |
| `/root/tz07b-work/wt-report/research/recorder/analyze.py` | 34,705 | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--research--recorder--analyze.py` |
| `/root/tz07b-work/wt-report/research/recorder/config.py` | 4,773 | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--research--recorder--config.py` |
| `/root/tz07b-work/wt-report/research/recorder/manifest.py` | 10,002 | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--research--recorder--manifest.py` |
| `/root/tz07b-work/wt-report/research/recorder/probe.py` | 9,324 | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | map, TZ-04b, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--research--recorder--probe.py` |
| `/root/tz07b-work/wt-report/research/recorder/recorder.py` | 25,658 | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--research--recorder--recorder.py` |
| `/root/tz07b-work/wt-report/research/recorder/selftest.py` | 30,591 | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz07b-work--wt-report--research--recorder--selftest.py` |
| `/root/tz08a-work/probe-g3.json` | 9,560 | `6a1cb899c3b1b372c00dedf66d2ad14fb253930e6f2b801a6ca1dbca66810d6f` | TZ-08a | `tz08a-work--probe-g3.json` |
| `/root/tz08a-work/probe-g3.py` | 3,746 | `2a311b7774432ba075a96cf2b66b9c38b5db1cee4a22d1e2e8c8880b0a14de2a` | TZ-08a | `tz08a-work--probe-g3.py` |
| `/root/tz08a-work/tz08a-observations.csv` | 1,066,357 | `b810b07165e98b29258479323a0c634ccaea1917135a3336b8d28fb4bb92fa77` | map, TZ-08a; unconditional | `tz08a-work--tz08a-observations.csv` |
| `/root/tz08a-work/tz08a-results.json` | 105,047 | `b2addb77eca57ef2d915737ab3a6a0295ff797461920cc1b046b8a318d2e8b6c` | TZ-08a | `tz08a-work--tz08a-results.json` |
| `/root/tz08a-work/tz08a-tables.md` | 42,801 | `1f3b7b9ec63de6a7ac68522924e9bc0b24604b55163ba57f4134c7f45fd81565` | TZ-08a | `tz08a-work--tz08a-tables.md` |
| `/root/tz08a-work/run2/tz08a-observations.csv` | 1,066,357 | `b810b07165e98b29258479323a0c634ccaea1917135a3336b8d28fb4bb92fa77` | map, TZ-08a | `tz08a-work--run2--tz08a-observations.csv` |
| `/root/tz08a-work/run2/tz08a-results.json` | 105,047 | `b2addb77eca57ef2d915737ab3a6a0295ff797461920cc1b046b8a318d2e8b6c` | TZ-08a | `tz08a-work--run2--tz08a-results.json` |
| `/root/tz08a-work/run2/tz08a-tables.md` | 42,801 | `1f3b7b9ec63de6a7ac68522924e9bc0b24604b55163ba57f4134c7f45fd81565` | TZ-08a | `tz08a-work--run2--tz08a-tables.md` |
| `/root/tz08a-work/src/BTC-EXECUTOR-INSTRUCTIONS.md` | 11,128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | map, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz08a-work--src--BTC-EXECUTOR-INSTRUCTIONS.md` |
| `/root/tz08a-work/src/SYSTEM-MAP.md` | 40,605 | `00bf58174de8bd83de4d2be31b531b1273ba716d2b510cba664f4780d8db52b8` | TZ-08, TZ-08a | `tz08a-work--src--SYSTEM-MAP.md` |
| `/root/tz08a-work/src/TZ-07a-variance-time.md` | 14,260 | `0e4852301c493ed7e4cb98d8d880a2c6b42b55f01811976ca9131fc62e61c4e3` | TZ-08, TZ-08a | `tz08a-work--src--TZ-07a-variance-time.md` |
| `/root/tz08a-work/src/TZ-08-out-of-sample.md` | 14,465 | `bacb45ec2c0a3ed824972fe0b536a99f5ef3bad68e78a5c07fbf0c1a09d77d00` | TZ-08 | `tz08a-work--src--TZ-08-out-of-sample.md` |
| `/root/tz08a-work/src/TZ-08a-out-of-sample.md` | 17,231 | `3c6ea77fabe9716b6bde98cdba728b67cb62a14f8172ac59bffd47dd04f5e687` | TZ-08a | `tz08a-work--src--TZ-08a-out-of-sample.md` |
| `/root/tz08a-work/src/pfair.py` | 12,499 | `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` | map, TZ-07b, TZ-08, TZ-08a | `tz08a-work--src--pfair.py` |
| `/root/tz08a-work/src/tz06-calibration.py` | 26,548 | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` | TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz08a-work--src--tz06-calibration.py` |
| `/root/tz08a-work/src/tz07a-variance-time.py` | 28,219 | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` | map, TZ-07b, TZ-08, TZ-08a | `tz08a-work--src--tz07a-variance-time.py` |
| `/root/tz08a-work/src/tz07b-settlement-dispersion.py` | 24,926 | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | map, TZ-07b, TZ-08, TZ-08a | `tz08a-work--src--tz07b-settlement-dispersion.py` |
| `/root/tz08a-work/wt/.gitignore` | 252 | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | map, TZ-01a, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--.gitignore` |
| `/root/tz08a-work/wt/BTC-EXECUTOR-INSTRUCTIONS.md` | 11,128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | map, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--BTC-EXECUTOR-INSTRUCTIONS.md` |
| `/root/tz08a-work/wt/SYSTEM-MAP.md` | 40,605 | `00bf58174de8bd83de4d2be31b531b1273ba716d2b510cba664f4780d8db52b8` | TZ-08, TZ-08a | `tz08a-work--wt--SYSTEM-MAP.md` |
| `/root/tz08a-work/wt/CryptoTZ/TZ-07a-variance-time.md` | 14,260 | `0e4852301c493ed7e4cb98d8d880a2c6b42b55f01811976ca9131fc62e61c4e3` | TZ-08, TZ-08a | `tz08a-work--wt--CryptoTZ--TZ-07a-variance-time.md` |
| `/root/tz08a-work/wt/CryptoTZ/TZ-08-out-of-sample.md` | 14,465 | `bacb45ec2c0a3ed824972fe0b536a99f5ef3bad68e78a5c07fbf0c1a09d77d00` | TZ-08 | `tz08a-work--wt--CryptoTZ--TZ-08-out-of-sample.md` |
| `/root/tz08a-work/wt/CryptoTZ/TZ-08a-out-of-sample.md` | 17,231 | `3c6ea77fabe9716b6bde98cdba728b67cb62a14f8172ac59bffd47dd04f5e687` | TZ-08a | `tz08a-work--wt--CryptoTZ--TZ-08a-out-of-sample.md` |
| `/root/tz08a-work/wt/research/pfair.py` | 12,499 | `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` | map, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--research--pfair.py` |
| `/root/tz08a-work/wt/research/selftest-pfair.py` | 15,647 | `97de9782d319c82ee6a7d81ddbd8e00d590d85ffe2daa41abe3d71ae92712c94` | map, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--research--selftest-pfair.py` |
| `/root/tz08a-work/wt/research/selftest-twap-divergence.py` | 16,736 | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | map, TZ-01a, TZ-02, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--research--selftest-twap-divergence.py` |
| `/root/tz08a-work/wt/research/twap-divergence.py` | 50,928 | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | map, TZ-01a, TZ-02, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--research--twap-divergence.py` |
| `/root/tz08a-work/wt/research/tz02-distribution.py` | 14,511 | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | map, TZ-03, TZ-04, TZ-04a, TZ-04b, TZ-05, TZ-05a, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--research--tz02-distribution.py` |
| `/root/tz08a-work/wt/research/tz06-calibration.py` | 27,138 | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | map, TZ-08a | `tz08a-work--wt--research--tz06-calibration.py` |
| `/root/tz08a-work/wt/research/tz07a-variance-time.py` | 28,219 | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` | map, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--research--tz07a-variance-time.py` |
| `/root/tz08a-work/wt/research/tz07b-settlement-dispersion.py` | 24,926 | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | map, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--research--tz07b-settlement-dispersion.py` |
| `/root/tz08a-work/wt/research/tz08a-out-of-sample.py` | 38,822 | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | map, TZ-08a | `tz08a-work--wt--research--tz08a-out-of-sample.py` |
| `/root/tz08a-work/wt/research/recorder/analyze.py` | 34,705 | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--research--recorder--analyze.py` |
| `/root/tz08a-work/wt/research/recorder/config.py` | 4,773 | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--research--recorder--config.py` |
| `/root/tz08a-work/wt/research/recorder/manifest.py` | 10,002 | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--research--recorder--manifest.py` |
| `/root/tz08a-work/wt/research/recorder/probe.py` | 9,324 | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | map, TZ-04b, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--research--recorder--probe.py` |
| `/root/tz08a-work/wt/research/recorder/recorder.py` | 25,658 | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--research--recorder--recorder.py` |
| `/root/tz08a-work/wt/research/recorder/selftest.py` | 30,591 | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | map, TZ-06, TZ-07, TZ-07a, TZ-07b, TZ-08, TZ-08a | `tz08a-work--wt--research--recorder--selftest.py` |

### 2.3 R3 — consolidate

The command, verbatim, from `/root/tz09-work`, at 2026-09-13 22:08:08 UTC:

```
mkdir /root/btc-forensics && while IFS=$'\t' read -r src dst; do cp -v --no-clobber --preserve=mode,timestamps -- "$src" "$dst"; done < /root/tz09-work/r1-plan.tsv > r3-cp.log 2>&1
```

It exited 0. Its output, `r3-cp.log`, is `182` lines: one `cp -v` line per file and one portability warning per file about `-n`.

<details><summary>r3-cp.log, verbatim</summary>

```
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz01-out-archive/tz01-out/twap-divergence-observations.parquet' -> '/root/btc-forensics/tz01-out-archive--tz01-out--twap-divergence-observations.parquet'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz01-out-archive/tz01-out/twap-divergence-summary.md' -> '/root/btc-forensics/tz01-out-archive--tz01-out--twap-divergence-summary.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2026-08.parquet' -> '/root/btc-forensics/tz01-out-archive--tz01-out--partitions--twap-divergence-2026-08.parquet'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz01-out-archive/tz01-out/state/coverage.json' -> '/root/btc-forensics/tz01-out-archive--tz01-out--state--coverage.json'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz06-work/results-1.json' -> '/root/btc-forensics/tz06-work--results-1.json'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz06-work/results-2.json' -> '/root/btc-forensics/tz06-work--results-2.json'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz06-work/tables-1.md' -> '/root/btc-forensics/tz06-work--tables-1.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz06-work/tables-2.md' -> '/root/btc-forensics/tz06-work--tables-2.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz06-work/tz06-observations-2.csv' -> '/root/btc-forensics/tz06-work--tz06-observations-2.csv'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz06-work/tz06-observations.csv' -> '/root/btc-forensics/tz06-work--tz06-observations.csv'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07-work/run-1.json' -> '/root/btc-forensics/tz07-work--run-1.json'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07-work/run-2.json' -> '/root/btc-forensics/tz07-work--run-2.json'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/results-0.json' -> '/root/btc-forensics/tz07b-work--results-0.json'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/run-1.json' -> '/root/btc-forensics/tz07b-work--run-1.json'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/run-2.json' -> '/root/btc-forensics/tz07b-work--run-2.json'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/.gitignore' -> '/root/btc-forensics/tz07b-work--wt--.gitignore'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/BTC-EXECUTOR-INSTRUCTIONS.md' -> '/root/btc-forensics/tz07b-work--wt--BTC-EXECUTOR-INSTRUCTIONS.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/SYSTEM-MAP.md' -> '/root/btc-forensics/tz07b-work--wt--SYSTEM-MAP.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/CryptoTZ/TZ-07a-variance-time.md' -> '/root/btc-forensics/tz07b-work--wt--CryptoTZ--TZ-07a-variance-time.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/research/pfair.py' -> '/root/btc-forensics/tz07b-work--wt--research--pfair.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/research/selftest-pfair.py' -> '/root/btc-forensics/tz07b-work--wt--research--selftest-pfair.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/research/selftest-twap-divergence.py' -> '/root/btc-forensics/tz07b-work--wt--research--selftest-twap-divergence.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/research/twap-divergence.py' -> '/root/btc-forensics/tz07b-work--wt--research--twap-divergence.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/research/tz02-distribution.py' -> '/root/btc-forensics/tz07b-work--wt--research--tz02-distribution.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/research/tz06-calibration.py' -> '/root/btc-forensics/tz07b-work--wt--research--tz06-calibration.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/research/tz07a-variance-time.py' -> '/root/btc-forensics/tz07b-work--wt--research--tz07a-variance-time.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/research/tz07b-settlement-dispersion.py' -> '/root/btc-forensics/tz07b-work--wt--research--tz07b-settlement-dispersion.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/research/recorder/analyze.py' -> '/root/btc-forensics/tz07b-work--wt--research--recorder--analyze.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/research/recorder/config.py' -> '/root/btc-forensics/tz07b-work--wt--research--recorder--config.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/research/recorder/manifest.py' -> '/root/btc-forensics/tz07b-work--wt--research--recorder--manifest.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/research/recorder/probe.py' -> '/root/btc-forensics/tz07b-work--wt--research--recorder--probe.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/research/recorder/recorder.py' -> '/root/btc-forensics/tz07b-work--wt--research--recorder--recorder.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt/research/recorder/selftest.py' -> '/root/btc-forensics/tz07b-work--wt--research--recorder--selftest.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/.gitignore' -> '/root/btc-forensics/tz07b-work--wt-report--.gitignore'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/BTC-EXECUTOR-INSTRUCTIONS.md' -> '/root/btc-forensics/tz07b-work--wt-report--BTC-EXECUTOR-INSTRUCTIONS.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/SYSTEM-MAP.md' -> '/root/btc-forensics/tz07b-work--wt-report--SYSTEM-MAP.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/CryptoTZ/TZ-07a-variance-time.md' -> '/root/btc-forensics/tz07b-work--wt-report--CryptoTZ--TZ-07a-variance-time.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/CryptoTZ/TZ-08-out-of-sample.md' -> '/root/btc-forensics/tz07b-work--wt-report--CryptoTZ--TZ-08-out-of-sample.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/CryptoTZ/TZ-08a-out-of-sample.md' -> '/root/btc-forensics/tz07b-work--wt-report--CryptoTZ--TZ-08a-out-of-sample.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/research/pfair.py' -> '/root/btc-forensics/tz07b-work--wt-report--research--pfair.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/research/selftest-pfair.py' -> '/root/btc-forensics/tz07b-work--wt-report--research--selftest-pfair.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/research/selftest-twap-divergence.py' -> '/root/btc-forensics/tz07b-work--wt-report--research--selftest-twap-divergence.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/research/twap-divergence.py' -> '/root/btc-forensics/tz07b-work--wt-report--research--twap-divergence.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/research/tz02-distribution.py' -> '/root/btc-forensics/tz07b-work--wt-report--research--tz02-distribution.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/research/tz06-calibration.py' -> '/root/btc-forensics/tz07b-work--wt-report--research--tz06-calibration.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/research/tz07a-variance-time.py' -> '/root/btc-forensics/tz07b-work--wt-report--research--tz07a-variance-time.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/research/tz07b-settlement-dispersion.py' -> '/root/btc-forensics/tz07b-work--wt-report--research--tz07b-settlement-dispersion.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/research/recorder/analyze.py' -> '/root/btc-forensics/tz07b-work--wt-report--research--recorder--analyze.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/research/recorder/config.py' -> '/root/btc-forensics/tz07b-work--wt-report--research--recorder--config.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/research/recorder/manifest.py' -> '/root/btc-forensics/tz07b-work--wt-report--research--recorder--manifest.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/research/recorder/probe.py' -> '/root/btc-forensics/tz07b-work--wt-report--research--recorder--probe.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/research/recorder/recorder.py' -> '/root/btc-forensics/tz07b-work--wt-report--research--recorder--recorder.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz07b-work/wt-report/research/recorder/selftest.py' -> '/root/btc-forensics/tz07b-work--wt-report--research--recorder--selftest.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/probe-g3.json' -> '/root/btc-forensics/tz08a-work--probe-g3.json'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/probe-g3.py' -> '/root/btc-forensics/tz08a-work--probe-g3.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/tz08a-observations.csv' -> '/root/btc-forensics/tz08a-work--tz08a-observations.csv'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/tz08a-results.json' -> '/root/btc-forensics/tz08a-work--tz08a-results.json'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/tz08a-tables.md' -> '/root/btc-forensics/tz08a-work--tz08a-tables.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/run2/tz08a-observations.csv' -> '/root/btc-forensics/tz08a-work--run2--tz08a-observations.csv'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/run2/tz08a-results.json' -> '/root/btc-forensics/tz08a-work--run2--tz08a-results.json'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/run2/tz08a-tables.md' -> '/root/btc-forensics/tz08a-work--run2--tz08a-tables.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/src/BTC-EXECUTOR-INSTRUCTIONS.md' -> '/root/btc-forensics/tz08a-work--src--BTC-EXECUTOR-INSTRUCTIONS.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/src/SYSTEM-MAP.md' -> '/root/btc-forensics/tz08a-work--src--SYSTEM-MAP.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/src/TZ-07a-variance-time.md' -> '/root/btc-forensics/tz08a-work--src--TZ-07a-variance-time.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/src/TZ-08-out-of-sample.md' -> '/root/btc-forensics/tz08a-work--src--TZ-08-out-of-sample.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/src/TZ-08a-out-of-sample.md' -> '/root/btc-forensics/tz08a-work--src--TZ-08a-out-of-sample.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/src/pfair.py' -> '/root/btc-forensics/tz08a-work--src--pfair.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/src/tz06-calibration.py' -> '/root/btc-forensics/tz08a-work--src--tz06-calibration.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/src/tz07a-variance-time.py' -> '/root/btc-forensics/tz08a-work--src--tz07a-variance-time.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/src/tz07b-settlement-dispersion.py' -> '/root/btc-forensics/tz08a-work--src--tz07b-settlement-dispersion.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/.gitignore' -> '/root/btc-forensics/tz08a-work--wt--.gitignore'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/BTC-EXECUTOR-INSTRUCTIONS.md' -> '/root/btc-forensics/tz08a-work--wt--BTC-EXECUTOR-INSTRUCTIONS.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/SYSTEM-MAP.md' -> '/root/btc-forensics/tz08a-work--wt--SYSTEM-MAP.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/CryptoTZ/TZ-07a-variance-time.md' -> '/root/btc-forensics/tz08a-work--wt--CryptoTZ--TZ-07a-variance-time.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/CryptoTZ/TZ-08-out-of-sample.md' -> '/root/btc-forensics/tz08a-work--wt--CryptoTZ--TZ-08-out-of-sample.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/CryptoTZ/TZ-08a-out-of-sample.md' -> '/root/btc-forensics/tz08a-work--wt--CryptoTZ--TZ-08a-out-of-sample.md'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/pfair.py' -> '/root/btc-forensics/tz08a-work--wt--research--pfair.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/selftest-pfair.py' -> '/root/btc-forensics/tz08a-work--wt--research--selftest-pfair.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/selftest-twap-divergence.py' -> '/root/btc-forensics/tz08a-work--wt--research--selftest-twap-divergence.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/twap-divergence.py' -> '/root/btc-forensics/tz08a-work--wt--research--twap-divergence.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/tz02-distribution.py' -> '/root/btc-forensics/tz08a-work--wt--research--tz02-distribution.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/tz06-calibration.py' -> '/root/btc-forensics/tz08a-work--wt--research--tz06-calibration.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/tz07a-variance-time.py' -> '/root/btc-forensics/tz08a-work--wt--research--tz07a-variance-time.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/tz07b-settlement-dispersion.py' -> '/root/btc-forensics/tz08a-work--wt--research--tz07b-settlement-dispersion.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/tz08a-out-of-sample.py' -> '/root/btc-forensics/tz08a-work--wt--research--tz08a-out-of-sample.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/recorder/analyze.py' -> '/root/btc-forensics/tz08a-work--wt--research--recorder--analyze.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/recorder/config.py' -> '/root/btc-forensics/tz08a-work--wt--research--recorder--config.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/recorder/manifest.py' -> '/root/btc-forensics/tz08a-work--wt--research--recorder--manifest.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/recorder/probe.py' -> '/root/btc-forensics/tz08a-work--wt--research--recorder--probe.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/recorder/recorder.py' -> '/root/btc-forensics/tz08a-work--wt--research--recorder--recorder.py'
cp: warning: behavior of -n is non-portable and may change in future; use --update=none instead
'/root/tz08a-work/wt/research/recorder/selftest.py' -> '/root/btc-forensics/tz08a-work--wt--research--recorder--selftest.py'
```
</details>

The destination name is `<source-directory-name>--<filename>`. For a nested file, the source-directory name is its directory relative to `/root`, with every `/` replaced by `--`. Destination names were asserted unique before any copy was made. V6 recomputed every SHA-256 at both ends: **91 of 91 equal**, and `/root/btc-forensics/` holds exactly the `91` planned entries.

### 2.4 R4 — delete

The Executor's command was refused by the session's permission classifier before it ran, and nothing was deleted then (§6 item 1). The Boss then ran the block below as a routing action, at 2026-09-13 23:56:45 UTC. `r4.log` is its `set -x` trace and output, verbatim:

```
+ S='python3 -B /root/tz09-work/wt/research/tz09-disk-inventory.py'
+ python3 -B /root/tz09-work/wt/research/tz09-disk-inventory.py state before-r4
state `before-r4` at 2026-09-13T23:56:45Z: recorder [228592], start sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`, 1034 interval directories, newest T0 `1789343700`; available `14,251,536,384`
+ du -x -B1 -s /root/tz01-out-archive
155107328	/root/tz01-out-archive
+ du -x -B1 -s --apparent-size /root/tz01-out-archive
154998670	/root/tz01-out-archive
+ rm -rf -- /root/tz01-out-archive/
+ python3 -B /root/tz09-work/wt/research/tz09-disk-inventory.py df df-r4-1
df `df-r4-1` at 2026-09-13T23:56:45Z: used `15,769,694,208`, available `14,406,639,616`
+ du -x -B1 -s /root/tz06-work
2273280	/root/tz06-work
+ du -x -B1 -s --apparent-size /root/tz06-work
2232322	/root/tz06-work
+ rm -rf -- /root/tz06-work/
+ python3 -B /root/tz09-work/wt/research/tz09-disk-inventory.py df df-r4-2
df `df-r4-2` at 2026-09-13T23:56:45Z: used `15,767,425,024`, available `14,408,908,800`
+ du -x -B1 -s /root/tz07-work
360448	/root/tz07-work
+ du -x -B1 -s --apparent-size /root/tz07-work
313097	/root/tz07-work
+ rm -rf -- /root/tz07-work/
+ python3 -B /root/tz09-work/wt/research/tz09-disk-inventory.py df df-r4-3
df `df-r4-3` at 2026-09-13T23:56:45Z: used `15,767,068,672`, available `14,409,265,152`
+ du -x -B1 -s /root/tz07b-work
2347008	/root/tz07b-work
+ du -x -B1 -s --apparent-size /root/tz07b-work
2065906	/root/tz07b-work
+ rm -rf -- /root/tz07b-work/
+ python3 -B /root/tz09-work/wt/research/tz09-disk-inventory.py df df-r4-4
df `df-r4-4` at 2026-09-13T23:56:45Z: used `15,764,725,760`, available `14,411,608,064`
+ du -x -B1 -s /root/tz08a-work
3923968	/root/tz08a-work
+ du -x -B1 -s --apparent-size /root/tz08a-work
3741250	/root/tz08a-work
+ rm -rf -- /root/tz08a-work/
+ python3 -B /root/tz09-work/wt/research/tz09-disk-inventory.py df df-r4-5
df `df-r4-5` at 2026-09-13T23:56:45Z: used `15,760,805,888`, available `14,415,527,936`
+ python3 -B /root/tz09-work/wt/research/tz09-disk-inventory.py state after-r4
state `after-r4` at 2026-09-13T23:56:45Z: recorder [228592], start sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`, 1034 interval directories, newest T0 `1789343700`; available `14,415,523,840`
+ python3 -B /root/tz09-work/wt/research/tz09-disk-inventory.py r5 r5 before-r4 after-r4
R5: available `14,251,536,384` at 2026-09-13T23:56:45Z → `14,415,523,840` at 2026-09-13T23:56:45Z; difference `163,987,456` bytes
R5: not negative, asserted
+ python3 -B /root/tz09-work/wt/research/tz09-disk-inventory.py v7 v7 before-r4 after-r4
V7: pid 228592 (start tick 355131283) → 228592 (start tick 355131283); interval directories 1034 → 1034
V7: 2 of 2
```

The Executor then verified the result from `r4.log`, the JSON each read wrote, `df`, `ps` and `test -e`:

| # | tree | `du -B1` before | apparent before | `df` available after | change from the previous read |
|---|---|---|---|---|---|
| R4.1 | `/root/tz01-out-archive/` | 155,107,328 | 154,998,670 | 14,406,639,616 | 155,103,232 |
| R4.2 | `/root/tz06-work/` | 2,273,280 | 2,232,322 | 14,408,908,800 | 2,269,184 |
| R4.3 | `/root/tz07-work/` | 360,448 | 313,097 | 14,409,265,152 | 356,352 |
| R4.4 | `/root/tz07b-work/` | 2,347,008 | 2,065,906 | 14,411,608,064 | 2,342,912 |
| R4.5 | `/root/tz08a-work/` | 3,923,968 | 3,741,250 | 14,415,527,936 | 3,919,872 |

The `du` figures come from R1 and equal the log's byte for byte. Each tree was absent afterwards, checked at 2026-09-14 00:01:51 UTC.

### 2.5 R5 — account for it

Free space immediately before R4 was `14,251,536,384` at 2026-09-13T23:56:45Z. Immediately after, it was `14,415,523,840` at 2026-09-13T23:56:45Z. The difference is **`163,987,456` bytes**, asserted not negative. The sum of the five trees' `du` figures is `164,012,032`.

## 3. The retention rule — TZ-09 §5

§5 fixes the rule. This report restates it and gives the numbers it requires.

1. **The capture is never deleted.** No interval directory under `/var/lib/btc-recorder/` is removed, truncated or rewritten, by any TZ, any script or any scheduled job. This run touched none: V7 and V8.
2. **Archiving, if it is ever done, is its own TZ and is reversible.** It compresses only intervals older than the oldest member of any set a committed report scores. It verifies every member file by SHA-256 after extraction, before any original is removed. M6's measured saving is `7,383,375` bytes on disk over the capture as it stood at `t1`, at ratio `0.931898`.
3. **Scratch retention.** A TZ's `/root/tz<NN>-work/` is reclaimed by the next TZ that runs after that TZ's report is on `main`, except files whose SHA-256 a committed artifact names; those live in `/root/btc-forensics/`. **The standing rule applied to this TZ:** this report names by hash exactly the files in Appendix B. Every other file under `/root/tz09-work/` is reclaimable the moment this report is committed, and so is `/root/tz09-work/wt`, the implementation worktree, once PR #10 is decided.
4. **The floor and the alarm.** `F` = `2,000,000,000` bytes. `D` = `86,304,964` bytes/day, the fall in `df` available over M3's window scaled to a day. `A` = `F + 3 × D` = `2,258,914,892` bytes. Free space at run end is `14,416,265,216`, which is `12,157,350,324` above `A`. Days to `F` at `D` are `143.87`. At the supplementary rate, `2,775,683,706` bytes/day, `A` would be `10,327,051,118` bytes. That figure is reported, not adopted.

## 4. Validation — TZ-09 §7

### V1 — gates

**Host gate, 3 of 3, asserted in `cmd_gate`, at 2026-09-13T17:55:36Z:**

- H1 capture directory holds interval directories: **True**
- H2 recorder running, newest start record carries the sha: **True**
- H3 filesystem is the device, at its total: **True**

The observed values: `/var/lib/btc-recorder/btc-updown-5m/` held `962` interval directories, the newest T0 `1789322100`. One recorder process was running, pid `228592`, cwd `/root/btc-5m-twap/research/recorder`. The newest start record is `recv_ns 1789206785264516934` with sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`. The filesystem is `/dev/vda2`, total `31,612,203,008`.

**Resource gate, asserted in `df_read` on every read.** Free space at run start was `6,570,545,152`, against the `2,000,000,000` floor. Every one of the `17` script reads was at or above `3,000,000,000`. The lowest script read was `6,199,312,384` at 2026-09-13T22:07:26Z, in `t2.json`. The lowest shell read was `6,102,839,296` at 2026-09-13 22:09:53 UTC.

**Fingerprint gate.** The map's revision string `2026-09-13-c` equals the TZ's. All six anchors are equal to the TZ header, asserted, and the four hashed ones equal the SHA-256 prefix of the artifact they name:

| anchor | map | TZ-09 | the named file's SHA-256, first 12 |
|---|---|---|---|
| `A1` | `229a944f2d51` | `229a944f2d51` | compared as a string |
| `A2` | `6c5089330629` | `6c5089330629` | `6c5089330629` (research/twap-divergence.py) |
| `A3` | `0-complete / 1-answered-no / 2-not-started` | `0-complete / 1-answered-no / 2-not-started` | compared as a string |
| `A4` | `437b45ea196b` | `437b45ea196b` | `437b45ea196b` (BTC-EXECUTOR-INSTRUCTIONS.md) |
| `A5` | `9fd1c7de0f74` | `9fd1c7de0f74` | `9fd1c7de0f74` (research/recorder/recorder.py) |
| `A6` | `cb72abb8dd8a` | `cb72abb8dd8a` | `cb72abb8dd8a` (research/pfair.py) |

### V2 — the committed script cannot delete

Read in the shell, on the committed file at `e45f38e`:

```
$ grep -nE 'os\.remove|os\.unlink|os\.rmdir|shutil\.rmtree|shutil\.move|os\.truncate|os\.rename' research/tz09-disk-inventory.py
(exit 1)
$ grep -n 'open(' research/tz09-disk-inventory.py
160:    with open(path, "w") as fh:
169:    with open(os.path.join(WORK, name + ".json"), "rb") as fh:
184:    with open(path, "rb") as fh:
254:            with open(f"/proc/{pid}/cmdline", "rb") as fh:
256:            with open(f"/proc/{pid}/stat", "rb") as fh:
264:    with open(RUNTIME, "rb") as fh:
274:def deleted_open(root_dev):
281:            with open(f"/proc/{pid}/comm", "rb") as fh:
447:    out["m4"] = deleted_open(os.stat("/").st_dev)
```

The first grep prints nothing: 0 of 7 names occur. Of the `open(` hits, lines 274 and 447 are `deleted_open`, a function name, and the other seven are real calls. Six open for reading (`"rb"`). The one `open(..., "w")`, line 160, is inside `write_out`. Its target is `os.path.realpath(os.path.join(WORK, name))`, and the line before it asserts that the target starts with `/root/tz09-work/`.

### V3 — inventory stability

M2 was re-run immediately after `t0`, as `t0b`, finishing at 2026-09-13T17:55:54Z. The ordering of every directory at or above `100,000,000` bytes is unchanged: **69 of 69**, asserted.

<details><summary>Both orderings</summary>

| # | `t0` | bytes | `t0b` | bytes |
|---|---|---|---|---|
| 1 | `/` | 23,577,714,688 | `/` | 23,578,095,616 |
| 2 | `/root` | 10,594,541,568 | `/root` | 10,594,914,304 |
| 3 | `/root/PROJECT_GAMING_PS5` | 8,471,851,008 | `/root/PROJECT_GAMING_PS5` | 8,471,855,104 |
| 4 | `/root/PROJECT_GAMING_PS5/netaudit` | 8,462,696,448 | `/root/PROJECT_GAMING_PS5/netaudit` | 8,462,700,544 |
| 5 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry` | 8,372,269,056 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry` | 8,372,269,056 |
| 6 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry/captures` | 6,896,218,112 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry/captures` | 6,896,218,112 |
| 7 | `/usr` | 4,588,097,536 | `/usr` | 4,588,097,536 |
| 8 | `/var` | 4,205,408,256 | `/var` | 4,205,412,352 |
| 9 | `/var/log` | 3,160,764,416 | `/var/log` | 3,160,764,416 |
| 10 | `/var/log/journal` | 3,019,530,240 | `/var/log/journal` | 3,019,530,240 |
| 11 | `/var/log/journal/1c53327a4d7a4405a156a1989a76a001` | 3,002,740,736 | `/var/log/journal/1c53327a4d7a4405a156a1989a76a001` | 3,002,740,736 |
| 12 | `/usr/lib` | 2,669,535,232 | `/usr/lib` | 2,669,535,232 |
| 13 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry/logs` | 1,007,222,784 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry/logs` | 1,007,222,784 |
| 14 | `/usr/lib/x86_64-linux-gnu` | 780,701,696 | `/usr/lib/x86_64-linux-gnu` | 780,701,696 |
| 15 | `/usr/lib/firmware` | 674,009,088 | `/usr/lib/firmware` | 674,009,088 |
| 16 | `/usr/bin` | 622,911,488 | `/usr/bin` | 622,911,488 |
| 17 | `/root/tz01-env` | 540,434,432 | `/root/tz01-env` | 540,434,432 |
| 18 | `/usr/share` | 533,917,696 | `/usr/share` | 533,917,696 |
| 19 | `/root/tz01-env/venv` | 471,957,504 | `/root/tz01-env/venv` | 471,957,504 |
| 20 | `/var/www` | 470,327,296 | `/var/www` | 470,327,296 |
| 21 | `/var/www/adjarabot` | 469,594,112 | `/var/www/adjarabot` | 469,594,112 |
| 22 | `/tmp` | 453,599,232 | `/tmp` | 453,599,232 |
| 23 | `/var/lib` | 419,340,288 | `/var/lib` | 419,344,384 |
| 24 | `/usr/lib/modules` | 332,951,552 | `/usr/lib/modules` | 332,951,552 |
| 25 | `/usr/src` | 325,926,912 | `/usr/src` | 325,926,912 |
| 26 | `/root/btc-5m-twap` | 313,143,296 | `/root/btc-5m-twap` | 313,143,296 |
| 27 | `/root/.npm` | 301,248,512 | `/root/.npm` | 301,248,512 |
| 28 | `/root/.npm/_cacache` | 301,178,880 | `/root/.npm/_cacache` | 301,178,880 |
| 29 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry/line-monitor` | 294,944,768 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry/line-monitor` | 294,944,768 |
| 30 | `/root/crypto-auto` | 292,741,120 | `/root/crypto-auto` | 292,741,120 |
| 31 | `/home` | 266,657,792 | `/home` | 266,657,792 |
| 32 | `/home/ai_developer` | 266,620,928 | `/home/ai_developer` | 266,620,928 |
| 33 | `/root/crypto-auto/.claude` | 265,330,688 | `/root/crypto-auto/.claude` | 265,330,688 |
| 34 | `/home/ai_developer/.local` | 259,440,640 | `/home/ai_developer/.local` | 259,440,640 |
| 35 | `/usr/lib/node_modules` | 233,283,584 | `/usr/lib/node_modules` | 233,283,584 |
| 36 | `/usr/lib/node_modules/@anthropic-ai` | 216,178,688 | `/usr/lib/node_modules/@anthropic-ai` | 216,178,688 |
| 37 | `/usr/lib/node_modules/@anthropic-ai/claude-code` | 216,174,592 | `/usr/lib/node_modules/@anthropic-ai/claude-code` | 216,174,592 |
| 38 | `/root/my_real_estate_bot` | 210,751,488 | `/root/my_real_estate_bot` | 210,751,488 |
| 39 | `/boot` | 210,616,320 | `/boot` | 210,616,320 |
| 40 | `/var/lib/apt` | 205,623,296 | `/var/lib/apt` | 205,623,296 |
| 41 | `/usr/lib/llvm-18` | 188,022,784 | `/usr/lib/llvm-18` | 188,022,784 |
| 42 | `/usr/lib/llvm-18/lib` | 188,018,688 | `/usr/lib/llvm-18/lib` | 188,018,688 |
| 43 | `/usr/local` | 167,690,240 | `/usr/local` | 167,690,240 |
| 44 | `/usr/local/lib` | 167,575,552 | `/usr/local/lib` | 167,575,552 |
| 45 | `/usr/lib/modules/6.8.0-136-generic` | 161,607,680 | `/usr/lib/modules/6.8.0-136-generic` | 161,607,680 |
| 46 | `/usr/lib/modules/6.8.0-139-generic` | 161,509,376 | `/usr/lib/modules/6.8.0-139-generic` | 161,509,376 |
| 47 | `/root/btc-5m-twap/.git` | 157,184,000 | `/root/btc-5m-twap/.git` | 157,184,000 |
| 48 | `/root/btc-5m-twap/research` | 155,439,104 | `/root/btc-5m-twap/research` | 155,439,104 |
| 49 | `/root/tz01-out-archive` | 155,107,328 | `/root/tz01-out-archive` | 155,107,328 |
| 50 | `/root/tz01-out-archive/tz01-out` | 155,103,232 | `/root/tz01-out-archive/tz01-out` | 155,103,232 |
| 51 | `/usr/lib/modules/6.8.0-136-generic/kernel` | 154,103,808 | `/usr/lib/modules/6.8.0-136-generic/kernel` | 154,103,808 |
| 52 | `/usr/lib/modules/6.8.0-139-generic/kernel` | 154,005,504 | `/usr/lib/modules/6.8.0-139-generic/kernel` | 154,005,504 |
| 53 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry/burst` | 152,842,240 | `/root/PROJECT_GAMING_PS5/netaudit/telemetry/burst` | 152,842,240 |
| 54 | `/var/cache` | 152,223,744 | `/var/cache` | 152,223,744 |
| 55 | `/usr/lib/python3` | 147,832,832 | `/usr/lib/python3` | 147,832,832 |
| 56 | `/usr/lib/python3/dist-packages` | 147,828,736 | `/usr/lib/python3/dist-packages` | 147,828,736 |
| 57 | `/usr/src/linux-headers-6.8.0-136` | 133,316,608 | `/usr/src/linux-headers-6.8.0-136` | 133,316,608 |
| 58 | `/usr/src/linux-headers-6.8.0-139` | 133,312,512 | `/usr/src/linux-headers-6.8.0-139` | 133,312,512 |
| 59 | `/root/.cache` | 118,599,680 | `/root/.cache` | 118,599,680 |
| 60 | `/root/.cache/pip` | 117,706,752 | `/root/.cache/pip` | 117,706,752 |
| 61 | `/usr/libexec` | 115,503,104 | `/usr/libexec` | 115,503,104 |
| 62 | `/var/cache/apt` | 114,532,352 | `/var/cache/apt` | 114,532,352 |
| 63 | `/usr/lib/firmware/nvidia` | 109,867,008 | `/usr/lib/firmware/nvidia` | 109,867,008 |
| 64 | `/usr/share/dict` | 109,350,912 | `/usr/share/dict` | 109,350,912 |
| 65 | `/usr/lib/snapd` | 109,244,416 | `/usr/lib/snapd` | 109,244,416 |
| 66 | `/var/lib/btc-recorder` | 108,896,256 | `/var/lib/btc-recorder` | 108,900,352 |
| 67 | `/usr/lib/x86_64-linux-gnu/openblas-pthread` | 106,729,472 | `/usr/lib/x86_64-linux-gnu/openblas-pthread` | 106,729,472 |
| 68 | `/root/my_real_estate_bot/data` | 103,161,856 | `/root/my_real_estate_bot/data` | 103,161,856 |
| 69 | `/usr/include` | 102,174,720 | `/usr/include` | 102,174,720 |

</details>

### V4 — window

`t0` is 2026-09-13T17:55:36Z and `t1` is 2026-09-13T18:56:38Z: `3661.756` s apart start to start, and `3652.952` s from the end of the `t0` set to the start of `t1`. Both are at least `3,600`, asserted.

### V5 — accounting closure

The fall in `df` available is `3,657,728`. The du `/` delta is `3,633,152`, which is the whole disjoint partition below `/`. The change in unlinked-open allocated bytes is `0`. **The residual is `24,576` bytes**, which does not exceed `100,000,000`. This is recorded, not asserted: §7 sets no threshold. Over the supplementary window the same closure leaves `0`.

### V6 — preservation

**91 of 91** preserved files have equal SHA-256 at source, at destination and in R1's record, asserted. `/root/btc-forensics/` holds exactly the `91` planned entries, also asserted. The per-file hashes are the SHA-256 column in §2.2.

### V7 — the capture is untouched

Immediately before R4: pid `228592`, start tick `355131283`, `1034` interval directories. Immediately after: pid `228592`, start tick `355131283`, `1034`. The pid is unchanged and the count has not fallen: **2 of 2**, asserted.

### V8 — the recorder survived

From run start (2026-09-13T17:55:36Z) to run end (2026-09-14T00:03:15Z), the pid went `228592` → `228592` and the start-record sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` → `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`. The newest interval directory's T0 went `1789322100` → `1789344000`. **3 of 3**, asserted. `ps` at run end shows `228592 Sat Sep 12 09:53:04 2026 /root/tz04a-env/venv/bin/python -B -u recorder.py`.

### V9 — fingerprint table

Read at run start from `origin/main` at `c23e18c86b33924979581c25be97c08cc2fbff23`. **The frozen rows match: 15 of 15**, in lines, bytes and SHA-256, asserted.

| path | lines | bytes | state | SHA-256 |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 425 | 48,655 | reported | `588645c3366837f27b8ad6b1ca0acc79febfef16858ba6b060f53482c80a6f10` |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` |
| `research/pfair.py` | 281 | 12,499 | frozen | `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` |
| `research/selftest-pfair.py` | 306 | 15,647 | frozen | `97de9782d319c82ee6a7d81ddbd8e00d590d85ffe2daa41abe3d71ae92712c94` |
| `research/tz06-calibration.py` | 577 | 27,138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` |
| `research/tz07a-variance-time.py` | 619 | 28,219 | frozen | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` |

The TZ read is `CryptoTZ/TZ-09-disk-inventory.md`: `227` lines, `12,139` bytes, `db811fea3dea51b58c4a7894cb9666e60b6fcb5b2e86073ba7c89cc9c6fe09e1`. Model: Opus, as the TZ names.

### V10 — free space, exact bytes

| instant | UTC | available | used |
|---|---|---|---|
| run start | 2026-09-13T17:55:36Z | 6,570,545,152 | 23,605,788,672 |
| M3 `t0` | 2026-09-13T17:55:36Z | 6,570,528,768 | 23,605,805,056 |
| M3 `t1` | 2026-09-13T18:56:38Z | 6,566,871,040 | 23,609,462,784 |
| immediately before R4 | 2026-09-13T23:56:45Z | 14,251,536,384 | 15,924,797,440 |
| immediately after R4 | 2026-09-13T23:56:45Z | 14,415,523,840 | 15,760,809,984 |
| run end | 2026-09-14T00:03:15Z | 14,416,265,216 | 15,760,068,608 |

The supplementary read `t2`, at 2026-09-13T22:07:18Z, had `6,199,349,248` available and `23,976,984,576` used.

## 5. Publication

- Branch `tz-09-disk-inventory` at `e45f38e89b5ee18e64a16a654b341d74fadcac26`, pushed.
- PR #10, <https://github.com/seahomebatumi-ai/btc-5m-twap/pull/10>, open and unmerged.
- `research/tz09-disk-inventory.py` is 894 lines and 41,004 bytes, SHA-256 `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6`.
- No Release; §9 asks for none. No dataset entered git.

§4.2 self-check, and TZ-09 §6's merge-base diff, verbatim:

```
$ git rev-list origin/main | grep -c e45f38e
0
$ git diff --name-only origin/main origin/tz-09-disk-inventory
research/tz09-disk-inventory.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'

$ git diff --name-only $(git merge-base HEAD origin/main) HEAD
research/tz09-disk-inventory.py
```

The only repository path the branch touches is `research/tz09-disk-inventory.py`. The report is the second authorized path, committed straight to `main`.

## 6. What could not be implemented as written

1. **R4 was run by the Boss, not by the Executor.** §4 says R3 and R4 are shell commands the Executor runs. The Executor's R4 command, the same ordered block, was refused by the session's permission classifier before execution. The trees were then confirmed intact at their R1 byte totals and no `before-r4` read existed. The block was handed to the Boss, who ran it at 23:56:45 UTC, as a routing action under contract §2. The outcome was verified from `r4.log`, the reads it wrote, `df`, `ps` and `test -e`, not from the Boss's account (§2.4). `rm -rf` of multiple trees therefore joins `kill` among the actions this sandbox refuses.
2. **The supplementary read `t2` is outside the TZ.** After M3, a shell `df` showed free space about `367,000,000` bytes below `t1`. The same M2 command set was then run once more, as `t2` at 2026-09-13T22:07:18Z, and the committed `m3` code compared `t1` with `t2`. Nothing in the report's first paragraph, in `D` or in `A` comes from it. It is disclosed because it names where the drain went, and because choosing a new deciding window after seeing data would be reinterpreting §3. Its non-zero rows are in Appendix C.
3. **Free space changed between `t2` and R4 through action outside this TZ.** Free space went from `6,199,349,248` at `t2` to `14,251,536,384` immediately before R4. The Boss reports that `PROJECT_GAMING_PS5`'s engineer cleared the telemetry captures. A read-only `du` measured `/root/PROJECT_GAMING_PS5/netaudit/telemetry/captures` at `40,960` bytes and `/root/PROJECT_GAMING_PS5` at `335,556,608`, at 2026-09-14 00:01:51 UTC. This TZ did not touch that tree, in keeping with §2.
4. **R2 carries a second rule: abbreviated hashes.** `CryptoReports/TZ-01-twap-divergence-report.md` §7.5 names the 2026-08 partition as `2570ed2ea4e6c48d...`, the first sixteen hex characters of its SHA-256. The full hash occurs in no artifact, so a literal full-hash search deletes that file. §5.3 keeps "files whose SHA-256 a committed artifact names", and a deletion cannot be undone, so the file was preserved (3,253,357 bytes). The rule is in `cmd_r1`: a run of at least eight hex characters closed by an ellipsis. It matched this one file and no other. **The opposite case was not preserved.** The same report's §2 gives one SHA-256 over all of `partitions/` (24 files) and one over all of `state/` (24 carry-tail files). Neither is any single file's hash. The other 23 partitions and the 24 state files were deleted under R2 as written, so those two rows of the TZ-01 report can no longer be verified from disk.
5. **R2 had a defect in its first run, fixed before anything was acted on.** The first R1 runs, `r1a` and `r1b` at 17:58 UTC, called `git ls-tree` from `research/`, which resolved `CryptoReports/` relative to that directory. They therefore searched `SYSTEM-MAP.md` only and preserved 55 files. The call now uses `--full-tree` and asserts that at least one report is found. No copy or deletion was made from those runs. The script at that point had SHA-256 `8320b91dec2be4a437e61c759eae1e23b012424313460d4f8660245dc8167450`, and `gate`, `t0`, `t0b` and V3 ran on it. Its differences from the committed `e45f38e` are the docstring, the snapshot printer (split into `print_snap` with a new `show`, and M5's 962-row listing summarized), `cmd_r1` and the command table. `df_read`, `du`, `m2`, `deleted_open`, `recorder_state`, `cmd_gate`, the measuring body of `cmd_snap`, `cmd_v3`, `cmd_m3` and `cmd_m6` are byte-identical between the two. `t1` ran on an intermediate version that differed from the committed one at most in `cmd_r1`, which a snapshot never calls. `t2`, R3, V6 and everything after them ran on the committed file.
6. **Contract §10 forbids reading `/root/tz01-out-archive/`; TZ-09 §4 R1 requires hashing it.** The TZ wins for this task, under the contract's opening rule. The tree was read only by R1, and 4 of its 51 files survive in `/root/btc-forensics/`.
7. **Start-up used worktrees.** Contract §1 says to run `git checkout main && git pull` first, but the recorder runs from the primary checkout, so that checkout was left on its branch. The implementation lives in `/root/tz09-work/wt`, and the report was committed from a detached worktree at `origin/main`. R4 deleted three older worktrees that sat inside the allow-listed trees. Their registrations under `.git/worktrees/` now show as `prunable`, and git still considers local `main` checked out in one of them. Those registrations lie outside the §4 allow-list and were not pruned.
8. **Readings chosen where §3 leaves room.**
   - **M2.** "Subtree" was read as a depth-2 directory, and "not this project's" as not being, and not lying under, one of the paths in `PROJECT_PATHS`. "Drill to --max-depth=3" was read as `du --max-depth=3 <subtree>`.
   - **M3's consumer rule.** Nested directories all satisfy the rule together, so the deepest satisfying directory is the one named. The table lists only the non-zero rows.
   - **M4.** The enumeration ran although the 100,000,000-byte condition was never met, because V5 needs its figure.
   - **V5.** The "sum of directory deltas" is the du `/` delta, which is the disjoint partition, and unlinked-open bytes are counted as allocated blocks.
   - **M5 and M6.** Both on-disk and apparent bytes are reported. M6's twenty oldest intervals hold no Tier C file, which is a compositional difference from the capture as a whole.
9. **Determinism.** Contract §6 requires byte-identical re-runs, which a live host cannot give for measurements. The deterministic part, R1 and R2, ran twice identically. V3 is the stability check the TZ fixes for the rest.
10. **Report structure.** TZ-09 §8's order (§3, §4, §5, §7, then publication) replaces contract §8's section list for this task. The contract's fingerprint section is V9 and its input section is V1 and V9. Nothing was re-collected. The capture was only read, and the dataset Release was not fetched: `A1` is compared as a string.
11. **Timing.** The session was idle from 18:56 to 22:05 UTC, on a usage limit. That is why M3 was computed after `t1` rather than at it, and why `t2` falls three hours after `t1`. No reading moved because of it. The whole R4 block executed within 23:56:45 UTC, so all seven of its reads carry the same second.

## Appendix A — every regular file R1 enumerated

`269` files. The five trees no longer exist, and this table is their record.

<details><summary>The full table</summary>

| file | bytes | SHA-256 | preserved |
|---|---|---|---|
| `/root/tz01-out-archive/tz01-out/twap-divergence-observations.parquet` | 76,810,985 | `0dc121291b897857ff87d9a1f85a3fc29a340d7c62829f2b21cf371d3c380f1e` | yes |
| `/root/tz01-out-archive/tz01-out/twap-divergence-summary.md` | 41,445 | `170c4c666e0dcee6c2b2eff51bc8702c6314cbda979cb24edbb89e6252d5b0c6` | yes |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2024-09.parquet` | 3,158,151 | `1f51d647a7df5b1f64de93c1f5be9bd7360cdfe50ccde3de5b0eabd9077421cf` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2024-10.parquet` | 3,267,254 | `9839708274d3166c84496e0d38e49a75ad5c5dacdb39d5d16ded6ba28b807f6e` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2024-11.parquet` | 3,178,957 | `4393a1bbe6af44646079458d16e354fc41c00841f33a96ee4288696402817602` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2024-12.parquet` | 3,302,361 | `8c8b8819d172f7bed46b900bd1555bda1a240afa05093279822f4f527ca4a8fe` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2025-01.parquet` | 3,307,177 | `233f4865bb411253a93a13a39f4fc0ad318660b063f54d7d30b4c96cc459a35a` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2025-02.parquet` | 2,973,855 | `92daa090201ab1a645cd8668f00081ba8c8e9578a1aad67db217288f582de94f` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2025-03.parquet` | 3,299,348 | `47aff725eabcaa32390766df5c60828791b15525f8be86224b988b7d087190a1` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2025-04.parquet` | 3,184,794 | `e8d7a0ee923cbf28a42c07fa89431cc467ed78994e969eeb7bd1fa914e70a017` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2025-05.parquet` | 3,293,371 | `ef1a7c45057760376faea9f8cdb614044c51b5cd4e8dc39a0f21889cf4657fbc` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2025-06.parquet` | 3,171,977 | `586e48f9712d68437ace472c88fd82aa3f27f3bced0035d1650398fac59fc4e1` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2025-07.parquet` | 3,282,554 | `7ac304cff8d2995d902ad88f1b5ad0de9d271c3b8d7f10dc1ed648808c0a4ad7` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2025-08.parquet` | 3,287,472 | `2daa81479a8f55813a3675d07a479cb7de56ffb093c3cc016da9618dd5f934fd` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2025-09.parquet` | 3,160,387 | `b41cbbb0be655b5726764c0ba8d5d2a9117f097dbf69ba5c1c289845c7bf52b9` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2025-10.parquet` | 3,306,411 | `e4d52ab8c2f2a0285c2ef8e27c47116d1b34cf8773ff8bbc2997db99f753872a` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2025-11.parquet` | 3,193,158 | `5ae081f483a5e76f61c60693f7ad77be046e1ebdda8fb0476103c735935db776` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2025-12.parquet` | 3,287,809 | `a2f9e63feb04f5aafdae770c2299a3815c37e0ede34175cfe4feee2b85596e9b` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2026-01.parquet` | 3,284,381 | `ed9c1901648695da68e05d0724ee81d4eafbf358ff7047bcf07f7cc442b14e23` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2026-02.parquet` | 2,976,093 | `017a4ccfa698814d93fb285f3ea8a8e89ecc2fc9bac8324c0739ccada36a6c9d` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2026-03.parquet` | 3,296,615 | `27666650b2a3085a595f61ca1cbd230716e0ae1913ef289a6702cbf089383bf7` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2026-04.parquet` | 3,174,584 | `397307b015cda60049d2f02ad0dea1939cd80362d82c02d908472c82c5c7c3bb` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2026-05.parquet` | 3,271,690 | `ecd2f1e64123d0d0461bd6edb77a31db37060bf9a2b777e4a90273994514e30d` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2026-06.parquet` | 3,185,444 | `728f5e1cc201f8e2396413dfdbc8452d85f6f6827f2760e8a579b5a2203af695` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2026-07.parquet` | 3,280,011 | `4f3d50a232b0b169f51a96aff9900f75332006dbc9f75ab214b50d1fcd4a568d` | — |
| `/root/tz01-out-archive/tz01-out/partitions/twap-divergence-2026-08.parquet` | 3,253,357 | `2570ed2ea4e6c48d687496160522c4eb4b5c27928824a3611bcca35d3a7e914d` | yes |
| `/root/tz01-out-archive/tz01-out/state/carry-2024-10.npz` | 31,614 | `061c4e6a5da5c3869caf75853b43abf2c35260df99a5cd0e8e99f4e5e7be909d` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2024-11.npz` | 31,614 | `03078925ab1c4bdbfed79ffe817f6da87a5f4a48a6eac160bb81e175de75ff94` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2024-12.npz` | 31,614 | `92026deedc1cc0c791beba8aa93b6e7d1eab3d2f0043b38d621ab44439678305` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2025-01.npz` | 31,614 | `10899ca3f99cb3d47754933953095620802a0598ffca5ff8971466477d613a87` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2025-02.npz` | 31,614 | `f3e51f82057926a9ae5ea8f7133109518ea027ac7d6b7f84698b048cf655ba36` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2025-03.npz` | 31,614 | `c436d2a6980c31d55d10c592eac8a9ae388f9f6ba2b1fc2509b8759155893bdd` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2025-04.npz` | 31,614 | `e95b28b38b8c0805bda0cd058d4d06667dd9ce6c5ea766ebd7d426a602f32c1f` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2025-05.npz` | 31,614 | `3aa51f4bc34a3d18ba587460855ba0b24a038b11a99395566d2271f697fc5427` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2025-06.npz` | 31,614 | `7203910ff9b21eed9d59d107d70fbcfecacb2e761473be9f7a9373b5b1e00b73` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2025-07.npz` | 31,614 | `aa6eb7c2209459da588648a22fcc158d706cdf841fa6a6c98d5c491222c3cef7` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2025-08.npz` | 31,614 | `f58e4311d88442b1c557d753531524157f7f391bf6df0fc10bc5d5b07c1f7956` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2025-09.npz` | 31,614 | `8b15d99c2cfaf25e51d19ac113610c5f91784742c91c4191fba3f194d81e363b` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2025-10.npz` | 31,614 | `a2dc5ecfd97504b7ace20742dbc33191a5e844c4c8c6c6ddda78ebca3156d5e9` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2025-11.npz` | 31,614 | `1c2ddb5c013e38184712157f4362a5f108807c9509994ff0a3a9390bb8c5b385` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2025-12.npz` | 31,614 | `79334c5e007e166d501a07023bd2c1aa403250186bb036115ff9e0360ec4d0a2` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2026-01.npz` | 31,614 | `4a9709b2e8b182bf2740df6abc11f80fbac4c07d02bafe48fd7c00960093a1cf` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2026-02.npz` | 31,614 | `4da55994a50836ca7000b12c25821d50d3b72d91fbf2c91a23aa1b9e100f4ea8` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2026-03.npz` | 31,614 | `8e4bda94579ec167fc6bbcf6802ccb64952a87d5d86821b84cd39e1e7cb61761` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2026-04.npz` | 31,614 | `d333ab8c9c3f0cf9c735b3e604476a287f7bcf8bea6773ae019b2cc496f9e949` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2026-05.npz` | 31,614 | `d483eb16101dc870abde5713193ad7154f81bae8500f37431c34f304c5b7c59e` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2026-06.npz` | 31,614 | `da0c3f3ccce95c1e362e28acd10121eda949bf880f9afde3aa9b190c9c9911e9` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2026-07.npz` | 31,614 | `2d15ef02e04ea3b091409106b7e0a9e6697460bb58895af9e12ab01b62417053` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2026-08.npz` | 31,614 | `d388045f65cde6694acb5353db1010862d04d686b7b3dbb073363b1221c74ae2` | — |
| `/root/tz01-out-archive/tz01-out/state/carry-2026-09.npz` | 31,614 | `04eec3315a2af498f47ec62fa286d584538d6f185264d05e4d1c2f1337d22fa4` | — |
| `/root/tz01-out-archive/tz01-out/state/coverage.json` | 10,293 | `83de2b2a778a8ba2960b413b12af413af4f405b1966e92ce8de7330f8fc38d13` | yes |
| `/root/tz06-work/err-1.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | — |
| `/root/tz06-work/head.md` | 8,454 | `96c0bf36113e9dc745b940a463c10c2387e246385ae587b7b3b7a476c8be7f09` | — |
| `/root/tz06-work/mid.md` | 6,928 | `5f515ee37dfdac2903188e9fd12a79994534cb93a52c0445dec0d777009c475c` | — |
| `/root/tz06-work/mid2.md` | 31,611 | `07b381afd62d9c239087fa4b7b5b72386833815e7d2b904866ca549d8488738e` | — |
| `/root/tz06-work/mkreport.py` | 3,822 | `cba9b9fb10d2ed509e4a7a1ba794eded2e3fe1ad70b9d1c8f8eeb74175a0038d` | — |
| `/root/tz06-work/rc-results-1.json` | 201,017 | `a614f57f598b9e2872adc0f53f3a1e356e0d9e0837b044df9fd66ffec17110ea` | — |
| `/root/tz06-work/rc-stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | — |
| `/root/tz06-work/report-parts.md` | 30,484 | `520e813dc561e221a9fc3fd30f9a04edf910b552462faba03fb0b2984a08832b` | — |
| `/root/tz06-work/results-1.json` | 90,457 | `15d0b0cfa699d11c87123807b7d8c979a34a554d8ae7e5f14f13f16172dee48d` | yes |
| `/root/tz06-work/results-2.json` | 90,457 | `15d0b0cfa699d11c87123807b7d8c979a34a554d8ae7e5f14f13f16172dee48d` | yes |
| `/root/tz06-work/tables-1.md` | 33,976 | `6827cd348262d1a4080a7ef75353f539585a6a211b28d7bc96567eb34ef1ebc6` | yes |
| `/root/tz06-work/tables-2.md` | 33,976 | `6827cd348262d1a4080a7ef75353f539585a6a211b28d7bc96567eb34ef1ebc6` | yes |
| `/root/tz06-work/tail.md` | 13,564 | `fdb3cdaf2e7dc6b8bf8e48f8da6dcdd0c5626e0d354609b51038746f70fa076a` | — |
| `/root/tz06-work/tz06-observations-2.csv` | 843,788 | `4e20c4fafbe60fe64c48ce1833a8da55f7fce2c0bad87e93b55ba95a2a4f85bb` | yes |
| `/root/tz06-work/tz06-observations.csv` | 843,788 | `4e20c4fafbe60fe64c48ce1833a8da55f7fce2c0bad87e93b55ba95a2a4f85bb` | yes |
| `/root/tz07-work/TZ-07a-variance-time-report.md` | 38,555 | `15c26ec8b7ac670bb136177fd3a87dcd56935077714feff48f833dd08b3af72b` | — |
| `/root/tz07-work/commit-msg.txt` | 1,145 | `c70efadeb18408dabbb22d04321a43fc6ef67eb5aad9647bda60e9035a319aed` | — |
| `/root/tz07-work/determinism.sh` | 905 | `5cb3d1a52f600ddb39bec9535b3c25f6214de95d0cfaa72ceb7906d5597c18be` | — |
| `/root/tz07-work/determinism.txt` | 386 | `ed804633b1e70c7ec43c1f9116075956e5096696f9db14ec7d333d0240aafea0` | — |
| `/root/tz07-work/err-1.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | — |
| `/root/tz07-work/extract.py` | 2,190 | `36a339ffecf38ec5d5e651c7ab914f7ec40dc6ff7a20125571692e23dbc04070` | — |
| `/root/tz07-work/impl-sha.txt` | 41 | `3aeef641afa329d10a765797a1fea474f45b3b6637fa27f829188f9bf40f866a` | — |
| `/root/tz07-work/pr-body.txt` | 2,011 | `5938c49dbb658714d466aafcb8b92bedfd220eb0d73409dc1859eb4f51172b52` | — |
| `/root/tz07-work/pr-url.txt` | 55 | `839b1476c0e5580917e3e0646d205ae2fe9995564e49b4dc6332770cbf9ba1a7` | — |
| `/root/tz07-work/report-part0.md` | 7,136 | `b1e49263d153bdab0e50fdd5654deead1424e5c1dfa3b49684496febbd76c6c3` | — |
| `/root/tz07-work/report-part2.md` | 18,518 | `70db14e7584e1fcfb5e80b85645c267d21c10274857998bb2206b22bdabf56d4` | — |
| `/root/tz07-work/report-part3.md` | 12,901 | `b464f805b60164584ad94d5896c07d132a375a21046d42ac920d68a0c288db82` | — |
| `/root/tz07-work/results-1.json` | 63,623 | `64515cffa976a22455835bfa18832a7246419ef805d25a53a6697d63d884db72` | — |
| `/root/tz07-work/run-1.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | — |
| `/root/tz07-work/run-1.json` | 64,052 | `1aab3a00b2a8617342d53d082e0f75c3c6cd50f17ac47510545715f4f22697e7` | yes |
| `/root/tz07-work/run-2.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | — |
| `/root/tz07-work/run-2.json` | 64,052 | `1aab3a00b2a8617342d53d082e0f75c3c6cd50f17ac47510545715f4f22697e7` | yes |
| `/root/tz07-work/separation.txt` | 303 | `44b3ca7e970815dec7747821fda7b147b473d2056481dc165dfb215ed139d2d7` | — |
| `/root/tz07-work/write-report.py` | 9,667 | `8d1d44d9924e51ae6d3b4b81cad6d07121ca8e1546205febdc77c79605e1ff8a` | — |
| `/root/tz07-work/write-report2.py` | 11,801 | `135e378f9213bb2b079016281bc010e56565b0c8084d5aba54effa7f03c235fd` | — |
| `/root/tz07-work/write-report3.py` | 15,756 | `de55800bb7ef2fe3fb8218f4ee657b622c3787765fbb5b85698191f93b5a9677` | — |
| `/root/tz07b-work/commit-msg.txt` | 1,928 | `8df2af99208a919012251a7743dd0e74840e5f901488b25b3bf80bf42fa4536a` | — |
| `/root/tz07b-work/determinism.sh` | 934 | `0318ab3a73f7d3c894163bfc5dfda933ef28192e0ed93ac8ae5974e4e51cc50a` | — |
| `/root/tz07b-work/determinism.txt` | 480 | `de055045fdcc50b74ef140ccd6652305846c9d22a396d46d0c9ddd5b53b570b5` | — |
| `/root/tz07b-work/emit.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | — |
| `/root/tz07b-work/emit.txt` | 141 | `2875cf827ba1cd418ff5f2166f05e865f51d33393b46c19bfca8a58688993a54` | — |
| `/root/tz07b-work/impl-sha.txt` | 41 | `1ec894ab13dc5c94e52a501da91ad7611ff4f87cab2f2c348406c6e80bbd6a82` | — |
| `/root/tz07b-work/pr-body.txt` | 3,273 | `2901f2e9af78a43361bdea16587f23e7c3a7df26986e31bfd8d5c8c6ba09acac` | — |
| `/root/tz07b-work/pr-url.txt` | 55 | `d674e20aa9a9eded6936660424654c41868f8170b22e7bba418fac41a130b734` | — |
| `/root/tz07b-work/results-0.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | — |
| `/root/tz07b-work/results-0.json` | 13,222 | `7f661c78cbeee11eb3cb62e1d9038d2772d7d66c479cc1d75d38077f617a7185` | yes |
| `/root/tz07b-work/run-1.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | — |
| `/root/tz07b-work/run-1.json` | 13,222 | `7f661c78cbeee11eb3cb62e1d9038d2772d7d66c479cc1d75d38077f617a7185` | yes |
| `/root/tz07b-work/run-2.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | — |
| `/root/tz07b-work/run-2.json` | 13,222 | `7f661c78cbeee11eb3cb62e1d9038d2772d7d66c479cc1d75d38077f617a7185` | yes |
| `/root/tz07b-work/separation.txt` | 351 | `c1b6f3387771e2e22a51b1515d9dd8593335d1137118970252a881cbb23fef45` | — |
| `/root/tz07b-work/smoke.py` | 1,213 | `1c11c08e2d83de8cd83ea1f7ab34847c0cdf526e1d6609853339cba972f10db5` | — |
| `/root/tz07b-work/tables.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | — |
| `/root/tz07b-work/tables.md` | 1,577 | `9bd86e88be84b3fb92611893b673ba277238921549236a734dca13252e3e68d0` | — |
| `/root/tz07b-work/v6.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | — |
| `/root/tz07b-work/v6.json` | 353 | `8f8aea8e8781dce00ea4a2a2218b7260061ace85676a81b89db850b7c2a2754e` | — |
| `/root/tz07b-work/wt/.git` | 44 | `8680f8c0eb69788a3f13a78de76ab8794fd8d70835e8c722beb93ee7fc11f6f4` | — |
| `/root/tz07b-work/wt/.gitignore` | 252 | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | yes |
| `/root/tz07b-work/wt/BTC-EXECUTOR-INSTRUCTIONS.md` | 11,128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `/root/tz07b-work/wt/SYSTEM-MAP.md` | 33,309 | `09f71ca07e1b2329f21bccd1523ed4607b122af5c54a2ba20e83fb3239fb9dac` | yes |
| `/root/tz07b-work/wt/CryptoReports/TZ-01-twap-divergence-report.md` | 56,532 | `6077fb6a0fb62d5803e70ee5d6f0b8bc8332d756da0af637606eca99bf44f65b` | — |
| `/root/tz07b-work/wt/CryptoReports/TZ-01a-twap-divergence-corrected-report.md` | 59,427 | `bc655c569ec10dffcf817f9dc6373575749b3f147441af640c7738ec5feb47bc` | — |
| `/root/tz07b-work/wt/CryptoReports/TZ-02-divergence-distribution-report.md` | 66,803 | `c7db53c035d389f05a784ba4c9b398a417c9aa7614112ac0d1afa842ccdedef2` | — |
| `/root/tz07b-work/wt/CryptoReports/TZ-03-repo-hygiene-report.md` | 14,910 | `e14cdd5067ed53bfbb4bef6de150331fbcb1ef259793953f165d25ee11a4d397` | — |
| `/root/tz07b-work/wt/CryptoReports/TZ-04-market-recorder-report.md` | 7,573 | `237116cc437dd9216927cf175a0c66921cff2296385bb4b4914cd8d3be74cf51` | — |
| `/root/tz07b-work/wt/CryptoReports/TZ-04a-market-recorder-corrected-report.md` | 9,868 | `975843f66a9c0d563c165e681b69482fbefbf8aca880bdd9f87216997e63292c` | — |
| `/root/tz07b-work/wt/CryptoReports/TZ-04b-market-recorder-scoring-report.md` | 68,352 | `a18ffd566085cea8f10feba139fadda0f1592f38adddde7e008792c46e8a8e9c` | — |
| `/root/tz07b-work/wt/CryptoReports/TZ-05-quote-capture-report.md` | 12,343 | `ec548d0e1a4b9bf09695d079b7513428b022460a2b411f9c8ee54f4698778daf` | — |
| `/root/tz07b-work/wt/CryptoReports/TZ-05a-quote-capture-deploy-report.md` | 26,565 | `cddca348120ae278f3c399ea21353f57e8b3722f3b0372e247cc985ab1351805` | — |
| `/root/tz07b-work/wt/CryptoReports/TZ-06-pfair-calibration-report.md` | 60,833 | `33863ce6d62443dd070646854b135438ee624c96b5204cd9851cfbca9939396f` | — |
| `/root/tz07b-work/wt/CryptoReports/TZ-07-variance-time-report.md` | 11,745 | `4056137f8de8ef6fa39e43a348a1f60bdfee10f7ffe2c29ebb6e4f6e7894c5b4` | — |
| `/root/tz07b-work/wt/CryptoReports/TZ-07a-variance-time-report.md` | 38,555 | `15c26ec8b7ac670bb136177fd3a87dcd56935077714feff48f833dd08b3af72b` | — |
| `/root/tz07b-work/wt/CryptoTZ/TZ-01-twap-divergence.md` | 10,121 | `455f58e0616daeacfb67ee7302d84520826780720b5c56c7e7a06463ec63dd57` | — |
| `/root/tz07b-work/wt/CryptoTZ/TZ-01a-twap-divergence-corrected.md` | 8,118 | `a8c4c7c22881236903797e2ffc2d8c87d6e9fc74cd282c7e40feb9eaecab65e3` | — |
| `/root/tz07b-work/wt/CryptoTZ/TZ-02-divergence-distribution.md` | 7,208 | `c8abadec3bb4763a383f397f8ef188cda4228ed1d356f635f8674456d586f2a3` | — |
| `/root/tz07b-work/wt/CryptoTZ/TZ-03-repo-hygiene.md` | 4,657 | `0cd150f54862e6c640510acba90c36f1c351e97d0e9b068a573822455668d56e` | — |
| `/root/tz07b-work/wt/CryptoTZ/TZ-04-market-recorder.md` | 10,008 | `95b2fd8d752a759f7b274aa0fc8ca62b54d9d27d84bc91cc33cc1014c518fe09` | — |
| `/root/tz07b-work/wt/CryptoTZ/TZ-04a-market-recorder-corrected.md` | 12,445 | `fff99e417a5117ab9e5186e793adea8bec9be9140864776a84ef0f7c1f20988b` | — |
| `/root/tz07b-work/wt/CryptoTZ/TZ-04b-market-recorder-scoring.md` | 15,466 | `f4ab08b6a58f84401d38124ff54a665aaa0808a0fb3b376a1362fcb63960effc` | — |
| `/root/tz07b-work/wt/CryptoTZ/TZ-05-quote-capture.md` | 8,506 | `4b9a41fb3301712e6629fb565c47e50a38cb3c85e605122394797ed9094285fe` | — |
| `/root/tz07b-work/wt/CryptoTZ/TZ-05a-quote-capture-deploy.md` | 10,876 | `16f4821308e0f931a469acd0c7d1facffc4c3bb6c75bcd266305d1acc241410b` | — |
| `/root/tz07b-work/wt/CryptoTZ/TZ-06-pfair-calibration.md` | 14,400 | `ec2135c810be9e736946c004b7a4ced0d5a00a322061c89a1519f2d4a30f8373` | — |
| `/root/tz07b-work/wt/CryptoTZ/TZ-07-variance-time.md` | 11,924 | `759d8ed001ed6746a6b7badd430fa1b3b362849594429849cf196bd892342e2b` | — |
| `/root/tz07b-work/wt/CryptoTZ/TZ-07a-variance-time.md` | 14,260 | `0e4852301c493ed7e4cb98d8d880a2c6b42b55f01811976ca9131fc62e61c4e3` | yes |
| `/root/tz07b-work/wt/CryptoTZ/TZ-07b-settlement-dispersion.md` | 15,032 | `476344ccf393c8e3f3eb7a70e97f71af7433a45a02af069978b2e8138c155541` | — |
| `/root/tz07b-work/wt/research/pfair.py` | 12,499 | `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` | yes |
| `/root/tz07b-work/wt/research/selftest-pfair.py` | 15,647 | `97de9782d319c82ee6a7d81ddbd8e00d590d85ffe2daa41abe3d71ae92712c94` | yes |
| `/root/tz07b-work/wt/research/selftest-twap-divergence.py` | 16,736 | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `/root/tz07b-work/wt/research/twap-divergence.py` | 50,928 | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `/root/tz07b-work/wt/research/tz02-distribution.py` | 14,511 | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | yes |
| `/root/tz07b-work/wt/research/tz06-calibration.py` | 26,548 | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` | yes |
| `/root/tz07b-work/wt/research/tz07a-variance-time.py` | 28,219 | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` | yes |
| `/root/tz07b-work/wt/research/tz07b-settlement-dispersion.py` | 24,926 | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | yes |
| `/root/tz07b-work/wt/research/recorder/analyze.py` | 34,705 | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | yes |
| `/root/tz07b-work/wt/research/recorder/config.py` | 4,773 | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | yes |
| `/root/tz07b-work/wt/research/recorder/manifest.py` | 10,002 | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | yes |
| `/root/tz07b-work/wt/research/recorder/probe.py` | 9,324 | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | yes |
| `/root/tz07b-work/wt/research/recorder/recorder.py` | 25,658 | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | yes |
| `/root/tz07b-work/wt/research/recorder/selftest.py` | 30,591 | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | yes |
| `/root/tz07b-work/wt-report/.git` | 51 | `fdbc86802d9416183be9d1dc746cce8372394b184b9e864edaa9b0bcb42c6d89` | — |
| `/root/tz07b-work/wt-report/.gitignore` | 252 | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | yes |
| `/root/tz07b-work/wt-report/BTC-EXECUTOR-INSTRUCTIONS.md` | 11,128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `/root/tz07b-work/wt-report/SYSTEM-MAP.md` | 40,605 | `00bf58174de8bd83de4d2be31b531b1273ba716d2b510cba664f4780d8db52b8` | yes |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-01-twap-divergence-report.md` | 56,532 | `6077fb6a0fb62d5803e70ee5d6f0b8bc8332d756da0af637606eca99bf44f65b` | — |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-01a-twap-divergence-corrected-report.md` | 59,427 | `bc655c569ec10dffcf817f9dc6373575749b3f147441af640c7738ec5feb47bc` | — |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-02-divergence-distribution-report.md` | 66,803 | `c7db53c035d389f05a784ba4c9b398a417c9aa7614112ac0d1afa842ccdedef2` | — |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-03-repo-hygiene-report.md` | 14,910 | `e14cdd5067ed53bfbb4bef6de150331fbcb1ef259793953f165d25ee11a4d397` | — |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-04-market-recorder-report.md` | 7,573 | `237116cc437dd9216927cf175a0c66921cff2296385bb4b4914cd8d3be74cf51` | — |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-04a-market-recorder-corrected-report.md` | 9,868 | `975843f66a9c0d563c165e681b69482fbefbf8aca880bdd9f87216997e63292c` | — |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-04b-market-recorder-scoring-report.md` | 68,352 | `a18ffd566085cea8f10feba139fadda0f1592f38adddde7e008792c46e8a8e9c` | — |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-05-quote-capture-report.md` | 12,343 | `ec548d0e1a4b9bf09695d079b7513428b022460a2b411f9c8ee54f4698778daf` | — |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-05a-quote-capture-deploy-report.md` | 26,565 | `cddca348120ae278f3c399ea21353f57e8b3722f3b0372e247cc985ab1351805` | — |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-06-pfair-calibration-report.md` | 60,833 | `33863ce6d62443dd070646854b135438ee624c96b5204cd9851cfbca9939396f` | — |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-07-variance-time-report.md` | 11,745 | `4056137f8de8ef6fa39e43a348a1f60bdfee10f7ffe2c29ebb6e4f6e7894c5b4` | — |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-07a-variance-time-report.md` | 38,555 | `15c26ec8b7ac670bb136177fd3a87dcd56935077714feff48f833dd08b3af72b` | — |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-07b-settlement-dispersion-report.md` | 27,788 | `44b2ee1a80c80867aa17bf6b0c378fccbf203655dfc39a7f323861aab4d7cf80` | — |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-08-out-of-sample-report.md` | 18,738 | `b0d0c8ed31c28bfa52dc449da4a06d33318f17221a6f9d94ce9bcc8f7ecccffe` | — |
| `/root/tz07b-work/wt-report/CryptoReports/TZ-08a-out-of-sample-report.md` | 77,715 | `86d4ba81e196ace179c65067a3620bb77dba20019f428ecd1c6e588bde6c1188` | — |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-01-twap-divergence.md` | 10,121 | `455f58e0616daeacfb67ee7302d84520826780720b5c56c7e7a06463ec63dd57` | — |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-01a-twap-divergence-corrected.md` | 8,118 | `a8c4c7c22881236903797e2ffc2d8c87d6e9fc74cd282c7e40feb9eaecab65e3` | — |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-02-divergence-distribution.md` | 7,208 | `c8abadec3bb4763a383f397f8ef188cda4228ed1d356f635f8674456d586f2a3` | — |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-03-repo-hygiene.md` | 4,657 | `0cd150f54862e6c640510acba90c36f1c351e97d0e9b068a573822455668d56e` | — |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-04-market-recorder.md` | 10,008 | `95b2fd8d752a759f7b274aa0fc8ca62b54d9d27d84bc91cc33cc1014c518fe09` | — |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-04a-market-recorder-corrected.md` | 12,445 | `fff99e417a5117ab9e5186e793adea8bec9be9140864776a84ef0f7c1f20988b` | — |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-04b-market-recorder-scoring.md` | 15,466 | `f4ab08b6a58f84401d38124ff54a665aaa0808a0fb3b376a1362fcb63960effc` | — |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-05-quote-capture.md` | 8,506 | `4b9a41fb3301712e6629fb565c47e50a38cb3c85e605122394797ed9094285fe` | — |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-05a-quote-capture-deploy.md` | 10,876 | `16f4821308e0f931a469acd0c7d1facffc4c3bb6c75bcd266305d1acc241410b` | — |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-06-pfair-calibration.md` | 14,400 | `ec2135c810be9e736946c004b7a4ced0d5a00a322061c89a1519f2d4a30f8373` | — |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-07-variance-time.md` | 11,924 | `759d8ed001ed6746a6b7badd430fa1b3b362849594429849cf196bd892342e2b` | — |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-07a-variance-time.md` | 14,260 | `0e4852301c493ed7e4cb98d8d880a2c6b42b55f01811976ca9131fc62e61c4e3` | yes |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-07b-settlement-dispersion.md` | 15,032 | `476344ccf393c8e3f3eb7a70e97f71af7433a45a02af069978b2e8138c155541` | — |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-08-out-of-sample.md` | 14,465 | `bacb45ec2c0a3ed824972fe0b536a99f5ef3bad68e78a5c07fbf0c1a09d77d00` | yes |
| `/root/tz07b-work/wt-report/CryptoTZ/TZ-08a-out-of-sample.md` | 17,231 | `3c6ea77fabe9716b6bde98cdba728b67cb62a14f8172ac59bffd47dd04f5e687` | yes |
| `/root/tz07b-work/wt-report/research/pfair.py` | 12,499 | `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` | yes |
| `/root/tz07b-work/wt-report/research/selftest-pfair.py` | 15,647 | `97de9782d319c82ee6a7d81ddbd8e00d590d85ffe2daa41abe3d71ae92712c94` | yes |
| `/root/tz07b-work/wt-report/research/selftest-twap-divergence.py` | 16,736 | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `/root/tz07b-work/wt-report/research/twap-divergence.py` | 50,928 | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `/root/tz07b-work/wt-report/research/tz02-distribution.py` | 14,511 | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | yes |
| `/root/tz07b-work/wt-report/research/tz06-calibration.py` | 26,548 | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` | yes |
| `/root/tz07b-work/wt-report/research/tz07a-variance-time.py` | 28,219 | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` | yes |
| `/root/tz07b-work/wt-report/research/tz07b-settlement-dispersion.py` | 24,926 | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | yes |
| `/root/tz07b-work/wt-report/research/recorder/analyze.py` | 34,705 | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | yes |
| `/root/tz07b-work/wt-report/research/recorder/config.py` | 4,773 | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | yes |
| `/root/tz07b-work/wt-report/research/recorder/manifest.py` | 10,002 | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | yes |
| `/root/tz07b-work/wt-report/research/recorder/probe.py` | 9,324 | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | yes |
| `/root/tz07b-work/wt-report/research/recorder/recorder.py` | 25,658 | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | yes |
| `/root/tz07b-work/wt-report/research/recorder/selftest.py` | 30,591 | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | yes |
| `/root/tz08a-work/assemble-report.py` | 4,649 | `0fff1384a80e6bd9966d9a97519a4b900d5a7393588332eac3e9e9a9d9fc1f53` | — |
| `/root/tz08a-work/probe-g3.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | — |
| `/root/tz08a-work/probe-g3.json` | 9,560 | `6a1cb899c3b1b372c00dedf66d2ad14fb253930e6f2b801a6ca1dbca66810d6f` | yes |
| `/root/tz08a-work/probe-g3.py` | 3,746 | `2a311b7774432ba075a96cf2b66b9c38b5db1cee4a22d1e2e8c8880b0a14de2a` | yes |
| `/root/tz08a-work/report-template.md` | 33,193 | `56e1a4a11e677f554268879c29791fe8c9ba638f824c2848d305474cf930fa86` | — |
| `/root/tz08a-work/run1.log` | 903 | `7c895dae034cf898ac3c8f672b813a47e8ceefb34f7163f8d10ee6d798db2697` | — |
| `/root/tz08a-work/run2.log` | 912 | `fa716ab75db4870147b360d2d8af8d18581a89bda8f60ebfbdd82b7a2969cdb4` | — |
| `/root/tz08a-work/tz08a-observations.csv` | 1,066,357 | `b810b07165e98b29258479323a0c634ccaea1917135a3336b8d28fb4bb92fa77` | yes |
| `/root/tz08a-work/tz08a-results.json` | 105,047 | `b2addb77eca57ef2d915737ab3a6a0295ff797461920cc1b046b8a318d2e8b6c` | yes |
| `/root/tz08a-work/tz08a-tables.md` | 42,801 | `1f3b7b9ec63de6a7ac68522924e9bc0b24604b55163ba57f4134c7f45fd81565` | yes |
| `/root/tz08a-work/run2/tz08a-observations.csv` | 1,066,357 | `b810b07165e98b29258479323a0c634ccaea1917135a3336b8d28fb4bb92fa77` | yes |
| `/root/tz08a-work/run2/tz08a-results.json` | 105,047 | `b2addb77eca57ef2d915737ab3a6a0295ff797461920cc1b046b8a318d2e8b6c` | yes |
| `/root/tz08a-work/run2/tz08a-tables.md` | 42,801 | `1f3b7b9ec63de6a7ac68522924e9bc0b24604b55163ba57f4134c7f45fd81565` | yes |
| `/root/tz08a-work/src/BTC-EXECUTOR-INSTRUCTIONS.md` | 11,128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `/root/tz08a-work/src/SYSTEM-MAP.md` | 40,605 | `00bf58174de8bd83de4d2be31b531b1273ba716d2b510cba664f4780d8db52b8` | yes |
| `/root/tz08a-work/src/TZ-07a-variance-time.md` | 14,260 | `0e4852301c493ed7e4cb98d8d880a2c6b42b55f01811976ca9131fc62e61c4e3` | yes |
| `/root/tz08a-work/src/TZ-08-out-of-sample.md` | 14,465 | `bacb45ec2c0a3ed824972fe0b536a99f5ef3bad68e78a5c07fbf0c1a09d77d00` | yes |
| `/root/tz08a-work/src/TZ-08-report.md` | 18,738 | `b0d0c8ed31c28bfa52dc449da4a06d33318f17221a6f9d94ce9bcc8f7ecccffe` | — |
| `/root/tz08a-work/src/TZ-08a-out-of-sample.md` | 17,231 | `3c6ea77fabe9716b6bde98cdba728b67cb62a14f8172ac59bffd47dd04f5e687` | yes |
| `/root/tz08a-work/src/pfair.py` | 12,499 | `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` | yes |
| `/root/tz08a-work/src/tz06-calibration.py` | 26,548 | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` | yes |
| `/root/tz08a-work/src/tz07a-variance-time.py` | 28,219 | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` | yes |
| `/root/tz08a-work/src/tz07b-settlement-dispersion.py` | 24,926 | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | yes |
| `/root/tz08a-work/wt/.git` | 45 | `29056cf78851d10feffeff525270a25158f7321f4cb80fe4157b4b07f3dc7042` | — |
| `/root/tz08a-work/wt/.gitignore` | 252 | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | yes |
| `/root/tz08a-work/wt/BTC-EXECUTOR-INSTRUCTIONS.md` | 11,128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `/root/tz08a-work/wt/SYSTEM-MAP.md` | 40,605 | `00bf58174de8bd83de4d2be31b531b1273ba716d2b510cba664f4780d8db52b8` | yes |
| `/root/tz08a-work/wt/CryptoReports/TZ-01-twap-divergence-report.md` | 56,532 | `6077fb6a0fb62d5803e70ee5d6f0b8bc8332d756da0af637606eca99bf44f65b` | — |
| `/root/tz08a-work/wt/CryptoReports/TZ-01a-twap-divergence-corrected-report.md` | 59,427 | `bc655c569ec10dffcf817f9dc6373575749b3f147441af640c7738ec5feb47bc` | — |
| `/root/tz08a-work/wt/CryptoReports/TZ-02-divergence-distribution-report.md` | 66,803 | `c7db53c035d389f05a784ba4c9b398a417c9aa7614112ac0d1afa842ccdedef2` | — |
| `/root/tz08a-work/wt/CryptoReports/TZ-03-repo-hygiene-report.md` | 14,910 | `e14cdd5067ed53bfbb4bef6de150331fbcb1ef259793953f165d25ee11a4d397` | — |
| `/root/tz08a-work/wt/CryptoReports/TZ-04-market-recorder-report.md` | 7,573 | `237116cc437dd9216927cf175a0c66921cff2296385bb4b4914cd8d3be74cf51` | — |
| `/root/tz08a-work/wt/CryptoReports/TZ-04a-market-recorder-corrected-report.md` | 9,868 | `975843f66a9c0d563c165e681b69482fbefbf8aca880bdd9f87216997e63292c` | — |
| `/root/tz08a-work/wt/CryptoReports/TZ-04b-market-recorder-scoring-report.md` | 68,352 | `a18ffd566085cea8f10feba139fadda0f1592f38adddde7e008792c46e8a8e9c` | — |
| `/root/tz08a-work/wt/CryptoReports/TZ-05-quote-capture-report.md` | 12,343 | `ec548d0e1a4b9bf09695d079b7513428b022460a2b411f9c8ee54f4698778daf` | — |
| `/root/tz08a-work/wt/CryptoReports/TZ-05a-quote-capture-deploy-report.md` | 26,565 | `cddca348120ae278f3c399ea21353f57e8b3722f3b0372e247cc985ab1351805` | — |
| `/root/tz08a-work/wt/CryptoReports/TZ-06-pfair-calibration-report.md` | 60,833 | `33863ce6d62443dd070646854b135438ee624c96b5204cd9851cfbca9939396f` | — |
| `/root/tz08a-work/wt/CryptoReports/TZ-07-variance-time-report.md` | 11,745 | `4056137f8de8ef6fa39e43a348a1f60bdfee10f7ffe2c29ebb6e4f6e7894c5b4` | — |
| `/root/tz08a-work/wt/CryptoReports/TZ-07a-variance-time-report.md` | 38,555 | `15c26ec8b7ac670bb136177fd3a87dcd56935077714feff48f833dd08b3af72b` | — |
| `/root/tz08a-work/wt/CryptoReports/TZ-07b-settlement-dispersion-report.md` | 27,788 | `44b2ee1a80c80867aa17bf6b0c378fccbf203655dfc39a7f323861aab4d7cf80` | — |
| `/root/tz08a-work/wt/CryptoReports/TZ-08-out-of-sample-report.md` | 18,738 | `b0d0c8ed31c28bfa52dc449da4a06d33318f17221a6f9d94ce9bcc8f7ecccffe` | — |
| `/root/tz08a-work/wt/CryptoTZ/TZ-01-twap-divergence.md` | 10,121 | `455f58e0616daeacfb67ee7302d84520826780720b5c56c7e7a06463ec63dd57` | — |
| `/root/tz08a-work/wt/CryptoTZ/TZ-01a-twap-divergence-corrected.md` | 8,118 | `a8c4c7c22881236903797e2ffc2d8c87d6e9fc74cd282c7e40feb9eaecab65e3` | — |
| `/root/tz08a-work/wt/CryptoTZ/TZ-02-divergence-distribution.md` | 7,208 | `c8abadec3bb4763a383f397f8ef188cda4228ed1d356f635f8674456d586f2a3` | — |
| `/root/tz08a-work/wt/CryptoTZ/TZ-03-repo-hygiene.md` | 4,657 | `0cd150f54862e6c640510acba90c36f1c351e97d0e9b068a573822455668d56e` | — |
| `/root/tz08a-work/wt/CryptoTZ/TZ-04-market-recorder.md` | 10,008 | `95b2fd8d752a759f7b274aa0fc8ca62b54d9d27d84bc91cc33cc1014c518fe09` | — |
| `/root/tz08a-work/wt/CryptoTZ/TZ-04a-market-recorder-corrected.md` | 12,445 | `fff99e417a5117ab9e5186e793adea8bec9be9140864776a84ef0f7c1f20988b` | — |
| `/root/tz08a-work/wt/CryptoTZ/TZ-04b-market-recorder-scoring.md` | 15,466 | `f4ab08b6a58f84401d38124ff54a665aaa0808a0fb3b376a1362fcb63960effc` | — |
| `/root/tz08a-work/wt/CryptoTZ/TZ-05-quote-capture.md` | 8,506 | `4b9a41fb3301712e6629fb565c47e50a38cb3c85e605122394797ed9094285fe` | — |
| `/root/tz08a-work/wt/CryptoTZ/TZ-05a-quote-capture-deploy.md` | 10,876 | `16f4821308e0f931a469acd0c7d1facffc4c3bb6c75bcd266305d1acc241410b` | — |
| `/root/tz08a-work/wt/CryptoTZ/TZ-06-pfair-calibration.md` | 14,400 | `ec2135c810be9e736946c004b7a4ced0d5a00a322061c89a1519f2d4a30f8373` | — |
| `/root/tz08a-work/wt/CryptoTZ/TZ-07-variance-time.md` | 11,924 | `759d8ed001ed6746a6b7badd430fa1b3b362849594429849cf196bd892342e2b` | — |
| `/root/tz08a-work/wt/CryptoTZ/TZ-07a-variance-time.md` | 14,260 | `0e4852301c493ed7e4cb98d8d880a2c6b42b55f01811976ca9131fc62e61c4e3` | yes |
| `/root/tz08a-work/wt/CryptoTZ/TZ-07b-settlement-dispersion.md` | 15,032 | `476344ccf393c8e3f3eb7a70e97f71af7433a45a02af069978b2e8138c155541` | — |
| `/root/tz08a-work/wt/CryptoTZ/TZ-08-out-of-sample.md` | 14,465 | `bacb45ec2c0a3ed824972fe0b536a99f5ef3bad68e78a5c07fbf0c1a09d77d00` | yes |
| `/root/tz08a-work/wt/CryptoTZ/TZ-08a-out-of-sample.md` | 17,231 | `3c6ea77fabe9716b6bde98cdba728b67cb62a14f8172ac59bffd47dd04f5e687` | yes |
| `/root/tz08a-work/wt/research/pfair.py` | 12,499 | `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` | yes |
| `/root/tz08a-work/wt/research/selftest-pfair.py` | 15,647 | `97de9782d319c82ee6a7d81ddbd8e00d590d85ffe2daa41abe3d71ae92712c94` | yes |
| `/root/tz08a-work/wt/research/selftest-twap-divergence.py` | 16,736 | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `/root/tz08a-work/wt/research/twap-divergence.py` | 50,928 | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `/root/tz08a-work/wt/research/tz02-distribution.py` | 14,511 | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | yes |
| `/root/tz08a-work/wt/research/tz06-calibration.py` | 27,138 | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | yes |
| `/root/tz08a-work/wt/research/tz07a-variance-time.py` | 28,219 | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` | yes |
| `/root/tz08a-work/wt/research/tz07b-settlement-dispersion.py` | 24,926 | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | yes |
| `/root/tz08a-work/wt/research/tz08a-out-of-sample.py` | 38,822 | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | yes |
| `/root/tz08a-work/wt/research/recorder/analyze.py` | 34,705 | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | yes |
| `/root/tz08a-work/wt/research/recorder/config.py` | 4,773 | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | yes |
| `/root/tz08a-work/wt/research/recorder/manifest.py` | 10,002 | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | yes |
| `/root/tz08a-work/wt/research/recorder/probe.py` | 9,324 | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | yes |
| `/root/tz08a-work/wt/research/recorder/recorder.py` | 25,658 | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | yes |
| `/root/tz08a-work/wt/research/recorder/selftest.py` | 30,591 | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | yes |

</details>

## Appendix B — this TZ's scratch outputs named by hash (§5.3)

Everything under `/root/tz09-work/` not listed here is reclaimable once this report is on `main`.

| file | bytes | SHA-256 |
|---|---|---|
| `/root/tz09-work/gate.json` | 8,140 | `ca10945591ffd04057ee51b15243b30f69588a136b303687bfccd65f085654f5` |
| `/root/tz09-work/t0.json` | 294,813 | `c6c163ab0200fd055d864f04933a851911cf8bb968e4fffbae36d18c0e8ccf01` |
| `/root/tz09-work/t0b.json` | 294,816 | `8956ba5509c342a7466161353879496bcfe19a7dd3c4330f98322362af41c332` |
| `/root/tz09-work/v3.json` | 3,866 | `165b9c35ca4e3f076db108cb48db8d05591a146f5d1d73476b88a08bc5398622` |
| `/root/tz09-work/t1.json` | 295,775 | `a09c7df9c997749a403b132cc646b6aa854dc74261f3cd083fe5a9bed95ea64b` |
| `/root/tz09-work/m3.json` | 217,564 | `fdc186632c2275c45f77df6676e40dc298ddd4e82e6c811b58c812d71eaad076` |
| `/root/tz09-work/m6.json` | 798 | `7a7c084276909b258a6fc68a711320f91caae4bb9058588acc8aa13ae3788e0b` |
| `/root/tz09-work/t2.json` | 298,819 | `37590a70483d24a14cfe16d5c2b06af643a89ad66244fab3356102467698b4ae` |
| `/root/tz09-work/m3-post.json` | 217,866 | `66786edc8e818ff188c27dfb99ab2190e59a004e12adb6317b0d353b95613ee5` |
| `/root/tz09-work/r1.json` | 121,573 | `3424b043bcd8a562dabeaed88201916bf99f77838d77f5ccb01760fc397c21a9` |
| `/root/tz09-work/r1-run2.json` | 121,573 | `3424b043bcd8a562dabeaed88201916bf99f77838d77f5ccb01760fc397c21a9` |
| `/root/tz09-work/r1-plan.tsv` | 10,030 | `043a971961011f7d32282ef82a436b99f49ca1a3c608e996f29831668058f29f` |
| `/root/tz09-work/r3-cp.log` | 19,403 | `2b60a43abd55a159c5e5b97355031efb1154359b7d5564ac909626da162b5935` |
| `/root/tz09-work/v6.json` | 51,743 | `abad040d1d57e75e02491fbf55dc8a5008882df6916cd8312b5c96366ed67f0c` |
| `/root/tz09-work/before-r4.json` | 1,081 | `0307104e58b6f54fa036346d79329341496e9e73ce294ef21cc3e1c287f85178` |
| `/root/tz09-work/df-r4-1.json` | 473 | `a78e7866e2b12f813af2fecc3f2409aac3c5d1158342c4bd6e8cbef4ffedbb25` |
| `/root/tz09-work/df-r4-2.json` | 471 | `20e3ecb52bd8ca43c82c0b649244b3d9d266496f21c16a968b0116acbcdcf26a` |
| `/root/tz09-work/df-r4-3.json` | 473 | `aca58323b7effb4bc51f3df319d3258bd1cf8ddf051a8150bda92edac9952258` |
| `/root/tz09-work/df-r4-4.json` | 473 | `2fa3ba1beb0a513d7232775c11c8c9517bdd7ee471d33ec14d8823290dbde574` |
| `/root/tz09-work/df-r4-5.json` | 473 | `38b4573d98f0154918c4f251d212c2b0ff0efa0f30a35e56443c0c585c7a16d7` |
| `/root/tz09-work/after-r4.json` | 1,082 | `d72114f02ad80c1f2c216b5d46a48aabd032b96b88ef6e11241b2aae998ab1b4` |
| `/root/tz09-work/r5.json` | 484 | `cc2804e428fa06de77413cd78279996e46657752178225abb72b0e69a048cd1d` |
| `/root/tz09-work/v7.json` | 113 | `8d4b4e919881fd835d2d7fe4d6497e5e141106635fdf210ec6183706c25520ac` |
| `/root/tz09-work/r4.log` | 2,707 | `9515daf5c66617e83e4b00d17e4c86dc62796db5577966c9e7c85f447a4065b9` |
| `/root/tz09-work/end.json` | 1,082 | `816b4616854fe6e24bf166d729d4b6aa1e029e3ca5f517e8f3a68f41adac9fd8` |
| `/root/tz09-work/v8.json` | 498 | `9ff20385c438234785a873acdcb05b12358f8bcbc3f351caa999e49b4d528ece` |
| `/root/tz09-work/retention.json` | 178 | `9dbfdbe4c4871b1a419e9f124765d41d0a1c9990beb6eb3cd67027b8db1ec674` |
| `/root/tz09-work/v10.json` | 628 | `df8251cfeb5703e4c7f1145909187f0e7a81f246514c55bb06000edbddd3e802` |
| `/root/tz09-work/prefix-script.py` | 38,979 | `8320b91dec2be4a437e61c759eae1e23b012424313460d4f8660245dc8167450` |

## Appendix C — the supplementary read, `t1` → `t2`

This read is not the deciding measurement (§6 item 2). The window was `11440.022` s and the fall `367,521,792` bytes, which is `2,775,683,706` bytes/day. The rule, applied mechanically, names `/root/PROJECT_GAMING_PS5/netaudit/telemetry/captures`. The V5 residual is `0`.

| directory | bytes at `t1` | bytes at `t2` | delta | delta, bytes/day |
|---|---|---|---|---|
| `/` | 23,581,347,840 | 23,948,869,632 | 367,521,792 | 2,775,683,706 |
| `/root` | 10,596,384,768 | 10,958,536,704 | 362,151,936 | 2,735,128,229 |
| `/root/PROJECT_GAMING_PS5` | 8,472,199,168 | 8,833,290,240 | 361,091,072 | 2,727,116,124 |
| `/root/PROJECT_GAMING_PS5/netaudit` | 8,463,044,608 | 8,824,135,680 | 361,091,072 | 2,727,116,124 |
| `/root/PROJECT_GAMING_PS5/netaudit/telemetry` | 8,372,576,256 | 8,733,630,464 | 361,054,208 | 2,726,837,711 |
| `/root/PROJECT_GAMING_PS5/netaudit/telemetry/captures` | 6,896,218,112 | 7,233,556,480 | 337,338,368 | 2,547,725,419 |
| `/root/PROJECT_GAMING_PS5/netaudit/telemetry/logs` | 1,007,222,784 | 1,024,073,728 | 16,850,944 | 127,265,625 |
| `/root/PROJECT_GAMING_PS5/netaudit/telemetry/burst` | 152,842,240 | 158,715,904 | 5,873,664 | 44,360,454 |
| `/var` | 4,207,194,112 | 4,212,576,256 | 5,382,144 | 40,648,282 |
| `/var/lib` | 420,753,408 | 424,984,576 | 4,231,168 | 31,955,613 |
| `/var/lib/btc-recorder` | 110,309,376 | 114,540,544 | 4,231,168 | 31,955,613 |
| `/var/log` | 3,161,137,152 | 3,162,288,128 | 1,150,976 | 8,692,669 |
| `/root/tz09-work` | 2,486,272 | 3,469,312 | 983,040 | 7,424,344 |
| `/root/PROJECT_GAMING_PS5/netaudit/telemetry/line-monitor` | 295,235,584 | 296,148,992 | 913,408 | 6,898,453 |
| `/var/log/nginx` | 1,765,376 | 1,855,488 | 90,112 | 680,565 |
| `/root/.claude` | 99,667,968 | 99,749,888 | 81,920 | 618,695 |
| `/root/.claude/projects` | 89,739,264 | 89,821,184 | 81,920 | 618,695 |
| `/var/log/sysstat` | 6,721,536 | 6,762,496 | 40,960 | 309,348 |
| `/root/PROJECT_GAMING_PS5/netaudit/cake-autorate-logs` | 798,720 | 835,584 | 36,864 | 278,413 |
| `/root/tz09-work/wt` | 1,310,720 | 1,314,816 | 4,096 | 30,935 |

