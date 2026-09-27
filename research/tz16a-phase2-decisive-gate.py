#!/usr/bin/env python3
"""TZ-16a — Phase 2's decisive gate, first look.

TZ-16 corrected. On the span map section 2.3 reserves — the first 2,400 qualifying slots with
`T0 > 1789669800` — the instrument takes, at every admissible checkpoint of the five admitted
`tau`, TZ-15's one share of the side whose executable ask `p_t` calls cheap after the taker fee,
and reads each of Phase 2's two answers from its own exact test:

* EDGE where the wins reach beyond the upper tail of a market calibrated at its own ask;
* NO EDGE where they fall below the lower tail of the pricer's own law;
* UNDECIDABLE between them.

Both laws are exact Poisson-binomial tails, read at a deviation shrunk by `r`, the square root of
the variance factor `f` of the null's residual `y - a`, measured on TZ-15's labelled set below the
reserve before any label of the span is read. Every constant is on disk, and the scoring commit on
`origin`, before the one label read, and nothing after that read raises on a label.

The same run carries the chain book's interlock on Tier C: every unit the set rule considers is
split by its exposure to the chain book, and Fisher's one-sided exact test reads whether exposed
units fail `quotes_complete` more often than the control.

No probability is computed here: `p_t` is `tz11a.checkpoint_row`'s. The selection, the fee, the
touch, the exact tail and the isolation guard are TZ-15's and TZ-14's, imported and never written
again. A later TZ imports `up`, `low`, `critical_upper`, `critical_lower`, `look_constants`,
`dependence`, `residual_dependence` and `read_look` from this file and writes none of them again.

The order of a run is section 5.1's and `build` asserts it:

     0  the fingerprint gate                       8  eligibility and selection, label-free
     1  host read 1                                9  the constants, on disk; V4 (d)
     2  the self-tests, then item 12's timing     10  the interlock
     3  `v6` and `v2_static`                       11  without `--score`: host read 3, V8, V9
     4  TZ-15's files, V4 (a) and (b), and `f`    12  with `--score`: the push check, the labels
     5  the set, with its clock condition         13  the statistic, the readings, the verdict
     6  the rows; host read 2                     14  the files; host read 3, V8, V9
     7  the quotes
"""

import ast
import collections
import decimal
import hashlib
import importlib.util
import json
import math
import os
import re
import resource
import stat
import subprocess
import sys
import time
from fractions import Fraction

T_START = time.perf_counter()

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)


def _load(name, filename):
    """Import a module whose filename carries a hyphen, so it cannot be `import`ed by name."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Section 5.1: one load and no other. `tz15` loaded `tz14`, which loaded `tz12` and everything
# below it; loading any of them a second time would be two module objects with two copies of
# every table. The load has side effects this TZ names: `tz15` and `tz14` each write the three
# thread-count environment variables and each install an audit hook that cannot be removed —
# `tz14`'s appends to `tz14.CAPTURE_OPENS`, `tz15`'s to `tz15.OPENS`. This instrument reads
# neither list; it installs its own hook below.
tz15 = _load("tz15phase2gate", "tz15-phase2-gate.py")
tz14 = tz15.tz14
tz12 = tz15.tz12
tz11a = tz15.tz11a
tz10b = tz15.tz10b
tz07b = tz15.tz07b
tz06 = tz15.tz06
pfair = tz15.pfair
config = tz15.config
D = tz15.D
load_manifests = tz15.load_manifests

import analyze                                                             # noqa: E402,F401
import manifest                                                            # noqa: E402,F401


# ---- section 0.1 and V1: the gate's expected values, literals of this instrument ------

# A gate never reads its own expected values from the file it checks.
REQUIRED_REVISION = "2026-09-27-a"
REQUIRED_ANCHORS = (("A1", "229a944f2d51"), ("A2", "6c5089330629"),
                    ("A3", "0-complete / 1-student-5tau-not-disqualified / 2-undecidable-5tau"),
                    ("A4", "437b45ea196b"), ("A5", "9fd1c7de0f74"),
                    ("A6", "729f0bcdbee3"))
# The four anchors that are the first 12 hex characters of a committed file's SHA-256.
ANCHOR_FILES = (("A2", "research/twap-divergence.py"),
                ("A4", "BTC-EXECUTOR-INSTRUCTIONS.md"),
                ("A5", "research/recorder/recorder.py"),
                ("A6", "research/pfair.py"))
# `tz15.v1_gates`' anchor pattern, applied to this revision.
ANCHOR_PATTERN = r"\|\s*`(A\d)`[^|]*\|\s*`?([^`|]+?)`?\s*\|"
FROZEN_ROWS = 24
TRACKED_ROWS = 2
REPORTED_ROWS = 1
MAP_PATH = os.path.join(REPO, "SYSTEM-MAP.md")
# V8: the three frozen files this TZ leans on.
V8_PATHS = ("research/pfair.py", "research/tz14-quote-inventory.py",
            "research/tz15-phase2-gate.py")
SELF_PATH = "research/tz16a-phase2-decisive-gate.py"
REPORT_PATH = "CryptoReports/TZ-16a-phase2-decisive-gate-report.md"
BRANCH = "tz-16a-phase2-decisive-gate"
# Step 1: the sha of the commit the capture runs, map section 6's host identity.
START_SHA = "4216c04673ced76b5b2ac60ef57c9abedc46f9b9"

# ---- section 3.0: the partitions and the counts -----------------------------------

ADMITTED = tz15.ADMITTED
NEED = 2400
AFTER = 1789669800
FIRST_UNIT = 1789670100
CHECKPOINTS = NEED * len(ADMITTED)
ADMITTED_READS = CHECKPOINTS * 2
# Section 0.8: `S7_DEADLINE_S` = 3600 s after `T0` in `research/recorder/recorder.py`, plus the
# 300 s of the close that writes the manifest after it.
DEADLINE_S = 3600 + 300

# ---- section 3.1 and section 3.2: TZ-15's two files, and V4 (a) and (b) ----------

TZ15_WORK = "/root/tz15-work"
TZ15_OBS_SHA256 = "a7ac8a495e00e21cd34af6ead7f05e9a2b741231c928bb61d4ec03ec0e610ce6"
TZ15_CON_SHA256 = "e6a93f9371e9fb32404482dac7b542c330399117ba0cf93e466b846e5878dfd3"
# TZ-15's eighteen columns in TZ-15's order, as `tz15.csv_text` writes its header. This file's own
# observations file carries the same eighteen.
OBS_COLUMNS = ("T0", "tau", "sigma_hat", "admissible", "p_t", "ask_up", "bid_up", "ask_dn",
               "bid_dn", "e_up", "e_dn", "selected", "side", "a", "q", "fee", "label", "y")
# V4 (a): `n` from the `selected` column `tz15.tables` printed (TZ-15 report section 4); `sum y`
# and `sum a` from the `S` and `sum a` columns it printed (section 7); `sum q` from TZ-15's own
# `tz15-constants.json` at full precision (TZ-16 report section 3).
TZ15_N = {240: 405, 180: 428, 120: 440, 90: 380, 60: 271}
TZ15_SUM_Y = {240: 210, 180: 211, 120: 190, 90: 164, 60: 99}
TZ15_SUM_A = {240: D("216.2300"), 180: D("212.5000"), 120: D("192.1940"), 90: D("156.7230"),
              60: D("102.5810")}
TZ15_SUM_Q = {240: D("233.579362178548589456"), 180: D("230.1410794878433773409"),
              120: D("208.2308022961688662051"), 90: D("171.86830345826790914045"),
              60: D("114.107227667538293020748")}
# V4 (b): the `s*`, `FP` and `POWER` columns `tz15.tables` printed, TZ-15 report section 5, each
# tolerance half a unit of the last digit printed.
TZ15_ALPHA = D("0.01")
TZ15_S_STAR = {240: 238, 180: 232, 120: 210, 90: 173, 60: 115}
TZ15_FP = {240: D("0.007476034950"), 180: D("0.008749059109"), 120: D("0.007886034792"),
           90: D("0.006740872864"), 60: D("0.008611872633")}
TZ15_POWER = {240: D("0.325740"), 180: D("0.432618"), 120: D("0.430438"), 90: D("0.459935"),
              60: D("0.467276")}
FP_TOL = D("5e-13")
POWER_TOL = D("5e-7")
V4A_COMPARISONS = 35
V4B_COMPARISONS = 15
# Section 3.2: the neighbours the dependence is estimated to.
LAGS = (1, 2, 3)

# ---- section 3.7 and section 4: the error allocation, literals of this TZ ------------

ALPHA1 = D("0.002")
BETA1 = D("0.002")
ALPHA2 = D("0.008")
BETA2 = D("0.008")
LOW_PRICE = D("0.10")
P4_BOUND = D("1.3")

# ---- section 3.10 and section 4.3: the interlock --------------------------------------

CHAINBOOK_ROOT = "/var/lib/btc-chainbook"
CHAINBOOK_RUNTIME = os.path.join(CHAINBOOK_ROOT, "runtime.jsonl")
WINDOW_NAME = "window.json"
# `E` of window `1790184600`, the first the service ran (TZ-18a report section 4).
EXPOSED_FROM = 1790185200
WINDOW_S = 900
EXPOSED_OFFSET = 600
# TZ-18a report section 2.4: the service's start record.
SERVICE_PID = 2699889
SERVICE_START_NS = 1790185190022755903
FIRE_AT = Fraction(1, 100)
POWER_QS = (Fraction(1, 100), Fraction(2, 100), Fraction(5, 100))

# ---- section 6: the two fail-fast bounds, both resource guards on wall-clock time ----

T12_WEIGHTS = 1200
T12_WEIGHT = D("0.37")
RECURSION_UNITS = 275069310
RECURSION_BASIS = 1440000
RECURSION_LIMIT_S = 400.0
ROWS_LIMIT_S = 450.0

# ---- V2: what this instrument's own tree never does, and does once ---------------------

NEVER_CALLED = (("analyze", "venue"), ("tz11a", "fit_student"), ("tz14", "v1_gates"),
                ("tz14", "selftests"), ("tz14", "build"), ("tz14", "main"),
                ("tz15", "v1_gates"), ("tz15", "selftests"), ("tz15", "reading"),
                ("tz15", "build"), ("tz15", "main"))
LABEL_READER = ("tz10b", "m2_labels")
BARRED_IMPORTS = ("urllib", "http", "socket", "ssl", "requests", "websockets")

# ---- V9: everything this instrument can write -----------------------------------------

WORK_ROOT = "/root/tz16a-work"
LEDGER_PATH = os.path.join(WORK_ROOT, "label-ledger.jsonl")
COMPARED = ("tz16a-constants.json", "tz16a-readings.json", "tz16a-tables.md",
            "tz16a-observations.csv", "tz16a-disclosure.md")
RUN_NAME = "tz16a-run.json"
OUT_NAMES = COMPARED + (RUN_NAME,)

# Section 5.1: the steps each kind of run passes through, in order.
SEQUENCES = {"selftest": ("0", "1", "2", "3"),
             "free": ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"),
             "score": ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "12", "13",
                       "14")}

# ---- the audit hook: every open under either capture root ----------------------------

CAPTURE_PREFIXES = (config.ROOT + os.sep, CHAINBOOK_ROOT + os.sep)
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC
OPENS = []
STEP = ["load"]


def _audit(event, args):
    """Record every open under either capture root: its absolute path, its mode and the step."""
    if event != "open" or not args or not isinstance(args[0], str):
        return
    try:
        path = os.path.abspath(args[0])
    except (TypeError, ValueError):
        return
    if not path.startswith(CAPTURE_PREFIXES):
        return
    mode = args[1] if len(args) > 1 and isinstance(args[1], str) else None
    flags = args[2] if len(args) > 2 and isinstance(args[2], int) else None
    OPENS.append((path, mode, flags, STEP[0]))


sys.addaudithook(_audit)


def _is_read(mode, flags):
    """An open that can only read: a mode with `r` and none of `wxa+`, or no write flag."""
    if mode is not None:
        return "r" in mode and not any(c in mode for c in "wxa+")
    return flags is not None and not flags & WRITE_FLAGS


def _step(run, name):
    """Move the run to its next step of section 5.1, asserting that it is the next one."""
    sequence, visited = run["sequence"], run["visited"]
    assert len(visited) < len(sequence), "section 5.1: step %s after the last step" % name
    assert name == sequence[len(visited)], \
        "section 5.1: step %s where step %s comes next" % (name, sequence[len(visited)])
    visited.append(name)
    STEP[0] = name
    run["marks"].append({"step": name, "at_s": round(time.perf_counter() - T_START, 3)})


def _sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def _map_text():
    with open(MAP_PATH, encoding="utf-8") as fh:
        return fh.read()


def _utc(epoch):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(epoch))


def git(*args):
    """The one subprocess call of this file: `git`, a fixed argument list, no shell."""
    done = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True)
    return done.returncode, done.stdout.strip()


# ---- section 0.1 and V1: the fingerprint gate, asserted as step 0 ----------------------

def v1_gates():
    """The revision, the six anchors and every row of map section 0's fingerprint table.

    Neither `tz14.v1_gates` nor `tz15.v1_gates` is called: they assert revisions `2026-09-18-b`
    and `2026-09-19-a`. Only the row reader `tz14.fingerprint_rows` is reused, and every
    expectation here is a literal above.
    """
    text = _map_text()
    assert ("**Revision string:** `%s`" % REQUIRED_REVISION) in text, \
        "section 0.1: the map does not carry revision %s" % REQUIRED_REVISION
    found = re.findall(ANCHOR_PATTERN, text)
    assert len(found) == len(REQUIRED_ANCHORS), \
        "section 0.1: %d anchor rows, not %d" % (len(found), len(REQUIRED_ANCHORS))
    table = dict(found)
    matched = []
    for name, want in REQUIRED_ANCHORS:
        assert table.get(name) == want, \
            "section 0.1: %s reads %r, not %r" % (name, table.get(name), want)
        matched.append(name)
    derived = []
    for name, path in ANCHOR_FILES:
        have = _sha256_file(os.path.join(REPO, path))[:12]
        assert have == dict(REQUIRED_ANCHORS)[name], \
            "section 0.1: %s re-derives to %s from %s" % (name, have, path)
        derived.append({"anchor": name, "path": path, "sha12": have})
    rows, counts = [], {"frozen": 0, "tracked": 0, "reported": 0}
    for row in tz14.fingerprint_rows():
        with open(os.path.join(REPO, row["path"]), "rb") as fh:
            body = fh.read()
        entry = {"path": row["path"], "state": row["state"], "lines": body.count(b"\n"),
                 "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest(),
                 "expected": row["expected"]}
        if row["state"] == "frozen":
            assert entry["sha256"] == row["expected"], \
                "section 0.1: %s hashes to %s, not %s" % (row["path"], entry["sha256"],
                                                          row["expected"])
        counts[row["state"]] += 1
        rows.append(entry)
    assert counts["frozen"] == FROZEN_ROWS, "section 0.1: %d frozen rows" % counts["frozen"]
    assert counts["tracked"] == TRACKED_ROWS, "section 0.1: %d tracked rows" % counts["tracked"]
    assert counts["reported"] == REPORTED_ROWS, \
        "section 0.1: %d reported rows" % counts["reported"]
    return {"revision": REQUIRED_REVISION, "anchors_matched": matched,
            "anchors_derived": derived, "rows": rows, "counts": counts}


def frozen_now():
    return {path: _sha256_file(os.path.join(REPO, path)) for path in V8_PATHS}


def v8(before, after):
    """V8: the three frozen files, equal to map section 0 at run start and, given, at run end."""
    expected = {row["path"]: row["expected"] for row in tz14.fingerprint_rows()
                if row["path"] in V8_PATHS}
    out = {}
    for path in V8_PATHS:
        assert expected.get(path), "V8: the map has no frozen row for %s" % path
        assert before[path] == expected[path], "V8: %s was %s at run start" % (path,
                                                                              before[path])
        if after is not None:
            assert after[path] == expected[path], "V8: %s is %s at run end" % (path,
                                                                              after[path])
        out[path] = {"expected": expected[path], "at_start": before[path],
                     "at_end": None if after is None else after[path]}
    return out


# ---- section 3.7: the two tails under the dependence measured -------------------------

def up(U, mu, r, s):
    """P(count >= s) read at the deviation shrunk by `r`: `U[k]`, `k = floor(mu + (s - mu) / r)`.

    `U` is `tz15.pb_upper` over `n` coins, so `n = len(U) - 1`. It is `1` where `k <= 0` and `0`
    where `k > n`. At `r = 1` the argument is `s` exactly and this is the exact tail.
    """
    n = len(U) - 1
    k = math.floor(mu + (D(s) - mu) / r)
    if k <= 0:
        return D(1)
    if k > n:
        return D(0)
    return U[k]


def low(U, mu, r, s):
    """P(count <= s) read the same way: `1 - U[k + 1]`, `k = ceil(mu + (s - mu) / r)`.

    It is `0` where `k < 0` and `1` where `k >= n`. Both functions round toward the heavier tail.
    """
    n = len(U) - 1
    k = math.ceil(mu + (D(s) - mu) / r)
    if k < 0:
        return D(0)
    if k >= n:
        return D(1)
    return D(1) - U[k + 1]


def critical_upper(U, mu, r, alpha):
    """`c`, the smallest `s` in `0 ... n` with `up <= alpha`, and `FP_E = up` at it.

    `c = n + 1` where none exists, and `FP_E` is then exactly `0`.
    """
    n = len(U) - 1
    for s in range(n + 1):
        tail = up(U, mu, r, s)
        if tail <= alpha:
            return s, tail
    return n + 1, D(0)


def critical_lower(U, mu, r, beta):
    """`d`, the largest `s` in `0 ... n` with `low <= beta`, and `FP_N = low` at it.

    `d = -1` where none exists, and `FP_N` is then exactly `0`.
    """
    n = len(U) - 1
    for s in range(n, -1, -1):
        tail = low(U, mu, r, s)
        if tail <= beta:
            return s, tail
    return -1, D(0)


def look_constants(a, q, r, alpha, beta, tails=None):
    """Section 3.7's six figures over the weights `a` (the null) and `q` (the pricer's law).

    `c` and `FP_E` from the null's upper tail, `d` and `FP_N` from the alternative's lower tail,
    `POWER_E` the alternative's tail at `c` and `POWER_N` the null's at `d`, each `0` at its
    unreachable end. `tails`, where given, is `(tz15.pb_upper(a), tz15.pb_upper(q))` already
    computed, which moves no figure.
    """
    U0, U1 = tails if tails is not None else (tz15.pb_upper(a), tz15.pb_upper(q))
    n = len(a)
    mu0, mu1 = sum(a, D(0)), sum(q, D(0))
    c, fp_e = critical_upper(U0, mu0, r, alpha)
    d, fp_n = critical_lower(U1, mu1, r, beta)
    power_e = up(U1, mu1, r, c) if c <= n else D(0)
    power_n = low(U0, mu0, r, d) if d >= 0 else D(0)
    return {"n": n, "mu0": mu0, "mu1": mu1, "r": r, "alpha": alpha, "beta": beta,
            "c": c, "d": d, "FP_E": fp_e, "FP_N": fp_n, "POWER_E": power_e, "POWER_N": power_n}


def read_look(n, S, c, d):
    """Section 4.1's table in its order: the reading, and whether the claimed size is rejected.

    The flag is true only where `S >= c` and `S <= d` both hold: EDGE is read, and the side also
    won less often than the pricer claimed.
    """
    if n == 0:
        return "UNDECIDABLE", False
    if S >= c:
        return "EDGE", S <= d
    if S <= d:
        return "NO EDGE", False
    return "UNDECIDABLE", False


def _row_of(n, reading):
    """The row of section 4.1's table that gave a reading."""
    if reading == "EDGE":
        return "S >= c"
    if reading == "NO EDGE":
        return "S <= d"
    return "n = 0" if n == 0 else "otherwise"


