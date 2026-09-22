# TZ-18 — the chain book capture, deployed — report

**G-DEPLOY: FAIL** — 0 of the first 14 qualifying checkpoints complete (threshold: ≥ 13 → PASS, ≤ 12 → FAIL).

**G-TIERC: PASS** — 4 of 4 five-minute intervals of the existing capture closing inside the proof window carry `quotes_complete` true; 0 false.

**G-CHAIN: PASS** — Q1 600 of 600, Q2 200 of 200, Q3 200 of 200 equal by exact `Decimal` value; and 600 / 200 / 200 equal as printed literals too.

**The G-DEPLOY FAIL is a defect in this Executor's build, not in the capture design, the host or
the venue.** Every read the deployed instrument issued was refused by the venue's edge with HTTP
403, `error code: 1010`, because the build sends no request headers. Measured, not inferred: with
TZ-17's two headers (`Accept: application/json`, `User-Agent`) the same two endpoints answered
**200** from this host during the run — for a live window's document and for **both** of its books.
TZ-18 §2 P6 and §3.8 forbid signalling the service and §6 R5's stop is authorized only on a
G-TIERC FAIL, which did not occur, so the corrected build could not be deployed in this session
and the service was left running. §6.1 and §6.2 give the evidence, the one-line correction and the
reason it was not applied.

G-CHAIN closes, offline, the gap TZ-17's audit left open: the 15-minute market and the 5-minute
market inside it are settled from the same published number, exactly, at 1,000 of 1,000 units.

Executor model: **Opus** (`claude-opus-5`), as the TZ's header requires. Branch
`tz-18-chainbook-capture` at `8caa0b41d5cdf9e74e92b11d4317d59a2ee7b567`, pull request #18,
unmerged. One repository path added: `research/tz18-chainbook-capture.py`.

---

## 0. Fingerprint

Map revision string read from `SYSTEM-MAP.md` §0: **`2026-09-19-c`** — equal to the TZ header's
required revision.

| anchor | required by TZ-18 | read from the map | re-derived from the file | result |
|---|---|---|---|---|
| `A1` observation set | `229a944f2d51` | `229a944f2d51` | — (not a file anchor) | equal |
| `A2` collector | `6c5089330629` | `6c5089330629` | `6c5089330629` from `research/twap-divergence.py` | equal |
| `A3` phase | `0-complete / 1-student-5tau-not-disqualified / 2-undecidable-5tau` | same | — | equal |
| `A4` executor contract | `437b45ea196b` | `437b45ea196b` | `437b45ea196b` from `BTC-EXECUTOR-INSTRUCTIONS.md` | equal |
| `A5` recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | `9fd1c7de0f74` from `research/recorder/recorder.py` | equal |
| `A6` pricer | `729f0bcdbee3` | `729f0bcdbee3` | `729f0bcdbee3` from `research/pfair.py` | equal |

**6 of 6 anchors equal; 4 of 4 file anchors re-derived** as the first 12 hex characters of each
file's SHA-256 rather than copied from the table, as §0.1 requires.

`A6` is stated because the TZ states it: **the pricer was not read, not called and not scored by
this TZ.** `research/pfair.py` is never imported by `research/tz18-chainbook-capture.py`; the
instrument imports nothing from the repository at all (§2 P7).

### Fingerprint table — all 24 hashed rows, `wc -l` / bytes / `sha256sum`

| path | lines | bytes | state | SHA-256 | result |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 826 | 156,425 | reported | `3a88c35707fb937043b56571d5b146819a43c905122f379ad89fc75c95e3e1a0` | self-reference, computed |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | **equal** |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | **equal** |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | **equal** |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | **equal** |
| `research/pfair.py` | 441 | 19,357 | frozen | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` | **equal** |
| `research/selftest-pfair.py` | 619 | 32,559 | frozen | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` | **equal** |
| `research/tz06-calibration.py` | 577 | 27,138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | **equal** |
| `research/tz07a-variance-time.py` | 623 | 28,414 | frozen | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` | **equal** |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | **equal** |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | **equal** |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | frozen | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | **equal** |
| `research/tz10b-sigma-or-link.py` | 1,224 | 61,018 | frozen | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | **equal** |
| `research/tz11a-student-link.py` | 1,231 | 64,732 | frozen | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` | **equal** |
| `research/tz12-sized-gate.py` | 1,157 | 61,637 | frozen | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` | **equal** |
| `research/tz13-sized-gate-test3.py` | 1,074 | 53,901 | frozen | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` | **equal** |
| `research/tz14-quote-inventory.py` | 2,124 | 109,972 | frozen | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` | **equal** |
| `research/tz15-phase2-gate.py` | 1,517 | 73,799 | frozen | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` | **equal** |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | **equal** |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | **equal** |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | **equal** |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | **equal** |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | **equal** |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | **equal** |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | **equal** |

