# TZ-03 — Repository hygiene — report

**Specification:** `CryptoTZ/TZ-03-repo-hygiene.md`
**Branch:** `tz-03-repo-hygiene` · **Commit:** `d9e58e8febd8548221598eed137cf40d31496047`
**Pull request:** [#1](https://github.com/seahomebatumi-ai/btc-5m-twap/pull/1) — **OPEN, not merged**
**Model:** Opus 5 — the model the TZ names. **Result: executed as written.**

No measurement. No gate. Three operations, and no byte of any file's content changed.

---

## 0. Fingerprint

Read from `SYSTEM-MAP.md` §0 on `main` at `76d4d9f` before any work.

| item | required by TZ | read from map | verdict |
|---|---|---|---|
| revision string | `2026-09-10-b` | `2026-09-10-b` | match |
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | match |
| `A2` — collector | `6c5089330629` | `6c5089330629` | match |
| `A3` — phase | `1-complete / 2-not-started` | `1-complete / 2-not-started` | match |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | match |

`A2` and `A4` were additionally recomputed from disk, not read from the table: `A2` =
`6c50893306292c74…` from `research/twap-divergence.py`, `A4` = `437b45ea196b9f01…` from the
contract. `A3` was read from map §5 rows 1 and 2. `A1` is the SHA-256 of the published Release
asset as recorded in map §2.1; this TZ reads no data and re-collected nothing, so the asset was
not re-downloaded.

**Gate verdict: PASS.** Work proceeded.

### Fingerprint table

Per TZ §Fingerprint gate, the §0 *file* table was **not** verified before starting: that table is
the object of this TZ and the contract row's path is wrong on disk by design until §2 has run.
Values below are computed on branch `tz-03-repo-hygiene` at `d9e58e8`, after §2.

| path | lines | bytes | state | SHA-256 | vs map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 222 | 12,716 | reported | `a2323219474d11dc7670964d098be79a27f8d6ac13f4364a3b1ccf52621a40c1` | self-reference |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | match |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | match |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | match |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | match |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | match |

All three `frozen` rows match the hash printed in the map. Line and byte counts match the map's
declared values on every row that declares them.

The contract row is the one the map flags as "not yet true on disk". Verified by content hash
under its defective path before §2, as map §0 directs:

```
$ git show "main:BTC-EXECUTOR-INSTRUCTIONS .md" | sha256sum
437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b
```

Same hash before the rename and after it — the rename changed the path and nothing else.

---

## 1. Input

Nothing was read as data and nothing was re-collected. This TZ has no dataset input: it does not
open the observation set, does not call `data.binance.vision`, and runs no Python.

Files read for governance only, both on `main` at `76d4d9f`: `CryptoTZ/TZ-03-repo-hygiene.md`
(112 lines) and `SYSTEM-MAP.md` (222 lines, `a2323219…a40c1`), plus the Executor contract
(234 lines, `437b45ea…6fb3b`).

The three paths operated on, as they stood on `main` before §2:

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `BTC-EXECUTOR-INSTRUCTIONS .md` | 234 | 11,128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` |
| `research/EXECUTOR-INSTRUCTIONS .md` | 234 | 11,128 | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` |
| `research/SYSTEM-MAP.md` | 213 | 11,640 | `f2a09deb8118123c79a17cad7a8bc1ae996c5dc70388130c84ed5e2641e4dc84` |

`research/EXECUTOR-INSTRUCTIONS .md` was byte-identical to the root contract, confirmed by `cmp`.
`research/SYSTEM-MAP.md` was **not** byte-identical to the root map — see §6 item 1.

---

## 2. Measurements

**None.** This TZ produces no number. It moves and deletes files. The TZ states this in its
header and no measurement was performed, invented or implied.

The three operations, exactly as run, in this order, on branch `tz-03-repo-hygiene`:

```
$ git mv "BTC-EXECUTOR-INSTRUCTIONS .md" "BTC-EXECUTOR-INSTRUCTIONS.md"
$ git rm "research/EXECUTOR-INSTRUCTIONS .md"
rm 'research/EXECUTOR-INSTRUCTIONS .md'
$ git rm "research/SYSTEM-MAP.md"
rm 'research/SYSTEM-MAP.md'
```

Every path quoted. `git mv` / `git rm` throughout; no `rm` followed by `git add` anywhere. Blob
identity is preserved and the rename is visible as a rename:

```
$ git diff --name-status -M main...HEAD
R100    BTC-EXECUTOR-INSTRUCTIONS .md   BTC-EXECUTOR-INSTRUCTIONS.md
D       research/EXECUTOR-INSTRUCTIONS .md
D       research/SYSTEM-MAP.md

$ git rev-parse "main:BTC-EXECUTOR-INSTRUCTIONS .md"
229011dfb6e958b01447d9097837a6e45fa14e82
$ git rev-parse "HEAD:BTC-EXECUTOR-INSTRUCTIONS.md"
229011dfb6e958b01447d9097837a6e45fa14e82
```

`R100` — 100% similarity. The blob SHA is the same object on both sides of the rename.

Staged set immediately before the commit — exactly three entries, nothing else:

```
$ git status --short
R  "BTC-EXECUTOR-INSTRUCTIONS .md" -> BTC-EXECUTOR-INSTRUCTIONS.md
D  "research/EXECUTOR-INSTRUCTIONS .md"
D  research/SYSTEM-MAP.md
?? research/__pycache__/
```

`research/__pycache__/` is untracked build residue that was already present in the working tree
at session start. It was **not** committed, and `.gitignore` was **not** edited — TZ §3 forbids
both touching `.gitignore` and acting on anything not named in §2.

---

## 3. Publication

| field | value |
|---|---|
| branch | `tz-03-repo-hygiene` |
| commit | `d9e58e8febd8548221598eed137cf40d31496047` |
| pushed to | `origin/tz-03-repo-hygiene` |
| pull request | [#1](https://github.com/seahomebatumi-ai/btc-5m-twap/pull/1), base `main`, head `tz-03-repo-hygiene` |
| PR state | `OPEN` · `mergedAt: null` · not a draft |
| Release tag / asset | none — this TZ produces no artifact |
| commit stat | `3 files changed, 447 deletions(-)` |

The pull request is **not merged**. Merge is the Boss's, after the Architect's verdict.

### §4.2 separation self-check, verbatim

```
$ git rev-list origin/main | grep -c d9e58e8
0

$ git diff --name-only origin/main origin/tz-03-repo-hygiene
BTC-EXECUTOR-INSTRUCTIONS.md
research/EXECUTOR-INSTRUCTIONS .md
research/SYSTEM-MAP.md

$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
(prints nothing)
```

First line is `0` — the implementation commit is **not** on `main`. Second line is implementation
paths only. Third prints nothing. Run against `origin/main` at `76d4d9f`, before this report was
committed; the report commit adds only `CryptoReports/TZ-03-repo-hygiene-report.md` and does not
change any of the three results.

---

## 4. Gate

**No gate.** The TZ states "No measurement. No gate. This TZ produces no number." There is no
deciding number, so none is quoted and none is reported to three decimals. Nothing was tuned and
no gate was reinterpreted, because there is no gate to reinterpret.

---

## 5. Validation

TZ §4, run on the branch after §2. Command and real output for each. Counts reported as counts.

### 4.1 — map hash

```
$ sha256sum SYSTEM-MAP.md
a2323219474d11dc7670964d098be79a27f8d6ac13f4364a3b1ccf52621a40c1  SYSTEM-MAP.md
```
Expected `a2323219474d11dc7670964d098be79a27f8d6ac13f4364a3b1ccf52621a40c1`. **Match** —
revision `2026-09-10-b` landed intact.

### 4.2 — contract hash unchanged by the rename

```
$ sha256sum BTC-EXECUTOR-INSTRUCTIONS.md
437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b  BTC-EXECUTOR-INSTRUCTIONS.md
```
Expected `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b`. **Match** — equal to
the pre-rename hash of `BTC-EXECUTOR-INSTRUCTIONS .md` reported in §1.

### 4.3 — no tracked path contains a space

```
$ git ls-files | grep -c " "
0
```
Expected `0`. **Match.** Count was `2` before §2 (`BTC-EXECUTOR-INSTRUCTIONS .md` and
`research/EXECUTOR-INSTRUCTIONS .md`); it is `0` after. 2 → 0.

### 4.4 — exactly one SYSTEM-MAP

```
$ git ls-files | grep -c "SYSTEM-MAP"
1
```
Expected `1`. **Match.** Was `2`. 2 → 1.

### 4.5 — exactly one EXECUTOR-INSTRUCTIONS

```
$ git ls-files | grep -c "EXECUTOR-INSTRUCTIONS"
1
```
Expected `1`. **Match.** Was `2`. 2 → 1.

### 4.6 — research/ holds measurement code only

```
$ git ls-files research/
research/selftest-twap-divergence.py
research/twap-divergence.py
research/tz02-distribution.py
```
Expected exactly those three. **Match** — 3 of 3 present, 0 extra. Was 5 entries; the two
governance files are gone. 5 → 3.

### 4.7 — diffstat is structural only

```
$ git diff --stat main...HEAD
 ...NSTRUCTIONS .md => BTC-EXECUTOR-INSTRUCTIONS.md |   0
 research/EXECUTOR-INSTRUCTIONS .md                 | 234 ---------------------
 research/SYSTEM-MAP.md                             | 213 -------------------
 3 files changed, 447 deletions(-)
```

Expected "one rename and two deletions; 0 insertions, 0 deletions of content lines". One rename,
two deletions, **0 insertions** — as required. The `447 deletions(-)` are the two whole-file
removals and nothing else (234 + 213 = 447); a `git rm` of a 234-line file necessarily reports
its lines in the diffstat, so the two clauses of this expectation cannot both hold under a
literal reading of the total. The structural reading — no line-level change to any retained
file — is what holds, and it is verified directly rather than inferred. See §6 item 2.

```
$ git diff --numstat main...HEAD
0       0       BTC-EXECUTOR-INSTRUCTIONS .md => BTC-EXECUTOR-INSTRUCTIONS.md
0       234     research/EXECUTOR-INSTRUCTIONS .md
0       213     research/SYSTEM-MAP.md

$ git diff --stat --diff-filter=M main...HEAD
(prints nothing — 0 files modified)

$ git diff --stat --diff-filter=A main...HEAD
(prints nothing — 0 files added)
```

The rename row is `0` added / `0` deleted. Files modified: **0**. Files added: **0**. Insertions
across the whole diff: **0**. Line-level deletions inside any file that survives to `HEAD`: **0**.

### 4.8 — research/*.py hashes unchanged

```
$ sha256sum research/selftest-twap-divergence.py research/twap-divergence.py research/tz02-distribution.py
ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a  research/selftest-twap-divergence.py
6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473  research/twap-divergence.py
f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4  research/tz02-distribution.py
```

Against the map §0 fingerprint table: `ed22e52f…a094a` match, `6c508933…1d473` match,
`f2ecd5c9…94bc4` match. **3 of 3 match, 0 differ.**

### 4.9 — no dataset or archive in the tree

```
$ git ls-tree -r --name-only HEAD | grep -E "\.parquet|\.zip"
(prints nothing)
```
Expected nothing. **Match** — 0 matching paths.

### Summary

**9 of 9 checks meet their expectation; 0 fail.** 4.7 meets it under the structural reading
recorded above and in §6 item 2.

**Asserted, or recorded?** These nine are **recorded, not asserted.** They are shell commands run
by hand and compared by eye against the TZ's expectation column; there is no script that aborts on
a false condition, because this TZ produces no script and contract §6 forbids writing one it did
not ask for. Contract §7 requires that distinction be stated in plain words, and it is stated here.
Each check is nonetheless falsifiable and independently re-runnable from the branch: every command
and its full output is printed above.

---

## 6. What could not be implemented as written

**Every operation in TZ §2 was implemented exactly as written. Nothing was omitted, substituted,
deferred or worked around.** Two findings about the TZ's own premises are recorded below because
a report is evidence, not acceptance; neither changed what was done.

**1. TZ §0 says the duplicates are byte-identical. For one of the two, that is not true.**

`research/SYSTEM-MAP.md` was not a copy of the current map. It was the **prior revision
`2026-09-10-a`** — 213 lines against the root map's 222, differing on 25 lines:

```
$ diff SYSTEM-MAP.md research/SYSTEM-MAP.md | grep -c '^[<>]'
25
$ sed -n '3p' SYSTEM-MAP.md
**Revision 2026-09-10-b.** Written by the Architect; the Executor never edits it. This is a
$ sed -n '3p' research/SYSTEM-MAP.md
**Revision 2026-09-10-a.** Written by the Architect; the Executor never edits it. This is a
```

The `-a` copy still called the contract `EXECUTOR-INSTRUCTIONS.md` throughout, recorded `main` at
`356c29a`, and lacked the §0 "one row below is not yet true on disk" paragraph, the
Architect's-mirror paragraph, and §7 defect 4 (it carried defects 1–3 only).

This does not make TZ §2 unsatisfiable, so it is not a BLOCKED condition: the operation names an
exact path and an exact verb, both unambiguous. It strengthens the stated rationale rather than
weakening it — a stale second map is a worse second source of truth than an identical one. The
blob is preserved in git history at `76d4d9f` and is recoverable with
`git show 76d4d9f:research/SYSTEM-MAP.md`; deletion loses nothing.

Raised because map §7 defect 4 and TZ §0 both assert byte-identity as fact, and the Architect may
want the wording corrected when defect 4 is closed. `research/EXECUTOR-INSTRUCTIONS .md` *was*
byte-identical, confirmed by `cmp`; the claim is wrong only for the map.

**2. TZ §4.7's expectation is self-contradictory under a literal reading.**

"one rename and two deletions; 0 insertions, 0 deletions of content lines" — two `git rm`s of a
234-line and a 213-line file report 447 deleted lines in `git diff --stat`. No diff can show both
"two deletions" and a zero deletion total. Rather than pick a reading silently, §5 4.7 prints the
raw `--stat`, then verifies the structural claim directly with `--numstat` and
`--diff-filter=M/A`: 0 files modified, 0 files added, 0 insertions, and 0 line-level deletions in
any surviving file. Contract §6 forbids editing a check to make it pass and forbids replacing one
with an equivalent, so 4.7 was run exactly as written and its output printed exactly as produced;
the extra commands are evidence added alongside it, not a substitution for it.

**3. Nothing else.** No file outside TZ §2 was created, deleted, renamed or modified. No content
byte changed anywhere in the repository. No history was rewritten, no commit amended, no force
push, no branch or tag deleted. The pull request is open and unmerged. `.gitignore` is untouched.
`/root/tz01-out-archive/` was not read.
