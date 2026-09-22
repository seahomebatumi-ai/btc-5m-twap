# TZ-17 — the settlement chain — report

**Executed.** The gate reads **PASS**: `N = 200` of 200 members, against a PASS condition of
`N >= 199`.

| field | value |
|---|---|
| TZ | `CryptoTZ/TZ-17-settlement-chain.md` |
| branch | `tz-17-settlement-chain`, head `8f1bc93e454275ddb3f0e060bed3bb9f2f9cf31b` |
| Executor model | **Opus** — the model the TZ names, and the one that ran |
| runs | R0, R1, R2, R3, each once |
| reading | **PASS** — the two market types settle on one reading at a shared boundary |

The 15-minute market `btc-updown-15m-{T}` and the 5-minute market `btc-updown-5m-{T+600}` were
found, at each of 200 consecutive windows from 2026-09-10 00:00 UTC to 2026-09-12 01:45 UTC, to
carry the *same* price to beat at the shared open and to resolve as the *same* reading at `T+900`
decides. I1, I2 and I3 each hold at 200 of 200.

---

## 0. Fingerprint

### 0.1 The map's §0, as this run read it

Read from `SYSTEM-MAP.md` on `main` at `2054800`, and asserted inside the instrument at each of
R1, R2 and R3 — the revision string, the six anchors, and the SHA-256 of every path the
fingerprint table lists. `A2`, `A4`, `A5` and `A6` were re-derived from
`research/twap-divergence.py`, `BTC-EXECUTOR-INSTRUCTIONS.md`, `research/recorder/recorder.py`
and `research/pfair.py` as the first 12 hex characters of each file's SHA-256, not copied from the
table. All 25 rows are listed with `wc -l` and `sha256sum`; the 22 in state `frozen` were asserted
equal.

```
revision 2026-09-19-c | anchors 6 of 6 | rows 25 | frozen 22 of 22
anchor A1 229a944f2d51
anchor A2 6c5089330629
anchor A3 0-complete / 1-student-5tau-not-disqualified / 2-undecidable-5tau
anchor A4 437b45ea196b
anchor A5 9fd1c7de0f74
anchor A6 729f0bcdbee3
path                                           wc -l     bytes state     sha256
SYSTEM-MAP.md                                    826    156425 reported  3a88c35707fb937043b56571d5b146819a43c905122f379ad89fc75c95e3e1a0
BTC-EXECUTOR-INSTRUCTIONS.md                     234     11128 frozen    437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b
research/twap-divergence.py                     1135     50928 frozen    6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473
research/selftest-twap-divergence.py             376     16736 frozen    ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a
research/tz02-distribution.py                    334     14511 tracked   f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4
research/pfair.py                                441     19357 frozen    729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68
research/selftest-pfair.py                       619     32559 frozen    b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa
research/tz06-calibration.py                     577     27138 frozen    715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f
research/tz07a-variance-time.py                  623     28414 frozen    513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771
research/tz07b-settlement-dispersion.py          515     24926 frozen    424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc
research/tz08a-out-of-sample.py                  745     38822 frozen    37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c
research/tz09-disk-inventory.py                  894     41004 frozen    b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6
research/tz10b-sigma-or-link.py                 1224     61018 frozen    406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088
research/tz11a-student-link.py                  1231     64732 frozen    0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839
research/tz12-sized-gate.py                     1157     61637 frozen    d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999
research/tz13-sized-gate-test3.py               1074     53901 frozen    a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd
research/tz14-quote-inventory.py                2124    109972 frozen    978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02
research/tz15-phase2-gate.py                    1517     73799 frozen    66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3
research/recorder/recorder.py                    608     25658 frozen    9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03
research/recorder/config.py                      112      4773 frozen    8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d
research/recorder/manifest.py                    254     10002 frozen    79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045
research/recorder/analyze.py                     813     34705 frozen    eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d
research/recorder/probe.py                       227      9324 frozen    50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2
research/recorder/selftest.py                    573     30591 frozen    c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90
.gitignore                                         5       252 tracked   9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b
```

Every anchor the TZ header requires was matched: `A1` `229a944f2d51`, `A2` `6c5089330629`,
`A3` `0-complete / 1-student-5tau-not-disqualified / 2-undecidable-5tau`, `A4` `437b45ea196b`,
`A5` `9fd1c7de0f74`, `A6` `729f0bcdbee3`. Revision `2026-09-19-c`. **25 rows, 22 frozen, 22 of 22
equal.** No `frozen` row moved and this TZ edited no committed file.

### 0.2 The §0 commands, verbatim

Run from `/root/btc-5m-twap` after contract §1 steps 1–5, in the TZ's own order.

```
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13528887296

$ find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json

$ pgrep -af recorder
228592 /root/tz04a-env/venv/bin/python -B -u recorder.py
2566820 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1790084493076-r8mhx1.sh 2>/dev/null || true && shopt -u extglob 2>/dev/null || true && { \builtin unalias -- 'unsetenv'; \builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'echo "=== df ===" && df -B1 --output=source,size,avail /var/lib/btc-recorder; echo "=== find ===" && find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit; echo "=== pgrep ===" && pgrep -af recorder; echo "=== grep ===" && grep -rl --include=runtime.jsonl 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder | head -n 1' < /dev/null && pwd -P >| /tmp/claude-b77f-cwd

$ grep -rl --include=runtime.jsonl 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder | head -n 1
/var/lib/btc-recorder/btc-updown-5m/1789488300/runtime.jsonl

$ du -sb /root/PROJECT_GAMING_PS5
400769377	/root/PROJECT_GAMING_PS5

$ systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1

$ systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3

$ test -e /root/tz14-work; echo "tz14-work exit=$?"
tz14-work exit=1

$ test -e /root/tz15-work; echo "tz15-work exit=$?"
tz15-work exit=0

$ git worktree list
/root/btc-5m-twap          2054800 [main]
/root/tz15-work/wt         f7f171a [tz-15-phase2-gate]
/root/tz15-work/wt-report  c729008 (detached HEAD)
```

**H1 holds** — `find` printed exactly one path. **H2 holds** — `pgrep` printed at least one line,
and the recorder is the first of them, pid `228592` running `recorder.py` out of
`/root/tz04a-env/`; `grep` printed one `runtime.jsonl` carrying
`4216c04673ced76b5b2ac60ef57c9abedc46f9b9`. The second `pgrep` line is the Executor's own shell,
which contains the string `recorder` in the command it was evaluating; H2 as the TZ words it is
met by the recorder line itself. **H3 holds** — source `/dev/vda2`, size `31612203008`.

**Resource gate holds** — `avail` `13,528,887,296` bytes, against the required `2,200,000,000`.
Headroom over the floor: `11,328,887,296` bytes.

`/root/tz14-work` is **gone**, `test -e` exit `1`, which is the outcome the map's §3 records the
Boss as having reported on 2026-09-19 and which TZ-16's §0 was to verify. `/root/tz15-work` is
present, exit `0`; this TZ read only `test -e` on it and touched nothing under it.

The `du` and `systemctl` reads carry no threshold here. `telemetry-watch.service` is `disabled`
(exit 1) and `inactive` (exit 3) — **fourteen reads running** — and `/root/PROJECT_GAMING_PS5`
stood at `400,769,377` bytes.

### 0.3 The same three reads at the end of the session

```
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13513277440

$ du -sb /root/PROJECT_GAMING_PS5
400790037	/root/PROJECT_GAMING_PS5

$ systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1

$ systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3

$ pgrep -af "recorder.py"
228592 /root/tz04a-env/venv/bin/python -B -u recorder.py

$ git worktree list
/root/btc-5m-twap          2054800 [main]
/root/tz15-work/wt         f7f171a [tz-15-phase2-gate]
/root/tz15-work/wt-report  c729008 (detached HEAD)
/root/tz17-work/wt         8f1bc93 [tz-17-settlement-chain]
/root/tz17-work/wt-report  2054800 (detached HEAD)

$ du -sb /root/tz17-work
11073071	/root/tz17-work
```

Free space fell `15,609,856` bytes across the session, of which `11,073,071` is this TZ's own
tree. `/root/PROJECT_GAMING_PS5` grew `20,660` bytes — idle by any measure, as at every read since
2026-09-14. The recorder is the same process, pid `228592`, unsignalled: this TZ stopped nothing,
restarted nothing and opened no file of the capture.

### 0.4 The three head checks the TZ's §6 requires

Run in `/root/tz17-work/wt` before each of R1, R2 and R3:

```
$ test "$(git rev-parse HEAD)" = "$(git rev-parse origin/tz-17-settlement-chain)"
R1 head-check exit=0
R2 head-check exit=0
R3 head-check exit=0
```

All three exited `0`: every run was made from the pushed commit
`8f1bc93e454275ddb3f0e060bed3bb9f2f9cf31b`, and R1, R2 and R3 all ran from the *same* commit, so
§6's "where that commit is not R1's" clause does not apply.

### 0.5 Interpreter and trees

`/root/tz01-env/venv/bin/python`, the research interpreter the map's §6 names, for all four runs.
The two worktrees the TZ's §0 requires were created from `origin/main` at `2054800` and both stay
registered.

---

## 1. Input

**R1 ran once**, to completion, and was not re-run. Nothing was re-collected: `/root/tz17-work/raw/`
was empty before it started, and the instrument refuses to start Stage F when
`/root/tz17-work/index.jsonl` already exists.

The only input is the venue's own published documents, fetched from the public Gamma API. **No file
under `/var/lib/btc-recorder/` was opened** — not a `gamma.json`, not a `resolution.json`, not a
quote file, not a stream. The two §0 commands that touch that path, `find` and `grep`, are P4's
named exemption and are the Executor's, not the instrument's.

### 1.1 Stage F

| quantity | value |
|---|---|
| candidates considered | `200` — k = 0 … 199 |
| requests issued, retries not counted | `801` |
| by market type | `btc-updown-15m-*` `200`; `btc-updown-5m-*` `601` |
| by HTTP status | `200`: **801**. No 404, no other 4xx, no 5xx, no transport error |
| attempts, retries included | `801` |
| retries | `0` |
| wall clock | `402.296` s |
| bytes written by R1 | `4,442,478` |
| mean body | `5,048` bytes (801 bodies) |
| largest requested 5-minute epoch | `1789178400` |
| largest requested 15-minute epoch | `1789177500` |
| P3 checks | `841` — one before each of the 801 Stage F and 40 re-fetch requests |
| free space, R1 start / end | `13,521,006,592` / `13,513,474,048` |
| stop reason | `complete` — the 200th candidate qualified at k = 199 |

801 is the exact count §3.4's no-refetch rule predicts for 200 candidates: `200` 15-minute slugs
plus `601` distinct 5-minute slugs, the set `{T_k, T_k+300, T_k+600 : k <= 199}` together with
`T_199 + 900`. It is well inside the `1,601` bound, which is the cost at the population's upper
bound of 400 candidates.

Pacing bound the run as the TZ's C4 predicted: `801 + 40 = 841` requests at the `0.5` s floor is
`420.5` s of pacing, and the measured reply delay — mean `94.5` ms over the 801 — is below it.
Stage F's measured `402.296` s is against a cap of `2,700` s.

### 1.2 The stability re-fetch

The four gate documents of the first 10 members, fetched a second time under the same pacing and
retries, into `/root/tz17-work/refetch/` and `/root/tz17-work/refetch.jsonl`.

| quantity | value |
|---|---|
| requests | `40` — exactly, as V4 requires |
| by market type | `15m` `10`; `5m` `30` |
| by HTTP status | `200`: **40** |
| retries | `0` |
| agree in `K` as `Decimal` tuples, `closed`, `outcomes`, `outcomePrices` | **40 of 40**, asserted |
| bodies differing in bytes anywhere else | `0` — printed, not asserted |

Not one of the forty documents moved between the two reads, in the four fields the gate depends on
or anywhere else in the body.

### 1.3 Files this run wrote

| path | what |
|---|---|
| `/root/tz17-work/raw/{slug}.body` | 801 bodies, byte for byte as received |
| `/root/tz17-work/index.jsonl` | 801 lines, one per attempt |
| `/root/tz17-work/refetch/{slug}.body` | the 40 re-fetched bodies |
| `/root/tz17-work/refetch.jsonl` | 40 lines, one per attempt |
| `/root/tz17-work/fetch-summary.json` | R1's own summary |
| `/root/tz17-work/run-1/`, `/root/tz17-work/run-2/` | R2's and R3's two outputs each |

Every one of them lies under `/root/tz17-work/` and outside both worktrees, asserted before each
open: `1,687` guard checks at R1, `3` at each of R2 and R3.

---

## 2. Measurements

### 2.1 The set

| quantity | value |
|---|---|
| candidates considered | `200` |
| members | `200` |
| non-members | `0` |
| first member `T` | `1788998400` — 2026-09-10 00:00 UTC, Thursday |
| last member `T` | `1789177500` — 2026-09-12 01:45 UTC, Saturday |
| last requested epoch | `1789178400` — 2026-09-12 02:00 UTC |
| member-list SHA-256 | `68ee20bcb4a915604ebefca4b6908853810b6c6003928777e59769a3b225cebc` |

The set closed at the first opportunity: **every one of candidates 0 … 199 qualified**, so the
members are the 200 consecutive 900-second slots from `1788998400`, and Stage F stopped there. The
member-list hash is taken over the members' `T` in increasing order, as decimal ASCII joined by
`\n` with no trailing newline, and is identical at R1, R2 and R3.

The largest epoch this run requested, `1789178400`, is `491,400` seconds below TZ-16's reserved
boundary `1789669800`. **Nothing in the reserved span was requested**, and P3 was checked before
every one of the 841 requests.

### 2.2 The three identities

| identity | holds |
|---|---|
| **I1** — one reading at the shared open, `\|K15 − K5a\| < 10^E` | **200 of 200** |
| **I2** — `O15 == "Up"` iff `K5d >= K15` | **200 of 200** |
| **I3** — `O5c == "Up"` iff `K5d >= K5c` | **200 of 200** |
| **holds** — all three at one member | **200 of 200** |

**`N = 200`.**

### 2.3 D1 — `I1_exact`

`K15 == K5a` as `Decimal`s at **200 of 200** members. The 15-minute market opening at `T` and the
5-minute market opening at `T` do not merely agree to the precision of the coarser literal — they
publish the *same literal*, to all 9 to 11 decimal places, at every member. The full member list is
in `tz17-summary.json` under `D1_I1_exact_members`; it is the member list itself.

### 2.4 D2 — the chain inside the window

Over the members whose `M5(T+300)` reads `ok`:

| check | holds / checks |
|---|---|
| **I4a** — `O(M5(T)) == "Up"` iff `K5b >= K5a` | **200 of 200** |
| **I4b** — `O(M5(T+300)) == "Up"` iff `K5c >= K5b` | **200 of 200** |
| members left out because `M5(T+300)` is not `ok` | **0** |

No member left the denominator. The two 5-minute markets *inside* the 15-minute window settle on
the same chain of readings as the two at its ends.

### 2.5 D3 — the distribution of `exponent` over the four gate literals

| literal | `-9` | `-10` | `-11` |
|---|---|---|---|
| `K15` | 4 | 33 | 163 |
| `K5a` | 4 | 33 | 163 |
| `K5c` | 3 | 36 | 161 |
| `K5d` | 4 | 33 | 163 |

Every literal carries at least 9 decimal places; none came close to the `precision` rejection at
`exponent > -2`. `K15` and `K5a` share their exponent distribution exactly, which D1 already
implies — they are the same literal.

### 2.6 D4 — near-strike members

| condition | count |
|---|---|
| `\|K5d − K15\| < 1` USD | **1** |
| `\|K5d − K5c\| < 1` USD | **5** |

| which | `k` | `T` | UTC | difference | outcome |
|---|---|---|---|---|---|
| `d15` | 13 | `1789010100` | 2026-09-10 03:15 Thu | `-0.70534386210` | `O15` = Down |
| `d5` | 33 | `1789028100` | 2026-09-10 08:15 Thu | `0.80257602335` | `O5c` = Up |
| `d5` | 129 | `1789114500` | 2026-09-11 08:15 Fri | `0.20962982511` | `O5c` = Up |
| `d5` | 134 | `1789119000` | 2026-09-11 09:30 Fri | `-0.46238149866` | `O5c` = Down |
| `d5` | 144 | `1789128000` | 2026-09-11 12:00 Fri | `0.07113186355` | `O5c` = Up |
| `d5` | 165 | `1789146900` | 2026-09-11 17:15 Fri | `0.45432492392` | `O5c` = Up |

These six are the members where a reading offset under a dollar could have flipped I2 or I3, and
every one of them resolved on the side `K5d` puts it. The tightest, `k = 144`, decided on
`0.071` USD — seven cents on a ~`114,000` USD number, `6 × 10^-7` relative. A settlement rule that
merely *correlated* with `K5d` would not survive that margin; one that *is* `K5d` does.

For scale, over all 200 members `|d15|` ranges from `0.705` to `1,398.314` USD and `|d5|` from
`0.071` to `462.629`. The outcomes are not one-sided: `O15` is Up at 98 and Down at 102 members,
`O5c` Up at 102 and Down at 98.

### 2.7 D5 — the key names of `events[0].eventMetadata`

| market type | key | count |
|---|---|---|
| `15m` | `finalPrice` | 200 |
| `15m` | `priceToBeat` | 200 |
| `5m` | `finalPrice` | 601 |
| `5m` | `priceToBeat` | 601 |

The union over every `ok` document is two keys, in both market types. `priceToBeat` is present at
801 of 801 — the field CANON §1.1 names, and no other metadata key exists to disagree with it.

### 2.8 D6 — `resolutionSource`

| market type | value | count |
|---|---|---|
| `15m` | `https://data.chain.link/streams/btc-usd-twap-60s-streams` | 200 |
| `5m` | `https://data.chain.link/streams/btc-usd-twap-60s-streams` | 601 |

**One distinct value, and it is the same string for both market types**, at 801 of 801 `ok`
documents. No document was missing the key. This is the venue's own published statement that the
two market families read one feed, and it agrees with what D1 and §2.2 measure against resolved
outcomes — which is what CANON §1.1's standing rule asks for, documentation not being enough.

### 2.9 D7 — the first non-`ok` gate document of each non-member

**Empty.** There are no non-members among the 200 candidates considered: every candidate's four
gate documents read `ok`.

### 2.10 Stage A's wall clock

| run | out | wall clock |
|---|---|---|
| R2 | `/root/tz17-work/run-1` | `0.249` s |
| R3 | `/root/tz17-work/run-2` | `0.240` s |

Both against the TZ's `300` s bound.

### 2.11 `tz17-candidates.csv`, in full

201 lines, `99,075` bytes, SHA-256
`96b5e21e2cc59e2f3bde332d60457533158bd16c2eeaaaba844bf35b1efc63ee`, byte-identical at R2 and R3.
Booleans are `1` / `0`; a field is left empty where it is undefined; literals are printed as
`str(Decimal)`. `d15 = K5d − K15` and `d5 = K5d − K5c`. Note that `sha_M5d` of candidate `k` equals
`sha_M5a` of candidate `k+1` throughout — that is the same stored body, fetched once, as §3.4
requires.

