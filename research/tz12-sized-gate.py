#!/usr/bin/env python3
"""TZ-12: the gate's own error rates.

TZ-11a section 4 closed the Student pricer with four gates that carried thresholds and no error
rates. This file measures, from the frozen pricer's own predictions and without reading any
label, how often each of those gates fails a pricer that is exactly right; it measures the one
table a shape-transfer test needs - the member-bootstrap spread of `log nu_hat` on the fit set,
`SIGMA_LOG_NU` - and it holds the sized gate of TZ-12 section 4, which TZ-13 applies unchanged to
test 3. It scores nothing and judges nothing.

This file is a driver. The sets, the member walk, the checkpoint rows, the Student fit and the
host reads come from `tz11a-student-link.py`, loaded once; `tz10b`, `tz08a`, `tz07b`, `tz07a` and
`tz06` are taken from that module and never loaded a second time. The Student link is
`pfair.log_t_cdf` and `pfair.t_cdf`; the Brier score and the calibration bins are `tz06.brier`,
`tz06.bin_of` and `tz06.calibration`; the scale search the grid is checked against is
`tz07a.lambda_hat` with the Student log CDF.

No label enters any number this file prints. Every checkpoint row keeps `label = None`;
`tz10b.m2_labels` is never called; `tz07a.lambda_hat` is called only on simulated or synthetic
labels, always with `log_cdf` given. The venue's settled documents are read in exactly one place:
inside the committed `tz06.qualification`, which every set formation calls - the resolution,
`resolved_up` and `priceToBeat` reads of 1,314 units, none after `1789427700`. In directories
after `1789427700` only `manifest.json` is opened, by `analyze.load_manifests`. No `quotes.jsonl.gz`
and no `gamma.json` is opened anywhere.

Read-only over the capture. The only files written are the four outputs, into a directory
asserted to lie outside the capture. The only subprocesses are `git`, through `tz10b.git`, each a
fixed argument list with no shell.

Run, from the worktree, on `/root/tz01-env/venv/bin/python`:

      python -B tz12-sized-gate.py --emit          # SIGMA_LOG_NU and its censored set
      python -B tz12-sized-gate.py --out <directory>

`--out` writes `tz12-results.json`, `tz12-tables.md` and `tz12-bootstrap.csv`, none of which
carries a wall-clock time or a path, so two runs compare by `cmp`; and `tz12-host.json`, the
run's own reads of the host and its timings.
"""

import os

# Section 0: every matrix product is computed the same way on every run. These three are the only
# environment writes this file makes, and they come before the first `import numpy`.
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import ast                                                                 # noqa: E402
import collections                                                         # noqa: E402
import hashlib                                                             # noqa: E402
import importlib.util                                                      # noqa: E402
import json                                                                # noqa: E402
import math                                                                # noqa: E402
import statistics                                                          # noqa: E402
import sys                                                                 # noqa: E402
import time                                                                # noqa: E402

import numpy                                                               # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import pfair                                                               # noqa: E402
from pfair import D, config                                                # noqa: E402
from analyze import load_manifests                                         # noqa: E402


