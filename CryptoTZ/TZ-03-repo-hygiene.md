# TZ-03 — Repository hygiene

**Canonical filename: `TZ-03-repo-hygiene.md`** — commit under this name in `CryptoTZ/`.

**Repository:** `btc-5m-twap`. **Model: Opus** — this TZ deletes tracked files and one of the
paths contains a space; a mis-quoted path deletes the wrong file. CANON routes data loss to
Opus regardless of how short the task is.

**No measurement. No gate.** This TZ produces no number. It moves and deletes files and
changes no byte of any file's content.

## Fingerprint gate

Required System Map revision string: **`2026-09-10-b`**. Required anchors:

| anchor | value |
|---|---|
| `A1` | `229a944f2d51` |
| `A2` | `6c5089330629` |
| `A3` | `1-complete / 2-not-started` |
| `A4` | `437b45ea196b` |

Verify the revision string and the four anchors **before** starting. **Do not verify the §0
file table before starting** — that table is the object of this TZ, and the contract row's
path is wrong on disk by design until §2 has run. A path mismatch on that row before the
repair is expected and is **not** a BLOCKED condition. Everything else in the fingerprint
gate applies as written in `BTC-EXECUTOR-INSTRUCTIONS.md` §1.

---

## 0. Why this exists

Both governance files were uploaded with defects that the Executor contract and the System
Map now depend on:

1. The contract is committed as `BTC-EXECUTOR-INSTRUCTIONS .md` — a space before the
   extension. CANON hard rule 1 is hyphens only, never spaces, in every deliverable filename.
2. Both files were also copied into `research/` as `research/EXECUTOR-INSTRUCTIONS .md` and
   `research/SYSTEM-MAP.md`. Two copies of the map are two sources of truth, which is the one
   thing the map exists to prevent, and `research/` is measurement code, not governance.

Contents are byte-identical to what the Architect delivered. **Only names and locations are
wrong. Nothing in this TZ edits content.**

---

## 1. Branch

```
git checkout main && git pull
git checkout -b tz-03-repo-hygiene
```

---

## 2. The three operations, and only these

```
git mv "BTC-EXECUTOR-INSTRUCTIONS .md" "BTC-EXECUTOR-INSTRUCTIONS.md"
git rm "research/EXECUTOR-INSTRUCTIONS .md"
git rm "research/SYSTEM-MAP.md"
```

Quote every path. Use `git mv` and `git rm`, never `rm` followed by `git add`, so that the
blob identity is preserved and the rename is visible as a rename in the diff.

Commit once, push, open a pull request against `main`. Do not merge it.

---

## 3. Forbidden in this TZ

- Editing a single byte of `SYSTEM-MAP.md`, `BTC-EXECUTOR-INSTRUCTIONS.md`, any report, any
  TZ, any `research/**` file, or `.gitignore`.
- Deleting, renaming or moving anything not named in §2.
- Rewriting history, amending a pushed commit, force-pushing, deleting a branch or a tag.
- Merging the pull request. Merge is the Boss's, after the Architect's verdict.

The root-artifact protection in `BTC-EXECUTOR-INSTRUCTIONS.md` §10 is waived **for the rename
in §2 only**. It applies in full to content.

---

## 4. Validation

Run each of these on the branch after §2 and paste the command and its output into the
report. Every one is an expectation, not a survey; a failure is BLOCKED.

| # | check | expectation |
|---|---|---|
| 4.1 | `sha256sum SYSTEM-MAP.md` | `a2323219474d11dc7670964d098be79a27f8d6ac13f4364a3b1ccf52621a40c1` — confirms revision `2026-09-10-b` landed intact |
| 4.2 | `sha256sum BTC-EXECUTOR-INSTRUCTIONS.md` | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` — unchanged by the rename |
| 4.3 | `git ls-files \| grep -c " "` | `0` — no tracked path contains a space |
| 4.4 | `git ls-files \| grep -c "SYSTEM-MAP"` | `1` |
| 4.5 | `git ls-files \| grep -c "EXECUTOR-INSTRUCTIONS"` | `1` |
| 4.6 | `git ls-files research/` | exactly `research/selftest-twap-divergence.py`, `research/twap-divergence.py`, `research/tz02-distribution.py` |
| 4.7 | `git diff --stat main...HEAD` | one rename and two deletions; **0 insertions, 0 deletions of content lines** |
| 4.8 | `sha256sum` of the three `research/*.py` files | unchanged from the §0 fingerprint table of the map |
| 4.9 | `git ls-tree -r --name-only HEAD \| grep -E "\.parquet\|\.zip"` | prints nothing |

Report the counts as counts. "All checks passed" is not a result.

---

## 5. Report

`CryptoReports/TZ-03-repo-hygiene-report.md`, straight to `main`, per
`BTC-EXECUTOR-INSTRUCTIONS.md` §4 and §8. Required: the fingerprint section, §2's commands as
run, the §4 table with real output, the §4.2 separation self-check from the contract, and the
"what could not be implemented" section — which should say "nothing".

The branch stays unmerged until the Architect's verdict.