```csv
k,T,member,reason,K15,K5a,K5c,K5d,O15,O5c,I1,I2,I3,holds,I1_exact,K5b,O5a,O5b,I4a,I4b,d15,d5,sha_M15,sha_M5a,sha_M5b,sha_M5c,sha_M5d
0,1788998400,1,ok,78275.35460685384,78275.35460685384,78293.19100745904,78279.29016456462,Up,Down,1,1,1,1,1,78308.28632218906,Up,Down,1,1,3.93555771078,-13.90084289442,160aca8c96b078e4d8a91506d80a8a19998fe7ca41e542895eb98bfdd66e69ca,caf22eb7e9f0dcbaa40819a8df44d48249b6e9c59c0db15eb30e2546859a8108,8cd8813b40eec8a93b2f7a6619d951e3364ade6d1621e6fb0fc478e59f7ff8b1,285757d8e6a2e690005ef3f0781badd84e7f4f4a642997f07976bc12474fc2f1,2b914c928d7a0b88163e201272182506f603f86a6395583a6284870e2bc4306a
1,1788999300,1,ok,78279.29016456462,78279.29016456462,78284.49425339627,78300.80736045327,Up,Up,1,1,1,1,1,78238.48247958202,Down,Up,1,1,21.51719588865,16.31310705700,221e75f401440f407c69d1dc3d06b1f33ec346b340462b4013644e4149b010ba,2b914c928d7a0b88163e201272182506f603f86a6395583a6284870e2bc4306a,d6fe48f3762cf6737937ec19f1a749d47a5948db7352b9ba8ffcde5de33f56d9,0001b708e057d4f92409f0efa00472bc309b760a7dc72f51174452c4028f0832,c84b6cdab7d22118064eaa8197dd0375d59590d1342d10e363ccf2899f5d5cfe
2,1789000200,1,ok,78300.80736045327,78300.80736045327,78256.8300215274,78146.0487241943,Down,Down,1,1,1,1,1,78233.55002087375,Down,Up,1,1,-154.75863625897,-110.7812973331,d8ee132823013eb63e1fabb408697290d63851f1ff13f0d318314945798c5999,c84b6cdab7d22118064eaa8197dd0375d59590d1342d10e363ccf2899f5d5cfe,ad5bdbcdccc6f4125de334943b3b2e7f0595c7c51eeb6a91534b9e34b4719582,dabd698e11957f12e367249196e5ed11e333855c90b09db6f2df02ae99b9a94d,8a62ea985f6ac674bf2fadb20d5256c5544dfe81666bd56a3e4da101f659a75d
3,1789001100,1,ok,78146.0487241943,78146.0487241943,78118.08975003277,78165.58461906224,Up,Up,1,1,1,1,1,78158.71635891867,Up,Down,1,1,19.53589486794,47.49486902947,29f336685b90f59598547c866f3b2fda093dbaf126a7c5e06c60a2544492c676,8a62ea985f6ac674bf2fadb20d5256c5544dfe81666bd56a3e4da101f659a75d,8e1b9da7bb7973af3fca79f4897624368e8944c86257ba59b077fd886921f2db,398fec6cea224dbc3e35e507ebaef5a64bda88443cab69af1eb3de261e0d2241,479731ec158dae6ae4ec98f725d5cb991846551cfa9f8a781269c9d9718a348a
4,1789002000,1,ok,78165.58461906224,78165.58461906224,78447.0853540835,78301.41109574407,Up,Down,1,1,1,1,1,78258.66755869988,Up,Up,1,1,135.82647668183,-145.67425833943,939da5d79cc16e1840e6c8a2def154ee241c8527456e60d9d72d62da5074daed,479731ec158dae6ae4ec98f725d5cb991846551cfa9f8a781269c9d9718a348a,398086455db4217e2b70d44add91852f7958f7b51452df2e1086bc523c219bfa,4d2f4b166fd79a823c85df8485bf5d0a4942b0f42c6dd6ed5da85111b54778f5,6f549cb1c8c662f9f07d10b0391d9d1181ef2f8d35c19b2e843af48bd8641b2f
5,1789002900,1,ok,78301.41109574407,78301.41109574407,78239.5390139177,78156.2440490353,Down,Down,1,1,1,1,1,78191.30377939618,Down,Up,1,1,-145.16704670877,-83.2949648824,dd333c4e3062d2acc2c37c0bddc91cc5bc286c8fb4100ae4acc00b35e06b746b,6f549cb1c8c662f9f07d10b0391d9d1181ef2f8d35c19b2e843af48bd8641b2f,eb719ddd03d9b898163880299c05205c9eef1c0357cbe17df63e7407ade57855,7d9fd7a67fa08edde9e10812e365bdf337bfa3b0908e4c58f99d5c4d7a82b4d9,274677a7831b6fa92a2985727ec8ab2767d640ce80a010b2dbb1eaa889555c01
6,1789003800,1,ok,78156.2440490353,78156.2440490353,77935.3898932715,78128.21643831622,Down,Up,1,1,1,1,1,78031.19081642033,Down,Down,1,1,-28.02761071908,192.82654504472,5cc91efd3d61ba76af29f08b5034aec40fd00e14bb481e8f90597caa6d208bfe,274677a7831b6fa92a2985727ec8ab2767d640ce80a010b2dbb1eaa889555c01,1e1ad62a14ee02debfb8442ce311af15e16c36f3994e71fcf4605a92818e2909,5afe67eec0984dc388b07893991e1f40141d0b702f7411db140ab5d3c2b3845e,23eabd3f4bb18fbe8a94782055dc9506e1d21fc9f75f5aa90355a95979ec8a81
7,1789004700,1,ok,78128.21643831622,78128.21643831622,77969.84601166584,78081.0287609906,Down,Up,1,1,1,1,1,78088.57064380439,Down,Down,1,1,-47.18767732562,111.18274932476,d98156287a610524d81b2bbca16e9c9ea31aa0dac4935baf68d3bc92711a7fcc,23eabd3f4bb18fbe8a94782055dc9506e1d21fc9f75f5aa90355a95979ec8a81,ef91015de5cfcc0f0c3492141ce2880c94e02e2640ae6005fb13098ccc234eb9,cbe79e04e0a5e62a6912c5c4efd011aa6d778bf8dc0eb495bbbe740a5edac466,6209236e36e8290e27d361d99650cb17837f70ae599827a9faf3f1fb92ffa33b
8,1789005600,1,ok,78081.0287609906,78081.0287609906,78009.09459403847,78007.71550378896,Down,Down,1,1,1,1,1,78020.05972112292,Down,Down,1,1,-73.31325720164,-1.37909024951,8709df1c0756b6fd957c826e13f55841c983f225694722a15af0ac561e0df789,6209236e36e8290e27d361d99650cb17837f70ae599827a9faf3f1fb92ffa33b,6952953d0a903e425f1c881ed1a67cfe6bed8214b18b76b80397ad4bb0ebf4d9,40cfe7a164cd9c3cfbfa0c557864e05bb257b1a9588161c39a18ab4d40a2b7c6,bffa2f1ec9fb98e1b3ccd2e357a618e534ee9ce005afae5f971b3995ff046903
9,1789006500,1,ok,78007.71550378896,78007.71550378896,77993.07048958661,77983.67806811098,Down,Down,1,1,1,1,1,78009.30486117497,Up,Down,1,1,-24.03743567798,-9.39242147563,0a5feead26b1e220812aa0986f850f9b99d5532d7c717321c36f15140e7e0eb5,bffa2f1ec9fb98e1b3ccd2e357a618e534ee9ce005afae5f971b3995ff046903,9c899bcb9f33e5a4b6df3a613d2bdc8aea7e4270a2c8d22d87985c87c148541f,967ee1368c1a7ff90db82f3542f585260f68d6056bee8bf9cd3283298b875781,d76c0683773f1a7b9f4ed1b2c5d46bc8914e3c173b8d5a69d474366c5ffd2cd0
10,1789007400,1,ok,77983.67806811098,77983.67806811098,78179.54083696728,78231.44094187258,Up,Up,1,1,1,1,1,78101.34371288358,Up,Up,1,1,247.76287376160,51.90010490530,8a5d7f1aaabb7afed25542c80fd89056bdecdb8df31c1b897da610514fe7d27f,d76c0683773f1a7b9f4ed1b2c5d46bc8914e3c173b8d5a69d474366c5ffd2cd0,d8394968b6bdbc07f6b52a3bf42ac621740affe5b863f074cc9dfe94df4ecc2c,b2439f3c87c8e58f5a03448ef783b42bb14c881f251a789fb04c9ad99783f67b,2593367fd425a9f4008249fbbbe9f5872d261ce01619f3bf29cfea7f1d985be9
11,1789008300,1,ok,78231.44094187258,78231.44094187258,78314.96668914653,78317.1660992391,Up,Up,1,1,1,1,1,78273.64207601247,Up,Up,1,1,85.72515736652,2.19941009257,7e17d170a7a044b5771f175473e4dbad6655531e309fd6ad7ce55713e0c2c0e1,2593367fd425a9f4008249fbbbe9f5872d261ce01619f3bf29cfea7f1d985be9,c98c1c5dd34b798e43b1282587bf6d5a9ce45e416ae6d820cc5c5dd26565ea76,adccb61ff80c9f52529794c907306c969d070232779856a90552a27639fb1624,fdc5dd05d0d06836fdcead6871bc8d74fd83a111548f7b193855806b79114571
12,1789009200,1,ok,78317.1660992391,78317.1660992391,78387.21132644264,78362.78395244612,Up,Down,1,1,1,1,1,78450.21421671307,Up,Down,1,1,45.61785320702,-24.42737399652,7bc0feb5006311a181c77055bf3d4ff9886c5b21e687c923d94ed999166ed51b,fdc5dd05d0d06836fdcead6871bc8d74fd83a111548f7b193855806b79114571,9d6222a4759efb75bc421029b8e02a73696252ae1338a12d1ef0a6ca79dce452,01aa9ecd2260b12ad35f36eee7634d39b131f9d84e3dfd9dde6b984fcf8c9f4b,c9780254397426462365495534adfc0c77b6a357e64f960de930d84ae4296cba
13,1789010100,1,ok,78362.78395244612,78362.78395244612,78297.61467039702,78362.07860858402,Down,Up,1,1,1,1,1,78339.62132443032,Down,Down,1,1,-0.70534386210,64.46393818700,b83b81e44726611f3e1a5b3303ad19cc0f5ef8327a42979b61a30142d74e71f1,c9780254397426462365495534adfc0c77b6a357e64f960de930d84ae4296cba,95db3dd53dbfceb7e41557159835a5341100ec122b8c83cdb26af0ee515bc2d3,d0294ff3c64d0b393c77a14d10423d7883e7e63edbd56adc9fcff328c381988d,aecfb4fd15aae9106d3fe292c5c8059e82aa36efaa117c7861e6b1a5b5be0b83
14,1789011000,1,ok,78362.07860858402,78362.07860858402,78321.10646524648,78341.49132932196,Down,Up,1,1,1,1,1,78414.53406267385,Up,Down,1,1,-20.58727926206,20.38486407548,64db4ccbbf2d267145f8c1e755b1db0f42e0d9824d184b96dcc71c4abc1acfff,aecfb4fd15aae9106d3fe292c5c8059e82aa36efaa117c7861e6b1a5b5be0b83,58f0792987cba2b27bb56a03519ed0d99548cc76b121aa301135bd0669cee2b4,0cbe1e65efab407ba0aff76fbbdf0fc149c1c181da6ceadbb968237383cffed2,e5a3ead2179843d67efe32a858c6da18a05b9c7f7f104fbbf0ee3528c7b96cbd
15,1789011900,1,ok,78341.49132932196,78341.49132932196,78306.8541319467,78270.82758933764,Down,Down,1,1,1,1,1,78415.6286249476,Up,Down,1,1,-70.66373998432,-36.02654260906,094ccca63e55ea329df23b00a486e7d8f5deff2cdabe743493bfdf97a622422e,e5a3ead2179843d67efe32a858c6da18a05b9c7f7f104fbbf0ee3528c7b96cbd,c5e5ef0e6b8f9eac07ec908b3a45ba197a3ea13814bde063b1f38ede8dad9428,5a35c7fd494a0ec608653491b053126e566b12d1a951df397e1295d327f91e94,4db6cbfe8b383140d5d05e51b70d5a45175b0c3f9e81fcd5f9cf502a92270ab3
16,1789012800,1,ok,78270.82758933764,78270.82758933764,78339.94685420349,78312.6845707022,Up,Down,1,1,1,1,1,78321.91242903512,Up,Up,1,1,41.85698136456,-27.26228350129,232bdd178c2f2759947b64a49e1d33c81a6b1b1a07787c2f2becd481a0b77975,4db6cbfe8b383140d5d05e51b70d5a45175b0c3f9e81fcd5f9cf502a92270ab3,a33c4b7c0971dc922c1f35dc8faa9392dd547355f4719b60a42632bcf3ef2edb,d587343d77abf73f246c9e3d5c72d3d559acfed01917fb477ead67020c139684,f0a772b7ba5d20590215bcde09b60e78267f727f1c2c71fc0c66fd3b7a35fb91
17,1789013700,1,ok,78312.6845707022,78312.6845707022,78349.98762717335,78370.52861589938,Up,Up,1,1,1,1,1,78364.22863773427,Up,Down,1,1,57.84404519718,20.54098872603,5be3eb3601f12ebf25e59d85c5e9e369ca5d4252b5c84c3b084c57367c6de61b,f0a772b7ba5d20590215bcde09b60e78267f727f1c2c71fc0c66fd3b7a35fb91,8d84b7fc322c3758b90cc19197a305cfd3fe2ae45eb5cce10c72f32777b226f9,c33e6d046cfbe90cbefe668d13eb7a74ffcea19985a573d9da93f631dbba6b13,d39dc9ed0e3f426d6652cd1a0c52c448b0c6f9eba70eadffc98843ed1605fc5d
18,1789014600,1,ok,78370.52861589938,78370.52861589938,78329.19920187492,78314.22811563523,Down,Down,1,1,1,1,1,78373.43114133582,Up,Down,1,1,-56.30050026415,-14.97108623969,560f2bf8d1311152252193f60246b904a46a023325c76129b0091cb60a4c1323,d39dc9ed0e3f426d6652cd1a0c52c448b0c6f9eba70eadffc98843ed1605fc5d,b21609ff8931518a8f66478c74532e886f84d976a5b2cb794977cb943cccf69f,c94919916252729a74b57c4109dd3adf8a8a92c3143dce82f9e263064b9dee66,c6221bdbe69f68350601d292532308a73674160d84bb7963c72694874d9ff534
19,1789015500,1,ok,78314.22811563523,78314.22811563523,78310.13574385042,78387.3901963535,Up,Up,1,1,1,1,1,78311.41567674518,Down,Down,1,1,73.16208071827,77.25445250308,32eb57de71e61e51e0c77bd88efb5d667634ad27934f5bf51382308063d0bdd7,c6221bdbe69f68350601d292532308a73674160d84bb7963c72694874d9ff534,a0c5235cdda51306eb0c5e42bacee5b02613317f512fb49079df795ce7c8121b,191f06c24acb9963e6a06147bd065123a45cb091e08378622283bc33af3f10a5,81aed9674bc9f82df6bb7cc41595716ad48cad4c594bd3f139fc26852573ccad
20,1789016400,1,ok,78387.3901963535,78387.3901963535,78283.85687699233,78399.11568714038,Up,Up,1,1,1,1,1,78252.99285284826,Down,Up,1,1,11.72549078688,115.25881014805,0687a0f5c472b0a05da86ae99db0d55f29ccb9db2ce854c341530900fc07e7b3,81aed9674bc9f82df6bb7cc41595716ad48cad4c594bd3f139fc26852573ccad,413b4debab66cd7af8338cf21acf0b3c4c7210e25ea5444dad4e022c8039fed8,c201edb49c5adc6bec6bfc69479ccfdb27aa4e624b1a00270746e5af079add57,859b5d408fc3c746117f7ab90376170e241e59de510247186931ff4f727dbed4
21,1789017300,1,ok,78399.11568714038,78399.11568714038,78345.67661791506,78468.3324384327,Up,Up,1,1,1,1,1,78350.94547291787,Down,Down,1,1,69.21675129232,122.65582051764,b18fb60d7bc1bd600fdd9913c649655b389e31a8a9a48f3bb356dcfb52a343a0,859b5d408fc3c746117f7ab90376170e241e59de510247186931ff4f727dbed4,1a814d75b1704b3f082142431b9fe190bddc34f90fee2c98eae885b650d40da8,403a5cb996743fe36e5b794bc3b64f6872e88dcd2885ac0393edfe0fd86da51c,168d25c99d8533603df02f8c535dec36dc89dbafc35540a38e3f13daa5063cb7
22,1789018200,1,ok,78468.3324384327,78468.3324384327,78420.83939735862,78389.63227961233,Down,Down,1,1,1,1,1,78446.25700341807,Down,Down,1,1,-78.70015882037,-31.20711774629,0f6781e17c1a838a724844715e659509b16b4a51a94ea6a74070b67c68742649,168d25c99d8533603df02f8c535dec36dc89dbafc35540a38e3f13daa5063cb7,61f0d5e4e47f92793d6919c884440423b1dc0c977b2dd4e1ffe5e5bfb2cfbf1c,e9c01cbfb9d4ae1ffe3bea27f46f74f0c1e7bbdccf0638e66123b2cfdf940014,e1d2712c6e9e33273bbda22f98faf51c259a486858d426d0ce75df051275f9ab
23,1789019100,1,ok,78389.63227961233,78389.63227961233,78486.24517850636,78500.91086091034,Up,Up,1,1,1,1,1,78384.31088555224,Down,Up,1,1,111.27858129801,14.66568240398,950b7a040ede45c815ad870298db2536482ccd3e680fc220d6157228297ef60f,e1d2712c6e9e33273bbda22f98faf51c259a486858d426d0ce75df051275f9ab,b3643d5ad4a1e3bd90748b2761fb208c2ab4300d639853a7862a3b7ee765a1e3,030ace3264f8dc0693d6b6b1be733d5f680b03dd64ead20ca6bc1482f8d0d7b6,47749bd4375edfcd9a2f7c629170e48f71a5f9da84acb2ae092cb019aca79080
24,1789020000,1,ok,78500.91086091034,78500.91086091034,78391.42830908002,78278.56516478992,Down,Down,1,1,1,1,1,78427.2904904181,Down,Down,1,1,-222.34569612042,-112.86314429010,a494539331d22b4d4990f26c3e9b60b57b691a54adf000c3531ded8476978f2f,47749bd4375edfcd9a2f7c629170e48f71a5f9da84acb2ae092cb019aca79080,12df7d2ef25b5b8f1d9885e9e68bf0d9a2462375c5ee9f2eccf443da8cd6b497,ba94410a5ee77f14773c5ee388c10f42ee85dd74b77fcee07d5b98c7fb812ea6,f1d5f7f9a7fb61ef5b200ee1196a2cd251e3d19306b1339740c8ad82737a60d2
25,1789020900,1,ok,78278.56516478992,78278.56516478992,78166.59333073568,78183.87439227755,Down,Up,1,1,1,1,1,78182.78185941318,Down,Down,1,1,-94.69077251237,17.28106154187,dc249a8130977d7f47c84bf6b1736d60b23c95cf38a49e715103885c4798f094,f1d5f7f9a7fb61ef5b200ee1196a2cd251e3d19306b1339740c8ad82737a60d2,c30606e7e38e039b3b351e6991efb3fbe59693389c7fa88d3078112831c0acdf,fd84c3c456c5fbe04e5dd487f797dcab4f25dc7a9f40917a19b0ce4262de0f24,2b129d106864c7623dd9e6ef6cdd14de134cece4b63da0679e1b3466788a401d
26,1789021800,1,ok,78183.87439227755,78183.87439227755,78156.31367922189,78164.75547678252,Down,Up,1,1,1,1,1,78143.9594736393,Down,Up,1,1,-19.11891549503,8.44179756063,50376dccce4c99516f00f6b19fbc08a2eec15db839db3f51cc8530b84018b841,2b129d106864c7623dd9e6ef6cdd14de134cece4b63da0679e1b3466788a401d,42a55f2f642f9c3909bf7e9d28e6bb7727371fd1a7e719778a233a0e6f0070f1,13236600b0a3b7450dc7b3046c99aec4656f84959ba05d4fb04079b49822c52b,ff18a98308c825b0ce5b8b1b5e5404413ee385764677a3425b8c9339165932a7
27,1789022700,1,ok,78164.75547678252,78164.75547678252,78393.81169041488,78390.82734765115,Up,Down,1,1,1,1,1,78402.29297103178,Up,Down,1,1,226.07187086863,-2.98434276373,f83c35bfed86df535be7ca41a2e3042e351dd36b42ea6f282ee6504b1ba798e3,ff18a98308c825b0ce5b8b1b5e5404413ee385764677a3425b8c9339165932a7,5e8a54b71bac114114d50ed5fec814722fd6276cef6837e76f79b966cc1ad4a7,5ba2fb7925f9974754fa480d147e5b425a4e5f7df42f3b569d041e0d839684ae,253bcd3c2d4f4a9fb34e3e1972fc0e4abf61d331d67f769326c1c0d7d9bd0557
28,1789023600,1,ok,78390.82734765115,78390.82734765115,78142.59401728374,78181.68628082289,Down,Up,1,1,1,1,1,78257.14931496639,Down,Down,1,1,-209.14106682826,39.09226353915,4390b86899b08a6f4b175af39462a2f392c7a949ace155ea39d75037e936a5e6,253bcd3c2d4f4a9fb34e3e1972fc0e4abf61d331d67f769326c1c0d7d9bd0557,4473101001409d9179ee5f4c1d3d074acf40834c3435ca4b0ae0954037cb98a9,4e0d30094040642931233d641fda2518c1f641c64d9d37a2b9cce71e9b7d93c3,76160f77eab4718dff6e88f1260c6446e53861dc1fb62934d747ecd0de5f9aca
29,1789024500,1,ok,78181.68628082289,78181.68628082289,78072.9660275432,78002.16278428928,Down,Down,1,1,1,1,1,78179.66643424038,Down,Down,1,1,-179.52349653361,-70.80324325392,46cbd3d7615ff5826cb39134b066747dbb4ca9c15744c688bff738544f5a000d,76160f77eab4718dff6e88f1260c6446e53861dc1fb62934d747ecd0de5f9aca,d8fe1c32f08d7f86a21f8ef15df95ab9b8ebbeaeabd210678102ba53b5200a82,f9c5a80107fe309bf9962ad74983ae033141b32f074d4dfc4a4ef3ddde71be72,f91d3b75ba919af2e4babe2617887716ed60b91ab0c2bcc7eff490a6b1c0f77b
30,1789025400,1,ok,78002.16278428928,78002.16278428928,77946.6547636639,77968.9363264824,Down,Up,1,1,1,1,1,77913.9127309279,Down,Up,1,1,-33.22645780688,22.2815628185,851febf1f177c520b94481acf45c89abb3f71c491d953ef96b55904c82dabfb4,f91d3b75ba919af2e4babe2617887716ed60b91ab0c2bcc7eff490a6b1c0f77b,d33b87451d3f6fbdd8fc8e11095e690843c6b99ea945fbd61babfae20f600b04,7ed1fb1511ce529add6e089d36e6f15971ee149f114b04b2067ce7699fcb89a7,474a43c1853968bfe936e02e68989e9ce72a9004c9872799fa59a65486e8de07
31,1789026300,1,ok,77968.9363264824,77968.9363264824,78082.8241026708,78087.68242348458,Up,Up,1,1,1,1,1,78035.20028180305,Up,Up,1,1,118.74609700218,4.85832081378,7ecdea6e631c22ecdcf7bb38eb872ba47bc7243b2ccb9e7862d640251f03b751,474a43c1853968bfe936e02e68989e9ce72a9004c9872799fa59a65486e8de07,fad2720f4bfd0987a5affdbb262ec1ef34348b425cb2da30a881ffad5e32cf1f,0d771d4bcfd81f9520861e34571fe6fd9711d1f1e25627a7eb99e7fbe947d8f9,3041557b3bfc9f1d1a530c95e86f0112447c8d00ea0c1ec2b19bac15eab642bb
32,1789027200,1,ok,78087.68242348458,78087.68242348458,78124.76927082468,78046.73330575664,Down,Down,1,1,1,1,1,78093.48908140462,Up,Up,1,1,-40.94911772794,-78.03596506804,c73775bbc9e9b41681f20d6d4f657c239ea56b8e2d3d92555a4c7abb3d7e7eb0,3041557b3bfc9f1d1a530c95e86f0112447c8d00ea0c1ec2b19bac15eab642bb,9adee8c0ee73ec216fc33da2022a0aa83cd7d0c82eb751fda742f90dd2c2bc2f,040c3c95e1f26889edbc061908531bac215847c6792b83efb9ca29014e4bfd13,b6ac320e4047f6570e12cd4536e194138fdb07ecd75334f57317d12c04ea199b
33,1789028100,1,ok,78046.73330575664,78046.73330575664,78133.09345767385,78133.8960336972,Up,Up,1,1,1,1,1,78034.12974960207,Down,Up,1,1,87.16272794056,0.80257602335,ee9536087e41a40bc0d25efb9e096122d3d9be0b2727c2b64d2b7941082fe4f8,b6ac320e4047f6570e12cd4536e194138fdb07ecd75334f57317d12c04ea199b,9a37d5b36418519ab3b27ec2fde2260f05465c6cbec7f5e9e96dfdeab9b96fe4,f73cee0cb4e20b57c9fcbeecc0324189faca4a45234834919e00003b57febf91,3040a3e3ee91e2965354ca952f021bc2864eb1952d531474cd50b7dfd3440135
34,1789029000,1,ok,78133.8960336972,78133.8960336972,78092.28502733899,78058.57233626726,Down,Down,1,1,1,1,1,78092.70204013622,Down,Down,1,1,-75.32369742994,-33.71269107173,915f13f420e9e679e9a6d19388dbab402a00ecb62c3ddf80fb1542d1b3a6c360,3040a3e3ee91e2965354ca952f021bc2864eb1952d531474cd50b7dfd3440135,57d059015187d55811c1e1a6864d9c63d7fb24c147f9e8d89c47c95632bee037,378feef482db0eee23f610423a8dfea5aac40225f0f6c17ac2236c9ff23d4bba,12ac820d0846fdb90034e3ca0ef832eb0695ecc728e0244f0b7cae70cefd788e
35,1789029900,1,ok,78058.57233626726,78058.57233626726,78139.10593913459,78079.18829171499,Up,Down,1,1,1,1,1,78071.15211367543,Up,Up,1,1,20.61595544773,-59.91764741960,765d6847e99b0a264819e656eb24e8a5514367fbe921041b148e8584bcb9b8d2,12ac820d0846fdb90034e3ca0ef832eb0695ecc728e0244f0b7cae70cefd788e,15b84aa835191a46bb6ffb2291b59b72a7b8defa2ef9a5a6c6abdde6cecbec92,6da2221612d9a44db72184b5998af1af9fe360060cea3b29c45e2ce76d317cb9,54fdabee52ed891eec982220cba74f62b8ec87ee256989c0bfa9ac1c38aa443c
36,1789030800,1,ok,78079.18829171499,78079.18829171499,78114.38068926647,78109.62125266965,Up,Down,1,1,1,1,1,78148.16476378508,Up,Down,1,1,30.43296095466,-4.75943659682,cc8ba9b8db05e0869fc462dc4cf8a7074bd5b9e510aa564660481501c74797a1,54fdabee52ed891eec982220cba74f62b8ec87ee256989c0bfa9ac1c38aa443c,62d153213a67e9f17086f0d4a2a0a7f3f18ff0677a3b0c3e0cefa83aa6bbbb7b,7f3a7916d095f2bf898ba3622a080b7c6518b1a9650279a772776f599452a5b8,9abf082bf7c3bd3a16722fa6ed540f08dee96107a03c0fb33db6e88ee874ea84
37,1789031700,1,ok,78109.62125266965,78109.62125266965,78168.20934854369,78176.33325953038,Up,Up,1,1,1,1,1,78165.19348439982,Up,Up,1,1,66.71200686073,8.12391098669,682c6a4460be2d46d2de5428ef9d31fc51a67526dcd27d7ed5fca76adcfd6c05,9abf082bf7c3bd3a16722fa6ed540f08dee96107a03c0fb33db6e88ee874ea84,4776a78f90e9d57f1ffcff70bc007eb768ad029345cabcc82435e86eca2b738c,6015032424c8722581a7f36eef415d66a4ea7ca5f0a0286e37ecc61107cdd7bc,593df530a8286e8de0bc074e380949d5911789ba8a6053d086d029cd0dd65689
38,1789032600,1,ok,78176.33325953038,78176.33325953038,77968.11793748569,77943.44146472016,Down,Down,1,1,1,1,1,78069.89162825399,Down,Down,1,1,-232.89179481022,-24.67647276553,1ef6c9aa504fe3f17758a0d1c0a544710f96ad283e5804e14c941aa905af63d7,593df530a8286e8de0bc074e380949d5911789ba8a6053d086d029cd0dd65689,59b72d045189b80ca7f4cf1b92d3df46ba64c85a9f5b7c57ed45d2c36ee6b30f,b184972af5927d446236562260cfeefccbe6307e1da6fcda7fbef4e0b17404bf,aa9ad8c75c192d040b16950f144bfd1a31ffccfd904f972c860e8540b617aef9
39,1789033500,1,ok,77943.44146472016,77943.44146472016,77979.98737803145,77935.35204315932,Down,Down,1,1,1,1,1,77958.94098654197,Up,Up,1,1,-8.08942156084,-44.63533487213,6f271014b42a511baba2734b608f5fe09e5f8c3f910566b29f92b9085c469c83,aa9ad8c75c192d040b16950f144bfd1a31ffccfd904f972c860e8540b617aef9,3309e09a6354d828216341242154b3c3e25d426fdeaad4466aa4fd48662c73a7,b72df5f5ba2c77026354312a5f9b421bfc014506d8c9c27815df724389afde6d,1db234eebb508253442630669e582e545dedf29f8f64e5f1c072daf08be03458
40,1789034400,1,ok,77935.35204315932,77935.35204315932,77941.19181584542,77961.73920334085,Up,Up,1,1,1,1,1,77985.38429586562,Up,Down,1,1,26.38716018153,20.54738749543,ba482cb31f1ffa15910f889ed7587696ea9bae8ddde876312c46a8ed996948bf,1db234eebb508253442630669e582e545dedf29f8f64e5f1c072daf08be03458,1f67ed9223900f68c18b965138f1b47beab6e0bb88adb2806247783ad7c1b1f8,e2be09f4e19b75b6bafbbdcba70989f99e4fa66d99198cfd72dd9dddc77d5c55,dfc330b708e2b296bab0ff3db2b98b2de24a4c15acca9a17d046d39959f32133
41,1789035300,1,ok,77961.73920334085,77961.73920334085,77929.3109339514,77951.2381818053,Down,Up,1,1,1,1,1,77960.66156700253,Down,Down,1,1,-10.50102153555,21.9272478539,37a143f82d0702e3e687b7bddabda10f17e6341ce592f69367668871cea9d080,dfc330b708e2b296bab0ff3db2b98b2de24a4c15acca9a17d046d39959f32133,21a403299a509a6b6ed1b9487933e89ae909c0bda83ccc7966d2ee231c31c928,343fca2e8a2bd171c53a4bc4e603b7d71229a35294e3168a436d2bcdc3f47535,6bbb020d94277687419b7563f462c985fa4ff8ec77df9b76b9fcfd8446da5d3b
42,1789036200,1,ok,77951.2381818053,77951.2381818053,77992.7092660935,77959.33744016201,Up,Down,1,1,1,1,1,77838.61125417026,Down,Up,1,1,8.09925835671,-33.37182593149,d6fc4414f7b213e8ab7f00ecbe389298bdef199d608f8fee8aedc0fb29fdec51,6bbb020d94277687419b7563f462c985fa4ff8ec77df9b76b9fcfd8446da5d3b,c0ba1392978709a51cc5657276580b41cdadd41b90078be60c7bf75b9ba7b088,4d54c58d6bc5dff9fe341e9127be7f7ad4f7c33026c9b7ed948deb2c6f763989,dac772a08269ab0ea69597ea589c023e7bed0df8f07d83b5c405ed642f69076b
43,1789037100,1,ok,77959.33744016201,77959.33744016201,77865.00461718025,77851.01860301352,Down,Down,1,1,1,1,1,77943.85495606261,Down,Down,1,1,-108.31883714849,-13.98601416673,a08e32422d72697019a09fa7ac483c128755836c2dc170d605be5763a0b6f419,dac772a08269ab0ea69597ea589c023e7bed0df8f07d83b5c405ed642f69076b,94d4833fee98fef528d3ddb945adb85c7557e0696e1ec617099fc6f0158668ba,e140ab228a4f12237a7173b366420c8fbe24e7e254fcdcc51e1df8f8febb219c,a46546efbb4f71b1ba974b90ec935373647f17cf22e5f00330949a3a5733b705
44,1789038000,1,ok,77851.01860301352,77851.01860301352,77809.90252906864,77866.54056535148,Up,Up,1,1,1,1,1,77781.09491800444,Down,Up,1,1,15.52196233796,56.63803628284,526fc1b4e343590aac7d20d694e69e74653dc941d3ce2dad09bd7f303649b8d4,a46546efbb4f71b1ba974b90ec935373647f17cf22e5f00330949a3a5733b705,c4768fe800ab2ccb8f28ac09564ba4cb9bc99631928b6109563b2d33c79d5d13,2630b7c6cb821850a6de8cad9d3d2ac6089036eb37141f8353342231ac473fd3,135385a7ba052b829e22a88ef09257250b6c86d78d70c2405de53b687d7fe71f
45,1789038900,1,ok,77866.54056535148,77866.54056535148,77981.12400468437,77970.90852036756,Up,Down,1,1,1,1,1,77936.31482678701,Up,Up,1,1,104.36795501608,-10.21548431681,0eabbfa18642015af6f5485ccea78d601ee38aa231586360edffe5a2b17b671c,135385a7ba052b829e22a88ef09257250b6c86d78d70c2405de53b687d7fe71f,5b14e34cbaf665a2b576720dcd98b4e690df57e2c4e96d0fb2802be6b20e5be2,f7ace6866424405d1125c759310b1d069309507bb748610749edf229569bf83d,2e2308f98d7d654e5cdaecf0eb04c44a940be706e29ac81831a6d221e67a6195
46,1789039800,1,ok,77970.90852036756,77970.90852036756,78012.99196675695,77965.427627578,Down,Down,1,1,1,1,1,78009.02725666278,Up,Up,1,1,-5.48089278956,-47.56433917895,a151a33123fa28fc139d18048ca4e21b6e8bccfe11cdeeb52e21888ce8f52d48,2e2308f98d7d654e5cdaecf0eb04c44a940be706e29ac81831a6d221e67a6195,721e15f2e614e2dde291077cdf8934068d6458f6741a4a104b3319a46bea807a,eae537a482be0aa058aa5a7ba1cbd7beef2815b94c0baa2b64f69f2eeb8b9dc3,96273dfd522250d17337b15dc5be3877cd1681ff24da9eb894f1e49e4283c171
47,1789040700,1,ok,77965.427627578,77965.427627578,77886.19732097082,77841.66813186124,Down,Down,1,1,1,1,1,77921.52278654193,Down,Down,1,1,-123.75949571676,-44.52918910958,5c08ff1f481b5c1e2a769a504851855fee2541c90b8b0ae80d4d209b83f66f2d,96273dfd522250d17337b15dc5be3877cd1681ff24da9eb894f1e49e4283c171,8ec5854200adefbaa505331ef710dea3efda42f37a320efc86237626aaca6e91,d857fd1252d244686e3bf24171eb3e4a9c646e6cb38086e3b4d68d307c33cc21,07715f471ea1a23639f6e2f5092b008011c534e35908c801536e42c90151ca85
48,1789041600,1,ok,77841.66813186124,77841.66813186124,77697.94437908904,77798.06937721721,Down,Up,1,1,1,1,1,77756.97756033039,Down,Down,1,1,-43.59875464403,100.12499812817,5c6c8719184aa20f26dd526df2007bc4e356d0b5092de2f8b14c9ab8dc58e546,07715f471ea1a23639f6e2f5092b008011c534e35908c801536e42c90151ca85,c3dd5787400a035186792f1d18f9586d729f88265057df7194cb511116bd8ded,179bb3c4ec33d0bfe0bdc66ce6e81880765cf7b901fa9eaaf6a308e82aa46309,b5501c0d6b6b6588fcd88e0197ebb329d8dbfdabbea880e0019c1b887efd9e93
49,1789042500,1,ok,77798.06937721721,77798.06937721721,77715.41740948678,77722.74452152329,Down,Up,1,1,1,1,1,77737.72999199171,Down,Down,1,1,-75.32485569392,7.32711203651,5cade228cd599a8aa8e9d43ad5b7245bae1a122afd8b8c3943312ed1bb844902,b5501c0d6b6b6588fcd88e0197ebb329d8dbfdabbea880e0019c1b887efd9e93,cb0979ceef80f9d20e9b0a72baf81faac2d6e6978bb9dba0820b3f8fd1623dbf,25e272be5d183738f6ea4ac92b36265990b53f9d0dbc39d8b7cec1d73315ee0a,4652295ec17f64713c6f1f5eff06bdf40a9ceffa47591c0358f5d19292fb67d9
50,1789043400,1,ok,77722.74452152329,77722.74452152329,77053.67280861265,77104.65133364187,Down,Up,1,1,1,1,1,77394.87108814674,Down,Down,1,1,-618.09318788142,50.97852502922,10e6b0271b86926f7246cf0d7fd4a489e42e62bb7d8c11ddc86bfefade8e0e32,4652295ec17f64713c6f1f5eff06bdf40a9ceffa47591c0358f5d19292fb67d9,a9724a3da28a098f515053d8d8d0d2d43b3738fb48763491cf984c03971c2582,dbdeb0c4971104282373ac1329f9accbeb09b5d5cea4cb4dcab644266a098859,5f5e3c17dd6c01cf9ff5d881d1ddc20023a893f5fa314079f3fd0d458e0861e2
51,1789044300,1,ok,77104.65133364187,77104.65133364187,76854.29465824828,76859.38810003125,Down,Up,1,1,1,1,1,76969.73466497668,Down,Down,1,1,-245.26323361062,5.09344178297,b23c35add785805485a39cb29a5c772073cc22a633f7f3674f193d3e9e61cece,5f5e3c17dd6c01cf9ff5d881d1ddc20023a893f5fa314079f3fd0d458e0861e2,897466aef7fffde2ba6028bf0acedafc3ed279dfd864e0b97558c8567c6c083e,87e71cf37c0cd57ae1ac01f4d02386f91e6e89ea5ae3c34ff6644eb1105b10e4,7940c64dc472ff30b65203157bff347da73ca9ca0833c0bc1b3eb64c66beb76f
52,1789045200,1,ok,76859.38810003125,76859.38810003125,76946.18974868667,76778.05211989283,Down,Down,1,1,1,1,1,77028.41821169681,Up,Down,1,1,-81.33598013842,-168.13762879384,ca6f9b492427664b5393f389e59829939ac457829556d9083e4fb2179b8b23a8,7940c64dc472ff30b65203157bff347da73ca9ca0833c0bc1b3eb64c66beb76f,37c9e653a1abeae6d5ce6ea58a42687cdaa5e15e36620026feb9a59a4c10f937,63913bd78181131483f591a04a3f2a274d65c57758e005f0a5f1c34ac0104639,c1dced80e1ed0ddc837a98b46622a910581626656ac38ad392d27fa175ded9da
53,1789046100,1,ok,76778.05211989283,76778.05211989283,76894.2439512744,76927.45495467987,Up,Up,1,1,1,1,1,76778.06940324116,Up,Up,1,1,149.40283478704,33.21100340547,7d42d8ab998b9207b066b9b1b4b3d591b50729ee12700f76dcdcc4bc893fea83,c1dced80e1ed0ddc837a98b46622a910581626656ac38ad392d27fa175ded9da,7408b8b7df29032aef9fff44e269d4ed970b65fca85edce20e37449bcbc6bae9,dcd47a2519ee79786a5338b223c2c628212f18af627b6e0e3f6cec7afb2b96fa,b42f0e69c1f3508a4252b0b598860b392fe4fbe3c23a1cb9d56c4d165a938e39
54,1789047000,1,ok,76927.45495467987,76927.45495467987,76974.46840483429,76944.97956783141,Up,Down,1,1,1,1,1,76877.43240300671,Down,Up,1,1,17.52461315154,-29.48883700288,184520107f249c810216bb5386f191b9565bc9903a4d4e6203fba36012723baa,b42f0e69c1f3508a4252b0b598860b392fe4fbe3c23a1cb9d56c4d165a938e39,5608bac6415d31cd77d0b5b48e67777d3710f8f1354ef333c568f6217b8a9924,2f791b05c1c7c3e27be7c6035367c5f235aaaffb6df8d0e028574fdd3e280f9c,10b934503af0e173d86b24ab8beaf56f7b00a279638c265b8bfbbc5922febb51
55,1789047900,1,ok,76944.97956783141,76944.97956783141,77174.80536178245,77176.79239620663,Up,Up,1,1,1,1,1,77040.37472195378,Up,Up,1,1,231.81282837522,1.98703442418,84a089cd2d46b54768a238dab18d53fcaaa354800b8fa16c535dc39d96a23638,10b934503af0e173d86b24ab8beaf56f7b00a279638c265b8bfbbc5922febb51,cf630f7e5883bf8dc36b66f83d6385ecd2168b94c77f191e1d60c4fb8e68a53d,5dac3acbbc327e8efc7f72bc10cd7a04f136ccf580f1a3011a3fd320b82c257b,784fbca8d1b19bc0c2704d965b1b27aa9f85c6ebb20986186840da7ea7d51c81
56,1789048800,1,ok,77176.79239620663,77176.79239620663,76966.30339945157,77091.62852412158,Down,Up,1,1,1,1,1,77206.88228469176,Up,Down,1,1,-85.16387208505,125.32512467001,ec1fe753cc75ffc933e1e7741aada10cf2adb9cbba3c5554d90d33a62b3e8320,784fbca8d1b19bc0c2704d965b1b27aa9f85c6ebb20986186840da7ea7d51c81,a0047d74e9031dc39a7ee86e02ffba4cc5a23935317305a837a8786967dc810a,2ae273b397f83774d6d14d516ac772ae7a26b72f514a225b83811fcea14b9709,b86a9628ad070c88f689fa716b5e530e9716daf839e98f37fdb8cedc7f6a872d
57,1789049700,1,ok,77091.62852412158,77091.62852412158,77150.4385487782,77318.81724083355,Up,Up,1,1,1,1,1,76971.07443570842,Down,Up,1,1,227.18871671197,168.37869205535,4ea7f6df0484fa117ad4c509db97b081206372bb21fa9693af07e287b93dcb35,b86a9628ad070c88f689fa716b5e530e9716daf839e98f37fdb8cedc7f6a872d,9e3b61428c5e9b47765e2ea994ca2cca72cc1acd07b77df5f5f59e97b67016be,5d2254a9633e1affd3fe5752e1683316c7ba25f6ae7a63f05cf66fa8e385bdc1,fbeafd681b1746b596ccb829dc36a4856961c1647701bc48a617bc2976c10ea4
58,1789050600,1,ok,77318.81724083355,77318.81724083355,77223.23484229567,77246.92741679208,Down,Up,1,1,1,1,1,77262.5517418417,Down,Down,1,1,-71.88982404147,23.69257449641,f395c08512ec9402aadca3f154f61532bb47976fdec040bb762c69ea1f15be5f,fbeafd681b1746b596ccb829dc36a4856961c1647701bc48a617bc2976c10ea4,61dbc21586c4b0c9135c751340655efc91726f52931ce7acbc342195a0ea0c1c,2a215b32eab709d28eecd4d1e85ddbd6b30fe1221bfd89e65a2de92b81014539,8a3652a15356cb98aa5fc8a05a0211991579d54648a981b7bcf0669c08518773
59,1789051500,1,ok,77246.92741679208,77246.92741679208,77358.2974653526,77367.65347016623,Up,Up,1,1,1,1,1,77309.52044004963,Up,Up,1,1,120.72605337415,9.35600481363,d01e547b6a153a604745342a70bcdea8dfa73052d673d7657bcc626924f84bd1,8a3652a15356cb98aa5fc8a05a0211991579d54648a981b7bcf0669c08518773,e8008e75a4123df6a5658d7d502bb5724583e24a9f5333ad029e4cdb41428e43,7e3fb9ca264450b4d6a8f87597d33a4cc6617490ab9333b6b81e0b86c0c360e6,fbad420194939edca204241377646e941fe9a180b90cba097e1e87be40f4db16
60,1789052400,1,ok,77367.65347016623,77367.65347016623,77339.00242003232,77308.36083126294,Down,Down,1,1,1,1,1,77282.98453095517,Down,Up,1,1,-59.29263890329,-30.64158876938,053f3ee31f037651bf0c28226c59b876924a1b941051fccc2f5e2f85131032ec,fbad420194939edca204241377646e941fe9a180b90cba097e1e87be40f4db16,bfa7051950558c840b045b3938471e0a9dd49a106e5eb4d0030598b82133dbc5,88f3a2849a0c08af52f027d13dbc7b60fc139357c475e9a2bfe6cf9721b96be3,cc13aafef4cc39dc553c019a08f5ad6410c49a55a6ce72846f1e5986d0af539b
61,1789053300,1,ok,77308.36083126294,77308.36083126294,77138.9913333538,77093.19803388818,Down,Down,1,1,1,1,1,77237.90129277576,Down,Down,1,1,-215.16279737476,-45.79329946562,4a769ee2efaf86c722db820512db84d89797234a5d1c9a95217ef375fbda34ac,cc13aafef4cc39dc553c019a08f5ad6410c49a55a6ce72846f1e5986d0af539b,2a11e49fbcd2d654de03497a318ff5e3f4a4788dbbd6e40eff6cf3e83d8d2df8,c2e867632d97c24fa3ac1b2aa1d72650d30f0a17c14ccf3e4fe8e209539ed041,66e074136cb1a1e79a2779a88d26d145567c1c14a9e540490c6fa2b62b2d157f
62,1789054200,1,ok,77093.19803388818,77093.19803388818,77252.71489230069,77199.46794881158,Up,Down,1,1,1,1,1,77163.33348558715,Up,Up,1,1,106.26991492340,-53.24694348911,480406f72a22451304ff65a61fad565772f3a5cf453023b7471e41882f41b793,66e074136cb1a1e79a2779a88d26d145567c1c14a9e540490c6fa2b62b2d157f,6995e3b26dfcb2ee01f0402533de0001dafd226c7b1024ea688babcaa213f6d4,1abc19509dc112a6b6ec981903069ec3b5ef4d0ae831e41f5c41c302041e75f2,a36470c4c57ca26e04745de5ff0a4d9a7dbea1fb9cc551597935e653afc3bd55
63,1789055100,1,ok,77199.46794881158,77199.46794881158,77122.02896003216,77208.88715118053,Up,Up,1,1,1,1,1,77120.73235821111,Down,Up,1,1,9.41920236895,86.85819114837,4e702f315b5ff0c11774210d9486d7558be33422402a3ef6030aa338e54eff67,a36470c4c57ca26e04745de5ff0a4d9a7dbea1fb9cc551597935e653afc3bd55,efe8fba3c93e00619b9a693616a296f4b5c53ce67b278a17bf4f5689316f894b,8af086f16c27ddaf263b769af58792d4a6a93875008e20c8f8ea900b6509bbca,24c0d4f70352165967bb159badc23486352c6b9a7f6b84e3d2cbec4625ddfa4f
64,1789056000,1,ok,77208.88715118053,77208.88715118053,76920.9982893358,76952.8483558589,Down,Up,1,1,1,1,1,77091.91037195263,Down,Down,1,1,-256.03879532163,31.8500665231,caa4cc7954c5cece80c3f4337124a85113f857f9f09323288c6ed384bf561fde,24c0d4f70352165967bb159badc23486352c6b9a7f6b84e3d2cbec4625ddfa4f,907541b922d3e6700ac626379454d9d6ee477cef2a0ec0f4ddce99f301c8d369,b94e867da330354533468da0e71b2f7e27ef3e20262316a11530e1c1f7af3304,d3af3d530b9b28950d3f12a3f7b45b842de168b539a238da77574f7dcc53fa6d
65,1789056900,1,ok,76952.8483558589,76952.8483558589,76962.89299205651,76900.18522572493,Down,Down,1,1,1,1,1,76868.3186931264,Down,Up,1,1,-52.66313013397,-62.70776633158,326f4f8cb633ff7ad00342e2312ddf087a076cebbbdeebe8bd5ceeb65d9f96be,d3af3d530b9b28950d3f12a3f7b45b842de168b539a238da77574f7dcc53fa6d,802ea22d1a81157909a80124bcddcc70cd0e9125a4aabe54c5765f86f17ee6f6,b8e99511449cf91fdefeb5a61f6fcbf8c15b27d6286a797dbba84b887aefd3d4,722924854d1c742be416f766c784dfd0cf20b145b32eaa4c1d18a3c06939278d
66,1789057800,1,ok,76900.18522572493,76900.18522572493,76947.68076384562,76985.51560038916,Up,Up,1,1,1,1,1,76849.12131078613,Down,Up,1,1,85.33037466423,37.83483654354,342f66cfa98aaea83fe60be95ee26a685880bd53af830fc561f0e4921b441456,722924854d1c742be416f766c784dfd0cf20b145b32eaa4c1d18a3c06939278d,9fa09fc5e255e1a5b2e48654d7b33fb2c87db1fd31e2e1c352a961c897e68cbf,0d8f1df859f573382d6ee226da0d3ee4c102e6148312238a36eac9d0b4c06c72,6b77bee53062114ef30ebdb2ab13a2747f5230633df3f3426b9813987824d5e3
67,1789058700,1,ok,76985.51560038916,76985.51560038916,77055.43127387509,77162.74182063523,Up,Up,1,1,1,1,1,77107.0317484837,Up,Down,1,1,177.22622024607,107.31054676014,1251120b93fc63b14c80adc164eed5d073b7097e9f67ff9c363522aa832c44b5,6b77bee53062114ef30ebdb2ab13a2747f5230633df3f3426b9813987824d5e3,8520228bde1b8d6f67986414183436df51f3c8c1ca61eb4dd9cba4ef3c828bcf,199010fa90107524e6fcfb580d51936d88d566fb242fc2f7de4ac1df911586fb,e7cb2093dea759dc57bbd1fe68ad7f2861cb49d8a6d526275bfecee21709ee0f
68,1789059600,1,ok,77162.74182063523,77162.74182063523,77109.72976891333,77135.21842809427,Down,Up,1,1,1,1,1,77103.24905599744,Down,Up,1,1,-27.52339254096,25.48865918094,d42e9b9d339065ba36585b164718650849385125db09ff2f1915eeb3c19a6c41,e7cb2093dea759dc57bbd1fe68ad7f2861cb49d8a6d526275bfecee21709ee0f,ccc0b81f83c6ea03dfddc33ff1cafe91de3b7727738bc64528aec3ec7902b0a6,1b42b2655137b0160c9ea080520579895170aeab250780a0820e5cabbde3384a,0e48c3cdb5759a633d70a64b67d598f79dfc15d457eaca35d4de98082de5d767
69,1789060500,1,ok,77135.21842809427,77135.21842809427,77234.99992818672,77288.95780687754,Up,Up,1,1,1,1,1,77111.28384757321,Down,Up,1,1,153.73937878327,53.95787869082,6355265d24c1667947009d9deafd862e9a1f421454258508af2ed58e79e69f85,0e48c3cdb5759a633d70a64b67d598f79dfc15d457eaca35d4de98082de5d767,cf8aa440863e9bcb39cf1d9060b1b434c537f0324344d0ec4659f41dfaf731cc,e523ca8073d0911e2d50c43924619b5bb66ef3cc912a432e7a1c8a2c11eb9871,3978278e288d0deaabd9cf1a8ffa7509742f584915738a623cc8049cfcf32ba0
70,1789061400,1,ok,77288.95780687754,77288.95780687754,77339.6935728633,77326.35437116234,Up,Down,1,1,1,1,1,77417.84142235764,Up,Down,1,1,37.39656428480,-13.33920170096,bc90b00a93369e03d01cd6297c6ccad00d5aaafda272d9c2b2e8f53c79f79b2d,3978278e288d0deaabd9cf1a8ffa7509742f584915738a623cc8049cfcf32ba0,b93c5c93759f3cf7fa7a6e0cb967d13c838b0e20e214e9f14747f7017feb926a,2bae440a16effc288f4ef05e78c1d3a18bd51038f19a04e88191d5ef8810f541,9d3f0cddf1d0f1a349040dc9ba0d982c098a039802cf89e81ee92ab40bf30faf
71,1789062300,1,ok,77326.35437116234,77326.35437116234,77372.98389262197,77305.51591877095,Down,Down,1,1,1,1,1,77369.07500612969,Up,Up,1,1,-20.83845239139,-67.46797385102,78ac1b5abcb18138e6c5caea07c39103b2bb6b39b8ffbd91f44a7bef59273ab4,9d3f0cddf1d0f1a349040dc9ba0d982c098a039802cf89e81ee92ab40bf30faf,ec10dc6806c2064a7eaf23bffba44cc7af32f94ca87e84950aedff53f38beb4c,cdc0531866b3189e7ccb090ae5b71c5d20a3438d96abf5ce2960d5007e54d673,448589243bedab640ab91ec7efb844784f36c8616436096e30e1985d5d7cd13f
72,1789063200,1,ok,77305.51591877095,77305.51591877095,77021.44515447697,76989.02720149234,Down,Down,1,1,1,1,1,77156.90449774603,Down,Down,1,1,-316.48871727861,-32.41795298463,f4c2001158a35e87c4610d4e0621134129ad1e07a4a98a3c5557d318972d5919,448589243bedab640ab91ec7efb844784f36c8616436096e30e1985d5d7cd13f,634c4c2eda87c4822a9af9d5d6f58056083e24a5d1ff4eebd9344e82f03790ed,960242750a864b76a9851ebde87ba29725b0e7f01671baa5e68fc8f168d74755,04edb2fbbceed07d1e2649519fc997dce2d81ce4238e3b44fd833e0bc9c9fa4e
73,1789064100,1,ok,76989.02720149234,76989.02720149234,77074.70886904445,77050.53410292504,Up,Down,1,1,1,1,1,77006.4598872457,Up,Up,1,1,61.50690143270,-24.17476611941,de0ed9d7717e29085e735fb7e405afd583bb6e69e4102fe9792c53d68aff4368,04edb2fbbceed07d1e2649519fc997dce2d81ce4238e3b44fd833e0bc9c9fa4e,bce029abc9e7e06a60acd6ae99b7e656e7f14f9bd6d98380240c403ceaddfac4,33addf633602fff929401104443d0944b6e46b24e42e0de53b4a7fb251d7fd9a,7e1f29e0e6eb7edcbf8312c0517424ded85bf8e042cb0694f99f2f3ab6133643
74,1789065000,1,ok,77050.53410292504,77050.53410292504,77124.00420600895,77116.72618282255,Up,Down,1,1,1,1,1,77026.89889091147,Down,Up,1,1,66.19207989751,-7.27802318640,f74f9225ec396cf3faa69104274871fecc8d76fa57486ffaadb4f1daf41402a7,7e1f29e0e6eb7edcbf8312c0517424ded85bf8e042cb0694f99f2f3ab6133643,a13d0f010447dc83c8e85f4b5f94584d1655b8dd9e72c4e7cf79016f26681ce4,dacfb538abd977cc9d96bab252310cc3edb296a423a92f5dfabdf78e19184dff,af52c6128f2b2d09fa0a19fdd04b0cfcb85d93d5f0824befb98cb9d30ea333a8
75,1789065900,1,ok,77116.72618282255,77116.72618282255,77243.54262999348,77208.64573947979,Up,Down,1,1,1,1,1,77098.26352943659,Down,Up,1,1,91.91955665724,-34.89689051369,d755c5953a47867b57b1363d5e8359e94bab401e3417b3e9896487881b34f388,af52c6128f2b2d09fa0a19fdd04b0cfcb85d93d5f0824befb98cb9d30ea333a8,2a09089fdf8517028b270a5ebff0ba4b949bec7a2216ddbc2e9676960ab32090,2f1b52d76130bdb799c8e4ea0d4b986d4908437d4c5638c3485cd47f4e280551,e45e044f7c86889492cd8e6f72c70995137727de8394170dbf76af9f86d1fd77
76,1789066800,1,ok,77208.64573947979,77208.64573947979,77152.27730352028,77131.78197920935,Down,Down,1,1,1,1,1,77188.27186480329,Down,Down,1,1,-76.86376027044,-20.49532431093,5fceb4c05d38c4a09421464e6361cb8710ea330e265b8d3bcb6d7b981ff1bf94,e45e044f7c86889492cd8e6f72c70995137727de8394170dbf76af9f86d1fd77,cc1b04de4a77c2387233da3a627dcd944a92d8953a5d792af5ace090a1d6e901,dee50db97fb9124c8ff5c577563545c1b7e1ddd1f2771a098749125e3eb69acd,b64d487c2b527d24aa6244898d0004f180d5320af80ef0fc2886679ecdca1278
77,1789067700,1,ok,77131.78197920935,77131.78197920935,77120.0450619005,77185.29626413062,Up,Up,1,1,1,1,1,77128.5010436972,Down,Down,1,1,53.51428492127,65.25120223012,9ffbd99cc168b69169eb1ad3e78a86cb32150d09065bb7c7927eeb496582a5e8,b64d487c2b527d24aa6244898d0004f180d5320af80ef0fc2886679ecdca1278,20718e695b287a42efbddc3aca9380aaadfa63d197efc7a5da7e71e787ce048a,ff43a6f6ed2deffeb3268edd870171bb72f6610081e6ae886b58b3b4a0d05660,864bb483993b06c78c8cc720e8767cf3a3ca602f16788eefe903db358e739d1f
78,1789068600,1,ok,77185.29626413062,77185.29626413062,77135.32838957116,77219.66411152983,Up,Up,1,1,1,1,1,77123.8903769554,Down,Up,1,1,34.36784739921,84.33572195867,43d0b23594dcd28c68e73024b96f0d2a958f5cb99580d3ee4dac47b3543e2958,864bb483993b06c78c8cc720e8767cf3a3ca602f16788eefe903db358e739d1f,c00c209dea49e6183363cb6396c0cfb3317d282fafa04ac28ea131b767e0ea70,d851bcb4056f304eee9e467eab5405917c8663d7ff35269c356fb79a07bcc1ff,9a91ba67b3af2d996516e7e8c7d60bfa0f693074192b499e1c31616182a928e3
79,1789069500,1,ok,77219.66411152983,77219.66411152983,77065.06153368457,77120.65277481219,Down,Up,1,1,1,1,1,77143.25260059936,Down,Down,1,1,-99.01133671764,55.59124112762,a93c0491b5ed1093cab2cabe6f42b1424db690009796c1a68dd117b1b7a77667,9a91ba67b3af2d996516e7e8c7d60bfa0f693074192b499e1c31616182a928e3,549322290e05b9366d9467bdeb57ede52cd2082993ae634d23b40d57f6a88dfc,11a59a2fb48c8f0db4341d8bb0fe74d47a328e9751041240b6e597bca689ae1c,4c8dff4109e2996cd473eaa361dfd9cf9d5e8bd0c115afed4baf69b64d3b45e4
80,1789070400,1,ok,77120.65277481219,77120.65277481219,77239.08094220991,77281.644536002,Up,Up,1,1,1,1,1,77125.90446262145,Up,Up,1,1,160.99176118981,42.56359379209,da5a20a45f968584aff20fb5eea23d66afc6c9e68e0494490a4c34ec20e3e49f,4c8dff4109e2996cd473eaa361dfd9cf9d5e8bd0c115afed4baf69b64d3b45e4,4b8066ea0f7188857adc888197af5adadb915a39ddd39e98a67b6111583b95bf,e2acefc02910fec30a401fb0f982ef6be8d20d87411acc366dcc841f13be1025,428904b434489f3eb031c64f9014b645f1bf4ae4da2622dcd7f18996d0f0df2b
81,1789071300,1,ok,77281.644536002,77281.644536002,77264.89446546383,77249.2308037349,Down,Down,1,1,1,1,1,77296.67096814676,Up,Down,1,1,-32.4137322671,-15.66366172893,e4b41d1fdef5f63e8f7ae4f0a7e18566751dd2f62746ea5d2f67d0c7afc1e431,428904b434489f3eb031c64f9014b645f1bf4ae4da2622dcd7f18996d0f0df2b,3f9d92f70c2ec3274f17c7dc63433e9e59ac1d95c08fe2ac3372c2042176e9cb,0a1befcd3e51f97c4b309611c8485d328fca69ff7b8eb522d6f749edef5f1521,5350804f6d32e39ecb62776de418a8d2999e490daa51585813525819cdcd4f0e
82,1789072200,1,ok,77249.2308037349,77249.2308037349,77231.89535829474,77267.17113497785,Up,Up,1,1,1,1,1,77235.5232547342,Down,Down,1,1,17.94033124295,35.27577668311,1ce3b432ff6df5b562356c01447ec99358ffd136ffb4c76c0f9c6012b8887ed1,5350804f6d32e39ecb62776de418a8d2999e490daa51585813525819cdcd4f0e,390198557d0cc323889b863ffebf68f722f5d73ca29e5184a239e5b62b32b071,c58a43beb43d09a34b1144f133accaf32ab9e204a27743ddcb59b942eb4b2add,a7164c9013de65aed9d075b953822cfe6f1f5567b33b98ed11e5a9af281edb5b
83,1789073100,1,ok,77267.17113497785,77267.17113497785,77267.58702832366,77242.01590611578,Down,Down,1,1,1,1,1,77208.30240492785,Down,Up,1,1,-25.15522886207,-25.57112220788,cd0fd451ea80fa16798c6ca96a9e74aed488a4b781b745b5a018470086e2b4b4,a7164c9013de65aed9d075b953822cfe6f1f5567b33b98ed11e5a9af281edb5b,384a7f52d436535b1d4d2d42ec39a60924a881ff465a30ad3e8186c5e47d9e27,51ed87a8de65b1559c9150ded00ed85908ab62b700472f64c4b6fc2155f7eb73,df449f87311b400db43bc5ff6cee6fae12ec754c7967c7ae5dd587917615230c
84,1789074000,1,ok,77242.01590611578,77242.01590611578,77245.80576184405,77228.2098744608,Down,Down,1,1,1,1,1,77209.71880795891,Down,Up,1,1,-13.80603165498,-17.59588738325,6ec080df8204a9224a1c0ced89c64f12ae9b564bbf7b913ed11da30ee37cb039,df449f87311b400db43bc5ff6cee6fae12ec754c7967c7ae5dd587917615230c,baa1f8bfa94338f4a7ea8d57f5ca35f691111fb6fb6ff56a5360e92a367a5c74,b7908c0964d7464c81b47b979ceb5cc3266fc1d6d312cdc1e3f990ad8a056a67,b7727b260862b8756d7a4c24e2edd8b565bc50af028dc759bfc836e2db2b4cee
85,1789074900,1,ok,77228.2098744608,77228.2098744608,77187.22673051385,77203.97199997357,Down,Up,1,1,1,1,1,77176.76229004978,Down,Up,1,1,-24.23787448723,16.74526945972,3fda4c4072127ee29881130c470eeec369b59e4f861ba2297902404c010f04b9,b7727b260862b8756d7a4c24e2edd8b565bc50af028dc759bfc836e2db2b4cee,03aa714bfe8d0aaaa37d2aa677cc855e7b0077fa1040d8e0f13aa2902915ce7f,e23d4fd04b5b0847e4a7486fc586e5d46163feb90561e9e1ba1c105170b8a85b,c756e34e2e6f02a828bd20aba11402a0eef1c326b9d3ef9b2287621e06434767
86,1789075800,1,ok,77203.97199997357,77203.97199997357,77160.3499583386,77122.9463956854,Down,Down,1,1,1,1,1,77176.16972111538,Down,Down,1,1,-81.02560428817,-37.4035626532,e00bab2c33522ae80e0f96a6b90b0f45f7e8787b5f5a4afac9bd1ec4f9e8bba2,c756e34e2e6f02a828bd20aba11402a0eef1c326b9d3ef9b2287621e06434767,1507deeefb1ff5c538d4c92df32f3eb6311095693273167229c06e84c45fc707,de37f62eb47d1ef36d71b568f487c86f55a09f51057127e27292cfa90e4f97ec,7844e829f24dd59002985148cf000f84fe468808c9601316a23b428405265ff3
87,1789076700,1,ok,77122.9463956854,77122.9463956854,77121.62790963803,77108.00870159527,Down,Down,1,1,1,1,1,77148.45004369355,Up,Down,1,1,-14.93769409013,-13.61920804276,2f954bf42b581eb964c757ecdd65b1490442e933fc68e7e7e3b905c4ce1e7311,7844e829f24dd59002985148cf000f84fe468808c9601316a23b428405265ff3,3b969324eb4bec5833f7c01319d8990bc68cef439d5ca7b612efe76c540d481b,20baa9d867629f9693d759a8e539b5d201193ad0f29e5111946341c2c22bb69e,8cc994dd67e9ba0dc26002c8ddac8716cdc439184465fe67353448ceaa61d5b2
88,1789077600,1,ok,77108.00870159527,77108.00870159527,77146.52213524636,77083.4515021426,Down,Down,1,1,1,1,1,77120.17633286199,Up,Up,1,1,-24.55719945267,-63.07063310376,39a05663836b41dbd17ccde7759fb2281a27de3f3d7673f292b2af1709fd3a66,8cc994dd67e9ba0dc26002c8ddac8716cdc439184465fe67353448ceaa61d5b2,bd3453a21f5155cab737b2652784b207a55e052afed7d05725991c46fce1e609,f53a53a73308d858f26e74a92e8acc4442585d5ef3161df7bb8d136f0de6820c,c5a9b03fb0af6babddfa681162158b1c733a21db4bcc0fd899872d7e2f0e926e
89,1789078500,1,ok,77083.4515021426,77083.4515021426,77130.93872372346,77065.7269213144,Down,Down,1,1,1,1,1,77169.39967174933,Up,Down,1,1,-17.7245808282,-65.21180240906,e7f082e76f730ca4976ad857d564af28736fedab2da5b27fd4e259797ab6c329,c5a9b03fb0af6babddfa681162158b1c733a21db4bcc0fd899872d7e2f0e926e,790df48cae94c539a3104d2b845081ee517f480aa111360d88f9e1dbf93de813,8351928732e61530262bec7c5a9432a305494cf74f4f92a47ba933ea5e322e6e,fe12c3c89ae142ad68030b40a375e5a63142ce30de76bce3d3a2373677730fe5
90,1789079400,1,ok,77065.7269213144,77065.7269213144,76882.98424809909,76836.71778554893,Down,Down,1,1,1,1,1,76968.2997265427,Down,Down,1,1,-229.00913576547,-46.26646255016,59d1d94e824f24898fd0539b01c0077c08da146a8e3b88624a669694a183f321,fe12c3c89ae142ad68030b40a375e5a63142ce30de76bce3d3a2373677730fe5,491870eb5d36b3b2f02936f1f4a0d21cdb92c7cf6d9d7a773f1512f73491bb1e,da0d8460d4f6c295f2334c041a6039de7f847ae6299a670eeaea148819e9215b,9be2241141c79618fd97da89c2c4b8a31100a638301066a4bf6cd602fdecfb95
91,1789080300,1,ok,76836.71778554893,76836.71778554893,76886.61621469156,76806.56223748066,Down,Down,1,1,1,1,1,76940.4241870252,Up,Down,1,1,-30.15554806827,-80.05397721090,4583189aed8e5a2e15e0f492324a621ffa78fdd8a90ae04ae52dc8b403ca7db9,9be2241141c79618fd97da89c2c4b8a31100a638301066a4bf6cd602fdecfb95,3aa7c8eb20eded355b52da3f51283ba23162ef2a80a57dc44339151b3e31e2f7,2a90893513a838cd2f8c1d0d43be52b3153d82eff43a03b9a7cda80fe20cd5f4,14f155d453772ec51b1a9f9ec258fafd25d719f4ff4191e1ddcf14c57cfe66ca
92,1789081200,1,ok,76806.56223748066,76806.56223748066,76661.25351434687,76579.18052666048,Down,Down,1,1,1,1,1,76743.88402472515,Down,Down,1,1,-227.38171082018,-82.07298768639,fecfc6cadc61e143190e9da1e8b23bd4d748151995630576b600328049a79205,14f155d453772ec51b1a9f9ec258fafd25d719f4ff4191e1ddcf14c57cfe66ca,4702b97d04a31f5233c93bea7dcd4d2482d169787735770565d441c1ae7b4816,57a69efd7f6403d4cc323cf7a979569bb622c7b767a128cda55daa7bf2a7f0e6,4f29cb51b4ab42c7833da1d2b5ebb8249527f309161aabf3d652e494a13a4d54
93,1789082100,1,ok,76579.18052666048,76579.18052666048,76676.18776313079,76739.78768995538,Up,Up,1,1,1,1,1,76612.80474846912,Up,Up,1,1,160.60716329490,63.59992682459,7503deac948c24293d33d99b5b36a981089a5902415d14fed4bbaa3bda5ac2bf,4f29cb51b4ab42c7833da1d2b5ebb8249527f309161aabf3d652e494a13a4d54,63dc4241d75db55793788b5aa2d802be3fd597fedabce0477191ab4f0fa7bbf2,2af6c674171cc71187cb227757f2136a5bd1c39d6938146e18e2305636c903d3,808550362f41bdb5a312b3d465204c98d9f868d9d0314d3f1d43191b9dc1012f
94,1789083000,1,ok,76739.78768995538,76739.78768995538,76754.66442533223,76740.9024078542,Up,Down,1,1,1,1,1,76753.29326080254,Up,Up,1,1,1.11471789882,-13.76201747803,11718bfed647cdb7174b17a5f9cf6aff54b3f3457a34ec8ffa4d6095fca02020,808550362f41bdb5a312b3d465204c98d9f868d9d0314d3f1d43191b9dc1012f,5ad540a7a8898b29c1f4ec39d3c6f3b94677e6221855d7a92f82fcb1a716793e,7f6501cfd1ca6d5c05bb674b8df924f58d2fbbfb3234b1ad5eceabd04c86cbe6,f6a3fe8556614a8b696f7d4256a774a2cdca73fe54eb376a5c3be5b744a8eb7f
95,1789083900,1,ok,76740.9024078542,76740.9024078542,76659.77831269866,76537.48162049733,Down,Down,1,1,1,1,1,76693.28360615425,Down,Down,1,1,-203.42078735687,-122.29669220133,4d4891406a81d77b61cdf473a92d8b2da935a591bd811fb234bbd7856365df06,f6a3fe8556614a8b696f7d4256a774a2cdca73fe54eb376a5c3be5b744a8eb7f,b3e7b14b2b830ff52b921b4f6ddedb3ea03b79c6f27a0518d13b8ce534544eed,8d80d29781a57d1cd3693e722aa8beb0d82eae88f3208edbfb7746b658a90780,fe4a765a02688ce16e8887d485fd30004c2b9e28baed41972e624c96fb9658cb
96,1789084800,1,ok,76537.48162049733,76537.48162049733,76766.72674921736,76792.06493548807,Up,Up,1,1,1,1,1,76656.21816267558,Up,Up,1,1,254.58331499074,25.33818627071,a1df6709a8db773de0cd9204a9fd398a1ff061198cc1c204ac244f03f59f7be7,fe4a765a02688ce16e8887d485fd30004c2b9e28baed41972e624c96fb9658cb,d72413a695df8693439f9411e5e5013ec4971195e3de651dded8132bed848d59,10a9a2f5891b792519ca7b886c67d3056d7fe47a44f9af9cebbf8e75ca18b72a,8ad181945a31df12660cfb5d7d53e164768a42114ff158353d42d40779bbbc25
97,1789085700,1,ok,76792.06493548807,76792.06493548807,76829.66346793415,76810.26239451912,Up,Down,1,1,1,1,1,76771.29699755281,Down,Up,1,1,18.19745903105,-19.40107341503,ec0cdd962efe16ba8cce5c276938c13a6eb6a270ded5729cb7dbbba6cd882185,8ad181945a31df12660cfb5d7d53e164768a42114ff158353d42d40779bbbc25,9133f85ab36cab7f03504e79b344546784a8619799e226cc5d9f7c2c50c7547f,7146523275dd582de5a839b2d139407a9663b18b90820a78ebce23fa6d868100,24af272ede0e1668d2893d6d604ff9f0e39ffdb445871e4f904a01f7e8be5cb6
98,1789086600,1,ok,76810.26239451912,76810.26239451912,76781.278046818,76744.82853162594,Down,Down,1,1,1,1,1,76714.71163820622,Down,Up,1,1,-65.43386289318,-36.44951519206,7b9fc137baa7a33642af76e6bef83157863b224bd2766708eb5dd92f6d152f0a,24af272ede0e1668d2893d6d604ff9f0e39ffdb445871e4f904a01f7e8be5cb6,cde54eb6cdf75d2d99506b263fc95a73d41dd235570a6eaa0bee582c130c9322,e44aba7e03e7bcdb24028b5ff08d21566a0de3ef6cdedaacb404ab38db9354d4,3e25084720461e82b43dfe41f8fd47ae2c51fa90d3b5e016acb5375657fd4be4
99,1789087500,1,ok,76744.82853162594,76744.82853162594,76850.49949050305,76875.97806067424,Up,Up,1,1,1,1,1,76754.6849409483,Up,Up,1,1,131.14952904830,25.47857017119,4ae82f943a390287e0a16ce2803041a1f49a716a7125f9cea3e98eb4aca5d3bf,3e25084720461e82b43dfe41f8fd47ae2c51fa90d3b5e016acb5375657fd4be4,b2551a6c807dd4abe3efdfab31a810ae0a470d572f625b8f06ab34591a4dcfae,16eaa16108e0882eb7f8c45923e05d377c19432317a13fa8c91ca9292e6a4a67,711218364add1efa983911a1c7669a582e265c1c839bdb27976ef6815eeb715b
100,1789088400,1,ok,76875.97806067424,76875.97806067424,76934.31641034728,76900.25065337685,Up,Down,1,1,1,1,1,76962.22349411841,Up,Down,1,1,24.27259270261,-34.06575697043,f271256297e6e30b7d283ba5dcf5b913e7764c3cc566d54e21169e5847fd5691,711218364add1efa983911a1c7669a582e265c1c839bdb27976ef6815eeb715b,8818342fea1564f214636c6bfcfa702c86b474f53d89531a3bd02f2268c035b4,1b9545fa22095e635a89b8f7eaaaa6b3522be9ded5516bbc4b7f104c853b99e6,db5b8dee6b3cf88e66c3acc83f9da6d52767c199380fd088cf5609a24a1b4a6c
101,1789089300,1,ok,76900.25065337685,76900.25065337685,76835.06664307191,76794.35674935025,Down,Down,1,1,1,1,1,76863.20015205565,Down,Down,1,1,-105.89390402660,-40.70989372166,a6857643a7bca52ee79c4a16b41eeb072c66abaa51a691fbe1716439396698e1,db5b8dee6b3cf88e66c3acc83f9da6d52767c199380fd088cf5609a24a1b4a6c,8c2279a80b31c5562ede08fe1fbcfbdeb1de7315971f5048efd0a0f15a3dafc1,2b7f8544f6fda191d4a38f553a03c9223f7da86b53a6398c1add3ecc79a9630a,e301fc124079c17e4c0a85454b3926afc6a119f7bfdfecf8c9b4ddefc2201c0a
102,1789090200,1,ok,76794.35674935025,76794.35674935025,76742.30089602366,76819.50756571381,Up,Up,1,1,1,1,1,76672.19120212205,Down,Up,1,1,25.15081636356,77.20666969015,d3790cc1622d7f3bb5fb8b5517b20745f2f825de8b0e2e02887f2a496193c9e1,e301fc124079c17e4c0a85454b3926afc6a119f7bfdfecf8c9b4ddefc2201c0a,673106baf000ffa8e5c71562c5f9c4c2f1da0ffec48986e0e3fd75edc4ff96bf,4018ff9fd350cc7b5b5de541362719b73c033970dacc9aa3e9425cb3508a8bdf,c2627fe34e4cc10cb44b179abdd3314b075df3a72062a12ec696e49a15ea55b4
103,1789091100,1,ok,76819.50756571381,76819.50756571381,76911.48580332252,76938.68176942073,Up,Up,1,1,1,1,1,76866.92258912728,Up,Up,1,1,119.17420370692,27.19596609821,f0cfe3fbf042e4915ab124b2df0245e03945cbab9caa01d3c779d57a7482081c,c2627fe34e4cc10cb44b179abdd3314b075df3a72062a12ec696e49a15ea55b4,6e312ba292deceb7d6046ece8b1bfaf5640a4f8607860c41d62ec82f4122a234,16bf14ac766daaef78d1a0ae35df1aed7b216887bbb0b6038264fa120bf74fcb,6386b3af5b04f05eced1f6476ba08f34549aee9906ad007c763dc7a019938d1f
104,1789092000,1,ok,76938.68176942073,76938.68176942073,76904.7873532122,76957.66043950828,Up,Up,1,1,1,1,1,76921.98519114878,Down,Down,1,1,18.97867008755,52.87308629608,e8f5b0f3a8cadeee872b1741440adf3bbe39a40f216a8c4e66a64b68c201540b,6386b3af5b04f05eced1f6476ba08f34549aee9906ad007c763dc7a019938d1f,15a3c8df9d86c474db970257e531debdc5f35b494ca96c7b13e26df57ff37198,773edc112d7a37ef80ffcfe98d6a46b05eeac08d2db4e0a11f1abb213d504097,1850a2811c2b486fd66dec0e136eea3938975c3e611782dcfb3bb1d7ffdb7877
105,1789092900,1,ok,76957.66043950828,76957.66043950828,76827.45582682306,76784.56819378451,Down,Down,1,1,1,1,1,76851.55867380752,Down,Down,1,1,-173.09224572377,-42.88763303855,54cd5a745e2c54435718cb85da767278478fe910726dfd8ca36501deae7b2a18,1850a2811c2b486fd66dec0e136eea3938975c3e611782dcfb3bb1d7ffdb7877,0ce8b9f2a324e9747ad328eaee66caa97261cf829e2ead9e3e181babec353f63,15cb4ecbbdf4bd15296ea9230c44fb1fc0955b6f7030adefb7e1734d5a4c2b54,ce9e8539f8dfc2c9bc2def05a0ab748731fc5e4f10b89595da5092a5f26f9cba
106,1789093800,1,ok,76784.56819378451,76784.56819378451,76889.90550448294,76840.2227360472,Up,Down,1,1,1,1,1,76756.24539137096,Down,Up,1,1,55.65454226269,-49.68276843574,cd987b1b78349a7692108e1cfa28e98697fd001e93a2b750486ab65867d98220,ce9e8539f8dfc2c9bc2def05a0ab748731fc5e4f10b89595da5092a5f26f9cba,2795e9372bc4928a19a7d394a629f554c59161b81246dda7a4f3204bd9744357,19b69df5713547979b932d1799b05c3a0c7c497fdb0870872ad185e2acb6c902,aef0b492983c86b6281d4a2b8710910ec0128eb624a77e4328ae90f925f5f657
107,1789094700,1,ok,76840.2227360472,76840.2227360472,76812.26336510431,76813.55276408969,Down,Up,1,1,1,1,1,76894.1550787116,Up,Down,1,1,-26.66997195751,1.28939898538,841da9a3d45211e7d51e2997435b9e485f0a155ca03e327cc3adfab37e9a4100,aef0b492983c86b6281d4a2b8710910ec0128eb624a77e4328ae90f925f5f657,b7720668722de5cbe9e60a5b1fb6238470290beaa781efa7504efee6790bc8b6,7b47f7411fb901e180d35b4b92bb6f32bf2dbee8e43d101ce386c0f73f0b0f6e,40caa382e596e5f019ee78916d24ee5b7283572000b572374ffc43a9d05ec5f2
108,1789095600,1,ok,76813.55276408969,76813.55276408969,76687.77459642132,76844.81219806969,Up,Up,1,1,1,1,1,76790.25394292337,Down,Down,1,1,31.25943398000,157.03760164837,9e02aafbee35befd3f365b14732475fe0534c341d3c72316685ee5ffc6ef32f8,40caa382e596e5f019ee78916d24ee5b7283572000b572374ffc43a9d05ec5f2,ada837a045ad652b77c6971383b53f7922a72d98a319f1bc4d845d497c83f03b,a3321faccf6280dbbb089d50998aa1cd703096cc61a86bbc9f69fa7901461d72,cd99c6c112cd08254ae728a88dfe96f959bfd1856310ddcd0652c8f0092746b4
109,1789096500,1,ok,76844.81219806969,76844.81219806969,76747.7921287829,76787.92624932372,Down,Up,1,1,1,1,1,76813.95346159581,Down,Down,1,1,-56.88594874597,40.13412054082,fa4a3adc640d523dbf10487ddf5b8aef342947866bd2eb839f23cf31396b4899,cd99c6c112cd08254ae728a88dfe96f959bfd1856310ddcd0652c8f0092746b4,a8175fdedbd437372a7d1adedd2ef76e8ff783a88d425e3c011bb6ad59eb9c78,50eca6f60b236e7f7febaf35103e3a94a4fd8dd656ad5020998e38b858a07006,72a866b4ff08bded3e91bc9f032045030db8d832265f94f54d15586f0f46c859
110,1789097400,1,ok,76787.92624932372,76787.92624932372,76837.88041579274,76831.3914706257,Up,Down,1,1,1,1,1,76705.59839167591,Down,Up,1,1,43.46522130198,-6.48894516704,a56f8ea1c163fa5ce67245e9644ae50ae3c42619c9677f2fc27bb9320ade7c74,72a866b4ff08bded3e91bc9f032045030db8d832265f94f54d15586f0f46c859,f4930ae912a705d53f571041491bcbc746c5c1468775f05399e8c3f42d725821,be16eec9e5571339d1141e1d227602f65d4aec28c6aba2881ccba5edd1029e76,aa2fb592110979fcd2f81d765473458beb41e78478f5899326ebfc7156806265
111,1789098300,1,ok,76831.3914706257,76831.3914706257,76778.49282506802,76859.06298543424,Up,Up,1,1,1,1,1,76774.3667871725,Down,Up,1,1,27.67151480854,80.57016036622,c3bb19e656ea1a1c0dbb2462d5499a56b32ef45a1b9efd1ccab34c277d50e2c0,aa2fb592110979fcd2f81d765473458beb41e78478f5899326ebfc7156806265,2f3fc226cea108daaf402f20c727014219e1960a420f359f62f67c7ad9814c67,dd7482d9599fa782298c61a82ed608d52406b25a3fbf3097751c5daa90ea0012,02ce1068a693e29618d5cfdc6d6a02633c176b4b2b5229e26cbc97975b777daf
112,1789099200,1,ok,76859.06298543424,76859.06298543424,76932.33135073294,76945.89563764159,Up,Up,1,1,1,1,1,76911.87274836579,Up,Up,1,1,86.83265220735,13.56428690865,86b301a40679e94e85a6ec9ac45acc31fc7be64506b3bbdba3ef8845b9f39435,02ce1068a693e29618d5cfdc6d6a02633c176b4b2b5229e26cbc97975b777daf,077b307b42bc3ce863a571b86ed15006edb84151ff2185f45c7c5b2d3d65b2c9,ffbb6fdf5b305d43b3a7917e0ee4878bc83493d5a35c9c2cc2ca4888c58b90dd,448eb7db989a4e2b7290e1dc97aca117ce4a2b5a49a92b6307706431bed56d32
113,1789100100,1,ok,76945.89563764159,76945.89563764159,77013.27300147671,77138.81433163738,Up,Up,1,1,1,1,1,76940.92058071692,Down,Up,1,1,192.91869399579,125.54133016067,3c2fbae954140853f772e945410188f472ca438e69d80bafb94940c8d8a7a368,448eb7db989a4e2b7290e1dc97aca117ce4a2b5a49a92b6307706431bed56d32,e75a9c8904abb6f4fb922d962d5e9cb48f0d2c3bcb181e1754f67870f3d3c8e7,1a1f9a1ff8294830a4a87312d32d14a6cad12520139cf86bfe73ffee9407a69e,c37f1b2afe8075696dc235e17dde676fc00e771849ad4728107084bca2bc0a92
114,1789101000,1,ok,77138.81433163738,77138.81433163738,77081.06550113883,77068.72012982526,Down,Down,1,1,1,1,1,77121.97873453319,Down,Down,1,1,-70.09420181212,-12.34537131357,58738b6f9624436e7dd656a3f53b81dc9ddf4170b9ad4475f6bb3595d91f490c,c37f1b2afe8075696dc235e17dde676fc00e771849ad4728107084bca2bc0a92,49b31ce2fc241620b7724dd2ebd37ca87cd881f1c6ab962848df10e7184c701f,ae9667cb8c254acf803624a9ebef0f6d14e026f1d6e17bf2f0d6fd2f61a2be38,3f32414f76adf57bb0ca07762d8765f2c87a9a0c95a65bff05d0df9287421e99
115,1789101900,1,ok,77068.72012982526,77068.72012982526,77102.43101348491,77096.47559169827,Up,Down,1,1,1,1,1,77078.3301728705,Up,Up,1,1,27.75546187301,-5.95542178664,36600d04fd0584a16c9fe5cf3e3c291924231a6964b33618fea1520a1cd7c0c0,3f32414f76adf57bb0ca07762d8765f2c87a9a0c95a65bff05d0df9287421e99,659acc175f53a27f90eb6e22e3f992170b0fe5c9169a283cb4d610fbf18bec53,23cee1f3c354a45492af9174741cf0050598eb487c494c50fc52e9cc5f978ae3,660db424a3309298b8febe649318c6c0cb4a2dbee8ffc839018bd900b4cbacc1
116,1789102800,1,ok,77096.47559169827,77096.47559169827,77048.73184120616,77095.3668885003,Down,Up,1,1,1,1,1,77048.52497623872,Down,Up,1,1,-1.10870319797,46.63504729414,556b4bce8ad497a8bdc9ce857525253673d2a7f65ce39145ee7a767139ce66b7,660db424a3309298b8febe649318c6c0cb4a2dbee8ffc839018bd900b4cbacc1,d9a953afc0f20e4eac72311aecebd1cae195f0287ca0d4ec6fb8f34554f3b238,8173b0a0dce4ea18e1d65839227725612d4b1e495eb7a29fd1ff642a6c3a3346,bdff1cc890eb7ec4f24d02c05aeea45908c1ab0359b49a3ba3a2fd3a2a58bb4c
117,1789103700,1,ok,77095.3668885003,77095.3668885003,77087.33166663778,77077.54661435763,Down,Down,1,1,1,1,1,77105.99588101369,Up,Down,1,1,-17.82027414267,-9.78505228015,e7924db954bdf560a2f229fae593acc1a06f9318f8d446e6f8435824efd81204,bdff1cc890eb7ec4f24d02c05aeea45908c1ab0359b49a3ba3a2fd3a2a58bb4c,564a33e880f6056cb2856be839f8af57a93bb7c5faf4c0442740c342008a62df,7cc393dff7d390fe4e55c4d81fcd5cc2ab4884b597165791558d15df93c8806c,37fa75852fb669fce1c1a9071ab1d81e4f4e8ca4d4fbee5d9316bd63193729e4
118,1789104600,1,ok,77077.54661435763,77077.54661435763,77135.73423435897,77153.79361331083,Up,Up,1,1,1,1,1,77075.11836858395,Down,Up,1,1,76.24699895320,18.05937895186,20cbeb8dd47100bd06a10006eb696e3c1989d1f65cc48a396cc4e095a137d91b,37fa75852fb669fce1c1a9071ab1d81e4f4e8ca4d4fbee5d9316bd63193729e4,7bee38eb3f782f2ed84de1bc834e2b48c1d78a287b125edb081532c53c06f216,e5ca8c47a225e498312ed666e40684d15cf4f0dd010ad0c342b99983d8864278,b17763ed1cfbd67136e629cf14d31650701322871903ffc9d47408be5091b222
119,1789105500,1,ok,77153.79361331083,77153.79361331083,77167.3000945013,77220.06824375165,Up,Up,1,1,1,1,1,77158.21469345674,Up,Up,1,1,66.27463044082,52.76814925035,1203bfdecabd9acef8f07ab874f22f53f255b2638fce86af1dcad4d60100873c,b17763ed1cfbd67136e629cf14d31650701322871903ffc9d47408be5091b222,0129da3bbd6654012f40336dd5a5faa943b923aafa5556ff25e5f5fc7d5ade19,616450db1e7f15dcf1a8dccee22b54d1028c8770744b081f00df72000d052d9a,1a4b86f6bd81233b7c3a4d8ec166527d06c110753d541599a78115fda66129a7
120,1789106400,1,ok,77220.06824375165,77220.06824375165,77249.27427234006,77371.14684944315,Up,Up,1,1,1,1,1,77224.46576944103,Up,Up,1,1,151.07860569150,121.87257710309,f4e4197bab8166bdd7f712d18039400143afe4b772958f3df898075d5d21d5ff,1a4b86f6bd81233b7c3a4d8ec166527d06c110753d541599a78115fda66129a7,982680e176f33d0194954a4e9e7a13712fa7cac84bdb7b28de0f2acf4e9bded8,6ac345ef287a7f684587195a22ace2a3b33abf8c91299b1b6dfd9afe7c970b3c,f44369edcec7cccca1d0ab245ae01f5dda280c0b7bd228daf8ff6a2a54f859a6
121,1789107300,1,ok,77371.14684944315,77371.14684944315,77238.97178354167,77245.85878658015,Down,Up,1,1,1,1,1,77290.22264147658,Down,Down,1,1,-125.28806286300,6.88700303848,f1cdf7a6a6d9356a3a5f10e00b7a710e6792e18dec30234e401c30ed82f4844e,f44369edcec7cccca1d0ab245ae01f5dda280c0b7bd228daf8ff6a2a54f859a6,253b7c20aa1dc4fe344ec9b6bcfcb7e3349599f463da236fd5aa9772b307e329,dc4dd936c07bb74bdf9cc4f9f6c7a7e9e2bebb354e8b3ae488001bd3b2871b08,2f7840416d136dc614dbdae24a3b4ec9ef09cb1dbc171ce975e52bc88d17390d
122,1789108200,1,ok,77245.85878658015,77245.85878658015,77221.77300432272,77193.57630037234,Down,Down,1,1,1,1,1,77155.8747952931,Down,Up,1,1,-52.28248620781,-28.19670395038,45ceb334e89aa5f499f84394f26d0612d107bc802147dbc8ce30954a9eea3626,2f7840416d136dc614dbdae24a3b4ec9ef09cb1dbc171ce975e52bc88d17390d,bdff39d26d0232a43d8b95d0ee6cabb6495a6ee85ac8f76df4295bbdadb82ece,8a74cca6b2712aaa66f441211d86960e5408fd88d4b9bb491f7dd2ac33f44438,10106f5d172d4e3ddc931d048227f11980c1820d52110619cc2e2429d748fa10
123,1789109100,1,ok,77193.57630037234,77193.57630037234,77246.81157832776,77261.39664920933,Up,Up,1,1,1,1,1,77238.33233458511,Up,Up,1,1,67.82034883699,14.58507088157,9da531ea9d9c944ddf36132996523a453da94083b86c966365c1dd57a966e5f0,10106f5d172d4e3ddc931d048227f11980c1820d52110619cc2e2429d748fa10,ed2d3dd4f8b7e71aa713c20470cd0ce0a8c4cc25e577a381809707b122c77c37,4fc3e9fc37a979664dce38affc602661034c1aa55f75e990ec1f6cfbb645e21c,d4131d6a32730fecbe4b0ba289f67f813835eb8b9216377bfb6cbb3939f9840b
124,1789110000,1,ok,77261.39664920933,77261.39664920933,77327.8757232541,77285.5307586083,Up,Down,1,1,1,1,1,77270.08206771173,Up,Up,1,1,24.13410939897,-42.3449646458,8d4bb6a81d787e9ffeede69d9ad84d8d96278867b25b46db9fe86d0caae3b11c,d4131d6a32730fecbe4b0ba289f67f813835eb8b9216377bfb6cbb3939f9840b,2cf6859e9c26b32ae849c45bbcabdbc9cadcdacd2afce1bdca7e82fb69154c46,67c674d4c28a86e799e6c3de1d1471b630791905d84b13d56e16c406c4dd0d3e,8b198ff46eff41dfa27933eac55e4ebde9c6c1105b07e8a4a0ec0767d71d9df3
125,1789110900,1,ok,77285.5307586083,77285.5307586083,77347.43933101652,77303.15767523917,Up,Down,1,1,1,1,1,77321.2161376296,Up,Up,1,1,17.62691663087,-44.28165577735,30efc982e425cc45165a3afa90d4e868b689ad60dfd637a236db48abaa731cea,8b198ff46eff41dfa27933eac55e4ebde9c6c1105b07e8a4a0ec0767d71d9df3,0a61c2a7ed6af7d66aacb486fc530e9d89b9ab0e65eaf5470394754a86b401f2,b296d5d14f4dc0881f3a4a869ea607c6fd6ea5c4d86bc2794f785d107525b54a,0ddb3ce0e61f2a9761cc817d9878b0c23b0bb5087044ab26b12827492f28c348
126,1789111800,1,ok,77303.15767523917,77303.15767523917,77240.8047694363,77238.62182630054,Down,Down,1,1,1,1,1,77278.67772939471,Down,Down,1,1,-64.53584893863,-2.18294313576,6ee74d98f7d381a8e2b98b0672192337abf4391d68bdbad61c2b774536f33a91,0ddb3ce0e61f2a9761cc817d9878b0c23b0bb5087044ab26b12827492f28c348,fe4cf881dc47bfeb8d14ecae06ae54a713dcf419fe43e6f7a5e7d26d9e04d6ad,1329d456bd8fe652c133c3b9a44662709c6e387af4ffcd3895cf611eeaf316e0,7ddaa5be9c61aa08b55b5f9e373798f89751c0235dac9257a71702da313c5d09
127,1789112700,1,ok,77238.62182630054,77238.62182630054,77182.04548476875,77197.93561349165,Down,Up,1,1,1,1,1,77213.21738515972,Down,Down,1,1,-40.68621280889,15.89012872290,a7f24f83aa72abe19b1ec7553e9e091ad18262a176cbdbe4577619e3d7dce29a,7ddaa5be9c61aa08b55b5f9e373798f89751c0235dac9257a71702da313c5d09,d8f82d7c3abdd5b6bcf59ea1fe8f0722ff6d6b9d231e21380d9c03d2bab9e6d8,81d166125381a3e6b2491833dabc28af692dd84bf17ecd3c17ececd6af448d72,d2ce24c9dad41e4a170376e00800be7f040b604c02f2ac50fa0fc1e8fd57e33d
128,1789113600,1,ok,77197.93561349165,77197.93561349165,77127.77598643015,77149.32455845892,Down,Up,1,1,1,1,1,77161.85075189042,Down,Down,1,1,-48.61105503273,21.54857202877,1aa138607b7c50802e53ef1cb88ed432fdcf9395c64e58209f0e20aa49c14495,d2ce24c9dad41e4a170376e00800be7f040b604c02f2ac50fa0fc1e8fd57e33d,471891acc1c66fae01d7d1279c1d80515c633c4450f7088dc022adc4f97a7e1b,0a700de4c576218611e5668c70d06a6553a90f81754d404465d2e6cb7e02d2a9,99dc8cbcc03331f9bb302b1c6f40a47b1c92655ae4b0bafcacfd63a8748e3920
129,1789114500,1,ok,77149.32455845892,77149.32455845892,77337.344970846,77337.55460067111,Up,Up,1,1,1,1,1,77206.81213231532,Up,Up,1,1,188.23004221219,0.20962982511,ce31ea521eff0e0ac58b0e1d68c4c7cf65bdf35c3b71d6a8cdcad775b7301bfe,99dc8cbcc03331f9bb302b1c6f40a47b1c92655ae4b0bafcacfd63a8748e3920,eceeb1ddf4bab8d04a1243abf83661211029fefc3dab2b47e22c265f8aff0902,acd890a3acdd712119e4492500f817485443e58f7ac20d87abf689ed3e5aac01,7c9c7a994c9129d13a9248a69e2dcdf66a8d25fe223f7b2fceb066f34f3571ae
130,1789115400,1,ok,77337.55460067111,77337.55460067111,77371.30218600675,77386.54628733752,Up,Up,1,1,1,1,1,77373.54777089928,Up,Down,1,1,48.99168666641,15.24410133077,3c0c8d8eea671d09a97d7b0dfe0cce7ba656cee67e7a524167e05d5a37736550,7c9c7a994c9129d13a9248a69e2dcdf66a8d25fe223f7b2fceb066f34f3571ae,e543078d3d8953aa45f2df20b1272e60eba2c5b07d6fb2609e826dfcc107573d,40f39e676a1db79ea91e3449b005eff6a3c2f69f4035e4171012b01b10c17c0f,68e3d89edfd982918efcb26cd363999ae9783edd4d07c983089fdf79f6238256
131,1789116300,1,ok,77386.54628733752,77386.54628733752,77329.51631407894,77330.59270826796,Down,Up,1,1,1,1,1,77352.58175418033,Down,Down,1,1,-55.95357906956,1.07639418902,5ef853f15592e62c10d56195aff8609c1ca728051f5492e40e6930666671b7fe,68e3d89edfd982918efcb26cd363999ae9783edd4d07c983089fdf79f6238256,d961af14831b7b032f902f2c3bb435f2479e9501b13f2acbc2298af3aaba7500,5eb90044c3af6f99b6c722eaf4f61e98815df5646809a36468919d1b3fe3854f,a02b3caa98f6bd2a7614400dfc46f9a3adae5eada34de5f12148f2a44aba8619
132,1789117200,1,ok,77330.59270826796,77330.59270826796,77258.6408110188,77255.77367268519,Down,Down,1,1,1,1,1,77303.84849345178,Down,Down,1,1,-74.81903558277,-2.86713833361,df045db15c48ed27dd1c96eb57799e2be6706d15c430df540900591afbcaa1bb,a02b3caa98f6bd2a7614400dfc46f9a3adae5eada34de5f12148f2a44aba8619,c34fdd1bc5478fcc0fadfd1f9ceec3b9eeaee18f3d5a8d65fa1eed4080be2f41,67cc033e5b069ecc2fbd9edd74715b230f6a42e6c0d714879b6a6b5ba7fd77d4,5e1648459f5c9d6fd1b126f70ccf72dbdb64f5f9c9b2d28e60e2c2bb12cd3a6f
133,1789118100,1,ok,77255.77367268519,77255.77367268519,77194.61877388648,77124.33354133394,Down,Down,1,1,1,1,1,77256.74950946531,Up,Down,1,1,-131.44013135125,-70.28523255254,db32fef5d1b75c9a1ab578ff379ba1713d4bfc60d8c4a175eb2e63b2f4eca326,5e1648459f5c9d6fd1b126f70ccf72dbdb64f5f9c9b2d28e60e2c2bb12cd3a6f,a5fc90539c033cb7a12b02279c1d1c077b0179845477df520734ed4d422e5ecf,eecc69122e53a7186b2082e952be382866a93a957570d5d5548c39ee91a68c81,6e816b5579a9a598b9135de46eee79cbdd5ff4e85e65dd131a85f6546ed40689
134,1789119000,1,ok,77124.33354133394,77124.33354133394,76932.7933262054,76932.33094470674,Down,Down,1,1,1,1,1,77079.7989500859,Down,Down,1,1,-192.00259662720,-0.46238149866,5bd58267d8b2d3982d6f3ca11942532789de889f6a274ad301ec206a53ceb4c0,6e816b5579a9a598b9135de46eee79cbdd5ff4e85e65dd131a85f6546ed40689,c4dd66ac003f21b36359c942116f108a3e0bd7a1391334adc0a5baffea04a21a,7680ec474f02d093e00a0665ce3d1fe29fad76b079cd1bdb9dce09948798d7d9,cc0c7e1970751d2f089154acae2d11d040643f35407fb5f026de875e7c89b0eb
135,1789119900,1,ok,76932.33094470674,76932.33094470674,77006.48654186317,77027.8115921245,Up,Up,1,1,1,1,1,76993.26117522382,Up,Up,1,1,95.48064741776,21.32505026133,705d1351a3dcf99fad3f25b2685feb2cdcde06319c3355061e1ef7dbe79380b4,cc0c7e1970751d2f089154acae2d11d040643f35407fb5f026de875e7c89b0eb,2bc0f29f22bc609bef40c934e31a020db427eab901a2e2de4634cf0ea01f56ad,0684d698e6fa07666b4ea2fa5abcfb987debd95341567b16c21e59af2cd5fb0a,5e9fbe6de5e416c83911858f7bf6772e0e7abcb67fade5cffd36e1cdea32389c
136,1789120800,1,ok,77027.8115921245,77027.8115921245,77087.30617719825,77033.79898332743,Up,Down,1,1,1,1,1,77103.9496977532,Up,Down,1,1,5.98739120293,-53.50719387082,5820f8802d84d371125bbcf2b83ed3444032782f01ecf2f3810a7a781f13b972,5e9fbe6de5e416c83911858f7bf6772e0e7abcb67fade5cffd36e1cdea32389c,fba5adae83b06b41abe2765145098c9146bcb30c4cb8735c1ddf93356489b859,2708da6fe12065c35d549747b2ca878bd4ee0f279b1c31c5ea85cd066cdb2c10,25bf935076de9ed30f2b01b3e80657ef6cc42cc1d649b9de351fe05d5d1ce45e
137,1789121700,1,ok,77033.79898332743,77033.79898332743,77067.0292664823,77011.45709542152,Down,Down,1,1,1,1,1,77101.94839518631,Up,Down,1,1,-22.34188790591,-55.57217106078,4ea5d42ffac21121778ca8e18c09a314bff1f830839b016ce739f613fc986cb3,25bf935076de9ed30f2b01b3e80657ef6cc42cc1d649b9de351fe05d5d1ce45e,164b194611751e3283cc342188194fc7f3d201460a96ad6486dfc8201c45b3b3,b8077b6381fc04be135cc4318ca4a5beb353d3aab0ade34d835e3fd96fd22778,36e51303f3d9fdd1d19f29ac66247894ee102e0082289ac75b489298e643db76
138,1789122600,1,ok,77011.45709542152,77011.45709542152,77011.38450452562,76978.22831820427,Down,Down,1,1,1,1,1,77002.36456633473,Down,Up,1,1,-33.22877721725,-33.15618632135,ec2c8d53bc084d6eb092f2213524883e25a295f7e8e697609df7a59012baad11,36e51303f3d9fdd1d19f29ac66247894ee102e0082289ac75b489298e643db76,91cd66f3b4e260fb482e51c249c8f4e0ec95071cdb125569edab0f8767d3c298,d393ecbbd23f4c18a0ff79bdb86856524f9bb900ac4cfe5924170a5b5ff42bf4,389d2ed6ee8dc20ccd5a5d0d04b1c183ed0b8e82f086e6251fdbd4bca4d416ed
139,1789123500,1,ok,76978.22831820427,76978.22831820427,76996.80076778619,76975.151061219,Down,Down,1,1,1,1,1,76979.77457762705,Up,Up,1,1,-3.07725698527,-21.64970656719,df1be820b9a8b12cd6a71aef908cb7868a4cf90f34ba1a720147b76cb1d30209,389d2ed6ee8dc20ccd5a5d0d04b1c183ed0b8e82f086e6251fdbd4bca4d416ed,7ab6f51444f1cee4b1ce40f08655f46928fa209ab3283f521e96af10c89c9803,35c52e0f2814f755d668c3264576b6231cb594572ec3e0901ea02bd59592ba39,a33fed69006e65adc7ccfd4ea31c36b59cbe263961e4e839d9e1c0f6ba6d4e0a
140,1789124400,1,ok,76975.151061219,76975.151061219,76766.42508416837,76787.04046960291,Down,Up,1,1,1,1,1,76864.29808894845,Down,Down,1,1,-188.11059161609,20.61538543454,7a0266159bf1e2d4fd0a1c36b9f4501c490a161e867f4ea8bdf45aaab9289ec6,a33fed69006e65adc7ccfd4ea31c36b59cbe263961e4e839d9e1c0f6ba6d4e0a,e1603a1172b5719b168d27b4816217238e5ddef65ce9fd1fb72da86d44e6f651,a4aebab644cc1f2650427b4e36530fcb216f7e84839c3f55a2f9896580a5b75f,3f294e74dd99f52b39dfd9fb97ce99d0c5087577a8eae630f71f70bba3caf57f
141,1789125300,1,ok,76787.04046960291,76787.04046960291,76793.09630765325,76816.51718664618,Up,Up,1,1,1,1,1,76774.99161592299,Down,Up,1,1,29.47671704327,23.42087899293,08887c6e1510e08fbfd0f1ba7064d45935637a66d75daae5e336ac567ae32140,3f294e74dd99f52b39dfd9fb97ce99d0c5087577a8eae630f71f70bba3caf57f,425be4af93fcf3d6edf93ca436c964c663c5482d991e6d819e8a527df1fb5bf7,33619501eb29cd2c212bd6c35aae053fadc8d51addb4796d1ce9b5edad50f589,1c34444f80a12769afb073939a9a1d93d6535841af5cc51b78d003fbe13b411c
142,1789126200,1,ok,76816.51718664618,76816.51718664618,76814.93429835774,76863.45787980147,Up,Up,1,1,1,1,1,76801.50992546981,Down,Up,1,1,46.94069315529,48.52358144373,5c481a3a77a47aab52c040cf869c688e69133fe423d5e93491d05cfe8215c5f1,1c34444f80a12769afb073939a9a1d93d6535841af5cc51b78d003fbe13b411c,9621f19d9badcb22933b28a53a30c30f6bc2c55b8b387ec5b69792ff1b9fd769,9df61916e39e8ea8cf918d8367e934daad53ba4d0f7a4e07eccc3b33a8534da0,7d4d1c6f229b200f68e6012772d5f0b0ff8db159c83b3de32236cb088fbc71eb
143,1789127100,1,ok,76863.45787980147,76863.45787980147,76956.2637048126,76994.84244708234,Up,Up,1,1,1,1,1,76914.47266004447,Up,Up,1,1,131.38456728087,38.57874226974,b6aee4d1d1cac2715f9bade95e3baf68e641547369f2104e1cd94e49708f8c62,7d4d1c6f229b200f68e6012772d5f0b0ff8db159c83b3de32236cb088fbc71eb,a1829aeffb2054dec02e1bcc3e8c2007332fcefdd1039f216b365dde606e32cc,0bc12f37f513efd0ec4f6cdb4888e0a1876cbf54b32522f522ec2cc175c26716,c71cc5d078e2a6e2ce7c69a4ee905006e9908915798194e0622bc0cc37b8126c
144,1789128000,1,ok,76994.84244708234,76994.84244708234,76893.39914931795,76893.4702811815,Down,Up,1,1,1,1,1,77033.43597852172,Up,Down,1,1,-101.37216590084,0.07113186355,c9f5c549e54c68d44ddd260cfe9130870a7a778c86fd20bdfe73780fa6d491d3,c71cc5d078e2a6e2ce7c69a4ee905006e9908915798194e0622bc0cc37b8126c,c3de27118723f1f62c4f49425ba33d71957f19e057d5ee1019e13d2bccce2174,8b6fa9e1d29d2dd81c117c39f80cef2af89feddad853676fee98710470ded53f,b01c22785ca16108ae204d11657e9369d6f4d2323e0c86dba9a940b0d6cac0fd
145,1789128900,1,ok,76893.4702811815,76893.4702811815,76950.1816946568,77062.89479932586,Up,Up,1,1,1,1,1,76989.00278449968,Up,Down,1,1,169.42451814436,112.71310466906,7ee64d465c9e65047d77b863120192a0467917bead71b992b6f95a0640620ba3,b01c22785ca16108ae204d11657e9369d6f4d2323e0c86dba9a940b0d6cac0fd,25007d86c316d7440363060df892b5f08f6b12dacd1e4002a0cd0990c518be6c,50c422084ad622b440354b740d0975f20b8911abc3af888c40cb9e83b8da29a5,c6a277e35736b50725d04091fd4429e4d7f95cd881e3fa5f528eab32c79ae966
146,1789129800,1,ok,77062.89479932586,77062.89479932586,77447.02788416749,77556.59692967658,Up,Up,1,1,1,1,1,77116.76536301666,Up,Up,1,1,493.70213035072,109.56904550909,38c0d7bad503617551ed188dfbe7fd45f014e65d5adfd8488bb4d5b55e35f82c,c6a277e35736b50725d04091fd4429e4d7f95cd881e3fa5f528eab32c79ae966,3a41a273b4e198b5489797baccbb53b9ca5775b45ff5cef2e280bd9bea5dbc9c,e9dfd4bc377fa29c30bceccaed2cc0195dbd35c9c749c642a4136715af8249bf,4a02db10e2353975a259c65bbe28b895a1825a8057915dc02d94e26f8c9551f9
147,1789130700,1,ok,77556.59692967658,77556.59692967658,77991.01223299143,77944.49352162132,Up,Down,1,1,1,1,1,77846.28189123243,Up,Up,1,1,387.89659194474,-46.51871137011,65186b705f493527aa4cead4985d52d8cfc00084e71e944f89d2857d0eb656c4,4a02db10e2353975a259c65bbe28b895a1825a8057915dc02d94e26f8c9551f9,fe5451d878dcd2b12d89ee5e6cfb7d5c433aa90a03cf3e179fd0ae28d352c525,c92f0dfdc1d983260f69284ec9c0100be663bbe3c52f28d394889438998db72e,8bd27a064eb3ea5d11e8903846367c879806a80ab4645fe348e98b0840065f36
148,1789131600,1,ok,77944.49352162132,77944.49352162132,77571.23779500848,77669.65932641042,Down,Up,1,1,1,1,1,77769.99875511043,Down,Down,1,1,-274.83419521090,98.42153140194,5c887b9db5546a98eccd39327d41fb04fb544757d3176cc7b71a97fd0df79bfb,8bd27a064eb3ea5d11e8903846367c879806a80ab4645fe348e98b0840065f36,814ab57e1ba0f90d4c0cfdda69bacd581df17a70c7f721a1e26c1587c41a154f,2e91f354dbabf604cbe8bbd2f2cb21e57b078019b2e22554d2fc7f1f0d691617,28394f4aeb94fa3175a3f0121d47e8870b67cf54a5aa139fcde2b9fb18e5d3c8
149,1789132500,1,ok,77669.65932641042,77669.65932641042,77712.31943413641,77520.20493505456,Down,Down,1,1,1,1,1,77677.28126530854,Up,Up,1,1,-149.45439135586,-192.11449908185,39d3bee8e263a7b38ad7217bf6208344c3314773ba0eb4439c5aaeb5cf4a2009,28394f4aeb94fa3175a3f0121d47e8870b67cf54a5aa139fcde2b9fb18e5d3c8,51c02617f7c2a1a39efc6f7bacf7356c8ff05a64101040ccbfd920dcc18cb884,8330a8d02121163def990b696090d7d08c9ed3bcb2c1236b025d940caa16d946,e6f85968ad966032fab000c77aa9c997af480cc087d62c863495b9345e68391f
150,1789133400,1,ok,77520.20493505456,77520.20493505456,77529.30631635452,77739.91663883052,Up,Up,1,1,1,1,1,77437.56466657677,Down,Up,1,1,219.71170377596,210.61032247600,8076464e909f3a654a6aa87d22f1d1769cf0290b43d644d2542b17a1b52edac5,e6f85968ad966032fab000c77aa9c997af480cc087d62c863495b9345e68391f,5cbcb252ee4c54cf0818648369109309a6d50fad38c0d8dc80783379f598f444,dbd22553ba4ac595bebda2b836ae1df30c2c5b46d9e3a45a7910fb0651a56d5a,f82df147c81170cae86a21eca758d496650c60185341cd8af58c9cca1ddc202f
151,1789134300,1,ok,77739.91663883052,77739.91663883052,78675.60121606916,79138.23054465246,Up,Up,1,1,1,1,1,78301.60722107367,Up,Up,1,1,1398.31390582194,462.62932858330,8088c1df8e9521f41fa28bffe12d371c35fe6495d7b434ab3b03c32c4df8ec5e,f82df147c81170cae86a21eca758d496650c60185341cd8af58c9cca1ddc202f,8bace10bc8ee009e2fd00225d708f34ae9d3540859c452d6d6aa4a8d67eeaa8c,b77a8261f5c5012e616267f72bb248d960fd3a49f7eff9af29d5cec5c45bbed2,2b858b36bd0c3e5ca1361206b587b4ebb58a44ee6b5f4ed4a5c2b3be78903c14
152,1789135200,1,ok,79138.23054465246,79138.23054465246,78970.60438339121,79102.36578775708,Down,Up,1,1,1,1,1,79448.29113321178,Up,Down,1,1,-35.86475689538,131.76140436587,f399a360cd2ee62fa8f23e389f024f046b8ee12192785ec70c7d472f3fd2557c,2b858b36bd0c3e5ca1361206b587b4ebb58a44ee6b5f4ed4a5c2b3be78903c14,26f5974aa063390931c5e6fdd73829ee4386a957d81820114da9c02b1c96ef6d,ba158534d73ee84d3ac66ddb366dc6c6d8b00de1d2b37975a4ac30ee84114156,b4e765838e3bfae0a0a1e54bfdae9182b32b1ea4c99a51349aac49c118b32dcf
153,1789136100,1,ok,79102.36578775708,79102.36578775708,79027.03025851019,79020.08247720185,Down,Down,1,1,1,1,1,79121.08547840222,Up,Down,1,1,-82.28331055523,-6.94778130834,4b9b74e25f20ba54074b34b1c930fef7df846b3f0657053ccb9a8ad946224b59,b4e765838e3bfae0a0a1e54bfdae9182b32b1ea4c99a51349aac49c118b32dcf,49205f924eab71a7b9fbe1fe951225bac62e8db8f56204908da7778c31ed2009,025f7dbb25c70a8e5bc1c4acbf3ea4d18c8bc013774691d52958519ec18dce50,c261de350999eea38230927012eff67af66e65c2608aee7094f3d0e00485aeea
154,1789137000,1,ok,79020.08247720185,79020.08247720185,78683.83735733459,78583.15757735418,Down,Down,1,1,1,1,1,78771.76489547871,Down,Down,1,1,-436.92489984767,-100.67977998041,43dfe4425070644bc3e8376e87f7005718fec8bc48c786a12085ffe97ef35e22,c261de350999eea38230927012eff67af66e65c2608aee7094f3d0e00485aeea,7d072d5a53aa3a2ce1b8fc9f16da76268e91f9ee0a253915b50893df376b4626,96bbc00c47d65398994955b977d1a5ee48646e401ecd9e8279e6d90de4691929,754b373fc1496f17284ece0302a357446c5c5d62368933266503dbdba61b0c41
155,1789137900,1,ok,78583.15757735418,78583.15757735418,78825.41483336494,78763.41369144642,Up,Down,1,1,1,1,1,78603.35541588272,Up,Up,1,1,180.25611409224,-62.00114191852,e469f3c5a84cfadfdc7efee5c5cca7d88300518c2c7d93f6b136140cd17ef35c,754b373fc1496f17284ece0302a357446c5c5d62368933266503dbdba61b0c41,5a95d9a90c6b47abc4b0c2b096f19083c8ad95e802acf6e3ae6365b9509f8fcc,c7ac640ea0dd95bcbdbcc32a08d17585b9acb69bfd10f660916859993f8c581c,13b1d17a49aad357203fd279fb286d2c4ee5722b39edef000fa9867bfce8d8ae
156,1789138800,1,ok,78763.41369144642,78763.41369144642,78644.59793614973,78547.27164317717,Down,Down,1,1,1,1,1,78627.63347641155,Down,Up,1,1,-216.14204826925,-97.32629297256,af69112766602838bf656f9c69a1628a3665a961e2f436100f81fafb4ef836db,13b1d17a49aad357203fd279fb286d2c4ee5722b39edef000fa9867bfce8d8ae,d5315588e7b4ecfd15937851238dfba1aceff8dd22f7380cb232d3d4b9232b03,433e88dd4bb755b8f2e8afd54a26823ba75cb13ab725bb326b1e933d7b9b107e,885f98d1b5c35dc0eb0328f56e146a0fd8f55275decd7d93d1d2b454bf633539
157,1789139700,1,ok,78547.27164317717,78547.27164317717,78695.93119214514,78722.34863621516,Up,Up,1,1,1,1,1,78630.47348264395,Up,Up,1,1,175.07699303799,26.41744407002,defd68297168eb0ab591a13c52b56591e1f2cf87e4753e2273ad554b831172e1,885f98d1b5c35dc0eb0328f56e146a0fd8f55275decd7d93d1d2b454bf633539,6bb17470af5192c19f8a28cecd1c67f0edd6ad9c25acc862dfff7c71bd1da7a1,f98a953ecd9a5c36ad0b193b5d73e86ab2f566442750e0da8393bf4c0a13710f,d2872589d281ce41d7be6b3289cc47a504b68ae0df51c1a8f1fe7d24488f214c
158,1789140600,1,ok,78722.34863621516,78722.34863621516,78759.51623783176,78648.5942038761,Down,Down,1,1,1,1,1,78788.3842337355,Up,Down,1,1,-73.75443233906,-110.92203395566,ca50ad371a0bf746dd673b5bd37d22ad2d736277e7b35a238c8ca45b46d64c82,d2872589d281ce41d7be6b3289cc47a504b68ae0df51c1a8f1fe7d24488f214c,be3eb90391658d131a2b9e4080f6d3f3b9579d4cbd70d6ea8a1a354d4ee1a0fd,b3189bb675e65a318cc9a6d1d11360dd07f35c95037d957633b23a5fc7afe332,0531146ed1b9a1e07751e38a4bcab8005beeaedf2f085d7a167de71c1886feac
159,1789141500,1,ok,78648.5942038761,78648.5942038761,77628.87576809042,77668.25470617329,Down,Up,1,1,1,1,1,78521.61767927674,Down,Down,1,1,-980.33949770281,39.37893808287,c50298c66be45a2d2ac0561383ae21994b55a930f29139f6d3da4b936f4e95a0,0531146ed1b9a1e07751e38a4bcab8005beeaedf2f085d7a167de71c1886feac,4d74ea5f973f075b4486521dea583e28168d5b4b1e05207c727428d9b7af8d71,c773a614b746c440f8bfd272e0e46e8fc26e6a896df54c557e5b8ee946119bb1,2817a6a86375e97bd0e82a394a16fe07f1aa53e9accff5debc87869ae2511f62
160,1789142400,1,ok,77668.25470617329,77668.25470617329,77938.71495375333,77794.3191741158,Up,Down,1,1,1,1,1,77812.47411387254,Up,Up,1,1,126.06446794251,-144.39577963753,417702c9010ac93e44d0f9388ddd5f66ba869aa498e265eac862fe61a11d9224,2817a6a86375e97bd0e82a394a16fe07f1aa53e9accff5debc87869ae2511f62,a87721a47909f8be264867a79c24c63b8ff60f172dbaa9bdc5c3d241daeb886c,7eaa2b95190f5858333b335f0db68cfd31f42b7f841f00cbbdc42edb27e90a66,c8c3ca829a541f6efd7232d2fdde9f982661f8bb68168c590d2e2d2cb6a20e96
161,1789143300,1,ok,77794.3191741158,77794.3191741158,77454.15564962271,77677.47901575633,Down,Up,1,1,1,1,1,77589.02089332421,Down,Down,1,1,-116.84015835947,223.32336613362,5824a5f56c027b39c87b7abeadbcf939f2530afa33b20e5a5ea86a4616871c20,c8c3ca829a541f6efd7232d2fdde9f982661f8bb68168c590d2e2d2cb6a20e96,b5df38740fdb39b49ac36f0e8e7ca5e186275a9ca49e3d5db12ee074a2d2f7c8,dc13a8bbf8d8198f96060784116bf95de86ef73243571edf2525e419b4600d9f,06ffccff4349d15becb4d6723d42ab768ba8c4969a2ab5593e6f7dc7d067b606
162,1789144200,1,ok,77677.47901575633,77677.47901575633,77644.1077952854,77771.3690293438,Up,Up,1,1,1,1,1,77717.73855340396,Up,Down,1,1,93.89001358747,127.2612340584,c385043c357b0ae8b60fbee0d3428c1943498ca0f6711a9a141e258f87626e9d,06ffccff4349d15becb4d6723d42ab768ba8c4969a2ab5593e6f7dc7d067b606,fc313d83337c71a80e63a376e96f18836772d1abb263267fc2c7ed7e9d53b225,6c23aeb569baa2b3a875790b79081642ecd625f2caf3b4598eb616a8e6bc6936,f9c7910fbf12322f71aee3913a41fb361be900174fb545745723948dee37fe11
163,1789145100,1,ok,77771.3690293438,77771.3690293438,77878.48923510186,77916.59934103714,Up,Up,1,1,1,1,1,77908.11937624824,Up,Down,1,1,145.23031169334,38.11010593528,a70a34b04f00cd4102f0504bf0ee0c44971d505f4782983f22d200d49692e885,f9c7910fbf12322f71aee3913a41fb361be900174fb545745723948dee37fe11,c67fd5708f8b21459af7346d6341fa6d555343c38e6af17fbaecea1127b73699,45bbfeb9bca266cd50c0d9201d03822013868d9f934c3b5cdc300fc43eb1e39b,fcdd57d24969a969d27f50ad647b01cb79f28602cc53fe5c3251096f086199be
164,1789146000,1,ok,77916.59934103714,77916.59934103714,77795.44348735148,77763.99743895458,Down,Down,1,1,1,1,1,77826.00341591836,Down,Down,1,1,-152.60190208256,-31.44604839690,a414f562cd3a44174f68aa1f60864142a0f2e2fd5620d1de1a0088028f9db278,fcdd57d24969a969d27f50ad647b01cb79f28602cc53fe5c3251096f086199be,533d8a717973da3cb378d57516899ba794efb8ccaee643757689083acef24947,385640f236f104b0ef6f474478273d73c499d2d47c87978e68d67e7af17e3d6c,14f38f3d6a64e70ba440df827f71a9393b84e383751d824c78d0bffb07a78883
165,1789146900,1,ok,77763.99743895458,77763.99743895458,77821.92941674418,77822.3837416681,Up,Up,1,1,1,1,1,77813.80840664764,Up,Up,1,1,58.38630271352,0.45432492392,b3eef6b228dd5980e529ca6cd6a4be8332e718f39bb75b28f76aebff0af36153,14f38f3d6a64e70ba440df827f71a9393b84e383751d824c78d0bffb07a78883,ef78bb2ec736856eea7f141b8518e51c9bdf9aeaf11343769ff9842d8a1ac90b,63d629716b015b09c48366ccac95edbf5bc6e3db3c954db5cbf83ddbb068fc97,921cb3b78403fff48087d59c01584889e17884fb42e0c7d8d3b481cbaa1f50a1
166,1789147800,1,ok,77822.3837416681,77822.3837416681,77576.93700616795,77612.49099064001,Down,Up,1,1,1,1,1,77793.5792824782,Down,Down,1,1,-209.89275102809,35.55398447206,fd0631ab6545b659f5ebdb971dc6aff8488507bd7baf26314e0356d0775bcd1b,921cb3b78403fff48087d59c01584889e17884fb42e0c7d8d3b481cbaa1f50a1,faae484e810f424155f3a0f8558222a38694a84ba2a6cfbc989194c9a50db3c2,c6fa56b176ba7792c2c3d41fc78fa554fd44a7e2456eab7fef1f0feef6e7e089,01158957702e620114cb90794a4c9b4d4e36900b78c3602b55a7c83a0f1c5202
167,1789148700,1,ok,77612.49099064001,77612.49099064001,77501.8388405545,77521.31250632214,Down,Up,1,1,1,1,1,77586.47332880799,Down,Down,1,1,-91.17848431787,19.47366576764,1d50e705aebd8c904e1142a42e964cc384c77ab5e37d19755390579832125346,01158957702e620114cb90794a4c9b4d4e36900b78c3602b55a7c83a0f1c5202,bc34e5278545308f08553dcc29a9399c1ebad6307b92f45d04cf1a2a6f53a762,b703f8584626b08503676a6888d7e296bdb18b636a7e92a9737f168f5b3d25f3,1242cec58d056a061fee7af28a020d22c0676aff18438733cb823230fe7c3909
168,1789149600,1,ok,77521.31250632214,77521.31250632214,77102.37183384618,76995.98566464451,Down,Down,1,1,1,1,1,77101.79722402354,Down,Up,1,1,-525.32684167763,-106.38616920167,4afaa8778dd25227ebdc46976892175d08c0a4737bef38ef0446b7f1a362c31d,1242cec58d056a061fee7af28a020d22c0676aff18438733cb823230fe7c3909,9d34df0779d9b2b31b4b2e093d0e32398c1fc1210b7620b61be30b3a97bbe7ef,7d6a067c68bc236b64ccc13f2028035959828abeb194d9f276e05c3edeccc918,5ac78c0c5e4b74ebb0ba5cce7cdc4f3141446b43ec5f4bf5bdd11037e6125735
169,1789150500,1,ok,76995.98566464451,76995.98566464451,77130.2532053917,77182.11334112498,Up,Up,1,1,1,1,1,77217.33712144825,Up,Down,1,1,186.12767648047,51.86013573328,881f9026f08c54ceda40f45757e568fb6f5fd1c2fbc1834befb948549490452d,5ac78c0c5e4b74ebb0ba5cce7cdc4f3141446b43ec5f4bf5bdd11037e6125735,bd24d0705be5392cef15d2d99275651d6712fd31bd1cadcc43e93e0831edf380,8f23c9dcc368fb6206a5698992f2d68116343e95863555a49e38715093d05cb9,a25697a009339b4cdb1808d6ddd9b46e6be768718324f073d71030865bbe8176
170,1789151400,1,ok,77182.11334112498,77182.11334112498,77200.4961876118,77089.4514950134,Down,Down,1,1,1,1,1,77214.09851737219,Up,Down,1,1,-92.66184611158,-111.0446925984,1ece101027e2a90aec1c65f2382820f409e547ca032685165f522d0f1b64428f,a25697a009339b4cdb1808d6ddd9b46e6be768718324f073d71030865bbe8176,9f5811f6dce4cf2f2eb0283e61fcdac80054dce886b9a4a6d6784cf83f0eb694,7ff1982e7744430056a3c444153d899f593083151406d93c961feb89d4fbbf57,9ee5f1583957c75fca74f321d1e98d4808462411b3b9cb68a01c9f6bde23e08c
171,1789152300,1,ok,77089.4514950134,77089.4514950134,76949.7176886125,77031.32450001215,Down,Up,1,1,1,1,1,77036.03338834947,Down,Down,1,1,-58.12699500125,81.60681139965,d009c1c16de4ab057f67e90ceefa2b4d161596b81da030b728f6525a3542b7fc,9ee5f1583957c75fca74f321d1e98d4808462411b3b9cb68a01c9f6bde23e08c,3148339370569e1b2a276ff52a41d28099170b05d22346b87d8d7824ead5eebe,79f67c71afef2fe3e7d386c5a828d425044aa0bb927b6a9d5b6ffdb510e21edd,3f9a9b9bd365c2e534d9dff43a8bd164d48641992c8f59a7a96f60698bf16966
172,1789153200,1,ok,77031.32450001215,77031.32450001215,77185.39891162432,77181.27277206692,Up,Down,1,1,1,1,1,77119.58174336745,Up,Up,1,1,149.94827205477,-4.12613955740,1c1d283d0746eac4ede04c3f0d06e5839bca3bc2719200f65687d7d8b982a32f,3f9a9b9bd365c2e534d9dff43a8bd164d48641992c8f59a7a96f60698bf16966,f335bc696273beb03f6523e7bc2bc7cf7ddbb6f7b767489b376b45905faf3f4a,700f7bbafe311ca8b8d7f04f5dcbe91b4b6f0d520fb5481c1f03691ba20337f2,1648884504560527d9dca5dee8118e04c718af87f70391169e9019e1111a0bd4
173,1789154100,1,ok,77181.27277206692,77181.27277206692,77221.50881796956,77247.16886966211,Up,Up,1,1,1,1,1,77154.6761069922,Down,Up,1,1,65.89609759519,25.66005169255,dc6334bfb74c2bd298e45b78a7d177ff33eaa19f0a07b856b953db52a1d0baec,1648884504560527d9dca5dee8118e04c718af87f70391169e9019e1111a0bd4,dfa1aec0ed0bc84711d54e4e02bec9c98f189308979006ed27667c33a022daf0,667155a378e77bf66b0e91c9aeb0abc3c8faba216f1927ef49d0083afc9e1607,8b23775cd172254ec3dcf083621047e37386e1b9a2a8143b95ff733f795ba143
174,1789155000,1,ok,77247.16886966211,77247.16886966211,77227.85685040572,77268.0480298392,Up,Up,1,1,1,1,1,77196.005095984,Down,Up,1,1,20.87916017709,40.19117943348,5ed3cc3ff37ad0f2494cc8ec98455cf03d0ad80d989cb6edb82d082469fe5a37,8b23775cd172254ec3dcf083621047e37386e1b9a2a8143b95ff733f795ba143,3a41dc5a016ffbcf58b4072bae21dd23dcbaab038b1f2242a1068eeb58d54c22,a7f9e03b699d2015f8c0a1492ca4872005f65591aa89aa4eeb5fc063dcd1efe1,fc4f8d9c8213a3a68c672fa363742bbd68c42b7e7362a1977336b7e31f10af96
175,1789155900,1,ok,77268.0480298392,77268.0480298392,77312.27564890587,77307.19315620817,Up,Down,1,1,1,1,1,77283.70851719969,Up,Up,1,1,39.14512636897,-5.08249269770,94bb99bc47fab519df16816c507afada5cc10c0e565ec1fa891ce6144498c62c,fc4f8d9c8213a3a68c672fa363742bbd68c42b7e7362a1977336b7e31f10af96,e7e4d97b8bbe1a19964889ff66ce3d3362f931a8f1787c39604230f52f7a8601,a1b9b5a194c92a5b1449b0a992e510a77e5b056fd6a1a87c0c231569f0ecc1f6,0621124907b8735e059edeb7539561994c7045d97ecab5538a0f700cbfc68304
176,1789156800,1,ok,77307.19315620817,77307.19315620817,77410.84798232243,77447.0139029806,Up,Up,1,1,1,1,1,77416.93941606335,Up,Down,1,1,139.82074677243,36.16592065817,980e32745f319050a06c025abb6bf87db7bbabdae19c944208a1a0d0eff46786,0621124907b8735e059edeb7539561994c7045d97ecab5538a0f700cbfc68304,34e7712da333e4dc8c9f06a29098cc9acc7908cfaf8974703bf8fd755ac67d97,ce44fd435c335d3c837f1f2f43f2380b9bb8a6cfa90c6f2f8cb847f4ffa11d8a,98e9a7d1830e7f81fec7030ab24d6b1d30e898d9a424cd7ed6c6c44919c8b4a8
177,1789157700,1,ok,77447.0139029806,77447.0139029806,77403.29269331139,77376.81110068176,Down,Down,1,1,1,1,1,77361.82786038534,Down,Up,1,1,-70.20280229884,-26.48159262963,b30207f80322384db70b1fc478dcad22fe5fd9dfec4b3f23fe7e994bdaf872e6,98e9a7d1830e7f81fec7030ab24d6b1d30e898d9a424cd7ed6c6c44919c8b4a8,a1afb4f7b7758a29b3fcff158b4ce242a7bad066a388efae09e1ae6d10d69679,66e2b482e0e1e84f2a35cf937485d1490de2e05b36f68f66a1e152f2b7a8ef46,f7c9591a998708caaf17409e47403595446b759821065ad19a1617cf20e84af2
178,1789158600,1,ok,77376.81110068176,77376.81110068176,77418.95220262479,77379.96045777074,Up,Down,1,1,1,1,1,77347.23277563512,Down,Up,1,1,3.14935708898,-38.99174485405,d389e48927dae5e86ff37e0080acab73a2f823449a2acb4fb94410bb4263a7a7,f7c9591a998708caaf17409e47403595446b759821065ad19a1617cf20e84af2,1f718ebae47a686b6d59269b19edc1b3d1d5919ff2b135e6649fc04f85705b0c,cf093c1ec8f29d337187d06f64e4a2f84b2d1c0f6a788fc48dbf28eb18c4e150,d50c696d63556983caf13bed8f1423b00232e793b7634c61a9f533b2acbdaca8
179,1789159500,1,ok,77379.96045777074,77379.96045777074,77231.25978574865,77322.81764097062,Down,Up,1,1,1,1,1,77262.80677982928,Down,Down,1,1,-57.14281680012,91.55785522197,6f03735bed296dca7d3de98ad9d9fc631e0bf6408c5c63be6aa321e33479fdd2,d50c696d63556983caf13bed8f1423b00232e793b7634c61a9f533b2acbdaca8,8d61ac9791a3d360c93c48222fcbf9821ea6a824f35cc81c42ed8401cdb04cfe,bef5f05151257e9e47d3969a04734be88194da7573f030c68ae0625ce8d34ff3,766b9b1b932f0fb5b69db005b9f9d11ab0e9e4603ccd228ef05757910987e6e2
180,1789160400,1,ok,77322.81764097062,77322.81764097062,77371.86763226046,77321.13326667031,Down,Down,1,1,1,1,1,77325.43931587391,Up,Up,1,1,-1.68437430031,-50.73436559015,b12a00e0357f20b88d7bfb06740c715333cbadcd8cf0c2a4047315e54428bb06,766b9b1b932f0fb5b69db005b9f9d11ab0e9e4603ccd228ef05757910987e6e2,e1f45fc4bba4e4018c8871feb55ae208ce7bfcc3b9ac7b014e0383030ea1bb08,c829c1f2c76c7a1764f3f5d661f7c09ae8d70541a11fe9f888c72c089ae6452f,bc6b6246a24d2a9816582b347509ceadedb74fe4e437f8210499f30423365574
181,1789161300,1,ok,77321.13326667031,77321.13326667031,77371.57654548716,77339.02214950044,Up,Down,1,1,1,1,1,77383.38933145914,Up,Down,1,1,17.88888283013,-32.55439598672,71e6e5e281deba2c963c4c66f9feb36025b8022481865e06af05156a96a635cf,bc6b6246a24d2a9816582b347509ceadedb74fe4e437f8210499f30423365574,f5730c5816145871c30c8ed121eb46bd0ba7bf4551ee008d3b1c1391af588682,ce1975bf2b23ebfcce0e3689d55389f48fc13e452c173f1aea559e8fee45d00c,2665668e50921f7be76cb6d6fb402096d91f5967d5b37d4d0fab9b0de75b1446
182,1789162200,1,ok,77339.02214950044,77339.02214950044,77370.3335314192,77323.3258708182,Down,Down,1,1,1,1,1,77352.52031674965,Up,Up,1,1,-15.69627868224,-47.0076606010,37ec3b92f32e5fe5c0ce66a37bc6fe8dfbf15858582ab5772250ed660dfcfe3e,2665668e50921f7be76cb6d6fb402096d91f5967d5b37d4d0fab9b0de75b1446,93be1c65ea8833c475948d7cfd9f560712e8d54ee377208e852f65b1e2ad0682,ce8156e458b7105add50ea614fc132c9cebe8a168bf07055ad066312c820aea4,5552dfc2d505cf8861cc46688bd1123992da06dbcbbb437c5ce337094c659efa
183,1789163100,1,ok,77323.3258708182,77323.3258708182,77217.05996916893,77072.37806427931,Down,Down,1,1,1,1,1,77265.00216856695,Down,Down,1,1,-250.94780653889,-144.68190488962,6f0f4cdafa480d58b666d24d71aa6f1ff8aab4e3ec273d05baa37216f1298c0f,5552dfc2d505cf8861cc46688bd1123992da06dbcbbb437c5ce337094c659efa,50d890b9b98624c09792d4f57c53181f77d00da7943fb37fd7c2eb2b4ac7f0e8,3cd8b0c079e60d4b4162db87bbd37952125f6983c92f67e1fd25d9114b42d8af,07694d31e84a26ddf05073f4219d084fd5149a1d255acc706b74fa23d1c184f8
184,1789164000,1,ok,77072.37806427931,77072.37806427931,77076.15447540258,77159.95095010198,Up,Up,1,1,1,1,1,77113.37649553461,Up,Down,1,1,87.57288582267,83.79647469940,85da33071f136dd79fef2a19e8aa001d6b0c260ebfbf26fedaa7b1551bd06d1b,07694d31e84a26ddf05073f4219d084fd5149a1d255acc706b74fa23d1c184f8,b81e12a9c23131aee874df216c499a1da56c67f39e218b0c77b0c172d13e681d,892393c64632720f194b689ac45fc7e4b322cad1cef890e6cae18af2ba6acaea,241beec427a587a95aa55c8ecd97a9f5188443e0f5712c2d1bee8d793b61db82
185,1789164900,1,ok,77159.95095010198,77159.95095010198,77176.38985587902,77100.877088373,Down,Down,1,1,1,1,1,77147.0690467927,Down,Up,1,1,-59.07386172898,-75.51276750602,e8462d882777ce6fbec6ca221ec248df4098eeae848d2fe1505061ccc9e5a603,241beec427a587a95aa55c8ecd97a9f5188443e0f5712c2d1bee8d793b61db82,2e9a5c7089af9520f23dae8690d167333064ef696a87eccb54ebced822b4f24b,88324c3cd45e989bff0bae1e746173905b88e3c92f453b2e1509bf6f80903a0b,798f5e7c00386fff74d091cab51e99a938a14d989259ae0e9d107f463b5c9548
186,1789165800,1,ok,77100.877088373,77100.877088373,77153.33004426048,77132.7042870074,Up,Down,1,1,1,1,1,77033.07522711034,Down,Up,1,1,31.8271986344,-20.62575725308,836a8e7329a9819c95d32c2808b09c544357281b70c70b30a3df26e573f6a2ae,798f5e7c00386fff74d091cab51e99a938a14d989259ae0e9d107f463b5c9548,c3bfda6ea59d1b114e4413108e7769ce3d7674f2c00bdd267e920d0f69bada93,ae78c1bc997f742816000d00bb4a247e6a0c0e106d0ff125124e95c4be7aa7ca,f0ded1a8f45ab871b72575d45f7563833ea423c9152acaef70650bedd7806c75
187,1789166700,1,ok,77132.7042870074,77132.7042870074,77078.99723150006,77128.46717392042,Down,Up,1,1,1,1,1,77053.18994864648,Down,Up,1,1,-4.23711308698,49.46994242036,258f877460e3895ea5fc1fe9b9c8f6df027fd5c729ad455e9de399c193f649be,f0ded1a8f45ab871b72575d45f7563833ea423c9152acaef70650bedd7806c75,56d37c450fb8b0a3c08749e8877b86bdd13557f53c5e4679a371d489f674dd54,7cf758f76d817969746af9018d420f746700cde0a3a73a59be9f710de1a673e7,d91c05f6cba9bf9c88c2fb8c7ba411dddde08d8dc3a21afcc06d8d872c7558b8
188,1789167600,1,ok,77128.46717392042,77128.46717392042,77171.91714869795,77112.9884726417,Down,Down,1,1,1,1,1,77167.87784434557,Up,Up,1,1,-15.47870127872,-58.92867605625,6a042a7e5baf17a77952b9128295b1613c3416d420967c7222bac419ba41beec,d91c05f6cba9bf9c88c2fb8c7ba411dddde08d8dc3a21afcc06d8d872c7558b8,6f9264a260f22c1e1d3345e778907eb0e96f13cbf9f88f9c77e6b419d959ea02,46d394024b6c6e52c9801ba6fd737c2a3f35a9258583bfa99a42f95b36ec9f33,69a242cda319f44c8d3877b5bdb6dbc58c50fb800be2afeb95404792a2ad8b63
189,1789168500,1,ok,77112.9884726417,77112.9884726417,77135.117116938,77173.31734570439,Up,Up,1,1,1,1,1,77129.15304800164,Up,Up,1,1,60.32887306269,38.20022876639,8c8b5b890b60b1319883b0c1a9d90e003f89ec0ec9978ae3795c083e91ffcb26,69a242cda319f44c8d3877b5bdb6dbc58c50fb800be2afeb95404792a2ad8b63,068e52c75084822ed7efd1cee0464e26698f824d7f597a9fab09afe0e2cbdf19,c5acda27c45147ee98e271855e56d31b30c1f23756cf95fb9e8471cb5f88d32f,98b50a6839e691be23f3df846eefad1d5e187719bd1619bbe368e52aa216463d
190,1789169400,1,ok,77173.31734570439,77173.31734570439,77185.72594969244,77199.53342264291,Up,Up,1,1,1,1,1,77184.84321599228,Up,Up,1,1,26.21607693852,13.80747295047,9fbc971ba615b100415a92260a6ae02308482ce176715cf56dc9e8beae7a1b5a,98b50a6839e691be23f3df846eefad1d5e187719bd1619bbe368e52aa216463d,87c80b09b96e50b0b5b8f6c895ff96d0ef501b215da8aff111ba91b9856fd5d4,1027ce59e9ce8a9e389b0ef9ac0f9cc7ddb2c9427f41be758129283168317656,a9e1b427b89ed3682aee5869297ca708f52244601f26315610c00d43edf0f247
191,1789170300,1,ok,77199.53342264291,77199.53342264291,77174.11470858997,77205.50569273818,Up,Up,1,1,1,1,1,77167.44622641175,Down,Up,1,1,5.97227009527,31.39098414821,4bbdd41672849cbb51a6f747ce35c56bdb6a730c3b827f44e67154c7af5c861a,a9e1b427b89ed3682aee5869297ca708f52244601f26315610c00d43edf0f247,8af5c9861055aaaa51b8f2c87343da4db0619d94d0b2511ec3b21ba5211b3ccd,d7c0b9e94fcd969e8d6281800803dc033cd7be3eeb42fb86bbee56d52402a8a4,54043e251c57e5d9c9823df2807db6ea18d45b30a77e01f3ccf9f013c46471cc
192,1789171200,1,ok,77205.50569273818,77205.50569273818,77281.1030921258,77269.61766176127,Up,Down,1,1,1,1,1,77277.05179019556,Up,Up,1,1,64.11196902309,-11.48543036453,df3419464af593b30ff290736e4d70909aa3b64de99b1f366b1ab3b66cfc39e9,54043e251c57e5d9c9823df2807db6ea18d45b30a77e01f3ccf9f013c46471cc,471944a45639da636c1b9c9f2c5f8c73676c9732387bd8a0bf3501e24366ca5a,11ee7d08c22bdad30a9cee890be106a867900f543284547d5ef473c9e96b8d7c,7d796e30716bf5617634cbfb717277ebb6a3d4a8310baaac3a0e82a81db26d85
193,1789172100,1,ok,77269.61766176127,77269.61766176127,77279.13831924475,77266.43024333965,Down,Down,1,1,1,1,1,77273.6503481681,Up,Up,1,1,-3.18741842162,-12.70807590510,d79a6302a254e9ce0424a283b080a3fed43dffc62f34122162d9eaa69b0e8ccf,7d796e30716bf5617634cbfb717277ebb6a3d4a8310baaac3a0e82a81db26d85,e840e81303d3821d6da31751b7cff0a6ed856e2cfdeba18e49bade21d446c14e,1e04292bb7ea4ccb4fac46f8c0c3fa39a52b0ed2ae3954494cfebc150dc6ff33,7bac0263692393ad574be15ec68470ccb4ccc826046beb00bb94c54ca1cd0c92
194,1789173000,1,ok,77266.43024333965,77266.43024333965,77240.63025225434,77274.66448019513,Up,Up,1,1,1,1,1,77256.25308488728,Down,Down,1,1,8.23423685548,34.03422794079,647be00e50825f5e49c8ce66d6e46231d6a5e82b0af0b80040ce6decb981f20c,7bac0263692393ad574be15ec68470ccb4ccc826046beb00bb94c54ca1cd0c92,b326dc90e3b9a30759aa650e5f7ca15bf1ef0805cae80b3d01a28a538b1c0109,f624f6415d3e75a3fd9bf85d85b869be19521a83196550739e328feea2e4ad51,1d3e8ccba96038a679b452d554a1c52e7ca5391ef59b9c096d0cfa642ae58c9e
195,1789173900,1,ok,77274.66448019513,77274.66448019513,77289.9541598107,77284.26465316408,Up,Down,1,1,1,1,1,77273.95215028716,Down,Up,1,1,9.60017296895,-5.68950664662,288ab1d45aabfd822bf0c84651df87db99c99ae4476d4bc1e8111b10c20a740d,1d3e8ccba96038a679b452d554a1c52e7ca5391ef59b9c096d0cfa642ae58c9e,1f1a6f905d0433473f3b8235f225e793bb0a92ffc5e99aaea3cb6c4a53fd8713,15142c0f9f9b0fb0d973c6e188a6eac760624d88dca40f5902e08c4bb9ef901a,08f0970e0d1cd1e35ad9a22ca5c97d8cf1e3df8ef4f533b41ce2f8d6f7b910f9
196,1789174800,1,ok,77284.26465316408,77284.26465316408,77333.54730925051,77348.88132792329,Up,Up,1,1,1,1,1,77254.15445104164,Down,Up,1,1,64.61667475921,15.33401867278,0c9ef6686f70b23a45f87610ab7bda57f48e00c1e3c90809f0661687b29b5e92,08f0970e0d1cd1e35ad9a22ca5c97d8cf1e3df8ef4f533b41ce2f8d6f7b910f9,c1417ef369ccc5d83027a9b6c679aa2c364a36d998f5603696bbc82647c53869,a31dc9f75a0994e9bfad5a8f8f33dff3a27f97c379754ffe623e427bd34b72d6,29d64bb93557342a13386a517f86b7f442d776c9b336201b27ea622c8a74384a
197,1789175700,1,ok,77348.88132792329,77348.88132792329,77311.86691549564,77308.64819994534,Down,Down,1,1,1,1,1,77358.84267634098,Up,Down,1,1,-40.23312797795,-3.21871555030,2533a2e1905e763109e66434d281188240d3f8d615c6a97a45fab39eb291af57,29d64bb93557342a13386a517f86b7f442d776c9b336201b27ea622c8a74384a,7717591c9dbd64fc8a512d56802f3d81b1dc9871fd8bbf9508fb44641152af54,3a87b4454eaa377901989aa129a26257e0049a983b73fea8c26d928c181f3f2e,fa5d69127b42ae8a18dcef4154767f7ac501792884d603bd5427d5f6b044cffd
198,1789176600,1,ok,77308.64819994534,77308.64819994534,77262.24932891903,77263.42445034436,Down,Up,1,1,1,1,1,77309.28732353343,Up,Down,1,1,-45.22374960098,1.17512142533,80778036a5e472625d5c36a4126b7d0b69ce2ab583a30fe67c24a92494a033c2,fa5d69127b42ae8a18dcef4154767f7ac501792884d603bd5427d5f6b044cffd,2fb54b80bed98b778b7d96a2abbed2724c86b308ed2b012bba8795747fbec3fa,83bc55a5c8933298692ba65dd7ef4cfe33fb9553582b45a0361169173a2c9440,4bd794fc55869014ab4d73ef07715eb4dca7b7509c54d7436164daeef0834ebc
199,1789177500,1,ok,77263.42445034436,77263.42445034436,77276.83793307896,77261.72875943598,Down,Down,1,1,1,1,1,77296.09480840537,Up,Down,1,1,-1.69569090838,-15.10917364298,c18e3bb8e17e9bfb5093828cff8214d3e3458785eb5a76aafa534f2ff23266e5,4bd794fc55869014ab4d73ef07715eb4dca7b7509c54d7436164daeef0834ebc,f9daf093012ce721985b791b87a737ba3d93315ff58bf573ee6af83adaafbddf,b83b3a51c0664bfe6af5e50734a69f8b47f866782c54a4fd46609d31928b1f9a,6dba7c733895a6a19f0e226cb2704a35de74c1d979c9f075adc00a7a14133b5c
```

