# TZ-10 — `sigma` or the link: the discriminating measurement — REPORT

**Status: BLOCKED at §5.2 and §7 V7, before any measurement exists.** The run evaluated the five
self-tests §5.2 fixes for `log_phi`, using `log_phi` exactly as §5.2 writes it and the committed
`pfair.phi`. **Three of the five go red.**

- **Item 4** fails on its own expectation. `log_phi(−10.819)` is `−61.834`, and item 4 requires it
  to lie between `−60.0` and `−55.0`. No correct `log Phi` can pass it.
- **Items 2 and 5** fail in the lower tail. The reference they compare against, `pfair.phi`, loses
  its relative accuracy there. `log_phi` does not.

§5.2 says each test aborts the run. Contract §6 says "a test is never edited to make it pass … both
stop the run and both require a new TZ", and contract §9 names "a test goes red" as a BLOCKED
condition.

Nothing TZ-10 asks for was computed:

- No branch `tz-10-sigma-or-link` was created.
- `research/pfair.py` and `research/selftest-pfair.py` were not edited.
- `research/tz10-sigma-or-link.py` was not written.
- No set was formed, and no manifest, stream or `resolution.json` was opened.
- No `Y`, `u`, `sigma_post`, `sigma_win`, `Λ`, `κ` or `λ̂` was computed, and no observations file
  was written.

`quotes.jsonl.gz` was never opened. Nothing was written under `/var/lib/btc-recorder/`. The live
recorder, pid `228592` on `4216c04`, was not signalled or restarted.

Executor model: **Opus** (`claude-opus-5`), as the TZ requires.

---

## 0. Fingerprint

Read from `origin/main` = `c2310fe3928720f8629aeb28bf31a12a89ed60c9`, fast-forwarded into the
primary checkout on 2026-09-14. The map was last changed at
`d9beec57a2c0b96ea909cb31cda6c394a45271a3`, and the TZ-10 file at `c2310fe`.

**Map revision required:** `2026-09-14-a`. **Read:** `2026-09-14-a`.

| anchor | required by TZ-10 §0 | read from map §0 |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` |
| `A2` — collector | `6c5089330629` | `6c5089330629` |
| `A3` — phase | `0-complete / 1-answered-no / 2-not-started` | `0-complete / 1-answered-no / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` |
| `A6` — pricer | `cb72abb8dd8a` | `cb72abb8dd8a` |

6 of 6 anchors match.

### Fingerprint table

Every row of the map's §0 table, computed on `main` at `c2310fe`. Lines are `wc -l` and bytes are
`wc -c`.

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 455 | 55,417 | reported | `33612850ba982535b1eb216c6716031dc474f9c1e52a1823fc6e11400d522ae3` | — |
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
values the map prints. A scratch script compared each row against the map's own table and printed
the result. The comparison is **recorded, not asserted**.

The TZ file:

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `CryptoTZ/TZ-10-sigma-or-link.md` | 316 | 17,794 | `c08bea39dd3582d4ce8373ee5dabbe1d06357722fedad5c9f97e92f65ab4054a` |

### Worktree hygiene — a disclosure, not a gate

`git worktree list --porcelain` at run start, verbatim. This was before the fast-forward to
`c2310fe`:

```
worktree /root/btc-5m-twap
HEAD f781dc3176ba9d146912ec7ed55c3071c6ee3bda
branch refs/heads/main

worktree /root/tz09-work/wt
HEAD e45f38e89b5ee18e64a16a654b341d74fadcac26
branch refs/heads/tz-09-disk-inventory

