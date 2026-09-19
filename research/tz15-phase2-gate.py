#!/usr/bin/env python3
"""TZ-15 — the Phase 2 gate.

The first statistic in this project that puts a quote beside the pricer. At each admissible
checkpoint of TZ-14's 1,200-member set the instrument takes, on paper and one share, the side
`p_t` says is underpriced by more than CANON section 1.1's taker fee, and asks whether that side
won more often than the ask it paid implied.

The null is a market calibrated at its own ask: each trade's outcome is a coin weighted by the
price paid, whatever `p_t` says. The number of wins is then a sum of independent coins with known
weights, so its distribution is computed exactly by one recursion — no simulation — and the
false-positive probability and the power against "the pricer is right" are exact numbers written
to disk before any outcome is read.

Nothing here computes a probability of its own: `p_t` is `tz11a.checkpoint_row`'s and the pricer
row carries nine keys and no settlement-derived quantity. The labels are read once, at section
3.6, only after the constants are on disk and the scoring commit is on `origin`.
"""

import os                                                                  # noqa: E402

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import ast                                                                 # noqa: E402
import collections                                                         # noqa: E402
import hashlib                                                             # noqa: E402
import importlib.util                                                      # noqa: E402
import json                                                                # noqa: E402
import math                                                                # noqa: E402
import re                                                                  # noqa: E402
import resource                                                            # noqa: E402
import subprocess                                                          # noqa: E402
import sys                                                                 # noqa: E402
import time                                                                # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def _load(name, filename):
    """Import a module whose filename carries a hyphen, so it cannot be `import`ed by name."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Section 5.1: one load and no other. `tz14` already loaded `tz12`, which loaded `tz11a`, which
# loaded `tz10b`, which loaded the other three; loading any of them a second time would be two
# module objects with two copies of every table. The load has side effects this TZ names: `tz14`
# writes the same three environment variables and installs an audit hook of its own that records
# the basename of every open under the capture root for the life of the process. Nothing can
# remove it, and this instrument never reads `tz14.CAPTURE_OPENS`.
tz14 = _load("tz14quoteinventory", "tz14-quote-inventory.py")
tz12 = tz14.tz12
tz11a = tz14.tz11a
tz10b = tz14.tz10b
tz07b = tz14.tz07b
tz06 = tz14.tz06
pfair = tz14.pfair
config = tz14.config
D = tz14.D
load_manifests = tz14.load_manifests

import analyze                                                             # noqa: E402
import manifest                                                            # noqa: E402


# ---- V1 and V10: the fingerprint gate's expected values, as literals of this instrument ----

# A gate never reads its own expected values from the file it checks (map section 7 item 67).
REQUIRED_REVISION = "2026-09-19-a"
REQUIRED_ANCHORS = (("A1", "229a944f2d51"), ("A2", "6c5089330629"),
                    ("A3", "0-complete / 1-student-5tau-not-disqualified / 2-inventory-complete"),
                    ("A4", "437b45ea196b"), ("A5", "9fd1c7de0f74"),
                    ("A6", "729f0bcdbee3"))
# The four anchors that are the first 12 hex characters of a committed file's SHA-256, so the
# instrument re-derives them from the bytes instead of trusting the table that prints them.
ANCHOR_FILES = (("A2", "research/twap-divergence.py"),
                ("A4", "BTC-EXECUTOR-INSTRUCTIONS.md"),
                ("A5", "research/recorder/recorder.py"),
                ("A6", "research/pfair.py"))
FROZEN_ROWS = 21
TRACKED_ROWS = 2
MAP_PATH = os.path.join(HERE, os.pardir, "SYSTEM-MAP.md")
PFAIR_PATH = "research/pfair.py"
TZ14_PATH = "research/tz14-quote-inventory.py"
SELF_PATH = "research/tz15-phase2-gate.py"

# ---- section 3.0: the partitions and the counts ------------------------------------

# The five tau Phase 1 did not disqualify inside the pricer's domain. No figure of this TZ is
# computed at tau 30 or 10; the committed functions called below compute them internally and
# they are discarded here.
ADMITTED = (240, 180, 120, 90, 60)
SET_SIZE = 1200
CHECKPOINTS = SET_SIZE * len(ADMITTED)
ADMITTED_READS = CHECKPOINTS * 2

# ---- section 3.1 and V4: the set, quoted from the TZ-14 report ---------------------

SET_SHA256 = "baa5a9d26855ea7ff07d062437df60617ba3e4e70dd74b3ac455a8a71a9b3154"
SET_UNITS = 1296
SET_LAST_MEMBER = 1789595400
# TZ-14 report section 2.2, tau 240 ... 60.
ADMISSIBLE_EXPECTED = ((240, 631), (180, 628), (120, 615), (90, 619), (60, 621))

# V4 (c): TZ-14's own observations file, from its report V11. Its two runs left two identical
# copies under the work root and either is read.
TZ14_WORK = "/root/tz14-work"
TZ14_OBS_SHA256 = "0fc46a68f923acbbb6839a781d92d9b4d2c5afa734d059fa59b49b6e10df5e3a"
# V4 (d): the copy TZ-14's section 9 made into the forensics store, from the TZ-13 report V11.
TZ13_OBS_PATH = "/root/btc-forensics/tz13-work--run1--tz13-observations.csv"
TZ13_OBS_SHA256 = "e78b01b5f06f485d15fe944fb37b17688507d278cb78add5143e12304a322f44"
# Map section 2.3: test 3's first member, and the first instant of the reserved span.
TZ13_FIRST_T0 = 1789428000
RESERVED_AFTER = 1789669800

# ---- section 3.5 and section 4: the gate's own thresholds, literals of this TZ ------

ALPHA = D("0.01")
POWER_FLOOR = D("0.8")
PROJECTION_MULTIPLES = (1, 2, 3)
LOW_PRICE = D("0.10")

# Section 2 item 7: the pricer row's allow-list, and nothing else ever joins it.
ROW_KEYS = ("T0", "tau", "state", "sigma_hat", "admissible", "sd_student", "z_student",
            "p_t", "label")

# Section 2 item 6: the twelve pfair entry points this instrument's own tree never calls.
PFAIR_PROBABILITY = ("p_fair", "p_fair_student", "state_and_sd", "far_branch", "near_branch",
                     "observations", "corrected_sd", "student_sd", "phi", "log_phi",
                     "t_cdf", "log_t_cdf")
# V2: named only as never called.
NEVER_CALLED = (("analyze", "venue"), ("tz11a", "fit_student"))
# V2: the one label reader, called exactly once.
LABEL_READER = ("tz10b", "m2_labels")

# ---- V9 and section 3.6: everything this instrument can write -----------------------

WORK_ROOT = "/root/tz15-work"
LEDGER_PATH = os.path.join(WORK_ROOT, "label-ledger.jsonl")
OUT_NAMES = ("tz15-constants.json", "tz15-readings.json", "tz15-tables.md",
             "tz15-observations.csv", "tz15-disclosure.md", "tz15-run.json")

# ---- section 6: the two fail-fast bounds, both resource guards on wall-clock time ---

T8_WEIGHTS = 1200
T8_WEIGHT = D("0.37")
RECURSION_UNITS = 215976010
RECURSION_BASIS = 1440000
RECURSION_LIMIT_S = 950.0
ROWS_LIMIT_S = 600.0

# V2 and V9, run time: every open of a path under the capture root, with its mode and the step
# of section 5.1 the run was in. Nothing is ever written back into the capture.
OPENS = []
STEP = ["load"]


def _step(name):
    """Move the run to a step of section 5.1. The hook stamps every open with it."""
    STEP[0] = name
    return name


def _audit(event, args):
    """Record every open under the capture root: its absolute path, its mode and the step."""
    if event != "open" or not args or not isinstance(args[0], str):
        return
    try:
        path = os.path.abspath(args[0])
    except (TypeError, ValueError):
        return
    if not path.startswith(config.ROOT + os.sep):
        return
    mode = args[1] if len(args) > 1 and isinstance(args[1], str) else "?"
    OPENS.append((path, mode, STEP[0]))


sys.addaudithook(_audit)


def _sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def _map_text():
    with open(MAP_PATH, encoding="utf-8") as fh:
        return fh.read()


# ---- section 0.1 and V1: the gate, asserted as step 0 of section 5.1 ---------------

def v1_gates():
    """The revision, the six anchors and every row of map section 0's fingerprint table.

    `tz14.v1_gates` is not called: it asserts revision `2026-09-18-b` and twenty rows. Only the
    row reader `tz14.fingerprint_rows` is reused, and every expectation here is a literal above.
    """
    text = _map_text()
    assert ("**Revision string:** `%s`" % REQUIRED_REVISION) in text, \
        "section 0.1: the map does not carry revision %s" % REQUIRED_REVISION
    found = dict(re.findall(r"\|\s*`(A\d)`[^|]*\|\s*`?([^`|]+?)`?\s*\|", text))
    matched = []
    for name, want in REQUIRED_ANCHORS:
        assert found.get(name) == want, \
            "section 0.1: %s reads %r, not %r" % (name, found.get(name), want)
        matched.append(name)
    derived = []
    for name, path in ANCHOR_FILES:
        have = _sha256_file(os.path.join(HERE, os.pardir, path))[:12]
        assert have == dict(REQUIRED_ANCHORS)[name], \
            "section 0.1: %s re-derives to %s from %s" % (name, have, path)
        derived.append({"anchor": name, "path": path, "sha12": have})
    rows, frozen, tracked, reported = [], 0, 0, 0
    for row in tz14.fingerprint_rows():
        full = os.path.join(HERE, os.pardir, row["path"])
        with open(full, "rb") as fh:
            body = fh.read()
        entry = {"path": row["path"], "state": row["state"], "lines": body.count(b"\n"),
                 "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest(),
                 "expected": row["expected"]}
        if row["state"] == "frozen":
            assert entry["sha256"] == row["expected"], \
                "section 0.1: %s hashes to %s, not %s" % (row["path"], entry["sha256"],
                                                          row["expected"])
            frozen += 1
        elif row["state"] == "tracked":
            tracked += 1
        else:
            reported += 1
        rows.append(entry)
    assert frozen == FROZEN_ROWS, "section 0.1: %d frozen rows, not %d" % (frozen, FROZEN_ROWS)
    assert tracked == TRACKED_ROWS, "section 0.1: %d tracked rows, not %d" % (tracked,
                                                                             TRACKED_ROWS)
    return {"revision": REQUIRED_REVISION, "anchors_matched": matched,
            "anchors_derived": derived, "rows": rows, "frozen": frozen, "tracked": tracked,
            "reported": reported}


def v8(before):
    """V8: the two frozen files this TZ leans on, byte-identical at run start and at run end.

    The expected values are the map's own `frozen` rows, read at run time, so the instrument
    carries no copy of a hash it is checking.
    """
    expected = {}
    for row in tz14.fingerprint_rows():
        if row["path"] in (PFAIR_PATH, TZ14_PATH):
            expected[row["path"]] = row["expected"]
    out = {}
    for path in (PFAIR_PATH, TZ14_PATH):
        after = _sha256_file(os.path.join(HERE, os.pardir, path))
        assert expected.get(path), "V8: the map has no frozen row for %s" % path
        assert before[path] == expected[path], "V8: %s was %s at run start" % (path,
                                                                              before[path])
        assert after == expected[path], "V8: %s is %s at run end" % (path, after)
        out[path] = {"expected": expected[path], "at_start": before[path], "at_end": after}
    return out


# ---- section 3.5: the exact tail of a sum of independent coins ---------------------

def pb_upper(weights):
    """`U(s) = P(S >= s)` for `s = 0 ... n`, exactly, over independent coins of known weights.

    One recursion: the mass of the count after each coin is the mass before it times `1 - w`
    plus the mass before it shifted by one, times `w`. All of it in `Decimal` at the 60 digits
    `pfair.py` sets on import. The caller hands the coins in ascending `T0`, so the result is
    identical on every run.
    """
    mass = [D(1)]
    for w in weights:
        keep = D(1) - w
        nxt = [D(0)] * (len(mass) + 1)
        for i, m in enumerate(mass):
            nxt[i] += m * keep
            nxt[i + 1] += m * w
        mass = nxt
    upper, total = [D(0)] * len(mass), D(0)
    for s in range(len(mass) - 1, -1, -1):
        total += mass[s]
        upper[s] = total
    return upper


def crit(weights, alpha):
    """The smallest `s` with `U(s) <= alpha`, and `U` at it. `n + 1` and `0` where none exists.

    `U` is non-increasing in `s`, so the first `s` that meets the bound is the smallest one.
    `s* = n + 1` is a count no outcome can reach, and the false-positive rate there is exactly
    zero rather than a number rounded to it.
    """
    upper = pb_upper(weights)
    n = len(weights)
    s_star = n + 1
    for s in range(n + 1):
        if upper[s] <= alpha:
            s_star = s
            break
    return s_star, (upper[s_star] if s_star <= n else D(0)), upper


# ---- section 3.4: the edges, the selection, and the isolation guard ----------------

def edges(p, ask_up, ask_dn):
    """The after-fee edge on each side, in exact `Decimal`. A side with no ask has no edge.

    `p` is `D(repr(row["p_t"]))` at the call site — the float's shortest representation, taken
    exactly, because `pfair.t_cdf` returns a float and no float enters a comparison here.
    """
    e_up = None if ask_up is None else p - ask_up - tz14.fee_pp(ask_up)
    e_dn = None if ask_dn is None else (D(1) - p) - ask_dn - tz14.fee_pp(ask_dn)
    return e_up, e_dn


def select(p, ask_up, ask_dn):
    """The trade taken where the larger existing edge is strictly positive; a tie goes to `Up`.

    Buying `Down` at its ask is the executable form of selling `Up`, and it is the trade used
    here because it is the trade a taker can place.
    """
    e_up, e_dn = edges(p, ask_up, ask_dn)
    out = {"e_up": e_up, "e_dn": e_dn, "selected": False, "side": None, "a": None, "q": None,
           "edge": None,
           "both_positive": (e_up is not None and e_dn is not None
                             and e_up > 0 and e_dn > 0)}
    existing = [e for e in (e_up, e_dn) if e is not None]
    if not existing or max(existing) <= 0:
        return out
    if e_up is not None and (e_dn is None or e_up >= e_dn):
        out.update({"selected": True, "side": tz14.UP, "a": ask_up, "q": p, "edge": e_up})
    else:
        out.update({"selected": True, "side": tz14.DOWN, "a": ask_dn, "q": D(1) - p,
                    "edge": e_dn})
    return out


def label_free(rows):
    """Section 2 items 5 and 7: every pricer row carries exactly the nine keys, `label` `None`.

    `tz11a.walk_member` computes `Y` and `r`, which are functions of the oracle after the
    checkpoint, and `tz11a.checkpoint_row` returns them. Neither is ever in a row this
    instrument keeps, and this raises if one appears.
    """
    for row in rows:
        assert set(row) == set(ROW_KEYS), \
            "section 2 item 7: a pricer row carries %r" % sorted(set(row) ^ set(ROW_KEYS))
        assert row["label"] is None, \
            "section 2 item 5: T0 %s tau %s carries a label" % (row.get("T0"), row.get("tau"))
    return len(rows)


# ---- section 4: the reading --------------------------------------------------------

def reading(n, S, s_star, power):
    """CANON PART II's rule with the polarity of Phase 2, in the order section 4 sets.

    EDGE is the null rejected beyond a critical count whose false-positive rate is exact, so it
    stands whatever the power; the power decides only between NO EDGE and UNDECIDABLE.
    """
    if n == 0:
        return "UNDECIDABLE"
    if S >= s_star:
        return "EDGE"
    return "NO EDGE" if (power if isinstance(power, type(D(0))) else D(str(power))) \
        >= POWER_FLOOR else "UNDECIDABLE"


# ---- section 5.2: the self-tests, seven items, before the capture is touched -------

def selftests():
    """Thirty-three assertions over seven items: 6, 3, 1, 3, 11, 4, 5.

    Every expectation is the Architect's, computed by an implementation that shares nothing
    with the code under test: items 1 to 4 in exact rationals, item 5 in exact decimal
    arithmetic, items 6 and 7 by construction from this TZ's own text.
    """
    lines, count = [], 0

    # 1. The exact tail against an independent enumeration of all sixteen outcomes:
    #    64/64, 61/64, 45/64, 19/64, 3/64, each a terminating decimal.
    u = pb_upper([D("0.25"), D("0.5"), D("0.75"), D("0.5")])
    assert len(u) == 5, "item 1: %d tails" % len(u)
    count += 1
    for s, want in enumerate(("1", "0.953125", "0.703125", "0.296875", "0.046875")):
        assert u[s] == D(want), "item 1: U(%d) is %s, not %s" % (s, u[s], want)
        count += 1
    lines.append("item 1: pb_upper over four coins gives 5 tails, "
                 + ", ".join(str(x) for x in u) + " — 6 assertions")

    # 2. The critical count against the binomial closed form, from `math.comb` in exact
    #    rationals: 1549/262144 and 5425/262144.
    half = [D("0.5")] * 20
    s2, fp2, u2 = crit(half, ALPHA)
    assert s2 == 16, "item 2: s* is %s" % s2
    assert fp2 == D("0.005908966064453125"), "item 2: FP is %s" % fp2
    assert u2[15] == D("0.020694732666015625"), "item 2: U(15) is %s" % u2[15]
    count += 3
    lines.append("item 2: twenty fair coins give s* = %d, FP = %s, U(15) = %s — 3 assertions"
                 % (s2, fp2, u2[15]))

    # 3. The power against the binomial closed form: 60047937765376 / 5^20, whose expansion
    #    terminates at the twentieth decimal.
    u3 = pb_upper([D("0.8")] * 20)
    assert u3[16] == D("0.62964826390266904576"), "item 3: U(16) is %s" % u3[16]
    count += 1
    lines.append("item 3: twenty coins at 0.8 give U(16) = %s — 1 assertion" % u3[16])

    # 4. The unreachable count: no `s` in 0 ... 3 meets the bound, so `s*` is `n + 1` and the
    #    false-positive rate is exactly zero.
    nine = [D("0.9")] * 3
    u4 = pb_upper(nine)
    s4, fp4, _ = crit(nine, ALPHA)
    assert u4[3] == D("0.729"), "item 4: U(3) is %s" % u4[3]
    assert s4 == 4, "item 4: s* is %s" % s4
    assert fp4 == D(0), "item 4: FP is %s" % fp4
    count += 3
    lines.append("item 4: three coins at 0.9 give U(3) = %s, s* = %d, FP = %s — 3 assertions"
                 % (u4[3], s4, fp4))

    # 5. Selection, exact, through `tz14.fee_pp`: fee(0.60) = fee(0.40) = 0.0168 and
    #    fee(0.41) = 0.016933, and every edge follows by subtraction.
    c1 = select(D("0.7"), D("0.60"), D("0.41"))
    assert c1["side"] == tz14.UP, "item 5 case 1: side %r" % c1["side"]
    assert c1["a"] == D("0.60"), "item 5 case 1: a %s" % c1["a"]
    assert c1["edge"] == D("0.0832"), "item 5 case 1: edge %s" % c1["edge"]
    c2 = select(D("0.605"), D("0.60"), D("0.41"))
    assert not c2["selected"], "item 5 case 2: selected"
    c3 = select(D("0.3"), D("0.41"), D("0.60"))
    assert c3["side"] == tz14.DOWN, "item 5 case 3: side %r" % c3["side"]
    assert c3["a"] == D("0.60"), "item 5 case 3: a %s" % c3["a"]
    assert c3["edge"] == D("0.0832"), "item 5 case 3: edge %s" % c3["edge"]
    c4 = select(D("0.7"), None, D("0.41"))
    assert not c4["selected"], "item 5 case 4: selected"
    c5 = select(D("0.5"), D("0.40"), D("0.40"))
    assert c5["both_positive"], "item 5 case 5: both edges are not positive"
    assert c5["side"] == tz14.UP, "item 5 case 5: side %r" % c5["side"]
    assert c5["edge"] == D("0.0832"), "item 5 case 5: edge %s" % c5["edge"]
    count += 11
    lines.append("item 5: five selections — Up at %s, nothing, Down at %s, nothing, Up on the "
                 "tie at %s — 11 assertions" % (c1["a"], c3["a"], c5["a"]))

    # 6. The isolation guard.
    good = [{k: (None if k == "label" else 0) for k in ROW_KEYS} for _ in range(2)]
    assert label_free(good) == 2, "item 6: the two clean rows did not pass"
    bad_label = dict(good[0])
    bad_label["label"] = 1
    bad_y = dict(good[0])
    bad_y["Y"] = 0.0
    bad_r = dict(good[0])
    bad_r["r"] = 0.0
    for name, row in (("a label", bad_label), ("the key Y", bad_y), ("the key r", bad_r)):
        try:
            label_free([row])
            raised = False
        except AssertionError:
            raised = True
        assert raised, "item 6: %s did not raise" % name
        count += 1
    count += 1
    lines.append("item 6: the guard passes two clean rows and raises on a label, on Y and on r "
                 "— 4 assertions")

    # 7. The reading rule, the power floor inclusive.
    cases = ((0, 0, 1, D("0"), "UNDECIDABLE"), (10, 8, 8, D("0.1"), "EDGE"),
             (10, 7, 8, D("0.85"), "NO EDGE"), (10, 7, 8, D("0.79"), "UNDECIDABLE"),
             (10, 7, 8, D("0.8"), "NO EDGE"))
    for n, S, s_star, power, want in cases:
        got = reading(n, S, s_star, power)
        assert got == want, "item 7: reading(%d, %d, %d, %s) is %s" % (n, S, s_star, power, got)
        count += 1
    lines.append("item 7: five readings, the 0.8 floor inclusive — 5 assertions")

    assert count == 33, "section 5.2: %d assertions, not 33" % count
    # Item 8 is a timing, not a test. Section 6's first fail-fast reads it.
    mark = time.perf_counter()
    pb_upper([T8_WEIGHT] * T8_WEIGHTS)
    t8 = time.perf_counter() - mark
    projected = RECURSION_UNITS * t8 / RECURSION_BASIS
    lines.append("item 8: one recursion over %d weights took %.4f s; the run projects %.1f s "
                 "of recursion against the %.0f s bound" % (T8_WEIGHTS, t8, projected,
                                                            RECURSION_LIMIT_S))
    if projected > RECURSION_LIMIT_S:
        raise SystemExit("BLOCKED at section 6: the recursions project %.1f s, above %.0f"
                         % (projected, RECURSION_LIMIT_S))
    return {"items": 7, "assertions": count, "lines": lines, "t8_s": t8,
            "projected_recursion_s": projected}


# ---- V2 and V6: the instrument's own syntax tree ------------------------------------

def _source():
    return open(os.path.abspath(__file__), encoding="utf-8").read()


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
    """`module.name` where a call's function is exactly that, else None."""
    func = node.func
    if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
        return func.value.id, func.attr
    return None


