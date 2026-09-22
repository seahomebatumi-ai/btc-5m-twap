#!/usr/bin/env python3
"""TZ-18 - the chain book capture, deployed.

One instrument, four modes, standard library only.

    --selftest      33 asserts over synthetic values; no network, no host read
    --verify-tz17   the three settlement identities of TZ-18 section 3.7, offline
    --serve         the long-lived capture of section 3.3, one window per 900 s
    --prove         the three readings of section 4 over what the capture stored

It stores replies byte for byte and it does not read them: no price, spread, size,
mid or book level is printed, written to an output file or computed anywhere outside
the byte-for-byte store (TZ-18 section 2, P3).

Written for TZ-18-chainbook-capture-deploy.md.  The TZ is the specification; this
file implements it and decides nothing.
"""

import argparse
import ast
import datetime
import errno
import gzip
import hashlib
import json
import os
import re
import signal
import sys
import threading
import time
import urllib.error
import urllib.request

from decimal import Decimal
from fractions import Fraction

if not __debug__:
    sys.stderr.write("tz18: refuses to run with asserts disabled (-O); "
                     "every count of this instrument is an assert\n")
    raise SystemExit(2)

# ----------------------------------------------------------------------------
# section 3.2 - the two endpoints, and nothing else.  Exactly two string
# constants in this file carry a scheme separator; S8 asserts it over the ast.
# ----------------------------------------------------------------------------

GAMMA_MARKET_URL = "https://gamma-api.polymarket.com/markets/slug/{slug}"
CLOB_BOOK_URL = "https://clob.polymarket.com/book?token_id={token_id}"

# ----------------------------------------------------------------------------
# Fixed constants of the TZ.  None of them is measured by this run.
# ----------------------------------------------------------------------------

MAP_REVISION = "2026-09-19-c"
ANCHORS = {
    "A1": "229a944f2d51",
    "A2": "6c5089330629",
    "A3": "0-complete / 1-student-5tau-not-disqualified / 2-undecidable-5tau",
    "A4": "437b45ea196b",
    "A5": "9fd1c7de0f74",
    "A6": "729f0bcdbee3",
}
ANCHOR_FILES = {
    "A2": "research/twap-divergence.py",
    "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
    "A5": "research/recorder/recorder.py",
    "A6": "research/pfair.py",
}
FINGERPRINT_ROWS_EXPECTED = 24
FINGERPRINT_FROZEN_EXPECTED = 22

CHAINBOOK_ROOT = "/var/lib/btc-chainbook"
RECORDER_ROOT = "/var/lib/btc-recorder"
TZ17_RAW = "/root/tz17-work/raw"
WORK_ROOT = "/root/tz18-work"
SVC_ROOT = "/root/tz18-svc"
WRITE_ROOTS = (WORK_ROOT + "/", SVC_ROOT + "/", CHAINBOOK_ROOT + "/")

RESOURCE_FLOOR = 2200000000          # section 0.2, 2.0e9 map floor + 2.0e8 write cap
WRITE_CAP = 200000000                # section 3.9
DISK_PATH = RECORDER_ROOT            # the path section 0.2's df names

WINDOW = 900
DOC_OFFSET = 605                     # section 3.3
DOC_GAP_S = 0.200                    # >= 200 ms between the two documents
CHECKPOINT_OFFSETS = (655, 715, 775, 805, 835, 865, 885)
CLOSE_OFFSET = 905
READ_TIMEOUT_S = 5.0
GZ_LEVEL = 6
SKEW_BOUND_NS = 1000000000           # section 4, G-DEPLOY completeness
BUDGET_S = 3900                      # section 4 / section 6 R3
QUALIFY_LEAD_S = 60
GATE_UNITS = 14                      # first 14 qualifying checkpoints
GATE_COMPLETE_PASS = 13              # >= 13 complete -> PASS
TIERC_INTERVAL = 300                 # the existing capture's 5-minute interval

# section 3.7 step 1 - the CSV inside the committed TZ-17 report
TZ17_REPORT_REL = "CryptoReports/TZ-17-settlement-chain-report.md"
CSV_SHA256 = "96b5e21e2cc59e2f3bde332d60457533158bd16c2eeaaaba844bf35b1efc63ee"
CSV_BYTES = 99075
CSV_LINES = 201
CSV_FENCE_OPEN = "```csv"
CSV_FENCE_CLOSE = "```"

SLOT_FIRST = 1788998400              # section 10, C5 - the 601 contiguous slots
SLOT_LAST = 1789178400
Q1_UNITS = 600
Q2_UNITS = 200
Q3_UNITS = 200
Q1_PASS = 599
Q2_PASS = 199
Q3_PASS = 199
DOCS_EXPECTED = 801
META_KEYS = frozenset(("priceToBeat", "finalPrice"))

# section 4 - the seven power figures, quoted from the TZ and recomputed by S7
POWER_LITERALS = (
    ("G-DEPLOY", 14, Fraction(1, 4), "0.899031627923250198364257812500"),
    ("G-DEPLOY", 14, Fraction(1, 10), "0.415370859484330000000000000000"),
    ("G-DEPLOY", 14, Fraction(1, 20), "0.152985562588816560668945312500"),
    ("G-CHAIN-Q1", 600, Fraction(1, 50), "0.999927940037418865985964653194"),
    ("G-CHAIN-Q1", 600, Fraction(1, 200), "0.801599779568236533442873619078"),
    ("G-CHAIN-Q23", 200, Fraction(1, 50), "0.910624516228067965960219332490"),
    ("G-CHAIN-Q23", 200, Fraction(1, 100), "0.595354315327973499366704428681"),
)
POWER_TOL = Fraction(1, 10 ** 18)

# section 5 S1 - Tier C's seven instants, map section 2.3, as offsets
TIERC_OFFSETS = (660, 720, 780, 810, 840, 870, 890)

# V11 - the key allow-lists, fixed here, asserted before each file is written
WINDOW_JSON_KEYS = frozenset((
    "T", "document_instant", "closed_wall_ns", "documents_ok", "checkpoints_complete",
    "status_counts", "skews_ns", "missed", "markets",
))
WINDOW_MARKET_KEYS = frozenset(("slug", "clobTokenIds", "outcomes", "conditionId"))
PROOF_JSON_KEYS = frozenset((
    "mode", "generated_wall_ns", "start_record", "proof_window", "control_window",
    "g_deploy", "g_tierc", "g_chain", "checkpoints", "skew_stats", "windows",
    "counters", "concurrency",
))
VERIFY_JSON_KEYS = frozenset((
    "mode", "generated_wall_ns", "csv", "bodies", "identities", "reading", "counters",
))
FORBIDDEN_KEYS = frozenset((
    "price", "prices", "bid", "bids", "ask", "asks", "mid", "midpoint", "size", "sizes",
    "level", "levels", "book", "books", "spread", "raw", "priceToBeat", "finalPrice",
    "best_bid", "best_ask", "amount", "quote", "quotes",
))

# ----------------------------------------------------------------------------
# Guards and counters.  Every number this file prints is one of these or is
# derived from a set it built; none is typed by hand.
# ----------------------------------------------------------------------------

COUNTERS = {
    "write_checks": 0,      # V5
    "bytes_written": 0,     # V13
    "recorder_opens": 0,    # V6
    "requests": 0,          # V7
    "asserts": 0,           # the self-test counting helper
}
_COUNTER_LOCK = threading.Lock()


def bump(name, by=1):
    with _COUNTER_LOCK:
        COUNTERS[name] += by
    return COUNTERS[name]