def _load(name, filename):
    """Import a module whose filename carries a hyphen, so it cannot be `import`ed by name."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Section 2: TZ-11a's instrument loads TZ-10b's, which loads the other four, so all six come
# through it. A later instrument takes every committed module from this one.
tz11a = _load("tz11astudentlink", "tz11a-student-link.py")
tz10b = tz11a.tz10b
tz08a = tz11a.tz08a
tz07b = tz11a.tz07b
tz07a = tz11a.tz07a
tz06 = tz11a.tz06

# Section 5.1: the constants, named there.
SEED = 20260915
SET_CODES = {"fit": 0, "test1": 1, "test2": 2, "test3": 3}
PURPOSES = {"null": 0, "over": 1, "under": 2, "double": 3, "coin": 4, "bootstrap": 9}
R_NULL = 20000
R_POWER = 2000
ALPHA = {"G1": 0.001, "G2": 0.001, "G3": 0.0025, "G4": 0.0025}
FAMILY_ALPHA = 0.048
COUNT_BOUND = 20
CRIT_RANK = 19950                                                          # 1-based rank of crit3
LAMBDA_K = (500, 3000)
LAMBDA_ONE_COLUMN = 500
LAMBDA_OVER = 1.5
LAMBDA_UNDER = 1.0 / 1.5
LAMBDA_DOUBLE = 2.0
POWER_TO_PASS = 0.5
B_BOOT = 24
BOUND_HITS_ALLOWED = 2
FIT_ADMISSIBLE = 280
Z4 = statistics.NormalDist().inv_cdf(1 - ALPHA["G4"] / 2)
U_BOOT = math.sqrt(23 / 14.8479557992677)

# Section 3.1 M1: the member-bootstrap standard deviation of `log nu_hat` over the fit set's 280
# admissible members, 24 replicates per tau, six significant digits - measured by `--emit` from
# the feed and the manifests alone, and asserted against every run's own measurement (V8).
SIGMA_LOG_NU = {240: D("0.476750"), 180: D("0.338445"), 120: D("0.361253"), 90: D("0.236061"),
                60: D("0.0876792"), 30: D("0.0557673"), 10: D("0.0326229")}
SIGMA_LOG_NU_CENSORED = frozenset({10})

TEST2_SHA256 = "2dd0fcc4dc2cf379e08c21a4524c3eab799aad7bff3136c37e32910cecb8fa70"
# Section 3.0 item 6: TZ-11a report section 1.2, the three "admissible" columns.
ADMISSIBLE_COUNTS = {
    "fit": {240: 280, 180: 280, 120: 280, 90: 280, 60: 280, 30: 280, 10: 280},
    "test1": {240: 35, 180: 29, 120: 28, 90: 28, 60: 28, 30: 28, 10: 30},
    "test2": {240: 231, 180: 237, 120: 233, 90: 234, 60: 233, 30: 235, 10: 235}}
FIRST_FITS_LIMIT_S = 40.0
GUARD_BINS = 100
GUARD_LR = 20
GUARD_LR_TOL = 0.02

# Section 3.1's fail-fast projection, `75 * t + 500` s, against CANON's single-session ceiling.
PROJECTION_SLOPE = 75
PROJECTION_OFFSET_S = 500
SESSION_CEILING_S = 3600

# Section 4, G4's named alternative: tails twice as heavy, `nu` halved, `|d| = log 2`.
ALT_LOG_RATIO = math.log(2.0)

SETS = ("fit", "test1", "test2")
TEST_SETS = ("test1", "test2")
SET_NAMES = tz11a.SET_NAMES
GATES = ("G1", "G2", "G3", "G4")
POWER_PURPOSES = ("over", "under", "double")

# The product of section 3.4 item 4 is formed in consecutive row blocks of this many replicates,
# so that one `L` block is at most 500 x 2,501 doubles.
BLOCK_ROWS = 500

# V12: crit3 from the first 10,000 null replicates, at the same quantile - rank 9,975 of 10,000.
V12_HALF = 10000
V12_RANK = CRIT_RANK * V12_HALF // R_NULL

# Section 5.2: the literals, and the tolerances, as the TZ writes them.
Z4_LITERAL = 3.02334143973915
U_BOOT_LITERAL = 1.24460225924042
CONSTANT_REL_TOL = 1e-12
ITEM3_LR_TOL = 0.02
ITEM3_LAMBDA_TOL = 0.002
POWER_ABS_TOL = 1e-12
STREAM_CHECK_DOUBLES = 1000

# The read set of V9 at the first host read, before the sets exist: every five-minute slot from
# the first unit the fit set considers to the last unit test 2 considers (TZ-11a report section
# 1.0). Step 4 asserts it equal to the units the three formations consider and each member's
# predecessor.
READ_FIRST, READ_LAST = 1789033800, 1789427700

# V2: the committed entry points that read or carry a label, which this file never calls.
LABEL_ENTRY_POINTS = ("m2_labels", "venue", "qualification", "score_member", "score", "table_for",
                      "score_rows", "lambda_with_influence", "m4", "m5", "v4", "fits", "build")
# V6: the two authorized paths, relative to `research/`, and the three environment keys.
TWO_PATHS = ("tz12-sized-gate.py", "../CryptoReports/TZ-12-sized-gate-report.md")
THIS_FILE = "research/tz12-sized-gate.py"
ENV_KEYS = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")

CSV_HEADER = ["tau", "replicate", "draws_sha256", "distinct_members", "anchors", "nu", "s",
              "nu_at_lower_bound", "nu_at_upper_bound", "s_at_lower_bound", "s_at_upper_bound",
              "evaluations", "log_nu"]

# Section 4.1: the Architect's pre-registered prediction, printed beside what is measured.
PREDICTION = (
    ("M1", "each SIGMA_LOG_NU at tau 240, 180 and 120 is larger than each at 90, 60 and 30; "
           "tau = 10 is censored"),
    ("M2, old G3", "on test 2's admissible rows the per-tau false-failure fraction lies in "
                   "0.15 ... 0.40 at tau 240 ... 60 and above 0.40 at 30 and at 10; on test 1's "
                   "it is above 0.60 at every tau"),
    ("M3, G1", "P0 <= 0.001 at every tau on test 2; above 0.001 at tau = 240 on test 1"),
    ("M3, G3", "P3 >= 0.5 at tau 180, 120, 90 and 60 on test 2, and below 0.5 at 240, 30 and "
               "10; below 0.5 at every tau on test 1"),
    ("TZ-13", "no gate FAILs on test 3, and the admitted domain is tau 180, 120, 90 and 60"))


# ---- section 3.4: the arithmetic ------------------------------------------------------------

def lambda_grid():
    """Section 3.4 item 3: `(500 + j) / 1000.0` for `j = 0 ... 2500`, with `lam_500 = 1.0`."""
    grid = [k / 1000.0 for k in range(LAMBDA_K[0], LAMBDA_K[1] + 1)]
    assert len(grid) == 2501 and grid[LAMBDA_ONE_COLUMN] == 1.0, "section 3.4: the grid is wrong"
    assert (grid[0], grid[-1]) == (tz07a.LAMBDA_LO, tz07a.LAMBDA_HI), \
        "section 3.4: the grid does not span the committed search interval"
    return grid


def grid_tables(zs, nu):
    """`(A - B, B.sum(axis=0))` for one population, each table `n x 2501` in float64:
    `A[i, j] = log F_nu(z_i / lam_j)` and `B[i, j] = log F_nu(-z_i / lam_j)`."""
    grid = lambda_grid()
    a = numpy.array([[pfair.log_t_cdf(z / lam, nu) for lam in grid] for z in zs],
                    dtype=numpy.float64)
    b = numpy.array([[pfair.log_t_cdf(-z / lam, nu) for lam in grid] for z in zs],
                    dtype=numpy.float64)
    return a - b, b.sum(axis=0)


def stream(set_code, tau, purpose):
    """Section 3.4 item 1: one fresh generator per set, tau and purpose."""
    return numpy.random.Generator(numpy.random.PCG64(
        numpy.random.SeedSequence([SEED, set_code, tau, purpose])))


def draw(set_code, tau, purpose, q, rows):
    """Section 3.4 items 1 and 2: `rows` replicates, each a row of labels drawn from `q`."""
    rng = stream(set_code, tau, purpose)
    q = numpy.asarray(q, dtype=numpy.float64)
    return (rng.random((rows, q.size)) < q).astype(numpy.float64)


def grid_lr(Y, diff, base):
    """Section 3.4 item 4: `L = Y @ (A - B) + B.sum(axis=0)`, each replicate's log-likelihood at
    every grid value; `LR = 2 (max L - L[:, 500])`, and `lambda_hat` at the first maximum.
    The product is formed in consecutive blocks of `BLOCK_ROWS` replicates."""
    grid = numpy.array(lambda_grid(), dtype=numpy.float64)
    lr = numpy.empty(Y.shape[0], dtype=numpy.float64)
    lam = numpy.empty(Y.shape[0], dtype=numpy.float64)
    for start in range(0, Y.shape[0], BLOCK_ROWS):
        block = Y[start:start + BLOCK_ROWS] @ diff + base
        k = numpy.argmax(block, axis=1)
        top = block[numpy.arange(block.shape[0]), k]
        lr[start:start + block.shape[0]] = 2.0 * (top - block[:, LAMBDA_ONE_COLUMN])
        lam[start:start + block.shape[0]] = grid[k]
    return lr, lam


def bin_counter(ps):
    """Section 3.4 item 6: `tz06.calibration` once on the predictions with every label 0 - its
    bins' `n`, `eligible` and `region` depend on the predictions alone - and `(E, count)`, where
    `count(Y)` gives each replicate's number of eligible bins whose Up count lies outside
    `[lo, hi]`."""
    bins = tz06.calibration([(p, 0) for p in ps])
    index = [tz06.bin_of(p) for p in ps]
    eligible = [(numpy.array([i for i, b in enumerate(index) if b == row["bin"]]),
                 row["region"][0], row["region"][1]) for row in bins if row["eligible"]]

    def count(Y):
        failing = numpy.zeros(Y.shape[0], dtype=numpy.int64)
        for cols, lo, hi in eligible:
            up = Y[:, cols].sum(axis=1)
            failing += (up < lo) | (up > hi)
        return failing
    return len(eligible), count


def k2_of(null_f, eligible):
    """Section 4 G2: the smallest `k`, `1 <= k <= E`, with at most `COUNT_BOUND` null `F` at or
    above it; `None` if there is none."""
    counts = collections.Counter(int(f) for f in null_f)
    for k in range(1, eligible + 1):
        if sum(c for f, c in counts.items() if f >= k) <= COUNT_BOUND:
            return k
    return None


def crit_of(null_lr):
    """Section 4 G3: the `CRIT_RANK`-th smallest null `LR`."""
    return sorted(null_lr)[CRIT_RANK - 1]


def g4_power(c4, s):
    """Section 4 G4's `P4`: `Phi((log 2 - c4) / s) + 1 - Phi((c4 + log 2) / s)`."""
    normal = statistics.NormalDist()
    return normal.cdf((ALT_LOG_RATIO - c4) / s) + 1.0 - normal.cdf((c4 + ALT_LOG_RATIO) / s)


def g4_constants(tau, m):
    """Section 4 G4 at one tau for a population of `m` members: `c4`, `s`, `P4`, the censored
    flag, and whether `LINK_NU[tau] / 2` lies below the search's lower bound."""
    sigma = float(SIGMA_LOG_NU[tau])
    s = sigma * math.sqrt(1 + FIT_ADMISSIBLE / m)
    c4 = Z4 * sigma * U_BOOT * math.sqrt(1 + FIT_ADMISSIBLE / m)
    return {"m": m, "SIGMA_LOG_NU": SIGMA_LOG_NU[tau], "s": s, "c4": c4, "P4": g4_power(c4, s),
            "censored": tau in SIGMA_LOG_NU_CENSORED,
            "half_LINK_NU_below_NU_LO": float(pfair.LINK_NU[tau]) / 2.0 < tz11a.NU_LO}


def brier_scores(ps, Y):
    """Section 3.4 item 5: `tz06.brier` per replicate, labels as `int`."""
    return [tz06.brier(list(zip(ps, Y[r].astype(numpy.int64).tolist())))
            for r in range(Y.shape[0])]