def v2_static():
    """V2's static half, over this instrument's own tree, before the capture is touched.

    The barred names are matched against `tz14.BANNED_SUBSTRINGS`, the committed tuple; this
    file writes none of the three itself, which is why the count below is zero by construction
    and not by a literal spelled here.
    """
    tree = ast.parse(_source())
    exempt = _docstring_nodes(tree)
    strings, carrying = 0, []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) \
                and id(node) not in exempt:
            strings += 1
            if any(bad in node.value for bad in tz14.BANNED_SUBSTRINGS):
                carrying.append(node.value)
    calls, probability, never, label_calls = 0, [], [], 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            calls += 1
            pair = _dotted(node)
            if pair and pair[0] == "pfair" and pair[1] in PFAIR_PROBABILITY:
                probability.append("%s.%s" % pair)
            if pair and pair in NEVER_CALLED:
                never.append("%s.%s" % pair)
            if pair and pair == LABEL_READER:
                label_calls += 1
    assert not carrying, "V2: %d string constants carry a barred name" % len(carrying)
    assert not probability, "V2: %r called" % probability
    assert not never, "V2: %r called" % never
    assert label_calls == 1, "V2: %d call sites of the label reader, not 1" % label_calls
    return {"strings_scanned": strings, "strings_carrying": len(carrying),
            "calls_scanned": calls, "pfair_probability_calls": len(probability),
            "never_called_calls": len(never), "label_reader_call_sites": label_calls,
            "docstrings_exempt": len(exempt)}


