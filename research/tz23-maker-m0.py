#!/usr/bin/env python3
"""TZ-23 - the maker track's first step, M0: do the makers of btc-updown-5m earn, at settlement and
with the 20% rebate, on the fills inside [T0, T0 + 240)?

    selftest          every rule of this file, on literals
    still             both capture units' MainPID and NRestarts: the first run records them, the
                      second compares
    rehearse          the whole path on the Architect's excluded span of 2026-10-03/04, against the
                      Architect's independent figures (G-REHEARSAL)
    fetch             the set - the first 4,032 qualifying markets from 1788530400 - and their
                      taker fills
    constants         label-free: every member's sums, V, the thresholds and the power, on disk
    rebate            label-free: the exact maker rebate of every 63rd member, from both feeds
    score             the labels, read once, and the reading
    scratch           the UUID directories beside this session's own, and which of them a running
                      claude process made
    reclaim TREE...   section 9

It requests gamma-api.polymarket.com and data-api.polymarket.com and nothing else, every request with
the two headers HEADERS fixes. Under /var/lib/btc-recorder and /var/lib/btc-chainbook it opens nothing:
an audit hook refuses any open there. It writes under /root/tz23-work/ and, in `reclaim`, new files in
/root/btc-forensics/ by exclusive create. It prints no price, size or outcome of any single fill or
market; it prints sums over a set. Exit 0: every assert of the mode held. Exit 1: an assert failed, and
its message names it. Run it with the recorder's interpreter, /root/tz04a-env.

Written for CryptoTZ/TZ-23-maker-m0.md. The TZ is the specification.
"""

import concurrent.futures
import datetime
import gzip
import hashlib
import io
import json
import math
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
from decimal import Decimal as D, getcontext

if not __debug__:
    sys.stderr.write("tz23: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

getcontext().prec = 60

# ---- the TZ's constants ------------------------------------------------------------------------

START = 1788530400           # 2026-09-04 14:00:00 UTC: the crypto taker delay is 150 ms from here on
N_SET = 4032                 # two whole weeks of five-minute markets
STEP = 300
CHUNK = 20                   # the most condition ids /v2/trades takes in one request
WINDOW = (0, 240)            # [T0, T0 + 240): the pricer's domain ends at tau = 60
BANDS = (("pre", None, 0), ("w0", 0, 60), ("w1", 60, 120), ("w2", 120, 180), ("w3", 180, 240),
         ("last", 240, 300), ("post", 300, None))
WINDOW_BANDS = ("w0", "w1", "w2", "w3")
EXCLUDED = ((1788998400, 1790452200, "labels read, TZ-04b to TZ-17"),
            (1791050100, 1791097800, "explored 2026-10-03/04"),
            (1788350400, 1788524100, "explored 2026-09-02/04"))
REHEARSAL = (1791050100, 144)
FEE_TYPE = "crypto_fees_v2"
FEE_SCHEDULE = {"exponent": 1, "rate": D("0.07"), "takerOnly": True, "rebateRate": D("0.2")}
REBATE_COEF = D("0.014")     # rebateRate 0.2 times the crypto fee rate 0.07
ALPHA = D("0.005")           # each answer's false-reading probability
DELTA = D("0.005")           # half a tick per share: NO EARN's alternative
LAMBDA = D("0.000021932")    # fixed before any member is read: sqrt(8 ln 200 / V projected)
SAMPLE_EVERY = 63            # the rebate check reads members 62, 125, ... : 64 of 4,032
FETCH_WORKERS = 2
FETCH_BUDGET_S = 7200        # a fetch projected past this after its first 30 chunks is BLOCKED
MEM_FLOOR = 147152896        # MemAvailable below which a mode that reads the venue or the cache stops
RESOLVED_AFTER_S = 3900      # a market younger than this may be unresolved; the walk stops before it
WALK_SLACK = 2016            # the walk considers at most one week of non-members beyond its need
MAX_PAGES = 5000             # a chunk's feed longer than this is BLOCKED
UA = "btc-5m-twap-m0/TZ-23"
HEADERS = {"User-Agent": UA, "Accept": "application/json"}
GAMMA = "https://gamma-api.polymarket.com/markets"
TRADES = "https://data-api.polymarket.com/v2/trades"

# The Architect's independent figures for the rehearsal span: v1 /trades, offset paging, raw pages
# parsed to Decimal by a script that shares no code with this file (TZ-23 section 10, C2).
REF = {
    "members": 144, "ups": 75, "n": 128031,
    "sh": D("3509409.854401"), "X": D("-44336.003951"), "C": D("-108894.2181475504884399"),
    "R": D("8015.91427290719561009665372913342"), "V": D("2140569358.582178867947"),
    "XU": D("-88853.166114"), "S": D("28056.96630645768404999665372913342"),
}

UNITS = {"recorder": "btc-recorder.service", "chainbook": "btc-chainbook.service"}
WORK = "/root/tz23-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/label-ledger.jsonl"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
CAPTURE_ROOTS = ("/var/lib/btc-recorder", "/var/lib/btc-chainbook")
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
CONDITION = re.compile(r"0x[0-9a-f]{64}")
LIVE_S = 60                  # a directory born this soon after a claude process started is that process's

OPENS = []


def _malloc_tune():
    """glibc raises its mmap threshold each time it frees a large block, so the 0.8 MB pages this TZ
    parses would be served from the heap and never returned; fixed at 128 KiB, with two arenas, the
    run's resident peak stays flat (TZ-23 section 0.3). True where both settings took."""
    try:
        import ctypes
        libc = ctypes.CDLL("libc.so.6")
        # mallopt(M_MMAP_THRESHOLD = -3, 128 KiB) and mallopt(M_ARENA_MAX = -8, 2)
        return libc.mallopt(-3, 131072) == 1 and libc.mallopt(-8, 2) == 1
    except (OSError, AttributeError):
        return False


MALLOC_TUNED = _malloc_tune()


def _audit(event, args):
    """No open at all under either capture root."""
    if event != "open" or not args or not isinstance(args[0], str):
        return
    path = os.path.abspath(args[0])
    for root in CAPTURE_ROOTS:
        if path == root or path.startswith(root + "/"):
            OPENS.append(path)
            raise RuntimeError("open refused under a capture root: %s" % path)


sys.addaudithook(_audit)


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))


