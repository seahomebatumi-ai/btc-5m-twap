# TZ-18a — the chain book capture, redeployed

**Canonical filename: `TZ-18a-chainbook-capture-redeploy.md`.** The Executor names the committed file
from this line, in `CryptoTZ/`, never from the name it received.

| field | value |
|---|---|
| corrects | TZ-18, whose build sent Python's default `User-Agent` and was refused at every request (map §7 item 77). TZ-18 and its report are immutable and stand; nothing of TZ-18 is re-run |
| map revision required | `2026-09-23-a` |
| anchors required | `A1` `229a944f2d51` · `A2` `6c5089330629` · `A3` `0-complete / 1-student-5tau-not-disqualified / 2-undecidable-5tau` · `A4` `437b45ea196b` · `A5` `9fd1c7de0f74` · `A6` `729f0bcdbee3` |
| fingerprint rows | all 25 hashed rows of the map's §0 table; the 23 in state `frozen` asserted equal |
| Executor model | **Opus** — network capture, a long-lived process and its stop, clock discipline |
| branch | `tz-18a-chainbook-capture` |
| file added | `research/tz18a-chainbook-capture.py` — the only path this TZ writes in the repository besides its report |
| derived from | `research/tz18-chainbook-capture.py` at `8caa0b41d5cdf9e74e92b11d4317d59a2ee7b567`, PR #18's head, served as `refs/pull/18/head`, SHA-256 `33753b2bb1e322a081e6cba8bad976268e2d6046dc350e6ceae3e748ad6e4bfe` — byte for byte except §3.3's changes |
| report | `CryptoReports/TZ-18a-chainbook-capture-redeploy-report.md`, pushed to `main` |
| pricer | **not read, not called, not scored.** `A6` is stated so that what was not scored is not in doubt |

A mismatch on the revision string, on any anchor, on any `frozen` row or on any condition of §0 is
**BLOCKED before any work**, with every read printed.

---

## 0. Preflight

### 0.1 Fingerprint

Print `wc -l`, byte count and `sha256sum` for every path in the map's §0 fingerprint table and for
`SYSTEM-MAP.md` itself. Assert the 23 `frozen` rows equal. Re-derive `A2`, `A4`, `A5` and `A6` as the
first 12 hex characters of each file's SHA-256 rather than copying the table.

### 0.2 Host gate

From `/root/btc-5m-twap`, output verbatim into the report:

```
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'; echo "exit=$?"
grep -rl --include=runtime.jsonl 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder | head -n 1
du -sb /root/PROJECT_GAMING_PS5
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
for d in /root/tz15-work /root/tz17-work /root/tz18-work /root/tz18-svc /root/tz18a-work /root/tz18a-svc; do test -e "$d"; echo "$d exit=$?"; done
find /root/btc-forensics -type f | wc -l
git worktree list
```

- **H1** — `find` prints exactly one path.
- **H2** — `pgrep -fx` prints exactly one line and `exit=0`. `-fx` matches the whole command line, so the
  shell evaluating this block, which carries the pattern as a substring, cannot match it.
- **H3** — `df` names source `/dev/vda2` and size `31612203008`. With H1 and the `grep` line's one path,
  these are the map §6 host-identity row.
- **Resource gate** — `avail` ≥ **`2,200,000,000`** bytes: the map §6 floor `2,000,000,000` plus the
  per-process write cap `200,000,000` (§3.7). Asserted again inside the instrument at every run and at
  every window.
- **Trees** — `/root/tz17-work` and `/root/tz18-work` exit `0`; `/root/tz18a-work` and `/root/tz18a-svc`
  exit `1`. `/root/tz15-work` and `/root/tz18-svc` are printed: the first is TZ-16's, the second §9 reclaims
  if present.
- **Forensic store** — exactly `211` files: map §3's count at TZ-15's end; TZ-17 §9 copies nothing into it and
  TZ-18 §2 writes only under its three roots.
- `du`, both `systemctl` reads and `git worktree list` are printed and carry no threshold. Map §3 counts
  seven worktrees at TZ-18's end.

### 0.3 Repository reads

```
git fetch origin
git fetch origin refs/pull/18/head
git ls-tree -r --name-only origin/main | grep -c '^CryptoReports/TZ-18-chainbook-capture-deploy-report.md$'
git ls-tree -r --name-only origin/main | grep -c '^research/tz18a-chainbook-capture.py$'
git ls-tree -r --name-only origin/main | grep -c '^research/tz18-chainbook-capture.py$'
git ls-remote origin refs/heads/tz-18a-chainbook-capture | wc -l
git show 8caa0b41d5cdf9e74e92b11d4317d59a2ee7b567:research/tz18-chainbook-capture.py | sha256sum
git show origin/main:CryptoTZ/TZ-18a-chainbook-capture-redeploy.md | sha256sum
```

- The TZ-18 report count must be `1`; the `tz18a` path count `0`; the `ls-remote` count `0`, the branch not
  yet existing; **the base blob's** hash `33753b2bb1e322a081e6cba8bad976268e2d6046dc350e6ceae3e748ad6e4bfe`. Any other
  value is **BLOCKED**.
- The `tz18` path count is printed with no threshold; `0` means PR #18 is still unmerged, as map §1 records.
- This TZ's own hash is printed; the Architect compares it with the file he delivered.

### 0.4 The TZ-18 service — stopped, and verified from its own record

Map §2.5 records that its stop was handed to the Boss on 2026-09-23. This section verifies it from the
service's own record and from `/proc`, never from his account:

```
pgrep -fx '/root/tz01-env/venv/bin/python -B -u /root/tz18-svc/tz18-chainbook-capture.py --serve'; echo "exit=$?"
test -e /proc/2608993; echo "proc exit=$?"
```

— the second read printed; K0 decides — and, from `/var/lib/btc-chainbook/runtime.jsonl` — counts, times and ids only, the map §2.5 exception —
every record's `event`, `pid` and `wall_ns` in UTC, with `commit` and `file_sha256` for each `start`.

- **K0** — `pgrep` prints no line and `exit=1`.
- **K1** — exactly one `start` record carries pid `2608993`, with `wall_ns` `1790117616052072857`, commit
  `8caa0b41d5cdf9e74e92b11d4317d59a2ee7b567` and `file_sha256` equal to the base blob's hash of §0.3 (TZ-18
  report §2.1 and §2.7). Otherwise **BLOCKED**.
- **K2** — a `stop` record carries pid `2608993` and a `wall_ns` later than that start's. Its instant is
  **`K_stop`**.

**If K0 fails**, the service still runs: its stop is authorized here, once, by block K-18, and verified as
§6.1 says; then K0 and K2 are read again. **If K0 holds and K2 finds no `stop` record**, the process ended
without writing one — a signal it cannot catch, or the host's own action. The absence is printed, nothing
blocks on it, and `K_stop` is the instant of the K0 read.

Also printed, by directory name only and opening nothing inside: the count of window directories under
`/var/lib/btc-chainbook/`, the smallest and the largest.

### 0.5 The diagnostic slug

Map §7 item 77: the TZ-18 Executor broke that TZ's P2 with requests outside the instrument, among them a
live settled fifteen-minute document of `5,462` bytes whose slug its report does not name. List every
regular file under `/root/tz18-work/` not beneath `/root/tz18-work/wt/` or `/root/tz18-work/wt-report/`,
sorted by path, with its bytes and SHA-256. Each whose name ends in `.py` or `.sh` is printed in full in the
report's Appendix A; no other file's content is read except to hash it. From those scripts the report names
every slug and every token id they requested — quoted where the script holds it as a literal, or as the
expression that produced it — and each fifteen-minute slug's `T` in UTC. If no script is found, the report
says so; that is a disclosure, not a block.

### 0.6 Trees and interpreter

Two worktrees from `origin/main`: `/root/tz18a-work/wt` on branch `tz-18a-chainbook-capture`, and
`/root/tz18a-work/wt-report` detached, from which the report is pushed. Then `sha256sum` of every file under
`/root/btc-forensics/` into `/root/tz18a-work/forensics-before.sha256`, `211` lines. Interpreter
`/root/tz01-env/venv/bin/python`, Python 3.12.3 (map §6), for every run. Neither `/root/tz01-env/` nor
`/root/tz04a-env/` is touched.

---

## 1. Why

TZ-18's `http_get` built `urllib.request.Request(url, method="GET")` (8caa0b4 line 434) and so sent Python's
default agent. Both venue hosts answered `403`, `error code: 1010`, to every request; no document yielded
token ids and no book was stored. G-DEPLOY read FAIL on that artifact; G-TIERC read PASS under two refused
requests per 900 s, a load that never tested it; G-CHAIN stands, re-derived by the Architect from the
venue's bytes (map §2.5, §4, §5 B1). This TZ redeploys the capture with the request fixed and proved on
the host before the service starts, re-reads G-DEPLOY and G-TIERC under the load the capture actually
applies, and carries every item map §7 item 77 assigns it. It also corrects two faults of TZ-18's design:

