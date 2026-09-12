# TZ-07 — the oracle feed's variance–time curve, and the corrected sigma — REPORT

**Status: BLOCKED.** The §0 fingerprint gate **cannot be performed**. `SYSTEM-MAP.md` at
`origin/main` is not the System Map: commit `891d161` replaced the 314-line map with a 17-line
Russian cover note addressed to the Boss, so the file has no `## 0. Fingerprint gate` section, no
anchor table and no fingerprint table. Contract §1.3 requires the TZ header's revision string and
anchors to be compared against `SYSTEM-MAP.md` §0, and §1.4 requires every `frozen` row of that
section's fingerprint table to be hashed and matched; neither section exists to be read. No work
was done beyond this gate: no branch `tz-07-variance-time` was created, `research/tz07-variance-time.py`
was not written, `research/pfair.py` and `research/selftest-pfair.py` were not touched, no interval
directory was opened, no curve was measured, no `G_RATIO` was computed, and V1–V8 were not run.
Nothing was written under `/var/lib/btc-recorder/`. The live recorder — pid `228592`, running since
2026-09-12 09:53:04 — was not signalled, restarted or otherwise disturbed; this report was produced
from a separate git worktree at `/root/tz07-work/main-wt` so that the checkout the recorder runs
from was never switched.

Executor model: **Opus** (`claude-opus-5`), as the TZ requires.

---

## 0. Fingerprint

Read from `SYSTEM-MAP.md` at `origin/main` = `2d3dbdb4319fe9035504e123cfc5c0e0cc85e879`, checked
out clean into a fresh worktree.

**Revision string required by TZ-07 §0:** `2026-09-12-b`.

**Revision string read:** none. The file declares no revision of itself; it carries no
`**Revision …**` line, which is how every map in this repository has declared itself since
`2026-09-10-a`. Line 3 contains the sentence *«Карта — ревизия `2026-09-12-b`»* — a statement
*about* a map, inside a note that is not one. The last commit at which `SYSTEM-MAP.md` was a map is
`891d161`'s parent `4b3723a68d56b11419504b939e92e58d59cb928b`, whose content was introduced by
`70e1a13`; that map declares **`2026-09-12-a`**.

| anchor | required by TZ-07 §0 | read from map §0 |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | **§0 absent — not readable** |
| `A2` — collector | `6c5089330629` | **§0 absent — not readable** |
| `A3` — phase | `0-complete / 1-open / 2-not-started` | **§0 absent — not readable** |
| `A4` — executor contract | `437b45ea196b` | **§0 absent — not readable** |
| `A5` — recorder | `9fd1c7de0f74` | **§0 absent — not readable** |
| `A6` — pricer | `18be5d185fee` | **§0 absent — not readable** |

### Fingerprint table

Contract §8.1 requires `wc -l` and `sha256sum` for the map and for **every file the map's §0 table
currently lists**. That table currently lists no files, so the only row the contract yields is the
map itself:

| path | lines | bytes | state | SHA-256 |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 17 | 3,308 | reported | `89a4907415b8184e42037e2c4a6228feb48f16746693f63bcd1e4a22c4e0e437` |

The hashes of the files the **previous** revision's table listed are given in §2 below, as evidence
for the blocker and for no other purpose.

---

## 1. The blocker

`SYSTEM-MAP.md` on `main` is a cover note, not the System Map, and the fingerprint gate therefore
has nothing to read. Commit `891d161` ("Update SYSTEM-MAP.md", 2026-09-12 20:40:48 +0400) is a
single-file change of `11 insertions(+), 308 deletions(-)`: it overwrote the map with the four-item
Russian instruction list that normally accompanies an upload — *«## Что сделать: 1. Одной
загрузкой… 2. В Claude Code на VPS… отправить `EXECUTE TZ-07` … 3. Прислать
`CryptoReports/TZ-07-variance-time-report.md` 4. Слить pull request»*. Two minutes later `2d3dbdb`
added `CryptoTZ/TZ-07-variance-time.md` and changed nothing else, so the map was never restored.
Revision `2026-09-12-b` — the revision TZ-07 §0 names, the one that would carry the new `A6` anchor,
the post-TZ-06 `frozen` hashes for `research/recorder/analyze.py` and `research/recorder/selftest.py`,
and rows for the three files TZ-06 created — does not exist anywhere in the repository's history.
Contract §1.3 and §1.4 are unsatisfiable as written, §9 names an absent required input and a failed
fingerprint gate as BLOCKED conditions, and §2 forbids substituting a reasonable alternative for a
missing Architect document — I may not reconstruct revision `-b` from the TZ header's own anchor
values, because a gate that reads its expected values from the file it is gating is not a gate. §10
separately forbids me from editing `SYSTEM-MAP.md` at all.

**There is no reading of the repository under which this gate passes.** Falling back to the last
real revision fails on two independent counts, both shown below: its revision string is
`2026-09-12-a` and TZ-07 requires `2026-09-12-b`, and two of its `frozen` rows no longer match the
files on `main`.

---

## 2. Evidence

### E1 — the map file at `origin/main`

```
$ git rev-parse origin/main
2d3dbdb4319fe9035504e123cfc5c0e0cc85e879
$ wc -l SYSTEM-MAP.md
17 SYSTEM-MAP.md
$ sha256sum SYSTEM-MAP.md
89a4907415b8184e42037e2c4a6228feb48f16746693f63bcd1e4a22c4e0e437  SYSTEM-MAP.md
$ grep -c '^## 0' SYSTEM-MAP.md
0
```

