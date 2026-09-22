#!/usr/bin/env python3
# TZ-17 - the settlement chain: do the 15-minute and 5-minute markets settle on one reading?
# Implements CryptoTZ/TZ-17-settlement-chain.md. Standard library only; imports nothing from
# research/. Runs on /root/tz01-env/venv/bin/python.

import argparse
import ast
import datetime
import decimal
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from decimal import Decimal
from fractions import Fraction

if not __debug__:
    raise SystemExit("TZ-17: refuses to run with asserts disabled")

decimal.getcontext().prec = 60

# ---------------------------------------------------------------- constants

SCHEME_SEP = ":" + "//"                       # built from parts; see S9
ENDPOINT = "https://gamma-api.polymarket.com/markets/slug/"
USER_AGENT = "btc-5m-twap-tz17"
TIMEOUT_S = 20
PACE_S = 0.5

REQUIRED_REVISION = "2026-09-19-c"
ANCHORS = {
    "A1": "229a944f2d51",
    "A2": "6c5089330629",
    "A3": "0-complete / 1-student-5tau-not-disqualified / 2-undecidable-5tau",
    "A4": "437b45ea196b",
    "A5": "9fd1c7de0f74",
    "A6": "729f0bcdbee3",
}
ANCHOR_SOURCES = {
    "A2": "research/twap-divergence.py",
    "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
    "A5": "research/recorder/recorder.py",
    "A6": "research/pfair.py",
}
TABLE_ROWS = 25
FROZEN_ROWS = 22

RESERVED_EPOCH = 1789669800                   # System Map 2.3, TZ-16's reserved span
START_T = 1788998400                          # 2026-09-10 00:00:00 UTC
CANDIDATE_CAP = 400
NEED = 200
PASS_MIN = 199
EARLY_STOP_K = 9                              # candidates 0..9
REFETCH_MEMBERS = 10
MAX_STAGE_F_REQUESTS = 1601
REFETCH_REQUESTS = 40
LARGEST_EPOCH = 1789358400

WORK = "/root/tz17-work"
WORKTREES = (WORK + "/wt", WORK + "/wt-report")
RAW_DIR = WORK + "/raw"
INDEX_PATH = WORK + "/index.jsonl"
REFETCH_DIR = WORK + "/refetch"
REFETCH_INDEX_PATH = WORK + "/refetch.jsonl"
FETCH_SUMMARY_PATH = WORK + "/fetch-summary.json"

WRITE_CAP = 200000000
SPACE_FLOOR = 2200000000
STAGE_F_WALL_S = 2700.0
STAGE_A_WALL_S = 300.0
FAILFAST_RUN = 20

POWER_2PCT = "0.910624516228067965960219332490"
POWER_1PCT = "0.595354315327973499366704428681"
POWER_TOL = Decimal("1E-18")

CSV_HEADER = ("k,T,member,reason,K15,K5a,K5c,K5d,O15,O5c,I1,I2,I3,holds,I1_exact,K5b,"
              "O5a,O5b,I4a,I4b,d15,d5,sha_M15,sha_M5a,sha_M5b,sha_M5c,sha_M5d")

PTB_RE = re.compile(r"^[0-9]+\.[0-9]+$")

# ---------------------------------------------------------------- counters

ASSERTS = {"n": 0}
WRITES = {"bytes": 0, "checks": 0}
P3 = {"checks": 0, "max_5m": 0, "max_15m": 0}


def A(cond, label):
    """One check. Increments the assert count and aborts the run when false."""
    ASSERTS["n"] += 1
    assert cond, label
    return True


class Blocked(Exception):
    pass


class EarlyStop(Blocked):
    pass


class FailFast(Blocked):
    pass


class WallClock(Blocked):
    pass


# ---------------------------------------------------------------- writing

def guarded_path(path):
    """P6: every open for writing lies under /root/tz17-work/ and outside both worktrees."""
    real = os.path.realpath(path)
    WRITES["checks"] += 1
    assert real == WORK or real.startswith(WORK + "/"), "P6: outside the work tree: " + real
    for wt in WORKTREES:
        assert real != wt and not real.startswith(wt + "/"), "P6: inside a worktree: " + real
    return real


def write_bytes(path, data):
    real = guarded_path(path)
    WRITES["bytes"] += len(data)
    assert WRITES["bytes"] <= WRITE_CAP, "P6: write cap exceeded"
    with open(real, "wb") as fh:
        fh.write(data)


def append_text(path, text):
    real = guarded_path(path)
    data = text.encode("utf-8")
    WRITES["bytes"] += len(data)
    assert WRITES["bytes"] <= WRITE_CAP, "P6: write cap exceeded"
    with open(real, "ab") as fh:
        fh.write(data)


def ensure_dir(path):
    real = guarded_path(path)
    os.makedirs(real, exist_ok=True)
    return real


