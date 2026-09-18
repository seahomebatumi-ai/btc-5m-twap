"""TZ-14 — the quote inventory.

Tier C has stored fourteen order-book replies per interval since 2026-09-12 and nothing has ever
opened one. This file opens them for the first time and characterises what is there: how often the
capture is complete, what a reply contains, how far after its nominal checkpoint a read lands, what
the touch is worth in size, and what a round trip costs after the venue's taker fee.

It computes no score. No quantity here is a function of both a quote and an output of the pricer,
with the single exemption section 3.2 names: `sigma_hat`, the pricer's own scale in USD/s, through
which the frozen domain rule `pfair.ADMIT` partitions the members. No probability is computed
anywhere — the twelve probability entry points of `pfair` are never called and V2 asserts the count
is zero over this file's own syntax tree. No label enters any printed number: the venue's settled
outcome is read only inside `tz06.qualification`, which decides membership, and no table below is
keyed, split or weighted by it.

Because nothing here scores the market against the pricer, Phase 2's sampling rule is still
correctable when TZ-15 writes it. That is the whole reason this TZ is separate from the gate.

The order of a full run is fixed by section 5.1 and asserted by `build`:

     1  host read 1, at the start floor, over the empty set
     2  the six self-tests of section 5.2
     3  `v6` and the static half of `v2_static`
     4  the set, section 3.1, with every assertion of that section
     5  the grids and the domain, section 3.2; host read 2, over the member set
     6  the quote probe: the first 20 members of sections 3.3 and 3.4, timed, fail-fast asserted
     7  sections 3.3 and 3.4 over the remaining members, with both manifest cross-checks
     8  sections 3.5, 3.6 and 3.7 over the parsed bodies; 3.7 item 4 and 3.8 over `gamma.json`
     9  the tables, the disclosure and the observations file
    10  host read 3, and V9's four assertions between read 1 and read 3

There is no gate here. This TZ admits nothing, disqualifies nothing and closes nothing.
"""

import os                                                                  # noqa: E402

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import ast                                                                 # noqa: E402
import collections                                                         # noqa: E402
import gzip                                                                # noqa: E402
import hashlib                                                             # noqa: E402
import importlib.util                                                      # noqa: E402
import json                                                                # noqa: E402
import math                                                                # noqa: E402
import re                                                                  # noqa: E402
import resource                                                            # noqa: E402
import shutil                                                              # noqa: E402
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


# Section 5.1: TZ-12's instrument loads TZ-11a's, which loads TZ-10b's, which loads the other
# three. Every committed module comes through that one object; loading any of them a second time
# would be two module objects with two copies of every table. `tz12` itself is loaded because
# self-test 5 reads `tz12.TEST2_SHA256` and section 6 reads `tz12.SESSION_CEILING_S`.
tz12 = _load("tz12sizedgate", "tz12-sized-gate.py")
tz11a = tz12.tz11a
tz10b = tz12.tz10b
tz07b = tz12.tz07b
tz06 = tz12.tz06
pfair = tz12.pfair
D = pfair.D
config = pfair.config
load_manifests = tz12.load_manifests

import analyze                                                             # noqa: E402
import manifest                                                            # noqa: E402

# ---- section 3.1: the set ----------------------------------------------------------

# The first 1,200 qualifying slots with `T0` after this instant. The instant is chosen so the walk
# opens at 1789206900 — the first unit TZ-05a considered and the first interval whose tau = 240
# checkpoint falls at or after the Tier C restart on 4216c04.
SET_NEED = 1200
SET_AFTER = 1789206600
FIRST_T0_MIN = 1789206900

# Section 3.0: the two tau partitions. `ADMITTED` is the five tau Phase 1 did not disqualify
# inside the pricer's domain; `OUTSIDE` is reported in the same tables in a separately headed
# block and supports no Phase 2 or Phase 3 claim.
ADMITTED = (240, 180, 120, 90, 60)
OUTSIDE = (30, 10)

# Section 3.0's re-derived row counts, asserted in `build`.
CHECKPOINTS = SET_NEED * len(config.QUOTE_TAUS)
CHECKPOINTS_ADMITTED = SET_NEED * len(ADMITTED)
READS_COMPLETE = CHECKPOINTS * config.TOKENS_PER_MARKET

# Section 5.2 item 1: `config.quote_checkpoint_epoch(1789206900, tau)` at the seven tau. Computed
# by the Architect as `t0 + 300 - tau` and cross-checked against the `t` values `config.py`'s own
# docstring states, {60, 120, 180, 210, 240, 270, 290}.
SELFTEST_T0 = 1789206900
CHECKPOINT_EPOCHS = (1789206960, 1789207020, 1789207080, 1789207110,
                     1789207140, 1789207170, 1789207190)

# Section 3.0: the `Q` summary. Nearest-rank on the sorted values.
QUANTILES = ("0.25", "0.50", "0.75", "0.90", "0.99")

# Section 3.6 item 3: cumulative size within k ticks of the executable touch.
KS = (0, 1, 2, 5)

# Section 3.6: the venue's own minimum order size where every reply carries one, and otherwise
# map section 6's TZ-05a measurement. Section 3.5 item 7: the tick where the reply carries none.
MIN_SIZE_FALLBACK = D("5")
TICK_FALLBACK = D("0.01")

# CANON section 1.1: fee = shares * 0.07 * p * (1 - p). Per share, in probability units.
FEE_RATE = D("0.07")
FEE_POINTS = (("0.50", "0.0175"), ("0.85", "0.008925"), ("0.90", "0.0063"))

# Probability points: one point is one hundredth of a probability.
PP = D("100")

# Section 3.4: one second in milliseconds, and the two counted thresholds.
OFFSET_SLOW_MS = 1000.0

# Section 6: the enforced probe and the projection, both resource guards on wall-clock time.
PROBE_MEMBERS = 20
PROBE_LIMIT_S = 4.0
PROJECTION_TAIL_S = 40.0
PROJECTION_LIMIT_S = 1200.0

# Section 5.2 item 5: the call shape of `tz06.scoring_set`, against a committed artifact.
TEST2_NEED = 400
TEST2_AFTER = 1789296300

# V9 and section 5.2 item 6: everything this instrument can write.
WORK_ROOT = "/root/tz14-work"
SELFTEST_DIR = os.path.join(WORK_ROOT, "selftest")

# V2 and V9: the only file names this instrument itself opens under the capture root. The
# settled document is not among them and cannot be: the audit hook below asserts the set of
# basenames this file's own frames open under `config.ROOT` is a subset of this list, which is
# a stronger statement than a count of zero against one name and needs no literal naming of a
# document section 2 item 7 bars this instrument from reading. Every open of that document
# during a run comes from `analyze.venue` inside `tz06.qualification`, and the hook records the
# calling source file of every open under the capture so the report can show exactly that.
CAPTURE_OPENS_ALLOWED = ("quotes.jsonl.gz", "quotes.jsonl", "gamma.json")

# Section 3.8: the market-document keys Phase 3 will need, and the two case-insensitive families.
GAMMA_KEYS = ("orderPriceMinTickSize", "outcomes", "clobTokenIds", "outcomePrices", "closed")
GAMMA_FAMILIES = (("fee", re.compile("fee", re.I)), ("reward", re.compile("reward", re.I)))

# Section 3.5 item 6: the scalar fields of the reply, present/absent and their distinct values.
BODY_FIELDS = ("tick_size", "min_order_size", "timestamp", "hash", "market", "asset_id")
# Above this many distinct values a field is reported by its cardinality and three examples
# rather than value by value. A reading, recorded in the report.
DISTINCT_LIST_MAX = 20

# Section 3.7 item 4: the two outcome strings, in the order `analyze.venue` reads them.
UP = "Up"
DOWN = "Down"

CSV_HEADER = ["T0", "tau", "token_id", "outcome", "status", "recv_ns", "offset_ms",
              "bid_levels", "ask_levels", "best_bid", "best_ask", "bid5", "ask5",
              "cum_bid_k0", "cum_bid_k1", "cum_bid_k2", "cum_bid_k5",
              "cum_ask_k0", "cum_ask_k1", "cum_ask_k2", "cum_ask_k5",
              "venue_timestamp", "sigma_hat", "admissible"]

# V2 and V9, run time: every open of a path under the capture root, with the mode it was opened
# in and the source file of the frame that opened it. Nothing is ever written back into it.
CAPTURE_OPENS = []


STDLIB = os.path.dirname(os.__file__)


def _caller():
    """The nearest frame outside the standard library that led to this open.

    `gzip.open` calls `builtins.open` from inside `gzip.py`, so the immediate frame names the
    standard library and not the reader. Walking out of it attributes each open to the code
    that asked for the file, which is what V2's allow-list and V9's mode proof are about.
    """
    depth = 2                    # 0 is this helper, 1 is the hook that called it
    while depth < 40:
        try:
            frame = sys._getframe(depth)
        except ValueError:
            return "?"
        name = frame.f_code.co_filename
        if not name.startswith(STDLIB) and not name.startswith("<"):
            return name
        depth += 1
    return "?"


def _audit(event, args):
    """Record every open under the capture root: its basename, its mode and its caller."""
    if event != "open" or not args or not isinstance(args[0], str):
        return
    if not os.path.abspath(args[0]).startswith(config.ROOT + os.sep):
        return
    mode = args[1] if len(args) > 1 and isinstance(args[1], str) else "?"
    CAPTURE_OPENS.append((os.path.basename(args[0]), mode, _caller()))


sys.addaudithook(_audit)


# ---- V1, V8 and V10: the fingerprint gate, asserted in the instrument ----------------

# The revision and the six anchors this TZ's own header requires. They are literals here and
# the map is read: a gate never reads its own expected values.
REQUIRED_REVISION = "2026-09-18-b"
REQUIRED_ANCHORS = (("A1", "229a944f2d51"), ("A2", "6c5089330629"),
                    ("A3", "0-complete / 1-student-5tau-not-disqualified / 2-not-started"),
                    ("A4", "437b45ea196b"), ("A5", "9fd1c7de0f74"),
                    ("A6", "729f0bcdbee3"))
# The four anchors that are the first 12 hex characters of a committed file's SHA-256, so the
# instrument can re-derive them from the bytes instead of trusting the table that prints them.
ANCHOR_FILES = (("A2", "research/twap-divergence.py"),
                ("A4", "BTC-EXECUTOR-INSTRUCTIONS.md"),
                ("A5", "research/recorder/recorder.py"),
                ("A6", "research/pfair.py"))
MAP_PATH = os.path.join(HERE, os.pardir, "SYSTEM-MAP.md")
PFAIR_PATH = "research/pfair.py"


def _sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def _map_text():
    with open(MAP_PATH, encoding="utf-8") as fh:
        return fh.read()


def fingerprint_rows():
    """Every row of map section 0's fingerprint table, as the map holds it."""
    rows = []
    for line in _map_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 5 or not cells[0].startswith("`"):
            continue
        path, state, digest = cells[0].strip("`"), cells[3], cells[4].strip("`")
        if state in ("frozen", "tracked", "reported"):
            rows.append({"path": path, "state": state,
                         "expected": digest if state == "frozen" else None})
    return rows


def v1_gates():
    """V1 and V10: the revision, the six anchors and every row of the fingerprint table.

    The map is read and the files are hashed; the TZ's required values are the literals above.
    Any `frozen` mismatch raises, which is the BLOCKED the TZ asks for.
    """
    text = _map_text()
    assert ("**Revision string:** `%s`" % REQUIRED_REVISION) in text,         "section 0.1: the map does not carry revision %s" % REQUIRED_REVISION
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
    rows, frozen, tracked = [], 0, 0
    for row in fingerprint_rows():
        full = os.path.join(HERE, os.pardir, row["path"])
        with open(full, "rb") as fh:
            body = fh.read()
        entry = {"path": row["path"], "state": row["state"],
                 "lines": body.count(b"\n"), "bytes": len(body),
                 "sha256": hashlib.sha256(body).hexdigest(), "expected": row["expected"]}
        if row["state"] == "frozen":
            assert entry["sha256"] == row["expected"], \
                "section 0.1: %s hashes to %s, not %s" % (row["path"], entry["sha256"],
                                                          row["expected"])
            frozen += 1
        elif row["state"] == "tracked":
            tracked += 1
        rows.append(entry)
    assert frozen == 20, "section 0.1: %d frozen rows, not 20" % frozen
    assert tracked == 2, "section 0.1: %d tracked rows, not 2" % tracked
    return {"revision": REQUIRED_REVISION, "anchors_matched": matched,
            "anchors_derived": derived, "rows": rows, "frozen": frozen, "tracked": tracked}


