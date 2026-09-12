# TZ-05 — Quote Capture — REPORT

**Status: BLOCKED.** The §0 fingerprint gate **passes**. The run is blocked because the session in
which the `EXECUTE TZ-05` trigger arrived is not the capture host: `/var/lib/btc-recorder/` does not
exist on it, no recorder process is running on it to be restarted, and egress to every Polymarket
host is refused by network policy. No work was done beyond the gate and the pre-run environment
check: no Tier C code was written, no checkpoint read was issued, no endpoint was fixed from the
documentation, no repair was applied, no branch `tz-05-quote-capture` was created, no file under
`research/` was touched, and nothing was written to `/var/lib/btc-recorder/`.

Executor model: **Opus** (`claude-opus-5`, served by `claude-opus-5`), as the TZ requires.

---

## 0. Fingerprint

Read from `SYSTEM-MAP.md` at `origin/main` = `45ad0721cd6eb601265a3d948c9e164373082618`, working
tree clean.

**Revision string read:** `2026-09-11-b` — TZ-05 requires `2026-09-11-b`. Match.

| anchor | required by TZ-05 §0 | computed | match |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | yes |
| `A2` — collector | `6c5089330629` | `6c5089330629` | yes |
| `A3` — phase | `0-complete / 1-open / 2-not-started` | `0-complete / 1-open / 2-not-started` | yes |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | yes |

`A1` was not copied from the map. The Release asset was fetched anonymously and hashed —
76,818,669 bytes, SHA-256
`229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b` — and the downloaded copy was
then deleted from scratch space. `A2` and `A4` are the first 12 hex characters of the SHA-256
values computed below. `A3` was read from map §5, which records phase 0 as `CLOSED 2026-09-11`,
phase 1 as `open — TZ-06, not yet written`, and phase 2 as `not started`.

### Fingerprint table

`wc -l`, bytes and `sha256sum` for `SYSTEM-MAP.md` and for every file the map's §0 table lists at
authoring time.

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 260 | 19,610 | reported | `c7014c175f411698bc4079eb79b718512c4d52b85256f25bae13b3a7433574d4` | self-reference |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | yes |

All three `frozen` rows match the hashes printed in the map. The §0 gate is clear, and so is the
contract §1.4 check.

---

## 1. The blocker

TZ-05 is a modification of a **running capture process** and is scored against **capture that does
not yet exist**: §3 adds Tier C to "the same process" that has been recording since 2026-09-10 into
`/var/lib/btc-recorder/**`, restarts it, and writes a restart record; §6 then scores the first 200
intervals "whose whole window lies after the Tier C restart record". This session does not run on
that host. It is an ephemeral Firecracker microVM, 209 seconds old when the environment was read,
whose only writable filesystem is `/dev/vda` with `270,553,174,016` bytes total and
`32,207,233,024` free — not map §6's measured `/dev/vda2`, `31,612,203,008` total and
`8,489,132,032` free — which carries none of the shared production services map §6 lists, no
`/var/www`, no `/var/lib/btc-recorder` (the `ROOT` constant of `research/recorder/config.py:10`),
no recorder process, no systemd unit, and Python 3.11.15 rather than the map's 3.12. Three required
inputs are therefore absent and none of them can be produced here. First, there is no process to
restart and no prior capture to extend, so the §3 restart record cannot be written and Tier A
continuity is not merely broken but never began. Second, the §6 scoring set cannot exist: 200
intervals of 300 seconds is `60,000` seconds — 16 h 40 m — of live capture that must run *after*
that restart record, and with it W1, W2, W4, W6 and W7 all have no observations to count. Third,
the network policy of this environment answers `403` to `CONNECT` for `gamma-api.polymarket.com`,
`clob.polymarket.com`, `ws-subscriptions-clob.polymarket.com` and `ws-live-data.polymarket.com`, so
the CLOB order-book endpoint that §3 requires be "read from the current Polymarket documentation at
implementation time" cannot be read, the fourteen checkpoint reads cannot be issued, and the §4
venue parameters cannot be captured. Under `BTC-EXECUTOR-INSTRUCTIONS.md` §9 a required input is
absent, and under §2 that is answered with a BLOCKED report and a full stop; §5.2 forbids writing a
substantive report against an outstanding publication step and §5.3 requires a blocked resource to
be resolved before the run rather than reported after it, so no capture was started, no partial
measurement was taken, and no repair was written — including R-a and R-b, which are §5 repairs to
the same recorder and belong to the same restart.

