# TZ-17 — The settlement chain: do the 15-minute and 5-minute markets settle on one reading?

| field | value |
|---|---|
| canonical filename | `CryptoTZ/TZ-17-settlement-chain.md` |
| report | `CryptoReports/TZ-17-settlement-chain-report.md` |
| branch | `tz-17-settlement-chain`, adding exactly one path: `research/tz17-settlement-chain.py` |
| Executor model | **Opus** — network capture and gate arithmetic |
| written | 2026-09-22, by the Architect. Supersedes nothing. Reads no Phase 2 input. |

**Fingerprint gate.** `SYSTEM-MAP.md` on `main` carries revision `2026-09-19-c` and these anchors,
or the run is BLOCKED before any work. Every `frozen` row of the map's §0 fingerprint table — 22
rows — hashes to its printed value, or BLOCKED.

| anchor | required |
|---|---|
| `A1` | `229a944f2d51` |
| `A2` | `6c5089330629` |
| `A3` | `0-complete / 1-student-5tau-not-disqualified / 2-undecidable-5tau` |
| `A4` | `437b45ea196b` |
| `A5` | `9fd1c7de0f74` |
| `A6` | `729f0bcdbee3` |

**Host gate** — System Map §6, "host identity". All three, or BLOCKED:

- **H1** `/var/lib/btc-recorder/` exists and holds interval directories;
- **H2** a recorder process is running, and a `runtime.jsonl` under `/var/lib/btc-recorder/`
  carries sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`;
- **H3** the filesystem holding `/var/lib/btc-recorder/` is `/dev/vda2`, total
  `31,612,203,008` bytes.

H2 checks that the sha occurs, not that the newest start record carries it, as §6's own wording
has it: this TZ reads no capture and depends on the host, not on the commit the recorder runs.

**Resource gate** — System Map §6, disk row: available space on that filesystem is at least
`2,200,000,000` bytes — the map's `2,000,000,000` floor plus this TZ's own write cap of
`200,000,000` bytes (§2 P6).

---

## 0. Start-up

Contract §1, steps 1–5, first. Then, in this order, from `/root/btc-5m-twap`:

```
df -B1 --output=source,size,avail /var/lib/btc-recorder
find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
pgrep -af recorder
grep -rl --include=runtime.jsonl 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder | head -n 1
du -sb /root/PROJECT_GAMING_PS5
systemctl is-enabled telemetry-watch.service; echo "exit=$?"
systemctl is-active telemetry-watch.service; echo "exit=$?"
test -e /root/tz14-work; echo "tz14-work exit=$?"
test -e /root/tz15-work; echo "tz15-work exit=$?"
git worktree list
```

H1 holds iff `find` prints one path. H2 holds iff `pgrep` prints at least one line and `grep`
prints one path. H3 holds iff `df` prints source `/dev/vda2` and size `31612203008`. The resource
gate holds iff `df` prints `avail` of at least `2200000000`. Every line of output goes into the
report's §0 verbatim. The `du` and `systemctl` reads are the three reads System Map §6 requires of
every TZ; they carry no threshold here.

Then create the two worktrees and work only in them:

```
git fetch origin
git worktree add -b tz-17-settlement-chain /root/tz17-work/wt origin/main
git worktree add --detach /root/tz17-work/wt-report origin/main
```

The implementation is written, committed and pushed from `/root/tz17-work/wt`. The report is
committed from `/root/tz17-work/wt-report` and pushed with `git push origin HEAD:main`. This
replaces the `git checkout` lines of contract §4.1 for this task only; the separation it protects
is asserted unchanged by V11.

---

## 1. Purpose

**The backup track, first step.** If the 15-minute market `btc-updown-15m-{T}` and the 5-minute
market `btc-updown-5m-{T+600}` resolve on one and the same reading of the Chainlink 60-second TWAP
feed at `T+900`, then during `[T+600, T+900]` they are two digital contracts on a single number
with two strikes — `K15(T)`, fixed ten minutes earlier, and `K5(T+600)`. Their prices are then
bound by monotonicity in the strike: where `K15(T) < K5(T+600)`, "Up" on the 15-minute market
pays in every state in which "Up" on the 5-minute market pays. That relation needs no model and no
`sigma`.

CANON §1.1 says the 15-minute markets read the 60-second feed and the 5-minute markets have read
it since 2026-08-14. That is documentation. CANON §1.1's standing rule admits a venue mechanic only
by measurement against resolved outcomes, and this TZ is that measurement. It uses only the
venue's own published documents — prices to beat and resolved outcomes — fetched from the public
Gamma API for markets that closed between 2026-09-10 and 2026-09-14. It computes no probability,
calls no pricer, opens no order book and no capture file, and requests nothing from TZ-16's
reserved span.

What each reading of §4 means, fixed now:

| reading | meaning |
|---|---|
| **PASS** | the two market types settle on one reading at a shared boundary. The next step needs both books read at the same instants; it is a deployment TZ followed by a measurement TZ, never this one. |
| **FAIL** | they do not; the backup track closes. |
| **UNDECIDABLE** | fewer than 200 windows qualify among the 400 considered; nothing closes. |

---

## 2. Scope

**Allowed changes:** one new file on branch `tz-17-settlement-chain`,
`research/tz17-settlement-chain.py`, and the report on `main`. The committed lines the new file
replaces: none — the path is in neither the map's §0 fingerprint table nor its §3 code table, and
V10 asserts the diff names it alone. This change is insertions only.

**Prohibitions:**

- **P1** No committed file is edited and no `frozen` row moves.
- **P2** The instrument makes no request to any host but `gamma-api.polymarket.com`, and to no
  path but `/markets/slug/btc-updown-15m-{T}` and `/markets/slug/btc-updown-5m-{t}` with `T` and
  `t` from §3.3. Nothing this TZ runs makes an authenticated venue call, holds a credential, places
  an order, or opens a CLOB, RTDS or websocket connection.
- **P3** No request for a 5-minute market with `t > 1789669800`, and none for a 15-minute market
  with `T + 900 > 1789669800` — TZ-16's reserved span, System Map §2.3. Checked before every
  request.
- **P4** The instrument opens no file under `/var/lib/btc-recorder/`. **Exempt:** the two
  host-gate commands of §0 — `find` lists paths and opens no file; `grep` reads `runtime.jsonl`
  files for one sha string. Nothing this TZ runs opens a `gamma.json`, a `resolution.json`, a quote
  file or a stream of any interval.
- **P5** The instrument imports nothing from `research/` and no package outside the standard
  library, and runs on `/root/tz01-env/venv/bin/python`. It contains no `subprocess`, `os.system`,
  `os.popen`, `os.exec*`, `os.spawn*` or `shell` keyword; S9 asserts this over its own syntax tree.
- **P6** Every file the instrument opens for writing lies under `/root/tz17-work/` and outside
  both worktrees, asserted before each open. R1 writes at most `200,000,000` bytes in total,
  asserted as it writes.
- **P7** No tree is removed. Nothing under `/root/tz14-work/`, `/root/tz15-work/`,
  `/root/btc-forensics/`, `/root/tz01-env/` or `/root/tz04a-env/` is modified; `/root/tz15-work/`
  is TZ-16's to reclaim, System Map §3. The recorder is not stopped, restarted or signalled.

Exempt from P4: the two §0 commands named in it. Outside P2 by its own wording: the Executor's
`git fetch` and `git push` to `origin`, which the contract requires. Exempt from P1, P3 and P5 to
P7: nothing.

---

## 3. Definitions and method

`decimal` context precision 60, as System Map §6 fixes for every price. Epochs are UTC seconds,
written as decimal ASCII integers; epochs are the authority for every membership and span.

### 3.1 Markets and fields

- `M15(T)`: slug `btc-updown-15m-{T}`, `T` a multiple of 900. `M5(t)`: slug
  `btc-updown-5m-{t}`, `t` a multiple of 300. Both are functions `slug15(T)` and `slug5(t)`.
- Request: `GET https://gamma-api.polymarket.com/markets/slug/{slug}`, headers
  `Accept: application/json` and `User-Agent: btc-5m-twap-tz17`, timeout 20 s. System Map §6 names
  this endpoint for the 5-minute market. That it serves the 15-minute slug is not yet measured;
  §3.3's early stop turns a path that does not into a BLOCKED report within 41 requests —
  10 for `M15` and 31 for the distinct `M5` of candidates 0 to 9.