**24 of 24 hashed rows read; 22 of 22 `frozen` rows equal.** The row for `SYSTEM-MAP.md` is the
self-reference the table names and is reported, not asserted. `research/tz02-distribution.py`
and `.gitignore` are `tracked` and are reported with no expectation; both happen to equal the
values printed in the map.

`research/tz17-settlement-chain.py` is deliberately not in that table, is not gated, and was not
compared — §0.1. It is read once in this report, for the two request headers it sets (§6).

The fingerprint gate above was run twice: once by the Executor before any work, and once inside
the instrument at each of R1, R4 and R6 (V1), where the counts are derived from the map text and
asserted rather than typed.

### 0.2 Host gate — the three conditions, verbatim

```
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13463633920

$ find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json

$ pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'
228592
pgrep exit=0

$ grep -rl --include=runtime.jsonl 4216c04673ced76b5b2ac60ef57c9abedc46f9b9 /var/lib/btc-recorder | head -n 1
/var/lib/btc-recorder/btc-updown-5m/1789488300/runtime.jsonl

$ du -sb /root/PROJECT_GAMING_PS5
403322657	/root/PROJECT_GAMING_PS5

$ systemctl is-enabled telemetry-watch.service; echo "exit=$?"
disabled
exit=1

$ systemctl is-active telemetry-watch.service; echo "exit=$?"
inactive
exit=3

$ test -e /root/tz17-work; echo "tz17-work exit=$?"
tz17-work exit=0

$ git worktree list
/root/btc-5m-twap          795f176 [main]
/root/tz15-work/wt         f7f171a [tz-15-phase2-gate]
/root/tz15-work/wt-report  c729008 (detached HEAD)
/root/tz17-work/wt         8f1bc93 [tz-17-settlement-chain]
/root/tz17-work/wt-report  c4f2099 (detached HEAD)
```

| condition | required | read | result |
|---|---|---|---|
| **H1** | `find` prints exactly one path | one path, `/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json` | **pass** |
| **H2** | `pgrep -fx` prints **exactly one line**, and its pid is the recorder's | one line, `228592`; `/proc/228592/cmdline` is `/root/tz04a-env/venv/bin/python -B -u recorder.py`, cwd `/root/btc-5m-twap/research/recorder` | **pass** |
| **H3** | `df` names source `/dev/vda2`, size `31612203008` | `/dev/vda2`, `31612203008` | **pass** |
| resource gate | `avail` ≥ `2,200,000,000` | `13,463,633,920` — `11,263,633,920` above the floor | **pass** |
| `test -e /root/tz17-work` | exit `0` | exit `0` | **pass** |

The line count of `pgrep -fx` was taken as its own count, `1`: this session's shell carries the
pattern as a substring and `-fx` cannot match it, which is the wording §0.2 fixed in place of
TZ-17's H2. `/root/tz17-work` is read-only input here and nothing in this session removed it
(§2 P5).

### 0.2b The same host reads at the end of the session

Taken after R6, `1,390` s after the opening reads, and printed beside them as §6 requires:

```
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 13453283328

$ find /var/lib/btc-recorder -mindepth 1 -maxdepth 3 -name manifest.json -print -quit
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json

$ pgrep -fx '/root/tz04a-env/venv/bin/python -B -u recorder.py'
228592
line count = 1

$ test -e /root/tz17-work; echo "tz17-work exit=$?"
tz17-work exit=0

$ git worktree list
/root/btc-5m-twap          795f176 [main]
/root/tz15-work/wt         f7f171a [tz-15-phase2-gate]
/root/tz15-work/wt-report  c729008 (detached HEAD)
/root/tz17-work/wt         8f1bc93 [tz-17-settlement-chain]
/root/tz17-work/wt-report  c4f2099 (detached HEAD)
/root/tz18-work/wt         8caa0b4 [tz-18-chainbook-capture]
/root/tz18-work/wt-report  795f176 (detached HEAD)
```

| read | open | close | change |
|---|---|---|---|
| H1, the one manifest path | `…/1789488300/manifest.json` | same | none |
| H2, the recorder | one line, pid `228592` | one line, pid `228592` | **none — the recorder was never signalled** |
| H3, source and size | `/dev/vda2`, `31612203008` | `/dev/vda2`, `31612203008` | none |
| `avail` | `13,463,633,920` | `13,453,283,328` | `−10,350,592` bytes, dominated by Tier C's own writes (§2.6) |
| `/root/tz17-work` | exists | exists | **none — nothing was reclaimed (§2 P5)** |
| worktrees | 5 | 7 | the two this TZ added, both kept |

### 0.3 The two repository reads

```
$ git show origin/main:CryptoReports/TZ-17-settlement-chain-report.md | sha256sum
0553061fb9f4793e0e73167042af0a770c5d640fae56f2fb1c7611b494c45815  -

$ git ls-tree -r --name-only origin/main | grep -c '^research/tz17-settlement-chain.py$'
1

$ git ls-tree -r --name-only origin/main | grep -c '^research/tz18-chainbook-capture.py$'
0
```