## 2. Evidence

The host is a fresh ephemeral VM, not the capture host. PID 1 is the microVM's own init, and
systemd is not running at all:

```
$ cat /proc/uptime | awk '{printf "container uptime: %.0f s\n",$1}'
container uptime: 209 s

$ hostname
vm

$ date -u +'%Y-%m-%dT%H:%M:%SZ'
2026-09-12T08:23:08Z

$ timedatectl
System has not been booted with systemd as init system (PID 1). Can't operate.
Failed to connect to bus: Host is down
```

The capture root does not exist, nothing the recorder writes exists anywhere on the filesystem, and
no recorder runs:

```
$ ls -la /var/lib/btc-recorder
ls: cannot access '/var/lib/btc-recorder': No such file or directory

$ find / -xdev -maxdepth 6 -type d \( -name 'btc-recorder*' -o -name 'btc-updown-5m' \) 2>/dev/null
(no output)

$ find / -xdev -maxdepth 8 \( -name 'manifest.json' -o -name '*.jsonl.gz' \) 2>/dev/null \
    | grep -v -e node_modules -e site-packages
/root/.claude/skills/synced/13f27ea5-.../manifest.json
/usr/local/go1.25.1/misc/chrome/gophertool/manifest.json
/usr/local/go1.24.7/misc/chrome/gophertool/manifest.json
/opt/pw-browsers/chromium-1194/chrome-linux/MEIPreload/manifest.json
/opt/pw-browsers/chromium-1194/chrome-linux/PrivacySandboxAttestationsPreloaded/manifest.json

$ ls /etc/systemd/system
getty.target.wants  multi-user.target.wants  redis.service  sockets.target.wants
sysinit.target.wants  timers.target.wants
```

Every userspace process on the box, enumerated by non-empty `/proc/PID/cmdline`. Nothing is
searched for, so — unlike the instrument map §7 item 9 retires — nothing can match the search
itself:

```
     1  /process_api --firecracker-init --addr 0.0.0.0:2024 --max-ws-buffer-size 32768 ...
   481  sbx-telemetry-collector
   482  /bin/sh -c if [ -d /opt/claude-code ]; then ln -sf ...
   486  /usr/local/bin/environment-manager task-run --stdin --session cse_015ChQw5dci...
   562  claude --output-format=stream-json --verbose --settings ...
  2233  /bin/bash -c ...                       # this measurement
  2235  python3 -                              # this measurement
userspace processes: 7
```

Five pre-existing userspace processes, plus the two that are this measurement. The whole process
table is 73 entries; the other 66 are kernel threads. No capture process of any kind exists, and
no systemd unit could start one.

`research/recorder/config.py:10` fixes that path, so it is the path Tier C would extend:

```
ROOT = "/var/lib/btc-recorder"
```

The filesystem is not the one map §6 measured, and there is no second volume that is:

```
$ python3 -c 'import shutil;u=shutil.disk_usage("/var/lib");print(u)'
usage(total=270553174016, used=7573655552, free=32207233024)

$ lsblk
NAME  MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
zram0 253:0    0    0B  0 disk
vda   254:0    0  256G  0 disk /
vdb   254:16   0  9.8M  1 disk /opt/rclone
vdc   254:32   0  236M  1 disk /opt/claude-code
vdd   254:48   0 47.2M  1 disk /opt/env-runner
vde   254:64   0  672K  1 disk /mnt/skills/public
vdf   254:80   0  5.6M  1 disk /mnt/skills/examples

$ ls /var/www
ls: cannot access '/var/www': No such file or directory

$ python3 -V
Python 3.11.15
```