- A document is the response body parsed by `json.loads(body, parse_float=Decimal)`.
- `K(doc)` — the price to beat, CANON §1.1 — is `doc["events"][0]["eventMetadata"]["priceToBeat"]`:
  a JSON number taken as `Decimal(str(value))` of the parsed value, or a string matching
  `^[0-9]+\.[0-9]+$` converted by `Decimal`.
- `O(doc)` — the resolved outcome: `outcomes` and `outcomePrices`, each a list or a JSON-encoded
  string of one, both of length 2; the outcome strings are exactly `{"Up", "Down"}`; each price
  converted by `Decimal(str(price))`; exactly one equals `1` and the other `0`. `O` is the outcome
  string whose price is `1`. Mapped by string, never by position, as System Map §6 records.

### 3.2 Validity of one document

`validity(status, doc, slug)` returns the first failing code, in this order, or `ok`:

| code | condition |
|---|---|
| `fetch` | no HTTP response after the retries of §3.4 |
| `absent` | HTTP 404 |
| `status` | any other status but 200 |
| `json` | the body does not parse as a JSON object |
| `slug` | `doc["slug"] != slug` |
| `open` | `doc["closed"] is not True` |
| `no-ptb` | `K(doc)` absent or not convertible |
| `ptb-range` | `K(doc)` not finite, or `<= 0` |
| `precision` | `K(doc).as_tuple().exponent > -2` — fewer than two decimal places |
| `unresolved` | `O(doc)` not determined by §3.1 |

