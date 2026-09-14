# TZ-10a — `sigma` or the link: the discriminating measurement — REPORT

**Status: BLOCKED at §7 V2, before any measurement exists.** V2 requires `u` under `sigma_hat` to
stay bit-identical when every feed report at or after the anchor is perturbed. `u` is `Y / sd`, and
`Y` is built from the reports after the anchor, so perturbing them moves `u` under any correct
implementation. No reading of the row that I could find passes it (§2).

- Every §0 gate passed first.
- The six `log_phi` self-tests of §5.2, which stopped TZ-10, were evaluated before anything was
  built. **All six pass as specified** (§4.1). They are not the blocker.

§7 V2 is byte-identical to TZ-10's, which TZ-10a carries over unchanged. Contract §6 says "a test
is never edited to make it pass … both stop the run and both require a new TZ". Contract §9 names
an unsatisfiable TZ as a BLOCKED condition.

Nothing TZ-10a asks for was computed:

- No branch `tz-10a-sigma-or-link` was created.
- `research/pfair.py` and `research/selftest-pfair.py` were not edited, and `log_phi` was not
  added.
- `research/tz10a-sigma-or-link.py` was not written.
- No set was formed and `tz06-calibration.scoring_set` was not called. No `resolution.json` and no
  `quotes.jsonl.gz` was opened.
- No `u`, `sigma_post`, `sigma_win`, `Λ`, `κ`, `λ̂`, `f`, `g` or `R²` was computed, and no
  observations file was written.

Nothing was written under `/var/lib/btc-recorder/`. The live recorder, pid `228592` on `4216c04`,
was not signalled or restarted.

Executor model: **Opus** (`claude-opus-5`), as the TZ requires.

---

## 0. Fingerprint

Read from `origin/main` = `6b8860cef02de43a2c997513d08af4ea399711b9`, fast-forwarded into the
primary checkout from `1fcd19f` on 2026-09-14. The map was last changed at
`1fad28d087591c61c0a36e81a68ef4206fd00091`, and the TZ-10a file at `6b8860c`.

**Map revision required:** `2026-09-14-b`. **Read:** `2026-09-14-b`.

| anchor | required by TZ-10a §0 | read from map §0 |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` |
| `A2` — collector | `6c5089330629` | `6c5089330629` |
| `A3` — phase | `0-complete / 1-answered-no / 2-not-started` | `0-complete / 1-answered-no / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` |
| `A6` — pricer | `cb72abb8dd8a` | `cb72abb8dd8a` |

6 of 6 anchors match. `A2`, `A4`, `A5` and `A6` were also recomputed from the files themselves, and
each equals the map's value.

### Fingerprint table

Every row of the map's §0 table, computed on `main` at `6b8860c`. Lines are `wc -l` and bytes are
`wc -c`.

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 459 | 58,464 | reported | `95d01dae142d1bcd327b39f5bee7ef1d415b8c095345cdf2cdfffc332d86f31d` | — |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | — |
| `research/pfair.py` | 281 | 12,499 | frozen | `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` | yes |
| `research/selftest-pfair.py` | 306 | 15,647 | frozen | `97de9782d319c82ee6a7d81ddbd8e00d590d85ffe2daa41abe3d71ae92712c94` | yes |
| `research/tz06-calibration.py` | 577 | 27,138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | yes |
| `research/tz07a-variance-time.py` | 619 | 28,219 | frozen | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` | yes |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | yes |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | yes |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | frozen | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | yes |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | yes |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | yes |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | yes |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | yes |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | yes |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | — |

**16 of 16 `frozen` rows match on lines, bytes and SHA-256**, and both `tracked` rows equal the
values the map prints. A scratch script parsed the map's own table, compared each row and printed
the result. The comparison is **recorded, not asserted**.

The TZ file:

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `CryptoTZ/TZ-10a-sigma-or-link.md` | 384 | 22,088 | `2688836d8e4dd981d7e9bef324d81844b4be6884e2d1d5b4c103f65db6b5e403` |

### Worktree hygiene — a disclosure, not a gate