def v8(before):
    """V8: `research/pfair.py` is byte-identical at run end to what it was at run start.

    The expected value is the map's own `frozen` row, read at run time, so the instrument
    carries no copy of a hash it is checking.
    """
    expected = None
    for row in fingerprint_rows():
        if row["path"] == PFAIR_PATH:
            expected = row["expected"]
    after = _sha256_file(os.path.join(HERE, os.pardir, PFAIR_PATH))
    assert expected is not None, "V8: the map has no frozen row for %s" % PFAIR_PATH
    assert before == expected, "V8: %s was %s at run start" % (PFAIR_PATH, before)
    assert after == expected, "V8: %s is %s at run end" % (PFAIR_PATH, after)
    return {"path": PFAIR_PATH, "expected": expected, "at_start": before, "at_end": after,
            "ADMIT": {tau: str(pfair.ADMIT[tau]) for tau in pfair.TAUS},
            "taus": len(pfair.TAUS)}


# ---- the Q summary, section 3.0 ----------------------------------------------------

def q_summary(values):
    """The minimum, the five nearest-rank quantiles, the maximum, and the count.

    Written once and meant everywhere section 3 says "as the `Q` summary". The nearest-rank
    rule takes the ceil(q * n)-th smallest value, so every figure printed is an observation
    and not an interpolation between two of them.
    """
    ordered = sorted(values)
    out = {"n": len(ordered)}
    if not ordered:
        out["min"] = out["max"] = None
        for q in QUANTILES:
            out[q] = None
        return out
    out["min"], out["max"] = ordered[0], ordered[-1]
    for q in QUANTILES:
        rank = max(1, int(math.ceil(float(q) * len(ordered))))
        out[q] = ordered[rank - 1]
    return out


def utc(epoch):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(epoch))


def weekday_of(t0):
    """The UTC weekday name of an interval's opening second."""
    return time.strftime("%a", time.gmtime(t0))


def is_weekend(t0):
    return weekday_of(t0) in ("Sat", "Sun")


# ---- section 3.1: the set ----------------------------------------------------------

def the_set(manifests):
    """The first `SET_NEED` qualifying slots with `T0` after `SET_AFTER`, and nothing else.

    Qualification is `tz06.qualification`'s own committed rule and is not restated here.
    `quotes_complete` is not a membership condition and is not made one: the rate at which the
    quote capture is complete is the first thing this TZ measures.
    """
    rows, ok = tz06.scoring_set(manifests, SET_NEED, after=SET_AFTER)
    members = [r["T0"] for r in rows if r["member"]]
    if not ok:
        last = max(int(name) for name in os.listdir(os.path.join(config.ROOT, config.SERIES)))
        raise SystemExit(
            "BLOCKED at section 0.6: %d of %d slots with T0 > %d qualify; %d units considered, "
            "first %d, last examined %d, last slot on disk %d"
            % (len(members), SET_NEED, SET_AFTER, len(rows), rows[0]["T0"] if rows else -1,
               rows[-1]["T0"] if rows else -1, last))
    assert ok, "section 3.1: the walk did not return a full set"
    assert len(members) == SET_NEED, "section 3.1: %d members" % len(members)
    assert members[0] >= FIRST_T0_MIN, "section 3.1: first member %d" % members[0]
    assert all(t0 % config.INTERVAL_S == 0 for t0 in members), "section 3.1: off the 300 s grid"
    assert all(b > a for a, b in zip(members, members[1:])), "section 3.1: not increasing"
    days = {}
    for t0 in members:
        days[weekday_of(t0)] = days.get(weekday_of(t0), 0) + 1
    doc = {"considered": len(rows), "members": len(members),
           "sha256": tz07b.member_list_sha(members),
           "first": members[0], "last": members[-1],
           "first_utc": utc(members[0]), "last_utc": utc(members[-1]),
           "span_days": (members[-1] - members[0]) / 86400.0,
           "weekday_counts": days,
           "weekend_members": sum(1 for t0 in members if is_weekend(t0)),
           "non_members": [{"T0": r["T0"], "reasons": r["reasons"]}
                           for r in rows if not r["member"]]}
    return rows, members, doc


# ---- section 3.2: the domain, from the pricer's scale and nothing else --------------

def domain(members):
    """`sigma_hat` at each of `pfair.TAUS` per member, and the admissible lists from it.

    `tz10b.grid_of` asserts the one-second grid over [T0-300, T0+300] is whole and raises when
    it is not. The committed set rule admits a member on its manifest and on two `chainlink`
    reports, not on a whole grid, so the two can disagree. A member that raises is caught,
    listed and excluded from this section's tables and from nothing else: its quote rows are
    read and reported exactly like any other member's.
    """
    walked, raised = {}, []
    for t0 in members:
        try:
            grid = tz10b.grid_of(pfair.merged_stream(t0, config.S3_STREAM), t0)
        except AssertionError as exc:
            raised.append({"T0": t0, "why": str(exc)})
            continue
        walked[t0] = {tau: {"sigma_hat": tz10b.sigma_hat_of(grid, tau)}
                      for tau in pfair.TAUS}
    whole = [t0 for t0 in members if t0 in walked]
    admissible = tz11a.admissible_members(walked, whole, pfair.ADMIT)
    per_tau = {}
    for tau in pfair.TAUS:
        listed = admissible[tau]
        per_tau[tau] = {
            "admissible": len(listed),
            "sha256": tz07b.member_list_sha(listed),
            "members": listed,
            "admit": str(pfair.ADMIT[tau]),
            "weekday": sum(1 for t0 in listed if not is_weekend(t0)),
            "weekend": sum(1 for t0 in listed if is_weekend(t0)),
            "sigma_hat": q_summary([float(walked[t0][tau]["sigma_hat"]) for t0 in whole]),
        }
    doc = {"grid_whole": len(whole), "grid_raised": len(raised), "raised": raised,
           "grid_whole_share": len(whole) / float(len(members)) if members else None,
           "grid_whole_weekday": sum(1 for t0 in whole if not is_weekend(t0)),
           "grid_whole_weekend": sum(1 for t0 in whole if is_weekend(t0)),
           "per_tau": per_tau}
    return walked, set(whole), {tau: set(admissible[tau]) for tau in pfair.TAUS}, doc


# ---- section 3.3: the quote file, read for the first time ---------------------------

def quote_lines(dirpath):
    """Every line of one interval's quote file, as the recorder wrote it.

    Located exactly as the recorder's own reader locates it, through `manifest._stream_path`,
    which prefers the `.gz` and falls back to the plain `.jsonl`. The skipping rule is
    `manifest._quote_reads`'s, line for line: a line that does not parse, or that lacks
    `recv_ns` or `tau`, is counted torn and dropped. This reader exists only because
    `_quote_reads` discards `raw`, and V4 asserts the two agree on every field both produce.
    """
    path = manifest._stream_path(dirpath, config.QUOTES_STEM)
    out = {"path": path, "present": os.path.exists(path), "reads": [], "torn": 0}
    if not out["present"]:
        return out
    opener = gzip.open if path.endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                recv_ns, tau = rec["recv_ns"], rec["tau"]
            except (ValueError, KeyError, TypeError):
                out["torn"] += 1
                continue
            body = rec.get("raw")
            try:
                json.loads(body)
                body_is_json = True
            except (ValueError, TypeError):
                body_is_json = False
            out["reads"].append({"recv_ns": recv_ns, "mono_ns": rec.get("mono_ns"),
                                 "tau": tau, "token_id": str(rec.get("token_id")),
                                 "status": rec.get("status"), "raw": body,
                                 "error": rec.get("error"), "body_is_json": body_is_json})
    return out


def _multiset(reads):
    """The four fields both readers produce, as a multiset. V4 compares these."""
    return collections.Counter((r["tau"], r["token_id"], r["status"], r["body_is_json"])
                               for r in reads)


def integrity(dirpath, doc):
    """V4 and section 3.3: the instrument's reader against the committed one, member by member.

    `manifest._quote_reads` is called on the same directory and the multiset of
    `(tau, token_id, status, body_is_json)` it returns must equal this instrument's. A
    disagreement is BLOCKING.
    """
    theirs = _multiset(manifest._quote_reads(dirpath))
    mine = _multiset(doc["reads"])
    return theirs == mine, theirs, mine


# ---- section 3.4: the read geometry -------------------------------------------------

def geometry(t0, reads, man):
    """`offset_ms` per read, against the value the member's own manifest already carries.

    The expression is the manifest's own, term for term, so equality is exact where both sides
    describe the same read. A value disagreement where both sides exist is BLOCKING: it is the
    one place this TZ can discover that the manifest and the file disagree about what was
    captured. A member whose manifest carries no `quote_offsets_ms` key at all is listed,
    excluded from this comparison with its reason, counted, and is not BLOCKING.
    """
    for r in reads:
        r["offset_ms"] = ((r["recv_ns"]
                           - config.quote_checkpoint_epoch(t0, r["tau"]) * 10 ** 9) / 1e6)
    if "quote_offsets_ms" not in man:
        return {"compared": False, "why": "manifest carries no quote_offsets_ms key",
                "disagreements": [], "only_mine": [], "only_theirs": []}
    theirs, mine = collections.defaultdict(list), collections.defaultdict(list)
    for q in man["quote_offsets_ms"]:
        theirs[(q["tau"], str(q["token_id"]), q["status"])].append(q["offset_ms"])
    for r in reads:
        mine[(r["tau"], r["token_id"], r["status"])].append(r["offset_ms"])
    bad, only_mine, only_theirs = [], [], []
    for key in set(theirs) | set(mine):
        a, b = sorted(theirs.get(key, [])), sorted(mine.get(key, []))
        if not theirs.get(key):
            only_mine.append({"T0": t0, "key": list(key), "mine": b})
        elif not mine.get(key):
            only_theirs.append({"T0": t0, "key": list(key), "theirs": a})
        elif a != b:
            bad.append({"T0": t0, "key": list(key), "theirs": a, "mine": b})
    return {"compared": True, "disagreements": bad,
            "only_mine": only_mine, "only_theirs": only_theirs}


# ---- section 3.5: the book, measured and not assumed --------------------------------

def book_of(raw):
    """One reply body, with every price and size carried in `Decimal` from its string.

    Nothing about the payload's shape is assumed: the top-level key set is returned as it was
    found, each side is returned as the list of levels it held in the order it held them, and
    a level whose price or size is missing or not a number is counted rather than guessed at.
    """
    body = json.loads(raw)
    out = {"keys": tuple(sorted(body.keys())) if isinstance(body, dict) else None,
           "ok": isinstance(body, dict), "bad_levels": 0}
    if not out["ok"]:
        out["bids"], out["asks"] = [], []
        return out
    for side in ("bids", "asks"):
        levels, raw_side = [], body.get(side)
        if isinstance(raw_side, list):
            for lv in raw_side:
                try:
                    levels.append((D(str(lv["price"])), D(str(lv["size"]))))
                except (KeyError, TypeError, ValueError, ArithmeticError):
                    out["bad_levels"] += 1
        out[side] = levels
        out[side + "_present"] = isinstance(raw_side, list)
    for field in BODY_FIELDS:
        out[field] = body.get(field) if field in body else None
        out[field + "_present"] = field in body
    return out


def _ordering(levels):
    """Ascending, descending or neither, by price, over a side as it was found."""
    if len(levels) < 2:
        return "single" if levels else "empty"
    prices = [p for p, _ in levels]
    if all(b > a for a, b in zip(prices, prices[1:])):
        return "ascending"
    if all(b < a for a, b in zip(prices, prices[1:])):
        return "descending"
    return "neither"


def best_of(book):
    """The best bid and the best ask, as `max` over `bids` and `min` over `asks`.

    Never from position 0: the ordering of a side is a measurement in section 3.5 item 2 and
    not a dependency of any number this TZ prints. Self-test 2 fixes that.
    """
    bid = max((p for p, _ in book["bids"]), default=None)
    ask = min((p for p, _ in book["asks"]), default=None)
    return bid, ask


def touch_of(book, min_size, tick):
    """The executable touch and the size standing within k ticks of it.

    `bid5` is the highest bid price whose size at that price is at least `min_size`, `ask5` the
    lowest such ask. The cumulative size at k is the sum over every level between the touch and
    k ticks behind it - for bids, priced at or above `bid5 - k * tick` and at or below `bid5`.
    """
    bid5 = max((p for p, s in book["bids"] if s >= min_size), default=None)
    ask5 = min((p for p, s in book["asks"] if s >= min_size), default=None)
    cum = {"bid": {}, "ask": {}}
    for k in KS:
        if bid5 is None:
            cum["bid"][k] = None
        else:
            cum["bid"][k] = sum((s for p, s in book["bids"]
                                 if bid5 - k * tick <= p <= bid5), D(0))
        if ask5 is None:
            cum["ask"][k] = None
        else:
            cum["ask"][k] = sum((s for p, s in book["asks"]
                                 if ask5 <= p <= ask5 + k * tick), D(0))
    band = (ask5 - bid5) if (bid5 is not None and ask5 is not None) else None
    return {"bid5": bid5, "ask5": ask5, "band": band, "cum": cum}


# ---- section 3.6: executability -----------------------------------------------------

def fee_pp(p):
    """CANON section 1.1's taker fee for one share, in probability units, in exact decimal.

    CANON publishes `fee = shares * 0.07 * p * (1 - p)` and three points of it: 1.75, 0.89 and
    0.63 probability points at p of 0.50, 0.85 and 0.90. Self-test 4 fixes this against them.
    """
    return FEE_RATE * p * (D(1) - p)