### 3.3 Candidates, qualification and the set

- Candidate `k`, for `k = 0, 1, …, 399`: `T_k = 1788998400 + 900·k`, from 2026-09-10 00:00:00 UTC.
  The last, `T_399 = 1789357500`, needs `M5(1789358400)`, the largest epoch this TZ can request —
  below the reserved boundary `1789669800`.
- A candidate's **gate documents** are `M15(T)`, `M5(T)`, `M5(T+600)` and `M5(T+900)`; its
  **disclosure document** is `M5(T+300)`.
- **A candidate qualifies iff its four gate documents read `ok`.** Qualification reads no identity
  of §3.5, so no selection on the gate is possible.
- **The set is the first 200 qualifying candidates in increasing `k`.** Stage F stops fetching once
  the 200th qualifies. If candidates 0 to 399 yield fewer than 200, the set cannot be formed and §4
  reads UNDECIDABLE.
- **Early stop:** if none of candidates 0 to 9 qualifies, Stage F stops and the run is BLOCKED. The
  BLOCKED report prints, for candidate 0: each request's status, each body's JSON type, and for an
  object its top-level key names and the key names of `events[0]` and of
  `events[0]["eventMetadata"]`, with each reason code.

### 3.4 Fetching — Stage F

- **Order.** Candidates in increasing `k`; within one, `M15(T)`, `M5(T)`, `M5(T+300)`, `M5(T+600)`,
  `M5(T+900)`. A slug already fetched is not requested again: `M5(T+900)` of candidate `k` is
  `M5(T)` of candidate `k+1`.
- **Pacing.** Request starts at least 0.5 s apart.
- **Retries.** On HTTP 429, any 5xx or a transport error: up to 3 more attempts, after waits of 5,
  10 and 20 s, or after `Retry-After` when present, capped at 60 s. A 404 or any other 4xx is not
  retried.
- **Storage.** The final attempt's body, byte for byte, as `/root/tz17-work/raw/{slug}.body`, and
  one line per attempt in `/root/tz17-work/index.jsonl`: `slug`, `attempt`, `status` or `null`,
  `error` (exception class name) or `null`, `bytes`, `sha256` of the body, `t_utc` (ISO 8601 with
  milliseconds) and `elapsed_ms`. Gaps are recorded, never filled.
- **Fail-fast.** Stage F stops, BLOCKED, if 20 consecutive requests end in `fetch` or `status`
  after their retries, or if its wall clock since the first request passes 2,700 s (§10 C4).
- **Stability re-fetch.** Once the set is formed, the four gate documents of the first 10 members —
  40 requests, under the same pacing and retries — are fetched once more into
  `/root/tz17-work/refetch/{slug}.body`, one line per attempt in `/root/tz17-work/refetch.jsonl`.
  V8 compares them.
- **R1's own summary**, `/root/tz17-work/fetch-summary.json`: requests by status and market type,
  retries, the wall clock, bytes written, the candidates considered, the member list and its
  SHA-256. It carries no key named `I1`, `I2`, `I3`, `holds` or `N`, asserted at R1's end.

### 3.5 Identities — Stage A