`git worktree list --porcelain` at run start, verbatim, before the fast-forward to `6b8860c`:

```
worktree /root/btc-5m-twap
HEAD 1fcd19f0409ffa10345fc66cdd8e353d635db319
branch refs/heads/main

worktree /root/tz09-work/wt
HEAD e45f38e89b5ee18e64a16a654b341d74fadcac26
branch refs/heads/tz-09-disk-inventory

worktree /root/tz09-work/wt-report
HEAD 33483975ca7fd1a1d6778e66c1ea94ab4e28c82f
detached
```

`prunable` entries: **0**, counted by `git worktree list --porcelain | grep -c '^prunable'`. The
primary checkout `/root/btc-5m-twap` is on branch **`main`**. The fast-forward changed two paths,
`CryptoTZ/TZ-10a-sigma-or-link.md` and `SYSTEM-MAP.md`. The recorder runs none of them.

---

## 1. Host gate, resource floor and the §6 preflight

| check | required | observed |
|---|---|---|
| `/var/lib/btc-recorder/` exists and holds interval directories | yes | yes. `btc-updown-5m/` held 1,107 directories at run start and 1,113 at the last read. The first is `1789033800` |
| recorder running, newest `runtime.jsonl` start record sha | `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | pid `228592`, `/root/tz04a-env/venv/bin/python -B -u recorder.py`, started Sat Sep 12 09:53:04 2026. The newest start record is `recv_ns` `1789206785264516934`, sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` |
| filesystem | `/dev/vda2`, total `31,612,203,008` bytes | `/dev/vda2`, total `31,612,203,008` bytes |
| free space at run start | at least `10,327,051,118` bytes | `14,402,289,664` bytes at 2026-09-14T05:58:27Z |

All three host checks pass, and so does the floor.

**Every `df` read in the run**, against the `3,000,000,000` bytes the TZ requires:

| UTC | free bytes on `/dev/vda2` | at or above `3,000,000,000` |
|---|---|---|
| 2026-09-14T05:58:27Z | 14,402,289,664 | yes |
| between 05:58:27Z and 05:59:13Z, time not recorded | 14,401,892,352 | yes |
| 2026-09-14T05:59:13Z | 14,401,863,680 | yes |
| 2026-09-14T06:06:26Z | 14,401,478,656 | yes |
| 2026-09-14T06:29:25Z | 14,400,008,192 | yes |
| 2026-09-14T06:29:38Z | 14,399,922,176 | yes |

The last row was **asserted**: a Python `assert` in `/root/tz10a-work/assemble-report.py` aborts
below the bound. The rows above it were compared by reading them, so they are **recorded, not
asserted**.

At the last read the recorder was still pid `228592`, and the newest start record still carried
sha `4216c04…`. The interval count had not fallen.

### The §6 preflight — recorded, and gating nothing beyond the floor

§6 asks for two reads of `df` and `du -x -B1 -s /root/PROJECT_GAMING_PS5`, taken at least `1,800` s
apart. Both reads were taken, and they are reported as read.

| read | `df` taken (UTC) | free bytes on `/dev/vda2` | `du -x -B1 -s /root/PROJECT_GAMING_PS5` (bytes) | `du` finished (UTC) |
|---|---|---|---|---|
| 1 | 2026-09-14T05:59:13Z | 14,401,863,680 | 336,695,296 | 2026-09-14T05:59:13Z |
| 2 | 2026-09-14T06:29:25Z | 14,400,008,192 | 336,859,136 | 2026-09-14T06:29:25Z |

The two `df` reads are `1,812` s apart.

- **Free space:** it changed by `-1,855,488` bytes between the reads, a fall of `88,473,600`
  bytes/day at that rate.
- **`PROJECT_GAMING_PS5`:** it changed by `+163,840` bytes.

This is arithmetic on two reads. It is not a §3 measurement, and it applies no rule from TZ-09.

---

## 2. The blocker

TZ-10a §7, line 351:

> | V2 | causality of the causal arm | perturb every feed report at or after the anchor: `u` under
> `sigma_hat` bit-identical, 120 of 120; negative control, perturbing the last readable report
> moves it, 120 of 120. **The `sigma_post` and `sigma_win` arms are non-causal by construction and
> are exempt from V2** — this row names the exemption so no other section has to imply it |

TZ-10a §3.0, lines 112–113:

> Write `u(a, tau, s) = Y(a, tau) / pfair.corrected_sd(s, tau)` — the standardized settlement
> residual …

**`u` cannot be bit-identical under this perturbation, by construction.** TZ-10a §2 takes `Y(a,
tau)` and the anchor enumeration from `tz07b-settlement-dispersion.py`. There (`residual`, lines
162–179), `Y` is:

- at `tau >= 60`, the time-weighted mean over `[a + tau − 60, a + tau]` minus the reading in force
  at `a`;
- below 60, `tau / 60` times the mean over `[a, a + tau]` minus that reading.

Every report either mean integrates is stamped after `a`. V2 multiplies exactly those reports by a
constant. The numerator of `u` therefore moves under any correct implementation, at every anchor
and every `tau`. That is what a settlement residual is: it is the future relative to its anchor.

The failure does not depend on how the boundary is read. Perturbing reports strictly after the
anchor with the committed `tz06.perturb_after` still moves `u`, at **140 of 140** checkpoint anchors
(§3).

**Reading "`u` under `sigma_hat`" as the denominator alone does not pass either:**

- **At the checkpoint anchor**, "at or after the anchor" includes the report stamped at the anchor
  instant.
  - The `chainlink` feed stamps whole seconds, and every anchor is a whole second. TZ-08a's report
    counts 2,347 of 2,400 checkpoints with a report at the exact instant.
  - That report is the last grid point `sigma_hat` reads, and it is also the "last readable report"
    V2's negative control perturbs.
  - `sigma_hat` moves at **133 of 140** checkpoint anchors (§3). This is TZ-08's V2 defect, which
    TZ-08a §7 V2 repaired by "**strictly greater than** the checkpoint instant". TZ-10's V2, carried
    into TZ-10a, says "at or after" again.
- **At every anchor before the checkpoint**, `sigma_hat` reads reports after the anchor.
  - `sigma_hat` is TZ-07b's `sigma`: one `pfair.realised_sigma` per member per `tau`, over
    `[T0 − 300, T0 + 300 − tau]` (`member_r`, line 200). It is applied to every anchor of the
    enumeration.
  - That is what makes `Λ` reproduce under V4, and M1 runs over those anchors.
  - Perturbing strictly after the earliest anchor, `T0 − 300`, moves `sigma_hat` at **140 of 140**
    (§3). §3.0's "causal? **yes**" holds at the checkpoint anchor only.