def v2_runtime(label_members):
    """V2's run-time half and V9's mode proof, from this instrument's own hook.

    Every open under the capture root is stamped with the step of section 5.1 it happened in.
    The settled document is opened by `analyze.venue` inside `tz06.qualification` at step 4 and
    by the one label read at step 10, and by nothing else in between.
    """
    banned = tz14.BANNED_SUBSTRINGS[0]
    per_step = collections.Counter()
    basenames = collections.Counter()
    modes = collections.Counter()
    reserved = []
    for path, mode, step in OPENS:
        base = os.path.basename(path)
        basenames[base] += 1
        modes[mode] += 1
        if banned in base:
            per_step[step] += 1
        parent = os.path.basename(os.path.dirname(path))
        if parent.isdigit() and int(parent) > RESERVED_AFTER and base != "manifest.json":
            reserved.append(path)
    write_modes = sorted(m for m in modes if any(c in m for c in "wxa+"))
    assert not write_modes, "V9: the capture was opened for writing: %r" % write_modes
    assert not reserved, "V9: %d opens in the reserved span: %r" % (len(reserved), reserved[:3])
    quiet = [s for s in ("5", "6", "7", "8", "9") if per_step.get(s)]
    assert not quiet, "V2: the settled document was opened at steps %r" % quiet
    if label_members is not None:
        assert per_step.get("10", 0) == label_members, \
            "V2: %d settled opens at step 10, not %d" % (per_step.get("10", 0), label_members)
    return {"opens_total": len(OPENS), "by_basename": dict(sorted(basenames.items())),
            "modes": dict(sorted(modes.items())), "write_modes": write_modes,
            "settled_opens_by_step": dict(sorted(per_step.items())),
            "settled_opens_steps_5_to_9": sum(per_step.get(s, 0)
                                              for s in ("5", "6", "7", "8", "9")),
            "opens_in_reserved_span": len(reserved),
            "label_members": label_members}


def git(*args):
    return subprocess.run(("git",) + args, cwd=HERE, capture_output=True,
                          text=True, check=True).stdout.strip()