1. **TZ-18 §3.3 said the two captures never request in the same second; at the document instant they
   do.** The recorder fetches the five-minute market's document, S6, at `T0 + 5` —
   `research/recorder/recorder.py` line 32, `S6_FETCH_OFFSET_S = 5`, and line 379 — which for
   `T0 = T + 600` is `T + 605`, TZ-18's instant for the same document. The document instant moves to
   **`T + 625`**: 20 s after S6's first attempt, 30 s before the first checkpoint.
2. **TZ-18's V10 asserted concurrency at the end of `--prove`, after the service had started, and said
   nothing of what a failure would do.** Here it is a disclosed count. When each book was observed is the
   receive skew, which G-DEPLOY bounds.

Nothing here measures a price. The scoring step, B2, is written only after TZ-16's first reading is on
`main` (map §5).

---

## 2. Scope, and what is prohibited

**Built:** exactly one repository file, `research/tz18a-chainbook-capture.py`, on the branch; and the report.

**Host paths written:** `/root/tz18a-work/**`; `/root/tz18a-svc/**`; `/var/lib/btc-chainbook/**` — new
window directories, appended `runtime.jsonl` records, `service.pid`, appended `service.log`;
`/root/btc-5m-twap/.git`, by the fetches, the branch and the worktree registrations; and
`/root/btc-forensics/`, by exclusive create only (§9).

**Host paths removed, and nothing else:** `/root/tz17-work`, `/root/tz18-work` and `/root/tz18-svc`, their
four worktrees and the untracked `__pycache__` directories in those (§9); and the stale
`/var/lib/btc-chainbook/service.pid`, which the service replaces (§3.3 D8).

Prohibited, each an abort rather than a warning:

- **P1 — under `/var/lib/btc-recorder/` only `manifest.json` is opened, by `--prestart` (§3.4) and
  `--prove` (§3.6).** Map §2.3's reserve excepts it because the committed loader reads every manifest for
  every set formation and a manifest carries neither a price nor an outcome. Two named exemptions: §0.2's
  `grep` over `runtime.jsonl` files, the map §6 host-identity read, whose records carry neither; and R3's
  `test -e`. Directory listings, `stat` and `statvfs` open no file.
- **P2 — no settled market document is requested or read, live or stored.** The only documents requested
  are of markets open at the instant of the request (§3.4, §3.5). **Named exemptions:** whatever §9 copies into
  `/root/btc-forensics/` — TZ-17's `801` stored bodies, its CSV and summary, TZ-18's `tz18-verify.csv` and
  other outputs, and every file §0.5 lists — is hashed and copied byte for byte, never parsed, and printed
  only where §0.5 prints a script; §9 steps 1 and 2 read committed reports for hexadecimal tokens and take,
  from TZ-17's committed CSV, the five `sha_*` columns alone. Every reading TZ-17's and TZ-18's files carry lies
  below the reserved boundary `1789669800`.
- **P3 — no price, size, spread, mid, book level or outcome is printed, written to an output file of §8 or
  computed outside the byte-for-byte store.** From a reply the instrument takes its status, byte count,
  SHA-256, times and whether its body parses as JSON; from a market document, also exactly `clobTokenIds`,
  `outcomes` — the two outcome labels, not a resolution — and `conditionId`: TZ-18 §3.3's design, which map
  §2.5 records in `window.json`'s exception. **Named exemption:** the store under `/var/lib/btc-chainbook/`
  keeps what it received verbatim, the reserved five-minute books among it, reserved there on map §2.3's and
  §2.5's terms; and P2's named exemptions, which copy or read such files without taking a value from one.
- **P4 — no order, no authentication, no credential, no CLOB key, no wallet.** The two GET endpoints of
  §3.2, and `127.0.0.1` inside `--selftest` only.
- **P5 — no request to a venue host from anything but the instrument's `--prestart` and `--serve`:** no
  `curl`, no probe script, no diagnosis. A failure this TZ does not provide for is a BLOCKED report, never a
  request (map §7 item 77).
- **P6 — no process is signalled but two, each only by its named block of §6.1:** TZ-18's service under §0.4
  and this TZ's under R5. The recorder is never signalled, reniced or touched.
- **P7 — no committed file is edited**, and no function of any committed file is imported or called; the
  instrument is standard-library only.
- **P8 — no live request and no gated statistic before the branch commit is pushed** (map §7 items 54 and
  77). `--selftest` smoke runs before the push are permitted and disclosed: they read no capture and reach
  `127.0.0.1` alone.

---

## 3. What to build

### 3.1 Derivation

```
git show 8caa0b41d5cdf9e74e92b11d4317d59a2ee7b567:research/tz18-chainbook-capture.py > research/tz18a-chainbook-capture.py
```

Assert its SHA-256 is **the base blob's**, §0.3's `33753b2b…`, before the first edit (V3). Apply §3.3's D1–D16 and nothing
else: the schedule, `run_window`, `fetch_books`, the verbatim store of TZ-18 §3.5, gzip at `mtime=0` and
level `6`, the write and open guards, `fingerprint_gate` and `token_ids_of` stay byte for byte. The report
maps every hunk of `diff -u` between the two files to one D-item (V4).

### 3.2 The request, every header fixed

The two endpoints are TZ-18 §3.2's and no others:

| use | request |
|---|---|
| market document | `GET https://gamma-api.polymarket.com/markets/slug/{slug}` |
| order book | `GET https://clob.polymarket.com/book?token_id={token_id}` |

One function builds every request, `build_request(url)`, returning
`urllib.request.Request(url, method="GET", headers={"Accept": "application/json", "User-Agent": "btc-5m-twap-tz18a"})`,
and `http_get` sends it through `urllib.request.urlopen(req, timeout=5.0)`. Under Python 3.12.3 the request
line is `GET <path-and-query> HTTP/1.1` and the header block is exactly these five fields, none repeated:

| field | value | added by |
|---|---|---|
| `Accept-Encoding` | `identity` | `http.client` |
| `Host` | `gamma-api.polymarket.com` or `clob.polymarket.com` | `urllib` |
| `Accept` | `application/json` | this instrument |
| `User-Agent` | `btc-5m-twap-tz18a` | this instrument |
| `Connection` | `close` | `urllib` |

S3 asserts that block on a loopback listener (§5). **Evidence, with the whole request** (map §7 item 75):
on 2026-09-23, from a second host under Python 3.12.3 with no proxy, this request — `GET`, those five
fields — was answered `200` by `gamma-api.polymarket.com` for `/markets/slug/btc-updown-15m-1788998400`,
`5,098` bytes of SHA-256 `160aca8c96b078e4d8a91506d80a8a19998fe7ca41e542895eb98bfdd66e69ca`, TZ-17's
`sha_M15` for that window; and `404`, `No orderbook exists for the requested token id`, `59` bytes, by
`clob.polymarket.com` for that market's first token — a settled market's reply, not a refusal. The same
document under the default agent answered `403`, `error code: 1010`. Both reads lie below the reserved
boundary. **The binding proof is the capture host's own:** `--prestart`, before the service starts (§3.4;
CANON hard rule 14).

### 3.3 The changes, D1 to D16

Line numbers are the base blob's, read from `refs/pull/18/head`.