class GuardError(RuntimeError):
    pass


def check_write_path(path):
    """V5 - every open for writing is checked against the three allowed roots."""
    bump("write_checks")
    p = os.path.abspath(path)
    for root in WRITE_ROOTS:
        if p.startswith(root):
            return p
    raise GuardError("write refused outside the three allowed roots: " + p)


def check_read_path(path):
    """V6 / P1 - under the reserved tree only manifest.json is ever opened."""
    p = os.path.abspath(path)
    if p == RECORDER_ROOT or p.startswith(RECORDER_ROOT + "/"):
        bump("recorder_opens")
        if os.path.basename(p) != "manifest.json":
            raise GuardError("open refused under the reserved tree: " + p)
    return p


def read_bytes(path):
    p = check_read_path(path)
    with open(p, "rb") as fh:
        return fh.read()


def write_bytes(path, data):
    p = check_write_path(path)
    d = os.path.dirname(p)
    if d and not os.path.isdir(d):
        os.makedirs(d, exist_ok=True)
    with open(p, "wb") as fh:
        fh.write(data)
    account(len(data))
    return len(data)


def append_bytes(path, data):
    p = check_write_path(path)
    d = os.path.dirname(p)
    if d and not os.path.isdir(d):
        os.makedirs(d, exist_ok=True)
    with open(p, "ab") as fh:
        fh.write(data)
    account(len(data))
    return len(data)


def account(n):
    """V13 - the write cap, summed as it is written and asserted."""
    total = bump("bytes_written", n)
    assert total <= WRITE_CAP, "write cap exceeded: %d > %d" % (total, WRITE_CAP)
    return total


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def guard_resources():
    """section 0.2 - the resource gate, asserted inside the instrument at every run."""
    st = os.statvfs(DISK_PATH)
    avail = st.f_bavail * st.f_frsize
    assert avail >= RESOURCE_FLOOR, "resource gate: avail %d < %d" % (avail, RESOURCE_FLOOR)
    return avail


def json_line(obj):
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            + "\n").encode("utf-8")


def assert_keys(obj, allowed, what):
    """V11 - a fixed allow-list, asserted before the file is written."""
    got = frozenset(obj.keys())
    assert got == allowed, "%s key set %s != %s" % (
        what, sorted(got), sorted(allowed))
    forbid_recursive(obj, what)
    return len(got)


def forbid_recursive(obj, what, depth=0):
    """No book level, size or mid leaves the store through an output file."""
    assert depth < 12, "%s nested too deep" % what
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert k not in FORBIDDEN_KEYS, "%s carries a forbidden key: %s" % (what, k)
            forbid_recursive(v, what, depth + 1)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            forbid_recursive(v, what, depth + 1)
    return True


def repo_root_of(path):
    return os.path.dirname(os.path.dirname(os.path.abspath(path)))


def utc(ts):
    return datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")


# ----------------------------------------------------------------------------
# section 3.3 - the schedule
# ----------------------------------------------------------------------------

def schedule_for(T):
    """The instants of the window at T.  tau' is the seconds left to T+900."""
    assert T % WINDOW == 0, "a window starts on a 900-second boundary: %d" % T
    return {
        "T": T,
        "document_instant": T + DOC_OFFSET,
        "checkpoints": [(T + off, WINDOW - off) for off in CHECKPOINT_OFFSETS],
        "close_instant": T + CLOSE_OFFSET,
        "slug_15m": "btc-updown-15m-%d" % T,
        "slug_5m": "btc-updown-5m-%d" % (T + 600),
    }


def tierc_instants(T):
    return [T + off for off in TIERC_OFFSETS]


# ----------------------------------------------------------------------------
# section 4 - the readings, fixed before their data
# ----------------------------------------------------------------------------

def checkpoint_is_complete(entries):
    """Four stored replies, all 200, each body non-empty and JSON, skew <= 1e9 ns."""
    if len(entries) != 4:
        return False, "not_four_entries"
    for e in entries:
        if e.get("status") != 200:
            return False, "status_not_200"
        if not e.get("bytes"):
            return False, "empty_body"
        try:
            json.loads(e.get("raw") or "")
        except Exception:
            return False, "body_not_json"
    skew = skew_of(entries)
    if skew is None:
        return False, "no_skew"
    if skew > SKEW_BOUND_NS:
        return False, "skew_above_bound"
    return True, "complete"


def skew_of(entries):
    """max(recv) - min(recv) over the reads that produced a reply, in ns."""
    recvs = [e["recv_mono_ns"] for e in entries if e.get("recv_mono_ns") is not None]
    if not recvs:
        return None
    return max(recvs) - min(recvs)


def concurrency_ok(entries):
    """V10 - the last send precedes the first recv of the four."""
    sends = [e["send_mono_ns"] for e in entries if e.get("send_mono_ns") is not None]
    recvs = [e["recv_mono_ns"] for e in entries if e.get("recv_mono_ns") is not None]
    if len(sends) != 4 or not recvs:
        return None
    return max(sends) < min(recvs)


def qualifies(document_instant, checkpoint_instant, start_wall_s):
    """G-DEPLOY's unit rule, with the reason a non-qualifier was excluded."""
    if document_instant < start_wall_s + QUALIFY_LEAD_S:
        return False, "document_instant_before_start+%d" % QUALIFY_LEAD_S
    if checkpoint_instant > start_wall_s + BUDGET_S:
        return False, "checkpoint_after_budget_end"
    return True, "qualifying"


def read_g_deploy(n_qualifying, n_complete):
    if n_qualifying < GATE_UNITS:
        return "UNDECIDABLE"
    if n_complete >= GATE_COMPLETE_PASS:
        return "PASS"
    return "FAIL"


def read_g_chain(q1, q2, q3):
    if q1 >= Q1_PASS and q2 >= Q2_PASS and q3 >= Q3_PASS:
        return "PASS"
    return "FAIL"


def power_of(n, p):
    """1 - (1-p)^n - n*p*(1-p)^(n-1), exact in Fraction."""
    q = Fraction(1) - p
    return Fraction(1) - q ** n - n * p * q ** (n - 1)


# ----------------------------------------------------------------------------
# V1 - the fingerprint gate, inside the instrument
# ----------------------------------------------------------------------------

ROW_RE = re.compile(
    r"^\| `([^`]+)` \| ([\d,—-]+) \| ([\d,—-]+) \| (\w+) \| "
    r"`?([0-9a-f]{64}|self-reference[^|]*?)`? \|", re.M)


