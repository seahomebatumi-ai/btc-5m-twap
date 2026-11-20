# TZ-50 — L1, the bot's account and one order's round trip from the live host in Sofia: the client installed offline at pinned hashes, a session key made on the host and authorized by the owner's signature on his own device, the wallet's pUSD approved to the venue's two exchanges at 1 pUSD each where short, one post-only buy of 5 shares at 0.01 placed and cancelled — and the bot's Telegram token and chat, and the Boss's own SSH key

**Canonical filename:** `TZ-50-l1-account-round-trip.md`. The committed file takes this name and no other.

**Executor model: Claude Opus 5.5.** Two hosts, keys of a venue made and authorized, an authenticated order path proved with money in the wallet, and the Boss's hands in the run at three points.

**Required System Map revision:** `2026-11-20-a` — **it ships with this TZ:** the Boss uploads `SYSTEM-MAP.md`, this file and `docs/l1-sign.html` in one upload onto `main` at `234a6e8`, which carries revision `2026-11-19-b`. The revision adds one `frozen` row, `docs/l1-sign.html` — this TZ's Appendix B — moves no other row and no anchor, and replaces no row (CANON hard rule 17); this TZ's merge adds `research/tz50-l1-account.py`, which the map revision attached to its verdict carries.

**Map sections this TZ rests on**, copied from §10's C8 (map §7 item 174): §0, the fingerprint gate, its table and the signing page; §1, the repository and its TZs; §2.6, the reward book — its store's bounds and its reserve; §3, the units, the trees on the host and the session directories; §5, L1's row and the reward book's days; §6, its rows host identity, for TZ host gates; live host; live host identity, for TZ host gates; live host — the venue's geoblock, measured 2026-11-19, TZ-48 and TZ-49; live host — the venue's CLOB from Sofia; language; git remote; egress; venue edge — the `User-Agent`; venue constants; maker incentives; RTDS session limit; disk; disk floors and caps; memory; clock; sandbox limit — destructive actions; and harness — background output; §7 items 86, 89, 91, 95, 98, 119, 124, 127, 132, 137, 138, 140, 143, 144, 150, 156, 163, 169, 174, 175, 176, 177, 180, 181, 183, 184, 185, 186, 187 and 188; §8. **And TZ-49's report**, `CryptoReports/TZ-49-live-host-ipv4-keys-report.md` on `main`, its §1 and §2, whose host this TZ starts from.

**Required anchors**, from map §0. A mismatch on any one is BLOCKED before any work:

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `6ac6e10aeabc` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

**Host gates:** §0.3, the capture host, where the Executor runs and the branch is made, and of whose capture nothing is touched; §0.6, the live host, reached as `live-host`.

**Written authorization — contract §10.** This TZ authorizes, in writing and nothing beyond it: from the live host, IPv4 alone, through the venue's official client `polymarket-client` `0.20.0` and the instrument's own calls — the relayer's reads and the owner's two signed batches of §3.7, an authorization of the session key and, where an exchange's allowance is short, an approval of `1` pUSD to it; the CLOB's authenticated reads by the session key; **one order** — a post-only, good-till-cancelled buy of `5` shares at `0.01` of the five-minute market open at that instant, on its `Down` side where its `Up` side's would cross the book, so two placements at most — read back, cancelled by its id and read back, and `cancel_all` of the key as the round trip's last act; `/balance-allowance/update`, the venue's refresh of its own view; the Polygon RPC's `eth_call` reads of the wallet's pUSD balance and allowances; and Telegram's `getMe`, `getMyCommands`, `getUpdates` and one `sendMessage`. **This TZ's whole loss is at most `0.10` pUSD** — two orders of `5` shares at `0.01` filled, which a post-only order resting at the lowest price does not expect (§1.5). Nothing else is signed, sent or spent; no withdrawal, transfer, deposit or allowance beyond those is made by any code of this run.

**Before `EXECUTE TZ-50`:** the Boss uploads, in one upload onto `main`, `SYSTEM-MAP.md` to the root, this file to `CryptoTZ/` and `docs/l1-sign.html` to `docs/` — the three files the run needs (CANON hard rule 10) — and nothing else. **Every other step of his sits inside the run, at the point that needs it, with a bound** (map §7 item 132): **B-PAGES**, §3.5, where GitHub Pages is not turned on by `gh`; **B-ACCOUNT**, §3.7 — on polymarket.com with the bot's MetaMask account: the withdrawal allowlist, a Relayer API key and a deposit; in Telegram, `/start` to his L1 bot — and **B-OWNER**, §3.7, one paste in his terminal on the capture host: the bot's token and the Relayer API key typed hidden, his own SSH public key, and two signatures in MetaMask's own browser. **The Boss reaches the live host as he does now** — `ssh live-host` as root on the capture host, or the provider's console; B-OWNER adds his own key where he gives one (§1.8).

**When: begun at any hour.** No reading of this TZ moves with the capture host's package-manager morning (map §6, process supervision; §7 items 143 and 176), so it keeps no band clear of it: the room is printed with no threshold, and no capture's state gates the run. **The run waits for the Boss** — at most `60` minutes for B-PAGES and `8` hours for B-ACCOUNT and B-OWNER (§3.5, §3.7) — beside about `50` minutes of its own (§6). **The venue changes under it, and the run is written for both sides of each change** (map §7 items 186 and 187): the fees and rebates at 2026-11-20 23:59 UTC, which a post-only order that does not fill never meets; and Polymarket Protocol V2 for the BTC five-minute markets from 2026-11-24, which the round trip reads from the market's own document and trades on either protocol (§1.5).

**What this TZ is.** L1's next step after TZ-49 (CANON PART II, L1; map §5, L1; §7 item 169): **the bot's account, its keys and one order's round trip at the minimum size, from the live host in Sofia, before any unit exists.** The venue's official client — `polymarket-client` `0.20.0`, the venue's own Python SDK — is installed on the live host from 35 wheels fetched over IPv4 and checked by size and SHA-256, into `/root/l1-env`; a session key — an Ethereum key that can sign the CLOB's orders and cannot withdraw (§1.2) — is made there, written once, `0600`, root's, never printed; the Boss authorizes it with his owner key, which never leaves his MetaMask, by signing one batch on **the signing page**, `docs/l1-sign.html`, served by GitHub Pages and making no request of its own (§1.3); where the wallet's pUSD allowance to either of the venue's two exchanges is under one order's cost, he signs a second batch approving `1` pUSD to it, and no more (§1.4); and one post-only buy of `5` shares at `0.01` is placed, read, cancelled and read through the session key (§1.5). The bot's Telegram token — he has made the bot — is written on the host by him alone, its chat pinned by his `/start`, and the round trip's report sent there (§1.7). His own SSH public key is added to root's where he gives one, so that Termius reaches the live host by key (§1.8). One instrument, `research/tz50-l1-account.py`: Appendix A; the page: Appendix B. **No unit is deployed and no process outlives the run** (CANON hard rule 14); L1's unit, its loss limit and its Telegram control panel — «Стоп» — are the next TZ's (map §7 item 184).

---

## 0. Gates

### 0.0 The readiness, then the work tree

After contract §1 steps 1 and 2, and before anything else, in the session — verbatim, read-only:

```
/root/tz04a-env/venv/bin/python -B - <<'EOF2'
import os, time
now = int(time.time())
v = os.statvfs("/var/lib"); free = v.f_bavail * v.f_frsize
with open("/proc/meminfo", encoding="utf-8") as fh:
    mem = [int(ln.split()[1]) * 1024 for ln in fh if ln.startswith("MemAvailable:")][0]
ready = free >= 7795535636 and mem >= 85051706
print("ready=%d: %d bytes free on /var/lib, 7795535636 needed; MemAvailable %d, 85051706 needed; at %d %s" % (ready, free, mem, now, time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now))))
EOF2
```

**`ready=1` begins the run. `ready=0`, or a read that ends without its `ready=` line, begins nothing:** no directory is made, nothing is written, committed or pushed and no report is written — this TZ has not executed (CANON hard rule 5) — and the Executor gives the Boss the read's line as printed and, in one line, in Russian, that `EXECUTE TZ-50` is sent again an hour later. This is not BLOCKED and owes no report (contract §5). Then:

```
mkdir /root/tz50-work /root/tz50-work/logs; echo "exit=$?"
```

`exit=0` proves neither existed; anything else is BLOCKED. The readiness read is run again into `logs/00-ready.log`. **From here every command's output goes to a log, one file per step, under the names §3's table fixes** — the capture host's under `/root/tz50-work/logs/`, the live host's under its own `/root/tz50-work/logs/` until §3.10 copies them — and nothing to the session's scratchpad; B-RECLAIM-OWN, §9, is the one exception (map §7 item 89).

Seven abbreviations, written out in full in every block handed to the Boss:

- **`P`** — `nice -n 19 /root/tz04a-env/venv/bin/python -B`, on the capture host.
- **`I0`** — `P /root/tz50-work/stage/research/tz50-l1-account.py`, the staged copy, for §0 alone.
- **`I`** — `P /root/tz50-work/wt/research/tz50-l1-account.py`, the committed copy, from §3.1 on.
- **`R 'X'`** — `ssh -T -o BatchMode=yes -o ConnectTimeout=20 -o LogLevel=QUIET live-host 'export LC_ALL=C; X'`: the command `X` on the live host under the C locale (map §7 item 185), never asking for anything — a terminal included — and never printing an error of its own, whose text would carry the host's address (§2 item 5); its exit tells. **It is a new connection by the Executor's key every time.**
- **`L M NN`** — the live host's standard-library mode `M` — quoted where it carries its argument, `'host before'` — into its log `NN`: `R 'cd /root/tz50-work && { date -u +%FT%T.%NZ; /usr/bin/python3 -B /root/tz50-work/tz50-l1-account.py M; echo "exit=$?"; } >> /root/tz50-work/logs/NN.log 2>&1; tail -n 60 /root/tz50-work/logs/NN.log'`.
- **`LC M NN`** — the same, the client's mode `M` under `/root/l1-env/bin/python -B` in place of `/usr/bin/python3 -B`.
- **`S`** — the scratchpad directory the session's system prompt names (map §7 item 98's form).

**`L` and `LC` run with the session's tool timeout at its maximum, 600 s.** A mode whose wait can pass it — `wheels`, `page`, `find-chat`, `roundtrip` — runs in the background with its `echo "exit=$?"`, the harness keeping a background command's output (map §6, harness — background output), and its log is read with `R 'tail -n 60 /root/tz50-work/logs/NN.log'` at most every 570 s until that line; a log that stops without it is read again once, and then BLOCKED. **Where the classifier refuses an `L` or `LC`**, its paste is the quoted part alone, run by the Boss in a terminal on the live host — `ssh live-host` as root on the capture host — and the Executor reads its log and runs none of it again (map §7 item 144). Every mode of the instrument runs from `/root/tz50-work` on its host — `main` asserts it (lines 3060 to 3091) — and prints its peak memory, its hook's refusals and its counts on every exit.

### 0.1 The instrument and the page, staged

Extract Appendices A and B from this TZ as the primary checkout carries it after contract §1's pull, with this script, verbatim, its one argument the destination, its output into `logs/01-stage.log`:

```
/root/tz04a-env/venv/bin/python -B - /root/tz50-work/stage <<'EOF2'
import hashlib, os, sys
SRC = "/root/btc-5m-twap/CryptoTZ/TZ-50-l1-account-round-trip.md"
DEST = sys.argv[1]
WANT = {"research/tz50-l1-account.py": "6943b54d5fb7824b9dbd467b53f8f7568ecb9851ff707399c9fe759a584617a4",
        "docs/l1-sign.html": "f1d92e7dd8a8cd15b7b96b86b357ebf80db4e10844b3fc269e92cef0aecba528"}
with open(SRC, encoding="utf-8") as fh:
    lines = fh.read().split("\n")
found, i = {}, 0
while i < len(lines):
    if lines[i].startswith("```") and " file=" in lines[i]:
        name, j = lines[i].split(" file=", 1)[1].strip(), i + 1
        while lines[j] != "```":
            j += 1
        found[name] = ("\n".join(lines[i + 1:j]) + "\n").encode("utf-8")
        i = j
    i += 1