| D | 8caa0b4 lines | change |
|---|---|---|
| **D1** | 2–16, the module docstring | names TZ-18a and its four modes; carries no URL |
| **D2** | 19–36, imports | add `import http.server`; remove line 35, `from decimal import Decimal`, whose only users D6 removes |
| **D3** | 55, 70, 71, 76, 77 | `MAP_REVISION = "2026-09-23-a"`, `FINGERPRINT_ROWS_EXPECTED = 25`, `FINGERPRINT_FROZEN_EXPECTED = 23`, `WORK_ROOT = "/root/tz18a-work"`, `SVC_ROOT = "/root/tz18a-svc"` |
| **D4** | 85 | `DOC_OFFSET = 625` (§1 item 1). `schedule_for` and `next_window` read it, and `qualifies` receives the instant `schedule_for` computes; none of the three is edited |
| **D5** | new constants | `ACCEPT = "application/json"`; `USER_AGENT = "btc-5m-twap-tz18a"`; `SERVICE_ARGV` and `OLD_SERVICE_ARGV`, the five strings of §3.5's command line and of TZ-18's; `REQUESTS_PER_WINDOW = 30`; `TIERC_MIN_FULL = 2`; `CLOSE_MARGIN_S = 5`; `BASE_RATE_S = 604800`; `FA_UNITS = 5`; `PRESTART_JSON_KEYS` (§3.4) |
| **D6** | 75, 98–115, 117, 122–125, 143–145, 360–363, 785–979 | remove `TZ17_RAW`; the TZ-17 CSV and identity constants; the four G-CHAIN rows of `POWER_LITERALS`, whose comment then counts three; `VERIFY_JSON_KEYS`; `read_g_chain`; and the `--verify-tz17` section whole — `extract_csv`, `meta_of`, `compare`, `mode_verify`. G-CHAIN stands (map §4) and §9 reclaims its input |
| **D7** | 426–463, `http_get` | the request from `build_request` (new, §3.2); `recv_mono_ns` and `recv_wall_ns` stamped only when a status was obtained, `None` otherwise — line 457 returned the same value on both branches (map §7 item 77); the docstring names the five fields |
| **D8** | 518–549, `acquire_single_instance` | new pure function `same_service(cmdline_bytes, argv)`: true iff the bytes, split on NUL with the one trailing empty field dropped and each field decoded as UTF-8, equal `argv` element for element. The pid file's pid is read; if `same_service` of its `/proc/{pid}/cmdline` holds with `SERVICE_ARGV` or with `OLD_SERVICE_ARGV`, return `None`, printing which; otherwise the file is stale and is replaced. Line 539's substring test is gone (map §7 item 76) |
| **D9** | 561–571, `runtime_record`'s `config` | gains `"headers": [["Accept", ACCEPT], ["User-Agent", USER_AGENT]]` and `"service_argv": list(SERVICE_ARGV)`; nothing else in the record changes |
| **D10** | 757–782, `mode_serve` | first: read `/proc/self/cmdline`; unless `same_service(it, SERVICE_ARGV)`, print it and return `2` having written nothing. A `None` from `acquire_single_instance` returns `3` |
| **D11** | 997–1024, `load_windows` | takes `s` and `A`; opens a window directory only where new pure function `considered(T, s, A)` holds — `T + DOC_OFFSET >= s` and `T + CLOSE_OFFSET + CLOSE_MARGIN_S <= A` |
| **D12** | 1037–1067, `manifest_scan` | takes `A`; a `manifest.json` counts only if it exists with `st_mtime_ns <= A * 10**9`; one that does not is reported `no_manifest_by_as_of` |
| **D13** | 138–142 and 1070–1236, `PROOF_JSON_KEYS` and `mode_prove` | §3.6: `--as-of` replaces the wall clock; G-DEPLOY's code unchanged; G-TIERC through new pure functions `issued_of` and `read_g_tierc` (§4); the G-CHAIN block and its read of `run-1/tz18-verify.json` removed; `"generated_wall_ns"` replaced by `"as_of"`; the terminal `assert n_conc_bad == 0` removed and the count kept (V10) |
| **D14** | new, `mode_prestart` | §3.4, with new pure functions `base_rate` and `p_false_alarm` |
| **D15** | 1239–1385, `mode_selftest` | §5's S1–S10, and no other item |
| **D16** | 1388–1420, `main` | modes `--selftest`, `--prestart`, `--serve`, `--prove`; arguments `--out`, `--repo`, `--as-of`; `--verify-tz17` and `--verify-json` removed |

### 3.4 `--prestart` — the request path, proved on the host before the service starts

Run once, as R1, from the copy of §3.5, with `--repo /root/tz18a-work/wt --out /root/tz18a-work/run-1`:

1. `guard_resources()`; `fingerprint_gate` on `--repo`; the SHA-256 of its own file printed.
2. **Processes.** Every `/proc/{pid}/cmdline` is read — a pid that vanishes mid-scan is skipped and
   counted — and the pids for which `same_service` holds with `SERVICE_ARGV`, and with `OLD_SERVICE_ARGV`,
   are counted. **Both counts must be `0`.**
3. **The base rate.** `p = int(time.time()) // 300 * 300`. For the `2,016` slots `T0 = p − 605,100, …,
   p − 600`, in steps of `300` — the five-minute intervals closing in `[p − 604,800, p)` — open
   `/var/lib/btc-recorder/btc-updown-5m/{T0}/manifest.json` where it exists. Count the directories present,
   the manifests read, `m`, and those whose `quotes_complete` is not JSON `true`, `f`. Print
   `p_false_alarm(f, m, 5) = 1 − (1 − f/m)^5`, exactly, as a fraction and to ten decimals, or `None` when
   `m = 0`. **This is G-TIERC's false-failure probability (§4), stated before any interval it judges
   exists.** Fail-fast: the scan aborts if its first `100` opens take more than `30` s (§10 C4).
4. **The live window.** `T* = int(time.time()) // 900 * 900`. If `now − T*` is below `30`, sleep until
   `T* + 30`; if above `840`, sleep until `T* + 930` and take `T* + 900` — at most `90` s either way. That
   fifteen-minute market is open, so its document is not settled.
5. **Request 1** — `http_get(GAMMA_MARKET_URL.format(slug="btc-updown-15m-%d" % T*))`. Assert status `200`,
   bytes `> 0`, the body parses as JSON, and `token_ids_of` returns two distinct non-empty ids.
6. **Request 2** — `http_get(CLOB_BOOK_URL.format(token_id=<the first of those ids>))`. Assert status
   `200`, bytes `> 0`, and the body parses as JSON. Nothing else is read from it.
7. Assert the request counter is `2`. Write `tz18a-prestart.json`, keys exactly `PRESTART_JSON_KEYS` =
   `mode`, `p_wall`, `file_sha256`, `fingerprint`, `processes`, `base_rate`, `requests`, `counters`. Each
   request entry carries `method`, `url`, `headers` — the two `build_request` sets — `status`, `bytes`,
   `sha256`, `parses_json`, `recv_wall_ns`, `elapsed_ns`, and, for request 1, the two token ids. No body is
   stored or printed. Print `READING P-START: served`.

A failed assert in steps 1–7 is **BLOCKED**, and the service is never started.

### 3.5 The service

```
mkdir -p /root/tz18a-svc
git -C /root/tz18a-work/wt show origin/tz-18a-chainbook-capture:research/tz18a-chainbook-capture.py > /root/tz18a-svc/tz18a-chainbook-capture.py
git -C /root/tz18a-work/wt rev-parse origin/tz-18a-chainbook-capture > /root/tz18a-svc/commit.txt
```

Assert the copy's SHA-256 equals **the branch blob's** — `git show origin/tz-18a-chainbook-capture:research/tz18a-chainbook-capture.py | sha256sum` —
and that `commit.txt` is 40 lowercase hex characters and a newline, which `read_commit` strips. Then start it:

```
setsid nohup /root/tz01-env/venv/bin/python -B -u \
  /root/tz18a-svc/tz18a-chainbook-capture.py --serve \
  >> /var/lib/btc-chainbook/service.log 2>&1 &
```

`SERVICE_ARGV` is those five strings — `/root/tz01-env/venv/bin/python`, `-B`, `-u`,
`/root/tz18a-svc/tz18a-chainbook-capture.py`, `--serve` — and `OLD_SERVICE_ARGV` is TZ-18's, its fourth
being `/root/tz18-svc/tz18-chainbook-capture.py`. The service runs under no other command line (D10) and
beside no instance of either (D8). On SIGTERM it writes a `stop` record, closes the open window's files and
exits — 8caa0b4 lines 505–506 and 778–779, unchanged.

For the window at `T`, TZ-18 §3.3–§3.5 hold unchanged but for D4: the documents of `btc-updown-15m-{T}` and,
`≥ 200` ms later, of `btc-updown-5m-{T+600}` at **`T + 625`**; four concurrent book reads at each of
`T + 655`, `715`, `775`, `805`, `835`, `865` and `885`, five seconds before Tier C's reads of the same
five-minute market; `window.json` at `T + 905`. **Thirty requests per 900 s**, `2,880` a day, `0.033` per
second, none in the second of a scheduled recorder request of the same market — S6's first attempt at
`T + 605` or a Tier C read. S6's retries, three seconds apart after a failure (`recorder.py` lines 381 and
389), are unscheduled and are not claimed.

### 3.6 `--prove --as-of A`

`A` is an integer epoch the Executor passes (R3). `s` is the last `start` record's `wall_ns / 10**9`; the
instrument asserts `s <= A <= now`. Every figure is a function of files that no longer change by `A`, so two
runs with one `A` write the same bytes (V8).

- **Considered windows** — `considered(T, s, A)` (D11). Their seven checkpoints each, in order of instant,
  are the checkpoints considered, and every one is disclosed (V9).
