# TZ-18 — the chain book capture, deployed

**Canonical filename: `TZ-18-chainbook-capture-deploy.md`.** The Executor names the committed file
from this line, in `CryptoTZ/`, never from the name it received.

| field | value |
|---|---|
| map revision required | `2026-09-19-c` |
| anchors required | `A1` `229a944f2d51` · `A2` `6c5089330629` · `A3` `0-complete / 1-student-5tau-not-disqualified / 2-undecidable-5tau` · `A4` `437b45ea196b` · `A5` `9fd1c7de0f74` · `A6` `729f0bcdbee3` |
| fingerprint rows | all 24 hashed rows of the map's §0 table; the 22 in state `frozen` asserted equal |
| Executor model | **Opus** — network capture, a long-lived process, clock discipline |
| branch | `tz-18-chainbook-capture` |
| file added | `research/tz18-chainbook-capture.py` — the only path this TZ writes in the repository |
| report | `CryptoReports/TZ-18-chainbook-capture-deploy-report.md`, pushed to `main` |
| pricer | **not read, not called, not scored.** `A6` is stated so that what was *not* scored is not in doubt |

A mismatch on the revision string, on any anchor, on any `frozen` row, or on any of §0.2's host
conditions is **BLOCKED before any work**, with every read printed.

---

## 0. Preflight

### 0.1 Fingerprint

Print `wc -l`, byte count and `sha256sum` for every path in the map's §0 fingerprint table, and for
`SYSTEM-MAP.md` itself. Assert the 22 `frozen` rows equal. Re-derive `A2`, `A4`, `A5` and `A6` from
their files as the first 12 hex characters of each file's SHA-256 rather than copying the table.

**`research/tz17-settlement-chain.py` is deliberately not in that table and is not gated.** Whether
PR #17 is merged is the Boss's, not this TZ's.

### 0.2 Host gate — three conditions, all mechanical

Run from `/root/btc-5m-twap`, output verbatim into the report:

```
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'
grep -rl --include=runtime.jsonl 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder | head -n 1
du -sb /root/PROJECT_GAMING_PS5
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
test -e /root/tz17-work; echo "tz17-work exit=$?"
git worktree list
```

