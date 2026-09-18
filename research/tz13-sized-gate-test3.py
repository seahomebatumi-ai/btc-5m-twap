"""TZ-13 — the sized gate on test 3.

TZ-12 measured, from the frozen pricer's own predictions, the false-failure probability and the
power of each of G1 … G4. This file applies that gate, once, to test 3 — the first 750 qualifying
slots after `1789427700` — a set no one has scored and whose outcomes no one has read.

Nothing is fitted here. `SD_SCALE`, `corrected_sd`, `ADMIT`, `LINK_NU`, `LINK_SCALE` and
`SIGMA_LOG_NU` are read from the committed files and never recomputed as constants. Every
threshold this file applies is read at run time from `research/pfair.py`, `research/tz11a-
student-link.py` or `research/tz12-sized-gate.py`; §4 of the TZ names no threshold as a literal
and neither does this file.

The order of a full run is fixed by §5.1 and asserted by `build`:

    1  host read 1, at the start floor
    2  the six self-tests of §5.2
    3  `v6` and the static half of `v2_static`
    4  the three committed sets and test 3, with every assertion of §3.1
    5  the walk and the guarded pass; host read 2
    6  the domain
    7  all 5,250 rows carry `label is None`
    8  `tz12.constants` for the seven tau, written to disk
    9  the same assertion again, over the same rows
   10  §3.6's projection — still free of any outcome
   11  `tz10b.m2_labels` — the first outcome read of the run
   12  the observed statistics, the readings, `tz12.verdict`, §4.3's weakening, the influence
   13  host read 3, and V9's four assertions between read 1 and read 3

The answer this instrument can give is per `tau`: NOT DISQUALIFIED, DISQUALIFIED or UNDECIDABLE.
It cannot confirm an edge — Phase 1 can only disqualify — and a `tau` that survives is admitted
to Phase 2 and to nothing else.
"""

import os                                                                  # noqa: E402

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import ast                                                                 # noqa: E402
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


