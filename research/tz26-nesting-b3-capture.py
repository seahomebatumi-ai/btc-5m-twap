#!/usr/bin/env python3
"""TZ-26 - the backup track's B3, its capture: the four books of the nested pair, streamed.

    serve             the service. For each 900 s window T: the documents of btc-updown-15m-{T} and
                      btc-updown-5m-{T+600} from T+545; the market websocket for their four tokens from
                      T+595 to T+905, every frame stored verbatim with its receive stamps; the chain
                      book's seven /book checkpoints, T+655 to T+885; window.json at T+910
    prestart          the request path on this host before the service starts, on the ETH nested pair:
                      two documents and one book through http_get, one stream session of 25 s through
                      the service's own stream code; the processes; G-TIERC's base rate
    prove A           G-STREAM, G-BOOKS and G-TIERC as of the epoch A; exit 3 is NOT YET
    load              G-LOAD: the service's processor time and memory since its start
    fingerprint       map section 0 against the primary checkout
    selftest          every rule of this file, on literals and on loopback servers only
    still             the recorder's unit: the first run records it, a later run compares (G-STILL)
    mark NAME         an instant, and the state of the unit it concerns, into state.json
    chainbook         the chain book's stop, from systemd, /proc and its own record (G-CB-STOP)
    unit N            G-UNIT for btc-pairbook.service at N restarts; at 0, G-START too
    restart           G-RESTART, from the service's own record
    restored          after a FAIL's two blocks: the pair book stopped, the chain book running again
    final             G-UNIT at one restart, G-STILL, and the unit's memory
    scratch OWN       the UUID directories beside OWN, this session's directory: live or earlier
    reclaim TREE...   section 9

It requests gamma-api.polymarket.com/markets/slug/, clob.polymarket.com/book and the market websocket
of ws-subscriptions-clob.polymarket.com, and nothing else, every request with the headers this file
fixes. It never authenticates, holds no credential and can place no order. The service writes what it
receives byte for byte and reads none of it back; no mode prints a price, a size, a side, a book's hash or
an outcome. An audit hook enforces section 2 of the TZ: under /var/lib/btc-recorder only a manifest.json is
opened, read only, by prestart and prove; under /var/lib/btc-chainbook only runtime.jsonl, read only, by
chainbook and restored; under /var/lib/btc-pairbook only serve writes; serve starts no process. Exit 0: every assert
held. Exit 1: an assert or a floor, named. Exit 2: serve refused its command line. Exit 3: another
instance runs, or NOT YET. Run it with /root/tz04a-env, whose websockets it needs.

Written for CryptoTZ/TZ-26-nesting-b3-capture.md. The TZ is the specification.
"""

import ast
import asyncio
import base64
import datetime
import errno
import gzip
import hashlib
import http.server
import json
import os
import re
import resource
import shutil
import signal
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
import zlib
from fractions import Fraction

import websockets
from websockets.asyncio.client import connect as ws_connect
from websockets.asyncio.server import serve as ws_serve

if not __debug__:
    sys.stderr.write("tz26: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(1)

# ---- the endpoints, and nothing else: three string constants carry a scheme separator ----------

GAMMA_MARKET_URL = "https://gamma-api.polymarket.com/markets/slug/{slug}"
CLOB_BOOK_URL = "https://clob.polymarket.com/book?token_id={token_id}"
CLOB_WS_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"

# ---- the TZ's constants: none of them is measured by this run -----------------------------------

MAP_REVISION = "2026-10-10-b"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 31, "tracked": 2, "reported": 1}

ROOT = "/var/lib/btc-pairbook"
RECORDER = "/var/lib/btc-recorder"
CHAINBOOK = "/var/lib/btc-chainbook"
SVC = "/root/btc-pairbook-svc"
WORK = "/root/tz26-work"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
DISK_PATH = "/var/lib"

UNIT = "btc-pairbook.service"
UNITS = {"recorder": "btc-recorder.service", "chainbook": "btc-chainbook.service", "pairbook": UNIT}
PYTHON = "/root/tz04a-env/venv/bin/python"
SERVICE_FILE = SVC + "/tz26-nesting-b3-capture.py"
SERVICE_ARGV = (PYTHON, "-B", "-u", SERVICE_FILE, "serve")
CHAINBOOK_ARGV = ("/root/tz01-env/venv/bin/python", "-B", "-u",
                  "/root/tz18a-svc/tz18a-chainbook-capture.py", "--serve")
MEMORY_MAX = 134217728       # MemoryMax=128M, the unit's ceiling (TZ-26 section 0.4)

UA = "btc-5m-twap-tz26"
ACCEPT = "application/json"

WINDOW = 900
DOC_OFFSET = 545             # the documents, from T+545, every DOC_RETRY_S until both carry token ids
DOC_RETRY_S = 5
DOC_GAP_S = 0.200            # >= 200 ms between two document requests
DOC_LAST = 880               # no document attempt starts after T+880
STREAM_OPEN = 595            # the stream, T+595 to T+905: the five-minute market's whole window, 5 s each side
STREAM_CLOSE = 905
CHECKPOINT_OFFSETS = (655, 715, 775, 805, 835, 865, 885)   # the chain book's seven
CLOSE_OFFSET = 910           # window.json
JOIN_LAST = 880              # a process starting inside a window joins it until T+880
READ_TIMEOUT_S = 5.0
GZ_LEVEL = 6                 # books.jsonl.gz, at the chain book's level
GZ_STREAM = 9                # stream files (TZ-26 section 6)
FLUSH_S = 10                 # a sync flush of the stream file at least every 10 s of frames
PING_S = 10                  # the venue's heartbeat: the text frame PING every 10 s
OPEN_TIMEOUT_S = 10
CLOSE_TIMEOUT_S = 2
MAX_FRAME = 1048576          # websockets' own default, 2 ** 20
MAX_QUEUE = 16               # and its queue: memory bounded at 16 frames of 1 MiB
BACKOFF_S = (1, 2, 4, 8)     # before a reconnect inside a window
SKEW_BOUND_NS = 1000000000   # a checkpoint's four replies within one second (the chain book's rule)

RESOURCE_FLOOR = 2200000000  # free bytes below which the service halts, exit 1
STREAM_FLOOR = 4500000000    # free bytes below which no stream opens for a window
STREAM_CAP = 8000000000      # stream bytes under ROOT at which no stream opens
WINDOW_STREAM_MAX = 100000000    # stored bytes of one window's stream at which it is cut
WRITE_CAP = 200000000        # bytes one process writes but its stream files
MEM_FLOOR = 107503616        # MemAvailable floor of prestart and prove: twice the self-test's peak (TZ-26 0.4)

# section 4 - the gates, fixed before their data
GATE_WINDOWS = 4             # G-STREAM and G-BOOKS: the first four qualifying windows
GATE_STREAM_PASS = 3         # >= 3 of 4 complete
GATE_CHECKPOINTS = 28        # G-BOOKS: their 28 checkpoints
GATE_BOOKS_PASS = 26         # >= 26 of 28 complete
TIERC_MIN = 2                # G-TIERC: at least two counted fully loaded exposed intervals
LOAD_MAX = Fraction(1, 4)    # G-LOAD: at most a quarter of the one processor, since the start
QUALIFY_LEAD_S = 60          # a window qualifies when T+545 >= s + 60
BUDGET_S = 6000              # the proof decides by s + 6,000
SUBSCRIBE_BY = 600           # the first subscribe at or before T+600
INITIAL_S = 5                # a book of each of the four tokens within 5 s of it
END_BY = 900                 # the stream's last close at or after T+900
GAP_MAX_NS = 15000000000     # no two consecutive received instants more than 15 s apart
LAG_RANGE_MS = (-1000, 60000)  # the venue-to-host lag, counted in ms and clamped to this range
BASE_RATE_S = 604800         # G-TIERC's base rate: the week before prestart
FA_UNITS = 4                 # four exposed intervals are judged
RESTART_MAX_S = 60
KNOWN = ("book", "price_change", "last_trade_price", "tick_size_change")

TOKEN = re.compile(r"[0-9a-f]{16,64}")
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
MANIFEST_RE = re.compile(re.escape(RECORDER) + r"/btc-updown-5m/[0-9]{10}/manifest\.json")
LIVE_S = 60

# the stored formats, and the allow-lists every output is asserted against before it is written
BOOK_KEYS = ("T", "tau_prime", "market", "slug", "token_id", "outcome_label", "url", "status",
             "send_mono_ns", "recv_mono_ns", "recv_wall_ns", "bytes", "sha256", "raw", "reason")
DOC_KEYS = ("slug", "url", "status", "send_mono_ns", "recv_mono_ns", "recv_wall_ns", "bytes",
            "sha256", "raw", "attempt", "pid")
WINDOW_JSON_KEYS = frozenset(("T", "document_instant", "documents_ok", "document_attempts",
                              "documents_ready_wall_ns", "closed_wall_ns", "checkpoints_complete",
                              "status_counts", "skews_ns", "missed", "markets", "stream", "joined_late",
                              "stopped", "pid"))
WINDOW_MARKET_KEYS = frozenset(("slug", "clobTokenIds", "outcomes", "conditionId"))
STREAM_KEYS = frozenset(("opened", "off_reason", "files", "segments", "frames", "frame_bytes", "pongs",
                         "pings", "first_frame_wall_ns", "last_frame_wall_ns", "max_gap_ns",
                         "subscribed_wall_ns", "stored_bytes", "cut"))
PRESTART_JSON_KEYS = frozenset(("mode", "p_wall", "file_sha256", "processes", "proxy_variables",
                                "base_rate", "requests", "stream", "counters"))
PROOF_JSON_KEYS = frozenset(("mode", "as_of", "start", "windows", "g_stream", "g_books", "g_tierc",
                             "control", "counters"))
FORBIDDEN_KEYS = frozenset(("price", "prices", "bid", "bids", "ask", "asks", "mid", "midpoint", "size",
                            "sizes", "level", "levels", "book", "books", "spread", "raw", "priceToBeat",
                            "finalPrice", "best_bid", "best_ask", "amount", "quote", "quotes", "side",
                            "outcomePrices", "hash"))
FRAME_KEYS = frozenset(("recv_ns", "mono_ns", "raw"))
FRAME_B64_KEYS = frozenset(("recv_ns", "mono_ns", "raw_b64"))

HERE = os.path.dirname(os.path.abspath(__file__))
MODE = [None]
COUNTERS = {"requests": 0, "sessions": 0, "bytes_written": 0, "stream_bytes": 0, "frames": 0}
_LOCK = threading.Lock()
STOP_FLAG = threading.Event()
STOP_EVENT = [None]


class GuardError(RuntimeError):
    pass


class FloorStop(Exception):
    pass


def bump(name, by=1):
    with _LOCK:
        COUNTERS[name] += by
        return COUNTERS[name]

# ---- the audit hook: TZ-26 section 2 as a pure function, and the hook that applies it ------------


WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
REFUSED = []
OPENS = {"manifest.json": 0, "chainbook": 0}
HOOKED = ("open", "os.listdir", "os.scandir", "subprocess.Popen", "os.system", "os.exec", "os.spawn",
          "os.posix_spawn", "os.fork", "os.forkpty")


def _under(p, root):
    return p == root or p.startswith(root + "/")


def _writing(wmode, flags):
    if isinstance(wmode, str):
        return bool(set(wmode) & set("wax+"))
    return isinstance(flags, int) and bool(flags & WRITE_FLAGS)


def _exclusive(wmode, flags):
    if isinstance(wmode, str):
        return "x" in wmode
    return isinstance(flags, int) and bool(flags & os.O_EXCL)


def _path(args):
    p = args[0] if args else None
    if isinstance(p, bytes):
        p = os.fsdecode(p)
    return os.path.abspath(p) if isinstance(p, str) else None


def policy(mode, event, args):
    """None where section 2 allows the event in this mode; otherwise the reason it is refused."""
    if event == "open":
        p = _path(args)
        if p is None:
            return None
        wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
        w = _writing(wm, fl)
        if _under(p, RECORDER):
            if mode in ("prestart", "prove") and not w and MANIFEST_RE.fullmatch(p):
                return None
            return "the recorder's root"
        if _under(p, CHAINBOOK):
            if mode in ("chainbook", "restored") and not w and p == CHAINBOOK + "/runtime.jsonl":
                return None
            return "the chain book's root"
        if _under(p, ROOT):
            if w:
                return None if mode == "serve" else "a write under the pair book's root"
            return None if mode in ("serve", "prove", "load", "unit", "restart", "final", "restored") else \
                "a read under the pair book's root"
        if w:
            if mode == "serve":
                return "a write outside the pair book's root"
            if _under(p, WORK):
                return None
            if mode == "reclaim" and _under(p, FORENSICS) and _exclusive(wm, fl):
                return None
            return "a write outside the work tree"
        return None
    if event in ("os.listdir", "os.scandir"):
        p = _path(args)
        if p is None:
            return None
        if _under(p, RECORDER):
            return "a listing under the recorder's root"
        if _under(p, CHAINBOOK):
            return "a listing under the chain book's root"
        if _under(p, ROOT):
            return None if mode in ("serve", "prove") else "a listing under the pair book's root"
        return None
    if event in HOOKED:
        return "a process started by the service" if mode == "serve" else None
    return None


def _audit(event, args):
    if event not in HOOKED:
        return
    why = policy(MODE[0], event, args)
    if why is not None:
        REFUSED.append((event, str(args[0]) if args else ""))
        raise GuardError("%s refused in mode %s, %s: %r" % (event, MODE[0], why, args[0] if args else None))
    if event == "open":
        p = _path(args)
        if p is not None and _under(p, RECORDER):
            OPENS["manifest.json"] += 1
        elif p is not None and _under(p, CHAINBOOK):
            OPENS["chainbook"] += 1


sys.addaudithook(_audit)

# ---- small helpers -------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return datetime.datetime.fromtimestamp(float(t), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def json_line(obj):
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def account(n):
    """Every byte a process writes but its stream files, against WRITE_CAP."""
    total = bump("bytes_written", n)
    if total > WRITE_CAP:
        raise FloorStop("write cap: %d bytes written, above %d" % (total, WRITE_CAP))
    return total