def round_trip(bid5, ask5):
    """`(ask5 - bid5) + fee(ask5) + fee(bid5)`, in probability units.

    The single number that decides whether a Phase 3 can exist. It is a function of the quotes
    alone and is reported here rather than asserted against anything.
    """
    if bid5 is None or ask5 is None:
        return None
    return (ask5 - bid5) + fee_pp(ask5) + fee_pp(bid5)


# ---- section 3.7 item 4 and section 3.8: the market document -------------------------

def documents(t0):
    """One member's `gamma.json`, read as the recorder reads it.

    `clobTokenIds` is parsed as JSON and indexed against `outcomes`, index by index. The Up
    token is `clobTokenIds[i]` where `outcomes[i] == "Up"` - the same string `analyze.venue`
    turns into its own flag, and the mapping TZ-04b validated at 200 of 200. No settled
    document is opened to establish it and no token is identified by position.
    """
    path = os.path.join(config.interval_dir(t0), "gamma.json")
    out = {"T0": t0, "present": os.path.exists(path), "tokens": {}, "outcomes": None,
           "usable": False, "why": None, "keys": (), "fields": {}, "families": {},
           "raw_fields": {}}
    if not out["present"]:
        out["why"] = "no gamma.json"
        return out
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    market = doc[0] if isinstance(doc, list) else doc
    if not isinstance(market, dict):
        out["why"] = "gamma.json is not an object"
        return out
    out["keys"] = tuple(sorted(market.keys()))
    for key in GAMMA_KEYS:
        out["fields"][key] = (key in market, market.get(key))
    for name, pattern in GAMMA_FAMILIES:
        out["families"][name] = tuple(sorted(k for k in market if pattern.search(k)))
        for key in out["families"][name]:
            out["raw_fields"][key] = market.get(key)
    outcomes, ids = market.get("outcomes"), market.get("clobTokenIds")
    try:
        outcomes = json.loads(outcomes) if isinstance(outcomes, str) else outcomes
        ids = json.loads(ids) if isinstance(ids, str) else ids
    except ValueError:
        out["why"] = "outcomes or clobTokenIds is not JSON"
        return out
    out["outcomes"] = tuple(outcomes) if isinstance(outcomes, list) else None
    if not isinstance(outcomes, list) or not isinstance(ids, list) \
            or len(outcomes) != 2 or len(ids) != 2 or sorted(outcomes) != sorted([UP, DOWN]):
        out["why"] = "outcomes is not a two-element Up/Down array"
        return out
    out["tokens"] = {str(ids[i]): outcomes[i] for i in range(2)}
    out["usable"] = True
    return out


def pairs(rows, docs):
    """Section 3.7: the two tokens of one checkpoint, where both returned a parseable 200.

    The population is exactly that - a checkpoint counts as paired on the two replies, not on
    what is in them. A sum whose input does not exist, because a side of one book is empty, is
    not computed at that checkpoint and the count of such checkpoints is reported beside the
    statistic rather than removed from the denominator in silence.

    A member whose `outcomes` is not a two-element Up/Down array is excluded from these tables
    and counted; nothing here is keyed by an outcome the venue settled, only by which of the
    two tokens the market document calls Up.
    """
    by_cp = collections.defaultdict(dict)
    for r in rows:
        if r["status"] == 200 and r["bid_levels"] is not None and r["outcome"] in (UP, DOWN):
            by_cp[(r["T0"], r["tau"])][r["outcome"]] = r
    out = {"paired": collections.Counter(), "bid_sum": collections.defaultdict(list),
           "ask_sum": collections.defaultdict(list), "mid_gap": collections.defaultdict(list),
           "bid5_sum": collections.defaultdict(list), "ask5_sum": collections.defaultdict(list),
           "bid_over": [], "ask_under": [], "free_lunch": [],
           "undefined": collections.Counter(),
           "excluded_members": sorted(d["T0"] for d in docs.values() if not d["usable"])}
    for (t0, tau), pair in sorted(by_cp.items()):
        if UP not in pair or DOWN not in pair:
            continue
        up, down = pair[UP], pair[DOWN]
        out["paired"][tau] += 1
        if up["best_bid"] is not None and down["best_bid"] is not None:
            bid_sum = up["best_bid"] + down["best_bid"]
            out["bid_sum"][tau].append(bid_sum)
            if bid_sum > D(1):
                out["bid_over"].append({"T0": t0, "tau": tau, "sum": str(bid_sum)})
        else:
            out["undefined"]["bid_sum"] += 1
        if up["best_ask"] is not None and down["best_ask"] is not None:
            ask_sum = up["best_ask"] + down["best_ask"]
            out["ask_sum"][tau].append(ask_sum)
            if ask_sum < D(1):
                out["ask_under"].append({"T0": t0, "tau": tau, "sum": str(ask_sum)})
        else:
            out["undefined"]["ask_sum"] += 1
        if up["mid"] is not None and down["mid"] is not None:
            out["mid_gap"][tau].append(up["mid"] - (D(1) - down["mid"]))
        else:
            out["undefined"]["mid_gap"] += 1
        if up["bid5"] is not None and down["bid5"] is not None:
            s5 = up["bid5"] + down["bid5"]
            out["bid5_sum"][tau].append(s5)
            if s5 > D(1):
                size = min(up["cum_bid"][0], down["cum_bid"][0])
                profit = s5 - D(1) - fee_pp(up["bid5"]) - fee_pp(down["bid5"])
                out["free_lunch"].append({"T0": t0, "tau": tau, "side": "bid",
                                          "sum": str(s5), "size": str(size),
                                          "profit_pp": str(profit * PP)})
        else:
            out["undefined"]["bid5_sum"] += 1
        if up["ask5"] is not None and down["ask5"] is not None:
            s5 = up["ask5"] + down["ask5"]
            out["ask5_sum"][tau].append(s5)
            if s5 < D(1):
                size = min(up["cum_ask"][0], down["cum_ask"][0])
                profit = D(1) - s5 - fee_pp(up["ask5"]) - fee_pp(down["ask5"])
                out["free_lunch"].append({"T0": t0, "tau": tau, "side": "ask",
                                          "sum": str(s5), "size": str(size),
                                          "profit_pp": str(profit * PP)})
        else:
            out["undefined"]["ask5_sum"] += 1
    return out


# ---- section 5.2: six self-tests, before the capture is touched ----------------------

def _synthetic_book(bids, asks):
    """A reply body composed here and carried through `book_of`, exactly as a real one is."""
    return book_of(json.dumps({"bids": [{"price": p, "size": s} for p, s in bids],
                               "asks": [{"price": p, "size": s} for p, s in asks]}))


def selftests():
    """Six items, thirty-six assertions, all before anything is read from the capture."""
    out, n = [], 0

    # 1. The checkpoint grid the capture and the pricer share. Eight assertions.
    assert config.QUOTE_TAUS == pfair.TAUS, \
        "self-test 1: %r != %r" % (config.QUOTE_TAUS, pfair.TAUS)
    n += 1
    got = []
    for tau, want in zip(config.QUOTE_TAUS, CHECKPOINT_EPOCHS):
        have = config.quote_checkpoint_epoch(SELFTEST_T0, tau)
        assert have == want, "self-test 1: tau %d gives %d, not %d" % (tau, have, want)
        n += 1
        got.append(have)
    out.append("1. config.QUOTE_TAUS == pfair.TAUS == %r; quote_checkpoint_epoch(%d, tau) = %r"
               % (config.QUOTE_TAUS, SELFTEST_T0, tuple(got)))

    # 2. The best price does not depend on order. Twelve assertions.
    up4 = [("0.49", "1"), ("0.50", "1"), ("0.51", "1"), ("0.52", "1")]
    ask3 = [("0.53", "1"), ("0.54", "1"), ("0.55", "1")]
    shuffled = [up4[2], up4[0], up4[3], up4[1]]
    shuffled_asks = [ask3[1], ask3[2], ask3[0]]
    books = [_synthetic_book(up4, ask3),
             _synthetic_book(up4[::-1], ask3[::-1]),
             _synthetic_book(shuffled, shuffled_asks),
             _synthetic_book([("0.52", "1")], [("0.53", "1")])]
    for i, book in enumerate(books):
        bid, ask = best_of(book)
        assert bid == D("0.52"), "self-test 2: book %d best bid %s" % (i, bid)
        assert ask == D("0.53"), "self-test 2: book %d best ask %s" % (i, ask)
        n += 2
    bid, ask = best_of(_synthetic_book([], ask3))
    assert bid is None, "self-test 2: empty bids gave a bid of %s" % bid
    assert ask == D("0.53"), "self-test 2: empty bids gave an ask of %s" % ask
    n += 2
    bid, ask = best_of(_synthetic_book(up4, []))
    assert bid == D("0.52"), "self-test 2: empty asks gave a bid of %s" % bid
    assert ask is None, "self-test 2: empty asks gave an ask of %s" % ask
    n += 2
    out.append("2. best_of returns 0.52 / 0.53 on four orderings and one level a side; "
               "None / 0.53 on empty bids and 0.52 / None on empty asks")

    # 3. The executable touch skips size below the minimum. Six assertions.
    book = _synthetic_book([("0.52", "3"), ("0.51", "10"), ("0.50", "2")],
                           [("0.53", "4"), ("0.54", "9")])
    bid, ask = best_of(book)
    assert bid == D("0.52"), "self-test 3: best bid %s" % bid
    assert ask == D("0.53"), "self-test 3: best ask %s" % ask
    n += 2
    touch = touch_of(book, D("5"), D("0.01"))
    assert touch["bid5"] == D("0.51"), "self-test 3: bid5 %s" % touch["bid5"]
    assert touch["ask5"] == D("0.54"), "self-test 3: ask5 %s" % touch["ask5"]
    assert touch["band"] == D("0.03"), "self-test 3: band %s" % touch["band"]
    assert touch["cum"]["bid"][1] == D("12"), "self-test 3: cum %s" % touch["cum"]["bid"][1]
    n += 4
    out.append("3. best 0.52 / 0.53; bid5 0.51, ask5 0.54, band exactly Decimal('0.03'), "
               "cumulative bid size at k=1 exactly 12")

    # 4. The fee in probability points, against CANON section 1.1's own three points.
    shown = []
    for p, want in FEE_POINTS:
        have = fee_pp(D(p))
        assert have == D(want), "self-test 4: fee_pp(%s) = %s, not %s" % (p, have, want)
        n += 1
        shown.append("%s -> %s (%s pp)" % (p, have, have * PP))
    out.append("4. " + "; ".join(shown))

    # 5. The set-formation call shape, against a committed artifact.
    rows, _ok = tz06.scoring_set(load_manifests(), TEST2_NEED, after=TEST2_AFTER)
    sha = tz07b.member_list_sha([r["T0"] for r in rows if r["member"]])
    assert sha == tz12.TEST2_SHA256, "self-test 5: %s != %s" % (sha, tz12.TEST2_SHA256)
    n += 1
    out.append("5. scoring_set(manifests, %d, after=%d) hashes to %s == tz12.TEST2_SHA256"
               % (TEST2_NEED, TEST2_AFTER, sha))

    # 6. The instrument's reader agrees with the committed one, on a directory it writes itself.
    if os.path.exists(SELFTEST_DIR):
        shutil.rmtree(SELFTEST_DIR)
    os.makedirs(SELFTEST_DIR)
    body_a = '{"bids":[{"price":"0.41","size":"7"}],"asks":[{"price":"0.44","size":"9"}]}'
    body_b = '{"bids":[{"price":"0.30","size":"11"}],"asks":[{"price":"0.35","size":"2"}]}'
    lines = [
        json.dumps({"recv_ns": 1, "mono_ns": 1, "tau": 240, "token_id": "AAA",
                    "status": 200, "raw": body_a}),
        json.dumps({"recv_ns": 2, "mono_ns": 2, "tau": 180, "token_id": "BBB",
                    "status": 200, "raw": body_b}),
        json.dumps({"recv_ns": 3, "mono_ns": 3, "tau": 120, "token_id": "AAA",
                    "status": 503, "raw": "service unavailable"}),
        '{"recv_ns": 4, "mono_ns": 4, "tau": 90, "token_id": "BB',
    ]
    with open(os.path.join(SELFTEST_DIR, config.QUOTES_STEM + ".jsonl"), "wt",
              encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    doc = quote_lines(SELFTEST_DIR)
    theirs = _multiset(manifest._quote_reads(SELFTEST_DIR))
    mine = _multiset(doc["reads"])
    assert theirs == mine, "self-test 6: %r != %r" % (theirs, mine)
    assert len(doc["reads"]) == 3, "self-test 6: %d entries" % len(doc["reads"])
    ordered = sorted(doc["reads"], key=lambda r: r["recv_ns"])
    assert [r["body_is_json"] for r in ordered] == [True, True, False], \
        "self-test 6: body_is_json %r" % [r["body_is_json"] for r in ordered]
    assert ordered[0]["raw"] == body_a, "self-test 6: the first raw body changed"
    assert ordered[1]["raw"] == body_b, "self-test 6: the second raw body changed"
    n += 5
    shutil.rmtree(SELFTEST_DIR)
    assert not os.path.exists(SELFTEST_DIR), "self-test 6: the directory outlived the test"
    n += 1
    out.append("6. both readers give the same 3-entry multiset %r; body_is_json true, true, "
               "false in recv_ns order; both raw bodies byte-identical; the directory is gone"
               % sorted(mine.elements()))
    assert n == 36, "V7: %d assertions, not 36" % n
    return {"items": 6, "assertions": n, "lines": out}


# ---- V2 and V6: the instrument read against its own syntax tree ----------------------

# Section 2 item 6: the twelve probability entry points this file's tree contains no call of.
PFAIR_PROBABILITY = ("p_fair", "p_fair_student", "state_and_sd", "far_branch", "near_branch",
                     "observations", "corrected_sd", "student_sd", "phi", "log_phi",
                     "t_cdf", "log_t_cdf")
# Section 2 item 6: the only `pfair` attributes this file may name.
PFAIR_ALLOWED = ("merged_stream", "reports", "ADMIT", "TAUS", "GATED_TAUS", "D", "MS", "config")
# Section 2 items 7 and 8: named here only so V2 can assert the call count is zero.
NEVER_CALLED = (("tz10b", "m2_labels"), ("tz11a", "walk_member"), ("tz11a", "fit_student"))
# V2, static: no string constant of this file carries any of these.
BANNED_SUBSTRINGS = ("reso" + "lution", "reso" + "lved_up", "priceTo" + "Beat")


def _source():
    return open(os.path.abspath(__file__), encoding="utf-8").read()


def _docstring_nodes(tree):
    """Every string constant that is a docstring, by identity, so V2 can exempt them."""
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
    """V2's static half: this file's own syntax tree, read before the capture is touched."""
    tree = ast.parse(_source())
    exempt = _docstring_nodes(tree)
    strings, carrying = 0, []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) \
                and id(node) not in exempt:
            strings += 1
            if any(bad in node.value for bad in BANNED_SUBSTRINGS):
                carrying.append(node.value)
    calls, probability, never, attrs = 0, [], [], set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            calls += 1
            pair = _dotted(node)
            if pair and pair[0] == "pfair" and pair[1] in PFAIR_PROBABILITY:
                probability.append("%s.%s" % pair)
            if pair and pair in NEVER_CALLED:
                never.append("%s.%s" % pair)
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) \
                and node.value.id == "pfair":
            attrs.add(node.attr)
    assert not carrying, "V2: %d string constants carry a barred name: %r" % \
        (len(carrying), carrying[:3])
    assert not probability, "V2: %r called" % probability
    assert not never, "V2: %r called" % never
    assert attrs <= set(PFAIR_ALLOWED), "V2: pfair attributes named: %r" % sorted(attrs)
    return {"strings_scanned": strings, "strings_carrying": len(carrying),
            "calls_scanned": calls, "probability_calls": len(probability),
            "never_called_calls": len(never), "pfair_attributes": sorted(attrs),
            "pfair_allowed": list(PFAIR_ALLOWED), "docstrings_exempt": len(exempt)}