def free_bytes(path):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def now_iso():
    t = datetime.datetime.now(datetime.timezone.utc)
    return t.strftime("%Y-%m-%dT%H:%M:%S.") + "%03dZ" % (t.microsecond // 1000)


# ---------------------------------------------------------------- 3.1 slugs and fields

def slug15(T):
    return "btc-updown-15m-" + str(int(T))


def slug5(t):
    return "btc-updown-5m-" + str(int(t))


def epoch_of(slug):
    """The epoch a slug names, with its market type."""
    if slug.startswith("btc-updown-15m-"):
        return "15m", int(slug[len("btc-updown-15m-"):])
    if slug.startswith("btc-updown-5m-"):
        return "5m", int(slug[len("btc-updown-5m-"):])
    raise ValueError("unknown slug " + slug)


def check_p3(slug):
    """P3, before every request: nothing from TZ-16's reserved span."""
    kind, e = epoch_of(slug)
    P3["checks"] += 1
    if kind == "15m":
        assert e + 900 <= RESERVED_EPOCH, "P3: 15m close in the reserved span: " + slug
        P3["max_15m"] = max(P3["max_15m"], e)
    else:
        assert e <= RESERVED_EPOCH, "P3: 5m epoch in the reserved span: " + slug
        P3["max_5m"] = max(P3["max_5m"], e)
    return True


def parse_body(raw):
    """The response body parsed with parse_float=Decimal, or None."""
    try:
        return json.loads(raw, parse_float=Decimal)
    except Exception:
        return None


def K(doc):
    """The price to beat, CANON 1.1, as Decimal - or None when it is not convertible."""
    try:
        value = doc["events"][0]["eventMetadata"]["priceToBeat"]
    except (KeyError, IndexError, TypeError):
        return None
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, str):
        if not PTB_RE.match(value):
            return None
        try:
            return Decimal(value)
        except decimal.InvalidOperation:
            return None
    if isinstance(value, (int, Decimal, float)):
        try:
            return Decimal(str(value))
        except (decimal.InvalidOperation, ValueError):
            return None
    return None


def _as_pair(value):
    if isinstance(value, list):
        out = value
    elif isinstance(value, str):
        try:
            out = json.loads(value)
        except Exception:
            return None
        if not isinstance(out, list):
            return None
    else:
        return None
    return out if len(out) == 2 else None


def O(doc):
    """The resolved outcome string, mapped by string and never by position - or None."""
    if not isinstance(doc, dict):
        return None
    outs = _as_pair(doc.get("outcomes"))
    prices = _as_pair(doc.get("outcomePrices"))
    if outs is None or prices is None:
        return None
    if set(o for o in outs if isinstance(o, str)) != {"Up", "Down"}:
        return None
    try:
        vals = [Decimal(str(p)) for p in prices]
    except (decimal.InvalidOperation, ValueError, TypeError):
        return None
    if any(not v.is_finite() for v in vals):
        return None
    ones = [i for i, v in enumerate(vals) if v == 1]
    zeros = [i for i, v in enumerate(vals) if v == 0]
    if len(ones) != 1 or len(zeros) != 1:
        return None
    return outs[ones[0]]


# ---------------------------------------------------------------- 3.2 validity

def validity(status, doc, slug):
    """The first failing code of 3.2, in order, or 'ok'."""
    if status is None:
        return "fetch"
    if status == 404:
        return "absent"
    if status != 200:
        return "status"
    if not isinstance(doc, dict):
        return "json"
    if doc.get("slug") != slug:
        return "slug"
    if doc.get("closed") is not True:
        return "open"
    k = K(doc)
    if k is None:
        return "no-ptb"
    if not k.is_finite() or k <= 0:
        return "ptb-range"
    if k.as_tuple().exponent > -2:
        return "precision"
    if O(doc) is None:
        return "unresolved"
    return "ok"


# ---------------------------------------------------------------- 3.3 candidates and the set

def candidates(start=START_T, cap=CANDIDATE_CAP):
    """Candidate k yields (k, T). Raises before yielding one that P3 forbids."""
    for k in range(cap):
        T = start + 900 * k
        if T + 900 > RESERVED_EPOCH:
            raise ValueError("P3: candidate %d would close at %d" % (k, T + 900))
        for t in (T, T + 300, T + 600, T + 900):
            if t > RESERVED_EPOCH:
                raise ValueError("P3: candidate %d would request %d" % (k, t))
        yield k, T


def gate_slugs(T):
    """The four gate documents, in 3.4's order."""
    return (slug15(T), slug5(T), slug5(T + 600), slug5(T + 900))


def all_slugs(T):
    """The four gate documents and the disclosure document, in 3.4's order."""
    return (slug15(T), slug5(T), slug5(T + 300), slug5(T + 600), slug5(T + 900))


def candidate_code(code_of, T):
    """A candidate qualifies iff its four gate documents read ok."""
    for slug in gate_slugs(T):
        code = code_of(slug)
        if code != "ok":
            return code
    return "ok"


def form_set(qualify, ks, need):
    """The first `need` qualifying candidates in increasing k. Stops once the need is met."""
    members, nonmembers, considered = [], [], []
    for k in ks:
        code = qualify(k)
        considered.append(k)
        if code == "ok":
            members.append(k)
            if len(members) == need:
                break
        else:
            nonmembers.append((k, code))
    return {
        "members": members,
        "nonmembers": nonmembers,
        "considered": considered,
        "complete": len(members) == need,
    }


