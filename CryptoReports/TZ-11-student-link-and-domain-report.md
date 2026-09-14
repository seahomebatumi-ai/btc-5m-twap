# TZ-11 — the Student link and the domain it is priced on — REPORT

**Status: BLOCKED at §5.2 item 5, before any code is built and before any constant is
measured.** Item 5 requires `p_fair_student` at `tau = 30` to return `F_3(−10.819)`. §5.1 defines
`p_fair_student` to evaluate `F` at `LINK_NU[30]`, and §3.2 makes `LINK_NU[30]` the fitted `ν̂`,
frozen at six significant digits. So the item passes only if a fit that has not yet been run lands
exactly on `3.00000`. At the neighbouring six-digit values it already fails by five orders of
magnitude (§2). The item tests the data, not the code, and contract §6 does not allow a test to be
edited to make it pass.

- Every §0 gate passed first: 6 of 6 anchors, 17 of 17 `frozen` rows, the three
  host checks and the resource floor. Both §0 preflight reads were taken, 8,791 s apart (§1).
- §5.2's items 1 to 4 were evaluated before anything was built, with §5.1 transcribed exactly.
  **All four pass as specified** (§4.1), so they are not the blocker. Item 6 reads the three
  tables and needs them to exist.
- Several other points in the text would need a reading, among them V6's "insertions only" against
  §5.3's new parameter, and §2's outcome rule against V4. They are listed in §4.2. **This stop does
  not rest on any of them.**

Nothing TZ-11 asks for was computed:

- `research/pfair.py`, `research/selftest-pfair.py` and `research/tz07a-variance-time.py` were not
  edited, and `research/tz11-student-link.py` was not written.
- No `ADMIT`, `LINK_NU` or `LINK_SCALE` was measured. No `r` walk was run.
- No `ν̂`, `ŝ`, `κ`, `λ̂`, Brier, bin table or influence figure was computed, and no label entered any
  number.
- No branch was pushed, and no pull request or Release exists. A local branch and worktree were
  created at start-up, before the probes. No file in them was ever changed. Both were removed
  before this report was written (§5).

Nothing was written under `/var/lib/btc-recorder/`, and no `quotes.jsonl.gz` or `gamma.json` was
opened. The live recorder, pid `228592` on `4216c04`, was not signalled or restarted.

Executor model: **Opus** (`claude-opus-5`), as the TZ requires.

---

## 0. Fingerprint

The spec was read from `origin/main` = `ecc5a0bf4792f995790c5c329a48b68a0358f256`, fast-forwarded into the primary checkout
from `69b8b57` on 2026-09-14. The map was last changed at `86dc60d482bc5688b3c2cdeab72380398ee04404`, and the TZ-11 file
arrived at `ecc5a0b`. The run started at about 13:17Z. Its first timed read is 13:18:30Z.

**Map revision required:** `2026-09-14-d`. **Read:** `2026-09-14-d`.

| anchor | required by TZ-11 §0 | read from map §0 |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` |
| `A2` — collector | `6c5089330629` | `6c5089330629` |
| `A3` — phase | `0-complete / 1-answered-no / 2-not-started` | `0-complete / 1-answered-no / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` |
| `A6` — pricer | `45b307b221d4` | `45b307b221d4` |

**6 of 6 anchors match.** `A2`, `A4`, `A5` and `A6` were also recomputed from the files
themselves, and each equals the map's value. `A1` is a Release asset and is not on disk.

### Fingerprint table

This covers every row of the map's §0 table, computed on `main` at `ecc5a0b`. Lines
are `wc -l` and bytes are `wc -c`. The scratch script `gate-check.py` parsed the map's own table and
compared each row. It asserts the frozen count, the revision string and the six anchors.

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 550 | 77,466 | reported | `b746ee33b019c0b774fa5929fad589cfebec23d31977647be7538c7838527f01` | — |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | — (equal to the map) |
| `research/pfair.py` | 313 | 13,985 | frozen | `45b307b221d410a7812759a89941dc7645dfda165a8e01a60aef5b17851a5d1e` | yes |
| `research/selftest-pfair.py` | 441 | 22,643 | frozen | `7e641c93ea0244890f2726629b9f28a76d8f078b43da47e9cd9a16dbb43f223a` | yes |
| `research/tz06-calibration.py` | 577 | 27,138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` | yes |
| `research/tz07a-variance-time.py` | 619 | 28,219 | frozen | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` | yes |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | yes |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` | yes |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | frozen | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` | yes |
| `research/tz10b-sigma-or-link.py` | 1,224 | 61,018 | frozen | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` | yes |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | yes |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | yes |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | yes |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | yes |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | yes |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | — (equal to the map) |

**17 of 17 `frozen` rows match on lines, bytes and SHA-256, and 2 of 2 `tracked` rows equal the map.**

The TZ file:

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `CryptoTZ/TZ-11-student-link-and-domain.md` | 487 | 29,765 | `15220788b164ee4d53d32892061bbc2ebd1509acf30282dd453af2c6df86775f` |