def v2_runtime():
    """V2's run-time half, from the audit hook: every open under the capture root.

    The count of opens of the settled document by this instrument is zero because the set of
    basenames opened by this file's own frames is a subset of the three this TZ declares, and
    that document is not one of them. Every open of it in the run comes from `analyze.venue`
    inside `tz06.qualification`, which section 2 item 7 names as the one exemption.
    """
    mine = collections.Counter()
    others = collections.Counter()
    modes = collections.Counter()
    for name, mode, caller in CAPTURE_OPENS:
        modes[(os.path.basename(caller), mode)] += 1
        if os.path.abspath(caller) == os.path.abspath(__file__):
            mine[name] += 1
        else:
            others[(os.path.basename(caller), name)] += 1
    assert set(mine) <= set(CAPTURE_OPENS_ALLOWED), \
        "V2: this instrument opened %r under the capture" % sorted(set(mine))
    write_modes = sorted(m for m in modes if any(c in m[1] for c in "wxa+"))
    assert not write_modes, "V9: a path under the capture was opened for writing: %r" % write_modes
    return {"opens_total": len(CAPTURE_OPENS),
            "by_this_instrument": dict(sorted(mine.items())),
            "by_committed_readers": {"%s / %s" % k: v for k, v in sorted(others.items())},
            "settled_document_opens_by_this_instrument": 0,
            "modes": {"%s / %r" % k: v for k, v in sorted(modes.items())},
            "write_modes": write_modes}


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
    scoped = git("status", "--porcelain", "--", "research/tz14-quote-inventory.py",
                 "../CryptoReports/TZ-14-quote-inventory-report.md")
    # Section 5.3: the committed lines this change replaces, read from `origin/main`. The path
    # does not exist there, so the list is empty and the diff is additive in the strict sense.
    at_base = subprocess.run(("git", "show", "%s:research/tz14-quote-inventory.py" % base),
                             cwd=HERE, capture_output=True, text=True)
    replaced = [] if at_base.returncode != 0 else \
        [l for l in at_base.stdout.splitlines()
         if l not in set(_source().splitlines())]
    assert not replaced, "V6: %d replaced lines" % len(replaced)
    return {"head": head, "merge_base": base, "diff_names": names,
            "status_porcelain": scoped, "replaced_lines": replaced,
            "attribute_stores": len(attribute_stores), "globals": len(globals_),
            "nonlocals": len(nonlocals), "environ_writes": sorted(environ),
            "path_at_merge_base": at_base.returncode == 0}


# ---- section 3.4: the timeout, read from the recorder as committed -------------------

def recorder_constant(name):
    """A module-level integer assignment of `research/recorder/recorder.py`, read by `ast`.

    `QUOTE_TIMEOUT_S` is 8, in seconds, and section 3.4 multiplies by 1,000 itself rather than
    carrying an 8,000 that the file does not hold.
    """
    tree = ast.parse(open(os.path.join(HERE, "recorder", "recorder.py"),
                          encoding="utf-8").read())
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name) and node.targets[0].id == name:
            return node.value.value
    raise SystemExit("BLOCKED: recorder.py has no module-level %s" % name)


# ---- steps 6 and 7: one member's quote file, its integrity and its geometry ----------

def read_member(t0, manifests):
    """Sections 3.3 and 3.4 for one member, with both manifest cross-checks."""
    dirpath = config.interval_dir(t0)
    doc = quote_lines(dirpath)
    agree, theirs, mine = integrity(dirpath, doc)
    man = manifests.get(t0) or {}
    geo = geometry(t0, doc["reads"], man)
    seen = collections.Counter((r["tau"], r["token_id"]) for r in doc["reads"])
    recomputed = (len(doc["reads"]) == config.QUOTE_READS_PER_INTERVAL
                  and all(r["status"] == 200 and r["body_is_json"] for r in doc["reads"]))
    return {"T0": t0, "quotes": doc, "agree": agree, "theirs": theirs, "mine": mine,
            "geometry": geo, "duplicate_pairs": [k for k, v in seen.items() if v > 1],
            "quotes_complete_manifest": man.get("quotes_complete"),
            "quotes_complete_recomputed": recomputed,
            "clock_offset_abs_max_ms": man.get("clock_offset_abs_max_ms"),
            "multi_start": isinstance(man.get("recorder_git_sha"), list)}


def book_pass(members, per_member, docs, walked, admissible, timeout_ms):
    """Sections 3.5, 3.6 and 3.7 over the parsed bodies, one member at a time.

    Every price and size is carried in `decimal.Decimal` from its string, never through a
    float. Each body is parsed once here and discarded before the next member, so the run
    holds the raw text of the capture and never the whole book of it.
    """
    rows = []
    stat = {"shapes": collections.Counter(), "shape_example": {},
            "orderings": {"bids": collections.Counter(), "asks": collections.Counter()},
            "levels": {"bids": [], "asks": []},
            "level_counts": {"bids": collections.Counter(), "asks": collections.Counter()},
            "empty": collections.defaultdict(lambda: collections.Counter()),
            "field_present": collections.Counter(), "field_values": {f: collections.Counter()
                                                                     for f in BODY_FIELDS},
            "asset_id_mismatch": [], "crossed": [], "bad_levels": 0,
            "not_object": 0, "unparsed_200": 0, "parsed": 0,
            "spread": collections.defaultdict(list), "ticks": collections.defaultdict(list),
            "tick_absent": 0, "ts_delta": collections.defaultdict(list), "ts_negative": 0,
            "ts_unparsed": 0}
    for t0 in members:
        tokens = docs[t0]["tokens"]
        for r in per_member[t0]["quotes"]["reads"]:
            tau, token = r["tau"], r["token_id"]
            row = {"T0": t0, "tau": tau, "token_id": token,
                   "outcome": tokens.get(token, ""), "status": r["status"],
                   "recv_ns": r["recv_ns"], "offset_ms": r["offset_ms"],
                   "error": r["error"], "body_is_json": r["body_is_json"],
                   "sigma_hat": (walked[t0][tau]["sigma_hat"] if t0 in walked else None),
                   "admissible": (t0 in admissible[tau]) if t0 in walked else None,
                   "bid_levels": None, "ask_levels": None, "best_bid": None, "best_ask": None,
                   "mid": None, "spread": None, "venue_timestamp": None,
                   "tick": None, "tick_present": False, "min_size_present": False,
                   "min_size": None, "t_own": None, "t_fb": None}
            if r["status"] != 200 or not r["body_is_json"]:
                if r["status"] == 200:
                    stat["unparsed_200"] += 1
                rows.append(row)
                continue
            book = book_of(r["raw"])
            if not book["ok"]:
                stat["not_object"] += 1
                rows.append(row)
                continue
            stat["parsed"] += 1
            stat["bad_levels"] += book["bad_levels"]
            stat["shapes"][book["keys"]] += 1
            if book["keys"] not in stat["shape_example"]:
                stat["shape_example"][book["keys"]] = (t0, tau)
            for side in ("bids", "asks"):
                stat["orderings"][side][_ordering(book[side])] += 1
                stat["levels"][side].append(len(book[side]))
                stat["level_counts"][side][len(book[side])] += 1
            if not book["bids"]:
                stat["empty"][tau]["bids"] += 1
            if not book["asks"]:
                stat["empty"][tau]["asks"] += 1
            if not book["bids"] and not book["asks"]:
                stat["empty"][tau]["neither"] += 1
            for field in BODY_FIELDS:
                if book[field + "_present"]:
                    stat["field_present"][field] += 1
                    stat["field_values"][field][str(book[field])] += 1
            if book["asset_id_present"] and str(book["asset_id"]) != token:
                stat["asset_id_mismatch"].append({"T0": t0, "tau": tau, "token_id": token,
                                                  "asset_id": str(book["asset_id"])})
            bid, ask = best_of(book)
            row["bid_levels"], row["ask_levels"] = len(book["bids"]), len(book["asks"])
            row["best_bid"], row["best_ask"] = bid, ask
            if bid is not None and ask is not None:
                row["mid"] = (bid + ask) / D(2)
                row["spread"] = ask - bid
                stat["spread"][tau].append(ask - bid)
                if bid >= ask:
                    stat["crossed"].append({"T0": t0, "tau": tau, "bid": str(bid),
                                            "ask": str(ask)})
            if book["tick_size_present"]:
                row["tick_present"] = True
                row["tick"] = D(str(book["tick_size"]))
            else:
                stat["tick_absent"] += 1
                row["tick"] = TICK_FALLBACK
            if row["spread"] is not None and row["tick"] > 0:
                stat["ticks"][tau].append(row["spread"] / row["tick"])
            if book["min_order_size_present"]:
                row["min_size_present"] = True
                row["min_size"] = D(str(book["min_order_size"]))
            if book["timestamp_present"]:
                try:
                    row["venue_timestamp"] = int(str(book["timestamp"]))
                    delta = r["recv_ns"] / 1e6 - row["venue_timestamp"]
                    stat["ts_delta"][tau].append(delta)
                    if delta < 0:
                        stat["ts_negative"] += 1
                except ValueError:
                    stat["ts_unparsed"] += 1
            own = row["min_size"] if row["min_size"] is not None else MIN_SIZE_FALLBACK
            row["t_own"] = touch_of(book, own, row["tick"])
            row["t_fb"] = (row["t_own"] if own == MIN_SIZE_FALLBACK
                           else touch_of(book, MIN_SIZE_FALLBACK, row["tick"]))
            rows.append(row)
    return rows, stat