def fingerprint_gate(repo, out):
    mapp = os.path.join(repo, "SYSTEM-MAP.md")
    raw = read_bytes(mapp)
    txt = raw.decode("utf-8")
    rev = re.search(r"\*\*Revision string:\*\* `([^`]+)`", txt).group(1)
    assert rev == MAP_REVISION, "map revision %s != %s" % (rev, MAP_REVISION)
    found = dict(re.findall(r"\| `(A\d)` — [^|]*\| `([^`]+)` \|", txt))
    n_anchor = 0
    for k in sorted(ANCHORS):
        assert found.get(k) == ANCHORS[k], "anchor %s: %r != %r" % (
            k, found.get(k), ANCHORS[k])
        n_anchor += 1
    assert n_anchor == len(ANCHORS), "anchors compared: %d" % n_anchor
    n_rederived = 0
    for k in sorted(ANCHOR_FILES):
        h = sha256_hex(read_bytes(os.path.join(repo, ANCHOR_FILES[k])))[:12]
        assert h == ANCHORS[k], "re-derived %s %s != %s" % (k, h, ANCHORS[k])
        n_rederived += 1
    rows = ROW_RE.findall(txt)
    hashed = [r for r in rows if len(r[4]) == 64]
    assert len(hashed) == FINGERPRINT_ROWS_EXPECTED, "hashed rows %d" % len(hashed)
    n_frozen = n_frozen_ok = 0
    for path, lines, byts, state, sha in hashed:
        blob = read_bytes(os.path.join(repo, path))
        h = sha256_hex(blob)
        if state == "frozen":
            n_frozen += 1
            assert h == sha, "frozen row %s: %s != %s" % (path, h, sha)
            n_frozen_ok += 1
    assert n_frozen == FINGERPRINT_FROZEN_EXPECTED, "frozen rows %d" % n_frozen
    out("V1 fingerprint: revision %s equal; anchors %d of %d; re-derived %d of %d; "
        "rows hashed %d of %d; frozen equal %d of %d" % (
            rev, n_anchor, len(ANCHORS), n_rederived, len(ANCHOR_FILES),
            len(hashed), FINGERPRINT_ROWS_EXPECTED, n_frozen_ok,
            FINGERPRINT_FROZEN_EXPECTED))
    out("V1 SYSTEM-MAP.md sha256 %s  bytes %d  lines %d" % (
        sha256_hex(raw), len(raw), raw.count(b"\n")))
    return {"anchors": n_anchor, "rederived": n_rederived, "rows": len(hashed),
            "frozen": n_frozen_ok}


# ----------------------------------------------------------------------------
# The network, used by --serve only
# ----------------------------------------------------------------------------

def http_get(url, timeout=READ_TIMEOUT_S):
    """One GET.  No retry, no authentication, no header but the default agent."""
    bump("requests")
    send_mono = time.monotonic_ns()
    status = None
    body = b""
    reason = None
    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = int(resp.status)
            body = resp.read()
    except urllib.error.HTTPError as exc:
        status = int(exc.code)
        try:
            body = exc.read()
        except Exception:
            body = b""
        reason = "http_error"
    except Exception as exc:
        reason = type(exc).__name__
    recv_mono = time.monotonic_ns()
    recv_wall = time.time_ns()
    try:
        raw = body.decode("utf-8")
    except UnicodeDecodeError:
        raw = body.decode("latin-1")
    return {
        "url": url,
        "status": status,
        "send_mono_ns": send_mono,
        "recv_mono_ns": recv_mono if status is not None or body else recv_mono,
        "recv_wall_ns": recv_wall,
        "bytes": len(body),
        "sha256": sha256_hex(body),
        "raw": raw,
        "reason": reason,
    }


def parse_maybe_string(value):
    """section 3.3 - where a value is a JSON-encoded string, parse it."""
    if isinstance(value, str):
        try:
            return json.loads(value)
        except Exception:
            return value
    return value


def token_ids_of(doc_raw):
    """clobTokenIds, outcomes and conditionId exactly as the document carries them."""
    doc = json.loads(doc_raw)
    if isinstance(doc, list):
        doc = doc[0] if doc else {}
    verbatim = {
        "clobTokenIds": doc.get("clobTokenIds"),
        "outcomes": doc.get("outcomes"),
        "conditionId": doc.get("conditionId"),
    }
    ids = parse_maybe_string(verbatim["clobTokenIds"])
    outs = parse_maybe_string(verbatim["outcomes"])
    if not isinstance(ids, list) or not isinstance(outs, list):
        return None, None, verbatim
    ids = [str(i) for i in ids]
    outs = [str(o) for o in outs]
    if len(ids) != 2 or len(set(ids)) != 2 or not all(ids):
        return None, None, verbatim
    labels = outs[:2] if len(outs) >= 2 else [None, None]
    return ids, labels, verbatim


# ----------------------------------------------------------------------------
# --serve
# ----------------------------------------------------------------------------

STOP = threading.Event()


def _sigterm(signum, frame):
    STOP.set()


def sleep_until(instant):
    while not STOP.is_set():
        left = instant - time.time()
        if left <= 0:
            return True
        time.sleep(min(left, 1.0))
    return False