def constants(rows, tau, set_code):
    """Every section 4 constant and every section 3.2 diagnostic for one population, from the
    rows' predictions alone, with section 3.4 item 7's two guards run inside. `rows` are
    checkpoint rows in ascending `T0`; no label is read or attached."""
    n = len(rows)
    assert n > 0, "section 3.4: an empty population"
    t0s = [r["T0"] for r in rows]
    assert t0s == sorted(set(t0s)), "section 3.4: rows are not one per member in T0 order"
    zs = [r["z_student"] for r in rows]
    ps = [r["p_t"] for r in rows]
    nu = float(pfair.LINK_NU[tau])
    diff, base = grid_tables(zs, nu)

    null = draw(set_code, tau, PURPOSES["null"], ps, R_NULL)
    null_lr, null_lam = grid_lr(null, diff, base)
    eligible, count = bin_counter(ps)
    null_f = count(null)
    null_brier = brier_scores(ps, null)

    # Guard 1: the committed calibration on the first 100 null replicates' own pairs.
    for r in range(GUARD_BINS):
        table = tz06.calibration(list(zip(ps, null[r].astype(numpy.int64).tolist())))
        assert sum(1 for b in table if b["eligible"]) == eligible \
            and sum(1 for b in table if b["fails"]) == int(null_f[r]), \
            "section 3.4 item 7: tau %d replicate %d: failing bins differ" % (tau, r)
    # Guard 2: the committed search on the first 20 null replicates.
    log_cdf = tz11a.student_log_cdf(nu)
    d_lr = d_lam = 0.0
    for r in range(GUARD_LR):
        fit = tz07a.lambda_hat(list(zip(zs, null[r].astype(numpy.int64).tolist())), log_cdf)
        gap = abs(fit["likelihood_ratio"] - float(null_lr[r]))
        assert gap <= GUARD_LR_TOL, \
            "section 3.4 item 7: tau %d replicate %d: LR differs by %g" % (tau, r, gap)
        d_lr = max(d_lr, gap)
        d_lam = max(d_lam, abs(fit["lambda_hat"] - float(null_lam[r])))
    del null

    q = {"over": [pfair.t_cdf(z / LAMBDA_OVER, nu) for z in zs],
         "under": [pfair.t_cdf(z / LAMBDA_UNDER, nu) for z in zs],
         "double": [pfair.t_cdf(z / LAMBDA_DOUBLE, nu) for z in zs]}
    crit3 = float(crit_of(null_lr))
    beyond = {}
    for purpose in POWER_PURPOSES:
        lr, _lam = grid_lr(draw(set_code, tau, PURPOSES[purpose], q[purpose], R_POWER), diff, base)
        beyond[purpose] = int(numpy.sum(lr > crit3))
    coin_brier = brier_scores(ps, draw(set_code, tau, PURPOSES["coin"], [0.5] * n, R_POWER))

    at_or_above = sum(1 for b in null_brier if b >= tz11a.G1_BRIER)
    coin_at_or_above = sum(1 for b in coin_brier if b >= tz11a.G1_BRIER)
    k2 = k2_of(null_f, eligible)
    f_counts = collections.Counter(int(f) for f in null_f)
    old_g3 = int(numpy.sum(numpy.abs(null_lam - 1.0) > tz11a.G3_BAND))
    g4 = g4_constants(tau, n)
    doc = {
        "tau": tau, "set_code": set_code, "n": n, "members_sha256": tz07b.member_list_sha(t0s),
        "LINK_NU": pfair.LINK_NU[tau],
        # G1
        "null_brier_at_or_above": at_or_above, "P0": at_or_above / R_NULL,
        "coin_brier_at_or_above": coin_at_or_above, "P1": coin_at_or_above / R_POWER,
        # G2
        "G2_gated": tau in pfair.GATED_TAUS, "E": eligible, "k2": k2,
        "null_f_at_or_above_k2": None if k2 is None else sum(
            c for f, c in f_counts.items() if f >= k2),
        "null_f_distribution": {f: f_counts[f] for f in sorted(f_counts)},
        # G3
        "crit3": crit3, "crit3_first_10000": float(sorted(null_lr[:V12_HALF])[V12_RANK - 1]),
        "over_beyond_crit3": beyond["over"], "P3": beyond["over"] / R_POWER,
        "under_beyond_crit3": beyond["under"], "P_under": beyond["under"] / R_POWER,
        "double_beyond_crit3": beyond["double"], "P_double": beyond["double"] / R_POWER,
        # G4
        "m": g4["m"], "c4": g4["c4"], "s": g4["s"], "P4": g4["P4"],
        "censored": g4["censored"], "half_LINK_NU_below_NU_LO": g4["half_LINK_NU_below_NU_LO"],
        "SIGMA_LOG_NU": g4["SIGMA_LOG_NU"],
        "G1_could_pass": coin_at_or_above / R_POWER >= POWER_TO_PASS,
        "G3_could_pass": beyond["over"] / R_POWER >= POWER_TO_PASS,
        # section 3.2: TZ-11a's gate on the same null replicates
        "old": {"G1_fail_fraction": at_or_above / R_NULL,
                "G2_f_at_or_above_1": sum(c for f, c in f_counts.items() if f >= 1),
                "G2_fraction_at_or_above_1": sum(c for f, c in f_counts.items() if f >= 1) / R_NULL,
                "G3_fail_count": old_g3, "G3_fail_fraction": old_g3 / R_NULL,
                "G3_lambda_hat_at_0_5": int(numpy.sum(null_lam == LAMBDA_K[0] / 1000.0)),
                "G3_lambda_hat_at_0_85": int(numpy.sum(null_lam == 850 / 1000.0)),
                "G3_lambda_hat_at_1_15": int(numpy.sum(null_lam == 1150 / 1000.0)),
                "G4_normal_approximation": 2.0 * (1.0 - statistics.NormalDist().cdf(
                    tz11a.G4_BAND / g4["s"]))},
        "null_lr_median": float(numpy.median(null_lr)),
        "guards": {"bins_compared": GUARD_BINS, "lr_compared": GUARD_LR,
                   "largest_lr_difference": d_lr, "largest_lambda_difference": d_lam}}
    return doc


# ---- section 4: the readings and the verdict -----------------------------------------------

def readings(consts, observed):
    """Section 4's four readings at one tau. `consts` is `constants`' output (or the same keys);
    `observed` holds `brier`, `failing_bins`, `lr`, `log_ratio` and `nu_on_bound`."""
    if observed["brier"] >= tz11a.G1_BRIER:
        g1 = "FAIL" if consts["P0"] <= ALPHA["G1"] else "UNDECIDABLE"
    else:
        g1 = "PASS" if consts["P1"] >= POWER_TO_PASS else "UNDECIDABLE"
    if consts["E"] == 0 or consts["k2"] is None:
        g2 = "UNDECIDABLE"
    elif observed["failing_bins"] >= consts["k2"]:
        g2 = "FAIL"
    else:
        g2 = "NO FAIL"
    if observed["lr"] > consts["crit3"]:
        g3 = "FAIL"
    elif consts["P3"] >= POWER_TO_PASS:
        g3 = "PASS"
    else:
        g3 = "UNDECIDABLE"
    if consts["censored"]:
        g4 = "UNDECIDABLE"
    elif abs(observed["log_ratio"]) > consts["c4"]:
        g4 = "FAIL"
    else:
        g4 = "NO FAIL"
    return {"G1": g1, "G2": g2, "G3": g3, "G4": g4, "G2_gated": consts["G2_gated"],
            "nu_on_bound": observed["nu_on_bound"]}


def verdict(per_tau):
    """Section 4's verdict from the seven tau's readings. G2 at a tau it does not gate is
    printed, never counted."""
    taus = [tau for tau in pfair.TAUS if tau in per_tau]
    failing = [(tau, gate) for tau in taus for gate in GATES
               if per_tau[tau][gate] == "FAIL" and (gate != "G2" or per_tau[tau]["G2_gated"])]
    if failing:
        return {"verdict": "CLOSED", "failing": failing, "admitted": [], "undecided": []}
    admitted = [tau for tau in taus if per_tau[tau]["G1"] == "PASS" and per_tau[tau]["G3"] == "PASS"]
    if not admitted:
        return {"verdict": "UNDECIDED", "failing": [], "admitted": [], "undecided": taus}
    return {"verdict": "NOT DISQUALIFIED", "failing": [], "admitted": admitted,
            "undecided": [tau for tau in taus if tau not in admitted]}


# ---- section 3.1: M1, the member bootstrap on the fit set alone ------------------------------

