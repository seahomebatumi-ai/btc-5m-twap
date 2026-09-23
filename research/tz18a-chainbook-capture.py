#!/usr/bin/env python3
"""TZ-18a - the chain book capture, redeployed.

One instrument, four modes, standard library only.

    --selftest      39 asserts over synthetic values; the socket reaches 127.0.0.1 only
    --prestart      the request path proved on this host before the service starts
    --serve         the long-lived capture of section 3.5, one window per 900 s
    --prove         the two readings of section 4 over what the capture stored

It stores replies byte for byte and it does not read them: no price, spread, size,
mid or book level is printed, written to an output file or computed anywhere outside
the byte-for-byte store (TZ-18a section 2, P3).

Written for TZ-18a-chainbook-capture-redeploy.md.  The TZ is the specification; this
file implements it and decides nothing.
"""

import argparse
import ast
import datetime
import errno
import gzip
import hashlib
import http.server
import json
import os
import re
import signal
import sys
import threading
import time
import urllib.error
import urllib.request

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

MAP_REVISION = "2026-09-23-a"
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
FINGERPRINT_ROWS_EXPECTED = 25
FINGERPRINT_FROZEN_EXPECTED = 23

CHAINBOOK_ROOT = "/var/lib/btc-chainbook"
RECORDER_ROOT = "/var/lib/btc-recorder"
WORK_ROOT = "/root/tz18a-work"
SVC_ROOT = "/root/tz18a-svc"
WRITE_ROOTS = (WORK_ROOT + "/", SVC_ROOT + "/", CHAINBOOK_ROOT + "/")

RESOURCE_FLOOR = 2200000000          # section 0.2, 2.0e9 map floor + 2.0e8 write cap
WRITE_CAP = 200000000                # section 3.9
DISK_PATH = RECORDER_ROOT            # the path section 0.2's df names

WINDOW = 900
DOC_OFFSET = 625                     # section 1 item 1 - 20 s after the recorder's S6
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

# section 3.2 and section 3.5 - the request this instrument sends, the service's
# exact argv, and the figures section 4 fixes before any of their data exists.
ACCEPT = "application/json"
USER_AGENT = "btc-5m-twap-tz18a"
SERVICE_ARGV = ("/root/tz01-env/venv/bin/python", "-B", "-u",
                SVC_ROOT + "/tz18a-chainbook-capture.py", "--serve")
OLD_SERVICE_ARGV = ("/root/tz01-env/venv/bin/python", "-B", "-u",
                    "/root/tz18-svc/tz18-chainbook-capture.py", "--serve")
REQUESTS_PER_WINDOW = 30             # 2 + 4 x 7, section 3.7
TIERC_MIN_FULL = 2                   # section 4, G-TIERC's PASS minimum
CLOSE_MARGIN_S = 5                   # section 3.6, considered()
BASE_RATE_S = 604800                 # section 3.4 step 3, the week before R1
FA_UNITS = 5                         # section 4, the most windows a proof can consider

