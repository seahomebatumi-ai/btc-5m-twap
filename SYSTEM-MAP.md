# SYSTEM MAP — btc-5m-twap

**Revision 2026-09-23-a.** Written by the Architect; the Executor never edits it. This is a
**state** document: what exists right now. It holds no mission, no rules and no history.

- The CANON (Architect's project instructions, not in this repository) holds the mission, the
  fair-value model, the measured facts and the phase gates.
- `BTC-EXECUTOR-INSTRUCTIONS.md` holds how the Executor works.
- **This map never restates a CANON §1.2 formula.**

---

## 0. Fingerprint gate

Every TZ header states the required revision string and the anchors below. The Executor compares
before doing any work; a mismatch is BLOCKED.

**Revision string:** `2026-09-23-a`

| anchor | value |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-undecidable-5tau` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `729f0bcdbee3` |

Anchors are the first 12 hex characters of the SHA-256 of the named artifact, except `A3`.
`A5` is `research/recorder/recorder.py`, the code the live capture runs. `A6` is
`research/pfair.py`, the only implementation of the model: **any TZ that scores a pricer states
`A6`, so what was scored is never in doubt.** `A6` changed at `fb5c426` when PR #8 replaced
`G_RATIO` with `SD_SCALE`: the §1.2 formulas and `state` are byte-identical inside it and only the
constant multiplying `sigma * sqrt(H(tau))` moved. `9bd4213a60a3` is the value TZ-07a and TZ-07b
were both gated against, and nothing scored under it is re-opened by this revision. **PR #9
touched no anchor:** `pfair.py` is byte-identical on both sides of `1b8e4a7`, so TZ-08a's scores
and every later score are gated against the same pricer. **PR #10 touched no anchor either:** it
added one file and changed none, so `A6` is unmoved across `f781dc3`. **TZ-10 and TZ-10a moved
nothing:** both stopped at their own validation before any file was edited. **PR #11 moved `A6`
for the first time since `fb5c426`:** TZ-10b added `LOG_PHI_CROSSOVER`, `log_phi_erfc_branch`,
`log_phi_asymptotic_branch` and `log_phi` to `pfair.py` — 32 insertions, no line removed or
altered — so `SD_SCALE`, `corrected_sd`, `phi`, `state` and both §1.2 branches are byte-identical
across the merge. **A second link function beside the first is not a change to the first**, and
`cb72abb8dd8a` stays the value TZ-08a and TZ-10b were gated against; nothing scored under it is
re-opened by this revision. **TZ-11 moved no anchor and no file:** it was BLOCKED at its own §5.2
before anything was built. **PR #12 moved `A6` from `45b307b221d4` to `729f0bcdbee3`:** TZ-11a
added twelve names to `pfair.py` after `log_phi` — the Student link `log_t_cdf` and `t_cdf` with
their three helpers and two constants, `student_sd`, `p_fair_student`, and the three measured
tables `ADMIT`, `LINK_NU` and `LINK_SCALE` — 128 insertions and no line removed or altered.
`SD_SCALE`, `corrected_sd`, `phi`, `log_phi`, `p_fair`, `far_branch`, `near_branch`,
`state_and_sd`, `TAUS` and `GATED_TAUS` are byte-identical across the merge, re-checked by the
Architect through `ast`. **TZ-11a was gated against `45b307b221d4` and scored `pfair.py` at
`729f0bcdbee3`**, its branch head `2746518`; nothing scored before it is re-opened. **PR #13 moved no
anchor:** it added one file and changed none, so `A6` is unmoved across `44d77008`, and TZ-12 was
gated against `729f0bcdbee3` and scored nothing at all — it reads no label and computes no observed
statistic of any set. The one table TZ-12 freezes, `SIGMA_LOG_NU`, lives in the new file and not in
`pfair.py`. **PR #14 moved no anchor either:** it added `research/tz13-sized-gate-test3.py` and changed
no path, so `A6` is unmoved across it. TZ-13 was gated against `729f0bcdbee3` and scored `pfair.py` at
`729f0bcdbee3` — the first score of the Student pricer under the sized gate. **PR #15 moved no anchor:**
it added `research/tz14-quote-inventory.py` and changed no path. TZ-14 read `pfair.py` at
`729f0bcdbee3` for `sigma_hat` alone and computed no probability. **PR #16 moved no anchor:** it added
`research/tz15-phase2-gate.py` and changed no path, merged at `8d2a4c6`. TZ-15 scored `pfair.py` at
`729f0bcdbee3` — the first statistic of a quote against the pricer — through `tz11a.checkpoint_row`,
calling no `pfair` entry point itself. **PR #17 moved no anchor:** it added
`research/tz17-settlement-chain.py` and changed no path, merged at `745715e`. TZ-17 and TZ-18 read no
pricer, and TZ-18's header states `A6` only so that what was not scored is not in doubt. **PR #18 moved
nothing:** it was closed unmerged (§1).

### Fingerprint table

Every report states `wc -l` and `sha256sum` for each row. `frozen` rows must match the hash
printed here or the run is BLOCKED. `tracked` rows are reported with no expectation.

| path | lines | bytes | state | SHA-256 |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | — | — | reported | self-reference; report the value you compute |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` |
| `research/pfair.py` | 441 | 19,357 | frozen | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` |
| `research/selftest-pfair.py` | 619 | 32,559 | frozen | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` |
| `research/tz06-calibration.py` | 577 | 27,138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` |
| `research/tz07a-variance-time.py` | 623 | 28,414 | frozen | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | frozen | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` |
| `research/tz10b-sigma-or-link.py` | 1,224 | 61,018 | frozen | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` |
| `research/tz11a-student-link.py` | 1,231 | 64,732 | frozen | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` |
| `research/tz12-sized-gate.py` | 1,157 | 61,637 | frozen | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` |
| `research/tz13-sized-gate-test3.py` | 1,074 | 53,901 | frozen | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` |
| `research/tz14-quote-inventory.py` | 2,124 | 109,972 | frozen | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` |
| `research/tz15-phase2-gate.py` | 1,517 | 73,799 | frozen | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` |
| `research/tz17-settlement-chain.py` | 1,102 | 38,622 | frozen | `e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92` |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` |

Hashes are of the file as committed on `main` at revision date, verified by the Architect against
`origin/main` — not copied from a report. Changing a `frozen` row requires a TZ that authorizes
it and a new map revision. **The six recorder files are frozen because the live capture runs
them**: an unauthorized edit is a change to a running instrument. **`pfair.py` is frozen because
every score this project will ever quote comes out of it** — both links and the four measured
tables. `tz07a-variance-time.py`, `tz07b-settlement-dispersion.py`, `tz08a-out-of-sample.py`,
`tz09-disk-inventory.py`, `tz10b-sigma-or-link.py`, `tz11a-student-link.py`, `tz12-sized-gate.py`
and `tz13-sized-gate-test3.py` are frozen because a committed measurement came out of each — for
`tz12-sized-gate.py` that is `SIGMA_LOG_NU`, the member-bootstrap spread of `log ν̂`, and the sized
gate; for `tz13-sized-gate-test3.py`, the first verdict under it; for `tz14-quote-inventory.py`, the
first read of the book — and it also holds **the only implementation of CANON §1.1's taker fee,
`fee_pp`, and of the executable touch, `touch_of`**, so every later TZ imports them from it and none
writes them again. `tz15-phase2-gate.py` is frozen for Phase 2's first reading, and because it holds
**the only implementation of the exact Poisson-binomial tail, `pb_upper`, its critical count, `crit`,
and the after-fee selection, `select`**, which a later TZ imports and never writes again.
`tz17-settlement-chain.py` is frozen for the backup track's first answer, B0, and because it holds
**the only committed request outside the recorder that the venue's edge serves** — `Accept:
application/json` and a `User-Agent` of its own, where Python's default agent is refused (§6).
`tz06-calibration.py` is frozen at
its post-PR-#9 hash: it carries `after` and `need`, and at their defaults the run is the one TZ-06
ran. **Every one of the twenty-five rows above was read byte for byte by the Architect from
`origin/main` at `202b791862736de0648b7fc1e1a53fb0a3ef3d93` on 2026-09-23**, the TZ-18 report, by
cloning the public repository and hashing each path: 25 of 25 equal to the values printed here, lines
and bytes included. The twenty-four carried rows are byte-identical to their values at `8d2a4c6`, and
the one row this revision adds is byte-identical to PR #17's head `8f1bc93` and to the hash TZ-17's
report prints.

**Revision `2026-09-19-c` reached `main` at `f883be7` and is confirmed there**, as §7 item 18's rule
requires of every upload: SHA-256 `3a88c35707fb937043b56571d5b146819a43c905122f379ad89fc75c95e3e1a0`,
byte-identical to the Architect's mirror, and it is the revision TZ-17 and TZ-18 were gated against.
`c0d18e8` re-uploaded it unchanged on 2026-09-22 — an empty commit — and
`CryptoTZ/TZ-18-chainbook-capture-deploy.md` landed at `795f176` byte-identical to the copy the
Architect audited. **This revision replaces the map and ships alone:** no TZ is attached. It is paired
with CANON revision `2026-09-23-a`, which lives in the Architect's project instructions and not here.

---

## 1. Repository

`github.com/seahomebatumi-ai/btc-5m-twap` — **public**. No dataset, archive or binary has ever
entered git history. A bare clone of it is one pack of `1,295` KiB, read by `git count-objects`
on 2026-09-23; it holds text alone and stays that way.

| path | contents |
|---|---|
| `CryptoTZ/` | specifications, Architect → Boss upload |
| `CryptoReports/` | reports, Executor → straight to `main` |
| `research/` | measurement code and the pricer, Executor → branch + PR |
| `research/recorder/` | live capture and its analyzer — six files, all on `main` |
| `engine/` | live engine — **does not exist yet** |
| root | `SYSTEM-MAP.md`, `BTC-EXECUTOR-INSTRUCTIONS.md`, `.gitignore` |

**Branches on `origin`, read with `git ls-remote` on 2026-09-23 as §7 item 55 requires.** `origin`
carries **one branch and no other**: `refs/heads/main` at `202b791862736de0648b7fc1e1a53fb0a3ef3d93`,
equal to `HEAD` — the TZ-18 report, 2026-09-22 23:20:20 UTC, parent `795f176`, the upload of TZ-18's
specification. `tz-18-chainbook-capture` was deleted when PR #18 was closed unmerged, and
`tz-17-settlement-chain` after PR #17's merge, as `tz-15-phase2-gate`, `tz-14-quote-inventory`,
`tz-13-sized-gate-test3`, `tz-12-sized-gate`, `tz-11a-student-link` and `tz-09-disk-inventory` were
before them. **Every commit any artifact names is still served**, as `refs/pull/NN/head`: `18` =
`8caa0b4`, `17` = `8f1bc93`, `16` = `f7f171a`, `15` = `ffef5cd`, `14` = `7ef9723`, `13` = `6dc0e24`,
`12` = `2746518`, `11` = `d34606e`, `10` = `e45f38e`, `9` = `e2625ea`, `8` = `26bbb61`, `7` = `c44af68`,
`6` = `5ed667a`, `5` = `4216c04` — the commit the capture runs — `4` = `0e13a5c`, `3` = `ee2f632`, `2` =
`3895356` and `1` = `d9e58e8`. The tag `refs/tags/tz-01a-dataset` is an annotated object `d3251aa`
peeling to `ea9290b`: twenty-two refs in all. No `tz-11` and no `tz-16` branch exists anywhere. The
head of `main` is never a gate; commits are named where they matter.

| pull request | head | disposition |
|---|---|---|
| PR #18 | `8caa0b4` | the chain book: one standard-library instrument with `--selftest`, `--verify-tz17`, `--serve` and `--prove`. **Closed unmerged** after the Architect's verdict of 2026-09-23, branch deleted: its service could not read the venue (§7 item 77). Its `--verify-tz17` produced G-CHAIN, which stands (§4). One file, 1,420 lines, never on `main`. |
| PR #17 | `8f1bc93` | the settlement chain: Stage F's fetch of the venue's own documents for 200 fifteen-minute windows and the 601 five-minute slots beneath them, Stage A's identities I1–I3 and D1–D7, and 37 self-test asserts. **Merged 2026-09-22** into `main` at `745715e` after the Architect's verdict, branch deleted. One file added, 1,102 lines, none changed, no anchor moved. |
| PR #16 | `f7f171a` | the Phase 2 gate: the selection on the after-fee edge, the exact constants, the once-only label read behind the push check and the ledger, the reading, influence, diagnostics, the projection and seven self-tests. **Merged 2026-09-19** into `main` at `8d2a4c6` after the Architect's verdict, branch deleted. One file added, 1,517 lines, none changed, no anchor moved. |
| PR #15 | `ffef5cd` | the quote inventory: the first read of Tier C over 1,200 intervals, the book's shape, executability, the two tokens, the market document, seven predictions, six self-tests. **Merged 2026-09-18** into `main` at `93d1341`, branch deleted. One file added, 2,124 lines, none changed, no anchor moved. It computes no probability and no statistic of a quote against the pricer. |
| PR #14 | `7ef9723` | the sized gate applied once to test 3: the set, the guarded walk, label-free constants written to disk before any outcome, the once-only outcome read, the per-`tau` verdict, the power projection and six self-tests. **Merged 2026-09-18** into `main` at `7ba5df1`, branch deleted. One file added, 1,074 lines, none changed, no anchor moved. |
| PR #13 | `6dc0e24` | the sized gate: `SIGMA_LOG_NU` and `SIGMA_LOG_NU_CENSORED`, the error rates of every TZ-11a gate, §4's constants per population, six self-tests and the TZ-13 instrument. **Merged 2026-09-17** into `main` at `44d77008`. One file added, none changed, no anchor moved. It reads no label and computes no observed statistic. |
| PR #12 | `2746518` | the Student link — `log_t_cdf`, `t_cdf`, `student_sd`, `p_fair_student` and the three tables `ADMIT`, `LINK_NU`, `LINK_SCALE` — its six self-tests, `log_cdf=None` on `tz07a.log_likelihood` and `tz07a.lambda_hat`, and the TZ-11a instrument. **Merged 2026-09-15** into `main` at `3452fb8`. Four files: `pfair.py` +128 −0, `selftest-pfair.py` +178 −0, `tz07a-variance-time.py` +8 −4 — exactly the four lines TZ-11a §5.3 names — and 1,231 new. `A6` moved; the ten `pfair.py` objects TZ-11a V6 names are byte-identical across it. |
| PR #11 | `d34606e` | the tail-accurate `log Phi`, its six self-tests and the TZ-10b instrument. **Merged 2026-09-14** into `main`. Three files, **insertions only**: 32 into `pfair.py`, 135 into `selftest-pfair.py`, 1,224 new. `A6` moved; `SD_SCALE`, `corrected_sd`, `phi` and `state` byte-identical across it. The merge commit is not named: no report states it and no gate reads it. |
| PR #10 | `e45f38e` | the disk inventory instrument. **Merged 2026-09-14** into `main` at `f781dc3`; the branch is gone from `origin` since 2026-09-17 (§7 item 55). One file added, none changed, no anchor moved. |
| PR #9 | `e2625ea` | the out-of-sample driver, and `after` / `need` on `scoring_set` and `build`. **Merged 2026-09-13** into `main` at `1b8e4a7`, branch deleted. 11 insertions and 3 deletions in `tz06-calibration.py`; `pfair.py` untouched on both sides. |
| PR #8 | `26bbb61` | `SD_SCALE`, the TZ-07b instrument and 30 self-tests; `G_RATIO` and the four checks that encoded it removed. **Merged 2026-09-13** into `main` at `fb5c426`, branch deleted. `pfair.py`: `state` untouched on both branches. |
| PR #7 | `c44af68` | `corrected_sd`, the TZ-07a instrument and 48 self-tests. **Merged 2026-09-13** into `main` at `467805e`. Purely additive to `pfair.py`: 42 insertions, no line removed or altered. |
| PR #6 | `5ed667a` | the pricer, its calibration pipeline and R-c. Merged 2026-09-12 at `4b3723a`. |
| PR #5 | `4216c04` | Tier C and the SNTP repair. Merged 2026-09-12 at `c3dab7d`. |
| PR #4 | `0e13a5c` | the TZ-05 BLOCKED report. Closed. |
| PR #3 | `ee2f632` | the recorder and its analyzer, merged after the TZ-04b verdict |
| PR #1 | `d9e58e8` | TZ-03, the rename and the two deletions |

Commits still named by an artifact: `ea9290b` — the commit the dataset tag points at; `a772d19` —
TZ-02; `3895356` — the recorder commit TZ-04b scored; `4216c04` — the commit the capture runs;
`5ed667a` — the commit that first implemented the pricer; `c44af68` — the commit that added
`corrected_sd` and the `G_RATIO` literals; `26bbb61` — the commit that replaced them with the
`SD_SCALE` literals; `e2625ea` — the commit TZ-08a scored from; `1b8e4a7` — the merge that put it
on `main`; `d34606e` — the commit `log_phi` and the TZ-10b instrument come from; `2746518` — the commit TZ-11a
scored from; `3452fb8` — the merge that put it on `main`; `6dc0e24` — the commit TZ-12 built and
both of its full runs are of; `44d77008` — the merge that put it on `main`, and the state the carried
rows of §0 were verified against; `2c7694a9` — the upload of revision `2026-09-17-a` and TZ-13, the
merge base TZ-13 built on; `7ef9723` — the commit TZ-13 built and both of its full runs are of; `7ba5df1` — the merge that put
it on `main`; `dad557d` — the upload of revision `2026-09-18-a`; `a314151` — the upload of TZ-14's
specification; `b2269bb` — the upload of revision `2026-09-18-b` and the merge base TZ-14 built on;
`ffef5cd` — the commit TZ-14 built and both of its full runs are of; `5516e73` — the TZ-14 report;
`93d1341` — the merge that put it on `main`; `704f3f3` — the upload of revision `2026-09-19-a`;
`041b5bc` — the upload of TZ-15's specification, and the merge base TZ-15 built on; `f7f171a` — the
commit TZ-15 built and both of its scored runs are of; `c729008` — the TZ-15 report; `8d2a4c6` — the
merge that put it on `main`; `f883be7` — the upload of revision `2026-09-19-c`, and `c0d18e8` its empty
re-upload; `2054800` — the upload of TZ-17's specification, and the merge base TZ-17 built on;
`8f1bc93` — the commit TZ-17 built and its runs are of; `c4f2099` — the TZ-17 report; `745715e` — the
merge that put it on `main`; `795f176` — the upload of TZ-18's specification, and the merge base TZ-18
built on; `8caa0b4` — the commit TZ-18 built, which every run of it and its service's `start` record
name; `202b791` — the TZ-18 report, and the state every row of §0 was read at.

**Tag:** `tz-01a-dataset` → `ea9290b92b9fa50c22d0560d5d01dfa392af44df`.

A read-only mirror of this map also sits in the Architect's project files. The repository copy is
the authority; the mirror is never edited and never quoted as state.

**Files on `main`:** twenty-seven TZ files (`TZ-01` … `TZ-18`, none yet for TZ-16), twenty-seven
reports, seventeen `research/` scripts, six `research/recorder/` files, two governance files, `.gitignore`
— **80 paths**, counted by the Architect with `git ls-tree -r --name-only` on `origin/main` at `202b791`:
27 under `CryptoReports/`, 27 under `CryptoTZ/`, 23 under `research/` and 3 at the root. **Eight of the
twenty-seven reports are BLOCKED reports**, each by its own status line and each one file in one commit: TZ-04 at
`28e4444`, TZ-04a at `3eead29`, TZ-05 at `0e13a5c`, TZ-07 at `8377180`, TZ-08 at `2fab92a`, TZ-10 at
`1fcd19f`, TZ-10a at `d015d3c` and TZ-11 at `0b080c1`. For the last three no branch and no pull
request exists, and no `research/` file moved (§7 item 73).

---

## 2. Data

### 2.1 The observation set — the only dataset that exists

| field | value |
|---|---|
| location | Release `TZ-01a validated observation set`, tag `tz-01a-dataset`, public |
| asset | `twap-divergence-observations.parquet` |
| size | 76,818,669 bytes |
| SHA-256 | `229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b` |
| rows | 1,051,170 — 210,234 intervals × 5 checkpoints |
| checkpoints | `tau` ∈ {240, 180, 120, 90, 60} seconds remaining |
| window | 2024-09 … 2026-08, 730 days |
| source | `data.binance.vision`, spot `BTCUSDT`, 1-second klines, 63,072,000 bars, each monthly archive checksum-verified |
| gaps | 0 missing bars, 0 forward-fills; 210,240 intervals found, 210,234 used |

Anyone can fetch and verify it with no token:
`curl -sL https://github.com/seahomebatumi-ai/btc-5m-twap/releases/download/tz-01a-dataset/twap-divergence-observations.parquet | sha256sum`

**Columns (25).** Keys `interval_open_ts`, `month`, `tau`, `t`. Inputs `K`, `S_t`, `naive_move`,
`twap_so_far`, `state`. Volatility `sigma_pre`, `sigma_live`, `sd_remaining_pre`,
`sd_remaining_live`. Prices `p_twap_pre`, `p_naive_pre`, `p_twap_live`, `p_naive_live`.
Settlement proxies `twap_1s`, `twap_30s`, `twap_60s`, `outcome_1s`, `outcome_30s`, `outcome_60s`.
Integrity `n_missing_bars`, `prior_filled_bars`.

**The price data and the integrity accounting remain valid.** The `p_twap_*` columns implement
the superseded `p_interval` model and the `outcome_*` columns are invalid labels — see §2.2. This
set is Binance data and can no longer supply a label to anything.

### 2.2 The outcome labels are invalid — withdrawn 2026-09-10

`outcome_1s`, `outcome_30s` and `outcome_60s` are all **full-interval averages** of Binance
prices compared against the interval open, at 1 / 30 / 60-second sampling.

**No Polymarket settlement rule has ever had that shape.** Before 2026-08-07 the venue compared a
single close against a single open. Since 2026-08-07 it compares two readings of a Chainlink
trailing-TWAP feed — one at the close, one at the open — with a 30-second lookback until
2026-08-14 and 60 seconds after it.

The three labels are therefore withdrawn, along with every score computed against them. They stay
in the Parquet file for forensics and are never used again. The 4.147% disagreement between
`outcome_1s` and `outcome_60s` is a fact about two invalid labels and carries no information.

Correct labels are the venue's own resolutions, captured per interval as `resolution.json`. TZ-04b
read 200 of them and TZ-06 read 400.

### 2.3 Live capture — two tiers running, the quotes of 1,200 intervals read twice and scored once

**Tier A** has been capturing since **2026-09-10 10:21:09 UTC**, into `/var/lib/btc-recorder/**`
on the VPS — outside the repository, never in git history. Streams, one gzipped file per interval:
`twap60`, `twap30`, `chainlink`, `binance`, plus `gamma.json` (S6, the market document at
`T0 + 5`), `resolution.json` (S7, the venue's settled document), `runtime.jsonl` and
`manifest.json`. Reports carry the venue payload's own `timestamp` in milliseconds and
`full_accuracy_value` at full precision; the manifest is a pure function of the interval directory
and of the schema of the day it was written.

**Tier C** — seven order-book snapshots per interval per token id, fourteen reads, at
`tau ∈ {240, 180, 120, 90, 60, 30, 10}` — was added **2026-09-12 09:53:05 UTC** on commit
`4216c04`, pid `228592`. It stores each reply verbatim with its HTTP status in
`quotes.jsonl.gz`, and the manifest gained `quotes_complete` and `quote_offsets_ms`, both
independent of `complete`. The Tier B order-book probe ran once, for 60 minutes, and retained
exactly one interval.

**What has been read.**

| read by | span | units considered | scored |
|---|---|---|---|
| TZ-04b | T0 `1789035900` … `1789100100` | 215 | 200, the Phase 0 set; all 15 non-members failed on `disconnect` |
| TZ-05a | T0 `1789206900` … `1789207800` | 5 | 4, deployment proof only — 56 of 56 reads at HTTP 200 |
| TZ-06 | T0 `1789033800` … `1789166400` | 443 | 400, the Phase 1 set; 43 non-members, every one failing on `disconnect`. **No member carries Tier C** — all closed before the `4216c04` restart |
| TZ-07a | first member `1789035000`, last `1789166400` | 443 | the same 400, re-derived by calling `tz06-calibration.scoring_set`. Feed only: `chainlink`, `twap60` and each member's `gamma.json` |
| TZ-07b | first member `1789035000`, last `1789166400` | 443 | the same 400 again, re-derived the same way; member list SHA-256 `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9`, of the sorted `T0` list as decimal ASCII joined by newlines with no trailing newline. `chainlink` only, plus `twap60` for `K` in the causality check. **No outcome read at all** — no `resolution.json`, no `priceToBeat`, no label |
| TZ-08 | — | — | **BLOCKED at its own §7 V2 before any score existed.** No branch, no driver, no set, no statistic |
| TZ-10 | — | — | **BLOCKED at its own §5.2 before any measurement existed.** Three of the five `log_phi` self-tests that TZ fixed cannot be passed by a correct implementation. No branch, no code, no set, no statistic; `pfair.py` and `selftest-pfair.py` untouched on `main` |
| TZ-10a | — | — | **BLOCKED at its own §7 V2 before any measurement existed.** V2 required `u = Y / sd` to be bit-identical under perturbation of the reports `Y` is built from; no correct implementation can pass it. No branch, no code, no set, no statistic. Its §5.2 self-tests were evaluated first and **all six passed**. The only capture read was a scratch probe over 20 interval directories — `chainlink` and manifests, no `resolution.json` and no quote file |
| TZ-10b | T0 `1789035000` … `1789296300` | 800 | **753 — the intersection: every member of the two 400s whose successor interval also qualifies**, 376 TZ-06 and 377 TZ-08a. Member-list SHA-256 `5cc0b9ceba02a5a9f9ebdeb4dfa421b89a90a58d0f414b8d95cc359cf2902590`, **rebuilt by the Architect from the report's own disclosure**, as were both committed 400s. 47 members fail the `sigma_post` rule: 5 on the successor manifest alone, 42 on that and a disconnect inside `[T0+300, T0+600]`. `manifest.json`, `chainlink`, `twap60`, and `resolution.json` in two named places; **no quote file and no `gamma.json` opened** |
| TZ-08a | T0 `1789166700` … `1789296300` | 433 | **400 — the Phase 1 out-of-sample set.** 33 non-members, every one failing on `disconnect`. Disjoint from the TZ-06 set by construction; member-list SHA-256 `3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762`, computed the same way. `manifest.json`, `resolution.json`, `chainlink` and `twap60`; **no quote file opened** |
| TZ-11 | — | — | **BLOCKED at its own §5.2 item 5 before anything was built.** That item fixed an expectation on `p_fair_student` at `ν = 3`, and the function it names reads `LINK_NU[tau]`, a table this same TZ would have measured; no correct implementation can pass it unless the fit returns exactly `3.00000`. No branch, no code, no constant, no set, no statistic; `pfair.py`, `selftest-pfair.py` and `tz07a-variance-time.py` untouched on `main`. §5.2's other five items were evaluated by a scratch probe first — items 1 to 4 **all pass**, item 6 needs tables that do not exist. Two scratch probes called `tz06.scoring_set` unmodified and carried out counts only; no label entered any number, no quote file and no `gamma.json` was opened |
| TZ-11a | T0 `1789033800` … `1789427700` | 1,314 | **three sets of 400:** the TZ-06 400 as the fit set, the TZ-08a 400 as test 1, and **test 2 — the first 400 qualifying slots after `1789296300`**: 438 considered from `1789296600`, members `1789296900` … `1789427700`, 38 non-members all on `disconnect`, member-list SHA-256 `2dd0fcc4dc2cf379e08c21a4524c3eab799aad7bff3136c37e32910cecb8fa70`. **All three lists rebuilt by the Architect from the report's disclosure, 3 of 3**, with `ADMIT` at 7 of 7 and every admissible count at 21 of 21. `manifest.json`, `chainlink` and `twap60` for all 1,200; `resolution.json` inside `tz06.qualification`, for the two test sets in M4 and M5, and for the TZ-08a 400 in V4; **no label of the fit set, no quote file and no `gamma.json` opened** |
| TZ-12 | T0 `1789033800` … `1789427700` | 1,314 | **the same three 400s, re-formed by `tz11a.the_sets` unmodified**, all three member-list hashes asserted equal to the committed values and each set's unit-by-unit disclosure asserted equal to TZ-11a's own run output, 3 of 3. 8,400 checkpoint rows, **every one carrying `label = None`, asserted after the last measurement**. `manifest.json`, `chainlink` and `twap60`; `resolution.json` only inside `tz06.qualification`, the set rule's own read, which §2 of that TZ names as its one exemption. **No score of any set was computed: every figure is a property of the pricer's own predictions.** No quote file and no `gamma.json` opened |
| TZ-13 | T0 `1789033800` … `1789669800` | 807 for test 3; the read set is 2,121 slots | **test 3 — the first 750 qualifying slots with `T0 > 1789427700`**: 807 considered from `1789428000`, members `1789428000` … `1789669800`, 57 non-members all on `disconnect`, member-list SHA-256 `0f618581ae8be86beed445fc5ad90b8d1d6352271ca8cfd5f5943207011273f2`; the three committed 400s re-formed by `tz11a.the_sets`, hash-asserted 3 of 3 and disjoint from test 3. **Test 3's outcomes were read once, by `tz10b.m2_labels` at 03:56:03 UTC, 19 minutes after its label-free constants were on disk** — 750 of 750 returned, 378 Up. The fit set and test 2 were walked for V4 and no label of either was read; test 1 was formed and not walked. `manifest.json`, `chainlink`, `twap60` and `resolution.json`; **no quote file and no `gamma.json` opened**. Re-derived by the Architect: 807 contiguous slots, the 57 non-members on the grid and inside the span, every member on a weekday |
| TZ-14 | T0 `1789206900` … `1789595400` | 1,296 | **the first 1,200 qualifying slots with `T0 > 1789206600`**: members `1789206900` … `1789595400`, 96 non-members all on `disconnect`, member-list SHA-256 `baa5a9d26855ea7ff07d062437df60617ba3e4e70dd74b3ac455a8a71a9b3154`, Saturday 2026-09-12 09:55 UTC to Wednesday 2026-09-16 21:50 — 428 weekend members, the first scored set to hold a weekend by construction. **Every member is a member of test 1, test 2 or test 3**, whose labels earlier TZs read. **Tier C opened for the first time: all 16,800 replies**, and `gamma.json` of all 1,200; `manifest.json`, `chainlink` and `twap60` through the set rule and `sigma_hat`; `resolution.json` only inside `tz06.qualification`. **No probability computed, no label in any printed number, no statistic of a quote against the pricer.** Re-derived by the Architect: the 1,296 contiguous slots, the weekday split from the grid, every admissible and two-sided count, and the four crossings of its §3.7 item 5 from the fee formula |
| TZ-15 | T0 `1789206900` … `1789595400` | 1,296 | **TZ-14's 1,200, re-formed by `tz14.the_set` unchanged** and asserted by member-list SHA-256 `baa5a9d26855…`, admissible `631` / `628` / `615` / `619` / `621` at `tau` 240 … 60 as TZ-14 measured them. **The first joint statistic of quote and label:** at every admissible checkpoint one share of the side whose ask `p_t` calls cheap after the fee — `405` / `428` / `440` / `380` / `271` selected, 1,924 in all — and **the labels of the 678 members eligible at some `tau`, read once per scored run by `tz10b.m2_labels`, 23 min 48 s after the scoring commit reached `origin`**; member-list SHA-256 `77944a015d4c…`. 12,000 admitted quote reads, `gamma.json`, `manifest.json`, `chainlink` and `twap60`; `resolution.json` inside `tz06.qualification` and in that one read, `1,974` opens a run = `1,296 + 678`. **No file of any interval with `T0 > 1789669800` opened but `manifest.json`**, asserted from the instrument's own audit hook. Re-derived by the Architect: `Up + Down` and `weekday + weekend` equal `n` at 5 of 5 `tau`, the two-sided books `631` / `625` / `558` / `474` / `311`, each half of TZ-14's admissible two-sided reads, and the opens reconciled |
| TZ-17 | — | — | **no capture file opened.** Its input is the venue's own documents over HTTP: 801 settled market documents, largest epoch `1789178400`, `491,400` s below the reserved boundary. Its §0 `find` and `grep` are the host gate's and read no body |
| TZ-18 | T0 `1790116200` … `1790118600` | 9 | **`manifest.json` only — 8 opens**, for G-TIERC's proof and control windows, under the manifest exception below; `1790118600` had no manifest yet when the proof ran. Nothing else under the capture root was opened, each open asserted by the instrument's own guard |

**Tier C has been read twice, for the same 1,200 intervals, and scored once**, by TZ-15. Every quote
after `1789595400` is unread, and every label after `1789669800` as well. **Reserved since 2026-09-19,
and now for TZ-16:** no TZ opens a quote body, a `gamma.json`, a `resolution.json` or a stream of any
interval with `T0 > 1789669800` except TZ-16, Phase 2's decisive gate, and the second look it
pre-registers for any `tau` its first look leaves undecided — both on a sampling rule fixed before any
score of the span exists (§5). TZ-15 read no EDGE, so the confirmation TZ an EDGE would have required
was never triggered; an EDGE either look reads is confirmed on the slots after the second look's last
member, which stay reserved on these terms. `manifest.json` is excepted, because the committed loader
reads every manifest for every set formation and a manifest carries neither a price nor an outcome.
It is the only span of this capture whose quotes and labels no one has seen. **A fifteen-minute
market's settled document is covered too wherever its window overlaps the span:** it carries the
published readings at `T` and `T+900`, which are the reserved five-minute markets' own (§4). The span's
five-minute books are also stored by the chain book, and are reserved there on these terms as well as
on §2.5's.

**Measured footprint.**

| quantity | exact bytes |
|---|---|
| Tier A per interval, TZ-04b | `76,643` |
| Tier A per interval, TZ-05a over four intervals | `58,651` |
| Tier A per day, the figure every projection uses | `22,073,069` |
| Tier C per interval, stored | `6,171.5` mean |
| Tier C per interval, raw | `61,896.5` mean |
| Tier C per interval, raw, **measured by TZ-14 over 1,200 intervals** | `61,971.6` mean — `74,365,905` over 16,800 replies |
| Tier C per interval, stored, measured by TZ-14 | `6,293.6` mean — `7,552,278` gzip over 1,200 files |
| Tier C per day | `1,777,392` |
| Tier A + Tier C per day | `23,850,461` |
| full order book per day, compressed — why it is never captured | `1,913,827,421` |

The two Tier A per-interval figures differ by 23%; the larger is kept in the projection because it
is the conservative one. **Measured against the filesystem by TZ-09 over one hour: `33,632,842`
bytes/day on disk and `26,784,064` apparent.** The projection understates the on-disk cost by
`9,782,381` bytes/day, because every interval directory holds eight or nine small files and the
filesystem rounds each to 4,096-byte blocks. Venue resolution reaches the recorder a median of `318` s after interval
close; the venue's own `closedTime` is a median of `55` s.

**The book, measured by TZ-14 over 1,200 intervals and 16,800 replies.** Complete: 14 reads at every
member, every one HTTP 200 and parseable, no duplicate, no torn line, `quotes_complete` 1,200 of 1,200.
One payload shape of ten keys — `asks`, `asset_id`, `bids`, `hash`, `last_trade_price`, `market`,
`min_order_size`, `neg_risk`, `tick_size`, `timestamp` — and `asset_id` equal to the requested token
at 16,800 of 16,800. **`bids` arrive ascending and `asks` descending, so position 0 is the worst price
on both sides**: a reader takes `max` over bids and `min` over asks, as `tz14.best_of` does. Reads
land `+39.6` to `+391.1` ms after the checkpoint, median about `52` ms, never negative and never timed
out; the reply's own `timestamp` precedes reception by a median of `21` to `27` ms, with a tail to
`1,311` ms; the host clock's worst offset over the set is `33.946` ms. **The book empties toward the
close:** both sides are quoted at `1.0000` of reads at `tau = 240`, `0.9975` at 180, `0.9358` at 120,
`0.8354` at 90, **`0.6050` at 60**, `0.2117` at 30 and `0.0500` at 10 — and no read is empty on both
sides, so at every checkpoint at least one side can be bought. The median spread is one tick at every
`tau`; at the venue's `min_order_size` of `5` the executable touch differs from the quoted one at 53
bids and 51 asks of 11,125 two-sided reads. **The round trip at the touch — spread plus both taker
fees — falls from `4.119` probability points at `tau = 240` to `1.851` at 60**, because the fee falls
as the price leaves 0.5, which is also why the book empties. The two tokens are one book quoted
twice: `mid_up − (1 − mid_down)` is exactly zero from the 0.25 to the 0.90 quantile at every admitted
`tau`, and one executable free lunch after fees appeared in 8,400 paired checkpoints, worth `0.79`
probability points on 90 shares. **Inside the domain the population is about half the set**: 631,
628, 615, 619 and 621 admissible members at `tau` 240 … 60, only 42 to 54 of them weekend, and at
`tau = 60` 311 of the 621 have both sides of the book quoted.

**Feed cadence, measured TZ-06 over 400 intervals:** `chainlink` and `twap60` both publish at
1 Hz — median gap between consecutive reports `1,000` ms on both, over 232,924 and 232,968 gaps,
a median of 584 reports per member per stream. The maximum gap of `34,000` ms is a recorded
disconnect in a neighbouring directory, not a hole in a member's own capture.

**Feed dispersion, measured TZ-07a over the same 400:** pooled over `3,028,021` one-second-grid
increments at fifteen lags, `g(h) = sigma_h^2 / sigma_1^2` rises from 1 at `h = 1` to `1.9561` at
`h = 20`, and is nearly flat above that — `2.2023` at `h = 300`. The rise is complete by twenty
seconds, so it is not an artifact of long extrapolation. Pooled and median-member readings part
company as `h` grows: `2.2023` against `1.3344` at `h = 300`. `10,779` increments were dropped
under the disconnect rule, contributed by 15 members.

**Settlement-quantity dispersion, measured TZ-07b over the same 400:** `1,384,934` admissible
anchors of `1,390,800`, `5,866` dropped by the same imported disconnect rule and by the same 15
members. `Λ(tau)` — the raw uncentred root mean square of `Y / (sigma * sqrt(H(tau)))`, where `Y`
is the settlement average minus the reading in force at the anchor — reads `1.52376` / `1.49602` /
`1.49628` / `1.47915` / `1.44466` / `1.38581` / `1.21118` at `tau` 240 / 180 / 120 / 90 / 60 / 30 /
10. **This is the dispersion of the variable the pricer's `sd` divides, not of a proxy for it**,
and §5 of that TZ froze it into the pricer.

Three diagnostics carry no threshold and are recorded because a question about **shape** now has
its data. The checkpoint-only reading is above the pooled one at every tau — `1.8184` against
`1.5238` at 240 — and the median-member reading below it. `MAD / 0.674490` and `IQR / 1.348980`
agree with each other to the third decimal and sit below `Λ` by 4% at `tau = 240` and 49% at
`tau = 10`. The empirical tails are lighter than the normal's at one `Λ` and heavier at three, at
every tau, and the gap widens monotonically as `tau` falls.

**Shape, measured TZ-10b over the 753 and over the full 800.** `κ = Λ_u / (MAD / 0.674490)` —
the root mean square of the standardized settlement residual divided by its own robust scale. A
normal gives exactly 1. Under the pricer's own causal `sigma`, `κ` reads
`1.1209` / `1.1328` / `1.1875` / `1.2926` / `1.5005` / `1.9753` / `3.2288` at `tau` 240 … 10 over
the intersection, and within 0.02 of that over the full 800 — 2.7 to 3.0 million anchors per
`tau`. The gradient in `tau` is the finding: the link is near-normal four minutes out and is not
a normal at any scale inside the final minute.

**The `sigma` reading is refuted, three ways — TZ-10b M1, M3 and M4 over the same 753.**
Standardizing by `sigma_post`, the successor interval's realised scale — non-causal, and free of
any estimation lag by construction — leaves `κ` **higher** at 7 of 7 `tau`: `2.1908` against
`1.5005` at 60, `2.8957` against `1.9753` at 30. Within deciles of the realised scale error
`log(sigma_post / sigma_hat)` the size-weighted `κ` is at or above pooled at 5 of 7 `tau`, and the
two extreme deciles read `3.449` and `2.655` at `tau = 30`. Four causal regressors fitted on the
intersection's TZ-06 share give `R²` `0.1090` in sample and **`−0.0189`** out. **A scale mixture
collapses when you condition on its mixing variable; this does not.**

**Where the tail lives — TZ-10b M3, deciles of `sigma_hat`, causal.** Within-stratum `κ` is at or
above the pooled value at 7 of 7 `tau`, and it is strongly ordered: at `tau = 30` the lowest
decile of `sigma_hat` reads `3.227` and the highest `1.119`; at 60, `2.611` against `1.077`. **The
heavy tail sits where the causal volatility estimate is smallest**, which is a decision-time
observable and is why TZ-11a carries an admissibility rule rather than only a link.

**`κ` is not stationary between the two windows, and TZ-10b did not measure it per set.** Re-derived
by the Architect from committed diagnostics: TZ-07b's in-sample table puts `κ` on the TZ-06 400 at
`1.042` at `tau = 240` and `1.961` at 10; TZ-08a V9 puts it on the TZ-08a 400 at `1.22` and `5.26`.
Same statistic, two adjacent day-and-a-half windows, a factor of 2.7 apart at `tau = 10`. TZ-11a M3
has since measured it per set, below, and the calendar below says what the two windows were.

**`κ` maps to a degrees-of-freedom, exactly.** For a Student's `t` with `ν` degrees of freedom the
population `κ` is `1.02257` / `1.03497` / `1.07758` / `1.10256` / `1.12223` / `1.15124` / `1.19826`
/ `1.28780` / `1.52734` / `1.92125` / `2.78935` at `ν` 30 / 20 / 10 / 8 / 7 / 6 / 5 / 4 / 3 / 2.5 /
2.2, computed by the Architect at 40 decimal digits and carrying no threshold. Inverted against the
measurements above, `ν` runs `7.06` / `6.59` / `5.19` / `3.96` / `3.06` / `2.46` / `2.14` at
`tau` 240 … 10 over the intersection — and per set, `17.1` against `4.69` at `tau = 240` and `2.47`
against `2.05` at `tau = 10`. **Below `ν = 3` the kurtosis does not exist and below 2 the variance
does not**: that is the quantitative form of §7 item 22, and it is why a root-mean-square scale
constant cannot be the estimator at short `tau`.

**The Student link, fitted by TZ-11a M1 on the fit set alone.** Over the admissible anchors of the
TZ-06 400 — `100,605` at `tau = 240` to `165,369` at 10 — the maximum-likelihood `ν̂` of a symmetric
Student's `t` reads `9.62070` / `13.7083` / `20.2258` / `16.0482` / `9.51490` / `4.79579` / `2.13489`
and `ŝ` `1.30678` / `1.36658` / `1.40748` / `1.37085` / `1.27997` / `1.08185` / `0.643873` at `tau`
240 … 10, all fourteen interior to the search, and the Student `t` beats the best zero-mean normal at
42 of 42 fits across the six populations. `ADMIT[tau]`, the fit set's 30th percentile of
`sigma_hat`, is `2.12324` … `2.18062` USD/s. No label entered any of the three tables.

**Within the domain, the shape transfers from weekday to weekday and cannot be read on the
weekend** — TZ-11a M3. On test 2's admissible members, 231 to 237, `ν̂` lies within a factor of 2 of
`LINK_NU` at 7 of 7 `tau`, `ŝ` within 6.4% of `LINK_SCALE`, and `κ` within `0.041` of the fit set's
admissible value at every `tau`. On test 1's, 28 to 35 members, `ν̂` sits on a search bound at 2 of
7 `tau`, and dropping its single most influential member moves it onto a bound at 4 of 7. **`κ` is
now measured per set** (§7 item 41): over all members `1.0467` … `1.9460` on the fit set, `1.2140` …
`5.2803` on test 1 and `1.1017` … `2.1142` on test 2, at `tau` 240 … 10.

**The calendar under the three sets** — read by the Architect from TZ-11a's own disclosure. The fit
set runs from Thursday 2026-09-10 10:10 to Friday 22:40 UTC, test 1 from Friday 22:45 to Sunday
2026-09-13 10:45, test 2 from Sunday 10:55 to Monday 2026-09-14 23:15. Median `sigma_hat` at
`tau = 240` is `2.774` USD/s on Thursday, `2.562` on Friday, `0.923` on Saturday, `0.918` and `1.257`
on Sunday's two parts and `2.956` on Monday, and `ADMIT` admits 73%, 68%, 8%, 6%, 24% and 78% of
those days' intervals. **Test 1 is the weekend, and every constant this project has seen fail to
transfer — `G_RATIO`, `SD_SCALE`, `κ` — failed between the Thursday–Friday set and the weekend
set.** Whether the regime or the dates carry that is not measured. Test 2's admissible rows are 85%
Monday.

**The TZ-08a set, formed 2026-09-13:** `433` grid slots from `1789166700` to `1789296300`, of
which **400** qualify and 33 fail on `disconnect` — a 92.4% qualifying rate, above the 90% the
projection used. The set is contiguous in wall-clock time, 2026-09-11 22:45 UTC to 2026-09-13
10:45 UTC: about a day and a half. **It is out of sample, and it is the weekend** — a second
volatility regime, which earlier revisions denied without a measurement (§7 item 55).

**Test 2, formed 2026-09-14 23:27 UTC by TZ-11a:** 438 slots from `1789296600` to `1789427700`,
**400** qualifying and 38 failing on `disconnect` — 91.3%.

**Test 3, formed 2026-09-18 by TZ-13 at run time:** 807 slots from `1789428000` to `1789669800`,
**750** qualifying and 57 failing on `disconnect` — 92.94%, the highest rate any set has shown. It
runs from Monday 2026-09-14 23:20 UTC to Thursday 2026-09-17 18:30 UTC: 6 members on Monday, 264 on
Tuesday, 272 on Wednesday and 208 on Thursday — **no weekend**. `ADMIT` admits 514 to 528 members
per `tau`, 68.5% to 70.4% — the fit set's own share by construction of `ADMIT`. **Its outcomes have
been read, and it is never a test set again.**

### 2.4 What is not in the data

**Nothing in the repository is a capture**: there is no Chainlink tick stream, no Polymarket quote,
no order-book depth, no fill and no fee-paid figure in git history, and there never will be.
**Settlement readings are, where an audit route needs them:** TZ-17's report prints the venue's
published price to beat at every boundary of its 200 windows, all below the reserved boundary.

On the host, oracle data and order-book snapshots both exist. **The order book has been aggregated
once, by TZ-14, and scored once, by TZ-15**, over the same 1,200 intervals; every other measurement
compares the Architect's models against either withdrawn labels (§2.2) or the venue's own resolutions,
or — TZ-17 and TZ-18 — the venue's documents against one another. **No fifteen-minute book has ever been
stored** (§2.5).

### 2.5 The fifteen-minute market, and the chain book

**TZ-17's documents.** `/root/tz17-work/raw/` holds 801 settled market documents as the venue served
them on 2026-09-22: 200 `btc-updown-15m-{T}` for the 200 consecutive windows `T` from `1788998400` to
`1789177500`, and the 601 `btc-updown-5m-*` slots from `1788998400` to `1789178400` beneath them, each
named by SHA-256 in TZ-17's committed CSV. **They are byte-stable at the venue:** the Architect
re-fetched all 801 on 2026-09-23 and they hash equal at 801 of 801. The largest epoch is `491,400` s
below §2.3's boundary.

**What they establish** (§4). The fifteen-minute market opening at `T` and the five-minute market
opening at `T` publish the same price-to-beat literal; both families name one resolution source; each
family's outcome agrees with one reading at every shared boundary; and the reading a market settles on,
`finalPrice`, is the next market's `priceToBeat` as the same literal, for both families. **Where the
reading at `T+600` is at or above the reading at `T`, every state that resolves `btc-updown-5m-{T+600}`
Up resolves `btc-updown-15m-{T}` Up**, and symmetrically below — exactly, with no margin to carry.

**The chain book.** Root `/var/lib/btc-chainbook/` on `/dev/vda2`, outside the repository. TZ-18
designed it: for each 900-second window `T`, the documents of `btc-updown-15m-{T}` and
`btc-updown-5m-{T+600}` at `T+605`, then four `/book` reads — both tokens of both markets, four threads
released together — at seven checkpoints from `T+655` to `T+885`, five seconds before Tier C's reads of
the same five-minute market; each reply stored verbatim with its status, byte count, SHA-256 and times,
and a `window.json` at `T+905`. **Deployed on 2026-09-22 at 22:53:36 UTC** as pid `2608993`, from the
copy `/root/tz18-svc/tz18-chainbook-capture.py` at `8caa0b4`, it was **refused by the venue on every
request** for want of a `User-Agent` (§6, §7 item 77): its windows hold two 403 documents each and 28
book entries with status null and reason `no_token_ids`. **No book has been stored.** Its stop was
handed to the Boss on 2026-09-23, because `kill` is refused in the Executor's session; TZ-18a's §0
verifies it from the service's own `stop` record in `runtime.jsonl` and from `/proc`, not from his
report.

**Reserved from its first byte, on Tier C's terms** (TZ-18 §9). Until the TZ that scores it — B2,
written only after TZ-16's first reading is on `main` — no TZ extracts a value from a body stored under
`/var/lib/btc-chainbook/`, a book reply or a market document, and no report prints a price, size,
spread, mid, book level or outcome from one. A deployment proof reads each stored line's status, byte
count, SHA-256 and times, and whether its body parses as JSON, and nothing else. `window.json` and
`runtime.jsonl` carry counts, times and token ids and are excepted. **Every window's five-minute market
is an interval of §2.3's span**, so its bodies are under that reserve as well, and B2 reads a window
only once §2.3's reserve has released that interval — CANON PART II's backup-track rule. Nothing of
this capture enters git history.

---

## 3. Code

| file | role |
|---|---|
| `research/twap-divergence.py` | the collector. Downloads and verifies the monthly archives, walks the 1-second bars, writes one row per checkpoint. The only implementation of the superseded `p_interval` arithmetic. |
| `research/selftest-twap-divergence.py` | its analytic self-tests |
| `research/tz02-distribution.py` | aggregation over the observation set. Reads the Parquet columns only. |
| `research/pfair.py` | **the pricer — the only implementation of the CANON §1.2 model, in any language.** Also the quantities it is fed: the merged stream, the time-weighted step-function mean, the one-second grid, the realised-sigma estimator, `settlement_mean`. Since `26bbb61` it carries `SD_SCALE` and `corrected_sd` — **the TZ-07b scale: one measured literal per tau, `10` included, and an unmeasured tau raises.** `G_RATIO` is removed rather than kept alongside; `c44af68` holds it in history. Imports its reader from `analyze.py` and carries no reader of its own. **Since `2746518` it also carries the Student link:** `log_t_cdf` and `t_cdf`, computed through a log-space regularized incomplete beta, `student_sd`, `p_fair_student`, and the three TZ-11a tables `ADMIT`, `LINK_NU` and `LINK_SCALE`, one literal per `tau`, `10` included; an unmeasured `tau` raises. `log_t_cdf` agrees with an independent 60-digit reference to `3e-13` relative for `\|z\|` from `0.01` to `200` at fourteen `ν` in `[2.05, 60]`, checked by the Architect; below `\|z\|` of about `1e-7 * sqrt(ν)` it returns exactly `0.5`, an error under `1e-7` in probability. |
| `research/selftest-pfair.py` | its analytic self-tests — **116 asserts since PR #12**: 56 model checks, 18 machinery checks, the 30 TZ-07b checks, TZ-10b's 6 `log_phi` checks and TZ-11a's 6 Student-link checks, every fixed expectation at `K = 100000.25` and `sigma = 3.25`. The four TZ-07a checks that encoded the superseded composition were deleted with it, none of them failing at the time. 116 of 116 reproduced by the Architect on a second machine |
| `research/tz06-calibration.py` | the Phase 1 pipeline: set formation, P, V1–V10, the gate tables. Carries no formula; calls `pfair.py` for every one. Since `1b8e4a7` `scoring_set` and `build` take `after` and `need`; at their defaults the run is the one TZ-06 ran, asserted by TZ-08a V1 to every digit of all six `Brier` values. |
| `research/tz07a-variance-time.py` | the variance–time instrument: the fifteen-lag curve, M6's disconnect rule, the in-sample diagnostics, the `gamma.json` key read. Its `G_RATIO` cross-check is removed; its `--emit-g` path still prints a table the pricer no longer has a place for. Since `2746518` `log_likelihood` and `lambda_hat` take `log_cdf=None`; at the default the committed `Φ` path runs unchanged, asserted by TZ-11a V4 to ten decimals. |
| `research/tz07b-settlement-dispersion.py` | the settlement-dispersion instrument: `Y(a, tau)` at every admissible anchor, the `Λ` table and its diagnostics, and the per-tau assert that the literal in `pfair.py` equals its own measurement to six significant digits. Imports M6's rule from `tz07a-variance-time.py` rather than reimplementing it, and opens no settled document. |
| `research/tz08a-out-of-sample.py` | the out-of-sample driver: the set assertions, the corrected and uncorrected gate tables, the scale statistic, the observations file. **Carries no threshold of its own** — G1 and G2 come from `tz06-calibration.py`, the scale statistic from `tz07a-variance-time.py`, the dispersion from `tz07b-settlement-dispersion.py`, and G3 is judged by the Architect. |
| `research/tz09-disk-inventory.py` | the disk inventory instrument: the `df` and `du` reads, the rate inventory, the unlinked-open enumeration, capture and log accounting, and R1's hash enumeration. **It cannot delete** — no deletion API occurs in it, and every `subprocess` call is a fixed argv of `df`, `du`, `git` or `journalctl --disk-usage`, with no shell. |
| `research/tz10b-sigma-or-link.py` | the sigma-or-link instrument: the intersection, `sigma_post`, `κ` through `shape`, the decile strata and the out-of-sample regression — and the helpers later instruments import: the host reads `free_bytes`, `recorder_pids`, `newest_start`, `read_set`, the grid readers `grid_of` and `sigma_hat_of`, and the label reader `m2_labels`. |
| `research/tz11a-student-link.py` | the Student-link instrument: the three sets, the member walk `walk_member`, the profile-likelihood fit of `ν` and `s` by nested golden section `fit_student`, M2's domain, the per-set refits, M4's scoring through `tz06.table_for` and `tz07a.lambda_hat(pairs, log_cdf)`, M5 and V2 … V12. **Carries no threshold of its own**; the Student likelihood and its search live here and in no other file. |
| `research/tz12-sized-gate.py` | **the sized-gate instrument, and the gate itself.** The member bootstrap of `log ν̂` and the two frozen literals `SIGMA_LOG_NU` and `SIGMA_LOG_NU_CENSORED`; the null and alternative label draws from the pricer's own `p_t`; the λ grid and `grid_lr`; `k2_of`, `crit_of`, `g4_power`, `g4_constants`, `constants`, `readings` and `verdict` — the four gates TZ-13 applies, with their error rates. **Carries no threshold of its own beyond what §4 of that TZ fixes**, reads no label, and keeps the loaded `tz11a` module so a later TZ can call §4 from it. |
| `research/tz13-sized-gate-test3.py` | **the sized gate applied once, to test 3.** Forms the set through `tz06.scoring_set`, walks it through `tz11a.walk_member`, sizes every gate through `tz12.constants` from the pricer's own predictions and writes the constants to disk, projects power at 2× and 3× the admissible rows, then reads outcomes once through `tz10b.m2_labels` and applies `tz12.readings` and `tz12.verdict` unchanged; §4's two further G4 clauses and §4.3's band are applied after, and can only weaken. **Carries no threshold of its own.** Its one departure from a committed call is the projection's synthetic `T0` keys (§7 item 61), in a table barred from every gate. |
| `research/tz14-quote-inventory.py` | **the quote inventory, and the quote machinery every later TZ imports.** `the_set` re-forms TZ-14's set with every assertion; `quote_lines` reads one quote file as the recorder wrote it, `raw` included, located by `manifest._stream_path`; `book_of` parses a reply into `Decimal` levels; `best_of` and `touch_of` give the quoted and the executable touch without depending on order; **`fee_pp` is the only implementation of CANON §1.1's taker fee**; `documents` maps token to outcome from `gamma.json`. Computes no probability. **Importing it has three side effects a later TZ names:** it writes the three thread-count environment variables; it loads `tz12-sized-gate.py`, so a later TZ takes `tz12` and everything below it from `tz14` rather than loading any of them again; and it **installs an audit hook that records the basename of every open under the capture root for the life of the process and cannot be removed** — it only appends to `tz14.CAPTURE_OPENS`. `tz14.v1_gates` asserts revision `2026-09-18-b` and twenty `frozen` rows, and no later TZ calls it. |
| `research/tz15-phase2-gate.py` | **The Phase 2 gate, on `main` since `8d2a4c6`.** Re-forms TZ-14's set through `tz14.the_set`, takes `p_t` from `tz11a.checkpoint_row` and each touch from `tz14.touch_of` at the reply's own minimum size and tick, and `select`s one share per admitted checkpoint — the larger after-fee edge, strictly positive, a tie to `Up`, the fee through `tz14.fee_pp`. **`pb_upper` is the exact Poisson-binomial upper tail**, a `Decimal` recursion at 60 digits, and `crit` its smallest critical count; both agree with an independent enumeration in rational arithmetic, and `select` with an independent re-implementation, at 0 disagreements, checked by the Architect. The labels are read once, through `tz10b.m2_labels`, behind a push check and a ledger. **Carries no threshold of its own beyond TZ-15 §4**, and its `reading` is §4's table, which §7 item 69 retires: a later TZ imports the tail, the selection and the guards, never `reading`. |
| `research/tz17-settlement-chain.py` | **the settlement-chain instrument, and the only committed request outside the recorder that the venue's edge serves.** Stage F fetches the venue's own market documents from the public Gamma path, paced at `0.5` s with a retry ladder, stores each body verbatim with its SHA-256 and stops at the 200th qualifying candidate; Stage A computes I1–I3 and D1–D7 from the stored bodies alone. Standard library only; imports nothing from the repository. Its request carries `Accept: application/json` and `User-Agent: btc-5m-twap-tz17` (§6). Its retry, fail-fast and early-stop paths ran only in its self-tests. |
| `research/recorder/recorder.py` | the live capture, Tier A and Tier C in one process. Read-only: no order path, no CLOB authentication, no credential, no pricing arithmetic. |
| `research/recorder/config.py` | every constant the capture uses, each traced to the TZ that fixed it |
| `research/recorder/manifest.py` | the per-interval manifest, a pure function of the interval directory |
| `research/recorder/analyze.py` | the TZ-04b analyzer and the only stream reader — `reports`, `last_at_or_before`, `first_at_or_after`, `venue`, `published_equal`, `scoring_set`. Repaired by TZ-06 R-c; runs. |
| `research/recorder/probe.py` | the Tier B order-book probe, run once |
| `research/recorder/selftest.py` | the recorder's self-tests — 115 asserts, each aborting the run |

**`research/tz18-chainbook-capture.py` is not on `main`.** It exists only as PR #18's head `8caa0b4`,
1,420 lines, 57,409 bytes, SHA-256 `33753b2bb1e322a081e6cba8bad976268e2d6046dc350e6ceae3e748ad6e4bfe`,
closed unmerged (§7 item 77), and as the copy `/root/tz18-svc/tz18-chainbook-capture.py` its service
ran. No row of §0 carries it, and none will until a corrected file is merged.

Outputs go to `research/out/**`, git-ignored except `twap-divergence-summary.md` and
`twap-divergence-contamination.md`. **`/root/tz01-out-archive/`, `/root/tz06-work/`,
`/root/tz07-work/`, `/root/tz07b-work/` and `/root/tz08a-work/` no longer exist** — TZ-09 R4
reclaimed all five, `163,987,456` bytes recovered. Everything a committed artifact names by hash was
copied first into **`/root/btc-forensics/`**: 91 files, each verified equal at source and
destination by SHA-256. The two per-observation files are there —
`tz06-work--tz06-observations.csv`, 2,801 lines, `843,788` bytes, SHA-256
`4e20c4fafbe60fe64c48ce1833a8da55f7fce2c0bad87e93b55ba95a2a4f85bb`, and
`tz08a-work--tz08a-observations.csv`, 2,801 lines, `1,066,357` bytes, SHA-256
`b810b07165e98b29258479323a0c634ccaea1917135a3336b8d28fb4bb92fa77` — both still outside the
repository and re-derivable from the pipeline. **What was not preserved:** 23 of the 24
`partitions/` files and all 24 `state/` files of the superseded TZ-01 output, which that report
names only by one hash over each whole set. See §7 item 31.
**`/root/tz04a-env/` is the interpreter the running recorder executes from, and
`/root/btc-forensics/` is the preserved evidence TZ-09 R3 copied out before R4. Neither is scratch
and nothing may remove either.**
**TZ-11a §9 copied 47 more files into `/root/btc-forensics/`, making 141.** **TZ-12 §9 copied 50
more, making `191`**, the 141 already there hashing unchanged, and then removed the three remaining
git worktrees — `/root/tz11a-work/wt`, `/root/tz09-work/wt` and `/root/tz09-work/wt-report`, one
`git worktree remove` each, never `--force`, none refused — and reclaimed **`/root/tz09-work/`** and
**`/root/tz11a-work/`**, each verified gone by `test -e`. The second of the two was refused by the
session's permission classifier in its single-tree form, which had not happened before; the Boss ran
the one-line block and the Executor verified the outcome from `test -e`, not from his report.
**TZ-13 §9 copied 6 more, making `197`**, the 191 already there hashing unchanged; it removed the
worktree `/root/tz12-work/wt` by `git worktree remove` without `--force`, and the session's classifier
refused `rm -rf /root/tz12-work`, one tree, as it had for TZ-12. **The Boss ran the handed block on
2026-09-18 and reported `GONE`; TZ-14's §0 verifies that by `test -e`, not from his report.**
**TZ-14 §9 copied 8 more, making `205`**, the 197 already there hashing unchanged — six TZ-13 outputs
and two files of its worktree, matched by any 16-to-64-hex token a committed report prints; it removed
`/root/tz13-work/wt` by `git worktree remove` without `--force` once two untracked `__pycache__`
directories no report names were deleted, and **`rm -rf /root/tz13-work` was not refused** by the
session's classifier this time, exit 0, verified by `test -e`. `/root/tz12-work` was verified gone by
`test -e` at TZ-14 §0.7, and `/root/tz13-work` at TZ-15 §0.7.
**TZ-15 §9 copied 6 more, making `211`**, the 205 already there hashing unchanged — four TZ-14 outputs
and two files of its worktree, by TZ-14's predicate; it removed `/root/tz14-work/wt` by `git worktree
remove` without `--force`, exit 0 at the first attempt, and the session's classifier refused
`rm -rf /root/tz14-work`, one tree, as it had for TZ-12 and TZ-13 and had not for TZ-14. **The Boss
ran the handed block on 2026-09-19 and reported `exit=1`, and TZ-17's §0 verified it by `test -e`,
exit `1`, on 2026-09-22.** **`/root/tz15-work/`** — the worktrees `/root/tz15-work/wt` and
`/root/tz15-work/wt-report`, the run directories and the label ledger — is TZ-16's to reclaim after
copying what TZ-15's report names by hash; TZ-16 reads two of its files first, `tz15-constants.json`
at `e6a93f9371e9…` and `tz15-observations.csv` at `a7ac8a495e00…`. The worktrees registered at
TZ-18's end were seven: the primary checkout `/root/btc-5m-twap`, `/root/tz15-work/wt` and
`/root/tz15-work/wt-report`, `/root/tz17-work/wt` and `/root/tz17-work/wt-report`, and
`/root/tz18-work/wt` and `/root/tz18-work/wt-report`.
**`/root/tz17-work/`** — 801 bodies under `raw/`, `index.jsonl`, `refetch/`, `scratch/` with a pre-run
probe and three harnesses, `run-1/`, `run-2/`, both worktrees and an untracked `research/__pycache__/`
inside `wt` — is TZ-18a's to reclaim once nothing TZ-18a runs reads it, after copying into
`/root/btc-forensics/` every file whose SHA-256 a committed report prints, by TZ-14's predicate: the
bodies, by TZ-17's CSV, and `tz17-candidates.csv` and `tz17-summary.json`, by TZ-17 §2.11 and §2.12.
**`/root/tz18-work/`** — both worktrees, `run-1/` to `run-3/`, `predebug/` and the Executor's diagnostic
scripts — is TZ-18a's to reclaim after it has named the diagnostic slug from those scripts; the TZ-18
report prints no hash of any of its files (§7 item 77). **`/root/tz18-svc/` is not scratch** while any
service runs from it, and no TZ removes it before the stop is verified.

---

## 4. What is validated, and by what

| claim | established by | status |
|---|---|---|
| the venue settles on a trailing-TWAP comparison — the 60-second feed at the close against the same feed at the open | TZ-04b V2: R1 agrees with the venue's resolved outcome on **200 of 200**, against a 199-of-200 gate fixed before any data was seen; re-run by TZ-06 R-c and reproduced exactly | **stands.** The only artifact here validated against a Polymarket settlement rule. |
| the interval-average reading is wrong, and so is the pre-August snapshot reading | TZ-04b V2: R2 175 of 200, R3 181 of 200; both reproduced by TZ-06 R-c | **stands.** Wrong on one interval in eight and one in ten — not near-misses. |
| the price to beat equals the settlement feed's reading at the open | TZ-04b V1 198 of 200; TZ-06 V3 **396 of 400**, median residual 3.78e-12 USD, worst 25.49 USD | **stands, with a ~1% failure rate every later result carries.** |
| the causal reading is genuinely causal | TZ-01a perturbation test; TZ-06 V4: 140 of 140 bit-identical under perturbation of the entire future, 140 of 140 negative controls move the model output; TZ-07a V2 repeats it on the corrected pricer, 120 of 120 and 120 of 120 | **stands.** |
| the oracle feed supports reconstructing the settlement average | TZ-06 P: the reconstructed close TWAP agrees in sign with the venue's outcome on **397 of 400**, against a floor of 396 fixed before any data was seen | **stands as a precondition.** Median absolute residual against the venue's own report `0.53` USD, worst `11.87`. |
| the Phase 1 pipeline reproduces on a later day and a different process | TZ-07a V4: `tz06-calibration.py` unmodified, six of six `Brier` values reproduced to all six decimals, P at 397 of 400 | **stands** |
| `p_fair` is not disqualified by the TZ-06 gate | TZ-06: G1 6 of 6, `Brier` 0.2107 … 0.0105 against 0.2496; G2 0 failing bins of 34 eligible | **stands as stated and for nothing more.** Phase 1 can only disqualify; it did not. |
| **`p_fair` is overconfident at `tau >= 120`** | Architect's audit of TZ-06's tables, then TZ-07a's own `λ̂`: **1.5220 / 1.4155 / 1.4139** at `tau` 240 / 180 / 120, and 1.1260 / 1.1368 / 1.4027 at 90 / 60 / 30 | **stands as a finding.** In-sample and post-hoc; it closes nothing. |
| **the oracle feed's variance grows faster than the lag** | TZ-07a M1, V1: fifteen lags, `3,028,021` increments, 400 members — `g(20) = 1.9561`, `g(300) = 2.2023` | **stands as a measurement of the feed** and of nothing else. |
| the TZ-07a correction over-widens `sd` below `tau = 120` | Architect's audit of TZ-07a §2.5: corrected `λ̂` 1.0301 / 0.9688 / 0.9846 at 240 / 180 / 120 but 0.8070 / 0.8128 at 90 / 60 and 1.4027 at 30 | **SUPERSEDED by TZ-07b.** `G_RATIO` is out of the pricer; this finding is why. Items 19 and 20 are closed. |
| **the dispersion of the settlement quantity, measured on the variable the `sd` divides** | TZ-07b M1, V1: `1,384,934` anchors of `1,390,800` over the 400 TZ-06 members at seven taus, `Λ` frozen into `pfair.py` as seven literals, each asserted against the measurement before anything was printed | **stands as a measurement of the feed.** Tested out of sample by TZ-08a V8, and it does not transfer — see the rows below. |
| the corrected pricer is causal and the pipeline still reproduces | TZ-07b V2 120 of 120 bit-identical under perturbation and 120 of 120 negative controls; V3 two full runs byte-identical; V4 TZ-06's six `Brier` values to all six decimals with P at 397 of 400, and TZ-07a's fifteen pooled `g(h)` to six significant digits | **stands** |
| **`p_fair` passes G1 and G2 out of sample** | TZ-08a on a disjoint 400: G1 6 of 6, smallest margin `0.047` at `tau = 240`; G2 **0 failing bins of 39 eligible** against an allowance of 2. The uncorrected pricer on the same set fails **7 of 36** | **stands.** Re-derived by the Architect: all 79 eligible bins reproduced in exact integer arithmetic, region and verdict, and the member list rebuilt from the disclosure table to the same SHA-256. It confirms nothing — Phase 1 can only disqualify. |
| **`p_fair` FAILS G3 out of sample, at `tau` 60 and 30** | TZ-08a's scale statistic, judged by the Architect against TZ-07a §8's `\|λ̂ − 1\| <= 0.15`: `λ̂` = 0.8629 / 1.1397 / 1.0291 / 1.0122 / **1.2949** / **2.0418** at 240 / 180 / 120 / 90 / 60 / 30 | **PHASE 1 ANSWERS NO.** §8: any one of G1, G2, G3 violated closes it. 240 and 180 pass with 0.013 and 0.010 to spare, which is not a margin on 400 observations. |
| the pre-registered prediction of item 22 is **refuted** | it predicted 0.999 / 0.946 / 0.945 / **0.761** / **0.787** / 1.012 and a failure at 90 and 60 with `λ̂` below 1. Observed: a pass at 90, and failures at 60 and 30 with `λ̂` above 1 | **the prediction failed, and how it failed is the finding.** It assumed the uncorrected `λ̂` is stable out of sample. It is not: 1.522→1.315, 1.416→1.705, 1.414→1.540, 1.126→1.497, 1.137→**1.871**, 1.403→**2.830** between two adjacent day-and-a-half windows. |
| **the two scale measurements point in opposite directions** | TZ-08a V8 ran the TZ-07b instrument unmodified on the new 400: `Λ_oos / SD_SCALE` = 1.046 / 1.019 / 0.929 / 0.913 / 0.910 / 0.913 at 240 … 30 | **stands as a measurement.** The RMS says narrow the `sd` by ~9% at short `tau`; `λ̂` says widen it by 29% at 60 and by 104% at 30. No constant per `tau` satisfies both: they are two functionals of a distribution that is not the assumed one. |
| **the settlement residual is not Gaussian, and less so the smaller `tau` is** | TZ-08a V9 on the same 400: `P(\|r\| > 3Λ)` = 0.0125 / 0.0085 / 0.0106 / 0.0158 / 0.0219 / 0.0268 / 0.0253 at 240 … 10, against the normal's 0.0027 — **8 to 10 times the normal tail below `tau = 90`** — while `MAD / 0.674490` sits 18 / 22 / 30 / 41 / 56 / 71 / 81 per cent below `Λ` | **stands, and it is why G3 failed.** A sharp centre with a heavy tail is not a normal at any scale. Item 22 suspected this in sample; out of sample the gap is roughly twice as wide. |
| **`λ̂` at `tau = 30` is carried by one observation** | Architect's arithmetic over TZ-08a §11 item 1: at `T0 1789268400` the feed moved about 40 USD in the final 30 s, `z = −10.819`, `p_fair` exactly `0.0`, and the venue resolved Up. That single point gains **+45.2** log points between `λ = 1` and `λ̂ = 2.0418`; the other 399 **lose 14.7** | **stands as a finding about the estimator and about the tail.** `Φ` assigned about 1e-27 to something that happened once in 400. Without that point the maximiser is below 1 — which does not rescue the gate, and is not a reason to drop it. |
| **the heavy tail is not a lagging `sigma`** | TZ-10b M1 and its §4.1 reading: `sigma_post`, the successor interval's realised scale, leaves `κ` higher at 7 of 7 `tau`. `f`, the share of the excess it removes, is **−1.3793** at `tau = 60` and **−0.9437** at 30; re-derived by the Architect at 7 of 7 | **stands.** The pre-registered prediction was 0.5–0.7 and 0.6–0.8. It failed, and the sign is the finding. |
| **conditioning on the realised scale error does not remove it either** | TZ-10b M3: within deciles of `log(sigma_post / sigma_hat)` the size-weighted `κ` is at or above pooled at 5 of 7 `tau`; the extreme deciles read `3.449` and `2.655` at `tau = 30` against `1.9753` pooled | **stands, and this is what closes the question.** Not M1 and not `f`: this is the test a scale mixture must pass and does not. |
| **the scale error is not forecastable from causal inputs** | TZ-10b M4: four causal regressors, fitted on the intersection's TZ-06 share and evaluated on its TZ-08a share against the in-sample mean — `R²` `0.1090` in sample, **`−0.0189`** out | **stands.** No model adopted, and this closes the repair-by-better-`sigma` route for those regressors. |
| **the heavy tail sits in the low-`sigma_hat` deciles** | TZ-10b M3, causal stratifier: `κ` `3.227` in decile 1 against `1.119` in decile 10 at `tau = 30`; `2.611` against `1.077` at 60 | **stands, and it is observable at decision time.** TZ-11 turns it into an admissibility rule. |
| the TZ-10b instrument is causal and reproduces what it must | V2 140 of 140 bit-identical and 140 of 140 controls, perturbed strictly after the checkpoint; V4 TZ-07b's `Λ` at 7 of 7 and TZ-08a V8's six ratios at 6 of 6; V3 three outputs byte-identical over two runs; V6 `SD_SCALE`, `corrected_sd`, `phi` and `state` byte-identical | **stands.** All three member lists rebuilt by the Architect from the report's own disclosure: 3 of 3. Nothing was re-fitted. |
| **`g`, TZ-10b §4.2's second reading, is not evidence** | Architect's audit: its denominator is `\|λ̂ − 1\|`, which is `0.0013` at `tau = 120` and sends `g` to `−122`; at `tau = 30` it reads `0.2115` against a `0.20` boundary and becomes `0.6574` once the single most influential observation is removed | **WITHDRAWN as a reading.** The verdict rests on `f` and on M3, both anchor-level. See §7 item 40. |
| **the settlement residual is Student-shaped, and within the domain the shape transfers from weekday to weekday** | TZ-11a M1 and M3: the Student `t` beats the best normal at 42 of 42 fits; on test 2's admissible members `\|log(ν̂ / LINK_NU)\| <= log 2` at 7 of 7 `tau` and `κ` within `0.041` of the fit set's | **stands as a measurement of the feed**, over 83,000 to 139,000 anchors per `tau` on test 2. Test 2's admissible rows are 85% Monday: weekday to weekday is all it shows. |
| **the Student pricer is closed by its own gate** | TZ-11a §4: G1 7 of 7 on both sets; G2 0 failing on both — **of 0 eligible on test 1**; G3 fails at `tau` 240, 180, 30, 10 on test 1 and at 90, 60 on test 2; G4 fails at 120, 90, 60, 30 on test 1. Re-derived by the Architect: 110 eligible bins in exact integers, every G1, G3 and G4 comparison, and M5 to the last digit | **stands as the verdict TZ-11a §4 fixed, and is not re-judged.** The pre-registered prediction was right on the answer and wrong on the mechanism: G4 held at `tau = 240` on both sets and failed at mid and short `tau` on test 1. |
| **G3, as written, cannot tell a calibrated pricer from a miscalibrated one on these populations** | Architect's audit: labels drawn from the pricer's own `p_t`, the report's bin tables standing in for its rows — an approximation that reproduces the reported `λ̂` to within `0.12` — at 4,000 replicates per population. With the pricer exactly right, G3 fails a given `tau` with probability `0.19` to `0.35` at `tau` 240 … 60, `0.52` at 30 and `0.71` at 10 on test 2's admissible rows, `0.67` to `1.00` on test 1's, and `0.09` to `0.74` even over all 400; some `tau` fails with probability at least `0.71` on every population scored. On test 2 the seven Student likelihood-ratio p-values run `0.019` to `0.85` | **stands as a finding about the gate, not about the pricer.** The TZ-11a closure is procedural: it shows the Student pricer neither miscalibrated nor calibrated. TZ-12 measures the same thing exactly. See §7 item 49. |
| **the gate's own error rates, measured exactly** | TZ-12 M2: 20,000 null replicates per population, labels drawn from the frozen pricer's own `p_t`, 14 populations. Old G3 fails an exactly correct pricer at `0.345` / `0.247` / `0.224` / `0.259` / `0.337` / `0.620` / `0.703` at `tau` 240 … 10 on test 2's admissible rows and at `0.684` to `1.000` on test 1's; some `tau` fails with probability at least `0.703`, and `0.979` under independence across `tau`. Old G1 fails at `0.0985` at `tau = 240` on test 1 and at 0 of 20,000 everywhere on test 2. Old G2 has 0 eligible bins at every gated `tau` on test 1 | **stands, and it closes the measurement half of §7 item 49.** Re-derived by the Architect from the report's own null tables: every `k2` of 7, the six-`tau` convolution `0.000080`, `1 − Π(1 − f)` = `0.9788`, and the 24 eligible bins equal TZ-11a's committed 24. The audit approximation that raised item 49 is confirmed — it said 0.19–0.35 at `tau` 240 … 60 and about 0.71 at 10 against 0.224–0.345 and 0.703 measured, and understated `tau = 30` (0.52 against 0.620). |
| **why the old G3 failed: the scale estimate runs to the edge** | TZ-12's diagnostic: the null `λ̂_grid` sits on the grid's lower bound `0.5` in `43%` of replicates at `tau = 10` on test 2 and `96%` on test 1, against 0 at `tau` 240 … 90 on test 2 | **stands.** With no confident prediction contradicted there is nothing to hold the maximiser, which is the mechanism item 49 named and this measures. |
| **TZ-11a's G4 failures on the weekend at `tau` 60 and 30 survive sizing** | TZ-12 M2's normal approximation to the old G4: false-failure `0.6279` / `0.5304` / `0.5629` / `0.3760` / **`0.0171`** / **`0.0002`** / `0.0000` at `tau` 240 … 10 on test 1. Re-derived by the Architect at 14 of 14, and the bootstrap has no bound hit at 60 or 30, so the spread constant there is uncensored | **stands as the one TZ-11a gate verdict that is signal rather than gate noise.** The tail index did not transfer to the weekend at short `tau`. The same TZ's G4 failures at 120 and 90 are not evidence: a correct pricer fails there 56% and 38% of the time. |
| **the sized gate admits at most two horizons on a 400-slot set** | TZ-12 M3 on test 2's 231 to 237 admissible members: G3's power against a 1.5× overconfidence is `0.2780` / `0.4990` / `0.6255` / `0.6180` / `0.4785` / `0.1645` / `0.0180` at `tau` 240 … 10, so only 120 and 90 clear the `0.5` floor. G1 could pass at 7 of 7, `P0` 0 of 20,000. G4 has power only at 60 and 30; `tau = 10` is censored and reads UNDECIDABLE | **stands, and it is why test 3 is 750 slots and not 400.** All 14 `c4`, 14 `s` and 14 `P4` re-derived by the Architect, and `Z4` = `Φ⁻¹(1 − 0.00125)` and `U_BOOT` = `sqrt(23 / χ²₀.₁₀(23))` to 15 digits; the family-wise Bonferroni total is `0.048` exactly. At 2,000 power replicates `tau` 180 and 60 lie inside one Monte Carlo standard error of the floor (§7 item 56). |
| **`SIGMA_LOG_NU`, the member-bootstrap spread of `log ν̂`, on the fit set alone** | TZ-12 M1: 24 refits of the 280 admissible fit members per `tau` — `0.476750` / `0.338445` / `0.361253` / `0.236061` / `0.0876792` / `0.0557673` / `0.0326229`, `tau = 10` censored at 7 of 24 refits on the search's lower bound | **stands as a measurement of the fit, with one caveat re-derived by the Architect:** at `tau` 240 and 120 the largest replicate sits on the search's **upper** bound `60` and carries `53%` and `33%` of the variance, which inflates the constant and widens G4 where G4 has no power anyway (§7 item 57). No verdict moves either way. |
| **test 1 is the weekend, and the absolute domain rule turns the pricer off there** | the Architect's reading of TZ-11a's disclosure against the calendar: median `sigma_hat` `0.92` USD/s on Saturday against `2.56` to `2.96` on Thursday, Friday and Monday; `ADMIT` admits 6% to 8% of weekend intervals | **stands as a fact about the three sets.** That the regime rather than the dates drives the non-transfer of every earlier constant is a hypothesis, not a measurement. |
| **the Student pricer is NOT DISQUALIFIED at `tau` 240, 180, 120, 90 and 60 under the sized gate** | TZ-13, applied once to test 3's 514 to 528 admissible members per `tau` — a Tuesday–Thursday set no one had scored — with every constant on disk before any outcome was read: G1 PASS at 7 of 7, `P0` 0 of 20,000 and `P1` 1.0000; G2 0 failing bins at every `tau` against `k2` 2 or 3; G3's likelihood ratio at most `6.230197` against `crit3` `7.087974` to `9.504963`, PASS with `P3` 0.6890 / 0.9295 / 0.9755 / 0.9675 / 0.9090 at 240 … 60; no G4 FAIL anywhere; §4.3's band at 0 of 21. `tau` 30 and 10 read UNDECIDABLE on G3's power, 0.3230 and 0.0495. Re-derived by the Architect: every `k2` from the null tables, all seven `s`, `c4` and `P4` from `SIGMA_LOG_NU`, `Z4` and `U_BOOT` at 40 digits, every gate reading and the verdict at 7 of 7 | **stands — Phase 1 does not disqualify the Student pricer at five `tau`, inside its domain, on weekday data.** It confirms nothing: Phase 1 can only disqualify. It admits those five `tau` to Phase 2 and to nothing else. |
| **at `tau` 90, 60 and 30 the Student pricer leans under-confident on test 3** | TZ-13: `λ̂` 0.8844 / 0.7436 / 0.6855 under the Student log CDF, likelihood ratios 1.906 / 6.230 / 3.135 — asymptotic χ²₁ p-values 0.17 / 0.013 / 0.077, none near the family bound — and 0.8559 / 0.6815 / 0.5979 without the single most influential member. G3's power against λ = 1/1.5 is 0.6500 at 60 and 0.0850 at 30. The residual scale points the other way: `ŝ` sits 2.5% to 3.1% above `LINK_SCALE` at 90 … 30 | **stands as a finding, not a failure.** The probability scale and the residual scale disagree in direction at short `tau`, as the normal link's did in TZ-08a V8, and which one describes the sign of the outcome is not measured. **A market quoting more confidently than `p_t` at these `tau` is not, by that fact, mispricing.** |
| **the Student shape holds on a third weekday set at `tau <= 120`** | TZ-13 on test 3's admissible members: `\|log(ν̂ / LINK_NU)\|` 0.076 / 0.061 / 0.088 / 0.093 / 0.034 at `tau` 120 … 10, every fit interior, and `ŝ` within 3.1% of `LINK_SCALE` there. At 240 and 180 `ν̂` reads 30.0 and 37.0 against 9.62 and 13.7, and dropping one member sends it to the search's upper bound 60 at 240 | **stands as a measurement of the feed.** At long `tau` the residual is near-normal and `ν` is not identified; G4 has had no power there on any set read. |
| **what the sized gate sees on 750 weekday slots** | TZ-13 §3.3 and §3.6: G3's power reaches the 0.5 floor at `tau` 240 … 60 and not at 30 or 10; G4's `P4` is below it at 240 … 90 at every multiple to 3×. Repeating test 3's admissible rows, `tau = 30` reaches the floor at 2×, `P3` 0.7095, and `tau = 10` does not at 3×, 0.1235 | **stands as a measurement of the instrument**, barred from every gate. `tau = 30` needs about 1,050 admissible members, about 1,600 slots considered at weekday rates; `tau = 10` is out of reach at any set this capture affords. |
| Tier C captures the book at seven checkpoints without loss | TZ-05a: 56 of 56 reads at HTTP 200, 4 of 4 `quotes_complete`; **TZ-14: 16,800 of 16,800 over 1,200 intervals**, 14 lines at every member, no duplicate, no torn line, `quotes_complete` 1,200 of 1,200 and equal to its recomputation; `manifest._quote_reads` and the instrument's own reader equal at 1,200 of 1,200 | **stands as a fact of the capture.** |
| the `/book` reply puts the worst price first | TZ-14 §3.5 item 2: `bids` ascending at 13,561 sides and `asks` descending at 13,563, never the reverse; 401 and 400 single-level, 2,838 and 2,837 empty | **stands.** A reader takes `max` over bids and `min` over asks, never position 0. |
| **the book empties as the close approaches** | TZ-14 §3.5 item 3: both sides quoted at `1.0000` / `0.9975` / `0.9358` / `0.8354` / `0.6050` / `0.2117` / `0.0500` of reads at `tau` 240 … 10; no read empty on both sides | **stands.** Re-derived by the Architect: the per-`tau` empties sum to the ordering table's 2,838 and 2,837, and every two-sided count and share at 7 of 7. |
| the executable touch is the quoted touch at the venue's minimum size | TZ-14 §3.6: `min_order_size` `5` at 16,800 of 16,800; `bid5` differs from the best bid at 53 and `ask5` from the best ask at 51 of 11,125 two-sided reads | **stands.** The per-`tau` split the report prints beside it sums to 102, not 104 (§7 item 67). |
| **the venue's fee schedule is CANON §1.1's** | TZ-14 §3.8: `feeSchedule` `{'exponent': 1, 'rate': 0.07, 'takerOnly': True, 'rebateRate': 0.2}` and `feeType` `crypto_fees_v2`, identical at 1,200 of 1,200 `gamma.json` | **stands — the first confirmation from the venue's own document**, beside TZ-05a's read of `/markets/{condition_id}`. |
| **the tick is not a constant of the interval** | TZ-14 §3.5 item 6 and §3.8: the `/book` `tick_size` is `0.01` at 15,640 replies and `0.001` at 1,160, while `gamma.json` at `T0 + 5` carries `orderPriceMinTickSize` `0.001` at 2 of 1,200 members | **stands, and it corrects §6's TZ-05a row**, which recorded three sources agreeing at one instant. A spread in ticks is not comparable across reads. |
| the two tokens are one book quoted twice | TZ-14 §3.7: `bid_up + bid_down` `0.99` and `ask_up + ask_down` `1.01` across the whole distribution; `mid_up − (1 − mid_down)` exactly 0 from the 0.25 to the 0.90 quantile at every admitted `tau`; one executable free lunch after both fees in 8,400 paired checkpoints | **stands.** The Up book carries the market's probability alone. Re-derived by the Architect: all four crossings from the fee formula, their legs `0.98`/`0.01`, `0.71`/`0.28`, `0.58`/`0.41` and `0.700`/`0.291`. |
| **the round trip at the touch falls with `tau`, and so does the population** | TZ-14 §3.6 item 5: median `4.119` / `3.517` / `2.833` / `2.203` / `1.851` probability points at `tau` 240 … 60, over 2,400 / 2,394 / 2,246 / 2,005 / 1,452 two-sided reads | **stands as a fact of the venue, and it refuted the pre-registered P4.** The fee falls because the price has left 0.5, which is also why the book empties: cheap trading and an obvious outcome are one phenomenon. |
| **Phase 2's first gate reads UNDECIDABLE at all five `tau`: the side the pricer chose did not beat the market's ask** | TZ-15 §4, applied once to TZ-14's 1,200, every constant on disk before any outcome was read: `S` `210` / `211` / `190` / `164` / `99` wins against `s*` `238` / `232` / `210` / `173` / `115` at `tau` 240 … 60 — 28, 21, 20, 9 and 16 short — at exact false-positive rates `0.0067` to `0.0087` per `tau` and `0.0395` over the family; `POWER` against the pricer's claim `0.3257` / `0.4326` / `0.4304` / `0.4599` / `0.4673`, below the `0.8` floor at all five. Gross `T` `−0.0154` / `−0.0035` / `−0.0050` / `+0.0192` / `−0.0132` a share, `−0.0286` / `−0.0139` / `−0.0130` / `+0.0118` / `−0.0195` after the fee; no single member moves any reading. Re-derived by the Architect: the instrument's `pb_upper`, `crit` and `select` against independent exact references, 0 disagreements over 120 critical-value cases and 20,000 selections; `T`, `T_fee`, the claimed edges and the family sum from the printed sums; `POWER` to about `0.002` by a normal approximation; every count to its parts | **stands — no `tau` reads EDGE, none is closed, and Phase 2 is not decided.** No confirmation is triggered. NO EDGE was out of reach before any label was read, which is §7 item 69. |
| **the outcomes tracked the market's prices rather than the pricer's, at four of five `tau`** | Architect's arithmetic over TZ-15's printed sums, post hoc: the pricer claimed `Σq − Σa` = `+17.3` / `+17.6` / `+16.0` / `+15.1` / `+11.5` wins over the ask at `tau` 240 … 60, and the outcomes gave `S − Σa` = `−6.2` / `−1.5` / `−2.2` / `+7.3` / `−3.6`; under the pricer's own law the lower tail at the observed `S` is about `0.004` / `0.010` / `0.007` / `0.12` / `0.002` by a normal approximation. TZ-15's diagnostics: the market's mid beats `p_t` on the Brier score at 5 of 5 `tau`, by `0.0008` to `0.0041`, over `631` / `625` / `558` / `474` / `311` two-sided books, and is the more confident of the two at `0.48` to `0.62` of them | **stands as a finding, not a reading, and it closes nothing.** A test of the pricer's claim would have rejected it at `tau` 240, 120 and 60 and reached the one-per-cent boundary at 180; TZ-15's gate had no such row (§7 item 69), and its readings are not re-judged. |
| **the fifteen-minute market opens on the five-minute market's reading and settles on the same chain** | TZ-17, over the 200 consecutive windows from `1788998400` to `1789177500`, against the venue's resolved outcomes: I1, the same price-to-beat literal, 200 of 200; I2 and I3, each family's outcome agreeing with one reading at the shared boundary, 200 of 200; the two five-minute markets inside the window, 200 of 200; one `resolutionSource` for both families at 801 of 801 documents. Gate `N >= 199`, power `0.9106` against a 2% per-window failure rate, fixed before any document was fetched | **stands — B0 closed 2026-09-22.** The 801 documents, re-fetched by the Architect on 2026-09-23, hash equal to TZ-17's at 801 of 801. Two statements of the report are wrong and move nothing (§7 item 74). |
| **the settlement reading at a boundary is one published number** | TZ-18 G-CHAIN, offline on TZ-17's 801 bodies, each re-hashed to TZ-17's CSV: `finalPrice` of each five-minute market equals the next one's `priceToBeat` at 600 of 600, and the fifteen-minute `finalPrice` equals the `priceToBeat` of the five-minute market at `T+900` and the `finalPrice` of the one at `T+600` at 200 of 200 each — by `Decimal` value and as the same printed literal, 0 mismatches. Gate `Q1 >= 599`, `Q2` and `Q3 >= 199`, fixed before its data | **stands, and it closes the gap TZ-17's audit found**: TZ-17 inferred each settlement from the next market's price to beat, on margins down to `0.071` USD. Re-derived by the Architect from the venue's own bytes on 2026-09-23 — the same 801 bodies by hash — at 1,000 of 1,000 by value and by literal. The nesting of the two families' outcomes is exact. |
| the chain book records both books at one instant | TZ-18 G-DEPLOY: **0 of the first 14 qualifying checkpoints complete** — every request refused with HTTP 403 | **FAIL, and a fact of the build, not of the venue's books** (§7 item 77). No pairing skew was measured. |
| a second capture leaves Tier C intact | TZ-18 G-TIERC: `quotes_complete` at 4 of 4 intervals closing in the 1,390 s proof window, and at 4 of 4 in the control window before it | **stands only for the load that ran** — two refused document requests per 900 s, against the 30 requests TZ-18 §3.9 sized. The interlock has not seen the capture's own load. |
| the collector was not modified between TZ-01a and TZ-02 | hash equality, `6c5089…` read from `origin/main` | **stands** |
| the sign of `D = p_interval − p_naive` has no preferred direction | TZ-02 measurement 1 | **stands, and is of no consequence** |
| the venue's maker-rewards terms are readable from our capture | TZ-07a V9: the `rewards` key is absent from all 400 `gamma.json`. **TZ-14 §3.8, over 1,200:** the `rewards` object is still absent, but `rewardsMaxSpread` `4.5`, `rewardsMinSize` `50` and `holdingRewardsEnabled` `False` are present at 1,200 of 1,200 as top-level keys; no top-level key carrying a daily rate exists | **NARROWED.** The per-market terms are in the capture under individual names; the rate paid is not, so no maker income can be computed from it. |
| the TWAP model beats the endpoint model · divergence is abundant · inversions are the rare tail | Gate B, Gate A2, TZ-02 | **WITHDRAWN** — all scored against §2.2 labels |

---

## 5. Phase state

| phase | question | state |
|---|---|---|
| 0 | is the settlement rule what the CANON §1.1 says it is? | **CLOSED 2026-09-11 — yes. TZ-04b: 200 of 200 against a 199-of-200 gate**, reproduced by TZ-06 R-c |
| 1 | is `p_fair` calibrated against true-rule labels? | **ANSWERED 2026-09-18.** The normal link: disqualified at `tau` 60 and 30 by TZ-08a, against the band TZ-07a §8 fixed. The Student link of TZ-11a: **NOT DISQUALIFIED at `tau` 240, 180, 120, 90 and 60, inside its domain**, by TZ-12's sized gate applied once to test 3 (TZ-13); **UNDECIDABLE at 30 and 10**, where G3 lacks power. Phase 1 can only disqualify: none of this is a confirmation. |
| 2 | does the **market price** deviate from `p_fair`, and by how much? | **UNDECIDABLE at `tau` 240, 180, 120, 90 and 60 — TZ-15, 2026-09-19.** No `tau` reads EDGE, so no confirmation is triggered; none could read NO EDGE, because its only route was power, `0.33` to `0.47` against a `0.8` floor at 1,200 slots. **Open for the Student pricer at those five `tau`, inside its domain, and at no other `tau`.** The decisive gate is TZ-16, on the reserved span of §2.3. |
| 3 | is the deviation capturable after fee, spread, depth, 50 ms taker delay, oracle basis? | not started |
| 4 | live, minimum size, fixed loss limit | not started |

**The backup track** — CANON PART II, beside the phases and never inside them; it uses no pricer.

| step | question | state |
|---|---|---|
| B0 | do both families settle on one reading at the shared boundaries? | **CLOSED 2026-09-22 — yes. TZ-17: 200 of 200 against a 199-of-200 gate**, power `0.91` against a 2% per-window failure rate |
| B1 | can both books be read at one instant, without disturbing the capture Phase 2 depends on? | **open.** The direct `finalPrice` identity it carried is **closed — TZ-18 G-CHAIN, 1,000 of 1,000 by literal**. The deployment read **G-DEPLOY FAIL, 0 of 14**, on its own build, and G-TIERC PASS under a load it never applied. **TZ-18a redeploys it** and reads both gates under the full load |
| B2 | does a violation exist on executable quotes, after both legs' taker fees? | not started; written only after TZ-16's first reading is on `main`, and it reads only windows whose five-minute interval §2.3's reserve has released |

**This project has a settlement variable measured and confirmed, a pricer that Phase 1 has not
disqualified at five `tau` inside its domain — which confirms nothing — and no known edge.** The
normal link is disqualified at `tau` 60 and 30, and TZ-10b showed why: the settlement residual is not
normal, and less so the smaller `tau` is. TZ-11a fitted the Student link and its causal domain on the
Thursday–Friday set and froze them. TZ-12 measured, from the frozen pricer's own predictions, each
gate's false-failure probability and power, and fixed the sized gate — `0.048` family-wise, power
against a 1.5× overconfidence, UNDECIDABLE without it. TZ-13 applied it once to 750 weekday slots no
one had scored, every constant on disk before any outcome was read. No gate failed anywhere.
**TZ-15 then applied Phase 2's first gate once, and it decided nothing.** **Beside the phases, the
backup track has its structure measured and not one of its prices read:** one published reading settles
every market at a shared boundary, exactly, and the capture that would read both books at once has not
yet stored one.

**What Phase 2 inherits.** Five `tau`, not seven. A domain that quotes on about 70% of weekday
intervals and 6% to 8% of weekend ones, and no set scored under the sized gate that contains a weekend. A pricer that
leans under-confident at `tau` 90, 60 and 30 on the one set that scored it (§4), so a disagreement
between the market and `p_t` there is not, by itself, the market's error. And the gate discipline of
CANON PART II: a threshold fixed before any quote is aggregated, and a false-failure probability and a
power stated before any outcome the gate judges is read.

**What TZ-15 found.** At each admissible checkpoint of TZ-14's 1,200 it took, on paper, one share of the
side whose executable ask `p_t` called cheap after the taker fee — 1,924 trades over five `tau` — and
asked the venue's outcomes whether that side won more often than the ask it paid implied. It did not:
`S` fell 9 to 28 wins short of the critical count at every `tau`, and below the ask's own expectation
at four of five. No `tau` reads EDGE. None could read NO EDGE either: its only route was power, and the
power to see the pricer's own claimed edge — `0.036` to `0.043` a share above the ask — was `0.33` to
`0.47` at 1,200 slots, fixed before any label was read. After the fact, and barred from every reading,
the outcomes tracked the market's prices rather than the pricer's at four of five `tau`, and the
market's mid beat `p_t` on the Brier score at all five (§4). **The gate's one-sidedness is the
Architect's defect (§7 item 69), and no reading is re-judged.**

**Phase 2's decisive gate is TZ-16**, on the reserved span of §2.3, **with an exact test for each
answer**: EDGE where the side the pricer chose wins beyond the one-per-cent upper tail of the null — the
market calibrated at its own ask — and NO EDGE where it wins below the one-per-cent lower tail of the
pricer's own law, each `0.05` family-wise over five `tau`, UNDECIDABLE between them. TZ-15's selection,
fee and domain carry over unchanged; the critical values are derived under the serial dependence of the
null's residual, measured on TZ-15's labelled set (§7 item 71); the report prints what the Architect's
re-derivation needs (§7 item 70). **Its sampling rule is fixed before any label of the span is read,
with one interim look:** the first 2,400 qualifying slots after `1789669800`, and, for each `tau` that
look leaves undecided, the first 3,600 — read by a second TZ that applies TZ-16's frozen rule
unchanged. Each answer's one per cent is split between the looks in the O'Brien–Fleming manner, about
`0.002` at the first and the rest at the second. From TZ-15's label-free constants, and if the
residuals are independent, the first look decides a given `tau` with probability about `0.46` to
`0.65` under either hypothesis, and the two looks together with about `0.86` to `0.95` — the same as
one look at 3,600; TZ-16 re-derives both under the dependence it measures. At the rate every set has
qualified at — 90.3% to 92.9% of slots, about 265 a day — 2,400 qualifying slots after `1789669800`
exist around **2026-09-27** and 3,600 around **2026-10-01**. Nothing runs before the first.
**Other assets' markets are not a shortcut:** the pricer's domain threshold is in USD/s and its link
tables are the BTC feed's, so each asset would need its own Phase 0 and Phase 1, and same-window
outcomes across assets move together, so they add far less information than their count.

---

## 6. Environment

| item | value |
|---|---|
| host | Vultr VPS (Warsaw); the Executor runs Claude Code CLI **on the VPS itself**. A cloud Claude Code session is not this host and cannot execute anything that touches the capture. |
| **host identity, for TZ host gates** | `/var/lib/btc-recorder/` exists and holds interval directories · the recorder process is running and the newest `runtime.jsonl` start record carries sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` · the filesystem holding it is `/dev/vda2`, total `31,612,203,008` bytes. All three, or it is not the capture host. |
| language | Python 3.12. **The research interpreter is `/root/tz01-env/venv/bin/python`** — Python 3.12.3 with `numpy` 2.5.3 — on which TZ-11a ran; the system `python3` has no `numpy`. The recorder runs from `/root/tz04a-env/`. Neither environment is scratch and no TZ removes either. |
| stack | Parquet storage, pandas/pyarrow, DuckDB for aggregation; `decimal.Decimal` at 60 digits for every price |
| auth | CLI subscription auth; `ANTHROPIC_API_KEY` must not be set |
| git remote | HTTPS with the repository token embedded in the remote URL |
| egress, **verified 2026-09-12** | DNS and TCP/443 open to `ws-live-data.polymarket.com`, `gamma-api.polymarket.com`, `clob.polymarket.com`, `ws-subscriptions-clob.polymarket.com`, `docs.polymarket.com`. Anonymous only; no credentials of any kind are held. |
| **venue edge — the `User-Agent`, measured 2026-09-22 and 2026-09-23** | `gamma-api.polymarket.com` and `clob.polymarket.com` both answer **HTTP 403, body `error code: 1010`**, to a request carrying `urllib`'s default `User-Agent`: every request TZ-18's service sent, and the Executor's diagnostics from the capture host. The Architect reproduced it from a second host and isolated the header: `Accept: application/json` alone is refused, a non-default `User-Agent` alone is served — `200` for a market document, `404` "no orderbook" for a settled token's book. `tz17-settlement-chain.py` sends `btc-5m-twap-tz17` and was served at 841 of 841. **Every request a TZ fixes names its `User-Agent`.** |
| **disk, measured 2026-09-22 by TZ-17 and TZ-18** | one writable filesystem `/dev/vda2`, total `31,612,203,008` bytes. **Lowest free reading `13,453,283,328`**, TZ-18's closing read after its R6; its opening read `13,463,633,920` — a fall of `10,350,592` bytes across its session, of which `821,504` its own outputs with its two worktrees excluded, the rest not attributed. TZ-17 read it four times the same day, from `13,528,887,296` at its §0 to `13,513,277,440` at its close, `11,073,071` of that fall its own tree. Earlier lowest readings: TZ-15 `13,757,030,400` at 2026-09-19 08:14:22 UTC, TZ-14 `13,826,813,952`, TZ-13 `13,907,984,384`, TZ-12 `14,206,689,280`, TZ-11a `14,264,078,336`, TZ-11 `14,330,757,120`, TZ-09 `14,416,265,216`. `/var/lib`, `/root` and `/var/www` are all on it. **Any TZ that states a resource floor states it in exact bytes and derives it from this row.** |
| **capture cost, measured** | modelled Tier A + Tier C `23,850,461` bytes/day; **measured against the filesystem by TZ-09, `33,632,842` on disk and `26,784,064` apparent**. That is the recorder's own write rate, and **it is not the rate this filesystem is filling at.** |
| **the consumer — stopped, and now measured rather than reported** | The consumer is `/root/PROJECT_GAMING_PS5/netaudit/telemetry/captures`, another project on this shared host. TZ-10b's two §6 reads, `12,977` s apart, found the whole tree idle at `9,135,750` bytes/day — consistent with TZ-10a. **A third read the TZ did not ask for, `2,423` s after the second, found it writing again: `+36,524,032` bytes**, the largest part one `30,516,707`-byte `.pcap`. Across that window free space fell `66,232,320` bytes — `2,361,691,000` bytes/day, of which at most `18,554,880` is TZ-10b's own scratch, leaving about `1,700,000,000` bytes/day for that project. Our own persistent baseline is unchanged at `50,352,616` bytes/day: capture `33,342,903`, journald `8,794,795`, that project idle `8,214,918`. **TZ-11 §0 and TZ-11a §0 measured it four times across `26,252` s**, from 13:18:30 to 20:36:02 UTC on 2026-09-14: `telemetry-watch.service` read `disabled` (exit 1) and `inactive` (exit 3) at all four, and `/root/PROJECT_GAMING_PS5` held `354,009,088`, `354,582,528`, `355,405,824` and `356,073,472` bytes — `6,794,238` bytes/day of growth, idle by any measure, and `20,135,936` bytes smaller at the first read than TZ-10b's 11:12:25 UTC read, which is the purge. **TZ-12 §0 measured it twice more across `15,395` s on 2026-09-15**, `disabled` (1) and `inactive` (3) at both, the tree at `360,812,544` and `361,918,464` bytes — `6,206,657` bytes/day, the same idle rate six reads running. **TZ-13 §0 measured it twice more across `17,608` s on 2026-09-17 and 2026-09-18**, `disabled` (1) and `inactive` (3) at both, the tree at `367,914,928` and `369,501,594` bytes — idle, eight reads running. **TZ-14 §0 measured it twice more across `1,805` s on 2026-09-18**, `disabled` (1) and `inactive` (3) at both, the tree at `373,987,996` and `374,137,569` bytes — idle, ten reads running. **TZ-15 §0 measured it twice more across `1,817` s on 2026-09-19**, `disabled` (1) and `inactive` (3) at both, the tree at `377,747,683` and `377,910,258` bytes — idle, twelve reads running; across that window `/dev/vda2` gained `9,396,224` bytes used, of which `7,250,569` was TZ-15's own tree, `607,804` the Executor's session store and `162,575` that project, leaving `1,375,276` — `65,395,622` bytes/day — for the capture and everything else. **TZ-17 §0 measured it twice more on 2026-09-22**, `disabled` (1) and `inactive` (3) at both, the tree at `400,769,377` and `400,790,037` bytes, and **TZ-18 §0 once more** the same day, `disabled` (1), `inactive` (3), `403,322,657` bytes — idle, fifteen reads running. The Boss's report is confirmed by measurement, and this row does not rest on it. |
| **headroom — measured on total free space, and conditional** | From the lowest reading, `13,453,283,328`, to the `2,000,000,000` floor is `11,453,283,328` bytes. **Across the `3.6` days from TZ-15's lowest read, 2026-09-19 08:14:22 UTC, to TZ-18's first, 2026-09-22 before 22:53 UTC, free space fell `293,396,480` bytes**; with `/root/tz17-work`, TZ-17's own `11,073,071`-byte tree, taken out and the `39,278,075` bytes of `/root/tz14-work` reclaimed inside the window put back, `321,601,484` bytes are left — about `89,000,000` bytes/day. The earlier windows measured `129,541,842` bytes/day, TZ-12's last read to TZ-13's, `61,185,412`, TZ-13's last to TZ-14's first, and at most `111,671,404`, TZ-14's first to TZ-15's first. **The fastest, `129,541,842`, is the one quoted, and gives `88` days**, because windows on a shared host fix neither end of the rate. It is the rate of change of free space over a stated window, as §7 item 25 requires, net of each measuring run's own tree, as §7 item 29 requires. **It is conditional on `telemetry-watch.service` staying disabled:** if it is re-enabled the measured active drain of `2,361,691,000` bytes/day returns and headroom is `4.8` days, so every TZ re-reads `df`, `du` and `systemctl is-enabled` in its own §0 and states all three. |
| **price to beat** | published by Gamma only after settlement, at `events[0].eventMetadata.priceToBeat`, and captured per interval in `resolution.json`. Not available before the close; a live pricer reconstructs it from the feed. **Beside it, `finalPrice` is the reading the market settled on, and it equals the next market's `priceToBeat` as the same literal** — 600 of 600 (§4) — so a label can be read from either document. |
| **resolution endpoint** | `GET https://gamma-api.polymarket.com/markets/slug/btc-updown-5m-{T0}`, polled from `T0+333` every 15 s; the same path serves `btc-updown-15m-{T}` (TZ-17, 200 of 200). **A settled document is byte-stable**: the 801 TZ-17 stored on 2026-09-22, re-fetched by the Architect on 2026-09-23, hash equal at 801 of 801, so any stored settled body can be re-verified from the venue. |
| **CLOB websocket** | `wss://ws-subscriptions-clob.polymarket.com/ws/market` |
| **CLOB order book, REST** | `GET https://clob.polymarket.com/book?token_id={token_id}` — public, unauthenticated |
| **venue constants, measured TZ-05a and TZ-14** | **tick size:** `0.01` in all three sources at the one instant TZ-05a read them — `orderPriceMinTickSize` (Gamma), `tick_size` (`/book`) and `minimum_tick_size` (`/markets/{condition_id}`) — **but not a constant of the interval**: TZ-14 read `/book` `tick_size` `0.001` at 1,160 of 16,800 replies, while `gamma.json` at `T0 + 5` carries `0.001` at 2 of 1,200 members, so the tick falls to `0.001` inside the interval as the price reaches the wings · **minimum order size `5`**, in every `/book` reply of TZ-14's 16,800 · **fee schedule** `{"exponent": 1, "rate": 0.07, "rebateRate": 0.2, "takerOnly": true}`, `feeType` `crypto_fees_v2`, confirmed by TZ-14 in all 1,200 `gamma.json` · outcome mapping resolved from the outcome strings, `outcomes[i] == "Up"` against `clobTokenIds[i]`, never from position — `["Up", "Down"]` at 1,200 of 1,200 |
| **maker incentives** | Read from the venue's documentation 2026-09-12: makers pay no fee; the measured `rebateRate` `0.2` is a share of the taker fee paid on a fill; separately the venue runs a liquidity-rewards programme paying for resting orders near the midpoint, scored quadratically in distance and linearly in size, sampled once a minute, configured per market as `rewards.rewardsMinSize`, `rewards.rewardsMaxSpread` and `clobRewards[].rewardsDailyRate`. **Measured TZ-07a V9 and TZ-14 §3.8:** the `rewards` object is absent from every `gamma.json` read — 400, then 1,200 — but the same documents carry `rewardsMaxSpread` `4.5`, `rewardsMinSize` `50` and `holdingRewardsEnabled` `False` as top-level keys at 1,200 of 1,200, beside `feesEnabled`, `takerBaseFee` `1000`, `makerBaseFee` `1000` and `makerRebatesFeeShareBps` `10000`. **No top-level key carries a daily rate**, so no maker income can be computed from the capture; no maker assumption rests on this row. |
| host is shared | unrelated production services live on the same filesystem — `crypto-auto`, `my_real_estate_bot`, `seahome_webapp.git`, `/var/www`, `/var/log`. The recorder never deletes anything it did not write. |
| capture path | `/var/lib/btc-recorder/**` and, for the chain book, `/var/lib/btc-chainbook/**` (§2.5) — both outside the repository by design, so no capture can reach git history |
| **RTDS session limit, measured 2026-09-10** | the server closes every websocket `7,200` s after it opens, `1001 Going away`, timer restarting on each new connection. Undocumented. **No TZ may require an unbroken socket for longer than this.** |
| clock | NTP-disciplined; SNTP replies validated at reception since `4216c04`. Maximum absolute offset measured over the TZ-05a window: `18.789` ms; **over TZ-14's 1,200 intervals: `33.946` ms**, no interval above 50. An offset above 50 ms invalidates a latency claim; it is not a membership condition for anything. |
| **sandbox limit — network** | calls that read the git token and send it to `api.github.com` are refused. `git` push/pull work. Release creation and asset upload cannot be done from inside the session — hand the upload to the Boss and verify by anonymous download. **The Architect's session is not the Executor's and is not constant:** it could not reach `github.com` on 2026-09-22 (TZ-18 §10 C3) and reached it and both venue hosts on 2026-09-23. A TZ never depends on the Architect's reach; a check it cannot perform becomes a BLOCK condition (CANON hard rule 13). |
| **sandbox limit — destructive actions** | `kill` is refused by the permission classifier, alone or inside a compound command, and TZ-09 established that `rm -rf` of several trees is refused the same way. `rm -rf` of **one** tree was refused for TZ-12, TZ-13 and TZ-15 and **not refused for TZ-14**, three refusals in four TZs, so refusal is not predictable. **Any TZ that must restart the recorder or remove a tree keeps the fallback: it hands the Boss one exact block** and verifies the outcome from `runtime.jsonl`, `ps`, `df` and `test -e` rather than from his report. TZ-18's service is the first process a TZ started that must be stopped this way (§2.5). |

Not yet decided by any TZ and therefore not present: systemd units, the Parquet decision journal,
any deployment of the engine. **Capture retention is fixed by TZ-09 §5:** the capture is never deleted; archiving,
if it is ever done, is its own reversible TZ; a TZ's `/root/tz<NN>-work/` is reclaimed by the next TZ
once that TZ's report is on `main`, except what a committed artifact names by hash, which is copied
to `/root/btc-forensics/` first.

---

## 7. Open defects

| # | defect | disposition |
|---|---|---|
| 1 | `research/tz02-distribution.py` records the collector-hash comparison into `checks["collector_sha_matches"]` but never asserts it. The run completes on a mismatch. | open. Fix in the next TZ that touches that file; do not edit the committed report. |
| 2 | The TZ-02 report was amended after commit (`356c29a`). | closed by rule: contract §3.2 and §5.2. Both versions stay in history. |
| 3 | The TZ-02 implementation commit `f8a0c37` reached `main` without a merge and without a verdict. | closed by rule: contract §4.1 and the §4.2 self-check. |
| 4 | The Executor contract carried a space before its extension and both governance files were duplicated inside `research/`. | closed by TZ-03, PR #1. |
| 5 | **The settlement mechanic was wrong from inception.** | CANON replaced, labels withdrawn (§2.2). **The class is closed by TZ-04b V2.** |
| 6 | **TZ-04 §4 set a 20 GB free-space floor written from assumption.** | closed by rule: every resource floor is stated in exact bytes derived from §6. |
| 7 | Two executions of TZ-04 wrote two different reports to one path. | closed by rule: a re-execution never reuses a report path. |
| 8 | **TZ-04a §6 required 200 *consecutive* complete intervals** across a socket the venue closes every 7,200 s. | closed by rule: a requirement is a count of qualifying units, never an unbroken run. |
| 9 | **The V4 read-only proof was a bad instrument.** | closed by TZ-05a R-a and by ruling: a text search cannot prove the absence of a capability. The standing carrier is the merge-base diff plus the absence of any CLOB auth path. |
| 10 | **The recorder's SNTP client accepted invalid replies.** | closed by TZ-05a R-b, merged; twelve self-tests reproduced independently by the Architect. |
| 11 | **TZ-05 could not be executed in one session on any host.** | closed by TZ-05a and by CANON hard rule 11. |
| 12 | **`analyze.py:207` aborted every run** after the TZ-05a restart, killing the instrument behind the Phase 0 count. | **closed by TZ-06 R-c, merged.** The span is now bounded by the next start record, `within_span` is asserted per scored interval, and the repaired analyzer reproduces TZ-04b on every count — 215 / 200 / 15 / 200 / 175 / 181. |
| 13 | The TZ-05a report's exclusion line gives the wrong window-opening time for `1789206600`. | closed by rule: membership is re-derived by the Architect from epochs rather than read from the report. |
| 14 | TZ-05a carries two sections numbered `## 7`. | closed by rule: section numbers are asserted unique in the pre-delivery change list. |
| 15 | **TZ-06's calibration gate was marginal only** — a per-bin interval with a two-bin allowance cannot see a coherent one-sided pattern, and it passed a pricer whose sd is understated by half at `tau = 240`. Architect's defect. | closed by TZ-08a and TZ-11a, each of which scored a scale and a shape statistic fixed before its data. Repaired by rule: **every calibration gate carries a scale statistic and a shape statistic, both fixed before any data is seen** — a rule item 49 found incomplete and completes. |
| 16 | **TZ-06 §3 and §4 pulled in opposite directions for 25 of the 400 members**: §3 forbids carrying a value across a recorded disconnect, §4 makes only the interval's own manifest a condition. | **closed by TZ-07a M6.** Of the 25, ten have their predecessor's outage before `T0 - 300` and lose no second; the other fifteen do overlap and are now excluded increment by increment — `10,779` of `3,038,800` dropped, per lag and by member. |
| 17 | **`analyze.py`'s `V5_determinism` fell from 215 of 215 to 0 of 215.** Rebuilding a 2026-09-10 manifest with today's `manifest.py` adds the two keys TZ-05a introduced; every field the old manifests carry rebuilds identically. | open. Repaired by rule in the next TZ that touches `analyze.py`: a determinism check compares a rebuild against a rebuild, never against an artifact written under an older schema. |
| 18 | **`SYSTEM-MAP.md` on `main` was replaced by a chat message.** Commit `891d161` overwrote the map with an upload note, so revision `2026-09-12-b` never existed in the repository and TZ-07's fingerprint gate had nothing to read. | closed by rule: **after every upload the Architect reads `origin/main` and confirms the file that landed before `EXECUTE` is sent.** Exercised for `2026-09-12-c`; the map on `main` and the Architect's mirror were confirmed equal by hash. **Exercised again on 2026-09-19:** revision `2026-09-19-b` reached the project files and not `main`, and this read caught it before any TZ was written against it (§0). |
| 19 | **The TZ-07a correction divides the wrong random variable.** `g(h)` is the dispersion of a *single increment* over lag `h`; the pricer's `sd` describes the settlement average minus the current price, which at `tau >= 60` is a lead of `tau - 60` seconds **plus** a 60-second average contributing `20` of the `tau - 40`. Substituting `g(tau - 40)` for the whole scales the averaging part by a ratio belonging to the lead part, and the error grows as the averaging share grows: in-sample `λ̂` lands at 1.03 / 0.97 / 0.98 at `tau` 240 / 180 / 120 but 0.807 / 0.813 at 90 / 60. Architect's defect. | **closed by TZ-07b**, merged at `fb5c426`: `Y(a, tau)` is the settlement average minus the reading in force at the anchor, measured at every admissible anchor of every member, and `G_RATIO` is gone from the pricer. The rule stands: **a correction is measured on the exact random variable it divides, never substituted from a proxy horizon.** |
| 20 | **TZ-07a §8 gates six taus while §4 corrects five.** `tau = 30` is on the near branch, where `G` was fixed at exactly 1 with no measurement, and G3 scores it anyway — in-sample `λ̂` there is 1.4027. Architect's defect. | **closed by TZ-07b**: the keys of `SD_SCALE` are `pfair.TAUS`, `10` included, and a tau with no measured scale raises inside `corrected_sd`. The rule stands: **every tau a gate scores carries a measured constant.** |
| 22 | **TZ-07b §4 justified the root mean square as the maximum-likelihood scale of a Gaussian, and the measurement it commissioned refutes the premise.** The report's own tail table shows `r` is lighter than normal at one `Λ` and heavier at three, at every tau and increasingly so as `tau` falls. The root mean square therefore overstates the calibrating scale by more where the RMS-to-robust gap is wider — which is exactly where the predicted `λ̂` sits furthest from 1. A robust constant is no answer either: it would predict 0.836 at `tau = 90` and 1.337 at 30. The open question is the residual's **shape**, and no single constant per tau addresses it. Architect's defect. | **closed by TZ-08a, and the question it raised is answered: the shape is the defect.** Out of sample the tail at `3Λ` runs 8 to 10 times the normal's below `tau = 90`, and the robust scale sits 56 to 81 per cent under the RMS. No constant per tau closes that, and G3 failed at 60 and 30. `SD_SCALE` was not touched before the test and is not touched after it. The rule stands: **a scale estimator is justified by a distributional assumption, and the report that freezes the estimator reports the check of that assumption in the same document.** |
| 23 | **TZ-07b §2 forbade reading any outcome while §7 V4 required re-running two pipelines that read outcomes internally.** The Executor read the two sections as governing different things, carried only counts of exact matches out of the subprocesses, and disclosed the reading. Architect's defect. | closed by ruling — the Executor's reading is upheld: V4's subprocesses are exempt and no calibration statistic left them. Repaired by rule: **a scope prohibition names, in its own section, the checks that are exempt from it.** |
| 24 | TZ-07b's V1 guard — the `bisect`ed window handed to `pfair.time_weighted_mean` — was verified on the **first member only**, 175 of 175. The members carrying a recorded disconnect are the ones a bounded slice would break on, and none was sampled. | closed by rule: **a guard on an implementation shortcut samples across the scored set and includes the pathological members by construction.** No re-run: the shortcut narrows an argument the function would otherwise have scanned to the same rows, the disconnect rule drops those anchors before the call, and V3 reproduced byte-identically over three full runs. |
| 25 | **The Architect's §6 headroom figure was wrong by two orders of magnitude.** `245 days` divided free space by the recorder's own write rate, on a host the same section calls shared. Measured total drain is 0.84 to 1.00 GB/day and the true figure is 4.6 to 5.7 days. Architect's defect. | **closed by TZ-09 and the Architect's audit of it.** The consumer is named in §6 in exact bytes. The rule stands: **a headroom figure is derived from the measured rate of change of free space over a stated wall-clock window, never from any one process's write rate** — and §6 now carries a range rather than a point, because one window on a host with an intermittent consumer fixes neither end. |
| 26 | **TZ-07a §8's G3 fixes a likelihood over `Phi` and no tail-accurate `log Phi`.** `pfair.phi` returns exactly `0.0` below `z ≈ −8.37`, so one saturated prediction that disagrees with its label sends `ll(1)` to `-inf`, the likelihood ratio to `inf` and its p-value to `0`. It happened at `tau = 30`, on `T0 1789268400`. Architect's defect. | closed by ruling — the Executor's reading of TZ-08a §4.5 is upheld and the run is **not** BLOCKED: the only quantity §8 bounds, `λ̂`, is unaffected past its sixth decimal (2.041843 against 2.041844 evaluated tail-accurately), and only the unthresholded quantities degenerate. Repaired by rule: **a specification that fixes a likelihood over `Phi` fixes its tail-accurate `log Phi` in the same section.** |
| 27 | **A statistic a gate bounds was reported with no influence figure, and one observation set it.** `λ̂ = 2.0418` at `tau = 30` is carried by a single point; the other 399 prefer `λ = 1` by 14.7 log points. Neither TZ-07a §8 nor TZ-08a asked for it, so the report could not have shown it and the Architect had to derive it during the audit. Architect's defect. | closed by TZ-10b and TZ-11a, which applied the rule — TZ-11a V12 at 28 `λ̂` and 21 `ν̂`. Repaired by rule: **a fitted statistic a gate bounds is reported together with its value recomputed without its single most influential observation.** The committed report is not edited, and the gate is judged on the value §8 defines. |
| 28 | `tz06-calibration.build`'s set-size assert message names `SET_SIZE` where the run may now pass a different `need`. Disclosed by TZ-08a §11 item 4; exact at the default, which every run to date has used. | open. Fix in the next TZ that touches that file; do not edit the committed report. |
| 29 | **TZ-09 §3 M3's consumer rule did not exclude the measuring run's own footprint.** It named `/root` at `43,490,744` bytes/day, of which `1,490,944` of `1,843,200` — **80.9%** — is `/root/tz09-work` and `/root/.claude`, this TZ's scratch and the Executor's own session store. Strip the apparatus and the named consumer runs at about `8,300,000` bytes/day. Architect's defect. | closed by TZ-11 §0 and TZ-11a §0, which re-measured the host after the stop and stated their own footprint separately. Repaired by rule: **a rate measurement of a shared resource subtracts the measuring run's own footprint from the quantity it attributes, and reports that footprint separately.** |
| 30 | **TZ-09 §3 fixed a one-hour deciding window on a host whose dominant consumer is intermittent.** The designed instrument missed the thing the TZ existed to find; a read the TZ did not ask for found it three hours later at `2,547,725,419` bytes/day. Architect's defect. | closed: four reads across `26,252` s found the consumer disabled and idle, and §6 carries a measured, conditional point figure. The Executor was right not to re-choose the window after seeing data, which would have been reinterpreting §3. Repaired by rule: **a window that must characterise an intermittent consumer is at least as long as that consumer's measured idle-to-active period, or the TZ states in its own §3 that its figure is a lower bound.** |
| 31 | **TZ-09 §5.3 defined preservation by "the SHA-256 a committed artifact names" and said nothing about a hash taken over several files.** `CryptoReports/TZ-01-…-report.md` §2 gives one SHA-256 over all of `partitions/` and one over all of `state/`; neither is any single file's hash, so R2 as written deleted 23 partition files and 24 state files, and those two rows can no longer be verified from disk. The Executor extended the rule to save an abbreviated-hash file and applied it literally here, disclosing both. Architect's defect. | closed by ruling — the Executor's reading is upheld, and the material loss is near zero: TZ-01's results are withdrawn under §2.2 and its dataset is superseded by the `tz-01a-dataset` Release asset. Repaired by rule: **a preservation rule states what an aggregate hash over several files names; where it names nothing, deleting any member is authorized only by a TZ that says so in exact counts.** |
| 32 | **TZ-09 §7 V2 proved the instrument cannot delete by grepping Python deletion APIs, and the instrument imports `subprocess`.** The check as specified could not have caught `subprocess.run(["rm", …])`; the Architect had to re-derive the proof during the audit by enumerating all four call sites. It holds — every argv is a fixed `df`, `du`, `git` or `journalctl --disk-usage`, with no shell — but the instrument did not establish it. Architect's defect, the same class as item 9. | closed by rule: **a proof that code cannot perform an action enumerates its delegation paths — `subprocess`, `shell=True`, external binaries — as well as the in-language APIs.** The committed report is not edited. |
| 33 | **TZ-10 §5.2 item 4 fixed a range that excludes the true value.** `log_phi(−10.819)` is `−61.8339909672382`; the TZ required it between `−60.0` and `−55.0`. §4 of this map already says `Phi` assigned about `1e-27` at that point, whose natural log is `−62.17`, so the TZ contradicted the map. **No correct `log Phi` could pass it**, and the Executor stopped rather than widen the range. The formula itself is sound: the Architect verified both branches against a 60-decimal-digit reference at fourteen points from `0` to `−40`, agreeing to 12 significant digits at every one. Architect's defect. | closed by TZ-10a, which states every expectation as a literal computed and cross-checked at 60 decimal digits before it was written. Repaired by rule: **a fixed numeric expectation is computed before it is written, never bounded by eye, and the TZ that fixes it states how it was cross-checked.** |
| 34 | **TZ-10 §5.2 items 2 and 5 tested a tail-accurate function against the inaccurate one it exists to replace, in the tail.** `pfair.phi` is `0.5*(1 + erf(z/sqrt(2)))`; below about `z = −4.5` that is the sum of two doubles near 1 and loses relative accuracy, reaching `1.8%` at `z = −8`. Both items ran to `−8` and could not pass under any reading of "12 significant digits". Architect's defect. | closed by TZ-10a: the identity against `pfair.phi` is confined to `z` in `−3 … 3`, where that implementation keeps 12 significant digits with margin, and the tail is checked against literals instead. Repaired by rule: **a self-test for a replacement implementation never uses the implementation it replaces as its reference in the region that motivated the replacement.** |
| 35 | **TZ-10 §2's scope list omitted `research/selftest-pfair.py` while §5.2 required five tests to be added to it**, and §0's table lists that file `frozen`. The Executor disclosed the contradiction and stopped before either reading had to be chosen. Architect's defect. | closed by TZ-10a, which names the file in its own scope section and authorizes the change. Repaired by rule: **a TZ's scope section names every repository path the TZ's own body requires it to change, and any `frozen` row a TZ moves is named there by path.** |
| 36 | **TZ-10 §7 V2 and TZ-10a §7 V2, byte-identical, required a quantity that is a function of the future to be bit-identical under perturbation of the future.** `u = Y / sd`, and `Y(a, tau)` is the settlement average over the window after the anchor minus the reading in force at it, so the numerator moves under any correct implementation, at every anchor and every `tau`. The same row perturbs **"at or after the anchor"** — the wording TZ-08 was BLOCKED on and TZ-08a §7 V2 repaired to "strictly greater than the checkpoint instant" — so even the denominator-only reading fails: `sigma_hat`'s last grid point is the anchor itself and it moved at 133 of 140 checkpoints, exactly the count with a report stamped at that instant. Two Architect's defects in one row, and the second is a regression of a repair already made. | closed by TZ-10b. Repaired by rule, both halves: **a causality check names the causal quantity it tests — never a realised outcome or any expression containing one — and names the exempt quantities in its own row**; and **a perturbation boundary is "strictly after the last instant the tested quantity may read", and a boundary once repaired is carried into every later TZ that reuses the check.** |
| 37 | **TZ-10a §5.2 item 1's two asymptotic literals reproduce the branch they test rather than an independent reference.** Against a 60-digit reference `log_phi(−36)` is `−652.503227593798` and `log_phi(−40)` is `−804.608442013754`; the TZ wrote `−652.503227593835` and `−804.60844201377`, which are the truncated series' own output — the dropped `105/z⁸` term, `5.67e-14` and `1.98e-14` relative. They pass the 12-significant-digit tolerance the TZ fixes, so item 1 went green, but the only two rows that exercise the asymptotic branch could confirm nothing except that it reproduces itself, and §5.2's claim that every literal was cross-checked at 60 decimal digits is false for those two. Architect's defect; found by the Architect's audit, not by the report. | closed by TZ-10b, which carries both corrected literals, names the reference and states the margin. Repaired by rule: **a fixed literal is computed from an implementation independent of the one under test, at a precision better than the tolerance it fixes by at least a decade, and the TZ names the reference and states the expected margin.** |
| 38 | **TZ-10a §3.0 defined `u = Y / corrected_sd` while §7 V4 required the instrument to reproduce TZ-07b's `Λ`**, which is the RMS of `Y / (sigma · sqrt(H(tau)))`. The two differ by the factor `SD_SCALE[tau]`, so V4 could not have passed at any `tau` under the TZ's own definition, and the RMS of `u` is `1` by construction. Disclosed by the Executor as §4.2 item 2; it would have BLOCKED the run a second time. Architect's defect. | closed by TZ-10b, which defines both quantities and the identity `u = r / SD_SCALE[tau]` linking them, and states which one every check reads. Repaired by rule: **a TZ that names a committed measurement as a reproduction target writes the exact expression that produced it and states the identity linking it to the quantity the instrument computes.** |
| 39 | **TZ-10a §2 stated that outcomes are read by M2 and by nothing else, while §3.0 forms both sets by calling `tz06-calibration.scoring_set`** — whose `qualification` calls `analyze.venue` and reads `resolved_up` and `priceToBeat` for every unit considered, member and non-member alike. This is item 23's class, and item 23's repair rule already existed when the TZ was written. The same TZ states `corrected_sd`'s argument order wrongly twice — §2 says a different **first** argument and §3.0 writes `corrected_sd(s, tau)`, against the committed signature `corrected_sd(tau, sigma)`. Architect's defect. | closed by TZ-10b, which names the set rule's own outcome reads as exempt and writes the signature as the file has it. Repaired by rule: **a prohibition in a scope section is checked against every committed entry point the TZ calls before the TZ is sent, and a TZ that names a committed function states its signature as the file has it.** |
| 40 | **TZ-10b §4.2's decision statistic `g` is a ratio whose denominator the gate elsewhere wants at zero.** `g = (\|λ̂_hat − 1\| − \|λ̂_post − 1\|) / \|λ̂_hat − 1\|`, and `λ̂_hat` at `tau = 120` is `1.001337`, so `g` reads `−122.39`; on the TZ-06 share at `tau = 240` it reads `−49.26`. At `tau = 30` it reads `0.2115` against a `0.20` boundary — a margin of `0.0115` — and becomes `0.6574`, a different row of §4's table, once the single most influential observation is removed. Architect's defect. | closed by ruling: the §4 verdict stands on `f` and on M3, both formed over millions of anchors, and `g` is withdrawn as a reading (§4). Repaired by rule: **a statistic a verdict table reads is bounded on the set it is read over, and a ratio is used only where its denominator is bounded away from zero by the gate's own construction; where it is not, the statistic is a diagnostic and the TZ says so in the row that defines it.** Item 27's leave-one-out rule worked — it is what exposed this — and now extends to every statistic a verdict table reads, not only a fitted one. |
| 41 | **TZ-10b §3.1 specified `κ` over the intersection and over the full 800, and never per set.** The one property that had already destroyed two constants — whether a statistic transfers between the two windows — was therefore not measured by the TZ that existed to characterise the residual. The Architect had to re-derive it during the audit from TZ-07b's and TZ-08a's committed diagnostics: `κ` `1.042` … `1.961` on the TZ-06 400 against `1.22` … `5.26` on the TZ-08a 400. Architect's defect. | closed by TZ-11a M3, which reported `κ`, `ν̂` and `ŝ` for six populations one by one. Repaired by rule: **a statistic measured over more than one set is reported per set before it is reported pooled, and a pooled figure never stands alone where the sets are the out-of-sample structure.** |
| 42 | **TZ-10b §7 V7 fixed its expectation in prose — "expected to agree past the sixth decimal" — and the phrase has three readings, one of which fails the run.** The observed pair is `2.0418426092` against `2.0418435851`, a difference of `9.759e-07`: below `1e-6`, but not equal at six printed decimals. The Executor stated all three readings, asserted the first and said which one the check turns on. Architect's defect. | closed by ruling — the Executor's reading is upheld, because §7 item 26 of this map names that exact pair and calls `λ̂` unaffected past its sixth decimal. Repaired by rule: **a numeric expectation is an inequality on a named quantity with an explicit bound and explicit units; a phrase about decimal places is not an expectation and never appears in a `## Validation` section.** |
| 43 | **TZ-10b §3.2 required `tz07a.lambda_hat` to run with a `log_phi` likelihood, while `tz07a-variance-time.py` is `frozen` and §2 authorized no file that could make it happen.** The Executor rebound the module-level `log_likelihood` for the length of each call, restored it in a `finally`, asserted the restoration before V7 used the original, and disclosed it. It is nevertheless a second implementation of a committed formula, living in an instrument. Architect's defect. | closed by ruling — the reading is upheld and no calibration figure escaped the substitution. Repaired by rule: **a TZ that requires a committed function to run with a substituted dependency authorizes an additive keyword parameter on that function, in the file that holds it, named by path in its own scope section — and the parameter's default reproduces the committed behaviour byte-for-byte. Substitution at run time is never the design.** TZ-11 §2 carries the first application. |
| 44 | **TZ-10b §2 listed `/root/btc-forensics/` as untouchable while §9 of the same TZ required three files copied into it.** This is the fourth instance of one class — items 23, 39 and now this — and the prose repair rule written at item 23 did not prevent the third or the fourth. Architect's defect, and the repair itself is the defect. | closed by ruling — the Executor's reading is upheld; each copy used exclusive create, and all 91 pre-existing files hash unchanged. Repaired by a mechanical check rather than a rule: **before a TZ is sent, its §2 prohibition list is diffed against every path and every committed entry point the TZ's own body names, and each intersection is either removed from the prohibition or written into §2 as a named exemption. The diff is performed, not intended.** |
| 45 | **TZ-11 §5.2 item 5 fixed a self-test expectation on a quantity the same TZ measures.** The item required `p_fair_student` to return `F_3(−10.819)` "at `ν = 3`", and §5.1 defines `p_fair_student(state, sd, tau)` to evaluate at `LINK_NU[tau]`, which §3.2 freezes from a maximum-likelihood fit that had not been run. The item therefore passes only if that fit returns exactly `3.00000` at six significant digits; the map's own inversion of `κ` puts `ν` near `2.46` at `tau = 30`, and at the six-digit neighbours `2.99999` and `3.00001` the value already differs by `1.49e-05` relative against a `1e-10` tolerance. The item tested the data, not the code. Architect's defect. | closed by TZ-11a, which splits the item: the literal comparison is made against `t_cdf(z, 3.0)` with `ν` written in the call, and the pricer's own `p_fair_student` is checked by an inequality that holds for every `ν` the search can return. Repaired by rule — **CANON PART VI check C2**: every fixed numeric expectation is either computed by an independent implementation or quoted from a committed artifact, and **an expectation whose value depends on a quantity this same TZ measures is forbidden**; where such a check is wanted it is written as an inequality that holds for every admissible value. |
| 46 | **TZ-11 §5.3 required a keyword parameter on two committed functions while §7 V6 required the diff to hold "insertions only".** Adding `log_cdf=None` replaces `def log_likelihood(pairs, lam):` and `def lambda_hat(pairs):`, and passing it on replaces the two call lines inside `lambda_hat`. V6 was unsatisfiable independently of item 45, so the run would have stopped a second time. Architect's defect. | closed by TZ-11a, which names the four replaced lines by number and by their committed text and asserts the removed-line set equals exactly those four. Repaired by rule — **CANON PART VI check C3**: for every file a TZ calls additive, the committed lines the change replaces are named, read from `origin/main`; where that list is not empty, the words "insertions only" never appear in the TZ. |
| 47 | **TZ-11 §7 V12 required a leave-one-out figure for every `ν̂` and neither defined influence for a profile fit nor priced the check.** Exact leave-one-member-out repeats §3.1's nested search once per member removed: about `2,600` likelihood evaluations per fit over up to `198,000` anchors, 42 populations, several hundred members each — of the order of `4e12` element operations, from about twelve hours vectorised to a week as the instrument is actually written, against a session that a usage limit paused for `2.2` hours mid-run. Architect's defect. | closed by TZ-11a: influence for a profile fit is defined as the member's own contribution to the log-likelihood at the optimum, one exact refit is required without the single largest contributor, the fit count is stated as `63`, the arithmetic is fixed as vectorised `float64`, and the run BLOCKS if the first fit exceeds `60` s. Repaired by rule — **CANON PART VI check C4**: every check whose cost grows with the data states that cost in evaluations and in seconds at the measured rate, and anything above `3,600` s of single-session compute is sampled under a stated rule or becomes its own TZ. |
| 48 | **Four quantities in TZ-11 had no population or no derivable count.** V4 asked for `tz07a.lambda_hat` on the TZ-08a 400 while §2 said labels enter a printed number in M4 and M5 only — the fifth instance of items 23, 39 and 44. V4's "50 members" holds only if its rule is read over the fit set and test 1 alone; over three sets it is at least 65. G2 said "pooled over `tau` as TZ-06 pools it" while §4 gated all seven, and `tz06.build` pools `pfair.GATED_TAUS`, which excludes `10`. §3.5 asked for a likelihood contribution without naming which of §3.4's two fits it comes from. Architect's defect, four times. | closed by TZ-11a, which names V4 as the third exempt outcome read, scopes the 50 to the two committed sets and requires the count re-derived and reported, pools G2 over `pfair.GATED_TAUS` with `tau = 10` reported and not pooled, and names M5's population. Repaired by rule — **CANON PART VI checks C5 and C6**: every count a Validation section states is re-derived from the sets §3 defines and named with them, and every statistic names the population it is computed over. |
| 49 | **TZ-11a §4 fixed four gates with thresholds and no error rates, and G3 — TZ-07a §8's band, carried unchanged — fails an exactly correct pricer more often than not.** Labels drawn from the pricer's own predictions give a per-`tau` false-failure probability of `0.19` to `0.35` at `tau` 240 … 60 on test 2's admissible rows, `0.52` and `0.71` at 30 and 10, `0.67` to `1.00` on test 1's, and a failing `tau` somewhere with probability at least `0.71` on every population scored. Where most predictions sit near 0 or 1, the scale estimate lands on the bound `0.5` whenever no confident prediction is contradicted, so `\|λ̂ − 1\| <= 0.15` is decided by whether a surprise happened. TZ-08a's G3 failure used the same band; Phase 1's answer for `p_fair` does not rest on it alone, because TZ-10b's `κ` refutes `Φ` over millions of anchors. Architect's defect, found by the Architect's audit. | **closed: TZ-12 measured every one of them exactly**, and the audit's approximation held — 0.224 to 0.345 at `tau` 240 … 60 and 0.703 at 10 on test 2 against the 0.19–0.35 and ~0.71 the audit predicted, with `tau = 30` understated at 0.52 against 0.620. **Closed by TZ-13:** the sized gate, applied once to test 3, read FAIL nowhere, NOT DISQUALIFIED at five `tau` with power, and UNDECIDABLE at two for want of it. The TZ-11a verdict stands and is not re-judged. Repaired by rule: **a gate states, before any label it judges is read, its false-failure probability under the model it scores — family-wise over every `tau` and set — and its power against a named alternative; a gate without that power reads UNDECIDABLE, which closes nothing and admits nothing.** |
| 50 | **TZ-11a's G2 read `pass` on test 1 with 0 eligible bins at all six gated `tau`.** A gate with nothing to judge printed the same word as a gate that judged and found nothing wrong. Architect's defect. | closed by item 49's rule: nothing eligible reads UNDECIDABLE. |
| 51 | **TZ-11a judged G4 on 28 to 35 members, where dropping the single most influential one moves `ν̂` onto a search bound at 4 of 7 `tau`.** The domain rule, an absolute level in USD/s, admitted 7% to 9% of a weekend set; TZ-11a §3.2 said its cost would be measured and did not say what a gate does when that cost empties the population. Architect's defect. | closed by TZ-12 and TZ-13: under the sized gate a statistic with nothing eligible, no power or a censored constant reads UNDECIDABLE, and on test 3 the domain admitted 514 to 528 members per `tau`. Repaired by item 49's rule, and: **a TZ whose rule filters a scored population states, in the gate, what each statistic reads when the filtered population cannot support it.** |
| 52 | **TZ-11a §3.1 and §10 C4 bounded one likelihood evaluation at "at most `198,000` anchors"** — the per-`tau` mean of TZ-07b's `1,384,934` — while the all-member populations hold up to `236,125`. The cost statement was wrong by 19% and harmless: the whole run took `294` s against a `3,600` s ceiling. Architect's defect. | closed by rule: **a cost bound is derived from the maximum of the population it bounds, never from a mean.** |
| 53 | **TZ-11a §10 C5 counted "TZ-08a V8's six ratios" while its own §7 V4 required seven `RMS(u)` at 7 of 7.** TZ-08a's V8 table has seven rows, `tau = 10` included; the Executor asserted seven and disclosed the conflict. The pre-send protocol ran and wrote a count it had not re-derived from the artifact it named. Architect's defect. | closed by ruling — the Executor's reading is upheld. Repaired by rule: **every count a C5 line states names, beside it, the table or line of the artifact it was counted from.** |
| 54 | **TZ-11a let the Executor's smoke passes read test-set labels before the scoring commit was final**, and that commit was then amended. Nothing that sets a scored number could move after the tables were frozen — V8 asserts them against the fit set's own measurement and §4's thresholds are the TZ's — and by the report's account, which cannot be checked because the earlier commit was never pushed, the amendment touched only the M5 table's `admissible` key. Nothing is re-opened. Architect's defect: the TZ did not forbid it. | closed by rule: **a TZ that scores out of sample states that no pass reads a test-set label until the commit that scores it is pushed; smoke passes run on the fit set.** |
| 55 | **Three statements in earlier revisions of this map were carried rather than read:** that `tz-09-disk-inventory` was deleted after PR #10 — `git ls-remote` shows it at `e45f38e`; that `/root/tz09-work/` was accounted for — its two worktrees were never named for reclaiming by any TZ; and that the TZ-08a set "is not a second volatility regime" — it is the weekend, with median `sigma_hat` at about a third of the weekday level. Architect's defect. | closed by rule: **the map's branch list is read with `git ls-remote` at each revision; every `/root/tz<NN>-work/` a TZ leaves behind is named in the next TZ's retention section until `test -e` shows it gone; and no statement about a regime is written without the measurement that makes it.** `/root/tz09-work/` is TZ-12's to reclaim, and it did. **The branch statement was wrong a second time, in the other direction:** revision `2026-09-15-a` put `tz-11a-student-link` and `tz-09-disk-inventory` on `origin`, read there by `ls-remote` on 2026-09-15, and on 2026-09-17 neither is there. TZ-12 pushed one branch and deleted none. The rule held — it is the `ls-remote` at this revision that caught it — and §1 now records the disappearance and the `refs/pull/*` refs that preserve both commits. |
| 56 | **TZ-12 §4 fixed a power floor and no replicate count that resolves it.** `R_POWER` is `0.5` and the power estimates come from 2,000 replicates, so one Monte Carlo standard error at the floor is `0.0112`. On test 2, `P3` reads `0.4990` at `tau = 180` and `0.4785` at 60: both 95% intervals straddle `0.5`, so the admitted set `{120, 90}` is separated from `{180, 60}` by simulation noise and not by the population. The Executor applied §4 as written, reported the prediction row as not holding, and refused to re-choose `R_POWER` after seeing the number — which is correct and is why this is the Architect's defect and not a run defect. | **closed by TZ-13:** the band covered no power estimate at any `tau` for any gate, 0 of 21, and moved nothing. Repaired by rule: **a gate that compares an estimated probability against a floor states the replicate count that makes one standard error small against the floor's own margin, and a reading whose confidence interval straddles the floor is UNDECIDABLE, never a decision.** TZ-13 applies the straddle reading at the committed `2,000`, where the band at the floor is `0.5 ± 0.0219`, and moves no frozen file to do it. |
| 57 | **TZ-12 §3.1's censoring rule lets a bound-hit replicate into a frozen spread.** A `tau` is censored only when more than 2 of 24 refits put `ν̂*` on a search bound, so one or two may enter. At `tau = 240` the largest replicate is exactly the upper bound `60.0000`; re-derived by the Architect from V12, dropping it takes `SIGMA_LOG_NU[240]` from `0.476750` to `0.334695` against the report's `0.334694` — **53% of the variance from one censored point** — and at `tau = 120` the same holds at 33%. A value pinned to a search bound is not a draw from the sampling distribution, and the constant it inflates is the width of G4's band. Architect's defect. | closed by arithmetic, not by a re-run: G4 has no power at `tau` 240 or 120 on either test set with the constant either way — `P4` `0.0027` against `0.0089` at 240, `0.0068` against `0.0132` at 120 — so no reading and no verdict moves, and `SIGMA_LOG_NU` stays frozen as measured. Repaired by rule: **a replicate whose fitted parameter lands on a search bound is censored, not averaged: either the bound is widened until no replicate touches it, or the `tau` is censored at the first bound hit.** TZ-13 carries the rule and does not re-fit the table. |
| 58 | **A target was stated in qualifying units without naming the instrument that counts them**, and the count that came back was a listing of interval directories filtered by day of week — 794 of 794, a filter that excluded nothing because the span holds no weekend. Qualification is the committed set rule: the interval's own manifest complete and no recorded disconnect in it or its predecessor. Every set formed to date lost 7.6% to 9.7% to that rule and none lost zero, so 793 directories are `716` to `732` qualifying slots, not 793. Architect's defect: the 750 was stated without its instrument. | closed by rule: **a count of qualifying units is produced only by the committed set-formation code, named by function in the sentence that states the count; a directory listing, a file count and a calendar filter are never that instrument.** The domain rule is `ADMIT[tau]` on `sigma_hat` in USD/s and is not a calendar rule: a weekday is not a qualification and a weekend interval above the threshold is admissible. |
| 59 | **TZ-13 §3.5 named `tz12.verdict(per_tau)` as the per-`tau` verdict, and the committed function returns one family-level verdict with an admitted list.** The Executor derived each `tau`'s verdict by §4.1's own rule and reported it beside the family verdict; the two agree. C7 read the function's signature and not its return. Architect's defect. | closed by ruling — the Executor's reading is upheld. Repaired by **CANON PART VI C7 as amended in CANON revision `2026-09-18-a`**: every behaviour a TZ attributes to a committed function is quoted from its body — its return statements, every assert on its arguments, and each branch the sentence relies on. |
| 60 | **TZ-13 §4 gave G4 three UNDECIDABLE clauses — power below the floor, a censored `tau`, a fit on a search edge — and §3.5 said the readings are `tz12.readings`' own, weakened by §4.3 and by nothing else; the committed `tz12.readings` carries the censoring clause alone and passes `nu_on_bound` through unread.** The Executor applied the two further clauses in a separate function that can only weaken; no verdict depends on which reading is taken, because G4 FAILs nowhere. Whether TZ-12's own §4 stated clauses its instrument omits is not re-read by this revision. Architect's defect. | closed by ruling — the reading is upheld. Repaired by C7 as amended, and by a rule now in **CANON PART II: power qualifies a silence, never a failure** — a statistic beyond a critical value whose false-failure rate is measured reads FAIL whatever the power; power decides only between PASS and UNDECIDABLE; a statistic whose critical value is not measured reads UNDECIDABLE. TZ-13's G4 weakening, and its §4.3 band — whose self-test item 2 turns a FAIL at `P = 0.50` into UNDECIDABLE — would each have discarded a measured failure had one occurred. None did. |
| 61 | **TZ-13 §3.6 asked for `tz12.constants` on repeated rows, and the committed function asserts one row per member.** The Executor keyed each copy `T0 · multiple + copy_index`, so the assertion passes with the function untouched, and confined the keys to the projection, a table barred from every gate. The precondition sits in the body, where C7 did not look. Architect's defect. | closed by ruling — the workaround is upheld, and it is TZ-13's only departure from a committed call. Repaired by C7 as amended. |
| 62 | **TZ-13 §6 costed a run at about `770` s, and the two took `1,579.6` and `1,591.3` s; its fail-fast, `35 t + 500 <= 3,000` s, projected `1,143` s for the first.** The estimate took the admissible population from the middle of the TZ's own predicted share — about 436 rows, where §7 item 52's rule requires the maximum, 750 — omitted the fit set V4 walks, `1,550` walked against `1,150` costed, and priced the base `tz12.constants` pass at `75` s against `155` measured. Measured, the `tz12.constants` calls cost about `54 t` of a run, so at the fail-fast's own limit, `t = 71` s, they alone come to about `3,900` s — past the `3,600` s ceiling within one run; the session ended at `3,171` s. Item 52's rule was in this map and did not prevent it. Architect's defect, the second of its class. | closed by rule, now mechanical — **CANON PART VI C4 as amended**: every cost is computed at the population's upper bound, a filtered population at its unfiltered size, over the union of the populations C6 lists, and every fail-fast bound is derived term by term from the same figures, its derivation written beside it. |
| 63 | **The TZ-13 report does not state the instant its scoring commit reached `origin`, and no Validation row asked for it** — the fact §7 item 54's rule exists to make checkable. V2's ledger proves one outcome read per run, not the order of that read and the push. Nothing that sets a TZ-13 verdict is discretionary — the constants are label-free and byte-identical across two runs, and every threshold is committed — so nothing turns on it. Architect's defect: a prohibition with no evidence row. | closed by rule: **a TZ that scores out of sample carries a Validation row that prints the instant its scoring commit reached `origin` beside the instant of its first outcome read.** |
| 64 | **TZ-14 §3.9's P5 named its population "paired checkpoints" and did not say what an undefined sum does to it.** At 2,838 of the 8,400 one book side is empty and `bid_up + bid_down` is not a number. The Executor's first implementation dropped those checkpoints and so moved P5's denominator from 8,400 to 5,562 without saying so; it caught this itself, restored the population and printed the undefined count beside the statistic (its R5). P5 holds under both readings. Architect's defect. | closed by ruling — the reading is upheld. Repaired by rule: **a statistic or a prediction over a population on which its quantity can be undefined states, in the sentence that defines it, whether an undefined value leaves the denominator, and the count of undefined units is printed beside it.** |
| 65 | **TZ-14 §3.6 chose `MIN_SIZE` by a statistic of the whole population — the reply's `min_order_size` "where present in every read" — while the touch it governs is computed inside the same pass.** No single pass could know the condition before using it. The Executor computed the touch at both candidates for every read and chose afterwards (its R7). Architect's defect. | closed by ruling — upheld; the two candidates were the same number at 16,800 of 16,800. Repaired by rule: **a constant a TZ selects from a population statistic is fixed by a prior, named pass or by a literal, never by the pass it governs — or the TZ states that every branch is computed and the choice made after.** |
| 66 | **Two of TZ-14's Validation rows contradicted the sections they summarise.** V11 listed "the four cumulative sizes" where §3.6 item 3 defines four per side, eight in all (its R4); V1 called the fingerprint gate *asserted* while §5.1's run order gave it no step, so no assertion could exist (its R3). C5 re-derived set sizes and not the counts inside a row's own prose, and nothing checked that every asserted row has a step. Architect's defect, twice. | closed by ruling — both readings upheld: eight columns, and a step 0 that runs the gate inside the instrument. Repaired by rule: **CANON PART VI C5's "each count a Validation section states" is performed literally** — every count written anywhere in a row, a column count, a list length, an item count, re-derived from the section that defines it, and not only the set sizes; and **every check a Validation row calls asserted has a numbered step in the run order.** |
| 67 | **Four statements in the TZ-14 report are wrong, and none moves a number.** §1.8 says `a314151` uploaded `research/tz13-sized-gate-test3.py` beside the TZ; it added the TZ alone, 725 lines. §1.2 attributes its directory reading, 2,425, to the run's start, while its last `T0`, `1789760700`, is 2026-09-18 19:45:00 UTC — the first preflight's minute — and V9 gives 2,430 at the start; the 4,856 `manifest.json` opens reconcile only with the later count, as `2 × 2,428`. §1.2 renders `1789033800` as 2026-09-09 22:30 UTC and `1789760700` as 22:25; they are 2026-09-10 09:50 and 2026-09-18 19:45. §2.6 item 2's per-`tau` split `(11, 12, 19, 22, 14, 9, 15)` sums to 102 beside totals of 53 and 51. Found by the Architect's audit. | closed by rule — item 13's governs the dates: **epochs are the authority, and every membership and span is re-derived from them.** And: **a total printed beside a per-category breakdown is computed from that breakdown by the instrument that prints both, and asserted equal to it.** The committed report is not edited. |
| 68 | **This map's §6 recorded three tick sources "agreeing" at `0.01` from TZ-05a's read at one instant**, and a later reader would take it for a constant of the market. TZ-14 read `0.001` at 1,160 of 16,800 `/book` replies while the market document at `T0 + 5` says `0.01` at 1,198 of 1,200: the tick moves inside the interval. Nothing was computed from the old row. Architect's defect, item 55's class — a statement carried rather than read. | closed by correcting §6. Repaired by rule: **a venue constant is recorded with the instant or the population it was read over, and is never written as a constant of the market unless a measurement along the market's own time axis says so.** |
| 69 | **TZ-15 §4 could close Phase 2 in one direction only.** EDGE came from an exact test — the market's own ask rejected beyond `s*` — but NO EDGE came from `POWER >= 0.8` alone, a design quantity fixed before any label, and no row of §4 tested the pricer's claim against the outcomes. At 1,200 slots the power was `0.33` to `0.47`, so NO EDGE was out of reach before a label was read; the outcomes then fell below the pricer's claim by more than the one-per-cent lower tail of its own law at `tau` 240, 120 and 60 and to that boundary at 180 (§4), and the gate had no row that could read it. Architect's defect: power stood in for a test. | closed by ruling — TZ-15's five readings stand as UNDECIDABLE and are not re-judged; the post-hoc figures are a finding. Repaired by rule, first applied by TZ-16: **a gate whose two answers each close its question reads each from its own exact test — EDGE from the null's upper tail, NO EDGE from the alternative's lower tail, each at a false-reading probability fixed before any label is read — and power sizes the set before any label is read and decides nothing after one is.** The rule is in CANON PART II since CANON revision `2026-09-19-a`. |
| 70 | **TZ-15 §8 required the Architect to re-derive `s*`, `FP` and `POWER` from `tz15-constants.json` and `S` from `tz15-observations.csv`, and neither file can reach the Architect.** Both live in `/root/tz15-work/` on the host, in no commit and no Release, and the delivery block carries the report alone. The audit verified instead the instrument's `pb_upper`, `crit` and `select` against independent exact references — 0 disagreements over 120 critical-value cases and 20,000 selections — and every sum, count and figure the report prints that can be re-derived from it; `POWER` it could check only to about `0.002`, by a normal approximation. Architect's defect: an audit step with no route for its input. | closed by ruling — the instrument's exactness and the report's arithmetic carry the verdict, and no reading was within reach of an error of that size: `S` sits 9 to 28 below `s*`, and `POWER` at least `0.33` below the floor. Repaired by rule: **an audit requirement names the route by which each input reaches the Architect; where none exists, the report prints what the re-derivation needs — for an exact Poisson-binomial constant, the null's weights as a table of distinct prices with their counts, which fixes that law exactly, and the alternative's first four power sums, which fix its first four cumulants.** |
| 71 | **The dependence TZ-15 printed bears on nothing, and the report read its direction backwards.** §3.7 asked for the lag-1 autocorrelation of `y` and said it bears on §4's independence assumption. That assumption is independence given the prices, and `y` inherits whatever persistence the prices `a` carry, so its autocorrelation is not zero under the null and does not test it — the residual `y − a` does. The report then read the printed `+0.129` and `+0.138` at `tau` 90 and 60 as making the null's tail heavier, "which pushes against EDGE"; a null tail heavier than the independent one makes the computed `s*` too permissive, so it pushes **toward** a false EDGE — by a variance factor of about `1.26` to `1.28` at that size, were it the residual's. Nothing turns on it: no `tau` read EDGE. The report also renders the largest per-`tau` false-positive rate, `0.008749`, as `0.0088`. Architect's defect in the statistic; the report's in the direction. | closed by rule, first applied by TZ-16: **a gate that assumes independence across units measures the dependence on the null's own residual, from a set whose labels are already read and before any label it judges is read, and derives its critical values under the dependence it measured; the direction in which a dependence moves a reading is derived, never asserted.** The committed report is not edited. |
| 72 | **Three sentences of TZ-15 held on the wrong run, the wrong count or the wrong type**, and the Executor read each correctly. V6 asserted at step 3 that `git diff --name-only` names one file, and step 3 runs on every tree, where before the commit it names none — the Executor asserted a subset and reported both (its §16 item 1). V4 (c) said TZ-14's two runs left two identical copies of its observations file; TZ-14's six trial runs left six more, eight in all, a count carried from TZ-14's account of its runs rather than read (its item 3). §5.2 item 7 wrote the power as a bare `0.8` for a comparison the instrument makes in `Decimal`, and the floor-inclusive case passes only because that float rounds up (its item 4). None moves a number. Architect's defect, three times. | closed by ruling — the three readings are upheld. Repaired by rule: **every assertion a Validation row fixes names the runs on which it must hold; a count of files on the host is read by the TZ that states it, never carried from a report's account of its runs; and a literal handed to an exact comparison is written in the type the comparison uses.** |
| 73 | **Five statements were carried rather than read, three in this map and two in the CANON.** §1 said "Three of the twenty-three reports are BLOCKED reports" through at least revisions `2026-09-18-b` and `2026-09-19-a`: at `2026-09-19-a` `main` held twenty-four reports, and eight are BLOCKED reports by their own status lines — TZ-04, TZ-04a, TZ-05, TZ-07, TZ-08, TZ-10, TZ-10a and TZ-11. §2.4 still said no aggregation of the order book had been performed, a revision after TZ-14 performed one. §1's pull-request table still said PR #10's branch exists, which no `ls-remote` has shown since 2026-09-17. CANON §1.4 still gave the tick as `0.01` after item 68 corrected it here, and CANON §1.5 still said the market's quotes had never been measured after TZ-14 read them. Nothing was computed from any of them. Architect's defect, item 55's class. | closed by correcting §1 from `git ls-tree`, `ls-remote` and each report's status line, §2.4 from §2.3, and the CANON in its revision `2026-09-19-a`. Repaired by item 55's rule, extended: **every count and every "not yet" this map or the CANON states is re-read at each revision from the artifact it describes, and one that was not re-read is deleted rather than carried.** |
| 74 | **TZ-17's report named six things that could not be implemented as written, two of them the Architect's; the audit found two wrong statements and one gap.** (1) V11 was fixed "after the report commit", where contract §3.2 forbids quoting it; the Executor ran it after the branch push and before the report commit. (4) H2 read "`pgrep` prints at least one line" from `pgrep -af recorder`, and the Executor's own shell, which carried the pattern, printed the second line. The rest are disclosures: (2) `/root/tz17-work/scratch/`, a pre-run probe of one candidate's documents and three harnesses, outside §9's list; (3) an untracked `research/__pycache__/` inside `/root/tz17-work/wt`, left because that TZ removed no tree; (5) the retry, fail-fast and early-stop paths never ran live; (6) the upper bounds were not reached. **Two statements of the report are wrong and move no number:** §2.6 puts its tightest margin, `0.071` USD, on "a ~114,000 USD number, 6 × 10^-7 relative" — the 801 documents' readings run from `76,537` to `79,448` USD, so it is about `9 × 10^-7`; and §4 says the backup track's first step "did not close" beside its own PASS. **The gap:** TZ-17 inferred each settlement from the next market's `priceToBeat` while every body it stored carries the venue's own `finalPrice`. | closed. (1) by TZ-18's wording, V14 and V15 "after the branch push and before the report commit"; (4) by CANON's rule that a process-identity condition matches the whole command line exactly — TZ-18's H2, `pgrep -fx`, read one line; (3) is carried in §3's retention list; the gap by TZ-18's G-CHAIN, 1,000 of 1,000 by literal (§4). The committed report is not edited. Repaired by item 13's rule, extended: **a figure a report states about its own data is computed from that data by the instrument, never written from memory.** |
| 75 | **TZ-18 let a request defect reach a long-lived process, then left the process no way to stop.** Its run order issued no request through the instrument's own request function before R2 started the service. It cited TZ-17's 801 HTTP 200s as proof that the fifteen-minute slug is served without the request that produced them — TZ-17 sends `Accept` and its own `User-Agent`, and the edge refuses Python's default agent (§6). And §6 R5 authorized a stop only on a G-TIERC FAIL, so the G-DEPLOY FAIL left a service sending refused requests from the capture host — the host Tier C reads the venue from — with no route inside the TZ to stop it. Architect's defect, three parts. | open until TZ-18a is on `main`. Repaired by rule, now **CANON hard rule 14**: **a TZ that starts a long-lived process first issues one live request per endpoint through the process's own request function, asserted served and parsed; fixes every header of that request; and authorizes and names the process's stop on every FAIL of every gate that judges it — by the Boss's hand where the session refuses `kill` — verified from the process's own record.** And: **evidence that the venue serves a request is cited with the whole request that produced it — method, URL and every header.** |
| 76 | **Five sentences of TZ-18 conflicted, and the Executor read each correctly.** P3 forbade a price in any output file of §8 while §3.7 step 6 required `tz18-verify.csv` to carry both readings of every unit; §3.7 named `/root/tz18-work/tz18-verify.csv` while §6 sent R1 and R6 to `run-1/` and `run-3/`; V10 asked for an assert at every checkpoint and a printed count of violations, which an assert at the first one leaves unprintable; V12 required the branch commit in the `start` record while §3.8 fixed an argv with no place for it; and §3.8's single-instance rule, "that command line is this service's", did not say equal, and the build compares a substring. Architect's defect, five times. | closed by ruling — the report's §6.3 items 1 to 4 are upheld: the output directory from the run with §3.7's file names, the count printed before one final assert, the commit from a `commit.txt` beside the copy. P3's reading is upheld because every reading in that file is already in TZ-17's committed CSV, by Q1 to Q3's own equalities, and all of it lies below the boundary. The substring goes to TZ-18a as a defect (item 77). Repaired by rule, **CANON PART VI C1 as amended in CANON revision `2026-09-23-a`**: the prohibition list is intersected with every output the body requires **by content class — a price, a label, an outcome, a settled document — as well as by path**; and **an identity check a TZ asks an instrument to make on a process is written as equality with the exact argv.** |
| 77 | **TZ-18's build sent Python's default `User-Agent`, and the venue refused every request it made.** `http_get` builds `urllib.request.Request(url, method="GET")` under a docstring that says "no header but the default agent"; both hosts answer 403 `error code: 1010` (§6), so no document yielded token ids, no book was read, G-DEPLOY read 0 of 14 and no pairing skew exists. **The Executor then broke P2 to diagnose it:** nine requests outside the instrument, among them a live settled fifteen-minute document of `5,462` bytes — outside the `5,008` to `5,103` bytes of every fifteen-minute document of TZ-17's set, which the venue serves byte-stable, so not one of the 801 — whose slug the report does not name; nothing of its body was printed, stored or parsed for a price, and no number anywhere comes from it. **The report omits what its TZ's §8 item 7 required:** the SHA-256, lines and bytes of `tz18-verify.csv`, so no committed artifact anchors that file. **Two defects sit in paths the run never reached:** `http_get` stamps `recv_mono_ns` on a read that produced no reply — its conditional returns the same value on both branches — so `window.json`'s skews would count a failed read; and the single-instance check matches a substring of `/proc/{pid}/cmdline`. And one disclosed departure: a `--verify-tz17` pass at 22:52:52 UTC read the 801 bodies before the branch commit and before R0; its outputs are byte-identical to R1's. The Executor's defects, found in part by its own report and in part by the Architect's audit. | **Rejected: PR #18 closed unmerged.** G-DEPLOY's FAIL stands as the reading of the artifact that ran; G-CHAIN stands, re-derived by the Architect (§4). **TZ-18a carries:** the stop verified from `runtime.jsonl`; the `User-Agent`; both latent fixes; the pre-start request of hard rule 14; G-DEPLOY and G-TIERC re-read under the full load; the three output hashes printed; the diagnostic slug named in its own §0 from the Executor's scripts on the host; and the reclaiming of `/root/tz17-work/` and `/root/tz18-work/` (§3). Repaired by rule: **a TZ's prohibitions bind every request of the session, the Executor's own included — a diagnosis the TZ does not provide for is a BLOCKED report, never a request; and item 54's rule extends to every gated statistic: no pass computes one before the commit that computes it is pushed.** |
| 21 | The TZ-07a report's §2.5 summary carries one `eligible bins` column for two estimators whose eligibility differs — 10 / 9 / 6 / 5 / 2 / 2 uncorrected against 8 / 10 / 9 / 7 / 3 / 2 corrected. The per-tau tables are correct; only the summary is ambiguous, and G2 counts failures over eligible bins. | closed by rule: **a summary table reporting two estimators reports eligibility per estimator.** The committed report is not edited. |

---

## 8. What does not exist yet

No validated link — Phase 1 can only fail to disqualify one — no measured edge, no Polymarket
client code, no execution path, no capital at risk. Nothing in this repository can place an order.
The recorder reads; it cannot write to any venue.

Two pricers exist. `p_fair`, the normal link, fails its scale gate at `tau` 60 and 30 on two
disjoint sets, and TZ-10b measured why — the settlement residual is not normal, and less so the
smaller `tau` is. The Student pricer, fitted on the Thursday–Friday set and frozen, **is not
disqualified at `tau` 240 … 60 inside its domain**, by a gate whose false-failure probability and
power were measured before any outcome it judged was read, on 750 Tuesday-to-Thursday slots. That is
the most Phase 1 can say, and it says nothing about the market.

The weekend is the other finding. Causal volatility there runs at about a third of the weekday
level, the domain rule declines to quote on more than nine weekend intervals in ten, and every
constant this project has seen fail to transfer failed between a weekday set and that weekend. **No
set scored under the sized gate contains a weekend.**

**The market has been read twice and scored once.** TZ-14 opened 16,800 order-book replies over 1,200
intervals and found the capture complete, the book one tick wide at the median, takeable at the venue's
minimum size, emptying toward the close — two-sided at every read four minutes out and at 60% of them
one minute out — and a round trip that costs `4.1` probability points four minutes out and `1.9` one
minute out, because the fee falls as the market makes up its mind. TZ-15 then took, on paper, one share
at each of 1,924 checkpoints where the Student pricer called the ask cheap after the fee: the side it
chose won less often than the ask implied at four of five `tau`, no `tau` reads EDGE, and 1,200 slots
gave no power to say NO EDGE. After the fact the outcomes tracked the market's prices rather than the
pricer's at four of five `tau`, and the market's mid beat `p_t` on the Brier score at every `tau`.
**Nothing says the market is wrong anywhere, and nothing yet says it is right.** That is TZ-16, on
up to 3,600 qualifying slots no one has seen, with an exact test for each answer and a first look at
2,400.

**The backup track has its structure and no price.** The fifteen-minute market and the five-minute
market inside it settle on one published number, so their outcomes nest exactly, and a violation of the
nesting on executable quotes would need no pricer. No capture has stored a fifteen-minute book: the first
deployment sent Python's default agent, the venue's edge refused every request, and TZ-18a redeploys it.

The recorder is running on `4216c04` with both tiers, pid `228592`, and `/dev/vda2` held
`13,453,283,328` bytes free at TZ-18's closing read on 2026-09-22. **The consumer is stopped, measured at
fifteen reads across eight days**, and headroom is **`88` days** on §6's figure, conditional on that
service staying disabled.
Between them the pricers, the recorder and the venue's own documents have produced eleven conclusions —
the Phase 0 answer, the normal link's Phase 1 answer, the reason for it, the shape of the residual, the
closure of the Student pricer by an unsized gate, the size of the gate, the Student pricer's Phase 1
answer under it, the inventory of the book, Phase 2's first reading, undecided, the backup track's first
answer, and the identity of the reading both families settle on — one deployment proof and one
deployment that failed on its own build, the measurements of the feed and of the host that §2 and §6
record, and seven written predictions that the data refuted:
the third on its mechanism rather than its answer, the fourth on one row of five, the fifth on four rows
of six and, at `tau = 60`, on its direction, the sixth on two rows of seven — the book's two-sidedness
and the cost at the short horizons — and the seventh on two rows of five: the long shot's share of the
selection at `tau = 60`, and the gate's power to close anywhere.
**Three specifications were stopped by the Executor before any measurement existed**, and the eight
mechanical checks of CANON PART VI exist because of them; every TZ written under those
checks since has run, and each audit still found defects of the Architect's — eight in TZ-18 alone
(§7 items 75 and 76). A gate that could close its question in one direction only is why TZ-16 reads
each answer from its own exact test; a deployment that failed and could not be stopped is why a TZ
that starts a process now proves its request path before it starts and names its stop (CANON hard
rule 14).