def fx(x):
    """A Decimal as fixed-point text, never in exponent form."""
    return format(x, "f")


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
    """The first run writes; a later run must produce the same bytes (determinism, contract §6)."""
    if os.path.exists(path):
        got = sha256_file(path)
        assert got == sha256_bytes(data), "determinism: %s differs from the first run" % path
        out("unchanged %s sha256 %s" % (path, got))
        return got
    write_atomic(path, data)
    return sha256_bytes(data)


def gz_bytes(text):
    """Deterministic gzip: no name, no time."""
    buf = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buf, mtime=0) as g:
        g.write(text.encode("utf-8"))
    return buf.getvalue()


def dumps(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=_dec) + "\n"


def _dec(o):
    if isinstance(o, D):
        return fx(o)
    raise TypeError(type(o))


def mem_available():
    with open("/proc/meminfo", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) * 1024
    raise AssertionError("no MemAvailable")


def floor_check():
    """Before a mode that reads the venue or the cache: glibc's two settings, and the memory floor."""
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


# ---- the venue -----------------------------------------------------------------------------------

def http_json(url, tries=8):
    """One GET with HEADERS, parsed with every JSON number as a Decimal of its own text. 429 and 5xx
    and transport errors are retried, honouring Retry-After up to 60 s; anything else is fatal."""
    last = None
    for k in range(tries):
        req = urllib.request.Request(url, headers=HEADERS, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
                assert r.status == 200, "HTTP %d %s" % (r.status, url)
                return json.loads(body, parse_float=D)
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


def gamma_docs(t0s):
    """The closed market documents of the given five-minute slugs, one request, keyed by slug."""
    q = [("slug", "btc-updown-5m-%d" % t) for t in t0s]
    q += [("closed", "true"), ("limit", str(len(t0s) + 5))]
    docs = http_json(GAMMA + "?" + urllib.parse.urlencode(q))
    assert isinstance(docs, list), "gamma: not a list"
    by = {}
    for d in docs:
        assert d["slug"] not in by, "gamma: slug %s twice" % d["slug"]
        by[d["slug"]] = d
    return by


def trades(cids, taker_only, tokens=None, keep_tx=False):
    """Every row /v2/trades serves for these conditions. The cursor carries no filter, so every
    request re-sends `condition` and `taker_only` beside it (TZ-23 section 1); every row is asserted
    to belong to the requested conditions and, where `tokens` is given, to carry its market's token
    for its outcome. Returns {condition: [row, ...]}; a row is [ts, side, outcome, size, price], or
    with `keep_tx` [ts, side, outcome, size, price, token, transaction, wallet]."""
    assert 1 <= len(cids) <= CHUNK and len(set(cids)) == len(cids)
    by = {c: [] for c in cids}
    cursor, pages = None, 0
    while True:
        q = {"condition": ",".join(cids), "limit": "1000", "taker_only": taker_only}
        if cursor:
            q["cursor"] = cursor
        doc = http_json(TRADES + "?" + urllib.parse.urlencode(q))
        pages += 1
        assert pages <= MAX_PAGES, "BLOCKED: more than %d pages for %s" % (MAX_PAGES, cids[0])
        assert isinstance(doc.get("data"), list) and isinstance(doc.get("pagination"), dict)
        for r in doc["data"]:
            c = r["condition_id"]
            assert c in by, "a row of %s outside the request" % c
            row = compact(r)
            if tokens is not None:
                assert r["token_id"] == tokens[c][0 if row[2] == "U" else 1], "token of %s" % c
            if keep_tx:
                row += [r["token_id"], r["transaction_hash"], r["proxy_wallet"]]
            by[c].append(row)
        cursor = doc["pagination"].get("next_cursor")
        if not cursor:
            assert doc["pagination"].get("has_more") in (False, None), "no cursor, has_more"
            break
    return by


def compact(r):
    """[block time, side, outcome, size, price], sizes and prices as the text of their Decimals."""
    side, outcome = r["side"], r["outcome"]
    assert side in ("BUY", "SELL"), side
    assert (outcome, r["outcome_index"]) in (("Up", 0), ("Down", 1)), (outcome, r["outcome_index"])
    s, p = r["size"], r["price"]
    assert isinstance(s, D) and isinstance(p, D) and s > 0 and 0 < p < 1, (s, p)
    t = r["timestamp"]
    assert isinstance(t, int) and not isinstance(t, bool)
    return [t, side[0], outcome[0], fx(s), fx(p)]


# ---- the rules -----------------------------------------------------------------------------------

def maker_terms(side, outcome, s, p):
    """The makers' side of one taker fill in Up shares: (x, pi). x > 0 is makers long Up, pi the Up
    price of the fill. A taker who buys Up sells it from makers; a taker who buys Down at p takes it
    from makers who are then long Up at 1 - p, whether they sold Down or bought Up."""
    if outcome == "U":
        return (-s, p) if side == "B" else (s, p)
    assert outcome == "D"
    return (s, 1 - p) if side == "B" else (-s, 1 - p)


def rebate(s, p):
    """The 20% maker rebate of the venue's fee, 0.07 * s * p * (1 - p), at the price reported."""
    return REBATE_COEF * s * p * (1 - p)


def band_of(dt):
    for name, lo, hi in BANDS:
        if (lo is None or dt >= lo) and (hi is None or dt < hi):
            return name
    raise AssertionError(dt)


def zero():
    return {"n": 0, "sh": D(0), "X": D(0), "C": D(0), "R": D(0)}


def aggregate(t0, rows):
    """Per band: fills, shares, the makers' net Up position X, its cost C = sum x * pi, and the
    rebate R. The window's sums are the sums over WINDOW_BANDS."""
    bands = {name: zero() for name, _lo, _hi in BANDS}
    for row in rows:
        ts, side, outcome, s, p = row[:5]
        s, p = D(s), D(p)
        x, pi = maker_terms(side, outcome, s, p)
        b = bands[band_of(ts - t0)]
        b["n"] += 1
        b["sh"] += s
        b["X"] += x
        b["C"] += x * pi
        b["R"] += rebate(s, p)
    win = zero()
    for name in WINDOW_BANDS:
        for k in win:
            win[k] += bands[name][k]
    return bands, win


def iso(t0):
    return datetime.datetime.fromtimestamp(t0, datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")


def excluded(t0, spans):
    for lo, hi, why in spans:
        if lo <= t0 <= hi:
            return why
    return None


def qualify(t0, doc):
    """Label-free: the first condition a candidate fails, or None. outcomePrices is checked for being
    one of the two resolved forms and nothing else is read from it (TZ-23 section 2, item 6 (a))."""
    if doc is None:
        return "absent"
    if json.loads(doc["outcomes"]) != ["Up", "Down"]:
        return "outcomes"
    if json.loads(doc["outcomePrices"]) not in (["1", "0"], ["0", "1"]):
        return "unresolved"
    if doc.get("closed") is not True:
        return "open"
    if doc.get("feeType") != FEE_TYPE or doc.get("feeSchedule") != FEE_SCHEDULE:
        return "fee"
    if doc.get("eventStartTime") != iso(t0):
        return "start"
    if not CONDITION.fullmatch(doc.get("conditionId") or ""):
        return "condition"
    tok = json.loads(doc["clobTokenIds"])
    if not (isinstance(tok, list) and len(tok) == 2 and all(t.isdigit() for t in tok)):
        return "tokens"
    return None


def kept_doc(doc):
    return {k: doc[k] for k in ("slug", "conditionId", "outcomes", "outcomePrices", "closed",
                                "feeType", "feeSchedule", "eventStartTime", "clobTokenIds")}


def label_of(doc):
    """The venue's resolved outcome: 1 Up, 0 Down. Called by `score` alone."""
    return {("1", "0"): 1, ("0", "1"): 0}[tuple(json.loads(doc["outcomePrices"]))]


# ---- the gate ------------------------------------------------------------------------------------

def gate_constants(V, sh, lam=LAMBDA, alpha=ALPHA, delta=DELTA):
    """Ville's inequality on exp(lam * M - lam^2 * V / 8), M the martingale part of the makers'
    settlement result: a false reading of either answer has probability at most alpha, at any look."""
    L = (1 / alpha).ln()
    thr = L / lam + lam * V / 8
    c = {"L": L, "lambda": lam, "alpha": alpha, "delta": delta, "V": V, "sh": sh, "thr": thr,
         "earn_at": thr, "no_earn_at": delta * sh - thr}
    if sh > 0:
        c["thr_per_share"] = thr / sh
        c["no_earn_per_share"] = delta - thr / sh
    sd = float(V.sqrt()) / 2.0 if V > 0 else 0.0
    z = (float(delta * sh - thr) / sd) if sd > 0 else float("-inf")
    c["power"] = D(repr(0.5 * (1.0 + math.erf(z / math.sqrt(2.0))))) if sd > 0 else D(0)
    return c


def reading(S, c):
    earn = S >= c["earn_at"]
    no_earn = S <= c["no_earn_at"]
    if earn:
        return "EARN", earn, no_earn
    if no_earn:
        return "NO EARN", earn, no_earn
    return "UNDECIDABLE", earn, no_earn


# ---- the set -------------------------------------------------------------------------------------

def next_open(t, spans):
    """The first T0 at or after t outside every excluded span."""
    moved = True
    while moved:
        moved = False
        for lo, hi, _why in spans:
            if lo <= t <= hi:
                t, moved = hi + STEP, True
    return t


def candidates(start, spans, need, docs_of):
    """Walk T0 = start, start + 300, ... past every excluded span, in chunks of at most CHUNK and
    never more than the members still needed, so no document after the need-th member is requested;
    return every candidate considered with its status."""
    considered, members, t = [], [], next_open(start, spans)
    while len(members) < need:
        assert len(considered) < need + WALK_SLACK, "BLOCKED: %d considered for %d members" % (
            len(considered), len(members))
        chunk = []
        while len(chunk) < min(CHUNK, need - len(members)):
            chunk.append(t)
            t = next_open(t + STEP, spans)
        assert chunk[-1] <= time.time() - RESOLVED_AFTER_S, \
            "BLOCKED: the walk reached %s, too recent to be resolved" % utc(chunk[-1])
        docs = docs_of(chunk)
        for c in chunk:
            doc = docs.get("btc-updown-5m-%d" % c)
            status = qualify(c, doc) or "member"
            considered.append((c, status))
            if status == "member":
                members.append((c, kept_doc(doc)))
                if len(members) == need:
                    break
    return considered, members


def chunk_path(cache, first):
    return os.path.join(cache, "%d.json.gz" % first)


def fetch_chunk(cache, group):
    """The taker fills of up to CHUNK members, written once, atomically."""
    path = chunk_path(cache, group[0][0])
    if os.path.exists(path):
        return path, False
    cids = [d["conditionId"] for _t, d in group]
    tokens = {d["conditionId"]: json.loads(d["clobTokenIds"]) for _t, d in group}
    by = trades(cids, "true", tokens)
    for rs in by.values():
        rs.sort()
    body = dumps({"members": [{"t0": t, "condition": d["conditionId"],
                               "rows": by[d["conditionId"]]} for t, d in group]})
    write_atomic(path, gz_bytes(body))
    return path, True


def form_set(base, start, spans, need):
    os.makedirs(base, exist_ok=True)
    setp = os.path.join(base, "set.json")
    if os.path.exists(setp):
        with open(setp, encoding="utf-8") as fh:
            s = json.load(fh, parse_float=D)
        out("the set from %s sha256 %s: %d considered, %d members" % (
            setp, sha256_file(setp), len(s["considered"]), len(s["members"])))
        return s
    t = time.time()
    considered, members = candidates(start, spans, need, gamma_docs)
    s = {"start": start, "need": need, "considered": considered,
         "members": [{"t0": t0, "doc": d} for t0, d in members]}
    write_atomic(setp, dumps(s).encode("utf-8"))
    out("the set formed in %.1f s: %d considered, %d members, %s sha256 %s" % (
        time.time() - t, len(considered), len(members), setp, sha256_file(setp)))
    with open(setp, encoding="utf-8") as fh:
        return json.load(fh, parse_float=D)


def fetch_fills(base, s, budget_s=FETCH_BUDGET_S):
    cache = os.path.join(base, "cache")
    os.makedirs(cache, exist_ok=True)
    groups, cur = [], []
    for m in s["members"]:
        cur.append((m["t0"], m["doc"]))
        if len(cur) == CHUNK:
            groups.append(cur)
            cur = []
    if cur:
        groups.append(cur)
    t, done, fresh = time.time(), 0, 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=FETCH_WORKERS) as pool:
        for path, new in pool.map(lambda g: fetch_chunk(cache, g), groups):
            done += 1
            fresh += 1 if new else 0
            if fresh == 30:
                proj = (time.time() - t) / fresh * (len(groups) - done + fresh)
                out("projected %.0f s for %d chunks after %d fetched" % (proj, len(groups), fresh))
                assert proj <= budget_s, "BLOCKED: fetch projected at %.0f s, above %d" % (proj,
                                                                                          budget_s)
            if done % 25 == 0 or done == len(groups):
                out("chunks %d of %d, %.0f s" % (done, len(groups), time.time() - t))
    return cache, groups


def member_rows(cache, groups):
    """Every member's rows, in T0 order, read back from the cache."""
    for g in groups:
        with gzip.open(chunk_path(cache, g[0][0]), "rt", encoding="utf-8") as fh:
            doc = json.load(fh)
        assert [m["t0"] for m in doc["members"]] == [t for t, _d in g]
        for m, (t, d) in zip(doc["members"], g):
            assert m["condition"] == d["conditionId"]
            yield t, d, m["rows"]


# ---- constants and score -------------------------------------------------------------------------

COLS = ["t0", "weekend"] + ["%s_%s" % (k, b) for b in ["win"] + [n for n, _l, _h in BANDS]
                            for k in ("n", "sh", "X", "C", "R")]


def segments(t0s):
    """Members counted by how many excluded spans end below them."""
    ends = sorted(hi for _lo, hi, _why in EXCLUDED)
    seg = {}
    for t in t0s:
        k = str(sum(1 for e in ends if e < t))
        seg[k] = seg.get(k, 0) + 1
    return seg


def weekend(t0):
    return 1 if datetime.datetime.fromtimestamp(t0, datetime.timezone.utc).weekday() >= 5 else 0


def build_constants(base, s, cache, groups, label):
    """Label-free: the members file, the fills file and the constants file. A second run must write
    the same bytes."""
    lines = [",".join(COLS)]
    tot = {"win": zero(), **{n: zero() for n, _l, _h in BANDS}}
    V = D(0)
    fills_path = os.path.join(base, "%s-fills.jsonl.gz" % label)
    tmp = fills_path + ".build"
    with open(tmp, "wb") as raw, gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as g:
        for t0, d, rows in member_rows(cache, groups):
            bands, win = aggregate(t0, rows)
            V += win["X"] * win["X"]
            cells = [str(t0), str(weekend(t0))]
            for name, agg in [("win", win)] + [(n, bands[n]) for n, _l, _h in BANDS]:
                for k in ("n", "sh", "X", "C", "R"):
                    tot[name][k] += agg[k]
                    cells.append(str(agg[k]) if k == "n" else fx(agg[k]))
            lines.append(",".join(cells))
            g.write(dumps({"t0": t0, "rows": rows}).encode("utf-8"))
    fills_sha = sha256_file(tmp)
    if os.path.exists(fills_path):
        assert sha256_file(fills_path) == fills_sha, "determinism: %s differs" % fills_path
        os.remove(tmp)
        out("unchanged %s sha256 %s" % (fills_path, fills_sha))
    else:
        os.replace(tmp, fills_path)
    members_csv = ("\n".join(lines) + "\n").encode("utf-8")
    c = gate_constants(V, tot["win"]["sh"])
    t0s = [m["t0"] for m in s["members"]]
    nonm = [[t, st] for t, st in s["considered"] if st != "member"]
    const = {"label": label, "members": len(t0s), "first": t0s[0], "last": t0s[-1],
             "member_list_sha": sha256_bytes(("\n".join(map(str, t0s)) + "\n").encode()),
             "considered": len(s["considered"]), "non_members": nonm,
             "weekend_members": sum(weekend(t) for t in t0s),
             "segments": segments(t0s),
             "totals": tot, "gate": c, "members_csv_sha": sha256_bytes(members_csv),
             "fills_sha": fills_sha}
    body = dumps(const).encode("utf-8")
    paths = {"fills.jsonl.gz": (fills_path, fills_sha)}
    for name, data in (("members.csv", members_csv), ("constants.json", body)):
        pth = os.path.join(base, "%s-%s" % (label, name))
        paths[name] = (pth, write_once(pth, data))
    return const, paths


def show_constants(const, paths):
    g, w = const["gate"], const["totals"]["win"]
    out("members %d, considered %d, first %d %s, last %d %s, weekend members %d" % (
        const["members"], const["considered"], const["first"], utc(const["first"]), const["last"],
        utc(const["last"]), const["weekend_members"]))
    out("member list sha %s" % const["member_list_sha"])
    out("members by the number of excluded spans ending below them: %s" % (
        ", ".join("%s: %d" % kv for kv in sorted(const["segments"].items()))))
    for t, st in const["non_members"]:
        out("non-member %d %s: %s" % (t, utc(t), st))
    out("window fills %d, shares %s, X %s, C %s, R %s" % (w["n"], fx(w["sh"]), fx(w["X"]),
                                                       fx(w["C"]), fx(w["R"])))
    for name, _l, _h in BANDS:
        b = const["totals"][name]
        out("band %-4s fills %d, shares %s" % (name, b["n"], fx(b["sh"])))
    out("V %s; lambda %s; L %s" % (fx(g["V"]), fx(g["lambda"]), fx(g["L"])))
    out("EARN at S >= %s (%s a share); NO EARN at S <= %s (%s a share)" % (
        fx(g["earn_at"]), fx(g["thr_per_share"]), fx(g["no_earn_at"]),
        fx(g["no_earn_per_share"])))
    out("power of either answer against the other's alternative, normal, variance V/4: %s"
        % fx(g["power"]))
    for name, (p, h) in sorted(paths.items()):
        out("wrote %s sha256 %s" % (p, h))


def score(base, s, const, label):
    """The labels, read once from the set's own documents, and the reading."""
    with open(os.path.join(base, "%s-members.csv" % label), encoding="utf-8") as fh:
        rows = [ln.split(",") for ln in fh.read().splitlines()]
    assert rows[0] == COLS
    ix = {k: i for i, k in enumerate(COLS)}
    docs = {m["t0"]: m["doc"] for m in s["members"]}
    assert len(rows) - 1 == len(docs)
    S = P = R = XU = D(0)
    ups = 0
    bands = {n: {"XU": D(0), "C": D(0), "R": D(0), "sh": D(0)} for n, _l, _h in BANDS}
    scored = ["t0,up,X,C,R,pnl"]
    for r in rows[1:]:
        t0 = int(r[ix["t0"]])
        up = label_of(docs[t0])
        ups += up
        X, C, Rm = D(r[ix["X_win"]]), D(r[ix["C_win"]]), D(r[ix["R_win"]])
        pnl = X * up - C + Rm
        S += pnl
        P += X * up - C
        R += Rm
        XU += X * up
        scored.append("%d,%d,%s,%s,%s,%s" % (t0, up, fx(X), fx(C), fx(Rm), fx(pnl)))
        for n, _l, _h in BANDS:
            b = bands[n]
            b["XU"] += D(r[ix["X_" + n]]) * up
            b["C"] += D(r[ix["C_" + n]])
            b["R"] += D(r[ix["R_" + n]])
            b["sh"] += D(r[ix["sh_" + n]])
    g = const["gate"]
    word, earn, no_earn = reading(S, {"earn_at": D(g["earn_at"]),
                                      "no_earn_at": D(g["no_earn_at"])})
    sh = D(g["sh"])
    res = {"label": label, "members": len(docs), "ups": ups, "S": S, "P": P, "R": R, "XU": XU,
           "sh": sh, "S_per_share": S / sh, "P_per_share": P / sh, "R_per_share": R / sh,
           "earn": earn, "no_earn": no_earn, "reading": word,
           "margin_earn": S - D(g["earn_at"]), "margin_no_earn": D(g["no_earn_at"]) - S,
           "bands": {n: {"pnl_per_share": ((b["XU"] - b["C"] + b["R"]) / b["sh"]) if b["sh"]
                         else None,
                         "rebate_per_share": (b["R"] / b["sh"]) if b["sh"] else None}
                     for n, b in bands.items()}}
    body = dumps(res).encode("utf-8")
    scored_csv = ("\n".join(scored) + "\n").encode("utf-8")
    for name, data in (("scored.csv", scored_csv), ("reading.json", body)):
        write_once(os.path.join(base, "%s-%s" % (label, name)), data)
    out("labels: %d members, %d Up" % (len(docs), ups))
    out("S %s = settlement %s + rebate %s; per share %s = %s + %s" % (
        fx(S), fx(P), fx(R), fx(res["S_per_share"]), fx(res["P_per_share"]),
        fx(res["R_per_share"])))
    out("EARN %s (margin %s); NO EARN %s (margin %s)" % (earn, fx(res["margin_earn"]), no_earn,
                                                       fx(res["margin_no_earn"])))
    for n, b in res["bands"].items():
        if b["pnl_per_share"] is not None:
            out("band %-4s makers per share %s, of it rebate %s - barred from every reading" % (
                n, fx(b["pnl_per_share"]), fx(b["rebate_per_share"])))
    out("wrote %s-scored.csv sha256 %s and %s-reading.json sha256 %s" % (
        label, sha256_bytes(scored_csv), label, sha256_bytes(body)))
    return res


# ---- modes ---------------------------------------------------------------------------------------

def git(*args):
    cp = subprocess.run(["git", "-C", WT] + list(args), capture_output=True, text=True)
    assert cp.returncode == 0, "git %s: %s" % (" ".join(args), cp.stderr.strip())
    return cp.stdout.strip()


def mode_rehearse():
    floor_check()
    base = os.path.join(WORK, "rehearsal")
    s = form_set(base, REHEARSAL[0], (), REHEARSAL[1])
    assert len(s["members"]) == REF["members"] and len(s["considered"]) == REF["members"], \
        "G-REHEARSAL: %d members of %d considered" % (len(s["members"]), len(s["considered"]))
    cache, groups = fetch_fills(base, s, budget_s=10 ** 9)
    const, paths = build_constants(base, s, cache, groups, "rehearsal")
    show_constants(const, paths)
    res = score(base, s, const, "rehearsal")
    w = const["totals"]["win"]
    got = {"members": const["members"], "ups": res["ups"], "n": w["n"], "sh": w["sh"],
           "X": w["X"], "C": w["C"], "R": w["R"], "V": const["gate"]["V"], "XU": res["XU"],
           "S": res["S"]}
    bad = [k for k in REF if got[k] != REF[k]]
    for k in REF:
        out("G-REHEARSAL %-7s instrument %s, the Architect's %s, %s" % (
            k, got[k], REF[k], "equal" if got[k] == REF[k] else "DIFFERENT"))
    assert not bad, "G-REHEARSAL FAIL: %s" % bad
    out("G-REHEARSAL PASS: %d of %d figures equal" % (len(REF), len(REF)))


def mode_fetch():
    floor_check()
    os.makedirs(WORK, exist_ok=True)
    base = os.path.join(WORK, "set")
    s = form_set(base, START, EXCLUDED, N_SET)
    assert len(s["members"]) == N_SET, "G-SET: %d members" % len(s["members"])
    cache, groups = fetch_fills(base, s)
    n = sum(1 for _ in member_rows(cache, groups))
    assert n == N_SET, "G-SET: %d members read back" % n
    out("G-SET PASS: %d members, %d chunks, every chunk read back" % (N_SET, len(groups)))


def set_and_groups():
    base = os.path.join(WORK, "set")
    with open(os.path.join(base, "set.json"), encoding="utf-8") as fh:
        s = json.load(fh, parse_float=D)
    groups = [[(m["t0"], m["doc"]) for m in s["members"][i:i + CHUNK]]
              for i in range(0, len(s["members"]), CHUNK)]
    return base, s, os.path.join(base, "cache"), groups


def mode_constants():
    floor_check()
    base, s, cache, groups = set_and_groups()
    assert len(s["members"]) == N_SET
    const, paths = build_constants(base, s, cache, groups, "tz23")
    show_constants(const, paths)
    st = load_state()
    st["constants_sha"] = paths["constants.json"][1]
    st["constants_at"] = utc(time.time())
    save_state(st)


def mode_rebate():
    """Label-free. For every SAMPLE_EVERY-th member: both feeds again, with transaction and wallet;
    the maker rows of each transaction are its rows less its one taker row; the exact rebate is the
    fee formula at each maker's own price. The taker feed must equal the cached rows."""
    floor_check()
    base, s, cache, groups = set_and_groups()
    sample = [(m["t0"], m["doc"]) for i, m in enumerate(s["members"]) if i % SAMPLE_EVERY ==
              SAMPLE_EVERY - 1]
    want = {t for t, _d in sample}
    cached = {}
    for g in groups:
        if want.intersection(t for t, _d in g):
            for t, _d, rows in member_rows(cache, [g]):
                if t in want:
                    cached[t] = rows
    assert set(cached) == want, "rebate: %d of %d sampled members in the cache" % (len(cached),
                                                                                   len(want))
    exact = reported = D(0)
    sh = D(0)
    n_tx = n_multi = n_skip = n_gap = 0
    gap_sh = D(0)
    for t0, d in sample:
        cid = d["conditionId"]
        tokens = {cid: json.loads(d["clobTokenIds"])}
        taker = trades([cid], "true", tokens, keep_tx=True)[cid]
        assert sorted(r[:5] for r in taker) == cached[t0], "rebate: the taker feed of %d changed" % t0
        pool, takers = {}, {}
        for r in trades([cid], "false", tokens, keep_tx=True)[cid]:
            pool.setdefault(r[6], []).append(r)
        for r in taker:
            takers.setdefault(r[6], []).append(r)
        for tx, trs in sorted(takers.items()):
            if len(trs) != 1:
                n_skip += 1
                continue
            r = trs[0]
            if not (WINDOW[0] <= r[0] - t0 < WINDOW[1]):
                continue
            makers = pool.get(tx, [])
            assert r in makers, "rebate: the taker row of %s is not among its rows" % tx
            makers.remove(r)
            gap = D(r[3]) - sum((D(m[3]) for m in makers), D(0))
            if gap != 0:
                n_gap += 1
                gap_sh += abs(gap)
            p = D(r[4])
            reported += D(r[3]) * p * (1 - p)
            exact += sum((D(m[3]) * D(m[4]) * (1 - D(m[4])) for m in makers), D(0))
            sh += D(r[3])
            n_tx += 1
            prices = {D(m[4]) if m[2] == r[2] else 1 - D(m[4]) for m in makers}
            n_multi += 1 if len(prices) > 1 else 0
    out("rebate check: %d members, %d window transactions, %d at several prices, %d transactions "
        "with other than one taker row skipped" % (len(sample), n_tx, n_multi, n_skip))
    out("transactions whose taker size differs from its makers' sum: %d, %s shares in all" % (
        n_gap, fx(gap_sh)))
    out("fee-equivalent at the reported price %s, at each maker's own price %s, ratio %s" % (
        fx(reported), fx(exact), fx(exact / reported) if reported else "undefined"))
    out("the rebate counted above the venue's, per share of the sample's window: %s" % (
        fx(REBATE_COEF * (reported - exact) / sh) if sh else "undefined"))


def mode_score():
    base, s, cache, groups = set_and_groups()
    st = load_state()
    cpath = os.path.join(base, "tz23-constants.json")
    assert sha256_file(cpath) == st.get("constants_sha"), "score: not the constants recorded"
    head = git("rev-parse", "HEAD")
    branches = git("branch", "-r", "--contains", head).split()
    assert "origin/tz-23-maker-m0" in branches, "score: HEAD %s is not on origin" % head
    with open(cpath, encoding="utf-8") as fh:
        const = json.load(fh, parse_float=D)
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(dumps({"at": utc(time.time()), "head": head, "members": const["members"],
                        "member_list_sha": const["member_list_sha"]}))
    res = score(base, s, const, "tz23")
    out("M0 READING: %s" % res["reading"])


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
    return tree == WORK and (rel == "state.json" or rel == "label-ledger.jsonl"
                             or rel.startswith("logs/"))


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
        "%d already held; forensic store %d -> %d files" % (considered, named, kept, copied, held,
                                                           before, after))