def choose_min_size(rows, stat):
    """Section 3.6: `MIN_SIZE` from the reply where every read carries one, else map section 6.

    Both touches were computed in the pass - one at the reply's own `min_order_size` and one at
    the fallback - so the choice made here selects between two measured answers rather than
    sending the run back over the capture a second time.
    """
    parsed = [r for r in rows if r["t_own"] is not None]
    present = sum(1 for r in parsed if r["min_size_present"])
    every = bool(parsed) and present == len(parsed)
    for r in rows:
        touch = r["t_own"] if every else r["t_fb"]
        r["bid5"] = touch["bid5"] if touch else None
        r["ask5"] = touch["ask5"] if touch else None
        r["band"] = touch["band"] if touch else None
        r["cum_bid"] = touch["cum"]["bid"] if touch else {k: None for k in KS}
        r["cum_ask"] = touch["cum"]["ask"] if touch else {k: None for k in KS}
        r["round_trip"] = round_trip(r["bid5"], r["ask5"])
    return {"source": "the reply's own min_order_size" if every
            else "map section 6's TZ-05a measurement, %s" % MIN_SIZE_FALLBACK,
            "from_reply": present, "from_map": len(parsed) - present,
            "reads_parsed": len(parsed), "every_read": every,
            "distinct": dict(stat["field_values"]["min_order_size"])}


def by_tau(rows, key, cast=float, where=None):
    """One column of the observation rows, grouped by `tau`, as the `Q` summary needs it."""
    out = collections.defaultdict(list)
    for r in rows:
        if r[key] is None or (where is not None and not where(r)):
            continue
        out[r["tau"]].append(cast(r[key]))
    return out


def tau_summaries(grouped):
    return {tau: q_summary(grouped.get(tau, [])) for tau in config.QUOTE_TAUS}


def geometry_tables(rows, timeout_ms, per_member, members):
    """Section 3.4's tables: the offsets per tau, the pair skew per checkpoint, the clock."""
    offsets = by_tau(rows, "offset_ms")
    per_cp = collections.defaultdict(list)
    seen = collections.defaultdict(list)
    for r in rows:
        seen[(r["T0"], r["tau"])].append(r["recv_ns"])
    for (t0, tau), recv in seen.items():
        if len(recv) == 2:
            per_cp[tau].append(abs(recv[0] - recv[1]) / 1e6)
    clock = [per_member[t0]["clock_offset_abs_max_ms"] for t0 in members
             if per_member[t0]["clock_offset_abs_max_ms"] is not None]
    return {
        "offsets": tau_summaries(offsets),
        "negative": {tau: sum(1 for v in offsets.get(tau, []) if v < 0)
                     for tau in config.QUOTE_TAUS},
        "over_1s": {tau: sum(1 for v in offsets.get(tau, []) if v > OFFSET_SLOW_MS)
                    for tau in config.QUOTE_TAUS},
        "over_timeout": {tau: sum(1 for v in offsets.get(tau, []) if v > timeout_ms)
                         for tau in config.QUOTE_TAUS},
        "timeout_ms": timeout_ms,
        "pair_skew_ms": tau_summaries(per_cp),
        "clock_offset_max_ms": max(clock) if clock else None,
        "clock_members_reported": len(clock),
        "clock_over_limit": sum(1 for v in clock if v > config.CLOCK_OFFSET_LIMIT_MS),
        "clock_limit_ms": config.CLOCK_OFFSET_LIMIT_MS,
    }


def executability(rows):
    """Section 3.6 items 1 to 5, each per tau and each over the reads of section 3.5."""
    parsed = [r for r in rows if r["t_own"] is not None]
    out = {"no_touch": {tau: 0 for tau in config.QUOTE_TAUS},
           "reads": {tau: 0 for tau in config.QUOTE_TAUS}}
    for r in parsed:
        out["reads"][r["tau"]] += 1
        if r["bid5"] is None or r["ask5"] is None:
            out["no_touch"][r["tau"]] += 1
    out["band_pp"] = tau_summaries(by_tau(parsed, "band", lambda v: float(v * PP)))
    out["round_trip_pp"] = tau_summaries(
        by_tau(parsed, "round_trip", lambda v: float(v * PP)))
    for name, flag in (("weekday", False), ("weekend", True)):
        out["round_trip_pp_" + name] = tau_summaries(
            by_tau(parsed, "round_trip", lambda v: float(v * PP),
                   where=lambda r, f=flag: is_weekend(r["T0"]) == f))
    for name, flag in (("admissible", True), ("not_admissible", False)):
        out["round_trip_pp_" + name] = tau_summaries(
            by_tau(parsed, "round_trip", lambda v: float(v * PP),
                   where=lambda r, f=flag: r["admissible"] is f))
    out["fee_bid5_pp"] = tau_summaries(
        by_tau(parsed, "bid5", lambda v: float(fee_pp(v) * PP)))
    out["fee_ask5_pp"] = tau_summaries(
        by_tau(parsed, "ask5", lambda v: float(fee_pp(v) * PP)))
    out["cum"] = {}
    for side in ("bid", "ask"):
        for k in KS:
            grouped = collections.defaultdict(list)
            for r in parsed:
                v = r["cum_" + side][k]
                if v is not None:
                    grouped[r["tau"]].append(float(v))
            out["cum"]["%s_k%d" % (side, k)] = tau_summaries(grouped)
    return out


def integrity_tables(members, per_member):
    """Section 3.3 items 1 to 8, over the 1,200 members."""
    out = {"no_file": [], "line_counts": collections.Counter(), "over_14": [],
           "dup_members": 0, "dup_pairs": 0, "torn": collections.Counter(),
           "status": collections.Counter(), "errors": collections.Counter(),
           "body_false_200": 0, "complete_agree": 0, "complete_disagree": [],
           "complete_manifest": 0, "complete_recomputed": 0, "multi_start": [],
           "reader_agree": 0, "reader_disagree": []}
    for t0 in members:
        m = per_member[t0]
        reads = m["quotes"]["reads"]
        if not m["quotes"]["present"]:
            out["no_file"].append(t0)
        out["line_counts"][len(reads)] += 1
        if len(reads) > config.QUOTE_READS_PER_INTERVAL:
            out["over_14"].append({"T0": t0, "lines": len(reads)})
        if m["duplicate_pairs"]:
            out["dup_members"] += 1
            out["dup_pairs"] += len(m["duplicate_pairs"])
        if m["quotes"]["torn"]:
            out["torn"][t0] = m["quotes"]["torn"]
        for r in reads:
            out["status"][r["status"]] += 1
            if r["status"] is None and r["error"] is not None:
                out["errors"][str(r["error"])] += 1
            if r["status"] == 200 and not r["body_is_json"]:
                out["body_false_200"] += 1
        if m["quotes_complete_manifest"]:
            out["complete_manifest"] += 1
        if m["quotes_complete_recomputed"]:
            out["complete_recomputed"] += 1
        if m["quotes_complete_manifest"] == m["quotes_complete_recomputed"]:
            out["complete_agree"] += 1
        else:
            out["complete_disagree"].append({"T0": t0,
                                             "manifest": m["quotes_complete_manifest"],
                                             "recomputed": m["quotes_complete_recomputed"]})
        if m["multi_start"]:
            out["multi_start"].append(t0)
        if m["agree"]:
            out["reader_agree"] += 1
        else:
            out["reader_disagree"].append({"T0": t0,
                                           "theirs": sorted(m["theirs"].items())[:4],
                                           "mine": sorted(m["mine"].items())[:4]})
    return out


def book_tables(stat, rows):
    """Section 3.5 items 1 to 8, over the reads at each tau."""
    shapes = []
    for keys, count in stat["shapes"].most_common():
        t0, tau = stat["shape_example"][keys]
        shapes.append({"keys": list(keys), "count": count, "example_T0": t0, "example_tau": tau})
    fields = {}
    for field in BODY_FIELDS:
        values = stat["field_values"][field]
        entry = {"present": stat["field_present"][field],
                 "absent": stat["parsed"] - stat["field_present"][field],
                 "distinct": len(values)}
        if len(values) <= DISTINCT_LIST_MAX:
            entry["values"] = values.most_common()
        else:
            entry["values"] = None
            entry["examples"] = values.most_common(3)
        fields[field] = entry
    return {
        "shapes": shapes,
        "orderings": {side: dict(stat["orderings"][side]) for side in ("bids", "asks")},
        "levels": {side: q_summary(stat["levels"][side]) for side in ("bids", "asks")},
        "level_counts": {side: sorted(stat["level_counts"][side].items())
                         for side in ("bids", "asks")},
        "empty": {tau: dict(stat["empty"][tau]) for tau in config.QUOTE_TAUS},
        "both_sides": {tau: sum(1 for r in rows if r["tau"] == tau
                                and r["best_bid"] is not None and r["best_ask"] is not None)
                       for tau in config.QUOTE_TAUS},
        "spread_pp": tau_summaries({tau: [float(v * PP) for v in vs]
                                    for tau, vs in stat["spread"].items()}),
        "spread_ticks": tau_summaries({tau: [float(v) for v in vs]
                                       for tau, vs in stat["ticks"].items()}),
        "tick_absent": stat["tick_absent"],
        "crossed": stat["crossed"],
        "fields": fields,
        "asset_id_mismatch": stat["asset_id_mismatch"],
        "ts_delta_ms": tau_summaries(stat["ts_delta"]),
        "ts_negative": stat["ts_negative"],
        "ts_unparsed": stat["ts_unparsed"],
        "parsed": stat["parsed"], "not_object": stat["not_object"],
        "unparsed_200": stat["unparsed_200"], "bad_levels": stat["bad_levels"],
    }


def document_tables(members, docs):
    """Section 3.7 item 4 and section 3.8, over the 1,200 market documents."""
    out = {"present": 0, "usable": 0, "unusable": [],
           "outcomes": collections.Counter(), "fields": {}, "families": {}}
    fields = {k: {"present": 0, "values": collections.Counter()} for k in GAMMA_KEYS}
    families = {name: collections.Counter() for name, _ in GAMMA_FAMILIES}
    family_values = {}
    for t0 in members:
        d = docs[t0]
        if d["present"]:
            out["present"] += 1
        if d["usable"]:
            out["usable"] += 1
        else:
            out["unusable"].append({"T0": t0, "why": d["why"]})
        if d["outcomes"] is not None:
            out["outcomes"][d["outcomes"]] += 1
        for key in GAMMA_KEYS:
            here, value = d["fields"].get(key, (False, None))
            if here:
                fields[key]["present"] += 1
                fields[key]["values"][str(value)[:120]] += 1
        for name, _ in GAMMA_FAMILIES:
            families[name][d["families"].get(name, ())] += 1
            for key in d["families"].get(name, ()):
                family_values.setdefault(key, collections.Counter())[
                    str(d["raw_fields"].get(key))[:120]] += 1
    for key in GAMMA_KEYS:
        entry = {"present": fields[key]["present"],
                 "absent": len(members) - fields[key]["present"],
                 "distinct": len(fields[key]["values"])}
        if entry["distinct"] <= DISTINCT_LIST_MAX:
            entry["values"] = fields[key]["values"].most_common()
        else:
            entry["values"] = None
            entry["examples"] = fields[key]["values"].most_common(3)
        out["fields"][key] = entry
    out["families"] = {name: [{"keys": list(k), "count": v}
                              for k, v in families[name].most_common()]
                       for name, _ in GAMMA_FAMILIES}
    out["family_values"] = {key: {"present": sum(counts.values()),
                                  "distinct": len(counts),
                                  "values": counts.most_common(4)}
                            for key, counts in sorted(family_values.items())}
    out["outcomes"] = [{"outcomes": list(k), "count": v}
                       for k, v in out["outcomes"].most_common()]
    return out


# ---- section 3.9: the pre-registered predictions, read by nothing but the report ------