def v6():
    """V6: the diff, this file's tree, and the three environment writes."""
    tree = ast.parse(_source())
    attribute_stores, globals_, nonlocals, environ = [], [], [], []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for t in targets:
                if isinstance(t, ast.Attribute):
                    attribute_stores.append(ast.dump(t))
                if isinstance(t, ast.Subscript) and isinstance(t.value, ast.Attribute) \
                        and isinstance(t.value.value, ast.Name) and t.value.value.id == "os" \
                        and t.value.attr == "environ":
                    environ.append(t.slice.value if isinstance(t.slice, ast.Constant) else "?")
        if isinstance(node, ast.Global):
            globals_.append(node.names)
        if isinstance(node, ast.Nonlocal):
            nonlocals.append(node.names)
    assert not attribute_stores, "V6: %d attribute stores" % len(attribute_stores)
    assert not globals_ and not nonlocals, "V6: global or nonlocal"
    assert sorted(environ) == ["MKL_NUM_THREADS", "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS"], \
        "V6: os.environ writes %r" % sorted(environ)
    head = git("rev-parse", "HEAD")
    base = git("merge-base", "HEAD", "origin/main")
    names = [n for n in git("diff", "--name-only", base, "HEAD").splitlines() if n]
    scoped = git("status", "--porcelain", "--", SELF_PATH,
                 "../CryptoReports/TZ-15-phase2-gate-report.md")
    # Section 5.3: the committed lines this change replaces, read from `origin/main`. The path
    # does not exist there, so the list is empty and the diff is additive in the strict sense.
    at_base = subprocess.run(("git", "show", "%s:%s" % (base, SELF_PATH)), cwd=HERE,
                             capture_output=True, text=True)
    replaced = [] if at_base.returncode != 0 else \
        [l for l in at_base.stdout.splitlines() if l not in set(_source().splitlines())]
    assert set(names) <= {SELF_PATH}, "V6: the diff names %r" % names
    assert not replaced, "V6: %d replaced lines" % len(replaced)
    return {"head": head, "merge_base": base, "diff_names": names, "status_porcelain": scoped,
            "replaced_lines": replaced, "attribute_stores": len(attribute_stores),
            "globals": len(globals_), "nonlocals": len(nonlocals),
            "environ_writes": sorted(environ), "path_at_merge_base": at_base.returncode == 0}


# ---- section 3.2: the pricer at each checkpoint ------------------------------------

def the_rows(members, manifests):
    """One pricer row per member per admitted `tau`, carrying the nine keys and nothing else.

    `walk_member`'s body and the calls inside it assert that the grid is whole and that every
    kept anchor has a mean. An `AssertionError` from it is BLOCKING: every member of this set
    was walked without one by committed code before, so a failure now means something under the
    pricer has changed.
    """
    rows = {}
    for t0 in members:
        try:
            walked = tz11a.walk_member(t0, manifests, False)
        except AssertionError as exc:
            raise SystemExit("BLOCKED at section 3.2: member %d: %s" % (t0, exc))
        for tau in ADMITTED:
            full = tz11a.checkpoint_row(t0, "tz14set", tau, walked[tau])
            rows[(t0, tau)] = {k: full[k] for k in ROW_KEYS}
    admissible = collections.Counter(tau for (_t0, tau), r in rows.items() if r["admissible"])
    for tau, want in ADMISSIBLE_EXPECTED:
        assert admissible[tau] == want, \
            "V4 (b): tau %d is admissible at %d checkpoints, not %d" % (tau, admissible[tau],
                                                                       want)
    return rows, {tau: admissible[tau] for tau in ADMITTED}


# ---- section 3.3: the quotes at each admitted checkpoint ---------------------------

def the_quotes(members, rows):
    """`ask5` and `bid5` of each side's reply, at each admitted checkpoint.

    The touch is `tz14.touch_of` on the venue's own minimum size and tick from the same reply,
    exactly as TZ-14 computed the touch it committed. A read that is not `200`, whose `book_of`
    result has `ok` false, whose book lacks `min_order_size` or `tick_size`, or that names a
    token outside the member's mapping is listed, counted and contributes no touch.
    """
    quotes, reads, skipped = {}, {}, []
    for t0 in members:
        docs = tz14.documents(t0)
        lines = tz14.quote_lines(config.interval_dir(t0))
        if not docs["usable"]:
            skipped.append({"T0": t0, "tau": None, "why": "market document: %s" % docs["why"]})
        for read in lines["reads"]:
            tau = read["tau"]
            if tau not in ADMITTED:
                continue
            key = (t0, tau)
            quotes.setdefault(key, {"ask_up": None, "bid_up": None,
                                    "ask_dn": None, "bid_dn": None})
            if read["status"] != 200 or not read["body_is_json"]:
                skipped.append({"T0": t0, "tau": tau, "why": "status %r" % read["status"]})
                continue
            book = tz14.book_of(read["raw"])
            if not book["ok"]:
                skipped.append({"T0": t0, "tau": tau, "why": "reply body is not an object"})
                continue
            if not book["min_order_size_present"] or not book["tick_size_present"]:
                skipped.append({"T0": t0, "tau": tau, "why": "the reply names no size or tick"})
                continue
            side = docs["tokens"].get(read["token_id"])
            if side is None:
                skipped.append({"T0": t0, "tau": tau, "why": "the token is outside the mapping"})
                continue
            touch = tz14.touch_of(book, D(str(book["min_order_size"])),
                                  D(str(book["tick_size"])))
            suffix = "up" if side == tz14.UP else "dn"
            quotes[key]["ask_" + suffix] = touch["ask5"]
            quotes[key]["bid_" + suffix] = touch["bid5"]
            reads[(t0, tau, read["token_id"])] = {
                "outcome": side, "bid5": touch["bid5"], "ask5": touch["ask5"],
                "sigma_hat": rows[key]["sigma_hat"], "admissible": rows[key]["admissible"]}
    for key in rows:
        quotes.setdefault(key, {"ask_up": None, "bid_up": None, "ask_dn": None, "bid_dn": None})
    return quotes, reads, skipped


# ---- section 3.4: eligibility, selection, and what the pricer claims ---------------

def the_trades(rows, quotes):
    """Per `(T0, tau)`: the edges, the selection, and every figure section 3.4 reports.

    Kept in records keyed by `(T0, tau)`, never in the pricer row.
    """
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
            rec.update({k: v for k, v in select(p, q["ask_up"], q["ask_dn"]).items()})
            if rec["selected"]:
                rec["fee"] = tz14.fee_pp(rec["a"])
        trades[key] = rec
    return trades


def label_free_report(trades, rows):
    """Section 3.4's report per `tau`, before any label exists."""
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
            p = D(repr(rows[(r["T0"], tau)]["p_t"]))
            mid = (r["bid_up"] + r["ask_up"]) / D(2)
            dev.append(p - mid)
            if abs(p - D("0.5")) < abs(mid - D("0.5")):
                confident += 1
        claim = [r["q"] - r["a"] for r in sel]
        after = [r["q"] - r["a"] - r["fee"] for r in sel]
        out[tau] = {
            "admissible": len(adm), "eligible": len(elig), "selected": n,
            "selected_up": sum(1 for r in sel if r["side"] == tz14.UP),
            "selected_down": sum(1 for r in sel if r["side"] == tz14.DOWN),
            "selected_weekend": sum(1 for r in sel if tz14.is_weekend(r["T0"])),
            "selected_weekday": sum(1 for r in sel if not tz14.is_weekend(r["T0"])),
            "both_edges_positive": sum(1 for r in recs if r["both_positive"]),
            "selected_at_or_below_0.10": sum(1 for r in sel if r["a"] <= LOW_PRICE),
            "q_price_paid": tz14.q_summary([r["a"] for r in sel]),
            "q_claimed_edge": tz14.q_summary(claim),
            "mean_claimed_edge": (sum(claim, D(0)) / n) if n else None,
            "mean_after_fee_claim": (sum(after, D(0)) / n) if n else None,
            "two_sided_up_books": len(two_sided),
            "q_p_minus_mid": tz14.q_summary(dev),
            "market_more_confident": confident,
            "market_more_confident_share": (D(confident) / D(len(two_sided)))
            if two_sided else None}
    return out


# ---- section 3.5: the gate's constants ---------------------------------------------

def constants(trades):
    """`s*`, `FP` and `POWER` per `tau`, exactly, from the market's prices and `p_t` alone.

    The coins are taken in ascending `T0`, so the recursion sees the same order on every run.
    """
    out = {}
    for tau in ADMITTED:
        sel = [t for (t0, tt), t in sorted(trades.items()) if tt == tau and t["selected"]]
        weights_a = [r["a"] for r in sel]
        weights_q = [r["q"] for r in sel]
        n = len(sel)
        s_star, fp, _u0 = crit(weights_a, ALPHA)
        u1 = pb_upper(weights_q)
        power = u1[s_star] if s_star <= n else D(0)
        out[tau] = {"n": n, "s_star": s_star, "FP": fp, "POWER": power,
                    "sum_a": sum(weights_a, D(0)), "sum_q": sum(weights_q, D(0)),
                    "sum_fee": sum((r["fee"] for r in sel), D(0)),
                    "members": [{"T0": r["T0"], "side": r["side"], "a": r["a"], "q": r["q"],
                                 "fee": r["fee"]} for r in sel]}
    return out