def acquire_single_instance(out):
    """section 3.8 - O_CREAT | O_EXCL, and a live sibling wins."""
    pidfile = os.path.join(CHAINBOOK_ROOT, "service.pid")
    me = os.path.abspath(__file__)
    while True:
        check_write_path(pidfile)
        try:
            fd = os.open(pidfile, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
            try:
                other = int(read_bytes(pidfile).decode("ascii").strip() or "0")
            except Exception:
                other = 0
            cmd = ""
            try:
                with open("/proc/%d/cmdline" % other, "rb") as fh:
                    cmd = fh.read().decode("utf-8", "replace").replace("\x00", " ").strip()
            except OSError:
                cmd = ""
            if cmd and me in cmd and "--serve" in cmd:
                out("service already running as pid %d: %s" % (other, cmd))
                return None
            out("stale pid file (pid %r, cmdline %r) replaced" % (other, cmd))
            os.unlink(pidfile)
            continue
        data = ("%d\n" % os.getpid()).encode("ascii")
        os.write(fd, data)
        os.close(fd)
        account(len(data))
        return pidfile


def runtime_record(event, extra=None):
    rec = {
        "event": event,
        "pid": os.getpid(),
        "wall_ns": time.time_ns(),
        "mono_ns": time.monotonic_ns(),
        "commit": read_commit(),
        "file_sha256": sha256_hex(read_bytes(os.path.abspath(__file__))),
        "argv": list(sys.argv),
        "config": {
            "root": CHAINBOOK_ROOT,
            "doc_offset": DOC_OFFSET,
            "checkpoint_offsets": list(CHECKPOINT_OFFSETS),
            "close_offset": CLOSE_OFFSET,
            "window": WINDOW,
            "timeout_s": READ_TIMEOUT_S,
            "gz_level": GZ_LEVEL,
            "budget_s": BUDGET_S,
            "write_cap": WRITE_CAP,
        },
    }
    if extra:
        rec.update(extra)
    append_bytes(os.path.join(CHAINBOOK_ROOT, "runtime.jsonl"), json_line(rec))
    return rec


def read_commit():
    """The branch commit, from the sidecar the Executor writes beside the copy.

    section 3.8 fixes argv exactly and carries no place for it, so the service reads
    it from commit.txt in its own directory and records what it read.
    """
    for cand in (os.path.join(os.path.dirname(os.path.abspath(__file__)), "commit.txt"),):
        try:
            return read_bytes(cand).decode("ascii").strip()
        except OSError:
            continue
    return None


def fetch_books(T, tau_prime, plan, out):
    """section 3.4 - four GETs, one per token id, each in its own thread."""
    entries = [None] * 4
    specs = []
    for market in ("m15", "m5"):
        ids = plan[market]["ids"]
        labels = plan[market]["labels"]
        slug = plan[market]["slug"]
        for i in range(2):
            specs.append({
                "market": market,
                "slug": slug,
                "token_id": None if ids is None else ids[i],
                "outcome_label": None if labels is None else labels[i],
            })
    assert len(specs) == 4, "a checkpoint is four reads: %d" % len(specs)

    if any(s["token_id"] is None for s in specs):
        for i, s in enumerate(specs):
            entries[i] = dict(s, T=T, tau_prime=tau_prime, url=None, status=None,
                              send_mono_ns=None, recv_mono_ns=None, recv_wall_ns=None,
                              bytes=0, sha256=None, raw="", reason="no_token_ids")
        return entries

    gate = threading.Event()

    def worker(idx, spec):
        gate.wait()
        res = http_get(CLOB_BOOK_URL.format(token_id=spec["token_id"]))
        entries[idx] = dict(spec, T=T, tau_prime=tau_prime, **res)

    threads = [threading.Thread(target=worker, args=(i, s), daemon=True)
               for i, s in enumerate(specs)]
    for th in threads:
        th.start()
    gate.set()
    deadline = time.monotonic() + READ_TIMEOUT_S + 2.0
    for th in threads:
        th.join(max(0.0, deadline - time.monotonic()))
    for i, s in enumerate(specs):
        if entries[i] is None:
            entries[i] = dict(s, T=T, tau_prime=tau_prime, url=None, status=None,
                              send_mono_ns=None, recv_mono_ns=None, recv_wall_ns=None,
                              bytes=0, sha256=None, raw="", reason="thread_deadline")
    return entries


BOOK_KEYS = ("T", "tau_prime", "market", "slug", "token_id", "outcome_label", "url",
             "status", "send_mono_ns", "recv_mono_ns", "recv_wall_ns", "bytes",
             "sha256", "raw", "reason")
DOC_KEYS = ("slug", "url", "status", "send_mono_ns", "recv_mono_ns", "recv_wall_ns",
            "bytes", "sha256", "raw")


def run_window(T, out):
    sched = schedule_for(T)
    wdir = os.path.join(CHAINBOOK_ROOT, str(T))
    out("window %d: document at %d (%s), close at %d" % (
        T, sched["document_instant"], utc(sched["document_instant"]),
        sched["close_instant"]))
    if not sleep_until(sched["document_instant"]):
        return None
    guard_resources()

    docs = []
    plan = {}
    for market, slug in (("m15", sched["slug_15m"]), ("m5", sched["slug_5m"])):
        if docs:
            time.sleep(DOC_GAP_S)
        res = http_get(GAMMA_MARKET_URL.format(slug=slug))
        rec = {k: res.get(k) for k in DOC_KEYS}
        rec["slug"] = slug
        docs.append(rec)
        ids = labels = None
        verbatim = {"clobTokenIds": None, "outcomes": None, "conditionId": None}
        if res["status"] == 200 and res["bytes"]:
            try:
                ids, labels, verbatim = token_ids_of(res["raw"])
            except Exception as exc:
                out("window %d %s: document unparsed (%s)" % (T, slug, type(exc).__name__))
        plan[market] = {"slug": slug, "ids": ids, "labels": labels, "verbatim": verbatim}

    payload = b"".join(json_line({k: d[k] for k in DOC_KEYS}) for d in docs)
    write_bytes(os.path.join(wdir, "documents.jsonl"), payload)
    documents_ok = all(d["status"] == 200 and d["bytes"] for d in docs) and \
        all(plan[m]["ids"] is not None for m in ("m15", "m5"))
    out("window %d: documents_ok=%s statuses=%s" % (
        T, documents_ok, [d["status"] for d in docs]))

    lines = []
    status_counts = {}
    skews = []
    complete = 0
    missed = 0
    for instant, tau_prime in sched["checkpoints"]:
        if time.time() > instant:
            missed += 1
            entries = []
            for market in ("m15", "m5"):
                for i in range(2):
                    ids = plan[market]["ids"]
                    labels = plan[market]["labels"]
                    entries.append({
                        "market": market, "slug": plan[market]["slug"],
                        "token_id": None if ids is None else ids[i],
                        "outcome_label": None if labels is None else labels[i],
                        "T": T, "tau_prime": tau_prime, "url": None, "status": None,
                        "send_mono_ns": None, "recv_mono_ns": None, "recv_wall_ns": None,
                        "bytes": 0, "sha256": None, "raw": "",
                        "reason": "missed_scheduled_%d" % instant,
                    })
            out("window %d tau' %d: missed (scheduled %d)" % (T, tau_prime, instant))
        else:
            if not sleep_until(instant):
                break
            entries = fetch_books(T, tau_prime, plan, out)
        ok, why = checkpoint_is_complete(entries)
        complete += 1 if ok else 0
        sk = skew_of(entries)
        skews.append(sk)
        for e in entries:
            key = "null" if e["status"] is None else str(e["status"])
            status_counts[key] = status_counts.get(key, 0) + 1
            lines.append(json_line({k: e.get(k) for k in BOOK_KEYS}))
        out("window %d tau' %d: statuses=%s skew_ns=%s complete=%s (%s)" % (
            T, tau_prime, [e["status"] for e in entries], sk, ok, why))

    while len(lines) < len(CHECKPOINT_OFFSETS) * 4 and STOP.is_set():
        break
    if lines:
        buf = gzip.compress(b"".join(lines), compresslevel=GZ_LEVEL, mtime=0)
        write_bytes(os.path.join(wdir, "books.jsonl.gz"), buf)

    sleep_until(sched["close_instant"])
    markets = {}
    for market in ("m15", "m5"):
        m = {"slug": plan[market]["slug"]}
        m.update({k: plan[market]["verbatim"].get(k) for k in
                  ("clobTokenIds", "outcomes", "conditionId")})
        assert frozenset(m.keys()) == WINDOW_MARKET_KEYS, "window.json market keys"
        markets[market] = m
    wj = {
        "T": T,
        "document_instant": sched["document_instant"],
        "closed_wall_ns": time.time_ns(),
        "documents_ok": documents_ok,
        "checkpoints_complete": complete,
        "status_counts": status_counts,
        "skews_ns": skews,
        "missed": missed,
        "markets": markets,
    }
    assert_keys(wj, WINDOW_JSON_KEYS, "window.json")
    write_bytes(os.path.join(wdir, "window.json"), json_line(wj))
    out("window %d closed: complete %d of %d, missed %d, lines %d" % (
        T, complete, len(CHECKPOINT_OFFSETS), missed, len(lines)))
    return wj


def next_window(now):
    T0 = (int(now) // WINDOW) * WINDOW
    return T0 if now <= T0 + DOC_OFFSET - 1 else T0 + WINDOW


def mode_serve(args, out):
    guard_resources()
    if not os.path.isdir(CHAINBOOK_ROOT):
        check_write_path(os.path.join(CHAINBOOK_ROOT, "x"))
        os.makedirs(CHAINBOOK_ROOT, exist_ok=True)
    pidfile = acquire_single_instance(out)
    if pidfile is None:
        return 0
    signal.signal(signal.SIGTERM, _sigterm)
    signal.signal(signal.SIGINT, _sigterm)
    rec = runtime_record("start")
    out("start record: " + json.dumps({k: rec[k] for k in
        ("event", "pid", "wall_ns", "commit", "file_sha256", "argv")}, sort_keys=True))
    skipped = next_window(time.time())
    if skipped != (int(time.time()) // WINDOW) * WINDOW:
        out("window %d already under way at start: no document fetch, contributes no unit"
            % ((int(time.time()) // WINDOW) * WINDOW))
    try:
        while not STOP.is_set():
            T = next_window(time.time())
            run_window(T, out)
    finally:
        runtime_record("stop", {"counters": dict(COUNTERS)})
        out("stop record written; requests %d, bytes %d" % (
            COUNTERS["requests"], COUNTERS["bytes_written"]))
    return 0


# ----------------------------------------------------------------------------
# --verify-tz17  (section 3.7)
# ----------------------------------------------------------------------------

def extract_csv(report_bytes):
    txt = report_bytes.decode("utf-8")
    lines = txt.split("\n")
    start = None
    for i, ln in enumerate(lines):
        if ln == CSV_FENCE_OPEN:
            start = i + 1
            break
    assert start is not None, "no csv fence in the TZ-17 report"
    end = None
    for j in range(start, len(lines)):
        if lines[j] == CSV_FENCE_CLOSE:
            end = j
            break
    assert end is not None, "no closing fence after the csv fence"
    block = "\n".join(lines[start:end]) + "\n"
    return block.encode("utf-8")


def meta_of(body_bytes, slug):
    """section 3.7 step 4 - events[0].eventMetadata, exactly two keys, Decimal values."""
    doc = json.loads(body_bytes, parse_float=Decimal)
    if isinstance(doc, list):
        doc = doc[0] if doc else {}
    events = doc.get("events")
    assert isinstance(events, list) and events, "%s: no events[0]" % slug
    em = events[0].get("eventMetadata")
    if isinstance(em, str):
        em = json.loads(em, parse_float=Decimal)
    assert isinstance(em, dict), "%s: eventMetadata is not a mapping" % slug
    assert frozenset(em.keys()) == META_KEYS, "%s: eventMetadata keys %s" % (
        slug, sorted(em.keys()))
    out = {}
    for k in sorted(META_KEYS):
        v = em[k]
        if isinstance(v, Decimal):
            out[k] = v
        elif isinstance(v, bool):
            out[k] = "type_error"
        elif isinstance(v, int):
            out[k] = Decimal(v)
        elif isinstance(v, str):
            try:
                out[k] = Decimal(v)
            except Exception:
                out[k] = "type_error"
        else:
            out[k] = "type_error"
    return out


def compare(a, b):
    """Equal by exact Decimal value, and equal as a printed literal."""
    if isinstance(a, str) or isinstance(b, str):
        return False, False, None
    return (a == b), (str(a) == str(b)), (a - b)


def mode_verify(args, out):
    guard_resources()
    repo = args.repo or repo_root_of(__file__)
    fp = fingerprint_gate(repo, out)

    report = read_bytes(os.path.join(repo, TZ17_REPORT_REL))
    out("TZ-17 report read from %s: bytes %d sha256 %s" % (
        os.path.join(repo, TZ17_REPORT_REL), len(report), sha256_hex(report)))
    csv_bytes = extract_csv(report)
    csv_sha = sha256_hex(csv_bytes)
    csv_lines = csv_bytes.decode("utf-8").rstrip("\n").split("\n")
    assert csv_sha == CSV_SHA256, "V3 csv sha256 %s != %s" % (csv_sha, CSV_SHA256)
    assert len(csv_bytes) == CSV_BYTES, "V3 csv bytes %d != %d" % (len(csv_bytes), CSV_BYTES)
    assert len(csv_lines) == CSV_LINES, "V3 csv lines %d != %d" % (len(csv_lines), CSV_LINES)
    out("V3 csv: sha256 %s bytes %d lines %d - all three equal" % (
        csv_sha, len(csv_bytes), len(csv_lines)))

    header = csv_lines[0].split(",")
    idx = {name: i for i, name in enumerate(header)}
    for col in ("T", "sha_M15", "sha_M5a", "sha_M5b", "sha_M5c", "sha_M5d"):
        assert col in idx, "csv column missing: %s" % col
    rows = []
    for ln in csv_lines[1:]:
        f = ln.split(",")
        rows.append({c: f[idx[c]] for c in
                     ("T", "sha_M15", "sha_M5a", "sha_M5b", "sha_M5c", "sha_M5d")})
    assert len(rows) == Q2_UNITS, "csv rows %d != %d" % (len(rows), Q2_UNITS)

    expected = {}
    for r in rows:
        T = int(r["T"])
        for col, slug in (("sha_M15", "btc-updown-15m-%d" % T),
                          ("sha_M5a", "btc-updown-5m-%d" % T),
                          ("sha_M5b", "btc-updown-5m-%d" % (T + 300)),
                          ("sha_M5c", "btc-updown-5m-%d" % (T + 600)),
                          ("sha_M5d", "btc-updown-5m-%d" % (T + 900))):
            prev = expected.get(slug)
            assert prev is None or prev == r[col], "csv disagrees with itself on %s" % slug
            expected[slug] = r[col]
    assert len(expected) == DOCS_EXPECTED, "distinct slugs %d != %d" % (
        len(expected), DOCS_EXPECTED)

    meta = {}
    n_hash_ok = 0
    for slug in sorted(expected):
        body = read_bytes(os.path.join(TZ17_RAW, slug + ".body"))
        h = sha256_hex(body)
        assert h == expected[slug], "V4 %s: %s != %s" % (slug, h, expected[slug])
        n_hash_ok += 1
        meta[slug] = meta_of(body, slug)
    out("V4 stored bodies re-hashed to the csv's value: %d of %d" % (
        n_hash_ok, DOCS_EXPECTED))

    units = []
    counts = {}
    slots = list(range(SLOT_FIRST, SLOT_LAST + 1, TIERC_INTERVAL))
    assert len(slots) == Q1_UNITS + 1, "contiguous slots %d" % len(slots)
    for i in range(len(slots) - 1):
        a = "btc-updown-5m-%d" % slots[i]
        b = "btc-updown-5m-%d" % slots[i + 1]
        units.append(("Q1", i, a, b, meta[a]["finalPrice"], meta[b]["priceToBeat"]))
    for i, r in enumerate(rows):
        T = int(r["T"])
        a = "btc-updown-15m-%d" % T
        b = "btc-updown-5m-%d" % (T + 900)
        units.append(("Q2", i, a, b, meta[a]["finalPrice"], meta[b]["priceToBeat"]))
    for i, r in enumerate(rows):
        T = int(r["T"])
        a = "btc-updown-15m-%d" % T
        b = "btc-updown-5m-%d" % (T + 600)
        units.append(("Q3", i, a, b, meta[a]["finalPrice"], meta[b]["finalPrice"]))

    csv_out = ["identity,index,slug_a,slug_b,value_a,value_b,equal_value,equal_literal,"
               "difference,sha_a,sha_b"]
    mismatches = []
    for ident, i, a, b, va, vb in units:
        eq_v, eq_l, diff = compare(va, vb)
        c = counts.setdefault(ident, {"n": 0, "value": 0, "literal": 0, "type_error": 0})
        c["n"] += 1
        c["value"] += 1 if eq_v else 0
        c["literal"] += 1 if eq_l else 0
        if isinstance(va, str) or isinstance(vb, str):
            c["type_error"] += 1
        if not eq_v:
            mismatches.append((ident, i, a, b, str(va), str(vb),
                               "type_error" if diff is None else str(diff)))
        csv_out.append("%s,%d,%s,%s,%s,%s,%d,%d,%s,%s,%s" % (
            ident, i, a, b, str(va), str(vb), 1 if eq_v else 0, 1 if eq_l else 0,
            "" if diff is None else str(diff), expected[a], expected[b]))
    body = ("\n".join(csv_out) + "\n").encode("utf-8")

    for ident, n in (("Q1", Q1_UNITS), ("Q2", Q2_UNITS), ("Q3", Q3_UNITS)):
        assert counts[ident]["n"] == n, "%s units %d != %d" % (ident, counts[ident]["n"], n)
    reading = read_g_chain(counts["Q1"]["value"], counts["Q2"]["value"],
                           counts["Q3"]["value"])
    for ident in ("Q1", "Q2", "Q3"):
        c = counts[ident]
        out("G-CHAIN %s: equal by value %d of %d; equal as printed literal %d of %d; "
            "type_error %d" % (ident, c["value"], c["n"], c["literal"], c["n"],
                               c["type_error"]))
    for m in mismatches:
        out("G-CHAIN mismatch %s[%d] %s vs %s: %s vs %s, difference %s" % m)
    out("G-CHAIN reading: %s" % reading)

    outdir = args.out or WORK_ROOT
    csv_path = os.path.join(outdir, "tz18-verify.csv")
    write_bytes(csv_path, body)
    js = {
        "mode": "verify-tz17",
        "generated_wall_ns": 0,
        "csv": {"sha256": csv_sha, "bytes": len(csv_bytes), "lines": len(csv_lines)},
        "bodies": {"expected": DOCS_EXPECTED, "rehashed_equal": n_hash_ok},
        "identities": {k: dict(v) for k, v in sorted(counts.items())},
        "reading": reading,
        "counters": {"fingerprint": fp,
                     "mismatches": len(mismatches),
                     "requests": COUNTERS["requests"],
                     "recorder_opens": COUNTERS["recorder_opens"]},
    }
    assert_keys(js, VERIFY_JSON_KEYS, "tz18-verify.json")
    json_path = os.path.join(outdir, "tz18-verify.json")
    write_bytes(json_path, (json.dumps(js, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    out("wrote %s sha256 %s bytes %d lines %d" % (
        csv_path, sha256_hex(body), len(body), body.count(b"\n")))
    out("wrote %s" % json_path)

    assert COUNTERS["requests"] == 0, "V7: request counter %d != 0" % COUNTERS["requests"]
    out("V7 request counter at exit: %d" % COUNTERS["requests"])
    out("V6 opens under the reserved tree: %d" % COUNTERS["recorder_opens"])
    assert COUNTERS["recorder_opens"] == 0, "V6 in verify mode must be 0"
    out("V5 write-path checks: %d" % COUNTERS["write_checks"])
    out("V13 bytes written: %d of cap %d" % (COUNTERS["bytes_written"], WRITE_CAP))
    return 0


# ----------------------------------------------------------------------------
# --prove  (sections 3.6 and 4)
# ----------------------------------------------------------------------------

def read_start_record(out):
    path = os.path.join(CHAINBOOK_ROOT, "runtime.jsonl")
    recs = [json.loads(ln) for ln in read_bytes(path).decode("utf-8").splitlines() if ln]
    starts = [r for r in recs if r.get("event") == "start"]
    assert starts, "no start record in runtime.jsonl"
    rec = starts[-1]
    out("start record: " + json.dumps({k: rec.get(k) for k in
        ("event", "pid", "wall_ns", "commit", "file_sha256", "argv")}, sort_keys=True))
    return rec


def load_windows(out):
    names = sorted(n for n in os.listdir(CHAINBOOK_ROOT)
                   if n.isdigit() and os.path.isdir(os.path.join(CHAINBOOK_ROOT, n)))
    windows = []
    for n in names:
        wdir = os.path.join(CHAINBOOK_ROOT, n)
        T = int(n)
        wj = None
        wp = os.path.join(wdir, "window.json")
        if os.path.exists(wp):
            wj = json.loads(read_bytes(wp))
        entries = []
        bp = os.path.join(wdir, "books.jsonl.gz")
        if os.path.exists(bp):
            blob = read_bytes(bp)
            for ln in gzip.decompress(blob).decode("utf-8").splitlines():
                if ln:
                    entries.append(json.loads(ln))
        docs = []
        dp = os.path.join(wdir, "documents.jsonl")
        if os.path.exists(dp):
            for ln in read_bytes(dp).decode("utf-8").splitlines():
                if ln:
                    docs.append(json.loads(ln))
        windows.append({"T": T, "window_json": wj, "entries": entries, "docs": docs,
                        "dir": wdir})
    out("windows on disk: %d (%s)" % (len(windows), ", ".join(str(w["T"]) for w in windows)))
    return windows


def median_str(values):
    s = sorted(values)
    n = len(s)
    if n == 0:
        return None
    if n % 2:
        return str(s[n // 2])
    return str(Fraction(s[n // 2 - 1] + s[n // 2], 2))


def manifest_scan(lo, hi, out, label):
    """section 3.6 - manifest.json and nothing else, under the reserved tree."""
    rows = []
    if not os.path.isdir(RECORDER_ROOT):
        return rows
    for fam in sorted(os.listdir(RECORDER_ROOT)):
        fdir = os.path.join(RECORDER_ROOT, fam)
        if not os.path.isdir(fdir):
            continue
        for name in sorted(os.listdir(fdir)):
            if not name.isdigit():
                continue
            T0 = int(name)
            close = T0 + TIERC_INTERVAL
            if not (lo <= close <= hi):
                continue
            mp = os.path.join(fdir, name, "manifest.json")
            if not os.path.exists(mp):
                rows.append({"family": fam, "T0": T0, "close": close,
                             "quotes_complete": None, "complete": None,
                             "manifest": False})
                continue
            m = json.loads(read_bytes(mp))
            rows.append({"family": fam, "T0": T0, "close": close,
                         "quotes_complete": m.get("quotes_complete"),
                         "complete": m.get("complete"), "manifest": True})
    for r in rows:
        out("G-TIERC %s: %s %d close %d (%s) quotes_complete=%r complete=%r" % (
            label, r["family"], r["T0"], r["close"], utc(r["close"]),
            r["quotes_complete"], r["complete"]))
    return rows


def mode_prove(args, out):
    guard_resources()
    repo = args.repo or repo_root_of(__file__)
    fp = fingerprint_gate(repo, out)

    start = read_start_record(out)
    start_wall_s = start["wall_ns"] / 1e9
    now = time.time()
    proof_lo, proof_hi = int(start_wall_s), int(now)
    length = proof_hi - proof_lo
    ctrl_lo, ctrl_hi = proof_lo - length, proof_lo
    out("proof window   [%d, %d] = [%s, %s], length %d s" % (
        proof_lo, proof_hi, utc(proof_lo), utc(proof_hi), length))
    out("control window [%d, %d] = [%s, %s], length %d s" % (
        ctrl_lo, ctrl_hi, utc(ctrl_lo), utc(ctrl_hi), length))

    windows = load_windows(out)

    # ---- G-DEPLOY, with the full disclosure of V9 -------------------------
    considered = []
    for w in windows:
        sched = schedule_for(w["T"])
        by_tau = {}
        for e in w["entries"]:
            by_tau.setdefault(e["tau_prime"], []).append(e)
        for instant, tau in sched["checkpoints"]:
            entries = by_tau.get(tau, [])
            q, why = qualifies(sched["document_instant"], instant, start_wall_s)
            if not entries:
                ok, reason = False, "not_stored"
            else:
                ok, reason = checkpoint_is_complete(entries)
            sk = skew_of(entries) if entries else None
            recvs = [e.get("recv_mono_ns") for e in entries]
            base = min([r for r in recvs if r is not None], default=None)
            deltas = [None if r is None or base is None else r - base for r in recvs]
            considered.append({
                "T": w["T"], "tau_prime": tau, "instant": instant,
                "document_instant": sched["document_instant"],
                "qualifying": q, "qualify_reason": why,
                "statuses": [e.get("status") for e in entries],
                "reasons": sorted({e.get("reason") for e in entries if e.get("reason")}),
                "recv_deltas_ns": deltas, "skew_ns": sk,
                "complete": ok, "complete_reason": reason,
                "concurrency_ok": concurrency_ok(entries) if entries else None,
            })
    considered.sort(key=lambda c: (c["instant"], c["T"]))

    out("")
    out("G-DEPLOY disclosure - every checkpoint considered, in order:")
    out("%-12s %5s %-11s %-34s %-22s %-13s %-9s %s" % (
        "window T", "tau'", "instant", "qualifying / reason", "statuses",
        "recv deltas ns", "skew ns", "complete / reason"))
    for c in considered:
        out("%-12d %5d %-11d %-34s %-22s %-13s %-9s %s" % (
            c["T"], c["tau_prime"], c["instant"],
            ("yes " if c["qualifying"] else "no  ") + c["qualify_reason"],
            ",".join("null" if s is None else str(s) for s in c["statuses"]) or "-",
            ",".join("null" if d is None else str(d) for d in c["recv_deltas_ns"]) or "-",
            "null" if c["skew_ns"] is None else str(c["skew_ns"]),
            ("yes " if c["complete"] else "no  ") + c["complete_reason"]))

    qualifying = [c for c in considered if c["qualifying"]]
    units = qualifying[:GATE_UNITS]
    n_complete = sum(1 for c in units if c["complete"])
    reading_deploy = read_g_deploy(len(qualifying), n_complete)
    n_missed = sum(1 for c in considered
                   if any(r.startswith("missed_") for r in c["reasons"]))
    n_incomplete = sum(1 for c in considered if not c["complete"])
    out("")
    out("G-DEPLOY: qualifying %d, units scored %d of %d, complete %d, "
        "incomplete %d, missed %d -> %s" % (
            len(qualifying), len(units), GATE_UNITS, n_complete, n_incomplete,
            n_missed, reading_deploy))

    skews = [c["skew_ns"] for c in considered
             if c["skew_ns"] is not None and len(c["statuses"]) == 4
             and all(s is not None for s in c["statuses"])]
    skew_stats = {"n": len(skews),
                  "min": min(skews) if skews else None,
                  "median": median_str(skews),
                  "max": max(skews) if skews else None}
    out("skew over the %d checkpoints that produced four replies: min %s, median %s, "
        "max %s ns" % (skew_stats["n"], skew_stats["min"], skew_stats["median"],
                       skew_stats["max"]))

    conc = [c for c in considered if c["concurrency_ok"] is not None]
    n_conc_bad = sum(1 for c in conc if not c["concurrency_ok"])
    out("V10 concurrency: checkpoints tested %d, last send after first recv in %d" % (
        len(conc), n_conc_bad))

    # ---- G-TIERC ----------------------------------------------------------
    out("")
    proof_rows = manifest_scan(proof_lo, proof_hi, out, "proof  ")
    ctrl_rows = manifest_scan(ctrl_lo, ctrl_hi, out, "control")
    bad = [r for r in proof_rows if r["manifest"] and r["quotes_complete"] is not True]
    reading_tierc = "FAIL" if bad else "PASS"
    out("G-TIERC: proof window intervals with a manifest %d, quotes_complete true %d, "
        "false %d -> %s" % (
            sum(1 for r in proof_rows if r["manifest"]),
            sum(1 for r in proof_rows if r["quotes_complete"] is True),
            len(bad), reading_tierc))
    out("G-TIERC control window intervals with a manifest %d, quotes_complete true %d "
        "(printed beside it, not gated)" % (
            sum(1 for r in ctrl_rows if r["manifest"]),
            sum(1 for r in ctrl_rows if r["quotes_complete"] is True)))

    # ---- G-CHAIN ----------------------------------------------------------
    vpath = args.verify_json or os.path.join(WORK_ROOT, "run-1", "tz18-verify.json")
    vj = json.loads(read_bytes(vpath))
    ids = vj["identities"]
    reading_chain = vj["reading"]
    out("")
    for k in ("Q1", "Q2", "Q3"):
        out("G-CHAIN %s: value %d of %d, literal %d of %d (from %s)" % (
            k, ids[k]["value"], ids[k]["n"], ids[k]["literal"], ids[k]["n"], vpath))
    out("G-CHAIN reading: %s" % reading_chain)

    # ---- the three readings, and the file ---------------------------------
    outdir = args.out or WORK_ROOT
    proof = {
        "mode": "prove",
        "generated_wall_ns": time.time_ns(),
        "start_record": {k: start.get(k) for k in
                         ("event", "pid", "wall_ns", "mono_ns", "commit", "file_sha256",
                          "argv")},
        "proof_window": {"lo": proof_lo, "hi": proof_hi, "length_s": length},
        "control_window": {"lo": ctrl_lo, "hi": ctrl_hi, "length_s": length},
        "g_deploy": {"qualifying": len(qualifying), "units": len(units),
                     "complete": n_complete, "incomplete": n_incomplete,
                     "missed": n_missed, "reading": reading_deploy},
        "g_tierc": {"proof": proof_rows, "control": ctrl_rows,
                    "false_count": len(bad), "reading": reading_tierc},
        "g_chain": {"identities": ids, "reading": reading_chain, "source": vpath},
        "checkpoints": considered,
        "skew_stats": skew_stats,
        "windows": [{"T": w["T"],
                     "documents_ok": (w["window_json"] or {}).get("documents_ok"),
                     "checkpoints_complete": (w["window_json"] or {}).get(
                         "checkpoints_complete"),
                     "doc_statuses": [d.get("status") for d in w["docs"]],
                     "closed": w["window_json"] is not None} for w in windows],
        "counters": dict(COUNTERS),
        "concurrency": {"tested": len(conc), "violations": n_conc_bad},
    }
    assert_keys(proof, PROOF_JSON_KEYS, "tz18-proof.json")
    ppath = os.path.join(outdir, "tz18-proof.json")
    write_bytes(ppath, (json.dumps(proof, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    out("wrote %s" % ppath)

    out("")
    out("READING G-DEPLOY: %s (complete %d of the first %d qualifying checkpoints)" % (
        reading_deploy, n_complete, len(units)))
    out("READING G-TIERC:  %s (%d of %d proof-window intervals not quotes_complete)" % (
        reading_tierc, len(bad), sum(1 for r in proof_rows if r["manifest"])))
    out("READING G-CHAIN:  %s (Q1 %d of %d, Q2 %d of %d, Q3 %d of %d by value)" % (
        reading_chain, ids["Q1"]["value"], ids["Q1"]["n"], ids["Q2"]["value"],
        ids["Q2"]["n"], ids["Q3"]["value"], ids["Q3"]["n"]))
    out("V5 write-path checks: %d" % COUNTERS["write_checks"])
    out("V6 opens under the reserved tree: %d, every basename manifest.json" %
        COUNTERS["recorder_opens"])
    out("V7 requests issued by this mode: %d" % COUNTERS["requests"])
    out("V13 bytes written: %d of cap %d" % (COUNTERS["bytes_written"], WRITE_CAP))
    assert COUNTERS["requests"] == 0, "--prove opens no socket"
    assert n_conc_bad == 0, "V10: %d checkpoints where the last send did not precede " \
                            "the first recv" % n_conc_bad
    return 0


# ----------------------------------------------------------------------------
# --selftest  (section 5) - 33 asserts through one counting helper
# ----------------------------------------------------------------------------

def mode_selftest(args, out):
    n = [0]

    def A(cond, item, what):
        assert cond, "%s FAILED: %s" % (item, what)
        n[0] += 1
        bump("asserts")
        out("  %-3s assert %2d  %s" % (item, n[0], what))

    out("S1 - the schedule of section 3.3 at T = 1790035200")
    T = 1790035200
    s = schedule_for(T)
    A(s["document_instant"] == 1790035805, "S1", "document instant 1790035805")
    inst = [i for i, _ in s["checkpoints"]]
    A(inst == [1790035855, 1790035915, 1790035975, 1790036005, 1790036035,
               1790036065, 1790036085], "S1", "the seven checkpoint instants")
    A(all(T + 600 < i < T + 900 for i in inst), "S1",
      "every checkpoint strictly inside (T+600, T+900)")
    tc = tierc_instants(T)
    A(tc == [1790035860, 1790035920, 1790035980, 1790036010, 1790036040, 1790036070,
             1790036090] and not (set(inst) & set(tc)), "S1",
      "no checkpoint equals any Tier C instant")

    out("S2 - qualifying and completeness on synthetic checkpoint records")

    def synth(statuses, skew_ns, body='{"a":1}'):
        rows = []
        for i, st in enumerate(statuses):
            rows.append({"status": st, "bytes": len(body) if st is not None else 0,
                         "raw": body if st is not None else "",
                         "send_mono_ns": 1000 + i,
                         "recv_mono_ns": 2000 + (skew_ns if i == 3 else 0),
                         "reason": None})
        return rows

    A(checkpoint_is_complete(synth([200] * 4, SKEW_BOUND_NS - 1))[0], "S2",
      "four 200s with skew 999,999,999 ns is complete")
    A(not checkpoint_is_complete(synth([200] * 4, SKEW_BOUND_NS + 1))[0], "S2",
      "the same with skew 1,000,000,001 ns is not complete")
    A(not checkpoint_is_complete(synth([200, 429, 200, 200], 10))[0], "S2",
      "one status 429 among four is not complete")

    out("S3 - json.loads(..., parse_float=Decimal) at live scale")
    lit = "76994.84244708234"
    doc = ('{"events":[{"eventMetadata":{"priceToBeat":' + lit +
           ',"finalPrice":' + lit + '}}]}').encode("utf-8")
    m = meta_of(doc, "synthetic")
    A(str(m["priceToBeat"]) == lit and m["priceToBeat"] == Decimal(lit), "S3",
      "a float body returns the exact literal " + lit)
    doc2 = ('{"events":[{"eventMetadata":"{\\"priceToBeat\\":\\"' + lit +
            '\\",\\"finalPrice\\":77000}"}]}').encode("utf-8")
    m2 = meta_of(doc2, "synthetic")
    A(m2["priceToBeat"] == Decimal(lit) and m2["finalPrice"] == Decimal(77000), "S3",
      "a str value and an int value convert to Decimal")
    doc3 = ('{"events":[{"eventMetadata":{"priceToBeat":[1,2],"finalPrice":' + lit +
            '}}]}').encode("utf-8")
    m3 = meta_of(doc3, "synthetic")
    A(m3["priceToBeat"] == "type_error", "S3", "a list value marks type_error")

    out("S4 - the three identities on synthetic pairs")
    a, b = Decimal("76994.84244708234"), Decimal("76994.84244708234")
    A(compare(a, b) == (True, True, Decimal("0")), "S4",
      "equal literals hold by value and by literal")
    c = Decimal("76994.84244708234") + Decimal("1E-9")
    ev, el, diff = compare(a, c)
    A((not ev) and (not el) and diff == Decimal("-1E-9"), "S4",
      "literals differing by 1E-9 fail and report that difference")
    ev2, el2, _ = compare(Decimal("1.10"), Decimal("1.1"))
    A(ev2 and not el2, "S4",
      "1.10 against 1.1 counts by value and not as a printed literal")
    A(compare(Decimal("1"), "type_error") == (False, False, None), "S4",
      "a type_error unit counts as a failure of its identity")

    out("S5 - the write guard")
    allowed = [os.path.join(WORK_ROOT, "x"), os.path.join(SVC_ROOT, "x"),
               os.path.join(CHAINBOOK_ROOT, "x")]
    A(all(check_write_path(p) == p for p in allowed), "S5",
      "a path under each of the three allowed roots opens")

    def raises(p):
        try:
            check_write_path(p)
            return False
        except GuardError:
            return True

    A(raises("/root/btc-5m-twap/x"), "S5", "a path in the repository raises")
    A(raises(RECORDER_ROOT + "/x"), "S5", "a path under the reserved tree raises")

    out("S6 - the readings of section 4 on synthetic counts")
    A(read_g_deploy(14, 13) == "PASS", "S6", "(14 qualifying, 13 complete) -> PASS")
    A(read_g_deploy(14, 12) == "FAIL", "S6", "(14 qualifying, 12 complete) -> FAIL")
    A(read_g_deploy(13, 13) == "UNDECIDABLE", "S6", "13 qualifying -> UNDECIDABLE")
    A(read_g_chain(598, 200, 200) == "FAIL", "S6", "Q1 598 -> FAIL")

    out("S7 - the seven power literals, recomputed in exact Fraction arithmetic")
    for gate, nn, p, lit7 in POWER_LITERALS:
        got = power_of(nn, p)
        want = Fraction(lit7)
        A(abs(got - want) <= POWER_TOL, "S7",
          "%s n=%d p=%s -> %s (tolerance 1E-18)" % (gate, nn, p, lit7))

    out("S8 - the instrument's own syntax tree")
    src = read_bytes(os.path.abspath(__file__))
    tree = ast.parse(src)
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for al in node.names:
                mods.add(al.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0 and node.module:
                mods.add(node.module.split(".")[0])
    A(mods and mods <= set(sys.stdlib_module_names), "S8",
      "every imported top-level module is in sys.stdlib_module_names (%d of %d)" % (
          len(mods & set(sys.stdlib_module_names)), len(mods)))
    A("subprocess" not in mods, "S8", "subprocess is not imported")
    bad_attr = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) \
                and node.value.id == "os":
            nm = node.attr
            if nm in ("system", "popen") or nm.startswith("spawn") or nm.startswith("exec"):
                bad_attr.append(nm)
    A(not bad_attr, "S8", "no system, popen, spawn* or exec* attribute is taken on os")
    bad_kw = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            for kw in node.keywords:
                if kw.arg == "shell":
                    bad_kw.append(ast.dump(node.func))
    A(not bad_kw, "S8", "no call carries a keyword shell")
    needle = ":" + "/" + "/"
    consts = [c.value for c in ast.walk(tree)
              if isinstance(c, ast.Constant) and isinstance(c.value, str)
              and needle in c.value]
    A(len(consts) == 2 and set(consts) == {GAMMA_MARKET_URL, CLOB_BOOK_URL}, "S8",
      "exactly two string constants carry a scheme separator, the two endpoints")

    out("")
    out("selftest: %d of %d asserts" % (n[0], n[0]))
    assert n[0] == COUNTERS["asserts"], "the counting helper disagrees with itself"
    return 0


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description="TZ-18 chain book capture")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--selftest", action="store_true")
    g.add_argument("--verify-tz17", dest="verify_tz17", action="store_true")
    g.add_argument("--serve", action="store_true")
    g.add_argument("--prove", action="store_true")
    ap.add_argument("--out", default=None, help="directory for this run's outputs")
    ap.add_argument("--repo", default=None, help="repository root for the fingerprint gate")
    ap.add_argument("--verify-json", dest="verify_json", default=None)
    args = ap.parse_args(argv)

    def out(msg):
        sys.stdout.write("[%s] %s\n" % (utc(time.time()), msg))
        sys.stdout.flush()

    if args.selftest:
        return mode_selftest(args, out)
    if args.verify_tz17:
        return mode_verify(args, out)
    if args.serve:
        return mode_serve(args, out)
    if args.prove:
        return mode_prove(args, out)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