def append_bytes(path, data):
    with open(path, "ab") as fh:
        fh.write(data)
    account(len(data))


def write_new(path, data):
    """A file that must not exist yet: exclusive create."""
    with open(path, "xb") as fh:
        fh.write(data)
    account(len(data))


def free_bytes():
    st = os.statvfs(DISK_PATH)
    return st.f_bavail * st.f_frsize


def guard_resources():
    free = free_bytes()
    if free < RESOURCE_FLOOR:
        raise FloorStop("free %d bytes, below the floor %d" % (free, RESOURCE_FLOOR))
    return free


def mem_available():
    with open("/proc/meminfo", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) * 1024
    raise AssertionError("no MemAvailable")


def floor_check():
    """Before a mode that reads the venue or the capture: the host's memory floor (section 0.4)."""
    avail = mem_available()
    out("MemAvailable %d bytes, floor %d" % (avail, MEM_FLOOR))
    assert avail >= MEM_FLOOR, "BLOCKED: MemAvailable %d bytes, below %d" % (avail, MEM_FLOOR)


def assert_keys(obj, allowed, what):
    got = frozenset(obj)
    assert got == allowed, "%s key set %s, required %s" % (what, sorted(got), sorted(allowed))
    forbid(obj, what)


def forbid(obj, what, depth=0):
    """No price, size, level, side or hash leaves the store through an output file."""
    assert depth < 12, "%s nested too deep" % what
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert k not in FORBIDDEN_KEYS, "%s carries a forbidden key: %s" % (what, k)
            forbid(v, what, depth + 1)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            forbid(v, what, depth + 1)


def load_state():
    if not os.path.exists(STATE):
        return {}
    with open(STATE, encoding="utf-8") as fh:
        return json.load(fh)


def save_state(state):
    tmp = STATE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(state, sort_keys=True, indent=1) + "\n")
    os.replace(tmp, STATE)