### 2.12 `tz17-summary.json`

`fb20cbf15751fdaac3dd0d2736192f891d746b91eab1db9bcef81d6a4e788937`, byte-identical at R2 and R3.
Its `D1_I1_exact_members` array holds the 200 member `T` values and is not reproduced here — it is
the member list of §2.1, whose SHA-256 is printed there and in the CSV's `T` column. Every other
key:

```json
{
 "D1_I1_exact_count": 200,
 "D2_I4a_checks": 200,
 "D2_I4a_holds": 200,
 "D2_I4b_checks": 200,
 "D2_I4b_holds": 200,
 "D2_excluded": 0,
 "D3_exponents": {
  "K15": {"-10": 33, "-11": 163, "-9": 4},
  "K5a": {"-10": 33, "-11": 163, "-9": 4},
  "K5c": {"-10": 36, "-11": 161, "-9": 3},
  "K5d": {"-10": 33, "-11": 163, "-9": 4}
 },
 "D4_near_strike_d15": 1,
 "D4_near_strike_d5": 5,
 "D5_event_metadata_keys": {
  "15m": {"finalPrice": 200, "priceToBeat": 200},
  "5m": {"finalPrice": 601, "priceToBeat": 601}
 },
 "D6_resolution_source": {
  "15m": {"https://data.chain.link/streams/btc-usd-twap-60s-streams": 200},
  "5m": {"https://data.chain.link/streams/btc-usd-twap-60s-streams": 601}
 },
 "D7_nonmember_first_code": {},
 "I1_holds": 200,
 "I2_holds": 200,
 "I3_holds": 200,
 "N": 200,
 "candidates_considered": 200,
 "gate_fail_at_or_below": 198,
 "gate_pass_at_or_above": 199,
 "largest_requested_5m_epoch": 1789178400,
 "member_count": 200,
 "member_list_sha256": "68ee20bcb4a915604ebefca4b6908853810b6c6003928777e59769a3b225cebc",
 "power_rate_0.01": "0.595354315327973499366704428681",
 "power_rate_0.02": "0.910624516228067965960219332490",
 "raw_bodies_rehashed": 801,
 "reading": "PASS",
 "set_complete": true
}
```