`A6` is `45b307b221d4`, as TZ-11 §0 requires. The value is the same before and after this run,
because `research/pfair.py` was not touched.

### Worktree hygiene — a disclosure, not a gate

`git worktree list` at run start showed four worktrees: the primary checkout on `main` at
`ecc5a0b`, `/root/tz09-work/wt`, `/root/tz09-work/wt-report` and `/root/tz10b-work/wt`. The
run then added `/root/tz11-work/wt` on a new local branch, `tz-11-student-link`, at `ecc5a0b`.
It removed both again before writing this report (§5). `git worktree list --porcelain` after the
removal, verbatim:

```
worktree /root/btc-5m-twap
HEAD ecc5a0bf4792f995790c5c329a48b68a0358f256
branch refs/heads/main

worktree /root/tz09-work/wt
HEAD e45f38e89b5ee18e64a16a654b341d74fadcac26
branch refs/heads/tz-09-disk-inventory

worktree /root/tz09-work/wt-report
HEAD 33483975ca7fd1a1d6778e66c1ea94ab4e28c82f
detached

worktree /root/tz10b-work/wt
HEAD d34606ee9a592e51293eaad0996c7cae3b84dfcd
branch refs/heads/tz-10b-sigma-or-link
```

The primary checkout `/root/btc-5m-twap` stayed on `main` for the whole run. The recorder runs
from it.

---

## 1. Host gate, resource floor and the §0 preflight

| check | required | observed |
|---|---|---|
| `/var/lib/btc-recorder/btc-updown-5m/` exists and holds interval directories | yes | yes. It held 1,194 directories at the host gate, the newest `1789391700`, and 1,226 at this report's assembly, the newest `1789401300` |
| recorder running; newest `runtime.jsonl` start record sha | `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | pid `228592`, `/root/tz04a-env/venv/bin/python -B -u recorder.py`, started Sat Sep 12 09:53:04 2026. The newest start record is `recv_ns` `1789206785264516934`, sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` |
| filesystem | `/dev/vda2`, total `31,612,203,008` bytes | `/dev/vda2`, total `31,612,203,008` bytes |
| free space at run start | at least `2,060,000,000` bytes | `14,337,896,448` bytes at 2026-09-14T13:18:30Z |

**All three host checks pass, and so does the floor.**

**Every read of free space in the run.** TZ-11 §0 requires each later read to be at least
`2,000,000,000` bytes:

| UTC | free bytes on `/dev/vda2` | read by | at or above the floor |
|---|---|---|---|
| before 13:18:30Z, time not recorded | 14,338,179,072 | host gate (`df -B1 /dev/vda2`) | yes — recorded, not asserted |
| 2026-09-14T13:18:30Z | 14,337,896,448 | §0 preflight read 1 (`df`) | yes — recorded, not asserted |
| 2026-09-14T15:45:01Z | 14,329,606,144 | §0 preflight read 2 (`df`) | yes — recorded, not asserted |
| 2026-09-14T15:56:06Z | 14,330,757,120 | this report's assembler (`os.statvfs`) | yes — **asserted** |

The first row was printed to the terminal by the host-gate `df` and was not saved to a file. The
last row is **asserted**: the assembler that wrote this report aborts below `2,000,000,000`.
Every other row was compared by reading it, so it is **recorded, not asserted**. At the last read,
the recorder was still pid `228592`, the newest start record still carried sha `4216c04…`, and the
interval count had not fallen.

### The §0 preflight — recorded, and gating nothing beyond the floor

§0 asks for `df -B1 /dev/vda2`, `du -x -B1 -s /root/PROJECT_GAMING_PS5` and
`systemctl is-enabled` / `is-active telemetry-watch.service`. They are taken at run start and
again at least `1,800` s later, each captured with its exit status. Both reads were taken, and
they are reported as read. No file of that project was opened: `du` reads sizes only.

| read | `df` taken (UTC) | free bytes on `/dev/vda2` | `du` of `/root/PROJECT_GAMING_PS5` (bytes) | `is-enabled` (exit) | `is-active` (exit) |
|---|---|---|---|---|---|
| 1 | 2026-09-14T13:18:30Z | 14,337,896,448 | 354,009,088 | `disabled` (1) | `inactive` (3) |
| 2 | 2026-09-14T15:45:01Z | 14,329,606,144 | 354,582,528 | `disabled` (1) | `inactive` (3) |

The two `df` reads are **8,791 s** apart. That is more than the `1,800` s asked for, because a
usage limit paused the session between them (§5).

- **Free space:** it changed by `-8,290,304` bytes, which is **`-81,479,043` bytes/day** at that rate.
- **`PROJECT_GAMING_PS5`:** it changed by `+573,440` bytes, which is **`+5,635,902` bytes/day**.
  Against TZ-10b's third read, `374,718,464` bytes at 2026-09-14T11:12:25Z, the tree is
  `20,135,936` bytes smaller.
- **`telemetry-watch.service`:** it was `disabled` with exit status 1, and `inactive` with exit
  status 3, at both reads.