# ---------------------------------------------------------------- 3.5 identities

def exponent(x):
    return x.as_tuple().exponent


def identity_1(k15, k5a):
    """I1 - one reading at the shared open, to the precision of the coarser literal."""
    e = max(exponent(k15), exponent(k5a))
    return abs(k15 - k5a) < Decimal(1).scaleb(e)


def expected_outcome(close, strike):
    """Both market types resolve Up when the close is at or above the price to beat."""
    return "Up" if close >= strike else "Down"


# ---------------------------------------------------------------- 4 gate

def reading(N, members):
    if members < NEED or N is None:
        return "UNDECIDABLE"
    if N >= PASS_MIN:
        return "PASS"
    return "FAIL"


def power(p):
    """P(N <= 198) when each of 200 windows fails independently with probability p."""
    p = Fraction(p)
    q = Fraction(1) - p
    return Fraction(1) - q ** NEED - NEED * p * q ** (NEED - 1)


def frac_to_decimal(f):
    return Decimal(f.numerator) / Decimal(f.denominator)


# ---------------------------------------------------------------- 5 self-tests

def _syn(slug="btc-updown-15m-1788998400", ptb="78275.35460685384", closed="true",
         outcomes='["Up", "Down"]', prices='["1", "0"]', drop_ptb=False):
    md = "{}" if drop_ptb else '{"finalPrice": 1.0, "priceToBeat": %s}' % ptb
    return ('{"slug": %s, "closed": %s, "outcomes": %s, "outcomePrices": %s, '
            '"resolutionSource": "chainlink", "events": [{"eventMetadata": %s}]}'
            % (json.dumps(slug), closed, json.dumps(outcomes), json.dumps(prices), md)
            ).encode("utf-8")


def selftests():
    start = ASSERTS["n"]

    # S1
    A(slug15(1788998400) == "btc-updown-15m-1788998400", "S1 slug15")
    A(slug5(1788999000) == "btc-updown-5m-1788999000", "S1 slug5")

    # S2
    gen = candidates(start=1789668900, cap=2)
    first = next(gen)
    A(first == (0, 1789668900), "S2 first candidate")
    raised = False
    try:
        next(gen)
    except ValueError:
        raised = True
    A(raised, "S2 raises before the second candidate, whose window ends at 1789670700")
    full = list(candidates(start=START_T, cap=CANDIDATE_CAP))
    A(len(full) == CANDIDATE_CAP and max(T + 900 for _, T in full) == LARGEST_EPOCH,
      "S2 400 candidates, largest requested epoch 1789358400")

    # S3 - twelve cases, in 3.2's order
    ok_slug = "btc-updown-15m-1788998400"
    cases = [
        ((200, parse_body(_syn()), ok_slug), "ok"),
        ((200, parse_body(b"[1, 2]"), ok_slug), "json"),
        ((200, parse_body(_syn()), "btc-updown-15m-1789000000"), "slug"),
        ((200, parse_body(_syn(closed="false")), ok_slug), "open"),
        ((200, parse_body(_syn(drop_ptb=True)), ok_slug), "no-ptb"),
        ((200, parse_body(_syn(ptb="-1.5")), ok_slug), "ptb-range"),
        ((200, parse_body(_syn(ptb="64123")), ok_slug), "precision"),
        ((200, parse_body(_syn(prices='["0.5", "0.5"]')), ok_slug), "unresolved"),
        ((200, parse_body(_syn(outcomes='["Yes", "No"]')), ok_slug), "unresolved"),
        ((404, None, ok_slug), "absent"),
        ((500, None, ok_slug), "status"),
        ((None, None, ok_slug), "fetch"),
    ]
    for args, want in cases:
        A(validity(*args) == want, "S3 %s" % want)

    # S4 - I1 at live magnitude
    A(identity_1(Decimal("64123.451234567891"), Decimal("64123.451234567891")), "S4 equal")
    A(not identity_1(Decimal("64123.451234567891"), Decimal("64123.451234567892")), "S4 1E-12")
    A(identity_1(Decimal("64123.45"), Decimal("64123.451234")), "S4 coarser literal")
    A(not identity_1(Decimal("64123.45"), Decimal("64123.4612")), "S4 beyond the coarser literal")

    # S5
    A(expected_outcome(Decimal("64123.451234567891"), Decimal("64123.451234567891")) == "Up",
      "S5 equality resolves Up")

    # S6
    A(reading(200, 200) == "PASS", "S6 200")
    A(reading(199, 200) == "PASS", "S6 199")
    A(reading(198, 200) == "FAIL", "S6 198")
    A(reading(None, 150) == "UNDECIDABLE", "S6 undecidable")

    # S7
    seq = ["ok", "fetch", "ok", "ok", "open", "ok"]
    got = form_set(lambda k: seq[k], range(len(seq)), 3)
    A(got["members"] == [0, 2, 3], "S7 members")
    A(got["considered"] == [0, 1, 2, 3], "S7 stops after k = 3")
    A(got["nonmembers"] == [(1, "fetch")], "S7 non-member")

    # S8
    A(abs(frac_to_decimal(power(Fraction(1, 50))) - Decimal(POWER_2PCT)) < POWER_TOL, "S8 p=1/50")
    A(abs(frac_to_decimal(power(Fraction(1, 100))) - Decimal(POWER_1PCT)) < POWER_TOL, "S8 p=1/100")
    A(power(Fraction(0)) == 0, "S8 p=0")

    # S9 - the instrument's own syntax tree
    with open(os.path.realpath(__file__), "rb") as fh:
        src = fh.read()
    tree = ast.parse(src)
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for al in node.names:
                mods.add(al.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0 and node.module:
                mods.add(node.module.split(".")[0])
    A(mods and mods <= set(sys.stdlib_module_names), "S9 every import is stdlib: %s" % sorted(mods))
    A("subprocess" not in mods, "S9 no subprocess")
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) \
                and node.value.id == "os":
            if node.attr in ("system", "popen") or node.attr.startswith("spawn") \
                    or node.attr.startswith("exec"):
                bad.append(node.attr)
    A(not bad, "S9 no process attribute on os: %s" % bad)
    shells = [kw.arg for node in ast.walk(tree) if isinstance(node, ast.Call)
              for kw in node.keywords if kw.arg == "shell"]
    A(not shells, "S9 no shell keyword")
    urls = [node.value for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, str)
            and SCHEME_SEP in node.value]
    A(len(urls) == 1 and urls[0] == ENDPOINT, "S9 exactly one endpoint literal: %d" % len(urls))

    return ASSERTS["n"] - start