For each member `T`: `K15 = K(M15(T))`, `K5a = K(M5(T))`, `K5c = K(M5(T+600))`,
`K5d = K(M5(T+900))`, `O15 = O(M15(T))`, `O5c = O(M5(T+600))`.

- **I1 — one reading at the shared open:** `|K15 − K5a| < 10^E`, where
  `E = max(exponent(K15), exponent(K5a))` and `exponent(x)` is `x.as_tuple().exponent` — equality
  to the precision the coarser of the two published literals carries.
- **I2 — the 15-minute market settles on the reading at `T+900`:** `O15 == "Up"` iff `K5d >= K15`.
- **I3 — the 5-minute market closing at `T+900` settles on the same reading:** `O5c == "Up"` iff
  `K5d >= K5c`.
- A member **holds** iff I1, I2 and I3 all hold. **`N`** is the number of members that hold.

`K5d` stands for the reading at `T+900` because `M5(T+900)` opens there and its price to beat is
the 60-second feed's reading at its open — CANON §1.1, and System Map §4's row for it, TZ-04b V1
198 of 200 and TZ-06 V3 396 of 400. I2 and I3 then ask whether both outcomes are those of that one
number. Both market types resolve "Up" when the close is at or above the price to beat.

### 3.6 Disclosure — no threshold

- **D1** `I1_exact`: members with `K15 == K5a` as `Decimal`s, and their count.
- **D2** the chain inside the window, over the members whose `M5(T+300)` reads `ok`, with
  `K5b = K(M5(T+300))`: **I4a** `O(M5(T)) == "Up"` iff `K5b >= K5a`; **I4b**
  `O(M5(T+300)) == "Up"` iff `K5c >= K5b`. Holds out of checks for each, and beside them the count
  of members left out because `M5(T+300)` is not `ok` — those members leave the denominator.
- **D3** the distribution of `exponent` over each of the four gate literals, over all members.
- **D4** near-strike members: `|K5d − K15| < 1` USD, and separately `|K5d − K5c| < 1` USD — the
  members where a reading offset under a dollar could flip I2 or I3.
- **D5** per market type, the union of the key names of `events[0]["eventMetadata"]` over every
  `ok` document, each with its count.
- **D6** per market type, the distinct values of `doc["resolutionSource"]` over every `ok`
  document, each truncated to 200 characters, with counts; a missing key is counted as `absent`.
- **D7** for every candidate considered that is not a member, the code of its first gate document
  that is not `ok` in §3.4's order; counts per code.

### 3.7 Outputs of Stage A

Written into the directory given by `--out`, each a pure function of `/root/tz17-work/raw/` and
`/root/tz17-work/index.jsonl`:

- `tz17-candidates.csv` — one line per candidate considered, in increasing `k`, header
  `k,T,member,reason,K15,K5a,K5c,K5d,O15,O5c,I1,I2,I3,holds,I1_exact,K5b,O5a,O5b,I4a,I4b,d15,d5,sha_M15,sha_M5a,sha_M5b,sha_M5c,sha_M5d`,
  where `d15 = K5d − K15`, `d5 = K5d − K5c`, `sha_*` the SHA-256 of each stored body, literals
  printed as `str(Decimal)`, and a field left empty where it is undefined.
- `tz17-summary.json` — `N`, the member count, the candidates considered, every count of §3.6 and
  §4, the member-list SHA-256, the two power literals of §4 and the §4 reading; keys sorted,
  `indent=1`, `ensure_ascii=True`, one trailing newline.

The member-list SHA-256 is taken over the members' `T` in increasing order, as decimal ASCII joined
by `\n`, with no trailing newline.

---

## 4. Gate

Fixed before any document is fetched. The statistic is `N`, over the 200 members of §3.3.

| reading | condition |
|---|---|
| **FAIL** | the set is formed and `N <= 198` |
| **PASS** | the set is formed and `N >= 199` |
| **UNDECIDABLE** | the set of 200 cannot be formed from candidates 0 to 399 |

- **False-failure probability** under the model this gate scores — the three identities hold at
  every window: exactly `0`. One statistic over one set, so the family-wise figure is also `0`.
- **Power** against the named alternative — each window independently fails at least one identity
  with probability `0.02`: `P(N <= 198) = 0.910624516228067965960219332490`, above the `0.8` floor.
  PASS is therefore available, and power decides nothing once a document is read.
- Against a rate of `0.01` the power is `0.595354315327973499366704428681`: this gate cannot tell a
  one-in-a-hundred anomaly rate from none, and a PASS does not claim to.