def bootstrap(walked, fit_admissible):
    """Section 3.1: 24 member-bootstrap refits per tau of the fit set's 280 admissible members,
    the committed `tz11a.fit_student` search unchanged. Returns M1 and, separately, each
    replicate's seconds - which differ from run to run and never enter a compared output."""
    out, seconds = {}, {}
    for tau in pfair.TAUS:
        members = fit_admissible[tau]
        assert len(members) == FIT_ADMISSIBLE, "M1: tau %d has %d admissible fit members" % (
            tau, len(members))
        rng = stream(SET_CODES["fit"], tau, PURPOSES["bootstrap"])
        replicates, seconds[tau] = [], []
        for b in range(B_BOOT):
            idx = rng.integers(0, FIT_ADMISSIBLE, size=FIT_ADMISSIBLE)
            drawn = sorted(members[int(i)] for i in idx)
            started = time.monotonic()
            fit = tz11a.fit_student(tz11a.population(walked, drawn, tau)[0])
            seconds[tau].append(time.monotonic() - started)
            replicates.append({
                "tau": tau, "replicate": b, "draws_sha256": tz07b.member_list_sha(drawn),
                "distinct_members": len(set(drawn)), "anchors": fit["n"], "nu": fit["nu"],
                "s": fit["s"], "nu_at_lower_bound": fit["nu_at_lower_bound"],
                "nu_at_upper_bound": fit["nu_at_upper_bound"],
                "s_at_lower_bound": fit["s_at_lower_bound"],
                "s_at_upper_bound": fit["s_at_upper_bound"], "evaluations": fit["evaluations"],
                "log_nu": math.log(fit["nu"]), "drawn": drawn})
        xs = [r["log_nu"] for r in replicates]
        mean = statistics.fmean(xs)
        m2 = statistics.fmean([(x - mean) ** 2 for x in xs])
        m3 = statistics.fmean([(x - mean) ** 3 for x in xs])
        hits = sum(1 for r in replicates if r["nu_at_lower_bound"] or r["nu_at_upper_bound"])
        leave_one_out = [statistics.stdev(xs[:i] + xs[i + 1:]) for i in range(B_BOOT)]
        out[tau] = {
            "members": len(members), "replicates": replicates,
            "sigma_log_nu": statistics.stdev(xs),
            "sigma_log_nu_6sd": tz07a.six_significant(D(statistics.stdev(xs))),
            "mean_log_nu": mean, "log_LINK_NU": math.log(float(pfair.LINK_NU[tau])),
            "mean_minus_log_LINK_NU": mean - math.log(float(pfair.LINK_NU[tau])),
            "nu_min": min(r["nu"] for r in replicates), "nu_max": max(r["nu"] for r in replicates),
            "skewness_g1": m3 / m2 ** 1.5 if m2 > 0 else None,
            "nu_bound_hits": hits,
            "nu_at_lower_bound": sum(1 for r in replicates if r["nu_at_lower_bound"]),
            "nu_at_upper_bound": sum(1 for r in replicates if r["nu_at_upper_bound"]),
            "s_bound_hits": sum(1 for r in replicates
                                if r["s_at_lower_bound"] or r["s_at_upper_bound"]),
            "censored": hits > BOUND_HITS_ALLOWED,
            "evaluations_min": min(r["evaluations"] for r in replicates),
            "evaluations_max": max(r["evaluations"] for r in replicates),
            "evaluations_total": sum(r["evaluations"] for r in replicates),
            "anchors_min": min(r["anchors"] for r in replicates),
            "anchors_max": max(r["anchors"] for r in replicates),
            "distinct_min": min(r["distinct_members"] for r in replicates),
            "distinct_max": max(r["distinct_members"] for r in replicates),
            "V12_leave_one_out_min": min(leave_one_out),
            "V12_leave_one_out_max": max(leave_one_out)}
    return out, seconds


def m1_literals(m1):
    measured = {tau: m1[tau]["sigma_log_nu"] for tau in pfair.TAUS}
    censored = frozenset(tau for tau in pfair.TAUS if m1[tau]["censored"])
    return measured, censored


# ---- section 5.2: the self-tests ------------------------------------------------------------

def selftests():
    """Six items, each an `assert` that aborts the run; the lines they print are returned."""
    lines = []

    # Item 1: the two constants against the Architect's 40-digit literals.
    rel_z4 = abs(Z4 / Z4_LITERAL - 1.0)
    rel_u = abs(U_BOOT / U_BOOT_LITERAL - 1.0)
    assert rel_z4 <= CONSTANT_REL_TOL and rel_u <= CONSTANT_REL_TOL, "section 5.2 item 1"
    lines.append("item 1: Z4 %r against %r, relative %.3g; U_BOOT %r against %r, relative %.3g"
                 % (Z4, Z4_LITERAL, rel_z4, U_BOOT, U_BOOT_LITERAL, rel_u))

    # Item 2: the rank rules.
    item2 = [crit_of(list(range(19999, -1, -1))),
             k2_of([0] * 19000 + [1] * 900 + [2] * 80 + [3] * 15 + [4] * 5, 4),
             k2_of([0] * 20000, 3), k2_of([0] * 19975 + [1] * 25, 1)]
    assert item2 == [19949, 3, 1, None], "section 5.2 item 2: %s" % item2
    lines.append("item 2: crit_of %s; k2_of %s, %s, %s" % tuple(item2))

    # Item 3: the grid against the committed search, on 201 synthetic pairs.
    nu = float(pfair.LINK_NU[30])
    zs = [-5 + i / 20 for i in range(201)]
    pairs = [(z, int((z > 0) != (i % 7 == 0))) for i, z in enumerate(zs)]
    fit = tz07a.lambda_hat(pairs, tz11a.student_log_cdf(nu))
    diff, base = grid_tables(zs, nu)
    lr, lam = grid_lr(numpy.array([[y for _z, y in pairs]], dtype=numpy.float64), diff, base)
    d_lr = abs(float(lr[0]) - fit["likelihood_ratio"])
    d_lam = abs(float(lam[0]) - fit["lambda_hat"])
    assert d_lr <= ITEM3_LR_TOL and d_lam <= ITEM3_LAMBDA_TOL, \
        "section 5.2 item 3: dLR %g, dlambda %g" % (d_lr, d_lam)
    lines.append("item 3: committed search lambda %.6f LR %.6f; grid lambda %.3f LR %.6f; "
                 "|dLR| %.3g, |dlambda| %.3g" % (fit["lambda_hat"], fit["likelihood_ratio"],
                                                 float(lam[0]), float(lr[0]), d_lr, d_lam))

    # Item 4: the power formula.
    p_a, p_b = g4_power(math.log(2.0), 0.1), g4_power(0.0, 0.1)
    assert abs(p_a - 0.5) <= POWER_ABS_TOL and abs(p_b - 1.0) <= POWER_ABS_TOL, \
        "section 5.2 item 4: %r %r" % (p_a, p_b)
    lines.append("item 4: g4_power(log 2, 0.1) %r; g4_power(0, 0.1) %r" % (p_a, p_b))

    # Item 5: the 19 readings and the 3 verdicts. Each row sets the inputs the TZ names; the
    # filler for every other input cannot change the named gate's reading under section 4.
    base_c = {"P0": 0.0, "P1": 1.0, "E": 3, "k2": 2, "G2_gated": True, "crit3": 9.0, "P3": 1.0,
              "c4": 0.8, "censored": False}
    base_o = {"brier": 0.10, "failing_bins": 0, "lr": 0.0, "log_ratio": 0.0, "nu_on_bound": False}
    cases = (
        ("G1", {"P0": 0.0005}, {"brier": 0.26}, "FAIL"),
        ("G1", {"P0": 0.002}, {"brier": 0.26}, "UNDECIDABLE"),
        ("G1", {"P0": 0.001}, {"brier": 0.2496}, "FAIL"),
        ("G1", {"P1": 0.7}, {"brier": 0.20}, "PASS"),
        ("G1", {"P1": 0.3}, {"brier": 0.20}, "UNDECIDABLE"),
        ("G1", {"P1": 0.5}, {"brier": 0.20}, "PASS"),
        ("G2", {"k2": 2, "E": 3}, {"failing_bins": 2}, "FAIL"),
        ("G2", {"k2": 2, "E": 3}, {"failing_bins": 1}, "NO FAIL"),
        ("G2", {"E": 0, "k2": None}, {"failing_bins": 0}, "UNDECIDABLE"),
        ("G2", {"E": 1, "k2": None}, {}, "UNDECIDABLE"),
        ("G3", {"crit3": 9.0}, {"lr": 10.0}, "FAIL"),
        ("G3", {"crit3": 9.0, "P3": 0.6}, {"lr": 5.0}, "PASS"),
        ("G3", {"crit3": 9.0, "P3": 0.4}, {"lr": 5.0}, "UNDECIDABLE"),
        ("G3", {"crit3": 9.0, "P3": 0.5}, {"lr": 9.0}, "PASS"),
        ("G4", {"c4": 0.8, "censored": False}, {"log_ratio": 1.0}, "FAIL"),
        ("G4", {"c4": 0.8, "censored": True}, {"log_ratio": 1.0}, "UNDECIDABLE"),
        ("G4", {"c4": 0.8, "censored": False}, {"log_ratio": 0.5}, "NO FAIL"),
        ("G4", {"c4": 0.8, "censored": False}, {"log_ratio": 0.8}, "NO FAIL"),
        ("G4", {"c4": 0.8, "censored": False}, {"log_ratio": 1.0, "nu_on_bound": True}, "FAIL"))
    asserted = 0
    for gate, c_in, o_in, want in cases:
        got = readings(dict(base_c, **c_in), dict(base_o, **o_in))[gate]
        assert got == want, "section 5.2 item 5: %s %s %s gives %s" % (gate, c_in, o_in, got)
        asserted += 1
    quiet = {"G1": "UNDECIDABLE", "G2": "NO FAIL", "G3": "UNDECIDABLE", "G4": "NO FAIL",
             "G2_gated": True}
    one_fail = {tau: dict(quiet) for tau in pfair.TAUS}
    one_fail[120] = dict(quiet, G3="FAIL")
    two_pass = {tau: dict(quiet) for tau in pfair.TAUS}
    for tau in (90, 60):
        two_pass[tau] = dict(quiet, G1="PASS", G3="PASS")
    two_pass[180] = dict(quiet, G1="PASS")
    none_pass = {tau: dict(quiet) for tau in pfair.TAUS}
    none_pass[30] = dict(quiet, G3="PASS")
    v_a, v_b, v_c = verdict(one_fail), verdict(two_pass), verdict(none_pass)
    assert v_a["verdict"] == "CLOSED", "section 5.2 item 5: %s" % v_a
    asserted += 1
    assert (v_b["verdict"], set(v_b["admitted"])) == ("NOT DISQUALIFIED", {90, 60}), \
        "section 5.2 item 5: %s" % v_b
    asserted += 1
    assert v_c["verdict"] == "UNDECIDED", "section 5.2 item 5: %s" % v_c
    asserted += 1
    assert asserted == 22, "section 5.2 item 5: %d assertions" % asserted
    lines.append("item 5: %d readings and %d verdicts as fixed: %d assertions; verdicts %s / %s "
                 "on %s / %s" % (len(cases), 3, asserted, v_a["verdict"], v_b["verdict"],
                                 v_b["admitted"], v_c["verdict"]))

    # Item 6: the streams.
    first = stream(2, 60, 0).random(STREAM_CHECK_DOUBLES)
    again = stream(2, 60, 0).random(STREAM_CHECK_DOUBLES)
    other = stream(2, 60, 1).random(1)
    assert numpy.array_equal(first, again) and other[0] != first[0], "section 5.2 item 6"
    lines.append("item 6: SeedSequence([20260915, 2, 60, 0]) twice: first %d doubles identical; "
                 "purpose 1's first double %r differs from purpose 0's %r"
                 % (STREAM_CHECK_DOUBLES, float(other[0]), float(first[0])))
    lines.append("self-tests: 6 of 6 items passed")
    for line in lines:
        sys.stderr.write(line + "\n")
    return {"items": 6, "passed": 6, "item5_assertions": asserted, "lines": lines}