- The first is **printed, not asserted**, and it is equal to `0553061fb9f4…`, the copy the
  Architect audited — the committed file and the forwarded copy are the same bytes here. What is
  asserted is the CSV inside it: V3, below.
- `CryptoReports/TZ-17-settlement-chain-report.md` exists on `origin/main` (count `1`): TZ-17 has
  published, so this TZ may build on its stored bodies.
- The second count is `1`: **PR #17 is merged.** Either state was legal.
- The third count is `0`, as §0.3 requires: this TZ's own path did not already exist. It was
  created by this session on the branch only, never on `main` before the report.

### 0.4 Trees and interpreter

Two worktrees from `origin/main` at `795f1763b8db81d9ba810b18f214ec59c38bbe97`:
`/root/tz18-work/wt` on branch `tz-18-chainbook-capture`, and `/root/tz18-work/wt-report`
detached, from which this report is pushed by `git push origin HEAD:main`. Every run used
`/root/tz01-env/venv/bin/python` — Python 3.12, the research interpreter of the map's §6.
Neither `/root/tz01-env/` nor `/root/tz04a-env/` was touched; the recorder's interpreter was
never invoked and its process was never signalled (§2 P6).

---

## 1. Input

| input | what was read | size | hash |
|---|---|---|---|
| `SYSTEM-MAP.md` | the fingerprint gate, §0 | 826 lines, 156,425 bytes | `3a88c357…95e3e1a0` |
| `CryptoTZ/TZ-18-chainbook-capture-deploy.md` | this specification, in full | 551 lines, 37,259 bytes | read, not gated |
| `CryptoReports/TZ-17-settlement-chain-report.md` | the CSV of its §2.11, from the worktree | 135,731 bytes | `0553061f…94c45815` |
| the CSV inside it | between the first ` ```csv ` line and the next ` ``` ` | 201 lines, 99,075 bytes | `96b5e21e…1efc63ee` — **asserted** |
| `/root/tz17-work/raw/*.body` | 801 stored market documents, read-only | 801 files | each re-hashed to the CSV's value — **801 of 801** |
| `/var/lib/btc-recorder/**/manifest.json` | the Tier C interlock, manifests only | see §2.3 | opened under the reserved tree: manifests only, asserted |
| `/var/lib/btc-chainbook/**` | what the capture stored in this session | see §2.1 | written by this TZ |

**Nothing was re-collected.** The 801 bodies are TZ-17's, untouched and unmodified; this TZ read
them, hashed them against the committed CSV and closed them. `/root/tz17-work/` was not
reclaimed, not written and not removed (§2 P5).

The 22 frozen repository files were read for hashing only. No committed file was edited, no
function of any committed file was imported or called, and the instrument is standard-library
only (§2 P7, asserted by S8 over its own syntax tree).

---

## 2. Measurements
### 2.1 What the capture stored

The service was started at `2026-09-22T22:53:36Z`, `start_wall_ns = 1790117616052072857`, pid
`2608993`, from `/root/tz18-svc/tz18-chainbook-capture.py` whose SHA-256 `33753b2b…` was asserted
equal to the committed blob's before it was started. It is still running.

| window `T` | document instant | document statuses | `documents_ok` | checkpoints stored | complete | missed | stored bytes |
|---|---|---|---|---|---|---|---|
| `1790117100` | 1790117705 | 403, 403 | false | 7 | 0 | 0 | 1,408 |
| `1790118000` | 1790118605 | 403, 403 | false | 7 | 0 | 0 | 1,408 |

Both windows are **well formed**: `documents.jsonl` carries exactly 2 lines, `books.jsonl.gz`
exactly **28** lines each — 7 checkpoints × 2 markets × 2 outcomes — and `window.json` was written
at `T+905` with the key set V11 fixes. **0 checkpoints were missed**; the scheduler hit every one
of its fourteen instants. Each `books.jsonl.gz` is `301` bytes with the gzip `MTIME` field equal to
`0` and level `6`, so a window's file is a pure function of its lines, as §3.5 requires.

What every one of the 28 rows per window carries is `status: null`, `reason: "no_token_ids"`: the
document fetch returned 403 and no `clobTokenIds` could be taken, so §3.4's rule applied — the four
entries are written as the failures they are rather than guessed at.

`runtime.jsonl` holds **1** record, the `start` of §3.8; no `stop` record exists because no signal
was sent (§2 P6, §3.8).

### 2.2 G-DEPLOY — every checkpoint considered, in order (V9)

Fourteen checkpoints were considered and **all fourteen qualify**: each window's document instant
is ≥ `start_wall + 60` s (`1790117705` and `1790118605` against `1790117676`) and every scheduled
instant is ≤ `start_wall + 3,900` s = `1790121516`. No checkpoint was excluded, so the column of
exclusion reasons is empty; none was skipped for being already under way at the start.

