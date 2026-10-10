#!/usr/bin/env python3
"""TZ-24 - the backup track's B2: does the nesting of btc-updown-5m-{T+600} inside btc-updown-15m-{T}
break on executable quotes, after both legs' taker fees?

    fingerprint       map section 0 against the primary checkout: the revision, the six anchors, four of
                      them re-derived, and every row of the table, each frozen row asserted equal
    selftest          every rule of this file, on literals and on a synthetic chain book
    still             both capture units: the first run records MainPID, NRestarts and ActiveState, the
                      second compares (G-STILL)
    scratch OWN       the UUID directories beside OWN, this session's directory: live or earlier
    rehearse          the document path over TZ-17's 200 windows, against the Architect's figures
                      (G-REHEARSAL)
    fetch             the set: every window T = 1790184600 ... 1791241200, its window.json and its two
                      settled documents (G-SET)
    constants         book-free: the members, N, NONE's alternative and the powers, on disk
    score             the members' books, read once a run, and the reading
    reclaim TREE...   section 9

It requests gamma-api.polymarket.com/markets and nothing else, every request with the two headers HEADERS
fixes. Under /var/lib/btc-recorder it opens nothing. Under /var/lib/btc-chainbook it opens, read only, a
considered window's window.json and - in `score` alone, after its two preconditions - its books.jsonl.gz:
an audit hook refuses every other open under either root. It writes under /root/tz24-work/ and, in
`reclaim`, new files in /root/btc-forensics/ by exclusive create. Exit 0: every assert of the mode held.
Exit 1: an assert failed, and its message names it. Run it with the research interpreter, /root/tz01-env,
which research/tz14-quote-inventory.py needs.

Written for CryptoTZ/TZ-24-nesting-b2.md. The TZ is the specification.
"""

import datetime
import gzip
import hashlib
import importlib.util
import io
import json
import os
import re
import resource
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zlib
from decimal import Decimal as D, getcontext