# ---- V2 and V6: this file's own syntax tree -------------------------------------------------

def own_tree():
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        source = fh.read()
    return source, ast.parse(source)


def docstring_nodes(tree):
    """The module docstring and every function docstring, by node identity."""
    out = set()
    for node in [tree] + [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]:
        body = node.body
        if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) \
                and isinstance(body[0].value.value, str):
            out.add(id(body[0].value))
    return out


def v2_static():
    """V2's static half, over this file's own syntax tree.

    The words below may appear in this file only inside a docstring. Any other string constant
    that carries one of them fails the check. They are read from this docstring, one per line
    between the two marker lines:

    forbidden:
    resolution
    resolved_up
    priceToBeat
    quotes.jsonl
    gamma.json
    end
    """
    _source, tree = own_tree()
    node = next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "v2_static")
    doc = ast.get_docstring(node).splitlines()
    words = doc[doc.index("forbidden:") + 1:doc.index("end")]
    assert len(words) == 5, "V2: the forbidden list reads %s" % words
    docs = docstring_nodes(tree)
    constants_scanned, carrying = 0, []
    calls, forbidden_calls, lambda_calls, bad_lambda = 0, [], 0, []
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in docs:
            constants_scanned += 1
            if any(w in n.value for w in words):
                carrying.append(n.lineno)
        elif isinstance(n, ast.Call):
            calls += 1
            if isinstance(n.func, ast.Attribute):
                if n.func.attr in LABEL_ENTRY_POINTS:
                    forbidden_calls.append((n.lineno, n.func.attr))
                if n.func.attr == "lambda_hat":
                    lambda_calls += 1
                    if len(n.args) != 2 or n.keywords or any(
                            isinstance(a, ast.Starred) for a in n.args):
                        bad_lambda.append(n.lineno)
    assert not carrying, "V2: string constants carry a forbidden word at lines %s" % carrying
    assert not forbidden_calls, "V2: label entry points called: %s" % forbidden_calls
    assert lambda_calls and not bad_lambda, "V2: lambda_hat calls at lines %s" % bad_lambda
    return {"forbidden_words": words, "string_constants_scanned": constants_scanned,
            "docstrings_exempt": len(docs), "calls_scanned": calls,
            "label_entry_points": list(LABEL_ENTRY_POINTS), "label_entry_point_calls": 0,
            "lambda_hat_calls": lambda_calls, "lambda_hat_calls_with_two_positional": lambda_calls}


def v6():
    """V6: the diff is one new file, and this file rebinds nothing it imports."""
    base = tz10b.git("merge-base", "HEAD", "main").strip()
    head = tz10b.git("rev-parse", "HEAD").strip()
    status = tz10b.git("status", "--porcelain", "--", *TWO_PATHS)
    assert not status.strip(), "V6: the run is not of committed files: %s" % status
    names = tz10b.git("diff", "--name-only", base, "HEAD").split()
    assert names == [THIS_FILE], "V6: the branch changes %s" % names
    _source, tree = own_tree()
    stores, scopes, env = [], [], []
    for n in ast.walk(tree):
        if isinstance(n, ast.Attribute) and isinstance(n.ctx, (ast.Store, ast.Del)):
            stores.append(n.lineno)
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Name) \
                and n.func.id in ("setattr", "delattr"):
            stores.append(n.lineno)
        elif isinstance(n, (ast.Global, ast.Nonlocal)):
            scopes.append(n.lineno)
        elif isinstance(n, ast.Subscript) and isinstance(n.ctx, (ast.Store, ast.Del)) \
                and isinstance(n.value, ast.Attribute) and n.value.attr == "environ":
            env.append(n.slice.value if isinstance(n.slice, ast.Constant) else None)
    assert not stores, "V6: attribute stores or setattr/delattr at lines %s" % stores
    assert not scopes, "V6: global or nonlocal at lines %s" % scopes
    assert tuple(env) == ENV_KEYS, "V6: os.environ is written at %s" % env
    assert tuple(SIGMA_LOG_NU) == tuple(pfair.TAUS), \
        "V6: SIGMA_LOG_NU carries %s" % list(SIGMA_LOG_NU)
    return {"merge_base": base, "head": head, "status_two_paths": status,
            "diff_names": names, "attribute_stores": stores, "global_or_nonlocal": scopes,
            "environ_writes": list(env), "sigma_keys": list(SIGMA_LOG_NU)}


# ---- V4: the instrument reproduces what is committed, with section 3.1's fail-fast ---------------

def v4_fits(walked, fit, fit_admissible):
    """V4 assertions 1 and 2: `ADMIT` at 7 of 7; `LINK_NU` and `LINK_SCALE` at 14 of 14 from
    seven fits over the fit set's admissible populations, timed together for the fail-fast."""
    measured = tz11a.measure_admit(walked, fit)
    rows = tz11a.check_literals("ADMIT", pfair.ADMIT,
                                {tau: measured[tau]["measured"] for tau in pfair.TAUS})
    fits, seconds = {}, {}
    for tau in pfair.TAUS:
        started = time.monotonic()
        fits[tau] = tz11a.fit_student(tz11a.population(walked, fit_admissible[tau], tau)[0])
        seconds[tau] = time.monotonic() - started
    t = sum(seconds.values())
    if t > FIRST_FITS_LIMIT_S:
        raise SystemExit("BLOCKED at section 3.1: V4's seven fits took %.1f s, above %.0f s; the "
                         "session projects to %.0f s (%d x t + %d) against CANON's %d s" % (
                             t, FIRST_FITS_LIMIT_S, PROJECTION_SLOPE * t + PROJECTION_OFFSET_S,
                             PROJECTION_SLOPE, PROJECTION_OFFSET_S, SESSION_CEILING_S))
    rows += tz11a.check_literals("LINK_NU", pfair.LINK_NU, {tau: fits[tau]["nu"] for tau in pfair.TAUS})
    rows += tz11a.check_literals("LINK_SCALE", pfair.LINK_SCALE,
                                 {tau: fits[tau]["s"] for tau in pfair.TAUS})
    assert len(rows) == 21, "V4: %d literals checked" % len(rows)
    doc = {"literals": rows, "admit_checked": 7, "link_checked": 14,
           "fits": {tau: {k: fits[tau][k] for k in (
               "n", "nu", "s", "nu_at_lower_bound", "nu_at_upper_bound", "s_at_lower_bound",
               "s_at_upper_bound", "evaluations")} for tau in pfair.TAUS}}
    return doc, {"seconds": seconds, "total": t,
                 "projection_s": PROJECTION_SLOPE * t + PROJECTION_OFFSET_S}