Its entire heading structure is one line, `## Что сделать` (line 13). The strings `A1`, `A2`, `A3`,
`A4`, `A5`, `frozen` and `Fingerprint` do not occur in it at all. `A6` occurs exactly once, on line
3, inside the prose sentence *«Существенное: новый якорь `A6` на прайсер»* — an announcement that
revision `-b` introduces such an anchor, never a row carrying its value.

### E2 — the commit that removed the map

```
$ git show --stat 891d161
commit 891d161503ddef3fa9b0ea7641f257533c877b13
Date:   Sat Sep 12 20:40:48 2026 +0400
    Update SYSTEM-MAP.md
 SYSTEM-MAP.md | 319 ++--------------------------------------------------------
 1 file changed, 11 insertions(+), 308 deletions(-)

$ git show --stat 2d3dbdb
commit 2d3dbdb4319fe9035504e123cfc5c0e0cc85e879
Date:   Sat Sep 12 20:42:28 2026 +0400
    Add files via upload
 CryptoTZ/TZ-07-variance-time.md | 214 ++++++++++++++++++++++++++++++++++++++++
 1 file changed, 214 insertions(+)
```

Every revision of the map that has ever been committed, newest first — the declaration line each
one carries. There are ten; none declares `2026-09-12-b`:

```
$ for c in $(git log --all --format=%H -- SYSTEM-MAP.md); do \
    r=$(git show $c:SYSTEM-MAP.md | grep -m1 -oP '^\*\*Revision \K[0-9a-z-]+'); \
    printf "%s  rev=%-14s  %s\n" "${c:0:7}" "${r:-<none>}" "$(git log -1 --format=%s $c)"; done
891d161  rev=<none>          Update SYSTEM-MAP.md
70e1a13  rev=2026-09-12-a    Update SYSTEM-MAP.md
c7f569d  rev=2026-09-11-c    Update SYSTEM-MAP.md
ab15e00  rev=2026-09-11-b    Update SYSTEM-MAP.md
8334408  rev=2026-09-11-a    Update SYSTEM-MAP.md
8d1a4fa  rev=2026-09-10-e    Update SYSTEM-MAP.md
3cd4feb  rev=2026-09-10-d    Update SYSTEM-MAP.md
8b28f86  rev=2026-09-10-c    Update SYSTEM-MAP.md
3538e1f  rev=2026-09-10-b    Update SYSTEM-MAP.md
984854e  rev=2026-09-10-a    Add files via upload
```

The single occurrence of the string `2026-09-12-b` anywhere in the history of this file is inside
`891d161`'s prose sentence quoted above, which is not a revision declaration.

### E3 — the fallback fails too

Revision `2026-09-12-a` at `4b3723a68d56b11419504b939e92e58d59cb928b` is the last `SYSTEM-MAP.md`
carrying a §0. Its table has twelve rows, nine of them `frozen`. Lines, bytes and hashes below are
computed on the clean `main` checkout; the last column compares them to what revision `-a` printed.

| path | lines | bytes | state in `-a` | SHA-256 on `main` | matches map `-a` |
|---|---|---|---|---|---|
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | yes |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | yes |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | yes |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | yes |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | yes |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | **no** — `-a` prints `5bade9ff5666…` at 788 lines / 33,323 bytes |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | **no** — `-a` prints `3678c0b4f95a…` at 516 lines / 27,693 bytes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | yes |

Both mismatches are the additive edits TZ-06 §0 authorized and its R-c applied; revision `-b` was
to have reprinted them. Under contract §1.4 they are two `frozen` rows that differ, which is a
second, independent BLOCKED.

Three files TZ-06 added are on `main` and appear in no §0 table anywhere:

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/pfair.py` | 233 | 9,844 | `18be5d185fee807fef9a840ab965dc42fa41c3a7a0b01b27c359afce96289676` |
| `research/selftest-pfair.py` | 221 | 10,939 | `f4b4f8287f3ebb0c9cbabaee40e87580bddab6d23ad0fe0e44aa87bc09bc3842` |
| `research/tz06-calibration.py` | 569 | 26,548 | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` |

### E4 — what the anchors would have matched

Stated so that the Architect can see the blocker is a missing document and not repository drift.
This is not the gate and does not stand in for it: the values on the right are computed from the
artifacts, not read from a map, and a gate whose expected values come from the gated TZ is not a
gate.

| anchor | required by TZ-07 §0 | artifact | computed |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | Release `tz-01a-dataset` | not re-downloaded this run; equals the value revision `-a` §2.1 records |
| `A2` — collector | `6c5089330629` | `research/twap-divergence.py` | `6c5089330629` |
| `A3` — phase | `0-complete / 1-open / 2-not-started` | map §5 | `-a` §5 reads phase 0 `CLOSED 2026-09-11`, phase 1 `open`, phase 2 `not started` |
| `A4` — executor contract | `437b45ea196b` | `BTC-EXECUTOR-INSTRUCTIONS.md` | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` | `research/recorder/recorder.py` | `9fd1c7de0f74` |
| `A6` — pricer | `18be5d185fee` | `research/pfair.py` | `18be5d185fee` |

---

## 3. Scope of the stop

The host gate of TZ-07 §0 was not evaluated: contract §1.3 puts the fingerprint gate before all
other work, and the host gate reads the capture. No `chainlink`, `twap60`, `binance`, `twap30`,
`quotes` or `runtime` file was opened, and no interval directory was listed or counted — V8's count
of post-`1789166400` intervals is therefore **not** in this report. `/root/tz07-work/` holds only
the git worktree this report was written from. The capture is untouched and still running.