- **G-DEPLOY** — 8caa0b4's code: qualifying iff the window's document instant `T + 625 >= s + 60` and the
  checkpoint's instant `<= s + 3,900`; the first 14 qualifying; completeness and reading as §4.
- **Exposure** — per considered window, `issued_of(document lines, book entries)`: how many carry a
  `send_mono_ns` that is not null, of `30`. A read still running at its thread's deadline is recorded with a
  null send stamp (8caa0b4 lines 632–636), so the count can understate the load and never overstate it. The
  window's **exposed interval** is `E = T + 600` when the count is `>= 1`; it is **fully loaded** when the
  count is `30`.
- **G-TIERC** — `read_g_tierc` over one row per considered window: its count, whether `E`'s manifest counts
  at `A` (D12), and that manifest's `quotes_complete` (§4).
- **Printed beside it, not gated:** every five-minute interval with `T0 + 300` in the proof window
  `[int(s), A]` and in the control window `[2·int(s) − A, int(s)]`, with `quotes_complete`, `complete` and
  whether it is exposed; manifests counted at `A`.
- **Skews** — minimum, median and maximum in ns over the considered checkpoints with four replies.
- **Concurrency** — per considered checkpoint with four sends, whether the last send precedes the first
  receive, and the count where it does not. Recorded, not asserted (V10).
- **Stored bytes** per considered window: its three files' sizes by `os.stat`.
- Output `tz18a-proof.json`, keys exactly `mode`, `as_of`, `start_record`, `proof_window`, `control_window`,
  `g_deploy`, `g_tierc`, `checkpoints`, `skew_stats`, `windows`, `counters`, `concurrency`. The request counter
  at exit is asserted `0`. Print `READING G-DEPLOY` and `READING G-TIERC`, each with its deciding count.

### 3.7 Cost, in exact units

| quantity | figure | derivation |
|---|---|---|
| requests per window | `30` | `2 + 4 × 7` |
| requests per day | `2,880` | `30 × 96` |
| added venue rate | `0.033` req/s | `2,880 / 86,400` |
| stored bytes | measured per window by §3.6 | TZ-18 §3.9 projected about `3.0` MB a day: `31,250` bytes a window at `96` windows a day |
| write cap | `200,000,000` bytes per process | TZ-18 §3.9's figure, summed per process by the base blob's `account` (lines 225–229), unchanged. `append_bytes` writes before it accounts (lines 219–221), so the service writes its stop record as it stops on reaching the cap — about `66` days after R2 at the projection; the report prints the figure from the measured bytes |
| resource floor | `2,200,000,000` bytes | map §6's `2,000,000,000` plus the cap; the service asserts it at every window and stops itself below it |
| forensic copies | `≈ 4,400,000` bytes | `801` bodies at TZ-17's measured mean of `5,048` bytes (TZ-17 report §1.1), TZ-18's two verify files at `233,549` bytes (TZ-18 report §2.6), and the smaller rest |

---

## 4. The gates, fixed here, before any of their data exists

**P-START** is the precondition of CANON hard rule 14: §3.4 served and parsed at both endpoints under
§3.2's request, or **BLOCKED** with nothing started. **G-DEPLOY** and **G-TIERC** judge the running
process. No threshold or sampling rule below moves once a number exists.

### G-DEPLOY — does the capture record both books at one instant?

TZ-18 §4's gate, unchanged but for the document instant (D4):

- **Unit:** a checkpoint. **Qualifying:** its window's document instant `T + 625 >= s + 60` and its own
  instant `<= s + 3,900`. A window under way at the start has no document fetch and contributes no unit.
- **Complete:** four stored replies, all HTTP `200`, each body non-empty and parsing as JSON, and a skew
  `<= 1,000,000,000` ns.
- **Reading:** of the first 14 qualifying checkpoints, `>= 13` complete → **PASS**; `<= 12` → **FAIL**;
  fewer than 14 qualifying by the budget end → **UNDECIDABLE**.
- **False-failure probability under a capture that loses nothing: exactly `0`.** This host's Tier C reads
  of the same venue returned `200` at `16,800` of `16,800` (map §2.3).
- **Power**, exactly `1 − (1−p)^14 − 14·p·(1−p)^13`: `p = 0.25` → `0.899031627923250198364257812500`;
  `p = 0.10` → `0.415370859484330000000000000000`; `p = 0.05` → `0.152985562588816560668945312500`. A
  deployment proof does not see a low loss rate; the TZ that scores these books re-reads completeness over
  its whole set first.

### G-TIERC — did the new capture disturb Tier C, under the load it actually applied?

- **Exposed interval:** `E = T + 600` of a considered window that issued at least one request; **fully
  loaded** when it issued all 30. The chain book requests only inside `E` — documents at `E + 25`, books at
  `E + 55` to `E + 285` — so each window's other two five-minute intervals carry none of its load, and are
  printed as the control they are.
- **Counted:** `E`'s `manifest.json` exists with `st_mtime_ns <= A · 10^9`.
- **FAIL:** any counted exposed interval whose `quotes_complete` is not `true`.
- **PASS:** no FAIL, and at least **two** counted fully loaded exposed intervals.
- **UNDECIDABLE:** otherwise — the interlock did not see the load. Map §4 holds TZ-18's G-TIERC PASS to the
  load that ran, two refused requests per window; under this rule that load reads UNDECIDABLE.
- **False-failure probability**, under "each exposed interval's `quotes_complete` fails independently at
  the rate the capture showed in the week before R1": `1 − (1 − f/m)^5`, printed by `--prestart` before the
  service starts — five being the most considered windows a proof ending by `s + 3,900` can hold.
  Family-wise over both gates it is the same number, G-DEPLOY's being `0`.
- **Power** at the PASS minimum of two fully loaded intervals, `1 − (1 − q)^2`, against a disturbance that
  breaks each with probability `q`: `q = 1` → `1`; `q = 0.5` → `0.75`; `q = 0.25` → `0.4375`. Two units see
  a gross disturbance and nothing finer.

### What the readings mean, fixed before the data

- **PASS and PASS** — both markets' books are recorded within one second of each other at `>= 13` of 14
  checkpoints under the declared request, and Tier C held at every exposed interval the proof saw. The
  service keeps running after the session, from its copy of the branch blob, unmerged, until the Architect's
  verdict. It says nothing
  about any price, book or edge, nor about a disturbance finer than two units can see.
- **Any other pair** — R5 stops the service in this session, verified, and B1 stays open.

---

## 5. Self-tests — `--selftest`

Each item is an `assert` through one counting helper, and the mode prints `n of n` with `n` counted.