# ---- section 3.2 and section 3.9: the dependence of the null's residual ---------------

def residual_dependence(x):
    """`rho_1 ... rho_3`, `f_hat = 1 + 2 * sum(rho)`, `f = max(1, f_hat)` and `r = sqrt(f)`.

    All in `Decimal` at the 60 digits `pfair.py` sets on import, over `x` in the order given.
    Total: where `n < 4` the result is undefined with the reason `"n < 4"`, and otherwise where
    the residuals do not vary it is undefined with the reason `"v = 0"`. It raises on neither.
    The exact sums the Architect re-derives from are returned beside: `sum x`, `sum x^2`, and per
    lag `P_k = sum x_i x_(i+k)`, `A_k = sum_(i <= n-k) x_i` and `B_k = sum_(i > k) x_i`.
    """
    x = list(x)
    n = len(x)
    if n < 4:
        return {"defined": False, "why": "n < 4", "n": n}
    mean = sum(x, D(0)) / D(n)
    dev = [xi - mean for xi in x]
    v = sum((e * e for e in dev), D(0))
    if v == 0:
        return {"defined": False, "why": "v = 0", "n": n}
    rho = [sum((dev[i] * dev[i + k] for i in range(n - k)), D(0)) / v for k in LAGS]
    f_hat = D(1) + D(2) * sum(rho, D(0))
    f = max(D(1), f_hat)
    return {"defined": True, "why": None, "n": n, "mean": mean, "v": v, "rho": rho,
            "f_hat": f_hat, "f": f, "r": f.sqrt(),
            "sum_x": sum(x, D(0)), "sum_x2": sum((xi * xi for xi in x), D(0)),
            "P": [sum((x[i] * x[i + k] for i in range(n - k)), D(0)) for k in LAGS],
            "A": [sum(x[:n - k], D(0)) for k in LAGS],
            "B": [sum(x[k:], D(0)) for k in LAGS]}


def _tz15_selected(path):
    """TZ-15's selected rows per `tau` in `ADMITTED`, ascending `T0`, from its observations file."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    header = tuple(lines[0].split(","))
    assert header == OBS_COLUMNS, "section 3.2: the file's columns are %r" % (header,)
    ix = {name: i for i, name in enumerate(header)}
    per_tau = {tau: [] for tau in ADMITTED}
    for line in lines[1:]:
        cells = line.split(",")
        assert len(cells) == len(OBS_COLUMNS), "section 3.2: a row of %d cells" % len(cells)
        tau = int(cells[ix["tau"]])
        if tau in per_tau and cells[ix["selected"]] == "1":
            per_tau[tau].append((int(cells[ix["T0"]]), D(cells[ix["a"]]), D(cells[ix["q"]]),
                                 int(cells[ix["y"]])))
    return {tau: sorted(rows) for tau, rows in per_tau.items()}, len(lines) - 1


def dependence(path):
    """Section 3.2: `residual_dependence` over TZ-15's selected residuals `y - a` at every `tau`.

    `path` is TZ-15's observations file, located by hash. Asserted defined at every `tau`: a
    `tau` with no measured dependence would have no `r`, and the stop is at step 4, before any
    file of the span is opened. Returns, per `tau`, the lists and sums V4 reads beside it.
    """
    selected, data_rows = _tz15_selected(path)
    out = {}
    for tau in ADMITTED:
        rows = selected[tau]
        a = [row[1] for row in rows]
        q = [row[2] for row in rows]
        y = [row[3] for row in rows]
        dep = residual_dependence([D(yi) - ai for ai, yi in zip(a, y)])
        assert dep["defined"], \
            "BLOCKED at section 3.2: tau %d: the dependence is undefined, %s" % (tau, dep["why"])
        out[tau] = {"n": len(rows), "T0": [row[0] for row in rows], "a": a, "q": q, "y": y,
                    "sum_a": sum(a, D(0)), "sum_q": sum(q, D(0)), "sum_y": sum(y),
                    "dependence": dep}
    return out, data_rows


# ---- section 3.1: TZ-15's two files, by hash ------------------------------------------

def locate():
    """Every regular file under TZ-15's work root whose SHA-256 is one of the two named.

    The first of each in sorted path order is read. The constants file is parsed as JSON for
    `n`, `sum_a` and `sum_q` per `tau` in `ADMITTED` and nothing else.
    """
    found = {TZ15_OBS_SHA256: [], TZ15_CON_SHA256: []}
    hashed = 0
    for dirpath, dirnames, filenames in os.walk(TZ15_WORK):
        for name in filenames:
            path = os.path.join(dirpath, name)
            if not stat.S_ISREG(os.lstat(path).st_mode):
                continue
            hashed += 1
            digest = _sha256_file(path)
            if digest in found:
                found[digest].append(path)
    obs, con = sorted(found[TZ15_OBS_SHA256]), sorted(found[TZ15_CON_SHA256])
    if not obs or not con:
        raise SystemExit("BLOCKED at section 3.1: %d copies of the observations file and %d of "
                         "the constants file under %s" % (len(obs), len(con), TZ15_WORK))
    with open(con[0], encoding="utf-8") as fh:
        doc = json.load(fh)
    per_tau = {}
    for tau in ADMITTED:
        entry = doc["per_tau"][str(tau)]
        n, sum_a, sum_q = entry["n"], entry["sum_a"], entry["sum_q"]
        assert isinstance(n, int) and not isinstance(n, bool), "section 3.1: n is %r" % (n,)
        assert isinstance(sum_a, str) and isinstance(sum_q, str), \
            "section 3.1: sum_a or sum_q is not a string at tau %d" % tau
        per_tau[tau] = {"n": n, "sum_a": D(sum_a), "sum_q": D(sum_q),
                        "sum_a_text": sum_a, "sum_q_text": sum_q}
    return {"work_root": TZ15_WORK, "regular_files_hashed": hashed,
            "observations": {"sha256": TZ15_OBS_SHA256, "copies": len(obs), "read": obs[0],
                             "paths": obs},
            "constants": {"sha256": TZ15_CON_SHA256, "copies": len(con), "read": con[0],
                          "paths": con},
            "constants_per_tau": per_tau}


def v4_tz15(located, dep):
    """V4 (a) and (b): TZ-15's two files are the ones it scored, 35 and 15 comparisons."""
    held_a, held_b, rows = 0, 0, {}
    for tau in ADMITTED:
        mine, theirs = dep[tau], located["constants_per_tau"][tau]
        checks = (("n", mine["n"] == TZ15_N[tau]),
                  ("sum y", mine["sum_y"] == TZ15_SUM_Y[tau]),
                  ("sum a", mine["sum_a"] == TZ15_SUM_A[tau]),
                  ("sum q", mine["sum_q"] == TZ15_SUM_Q[tau]),
                  ("n = constants n", mine["n"] == theirs["n"]),
                  ("sum a = constants sum_a", mine["sum_a"] == theirs["sum_a"]),
                  ("sum q = constants sum_q", mine["sum_q"] == theirs["sum_q"]))
        for name, holds in checks:
            assert holds, "BLOCKED at V4 (a): tau %d: %s does not hold" % (tau, name)
            held_a += 1
        s_star, fp, _upper = tz15.crit(mine["a"], TZ15_ALPHA)
        u1 = tz15.pb_upper(mine["q"])
        power = u1[s_star] if s_star <= mine["n"] else D(0)
        assert s_star == TZ15_S_STAR[tau], "BLOCKED at V4 (b): tau %d: s* is %d" % (tau, s_star)
        held_b += 1
        assert abs(fp - TZ15_FP[tau]) <= FP_TOL, "BLOCKED at V4 (b): tau %d: FP is %s" % (tau, fp)
        held_b += 1
        assert abs(power - TZ15_POWER[tau]) <= POWER_TOL, \
            "BLOCKED at V4 (b): tau %d: POWER is %s" % (tau, power)
        held_b += 1
        rows[tau] = {"n": mine["n"], "sum_y": mine["sum_y"], "sum_a": mine["sum_a"],
                     "sum_q": mine["sum_q"], "constants_n": theirs["n"],
                     "constants_sum_a": theirs["sum_a_text"],
                     "constants_sum_q": theirs["sum_q_text"], "s_star": s_star, "FP": fp,
                     "POWER": power, "FP_quoted": TZ15_FP[tau], "POWER_quoted": TZ15_POWER[tau],
                     "FP_gap": abs(fp - TZ15_FP[tau]),
                     "POWER_gap": abs(power - TZ15_POWER[tau])}
    assert held_a == V4A_COMPARISONS, "V4 (a): %d comparisons, not %d" % (held_a,
                                                                         V4A_COMPARISONS)
    assert held_b == V4B_COMPARISONS, "V4 (b): %d comparisons, not %d" % (held_b,
                                                                         V4B_COMPARISONS)
    return {"a_held": held_a, "b_held": held_b, "per_tau": rows}


# ---- section 3.10 and section 4.3: the interlock's pure arithmetic --------------------