- Both figures were computed as `1 − (1−p)^200 − 200·p·(1−p)^199` in exact rational arithmetic and
  cross-checked by summing the binomial mass over 2 to 200 failures at 60 digits; the two agree in
  all 30 printed decimals.
- No row of this table moves after `N` is known, and nothing is tuned to reach it.

---

## 5. Self-tests

Run by every invocation before any network request and before any file but the instrument's own
source is read, each an `assert` that aborts the run. The report prints the count of asserts as
`n of n`.

- **S1** `slug15(1788998400) == "btc-updown-15m-1788998400"` and
  `slug5(1788999000) == "btc-updown-5m-1788999000"`.
- **S2** `candidates(start=1789668900, cap=2)` raises before yielding its second candidate, whose
  15-minute window would end at `1789670700`; `candidates(start=1788998400, cap=400)` yields 400
  candidates whose largest requested epoch is `1789358400`.
- **S3** `validity` on synthetic inputs returns, in this order: `ok` for a valid document; `json`
  for a body that is a JSON array; `slug` for a slug mismatch; `open` for `"closed": false`;
  `no-ptb` with `priceToBeat` removed; `ptb-range` for the JSON number `-1.5`; `precision` for the
  JSON number `64123`; `unresolved` for `outcomePrices` `["0.5", "0.5"]`; `unresolved` for outcomes
  `["Yes", "No"]`; `absent` for status 404; `status` for status 500; `fetch` for no response — 12
  cases.
- **S4** I1 on `Decimal` pairs at live magnitude: (`64123.451234567891`, `64123.451234567891`)
  holds; (`64123.451234567891`, `64123.451234567892`) fails, the difference `1E-12` not being below
  `10^-12`; (`64123.45`, `64123.451234`) holds, `E = -2`; (`64123.45`, `64123.4612`) fails.
- **S5** I2 at equality: `K5d = K15 = 64123.451234567891` gives `"Up"`.
- **S6** `reading(N=200, members=200) == "PASS"`, `reading(N=199, members=200) == "PASS"`,
  `reading(N=198, members=200) == "FAIL"`, `reading(N=None, members=150) == "UNDECIDABLE"`.
- **S7** `form_set` on the synthetic qualification sequence `ok, fetch, ok, ok, open, ok` with
  `need=3` returns members `k = 0, 2, 3`, stops after `k = 3`, and lists `k = 1` as a non-member
  with code `fetch`.
- **S8** `power(Fraction(1, 50))` differs from `0.910624516228067965960219332490` by less than
  `1E-18`, `power(Fraction(1, 100))` from `0.595354315327973499366704428681` by less than `1E-18`,
  and `power(Fraction(0)) == 0`. The instrument computes in `fractions.Fraction` and compares as
  `Decimal` at 60 digits. Reference: §4's two independent computations, exact to 30 decimals —
  twelve decades finer than the tolerance.
- **S9** The instrument's own source, parsed with `ast`: every imported top-level module is in
  `sys.stdlib_module_names`; none is `subprocess`; no attribute `system`, `popen`, or any name
  starting `spawn` or `exec`, is taken on `os`; no call carries a keyword `shell`; and exactly one
  string constant contains `://`, equal to `https://gamma-api.polymarket.com/markets/slug/`.

---

## 6. Invocations and runs

Every run is `/root/tz01-env/venv/bin/python research/tz17-settlement-chain.py …` from
`/root/tz17-work/wt`.

| run | invocation | does |
|---|---|---|
| R0 | `--selftest` | §5 only; no network, and no file read but the instrument's own source |
| R1 | `--fetch` | §5; the fingerprint gate inside the instrument; the resource gate by `os.statvfs`, `f_bavail * f_frsize >= 2200000000`, at start and at end; Stage F; the stability re-fetch |
| R2 | `--analyze --out /root/tz17-work/run-1` | §5; the fingerprint gate; Stage A |
| R3 | `--analyze --out /root/tz17-work/run-2` | the same, in a fresh process |

- **The fingerprint gate inside the instrument** parses the map's own §0 tables. It asserts the
  revision string and the six anchors against this TZ's literals; re-derives `A2` from
  `research/twap-divergence.py`, `A4` from `BTC-EXECUTOR-INSTRUCTIONS.md`, `A5` from
  `research/recorder/recorder.py` and `A6` from `research/pfair.py`, each the first 12 hex
  characters of the file's SHA-256; and hashes every path the fingerprint table lists — 25 rows,
  the map's own included — asserting the 22 `frozen` rows.
