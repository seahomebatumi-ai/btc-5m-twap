# TZ-04 — Market and Oracle Recorder — REPORT

**Status: BLOCKED.** The §0 fingerprint gate **passes**. The run is blocked at §4 on the
capture host's free disk space. No work was done beyond the gate and the pre-run resource
check: no recorder was written, no socket was subscribed, no branch was created, nothing
under `research/recorder/` exists, and nothing was written to `/var/lib/btc-recorder/`.

Executor model: **Opus** (`claude-opus-5`), as the TZ requires.

This report is the record of a second execution of TZ-04, triggered after the Architect
published System Map revision `2026-09-10-d`. The previous TZ-04 report — BLOCKED at the
fingerprint gate against revision `2026-09-10-c` — remains in history unedited at commit
`28e4444`, and nothing in it is amended, withdrawn or restated here.

---

## 0. Fingerprint

Read from `SYSTEM-MAP.md` at `origin/main` = `3cd4febaecf29321a5a4246fba5c374433064782`.

**Revision string read:** `2026-09-10-d` — TZ-04 requires `2026-09-10-d`. Match.

| anchor | required by TZ-04 §0 | computed | match |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | yes |
| `A2` — collector | `6c5089330629` | `6c5089330629` | yes |
| `A3` — phase | `0-reopened / 1-reopened / 2-not-started` | `0-reopened / 1-reopened / 2-not-started` | yes |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | yes |

`A1` was not copied from the map. The Release asset was fetched anonymously and hashed:
76,818,669 bytes, SHA-256
`229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b`. `A2` and `A4` are the
first 12 hex characters of the SHA-256 values computed below. `A3` was read from map §5,
which now records phase 0 and phase 1 as `reopened` and phase 2 as `not started`.

### Fingerprint table

`wc -l`, bytes and `sha256sum` for `SYSTEM-MAP.md` and for every file the map's §0 table
lists at authoring time.

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 225 | 13,124 | reported | `e537db2114e9fd52e83d7a6c05c014179cd3747d0c06b3feb0e35e41d3509229` | self-reference |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | yes |

All three `frozen` rows match the hashes printed in the map. The contract §1.4 check passes.
The §0 gate that blocked the previous execution is clear.

---

## 1. The blocker

TZ-04 §4 requires the recorder to "stop cleanly, loudly and without truncating a partial
interval **below 20 GB free**", and TZ-04 §6 requires a continuous **24-hour** proving run
yielding **≥ 280 intervals** before any report. The capture path `/var/lib/btc-recorder/`
resolves to the host's only writable filesystem, `/dev/vda2`, which has **9,620,611,072 bytes
free** — 8.96 GiB, or 9.62 GB decimal. The §4 stop condition is therefore already true before
the first frame is written: a recorder implemented as specified stops at startup and captures
zero intervals, so the §6 proving run cannot begin, let alone complete. The two sections
cannot both be satisfied on this host, which makes the specification unsatisfiable here under
`BTC-EXECUTOR-INSTRUCTIONS.md` §2 and §9. It is not repairable inside TZ-04: lowering or
waiving the 20 GB floor is a threshold change, forbidden by contract §10 "not even to fix an
obvious error"; and freeing the shortfall is both outside this TZ's scope — §2 confines it to
"read-only capture and integrity accounting" — and, as the arithmetic below shows,
insufficient even if every unrelated file on the host were destroyed. Per contract §5.3 a
resource that blocks the run is resolved before the run, not reported after it, so no capture
was started.

## 2. Evidence

The capture path is on the host's only writable filesystem, and there is no second volume:

```
$ df -h /var/lib
Filesystem      Size  Used Avail Use% Mounted on
/dev/vda2        30G   20G  9.0G  69% /

$ stat -c '%m %d %n' /var/lib /root/btc-5m-twap /
/  64770  /var/lib
/  64770  /root/btc-5m-twap
/  64770  /

$ lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sr0     11:0    1 1024M  1 rom
vda    253:0    0   32G  0 disk
├─vda1 253:1    0  512M  0 part /boot/efi
└─vda2 253:2    0 31.5G  0 part /
```

Exact figures, read with `shutil.disk_usage` against the parent of the TZ-04 capture path:

```
$ python3 -c 'import shutil; print(shutil.disk_usage("/var/lib"))'
usage(total=31612203008, used=20555722752, free=9620611072)
```

The block holds under either reading of "20 GB":

| floor as written | floor in bytes | free in bytes | shortfall |
|---|---|---|---|
| 20 GB decimal | 20,000,000,000 | 9,620,611,072 | 10,379,388,928 |
| 20 GiB binary | 21,474,836,480 | 9,620,611,072 | 11,854,225,408 |

The shortfall exceeds what the host can yield. Taking the most generous reading — the decimal
one, a 10,379,388,928-byte shortfall — the sum of every project directory, log tree and web
root on this host unrelated to `btc-5m-twap` is **10,193,259,585 bytes**:

```
$ du -sb /root/PROJECT_GAMING_PS5 /var/log /var/www /root/crypto-auto \
         /root/my_real_estate_bot /root/seahome_webapp.git | awk '{s+=$1} END {print s}'
10193259585
```

Destroying all of it — which no TZ authorizes and which this Executor did not do — would
still leave the host **186,129,343 bytes short of the floor, before the recorder wrote its
first byte**. The filesystem's total capacity, 31,612,203,008 bytes, leaves 11.61 GB above a
20 GB decimal floor when completely empty, and the operating system that must run the
recorder occupies that filesystem too.

Egress was checked before the disk figure was read, and is not the blocker. DNS resolves and
TCP/443 is open to `ws-live-data.polymarket.com`, `gamma-api.polymarket.com`,
`clob.polymarket.com` and `ws-subscriptions-clob.polymarket.com`; an unauthenticated
`GET https://gamma-api.polymarket.com/markets?limit=1` returned HTTP 200. No websocket
subscription was opened, no CLOB or resolution URL was fixed from the documentation, and no
frame was recorded.

Nothing was created or modified outside `CryptoReports/`. No file under `research/` was
touched, no directory `research/recorder/` was created, no branch `tz-04-market-recorder`
exists, `/var/lib/btc-recorder/` was never created, and the scratch directory used for the
`A1` download was removed:

```
$ ls research/
out
__pycache__
selftest-twap-divergence.py
twap-divergence.py
tz02-distribution.py

$ git status --porcelain
?? research/__pycache__/

$ git branch -a
* main
  tz-01-twap-divergence
  tz-01a-twap-divergence-corrected
  tz-02-divergence-distribution
  tz-03-repo-hygiene
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
  remotes/origin/tz-01-twap-divergence
  remotes/origin/tz-01a-twap-divergence-corrected
  remotes/origin/tz-02-divergence-distribution
  remotes/origin/tz-03-repo-hygiene
```

`research/__pycache__/` is pre-existing and untracked; it predates this execution and was not
created, modified or committed by it.