def fisher_upper(f_E, m_E, f_C, m_C):
    """`p_I`: P(a hypergeometric draw of `m_E` of `m_E + m_C` units holds at least `f_E` failures).

    Fisher's one-sided exact test, in `Fraction`, from its integer arguments alone.
    """
    assert 0 <= f_E <= m_E and 0 <= f_C <= m_C, "section 3.10: counts %r" % ((f_E, m_E, f_C,
                                                                              m_C),)
    total, failures = m_E + m_C, f_E + f_C
    hits = sum(math.comb(failures, j) * math.comb(total - failures, m_E - j)
               for j in range(f_E, min(m_E, failures) + 1))
    return Fraction(hits, math.comb(total, m_E))


def interlock_reading(f_E, p_I):
    """Section 4.3: FIRE where `f_E >= 1` and `p_I <= 1/100`; otherwise HOLD."""
    return "FIRE" if f_E >= 1 and p_I <= FIRE_AT else "HOLD"


def interlock_power(m_E, m_C, q):
    """`k*`, the smallest `k >= 1` at which `k` exposed failures and none in the control give
    `p_I <= 1/100`, and the exact probability that a binomial count over `m_E` units at `q`
    reaches it. Where no `k` reaches the bound, `k*` is `None` and the power `0`.
    """
    k_star = None
    for k in range(1, m_E + 1):
        if fisher_upper(k, m_E, 0, m_C) <= FIRE_AT:
            k_star = k
            break
    if k_star is None:
        return None, Fraction(0)
    below = sum((math.comb(m_E, j) * q ** j * (1 - q) ** (m_E - j) for j in range(k_star)),
                Fraction(0))
    return k_star, 1 - below


# ---- section 5.2: the self-tests, eleven items, before any interval directory is opened -

SELFTEST_COUNTS = (14, 5, 4, 6, 6, 6, 19, 8, 8, 2, 4)
SELFTEST_TOTAL = 82


def selftests():
    """Eighty-two assertions over eleven items: 14, 5, 4, 6, 6, 6, 19, 8, 8, 2, 4.

    Every expectation is the Architect's, computed in exact rationals by an implementation that
    shares nothing with the code under test, or fixed by construction (TZ section 10 C2). Every
    numeric comparison is between `Fraction` values converted exactly from `Decimal`; a reading
    or a reason is compared as the word the TZ writes, a flag as a boolean.
    """
    counts = [0] * (len(SELFTEST_COUNTS) + 1)
    lines = []

    def ok(item, condition, message):
        assert condition, "section 5.2 item %d: %s" % (item, message)
        counts[item] += 1

    F = Fraction

    # 1. `up` and `low` at r = 1 against the sixteen outcomes of four coins.
    u = tz15.pb_upper([D("0.25"), D("0.5"), D("0.75"), D("0.5")])
    want_up = (F(1), F(1), F(61, 64), F(45, 64), F(19, 64), F(3, 64), F(0))
    want_low = (F(0), F(3, 64), F(19, 64), F(45, 64), F(61, 64), F(1), F(1))
    for i, s in enumerate(range(-1, 6)):
        got = up(u, D("2"), D(1), s)
        ok(1, F(got) == want_up[i], "up at %d is %s" % (s, got))
    for i, s in enumerate(range(-1, 6)):
        got = low(u, D("2"), D(1), s)
        ok(1, F(got) == want_low[i], "low at %d is %s" % (s, got))
    lines.append("item 1: up and low at s = -1 ... 5 over four coins, against the sixteen "
                 "outcomes — %d assertions" % counts[1])

    # 2. `critical_upper` at r = 1 on twenty fair coins, and `tz15.crit` beside it.
    half = [D("0.5")] * 20
    u2 = tz15.pb_upper(half)
    c2, fp2 = critical_upper(u2, D("10"), D(1), D("0.002"))
    ok(2, c2 == 17, "c is %d" % c2)
    ok(2, F(fp2) == F(1351, 1048576), "FP_E is %s" % fp2)
    ok(2, F(up(u2, D("10"), D(1), 16)) == F(1549, 262144), "up at 16 is not 1549/262144")
    s_star, fp_crit, _upper = tz15.crit(half, D("0.002"))
    ok(2, s_star == 17, "tz15.crit gives %d" % s_star)
    ok(2, F(fp_crit) == F(1351, 1048576), "tz15.crit's FP is %s" % fp_crit)
    lines.append("item 2: twenty fair coins give c = %d, FP_E = %s; tz15.crit gives %d and %s "
                 "— %d assertions" % (c2, fp2, s_star, fp_crit, counts[2]))

    # 3. `critical_upper` under dependence: r = sqrt(1.21) = 1.1 moves c from 17 to 18.
    r3 = D("1.21").sqrt()
    ok(3, r3 == D("1.1"), "sqrt(1.21) is %s" % r3)
    c3, fp3 = critical_upper(u2, D("10"), r3, D("0.002"))
    ok(3, c3 == 18, "c is %d" % c3)
    ok(3, F(fp3) == F(1351, 1048576), "FP_E is %s" % fp3)
    ok(3, F(up(u2, D("10"), r3, 17)) == F(1549, 262144), "up at 17 is not 1549/262144")
    lines.append("item 3: at r = %s the same coins give c = %d, FP_E = %s — %d assertions"
                 % (r3, c3, fp3, counts[3]))

    # 4. `critical_lower` against the binomial at 0.8, at r = 1 and r = 1.1; denominator 5^20.
    eight = [D("0.8")] * 20
    u4 = tz15.pb_upper(eight)
    d4, fn4 = critical_lower(u4, D("16"), D(1), D("0.002"))
    ok(4, d4 == 9, "d at r = 1 is %d" % d4)
    ok(4, F(fn4) == F(53731317297, 95367431640625), "FP_N at r = 1 is %s" % fn4)
    ok(4, F(low(u4, D("16"), D(1), 10)) == F(247462024753, 95367431640625),
       "low at 10 is not 247462024753/5^20")
    d4b, fn4b = critical_lower(u4, D("16"), D("1.1"), D("0.002"))
    ok(4, d4b == 8, "d at r = 1.1 is %d" % d4b)
    ok(4, F(fn4b) == F(53731317297, 95367431640625), "FP_N at r = 1.1 is %s" % fn4b)
    ok(4, F(low(u4, D("16"), D("1.1"), 9)) == F(247462024753, 95367431640625),
       "low at 9 under r = 1.1 is not 247462024753/5^20")
    lines.append("item 4: twenty coins at 0.8 give d = %d at r = 1 and d = %d at r = 1.1, FP_N = "
                 "%s both — %d assertions" % (d4, d4b, fn4, counts[4]))

    # 5. The unreachable ends: c = n + 1 and d = -1, each with its false-reading rate exactly 0.
    nine = [D("0.9")] * 3
    u5 = tz15.pb_upper(nine)
    c5, fp5 = critical_upper(u5, D("2.7"), D(1), D("0.002"))
    ok(5, c5 == 4, "c is %d" % c5)
    ok(5, F(fp5) == F(0), "FP_E is %s" % fp5)
    ok(5, F(up(u5, D("2.7"), D(1), 3)) == F(D("0.729")), "up at 3 is not 0.729")
    halves = [D("0.5")] * 3
    u5b = tz15.pb_upper(halves)
    d5, fn5 = critical_lower(u5b, D("1.5"), D(1), D("0.002"))
    ok(5, d5 == -1, "d is %d" % d5)
    ok(5, F(fn5) == F(0), "FP_N is %s" % fn5)
    ok(5, F(low(u5b, D("1.5"), D(1), 0)) == F(D("0.125")), "low at 0 is not 0.125")
    lines.append("item 5: three coins at 0.9 give c = %d, FP_E = %s; three at 0.5 give d = %d, "
                 "FP_N = %s — %d assertions" % (c5, fp5, d5, fn5, counts[5]))

    # 6. `look_constants` at r = 1: fair coins for the null, coins at 0.8 for the alternative.
    lc = look_constants([D("0.5")] * 20, [D("0.8")] * 20, D(1), D("0.002"), D("0.002"))
    ok(6, lc["c"] == 17, "c is %d" % lc["c"])
    ok(6, lc["d"] == 9, "d is %d" % lc["d"])
    ok(6, F(lc["FP_E"]) == F(1351, 1048576), "FP_E is %s" % lc["FP_E"])
    ok(6, F(lc["FP_N"]) == F(53731317297, 95367431640625), "FP_N is %s" % lc["FP_N"])
    ok(6, F(lc["POWER_E"]) == F(39238821216256, 95367431640625),
       "POWER_E is %s" % lc["POWER_E"])
    ok(6, F(lc["POWER_N"]) == F(215955, 524288), "POWER_N is %s" % lc["POWER_N"])
    lines.append("item 6: c = %d, d = %d, POWER_E = %s, POWER_N = %s — %d assertions"
                 % (lc["c"], lc["d"], lc["POWER_E"], lc["POWER_N"], counts[6]))

    # 7. `residual_dependence` against exact rational autocovariances, and its two undefined cases.
    tol = F(D("1e-50"))

    def x_of(a, y):
        return [D(yi) - ai for ai, yi in zip(a, y)]

    cases7 = (("a", [D("0.5")] * 16, [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
               (F(9, 16), F(1, 8), F(-5, 16)), F(7, 4), F(7, 4)),
              ("b", [D("0.5")] * 8, [1, 0, 1, 0, 1, 0, 1, 0],
               (F(-7, 8), F(3, 4), F(-5, 8)), F(-1, 2), F(1)),
              ("c", [D(v) for v in ("0.30", "0.55", "0.62", "0.41", "0.48", "0.70", "0.25",
                                    "0.53")], [1, 1, 0, 0, 1, 1, 0, 1],
               (F(837, 68824), F(-10645, 17206), F(165, 9832)), F(-1544, 8603), F(1)))
    for name, a, y, rhos, f_hat, f in cases7:
        res = residual_dependence(x_of(a, y))
        for k, want in zip(LAGS, rhos):
            got = res["rho"][k - 1] if res["defined"] else None
            ok(7, got is not None and abs(F(got) - want) <= tol, "(%s) rho_%d is %s"
               % (name, k, got))
        got = res["f_hat"] if res["defined"] else None
        ok(7, got is not None and abs(F(got) - f_hat) <= tol, "(%s) f_hat is %s" % (name, got))
        got = res["f"] if res["defined"] else None
        ok(7, got is not None and F(got) == f, "(%s) f is %s" % (name, got))
    res_d = residual_dependence(x_of([D("0.5")] * 3, [1, 0, 1]))
    ok(7, res_d["defined"] is False, "(d) is defined")
    ok(7, res_d["why"] == "n < 4", "(d) reason is %r" % res_d["why"])
    res_e = residual_dependence(x_of([D("0.5")] * 4, [1, 1, 1, 1]))
    ok(7, res_e["defined"] is False, "(e) is defined")
    ok(7, res_e["why"] == "v = 0", "(e) reason is %r" % res_e["why"])
    lines.append("item 7: three residual series against exact rationals and the two undefined "
                 "cases, 'n < 4' and 'v = 0' — %d assertions" % counts[7])

    # 8. `read_look`: six readings in section 4.1's order, and two flags.
    cases8 = ((0, 0, 1, -1, "UNDECIDABLE", None), (10, 8, 8, 2, "EDGE", False),
              (10, 2, 8, 2, "NO EDGE", None), (10, 5, 8, 2, "UNDECIDABLE", None),
              (10, 6, 6, 6, "EDGE", True), (10, 6, 7, 6, "NO EDGE", None))
    for n, S, c, d, want, flag in cases8:
        got, rejected = read_look(n, S, c, d)
        ok(8, got == want, "read_look(%d, %d, %d, %d) is %s" % (n, S, c, d, got))
        if flag is not None:
            ok(8, rejected is flag, "read_look(%d, %d, %d, %d)'s flag is %r" % (n, S, c, d,
                                                                                rejected))
    lines.append("item 8: six readings and two claim-rejected flags — %d assertions" % counts[8])

    # 9. `fisher_upper` and `interlock_reading`, called with literals.
    cases9 = ((3, 10, 0, 20, F(6, 203), "HOLD"), (4, 10, 0, 20, F(2, 261), "FIRE"),
              (2, 10, 1, 20, F(51, 203), "HOLD"), (0, 10, 0, 20, F(1), "HOLD"))
    for f_e, m_e, f_c, m_c, want, reading in cases9:
        p_i = fisher_upper(f_e, m_e, f_c, m_c)
        ok(9, p_i == want, "fisher_upper%r is %s" % ((f_e, m_e, f_c, m_c), p_i))
        got = interlock_reading(f_e, p_i)
        ok(9, got == reading, "interlock_reading(%d, %s) is %s" % (f_e, p_i, got))
    lines.append("item 9: four Fisher tails, 6/203, 2/261, 51/203 and 1, and their readings "
                 "HOLD, FIRE, HOLD, HOLD — %d assertions" % counts[9])

    # 10. `interlock_power` at m_E = 10, m_C = 20.
    k_star, power = interlock_power(10, 20, F(1, 2))
    ok(10, k_star == 4, "k* is %r" % k_star)
    ok(10, power == F(53, 64), "the power at q = 1/2 is %s" % power)
    lines.append("item 10: k* = %d and the power at q = 1/2 is %s — %d assertions"
                 % (k_star, power, counts[10]))

    # 11. The isolation guard, `tz15.label_free`.
    good = [{k: (None if k == "label" else 0) for k in tz15.ROW_KEYS} for _ in range(2)]
    try:
        tz15.label_free(good)
        raised = False
    except AssertionError:
        raised = True
    ok(11, raised is False, "two clean rows raised")
    for name, key, value in (("a label of 1", "label", 1), ("the key Y", "Y", 0.0),
                             ("the key r", "r", 0.0)):
        bad = dict(good[0])
        bad[key] = value
        try:
            tz15.label_free([bad])
            raised = False
        except AssertionError:
            raised = True
        ok(11, raised is True, "%s did not raise" % name)
    lines.append("item 11: the guard passes two clean rows and raises on a label, on Y and on r "
                 "— %d assertions" % counts[11])

    got = tuple(counts[1:])
    assert got == SELFTEST_COUNTS, "section 5.2: the items hold %r assertions" % (got,)
    assert sum(got) == SELFTEST_TOTAL, "section 5.2: %d assertions, not %d" % (sum(got),
                                                                              SELFTEST_TOTAL)

    # Item 12 is a timing, not a test. Section 6's first fail-fast reads it.
    mark = time.perf_counter()
    tz15.pb_upper([T12_WEIGHT] * T12_WEIGHTS)
    t12 = time.perf_counter() - mark
    projected = RECURSION_UNITS * t12 / RECURSION_BASIS
    lines.append("item 12: one recursion over %d weights took %.4f s; the run projects %.1f s of "
                 "recursion against the %.0f s bound" % (T12_WEIGHTS, t12, projected,
                                                        RECURSION_LIMIT_S))
    if projected > RECURSION_LIMIT_S:
        raise SystemExit("BLOCKED at section 6: the recursions project %.1f s, above %.0f s"
                         % (projected, RECURSION_LIMIT_S))
    return {"items": len(SELFTEST_COUNTS), "assertions": sum(got), "per_item": list(got),
            "lines": lines, "t12_s": t12, "projected_recursion_s": projected}


# ---- V2 and V6: this instrument's own syntax tree -------------------------------------

def _source():
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        return fh.read()


def _docstring_nodes(tree):
    """Every string constant that is a docstring, by identity, so V2 can exempt it."""
    out = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            body = node.body
            if body and isinstance(body[0], ast.Expr) \
                    and isinstance(body[0].value, ast.Constant) \
                    and isinstance(body[0].value.value, str):
                out.add(id(body[0].value))
    return out


def _dotted(node):
    """`(module, name)` where a call's function is exactly `module.name`, else None."""
    func = node.func
    if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
        return func.value.id, func.attr
    return None


def v2_static():
    """V2's static half over this file's own tree, at step 3, before the capture is touched."""
    tree = ast.parse(_source())
    exempt = _docstring_nodes(tree)
    strings, carrying = 0, []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) \
                and id(node) not in exempt:
            strings += 1
            if any(bad in node.value for bad in tz14.BANNED_SUBSTRINGS):
                carrying.append(node.value)
    calls, probability, never, label_calls, runs, run_ok = 0, [], [], 0, 0, []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        calls += 1
        pair = _dotted(node)
        if pair and pair[0] == "pfair" and pair[1] in tz15.PFAIR_PROBABILITY:
            probability.append("%s.%s" % pair)
        if pair and pair in NEVER_CALLED:
            never.append("%s.%s" % pair)
        if pair == LABEL_READER:
            label_calls += 1
        if pair == ("subprocess", "run"):
            runs += 1
            first = node.args[0] if node.args else None
            literal = isinstance(first, (ast.List, ast.Tuple)) and bool(first.elts) \
                and isinstance(first.elts[0], ast.Constant) and first.elts[0].value == "git"
            run_ok.append(literal and not any(k.arg == "shell" for k in node.keywords))
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names = [alias.name for alias in node.names]
        elif isinstance(node, ast.ImportFrom):
            names = [node.module or ""]
        else:
            continue
        imports += [name for name in names if name.split(".")[0] in BARRED_IMPORTS]
    assert not carrying, "V2: %d string constants carry a barred name" % len(carrying)
    assert not probability, "V2: %r called" % probability
    assert not never, "V2: %r called" % never
    assert label_calls == 1, "V2: %d call sites of the label reader, not 1" % label_calls
    assert not imports, "V2: %r imported" % imports
    assert runs == 1 and all(run_ok), "V2: %d subprocess.run call sites, %r" % (runs, run_ok)
    return {"strings_scanned": strings, "strings_carrying": len(carrying),
            "calls_scanned": calls, "pfair_probability_calls": len(probability),
            "never_called_calls": len(never), "never_called_names": len(NEVER_CALLED),
            "label_reader_call_sites": label_calls, "barred_imports": len(imports),
            "subprocess_run_call_sites": runs, "subprocess_run_begins_with_git": all(run_ok),
            "docstrings_exempt": len(exempt)}