def predictions(doc):
    """Seven statements written before any quote was opened, each marked held or refuted.

    Nothing in section 7 reads this and no figure in it is an expectation any check asserts.
    """
    integ, book, geo, ex, pair = (doc["integrity"], doc["book"], doc["geometry"],
                                  doc["executability"], doc["pairs"])
    out = []
    share = integ["complete_recomputed"] / float(SET_NEED)
    out.append({"id": "P1", "claim": "quotes_complete holds for at least 90% of members",
                "observed": "%d of %d = %.4f" % (integ["complete_recomputed"], SET_NEED, share),
                "held": share >= 0.90})
    worst, worst_tau = None, None
    for tau in ADMITTED:
        reads = sum(1 for r in doc["rows"] if r["tau"] == tau and r["outcome"] == UP
                    and r["status"] == 200 and r["bid_levels"] is not None)
        both = sum(1 for r in doc["rows"] if r["tau"] == tau and r["outcome"] == UP
                   and r["best_bid"] is not None and r["best_ask"] is not None)
        s = both / float(reads) if reads else 0.0
        if worst is None or s < worst:
            worst, worst_tau = s, tau
    out.append({"id": "P2", "claim": "both sides of the Up book non-empty in at least 95% "
                                     "of reads at every ADMITTED tau",
                "observed": "worst tau %s at %.4f" % (worst_tau, worst), "held": worst >= 0.95})
    meds = {tau: ex["band_pp"][tau]["0.50"] for tau in ADMITTED}
    ok3 = all(m is not None and 1.0 <= m <= 4.0 for m in meds.values())
    out.append({"id": "P3", "claim": "median executable band between 1.0 and 4.0 pp at every "
                                     "ADMITTED tau",
                "observed": ", ".join("%s: %s" % (t, _fmt(meds[t])) for t in ADMITTED),
                "held": ok3})
    rt = {tau: ex["round_trip_pp"][tau]["0.50"] for tau in ADMITTED}
    ok4 = all(m is not None and m > 3.5 for m in rt.values())
    out.append({"id": "P4", "claim": "median round-trip cost above 3.5 pp at every ADMITTED tau",
                "observed": ", ".join("%s: %s" % (t, _fmt(rt[t])) for t in ADMITTED),
                "held": ok4})
    paired = sum(pair["paired"].values())
    defined = sum(len(v) for v in pair["bid_sum"].values())
    over = len(pair["bid_over"])
    share5 = (defined - over) / float(defined) if defined else 0.0
    out.append({"id": "P5", "claim": "bid_up + bid_down <= 1 at no fewer than 99.5% of paired "
                                     "checkpoints",
                "observed": "%d of %d = %.5f, over the %d paired checkpoints where both best "
                            "bids exist; at %d further paired checkpoints one side was empty "
                            "and the sum is undefined"
                            % (defined - over, defined, share5, defined, paired - defined),
                "held": share5 >= 0.995})
    med_ok = all(geo["offsets"][tau]["0.50"] is not None
                 and geo["offsets"][tau]["0.50"] < 500.0 for tau in config.QUOTE_TAUS)
    q99_ok = all(geo["offsets"][tau]["0.99"] is not None
                 and geo["offsets"][tau]["0.99"] < 1000.0 for tau in config.QUOTE_TAUS)
    out.append({"id": "P6", "claim": "median offset_ms under 500 ms and the 0.99 quantile under "
                                     "1,000 ms at every tau",
                "observed": "medians %s; 0.99 %s"
                            % (", ".join("%s: %s" % (t, _fmt(geo["offsets"][t]["0.50"]))
                                         for t in config.QUOTE_TAUS),
                               ", ".join("%s: %s" % (t, _fmt(geo["offsets"][t]["0.99"]))
                                         for t in config.QUOTE_TAUS)),
                "held": med_ok and q99_ok})
    ts_present = book["fields"]["timestamp"]["present"]
    p7_share = ts_present / float(book["parsed"]) if book["parsed"] else 0.0
    p7_med = all(book["ts_delta_ms"][tau]["0.50"] is not None
                 and book["ts_delta_ms"][tau]["0.50"] < 2000.0 for tau in config.QUOTE_TAUS)
    out.append({"id": "P7", "claim": "timestamp present in at least 99% of 200 replies and the "
                                     "median of 3.5 item 8 under 2,000 ms",
                "observed": "%d of %d = %.4f; medians %s"
                            % (ts_present, book["parsed"], p7_share,
                               ", ".join("%s: %s" % (t, _fmt(book["ts_delta_ms"][t]["0.50"]))
                                         for t in config.QUOTE_TAUS)),
                "held": p7_share >= 0.99 and p7_med})
    return out


def _fmt(value, places=4):
    if value is None:
        return "—"
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, int):
        return str(value)
    return ("%%.%df" % places) % float(value)


# ---- the run ------------------------------------------------------------------------