def quantiles(values):
    if not values:
        return None
    v = sorted(values)
    return {"n": len(v), "min": v[0], "median": v[(len(v) - 1) // 2], "p99": v[(len(v) * 99) // 100],
            "max": v[-1]}

# ---- the schedule -------------------------------------------------------------------------------


def slug15(t, asset="btc"):
    return "%s-updown-15m-%d" % (asset, t)


def slug5(t, asset="btc"):
    return "%s-updown-5m-%d" % (asset, t)


def schedule_for(T):
    assert T % WINDOW == 0, "a window starts on a 900-second boundary: %d" % T
    return {"T": T, "document_instant": T + DOC_OFFSET, "stream_open": T + STREAM_OPEN,
            "stream_close": T + STREAM_CLOSE,
            "checkpoints": [(T + off, WINDOW - off) for off in CHECKPOINT_OFFSETS],
            "close_instant": T + CLOSE_OFFSET}


def next_window(now):
    """The window to run next and whether it is joined late: the current 900 s window until T+880,
    after that the next one."""
    c = int(now) // WINDOW * WINDOW
    if now <= c + JOIN_LAST:
        return c, now > c + DOC_OFFSET
    return c + WINDOW, False


def joinable(wdir):
    """A window a process may still run: no earlier process closed it or wrote its books."""
    return not (os.path.exists(os.path.join(wdir, "window.json")) or
                os.path.exists(os.path.join(wdir, "books.jsonl.gz")))


def tierc_instants(T):
    """The recorder's seven Tier C reads of btc-updown-5m-{T+600} (config.py line 93)."""
    return [T + 600 + 300 - tau for tau in (240, 180, 120, 90, 60, 30, 10)]

# ---- the network: two REST endpoints -------------------------------------------------------------


def build_request(url):
    """The one builder of every HTTP request: GET with Accept and this file's User-Agent."""
    return urllib.request.Request(url, method="GET", headers={"Accept": ACCEPT, "User-Agent": UA})


def http_get(url, timeout=READ_TIMEOUT_S):
    """One GET through build_request. No retry. Both receive stamps only where a status came back."""
    bump("requests")
    send_mono = time.monotonic_ns()
    status, body, reason = None, b"", None
    try:
        with urllib.request.urlopen(build_request(url), timeout=timeout) as resp:
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
    recv_mono, recv_wall = time.monotonic_ns(), time.time_ns()
    if status is None:
        recv_mono = recv_wall = None
    try:
        raw = body.decode("utf-8")
    except UnicodeDecodeError:
        raw = body.decode("latin-1")
    return {"url": url, "status": status, "send_mono_ns": send_mono, "recv_mono_ns": recv_mono,
            "recv_wall_ns": recv_wall, "bytes": len(body), "sha256": sha256_bytes(body), "raw": raw,
            "reason": reason}


def parse_maybe_string(v):
    if isinstance(v, str):
        try:
            return json.loads(v)
        except ValueError:
            return v
    return v


def token_ids_of(doc_raw):
    """clobTokenIds, outcomes and conditionId exactly as the document carries them, and the two ids."""
    doc = json.loads(doc_raw)
    if isinstance(doc, list):
        doc = doc[0] if doc else {}
    if not isinstance(doc, dict):
        return None, None, {"clobTokenIds": None, "outcomes": None, "conditionId": None}
    verbatim = {"clobTokenIds": doc.get("clobTokenIds"), "outcomes": doc.get("outcomes"),
                "conditionId": doc.get("conditionId")}
    ids, outs = parse_maybe_string(verbatim["clobTokenIds"]), parse_maybe_string(verbatim["outcomes"])
    if not isinstance(ids, list) or not isinstance(outs, list):
        return None, None, verbatim
    ids, outs = [str(i) for i in ids], [str(o) for o in outs]
    if len(ids) != 2 or len(set(ids)) != 2 or not all(ids):
        return None, None, verbatim
    return ids, (outs[:2] if len(outs) >= 2 else [None, None]), verbatim


def checkpoint_is_complete(entries):
    """The chain book's rule: four replies, all 200, each non-empty and JSON, within one second."""
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
    sk = skew_of(entries)
    if sk is None:
        return False, "no_skew"
    if sk > SKEW_BOUND_NS:
        return False, "skew_above_bound"
    return True, "complete"


def skew_of(entries):
    recvs = [e["recv_mono_ns"] for e in entries if e.get("recv_mono_ns") is not None]
    return (max(recvs) - min(recvs)) if recvs else None


def entry(spec, T, tau, **kw):
    e = dict(spec, T=T, tau_prime=tau, url=None, status=None, send_mono_ns=None, recv_mono_ns=None,
             recv_wall_ns=None, bytes=0, sha256=None, raw="", reason=None)
    e.update(kw)
    return e


def specs_of(plan):
    out_ = []
    for m in ("m15", "m5"):
        ids, labels = plan[m]["ids"], plan[m]["labels"]
        for i in range(2):
            out_.append({"market": m, "slug": plan[m]["slug"], "token_id": None if ids is None else ids[i],
                         "outcome_label": None if labels is None else labels[i]})
    return out_


def fetch_books(T, tau, plan):
    """Four GETs, one per token, each in its own thread, released together (the chain book's design)."""
    specs = specs_of(plan)
    if any(s["token_id"] is None for s in specs):
        return [entry(s, T, tau, reason="no_token_ids") for s in specs]
    entries = [None] * 4
    gate = threading.Event()

    def worker(i, s):
        gate.wait()
        entries[i] = dict(s, T=T, tau_prime=tau, **http_get(CLOB_BOOK_URL.format(token_id=s["token_id"])))

    threads = [threading.Thread(target=worker, args=(i, s), daemon=True) for i, s in enumerate(specs)]
    for th in threads:
        th.start()
    gate.set()
    deadline = time.monotonic() + READ_TIMEOUT_S + 2.0
    for th in threads:
        th.join(max(0.0, deadline - time.monotonic()))
    return [entries[i] if entries[i] is not None else entry(s, T, tau, reason="thread_deadline")
            for i, s in enumerate(specs)]

# ---- the network: the stream ---------------------------------------------------------------------


def subscription(tokens):
    """The documented subscribe frame, compact, the four tokens in the documents' order."""
    return json.dumps({"assets_ids": list(tokens), "type": "market"}, separators=(",", ":"))


def connect_kwargs(proxy=True):
    """Every option of the opening handshake, fixed: no compression offered, no protocol ping, this
    file's User-Agent; `proxy` is websockets' own default, the environment's; None on the loopback."""
    return {"open_timeout": OPEN_TIMEOUT_S, "close_timeout": CLOSE_TIMEOUT_S, "ping_interval": None,
            "max_size": MAX_FRAME, "max_queue": MAX_QUEUE, "compression": None, "user_agent_header": UA,
            "proxy": proxy}


def stopping():
    return STOP_FLAG.is_set()


async def sleep_until(t):
    """True at t; False at once where the service is stopping."""
    while True:
        if stopping():
            return False
        left = t - time.time()
        if left <= 0:
            return True
        ev = STOP_EVENT[0]
        if ev is None:
            await asyncio.sleep(min(left, 0.5))
        else:
            try:
                await asyncio.wait_for(ev.wait(), timeout=min(left, 0.5))
            except TimeoutError:
                pass


class StreamWriter:
    """One stream file: gzip, a sync flush at least every FLUSH_S, one JSON line per received frame -
    recv_ns, mono_ns and raw, the frame verbatim - and one per session event; the last an `end` line."""

    def __init__(self, path, level=GZ_STREAM, window_max=WINDOW_STREAM_MAX, flush_s=FLUSH_S):
        self.path = path
        self.fh = open(path, "xb")
        self.gz = gzip.GzipFile(filename="", mode="wb", fileobj=self.fh, compresslevel=level, mtime=0)
        self.window_max, self.flush_s = window_max, flush_s
        self.last_flush = time.monotonic()
        self.frames = self.frame_bytes = self.pongs = self.pings = 0
        self.first = self.last = self.max_gap = self.subscribed = None
        self.cut = False
        self.stored = 0

    def _line(self, b):
        self.gz.write(b)
        if time.monotonic() - self.last_flush >= self.flush_s:
            self.flush()

    def flush(self):
        self.gz.flush()
        self.fh.flush()
        self.last_flush = time.monotonic()
        self.stored = self.fh.tell()
        if self.stored >= self.window_max:
            self.cut = True

    def frame(self, msg):
        wall, mono = time.time_ns(), time.monotonic_ns()
        if isinstance(msg, (bytes, bytearray)):
            self._line((json.dumps({"recv_ns": wall, "mono_ns": mono,
                                    "raw_b64": base64.b64encode(bytes(msg)).decode("ascii")},
                                   separators=(",", ":")) + "\n").encode("utf-8"))
            n = len(msg)
        else:
            self._line((json.dumps({"recv_ns": wall, "mono_ns": mono, "raw": msg}, ensure_ascii=False,
                                   separators=(",", ":")) + "\n").encode("utf-8"))
            n = len(msg.encode("utf-8"))
            if msg == "PONG":
                self.pongs += 1
        self.frames += 1
        self.frame_bytes += n
        if self.last is not None:
            gap = wall - self.last
            self.max_gap = gap if self.max_gap is None else max(self.max_gap, gap)
        if self.first is None:
            self.first = wall
        self.last = wall

    def event(self, name, **kw):
        obj = {"recv_ns": time.time_ns(), "mono_ns": time.monotonic_ns(), "event": name}
        for k in sorted(kw):
            obj[k] = kw[k]
        if name == "ping":
            self.pings += 1
        if name == "subscribe" and self.subscribed is None:
            self.subscribed = obj["recv_ns"]
        self._line((json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8"))

    def close(self):
        self.event("end", frames=self.frames, frame_bytes=self.frame_bytes, pongs=self.pongs, pings=self.pings)
        self.gz.close()
        self.fh.close()
        self.stored = os.path.getsize(self.path)
        bump("stream_bytes", self.stored)
        bump("frames", self.frames)

    def summary(self):
        return {"frames": self.frames, "frame_bytes": self.frame_bytes, "pongs": self.pongs,
                "pings": self.pings, "first_frame_wall_ns": self.first, "last_frame_wall_ns": self.last,
                "max_gap_ns": self.max_gap, "subscribed_wall_ns": self.subscribed, "cut": self.cut}


async def ping_loop(ws, w, seg, ping_s):
    while True:
        await asyncio.sleep(ping_s)
        await ws.send("PING")
        w.event("ping", seg=seg)


async def one_session(w, seg, tokens, end, url, ping_s, kw):
    """One connection: open, subscribe, every frame to the writer until `end`, a stop, a cut or a drop."""
    w.event("connect", seg=seg, url=url, pid=os.getpid())
    bump("sessions")
    reason, code = None, None
    try:
        async with ws_connect(url, **kw) as ws:
            w.event("open", seg=seg, status=ws.response.status_code,
                    extensions=ws.response.headers.get("Sec-WebSocket-Extensions"))
            msg = subscription(tokens)
            await ws.send(msg)
            w.event("subscribe", seg=seg, message=msg)
            pinger = asyncio.create_task(ping_loop(ws, w, seg, ping_s))
            try:
                while True:
                    left = end - time.time()
                    if left <= 0:
                        reason = "end"
                        break
                    if stopping():
                        reason = "stop"
                        break
                    try:
                        frame = await asyncio.wait_for(ws.recv(), timeout=min(left, 0.5))
                    except TimeoutError:
                        continue
                    w.frame(frame)
                    if w.cut:
                        reason = "cut"
                        break
            finally:
                pinger.cancel()
                try:
                    await pinger
                except BaseException:
                    pass
    except websockets.ConnectionClosed as exc:
        reason = "closed"
        code = exc.rcvd.code if exc.rcvd is not None else None
    except Exception as exc:
        reason = "%s: %s" % (type(exc).__name__, str(exc)[:200])
    w.event("close", seg=seg, reason=reason, code=code)
    return reason


def next_stream_path(wdir):
    k = 0
    while True:
        p = os.path.join(wdir, "stream.jsonl.gz" if k == 0 else "stream.%d.jsonl.gz" % k)
        if not os.path.exists(p):
            return p
        k += 1


async def stream_window(wdir, tokens, start, end, stats, url=CLOB_WS_URL, ping_s=PING_S, kw=None,
                        backoff=BACKOFF_S, level=GZ_STREAM, window_max=WINDOW_STREAM_MAX):
    """The stream of one window: sessions from `start` to `end`, a reconnect after each drop."""
    if not await sleep_until(start):
        return
    kw = connect_kwargs() if kw is None else kw
    w = StreamWriter(next_stream_path(wdir), level=level, window_max=window_max)
    stats["opened"] = True
    stats["files"].append(os.path.basename(w.path))
    seg = 0
    try:
        while not stopping() and time.time() < end and not w.cut:
            await one_session(w, seg, tokens, end, url, ping_s, kw)
            seg += 1
            if stopping() or time.time() >= end or w.cut:
                break
            await sleep_until(min(end, time.time() + backoff[min(seg - 1, len(backoff) - 1)]))
    finally:
        w.close()
        stats["segments"] += seg
        s = w.summary()
        for k in ("frames", "frame_bytes", "pongs", "pings"):
            stats[k] += s[k]
        for k in ("first_frame_wall_ns", "subscribed_wall_ns"):
            if stats[k] is None:
                stats[k] = s[k]
        if s["last_frame_wall_ns"] is not None:
            stats["last_frame_wall_ns"] = s["last_frame_wall_ns"]
        if s["max_gap_ns"] is not None:
            stats["max_gap_ns"] = s["max_gap_ns"] if stats["max_gap_ns"] is None else max(
                stats["max_gap_ns"], s["max_gap_ns"])
        stats["stored_bytes"] += w.stored
        stats["cut"] = stats["cut"] or s["cut"]


def stream_bytes_total(root):
    """The bytes of every stream file under root, by directory entries alone."""
    total = 0
    if not os.path.isdir(root):
        return 0
    with os.scandir(root) as it:
        dirs = [d.path for d in it if d.is_dir(follow_symlinks=False) and d.name.isdigit()]
    for d in dirs:
        with os.scandir(d) as it:
            for f in it:
                if f.name.startswith("stream") and f.name.endswith(".jsonl.gz"):
                    total += f.stat(follow_symlinks=False).st_size
    return total


def stream_off_reason(docs_ok, free, total):
    """Why no stream opens for a window, or None: the documents, the stream floor, the stream cap."""
    if not docs_ok:
        return "documents"
    if free < STREAM_FLOOR:
        return "floor"
    if total >= STREAM_CAP:
        return "cap"
    return None


def new_stream_stats():
    return {"opened": False, "off_reason": None, "files": [], "segments": 0, "frames": 0, "frame_bytes": 0,
            "pongs": 0, "pings": 0, "first_frame_wall_ns": None, "last_frame_wall_ns": None,
            "max_gap_ns": None, "subscribed_wall_ns": None, "stored_bytes": 0, "cut": False}

# ---- the service ---------------------------------------------------------------------------------


def same_service(cmdline_bytes, argv):
    """Equality with the exact argv, field for field, never a substring."""
    fields = cmdline_bytes.split(b"\x00")
    if fields and fields[-1] == b"":
        fields = fields[:-1]
    try:
        decoded = [f.decode("utf-8") for f in fields]
    except UnicodeDecodeError:
        return False
    return decoded == list(argv)


def processes_with(argv):
    found = []
    for pid in sorted((p for p in os.listdir("/proc") if p.isdigit()), key=int):
        try:
            with open("/proc/%s/cmdline" % pid, "rb") as fh:
                cmd = fh.read()
        except OSError:
            continue
        if same_service(cmd, argv):
            found.append(int(pid))
    return found


def read_commit(directory):
    try:
        with open(os.path.join(directory, "commit.txt"), "rb") as fh:
            return fh.read().decode("ascii").strip()
    except OSError:
        return None


def runtime_record(root, event, extra=None):
    with open(os.path.abspath(__file__), "rb") as fh:
        own = sha256_bytes(fh.read())
    rec = {"event": event, "pid": os.getpid(), "wall_ns": time.time_ns(), "mono_ns": time.monotonic_ns(),
           "commit": read_commit(HERE), "file_sha256": own, "argv": list(sys.argv),
           "config": {"root": root, "headers": [["Accept", ACCEPT], ["User-Agent", UA]],
                      "service_argv": list(SERVICE_ARGV), "ws_url": CLOB_WS_URL, "doc_offset": DOC_OFFSET,
                      "stream": [STREAM_OPEN, STREAM_CLOSE], "checkpoint_offsets": list(CHECKPOINT_OFFSETS),
                      "close_offset": CLOSE_OFFSET, "ping_s": PING_S, "gz_stream": GZ_STREAM,
                      "flush_s": FLUSH_S, "max_frame": MAX_FRAME, "max_queue": MAX_QUEUE,
                      "resource_floor": RESOURCE_FLOOR, "stream_floor": STREAM_FLOOR, "stream_cap": STREAM_CAP,
                      "window_stream_max": WINDOW_STREAM_MAX, "write_cap": WRITE_CAP}}
    if extra:
        rec.update(extra)
    append_bytes(os.path.join(root, "runtime.jsonl"), json_line(rec))
    return rec


def acquire_single_instance(root):
    """O_CREAT | O_EXCL; a live sibling, identified by equality with SERVICE_ARGV, wins."""
    pidfile = os.path.join(root, "service.pid")
    while True:
        try:
            fd = os.open(pidfile, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
            try:
                with open(pidfile, "rb") as fh:
                    other = int(fh.read().decode("ascii").strip() or "0")
            except (OSError, ValueError):
                other = 0
            try:
                with open("/proc/%d/cmdline" % other, "rb") as fh:
                    cmd = fh.read()
            except OSError:
                cmd = b""
            if other != os.getpid() and same_service(cmd, SERVICE_ARGV):
                out("another instance runs as pid %d" % other)
                return None
            out("stale pid file (pid %d) replaced" % other)
            os.unlink(pidfile)
            continue
        data = ("%d\n" % os.getpid()).encode("ascii")
        os.write(fd, data)
        os.close(fd)
        account(len(data))
        return pidfile


async def fetch_documents(T, wdir, slugs, plan):
    """Both documents, from now, every DOC_RETRY_S, until both carry two token ids or T+880; every
    attempt stored verbatim in documents.jsonl."""
    attempts = 0
    path = os.path.join(wdir, "documents.jsonl")
    while True:
        for m in ("m15", "m5"):
            if plan[m]["ids"] is not None:
                continue
            if attempts:
                await asyncio.sleep(DOC_GAP_S)
            res = await asyncio.to_thread(http_get, GAMMA_MARKET_URL.format(slug=slugs[m]))
            attempts += 1
            rec = {k: res.get(k) for k in DOC_KEYS if k not in ("attempt", "pid")}
            rec.update({"slug": slugs[m], "attempt": attempts, "pid": os.getpid()})
            append_bytes(path, json_line(rec))
            if res["status"] == 200 and res["bytes"]:
                try:
                    ids, labels, verbatim = token_ids_of(res["raw"])
                except ValueError:
                    ids, labels, verbatim = None, None, plan[m]["verbatim"]
                plan[m]["verbatim"] = verbatim
                if ids is not None:
                    plan[m]["ids"], plan[m]["labels"] = ids, labels
        if all(plan[m]["ids"] is not None for m in ("m15", "m5")):
            return attempts, time.time_ns()
        if stopping() or time.time() + DOC_RETRY_S > T + DOC_LAST:
            return attempts, None
        if not await sleep_until(time.time() + DOC_RETRY_S):
            return attempts, None


async def checkpoints(T, plan, sched):
    lines, status_counts, skews = [], {}, []
    complete = missed = 0
    for instant, tau in sched["checkpoints"]:
        if stopping():
            ents = [entry(s, T, tau, reason="stopped") for s in specs_of(plan)]
        elif time.time() > instant:
            missed += 1
            ents = [entry(s, T, tau, reason="missed_scheduled_%d" % instant) for s in specs_of(plan)]
        elif not await sleep_until(instant):
            ents = [entry(s, T, tau, reason="stopped") for s in specs_of(plan)]
        else:
            ents = await asyncio.to_thread(fetch_books, T, tau, plan)
        ok, _why = checkpoint_is_complete(ents)
        complete += 1 if ok else 0
        skews.append(skew_of(ents))
        for e in ents:
            key = "null" if e["status"] is None else str(e["status"])
            status_counts[key] = status_counts.get(key, 0) + 1
            lines.append(json_line({k: e.get(k) for k in BOOK_KEYS}))
    return lines, complete, missed, status_counts, skews


async def run_window(T, late, store, asset="btc", root=None):
    """One window, the whole of it; window.json last. `store` carries the stream bytes under root."""
    root = ROOT if root is None else root
    sched = schedule_for(T)
    slugs = {"m15": slug15(T, asset), "m5": slug5(T + 600, asset)}
    plan = {m: {"slug": slugs[m], "ids": None, "labels": None,
                "verbatim": {"clobTokenIds": None, "outcomes": None, "conditionId": None}} for m in slugs}
    out("window %d (%s): documents from %s%s" % (T, utc(T), utc(T + DOC_OFFSET), ", joined late" if late else ""))
    if not await sleep_until(T + DOC_OFFSET):
        return None
    free = guard_resources()
    wdir = os.path.join(root, str(T))
    os.makedirs(wdir, exist_ok=True)
    attempts, ready = await fetch_documents(T, wdir, slugs, plan)
    docs_ok = ready is not None
    stats = new_stream_stats()
    stats["off_reason"] = stream_off_reason(docs_ok, free, store["stream_bytes"])
    task = None
    if stats["off_reason"] is None:
        tokens = plan["m15"]["ids"] + plan["m5"]["ids"]
        task = asyncio.create_task(stream_window(wdir, tokens, max(T + STREAM_OPEN, time.time()),
                                                 T + STREAM_CLOSE, stats))
    try:
        lines, complete, missed, status_counts, skews = await checkpoints(T, plan, sched)
    finally:
        if task is not None:
            try:
                await task
            except GuardError:
                raise
            except Exception as exc:
                stats["off_reason"] = "error: %s" % type(exc).__name__
            store["stream_bytes"] += stats["stored_bytes"]
    if lines:
        write_new(os.path.join(wdir, "books.jsonl.gz"), gzip.compress(b"".join(lines), compresslevel=GZ_LEVEL, mtime=0))
    await sleep_until(sched["close_instant"])
    markets = {}
    for m in ("m15", "m5"):
        mk = {"slug": slugs[m]}
        mk.update({k: plan[m]["verbatim"].get(k) for k in ("clobTokenIds", "outcomes", "conditionId")})
        assert frozenset(mk) == WINDOW_MARKET_KEYS, "window.json market keys"
        markets[m] = mk
    assert frozenset(stats) == STREAM_KEYS, "window.json stream keys"
    wj = {"T": T, "document_instant": sched["document_instant"], "documents_ok": docs_ok,
          "document_attempts": attempts, "documents_ready_wall_ns": ready, "closed_wall_ns": time.time_ns(),
          "checkpoints_complete": complete, "status_counts": status_counts, "skews_ns": skews,
          "missed": missed, "markets": markets, "stream": stats, "joined_late": late, "stopped": stopping(),
          "pid": os.getpid()}
    assert_keys(wj, WINDOW_JSON_KEYS, "window.json")
    write_new(os.path.join(wdir, "window.json"), json_line(wj))
    out("window %d closed: documents %s in %d attempts; checkpoints %d of 7, missed %d; stream %s, %d frames, "
        "%d segments, %d bytes stored%s" % (
            T, docs_ok, attempts, complete, missed, "opened" if stats["opened"] else "off (%s)" % stats["off_reason"],
            stats["frames"], stats["segments"], stats["stored_bytes"], ", stopped" if wj["stopped"] else ""))
    return wj


def request_stop():
    STOP_FLAG.set()
    if STOP_EVENT[0] is not None:
        STOP_EVENT[0].set()


async def serve_main(root=None, asset="btc", windows=None):
    """The service's loop. `windows` bounds the number of windows; None in the service."""
    root = ROOT if root is None else root
    loop = asyncio.get_running_loop()
    STOP_EVENT[0] = asyncio.Event()
    for sig in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(sig, request_stop)
    try:
        free = guard_resources()
    except FloorStop as exc:
        out("refusing to start: %s" % exc)
        return 1
    os.makedirs(root, exist_ok=True)
    if acquire_single_instance(root) is None:
        return 3
    store = {"stream_bytes": stream_bytes_total(root)}
    rec = runtime_record(root, "start", {"free_bytes": free, "stream_bytes": store["stream_bytes"]})
    out("start record: pid %d commit %s file_sha256 %s; free %d bytes, streams %d bytes" % (
        rec["pid"], rec["commit"], rec["file_sha256"], free, store["stream_bytes"]))
    rc, done = 0, 0
    try:
        while not stopping() and (windows is None or done < windows):
            T, late = next_window(time.time())
            if late and not joinable(os.path.join(root, str(T))):
                out("window %d already closed by an earlier process: not rejoined" % T)
                await sleep_until(T + CLOSE_OFFSET)
                continue
            try:
                await run_window(T, late, store, asset, root)
                done += 1
            except FloorStop as exc:
                rc = 1
                runtime_record(root, "halt", {"T": T, "reason": str(exc)})
                out("halt: %s" % exc)
                break
            except GuardError:
                rc = 1
                raise
            except Exception as exc:
                runtime_record(root, "error", {"T": T, "error": "%s: %s" % (type(exc).__name__, str(exc)[:300])})
                out("window %d error: %r" % (T, exc))
                await sleep_until(T + CLOSE_OFFSET)
    finally:
        runtime_record(root, "stop", {"counters": dict(COUNTERS), "code": rc})
        out("stop record written; requests %d, sessions %d, frames %d, stream bytes %d, other bytes %d" % (
            COUNTERS["requests"], COUNTERS["sessions"], COUNTERS["frames"], COUNTERS["stream_bytes"],
            COUNTERS["bytes_written"]))
    return rc


def mode_serve():
    try:
        with open("/proc/self/cmdline", "rb") as fh:
            mine = fh.read()
    except OSError:
        mine = b""
    if not same_service(mine, SERVICE_ARGV):
        out("refuses to serve: /proc/self/cmdline %r is not %r; nothing written" % (
            mine.decode("utf-8", "replace").replace("\x00", " "), list(SERVICE_ARGV)))
        return 2
    return asyncio.run(serve_main())

# ---- reading what the service stored: total, it never raises on data ------------------------------


def stream_rows(path, report):
    """Every complete line of a stream file, parsed, read incrementally in pieces of at most 4 MiB;
    `report` gets `torn` - cut before its trailer, or with bytes past it - and `bad`, the lines that do
    not parse."""
    d = zlib.decompressobj(16 + zlib.MAX_WBITS)
    buf, torn = b"", False
    with open(path, "rb") as fh:
        pending = b""
        while True:
            if not pending:
                pending = fh.read(1 << 16)
                if not pending:
                    break
            try:
                data = d.decompress(pending, 1 << 22)
            except zlib.error:
                torn = True
                break
            pending = d.unconsumed_tail
            buf += data
            lines = buf.split(b"\n")
            buf = lines.pop()
            for ln in lines:
                try:
                    yield json.loads(ln)
                except ValueError:
                    report["bad"] += 1
            if d.eof:
                if d.unused_data or pending or fh.read(1):
                    torn = True
                break
    if not d.eof or buf:
        torn = True
    report["torn"] = report["torn"] or torn


def counted_quantiles(counter):
    """min, the nearest-rank median, p99 and max of the values a Counter counts, or None where empty."""
    n = sum(counter.values())
    if not n:
        return None
    keys = sorted(counter)
    res, seen = {"n": n, "min": keys[0], "max": keys[-1]}, 0
    marks = {"median": (n - 1) // 2, "p99": (n * 99) // 100}
    for k in keys:
        lo, seen = seen, seen + counter[k]
        for name, idx in marks.items():
            if lo <= idx < seen:
                res[name] = k
    return {k: res[k] for k in ("n", "min", "median", "p99", "max")}


def frame_tokens(obj):
    """The event types and token ids a parsed frame names, and the venue time of a price_change, or
    None where the frame does not conform to the documented market channel."""
    items = obj if isinstance(obj, list) else [obj]
    if not items:
        return None
    types, toks, ts = [], set(), None
    for it in items:
        if not isinstance(it, dict):
            return None
        et = it.get("event_type")
        if et not in KNOWN:
            return None
        if et == "price_change":
            pcs = it.get("price_changes")
            if not isinstance(pcs, list) or not pcs:
                return None
            for pc in pcs:
                if not (isinstance(pc, dict) and isinstance(pc.get("asset_id"), str)):
                    return None
                toks.add(pc["asset_id"])
            t = it.get("timestamp")
            if isinstance(t, str) and t.isascii() and t.isdigit():
                ts = int(t)
        else:
            if not isinstance(it.get("asset_id"), str):
                return None
            toks.add(it["asset_id"])
        types.append(et)
    return types, toks, ts


def stream_unit(T, wdir, wj, tokens15, tokens5):
    """G-STREAM's unit: the reasons a window's stream is not complete, none where it is, and its counts.
    Reads a frame for its JSON shape, event types, token ids and the venue's time, and nothing else."""
    st = wj.get("stream") if isinstance(wj, dict) else None
    if not isinstance(st, dict) or frozenset(st) != STREAM_KEYS:
        return ["window.json"], {}
    why = []
    if not wj.get("documents_ok"):
        why.append("documents")
    if wj.get("joined_late"):
        why.append("joined late")
    if wj.get("stopped"):
        why.append("stopped")
    if not st["opened"] or not st["files"]:
        why.append("no stream (%s)" % st["off_reason"])
        return why, {}
    m15, m5 = set(tokens15), set(tokens5)
    four = m15 | m5
    s = {"files": len(st["files"]), "frames": 0, "pongs": 0, "frames_m15": 0, "frames_m5": 0, "bytes_m15": 0,
         "bytes_m5": 0, "nonconforming": 0, "foreign": 0, "torn": 0, "bad_lines": 0, "stored_bytes": 0,
         "subscribes": 0, "closes": 0, "pings": 0, "max_gap_ns": None, "subscribe_offset_ms": None,
         "last_close_offset_ms": None, "lag_ms": None}
    lags, early, sub0, last, end = {}, set(), None, None, None
    gap = 0
    for name in st["files"]:
        p = os.path.join(wdir, name)
        if not os.path.isfile(p):
            why.append("missing %s" % name)
            continue
        s["stored_bytes"] += os.path.getsize(p)
        rep = {"torn": False, "bad": 0}
        ended = False
        for r in stream_rows(p, rep):
            ended = False
            if not isinstance(r, dict) or type(r.get("recv_ns")) is not int:
                s["bad_lines"] += 1
                continue
            t = r["recv_ns"]
            ev = r.get("event")
            if ev is not None:
                if ev == "subscribe":
                    s["subscribes"] += 1
                    if sub0 is None:
                        sub0 = t
                elif ev == "close":
                    s["closes"] += 1
                    end = t
                elif ev == "ping":
                    s["pings"] += 1
                elif ev == "end":
                    ended = True
                if ev in ("subscribe", "close") and last is not None:
                    gap = max(gap, t - last)
                if ev in ("subscribe", "close") and sub0 is not None:
                    last = t
                continue
            keys = frozenset(r)
            if keys == FRAME_B64_KEYS:
                s["nonconforming"] += 1
            elif keys != FRAME_KEYS or not isinstance(r["raw"], str):
                s["bad_lines"] += 1
                continue
            s["frames"] += 1
            if sub0 is not None:
                if last is not None:
                    gap = max(gap, t - last)
                last = t
            if keys == FRAME_B64_KEYS:
                continue
            raw = r["raw"]
            if raw == "PONG":
                s["pongs"] += 1
                continue
            try:
                obj = json.loads(raw)
            except ValueError:
                s["nonconforming"] += 1
                continue
            got = frame_tokens(obj)
            if got is None:
                s["nonconforming"] += 1
                continue
            types, toks, ts = got
            if not toks <= four:
                s["foreign"] += 1
            n = len(raw.encode("utf-8"))
            if toks <= m15:
                s["frames_m15"] += 1
                s["bytes_m15"] += n
            elif toks <= m5:
                s["frames_m5"] += 1
                s["bytes_m5"] += n
            if ts is not None:
                lag = min(max(t // 1000000 - ts, LAG_RANGE_MS[0]), LAG_RANGE_MS[1])
                lags[lag] = lags.get(lag, 0) + 1
            if "book" in types and sub0 is not None and t <= sub0 + INITIAL_S * 10 ** 9:
                for it in (obj if isinstance(obj, list) else [obj]):
                    if it.get("event_type") == "book":
                        early.add(it["asset_id"])
        s["torn"] += 1 if rep["torn"] else 0
        s["bad_lines"] += rep["bad"]
        if not ended:
            why.append("no end line in %s" % name)
    for k, flag in (("torn", "torn"), ("bad_lines", "bad lines"), ("nonconforming", "nonconforming frames"),
                    ("foreign", "foreign tokens")):
        if s[k]:
            why.append(flag)
    if sub0 is None:
        why.append("no subscribe")
    else:
        s["subscribe_offset_ms"] = (sub0 - T * 10 ** 9) // 1000000
        if sub0 > (T + SUBSCRIBE_BY) * 10 ** 9:
            why.append("late subscribe")
        if not four <= early:
            why.append("initial books")
        s["max_gap_ns"] = gap
        if gap > GAP_MAX_NS:
            why.append("gap")
    if end is None or end < (T + END_BY) * 10 ** 9:
        why.append("short")
    if end is not None:
        s["last_close_offset_ms"] = (end - T * 10 ** 9) // 1000000
    if s["frames"] != st["frames"]:
        why.append("count")
    s["lag_ms"] = counted_quantiles(lags)
    return why, s


def books_of(wdir):
    """The window's stored checkpoint reads grouped by tau', or None where the file is unreadable."""
    p = os.path.join(wdir, "books.jsonl.gz")
    if not os.path.isfile(p):
        return None
    try:
        with gzip.open(p, "rb") as fh:
            text = fh.read().decode("utf-8")
        lines = [json.loads(ln) for ln in text.split("\n") if ln]
    except (OSError, EOFError, ValueError, zlib.error):
        return None
    by = {}
    for ln in lines:
        if isinstance(ln, dict):
            by.setdefault(ln.get("tau_prime"), []).append(ln)
    return by


def read_g_stream(units):
    """units: whether each of the first qualifying windows is complete, in order."""
    if len(units) < GATE_WINDOWS:
        return "UNDECIDABLE"
    return "PASS" if sum(1 for u in units[:GATE_WINDOWS] if u) >= GATE_STREAM_PASS else "FAIL"


def read_g_books(n_checkpoints, n_complete):
    if n_checkpoints < GATE_CHECKPOINTS:
        return "UNDECIDABLE"
    return "PASS" if n_complete >= GATE_BOOKS_PASS else "FAIL"


def read_g_tierc(rows):
    """rows: (fully loaded, counted, quotes_complete) per exposed interval."""
    if any(c and q is not True for _f, c, q in rows):
        return "FAIL"
    if sum(1 for f, c, q in rows if f and c and q is True) >= TIERC_MIN:
        return "PASS"
    return "UNDECIDABLE"


def comb(n, k):
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c


def p_fail_at_least(n, k, p):
    """P(at least k of n independent units fail, each with probability p), exact."""
    return sum(comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


def p_false_alarm(f, m, units):
    if m == 0:
        return None
    return 1 - (1 - Fraction(f, m)) ** units


def decimals(fr, places=10):
    if fr is None:
        return None
    scale = 10 ** places
    q, r = divmod(fr.numerator * scale, fr.denominator)
    if 2 * r >= fr.denominator:
        q += 1
    s = str(q).rjust(places + 1, "0")
    return s[:-places] + "." + s[-places:]

# ---- the modes -----------------------------------------------------------------------------------


ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"`?([0-9a-f]{64}|self-reference[^|]*?)`? \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)


def mode_fingerprint():
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
        out("%-44s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, "
        "tracked %d, reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"],
                                     states["tracked"], states["reported"]))


def systemctl_show(unit, props):
    args = ["systemctl", "show", unit]
    for prop in props:
        args += ["-p", prop]
    cp = subprocess.run(args, capture_output=True, text=True)
    assert cp.returncode == 0, "systemctl show %s: %s" % (unit, cp.stderr.strip())
    return dict(line.split("=", 1) for line in cp.stdout.split("\n") if "=" in line)


def systemctl_word(verb, unit):
    cp = subprocess.run(["systemctl", verb, unit], capture_output=True, text=True)
    return cp.stdout.strip()


def mode_still():
    st = load_state()
    now = {}
    for key, unit in sorted(UNITS.items()):
        try:
            kv = systemctl_show(unit, ["MainPID", "NRestarts", "ActiveState", "MemoryCurrent", "MemoryPeak"])
        except AssertionError as exc:
            if key == "recorder":
                raise
            out("%s unread: %s" % (unit, exc))
            continue
        now[key] = {k: kv.get(k) for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, MemoryCurrent %s, MemoryPeak %s" % (unit, now[key], kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "recorder": now["recorder"]}
        save_state(st)
        out("still: the recorder recorded")
        return
    same = now["recorder"] == st["still"]["recorder"]
    out("G-STILL %s: the recorder %s since %s" % ("PASS" if same else "FAIL", "unchanged" if same else "changed",
                                                  st["still"]["at"]))
    assert same, "G-STILL FAIL: the recorder's unit %r, then %r" % (st["still"]["recorder"], now["recorder"])


def mode_mark(name):
    assert name in ("stop-cb", "start-svc", "kill-svc", "restore"), "mark %r" % name
    st = load_state()
    marks = st.setdefault("marks", {})
    assert name not in marks, "mark %s already taken" % name
    unit = UNITS["chainbook"] if name in ("stop-cb", "restore") else UNIT
    kv = systemctl_show(unit, ["MainPID", "NRestarts", "ActiveState"])
    marks[name] = {"ns": time.time_ns(), "unit": unit, "MainPID": kv.get("MainPID"), "NRestarts": kv.get("NRestarts"),
                   "ActiveState": kv.get("ActiveState")}
    save_state(st)
    out("mark %s at %s: %s %r" % (name, utc(marks[name]["ns"] / 1e9), unit, marks[name]))


def read_runtime(path):
    recs = []
    with open(path, "rb") as fh:
        for ln in fh.read().split(b"\n"):
            if ln.strip():
                recs.append(json.loads(ln))
    return recs


def mode_chainbook():
    """G-CB-STOP: the chain book stopped through systemd, disabled, no process left, and its own record
    ending in a stop of the MainPID the mark read, at or after the mark."""
    st = load_state()
    mark = st.get("marks", {}).get("stop-cb")
    assert mark is not None, "chainbook: no stop-cb mark"
    active = systemctl_word("is-active", UNITS["chainbook"])
    enabled = systemctl_word("is-enabled", UNITS["chainbook"])
    procs = processes_with(CHAINBOOK_ARGV)
    recs = read_runtime(CHAINBOOK + "/runtime.jsonl")
    last = recs[-1]
    stop_s = last.get("wall_ns", 0) / 1e9
    phase = int(stop_s) % WINDOW
    out("chain book: is-active %s, is-enabled %s, processes %r; %d runtime records, the last %s of pid %s at %s, "
        "%d s into its window, %s" % (active, enabled, procs, len(recs), last.get("event"), last.get("pid"), utc(stop_s),
                                      phase, "inside its idle stretch" if 5 <= phase < 625 else "inside a window"))
    checks = {"inactive": active in ("inactive", "failed"), "disabled": enabled == "disabled",
              "no process": procs == [],
              "stop record": last.get("event") == "stop" and str(last.get("pid")) == str(mark["MainPID"])
              and last.get("wall_ns", 0) >= mark["ns"]}
    for k, v in checks.items():
        out("G-CB-STOP %-12s %s" % (k, v))
    assert all(checks.values()), "G-CB-STOP FAIL: %r" % checks
    out("G-CB-STOP PASS: stopped at %s, its MainPID %s, the mark at %s" % (utc(stop_s), mark["MainPID"],
                                                                         utc(mark["ns"] / 1e9)))


def mode_restored():
    """After K-26 and B-RESTORE-CB: the pair book stopped through systemd, disabled, no process left, its own
    record ending in a stop; the chain book active, enabled, one process under its argv, and its own record
    ending in a start after the restore mark."""
    st = load_state()
    mark = st.get("marks", {}).get("restore")
    assert mark is not None, "restored: no restore mark"
    pb = read_runtime(ROOT + "/runtime.jsonl")
    cb = read_runtime(CHAINBOOK + "/runtime.jsonl")
    checks = {"pair book inactive": systemctl_word("is-active", UNIT) in ("inactive", "failed"),
              "pair book disabled": systemctl_word("is-enabled", UNIT) == "disabled",
              "pair book no process": processes_with(SERVICE_ARGV) == [],
              "pair book stop record": bool(pb) and pb[-1].get("event") == "stop",
              "chain book active": systemctl_word("is-active", UNITS["chainbook"]) == "active",
              "chain book enabled": systemctl_word("is-enabled", UNITS["chainbook"]) == "enabled",
              "chain book one process": len(processes_with(CHAINBOOK_ARGV)) == 1,
              "chain book start record": bool(cb) and cb[-1].get("event") == "start" and cb[-1].get("wall_ns", 0) >= mark["ns"]
              and [cb[-1].get("pid")] == processes_with(CHAINBOOK_ARGV)}
    for k, v in checks.items():
        out("RESTORED %-24s %s" % (k, v))
    assert all(checks.values()), "RESTORED FAIL: %r" % {k: v for k, v in checks.items() if not v}
    out("RESTORED PASS: the pair book stopped at %s; the chain book started as pid %s at %s" % (
        utc(pb[-1]["wall_ns"] / 1e9), cb[-1]["pid"], utc(cb[-1]["wall_ns"] / 1e9)))


def unit_reads(n_restarts):
    kv = systemctl_show(UNIT, ["ActiveState", "SubState", "UnitFileState", "FragmentPath", "ControlGroup",
                               "MemoryMax", "NRestarts", "MainPID", "MemoryCurrent", "MemoryPeak"])
    pid = int(kv["MainPID"])
    with open("/proc/%d/cmdline" % pid, "rb") as fh:
        cmd = fh.read()
    cwd = os.readlink("/proc/%d/cwd" % pid)
    with open("/proc/%d/cgroup" % pid, encoding="utf-8") as fh:
        cg = fh.read()
    checks = {"active": kv["ActiveState"] == "active" and kv["SubState"] == "running",
              "enabled": kv["UnitFileState"] == "enabled",
              "fragment": kv["FragmentPath"] == "/etc/systemd/system/" + UNIT,
              "control group": kv["ControlGroup"] == "/system.slice/" + UNIT,
              "ceiling": kv["MemoryMax"] == str(MEMORY_MAX),
              "restarts": kv["NRestarts"] == str(n_restarts),
              "argv": same_service(cmd, SERVICE_ARGV), "cwd": cwd == SVC,
              "cgroup": ("/system.slice/" + UNIT) in cg and "/user.slice" not in cg,
              "sole instance": processes_with(SERVICE_ARGV) == [pid]}
    return kv, checks, pid


def svc_blob():
    with open(SERVICE_FILE, "rb") as fh:
        return sha256_bytes(fh.read())


def mode_unit(n):
    kv, checks, pid = unit_reads(n)
    if n == 0:
        st = load_state()
        mark = st.get("marks", {}).get("start-svc")
        assert mark is not None, "unit 0: no start-svc mark"
        starts = [r for r in read_runtime(ROOT + "/runtime.jsonl") if r.get("event") == "start"]
        first = starts[0] if starts else {}
        checks.update({
            "one start": len(starts) == 1, "start pid": first.get("pid") == pid,
            "start after mark": first.get("wall_ns", 0) >= mark["ns"],
            "commit": first.get("commit") == read_commit(SVC) and isinstance(first.get("commit"), str)
            and re.fullmatch(r"[0-9a-f]{40}", first.get("commit") or "") is not None,
            "file": first.get("file_sha256") == svc_blob(),
            "start argv": first.get("argv") == list(SERVICE_ARGV[3:]),
            "headers": first.get("config", {}).get("headers") == [["Accept", ACCEPT], ["User-Agent", UA]]})
        out("G-START: the start record of pid %s at %s, commit %s, file %s" % (
            first.get("pid"), utc(first.get("wall_ns", 0) / 1e9), first.get("commit"), first.get("file_sha256")))
    for k, v in checks.items():
        out("G-UNIT %-16s %s" % (k, v))
    out("%s MainPID %d, NRestarts %s, MemoryMax %s, MemoryCurrent %s, MemoryPeak %s" % (
        UNIT, pid, kv["NRestarts"], kv["MemoryMax"], kv["MemoryCurrent"], kv["MemoryPeak"]))
    assert all(checks.values()), "G-UNIT FAIL: %r" % {k: v for k, v in checks.items() if not v}
    out("G-UNIT PASS at %d restarts%s" % (n, "; G-START PASS" if n == 0 else ""))


def mode_restart():
    """G-RESTART: since the kill mark, the records are a stop of the marked MainPID and a start of
    another, within RESTART_MAX_S, on the same commit and file; G-UNIT at one restart."""
    st = load_state()
    mark = st.get("marks", {}).get("kill-svc")
    assert mark is not None, "restart: no kill-svc mark"
    recs = read_runtime(ROOT + "/runtime.jsonl")
    after = [r for r in recs if r.get("wall_ns", 0) >= mark["ns"]]
    for r in after:
        out("record %s pid %s at %s" % (r.get("event"), r.get("pid"), utc(r["wall_ns"] / 1e9)))
    ok = (len(after) == 2 and after[0].get("event") == "stop" and str(after[0].get("pid")) == str(mark["MainPID"])
          and after[1].get("event") == "start" and after[1].get("pid") != after[0].get("pid")
          and after[1]["wall_ns"] - after[0]["wall_ns"] <= RESTART_MAX_S * 10 ** 9
          and after[1].get("commit") == recs[0].get("commit") and after[1].get("file_sha256") == recs[0].get("file_sha256"))
    assert ok, "G-RESTART FAIL: the records since the mark are %r" % [(r.get("event"), r.get("pid")) for r in after]
    out("G-RESTART: the stop of %s, the start of %s %.3f s later" % (
        after[0]["pid"], after[1]["pid"], (after[1]["wall_ns"] - after[0]["wall_ns"]) / 1e9))
    mode_unit(1)
    out("G-RESTART PASS")


def cgroup_memory(cg):
    vals = {}
    for name in ("memory.current", "memory.peak", "memory.swap.current", "memory.swap.peak"):
        try:
            with open(os.path.join(cg, name), encoding="utf-8") as fh:
                vals[name] = fh.read().strip()
        except OSError as exc:
            vals[name] = "unread: %s" % type(exc).__name__
    try:
        with open(os.path.join(cg, "memory.stat"), encoding="utf-8") as fh:
            stat = dict(ln.split() for ln in fh if ln.strip())
        for k in ("anon", "file", "kernel", "sock", "file_dirty", "file_writeback"):
            vals["stat." + k] = stat.get(k)
    except OSError as exc:
        vals["memory.stat"] = "unread: %s" % type(exc).__name__
    return vals


def process_cpu(pid):
    with open("/proc/%d/stat" % pid, encoding="utf-8") as fh:
        f = fh.read().rsplit(")", 1)[1].split()
    hz = os.sysconf("SC_CLK_TCK")
    with open("/proc/stat", encoding="utf-8") as fh:
        btime = int([ln for ln in fh.read().split("\n") if ln.startswith("btime ")][0].split()[1])
    return Fraction(int(f[11]) + int(f[12]), hz), btime + Fraction(int(f[19]), hz)


def mode_load():
    """G-LOAD: the service's processor time since its process started, at most LOAD_MAX of the elapsed
    wall time; its memory printed."""
    kv = systemctl_show(UNIT, ["MainPID", "ControlGroup", "MemoryCurrent", "MemoryPeak"])
    pid = int(kv["MainPID"])
    cpu, began = process_cpu(pid)
    elapsed = Fraction(time.time_ns(), 10 ** 9) - began
    frac = cpu / elapsed
    for k, v in cgroup_memory("/sys/fs/cgroup" + kv["ControlGroup"]).items():
        out("%s %s" % (k, v))
    with open("/proc/%d/status" % pid, encoding="utf-8") as fh:
        for ln in fh:
            if ln.split(":")[0] in ("VmRSS", "VmHWM", "VmSwap", "Threads"):
                out("process %d %s" % (pid, ln.strip()))
    out("G-LOAD: process %d, processor %s s over %s s since %s: %s of one core, bound %s" % (
        pid, decimals(cpu, 2), decimals(elapsed, 1), utc(began), decimals(frac, 4), decimals(LOAD_MAX, 2)))
    assert frac <= LOAD_MAX, "G-LOAD FAIL: %s of one core, above %s" % (decimals(frac, 4), decimals(LOAD_MAX, 2))
    out("G-LOAD PASS")


def mode_final():
    mode_unit(1)
    mode_still()
    kv = systemctl_show(UNIT, ["MainPID", "ControlGroup"])
    for k, v in cgroup_memory("/sys/fs/cgroup" + kv["ControlGroup"]).items():
        out("%s %s" % (k, v))
    out("FINAL PASS")


def considered(T, s, a):
    return T + JOIN_LAST >= s and T + CLOSE_OFFSET <= a


def qualifies(T, s, a):
    return T + DOC_OFFSET >= s + QUALIFY_LEAD_S and T + CLOSE_OFFSET <= min(a, s + BUDGET_S)


def manifest_of(T0, a):
    """A five-minute interval's manifest as of a: (counted, quotes_complete, complete, Tier C offsets)."""
    p = "%s/btc-updown-5m/%d/manifest.json" % (RECORDER, T0)
    try:
        st = os.stat(p)
    except OSError:
        return False, None, None, []
    if st.st_mtime_ns > a * 10 ** 9:
        return False, None, None, []
    with open(p, "rb") as fh:
        m = json.loads(fh.read())
    offs = [q.get("offset_ms") for q in m.get("quote_offsets_ms", []) if isinstance(q, dict)
            and isinstance(q.get("offset_ms"), (int, float))]
    return True, m.get("quotes_complete"), m.get("complete"), offs


def window_row(t, q, a):
    """One considered window, read: its row, and the unit, the complete checkpoints and the exposed
    interval it contributes where it qualifies."""
    wdir = os.path.join(ROOT, str(t))
    row = {"T": t, "qualifying": q}
    by = books_of(wdir) or {}
    cks = []
    for off in CHECKPOINT_OFFSETS:
        ents = by.get(WINDOW - off, [])
        okc, whyc = checkpoint_is_complete(ents)
        cks.append({"tau_prime": WINDOW - off, "complete": okc, "why": whyc,
                    "statuses": [e.get("status") for e in ents], "skew_ns": skew_of(ents)})
    row["checkpoints"] = cks
    n_ok = sum(1 for c in cks if c["complete"])
    counted, qc, comp, offs = manifest_of(t + 600, a)
    trow = {"E": t + 600, "fully_loaded": False, "counted": counted, "quotes_complete": qc, "complete": comp,
            "offsets_ms": quantiles(offs)}
    wjp = os.path.join(wdir, "window.json")
    if not os.path.isfile(wjp):
        row["why"] = ["no window.json"]
        return row, False, n_ok, trow
    try:
        with open(wjp, "rb") as fh:
            wj = json.loads(fh.read())
    except ValueError:
        wj = None
    if not isinstance(wj, dict):
        row["why"] = ["window.json unreadable"]
        return row, False, n_ok, trow
    mk = wj.get("markets") if isinstance(wj.get("markets"), dict) else {}
    toks = []
    for m in ("m15", "m5"):
        ids = parse_maybe_string((mk.get(m) or {}).get("clobTokenIds"))
        toks.append([str(x) for x in ids] if isinstance(ids, list) else [])
    why, stats = stream_unit(t, wdir, wj, toks[0], toks[1])
    st = wj.get("stream") if isinstance(wj.get("stream"), dict) else {}
    row.update({"why": why, "stream": stats, "checkpoints_complete": wj.get("checkpoints_complete"),
                "missed": wj.get("missed"), "documents_ok": wj.get("documents_ok"),
                "document_attempts": wj.get("document_attempts"), "joined_late": wj.get("joined_late"),
                "stream_opened": st.get("opened"), "stream_off": st.get("off_reason"),
                "stored_bytes_window": sum(os.path.getsize(os.path.join(wdir, n)) for n in sorted(os.listdir(wdir)))})
    trow["fully_loaded"] = (bool(st.get("opened")) and stats.get("subscribe_offset_ms") is not None
                            and stats["subscribe_offset_ms"] <= SUBSCRIBE_BY * 1000 and "short" not in why
                            and all(len(c["statuses"]) == 4 and None not in c["statuses"] for c in cks))
    return row, not why, n_ok, trow


def mode_prove(a):
    floor_check()
    starts = [r for r in read_runtime(ROOT + "/runtime.jsonl") if r.get("event") == "start"]
    assert starts, "prove: no start record"
    s = starts[0]["wall_ns"] / 1e9
    assert s <= a <= time.time(), "prove: as-of %d outside [%s, now]" % (a, s)
    out("the service's first start: pid %s at %s" % (starts[0]["pid"], utc(s)))
    plan, t = [], (int(s) // WINDOW) * WINDOW - WINDOW
    while t + CLOSE_OFFSET <= a:
        if considered(t, s, a):
            plan.append((t, qualifies(t, s, a) and sum(1 for _t, q in plan if q) < GATE_WINDOWS))
        t += WINDOW
    quals = [t for t, q in plan if q]
    counted_now = sum(1 for t in quals if manifest_of(t + 600, a)[0])
    if (len(quals) < GATE_WINDOWS or counted_now < len(quals)) and a < s + BUDGET_S:
        nxt = int(a) + 300
        out("NOT YET: %d of %d qualifying windows closed, %d of %d exposed manifests counted, as of %d; run again "
            "at or after %d (%s)" % (len(quals), GATE_WINDOWS, counted_now, len(quals), a, nxt, utc(nxt)))
        return 3
    windows, units, ckpts, ckpt_ok, tierc = [], [], 0, 0, []
    for t, q in plan:
        row, unit, n_ok, trow = window_row(t, q, a)
        windows.append(row)
        if q:
            units.append(unit)
            ckpts += len(CHECKPOINT_OFFSETS)
            ckpt_ok += n_ok
            tierc.append(trow)
    g_stream = read_g_stream(units)
    g_books = read_g_books(ckpts, ckpt_ok)
    g_tierc = read_g_tierc([(r["fully_loaded"], r["counted"], r["quotes_complete"]) for r in tierc])
    exposed = {r["E"] for r in tierc}
    control = []
    T0 = (int(s) // 300 + 1) * 300
    while T0 + 330 <= a and T0 <= s + BUDGET_S:
        if T0 not in exposed and T0 % WINDOW != 600:
            counted, qc, comp, offs = manifest_of(T0, a)
            if counted:
                control.append({"T0": T0, "quotes_complete": qc, "complete": comp, "offsets_ms": quantiles(offs)})
        T0 += 300
    for row in windows:
        out("window %d %s qualifying %s: %s; stream %s" % (row["T"], utc(row["T"]), row["qualifying"],
                                                           "complete" if not row.get("why") else row["why"],
                                                           json.dumps(row.get("stream"), sort_keys=True)))
        for c in row.get("checkpoints", []):
            out("  checkpoint tau' %3d: %s %s statuses %s skew_ns %s" % (c["tau_prime"], c["complete"], c["why"],
                                                                      c["statuses"], c["skew_ns"]))
    for r in tierc:
        out("exposed %d %s: fully loaded %s, counted %s, quotes_complete %s, complete %s, Tier C offsets %s" % (
            r["E"], utc(r["E"]), r["fully_loaded"], r["counted"], r["quotes_complete"], r["complete"], r["offsets_ms"]))
    for r in control:
        out("control %d %s: quotes_complete %s, complete %s, Tier C offsets %s" % (
            r["T0"], utc(r["T0"]), r["quotes_complete"], r["complete"], r["offsets_ms"]))
    proof = {"mode": "prove", "as_of": a, "start": {"pid": starts[0]["pid"], "wall_ns": starts[0]["wall_ns"],
                                                    "commit": starts[0].get("commit"),
                                                    "file_sha256": starts[0].get("file_sha256")},
             "windows": windows, "g_stream": {"units": units, "reading": g_stream},
             "g_books": {"checkpoints": ckpts, "complete": ckpt_ok, "reading": g_books},
             "g_tierc": {"rows": tierc, "reading": g_tierc}, "control": control,
             "counters": {"requests": COUNTERS["requests"], "sessions": COUNTERS["sessions"]}}
    assert_keys(proof, PROOF_JSON_KEYS, "proof.json")
    assert COUNTERS["requests"] == 0 and COUNTERS["sessions"] == 0, "prove made a request"
    os.makedirs(os.path.join(WORK, "proof"), exist_ok=True)
    path = os.path.join(WORK, "proof", "proof-%d.json" % a)
    body = json_line(proof)
    if os.path.exists(path):
        assert sha256_file(path) == sha256_bytes(body), "prove: %s differs from the first run" % path
        out("unchanged %s sha256 %s" % (path, sha256_bytes(body)))
    else:
        with open(path, "xb") as fh:
            fh.write(body)
        out("wrote %s sha256 %s, %d bytes" % (path, sha256_bytes(body), len(body)))
    out("READING G-STREAM: %s, %d of %d complete" % (g_stream, sum(1 for u in units if u), len(units)))
    out("READING G-BOOKS: %s, %d of %d checkpoints complete" % (g_books, ckpt_ok, ckpts))
    out("READING G-TIERC: %s, %d counted fully loaded exposed intervals with quotes_complete true" % (
        g_tierc, sum(1 for r in tierc if r["fully_loaded"] and r["counted"] and r["quotes_complete"] is True)))
    return 0


def base_rate(p, span_s=BASE_RATE_S, step=300):
    """The T0 of every five-minute interval closing in [p - span_s, p)."""
    return list(range(p - span_s - step, p - step, step))


async def prestart_session(wdir, tokens, seconds):
    stats = new_stream_stats()
    STOP_FLAG.clear()
    t0 = time.time()
    await stream_window(wdir, tokens, t0, t0 + seconds, stats)
    return stats


def mode_prestart():
    """CANON hard rule 14's proof, on the ETH nested pair: two documents and one book through http_get, one
    stream session through stream_window; the processes; G-TIERC's base rate. Prints counts only."""
    floor_check()
    with open(os.path.abspath(__file__), "rb") as fh:
        own = sha256_bytes(fh.read())
    out("file %s sha256 %s" % (os.path.abspath(__file__), own))
    proxies = sorted(k for k in os.environ if k.lower() in ("http_proxy", "https_proxy", "all_proxy"))
    out("free %d bytes at %s; proxy variables in the environment: %d" % (free_bytes(), DISK_PATH, len(proxies)))
    procs = {"service": processes_with(SERVICE_ARGV), "chainbook": processes_with(CHAINBOOK_ARGV)}
    out("processes: the service's argv %r, the chain book's %r" % (procs["service"], procs["chainbook"]))
    assert procs["service"] == [], "prestart: an instance of the service already runs"
    p = int(time.time()) // 300 * 300
    slots = base_rate(p)
    m = f = 0
    t_scan = time.monotonic()
    for k, T0 in enumerate(slots):
        if k == 100:
            assert time.monotonic() - t_scan <= 30, "prestart: the base-rate scan's first 100 slots took over 30 s"
        try:
            with open("%s/btc-updown-5m/%d/manifest.json" % (RECORDER, T0), "rb") as fh:
                mm = json.loads(fh.read())
        except OSError:
            continue
        m += 1
        f += 0 if mm.get("quotes_complete") is True else 1
    fa = p_false_alarm(f, m, FA_UNITS)
    out("base rate: %d slots, %d manifests read, %d without quotes_complete true; G-TIERC's false alarm "
        "1 - (1 - f/m)^4 = %s = %s" % (len(slots), m, f, fa, decimals(fa)))
    now = time.time()
    T = int(now) // WINDOW * WINDOW
    if now > T + 840:
        T += WINDOW
    slugs = {"m15": slug15(T, "eth"), "m5": slug5(T + 600, "eth")}
    reqs, toks = [], {}
    for k in ("m15", "m5"):
        res = http_get(GAMMA_MARKET_URL.format(slug=slugs[k]))
        ids = None
        if res["status"] == 200:
            try:
                ids = token_ids_of(res["raw"])[0]
            except ValueError:
                ids = None
        assert res["status"] == 200 and res["bytes"] > 0 and ids is not None, \
            "prestart: %s %s, %d bytes" % (slugs[k], res["status"], res["bytes"])
        toks[k] = ids
        reqs.append({"method": "GET", "url": res["url"], "headers": [["Accept", ACCEPT], ["User-Agent", UA]],
                     "status": res["status"], "bytes": res["bytes"], "sha256": res["sha256"], "parses_json": True,
                     "elapsed_ns": res["recv_mono_ns"] - res["send_mono_ns"], "token_ids": ids})
        time.sleep(DOC_GAP_S)
    res = http_get(CLOB_BOOK_URL.format(token_id=toks["m15"][0]))
    try:
        json.loads(res["raw"])
        pj = True
    except ValueError:
        pj = False
    assert res["status"] == 200 and res["bytes"] > 0 and pj, "prestart: the book %s, %d bytes" % (res["status"], res["bytes"])
    reqs.append({"method": "GET", "url": res["url"], "headers": [["Accept", ACCEPT], ["User-Agent", UA]],
                 "status": res["status"], "bytes": res["bytes"], "sha256": res["sha256"], "parses_json": pj,
                 "elapsed_ns": res["recv_mono_ns"] - res["send_mono_ns"]})
    assert COUNTERS["requests"] == 3, "prestart: %d requests" % COUNTERS["requests"]
    for name in ("prestart", "prestart-2"):
        d = os.path.join(WORK, name)
        if not os.path.exists(d):
            break
    else:
        raise AssertionError("prestart: prestart and prestart-2 both exist")
    os.makedirs(d)
    tokens = toks["m15"] + toks["m5"]
    stats = asyncio.run(prestart_session(d, tokens, 25))
    wj = {"documents_ok": True, "joined_late": False, "stopped": False, "stream": stats}
    why, sst = stream_unit(T, d, wj, toks["m15"], toks["m5"])
    path = os.path.join(d, "stream.jsonl.gz")
    rep = {"torn": False, "bad": 0}
    opens = [r for r in stream_rows(path, rep) if isinstance(r, dict) and r.get("event") == "open"]
    checks = {"one session": stats["segments"] == 1 and COUNTERS["sessions"] == 1,
              "101": len(opens) == 1 and opens[0].get("status") == 101 and opens[0].get("extensions") is None,
              "subscribed": stats["subscribed_wall_ns"] is not None,
              "initial books": "initial books" not in why,
              "heartbeat": stats["pongs"] >= 1 and stats["pings"] >= 2,
              "conforming": not ({"nonconforming frames", "foreign tokens", "bad lines", "torn", "count"} & set(why)),
              "whole file": not rep["torn"] and rep["bad"] == 0 and "no end line in stream.jsonl.gz" not in why}
    for k, v in checks.items():
        out("P-START %-14s %s" % (k, v))
    out("the session: %d frames, %d frame bytes, %d pongs, %d pings, %d stored bytes, largest gap %s ns, "
        "frames m15 %s m5 %s" % (stats["frames"], stats["frame_bytes"], stats["pongs"], stats["pings"],
                                 stats["stored_bytes"], sst.get("max_gap_ns"), sst.get("frames_m15"), sst.get("frames_m5")))
    doc = {"mode": "prestart", "p_wall": p, "file_sha256": own, "processes": procs, "proxy_variables": len(proxies),
           "base_rate": {"slots": len(slots), "manifests": m, "f": f, "false_alarm": str(fa) if fa is not None else None,
                         "false_alarm_decimal": decimals(fa)},
           "requests": reqs, "stream": {"slugs": slugs, "tokens": tokens, "stats": stats, "checks": checks,
                                        "frames_m15": sst.get("frames_m15"), "frames_m5": sst.get("frames_m5")},
           "counters": {"requests": COUNTERS["requests"], "sessions": COUNTERS["sessions"]}}
    assert_keys(doc, PRESTART_JSON_KEYS, "prestart.json")
    body = json_line(doc)
    with open(os.path.join(d, "prestart.json"), "xb") as fh:
        fh.write(body)
    out("wrote %s sha256 %s" % (os.path.join(d, "prestart.json"), sha256_bytes(body)))
    out("wrote %s sha256 %s, %d bytes" % (path, sha256_file(path), os.path.getsize(path)))
    assert all(checks.values()), "P-START FAIL: %r" % {k: v for k, v in checks.items() if not v}
    out("READING P-START: served")


def proc_start_times():
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
    """Kept whatever a report prints: the state, the logs, the request-path proof and the proofs."""
    return tree == WORK and (rel == "state.json" or rel.startswith("logs/") or rel.startswith("prestart")
                             or rel.startswith("proof/"))


def pristine(tree):
    cp = subprocess.run(["git", "-C", tree, "status", "--porcelain", "--ignored"], capture_output=True, text=True)
    assert cp.returncode == 0 and cp.stdout == "", "reclaim: %s holds %r" % (tree, cp.stdout[:400])
    head = subprocess.run(["git", "-C", tree, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
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
            assert not [p for p, s, _a in procs if s - 1 <= b <= s + LIVE_S], "reclaim: %s belongs to a running process" % t
    tokens = report_tokens()
    lengths = sorted({len(t) for t in tokens})
    before = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    out("reclaim: %d report tokens; forensic store holds %d files" % (len(tokens), before))
    considered_n = named = kept = copied = held = 0
    for tree in trees:
        if tree == WORK and os.path.isdir(WT):
            pristine(WT)
        for dirpath, dirnames, filenames in os.walk(tree):
            dirnames[:] = sorted(d for d in dirnames if os.path.join(dirpath, d) != WT)
            for name in sorted(filenames):
                path = os.path.join(dirpath, name)
                if os.path.islink(path) or not os.path.isfile(path):
                    continue
                considered_n += 1
                rel = os.path.relpath(path, tree)
                h = sha256_file(path)
                is_named = any(h[:k] in tokens for k in lengths)
                is_kept = by_name(tree, rel)
                if not (is_named or is_kept):
                    continue
                named += 1 if is_named else 0
                kept += 1 if is_kept and not is_named else 0
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--" + rel.replace("/", "--"))
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
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, %d already held; "
        "forensic store %d -> %d files" % (considered_n, named, kept, copied, held, before, after))

# ---- the self-test: literals and loopback servers only -------------------------------------------


class _Http(http.server.BaseHTTPRequestHandler):
    seen = []

    def do_GET(self):
        _Http.seen.append((self.requestline, sorted((k.lower(), v) for k, v in self.headers.items())))
        body, code = (b"error code: 1010\n", 403) if self.path.startswith("/refused") else (b"{}", 200)
        self.send_response(code)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


def synth_book(tok, cond):
    return {"event_type": "book", "asset_id": tok, "market": cond, "timestamp": "1791000000000", "hash": "ab" * 20,
            "bids": [{"price": "0.48", "size": "10"}], "asks": [{"price": "0.52", "size": "10"}]}


def synth_change(toks, cond, ms):
    return {"event_type": "price_change", "market": cond, "timestamp": str(ms),
            "price_changes": [{"asset_id": t, "price": "0.5", "size": "1", "side": "BUY", "hash": "cd" * 20,
                               "best_bid": "0.49", "best_ask": "0.51"} for t in toks]}


async def loopback_venue(state, close_first_after=None):
    """A venue on 127.0.0.1: the subscription read, the four books sent as one list frame, a price change
    every 5 ms, one in seven for the second market; PONG to PING; the first connection closed by the
    venue after `close_first_after` seconds."""
    conds = {"m15": "0x" + "1" * 64, "m5": "0x" + "2" * 64}

    async def handler(ws):
        state["connections"] += 1
        k = state["connections"]
        state["headers"].append(sorted((n.lower(), v) for n, v in ws.request.headers.raw_items()))
        msg = await ws.recv()
        state["subs"].append(msg)
        toks = json.loads(msg)["assets_ids"]
        await ws.send(json.dumps([synth_book(t, conds["m15"] if i < 2 else conds["m5"]) for i, t in enumerate(toks)]))

        async def sender():
            n = 0
            while True:
                await asyncio.sleep(0.005)
                n += 1
                if n % 7 == 0:
                    await ws.send(json.dumps(synth_change(toks[2:], conds["m5"], 1791000000000 + n)))
                else:
                    await ws.send(json.dumps(synth_change(toks[:2], conds["m15"], 1791000000000 + n)))

        task = asyncio.create_task(sender())
        closer = None
        try:
            if close_first_after is not None and k == 1:
                async def close_later():
                    await asyncio.sleep(close_first_after)
                    await ws.close(code=1011, reason="test")
                closer = asyncio.create_task(close_later())
            async for m in ws:
                if m == "PING":
                    state["pings"] += 1
                    await ws.send("PONG")
        except websockets.ConnectionClosed:
            pass
        finally:
            task.cancel()
            if closer is not None:
                closer.cancel()

    return await ws_serve(handler, "127.0.0.1", 0, compression=None)


def mode_selftest():
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    # the schedule, against integers computed outside this file
    T = 1791627300
    sch = schedule_for(T)
    ok(sch["document_instant"] == 1791627845 and sch["stream_open"] == 1791627895
       and sch["stream_close"] == 1791628205 and sch["close_instant"] == 1791628210,
       "documents at T+545, the stream T+595 to T+905, window.json at T+910")
    ok([c for c, _t in sch["checkpoints"]] == [1791627955, 1791628015, 1791628075, 1791628105, 1791628135,
                                               1791628165, 1791628185]
       and [t for _c, t in sch["checkpoints"]] == [245, 185, 125, 95, 65, 35, 15],
       "the chain book's seven checkpoints, tau' 245 to 15")
    ok(tierc_instants(T) == [1791627960, 1791628020, 1791628080, 1791628110, 1791628140, 1791628170, 1791628190]
       and not set(tierc_instants(T)) & {c for c, _t in sch["checkpoints"]},
       "Tier C reads the same five-minute market 5 s after each checkpoint, never in its second")
    ok(sch["stream_open"] < T + 600 and sch["stream_close"] > T + 900 and sch["document_instant"] < T + 605,
       "the stream covers the five-minute market's whole window; the documents precede the recorder's S6 at T+605")
    ok(next_window(T + 10) == (T, False) and next_window(T + 545) == (T, False) and next_window(T + 546) == (T, True)
       and next_window(T + 880) == (T, True) and next_window(T + 881) == (T + 900, False)
       and next_window(T + 910) == (T + 900, False) and next_window(T + 899.5) == (T + 900, False),
       "next_window: scheduled to T+545, joined late to T+880, then the next window")
    ok(stream_off_reason(False, 10 ** 10, 0) == "documents" and stream_off_reason(True, STREAM_FLOOR - 1, 0) == "floor"
       and stream_off_reason(True, STREAM_FLOOR, STREAM_CAP) == "cap"
       and stream_off_reason(True, STREAM_FLOOR, STREAM_CAP - 1) is None,
       "the stream opens only with both documents, free at or above the floor, the store below the cap")
    # equality, never a substring
    good = ("\x00".join(SERVICE_ARGV) + "\x00").encode()
    ok(same_service(good, SERVICE_ARGV), "same_service: the exact argv")
    ok(not same_service(("bash\x00-c\x00" + " ".join(SERVICE_ARGV) + "\x00").encode(), SERVICE_ARGV),
       "same_service: a shell carrying the argv as text is not the service")
    ok(not same_service(good + b"--x\x00", SERVICE_ARGV) and not same_service(b"", SERVICE_ARGV),
       "same_service: a sixth field, and nothing, are not the service")
    # the audit policy, as a pure function, and the hook itself
    man = RECORDER + "/btc-updown-5m/1791628200/manifest.json"
    ok(policy("serve", "open", (ROOT + "/1791627300/stream.jsonl.gz", "xb", 0)) is None,
       "serve writes under the pair book's root")
    ok(policy("serve", "open", (WORK + "/x", "wb", 0)) is not None and policy("serve", "open", ("/tmp/x", "wb", 0)) is not None,
       "serve writes nowhere else")
    ok(policy("serve", "subprocess.Popen", ("systemctl",)) is not None and policy("serve", "os.fork", ()) is not None
       and policy("unit", "subprocess.Popen", ("systemctl",)) is None,
       "serve starts no process; the systemd reads may")
    ok(policy("prove", "open", (man, "rb", 0)) is None and policy("prestart", "open", (man, "rb", 0)) is None
       and policy("prove", "open", (man.replace("manifest.json", "quotes.jsonl.gz"), "rb", 0)) is not None
       and policy("prove", "open", (RECORDER + "/runtime.jsonl", "rb", 0)) is not None
       and policy("serve", "open", (man, "rb", 0)) is not None,
       "under the recorder's root only a manifest, read only, by prestart and prove")
    ok(policy("prove", "open", (man, "r+b", 0)) is not None and policy("prove", "os.scandir", (RECORDER + "/btc-updown-5m",)) is not None,
       "no manifest is opened for writing, and the recorder's root is never listed")
    ok(policy("chainbook", "open", (CHAINBOOK + "/runtime.jsonl", "rb", 0)) is None
       and policy("chainbook", "open", (CHAINBOOK + "/1791627300/window.json", "rb", 0)) is not None
       and policy("chainbook", "os.listdir", (CHAINBOOK,)) is not None
       and policy("prove", "open", (CHAINBOOK + "/runtime.jsonl", "rb", 0)) is not None,
       "under the chain book's root only its runtime.jsonl, by chainbook; nothing listed")
    ok(policy("prove", "open", (ROOT + "/1791627300/window.json", "rb", 0)) is None
       and policy("prove", "open", (ROOT + "/1791627300/window.json", "wb", 0)) is not None
       and policy("prestart", "open", (ROOT + "/runtime.jsonl", "rb", 0)) is not None,
       "the pair book's root is written by serve alone and read by the modes that judge it")
    ok(policy("reclaim", "open", (FORENSICS + "/x", "xb", 0)) is None
       and policy("reclaim", "open", (FORENSICS + "/x", "wb", 0)) is not None,
       "the forensic store takes new files by exclusive create alone")
    MODE[0] = "selftest"
    for p in (RECORDER + "/runtime.jsonl", CHAINBOOK + "/runtime.jsonl", ROOT + "/runtime.jsonl"):
        try:
            open(p, "rb")
            refused = False
        except GuardError:
            refused = True
        except OSError:
            refused = False
        ok(refused and REFUSED[-1][1] == p, "the hook refuses %s before it is opened" % p)
    REFUSED.clear()
    # the request, on a loopback listener, with every proxy variable removed from this process
    removed = [k for k in list(os.environ) if k.lower() in ("http_proxy", "https_proxy", "all_proxy", "no_proxy")]
    for k in removed:
        del os.environ[k]
    out("  proxy variables removed: %d" % len(removed))
    req = build_request("http" + ":" + "//example.invalid/")
    ok(req.get_method() == "GET" and sorted((k.lower(), v) for k, v in req.header_items()) ==
       [("accept", "application/json"), ("user-agent", UA)], "build_request: GET, Accept and this file's User-Agent")
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _Http)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    port = srv.server_address[1]
    base = "http" + ":" + "//127.0.0.1:%d" % port
    before = COUNTERS["requests"]
    r = http_get(base + "/book?token_id=1")
    line, hdrs = _Http.seen[-1]
    ok(line.startswith("GET /book?token_id=1 ") and hdrs == sorted([
        ("accept", "application/json"), ("accept-encoding", "identity"), ("connection", "close"),
        ("host", "127.0.0.1:%d" % port), ("user-agent", UA)]), "the wire: exactly five header fields")
    ok(r["status"] == 200 and r["bytes"] == 2 and r["sha256"] == "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a"
       and r["recv_mono_ns"] >= r["send_mono_ns"], "http_get records 200, 2 bytes, the body's SHA-256 and both stamps")
    r = http_get(base + "/refused")
    ok(r["status"] == 403 and r["bytes"] == 17 and r["reason"] == "http_error" and r["recv_wall_ns"] is not None,
       "a refusal is a stored reply with its status")
    srv.shutdown()
    srv.server_close()
    r = http_get(base + "/closed")
    ok(r["status"] is None and r["bytes"] == 0 and r["recv_mono_ns"] is None and r["recv_wall_ns"] is None,
       "no reply: no status and no receive stamp")
    ok(COUNTERS["requests"] - before == 3, "three loopback requests counted")
    ok(skew_of([{"recv_mono_ns": None}, {"recv_mono_ns": 7}, {"recv_mono_ns": 12}]) == 5, "skew over the replies that came")
    four = [{"status": 200, "bytes": 2, "raw": "{}", "recv_mono_ns": 10 ** 9 + i} for i in range(4)]
    ok(checkpoint_is_complete(four) == (True, "complete") and checkpoint_is_complete(four[:3])[0] is False
       and checkpoint_is_complete(four[:3] + [dict(four[3], recv_mono_ns=2 * 10 ** 9 + 1)])[1] == "skew_above_bound",
       "a checkpoint: four replies within one second")
    ok(token_ids_of('{"clobTokenIds": "[\\"11\\", \\"22\\"]", "outcomes": "[\\"Up\\", \\"Down\\"]", "conditionId": "0xab"}')[:2]
       == (["11", "22"], ["Up", "Down"]) and token_ids_of('{"clobTokenIds": "[\\"11\\"]"}')[0] is None
       and token_ids_of("[]")[0] is None, "token_ids_of: two distinct ids from the JSON-in-JSON fields, or none")
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    try:
        toks = ["101", "102", "103", "104"]

        async def run_stream(close_first_after, seconds, stop_after=None):
            state = {"connections": 0, "headers": [], "subs": [], "pings": 0}
            server = await loopback_venue(state, close_first_after)
            port_ = server.sockets[0].getsockname()[1]
            url = "ws" + ":" + "//127.0.0.1:%d/ws/market" % port_
            stats = new_stream_stats()
            t0 = time.time()
            STOP_FLAG.clear()
            if stop_after is not None:
                asyncio.get_running_loop().call_later(stop_after, STOP_FLAG.set)
            await stream_window(tmp, toks, t0, t0 + seconds, stats, url=url, ping_s=0.2,
                                kw=connect_kwargs(proxy=None), backoff=(0.1,))
            server.close()
            await server.wait_closed()
            return state, stats

        state, stats = asyncio.run(run_stream(0.6, 1.6))
        ok(state["connections"] == 2 and stats["segments"] == 2, "a close by the venue, then one reconnect")
        ok(all(x == subscription(toks) for x in state["subs"])
           and state["subs"][0] == '{"assets_ids":["101","102","103","104"],"type":"market"}',
           "the subscription: the documented frame, compact")
        ok(sorted(k for k, _v in state["headers"][0]) == ["connection", "host", "sec-websocket-key",
                                                          "sec-websocket-version", "upgrade", "user-agent"]
           and dict(state["headers"][0])["user-agent"] == UA,
           "the handshake: six header fields, this file's User-Agent, no extension offered")
        ok(stats["pings"] >= 4 and stats["pongs"] >= 2 and state["pings"] >= stats["pongs"],
           "the heartbeat: PING on its period, PONG stored")
        path = os.path.join(tmp, stats["files"][0])
        rep = {"torn": False, "bad": 0}
        rows = list(stream_rows(path, rep))
        evs = [r["event"] for r in rows if "event" in r]
        ok(not rep["torn"] and rep["bad"] == 0 and evs[:3] == ["connect", "open", "subscribe"] and evs[-1] == "end"
           and evs.count("close") == 2 and evs.count("connect") == 2,
           "the file: connect, open, subscribe, frames, close, the same again, end")
        closes = [r for r in rows if r.get("event") == "close"]
        ok(closes[0]["reason"] == "closed" and closes[0]["code"] == 1011 and closes[1]["reason"] == "end",
           "the venue's close is recorded with its code, the window's end as end")
        fr = [r for r in rows if "raw" in r]
        ok(len(fr) == stats["frames"] and all(frozenset(r) == FRAME_KEYS for r in fr)
           and fr[0]["raw"].startswith('[{"event_type": "book"'),
           "every frame a line of recv_ns, mono_ns and the frame verbatim; the first the four books")
        wj = {"documents_ok": True, "joined_late": False, "stopped": False, "stream": stats}
        T_ok = (min(r["recv_ns"] for r in rows) // 10 ** 9) // WINDOW * WINDOW
        why, sst = stream_unit(T_ok, tmp, wj, toks[:2], toks[2:])
        ok(sst["frames"] == stats["frames"] and sst["nonconforming"] == 0 and sst["foreign"] == 0
           and sst["frames_m15"] > sst["frames_m5"] > 0 and sst["subscribes"] == 2 and "initial books" not in why
           and "count" not in why, "the unit reads the stream back: every frame conforms, both markets, both sessions")
        ok("short" in why, "a stream that ends before its window's T+900 reads short")
        os.remove(path)
        t1 = time.time()
        state, stats = asyncio.run(run_stream(None, 30, stop_after=0.5))
        STOP_FLAG.clear()
        rep = {"torn": False, "bad": 0}
        rows = list(stream_rows(os.path.join(tmp, stats["files"][0]), rep))
        ok(time.time() - t1 < 5 and not rep["torn"] and rows[-1]["event"] == "end"
           and [r for r in rows if r.get("event") == "close"][0]["reason"] == "stop",
           "a stop closes the session at once and the file whole")
        os.remove(os.path.join(tmp, stats["files"][0]))
        # the writer: a sync flush makes a cut file readable to its last flush; the window maximum cuts
        p = os.path.join(tmp, "w.jsonl.gz")
        w = StreamWriter(p, flush_s=3600)
        for k in range(50):
            w.frame('{"k": %d}' % k)
        w.flush()
        with open(p, "rb") as fh:
            partial = fh.read()
        for k in range(50, 60):
            w.frame('{"k": %d}' % k)
        w.close()
        q = os.path.join(tmp, "torn.jsonl.gz")
        with open(q, "wb") as fh:
            fh.write(partial)
        rep = {"torn": False, "bad": 0}
        rows = list(stream_rows(q, rep))
        ok(rep["torn"] and len(rows) == 50 and rows[-1]["raw"] == '{"k": 49}', "a file cut after a sync flush reads to it, torn")
        rep = {"torn": False, "bad": 0}
        rows = list(stream_rows(p, rep))
        ok(not rep["torn"] and len(rows) == 61 and rows[-1]["event"] == "end" and rows[-1]["frames"] == 60,
           "the whole file: 60 frames and the end line")
        with open(q, "wb") as fh:
            fh.write(partial[:len(partial) // 2])
        rep = {"torn": False, "bad": 0}
        rows2 = list(stream_rows(q, rep))
        ok(rep["torn"] and len(rows2) < 50, "a file cut mid-block is torn, read to its last whole line")
        with open(q, "wb") as fh:
            with open(p, "rb") as src:
                fh.write(src.read() + b"\x00")
        rep = {"torn": False, "bad": 0}
        rows3 = list(stream_rows(q, rep))
        ok(rep["torn"] and len(rows3) == 61, "bytes past the trailer read torn")
        w = StreamWriter(os.path.join(tmp, "cap.jsonl.gz"), window_max=200, flush_s=0)
        w.frame("".join(sha256_bytes(b"%d" % i) for i in range(40)))
        ok(w.cut, "the window maximum cuts the stream")
        w.close()
        w = StreamWriter(os.path.join(tmp, "bin.jsonl.gz"))
        w.frame(b"\x00\xff")
        w.close()
        rep = {"torn": False, "bad": 0}
        rows = list(stream_rows(os.path.join(tmp, "bin.jsonl.gz"), rep))
        ok(rows[0]["raw_b64"] == "AP8=", "a binary frame is stored as base64, verbatim")
        ok(next_stream_path(tmp) == os.path.join(tmp, "stream.jsonl.gz"), "the first stream file of a window")
        open(os.path.join(tmp, "stream.jsonl.gz"), "wb").close()
        ok(next_stream_path(tmp) == os.path.join(tmp, "stream.1.jsonl.gz"), "a second process writes the next name")
        ok(joinable(tmp), "a directory without window.json or books is joinable")
        open(os.path.join(tmp, "books.jsonl.gz"), "wb").close()
        ok(not joinable(tmp), "a directory holding books is not rejoined")
        # the unit, on synthetic windows: every reason it names
        t = 1791627300
        four_toks = ["11", "12", "13", "14"]
        ns = 10 ** 9

        def synth(name, sub_at, frames, end_at, close_ok=True, extra=None, declared=None):
            d = os.path.join(tmp, name)
            os.makedirs(d)
            lines = [{"recv_ns": sub_at - 10 ** 6, "mono_ns": 1, "event": "connect", "seg": 0},
                     {"recv_ns": sub_at, "mono_ns": 2, "event": "subscribe", "seg": 0, "message": "m"}]
            lines += frames
            if close_ok:
                lines.append({"recv_ns": end_at, "mono_ns": 3, "event": "close", "seg": 0, "reason": "end", "code": None})
                lines.append({"recv_ns": end_at + 1, "mono_ns": 4, "event": "end", "frames": len(frames)})
            body = "".join(json.dumps(x) + "\n" for x in lines).encode()
            with open(os.path.join(d, "stream.jsonl.gz"), "wb") as fh:
                fh.write(gzip.compress(body, mtime=0))
            st = new_stream_stats()
            st.update({"opened": True, "files": ["stream.jsonl.gz"], "frames": len(frames) if declared is None else declared})
            wj_ = {"documents_ok": True, "joined_late": False, "stopped": False, "stream": st}
            if extra:
                wj_.update(extra)
            return stream_unit(t, d, wj_, four_toks[:2], four_toks[2:])

        books = [{"recv_ns": (t + 595) * ns + 10 ** 8, "mono_ns": 0,
                  "raw": json.dumps([synth_book(x, "0xc") for x in four_toks])}]
        steady = [{"recv_ns": (t + 596 + k) * ns, "mono_ns": 0,
                   "raw": json.dumps(synth_change(four_toks[:2] if k % 2 else four_toks[2:], "0xc", (t + 596 + k) * 1000))}
                  for k in range(309)]
        why, sst = synth("good", (t + 595) * ns, books + steady, (t + 905) * ns)
        ok(why == [] and sst["frames"] == 310 and sst["max_gap_ns"] == ns and sst["lag_ms"]["median"] == 0
           and sst["subscribe_offset_ms"] == 595000 and sst["last_close_offset_ms"] == 905000,
           "a window streamed from T+595 to T+905: complete, its largest gap 1 s")
        why, _s = synth("late", (t + 601) * ns, [dict(books[0], recv_ns=(t + 601) * ns + 1)] + steady[6:], (t + 905) * ns)
        ok(why == ["late subscribe"], "a subscription after T+600 reads late subscribe, and nothing else")
        why, _s = synth("nobook", (t + 595) * ns, steady, (t + 905) * ns)
        ok(why == ["initial books"], "no book of the four tokens within 5 s of it reads initial books")
        holed = books + [x for x in steady if not ((t + 700) * ns <= x["recv_ns"] <= (t + 716) * ns)]
        why, _s = synth("gap", (t + 595) * ns, holed, (t + 905) * ns)
        ok(why == ["gap"], "18 s without a frame reads gap")
        why, _s = synth("torn", (t + 595) * ns, books + steady, (t + 905) * ns, close_ok=False)
        ok(why == ["no end line in stream.jsonl.gz", "short"], "a file without its end line and its close reads so")
        why, _s = synth("early", (t + 595) * ns, books + steady[:290], (t + 890) * ns)
        ok(why == ["short"], "a stream whose last close is before T+900 reads short")
        odd = books + steady + [{"recv_ns": (t + 904) * ns + 1, "mono_ns": 0, "raw": '{"event_type": "new_market", "asset_id": "11"}'},
                                {"recv_ns": (t + 904) * ns + 2, "mono_ns": 0, "raw": json.dumps(synth_book("99", "0xd"))}]
        why, _s = synth("odd", (t + 595) * ns, odd, (t + 905) * ns, declared=len(odd) - 1)
        ok(why == ["nonconforming frames", "foreign tokens", "count"],
           "an undocumented event type, a token not subscribed and a count off its window.json are named")
        why, _s = synth("joined", (t + 595) * ns, books + steady, (t + 905) * ns, extra={"joined_late": True})
        ok(why == ["joined late"], "a window joined late is no unit")
        why, _s = synth("nodocs", (t + 595) * ns, books + steady, (t + 905) * ns, extra={"documents_ok": False})
        ok(why == ["documents"], "a window without both documents is no unit")
        off = new_stream_stats()
        off["off_reason"] = "cap"
        ok(stream_unit(t, tmp, {"documents_ok": True, "stream": off}, four_toks[:2], four_toks[2:])[0] == ["no stream (cap)"],
           "a window whose stream did not open names why")
        ok(frame_tokens([synth_book("11", "0xc")]) == (["book"], {"11"}, None)
           and frame_tokens(synth_change(["11", "12"], "0xc", 5))[1:] == ({"11", "12"}, 5)
           and frame_tokens({"event_type": "tick_size_change", "asset_id": "11"}) == (["tick_size_change"], {"11"}, None)
           and frame_tokens({"event_type": "last_trade_price", "asset_id": "12"})[1] == {"12"}
           and frame_tokens([]) is None and frame_tokens({"event_type": "book"}) is None
           and frame_tokens({"event_type": "price_change", "price_changes": []}) is None and frame_tokens(7) is None,
           "frame_tokens: the four documented types and their token ids, nothing else")
        good_wj = {k: None for k in WINDOW_JSON_KEYS}
        assert_keys(good_wj, WINDOW_JSON_KEYS, "window.json")
        try:
            assert_keys(dict(good_wj, stream={"best_ask": 1}), WINDOW_JSON_KEYS, "window.json")
            caught = False
        except AssertionError:
            caught = True
        ok(caught, "a forbidden key at any depth fails the allow-list")
        ok(not (STREAM_KEYS | WINDOW_JSON_KEYS | WINDOW_MARKET_KEYS | PROOF_JSON_KEYS | PRESTART_JSON_KEYS) & FORBIDDEN_KEYS,
           "no allowed key is a forbidden one")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    # the readings, on synthetic counts, and their error rates against fractions computed outside this file
    ok([read_g_stream(u) for u in ([True] * 4, [True, True, True, False], [True, True, False, False], [True] * 3)]
       == ["PASS", "PASS", "FAIL", "UNDECIDABLE"], "G-STREAM: 4 and 3 of 4, 2 of 4, fewer than 4")
    ok([read_g_books(28, 26), read_g_books(28, 25), read_g_books(27, 27)] == ["PASS", "FAIL", "UNDECIDABLE"],
       "G-BOOKS: 26 of 28, 25 of 28, fewer than 28")
    ok([read_g_tierc(r) for r in ([(True, True, True)] * 2, [(True, True, True)] * 2 + [(False, True, False)],
                                 [(True, True, True), (True, False, None)], [(True, True, True), (False, True, True)])]
       == ["PASS", "FAIL", "UNDECIDABLE", "UNDECIDABLE"], "G-TIERC: two loaded, any failure, too few loaded")
    ok(p_fail_at_least(4, 2, Fraction(1, 100)) == Fraction(59203, 100000000), "G-STREAM's false failure at 1 in 100")
    ok(p_fail_at_least(4, 2, Fraction(1, 4)) == Fraction(67, 256) and p_fail_at_least(4, 2, Fraction(1, 2)) == Fraction(11, 16),
       "G-STREAM's power at 1 in 4 and 1 in 2")
    ok(p_fail_at_least(28, 3, Fraction(1, 100)) == Fraction(1, 1) - Fraction(99, 100) ** 28 - 28 * Fraction(1, 100)
       * Fraction(99, 100) ** 27 - 378 * Fraction(1, 100) ** 2 * Fraction(99, 100) ** 26
       and decimals(p_fail_at_least(28, 3, Fraction(1, 100)), 10) == "0.0027171219",
       "G-BOOKS' false failure at 1 in 100")
    ok(decimals(p_fail_at_least(28, 3, Fraction(1, 4)), 10) == "0.9833852515"
       and decimals(p_fail_at_least(28, 3, Fraction(1, 10)), 10) == "0.5406170777", "G-BOOKS' power at 1 in 4 and 1 in 10")
    ok(p_false_alarm(0, 2016, 4) == 0 and p_false_alarm(1, 2016, 4) == 1 - Fraction(2015, 2016) ** 4
       and p_false_alarm(0, 0, 4) is None, "G-TIERC's false alarm, exact")
    ok(decimals(Fraction(1, 3), 4) == "0.3333" and decimals(Fraction(2, 3), 4) == "0.6667", "decimals: half up")
    # this file's own syntax: its imports and its endpoints
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            mods |= {a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom):
            mods.add((node.module or "").split(".")[0])
    ok(mods - set(sys.stdlib_module_names) == {"websockets"}, "imports: the standard library and websockets")
    sep = ":" + "//"
    urls = sorted({c.value for c in ast.walk(tree) if isinstance(c, ast.Constant) and isinstance(c.value, str)
                   and sep in c.value})
    ok(urls == sorted([GAMMA_MARKET_URL, CLOB_BOOK_URL, CLOB_WS_URL]), "exactly three endpoints in the file's text")
    ok(websockets.__version__ == "17.1", "websockets 17.1, the recorder's")
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz26-nesting-b3-capture.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    MODE[0] = mode
    rc = 0
    if mode == "serve":
        assert not rest, "serve takes no argument"
        rc = mode_serve()
    elif mode == "prove":
        assert len(rest) == 1 and rest[0].isdigit(), "prove A"
        rc = mode_prove(int(rest[0]))
    elif mode == "unit":
        assert len(rest) == 1 and rest[0] in ("0", "1"), "unit N"
        mode_unit(int(rest[0]))
    elif mode == "mark":
        assert len(rest) == 1, "mark NAME"
        mode_mark(rest[0])
    elif mode == "scratch":
        assert len(rest) == 1, "scratch OWN"
        mode_scratch(rest[0])
    elif mode == "reclaim":
        mode_reclaim(rest)
    else:
        table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "still": mode_still,
                 "chainbook": mode_chainbook, "restart": mode_restart, "final": mode_final,
                 "prestart": mode_prestart, "load": mode_load, "restored": mode_restored}
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    if mode != "serve":
        out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
        out("opens refused: %d; manifest opens attempted %d; chain book opens %d; requests %d, stream sessions %d" % (
            len(REFUSED), OPENS["manifest.json"], OPENS["chainbook"], COUNTERS["requests"], COUNTERS["sessions"]))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