def v6(mode):
    """V6: the diff, and this file's own tree — no global, nonlocal, attribute or env store."""
    tree = ast.parse(_source())
    attribute_stores, globals_, nonlocals, environ = [], [], [], []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                for sub in ast.walk(target):
                    if isinstance(sub, ast.Attribute) and isinstance(sub.ctx, ast.Store):
                        attribute_stores.append(ast.dump(sub))
                    if isinstance(sub, ast.Subscript) and isinstance(sub.value, ast.Attribute) \
                            and sub.value.attr == "environ":
                        environ.append(ast.dump(sub))
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Attribute) and (
                    (isinstance(func.value, ast.Attribute) and func.value.attr == "environ")
                    or func.attr in ("putenv", "unsetenv")):
                environ.append(ast.dump(func))
        if isinstance(node, ast.Global):
            globals_.append(node.names)
        if isinstance(node, ast.Nonlocal):
            nonlocals.append(node.names)
    assert not attribute_stores, "V6: %d attribute stores" % len(attribute_stores)
    assert not globals_ and not nonlocals, "V6: global or nonlocal"
    assert not environ, "V6: %d environment writes" % len(environ)
    code, head = git("rev-parse", "HEAD")
    assert code == 0, "V6: git rev-parse failed"
    code, base = git("merge-base", "HEAD", "origin/main")
    assert code == 0, "V6: git merge-base failed"
    code, diff = git("diff", "--name-only", base, "HEAD")
    assert code == 0, "V6: git diff failed"
    names = [n for n in diff.splitlines() if n]
    code, porcelain = git("status", "--porcelain", "--", SELF_PATH, REPORT_PATH)
    assert code == 0, "V6: git status failed"
    # Section 5.3: the committed lines this change replaces, read from the merge base. The path
    # does not exist there, so the list is empty.
    code, at_base = git("show", "%s:%s" % (base, SELF_PATH))
    source_lines = set(_source().splitlines())
    replaced = [] if code != 0 else [l for l in at_base.splitlines() if l not in source_lines]
    assert set(names) <= {SELF_PATH}, "V6: the diff names %r" % names
    assert not replaced, "V6: %d replaced lines" % len(replaced)
    if mode == "score":
        assert names == [SELF_PATH], "V6: the scoring commit's diff names %r" % names
        assert porcelain == "", "V6: the scoring tree is not the commit: %r" % porcelain
    return {"head": head, "merge_base": base, "diff_names": names,
            "status_porcelain": porcelain, "replaced_lines": len(replaced),
            "path_at_merge_base": code == 0, "attribute_stores": len(attribute_stores),
            "globals": len(globals_), "nonlocals": len(nonlocals), "environ_writes": len(environ)}


# ---- V2 at run time and V9: from this instrument's own hook ---------------------------

def _banned_opens(step):
    banned = tz14.BANNED_SUBSTRINGS[0]
    return sum(1 for path, _mode, _flags, at in OPENS
               if at == step and banned in os.path.basename(path))


def v2_step(run, step, expected):
    """V2 at run time: the settled document's opens at one step, asserted equal to `expected`."""
    got = _banned_opens(step)
    assert got == expected, "V2: %d settled opens at step %s, not %d" % (got, step, expected)
    run["v2_runtime"][step] = got
    return got


def v9_opens(last_member):
    """V9's hook half: every open reads; nothing past the last member but manifests; chain book."""
    per_base, modes, writes, past, chainbook = collections.Counter(), collections.Counter(), \
        [], [], []
    for path, mode, flags, _step_at in OPENS:
        base = os.path.basename(path)
        per_base[base] += 1
        modes[mode if mode is not None else "flags"] += 1
        if not _is_read(mode, flags):
            writes.append(path)
        if path.startswith(CHAINBOOK_ROOT + os.sep):
            if base not in (WINDOW_NAME, os.path.basename(CHAINBOOK_RUNTIME)):
                chainbook.append(path)
            continue
        parent = os.path.basename(os.path.dirname(path))
        if parent.isdigit() and last_member is not None and int(parent) > last_member \
                and base != "manifest.json":
            past.append(path)
    assert not writes, "V9: %d opens that can write: %r" % (len(writes), writes[:3])
    assert not past, "V9: %d opens past the last member: %r" % (len(past), past[:3])
    assert not chainbook, "V9: %d chain book opens of another file: %r" % (len(chainbook),
                                                                          chainbook[:3])
    return {"opens_total": len(OPENS), "by_basename": dict(sorted(per_base.items())),
            "modes": dict(sorted(modes.items())), "write_opens": len(writes),
            "opens_past_last_member_not_manifest": len(past),
            "chainbook_opens_other": len(chainbook), "last_member": last_member}


def v9_host(host):
    """V9's host half, between host read 1, 2 and 3."""
    first, second, last = host[0], host[1], host[-1]
    assert first["recorder_pids"] == last["recorder_pids"], \
        "V9: the recorder pids moved from %r to %r" % (first["recorder_pids"],
                                                       last["recorder_pids"])
    assert first["newest_start_sha"] == last["newest_start_sha"], "V9: the start record moved"
    assert first["newest_start_recv_ns"] == last["newest_start_recv_ns"], \
        "V9: the start record's recv_ns moved"
    assert last["interval_directories"] >= first["interval_directories"], \
        "V9: the directory count fell from %d to %d" % (first["interval_directories"],
                                                        last["interval_directories"])
    assert second["read_set_sha256"] == last["read_set_sha256"], \
        "V9: the read set moved between reads 2 and 3"
    return {"pids": last["recorder_pids"], "start_sha": last["newest_start_sha"],
            "directories": [h["interval_directories"] for h in host],
            "read_set_sha256": last["read_set_sha256"]}


def host_read(when, t0s, floor):
    """`tz11a.host_read`, with the bound it asserted and the reader named."""
    doc = tz11a.host_read(when, t0s, floor)
    doc["reader"] = "tz11a.host_read"
    doc["bound"] = floor
    doc["asserted"] = True
    return doc


# ---- section 3.3: the set -------------------------------------------------------------

def the_set(manifests):
    """The first 2,400 qualifying slots with `T0 > 1789669800`, by `tz06.scoring_set` unchanged.

    `whole` and the clock condition are BLOCKING, printed before any quote file or market
    document is opened: the recorder writes a manifest only after the outcome poll ends, up to
    3,600 s after `T0`, so a walk formed inside that window could count a slow interval out.
    """
    rows, whole = tz06.scoring_set(manifests, NEED, after=AFTER)
    members = [r["T0"] for r in rows if r["member"]]
    now = time.time()
    clock_ok = bool(members) and now >= members[-1] + DEADLINE_S
    if not whole or not clock_ok:
        raise SystemExit(
            "BLOCKED at section 3.3: whole %s; %d members of %d; %d units considered, first %s, "
            "last %s; clock %.0f against %s"
            % (whole, len(members), NEED, len(rows), rows[0]["T0"] if rows else None,
               rows[-1]["T0"] if rows else None, now,
               (members[-1] + DEADLINE_S) if members else None))
    assert len(members) == NEED, "section 3.3: %d members" % len(members)
    assert rows[0]["T0"] == FIRST_UNIT, "section 3.3: the first unit is %d" % rows[0]["T0"]
    gaps = collections.Counter(b["T0"] - a["T0"] for a, b in zip(rows, rows[1:]))
    assert set(gaps) == {config.INTERVAL_S}, "section 3.3: steps %r" % dict(gaps)
    assert rows[-1]["T0"] == members[-1], "section 3.3: the walk ran past the last member"
    days = collections.Counter(tz14.weekday_of(t0) for t0 in members)
    reasons = collections.Counter(", ".join(r["reasons"]) for r in rows if not r["member"])
    doc = {"considered": len(rows), "members": len(members),
           "sha256": tz07b.member_list_sha(members),
           "first_unit": rows[0]["T0"], "last_unit": rows[-1]["T0"],
           "first_member": members[0], "last_member": members[-1],
           "first_member_utc": _utc(members[0]), "last_member_utc": _utc(members[-1]),
           "weekday_counts": {day: days[day] for day in sorted(days)},
           "weekend_members": sum(1 for t0 in members if tz14.is_weekend(t0)),
           "non_members": [{"T0": r["T0"], "reasons": r["reasons"]}
                           for r in rows if not r["member"]],
           "non_member_reasons": dict(sorted(reasons.items())),
           "clock": int(now), "clock_bound": members[-1] + DEADLINE_S}
    return rows, members, doc


# ---- section 3.4: the pricer at each checkpoint ---------------------------------------

def the_rows(members, manifests):
    """One pricer row per member per admitted `tau`, carrying `tz15.ROW_KEYS` and nothing else.

    An `AssertionError` from `tz11a.walk_member` is BLOCKING, with the member and the message.
    """
    rows = {}
    for t0 in members:
        try:
            walked = tz11a.walk_member(t0, manifests, False)
        except AssertionError as exc:
            raise SystemExit("BLOCKED at section 3.4: member %d: %s" % (t0, exc))
        for tau in ADMITTED:
            full = tz11a.checkpoint_row(t0, "tz16aset", tau, walked[tau])
            rows[(t0, tau)] = {k: full[k] for k in tz15.ROW_KEYS}
    per_tau = {}
    for tau in ADMITTED:
        adm = [t0 for t0 in members if rows[(t0, tau)]["admissible"]]
        per_tau[tau] = {"admissible": len(adm),
                        "weekday": sum(1 for t0 in adm if not tz14.is_weekend(t0)),
                        "weekend": sum(1 for t0 in adm if tz14.is_weekend(t0))}
    return rows, per_tau


# ---- section 3.5: the quotes at each admitted checkpoint ------------------------------