**This run's own footprint is stated separately** (System Map §7 item 29).

- `/root/tz11-work` was created by the same command as read 1. At read 2 it held
  `1,904,640` bytes on disk. Most of that was the checked-out worktree, which was removed
  afterwards.
- The session store `/root/.claude` held `107,630,592` bytes at read 2. It was not measured at
  read 1, so its growth over the window is unknown.
- The recorder's own measured rate, `33,632,842` bytes/day on disk (map §6), is about
  `3,422,064` bytes over this window.

This is arithmetic on two reads. It applies no rule from TZ-09, and it gates nothing.

---

## 2. The blocker

TZ-11 §5.2 item 5, lines 369–373:

> **Item 5 — the pathology removed, at live scale.** At `K = 100000.25`, `sigma = 3.25`,
> `tau = 30`, built through `state_and_sd`, `student_sd` and `p_fair_student` at `ν = 3`: at the
> `S_t` that recovers `z = −10.819`, `p_fair` is exactly `0.0` and its log is not finite, while
> `p_t` is `8.4465826393e-04` to 10 significant digits and `log_t_cdf` is `-7.07657843379202`.
> The literals come from item 1's reference.

TZ-11 §5.1, lines 322–324, defines the tables and the function the item names:

```
ADMIT, LINK_NU, LINK_SCALE     the three measured tables, Decimal literals, keys = TAUS
student_sd(tau, sigma)         LINK_SCALE[tau] * sigma * H(tau).sqrt(), H as corrected_sd has it
p_fair_student(state, sd, tau) t_cdf(float(state / sd), float(LINK_NU[tau]))
```

TZ-11 §3.2, lines 205–208, fixes what `LINK_NU[30]` is:

> **M1 is then repeated on the admissible members of the fit set**, and those two tables — `ν̂(tau)`
> and `ŝ(tau)` — are frozen into `pfair.py` as `LINK_NU` and `LINK_SCALE`, six significant digits,
> under the same per-`tau` assert.

V8 (lines 444–446) asserts that each literal equals this run's own measurement before any table is
printed.

**`p_fair_student` takes no `ν` argument.** At `tau = 30` it evaluates `F` at `LINK_NU[30]`. That
is the maximum-likelihood `ν̂` of a fit that has not been run, rounded to six significant digits.
Item 5's `p_t` literal is `F_3(−10.819)`, the number TZ-11 §1 quotes. So:

- **The `p_t` comparison passes if and only if §3.2's fit returns `3.00000`** at six significant
  digits.
- **It is steep in `ν`.** At the six-digit neighbours `2.99999` and `3.00001`, `p_t` already
  differs from the literal by `1.49e-05` relative. The item asks for 10 significant digits,
  which allows about `1e-10`. The `log_t_cdf` literal differs by `2.11e-06` relative at
  the same neighbours, against the `1e-12` item 1 uses.
- **The scale does not matter.** The recovered `z` is exactly `−10.819` as a double, whatever
  `LINK_SCALE[30]` is. Only `ν` moves `p_t` (§3).

So the item tests what the data will say, not what the code does. Any outcome of §3.2's fit other
than exactly `3.00000` turns it red. Contract §6: "A test is never edited to make it pass. A red
test is either a product defect or a defective expectation. Both stop the run and both require a
new TZ."

**Two changes would make it pass, and the text forbids both:**