**The only V2 that passes needs three changes.** It would have to test the denominator rather than
`u`, perturb strictly after rather than at or after, and use the checkpoint anchor only. Each
change edits the test, which contract §6 forbids. Choosing among them would substitute an
alternative, which contract §2 forbids ("do not repair a defective TZ, guess the intent, or
substitute a reasonable alternative").

The stop comes before any code is built. V2 is the only check behind §3.0's "causal? **yes**"
and behind M3's causal stratum. Building the instrument first would have produced exactly the
numbers a BLOCKED report may not carry.

---

## 3. Evidence

One scratch script outside the repository.

- It imports the committed `research/pfair.py`, `tz07b-settlement-dispersion.py`,
  `tz07a-variance-time.py` and `tz06-calibration.py` from the `main` checkout, unmodified.
- It forms `Y`, `sigma_hat` and `u` exactly as `tz07b.member_r` forms them, dividing by
  `pfair.corrected_sd` as §3.0 writes. The one-line "at or after" perturbation is the only new
  code.
- It prints and asserts nothing: **recorded, not asserted**, because it is the evidence for a stop
  and not a delivered check.

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `/root/tz10a-work/probe-v2.py` | 66 | 3,657 | `523cfca70e32d7f19357fd6a3023c19fd79b56c20d16651ca06d5e6f30508468` |

Run as `/root/tz01-env/venv/bin/python -B probe-v2.py` from `/root/tz10a-work`, in 0.8 s.

**What it reads, and what it does not.**

- **No set is formed and no outcome is read.** The intervals are the first 20 grid slots, from
  TZ-07b's first member `1789035000`, whose own and predecessor manifests exist and on whose grid
  TZ-07a M6 excludes no second. That is 20 of the 22 slots `1789035000` … `1789041300`.
- It reads every `manifest.json` (through `analyze.load_manifests`), and the `chainlink` stream of
  those 20 directories and their predecessors.
- It opens no `resolution.json`, no `twap60` and no quote file.

Each interval contributes seven checkpoint anchors, `a = T0 + 300 − tau`, and seven earliest
anchors, `a = T0 − 300`.

| perturbation of the `chainlink` stream | anchors | `u` bit-identical | `u` moved | `sigma_hat` moved |
|---|---|---|---|---|
| **V2 as written:** every report with `ts >=` the anchor, times `tz06.PERTURBATION` | 140 checkpoint | **0** | 140 | 133 |
| committed `tz06.perturb_after`, `ts >` the anchor | 140 checkpoint | **0** | 140 | 0 |
| negative control: `tz06.perturb_one` on `tz06.last_readable` | 140 checkpoint | — | 140 | not counted |
| committed `tz06.perturb_after`, `ts >` the earliest anchor `T0 − 300` | 140 earliest | **0** | 140 | 140 |

Checkpoint anchors with a `chainlink` report stamped at the exact anchor instant: **133 of 140**.

One row, `T0 1789035000` at `tau = 240`, as printed:

| quantity | unperturbed | at or after the anchor | strictly after |
|---|---|---|---|
| `u` under `sigma_hat` | 0.277633967298 | 0.274221157642 | 0.420627951446 |
| `sigma_hat` | 2.530099830422 | 2.561844256605 | 2.530099830422 |

### The probe, verbatim

```python
# TZ-10a section 7 V2 probe: the specified perturbation, applied to u under sigma_hat.
# Scratch only. Imports the committed instruments unmodified and writes nothing.
# No set is formed and no outcome is read: the intervals are the first N directories from
# TZ-07b's first member on whose grid TZ-07a M6 excludes no second.
import importlib.util, os, sys
HERE = "/root/btc-5m-twap/research"
sys.path.insert(0, HERE)
import pfair
from pfair import MS, config
from analyze import load_manifests
spec = importlib.util.spec_from_file_location("tz07b", os.path.join(HERE, "tz07b-settlement-dispersion.py"))
tz07b = importlib.util.module_from_spec(spec); spec.loader.exec_module(tz07b)
tz07a, tz06 = tz07b.tz07a, tz07b.tz07a.tz06
FIRST, N = 1789035000, 20            # map section 2.3: TZ-07b's first member

def u_parts(s3, t0, a, tau):
    """Y(a, tau), sigma_hat and u exactly as tz07b.member_r forms them, with corrected_sd."""
    keys = [ts for ts, _v in s3]
    grid = pfair.second_grid(s3, t0 + tz07b.GRID_LO, t0 + tz07b.GRID_HI)
    sigma = pfair.realised_sigma(grid[:tz07b.GRID_POINTS - tau])
    y = tz07b.residual(s3, keys, t0, grid, a, tau)
    return y, sigma, y / pfair.corrected_sd(tau, sigma)

def at_or_after(rows, ts_ms):        # V2 as written: every report with ts >= the anchor
    return [(ts, v * tz06.PERTURBATION if ts >= ts_ms else v) for ts, v in rows]

manifests = load_manifests()
chosen, t0 = [], FIRST
while len(chosen) < N:
    if manifests.get(t0) and manifests.get(t0 - config.INTERVAL_S) \
            and not tz07a.excluded_seconds(t0, manifests):
        chosen.append(t0)
    t0 += config.INTERVAL_S
print("intervals", len(chosen), chosen[0], "...", chosen[-1])

c = dict(n=0, at_instant=0, A_u=0, A_sigma=0, B_u=0, B_sigma=0, C_u=0, E_n=0, E_sigma=0, E_u=0)
example = None
for t0 in chosen:
    s3 = pfair.merged_stream(t0, config.S3_STREAM)
    stamps = {ts for ts, _v in s3}
    for tau in pfair.TAUS:
        a = config.INTERVAL_S - tau                      # the checkpoint anchor, T0 + t
        a_ms = (t0 + a) * MS
        y0, s0, u0 = u_parts(s3, t0, a, tau)
        yA, sA, uA = u_parts(at_or_after(s3, a_ms), t0, a, tau)
        yB, sB, uB = u_parts(tz06.perturb_after(s3, a_ms), t0, a, tau)
        yC, sC, uC = u_parts(tz06.perturb_one(s3, tz06.last_readable(s3, a_ms)), t0, a, tau)
        c["n"] += 1; c["at_instant"] += a_ms in stamps
        c["A_u"] += uA != u0; c["A_sigma"] += sA != s0
        c["B_u"] += uB != u0; c["B_sigma"] += sB != s0
        c["C_u"] += uC != u0
        if example is None:
            example = (t0, tau, u0, uA, uB, s0, sA, sB)
        e = tz07b.GRID_LO                                # the earliest anchor, T0 - 300
        e_ms = (t0 + e) * MS
        _y, se, ue = u_parts(s3, t0, e, tau)
        _y, sE, uE = u_parts(tz06.perturb_after(s3, e_ms), t0, e, tau)
        c["E_n"] += 1; c["E_sigma"] += sE != se; c["E_u"] += uE != ue
print("checkpoint anchors", c["n"], "; report stamped at the anchor instant", c["at_instant"])
print("A  at-or-after the anchor (V2 as written): u moved", c["A_u"], "sigma_hat moved", c["A_sigma"])
print("B  strictly after (tz06.perturb_after):    u moved", c["B_u"], "sigma_hat moved", c["B_sigma"])
print("C  negative control, last readable report: u moved", c["C_u"])
print("E  earliest anchor T0-300, strictly after: anchors", c["E_n"], "sigma_hat moved", c["E_sigma"], "u moved", c["E_u"])
t0, tau, u0, uA, uB, s0, sA, sB = example
print("example T0 %d tau %d: u %.12f | at-or-after %.12f | strictly-after %.12f" % (t0, tau, u0, uA, uB))
print("                  sigma_hat %.12f | at-or-after %.12f | strictly-after %.12f" % (s0, sA, sB))
```

---

## 4. Found in the same reading — not the blocker

### 4.1 §5.2's six self-tests pass as specified

A second scratch script evaluated the six items before anything was built, as the TZ-10 stop
taught.

- It transcribes §5.2's `log_phi` verbatim and imports the committed `pfair.phi` and
  `pfair.far_branch`.
- It prints and asserts nothing: **recorded, not asserted**. The six items are §7 V7's, and they
  were never added to `selftest-pfair.py`.

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `/root/tz10a-work/probe-selftests.py` | 56 | 2,917 | `b67ee8b24a103a38467b69d7df424309862a5567e07d6340a53d527d37a4e747` |

| item | result |
|---|---|
| 1 — the fourteen literals, 12 significant digits | **14 of 14**; the largest relative difference is `2.94e-15`, at `z = −15` |
| 2 — the branches agree to 10 significant digits at `−30`, `−32`, `−34` | **3 of 3**, at `3.49e-13`, `1.84e-13` and `1.01e-13` |
| 3 — `exp(log_phi(z)) == pfair.phi(z)` to 12 significant digits at `−3 … 3` | **7 of 7**; the largest relative difference is `5.3e-15`, at `z = −3` |
| 4 — the composition at `K = 100000.25`, `sigma = 3.25`, far branch at `tau = 240` | **4 of 4**. The recovered `z` is exactly `−10.819`, `−8.0`, `−3.0` and `0.0` as doubles |
| 5 — strictly increasing over `−40 … 5`, and finite over `−40 … 40`, step `0.001` | 45,001 points with 0 non-increasing steps; 80,001 points with 0 non-finite values |
| 6 — at `z = −10.819` | `pfair.phi` is exactly `0.0`; `log(pfair.phi(z))` is not finite; `log_phi` is finite; `exp(log_phi)` prints `1.399068e-27` under `%.6e` and is positive. All four hold |

Reading choices, all mine:

- "12 significant digits" is equality under `%.11e`, as §5.2 states, and "10" is equality under
  `%.9e`.
- Grid points are `−40 + 0.001 i`.
- **Item 6 needs a reading.** Python's `math.log(0.0)` raises `ValueError` rather than returning a
  value, so the probe counts the raise as "not finite".

### The probe, verbatim

```python
# TZ-10a section 5.2 probe: the six self-tests, evaluated before anything is built.
# Scratch only; imports the committed pricer unmodified; log_phi transcribed from section 5.2.
import math, sys
sys.path.insert(0, "/root/btc-5m-twap/research")
import pfair
from pfair import D

def log_phi(z):
    if z > -35:
        return math.log(0.5 * math.erfc(-z / math.sqrt(2)))
    return (-0.5*z*z - 0.5*math.log(2*math.pi) - math.log(-z)
            + math.log1p(-1/z**2 + 3/z**4 - 15/z**6))
def erfc_br(z): return math.log(0.5 * math.erfc(-z / math.sqrt(2)))
def asym_br(z): return (-0.5*z*z - 0.5*math.log(2*math.pi) - math.log(-z) + math.log1p(-1/z**2 + 3/z**4 - 15/z**6))
def rel(a, b): return abs(a - b) / abs(b)
LIT = [(0,"-0.693147180559945"),(-1,"-1.84102164500926"),(-2,"-3.78318433368203"),(-3,"-6.60772622151035"),
       (-4,"-10.3601014865273"),(-5,"-15.0649983939887"),(-6,"-20.7367689499747"),(-8,"-35.0134371599145"),
       (-10.819,"-61.8339909672382"),(-15,"-116.131384845712"),(-20,"-203.917155371097"),(-30,"-454.321243956343"),
       (-36,"-652.503227593835"),(-40,"-804.60844201377")]
n = 0
print("[1]")
for z, s in LIT:
    v, e = log_phi(float(z)), float(s)
    ok = "%.11e" % v == "%.11e" % e; n += ok
    print("  z=%-8s got %.15g lit %s rel %.3g ok %s" % (z, v, s, rel(v, e), ok))
print("  item1", n, "of", len(LIT))
print("[2]")
for z in (-30.0, -32.0, -34.0):
    a, b = erfc_br(z), asym_br(z)
    print("  z=%g erfc %.15g asym %.15g rel %.3g ok %s" % (z, a, b, rel(b, a), "%.9e" % a == "%.9e" % b))
print("[3]")
for z in range(-3, 4):
    a, b = math.exp(log_phi(float(z))), pfair.phi(float(z))
    print("  z=%d exp(log_phi) %.15g phi %.15g rel %.3g ok %s" % (z, a, b, rel(a, b), "%.11e" % a == "%.11e" % b))
print("[4]")
K, SIG = D("100000.25"), D("3.25")
sd = pfair.far_branch(240, K, K, SIG)[1]
for z, s in [(-10.819,"-61.8339909672382"),(-8,"-35.0134371599145"),(-3,"-6.60772622151035"),(0,"-0.693147180559945")]:
    st = K + D(repr(float(z))) * sd
    zz = float((st - K) / sd); v = log_phi(zz)
    print("  z=%s zz=%r finite %s got %.15g ok %s rel %.3g" % (z, zz, math.isfinite(v), v, "%.11e" % v == "%.11e" % float(s), rel(v, float(s))))
print("[5]")
zs = [-40 + 0.001*i for i in range(45001)]
vals = [log_phi(z) for z in zs]
bad = sum(1 for i in range(len(vals)-1) if not vals[i] < vals[i+1])
zf = [-40 + 0.001*i for i in range(80001)]
nf = sum(1 for z in zf if not math.isfinite(log_phi(z)))
print("  increasing pts", len(zs), "bad", bad, "; finite pts", len(zf), "nonfinite", nf, "last", zf[-1], log_phi(zf[-1]))
print("[6]")
z = -10.819
p = pfair.phi(z)
try: lp = math.log(p); lpf = math.isfinite(lp)
except ValueError as e: lp, lpf = repr(e), False
v = log_phi(z)
print("  phi", repr(p), "==0.0", p == 0.0, "log(phi)", lp, "finite", lpf, "log_phi finite", math.isfinite(v),
      "exp %.6e" % math.exp(v), "ok7", "%.6e" % math.exp(v) == "1.399068e-27", ">0", math.exp(v) > 0)
```

### 4.2 Other points in the text that a successor would meet

None of these was needed to reach the stop, and none was resolved. Each is stated with where it
sits.

1. **§2 against §3.0, on outcomes.**
   - §2 (line 94): "**Outcomes are read**, by M2 and by nothing else".
   - §3.0 (line 107) forms the 800 by calling `tz06-calibration.scoring_set`. Its `qualification`
     (line 69) calls `analyze.venue`, which opens every unit's `resolution.json` and reads
     `resolved_up` and `priceToBeat` (`analyze.py` lines 150–162). Conditions 2 and 3 of the set
     rule are outcome reads, for members and non-members alike.
   - This is the class of System Map §7 item 23.
2. **§3.0's `Λ` against V4's.**
   - §3.0 (line 113) says the uncentred RMS of `u` "under the pricer's own `sigma` is exactly
     TZ-07b's `Λ`".
   - `pfair.corrected_sd(tau, sigma)` is `SD_SCALE[tau] · sigma · sqrt(H(tau))` (`pfair.py` lines
     125–144). TZ-07b's `Λ` is the RMS of `Y / (sigma · sqrt(H(tau)))` (`tz07b` lines 131–141 and
     213).
   - So the RMS of `u` is `Λ / SD_SCALE[tau]`, and on the TZ-06 400 that is `1` to within the
     rounding of a six-digit literal.
   - V4 requires "TZ-07b's `Λ` table to six significant digits". `κ` and the tail fraction are
     scale-free, so this touches no verdict.