| item | asserts | what |
|---|---|---|
| **S1** | `5` | the schedule at `T = 1790035200`: (1) document instant `1790035825`; (2) checkpoints `1790035855`, `1790035915`, `1790035975`, `1790036005`, `1790036035`, `1790036065`, `1790036085`; (3) each strictly inside `(T+600, T+900)`; (4) Tier C instants `1790035860`, `1790035920`, `1790035980`, `1790036010`, `1790036040`, `1790036070`, `1790036090`, none equal to a checkpoint; (5) the document instant is `20` s after the recorder's S6 instant `1790035805` and `30` s before the first checkpoint |
| **S2** | `3` | TZ-18's S2, unchanged |
| **S3** | `5` | the request, against `127.0.0.1` only, after `http_proxy`, `https_proxy`, `all_proxy` and their upper-case forms are removed from this process's environment, the number removed printed: (1) `build_request(u)` has method `GET` and `header_items()`, names lowercased, exactly `accept: application/json` and `user-agent: btc-5m-twap-tz18a`; (2) against a listener answering `200` with body `{}`, the received header block, names lowercased and sorted, is exactly `accept: application/json`, `accept-encoding: identity`, `connection: close`, `host: 127.0.0.1:{port}`, `user-agent: btc-5m-twap-tz18a`, no name repeated, and the request line begins `GET /`; (3) its record: status `200`, bytes `2`, sha256 `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`, both receive stamps non-null, `recv_mono_ns >= send_mono_ns`; (4) against a listener answering `403` with body `error code: 1010\n`: status `403`, bytes `17`, both receive stamps non-null, reason `http_error`; (5) against a closed port: status `None`, bytes `0`, both receive stamps `None`; and `skew_of` over records whose `recv_mono_ns` are `None`, `7` and `12` is `5` |
| **S4** | `4` | `same_service`: (1) `b"/root/tz01-env/venv/bin/python\0-B\0-u\0/root/tz18a-svc/tz18a-chainbook-capture.py\0--serve\0"` with `SERVICE_ARGV` → true; (2) `b"bash\0-c\0/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve\0"` → false; (3) TZ-18's command line → false with `SERVICE_ARGV`, true with `OLD_SERVICE_ARGV`; (4) `SERVICE_ARGV` with a sixth field `--x` → false, and `b""` → false |
| **S5** | `3` | the write guard: (1) a path under each of `/root/tz18a-work/`, `/root/tz18a-svc/` and `/var/lib/btc-chainbook/` passes; (2) `/root/btc-5m-twap/x` and `/root/tz18-work/x` raise; (3) `/var/lib/btc-recorder/x` raises |
| **S6** | `8` | readings on synthetic counts: (1) `read_g_deploy(14, 13)` PASS; (2) `(14, 12)` FAIL; (3) `(13, 13)` UNDECIDABLE; `read_g_tierc` over rows `(issued, counted, quotes_complete)`: (4) `(30, yes, true)`, `(30, yes, true)` → PASS; (5) those two and `(1, yes, false)` → FAIL; (6) `(30, yes, true)`, `(30, no, null)` → UNDECIDABLE; (7) `(30, yes, true)`, `(29, yes, true)` → UNDECIDABLE; (8) `(0, yes, false)`, `(30, yes, true)`, `(30, yes, true)` → PASS |
| **S7** | `3` | §4's three G-DEPLOY power literals, recomputed exactly in `Fraction`, tolerance `1E-18` |
| **S8** | `5` | TZ-18's S8 over this file's own syntax tree: imports within `sys.stdlib_module_names`; no `subprocess`; no `system`, `popen`, `spawn*` or `exec*` taken on `os`; no `shell` keyword; exactly two string constants containing `:` `/` `/`, equal to §3.2's endpoints — S3's loopback URLs are assembled from separate literals |
| **S9** | `2` | (1) `considered(T, 1790035000.0, 1790040000)` is true at `T = 1790035200`, false at `1790034300`, false at `1790039700`; (2) `issued_of` is `30` over 2 document lines and 28 entries, all with `send_mono_ns`, and `2` when the 28 entries' `send_mono_ns` are null |
| **S10** | `1` | `p_false_alarm(0, 2016, 5) == Fraction(0)`, `p_false_alarm(1, 2016, 5) == Fraction(82508989399201, 33300644496408576)` exactly, and `p_false_alarm(0, 0, 5) is None` |

**Total `39`.** A failure aborts the run.

---

## 6. Runs, in this order

| run | what | condition |
|---|---|---|
| **B** | derive (§3.1), build, commit, push the branch; print `P_push` — `date -u +%s` taken as `git push` exits `0` — and `git ls-remote origin refs/heads/tz-18a-chainbook-capture` | before the push, smoke `--selftest` runs only (P8) |
| **C** | the copy and `commit.txt` (§3.5), hash asserted | after B |
| **R0** | `--selftest` from the copy → `39 of 39` | after C |
| **R1** | `--prestart` (§3.4) → `/root/tz18a-work/run-1/` | not before `K_stop + 900` s (§0.4), so that no window directory the new service opens can already exist |
| **R2** | start the service (§3.5); print its `start` record; V12 | within `600` s of R1's exit; if that lapses, R1 is repeated once, into `run-1b/`, first |
| **R3** | the Executor sleeps, checking once a minute with `test -e` and reading nothing | ends at the first check at which `/var/lib/btc-chainbook/{W2}/window.json` and the `manifest.json` of `E1 = W1 + 600` and of `E2 = W2 + 600` all exist, or at `s + 3,900`, where `W1 = 900 · ceil((s − 565) / 900)` is the first window whose document instant is `>= s + 60` and `W2 = W1 + 900`. **`A = min(floor(now), floor(s) + 3,900)`** |
| **R4** | `--prove --as-of A` → `/root/tz18a-work/run-2/` | after R3 |
| **R4b** | the same → `/root/tz18a-work/run-3/`; `cmp` against R4's file | after R4 |
| **R5** | **only if (G-DEPLOY, G-TIERC) ≠ (PASS, PASS):** block K-18a (§6.1), verified | after R4b |
| **R6** | retention (§9) | after R4b, and after R5 where it ran |

Every run is `/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py <mode>`, with
`--repo /root/tz18a-work/wt` and `--out` for `--prestart` and `--prove`. Before R1, R4 and R4b, assert that
`git -C /root/tz18a-work/wt rev-parse HEAD` equals `git rev-parse origin/tz-18a-chainbook-capture` and that
the copy's SHA-256 equals the branch blob's; print both, and the epoch at which each of R1, R4 and R4b starts.
§0.2's reads are repeated after R6 and printed beside the opening ones.

**Compute, not wall clock, is bounded:** R0, R1, R4, R4b and §9 stay under `900` s together at their upper
bounds (§10 C4). R3 is a sleep, ending by `s + 3,900`.

### 6.1 The two stop blocks

Each selects by the whole command line, so it can signal nothing else, and a shell carrying its pattern
cannot match it.

**K-18** — TZ-18's service, only under §0.4:

```
P=$(pgrep -fx '/root/tz01-env/venv/bin/python -B -u /root/tz18-svc/tz18-chainbook-capture.py --serve'); echo "pid=[$P]"; test -n "$P" && kill -TERM $P; echo "exit=$?"
```

**K-18a** — this TZ's service, only under R5:

```
P=$(pgrep -fx '/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve'); echo "pid=[$P]"; test -n "$P" && kill -TERM $P; echo "exit=$?"
```

The Executor runs the block once. If the session's classifier refuses it — map §6: `kill` is refused alone
or inside a compound command — the Executor prints it, the Boss runs it verbatim in a root shell on the
VPS, and the Executor waits. **Verification is the Executor's, never the Boss's account:** `30` s after the
block, `pgrep -fx` with the same argv prints no line and exits `1`, and `runtime.jsonl` holds a `stop` record
with the pid the block printed, later than that pid's `start`. If the process is still alive `120` s after
the block, the same block with `-KILL` in place of `-TERM` is authorized by the same route; a `stop` record
then missing is disclosed beside the `pgrep` read, which decides.

---

## 7. Validation

Every row is an `assert` that aborts the run unless it says otherwise in plain words. Counts come from the
run, never typed.

| # | row | runs |
|---|---|---|
| **V1** | the fingerprint gate inside the instrument: revision equal, anchors 6 of 6, re-derived 4 of 4, rows hashed 25 of 25, `frozen` equal 23 of 23 | R1, R4, R4b |
| **V2** | host and resource gates: H1–H3 compared by the Executor (§0.2); `avail >= 2,200,000,000` asserted inside the instrument at each run and each window | §0, R1, R4, R4b, the service |
| **V3** | the base blob hashes to `33753b2bb1e322a081e6cba8bad976268e2d6046dc350e6ceae3e748ad6e4bfe` before the first edit | B |
| **V4** | every hunk of `diff -u` between the base blob and the new file maps to exactly one D-item; the report prints each hunk's header line with its D — disclosed for the Architect's check, not asserted | B |
| **V5** | the write guard: every open for writing is checked against the three roots before it opens; counts printed | all |
| **V6** | the open guard under `/var/lib/btc-recorder/`: every basename `manifest.json`; counts printed — R0 `0`, R1 at most `2,016`, R4 and R4b equal | all |
| **V7** | requests: R0 exactly `3`, each to `127.0.0.1`; R1 exactly `2`; R4 and R4b `0` | R0, R1, R4, R4b |
| **V8** | determinism: `tz18a-proof.json` byte-identical between R4 and R4b, `cmp` clean; SHA-256, lines and bytes printed | R4b |
| **V9** | every considered checkpoint disclosed in order, qualifying or not, with its reason, its four statuses and its skew | R4 |
| **V10** | concurrency per considered checkpoint with four sends, and the count where the last send did not precede the first receive — recorded, not asserted | R4 |
| **V11** | the key sets of `window.json`, `tz18a-prestart.json` and `tz18a-proof.json` are fixed in the source and asserted before each write, with no forbidden key at any depth | all |
| **V12** | the `start` record's `commit` equals `origin/tz-18a-chainbook-capture` and its `file_sha256` the branch blob's; `pgrep -fx` with `SERVICE_ARGV` prints exactly one line, equal to `service.pid` and to the record's pid; `/proc/{pid}/cmdline` is `SERVICE_ARGV` NUL-joined; `runtime.jsonl` holds exactly one `start` record written in this session | R2, and at the session's end where R5 did not run |
| **V13** | the write cap: each process's bytes summed as written, `<= 200,000,000`, printed | all |
| **V14** | `git diff --name-only origin/main origin/tz-18a-chainbook-capture` prints exactly `research/tz18a-chainbook-capture.py`, after the branch push and before the report commit | after the push |
| **V15** | contract §4.2's separation self-check, verbatim, after the branch push and before the report commit | after the push |
| **V16** | order: `P_push` < the first `recv_wall_ns` of the R1 run that preceded R2 < `s` < R4's start; and `s >= K_stop + 900` | R4 |
| **V17** | where R5 ran, the stop verified as §6.1 says | R5 |
| **V18** | retention: the `211` files of `forensics-before.sha256` hash unchanged; every hash §9 step 2 names held; counts before and after | R6 |