- **Order.** The implementation is committed and pushed to `origin/tz-17-settlement-chain` before
  R1. Before each of R1, R2 and R3 the Executor runs
  `test "$(git rev-parse HEAD)" = "$(git rev-parse origin/tz-17-settlement-chain)"` in
  `/root/tz17-work/wt` and stops on a non-zero exit; all three outputs go into the report.
- **Re-runs.** R1 computes no identity of §3.5, so re-running it cannot select on the gate. If R1
  stops on a transport failure or an instrument defect before it completes, it may be run again
  from an empty `/root/tz17-work/raw/` after the fix is pushed; every attempt is listed in the
  report's §6 with its stop reason. R2 and R3 each run once, both from the final pushed commit;
  where that commit is not R1's, the report names both.
- **Stage A's bound.** R2 and R3 each stop, BLOCKED, past 300 s of wall clock.

---

## 7. Validation

Each row names the runs it must hold on. Every row is an `assert` or an explicit non-zero exit.

| # | check | runs |
|---|---|---|
| V1 | Revision `2026-09-19-c`, 6 of 6 anchors, 22 of 22 `frozen` rows equal; the report's §0 lists all 25 rows of the table with `wc -l` and `sha256sum` | R1, R2, R3 |
| V2 | H1, H2 and H3 hold; available space at least `2,200,000,000` bytes at §0 and at R1's start and end, each figure printed | §0, R1 |
| V3 | Every request passes P3 before it is sent; the largest requested 5-minute epoch is printed and is at most `1789358400` | R1 |
| V4 | Stage F issues at most `1,601` requests, retries not counted, and the re-fetch exactly `40`; every attempt has its `index.jsonl` or `refetch.jsonl` line; every stored body re-hashes to its line's `sha256` | R1; the re-hash at R2 and R3 |
| V5 | R2's and R3's member lists equal R1's, and the three member-list SHA-256 are printed and equal | R1, R2, R3 |
| V6 | Every §5 assert passes before the first network request and before any file but the instrument's own source is read, `n of n` printed | R0, R1, R2, R3 |
| V7 | `tz17-candidates.csv` and `tz17-summary.json` are byte-identical across R2 and R3; both SHA-256 printed | R2, R3 |
| V8 | The 40 re-fetched gate documents equal the stored ones in `K` as `Decimal` tuples, in `closed`, in `outcomes` and in `outcomePrices`: 40 of 40. The number whose bytes differ anywhere else is printed, not asserted | R1 |
| V9 | Every open for writing lies under `/root/tz17-work/` and outside both worktrees; R1's total bytes written printed, and at most `200,000,000` | R1, R2, R3 |
| V10 | `git diff --name-only origin/main origin/tz-17-settlement-chain` prints exactly `research/tz17-settlement-chain.py` | after the branch push |
| V11 | Contract §4.2's separation self-check, output pasted verbatim; its first line prints `0` | after the report commit |
| V12 | S9's syntax-tree guard | R0 |
| V13 | `fetch-summary.json` carries no key named `I1`, `I2`, `I3`, `holds` or `N` | R1 |

No row reads a label of TZ-16's span, and none can: P3 is checked before every request.

---

## 8. Report

Contract §8's seven sections, in order. In them:

- **§0** the fingerprint table, all 25 rows; the revision and anchors read; every §0 command of this
  TZ with its output verbatim; the three `test "$(git rev-parse …)"` outputs of §6.
- **§1 Input** requests by status and by market type, retries, Stage F's wall clock, bytes stored,
  the re-fetch, and every R1 attempt with its stop reason; or the statement that R1 ran once.
- **§2 Measurements** `tz17-candidates.csv` in full as a fenced `csv` block; `N`; the counts of I1,
  I2 and I3 over the members; D1 to D7; the member-list SHA-256; the largest requested epoch; Stage
  A's wall clock in each of R2 and R3.
- **§3 Publication** branch, commit, V10 and V11.
- **§4 Gate** §4's table quoted, `N`, and the reading.
- **§5 Validation** V1 to V13, each with its count, whether it is asserted, and the runs it held on.
- **§6 What could not be implemented as written.**