| window `T` | `tau'` | instant | qualifying | four statuses | recv deltas (ns) | skew (ns) | complete / reason |
|---|---|---|---|---|---|---|---|
| 1790117100 | 245 | 1790117755 | yes | null, null, null, null | — | — | no — `status_not_200` |
| 1790117100 | 185 | 1790117815 | yes | null, null, null, null | — | — | no — `status_not_200` |
| 1790117100 | 125 | 1790117875 | yes | null, null, null, null | — | — | no — `status_not_200` |
| 1790117100 | 95 | 1790117905 | yes | null, null, null, null | — | — | no — `status_not_200` |
| 1790117100 | 65 | 1790117935 | yes | null, null, null, null | — | — | no — `status_not_200` |
| 1790117100 | 35 | 1790117965 | yes | null, null, null, null | — | — | no — `status_not_200` |
| 1790117100 | 15 | 1790117985 | yes | null, null, null, null | — | — | no — `status_not_200` |
| 1790118000 | 245 | 1790118655 | yes | null, null, null, null | — | — | no — `status_not_200` |
| 1790118000 | 185 | 1790118715 | yes | null, null, null, null | — | — | no — `status_not_200` |
| 1790118000 | 125 | 1790118775 | yes | null, null, null, null | — | — | no — `status_not_200` |
| 1790118000 | 95 | 1790118805 | yes | null, null, null, null | — | — | no — `status_not_200` |
| 1790118000 | 65 | 1790118835 | yes | null, null, null, null | — | — | no — `status_not_200` |
| 1790118000 | 35 | 1790118865 | yes | null, null, null, null | — | — | no — `status_not_200` |
| 1790118000 | 15 | 1790118885 | yes | null, null, null, null | — | — | no — `status_not_200` |

**Complete 0, incomplete 14, missed 0, of 14 qualifying.** The deltas and skews are `—` because no
reply arrived: a delta from the first reply and a spread over four replies are undefined on an
empty set, and the instrument records them as null rather than as `0`, which would have been a
number that did not happen.

### 2.3 The seven skews per window, in nanoseconds

**No skew was measurable in this run.** The statistic's population — every checkpoint that
produced four replies — is **empty**, so its minimum, median and maximum are undefined and are
reported as undefined rather than as zero:

| statistic | value | population |
|---|---|---|
| checkpoints with four replies | **0** | of 14 considered |
| minimum skew | undefined | — |
| median skew | undefined | — |
| maximum skew | undefined | — |

This is the number §8 item 5 calls "the number the next TZ will size its pairing rule from", and
**this run does not supply it.** The next deployment must produce it before any TZ sizes a pairing
rule; nothing here may be used as a stand-in.

### 2.4 G-TIERC — the two windows, interval by interval

Proof window `[1790117616, 1790119006]` = `22:53:36Z … 23:16:46Z`, length `1,390` s — from the
service's `start` record to the moment `--prove` ran. Control window `[1790116226, 1790117616]` =
`22:30:26Z … 22:53:36Z`, the same `1,390` s ending at the start record.

| window | interval `T0` | closes | `quotes_complete` | `complete` |
|---|---|---|---|---|
| proof | 1790117400 | 22:55:00Z | **true** | false |
| proof | 1790117700 | 23:00:00Z | **true** | true |
| proof | 1790118000 | 23:05:00Z | **true** | true |
| proof | 1790118300 | 23:10:00Z | **true** | true |
| proof | 1790118600 | 23:15:00Z | *no `manifest.json` yet* | — |
| control | 1790116200 | 22:35:00Z | true | true |
| control | 1790116500 | 22:40:00Z | true | true |
| control | 1790116800 | 22:45:00Z | true | true |
| control | 1790117100 | 22:50:00Z | true | true |

**Proof window: 4 intervals carry a `manifest.json`, 4 of 4 `quotes_complete` true, 0 false.**
Control window: 4 intervals, 4 of 4 true. The interval closing at `23:15:00Z` had not yet written
its manifest when the proof ran and is excluded by §3.6's own wording — "whose `manifest.json`
exists" — and disclosed here rather than counted either way.

`complete` is `false` for the interval closing `22:55:00Z` and true for the rest; the gate is on
`quotes_complete` alone, and `complete` is printed beside it because §8 item 6 asks for both. That
`false` sits in an interval that opened at `22:49:00Z`, four and a half minutes **before** this
session started anything, so it cannot be an effect of this capture.

Only `manifest.json` was ever opened under `/var/lib/btc-recorder/`: **8 opens, every basename
`manifest.json`**, asserted per open by the guard (V6). The recorder was never signalled, never
stopped and never touched, and `pgrep -fx` returns the same single pid `228592` at the end of the
session as at the start.

### 2.5 Request accounting

| source | attempts | statuses | retries |
|---|---|---|---|
| the instrument, documents | 2 per window | all `403` | `0` by construction — §3.4 forbids a retry inside a checkpoint and the instrument has no retry path at all |
| the instrument, books | `0` | — | — |
| Executor diagnostics, §6.1 | 9 | 4 × `403`, 4 × `200`, 1 × `404` | `0` |