if not __debug__:
    sys.stderr.write("tz24: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

getcontext().prec = 60

# ---- the TZ's constants ------------------------------------------------------------------------

FIRST_T = 1790184600         # 2026-09-23 17:30 UTC: the first window TZ-18a's service fetched documents for
LAST_T = 1791241200          # 2026-10-05 23:00 UTC: its five-minute market, 1791241800, is M0's last member
WINDOW = 900
CONSIDERED = (LAST_T - FIRST_T) // WINDOW + 1
OFFSETS = (655, 715, 775, 805, 835, 865, 885)   # the chain book's seven checkpoints after T
TAUS = tuple(WINDOW - o for o in OFFSETS)       # seconds left to T + 900: 245, 185, 125, 95, 65, 35, 15
SECOND_SPAN = 1791099000     # the first window after the chain book's restart under its unit
CHUNK = 20                   # slugs a gamma request: ten windows
ALPHA = D("0.005")           # NONE's false-reading probability
N_MIN = 528                  # the fewest members at which NONE's alternative is at most 1 window in 100
THETAS = (D("0.001"), D("0.005"), D("0.01"))
SKEW_BOUND_NS = 150000000    # the two legs received at most 150 ms apart: CANON section 1.1's taker delay
TS_BOUND_MS = 150            # and the two books' own timestamps at most 150 ms apart
ROWS_SHOWN = 40              # firm and loose units printed in full, each class, in member order
FEE_TYPE = "crypto_fees_v2"
FEE_SCHEDULE = {"exponent": 1, "rate": D("0.07"), "takerOnly": True, "rebateRate": D("0.2")}
MEM_FLOOR = 141189120        # MemAvailable below which a mode that reads the venue or the capture stops
FETCH_BUDGET_S = 900         # a fetch projected past this after its first 20 requests is BLOCKED
UA = "btc-5m-twap-b2/TZ-24"
HEADERS = {"User-Agent": UA, "Accept": "application/json"}
GAMMA = "https://gamma-api.polymarket.com/markets"
REHEARSAL = (1788998400, 200)    # TZ-17's 200 windows, 1788998400 ... 1789177500

# The Architect's independent figures for the rehearsal: TZ-17's committed CSV, and the venue's documents
# re-fetched one a request by a script that shares no code with this file (TZ-24 section 4.1).
REF = {
    "windows": 200, "members": 200, "d_pos": 102, "d_neg": 98, "d_zero": 0, "up15": 98, "up5": 102,
    "sum_d": D("-2198.32154130825"), "sum_abs_d": D("19953.70645914237"),
    "digest": "a9b57a6ea03fa6d57d964afcf1aa17da463547a5bf216069430d25d99cf1b3ee",
}

MAP_REVISION = "2026-10-10-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 30, "tracked": 2, "reported": 1}

UNITS = {"recorder": "btc-recorder.service", "chainbook": "btc-chainbook.service"}
WORK = "/root/tz24-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/book-ledger.jsonl"
BRANCH = "tz-24-nesting-b2"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
CHAINBOOK = "/var/lib/btc-chainbook"
RECORDER = "/var/lib/btc-recorder"
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
CONDITION = re.compile(r"0x[0-9a-f]{64}")
LIVE_S = 60                  # a directory born this soon after a claude process started is that process's

# The chain book's book line, research/tz18a-chainbook-capture.py BOOK_KEYS, and the two legs of each pair.
BOOK_KEYS = frozenset(("T", "tau_prime", "market", "slug", "token_id", "outcome_label", "url", "status",
                       "send_mono_ns", "recv_mono_ns", "recv_wall_ns", "bytes", "sha256", "raw",
                       "reason"))
LEGS = {"A": (("m15", "Up"), ("m5", "Down")),     # D > 0: Up of the 5m implies Up of the 15m
        "B": (("m5", "Up"), ("m15", "Down"))}     # D < 0: Up of the 15m implies Up of the 5m

HERE = os.path.dirname(os.path.abspath(__file__))
_TZ14 = []


def tz14():
    """research/tz14-quote-inventory.py, loaded once, on first use: the only implementation of the taker fee,
    `fee_pp`, and of the executable touch, `touch_of`, with `book_of`, which parses a reply for it. Loading it
    writes three thread-count variables, loads tz12 and everything below it, and installs an audit hook that
    records opens under /var/lib/btc-recorder; this file reads that record only to print its length."""
    if not _TZ14:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        spec = importlib.util.spec_from_file_location(
            "tz14quoteinventory", os.path.join(HERE, "tz14-quote-inventory.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _TZ14.append(mod)
    return _TZ14[0]


def _malloc_tune():
    """glibc's mmap threshold fixed at 128 KiB and two arenas, as TZ-23 fixed them. True where both took."""
    try:
        import ctypes
        libc = ctypes.CDLL("libc.so.6")
        return libc.mallopt(-3, 131072) == 1 and libc.mallopt(-8, 2) == 1
    except (OSError, AttributeError):
        return False


MALLOC_TUNED = _malloc_tune()

# ---- the audit hook ------------------------------------------------------------------------------

REFUSED = []
CB_OPENS = {"window.json": 0, "books.jsonl.gz": 0}
BOOKS_OPEN = [False]         # set by `score` alone, after its two preconditions
CB_PATH = re.compile(r"/var/lib/btc-chainbook/([0-9]{10})/(window\.json|books\.jsonl\.gz)")
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC


def cb_decision(path, mode, flags, books_open):
    """TZ-24 section 2, item 3, as a pure function of one open under the chain book: 'allow' or the
    reason it is refused."""
    m = CB_PATH.fullmatch(path)
    if m is None:
        return "not a window's window.json or books.jsonl.gz"
    if isinstance(mode, str):
        if set(mode) & set("wax+"):
            return "not read-only"
    elif not (isinstance(flags, int) and flags & WRITE_FLAGS == 0):
        return "not read-only"
    t = int(m.group(1))
    if not (FIRST_T <= t <= LAST_T and (t - FIRST_T) % WINDOW == 0):
        return "not a considered window"
    if m.group(2) == "books.jsonl.gz" and not books_open:
        return "a book before score's preconditions"
    return "allow"


def _audit(event, args):
    if event != "open" or not args:
        return
    p = args[0]
    if isinstance(p, bytes):
        p = os.fsdecode(p)
    if not isinstance(p, str):
        return
    path = os.path.abspath(p)
    if path == RECORDER or path.startswith(RECORDER + "/"):
        REFUSED.append(path)
        raise RuntimeError("open refused under the recorder's root: %s" % path)
    if path == CHAINBOOK or path.startswith(CHAINBOOK + "/"):
        why = cb_decision(path, args[1] if len(args) > 1 else None,
                          args[2] if len(args) > 2 else None, BOOKS_OPEN[0])
        if why != "allow":
            REFUSED.append(path)
            raise RuntimeError("open refused under the chain book's root, %s: %s" % (why, path))
        CB_OPENS[os.path.basename(path)] += 1


sys.addaudithook(_audit)

# ---- small helpers -------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))


def iso(t):
    return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fx(x):
    """A Decimal as fixed-point text, never in exponent form."""
    return format(x, "f")


def lit(x):
    """A venue number as the text of its literal: a Decimal of its own text, or an int."""
    assert isinstance(x, (D, int)) and not isinstance(x, bool), type(x)
    return str(x)


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def write_atomic(path, data):
    tmp = path + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(data)
    os.replace(tmp, path)


def write_once(path, data):
    """The first run writes; a later run must produce the same bytes (determinism, contract section 6)."""
    if os.path.exists(path):
        got = sha256_file(path)
        assert got == sha256_bytes(data), "determinism: %s differs from the first run" % path
        out("unchanged %s sha256 %s" % (path, got))
        return got
    write_atomic(path, data)
    return sha256_bytes(data)


def gz_bytes(data):
    """Deterministic gzip: no name, no time."""
    buf = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buf, mtime=0) as g:
        g.write(data)
    return buf.getvalue()


def _dec(o):
    if isinstance(o, D):
        return fx(o)
    raise TypeError(type(o))


def dumps(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=_dec) + "\n"


def loads_maybe(v):
    """A field the venue sends as JSON text inside JSON, parsed; anything else as it is."""
    if isinstance(v, str):
        try:
            return json.loads(v)
        except ValueError:
            return None
    return v


def mem_available():
    with open("/proc/meminfo", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) * 1024
    raise AssertionError("no MemAvailable")


def floor_check():
    """Before a mode that reads the venue or the capture: glibc's two settings, and the memory floor."""
    assert MALLOC_TUNED, "BLOCKED: glibc did not take the mmap threshold and the arena count"
    avail = mem_available()
    out("MemAvailable %d bytes, floor %d" % (avail, MEM_FLOOR))
    assert avail >= MEM_FLOOR, "BLOCKED: MemAvailable %d bytes, below %d" % (avail, MEM_FLOOR)


def load_state():
    if not os.path.exists(STATE):
        return {}
    with open(STATE, encoding="utf-8") as fh:
        return json.load(fh)


def save_state(state):
    write_atomic(STATE, (json.dumps(state, sort_keys=True, indent=1) + "\n").encode("utf-8"))


def slug15(t):
    return "btc-updown-15m-%d" % t


def slug5(t):
    return "btc-updown-5m-%d" % t


def quantiles(values):
    """min, the nearest-rank median and max of a list, or None where it is empty."""
    if not values:
        return None
    v = sorted(values)
    return {"n": len(v), "min": v[0], "median": v[(len(v) - 1) // 2], "max": v[-1]}

# ---- the venue -----------------------------------------------------------------------------------


def http_json(url, tries=8):
    """One GET with HEADERS: the body's bytes and its JSON, every number a Decimal of its own text. 429,
    5xx and transport errors are retried, honouring Retry-After up to 60 s; anything else is fatal."""
    last = None
    for k in range(tries):
        req = urllib.request.Request(url, headers=HEADERS, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
                assert r.status == 200, "HTTP %d %s" % (r.status, url)
                return body, json.loads(body, parse_float=D)
        except urllib.error.HTTPError as e:
            last = "HTTP %d" % e.code
            if e.code not in (429, 500, 502, 503, 504):
                raise AssertionError("%s on %s: %r" % (last, url, e.read()[:200]))
            wait = e.headers.get("Retry-After")
            time.sleep(min(60.0, float(wait)) if wait else min(60.0, 2.0 ** k))
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
            last = "%s %s" % (type(e).__name__, e)
            time.sleep(min(60.0, 2.0 ** k))
    raise AssertionError("BLOCKED: %d attempts failed on %s, the last %s" % (tries, url, last))


def by_slug(docs, slugs):
    assert isinstance(docs, list), "gamma: not a list"
    by = {}
    for d in docs:
        s = d.get("slug")
        assert s in slugs, "gamma: %r was not requested" % s
        assert s not in by, "gamma: %s twice" % s
        by[s] = d
    return by


def gamma_cached(docs_dir, slugs):
    """The settled documents of up to CHUNK slugs, one request, its body stored once, gzip, verbatim."""
    assert 1 <= len(slugs) <= CHUNK and len(set(slugs)) == len(slugs)
    path = os.path.join(docs_dir, "%s.json.gz" % slugs[0])
    if os.path.exists(path):
        with gzip.open(path, "rb") as fh:
            docs = json.loads(fh.read(), parse_float=D)
    else:
        q = [("slug", s) for s in slugs] + [("closed", "true"), ("limit", str(len(slugs) + 5))]
        body, docs = http_json(GAMMA + "?" + urllib.parse.urlencode(q))
        write_atomic(path, gz_bytes(body))
    return by_slug(docs, slugs)

# ---- the rules: the chain book's window, the settled documents, the identities ----------------


def window_problem(w, t):
    """The first condition a window.json fails, or None, with the chain book's token map."""
    if not isinstance(w, dict) or w.get("T") != t:
        return "window T", None
    if w.get("documents_ok") is not True:
        return "documents", None
    if w.get("checkpoints_complete") != len(OFFSETS) or w.get("missed") != 0:
        return "incomplete", None
    mk = w.get("markets")
    if not (isinstance(mk, dict) and set(mk) == {"m15", "m5"}
            and all(isinstance(v, dict) for v in mk.values())):
        return "markets", None
    if mk["m15"].get("slug") != slug15(t) or mk["m5"].get("slug") != slug5(t + 600):
        return "slugs", None
    mapping = {}
    for m in ("m15", "m5"):
        outs = loads_maybe(mk[m].get("outcomes"))
        toks = loads_maybe(mk[m].get("clobTokenIds"))
        cond = mk[m].get("conditionId")
        if outs != ["Up", "Down"] or not two_tokens(toks) or not CONDITION.fullmatch(cond or ""):
            return "tokens", None
        mapping[m] = {"Up": toks[0], "Down": toks[1], "condition": cond}
    return None, mapping


def two_tokens(toks):
    return (isinstance(toks, list) and len(toks) == 2 and toks[0] != toks[1]
            and all(isinstance(x, str) and x.isdigit() for x in toks))


def chainbook_window(root, t):
    """A considered window as the chain book stored it: the reason it is not a member, or its token map.
    window.json carries counts, times and token ids (map section 2.5's exception); nothing else is opened."""
    d = os.path.join(root, str(t))
    if not os.path.isdir(d):
        return "no directory", None
    if not os.path.isfile(os.path.join(d, "window.json")):
        return "no window.json", None
    if not os.path.isfile(os.path.join(d, "books.jsonl.gz")):
        return "no books", None
    with open(os.path.join(d, "window.json"), "rb") as fh:
        raw = fh.read()
    try:
        w = json.loads(raw)
    except ValueError:
        return "window.json", None
    return window_problem(w, t)


def readings_of(doc):
    """priceToBeat and finalPrice from events[0].eventMetadata, as the venue printed them, or None, None."""
    ev = doc.get("events")
    if not (isinstance(ev, list) and ev and isinstance(ev[0], dict)):
        return None, None
    em = ev[0].get("eventMetadata")
    if not isinstance(em, dict):
        return None, None
    vals = []
    for k in ("priceToBeat", "finalPrice"):
        v = em.get(k)
        if isinstance(v, bool) or not isinstance(v, (D, int)) or not v > 0:
            return None, None
        vals.append(D(v) if isinstance(v, int) else v)
    return vals[0], vals[1]


def outcome_of(doc):
    return {("1", "0"): "Up", ("0", "1"): "Down"}[tuple(loads_maybe(doc["outcomePrices"]))]


def doc_problem(doc, start, cb):
    """The first condition a settled document fails, or None. `cb` is the chain book's map for that market,
    or None in the rehearsal, which has no chain book."""
    if doc is None:
        return "absent"
    if doc.get("closed") is not True:
        return "open"
    if loads_maybe(doc.get("outcomes")) != ["Up", "Down"]:
        return "outcomes"
    if loads_maybe(doc.get("outcomePrices")) not in (["1", "0"], ["0", "1"]):
        return "unresolved"
    if doc.get("feeType") != FEE_TYPE or doc.get("feeSchedule") != FEE_SCHEDULE:
        return "fee"
    if doc.get("eventStartTime") != iso(start):
        return "start"
    if not CONDITION.fullmatch(doc.get("conditionId") or ""):
        return "condition"
    toks = loads_maybe(doc.get("clobTokenIds"))
    if not two_tokens(toks):
        return "tokens"
    if cb is not None and (toks != [cb["Up"], cb["Down"]] or doc["conditionId"] != cb["condition"]):
        return "not the chain book's tokens"
    ptb, fin = readings_of(doc)
    if ptb is None:
        return "readings"
    return None


def identities(d15, d5):
    """E1: one reading settles both, the same literal. E2 and E3: each outcome is Up iff its finalPrice is
    at or above its priceToBeat."""
    p15, f15 = readings_of(d15)
    p5, f5 = readings_of(d5)
    return (lit(f15) == lit(f5), (outcome_of(d15) == "Up") == (f15 >= p15),
            (outcome_of(d5) == "Up") == (f5 >= p5))


def pairs_of(dv):
    """The dominated pairs of a window: A where the 5m strike is above the 15m's, B below, both at equal."""
    return ["A"] if dv > 0 else (["B"] if dv < 0 else ["A", "B"])


def payoff(pair, r0, r600, r900):
    """What the pair pays at settlement, per share of each leg: the containment, by its own outcomes."""
    up15, up5 = 1 if r900 >= r0 else 0, 1 if r900 >= r600 else 0
    return (up15 + 1 - up5) if pair == "A" else (up5 + 1 - up15)

# ---- the costs -----------------------------------------------------------------------------------


def costs(a):
    """One share bought at a, its fee tz14.fee_pp(a), two ways the venue could collect it: on top of the
    price, a + fee; or in shares, a / (1 - fee / a), the cost of one share net of the fee."""
    f = tz14().fee_pp(a)
    return a + f, a / (1 - f / a)


def classify(ax, ay, skew_ns, dt_ms):
    """The pair's cost a share of each leg after both taker fees, and its class. firm: below 1 with the fee
    collected either way, the two replies received at most SKEW_BOUND_NS apart and the two books' own
    timestamps at most TS_BOUND_MS apart. loose: below 1 with the fee on top, but not firm. none: at or above
    1 with the fee on top. unquoted: a leg has no ask at the venue's minimum size."""
    r = {"k_top": None, "k_shares": None, "cls": "unquoted", "sub": ""}
    if ax is None or ay is None:
        return r
    tx, sx = costs(ax)
    ty, sy = costs(ay)
    r["k_top"], r["k_shares"] = tx + ty, sx + sy
    timed = skew_ns is not None and dt_ms is not None
    together = timed and skew_ns <= SKEW_BOUND_NS and dt_ms <= TS_BOUND_MS
    if r["k_shares"] < 1 and together:
        r["cls"] = "firm"
    elif r["k_top"] < 1:
        r["cls"] = "loose"
        r["sub"] = "convention" if r["k_shares"] >= 1 else ("no time" if not timed else "apart")
    else:
        r["cls"] = "none"
    return r


def reading_of(n_clean, v_firm, v_any):
    """Section 4.3: VIOLATION on one firm window; NONE on no window firm or loose among at least N_MIN
    members whose every unit read valid; UNDECIDABLE otherwise."""
    if v_firm >= 1:
        return "VIOLATION"
    if v_any == 0 and n_clean >= N_MIN:
        return "NONE"
    return "UNDECIDABLE"


def theta1(n):
    """NONE's alternative: the per-window violation probability at which no violation in n windows has
    probability exactly ALPHA."""
    return 1 - (ALPHA.ln() / n).exp()


def power(n, theta):
    return 1 - (1 - theta) ** n

# ---- the set -------------------------------------------------------------------------------------


def form_set(base, root, ts, docs_fn, chainbook=True, budget_s=None):
    """Every considered window, in order, with its status; and the members with what the score needs."""
    os.makedirs(base, exist_ok=True)
    setp = os.path.join(base, "set.json")
    if os.path.exists(setp):
        with open(setp, encoding="utf-8") as fh:
            s = json.load(fh)
        out("the set from %s sha256 %s: %d considered, %d members" % (
            setp, sha256_file(setp), len(s["considered"]), len(s["members"])))
        return s
    t0 = time.time()
    status, pending = {}, []
    for t in ts:
        why, mapping = chainbook_window(root, t) if chainbook else (None, None)
        status[t] = why
        if why is None:
            pending.append((t, mapping))
    docs_dir = os.path.join(base, "docs")
    os.makedirs(docs_dir, exist_ok=True)
    members, requests = [], 0
    total = -(-len(pending) // (CHUNK // 2))
    t_req = time.time()
    for i in range(0, len(pending), CHUNK // 2):
        grp = pending[i:i + CHUNK // 2]
        slugs = [s for t, _m in grp for s in (slug15(t), slug5(t + 600))]
        by = docs_fn(docs_dir, slugs)
        requests += 1
        if budget_s is not None and requests == 20:
            proj = (time.time() - t_req) / 20 * total
            out("projected %.0f s for %d document requests after 20" % (proj, total))
            assert proj <= budget_s, "BLOCKED: the fetch projected at %.0f s, above %d" % (proj, budget_s)
        for t, mapping in grp:
            d15, d5 = by.get(slug15(t)), by.get(slug5(t + 600))
            why = doc_problem(d15, t, mapping and mapping["m15"])
            if why:
                status[t] = "15m document: " + why
                continue
            why = doc_problem(d5, t + 600, mapping and mapping["m5"])
            if why:
                status[t] = "5m document: " + why
                continue
            e1, e2, e3 = identities(d15, d5)
            if not (e1 and e2 and e3):
                status[t] = "E1" if not e1 else ("E2" if not e2 else "E3")
                continue
            p15, f15 = readings_of(d15)
            p5, _f5 = readings_of(d5)
            dv = p5 - p15
            t15, t5 = loads_maybe(d15["clobTokenIds"]), loads_maybe(d5["clobTokenIds"])
            members.append({
                "T": t, "R0": lit(p15), "R600": lit(p5), "R900": lit(f15), "D": fx(dv),
                "O15": outcome_of(d15), "O5": outcome_of(d5), "pairs": pairs_of(dv),
                "map": {"m15": {"Up": t15[0], "Down": t15[1], "condition": d15["conditionId"]},
                        "m5": {"Up": t5[0], "Down": t5[1], "condition": d5["conditionId"]}}})
            status[t] = "member"
    s = {"first": ts[0], "last": ts[-1], "considered": [[t, status[t]] for t in ts],
         "members": members, "requests": requests}
    write_atomic(setp, dumps(s).encode("utf-8"))
    out("the set formed in %.1f s: %d considered, %d members, %d document requests, %s sha256 %s" % (
        time.time() - t0, len(ts), len(members), requests, setp, sha256_file(setp)))
    with open(setp, encoding="utf-8") as fh:
        return json.load(fh)


def weekend(t):
    return 1 if datetime.datetime.fromtimestamp(t, datetime.timezone.utc).weekday() >= 5 else 0


def build_constants(base, s, label):
    """Book-free: the members, N, NONE's alternative and VIOLATION's power. A second run must write the
    same bytes."""
    ms = s["members"]
    n = len(ms)
    ts = [m["T"] for m in ms]
    th = theta1(n) if n else None
    c = {"label": label, "considered": len(s["considered"]), "members": n,
         "first": ts[0] if ts else None, "last": ts[-1] if ts else None,
         "member_list_sha": sha256_bytes(("\n".join(map(str, ts)) + "\n").encode()),
         "set_sha": sha256_file(os.path.join(base, "set.json")),
         "non_members": [[t, st] for t, st in s["considered"] if st != "member"],
         "pairs": {k: sum(1 for m in ms if m["pairs"] == v) for k, v in
                   (("A", ["A"]), ("B", ["B"]), ("AB", ["A", "B"]))},
         "weekend": sum(weekend(t) for t in ts),
         "spans": {"1": sum(1 for t in ts if t < SECOND_SPAN), "2": sum(1 for t in ts if t >= SECOND_SPAN)},
         "alpha": ALPHA, "n_min": N_MIN, "none_possible": n >= N_MIN, "theta1": th,
         "powers": {fx(th_): power(n, th_) for th_ in THETAS},
         "skew_bound_ns": SKEW_BOUND_NS, "ts_bound_ms": TS_BOUND_MS, "taus": list(TAUS)}
    path = os.path.join(base, "%s-constants.json" % label)
    return c, path, write_once(path, dumps(c).encode("utf-8"))


def show_constants(c, path, sha):
    out("considered %d, members %d, first %s %s, last %s %s, weekend members %d, by span %s" % (
        c["considered"], c["members"], c["first"], utc(c["first"]) if c["first"] else "-", c["last"],
        utc(c["last"]) if c["last"] else "-", c["weekend"], c["spans"]))
    out("member list sha %s; set sha %s" % (c["member_list_sha"], c["set_sha"]))
    out("members by pair: %s" % c["pairs"])
    for t, st in c["non_members"]:
        out("non-member %d %s: %s" % (t, utc(t), st))
    out("NONE possible: %s (N %d, N_MIN %d); its alternative theta1 = %s a window" % (
        c["none_possible"], c["members"], N_MIN, fx(c["theta1"]) if c["theta1"] is not None else "-"))
    for k, v in sorted(c["powers"].items()):
        out("power of VIOLATION against a firm-violation probability of %s a window: %s" % (k, fx(v)))
    out("wrote %s sha256 %s" % (path, sha))

# ---- the books -----------------------------------------------------------------------------------


def read_books(root, t):
    """A member's stored lines, parsed, or the reason they cannot be. Total: data never raises here."""
    path = os.path.join(root, str(t), "books.jsonl.gz")
    try:
        with gzip.open(path, "rb") as fh:
            text = fh.read().decode("utf-8")
        return [json.loads(ln) for ln in text.split("\n") if ln], None
    except (OSError, EOFError, ValueError, zlib.error) as e:
        return None, "books unreadable: %s" % type(e).__name__


def venue_ms(book):
    """The reply's own timestamp in milliseconds, or None where it is not a run of ASCII digits."""
    v = book.get("timestamp")
    s = str(v) if v is not None else ""
    return int(s) if s.isascii() and s.isdigit() else None


def line_check(ln, t, member):
    """One stored reply: its problem, or None with what the pair needs from it."""
    if not isinstance(ln, dict) or frozenset(ln) != BOOK_KEYS:
        return "keys", None
    m = ln["market"]
    if ln["T"] != t or m not in ("m15", "m5") or ln["tau_prime"] not in TAUS:
        return "place", None
    if ln["slug"] != (slug15(t) if m == "m15" else slug5(t + 600)):
        return "slug", None
    if ln["status"] != 200:
        return "status", None
    raw = ln["raw"]
    if not isinstance(raw, str):
        return "raw", None
    try:
        b = raw.encode("utf-8")
    except UnicodeEncodeError:
        return "raw", None
    if ln["bytes"] != len(b) or ln["sha256"] != sha256_bytes(b):
        return "hash", None
    mp = member["map"][m]
    outcome = {mp["Up"]: "Up", mp["Down"]: "Down"}.get(ln["token_id"]) if isinstance(
        ln["token_id"], str) else None
    if outcome is None or ln["outcome_label"] != outcome:
        return "token", None
    try:
        book = tz14().book_of(raw)
    except Exception:            # the reply is data: a body that cannot be parsed is a finding, never a stop
        return "body", None
    if not book["ok"] or book["bad_levels"]:
        return "body", None
    if not (book["min_order_size_present"] and book["tick_size_present"]):
        return "size or tick", None
    try:
        size, tick = D(str(book["min_order_size"])), D(str(book["tick_size"]))
        if not (size > 0 and tick > 0):
            return "size or tick", None
    except ArithmeticError:
        return "size or tick", None
    if str(book["asset_id"]) != ln["token_id"]:
        return "asset", None
    return None, {"outcome": outcome, "book": book, "size": size, "tick": tick, "ts": venue_ms(book),
                  "recv": ln["recv_mono_ns"] if type(ln["recv_mono_ns"]) is int else None,
                  "wall": ln["recv_wall_ns"] if type(ln["recv_wall_ns"]) is int else None}


def units_of(member, lines):
    """Per tau': (tau, problem, legs) - legs maps (market, outcome) to what line_check returned."""
    t = member["T"]
    by_tau = {tau: [] for tau in TAUS}
    for ln in lines:
        k = ln.get("tau_prime") if isinstance(ln, dict) else None
        if type(k) is int and k in by_tau:
            by_tau[k].append(ln)
    res = []
    for tau in TAUS:
        lns, legs, why = by_tau[tau], {}, None
        if len(lns) != 4:
            why = "lines %d" % len(lns)
        for ln in lns if why is None else ():
            why, info = line_check(ln, t, member)
            if why:
                break
            key = (ln["market"], info["outcome"])
            if key in legs:
                why = "duplicate"
                break
            legs[key] = info
        res.append((tau, why, legs if why is None else None))
    return res


COLS = ["T", "tau", "pair", "valid", "why", "ask_x", "ask_y", "k_top", "k_shares", "cls", "sub", "skew_ns",
        "ts_x", "ts_y", "dt_ms", "lag_x_ms", "lag_y_ms", "q_x", "q_y"]


def lag_ms(leg):
    """Milliseconds from the reply's own timestamp to its receipt, on the host's wall clock."""
    return None if leg["ts"] is None or leg["wall"] is None else leg["wall"] // 1000000 - leg["ts"]


def rows_of(member, units):
    """One row a unit and pair; an invalid unit is one row with its problem."""
    rows = []
    for tau, why, legs in units:
        if why is not None:
            rows.append({"T": member["T"], "tau": tau, "pair": "-", "valid": 0, "why": why})
            continue
        for pair in member["pairs"]:
            x, y = (legs[k] for k in LEGS[pair])
            skew = None if x["recv"] is None or y["recv"] is None else abs(x["recv"] - y["recv"])
            try:
                tx = tz14().touch_of(x["book"], x["size"], x["tick"])
                ty = tz14().touch_of(y["book"], y["size"], y["tick"])
                if any(a is not None and a <= 0 for a in (tx["ask5"], ty["ask5"])):
                    rows.append({"T": member["T"], "tau": tau, "pair": pair, "valid": 0, "why": "price"})
                    continue
                dt = None if x["ts"] is None or y["ts"] is None else abs(x["ts"] - y["ts"])
                r = classify(tx["ask5"], ty["ask5"], skew, dt)
            except ArithmeticError:
                rows.append({"T": member["T"], "tau": tau, "pair": pair, "valid": 0, "why": "levels"})
                continue
            r.update({"T": member["T"], "tau": tau, "pair": pair, "valid": 1, "why": "",
                      "ask_x": tx["ask5"], "ask_y": ty["ask5"], "skew_ns": skew,
                      "ts_x": x["ts"], "ts_y": y["ts"], "dt_ms": dt,
                      "lag_x_ms": lag_ms(x), "lag_y_ms": lag_ms(y),
                      "q_x": tx["cum"]["ask"][0], "q_y": ty["cum"]["ask"][0]})
            rows.append(r)
    return rows


def cell(v):
    if v is None:
        return ""
    return fx(v) if isinstance(v, D) else str(v)


def band_of(dv):
    a = abs(dv)
    return "<1" if a < 1 else ("1-10" if a < 10 else ("10-100" if a < 100 else ">=100"))


def score(base, root, s, c, label):
    """The members' books, read once, and the reading. Everything after the first book is total."""
    ms = s["members"]
    n = len(ms)
    assert c["members"] == n and c["member_list_sha"] == sha256_bytes(
        ("\n".join(str(m["T"]) for m in ms) + "\n").encode()), "score: the constants are not this set's"
    lines_csv = [",".join(COLS)]
    allrows, flags = [], []
    invalid, clean = {}, 0
    for m in ms:
        lines, why = read_books(root, m["T"])
        units = ([(tau, why, None) for tau in TAUS] if lines is None else units_of(m, lines))
        rows = rows_of(m, units)
        for r in rows:
            if not r["valid"]:
                invalid[r["why"]] = invalid.get(r["why"], 0) + 1
            lines_csv.append(",".join(cell(r.get(k)) for k in COLS))
        allrows += [(m, r) for r in rows]
        flags.append((m, any(r.get("cls") == "firm" for r in rows),
                      any(r.get("cls") in ("firm", "loose") for r in rows)))
        clean += 1 if all(r["valid"] for r in rows) else 0
    v_firm = sum(1 for _m, f, _a in flags if f)
    v_any = sum(1 for _m, _f, a in flags if a)
    word = reading_of(clean, v_firm, v_any)
    valid = [(m, r) for m, r in allrows if r["valid"]]
    cls_n = {k: sum(1 for _m, r in valid if r["cls"] == k) for k in ("firm", "loose", "none", "unquoted")}
    sub_n = {k: sum(1 for _m, r in valid if r["cls"] == "loose" and r["sub"] == k)
             for k in ("convention", "apart", "no time")}
    by_tau = {str(tau): {k: sum(1 for _m, r in valid if r["tau"] == tau and r["cls"] == k)
                         for k in ("firm", "loose", "none", "unquoted")} for tau in TAUS}
    by_pair = {p: {k: sum(1 for _m, r in valid if r["pair"] == p and r["cls"] == k)
                   for k in ("firm", "loose", "none", "unquoted")} for p in ("A", "B")}
    closest = {}
    for tau in TAUS:
        for p in ("A", "B"):
            q = [(r["k_top"], m["T"], r) for m, r in valid if r["tau"] == tau and r["pair"] == p and
                 r["k_top"] is not None]
            if q:
                k, t, r = min(q, key=lambda z: (z[0], z[1]))
                closest["%d %s" % (tau, p)] = {"T": t, "ask_x": r["ask_x"], "ask_y": r["ask_y"],
                                               "k_top": k, "k_shares": r["k_shares"],
                                               "skew_ns": r["skew_ns"]}
    firm = [(m, r) for m, r in valid if r["cls"] == "firm"]
    loose = [(m, r) for m, r in valid if r["cls"] == "loose"]
    best = {}
    for m, r in firm:
        p = (1 - r["k_shares"]) * min(r["q_x"], r["q_y"])
        best[m["T"]] = max(best.get(m["T"], D(0)), p)
    profit = sum(best.values(), D(0))
    bands = {}
    for m, f, a in flags:
        b = bands.setdefault(band_of(D(m["D"])), {"members": 0, "firm": 0, "any": 0})
        b["members"] += 1
        b["firm"] += f
        b["any"] += a
    res = {
        "label": label, "members": n, "units": n * len(TAUS), "rows": len(allrows),
        "invalid": invalid, "classes": cls_n, "loose_by": sub_n, "by_tau": by_tau, "by_pair": by_pair,
        "v_firm": v_firm, "v_any": v_any, "reading": word, "n_clean": clean,
        "none_possible": clean >= N_MIN, "theta1_clean": theta1(clean) if clean else None,
        "pre_fee_inversions": sum(1 for _m, r in valid if r["ask_x"] is not None and
                                  r["ask_y"] is not None and r["ask_x"] + r["ask_y"] < 1),
        "closest": closest,
        "firm_margin_shares": quantiles([1 - r["k_shares"] for _m, r in firm]),
        "firm_skew_ns": quantiles([r["skew_ns"] for _m, r in firm]),
        "firm_dt_ms": quantiles([r["dt_ms"] for _m, r in firm if r["dt_ms"] is not None]),
        "firm_lag_ms": quantiles([v for _m, r in firm for v in (r["lag_x_ms"], r["lag_y_ms"])
                                  if v is not None]),
        "firm_q": quantiles([min(r["q_x"], r["q_y"]) for _m, r in firm]),
        "firm_profit_at_touch": profit,
        "firm_profit_per_day": (profit * 96 / n) if n else None,
        "loose_margin_top": quantiles([1 - r["k_top"] for _m, r in loose]),
        "d_bands": bands,
    }
    units_csv = ("\n".join(lines_csv) + "\n").encode("utf-8")
    body = dumps(res).encode("utf-8")
    hu = write_once(os.path.join(base, "%s-units.csv" % label), units_csv)
    hr = write_once(os.path.join(base, "%s-reading.json" % label), body)
    out("books: %d members, %d units, %d rows, invalid %s" % (n, n * len(TAUS), len(allrows), invalid))
    out("rows by class: %s; loose by reason: %s" % (cls_n, sub_n))
    for tau in TAUS:
        out("tau' %3d: %s" % (tau, by_tau[str(tau)]))
    out("by pair: %s" % by_pair)
    out("windows with a firm violation V_firm %d of %d; with any V_any %d of %d; clean members %d" % (
        v_firm, n, v_any, n, clean))
    out("NONE possible: %s; its alternative at the clean members, theta1 = %s a window" % (
        res["none_possible"], cell(res["theta1_clean"])))
    out("ROW columns: class,reason,T,tau',pair,ask_x,ask_y,k_top,k_shares,skew_ns,ts_x,ts_y,dt_ms,q_x,q_y,"
        "R0,R600")
    for name, group in (("firm", firm), ("loose", loose)):
        for m, r in group[:ROWS_SHOWN]:
            out("ROW %s,%s,%d,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (
                r["cls"], r["sub"], r["T"], r["tau"], r["pair"], cell(r["ask_x"]), cell(r["ask_y"]),
                cell(r["k_top"]), cell(r["k_shares"]), cell(r["skew_ns"]), cell(r["ts_x"]),
                cell(r["ts_y"]), cell(r["dt_ms"]), cell(r["q_x"]), cell(r["q_y"]), m["R0"], m["R600"]))
        if len(group) > ROWS_SHOWN:
            out("%d more %s rows, in %s-units.csv" % (len(group) - ROWS_SHOWN, name, label))
    for k, v in sorted(closest.items(), key=lambda kv: (-int(kv[0].split()[0]), kv[0])):
        out("closest tau' %s: T %d ask_x %s ask_y %s k_top %s k_shares %s skew_ns %s - barred" % (
            k, v["T"], cell(v["ask_x"]), cell(v["ask_y"]), cell(v["k_top"]), cell(v["k_shares"]),
            cell(v["skew_ns"])))
    out("pre-fee inversions, ask_x + ask_y < 1: %d rows - barred" % res["pre_fee_inversions"])
    for k in ("firm_margin_shares", "firm_skew_ns", "firm_dt_ms", "firm_lag_ms", "firm_q",
              "loose_margin_top"):
        q = res[k]
        out("%s: %s - barred" % (k, "none" if q is None else
                                 ", ".join("%s %s" % (kk, cell(vv)) for kk, vv in q.items())))
    out("firm profit at the touch, the best unit a window: %s USDC, %s a day of members - barred" % (
        fx(profit), cell(res["firm_profit_per_day"])))
    out("members by |D| in USD: %s - barred" % bands)
    out("wrote %s-units.csv sha256 %s and %s-reading.json sha256 %s" % (label, hu, label, hr))
    return res

# ---- modes ---------------------------------------------------------------------------------------


def git(*args):
    cp = subprocess.run(["git", "-C", WT] + list(args), capture_output=True, text=True)
    assert cp.returncode == 0, "git %s: %s" % (" ".join(args), cp.stderr.strip())
    return cp.stdout.strip()


ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"`?([0-9a-f]{64}|self-reference[^|]*?)`? \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)


def mode_fingerprint():
    """Contract section 1 steps 3 and 4, asserted: map section 0 against the primary checkout."""
    with open(os.path.join(PRIMARY, "SYSTEM-MAP.md"), "rb") as fh:
        raw = fh.read()
    txt = raw.decode("utf-8")
    rev = re.findall(r"^\*\*Revision string:\*\* `([^`]+)`$", txt, re.M)
    assert rev == [MAP_REVISION], "map revision %r, required %s" % (rev, MAP_REVISION)
    found = dict(ANCHOR_ROW.findall(txt))
    assert found == ANCHORS, "anchors %r" % found
    for k, rel in sorted(ANCHOR_FILES.items()):
        h = sha256_file(os.path.join(PRIMARY, rel))[:12]
        assert h == ANCHORS[k], "re-derived %s %s, the map %s" % (k, h, ANCHORS[k])
        out("re-derived %s %s sha256[:12] %s equal" % (k, rel, h))
    rows = ROW.findall(txt)
    states = {k: sum(1 for r in rows if r[3] == k) for k in MAP_ROWS}
    assert states == MAP_ROWS and len(rows) == sum(MAP_ROWS.values()), "rows %r" % states
    for path, lines, nbytes, state, sha in rows:
        with open(os.path.join(PRIMARY, path), "rb") as fh:
            blob = fh.read()
        got = (blob.count(b"\n"), len(blob), sha256_bytes(blob))
        if state == "frozen":
            want = (int(lines.replace(",", "")), int(nbytes.replace(",", "")), sha)
            assert got == want, "frozen row %s: %r, the map %r" % (path, got, want)
        tail = " equal" if state == "frozen" else ""
        out("%-44s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state, tail))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, "
        "tracked %d, reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"],
                                     states["tracked"], states["reported"]))


def mode_rehearse():
    floor_check()
    base = os.path.join(WORK, "rehearsal")
    ts = [REHEARSAL[0] + WINDOW * k for k in range(REHEARSAL[1])]
    s = form_set(base, None, ts, gamma_cached, chainbook=False)
    ms = s["members"]
    dvs = [D(m["D"]) for m in ms]
    lines = ["%d,%s,%s,%s,%s,%s" % (m["T"], m["R0"], m["R600"], m["R900"], m["O15"], m["O5"]) for m in ms]
    got = {"windows": len(s["considered"]), "members": len(ms),
           "d_pos": sum(1 for d in dvs if d > 0), "d_neg": sum(1 for d in dvs if d < 0),
           "d_zero": sum(1 for d in dvs if d == 0),
           "up15": sum(1 for m in ms if m["O15"] == "Up"), "up5": sum(1 for m in ms if m["O5"] == "Up"),
           "sum_d": sum(dvs, D(0)), "sum_abs_d": sum((abs(d) for d in dvs), D(0)),
           "digest": sha256_bytes(("\n".join(lines) + "\n").encode())}
    for t, st in s["considered"]:
        if st != "member":
            out("rehearsal non-member %d: %s" % (t, st))
    bad = [k for k in REF if got[k] != REF[k]]
    for k in REF:
        out("G-REHEARSAL %-9s instrument %s, the Architect's %s, %s" % (
            k, cell(got[k]), cell(REF[k]), "equal" if got[k] == REF[k] else "DIFFERENT"))
    assert not bad, "G-REHEARSAL FAIL: %s" % bad
    out("G-REHEARSAL PASS: %d of %d figures equal; %d document requests" % (
        len(REF), len(REF), s["requests"]))


def considered_windows():
    return [FIRST_T + WINDOW * k for k in range(CONSIDERED)]


def mode_fetch():
    floor_check()
    os.makedirs(WORK, exist_ok=True)
    base = os.path.join(WORK, "set")
    s = form_set(base, CHAINBOOK, considered_windows(), gamma_cached, budget_s=FETCH_BUDGET_S)
    assert [t for t, _st in s["considered"]] == considered_windows(), "G-SET: the considered windows"
    assert all(st for _t, st in s["considered"]), "G-SET: a window without a status"
    assert [m["T"] for m in s["members"]] == [t for t, st in s["considered"] if st == "member"]
    st = load_state()
    st["set_sha"] = sha256_file(os.path.join(base, "set.json"))
    save_state(st)
    reasons = {}
    for _t, w in s["considered"]:
        reasons[w] = reasons.get(w, 0) + 1
    out("G-SET PASS: %d considered, %d members; statuses %s; set.json sha256 %s" % (
        len(s["considered"]), len(s["members"]), dict(sorted(reasons.items())), st["set_sha"]))


def the_set():
    base = os.path.join(WORK, "set")
    with open(os.path.join(base, "set.json"), encoding="utf-8") as fh:
        return base, json.load(fh)


def mode_constants():
    floor_check()
    base, s = the_set()
    st = load_state()
    assert sha256_file(os.path.join(base, "set.json")) == st.get("set_sha"), "constants: not G-SET's set"
    c, path, sha = build_constants(base, s, "tz24")
    show_constants(c, path, sha)
    st["constants_sha"] = sha
    st["constants_at"] = utc(time.time())
    save_state(st)


def mode_score():
    floor_check()
    base, s = the_set()
    st = load_state()
    cpath = os.path.join(base, "tz24-constants.json")
    assert sha256_file(cpath) == st.get("constants_sha"), "score: not the constants recorded"
    with open(cpath, encoding="utf-8") as fh:
        c = json.load(fh, parse_float=D)
    assert c["set_sha"] == sha256_file(os.path.join(base, "set.json")), "score: not the constants' set"
    head = git("rev-parse", "HEAD")
    branches = git("branch", "-r", "--contains", head).split()
    assert "origin/" + BRANCH in branches, "score: HEAD %s is not on origin" % head
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(dumps({"at": utc(time.time()), "head": head, "members": c["members"],
                        "member_list_sha": c["member_list_sha"], "constants_sha": st["constants_sha"]}))
    BOOKS_OPEN[0] = True
    res = score(base, CHAINBOOK, s, c, "tz24")
    out("B2 READING: %s" % res["reading"])


def mode_still():
    st = load_state()
    now = {}
    for key, unit in UNITS.items():
        cp = subprocess.run(["systemctl", "show", unit, "-p", "MainPID", "-p", "NRestarts",
                             "-p", "ActiveState", "-p", "MemoryCurrent", "-p", "MemoryPeak"],
                            capture_output=True, text=True)
        assert cp.returncode == 0, cp.stderr
        kv = dict(line.split("=", 1) for line in cp.stdout.split("\n") if "=" in line)
        now[key] = {k: kv[k] for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, MemoryCurrent %s, MemoryPeak %s" % (unit, now[key], kv.get("MemoryCurrent"),
                                                        kv.get("MemoryPeak")))
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "units": now}
        save_state(st)
        out("still: recorded")
        return
    same = now == st["still"]["units"]
    out("G-STILL %s: %s since %s" % ("PASS" if same else "FAIL", "unchanged" if same else
                                     "changed", st["still"]["at"]))


def proc_start_times():
    """The start instant of every running process whose argv[0] is `claude` or ends in `/claude.exe`."""
    with open("/proc/stat", encoding="utf-8") as fh:
        btime = int([ln for ln in fh.read().split("\n") if ln.startswith("btime ")][0].split()[1])
    hz = os.sysconf("SC_CLK_TCK")
    found = []
    for pid in sorted((p for p in os.listdir("/proc") if p.isdigit()), key=int):
        try:
            with open("/proc/%s/cmdline" % pid, "rb") as fh:
                argv = fh.read().split(b"\0")
            with open("/proc/%s/stat" % pid, encoding="utf-8") as fh:
                fields = fh.read().rsplit(")", 1)[1].split()
        except OSError:
            continue
        a0 = argv[0].decode("utf-8", "replace") if argv else ""
        if a0 == "claude" or a0.endswith("/claude.exe"):
            found.append((int(pid), btime + int(fields[19]) / hz, a0))
    return found


def birth(path):
    cp = subprocess.run(["stat", "-c", "%W", path], capture_output=True, text=True)
    assert cp.returncode == 0, cp.stderr
    return int(cp.stdout.strip())


def mode_scratch(own):
    """Lists the UUID directories beside `own`, this session's, and names each live or earlier."""
    parent = os.path.dirname(own)
    procs = proc_start_times()
    for pid, t, a0 in procs:
        out("running %d started %s %s" % (pid, utc(t), a0))
    for name in sorted(os.listdir(parent)):
        path = os.path.join(parent, name)
        if path == own or not UUID.fullmatch(name) or not os.path.isdir(path):
            continue
        b = birth(path)
        owner = [pid for pid, t, _a in procs if t - 1 <= b <= t + LIVE_S]
        out("%s born %s: %s" % (name, utc(b), ("live, process %s" % owner) if owner else "earlier"))


def report_tokens():
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8", errors="replace") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    """Kept whatever a report prints: the state, the ledger, the logs, and the venue's documents as served."""
    return tree == WORK and (rel == "state.json" or rel == "book-ledger.jsonl" or rel.startswith("logs/")
                             or rel.startswith("set/docs/") or rel.startswith("rehearsal/docs/"))


def pristine(tree):
    cp = subprocess.run(["git", "-C", tree, "status", "--porcelain", "--ignored"],
                        capture_output=True, text=True)
    assert cp.returncode == 0 and cp.stdout == "", "reclaim: %s holds %r" % (tree, cp.stdout[:400])
    head = subprocess.run(["git", "-C", tree, "rev-parse", "HEAD"], capture_output=True,
                          text=True).stdout.strip()
    up = subprocess.run(["git", "-C", tree, "rev-parse", "@{u}"], capture_output=True, text=True)
    assert up.returncode == 0 and up.stdout.strip() == head, \
        "reclaim: %s is at %s, its upstream at %r" % (tree, head, up.stdout.strip())
    out("reclaim: %s skipped: no file but its HEAD's, and HEAD %s is its upstream's" % (tree, head))


def reclaimable(tree):
    if tree == WORK:
        return True
    return (tree.startswith("/tmp/") and os.path.isdir(tree) and not os.path.islink(tree)
            and UUID.fullmatch(os.path.basename(tree)) is not None
            and "btc-5m-twap" in os.path.basename(os.path.dirname(tree)))


def mode_reclaim(trees):
    assert trees and all(reclaimable(t) for t in trees), "reclaim: %r" % (trees,)
    procs = proc_start_times()
    for t in trees:
        if t != WORK:
            b = birth(t)
            assert not [p for p, s, _a in procs if s - 1 <= b <= s + LIVE_S], \
                "reclaim: %s belongs to a running process" % t
    tokens = report_tokens()
    lengths = sorted({len(t) for t in tokens})
    before = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    out("reclaim: %d report tokens; forensic store holds %d files" % (len(tokens), before))
    considered = named = kept = copied = held = 0
    for tree in trees:
        if tree == WORK and os.path.isdir(WT):
            pristine(WT)
        for dirpath, dirnames, filenames in os.walk(tree):
            dirnames[:] = sorted(d for d in dirnames if os.path.join(dirpath, d) != WT)
            for name in sorted(filenames):
                path = os.path.join(dirpath, name)
                if os.path.islink(path) or not os.path.isfile(path):
                    continue
                considered += 1
                rel = os.path.relpath(path, tree)
                h = sha256_file(path)
                is_named = any(h[:k] in tokens for k in lengths)
                is_kept = by_name(tree, rel)
                if not (is_named or is_kept):
                    continue
                named += 1 if is_named else 0
                kept += 1 if is_kept and not is_named else 0
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--"
                                    + rel.replace("/", "--"))
                if os.path.exists(dest):
                    got = sha256_file(dest)
                    assert got == h, "reclaim: %s exists with sha256 %s, source %s" % (dest, got, h)
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest) == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, "
        "%d already held; forensic store %d -> %d files" % (
            considered, named, kept, copied, held, before, after))