**Audit route.** Everything the Architect re-derives — each member's four literals, two outcomes,
three flags and the member list — is in the fenced CSV of §2. The raw bodies stay under
`/root/tz17-work/raw/`, and the endpoint is public: any document can be fetched again and compared
with the CSV's fields.

---

## 9. Retention

- **Creates `/root/tz17-work/`**: `wt`, `wt-report`, `raw/`, `index.jsonl`, `refetch/`,
  `refetch.jsonl`, `fetch-summary.json`, `run-1/`, `run-2/`. It stays until the first TZ written
  after this report is on `main`, which copies what this report names by hash into
  `/root/btc-forensics/` and reclaims the rest.
- **`/root/tz15-work/`** is TZ-16's to reclaim, System Map §3. This TZ reads `test -e` and touches
  nothing.
- **`/root/tz14-work/`**: System Map §3 records the Boss's removal block of 2026-09-19 reporting
  `exit=1`. This TZ reads `test -e` and states the result; TZ-16's §0 stays the TZ that verifies it.
- `/root/btc-forensics/`, `/root/tz01-env/` and `/root/tz04a-env/` are never removed. This TZ copies
  nothing into `/root/btc-forensics/`.
- **Worktrees at the end:** `git worktree list` printed. `/root/tz17-work/wt` and
  `/root/tz17-work/wt-report` stay registered.

---

## 10. Pre-send checks

Performed on 2026-09-22 against this file, as a separate reading after §9 was written. Every
defect that reading found was repaired in the body before the results below were recorded.

- **C1 — scope against body.** Repository paths the body names: 28 — the three this TZ creates
  (`CryptoTZ/TZ-17-settlement-chain.md`, `CryptoReports/TZ-17-settlement-chain-report.md`,
  `research/tz17-settlement-chain.py`) and the 25 rows of the map's §0 fingerprint table, five of
  them by name (`SYSTEM-MAP.md`, `BTC-EXECUTOR-INSTRUCTIONS.md`, `research/twap-divergence.py`,
  `research/recorder/recorder.py`, `research/pfair.py`). Committed entry points called: 0.
  Intersections with §2: 2 — P4 against §0's `find` and `grep` under `/var/lib/btc-recorder/`,
  named as P4's exemption; P2 against the Executor's `git fetch` and `git push`, removed by scoping
  P2 to the instrument and stated in §2's exemption line. Reading or hashing the 25 table paths,
  `test -e` on `/root/tz14-work` and `/root/tz15-work`, and running `/root/tz01-env/venv/bin/python`
  modify nothing and meet no prohibition.
- **C2 — origin of every expectation.** §5: S1's two slugs, S2's `1789670700`, `1789358400` and
  `400`, S4's four booleans with `1E-12` and `E = -2`, and S7's members `0, 2, 3` are computed
  independently in exact integer, string or `Decimal` arithmetic from §3's definitions; S3, S5, S6
  and S9 test definitions of §3.1, §3.2, §3.5 and §4, not numbers; S8's two literals are computed
  independently — exact `Fraction` evaluation of the closed form and a separate 60-digit binomial
  summation, agreeing in all 30 decimals — with tolerance `1E-18`, twelve decades coarser than the
  reference's `1E-30`. §7: `2026-09-19-c`, the six anchors, `22` and `25` are quoted from the map's
  §0; `31,612,203,008` from its §6 host identity; `1789669800` from its §2.3; `2,200,000,000` is its
  §6 floor `2,000,000,000` plus this TZ's `200,000,000` cap; `1789358400`, `1,601` and `40` are
  computed from §3.3 and §3.4; V11's `0` is quoted from contract §4.2. No expectation depends on a
  quantity this TZ measures: `N` is read by §4 and asserted nowhere, and V8's `40 of 40` holds for
  every admissible value of the fields it compares.
- **C3 — shape of every diff.** Called additive: `research/tz17-settlement-chain.py`, a new file.
  Committed lines replaced: none — the path is in neither the map's §0 fingerprint table nor its §3
  code table, and V10 asserts against `origin/main` at run time that the diff names that path
  alone. "insertions only" appears once, in §2, where the list is empty.