# section 4 - the three power figures, quoted from the TZ and recomputed by S7
POWER_LITERALS = (
    ("G-DEPLOY", 14, Fraction(1, 4), "0.899031627923250198364257812500"),
    ("G-DEPLOY", 14, Fraction(1, 10), "0.415370859484330000000000000000"),
    ("G-DEPLOY", 14, Fraction(1, 20), "0.152985562588816560668945312500"),
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
    "mode", "as_of", "start_record", "proof_window", "control_window",
    "g_deploy", "g_tierc", "checkpoints", "skew_stats", "windows",
    "counters", "concurrency",
))
PRESTART_JSON_KEYS = frozenset((
    "mode", "p_wall", "file_sha256", "fingerprint", "processes", "base_rate",
    "requests", "counters",
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

def build_request(url):
    """section 3.2 - the one builder of every request this instrument sends.

    Under Python 3.12.3 the wire block is exactly five fields, none repeated:
    Accept-Encoding identity from http.client, Host and Connection close from
    urllib, and the two set here.  TZ-18 sent Python's default agent and was
    refused 403, error code 1010, at every request (map section 7 item 77).
    """
    return urllib.request.Request(
        url, method="GET", headers={"Accept": ACCEPT, "User-Agent": USER_AGENT})


def http_get(url, timeout=READ_TIMEOUT_S):
    """One GET through build_request.  No retry, no authentication, no credential.

    Both receive stamps are taken only where a status was obtained; where none
    was, each is None.  TZ-18 returned the same value on both branches.
    """
    bump("requests")
    send_mono = time.monotonic_ns()
    status = None
    body = b""
    reason = None
    try:
        req = build_request(url)
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
    if status is None:
        recv_mono = None
        recv_wall = None
    try:
        raw = body.decode("utf-8")
    except UnicodeDecodeError:
        raw = body.decode("latin-1")
    return {
        "url": url,
        "status": status,
        "send_mono_ns": send_mono,
        "recv_mono_ns": recv_mono,
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


def same_service(cmdline_bytes, argv):
    """Equality with the exact argv, never a substring (map section 7 item 76).

    The bytes are split on NUL, the one trailing empty field is dropped, each
    field is decoded as UTF-8, and the result must equal argv element for element.
    """
    fields = cmdline_bytes.split(b"\x00")
    if fields and fields[-1] == b"":
        fields = fields[:-1]
    try:
        decoded = [f.decode("utf-8") for f in fields]
    except UnicodeDecodeError:
        return False
    if len(decoded) != len(argv):
        return False
    return all(a == b for a, b in zip(decoded, argv))


def acquire_single_instance(out):
    """section 3.8 - O_CREAT | O_EXCL, and a live sibling wins.

    The sibling is identified by equality with SERVICE_ARGV or with TZ-18's
    OLD_SERVICE_ARGV; anything else makes the pid file stale.
    """
    pidfile = os.path.join(CHAINBOOK_ROOT, "service.pid")
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
            cmd = b""
            try:
                with open("/proc/%d/cmdline" % other, "rb") as fh:
                    cmd = fh.read()
            except OSError:
                cmd = b""
            live = None
            for argv, which in ((SERVICE_ARGV, "SERVICE_ARGV"),
                                (OLD_SERVICE_ARGV, "OLD_SERVICE_ARGV")):
                if same_service(cmd, argv):
                    live = which
                    break
            if live is not None:
                out("service already running as pid %d, argv equal to %s: %s"
                    % (other, live, " ".join(argv)))
                return None
            out("stale pid file (pid %r, cmdline %r) replaced"
                % (other, cmd.decode("utf-8", "replace").replace("\x00", " ")))
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
            "headers": [["Accept", ACCEPT], ["User-Agent", USER_AGENT]],
            "service_argv": list(SERVICE_ARGV),
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
    try:
        with open("/proc/self/cmdline", "rb") as fh:
            mine = fh.read()
    except OSError:
        mine = b""
    if not same_service(mine, SERVICE_ARGV):
        out("D10 refuses to serve: /proc/self/cmdline %r is not SERVICE_ARGV %r; "
            "nothing written" % (mine.decode("utf-8", "replace").replace("\x00", " "),
                                 list(SERVICE_ARGV)))
        return 2
    guard_resources()
    if not os.path.isdir(CHAINBOOK_ROOT):
        check_write_path(os.path.join(CHAINBOOK_ROOT, "x"))
        os.makedirs(CHAINBOOK_ROOT, exist_ok=True)
    pidfile = acquire_single_instance(out)
    if pidfile is None:
        return 3
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
# --prestart  (section 3.4) - the request path, proved on this host before the
# service starts.  CANON hard rule 14's precondition.
# ----------------------------------------------------------------------------

def base_rate(p, span_s=BASE_RATE_S, step=TIERC_INTERVAL):
    """The T0 of every five-minute interval closing in [p - span_s, p).

    The last slot is p - 2 * step, whose close is p - step; p - step itself is
    excluded because its close is p, which the half-open window does not hold.
    """
    return list(range(p - span_s - step, p - step, step))


def p_false_alarm(f, m, units):
    """G-TIERC's false-failure probability, 1 - (1 - f/m)^units, exact; None at m=0."""
    if m == 0:
        return None
    return Fraction(1) - (Fraction(1) - Fraction(f, m)) ** units


def decimals_of(fr, places=10):
    """A Fraction rendered to a fixed number of decimals, half up, in integers."""
    if fr is None:
        return None
    scale = 10 ** places
    q, r = divmod(fr.numerator * scale, fr.denominator)
    if 2 * r >= fr.denominator:
        q += 1
    sign = "-" if q < 0 else ""
    s = str(abs(q)).rjust(places + 1, "0")
    return sign + s[:-places] + "." + s[-places:]


def parses_json(raw):
    """Whether a body parses as JSON.  Nothing is taken from what it parsed to."""
    try:
        json.loads(raw)
        return True
    except Exception:
        return False


def mode_prestart(args, out):
    guard_resources()
    repo = args.repo or repo_root_of(__file__)
    fp = fingerprint_gate(repo, out)
    me = os.path.abspath(__file__)
    my_sha = sha256_hex(read_bytes(me))
    out("instrument: %s sha256 %s" % (me, my_sha))

    # ---- step 2 - every /proc/{pid}/cmdline, by equality with the argv ----
    n_pids = n_gone = 0
    hits = {"service_argv": [], "old_service_argv": []}
    for name in sorted(os.listdir("/proc")):
        if not name.isdigit():
            continue
        n_pids += 1
        try:
            with open("/proc/%s/cmdline" % name, "rb") as fh:
                cmd = fh.read()
        except OSError:
            n_gone += 1
            continue
        if same_service(cmd, SERVICE_ARGV):
            hits["service_argv"].append(int(name))
        if same_service(cmd, OLD_SERVICE_ARGV):
            hits["old_service_argv"].append(int(name))
    processes = {"pids_scanned": n_pids, "vanished_mid_scan": n_gone,
                 "service_argv": hits["service_argv"],
                 "old_service_argv": hits["old_service_argv"]}
    out("processes: %d pids read, %d vanished mid-scan; equal to SERVICE_ARGV %d, "
        "to OLD_SERVICE_ARGV %d" % (n_pids, n_gone, len(hits["service_argv"]),
                                    len(hits["old_service_argv"])))
    assert not hits["service_argv"], \
        "a process already runs this service: %r" % hits["service_argv"]
    assert not hits["old_service_argv"], \
        "TZ-18's service still runs: %r" % hits["old_service_argv"]

    # ---- step 3 - the base rate, stated before any interval it judges exists --
    p = int(time.time()) // TIERC_INTERVAL * TIERC_INTERVAL
    slots = base_rate(p)
    assert len(slots) == BASE_RATE_S // TIERC_INTERVAL, \
        "base-rate slots %d" % len(slots)
    fam = os.path.join(RECORDER_ROOT, "btc-updown-5m")
    n_dirs = m = f = n_open = 0
    t0_scan = time.monotonic()
    for T0 in slots:
        d = os.path.join(fam, str(T0))
        if not os.path.isdir(d):
            continue
        n_dirs += 1
        mp = os.path.join(d, "manifest.json")
        if not os.path.exists(mp):
            continue
        blob = read_bytes(mp)
        n_open += 1
        if n_open == 100:
            spent = time.monotonic() - t0_scan
            assert spent <= 30.0, \
                "section 10 C4 fail-fast: the first 100 opens took %.3f s" % spent
        m += 1
        if json.loads(blob).get("quotes_complete") is not True:
            f += 1
    fa = p_false_alarm(f, m, FA_UNITS)
    base = {"p_wall": p, "span_s": BASE_RATE_S, "slots": len(slots),
            "directories": n_dirs, "manifests": m, "not_quotes_complete": f,
            "units": FA_UNITS,
            "p_false_alarm": None if fa is None else str(fa),
            "p_false_alarm_decimals": decimals_of(fa)}
    out("base rate: p %d (%s), slots %d, directories %d, manifests m=%d, "
        "not quotes_complete f=%d" % (p, utc(p), len(slots), n_dirs, m, f))
    out("G-TIERC false-failure probability 1 - (1 - f/m)^%d = %s = %s"
        % (FA_UNITS, base["p_false_alarm"], base["p_false_alarm_decimals"]))

    # ---- step 4 - a fifteen-minute market that is open, so not settled ----
    Tstar = int(time.time()) // WINDOW * WINDOW
    age = time.time() - Tstar
    if age < 30:
        out("live window %d is %.1f s old: waiting to %d" % (Tstar, age, Tstar + 30))
        sleep_until(Tstar + 30)
    elif age > 840:
        out("live window %d is %.1f s old: waiting to %d and taking %d"
            % (Tstar, age, Tstar + WINDOW + 30, Tstar + WINDOW))
        sleep_until(Tstar + WINDOW + 30)
        Tstar = Tstar + WINDOW
    slug = "btc-updown-15m-%d" % Tstar
    out("live fifteen-minute market %s at %d (%s); it closes at %d"
        % (slug, int(time.time()), utc(time.time()), Tstar + WINDOW))

    # ---- steps 5 and 6 - the two requests --------------------------------
    requests = []

    def record(res, extra=None):
        ent = {
            "method": "GET",
            "url": res["url"],
            "headers": [["Accept", ACCEPT], ["User-Agent", USER_AGENT]],
            "status": res["status"],
            "bytes": res["bytes"],
            "sha256": res["sha256"],
            "parses_json": parses_json(res["raw"]),
            "recv_wall_ns": res["recv_wall_ns"],
            "elapsed_ns": (None if res["recv_mono_ns"] is None
                           else res["recv_mono_ns"] - res["send_mono_ns"]),
        }
        if extra:
            ent.update(extra)
        requests.append(ent)
        out("request %d: GET %s -> status %r, bytes %d, sha256 %s, parses_json %r, "
            "elapsed_ns %r, recv_wall_ns %r"
            % (len(requests), ent["url"], ent["status"], ent["bytes"], ent["sha256"],
               ent["parses_json"], ent["elapsed_ns"], ent["recv_wall_ns"]))
        return ent

    r1 = http_get(GAMMA_MARKET_URL.format(slug=slug))
    ids = None
    if r1["status"] == 200 and r1["bytes"]:
        ids = token_ids_of(r1["raw"])[0]
    e1 = record(r1, {"token_ids": ids})
    assert e1["status"] == 200, "P-START request 1 status %r" % e1["status"]
    assert e1["bytes"] > 0, "P-START request 1 returned no bytes"
    assert e1["parses_json"], "P-START request 1 body does not parse as JSON"
    assert ids is not None and len(ids) == 2 and len(set(ids)) == 2 and all(ids), \
        "P-START request 1 yielded no two distinct non-empty token ids"
    out("token ids: %s and %s" % (ids[0], ids[1]))

    r2 = http_get(CLOB_BOOK_URL.format(token_id=ids[0]))
    e2 = record(r2)
    assert e2["status"] == 200, "P-START request 2 status %r" % e2["status"]
    assert e2["bytes"] > 0, "P-START request 2 returned no bytes"
    assert e2["parses_json"], "P-START request 2 body does not parse as JSON"

    # ---- step 7 - the output file ---------------------------------------
    assert COUNTERS["requests"] == 2, \
        "V7: --prestart issued %d requests" % COUNTERS["requests"]
    outdir = args.out or WORK_ROOT
    js = {
        "mode": "prestart",
        "p_wall": p,
        "file_sha256": my_sha,
        "fingerprint": fp,
        "processes": processes,
        "base_rate": base,
        "requests": requests,
        "counters": dict(COUNTERS),
    }
    assert_keys(js, PRESTART_JSON_KEYS, "tz18a-prestart.json")
    body = (json.dumps(js, indent=2, sort_keys=True) + "\n").encode("utf-8")
    jpath = os.path.join(outdir, "tz18a-prestart.json")
    write_bytes(jpath, body)
    out("wrote %s sha256 %s bytes %d lines %d"
        % (jpath, sha256_hex(body), len(body), body.count(b"\n")))
    out("V5 write-path checks: %d" % COUNTERS["write_checks"])
    out("V6 opens under the reserved tree: %d, every basename manifest.json"
        % COUNTERS["recorder_opens"])
    out("V7 requests issued by this mode: %d" % COUNTERS["requests"])
    out("V13 bytes written: %d of cap %d" % (COUNTERS["bytes_written"], WRITE_CAP))
    out("READING P-START: served")
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


def considered(T, s, A):
    """D11 - the window at T is considered iff its document instant falls at or
    after the service's start instant s, and its close plus the margin at or
    before the as-of instant A, so that its three files no longer change."""
    return T + DOC_OFFSET >= s and T + CLOSE_OFFSET + CLOSE_MARGIN_S <= A


def load_windows(s, A, out):
    names = sorted(n for n in os.listdir(CHAINBOOK_ROOT)
                   if n.isdigit() and os.path.isdir(os.path.join(CHAINBOOK_ROOT, n)))
    windows = []
    skipped = []
    for n in names:
        T = int(n)
        if not considered(T, s, A):
            skipped.append(T)
            continue
        wdir = os.path.join(CHAINBOOK_ROOT, n)
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
        stored = {}
        for fn in ("documents.jsonl", "books.jsonl.gz", "window.json"):
            try:
                stored[fn] = os.stat(os.path.join(wdir, fn)).st_size
            except OSError:
                stored[fn] = None
        windows.append({"T": T, "window_json": wj, "entries": entries, "docs": docs,
                        "dir": wdir, "stored_bytes": stored})
    out("window directories on disk: %d; considered %d (%s)" % (
        len(names), len(windows), ", ".join(str(w["T"]) for w in windows) or "-"))
    out("window directories not considered: %d (%s)" % (
        len(skipped), ", ".join(str(t) for t in skipped) or "-"))
    return windows


def median_str(values):
    s = sorted(values)
    n = len(s)
    if n == 0:
        return None
    if n % 2:
        return str(s[n // 2])
    return str(Fraction(s[n // 2 - 1] + s[n // 2], 2))


def manifest_scan(lo, hi, A, out, label):
    """section 3.6 - manifest.json and nothing else, under the reserved tree.

    A manifest counts only if it exists with st_mtime_ns <= A * 10**9, so two
    runs with one A read the same files.  os.stat opens nothing.
    """
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
            try:
                counted = os.stat(mp).st_mtime_ns <= A * 10 ** 9
            except OSError:
                counted = False
            if not counted:
                rows.append({"family": fam, "T0": T0, "close": close,
                             "quotes_complete": None, "complete": None,
                             "manifest": False, "reason": "no_manifest_by_as_of"})
                continue
            m = json.loads(read_bytes(mp))
            rows.append({"family": fam, "T0": T0, "close": close,
                         "quotes_complete": m.get("quotes_complete"),
                         "complete": m.get("complete"),
                         "manifest": True, "reason": None})
    for r in rows:
        out("G-TIERC %s: %s %d close %d (%s) counted=%r quotes_complete=%r "
            "complete=%r%s" % (
                label, r["family"], r["T0"], r["close"], utc(r["close"]),
                r["manifest"], r["quotes_complete"], r["complete"],
                "" if r["reason"] is None else " (" + r["reason"] + ")"))
    return rows


def issued_of(doc_lines, book_entries):
    """section 3.6 - how many of a window's 30 requests carry a send stamp.

    A read still running at its thread's deadline is stored with a null send
    stamp, so this count can understate the load and never overstate it.
    """
    n = 0
    for d in doc_lines:
        if d.get("send_mono_ns") is not None:
            n += 1
    for e in book_entries:
        if e.get("send_mono_ns") is not None:
            n += 1
    return n


def read_g_tierc(rows):
    """section 4 - one row per considered window: issued, counted, quotes_complete."""
    exposed = [r for r in rows if r["issued"] >= 1]
    counted = [r for r in exposed if r["counted"]]
    if any(r["quotes_complete"] is not True for r in counted):
        return "FAIL"
    full = [r for r in counted if r["issued"] == REQUESTS_PER_WINDOW]
    if len(full) >= TIERC_MIN_FULL:
        return "PASS"
    return "UNDECIDABLE"


def mode_prove(args, out):
    guard_resources()
    repo = args.repo or repo_root_of(__file__)
    fp = fingerprint_gate(repo, out)

    assert args.as_of is not None, "--prove requires --as-of"
    A = int(args.as_of)
    start = read_start_record(out)
    s = start["wall_ns"] / 1e9
    now = time.time()
    assert s <= A, "--as-of %d precedes the start record's %.9f" % (A, s)
    assert A <= now, "--as-of %d is in the future; now is %.9f" % (A, now)
    proof_lo, proof_hi = int(s), A
    length = proof_hi - proof_lo
    ctrl_lo, ctrl_hi = 2 * int(s) - A, int(s)
    out("as-of A %d (%s); start s %.9f (%s); s <= A <= now holds" % (
        A, utc(A), s, utc(s)))
    out("proof window   [%d, %d] = [%s, %s], length %d s" % (
        proof_lo, proof_hi, utc(proof_lo), utc(proof_hi), length))
    out("control window [%d, %d] = [%s, %s], length %d s" % (
        ctrl_lo, ctrl_hi, utc(ctrl_lo), utc(ctrl_hi), length))

    windows = load_windows(s, A, out)

    # ---- G-DEPLOY, with the full disclosure of V9 -------------------------
    cps = []
    for w in windows:
        sched = schedule_for(w["T"])
        by_tau = {}
        for e in w["entries"]:
            by_tau.setdefault(e["tau_prime"], []).append(e)
        for instant, tau in sched["checkpoints"]:
            entries = by_tau.get(tau, [])
            q, why = qualifies(sched["document_instant"], instant, s)
            if not entries:
                ok, reason = False, "not_stored"
            else:
                ok, reason = checkpoint_is_complete(entries)
            sk = skew_of(entries) if entries else None
            recvs = [e.get("recv_mono_ns") for e in entries]
            base = min([r for r in recvs if r is not None], default=None)
            deltas = [None if r is None or base is None else r - base for r in recvs]
            sends = [e.get("send_mono_ns") for e in entries]
            cps.append({
                "T": w["T"], "tau_prime": tau, "instant": instant,
                "document_instant": sched["document_instant"],
                "qualifying": q, "qualify_reason": why,
                "statuses": [e.get("status") for e in entries],
                "reasons": sorted({e.get("reason") for e in entries if e.get("reason")}),
                "recv_deltas_ns": deltas, "skew_ns": sk,
                "sends_stamped": sum(1 for x in sends if x is not None),
                "complete": ok, "complete_reason": reason,
                "concurrency_ok": concurrency_ok(entries) if entries else None,
            })
    cps.sort(key=lambda c: (c["instant"], c["T"]))

    out("")
    out("G-DEPLOY disclosure - every checkpoint of every considered window, in order:")
    out("%-12s %5s %-11s %-34s %-22s %-13s %-9s %s" % (
        "window T", "tau'", "instant", "qualifying / reason", "statuses",
        "recv deltas ns", "skew ns", "complete / reason"))
    for c in cps:
        out("%-12d %5d %-11d %-34s %-22s %-13s %-9s %s" % (
            c["T"], c["tau_prime"], c["instant"],
            ("yes " if c["qualifying"] else "no  ") + c["qualify_reason"],
            ",".join("null" if st is None else str(st) for st in c["statuses"]) or "-",
            ",".join("null" if d is None else str(d) for d in c["recv_deltas_ns"]) or "-",
            "null" if c["skew_ns"] is None else str(c["skew_ns"]),
            ("yes " if c["complete"] else "no  ") + c["complete_reason"]))

    qualifying = [c for c in cps if c["qualifying"]]
    units = qualifying[:GATE_UNITS]
    n_complete = sum(1 for c in units if c["complete"])
    reading_deploy = read_g_deploy(len(qualifying), n_complete)
    n_missed = sum(1 for c in cps
                   if any(r.startswith("missed_") for r in c["reasons"]))
    n_incomplete = sum(1 for c in cps if not c["complete"])
    out("")
    out("G-DEPLOY: qualifying %d, units scored %d of %d, complete %d, "
        "incomplete %d, missed %d -> %s" % (
            len(qualifying), len(units), GATE_UNITS, n_complete, n_incomplete,
            n_missed, reading_deploy))

    skews = [c["skew_ns"] for c in cps
             if c["skew_ns"] is not None and len(c["statuses"]) == 4
             and all(st is not None for st in c["statuses"])]
    skew_stats = {"n": len(skews),
                  "min": min(skews) if skews else None,
                  "median": median_str(skews),
                  "max": max(skews) if skews else None}
    out("skew over the %d checkpoints that produced four replies: min %s, median %s, "
        "max %s ns" % (skew_stats["n"], skew_stats["min"], skew_stats["median"],
                       skew_stats["max"]))

    conc = [c for c in cps if c["sends_stamped"] == 4]
    n_conc_bad = sum(1 for c in conc if not c["concurrency_ok"])
    out("V10 concurrency, recorded and not asserted: considered checkpoints with four "
        "sends %d, last send not before the first receive in %d" % (len(conc), n_conc_bad))
    for c in conc:
        if not c["concurrency_ok"]:
            out("V10 window %d tau' %d instant %d: last send did not precede the "
                "first receive" % (c["T"], c["tau_prime"], c["instant"]))

    # ---- G-TIERC ----------------------------------------------------------
    out("")
    tierc_rows = []
    for w in windows:
        issued = issued_of(w["docs"], w["entries"])
        E = w["T"] + WINDOW - TIERC_INTERVAL
        mp = os.path.join(RECORDER_ROOT, "btc-updown-5m", str(E), "manifest.json")
        try:
            counted = os.stat(mp).st_mtime_ns <= A * 10 ** 9
        except OSError:
            counted = False
        qc = json.loads(read_bytes(mp)).get("quotes_complete") if counted else None
        tierc_rows.append({
            "T": w["T"], "issued": issued, "of": REQUESTS_PER_WINDOW,
            "fully_loaded": issued == REQUESTS_PER_WINDOW,
            "E": E, "exposed": issued >= 1, "counted": counted,
            "quotes_complete": qc,
            "reason": None if counted else "no_manifest_by_as_of",
        })
    for r in tierc_rows:
        out("G-TIERC window %d: issued %d of %d, fully loaded %r, E %d (%s), "
            "counted %r, quotes_complete %r%s" % (
                r["T"], r["issued"], r["of"], r["fully_loaded"], r["E"],
                utc(r["E"]), r["counted"], r["quotes_complete"],
                "" if r["reason"] is None else " (" + r["reason"] + ")"))
    reading_tierc = read_g_tierc(tierc_rows)
    n_exposed = sum(1 for r in tierc_rows if r["exposed"])
    n_counted = sum(1 for r in tierc_rows if r["exposed"] and r["counted"])
    n_full = sum(1 for r in tierc_rows if r["exposed"] and r["counted"]
                 and r["fully_loaded"])
    n_bad = sum(1 for r in tierc_rows if r["exposed"] and r["counted"]
                and r["quotes_complete"] is not True)
    out("G-TIERC: exposed intervals %d, counted at A %d, fully loaded and counted %d "
        "(PASS needs %d), counted with quotes_complete not true %d -> %s" % (
            n_exposed, n_counted, n_full, TIERC_MIN_FULL, n_bad, reading_tierc))

    out("")
    proof_rows = manifest_scan(proof_lo, proof_hi, A, out, "proof  ")
    ctrl_rows = manifest_scan(ctrl_lo, ctrl_hi, A, out, "control")
    exposed_E = {r["E"] for r in tierc_rows if r["exposed"]}
    for r in proof_rows + ctrl_rows:
        r["exposed"] = r["T0"] in exposed_E
    out("proof-window intervals %d, manifests counted %d, quotes_complete true %d, "
        "exposed %d (printed beside the gate, not gated)" % (
            len(proof_rows), sum(1 for r in proof_rows if r["manifest"]),
            sum(1 for r in proof_rows if r["quotes_complete"] is True),
            sum(1 for r in proof_rows if r["exposed"])))
    out("control-window intervals %d, manifests counted %d, quotes_complete true %d, "
        "exposed %d" % (
            len(ctrl_rows), sum(1 for r in ctrl_rows if r["manifest"]),
            sum(1 for r in ctrl_rows if r["quotes_complete"] is True),
            sum(1 for r in ctrl_rows if r["exposed"])))

    for w in windows:
        out("stored bytes, window %d: %s" % (w["T"], json.dumps(
            w["stored_bytes"], sort_keys=True)))

    # ---- the two readings, and the file ----------------------------------
    outdir = args.out or WORK_ROOT
    proof = {
        "mode": "prove",
        "as_of": A,
        "start_record": {k: start.get(k) for k in
                         ("event", "pid", "wall_ns", "mono_ns", "commit", "file_sha256",
                          "argv")},
        "proof_window": {"lo": proof_lo, "hi": proof_hi, "length_s": length},
        "control_window": {"lo": ctrl_lo, "hi": ctrl_hi, "length_s": length},
        "g_deploy": {"qualifying": len(qualifying), "units": len(units),
                     "complete": n_complete, "incomplete": n_incomplete,
                     "missed": n_missed, "reading": reading_deploy},
        "g_tierc": {"windows": tierc_rows, "proof": proof_rows, "control": ctrl_rows,
                    "exposed": n_exposed, "counted": n_counted,
                    "fully_loaded_counted": n_full, "false_count": n_bad,
                    "min_fully_loaded": TIERC_MIN_FULL, "reading": reading_tierc},
        "checkpoints": cps,
        "skew_stats": skew_stats,
        "windows": [{"T": w["T"],
                     "documents_ok": (w["window_json"] or {}).get("documents_ok"),
                     "checkpoints_complete": (w["window_json"] or {}).get(
                         "checkpoints_complete"),
                     "doc_statuses": [d.get("status") for d in w["docs"]],
                     "closed": w["window_json"] is not None,
                     "issued": issued_of(w["docs"], w["entries"]),
                     "stored_bytes": w["stored_bytes"]} for w in windows],
        "counters": dict(COUNTERS),
        "concurrency": {"tested": len(conc), "violations": n_conc_bad},
    }
    assert_keys(proof, PROOF_JSON_KEYS, "tz18a-proof.json")
    ppath = os.path.join(outdir, "tz18a-proof.json")
    write_bytes(ppath, (json.dumps(proof, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    out("wrote %s" % ppath)

    out("")
    out("READING G-DEPLOY: %s (complete %d of the first %d qualifying checkpoints)" % (
        reading_deploy, n_complete, len(units)))
    out("READING G-TIERC:  %s (%d counted fully loaded exposed intervals of the %d "
        "counted; %d not quotes_complete)" % (
            reading_tierc, n_full, n_counted, n_bad))
    out("V1 fingerprint counts: %s" % json.dumps(fp, sort_keys=True))
    out("V5 write-path checks: %d" % COUNTERS["write_checks"])
    out("V6 opens under the reserved tree: %d, every basename manifest.json" %
        COUNTERS["recorder_opens"])
    out("V7 requests issued by this mode: %d" % COUNTERS["requests"])
    out("V13 bytes written: %d of cap %d" % (COUNTERS["bytes_written"], WRITE_CAP))
    assert COUNTERS["requests"] == 0, "--prove opens no socket"
    return 0


# ----------------------------------------------------------------------------
# --selftest  (section 5) - 39 asserts through one counting helper
# ----------------------------------------------------------------------------

def mode_selftest(args, out):
    n = [0]

    def A(cond, item, what):
        assert cond, "%s FAILED: %s" % (item, what)
        n[0] += 1
        bump("asserts")
        out("  %-3s assert %2d  %s" % (item, n[0], what))

    out("S1 - the schedule of section 3.5 at T = 1790035200")
    T = 1790035200
    sch = schedule_for(T)
    A(sch["document_instant"] == 1790035825, "S1", "document instant 1790035825")
    inst = [i for i, _ in sch["checkpoints"]]
    A(inst == [1790035855, 1790035915, 1790035975, 1790036005, 1790036035,
               1790036065, 1790036085], "S1", "the seven checkpoint instants")
    A(all(T + 600 < i < T + 900 for i in inst), "S1",
      "every checkpoint strictly inside (T+600, T+900)")
    tc = tierc_instants(T)
    A(tc == [1790035860, 1790035920, 1790035980, 1790036010, 1790036040, 1790036070,
             1790036090] and not (set(inst) & set(tc)), "S1",
      "no checkpoint equals any Tier C instant")
    A(sch["document_instant"] - 1790035805 == 20
      and inst[0] - sch["document_instant"] == 30, "S1",
      "the document instant is 20 s after the recorder's S6 instant 1790035805 "
      "and 30 s before the first checkpoint")

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

    out("S3 - the request, on a loopback listener and against nothing else")
    n_removed = 0
    for var in ("http_proxy", "https_proxy", "all_proxy",
                "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY"):
        if var in os.environ:
            del os.environ[var]
            n_removed += 1
    out("  S3  proxy variables removed from this process's environment: %d" % n_removed)

    def loopback(port):
        return "http" + ":" + "/" + "/" + "127.0.0.1" + ":" + str(port) + "/" + "x"

    def listener(code, body, box):
        class H(http.server.BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def do_GET(self):
                box["requestline"] = self.requestline
                box["headers"] = [(k, v) for k, v in self.headers.items()]
                self.send_response(code)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, fmt, *a):
                return

        srv = http.server.HTTPServer(("127.0.0.1", 0), H)
        th = threading.Thread(target=srv.handle_request, daemon=True)
        th.start()
        return srv, th

    req = build_request(loopback(1))
    A(req.get_method() == "GET"
      and sorted((k.lower(), v) for k, v in req.header_items())
      == [("accept", "application/json"), ("user-agent", "btc-5m-twap-tz18a")],
      "S3", "build_request has method GET and exactly the two fields it sets")

    box2 = {}
    srv2, th2 = listener(200, b"{}", box2)
    port2 = srv2.server_address[1]
    rec2 = http_get(loopback(port2))
    th2.join(READ_TIMEOUT_S + 2.0)
    srv2.server_close()
    seen = sorted((k.lower(), v) for k, v in box2["headers"])
    A(seen == [("accept", "application/json"), ("accept-encoding", "identity"),
               ("connection", "close"), ("host", "127.0.0.1:%d" % port2),
               ("user-agent", "btc-5m-twap-tz18a")]
      and len({k for k, _ in seen}) == 5
      and box2["requestline"].startswith("GET /"), "S3",
      "the wire block is exactly the five fields of section 3.2, no name repeated, "
      "and the request line begins GET /")
    A(rec2["status"] == 200 and rec2["bytes"] == 2
      and rec2["sha256"] == ("44136fa355b3678a1146ad16f7e8649e94fb4fc21fe"
                             "77e8310c060f61caaff8a")
      and rec2["recv_mono_ns"] is not None and rec2["recv_wall_ns"] is not None
      and rec2["recv_mono_ns"] >= rec2["send_mono_ns"], "S3",
      "its record: status 200, bytes 2, sha256 of the two-byte body, both receive "
      "stamps non-null, recv_mono_ns >= send_mono_ns")

    box4 = {}
    srv4, th4 = listener(403, b"error code: 1010\n", box4)
    rec4 = http_get(loopback(srv4.server_address[1]))
    th4.join(READ_TIMEOUT_S + 2.0)
    srv4.server_close()
    A(rec4["status"] == 403 and rec4["bytes"] == 17
      and rec4["recv_mono_ns"] is not None and rec4["recv_wall_ns"] is not None
      and rec4["reason"] == "http_error", "S3",
      "a 403 of 17 bytes: both receive stamps non-null, reason http_error")

    dead = http.server.HTTPServer(("127.0.0.1", 0),
                                  http.server.BaseHTTPRequestHandler)
    dead_port = dead.server_address[1]
    dead.server_close()
    rec5 = http_get(loopback(dead_port))
    A(rec5["status"] is None and rec5["bytes"] == 0
      and rec5["recv_mono_ns"] is None and rec5["recv_wall_ns"] is None
      and skew_of([{"recv_mono_ns": None}, {"recv_mono_ns": 7},
                   {"recv_mono_ns": 12}]) == 5, "S3",
      "a closed port: status None, bytes 0, both receive stamps None; and skew_of "
      "over (None, 7, 12) is 5")

    out("S4 - same_service, equality with the exact argv")
    mine = (b"/root/tz01-env/venv/bin/python\x00-B\x00-u\x00"
            b"/root/tz18a-svc/tz18a-chainbook-capture.py\x00--serve\x00")
    A(same_service(mine, SERVICE_ARGV), "S4",
      "the service's own NUL-joined command line equals SERVICE_ARGV")
    shell = (b"bash\x00-c\x00/root/tz01-env/venv/bin/python -B -u "
             b"/root/tz18a-svc/tz18a-chainbook-capture.py --serve\x00")
    A(not same_service(shell, SERVICE_ARGV), "S4",
      "a shell holding that command line as one argument does not equal it")
    old = (b"/root/tz01-env/venv/bin/python\x00-B\x00-u\x00"
           b"/root/tz18-svc/tz18-chainbook-capture.py\x00--serve\x00")
    A((not same_service(old, SERVICE_ARGV)) and same_service(old, OLD_SERVICE_ARGV),
      "S4", "TZ-18's command line equals OLD_SERVICE_ARGV and not SERVICE_ARGV")
    A((not same_service(mine + b"--x\x00", SERVICE_ARGV))
      and (not same_service(b"", SERVICE_ARGV)), "S4",
      "a sixth field --x fails, and so does an empty command line")

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

    A(raises("/root/btc-5m-twap/x") and raises("/root/tz18-work/x"), "S5",
      "a path in the repository and one in TZ-18's tree both raise")
    A(raises(RECORDER_ROOT + "/x"), "S5", "a path under the reserved tree raises")

    out("S6 - the readings of section 4 on synthetic counts")
    A(read_g_deploy(14, 13) == "PASS", "S6", "(14 qualifying, 13 complete) -> PASS")
    A(read_g_deploy(14, 12) == "FAIL", "S6", "(14 qualifying, 12 complete) -> FAIL")
    A(read_g_deploy(13, 13) == "UNDECIDABLE", "S6", "13 qualifying -> UNDECIDABLE")

    def trow(issued, counted, qc):
        return {"issued": issued, "counted": counted, "quotes_complete": qc}

    full_ok = [trow(30, True, True), trow(30, True, True)]
    A(read_g_tierc(full_ok) == "PASS", "S6",
      "two fully loaded counted intervals, both quotes_complete -> PASS")
    A(read_g_tierc(full_ok + [trow(1, True, False)]) == "FAIL", "S6",
      "one counted exposed interval not quotes_complete -> FAIL")
    A(read_g_tierc([trow(30, True, True), trow(30, False, None)]) == "UNDECIDABLE",
      "S6", "one fully loaded counted and one uncounted -> UNDECIDABLE")
    A(read_g_tierc([trow(30, True, True), trow(29, True, True)]) == "UNDECIDABLE",
      "S6", "one fully loaded and one that issued 29 -> UNDECIDABLE")
    A(read_g_tierc([trow(0, True, False)] + full_ok) == "PASS", "S6",
      "a window that issued nothing is not exposed and does not fail the gate")

    out("S7 - the three power literals, recomputed in exact Fraction arithmetic")
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

    out("S9 - considered() and issued_of()")
    A(considered(1790035200, 1790035000.0, 1790040000)
      and not considered(1790034300, 1790035000.0, 1790040000)
      and not considered(1790039700, 1790035000.0, 1790040000), "S9",
      "considered(T, 1790035000.0, 1790040000): true at 1790035200, false at "
      "1790034300 and at 1790039700")
    two_docs = [{"send_mono_ns": 11}, {"send_mono_ns": 12}]
    ents = [{"send_mono_ns": 20 + i} for i in range(28)]
    ents_null = [{"send_mono_ns": None} for _ in range(28)]
    A(issued_of(two_docs, ents) == 30 and issued_of(two_docs, ents_null) == 2, "S9",
      "issued_of is 30 over 2 documents and 28 stamped entries, 2 when the 28 are null")

    out("S10 - p_false_alarm, exact")
    A(p_false_alarm(0, 2016, FA_UNITS) == Fraction(0)
      and p_false_alarm(1, 2016, FA_UNITS) == Fraction(82508989399201,
                                                      33300644496408576)
      and p_false_alarm(0, 0, FA_UNITS) is None, "S10",
      "p_false_alarm(0, 2016, 5) is 0, (1, 2016, 5) is "
      "82508989399201/33300644496408576, and (0, 0, 5) is None")

    out("")
    out("selftest: %d of %d asserts" % (n[0], n[0]))
    assert n[0] == COUNTERS["asserts"], "the counting helper disagrees with itself"
    out("V7 requests issued by this mode: %d, each to 127.0.0.1" % COUNTERS["requests"])
    out("V5 write-path checks: %d" % COUNTERS["write_checks"])
    out("V6 opens under the reserved tree: %d" % COUNTERS["recorder_opens"])
    out("V13 bytes written: %d of cap %d" % (COUNTERS["bytes_written"], WRITE_CAP))
    return 0


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description="TZ-18a chain book capture")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--selftest", action="store_true")
    g.add_argument("--prestart", action="store_true")
    g.add_argument("--serve", action="store_true")
    g.add_argument("--prove", action="store_true")
    ap.add_argument("--out", default=None, help="directory for this run's outputs")
    ap.add_argument("--repo", default=None, help="repository root for the fingerprint gate")
    ap.add_argument("--as-of", dest="as_of", type=int, default=None,
                    help="the integer epoch --prove reads the store as of")
    args = ap.parse_args(argv)

    def out(msg):
        sys.stdout.write("[%s] %s\n" % (utc(time.time()), msg))
        sys.stdout.flush()

    if args.selftest:
        return mode_selftest(args, out)
    if args.prestart:
        return mode_prestart(args, out)
    if args.serve:
        return mode_serve(args, out)
    if args.prove:
        return mode_prove(args, out)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