def _load(name, filename):
    """Import a module whose filename carries a hyphen, so it cannot be `import`ed by name."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Section 5.1: TZ-12's instrument loads TZ-11a's, which loads TZ-10b's, which loads the other
# four. Every committed module comes through that one object; loading any of them a second time
# would be two module objects with two copies of every table.
tz12 = _load("tz12sizedgate", "tz12-sized-gate.py")
tz11a = tz12.tz11a
tz10b = tz12.tz10b
tz08a = tz12.tz08a
tz07b = tz12.tz07b
tz07a = tz12.tz07a
tz06 = tz12.tz06
pfair = tz12.pfair
D = pfair.D
config = pfair.config
load_manifests = tz12.load_manifests

# Section 3.1: test 3 is the first `TEST3_NEED` qualifying slots strictly after `TEST3_AFTER`.
# `TEST3_AFTER` is map §2.3's last unit of test 2; `FIRST_400` is §3.1 item 3's superset check.
TEST3_NEED = 750
TEST3_AFTER = 1789427700
FIRST_400 = 400
TEST3_ROWS = TEST3_NEED * len(pfair.TAUS)
SET_NAME = "test3"
SET_LABEL = "test 3 (first 750 after 1789427700)"

# Section 3.2: the guarded sample, three lists of this many before the union.
GUARD_HEAD = 25
GUARD_TAIL = 25
GUARD_EXCLUDED = 25

# Section 3.6: the projection's multiples, and the key each repeated row carries.
PROJECTION_MULTIPLES = (1, 2, 3)

# Section 4.3: the straddle rule. `1.96` is the two-sided normal 95% point the TZ writes; the
# half-width at `P = 0.5` is the Architect's literal, checked in §5.2 item 1 to a relative 1e-12.
STRADDLE_Z = 1.96
STRADDLE_HALF_WIDTH = 0.021913466179498
CONSTANT_REL_TOL = 1e-12
POWER_REL_TOL = 1e-9

# Section 5.2 item 4: the Student CDF at nu 1 and 2, from closed forms that use no incomplete
# beta and no normal quadrature — computed by the Architect at 25 significant digits in `mpmath`.
T_CDF_POINTS = (-2.0, -0.5)
T_CDF_LITERALS = {(-2.0, 1): 0.1475836176504332741754011,
                  (-0.5, 1): 0.3524163823495667258245989,
                  (-2.0, 2): 0.09175170953613698363378599,
                  (-0.5, 2): 1.0 / 3.0}

# Section 5.2 item 5: two values quoted from the TZ-12 report §4 V7 item 4, and one the Architect
# computed from `2 - Phi((c - log 2)/s) - Phi((c + log 2)/s)` in an independent implementation.
G4_POWER_HALF = (math.log(2.0), 0.1, 0.5)
G4_POWER_ONE = (0.0, 0.1, 1.0)
G4_POWER_TEST2_240 = (2.668167, 0.709080, 0.00267475310692794)

# Section 5.2 item 3: the call shape, proved against a committed hash before §3.1 uses it.
ITEM3_NEED = 400
ITEM3_AFTER = 1789296300

# V4: the TZ-12 report §2 test-2 table, 7 rows and 11 gated columns — 77 values. `E` and `k2` are
# integers; `P0`, `P1`, `P3`, `P_under` and `P_double` are quoted by their replicate counts, which
# are exact; `crit3`, `c4` and `s` are quoted at the six decimals the report prints and `P4` at
# its four. The count is the numerator over `R_NULL` for `P0` and over `R_POWER` for the rest.
V4_TEST2 = {
    240: {"E": 5, "k2": 2, "P0_count": 0, "P1_count": 2000, "crit3": "8.854495",
          "P3_count": 556, "P_under_count": 729, "P_double_count": 1527,
          "c4": "2.668167", "s": "0.709080", "P4": "0.0027"},
    180: {"E": 7, "k2": 2, "P0_count": 0, "P1_count": 2000, "crit3": "9.234764",
          "P3_count": 998, "P_under_count": 996, "P_double_count": 1909,
          "c4": "1.880949", "s": "0.499872", "P4": "0.0087"},
    120: {"E": 5, "k2": 2, "P0_count": 0, "P1_count": 2000, "crit3": "9.385526",
          "P3_count": 1251, "P_under_count": 922, "P_double_count": 1986,
          "c4": "2.017019", "s": "0.536034", "P4": "0.0068"},
    90: {"E": 3, "k2": 2, "P0_count": 0, "P1_count": 2000, "crit3": "9.127945",
         "P3_count": 1236, "P_under_count": 732, "P_double_count": 1990,
         "c4": "1.316484", "s": "0.349863", "P4": "0.0374"},
    60: {"E": 2, "k2": 2, "P0_count": 0, "P1_count": 2000, "crit3": "9.122797",
         "P3_count": 957, "P_under_count": 372, "P_double_count": 1957,
         "c4": "0.489548", "s": "0.130100", "P4": "0.9412"},
    30: {"E": 2, "k2": 2, "P0_count": 0, "P1_count": 2000, "crit3": "6.910353",
         "P3_count": 329, "P_under_count": 0, "P_double_count": 1301,
         "c4": "0.310647", "s": "0.082556", "P4": "1.0000"},
    10: {"E": 2, "k2": 2, "P0_count": 0, "P1_count": 2000, "crit3": "7.164746",
         "P3_count": 36, "P_under_count": 0, "P_double_count": 154,
         "c4": "0.181723", "s": "0.048294", "P4": "1.0000"}}
V4_COLUMNS = ("E", "k2", "P0", "P1", "crit3", "P3", "P_under", "P_double", "c4", "s", "P4")
V4_VALUES = len(V4_COLUMNS) * len(pfair.TAUS)

# Section 6: the fail-fast on the first `tz12.constants` call, and the run projection after it.
FIRST_CONSTANTS_LIMIT_S = 120.0
CONSTANTS_SLOPE = 35
CONSTANTS_OFFSET_S = 500
RUN_CEILING_S = 3000

# V9's read set: every five-minute slot from the first unit the fit set considers to the last
# unit test 3 considers. Both ends are fixed before the run so that read 1 and read 3 hash the
# same set; step 4 asserts that the four formations consider nothing outside it.
READ_FIRST = 1789033800
READ_LAST = 1789669800

# V2: the committed entry points that read an outcome from the capture. This file calls exactly
# one of them, `tz10b.m2_labels`, inside `labels`, and nowhere else.
LABEL_ENTRY_POINTS = ("m2_labels", "venue", "qualification", "score_member", "score")
LABEL_READER = "labels"

# V6: the two authorized paths, relative to `research/`, and the three environment keys.
TWO_PATHS = ("tz13-sized-gate-test3.py", "../CryptoReports/TZ-13-sized-gate-test3-report.md")
THIS_FILE = "research/tz13-sized-gate-test3.py"
ENV_KEYS = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")

# Section 4.3's nine fixed rows: each reading crossed with a power inside the band, above it and
# below it. `0.5` is inside; `0.30` and `0.70` are outside on either side.
WEAKEN_ROWS = tuple((reading, power)
                    for reading in ("PASS", "FAIL", "UNDECIDABLE")
                    for power in (0.5, 0.70, 0.30))

# The gate's four readings and the power each one's UNDECIDABLE clause reads. G2 has no power.
GATE_POWER = {"G1": "P1", "G2": None, "G3": "P3", "G4": "P4"}

CSV_HEADER = tz11a.CSV_HEADER

# Section 4.4: the Architect's pre-registered prediction, printed beside what was measured.
PREDICTION = (
    ("1", "test 3 forms from 810 to 840 units considered, a qualifying rate between 0.88 "
          "and 0.93"),
    ("2", "the admissible share of 750 lies between 0.50 and 0.65 at every tau"),
    ("3", "P3 >= 0.8 at tau 180, 120, 90 and 60; P3 between 0.45 and 0.70 at 240; P3 < 0.3 at "
          "30; P3 < 0.1 at 10"),
    ("4", "P0 <= 0.001 and P1 >= 0.95 at every tau"),
    ("5", "the verdict reads NOT DISQUALIFIED at tau 180, 120 and 90; DISQUALIFIED at 60, "
          "through G3, with lambda-hat > 1; UNDECIDABLE at 240, 30 and 10"),
    ("6", "in §3.6, tau = 10 does not reach tz12.POWER_TO_PASS at 3x"))


# ---- section 4.3: the straddle rule -------------------------------------------------------

def straddle(power, replicates):
    """Section 4.3: does simulation error at `power` cover `tz12.POWER_TO_PASS`?

    A power estimate is a fraction of `replicates` draws. Where the two-sided 95% band around it
    covers the floor, the comparison against the floor is not a decision.
    """
    half = STRADDLE_Z * math.sqrt(power * (1.0 - power) / replicates)
    return abs(power - tz12.POWER_TO_PASS) <= half


def weaken(reading, power):
    """Section 4.3 applied to one gate's reading: inside the band, nothing is decided.

    This can only weaken. PASS and FAIL may become UNDECIDABLE; UNDECIDABLE never becomes
    anything else; a reading whose power lies outside the band is returned untouched.
    """
    if straddle(power, tz12.R_POWER):
        return "UNDECIDABLE"
    return reading


def g4_undecidable(consts, note):
    """Section 4's G4, whose UNDECIDABLE clause the committed `tz12.readings` carries only in
    part: that function returns UNDECIDABLE when `tau` is censored, and §4 adds two more — a
    power below the floor, and a fit that lands on a search edge as `tz11a.bound_note` reports
    it. Both are recorded here and applied in `verdicts`, never by editing the committed file.
    """
    why = []
    if consts["censored"]:
        why.append("censored")
    if consts["P4"] < tz12.POWER_TO_PASS:
        why.append("P4 below the floor")
    if note != "interior":
        why.append("the fit is on a search edge: %s" % note)
    return why


# ---- section 5.2: the six self-tests -------------------------------------------------------

def selftests(manifests):
    """Six items, each an `assert` that aborts the run; the lines they print are returned.

    Every one runs before anything is read from the capture, except item 3, whose whole subject
    is the set-formation call shape and which therefore forms one committed set.
    """
    lines, counts = [], {}

    # Item 1: the straddle band, five calls and the half-width against the Architect's literal.
    half = STRADDLE_Z * math.sqrt(0.25 / tz12.R_POWER)
    rel = abs(half / STRADDLE_HALF_WIDTH - 1.0)
    item1 = (straddle(0.5, tz12.R_POWER), straddle(0.478086, tz12.R_POWER),
             straddle(0.521914, tz12.R_POWER), straddle(0.48, tz12.R_POWER),
             straddle(0.52, tz12.R_POWER))
    assert item1 == (True, False, False, True, True), "section 5.2 item 1: %s" % (item1,)
    assert rel <= CONSTANT_REL_TOL, "section 5.2 item 1: half-width %r against %r, relative %g" % (
        half, STRADDLE_HALF_WIDTH, rel)
    counts["item 1"] = 6
    lines.append("item 1: straddle at 0.5 / 0.478086 / 0.521914 / 0.48 / 0.52 is %s; half-width "
                 "%r against %r, relative %.3g" % (" / ".join(str(v) for v in item1), half,
                                                   STRADDLE_HALF_WIDTH, rel))

    # Item 2: weakening only, over the nine fixed rows.
    item2 = []
    for reading, power in WEAKEN_ROWS:
        got = weaken(reading, power)
        inside = straddle(power, tz12.R_POWER)
        assert (got == "UNDECIDABLE") if inside else (got == reading), \
            "section 5.2 item 2: weaken(%s, %r) is %s" % (reading, power, got)
        assert not (reading == "UNDECIDABLE" and got in ("PASS", "FAIL")), \
            "section 5.2 item 2: UNDECIDABLE became %s" % got
        assert not (reading == "FAIL" and got == "PASS"), "section 5.2 item 2: FAIL became PASS"
        item2.append("%s@%.2f->%s" % (reading, power, got))
    counts["item 2"] = len(WEAKEN_ROWS)
    lines.append("item 2: %s" % " ".join(item2))

    # Item 3: the set-formation call shape, against a hash a committed artifact names.
    rows3, full3 = tz06.scoring_set(manifests, ITEM3_NEED, after=ITEM3_AFTER)
    members3 = [r["T0"] for r in rows3 if r["member"]]
    sha3 = tz07b.member_list_sha(members3)
    assert full3 and sha3 == tz12.TEST2_SHA256, \
        "section 5.2 item 3: the call shape yields %s" % sha3
    counts["item 3"] = 1
    lines.append("item 3: scoring_set(manifests, %d, after=%d) -> %d members, %s"
                 % (ITEM3_NEED, ITEM3_AFTER, len(members3), sha3))

    # Item 4: the Student CDF against closed forms independent of the implementation under test.
    item4 = []
    for nu in (1, 2):
        for z in T_CDF_POINTS:
            got = pfair.t_cdf(z, nu)
            want = T_CDF_LITERALS[(z, nu)]
            rel4 = abs(got / want - 1.0)
            assert rel4 <= CONSTANT_REL_TOL, \
                "section 5.2 item 4: t_cdf(%r, %d) is %r against %r" % (z, nu, got, want)
            mirror = pfair.t_cdf(-z, nu)
            assert abs((mirror + got) - 1.0) <= CONSTANT_REL_TOL, \
                "section 5.2 item 4: t_cdf is not symmetric at %r, nu %d" % (z, nu)
            item4.append("t_cdf(%r, %d)=%.17g rel %.2g" % (z, nu, got, rel4))
    counts["item 4"] = 8
    lines.append("item 4: %s; symmetry 4 of 4" % "; ".join(item4))

    # Item 5: `tz12.g4_power` at three fixed arguments.
    item5 = []
    for c4, s, want in (G4_POWER_HALF, G4_POWER_ONE, G4_POWER_TEST2_240):
        got = tz12.g4_power(c4, s)
        rel5 = abs(got / want - 1.0)
        assert rel5 <= POWER_REL_TOL, \
            "section 5.2 item 5: g4_power(%r, %r) is %r against %r" % (c4, s, got, want)
        item5.append("g4_power(%r, %r)=%.17g rel %.2g" % (c4, s, got, rel5))
    counts["item 5"] = 3
    lines.append("item 5: %s" % "; ".join(item5))

    # Item 6: stream separation, four assertions.
    def first(set_code, tau, purpose, n=1):
        return tz12.stream(set_code, tau, purpose).random(n)

    a = first(tz12.SET_CODES[SET_NAME], 60, 0, tz12.STREAM_CHECK_DOUBLES)
    b = first(tz12.SET_CODES[SET_NAME], 60, 0, tz12.STREAM_CHECK_DOUBLES)
    assert numpy.array_equal(a, b), "section 5.2 item 6: the same call gave two streams"
    other_set = float(first(tz12.SET_CODES["test2"], 60, 0)[0])
    other_purpose = float(first(tz12.SET_CODES[SET_NAME], 60, 1)[0])
    assert other_set != float(a[0]), "section 5.2 item 6: two sets share a first double"
    assert other_purpose != float(a[0]), "section 5.2 item 6: two purposes share a first double"
    counts["item 6"] = 4
    lines.append("item 6: %d doubles identical; test2 first %.17g, purpose 1 first %.17g, test3 "
                 "first %.17g" % (tz12.STREAM_CHECK_DOUBLES, other_set, other_purpose,
                                  float(a[0])))
    return {"lines": lines, "counts": counts, "items": len(counts),
            "assertions": sum(counts.values()),
            "item3_members": len(members3), "item3_sha256": sha3}


# ---- V2 and V6: the instrument read as a syntax tree ----------------------------------------

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


def enclosing(tree):
    """Every node that lies inside a top-level function, by node identity, to that function's
    name. A node in no function maps to nothing, so `get` returns the module itself."""
    out = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            for inner in ast.walk(node):
                out[id(inner)] = node.name
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
    node = next(n for n in ast.walk(tree)
                if isinstance(n, ast.FunctionDef) and n.name == "v2_static")
    doc = ast.get_docstring(node).splitlines()
    words = doc[doc.index("forbidden:") + 1:doc.index("end")]
    assert len(words) == 5, "V2: the forbidden list reads %s" % words
    docs = docstring_nodes(tree)
    inside = enclosing(tree)
    constants_scanned, carrying = 0, []
    calls, outside_reader, reader_calls = 0, [], 0
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in docs:
            constants_scanned += 1
            if any(w in n.value for w in words):
                carrying.append(n.lineno)
        elif isinstance(n, ast.Call):
            calls += 1
            if isinstance(n.func, ast.Attribute) and n.func.attr in LABEL_ENTRY_POINTS:
                if inside.get(id(n)) == LABEL_READER:
                    reader_calls += 1
                else:
                    outside_reader.append((n.lineno, n.func.attr))
    assert not carrying, "V2: string constants carry a forbidden word at lines %s" % carrying
    assert not outside_reader, "V2: an outcome entry point is called at %s" % outside_reader
    assert reader_calls == 1, "V2: %d outcome reads inside %s" % (reader_calls, LABEL_READER)
    return {"forbidden_words": words, "string_constants_scanned": constants_scanned,
            "docstrings_exempt": len(docs), "constants_carrying_a_forbidden_word": len(carrying),
            "calls_scanned": calls, "label_entry_points": list(LABEL_ENTRY_POINTS),
            "label_entry_point_calls_outside_the_reader": len(outside_reader),
            "label_entry_point_calls_inside_the_reader": reader_calls}


def v6():
    """V6: the diff is one new file, and this file rebinds nothing it imports."""
    base = tz10b.git("merge-base", "HEAD", "origin/main").strip()
    head = tz10b.git("rev-parse", "HEAD").strip()
    status = tz10b.git("status", "--porcelain", "--", *TWO_PATHS)
    assert not status.strip(), "V6: the run is not of committed files: %s" % status
    names = tz10b.git("diff", "--name-only", base, "HEAD").split()
    assert names == [THIS_FILE], "V6: the branch changes %s" % names
    replaced = [line for line in tz10b.git("diff", "--unified=0", base, "HEAD").splitlines()
                if line.startswith("-") and not line.startswith("---")]
    assert not replaced, "V6: the change replaces %d committed lines" % len(replaced)
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
    return {"merge_base": base, "head": head, "status_two_paths": status, "diff_names": names,
            "replaced_lines": replaced, "replaced_line_count": len(replaced),
            "attribute_stores": stores, "global_or_nonlocal": scopes,
            "environ_writes": list(env)}


# ---- section 3.1: the sets -------------------------------------------------------------------

def the_set(manifests, committed):
    """Section 3.1: test 3, by the committed set rule, with that section's four assertions."""
    rows, full = tz06.scoring_set(manifests, TEST3_NEED, after=TEST3_AFTER)
    members = [r["T0"] for r in rows if r["member"]]
    if not full:
        last = max(int(name) for name in os.listdir(os.path.join(config.ROOT, config.SERIES)))
        raise SystemExit(
            "BLOCKED at section 0.6: %d of %d qualifying slots with T0 > %d; %d units "
            "considered, from %d to %d; the last slot on disk is %d"
            % (len(members), TEST3_NEED, TEST3_AFTER, len(rows), rows[0]["T0"],
               rows[-1]["T0"], last))
    assert len(members) == TEST3_NEED and min(members) > TEST3_AFTER, \
        "section 3.1 item 1: %d members, first %d" % (len(members), min(members))
    for name in tz11a.SETS:
        overlap = sorted(set(members) & set(committed[name][1]))
        assert not overlap, "section 3.1 item 2: test 3 meets %s at %s" % (name, overlap)
    rows400, full400 = tz06.scoring_set(manifests, FIRST_400, after=TEST3_AFTER)
    first400 = [r["T0"] for r in rows400 if r["member"]]
    assert full400 and first400 == members[:FIRST_400], \
        "section 3.1 item 3: the first %d members are not a prefix of test 3" % FIRST_400
    sha = tz07b.member_list_sha(members)
    reasons = {}
    for r in rows:
        if not r["member"]:
            key = " + ".join(r["reasons"])
            reasons[key] = reasons.get(key, 0) + 1
    doc = {"set": SET_NAME, "label": SET_LABEL, "need": TEST3_NEED, "after": TEST3_AFTER,
           "units_considered": len(rows), "members": len(members),
           "non_members": len(rows) - len(members),
           "non_member_reasons": dict(sorted(reasons.items())),
           "qualifying_rate": len(members) / len(rows),
           "first_unit": rows[0]["T0"], "last_unit": rows[-1]["T0"],
           "first_member": members[0], "last_member": members[-1],
           "member_list_sha256": sha, "member_list_sha256_asserted": False,
           "first_400_sha256": tz07b.member_list_sha(first400),
           "superset_of_the_first_400": True,
           "pairwise_disjoint_asserted": len(tz11a.SETS),
           "disclosure_sha256": tz12.disclosure_sha(rows)}
    return rows, members, doc