def read_range():
    """V9's read set at the first host read: every slot from `READ_FIRST` to `READ_LAST`."""
    return list(range(READ_FIRST, READ_LAST + config.INTERVAL_S, config.INTERVAL_S))


# ---- --emit: the two literals, measured on the fit set alone ------------------------------------

def emit():
    started = time.monotonic()
    host = tz11a.host_read("emit start", read_range(), tz11a.FLOOR_START_BYTES)
    sys.stderr.write("emit start %s, %d bytes free\n" % (host["utc"], host["free_bytes"]))
    manifests = load_manifests()
    _rows, fit = tz11a.fit_set(manifests)
    walked = {t0: tz11a.walk_member(t0, manifests, False) for t0 in fit}
    fit_admissible = tz11a.admissible_members(walked, fit, pfair.ADMIT)
    _doc, timing = v4_fits(walked, fit, fit_admissible)
    sys.stderr.write("V4 seven fits %.1f s; projection %.0f s\n" % (timing["total"],
                                                                 timing["projection_s"]))
    m1, seconds = bootstrap(walked, fit_admissible)
    measured, censored = m1_literals(m1)
    for tau in pfair.TAUS:
        b = m1[tau]
        sys.stderr.write("tau %d: sigma %r, mean log nu %.6f, nu %.4f .. %.4f, bound hits %d, "
                         "%.1f s\n" % (tau, b["sigma_log_nu"], b["mean_log_nu"], b["nu_min"],
                                      b["nu_max"], b["nu_bound_hits"], sum(seconds[tau])))
    sys.stdout.write("SIGMA_LOG_NU = {%s}\n" % ", ".join(
        '%d: D("%s")' % (tau, tz07a.six_significant(D(measured[tau]))) for tau in pfair.TAUS))
    sys.stdout.write("SIGMA_LOG_NU_CENSORED = frozenset({%s})\n" % ", ".join(
        str(tau) for tau in pfair.TAUS if tau in censored))
    sys.stderr.write("emit took %.1f s\n" % (time.monotonic() - started))


# ---- M2's per-set figures and the prediction ---------------------------------------------------

def per_set(m3_set):
    """Section 3.2's per-set figures for one test set: G2's six-tau total by exact convolution of
    the six per-tau null distributions, "under independent per-tau draws", and G3's two figures
    for "some tau fails"."""
    total = {0: 1}
    for tau in pfair.GATED_TAUS:
        dist = m3_set[tau]["null_f_distribution"]
        nxt = collections.Counter()
        for a, ca in total.items():
            for b, cb in dist.items():
                nxt[a + b] += ca * cb
        total = dict(nxt)
    reach = tz06.MAX_FAILING_BINS + 1
    hits = sum(c for k, c in total.items() if k >= reach)
    fractions = {tau: m3_set[tau]["old"]["G3_fail_fraction"] for tau in pfair.TAUS}
    product = 1.0
    for tau in pfair.TAUS:
        product *= 1.0 - fractions[tau]
    return {"G2_total_reaches": reach,
            "G2_probability_independent_per_tau": hits / R_NULL ** len(pfair.GATED_TAUS),
            "G2_eligible_total": sum(m3_set[tau]["E"] for tau in pfair.GATED_TAUS),
            "G3_largest_per_tau": max(fractions.values()),
            "G3_one_minus_product": 1.0 - product}


def prediction(m1, m3):
    """Section 4.1, each row compared with what was measured - recorded, not asserted."""
    sig = {tau: m1[tau]["sigma_log_nu"] for tau in pfair.TAUS}
    t1, t2 = m3["test1"], m3["test2"]
    f = {name: {tau: m3[name][tau]["old"]["G3_fail_fraction"] for tau in pfair.TAUS}
         for name in TEST_SETS}
    rows = [
        ("M1", PREDICTION[0][1],
         "SIGMA_LOG_NU %s; censored %s" % (" / ".join("%d: %.4f" % (t, sig[t]) for t in pfair.TAUS),
                                          sorted(SIGMA_LOG_NU_CENSORED) or "none"),
         min(sig[t] for t in (240, 180, 120)) > max(sig[t] for t in (90, 60, 30))
         and 10 in SIGMA_LOG_NU_CENSORED),
        ("M2, old G3", PREDICTION[1][1],
         "test 2: %s; test 1: %s" % (" / ".join("%.3f" % f["test2"][t] for t in pfair.TAUS),
                                     " / ".join("%.3f" % f["test1"][t] for t in pfair.TAUS)),
         all(0.15 <= f["test2"][t] <= 0.40 for t in (240, 180, 120, 90, 60))
         and all(f["test2"][t] > 0.40 for t in (30, 10))
         and all(f["test1"][t] > 0.60 for t in pfair.TAUS)),
        ("M3, G1", PREDICTION[2][1],
         "P0 on test 2: %s; on test 1 at tau 240: %.5f" % (
             " / ".join("%.5f" % t2[t]["P0"] for t in pfair.TAUS), t1[240]["P0"]),
         all(t2[t]["P0"] <= 0.001 for t in pfair.TAUS) and t1[240]["P0"] > 0.001),
        ("M3, G3", PREDICTION[3][1],
         "P3 on test 2: %s; on test 1: %s" % (" / ".join("%.4f" % t2[t]["P3"] for t in pfair.TAUS),
                                              " / ".join("%.4f" % t1[t]["P3"] for t in pfair.TAUS)),
         all(t2[t]["P3"] >= 0.5 for t in (180, 120, 90, 60))
         and all(t2[t]["P3"] < 0.5 for t in (240, 30, 10))
         and all(t1[t]["P3"] < 0.5 for t in pfair.TAUS)),
        ("TZ-13", PREDICTION[4][1], "not measured here: test 3 is not formed", None)]
    return [{"quantity": q, "predicted": p, "measured": m, "holds": h} for q, p, m, h in rows]


# ---- the run -----------------------------------------------------------------------------------

def disclosure_sha(rows):
    """SHA-256 of one set's unit-by-unit disclosure as `tz11a.the_sets` returns it."""
    return hashlib.sha256(json.dumps(rows, sort_keys=True, default=str).encode("utf-8")).hexdigest()