No book read was ever issued: a 403 on the document yields no `clobTokenIds`, and §3.4 then
writes the four entries with `status: null` and `reason: "no_token_ids"` rather than guessing an
id. The venue therefore saw 2 requests per 900 s from the instrument, not the 30 of §3.9.

No order was placed, no authentication was offered, no credential, CLOB key or wallet was read or
held, and exactly two endpoints were contacted — asserted over the instrument's own syntax tree
by S8, which finds exactly two string constants carrying a scheme separator and requires them to
be §3.2's two.

### 2.6 Bytes, the write cap and the `df` delta

| quantity | figure |
|---|---|
| R1 bytes written | 233,549 |
| R4 bytes written | 11,211 |
| R6 bytes written | 233,549 |
| pre-commit debug run (§6.3 item 5) | 233,549 |
| the service, to the end of the session | 6,095 on disk under `/var/lib/btc-chainbook/` |
| `/root/tz18-svc/` | 57,450 |
| `/root/tz18-work/` outputs, excluding the two worktrees | 757,959 |
| **session total written by this TZ** | **821,504** |
| **write cap, asserted inside every run as it writes** | **200,000,000** — the session used `0.41%` of it |

`df` on `/var/lib/btc-recorder`, opening and closing:

```
open   /dev/vda2  31612203008  13463633920
close  /dev/vda2  31612203008  13453283328
delta                          -10,350,592 bytes over 1,390 s
```

The `10,350,592`-byte fall is dominated by Tier C's own five-minute intervals closing during the
session, not by this TZ: everything this TZ wrote anywhere on the host is `821,504` bytes, and
`6,095` of that is under `/var/lib/btc-chainbook/`. Closing `avail` is `11,253,283,328` bytes above
the map's `2,000,000,000` floor. The resource gate was re-asserted inside the instrument through
`os.statvfs` at R1, R4, R6 and at every window the service opened.

### 2.7 The service, at the end of the session (V12)

| item | value |
|---|---|
| pid | `2608993`, alive |
| `/proc/2608993/cmdline` | `/root/tz01-env/venv/bin/python -B -u /root/tz18-svc/tz18-chainbook-capture.py --serve` |
| §3.8's argv | `/root/tz01-env/venv/bin/python -B -u /root/tz18-svc/tz18-chainbook-capture.py --serve` — **equal** |
| `start` record commit | `8caa0b41d5cdf9e74e92b11d4317d59a2ee7b567`, the branch head |
| `start` record `file_sha256` | `33753b2bb1e322a081e6cba8bad976268e2d6046dc350e6ceae3e748ad6e4bfe` |
| the committed blob's SHA-256 | `33753b2bb1e322a081e6cba8bad976268e2d6046dc350e6ceae3e748ad6e4bfe` — **equal**, asserted before the start |
| `service.pid` | `2608993`, created with `O_CREAT | O_EXCL` |
| records in `runtime.jsonl` | `1` — one `start`, no `stop`: no signal was sent |

**The service is still running and is still issuing refused requests.** §6.2 states why it was left
running and what it costs.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-18-chainbook-capture` |
| implementation commit | `8caa0b41d5cdf9e74e92b11d4317d59a2ee7b567` |
| file added | `research/tz18-chainbook-capture.py`, 1,420 lines, 57,409 bytes, SHA-256 `33753b2bb1e322a081e6cba8bad976268e2d6046dc350e6ceae3e748ad6e4bfe` |
| pull request | [#18](https://github.com/seahomebatumi-ai/btc-5m-twap/pull/18), **unmerged** |
| report | `CryptoReports/TZ-18-chainbook-capture-deploy-report.md`, pushed straight to `main` from `/root/tz18-work/wt-report` |
| Release asset | none — this TZ produces no dataset for git or for a Release |

No dataset, archive or binary enters git history: the capture lives in `/var/lib/btc-chainbook/`
and nothing of it is committed, ever (§9 of the TZ).

### 3.1 The mandatory separation self-check, verbatim (V14, V15)

```
$ git diff --name-only origin/main origin/tz-18-chainbook-capture
research/tz18-chainbook-capture.py

$ git rev-list origin/main | grep -c 8caa0b41d5cdf9e74e92b11d4317d59a2ee7b567     # must print 0
0

$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'  # must print nothing
(no output)