# ---- section 3.2: the walk, the rows and the domain -------------------------------------------

def walk(members, manifests):
    """Section 3.2: every member walked by the committed walk, with `guard` false."""
    return {t0: tz11a.walk_member(t0, manifests, False) for t0 in members}


def guard_sample(members, manifests):
    """Section 3.2: the sample the guarded pass runs over, formed mechanically.

    The first 25 members in ascending `T0`, the last 25, and the 25 whose run-up window holds the
    most excluded seconds as `tz07a.excluded_seconds` returns them, ties broken by ascending
    `T0`. The three lists are unioned, so the sample is at most 75; its size is re-derived here.
    """
    head = members[:GUARD_HEAD]
    tail = members[-GUARD_TAIL:]
    counts = {t0: len(tz07a.excluded_seconds(t0, manifests)) for t0 in members}
    worst = sorted(members, key=lambda t0: (-counts[t0], t0))[:GUARD_EXCLUDED]
    sample = sorted(set(head) | set(tail) | set(worst))
    doc = {"head": len(head), "tail": len(tail), "most_excluded_seconds": len(worst),
           "at_most": GUARD_HEAD + GUARD_TAIL + GUARD_EXCLUDED, "size": len(sample),
           "largest_excluded_second_counts": [[t0, counts[t0]] for t0 in worst],
           "members_with_any_excluded_second": sum(1 for t0 in members if counts[t0]),
           "overlap_head_tail_worst": len(head) + len(tail) + len(worst) - len(sample)}
    return sample, doc