---

## 8. What the report prints

`CryptoReports/TZ-18a-chainbook-capture-redeploy-report.md`, pushed from `/root/tz18a-work/wt-report` with
`git push origin HEAD:main`; the implementation on its branch with a pull request, unmerged. If `main` moved
meanwhile, the report commit is made again on the new `origin/main`; nothing is ever forced.

1. **In the first ten lines:** P-START; G-DEPLOY and G-TIERC, each with its deciding count; the service
   running or stopped, and how that was verified.
2. §0, verbatim, opening and closing; K0–K2 and `K_stop`; the window directories by name.
3. The instrument: SHA-256, lines, bytes; the branch commit; `P_push`; V4's hunk map.
4. P-START: per request, method, URL, the two fields `build_request` sets and S3's five-field block, status,
   bytes, SHA-256, parse result and elapsed time; the two token ids; the base rate — slots, directories,
   `m`, `f` — and `1 − (1 − f/m)^5`.
5. The service: pid, argv, `start` record, commit, file SHA-256, `service.pid`, and the closing `/proc` read.
6. **G-DEPLOY's disclosure** (V9), and the counts of complete, incomplete and missed checkpoints.
7. The skews — minimum, median, maximum — **the number the next TZ sizes its pairing rule from.**
8. **G-TIERC:** per considered window, its issued count, fully loaded or not, `E`, counted or not and
   `quotes_complete`; then the proof and control windows, interval by interval.
9. Request accounting — R0's three, R1's two, the service's per window by status; stored bytes per window;
   the write cap in days at the measured rate; the `df` deltas.
10. Every output file of R1, R4 and R4b: SHA-256, lines, bytes.
11. **TZ-18's three outputs** — `/root/tz18-work/run-1/tz18-verify.csv`, `run-1/tz18-verify.json` and
    `run-2/tz18-proof.json` — SHA-256, lines, bytes; and the `run-3/` and `predebug/` copies of the first two
    asserted equal to them by hash. The TZ-18 report printed no hash of any of its files (map §3).
12. Retention per §9, with every count.
13. V1–V18, each with the count it asserted and the runs it held on.
14. What could not be implemented as written.

**Appendix A:** the diagnostic scripts, in full (§0.5).

Any row is re-derivable by the Architect from `tz18a-prestart.json`, `tz18a-proof.json` and the stored
window files, without re-running anything.

---

## 9. Retention

In this order, each step only after the previous one completed as it says:

1. **Copy first.** Every file under `/root/tz17-work/`, `/root/tz18-work/` and `/root/tz18-svc/`, worktrees
   included, whose SHA-256 is named by any committed report on `main` — matched against every hexadecimal
   token of 16 to 64 characters those reports print, the predicate TZ-14 and TZ-15 used — and, named here,
   TZ-18's three outputs of §8 item 11, every file §0.5 listed, and `/root/tz18-svc/commit.txt`. Each is
   copied into `/root/btc-forensics/` by exclusive create unless the store already holds its hash, the hash
   asserted at source and destination, under its path below `/root/` with `/` replaced by `--` — for
   instance `tz17-work--raw--btc-updown-15m-1788998400.body` — in sorted path order.
2. **Then assert** that the store holds, by hash, all `801` values of the five `sha_*` columns of TZ-17's
   CSV — extracted as TZ-18 §3.7 step 1 extracts it: SHA-256
   `96b5e21e2cc59e2f3bde332d60457533158bd16c2eeaaaba844bf35b1efc63ee`, `99,075` bytes, `201` lines — and
   `tz17-candidates.csv` and `tz17-summary.json`, `96b5e21e…` and
   `fb20cbf15751fdaac3dd0d2736192f891d746b91eab1db9bcef81d6a4e788937` (TZ-17 report §5 V7), and TZ-18's three
   outputs; and that the `211` files of `forensics-before.sha256` hash unchanged. Print the counts before
   and after, and the count copied from each tree.
3. **Then the worktrees** — `/root/tz17-work/wt`, `/root/tz17-work/wt-report`, `/root/tz18-work/wt`,
   `/root/tz18-work/wt-report` — each by `git worktree remove` without `--force`, after its untracked
   `__pycache__` directories are deleted. One that still refuses stays, with its tree, and is reported.
4. **Then the trees** — `rm -rf /root/tz17-work`, `rm -rf /root/tz18-work`, `rm -rf /root/tz18-svc`, one
   command naming one tree each, a tree only once its worktrees are gone — verified by `test -e`. If the
   classifier refuses any, the Boss is handed one block of the refused commands, and the outcome is verified
   by `test -e`: in this session if he runs it before the report, otherwise by the next TZ's §0.

`/root/tz18a-work/` is the next TZ's to reclaim on the same terms. `/root/tz18a-svc/` is not scratch while a
service runs from it. `/root/tz15-work/` stays TZ-16's (map §3). **The capture is never deleted:**
`/var/lib/btc-chainbook/` keeps TZ-18's windows beside this service's, all reserved on map §2.5's terms, and
nothing of it enters git history.

---

## 10. Pre-send checks

Performed on 2026-09-23 against this file, in a reading separate from its writing, with `origin/main` at
`fda5eb6` — `SYSTEM-MAP.md` SHA-256 `704070149009…`, byte-equal to the project copy — and `refs/pull/18/head`
at `8caa0b4`, both read directly. Line numbers are the base blob's unless a row names another file.

### C1 — scope against body

| named in the body | how | intersects, by path or by content class | resolution |
|---|---|---|---|
| `research/tz18a-chainbook-capture.py` | written, branch | — | new; P7 binds committed files |
| `CryptoReports/TZ-18a-chainbook-capture-redeploy-report.md` | written, `main` | — | — |
| this TZ, `SYSTEM-MAP.md`, the 25 table paths | hashed | — | — |
| the base blob at `8caa0b4` | `git show` | — | not on `main` |
| `CryptoReports/TZ-18-chainbook-capture-deploy-report.md` | counted | — | — |
| every committed report | read for hex tokens (§9) | P3 by class: reports print prices and outcomes | P2's named exemption, tokens only |
| TZ-17's committed CSV | five `sha_*` columns (§9) | P2 and P3 by class: readings, outcomes | P2's named exemption, the five columns alone |
| `research/recorder/recorder.py` | cited | — | not run, not imported |
| `/var/lib/btc-recorder/**` | `manifest.json` opens; `find`, `df`, `grep` over `runtime.jsonl`, `test -e`, `statvfs`, listings | P1 by path | P1's scope; two named exemptions; "open no file" |
| `/var/lib/btc-chainbook/**` | written; `runtime.jsonl`, considered windows and directory names read | P3 by class: books, live documents | P3's named exemption |
| `/var/lib/btc-chainbook/service.pid` | replaced | §2's removal list | named there |
| `/root/tz18a-work/**`, `/root/tz18a-svc/**`, `/root/btc-5m-twap/.git` | written | — | named in §2's written list |
| `/root/btc-forensics/` | exclusive create; hashed | P2 and P3 by class: settled documents, readings, outcomes | P2's named exemption, cross-referenced by P3; §2's written list |
| `/root/tz17-work`, `/root/tz18-work`, `/root/tz18-svc` | hashed, copied, removed; scripts printed | P2 and P3 by class; §2's removal list | P2's named exemption; named in the removal list |
| `/root/tz15-work`, `/root/PROJECT_GAMING_PS5`, `/root/tz01-env/`, `/root/tz04a-env/` | `test -e`, `du`, interpreter, a `pgrep` pattern | — | untouched |
| `/proc/**` | `pgrep`, `cmdline` scans, `test -e` | P6 by class | reads; signals only by K-18 and K-18a |
| the two venue endpoints | `--prestart`, `--serve` | P2, P3 and P5 | P2's own text, live markets only; P3's own text; P5's own text |
| `127.0.0.1` | S3 | P4 | P4's own text |
| `tz18a-prestart.json`, `tz18a-proof.json`, `forensics-before.sha256`, the report | outputs | P3 by class | token ids, statuses, counts, hashes, flags — no price or outcome; key sets allow-listed (V11) |
| K-18, K-18a | signal | P6 | P6's own text |
| `git worktree remove` ×4, `rm -rf` ×3 | removal | §2's removal list | named there |

