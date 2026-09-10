# TZ-04 — Market and Oracle Recorder — REPORT

**Status: BLOCKED.** The §0 fingerprint gate failed. No work was done: no recorder was
written, no socket was opened, no branch was created, nothing under `research/recorder/`
exists.

Executor model: **Opus** (`claude-opus-5`), as the TZ requires.

---

## 0. Fingerprint

Read from `SYSTEM-MAP.md` at `origin/main` = `7cbeeb3676e7712e119896f8a1415ef5bb1cedb8`.

**Revision string read:** `2026-09-10-c` — TZ-04 requires `2026-09-10-d`.

| anchor | required by TZ-04 §0 | computed | match |
|---|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | yes |
| `A2` — collector | `6c5089330629` | `6c5089330629` | yes |
| `A3` — phase | `0-reopened / 1-reopened / 2-not-started` | `1-complete / 2-not-started` | **no** |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | yes |

`A1` was not copied from the map. The Release asset was fetched anonymously and hashed:
76,818,669 bytes, SHA-256
`229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b`. `A3` was read from
map §5, which records phase 0 and phase 1 as `complete`.

### Fingerprint table

`wc -l`, bytes and `sha256sum` for `SYSTEM-MAP.md` and for every file the map's §0 table
lists at authoring time.

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 218 | 12,460 | reported | `d84fe3db984c13ebca62d59afc2a8afe2d2d78b400717eba72233a772cbefb88` | self-reference |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | yes |

All three `frozen` rows match the hashes printed in the map. The contract §1.4 check passes.
The block is entirely §0.

---

## 1. The blocker

TZ-04 requires System Map revision `2026-09-10-d` and phase anchor
`0-reopened / 1-reopened / 2-not-started`; the map committed on `origin/main` is revision
`2026-09-10-c` and states `1-complete / 2-not-started`. TZ-04 §1 asserts that "The CANON and
the System Map have been replaced accordingly" following the 2026-09-10 finding that the
CANON §1.1 settlement mechanic was wrong, but that replacement is not present in the
repository: the upload commit `7cbeeb3` ("Add files via upload") added
`CryptoTZ/TZ-04-market-recorder.md` and nothing else. The specification is therefore
gated on a state document that does not exist here, and the two anchors that fail are
exactly the two the map revision would have carried. TZ-04 §0 directs BLOCKED before any
work, and `BTC-EXECUTOR-INSTRUCTIONS.md` §1.3, §2 and §9 direct a BLOCKED report and a full
stop.

## 2. Evidence

The upload commit touched one file:

```
$ git show --stat --oneline 7cbeeb3
7cbeeb3 Add files via upload
 CryptoTZ/TZ-04-market-recorder.md | 187 ++++++++++++++++++++++++++++++++++++++
 1 file changed, 187 insertions(+)
```

No revision `2026-09-10-d` of the map exists on any ref in the repository. Every commit that
has ever touched `SYSTEM-MAP.md`, across all branches, remotes and tags:

```
3ab0270  2026-09-10T01:31:48+04:00  Revision 2026-09-10-c
8b28f86  2026-09-10T01:30:39+04:00  Revision 2026-09-10-c
d9e58e8  2026-09-09T21:16:25+00:00  Revision 2026-09-10-b
3538e1f  2026-09-10T01:11:28+04:00  Revision 2026-09-10-b
984854e  2026-09-10T00:50:26+04:00  Revision 2026-09-10-a
```

`git ls-remote origin` lists `main`, `tz-01-twap-divergence`,
`tz-01a-twap-divergence-corrected`, `tz-02-divergence-distribution`, `tz-03-repo-hygiene`,
`refs/pull/1/head` and `refs/tags/tz-01a-dataset`. The highest map revision on any of them
is `2026-09-10-c`.

The map's own §0 table publishes the anchors as read above:

```
**Revision string:** `2026-09-10-c`

| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `1-complete / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
```

Nothing was created or modified outside `CryptoReports/`. No file under `research/` was
touched, no directory `research/recorder/` was created, no network capture was started, and
no scratch space outside the repository was left behind.