| item | map §6, measured on the capture host | this session |
|---|---|---|
| writable filesystem | `/dev/vda2` | `/dev/vda` |
| total bytes | 31,612,203,008 | 270,553,174,016 |
| free bytes | 8,489,132,032 | 32,207,233,024 |
| capture root present | yes, capturing since 2026-09-10 10:21:09 UTC | absent |
| shared services on the filesystem | `crypto-auto`, `my_real_estate_bot`, `seahome_webapp.git`, `/var/www`, `/var/log` | none present |
| Python | 3.12 | 3.11.15 |

W4 asks for "free space at the restart and at authoring, in exact bytes" and map §6 requires every
floor to be derived from its measured row. Neither number exists here: there is no restart, and the
free-space figure this host reports describes a different filesystem.

The §6 scoring set requires capture time that no session can contain, and which must follow a
restart record that was never written:

```
$ python3 -c 'n=200;s=300;t=n*s;print(t, t//3600, t%3600//60)'
60000 16 40
```

Egress to the venue is refused by this environment's network policy. DNS resolves; the CONNECT is
denied:

```
$ curl -sS -o /dev/null -w 'HTTP %{http_code}\n' --max-time 25 \
    'https://gamma-api.polymarket.com/markets?limit=1'
curl: (56) CONNECT tunnel failed, response 403
HTTP 000

$ curl -sS --max-time 20 "$HTTPS_PROXY/__agentproxy/status"
  "recentRelayFailures": [
    { "kind": "connect_rejected",
      "detail": "gateway answered 403 to CONNECT (policy denial or upstream failure)",
      "host": "gamma-api.polymarket.com:443" },
    { "kind": "connect_rejected",
      "detail": "gateway answered 403 to CONNECT (policy denial or upstream failure)",
      "host": "clob.polymarket.com:443" },
    ...
  ]
```

The same denial applies to `clob.polymarket.com`, `ws-subscriptions-clob.polymarket.com` and
`ws-live-data.polymarket.com`. The anonymous GitHub Release fetch used for `A1` succeeded through
the same proxy — HTTP 200, 76,818,669 bytes — so the denial is host-scoped policy and not a
general loss of egress. Map §6's egress row, verified 2026-09-10 on the capture host, is not
contradicted by this: it describes a different host.

Nothing was created or modified outside `CryptoReports/`. The working tree carried no changes
before this report was written, no branch `tz-05-quote-capture` exists, and the six
`research/recorder/` files are as PR #3 merged them:

```
$ git rev-parse HEAD
45ad0721cd6eb601265a3d948c9e164373082618

$ git status --porcelain      # read before this report file was written
(empty)

$ git ls-tree -r --name-only HEAD research/
research/recorder/analyze.py
research/recorder/config.py
research/recorder/manifest.py
research/recorder/probe.py
research/recorder/recorder.py
research/recorder/selftest.py
research/selftest-twap-divergence.py
research/twap-divergence.py
research/tz02-distribution.py

$ git branch -a
  claude/gifted-hawking-22knfr
* main
  remotes/origin/claude/gifted-hawking-22knfr
  remotes/origin/main
  remotes/origin/tz-04b-market-recorder

$ git status --porcelain
?? CryptoReports/TZ-05-quote-capture-report.md
```

Map §1's file counts hold: eight TZ files, seven reports before this one, three `research/`
scripts, six `research/recorder/` files, `.gitignore`.

One publication fact, stated because it is checkable against the repository and the Architect
verifies every such claim. TZ-05's header sends this report "straight to `main`". The session
harness that runs this Executor is configured with `claude/gifted-hawking-22knfr` as its only
writable branch and forbids a push to any other, so this report is committed there and reaching
`main` is a routing action for the Boss. It carries no implementation commit — there is none — so
the contract §4.1 separation it exists to protect is not at issue.