worktree /root/tz09-work/wt-report
HEAD 33483975ca7fd1a1d6778e66c1ea94ab4e28c82f
detached
```

`prunable` entries: **0**, counted by `grep -c '^prunable'`. The primary checkout
`/root/btc-5m-twap` is on branch **`main`**. The fast-forward changed two paths,
`CryptoTZ/TZ-10-sigma-or-link.md` and `SYSTEM-MAP.md`. No file the recorder runs was among them.

---

## 1. Host gate and resource floor

| check | required | observed |
|---|---|---|
| `/var/lib/btc-recorder/` exists and holds interval directories | yes | yes. `btc-updown-5m/` held 1,102 directories at run start and 1,103 at the last read. The first is `1789033800` |
| recorder running, newest `runtime.jsonl` start record sha | `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | pid `228592`, `/root/tz04a-env/venv/bin/python -B -u recorder.py`, started Sat Sep 12 09:53:04 2026. The newest start record is `recv_ns` `1789206785264516934`, sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` |
| filesystem | `/dev/vda2`, total `31,612,203,008` bytes | `/dev/vda2`, total `31,612,203,008` bytes |
| free space at run start | at least `10,327,051,118` bytes | `14,403,325,952` bytes at 2026-09-14T05:36:09Z |
| every later `df` read | at least `3,000,000,000` bytes | `14,402,342,912` bytes at 2026-09-14T05:39:08Z |

All three host checks pass, and so does the floor, at both reads.

---

## 2. The blocker

TZ-10 §5.2, from line 263:

> Self-tests, each aborting the run, added to `selftest-pfair.py`:
>
> 2. `log_phi(z)` agrees with `log(phi(z))` to 12 significant digits for `z` in `−8 … 0`, at eleven
>    points, at realistic magnitude …
>
> 4. `log_phi(−10.819)` is finite and lies between `−60.0` and `−55.0`;
>
> 5. `exp(log_phi(z)) == phi(z)` to 12 significant digits for `z` in `−8 … 8`.

§7 V7 requires "the five self-tests of §5.2, each aborting".

**Item 4 is a defective expectation.** The expectation it fixes excludes the true value.

- `log_phi(−10.819)` is `−61.833990967238` on the `erfc` branch §5.2 selects for `z > −35`.
- §5.2's own asymptotic branch, evaluated at the same point, gives `−61.833991491603`. The
  `5.2e-7` gap is the series truncation at `|z| ≈ 10.8`.
- Both lie `1.83` below the lower bound of `−60.0`.
- `exp(−61.834)` is `1.399e-27`. The map already states this figure in its §4 row on `T0
  1789268400`: "`Φ` assigned about 1e-27". The natural log of `1e-27` is `−62.17`. The map's figure
  and item 4's range therefore contradict each other.

An implementation that passes item 4 would be computing something other than `log Phi`.

**Items 2 and 5 go red where `pfair.phi` itself is inaccurate.**

- `pfair.phi` is `0.5 * (1 + erf(z / sqrt(2)))`. Below about `z = −5`, `1 + erf(·)` is the sum of
  two doubles of magnitude 1 and opposite sign. Its absolute error stays near `1e-16`, so its
  relative error grows as `Phi` shrinks.
- §5.2's `log_phi` uses `erfc`, which keeps its relative accuracy in the tail.
- At `z = −8`, `pfair.phi` returns `6.10622663543836e-16`. `exp(log_phi(−8))` gives
  `6.22096057427181e-16`, and `Phi(−8)` is `6.22096e-16`, so `pfair.phi` is the one that is `1.8%`
  off.
- Item 2 compares `log_phi` against `log(pfair.phi)`, and item 5 compares `exp(log_phi)` against
  `pfair.phi`. At `z = −8` their relative disagreements are `5.3e-4` and `1.9e-2`.

`−8` is an endpoint of the range both items state, so neither passes whatever grid is chosen or
however "12 significant digits" is read.

The two readings open to me both stop the run:

- **As written:** items 2, 4 and 5 fail. §5.2 makes each one abort the run.
- **Adjusting them to pass:** that would mean widening item 4's range, trimming the tail from items
  2 and 5, or comparing against something other than `phi`. Each of those edits a test to make it
  pass, which contract §6 forbids. Contract §2 says the Executor does "not repair a defective TZ,
  guess the intent, or substitute a reasonable alternative".

The stop comes before any measurement. V7 is where these tests are first required. `log_phi` is
what M2's likelihood is defined over (§3.2: "The likelihood uses `log_phi` (§5.2) and never
`log(phi(...))`"), so no `λ̂` of any kind could be computed without it.

---

## 3. Evidence

One scratch script outside the repository. It imports the committed `research/pfair.py` from the
`main` checkout, unmodified, for `phi`, `far_branch` and `D`. It transcribes §5.2's `log_phi`
formula verbatim. It prints its results and asserts nothing: **recorded, not asserted**, because it
is the evidence for a stop and not a delivered check.

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `/root/tz10-work/probe-log-phi.py` | 56 | 2,685 | `5eef7ae91f1ac0fbd70b2b6b724c6f4688194c537f3c09d89f42d3b2298fd481` |

Run as `/root/tz01-env/venv/bin/python -B /root/tz10-work/probe-log-phi.py`.

Reading choices, all mine:

- "Agrees to 12 significant digits" is taken as equality under `%.11e` formatting. The relative
  difference is printed beside it, so any other reading can be applied to the same numbers.
- For item 2, the eleven points are `−8 + 0.8 i`, `i = 0 … 10`. Each is formed at live scale: `z =
  (S_t − K) / sd`, with `K = 100000.25`, `sd = pfair.far_branch(240, K, K, 3.25)[1]` and `S_t = K +
  z_target · sd`.
- For item 5, the points are the seventeen integers `−8 … 8`, formed the same way.
- For item 3, the grid runs over `−40 … 5` in steps of `0.001`.

The probe's first printed line is labelled "sha check" but prints the byte count of `pfair.py`,
`12499`. The file's hash is in §0.

### E1 — item 4

| quantity | value |
|---|---|
| `log_phi(−10.819)`, `erfc` branch | `−61.833990967238` |
| finite | yes |
| in `[−60.0, −55.0]` | **no** |
| §5.2's asymptotic branch at the same `z` | `−61.833991491603` |
| `exp(log_phi(−10.819))` | `1.39907e-27` |
| `pfair.phi(−10.819)` | `0.0` |

### E2 — item 2, `log_phi(z)` against `log(pfair.phi(z))`

| `z` | `log_phi` | `log(phi)` | relative difference | equal to 12 sig. digits |
|---|---|---|---|---|
| −8.0 | −35.0134371599145 | −35.0320524774387 | 5.31e-4 | **no** |
| −7.2 | −28.8314575203219 | −28.831543303396 | 2.98e-6 | **no** |
| −6.4 | −23.2783141859372 | −23.2783143023803 | 5.0e-9 | **no** |
| −5.6 | −18.3513794959093 | −18.3513794957775 | 7.18e-12 | **no** |
| −4.8 | −14.0470288900935 | −14.0470288901271 | 2.39e-12 | yes |
| −4.0 | −10.3601014865273 | −10.3601014865273 | 0 | yes |
| −3.2 | −7.28297550290363 | −7.28297550290361 | 2.07e-15 | yes |
| −2.4 | −4.80392166687067 | −4.80392166687067 | 3.7e-16 | yes |
| −1.6 | −2.90407801030224 | −2.90407801030224 | 1.53e-16 | yes |
| −0.8 | −1.55185131918778 | −1.55185131918778 | 0 | yes |
| 0.0 | −0.693147180559945 | −0.693147180559945 | 0 | yes |

**7 of 11** agree; the four that do not are the four lowest.

### E3 — item 5, `exp(log_phi(z))` against `pfair.phi(z)`

| `z` | `exp(log_phi)` | `phi` | relative difference | equal to 12 sig. digits |
|---|---|---|---|---|
| −8 | 6.22096057427181e-16 | 6.10622663543836e-16 | 1.88e-2 | **no** |
| −7 | 1.27981254388583e-12 | 1.27980959163665e-12 | 2.31e-6 | **no** |
| −6 | 9.86587645037701e-10 | 9.86587644913328e-10 | 1.26e-10 | **no** |
| −5 | 2.86651571879195e-07 | 2.86651571868024e-07 | 3.9e-11 | **no** |
| −4 … 8 | — | — | at most 5.3e-15 | yes, 13 of 13 |

**13 of 17** agree; the four that do not are the four lowest.

### E4 — items 1 and 3, which pass

| item | result |
|---|---|
| 1 — the two branches agree to 10 significant digits at `−30`, `−32`, `−34` | 3 of 3. Relative differences are `3.49e-13`, `1.84e-13` and `1.01e-13` |
| 3 — `log_phi` strictly increasing over `−40 … 5` | 45,001 points; 0 non-increasing steps |

### The probe, verbatim

```python
# TZ-10 section 5.2 probe: the specified log_phi against the committed pfair.phi.
# Scratch only; imports the committed pricer unmodified.
import math, sys
sys.path.insert(0, "/root/btc-5m-twap/research")
import pfair
from pfair import D