The file as written is indented `1`, keys sorted, `ensure_ascii=True`, one trailing newline; the
block above is that file with `D1_I1_exact_members` elided and the small nested objects folded onto
one line each for reading. Its hash is the hash of the file on disk, not of this block.

Both power figures the instrument computed in exact `Fraction` arithmetic reproduce §4's literals
to all 30 printed decimals.

### 2.13 Audit route

Every literal, outcome and flag the Architect re-derives is in §2.11's CSV, with the SHA-256 of each
of the five stored bodies beside it. The bodies stay under `/root/tz17-work/raw/`, and the endpoint
is public and unauthenticated, so any document can be fetched again and compared field by field
with the CSV. The member list is the CSV's `T` column in order.

---

## 3. Publication

| field | value |
|---|---|
| branch | `tz-17-settlement-chain` |
| implementation commit | `8f1bc93e454275ddb3f0e060bed3bb9f2f9cf31b` |
| file added | `research/tz17-settlement-chain.py` — 1,102 lines, 38,622 bytes |
| SHA-256 | `e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92` |
| pull request | [#17](https://github.com/seahomebatumi-ai/btc-5m-twap/pull/17), opened against `main`; **not merged** — merge is the Boss's, after the Architect's verdict |
| Release | none created, and none required: this TZ produces no asset over ~1 MB |

**V10**, run after the branch push and before the report commit:

```
$ git diff --name-only origin/main origin/tz-17-settlement-chain
research/tz17-settlement-chain.py
```

Exactly the one path the TZ's §2 allows. The change is insertions only: the path is in neither the
map's §0 fingerprint table nor its §3 code table, so it replaces no committed line.

**V11 — contract §4.2's mandatory separation self-check, verbatim:**

```
$ git rev-list origin/main | grep -c 8f1bc93e454275ddb3f0e060bed3bb9f2f9cf31b
0

$ git diff --name-only origin/main origin/tz-17-settlement-chain
research/tz17-settlement-chain.py

$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
(no output)
```

The first line prints `0`: `main` does **not** carry the implementation commit. The branch differs
from `main` by exactly one implementation file. No dataset, archive or binary is in git history.
This report is the only path this TZ pushes to `main`, in one commit, from
`/root/tz17-work/wt-report` by `git push origin HEAD:main`, as the TZ's §0 requires in place of
contract §4.1's `git checkout` lines. §6 below records when this check was run relative to the
report commit.

---

## 4. Gate

The gate as the TZ fixes it, before any document was fetched, quoted:

| reading | condition |
|---|---|
| **FAIL** | the set is formed and `N <= 198` |
| **PASS** | the set is formed and `N >= 199` |
| **UNDECIDABLE** | the set of 200 cannot be formed from candidates 0 to 399 |

The set **was** formed: 200 members from 200 candidates considered.

**The deciding number is `N = 200.000`.**

`200 >= 199`, so the reading is **PASS**.

Nothing was tuned to reach it and no row of the table moved after `N` was known. `N` is asserted
nowhere in the instrument — it is read by §4 and by nothing else — and R1, which fetched every
document, computes no identity of §3.5 at all, so no re-run could have selected on the gate.

What the TZ fixed PASS to mean, quoted: *the two market types settle on one reading at a shared
boundary. The next step needs both books read at the same instants; it is a deployment TZ followed
by a measurement TZ, never this one.* This report opens no book and proposes no next step; it
records that the backup track's first step did not close.

**The error rates, as the TZ states them:**

| figure | value |
|---|---|
| false-failure probability under the model this gate scores | exactly `0` |
| family-wise figure — one statistic over one set | exactly `0` |
| power against a `0.02` per-window failure rate | `0.910624516228067965960219332490` — above the `0.8` floor |
| power against a `0.01` per-window failure rate | `0.595354315327973499366704428681` |

Both were recomputed by the instrument in exact `Fraction` arithmetic as
`1 − (1−p)^200 − 200·p·(1−p)^199` and agree with the TZ's literals in all 30 decimals (S8, at a
tolerance of `1E-18`). The second figure is the honest limit of this reading: **a PASS here does
not claim a one-in-a-hundred anomaly rate is absent**, because against that alternative the gate
has power `0.595`. What it does claim, it claims at `N = 200` — not one window of 200 failed any of
the three identities, and the observed count leaves no margin between PASS and perfect.