def guarded_pass(sample, manifests, rows):
    """Section 3.2: the same walk again with `guard` true, every row asserted identical."""
    compared = 0
    for t0 in sample:
        again = tz11a.walk_member(t0, manifests, True)
        for tau in pfair.TAUS:
            row = tz11a.checkpoint_row(t0, SET_NAME, tau, again[tau])
            assert row == rows[t0][tau], \
                "section 3.2: the guarded row differs at %d tau %d" % (t0, tau)
            compared += 1
    return {"members": len(sample), "rows_compared": compared,
            "rows_identical": compared, "taus": len(pfair.TAUS)}


def admissible(walked, members):
    """Section 3.2: the admissible members per `tau`, at the committed literal `pfair.ADMIT`."""
    per_tau = tz11a.admissible_members(walked, members, pfair.ADMIT)
    doc = {}
    for tau in pfair.TAUS:
        held = per_tau[tau]
        doc[tau] = {"tau": tau, "ADMIT": pfair.ADMIT[tau], "members": len(held),
                    "of": len(members), "share": len(held) / len(members),
                    "member_list_sha256": tz07b.member_list_sha(held),
                    "first": held[0] if held else None, "last": held[-1] if held else None}
    return per_tau, doc


def rows_of(walked, members):
    """Section 3.2: one checkpoint row per member per `tau`, every one carrying no outcome."""
    return {t0: {tau: tz11a.checkpoint_row(t0, SET_NAME, tau, walked[t0][tau])
                 for tau in pfair.TAUS} for t0 in members}