**21 entries. 8 intersections, each closed by a named exemption or a named entry of §2's removal list** —
the reports' tokens, the CSV's five columns, the recorder root's non-manifest reads, the chain book store,
the forensic copies, the three trees' contents and their removal, `service.pid`. **4 more fall inside a
prohibition's own wording** — the venue replies, the loopback, the `/proc` reads, the two stop blocks. None
open.

### C2 — origin of every expectation

| class | the fixed expectations of §5 and §7 |
|---|---|
| computed by an implementation independent of the one under test, exact | S1's 18: `1790035825`, the seven checkpoints, the seven Tier C instants from `t0 + INTERVAL_S - tau` (`config.py` line 93), `1790035805` from `S6_FETCH_OFFSET_S = 5` (`recorder.py` line 32), `20`, `30` — integer arithmetic. S3's `2`, `44136fa3…` (SHA-256 of `{}`), `17`, `5`, and the five-field block, captured on a loopback listener under Python 3.12.3. S7's three values as exact fractions `241331965/268435456`, `41537085948433/100000000000000`, `250651545745517053/1638400000000000000`, each a terminating decimal equal to its 30-place literal and to TZ-18 §4's. S9's true, false, false, `30`, `2`. S10's `0`, `82508989399201/33300644496408576`, `None`, in `Fraction`. Exact, so beyond any tolerance by more than ten decades |
| quoted from a committed artifact | S2's `999,999,999`, `1,000,000,001`, `429` (TZ-18 §5). S6's `14`, `13`, `12` (TZ-18 §4). V1's `6`, `4`, `25`, `23` (map §0 at `2026-09-23-a`, its table counted by the base blob's own `ROW_RE`: 26 rows, 25 hashed, 23 `frozen`, 2 tracked). V2's `2,200,000,000` = `2,000,000,000` (map §6) + `200,000,000` (TZ-18 §3.9). V3's `33753b2b…` (TZ-18 report §3, re-derived from `refs/pull/18/head`). V13's `200,000,000` (TZ-18 §3.9). V18's and §0.2's `211` (map §3). §9's `801`, `96b5e21e…`, `99,075`, `201`, `fb20cbf1…` (TZ-17 report §5 V7, TZ-18 §3.7 step 1), re-derived here from the committed report: 201 lines, 99,075 bytes, 801 distinct values in 1,000 cells |
| design counts of this TZ | S6's `30` and `2`; S8's `2`; V6's `0` and `<= 2,016`; V7's `3`, `2`, `0`; V14's one path; V16's `900` |

**The third kind occurs 0 times.** `m`, `f`, `1 − (1 − f/m)^5`, `s`, `A`, `K_stop`, the skews, statuses,
issued counts and stored bytes are printed, or compared only with each other (V6, V8, V16); V6's `<= 2,016`
holds for every admissible value.

### C3 — shape of every diff

No file is called additive, and §0–§9 never describe a change as insertions alone. The repository
gains one path, `research/tz18a-chainbook-capture.py` — absent from `origin/main` at `fda5eb6`, `git ls-tree`
count `0` — and the report; no committed file changes, which V14 asserts. The base blob is not on `main`;
§3.3 names the base lines each change replaces, read from `refs/pull/18/head`: D1 2–16; D2 35; D3 55, 70,
71, 76, 77; D4 85; D6 75, 98–115, 117, 122–125, 143–145, 360–363, 785–979; D7 426–463; D8 518–549; D9
561–571; D10 757–782; D11 997–1024; D12 1037–1067; D13 138–142, 1070–1236; D15 1239–1385; D16 1388–1420 —
pairwise disjoint. D5 and D14 replace nothing.

### C4 — cost of every check

Measured rate: Stage A of TZ-17 read, hashed and parsed 801 stored bodies in `0.249` s and `0.240` s on this
host (TZ-17 report §2.10) — **`0.31` ms a file**.

| check | population at its upper bound | evaluations | seconds |
|---|---|---|---|
| fingerprint gate, R1, R4, R4b | 26 files, `1,062,750` bytes, each run | 78 | `0.03` |
| R0 | 39 asserts, one `ast` parse, 3 loopback requests at the `5.0` s timeout | 43 | `<= 16` |
| R1, process scan | one read per live pid, at `32,768` | 32,768 | `<= 10.2` |
| R1, base rate | the 2,016 slots, unfiltered | 2,016 | `0.63` at the measured rate; `<= 604.8` at the fail-fast edge |
| R1, live requests | 2 at the `5.0` s timeout | 2 | `<= 10` |
| R4, R4b | per run `<= 5` windows: `<= 10` document lines, `<= 140` entries, `<= 5` `window.json`, `<= 15` `stat`; `<= 33` manifests | `<= 203` each | `<= 0.07` each |
| §9 | the three trees and the store at `<= 10,000` files, hashed at source and destination | `<= 20,000` | `<= 6.2` |

**Sum `<= 648` s with the fail-fast edge, `43` s without it** — under the `900` s §6 states and the `3,600` s
ceiling. Fail-fast bounds, term by term: §3.4 step 3 aborts when the first `100` opens exceed `30` s, `0.3`
s an open — about 970 times the measured rate — so `2,016 × 0.3 = 604.8` s is the most the scan can take;
the `5.0` s timeout is the base blob's `READ_TIMEOUT_S`, line 89, so R0's three requests and R1's two cost
at most `25` s; R3's `s + 3,900` is `BUDGET_S`, line 92, and since `W2 + 900 < s + 2,135` it leaves at
least `1,765` s after E2's close for E2's manifest. The live-window wait, `<= 90` s, and R3 are sleeps.

### C5 — every count

- `25`, `23`, `6`, `4`: the map's §0 at `fda5eb6` under `ROW_RE` — 26 rows, 25 hashed, 23 `frozen`, 2
  tracked; anchors `A1`–`A6`; re-derived `A2`, `A4`, `A5`, `A6`.
- `39` = `5 + 3 + 5 + 4 + 3 + 8 + 3 + 5 + 2 + 1`, S1 to S10.
- `14`, `13`, `12`: over the first 14 qualifying checkpoints. W1 and W2 carry 7 each, `W1 < s + 335` and
  `W2 + 885 < s + 2,120 <= s + 3,900`, so 14 qualify before the budget ends whenever the service runs.
- `30` = `2 + 4 × 7`; `2,880` = `30 × 96`, `96` = `86,400 / 900`; `0.033` ≈ `2,880 / 86,400`.
- `2,016` = `(605,100 − 600) / 300 + 1`, the multiples of 300 in `[p − 605,100, p − 600]`.
- `5` = `⌊3,615 / 900⌋ + 1`, the multiples of 900 in `[s − 625, s + 2,990]`, which `considered` admits when
  `A <= s + 3,900`.
- `33` = `14 + 14 + 5`; `14` = `3,900 / 300 + 1`, the closes in a window no longer than 3,900 s.
- `801` = `200 + 601`, `601` = `4 × 200 − 199` shared boundaries; re-derived from the extracted CSV, 801
  distinct values in 1,000 cells.
- `211`: map §3. `7` worktrees at TZ-18's end (map §3), `4` of them §9's.
- V7's `3`: S3 items 2, 4 and 5 send one request each, item 1 none; `2`: §3.4 steps 5 and 6.
- `5` wire fields, `2` set by the instrument: §3.2's table. `16` D-items, `18` V-rows, `8` prohibitions.

### C6 — every population

| statistic | population |
|---|---|
| G-DEPLOY reading | the first 14 qualifying checkpoints, by instant, of the considered windows |
| V9 | every checkpoint of every considered window |
| skews | considered checkpoints with four non-null receive stamps |
| V10 | considered checkpoints with four non-null send stamps |
| `issued_of` | each considered window's 2 document lines and 28 book entries |
| G-TIERC reading | considered windows with `issued >= 1`, `E` counted at `A`; the PASS count over those with `issued = 30` |
| proof and control printouts | five-minute intervals with `T0 + 300` in `[int(s), A]` and in `[2·int(s) − A, int(s)]`, manifests counted at `A` |
| `m`, `f`, `1 − (1 − f/m)^5` | the 2,016 slots closing in `[p − 604,800, p)`, manifests present |
| process counts | every live pid in `/proc` at the scan |
| request accounting | every request of R0, R1 and the service |
| stored bytes | the three files of each considered window |
| write cap, V13 | the bytes each instrument process writes |
| V6 | every open under `/var/lib/btc-recorder/` in each run |
| §9 and V18 | every file under the three trees and the store; the 801, 2 and 3 named hashes; the 211 pre-existing files |