$ git log --oneline -1 origin/tz-18-chainbook-capture
8caa0b4 TZ-18: the chain book capture, deployed
$ git log --oneline -1 origin/main
795f176 Add files via upload
```

The branch differs from `main` by exactly one path, `main` did not carry the implementation
commit when this was run, and no `.parquet` or `.zip` is in git history. Run after the branch
push and before the report commit, as V14 and V15 require.

---

## 4. Gate

Three readings. None gates another, and no row of §4 moved after a number was known.

### G-DEPLOY — does the capture record both books at one instant?

> **Unit:** a checkpoint. **Qualifying:** its window's document instant `T + 605` is ≥
> `start_wall + 60` s **and** its own scheduled instant is ≤ `start_wall + 3,900` s.
> **Complete:** four stored replies, all HTTP 200, each body non-empty and parsing as JSON, and a
> skew ≤ `1,000,000,000` ns.
> **Reading:** of the **first 14 qualifying checkpoints**, **≥ 13 complete → PASS**; **≤ 12 →
> FAIL**; fewer than 14 qualifying by the budget end → UNDECIDABLE.

Qualifying checkpoints: **14**. Complete: **0.000** of 14. Deciding number **0 ≤ 12**.

**Reading: FAIL.**

The gate is read exactly as written and is not reinterpreted. What produced the number is stated
without softening it: all 28 book reads of the two qualifying windows carry
`status: null, reason: "no_token_ids"`, because both document fetches of both windows returned
HTTP 403 and no `clobTokenIds` could be taken. The cause is one omission in this Executor's
build — no request headers — proven by measurement in §6.1, where the same endpoints answer 200
from this host with TZ-17's two headers, for a live window's document and for both of its books.

**A FAIL here is a statement about the artifact that ran, not about the capture design and not
about the venue.** Nothing about any price, book or edge is claimed or implied by it.

False-failure probability under a capture that loses nothing: `0`. Family-wise over one statistic
on one set: `0`. The power table of §4 stands as written and was verified to `1E-18` in exact
`Fraction` arithmetic by S7 (`p = 0.25 → 0.899031627923250198364257812500`,
`p = 0.10 → 0.415370859484330000000000000000`,
`p = 0.05 → 0.152985562588816560668945312500`); it is not used to interpret this reading, because
the failure rate observed here is `1`, not a small `p`.

### G-TIERC — did the new capture disturb the old one?

> Every 5-minute interval of `/var/lib/btc-recorder/` whose `T0 + 300` lies inside the proof
> window and whose `manifest.json` exists must carry `quotes_complete` true. One false → FAIL.

Intervals in the proof window carrying a `manifest.json`: **4**. With `quotes_complete` true:
**4.000 of 4**. False: **0**.

**Reading: PASS.** R5 therefore did not run: the service was not stopped, and no block of §6 R5
was executed or quoted as executed.

The control window of equal length ending at the start record reads **4 of 4** as well, printed
beside it and not gated. Interval by interval, both windows are in §2.4.

False-failure under "the new capture does not disturb the old one": `0`. **No power is claimed:
this is an interlock, not a measurement**, and with 4 units in the proof window it could only have
detected a disturbance that struck one of four intervals — a small window, disclosed as such. The
recorder's pid is unchanged across the session and only `manifest.json` was ever opened under its
tree.

### G-CHAIN — is the settlement reading the same published number for both families?

> **Reading:** `Q1 ≥ 599` of `600` **and** `Q2 ≥ 199` of `200` **and** `Q3 ≥ 199` of `200` →
> **PASS**. Any identity at or below `n − 2` → **FAIL**.

| identity | units | equal by exact `Decimal` value | equal as a printed literal | `type_error` | threshold |
|---|---|---|---|---|---|
| **Q1** — `finalPrice` of the 5-minute market at slot `i` equals `priceToBeat` at slot `i+1` | 600 | **600.000 of 600** | 600 of 600 | 0 | ≥ 599 |
| **Q2** — `finalPrice` of `btc-updown-15m-{T}` equals `priceToBeat` of `btc-updown-5m-{T+900}` | 200 | **200.000 of 200** | 200 of 200 | 0 | ≥ 199 |
| **Q3** — `finalPrice` of `btc-updown-15m-{T}` equals `finalPrice` of `btc-updown-5m-{T+600}` | 200 | **200.000 of 200** | 200 of 200 | 0 | ≥ 199 |

**Reading: PASS.** 1,000 of 1,000 units hold, and **zero mismatches** were found, so the list of
mismatches with their differences that §8 item 7 asks for is empty — stated as a count, not as
"all checks passed".

Every unit holds not only by value but as the same printed literal, which is the stronger of the
two columns §3.7 asks for: the two families do not merely agree to within a rounding, they carry
the same decimal string.

**What this PASS means, quoted from §4 and not extended:** the 15-minute market and the 5-minute
market inside it are settled from the same published number, exactly, so the nesting of their
outcomes is exact rather than approximate, and a later TZ may treat the constraint as model-free.
**What it does not mean:** nothing about any price, any book, any edge.

It also closes, directly, the gap TZ-17's audit found: TZ-17 inferred each market's settlement
reading from the *next* market's price to beat, and this reads the venue's own `finalPrice`
against it, on the same 801 bodies, offline. Both readings agree at 1,000 of 1,000.

False-failure under "each boundary has one published reading": `0`. Family-wise over three
identities on one set of documents: `0`. Power, verified to `1E-18` by S7: Q1 at `p = 0.02`
`0.999927940037418865985964653194`, at `p = 0.005` `0.801599779568236533442873619078`; Q2 and Q3
at `p = 0.02` `0.910624516228067965960219332490`, at `p = 0.01`
`0.595354315327973499366704428681`.

---

## 5. Validation

| # | row | count | asserted? | runs it held on |
|---|---|---|---|---|
| **V1** | fingerprint gate inside the instrument | revision equal; anchors **6 of 6**; file anchors re-derived **4 of 4**; rows hashed **24 of 24**; frozen equal **22 of 22** | asserted — each row aborts the run | R1, R4, R6 |
| **V2** | host and resource gates | H1, H2, H3 printed verbatim in §0.2 and compared by the Executor; `avail` asserted `≥ 2,200,000,000` inside the instrument at each run through `os.statvfs` | H1–H3 **compared by the Executor, not asserted in code**; the resource floor **asserted** | §0, R1, R4, R6 |
| **V3** | the CSV extracted from the committed TZ-17 report | sha256 `96b5e21e…`, **99,075** bytes, **201** lines | asserted, three separate asserts | R1, R6 |
| **V4** | stored bodies re-hash to the CSV's value | **801 of 801** | asserted per body | R1, R6 |
| **V5** | the write guard | checks performed: R1 **2**, R4 **1**, R6 **2**; service **12 (2 documents, 2 book files, 2 window files, 1 runtime record, 1 pid file over two windows and the start)** | asserted before every open for writing | all |
| **V6** | the open guard under the reserved tree | R1 **0**, R6 **0**; R4 ****8****, every basename `manifest.json` | asserted per open | R4 / R1, R6 |
| **V7** | R1 and R6 open no socket | request counter at exit **0** in both | asserted | R1, R6 |
| **V8** | determinism | `tz18-verify.csv` and `tz18-verify.json` byte-identical between R1 and R6, `cmp` clean, two fresh processes from the same commit | asserted by `cmp` exit `0` | R6 |
| **V9** | every checkpoint the proof considered, disclosed in order | **14** checkpoints, qualifying and non-qualifying alike, with the reason, the four statuses and the skew | disclosure, printed in §2.2 | R4 |
| **V10** | the four reads of a checkpoint are issued concurrently | checkpoints with four issued sends: **0** — no book read was ever issued, because no document yielded token ids; violations **0** | asserted (`violations == 0`), on an **empty population** | R4 |
| **V11** | no price leaves the store | key sets of `window.json`, `tz18-proof.json` and `tz18-verify.json` are fixed allow-lists in the source, checked before each write, plus a recursive refusal of any forbidden key | asserted | all |
| **V12** | the service's `start` record and `/proc` | start record carries commit `8caa0b41…` and file SHA-256 `33753b2b…`; `/proc/2608993/cmdline` equals §3.8's argv, at R2 and at the session end | compared by the Executor and printed | R2, session end |
| **V13** | the write cap | bytes written: R1 **233,549**; R4 **11,211**; R6 **233,549**; service **6,095 on disk**; session total **821,504** of cap **200,000,000** | asserted as it writes | all |
| **V14** | the branch diff names exactly one path | **1** path, `research/tz18-chainbook-capture.py` | printed verbatim in §3.1 | after push |
| **V15** | the mandatory separation self-check | `main` does not carry the implementation commit (**0**); one path differs; no `.parquet` or `.zip` | printed verbatim in §3.1 | after push |

**V10 is a check on an empty population and therefore cannot have failed in this run.** It is
reported as what it is. The concurrency of the four reads is implemented — four threads are
created and started, and each waits on one `threading.Event` before it opens a socket — but the
build never reached a book read, so the property was never exercised against live timings. The
next deployment must read V10 for the first time.

---

## 6. What could not be implemented as written

### 6.1 The deployed instrument sent no request headers, and every read was refused

This is the finding of the run, and it is the Executor's defect, not the TZ's.

`research/tz18-chainbook-capture.py` builds its request as
`urllib.request.Request(url, method="GET")` with no headers, so it goes out with urllib's
default agent. Both of the venue's hosts sit behind an edge filter that refuses that agent:

```
HTTP 403, body: 'error code: 1010\n'   (17 bytes)
```

Cloudflare's `1010` is a browser-integrity refusal. The TZ names two public, unauthenticated GET
endpoints and says nothing about headers; TZ-17 — the artifact this TZ quotes as evidence that
the 15-minute slug is served — sets two, at line 30 and line 593 of `research/tz17-settlement-chain.py`:

```python
USER_AGENT = "btc-5m-twap-tz17"
...
headers={"Accept": "application/json", "User-Agent": USER_AGENT},
```

I did not carry them over. That single omission is the whole of the failure.

**Measured, not inferred.** Four diagnostic requests, issued by the Executor from this host
during the run, against the same two endpoints named in §3.2, printing status and byte count and
never a body:

| request | headers | result |
|---|---|---|
| document, settled 15-minute slug | none | **403**, 17 bytes, `error code: 1010` |
| document, same slug | TZ-17's two | **200**, 5,462 bytes |
| book, token of a settled market | none | **403**, 17 bytes |
| book, token of a settled market | TZ-17's two | **404**, `{"error":"No orderbook exists for the requested token id"}` — the expected reply for a resolved market, not a refusal |

and four more against the **live** window `1790117100`, at `t = 860` s into it — inside exactly
the span this capture reads:

| request | headers | result |
|---|---|---|
| live 15-minute document | none | **403**, 17 bytes |
| live 15-minute document | TZ-17's two | **200**, 5,269 bytes, two distinct `clobTokenIds` |
| live 15-minute book, first token | TZ-17's two | **200**, 3,252 bytes |
| live 15-minute book, second token | TZ-17's two | **200**, 3,252 bytes |

So: the venue serves this host, the 15-minute market's book exists and is served mid-window, and
the capture's design works. Nine requests in total were issued outside the instrument in this
session — one of the eight above was issued twice across two probe scripts — and they are
counted in §2.5's request accounting. No body from any of them was printed, stored or parsed for
a price.

**The one-line correction** the next build needs, and nothing else:

```python
req = urllib.request.Request(url, method="GET",
                             headers={"Accept": "application/json",
                                      "User-Agent": "btc-5m-twap-tz18"})