def projection(trades):
    """`s*` and `POWER` over the selected rows repeated two and three times.

    Barred from every reading. It is how much more capture a decision at an UNDECIDABLE `tau`
    would cost, and nothing else.
    """
    out = {}
    for tau in ADMITTED:
        sel = [t for (t0, tt), t in sorted(trades.items()) if tt == tau and t["selected"]]
        a = [r["a"] for r in sel]
        q = [r["q"] for r in sel]
        rows, reached = {}, None
        for k in PROJECTION_MULTIPLES:
            wa, wq = a * k, q * k
            nk = len(wa)
            s_k, fp_k, _ = crit(wa, ALPHA)
            u1 = pb_upper(wq)
            power_k = u1[s_k] if s_k <= nk else D(0)
            rows[k] = {"n": nk, "s_star": s_k, "FP": fp_k, "POWER": power_k}
            if reached is None and power_k >= POWER_FLOOR:
                reached = k
        out[tau] = {"multiples": rows, "smallest_k_at_power_floor": reached}
    return out


# ---- section 3.6: the labels, read once --------------------------------------------

def labels(trades, out_dir):
    """The one label read of this TZ, after the constants are on disk and `HEAD` is on `origin`.

    The push is asserted from `git rev-parse` and `git branch -r --contains`, each a fixed
    argument list with no shell, so no label is read by a commit that is not on `origin`.
    """
    head = git("rev-parse", "HEAD")
    branches = [b.strip() for b in git("branch", "-r", "--contains", head).splitlines()]
    branches = [b[2:] if b.startswith("* ") else b for b in branches]
    assert "origin/tz-15-phase2-gate" in branches, \
        "V5: HEAD %s is not on origin/tz-15-phase2-gate; it is on %r" % (head, branches)
    eligible = sorted({t0 for (t0, _tau), t in trades.items() if t["eligible"]})
    when = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    read = tz10b.m2_labels(sorted(eligible))
    line = {"utc": when, "head": head, "members": len(eligible),
            "member_list_sha256": tz07b.member_list_sha(eligible)}
    if not os.path.isdir(WORK_ROOT):
        os.makedirs(WORK_ROOT)
    with open(LEDGER_PATH, "at", encoding="utf-8") as fh:
        fh.write(json.dumps(line, sort_keys=True) + "\n")
    with open(LEDGER_PATH, encoding="utf-8") as fh:
        ledger = [l.rstrip("\n") for l in fh if l.strip()]
    return read, {"line": line, "ledger": ledger, "read_utc": when,
                  "branches_containing_head": branches, "out_dir": out_dir}


# ---- section 3.7: the observed statistic, influence and the diagnostics ------------

def observed(trades, consts, read):
    """`S` and everything that is a function of it, per `tau`, with section 4's reading."""
    out = {}
    for tau in ADMITTED:
        sel = [t for (t0, tt), t in sorted(trades.items()) if tt == tau and t["selected"]]
        n = len(sel)
        c = consts[tau]
        ys = []
        for r in sel:
            lab = read[r["T0"]]
            ys.append(lab if r["side"] == tz14.UP else 1 - lab)
        S = sum(ys)
        T = ((D(S) - c["sum_a"]) / D(n)) if n else None
        out[tau] = {
            "n": n, "S": S, "sum_a": c["sum_a"], "sum_q": c["sum_q"], "sum_fee": c["sum_fee"],
            "T": T, "T_fee": (T - c["sum_fee"] / D(n)) if n else None,
            "win_rate": (D(S) / D(n)) if n else None,
            "mean_price_paid": (c["sum_a"] / D(n)) if n else None,
            "mean_q": (c["sum_q"] / D(n)) if n else None,
            "s_star": c["s_star"], "FP": c["FP"], "POWER": c["POWER"],
            "reading": reading(n, S, c["s_star"], c["POWER"]),
            "y": ys, "T0": [r["T0"] for r in sel]}
    return out


def influence(trades, obs):
    """Section 3.7: the most influential selected member removed, and everything recomputed.

    Recorded beside the value section 4 reads, never in place of it. `T` is the mean of
    `x = y - a`, so the member removed is the one furthest from that mean.
    """
    out = {}
    for tau in ADMITTED:
        sel = [t for (t0, tt), t in sorted(trades.items()) if tt == tau and t["selected"]]
        o = obs[tau]
        if o["n"] < 2:
            out[tau] = {"defined": False, "why": "influence needs n >= 2; n is %d" % o["n"]}
            continue
        worst, worst_at = None, None
        for r, y in zip(sel, o["y"]):
            gap = abs((D(y) - r["a"]) - o["T"])
            if worst is None or gap > worst or (gap == worst and r["T0"] < worst_at["T0"]):
                worst, worst_at = gap, r
        kept = [(r, y) for r, y in zip(sel, o["y"]) if r["T0"] != worst_at["T0"]]
        n = len(kept)
        s_star, fp, _ = crit([r["a"] for r, _ in kept], ALPHA)
        u1 = pb_upper([r["q"] for r, _ in kept])
        power = u1[s_star] if s_star <= n else D(0)
        S = sum(y for _, y in kept)
        out[tau] = {"defined": True, "removed_T0": worst_at["T0"], "removed_side": worst_at["side"],
                    "removed_a": worst_at["a"], "gap": worst, "n": n, "S": S, "s_star": s_star,
                    "FP": fp, "POWER": power, "reading": reading(n, S, s_star, power)}
    return out


def diagnostics(trades, rows, read):
    """Barred from every reading. The mid against `p_t`, and the independence the gate assumes."""
    out = {}
    for tau in ADMITTED:
        recs = [t for (t0, tt), t in sorted(trades.items()) if tt == tau]
        two = [r for r in recs
               if r["eligible"] and r["bid_up"] is not None and r["ask_up"] is not None]
        doc = {"two_sided_up_books": len(two)}
        if two:
            mids = [(r["bid_up"] + r["ask_up"]) / D(2) for r in two]
            ps = [D(repr(rows[(r["T0"], tau)]["p_t"])) for r in two]
            labs = [D(read[r["T0"]]) for r in two]
            k = D(len(two))
            doc.update({"mean_label": sum(labs, D(0)) / k,
                        "mean_mid": sum(mids, D(0)) / k,
                        "mean_p_t": sum(ps, D(0)) / k,
                        "brier_mid": sum(((m - l) ** 2 for m, l in zip(mids, labs)), D(0)) / k,
                        "brier_p_t": sum(((p - l) ** 2 for p, l in zip(ps, labs)), D(0)) / k})
        else:
            for key in ("mean_label", "mean_mid", "mean_p_t", "brier_mid", "brier_p_t"):
                doc[key] = None
        sel = [r for r in recs if r["selected"]]
        ys = [read[r["T0"]] if r["side"] == tz14.UP else 1 - read[r["T0"]] for r in sel]
        if len(ys) >= 3 and len(set(ys)) > 1:
            mean = D(sum(ys)) / D(len(ys))
            num = sum(((D(ys[i]) - mean) * (D(ys[i - 1]) - mean) for i in range(1, len(ys))),
                      D(0))
            den = sum(((D(y) - mean) ** 2 for y in ys), D(0))
            doc["lag1_autocorrelation"] = num / den
            doc["autocorrelation_n"] = len(ys)
        else:
            doc["lag1_autocorrelation"] = None
            doc["autocorrelation_n"] = len(ys)
            doc["autocorrelation_why"] = ("needs three selected members and a y that is not "
                                          "constant; n is %d with %d distinct values"
                                          % (len(ys), len(set(ys))))
        out[tau] = doc
    return out


# ---- V4: the inputs are the committed ones -----------------------------------------