# ---------------------------------------------------------------- fingerprint gate

def map_text(root):
    with open(os.path.join(root, "SYSTEM-MAP.md"), "r", encoding="utf-8") as fh:
        return fh.read()


def parse_map(text):
    m = re.search(r"\*\*Revision string:\*\*\s+`([^`]+)`", text)
    rev = m.group(1) if m else None
    head = text.split("### Fingerprint table")[0]
    anchors = {}
    for row in re.finditer(r"^\|\s*`(A[1-6])`[^|]*\|\s*`([^`]+)`\s*\|\s*$", head, re.M):
        anchors[row.group(1)] = row.group(2)
    lines = text.splitlines()
    idx = None
    for i, line in enumerate(lines):
        if line.startswith("### Fingerprint table"):
            idx = i
            break
    rows, started = [], False
    for line in lines[idx:]:
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 5 and cells[0].startswith("`"):
                sha = re.search(r"([0-9a-f]{64})", cells[4])
                rows.append({
                    "path": cells[0].strip("`"),
                    "lines": cells[1],
                    "bytes": cells[2],
                    "state": cells[3],
                    "sha": sha.group(1) if sha else None,
                })
                started = True
        elif started and not line.strip():
            break
    return rev, anchors, rows


def fingerprint_gate(root, echo=True):
    text = map_text(root)
    rev, anchors, rows = parse_map(text)
    A(rev == REQUIRED_REVISION, "V1 revision %r" % rev)
    A(len(anchors) == 6, "V1 six anchors, read %d" % len(anchors))
    for name in sorted(ANCHORS):
        A(anchors.get(name) == ANCHORS[name],
          "V1 anchor %s: %r" % (name, anchors.get(name)))
    for name in sorted(ANCHOR_SOURCES):
        got = sha256_file(os.path.join(root, ANCHOR_SOURCES[name]))[:12]
        A(got == ANCHORS[name], "V1 anchor %s re-derived %s" % (name, got))
    A(len(rows) == TABLE_ROWS, "V1 %d rows, expected %d" % (len(rows), TABLE_ROWS))
    frozen = 0
    report = []
    for row in rows:
        path = os.path.join(root, row["path"])
        with open(path, "rb") as fh:
            data = fh.read()
        got = sha256_bytes(data)
        nl = data.count(b"\n")
        report.append((row["path"], nl, len(data), row["state"], got))
        if row["state"] == "frozen":
            frozen += 1
            A(got == row["sha"], "V1 frozen row %s: %s" % (row["path"], got))
    A(frozen == FROZEN_ROWS, "V1 %d frozen rows, expected %d" % (frozen, FROZEN_ROWS))
    if echo:
        print("## fingerprint")
        print("revision %s | anchors %d of %d | rows %d | frozen %d of %d"
              % (rev, len(anchors), 6, len(rows), frozen, FROZEN_ROWS))
        for name in sorted(anchors):
            print("anchor %s %s" % (name, anchors[name]))
        print("%-44s %7s %9s %-9s %s" % ("path", "wc -l", "bytes", "state", "sha256"))
        for path, nl, size, state, got in report:
            print("%-44s %7d %9d %-9s %s" % (path, nl, size, state, got))
    return report


# ---------------------------------------------------------------- 3.4 Stage F

PACE = {"last": 0.0}


def pace():
    wait = PACE["last"] + PACE_S - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    PACE["last"] = time.monotonic()