def build():
    started = time.monotonic()
    timing = {}
    reads = read_range()
    host = [tz11a.host_read("run start", reads, tz11a.FLOOR_START_BYTES)]

    # Everything that stops the run on a defect of the instrument comes before any measurement.
    tests = selftests()
    timing["selftests_seconds"] = time.monotonic() - started
    additive = v6()
    static = v2_static()

    manifests = load_manifests()
    sets, set_doc = tz11a.the_sets(manifests)
    assert set_doc["test2"]["member_list_sha256"] == TEST2_SHA256, \
        "V5: test 2 hashes to %s" % set_doc["test2"]["member_list_sha256"]
    fit, test1, test2 = (sets[name][1] for name in SETS)
    for name in SETS:
        assert sets[name][1] == sorted(sets[name][1]), "section 3.0: %s is not in T0 order" % name
    members = fit + test1 + test2
    formed = sorted({r["T0"] for name in SETS for r in sets[name][0]}
                    | {t0 - config.INTERVAL_S for t0 in members})
    assert formed == reads, "V9: the read set is not the units considered and their predecessors"
    timing["sets_seconds"] = time.monotonic() - started

    walked = {}
    for t0 in members:
        walked[t0] = tz11a.walk_member(t0, manifests, False)
    timing["walk_seconds"] = time.monotonic() - started
    host.append(tz11a.host_read("after the walk", reads, tz11a.FLOOR_BYTES))

    # Section 3.0 items 5 to 7: the rows, never labelled, and the admissible populations.
    set_of = {t0: name for name in SETS for t0 in sets[name][1]}
    checkpoints = {t0: {tau: tz11a.checkpoint_row(t0, set_of[t0], tau, walked[t0][tau])
                        for tau in pfair.TAUS} for t0 in members}
    admissible = {name: tz11a.admissible_members(walked, sets[name][1], pfair.ADMIT)
                  for name in SETS}
    populations, adm_doc, counts_asserted = {}, {}, 0
    for name in SETS:
        adm_doc[name] = {}
        for tau in pfair.TAUS:
            rows = [checkpoints[t0][tau] for t0 in sets[name][1] if checkpoints[t0][tau]["admissible"]]
            assert [r["T0"] for r in rows] == admissible[name][tau], \
                "section 3.0: %s tau %d: the admissible rows are not tz11a's" % (name, tau)
            assert len(rows) == ADMISSIBLE_COUNTS[name][tau], \
                "V4: %s tau %d admits %d, TZ-11a %d" % (name, tau, len(rows),
                                                        ADMISSIBLE_COUNTS[name][tau])
            counts_asserted += 1
            populations[(name, tau)] = rows
            adm_doc[name][tau] = {"count": len(rows),
                                  "sha256": tz07b.member_list_sha([r["T0"] for r in rows])}
    assert counts_asserted == 21, "V4: %d admissible counts" % counts_asserted

    # V4 with the fail-fast, then M1 and V8 - all before M2 starts.
    reproduction, fit_timing = v4_fits(walked, fit, admissible["fit"])
    reproduction["admissible_counts_asserted"] = counts_asserted
    timing["v4_fits"] = fit_timing
    m1, m1_seconds = bootstrap(walked, admissible["fit"])
    timing["m1_seconds"] = m1_seconds
    measured, censored = m1_literals(m1)
    v8 = tz11a.check_literals("SIGMA_LOG_NU", SIGMA_LOG_NU, measured)
    assert SIGMA_LOG_NU_CENSORED == censored, \
        "V8: SIGMA_LOG_NU_CENSORED is %s; this run measures %s" % (
            sorted(SIGMA_LOG_NU_CENSORED), sorted(censored))
    v8_asserted = len(v8) + 1
    assert v8_asserted == 8, "V8: %d assertions" % v8_asserted

    # M2 and M3: the 14 populations, from their predictions alone.
    m3, timing["constants_seconds"] = {}, {}
    for name in TEST_SETS:
        m3[name] = {}
        for tau in pfair.TAUS:
            begun = time.monotonic()
            m3[name][tau] = constants(populations[(name, tau)], tau, SET_CODES[name])
            timing["constants_seconds"]["%s-%d" % (name, tau)] = time.monotonic() - begun
    m2 = {name: per_set(m3[name]) for name in TEST_SETS}

    # V2's run-time half: no row was ever labelled.
    unlabeled = sum(1 for t0 in members for tau in pfair.TAUS if checkpoints[t0][tau]["label"] is None)
    assert unlabeled == len(members) * len(pfair.TAUS) == 8400, \
        "V2: %d of %d rows carry no label" % (unlabeled, len(members) * len(pfair.TAUS))

    host.append(tz11a.host_read("run end", reads, tz11a.FLOOR_BYTES))
    start, end = host[0], host[-1]
    assert end["recorder_pids"] == start["recorder_pids"], "V9: the recorder pid changed"
    assert end["newest_start_sha"] == start["newest_start_sha"] \
        and end["newest_start_recv_ns"] == start["newest_start_recv_ns"], \
        "V9: the recorder restarted during the run"
    assert end["interval_directories"] >= start["interval_directories"], \
        "V9: the interval count fell"
    assert end["read_set_sha256"] == start["read_set_sha256"], \
        "V9: a file this run reads changed during the run"
    timing["total_seconds"] = time.monotonic() - started

    doc = {
        "tz": "TZ-12",
        "sets": set_doc,
        "disclosure_sha256": {name: disclosure_sha(sets[name][0]) for name in SETS},
        "V5": {"hashes_asserted": 3, "test2_expected": TEST2_SHA256},
        "admissible": adm_doc,
        "constants": {"SEED": SEED, "R_NULL": R_NULL, "R_POWER": R_POWER, "ALPHA": ALPHA,
                      "FAMILY_ALPHA": FAMILY_ALPHA, "COUNT_BOUND": COUNT_BOUND,
                      "CRIT_RANK": CRIT_RANK, "Z4": Z4, "U_BOOT": U_BOOT,
                      "FIT_ADMISSIBLE": FIT_ADMISSIBLE, "G1_BRIER": tz11a.G1_BRIER,
                      "G3_BAND": tz11a.G3_BAND, "G4_BAND": tz11a.G4_BAND,
                      "SIGMA_LOG_NU": {tau: SIGMA_LOG_NU[tau] for tau in pfair.TAUS},
                      "SIGMA_LOG_NU_CENSORED": sorted(SIGMA_LOG_NU_CENSORED),
                      "LINK_NU": {tau: pfair.LINK_NU[tau] for tau in pfair.TAUS},
                      "ADMIT": {tau: pfair.ADMIT[tau] for tau in pfair.TAUS}},
        "selftests": tests, "V2": {"static": static, "rows": len(members) * len(pfair.TAUS),
                                   "rows_with_label_none": unlabeled},
        "V4": reproduction, "M1": m1, "V8": {"rows": v8, "censored_measured": sorted(censored),
                                             "asserted": v8_asserted},
        "M3": m3, "M2": m2, "prediction": prediction(m1, m3), "V6": additive}
    csv = csv_text(m1)
    return doc, csv, {"reads": host, "read_set_directories": len(reads), "timing": timing}


def csv_text(m1):
    lines = [",".join(CSV_HEADER)]
    for tau in pfair.TAUS:
        for r in m1[tau]["replicates"]:
            lines.append(",".join(tz11a.cell(r[key]) for key in CSV_HEADER))
    return "\n".join(lines) + "\n"


# ---- output --------------------------------------------------------------------------------------

def frac(count, total):
    return "%.4f (%d of %s)" % (count / total, count, format(total, ","))