---

## 5. Validation

Every row below is an `assert` inside the instrument that aborts the run when false, unless the row
says otherwise in plain words. Counts are derived from the run, never typed.

### V1 — the fingerprint gate. **Asserted. R1, R2, R3.**

Revision `2026-09-19-c` equal; **6 of 6** anchors equal, four of them re-derived from their files
rather than read from the table; **25 of 25** rows hashed; **22 of 22** `frozen` rows equal. §0.1
lists all 25 rows with `wc -l` and `sha256sum`. Held identically at all three runs.

### V2 — host and resource gates. **Partly asserted. §0, R1.**

H1, H2 and H3 hold; the evidence is §0.2, verbatim. Available space, each figure printed:

| when | bytes | against |
|---|---|---|
| §0 | `13,528,887,296` | `2,200,000,000` |
| R1 start | `13,521,006,592` | `2,200,000,000`, **asserted** by `os.statvfs`, `f_bavail * f_frsize` |
| R1 end | `13,513,474,048` | `2,200,000,000`, **asserted** the same way |

The two R1 figures are asserted inside the instrument. **The §0 figure and the three host
conditions are read by the Executor at the shell and compared by hand: recorded, not asserted.**
The TZ's §0 states them as shell commands whose output goes into this report verbatim, and that is
what was done; no script of this TZ re-evaluates them.