# ---- the self-test -------------------------------------------------------------------------------


def synth_reply(token, cond, bids, asks, ts, tick="0.01"):
    """A /book reply as the venue sends it: bids ascending and asks descending, the worst price first."""
    return json.dumps({
        "market": cond, "asset_id": token, "timestamp": str(ts), "hash": sha256_bytes(token.encode())[:40],
        "bids": [{"price": p, "size": q} for p, q in sorted(bids, key=lambda z: D(z[0]))],
        "asks": [{"price": p, "size": q} for p, q in sorted(asks, key=lambda z: -D(z[0]))],
        "min_order_size": "5", "tick_size": tick, "neg_risk": False, "last_trade_price": "0.5"},
        separators=(",", ":"))


def synth_window(root, t, mp, books, complete=7):
    """window.json and books.jsonl.gz in the chain book's own format. books[(tau, market, outcome)] is
    (bids, asks, tick, receive delay ms, book time shift ms); a missing key is a coherent book around 0.5.
    The reply's own timestamp is 20 ms after the checkpoint plus the shift, its receipt 45 ms after plus the
    delay."""
    d = os.path.join(root, str(t))
    os.makedirs(d, exist_ok=True)
    lines = []
    for off, tau in zip(OFFSETS, TAUS):
        for m in ("m15", "m5"):
            for o in ("Up", "Down"):
                tok = mp[m][o]
                bids, asks, tick, late, shift = books.get((tau, m, o), (
                    [("0.48", "100"), ("0.47", "300")], [("0.52", "100"), ("0.53", "300")], "0.01", 0, 0))
                raw = synth_reply(tok, mp[m]["condition"], bids, asks, (t + off) * 1000 + 20 + shift, tick)
                b = raw.encode()
                lines.append(json.dumps({
                    "T": t, "tau_prime": tau, "market": m,
                    "slug": slug15(t) if m == "m15" else slug5(t + 600),
                    "token_id": tok, "outcome_label": o, "url": "u", "status": 200,
                    "send_mono_ns": 10 ** 12 + off * 10 ** 9,
                    "recv_mono_ns": 10 ** 12 + off * 10 ** 9 + (40 + late) * 10 ** 6,
                    "recv_wall_ns": ((t + off) * 1000 + 45 + late) * 10 ** 6, "bytes": len(b),
                    "sha256": sha256_bytes(b),
                    "raw": raw, "reason": None}, sort_keys=True, separators=(",", ":")))
    with open(os.path.join(d, "books.jsonl.gz"), "wb") as fh:
        fh.write(gz_bytes(("\n".join(lines) + "\n").encode()))
    wj = {"T": t, "document_instant": t + 625, "closed_wall_ns": (t + 905) * 10 ** 9, "documents_ok": True,
          "checkpoints_complete": complete, "status_counts": {"200": 28}, "skews_ns": [1] * 7, "missed": 0,
          "markets": {m: {"slug": slug15(t) if m == "m15" else slug5(t + 600),
                          "clobTokenIds": json.dumps([mp[m]["Up"], mp[m]["Down"]]),
                          "outcomes": '["Up", "Down"]', "conditionId": mp[m]["condition"]}
                      for m in ("m15", "m5")}}
    with open(os.path.join(d, "window.json"), "wb") as fh:
        fh.write(dumps(wj).encode())