def the_quotes(members, rows):
    """`ask5` and `bid5` of each side's reply at each admitted checkpoint — TZ-15's rule.

    A read that is not `200` or not JSON, whose `book_of` result has `ok` false, whose book lacks
    `min_order_size` or `tick_size`, or whose token is outside the member's mapping, and a member
    whose market document is not usable, is listed with its reason and contributes no touch.
    """
    quotes = {key: {"ask_up": None, "bid_up": None, "ask_dn": None, "bid_dn": None}
              for key in rows}
    present, used, listed = collections.Counter(), collections.Counter(), []
    for t0 in members:
        docs = tz14.documents(t0)
        lines = tz14.quote_lines(config.interval_dir(t0))
        if not docs["usable"]:
            listed.append({"T0": t0, "tau": None, "token_id": None,
                           "why": "market document: %s" % docs["why"]})
        for read in lines["reads"]:
            tau = read["tau"]
            if tau not in ADMITTED:
                continue
            present[tau] += 1
            key = (t0, tau)
            entry = {"T0": t0, "tau": tau, "token_id": read["token_id"]}
            if read["status"] != 200 or not read["body_is_json"]:
                listed.append(dict(entry, why="status %r, JSON %s" % (read["status"],
                                                                      read["body_is_json"])))
                continue
            book = tz14.book_of(read["raw"])
            if not book["ok"]:
                listed.append(dict(entry, why="the reply body is not an object"))
                continue
            if not book["min_order_size_present"] or not book["tick_size_present"]:
                listed.append(dict(entry, why="the reply names no size or no tick"))
                continue
            side = docs["tokens"].get(read["token_id"])
            if side is None:
                listed.append(dict(entry, why="the token is outside the mapping"))
                continue
            touch = tz14.touch_of(book, D(str(book["min_order_size"])),
                                  D(str(book["tick_size"])))
            suffix = "up" if side == tz14.UP else "dn"
            quotes[key]["ask_" + suffix] = touch["ask5"]
            quotes[key]["bid_" + suffix] = touch["bid5"]
            used[tau] += 1
    by_reason = collections.Counter((e["tau"], e["why"]) for e in listed)
    doc = {"present": {tau: present[tau] for tau in ADMITTED},
           "used": {tau: used[tau] for tau in ADMITTED},
           "listed": listed,
           "listed_by_reason": [{"tau": tau, "why": why, "count": n}
                                for (tau, why), n in sorted(by_reason.items(),
                                                            key=lambda kv: (str(kv[0][0]),
                                                                            kv[0][1]))]}
    return quotes, doc


# ---- section 3.6: eligibility, selection and what the pricer claims -------------------

def the_trades(rows, quotes):
    """Per `(T0, tau)`: eligibility, `tz15.select`'s trade, and its fee. Never in the pricer row."""
    trades = {}
    for key, row in sorted(rows.items()):
        q = quotes[key]
        rec = {"T0": key[0], "tau": key[1], "admissible": row["admissible"],
               "ask_up": q["ask_up"], "bid_up": q["bid_up"],
               "ask_dn": q["ask_dn"], "bid_dn": q["bid_dn"],
               "eligible": False, "selected": False, "side": None, "a": None, "q": None,
               "e_up": None, "e_dn": None, "edge": None, "both_positive": False,
               "fee": None, "p": None}
        if row["admissible"]:
            rec["eligible"] = q["ask_up"] is not None or q["ask_dn"] is not None
        if rec["eligible"]:
            p = D(repr(row["p_t"]))
            rec["p"] = p
            rec.update(tz15.select(p, q["ask_up"], q["ask_dn"]))
            if rec["selected"]:
                rec["fee"] = tz14.fee_pp(rec["a"])
        trades[key] = rec
    return trades


def _selected(trades, tau):
    """The selected trades at one `tau`, in ascending `T0`."""
    return [t for (t0, tt), t in sorted(trades.items()) if tt == tau and t["selected"]]


def label_free_report(trades):
    """Section 3.6's report per `tau`, before any label exists."""
    out = {}
    for tau in ADMITTED:
        recs = [t for (t0, tt), t in sorted(trades.items()) if tt == tau]
        adm = [r for r in recs if r["admissible"]]
        elig = [r for r in recs if r["eligible"]]
        sel = [r for r in recs if r["selected"]]
        n = len(sel)
        two_sided = [r for r in elig if r["bid_up"] is not None and r["ask_up"] is not None]
        dev, confident = [], 0
        for r in two_sided:
            mid = (r["bid_up"] + r["ask_up"]) / D(2)
            dev.append(r["p"] - mid)
            if abs(r["p"] - D("0.5")) < abs(mid - D("0.5")):
                confident += 1
        claim = [r["q"] - r["a"] for r in sel]
        after = [r["q"] - r["a"] - r["fee"] for r in sel]
        out[tau] = {
            "admissible": len(adm), "eligible": len(elig), "selected": n,
            "selected_up": sum(1 for r in sel if r["side"] == tz14.UP),
            "selected_down": sum(1 for r in sel if r["side"] == tz14.DOWN),
            "selected_weekday": sum(1 for r in sel if not tz14.is_weekend(r["T0"])),
            "selected_weekend": sum(1 for r in sel if tz14.is_weekend(r["T0"])),
            "both_edges_positive": sum(1 for r in recs if r["both_positive"]),
            "selected_at_or_below_0.10": sum(1 for r in sel if r["a"] <= LOW_PRICE),
            "q_price_paid": tz14.q_summary([r["a"] for r in sel]),
            "q_claimed_edge": tz14.q_summary(claim),
            "mean_claimed_edge": (sum(claim, D(0)) / D(n)) if n else None,
            "mean_after_fee_claim": (sum(after, D(0)) / D(n)) if n else None,
            "two_sided_up_books": len(two_sided),
            "q_p_minus_mid": tz14.q_summary(dev),
            "market_more_confident": confident,
            "market_more_confident_share": (D(confident) / D(len(two_sided)))
            if two_sided else None}
    return out


# ---- section 3.7: the gate's constants, exact, before any label ------------------------

def constants(trades, dep):
    """Per `tau`: the look at `r`, the independence columns, the projection, and V4 (d).

    The coins are the selected trades in ascending `T0`. `U0` and `U1` are computed once per
    `tau` and read at `r` and at `r = 1`; `tz15.crit` computes its own for V4 (d).
    """
    out = {}
    for tau in ADMITTED:
        sel = _selected(trades, tau)
        a = [t["a"] for t in sel]
        q = [t["q"] for t in sel]
        n = len(sel)
        r = dep[tau]["dependence"]["r"]
        tails = (tz15.pb_upper(a), tz15.pb_upper(q))
        look = look_constants(a, q, r, ALPHA1, BETA1, tails)
        indep = look_constants(a, q, D(1), ALPHA1, BETA1, tails)
        s_star, fp_crit, _upper = tz15.crit(a, ALPHA1)
        assert indep["c"] == s_star, "V4 (d): tau %d: c at r = 1 is %d, tz15.crit's %d" % (
            tau, indep["c"], s_star)
        assert indep["FP_E"] == fp_crit, "V4 (d): tau %d: FP_E at r = 1 is %s, tz15.crit's %s" \
            % (tau, indep["FP_E"], fp_crit)
        assert look["FP_E"] <= ALPHA1 and look["FP_N"] <= BETA1, \
            "section 4.1: tau %d: a false-reading rate above its allocation" % tau
        projection = look_constants(a + a[::2], q + q[::2], r, ALPHA2, BETA2)
        distinct = collections.Counter(a)
        out[tau] = {"n": n, "mu0": look["mu0"], "mu1": look["mu1"], "r": r,
                    "f": dep[tau]["dependence"]["f"],
                    "look": look, "independence": indep, "projection": projection,
                    "v4d": {"c": s_star, "FP_E": fp_crit},
                    "distinct_a": [[price, distinct[price]] for price in sorted(distinct)],
                    "power_sums_q": [sum((x ** k for x in q), D(0)) for k in (1, 2, 3, 4)],
                    "sum_fee": sum((t["fee"] for t in sel), D(0)),
                    "members": [{"T0": t["T0"], "side": t["side"], "a": t["a"], "q": t["q"],
                                 "fee": t["fee"]} for t in sel]}
    return out


# ---- section 3.10: the chain book's interlock on Tier C --------------------------------