def http_once(slug):
    req = urllib.request.Request(
        ENDPOINT + slug,
        headers={"Accept": "application/json", "User-Agent": USER_AGENT},
    )
    t0 = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_S) as resp:
            body = resp.read()
            return resp.status, body, None, dict(resp.headers), (time.monotonic() - t0) * 1000.0
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read()
        except Exception:
            body = b""
        return exc.code, body, None, dict(exc.headers or {}), (time.monotonic() - t0) * 1000.0
    except Exception as exc:
        return None, b"", type(exc).__name__, {}, (time.monotonic() - t0) * 1000.0


def retry_wait(attempt, headers):
    base = (5, 10, 20)[min(attempt, 2)]
    ra = headers.get("Retry-After") if headers else None
    if ra:
        try:
            base = int(str(ra).strip())
        except ValueError:
            pass
    return min(base, 60)


class Fetcher:
    """Stage F's one request path: pacing, P3, retries and the index line."""

    def __init__(self, raw_dir, index_path, deadline=None):
        self.raw_dir = ensure_dir(raw_dir)
        self.index_path = index_path
        self.deadline = deadline
        self.requests = 0
        self.attempts = 0
        self.retries = 0
        self.lines = 0
        self.by_status = {}
        self.by_kind = {}
        self.consecutive_fail = 0

    def fetch(self, slug):
        check_p3(slug)
        if self.deadline is not None and time.monotonic() > self.deadline:
            raise WallClock("Stage F passed its %.0f s wall clock" % STAGE_F_WALL_S)
        self.requests += 1
        kind, _ = epoch_of(slug)
        self.by_kind[kind] = self.by_kind.get(kind, 0) + 1
        status = body = error = None
        headers = {}
        for attempt in range(4):
            pace()
            status, body, error, headers, elapsed = http_once(slug)
            self.attempts += 1
            line = json.dumps({
                "slug": slug,
                "attempt": attempt,
                "status": status,
                "error": error,
                "bytes": len(body),
                "sha256": sha256_bytes(body),
                "t_utc": now_iso(),
                "elapsed_ms": round(elapsed, 3),
            }, sort_keys=True)
            append_text(self.index_path, line + "\n")
            self.lines += 1
            retriable = status is None or status == 429 or (status is not None and status >= 500)
            if not retriable or attempt == 3:
                break
            self.retries += 1
            time.sleep(retry_wait(attempt, headers))
        key = "null" if status is None else str(status)
        self.by_status[key] = self.by_status.get(key, 0) + 1
        if status is not None:
            write_bytes(os.path.join(self.raw_dir, slug + ".body"), body)
        if status is None or status != 200:
            self.consecutive_fail += 1
            if self.consecutive_fail >= FAILFAST_RUN:
                raise FailFast("%d consecutive requests ended in fetch or status" % FAILFAST_RUN)
        else:
            self.consecutive_fail = 0
        return status, body


def diagnose(store, T):
    """The BLOCKED disclosure of 3.3's early stop, for one candidate."""
    out = []
    for slug in all_slugs(T):
        status, doc = store.get(slug, (None, None))
        row = {"slug": slug, "status": status,
               "json_type": type(doc).__name__ if doc is not None else "none",
               "code": validity(status, doc, slug)}
        if isinstance(doc, dict):
            row["top_level_keys"] = sorted(doc.keys())
            ev = doc.get("events")
            if isinstance(ev, list) and ev and isinstance(ev[0], dict):
                row["events_0_keys"] = sorted(ev[0].keys())
                md = ev[0].get("eventMetadata")
                if isinstance(md, dict):
                    row["event_metadata_keys"] = sorted(md.keys())
        out.append(row)
    return out