def log_phi(z):   # TZ-10 section 5.2, transcribed
    if z > -35:
        return math.log(0.5 * math.erfc(-z / math.sqrt(2)))
    return (-0.5*z*z - 0.5*math.log(2*math.pi) - math.log(-z)
            + math.log1p(-1/z**2 + 3/z**4 - 15/z**6))

def rel(a, b):
    return abs(a - b) / abs(b)

def sig12(a, b):
    return "%.11e" % a == "%.11e" % b

K, SIGMA = D("100000.25"), D("3.25")
sd = pfair.far_branch(240, K, K, SIGMA)[1]          # sigma*sqrt(200), live scale
def z_at(target):                                   # z formed as state / sd at K = 100000.25
    s_t = K + D(repr(target)) * sd
    return float((s_t - K) / sd)

print("pfair.py sha check:", open(pfair.__file__,'rb').read().__len__(), "bytes")
print("\n[1] branch agreement at -30,-32,-34 (10 sig digits)")
for z in (-30.0, -32.0, -34.0):
    a = math.log(0.5*math.erfc(-z/math.sqrt(2)))
    b = (-0.5*z*z - 0.5*math.log(2*math.pi) - math.log(-z) + math.log1p(-1/z**2 + 3/z**4 - 15/z**6))
    print("  z=%g  erfc-branch %.15g  asymptotic %.15g  rel %.3g  10sd-equal %s" % (z, a, b, rel(b, a), "%.9e" % a == "%.9e" % b))