def interlock(considered, manifests):
    """Every unit the set rule considered, split by its exposure to the chain book.

    Exposed: `T0 >= 1790185200`, `T0 mod 900 = 600` and the window `T0 - 600`'s `window.json`
    present; fully loaded where its `missed` is `0`. Control: every other unit with a manifest.
    A failure is a manifest whose `quotes_complete` is not JSON `true`. Reads `window.json` and
    the chain book's `runtime.jsonl` and no other file under its root.
    """
    units = []
    for row in considered:
        t0 = row["T0"]
        doc = manifests.get(t0)
        unit = {"T0": t0, "group": None, "failure": None, "quotes_complete": None,
                "fully_loaded": None, "missed": None}
        if doc is None:
            unit["group"] = "no manifest"
            units.append(unit)
            continue
        unit["quotes_complete"] = doc.get("quotes_complete")
        unit["failure"] = doc.get("quotes_complete") is not True
        unit["group"] = "control"
        if t0 >= EXPOSED_FROM and t0 % WINDOW_S == EXPOSED_OFFSET:
            path = os.path.join(CHAINBOOK_ROOT, str(t0 - EXPOSED_OFFSET), WINDOW_NAME)
            if os.path.exists(path):
                with open(path, encoding="utf-8") as fh:
                    window = json.load(fh)
                missed = window.get("missed")
                unit["group"] = "exposed"
                unit["missed"] = missed
                unit["fully_loaded"] = isinstance(missed, int) and not isinstance(missed, bool) \
                    and missed == 0
        units.append(unit)
    exposed = [u for u in units if u["group"] == "exposed"]
    control = [u for u in units if u["group"] == "control"]
    apart = [u for u in units if u["group"] == "no manifest"]
    f_e, m_e = sum(1 for u in exposed if u["failure"]), len(exposed)
    f_c, m_c = sum(1 for u in control if u["failure"]), len(control)
    assert m_e + m_c + len(apart) == len(considered), "V13: the groups do not add up"
    assert f_e <= m_e and f_c <= m_c, "V13: more failures than units"
    p_i = fisher_upper(f_e, m_e, f_c, m_c)
    reading = interlock_reading(f_e, p_i)
    power = []
    for q in POWER_QS:
        k_star, prob = interlock_power(m_e, m_c, q)
        power.append({"q": q, "k_star": k_star, "power": prob})
    eras = {}
    for name, keep in (("before", lambda t0: t0 < EXPOSED_FROM),
                       ("after", lambda t0: t0 >= EXPOSED_FROM)):
        eras[name] = {"exposed": sum(1 for u in exposed if keep(u["T0"])),
                      "exposed_failures": sum(1 for u in exposed if keep(u["T0"]) and u["failure"]),
                      "control": sum(1 for u in control if keep(u["T0"])),
                      "control_failures": sum(1 for u in control if keep(u["T0"]) and u["failure"]),
                      "no_manifest": sum(1 for u in apart if keep(u["T0"]))}
    records, torn = [], 0
    with open(CHAINBOOK_RUNTIME, encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
                records.append({"event": rec.get("event"), "pid": rec.get("pid"),
                                "wall_ns": rec.get("wall_ns")})
            except (ValueError, AttributeError):
                torn += 1
    start = [r for r in records if r["event"] == "start" and r["pid"] == SERVICE_PID
             and r["wall_ns"] == SERVICE_START_NS]
    stops = [r for r in records if r["event"] == "stop" and r["pid"] == SERVICE_PID
             and isinstance(r["wall_ns"], int) and r["wall_ns"] > SERVICE_START_NS]
    return {"units": units, "considered": len(considered), "f_E": f_e, "m_E": m_e,
            "f_C": f_c, "m_C": m_c, "no_manifest": [u["T0"] for u in apart],
            "fully_loaded": sum(1 for u in exposed if u["fully_loaded"]),
            "failures": [u["T0"] for u in units if u["failure"]],
            "exposed_failures": [u["T0"] for u in exposed if u["failure"]],
            "p_I": p_i, "reading": reading, "power": power, "eras": eras,
            "runtime_records": records, "runtime_torn": torn,
            "service_start_found": bool(start), "service_stop_follows": bool(stops)}


# ---- section 3.8: the labels, read once ------------------------------------------------

def labels(trades):
    """The one label read, after the constants are on disk and `HEAD` is on `origin`.

    The push is asserted from `git rev-parse` and `git branch -r --contains`, each a fixed
    argument list with no shell, so no label is read by a commit that is not on `origin`.
    """
    code, head = git("rev-parse", "HEAD")
    assert code == 0, "V5: git rev-parse failed"
    code, text = git("branch", "-r", "--contains", head)
    assert code == 0, "V5: git branch -r --contains failed"
    branches = [b.strip() for b in text.splitlines() if b.strip()]
    assert "origin/" + BRANCH in branches, \
        "V5: HEAD %s is not on origin/%s; it is on %r" % (head, BRANCH, branches)
    eligible = sorted({t0 for (t0, _tau), t in trades.items() if t["eligible"]})
    selected = {t0 for (t0, _tau), t in trades.items() if t["selected"]}
    assert selected <= set(eligible), "section 3.8: a selected member is not eligible"
    when, when_ns = _utc(time.time()), time.time_ns()
    read = tz10b.m2_labels(eligible)
    done_ns = time.time_ns()
    line = {"utc": when, "head": head, "members": len(eligible),
            "member_list_sha256": tz07b.member_list_sha(eligible)}
    with open(LEDGER_PATH, "at", encoding="utf-8") as fh:
        fh.write(json.dumps(line, sort_keys=True) + "\n")
    with open(LEDGER_PATH, encoding="utf-8") as fh:
        ledger = [l.rstrip("\n") for l in fh if l.strip()]
    return read, {"line": line, "ledger": ledger, "read_started_ns": when_ns,
                  "read_done_ns": done_ns, "branches_containing_head": branches}


# ---- section 3.9 and section 4: after the label read, every figure is total -----------

def _y_of(trade, read):
    """1 where the side bought won: the label for `Up`, one minus it for `Down`."""
    label = read[trade["T0"]]
    return label if trade["side"] == tz14.UP else 1 - label


def observed(trades, consts, read):
    """`S`, `T`, `T_fee`, the win rate beside the mean `a` and `q`, and section 4.1's reading."""
    out = {}
    for tau in ADMITTED:
        sel = _selected(trades, tau)
        c = consts[tau]
        n = len(sel)
        ys = [_y_of(t, read) for t in sel]
        S = sum(ys)
        look = c["look"]
        reading, rejected = read_look(n, S, look["c"], look["d"])
        T = ((D(S) - c["mu0"]) / D(n)) if n else None
        out[tau] = {"n": n, "S": S, "mu0": c["mu0"], "mu1": c["mu1"], "sum_fee": c["sum_fee"],
                    "T": T, "T_fee": (T - c["sum_fee"] / D(n)) if n else None,
                    "win_rate": (D(S) / D(n)) if n else None,
                    "mean_a": (c["mu0"] / D(n)) if n else None,
                    "mean_q": (c["mu1"] / D(n)) if n else None,
                    "c": look["c"], "d": look["d"], "FP_E": look["FP_E"], "FP_N": look["FP_N"],
                    "reading": reading, "claim_rejected": rejected, "row": _row_of(n, reading),
                    "y": ys, "T0": [t["T0"] for t in sel]}
    return out


def influence(trades, consts, obs):
    """The member whose `|x - T|` is largest, `x = y - a`, removed, and the look recomputed.

    Ties go to the smallest `T0`. `mu0`, `mu1`, `U0`, `U1`, `c`, `d`, `FP_E`, `FP_N`, `S` and the
    reading are recomputed exactly on the `n - 1` at the same `r`. Recorded, not a reading.
    """
    out = {}
    for tau in ADMITTED:
        sel = _selected(trades, tau)
        o = obs[tau]
        if o["n"] < 2:
            out[tau] = {"defined": False, "why": "n < 2", "n": o["n"]}
            continue
        worst, worst_at = None, None
        for t, y in zip(sel, o["y"]):
            gap = abs((D(y) - t["a"]) - o["T"])
            if worst is None or gap > worst:
                worst, worst_at = gap, t
        kept = [(t, y) for t, y in zip(sel, o["y"]) if t["T0"] != worst_at["T0"]]
        look = look_constants([t["a"] for t, _y in kept], [t["q"] for t, _y in kept],
                              consts[tau]["r"], ALPHA1, BETA1)
        S = sum(y for _t, y in kept)
        reading, rejected = read_look(len(kept), S, look["c"], look["d"])
        out[tau] = {"defined": True, "why": None, "removed_T0": worst_at["T0"],
                    "removed_side": worst_at["side"], "removed_a": worst_at["a"], "gap": worst,
                    "n": len(kept), "S": S, "mu0": look["mu0"], "mu1": look["mu1"],
                    "c": look["c"], "d": look["d"], "FP_E": look["FP_E"], "FP_N": look["FP_N"],
                    "reading": reading, "claim_rejected": rejected}
    return out


def diagnostics(trades, read):
    """Barred from every reading: the mid against `p_t`, and the dependence on this look."""
    out = {}
    for tau in ADMITTED:
        recs = [t for (t0, tt), t in sorted(trades.items()) if tt == tau]
        two = [r for r in recs
               if r["eligible"] and r["bid_up"] is not None and r["ask_up"] is not None]
        doc = {"two_sided_up_books": len(two)}
        if two:
            mids = [(r["bid_up"] + r["ask_up"]) / D(2) for r in two]
            ps = [r["p"] for r in two]
            labs = [D(read[r["T0"]]) for r in two]
            k = D(len(two))
            doc.update({"defined": True, "why": None,
                        "mean_label": sum(labs, D(0)) / k,
                        "mean_mid": sum(mids, D(0)) / k,
                        "mean_p_t": sum(ps, D(0)) / k,
                        "brier_mid": sum(((m - l) ** 2 for m, l in zip(mids, labs)), D(0)) / k,
                        "brier_p_t": sum(((p - l) ** 2 for p, l in zip(ps, labs)), D(0)) / k})
        else:
            doc.update({"defined": False, "why": "no eligible two-sided Up book",
                        "mean_label": None, "mean_mid": None, "mean_p_t": None,
                        "brier_mid": None, "brier_p_t": None})
        sel = [r for r in recs if r["selected"]]
        doc["own_look"] = residual_dependence([D(_y_of(r, read)) - r["a"] for r in sel])
        out[tau] = doc
    return out


def verdict(obs):
    """Section 4.4's verdict over the five `tau`, and which TZ follows."""
    readings = {tau: obs[tau]["reading"] for tau in ADMITTED}
    edge = [t for t in ADMITTED if readings[t] == "EDGE"]
    no_edge = [t for t in ADMITTED if readings[t] == "NO EDGE"]
    undecided = [t for t in ADMITTED if readings[t] == "UNDECIDABLE"]
    names = lambda taus: ", ".join(str(t) for t in taus) or "none"
    if len(no_edge) == len(ADMITTED):
        line = ("Phase 2 reads NO for the Student pricer, inside its domain, at the five tau: "
                "where it disagreed with the market by more than the fee, its side did not win "
                "at the rate it claimed. It says nothing about any other pricer.")
    elif edge:
        line = ("Phase 2 reads YES at tau %s, subject to confirmation (section 4.2); Phase 3 "
                "does not open on it. NO EDGE, closed: %s. UNDECIDABLE, to the second look: %s."
                % (names(edge), names(no_edge), names(undecided)))
    else:
        line = ("NO EDGE, closed: %s. UNDECIDABLE, to section 4.2's second look: %s. No tau "
                "reads EDGE." % (names(no_edge), names(undecided)))
    follows = []
    if undecided:
        follows.append("section 4.2's second look at tau %s" % names(undecided))
    if edge:
        follows.append("a confirmation at tau %s" % names(edge))
    return {"readings": readings, "EDGE": edge, "NO_EDGE": no_edge, "UNDECIDABLE": undecided,
            "claim_rejected": [t for t in ADMITTED if obs[t]["claim_rejected"]],
            "verdict": line,
            "follows": " and ".join(follows) if follows else "neither",
            "FP_E_sum": sum((obs[t]["FP_E"] for t in ADMITTED), D(0)),
            "FP_N_sum": sum((obs[t]["FP_N"] for t in ADMITTED), D(0))}


def predictions(free, dep, lock, obs):
    """Section 3.11's five, TZ-16's word for word. Barred from every gate and every reading."""
    out = [{"id": "P1", "claim": "the eligible count equals the admissible count at every tau",
            "held": all(free[t]["eligible"] == free[t]["admissible"] for t in ADMITTED),
            "observed": ", ".join("%d: %d of %d" % (t, free[t]["eligible"], free[t]["admissible"])
                                  for t in ADMITTED)}]
    if obs is None:
        out.append({"id": "P2", "claim": "no tau reads EDGE", "held": None,
                    "observed": "no label was read in this run"})
        out.append({"id": "P3", "claim": "NO EDGE at tau 240, 180, 120 and 60, and not at 90",
                    "held": None, "observed": "no label was read in this run"})
    else:
        readings = {t: obs[t]["reading"] for t in ADMITTED}
        text = ", ".join("%d: %s" % (t, readings[t]) for t in ADMITTED)
        out.append({"id": "P2", "claim": "no tau reads EDGE",
                    "held": not any(r == "EDGE" for r in readings.values()), "observed": text})
        out.append({"id": "P3", "claim": "NO EDGE at tau 240, 180, 120 and 60, and not at 90",
                    "held": all(readings[t] == "NO EDGE" for t in (240, 180, 120, 60))
                    and readings[90] != "NO EDGE", "observed": text})
    fs = {t: dep[t]["dependence"]["f"] for t in ADMITTED}
    out.append({"id": "P4", "claim": "f < 1.3 at all five tau",
                "held": all(fs[t] < P4_BOUND for t in ADMITTED),
                "observed": ", ".join("%d: %s" % (t, _sig(fs[t], 6)) for t in ADMITTED)})
    out.append({"id": "P5", "claim": "the interlock reads HOLD", "held": lock["reading"] == "HOLD",
                "observed": "%s, f_E = %d of m_E = %d, f_C = %d of m_C = %d, p_I = %s"
                % (lock["reading"], lock["f_E"], lock["m_E"], lock["f_C"], lock["m_C"],
                   lock["p_I"])})
    return out


# ---- formatting: every function here is total ------------------------------------------

def _fixed(value, places):
    """`value` to `places` decimals; the value itself where it cannot be; a dash for None."""
    if value is None:
        return "—"
    try:
        return format(value.quantize(D(1).scaleb(-places)), "f")
    except (AttributeError, ArithmeticError, TypeError, ValueError):
        return str(value)


def _sig(value, digits=20):
    """`value` to `digits` significant digits; a dash for None."""
    if value is None:
        return "—"
    try:
        return str(decimal.Context(prec=digits).plus(value))
    except (AttributeError, ArithmeticError, TypeError, ValueError):
        return str(value)


def _exact(value):
    return "—" if value is None else str(value)


def _frac10(value):
    """A `Fraction` as its exact ratio and to ten decimals."""
    try:
        dec = (D(value.numerator) / D(value.denominator)).quantize(D("1e-10"))
        return "%s (%s)" % (value, dec)
    except (AttributeError, ArithmeticError, TypeError, ValueError, ZeroDivisionError):
        return str(value)


def _ratio(value, digits):
    """A `Fraction` to `digits` significant digits, for one whose exact ratio runs to hundreds."""
    try:
        return _sig(D(value.numerator) / D(value.denominator), digits)
    except (AttributeError, ArithmeticError, TypeError, ValueError, ZeroDivisionError):
        return str(value)


def _jsonable(value):
    """Everything in the documents, as JSON can carry it: Decimal and Fraction as strings."""
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    if isinstance(value, (bool, int, str)) or value is None:
        return value
    if isinstance(value, float):
        return repr(value)
    return str(value)


def _dumps(value):
    return json.dumps(_jsonable(value), indent=2, sort_keys=True) + "\n"


def constants_text(doc):
    """`tz16a-constants.json`: section 3.7 per `tau`, section 3.2's figures, and the inputs."""
    body = {"ADMITTED": list(ADMITTED), "alpha1": ALPHA1, "beta1": BETA1, "alpha2": ALPHA2,
            "beta2": BETA2, "set_sha256": doc["set"]["sha256"], "members": doc["set"]["members"],
            "units_considered": doc["set"]["considered"],
            "tz15_files": {k: v for k, v in doc["located"].items() if k != "constants_per_tau"},
            "tz15_constants_per_tau": {tau: {"n": e["n"], "sum_a": e["sum_a_text"],
                                             "sum_q": e["sum_q_text"]}
                                       for tau, e in doc["located"]["constants_per_tau"].items()},
            "dependence": {tau: _dep_figures(doc["dep"][tau]) for tau in ADMITTED},
            "per_tau": {tau: {k: v for k, v in doc["constants"][tau].items()}
                        for tau in ADMITTED}}
    return _dumps(body)


def _dep_figures(entry):
    """Section 3.2's printed figures for one `tau`: the exact sums, and `rho`, `f_hat`, `f`, `r`."""
    dep = entry["dependence"]
    out = {"n": entry["n"], "sum_a": entry["sum_a"], "sum_q": entry["sum_q"],
           "sum_y": entry["sum_y"], "defined": dep["defined"], "why": dep["why"]}
    if dep["defined"]:
        out.update({"sum_x": dep["sum_x"], "sum_x2": dep["sum_x2"], "P": dep["P"], "A": dep["A"],
                    "B": dep["B"], "rho": dep["rho"], "f_hat": dep["f_hat"], "f": dep["f"],
                    "r": dep["r"]})
    return out


def csv_text(doc):
    """V11: one row per member per `tau` in `ADMITTED` — 12,000 rows and a header.

    TZ-15's eighteen columns in TZ-15's order; `label` and `y` are empty in a run that read no
    label. With the constants file it reconstructs every number of sections 3.6, 3.7 and 3.9.
    """
    read = doc.get("label_read") or {}
    out = [",".join(OBS_COLUMNS)]
    for key in sorted(doc["trades"]):
        t = doc["trades"][key]
        row = doc["rows"][key]
        lab = read.get(key[0])
        y = None
        if lab is not None and t["selected"]:
            y = lab if t["side"] == tz14.UP else 1 - lab
        out.append(",".join(tz14.cell(v) for v in (
            key[0], key[1], row["sigma_hat"], row["admissible"], repr(row["p_t"]),
            t["ask_up"], t["bid_up"], t["ask_dn"], t["bid_dn"], t["e_up"], t["e_dn"],
            t["selected"], t["side"], t["a"], t["q"], t["fee"], lab, y)))
    return "\n".join(out) + "\n"


def disclosure_text(doc):
    """V11: every unit considered, the eligible and selected lists, and the listed reads."""
    lock = {u["T0"]: u for u in doc["interlock"]["units"]}
    members = set(doc["members"])
    out = ["# TZ-16a — disclosure", "",
           "## Every unit considered, ascending `T0`", "",
           "| `T0` | UTC | weekday | member | reasons | `quotes_complete` | interlock group |",
           "|---|---|---|---|---|---|---|"]
    for row in doc["considered"]:
        t0 = row["T0"]
        u = lock.get(t0, {})
        qc = u.get("quotes_complete")
        out.append("| %d | %s | %s | %s | %s | %s | %s |"
                   % (t0, _utc(t0), tz14.weekday_of(t0), "yes" if t0 in members else "no",
                      ", ".join(row["reasons"]) or "—",
                      "—" if u.get("group") == "no manifest" else json.dumps(qc),
                      u.get("group") or "—"))
    for tau in ADMITTED:
        for kind in ("eligible", "selected"):
            lst = sorted(t["T0"] for (t0, tt), t in doc["trades"].items() if tt == tau and t[kind])
            out += ["", "## tau %d — %s: %d members" % (tau, kind, len(lst)), "",
                    "`tz07b.member_list_sha` = `%s`" % tz07b.member_list_sha(lst), "",
                    "```", ", ".join(str(t) for t in lst) or "(none)", "```"]
    out += ["", "## Section 3.5 — the listed reads, by reason", "",
            "| `T0` | `tau` | token id | reason |", "|---|---|---|---|"]
    for e in doc["quotes"]["listed"]:
        out.append("| %d | %s | %s | %s |" % (e["T0"], _exact(e["tau"]), _exact(e["token_id"]),
                                              e["why"]))
    if not doc["quotes"]["listed"]:
        out.append("| — | — | — | none listed |")
    return "\n".join(out) + "\n"


def readings_text(doc):
    """V3's deterministic record of what sections 3.3 to 3.11 and section 4 produced."""
    obs = doc.get("observed")
    lock = {k: v for k, v in doc["interlock"].items() if k != "units"}
    body = {"ADMITTED": list(ADMITTED), "score": doc["mode"] == "score",
            "set": {k: v for k, v in doc["set"].items() if k not in ("clock", "clock_bound")},
            "admissible": doc["admissible"],
            "quotes": {k: v for k, v in doc["quotes"].items() if k != "listed"},
            "label_free": doc["free"],
            "v4": doc["v4"], "dependence": {tau: _dep_figures(doc["dep"][tau]) for tau in ADMITTED},
            "constants": {tau: {k: v for k, v in doc["constants"][tau].items()
                                if k not in ("members", "distinct_a")} for tau in ADMITTED},
            "interlock": lock, "predictions": doc["predictions"]}
    if obs is not None:
        body["observed"] = {tau: {k: v for k, v in obs[tau].items() if k not in ("y", "T0")}
                            for tau in ADMITTED}
        body["influence"] = doc["influence"]
        body["diagnostics"] = doc["diagnostics"]
        body["verdict"] = doc["verdict"]
        body["labels_read"] = len(doc["label_read"])
        body["labels_up"] = sum(doc["label_read"].values())
    return _dumps(body)


def tables(doc):
    """Every table the report prints, from this run's own numbers and nothing else."""
    free, consts, lock, dep = doc["free"], doc["constants"], doc["interlock"], doc["dep"]
    obs = doc.get("observed")
    out = ["# TZ-16a — Phase 2's decisive gate, first look", ""]
    out += ["## Summary", ""]
    if obs is None:
        out.append("- **No label was read in this run.** It stopped at step 11 with its "
                   "constants on disk.")
    else:
        v = doc["verdict"]
        out.append("- **Reading per `tau`:** " + "; ".join(
            "%d **%s**%s" % (t, v["readings"][t], " (the claimed size is also rejected)"
                             if obs[t]["claim_rejected"] else "") for t in ADMITTED) + ".")
        out.append("- **Verdict (section 4.4):** " + v["verdict"])
        out.append("- **Which TZ must follow:** " + v["follows"] + ".")
    out.append("- **Interlock (sections 3.10 and 4.3):** **%s** — `f_E` = %d of `m_E` = %d, "
               "`f_C` = %d of `m_C` = %d, `p_I` = %s." % (lock["reading"], lock["f_E"],
                                                         lock["m_E"], lock["f_C"], lock["m_C"],
                                                         _frac10(lock["p_I"])))
    out.append("")

    loc = doc["located"]
    out += ["## Section 3.1 — TZ-15's two files, located by hash", "",
            "Regular files hashed under `%s`: %d." % (loc["work_root"],
                                                      loc["regular_files_hashed"]), "",
            "| file | SHA-256 | copies | read |", "|---|---|---|---|",
            "| `tz15-observations.csv` | `%s` | %d | `%s` |" % (
                loc["observations"]["sha256"], loc["observations"]["copies"],
                loc["observations"]["read"]),
            "| `tz15-constants.json` | `%s` | %d | `%s` |" % (
                loc["constants"]["sha256"], loc["constants"]["copies"],
                loc["constants"]["read"]), ""]
    v4 = doc["v4"]
    out += ["## Section 3.2 and V4 (a) — the file against the literals and the constants file",
            "", "| `tau` | `n` | constants `n` | `sum y` | `sum a` | constants `sum_a` | "
            "`sum q` | constants `sum_q` |", "|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        e = v4["per_tau"][tau]
        out.append("| %d | %d | %d | %d | %s | %s | %s | %s |"
                   % (tau, e["n"], e["constants_n"], e["sum_y"], e["sum_a"],
                      e["constants_sum_a"], e["sum_q"], e["constants_sum_q"]))
    out += ["", "**V4 (a): %d of %d comparisons hold; V4 (b): %d of %d.**"
            % (v4["a_held"], V4A_COMPARISONS, v4["b_held"], V4B_COMPARISONS), "",
            "| `tau` | `s*` | `FP` | quoted | gap | `POWER` at `s*` | quoted | gap |",
            "|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        e = v4["per_tau"][tau]
        out.append("| %d | %d | %s | %s | %s | %s | %s | %s |"
                   % (tau, e["s_star"], _fixed(e["FP"], 15), e["FP_quoted"],
                      _sig(e["FP_gap"], 3), _fixed(e["POWER"], 9), e["POWER_quoted"],
                      _sig(e["POWER_gap"], 3)))
    out += ["", "## Section 3.2 — the dependence of the null's residual on TZ-15's set", "",
            "Exact sums over `x = y - a` in ascending `T0`:", "",
            "| `tau` | `n` | `sum x` | `sum x^2` |", "|---|---|---|---|"]
    for tau in ADMITTED:
        d = dep[tau]["dependence"]
        out.append("| %d | %d | %s | %s |" % (tau, dep[tau]["n"], _exact(d.get("sum_x")),
                                              _exact(d.get("sum_x2"))))
    out += ["", "| `tau` | `k` | `P_k` | `A_k` | `B_k` |", "|---|---|---|---|---|"]
    for tau in ADMITTED:
        d = dep[tau]["dependence"]
        for i, k in enumerate(LAGS):
            out.append("| %d | %d | %s | %s | %s |" % (tau, k, _exact(d["P"][i]),
                                                       _exact(d["A"][i]), _exact(d["B"][i])))
    out += ["", "To 20 significant digits:", "",
            "| `tau` | `rho_1` | `rho_2` | `rho_3` | `f_hat` | `f` | `r` |",
            "|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        d = dep[tau]["dependence"]
        out.append("| %d | %s | %s | %s | %s | %s | %s |"
                   % (tau, _sig(d["rho"][0]), _sig(d["rho"][1]), _sig(d["rho"][2]),
                      _sig(d["f_hat"]), _sig(d["f"]), _sig(d["r"])))

    s = doc["set"]
    out += ["", "## Section 3.3 — the set", "",
            "| units considered | members | first unit | last unit | member-list SHA-256 |",
            "|---|---|---|---|---|",
            "| %d | %d | %d | %d | `%s` |" % (s["considered"], s["members"], s["first_unit"],
                                               s["last_unit"], s["sha256"]), "",
            "First member `%d` (%s), last `%d` (%s). Weekend members: %d."
            % (s["first_member"], s["first_member_utc"], s["last_member"],
               s["last_member_utc"], s["weekend_members"]), "",
            "| weekday | members |", "|---|---|"]
    for day, n in s["weekday_counts"].items():
        out.append("| %s | %d |" % (day, n))
    out += ["", "Non-members, %d, by reason:" % len(s["non_members"]), "",
            "| reasons | units |", "|---|---|"]
    for why, n in s["non_member_reasons"].items():
        out.append("| %s | %d |" % (why, n))
    out += ["", "Every non-member, by reason:", ""]
    for why in s["non_member_reasons"]:
        out.append("- %s: %s" % (why, ", ".join(str(u["T0"]) for u in s["non_members"]
                                               if ", ".join(u["reasons"]) == why)))
    out += ["", "## Section 3.4 — the pricer at each checkpoint", "",
            "| `tau` | admissible | weekday | weekend |", "|---|---|---|---|"]
    for tau in ADMITTED:
        a = doc["admissible"][tau]
        out.append("| %d | %d | %d | %d |" % (tau, a["admissible"], a["weekday"], a["weekend"]))
    qd = doc["quotes"]
    out += ["", "## Section 3.5 — the quotes at each admitted checkpoint", "",
            "| `tau` | reads present | reads used | listed |", "|---|---|---|---|"]
    for tau in ADMITTED:
        listed = sum(e["count"] for e in qd["listed_by_reason"] if e["tau"] == tau)
        out.append("| %d | %d | %d | %d |" % (tau, qd["present"][tau], qd["used"][tau], listed))
    out += ["", "Listed, by reason:", "", "| `tau` | reason | count |", "|---|---|---|"]
    for e in qd["listed_by_reason"]:
        out.append("| %s | %s | %d |" % (_exact(e["tau"]), e["why"], e["count"]))
    if not qd["listed_by_reason"]:
        out.append("| — | none listed | 0 |")

    out += ["", "## Section 3.6 — eligibility, selection and the claim, before any label", "",
            "| `tau` | admissible | eligible | selected | Up | Down | weekday | weekend | "
            "both edges positive | at or below 0.10 |", "|---|---|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        f = free[tau]
        out.append("| %d | %d | %d | %d | %d | %d | %d | %d | %d | %d |"
                   % (tau, f["admissible"], f["eligible"], f["selected"], f["selected_up"],
                      f["selected_down"], f["selected_weekday"], f["selected_weekend"],
                      f["both_edges_positive"], f["selected_at_or_below_0.10"]))
    out += ["", "| `tau` | `n` | min `a` | 0.25 | median `a` | 0.75 | max `a` | mean `q - a` | "
            "mean `q - a - fee(a)` |", "|---|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        f, q = free[tau], free[tau]["q_price_paid"]
        out.append("| %d | %d | %s | %s | %s | %s | %s | %s | %s |"
                   % (tau, f["selected"], _exact(q["min"]), _exact(q["0.25"]), _exact(q["0.50"]),
                      _exact(q["0.75"]), _exact(q["max"]), _fixed(f["mean_claimed_edge"], 6),
                      _fixed(f["mean_after_fee_claim"], 6)))
    out += ["", "| `tau` | `q - a`: min | 0.25 | median | 0.75 | 0.90 | max |",
            "|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        q = free[tau]["q_claimed_edge"]
        out.append("| %d | %s | %s | %s | %s | %s | %s |"
                   % (tau, _fixed(q["min"], 6), _fixed(q["0.25"], 6), _fixed(q["0.50"], 6),
                      _fixed(q["0.75"], 6), _fixed(q["0.90"], 6), _fixed(q["max"], 6)))
    out += ["", "Over the eligible checkpoints whose Up book is two-sided at the touch, "
            "`D = p - (bid_up + ask_up) / 2`:", "",
            "| `tau` | books | min `D` | 0.25 | median | 0.75 | max | market more confident |",
            "|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        f, q = free[tau], free[tau]["q_p_minus_mid"]
        out.append("| %d | %d | %s | %s | %s | %s | %s | %d (%s) |"
                   % (tau, f["two_sided_up_books"], _fixed(q["min"], 6), _fixed(q["0.25"], 6),
                      _fixed(q["0.50"], 6), _fixed(q["0.75"], 6), _fixed(q["max"], 6),
                      f["market_more_confident"], _fixed(f["market_more_confident_share"], 4)))

    out += ["", "## Section 3.7 — the gate's constants, exact, on disk before any label", "",
            "`alpha1 = beta1 = %s`; the look at the `r` of section 3.2:" % ALPHA1, "",
            "| `tau` | `n` | `mu0` | `mu1` | `r` | `c` | `d` | `FP_E` | `FP_N` | `POWER_E` | "
            "`POWER_N` |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        c = consts[tau]
        k = c["look"]
        out.append("| %d | %d | %s | %s | %s | %d | %d | %s | %s | %s | %s |"
                   % (tau, c["n"], _exact(c["mu0"]), _fixed(c["mu1"], 12), _sig(c["r"]),
                      k["c"], k["d"], _fixed(k["FP_E"], 12), _fixed(k["FP_N"], 12),
                      _fixed(k["POWER_E"], 6), _fixed(k["POWER_N"], 6)))
    out += ["", "`FP_E` sums to %s and `FP_N` to %s over the five `tau`."
            % (_fixed(sum((consts[t]["look"]["FP_E"] for t in ADMITTED), D(0)), 12),
               _fixed(sum((consts[t]["look"]["FP_N"] for t in ADMITTED), D(0)), 12)), "",
            "Independence beside it, at `r = 1`, barred from every reading:", "",
            "| `tau` | `c` | `d` | `FP_E` | `FP_N` | `POWER_E` | `POWER_N` | `tz15.crit` `s*` / "
            "`FP` |", "|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        k, c4 = consts[tau]["independence"], consts[tau]["v4d"]
        out.append("| %d | %d | %d | %s | %s | %s | %s | %d / %s |"
                   % (tau, k["c"], k["d"], _fixed(k["FP_E"], 12), _fixed(k["FP_N"], 12),
                      _fixed(k["POWER_E"], 6), _fixed(k["POWER_N"], 6), c4["c"],
                      _fixed(c4["FP_E"], 12)))
    out += ["", "The second look's projection, `w + w[::2]` at `alpha2 = beta2 = %s` and the same "
            "`r`, barred from every reading:" % ALPHA2, "",
            "| `tau` | coins | `c` | `d` | `FP_E` | `FP_N` | `POWER_E` | `POWER_N` |",
            "|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        k = consts[tau]["projection"]
        out.append("| %d | %d | %d | %d | %s | %s | %s | %s |"
                   % (tau, k["n"], k["c"], k["d"], _fixed(k["FP_E"], 12), _fixed(k["FP_N"], 12),
                      _fixed(k["POWER_E"], 6), _fixed(k["POWER_N"], 6)))
    out += ["", "Exact, per `tau`:", ""]
    for tau in ADMITTED:
        c, k = consts[tau], consts[tau]["look"]
        out += ["- `tau` %d: `r` = `%s`; `FP_E` = `%s`; `FP_N` = `%s`; `POWER_E` = `%s`; "
                "`POWER_N` = `%s`." % (tau, c["r"], k["FP_E"], k["FP_N"], k["POWER_E"],
                                        k["POWER_N"])]
    out += ["", "The alternative's first four power sums, `sum q^k`:", "",
            "| `tau` | `sum q` | `sum q^2` | `sum q^3` | `sum q^4` |", "|---|---|---|---|---|"]
    for tau in ADMITTED:
        ps = consts[tau]["power_sums_q"]
        out.append("| %d | %s | %s | %s | %s |" % (tau, ps[0], _sig(ps[1], 30), _sig(ps[2], 30),
                                                   _sig(ps[3], 30)))
    out += ["", "The null's weights as distinct prices with their counts — they fix `U0` "
            "exactly:", ""]
    for tau in ADMITTED:
        dist = consts[tau]["distinct_a"]
        out += ["- `tau` %d, %d coins, %d distinct prices: %s" % (
            tau, consts[tau]["n"], len(dist),
            ", ".join("%s × %d" % (price, n) for price, n in dist) or "none")]

    out += ["", "## Section 3.10 and section 4.3 — the interlock", "",
            "| group | units | failures |", "|---|---|---|",
            "| exposed | %d | %d |" % (lock["m_E"], lock["f_E"]),
            "| control | %d | %d |" % (lock["m_C"], lock["f_C"]),
            "| no manifest, apart | %d | — |" % len(lock["no_manifest"]),
            "| considered | %d | — |" % lock["considered"], "",
            "| era | exposed | exposed failures | control | control failures | no manifest |",
            "|---|---|---|---|---|---|"]
    for era, label in (("before", "`T0 < %d`" % EXPOSED_FROM),
                       ("after", "`T0 >= %d`" % EXPOSED_FROM)):
        e = lock["eras"][era]
        out.append("| %s | %d | %d | %d | %d | %d |" % (label, e["exposed"], e["exposed_failures"],
                                                         e["control"], e["control_failures"],
                                                         e["no_manifest"]))
    out += ["", "Fully loaded exposed units: %d of %d." % (lock["fully_loaded"], lock["m_E"]),
            "Failures, every `T0`: %s." % (", ".join(str(t) for t in lock["failures"]) or "none"),
            "Units with no manifest: %s." % (", ".join(str(t) for t in lock["no_manifest"])
                                             or "none"), "",
            "`p_I` = %s. **Reading: %s.**" % (_frac10(lock["p_I"]), lock["reading"]), "",
            "| `q` | `k*` | P(Bin(`m_E`, `q`) >= `k*`) |", "|---|---|---|"]
    for p in lock["power"]:
        out.append("| %s | %s | %s |" % (p["q"], _exact(p["k_star"]), _ratio(p["power"], 20)))
    out += ["", "The chain book's `runtime.jsonl`, every record (%d; %d unparsed):"
            % (len(lock["runtime_records"]), lock["runtime_torn"]), "",
            "| event | pid | `wall_ns` |", "|---|---|---|"]
    for rec in lock["runtime_records"]:
        out.append("| %s | %s | %s |" % (_exact(rec["event"]), _exact(rec["pid"]),
                                         _exact(rec["wall_ns"])))
    out += ["", "The start record of pid %d at `wall_ns` %d: %s. A `stop` record of that pid "
            "after it: %s." % (SERVICE_PID, SERVICE_START_NS,
                               "found" if lock["service_start_found"] else "not found",
                               "yes" if lock["service_stop_follows"] else "no")]

    if obs is not None:
        v = doc["verdict"]
        out += ["", "## Section 3.9 and section 4.1 — the observed statistic and the reading", "",
                "| `tau` | `n` | `S` | `c` | `d` | `sum a` | win rate | mean `a` | mean `q` | "
                "`T` | `T_fee` | row | **reading** |",
                "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for tau in ADMITTED:
            o = obs[tau]
            out.append("| %d | %d | %d | %d | %d | %s | %s | %s | %s | %s | %s | `%s` | **%s**%s |"
                       % (tau, o["n"], o["S"], o["c"], o["d"], _exact(o["mu0"]),
                          _fixed(o["win_rate"], 6), _fixed(o["mean_a"], 6),
                          _fixed(o["mean_q"], 6), _fixed(o["T"], 6), _fixed(o["T_fee"], 6),
                          o["row"], o["reading"],
                          " — the claimed size is also rejected" if o["claim_rejected"] else ""))
        out += ["", "**Error rates of this look, exact under the model each test scores:** "
                "`FP_E` sums to %s and `FP_N` to %s over the five `tau`."
                % (_fixed(v["FP_E_sum"], 12), _fixed(v["FP_N_sum"], 12)), "",
                "**The verdict.** " + v["verdict"], "",
                "**Which TZ must follow:** " + v["follows"] + ".", "",
                "## Section 3.9 — influence, recorded, not a reading", "",
                "| `tau` | removed `T0` | side | `a` | `n - 1` | `S` | `c` | `d` | `FP_E` | `FP_N` "
                "| reading |", "|---|---|---|---|---|---|---|---|---|---|---|"]
        for tau in ADMITTED:
            i = doc["influence"][tau]
            if not i["defined"]:
                out.append("| %d | — | — | — | — | — | — | — | — | — | undefined: %s |"
                           % (tau, i["why"]))
                continue
            out.append("| %d | %d | %s | %s | %d | %d | %d | %d | %s | %s | %s |"
                       % (tau, i["removed_T0"], i["removed_side"], _exact(i["removed_a"]),
                          i["n"], i["S"], i["c"], i["d"], _fixed(i["FP_E"], 12),
                          _fixed(i["FP_N"], 12), i["reading"]))
        out += ["", "## Section 3.9 — diagnostics, each barred from every reading", "",
                "| `tau` | two-sided books | mean label | mean mid | mean `p_t` | Brier mid | "
                "Brier `p_t` |", "|---|---|---|---|---|---|---|"]
        for tau in ADMITTED:
            d = doc["diagnostics"][tau]
            out.append("| %d | %d | %s | %s | %s | %s | %s |"
                       % (tau, d["two_sided_up_books"], _fixed(d["mean_label"], 6),
                          _fixed(d["mean_mid"], 6), _fixed(d["mean_p_t"], 6),
                          _fixed(d["brier_mid"], 6), _fixed(d["brier_p_t"], 6)))
        out += ["", "The dependence on this look's own selected residuals, in `T0` order:", "",
                "| `tau` | `n` | `rho_1` | `rho_2` | `rho_3` | `f_hat` | `f` |",
                "|---|---|---|---|---|---|---|"]
        for tau in ADMITTED:
            own = doc["diagnostics"][tau]["own_look"]
            if not own["defined"]:
                out.append("| %d | %d | undefined: %s | — | — | — | — |" % (tau, own["n"],
                                                                            own["why"]))
                continue
            out.append("| %d | %d | %s | %s | %s | %s | %s |"
                       % (tau, own["n"], _sig(own["rho"][0], 6), _sig(own["rho"][1], 6),
                          _sig(own["rho"][2], 6), _sig(own["f_hat"], 6), _sig(own["f"], 6)))
    out += ["", "## Section 3.11 — the five pre-registered predictions", "",
            "| # | prediction | observed | verdict |", "|---|---|---|---|"]
    for p in doc["predictions"]:
        out.append("| %s | %s | %s | **%s** |"
                   % (p["id"], p["claim"], p["observed"],
                      "held" if p["held"] else ("refuted" if p["held"] is False else "—")))
    out.append("")
    return "\n".join(out) + "\n"


def write_outputs(doc, out_dir):
    """The four files written at the run's last step, each total over the document."""
    texts = {"tz16a-tables.md": tables(doc), "tz16a-observations.csv": csv_text(doc),
             "tz16a-disclosure.md": disclosure_text(doc), "tz16a-readings.json": readings_text(doc)}
    for name, text in sorted(texts.items()):
        with open(os.path.join(out_dir, name), "wt", encoding="utf-8") as fh:
            fh.write(text)
    return {name: hashlib.sha256(text.encode("utf-8")).hexdigest()
            for name, text in sorted(texts.items())}


def after_labels(doc, read):
    """Section 3.9 and section 4, from the labels read. Total: nothing here raises on a label."""
    doc["label_read"] = read
    doc["observed"] = observed(doc["trades"], doc["constants"], read)
    doc["influence"] = influence(doc["trades"], doc["constants"], doc["observed"])
    doc["diagnostics"] = diagnostics(doc["trades"], read)
    doc["verdict"] = verdict(doc["observed"])
    doc["predictions"] = predictions(doc["free"], doc["dep"], doc["interlock"], doc["observed"])
    return doc


# ---- the run ----------------------------------------------------------------------------

def build(mode, out_dir):
    """Section 5.1's fixed order, asserted step by step. `mode` is selftest, free or score."""
    run = {"sequence": SEQUENCES[mode], "visited": [], "marks": [], "v2_runtime": {}}
    doc = {"mode": mode, "run": run, "out_dir": out_dir, "observed": None}

    _step(run, "0")
    before = frozen_now()
    doc["gates"] = v1_gates()
    doc["v8_start"] = v8(before, None)

    _step(run, "1")
    doc["host"] = [host_read("start", set(), tz11a.FLOOR_START_BYTES)]
    assert doc["host"][0]["newest_start_sha"] == START_SHA, \
        "step 1: the newest start record carries %s" % doc["host"][0]["newest_start_sha"]

    _step(run, "2")
    doc["selftests"] = selftests()

    _step(run, "3")
    doc["v6"] = v6(mode)
    doc["v2_static"] = v2_static()
    for step in ("0", "1", "2", "3"):
        v2_step(run, step, 0)
    if mode == "selftest":
        others = sorted({path for path, _m, _f, _s in OPENS if path != tz10b.RUNTIME_PATH})
        assert not others, "section 5.1: --selftest opened %r" % others[:3]
        doc["opens"] = [path for path, _m, _f, _s in OPENS]
        return doc

    _step(run, "4")
    doc["located"] = located = locate()
    doc["dep"], doc["tz15_data_rows"] = dependence(located["observations"]["read"])
    doc["v4"] = v4_tz15(located, doc["dep"])
    v2_step(run, "4", 0)

    _step(run, "5")
    manifests = load_manifests()
    considered, members, doc["set"] = the_set(manifests)
    doc["considered"], doc["members"] = considered, members
    settled = tz14.BANNED_SUBSTRINGS[0] + ".json"
    expected = sum(1 for row in considered if manifests.get(row["T0"]) is not None
                   and os.path.exists(os.path.join(config.interval_dir(row["T0"]), settled)))
    doc["set"]["settled_opens_expected"] = expected
    v2_step(run, "5", expected)

    _step(run, "6")
    doc["rows"], doc["admissible"] = the_rows(members, manifests)
    assert len(doc["rows"]) == CHECKPOINTS, "section 3.0: %d checkpoints" % len(doc["rows"])
    doc["host"].append(host_read("after the rows", set(members), tz11a.FLOOR_BYTES))
    elapsed = time.perf_counter() - T_START
    doc["elapsed_after_step_6_s"] = elapsed
    if elapsed > ROWS_LIMIT_S:
        raise SystemExit("BLOCKED at section 6: %.1f s elapsed after step 6, above %.0f s"
                         % (elapsed, ROWS_LIMIT_S))
    v2_step(run, "6", 0)

    _step(run, "7")
    quotes, doc["quotes"] = the_quotes(members, doc["rows"])
    v2_step(run, "7", 0)

    _step(run, "8")
    doc["trades"] = trades = the_trades(doc["rows"], quotes)
    assert len(trades) == CHECKPOINTS, "V11: %d observation rows, not %d" % (len(trades),
                                                                            CHECKPOINTS)
    doc["free"] = label_free_report(trades)
    doc["rows_checked_8"] = tz15.label_free(list(doc["rows"].values()))
    v2_step(run, "8", 0)

    _step(run, "9")
    doc["constants"] = constants(trades, doc["dep"])
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    text = constants_text(doc)
    with open(os.path.join(out_dir, "tz16a-constants.json"), "wt", encoding="utf-8") as fh:
        fh.write(text)
    doc["constants_written_utc"] = _utc(time.time())
    doc["constants_sha256"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
    doc["rows_checked_9"] = tz15.label_free(list(doc["rows"].values()))
    v2_step(run, "9", 0)

    _step(run, "10")
    doc["interlock"] = interlock(considered, manifests)
    doc["predictions"] = predictions(doc["free"], doc["dep"], doc["interlock"], None)
    v2_step(run, "10", 0)

    if mode == "free":
        _step(run, "11")
        doc["sha256"] = write_outputs(doc, out_dir)
        doc["host"].append(host_read("end", set(members), tz11a.FLOOR_BYTES))
        doc["v8"] = v8(before, frozen_now())
        doc["v9"] = {"host": v9_host(doc["host"]), "opens": v9_opens(members[-1])}
        v2_step(run, "11", 0)
        return doc

    _step(run, "12")
    read, doc["labels"] = labels(trades)
    v2_step(run, "12", doc["labels"]["line"]["members"])

    _step(run, "13")
    after_labels(doc, read)

    _step(run, "14")
    doc["sha256"] = write_outputs(doc, out_dir)
    doc["host"].append(host_read("end", set(members), tz11a.FLOOR_BYTES))
    doc["v8"] = v8(before, frozen_now())
    doc["v9"] = {"host": v9_host(doc["host"]), "opens": v9_opens(members[-1])}
    return doc


def run_text(doc, argv):
    """`tz16a-run.json`: instants, timings and the checks' own records. Not compared by V3."""
    keys = ("mode", "gates", "v8_start", "host", "selftests", "v6", "v2_static", "located",
            "v4", "set", "admissible", "elapsed_after_step_6_s", "constants_written_utc",
            "constants_sha256", "labels", "v8", "v9", "sha256", "tz15_data_rows")
    body = {k: doc.get(k) for k in keys}
    body.update({"marks": doc["run"]["marks"], "visited": doc["run"]["visited"],
                 "v2_runtime": doc["run"]["v2_runtime"], "argv": argv, "pid": os.getpid(),
                 "python": sys.version, "interpreter": sys.executable,
                 "numpy": getattr(sys.modules.get("numpy"), "__version__", None),
                 "elapsed_s": time.perf_counter() - T_START,
                 "peak_rss_kb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                 "session_ceiling_s": tz12.SESSION_CEILING_S, "writable": sorted(
                     [os.path.join(doc["out_dir"], n) for n in OUT_NAMES] + [LEDGER_PATH])
                 if doc["out_dir"] else [LEDGER_PATH]})
    if body["located"] is not None:
        body["located"] = {k: v for k, v in body["located"].items() if k != "constants_per_tau"}
    return _dumps(body)


def main(argv):
    flags = [a for a in argv if a.startswith("--")]
    assert set(flags) <= {"--selftest", "--score", "--out"}, "usage: %r" % flags
    assert not ("--selftest" in flags and "--score" in flags), "--selftest and --score together"
    mode = "selftest" if "--selftest" in flags else ("score" if "--score" in flags else "free")
    out_dir = None
    if "--out" in argv:
        out_dir = os.path.abspath(argv[argv.index("--out") + 1])
    if mode != "selftest":
        assert out_dir is not None, "--out names the run directory"
        assert out_dir.startswith(WORK_ROOT + os.sep), "--out must lie under %s" % WORK_ROOT
        assert not os.path.exists(out_dir), "--out %s already exists" % out_dir
    doc = build(mode, out_dir)
    for line in doc["selftests"]["lines"]:
        sys.stdout.write(line + "\n")
    sys.stdout.write("V7: %d of %d items, %d assertions, per item %s\n"
                     % (doc["selftests"]["items"], len(SELFTEST_COUNTS),
                        doc["selftests"]["assertions"], doc["selftests"]["per_item"]))
    sys.stdout.write("V6: %s\n" % json.dumps(_jsonable(doc["v6"]), sort_keys=True))
    sys.stdout.write("V2 static: %s\n" % json.dumps(_jsonable(doc["v2_static"]), sort_keys=True))
    if mode == "selftest":
        sys.stdout.write("capture opens: %s\n" % doc["opens"])
    else:
        with open(os.path.join(out_dir, RUN_NAME), "wt", encoding="utf-8") as fh:
            fh.write(run_text(doc, argv))
        sys.stdout.write("%s  tz16a-constants.json\n" % doc["constants_sha256"])
        for name, digest in sorted(doc["sha256"].items()):
            sys.stdout.write("%s  %s\n" % (digest, name))
    for mark in doc["run"]["marks"]:
        sys.stdout.write("step %s at %.1f s\n" % (mark["step"], mark["at_s"]))
    sys.stdout.write("elapsed %.1f s, peak RSS %d kB\n"
                     % (time.perf_counter() - T_START,
                        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))


if __name__ == "__main__":
    main(sys.argv[1:])