def unlabelled(rows, members, where):
    """Steps 7 and 9: all 5,250 rows carry `label is None`, counted and asserted."""
    seen, carried = 0, []
    for t0 in members:
        for tau in pfair.TAUS:
            seen += 1
            if rows[t0][tau]["label"] is not None:
                carried.append((t0, tau))
    assert seen == TEST3_ROWS and not carried, \
        "V2 at %s: %d rows, %d carrying an outcome" % (where, seen, len(carried))
    return {"where": where, "rows": seen, "label_is_none": seen - len(carried),
            "required": TEST3_ROWS, "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


# ---- section 3.3: the constants, from predictions alone ---------------------------------------

def sizing(rows, per_tau, set_name, timing):
    """Section 3.3: `tz12.constants` at every `tau`, over one set's admissible rows.

    The first call is timed and §6's fail-fast applied to it: above `FIRST_CONSTANTS_LIMIT_S`
    the run is BLOCKED, and so is a projection of `35 t + 500` s above `RUN_CEILING_S`.
    """
    out = {}
    for tau in pfair.TAUS:
        population = [rows[t0][tau] for t0 in per_tau[tau]]
        started = time.monotonic()
        out[tau] = tz12.constants(population, tau, tz12.SET_CODES[set_name])
        seconds = time.monotonic() - started
        timing.setdefault(set_name, {})[tau] = seconds
        if not timing.get("first_checked"):
            timing["first_seconds"] = seconds
            timing["first_projection_s"] = CONSTANTS_SLOPE * seconds + CONSTANTS_OFFSET_S
            timing["first_checked"] = True
            if seconds > FIRST_CONSTANTS_LIMIT_S:
                raise SystemExit("BLOCKED at section 6: the first tz12.constants call took "
                                 "%.1f s, above %.0f s" % (seconds, FIRST_CONSTANTS_LIMIT_S))
            if timing["first_projection_s"] > RUN_CEILING_S:
                raise SystemExit("BLOCKED at section 6: the run projects %.0f s (%d x %.1f + "
                                 "%d), above %d s" % (timing["first_projection_s"],
                                                      CONSTANTS_SLOPE, seconds,
                                                      CONSTANTS_OFFSET_S, RUN_CEILING_S))
    return out


# ---- section 3.6: how the gate's power grows with the population -------------------------------

def repeated(population, multiple):
    """Section 3.6: one population's rows repeated `multiple` times.

    `tz12.constants` asserts one row per member in ascending `T0`, so the copies cannot carry the
    member's own `T0`. Each copy takes the key `T0 * multiple + copy`, which is strictly
    increasing across the whole multiset and unique within it. The key enters that assertion and
    `members_sha256` and nothing else: no statistic of `tz12.constants` reads a `T0`.
    """
    out = []
    for row in population:
        for copy in range(multiple):
            out.append(dict(row, T0=row["T0"] * multiple + copy))
    return out


def projection(rows, per_tau):
    """Section 3.6: `P3`, `P1` and `P4` at 1x, 2x and 3x, and where `P3` reaches the floor.

    A repeated row is not a new observation. It holds the scale of the likelihood fixed while
    multiplying its weight, which is what a larger set would do to the non-centrality and is not
    what a larger set would do to anything else. No verdict, threshold or admission reads this.
    """
    out = {}
    for tau in pfair.TAUS:
        base = [rows[t0][tau] for t0 in per_tau[tau]]
        at = {}
        for multiple in PROJECTION_MULTIPLES:
            consts = tz12.constants(repeated(base, multiple), tau,
                                    tz12.SET_CODES[SET_NAME])
            at[multiple] = {"n": consts["n"], "P3": consts["P3"], "P1": consts["P1"],
                            "P4": consts["P4"], "crit3": consts["crit3"], "E": consts["E"],
                            "k2": consts["k2"]}
        reaches = [m for m in PROJECTION_MULTIPLES if at[m]["P3"] >= tz12.POWER_TO_PASS]
        out[tau] = {"tau": tau, "at": at, "smallest_multiple_reaching_the_floor":
                    reaches[0] if reaches else None,
                    "floor": tz12.POWER_TO_PASS}
    return out


# ---- section 3.4: the outcomes, read once ------------------------------------------------------

def labels(members, ledger):
    """Section 3.4: the one outcome read of the run, after §3.3's output is on disk.

    `tz10b.m2_labels` is the single committed entry point this file calls that reads the venue's
    settled document, and `ledger` counts the call so V2 can assert it happened exactly once.
    """
    ledger["m2_labels_calls"] += 1
    ledger["m2_labels_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    got = tz10b.m2_labels(members)
    missing = [t0 for t0 in members if t0 not in got]
    return got, {"members": len(members), "returned": len(got), "missing": len(missing),
                 "missing_members": missing, "utc": ledger["m2_labels_utc"],
                 "up": sum(got.values()), "calls": ledger["m2_labels_calls"]}


# ---- section 3.5: the observed statistics ------------------------------------------------------

def observed(rows, walked, per_tau, label_of):
    """Section 3.5, per `tau`, over test 3's admissible rows with the outcomes of §3.4.

    Brier and the bins by the committed definitions; the scale by the committed search under the
    committed Student log CDF; the shape by the committed fit over the same members' anchors.
    Every figure a verdict table reads is produced a second time without its single most
    influential member — reported, not asserted, and never read by a gate.
    """
    out = {}
    for tau in pfair.TAUS:
        held = [t0 for t0 in per_tau[tau] if t0 in label_of]
        scored = []
        for t0 in held:
            scored.append(dict(rows[t0][tau], label=label_of[t0]))
        pairs = [(r["p_t"], r["label"]) for r in scored]
        zs = [(r["z_student"], r["label"]) for r in scored]
        nu = float(pfair.LINK_NU[tau])
        log_cdf = tz11a.student_log_cdf(nu)
        table = tz06.table_for(tau, scored, "p_t", tz11a.G1_BRIER)
        lam = tz11a.lambda_with_influence(zs, held, log_cdf)
        r, offsets, _flat, _squares = tz11a.population(walked, held, tau)
        fit = tz11a.fit_student(r)
        note = tz11a.bound_note(fit)
        influence = tz11a.influence_refit(r, offsets, held, fit)
        log_ratio = math.log(fit["nu"] / nu)
        out[tau] = {
            "tau": tau, "members": len(held), "excluded_for_want_of_an_outcome":
                len(per_tau[tau]) - len(held),
            "member_list_sha256": tz07b.member_list_sha(held),
            "up_rate": table["observed_up_rate"],
            "brier": tz06.brier(pairs), "brier_constant": tz11a.G1_BRIER,
            "eligible_bins": table["eligible_bins"], "failing_bins": table["failing_bins"],
            "bins": table["bins"],
            "lambda_hat": lam["lambda_hat"], "lr": lam["likelihood_ratio"],
            "chi_square_1df_p": lam["chi_square_1df_p"],
            "nu_hat": fit["nu"], "s_hat": fit["s"], "anchors": fit["n"],
            "LINK_NU": pfair.LINK_NU[tau], "log_ratio": log_ratio,
            "bound_note": note, "nu_on_bound": note != "interior",
            "influence": {
                "lambda_hat_without": lam["most_influential"]["lambda_hat_without"],
                "lambda_shift": lam["most_influential"]["shift"],
                "lambda_most_influential_T0": lam["most_influential"]["T0"],
                "nu_without": influence["nu_without"], "s_without": influence["s_without"],
                "nu_shift": influence["nu_shift"],
                "nu_most_influential_T0": influence["T0"],
                "log_ratio_without": math.log(influence["nu_without"] / nu)}}
    return out


def verdicts(consts, obs):
    """Section 4: the committed readings, then §4's own G4 clauses, then §4.3's band.

    `tz12.readings` is called as the file holds it. Its G4 carries only the censored clause of
    §4; the other two — a power below the floor and a fit on a search edge — are added here and
    can only turn a reading into UNDECIDABLE. §4.3's band is applied last and can only do the
    same. The committed reading is kept beside the weakened one so both are on the record.
    """
    committed, weakened, why = {}, {}, {}
    for tau in pfair.TAUS:
        o = obs[tau]
        reading = tz12.readings(consts[tau], {
            "brier": o["brier"], "failing_bins": o["failing_bins"], "lr": o["lr"],
            "log_ratio": o["log_ratio"], "nu_on_bound": o["nu_on_bound"]})
        committed[tau] = dict(reading)
        after = dict(reading)
        note = []
        extra = g4_undecidable(consts[tau], o["bound_note"])
        if extra and after["G4"] != "UNDECIDABLE":
            after["G4"] = "UNDECIDABLE"
            note.append("G4: %s" % "; ".join(extra))
        elif extra:
            note.append("G4: %s" % "; ".join(extra))
        for gate, key in GATE_POWER.items():
            if key is None:
                continue
            power = consts[tau][key]
            before = after[gate]
            after[gate] = weaken(before, power)
            if after[gate] != before:
                note.append("%s: %s became UNDECIDABLE, %s = %.4f is inside the band"
                            % (gate, before, key, power))
        weakened[tau] = after
        why[tau] = note
    committed_verdict = tz12.verdict(committed)
    weakened_verdict = tz12.verdict(weakened)
    per_tau = {}
    for tau in pfair.TAUS:
        reading = weakened[tau]
        failing = [gate for gate in tz12.GATES
                   if reading[gate] == "FAIL" and (gate != "G2" or reading["G2_gated"])]
        if failing:
            answer, because = "DISQUALIFIED", failing
        elif reading["G1"] == "PASS" and reading["G3"] == "PASS":
            answer, because = "NOT DISQUALIFIED", []
        else:
            answer = "UNDECIDABLE"
            because = [gate for gate in ("G1", "G3") if reading[gate] != "PASS"]
        per_tau[tau] = {"tau": tau, "verdict": answer, "because": because,
                        "readings": reading, "committed_readings": committed[tau],
                        "weakened_by": why[tau],
                        "powers": {key: consts[tau][key] for key in ("P0", "P1", "P3", "P4")},
                        "straddles": {gate: straddle(consts[tau][key], tz12.R_POWER)
                                      for gate, key in GATE_POWER.items() if key}}
    return {"per_tau": per_tau, "committed_family_verdict": committed_verdict,
            "weakened_family_verdict": weakened_verdict,
            "family_alpha": tz12.FAMILY_ALPHA, "alpha": dict(tz12.ALPHA),
            "count_bound": tz12.COUNT_BOUND, "crit_rank": tz12.CRIT_RANK}


# ---- V4: the instrument reproduces what is committed --------------------------------------------

def v4(walked, fit, fit_admissible, test2_consts):
    """V4: the four measured tables, and the TZ-12 report's §2 test-2 table at 77 of 77."""
    doc, timing = tz12.v4_fits(walked, fit, fit_admissible)
    sigma = [{"tau": tau, "in_tz12": tz12.SIGMA_LOG_NU[tau]} for tau in pfair.TAUS]
    assert tuple(tz12.SIGMA_LOG_NU) == tuple(pfair.TAUS), \
        "V4: tz12.SIGMA_LOG_NU carries %s" % list(tz12.SIGMA_LOG_NU)
    checked, mismatched = 0, []
    for tau in pfair.TAUS:
        want, got = V4_TEST2[tau], test2_consts[tau]
        pairs = (("E", want["E"], got["E"]), ("k2", want["k2"], got["k2"]),
                 ("P0", want["P0_count"], got["null_brier_at_or_above"]),
                 ("P1", want["P1_count"], got["coin_brier_at_or_above"]),
                 ("crit3", want["crit3"], "%.6f" % got["crit3"]),
                 ("P3", want["P3_count"], got["over_beyond_crit3"]),
                 ("P_under", want["P_under_count"], got["under_beyond_crit3"]),
                 ("P_double", want["P_double_count"], got["double_beyond_crit3"]),
                 ("c4", want["c4"], "%.6f" % got["c4"]),
                 ("s", want["s"], "%.6f" % got["s"]),
                 ("P4", want["P4"], "%.4f" % got["P4"]))
        for column, expected, actual in pairs:
            checked += 1
            if expected != actual:
                mismatched.append((tau, column, expected, actual))
    assert not mismatched and checked == V4_VALUES, \
        "BLOCKED at V4: %d of %d values differ: %s" % (len(mismatched), checked, mismatched)
    doc["sigma_log_nu"] = sigma
    doc["sigma_log_nu_censored"] = sorted(tz12.SIGMA_LOG_NU_CENSORED)
    doc["test2_values_checked"] = checked
    doc["test2_values_required"] = V4_VALUES
    doc["test2_columns"] = list(V4_COLUMNS)
    doc["test2_mismatched"] = mismatched
    return doc, timing


# ---- V8 and V10: the fingerprint --------------------------------------------------------------

def fingerprint(paths):
    """`wc -l`, `wc -c` and `sha256sum` of every path, read from the working tree."""
    out = {}
    for path in paths:
        full = os.path.join(HERE, "..", path)
        with open(full, "rb") as fh:
            blob = fh.read()
        out[path] = {"lines": blob.count(b"\n"), "bytes": len(blob),
                     "sha256": hashlib.sha256(blob).hexdigest()}
    return out


MAP_PATHS = ("SYSTEM-MAP.md", "BTC-EXECUTOR-INSTRUCTIONS.md", "research/twap-divergence.py",
             "research/selftest-twap-divergence.py", "research/tz02-distribution.py",
             "research/pfair.py", "research/selftest-pfair.py", "research/tz06-calibration.py",
             "research/tz07a-variance-time.py", "research/tz07b-settlement-dispersion.py",
             "research/tz08a-out-of-sample.py", "research/tz09-disk-inventory.py",
             "research/tz10b-sigma-or-link.py", "research/tz11a-student-link.py",
             "research/tz12-sized-gate.py", "research/recorder/recorder.py",
             "research/recorder/config.py", "research/recorder/manifest.py",
             "research/recorder/analyze.py", "research/recorder/probe.py",
             "research/recorder/selftest.py", ".gitignore", THIS_FILE)


# ---- the run ------------------------------------------------------------------------------------

def read_range():
    """V9's read set: every five-minute slot from `READ_FIRST` to `READ_LAST`."""
    return list(range(READ_FIRST, READ_LAST + config.INTERVAL_S, config.INTERVAL_S))


def build(target):
    """The thirteen steps of §5.1, in that order, with the order itself asserted."""
    order, clock, timing = [], {}, {}
    started = time.monotonic()
    ledger = {"m2_labels_calls": 0, "m2_labels_utc": None}

    # 1. host read 1.
    host1 = tz11a.host_read("run start", read_range(), tz11a.FLOOR_START_BYTES)
    order.append("1 host read 1")

    # 2. the six self-tests.
    manifests = load_manifests()
    tests = selftests(manifests)
    order.append("2 self-tests")

    # 3. v6 and the static half of v2.
    diff = v6()
    static = v2_static()
    order.append("3 v6 and v2 static")

    # 4. the three committed sets and test 3.
    sets, sets_doc = tz11a.the_sets(manifests)
    rows3, members, set_doc = the_set(manifests, sets)
    considered = set()
    for name in tz11a.SETS:
        considered.update(r["T0"] for r in sets[name][0])
    considered.update(r["T0"] for r in rows3)
    outside = sorted(t0 for t0 in considered if t0 < READ_FIRST or t0 > READ_LAST)
    assert not outside, "V9: %d units considered lie outside the read set" % len(outside)
    assert set_doc["last_unit"] == READ_LAST, \
        "V9: test 3's last unit is %d, not %d" % (set_doc["last_unit"], READ_LAST)
    order.append("4 the four sets")

    # 5. the walk, the guarded pass, host read 2.
    # V4 reads the fit set's admissible rows for ADMIT, LINK_NU and LINK_SCALE, and test 2's for
    # the TZ-12 table. Test 1 is formed for §3.1's disjointness and is never walked.
    committed_members = list(sets["fit"][1]) + list(sets["test2"][1])
    walked_committed = walk(committed_members, manifests)
    walked = walk(members, manifests)
    rows = rows_of(walked, members)
    sample, guard_doc = guard_sample(members, manifests)
    guard_doc.update(guarded_pass(sample, manifests, rows))
    host2 = tz11a.host_read("after the walk", read_range(), tz11a.FLOOR_BYTES)
    order.append("5 the walk and the guarded pass")

    # 6. the domain.
    per_tau, domain = admissible(walked, members)
    test2_admissible = tz11a.admissible_members(walked_committed, sets["test2"][1], pfair.ADMIT)
    fit_admissible = tz11a.admissible_members(walked_committed, sets["fit"][1], pfair.ADMIT)
    order.append("6 the domain")

    # 7. every row carries no outcome.
    step7 = unlabelled(rows, members, "step 7")
    clock["rows_unlabelled_first"] = step7["utc"]
    order.append("7 label is None, 5,250 of 5,250")

    # 8. the constants, and their output on disk.
    consts = sizing(rows, per_tau, SET_NAME, timing)
    clock["sizing_written"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(os.path.join(target, "tz13-sizing.json"), "w", encoding="utf-8",
              newline="\n") as fh:
        fh.write(json.dumps({"set": SET_NAME, "constants": consts, "domain": domain},
                            sort_keys=True, indent=2, default=str) + "\n")
    order.append("8 tz12.constants, written to disk")

    # 9. the same assertion again.
    step9 = unlabelled(rows, members, "step 9")
    clock["rows_unlabelled_second"] = step9["utc"]
    order.append("9 label is None again")

    # 10. the projection — still free of any outcome.
    projected = projection(rows, per_tau)
    order.append("10 the projection")

    # V4's reproduction runs here, on test 2's admissible rows, still before any outcome.
    test2_rows = {t0: {tau: tz11a.checkpoint_row(t0, "test2", tau, walked_committed[t0][tau])
                       for tau in pfair.TAUS} for t0 in sets["test2"][1]}
    test2_consts = sizing(test2_rows, test2_admissible, "test2", timing)
    v4_doc, v4_timing = v4(walked_committed, sets["fit"][1], fit_admissible, test2_consts)

    # 11. the outcomes, read once — the first outcome read of the run.
    label_of, label_doc = labels(members, ledger)
    clock["labels_read"] = label_doc["utc"]
    order.append("11 tz10b.m2_labels")

    # 12. the observed statistics, the readings, the verdict, the weakening, the influence.
    obs = observed(rows, walked, per_tau, label_of)
    gate = verdicts(consts, obs)
    order.append("12 the readings and the verdict")

    # 13. host read 3, and V9's four assertions.
    host3 = tz11a.host_read("run end", read_range(), tz11a.FLOOR_BYTES)
    assert host1["recorder_pids"] == host3["recorder_pids"], \
        "V9: the recorder pids moved from %s to %s" % (host1["recorder_pids"],
                                                       host3["recorder_pids"])
    assert host1["newest_start_recv_ns"] == host3["newest_start_recv_ns"] \
        and host1["newest_start_sha"] == host3["newest_start_sha"], \
        "V9: the newest start record moved"
    assert host3["interval_directories"] >= host1["interval_directories"], \
        "V9: the interval count fell from %d to %d" % (host1["interval_directories"],
                                                       host3["interval_directories"])
    assert host1["read_set_sha256"] == host3["read_set_sha256"], "V9: the read set changed"
    order.append("13 host read 3 and V9")
    assert ledger["m2_labels_calls"] == 1, \
        "V2: m2_labels was called %d times" % ledger["m2_labels_calls"]

    doc = {
        "set": set_doc, "committed_sets": sets_doc, "guard": guard_doc, "domain": domain,
        "constants": consts, "projection": projected, "labels": label_doc,
        "observed": obs, "gate": gate, "v4": v4_doc, "v2_static": static, "v6": diff,
        "selftests": tests, "order": order, "clock": clock,
        "rows_unlabelled": [step7, step9],
        "fingerprint": fingerprint(MAP_PATHS),
        "prediction": [{"n": n, "predicted": text} for n, text in PREDICTION],
        "straddle": {"z": STRADDLE_Z, "replicates": tz12.R_POWER,
                     "half_width_at_one_half": STRADDLE_HALF_WIDTH,
                     "floor": tz12.POWER_TO_PASS},
        "disclosure": [{"T0": r["T0"], "member": bool(r["member"]),
                        "reasons": list(r["reasons"])} for r in rows3],
    }
    host = {"reads": [host1, host2, host3], "floor_start": tz11a.FLOOR_START_BYTES,
            "floor": tz11a.FLOOR_BYTES, "reads_asserted": 3,
            "constants_seconds": timing, "v4_fits_seconds": v4_timing,
            "wall_clock_s": time.monotonic() - started,
            "interpreter": sys.version, "numpy": numpy.__version__}
    return doc, csv_text(members, rows, label_of), tables(doc), host


def csv_text(members, rows, label_of):
    """V11: one row per member per `tau`, sufficient to reconstruct any single row."""
    lines = [",".join(CSV_HEADER)]
    for t0 in members:
        for tau in pfair.TAUS:
            row = dict(rows[t0][tau], label=label_of.get(t0))
            lines.append(",".join(tz11a.cell(row[key]) for key in CSV_HEADER))
    return "\n".join(lines) + "\n"


# ---- output ---------------------------------------------------------------------------------

def f4(value):
    return "%.4f" % value


def f6(value):
    return "%.6f" % value


def tables(doc):
    out = ["## The set", ""]
    s = doc["set"]
    out += ["| field | value |", "|---|---|",
            "| units considered | %d (%d … %d) |" % (s["units_considered"], s["first_unit"],
                                                     s["last_unit"]),
            "| members | %d (%d … %d) |" % (s["members"], s["first_member"], s["last_member"]),
            "| non-members | %d (%s) |" % (s["non_members"], ", ".join(
                "%s: %d" % (k, v) for k, v in s["non_member_reasons"].items()) or "none"),
            "| qualifying rate | %.4f |" % s["qualifying_rate"],
            "| member list SHA-256 | `%s` |" % s["member_list_sha256"],
            "| first 400 SHA-256 | `%s` |" % s["first_400_sha256"],
            "| disclosure SHA-256 | `%s` |" % s["disclosure_sha256"], ""]

    out += ["## The domain", "", "| tau | ADMIT | admissible | share of 750 | member list |",
            "|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        d = doc["domain"][tau]
        out.append("| %d | %s | %d | %.4f | `%s` |" % (tau, d["ADMIT"], d["members"],
                                                       d["share"], d["member_list_sha256"]))

    out += ["", "## The constants, from the predictions alone", "",
            "| tau | m | P0 | P1 | E | k2 | crit3 | P3 | P_under | P_double | c4 | s | P4 |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        c = doc["constants"][tau]
        out.append("| %d | %d | %s | %s | %d | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            tau, c["n"], tz12.frac(c["null_brier_at_or_above"], tz12.R_NULL),
            tz12.frac(c["coin_brier_at_or_above"], tz12.R_POWER), c["E"],
            "—" if c["k2"] is None else c["k2"], f6(c["crit3"]),
            tz12.frac(c["over_beyond_crit3"], tz12.R_POWER),
            tz12.frac(c["under_beyond_crit3"], tz12.R_POWER),
            tz12.frac(c["double_beyond_crit3"], tz12.R_POWER),
            f6(c["c4"]), f6(c["s"]), f4(c["P4"])))

    out += ["", "## The observed statistics", "",
            "| tau | m | up rate | Brier | eligible bins | failing bins | lambda-hat | LR | "
            "nu-hat | s-hat | search edge | log(nu-hat / LINK_NU) |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        o = doc["observed"][tau]
        out.append("| %d | %d | %.4f | %.6f | %d | %d | %.6f | %.6f | %.4f | %.4f | %s | %+.6f |"
                   % (tau, o["members"], o["up_rate"], o["brier"], o["eligible_bins"],
                      o["failing_bins"], o["lambda_hat"], o["lr"], o["nu_hat"], o["s_hat"],
                      o["bound_note"], o["log_ratio"]))

    out += ["", "## The gate", "",
            "| tau | G1 | G2 | G3 | G4 | verdict | left there by |", "|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        v = doc["gate"]["per_tau"][tau]
        r = v["readings"]
        out.append("| %d | %s | %s | %s | %s | **%s** | %s |" % (
            tau, r["G1"], "%s%s" % (r["G2"], "" if r["G2_gated"] else " (not gated)"),
            r["G3"], r["G4"], v["verdict"],
            ", ".join(v["because"]) if v["because"] else "—"))

    out += ["", "## The projection — a projection, and no gate reads it", "",
            "| tau | n at 1x | P3 1x | P3 2x | P3 3x | P1 1x/2x/3x | P4 1x/2x/3x | "
            "smallest multiple reaching 0.5 |", "|---|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        p = doc["projection"][tau]
        at = p["at"]
        out.append("| %d | %d | %s | %s | %s | %s | %s | %s |" % (
            tau, at[1]["n"], f4(at[1]["P3"]), f4(at[2]["P3"]), f4(at[3]["P3"]),
            " / ".join(f4(at[m]["P1"]) for m in PROJECTION_MULTIPLES),
            " / ".join(f4(at[m]["P4"]) for m in PROJECTION_MULTIPLES),
            p["smallest_multiple_reaching_the_floor"] or "not at 3x"))

    out += ["", "## Influence — recorded, not asserted", "",
            "| tau | lambda-hat | without | shift | nu-hat | without | shift | crit3 | "
            "from 10,000 |", "|---|---|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        o = doc["observed"][tau]
        i = o["influence"]
        c = doc["constants"][tau]
        out.append("| %d | %.6f | %.6f | %+.6f | %.4f | %.4f | %+.4f | %s | %s |" % (
            tau, o["lambda_hat"], i["lambda_hat_without"], i["lambda_shift"], o["nu_hat"],
            i["nu_without"], i["nu_shift"], f6(c["crit3"]), f6(c["crit3_first_10000"])))
    return "\n".join(out) + "\n"


def main(argv):
    if argv[1:2] != ["--out"] or len(argv) != 3:
        sys.stderr.write("usage: python -B tz13-sized-gate-test3.py --out <directory>\n")
        return 2
    target = os.path.realpath(argv[2])
    capture = os.path.realpath(config.ROOT)
    assert os.path.isdir(target), "no directory %s" % target
    assert not (target + os.sep).startswith(capture + os.sep), \
        "V9: %s is inside the capture" % target
    doc, csv, md, host = build(target)
    outputs = {"tz13-results.json": json.dumps(doc, sort_keys=True, indent=2, default=str) + "\n",
               "tz13-tables.md": md,
               "tz13-observations.csv": csv,
               "tz13-host.json": json.dumps(host, sort_keys=True, indent=2, default=str) + "\n"}
    for name, text in outputs.items():
        with open(os.path.join(target, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