### V3 — P3 before every request. **Asserted. R1.**

`841` P3 checks against `841` requests — `801` Stage F plus `40` re-fetch — asserted equal for
Stage F's `801` at the point the set closed, and each individual check aborts the run on violation.
Largest requested 5-minute epoch **`1789178400`**, asserted at most `1789358400`; largest requested
15-minute epoch `1789177500`, whose close at `1789178400` is likewise below the boundary. No row of
this report reads a label of TZ-16's span, and none could: the span was never requested.

### V4 — request accounting and re-hashing. **Asserted. R1; the re-hash also at R2 and R3.**

`801 <= 1,601` Stage F requests, retries not counted; re-fetch **exactly `40`**; `801` attempts
against `801` `index.jsonl` lines and `40` attempts against `40` `refetch.jsonl` lines, asserted
equal; **`801` of `801`** stored bodies re-hash to their line's `sha256` and match its `bytes`,
asserted at R1's end and again at the start of each of R2 and R3.

### V5 — one member list. **Asserted. R1, R2, R3.**

| run | member-list SHA-256 |
|---|---|
| R1 | `68ee20bcb4a915604ebefca4b6908853810b6c6003928777e59769a3b225cebc` |
| R2 | `68ee20bcb4a915604ebefca4b6908853810b6c6003928777e59769a3b225cebc` |
| R3 | `68ee20bcb4a915604ebefca4b6908853810b6c6003928777e59769a3b225cebc` |