def tables(doc):
    out = ["## Sets", ""]
    for name in SETS:
        d = doc["sets"][name]
        out.append("- %s: %d units considered (%d … %d), %d members (%d … %d), %d non-members "
                   "(%s); member list `%s`; disclosure rows SHA-256 `%s`" % (
                       SET_NAMES[name], d["units_considered"], d["first_unit"], d["last_unit"],
                       d["members"], d["first_member"], d["last_member"], d["non_members"],
                       ", ".join("%s: %d" % kv for kv in d["non_member_reasons"].items()) or "none",
                       d["member_list_sha256"], doc["disclosure_sha256"][name]))

    out += ["", "## Admissible rows", "",
            "| set | tau | admissible members | TZ-11a §1.2 | `tz07b.member_list_sha` of the admissible `T0` list |",
            "|---|---|---|---|---|"]
    for name in SETS:
        for tau in pfair.TAUS:
            a = doc["admissible"][name][tau]
            out.append("| %s | %d | %d | %d | `%s` |" % (name, tau, a["count"],
                                                       ADMISSIBLE_COUNTS[name][tau], a["sha256"]))

    out += ["", "## Self-tests", "", "```"] + doc["selftests"]["lines"] + ["```"]

    v4 = doc["V4"]
    out += ["", "## V4", "", "| table | tau | measured | six significant digits | literal | equal |",
            "|---|---|---|---|---|---|"]
    for row in v4["literals"]:
        out.append("| `%s` | %d | %r | %s | %s | %s |" % (row["table"], row["tau"],
                                                         float(row["measured"]),
                                                         row["measured_6sd"], row["in_pfair"],
                                                         "yes" if row["equal"] else "no"))
    out += ["", "| tau | anchors | `ν̂` | `ŝ` | search edge | evaluations |", "|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        f = v4["fits"][tau]
        out.append("| %d | %d | %.6f | %.6f | %s | %d |" % (tau, f["n"], f["nu"], f["s"],
                                                            tz11a.bound_note(f), f["evaluations"]))

    m1 = doc["M1"]
    out += ["", "## M1 — the member bootstrap", "",
            "| tau | `SIGMA_LOG_NU`, measured | six significant digits | mean of `x_b` | "
            "`log LINK_NU` | difference | smallest `ν̂*` | largest `ν̂*` | skewness `g1` | "
            "`ν̂*` on a bound (lower, upper) | `ŝ*` on a bound | censored | distinct members | "
            "anchors | evaluations (min … max, total) |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        b = m1[tau]
        out.append("| %d | %.9f | %s | %.6f | %.6f | %+.6f | %.4f | %.4f | %s | %d (%d, %d) | %d | "
                   "%s | %d … %d | %d … %d | %d … %d, %d |" % (
                       tau, b["sigma_log_nu"], b["sigma_log_nu_6sd"], b["mean_log_nu"],
                       b["log_LINK_NU"], b["mean_minus_log_LINK_NU"], b["nu_min"], b["nu_max"],
                       "—" if b["skewness_g1"] is None else "%+.4f" % b["skewness_g1"],
                       b["nu_bound_hits"], b["nu_at_lower_bound"], b["nu_at_upper_bound"],
                       b["s_bound_hits"], "yes" if b["censored"] else "no", b["distinct_min"],
                       b["distinct_max"], b["anchors_min"], b["anchors_max"],
                       b["evaluations_min"], b["evaluations_max"], b["evaluations_total"]))

    out += ["", "## V8", "", "| table | tau | measured | six significant digits | literal | equal |",
            "|---|---|---|---|---|---|"]
    for row in doc["V8"]["rows"]:
        out.append("| `SIGMA_LOG_NU` | %d | %r | %s | %s | %s |" % (
            row["tau"], float(row["measured"]), row["measured_6sd"], row["in_pfair"],
            "yes" if row["equal"] else "no"))
    out += ["", "`SIGMA_LOG_NU_CENSORED` = %s; this run's censored set = %s. %d assertions." % (
        doc["constants"]["SIGMA_LOG_NU_CENSORED"], doc["V8"]["censored_measured"],
        doc["V8"]["asserted"])]

    out += ["", "## M2 — TZ-11a's gate, sized after the fact", ""]
    for name in TEST_SETS:
        out += ["### %s, admissible rows" % SET_NAMES[name], "",
                "| tau | n | old G1: null Brier `>= 0.2496` | old G2: null `F >= 1` | null `F` "
                "distribution | old G3: null `\\|λ̂_grid − 1\\| > 0.15` | null `λ̂_grid` at 0.5 | "
                "old G4, normal approximation |", "|---|---|---|---|---|---|---|---|"]
        for tau in pfair.TAUS:
            c = doc["M3"][name][tau]
            o = c["old"]
            out.append("| %d | %d | %s | %s | %s | %s | %s | %.4f |" % (
                tau, c["n"], frac(c["null_brier_at_or_above"], R_NULL),
                frac(o["G2_f_at_or_above_1"], R_NULL) + ("" if c["G2_gated"] else ", not gated"),
                ", ".join("%d: %d" % kv for kv in c["null_f_distribution"].items()),
                frac(o["G3_fail_count"], R_NULL), frac(o["G3_lambda_hat_at_0_5"], R_NULL),
                o["G4_normal_approximation"]))
        s = doc["M2"][name]
        out += ["", "Old G2, the six-tau total of failing bins reaching %d, under independent "
                "per-tau draws: **%.6f** (%d eligible bins over the six gated tau). Old G3, some "
                "tau fails: at least **%.4f** (the largest per-tau fraction); **%.4f** as "
                "`1 − Π(1 − fraction)`." % (s["G2_total_reaches"],
                                             s["G2_probability_independent_per_tau"],
                                             s["G2_eligible_total"], s["G3_largest_per_tau"],
                                             s["G3_one_minus_product"]), ""]

    out += ["## M3 — section 4's constants", ""]
    for name in TEST_SETS:
        out += ["### %s, admissible rows" % SET_NAMES[name], "",
                "| tau | m | G1 `P0` | G1 `P1` | G2 `E` | G2 `k2` | null `F >= k2` | G3 `crit3` | "
                "G3 `P3` (λ = 1.5) | `P_under` (λ = 1/1.5) | `P_double` (λ = 2) | G4 `c4` | G4 `s` | "
                "G4 `P4` | `LINK_NU / 2 < 2.05` | censored | G1 could PASS | G3 could PASS |",
                "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for tau in pfair.TAUS:
            c = doc["M3"][name][tau]
            out.append("| %d | %d | %s | %s | %d%s | %s | %s | %.6f | %s | %s | %s | %.6f | %.6f | "
                       "%.4f | %s | %s | %s | %s |" % (
                           tau, c["m"], frac(c["null_brier_at_or_above"], R_NULL),
                           frac(c["coin_brier_at_or_above"], R_POWER), c["E"],
                           "" if c["G2_gated"] else " (printed, not gated)",
                           "—" if c["k2"] is None else c["k2"],
                           "—" if c["null_f_at_or_above_k2"] is None else c["null_f_at_or_above_k2"],
                           c["crit3"], frac(c["over_beyond_crit3"], R_POWER),
                           frac(c["under_beyond_crit3"], R_POWER),
                           frac(c["double_beyond_crit3"], R_POWER), c["c4"], c["s"], c["P4"],
                           "yes" if c["half_LINK_NU_below_NU_LO"] else "no",
                           "yes" if c["censored"] else "no",
                           "yes" if c["G1_could_pass"] else "no",
                           "yes" if c["G3_could_pass"] else "no"))
        out.append("")

    out += ["## V12", "", "| tau | `SIGMA_LOG_NU` | leave one replicate out: smallest | largest |",
            "|---|---|---|---|"]
    for tau in pfair.TAUS:
        b = m1[tau]
        out.append("| %d | %.6f | %.6f | %.6f |" % (tau, b["sigma_log_nu"],
                                                    b["V12_leave_one_out_min"],
                                                    b["V12_leave_one_out_max"]))
    out += ["", "| set | tau | `crit3`, 20,000 null | `crit3`, first 10,000 (rank %d) | null `LR` median |"
            % V12_RANK, "|---|---|---|---|---|"]
    for name in TEST_SETS:
        for tau in pfair.TAUS:
            c = doc["M3"][name][tau]
            out.append("| %s | %d | %.6f | %.6f | %.6f |" % (name, tau, c["crit3"],
                                                            c["crit3_first_10000"],
                                                            c["null_lr_median"]))

    out += ["", "## Guards", "", "| set | tau | bins compared | `LR` compared | largest `\\|ΔLR\\|` | "
            "largest `\\|Δλ̂\\|` | null `λ̂_grid` at 0.85 | at 1.15 |", "|---|---|---|---|---|---|---|---|"]
    for name in TEST_SETS:
        for tau in pfair.TAUS:
            c = doc["M3"][name][tau]
            g = c["guards"]
            out.append("| %s | %d | %d | %d | %.3g | %.3g | %d | %d |" % (
                name, tau, g["bins_compared"], g["lr_compared"], g["largest_lr_difference"],
                g["largest_lambda_difference"], c["old"]["G3_lambda_hat_at_0_85"],
                c["old"]["G3_lambda_hat_at_1_15"]))

    out += ["", "## Prediction", "", "| quantity | predicted | measured | holds |", "|---|---|---|---|"]
    for row in doc["prediction"]:
        out.append("| %s | %s | %s | %s |" % (row["quantity"], row["predicted"], row["measured"],
                                              "—" if row["holds"] is None
                                              else ("yes" if row["holds"] else "no")))

    v2 = doc["V2"]
    s = v2["static"]
    out += ["", "## V2", "", "| count | value |", "|---|---|",
            "| string constants scanned, docstrings exempt | %d (%d docstrings) |" % (
                s["string_constants_scanned"], s["docstrings_exempt"]),
            "| string constants carrying a forbidden word | 0 |",
            "| calls scanned | %d |" % s["calls_scanned"],
            "| calls of a label entry point | %d |" % s["label_entry_point_calls"],
            "| calls of `lambda_hat`, each with exactly two positional arguments | %d of %d |" % (
                s["lambda_hat_calls_with_two_positional"], s["lambda_hat_calls"]),
            "| checkpoint rows with `label is None` after M3 | %d of %d |" % (
                v2["rows_with_label_none"], v2["rows"])]
    v6d = doc["V6"]
    out += ["", "## V6", "", "merge base `%s` · head `%s` · `git status --porcelain` for the two "
            "paths: %s · `git diff --name-only`: %s · attribute stores: %s · `global`/`nonlocal`: %s · "
            "`os.environ` writes: %s · `SIGMA_LOG_NU` keys: %s" % (
                v6d["merge_base"], v6d["head"], "empty" if not v6d["status_two_paths"].strip()
                else v6d["status_two_paths"], ", ".join(v6d["diff_names"]),
                v6d["attribute_stores"] or "none", v6d["global_or_nonlocal"] or "none",
                ", ".join(v6d["environ_writes"]), v6d["sigma_keys"])]
    return "\n".join(out) + "\n"


def main(argv):
    if argv[1:] == ["--emit"]:
        emit()
        return 0
    if argv[1:2] != ["--out"] or len(argv) != 3:
        sys.stderr.write("usage: python -B tz12-sized-gate.py --out <directory> | --emit\n")
        return 2
    target = os.path.realpath(argv[2])
    capture = os.path.realpath(config.ROOT)
    assert os.path.isdir(target), "no directory %s" % target
    assert not (target + os.sep).startswith(capture + os.sep), \
        "V9: %s is inside the capture" % target
    doc, csv, host = build()
    outputs = {"tz12-results.json": json.dumps(doc, sort_keys=True, indent=2, default=str) + "\n",
               "tz12-tables.md": tables(doc),
               "tz12-bootstrap.csv": csv,
               "tz12-host.json": json.dumps(host, sort_keys=True, indent=2, default=str) + "\n"}
    for name, text in outputs.items():
        with open(os.path.join(target, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