print("\n[2] log_phi(z) vs log(pfair.phi(z)), 11 points on -8..0, z formed at K=100000.25, sigma=3.25")
for i in range(11):
    z = z_at(-8 + 0.8*i)
    a, p = log_phi(z), pfair.phi(z)
    b = math.log(p)
    print("  z=%+.6f  log_phi %.15g  log(phi) %.15g  rel %.3g  12sd-equal %s" % (z, a, b, rel(a, b), sig12(a, b)))

print("\n[3] strictly increasing over -40..5, step 0.001")
zs = [-40 + 0.001*i for i in range(45001)]
vals = [log_phi(z) for z in zs]
bad = [(zs[i], vals[i], vals[i+1]) for i in range(len(vals)-1) if not vals[i] < vals[i+1]]
print("  points", len(zs), "non-increasing steps", len(bad), bad[:3])

print("\n[4] log_phi(-10.819), required finite and in [-60.0, -55.0]")
v = log_phi(-10.819)
print("  log_phi(-10.819) = %.12f  finite %s  in range %s" % (v, math.isfinite(v), -60.0 <= v <= -55.0))
print("  exp of it = %.6g ; pfair.phi(-10.819) = %r" % (math.exp(v), pfair.phi(-10.819)))
print("  asymptotic branch at -10.819 = %.12f" % (-0.5*10.819**2 - 0.5*math.log(2*math.pi) - math.log(10.819) + math.log1p(-1/10.819**2 + 3/10.819**4 - 15/10.819**6)))

print("\n[5] exp(log_phi(z)) vs pfair.phi(z), z in -8..8, 17 integer points")
for k in range(-8, 9):
    z = z_at(float(k))
    a, b = math.exp(log_phi(z)), pfair.phi(z)
    print("  z=%+.6f  exp(log_phi) %.15g  phi %.15g  rel %.3g  12sd-equal %s" % (z, a, b, rel(a, b), sig12(a, b)))
```

---

## 4. Found in the same reading — not the blocker

**§2 and §5.2 disagree about `selftest-pfair.py`.** §2's "May be touched" list names two repository
paths: the new `research/tz10-sigma-or-link.py`, and `research/pfair.py`, additively. §5.2 adds five
self-tests to `research/selftest-pfair.py`, which the map's §0 table lists as `frozen`. §2's "May
not be touched" list does not name it either. The run stopped before either reading had to be
chosen, and no remedy is proposed.

---

## 5. What was not done

- **§6 preflight.** The first `df` and `du -x -B1 -s /root/PROJECT_GAMING_PS5` read was taken at
  run start. The second, due at least `1,800` s later, was not, because the run stopped first.
  Section 1 carries the free-space figure only as a floor check. The `du` figure is not reported,
  because one read is not the measurement §6 defines and a BLOCKED report carries no partial
  measurement.
- **V2–V6 and V8–V11.** Not run. No code, set or statistic exists for them to act on.
- **Publication.** There is no branch, no pull request and no Release. This report is the only path
  the run adds to the repository.
- **Scratch.** `/root/tz10-work/` holds the one probe named in §3 and nothing else. Nothing outside
  it and this report was created or modified. `/root/btc-forensics/` and `/root/tz04a-env/` were
  not touched.