R2 and R3 each re-derive the set from `/root/tz17-work/raw/` and `/root/tz17-work/index.jsonl`
alone and assert it equal to R1's, both by hash and unit by unit against
`fetch-summary.json`'s list.

### V6 — the self-tests, before anything else. **Asserted. R0, R1, R2, R3.**

**37 of 37**, at every run, before the first network request and before any file but the
instrument's own source is read. `n` is the count the run returns, not a literal. R0 verbatim:

```
$ /root/tz01-env/venv/bin/python research/tz17-settlement-chain.py --selftest
## self-tests
37 of 37
```

By item: S1 `2`, S2 `3`, S3 `12`, S4 `4`, S5 `1`, S6 `4`, S7 `3`, S8 `3`, S9 `5`. Each is an
`assert` through one counting helper; the instrument refuses to start at all when `__debug__` is
false, so the count cannot be hollowed out by `-O`.

### V7 — determinism. **Asserted by comparison. R2, R3.**

| file | R2 | R3 | equal |
|---|---|---|---|
| `tz17-candidates.csv` | `96b5e21e2cc59e2f3bde332d60457533158bd16c2eeaaaba844bf35b1efc63ee` | `96b5e21e2cc59e2f3bde332d60457533158bd16c2eeaaaba844bf35b1efc63ee` | yes |
| `tz17-summary.json` | `fb20cbf15751fdaac3dd0d2736192f891d746b91eab1db9bcef81d6a4e788937` | `fb20cbf15751fdaac3dd0d2736192f891d746b91eab1db9bcef81d6a4e788937` | yes |