### C7 — every signature and every behaviour

Base blob, `8caa0b4`:

| function | signature | lines relied on | for |
|---|---|---|---|
| `http_get` | L426 `def http_get(url, timeout=READ_TIMEOUT_S):` | L434 `req = urllib.request.Request(url, method="GET")`; L447–448 both stamps taken unconditionally; L457 `"recv_mono_ns": recv_mono if status is not None or body else recv_mono,` | §1, D7 |
| `checkpoint_is_complete` | L305 `def checkpoint_is_complete(entries):` | L307 four entries; L310 status `200`; L312 non-empty; L315 `json.loads`; L321 the skew bound | §4 |
| `skew_of` | L326 `def skew_of(entries):` | L328 `... if e.get("recv_mono_ns") is not None]` | S3 (5) |
| `concurrency_ok` | L334 `def concurrency_ok(entries):` | L338 `if len(sends) != 4 or not recvs:`; L340 `return max(sends) < min(recvs)` | §3.6, V10 |
| `qualifies` | L343 `def qualifies(document_instant, checkpoint_instant, start_wall_s):` | L345 `if document_instant < start_wall_s + QUALIFY_LEAD_S:`; L347 `if checkpoint_instant > start_wall_s + BUDGET_S:` | D4, §4 |
| `read_g_deploy` | L352 `def read_g_deploy(n_qualifying, n_complete):` | L353–357 UNDECIDABLE below `GATE_UNITS`, PASS at `GATE_COMPLETE_PASS`, else FAIL | S6 (1)–(3) |
| `schedule_for`, `next_window` | L284 `def schedule_for(T):`; L752 `def next_window(now):` | L289 `"document_instant": T + DOC_OFFSET,`; L754 `return T0 if now <= T0 + DOC_OFFSET - 1 else T0 + WINDOW` | D4 |
| `fingerprint_gate` | L381 `def fingerprint_gate(repo, out):` | L386 the revision assert; L410 the `frozen` count assert | D3, V1 |
| `token_ids_of` | L476 `def token_ids_of(doc_raw):` | L492 `if len(ids) != 2 or len(set(ids)) != 2 or not all(ids):` | §3.4 step 5 |
| `acquire_single_instance` | L518 `def acquire_single_instance(out):` | L539 `if cmd and me in cmd and "--serve" in cmd:` | D8 |
| `runtime_record` | L552 `def runtime_record(event, extra=None):` | L561–571 the `config` dict | D9 |
| `account`, `append_bytes` | L225 `def account(n):`; L214 `def append_bytes(path, data):` | L228 the cap assert; L219–221 write, then `account` | §3.7 |
| `guard_resources` | L236 `def guard_resources():` | L238–240 `statvfs` and the floor assert | V2, §3.7 |
| `check_write_path`, `check_read_path` | L177 `def check_write_path(path):`; L187 `def check_read_path(path):` | L181–184 the three roots; L190–193 `manifest.json` alone | S5, V5, V6 |
| `_sigterm`, `mode_serve` | L505 `def _sigterm(signum, frame):`; L757 `def mode_serve(args, out):` | L506 `STOP.set()`; L762–764 the `None` return; L778–779 the `finally` stop record | §3.5, D10 |
| `fetch_books` | L593 `def fetch_books(T, tau_prime, plan, out):` | L610–614 `no_token_ids` and L632–636 `thread_deadline` entries, both `send_mono_ns=None` | §3.6 |
| `run_window` | L647 `def run_window(T, out):` | L653 the document instant; L659–662 the two documents, `DOC_GAP_S` apart; L668 ids only on `200`; L699–700 missed entries with `"send_mono_ns": None` | §3.5, §3.6 |
| `read_start_record` | L986 `def read_start_record(out):` | L991 `rec = starts[-1]` | §3.6 |
| `load_windows` | L997 `def load_windows(out):` | L998 every window directory listed | D11 |
| `manifest_scan` | L1037 `def manifest_scan(lo, hi, out, label):` | L1051 `if not (lo <= close <= hi):`; L1059 `m = json.loads(read_bytes(mp))` | D12, §3.6 |
| `mode_prove` | L1070 `def mode_prove(args, out):` | L1076 `start_wall_s = start["wall_ns"] / 1e9`; L1178 the `tz18-verify.json` read; L1192 `"generated_wall_ns": time.time_ns(),`; L1234 the terminal assert | D13 |
| `mode_selftest`, `main` | L1243 `def mode_selftest(args, out):`; L1392 `def main(argv=None):` | L1396 `--verify-tz17`; L1401 `--verify-json` | D15, D16 |

`origin/main`, `fda5eb6`:

| file | lines relied on | for |
|---|---|---|
| `research/recorder/recorder.py` | L32 `S6_FETCH_OFFSET_S = 5`; L375 `async def fetch_s6(self, t0, path):`; L379 `await sleep_until(t0 + S6_FETCH_OFFSET_S)`; L381 `for _ in range(5):`; L389 `await asyncio.sleep(3)` | §1 item 1, §3.5, S1 (5) |
| `research/recorder/config.py` | L61 `QUOTE_TAUS = (240, 180, 120, 90, 60, 30, 10)`; L87 `def quote_checkpoint_epoch(t0, tau):`, L93 `return t0 + INTERVAL_S - tau`; L107–108 `interval_dir` | S1 (4), §3.4 step 3 |
| `research/recorder/manifest.py` | L203–204 `quotes_complete = (len(quote_reads) == config.QUOTE_READS_PER_INTERVAL and all(r["status"] == 200 and r["body_is_json"] for r in quote_reads))`; L241 `def write(dirpath):`, L247 `os.replace(tmp, path)` | §4 G-TIERC, D12 |

Every sentence holds against its lines. One was rewritten in this pass: D4 had `qualifies` reading
`DOC_OFFSET`, and L343–349 show it receives the instant `schedule_for` computes.

### C8 — every cross-reference

| reference | read at | supports |
|---|---|---|
| map §0 | the revision, the six anchors, the 26-row table | header, §0.1, V1 |
| map §1 | PR #18's row: closed unmerged, never on `main` | §0.3 |
| map §2.3 | the `manifest.json` exception; 16,800 replies, every one `200` and parseable | P1, P3, §4 |
| map §2.5 | the stop handed to the Boss on 2026-09-23; the `window.json` and `runtime.jsonl` exception; the chain book's books reserved | §0.4, P3, §9 |
| map §3 | `211`; seven worktrees; the two trees TZ-18a reclaims; no hash in the TZ-18 report; `/root/tz15-work/` TZ-16's | §0.2, §8, §9 |
| map §4 | G-CHAIN stands; TZ-18's G-TIERC stands only for the load that ran | §1, D6, §4 |
| map §5 | B1 open; B2 only after TZ-16's first reading | §1 |
| map §6 | host identity; the `2,000,000,000` floor; Python 3.12.3; `kill` refused alone or in a compound command | §0.2, §0.6, §3.7, §6.1 |
| map §7 items 54, 75, 76, 77 | no pass before the push; the whole-request rule; the substring check; TZ-18a's list and the no-diagnosis rule | P5, P8, §3.2, D8, §1 |
| CANON hard rule 14 | the pre-start request, fixed headers, a named and verified stop | §3.2, §3.4, §4 |
| contract §4.2 | the separation self-check | V15 |
| TZ-18 §2, §3.2, §3.3, §3.5, §3.7 step 1, §3.9, §4, §5 | host paths; endpoints; the schedule and its same-second sentence; storage; the CSV extraction; cost and cap; G-DEPLOY; S2 and S8 | §0.2, §1, §3, §4, §5, §9 |
| TZ-18 report §2.1, §2.6, §2.7, §3 | the start record; bytes; the service table; the file's hash | §0.4, §3.7, V3 |
| TZ-17 §9; TZ-17 report §1.1, §2.10, §5 V7 | copies nothing; the `5,048`-byte mean; Stage A's time; the two hashes | §0.2, §3.7, C4, §9 |
| base blob lines and `recorder.py` lines | as C7 quotes them | §1, §3, D2, D7, D8 |
| internal §0.2 to §10 | every one exists in this file | — |

Each reference was read, none from memory, and each supports its sentence. One sentence was rewritten in
this pass: §4's G-TIERC UNDECIDABLE line had attributed to map §4 a reading it does not state.

### Checks this session could not perform

None. The repository at `fda5eb6` and `refs/pull/18/head`, and both venue hosts, were read in this session.
What only the capture host holds is a condition the Executor evaluates: the 211-file store (§0.2), the TZ-18
service's records (§0.4), the diagnostic scripts (§0.5), and the wire block under the host's own
interpreter (S3), which R0 asserts before any live request.