# ---- the self-test -------------------------------------------------------------------------------

def mode_selftest():
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    ok(MALLOC_TUNED, "glibc took the 128 KiB mmap threshold and the two arenas")
    # the sign convention, at live magnitudes: a taker's result and the makers' are opposite
    for side, outcome, s, p in (("B", "U", D("364.58"), D("0.999")), ("S", "U", D("30"), D("0.99")),
                                ("B", "D", D("100"), D("0.01")), ("S", "D", D("1250.5"), D("0.47"))):
        x, pi = maker_terms(side, outcome, s, p)
        for up in (0, 1):
            won = up if outcome == "U" else 1 - up
            taker = s * (won - p) if side == "B" else s * (p - won)
            ok(x * (up - pi) == -taker, "makers' result is minus the taker's: %s %s up=%d" % (
                side, outcome, up))
    ok(maker_terms("B", "D", D("100"), D("0.01")) == (D("100"), D("0.99")),
       "a taker buying Down at 0.01 leaves makers long 100 Up at 0.99")
    ok(maker_terms("S", "D", D("10"), D("0.01")) == (D("-10"), D("0.99")),
       "a taker selling Down at 0.01 leaves makers short 10 Up at 0.99")
    # the four-maker transaction of the excluded span, by hand: makers +1 USDC if Up, -99 if Down
    x, pi = maker_terms("B", "D", D("100"), D("0.01"))
    ok(x * (1 - pi) == D("1.00") and x * (0 - pi) == D("-99.00"),
       "a 100-share Down purchase at 0.01: makers +1.00 on Up and -99.00 on Down")
    ok(rebate(D("100"), D("0.5")) == D("0.35"), "rebate of 100 shares at 0.50 is 0.35 USDC")
    ok(rebate(D("100"), D("0.99")) == D("0.01386"), "rebate of 100 shares at 0.99 is 0.01386 USDC")
    ok(rebate(D("100"), D("0.3")) == rebate(D("100"), D("0.7")), "the rebate is symmetric in p")
    ok(REBATE_COEF == FEE_SCHEDULE["rate"] * FEE_SCHEDULE["rebateRate"], "0.014 = 0.07 * 0.2")
    # bands
    ok([band_of(d) for d in (-1, 0, 59, 60, 239, 240, 299, 300)] ==
       ["pre", "w0", "w0", "w1", "w3", "last", "last", "post"], "band edges")
    ok(WINDOW == (0, 240) and WINDOW_BANDS == ("w0", "w1", "w2", "w3"), "the window is [T0, T0+240)")
    # aggregate on literal rows: a fill at T0 + 239 counts, at T0 + 240 does not
    t0 = 1788530400
    rows = [[t0 + 239, "B", "U", "10", "0.6"], [t0 + 240, "B", "U", "10", "0.6"],
            [t0 - 5, "S", "D", "4", "0.25"]]
    bands, win = aggregate(t0, rows)
    ok(win["n"] == 1 and win["sh"] == D("10") and win["X"] == D("-10") and win["C"] == D("-6.0"),
       "the window takes T0+239 and not T0+240")
    ok(bands["pre"]["X"] == D("-4") and bands["pre"]["C"] == D("-3.00"),
       "a Down sale before T0 leaves makers short 4 Up at 0.75")
    ok(bands["last"]["n"] == 1, "T0+240 is the last minute")
    # the window's sums equal the sums of its four bands
    ok(all(win[k] == sum((bands[b][k] for b in WINDOW_BANDS), D(0) if k != "n" else 0)
           for k in win), "the window is the sum of w0..w3")
    # qualification
    good = {"slug": "btc-updown-5m-1788530400", "outcomes": '["Up", "Down"]', "outcomePrices": '["0", "1"]',
            "closed": True, "feeType": FEE_TYPE,
            "feeSchedule": {"exponent": 1, "rate": D("0.07"), "takerOnly": True, "rebateRate": D("0.2")},
            "eventStartTime": "2026-09-04T14:00:00Z", "conditionId": "0x" + "ab" * 32,
            "clobTokenIds": '["123", "456"]'}
    ok(qualify(1788530400, good) is None, "a resolved, fee-schedule-conforming market qualifies")
    for key, val, why in (("outcomePrices", '["0.5", "0.5"]', "unresolved"), ("closed", False, "open"),
                          ("feeType", "crypto_fees", "fee"), ("eventStartTime", "2026-09-04T14:05:00Z", "start"),
                          ("conditionId", "0x12", "condition"), ("outcomes", '["Yes", "No"]', "outcomes"),
                          ("clobTokenIds", '["123"]', "tokens")):
        bad = dict(good)
        bad[key] = val
        ok(qualify(1788530400, bad) == why, "%s=%r reads %s" % (key, val, why))
    bad = dict(good)
    bad["feeSchedule"] = {"exponent": 1, "rate": D("0.07"), "takerOnly": True, "rebateRate": D("0.25")}
    ok(qualify(1788530400, bad) == "fee", "a 25% rebate is not this TZ's schedule")
    ok(qualify(1788530400, None) == "absent", "no document reads absent")
    ok(label_of(good) == 0 and label_of(dict(good, outcomePrices='["1", "0"]')) == 1, "labels")
    # the set walk: exclusions, the need-th member, nothing considered after it
    def fake_docs(t0s):
        return {"btc-updown-5m-%d" % t: dict(good, slug="btc-updown-5m-%d" % t, eventStartTime=iso(t),
                                            outcomePrices=('["1", "0"]' if (t // 300) % 7 else '["0.5", "0.5"]'))
                for t in t0s}
    cons, mem = candidates(1791049500, EXCLUDED, 5, fake_docs)
    ok([m[0] for m in mem] == [1791049500, 1791049800, 1791098100, 1791098700, 1791099000],
       "the walk takes the five members around the excluded span, past one unresolved")
    ok([t for t, st in cons if st != "member"] == [1791098400], "1791098400 reads unresolved")
    ok(not [t for t, _st in cons if 1791050100 <= t <= 1791097800],
       "no candidate of the explored span is considered")
    asked = []
    candidates(1791049500, EXCLUDED, 5, lambda ts: (asked.extend(ts), fake_docs(ts))[1])
    ok(asked == [t for t, _st in cons] and asked[-1] == mem[-1][0],
       "every document requested is a candidate considered, the last the 5th member's")
    ok(cons[-1][1] == "member" and cons[-1][0] == mem[-1][0], "nothing is considered after the 5th member")
    ok(excluded(1788350400, EXCLUDED) and excluded(1788524100, EXCLUDED) and
       not excluded(1788524400, EXCLUDED), "the 2026-09-02/04 span is excluded, its next market is not")
    ok(excluded(1791097800, EXCLUDED) and not excluded(1791098100, EXCLUDED),
       "the 2026-10-03/04 span ends at 1791097800")
    ok(excluded(1788998400, EXCLUDED) and excluded(1790452200, EXCLUDED) and
       not excluded(1788998100, EXCLUDED) and not excluded(1790452500, EXCLUDED),
       "the labelled span 1788998400 ... 1790452200 is excluded, its neighbours are not")
    ok(next_open(1788998100 + STEP, EXCLUDED) == 1790452500, "the walk steps over the labelled span")
    ok(START == 1788530400 and iso(START) == "2026-09-04T14:00:00Z", "the set starts at 2026-09-04 14:00 UTC")
    # the gate: Ville's threshold, independent of the code path, at a realistic V
    V = D("88119062784.573977477054291666666666666666666666667")
    sh = D("157239560.97379616666666666666666666666666666666667")
    c = gate_constants(V, sh)
    L = D(200).ln()
    ok(abs(c["thr"] - (L / LAMBDA + LAMBDA * V / 8)) == 0, "thr = L/lambda + lambda V/8")
    ok(abs(c["thr"] - (L * V / 2).sqrt()) / c["thr"] < D("1e-6"),
       "at the projected V the threshold is Hoeffding's sqrt(V ln(1/alpha) / 2)")
    ok(D("0.0030") < c["thr_per_share"] < D("0.0031"), "the projected threshold is 0.31 c a share")
    ok(D("0.97") < c["power"] < D("0.99"), "the projected power is 0.979")
    ok(reading(c["earn_at"], c)[0] == "EARN", "S at the EARN threshold reads EARN")
    ok(reading(c["earn_at"] - D("0.000001"), c)[0] == "UNDECIDABLE", "just below it does not")
    ok(reading(c["no_earn_at"], c)[0] == "NO EARN", "S at the NO EARN threshold reads NO EARN")
    ok(reading(c["no_earn_at"] + D("0.000001"), c)[0] == "UNDECIDABLE", "just above it does not")
    # the bound itself, by simulation under the least favourable null: every member's conditional
    # mean exactly 0, fair coins at the projected inventories; P(EARN) must be at most alpha
    import random
    rng = random.Random(23)
    xs = [D(rng.choice((3000, 4000, 5000, 6000))) for _ in range(2000)]
    Vs = sum(x * x for x in xs)
    cs = gate_constants(Vs, D(2000 * 40000))
    hits = 0
    for _ in range(400):
        S = sum(x * (1 if rng.random() < 0.5 else -1) / 2 for x in xs)
        hits += 1 if S >= cs["earn_at"] else 0
    ok(hits <= 2, "400 null runs at fair coins: %d read EARN, at most 2 expected at alpha 0.005" % hits)
    # the constants are label-free, and the score is not: two members, their labels flipped
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    try:
        cache = os.path.join(tmp, "cache")
        os.makedirs(cache)
        t0s = (1788530400, 1788530700)
        fills = {1788530400: [[1788530410, "B", "U", "120", "0.55"], [1788530500, "S", "D", "40", "0.3"]],
                 1788530700: [[1788530760, "B", "D", "75.5", "0.62"], [1788530650, "S", "U", "9", "0.5"]]}
        docs = [dict(good, slug="btc-updown-5m-%d" % t, eventStartTime=iso(t),
                     conditionId="0x%064x" % (i + 1)) for i, t in enumerate(t0s)]
        write_atomic(chunk_path(cache, t0s[0]), gz_bytes(dumps({"members": [
            {"t0": t, "condition": d["conditionId"], "rows": fills[t]} for t, d in zip(t0s, docs)]})))
        outs = []
        for k, prices in enumerate(('["1", "0"]', '["0", "1"]')):
            base = os.path.join(tmp, "b%d" % k)
            os.makedirs(base)
            st = {"start": t0s[0], "need": 2, "considered": [[t, "member"] for t in t0s],
                  "members": [{"t0": t, "doc": dict(kept_doc(d), outcomePrices=prices)}
                              for t, d in zip(t0s, docs)]}
            groups = [[(m["t0"], m["doc"]) for m in st["members"]]]
            const, paths = build_constants(base, st, cache, groups, "t")
            res = score(base, st, const, "t")
            with open(paths["constants.json"][0], "rb") as fh:
                outs.append((fh.read(), res["S"]))
        ok(outs[0][0] == outs[1][0], "the constants file is byte-identical with every label flipped")
        ok(outs[0][1] != outs[1][1], "the score moves when the labels flip (negative control)")
        # by hand: the window's X is -120 - 40 = -160 for the first member and +75.5 for the
        # second, whose Up sale at T0 - 50 is outside the window; S(Up) - S(Down) is their sum
        ok(outs[0][1] - outs[1][1] == D("-84.5"),
           "the score moves by the window's X, -160 + 75.5 = -84.5, by hand")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    # deterministic gzip and JSON
    ok(gz_bytes("abc\n") == gz_bytes("abc\n"), "gzip is deterministic")
    ok(dumps({"b": D("0.10"), "a": 1}) == '{"a":1,"b":"0.10"}\n', "JSON is sorted with Decimals as text")
    ok(fx(D("1E-7")) == "0.0000001", "no exponent form")
    # the audit hook
    try:
        open("/var/lib/btc-recorder/runtime.jsonl", "rb")
        refused = False
    except RuntimeError:
        refused = True
    except OSError:
        refused = False
    ok(refused and OPENS == ["/var/lib/btc-recorder/runtime.jsonl"],
       "an open under the recorder's root is refused before it happens")
    OPENS.clear()
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz23-maker-m0.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    table = {"selftest": mode_selftest, "still": mode_still, "rehearse": mode_rehearse,
             "fetch": mode_fetch, "constants": mode_constants, "rebate": mode_rebate,
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
    out("opens under the capture roots: %d" % len(OPENS))


if __name__ == "__main__":
    main(sys.argv[1:])