def synth_doc(slug, start, mp, ptb, fin, up, fee=None):
    return {"slug": slug, "closed": True, "outcomes": '["Up", "Down"]',
            "outcomePrices": '["1", "0"]' if up else '["0", "1"]', "feeType": FEE_TYPE,
            "feeSchedule": fee or dict(FEE_SCHEDULE), "eventStartTime": iso(start),
            "conditionId": mp["condition"], "clobTokenIds": json.dumps([mp["Up"], mp["Down"]]),
            "events": [{"eventMetadata": {"priceToBeat": D(ptb), "finalPrice": D(fin)}}]}


def mode_selftest():
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    ok(MALLOC_TUNED, "glibc took the 128 KiB mmap threshold and the two arenas")
    ok(getcontext().prec == 60, "Decimal arithmetic at 60 digits in the thread that does every sum")
    t14 = tz14()
    ok(t14.fee_pp(D("0.50")) == D("0.0175") and t14.fee_pp(D("0.85")) == D("0.008925")
       and t14.fee_pp(D("0.90")) == D("0.0063"), "tz14.fee_pp at CANON section 1.1's three points")
    ok(getcontext().prec == 60, "loading tz14 leaves the precision at 60 digits")
    # the costs, against exact rationals computed outside this file (TZ-24 section 10, C2)
    r = classify(D("0.95"), D("0.04"), 0, 0)
    ok(r["k_top"] == D("0.996013") and r["cls"] == "firm", "0.95 + 0.04 after both fees on top: 0.996013, firm")
    ok(abs(r["k_shares"] - D("0.99621832502954164619048315760392936168528098774527312144822")) < D("1e-50"),
       "0.95 + 0.04 with the fee in shares: 1157525/1161919")
    r = classify(D("0.480"), D("0.485"), 7000000, 0)
    ok(r["k_top"] == D("0.99995625") and r["cls"] == "loose" and r["sub"] == "convention",
       "0.480 + 0.485: 0.99995625 on top, below 1; in shares above 1: loose, convention")
    ok(abs(r["k_shares"] - D("1.00127013455235589192119365130384999402817782813903228834089")) < D("1e-50"),
       "0.480 + 0.485 with the fee in shares: 1.0012701345...")
    r = classify(D("0.97"), D("0.02"), 400000000, 0)
    ok(r["k_top"] == D("0.993409") and r["cls"] == "loose" and r["sub"] == "apart",
       "0.97 + 0.02 received 400 ms apart: loose, apart")
    ok(classify(D("0.97"), D("0.02"), 150000000, 150)["cls"] == "firm",
       "received 150 ms apart, books 150 ms apart: firm")
    ok(classify(D("0.97"), D("0.02"), 150000001, 0)["cls"] == "loose", "received 150 ms and 1 ns apart: loose")
    ok(classify(D("0.97"), D("0.02"), 0, 151)["sub"] == "apart", "books 151 ms apart by their own clocks: loose")
    ok(classify(D("0.97"), D("0.02"), None, 0)["sub"] == "no time", "a leg without a receive time is not firm")
    ok(classify(D("0.97"), D("0.02"), 0, None)["sub"] == "no time", "a book without its own time is not firm")
    r = classify(D("0.996"), D("0.003"), 0, 0)
    ok(r["k_top"] == D("0.99948825") and r["cls"] == "firm" and
       abs(r["k_shares"] - D("0.99950403631641686324217092909083527810659239239162280689988")) < D("1e-50"),
       "a one-tick inversion at the 0.001 tick: 0.99948825, firm")
    r = classify(D("0.50"), D("0.50"), 0, 0)
    ok(r["k_top"] == D("1.035") and r["cls"] == "none", "0.50 + 0.50 costs 1.035: none")
    ok(classify(None, D("0.5"), 0, 0)["cls"] == "unquoted", "a leg without an ask is unquoted")
    for a in (D("0.001"), D("0.01"), D("0.3333"), D("0.5"), D("0.99"), D("0.999")):
        top, shares = costs(a)
        ok(shares >= top > a, "the fee in shares costs at least the fee on top, at %s" % a)
    # the pairs and the containment, by enumeration of the reading at T + 900
    ok(pairs_of(D("0.01")) == ["A"] and pairs_of(D("-3.5")) == ["B"] and pairs_of(D("0")) == ["A", "B"],
       "the pairs by the sign of D")
    ok(LEGS["A"] == (("m15", "Up"), ("m5", "Down")) and LEGS["B"] == (("m5", "Up"), ("m15", "Down")),
       "A buys 15m Up and 5m Down; B buys 5m Up and 15m Down")
    r0 = D("78000.5")
    for r600 in (D("78010.25"), D("77990.75"), r0):
        for r900 in (D("77980"), D("77990.75"), D("77995"), r0, D("78005"), D("78010.25"), D("78020")):
            for p in pairs_of(r600 - r0):
                ok(payoff(p, r0, r600, r900) >= 1,
                   "pair %s pays at least 1: R0 %s, R600 %s, R900 %s" % (p, r0, r600, r900))
    ok(payoff("A", r0, D("78010.25"), D("78005")) == 2, "between the strikes pair A pays 2")
    ok(payoff("A", r0, D("77990.75"), D("77995")) == 0, "pair A is not dominated where D < 0")
    # NONE's alternative and VIOLATION's power, against values computed outside this file
    ok(theta1(N_MIN) <= D("0.01") < theta1(N_MIN - 1), "N_MIN = 528 is the fewest members with theta1 <= 1%")
    ok(abs(theta1(528) - D("0.0099845124461688076149542661933792988781358095260817")) < D("1e-50"),
       "theta1(528) = 0.009984512446...")
    for k in (528, 1000, 1084, 1175):
        ok(abs((1 - theta1(k)) ** k - ALPHA) < D("1e-50"), "(1 - theta1(%d))^%d = alpha" % (k, k))
    ok(abs(power(1000, D("0.01")) - D("0.99995682875258934174901136717136474026078912309378513559")) <
       D("1e-50"), "power(1000, 0.01) = 1 - 0.99^1000")
    ok([reading_of(*a) for a in ((1084, 0, 0), (527, 0, 0), (528, 0, 0), (1084, 1, 1), (0, 2, 9),
                                 (1084, 0, 3))] ==
       ["NONE", "UNDECIDABLE", "NONE", "VIOLATION", "VIOLATION", "UNDECIDABLE"],
       "the reading table, by clean members, firm windows and any windows")
    ok(CONSIDERED == 1175 and TAUS == (245, 185, 125, 95, 65, 35, 15), "1,175 windows of seven checkpoints")
    ok(iso(FIRST_T) == "2026-09-23T17:30:00Z" and iso(LAST_T + 600) == "2026-10-05T23:10:00Z",
       "the span: 2026-09-23 17:30 to the window whose five-minute market opens 2026-10-05 23:10")
    # the audit rule, as a pure function, and the hook itself
    cb = CHAINBOOK + "/%d/%s"
    ok(cb_decision(cb % (FIRST_T, "window.json"), "rb", None, False) == "allow", "window.json read: allowed")
    ok(cb_decision(cb % (LAST_T, "books.jsonl.gz"), "rb", None, True) == "allow", "books in score: allowed")
    ok(cb_decision(cb % (LAST_T, "books.jsonl.gz"), "rb", None, False) != "allow", "books before score: refused")
    ok(cb_decision(cb % (LAST_T + WINDOW, "window.json"), "rb", None, False) != "allow",
       "a window after the span: refused")
    ok(cb_decision(cb % (FIRST_T - WINDOW, "window.json"), "rb", None, False) != "allow",
       "a window before the span: refused")
    ok(cb_decision(cb % (FIRST_T + 300, "window.json"), "rb", None, False) != "allow", "off the grid: refused")
    ok(cb_decision(cb % (FIRST_T, "window.json"), "r+b", None, False) != "allow", "a write mode: refused")
    ok(cb_decision(cb % (FIRST_T, "window.json"), None, os.O_RDWR, False) != "allow", "os.open RDWR: refused")
    ok(cb_decision(cb % (FIRST_T, "window.json"), None, os.O_RDONLY, False) == "allow", "os.open RDONLY: allowed")
    ok(cb_decision(CHAINBOOK + "/runtime.jsonl", "rb", None, False) != "allow", "runtime.jsonl: refused")
    ok(cb_decision(cb % (FIRST_T, "documents.jsonl"), "rb", None, False) != "allow", "documents.jsonl: refused")
    for p in (RECORDER + "/runtime.jsonl", CHAINBOOK + "/runtime.jsonl",
              CHAINBOOK + "/%d/books.jsonl.gz" % FIRST_T):
        try:
            open(p, "rb")
            refused = False
        except RuntimeError:
            refused = True
        except OSError:
            refused = False
        ok(refused and REFUSED[-1] == p, "the hook refuses %s before it is opened" % p)
    REFUSED.clear()
    # windows and documents
    mp = {"m15": {"Up": "111", "Down": "222", "condition": "0x" + "1" * 64},
          "m5": {"Up": "333", "Down": "444", "condition": "0x" + "2" * 64}}
    t = FIRST_T
    good = {"T": t, "documents_ok": True, "checkpoints_complete": 7, "missed": 0,
            "markets": {"m15": {"slug": slug15(t), "clobTokenIds": '["111", "222"]', "outcomes": '["Up", "Down"]',
                                "conditionId": mp["m15"]["condition"]},
                        "m5": {"slug": slug5(t + 600), "clobTokenIds": '["333", "444"]',
                               "outcomes": '["Up", "Down"]', "conditionId": mp["m5"]["condition"]}}}
    ok(window_problem(good, t) == (None, mp), "a complete window.json yields the chain book's token map")
    for change, why in ((("checkpoints_complete", 6), "incomplete"), (("missed", 1), "incomplete"),
                        (("documents_ok", False), "documents"), (("T", t + 900), "window T")):
        bad = dict(good)
        bad[change[0]] = change[1]
        ok(window_problem(bad, t)[0] == why, "%s=%r reads %s" % (change[0], change[1], why))
    d15 = synth_doc(slug15(t), t, mp["m15"], "78000.5", "78020.25", True)
    d5 = synth_doc(slug5(t + 600), t + 600, mp["m5"], "78030", "78020.25", False)
    ok(doc_problem(d15, t, mp["m15"]) is None and doc_problem(d5, t + 600, mp["m5"]) is None,
       "two settled documents that conform")
    ok(identities(d15, d5) == (True, True, True), "E1, E2 and E3 hold")
    ok(doc_problem(d15, t + 900, mp["m15"]) == "start", "a document of another window reads start")
    ok(doc_problem(dict(d15, closed=False), t, mp["m15"]) == "open", "an open document")
    ok(doc_problem(dict(d15, outcomePrices='["0.5", "0.5"]'), t, mp["m15"]) == "unresolved", "unresolved")
    ok(doc_problem(dict(d15, feeSchedule=dict(FEE_SCHEDULE, rebateRate=D("0.25"))), t, mp["m15"]) == "fee",
       "another rebate rate reads fee")
    ok(doc_problem(dict(d15, clobTokenIds='["222", "111"]'), t, mp["m15"]) == "not the chain book's tokens",
       "tokens swapped against the chain book's read so")
    ok(doc_problem(dict(d15, events=[{"eventMetadata": {"priceToBeat": D("1")}}]), t, mp["m15"]) == "readings",
       "a document without finalPrice reads readings")
    ok(doc_problem(None, t, mp["m15"]) == "absent", "no document reads absent")
    tie = synth_doc(slug15(t), t, mp["m15"], "78020.25", "78020.25", True)
    ok(identities(tie, d5)[1], "E2 at equality: Up")
    ok(not identities(synth_doc(slug15(t), t, mp["m15"], "78000.5", "78020.250", True), d5)[0],
       "E1 compares literals: 78020.250 is not 78020.25")
    ok(not identities(dict(d15, outcomePrices='["0", "1"]'), d5)[1], "E2 fails on the wrong outcome")
    # line_check is total on what a stored line can hold
    good_raw = synth_reply("111", mp["m15"]["condition"], [("0.48", "10")], [("0.52", "10")], t * 1000)
    line = {"T": t, "tau_prime": 245, "market": "m15", "slug": slug15(t), "token_id": "111",
            "outcome_label": "Up", "url": "u", "status": 200, "send_mono_ns": 1, "recv_mono_ns": 2,
            "recv_wall_ns": 3, "bytes": len(good_raw.encode()), "sha256": sha256_bytes(good_raw.encode()),
            "raw": good_raw, "reason": None}
    member = {"T": t, "map": mp}
    ok(line_check(line, t, member)[0] is None, "a stored line as the chain book writes it reads valid")
    ok(line_check(dict(line, raw="\ud800"), t, member)[0] == "raw", "a body that is not UTF-8 text reads raw")
    ok(line_check(dict(line, raw="{", bytes=1, sha256=sha256_bytes(b"{")), t, member)[0] == "body",
       "a body that does not parse reads body")
    ok(line_check(dict(line, token_id=["111"]), t, member)[0] == "token", "a token that is not text reads token")
    ok(line_check(dict(line, outcome_label="Down"), t, member)[0] == "token", "a label against the map reads token")
    ok(line_check(dict(line, status=403), t, member)[0] == "status", "a refused read reads status")
    ok(line_check({"T": t}, t, member)[0] == "keys", "a line without the chain book's keys reads keys")
    ok(venue_ms({"timestamp": "\u00b2"}) is None and venue_ms({"timestamp": "1790184600123"}) == 1790184600123,
       "a book time is a run of ASCII digits or nothing")
    # a synthetic chain book end to end: the set, the constants, the score, twice
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    try:
        root = os.path.join(tmp, "chainbook")
        ts = [FIRST_T + WINDOW * k for k in range(10)]
        maps, docs = {}, {}
        plan = {  # T index: (R0, R600, R900, books)
            0: ("78000.5", "78010.25", "78005",
                {(35, "m15", "Up"): ([("0.94", "50")], [("0.95", "50")], "0.01", 0, 0),
                 (35, "m5", "Down"): ([("0.03", "20")], [("0.04", "20")], "0.01", 0, 0)}),
            1: ("78000.5", "77990.75", "77995", {}),
            2: ("78000.5", "78010.25", "78020",
                {(65, "m15", "Up"): ([("0.470", "9")], [("0.480", "9")], "0.001", 0, 0),
                 (65, "m5", "Down"): ([("0.484", "9")], [("0.485", "9")], "0.001", 0, 0)}),
            3: ("78000.5", "77990.75", "78001",
                {(15, "m5", "Up"): ([("0.96", "7")], [("0.97", "7")], "0.01", 0, 0),
                 (15, "m15", "Down"): ([("0.01", "8")], [("0.02", "8")], "0.01", 400, 0)}),
            4: ("78000.5", "78010.25", "77999",
                {(245, "m15", "Up"): ([("0.48", "100")], [("0.52", "4")], "0.01", 0, 0)}),
            5: ("78000.5", "78000.5", "78001",
                {(95, "m15", "Up"): ([("0.94", "50")], [("0.95", "50")], "0.01", 0, 0),
                 (95, "m5", "Down"): ([("0.03", "20")], [("0.04", "20")], "0.01", 0, 300)}),
            6: ("78000.5", "78010.25", "78005", {}),
            8: ("78000.5", "78010.25", "78005", {}),
            9: ("78000.5", "78010.25", "78005", {}),
        }
        for k, t in enumerate(ts):
            maps[t] = {"m15": {"Up": str(1000 + 4 * k), "Down": str(1001 + 4 * k),
                               "condition": "0x%064x" % (2 * k + 1)},
                       "m5": {"Up": str(1002 + 4 * k), "Down": str(1003 + 4 * k),
                              "condition": "0x%064x" % (2 * k + 2)}}
            if k == 7:
                continue                      # no directory
            r0, r600, r900, books = plan[k]
            synth_window(root, t, maps[t], books, complete=6 if k == 6 else 7)
            up15, up5 = D(r900) >= D(r0), D(r900) >= D(r600)
            docs[slug15(t)] = synth_doc(slug15(t), t, maps[t]["m15"], r0, r900, up15,
                                        fee=dict(FEE_SCHEDULE, rate=D("0.08")) if k == 9 else None)
            docs[slug5(t + 600)] = synth_doc(slug5(t + 600), t + 600, maps[t]["m5"], r600,
                                             "78005.5" if k == 8 else r900, up5)
        # window 4: one stored line whose hash is not its body's
        p = os.path.join(root, str(ts[4]), "books.jsonl.gz")
        with gzip.open(p, "rb") as fh:
            lines = fh.read().decode().split("\n")
        hit = [i for i, ln in enumerate(lines) if '"tau_prime":125' in ln and '"market":"m5"' in ln][0]
        rec = json.loads(lines[hit])
        rec["sha256"] = "0" * 64
        lines[hit] = json.dumps(rec, sort_keys=True, separators=(",", ":"))
        with open(p, "wb") as fh:
            fh.write(gz_bytes("\n".join(lines).encode()))
        asked = []

        def fake_docs(_dir, slugs):
            asked.append(list(slugs))
            return {s: docs[s] for s in slugs if s in docs}
        base = os.path.join(tmp, "set")
        s = form_set(base, root, ts, fake_docs)
        st = dict(s["considered"])
        ok([st[t] for t in ts] == ["member"] * 6 + ["incomplete", "no directory", "E1", "15m document: fee"],
           "ten windows: six members, and four non-members with their reasons")
        ok([len(a) for a in asked] == [16], "eight windows' documents in one request of sixteen slugs")
        c, cpath, csha = build_constants(base, s, "t")
        ok(c["members"] == 6 and c["pairs"] == {"A": 3, "B": 2, "AB": 1} and not c["none_possible"],
           "constants: six members, pairs A 3, B 2, AB 1; NONE impossible below 528")
        BOOKS_OPEN[0] = True
        res = score(base, root, s, c, "t")
        ok(res["v_firm"] == 1 and res["v_any"] == 4 and res["reading"] == "VIOLATION",
           "V_firm 1 and V_any 4: VIOLATION")
        ok(res["n_clean"] == 5 and not res["none_possible"], "five clean members: the sixth has an invalid unit")
        ok(res["rows"] == 49 and res["invalid"] == {"hash": 1}, "49 rows, one invalid unit, by its hash")
        ok(res["classes"] == {"firm": 1, "loose": 3, "none": 43, "unquoted": 1},
           "classes: firm 1, loose 3, none 43, unquoted 1")
        ok(res["loose_by"] == {"convention": 1, "apart": 2, "no time": 0},
           "loose: convention 1, apart 2 - received 400 ms apart, and books 300 ms apart by their own clocks")
        ok(abs(res["firm_profit_at_touch"] -
               (1 - D("0.99621832502954164619048315760392936168528098774527312144822")) * 20) < D("1e-48"),
           "the firm unit's profit at the touch: its margin, 0.0037816749..., times 20 shares")
        ok(res["pre_fee_inversions"] == 4, "four rows whose asks sum below 1 before any fee")
        with open(cpath, "rb") as fh:
            const0 = fh.read()
        res2 = score(base, root, s, c, "t")
        ok(res2 == res, "a second score writes and returns the same")
        # the constants ignore every book; the score does not (negative control)
        p0 = os.path.join(root, str(ts[0]), "books.jsonl.gz")
        synth_window(root, ts[0], maps[ts[0]],
                     {(35, "m15", "Up"): ([("0.94", "50")], [("0.96", "50")], "0.01", 0, 0),
                      (35, "m5", "Down"): ([("0.03", "20")], [("0.04", "20")], "0.01", 0, 0)})
        base2 = os.path.join(tmp, "set2")
        os.makedirs(base2)
        shutil.copy(os.path.join(base, "set.json"), os.path.join(base2, "set.json"))
        c2, cpath2, _h = build_constants(base2, s, "t")
        with open(cpath2, "rb") as fh:
            ok(fh.read() == const0, "the constants file is byte-identical with a book changed")
        res3 = score(base2, root, s, c2, "t")
        ok(res3["v_firm"] == 0 and res3["v_any"] == 3 and res3["reading"] == "UNDECIDABLE",
           "the score moves when the book moves: 0.96 + 0.04 is no violation")
        ok(os.path.exists(p0), "the synthetic book stands")
        BOOKS_OPEN[0] = False
    finally:
        BOOKS_OPEN[0] = False
        shutil.rmtree(tmp, ignore_errors=True)
    # deterministic gzip and JSON
    ok(gz_bytes(b"abc\n") == gz_bytes(b"abc\n"), "gzip is deterministic")
    ok(dumps({"b": D("0.10"), "a": 1}) == '{"a":1,"b":"0.10"}\n', "JSON is sorted with Decimals as text")
    ok(fx(D("1E-7")) == "0.0000001", "no exponent form")
    ok(len(t14.CAPTURE_OPENS) == 0, "tz14's own hook recorded no open under the recorder's root")
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz24-nesting-b2.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "still": mode_still,
             "rehearse": mode_rehearse, "fetch": mode_fetch, "constants": mode_constants,
             "score": mode_score}
    if mode == "reclaim":
        mode_reclaim(rest)
    elif mode == "scratch":
        assert len(rest) == 1, "scratch OWN"
        mode_scratch(rest[0])
    else:
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    out("malloc tuned: %s" % MALLOC_TUNED)
    out("peak memory of this run: %d bytes" % (
        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
    out("opens refused under the capture roots: %d; chain book opens: window.json %d, books.jsonl.gz %d; "
        "tz14's record of opens under the recorder's root: %s" % (
            len(REFUSED), CB_OPENS["window.json"], CB_OPENS["books.jsonl.gz"],
            len(_TZ14[0].CAPTURE_OPENS) if _TZ14 else "not loaded"))


if __name__ == "__main__":
    main(sys.argv[1:])