- **H1** — `find` prints exactly one path.
- **H2** — `pgrep -fx` prints **exactly one line**, and its pid is the recorder's. `-fx` matches the
  whole command line and nothing else: a shell evaluating this block carries the pattern as a
  substring and cannot match it exactly. *(TZ-17's H2 read "at least one line" from `pgrep -af
  recorder` and was satisfied by the Executor's own shell — its report §6 item 4. This row replaces
  that wording.)*
- **H3** — `df` names source `/dev/vda2` and size `31612203008` bytes, the map §6 host-identity row.
- **Resource gate** — `avail` **≥ `2,200,000,000`** bytes: the map §6 floor of `2,000,000,000` plus
  this TZ's own write cap of `200,000,000` (§3.9). Asserted again inside the instrument at every run
  through `os.statvfs`, `f_bavail * f_frsize`.
- `test -e /root/tz17-work` must exit `0`. Its tree is this TZ's **read-only** input and nothing here
  removes it.

### 0.3 Two repository reads, printed, one of them asserted

```
git show origin/main:CryptoReports/TZ-17-settlement-chain-report.md | sha256sum
git ls-tree -r --name-only origin/main | grep -c '^research/tz17-settlement-chain.py$'
git ls-tree -r --name-only origin/main | grep -c '^research/tz18-chainbook-capture.py$'
```

- The first is **printed**, not asserted: `0553061fb9f4793e0e73167042af0a770c5d640fae56f2fb1c7611b494c45815`
  is the copy the Architect audited, and a trailing byte may separate a committed file from a
  forwarded copy. **What is asserted is the CSV inside it** — §3.7, where it does work.
- The report path must exist on `origin/main`, or the run is **BLOCKED**: a TZ that has not published
  has not executed, and this TZ builds on TZ-17's stored bodies.
- The second count is printed and carries no threshold — `0` means PR #17 is unmerged, `1` means
  merged; either is a legal state for this TZ.
- The third count must be `0`, or the run is **BLOCKED**: this TZ's own path must not already exist.
  *(The Architect could not read `origin/main` when this TZ was written — §10, C3 — so the check is
  mechanical and belongs to the Executor.)*

### 0.4 Trees and interpreter

Two worktrees from `origin/main`: `/root/tz18-work/wt` on branch `tz-18-chainbook-capture`, and
`/root/tz18-work/wt-report` detached, from which the report is pushed by
`git push origin HEAD:main`. Interpreter `/root/tz01-env/venv/bin/python` — the research interpreter
of the map's §6 — for every run. Neither `/root/tz01-env/` nor `/root/tz04a-env/` is touched.

---

## 1. Why

TZ-17 measured, on 200 resolved windows, that `btc-updown-15m-{T}` and `btc-updown-5m-{T}` open on
the same published reading — the same literal at 200 of 200 — and that both families' outcomes agree
with one reading at each shared boundary, at 200 of 200. That makes one structural statement
available with no model and no forecast: **when the reading at `T+600` is at or above the reading at
`T`, every state in which `btc-updown-5m-{T+600}` resolves Up is a state in which
`btc-updown-15m-{T}` resolves Up**, and symmetrically below. The two markets' executable prices are
therefore constrained by each other, and a violation of that constraint would be an edge that needs
neither `p_fair` nor a direction.

Nobody has looked at the two books at once. Tier C records the 5-minute book at seven checkpoints; no
capture has ever opened a 15-minute market. **This TZ deploys the capture and proves it, and scores
nothing about any price** — the measurement is the next TZ's, as CANON hard rule 11 requires and as
TZ-17's own §4 stated when it fixed what PASS would mean.

It also closes the one gap the TZ-17 audit found, offline and with no network: TZ-17 inferred each
market's settlement reading from the *next* market's price to beat, while every document it stored
also carries the venue's own `finalPrice`. §3.7 compares them directly, on the 801 bodies already on
disk, before anything reclaims them.

---

## 2. Scope, and what is prohibited

**Built:** exactly one repository file, `research/tz18-chainbook-capture.py`.

**Host paths written:** `/root/tz18-work/**` (worktrees and run outputs), `/root/tz18-svc/**` (the
copy of the instrument the service executes) and `/var/lib/btc-chainbook/**` (the new capture).
Nothing else, asserted before every open (§7 V5).

Prohibited, each an abort rather than a warning:

- **P1 — no file under `/var/lib/btc-recorder/` is opened, with one named exemption:**
  `manifest.json`, and only in `--prove` (§3.6). The map's §2.3 reserves that tree — "no TZ opens a
  quote body, a `gamma.json`, a `resolution.json` or a stream of any interval with `T0 > 1789669800`
  except TZ-16" — and excepts the manifest in the same sentence, "because the committed loader reads
  every manifest for every set formation and a manifest carries neither a price nor an outcome."
- **P2 — no label, no outcome, no settled document, live or stored, except the 801 bodies of
  `/root/tz17-work/raw/`**, whose largest epoch is `1789178400`, `491,400` s below the reserved
  boundary `1789669800`.
- **P3 — no price, spread, size, mid or book level is printed, written to any output file of §8, or
  computed anywhere outside the byte-for-byte store.** The capture stores replies; it does not read
  them. The proof counts them.
- **P4 — no order, no authentication, no credential, no CLOB key, no wallet.** Two GET endpoints
  (§3.2) and nothing else, asserted over the instrument's own syntax tree (§5 S8).
- **P5 — nothing is removed:** no tree, no file, no worktree, no branch. `/root/tz17-work/` is opened
  read-only and is not reclaimed here.
- **P6 — no process is signalled.** The recorder is not stopped, restarted, reniced or touched.
- **P7 — no committed file of the repository is edited**, and no function of any committed file is
  imported or called. The instrument is stdlib-only.

---

## 3. What to build

### 3.1 The instrument

`research/tz18-chainbook-capture.py`, Python 3.12, **standard library only** — `argparse`, `ast`,
`datetime`, `decimal`, `errno`, `gzip`, `hashlib`, `json`, `os`, `re`, `signal`, `sys`, `threading`,
`time`, `urllib`. No `subprocess`, no `shell=True`, no external binary. It refuses to start when
`__debug__` is false, so no count can be hollowed out by `-O`.

Four modes, and no other: `--selftest`, `--verify-tz17`, `--serve`, `--prove`.

### 3.2 The two endpoints, and nothing else

| use | request |
|---|---|
| market document | `GET https://gamma-api.polymarket.com/markets/slug/{slug}` |
| order book | `GET https://clob.polymarket.com/book?token_id={token_id}` |

Both are public and unauthenticated — the map's §6 rows "resolution endpoint" and "CLOB order book,
REST", and both hosts are in §6's verified egress list. TZ-17 issued 801 requests to the first,
including `btc-updown-15m-*`, and every one returned HTTP 200 (its report §1.1), so the 15-minute
slug is known to be served. Exactly two string constants in the file contain `://`, asserted (§5 S8).

### 3.3 The schedule

Windows are the 900-second slots, `T ≡ 0 (mod 900)`. For the window at `T`:

| instant | action |
|---|---|
| `T + 605` | fetch the document of `btc-updown-15m-{T}`, then, ≥ `200` ms later, of `btc-updown-5m-{T+600}`; from each, take `clobTokenIds`, `outcomes` and `conditionId` **exactly as the document carries them** — where a value is a JSON-encoded string, parse it the way §3.7 step 4 parses `eventMetadata` — and require two distinct non-empty ids per market |
| `T + 655` | checkpoint, `tau' = 245` |
| `T + 715` | checkpoint, `tau' = 185` |
| `T + 775` | checkpoint, `tau' = 125` |
| `T + 805` | checkpoint, `tau' = 95` |
| `T + 835` | checkpoint, `tau' = 65` |
| `T + 865` | checkpoint, `tau' = 35` |
| `T + 885` | checkpoint, `tau' = 15` |
| `T + 905` | write `window.json`, close the window |

`tau'` is the seconds remaining to `T + 900`, the instant both markets settle on.

**The five-second offset is deliberate and is not a preference.** Tier C reads the same 5-minute
market at `tau ∈ {240, 180, 120, 90, 60, 30, 10}`, i.e. at `T+660 … T+890` (map §2.3). This capture
fires five seconds earlier at every checkpoint, so the two processes never issue a request in the
same second, and the venue sees `28` added requests per 900 s — `0.031` per second — from this host.

A checkpoint whose instant has already passed when the scheduler reaches it is **not** read and is
recorded as missed, with its scheduled instant; nothing is back-filled and no read is retried into a
later slot (Tier C's rule, map §2.3).

### 3.4 The four reads of a checkpoint

Four GETs — 15m Up, 15m Down, 5m Up, 5m Down — one per token id, each in its own thread. All four
threads are created and started before any of them opens a socket, and the checkpoint waits for all
four with a deadline of `5.0` s per read. Each thread records, for its own read:

`send_mono_ns`, `recv_mono_ns`, `recv_wall_ns`, the HTTP status (null when no reply arrived), the
body **verbatim and unparsed**, its byte count and its SHA-256.

No retry inside a checkpoint. The checkpoint's **skew** is `max(recv_mono_ns) − min(recv_mono_ns)`
over the four reads that produced a reply, recorded in nanoseconds.

If the window's documents did not yield token ids, the four entries are still written, with status
null and `reason: "no_token_ids"`, so that §4's gate counts them as the failures they are.

### 3.5 Storage — verbatim, never re-serialised

Root `/var/lib/btc-chainbook/`, one directory per window, named `{T}`:

| file | content |
|---|---|
| `documents.jsonl` | 2 lines, one per market document: `{slug, url, status, send_mono_ns, recv_mono_ns, recv_wall_ns, bytes, sha256, raw}` — `raw` is the body exactly as received, carried as a JSON string |
| `books.jsonl.gz` | 28 lines, the same fields plus `{T, tau_prime, market, token_id, outcome_label, reason}` |
| `window.json` | written at `T+905`: counts and timings only — per-status counts, the seven skews in ns, `documents_ok`, `checkpoints_complete`, and `clobTokenIds`, `outcomes` and `conditionId` per market, verbatim as read |

`outcome_label` in `books.jsonl.gz` is the **positional** pairing of `clobTokenIds` with `outcomes`
and is advisory only: the map's §6 venue-constants row resolves the outcome mapping from
`tokens[].outcome` and not from array position, so the TZ that scores these books resolves it there
and never depends on this field.

`/var/lib/btc-chainbook/runtime.jsonl` carries one `start` record per process start —
`{event, pid, wall_ns, mono_ns, commit, file_sha256, argv, config}` — and one `stop` record on
SIGTERM. Gzip is written with `mtime=0` and a fixed compression level `6`, so a window's file is a
pure function of its lines.

**A gap is recorded, never filled.** A missed checkpoint, a null status, a short body: each is stored
as it happened.

### 3.6 The interlock that protects the existing capture

Tier C is Phase 2's input and this TZ adds load to the same host and the same venue. `--prove`
therefore reads, for every interval directory of `/var/lib/btc-recorder/` whose `T0 + 300` falls
inside the proof window, **only `manifest.json`**, and prints `quotes_complete` and `complete` for
each. It prints the same two counts over the control window of equal length ending at the start
record. An open guard records every path opened under that root and asserts that every basename is
`manifest.json` (§7 V6).

### 3.7 `--verify-tz17` — the direct settlement identity, offline

No network. Read-only on `/root/tz17-work/raw/`.

1. Read `CryptoReports/TZ-17-settlement-chain-report.md` from the worktree. Take the text between the
   first line equal to ` ```csv ` and the next line equal to ` ``` `, exactly as it stands, ending
   with its own final newline. **Assert its SHA-256 equals
   `96b5e21e2cc59e2f3bde332d60457533158bd16c2eeaaaba844bf35b1efc63ee`**, `99,075` bytes, `201` lines.
2. Parse it. For each of the 200 rows, form five slugs — `btc-updown-15m-{T}` and
   `btc-updown-5m-{T}`, `{T+300}`, `{T+600}`, `{T+900}` — and take the five SHA-256 columns
   `sha_M15`, `sha_M5a`, `sha_M5b`, `sha_M5c`, `sha_M5d` as those bodies' expected hashes.
3. For each of the `801` distinct slugs: read `/root/tz17-work/raw/{slug}.body`, hash it, **assert it
   equals the CSV's value**. `801` of `801`, or abort.
4. Parse each body with `json.loads(body, parse_float=decimal.Decimal)`. Locate
   `events[0].eventMetadata`; where that value is a string, parse it the same way. Require a mapping
   whose key set is exactly `{"priceToBeat", "finalPrice"}` — TZ-17's report §2.7 measured those two
   keys and no others at 801 of 801 documents. Convert each value to `Decimal`: a `Decimal` stays, an
   `int` goes through `Decimal(value)`, a `str` through `Decimal(value)`; any other type marks that
   unit `type_error`, which counts as a failure of its identity and is disclosed.
5. Compute three identities, by exact `Decimal` value:

| identity | units | statement |
|---|---|---|
| **Q1** | `600` | `finalPrice` of the 5-minute market at slot `i` equals `priceToBeat` of the 5-minute market at slot `i+1`, over the 601 contiguous 300-second slots the stored set forms |
| **Q2** | `200` | `finalPrice` of `btc-updown-15m-{T}` equals `priceToBeat` of `btc-updown-5m-{T+900}` |
| **Q3** | `200` | `finalPrice` of `btc-updown-15m-{T}` equals `finalPrice` of `btc-updown-5m-{T+600}` |

   Report, per identity, both the count equal by **value** and the count equal as a **printed
   literal**; §4 gates on value.
6. Write `/root/tz18-work/tz18-verify.csv` — one row per unit: identity, index, the two slugs, the
   two literals as `str(Decimal)`, the equality flag, the difference, and the two body SHA-256s — and
   `/root/tz18-work/tz18-verify.json` with the counts. Any single row is reconstructible from the two
   named bodies without re-running anything.

### 3.8 The service

The Executor copies the instrument to `/root/tz18-svc/tz18-chainbook-capture.py` and asserts the
copy's SHA-256 equals the committed blob's, then starts it detached:

```
setsid nohup /root/tz01-env/venv/bin/python -B -u \
  /root/tz18-svc/tz18-chainbook-capture.py --serve \
  >> /var/lib/btc-chainbook/service.log 2>&1 &
```

The copy exists so the service does not depend on a worktree a later TZ will reclaim; the start
record carries both the branch commit and the file's SHA-256, so what is running is never in doubt.

**Single instance:** on start the instrument creates `/var/lib/btc-chainbook/service.pid` with
`O_CREAT | O_EXCL`. If the file exists it reads the pid and `/proc/{pid}/cmdline`; if that command
line is this service's, it exits without writing anything; otherwise it replaces the file. On SIGTERM
it writes a `stop` record, closes the open window's files and exits. **This TZ sends it no signal.**

### 3.9 Cost, in exact units

| quantity | figure | derivation |
|---|---|---|
| requests per window | `30` | 28 book reads + 2 documents |
| requests per day | `2,880` | `30 × 96` windows |
| added venue rate | `0.033` req/s | `2,880 / 86,400` |
| stored bytes per day | `≈ 1,185,408` books + `≈ 193,843` documents | Tier C stores `6,171.5` bytes per 14 reads (map §2.3) → `441` per read, `× 2,688`; documents at TZ-17's measured mean body `5,048` bytes, gzip-free, `× 192`, taken at one fifth after compression |
| block rounding | `≈ 1,572,864` bytes/day | `96` windows × `4` files × `4,096` |
| **total on disk** | **`≈ 3.0` MB/day** | sum, rounded up |
| against headroom | `11,513,277,440` bytes above the floor at TZ-17's closing `df` | `3` MB/day is `0.009%` of it per day |
| write cap, asserted | `200,000,000` bytes for everything this TZ writes in the session | asserted as it writes and again at the end |

---

## 4. The gates, fixed here, before any of their data exists

Three readings. **None gates another**, and no row below moves after a number is known.

### G-DEPLOY — does the capture record both books at one instant?

- **Unit:** a checkpoint. **Qualifying:** its window's document instant `T + 605` is ≥ `start_wall + 60` s
  **and** its own scheduled instant is ≤ `start_wall + 3,900` s, where `start_wall` is the service's
  `start` record. A window already under way when the service starts has no document fetch and
  therefore contributes no unit — a property of the schedule, not of any outcome; every such
  checkpoint is still disclosed with that reason.
- **Complete:** four stored replies, all HTTP 200, each body non-empty and parsing as JSON, and a
  skew ≤ `1,000,000,000` ns.
- **Reading:** of the **first 14 qualifying checkpoints**, **≥ 13 complete → PASS**; **≤ 12 → FAIL**;
  **fewer than 14 qualifying checkpoints by the budget end → UNDECIDABLE**, with every checkpoint
  considered disclosed in order.
- **False-failure probability under a capture that loses nothing: exactly `0`.** Family-wise over one
  statistic on one set: `0`.
- **Power**, against a per-checkpoint failure rate, computed exactly as
  `1 − (1−p)^14 − 14·p·(1−p)^13`:

| alternative | power |
|---|---|
| `p = 0.25` | `0.899031627923250198364257812500` |
| `p = 0.10` | `0.415370859484330000000000000000` |
| `p = 0.05` | `0.152985562588816560668945312500` |

  **A deployment proof is not sized to see a low loss rate**, and this one does not claim to: at 5%
  it fails to notice five times in six. The measurement TZ re-reads completeness over its whole set
  before it scores anything.

### G-TIERC — did the new capture disturb the old one? (safety interlock)

Every 5-minute interval of `/var/lib/btc-recorder/` whose `T0 + 300` lies inside the proof window and
whose `manifest.json` exists must carry `quotes_complete` true. **One false → FAIL, the service is
stopped in the same session** by the block of §6 R5, and the report says so in its first line.
False-failure `0` under "the new capture does not disturb the old one". No power is claimed: this is
an interlock, not a measurement, and the control window is printed beside it.

### G-CHAIN — is the settlement reading the same published number for both families?

- **Reading:** `Q1 ≥ 599` of `600` **and** `Q2 ≥ 199` of `200` **and** `Q3 ≥ 199` of `200` → **PASS**.
  Any identity at or below `n − 2` → **FAIL**. Every mismatch is printed with its difference.
- **False-failure under "each boundary has one published reading": exactly `0`.** Family-wise over
  three identities on one set of documents: `0`.
- **Power**, exactly `1 − (1−p)^n − n·p·(1−p)^(n−1)`:

| identity | `p = 0.02` | smaller alternative |
|---|---|---|
| Q1, `n = 600` | `0.999927940037418865985964653194` | `p = 0.005`: `0.801599779568236533442873619078` |
| Q2 and Q3, `n = 200` | `0.910624516228067965960219332490` | `p = 0.01`: `0.595354315327973499366704428681` |

**What a PASS means, fixed before the data:** the 15-minute market and the 5-minute market inside it
are settled from the same published number, exactly, so the nesting of their outcomes is exact rather
than approximate, and a later TZ may treat the constraint as model-free. **What it does not mean:**
nothing about any price, any book, any edge. A FAIL means TZ-17's outcome agreement rests on margins
rather than on identity, and the backup track's next TZ is rewritten before it is run.

---

## 5. Self-tests — `--selftest`, before anything else

Each item is an `assert` through one counting helper, and the mode prints `n of n` where `n` is the
count the run returns, never a literal.

| item | asserts | what |
|---|---|---|
| **S1** | `4` | the schedule of §3.3 at `T = 1790035200`: document instant `1790035805`; the seven checkpoint instants `1790035855`, `1790035915`, `1790035975`, `1790036005`, `1790036035`, `1790036065`, `1790036085`; every one strictly inside `(T+600, T+900)`; and none equal to any Tier C instant `1790035860`, `1790035920`, `1790035980`, `1790036010`, `1790036040`, `1790036070`, `1790036090` |
| **S2** | `3` | qualifying and completeness of §4 on synthetic checkpoint records: four 200s with skew `999,999,999` ns is complete; the same with skew `1,000,000,001` ns is not; one status 429 among four is not |
| **S3** | `3` | `json.loads(…, parse_float=Decimal)` on a body carrying `76994.84244708234` returns that exact literal; a `str` value and an `int` value convert; a `list` value marks `type_error` |
| **S4** | `4` | the three identities on synthetic pairs: equal literals hold; literals differing by `1E-9` fail and report that difference; equal value with unequal printed literal (`1.10` against `1.1`) counts in the value column and not in the literal column |
| **S5** | `3` | the write guard: a path under `/root/tz18-work/`, `/root/tz18-svc/` and `/var/lib/btc-chainbook/` opens; `/root/btc-5m-twap/x` raises; `/var/lib/btc-recorder/x` raises |
| **S6** | `4` | the readings of §4 on synthetic counts: `(14, 13) → PASS`; `(14, 12) → FAIL`; `(13 qualifying) → UNDECIDABLE`; `Q1 598 → FAIL` |
| **S7** | `7` | the seven power literals of §4, recomputed in exact `Fraction` arithmetic and compared to this TZ's strings at a tolerance of `1E-18` |
| **S8** | `5` | over the instrument's own `ast`: every imported top-level module is in `sys.stdlib_module_names`; none is `subprocess`; no attribute `system`, `popen`, or any name starting `spawn` or `exec`, is taken on `os`; no call carries a keyword `shell`; **exactly two string constants contain `:` `/` `/`**, equal to §3.2's two endpoints, the needle assembled from separate literals so that it is not a third match |

**Total: `33`.** A failure aborts; the mode prints the count it counted.

---

## 6. Runs, in this order

| run | what | where |
|---|---|---|
| **R0** | `--selftest` | before the first network request and before any file but the instrument's own source is read |
| **R1** | `--verify-tz17` → `/root/tz18-work/run-1/` | offline; no socket is opened, asserted |
| **R2** | copy to `/root/tz18-svc/`, assert the hash, start the service (§3.8), print the `start` record | the service begins scheduling |
| **R3** | wait to the budget end, `3,900` s after `start_wall`, or until the 14th qualifying checkpoint has been written, whichever comes first | the Executor sleeps; it does not poll the venue |
| **R4** | `--prove` → `/root/tz18-work/run-2/` — §4's three readings, §3.6's interlock, the disclosure of every checkpoint considered | reads only `/var/lib/btc-chainbook/**` and `manifest.json` |
| **R5** | **only if G-TIERC reads FAIL:** stop the service with the one block the report quotes, verify from `runtime.jsonl` and `/proc` that it is gone, and report FAIL | — |
| **R6** | `--verify-tz17` again → `/root/tz18-work/run-3/`, asserted byte-identical to R1's two outputs | determinism |

Before each of R1, R4 and R6, assert `git rev-parse HEAD` equals
`git rev-parse origin/tz-18-chainbook-capture`, and print the exit code.

The three §0.2 host reads and `df` are taken again at the end of the session and printed beside the
opening ones. **Compute, not wall clock, is bounded:** R0, R1, R4 and R6 together are under `120` s
(§10, C4); R3 is a sleep and the session's wall clock is bounded at `3,900` s from the start record.

---

## 7. Validation

Every row is an `assert` that aborts the run, unless it says otherwise in plain words. Counts are
derived from the run, never typed.

| # | row | runs |
|---|---|---|
| **V1** | the fingerprint gate: revision equal, 6 of 6 anchors, 24 of 24 rows hashed, 22 of 22 `frozen` equal | R1, R4, R6 |
| **V2** | host and resource gates: H1, H2, H3 printed verbatim and compared by the Executor; `avail ≥ 2,200,000,000` asserted inside the instrument at each run | §0, R1, R4, R6 |
| **V3** | the CSV extracted from the committed TZ-17 report hashes to `96b5e21e…`, `99,075` bytes, `201` lines | R1, R6 |
| **V4** | `801` of `801` stored bodies re-hash to the CSV's value | R1, R6 |
| **V5** | the write guard: every open for writing is checked against the three allowed roots before the open; the count of checks is printed | all |
| **V6** | the open guard: every path opened under `/var/lib/btc-recorder/` has basename `manifest.json`; the count is printed; in R1 and R6 that count is **`0`** | R4 / R1, R6 |
| **V7** | R1 opens no socket: the instrument asserts, in `--verify-tz17`, that its own request counter is `0` at exit | R1, R6 |
| **V8** | determinism: `tz18-verify.csv` and `tz18-verify.json` byte-identical between R1 and R6, `cmp` clean, two fresh processes from the same commit | R6 |
| **V9** | every checkpoint the proof considered is disclosed in order, qualifying and non-qualifying alike, with the reason each non-qualifier was excluded and, for each incomplete one, the four statuses and the skew | R4 |
| **V10** | the four reads of a checkpoint are issued concurrently: the instrument asserts at every checkpoint that the last `send_mono_ns` precedes the first `recv_mono_ns` of the four, and prints the count of checkpoints where it does not | R4 |
| **V11** | no price leaves the store: the key sets of `window.json`, `tz18-proof.json` and `tz18-verify.json` are fixed allow-lists in the source, asserted before each file is written, and none contains a book level, size or mid | all |
| **V12** | the service's `start` record carries the branch commit and the file SHA-256, and the running `/proc/{pid}/cmdline` equals the argv of §3.8 | R2, and again at the session end |
| **V13** | the write cap: the session's own bytes written are summed as they are written and asserted `≤ 200,000,000`, printed at the end | all |
| **V14** | the branch diff names exactly one path — `git diff --name-only origin/main origin/tz-18-chainbook-capture` — printed verbatim, after the branch push and before the report commit | after push |
| **V15** | the mandatory separation self-check, printed verbatim, run after the branch push and before the report commit: `main` does not carry the implementation commit, the branch differs from `main` by that one path, and no `.parquet` or `.zip` is in git history | after push |

---

## 8. What the report prints

`CryptoReports/TZ-18-chainbook-capture-deploy-report.md`, pushed straight to `main` from
`/root/tz18-work/wt-report`, and the implementation left on its branch with a pull request, unmerged.

1. The three readings — **G-DEPLOY**, **G-TIERC**, **G-CHAIN** — each in one line with its deciding
   count, in the first ten lines of the file.
2. §0's fingerprint, host and repository reads, verbatim, opening and closing.
3. The service: pid, argv, start record, file SHA-256, branch commit, and the closing `/proc` read.
4. **G-DEPLOY's full disclosure:** every checkpoint considered, in order — window `T`, `tau'`,
   qualifying or not with the reason, the four statuses, the four `recv_mono_ns` deltas from the
   first, and the skew. Counts of complete, incomplete and missed.
5. The seven skews per window in nanoseconds, with their minimum, median and maximum over the proof —
   **the number the next TZ will size its pairing rule from.**
6. **G-TIERC:** the two windows, interval by interval, with `quotes_complete` and `complete`.
7. **G-CHAIN:** `Q1`, `Q2`, `Q3` by value and by literal, every mismatch with its difference and its
   two slugs, and the `tz18-verify.csv` hash, line count and byte count. If every unit holds, say so
   as a count, never as "all checks passed".
8. Request accounting: attempts, statuses, retries (`0` by construction), bytes written, the write-cap
   figure, and the `df` deltas.
9. V1 … V15, each with the count it asserted and the runs it held on.
10. **What could not be implemented as written**, item by item, with the reading the Executor applied.

Any single row of the report is re-derivable by the Architect from `tz18-verify.csv`,
`tz18-proof.json` and the stored bodies, without re-running the pipeline.

---

## 9. Retention, and the reserve this capture inherits

- **Nothing is removed by this TZ** — not `/root/tz17-work/`, not a worktree, not a branch. `P5`.
- `/root/tz18-work/` and `/root/tz18-svc/` stay; `/root/tz18-svc/` is **not** scratch, because the
  service executes from it, and no later TZ removes it while the service runs.
- **The new capture is reserved on the same terms as Tier C's:** no TZ opens a body under
  `/var/lib/btc-chainbook/`, and no report prints a price, size or spread from it, before the TZ that
  scores it — which is written only after TZ-16's first reading is on `main`. `window.json` and
  `runtime.jsonl` are excepted, because they carry counts and timings and neither a price nor an
  outcome.
- Nothing of the capture enters git history, ever.

---

## 10. Pre-send checks

Performed against this file, start to end, as a separate reading after §9 was written.

**C1 — scope against body.** Repository paths named: `research/tz18-chainbook-capture.py` (written),
`CryptoReports/TZ-18-chainbook-capture-deploy-report.md` (written), `CryptoReports/TZ-17-settlement-chain-report.md`
(read), `research/tz17-settlement-chain.py` (named in one printed count only), `SYSTEM-MAP.md` (read).
Host paths named: `/root/tz18-work/**`, `/root/tz18-svc/**`, `/var/lib/btc-chainbook/**` (written);
`/root/tz17-work/raw/` and `/root/btc-5m-twap` (read); `/var/lib/btc-recorder/**/manifest.json`,
`/root/tz04a-env/`, `/root/tz01-env/`, `/root/PROJECT_GAMING_PS5` (read). **Three intersections with
§2's prohibitions, all three carried as named exemptions written into §2 and §3:** the TZ-17 report
(P7 — read, never edited), `/root/tz17-work/raw/` (P2 — the only settled documents, all below the
reserved boundary), `manifest.json` (P1 — the map's own exception, quoted). No other intersection.

**C2 — origin of every expectation.** Thirty-seven fixed expectations, every one in exactly one of
the two admitted classes. **Twenty-four computed independently by the Architect at 50 significant
digits** — a precision better than their `1E-18` tolerance by more than ten decades: the seven power
figures of §4 (exact `Fraction` binomial tails), the seven checkpoint instants and the seven Tier C
instants of §5 S1, and the CSV's `96b5e21e…`, `99,075` bytes and `201` lines of §3.7 and V3.
**Thirteen quoted from a committed artifact, named:**
`5,048` bytes mean body and the 801 HTTP 200s (TZ-17 report
§1.1), the two `eventMetadata` keys at 801 of 801 (§2.7), the five hash columns and the slug families
(§2.11), `0553061fb9f4…` (the audited copy of that report), `e1883424…` (its §3), Tier C's
`6,171.5` bytes per interval and its seven `tau` (map §2.3), `2,000,000,000`, `31612203008`,
`/dev/vda2`, `4216c0467…`, and the two endpoints (map §6). **No expectation depends on a quantity
this TZ measures:** the write cap, the skew bound, the budget and the resource floor are inequalities
that hold for every admissible value of what is measured, and G-DEPLOY's count is read, never
asserted.

**C3 — shape of every diff.** One file, `research/tz18-chainbook-capture.py`, new. **This check could
not be performed against `origin/main`: the Architect's sandbox refused network egress to
`github.com` on 2026-09-22**, and the web copies of that repository are stale snapshots. It is
therefore mechanical and the Executor's: §0.3's third command must print `0` or the run is BLOCKED.
The words "insertions only" appear nowhere in this TZ.

**C4 — cost of every check.** At the population's upper bound, on the measured rates: `--verify-tz17`
reads and hashes `801` bodies of `5,048` bytes mean — `4.4` MB, under `2` s — parses `801` JSON
documents at `~2` ms each, `≈ 1.6` s, and compares `1,000` units, under `0.1` s; `--prove` reads at
most `3` windows' `84` stored replies and at most `20` manifests, under `5` s; `--selftest` is `33`
asserts over synthetic values, under `1` s. Summed over R0, R1, R4 and R6: **under `120` s of
single-session compute**, against the `3,600` s ceiling. R3 is a sleep, not compute, and is bounded
at `3,900` s of wall clock by the budget in §4 and §6, which is also the term every fail-fast bound is
derived from: a window contributes `7` checkpoints and the first fully covered window begins at most
`900` s after the start record, so the `14` units the gate needs are complete at most `2,705` s after
it — `900 + 905 + 900` — inside the `3,900` s budget, which itself admits at most `35`.

**C5 — every count.** Re-derived from the sets §3 and §4 define: `801` distinct slugs = `200`
15-minute + `601` 5-minute, the latter the `601` contiguous 300-second slots from `1788998400` to
`1789178400`; `600` Q1 pairs = `601 − 1`; `200` Q2 and `200` Q3, one per window; `28` reads per window
= `4 × 7`; `30` requests per window = `28 + 2`; `2,880` per day = `30 × 96`; `14` qualifying
checkpoints = the gate's own unit count; `33` self-test asserts = `4+3+3+4+3+4+7+5`; `24` fingerprint
rows and `22` frozen, from the map's §0 table as it stands at `2026-09-19-c`.

**C6 — every population.** G-DEPLOY: the first 14 qualifying checkpoints. G-TIERC: the 5-minute
intervals of the existing capture closing inside the proof window, and the control window of equal
length before the start record. G-CHAIN: Q1 over the 600 consecutive 5-minute slot pairs, Q2 and Q3
over the 200 windows. Skew statistics: every checkpoint that produced four replies. Request
accounting: every attempt of the session. The write-cap figure: every byte this session writes.

**C7 — every signature and every behaviour.** **This TZ names no committed function and imports
nothing from the repository.** The instrument is stdlib-only (§3.1) and every behaviour it relies on
is its own, specified here. There is therefore no signature to quote and no committed body to read —
which is also why C7 survives the egress failure that C3 did not.

**C8 — every cross-reference.** Resolved by reading the referenced text, not from memory: CANON
§1.1 (settlement mechanics, the taker fee, the 15-minute markets' 60-second feed), §1.6 (what is
closed), PART II (gates fixed before data, and what UNDECIDABLE closes), PART III hard rules 1, 2, 8,
9, 10 and 11, and PART III's CODE standard on verbatim capture; map §0 (revision, anchors, table),
§2.3 (Tier C's seven `tau`, the per-interval byte figures, the reserved span and its `manifest.json`
exception, quoted in §2), §6 (host identity, disk floor, interpreter, egress list, the two endpoints,
venue constants, the sandbox's classifier limits); TZ-17's report §1.1, §2.7, §2.11, §3 and §6 item 4.
**Not referenced anywhere in this TZ: `BTC-EXECUTOR-INSTRUCTIONS.md`** — the Architect could not read
it in this session, so this TZ names no section of it and states every requirement of its own
mechanically. The contract governs the Executor regardless, and where it and this TZ disagree, the
Executor reports BLOCKED rather than choosing.