3. **"close" in §3.0's table.**
   - For `sigma_post` (line 118), "`[close, close + 300]` — the successor interval" fixes `close =
     T0 + 300`.
   - For `sigma_win` (line 119), "`[a, close]` — the window that generates `Y`" is `[a, a + tau]`
     under TZ-07b's anchor enumeration.
   - The two agree only at the checkpoint anchor. Every other anchor of M1 has two candidate
     windows.
4. **V2's count names no unit.** "120 of 120" does not say whether it counts members, observations
   or anchors, or which `tau`s and anchors are sampled.
5. **The argument order of `corrected_sd`.** §2 (line 101) says a different `sigma` is
   "`pfair.corrected_sd` with a different first argument". The function's first parameter is `tau`,
   and `sigma` is the second (`pfair.py` line 125). §3.0 writes it `corrected_sd(s, tau)`.

---

## 5. What was not done

- **V1 … V11.** Only V1's gates ran, at §0 and §1. V2 was evaluated by the probe in §3 and not as a
  delivered check. Nothing else exists for the other rows to act on.
- **Publication.** There is no branch, no pull request and no Release. This report is the only path
  the run adds to the repository.
- **§9's TZ-10 scratch step.** `/root/tz10-work/probe-log-phi.py` was not copied to
  `/root/btc-forensics/`, and `/root/tz10-work/` was not reclaimed: §9 is a step of an executed
  run, and this run stopped. The file is intact, with SHA-256
  `5eef7ae91f1ac0fbd70b2b6b724c6f4688194c537f3c09d89f42d3b2298fd481`, the value TZ-10's report names.
- **Scratch.** `/root/tz10a-work/` holds the two probes named by hash in §3 and §4.1, this report's
  draft and the script that spliced the probes and the host reads into it. Nothing outside it and
  this report was created or modified. `/root/btc-forensics/` and `/root/tz04a-env/` were not
  touched. `research/__pycache__/` was untracked before the run started, and every probe ran with
  `python -B`.