Both files byte-identical, `cmp` clean, in two fresh processes from the same commit. Both outputs
are pure functions of `raw/` and `index.jsonl`: no timestamp, no wall clock and no process counter
enters either file.

### V8 — the stability re-fetch. **Asserted. R1.**

**40 of 40** re-fetched gate documents equal the stored ones in `K` as `Decimal` tuples, in
`closed`, in `outcomes` and in `outcomePrices`. The number whose bytes differ anywhere else is
**`0`** — printed, not asserted, as the row requires.

### V9 — the write guard. **Asserted. R1, R2, R3.**

Every open for writing was checked before the open against `/root/tz17-work/` and against both
worktree paths: `1,687` checks at R1, `3` at each of R2 and R3. **R1 wrote `4,442,478` bytes**,
against the `200,000,000` cap, asserted as it wrote and again at the end. R2 and R3 wrote
`103,216` bytes each.

### V10 — the diff names one path. **Asserted by inspection. After the branch push.**

Output in §3: exactly `research/tz17-settlement-chain.py`.

### V11 — contract §4.2's separation self-check. **Asserted by inspection.**

Output in §3, verbatim; the first line prints **`0`**. See §6 for when it was run.

### V12 — S9's syntax-tree guard. **Asserted. R0 (and every run).**

Five asserts over the instrument's own `ast`: every imported top-level module is in
`sys.stdlib_module_names`; none is `subprocess`; no attribute `system`, `popen`, or any name
starting `spawn` or `exec`, is taken on `os`; no call carries a keyword `shell`; and **exactly one
string constant contains `:` `/` `/`**, equal to the Gamma slug endpoint. The needle itself is
assembled from two literals so that it is not a second match. The imports the guard admitted:
`argparse`, `ast`, `datetime`, `decimal`, `fractions`, `hashlib`, `json`, `os`, `re`, `sys`,
`time`, `urllib`.

### V13 — `fetch-summary.json` carries no gate name. **Asserted. R1.**

Asserted before the file is written that its key set intersects `{I1, I2, I3, holds, N}` in
nothing. R1 computes no identity of §3.5 and holds no such value to write.

### The one population every row above is taken over

`N` and the counts of I1, I2 and I3: the 200 members. D1 and D4: the members. D2: the members whose
`M5(T+300)` reads `ok`, which is all 200. D3: the four gate literals of every member. D5 and D6:
every `ok` document, per market type — 200 and 601. D7: the candidates considered that are not
members, of which there are none. Request accounting: every Stage F attempt and the 40 re-fetches.

---

## 6. What could not be implemented as written

Six things, none of them a deviation from a gate, a definition or a formula.

**1. V11's row names "after the report commit"; it was run after the branch push and before it.**
Contract §3.2 forbids editing a committed report, so output produced after the report commit could
never reach the report that is required to quote it. The check was therefore run at the last moment
at which its output can be recorded, and §3 prints it verbatim. This costs nothing that V11
asserts: its condition is that the first line prints `0`, and the report commit adds only
`CryptoReports/TZ-17-settlement-chain-report.md` to `main` — it cannot place the implementation
commit `8f1bc93e…` into `git rev-list origin/main`. The second command's output *does* change once
the report is on `main`, which is why **V10 — the row that actually asserts that output — is
scheduled "after the branch push" and was run there**, before the report commit, exactly as its
own row requires.

**2. `/root/tz17-work/scratch/` exists beside the directories §9 lists.** It holds the pre-run
probe of one candidate's documents and three small harnesses that exercised Stage F and Stage A at
`need = 3` before the branch was pushed, together with their scratch bodies — `8` files and a
`dry/` tree. §9's list of what this TZ creates does not name it. It is under `/root/tz17-work/`,
outside both worktrees, inside the write guard and inside the `200,000,000` cap, and it is retained
with the rest of the tree for the TZ that reclaims it. The probe used the same endpoint and the
same slug family as §3.3 and requested nothing in the reserved span; its purpose was to learn the
document's shape before building against it, which §3.1 anticipates by providing a BLOCKED path for
an endpoint that does not serve the 15-minute slug. It does.

**3. `research/__pycache__/` appeared inside `/root/tz17-work/wt`** when those harnesses imported
the instrument by path. It is untracked, is in no commit, and V10's output is unaffected. **P7 says
no tree is removed, so it was left in place** rather than deleted; later runs were made with
`PYTHONDONTWRITEBYTECODE=1`. The TZ that removes this worktree will need to account for it, as
TZ-13's and TZ-14's did for the same directory.

**4. `pgrep -af recorder` matches the Executor's own shell as well as the recorder.** The §0
command is quoted verbatim in §0.2 and prints two lines; the second is the `bash -c` that was
evaluating the §0 block, which contains the string `recorder` in its own text. H2 as the TZ words
it — "`pgrep` prints at least one line" — is met, and it is met by the recorder itself, pid
`228592`, the same pid the map's §2.3 records for the `4216c04` restart. The closing read in §0.3
uses `pgrep -af "recorder.py"` and prints that one line alone.

**5. The TZ's §3.4 fail-fast, early stop and retry paths were never exercised.** All 841 requests
returned HTTP 200 at the first attempt. The retry ladder, the 20-consecutive-failure rule, the
`2,700` s wall cap, the `41`-request early stop and its BLOCKED disclosure are implemented and
were exercised only by S3's synthetic `fetch` and `status` cases; **no live failure tested them**.
Likewise D7 is empty and the CSV's non-member columns are empty at every row, because there are no
non-members: that path was checked before the run against a synthetic store, not in R1.

**6. The counts the TZ predicts as upper bounds were not reached, and should not be read as
unused capacity.** Stage F's `1,601` is the cost over 400 candidates; the set closed at candidate
199, so `801` requests were issued. The `200,000,000` byte cap saw `4,442,478`. Both bounds held
with room, and the run stopped where §3.3 tells it to, not where a budget ran out.

Nothing else. No committed file was edited, no `frozen` row moved, no capture file was opened, no
authenticated venue call was made, no credential was held, no order book was opened, no tree was
removed, the recorder was not signalled, and no epoch in TZ-16's reserved span was requested.