def stage_f():
    assert not os.path.exists(INDEX_PATH), \
        "Stage F: %s exists; re-run 6 requires an empty raw/ and no index" % INDEX_PATH
    ensure_dir(WORK)
    ensure_dir(RAW_DIR)
    A(free_bytes(WORK) >= SPACE_FLOOR, "V2 resource gate at R1's start")
    start_free = free_bytes(WORK)
    print("## R1 start")
    print("free_bytes_start %d" % start_free)
    t_start = time.monotonic()
    fetcher = Fetcher(RAW_DIR, INDEX_PATH, deadline=t_start + STAGE_F_WALL_S)
    store = {}
    bodies = {}

    def code_of(slug):
        status, doc = store[slug]
        return validity(status, doc, slug)

    def ensure(slug):
        if slug in store:
            return
        status, body = fetcher.fetch(slug)
        store[slug] = (status, parse_body(body) if status is not None else None)
        bodies[slug] = body

    state = {"ok": 0}

    def qualify(k):
        T = START_T + 900 * k
        for slug in all_slugs(T):
            ensure(slug)
        code = candidate_code(code_of, T)
        if code == "ok":
            state["ok"] += 1
        if k == EARLY_STOP_K and state["ok"] == 0:
            raise EarlyStop("none of candidates 0 to %d qualifies" % EARLY_STOP_K)
        return code

    ks = [k for k, _ in candidates()]
    stop_reason = "complete"
    try:
        found = form_set(qualify, ks, NEED)
    except EarlyStop as exc:
        payload = {"blocked": "early-stop", "detail": str(exc),
                   "candidate_0": diagnose(store, START_T)}
        print("## BLOCKED early stop")
        print(json.dumps(payload, indent=1, sort_keys=True))
        raise
    wall = time.monotonic() - t_start

    members = [START_T + 900 * k for k in found["members"]]
    member_sha = sha256_bytes("\n".join(str(T) for T in members).encode("ascii"))
    if not found["complete"]:
        stop_reason = "fewer than %d qualifying candidates" % NEED

    A(fetcher.requests <= MAX_STAGE_F_REQUESTS,
      "V4 Stage F issued %d requests" % fetcher.requests)
    A(P3["checks"] == fetcher.requests, "V3 P3 checked %d times for %d requests"
      % (P3["checks"], fetcher.requests))
    A(P3["max_5m"] <= LARGEST_EPOCH, "V3 largest 5m epoch %d" % P3["max_5m"])

    # stability re-fetch - the four gate documents of the first 10 members
    ensure_dir(REFETCH_DIR)
    refetch = Fetcher(REFETCH_DIR, REFETCH_INDEX_PATH, deadline=None)
    compared = 0
    differing_bytes = 0
    for T in members[:REFETCH_MEMBERS]:
        for slug in gate_slugs(T):
            status, body = refetch.fetch(slug)
            doc2 = parse_body(body) if status is not None else None
            status1, doc1 = store[slug]
            k1, k2 = K(doc1), K(doc2)
            same = (
                status == status1
                and isinstance(doc2, dict)
                and (k1.as_tuple() if k1 is not None else None)
                == (k2.as_tuple() if k2 is not None else None)
                and doc1.get("closed") == doc2.get("closed")
                and doc1.get("outcomes") == doc2.get("outcomes")
                and doc1.get("outcomePrices") == doc2.get("outcomePrices")
            )
            A(same, "V8 re-fetch differs for %s" % slug)
            compared += 1
            if body != bodies[slug]:
                differing_bytes += 1
    A(refetch.requests == REFETCH_REQUESTS, "V4 re-fetch %d requests" % refetch.requests)
    A(compared == REFETCH_REQUESTS, "V8 %d of %d" % (compared, REFETCH_REQUESTS))
    A(fetcher.attempts == fetcher.lines, "V4 every Stage F attempt has an index line")
    A(refetch.attempts == refetch.lines, "V4 every re-fetch attempt has a refetch line")
    rehashed = rehash_raw(RAW_DIR, INDEX_PATH)

    end_free = free_bytes(WORK)
    A(end_free >= SPACE_FLOOR, "V2 resource gate at R1's end")
    A(WRITES["bytes"] <= WRITE_CAP, "V9 bytes written %d" % WRITES["bytes"])

    summary = {
        "candidates_considered": len(found["considered"]),
        "member_count": len(members),
        "member_list": members,
        "member_list_sha256": member_sha,
        "set_complete": found["complete"],
        "stop_reason": stop_reason,
        "requests_stage_f": fetcher.requests,
        "requests_refetch": refetch.requests,
        "attempts_stage_f": fetcher.attempts,
        "attempts_refetch": refetch.attempts,
        "retries_stage_f": fetcher.retries,
        "retries_refetch": refetch.retries,
        "requests_by_status": fetcher.by_status,
        "requests_by_market_type": fetcher.by_kind,
        "refetch_by_status": refetch.by_status,
        "refetch_by_market_type": refetch.by_kind,
        "refetch_bodies_differing_in_bytes": differing_bytes,
        "wall_clock_s": round(wall, 3),
        "bytes_written": WRITES["bytes"],
        "free_bytes_start": start_free,
        "free_bytes_end": end_free,
        "largest_requested_5m_epoch": P3["max_5m"],
        "largest_requested_15m_epoch": P3["max_15m"],
        "p3_checks": P3["checks"],
        "write_guard_checks": WRITES["checks"],
        "raw_bodies_rehashed": rehashed,
    }
    forbidden = {"I1", "I2", "I3", "holds", "N"}
    A(not (set(summary) & forbidden), "V13 fetch-summary.json carries a forbidden key")
    write_bytes(FETCH_SUMMARY_PATH,
                (json.dumps(summary, indent=1, sort_keys=True) + "\n").encode("utf-8"))

    print("## R1 done")
    for key in sorted(summary):
        if key == "member_list":
            continue
        print("%s %s" % (key, json.dumps(summary[key], sort_keys=True)))
    print("free_bytes_end %d" % end_free)
    print("V8 %d of %d" % (compared, REFETCH_REQUESTS))
    return summary