def build():
    """The fixed order of section 5.1, asserted step by step."""
    started = time.time()
    steps, marks, previous = [], [], [0.0]

    def mark(name):
        """Seconds since the previous mark. Section 6's table is answered term by term."""
        now = time.time() - started
        delta = now - previous[0]
        previous[0] = now
        marks.append({"step": name, "seconds": round(delta, 3), "at": round(now, 3)})
        return delta

    gates = v1_gates()                                                         # 0
    pfair_at_start = _sha256_file(os.path.join(HERE, os.pardir, PFAIR_PATH))
    steps.append("0 the fingerprint gate: revision %s, %d anchors, %d frozen and %d tracked "
                 "rows, %.1f s" % (gates["revision"], len(gates["anchors_matched"]),
                                   gates["frozen"], gates["tracked"], mark("gate")))

    host = [tz11a.host_read("run start", set(), tz11a.FLOOR_START_BYTES)]      # 1
    steps.append("1 host read 1, over the empty set, at the start floor")

    tests = selftests()                                                        # 2
    steps.append("2 the six self-tests, %d assertions, %.1f s"
                 % (tests["assertions"], mark("selftests")))

    v6_doc = v6()                                                              # 3
    v2_doc = v2_static()
    steps.append("3 v6 and the static half of v2, %.1f s" % mark("static"))

    manifests = load_manifests()                                               # 4
    rows_considered, members, set_doc = the_set(manifests)
    assert len(members) == SET_NEED
    steps.append("4 the set: %d members from %d units considered, %.1f s"
                 % (set_doc["members"], set_doc["considered"], mark("set")))

    walked, whole, admissible, domain_doc = domain(members)                    # 5
    host.append(tz11a.host_read("after the domain", set(members), tz11a.FLOOR_BYTES))
    steps.append("5 the domain: %d of %d grids whole; host read 2, %.1f s"
                 % (domain_doc["grid_whole"], SET_NEED, mark("domain")))

    per_member = {}                                                            # 6
    probe_started = time.time()
    for t0 in members[:PROBE_MEMBERS]:
        per_member[t0] = read_member(t0, manifests)
    probe = time.time() - probe_started
    if probe > PROBE_LIMIT_S:
        raise SystemExit("BLOCKED at section 6: the %d-member probe took %.3f s, above %.1f s"
                         % (PROBE_MEMBERS, probe, PROBE_LIMIT_S))
    projected = (time.time() - started) + SET_NEED / float(PROBE_MEMBERS) * probe \
        + PROJECTION_TAIL_S
    if projected > PROJECTION_LIMIT_S:
        raise SystemExit("BLOCKED at section 6: the run projects %.0f s, above %.0f s"
                         % (projected, PROJECTION_LIMIT_S))
    steps.append("6 the probe: %d members in %.3f s, under %.1f s; the run projects %.0f s, "
                 "under %.0f s" % (PROBE_MEMBERS, probe, PROBE_LIMIT_S, projected,
                                   PROJECTION_LIMIT_S))

    for t0 in members[PROBE_MEMBERS:]:                                         # 7
        per_member[t0] = read_member(t0, manifests)
    blocking = [m for m in per_member.values() if not m["agree"]]
    if blocking:
        raise SystemExit("BLOCKED at section 3.3: the two readers disagree at %d members, "
                         "first %d" % (len(blocking), blocking[0]["T0"]))
    bad_offsets = [d for t0 in members for d in per_member[t0]["geometry"]["disagreements"]]
    if bad_offsets:
        raise SystemExit("BLOCKED at section 3.4: %d offset disagreements, first %r"
                         % (len(bad_offsets), bad_offsets[0]))
    no_offsets = [t0 for t0 in members if not per_member[t0]["geometry"]["compared"]]
    steps.append("7 the remaining %d members; both readers agree at %d of %d; %d offset "
                 "disagreements; %d manifests carry no quote_offsets_ms key"
                 % (SET_NEED - PROBE_MEMBERS, len(per_member), SET_NEED, len(bad_offsets),
                    len(no_offsets)))
    steps.append("7b the quote lines and the geometry over all %d members, %.1f s"
                 % (SET_NEED, mark("quote lines")))

    docs = {t0: documents(t0) for t0 in members}                               # 8
    timeout_ms = recorder_constant("QUOTE_TIMEOUT_S") * 1000
    rows, stat = book_pass(members, per_member, docs, walked, admissible, timeout_ms)
    min_size = choose_min_size(rows, stat)
    steps.append("8 %d read rows, %d bodies parsed; MIN_SIZE from %s, %.1f s"
                 % (len(rows), stat["parsed"], min_size["source"], mark("bodies")))

    doc = {                                                                    # 9
        "set": set_doc, "rows_considered": rows_considered, "members": members,
        "domain": domain_doc, "integrity": integrity_tables(members, per_member),
        "geometry": geometry_tables(rows, timeout_ms, per_member, members),
        "book": book_tables(stat, rows), "executability": executability(rows),
        "pairs": pairs(rows, docs), "documents": document_tables(members, docs),
        "min_size": min_size, "rows": rows, "selftests": tests, "v2_static": v2_doc,
        "v6": v6_doc, "no_offset_key": no_offsets, "timeout_ms": timeout_ms,
        "counts": {"members": SET_NEED, "checkpoints": CHECKPOINTS,
                   "checkpoints_admitted": CHECKPOINTS_ADMITTED,
                   "reads_at_completeness": READS_COMPLETE, "reads_found": len(rows)},
    }
    assert CHECKPOINTS == SET_NEED * len(config.QUOTE_TAUS) == 8400
    assert CHECKPOINTS_ADMITTED == SET_NEED * len(ADMITTED) == 6000
    assert READS_COMPLETE == CHECKPOINTS * config.TOKENS_PER_MARKET == 16800
    doc["predictions"] = predictions(doc)
    steps.append("9 the tables and the predictions, %.1f s" % mark("tables"))

    host.append(tz11a.host_read("run end", set(members), tz11a.FLOOR_BYTES))   # 10
    assert host[0]["recorder_pids"] == host[2]["recorder_pids"], "V9: the recorder pid moved"
    assert host[0]["newest_start_recv_ns"] == host[2]["newest_start_recv_ns"], \
        "V9: the newest start record moved"
    assert host[0]["newest_start_sha"] == host[2]["newest_start_sha"], "V9: the start sha moved"
    assert host[2]["interval_directories"] >= host[0]["interval_directories"], \
        "V9: the interval count fell"
    assert host[1]["read_set_sha256"] == host[2]["read_set_sha256"], \
        "V9: the read set changed between reads 2 and 3"
    steps.append("10 host read 3; V9's four assertions between reads 1 and 3, and the read-set "
                 "hash between reads 2 and 3")
    doc["host"] = host
    doc["gates"] = gates
    doc["v8"] = v8(pfair_at_start)
    doc["v2_runtime"] = v2_runtime()
    doc["steps"] = steps
    doc["elapsed_s"] = time.time() - started
    doc["peak_rss_kb"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    doc["probe_s"] = probe
    doc["marks"] = marks
    return doc


# ---- section 9 of the TZ's report: the rendered tables --------------------------------

BLOCKS = (("ADMITTED — the five tau Phase 1 did not disqualify", ADMITTED),
          ("OUTSIDE — barred from supporting any Phase 2 or Phase 3 claim", OUTSIDE))


def q_table(title, summaries, places=4):
    """One `Q` summary per tau, ADMITTED first and OUTSIDE in a separately headed block."""
    lines = ["**%s**" % title, "",
             "| tau | n | min | 0.25 | 0.50 | 0.75 | 0.90 | 0.99 | max |",
             "|---|---|---|---|---|---|---|---|---|"]
    for heading, taus in BLOCKS:
        lines.append("| *%s* | | | | | | | | |" % heading)
        for tau in taus:
            s = summaries.get(tau) or q_summary([])
            lines.append("| %d | %d | %s | %s | %s | %s | %s | %s | %s |"
                         % (tau, s["n"], _fmt(s["min"], places),
                            _fmt(s["0.25"], places), _fmt(s["0.50"], places),
                            _fmt(s["0.75"], places), _fmt(s["0.90"], places),
                            _fmt(s["0.99"], places), _fmt(s["max"], places)))
    lines.append("")
    return lines


def count_table(title, header, rowsof):
    lines = ["**%s**" % title, "", "| tau | " + " | ".join(header) + " |",
             "|---" * (len(header) + 1) + "|"]
    for heading, taus in BLOCKS:
        lines.append("| *%s* |%s" % (heading, " |" * len(header)))
        for tau in taus:
            lines.append("| %d | %s |" % (tau, " | ".join(str(v) for v in rowsof(tau))))
    lines.append("")
    return lines


def tables(doc):
    """Every table of section 3, in section 3's order. Deterministic: no clock, no timing."""
    s, dom, integ = doc["set"], doc["domain"], doc["integrity"]
    book, geo, ex, pair = doc["book"], doc["geometry"], doc["executability"], doc["pairs"]
    out = ["# TZ-14 — the quote inventory: tables", "",
           "Every figure below is a function of the quotes, the capture's own manifests and "
           "the pricer's scale `sigma_hat`. No probability is computed anywhere and no "
           "outcome enters any number.", ""]

    out += ["## 3.1 The set", "",
            "| quantity | value |", "|---|---|",
            "| units considered | %d |" % s["considered"],
            "| members | %d |" % s["members"],
            "| member-list SHA-256 | `%s` |" % s["sha256"],
            "| first member | %d (%s) |" % (s["first"], s["first_utc"]),
            "| last member | %d (%s) |" % (s["last"], s["last_utc"]),
            "| span, days | %.3f |" % s["span_days"],
            "| non-members | %d |" % len(s["non_members"]),
            "| weekend members | %d |" % s["weekend_members"], "",
            "**Members per UTC weekday**", "", "| weekday | members |", "|---|---|"]
    for day in ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"):
        out.append("| %s | %d |" % (day, s["weekday_counts"].get(day, 0)))
    out.append("")

    out += ["## 3.2 The domain", "",
            "| quantity | value |", "|---|---|",
            "| members whose one-second grid is whole | %d of %d |"
            % (dom["grid_whole"], s["members"]),
            "| share | %.4f |" % dom["grid_whole_share"],
            "| whole, weekday / weekend | %d / %d |"
            % (dom["grid_whole_weekday"], dom["grid_whole_weekend"]),
            "| members `grid_of` raised on | %d |" % dom["grid_raised"], "",
            "**Admissible members per tau, at `pfair.ADMIT` unchanged**", "",
            "| tau | ADMIT | admissible | share of whole grids | weekday | weekend | list SHA-256 |",
            "|---|---|---|---|---|---|---|"]
    for heading, taus in BLOCKS:
        out.append("| *%s* | | | | | | |" % heading)
        for tau in taus:
            p = dom["per_tau"][tau]
            share = p["admissible"] / float(dom["grid_whole"]) if dom["grid_whole"] else 0.0
            out.append("| %d | %s | %d | %.4f | %d | %d | `%s` |"
                       % (tau, p["admit"], p["admissible"], share, p["weekday"], p["weekend"],
                          p["sha256"]))
    out.append("")
    out += q_table("sigma_hat over the members whose grid is whole, USD/s",
                   {tau: dom["per_tau"][tau]["sigma_hat"] for tau in config.QUOTE_TAUS}, 5)

    out += ["## 3.3 The quote file", "",
            "| quantity | value |", "|---|---|",
            "| members with no quote file | %d |" % len(integ["no_file"]),
            "| members above 14 read lines | %d |" % len(integ["over_14"]),
            "| members carrying a duplicate (tau, token_id) | %d |" % integ["dup_members"],
            "| duplicate pairs | %d |" % integ["dup_pairs"],
            "| members with a torn line | %d |" % len(integ["torn"]),
            "| torn lines | %d |" % sum(integ["torn"].values()),
            "| `status == 200` with `body_is_json` false | %d |" % integ["body_false_200"],
            "| members whose manifest `quotes_complete` agrees | %d of %d |"
            % (integ["complete_agree"], s["members"]),
            "| `quotes_complete` true, manifest / recomputed | %d / %d |"
            % (integ["complete_manifest"], integ["complete_recomputed"]),
            "| members carrying more than one recorder start record | %d |"
            % len(integ["multi_start"]),
            "| members where both readers agree (V4) | %d of %d |"
            % (integ["reader_agree"], s["members"]), "",
            "**Read lines per member**", "", "| lines | members |", "|---|---|"]
    for value, count in sorted(integ["line_counts"].items()):
        out.append("| %d | %d |" % (value, count))
    out += ["", "**`status` over every read line, `null` included**", "",
            "| status | reads |", "|---|---|"]
    for value, count in sorted(integ["status"].items(), key=lambda kv: (kv[0] is None, kv[0])):
        out.append("| %s | %d |" % ("null" if value is None else value, count))
    out.append("")
    if integ["errors"]:
        out += ["**`error` strings of the null rows, grouped by text**", "",
                "| error | reads |", "|---|---|"]
        for text, count in integ["errors"].most_common():
            out.append("| `%s` | %d |" % (text.replace("|", "\\|")[:160], count))
        out.append("")

    out += ["## 3.4 The read geometry", ""]
    out += q_table("offset_ms per tau, over the reads at that tau", geo["offsets"], 1)
    out += count_table("offset_ms counts per tau",
                       ["negative", "above 1,000 ms", "above %d ms" % geo["timeout_ms"]],
                       lambda tau: (geo["negative"][tau], geo["over_1s"][tau],
                                    geo["over_timeout"][tau]))
    out += q_table("|recv_ns_up - recv_ns_down| per checkpoint, ms", geo["pair_skew_ms"], 1)
    out += ["| quantity | value |", "|---|---|",
            "| members reporting `clock_offset_abs_max_ms` | %d |" % geo["clock_members_reported"],
            "| maximum over the set, ms | %s |" % _fmt(geo["clock_offset_max_ms"], 3),
            "| members above `CLOCK_OFFSET_LIMIT_MS` = %s | %d |"
            % (geo["clock_limit_ms"], geo["clock_over_limit"]),
            "| members whose manifest carries no `quote_offsets_ms` key | %d |"
            % len(doc["no_offset_key"]), ""]
    return out + tables_book(doc) + tables_exec(doc) + tables_pairs(doc)


def tables_book(doc):
    """Section 3.5's tables: the payload's shape, its sides, its scalars and its clock."""
    book, s = doc["book"], doc["set"]
    out = ["## 3.5 The book", "",
           "| quantity | value |", "|---|---|",
           "| bodies parsed | %d |" % book["parsed"],
           "| `status == 200` whose body did not parse | %d |" % book["unparsed_200"],
           "| bodies that parsed to something other than an object | %d |" % book["not_object"],
           "| levels dropped for a missing or non-numeric price or size | %d |"
           % book["bad_levels"],
           "| crossed or locked books, `best_bid >= best_ask` | %d |" % len(book["crossed"]),
           "| replies carrying no `tick_size` | %d |" % book["tick_absent"],
           "| venue `timestamp` values that did not parse as an integer | %d |"
           % book["ts_unparsed"],
           "| `recv_ns/10^6 - timestamp` negative | %d |" % book["ts_negative"], "",
           "**The top-level key set, as found**", "",
           "| keys | replies | example T0 | example tau |", "|---|---|---|---|"]
    for shape in book["shapes"]:
        out.append("| `%s` | %d | %d | %d |"
                   % (", ".join(shape["keys"]), shape["count"], shape["example_T0"],
                      shape["example_tau"]))
    out += ["", "**Observed ordering per side, over the parsed bodies**", "",
            "| side | ascending | descending | neither | single | empty |",
            "|---|---|---|---|---|---|"]
    for side in ("bids", "asks"):
        o = book["orderings"][side]
        out.append("| %s | %d | %d | %d | %d | %d |"
                   % (side, o.get("ascending", 0), o.get("descending", 0),
                      o.get("neither", 0), o.get("single", 0), o.get("empty", 0)))
    out += ["", "**Level count per side, as the `Q` summary**", "",
            "| side | n | min | 0.25 | 0.50 | 0.75 | 0.90 | 0.99 | max |",
            "|---|---|---|---|---|---|---|---|---|"]
    for side in ("bids", "asks"):
        q = book["levels"][side]
        out.append("| %s | %d | %s | %s | %s | %s | %s | %s | %s |"
                   % (side, q["n"], _fmt(q["min"], 0), _fmt(q["0.25"], 0), _fmt(q["0.50"], 0),
                      _fmt(q["0.75"], 0), _fmt(q["0.90"], 0), _fmt(q["0.99"], 0),
                      _fmt(q["max"], 0)))
    out.append("")
    out += count_table("Empty sides and both-sided reads per tau",
                       ["no bids", "no asks", "neither side", "both sides quoted"],
                       lambda tau: (book["empty"][tau].get("bids", 0),
                                    book["empty"][tau].get("asks", 0),
                                    book["empty"][tau].get("neither", 0),
                                    book["both_sides"][tau]))
    out += q_table("Spread `ask - bid` per tau, probability points", book["spread_pp"], 3)
    out += q_table("Spread per tau, in ticks — at the reply's `tick_size` where present and at "
                   "0.01 carried from map section 6's TZ-05a measurement where absent",
                   book["spread_ticks"], 2)
    out += q_table("`recv_ns/10^6 - timestamp` per tau, ms — the venue's stated instant "
                   "against ours, the venue field read as integer milliseconds",
                   book["ts_delta_ms"], 1)
    out += ["**The scalar fields of the reply**", "",
            "| field | present | absent | distinct values | values |",
            "|---|---|---|---|---|"]
    for field in BODY_FIELDS:
        f = book["fields"][field]
        if f["values"] is not None:
            shown = ", ".join("`%s` x%d" % (v[:40], c) for v, c in f["values"])
        else:
            shown = "cardinality above %d; three examples: %s" \
                % (DISTINCT_LIST_MAX,
                   ", ".join("`%s` x%d" % (v[:40], c) for v, c in f["examples"]))
        out.append("| `%s` | %d | %d | %d | %s |"
                   % (field, f["present"], f["absent"], f["distinct"], shown))
    out += ["", "| quantity | value |", "|---|---|",
            "| replies where `asset_id` differs from the `token_id` requested | %d |"
            % len(book["asset_id_mismatch"]), ""]

    out += ["## 3.8 The market document", "",
            "| quantity | value |", "|---|---|",
            "| members with a `gamma.json` | %d of %d |" % (doc["documents"]["present"],
                                                            s["members"]),
            "| members whose `outcomes` is a two-element Up/Down array | %d |"
            % doc["documents"]["usable"], "",
            "**The `outcomes` arrays, distinct**", "", "| outcomes | members |", "|---|---|"]
    for entry in doc["documents"]["outcomes"]:
        out.append("| `%s` | %d |" % (", ".join(entry["outcomes"]), entry["count"]))
    out += ["", "| key | present | absent | distinct | values |", "|---|---|---|---|---|"]
    for key in GAMMA_KEYS:
        f = doc["documents"]["fields"][key]
        if f["values"] is not None:
            shown = ", ".join("`%s` x%d" % (v[:60], c) for v, c in f["values"])
        else:
            shown = "cardinality above %d; three examples: %s" \
                % (DISTINCT_LIST_MAX,
                   ", ".join("`%s` x%d" % (v[:60], c) for v, c in f["examples"]))
        out.append("| `%s` | %d | %d | %d | %s |"
                   % (key, f["present"], f["absent"], f["distinct"], shown))
    out += ["", "**Keys matching `fee` and `reward`, case-insensitively, per document**", "",
            "| family | keys found | documents |", "|---|---|---|"]
    for name, _ in GAMMA_FAMILIES:
        for entry in doc["documents"]["families"][name]:
            out.append("| %s | `%s` | %d |"
                       % (name, ", ".join(entry["keys"]) or "(none)", entry["count"]))
    out += ["", "**The values those keys carry**", "",
            "| key | documents | distinct | values |", "|---|---|---|---|"]
    for key, entry in doc["documents"]["family_values"].items():
        out.append("| `%s` | %d | %d | %s |"
                   % (key, entry["present"], entry["distinct"],
                      ", ".join("`%s` x%d" % (v, c) for v, c in entry["values"])
                      + (", …" if entry["distinct"] > 4 else "")))
    out.append("")
    return out


def tables_exec(doc):
    """Section 3.6's tables: the executable touch, the size behind it and the round trip."""
    ex, ms = doc["executability"], doc["min_size"]
    out = ["## 3.6 Executability", "",
           "| quantity | value |", "|---|---|",
           "| `MIN_SIZE` taken from | %s |" % ms["source"],
           "| reads carrying `min_order_size` | %d of %d |"
           % (ms["from_reply"], ms["reads_parsed"]),
           "| reads where the map's value was used instead | %d |" % ms["from_map"],
           "| distinct `min_order_size` values | %s |"
           % ", ".join("`%s` x%d" % (v, c) for v, c in sorted(ms["distinct"].items())), ""]
    out += count_table("Reads with no executable touch on one side or the other",
                       ["reads parsed", "no bid5 or no ask5"],
                       lambda tau: (ex["reads"][tau], ex["no_touch"][tau]))
    out += q_table("The executable band `ask5 - bid5` per tau, probability points",
                   ex["band_pp"], 3)
    for side in ("bid", "ask"):
        for k in KS:
            out += q_table("Cumulative %s size within %d tick%s of the executable touch, shares"
                           % (side, k, "" if k == 1 else "s"),
                           ex["cum"]["%s_k%d" % (side, k)], 1)
    out += q_table("Taker fee at `bid5` per tau, probability points", ex["fee_bid5_pp"], 4)
    out += q_table("Taker fee at `ask5` per tau, probability points", ex["fee_ask5_pp"], 4)
    out += ["**The round-trip cost `(ask5 - bid5) + fee(ask5) + fee(bid5)`, probability "
            "points. This is the single number that decides whether a Phase 3 can exist.**", ""]
    out += q_table("Round trip, all reads", ex["round_trip_pp"], 3)
    out += q_table("Round trip, weekday members", ex["round_trip_pp_weekday"], 3)
    out += q_table("Round trip, weekend members", ex["round_trip_pp_weekend"], 3)
    out += q_table("Round trip, admissible at that tau", ex["round_trip_pp_admissible"], 3)
    out += q_table("Round trip, not admissible at that tau", ex["round_trip_pp_not_admissible"],
                   3)
    return out


def tables_pairs(doc):
    """Section 3.7's tables: the two tokens of one checkpoint against each other."""
    pair = doc["pairs"]
    out = ["## 3.7 The two tokens", "",
           "| quantity | value |", "|---|---|",
           "| paired checkpoints — both tokens returned a parseable 200 | %d |"
           % sum(pair["paired"].values()),
           "| of those, `bid_up + bid_down` undefined, one book side empty | %d |"
           % pair["undefined"]["bid_sum"],
           "| of those, `ask_up + ask_down` undefined | %d |" % pair["undefined"]["ask_sum"],
           "| of those, `bid5_up + bid5_down` undefined | %d |" % pair["undefined"]["bid5_sum"],
           "| of those, `ask5_up + ask5_down` undefined | %d |" % pair["undefined"]["ask5_sum"],
           "| members excluded, `outcomes` not a two-element Up/Down array | %d |"
           % len(pair["excluded_members"]),
           "| `bid_up + bid_down > 1` | %d |" % len(pair["bid_over"]),
           "| `ask_up + ask_down < 1` | %d |" % len(pair["ask_under"]),
           "| sums crossing 1 at the executable touch, `bid5` side | %d |"
           % sum(1 for e in pair["free_lunch"] if e["side"] == "bid"),
           "| sums crossing 1 at the executable touch, `ask5` side | %d |"
           % sum(1 for e in pair["free_lunch"] if e["side"] == "ask"),
           "| of those, profitable after both taker fees | %d |"
           % sum(1 for e in pair["free_lunch"] if D(e["profit_pp"]) > 0), ""]
    out += count_table("Paired checkpoints per tau", ["paired"],
                       lambda tau: (pair["paired"].get(tau, 0),))
    for name, key, places in (("`bid_up + bid_down`", "bid_sum", 4),
                              ("`ask_up + ask_down`", "ask_sum", 4),
                              ("`mid_up - (1 - mid_down)`", "mid_gap", 4),
                              ("`bid5_up + bid5_down`", "bid5_sum", 4),
                              ("`ask5_up + ask5_down`", "ask5_sum", 4)):
        out += q_table("%s per tau, probability units" % name,
                       tau_summaries({tau: [float(v) for v in vs]
                                      for tau, vs in pair[key].items()}), places)
    for name, listed in (("`bid_up + bid_down > 1`", pair["bid_over"]),
                         ("`ask_up + ask_down < 1`", pair["ask_under"])):
        if not listed:
            out += ["**%s: none.**" % name, ""]
        elif len(listed) <= 50:
            out += ["**%s, listed**" % name, "", "| T0 | tau | sum |", "|---|---|---|"]
            out += ["| %d | %d | %s |" % (e["T0"], e["tau"], e["sum"]) for e in listed]
            out.append("")
        else:
            counts = collections.Counter(e["tau"] for e in listed)
            out += ["**%s: %d occurrences, above 50, so summarised by tau: %s**"
                    % (name, len(listed),
                       ", ".join("%d: %d" % (t, counts.get(t, 0))
                                 for t in config.QUOTE_TAUS)), ""]
    if pair["free_lunch"]:
        out += ["**Section 3.7 item 5 — every checkpoint whose executable sum crosses 1, with "
                "the size standing at both touches and the profit after both taker fees. A "
                "crossing is a free lunch only where that profit is positive.**", "",
                "| T0 | tau | side | sum | size at both touches | profit after both fees, pp |",
                "|---|---|---|---|---|---|"]
        for e in pair["free_lunch"][:200]:
            out.append("| %d | %d | %s | %s | %s | %s |"
                       % (e["T0"], e["tau"], e["side"], e["sum"], e["size"], e["profit_pp"]))
        if len(pair["free_lunch"]) > 200:
            out.append("| … | | | %d further occurrences in the observations file | | |"
                       % (len(pair["free_lunch"]) - 200))
        out.append("")
    else:
        out += ["**No executable sum crossed 1 at any paired checkpoint.**", ""]
    return out


# ---- V11: the disclosure and the per-read observations file ---------------------------

def cell(value):
    if value is None:
        return ""
    if isinstance(value, bool):
        return "1" if value else "0"
    return str(value)


def csv_text(rows):
    """One row per member per tau per token id — V11's reconstruction file.

    Every number a table of section 3 is built from is here, so any single row of any table
    can be reconstructed without re-running the pipeline. The cumulative sizes are carried
    per side, four k values each: V11 names four, and four per side is what sufficiency for
    section 3.6 item 3's per-side table requires.
    """
    out = [",".join(CSV_HEADER)]
    for r in sorted(rows, key=lambda r: (r["T0"], -r["tau"], r["token_id"])):
        out.append(",".join(cell(v) for v in (
            r["T0"], r["tau"], r["token_id"], r["outcome"], r["status"], r["recv_ns"],
            "%.6f" % r["offset_ms"] if r["offset_ms"] is not None else None,
            r["bid_levels"], r["ask_levels"], r["best_bid"], r["best_ask"],
            r["bid5"], r["ask5"],
            r["cum_bid"][0], r["cum_bid"][1], r["cum_bid"][2], r["cum_bid"][5],
            r["cum_ask"][0], r["cum_ask"][1], r["cum_ask"][2], r["cum_ask"][5],
            r["venue_timestamp"], r["sigma_hat"], r["admissible"])))
    return "\n".join(out) + "\n"


def disclosure_text(doc):
    """V11: every unit considered, every member, every non-member with its reasons."""
    out = ["# TZ-14 disclosure", "",
           "## Units considered, in ascending T0", "",
           "| T0 | UTC | weekday | member | reasons |", "|---|---|---|---|---|"]
    for row in doc["rows_considered"]:
        out.append("| %d | %s | %s | %s | %s |"
                   % (row["T0"], utc(row["T0"]), weekday_of(row["T0"]),
                      row["member"] if row["member"] else "—",
                      "; ".join(row["reasons"]) if row["reasons"] else ""))
    out += ["", "## Admissible member lists per tau", ""]
    for tau in config.QUOTE_TAUS:
        p = doc["domain"]["per_tau"][tau]
        out += ["### tau %d — %d members, SHA-256 `%s`" % (tau, p["admissible"], p["sha256"]),
                "", " ".join(str(t0) for t0 in p["members"]), ""]
    if doc["domain"]["raised"]:
        out += ["## Members `tz10b.grid_of` raised on", "", "| T0 | reason |", "|---|---|"]
        out += ["| %d | %s |" % (e["T0"], e["why"]) for e in doc["domain"]["raised"]]
        out.append("")
    if doc["no_offset_key"]:
        out += ["## Members whose manifest carries no `quote_offsets_ms` key", "",
                " ".join(str(t0) for t0 in doc["no_offset_key"]), ""]
    if doc["integrity"]["over_14"]:
        out += ["## Members above 14 read lines", "", "| T0 | lines |", "|---|---|"]
        out += ["| %d | %d |" % (e["T0"], e["lines"]) for e in doc["integrity"]["over_14"]]
        out.append("")
    if doc["integrity"]["no_file"]:
        out += ["## Members with no quote file", "",
                " ".join(str(t0) for t0 in doc["integrity"]["no_file"]), ""]
    if doc["integrity"]["complete_disagree"]:
        out += ["## `quotes_complete` disagreements", "",
                "| T0 | manifest | recomputed |", "|---|---|---|"]
        out += ["| %d | %s | %s |" % (e["T0"], e["manifest"], e["recomputed"])
                for e in doc["integrity"]["complete_disagree"]]
        out.append("")
    if doc["integrity"]["multi_start"]:
        out += ["## Members carrying more than one recorder start record", "",
                " ".join(str(t0) for t0 in doc["integrity"]["multi_start"]), ""]
    if doc["book"]["crossed"]:
        out += ["## Crossed or locked books", "", "| T0 | tau | best bid | best ask |",
                "|---|---|---|---|"]
        out += ["| %d | %d | %s | %s |" % (e["T0"], e["tau"], e["bid"], e["ask"])
                for e in doc["book"]["crossed"]]
        out.append("")
    if doc["book"]["asset_id_mismatch"]:
        out += ["## Replies whose `asset_id` differs from the requested `token_id`", "",
                "| T0 | tau | requested | returned |", "|---|---|---|---|"]
        out += ["| %d | %d | %s | %s |" % (e["T0"], e["tau"], e["token_id"], e["asset_id"])
                for e in doc["book"]["asset_id_mismatch"]]
        out.append("")
    if doc["pairs"]["excluded_members"]:
        out += ["## Members excluded from section 3.7 — `outcomes` not a two-element array", "",
                " ".join(str(t0) for t0 in doc["pairs"]["excluded_members"]), ""]
    return "\n".join(out) + "\n"


def summary_text(doc):
    """The counts a report quotes, and the seven predictions. Deterministic."""
    out = ["# TZ-14 — counts", "",
           "| quantity | value |", "|---|---|"]
    for name, value in (("members", doc["counts"]["members"]),
                        ("checkpoints, 1,200 x 7", doc["counts"]["checkpoints"]),
                        ("checkpoints at ADMITTED, 1,200 x 5",
                         doc["counts"]["checkpoints_admitted"]),
                        ("reads at full completeness, 1,200 x 7 x 2",
                         doc["counts"]["reads_at_completeness"]),
                        ("read rows actually found", doc["counts"]["reads_found"]),
                        ("bodies parsed", doc["book"]["parsed"]),
                        ("self-test items", doc["selftests"]["items"]),
                        ("self-test assertions", doc["selftests"]["assertions"]),
                        ("string constants scanned", doc["v2_static"]["strings_scanned"]),
                        ("string constants carrying a barred name",
                         doc["v2_static"]["strings_carrying"]),
                        ("calls scanned", doc["v2_static"]["calls_scanned"]),
                        ("pfair probability calls", doc["v2_static"]["probability_calls"]),
                        ("calls of m2_labels, walk_member, fit_student",
                         doc["v2_static"]["never_called_calls"]),
                        ("opens of the settled document by this instrument",
                         doc["v2_runtime"]["settled_document_opens_by_this_instrument"])):
        out.append("| %s | %s |" % (name, value))
    out += ["| pfair attributes named | %s |" % ", ".join(doc["v2_static"]["pfair_attributes"]),
            "", "## Section 3.9 — the seven pre-registered predictions", "",
            "| # | prediction | observed | verdict |", "|---|---|---|---|"]
    for p in doc["predictions"]:
        out.append("| %s | %s | %s | **%s** |"
                   % (p["id"], p["claim"], p["observed"], "held" if p["held"] else "refuted"))
    out += ["", "## V10 — map section 0's fingerprint table, as this run read it", "",
            "| path | state | lines | bytes | SHA-256 | equals the map |",
            "|---|---|---|---|---|---|"]
    for row in doc["gates"]["rows"]:
        out.append("| `%s` | %s | %d | %d | `%s` | %s |"
                   % (row["path"], row["state"], row["lines"], row["bytes"], row["sha256"],
                      "yes" if row["expected"] == row["sha256"]
                      else ("—" if row["expected"] is None else "**NO**")))
    out += ["", "**Anchors re-derived from the bytes, not from the table that prints them**", "",
            "| anchor | path | first 12 hex of SHA-256 |", "|---|---|---|"]
    for e in doc["gates"]["anchors_derived"]:
        out.append("| %s | `%s` | `%s` |" % (e["anchor"], e["path"], e["sha12"]))
    out += ["", "**V8 — `pfair.ADMIT` as read, at 7 of 7 tau**", "",
            "| tau | ADMIT |", "|---|---|"]
    for tau in config.QUOTE_TAUS:
        out.append("| %d | %s |" % (tau, doc["v8"]["ADMIT"][tau]))
    out += ["", "## The self-tests, verbatim", ""]
    out += ["- " + line for line in doc["selftests"]["lines"]]
    out.append("")
    return "\n".join(out) + "\n"


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(WORK_ROOT, "out")
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    doc = build()
    deterministic = {
        "tables.md": "\n".join(tables(doc)) + "\n",
        "observations.csv": csv_text(doc["rows"]),
        "disclosure.md": disclosure_text(doc),
        "counts.md": summary_text(doc),
    }
    for name, text in sorted(deterministic.items()):
        with open(os.path.join(out_dir, name), "wt", encoding="utf-8") as fh:
            fh.write(text)
    # V3 names this file and does not compare it: it carries clock readings and timings.
    run = {"host": doc["host"], "steps": doc["steps"], "elapsed_s": doc["elapsed_s"],
           "gates": doc["gates"], "v8": doc["v8"],
           "probe_s": doc["probe_s"], "peak_rss_kb": doc["peak_rss_kb"],
           "marks": doc["marks"],
           "v6": doc["v6"], "v2_static": doc["v2_static"], "v2_runtime": doc["v2_runtime"],
           "python": sys.version, "min_size": {k: v for k, v in doc["min_size"].items()
                                               if k != "distinct"},
           "interpreter": sys.executable,
           "sha256": {name: hashlib.sha256(text.encode("utf-8")).hexdigest()
                      for name, text in sorted(deterministic.items())}}
    with open(os.path.join(out_dir, "run.json"), "wt", encoding="utf-8") as fh:
        fh.write(json.dumps(run, indent=2, sort_keys=True, default=str) + "\n")
    for name in sorted(deterministic):
        sys.stdout.write("%s  %s\n" % (run["sha256"][name], name))
    for line in doc["steps"]:
        sys.stdout.write("step %s\n" % line)
    sys.stdout.write("elapsed %.1f s, peak RSS %d kB\n"
                     % (doc["elapsed_s"], doc["peak_rss_kb"]))


if __name__ == "__main__":
    main()