assert sorted(found) == sorted(WANT), sorted(found)
for name in sorted(found):
    data = found[name]
    assert hashlib.sha256(data).hexdigest() == WANT[name], name
    path = os.path.join(DEST, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        with open(path, "rb") as fh:
            assert fh.read() == data, path + " exists with other bytes"
        print(path, data.count(b"\n"), len(data), hashlib.sha256(data).hexdigest(), "equal, kept")
        continue
    with open(path, "xb") as fh:
        fh.write(data)
    print(path, data.count(b"\n"), len(data), hashlib.sha256(data).hexdigest(), "created")
EOF2
```

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/tz50-l1-account.py` | 3,091 | 174,674 | `6943b54d5fb7824b9dbd467b53f8f7568ecb9851ff707399c9fe759a584617a4` |
| `docs/l1-sign.html` | 218 | 11,846 | `f1d92e7dd8a8cd15b7b96b86b357ebf80db4e10844b3fc269e92cef0aecba528` |

A failed assert or another hash is BLOCKED; here both lines read `created`. The staged instrument runs §0.2's `fingerprint`, §0.3's `room`, §0.5's `number` and `refs`, §0.6's `methods`, and is the copy §0.6 sends to the live host; the staged page is compared with `main`'s by `fingerprint`, and never committed by this run — it reached `main` in the Boss's upload.

### 0.2 Fingerprint

`I0 fingerprint`, into `logs/02-fingerprint.log`, performs contract §1 steps 3 and 4 inside the instrument and asserts them, against `SYSTEM-MAP.md` and the files of its §0 table in the primary checkout `/root/btc-5m-twap`: revision `2026-11-20-a`; the six anchors; `A2`, `A4`, `A5` and `A6` re-derived as the first 12 hex characters of those files' SHA-256; the table's **67** rows, each printed in lines, bytes and SHA-256 — **64** `frozen` rows asserted equal to the map, `docs/l1-sign.html` among them, **2** `tracked` and **1** `reported`; the map's own lines, bytes and SHA-256; and `docs/l1-sign.html` on `main` asserted equal to Appendix B by its bytes and SHA-256 (`mode_fingerprint`, lines 1057 to 1092). It prints `FINGERPRINT PASS` or stops at the first mismatch, which is BLOCKED — the upload without the map, or without the page, among them.

### 0.3 Host gate — the capture host

From `/root/btc-5m-twap`, output verbatim into `logs/03-host-gate.log`:

```
date -u; date -u +%s; uptime -s; nproc; grep -E '^(MemTotal|MemAvailable|SwapTotal|SwapFree):' /proc/meminfo
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
grep -c e3975b5da44c5328adf3bf3914634cd878842c73 /var/lib/btc-recorder/runtime.jsonl
/root/tz04a-env/venv/bin/python -c 'import sys; print(sys.version.split()[0])'
command -v ssh scp gh
TZ=UTC systemctl show btc-recorder.service btc-rewardbook.service adv3-bot.service btc-rewardbook-archive.service btc-rewardbook-archive.timer -p Id -p MainPID -p NRestarts -p ActiveState -p UnitFileState -p ActiveEnterTimestamp
du -sb /var/lib/btc-rewardbook /root/btc-forensics /root/.claude-8j 2>&1; find /root/btc-forensics -type f | wc -l
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
test -e /root/tz49-work; echo "/root/tz49-work exit=$?"
test -e /root/.ssh/live-host; echo "/root/.ssh/live-host exit=$?"
git -C /root/btc-5m-twap worktree list
echo "$S"; ls -la "$(dirname "$(dirname "$S")")"
```

then the memory gate's own reads, appended to the same log:

```
for k in 1 2 3 4 5; do m=$(( $(awk '/^MemAvailable:/ {print $2}' /proc/meminfo) * 1024 )); echo "MemAvailable read $k $(date -u +%T): $m"; [ "$m" -ge 85051706 ] && break; [ "$k" -lt 5 ] && sleep 60; done
```

- **H1** — `find` prints exactly one path.
- **H2** — `df` names source `/dev/vda2` and size `31612203008` (map §6, disk); `grep -c` prints at least `1`. With H1 this is map §6's host identity (map §7 item 86).
- **H3** — the interpreter prints `3.12.`.
- **H4** — `command -v` prints three paths, one each for `ssh`, `scp` and `gh`: the access's tools and the one §3.5 turns Pages on with.
- **Memory gate** — the last `MemAvailable read` at least `85,051,706` bytes: a read below it is read again 60 s later, five reads at most, the first at or above it passing (§0.4; map §7 item 137).
- **Disk gate** — `avail` at least `7,795,535,636` bytes, §0.0's bound read again (§0.4).

These are seven checks — H2 two — and any one failing is BLOCKED. **The rest is printed and carries no threshold:** the units this TZ leaves alone, whose states the closing reads print again (§3.10); the reward book's store, the forensic store and its count and the sessions' configuration directory by `du` (map §2.6); the consumer's two states, on which map §6's headroom is conditional; `/root/tz49-work` gone, as TZ-49's report read it; the Executor's key, which TZ-47 made; the worktrees, map §3's two; and the listing of the directory that holds the session's own (map §7 item 150). Then `I0 room`, into `logs/04-room.log` (`mode_room`, lines 1134 to 1153): `btc-rewardbook-archive.service` read until it reads `inactive`, at most 30 reads 60 s apart — still running at the last read, the room is not read — then free space on `/var/lib`, the reward book's stream files by their directory entries alone, the room and **its margin over `STREAM_FLOOR` and `PEAK`**, printed, no threshold, as map §7 item 175 asks of every TZ that touches the host; a margin under `1,000,000,000` is flagged in the line itself. **Its wait can pass one call's 600 s:** it runs in the background with `echo "exit=$?"` after it, and its log is read at most every 570 s until that line.

### 0.4 Resource floors, in exact bytes

**The capture host's disk: `7,795,535,636` bytes available on `/var/lib`, at §0.0 and §0.3 and at the start of `room`** (`CAPTURE_FLOOR`, line 284): the reward book's `STREAM_FLOOR`, `7,300,000,000`, below which no stream of it opens for a slot (`research/tz33-reward-book-capture.py` line 190), plus `PEAK`, `445,535,636`, the most its store holds between two runs of its archive (map §6, disk floors and caps), plus `50,000,000`, this session's writes there at most — the worktree, `main`'s 187 files of about `16,600,000` bytes with this TZ's upload and the instrument; the stage, under `200,000`; both hosts' logs, under `5,000,000`. **The live host's disk: `2,447,483,648` bytes available on `/` at the start of `host`, `geoblock`, `page`, `wheels`, `secrets`, `key`, `authorize`, `approve`, `ready` and `roundtrip`** (`LIVE_FLOOR`, line 288): journald's `SystemKeepFree`, `2,147,483,648`, under which the journal itself writes nothing (TZ-49 §1.5); the client's tree, `200,000,000` at most — `47,855,239` bytes installed by the Architect from the same 35 wheels; and the live work tree, `100,000,000` at most — the wheels, `14,422,773` bytes, and the logs. The live host read `16,987,521,024` to `16,987,779,072` bytes available at TZ-49 (map §6, live host).

**Memory: `MemAvailable` at least `85,051,706` bytes at §0.0 and §0.3 and at the start of every standard-library mode that reads the floors on either host, and at least `275,045,368` at the start of every client mode that does** (`MEM_FLOOR` and `MEM_FLOOR_SDK`, lines 290 and 291; `floors`, lines 523 to 537): each twice the host peak modelled from the largest of the Architect's runs of its kind at the ratio TZ-37 measured between a host's peak and the Architect's for one code, `58,953,728 / 49,168,384` (map §6, memory; §7 item 156) — `selftest`, `35,467,264` bytes at the largest of the Architect's runs on these bytes, the largest of the standard-library modes, and `sdk-selftest`, `114,696,192` at the largest of its runs, the client's modes importing the same client, under Python 3.12 on these bytes but for the two floors' own values: so `42,525,853` and `137,522,684` modelled. A read below the floor is read again every 60 s, five reads at most, the first at or above it passing and five below it BLOCKING (map §7 item 137). The capture host's `MemAvailable` read `136,404,992` to `562,360,320` across the TZs since 2026-10-31 (map §6, memory); the live host's `MemTotal` is `1,944,465,408` (map §6, live host). Every mode runs under `nice -n 19` on the capture host: it has one processor.

### 0.5 Refs and the number

`I0 number`, into `logs/05-number.log`, and `I0 refs`, into `logs/05-refs.log`, after §0.4; both again in §3.1. **NUMBER — CANON hard rule 2:** `I0 number` reads `git ls-tree --name-only origin/main -- CryptoTZ/ CryptoReports/` in the primary checkout and must print `NUMBER PASS - 2 of 2`: `CryptoTZ/` holds `TZ-50-l1-account-round-trip.md` and no other file whose name begins with `TZ-50-`, and `CryptoReports/` no report whose name does (`number_reading` and `mode_number`, lines 745 to 750 and lines 1095 to 1103; map §7 item 127). Anything else is BLOCKED. `CryptoTZ/` and `CryptoReports/` end at TZ-49's files on `main` at `234a6e8`, so this TZ's number is 50. **`I0 refs`** prints `HEAD` and `refs/heads/main` and every other ref counted by kind — never every tag (map §7 item 177) — and BLOCKS where `refs/heads/tz-50-l1-account-round-trip` exists (`refs_reading` and `mode_refs`, lines 753 to 772 and lines 1106 to 1117). The reward book's archive adds a tag every three hours and the Boss's upload a commit: the report names each kind whose count differs from map §1's read and `main`'s new commit — a difference is recorded, not BLOCKING.

### 0.6 The live host — access, its gate, the geoblock and root by key, before any key of a venue exists

**Access**, into `logs/06-access.log`:

```
R 'true'; echo "exit=$?"
ssh-keygen -lf /root/.ssh/live-host.pub
ssh -G -T live-host | grep -E '^(user|hostkeyalias|identityfile|identitiesonly|serveraliveinterval) '
ssh-keygen -lF live-host
R 'hostname -s; id -un; test -e /root/tz50-work; echo "work tree exit=$?"; test -e /root/tz49-work; echo "tz49 tree exit=$?"'
```

**`exit=0`, the pinned key `ED25519` `SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw`, TZ-47's, and the last read `vs-2348`, `root`, `work tree exit=1` and `tz49 tree exit=1`; anything else is BLOCKED** — the access is TZ-47's and TZ-49 left it standing (map §6, live host; TZ-49's report §2), and root takes no password there now, so no paste of the Boss's can make it again. The alias's `hostname` line is never printed (§2 item 5). **The copy**, into `logs/07-copy.log`:

```
R 'mkdir /root/tz50-work /root/tz50-work/logs; echo "exit=$?"'
scp -q -o BatchMode=yes -o LogLevel=QUIET /root/tz50-work/stage/research/tz50-l1-account.py live-host:/root/tz50-work/tz50-l1-account.py; echo "scp exit=$?"
R 'sha256sum /root/tz50-work/tz50-l1-account.py; wc -lc /root/tz50-work/tz50-l1-account.py'
```

`exit=0`, `scp exit=0`, and §0.1's line count, bytes and SHA-256 — anything else is BLOCKED. **The live host's gate:** `L 'host before' 40-host-before` (`mode_host`, lines 1286 to 1316): TZ-49's five checks of `live_gate` (lines 809 to 817) — **LH1** the host name's first label `vs-2348` (map §7 item 180), **LH2** Ubuntu 24.04, **LH3** Python 3.12, **LH4** neither `/var/lib/btc-recorder` nor `/root/btc-5m-twap` present, **LH5** TZ-47's pinned key among the host's own SSH host keys — and §0.4's floors: any failing is BLOCKED, `exit=1`. **Every live mode but `host`, which reads all five, and `selftest`, `sdk-selftest` and `env`, which change nothing of the host, begins with LH1, LH5 and LH4 again** (`is_live_host` and `assert_live`, lines 611 to 617). It prints the host's facts — the kernel, the memory, the disk, `/etc/default/locale` and `locale` once (map §7 item 185), the clock by `timedatectl show`, root's authorized keys by fingerprint, and every L1 path's state by kind, mode, owner and size, never a file's content: at this read every one of them absent. **The geoblock, before any key of a venue exists** (CANON PART IV): `L geoblock 41-geoblock` (`geo_read` and `mode_geoblock`, lines 1319 to 1347): **G-GEO** (§4.1), over IPv4 alone, at most three reads 30 s apart while unread. `exit=0` PASS; **`exit=1` is BLOCKED** — the venue blocks this address or did not read it — and the run goes to §3.10's copy and §9, nothing having changed on the live host but its work tree. **Root by key alone, as TZ-49 left it:** `L sshd 42-sshd` (`mode_sshd`, lines 1350 to 1362) — **G-SSH K1 to K5**: TZ-49's drop-in byte for byte and `0644`, and `passwordauthentication no`, `kbdinteractiveauthentication no`, `permitrootlogin without-password` and `pubkeyauthentication yes` in force by `sshd -T` — and, into `logs/08-methods.log`, `{ date -u +%FT%T.%NZ; I0 methods gate; echo "exit=$?"; } >> /root/tz50-work/logs/08-methods.log 2>&1` (`mode_methods`, lines 1156 to 1172) — **K6**: one connection from the capture host that offers no key and can answer no prompt, of whose text the mode prints the methods the live host's sshd offers root and nothing else, which must be `['publickey']`. A FAIL of any of the six is BLOCKED: TZ-49's state does not stand, and no credential of L1 is written to a host whose root takes a password.

---

## 1. Why this TZ exists, and what it decides

**The venue's terms below were read by the Architect from `docs.polymarket.com` and the client's own source on 2026-11-19 and 2026-11-20, and are not measured; this run measures the ones its gates name.** Pages: `/trading/session-keys`, `/trading/wallets-auth`, `/trading/place-orders`, `/trading/manage-orders`, `/migrate/polymarket-v2/overview` and `/sdk-integrations`, `/programs/fee-and-rebate-changes-november-2026`, `/changelog/sdks` and `/changelog/predictions`; the help centre's *Withdrawal Allowlist*, `help.polymarket.com/en/articles/18323576`; and `polymarket-client` `0.20.0`'s source, the wheel of Appendix A's set.

### 1.1 The step

CANON PART II's L1 opens on TZ-45's EARN: rule W live at the minimum size from the live host in Sofia, its whole loss fixed in its TZ, each step a TZ of its own (map §7 item 169). TZ-49 prepared the host — the venue's geoblock read `BG`, not blocked, over IPv4 alone; root by key alone; its swap and its journal (map §6, live host). **This TZ is the step before any unit:** the account the unit will trade from, its keys, and one order's round trip through them — because CANON PART IV's trap, `signature_type` and the client's version, authenticates first and fails at the order, and only a live order's round trip proves the path. It also carries the two things the Boss asked for with it (§1.7, §1.8).

### 1.2 The account: who holds what — decided, CANON PART IV

- **The owner** is an account of MetaMask kept for the bot alone, on the Boss's own device; its key never reaches any host of this project and signs only there. **The bot's wallet** is that owner's Polymarket **Deposit Wallet** — the account type of every account the venue has created since 2026-05-04, its address derived from the owner's (the client's `derive_uups_deposit_wallet_address` and `derive_beacon_deposit_wallet_address`), deployed by the venue when the account is made on polymarket.com.
- **The session key** is an Ethereum key — an EOA — that the owner authorizes on the wallet for 180 days with scope `CLOB`: it signs the CLOB's orders for the wallet and **cannot withdraw** — it executes no wallet transaction, a withdrawal or an approval among them. It is made on the live host by `eth_account` from `os.urandom`, written once, `0600`, root's, to `/etc/l1-bot/session-key`, and never printed, hashed or copied (`mode_key`, lines 2005 to 2022). **Its revocation is the stop of every order path:** revoking it cancels its open orders and ends its signing (§4.11, B-REVOKE).
- **The owner's Relayer API key**, made by the Boss on `polymarket.com/settings?tab=api-keys` for the owner's address, lets the venue's relayer accept a batch the owner signed — an authorization, a revocation, an approval — and pays its gas. It moves nothing by itself: every batch it carries is signed by the owner on his device. It is typed by the Boss, hidden, into `/etc/l1-bot/relayer-key`, `0600`, root's, with the owner's address beside it, and never printed (`mode_secrets`, lines 1473 to 1526).
- **The withdrawal allowlist** is turned on before the first deposit: on polymarket.com, *Settings → Account → Withdrawal allowlist*, with an email for its codes; Polygon addresses only, and neither the login wallet nor the Deposit Wallet; on at once, any later change taking 48 hours. **With it, money leaves the wallet only to an address the Boss saved** — whoever holds the session key, or the host.
- **The immediate stop, needing no host:** the Boss withdraws the wallet's pUSD on polymarket.com to his saved address, signing in MetaMask — an empty wallet trades nothing. B-REVOKE is the stop of the key itself.

### 1.3 The signing page — decided

**The owner signs on his own device, and no host holds his key**, so his signature is made in MetaMask from a page: **`docs/l1-sign.html`, Appendix B**, served by GitHub Pages from `main` at `https://seahomebatumi-ai.github.io/btc-5m-twap/l1-sign.html` — this repository is public, and GitHub serves the page's bytes over HTTPS. **The instrument prints a link** whose fragment — after `#`, which no request carries — holds the operation and its fields; the page shows them, asks MetaMask to switch to Polygon, chain `137`, and to sign the Deposit Wallet's EIP-712 `Batch` as the owner, and shows the signature, which the Boss copies back into his terminal. **The page makes no network request of its own** and holds no key; **no field of a link can name another contract, spender or amount** — an approval names its exchanges by letter, `c` or `v`, and the page alone holds their addresses and the amount, `1` pUSD; the instrument recovers the signature to the owner under the client's own typed data before anything is submitted (`ask_signature`, lines 1823 to 1851), so a page that signed anything else is refused before the relayer sees it. **Tested by the Architect, 2026-11-20:** nine links of the three operations — authorize, revoke, and approve of `c`, `v` and `cv` — gave typed data whose digests equal the client's `build_deposit_wallet_typed_data`, signed by MetaMask's own library `@metamask/eth-sig-util` `8.2.0` and recovered to the owner; fifteen malformed links refused; and in a DOM stand-in, `jsdom`, with a stand-in of MetaMask's provider, the page signed on Polygon, switched a chain, refused another account, an expired link and a broken one, and signed an approval of the two exchanges. **GitHub Pages is not turned on today** — the Architect read `404` at the site and the page on 2026-11-20 — so §3.5 turns it on for `main`'s `docs/`: by `gh`, or by the Boss's four clicks.

### 1.4 The approvals — decided: `1` pUSD to each exchange whose allowance is short, never the maximum

A buy is taken from the wallet's pUSD by the exchange that matches it, which must hold an allowance; **an approval is a wallet transaction, which only the owner signs** (§1.2). **Two exchanges are in play** (map §7 item 186): the standard exchange, `0xE111180000d2663C0091e4f400237545B87B996B`, for a CTF market, and the V2 exchange, `0xe3333700cA9d93003F00f0F71f8515005F6c00Aa`, for a Protocol V2 market — the venue's table, and the client's `standard_exchange` and `exchange_v3`, asserted equal in `client` (lines 1697 to 1739). The BTC five-minute markets move to V2 from 2026-11-24, so the run cannot know which one its order meets. **`approve`** reads both allowances on chain — `allowance(wallet, exchange)` on pUSD, `0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB` — and, for each under one order's cost, `50,000` units, asks the owner to sign one batch of `approve(exchange, 1,000,000)` — `1` pUSD — submitted through his Relayer API key (`approve_flow`, lines 1915 to 1982); where none is short it asks nothing. **The bound is the reason:** an allowance is what an exchange can take from the wallet for orders the wallet's signers sign, so `1` pUSD bounds what a stolen session key can spend through each exchange until L1's unit TZ approves its own budget, inside its own loss limit. polymarket.com may have set larger allowances when the account was made — the site prompts for its own approvals — and then nothing is signed here; what the run read is printed and recorded.

### 1.5 The round trip — decided

**One order, the smallest the venue takes, at the price that does not expect a fill:** a buy of `5` shares at `0.01` — the BTC five-minute family's minimum size and the lowest price on either of its ticks (map §6, venue constants) — post-only, good-till-cancelled, on the five-minute market open at that instant (`roundtrip_flow`, lines 2178 to 2278). **Why this market:** it has no liquidity rewards (map §6, maker incentives), so a resting order of ours there touches no reward book, and its document is read for its identity alone — slug, flags, outcomes, IDs and condition, and its `version` — no price, size, rate or outcome (§2 item 5). **Its window must keep `150` s at placement**, or the run waits for the next. **Post-only** means the venue refuses an order that would cross the book: where `Up`'s best ask is already `0.01` its buy is refused as `post_only_would_cross`, and the run places on `Down`, whose ask is then near `0.99` — the two cannot both cross, so **two placements at most**, and a placement refused for anything else ends the round trip. **The order is read back live** — `LIVE`, `0.01`, `5`, `BUY`, `GTC`, nothing matched, its maker the wallet and its asset the token — **cancelled by its id, read back cancelled with nothing matched**, the key's and the wallet's open orders read none, and the wallet's pUSD on chain read equal before and after; **`cancel_all` of the key is its last act whatever happened.** A market resolving under a resting order cancels it at the venue. **The whole loss is at most `0.10` pUSD** — two orders of five shares at one cent filled, whose shares then settle at zero (`RT_LOSS_MAX_UNITS`, line 267). **Both protocols:** a CTF market's document trades its `clobTokenIds` through the standard exchange; a V2 market's — `version` `"v2"` — its `positionIds` through the V2 exchange, signed under domain version `"3"`; the instrument reads the version, checks each ID's kind by the client's reserved bits — zero in a V2 position ID, `V2_RESERVED`, line 132 — checks that the client signs for the same exchange (`resolve_order_exchange_address`), and refuses a negative-risk market (`market_reading`, lines 981 to 1025). **The clock** must read NTP-synchronized before any order (`mode_roundtrip`, lines 2281 to 2309). **A round trip runs once:** a second run is refused where an earlier record placed an order, and three records end it (§4.8).

### 1.6 The client — decided: the venue's own, pinned by hash, installed offline

CANON PART IV names the official CLOB client at a pinned version. **The venue's own Python SDK is `polymarket-client`** — its changelog names the older `py-clob-client` deprecated — and **`0.20.0`** is its latest; from `0.18.0` its session-key authorization and revocation take a Relayer API key as well as a Builder key (its changelog). **Its 34 distributions, each pinned to a version and a SHA-256, and `pip` `24.0`'s own wheel**, 35 wheels of `14,422,773` bytes, are fetched by the instrument from `files.pythonhosted.org` over IPv4, each kept only where its size and SHA-256 are the set's (`fetch_wheels`, lines 1393 to 1433; `WHEEL_SET`, lines 174 to 245); **the environment is made without the network:** `python3 -m venv --without-pip /root/l1-env`, then `pip` run from its own wheel with `--no-index --no-deps --require-hashes` against the wheels and the requirements the instrument wrote. No `apt`, no package from anywhere else, and no version chosen at install time: the set was resolved by the Architect on 2026-11-19 and is frozen in the instrument. `env` then reads the installed distributions against the pins — none missing, extra or at another version — and asserts the client's terms this file relies on: its session lifetime, `15,534,000` s, a batch's `600` s, its selectors, its hosts, its exchanges and its V2 bits (`mode_env` and `client`, lines 1985 to 2002 and lines 1697 to 1739). **Every request of the client carries this TZ's agent, `btc-5m-twap-tz50`** (map §6, venue edge), and every lookup goes through `gai4`, which asks `AF_INET` alone (lines 457 to 467).

### 1.7 Telegram — decided: the bot's token and its chat now, its control panel with the unit

The Boss has made the bot of L1 and holds its token (his message of 2026-11-19). Map §7 item 184 fixes the panel: L1's unit reports to his one pinned chat through a bot of its own, and **one command acts, «Стоп»**, which cancels every open order of the key and stops the unit so that it does not start again, a reboot included; Telegram never places, sizes, prices or moves an order, and never starts the unit. **A stop has nothing to stop until the unit runs, so the panel is built with the unit, in L1's unit TZ;** this TZ puts in place what the panel stands on: **the token**, typed by the Boss, hidden, into `/etc/l1-bot/telegram-token`, `0600`, root's, never printed (`mode_secrets`); **its proof**, `getMe` and `getMyCommands` (`mode_tg_probe`, lines 1595 to 1605); **the chat**, pinned to `/etc/l1-bot/chat-id` as the one private chat that sent the bot `/start` — two such chats FAIL, so a stranger who found the bot first cannot be pinned (`mode_find_chat`, lines 1608 to 1638); and **one message**, the round trip's report, in Russian, from its record, carrying no address, id or hash (`report_text` and `mode_tg_report`, lines 1641 to 1658 and lines 1674 to 1692). No poller runs after the run: one token serves one poller of `getUpdates`, and the unit's is the next TZ's.

### 1.8 The Boss's login — decided: his own key, made on his device

Since TZ-49 the live host takes root by key alone, so Termius's password login is refused (map §7 item 183). **A key made by the Executor would put the Boss's private key on a server and in the session's text; a key made in Termius never leaves his phone**, so B-OWNER asks him for his key's **public** line and `bosskey` appends it to root's `authorized_keys` — one line, a public key of a known type, RSA at `3,072` bits or more, never a private key, options or two lines — printing its type and fingerprint and root's keys by fingerprint (`mode_bosskey` and `pubkey_line`, lines 1529 to 1566 and lines 863 to 895). An empty answer skips it: the Boss keeps `ssh live-host` from the capture host and the provider's console. Root's password stays off.

### 1.9 IPv4 alone, and what is printed

**IPv4 alone, in every mode** (map §7 item 181): every socket is `AF_INET`, every name resolved in `AF_INET` alone — the client's through `gai4` — and the audit hook refuses an `AF_INET6` socket and a lookup in any other family; an `AF_UNIX` socket is let through in the client's modes alone, asyncio's own self-pipe, which reaches no network (`policy`, lines 366 to 441). **The hook refuses every open, change, listing, connection and process §2 does not give the running mode** — each credential readable by the modes that need it alone, the session key's file written by `key` alone and by exclusive create, the terminal opened by the Boss's modes alone. **To its log no mode writes a key, a token, the relayer key, an address of the bot's wallet, owner or session key, a transaction hash, an order's id, a chat id or the bot's name**, and none reads or prints a price or size of any book; **what the Boss must check before he signs — the owner, the wallet, the key, the exchanges — goes to his terminal alone**, and the link carries them in its fragment, which no request sends.

---

## 2. Scope

Allowed, and nothing else:

1. **The branch `tz-50-l1-account-round-trip`** carries one file, `research/tz50-l1-account.py`, new (§10 C3). No other repository file changes: `SYSTEM-MAP.md`, this file and `docs/l1-sign.html` reached `main` in the Boss's upload. The report goes to `main` (contract §4). **GitHub Pages** is turned on for `main`'s `docs/` by §3.5's `gh api` — the one change this run makes to the repository's settings — or by B-PAGES.
2. **The capture host.** *Written:* `/root/tz50-work/**` — logs, the stage, the live host's logs as copied, the branch worktree and the self-test's temporary tree — removed by §9; copies into `/root/btc-forensics/` by `reclaim`'s exclusive create alone (§9); earlier session directories under `/tmp/` by B-RECLAIM-SCRATCH (§3.3). *Read:* the primary checkout and `origin`'s refs; the reward book's store by the names and sizes of its directory entries alone, while its archive is not running — no file of it opened — every day from 2026-11-14 staying reserved (map §2.6); the recorder's store by §0.3's `find` and `grep -c`; systemd's records of this project's units and `telemetry-watch.service`'s two states; the directory that holds this session's own, by `scratch`; root's SSH files of the access by `ssh -G` and `ssh-keygen`; `/proc`; `df` and `statvfs` of `/var/lib`; `du` and `test -e` of the trees §0.3 names; GitHub's Pages record of this repository by `gh api`. **No unit of the capture host is started, stopped, signalled, enabled, disabled or edited, and no store of it is written.** The Boss's B-OWNER runs there in his own terminal and writes nothing there.
3. **The live host.** *Written, and removed by §9:* `/root/tz50-work/**` — the instrument's copy, the logs, the wheels and their `requirements.txt`, the self-test's tree. *Written, and kept — L1's:* **`/root/l1-env/**`**, the client's environment, by B-ENV alone; **`/etc/l1-bot/`**, `0700`, root's, with `session-key` by `key`, `relayer-key` and `telegram-token` by `secrets` — typed by the Boss — and `chat-id` by `find-chat`, each `0600`, root's, by exclusive create, never rewritten; **`/var/lib/l1-bot/`**, `0700`, root's, with `account.json` — the owner's, the wallet's and the session key's addresses, the key's scope and validity, the allowances read and the instants of authorization and approval — by `secrets`, `authorize` and `approve`, `tz50-roundtrip-N.json`, `N` at most `3`, by `roundtrip`, and `tz50-l1-account.py`, the instrument's copy for B-REVOKE, by §3.10's `install`; **one line of `/root/.ssh/authorized_keys`**, the Boss's public key, by `bosskey` where he gives one. *Units:* none started, stopped, enabled or edited. *Read:* `/proc`; `/etc/os-release`, `/etc/default/locale`, the SSH host keys' public halves, TZ-49's sshd drop-in and `sshd -T`'s print by the keywords this TZ names; `timedatectl`; root's authorized keys by type and fingerprint; L1's paths by kind, mode, owner and size — **a credential's file by those alone**, never its content but by the mode that uses it, each listed in `READS` (lines 317 to 320).
4. **The network.** From the live host, IPv4 alone, every request with `User-Agent: btc-5m-twap-tz50` (`HEADERS`, line 120; the client's agent set to it in `client`): **anonymous** — `https://polymarket.com/api/geoblock`, at most three reads each time §3 runs it; `https://seahomebatumi-ai.github.io/btc-5m-twap/l1-sign.html`, at most twenty reads each time; the 35 wheels from `https://files.pythonhosted.org`, at most three reads each; one five-minute market's gamma document, `https://gamma-api.polymarket.com/markets/slug/btc-updown-5m-<T0>`, at most three — one a round trip; Polygon's RPC, `https://polygon.drpc.org`, the client's own, `eth_call` of pUSD's `balanceOf` and `allowance` alone; the relayer's `/deployed` and the batch's parameters; **authenticated, and authorized by this TZ in writing (contract §10; this file's header)** — the relayer's submissions of the owner's signed batches, by his Relayer API key: one authorization of the session key, and one approval where an allowance is short, each at most three times by its links; the CLOB's derivation of the session key's API credentials and its reads by them — closed-only mode, the wallet's balance and allowances, the key's and the wallet's open orders, one order by its id — and `/balance-allowance/update`; **the one order** of §1.5, at most two placements, its cancellation by id and `cancel_all`; Telegram's Bot API by the bot's token — `getMe`, `getMyCommands`, `getUpdates` with `allowed_updates` `message` alone, and one `sendMessage` to the pinned chat. **The hook refuses a lookup of any host the mode's list does not name or in any family but `AF_INET`, a socket of any family but `AF_INET` — `AF_UNIX` in the client's modes alone — and a connection to an address this process did not resolve from an allowed name** (`policy`, lines 366 to 441; `NET`, lines 308 to 312). From the capture host: `git` with GitHub — the fetch, `ls-remote`, the push — `gh pr create` and `gh api` of this repository's Pages, which carry `gh`'s credential; `ssh` and `scp` with the live host, `methods`' two connections among them.
5. **Prints and records.** No address of either host, and of the live host's name its first label alone — the geoblock's `ip` compared and never printed, `ssh` and `scp` quiet, `methods`' text by its methods alone, the alias's `hostname` line left out. **To every log and record of this run:** no key, token, relayer key, signature, password or private key; **no address of the bot's owner, wallet or session key**, no transaction hash, no order id, no chat id and no bot name; what the Boss checks before he signs goes to his terminal alone. **No price, size, side, book hash, rate, competitiveness or outcome of any book or market is read or printed** — the gamma document's `outcomePrices` is in its reply and read by nothing; the order's own state is read by its id — its status, price, size, side, type and matched size, and whether its maker is the wallet and its asset the token — and the wallet's own pUSD balance and allowances, which no reserve holds. The reward book's store, every day from 2026-11-14 reserved, is read by names and sizes alone.
6. **Money and keys.** The session key is made on the live host and is never printed, hashed or copied; the owner's key never reaches any host; the Relayer API key and the bot's token are typed by the Boss alone. **This run moves money only by the one order**, whose loss is at most `0.10` pUSD, and **signs nothing but** the order's two placements at most, through the session key, and the owner's two batches — the authorization, and the approval of `1` pUSD to each exchange whose allowance is short — on his device. **No withdrawal, transfer, deposit, revocation or allowance beyond those is made by any code of this run**; the deposit and the allowlist are the Boss's own, on polymarket.com.
7. **The session's own trees** — `/root/tz50-work/**` on both hosts — written and removed by §9 (CANON hard rule 15). L1's paths of item 3 stay: they are the step's deployment.

---

## 3. The work, in this order

Every command's output goes to its log, one file per step under the names below, and is quoted in the report; a step run again appends to its own log under a `date -u` line. **After a BLOCK, §3.10's copy runs where the live host is reachable and holds its work tree, then §9** — before §3.1 without its `git worktree remove` line and with `I0` in place of `I`. **A BLOCK after §3.6 leaves L1's paths as they stand** — none is removed by this run — and the report names each by its state.

| step | the capture host's logs | the live host's logs |
|---|---|---|
| §0.0 to §0.5 | `00-ready.log`, `01-stage.log`, `02-fingerprint.log`, `03-host-gate.log`, `04-room.log`, `05-number.log`, `05-refs.log` | — |
| §0.6 | `06-access.log`, `07-copy.log`, `08-methods.log` | `40-host-before.log`, `41-geoblock.log`, `42-sshd.log` |
| §3.1 | `10-number.log`, `11-worktree.log`, `12-fingerprint.log`, `13-push.log`, `14-pr.log` | — |
| §3.2 | `20-selftest.log` | `50-selftest.log` |
| §3.3 | `30-scratch.log`, `32-reclaim-scratch.log` | — |
| §3.4 | — | `51-wheels.log`, `52-B-ENV.log`, `53-env.log`, `54-sdk-selftest.log` |
| §3.5, §3.6 | `35-pages.log` | `55-page.log`, `56-key.log` |
| §3.7 | `37-handover.log` | `70-B-OWNER.log` |
| §3.8 | — | `71-ready.log`, `72-tg-probe.log`, `73-find-chat.log` |
| §3.9 | — | `74-geoblock.log`, `75-roundtrip.log`, `76-record.log`, `77-tg-report.log` |
| §3.10 | `80-live-copy.log`, `88-methods-after.log`, `90-closing.log`, `99-selfcheck.log` | `78-sshd-after.log`, `79-host-after.log`, `81-keep.log` |

**Where the session's permission classifier refuses a command of a block named B-… or of a live host's step `L` or `LC`**, the Executor tries it once and hands the Boss its paste, unchanged, once, in plain words (CANON hard rule 14; map §6, sandbox limit — destructive actions; §7 items 124, 138 and 144): every paste is one command line, every step after the first gated on the one before it, its output appended to its log under a `date -u` line, so that the Executor verifies it from that log and runs none of it again. **A block handed to the Boss holds back only the steps that read what it changes** (map §7 item 140).

### 3.1 The branch and its file

```
git -C /root/btc-5m-twap fetch origin
I0 number
git -C /root/btc-5m-twap worktree add -b tz-50-l1-account-round-trip /root/tz50-work/wt origin/main
```

Into `10-number.log` the fetch and `I0 number`, which must print `NUMBER PASS - 2 of 2` again (§0.5), or BLOCKED; into `11-worktree.log` the worktree and §0.1's script again, verbatim but for its argument, `/root/tz50-work/wt` — it must print the instrument `created` and the page `equal, kept`, the worktree holding `main`'s page byte for byte; into `12-fingerprint.log` `I fingerprint`, which must print `FINGERPRINT PASS` again, from the worktree's file. Into `13-push.log`: `I0 refs` (§0.5); commit the instrument alone on the branch; push with `git -C /root/tz50-work/wt push -u origin tz-50-l1-account-round-trip` — through `credential.helper=!gh auth git-credential` where the URL's credential is refused (map §6, git remote) — then:

```
date -u +%FT%T.%NZ; git -C /root/tz50-work/wt ls-remote origin refs/heads/tz-50-l1-account-round-trip
git -C /root/tz50-work/wt rev-parse HEAD
git -C /root/tz50-work/wt diff --numstat origin/main HEAD
```

— the instant the commit is on `origin`, its hash there, which must be the worktree's `HEAD`, and the diff: `3091 0` for the instrument, one path and no other; into `14-pr.log` the pull request against `main`, opened with `gh pr create`. A failed assert or a non-zero exit here is BLOCKED.

### 3.2 The self-test, on both hosts

`I selftest`, into `20-selftest.log`, and `L selftest 50-selftest` must each print `SELFTEST PASS: 135 checks, 135 passed` and `refused by the hook: 5` — the self-test's own live refusals: an `AF_INET6` socket, a lookup in no family, a read of the bot's token in this mode, a write outside the work tree and a command this mode does not name. It reaches no network but listeners of its own on `127.0.0.1`, and runs on literals and on a temporary tree under `/root/tz50-work/selftest-tmp/`, which it removes (`mode_selftest`, lines 2776 to 3055). It proves NUMBER and the refs by kind; the room; G-GEO's readings and that its printed fields never carry the address; the live host gate and each of its five checks failing alone; G-SSH K1 to K5 and each failing alone, and K6's methods from `ssh -v`'s text, never its address; `reclaim`'s predicate; the Boss's key — ed25519 and RSA of 4,096 bits accepted, and eight wrong lines refused, a private key and options among them; an address as typed, a bot token and a relayer key; the signing link's fields in the page's order for the three operations, and an approval of a third exchange refused; the 34 pinned requirements and G-ENV's installed reading with its three faults; the private chats that sent `/start`; the five-minute window; the market — a CTF market's token IDs and a V2 market's position IDs each by its outcome and its exchange, and twelve wrong documents refused, a negative-risk one and IDs of the other kind among them; G-RT on a record and failing on each of its checks alone; the report's text, which carries no address or id; the hook's decisions in every mode on files, the terminal, the network — IPv4 alone — and commands, and its live refusals; the credentials written `0600` by exclusive create, an existing file refused, refused inputs asked again, a second run keeping everything; the Boss's key appended on its own line, a present key kept and an empty answer skipped; and against loopback stand-ins, every request with this TZ's agent: G-GEO, G-PAGE and another path refused, the wheels with one refused for its bytes and then kept, and one not served ending the fetch, `getMe`, the chat pinned and two chats refused, and the report sent to the pinned chat; and the floors. A red self-test stops the run here, and it goes to §3.10 and §9.

### 3.3 The directories beside this session, and B-RECLAIM-SCRATCH

`I scratch "$(dirname "$S")"`, into `30-scratch.log`, lists every UUID directory beside this session's own and names each **live** — born from 1 s before to 60 s after the start of a running process whose `argv[0]` is `claude` or ends in `/claude.exe` — or **earlier** (`mode_scratch`, lines 1201 to 1215; map §7 items 91 and 150). Map §3 lists beside this session's own TZ-49's pair, `51f223d3-deb1-5de5-80aa-0eb16a447b53` and `6ce33308-8331-4563-bb79-d8486968f8ad`, and `95cf58d2-1ec6-4c73-a622-38d04665f5ae` and `ccca2df8-e51d-56bc-8205-06299775095a`, which it names live and no TZ's. **The rule alone decides:** every directory `scratch` names earlier is reclaimed (map §7 item 95). **B-RECLAIM-SCRATCH**, for every directory `I scratch` names **earlier** — none it named live, and never this session's own — into `32-reclaim-scratch.log`:

```
cd /root/tz50-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz50-work/wt/research/tz50-l1-account.py reclaim <each earlier directory, by its full path>
rm -rf <one such directory>; echo "exit=$?"
test -e <that directory>; echo "exit=$?"
```

One `reclaim` names every earlier directory and must print `RECLAIM PASS` before any removal; then one `rm -rf` and one `test -e` a directory, the last reading `exit=1`. `reclaim` refuses a directory born from 1 s before to 60 s after a running claude process started, and any path but `/root/tz50-work` that is not a UUID directory under `/tmp/` whose parent's name carries `btc-5m-twap` (`reclaimable`, lines 848 to 853; `mode_reclaim`, lines 1234 to 1281), and keeps nothing of such a directory. If `I scratch` names none earlier, the block is recorded as empty and skipped. **Its paste**, where the classifier refuses it — the Executor writes in every earlier directory's full path, one `rm -rf` and one `test -e` a directory, all chained to the `reclaim`'s `exit=0`:

```
{ date -u +%FT%T.%NZ; (cd /root/tz50-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz50-work/wt/research/tz50-l1-account.py reclaim <D1> <D2>); echo "exit=$?"; } >> /root/tz50-work/logs/32-reclaim-scratch.log 2>&1 && tail -n 1 /root/tz50-work/logs/32-reclaim-scratch.log | grep -qx 'exit=0' && { date -u +%FT%T.%NZ; rm -rf <D1>; echo "exit=$?"; test -e <D1>; echo "exit=$?"; rm -rf <D2>; echo "exit=$?"; test -e <D2>; echo "exit=$?"; } >> /root/tz50-work/logs/32-reclaim-scratch.log 2>&1
```

It holds back nothing of §3.4 to §3.10, which read none of what it removes.

### 3.4 The client's environment — G-ENV

1. `L wheels 51-wheels` (`fetch_wheels` and `mode_wheels`, lines 1393 to 1439): the 35 wheels of `WHEEL_SET` into `/root/tz50-work/wheels/`, each fetched at most three times 30 s apart and kept only where its size and SHA-256 are the set's, then `requirements.txt` — 34 lines, `name==version --hash=sha256:…`, `pip` not among them. It must print `G-ENV wheels PASS: 35 of 35, 14422773 bytes in all`; anything else is BLOCKED.
2. **B-ENV**, the Executor's, into `52-B-ENV.log`:

```
R 'cd /root/tz50-work && { date -u +%FT%T.%NZ; test ! -e /root/l1-env && /usr/bin/python3 -m venv --without-pip /root/l1-env && /root/l1-env/bin/python /root/tz50-work/wheels/pip-24.0-py3-none-any.whl/pip install --no-index --no-deps --require-hashes --no-cache-dir --disable-pip-version-check --find-links /root/tz50-work/wheels -r /root/tz50-work/wheels/requirements.txt; echo "exit=$?"; du -sb /root/l1-env; ls -la /root/l1-env/bin/python; } >> /root/tz50-work/logs/52-B-ENV.log 2>&1; tail -n 40 /root/tz50-work/logs/52-B-ENV.log'
```

`exit=0` and `du` at most `200,000,000` bytes; anything else is BLOCKED. `test ! -e` refuses to install over an environment already there: none exists before this run (`host before`). `pip` installs from the wheels alone, every one checked against its hash, and resolves nothing — no other package, index or version can enter. **Its paste**, where the classifier refuses it, is the quoted part alone, run by the Boss on the live host (`ssh live-host` on the capture host).
3. `LC env 53-env` (`mode_env`, lines 1985 to 2002): **G-ENV installed** — the interpreter `/root/l1-env`'s, the 34 distributions installed each at its pin, none missing, extra or at another version, and the client's terms asserted in `client` (lines 1697 to 1739). It must print `G-ENV installed PASS`; anything else is BLOCKED.
4. `LC sdk-selftest 54-sdk-selftest` (`mode_sdk_selftest`, lines 2572 to 2764): the client's flows against loopback stand-ins of the relayer, the CLOB, gamma and the RPC, the client's own code throughout — the client's agent and lookups this TZ's, and the hook on `AF_INET6`, `AF_UNIX` and a host no mode names; the authorization — a link signed as the page signs, after a non-signature and another key's signature refused at the terminal, one request to the relayer, and printed lines that carry no address or hash; the key's registration, and a key never authorized refused; an authorization kept on a second run; G-READY before the approvals, five of seven, and after them, seven; the approval of the V2 exchange alone, of both after an empty answer, and of none where none is short; the round trip — a crossing `Up` refused as a `400` and as a refusal, no crossing, a wait for the next window, a V2 market traded by its position IDs through the V2 exchange, the V2 exchange's allowance short, a placement matched and a balance under one order's cost — and no order of the stand-in left live; the revocation, and the key refused after it; the relayer's `FAILED` raising; and every request with this TZ's agent. It must print `SDK SELFTEST PASS: 31 checks, 31 passed` and `refused by the hook: 2` — its own: an `AF_INET6` socket and a lookup of a host the mode does not name; anything else stops the run here, and it goes to §3.10 and §9.

### 3.5 The signing page — G-PAGE, and B-PAGES

Into `35-pages.log`, on the capture host:

```
gh api repos/seahomebatumi-ai/btc-5m-twap/pages --jq '{status: .status, build_type: .build_type, source: .source, html_url: .html_url}'; echo "exit=$?"
```

**Where it reads `exit=0` with `source` `main` and `/docs`**, Pages stands. **Where it reads not found**, the Executor turns it on, once:

```
gh api -X POST repos/seahomebatumi-ai/btc-5m-twap/pages -f 'source[branch]=main' -f 'source[path]=/docs' --jq '{status: .status, source: .source, html_url: .html_url}'; echo "exit=$?"
```

Then `L page 55-page` (`page_read` and `mode_page`, lines 1365 to 1390), in the background: **G-PAGE** (§4.3), up to `20` reads `30` s apart — GitHub's first build of the site takes minutes. **Where the POST is refused, Pages reads another source, or G-PAGE reads FAIL**, the Executor hands the Boss **B-PAGES** once, in plain words, in Russian:

> На github.com, в репозитории `seahomebatumi-ai/btc-5m-twap`: **Settings → Pages**; в разделе **Build and deployment**: Source — **Deploy from a branch**, Branch — **main**, папка — **/docs**; **Save**. Через минуту-две страница появится сама; больше ничего делать не нужно.

and runs `L page 55-page` again every `600` s for at most `60` minutes from the handover; the first PASS ends the wait, and **at the bound the run is BLOCKED** (map §7 item 132). Nothing of the Boss's account is touched before G-PAGE reads PASS.

### 3.6 The session key — G-KEY

`LC key 56-key` (`mode_key`, lines 2005 to 2022): the session key made once, written to `/etc/l1-bot/session-key` by exclusive create, `0600`, root's, under `/etc/l1-bot/` made `0700`; read back and its address re-derived equal; never printed. It must print `G-KEY … made` or, on a run after an earlier one, `present, kept`; anything else is BLOCKED. **It comes after §0.6's G-GEO, which read the venue's geoblock before any key of a venue existed** (CANON PART IV).

### 3.7 The Boss's part — B-ACCOUNT and B-OWNER

**Only after G-ENV, the client's self-test, G-PAGE and G-KEY read PASS.** The Executor writes the handover's instant into `37-handover.log` and hands the Boss, **once, in one message, in Russian, these words, with the paste below written in full:**

> **Шаг 1 — polymarket.com, в аккаунте MetaMask бота** (отдельный аккаунт MetaMask, только для бота; удобнее с компьютера — MetaMask в браузере, — но можно и с телефона):
> 1. Войдите на polymarket.com этим аккаунтом; если аккаунта ещё нет, вход его создаст. Если сайт попросит подтвердить включение торговли — подтвердите.
> 2. **Settings → Account → Withdrawal allowlist → Turn on.** Добавьте адрес вашего основного кошелька **в сети Polygon** — не кошелёк бота и не адрес, которым входите, — и подтвердите кодом из письма. **Это до первого депозита:** после этого деньги со счёта бота могут уйти только на сохранённый адрес.
> 3. **Settings → API Keys → Relayer API Keys:** создайте ключ и не закрывайте страницу — ключ понадобится в шаге 4.
> 4. **Deposit:** внесите не меньше **2 USDC** (минимум площадки в сети Polygon); удобно **10**. Это ТЗ рискует не больше **0,10**; остальное останется для следующего шага.
>
> **Шаг 2 — Telegram:** откройте своего бота L1 и отправьте ему **/start**.
>
> **Шаг 3 — Termius, если хотите входить на сервер в Софии напрямую:** Keychain → **+** → **Generate Key**, тип **ED25519** → Save; затем у этого ключа — **Copy public key**. Публичный ключ передавать безопасно; закрытый остаётся в телефоне.
>
> **Шаг 4 — в терминале сервера в Варшаве, под root,** вставьте одну строку ниже. Она спросит: токен бота от BotFather и Relayer API key — ввод скрыт, — затем адрес владельца ключа, то есть адрес аккаунта MetaMask бота; затем публичный ключ из Termius — или просто Enter, чтобы пропустить. Потом покажет **ссылку**: откройте её **во встроенном браузере MetaMask** (аккаунт бота), сверьте адреса с теми, что в терминале, нажмите кнопку, подпишите, скопируйте подпись и вставьте её в терминал. Может быть вторая ссылка — разрешение биржам Polymarket списывать до 1 pUSD для ордеров бота; так же. Если связь прервётся, пока вы в MetaMask, — вставьте ту же строку ещё раз: сделанное не повторится.

**B-OWNER**, the paste, one line, run by the Boss as root in a terminal on the capture host:

```
ssh -t live-host 'export LC_ALL=C; cd /root/tz50-work && { date -u +%FT%T.%NZ; /usr/bin/python3 -B tz50-l1-account.py secrets && /usr/bin/python3 -B tz50-l1-account.py bosskey && /root/l1-env/bin/python -B tz50-l1-account.py authorize && /root/l1-env/bin/python -B tz50-l1-account.py approve; echo "exit=$?"; } >> /root/tz50-work/logs/70-B-OWNER.log 2>&1'
```

**What it writes to its log is the instrument's own lines alone; what it asks and shows goes to his terminal alone** — the terminal is opened by the Boss's modes alone, and a hidden answer is read by `getpass` (`Tty`, lines 1442 to 1460). **Its four modes, each gated on the one before it:** `secrets` — the token, the Relayer API key and its owner's address, each refused and asked again where it is not of its form, three times at most, each written once and kept on a second run (`mode_secrets`); `bosskey` — his public key or none (`mode_bosskey`); `authorize` — **G-AUTH** (§4.5): the owner's Deposit Wallet derived and read deployed, the session key's authorization built by the client's own code, its link printed to the terminal, his signature taken and recovered to the owner, submitted through his Relayer API key, its transaction confirmed and the key read acting for the wallet; at most three links, each valid `600` s; an authorization that stands from an earlier run is kept and nothing is signed (`owner_flow`, `registered` and `authorize_kept`, lines 1854 to 1912, 1788 to 1810 and 1813 to 1820); `approve` — **G-APPROVE** (§4.6): both exchanges' allowances read on chain, and for those under one order's cost a batch approving `1` pUSD each, signed, submitted and confirmed, the allowances read again; where none is short, nothing is signed (`approve_flow`).

**The wait:** the Executor reads `R 'tail -n 3 /root/tz50-work/logs/70-B-OWNER.log'` at most every 570 s, each read with its instant into `37-handover.log`, **for at most `8` hours from the handover**, until a line `exit=` follows the log's last `date -u` line; **at the bound the run is BLOCKED** (map §7 item 132). `exit=0` goes to §3.8. **Another exit:** the Executor reads the log whole, names the mode and the line that stopped it, and hands the same paste again, unchanged, with one line in Russian saying what to do differently — **at most twice more, inside the same bound**; every mode keeps what an earlier run did. **Where the log shows the relayer refusing the key, or `the owner's Deposit Wallet is not deployed`** — a key or an address typed wrong — the Executor first runs **B-RESET**, into the same log:

```
R 'cd /root/tz50-work && { date -u +%FT%T.%NZ; rm -f /etc/l1-bot/relayer-key /var/lib/l1-bot/account.json; ls -la /etc/l1-bot /var/lib/l1-bot; echo "exit=$?"; } >> /root/tz50-work/logs/70-B-OWNER.log 2>&1'
```

— this run's two files of the Boss's entry, which nothing has used — and then hands the paste again. **B-RESET's paste**, where the classifier refuses it, is its quoted part alone, run by the Boss on the live host. Nothing else of `/etc/l1-bot/` is removed by this run.

### 3.8 After the paste — G-READY and G-TG

The Executor reads `70-B-OWNER.log` whole and requires, after its last `date -u` line: `SECRETS telegram-token:`, `SECRETS relayer-key:` and `SECRETS account:` each `written` or `kept`; a `BOSSKEY` line — `added`, `present already` or `skipped`; `G-AUTH authorize PASS`; `G-APPROVE PASS`; and `exit=0` — anything else is §3.7's. Then:

1. `LC ready 71-ready` (`ready_flow` and `mode_ready`, lines 2121 to 2159): **G-READY** (§4.7), seven checks. **A FAIL is read again every `600` s for at most `120` minutes** — a deposit on its way, or the venue's view behind the chain — the Executor telling the Boss once, in one line in Russian, which check reads FAIL; **at the bound the run is BLOCKED**, no order having been placed.
2. `L tg-probe 72-tg-probe` (`mode_tg_probe`): **G-TG's first check** (§4.10).
3. `L find-chat 73-find-chat` (`mode_find_chat`), in the background: **G-TG's second check** — waits at most `1,800` s for the Boss's `/start`. Where it ends with no chat, the Executor tells the Boss once, in one line, to send `/start` to his bot, and runs it once more. **G-TG decides nothing of the order path:** a FAIL of it skips §3.9's report message alone.

### 3.9 The round trip — G-RT

1. `L geoblock 74-geoblock`: **G-GEO again, immediately before the order** (§4.1; map §7 item 163) — the order comes from the live host's address alone, which the venue reads at this instant. **Anything but PASS is BLOCKED before any order.**
2. `LC roundtrip 75-roundtrip` (`roundtrip_flow` and `mode_roundtrip`, lines 2178 to 2309), in the background: the clock read NTP-synchronized, then §1.5's round trip, its record written to `/var/lib/l1-bot/tz50-roundtrip-1.json`, `0600`, and **G-RT** (§4.8) printed check by check.
3. Into `76-record.log`: `R 'cat /var/lib/l1-bot/tz50-roundtrip-*.json; ls -la /var/lib/l1-bot'` — **the round trip's record, every field of it, quoted in the report** (CANON hard rule 16): it holds no key, address, id or hash (§2 item 5), so the reading it rests on leaves the host with the report.
4. **A round trip that placed nothing** — its record's `placements` empty, stopped by the market's document, its window, closed-only mode, the balance, an allowance or an open order — **is run again, step 1 first, at most twice more**; the mode itself refuses a run after a record that placed an order, and a fourth record (`mode_roundtrip`). **A round trip that placed an order is never run again**, whatever G-RT read.
5. `L tg-report 77-tg-report` (`mode_tg_report`): **G-TG's third check** — the last record's report sent to the pinned chat, its text printed line by line; skipped where G-TG's chat did not read PASS.

### 3.10 The closing reads, the live host's logs and the stop kept

1. `L sshd 78-sshd-after` and, into `88-methods-after.log`, `{ date -u +%FT%T.%NZ; I methods after; echo "exit=$?"; } >> /root/tz50-work/logs/88-methods-after.log 2>&1`: **G-SSH after** — K1 to K6 again, root by key alone with the Boss's key added.
2. `L 'host after' 79-host-after`: the gate and the host's facts again — root's authorized keys by fingerprint, the Executor's and the Boss's where he gave one, and L1's paths by kind, mode, owner and size.
3. **The stop kept on the host**, the Executor's, into `81-keep.log` — where `/var/lib/l1-bot/` exists:

```
R 'cd /root/tz50-work && { date -u +%FT%T.%NZ; install -m 0600 -o root -g root /root/tz50-work/tz50-l1-account.py /var/lib/l1-bot/tz50-l1-account.py && sha256sum /var/lib/l1-bot/tz50-l1-account.py; echo "exit=$?"; ls -la /etc/l1-bot /var/lib/l1-bot; } >> /root/tz50-work/logs/81-keep.log 2>&1; tail -n 20 /root/tz50-work/logs/81-keep.log'
```

`exit=0` and §0.1's SHA-256: **B-REVOKE** (§4.11) runs this copy, so the stop of the order path stays on the host after the work tree goes.
4. Into `80-live-copy.log`:

```
scp -q -r -o BatchMode=yes -o LogLevel=QUIET live-host:/root/tz50-work/logs /root/tz50-work/live-logs; echo "scp exit=$?"
diff <(R 'cd /root/tz50-work/logs && sha256sum *') <(cd /root/tz50-work/live-logs && sha256sum *); echo "diff exit=$?"
ls -la /root/tz50-work/live-logs
```

`scp exit=0` and `diff exit=0`: every log of the live host on the capture host, byte for byte. **G-PRINT** (§4.9), into the same log:

```
grep -rEn '0x[0-9a-fA-F]{40}|[0-9]{5,12}:[A-Za-z0-9_-]{30,}' /root/tz50-work/logs /root/tz50-work/live-logs | wc -l
grep -rlF "$(ssh -G -T live-host | awk '/^hostname /{print $2}')" /root/tz50-work/logs /root/tz50-work/live-logs | wc -l
```

— an address of the form a wallet or key has, or a bot token's, in any log of either host, and the live host's address, which the command reads from the alias and never prints: each count must be `0`.
5. Into `90-closing.log`:

```
R 'date -u; free -b; df -B1 --output=source,size,avail /; systemctl is-active ssh.service; ls -la /etc/l1-bot /var/lib/l1-bot; stat -c "%n %s %a %U" /etc/l1-bot/* /var/lib/l1-bot/*; du -sb /root/l1-env; /root/l1-env/bin/python -c "import importlib.metadata as m; print(m.version(\"polymarket-client\"))"; sshd -T | grep -E "^(permitrootlogin|pubkeyauthentication|passwordauthentication|kbdinteractiveauthentication) "'
TZ=UTC systemctl show btc-recorder.service btc-rewardbook.service adv3-bot.service btc-rewardbook-archive.service btc-rewardbook-archive.timer -p Id -p MainPID -p NRestarts -p ActiveState -p UnitFileState -p ActiveEnterTimestamp
df -B1 --output=source,size,avail /var/lib/btc-recorder; du -sb /root/tz50-work /var/lib/btc-rewardbook; free -b
git -C /root/btc-5m-twap ls-remote origin refs/heads/tz-50-l1-account-round-trip
```

Every line is quoted. **The capture host's units read as at §0.3** — the same `MainPID`, `NRestarts` and `ActiveState` — or the report names the cause from their journal: this TZ touches none of them. Then contract §4.2's self-check, `C` the branch's commit, into `99-selfcheck.log`:

```
git -C /root/btc-5m-twap fetch origin
git -C /root/btc-5m-twap rev-list origin/main | grep -c "$C"
git -C /root/btc-5m-twap diff --name-only origin/main origin/tz-50-l1-account-round-trip
git -C /root/btc-5m-twap diff --numstat origin/main origin/tz-50-l1-account-round-trip
git -C /root/btc-5m-twap ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
```

Then the report is drafted (§8), and §9 runs.

---

## 4. The gates — fixed here, before any of their data exists

| gate | its population | PASS | FAIL does |
|---|---|---|---|
| **G-GEO** | one read of the venue's geoblock over IPv4, at most three while unread | status `200`, `blocked` `False`, `country` two capital letters | BLOCKED, before any key (§0.6) or any order (§3.9) |
| **G-SSH** | TZ-49's drop-in, one `sshd -T`, one connection that offers no key | K1 to K6, six of six | BLOCKED at §0.6; recorded at §3.10 |
| **G-ENV** | the 35 wheels; the 34 distributions installed; the client's terms | 35 of 35 by size and SHA-256; none missing, extra or at another version | BLOCKED |
| **G-PAGE** | the page as GitHub Pages serves it, at most twenty reads | status `200`, Appendix B's `11,846` bytes and SHA-256 | B-PAGES, then BLOCKED at its bound |
| **G-KEY** | `/etc/l1-bot/session-key` | made or kept, `0600`, root's, its address re-derived | BLOCKED |
| **G-AUTH** | the owner's signature and the relayer's transaction | recovered to the owner, confirmed, and the key read acting for the wallet | the paste again (§3.7), then BLOCKED at its bound |
| **G-APPROVE** | the wallet's pUSD allowance on chain to each exchange | each at least `50,000` units, by an approval of `1,000,000` or as found | as G-AUTH |
| **G-READY** | the account read through the session key | seven of seven | read again for 120 minutes, then BLOCKED |
| **G-RT** | the round trip's record | nine of nine | recorded; a run that placed nothing is run again (§3.9) |
| **G-PRINT** | every log of both hosts | `0` and `0` | the report withholds the text and names it (§8) |
| **G-TG** | the bot's `getMe`; its updates; one message | three of three | recorded; the order path goes on |

**No gate is read against a threshold a later step sets, and none is redefined after its data exists.**

### 4.1 G-GEO

`geo_reading` (lines 790 to 797): **UNREAD** unless the reply's status is `200` and its `blocked` a boolean and its `country` two capital letters; **BLOCKED** where `blocked` is true; **PASS** where it is false. Read at most three times 30 s apart while UNREAD, over IPv4 alone; printed of each read its status, `blocked`, `country`, `region`, its keys' names and whether the address the venue saw is the connection's own — a comparison, never the address (`geo_read`). TZ-48 and TZ-49 read `False`, `BG` (map §6, live host — the venue's geoblock).

### 4.2 G-SSH

K1 to K5, `ssh_reading` (lines 830 to 839): TZ-49's drop-in at `SSHD_SHA256` (line 142) and mode `0644`; `passwordauthentication no`, `kbdinteractiveauthentication no`, `permitrootlogin without-password` and `pubkeyauthentication yes` in force. K6, `methods_of` (lines 842 to 845): the methods offered to a connection with no key, `['publickey']`. All six PASS at §0.6, or BLOCKED; after `bosskey`, again at §3.10.

### 4.3 G-PAGE

`page_read` (lines 1365 to 1382): a read of the page at its URL whose status is `200` and whose bytes are `PAGE_BYTES`, `11,846`, with SHA-256 `PAGE_SHA256`, `f1d92e7dd8a8cd15b7b96b86b357ebf80db4e10844b3fc269e92cef0aecba528` (lines 167 and 168) — Appendix B's — at most twenty reads 30 s apart; each read's status, content type, length and hash printed.

### 4.4 G-ENV and G-KEY

**Wheels:** every one of the 35 of `WHEEL_SET` kept only where its size and SHA-256 are the set's, `14,422,773` bytes in all. **Installed** (`installed_reading`, lines 952 to 958): the installed distributions' names and versions equal to the 34 pins — none missing, extra or at another version — under `/root/l1-env`'s interpreter; and `client`'s asserts — the version `0.20.0`, the session lifetime `15,534,000` s, a batch's `600` s, the two selectors, the approve and allowance selectors, the V2 bits, the hosts, pUSD and the two exchanges. **G-KEY:** the key's file made by exclusive create, `0600`, root's, a secp256k1 key whose address read back equals the one made.

### 4.5 G-AUTH

PASS where the owner's signature recovers to the owner under the client's own typed data, the relayer accepts the batch through his Relayer API key and its transaction reads confirmed, and **the key then acts for the wallet** — the client made with it and the wallet's open orders listed by it — read up to 30 times 10 s apart (`registered`); or where an earlier run's authorization of this key stands, read acting at one read (`authorize_kept`). **The key's scope is `CLOB` and its validity the client's, `15,534,000` s from the request** — 180 days less five hours.

### 4.6 G-APPROVE

PASS where, after the run, the wallet's pUSD allowance on chain to the standard exchange and to the V2 exchange each reads at least `50,000` units — one order's cost — whether as found or by the approval of `1,000,000` units to each that was short; the allowances printed as pUSD, or `max` at `2²⁵⁵` and above (`approve_flow`, `chain_allowances` and `shown`, lines 1915 to 1982 and lines 2098 to 2109).

### 4.7 G-READY

`ready_flow` (lines 2121 to 2147), the CLOB's view refreshed first by `/balance-allowance/update`: **(1)** a Deposit Wallet signed for by a session key; **(2)** not in closed-only mode; **(3)** its pUSD on chain at least one order's cost; **(4)** its allowance on chain to the standard exchange at least that; **(5)** to the V2 exchange at least that; **(6)** no open order of the key; **(7)** no open order of the wallet by the key. The CLOB's own view of the balance and its allowances is printed beside, no threshold.

### 4.8 G-RT

`rt_reading` (lines 1028 to 1052), from the record alone: **(1)** one placement accepted live, the last; **(2)** at most two placements; **(3)** every earlier one refused as crossing the book; **(4)** read back `LIVE` at `0.01`, `5`, `BUY`, `GTC`, nothing matched, its maker the wallet, its asset the token; **(5)** cancelled by its own request; **(6)** read back cancelled, nothing matched; **(7)** no open order of the key after it; **(8)** none of the wallet by the key; **(9)** the wallet's pUSD on chain after equal to before. **Before any placement** the record must read the clock synchronized, closed-only `False`, the balance at least one order's cost, no open order, the market eligible, the client signing for the exchange the market's version names, and that exchange's allowance at least one order's cost — each else stops it with its reason, nothing placed. Printed beside, no threshold: the placement's and the cancellation's milliseconds, the CLOB's view of the balance, the market's version and its window's seconds left.

### 4.9 G-PRINT

Over every log of both hosts after §3.10's copy: **`0`** lines with an `0x` address of forty hex digits or a bot token's form, and **`0`** files holding the live host's address. A count above `0` is a defect of the instrument: the report quotes no matched text, names the file and the line, and the Architect's verdict decides.

### 4.10 G-TG

**(1)** `getMe` answers `is_bot` with a username, and `getMyCommands` a list; **(2)** exactly one private chat sent `/start`, pinned to `/etc/l1-bot/chat-id` by exclusive create, `0600` — none in `1,800` s, or two, FAIL; **(3)** the report's message sent, its id an integer. None of it gates the order path.

### 4.11 The stops — CANON hard rule 14, and B-REVOKE

**This TZ deploys no unit and starts no process that outlives it.** The round trip's last act is `cancel_all` of the key, whatever happened, and a market resolving cancels a resting order at the venue. **The stops of the order path after this run, in the Boss's hands:**

- **Withdraw** — on polymarket.com, the wallet's pUSD to his saved address, signed in MetaMask: needs no host.
- **B-REVOKE** — the session key revoked, its open orders cancelled by the venue, its signing ended: one line, as root in a terminal on the capture host, the same signing page and the same Relayer API key:

```
ssh -t live-host 'export LC_ALL=C; mkdir -p /root/tz50-work/logs && cp /var/lib/l1-bot/tz50-l1-account.py /root/tz50-work/ && cd /root/tz50-work && { date -u +%FT%T.%NZ; /root/l1-env/bin/python -B tz50-l1-account.py revoke; echo "exit=$?"; } >> /root/tz50-work/logs/90-B-REVOKE.log 2>&1'
```

**It is not run by this TZ**, and no FAIL of this TZ calls for it: the key can spend at most the allowances' `1` pUSD an exchange through orders, and the run's own loss is bounded at `0.10` pUSD. `revoke` is tested by the client's self-test against the stand-in (§3.4).

### 4.12 What a PASS establishes, and what it does not

**Established:** the client at its pins on the live host; a session key there that the owner authorized from his own device, which acts for the wallet; the wallet's pUSD and its allowances; and **one order's round trip through that key from Sofia** — accepted live, read, cancelled by its id and gone, the wallet unchanged — on the market version of its day; the bot's token, its pinned chat and a message delivered; the Boss's key on root's list. **Not established:** that an order fills, or what a fill costs — none is expected; anything of the reward markets, their books or rule W's quoting, which L1's unit TZ measures inside its own loss limit; the venue's payouts to our address — L1's measurement; the reward book's capture of Protocol V2 markets (map §7 item 186); that the geoblock stays `False` — the unit reads it before it quotes; and the latency of an order — the placement's and cancellation's milliseconds are printed and decide nothing.

---

## 5. The instrument

`research/tz50-l1-account.py`, Appendix A, fixed by the Architect as this TZ's Validation and written byte for byte. **The standard library alone in every mode but the client's** — on the capture host under `/root/tz04a-env`, on the live host under its system `/usr/bin/python3`, Python 3.12 (LH3); **the client's modes** — `env`, `key`, `authorize`, `approve`, `revoke`, `ready`, `roundtrip` and `sdk-selftest` — under `/root/l1-env/bin/python`, importing the venue's client and nothing of this repository. **It loads no other instrument.** Its own hook, `policy` (lines 366 to 441), applied by `_audit` (lines 444 to 454): writes inside the work tree alone — and L1's files each by the modes `WRITES` names, the credentials by exclusive create — into the forensic store by `reclaim`'s exclusive create alone; no file of a capture's store or of the advisor's credentials opened in any mode, and the reward book's store listed by `room` alone; IPv4 alone; a command only where the mode's list names it — `file` among the client's modes, which `pycryptodome`'s import runs on the interpreter. **Its code:** the TZ's constants (lines 80 to 298); the hook (lines 300 to 467); helpers and the network, IPv4 alone, every request with this TZ's agent (lines 469 to 740); the readings as pure functions (lines 742 to 1052); the capture host's modes (lines 1054 to 1281); the live host's standard-library modes (lines 1283 to 1692); the client's modes (lines 1694 to 2309); the client's self-test and its stand-ins (lines 2311 to 2764); the self-test (lines 2766 to 3055); and `main` (lines 3060 to 3091). **Exits:** `0` every assert held; `1` a failed assert, named, or a BLOCK whose message says so; `2` run with `-O`; `4` a reading's FAIL. Every mode prints, on every exit, its peak memory, the hook's refusals and its counts. **Each live read is a measurement of its instant and is made once; the pure functions under every reading are checked against literals by the self-test on both hosts, and the client's flows against stand-ins by the client's self-test** (contract §6).

---

## 6. Cost

At the populations' upper bounds (§10 C4): `selftest` about 2 s on each host; `sdk-selftest` about 15 s; `fingerprint` under 1 s over 67 rows; `number`, `refs`, `scratch` about 1 s each; `methods` at most 60 s; `sshd` at most 20 s; `room` under 1 s beside its wait for the archive, at most 30 reads 60 s apart; `reclaim` under 2 s; `geoblock` at most 150 s — three reads at two timeouts of 15 s, two waits of 30 s; `host` at most 60 s of commands — three at 20 s — beside its floors' reads; `wheels` under 30 s at a few MB a second, in the background, the first wheel not served whole in three reads ending it; B-ENV under 60 s; `env` and `key` under 5 s each; `page` at most about 900 s — twenty reads at two timeouts of 15 s and nineteen waits of 30 s — in the background; `ready` at most about 330 s, its key read once; `tg-probe` under 5 s; `find-chat` at most 1,800 s, in the background; `roundtrip` under 10 s of requests, beside a wait of at most 152 s for its window, in the background; `tg-report` under 5 s; `authorize` and `approve` the Boss's, each at most three links of 600 s and the relayer's confirmation. **Waits, not compute:** B-PAGES at most 60 minutes; B-ACCOUNT and B-OWNER at most 8 hours; G-READY at most 120 minutes; the room's archive at most 30 minutes. **No check reaches `3,600` s of compute.** About 50 minutes of the session's wall clock beside the waits.

---

## 7. Validation

The report shows each, with its count, and says whether it is asserted:

- **V1** — `FINGERPRINT PASS` at §0.2 and §3.1: revision `2026-11-20-a`; anchors 6, 4 re-derived; rows `67` = `64` + `2` + `1`, 64 `frozen` equal; the page on `main` equal to Appendix B. Asserted.
- **V2** — `NUMBER PASS - 2 of 2` at §0.5 and §3.1; refs by kind, each kind that differs from map §1 named, the branch absent before the push. Asserted.
- **V3** — §0.1's script at §0.1 and §3.1: two files at §0.1's lines, bytes and SHA-256 — `created` twice, then `created` and `equal, kept`; the live host's copy the same SHA-256 (§0.6). Asserted.
- **V4** — the branch: one path, `--numstat` `3091 0`, the commit on `origin` the worktree's `HEAD`. Asserted.
- **V5** — the capture host gate, seven checks; the room and its margin printed. Asserted.
- **V6** — the access: `exit=0`, TZ-47's pinned key, `vs-2348`, `root`, both trees absent; the copy's SHA-256. Asserted.
- **V7** — the live host gate, five checks, and its floors, at `host before` and `host after`. Asserted.
- **V8** — `G-GEO PASS` at §0.6 and §3.9, every read's line. Asserted; BLOCKED otherwise.
- **V9** — `G-SSH` K1 to K5 and K6 at §0.6 and §3.10. Asserted at §0.6.
- **V10** — `SELFTEST PASS: 135 checks, 135 passed` on both hosts, `refused by the hook: 5`; `SDK SELFTEST PASS: 31 checks, 31 passed` on the live host, `refused by the hook: 2`. Asserted.
- **V11** — §3.3: `scratch`'s listing; `RECLAIM PASS` where it named any directory earlier, each removal's `test -e` `exit=1`. Asserted where it runs.
- **V12** — G-ENV: `35 of 35`, `14422773` bytes; B-ENV's `exit=0` and `du`; `G-ENV installed PASS`, 34 distributions. Asserted.
- **V13** — Pages: the `gh api` reads, who turned Pages on and when; `G-PAGE PASS` with its read's status, type, length and hash. Asserted.
- **V14** — `G-KEY`: made or kept, its file's state. Asserted.
- **V15** — B-OWNER: the handover's instant; every read of its log with its instant; each run of the paste with its exit; B-RESET where it ran; the `SECRETS` lines, `BOSSKEY`'s, `G-AUTH authorize PASS` and `G-APPROVE PASS` with the allowances before and after. Asserted by their own lines.
- **V16** — `G-READY PASS: 7 of 7`, every read with its instant. Asserted.
- **V17** — G-TG: `getMe` PASS, the chat pinned, the report's message sent with its text. Recorded.
- **V18** — `G-RT PASS: 9 of 9`, every placement's line, the read-backs, the cancellation, the balances before and after, and the record whole. Asserted; a run that placed nothing and its re-runs each recorded.
- **V19** — G-PRINT: `0` and `0`. Asserted.
- **V20** — §3.10: the kept copy at §0.1's SHA-256; `scp exit=0` and `diff exit=0`; the capture host's units as at §0.3, or the cause named; contract §4.2's self-check: `0`, one path, `3091 0`, nothing. Asserted where a command asserts it.
- **V21** — every mode's printed peak — the standard library's each under `42,525,853`, the client's each under `137,522,684` — and every memory and free-space read with its instant and its floor. Recorded.
- **V22** — §9: `RECLAIM PASS`; `/root/tz50-work` gone on both hosts, `test -e` `exit=1` each; L1's paths on the live host as §3.10 read them; the capture host's worktrees the primary checkout and `/root/btc-recorder-svc`; the forensic store's count. Asserted where a command asserts it.

---

## 8. The report

`CryptoReports/TZ-50-l1-account-round-trip-report.md`, contract §8's sections in their order. **§2 Measurements** gives, beside §7's lines: **the live host** — `host before` and `host after` whole, side by side where they differ; **the geoblock** — every read's line, at §0.6 and §3.9; **root by key alone** — `42-sshd.log`, `08-methods.log`, `78-sshd-after.log` and `88-methods-after.log` whole; **the client** — `51-wheels.log`'s summary lines, `52-B-ENV.log` whole, `53-env.log` whole; **the page** — `35-pages.log` and `55-page.log` whole; **the Boss's part** — `37-handover.log` and `70-B-OWNER.log` whole; **the account** — `71-ready.log` whole; **the round trip** — `75-roundtrip.log` and `76-record.log` whole, the record's every field (CANON hard rule 16); **Telegram** — `72-` to `73-` and `77-tg-report.log` whole; **G-PRINT**'s two counts; **the capture host** — §0.3's and §3.10's reads, the room and its margin; and **every free-space and `MemAvailable` read**, with its instant and its bound. **§4 Gate** states G-RT's reading in its first line. **§6** names every departure, every refusal by the classifier with the block, its words and who ran it, every block run by the Boss with its instant, and each time the Boss's paste was run. **The report prints no address of either host, of the bot's owner, wallet or session key, no key, token, relayer key, signature, transaction hash, order id, chat id or bot name** — G-PRINT asserts the logs it quotes carry none.

---

## 9. Reclaim — both hosts left clean (CANON hard rule 15)

**B-RECLAIM-LIVE**, after §3.10's copy read `diff exit=0` — or, after a BLOCK, after the copy where the live host is reachable — the Executor's first:

```
R 'rm -rf /root/tz50-work; test -e /root/tz50-work; echo "exit=$?"'
```

It must print `exit=1`. **Its paste**, run by the Boss in a terminal on the live host: `rm -rf /root/tz50-work; test -e /root/tz50-work; echo "exit=$?"`. Nothing of the live host's work tree is kept there: its logs are on the capture host byte for byte (§3.10), its copy of the instrument is the stage's by SHA-256 and is kept at `/var/lib/l1-bot/` for B-REVOKE, and its wheels are PyPI's, by the hashes of Appendix A. **Kept on the live host — L1's, this TZ's deployment:** `/root/l1-env/`, `/etc/l1-bot/` and `/var/lib/l1-bot/` as §3.10 read them, and the Boss's line in root's `authorized_keys`.

**What the capture host keeps:** `reclaim` copies every regular file of `/root/tz50-work` but the branch worktree's and the self-test's temporary tree's — the logs, the live host's logs and the stage's two files — into `/root/btc-forensics/` as `tz50-work--<path with / as -->`, by exclusive create, its hash verified; a name already there with the same hash is counted as held, and with another hash is a failed assert; after each copy free space stays at or above `7,400,000,000` bytes or it BLOCKS (`mode_reclaim`, lines 1234 to 1281; `RECLAIM_FLOOR`, line 289). **No file of this run is held by a Release**, so none is left to one. The branch worktree is not copied: `reclaim` asserts that `git status --porcelain --ignored` in it prints nothing and that its `HEAD` is its upstream's (`pristine`, lines 1218 to 1224), so `git worktree remove` needs no `--force` (map §7 item 89). The report's draft in `CryptoReports/` counts as the report. **No `reclaim`'s output is filtered** (map §7 item 119).

**B-RECLAIM-OWN**, last, after B-RECLAIM-LIVE and with the report drafted. **Its output is written to no file; the report quotes it verbatim from the session**, every line of it:

```
(cd /root/tz50-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz50-work/wt/research/tz50-l1-account.py reclaim /root/tz50-work); echo "reclaim exit=$?"
cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz50-work/wt; echo "exit=$?"
rm -rf /root/tz50-work; echo "exit=$?"
test -e /root/tz50-work; echo "exit=$?"
git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
find /root/btc-forensics -type f | wc -l
df -B1 --output=source,size,avail /var/lib/btc-recorder
```

`reclaim` must print `RECLAIM PASS` before the removals. **Its paste**, where the classifier refuses any line of it — every step chained to the one before it, the removals reached only after `RECLAIM PASS`; its output goes to the Boss's terminal, the tree its log would be in being removed:

```
(cd /root/tz50-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz50-work/wt/research/tz50-l1-account.py reclaim /root/tz50-work) && cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz50-work/wt && rm -rf /root/tz50-work; test -e /root/tz50-work; echo "exit=$?"; git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list; find /root/btc-forensics -type f | wc -l
```

Where the Boss ran it, the Executor verifies it by its own reads — `test -e /root/tz50-work; echo "exit=$?"`, `git -C /root/btc-5m-twap worktree list`, `find /root/btc-forensics -type f | wc -l` and `sha256sum /root/btc-forensics/tz50-work--*` against the report's hashes — and the report quotes those reads. The branch `tz-50-l1-account-round-trip` stays on `origin` and as a local ref; only its working tree goes. **Kept on the capture host:** the Executor's access and the forensic store; nothing of the capture was touched.

---

## 10. Pre-send checks

Performed by the Architect on 2026-11-20 against this file, start to end, in a reading separate from its writing. Every committed file was read at `origin/main` `234a6e8`; Appendices A and B at §0.1's SHA-256; the venue's client at `polymarket_client-0.20.0-py3-none-any.whl`, Appendix A's set's SHA-256.

| # | check | result |
|---|---|---|
| **C1** | scope against body | **Named by the body, each inside §2.** *Repository, written:* `research/tz50-l1-account.py` on the branch, `CryptoReports/TZ-50-l1-account-round-trip-report.md` on `main`, and Pages' setting for `main`'s `docs/` — §2 item 1. *Repository, read:* this file by §0.1's script; `SYSTEM-MAP.md`, the 67 files of its §0 table and `docs/l1-sign.html` by `fingerprint`; `CryptoTZ/` and `CryptoReports/` by `number`; `origin`'s refs by `refs` and §3.1's `ls-remote`; TZ-49's report and `research/tz33-reward-book-capture.py` line 190 cited, never opened by the instrument. *Capture host, written:* `/root/tz50-work/**` — §2 items 2 and 7; `/root/btc-forensics/tz50-work--*` by `reclaim`; earlier session directories by B-RECLAIM-SCRATCH — §2 item 2. *Capture host, read:* §0.0's, §0.3's, §0.6's and §3.10's reads and `gh api`'s Pages record — §2 item 2. *Live host, written:* `/root/tz50-work/**` — §2 items 3 and 7; `/root/l1-env/**` by B-ENV; `/etc/l1-bot/` and its four files by `key`, `secrets` and `find-chat`; `/var/lib/l1-bot/` with `account.json` by `secrets`, `authorize` and `approve`, the round trip's records by `roundtrip`, and the kept instrument by §3.10's `install`; the removals of B-RESET, two files of this run; one line of `authorized_keys` by `bosskey` — §2 item 3. *Live host, read:* `/proc`, `/etc/os-release`, `/etc/default/locale`, the host keys' public halves, the drop-in and `sshd -T`, `timedatectl`, root's keys by fingerprint, L1's paths by state — §2 item 3. *Network:* the geoblock, the page, the wheels, gamma's one document a round trip, the RPC's `eth_call`, the relayer, the CLOB and Telegram from the live host over IPv4 alone; GitHub and the live host from the capture host — §2 item 4. **By content class:** no output carries a price, size, side, book hash, rate, competitiveness or outcome of a market — gamma's reply holds `outcomePrices`, which nothing reads, and the order's own state and the wallet's own balance and allowances are this run's, under no reserve; no output carries an address of either host or of the bot's owner, wallet or key, a key, token, relayer key, signature, transaction hash, order id, chat id or bot name — the self-tests assert it of `G-GEO`'s fields, `ssh -v`'s methods, the owner flows' printed lines, the round trip's and the report's text, and G-PRINT reads every log; the Boss's terminal is outside every log. **No intersection, and no exemption needed beyond §2's own.** |
| **C2** | origin of every expectation | **Every fixed literal of §0, §4, §5 and §7, of two kinds and no third.** *Quoted from a committed artifact, named:* revision `2026-11-20-a`, the six anchors and rows `67` = `64` + `2` + `1` (map §0, this TZ's revision, counted by an independent parse); `31612203008` and `e3975b5da44c5328adf3bf3914634cd878842c73` (map §6, disk and host identity); `7,300,000,000` (tz33 line 190); `445,535,636` (map §6, disk floors and caps); `58,953,728` and `49,168,384` (map §6, memory); `2,147,483,648`, TZ-49's `SystemKeepFree` (its report §2); `vs-2348`, the pinned host key `SHA256:Y14Iy6ok…` and the Executor's `SHA256:1xbA0Mhj…` (map §6, live host identity; TZ-47's and TZ-49's reports); `SSHD_SHA256` `94fff8f1…`, re-derived by the Architect from `research/tz49-live-host.py`'s `SSHD_TEXT` at `234a6e8`, 340 bytes; the session directories (map §3); the venue's exchanges, pUSD, the V2 bits, `15,534,000` s and `600` s (the client's own source, `environments.py`, `protocol.py`, `session_keys.py` and `deposit_wallet.py`, and the venue's table in `/trading/wallets-auth`); the minimum size `5` and the ticks (map §6, venue constants). *Computed by an implementation independent of the one under test:* the instrument's and the page's lines, bytes and SHA-256 by `wc` and `sha256sum`; the 35 wheels' sizes and SHA-256 by `sha256sum` over the files PyPI served, against PyPI's own JSON digests; `47,855,239` bytes by `du -sb` of the Architect's environment from them; the page's typed data by the client's `build_deposit_wallet_typed_data` and MetaMask's `@metamask/eth-sig-util` `8.2.0`, nine links; `50,000` = 5 · 0.01 · 10⁶; `100,000` = 2 · 50,000; `1,000,000` = 1 · 10⁶; `7,795,535,636` = 7,300,000,000 + 445,535,636 + 50,000,000; `2,447,483,648` = 2,147,483,648 + 200,000,000 + 100,000,000; `7,400,000,000` = 7,300,000,000 + 100,000,000; `14,422,773` the sum of the 35 sizes. *Measured by the kernel, not by the code under test:* `35,467,264` and `114,696,192`, the `ru_maxrss` of the largest of the Architect's runs, and from them `42,525,853` and `137,522,684` = ⌈peak · 58,953,728 / 49,168,384⌉ and `85,051,706` and `275,045,368` their doubles (map §7 item 156) — floors asserted at each mode's start; V21 records the peaks and asserts nothing. *Counted on the Architect's runs of the self-tests on these bytes, which run on literals and stand-ins alone:* `135` and `5`, `31` and `2`. **No expectation depends on a quantity this TZ measures.** |
| **C3** | shape of every diff | **One file, new.** `research/tz50-l1-account.py` is absent from `origin/main` (`git cat-file -e` exit `128`): `3091` lines added and `0` removed; no committed line is replaced. `docs/l1-sign.html` is absent from `origin/main` too (exit `128`) and reaches it in the Boss's upload, not in this run's diff; `SYSTEM-MAP.md` is replaced by its revision in the same upload. The report is new on `main`. |
| **C4** | cost of every check | At the populations' upper bounds (§6): `selftest` about 2 s at each of the Architect's runs on these bytes, `sdk-selftest` about 15 s at each of its runs; `fingerprint` under 1 s over the 67 rows' files and the page; `number` and `scratch` under 1 s; `refs` one `ls-remote`; `room` under 1 s over at most `PEAK`'s fourteen slots of streams, beside its archive's wait; `reclaim` under 2 s over at most `20,000,000` bytes; `methods` at most 60 s; `geoblock` at most 150 s — three reads at two timeouts of 15 s, two waits of 30 s; `sshd` at most 20 s; `host` at most 60 s of commands beside its floors' reads; `wheels` under 30 s in the Architect's fetch of the same set, and in the background, since a wheel served slowly is bounded by its reads' timeouts and not in all — the first wheel not served whole in three reads ends it; B-ENV under 60 s; `env` and `key` under 5 s; `page` at most 900 s, in the background; `ready` at most about 330 s; `find-chat` at most 1,800 s, in the background; `roundtrip` under 10 s of requests and a wait of at most 152 s; Telegram's calls under 5 s each. **Waits, not compute:** B-PAGES 60 minutes, B-ACCOUNT and B-OWNER 8 hours, G-READY 120 minutes, the archive 30 minutes. **No check reaches `3,600` s of compute.** Fail-fast bounds, each derived: `TIMEOUT_S` `15` — the venue's edge answered in a median of 0.131 s at TZ-49, a hundred times a reply; `TRIES` `3`, `30` s apart — a fault of a minute is outlasted; `PAGE_TRIES` `20` — GitHub's first build of a site takes minutes, ten covered; `RT_MIN_LEFT_S` `150` — the round trip ends in under 10 s, so half a window is fifteen times its need; `READY_TRIES` `30`, `10` s apart — a confirmed relayer transaction is read by the CLOB within seconds; `TG_WAIT_S` `1,800` — the Boss's `/start` is in B-ACCOUNT, before the paste; `DEADLINE_S` `600` and `LINKS` `3` — the client's batch validity, and three tries to open a link and sign; `MEM_READS` `5`, `60` s apart — map §7 item 137; the 8 hours — an allowlist's email code and a deposit's arrival, the slowest of the Boss's steps, with room. |
| **C5** | every count | V1: `67 = 64 + 2 + 1`, over map §0's table of revision `2026-11-20-a` by an independent parse — `2026-11-19-b`'s 66 rows and `docs/l1-sign.html`. V2: `2 of 2`, over `CryptoTZ/` and `CryptoReports/` at `origin/main` — no `TZ-50-` file at `234a6e8`, `TZ-50-l1-account-round-trip.md` alone after the upload. V3: `2` files over Appendices A and B's fenced blocks. V4: `1` path. V5: `7` = H1 1 + H2 2 + H3 1 + H4 1 + memory 1 + disk 1. V7: `5` over `live_gate`'s keys. V9: `6` = K1 and `SSHD_IN_FORCE`'s four, and K6. V10: `135` and `31`, the `ok` calls the two self-tests executed at each of the Architect's runs; `5` and `2` their live refusals, each named in §3.2 and §3.4. V12: `35` over `WHEEL_SET`, `34` over `pins` — the set without `pip`. V16: `7` over `ready_flow`'s keys. V18: `9` over `rt_reading`'s keys; placements at most `2` = `RT_MAX_PLACEMENTS`; records at most `3` = `RT_RECORD`'s digits. G-APPROVE: `2` exchanges over `EXCHANGES`. G-TG: `3`. |
| **C6** | every population | Each of §4's gates names its population in its table's column. The peaks: over the Architect's runs of the two self-tests on these bytes under Python 3.12. `MemAvailable`'s range: map §6's reads since 2026-10-31. The placement's and cancellation's milliseconds: over the round trip's one live order, printed and deciding nothing. The CLOB's view of the balance: over its one read before and after, printed beside the chain's. |
| **C7** | every signature and every behaviour | **Committed, read at `234a6e8`:** `research/tz33-reward-book-capture.py` line 190, `STREAM_FLOOR = 7300000000    # free bytes below which no stream opens for a slot`; `research/tz49-live-host.py`'s `SSHD_TEXT`, hashed. This TZ calls no committed function. **The venue's client, the wheel of Appendix A's set, each signature quoted and each behaviour the body attributes read in its body:** `erc20_approval_call(*, token_address, spender, amount) -> TransactionCall` (`calls.py` line 57) — an `approve` call on the token; `authorize_session_signer_call(*, wallet_address, session_signer, valid_until)` (line 68); `build_deposit_wallet_typed_data(*, wallet, calls, …)` (`deposit_wallet.py` line 30); `build_deposit_wallet_payload(*, signer_address, deposit_wallet_factory, …)` (`gasless.py` line 212), and `wrap_deposit_wallet_signature`, which returns an owner's signature unchanged; `submit_gasless(relayer, *, payload) -> RelayerExecuteResponse`, which posts `/submit` (`submit.py` lines 24 to 27); `resolve_order_exchange_address(config, *, asset_id, neg_risk) -> EvmAddress`, whose first branch, `if is_v2_position_id(asset_id)`, returns `exchange_v3` (`context.py` lines 66 to 69); `build_update_balance_allowance_request(*, asset_type, asset_id=None, …)` (`account.py` line 259) and `signature_type_for(wallet_type) -> int` (`wallet.py` line 68), which the client's own allowance recovery calls before `/balance-allowance/update`; `fetch_execute_params(relayer, *, address, …)` and `fetch_deployed(relayer, *, address, …)`; `derive_uups_deposit_wallet_address(signer, config)` and `derive_beacon_deposit_wallet_address(signer, config)` (`wallet.py` lines 90 and 97); `AsyncSecureClient.create`, whose `_ensure_wallet_ready` reads `/deployed` and, for a session key, deploys nothing; `create_limit_order(…, post_only=True)` and `post_order`, used where `place_limit_order` would try the client's allowance recovery, which a session key cannot sign. **Appendix A's own, each sentence of the body against the lines it cites:** every citation of the form `` `name`, lines a to b `` checked mechanically against the file's own definitions — 48 citations, each the function's or two adjacent functions' span — and every `line N` against the constant it names. |
| **C8** | every cross-reference | **Map, revision `2026-11-20-a`, read in full for each item cited, its disposition column included:** items 86, 89, 91, 95, 98, 119, 124, 127, 132, 137, 138, 140, 143, 144, 150, 156, 163, 169, 174, 175, 176, 177, 180, 181, 183, 184, 185, 186, 187 and 188, each supporting its sentence; **the duties the items leave to the Architect "before" a step** (CANON PART VI, the fifth rule): item 132 — the Boss's steps inside the run with bounds, §3.5 and §3.7; item 175 — the room printed, §0.3; item 184 — the panel's duty is the unit TZ's, and this TZ's part is §1.7's; item 185 — `LC_ALL=C` in `R` and the locale printed once, §0.0 and §0.6; item 186 — the round trip trades either protocol, §1.5, and the reward book's V2 read is the unit TZ's, before it. **CANON** PART II (L1), PART III (hard rules 2, 4, 5, 10, 13 to 17; canonical locations — `docs/l1-sign.html` and L1's relayer key are in its revision `2026-11-20-a`'s table), PART IV (the live host, IPv4 alone, keys, control) and PART VI. **The Executor contract**, `A4` `6ac6e10aeabc`: §1's steps, §4's report and self-check, §5's not-BLOCKED readiness, §6's tests, §8's sections and §10's written authorization. **This file's own sections**, each `§` resolved. **The Boss's words:** none quoted; his message of 2026-11-19 is named, not quoted. |

**Not performable in the session that wrote this TZ, and converted into conditions the run evaluates** (CANON hard rule 13): **(1)** that the live host's Python makes an environment with `venv --without-pip` and that `pip` `24.0` runs from its own wheel there — the Architect ran both on Python 3.12 in his session, not on the live host: B-ENV's `exit=0` and G-ENV installed BLOCK otherwise (§3.4); **(2)** that `gh`'s credential may turn Pages on for this repository: B-PAGES where it may not, and G-PAGE decides (§3.5); **(3)** that the venue takes this owner's Relayer API key, his signature through the page and the session key's orders: G-AUTH, G-APPROVE and G-RT read each from the venue itself; **(4)** that polymarket.com's settings are where B-ACCOUNT names them — read from the venue's documentation and help centre, not seen: each is verified by the mode that reads what it made — `secrets` the key's form, `authorize` the relayer's answer, G-READY the deposit, and the allowlist by the Boss on the site.

---

## Appendix A — the instrument, byte for byte

### `research/tz50-l1-account.py`

```python file=research/tz50-l1-account.py
#!/usr/bin/env python3
"""TZ-50 - L1's account, its session key and one order's round trip at the minimum size, from the live host in Sofia.
The bot's Deposit Wallet is the Boss's; its owner key stays in his MetaMask. This file makes a session key on the live
host, which can trade and cannot withdraw, has the Boss authorize it by his own signature through the signing page,
docs/l1-sign.html, has him approve the wallet's pUSD to the venue's two exchanges at 1 pUSD each where it is short,
and proves one order's round trip with the key through the venue's official client, polymarket-client, installed at
pinned versions and hashes into /root/l1-env. It pins the bot's Telegram chat and reports there.

On the capture host, from /root/tz50-work, under /root/tz04a-env:
    fingerprint       map section 0 against the primary checkout
    number            CANON hard rule 2: of the number TZ-50, this TZ's file alone under CryptoTZ/, no report
    refs              origin's refs by kind; no branch of this TZ yet
    room              the capture's room and its margin (map section 7 item 175); no threshold
    methods LABEL     G-SSH K6: the methods the live host's sshd offers root, read from outside
    scratch OWN       the UUID directories beside this session's own, each named live or earlier
    reclaim TREE...   section 9: the work tree's files into the forensic store
On the live host, from /root/tz50-work, under its system python3 (the standard library alone):
    host LABEL        the live host gate and the facts L1 starts from; exit 1 where the gate fails
    geoblock          G-GEO over IPv4 alone; exit 1 where blocked or unread
    sshd              G-SSH K1 to K5: TZ-49's drop-in and sshd's configuration in force; exit 4 on FAIL
    page              G-PAGE: the signing page as GitHub Pages serves it, byte for byte; exit 4 on FAIL
    wheels            G-ENV's first half: the 35 pinned wheels from PyPI, each by its size and SHA-256
    secrets           the Boss, at his terminal: the bot's Telegram token, the owner's Relayer API key and address
    bosskey           the Boss, at his terminal: his own SSH public key for root, or none
    tg-probe          G-TG's first check: the bot's getMe
    find-chat         G-TG's second: the one private chat that sent /start, pinned
    tg-report         G-TG's third: the round trip's report, sent to that chat
On the live host, from /root/tz50-work, under /root/l1-env/bin/python (the venue's client):
    env               G-ENV's second half: the 34 distributions installed, each at its pin, and the client's terms
    key               G-KEY: the session key, made once, never printed
    authorize         G-AUTH, the Boss at his terminal: the owner's signature from MetaMask, its submission and
                      the key's registration; exit 4 on FAIL
    approve           G-APPROVE, the Boss at his terminal: where the wallet's pUSD allowance to either exchange is
                      under one order's cost, the owner's signature approving 1 pUSD to each such; exit 4 on FAIL
    revoke            the Boss's stop of the order path: the same flow, revoking the key; not run by TZ-50
    ready             G-READY: the account read through the session key; exit 4 on FAIL
    roundtrip         G-RT: one post-only order at the minimum size placed, read, cancelled and read; exit 4 on FAIL
    sdk-selftest      the client's flows against loopback stand-ins of the relayer, the CLOB and gamma
On either host:
    selftest          every rule of this file that needs no client, on literals, temporary trees and loopback servers

IPv4 alone, in this process (map section 7 item 181): every network socket it opens is AF_INET, every name is
resolved in AF_INET alone, and its audit hook refuses an AF_INET6 socket and a lookup in any other family; the
client's modes resolve through a wrapper that asks AF_INET of every lookup. An AF_UNIX socket is let through in the
client's modes alone - asyncio's own self-pipe - and reaches no network. No mode prints to its log a key, a token, an
address of the bot's wallets or keys, a transaction hash or an order's id, and none reads or prints a price or size of
any book; what the Boss must check before he signs - the addresses - goes to his terminal alone.

Written for CryptoTZ/TZ-50-l1-account-round-trip.md. The TZ is the specification.
"""

import asyncio
import base64
import datetime
import getpass
import hashlib
import http.client
import http.server
import json
import os
import re
import resource
import shutil
import socket
import ssl
import struct
import subprocess
import sys
import threading
import time
import types
import urllib.parse

if not __debug__:
    sys.stderr.write("tz50: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

PYFILE = "tz50-l1-account.py"

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------------

MAP_REVISION = "2026-11-20-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "6ac6e10aeabc", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 64, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"(?:`([0-9a-f]{64})`|[^|]*) \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)
NUMBER = "TZ-50-"
OWN_TZ = "CryptoTZ/TZ-50-l1-account-round-trip.md"
BRANCH = "tz-50-l1-account-round-trip"

PRIMARY = "/root/btc-5m-twap"
WORK = "/root/tz50-work"
WT = WORK + "/wt"
TMP = WORK + "/selftest-tmp"
WHEELS = WORK + "/wheels"
FORENSICS = "/root/btc-forensics"
RB = "/var/lib/btc-rewardbook"
RB_ARCHIVE_SVC = "btc-rewardbook-archive.service"
ARCHIVE_READS, ARCHIVE_WAIT_S = 30, 60
CAPTURE_MARK = "/var/lib/btc-recorder"     # map section 6, host identity: on the capture host alone
PROTECTED = ("/var/lib/btc-recorder", "/var/lib/btc-chainbook", "/var/lib/btc-pairbook", RB,
             "/var/lib/btc-rewardbook-archive", "/var/lib/btc-pairbook-archive", "/var/lib/adv3-bot", "/etc/adv3-bot")
LIVE_HOSTNAME = "vs-2348"                  # the host name's first label; the rest is its provider's domain
LIVE_HOST_KEY = ("ssh-ed25519", "SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw")   # TZ-47 report section 2.2
EXECUTOR_KEY = ("ssh-ed25519", "SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo")   # root's key since TZ-47
LIVE_ALIAS = "live-host"                    # root's ~/.ssh/config alias on the capture host; it alone holds the address
HOST_KEY_DIR = "/etc/ssh"
CAPTURE_DISK = "/var/lib"
LIVE_DISK = "/"
IPV4 = re.compile(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}")
ADDRESS = re.compile(r"0x[0-9a-fA-F]{40}")
ZERO_ADDRESS = "0x" + "0" * 40

UA = "btc-5m-twap-tz50"
HEADERS = (("User-Agent", UA), ("Accept", "application/json"))
GEO_HOST, GEO_PATH = "polymarket.com", "/api/geoblock"
CLOB_HOST = "clob.polymarket.com"
RELAYER_HOST = "relayer-v2.polymarket.com"
GAMMA_HOST = "gamma-api.polymarket.com"
RPC_HOST = "polygon.drpc.org"            # the client's own Polygon RPC: the wallet's collateral read on chain
BALANCE_OF = "70a08231"                  # balanceOf(address)
ALLOWANCE_OF = "dd62ed3e"                # allowance(address,address)
APPROVE_SEL = "095ea7b3"                 # approve(address,uint256)
PUSD = "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB"                 # the client's collateral_token
EXCHANGES = (("c", "0xE111180000d2663C0091e4f400237545B87B996B"),   # standard_exchange: a CTF market's orders
             ("v", "0xe3333700cA9d93003F00f0F71f8515005F6c00Aa"))   # exchange_v3: a Protocol V2 market's orders
V2_RESERVED = ((1 << 64) - 1) << 40      # the client's _V2_RESERVED_BITS_MASK: all zero in a V2 position ID
APPROVE_METADATA = "btc-5m-twap TZ-50 approvals"
TG_HOST = "api.telegram.org"
PAGES_HOST, PAGE_PATH = "seahomebatumi-ai.github.io", "/btc-5m-twap/l1-sign.html"
PYPI_HOST = "files.pythonhosted.org"
TIMEOUT_S, READ_MAX = 15, 4194304
TRIES, TRY_GAP_S = 3, 30
PAGE_TRIES = 20                # the page read over ten minutes: GitHub Pages' first build after it is turned on

SSHD_DROPIN = "/etc/ssh/sshd_config.d/00-btc-5m-twap.conf"
SSHD_SHA256 = "94fff8f1f044b31d393eecf24700dabc5b7316c70a37d0f3984cbc5957563624"   # TZ-49's SSHD_TEXT
SSHD_IN_FORCE = (("passwordauthentication", "no"), ("kbdinteractiveauthentication", "no"),
                 ("permitrootlogin", "without-password"), ("pubkeyauthentication", "yes"))
METHODS_ONLY = ["publickey"]
AUTHORIZED_KEYS = "/root/.ssh/authorized_keys"
BOSS_KEY_TYPES = ("ssh-ed25519", "ecdsa-sha2-nistp256", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp521",
                  "sk-ssh-ed25519@openssh.com", "ssh-rsa")
RSA_MIN_BITS = 3072

# ---- L1's files: credentials under /etc/l1-bot, its record under /var/lib/l1-bot, its client under /root/l1-env --

L1_ETC = "/etc/l1-bot"
SESSION_KEY_FILE = L1_ETC + "/session-key"
RELAYER_FILE = L1_ETC + "/relayer-key"
TG_TOKEN_FILE = L1_ETC + "/telegram-token"
CHAT_FILE = L1_ETC + "/chat-id"
L1_VAR = "/var/lib/l1-bot"
ACCOUNT_FILE = L1_VAR + "/account.json"
RT_RECORD = re.compile(r"tz50-roundtrip-([123])\.json")   # one record a run, under L1_VAR; three runs at most
L1_ENV = "/root/l1-env"
SECRETS = (SESSION_KEY_FILE, RELAYER_FILE, TG_TOKEN_FILE, CHAT_FILE)

# ---- the signing page: docs/l1-sign.html on main, served by GitHub Pages ------------------------------------

PAGE_REPO_PATH = "docs/l1-sign.html"
PAGE_SHA256 = "f1d92e7dd8a8cd15b7b96b86b357ebf80db4e10844b3fc269e92cef0aecba528"
PAGE_BYTES = 11846
PAGE_URL = "https://" + PAGES_HOST + PAGE_PATH

# ---- the venue's client, pinned: 34 distributions and pip itself, each by its size and SHA-256 on PyPI ---------

PIP_WHEEL = "pip-24.0-py3-none-any.whl"
WHEEL_SET = (
    ("annotated_types-0.8.0-py3-none-any.whl", 13427, "f072f4d804ea359e4eaf198b1af7a8b0943881a87f31bb764f8bf219bb9419e0",
     "/packages/99/91/8acff4f5e50511b911bbccb72b8628a49c68ce14148cd9f6431094859a90/annotated_types-0.8.0-py3-none-any.whl"),
    ("anyio-4.16.0-py3-none-any.whl", 134521, "c66ae634e0b8228396b801741beb3294326d4b6102f7bba4041c0dfb58c29026",
     "/packages/a9/16/7757fb84c819accc7d7e9af5291b261e4abb8627ee040f99e7d35ef2457a/anyio-4.16.0-py3-none-any.whl"),
    ("bitarray-3.12.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", 404906, "8a32e10bd3c7e287df1e4c3da73efda5585a56ec59337b1467245f53dd469a99",
     "/packages/c0/8a/c9d2e34decc080374ea3dcca6d46c86907c1eb2ea5c47a13c7d0cf28e084/bitarray-3.12.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl"),
    ("certifi-2026.10.23-py3-none-any.whl", 135082, "e9b54de76e530bb6cf0ccd036787103acb58fd42ba930ea8bf948ddbaa2f61d1",
     "/packages/32/d1/a3652fe2c19134d0d15922177821d863cbd7e842d53a21bbe7e8e3a1b5ac/certifi-2026.10.23-py3-none-any.whl"),
    ("ckzg-2.1.8-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", 176775, "10339d23e36b8a0a4e6fda7f6c72d6b2fd4e1506f7b64a661ba8c706ee33f335",
     "/packages/43/af/d0ed7c7b2babfa76e91190a90e8e1f93729d63370493c2c79acfe9002abe/ckzg-2.1.8-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl"),
    ("cytoolz-1.2.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", 3153531, "f99e8e1f1e84522257c4c762ed194106b6b40eeca5a5d181b180fdeb3e927ef5",
     "/packages/8a/25/d782900308fff1872ec5df44b2a2ec36eee97e442657038a2b7e9f25c58c/cytoolz-1.2.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl"),
    ("eth_abi-5.2.0-py3-none-any.whl", 28511, "17abe47560ad753f18054f5b3089fcb588f3e3a092136a416b6c1502cb7e8877",
     "/packages/7a/b4/2f3982c4cbcbf5eeb6aec62df1533c0e63c653b3021ff338d44944405676/eth_abi-5.2.0-py3-none-any.whl"),
    ("eth_account-0.13.7-py3-none-any.whl", 587452, "39727de8c94d004ff61d10da7587509c04d2dc7eac71e04830135300bdfc6d24",
     "/packages/46/18/088fb250018cbe665bc2111974301b2d59f294a565aff7564c4df6878da2/eth_account-0.13.7-py3-none-any.whl"),
    ("eth_hash-0.8.0-py3-none-any.whl", 7965, "523718a51b369ab89866b929a5c93c52978cd866ea309192ad980dd8271f9fac",
     "/packages/87/87/b36792150ca0b28e4df683a34be15a61461ca0e349e5b5cf3ec8f694edb9/eth_hash-0.8.0-py3-none-any.whl"),
    ("eth_keyfile-0.8.1-py3-none-any.whl", 7510, "65387378b82fe7e86d7cb9f8d98e6d639142661b2f6f490629da09fddbef6d64",
     "/packages/88/fc/48a586175f847dd9e05e5b8994d2fe8336098781ec2e9836a2ad94280281/eth_keyfile-0.8.1-py3-none-any.whl"),
    ("eth_keys-0.8.0-py3-none-any.whl", 20461, "a7b94222638cccbdf2b5dae5c365d883a96826d82bb0faeb56baa65375f514ae",
     "/packages/f9/f5/24806598664a2fbc65d5ed4f0e9e986e7f9061e3b43738412c8df7ba1cbd/eth_keys-0.8.0-py3-none-any.whl"),
    ("eth_rlp-3.0.0-py3-none-any.whl", 15221, "32f355261c36ad2c369db098170f873123795667e50d496b034f369e2c9d2346",
     "/packages/ab/35/a3071f2a7ee701f99c8562865edbc426991d0964543d2947901b4135f259/eth_rlp-3.0.0-py3-none-any.whl"),
    ("eth_typing-6.0.0-py3-none-any.whl", 19191, "ee74fb641eb36dd885e1c42c2a3055314efa532b3e71480816df70a94d35cfb9",
     "/packages/aa/0d/e756622fab29f404d846d7464f929d642a7ee6eff5b38bcc79e7c64ac630/eth_typing-6.0.0-py3-none-any.whl"),
    ("eth_utils-5.3.1-py3-none-any.whl", 102529, "1f5476d8f29588d25b8ae4987e1ffdfae6d4c09026e476c4aad13b32dda3ead0",
     "/packages/bf/4d/257cdc01ada430b8e84b9f2385c2553f33218f5b47da9adf0a616308d4b7/eth_utils-5.3.1-py3-none-any.whl"),
    ("h11-0.16.0-py3-none-any.whl", 37515, "63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86",
     "/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl"),
    ("h2-4.4.1-py3-none-any.whl", 62636, "0e25f1462b23c9cb82d9eb02e28bc706dac2a68cb457c6a0d74d63c8a2a5d0e6",
     "/packages/7e/22/e85faf23bd72a92d1921e37d674ca56eb298a3c8be31fdecef0ff2b3aaac/h2-4.4.1-py3-none-any.whl"),
    ("hexbytes-2.0.0-py3-none-any.whl", 18866, "5425bd7ac83cdd9791c13a5bf97cfe9b9609a304b1ef3ab146adfd50de06cf0e",
     "/packages/e8/72/c7049aabd9e05efebc29b10208b11e5ae5cf819f48685ffced6abf871d10/hexbytes-2.0.0-py3-none-any.whl"),
    ("hpack-4.2.0-py3-none-any.whl", 34246, "858ac0b02280fa582b5080d68db0899c62a80375e0e5413a74970c5e518b6986",
     "/packages/71/b4/4a9fcfb2aef6ba44d9073ecd301443aa00b3dac95de5619f2a7de7ec8a91/hpack-4.2.0-py3-none-any.whl"),
    ("httpcore-1.0.9-py3-none-any.whl", 78784, "2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55",
     "/packages/7e/f5/f66802a942d491edb555dd61e3a9961140fd64c90bce1eafd741609d334d/httpcore-1.0.9-py3-none-any.whl"),
    ("httpx-0.28.1-py3-none-any.whl", 73517, "d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad",
     "/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl"),
    ("hyperframe-6.1.0-py3-none-any.whl", 13007, "b03380493a519fce58ea5af42e4a42317bf9bd425596f7a0835ffce80f1a42e5",
     "/packages/48/30/47d0bf6072f7252e6521f3447ccfa40b421b6824517f82854703d0f5a98b/hyperframe-6.1.0-py3-none-any.whl"),
    ("idna-3.20-py3-none-any.whl", 69583, "ab7ae7122974553370f0bdb919e1a960b2cd1bc1ef0276416d896db81c14582c",
     "/packages/58/a2/bb081bab032533a855d44de1d56f8e8426114ff1ba5d1f07a438a0a654f8/idna-3.20-py3-none-any.whl"),
    ("msgpack-1.2.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", 475652, "c4d5bbdbea8f5669b3a734d6c226772804fb120848f99cbe63a0ddee63b049c9",
     "/packages/1e/d9/f59bd841fc2fd2b74dc50ce85860a6a25f58e588dd48946aeaf2862cf990/msgpack-1.2.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl"),
    ("parsimonious-0.10.0-py3-none-any.whl", 48427, "982ab435fabe86519b57f6b35610aa4e4e977e9f02a14353edf4bbc75369fc0f",
     "/packages/aa/0f/c8b64d9b54ea631fcad4e9e3c8dbe8c11bb32a623be94f22974c88e71eaf/parsimonious-0.10.0-py3-none-any.whl"),
    ("polymarket_client-0.20.0-py3-none-any.whl", 428375, "677e074364bc051e330b1430e22b634ddf308e95c7ba6ca85645cd82741625c6",
     "/packages/25/91/e0d5814619fbab8ed9614f3791624834580fb619bb39f76792824baa3970/polymarket_client-0.20.0-py3-none-any.whl"),
    ("pycryptodome-3.24.1-cp37-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", 2276644, "93619c3117a8f14ea1267b427e465d152a66c89c3d3c643262070c05b2855aae",
     "/packages/a0/3f/e6a6b5d261746378a9267af50463d6aa01f88f88c98bedfd404c94eb7ec6/pycryptodome-3.24.1-cp37-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl"),
    ("pydantic-2.14.3-py3-none-any.whl", 494071, "3f7b347782ab7e4cf4c798496ae3a82787d9f21ec12676a9c564355eeef8daa8",
     "/packages/72/b8/b864503789ef5c58597d2a7b4adbee62c26440ab1e682581fc6838df8947/pydantic-2.14.3-py3-none-any.whl"),
    ("pydantic_core-2.50.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", 2261727, "c81d98e27d9d9261909dcccab1ba5d6ea1c98b0bb9470e368604614fd1d36ddd",
     "/packages/91/23/e0c6e3cd09a0ac809953fea698c816b9f03bf0b35b6820c9553e4f5d85a8/pydantic_core-2.50.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl"),
    ("regex-2026.11.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", 808826, "ab4a0c5cd3df4b93841ba4a419a5438b2a4c78a4e418682fc674e3f50d56b857",
     "/packages/46/c2/59c5b6cf4b762d80de04cf60f2d0deba1da2f4172a91c41eaee8933080a8/regex-2026.11.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl"),
    ("rlp-5.0.0-py3-none-any.whl", 19832, "9525fb895d3a6540b7401eadd11c1b64740a5eccb82e543ac7e9735d319b0977",
     "/packages/a7/35/26ea7adca149e506bb03c50ade0c4d96cf269e6fc13a2b3f726d65905ffb/rlp-5.0.0-py3-none-any.whl"),
    ("toolz-1.2.0-py3-none-any.whl", 60789, "890f820b1cb8152785aaf9386d8707770110809035800985ca65cb24ce1120ef",
     "/packages/db/17/4c8beb6c8c4176c6bf143bfd7e1e4dd6719b00ced90738c7ac471b71c1df/toolz-1.2.0-py3-none-any.whl"),
    ("typing_extensions-4.16.0-py3-none-any.whl", 45571, "481caa481374e813c1b176ada14e97f1f67a4539ce9cfeb3f350d78d6370c2e8",
     "/packages/49/d3/b8441a820a491ddfc024b0b0cf0393375b75ea13866d9c66727e54c2fc80/typing_extensions-4.16.0-py3-none-any.whl"),
    ("typing_inspection-0.4.5-py3-none-any.whl", 14874, "bc210535442b39e1bf2805e0c7a17dfd6a4ace760c84c7f7d16245d23a6b1c39",
     "/packages/de/0c/ea2544850a7c135e15033a5c7a8e7211136184b7ae63e2239d557c2b3019/typing_inspection-0.4.5-py3-none-any.whl"),
    ("websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", 182523, "64dee438fed052b52e4f98f76c5790513235efaa1ef7f3f2192c392cd7c91b65",
     "/packages/14/8f/aa61f528fba38578ec553c145857a181384c72b98156f858ca5c8e82d9d3/websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl"),
    ("pip-24.0-py3-none-any.whl", 2110226, "ba0d021a166865d2265246961bec0152ff124de910c5cc39f1156ce3fa7c69dc",
     "/packages/8a/6a/19e9fe04fca059ccf770861c7d5721ab4c2aebc539889e97c7977528a53b/pip-24.0-py3-none-any.whl"),
)
SDK_DIST, SDK_VERSION = "polymarket-client", "0.20.0"

# ---- the venue's terms, read on 2026-11-19 from the client's own source and docs.polymarket.com -----------------

CHAIN_ID = 137
SCOPES = ("CLOB",)
LIFETIME_S = 15534000          # 4,315 h: the client's _SESSION_KEY_LIFETIME_SECONDS; the venue's 180 days less 5 h
DEADLINE_S = 600               # the client's _DEPOSIT_WALLET_DEADLINE_S: a signed batch's validity
SELECTORS = {"authorize": "24017fae", "revoke": "e63f952f"}   # authorizeSessionSigner(address,uint256), revoke...(address)
LINKS, SIGNATURE_TRIES = 3, 3  # fresh signing links, and signatures asked of one link
READY_TRIES, READY_GAP_S = 30, 10

# ---- the round trip ---------------------------------------------------------------------------------------------

RT_FAMILY = "btc-updown-5m-"
RT_WINDOW_S = 300
RT_MIN_LEFT_S = 150            # the window open at placement keeps at least this long; else the next is waited for
RT_PRICE = "0.01"              # the lowest price on either tick the family uses, 0.01 or 0.001 (map section 6)
RT_SIZE = "5"                  # the family's minimum order size (map section 6, venue constants)
RT_MAX_PLACEMENTS = 2         # its Up token, and its Down token where the first crosses the book
RT_COST_UNITS = 50000          # 5 shares at 0.01, in the collateral's six-decimal units: what one fill can cost
RT_LOSS_MAX_UNITS = RT_COST_UNITS * RT_MAX_PLACEMENTS            # 0.10 pUSD: this TZ's whole loss, at most
APPROVE_UNITS = 1000000        # 1 pUSD to each exchange whose allowance is short, never the maximum: what a key can
                               # spend through that exchange until another TZ approves more
RT_SIDES = ("Up", "Down")

# ---- Telegram ---------------------------------------------------------------------------------------------------

TG_WAIT_S = 1800
TOKEN_RE = re.compile(r"[0-9]{5,12}:[A-Za-z0-9_-]{30,64}")
RELAYER_KEY_RE = re.compile(r"[A-Za-z0-9._:-]{16,256}")

# ---- floors -----------------------------------------------------------------------------------------------------

STREAM_FLOOR = 7300000000    # research/tz33-reward-book-capture.py line 190
PEAK = 445535636             # fourteen slots of 31,823,974 bytes (TZ-46; map section 6)
MARGIN_WATCH = 1000000000    # map section 7 item 175
SESSION_WRITES = 50000000    # this session's writes on the capture host, at most
CAPTURE_FLOOR = STREAM_FLOOR + PEAK + SESSION_WRITES                       # 7,795,535,636
JOURNAL_KEEP_FREE = 2147483648                                             # TZ-49's SystemKeepFree=2G
L1_ENV_MAX = 200000000       # the client's tree, 47,855,239 bytes installed by the Architect, with room
LIVE_WORK_MAX = 100000000    # the live work tree: the wheels, 14,422,773 bytes, and the logs
LIVE_FLOOR = JOURNAL_KEEP_FREE + L1_ENV_MAX + LIVE_WORK_MAX                 # 2,447,483,648
RECLAIM_FLOOR = STREAM_FLOOR + 100000000
MEM_FLOOR = 85051706          # twice 42,525,853: selftest's 35,467,264 at TZ-37's ratio, 58,953,728 / 49,168,384
MEM_FLOOR_SDK = 275045368     # twice 137,522,684: sdk-selftest's 114,696,192 at the same ratio (map item 156)
MEM_READS, MEM_WAIT_S = 5, 60

UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
DAY_RE = re.compile(r"[0-9]{10}")
RB_STREAM_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.stream\.jsonl\.gz")
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
LIVE_S = 60

# ---- the audit hook: TZ-50 section 2 as a pure function, and the hook that applies it -------------------------

MODE = [None]
REFUSED = []
RESOLVED = set()
COUNTS = {"lookups": 0, "requests": 0}
CLIENT_MODES = ("env", "key", "authorize", "approve", "revoke", "ready", "roundtrip", "sdk-selftest")
TTY_MODES = ("secrets", "bosskey", "authorize", "approve", "revoke")
NET = {"geoblock": (GEO_HOST,), "page": (PAGES_HOST,), "wheels": (PYPI_HOST,),
       "tg-probe": (TG_HOST,), "find-chat": (TG_HOST,), "tg-report": (TG_HOST,),
       "authorize": (RELAYER_HOST, CLOB_HOST), "revoke": (RELAYER_HOST, CLOB_HOST), "approve": (RELAYER_HOST, RPC_HOST),
       "ready": (RELAYER_HOST, CLOB_HOST, RPC_HOST), "roundtrip": (RELAYER_HOST, CLOB_HOST, GAMMA_HOST, RPC_HOST),
       "selftest": ("127.0.0.1",), "sdk-selftest": ("127.0.0.1",)}
EXECS = {"number": ("git",), "refs": ("git",), "room": ("systemctl",), "scratch": ("stat",), "reclaim": ("git", "stat"),
         "methods": ("ssh",), "host": ("systemctl", "timedatectl", "locale"), "sshd": ("sshd",)}
for _m in CLIENT_MODES:      # pycryptodome's import runs platform.architecture(), which runs `file` on the interpreter
    EXECS[_m] = ("file", "timedatectl") if _m == "roundtrip" else ("file",)
READS = {SESSION_KEY_FILE: ("key", "authorize", "revoke", "ready", "roundtrip"),
         RELAYER_FILE: ("secrets", "authorize", "approve", "revoke"),
         TG_TOKEN_FILE: ("secrets", "tg-probe", "find-chat", "tg-report"),
         CHAT_FILE: ("find-chat", "tg-report")}
WRITES = {SESSION_KEY_FILE: ("key",), RELAYER_FILE: ("secrets",), TG_TOKEN_FILE: ("secrets",),
          CHAT_FILE: ("find-chat",), AUTHORIZED_KEYS: ("bosskey",),
          ACCOUNT_FILE: ("secrets", "authorize", "approve", "revoke"),
          ACCOUNT_FILE + ".tmp": ("secrets", "authorize", "approve", "revoke")}
EXCLUSIVE = (SESSION_KEY_FILE, RELAYER_FILE, TG_TOKEN_FILE, CHAT_FILE)
MKDIRS = {L1_ETC: ("secrets", "key"), L1_VAR: ("secrets", "authorize", "approve", "revoke", "roundtrip")}
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
CHANGE_EVENTS = ("os.remove", "os.rename", "os.rmdir", "os.mkdir", "os.truncate", "os.chmod", "os.chown",
                 "os.utime", "os.link", "os.symlink", "shutil.rmtree", "shutil.copyfile")
HOOKED = ("open", "os.listdir", "os.scandir", "socket.__new__", "socket.getaddrinfo", "socket.connect",
          "subprocess.Popen") + CHANGE_EVENTS


class GuardError(RuntimeError):
    pass


def _under(p, root):
    return p == root or p.startswith(root + "/")


def _path(p):
    if isinstance(p, bytes):
        p = os.fsdecode(p)
    return os.path.abspath(p) if isinstance(p, str) else None


def _writing(wmode, flags):
    if isinstance(wmode, str):
        return bool(set(wmode) & set("wax+"))
    return isinstance(flags, int) and bool(flags & WRITE_FLAGS)


def _exclusive(wmode, flags):
    if isinstance(wmode, str):
        return "x" in wmode
    return isinstance(flags, int) and bool(flags & os.O_EXCL)


def _appending(wmode, flags):
    if isinstance(wmode, str):
        return wmode in ("a", "ab")
    return isinstance(flags, int) and bool(flags & os.O_APPEND) and not flags & os.O_TRUNC


def policy(mode, event, args):
    """None where TZ-50 section 2 allows the event in this mode; otherwise why it is refused. Pure but for the
    addresses this process resolved from an allowed name. IPv4 alone (map section 7 item 181): a network socket of
    any family but AF_INET, a lookup in any family but AF_INET and a connection to anything but an IPv4 address are
    refused in every mode; an AF_UNIX socket is let through in the client's modes alone, asyncio's self-pipe."""
    if event == "socket.__new__":
        fam = args[1] if len(args) > 1 else None
        if fam == socket.AF_INET or (fam == socket.AF_UNIX and mode in CLIENT_MODES):
            return None
        return "a socket of family %r: IPv4 alone" % (fam,)
    if event == "socket.getaddrinfo":
        host = args[0] if args else None
        if isinstance(host, bytes):
            host = host.decode("ascii", "replace")
        fam = args[2] if len(args) > 2 else None
        if fam != socket.AF_INET:
            return "a lookup of %r in family %r: IPv4 alone" % (host, fam)
        return None if host in RESOLVED or host in NET.get(mode, ()) else "a lookup of %r" % (host,)
    if event == "socket.connect":
        addr = args[1] if len(args) > 1 else None
        if isinstance(addr, (str, bytes)) and mode in CLIENT_MODES:
            return None                     # an AF_UNIX path: asyncio's self-pipe never connects one, but nothing else may
        ok = isinstance(addr, tuple) and len(addr) == 2 and isinstance(addr[0], str) \
            and IPV4.fullmatch(addr[0]) is not None and (addr[0] in RESOLVED or addr[0] in NET.get(mode, ()))
        return None if ok else "a connection to %r" % (addr,)
    if event == "subprocess.Popen":
        exe = args[0] if args and args[0] else (args[1][0] if len(args) > 1 and args[1] else None)
        name = os.path.basename(os.fsdecode(exe)) if exe is not None else None
        return None if name in EXECS.get(mode, ()) else "running %r" % (name,)
    p = _path(args[0]) if args else None
    if p is None:
        return None
    if event == "open":
        wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
        if any(_under(p, r) for r in PROTECTED):
            return "an open under a capture's store or the advisor's credentials"
        if p == "/dev/tty":
            return None if mode in TTY_MODES else "the terminal outside the Boss's modes"
        if p == "/dev/null":
            return None
        if p in READS and mode not in READS[p] and not _writing(wm, fl):
            return "a read of %s in mode %s" % (p, mode)
        if _writing(wm, fl):
            if _under(p, FORENSICS):
                return None if mode == "reclaim" and _exclusive(wm, fl) else "a write into the forensic store"
            if os.path.dirname(p) == L1_VAR and RT_RECORD.fullmatch(os.path.basename(p)):
                return None if mode == "roundtrip" and _exclusive(wm, fl) else "a round trip's record in mode %s" % mode
            if p in WRITES:
                if mode not in WRITES[p]:
                    return "a write of %s in mode %s" % (p, mode)
                if p in EXCLUSIVE and not _exclusive(wm, fl):
                    return "a write of %s that is not an exclusive create" % p
                if p == AUTHORIZED_KEYS and not _appending(wm, fl):
                    return "a write of %s that is not an append" % p
                return None
            if not _under(p, WORK):
                return "a write outside the work tree"
        return None
    if event in ("os.listdir", "os.scandir"):
        if _under(p, RB):
            return None if mode == "room" else "a listing of the reward book's store"
        return "a listing under a capture's store" if any(_under(p, r) for r in PROTECTED) else None
    paths = [p]
    if event in ("os.rename", "os.link", "os.symlink", "shutil.copyfile") and len(args) > 1:
        paths.append(_path(args[1]))
    for q in paths:
        if q is None or _under(q, WORK):
            continue
        if event == "os.mkdir" and q in MKDIRS and mode in MKDIRS[q]:
            continue
        if event == "os.chmod" and q in WRITES and mode in WRITES[q]:
            continue
        if event == "os.rename" and q in (ACCOUNT_FILE, ACCOUNT_FILE + ".tmp") and mode in WRITES[ACCOUNT_FILE]:
            continue
        return "a change outside the work tree"
    return None


def _audit(event, args):
    if event not in HOOKED:
        return
    why = policy(MODE[0], event, args)
    if why is not None:
        REFUSED.append((event, MODE[0]))
        raise GuardError("%s refused in mode %s: %s" % (event, MODE[0], why))


sys.addaudithook(_audit)
_GAI = socket.getaddrinfo


def gai4(host, port, family=0, type=0, proto=0, flags=0):
    """socket.getaddrinfo with AF_INET asked of every lookup that asks for no family, and any other family refused:
    the client's modes resolve through it, so httpx and asyncio open IPv4 sockets alone (map section 7 item 181)."""
    if family in (0, socket.AF_UNSPEC):
        family = socket.AF_INET
    if family != socket.AF_INET:
        raise GuardError("a lookup of %r in family %r: IPv4 alone" % (host, family))
    infos = _GAI(host, port, family, type, proto, flags)
    RESOLVED.update(ai[4][0] for ai in infos if ai[0] == socket.AF_INET)
    COUNTS["lookups"] += 1
    return infos

# ---- small helpers ------------------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return datetime.datetime.fromtimestamp(float(t), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path, chunk=1 << 20):
    """The SHA-256 and the byte count of a file read as bytes."""
    h, n = hashlib.sha256(), 0
    with open(path, "rb") as fh:
        for b in iter(lambda: fh.read(chunk), b""):
            h.update(b)
            n += len(b)
    return h.hexdigest(), n


def read_text(path, default=None):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return default


def meminfo(text):
    """The fields of /proc/meminfo in bytes. Pure."""
    found = {}
    for line in text.split("\n"):
        f = line.split()
        if len(f) >= 2 and f[0].endswith(":") and f[1].isdigit():
            found[f[0][:-1]] = int(f[1]) * (1024 if len(f) > 2 and f[2] == "kB" else 1)
    return found


def mem_available():
    return meminfo(read_text("/proc/meminfo", ""))["MemAvailable"]


def fs_bytes(path):
    """Total, available and free bytes of the file system holding `path`."""
    st = os.statvfs(path)
    return st.f_blocks * st.f_frsize, st.f_bavail * st.f_frsize, st.f_bfree * st.f_frsize


def floors(disk, disk_floor, mem_floor=None, read=mem_available, sleep=time.sleep, statf=fs_bytes):
    """At a mode's start: MemAvailable read up to five times 60 s apart, the first at or above the memory floor
    passing - the client's modes' own where they run; the available bytes of `disk` at or above disk_floor."""
    mem_floor = mem_floor or (MEM_FLOOR_SDK if MODE[0] in CLIENT_MODES else MEM_FLOOR)
    for k in range(1, MEM_READS + 1):
        m = read()
        out("MemAvailable read %d: %d bytes, floor %d" % (k, m, mem_floor))
        if m >= mem_floor:
            break
        assert k < MEM_READS, "BLOCKED: MemAvailable below %d at %d reads" % (mem_floor, MEM_READS)
        sleep(MEM_WAIT_S)
    avail = statf(disk)[1]
    out("available on %s: %d bytes, floor %d" % (disk, avail, disk_floor))
    assert avail >= disk_floor, "BLOCKED: %d bytes available on %s, below %d" % (avail, disk, disk_floor)
    return avail


def run(argv, timeout=20, env=None):
    """A command under TZ=UTC and the C locale, or under `env` where given: (exit, stdout, stderr)."""
    cp = subprocess.run(argv, capture_output=True, text=True, timeout=timeout,
                        env=env if env is not None else dict(os.environ, **SHOW_ENV))
    return cp.returncode, cp.stdout, cp.stderr


def show(unit, props):
    """systemctl show: {property: value}."""
    args = ["systemctl", "show", unit]
    for p in props:
        args += ["-p", p]
    rc, so, se = run(args)
    assert rc == 0, "systemctl show %s: %s" % (unit, se.strip())
    kv = {}
    for line in so.split("\n"):
        if "=" in line:
            k, v = line.split("=", 1)
            kv[k] = v
    return kv


def git(*args, tree=PRIMARY):
    rc, so, se = run(["git", "-C", tree] + list(args), timeout=120)
    assert rc == 0, "git %s: %s" % (" ".join(args), se.strip()[:300])
    return so.strip()


def record(kind, obj):
    out("RECORD %s %s" % (kind, json.dumps(obj, sort_keys=True, separators=(",", ":"))))


def is_capture_host():
    return os.path.isdir(CAPTURE_MARK)


def first_label(name):
    """A host name to its first dot. Pure."""
    return name.split(".", 1)[0]


def short_hostname():
    return first_label(socket.gethostname())


def key_fingerprints(text):
    """The type and SHA256 fingerprint of each key line of an authorized_keys or .pub text, in ssh-keygen's form;
    never a key's comment. Pure."""
    found = []
    for ln in text.split("\n"):
        f = ln.split()
        for i, w in enumerate(f[:-1]):
            if w.startswith("ssh-") or w.startswith("ecdsa-") or w.startswith("sk-"):
                try:
                    blob = base64.b64decode(f[i + 1], validate=True)
                except ValueError:
                    break
                found.append((w, "SHA256:" + base64.b64encode(hashlib.sha256(blob).digest()).decode().rstrip("=")))
                break
    return found


def host_keys():
    names = sorted(os.listdir(HOST_KEY_DIR)) if os.path.isdir(HOST_KEY_DIR) else []
    found = []
    for n in names:
        if n.startswith("ssh_host_") and n.endswith("_key.pub"):
            found += key_fingerprints(read_text(os.path.join(HOST_KEY_DIR, n), "") or "")
    return sorted(found)


def is_live_host():
    return (short_hostname() == LIVE_HOSTNAME and LIVE_HOST_KEY in host_keys()
            and not os.path.exists(CAPTURE_MARK))


def assert_live():
    assert is_live_host(), "BLOCKED: this mode runs on the live host %s and nowhere else" % LIVE_HOSTNAME


def file_state(path):
    """A path's kind, mode, owner and size - never its content: what may be printed of a credential."""
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return "absent"
    kind = "dir" if os.path.isdir(path) and not os.path.islink(path) else (
        "file" if os.path.isfile(path) and not os.path.islink(path) else "other")
    return "%s mode %04o uid %d bytes %d" % (kind, st.st_mode & 0o7777, st.st_uid, st.st_size)


def private_file_ok(path, mode=0o600):
    """A regular file, not a link, root's, of `mode`, and not empty."""
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return False
    return (os.path.isfile(path) and not os.path.islink(path) and st.st_uid == 0
            and st.st_mode & 0o7777 == mode and st.st_size > 0)


def write_private(path, data, dir_mode=0o700):
    """`data` to `path` by exclusive create, 0600 from its first byte; its directory made 0700 where absent.
    Returns the bytes written."""
    d = os.path.dirname(path)
    if not os.path.isdir(d):
        os.mkdir(d, dir_mode)
    st = os.lstat(d)
    assert st.st_uid == 0 and st.st_mode & 0o7777 == dir_mode and not os.path.islink(d), \
        "%s: %s" % (d, file_state(d))
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        os.write(fd, data)
        os.fsync(fd)
    finally:
        os.close(fd)
    assert private_file_ok(path), "%s: %s" % (path, file_state(path))
    return len(data)


def write_json_atomic(path, obj, dir_mode=0o700):
    """`obj` as JSON to `path` through `path`.tmp and a rename, 0600."""
    d = os.path.dirname(path)
    if not os.path.isdir(d):
        os.mkdir(d, dir_mode)
    tmp = path + ".tmp"
    data = (json.dumps(obj, sort_keys=True, indent=1) + "\n").encode()
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        os.write(fd, data)
        os.fsync(fd)
    finally:
        os.close(fd)
    os.rename(tmp, path)
    return len(data)

# ---- the network, standard library: IPv4 alone, every request with this TZ's agent --------------------------


def resolve(host, port=443):
    """The IPv4 addresses of `host`, sorted; each is the only address a later connection may use. An address
    literal is its own."""
    if IPV4.fullmatch(host):
        return [host]
    infos = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
    addrs = sorted({ai[4][0] for ai in infos})
    RESOLVED.update(addrs)
    COUNTS["lookups"] += 1
    return addrs


def connect4(addr, port, timeout):
    """A TCP connection to the IPv4 address `addr`: its socket AF_INET by construction, and no lookup made."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(timeout)
        s.connect((addr, port))
    except BaseException:
        s.close()
        raise
    return s


def err_of(exc):
    """An error as printed: its type, errno and the C library's message - never an address. Pure."""
    no, msg = getattr(exc, "errno", None), getattr(exc, "strerror", None)
    return "%s errno %s: %s" % (type(exc).__name__, no, msg) if no is not None else type(exc).__name__


def http_call(base, method, path, body=None, timeout=TIMEOUT_S, max_bytes=READ_MAX):
    """One request over a fresh IPv4 connection to base = (scheme, host, port), every header this TZ's: (status,
    headers, body, the connection's own source address). A body over max_bytes is refused."""
    scheme, host, port = base
    addr = resolve(host, port)[0]
    if scheme == "https":
        c = http.client.HTTPSConnection(host, port, timeout=timeout, context=ssl.create_default_context())
    else:
        c = http.client.HTTPConnection(host, port, timeout=timeout)
    c._create_connection = lambda address, timeout=None, source_address=None: connect4(addr, port, timeout)
    hdrs = dict(HEADERS)
    data = None
    if body is not None:
        data = json.dumps(body, separators=(",", ":")).encode()
        hdrs["Content-Type"] = "application/json"
    try:
        c.request(method, path, body=data, headers=hdrs)
        src = c.sock.getsockname()[0]
        r = c.getresponse()
        blob = r.read(max_bytes + 1)
        assert len(blob) <= max_bytes, "a reply over %d bytes" % max_bytes
        COUNTS["requests"] += 1
        return r.status, {k.lower(): v for k, v in r.getheaders()}, blob, src
    finally:
        c.close()


def json_of(blob):
    try:
        return json.loads(blob.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return None

# ---- the readings: pure -------------------------------------------------------------------------------------


def number_reading(names, own):
    """NUMBER, CANON hard rule 2: CryptoTZ/ holds this TZ's file and no other of its number; CryptoReports/ no report
    of it. Pure."""
    tz = [n for n in names if n.startswith("CryptoTZ/" + NUMBER)]
    rp = [n for n in names if n.startswith("CryptoReports/" + NUMBER)]
    return tz == [own] and not rp, tz, rp


def refs_reading(text):
    """origin's refs counted by kind, and whether this TZ's branch is among them. Pure."""
    kinds, branch = {}, False
    for ln in text.split("\n"):
        if "\t" not in ln:
            continue
        ref = ln.split("\t", 1)[1].strip()
        branch = branch or ref == "refs/heads/" + BRANCH
        if ref in ("HEAD", "refs/heads/main"):
            k = ref
        elif ref.startswith("refs/heads/tz-"):
            k = "refs/heads/tz-*"
        elif ref.startswith("refs/pull/"):
            k = "refs/pull/*/" + ref.rsplit("/", 1)[1]
        elif ref.startswith("refs/tags/pairbook-streams-") or ref.startswith("refs/tags/rewardbook-streams-"):
            k = ref.split("-streams-", 1)[0] + "-streams-*" + ("^{}" if ref.endswith("^{}") else "")
        else:
            k = ref
        kinds[k] = kinds.get(k, 0) + 1
    return kinds, branch


def room_reading(avail, streams):
    """The room and its margin over the stream floor and PEAK (map section 7 item 175). Pure."""
    room = avail + streams
    return room, room - STREAM_FLOOR - PEAK


def geo_fields(doc):
    """What may be printed of the venue's reply: blocked, country and region, and its keys' names - never the
    address it carries. Pure."""
    if not isinstance(doc, dict):
        return None
    return {"blocked": doc.get("blocked"), "country": doc.get("country"), "region": doc.get("region"),
            "keys": sorted(str(k) for k in doc)}


def geo_reading(status, doc):
    """One geoblock read: UNREAD unless status 200 and a reply whose blocked is a boolean and whose country is two
    capital letters; else BLOCKED where blocked is true, PASS where it is false. Pure."""
    f = geo_fields(doc)
    if status != 200 or f is None or not isinstance(f["blocked"], bool) \
            or not (isinstance(f["country"], str) and re.fullmatch(r"[A-Z]{2}", f["country"])):
        return "UNREAD"
    return "BLOCKED" if f["blocked"] else "PASS"


def os_release(text):
    found = {}
    for ln in text.split("\n"):
        if "=" in ln and not ln.startswith("#"):
            k, v = ln.split("=", 1)
            found[k.strip()] = v.strip().strip('"')
    return found


def live_gate(hostname, osrel, pyver, capture_paths, keys):
    """The live host gate's five checks, TZ-49's: `hostname` the first label of the host's name, `keys` its SSH host
    keys by type and fingerprint. Pure."""
    checks = {"LH1 hostname %s" % LIVE_HOSTNAME: hostname == LIVE_HOSTNAME,
              "LH2 Ubuntu 24.04": osrel.get("ID") == "ubuntu" and osrel.get("VERSION_ID") == "24.04",
              "LH3 Python 3.12": tuple(pyver[:2]) == (3, 12),
              "LH4 not the capture host": not capture_paths,
              "LH5 the host key pinned at TZ-47's first connection": LIVE_HOST_KEY in keys}
    return all(checks.values()), checks


def sshd_effective(text):
    """`sshd -T` text: each keyword and its value, the last line of a keyword kept. Pure."""
    found = {}
    for ln in text.split("\n"):
        f = ln.strip().split(None, 1)
        if len(f) == 2:
            found[f[0].lower()] = f[1].strip()
    return found


def ssh_reading(dropin, effective):
    """G-SSH's K1 to K5: `dropin` TZ-49's sshd drop-in's (SHA-256, mode) or None; `effective` sshd_effective's
    reading of `sshd -T`. Pure."""
    checks = {"K1 TZ-49's sshd drop-in, byte for byte": dropin == (SSHD_SHA256, 0o644)}
    for i, (k, v) in enumerate(SSHD_IN_FORCE, 2):
        checks["K%d %s %s" % (i, k, v)] = effective.get(k) == v
    return all(checks.values()), checks


METHODS_RE = re.compile(r"Authentications that can continue: ([A-Za-z0-9@.,_-]+)")


def methods_of(text):
    """The lists of authentication methods an sshd offered, from `ssh -v` text: each list once, sorted - nothing
    else of the text, which carries the address. Pure."""
    return sorted(set(METHODS_RE.findall(text)))


def reclaimable(tree):
    if tree == WORK:
        return True
    return (tree.startswith("/tmp/") and os.path.isdir(tree) and not os.path.islink(tree)
            and UUID.fullmatch(os.path.basename(tree)) is not None
            and "btc-5m-twap" in os.path.basename(os.path.dirname(tree)))


def _ssh_string(blob, i):
    assert i + 4 <= len(blob), "a truncated key"
    n = struct.unpack(">I", blob[i:i + 4])[0]
    assert i + 4 + n <= len(blob), "a truncated key"
    return blob[i + 4:i + 4 + n], i + 4 + n


def pubkey_line(text):
    """The Boss's SSH public key as one line of authorized_keys: (the line, its type, its fingerprint, its bits for
    RSA). Refuses a private key, options, two lines, an unknown type, a blob whose own type differs from its line's,
    and RSA under RSA_MIN_BITS. Pure."""
    line = text.strip()
    if not line:
        raise ValueError("empty")
    if "PRIVATE" in line.upper() or "\n" in line or "\r" in line:
        raise ValueError("not one public key line")
    f = line.split()
    if len(f) < 2 or f[0] not in BOSS_KEY_TYPES:
        raise ValueError("not a public key of a known type at the line's start")
    try:
        blob = base64.b64decode(f[1], validate=True)
    except ValueError:
        raise ValueError("the key is not base64")
    try:
        kind, i = _ssh_string(blob, 0)
        assert kind.decode("ascii") == f[0], "the key's own type differs"
        bits = None
        if f[0] == "ssh-rsa":
            _e, i = _ssh_string(blob, i)
            n, i = _ssh_string(blob, i)
            bits = int.from_bytes(n, "big").bit_length()
            assert bits >= RSA_MIN_BITS, "RSA of %d bits" % bits
        elif f[0] == "ssh-ed25519":
            pk, i = _ssh_string(blob, i)
            assert len(pk) == 32, "an ed25519 key of %d bytes" % len(pk)
        assert i <= len(blob)
    except (AssertionError, UnicodeDecodeError) as exc:
        raise ValueError(str(exc) or "a malformed key")
    fp = "SHA256:" + base64.b64encode(hashlib.sha256(blob).digest()).decode().rstrip("=")
    return " ".join(f), f[0], fp, bits


def valid_address(text):
    """An EVM address as typed: its lowercase form, or None. Pure."""
    t = (text or "").strip()
    if not ADDRESS.fullmatch(t) or t.lower() == ZERO_ADDRESS:
        return None
    return t.lower()


def token_ok(text):
    return isinstance(text, str) and TOKEN_RE.fullmatch(text) is not None


def relayer_key_ok(text):
    return isinstance(text, str) and RELAYER_KEY_RE.fullmatch(text) is not None


def sign_link(op, owner, wallet, key, nonce, deadline, valid_until=None, url=PAGE_URL, exchanges=None):
    """The signing page's link: every field in the fragment, which no request carries. An approval names its
    exchanges by letter - c, v or cv - and the page alone holds their addresses and the amount. Pure."""
    assert op in ("authorize", "revoke", "approve")
    f = [("v", "1"), ("op", op), ("o", owner), ("w", wallet)]
    if op == "approve":
        assert exchanges in ("c", "v", "cv"), exchanges
        f.append(("x", exchanges))
    else:
        f.append(("k", key))
    if op == "authorize":
        f.append(("u", str(int(valid_until))))
    f += [("n", str(int(nonce))), ("d", str(int(deadline)))]
    return url + "#" + "&".join("%s=%s" % (k, v) for k, v in f)


def wheel_name(filename):
    """A wheel file's distribution name, normalized as pip normalizes it, and its version. Pure."""
    m = re.fullmatch(r"([A-Za-z0-9_.]+?)-([0-9][^-]*)-.+\.whl", filename)
    assert m, filename
    return re.sub(r"[-_.]+", "-", m.group(1)).lower(), m.group(2)


def requirements_text(wheel_set=None):
    """The hash-pinned requirements of the client's 34 distributions: every wheel of the set but pip's. Pure."""
    rows = []
    for fn, _size, sha, _url in (wheel_set or WHEEL_SET):
        if fn == PIP_WHEEL:
            continue
        name, ver = wheel_name(fn)
        rows.append("%s==%s --hash=sha256:%s" % (name, ver, sha))
    return "\n".join(sorted(rows)) + "\n"


def pins(wheel_set=None):
    return dict(wheel_name(fn) for fn, _s, _h, _u in (wheel_set or WHEEL_SET) if fn != PIP_WHEEL)


def installed_reading(found, want):
    """G-ENV's second half: the distributions installed against the pins - none missing, none extra, none at another
    version. Pure."""
    missing = sorted(set(want) - set(found))
    extra = sorted(set(found) - set(want))
    wrong = sorted(k for k in set(want) & set(found) if found[k] != want[k])
    return not (missing or extra or wrong), missing, extra, wrong


def private_starts(updates):
    """The private chats that sent /start among Telegram updates, sorted. Pure."""
    chats = set()
    for u in updates:
        m = u.get("message") if isinstance(u, dict) else None
        if not isinstance(m, dict):
            continue
        chat = m.get("chat") or {}
        if (m.get("text") or "").startswith("/start") and chat.get("type") == "private" \
                and isinstance(chat.get("id"), int):
            chats.add(chat["id"])
    return sorted(chats)


def window_of(now):
    """The five-minute window open at `now`: (its open, the seconds left in it). Pure."""
    t0 = int(now) // RT_WINDOW_S * RT_WINDOW_S
    return t0, t0 + RT_WINDOW_S - now


def market_reading(doc, t0):
    """A five-minute market's gamma document read for the round trip: (ok, why, its Up and Down trading IDs, its
    condition, its exchange's letter). A CTF market - version v1 or none - trades its clobTokenIds on the CTF
    exchange, a Protocol V2 market its positionIds on the V2 exchange, each ID checked to be of its own kind by the
    client's reserved bits; a negative-risk market is refused. Its IDs are read from its outcomes, never by position;
    no price of it is read. Pure."""
    no = (False, None, {}, None, None)
    if isinstance(doc, list):
        doc = doc[0] if len(doc) == 1 else None
    if not isinstance(doc, dict):
        return (False, "no document") + no[2:]
    if doc.get("slug") != RT_FAMILY + str(t0):
        return (False, "another market's document") + no[2:]
    for k, v in (("active", True), ("closed", False), ("acceptingOrders", True), ("enableOrderBook", True)):
        if doc.get(k) is not v:
            return (False, "%s is %r" % (k, doc.get(k))) + no[2:]
    version = doc.get("version")
    if version not in (None, "v1", "v2"):
        return (False, "version is %r" % (version,)) + no[2:]
    if doc.get("negRisk") not in (None, False):
        return (False, "negRisk is %r" % (doc.get("negRisk"),)) + no[2:]
    try:
        mins = float(doc.get("orderMinSize"))
    except (TypeError, ValueError):
        mins = None
    if mins != float(RT_SIZE):
        return (False, "orderMinSize is %r" % (doc.get("orderMinSize"),)) + no[2:]
    field = "positionIds" if version == "v2" else "clobTokenIds"
    try:
        outcomes, ids = doc.get("outcomes"), doc.get(field)
        outcomes = json.loads(outcomes) if isinstance(outcomes, str) else outcomes
        ids = json.loads(ids) if isinstance(ids, str) else ids
    except ValueError:
        return (False, "outcomes or %s is not JSON" % field) + no[2:]
    if not (isinstance(outcomes, list) and isinstance(ids, list) and len(outcomes) == 2 and len(ids) == 2
            and sorted(outcomes) == sorted(RT_SIDES) and all(isinstance(t, str) and t.isdigit() and 0 < int(t) < 1 << 256
                                                             for t in ids)):
        return (False, "outcomes is not a two-element Up/Down array of %s" % field) + no[2:]
    if any((int(t) & V2_RESERVED == 0) != (version == "v2") for t in ids):
        return (False, "an ID of %s is not of its version's kind" % field) + no[2:]
    cid = doc.get("conditionId")
    if not (isinstance(cid, str) and re.fullmatch(r"0x[0-9a-fA-F]{64}", cid)):
        return (False, "no condition id") + no[2:]
    return True, "eligible, %s" % ("Protocol V2" if version == "v2" else "CTF"), \
        {outcomes[i]: ids[i] for i in range(2)}, cid, ("v" if version == "v2" else "c")


def rt_reading(rt):
    """G-RT, from the round trip's own record. Pure. PASS: one placement accepted live, at most RT_MAX_PLACEMENTS
    made, every earlier one refused as post-only crossing the book; the order read back live at this TZ's price,
    size, side and type with nothing matched; cancelled by its own request; read back cancelled with nothing matched;
    no open order of the key, of the wallet by the key, after it; the balance after equal to the balance before."""
    pl = rt.get("placements", [])
    live = [p for p in pl if p.get("result") == "live"]
    checks = {
        "a placement accepted live": len(live) == 1 and pl[-1].get("result") == "live",
        "placements at most %d" % RT_MAX_PLACEMENTS: 0 < len(pl) <= RT_MAX_PLACEMENTS,
        "every earlier placement refused as crossing the book": all(
            p.get("result") == "post_only_would_cross" for p in pl[:-1]),
        "read back LIVE at 0.01, 5, BUY, GTC, nothing matched": rt.get("read_live") == {
            "status": "LIVE", "price": RT_PRICE, "size": RT_SIZE, "side": "BUY", "type": "GTC", "matched": "0",
            "maker is the wallet": True, "asset is the token": True},
        "cancelled by its own request": rt.get("cancel") == {"canceled": True, "not_canceled": 0},
        "read back cancelled, nothing matched": (isinstance(rt.get("read_after"), dict)
                                                 and str(rt["read_after"].get("status", "")).startswith("CANCELED")
                                                 and rt["read_after"].get("matched") == "0"),
        "no open order of the key after it": rt.get("open_after") == 0,
        "no open order of the wallet by the key after it": rt.get("wallet_open_after") == 0,
        "the balance after equal to the balance before": (isinstance(rt.get("balance_before"), int)
                                                          and rt.get("balance_before") == rt.get("balance_after")),
    }
    return all(checks.values()), checks

# ---- the capture host's modes -------------------------------------------------------------------------------


def mode_fingerprint():
    assert is_capture_host(), "BLOCKED: fingerprint runs on the capture host"
    with open(os.path.join(PRIMARY, "SYSTEM-MAP.md"), "rb") as fh:
        raw = fh.read()
    txt = raw.decode("utf-8")
    rev = re.findall(r"^\*\*Revision string:\*\* `([^`]+)`$", txt, re.M)
    assert rev == [MAP_REVISION], "BLOCKED: map revision %r, required %s" % (rev, MAP_REVISION)
    found = dict(ANCHOR_ROW.findall(txt))
    assert found == ANCHORS, "BLOCKED: anchors %r" % found
    for k, rel in sorted(ANCHOR_FILES.items()):
        h = sha256_file(os.path.join(PRIMARY, rel))[0][:12]
        assert h == ANCHORS[k], "BLOCKED: re-derived %s %s, the map %s" % (k, h, ANCHORS[k])
        out("re-derived %s %s sha256[:12] %s equal" % (k, rel, h))
    rows = ROW.findall(txt)
    states = {k: sum(1 for r in rows if r[3] == k) for k in MAP_ROWS}
    assert states == MAP_ROWS and len(rows) == sum(MAP_ROWS.values()), "BLOCKED: rows %r" % states
    for path, lines, nbytes, state, sha in rows:
        with open(os.path.join(PRIMARY, path), "rb") as fh:
            blob = fh.read()
        got = (blob.count(b"\n"), len(blob), sha256_bytes(blob))
        if state == "frozen":
            want = (int(lines.replace(",", "")), int(nbytes.replace(",", "")), sha)
            assert got == want, "BLOCKED: frozen row %s: %r, the map %r" % (path, got, want)
        out("%-48s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    with open(os.path.join(PRIMARY, PAGE_REPO_PATH), "rb") as fh:
        page = fh.read()
    pg = (len(page), sha256_bytes(page))
    out("%s %d bytes sha256 %s, this TZ's %d and %s: %s" % (PAGE_REPO_PATH, pg[0], pg[1], PAGE_BYTES, PAGE_SHA256,
                                                            "equal" if pg == (PAGE_BYTES, PAGE_SHA256) else "DIFFER"))
    assert pg == (PAGE_BYTES, PAGE_SHA256), "BLOCKED: %s on main is not this TZ's Appendix B" % PAGE_REPO_PATH
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d; the signing page on main equal to Appendix B" % (
            MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"], states["reported"]))
    return 0


def mode_number():
    assert is_capture_host(), "BLOCKED: number runs on the capture host"
    names = git("ls-tree", "--name-only", "origin/main", "--", "CryptoTZ/", "CryptoReports/").split("\n")
    ok, tz, rp = number_reading(names, OWN_TZ)
    out("origin/main %s: %d paths under CryptoTZ/ and CryptoReports/; of the number %s: %s and %s" % (
        git("rev-parse", "origin/main"), len(names), NUMBER, tz, rp))
    out("NUMBER %s" % ("PASS - 2 of 2" if ok else "FAIL"))
    assert ok, "BLOCKED: of the number %s, CryptoTZ/ holds %s and CryptoReports/ %s" % (NUMBER, tz, rp)
    return 0


def mode_refs():
    assert is_capture_host(), "BLOCKED: refs runs on the capture host"
    text = git("ls-remote", "origin")
    kinds, branch = refs_reading(text)
    for ln in text.split("\n"):
        if ln.endswith("\tHEAD") or ln.endswith("\trefs/heads/main"):
            out("REF %s" % ln)
    for k in sorted(kinds):
        out("REFS %-40s %d" % (k, kinds[k]))
    out("REFS %d lines; refs/heads/%s %s" % (sum(kinds.values()), BRANCH, "PRESENT" if branch else "absent"))
    assert not branch, "BLOCKED: refs/heads/%s exists on origin already" % BRANCH
    return 0


def rb_streams(root=RB):
    """The reward book's stream files by their directory entries alone: (bytes, files, day directories)."""
    total = files = 0
    with os.scandir(root) as it:
        days = sorted(e.name for e in it if e.is_dir(follow_symlinks=False) and DAY_RE.fullmatch(e.name))
    for d in days:
        with os.scandir(os.path.join(root, d)) as it:
            for e in it:
                if e.is_file(follow_symlinks=False) and RB_STREAM_RE.fullmatch(e.name):
                    total += e.stat(follow_symlinks=False).st_size
                    files += 1
    return total, files, len(days)


def mode_room(sleep=time.sleep):
    """The room, read while the reward book's archive is not running (map section 3, the units)."""
    assert is_capture_host(), "BLOCKED: room runs on the capture host"
    for k in range(1, ARCHIVE_READS + 1):
        state = show(RB_ARCHIVE_SVC, ["ActiveState"]).get("ActiveState")
        out("%s read %d: %s" % (RB_ARCHIVE_SVC, k, state))
        if state == "inactive":
            break
        if k == ARCHIVE_READS:
            out("ROOM not read: the reward book's archive was running at %d reads" % ARCHIVE_READS)
            return 0
        sleep(ARCHIVE_WAIT_S)
    avail = floors(CAPTURE_DISK, CAPTURE_FLOOR)
    streams, files, days = rb_streams()
    room, margin = room_reading(avail, streams)
    out("ROOM: %d bytes available on %s; the reward book's stream files %d bytes in %d files under %d day "
        "directories; the room %d; its margin over STREAM_FLOOR %d and PEAK %d: %d bytes%s" % (
            avail, CAPTURE_DISK, streams, files, days, room, STREAM_FLOOR, PEAK, margin,
            "" if margin >= MARGIN_WATCH else " - BELOW %d (map section 7 item 175)" % MARGIN_WATCH))
    return 0


def mode_methods(label):
    """G-SSH K6: the methods the live host's sshd offers root, read from outside by one connection that offers no
    key and can answer no prompt. Of ssh's text, which carries the address, nothing is printed but the methods."""
    assert label in ("gate", "after"), "methods takes gate or after"
    assert is_capture_host(), "BLOCKED: methods runs on the capture host"
    try:
        rc, so, se = run(["ssh", "-T", "-v", "-o", "BatchMode=yes", "-o", "ConnectTimeout=20", "-o",
                          "PubkeyAuthentication=no", "-o", "PreferredAuthentications=password,keyboard-interactive",
                          "-o", "NumberOfPasswordPrompts=0", LIVE_ALIAS, "true"], timeout=60)
    except subprocess.TimeoutExpired:
        rc, so, se = None, "", ""
    found = methods_of(so + "\n" + se)
    ok = found == METHODS_ONLY
    out("METHODS %s: the methods the live host's sshd offers root, from outside: %s; ssh exit %s" % (
        label, found, "none, past 60 s" if rc is None else rc))
    out("G-SSH K6 %s alone, from outside: %s" % (",".join(METHODS_ONLY), "PASS" if ok else "FAIL"))
    return 0 if ok else 4


def proc_start_times():
    """The start instant of every running process whose argv[0] is `claude` or ends in `/claude.exe`."""
    with open("/proc/stat", encoding="utf-8") as fh:
        btime = int([ln for ln in fh.read().split("\n") if ln.startswith("btime ")][0].split()[1])
    hz = os.sysconf("SC_CLK_TCK")
    found = []
    for pid in sorted((p for p in os.listdir("/proc") if p.isdigit()), key=int):
        try:
            with open("/proc/%s/cmdline" % pid, "rb") as fh:
                argv = fh.read().split(b"\0")
            with open("/proc/%s/stat" % pid, encoding="utf-8") as fh:
                fields = fh.read().rsplit(")", 1)[1].split()
        except OSError:
            continue
        a0 = argv[0].decode("utf-8", "replace") if argv else ""
        if a0 == "claude" or a0.endswith("/claude.exe"):
            found.append((int(pid), btime + int(fields[19]) / hz, a0))
    return found


def birth(path):
    rc, so, se = run(["stat", "-c", "%W", path])
    assert rc == 0, se
    return int(so.strip())


def mode_scratch(own):
    """Lists the UUID directories beside `own`, this session's, and names each live or earlier."""
    assert is_capture_host(), "BLOCKED: scratch runs on the capture host"
    parent = os.path.dirname(own)
    procs = proc_start_times()
    for pid, t, a0 in procs:
        out("running %d started %s %s" % (pid, utc(t), a0))
    for name in sorted(os.listdir(parent)):
        path = os.path.join(parent, name)
        if path == own or not UUID.fullmatch(name) or not os.path.isdir(path):
            continue
        b = birth(path)
        owner = [pid for pid, t, _a in procs if t - 1 <= b <= t + LIVE_S]
        out("%s born %s: %s" % (name, utc(b), ("live, process %s" % owner) if owner else "earlier"))
    return 0


def pristine(tree):
    rc, so, _se = run(["git", "-C", tree, "status", "--porcelain", "--ignored"])
    assert rc == 0 and so == "", "reclaim: %s holds %r" % (tree, so[:400])
    head = git("rev-parse", "HEAD", tree=tree)
    up = git("rev-parse", "@{u}", tree=tree)
    assert up == head, "reclaim: %s is at %s, its upstream at %s" % (tree, head, up)
    out("reclaim: %s skipped: no file but its HEAD's, and HEAD %s is its upstream's" % (tree, head))


def tree_count(root):
    n = 0
    for _d, _s, files in os.walk(root):
        n += len(files)
    return n


def mode_reclaim(trees):
    """The work tree's every file but the worktree's and the wheels into the forensic store, each by exclusive
    create and its SHA-256 checked; an earlier session's directory checked reclaimable and not live."""
    assert is_capture_host(), "BLOCKED: reclaim runs on the capture host"
    assert trees and all(reclaimable(t) for t in trees), "reclaim: %r" % (trees,)
    procs = proc_start_times()
    for t in trees:
        if t != WORK:
            b = birth(t)
            owner = [p for p, s, _a in procs if s - 1 <= b <= s + LIVE_S]
            assert not owner, "reclaim: %s belongs to the running process %s" % (t, owner)
    before = tree_count(FORENSICS)
    considered = copied = held = 0
    for tree in trees:
        if tree != WORK:
            n = sum(len(f) for _d, _s, f in os.walk(tree))
            out("reclaim: %s, an earlier session's directory of %d files: nothing of it is kept" % (tree, n))
            continue
        if os.path.isdir(WT):
            pristine(WT)
        for dirpath, dirnames, filenames in os.walk(tree):
            dirnames[:] = sorted(d for d in dirnames if os.path.join(dirpath, d) not in (WT, TMP, WHEELS))
            for name in sorted(filenames):
                path = os.path.join(dirpath, name)
                if os.path.islink(path) or not os.path.isfile(path):
                    continue
                considered += 1
                rel = os.path.relpath(path, tree)
                h = sha256_file(path)[0]
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--" + rel.replace("/", "--"))
                if os.path.exists(dest):
                    assert sha256_file(dest)[0] == h, "reclaim: %s exists with another sha256" % dest
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                size, avail = os.path.getsize(path), fs_bytes(FORENSICS)[1]
                assert avail - size >= RECLAIM_FLOOR, "BLOCKED: reclaim: %d bytes available, %s is %d" % (
                    avail, path, size)
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest)[0] == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = tree_count(FORENSICS)
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d copied, %d already held; the forensic store %d -> %d files" % (
        considered, copied, held, before, after))
    return 0

# ---- the live host's modes, standard library ----------------------------------------------------------------


def mode_host(label):
    """The live host gate, TZ-49's five checks, and the facts L1 starts from: its locale (map section 7 item 185),
    its clock, root's keys by fingerprint and L1's paths by kind, mode, owner and size - never a file's content."""
    assert label in ("before", "after"), "host takes before or after"
    osrel = os_release(read_text("/etc/os-release", "") or "")
    ok, checks = live_gate(short_hostname(), osrel, sys.version_info,
                           [p for p in (CAPTURE_MARK, PRIMARY) if os.path.exists(p)], host_keys())
    for k, v in checks.items():
        out("%s: %s" % (k, "PASS" if v else "FAIL"))
    out("LIVE HOST GATE %s: %d of 5" % ("PASS" if ok else "FAIL", sum(checks.values())))
    if not ok:
        return 1
    floors(LIVE_DISK, LIVE_FLOOR)
    mem = meminfo(read_text("/proc/meminfo", ""))
    total, avail, _free = fs_bytes(LIVE_DISK)
    out("HOST %s: kernel %s; Python %s; %s; MemTotal %d MemAvailable %d SwapTotal %d SwapFree %d; / %d bytes, "
        "%d available" % (label, os.uname().release, sys.version.split()[0], osrel.get("PRETTY_NAME"),
                          mem.get("MemTotal", -1), mem.get("MemAvailable", -1), mem.get("SwapTotal", -1),
                          mem.get("SwapFree", -1), total, avail))
    for ln in (read_text("/etc/default/locale", "") or "").split("\n"):
        if ln.strip() and not ln.lstrip().startswith("#"):
            out("LOCALE /etc/default/locale: %s" % ln.strip())
    rc, so, _se = run(["locale"], env=dict(os.environ))
    out("LOCALE `locale` in this session, exit %d: %s" % (rc, "; ".join(x for x in so.split("\n") if x)))
    rc, so, _se = run(["timedatectl", "show", "-p", "NTP", "-p", "NTPSynchronized", "-p", "TimeUSec"])
    out("CLOCK exit %d: %s" % (rc, "; ".join(x for x in so.split("\n") if x)))
    keys = key_fingerprints(read_text(AUTHORIZED_KEYS, "") or "")
    out("SSHD authorized keys of root: %s; the Executor's among them: %s" % (keys, EXECUTOR_KEY in keys))
    for p in (L1_ETC,) + SECRETS + (L1_VAR, ACCOUNT_FILE) + tuple(rt_paths()) + (L1_ENV, WHEELS):
        out("PATH %s: %s" % (p, file_state(p)))
    return 0


def geo_read(base=("https", GEO_HOST, 443), sleep=time.sleep):
    """G-GEO: up to TRIES reads TRY_GAP_S apart while a reply is unread, over IPv4 alone; printed of each its status,
    its fields and whether the address the venue saw is the connection's own - a comparison, never the address."""
    for k in range(1, TRIES + 1):
        try:
            status, _h, blob, src = http_call(base, "GET", GEO_PATH)
            doc = json_of(blob)
            reading, f = geo_reading(status, doc), geo_fields(doc) or {}
            same = isinstance(doc, dict) and doc.get("ip") == src
            out("G-GEO read %d over IPv4: status %s, %d bytes, blocked %r, country %r, region %r, keys %s; the address "
                "the venue saw is the connection's own: %s -> %s" % (k, status, len(blob), f.get("blocked"),
                                                                     f.get("country"), f.get("region"), f.get("keys"),
                                                                     same, reading))
        except (OSError, http.client.HTTPException, ssl.SSLError) as exc:
            reading = "UNREAD"
            out("G-GEO read %d over IPv4: %s -> UNREAD" % (k, err_of(exc)))
        if reading != "UNREAD":
            return reading
        if k < TRIES:
            sleep(TRY_GAP_S)
    return "UNREAD"


def mode_geoblock():
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    r = geo_read()
    out("G-GEO %s" % r)
    return 0 if r == "PASS" else 1


def mode_sshd():
    """G-SSH K1 to K5 on the live host: TZ-49's drop-in, byte for byte, and sshd's configuration in force."""
    assert_live()
    st = None
    if os.path.isfile(SSHD_DROPIN) and not os.path.islink(SSHD_DROPIN):
        st = (sha256_file(SSHD_DROPIN)[0], os.stat(SSHD_DROPIN).st_mode & 0o7777)
    rc, so, se = run(["sshd", "-T"])
    assert rc == 0, "sshd -T: %s" % se.strip()[:300]
    ok, checks = ssh_reading(st, sshd_effective(so))
    for k, v in checks.items():
        out("%s: %s" % (k, "PASS" if v else "FAIL"))
    out("G-SSH K1 to K5 %s: %d of 5" % ("PASS" if ok else "FAIL", sum(checks.values())))
    return 0 if ok else 4


def page_read(base=("https", PAGES_HOST, 443), path=PAGE_PATH, want=None, sleep=time.sleep, tries=PAGE_TRIES):
    """G-PAGE: the signing page as GitHub Pages serves it, read up to `tries` times TRY_GAP_S apart until its bytes
    are Appendix B's - its length and SHA-256 - printed with its status and type."""
    want = want or (PAGE_BYTES, PAGE_SHA256)
    for k in range(1, tries + 1):
        try:
            status, h, blob, _src = http_call(base, "GET", path)
            got = (len(blob), sha256_bytes(blob))
            out("G-PAGE read %d: status %s, content-type %r, %d bytes, sha256 %s: %s" % (
                k, status, h.get("content-type"), got[0], got[1], "equal" if status == 200 and got == want else
                "not this TZ's page"))
            if status == 200 and got == want:
                return True
        except (OSError, http.client.HTTPException, ssl.SSLError) as exc:
            out("G-PAGE read %d: %s" % (k, err_of(exc)))
        if k < tries:
            sleep(TRY_GAP_S)
    return False


def mode_page():
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    ok = page_read()
    out("G-PAGE %s: %s" % ("PASS" if ok else "FAIL", PAGE_URL))
    return 0 if ok else 4


def fetch_wheels(base=("https", PYPI_HOST, 443), dest=WHEELS, wheel_set=None, sleep=time.sleep):
    """G-ENV's first half: every wheel of the set into `dest`, kept where its bytes are the set's, else fetched from
    PyPI over IPv4 and kept where its size and SHA-256 are - the first not served so ending it; then requirements."""
    wheel_set = wheel_set or WHEEL_SET
    if not os.path.isdir(dest):
        os.mkdir(dest, 0o755)
    good = 0
    for fn, size, sha, urlpath in wheel_set:
        path = os.path.join(dest, fn)
        if os.path.isfile(path) and sha256_file(path) == (sha, size):
            good += 1
            out("WHEEL kept       %-64s %9d %s" % (fn[:64], size, sha))
            continue
        blob = None
        for k in range(1, TRIES + 1):
            try:
                status, _h, b, _src = http_call(base, "GET", urlpath, timeout=60)
                if status == 200 and len(b) == size and sha256_bytes(b) == sha:
                    blob = b
                    break
                out("WHEEL %s read %d: status %s, %d bytes, sha256 %s: not the set's" % (
                    fn, k, status, len(b), sha256_bytes(b)))
            except (OSError, http.client.HTTPException, ssl.SSLError) as exc:
                out("WHEEL %s read %d: %s" % (fn, k, err_of(exc)))
            if k < TRIES:
                sleep(TRY_GAP_S)
        if blob is None:
            break                   # one wheel PyPI did not serve whole in three reads ends the fetch: G-ENV FAIL
        with open(path + ".part", "wb") as fh:
            fh.write(blob)
        os.rename(path + ".part", path)
        assert sha256_file(path) == (sha, size), path
        good += 1
        out("WHEEL downloaded %-64s %9d %s" % (fn[:64], size, sha))
    req = requirements_text(wheel_set).encode()
    with open(os.path.join(dest, "requirements.txt"), "wb") as fh:
        fh.write(req)
    out("WHEELS requirements.txt: %d lines, %d bytes, sha256 %s" % (req.count(b"\n"), len(req), sha256_bytes(req)))
    out("G-ENV wheels %s: %d of %d, %d bytes in all" % ("PASS" if good == len(wheel_set) else "FAIL", good,
                                                       len(wheel_set), sum(w[1] for w in wheel_set)))
    return good == len(wheel_set)


def mode_wheels():
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    return 0 if fetch_wheels() else 4


class Tty:
    """The Boss's terminal: what he is asked and shown goes there, and to no log."""

    def __init__(self, path="/dev/tty"):
        self.fh = open(path, "r+", encoding="utf-8", errors="replace")

    def say(self, text):
        self.fh.write(text + "\n")
        self.fh.flush()

    def ask(self, prompt, hidden=False):
        if hidden:
            return getpass.getpass(prompt, stream=self.fh)
        self.fh.write(prompt)
        self.fh.flush()
        line = self.fh.readline()
        if line == "":
            raise EOFError("the terminal closed")
        return line.rstrip("\r\n")


def ask_until(tty, prompt, ok, hidden=False, tries=3, refusal="Не подходит — попробуйте ещё раз."):
    """An answer the predicate accepts, asked at most `tries` times; None where none was."""
    for _k in range(tries):
        a = tty.ask(prompt, hidden=hidden).strip()
        if ok(a):
            return a
        tty.say(refusal)
    return None


def mode_secrets(tty=None, token_file=TG_TOKEN_FILE, relayer_file=RELAYER_FILE, account_file=ACCOUNT_FILE):
    """The Boss's credentials onto the live host, typed by him at his terminal: the bot's Telegram token and the
    owner's Relayer API key hidden, the key's signer address - the owner - shown. Each written once, by exclusive
    create, 0600, root's; one that is already in place is kept. Printed: written or kept, and the bytes - never a
    value."""
    if tty is None:
        assert_live()
        floors(LIVE_DISK, LIVE_FLOOR)
        tty = Tty()
    tty.say("L1 · ТЗ-50: учётные данные бота. Ввод токенов скрыт; ничего из введённого не попадает в журнал.")
    done = {}
    t = read_text(token_file) if os.path.exists(token_file) else None
    if t is not None and token_ok(t.strip()) and private_file_ok(token_file):
        done["telegram-token"] = "kept"
    else:
        assert t is None, "BLOCKED: %s holds something that is not a bot token: %s" % (token_file, file_state(token_file))
        v = ask_until(tty, "Токен Telegram-бота L1 от BotFather (ввод скрыт): ", token_ok, hidden=True,
                      refusal="Это не токен бота (вида 123456789:AA…). Ещё раз.")
        if v is None:
            out("SECRETS telegram-token: no token in 3 tries")
            return 4
        done["telegram-token"] = "written, %d bytes" % write_private(token_file, (v + "\n").encode())
    r = read_text(relayer_file) if os.path.exists(relayer_file) else None
    if r is not None:
        doc = json_of(r.encode())
        assert isinstance(doc, dict) and relayer_key_ok(doc.get("key")) and valid_address(doc.get("address")) \
            and private_file_ok(relayer_file), "BLOCKED: %s is not a relayer key: %s" % (relayer_file,
                                                                                       file_state(relayer_file))
        owner = valid_address(doc["address"])
        done["relayer-key"] = "kept"
    else:
        key = ask_until(tty, "Relayer API key — polymarket.com → Settings → API Keys (ввод скрыт): ", relayer_key_ok,
                        hidden=True, refusal="Это не похоже на ключ. Ещё раз.")
        owner = ask_until(tty, "Signer Address того же ключа (0x…, это адрес владельца — аккаунта MetaMask бота): ",
                          valid_address, refusal="Нужен адрес вида 0x и 40 шестнадцатеричных знаков. Ещё раз.")
        if key is None or owner is None:
            out("SECRETS relayer-key: no key or no address in 3 tries")
            return 4
        owner = valid_address(owner)
        body = (json.dumps({"key": key, "address": owner}, sort_keys=True) + "\n").encode()
        done["relayer-key"] = "written, %d bytes" % write_private(relayer_file, body)
    acct = json_of((read_text(account_file) or "").encode()) if os.path.exists(account_file) else None
    if acct is None:
        done["account"] = "written, %d bytes" % write_json_atomic(account_file, {"owner": owner})
    else:
        assert isinstance(acct, dict) and acct.get("owner") == owner, \
            "BLOCKED: %s names another owner than the relayer key's" % account_file
        done["account"] = "kept"
    for k in ("telegram-token", "relayer-key", "account"):
        out("SECRETS %s: %s" % (k, done[k]))
    for p in (token_file, relayer_file, account_file):
        out("PATH %s: %s" % (p, file_state(p)))
    tty.say("Готово: токен бота и ключ Relayer записаны на сервер.")
    return 0


def mode_bosskey(tty=None, path=AUTHORIZED_KEYS):
    """The Boss's own SSH public key appended to root's authorized_keys - one line, a public key of a known type -
    or none where he gives none. Printed: its type and fingerprint, and root's keys by fingerprint."""
    if tty is None:
        assert_live()
        tty = Tty()
    before = key_fingerprints(read_text(path, "") or "")
    got = None
    for _k in range(3):
        line = tty.ask("Публичный ключ из Termius (одна строка ssh-ed25519 …) — или просто Enter, чтобы пропустить: ")
        if not line.strip():
            out("BOSSKEY skipped: no key given; root's keys by fingerprint: %s" % before)
            tty.say("Пропущено: вход на этот сервер остаётся через «ssh live-host» с сервера в Варшаве.")
            return 0
        try:
            got = pubkey_line(line)
            break
        except ValueError as exc:
            tty.say("Это не публичный ключ (%s). В Termius: Keychain → ключ → Copy public key." % exc)
            out("BOSSKEY refused a line: %s" % exc)
    if got is None:
        return 4
    full, kind, fp, bits = got
    if (kind, fp) in before:
        out("BOSSKEY present already: %s %s; root's keys by fingerprint: %s" % (kind, fp, before))
        tty.say("Этот ключ уже стоит на сервере: %s" % fp)
        return 0
    text = read_text(path, "") or ""
    with open(path, "a", encoding="utf-8") as fh:
        if text and not text.endswith("\n"):
            fh.write("\n")
        fh.write(full + "\n")
    after = key_fingerprints(read_text(path, "") or "")
    assert (kind, fp) in after and len(after) == len(before) + 1, "BOSSKEY: %r" % (after,)
    out("BOSSKEY added: %s %s%s; root's keys by fingerprint: %s" % (kind, fp, "" if bits is None else ", %d bits" % bits,
                                                                    after))
    tty.say("Ключ добавлен: %s. Вход в Termius напрямую теперь работает этим ключом." % fp)
    return 0

# ---- Telegram: the Bot API through one request function -------------------------------------------------------


class Telegram:
    """Every call a JSON POST with this TZ's agent; the token is in the path and in no printed line."""

    def __init__(self, token, base=("https", TG_HOST, 443)):
        self.token, self.base = token, base

    def call(self, method, http_timeout=30, **params):
        status, _h, blob, _src = http_call(self.base, "POST", "/bot%s/%s" % (self.token, method), body=params,
                                           timeout=http_timeout)
        doc = json_of(blob)
        if not (isinstance(doc, dict) and doc.get("ok") is True):
            code = doc.get("error_code") if isinstance(doc, dict) else status
            desc = doc.get("description") if isinstance(doc, dict) else None
            raise RuntimeError("telegram %s: %s %s" % (method, code, desc))
        return doc["result"]


def read_token(path=TG_TOKEN_FILE):
    assert private_file_ok(path), "BLOCKED: %s: %s" % (path, file_state(path))
    t = (read_text(path) or "").strip()
    assert token_ok(t), "BLOCKED: %s holds no bot token" % path
    return t


def mode_tg_probe(tg=None):
    """G-TG's first check: getMe answers is_bot and a username, getMyCommands a list; the name is not printed."""
    if tg is None:
        assert_live()
        tg = Telegram(read_token())
    me = tg.call("getMe")
    cmds = tg.call("getMyCommands")
    ok = isinstance(me, dict) and me.get("is_bot") is True and bool(me.get("username")) and isinstance(cmds, list)
    out("G-TG getMe: a bot with a username - its name withheld, as a public report would publish it - %d commands in "
        "its menu: %s" % (len(cmds) if isinstance(cmds, list) else -1, "PASS" if ok else "FAIL"))
    return 0 if ok else 4


def mode_find_chat(tg=None, chat_file=CHAT_FILE, wait_s=TG_WAIT_S):
    """G-TG's second check: the one private chat that sent /start to the bot, pinned to chat_file, 0600, by exclusive
    create; a chat already pinned is kept. Waits up to wait_s for a /start. Prints counts only, never a chat id."""
    if tg is None:
        assert_live()
        tg = Telegram(read_token())
    if os.path.exists(chat_file):
        c = (read_text(chat_file) or "").strip()
        assert re.fullmatch(r"-?[0-9]+", c) and private_file_ok(chat_file), "BLOCKED: %s: %s" % (
            chat_file, file_state(chat_file))
        out("G-TG chat: pinned already, kept")
        return 0
    deadline, said, offset = time.time() + wait_s, False, {}
    while True:
        ups = tg.call("getUpdates", http_timeout=80, timeout=min(50, max(1, int(deadline - time.time()))),
                      allowed_updates=["message"], **offset)
        private = private_starts(ups)
        if len(private) == 1:
            break
        if len(private) > 1 or time.time() >= deadline:
            out("G-TG chat: updates %d, private chats that sent /start: %d - FAIL" % (len(ups), len(private)))
            return 1
        if ups:
            offset = {"offset": ups[-1]["update_id"] + 1}
        if not said:
            out("G-TG chat: no /start among %d pending updates; waiting up to %d s for the Boss's /start" % (
                len(ups), wait_s))
            said = True
    write_private(chat_file, ("%d\n" % private[0]).encode())
    out("G-TG chat: updates %d, private chats that sent /start: 1, pinned to %s" % (len(ups), chat_file))
    return 0


def report_text(rt, acct):
    """The round trip's report to the Boss's chat, in Russian, from its record: no address, id or hash. Pure."""
    ok, _checks = rt_reading(rt)
    live = [p for p in rt.get("placements", []) if p.get("result") == "live"]
    until = acct.get("valid_until")
    lines = ["L1 · ТЗ-50 · счёт бота и первый ордер",
             "• Сессионный ключ разрешён владельцем: только ордера CLOB, вывод средств ему недоступен%s." % (
                 ", до %s UTC" % utc(until)[:10] if isinstance(until, int) else ""),
             "• Ордер: покупка %s %s по %s (post-only) на %s — %s." % (
                 RT_SIZE, live[0]["side"] if live else "—", RT_PRICE, rt.get("market", "—"),
                 "выставлен за %s мс, отменён за %s мс" % (live[0].get("ms"), rt.get("cancel_ms")) if live
                 else "не выставлен"),
             "• Баланс: %s pUSD до и %s pUSD после; открытых ордеров нет: %s." % (
                 units(rt.get("balance_before")), units(rt.get("balance_after")),
                 "да" if rt.get("open_after") == 0 and rt.get("wallet_open_after") == 0 else "нет"),
             "• Итог: %s." % ("ордер туда и обратно прошёл" if ok else "проверка не пройдена — смотрите отчёт ТЗ-50"),
             "Кнопка «Стоп» и отчёты работающего бота появятся вместе с ним — в следующем ТЗ."]
    return "\n".join(lines)


def units(v):
    """Six-decimal collateral units as pUSD. Pure."""
    return "%d.%06d" % divmod(v, 1000000) if isinstance(v, int) and v >= 0 else "—"


def rt_paths(root=L1_VAR):
    """The round trip's records under `root`, in run order."""
    if not os.path.isdir(root):
        return []
    found = sorted((int(m.group(1)), n) for n in os.listdir(root) for m in [RT_RECORD.fullmatch(n)] if m)
    return [os.path.join(root, n) for _i, n in found]


def mode_tg_report(tg=None, root=L1_VAR, account_file=ACCOUNT_FILE, chat_file=CHAT_FILE):
    """G-TG's third check: the last round trip's report sent to the pinned chat; the text printed, its message id."""
    if tg is None:
        assert_live()
        tg = Telegram(read_token())
    paths = rt_paths(root)
    assert paths, "BLOCKED: no round trip recorded under %s" % root
    rt = json_of((read_text(paths[-1]) or "").encode())
    acct = json_of((read_text(account_file) or "").encode())
    assert isinstance(rt, dict) and isinstance(acct, dict), "BLOCKED: no round trip or no account record"
    assert private_file_ok(chat_file), "BLOCKED: %s: %s" % (chat_file, file_state(chat_file))
    chat = int((read_text(chat_file) or "").strip())
    text = report_text(rt, acct)
    msg = tg.call("sendMessage", chat_id=chat, text=text, disable_web_page_preview=True)
    ok = isinstance(msg, dict) and isinstance(msg.get("message_id"), int)
    for ln in text.split("\n"):
        out("G-TG report | %s" % ln)
    out("G-TG report sent: %s" % ("PASS, message %d" % msg["message_id"] if ok else "FAIL"))
    return 0 if ok else 4

# ---- the venue's client: /root/l1-env, polymarket-client 0.20.0 ----------------------------------------------


def client():
    """The venue's client, made ready in this process: every lookup through gai4, every request with this TZ's
    agent; its pinned version and the terms this file relies on asserted. Returns the names the modes use."""
    import dataclasses
    import importlib.metadata as md
    socket.getaddrinfo = gai4
    import httpx
    import httpx._client
    httpx._client.USER_AGENT = UA
    from eth_account import Account
    from eth_account.messages import encode_typed_data
    from eth_utils import to_checksum_address
    from polymarket import AsyncSecureClient, RelayerApiKey
    from polymarket.clients._transport import AsyncTransport
    from polymarket.environments import PRODUCTION, _create_environment
    from polymarket.errors import RequestRejectedError
    from polymarket.models.clob.relayer import RelayerTransactionType
    from polymarket.transactions import GaslessTransactionHandle
    from polymarket._internal import protocol as P
    from polymarket._internal import wallet as W
    from polymarket._internal.actions import account as A
    from polymarket._internal.actions import session_keys as S
    from polymarket._internal.actions.orders.context import resolve_order_exchange_address
    from polymarket._internal.actions.relayer import calls as C
    from polymarket._internal.actions.relayer import gasless as G
    from polymarket._internal.actions.relayer.auth import make_relayer_header_resolver
    from polymarket._internal.actions.relayer.deployed import fetch_deployed
    from polymarket._internal.actions.relayer.nonce import fetch_execute_params
    from polymarket._internal.actions.relayer.submit import submit_gasless
    from polymarket._internal.actions.relayer.signing.deposit_wallet import build_deposit_wallet_typed_data
    assert md.version(SDK_DIST) == SDK_VERSION, "the client is %s, not %s" % (md.version(SDK_DIST), SDK_VERSION)
    assert S._SESSION_KEY_LIFETIME_SECONDS == LIFETIME_S and G._DEPOSIT_WALLET_DEADLINE_S == DEADLINE_S
    assert C._DEPOSIT_WALLET_AUTHORIZE_SESSION_SIGNER_SELECTOR.hex() == SELECTORS["authorize"]
    assert C._DEPOSIT_WALLET_REVOKE_SESSION_SIGNER_SELECTOR.hex() == SELECTORS["revoke"]
    assert (C._ERC20_APPROVE_SELECTOR.hex(), C._ERC20_ALLOWANCE_SELECTOR.hex()) == (APPROVE_SEL, ALLOWANCE_OF)
    assert P._V2_RESERVED_BITS_MASK == V2_RESERVED, "the client's V2 position IDs"
    cfg = PRODUCTION._config
    assert (cfg.collateral_token, cfg.standard_exchange, cfg.exchange_v3) == (PUSD,) + tuple(a for _x, a in EXCHANGES), \
        "the client's collateral and exchanges"
    assert (cfg.chain_id, cfg.clob_url, cfg.relayer_url, cfg.gamma_url, cfg.rpc_url) == (
        CHAIN_ID, "https://" + CLOB_HOST, "https://" + RELAYER_HOST, "https://" + GAMMA_HOST, "https://" + RPC_HOST), \
        "the client's hosts"
    return types.SimpleNamespace(**{k: v for k, v in locals().items() if k != "md"})


def test_env(k, base_url):
    """An environment of the client whose CLOB, relayer and gamma are the self-test's loopback stand-in."""
    cfg = k.dataclasses.replace(k.PRODUCTION._config, clob_url=base_url + "/clob", relayer_url=base_url + "/relayer",
                                gamma_url=base_url + "/gamma", rpc_url=base_url + "/rpc", relayer_poll_frequency_ms=50,
                                relayer_max_polls=40)
    return k._create_environment(name="tz50-selftest", config=cfg)


def load_session_key(path=SESSION_KEY_FILE):
    assert private_file_ok(path), "BLOCKED: %s: %s" % (path, file_state(path))
    v = (read_text(path) or "").strip()
    assert re.fullmatch(r"0x[0-9a-f]{64}", v), "BLOCKED: %s holds no key" % path
    return v


def load_relayer(path=RELAYER_FILE):
    assert private_file_ok(path), "BLOCKED: %s: %s" % (path, file_state(path))
    doc = json_of((read_text(path) or "").encode())
    assert isinstance(doc, dict) and relayer_key_ok(doc.get("key")) and valid_address(doc.get("address")), \
        "BLOCKED: %s holds no relayer key" % path
    return doc["key"], valid_address(doc["address"])


def load_account(path=ACCOUNT_FILE):
    doc = json_of((read_text(path) or "").encode())
    assert isinstance(doc, dict) and valid_address(doc.get("owner")), "BLOCKED: %s holds no account" % path
    return doc


async def first_items(paginator):
    page = await paginator.first_page()
    return list(page.items)


async def resolve_wallet(k, owner, rt, cfg):
    """The owner's Deposit Wallet, as the client resolves a default one: the legacy derivation where the relayer
    reads it deployed, else the beacon derivation, which must read deployed."""
    uups = k.W.derive_uups_deposit_wallet_address(owner, cfg.wallet_derivation)
    if await k.fetch_deployed(rt, address=uups, type=k.RelayerTransactionType.WALLET):
        return uups, "legacy"
    beacon = k.W.derive_beacon_deposit_wallet_address(owner, cfg.wallet_derivation)
    assert await k.fetch_deployed(rt, address=beacon, type=k.RelayerTransactionType.WALLET), \
        "BLOCKED: the owner's Deposit Wallet is not deployed"
    return beacon, "beacon"


async def registered(k, env, key_hex, wallet, session, want, tries=READY_TRIES, gap=READY_GAP_S, sleep=None):
    """Whether the session key acts for the wallet - its client made and the wallet's orders listed by it - read
    up to `tries` times `gap` apart until the reading is `want`. Returns the last reading."""
    sleep = sleep or asyncio.sleep
    state = None
    for i in range(1, tries + 1):
        try:
            c = await k.AsyncSecureClient.create(private_key=key_hex, wallet=wallet, environment=env)
            try:
                assert c.wallet_type == "DEPOSIT_WALLET" and c._ctx.signer_type == "SESSION_KEY", "not a session key"
                items = await first_items(c.list_wallet_open_orders(signer_addresses=[session]))
                state = True
                out("KEY read %d: the session key lists the wallet's orders - %d on the first page" % (i, len(items)))
            finally:
                await c.close()
        except k.RequestRejectedError as exc:
            state = False
            out("KEY read %d: refused, status %s" % (i, exc.status))
        if state is want:
            return state
        if i < tries:
            await sleep(gap)
    return state


async def authorize_kept(k, env, key_hex, acct):
    """Whether an earlier run's authorization of this key stands - the account records it for this key, unrevoked,
    and the key acts for the wallet at one read - so that a second run of the Boss's paste asks for no signature."""
    session = k.Account.from_key(key_hex).address
    if not (acct.get("authorized_at") and acct.get("session_key") == session.lower() and acct.get("wallet")
            and not acct.get("revoked_at")):
        return False
    return (await registered(k, env, key_hex, acct["wallet"], session, want=True, tries=1)) is True


def ask_signature(k, op, tty, td, owner_cs, deadline, link, now):
    """One link's answers at the terminal: the owner's signature of the typed data `td`, recovered to the owner by
    the client's own encoding; None where none came in SIGNATURE_TRIES answers, an empty answer asks for a new
    link, or it came within ten seconds of the link's deadline."""
    for t in range(1, SIGNATURE_TRIES + 1):
        ans = tty.ask("Подпись из MetaMask (0x…), или просто Enter — новая ссылка: ").strip()
        if not ans:
            break
        if not re.fullmatch(r"0x[0-9a-fA-F]{130}", ans):
            tty.say("Это не подпись: нужно 0x и 130 шестнадцатеричных знаков.")
            out("OWNER %s link %d answer %d: not a signature" % (op, link, t))
            continue
        try:
            rec = k.Account.recover_message(k.encode_typed_data(full_message=td), signature=ans)
        except Exception:   # an unrecoverable signature is the same answer as another signer's
            rec = None
        if rec != owner_cs:
            tty.say("Подпись не владельца для этой ссылки: подпишите ссылку выше аккаунтом владельца.")
            out("OWNER %s link %d answer %d: a signature, not the owner's for this batch" % (op, link, t))
            continue
        if int(now()) > int(deadline) - 10:
            tty.say("Срок этой ссылки истёк — вот новая.")
            out("OWNER %s link %d: the owner's signature, past its deadline" % (op, link))
            return None
        out("OWNER %s link %d: the owner's signature, recovered to the owner under the client's own typed data" % (
            op, link))
        return ans
    out("OWNER %s link %d: no owner's signature" % (op, link))
    return None


async def owner_flow(k, op, env, tty, key_hex, relayer_key, owner, page_url=PAGE_URL, now=time.time):
    """authorize or revoke: the owner's signature of one Deposit Wallet batch, made in MetaMask on the Boss's device
    from the signing page's link, checked to recover to the owner, submitted to the relayer with his Relayer API key
    and its transaction confirmed. Every part but the signature is the client's own code. Returns (wallet, session,
    valid_until) or None where no signature came."""
    cfg = env._config
    owner_cs = k.to_checksum_address(owner)
    rt = k.AsyncTransport(base_url=cfg.relayer_url, header_resolver=k.make_relayer_header_resolver(
        k.RelayerApiKey(key=relayer_key, address=owner_cs)))
    try:
        wallet, how = await resolve_wallet(k, owner_cs, rt, cfg)
        session = k.Account.from_key(key_hex).address
        out("OWNER %s: the owner's Deposit Wallet derived (%s) and deployed; the addresses withheld" % (op, how))
        for link in range(1, LINKS + 1):
            if op == "authorize":
                req = k.S._parse_authorize_session_key_request(address=session, scopes=list(SCOPES), idempotency_key=None)
                call = k.C.authorize_session_signer_call(wallet_address=wallet, session_signer=req.address,
                                                         valid_until=req.valid_until_epoch)
                until = req.valid_until_epoch
            else:
                req = k.S._parse_revoke_session_key_request(address=session, idempotency_key=None)
                call = k.C.revoke_session_signer_call(wallet_address=wallet, session_signer=req.address)
                until = None
            nonce = (await k.fetch_execute_params(rt, address=owner_cs, type=k.RelayerTransactionType.WALLET)).nonce
            deadline = str(int(now()) + DEADLINE_S)
            td = k.build_deposit_wallet_typed_data(wallet=wallet, calls=[call], nonce=nonce, deadline=deadline,
                                                   chain_id=cfg.chain_id)
            url = sign_link(op, owner_cs, wallet, session, nonce, deadline, until, url=page_url)
            tty.say("")
            tty.say("%s сессионного ключа бота. Владелец: %s" % ("Разрешение" if op == "authorize" else "Отзыв", owner_cs))
            tty.say("Кошелёк бота (Deposit Wallet): %s" % wallet)
            tty.say("Сессионный ключ: %s%s" % (session, ", только ордера CLOB, до %s UTC" % utc(until) if until else ""))
            tty.say("Откройте эту ссылку во встроенном браузере MetaMask (аккаунт бота), проверьте ключ и подпишите;"
                    " ссылка действует до %s UTC:" % utc(int(deadline))[11:19])
            tty.say(url)
            sig = ask_signature(k, op, tty, td, owner_cs, deadline, link, now)
            if sig is None:
                continue
            batch = k.G.SignedDepositWalletBatch(nonce=nonce, deadline=deadline, signature=sig)
            ctx = types.SimpleNamespace(wallet=wallet, relayer=rt, environment_config=cfg)
            if op == "authorize":
                payload = k.S._build_authorization_payload(ctx, request=req, batch=batch)
                path, parse = k.S._AUTHORIZATIONS_PATH, k.S._AuthorizeSessionKeyResponse.parse_response
            else:
                payload = k.S._build_revocation_payload(ctx, request=req, batch=batch)
                path, parse = k.S._REVOCATIONS_PATH, k.S._RevokeSessionKeyResponse.parse_response
            resp = await k.S._post_session_key_operation(ctx, path=path, payload=payload,
                                                          idempotency_key=req.idempotency_key, parse=parse)
            (k.S._assert_authorization_accepted if op == "authorize" else k.S._assert_revocation_accepted)(resp.status)
            out("OWNER %s: the relayer accepted the request, status %s" % (op, resp.status))
            await k.GaslessTransactionHandle(transaction_id=resp.transaction_id,
                                             transaction_hash=getattr(resp, "transaction_hash", None), _relayer=rt,
                                             _max_polls=cfg.relayer_max_polls,
                                             _poll_delay_s=cfg.relayer_poll_frequency_ms / 1000).wait()
            out("OWNER %s: the relayer's transaction confirmed" % op)
            return wallet, session, until
        return None
    finally:
        await rt.close()


async def approve_flow(k, env, tty, relayer_key, owner, page_url=PAGE_URL, now=time.time, sleep=None):
    """approve: where the wallet's pUSD allowance on chain to either exchange is under one order's cost, the owner's
    signature of one Deposit Wallet batch of approve(exchange, APPROVE_UNITS) on pUSD for each such exchange - never
    the maximum - made in MetaMask from the signing page's link, recovered to the owner, submitted to the relayer
    with his Relayer API key and confirmed, and the allowances read on chain again. Every part but the signature is
    the client's own code. Returns (wallet, before, after): after is before where nothing was short, None where no
    signature came."""
    sleep = sleep or asyncio.sleep
    cfg = env._config
    owner_cs = k.to_checksum_address(owner)
    rt = k.AsyncTransport(base_url=cfg.relayer_url, header_resolver=k.make_relayer_header_resolver(
        k.RelayerApiKey(key=relayer_key, address=owner_cs)))
    try:
        wallet, how = await resolve_wallet(k, owner_cs, rt, cfg)
        before = await chain_allowances(k, env, wallet)
        out("OWNER approve: the owner's Deposit Wallet derived (%s) and deployed; its pUSD allowances on chain %s" % (
            how, shown(before)))
        short = [(x, a) for x, a in EXCHANGES if not enough(before[x])]
        if not short:
            out("OWNER approve: every allowance at least one order's cost - kept, nothing to sign")
            return wallet, before, before
        calls = [k.C.erc20_approval_call(token_address=PUSD, spender=a, amount=APPROVE_UNITS) for _x, a in short]
        letters = "".join(x for x, _a in short)
        for link in range(1, LINKS + 1):
            nonce = (await k.fetch_execute_params(rt, address=owner_cs, type=k.RelayerTransactionType.WALLET)).nonce
            deadline = str(int(now()) + DEADLINE_S)
            td = k.build_deposit_wallet_typed_data(wallet=wallet, calls=calls, nonce=nonce, deadline=deadline,
                                                   chain_id=cfg.chain_id)
            url = sign_link("approve", owner_cs, wallet, None, nonce, deadline, url=page_url, exchanges=letters)
            tty.say("")
            tty.say("Разрешение %s Polymarket списывать pUSD кошелька бота для исполнения его ордеров — %s %s pUSD. "
                    "Владелец: %s" % ("двум биржам" if len(short) == 2 else "бирже", "каждой не больше" if len(short) == 2
                                      else "не больше", units(APPROVE_UNITS).rstrip("0").rstrip("."), owner_cs))
            tty.say("Кошелёк бота (Deposit Wallet): %s" % wallet)
            for x, a in short:
                tty.say("Биржа для рынков %s: %s" % ("протокола V2" if x == "v" else "CTF", a))
            tty.say("Откройте эту ссылку во встроенном браузере MetaMask (аккаунт бота), проверьте биржи и подпишите;"
                    " ссылка действует до %s UTC:" % utc(int(deadline))[11:19])
            tty.say(url)
            sig = ask_signature(k, "approve", tty, td, owner_cs, deadline, link, now)
            if sig is None:
                continue
            payload = k.G.build_deposit_wallet_payload(
                signer_address=owner_cs, deposit_wallet_factory=cfg.wallet_derivation.deposit_wallet_factory,
                wallet=wallet, calls=calls, nonce=nonce, deadline=deadline, signature=sig, metadata=APPROVE_METADATA)
            try:
                resp = await k.submit_gasless(rt, payload=payload)
            except k.RequestRejectedError as exc:
                tty.say("Релейер не принял эту подпись — вот новая ссылка.")
                out("OWNER approve link %d: the relayer refused the batch, status %s" % (link, exc.status))
                continue
            out("OWNER approve: the relayer accepted the batch of %d, state %s" % (len(calls), resp.state))
            await k.GaslessTransactionHandle(transaction_id=resp.transaction_id, transaction_hash=resp.transaction_hash,
                                             _relayer=rt, _max_polls=cfg.relayer_max_polls,
                                             _poll_delay_s=cfg.relayer_poll_frequency_ms / 1000).wait()
            out("OWNER approve: the relayer's transaction confirmed")
            after = None
            for i in range(1, READY_TRIES + 1):
                after = await chain_allowances(k, env, wallet)
                out("OWNER approve read %d: allowances on chain %s" % (i, shown(after)))
                if all(enough(v) for v in after.values()):
                    break
                if i < READY_TRIES:
                    await sleep(READY_GAP_S)
            return wallet, before, after
        return wallet, before, None
    finally:
        await rt.close()


def mode_env():
    """G-ENV's second half, in /root/l1-env: the distributions installed are the pins, none missing, extra or at
    another version; the interpreter is this venv's; the client's terms are this file's."""
    import importlib.metadata as md
    ok_prefix = os.path.realpath(sys.prefix) == L1_ENV
    found = {}
    for d in md.distributions():
        found[re.sub(r"[-_.]+", "-", d.metadata["Name"]).lower()] = d.version
    ok, missing, extra, wrong = installed_reading(found, pins())
    k = client()
    out("ENV interpreter %s, prefix %s: %s" % (sys.version.split()[0], sys.prefix, "PASS" if ok_prefix else "FAIL"))
    out("ENV distributions: %d installed, %d pinned; missing %s, extra %s, another version %s" % (
        len(found), len(pins()), missing, extra, wrong))
    out("ENV the client %s %s; session keys %d s, a batch %d s; selectors %s; hosts %s, %s, %s" % (
        SDK_DIST, SDK_VERSION, LIFETIME_S, DEADLINE_S, SELECTORS, k.cfg.clob_url, k.cfg.relayer_url, k.cfg.gamma_url))
    good = ok and ok_prefix
    out("G-ENV installed %s" % ("PASS" if good else "FAIL"))
    return 0 if good else 4


def mode_key(path=SESSION_KEY_FILE):
    """G-KEY: the session key made once on this host - a fresh secp256k1 key from os.urandom by eth_account - into
    its own file by exclusive create, 0600, root's; read back and its address re-derived. Never printed, hashed or
    copied; a key already in place is kept."""
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    k = client()
    if os.path.exists(path):
        load_session_key(path)
        out("G-KEY %s: present, kept; %s" % (path, file_state(path)))
        return 0
    acct = k.Account.create()
    write_private(path, ("0x%s\n" % acct.key.hex().removeprefix("0x")).encode())
    back = load_session_key(path)
    assert k.Account.from_key(back).address == acct.address, "the key read back is not the key made"
    del acct, back
    out("G-KEY %s: made; %s; read back and its address re-derived equal; address withheld" % (path, file_state(path)))
    return 0


def mode_owner(op):
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    k = client()
    tty = Tty()
    acct = load_account()
    relayer_key, owner = load_relayer()
    assert acct["owner"] == owner, "BLOCKED: the account's owner is not the relayer key's"
    if op == "approve":
        wallet, before, after = asyncio.run(approve_flow(k, k.PRODUCTION, tty, relayer_key, owner))
        assert acct.get("wallet") in (None, wallet.lower()), "BLOCKED: the account's wallet is another"
        good = after is not None and all(enough(v) for v in after.values())
        acct.update({"wallet": wallet.lower(), "allowances": shown(after if after is not None else before)})
        if good and after is not before:
            acct["approved_at"] = int(time.time())
        write_json_atomic(ACCOUNT_FILE, acct)
        out("G-APPROVE %s: allowances on chain %s, each at least one order's cost: %s" % (
            "PASS" if good else "FAIL", acct["allowances"], good))
        tty.say("Готово: биржи могут исполнять ордера бота." if good else
                "Не получилось — исполнитель увидит причину в журнале.")
        return 0 if good else 4
    key_hex = load_session_key()
    if op == "authorize" and asyncio.run(authorize_kept(k, k.PRODUCTION, key_hex, acct)):
        out("G-AUTH authorize PASS: kept - the key authorized at %s acts for the wallet; nothing signed" % (
            utc(acct["authorized_at"])))
        tty.say("Ключ уже разрешён и работает — подписывать ничего не нужно.")
        return 0
    got = asyncio.run(owner_flow(k, op, k.PRODUCTION, tty, key_hex, relayer_key, owner))
    if got is None:
        out("G-AUTH %s FAIL: no owner's signature in %d links" % (op, LINKS))
        return 4
    wallet, session, until = got
    state = asyncio.run(registered(k, k.PRODUCTION, key_hex, wallet, session, want=(op == "authorize")))
    good = state is (op == "authorize")
    acct.update({"wallet": wallet.lower(), "session_key": session.lower(), "scopes": list(SCOPES)})
    if op == "authorize" and good:
        acct.update({"valid_until": until, "authorized_at": int(time.time())})
    if op == "revoke" and good:
        acct["revoked_at"] = int(time.time())
    write_json_atomic(ACCOUNT_FILE, acct)
    out("G-AUTH %s %s: the key %s for the wallet" % (op, "PASS" if good else "FAIL",
                                                      "acts" if state else "does not act"))
    tty.say("Готово: ключ %s." % ("разрешён и работает" if op == "authorize" else "отозван") if good else
            "Не получилось — исполнитель увидит причину в журнале.")
    return 0 if good else 4


def _word(address):
    return address.lower().removeprefix("0x").rjust(64, "0")


async def chain_call(k, env, data):
    """One eth_call on the collateral token through the client's own RPC with this TZ's agent: the 32-byte result
    as a number, None where the reply is not one."""
    cfg = env._config
    body = {"jsonrpc": "2.0", "id": 1, "method": "eth_call",
            "params": [{"to": cfg.collateral_token, "data": data}, "latest"]}
    async with k.httpx.AsyncClient(timeout=TIMEOUT_S) as h:
        r = await h.post(cfg.rpc_url, json=body)
        COUNTS["requests"] += 1
    try:
        res = r.json().get("result")
        return int(res, 16) if r.status_code == 200 and isinstance(res, str) and re.fullmatch(r"0x[0-9a-fA-F]{1,64}", res) \
            else None
    except ValueError:
        return None


async def chain_balance(k, env, wallet):
    """The wallet's pUSD on chain: balanceOf(wallet)."""
    return await chain_call(k, env, "0x" + BALANCE_OF + _word(wallet))


async def chain_allowances(k, env, wallet):
    """The wallet's pUSD allowance on chain to each exchange, by its letter: allowance(wallet, exchange)."""
    return {x: await chain_call(k, env, "0x" + ALLOWANCE_OF + _word(wallet) + _word(a)) for x, a in EXCHANGES}


def enough(v):
    return isinstance(v, int) and v >= RT_COST_UNITS


def shown(allowances):
    """Allowances as printed: pUSD, or max at 2^255 and above. Pure."""
    return {x: ("max" if isinstance(v, int) and v >= 1 << 255 else units(v)) for x, v in (allowances or {}).items()}


async def clob_refresh(k, c):
    """The CLOB's view of the wallet's pUSD and allowances re-read from chain: /balance-allowance/update, as the
    client's own allowance recovery calls it."""
    path, params = k.A.build_update_balance_allowance_request(
        asset_type="COLLATERAL", signature_type=k.W.signature_type_for(c._ctx.wallet_type))
    await c._ctx.secure_clob.get_bytes(path, params=params)
    COUNTS["requests"] += 1


async def ready_flow(k, env, key_hex, acct):
    """G-READY: the account read through the session key - a Deposit Wallet signed for by a session key, not in
    closed-only mode, its pUSD on chain at least one order's cost, its pUSD allowance on chain to each exchange at
    least that, and no open order of the key. The CLOB's own view, refreshed first, is printed beside, no threshold."""
    c = await k.AsyncSecureClient.create(private_key=key_hex, wallet=acct["wallet"], environment=env)
    try:
        session = k.Account.from_key(key_hex).address
        await clob_refresh(k, c)
        ba = await c.get_balance_allowance(asset_type="COLLATERAL")
        onchain = await chain_balance(k, env, acct["wallet"])
        allow = await chain_allowances(k, env, acct["wallet"])
        checks = {
            "a Deposit Wallet signed for by a session key": c.wallet_type == "DEPOSIT_WALLET"
            and c._ctx.signer_type == "SESSION_KEY",
            "not in closed-only mode": (await c.get_closed_only_mode()) is False,
            "its pUSD on chain at least one order's cost": enough(onchain),
            "its allowance on chain to the CTF exchange at least one order's cost": enough(allow["c"]),
            "its allowance on chain to the V2 exchange at least one order's cost": enough(allow["v"]),
            "no open order of the key": len(await first_items(c.list_open_orders())) == 0,
            "no open order of the wallet by the key": len(await first_items(
                c.list_wallet_open_orders(signer_addresses=[session]))) == 0}
        out("READY pUSD on chain %s, allowances on chain %s; the CLOB's view %s pUSD, allowances %d, at least one "
            "order's cost %d" % (units(onchain), shown(allow), units(ba.balance), len(ba.allowances),
                                 sum(1 for v in ba.allowances.values() if v >= RT_COST_UNITS)))
        return checks
    finally:
        await c.close()


def mode_ready():
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    k = client()
    checks = asyncio.run(ready_flow(k, k.PRODUCTION, load_session_key(), load_account()))
    for name, v in checks.items():
        out("G-READY %s: %s" % (name, "PASS" if v else "FAIL"))
    ok = all(checks.values())
    out("G-READY %s: %d of %d" % ("PASS" if ok else "FAIL", sum(checks.values()), len(checks)))
    return 0 if ok else 4


def dec(v):
    """A decimal as the venue would print it, normalized: 0.01, 5, 0. Pure."""
    import decimal
    d = decimal.Decimal(str(v)).normalize()
    return format(d, "f") if d != 0 else "0"


async def gamma_market(k, env, t0):
    """The five-minute market of window t0, its gamma document read with this TZ's agent - its tokens and condition
    taken, no price read."""
    async with k.httpx.AsyncClient(base_url=env._config.gamma_url, timeout=TIMEOUT_S) as h:
        r = await h.get("/markets/slug/%s%d" % (RT_FAMILY, t0))
        COUNTS["requests"] += 1
        return r.status_code, (r.json() if r.status_code == 200 else None)


async def roundtrip_flow(k, env, key_hex, acct, now=time.time, sleep=None, perf=time.perf_counter_ns):
    """G-RT's record: one post-only BUY of RT_SIZE at RT_PRICE, GTC, in the five-minute market open at placement -
    its Up token, its Down token where the first crosses the book - read back, cancelled by its id, read back, and
    the key's and the wallet's open orders and the balance read after. The market's own close is the venue's net
    under a resting order; cancel_all is this flow's last act whatever happened."""
    sleep = sleep or asyncio.sleep
    rt = {"placements": []}
    c = await k.AsyncSecureClient.create(private_key=key_hex, wallet=acct["wallet"], environment=env)
    try:
        session = k.Account.from_key(key_hex).address
        assert c.wallet_type == "DEPOSIT_WALLET" and c._ctx.signer_type == "SESSION_KEY", "not a session key"
        rt["closed_only"] = await c.get_closed_only_mode()
        rt["balance_before"] = await chain_balance(k, env, acct["wallet"])
        rt["clob_balance_before"] = (await c.get_balance_allowance(asset_type="COLLATERAL")).balance
        rt["open_before"] = len(await first_items(c.list_open_orders()))
        if rt["closed_only"] is not False or not isinstance(rt["balance_before"], int) \
                or rt["balance_before"] < RT_COST_UNITS or rt["open_before"]:
            rt["stopped"] = "before any placement: closed-only, balance or an open order"
            return rt
        t0, left = window_of(now())
        if left < RT_MIN_LEFT_S:
            out("RT window %d has %d s left, under %d: waiting %d s for the next" % (t0, left, RT_MIN_LEFT_S, left + 2))
            await sleep(left + 2)
            t0, left = window_of(now())
        status, doc = await gamma_market(k, env, t0)
        ok, why, tokens, cid, ex = market_reading(doc, t0)
        rt.update(market=RT_FAMILY + str(t0), market_status=status, market_reading=why, left_s=int(left), exchange=ex)
        out("RT market %s%d: gamma status %s, %s; %d s left in its window" % (RT_FAMILY, t0, status, why, left))
        if not ok:
            rt["stopped"] = "the market is not eligible"
            return rt
        spender = dict(EXCHANGES)[ex]
        rt["client_exchange"] = all(
            str(k.resolve_order_exchange_address(env._config, asset_id=t, neg_risk=False)).lower() == spender.lower()
            for t in tokens.values())
        rt["allowance"] = (await chain_allowances(k, env, acct["wallet"]))[ex]
        out("RT the client signs for the %s exchange: %s; the wallet's allowance on chain to it %s pUSD" % (
            "V2" if ex == "v" else "CTF", rt["client_exchange"], shown({ex: rt["allowance"]})[ex]))
        if not (rt["client_exchange"] and enough(rt["allowance"])):
            rt["stopped"] = "the client's exchange is not the market's, or its allowance is short"
            return rt
        await clob_refresh(k, c)
        oid = token = None
        for side in RT_SIDES[:RT_MAX_PLACEMENTS]:
            token = tokens[side]
            signed = await c.create_limit_order(asset_id=token, price=RT_PRICE, size=RT_SIZE, side="BUY",
                                                post_only=True)
            t_a = perf()
            try:
                resp = await c.post_order(signed)
                if resp.ok:
                    result = "live" if resp.status == "live" else "filled or pending: %s" % resp.status
                else:
                    result = resp.code if resp.code == "post_only_would_cross" else "refused: %s" % resp.code
            except k.RequestRejectedError as exc:
                resp = None
                result = "post_only_would_cross" if "crosses book" in str(exc) else "refused: status %s" % exc.status
            ms = (perf() - t_a) // 1000000
            rt["placements"].append({"side": side, "result": result, "ms": int(ms)})
            out("RT placement %d: BUY %s %s at %s, post-only, GTC: %s in %d ms" % (
                len(rt["placements"]), RT_SIZE, side, RT_PRICE, result, ms))
            if result == "live":
                oid = resp.order_id
                break
            if result != "post_only_would_cross":
                break
        if oid is None:
            rt["stopped"] = "no placement live"
            return rt
        o1 = await c.get_order(order_id=oid)
        rt["read_live"] = {"status": o1.status, "price": dec(o1.price), "size": dec(o1.original_size),
                           "side": o1.side, "type": o1.order_type, "matched": dec(o1.size_matched),
                           "maker is the wallet": o1.maker_address.lower() == acct["wallet"].lower(),
                           "asset is the token": str(o1.asset_id) == token}
        t_c = perf()
        cr = await c.cancel_order(order_id=oid)
        rt["cancel_ms"] = int((perf() - t_c) // 1000000)
        rt["cancel"] = {"canceled": oid in cr.canceled, "not_canceled": len(cr.not_canceled)}
        try:
            o2 = await c.get_order(order_id=oid)
            rt["read_after"] = {"status": o2.status, "matched": dec(o2.size_matched)}
        except k.RequestRejectedError as exc:
            rt["read_after"] = {"status": "not served, status %s" % exc.status, "matched": None}
        rt["open_after"] = len(await first_items(c.list_open_orders()))
        rt["wallet_open_after"] = len(await first_items(c.list_wallet_open_orders(signer_addresses=[session])))
        rt["balance_after"] = await chain_balance(k, env, acct["wallet"])
        rt["clob_balance_after"] = (await c.get_balance_allowance(asset_type="COLLATERAL")).balance
        out("RT read live %s; cancel %s in %d ms; read after %s; open after: the key's %d, the wallet's by the key %d; "
            "collateral on chain %s -> %s pUSD, the CLOB's view %s -> %s" % (
                rt["read_live"], rt["cancel"], rt["cancel_ms"], rt["read_after"], rt["open_after"],
                rt["wallet_open_after"], units(rt["balance_before"]), units(rt["balance_after"]),
                units(rt["clob_balance_before"]), units(rt["clob_balance_after"])))
        return rt
    finally:
        try:
            ca = await c.cancel_all()
            rt["final_cancel_all"] = {"canceled": len(ca.canceled), "not_canceled": len(ca.not_canceled)}
        except Exception as exc:   # the record says what the last act met; the gate reads the open orders
            rt["final_cancel_all"] = "error %s" % type(exc).__name__
        out("RT the last act, cancel_all of the key: %s" % (rt["final_cancel_all"],))
        await c.close()


def mode_roundtrip():
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    rc, so, _se = run(["timedatectl", "show", "-p", "NTPSynchronized", "--value"])
    synced = rc == 0 and so.strip() == "yes"
    out("RT clock NTP-synchronized: %s" % synced)
    if not synced:
        out("G-RT FAIL: the clock is not NTP-synchronized; no order placed")
        return 4
    k = client()
    acct = load_account()
    assert acct.get("wallet") and acct.get("session_key") and acct.get("authorized_at"), \
        "BLOCKED: the account record names no authorized session key"
    earlier = rt_paths()
    for p in earlier:
        prior = json_of((read_text(p) or "").encode()) or {}
        assert not prior.get("placements"), "BLOCKED: %s placed an order already; a round trip runs once" % p
    assert len(earlier) < 3, "BLOCKED: three round trips are recorded already"
    rt = asyncio.run(roundtrip_flow(k, k.PRODUCTION, load_session_key(), acct))
    rt["at"] = int(time.time())
    path = os.path.join(L1_VAR, "tz50-roundtrip-%d.json" % (len(earlier) + 1))
    n = write_private(path, (json.dumps(rt, sort_keys=True, indent=1) + "\n").encode())
    out("RT record %s: %d bytes, 0600" % (path, n))
    ok, checks = rt_reading(rt)
    for name, v in checks.items():
        out("G-RT %s: %s" % (name, "PASS" if v else "FAIL"))
    out("G-RT %s: %d of %d; this TZ's whole loss at most %s pUSD" % ("PASS" if ok else "FAIL", sum(checks.values()),
                                                                  len(checks), units(RT_LOSS_MAX_UNITS)))
    return 0 if ok else 4

# ---- the self-tests -----------------------------------------------------------------------------------------


class FakeTty:
    """The Boss's terminal, scripted: each answer a string, or a function of everything said so far."""

    def __init__(self, answers):
        self.answers, self.said = list(answers), []

    def say(self, text):
        self.said.append(text)

    def ask(self, prompt, hidden=False):
        self.said.append(prompt)
        a = self.answers.pop(0)
        return a(self.said) if callable(a) else a


class _Fake(http.server.BaseHTTPRequestHandler):
    """The self-tests' loopback stand-in of the relayer, the CLOB, gamma, GitHub Pages, PyPI, the geoblock and
    Telegram, under one port, each by its path's first segment. It records every request's agent."""
    protocol_version = "HTTP/1.1"

    def log_message(self, *_a):
        pass

    def _send(self, code, obj=None, raw=None, ctype="application/json"):
        body = raw if raw is not None else json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._route("GET")

    def do_POST(self):
        self._route("POST")

    def do_DELETE(self):
        self._route("DELETE")

    def _route(self, method):
        st = self.server.st
        u = urllib.parse.urlsplit(self.path)
        q = {a: b[0] for a, b in urllib.parse.parse_qs(u.query).items()}
        n = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(n) if n else b""
        body = json.loads(raw) if raw else None
        st["seen"].append((method, u.path, self.headers.get("User-Agent")))
        seg, rest = (u.path.split("/", 2)[1:] + [""])[:2]
        try:
            code, obj = (st["handlers"].get(seg) or st["handlers"]["*"])(st, method, "/" + rest, q, body, self.headers)
        except Exception as exc:     # a stand-in's own fault is a 500 the test sees
            code, obj = 500, {"error": "%s: %s" % (type(exc).__name__, exc)}
        if isinstance(obj, (bytes, bytearray)):
            self._send(code, raw=bytes(obj), ctype="application/octet-stream")
        else:
            self._send(code, obj)


def fake_server(handlers):
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _Fake)
    srv.daemon_threads = True
    srv.st = {"seen": [], "handlers": handlers}
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def _tx_handler(st, txid):
    st["polls"][txid] = st["polls"].get(txid, 0) + 1
    state = "STATE_CONFIRMED" if st["polls"][txid] >= 2 else "STATE_NEW"
    return 200, {"transaction_id": txid, "transaction_hash": "0x" + "ab" * 32, "state": state, "error_msg": None}


def _relayer(k):
    def handler(st, method, path, q, body, h):
        if method == "GET" and path == "/deployed":
            return 200, {"deployed": q.get("address", "").lower() == st["wallet"].lower()}
        if method == "GET" and path == "/v1/account/transactions/params":
            assert q.get("type") == "WALLET" and q.get("address", "").lower() == st["owner"].lower()
            return 200, {"address": "0x" + "11" * 20, "nonce": str(st["nonce"])}
        if method == "GET" and path.startswith("/v1/account/transactions/"):
            return _tx_handler(st, path.rsplit("/", 1)[1])
        if method == "POST" and path in ("/v1/session-signers/authorizations", "/v1/session-signers/revocations"):
            assert h.get("RELAYER_API_KEY") == st["relayer_key"], "the relayer key"
            assert h.get("RELAYER_API_KEY_ADDRESS") == st["owner"], "the relayer key's address"
            assert h.get("Idempotency-Key"), "an idempotency key"
            auth = path.endswith("authorizations")
            want = {"deadline", "nonce", "sessionSignerAddress", "signature", "walletAddress"} | (
                {"scopes", "validUntil"} if auth else set())
            assert set(body) == want, sorted(body)
            assert body["walletAddress"] == st["wallet"] and body["nonce"] == str(st["nonce"])
            assert int(body["deadline"]) >= int(time.time()) + 10, "the deadline"
            if auth:
                assert body["scopes"] == list(SCOPES)
                assert abs(int(body["validUntil"]) - int(time.time()) - LIFETIME_S) < 120, "validUntil"
                call = k.C.authorize_session_signer_call(wallet_address=st["wallet"],
                                                         session_signer=body["sessionSignerAddress"],
                                                         valid_until=int(body["validUntil"]))
            else:
                call = k.C.revoke_session_signer_call(wallet_address=st["wallet"],
                                                      session_signer=body["sessionSignerAddress"])
            td = k.build_deposit_wallet_typed_data(wallet=st["wallet"], calls=[call], nonce=body["nonce"],
                                                   deadline=body["deadline"], chain_id=CHAIN_ID)
            rec = k.Account.recover_message(k.encode_typed_data(full_message=td), signature=body["signature"])
            assert rec == st["owner"], "the owner's signature"
            st["nonce"] += 1
            if st.get("refuse"):
                return 200, {"operationId": "op", "status": "FAILED", "transactionHash": "", "transactionId": "txf"}
            if auth:
                st["authorized"].add(body["sessionSignerAddress"].lower())
                return 200, {"operationId": "op", "status": "SUBMITTED", "transactionHash": "0x" + "cd" * 32,
                             "transactionId": "txa%d" % st["nonce"]}
            st["authorized"].discard(body["sessionSignerAddress"].lower())
            return 200, {"fenced": True, "operationId": "op", "status": "PENDING", "transactionId": "txr%d" % st["nonce"]}
        if method == "POST" and path == "/submit":
            assert h.get("RELAYER_API_KEY") == st["relayer_key"], "the relayer key"
            assert h.get("RELAYER_API_KEY_ADDRESS") == st["owner"], "the relayer key's address"
            dw = body["depositWalletParams"]
            assert (body["type"], body["from"], body["to"], body["nonce"], body["metadata"], dw["depositWallet"]) == (
                "WALLET", st["owner"], k.PRODUCTION._config.wallet_derivation.deposit_wallet_factory, str(st["nonce"]),
                APPROVE_METADATA, st["wallet"]), body
            spenders = ["0x" + c["data"][34:74] for c in dw["calls"]]
            calls = [k.C.erc20_approval_call(token_address=PUSD, spender=k.to_checksum_address(a), amount=APPROVE_UNITS)
                     for a in spenders]
            assert [(c["target"], c["value"], c["data"]) for c in dw["calls"]] == [
                (str(c.to), "0", str(c.data)) for c in calls], dw["calls"]
            td = k.build_deposit_wallet_typed_data(wallet=st["wallet"], calls=calls, nonce=body["nonce"],
                                                   deadline=dw["deadline"], chain_id=CHAIN_ID)
            rec = k.Account.recover_message(k.encode_typed_data(full_message=td), signature=body["signature"])
            assert rec == st["owner"], "the owner's signature"
            st["nonce"] += 1
            st["batches"].append(spenders)
            for a in spenders:
                st["allowances"][a] = APPROVE_UNITS
            return 200, {"transactionID": "txp%d" % st["nonce"], "transactionHash": "", "state": "STATE_NEW"}
        return 404, {"error": "no such path %s %s" % (method, path)}
    return handler


def _order_wire(o, st):
    return {"id": o["id"], "market": st["cid"], "asset_id": o["token"], "owner": o["owner"],
            "maker_address": st["wallet"], "side": "BUY", "price": o["price"], "original_size": o["size"],
            "size_matched": "0", "outcome": "Up" if o["token"] == st["tokens"]["Up"] else "Down", "order_type": "GTC",
            "status": o["status"], "associate_trades": [], "created_at": 1795000000, "expiration": "0"}


def _clob(st, method, path, q, body, h):
    addr = (h.get("POLY_ADDRESS") or "").lower()
    if path in ("/auth/api-key", "/auth/derive-api-key"):
        assert h.get("POLY_SIGNATURE") and h.get("POLY_TIMESTAMP") and h.get("POLY_NONCE") == "0", "L1 headers"
        if method == "POST" and addr in st["creds"]:
            return 400, {"error": "Could not create api key"}
        st["creds"].setdefault(addr, {"apiKey": "k-%d" % len(st["creds"]),
                                      "secret": base64.urlsafe_b64encode(os.urandom(32)).decode(), "passphrase": "pp"})
        return 200, st["creds"][addr]
    if path.startswith("/markets-by-token/"):
        return 200, {"condition_id": st["cid"]}
    if path.startswith("/clob-markets/"):
        return 200, {"nr": False, "mts": "0.01", "fd": {"r": 0.07, "e": 1},
                     "t": [{"t": st["tokens"]["Up"]}, {"t": st["tokens"]["Down"]}]}
    cred = st["creds"].get(addr)
    if not (cred and h.get("POLY_API_KEY") == cred["apiKey"] and h.get("POLY_SIGNATURE") and h.get("POLY_TIMESTAMP")):
        return 401, {"error": "Unauthorized/Invalid api key"}
    if path == "/auth/api-keys":
        return 200, {"apiKeys": [cred["apiKey"]]}
    if addr not in st["authorized"]:
        return 401, {"error": "the signer is not authorized for the wallet"}
    mine = [o for o in st["orders"].values() if o["owner"] == cred["apiKey"]]
    if path == "/auth/ban-status/closed-only":
        return 200, {"closed_only": False}
    if path == "/balance-allowance/update":
        assert q.get("asset_type") == "COLLATERAL" and q.get("signature_type") == "3", q
        st["refreshed"] = st.get("refreshed", 0) + 1
        return 200, {}
    if path == "/balance-allowance":
        assert q.get("asset_type") == "COLLATERAL" and q.get("signature_type") == "3", q
        return 200, {"balance": str(st["balance"]), "allowances": {"0x" + "e1" * 20: "115792089237316195423570985008687"}}
    if path == "/order" and method == "POST":
        o = body["order"]
        assert body.get("postOnly") is True and body.get("orderType") == "GTC" and body.get("owner") == cred["apiKey"]
        assert (o["side"], o["signatureType"], o["maker"], o["signer"], o["makerAmount"], o["takerAmount"]) == (
            "BUY", 3, st["wallet"], st["wallet"], "50000", "5000000"), o
        st["posted"].append(o["tokenId"])
        if o["tokenId"] == st.get("cross"):
            msg = "invalid post-only order: order crosses book"
            if st.get("cross_http"):
                return 400, {"error": msg}
            return 200, {"success": False, "errorMsg": msg, "orderID": "", "status": "", "makingAmount": "",
                         "takingAmount": ""}
        oid = "0x%064x" % (len(st["orders"]) + 1)
        st["orders"][oid] = {"id": oid, "token": o["tokenId"], "owner": cred["apiKey"], "price": "0.01", "size": "5",
                             "status": "LIVE"}
        status = st.get("post_status", "live")
        return 200, {"success": True, "errorMsg": "", "orderID": oid, "status": status, "makingAmount": "",
                     "takingAmount": "", "tradeIDs": [], "transactionsHashes": []}
    if path.startswith("/data/order/"):
        o = st["orders"].get(path.rsplit("/", 1)[1])
        return (200, _order_wire(o, st)) if o else (404, {"error": "order not found"})
    if path == "/order" and method == "DELETE":
        o = st["orders"].get(body["orderID"])
        if o and o["status"] == "LIVE":
            o["status"] = "CANCELED"
            return 200, {"canceled": [o["id"]], "not_canceled": {}}
        return 200, {"canceled": [], "not_canceled": {body["orderID"]: "order not found"}}
    if path == "/cancel-all" and method == "DELETE":
        ids = [o["id"] for o in mine if o["status"] == "LIVE"]
        for i in ids:
            st["orders"][i]["status"] = "CANCELED"
        return 200, {"canceled": ids, "not_canceled": {}}
    if path == "/data/orders":
        return 200, {"data": [_order_wire(o, st) for o in mine if o["status"] == "LIVE"], "next_cursor": "LTE="}
    if path == "/data/wallet-open-orders":
        live = [o for o in st["orders"].values() if o["status"] == "LIVE"]
        return 200, {"data": [dict(_order_wire(o, st), signer_address=addr) for o in live], "next_cursor": ""}
    return 404, {"error": "no such path %s %s" % (method, path)}


def _rpc(st, method, path, q, body, h):
    assert method == "POST" and body["method"] == "eth_call" and body["params"][1] == "latest", body
    call = body["params"][0]
    d = call["data"]
    assert call["to"] == PUSD and d[34:74] == st["wallet"].lower()[2:], call
    if d[:10] == "0x" + BALANCE_OF and len(d) == 74:
        v = st["balance"]
    else:
        assert d[:10] == "0x" + ALLOWANCE_OF and len(d) == 138, call
        v = st["allowances"].get("0x" + d[98:138], 0)
    return 200, {"jsonrpc": "2.0", "id": body["id"], "result": "0x%064x" % v}


def _gamma(st, method, path, q, body, h):
    if path == "/markets/slug/%s%d" % (RT_FAMILY, st["t0"]):
        doc = {"slug": RT_FAMILY + str(st["t0"]), "active": True, "closed": False, "acceptingOrders": True,
               "enableOrderBook": True, "orderMinSize": 5, "conditionId": st["cid"], "negRisk": False,
               "outcomes": json.dumps(["Up", "Down"]), "outcomePrices": json.dumps(["0.5", "0.5"]),
               "clobTokenIds": json.dumps([st["ctf"]["Up"], st["ctf"]["Down"]])}
        if st.get("version") == "v2":
            doc.update(version="v2", positionIds=json.dumps([st["v2"]["Up"], st["v2"]["Down"]]))
        return 200, doc
    return 404, {"error": "not found"}


def withheld(text):
    """No EVM address and no 32-byte hex - an order's id, a transaction's hash - in `text`. Pure."""
    return re.search(r"0x[0-9a-fA-F]{40}", text) is None


def quiet(fn):
    """fn's result and every line it printed; the lines printed again after."""
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        got = fn()
    sys.stdout.write(buf.getvalue())
    return got, buf.getvalue()


def mode_sdk_selftest():
    """The client's flows, in /root/l1-env, against the loopback stand-in: the owner's authorization from a link
    signed as the page signs, wrong answers refused; the key's registration; G-READY; the round trip in its four
    shapes; the revocation; a relayer's refusal; every request with this TZ's agent; the hook's IPv4 rules live."""
    k = client()
    passed = []

    def ok(cond, what):
        assert cond, "SDK SELFTEST FAIL: " + what
        passed.append(what)
        out("ok   " + what)

    ok(k.httpx._client.USER_AGENT == UA and socket.getaddrinfo is gai4, "the client's agent and lookups are this TZ's")
    for fam, bad in ((socket.AF_INET6, True), (socket.AF_UNIX, False)):
        try:
            s = socket.socket(fam, socket.SOCK_STREAM)
            s.close()
            refused = False
        except GuardError:
            refused = True
        ok(refused == bad, "the hook: a socket of family %s %s" % (fam.name, "refused" if bad else "let through"))
    try:
        socket.getaddrinfo("localhost", 80, socket.AF_INET6)
        ok(False, "an AF_INET6 lookup")
    except GuardError:
        ok(True, "the hook: an AF_INET6 lookup refused by gai4")
    try:
        socket.getaddrinfo("example.com", 443)
        ok(False, "a lookup of an unlisted host")
    except GuardError:
        ok(True, "the hook: a lookup of a host this mode does not name refused")
    a, b = socket.socketpair()
    a.close()
    b.close()
    ok(True, "the hook: asyncio's self-pipe, an AF_UNIX socketpair, let through")

    owner, other = k.Account.create(), k.Account.create()
    sess_key = "0x" + os.urandom(32).hex()
    session = k.Account.from_key(sess_key).address
    cfg0 = k.PRODUCTION._config
    wallet = k.W.derive_beacon_deposit_wallet_address(owner.address, cfg0.wallet_derivation)
    h1, h2 = (int.from_bytes(hashlib.sha256(b).digest(), "big") for b in (b"tz50 up", b"tz50 down"))
    ctf = {"Up": str(h1), "Down": str(h2)}                                    # reserved bits set: CTF token IDs
    v2 = {"Up": str((h1 >> 104 << 104) | 1), "Down": str((h1 >> 104 << 104) | 2)}   # reserved bits zero: V2 IDs
    assert all(int(t) & V2_RESERVED for t in ctf.values()) and not any(int(t) & V2_RESERVED for t in v2.values())
    st_extra = {"owner": owner.address, "wallet": wallet, "relayer_key": "rk-0123456789abcdef", "nonce": 7,
                "authorized": set(), "polls": {}, "creds": {}, "orders": {}, "balance": 10000000,
                "cid": "0x" + "ab" * 32, "ctf": ctf, "v2": v2, "tokens": ctf, "allowances": {}, "batches": [],
                "posted": []}
    srv = fake_server({"relayer": _relayer(k), "clob": _clob, "gamma": _gamma, "rpc": _rpc})
    srv.st.update(st_extra)
    st = srv.st
    env = test_env(k, "http://127.0.0.1:%d" % srv.server_address[1])

    def sign_from(said, key=owner):
        url = [s for s in said if s.startswith("https://x.test/l1-sign.html#")][-1]
        f = dict(p.split("=", 1) for p in url.split("#", 1)[1].split("&"))
        if f["op"] == "authorize":
            calls = [k.C.authorize_session_signer_call(wallet_address=f["w"], session_signer=f["k"],
                                                       valid_until=int(f["u"]))]
        elif f["op"] == "revoke":
            calls = [k.C.revoke_session_signer_call(wallet_address=f["w"], session_signer=f["k"])]
        else:
            calls = [k.C.erc20_approval_call(token_address=PUSD, spender=dict(EXCHANGES)[x], amount=APPROVE_UNITS)
                     for x in f["x"]]
        td = k.build_deposit_wallet_typed_data(wallet=f["w"], calls=calls, nonce=f["n"], deadline=f["d"],
                                               chain_id=CHAIN_ID)
        return "0x" + key.sign_message(k.encode_typed_data(full_message=td)).signature.hex().removeprefix("0x")

    tty = FakeTty(["not a signature", lambda said: sign_from(said, other), sign_from])
    got, printed = quiet(lambda: asyncio.run(owner_flow(k, "authorize", env, tty, sess_key, st["relayer_key"],
                                                        owner.address.lower(), page_url="https://x.test/l1-sign.html")))
    ok(got is not None and got[0] == wallet and got[1] == session and session.lower() in st["authorized"],
       "authorize: a link signed as the page signs, after a non-signature and another key's signature refused")
    ok(sum(1 for s in tty.said if "Подпись не владельца" in s) == 1 and sum(1 for s in tty.said if "Это не подпись" in s)
       == 1, "authorize: the two wrong answers each refused once, at the terminal")
    ok(st["nonce"] == 8, "authorize: the relayer took one request, its nonce moved once")
    ok(withheld(printed) and not withheld("\n".join(tty.said)),
       "authorize: the printed lines carry no address and no hash; the terminal shows them to the Boss")
    ok(asyncio.run(registered(k, env, sess_key, wallet, session, want=True, tries=2, gap=0)) is True,
       "the key's registration: it lists the wallet's orders")
    other_key = "0x" + os.urandom(32).hex()
    ok(asyncio.run(registered(k, env, other_key, wallet, k.Account.from_key(other_key).address, want=True, tries=2,
                              gap=0)) is False, "a key never authorized: refused at each of two reads")
    acct = {"owner": owner.address.lower(), "wallet": wallet.lower(), "session_key": session.lower(),
            "authorized_at": 1}
    fresh = "0x" + hashlib.sha256(b"tz50 another session key").hexdigest()
    ok(quiet(lambda: asyncio.run(authorize_kept(k, env, sess_key, acct)))[0] is True and
       quiet(lambda: asyncio.run(authorize_kept(k, env, sess_key, dict(acct, revoked_at=2))))[0] is False and
       quiet(lambda: asyncio.run(authorize_kept(k, env, fresh, acct)))[0] is False,
       "authorize kept on a second run: this key, unrevoked, acting; a revoked record or another key is not")
    checks = asyncio.run(ready_flow(k, env, sess_key, acct))
    ok(sum(checks.values()) == 5 and not checks["its allowance on chain to the CTF exchange at least one order's cost"]
       and not checks["its allowance on chain to the V2 exchange at least one order's cost"],
       "G-READY before any approval: 5 of 7, both allowances short")
    ctf_x, v2_x = (a.lower() for _x, a in EXCHANGES)
    st["allowances"] = {ctf_x: 2 ** 256 - 1}
    tty = FakeTty([sign_from])
    got, printed = quiet(lambda: asyncio.run(approve_flow(k, env, tty, st["relayer_key"], owner.address.lower(),
                                                          page_url="https://x.test/l1-sign.html", sleep=lambda s: None)))
    link = [x for x in tty.said if x.startswith("https://x.test/l1-sign.html#")]
    ok(got[2] == {"c": 2 ** 256 - 1, "v": APPROVE_UNITS} and st["batches"] == [[v2_x]] and len(link) == 1 and
       "&x=v&" in link[0] and st["nonce"] == 9 and withheld(printed),
       "approve, the V2 exchange short: one link of x=v, one call of 1 pUSD, the CTF exchange's maximum kept")
    st["allowances"] = {}
    tty = FakeTty(["", sign_from])
    got, printed = quiet(lambda: asyncio.run(approve_flow(k, env, tty, st["relayer_key"], owner.address.lower(),
                                                          page_url="https://x.test/l1-sign.html", sleep=lambda s: None)))
    links = [x for x in tty.said if x.startswith("https://x.test/l1-sign.html#")]
    ok(got[2] == {"c": APPROVE_UNITS, "v": APPROVE_UNITS} and st["batches"][-1] == [ctf_x, v2_x] and len(links) == 2
       and all("&x=cv&" in x for x in links) and st["nonce"] == 10,
       "approve, both short: an empty answer gives a second link, one batch of two calls of 1 pUSD each")
    got, printed = quiet(lambda: asyncio.run(approve_flow(k, env, FakeTty([]), st["relayer_key"],
                                                          owner.address.lower(), page_url="https://x.test/l1-sign.html")))
    ok(got[1] is got[2] and len(st["batches"]) == 2 and st["nonce"] == 10,
       "approve, nothing short: kept, nothing asked, nothing sent")
    checks = asyncio.run(ready_flow(k, env, sess_key, acct))
    ok(all(checks.values()) and len(checks) == 7 and st["refreshed"] >= 2,
       "G-READY: 7 of 7 against the stand-in, the CLOB's view refreshed first")

    def trip(now, cross=None, cross_http=False, post_status="live"):
        st.update(cross=cross, cross_http=cross_http, post_status=post_status, t0=window_of(now)[0])
        slept = []

        async def nap(s):
            slept.append(s)
            st["t0"] = window_of(now + s)[0]

        clock = [now]

        def fake_now():
            return clock[0] + sum(slept)
        rt, printed = quiet(lambda: asyncio.run(roundtrip_flow(k, env, sess_key, acct, now=fake_now, sleep=nap)))
        assert withheld(printed), "the round trip printed an address, an id or a hash"
        return rt, slept

    base = 1795000020.0
    for label, kw, sides in (("Up crossing, as a 400", dict(cross=ctf["Up"], cross_http=True), ["Up", "Down"]),
                             ("Up crossing, as a refusal", dict(cross=ctf["Up"]), ["Up", "Down"]),
                             ("no crossing", {}, ["Up"])):
        rt, slept = trip(base, **kw)
        good, chk = rt_reading(rt)
        ok(good and [p["side"] for p in rt["placements"]] == sides and slept == [] and rt["read_after"]["status"] ==
           "CANCELED" and rt["final_cancel_all"] == {"canceled": 0, "not_canceled": 0},
           "the round trip, %s: G-RT PASS, %d of %d, placements %s" % (label, sum(chk.values()), len(chk), sides))
    rt, slept = trip(base + 80)
    ok(rt_reading(rt)[0] and slept == [102.0] and rt["market"] == RT_FAMILY + str(int(base) // 300 * 300 + 300),
       "the round trip with 100 s left: waits 102 s for the next window, and PASS there")
    st.update(version="v2", tokens=v2)
    rt, slept = trip(base, cross=v2["Up"])
    ok(rt_reading(rt)[0] and rt["exchange"] == "v" and rt["client_exchange"] is True and
       [p["side"] for p in rt["placements"]] == ["Up", "Down"] and st["posted"][-2:] == [v2["Up"], v2["Down"]] and
       all(t in ctf.values() for t in st["posted"][:-2]),
       "the round trip on a Protocol V2 market: its positionIds traded through the V2 exchange, G-RT PASS")
    st["allowances"][v2_x] = 10
    rt, slept = trip(base)
    ok(not rt_reading(rt)[0] and rt["placements"] == [] and rt["exchange"] == "v" and "allowance" in rt["stopped"],
       "the round trip with the V2 exchange's allowance short: nothing placed, G-RT FAIL")
    st.update(version=None, tokens=ctf)
    st["allowances"][v2_x] = APPROVE_UNITS
    rt, slept = trip(base, post_status="matched")
    good, chk = rt_reading(rt)
    ok(not good and rt["placements"][0]["result"] == "filled or pending: matched" and
       rt["final_cancel_all"]["canceled"] == 1,
       "the round trip with a placement matched: G-RT FAIL, and the last act cancels what stands")
    st["balance"] = 10
    rt, _s = trip(base)
    ok(not rt_reading(rt)[0] and rt["placements"] == [] and "before any placement" in rt.get("stopped", ""),
       "the round trip under one order's cost: nothing placed, G-RT FAIL")
    st["balance"] = 10000000
    ok(all(o["status"] != "LIVE" for o in st["orders"].values()), "no order of the stand-in left live by any trip")

    tty = FakeTty([sign_from])
    got = asyncio.run(owner_flow(k, "revoke", env, tty, sess_key, st["relayer_key"], owner.address.lower(),
                                 page_url="https://x.test/l1-sign.html"))
    ok(got is not None and session.lower() not in st["authorized"], "revoke: one link signed, the key removed")
    ok(asyncio.run(registered(k, env, sess_key, wallet, session, want=False, tries=2, gap=0)) is False,
       "after revoke: the key refused")
    st["refuse"] = True
    try:
        asyncio.run(owner_flow(k, "authorize", env, FakeTty([sign_from]), sess_key, st["relayer_key"],
                               owner.address.lower(), page_url="https://x.test/l1-sign.html"))
        ok(False, "a relayer's FAILED")
    except Exception as exc:
        ok(type(exc).__name__ == "TransactionFailedError", "authorize: the relayer's FAILED raises %s" %
           type(exc).__name__)
    st["refuse"] = False
    agents = sorted({ua for _m, _p, ua in st["seen"]})
    ok(agents == [UA], "every one of %d requests carried the agent %s" % (len(st["seen"]), UA))
    srv.shutdown()
    out("SDK SELFTEST PASS: %d checks, %d passed; refused by the hook: %d, each a check's own" % (
        len(passed), len(passed), len(REFUSED)))
    return 0


def _ssh_str(b):
    return struct.pack(">I", len(b)) + b


def _pub(kind, *parts):
    return "%s %s tz50-selftest" % (kind, base64.b64encode(_ssh_str(kind.encode()) + b"".join(
        _ssh_str(p) for p in parts)).decode())


def mode_selftest():
    """Every rule of this file that needs no client: the readings on literals; the hook's decisions and its live
    refusals; the credentials' files and the Boss's key under a temporary tree; the geoblock, the page, the wheels
    and Telegram against a loopback stand-in, each request with this TZ's agent."""
    passed = []

    def ok(cond, what):
        assert cond, "SELFTEST FAIL: " + what
        passed.append(what)
        out("ok   " + what)

    def refused(fn):
        try:
            fn()
        except GuardError:
            return True
        return False

    if os.path.exists(TMP):
        shutil.rmtree(TMP)
    os.mkdir(TMP, 0o700)
    # -- the readings, pure
    ok(number_reading([OWN_TZ, "CryptoTZ/TZ-49-x.md"], OWN_TZ)[0] and not number_reading(
        [OWN_TZ, "CryptoTZ/TZ-50-other.md"], OWN_TZ)[0] and not number_reading(
        [OWN_TZ, "CryptoReports/TZ-50-l1-account-round-trip-report.md"], OWN_TZ)[0], "NUMBER: own file alone, no report")
    kinds, br = refs_reading("a\tHEAD\nb\trefs/heads/main\nc\trefs/heads/tz-49-x\nd\trefs/tags/rewardbook-streams-1\n"
                             "e\trefs/heads/" + BRANCH + "\n")
    ok(br and kinds == {"HEAD": 1, "refs/heads/main": 1, "refs/heads/tz-*": 2, "refs/tags/rewardbook-streams-*": 1},
       "refs by kind, this TZ's branch seen")
    ok(room_reading(8000000000, 100) == (8000000100, 8000000100 - STREAM_FLOOR - PEAK), "the room and its margin")
    for status, doc, want in ((200, {"blocked": False, "country": "BG", "ip": "x"}, "PASS"),
                              (200, {"blocked": True, "country": "PL"}, "BLOCKED"),
                              (200, {"blocked": "false", "country": "BG"}, "UNREAD"),
                              (200, {"blocked": False, "country": "bg"}, "UNREAD"), (403, None, "UNREAD")):
        ok(geo_reading(status, doc) == want, "G-GEO %s on %r" % (want, doc))
    ok("198.51.100.7" not in str(geo_fields({"blocked": False, "country": "BG", "ip": "198.51.100.7"})),
       "G-GEO prints the reply's keys and fields, never its address")
    good = ("vs-2348", {"ID": "ubuntu", "VERSION_ID": "24.04"}, (3, 12, 3), [], [LIVE_HOST_KEY])
    ok(live_gate(*good)[0], "the live host gate: 5 of 5")
    for i, bad in enumerate((("vs-2348.example",), ({"ID": "debian", "VERSION_ID": "12"},), ((3, 13, 0),),
                             (["/var/lib/btc-recorder"],), ([("ssh-ed25519", "SHA256:x")],))):
        args = list(good)
        args[i] = bad[0]
        ok(not live_gate(*args)[0], "the live host gate fails on LH%d alone" % (i + 1))
    eff = sshd_effective("port 22\npasswordauthentication no\nkbdinteractiveauthentication no\npermitrootlogin "
                         "without-password\npubkeyauthentication yes\n")
    ok(ssh_reading((SSHD_SHA256, 0o644), eff)[0], "G-SSH K1 to K5: 5 of 5")
    ok(not ssh_reading((SSHD_SHA256, 0o600), eff)[0] and not ssh_reading(None, eff)[0], "G-SSH K1 fails alone")
    for kw, v in SSHD_IN_FORCE:
        ok(not ssh_reading((SSHD_SHA256, 0o644), dict(eff, **{kw: "yes" if v != "yes" else "no"}))[0],
           "G-SSH fails on %s alone" % kw)
    ok(methods_of("debug1: Authentications that can continue: publickey\nfoo 192.0.2.1\n"
                  "debug1: Authentications that can continue: publickey\n") == ["publickey"], "methods, the address never")
    ok(reclaimable(WORK) and not reclaimable("/root") and not reclaimable("/tmp/x/y"), "reclaim's trees")
    ed = _pub("ssh-ed25519", b"\x01" * 32)
    rsa4k = _pub("ssh-rsa", b"\x01\x00\x01", b"\x00" + b"\xff" * 512)
    rsa2k = _pub("ssh-rsa", b"\x01\x00\x01", b"\x00" + b"\xff" * 256)
    ok(pubkey_line(ed)[1:3] == ("ssh-ed25519", key_fingerprints(ed)[0][1]), "the Boss's key: ed25519, its fingerprint")
    ok(pubkey_line(rsa4k)[3] == 4096, "the Boss's key: RSA of 4096 bits")
    for bad, why in ((rsa2k, "RSA of 2048 bits"), ("-----BEGIN OPENSSH PRIVATE KEY-----", "a private key"),
                     ('from="10.0.0.1" ' + ed, "options before the key"), ("ssh-ed25519 %%%", "not base64"),
                     (ed + "\n" + ed, "two lines"), ("ssh-dss AAAA", "an unknown type"),
                     (_pub("ssh-ed25519", b"\x01" * 31), "a short ed25519 key"),
                     ("ssh-rsa " + ed.split()[1], "a blob of another type")):
        try:
            pubkey_line(bad)
            ok(False, "the Boss's key refuses " + why)
        except ValueError:
            ok(True, "the Boss's key refuses " + why)
    ok(valid_address("0x" + "aB" * 20) == "0x" + "ab" * 20 and valid_address(ZERO_ADDRESS) is None and
       valid_address("0x12") is None, "an address as typed")
    ok(token_ok("123456789:" + "A" * 35) and not token_ok("123:abc") and relayer_key_ok("019a2b3c-4d5e-6f70-8192-a3b4c5d6e7f8")
       and not relayer_key_ok("short") and not relayer_key_ok("has space in it here"), "a token and a relayer key")
    o, w, s_ = "0x" + "1" * 40, "0x" + "2" * 40, "0x" + "3" * 40
    ok(sign_link("authorize", o, w, s_, 7, 1800000600, 1815534000) == PAGE_URL + "#v=1&op=authorize&o=%s&w=%s&k=%s"
       "&u=1815534000&n=7&d=1800000600" % (o, w, s_) and sign_link("revoke", o, w, s_, 8, 9).endswith(
        "#v=1&op=revoke&o=%s&w=%s&k=%s&n=8&d=9" % (o, w, s_)) and sign_link("approve", o, w, None, 10, 11,
                                                                       exchanges="cv").endswith(
        "#v=1&op=approve&o=%s&w=%s&x=cv&n=10&d=11" % (o, w)), "the signing link's fields, the page's order")
    try:
        sign_link("approve", o, w, None, 1, 2, exchanges="cvz")
        ok(False, "an approval of another exchange")
    except AssertionError:
        ok(True, "the signing link refuses an approval of a third exchange")
    req = requirements_text()
    ok(len(WHEEL_SET) == 35 and req.count("\n") == 34 and "pip==" not in req and "polymarket-client==0.20.0 --hash"
       in req and req.split("\n")[:-1] == sorted(req.split("\n")[:-1]), "the requirements: 34 pinned lines, pip's not")
    p = pins()
    ok(installed_reading(dict(p), p)[0] and installed_reading(dict(p, extra="1"), p)[2] == ["extra"] and
       installed_reading({a: b for a, b in p.items() if a != "httpx"}, p)[1] == ["httpx"] and
       installed_reading(dict(p, httpx="9"), p)[3] == ["httpx"], "G-ENV's installed reading and its three faults")
    ups = [{"update_id": 1, "message": {"text": "/start", "chat": {"id": 42, "type": "private"}}},
           {"update_id": 2, "message": {"text": "hi", "chat": {"id": 43, "type": "private"}}},
           {"update_id": 3, "message": {"text": "/start", "chat": {"id": -5, "type": "group"}}}]
    ok(private_starts(ups) == [42], "the private chats that sent /start")
    ok(window_of(1795000020) == (1794999900, 180) and window_of(1795000200) == (1795000200, 300), "the window")
    t1, t2 = str(3 << 200 | 5 << 50), str(7 << 200 | 9 << 60)            # reserved bits set: CTF token IDs
    p1, p2 = str(3 << 200 | 1), str(3 << 200 | 2)                        # reserved bits zero: V2 position IDs
    doc = {"slug": RT_FAMILY + "1794999900", "active": True, "closed": False, "acceptingOrders": True,
           "enableOrderBook": True, "orderMinSize": 5, "conditionId": "0x" + "ab" * 32, "negRisk": False,
           "outcomes": '["Down", "Up"]', "clobTokenIds": json.dumps([t2, t1])}
    ok(market_reading(doc, 1794999900) == (True, "eligible, CTF", {"Down": t2, "Up": t1}, "0x" + "ab" * 32, "c"),
       "the market: a CTF market, its token IDs by outcome, the CTF exchange")
    v2doc = dict(doc, version="v2", positionIds=json.dumps([p2, p1]))
    ok(market_reading(v2doc, 1794999900) == (True, "eligible, Protocol V2", {"Down": p2, "Up": p1}, "0x" + "ab" * 32,
                                             "v"), "the market: a Protocol V2 market, its position IDs, the V2 exchange")
    for key, val in (("slug", "x"), ("closed", True), ("acceptingOrders", False), ("orderMinSize", 15),
                     ("outcomes", '["Yes", "No"]'), ("conditionId", "0x12"), ("clobTokenIds", "not json"),
                     ("negRisk", True), ("version", "v3"), ("clobTokenIds", json.dumps([p2, p1]))):
        ok(not market_reading(dict(doc, **{key: val}), 1794999900)[0], "the market refused on %s %s" % (
            key, ("V2 position IDs" if val == json.dumps([p2, p1]) else repr(val))))
    for key, val in (("positionIds", json.dumps([t2, t1])), ("positionIds", None)):
        ok(not market_reading(dict(v2doc, **{key: val}), 1794999900)[0], "the V2 market refused on %s %s" % (
            key, "CTF token IDs" if val else "absent"))
    rt = {"placements": [{"side": "Up", "result": "post_only_would_cross", "ms": 40},
                         {"side": "Down", "result": "live", "ms": 50}],
          "read_live": {"status": "LIVE", "price": "0.01", "size": "5", "side": "BUY", "type": "GTC", "matched": "0",
                        "maker is the wallet": True, "asset is the token": True},
          "cancel": {"canceled": True, "not_canceled": 0}, "read_after": {"status": "CANCELED", "matched": "0"},
          "open_after": 0, "wallet_open_after": 0, "balance_before": 10000000, "balance_after": 10000000,
          "market": RT_FAMILY + "1794999900", "cancel_ms": 60}
    ok(rt_reading(rt)[0], "G-RT: PASS on a record of two placements")
    for key, val in (("placements", [{"side": "Up", "result": "refused: unknown"}, {"side": "Down", "result": "live"}]),
                     ("placements", []), ("read_live", dict(rt["read_live"], matched="1")),
                     ("cancel", {"canceled": False, "not_canceled": 1}), ("read_after", {"status": "LIVE"}),
                     ("open_after", 1), ("wallet_open_after", 1), ("balance_after", 9950000)):
        ok(not rt_reading(dict(rt, **{key: val}))[0], "G-RT fails on %s alone" % key)
    ok(rt_reading(dict(rt, read_after={"status": "CANCELED_MARKET_RESOLVED", "matched": "0"}))[0],
       "G-RT: a cancellation's family of statuses")
    txt = report_text(rt, {"valid_until": 1810000000})
    ok(withheld(txt) and "Down" in txt and "отменён за 60 мс" in txt and "10.000000 pUSD" in txt,
       "the report: what happened, no address or id")
    ok(units(1234567) == "1.234567" and units(None) == "—", "pUSD from units")
    # -- the hook
    MODE[0] = "selftest"
    for mode, event, args, allowed in (
            ("selftest", "socket.getaddrinfo", ("example.com", 443, socket.AF_INET), False),
            ("geoblock", "socket.getaddrinfo", (GEO_HOST, 443, socket.AF_INET), True),
            ("geoblock", "socket.getaddrinfo", (GEO_HOST, 443, socket.AF_UNSPEC), False),
            ("authorize", "socket.getaddrinfo", (RELAYER_HOST.encode(), 443, socket.AF_INET), True),
            ("authorize", "socket.getaddrinfo", (GAMMA_HOST, 443, socket.AF_INET), False),
            ("approve", "socket.getaddrinfo", (RPC_HOST, 443, socket.AF_INET), True),
            ("approve", "socket.getaddrinfo", (CLOB_HOST, 443, socket.AF_INET), False),
            ("approve", "open", (RELAYER_FILE, "r", 0), True), ("approve", "open", (SESSION_KEY_FILE, "r", 0), False),
            ("approve", "os.rename", (ACCOUNT_FILE + ".tmp", ACCOUNT_FILE), True),
            ("approve", "open", ("/dev/tty", "r+", None), True),
            ("roundtrip", "socket.getaddrinfo", (GAMMA_HOST, 443, socket.AF_INET), True),
            ("roundtrip", "socket.getaddrinfo", (RPC_HOST, 443, socket.AF_INET), True),
            ("roundtrip", "socket.getaddrinfo", ("data-api.polymarket.com", 443, socket.AF_INET), False),
            ("roundtrip", "socket.__new__", (None, socket.AF_UNIX, 1, 0), True),
            ("geoblock", "socket.__new__", (None, socket.AF_UNIX, 1, 0), False),
            ("roundtrip", "socket.__new__", (None, socket.AF_INET6, 1, 0), False),
            ("roundtrip", "socket.connect", (None, ("192.0.2.9", 443)), False),
            ("secrets", "open", ("/dev/tty", "r+", None), True), ("ready", "open", ("/dev/tty", "r+", None), False),
            ("ready", "open", (SESSION_KEY_FILE, "r", 0), True), ("ready", "open", (RELAYER_FILE, "r", 0), False),
            ("host", "open", (TG_TOKEN_FILE, "r", 0), False), ("tg-report", "open", (CHAT_FILE, "r", 0), True),
            ("key", "open", (SESSION_KEY_FILE, None, os.O_WRONLY | os.O_CREAT | os.O_EXCL), True),
            ("key", "open", (SESSION_KEY_FILE, None, os.O_WRONLY | os.O_CREAT), False),
            ("secrets", "open", (SESSION_KEY_FILE, None, os.O_WRONLY | os.O_CREAT | os.O_EXCL), False),
            ("bosskey", "open", (AUTHORIZED_KEYS, "a", None), True),
            ("bosskey", "open", (AUTHORIZED_KEYS, "w", None), False),
            ("host", "open", (AUTHORIZED_KEYS, "a", None), False),
            ("roundtrip", "open", (L1_VAR + "/tz50-roundtrip-2.json", None, os.O_WRONLY | os.O_CREAT | os.O_EXCL), True),
            ("roundtrip", "open", (L1_VAR + "/tz50-roundtrip-4.json", None, os.O_WRONLY | os.O_CREAT | os.O_EXCL), False),
            ("authorize", "open", (L1_VAR + "/tz50-roundtrip-1.json", None, os.O_WRONLY | os.O_CREAT | os.O_EXCL), False),
            ("authorize", "os.rename", (ACCOUNT_FILE + ".tmp", ACCOUNT_FILE), True),
            ("ready", "os.rename", (ACCOUNT_FILE + ".tmp", ACCOUNT_FILE), False),
            ("secrets", "os.mkdir", (L1_ETC, 0o700), True), ("ready", "os.mkdir", (L1_ETC, 0o700), False),
            ("wheels", "open", (WHEELS + "/a.whl", "wb", None), True), ("wheels", "open", ("/root/x", "wb", None), False),
            ("reclaim", "open", (FORENSICS + "/x", "xb", None), True), ("selftest", "open", (FORENSICS + "/x", "xb", None),
                                                                        False),
            ("host", "open", ("/var/lib/adv3-bot/journal.jsonl", "r", 0), False),
            ("host", "subprocess.Popen", ("timedatectl", ["timedatectl"]), True),
            ("secrets", "subprocess.Popen", ("bash", ["bash"]), False)):
        got = policy(mode, event, args) is None
        ok(got == allowed, "the hook in %s: %s %s %s" % (mode, event, str(args[:2])[:70],
                                                         "allowed" if allowed else "refused"))
    ok(refused(lambda: socket.socket(socket.AF_INET6, socket.SOCK_STREAM)), "the hook refuses an AF_INET6 socket, live")
    ok(refused(lambda: socket.getaddrinfo("localhost", 80)), "the hook refuses a lookup in no family, live")
    ok(refused(lambda: open(TG_TOKEN_FILE, "r")), "the hook refuses a read of the bot's token in this mode, live")
    ok(refused(lambda: open("/root/tz50-selftest-outside", "w")), "the hook refuses a write outside the work tree, live")
    ok(refused(lambda: subprocess.run(["true"])), "the hook refuses a command this mode does not name, live")
    # -- files under the temporary tree
    tok, rel, acc = TMP + "/etc/telegram-token", TMP + "/etc/relayer-key", TMP + "/var/account.json"
    tty = FakeTty(["123:bad", "123456789:" + "B" * 35, "019a2b3c-4d5e-6f70-8192-a3b4c5d6e7f8", "0x12",
                   "0x" + "Ab" * 20])
    ok(mode_secrets(tty, tok, rel, acc) == 0 and private_file_ok(tok) and private_file_ok(rel) and
       json_of(open(acc, "rb").read()) == {"owner": "0x" + "ab" * 20} and oct(os.stat(TMP + "/etc").st_mode & 0o7777)
       == "0o700", "secrets: the token, the relayer key and its owner written 0600, refused inputs asked again")
    ok(mode_secrets(FakeTty([]), tok, rel, acc) == 0, "secrets again: every item kept, nothing asked")
    try:
        write_private(tok, b"x")
        ok(False, "an exclusive create over an existing file")
    except FileExistsError:
        ok(True, "write_private refuses an existing file")
    ak = TMP + "/authorized_keys"
    with open(ak, "w") as fh:
        fh.write("ssh-ed25519 %s executor" % base64.b64encode(_ssh_str(b"ssh-ed25519") + _ssh_str(b"\x02" * 32)).decode())
    tty = FakeTty(["-----BEGIN OPENSSH PRIVATE KEY-----", ed])
    ok(mode_bosskey(tty, ak) == 0 and len(key_fingerprints(open(ak).read())) == 2 and
       open(ak).read().count("\n") == 2, "bosskey: a private key refused, the public one appended on its own line")
    ok(mode_bosskey(FakeTty([ed]), ak) == 0 and len(key_fingerprints(open(ak).read())) == 2, "bosskey: present, kept")
    ok(mode_bosskey(FakeTty([""]), ak) == 0, "bosskey: none given, skipped")
    # -- the network, against the loopback stand-in
    page = b"<!DOCTYPE html><p>tz50</p>\n"
    wheel_a, wheel_b = b"wheel-a" * 100, b"wheel-b" * 50
    tg_token = "123456789:" + "C" * 35
    calls = {"bad_wheel": 1}

    def h_geo(st, method, path, q, body, h):
        return 200, {"blocked": False, "country": "BG", "region": "22", "ip": "127.0.0.1"}

    def h_page(st, method, path, q, body, h):
        return (200, page) if path == "/l1-sign.html" else (404, {})

    def h_pypi(st, method, path, q, body, h):
        if path == "/b.whl" and calls["bad_wheel"]:
            calls["bad_wheel"] -= 1
            return 200, b"truncated"
        return (200, {"/a.whl": wheel_a, "/b.whl": wheel_b}[path]) if path in ("/a.whl", "/b.whl") else (404, b"")

    sent = []

    def h_tg(st, method, path, q, body, h):
        assert path.split("/")[-1] in ("getMe", "getMyCommands", "getUpdates", "sendMessage"), path
        m = path.split("/")[-1]
        if m == "getMe":
            return 200, {"ok": True, "result": {"is_bot": True, "username": "tz50_selftest_bot"}}
        if m == "getMyCommands":
            return 200, {"ok": True, "result": []}
        if m == "getUpdates":
            return 200, {"ok": True, "result": ups}
        sent.append(body)
        return 200, {"ok": True, "result": {"message_id": 77}}

    srv = fake_server({"api": h_geo, "btc-5m-twap": h_page, "pypi": h_pypi, "*": h_tg})
    base = ("http", "127.0.0.1", srv.server_address[1])
    ok(geo_read(base, sleep=lambda s: None) == "PASS", "G-GEO against the stand-in: PASS, the address its own")
    ok(page_read(base, path="/btc-5m-twap/l1-sign.html", want=(len(page), sha256_bytes(page)), sleep=lambda s: None)
       and not page_read(base, path="/btc-5m-twap/other.html", want=(len(page), sha256_bytes(page)),
                         sleep=lambda s: None, tries=3), "G-PAGE: the page's bytes, and another path refused")
    mini = (("a-1.0-py3-none-any.whl", len(wheel_a), sha256_bytes(wheel_a), "/pypi/a.whl"),
            ("b-2.0-py3-none-any.whl", len(wheel_b), sha256_bytes(wheel_b), "/pypi/b.whl"),
            (PIP_WHEEL, len(wheel_a), sha256_bytes(wheel_a), "/pypi/a.whl"))
    ok(fetch_wheels(base, TMP + "/wheels", mini, sleep=lambda s: None) and
       open(TMP + "/wheels/requirements.txt").read() == "a==1.0 --hash=sha256:%s\nb==2.0 --hash=sha256:%s\n" % (
           sha256_bytes(wheel_a), sha256_bytes(wheel_b)), "G-ENV wheels: 3 of 3, one refused once for its bytes")
    ok(fetch_wheels(base, TMP + "/wheels", mini, sleep=lambda s: None), "G-ENV wheels again: every one kept")
    gone = mini[:1] + (("c-3.0-py3-none-any.whl", 9, "0" * 64, "/pypi/c.whl"),) + mini[1:]
    ok(not fetch_wheels(base, TMP + "/wheels2", gone, sleep=lambda s: None) and sorted(os.listdir(TMP + "/wheels2")) ==
       ["a-1.0-py3-none-any.whl", "requirements.txt"], "G-ENV wheels: the first wheel not served whole ends the fetch")
    tg = Telegram(tg_token, base)
    ok(mode_tg_probe(tg) == 0, "G-TG getMe against the stand-in")
    chat = TMP + "/etc/chat-id"
    ok(mode_find_chat(tg, chat, wait_s=5) == 0 and open(chat).read() == "42\n" and private_file_ok(chat),
       "G-TG chat: one private /start, pinned 0600")
    ok(mode_find_chat(tg, chat, wait_s=5) == 0, "G-TG chat: pinned already, kept")
    ups.append({"update_id": 4, "message": {"text": "/start", "chat": {"id": 44, "type": "private"}}})
    ok(mode_find_chat(tg, TMP + "/etc/chat-id-2", wait_s=5) == 1, "G-TG chat: two private /start, FAIL")
    os.makedirs(TMP + "/var2", 0o700)
    with open(TMP + "/var2/tz50-roundtrip-1.json", "w") as fh:
        json.dump(rt, fh)
    with open(TMP + "/var2/account.json", "w") as fh:
        json.dump({"owner": "0x" + "ab" * 20, "valid_until": 1810000000}, fh)
    ok(mode_tg_report(tg, TMP + "/var2", TMP + "/var2/account.json", chat) == 0 and sent[-1]["chat_id"] == 42 and
       sent[-1]["text"] == report_text(rt, {"valid_until": 1810000000}), "G-TG report: sent to the pinned chat")
    agents = sorted({ua for _m, _p, ua in srv.st["seen"]})
    ok(agents == [UA], "every one of %d requests carried the agent %s" % (len(srv.st["seen"]), UA))
    srv.shutdown()
    floors("/", 1, mem_floor=1, read=lambda: 2, sleep=lambda s: None, statf=lambda d: (10, 5, 5))
    try:
        floors("/", 6, mem_floor=1, read=lambda: 2, sleep=lambda s: None, statf=lambda d: (10, 5, 5))
        ok(False, "a disk floor")
    except AssertionError:
        ok(True, "the floors: a disk under its floor BLOCKS")
    shutil.rmtree(TMP)
    ok(not os.path.exists(TMP), "the temporary tree removed")
    out("SELFTEST PASS: %d checks, %d passed; refused by the hook: %d, each a check's own" % (
        len(passed), len(passed), len(REFUSED)))
    return 0

# ---- main ---------------------------------------------------------------------------------------------------


def main(argv):
    if not argv:
        sys.exit("usage: %s MODE [ARG...]" % PYFILE)
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "number": mode_number, "refs": mode_refs, "room": mode_room,
             "geoblock": mode_geoblock, "sshd": mode_sshd, "page": mode_page, "wheels": mode_wheels,
             "secrets": mode_secrets, "bosskey": mode_bosskey, "tg-probe": mode_tg_probe, "find-chat": mode_find_chat,
             "tg-report": mode_tg_report, "env": mode_env, "key": mode_key, "ready": mode_ready,
             "roundtrip": mode_roundtrip, "authorize": lambda: mode_owner("authorize"),
             "approve": lambda: mode_owner("approve"), "revoke": lambda: mode_owner("revoke"),
             "selftest": mode_selftest, "sdk-selftest": mode_sdk_selftest}
    one = {"scratch": mode_scratch, "methods": mode_methods, "host": mode_host}
    rc = 1
    try:
        if mode == "reclaim":
            rc = mode_reclaim(rest)
        elif mode in one:
            assert len(rest) == 1, "%s takes one argument" % mode
            rc = one[mode](rest[0])
        else:
            assert mode in table and not rest, "unknown mode %r" % (argv,)
            rc = table[mode]()
    finally:    # printed on every exit, a BLOCK's and a failed assert's included
        out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
        out("refused by the hook: %d; lookups %d, requests %d" % (len(REFUSED), COUNTS["lookups"], COUNTS["requests"]))
    return rc or 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

## Appendix B — the signing page, byte for byte

### `docs/l1-sign.html`

```html file=docs/l1-sign.html
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<title>btc-5m-twap · L1 · подпись владельца</title>
<style>
body { font: 16px/1.45 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; background: #f6f7f9; color: #15171a; }
main { max-width: 640px; margin: 0 auto; padding: 16px; }
h1 { font-size: 20px; margin: 8px 0 12px; }
table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 8px; overflow: hidden; }
td { padding: 8px 10px; border-bottom: 1px solid #e6e8eb; vertical-align: top; word-break: break-all; }
td:first-child { width: 38%; color: #5a6270; word-break: normal; }
button { display: block; width: 100%; margin: 14px 0 8px; padding: 14px; font-size: 17px; border: 0; border-radius: 10px; background: #1652f0; color: #fff; }
button:disabled { background: #9aa6bd; }
textarea { width: 100%; box-sizing: border-box; font: 13px/1.4 ui-monospace, Menlo, monospace; padding: 8px; }
pre { white-space: pre-wrap; word-break: break-all; font-size: 12px; background: #fff; padding: 8px; border-radius: 8px; }
#msg { min-height: 1.4em; font-weight: 600; }
.bad { color: #b42318; }
.good { color: #067647; }
.small { font-size: 13px; color: #5a6270; }
</style>
</head>
<body>
<main>
<h1>Подпись владельца кошелька бота</h1>
<table id="sum"></table>
<button id="go" type="button" disabled>Подключить MetaMask и подписать</button>
<p id="msg" role="status"></p>
<div id="done" hidden>
<p>Подпись готова. Скопируйте её и вставьте в терминал на сервере, где ждёт запрос:</p>
<textarea id="sig" rows="4" readonly></textarea>
<button id="copy" type="button">Скопировать подпись</button>
</div>
<details><summary>Что именно подписывается</summary><pre id="td"></pre></details>
<p class="small">Страница ничего не отправляет в сеть и ничего не хранит: подпись остаётся на этом экране, пока вы её не скопируете. Ключ владельца не покидает MetaMask. Подпись делает только то, что написано в таблице выше, и никому не даёт права вывести средства из кошелька.</p>
</main>
<script>
"use strict";
// btc-5m-twap, TZ-50: the owner's signing page of L1. Served by GitHub Pages from main's docs/l1-sign.html, byte for
// byte from the TZ's appendix. It reads its fields from the URL fragment, which no request carries, builds one
// Deposit Wallet EIP-712 Batch - authorizeSessionSigner(key, validUntil) or revokeSessionSigner(key) called on the
// wallet itself, or approve(exchange, 1 pUSD) called on pUSD for one or both of the venue's two exchanges - asks
// MetaMask to sign it as the owner on Polygon, and shows the signature. It makes no network request of its own, and
// no field of a link can name another contract, another spender or another amount.

const CHAIN_ID = 137;
const SELECTOR = {authorize: "24017fae", revoke: "e63f952f", approve: "095ea7b3"};
const PUSD = "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB";
const EXCHANGE = {c: "0xE111180000d2663C0091e4f400237545B87B996B", v: "0xe3333700cA9d93003F00f0F71f8515005F6c00Aa"};
const EXCHANGE_NAME = {c: "Биржа для рынков CTF", v: "Биржа для рынков протокола V2"};
const APPROVE_UNITS = 1000000;
const ZERO = "0x0000000000000000000000000000000000000000";
const POLYGON = {chainId: "0x89", chainName: "Polygon", nativeCurrency: {name: "POL", symbol: "POL", decimals: 18},
                 rpcUrls: ["https://polygon-rpc.com"], blockExplorerUrls: ["https://polygonscan.com"]};
const FIELDS = {authorize: ["d", "k", "n", "o", "op", "u", "v", "w"], revoke: ["d", "k", "n", "o", "op", "v", "w"],
                approve: ["d", "n", "o", "op", "v", "w", "x"]};

function parseFragment(hash) {
  const h = hash.charAt(0) === "#" ? hash.slice(1) : hash;
  const p = Object.create(null);
  for (const part of h.split("&")) {
    if (part === "") continue;
    const i = part.indexOf("=");
    if (i < 1) throw new Error("fragment: a field without a name or a value");
    const k = part.slice(0, i), v = decodeURIComponent(part.slice(i + 1));
    if (Object.prototype.hasOwnProperty.call(p, k)) throw new Error("fragment: field " + k + " twice");
    p[k] = v;
  }
  if (p.v !== "1") throw new Error("fragment: version");
  if (!Object.prototype.hasOwnProperty.call(FIELDS, p.op)) throw new Error("fragment: operation");
  if (Object.keys(p).sort().join(",") !== FIELDS[p.op].join(",")) throw new Error("fragment: fields");
  const addresses = p.op === "approve" ? ["o", "w"] : ["o", "w", "k"];
  for (const a of addresses) {
    if (!/^0x[0-9a-fA-F]{40}$/.test(p[a])) throw new Error("fragment: address " + a);
    if (p[a].toLowerCase() === ZERO) throw new Error("fragment: the zero address");
  }
  if (p.op === "approve" && ["c", "v", "cv"].indexOf(p.x) < 0) throw new Error("fragment: exchanges");
  for (const n of (p.op === "authorize" ? ["u", "n", "d"] : ["n", "d"])) {
    if (!/^(0|[1-9][0-9]{0,29})$/.test(p[n])) throw new Error("fragment: number " + n);
  }
  return p;
}

function word(hex) {
  if (!/^[0-9a-f]{1,64}$/.test(hex)) throw new Error("word");
  return hex.padStart(64, "0");
}

function calls(p) {
  if (p.op === "approve") {
    return p.x.split("").map((x) => ({target: PUSD, value: "0", data: "0x" + SELECTOR.approve +
      word(EXCHANGE[x].slice(2).toLowerCase()) + word(APPROVE_UNITS.toString(16))}));
  }
  const key = word(p.k.slice(2).toLowerCase());
  const data = p.op === "authorize" ? "0x" + SELECTOR.authorize + key + word(BigInt(p.u).toString(16))
    : "0x" + SELECTOR.revoke + key;
  return [{target: p.w, value: "0", data: data}];
}

function typedData(p) {
  return {
    types: {
      EIP712Domain: [{name: "name", type: "string"}, {name: "version", type: "string"},
                     {name: "chainId", type: "uint256"}, {name: "verifyingContract", type: "address"}],
      Batch: [{name: "wallet", type: "address"}, {name: "nonce", type: "uint256"},
              {name: "deadline", type: "uint256"}, {name: "calls", type: "Call[]"}],
      Call: [{name: "target", type: "address"}, {name: "value", type: "uint256"}, {name: "data", type: "bytes"}]
    },
    primaryType: "Batch",
    domain: {name: "DepositWallet", version: "1", chainId: CHAIN_ID, verifyingContract: p.w},
    message: {wallet: p.w, nonce: p.n, deadline: p.d, calls: calls(p)}
  };
}

function utc(sec) {
  return new Date(Number(sec) * 1000).toISOString().replace("T", " ").slice(0, 19) + " UTC";
}

function boot() {
  const $ = (id) => document.getElementById(id);
  const say = (text, cls) => { $("msg").textContent = text; $("msg").className = cls || ""; };
  let p;
  try {
    p = parseFragment(window.location.hash);
  } catch (e) {
    say("Ссылка неполная или повреждена (" + e.message + "). Откройте её заново из терминала.", "bad");
    return;
  }
  const what = {
    authorize: "разрешить сессионный ключ: только ордера CLOB, без вывода средств, на 180 дней",
    revoke: "отозвать сессионный ключ: его ордера отменяются, торговать он больше не может",
    approve: p.op === "approve" && p.x.length === 2
      ? "разрешить двум биржам Polymarket списывать pUSD кошелька бота для исполнения его ордеров — каждой не больше 1 pUSD"
      : "разрешить бирже Polymarket списывать pUSD кошелька бота для исполнения его ордеров — не больше 1 pUSD"
  };
  const rows = [["Операция", what[p.op]], ["Кошелёк бота (Deposit Wallet)", p.w], ["Владелец — подписывает он", p.o]];
  if (p.op === "approve") {
    for (const x of p.x.split("")) rows.push([EXCHANGE_NAME[x], EXCHANGE[x] + " — до 1 pUSD"]);
    rows.push(["Токен", "pUSD " + PUSD]);
  } else {
    rows.push(["Сессионный ключ", p.k]);
  }
  if (p.op === "authorize") rows.push(["Ключ действует до", utc(p.u)]);
  rows.push(["Подпись годна до", utc(p.d)]);
  for (const [a, b] of rows) {
    const tr = document.createElement("tr");
    const td1 = document.createElement("td"), td2 = document.createElement("td");
    td1.textContent = a;
    td2.textContent = b;
    tr.appendChild(td1);
    tr.appendChild(td2);
    $("sum").appendChild(tr);
  }
  $("td").textContent = JSON.stringify(typedData(p), null, 2);
  const left = Number(p.d) - Math.floor(Date.now() / 1000);
  if (left < 15) {
    say("Срок этой ссылки истёк. Запустите в терминале ту же команду ещё раз — она покажет новую ссылку.", "bad");
    return;
  }
  say("Ссылка действует ещё " + Math.floor(left / 60) + " мин " + (left % 60) + " с.", "");
  $("go").disabled = false;
  $("go").addEventListener("click", async () => {
    $("go").disabled = true;
    try {
      const eth = window.ethereum;
      if (!eth || typeof eth.request !== "function") {
        throw new Error("MetaMask не найден. Откройте эту ссылку во встроенном браузере MetaMask " +
                        "или в браузере, где установлен MetaMask.");
      }
      const accounts = await eth.request({method: "eth_requestAccounts"});
      const account = accounts && accounts[0];
      if (!account || account.toLowerCase() !== p.o.toLowerCase()) {
        throw new Error("В MetaMask выбран другой аккаунт. Выберите аккаунт владельца " + p.o +
                        " (кошелёк бота) и нажмите кнопку снова.");
      }
      const chain = await eth.request({method: "eth_chainId"});
      if (parseInt(chain, 16) !== CHAIN_ID) {
        try {
          await eth.request({method: "wallet_switchEthereumChain", params: [{chainId: POLYGON.chainId}]});
        } catch (e) {
          if (e && e.code === 4902) {
            await eth.request({method: "wallet_addEthereumChain", params: [POLYGON]});
          } else {
            throw e;
          }
        }
      }
      if (Number(p.d) - Math.floor(Date.now() / 1000) < 15) throw new Error("Срок ссылки истёк — получите новую.");
      say("Проверьте запрос в MetaMask и подпишите его.", "");
      const sig = await eth.request({method: "eth_signTypedData_v4", params: [account, JSON.stringify(typedData(p))]});
      if (typeof sig !== "string" || !/^0x[0-9a-fA-F]{130}$/.test(sig)) throw new Error("MetaMask вернул не подпись.");
      $("sig").value = sig;
      $("done").hidden = false;
      say("Готово. Скопируйте подпись и вставьте её в терминал.", "good");
    } catch (e) {
      say((e && e.message) ? e.message : String(e), "bad");
      $("go").disabled = false;
    }
  });
  $("copy").addEventListener("click", async () => {
    const t = $("sig");
    try {
      await navigator.clipboard.writeText(t.value);
    } catch (e) {
      t.focus();
      t.select();
      document.execCommand("copy");
    }
    say("Подпись скопирована.", "good");
  });
}

if (typeof document !== "undefined") boot();
</script>
</body>
</html>
```