- **Evaluate `p_t` as `t_cdf(z, 3.0)`, without going through `p_fair_student`.** That drops the
  function the item says it is "built through". It swaps in a different test, which contract §2
  forbids ("do not repair a defective TZ, guess the intent, or substitute a reasonable
  alternative").
- **Hold `LINK_NU[30]` at `3` for the length of the item.** That is a run-time substitution. §5.3
  (line 392) says "No name is rebound at run time anywhere in this TZ", and map §7 item 43 says
  "Substitution at run time is never the design".

**The stop comes before anything is built or measured.** V7 requires `selftest-pfair.py`, with
§5.2's family in it, to exit 0. §3.2's fit would have to run first for `LINK_NU` to exist, and it
would produce a frozen table this report may not carry. `LINK_NU[30]` was not measured. The stop
does not depend on its value, except in the one case where it is exactly `3.00000`.

---

## 3. Evidence

The evidence is one scratch script outside the repository, `probe-selftests.py`.

- It writes §5.1's `log_beta`, `_betacf`, `log_betainc_reg`, `log_t_cdf` and `t_cdf` exactly as
  §5.1 specifies them, with `LOG_BETA_CF_MAX = 300` and `LOG_BETA_TOL = 1e-16`. The continued
  fraction is the modified Lentz form of `I_x(a, b)`.
- It imports only the committed `research/pfair.py`, unmodified, from the `main` checkout. It uses
  that file for `phi`, `p_fair`, `state_and_sd` and the horizon constants.
- For item 5 it writes `student_sd` and `p_fair_student` as §5.1 defines them. They read a table
  passed in, which is filled with candidate literals because `LINK_NU` does not exist.
- It reads no capture file and no outcome.
- It prints and asserts nothing, so it is **recorded, not asserted**. It is evidence for a stop,
  not a delivered check.

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `/root/tz11-work/probe-selftests.py` | 178 | 7,024 | `ede6a0b4948f66fbf6c3d6156e1225444ab8b42936f36cbc8a6fc6afeb14df9b` |

It was run as `python3 -B probe-selftests.py` from `/root/tz11-work`. This report's assembler ran
it again, and its output was **asserted** identical to the saved output, `probe-selftests.out`
(`52b93f42b2f703a79f67c062582c66dfe86432d23fb58b27e74f1b49304d4dce`).

Item 5's part of the output, verbatim. The first three rows vary `LINK_SCALE[30]` at `ν = 3`. The
last five pass each candidate `LINK_NU[30]` through `p_fair_student`, with `m_r = S_t`, so the near
branch's `state` is `S_t − K`:

```
item 5
  LINK_SCALE 1: z -10.819, phi 0.0, F_3 8.4465826393e-04 (want 8.4465826393e-04), log -7.07657843379202
  LINK_SCALE 1.2: z -10.819, phi 0.0, F_3 8.4465826393e-04 (want 8.4465826393e-04), log -7.07657843379202
  LINK_SCALE 1.38581: z -10.819, phi 0.0, F_3 8.4465826393e-04 (want 8.4465826393e-04), log -7.07657843379202
  if LINK_NU[30] were 2.2: F(-10.819) = 2.9952601976e-03, log -5.8107241738761
  if LINK_NU[30] were 2.5: F(-10.819) = 1.8303604978e-03, log -6.30324233817012
  if LINK_NU[30] were 3.5: F(-10.819) = 4.0961228762e-04, log -7.80029948561353
  if LINK_NU[30] were 4: F(-10.819) = 2.0703014310e-04, log -8.48264615644609
item 5, through section 5.1's own p_fair_student
  LINK_NU[30] = 2.99999: z -10.819  p_fair 0.0  p_t 8.4467088184e-04  relative to 8.4465826393e-04 1.49e-05  10 significant digits False  log_t_cdf -7.07656349542014  relative to the literal 2.11e-06
  LINK_NU[30] = 3.00000: z -10.819  p_fair 0.0  p_t 8.4465826393e-04  relative to 8.4465826393e-04 7.86e-14  10 significant digits True  log_t_cdf -7.07657843379202  relative to the literal 1.26e-16
  LINK_NU[30] = 3.00001: z -10.819  p_fair 0.0  p_t 8.4464564622e-04  relative to 8.4465826393e-04 1.49e-05  10 significant digits False  log_t_cdf -7.07659337214417  relative to the literal 2.11e-06
  LINK_NU[30] = 2.50000: z -10.819  p_fair 0.0  p_t 1.8303604978e-03  relative to 8.4465826393e-04 1.17  10 significant digits False  log_t_cdf -6.30324233817012  relative to the literal 0.109
  LINK_NU[30] = 3.50000: z -10.819  p_fair 0.0  p_t 4.0961228762e-04  relative to 8.4465826393e-04 0.515  10 significant digits False  log_t_cdf -7.80029948561353  relative to the literal 0.102
```

### The probe, verbatim

```python
# TZ-11 probe, scratch only: section 5.1's functions written exactly as the TZ specifies them,
# evaluated against section 5.2's six items before anything is built in the repository.
# Nothing here is committed. It reads nothing but pfair.py (for phi, state_and_sd, H).
import math
import sys

sys.path.insert(0, "/root/btc-5m-twap/research")
import pfair
from pfair import D

LOG_BETA_CF_MAX = 300
LOG_BETA_TOL = 1e-16
TINY = 1e-300
ITER = {"max": 0, "raised": []}


def log_beta(a, b):
    return math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)


def _betacf(a, b, x):
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < TINY:
        d = TINY
    d = 1.0 / d
    h = d
    for m in range(1, LOG_BETA_CF_MAX + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < TINY:
            d = TINY
        c = 1.0 + aa / c
        if abs(c) < TINY:
            c = TINY
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < TINY:
            d = TINY
        c = 1.0 + aa / c
        if abs(c) < TINY:
            c = TINY
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < LOG_BETA_TOL:
            ITER["max"] = max(ITER["max"], m)
            return h
    ITER["raised"].append((a, b, x))
    raise ArithmeticError("no convergence a=%r b=%r x=%r" % (a, b, x))


def log_betainc_reg(a, b, x):
    if x >= 1:
        return 0.0
    if x <= 0:
        raise ValueError(x)
    if x < (a + 1) / (a + b + 2):
        return (a * math.log(x) + b * math.log1p(-x) - math.log(a) - log_beta(a, b)
                + math.log(_betacf(a, b, x)))
    return math.log1p(-math.exp(log_betainc_reg(b, a, 1 - x)))


def log_t_cdf(z, nu):
    if z <= 0:
        return log_betainc_reg(nu / 2, 0.5, nu / (nu + z * z)) - math.log(2)
    return math.log1p(-math.exp(log_t_cdf(-z, nu)))


def t_cdf(z, nu):
    return math.exp(log_t_cdf(z, nu))


def rel(a, b):
    return abs(a - b) / abs(b)


ZS = ("0", "-1", "-3", "-5", "-8", "-10.819", "-20", "-50")
LIT = {
    2: "-0.693147180559945 -1.55435868307644 -3.04213264974235 -3.96992886866936 -4.87513859809586 -5.46847054829007 -6.68835316116258 -8.51779297152817",
    2.5: "-0.693147180559945 -1.59933653536950 -3.31626685434013 -4.44598122091119 -5.56532867478168 -6.30324233817012 -7.82481099775613 -10.1104508277657",
    3: "-0.693147180559945 -1.63218922449412 -3.54618467545091 -4.86702610492042 -6.19564464966101 -7.07657843379202 -8.89844171394626 -11.6397847632440",
    4: "-0.693147180559945 -1.67691149318135 -3.91347485706189 -5.58727573561669 -7.32032286818778 -8.48264615644609 -10.9009041296344 -14.5521443574038",
    7: "-0.693147180559945 -1.74120896160071 -4.60806807421352 -7.15283904545879 -9.99615988572270 -11.9667403968485 -16.1409126343562 -22.5096639254306",
}

print("item 1")
worst, fmt_diff = 0.0, []
for nu, row in LIT.items():
    for z, want in zip(ZS, row.split()):
        got = log_t_cdf(float(z), float(nu))
        r = rel(got, float(want))
        worst = max(worst, r)
        if "%.11e" % got != "%.11e" % float(want):
            fmt_diff.append((nu, z, got, want))
print("  40 points, worst relative %.3g, pass(1e-12) %s; %%.11e-string mismatches: %s"
      % (worst, worst < 1e-12, fmt_diff))

print("item 2")
w2 = 0.0
for nu in (2.5, 3.0, 7.0):
    for z in (0.5, 1.0, 2.0, 3.0, 5.0):
        s = t_cdf(z, nu) + t_cdf(-z, nu)
        w2 = max(w2, abs(s - 1.0))
print("  15 pairs, worst |sum - 1| %.3g, pass %s" % (w2, w2 < 1e-12))

print("item 3")
try:
    gaps = []
    for z in range(-3, 4):
        gaps.append((z, rel(t_cdf(float(z), 1e6), pfair.phi(float(z)))))
    print("  gaps", ["%d: %.3g" % g for g in gaps], "worst %.3g" % max(g for _z, g in gaps))
except ArithmeticError as exc:
    print("  RAISED:", exc)
print("  max CF iterations so far", ITER["max"], "raised", ITER["raised"])

print("item 4")
for nu in (2.05, 3.0, 60.0):
    try:
        up = [log_t_cdf(-60 + 0.001 * i, nu) for i in range(65001)]
        bad = sum(1 for a, b in zip(up, up[1:]) if not a < b)
        pts = [-200 + 0.01 * i for i in range(40001)]
        nonfin = sum(1 for z in pts if not math.isfinite(log_t_cdf(z, nu)))
        print("  nu %g: not increasing %d of 65000 steps, not finite %d of 40001" % (nu, bad, nonfin))
    except ArithmeticError as exc:
        print("  nu %g RAISED: %s" % (nu, exc))
print("  max CF iterations so far", ITER["max"], "raised", len(ITER["raised"]))

print("item 5")
K, SIGMA, TAU = D("100000.25"), D("3.25"), 30
for scale in (D("1"), D("1.2"), D("1.38581")):
    h = D(TAU) ** 3 / D(10800)
    sd = scale * SIGMA * h.sqrt()
    # near branch: state = ((60-tau) m_r + tau S_t)/60 - K ; take m_r = S_t so state = S_t - K
    s_t = K + D("-10.819") * sd
    state, _ = pfair.state_and_sd(TAU, s_t, K, SIGMA, s_t)
    z = float(state / sd)
    print("  LINK_SCALE %s: z %r, phi %r, F_3 %.10e (want 8.4465826393e-04), log %.15g" % (
        scale, z, pfair.phi(z), t_cdf(z, 3.0), log_t_cdf(z, 3.0)))
for nu in (2.2, 2.5, 3.5, 4.0):
    print("  if LINK_NU[30] were %g: F(-10.819) = %.10e, log %.15g" % (
        nu, t_cdf(-10.819, nu), log_t_cdf(-10.819, nu)))

# ---- item 5 as section 5.1 defines the functions it names ---------------------------------
# p_fair_student(state, sd, tau) = t_cdf(float(state / sd), float(LINK_NU[tau])) and
# student_sd(tau, sigma) = LINK_SCALE[tau] * sigma * H(tau).sqrt(), H as corrected_sd has it.
# LINK_NU[30] is section 3.2's fitted value, frozen at six significant digits and asserted by V8
# equal to the measurement. It is not measured here: the table is filled with candidate literals
# only to show what item 5's comparison does under each.
print("item 5, through section 5.1's own p_fair_student")


def student_sd(tau, sigma, table):
    h = D(tau) ** 3 / D(pfair.TAU_CUBED_DIVISOR) if tau < pfair.SETTLEMENT_S else D(tau - 40)
    return table["LINK_SCALE"][tau] * sigma * h.sqrt()


def p_fair_student(state, sd, tau, table):
    return t_cdf(float(state / sd), float(table["LINK_NU"][tau]))


WANT_P, WANT_LOG = 8.4465826393e-04, -7.07657843379202
for nu_literal in ("2.99999", "3.00000", "3.00001", "2.50000", "3.50000"):
    table = {"LINK_NU": {30: D(nu_literal)}, "LINK_SCALE": {30: D("1.00000")}}
    sd = student_sd(TAU, SIGMA, table)
    s_t = K + D("-10.819") * sd
    state, _ = pfair.state_and_sd(TAU, s_t, K, SIGMA, s_t)
    z = float(state / sd)
    p_t = p_fair_student(state, sd, TAU, table)
    print("  LINK_NU[30] = %s: z %r  p_fair %r  p_t %.10e  relative to 8.4465826393e-04 %.3g  "
          "10 significant digits %s  log_t_cdf %.15g  relative to the literal %.3g"
          % (nu_literal, z, pfair.p_fair(state, sd), p_t, rel(p_t, WANT_P),
             "%.9e" % p_t == "%.9e" % WANT_P, log_t_cdf(z, float(table["LINK_NU"][30])),
             rel(log_t_cdf(z, float(table["LINK_NU"][30])), WANT_LOG)))
```

---

## 4. Found in the same reading — not the blocker

### 4.1 §5.2's other items pass as specified

These come from the same probe, and are **recorded, not asserted**. None was added to
`selftest-pfair.py`.

| item | result |
|---|---|
| 1 — `log_t_cdf` against the 40 literals, to `1e-12` relative | **40 of 40**. The worst relative difference is `4.01e-15`. All 40 also agree under `%.11e` equality, the reading TZ-10b used |
| 2 — symmetry, `z` in `{0.5, 1, 2, 3, 5}` by `ν` in `{2.5, 3, 7}` | **15 of 15**. The worst `\|F(z) + F(−z) − 1\|` is `0` |
| 3 — the normal limit, `t_cdf(z, 1e6)` against `pfair.phi(z)` over `−3 … 3` | the worst relative gap is `2.46e-05` at `z = −3`, below `1e-4`. §5.2 expected `2.46e-5` |
| 4 — shape | at each `ν` in `{2.05, 3, 60}`, all 65,000 steps over `−60 … 5` are strictly increasing, and all 40,001 points over `−200 … 200` are finite. It passes under either reading of which `ν` the sentence applies to |
| 6 — the three tables | not evaluated: it reads `ADMIT`, `LINK_NU` and `LINK_SCALE`, which do not exist |

The continued fraction converged at every call, within **40** of its 300 iterations, and it
never raised. `LOG_BETA_TOL = 1e-16` is smaller than the gap between `1.0` and either adjacent
double, which is `1.1e-16` below and `2.2e-16` above. So the test `abs(delta − 1) < 1e-16` is met
only when `delta` is exactly `1.0`, and it was met at every call.

### 4.2 Other points in the text that a successor would meet

None of these was needed to reach the stop, and none was resolved. Each is stated with where it
sits.

1. **V6's "insertions only" against §5.3's parameter.**
   - V6 (line 435) requires the diff against the merge base to hold "insertions only for the three
     that already exist", and `research/tz07a-variance-time.py` is one of the three.
   - §5.3 (lines 380–381) makes `log_likelihood` and `lambda_hat` "each gain a keyword parameter
     `log_cdf=None`". The committed definitions are `def log_likelihood(pairs, lam):` (line 270)
     and `def lambda_hat(pairs):` (line 282). Adding a parameter replaces both lines.
   - `lambda_hat` must also pass `log_cdf` on in its two calling lines, 292 and 297. That replaces
     two more lines.
   - Only a run-time substitution, or a second copy of the search, avoids those replacements. §5.3
     (line 392) and map §7 item 43 exclude the first. Contract §6's "one implementation of every
     formula" excludes the second.
   - V6's own exception (lines 438–439) names the two functions for the `ast` comparison only.
2. **§2's outcome rule against V4.**
   - §2 (lines 116–121) says outcomes are read "in exactly two places": inside `tz06.qualification`,
     and inside M4 and M5, "the only places a label enters a number this TZ prints".
   - V4 (lines 426–427) requires `tz07a.lambda_hat` at its default to return `2.0418426092` on the
     TZ-08a 400. `lambda_hat` takes `(z, label)` pairs, so V4 reads all 400 labels and prints a
     number computed from them.
   - V4 is neither M4 nor M5, and §2 does not name it. This is the class of map §7 items 23, 39
     and 44.
3. **V4's "50 members" against its own rule.**
   - V4 (lines 427–430) says "on 50 members — the first 20 of the fit set plus every member whose
     grid M6 drops a second of".
   - `tz07a.excluded_seconds` finds such a second in 15 fit-set members and 16
     test-1 members. One of them, `1789035900`, is among the first 20, so the two committed sets
     give exactly 50.
   - Test 2's first 318 members, formed at 15:45Z by the second probe (§5),
     already hold 15 more.
   - So the count 50 holds only if the rule is read over the fit set and test 1 alone. Over all
     three sets it is at least 65.
4. **G2's pooling.**
   - §4 (line 261) gates all seven `tau`.
   - G2 (line 267) pools "over `tau` as TZ-06 pools it". `tz06.build` sums failing bins over
     `pfair.GATED_TAUS` (lines 479–482), which leaves out `10`.
   - Whether G2 pools six `tau` or seven needs a reading.
5. **M5's population.**
   - §3.5 (lines 249–250) asks for the contribution of `T0 1789268400` to `ll(λ̂)` and to `ll(1)`
     at `tau = 30`, without naming the population.
   - §3.4 fits `λ̂` on the admissible rows (item 3) and on all members (item 5).
   - Whether `1789268400` is admissible at `tau = 30` is not known until `ADMIT` is measured.
6. **V12 for `ν̂`.**
   - V12 (lines 458–461) asks for every `ν̂` "with the same, the influential member named", but
     does not define influence for a profile fit.
   - Exact leave-one-member-out repeats §3.1's nested search once per member removed. That search
     costs about 2,600 likelihood evaluations, each over all of a population's anchors, and §3
     fits 42 populations.
   - That cost is arithmetic on §3.1's bounds and tolerance. It was not measured.

---

## 5. What was not done, and what stayed in scratch

- **V1 … V12.** Only V1's gates and the §0 preflight ran. V7's §5.2 items were evaluated by the
  probe in §3, not as a delivered check. Nothing exists for the other checks to act on.
- **Sets.** Two scratch probes formed set windows by calling the committed
  `tz06-calibration.scoring_set`, unmodified. Its `qualification` opens `resolution.json` for
  every unit considered, as every set formation does. Only counts left the probes, and no label
  entered any number.
  - `probe-count.py` walked test 2 at 13:19Z.
  - `probe-m6.py` walked all three windows at 15:45Z. At that time test 2 held
    318 of its 400 members, so it did not yet exist. The stop does not depend on this.
- **The branch.**
  - `git worktree add /root/tz11-work/wt -b tz-11-student-link main` ran at start-up.
  - `git -C /root/tz11-work/wt status --porcelain` then printed nothing, and `HEAD` was still
    `ecc5a0b`.
  - `git worktree remove /root/tz11-work/wt` and `git branch -d tz-11-student-link` then removed
    both. Neither command was refused.
  - Afterwards `git branch --list 'tz-11*'` and `git ls-remote origin 'refs/heads/tz-11*'` print
    nothing, and `test -e /root/tz11-work/wt` reports it absent.
  - The branch never held a commit of its own and was never pushed.
- **§6 and §9, the retention step.**
  - `/root/tz10b-work/` was not reclaimed, and nothing was copied to `/root/btc-forensics/`. That
    is a step of an executed run, and this run stopped.
  - The files the TZ-10b report names by SHA-256 are intact. Each hash below was recomputed by the
    assembler and **asserted** to appear in that report:

| file | bytes | SHA-256 | named in the TZ-10b report |
|---|---|---|---|
| `/root/tz10b-work/run-1/tz10b-results.json` | 332,640 | `994297738a539d67417911cd32f713f05892e36d443a8139ad4e844d50d1383d` | yes |
| `/root/tz10b-work/run-1/tz10b-tables.md` | 119,347 | `4dc3bfa41dee5dfd89ab2bd3345c28d43e314b9fefa77d4e2f5528d43236d39f` | yes |
| `/root/tz10b-work/run-1/tz10b-observations.csv` | 5,553,429 | `142ea46b765bbdb1796f0da03b198755ac7904aacb748e91419db0a8b423eacd` | yes |
| `/root/tz10b-work/run-2/tz10b-results.json` | 332,640 | `994297738a539d67417911cd32f713f05892e36d443a8139ad4e844d50d1383d` | yes |
| `/root/tz10b-work/run-2/tz10b-tables.md` | 119,347 | `4dc3bfa41dee5dfd89ab2bd3345c28d43e314b9fefa77d4e2f5528d43236d39f` | yes |
| `/root/tz10b-work/run-2/tz10b-observations.csv` | 5,553,429 | `142ea46b765bbdb1796f0da03b198755ac7904aacb748e91419db0a8b423eacd` | yes |
| `/root/tz10b-work/tz10b-observations.csv` | 5,553,429 | `142ea46b765bbdb1796f0da03b198755ac7904aacb748e91419db0a8b423eacd` | yes |

- **`/root/btc-forensics/` and `/root/tz04a-env/`** were not touched. `/root/btc-forensics/` holds
  94 files.
- **Scratch.** `/root/tz11-work/` holds the files below and nothing else. Nothing outside that
  directory and this report was created or modified, except git's own records of the worktree and
  branch in `.git`, which were removed with them. `research/__pycache__/` was untracked before the
  run started, and every probe ran with `python3 -B`. `scipy-ref.out` is a double-precision
  cross-check of item 1's literals, made with `scipy.stats.t.logcdf` in `/root/tz01-env/venv`. No
  number in this report comes from it.

| file | bytes | last written (UTC) | what it is |
|---|---|---|---|
| `preflight-1.txt` | 265 | 2026-09-14T13:18:30Z | §0 preflight read 1 |
| `probe-count.py` | 663 | 2026-09-14T13:18:58Z | first probe: test 2's walk, counts only |
| `scipy-ref.out` | 844 | 2026-09-14T15:40:20Z | a cross-check of item 1's literals; nothing in this report rests on it |
| `preflight-2.txt` | 334 | 2026-09-14T15:45:02Z | §0 preflight read 2 |
| `probe-m6.py` | 1,098 | 2026-09-14T15:45:24Z | second probe: the three walks and M6's members, counts only |
| `probe-m6.out` | 715 | 2026-09-14T15:45:46Z | its output |
| `probe-selftests.py` | 7,024 | 2026-09-14T15:45:48Z | §3's probe |
| `probe-selftests.out` | 2,228 | 2026-09-14T15:45:49Z | its output |
| `gate-check.py` | 2,696 | 2026-09-14T15:45:51Z | §0's fingerprint check |
| `gate-check.out` | 3,499 | 2026-09-14T15:45:51Z | its output |
| `worktree-removed.txt` | 476 | 2026-09-14T15:47:49Z | §0's worktree removal record |
| `report-draft.md` | 37,391 | 2026-09-14T15:55:00Z | this report, assembled |
| `assemble-report.py` | 17,422 | 2026-09-14T15:55:43Z | this assembler |
| `prose.md` | 20,376 | 2026-09-14T15:55:45Z | this report's text before splicing |

- **The timeline.**
  - A usage limit paused the session from shortly after 13:19Z until 15:37Z. The last scratch
    file written before the pause is `probe-count.py`, at 13:18:58Z, and the next is
    `scipy-ref.out`, at 15:40:20Z. The scratch table shows the gap.
  - Nothing ran during the pause.
  - The gates, the fingerprint, preflight read 1 and the first probe came before it. Every other
    probe, preflight read 2 and this report came after it, against the same `main` at `ecc5a0b`.

The second probe, verbatim. It is the source of the counts in §4.2 item 3. Its output is saved as
`probe-m6.out`:

| file | lines | bytes | SHA-256 |
|---|---|---|---|
| `/root/tz11-work/probe-m6.py` | 18 | 1,098 | `78e36b4ee9ba07aee43003bdcdd92b1734b4fefde088d48577361f85fec206d9` |

```python
# TZ-11 probe, scratch only: which members of each set carry a second M6 drops (V4's guard rule).
import os, sys, importlib.util
HERE = "/root/btc-5m-twap/research"
sys.path.insert(0, HERE)
import pfair  # noqa: puts research/recorder on sys.path
from analyze import load_manifests
spec = importlib.util.spec_from_file_location("tz08aoutofsample", os.path.join(HERE, "tz08a-out-of-sample.py"))
tz08a = importlib.util.module_from_spec(spec); spec.loader.exec_module(tz08a)
tz06, tz07a = tz08a.tz06, tz08a.tz07a
m = load_manifests()
out = {}
for name, kw in (("fit", {}), ("test1", {"after": 1789166400}), ("test2-so-far", {"after": 1789296300})):
    rows, full = tz06.scoring_set(m, **kw)
    members = [r["T0"] for r in rows if r["member"]]
    drop = [t0 for t0 in members if tz07a.excluded_seconds(t0, m)]
    out[name] = (len(members), full, len(drop), drop)
    print(name, "members", len(members), "full", full, "M6-dropping", len(drop), drop)
print("guard over fit+test1:", len(set([r["T0"] for r in tz06.scoring_set(m)[0] if r["member"]][:20]) | set(out["fit"][3]) | set(out["test1"][3])))
```

```
fit members 400 full True M6-dropping 15 [1789035900, 1789043100, 1789050300, 1789057500, 1789064700, 1789071900, 1789073100, 1789080300, 1789102500, 1789128300, 1789131600, 1789138800, 1789141800, 1789149000, 1789162500]
test1 members 400 full True M6-dropping 16 [1789169700, 1789170600, 1789177800, 1789185000, 1789197000, 1789200300, 1789206900, 1789214100, 1789221300, 1789252800, 1789260000, 1789267200, 1789274400, 1789278300, 1789285500, 1789292700]
test2-so-far members 318 full False M6-dropping 15 [1789296900, 1789304100, 1789306500, 1789313700, 1789319100, 1789320000, 1789327200, 1789334400, 1789341600, 1789348800, 1789356000, 1789363200, 1789377300, 1789384500, 1789390500]
guard over fit+test1: 50
```