def rehash_raw(raw_dir, index_path):
    """V4: every stored body re-hashes to its index line's sha256."""
    final = {}
    with open(index_path, "r", encoding="utf-8") as fh:
        for line in fh:
            rec = json.loads(line)
            final[rec["slug"]] = rec
    checked = 0
    for slug, rec in sorted(final.items()):
        path = os.path.join(raw_dir, slug + ".body")
        if rec["status"] is None:
            continue
        with open(path, "rb") as fh:
            data = fh.read()
        A(sha256_bytes(data) == rec["sha256"] and len(data) == rec["bytes"],
          "V4 stored body %s does not re-hash" % slug)
        checked += 1
    return checked


# ---------------------------------------------------------------- 3.5 to 3.7 Stage A

def load_store(raw_dir, index_path):
    final = {}
    with open(index_path, "r", encoding="utf-8") as fh:
        for line in fh:
            rec = json.loads(line)
            final[rec["slug"]] = rec
    store, shas = {}, {}
    for slug, rec in final.items():
        if rec["status"] is None:
            store[slug] = (None, None)
            shas[slug] = ""
            continue
        with open(os.path.join(raw_dir, slug + ".body"), "rb") as fh:
            data = fh.read()
        store[slug] = (rec["status"], parse_body(data))
        shas[slug] = rec["sha256"]
    return store, shas


def dec(x):
    return "" if x is None else str(x)


def flag(x):
    return "" if x is None else ("1" if x else "0")


def bump(table, key):
    table[key] = table.get(key, 0) + 1