- **C4 — cost of every check,** at the population's upper bound of 400 candidates, never at the
  200 expected. Stage F: `1,601` requests plus `40` re-fetches, `1,641` in all. TZ-14's measured
  Polymarket REST reply delay, `39.6` to `391.1` ms (map §2.3), is below the `0.5` s pacing interval,
  so pacing binds: `1,641 × 0.5 = 820.5` s. Fail-fast, term by term: the `2,700` s cap is `820.5` s
  plus `1,879.5` s of slack; a fully retried request adds at most `3 × 20` s of timeouts and
  `5 + 10 + 20` s of waits, `95` s, so the slack absorbs 19 of them. The consecutive-failure rule
  fires at `20 × (4 × 20 + 35) = 2,300` s, inside the cap; with `Retry-After` at its `60` s cap a
  request can take `4 × 20 + 3 × 60 = 260` s, and the wall cap binds. The early stop costs `41`
  requests, `20.5` s at the pacing floor. Stage A: at most `1,601` bodies, `200,000,000` bytes and
  `400` identity evaluations per run; no parse rate is measured on this host, so each run is capped
  at `300` s and prints its measured wall clock. Self-tests and fingerprint hashing are constant:
  25 files, `845,887` bytes listed plus the map's own `156,425`. Session upper bound
  `2,700 + 300 + 300 = 3,300` s, below `3,600`; nothing is sampled and nothing is split.
- **C5 — every count.** `22` and `25`: the map's §0 fingerprint table, rows in state `frozen` and
  all rows (22 frozen, 2 tracked, 1 reported). `6`: its §0 anchor table, `A1` to `A6`. `1,601`:
  `400` `M15` of candidates 0 to 399 (§3.3) plus `1,201` distinct `M5`, the set
  `{T_k, T_k + 300, T_k + 600 : k <= 399}` together with `T_399 + 900` (§3.3, §3.4), counted by
  enumeration. `40`: the first 10 members times their 4 gate documents (§3.4). `41` (§3.1): the
  `10` `M15` and `31` distinct `M5` of candidates 0 to 9. `1789358400`: `T_399 + 900`, with
  `T_399 = 1788998400 + 399 × 900 = 1789357500` (§3.3). `12`: §5's S3 list.
- **C6 — every population.** `N` and the counts of I1, I2 and I3: the 200 members (§3.3). D1 and
  D4: the members. D2: the members whose `M5(T+300)` reads `ok`, the excluded count printed and out
  of the denominator. D3: the four gate literals of every member. D5 and D6: every `ok` document,
  per market type. D7: the candidates considered that are not members. Request accounting: every
  Stage F attempt, and the 40 re-fetches. V8's byte-difference count: the 40 re-fetched documents.
  Stage A's wall clock: each of R2 and R3.
- **C7 — every signature and every behaviour.** The TZ names no committed function. P5 forbids any
  import from `research/`, and every function it names — `slug15`, `slug5`, `candidates`,
  `validity`, `form_set`, `reading`, `power`, `K`, `O` — is defined by this TZ in the new file.
  Nothing to quote, no commit to name.
- **C8 — every cross-reference,** each resolved by reading the text on 2026-09-22. CANON §1.1: the
  60-second feed for the 15-minute markets and for the 5-minute markets since 2026-08-14, the price
  to beat at `events[0].eventMetadata.priceToBeat`, and the standing rule on measurement — §1, §3.1.
  CANON PART II: false-failure probability, power against a named alternative, UNDECIDABLE — §4.
  System Map §0, revision `2026-09-19-c`: the revision, the six anchors, the 25-row table with 22
  `frozen`; `A5` and `A6` named in its prose, `A2` and `A4` as "collector" and "executor contract",
  whose values equal the first 12 hex characters of the table's hashes for
  `research/twap-divergence.py` and `BTC-EXECUTOR-INSTRUCTIONS.md` — header, §6, V1. §2.3: the
  reserved span `T0 > 1789669800` and TZ-14's reply delay — P3, C4. §3: `/root/tz15-work/` as
  TZ-16's and `/root/tz14-work/` at `exit=1` — P7, §9. §4: the price-to-beat row, TZ-04b V1 198 of
  200 and TZ-06 V3 396 of 400 — §3.5. §6: host identity — H2 is weaker than its second clause, and
  the header says so beside it — the interpreter, egress to `gamma-api.polymarket.com`, the
  `2,000,000,000` floor, the three reads every §0 states, the resolution endpoint, `Decimal` at 60
  digits, and outcome mapping by string — header, §0, §3. Executor contract, revision
  `2026-09-10-a`: §1 steps 1 to 5, the `git checkout` lines of §4.1, §4.2's self-check with first
  line `0`, and §8's seven sections — §0, V11, §8.