def v4_tz14(reads):
    """V4 (c): every admitted read against TZ-14's own observations file, cell by cell."""
    found = []
    for name in sorted(os.listdir(TZ14_WORK)):
        path = os.path.join(TZ14_WORK, name, "observations.csv")
        if os.path.isfile(path) and _sha256_file(path) == TZ14_OBS_SHA256:
            found.append(path)
    assert found, "V4 (c): no file under %s hashes to %s" % (TZ14_WORK, TZ14_OBS_SHA256)
    path = found[0]
    with open(path, encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split(",")
        idx = {name: i for i, name in enumerate(header)}
        agreed, compared, disagreed = 0, 0, []
        for line in fh:
            cells = line.rstrip("\n").split(",")
            t0, tau = int(cells[idx["T0"]]), int(cells[idx["tau"]])
            if tau not in ADMITTED:
                continue
            key = (t0, tau, cells[idx["token_id"]])
            mine = reads.get(key)
            compared += 1
            if mine is None:
                disagreed.append({"key": key, "field": "the read itself", "theirs": "present",
                                  "mine": "absent"})
                continue
            ok = True
            for field in ("outcome", "bid5", "ask5", "sigma_hat", "admissible"):
                theirs = cells[idx[field]]
                ours = tz14.cell(mine[field])
                if theirs != ours:
                    ok = False
                    disagreed.append({"key": key, "field": field, "theirs": theirs,
                                      "mine": ours})
            agreed += 1 if ok else 0
    assert compared == ADMITTED_READS, \
        "V4 (c): %d admitted reads in TZ-14's file, not %d" % (compared, ADMITTED_READS)
    assert not disagreed, "V4 (c): %d cells differ: %r" % (len(disagreed), disagreed[:3])
    return {"path": path, "copies_found": len(found), "sha256": TZ14_OBS_SHA256,
            "compared": compared, "agreed": agreed, "disagreed": len(disagreed),
            "fields": ["outcome", "bid5", "ask5", "sigma_hat", "admissible"]}


def v4_tz13(members, rows, read):
    """V4 (d): `p_t` and the label against what TZ-13 computed on the overlapping members."""
    have = _sha256_file(TZ13_OBS_PATH)
    assert have == TZ13_OBS_SHA256, "V4 (d): %s hashes to %s" % (TZ13_OBS_PATH, have)
    theirs = {}
    seen = set()
    with open(TZ13_OBS_PATH, encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split(",")
        idx = {name: i for i, name in enumerate(header)}
        for line in fh:
            cells = line.rstrip("\n").split(",")
            t0, tau = int(cells[idx["T0"]]), int(cells[idx["tau"]])
            if t0 <= SET_LAST_MEMBER:
                seen.add(t0)
            if tau in ADMITTED:
                theirs[(t0, tau)] = (cells[idx["p_t"]], cells[idx["label"]])
    overlap = sorted(t0 for t0 in members if t0 >= TZ13_FIRST_T0)
    assert seen == set(overlap), \
        "V4 (d): TZ-13 names %d members at or below %d; this set has %d at or above %d" \
        % (len(seen), SET_LAST_MEMBER, len(overlap), TZ13_FIRST_T0)
    p_ok, lab_ok, lab_seen, bad = 0, 0, 0, []
    for t0 in overlap:
        for tau in ADMITTED:
            cell_p, cell_l = theirs[(t0, tau)]
            if repr(rows[(t0, tau)]["p_t"]) == cell_p:
                p_ok += 1
            else:
                bad.append({"T0": t0, "tau": tau, "field": "p_t", "theirs": cell_p,
                            "mine": repr(rows[(t0, tau)]["p_t"])})
            if read is not None and t0 in read:
                lab_seen += 1
                if tz14.cell(read[t0]) == cell_l:
                    lab_ok += 1
                else:
                    bad.append({"T0": t0, "tau": tau, "field": "label", "theirs": cell_l,
                                "mine": tz14.cell(read[t0])})
    assert not bad, "V4 (d): %d cells differ: %r" % (len(bad), bad[:3])
    return {"path": TZ13_OBS_PATH, "sha256": have, "overlap_members": len(overlap),
            "first_overlap": overlap[0] if overlap else None,
            "p_t_compared": p_ok, "labels_compared": lab_seen, "labels_agreed": lab_ok,
            "disagreed": len(bad)}


# ---- section 3.8: the pre-registered predictions ------------------------------------

def predictions(free, obs):
    """Five, written before any quote had been put beside a price. Barred from every gate."""
    out = []
    p1 = all(free[tau]["eligible"] == free[tau]["admissible"] for tau in ADMITTED)
    out.append({"id": "P1", "claim": "the eligible count equals the admissible count at every "
                "tau in ADMITTED", "held": p1,
                "observed": ", ".join("%d: %d of %d" % (tau, free[tau]["eligible"],
                                                        free[tau]["admissible"])
                                      for tau in ADMITTED)})
    low, n60 = free[60]["selected_at_or_below_0.10"], free[60]["selected"]
    out.append({"id": "P2", "claim": "at tau = 60 more than half of the selected trades are "
                "priced at or below 0.10", "held": bool(n60) and low * 2 > n60,
                "observed": "%d of %d selected at 60 are at or below 0.10" % (low, n60)})
    if obs is None:
        for pid, claim in (("P3", "at tau = 60 the selected trades win less often than their "
                            "prices implied: S < sum a"),
                           ("P4", "no tau reads EDGE"),
                           ("P5", "at least one tau reads NO EDGE")):
            out.append({"id": pid, "claim": claim, "held": None,
                        "observed": "no label was read in this run"})
        return out
    o60 = obs[60]
    out.append({"id": "P3", "claim": "at tau = 60 the selected trades win less often than "
                "their prices implied: S < sum a",
                "held": bool(o60["n"]) and D(o60["S"]) < o60["sum_a"],
                "observed": "S = %d against sum a = %s" % (o60["S"], o60["sum_a"])})
    readings = {tau: obs[tau]["reading"] for tau in ADMITTED}
    out.append({"id": "P4", "claim": "no tau reads EDGE",
                "held": not any(r == "EDGE" for r in readings.values()),
                "observed": ", ".join("%d: %s" % (t, readings[t]) for t in ADMITTED)})
    out.append({"id": "P5", "claim": "at least one tau reads NO EDGE",
                "held": any(r == "NO EDGE" for r in readings.values()),
                "observed": ", ".join("%d: %s" % (t, readings[t]) for t in ADMITTED)})
    return out


def verdict(obs):
    """Section 4's verdict over the five `tau`, and the family bound."""
    readings = {tau: obs[tau]["reading"] for tau in ADMITTED}
    edge = [t for t in ADMITTED if readings[t] == "EDGE"]
    no_edge = [t for t in ADMITTED if readings[t] == "NO EDGE"]
    undecided = [t for t in ADMITTED if readings[t] == "UNDECIDABLE"]
    if edge:
        line = ("Phase 2 reads YES at tau %s, subject to confirmation on the reserved span. "
                "Phase 3 does not open on it." % ", ".join(str(t) for t in edge))
    elif len(no_edge) == len(ADMITTED):
        line = ("Phase 2 reads NO for the Student pricer, inside its domain, at all five tau. "
                "It says nothing about any other pricer.")
    else:
        line = ("The tau that read NO EDGE are closed: %s. Each UNDECIDABLE tau carries the "
                "projection's multiple: %s."
                % (", ".join(str(t) for t in no_edge) or "none",
                   ", ".join(str(t) for t in undecided) or "none"))
    return {"readings": readings, "EDGE": edge, "NO_EDGE": no_edge, "UNDECIDABLE": undecided,
            "verdict": line,
            "family_FP_sum": sum((obs[t]["FP"] for t in ADMITTED), D(0))}


# ---- section 0.5, section 0.6 and section 0.7: the recorded reads -------------------

def refs():
    """Section 0.6: every ref on `origin`, read before the branch of section 2 exists."""
    out = subprocess.run(("git", "ls-remote", "origin"), cwd=HERE, capture_output=True,
                         text=True)
    return {"returncode": out.returncode, "refs": [l for l in out.stdout.splitlines() if l]}


def trees():
    """Section 0.7: TZ-13's tree is gone and TZ-14's is still here for V4 (c)."""
    tz13 = os.path.exists("/root/tz13-work")
    tz14dir = os.path.isdir(TZ14_WORK)
    assert not tz13, "section 0.7: /root/tz13-work still exists"
    assert tz14dir, "section 0.7: %s does not exist; V4 (c) reads a file from it" % TZ14_WORK
    return {"/root/tz13-work": "absent", TZ14_WORK: "present",
            "tz14_entries": sorted(os.listdir(TZ14_WORK))}


# ---- the run ------------------------------------------------------------------------

def build(score, out_dir):
    """The fixed order of section 5.1, asserted step by step."""
    started = time.perf_counter()
    marks, steps = {}, []

    def mark(name):
        steps.append("%s at %.1f s" % (name, time.perf_counter() - started))
        marks[name] = time.perf_counter() - started

    _step("0")
    before = {p: _sha256_file(os.path.join(HERE, os.pardir, p))
              for p in (PFAIR_PATH, TZ14_PATH)}
    gates = v1_gates()
    tree_doc = trees()
    ref_doc = refs()
    mark("0 gates")

    _step("1")
    listing_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    host1 = tz11a.host_read("start", set(), tz11a.FLOOR_START_BYTES)
    host1["listing_utc"] = listing_at
    host1["bound"] = tz11a.FLOOR_START_BYTES
    host1["asserted"] = True
    names = sorted(int(n) for n in os.listdir(os.path.join(config.ROOT, config.SERIES)))
    host1["first_T0"], host1["last_T0"] = names[0], names[-1]
    total = os.statvfs("/")
    host1["filesystem_total_bytes"] = total.f_blocks * total.f_frsize
    mark("1 host read 1")

    _step("2")
    tests = selftests()
    mark("2 self-tests")

    _step("3")
    diff = v6()
    static = v2_static()
    mark("3 v6 and v2 static")

    _step("4")
    manifests = load_manifests()
    rows_considered, members, set_doc = tz14.the_set(manifests)
    sha = tz07b.member_list_sha(members)
    assert sha == SET_SHA256, "V4 (a): the set hashes to %s" % sha
    assert len(rows_considered) == SET_UNITS, \
        "V4 (a): %d units considered, not %d" % (len(rows_considered), SET_UNITS)
    assert max(members) <= SET_LAST_MEMBER, \
        "V4 (a): the last member is %d, above %d" % (max(members), SET_LAST_MEMBER)
    mark("4 the set")

    _step("5")
    rows, admissible = the_rows(members, manifests)
    host2 = tz11a.host_read("after the rows", set(members), tz11a.FLOOR_BYTES)
    host2["bound"] = tz11a.FLOOR_BYTES
    host2["asserted"] = True
    elapsed = time.perf_counter() - started
    if elapsed > ROWS_LIMIT_S:
        raise SystemExit("BLOCKED at section 6: %.1f s elapsed after section 3.2, above %.0f"
                         % (elapsed, ROWS_LIMIT_S))
    mark("5 the rows and host read 2")

    _step("6")
    quotes, reads, skipped = the_quotes(members, rows)
    v4c = v4_tz14(reads)
    mark("6 the quotes and V4 (c)")

    _step("7")
    trades = the_trades(rows, quotes)
    free = label_free_report(trades, rows)
    kept_rows = label_free(list(rows.values()))
    mark("7 selection and the first label-free assertion")

    _step("8")
    consts = constants(trades)
    proj = projection(trades)
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    constants_text = json.dumps(
        {"ADMITTED": list(ADMITTED), "alpha": str(ALPHA), "power_floor": str(POWER_FLOOR),
         "set_sha256": sha, "members": len(members),
         "per_tau": {str(tau): {"n": consts[tau]["n"], "s_star": consts[tau]["s_star"],
                                "FP": str(consts[tau]["FP"]),
                                "POWER": str(consts[tau]["POWER"]),
                                "sum_a": str(consts[tau]["sum_a"]),
                                "sum_q": str(consts[tau]["sum_q"]),
                                "sum_fee": str(consts[tau]["sum_fee"]),
                                "projection": {str(k): {"n": v["n"], "s_star": v["s_star"],
                                                        "FP": str(v["FP"]),
                                                        "POWER": str(v["POWER"])}
                                               for k, v in proj[tau]["multiples"].items()},
                                "smallest_k_at_power_floor":
                                    proj[tau]["smallest_k_at_power_floor"],
                                "selected": [{"T0": m["T0"], "side": m["side"],
                                              "a": str(m["a"]), "q": str(m["q"]),
                                              "fee": str(m["fee"])}
                                             for m in consts[tau]["members"]]}
                     for tau in ADMITTED}},
        indent=2, sort_keys=True) + "\n"
    with open(os.path.join(out_dir, "tz15-constants.json"), "wt", encoding="utf-8") as fh:
        fh.write(constants_text)
    constants_written = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    label_free(list(rows.values()))
    mark("8 the constants and the second label-free assertion")

    doc = {"gates": gates, "trees": tree_doc, "refs": ref_doc, "host": [host1, host2],
           "selftests": tests, "v6": diff, "v2_static": static, "set": set_doc,
           "admissible": admissible, "quotes_skipped": skipped, "free": free,
           "constants": consts, "projection": proj, "rows_checked": kept_rows,
           "v4_tz14": v4c, "constants_written_utc": constants_written,
           "members": members, "trades": trades, "rows": rows, "score": score,
           "constants_text_sha256": hashlib.sha256(constants_text.encode("utf-8")).hexdigest()}

    if not score:
        _step("9")
        host3 = tz11a.host_read("end", set(members), tz11a.FLOOR_BYTES)
        host3["bound"] = tz11a.FLOOR_BYTES
        host3["asserted"] = True
        doc["host"].append(host3)
        doc["v2_runtime"] = v2_runtime(None)
        doc["v8"] = v8(before)
        doc["v9"] = v9_doc(doc["host"], out_dir)
        doc["observed"] = None
        doc["predictions"] = predictions(free, None)
        doc["elapsed_s"] = time.perf_counter() - started
        doc["steps"], doc["marks"] = steps, marks
        mark("9 host read 3 and V9")
        doc["peak_rss_kb"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        return doc

    _step("10")
    read, ledger = labels(trades, out_dir)
    doc["labels"] = ledger
    mark("10 the label read")

    _step("11")
    obs = observed(trades, consts, read)
    doc["observed"] = obs
    doc["influence"] = influence(trades, obs)
    doc["diagnostics"] = diagnostics(trades, rows, read)
    doc["verdict"] = verdict(obs)
    doc["predictions"] = predictions(free, obs)
    doc["label_read"] = read
    mark("11 the statistic, the readings and the verdict")

    _step("12")
    doc["v4_tz13"] = v4_tz13(members, rows, read)
    mark("12 V4 (d)")

    _step("13")
    host3 = tz11a.host_read("end", set(members), tz11a.FLOOR_BYTES)
    host3["bound"] = tz11a.FLOOR_BYTES
    host3["asserted"] = True
    doc["host"].append(host3)
    doc["v2_runtime"] = v2_runtime(ledger["line"]["members"])
    doc["v8"] = v8(before)
    doc["v9"] = v9_doc(doc["host"], out_dir)
    doc["elapsed_s"] = time.perf_counter() - started
    doc["steps"], doc["marks"] = steps, marks
    mark("13 host read 3, V9 and the files")
    doc["peak_rss_kb"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return doc


def v9_doc(host, out_dir):
    """V9: the capture is untouched, and everything this instrument can write, enumerated."""
    first, last = host[0], host[-1]
    assert first["recorder_pids"] == last["recorder_pids"], \
        "V9: the recorder pids moved from %r to %r" % (first["recorder_pids"],
                                                       last["recorder_pids"])
    assert first["newest_start_sha"] == last["newest_start_sha"], "V9: the start record moved"
    assert first["newest_start_recv_ns"] == last["newest_start_recv_ns"], \
        "V9: the start record's recv_ns moved"
    assert last["interval_directories"] >= first["interval_directories"], \
        "V9: the directory count fell from %d to %d" % (first["interval_directories"],
                                                        last["interval_directories"])
    assert host[1]["read_set_sha256"] == last["read_set_sha256"], \
        "V9: the read set moved between reads 2 and 3"
    return {"pid_unchanged": True, "start_record_unchanged": True,
            "directories": [h["interval_directories"] for h in host],
            "read_set_sha256": host[1]["read_set_sha256"],
            "writable": sorted([os.path.join(out_dir, n) for n in OUT_NAMES] + [LEDGER_PATH])}


# ---- the files ----------------------------------------------------------------------

def _s(value, places=None):
    if value is None:
        return "—"
    if places is None:
        return str(value)
    return str(value.quantize(D(1).scaleb(-places))) if hasattr(value, "quantize") \
        else ("%.*f" % (places, value))


def csv_text(doc):
    """V11: one row per member per `tau` in `ADMITTED` — 6,000 rows and a header.

    Sufficient to reconstruct every number of sections 3.4, 3.5 and 3.7 without re-running.
    """
    read = doc.get("label_read") or {}
    head = ["T0", "tau", "sigma_hat", "admissible", "p_t", "ask_up", "bid_up", "ask_dn",
            "bid_dn", "e_up", "e_dn", "selected", "side", "a", "q", "fee", "label", "y"]
    out = [",".join(head)]
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
    """V11: the units considered, and the eligible and selected lists per `tau`."""
    out = ["# TZ-15 — disclosure", "",
           "## Units considered, ascending `T0`", "",
           "| `T0` | UTC | weekday | member | reasons |", "|---|---|---|---|---|"]
    members = set(doc["members"])
    non = {r["T0"]: r["reasons"] for r in doc["set"]["non_members"]}
    for t0 in sorted(set(doc["members"]) | set(non)):
        out.append("| %d | %s | %s | %s | %s |"
                   % (t0, tz14.utc(t0), tz14.weekday_of(t0),
                      "yes" if t0 in members else "no",
                      ", ".join(non.get(t0, [])) or "—"))
    for tau in ADMITTED:
        for kind in ("eligible", "selected"):
            lst = sorted(t["T0"] for (t0, tt), t in doc["trades"].items()
                         if tt == tau and t[kind])
            out += ["", "## tau %d — %s: %d members" % (tau, kind, len(lst)), "",
                    "`tz07b.member_list_sha` = `%s`" % tz07b.member_list_sha(lst), "",
                    "```", ", ".join(str(t) for t in lst) or "(none)", "```"]
    return "\n".join(out) + "\n"


def tables(doc):
    """Section 3.4, section 3.5, section 3.7 and section 4, as the report prints them."""
    free, consts, proj = doc["free"], doc["constants"], doc["projection"]
    obs = doc["observed"]
    out = ["# TZ-15 — the Phase 2 gate", "",
           "## Section 3.4 — the label-free report, per `tau`", "",
           "| `tau` | admissible | eligible | selected | Up | Down | weekday | weekend | "
           "both edges positive | at or below 0.10 |", "|---|---|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        f = free[tau]
        out.append("| %d | %d | %d | %d | %d | %d | %d | %d | %d | %d |"
                   % (tau, f["admissible"], f["eligible"], f["selected"], f["selected_up"],
                      f["selected_down"], f["selected_weekday"], f["selected_weekend"],
                      f["both_edges_positive"], f["selected_at_or_below_0.10"]))
    out += ["", "**The price paid and the edge `p_t` claims, over the selected members**", "",
            "| `tau` | `n` | mean `a` | mean `q - a` | mean after fee | min `a` | median `a` | "
            "max `a` |", "|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        f, q = free[tau], free[tau]["q_price_paid"]
        mean_a = (consts[tau]["sum_a"] / D(f["selected"])) if f["selected"] else None
        out.append("| %d | %d | %s | %s | %s | %s | %s | %s |"
                   % (tau, f["selected"], _s(mean_a, 6),
                      _s(f["mean_claimed_edge"], 6), _s(f["mean_after_fee_claim"], 6),
                      _s(q["min"]), _s(q["0.50"]), _s(q["max"])))
    out += ["", "**The market's mid against `p_t`, over the eligible two-sided Up books**", "",
            "| `tau` | books | min `D` | 0.25 | median | 0.75 | max | market more confident |",
            "|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        f, q = free[tau], free[tau]["q_p_minus_mid"]
        share = f["market_more_confident_share"]
        out.append("| %d | %d | %s | %s | %s | %s | %s | %d (%s) |"
                   % (tau, f["two_sided_up_books"], _s(q["min"]), _s(q["0.25"]), _s(q["0.50"]),
                      _s(q["0.75"]), _s(q["max"]), f["market_more_confident"],
                      _s(share, 4) if share is not None else "—"))
    out += ["", "## Section 3.5 — the gate's constants, exact, before any label", "",
            "| `tau` | `n` | `s*` | `FP` | `POWER` | `k = 2` `s*` / `POWER` | "
            "`k = 3` `s*` / `POWER` | smallest `k` at 0.8 |",
            "|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        c, p = consts[tau], proj[tau]
        out.append("| %d | %d | %s | %s | %s | %s / %s | %s / %s | %s |"
                   % (tau, c["n"], c["s_star"], _s(c["FP"], 12), _s(c["POWER"], 6),
                      p["multiples"][2]["s_star"], _s(p["multiples"][2]["POWER"], 6),
                      p["multiples"][3]["s_star"], _s(p["multiples"][3]["POWER"], 6),
                      p["smallest_k_at_power_floor"] or "none"))
    if obs is None:
        out += ["", "**No label was read in this run.** It stopped after section 3.5 with its "
                "constants on disk.", ""]
        return "\n".join(out) + "\n"
    out += ["", "## Section 3.7 and section 4 — the observed statistic and the reading", "",
            "| `tau` | `n` | `S` | `s*` | `sum a` | win rate | mean `a` | mean `q` | `T` | "
            "`T_fee` | `FP` | `POWER` | **reading** |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        o = obs[tau]
        out.append("| %d | %d | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | **%s** |"
                   % (tau, o["n"], o["S"], o["s_star"], _s(o["sum_a"], 4),
                      _s(o["win_rate"], 6), _s(o["mean_price_paid"], 6), _s(o["mean_q"], 6),
                      _s(o["T"], 6), _s(o["T_fee"], 6), _s(o["FP"], 12), _s(o["POWER"], 6),
                      o["reading"]))
    out += ["", "**The family bound.** `FP` sums to %s over the five `tau`; Bonferroni puts the "
            "probability of EDGE anywhere under the null at most there, whatever the "
            "dependence." % _s(doc["verdict"]["family_FP_sum"], 12),
            "", "**The verdict.** " + doc["verdict"]["verdict"], "",
            "## Section 3.7 — influence, recorded, not a reading", "",
            "| `tau` | removed `T0` | side | `a` | `n - 1` | `S` | `s*` | `POWER` | reading |",
            "|---|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        i = doc["influence"][tau]
        if not i["defined"]:
            out.append("| %d | — | — | — | — | — | — | — | undefined: %s |" % (tau, i["why"]))
            continue
        out.append("| %d | %d | %s | %s | %d | %d | %s | %s | %s |"
                   % (tau, i["removed_T0"], i["removed_side"], _s(i["removed_a"]), i["n"],
                      i["S"], i["s_star"], _s(i["POWER"], 6), i["reading"]))
    out += ["", "## Section 3.7 — diagnostics, barred from every reading", "",
            "| `tau` | two-sided books | mean label | mean mid | mean `p_t` | Brier mid | "
            "Brier `p_t` | lag-1 autocorrelation of `y` |",
            "|---|---|---|---|---|---|---|---|"]
    for tau in ADMITTED:
        d = doc["diagnostics"][tau]
        out.append("| %d | %d | %s | %s | %s | %s | %s | %s |"
                   % (tau, d["two_sided_up_books"], _s(d["mean_label"], 6), _s(d["mean_mid"], 6),
                      _s(d["mean_p_t"], 6), _s(d["brier_mid"], 6), _s(d["brier_p_t"], 6),
                      _s(d["lag1_autocorrelation"], 6)))
    out += ["", "## Section 3.8 — the five pre-registered predictions", "",
            "| # | prediction | observed | verdict |", "|---|---|---|---|"]
    for p in doc["predictions"]:
        out.append("| %s | %s | %s | **%s** |"
                   % (p["id"], p["claim"], p["observed"],
                      "held" if p["held"] else ("refuted" if p["held"] is False else "—")))
    out.append("")
    return "\n".join(out) + "\n"


def readings_text(doc):
    """V3's deterministic record of everything section 3.7 and section 4 produced."""
    obs = doc["observed"]
    body = {"ADMITTED": list(ADMITTED), "label_free": doc["free"], "admissible": doc["admissible"],
            "predictions": doc["predictions"], "score": doc["score"],
            "set_sha256": doc["set"]["sha256"], "units_considered": doc["set"]["considered"]}
    if obs is not None:
        body["observed"] = {str(t): {k: v for k, v in obs[t].items() if k not in ("y", "T0")}
                            for t in ADMITTED}
        body["y_sum"] = {str(t): obs[t]["S"] for t in ADMITTED}
        body["influence"] = {str(t): doc["influence"][t] for t in ADMITTED}
        body["diagnostics"] = {str(t): doc["diagnostics"][t] for t in ADMITTED}
        body["verdict"] = doc["verdict"]
        body["v4_tz13"] = doc["v4_tz13"]
    return json.dumps(body, indent=2, sort_keys=True, default=str) + "\n"


def main():
    args = [a for a in sys.argv[1:]]
    score = "--score" in args
    rest = [a for a in args if a != "--score"]
    out_dir = rest[0] if rest else os.path.join(WORK_ROOT, "out")
    doc = build(score, out_dir)
    deterministic = {"tz15-tables.md": tables(doc),
                     "tz15-observations.csv": csv_text(doc),
                     "tz15-disclosure.md": disclosure_text(doc),
                     "tz15-readings.json": readings_text(doc)}
    for name, text in sorted(deterministic.items()):
        with open(os.path.join(out_dir, name), "wt", encoding="utf-8") as fh:
            fh.write(text)
    run = {"host": doc["host"], "steps": doc["steps"], "marks": doc["marks"],
           "elapsed_s": doc["elapsed_s"], "peak_rss_kb": doc["peak_rss_kb"],
           "gates": doc["gates"], "trees": doc["trees"], "refs": doc["refs"],
           "selftests": doc["selftests"], "v6": doc["v6"], "v2_static": doc["v2_static"],
           "v2_runtime": doc["v2_runtime"], "v8": doc["v8"], "v9": doc["v9"],
           "v4_tz14": doc["v4_tz14"], "v4_tz13": doc.get("v4_tz13"),
           "labels": doc.get("labels"), "quotes_skipped": doc["quotes_skipped"],
           "rows_checked": doc["rows_checked"], "score": doc["score"],
           "constants_written_utc": doc["constants_written_utc"],
           "constants_text_sha256": doc["constants_text_sha256"],
           "python": sys.version, "interpreter": sys.executable,
           "sha256": {name: hashlib.sha256(text.encode("utf-8")).hexdigest()
                      for name, text in sorted(deterministic.items())}}
    with open(os.path.join(out_dir, "tz15-run.json"), "wt", encoding="utf-8") as fh:
        fh.write(json.dumps(run, indent=2, sort_keys=True, default=str) + "\n")
    sys.stdout.write("%s  tz15-constants.json\n" % doc["constants_text_sha256"])
    for name in sorted(deterministic):
        sys.stdout.write("%s  %s\n" % (run["sha256"][name], name))
    for line in doc["steps"]:
        sys.stdout.write("step %s\n" % line)
    sys.stdout.write("elapsed %.1f s, peak RSS %d kB\n"
                     % (doc["elapsed_s"], doc["peak_rss_kb"]))


if __name__ == "__main__":
    main()