def stage_a(out_dir):
    t0 = time.monotonic()
    rehashed = rehash_raw(RAW_DIR, INDEX_PATH)
    store, shas = load_store(RAW_DIR, INDEX_PATH)

    def code_of(slug):
        status, doc = store[slug]
        return validity(status, doc, slug)

    present = set(store)
    ks = []
    for k, T in candidates():
        if not all(slug in present for slug in all_slugs(T)):
            break
        ks.append(k)
    found = form_set(lambda k: candidate_code(code_of, START_T + 900 * k), ks, NEED)
    member_ks = set(found["members"])
    members = [START_T + 900 * k for k in found["members"]]
    member_sha = sha256_bytes("\n".join(str(T) for T in members).encode("ascii"))

    rows = []
    N = 0
    counts = {"I1": 0, "I2": 0, "I3": 0}
    d1_members, d1_count = [], 0
    d2 = {"I4a_holds": 0, "I4a_checks": 0, "I4b_holds": 0, "I4b_checks": 0, "excluded": 0}
    d3 = {"K15": {}, "K5a": {}, "K5c": {}, "K5d": {}}
    d4 = {"near_d15": 0, "near_d5": 0}
    d5 = {"15m": {}, "5m": {}}
    d6 = {"15m": {}, "5m": {}}
    d7 = {}

    for slug, (status, doc) in store.items():
        if validity(status, doc, slug) != "ok":
            continue
        kind, _ = epoch_of(slug)
        for key in sorted(doc["events"][0]["eventMetadata"].keys()):
            bump(d5[kind], key)
        src = doc.get("resolutionSource")
        bump(d6[kind], "absent" if src is None else str(src)[:200])

    for k in found["considered"]:
        T = START_T + 900 * k
        s15, s5a, s5b, s5c, s5d = all_slugs(T)
        docs = {name: store[slug] for name, slug in
                (("M15", s15), ("M5a", s5a), ("M5b", s5b), ("M5c", s5c), ("M5d", s5d))}
        codes = {name: validity(st, dc, slug) for (name, (st, dc)), slug in
                 zip(docs.items(), (s15, s5a, s5b, s5c, s5d))}
        is_member = k in member_ks
        reason = "ok" if is_member else candidate_code(code_of, T)
        if not is_member:
            bump(d7, reason)

        def lit(name):
            st, dc = docs[name]
            return K(dc) if codes[name] == "ok" else None

        def out(name):
            st, dc = docs[name]
            return O(dc) if codes[name] == "ok" else None

        K15, K5a, K5b, K5c, K5d = (lit(n) for n in ("M15", "M5a", "M5b", "M5c", "M5d"))
        O15, O5a, O5b, O5c = (out(n) for n in ("M15", "M5a", "M5b", "M5c"))

        i1 = i2 = i3 = holds = i1x = None
        d15 = d5v = None
        if is_member:
            i1 = identity_1(K15, K5a)
            i2 = (O15 == expected_outcome(K5d, K15))
            i3 = (O5c == expected_outcome(K5d, K5c))
            holds = bool(i1 and i2 and i3)
            i1x = (K15 == K5a)
            d15 = K5d - K15
            d5v = K5d - K5c
            counts["I1"] += int(i1)
            counts["I2"] += int(i2)
            counts["I3"] += int(i3)
            N += int(holds)
            if i1x:
                d1_count += 1
                d1_members.append(T)
            if abs(d15) < 1:
                d4["near_d15"] += 1
            if abs(d5v) < 1:
                d4["near_d5"] += 1
            for name, val in (("K15", K15), ("K5a", K5a), ("K5c", K5c), ("K5d", K5d)):
                bump(d3[name], str(exponent(val)))

        i4a = i4b = None
        if is_member:
            if codes["M5b"] == "ok":
                i4a = (O5a == expected_outcome(K5b, K5a))
                i4b = (O5b == expected_outcome(K5c, K5b))
                d2["I4a_checks"] += 1
                d2["I4b_checks"] += 1
                d2["I4a_holds"] += int(i4a)
                d2["I4b_holds"] += int(i4b)
            else:
                d2["excluded"] += 1

        rows.append(",".join([
            str(k), str(T), flag(is_member), reason,
            dec(K15), dec(K5a), dec(K5c), dec(K5d),
            O15 or "", O5c or "",
            flag(i1), flag(i2), flag(i3), flag(holds), flag(i1x),
            dec(K5b), O5a or "", O5b or "", flag(i4a), flag(i4b),
            dec(d15), dec(d5v),
            shas.get(s15, ""), shas.get(s5a, ""), shas.get(s5b, ""),
            shas.get(s5c, ""), shas.get(s5d, ""),
        ]))

    complete = found["complete"]
    verdict = reading(N if complete else None, len(members))

    ensure_dir(out_dir)
    csv_text = CSV_HEADER + "\n" + "\n".join(rows) + "\n"
    csv_path = os.path.join(out_dir, "tz17-candidates.csv")
    write_bytes(csv_path, csv_text.encode("utf-8"))

    summary = {
        "N": N if complete else None,
        "reading": verdict,
        "set_complete": complete,
        "member_count": len(members),
        "member_list_sha256": member_sha,
        "candidates_considered": len(found["considered"]),
        "I1_holds": counts["I1"],
        "I2_holds": counts["I2"],
        "I3_holds": counts["I3"],
        "D1_I1_exact_count": d1_count,
        "D1_I1_exact_members": d1_members,
        "D2_I4a_holds": d2["I4a_holds"],
        "D2_I4a_checks": d2["I4a_checks"],
        "D2_I4b_holds": d2["I4b_holds"],
        "D2_I4b_checks": d2["I4b_checks"],
        "D2_excluded": d2["excluded"],
        "D3_exponents": d3,
        "D4_near_strike_d15": d4["near_d15"],
        "D4_near_strike_d5": d4["near_d5"],
        "D5_event_metadata_keys": d5,
        "D6_resolution_source": d6,
        "D7_nonmember_first_code": d7,
        "largest_requested_5m_epoch": max(
            (epoch_of(s)[1] for s in store if s.startswith("btc-updown-5m-")), default=0),
        "power_rate_0.02": str(frac_to_decimal(power(Fraction(1, 50))).quantize(Decimal(POWER_2PCT))),
        "power_rate_0.01": str(frac_to_decimal(power(Fraction(1, 100))).quantize(Decimal(POWER_1PCT))),
        "gate_fail_at_or_below": 198,
        "gate_pass_at_or_above": PASS_MIN,
        "raw_bodies_rehashed": rehashed,
    }
    json_path = os.path.join(out_dir, "tz17-summary.json")
    write_bytes(json_path, (json.dumps(summary, indent=1, sort_keys=True) + "\n").encode("utf-8"))

    wall = time.monotonic() - t0
    A(wall <= STAGE_A_WALL_S, "Stage A passed its %.0f s bound" % STAGE_A_WALL_S)
    A(WRITES["bytes"] <= WRITE_CAP, "V9 bytes written %d" % WRITES["bytes"])

    # V5 against R1's own member list
    with open(FETCH_SUMMARY_PATH, "r", encoding="utf-8") as fh:
        fetch_summary = json.load(fh)
    A(fetch_summary["member_list_sha256"] == member_sha,
      "V5 member list differs from R1's")
    A(fetch_summary["member_list"] == members, "V5 member list differs from R1's, unit by unit")

    print("## Stage A")
    print("out %s" % out_dir)
    print("wall_clock_s %.3f" % wall)
    print("candidates_considered %d" % len(found["considered"]))
    print("member_count %d" % len(members))
    print("member_list_sha256 %s" % member_sha)
    print("N %s" % (N if complete else "null"))
    print("reading %s" % verdict)
    print("I1 %d of %d | I2 %d of %d | I3 %d of %d"
          % (counts["I1"], len(members), counts["I2"], len(members),
             counts["I3"], len(members)))
    print("csv_sha256 %s %d bytes" % (sha256_bytes(csv_text.encode("utf-8")), len(csv_text)))
    print("json_sha256 %s" % sha256_file(json_path))
    print("bytes_written %d | write_guard_checks %d" % (WRITES["bytes"], WRITES["checks"]))
    print("raw_bodies_rehashed %d" % rehashed)
    return summary


# ---------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description="TZ-17 settlement chain")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--analyze", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)

    n = selftests()
    print("## self-tests")
    print("%d of %d" % (n, n))
    if args.selftest:
        return 0

    root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    fingerprint_gate(root)

    if args.fetch:
        stage_f()
    if args.analyze:
        if not args.out:
            raise SystemExit("--analyze needs --out")
        stage_a(args.out)
    if not (args.fetch or args.analyze):
        raise SystemExit("nothing to do: pass --selftest, --fetch or --analyze")
    return 0


if __name__ == "__main__":
    sys.exit(main())