```

### 6.2 Why the corrected build was not deployed in this session

It could not be, without breaking a written prohibition.

- **§2 P6** — "no process is signalled."
- **§3.8** — "**This TZ sends it no signal.**"
- **§6 R5** — the one authorized stop is conditioned on **G-TIERC reading FAIL**, and G-TIERC
  reads **PASS**.

The service holds `/var/lib/btc-chainbook/service.pid` and refuses a second instance by design
(§3.8), so a corrected build could not be started beside it either, and starting one would have
doubled the venue load and interleaved two writers into one window directory. Replacing the
deployed build therefore requires a signal that this TZ does not authorize under the condition
that actually occurred.

Per `BTC-EXECUTOR-INSTRUCTIONS.md` §2, an authorization that did not arrive inside a committed TZ
did not arrive. **I left the service running and report the gate as it reads.**

**What that costs while it stands.** The instrument issues two document GETs per 900-second
window and — because a 403 yields no token ids — **no book reads at all**: `2` requests per
window, `192` per day, `0.0022` req/s, against the `30` per window and `2,880` per day the TZ
sized. Each window stores `1,408` bytes (28 book rows carrying `status: null`,
`reason: "no_token_ids"`, two 17-byte document bodies and a `window.json`), about `0.14` MB/day
against the `3.0` MB/day of §3.9. It is a small, bounded, harmless cost, and it does not touch
Tier C — which G-TIERC measured directly, below.

**The recommended next TZ** is short: authorize the stop of pid `2608993` with the block it
quotes, take the two headers above, and re-run this TZ's R2 through R4 unchanged. Every other
part of this instrument was exercised and held: the schedule, the window lifecycle, the verbatim
store, the gzip determinism, the guards, the disclosure and all 33 self-tests.

### 6.3 Readings applied where the TZ left a choice

1. **The branch commit in the `start` record (V12) against §3.8's fixed argv.** §3.8 fixes the
   service's argv exactly and leaves it no flag for a commit, while V12 requires the `start`
   record to carry the branch commit. The instrument reads it from `commit.txt` beside its own
   copy in `/root/tz18-svc/` and records what it read. `/proc/2608993/cmdline` is byte-equal to
   §3.8's argv, and the record carries commit `8caa0b41…` and file SHA-256 `33753b2b…`.
2. **Where §3.7's two output files are written.** §3.7 names `/root/tz18-work/tz18-verify.csv`;
   §6 sends R1 to `/root/tz18-work/run-1/` and R6 to `/root/tz18-work/run-3/`. The instrument
   takes the directory from the run and keeps the filenames §3.7 fixed, so both readings hold and
   V8's `cmp` compares two files of the same name from two different runs.
3. **V10's assert and its printed count.** §7 asks V10 both to assert per checkpoint and to print
   the count of checkpoints where the property does not hold. The instrument collects the
   violations, prints the count, writes every output file, and asserts the count is `0` at the
   very end of `--prove`, so a violation would be fully disclosed before it aborted.
4. **Windows already under way when the service starts.** §4 says such a window "contributes no
   unit … every such checkpoint is still disclosed with that reason", while §3.5's schemas give a
   missed document fetch no representation. The instrument begins at the first window whose
   document instant has not yet passed, so every stored window is well-formed; the window
   partially elapsed at start is named here instead: the service started at `22:53:36Z` inside
   window `1790117100`, whose document instant `1790117705` had **not** passed, so that window
   was captured in full and qualified. No window was skipped in this session.
5. **A pre-commit debug run of `--verify-tz17`** was made at `22:52:52Z` into
   `/root/tz18-work/predebug/`, before the branch commit, to find defects before publishing. It
   produced the same two files, byte-identical to R1's. It is not R1, R6 or any run of §6, it is
   disclosed here, and nothing was removed (§2 P5).

Nothing else in the TZ was unimplementable. No gate threshold, definition, population or formula
was changed, and no gate was reinterpreted.
