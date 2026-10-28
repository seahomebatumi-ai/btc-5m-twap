#!/usr/bin/env python3
"""TZ-33 - the L track's L0, its capture: the reward book.

    serve             the service. Once a UTC day it selects the day's markets by TZ-33 section 1's rule - the
                      venue's reward listing ranked by daily rate, each candidate's gamma and CLOB documents -
                      and stores every reply verbatim; for every 900 s slot S of the day it streams the CLOB
                      market websocket for both tokens of every selected market from S-5 to S+905, every frame
                      stored verbatim with its receive stamps, polls each market's reward document three times,
                      and writes the slot's summary at S+910
    prestart          the request path on this host before the service starts: one listing page, one gamma
                      batch, two CLOB documents and two reward documents through http_get, one stream session of
                      25 s through the service's own stream code; the processes; the neighbours' base rates, read
                      once the pair book's archive is not running
    prove A           G-SELECT, G-STREAM, G-REWARDS and G-NEIGHBORS as of the epoch A, the neighbours read from the
                      service's first start once the pair book's archive is not running; exit 3 NOT YET
    resume A          G-RESUME: the first slot opened after the restart, as of A; exit 3 NOT YET
    load              G-LOAD: the service's processor time and memory since its start
    fingerprint       map section 0 against the primary checkout
    selftest          every rule of this file, on literals and on loopback servers only
    still             the recorder's and the pair book's units: the first run records them, a later run compares
    mark NAME         an instant, and the state of the reward book's unit, into state.json
    unit N            G-UNIT for btc-rewardbook.service at N restarts; at 0, G-START too
    restart           G-RESTART, from the service's own record
    final             G-UNIT at one restart, G-STILL, and the unit's memory
    stopped           after K-33: the reward book stopped through systemd, disabled, no process left
    scratch OWN       the UUID directories beside OWN, this session's directory: live or earlier
    reclaim TREE...   section 9

It requests clob.polymarket.com/rewards/markets/current, gamma-api.polymarket.com/markets,
clob.polymarket.com/markets/{condition_id}, clob.polymarket.com/rewards/markets/{condition_id} and the market
websocket of ws-subscriptions-clob.polymarket.com, and nothing else, every request with the headers this file
fixes. It never authenticates, holds no credential and can place no order. The service writes what it receives
byte for byte; no mode prints a price, a size, a side, a book's hash, a rate or an outcome. An audit hook
enforces section 2 of the TZ: under /var/lib/btc-recorder only a manifest.json is opened, read only, by prestart
and prove; under /var/lib/btc-pairbook only a window's window.json, read only, by prestart and prove; under
/var/lib/btc-pairbook-archive only ledger.jsonl, read only, by still and final; under /var/lib/btc-rewardbook
only serve writes; serve starts no process. Exit 0: every assert held. Exit 1: an assert or a floor, named.
Exit 2: serve refused its command line. Exit 3: another instance runs, or NOT YET. Run it with /root/tz04a-env,
whose websockets it needs.

Written for CryptoTZ/TZ-33-reward-book-capture.md. The TZ is the specification.
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
import urllib.parse
import urllib.request
import zlib
from collections import Counter
from decimal import Decimal
from fractions import Fraction

import websockets
from websockets.asyncio.client import connect as ws_connect
from websockets.asyncio.server import serve as ws_serve

if not __debug__:
    sys.stderr.write("tz33: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(1)


def _malloc_tune():
    """glibc raises its mmap threshold each time it frees a large block, so the frames of a slot's first book list and
    the listing's pages would be served from the heap and never returned; fixed at 128 KiB, with two arenas, as
    TZ-23's instrument does (research/tz23-maker-m0.py lines 112 to 122). True where both settings took."""
    try:
        import ctypes
        libc = ctypes.CDLL("libc.so.6")
        # mallopt(M_MMAP_THRESHOLD = -3, 128 KiB) and mallopt(M_ARENA_MAX = -8, 2)
        return libc.mallopt(-3, 131072) == 1 and libc.mallopt(-8, 2) == 1
    except (OSError, AttributeError):
        return False


MALLOC_TUNED = _malloc_tune()

# ---- the endpoints, and nothing else: five string constants carry a scheme separator --------------------

CLOB_LISTING_URL = "https://clob.polymarket.com/rewards/markets/current?next_cursor={cursor}"
GAMMA_MARKETS_URL = "https://gamma-api.polymarket.com/markets?{query}"
CLOB_MARKET_URL = "https://clob.polymarket.com/markets/{condition_id}"
CLOB_REWARDS_URL = "https://clob.polymarket.com/rewards/markets/{condition_id}"
CLOB_WS_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
URLS = {"listing": CLOB_LISTING_URL, "gamma": GAMMA_MARKETS_URL, "clob": CLOB_MARKET_URL,
        "rewards": CLOB_REWARDS_URL, "ws": CLOB_WS_URL}

# ---- the TZ's constants: none of them is measured by this run --------------------------------------------

MAP_REVISION = "2026-10-27-b"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 41, "tracked": 2, "reported": 1}

ROOT = "/var/lib/btc-rewardbook"
RECORDER = "/var/lib/btc-recorder"
PAIRBOOK = "/var/lib/btc-pairbook"
ARCHIVE_STATE = "/var/lib/btc-pairbook-archive"
ARCHIVE_LEDGER = ARCHIVE_STATE + "/ledger.jsonl"
CHAINBOOK = "/var/lib/btc-chainbook"
SVC = "/root/btc-rewardbook-svc"
WORK = "/root/tz33-work"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
DISK_PATH = "/var/lib"

UNIT = "btc-rewardbook.service"
NEIGHBORS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service"}
ARCHIVE_UNIT = "btc-pairbook-archive.service"
ARCHIVE_TIMER = "btc-pairbook-archive.timer"
PYTHON = "/root/tz04a-env/venv/bin/python"
SERVICE_FILE = SVC + "/tz33-reward-book-capture.py"
SERVICE_ARGV = (PYTHON, "-B", "-u", SERVICE_FILE, "serve")
MEMORY_MAX = 201326592       # MemoryMax=192M, the unit's ceiling (TZ-33 section 0.4)
NICE = 10                    # Nice=10: the recorder and the pair book run at 0

UA = "btc-5m-twap-tz33"
ACCEPT = "application/json"

# section 1 - the selection rule, fixed before its data
DAY = 86400
SET_SIZE = 150               # the day's set: the first 150 candidates of the ranking that pass every check
WALK_MAX = 1500              # no candidate is walked past the 1,500th of the ranking
GAMMA_BATCH = 50             # condition ids a gamma request carries
GAMMA_LIMIT = 100            # its limit parameter, above the batch
END_MIN_S = 15 * DAY         # endDate at or after D0 + 15 days: 14 days after the day's end
EVENT_BAND_S = (-DAY, 2 * DAY)   # no event startTime or endDate in [D0 - 1 day, D0 + 2 days)
EXCLUDED_TAGS = frozenset((
    "sports", "esports",
    "crypto", "crypto prices", "bitcoin", "ethereum", "solana", "pre-market", "crypto listings",
    "hit price", "up or down", "finance updown", "pyth finance", "equity daily pyth", "stocks", "equities",
    "commodities", "oil", "gold", "forex", "fx", "price milestone", "price comparison", "daily-close",
    "gas price",
    "weather", "daily temperature", "highest temperature", "lowest temperature", "temperature", "global temp"))
LISTING_FIRST = "MA=="       # the listing's first cursor
LISTING_END = "LTE="         # the cursor the listing returns after its last page
LISTING_PAGES_MAX = 100
REQUEST_TRIES = 3            # a selection request is tried at most three times, 1 s and 2 s apart
RETRY_S = (1, 2)
REQUEST_GAP_S = 0.1          # at least 100 ms between two requests of a selection
SELECT_LEAD_S = 900          # day D is selected from D0 - 900 s, before its first slot opens
SELECT_RETRY_S = 60          # a failed attempt is tried again 60 s later
SELECT_ATTEMPTS_MAX = 120    # at most 120 attempts a day

# the slot
SLOT = 900
OPEN_BEFORE = 5              # a slot's stream opens at S - 5 and closes at S + 905
CLOSE_AFTER = 905
SLOT_JSON_AT = 910           # the slot's summary at S + 910
JOIN_LAST = 880              # a process starting inside a slot joins it until S + 880
LAUNCH_LEAD = 1              # a slot's task starts 1 s before its stream opens
REWARD_ROUNDS = (30, 330, 630)   # three polls of every market a slot, 300 s apart
REWARD_SPAN_MS = 270000      # a round's polls spread evenly over 270 s
REWARD_LAST = 900            # no poll starts after S + 900
READ_TIMEOUT_S = 10.0        # a selection request
POLL_TIMEOUT_S = 5.0         # a reward document poll
PING_S = 10                  # the venue's heartbeat: the text frame PING every 10 s
OPEN_TIMEOUT_S = 10
CLOSE_TIMEOUT_S = 2
MAX_FRAME = 16777216         # 16 MiB: a slot's first frame holds the books of 300 tokens
MAX_QUEUE = 16               # websockets' own default
BACKOFF_S = (1, 2, 4, 8)     # before a reconnect inside a slot
GZ_STREAM = 9                # stream files (TZ-33 section 6)
GZ_LEVEL = 6                 # every other gzip file
FLUSH_S = 10                 # a sync flush of the stream file at least every 10 s of frames

RESOURCE_FLOOR = 2200000000  # free bytes below which the service halts, exit 1: read at every slot and selection
STREAM_FLOOR = 7300000000    # free bytes below which no stream opens for a slot
STREAM_CAP = 4000000000      # stream bytes under ROOT at which no stream opens, summed again at every slot
SLOT_STREAM_MAX = 100000000  # stored bytes of one slot's stream at which it is cut
WRITE_CAP = 1000000000       # bytes one process writes but its stream files
MEM_FLOOR = 135569408        # MemAvailable floor of the reading modes: twice the largest measured peak (section 0.4)

# the pair book's archive: no mode reads the pair book's store while its service runs (map section 6)
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")
HOLD_STEP_S = 10
HOLD_MAX_S = 7200

# section 4 - the gates, fixed before their data
GATE_SLOTS = 4               # G-STREAM and G-REWARDS: the first four qualifying slots
GATE_STREAM_PASS = 3         # >= 3 of 4 complete
REWARDS_PASS = Fraction(99, 100)   # G-REWARDS: at least 99 in 100 of their polls served
QUALIFY_LEAD_S = 300         # a slot qualifies when S - 5 >= s + 300
BUDGET_S = 6000              # the proof decides by s + 6,000
INITIAL_S = 10               # a book of every subscribed token within 10 s of the first subscribe
GAP_MAX_NS = 15000000000     # no two consecutive received instants more than 15 s apart
LAG_RANGE_MS = (-1000, 60000)
LOAD_MAX = Fraction(1, 10)   # G-LOAD: at most a tenth of the one processor, since the start
RESTART_MAX_S = 60
RESUME_LEAD_S = 60           # G-RESUME's slot opens at least 60 s after the restarted process starts
BASE_RATE_S = 604800         # the neighbours' base rates: the week before prestart
BASE_INTERVALS = 2016        # the recorder's last 2,016 intervals closed 600 s before prestart
BASE_WINDOWS = 672           # the pair book's last 672 windows whose window.json was due 60 s before it
NEIGHBOR_WAIT_S = 600        # the proof decides 600 s after the fourth qualifying slot's summary
NEIGHBOR_MIN = {"recorder": 8, "pairbook": 3}
NEIGHBOR_UNITS_MAX = {"recorder": 16, "pairbook": 5}   # the most units the span from the start can hold
KNOWN = ("book", "price_change", "last_trade_price", "tick_size_change")

TOKEN = re.compile(r"[0-9a-f]{16,64}")
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
CID_RE = re.compile(r"0x[0-9a-f]{64}")
TOKEN_ID_RE = re.compile(r"[0-9]{1,100}")
MANIFEST_RE = re.compile(re.escape(RECORDER) + r"/btc-updown-5m/[0-9]{10}/manifest\.json")
WINDOW_RE = re.compile(re.escape(PAIRBOOK) + r"/[0-9]{10}/window\.json")
DAY_RE = re.compile(r"[0-9]{10}")
SLOT_FILE_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.(stream\.jsonl\.gz|rewards\.jsonl\.gz|slot\.json)")
SELECT_FILE_RE = re.compile(r"select\.([0-9]+)\.(json|replies\.jsonl\.gz)")
LIVE_S = 60

# the stored formats, and the allow-lists every summary is asserted against before it is written
REPLY_KEYS = frozenset(("kind", "key", "try", "url", "status", "send_wall_ns", "send_mono_ns", "recv_mono_ns",
                        "recv_wall_ns", "bytes", "sha256", "raw", "reason"))
POLL_KEYS = frozenset(("S", "round", "i", "condition_id", "due_wall_ns", "url", "status", "send_wall_ns",
                       "send_mono_ns", "recv_mono_ns", "recv_wall_ns", "bytes", "sha256", "raw", "reason"))
SELECT_KEYS = frozenset(("day", "attempt", "ok", "reason", "pid", "started_wall_ns", "finished_wall_ns",
                         "replies", "listing", "walked", "reasons", "walk", "members", "rule"))
MEMBER_KEYS = frozenset(("rank", "condition_id", "token_ids", "outcomes", "slug", "end_date", "rate",
                         "min_size", "max_spread", "neg_risk", "tags"))
SLOT_JSON_KEYS = frozenset(("S", "day", "index", "pid", "task_wall_ns", "joined_late", "stopped", "selection",
                            "markets", "tokens", "stream", "rewards", "closed_wall_ns", "error"))
STREAM_KEYS = frozenset(("opened", "off_reason", "file", "segments", "frames", "frame_bytes", "pongs", "pings",
                         "first_frame_wall_ns", "last_frame_wall_ns", "max_gap_ns", "subscribed_wall_ns",
                         "stored_bytes", "cut"))
REWARDS_JSON_KEYS = frozenset(("file", "scheduled", "polled", "missed", "served", "rows", "status_counts",
                               "stored_bytes"))
PRESTART_JSON_KEYS = frozenset(("mode", "p_wall", "file_sha256", "processes", "proxy_variables", "base_rates",
                                "requests", "walk", "stream", "counters"))
PROOF_JSON_KEYS = frozenset(("mode", "as_of", "start", "g_select", "slots", "g_stream", "g_rewards",
                             "neighbors", "counters"))
RESUME_JSON_KEYS = frozenset(("mode", "as_of", "restart", "slot", "g_resume"))
FORBIDDEN_KEYS = frozenset(("price", "prices", "bid", "bids", "ask", "asks", "mid", "midpoint", "size",
                            "sizes", "level", "levels", "book", "books", "spread", "raw", "priceToBeat",
                            "finalPrice", "best_bid", "best_ask", "amount", "quote", "quotes", "side",
                            "outcomePrices", "hash", "rate", "rates", "rate_per_day", "total_daily_rate",
                            "market_competitiveness", "min_size", "max_spread"))
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


class SelectionError(Exception):
    pass


def bump(name, by=1):
    with _LOCK:
        COUNTERS[name] += by
        return COUNTERS[name]

# ---- the audit hook: TZ-33 section 2 as a pure function, and the hook that applies it ---------------------


WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
REFUSED = []
OPENS = {"manifest.json": 0, "window.json": 0, "ledger.jsonl": 0}
HOOKED = ("open", "os.listdir", "os.scandir", "subprocess.Popen", "os.system", "os.exec", "os.spawn",
          "os.posix_spawn", "os.fork", "os.forkpty")
ROOT_READERS = ("serve", "prove", "resume", "unit", "restart", "stopped")


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
        if _under(p, ARCHIVE_STATE):
            if mode in ("still", "final") and not w and p == ARCHIVE_LEDGER:
                return None
            return "the archive's state"
        if _under(p, PAIRBOOK):
            if mode in ("prestart", "prove") and not w and WINDOW_RE.fullmatch(p):
                return None
            return "the pair book's root"
        if _under(p, CHAINBOOK):
            return "the chain book's root"
        if _under(p, ROOT):
            if w:
                return None if mode == "serve" else "a write under the reward book's root"
            return None if mode in ROOT_READERS else "a read under the reward book's root"
        if w:
            if mode == "serve":
                return "a write outside the reward book's root"
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
        for root, name in ((RECORDER, "the recorder's root"), (ARCHIVE_STATE, "the archive's state"),
                           (PAIRBOOK, "the pair book's root"), (CHAINBOOK, "the chain book's root")):
            if _under(p, root):
                return "a listing under " + name
        if _under(p, ROOT):
            return None if mode in ("serve", "prove", "resume") else "a listing under the reward book's root"
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
        elif p is not None and _under(p, PAIRBOOK):
            OPENS["window.json"] += 1
        elif p is not None and _under(p, ARCHIVE_STATE):
            OPENS["ledger.jsonl"] += 1


sys.addaudithook(_audit)

# ---- small helpers -------------------------------------------------------------------------------------------


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
    """Before a mode that reads the venue or the capture: glibc's two settings and the host's memory floor (section
    0.4)."""
    assert MALLOC_TUNED, "BLOCKED: glibc did not take the mmap threshold and the arena count"
    avail = mem_available()
    out("MemAvailable %d bytes, floor %d" % (avail, MEM_FLOOR))
    assert avail >= MEM_FLOOR, "BLOCKED: MemAvailable %d bytes, below %d" % (avail, MEM_FLOOR)


def archive_state():
    cp = subprocess.run(["systemctl", "is-active", ARCHIVE_UNIT], capture_output=True, text=True)
    return cp.stdout.strip()


def archive_hold(state_of=archive_state, clock=time.time, sleep=time.sleep):
    """Before the first read of the pair book's store: until the archive's service is not running, read every
    HOLD_STEP_S; BLOCKED past HOLD_MAX_S. Returns the state read last and the seconds waited."""
    t0 = clock()
    while True:
        st = state_of()
        if st not in RUNNING:
            waited = clock() - t0
            out("the pair book's archive: %s after %.0f s" % (st or "unread", waited))
            return st, waited
        assert clock() - t0 <= HOLD_MAX_S, "BLOCKED: the archive's service read %s for %.0f s" % (st, clock() - t0)
        sleep(HOLD_STEP_S)


def assert_keys(obj, allowed, what):
    got = frozenset(obj)
    assert got == allowed, "%s key set %s, required %s" % (what, sorted(got), sorted(allowed))


def forbid(obj, what, depth=0):
    """No price, size, level, side, hash or rate leaves the store through an output file."""
    assert depth < 14, "%s nested too deep" % what
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


def decimals(fr, places=10):
    if fr is None:
        return None
    scale = 10 ** places
    q, r = divmod(fr.numerator * scale, fr.denominator)
    if 2 * r >= fr.denominator:
        q += 1
    if places == 0:
        return str(q)
    s = str(q).rjust(places + 1, "0")
    return s[:-places] + "." + s[-places:]


def stopping():
    return STOP_FLAG.is_set()


def request_stop():
    STOP_FLAG.set()
    if STOP_EVENT[0] is not None:
        STOP_EVENT[0].set()


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

# ---- the network: four REST endpoints --------------------------------------------------------------------------


def build_request(url):
    """The one builder of every HTTP request: GET with Accept and this file's User-Agent."""
    return urllib.request.Request(url, method="GET", headers={"Accept": ACCEPT, "User-Agent": UA})


def http_get(url, timeout=READ_TIMEOUT_S):
    """One GET through build_request. No retry. Both receive stamps only where a status came back."""
    bump("requests")
    send_wall, send_mono = time.time_ns(), time.monotonic_ns()
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
    return {"url": url, "status": status, "send_wall_ns": send_wall, "send_mono_ns": send_mono,
            "recv_mono_ns": recv_mono, "recv_wall_ns": recv_wall, "bytes": len(body), "sha256": sha256_bytes(body),
            "raw": raw, "reason": reason}


def loads_exact(raw):
    """JSON with every non-integer number a Decimal of its own text."""
    return json.loads(raw, parse_float=Decimal)


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str)


def number(v):
    return isinstance(v, (int, Decimal)) and not isinstance(v, bool)

# ---- the selection rule: TZ-33 section 1, pure functions of the stored replies ----------------------------------


def compact_row(row):
    """A listing row reduced to the fields the rule reads and a digest of the whole row, for the conflict test."""
    if not isinstance(row, dict):
        return None
    return {"condition_id": row.get("condition_id"), "total_daily_rate": row.get("total_daily_rate"),
            "rewards_min_size": row.get("rewards_min_size"), "rewards_max_spread": row.get("rewards_max_spread"),
            "digest": sha256_bytes(canonical(row).encode("utf-8"))}


def listing_rows(compact):
    """Every compact row once, in first appearance: (rows, conflicts, unkeyed). A condition id whose rows are not
    all identical is a conflict; a row without a string condition id is unkeyed."""
    rows, conflicts, unkeyed = {}, set(), 0
    for row in compact:
        cid = row.get("condition_id") if isinstance(row, dict) else None
        if not isinstance(cid, str):
            unkeyed += 1
            continue
        if cid in rows:
            if rows[cid]["digest"] != row["digest"]:
                conflicts.add(cid)
        else:
            rows[cid] = row
    return rows, conflicts, unkeyed


def listing_verdict(row):
    """None where a listing row may be ranked; otherwise why not."""
    if not CID_RE.fullmatch(row.get("condition_id", "")):
        return "condition id"
    for k in ("total_daily_rate", "rewards_min_size", "rewards_max_spread"):
        v = row.get(k)
        if not number(v):
            return "no " + k
        if not v > 0:
            return k + " not positive"
    return None


def ranking(rows, conflicts, unkeyed=0):
    """The ranked candidates, by total_daily_rate descending and condition id ascending, and the rows dropped."""
    ranked, dropped = [], Counter()
    if unkeyed:
        dropped["condition id"] += unkeyed
    for cid, row in rows.items():
        if cid in conflicts:
            dropped["conflicting rows"] += 1
            continue
        why = listing_verdict(row)
        if why is not None:
            dropped[why] += 1
            continue
        ranked.append((cid, row))
    ranked.sort(key=lambda x: (-x[1]["total_daily_rate"], x[0]))
    return ranked, dropped


def iso_seconds(s):
    """An ISO-8601 instant that carries its zone, as epoch seconds; None where it does not parse or has no zone."""
    if not isinstance(s, str) or not s:
        return None
    try:
        d = datetime.datetime.fromisoformat(s[:-1] + "+00:00" if s.endswith("Z") else s)
    except ValueError:
        return None
    if d.tzinfo is None:
        return None
    return d.timestamp()


def gamma_verdict(docs, d0):
    """docs: every gamma document of the candidate's condition id. None where it passes; otherwise why not."""
    if not docs:
        return "no gamma document"
    if len(docs) > 1:
        return "two gamma documents"
    d = docs[0]
    end = iso_seconds(d.get("endDate"))
    if end is None:
        return "end date unreadable"
    if end < d0 + END_MIN_S:
        return "ends within 14 days of the day's end"
    if d.get("gameStartTime") not in (None, ""):
        return "game start time"
    evs = d.get("events")
    if evs is not None and not isinstance(evs, list):
        return "events unreadable"
    for e in evs or []:
        if not isinstance(e, dict):
            return "events unreadable"
        for key, name in (("startTime", "start"), ("endDate", "end")):
            st = e.get(key)
            if st in (None, ""):
                continue
            t = iso_seconds(st)
            if t is None:
                return "event %s unreadable" % name
            if d0 + EVENT_BAND_S[0] <= t < d0 + EVENT_BAND_S[1]:
                return "event %s near the day" % name
    return None


def clob_verdict(doc, cid):
    """The candidate's CLOB document: None where it passes; otherwise why not."""
    if not isinstance(doc, dict):
        return "CLOB document unreadable"
    if doc.get("condition_id") != cid:
        return "CLOB document of another market"
    for k, want in (("active", True), ("closed", False), ("archived", False), ("accepting_orders", True),
                    ("enable_order_book", True)):
        if doc.get(k) is not want:
            return "%s not %s" % (k, str(want).lower())
    toks = doc.get("tokens")
    if not isinstance(toks, list) or len(toks) != 2 or not all(isinstance(t, dict) for t in toks):
        return "not two tokens"
    ids = [t.get("token_id") for t in toks]
    if not all(isinstance(i, str) and TOKEN_ID_RE.fullmatch(i) for i in ids) or ids[0] == ids[1]:
        return "token ids"
    if doc.get("game_start_time") not in (None, ""):
        return "game start time"
    sd = doc.get("seconds_delay")
    if sd is not None and (not number(sd) or sd != 0):
        return "seconds delay"
    tags = doc.get("tags")
    if tags is not None and not isinstance(tags, list):
        return "tags unreadable"
    hit = sorted({t.strip().lower() for t in tags or [] if isinstance(t, str)} & EXCLUDED_TAGS)
    if hit:
        return "tag " + hit[0]
    return None


def member_of(rank, cid, row, gdoc, cdoc):
    toks = cdoc["tokens"]
    m = {"rank": rank, "condition_id": cid, "token_ids": [toks[0]["token_id"], toks[1]["token_id"]],
         "outcomes": [toks[0].get("outcome"), toks[1].get("outcome")], "slug": cdoc.get("market_slug"),
         "end_date": gdoc.get("endDate"), "rate": str(row["total_daily_rate"]),
         "min_size": str(row["rewards_min_size"]), "max_spread": str(row["rewards_max_spread"]),
         "neg_risk": cdoc.get("neg_risk"), "tags": cdoc.get("tags")}
    assert frozenset(m) == MEMBER_KEYS, "member keys"
    return m


def walk(ranked, d0, fetch_gamma, fetch_clob, k=SET_SIZE, walk_max=WALK_MAX, batch=GAMMA_BATCH):
    """TZ-33 section 1's walk: the ranking in order, a gamma request for each block of `batch` candidates, a CLOB
    document for each candidate that passes its gamma checks, until `k` members or the `walk_max`-th candidate.
    Returns the members, every walked candidate's [rank, condition id, verdict], the verdicts' counts and the
    number of candidates the gamma requests covered."""
    members, rows, reasons = [], [], Counter()
    limit = min(len(ranked), walk_max)
    i = 0
    while i < limit and len(members) < k:
        block = ranked[i:min(i + batch, limit)]
        docs = fetch_gamma([cid for cid, _row in block])
        for j, (cid, row) in enumerate(block):
            if len(members) >= k:
                break
            why = gamma_verdict(docs.get(cid, []), d0)
            if why is None:
                cdoc = fetch_clob(cid)
                why = "no CLOB document" if cdoc is None else clob_verdict(cdoc, cid)
                if why is None:
                    members.append(member_of(i + j, cid, row, docs[cid][0], cdoc))
            rows.append([i + j, cid, why or "member"])
            reasons[why or "member"] += 1
        i += len(block)
    return members, rows, reasons, i


def gamma_query(cids):
    return urllib.parse.urlencode([("limit", GAMMA_LIMIT)] + [("condition_ids", c) for c in cids])


def docs_by_condition(obj, cids):
    """A gamma reply's documents grouped by the requested condition ids; documents of other ids are ignored."""
    assert isinstance(obj, list), "a gamma reply that is not a list"
    want = set(cids)
    found = {}
    for d in obj:
        if isinstance(d, dict) and d.get("conditionId") in want:
            found.setdefault(d["conditionId"], []).append(d)
    return found

# ---- the fetchers: live, every try kept; and stored, the same replies read back --------------------------------


class LiveFetch:
    """The selection's requests through http_get: every try one reply record handed to `sink`, a request tried at
    most REQUEST_TRIES times on a network error, a 429 or a 5xx; a final reply that is not 200 (or 404 for a CLOB
    document) fails the attempt."""

    def __init__(self, sink, urls=None, getter=None, sleep=time.sleep, gap=REQUEST_GAP_S):
        self.sink = sink
        self.urls = dict(URLS, **(urls or {}))
        self.get = getter or http_get
        self.sleep, self.gap = sleep, gap
        self.requests = 0

    def _one(self, kind, key, url):
        for t in range(REQUEST_TRIES):
            if stopping():
                raise SelectionError("stopped")
            if self.requests:
                self.sleep(self.gap)
            self.requests += 1
            res = self.get(url)
            rec = {"kind": kind, "key": key, "try": t}
            rec.update({k: res[k] for k in ("url", "status", "send_wall_ns", "send_mono_ns", "recv_mono_ns",
                                            "recv_wall_ns", "bytes", "sha256", "raw", "reason")})
            assert frozenset(rec) == REPLY_KEYS, "reply keys"
            self.sink(rec)
            st = res["status"]
            if st is not None and st != 429 and st < 500:
                return res
            if t + 1 < REQUEST_TRIES:
                self.sleep(RETRY_S[min(t, len(RETRY_S) - 1)])
        return res

    def listing(self, cursor):
        res = self._one("listing", cursor, self.urls["listing"].format(cursor=cursor))
        if res["status"] != 200:
            raise SelectionError("listing page %s: status %s" % (cursor, res["status"]))
        return res["raw"]

    def gamma(self, cids):
        res = self._one("gamma", list(cids), self.urls["gamma"].format(query=gamma_query(cids)))
        if res["status"] != 200:
            raise SelectionError("gamma request: status %s" % res["status"])
        return res["raw"]

    def clob(self, cid):
        res = self._one("clob", cid, self.urls["clob"].format(condition_id=cid))
        if res["status"] == 404:
            return None
        if res["status"] != 200:
            raise SelectionError("CLOB document %s: status %s" % (cid, res["status"]))
        return res["raw"]


class StoredFetch:
    """The same requests answered from an attempt's replies file, read in order: each request must be the next one
    the attempt made, and its answer is that request's last try."""

    def __init__(self, path):
        self.it = self._groups(path)
        self.pos = 0

    @staticmethod
    def _groups(path):
        with gzip.open(path, "rb") as fh:
            key, last = None, None
            for ln in fh:
                if not ln.strip():
                    continue
                r = json.loads(ln)
                k = (r["kind"], canonical(r["key"]))
                if key is not None and k != key:
                    yield key, last
                key, last = k, r
            if key is not None:
                yield key, last

    def _next(self, kind, key):
        got = next(self.it, None)
        assert got is not None, "stored replies: no reply for %s %s" % (kind, key)
        k, r = got
        assert k == (kind, canonical(key)), "stored replies: %r where %r was requested" % (k, (kind, key))
        self.pos += 1
        return r

    def exhausted(self):
        return next(self.it, None) is None

    def listing(self, cursor):
        r = self._next("listing", cursor)
        if r["status"] != 200:
            raise SelectionError("listing page %s: status %s" % (cursor, r["status"]))
        return r["raw"]

    def gamma(self, cids):
        r = self._next("gamma", list(cids))
        if r["status"] != 200:
            raise SelectionError("gamma request: status %s" % r["status"])
        return r["raw"]

    def clob(self, cid):
        r = self._next("clob", cid)
        if r["status"] == 404:
            return None
        if r["status"] != 200:
            raise SelectionError("CLOB document %s: status %s" % (cid, r["status"]))
        return r["raw"]


def run_rule(fetch, d0, k=SET_SIZE, walk_max=WALK_MAX):
    """The whole of TZ-33 section 1 through a fetcher: the listing's pages, the ranking, the walk. Returns the
    result's fields; raises SelectionError where a reply fails the attempt."""
    compact, n_pages, n_rows, cursor = [], 0, 0, LISTING_FIRST
    for _n in range(LISTING_PAGES_MAX):
        try:
            obj = loads_exact(fetch.listing(cursor))
        except ValueError:
            raise SelectionError("listing page %s: not JSON" % cursor)
        if not (isinstance(obj, dict) and isinstance(obj.get("data"), list)):
            raise SelectionError("listing page %s: not a page" % cursor)
        n_pages += 1
        n_rows += len(obj["data"])
        compact.extend(compact_row(r) for r in obj["data"])
        nxt = obj.get("next_cursor")
        if not obj["data"] or nxt == LISTING_END:
            break
        if not isinstance(nxt, str) or not nxt:
            raise SelectionError("listing page %s: no next cursor" % cursor)
        cursor = nxt
        obj = None
    else:
        raise SelectionError("listing beyond %d pages" % LISTING_PAGES_MAX)
    rows, conflicts, unkeyed = listing_rows(compact)
    compact = None
    ranked, dropped = ranking(rows, conflicts, unkeyed)

    def fetch_gamma(cids):
        try:
            return docs_by_condition(loads_exact(fetch.gamma(cids)), cids)
        except ValueError:
            raise SelectionError("gamma request: not JSON")

    def fetch_clob(cid):
        raw = fetch.clob(cid)
        if raw is None:
            return None
        try:
            return loads_exact(raw)
        except ValueError:
            return "unreadable"

    members, walked, reasons, covered = walk(ranked, d0, fetch_gamma, fetch_clob, k=k, walk_max=walk_max)
    listing = {"pages": n_pages, "rows": n_rows, "distinct": len(rows),
               "conflicts": len(conflicts), "dropped": dict(sorted(dropped.items())), "ranked": len(ranked)}
    return {"listing": listing, "walked": len(walked), "covered": covered, "reasons": dict(sorted(reasons.items())),
            "walk": walked, "members": members}


def rule_record():
    return {"set_size": SET_SIZE, "walk_max": WALK_MAX, "gamma_batch": GAMMA_BATCH, "end_min_s": END_MIN_S,
            "event_band_s": list(EVENT_BAND_S), "excluded_tags": sorted(EXCLUDED_TAGS)}


def select_paths(ddir, a):
    return os.path.join(ddir, "select.%d.json" % a), os.path.join(ddir, "select.%d.replies.jsonl.gz" % a)


def next_attempt(ddir):
    a = 0
    while any(os.path.exists(p) for p in select_paths(ddir, a)):
        a += 1
    return a


def attempt_day(d0, root, urls=None, getter=None, sleep=time.sleep, k=SET_SIZE):
    """One attempt at day d0's selection: every reply written as it comes, the result written last. Returns the
    result, ok or not."""
    ddir = os.path.join(root, str(d0))
    os.makedirs(ddir, exist_ok=True)
    a = next_attempt(ddir)
    jpath, rpath = select_paths(ddir, a)
    started = time.time_ns()
    ok, reason, res = True, None, None
    with open(rpath, "xb") as fh:
        gz = gzip.GzipFile(filename="", mode="wb", fileobj=fh, compresslevel=GZ_LEVEL, mtime=0)
        lines = [0]

        def sink(rec):
            gz.write(json_line(rec))
            lines[0] += 1

        fetch = LiveFetch(sink, urls=urls, getter=getter, sleep=sleep)
        try:
            res = run_rule(fetch, d0, k=k)
        except SelectionError as exc:
            ok, reason = False, str(exc)
        finally:
            gz.close()
    size = os.path.getsize(rpath)
    account(size)
    rec = {"day": d0, "attempt": a, "ok": ok, "reason": reason, "pid": os.getpid(), "started_wall_ns": started,
           "finished_wall_ns": time.time_ns(),
           "replies": {"file": os.path.basename(rpath), "sha256": sha256_file(rpath), "bytes": size, "lines": lines[0],
                       "requests": fetch.requests},
           "listing": res["listing"] if res else None, "walked": res["walked"] if res else None,
           "reasons": res["reasons"] if res else None, "walk": res["walk"] if res else None,
           "members": res["members"] if res else None,
           "rule": dict(rule_record(), covered=res["covered"] if res else None)}
    assert frozenset(rec) == SELECT_KEYS, "select json keys"
    write_new(jpath, json_line(rec))
    return rec


def load_selection(ddir):
    """The day's first ok attempt, its replies' SHA-256 asserted against its record; None where there is none."""
    a = 0
    while True:
        jpath, rpath = select_paths(ddir, a)
        if not os.path.exists(jpath):
            if os.path.exists(rpath):
                a += 1
                continue
            return None
        with open(jpath, "rb") as fh:
            rec = json.loads(fh.read())
        if rec.get("ok") is True:
            assert sha256_file(rpath) == rec["replies"]["sha256"], "%s: replies differ from their record" % rpath
            return rec
        a += 1


# ---- the schedule: pure functions of instants ------------------------------------------------------------------


def day_of(t):
    return int(t) // DAY * DAY


def first_slot(now):
    """The slot a process starting at `now` runs first, and whether it joins it late - after its stream's open at
    S - 5: the current slot until S + 880, after that the next."""
    c = int(now) // SLOT * SLOT
    if now <= c + JOIN_LAST:
        return c, now > c - OPEN_BEFORE
    return c + SLOT, now > c + SLOT - OPEN_BEFORE


def selection_plan(now, have):
    """The days to attempt at `now` - today, and tomorrow from its D0 - 900 - less those already selected; and the
    next instant the plan changes."""
    today = day_of(now)
    due = [today]
    if now >= today + DAY - SELECT_LEAD_S:
        due.append(today + DAY)
    todo = [d for d in due if d not in have]
    nxt = today + DAY - SELECT_LEAD_S if now < today + DAY - SELECT_LEAD_S else today + 2 * DAY - SELECT_LEAD_S
    return todo, nxt


def slot_schedule(s):
    """A slot's instants: its stream, its summary, its last poll, and its polls' rounds and span."""
    return {"S": s, "open": s - OPEN_BEFORE, "close": s + CLOSE_AFTER, "json_at": s + SLOT_JSON_AT,
            "poll_last": s + REWARD_LAST, "rounds_ms": [off * 1000 for off in REWARD_ROUNDS],
            "span_ms": REWARD_SPAN_MS}


def poll_instants(sched, n_markets):
    """Each of n markets polled once a round, the round's polls spread evenly over its span, in time order."""
    polls = []
    for r, off in enumerate(sched["rounds_ms"]):
        for i in range(n_markets):
            polls.append((sched["S"] * 1000 + off + i * sched["span_ms"] // n_markets, r, i))
    polls.sort()
    return polls


def slot_paths(ddir, s, k):
    return {name: os.path.join(ddir, "%d.%d.%s" % (s, k, name)) for name in
            ("stream.jsonl.gz", "rewards.jsonl.gz", "slot.json")}


def slot_index(ddir, s):
    k = 0
    while any(os.path.exists(p) for p in slot_paths(ddir, s, k).values()):
        k += 1
    return k

# ---- the network: the stream -------------------------------------------------------------------------------------


def subscription(tokens):
    """The documented subscribe frame, compact, the tokens in the day's set's order."""
    return json.dumps({"assets_ids": list(tokens), "type": "market"}, separators=(",", ":"))


def connect_kwargs(proxy=True):
    """Every option of the opening handshake, fixed: no compression offered, no protocol ping, this file's
    User-Agent; `proxy` is websockets' own default, the environment's; None on the loopback."""
    return {"open_timeout": OPEN_TIMEOUT_S, "close_timeout": CLOSE_TIMEOUT_S, "ping_interval": None,
            "max_size": MAX_FRAME, "max_queue": MAX_QUEUE, "compression": None, "user_agent_header": UA,
            "proxy": proxy}


class StreamWriter:
    """One stream file: gzip, a sync flush at least every FLUSH_S, one JSON line per received frame - recv_ns,
    mono_ns and raw, the frame verbatim - and one per session event; the last an `end` line."""

    def __init__(self, path, level=GZ_STREAM, slot_max=SLOT_STREAM_MAX, flush_s=FLUSH_S):
        self.path = path
        self.fh = open(path, "xb")
        self.gz = gzip.GzipFile(filename="", mode="wb", fileobj=self.fh, compresslevel=level, mtime=0)
        self.slot_max, self.flush_s = slot_max, flush_s
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
        if self.stored >= self.slot_max:
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
        return {"frames": self.frames, "frame_bytes": self.frame_bytes, "pongs": self.pongs, "pings": self.pings,
                "first_frame_wall_ns": self.first, "last_frame_wall_ns": self.last, "max_gap_ns": self.max_gap,
                "subscribed_wall_ns": self.subscribed, "cut": self.cut}


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
            w.event("subscribe", seg=seg, tokens=len(tokens), message_sha256=sha256_bytes(msg.encode("utf-8")))
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


def new_stream_stats():
    return {"opened": False, "off_reason": None, "file": None, "segments": 0, "frames": 0, "frame_bytes": 0,
            "pongs": 0, "pings": 0, "first_frame_wall_ns": None, "last_frame_wall_ns": None, "max_gap_ns": None,
            "subscribed_wall_ns": None, "stored_bytes": 0, "cut": False}


async def stream_slot(path, tokens, start, end, stats, url=CLOB_WS_URL, ping_s=PING_S, kw=None, backoff=BACKOFF_S,
                      level=GZ_STREAM, slot_max=SLOT_STREAM_MAX):
    """The stream of one slot: sessions from `start` to `end` into one file, a reconnect after each drop."""
    if not await sleep_until(start):
        return
    kw = connect_kwargs() if kw is None else kw
    w = StreamWriter(path, level=level, slot_max=slot_max)
    stats["opened"] = True
    stats["file"] = os.path.basename(path)
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
        stats["segments"] = seg
        stats.update({k: v for k, v in w.summary().items()})
        stats["stored_bytes"] = w.stored


def stream_bytes_total(root):
    """The bytes of every stream file under root, by directory entries alone - read again at every slot."""
    total = 0
    if not os.path.isdir(root):
        return 0
    with os.scandir(root) as it:
        dirs = sorted(d.path for d in it if d.is_dir(follow_symlinks=False) and DAY_RE.fullmatch(d.name))
    for d in dirs:
        with os.scandir(d) as it:
            for f in it:
                if f.name.endswith(".stream.jsonl.gz") and SLOT_FILE_RE.fullmatch(f.name):
                    total += f.stat(follow_symlinks=False).st_size
    return total


def stream_off_reason(selected, n_members, free, total):
    """Why no stream opens for a slot, or None: the selection, an empty set, the stream floor, the stream cap."""
    if not selected:
        return "no selection"
    if n_members == 0:
        return "empty set"
    if free < STREAM_FLOOR:
        return "floor"
    if total >= STREAM_CAP:
        return "cap"
    return None

# ---- the reward documents: three polls of every member a slot ----------------------------------------------------


def poll_rows(rec, cid):
    """The rows of the polled market a reward reply carries - 0 or 1 - or None where the poll is not served: a
    status other than 200, a body that is not a page, more than one row, or a row of another market."""
    if rec.get("status") != 200:
        return None
    try:
        obj = json.loads(rec.get("raw") or "")
    except ValueError:
        return None
    rows = obj.get("data") if isinstance(obj, dict) else None
    if not isinstance(rows, list) or len(rows) > 1:
        return None
    if rows and not (isinstance(rows[0], dict) and rows[0].get("condition_id") == cid):
        return None
    return len(rows)


def poll_served(rec, cid):
    """A poll is served when the venue answered 200 with a page of at most one row, of the polled market; a page
    without a row is the venue's record that the market pays no reward now."""
    return poll_rows(rec, cid) is not None


async def poll_rewards(sched, polls, members, lines, counts, url=CLOB_REWARDS_URL, getter=None):
    """Each member's polls at its instants; an instant already past when the slot's task starts is missed, and so is
    one past the slot's last poll instant."""
    getter = getter or (lambda u: http_get(u, timeout=POLL_TIMEOUT_S))
    started = time.time()
    for due_ms, r, i in polls:
        due = due_ms / 1000
        if due < started or time.time() > sched["poll_last"]:
            counts["missed"] += 1
            continue
        if not await sleep_until(due):
            break
        cid = members[i]["condition_id"]
        res = await asyncio.to_thread(getter, url.format(condition_id=cid))
        rec = {"S": sched["S"], "round": r, "i": i, "condition_id": cid, "due_wall_ns": due_ms * 1000000}
        rec.update({k: res[k] for k in ("url", "status", "send_wall_ns", "send_mono_ns", "recv_mono_ns",
                                        "recv_wall_ns", "bytes", "sha256", "raw", "reason")})
        assert frozenset(rec) == POLL_KEYS, "poll keys"
        lines.append(json_line(rec))
        counts["polled"] += 1
        got = poll_rows(rec, cid)
        counts["served"] += 0 if got is None else 1
        counts["rows"] += got or 0
        st = "null" if rec["status"] is None else str(rec["status"])
        counts["status_counts"][st] = counts["status_counts"].get(st, 0) + 1

# ---- the service ----------------------------------------------------------------------------------------------


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
                      "service_argv": list(SERVICE_ARGV), "urls": dict(sorted(URLS.items())),
                      "rule": rule_record(), "slot": SLOT, "stream": [-OPEN_BEFORE, CLOSE_AFTER],
                      "slot_json_at": SLOT_JSON_AT, "reward_rounds": list(REWARD_ROUNDS),
                      "reward_span_ms": REWARD_SPAN_MS, "select_lead_s": SELECT_LEAD_S, "ping_s": PING_S,
                      "gz_stream": GZ_STREAM, "flush_s": FLUSH_S, "max_frame": MAX_FRAME, "max_queue": MAX_QUEUE,
                      "resource_floor": RESOURCE_FLOOR, "stream_floor": STREAM_FLOOR, "stream_cap": STREAM_CAP,
                      "slot_stream_max": SLOT_STREAM_MAX, "write_cap": WRITE_CAP, "malloc_tuned": MALLOC_TUNED}}
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


class Book:
    """The service's state shared by its tasks: the selections by day, the attempts made, a halt."""

    def __init__(self, root, urls=None, getter=None, k=SET_SIZE):
        self.root, self.urls, self.getter, self.k = root, dict(URLS, **(urls or {})), getter, k
        self.selections = {}
        self.attempts = Counter()
        self.halt = []
        self.free = free_bytes

    def load(self, d0):
        ddir = os.path.join(self.root, str(d0))
        if d0 in self.selections or not os.path.isdir(ddir):
            return
        rec = load_selection(ddir)
        if rec is not None:
            self.selections[d0] = {"rec": rec, "sha256": sha256_file(select_paths(ddir, rec["attempt"])[0])}
            out("day %d (%s): selection attempt %d loaded, %d members" % (d0, utc(d0), rec["attempt"],
                                                                          len(rec["members"])))

    def floor(self):
        """The free bytes, read now; FloorStop below RESOURCE_FLOOR."""
        free = self.free()
        if free < RESOURCE_FLOOR:
            raise FloorStop("free %d bytes, below the floor %d" % (free, RESOURCE_FLOOR))
        return free

    async def ensure(self, d0):
        """One attempt at day d0's selection where none is held; a runtime record of it."""
        self.load(d0)
        if d0 in self.selections or self.attempts[d0] >= SELECT_ATTEMPTS_MAX or stopping():
            return
        self.floor()
        self.attempts[d0] += 1
        t0 = time.time()
        rec = await asyncio.to_thread(attempt_day, d0, self.root, self.urls, self.getter, time.sleep, self.k)
        ddir = os.path.join(self.root, str(d0))
        n = len(rec["members"]) if rec["ok"] else 0
        runtime_record(self.root, "select", {"day": d0, "attempt": rec["attempt"], "ok": rec["ok"],
                                             "reason": rec["reason"], "members": n,
                                             "requests": rec["replies"]["requests"],
                                             "seconds": round(time.time() - t0, 3)})
        out("day %d (%s): selection attempt %d %s, %d members, %d requests, %.1f s%s" % (
            d0, utc(d0), rec["attempt"], "ok" if rec["ok"] else "failed", n, rec["replies"]["requests"],
            time.time() - t0, "" if rec["ok"] else ": " + rec["reason"]))
        if rec["ok"]:
            self.selections[d0] = {"rec": rec, "sha256": sha256_file(select_paths(ddir, rec["attempt"])[0])}

    async def selection_loop(self):
        while not stopping():
            todo, nxt = selection_plan(time.time(), set(self.selections))
            for d0 in todo:
                await self.ensure(d0)
            for d0 in [d for d in self.selections if d < day_of(time.time()) - DAY]:
                del self.selections[d0]
            todo, nxt = selection_plan(time.time(), set(self.selections))
            pending = [d for d in todo if self.attempts[d] < SELECT_ATTEMPTS_MAX]
            await sleep_until(min(nxt, time.time() + SELECT_RETRY_S) if pending else nxt)

    async def selection_for(self, d0, deadline):
        while not stopping():
            if d0 in self.selections:
                return self.selections[d0]
            if time.time() >= deadline:
                return None
            await sleep_until(min(deadline, time.time() + 1))
        return self.selections.get(d0)


async def run_slot(book, sched, ws_url=CLOB_WS_URL, kw=None, ping_s=PING_S, backoff=BACKOFF_S, poll_url=CLOB_REWARDS_URL,
                   poll_getter=None, join_last=None):
    """One slot, the whole of it: the day's selection, the stream and the polls, the rewards file, the summary."""
    book.floor()
    s = sched["S"]
    d0 = day_of(s)
    ddir = os.path.join(book.root, str(d0))
    os.makedirs(ddir, exist_ok=True)
    task_wall = time.time_ns()
    joined_late = task_wall / 1e9 > sched["open"]
    k = slot_index(ddir, s)
    paths = slot_paths(ddir, s, k)
    sel = await book.selection_for(d0, s + JOIN_LAST if join_last is None else join_last)
    members = sel["rec"]["members"] if sel else []
    tokens = [t for m in members for t in m["token_ids"]]
    stats = new_stream_stats()
    stats["off_reason"] = "stopped" if stopping() else \
        stream_off_reason(sel is not None, len(members), book.free(), stream_bytes_total(book.root))
    polls = poll_instants(sched, len(members)) if members else []
    counts = {"polled": 0, "missed": 0, "served": 0, "rows": 0, "status_counts": {}}
    lines, error, tasks = [], None, []
    if stats["off_reason"] is None:
        tasks.append(asyncio.create_task(stream_slot(paths["stream.jsonl.gz"], tokens, max(sched["open"], time.time()),
                                                     sched["close"], stats, url=ws_url, ping_s=ping_s, kw=kw,
                                                     backoff=backoff)))
    if polls and not stopping():
        tasks.append(asyncio.create_task(poll_rewards(sched, polls, members, lines, counts, url=poll_url,
                                                      getter=poll_getter)))
    try:
        for t in tasks:
            try:
                await t
            except (GuardError, FloorStop):
                raise
            except Exception as exc:
                error = "%s: %s" % (type(exc).__name__, str(exc)[:300])
    finally:
        for t in tasks:
            if not t.done():
                t.cancel()
    rew = {"file": None, "scheduled": len(polls), "polled": counts["polled"], "missed": counts["missed"],
           "served": counts["served"], "rows": counts["rows"], "status_counts": counts["status_counts"], "stored_bytes": 0}
    if lines:
        body = gzip.compress(b"".join(lines), compresslevel=GZ_LEVEL, mtime=0)
        write_new(paths["rewards.jsonl.gz"], body)
        rew.update({"file": os.path.basename(paths["rewards.jsonl.gz"]), "stored_bytes": len(body)})
    await sleep_until(sched["json_at"])
    assert frozenset(stats) == STREAM_KEYS and frozenset(rew) == REWARDS_JSON_KEYS, "slot json parts"
    sj = {"S": s, "day": d0, "index": k, "pid": os.getpid(), "task_wall_ns": task_wall, "joined_late": joined_late,
          "stopped": stopping(), "selection": None if sel is None else selection_id_of(sel), "markets": len(members),
          "tokens": len(tokens), "stream": stats, "rewards": rew, "closed_wall_ns": time.time_ns(), "error": error}
    assert_keys(sj, SLOT_JSON_KEYS, "slot json")
    write_new(paths["slot.json"], json_line(sj))
    out("slot %d (%s) index %d: %d markets; stream %s, %d frames, %d segments, %d bytes; polls %d served of %d, %d "
        "with a row, %d missed%s%s" % (s, utc(s), k, len(members),
                                       "opened" if stats["opened"] else "off (%s)" % stats["off_reason"],
                                       stats["frames"], stats["segments"], stats["stored_bytes"], counts["served"],
                                       len(polls), counts["rows"], counts["missed"], ", stopped" if sj["stopped"] else "",
                                       ", error " + error if error else ""))
    return sj


def selection_id_of(sel):
    return {"day": sel["rec"]["day"], "attempt": sel["rec"]["attempt"], "sha256": sel["sha256"]}


async def guarded(book, coro, what):
    """A task of the service: a floor or a refused open halts it; anything else is an error record."""
    try:
        return await coro
    except (FloorStop, GuardError) as exc:
        book.halt.append("%s: %s" % (what, exc))
        try:
            runtime_record(book.root, "halt", {"what": what, "reason": str(exc)[:300]})
        except Exception:
            pass
        out("halt in %s: %s" % (what, exc))
        request_stop()
    except Exception as exc:
        runtime_record(book.root, "error", {"what": what, "error": "%s: %s" % (type(exc).__name__, str(exc)[:300])})
        out("%s error: %r" % (what, exc))


async def serve_main(root=None, urls=None, slots=None):
    """The service's loop. `slots` bounds the number of slots launched; None in the service."""
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
    if not MALLOC_TUNED:
        out("refusing to start: glibc did not take the mmap threshold and the arena count")
        return 1
    os.makedirs(root, exist_ok=True)
    if acquire_single_instance(root) is None:
        return 3
    total = stream_bytes_total(root)
    rec = runtime_record(root, "start", {"free_bytes": free, "stream_bytes": total})
    out("start record: pid %d commit %s file_sha256 %s; free %d bytes, streams %d bytes" % (
        rec["pid"], rec["commit"], rec["file_sha256"], free, total))
    book = Book(root, urls=urls)
    sel_task = asyncio.create_task(guarded(book, book.selection_loop(), "selection"))
    tasks, launched = set(), 0
    s, _late = first_slot(time.time())
    try:
        while not stopping() and (slots is None or launched < slots):
            if not await sleep_until(s - OPEN_BEFORE - LAUNCH_LEAD):
                break
            t = asyncio.create_task(guarded(book, run_slot(book, slot_schedule(s), ws_url=book.urls["ws"],
                                                           poll_url=book.urls["rewards"]), "slot %d" % s))
            tasks.add(t)
            t.add_done_callback(tasks.discard)
            launched += 1
            s += SLOT
        if slots is not None:
            while tasks and not stopping():
                await asyncio.sleep(0.2)
            request_stop()
    finally:
        await asyncio.gather(*list(tasks), sel_task, return_exceptions=True)
        rc = 1 if book.halt else 0
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

# ---- reading what the service stored: total, it never raises on data --------------------------------------------


def stream_rows(path, report):
    """Every complete line of a stream file, parsed, read incrementally in pieces of at most 4 MiB; `report` gets
    `torn` - cut before its trailer, or with bytes past it - and `bad`, the lines that do not parse."""
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


def frame_tokens(obj):
    """The event types and token ids a parsed frame names, and the venue time of a price_change, or None where the
    frame does not conform to the documented market channel."""
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


def read_json_file(path):
    try:
        with open(path, "rb") as fh:
            obj = json.loads(fh.read())
    except (OSError, ValueError):
        return None
    return obj


def slot_unit(s, path, sj, tokens):
    """G-STREAM's unit: the reasons a slot's stream is not complete, none where it is, and its counts. Reads a frame
    for its JSON shape, event types, token ids and the venue's time, and nothing else."""
    if not isinstance(sj, dict) or frozenset(sj) != SLOT_JSON_KEYS:
        return ["slot json"], {}
    st = sj.get("stream") if isinstance(sj.get("stream"), dict) else {}
    if frozenset(st) != STREAM_KEYS:
        return ["slot json"], {}
    why = []
    for flag in ("joined_late", "stopped"):
        if sj.get(flag):
            why.append(flag.replace("_", " "))
    if sj.get("error"):
        why.append("error")
    if not st["opened"] or not st["file"]:
        why.append("no stream (%s)" % st["off_reason"])
        return why, {}
    want = set(tokens)
    s_ = {"frames": 0, "pongs": 0, "types": {}, "nonconforming": 0, "foreign": 0, "torn": 0, "bad_lines": 0,
          "stored_bytes": 0, "subscribes": 0, "closes": 0, "pings": 0, "max_gap_ns": None, "subscribe_offset_ms": None,
          "last_close_offset_ms": None, "lag_ms": None, "initial_tokens": 0}
    lags, early, sub0, last, end = Counter(), set(), None, None, None
    gap = 0
    if not os.path.isfile(path):
        return why + ["missing stream file"], s_
    s_["stored_bytes"] = os.path.getsize(path)
    rep = {"torn": False, "bad": 0}
    ended = False
    types = Counter()
    for r in stream_rows(path, rep):
        ended = False
        if not isinstance(r, dict) or type(r.get("recv_ns")) is not int:
            s_["bad_lines"] += 1
            continue
        t = r["recv_ns"]
        ev = r.get("event")
        if ev is not None:
            if ev == "subscribe":
                s_["subscribes"] += 1
                if sub0 is None:
                    sub0 = t
            elif ev == "close":
                s_["closes"] += 1
                end = t
            elif ev == "ping":
                s_["pings"] += 1
            elif ev == "end":
                ended = True
            if ev in ("subscribe", "close") and last is not None:
                gap = max(gap, t - last)
            if ev in ("subscribe", "close") and sub0 is not None:
                last = t
            continue
        keys = frozenset(r)
        if keys == FRAME_B64_KEYS:
            s_["nonconforming"] += 1
        elif keys != FRAME_KEYS or not isinstance(r["raw"], str):
            s_["bad_lines"] += 1
            continue
        s_["frames"] += 1
        if sub0 is not None:
            if last is not None:
                gap = max(gap, t - last)
            last = t
        if keys == FRAME_B64_KEYS:
            continue
        raw = r["raw"]
        if raw == "PONG":
            s_["pongs"] += 1
            continue
        try:
            obj = json.loads(raw)
        except ValueError:
            s_["nonconforming"] += 1
            continue
        got = frame_tokens(obj)
        if got is None:
            s_["nonconforming"] += 1
            continue
        tys, toks, ts = got
        for ty in tys:
            types[ty] += 1
        if not toks <= want:
            s_["foreign"] += 1
        if ts is not None:
            lags[min(max(t // 1000000 - ts, LAG_RANGE_MS[0]), LAG_RANGE_MS[1])] += 1
        if "book" in tys and sub0 is not None and t <= sub0 + INITIAL_S * 10 ** 9:
            for it in (obj if isinstance(obj, list) else [obj]):
                if it.get("event_type") == "book":
                    early.add(it["asset_id"])
    s_["torn"] = 1 if rep["torn"] else 0
    s_["bad_lines"] += rep["bad"]
    s_["types"] = sorted([k, v] for k, v in types.items())
    s_["initial_tokens"] = len(early & want)
    if not ended:
        why.append("no end line")
    for k, flag in (("torn", "torn"), ("bad_lines", "bad lines"), ("nonconforming", "nonconforming frames"),
                    ("foreign", "foreign tokens")):
        if s_[k]:
            why.append(flag)
    if sub0 is None:
        why.append("no subscribe")
    else:
        s_["subscribe_offset_ms"] = (sub0 - s * 10 ** 9) // 1000000
        if sub0 > s * 10 ** 9:
            why.append("late subscribe")
        if not want <= early:
            why.append("initial books")
        s_["max_gap_ns"] = gap
        if gap > GAP_MAX_NS:
            why.append("gap")
    if end is None or end < (s + 900) * 10 ** 9:
        why.append("short")
    if end is not None:
        s_["last_close_offset_ms"] = (end - s * 10 ** 9) // 1000000
    if s_["frames"] != st["frames"]:
        why.append("count")
    if st["cut"]:
        why.append("cut")
    s_["lag_ms"] = counted_quantiles(lags)
    return why, s_


def rewards_unit(path, sj, members):
    """G-REWARDS' count over a slot: the polls scheduled, the lines stored, the polls served; each line's market the
    member its index names. Reads a body for its status, its JSON shape and its row's condition id alone."""
    n = {"scheduled": 0, "lines": 0, "served": 0, "rows": 0, "mismatched": 0, "unreadable": 0, "statuses": {}}
    if not isinstance(sj, dict) or not isinstance(sj.get("rewards"), dict):
        return n
    n["scheduled"] = sj["rewards"].get("scheduled") or 0
    if not sj["rewards"].get("file") or not os.path.isfile(path):
        return n
    try:
        with open(path, "rb") as fh:
            data = gzip.decompress(fh.read())
    except (OSError, EOFError, zlib.error):
        n["unreadable"] += 1
        return n
    for ln in data.split(b"\n"):
        if not ln:
            continue
        try:
            rec = json.loads(ln)
        except ValueError:
            n["unreadable"] += 1
            continue
        if not isinstance(rec, dict) or frozenset(rec) != POLL_KEYS:
            n["unreadable"] += 1
            continue
        n["lines"] += 1
        i = rec.get("i")
        if not (isinstance(i, int) and 0 <= i < len(members) and members[i]["condition_id"] == rec["condition_id"]):
            n["mismatched"] += 1
            continue
        st = "null" if rec["status"] is None else str(rec["status"])
        n["statuses"][st] = n["statuses"].get(st, 0) + 1
        got = poll_rows(rec, rec["condition_id"])
        n["served"] += 0 if got is None else 1
        n["rows"] += got or 0
    n["statuses"] = dict(sorted(n["statuses"].items()))
    return n


def read_runtime(path):
    recs = []
    with open(path, "rb") as fh:
        for ln in fh.read().split(b"\n"):
            if ln.strip():
                recs.append(json.loads(ln))
    return recs


def read_g_stream(units):
    """units: whether each of the first qualifying slots is complete, in order."""
    if len(units) < GATE_SLOTS:
        return "UNDECIDABLE"
    return "PASS" if sum(1 for u in units[:GATE_SLOTS] if u) >= GATE_STREAM_PASS else "FAIL"


def read_g_rewards(n_slots, scheduled, served):
    if n_slots < GATE_SLOTS or scheduled == 0:
        return "UNDECIDABLE"
    return "PASS" if Fraction(served, scheduled) >= REWARDS_PASS else "FAIL"


def read_neighbors(rows):
    """rows: (kind, counted, ok). BROKEN on any counted failure; HOLD with enough counted of both kinds."""
    if any(c and not ok for _k, c, ok in rows):
        return "BROKEN"
    if all(sum(1 for k, c, ok in rows if k == kind and c and ok) >= NEIGHBOR_MIN[kind] for kind in NEIGHBOR_MIN):
        return "HOLD"
    return "UNDECIDABLE"


def comb(n, k):
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c


def p_fail_at_least(n, k, p):
    """P(at least k of n independent units fail, each with probability p), exact: one less the k terms below k."""
    return 1 - sum(comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k))


def p_false_alarm(f, m, units):
    if m == 0:
        return None
    return 1 - (1 - Fraction(f, m)) ** units


def p_false_alarm_both(rates, units):
    """G-NEIGHBORS' false failure: a counted failure among the units of both kinds, each failing at its base rate."""
    keep = Fraction(1)
    for kind in ("recorder", "pairbook"):
        if rates[kind]["m"] == 0:
            return None
        keep *= (1 - Fraction(rates[kind]["f"], rates[kind]["m"])) ** units[kind]
    return 1 - keep


def manifest_of(t0, a):
    """A five-minute interval's manifest as of a: (counted, quotes_complete)."""
    p = "%s/btc-updown-5m/%d/manifest.json" % (RECORDER, t0)
    try:
        st = os.stat(p)
    except OSError:
        return False, None
    if st.st_mtime_ns > a * 10 ** 9:
        return False, None
    m = read_json_file(p)
    return True, (m.get("quotes_complete") if isinstance(m, dict) else None)


def pairbook_window_ok(wj):
    """The pair book's window, from its window.json alone: documents, the stream opened, seven checkpoints."""
    if not isinstance(wj, dict):
        return False
    st = wj.get("stream") if isinstance(wj.get("stream"), dict) else {}
    return (wj.get("documents_ok") is True and st.get("opened") is True and st.get("off_reason") is None
            and wj.get("checkpoints_complete") == 7 and wj.get("stopped") is False)


def window_of(t, a):
    """The pair book's window T as of a: (counted, ok)."""
    p = "%s/%d/window.json" % (PAIRBOOK, t)
    try:
        st = os.stat(p)
    except OSError:
        return False, None
    if st.st_mtime_ns > a * 10 ** 9:
        return False, None
    return True, pairbook_window_ok(read_json_file(p))


def recorder_units(lo, hi):
    """The recorder's five-minute intervals that open and close inside [lo, hi]."""
    t0 = -(-lo // 300) * 300
    found = []
    while t0 + 300 <= hi:
        found.append(t0)
        t0 += 300
    return found


def pairbook_units(lo, hi):
    """The pair book's windows whose stream, T+595 to T+905, lies inside [lo, hi]."""
    t = -(-(lo - 595) // 900) * 900
    found = []
    while t + 905 <= hi:
        found.append(t)
        t += 900
    return found


def neighbor_units(lo, hi, a):
    """The neighbours' units inside [lo, hi], each read as of a."""
    rows = []
    for t0 in recorder_units(lo, hi):
        c, q = manifest_of(t0, a)
        rows.append({"kind": "recorder", "unit": t0, "counted": c, "ok": q is True})
    for t in pairbook_units(lo, hi):
        c, ok = window_of(t, a)
        rows.append({"kind": "pairbook", "unit": t, "counted": c, "ok": ok is True})
    return rows


def base_rates(p):
    """The neighbours' failure rates in the week before p: the recorder's last 2,016 intervals closed 600 s before p,
    by their manifests' quotes_complete; the pair book's last 672 windows whose window.json was due 60 s before p, by
    that file; for each the units, those read (m) and those failing (f)."""
    res = {}
    t_scan = time.monotonic()
    r_last = (p - 900) // 300 * 300
    m = f = 0
    for j in range(BASE_INTERVALS):
        if j == 100:
            assert time.monotonic() - t_scan <= 30, "base rates: the first 100 manifests took over 30 s"
        c, q = manifest_of(r_last - 300 * j, p)
        if c:
            m += 1
            f += 0 if q is True else 1
    res["recorder"] = {"slots": BASE_INTERVALS, "m": m, "f": f, "last": r_last}
    w_last = (p - 970) // 900 * 900
    m = f = 0
    for j in range(BASE_WINDOWS):
        c, ok = window_of(w_last - 900 * j, p)
        if c:
            m += 1
            f += 0 if ok else 1
    res["pairbook"] = {"slots": BASE_WINDOWS, "m": m, "f": f, "last": w_last}
    return res

# ---- the modes ---------------------------------------------------------------------------------------------------


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
        out("%-46s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
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


def ledger_restarts(since_ns):
    """The archive's restart records since an instant, in order, from its own ledger."""
    with open(ARCHIVE_LEDGER, "rb") as fh:
        raw = fh.read()
    recs = [json.loads(ln) for ln in raw.split(b"\n")[:-1] if ln.strip()]
    return [r for r in recs if r.get("event") == "restart" and r.get("wall_ns", 0) >= since_ns]


def still_reading(before, now, restarts):
    """G-STILL from the two reads and the archive's restart records between them, in order: PASS where both units
    are unchanged, or where the recorder is unchanged and the pair book's change is the archive's own restarts
    alone - a chain of records from the recorded MainPID to the current one, NRestarts one higher at each, the unit
    active. Pure: it reads nothing but its arguments."""
    if now == before:
        return True, "unchanged"
    if now["recorder"] != before["recorder"]:
        return False, "the recorder changed"
    b, n = before["pairbook"], now["pairbook"]
    pid, count = b["MainPID"], int(b["NRestarts"])
    for r in restarts:
        if str(r.get("stopped")) != pid or str(r.get("NRestarts")) != str(count + 1):
            return False, "a restart record that does not follow %s at NRestarts %d: %r" % (pid, count, r)
        pid, count = str(r.get("pid")), count + 1
    if restarts and pid == n["MainPID"] and str(count) == n["NRestarts"] and n["ActiveState"] == "active":
        return True, "changed by the archive's own restarts alone: %d" % len(restarts)
    return False, "the pair book changed, %d restart records of the archive since the first read" % len(restarts)


def mode_still():
    """G-STILL: the recorder and the pair book. The first run records them; a later run compares. A FAIL runs no
    block: the report names its cause from both units' journal (section 4.7)."""
    st = load_state()
    now = {}
    for key, unit in sorted(NEIGHBORS.items()):
        kv = systemctl_show(unit, ["MainPID", "NRestarts", "ActiveState", "MemoryCurrent", "MemoryPeak"])
        now[key] = {k: kv.get(k) for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, MemoryCurrent %s, MemoryPeak %s" % (unit, now[key], kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    for unit in (ARCHIVE_TIMER, ARCHIVE_UNIT):
        kv = systemctl_show(unit, ["ActiveState", "SubState", "UnitFileState", "Result"])
        out("%s %s" % (unit, kv))
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "at_ns": time.time_ns(), "units": now}
        save_state(st)
        out("still: recorded")
        return True
    restarts = ledger_restarts(st["still"]["at_ns"])
    for r in restarts:
        out("the archive's restart record %s: run %s, window %s, pid %s after %s, NRestarts %s" % (
            utc(r["wall_ns"] / 1e9), r.get("run"), r.get("W"), r.get("pid"), r.get("stopped"), r.get("NRestarts")))
    ok, why = still_reading(st["still"]["units"], now, restarts)
    out("G-STILL %s: %s since %s" % ("PASS" if ok else "FAIL", why, st["still"]["at"]))
    return ok


def mode_mark(name):
    assert name in ("start-svc", "kill-svc", "stop"), "mark %r" % name
    st = load_state()
    marks = st.setdefault("marks", {})
    assert name not in marks, "mark %s already taken" % name
    kv = systemctl_show(UNIT, ["MainPID", "NRestarts", "ActiveState"])
    marks[name] = {"ns": time.time_ns(), "unit": UNIT, "MainPID": kv.get("MainPID"), "NRestarts": kv.get("NRestarts"),
                   "ActiveState": kv.get("ActiveState")}
    save_state(st)
    out("mark %s at %s: %s %r" % (name, utc(marks[name]["ns"] / 1e9), UNIT, marks[name]))


def unit_reads(n_restarts):
    kv = systemctl_show(UNIT, ["ActiveState", "SubState", "UnitFileState", "FragmentPath", "ControlGroup",
                               "MemoryMax", "Nice", "NRestarts", "MainPID", "MemoryCurrent", "MemoryPeak"])
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
              "nice": kv["Nice"] == str(NICE),
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
            "headers": first.get("config", {}).get("headers") == [["Accept", ACCEPT], ["User-Agent", UA]],
            "malloc": first.get("config", {}).get("malloc_tuned") is True})
        out("G-START: the start record of pid %s at %s, commit %s, file %s" % (
            first.get("pid"), utc(first.get("wall_ns", 0) / 1e9), first.get("commit"), first.get("file_sha256")))
    for k, v in checks.items():
        out("G-UNIT %-16s %s" % (k, v))
    out("%s MainPID %d, NRestarts %s, MemoryMax %s, MemoryCurrent %s, MemoryPeak %s" % (
        UNIT, pid, kv["NRestarts"], kv["MemoryMax"], kv["MemoryCurrent"], kv["MemoryPeak"]))
    assert all(checks.values()), "G-UNIT FAIL: %r" % {k: v for k, v in checks.items() if not v}
    out("G-UNIT PASS at %d restarts%s" % (n, "; G-START PASS" if n == 0 else ""))


def mode_restart():
    """G-RESTART: since the kill mark, the records are a stop of the marked MainPID and a start of another,
    within RESTART_MAX_S, on the same commit and file; G-UNIT at one restart."""
    st = load_state()
    mark = st.get("marks", {}).get("kill-svc")
    assert mark is not None, "restart: no kill-svc mark"
    recs = read_runtime(ROOT + "/runtime.jsonl")
    after = [r for r in recs if r.get("wall_ns", 0) >= mark["ns"] and r.get("event") in ("start", "stop")]
    for r in after:
        out("record %s pid %s at %s" % (r.get("event"), r.get("pid"), utc(r["wall_ns"] / 1e9)))
    first = [r for r in recs if r.get("event") == "start"][0]
    ok = (len(after) == 2 and after[0].get("event") == "stop" and str(after[0].get("pid")) == str(mark["MainPID"])
          and after[1].get("event") == "start" and after[1].get("pid") != after[0].get("pid")
          and after[1]["wall_ns"] - after[0]["wall_ns"] <= RESTART_MAX_S * 10 ** 9
          and after[1].get("commit") == first.get("commit") and after[1].get("file_sha256") == first.get("file_sha256"))
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
    """G-LOAD: the service's processor time since its process started, at most LOAD_MAX of the elapsed wall time;
    its memory printed."""
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
    ok = mode_still()
    kv = systemctl_show(UNIT, ["MainPID", "ControlGroup"])
    for k, v in cgroup_memory("/sys/fs/cgroup" + kv["ControlGroup"]).items():
        out("%s %s" % (k, v))
    out("FINAL PASS: G-UNIT at one restart; G-STILL %s" % ("PASS" if ok else "FAIL, recorded"))


def mode_stopped():
    """After K-33: the reward book stopped through systemd, disabled, no process left, its record ending in a stop
    at or after the stop mark."""
    st = load_state()
    mark = st.get("marks", {}).get("stop")
    assert mark is not None, "stopped: no stop mark"
    recs = read_runtime(ROOT + "/runtime.jsonl")
    checks = {"inactive": systemctl_word("is-active", UNIT) in ("inactive", "failed"),
              "disabled": systemctl_word("is-enabled", UNIT) == "disabled",
              "no process": processes_with(SERVICE_ARGV) == [],
              "stop record": bool(recs) and recs[-1].get("event") == "stop" and recs[-1].get("wall_ns", 0) >= mark["ns"]}
    for k, v in checks.items():
        out("STOPPED %-12s %s" % (k, v))
    assert all(checks.values()), "STOPPED FAIL: %r" % {k: v for k, v in checks.items() if not v}
    out("STOPPED PASS: the reward book stopped at %s" % utc(recs[-1]["wall_ns"] / 1e9))


def considered(s_, s, a):
    return s_ + JOIN_LAST >= s and s_ + SLOT_JSON_AT <= min(a, s + BUDGET_S)


def qualifies(s_, s, a):
    return s_ - OPEN_BEFORE >= s + QUALIFY_LEAD_S and s_ + SLOT_JSON_AT <= min(a, s + BUDGET_S)


def day_selection(d0, cache):
    """The day's selection as the service holds it: its first ok attempt and that attempt's file hash."""
    if d0 not in cache:
        ddir = os.path.join(ROOT, str(d0))
        rec = load_selection(ddir) if os.path.isdir(ddir) else None
        cache[d0] = None if rec is None else {"rec": rec, "sha256": sha256_file(select_paths(ddir, rec["attempt"])[0])}
    return cache[d0]


def slot_row(s, q, cache):
    """One considered slot, read: every index's summary flags; for index 0 alone, the stream unit and the polls."""
    d0 = day_of(s)
    ddir = os.path.join(ROOT, str(d0))
    sel = day_selection(d0, cache)
    members = sel["rec"]["members"] if sel else []
    tokens = [t for m in members for t in m["token_ids"]]
    row = {"S": s, "qualifying": q, "indices": []}
    k = 0
    while True:
        paths = slot_paths(ddir, s, k)
        if not any(os.path.exists(p) for p in paths.values()):
            break
        sj = read_json_file(paths["slot.json"])
        flags = {"index": k, "slot_json": isinstance(sj, dict)}
        if isinstance(sj, dict):
            st = sj.get("stream") if isinstance(sj.get("stream"), dict) else {}
            flags.update({"joined_late": sj.get("joined_late"), "stopped": sj.get("stopped"), "error": sj.get("error"),
                          "markets": sj.get("markets"), "stream_opened": st.get("opened"),
                          "stream_off": st.get("off_reason"), "segments": st.get("segments"),
                          "frames": st.get("frames")})
        row["indices"].append(flags)
        k += 1
    paths = slot_paths(ddir, s, 0)
    sj = read_json_file(paths["slot.json"])
    why, stats = slot_unit(s, paths["stream.jsonl.gz"], sj, tokens)
    if len(row["indices"]) != 1:
        why = why + ["indices %d" % len(row["indices"])]
    if sel is None:
        why = why + ["no day selection"]
    elif not isinstance(sj, dict) or sj.get("selection") != selection_id_of(sel):
        why = why + ["another selection"]
    row.update({"why": why, "stream": stats, "rewards": rewards_unit(paths["rewards.jsonl.gz"], sj, members)})
    return row, not why


def select_reading(d0, cache):
    """G-SELECT for a day: its first ok attempt re-derived from its stored replies alone, through the same rule."""
    ddir = os.path.join(ROOT, str(d0))
    sel = day_selection(d0, cache)
    res = {"day": d0, "ok": False, "why": [], "attempt": None, "failed_before": 0, "members": 0, "requests": None,
           "listing": None, "walked": None, "reasons": None}
    if not os.path.isdir(ddir):
        res["why"].append("no day directory")
        return res
    res["failed_before"] = sum(1 for n in os.listdir(ddir) if SELECT_FILE_RE.fullmatch(n)
                               and n.endswith(".json")) - (1 if sel else 0)
    if sel is None:
        res["why"].append("no ok selection")
        return res
    rec = sel["rec"]
    fetch = StoredFetch(select_paths(ddir, rec["attempt"])[1])
    try:
        again = run_rule(fetch, d0)
    except (SelectionError, AssertionError) as exc:
        res["why"].append("re-derivation: %s" % exc)
        return res
    for key in ("members", "walk", "reasons", "listing", "walked"):
        if again[key] != rec[key]:
            res["why"].append("%s differ" % key)
    if not fetch.exhausted():
        res["why"].append("replies left unread")
    if len(rec["members"]) != SET_SIZE:
        res["why"].append("members %d" % len(rec["members"]))
    res.update({"ok": not res["why"], "attempt": rec["attempt"], "members": len(rec["members"]),
                "requests": rec["replies"]["requests"], "listing": rec["listing"], "walked": rec["walked"],
                "reasons": rec["reasons"]})
    return res


def mode_prove(a):
    floor_check()
    starts = [r for r in read_runtime(ROOT + "/runtime.jsonl") if r.get("event") == "start"]
    assert starts, "prove: no start record"
    s = starts[0]["wall_ns"] / 1e9
    assert s <= a <= time.time(), "prove: as-of %d outside [%s, now]" % (a, s)
    out("the service's first start: pid %s at %s" % (starts[0]["pid"], utc(s)))
    plan, t = [], int(s) // SLOT * SLOT
    while t + SLOT_JSON_AT <= a:
        if considered(t, s, a):
            plan.append((t, qualifies(t, s, a) and sum(1 for _t, q in plan if q) < GATE_SLOTS))
        t += SLOT
    quals = [t for t, q in plan if q]
    decide = (len(quals) == GATE_SLOTS and a >= quals[-1] + SLOT_JSON_AT + NEIGHBOR_WAIT_S) or a >= s + BUDGET_S
    if not decide:
        nxt = int(a) + 300
        out("NOT YET: %d of %d qualifying slots closed as of %d; run again at or after %d (%s)" % (
            len(quals), GATE_SLOTS, a, nxt, utc(nxt)))
        return 3
    cache, rows, units, sched, served = {}, [], [], 0, 0
    for t, q in plan:
        row, unit = slot_row(t, q, cache)
        rows.append(row)
        if q:
            units.append(unit)
            sched += row["rewards"]["scheduled"]
            served += row["rewards"]["served"]
    days = sorted({day_of(t) for t in quals}) or [day_of(s)]
    g_select = [select_reading(d, cache) for d in days]
    g_stream = read_g_stream(units)
    g_rewards = read_g_rewards(len(quals), sched, served)
    sel_reading = "PASS" if g_select and all(x["ok"] for x in g_select) else "FAIL"
    nb = {"span": None, "rows": [], "reading": "UNDECIDABLE"}
    if len(quals) == GATE_SLOTS:
        lo, hi = -(-starts[0]["wall_ns"] // 10 ** 9), quals[-1] + CLOSE_AFTER
        nb["span"] = [lo, hi]
        archive_hold()
        nb["rows"] = neighbor_units(lo, hi, a)
        nb["reading"] = read_neighbors([(r["kind"], r["counted"], r["ok"]) for r in nb["rows"]])
    for x in g_select:
        out("G-SELECT day %d (%s): %s; attempt %s, %d failed before it, %s requests; members %d; listing %s; walked "
            "%s; verdicts %s" % (x["day"], utc(x["day"]), "re-derived equal" if x["ok"] else x["why"], x["attempt"],
                                 x["failed_before"], x["requests"], x["members"], json.dumps(x["listing"], sort_keys=True),
                                 x["walked"], json.dumps(x["reasons"], sort_keys=True)))
    for row in rows:
        out("slot %d %s qualifying %s: %s; indices %s; stream %s; polls %s" % (
            row["S"], utc(row["S"]), row["qualifying"], "complete" if not row["why"] else row["why"],
            json.dumps(row["indices"], sort_keys=True), json.dumps(row["stream"], sort_keys=True),
            json.dumps(row["rewards"], sort_keys=True)))
    for r in nb["rows"]:
        out("neighbour %s %d %s: counted %s, ok %s" % (r["kind"], r["unit"], utc(r["unit"]), r["counted"], r["ok"]))
    proof = {"mode": "prove", "as_of": a, "start": {"pid": starts[0]["pid"], "wall_ns": starts[0]["wall_ns"],
                                                    "commit": starts[0].get("commit"),
                                                    "file_sha256": starts[0].get("file_sha256")},
             "g_select": {"days": g_select, "reading": sel_reading}, "slots": rows,
             "g_stream": {"units": units, "reading": g_stream},
             "g_rewards": {"scheduled": sched, "served": served, "reading": g_rewards}, "neighbors": nb,
             "counters": {"requests": COUNTERS["requests"], "sessions": COUNTERS["sessions"]}}
    assert_keys(proof, PROOF_JSON_KEYS, "proof.json")
    forbid(proof, "proof.json")
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
    qs = [row for row in rows if row["qualifying"]]
    if qs:
        tot = sum(row["stream"].get("stored_bytes", 0) for row in qs)
        frames = sum(row["stream"].get("frames", 0) for row in qs)
        per_slot = Fraction(tot, len(qs))
        store = stream_bytes_total(ROOT)
        out("STREAM RATE, barred: %d qualifying slots, %d frames, %s a second over their streams' 910 s; %d stored "
            "bytes, %s a slot, %s a day of 96 slots; the store's streams now %d bytes, the cap %d in %s days at that "
            "rate" % (len(qs), frames, decimals(Fraction(frames, 910 * len(qs)), 1), tot, decimals(per_slot, 0),
                      decimals(per_slot * 96, 0), store, STREAM_CAP,
                      decimals(Fraction(max(STREAM_CAP - store, 0)) / (per_slot * 96), 2) if tot else "unread"))
    out("READING G-SELECT: %s, %d of %d days re-derived equal with %d members" % (
        sel_reading, sum(1 for x in g_select if x["ok"]), len(g_select), SET_SIZE))
    out("READING G-STREAM: %s, %d of %d complete" % (g_stream, sum(1 for u in units if u), len(units)))
    out("READING G-REWARDS: %s, %d of %d polls served" % (g_rewards, served, sched))
    out("READING G-NEIGHBORS: %s, %s" % (nb["reading"], ", ".join(
        "%s %d counted of %d, %d failing" % (kind, sum(1 for r in nb["rows"] if r["kind"] == kind and r["counted"]),
                                             sum(1 for r in nb["rows"] if r["kind"] == kind),
                                             sum(1 for r in nb["rows"] if r["kind"] == kind and r["counted"] and not r["ok"]))
        for kind in ("recorder", "pairbook"))))
    return 0


def mode_resume(a):
    """G-RESUME: the first slot opening at least RESUME_LEAD_S after the restarted process's start, complete."""
    floor_check()
    st = load_state()
    mark = st.get("marks", {}).get("kill-svc")
    assert mark is not None, "resume: no kill-svc mark"
    recs = read_runtime(ROOT + "/runtime.jsonl")
    after = [r for r in recs if r.get("event") == "start" and r.get("wall_ns", 0) >= mark["ns"]]
    assert after, "resume: no start after the kill mark"
    s2 = after[0]["wall_ns"] / 1e9
    s_ = -(-(int(s2) + RESUME_LEAD_S + OPEN_BEFORE) // SLOT) * SLOT
    assert a <= time.time(), "resume: as-of in the future"
    if a < s_ + SLOT_JSON_AT:
        out("NOT YET: slot %d (%s) closes at %d; run again at or after it" % (s_, utc(s_), s_ + SLOT_JSON_AT))
        return 3
    kill_slot = int(mark["ns"] // 10 ** 9) // SLOT * SLOT
    cache = {}
    krow, _ = slot_row(kill_slot, False, cache)
    row, unit = slot_row(s_, True, cache)
    out("the kill's slot %d %s: indices %s" % (kill_slot, utc(kill_slot), json.dumps(krow["indices"], sort_keys=True)))
    out("slot %d %s: %s; stream %s; polls %s" % (s_, utc(s_), "complete" if unit else row["why"],
                                               json.dumps(row["stream"], sort_keys=True),
                                               json.dumps(row["rewards"], sort_keys=True)))
    doc = {"mode": "resume", "as_of": a, "restart": {"pid": after[0]["pid"], "wall_ns": after[0]["wall_ns"],
                                                     "kill_slot": krow},
           "slot": row, "g_resume": "PASS" if unit else "FAIL"}
    assert_keys(doc, RESUME_JSON_KEYS, "resume.json")
    forbid(doc, "resume.json")
    os.makedirs(os.path.join(WORK, "resume"), exist_ok=True)
    path = os.path.join(WORK, "resume", "resume-%d.json" % a)
    body = json_line(doc)
    if os.path.exists(path):
        assert sha256_file(path) == sha256_bytes(body), "resume: %s differs from the first run" % path
        out("unchanged %s sha256 %s" % (path, sha256_bytes(body)))
    else:
        with open(path, "xb") as fh:
            fh.write(body)
        out("wrote %s sha256 %s, %d bytes" % (path, sha256_bytes(body), len(body)))
    out("READING G-RESUME: %s" % doc["g_resume"])
    return 0


async def prestart_session(path, tokens, seconds):
    stats = new_stream_stats()
    STOP_FLAG.clear()
    t0 = time.time()
    await stream_slot(path, tokens, t0, t0 + seconds, stats)
    return stats


def session_checks(path, tokens, stats):
    """P-START's seven checks on a session's file, from its lines alone."""
    rep = {"torn": False, "bad": 0}
    rows = list(stream_rows(path, rep))
    opens = [r for r in rows if isinstance(r, dict) and r.get("event") == "open"]
    subs = [r["recv_ns"] for r in rows if isinstance(r, dict) and r.get("event") == "subscribe"]
    early, bad, foreign = set(), 0, 0
    for r in rows:
        if not isinstance(r, dict) or "event" in r:
            continue
        if frozenset(r) != FRAME_KEYS or not isinstance(r.get("raw"), str):
            bad += 1
            continue
        if r["raw"] == "PONG":
            continue
        try:
            got = frame_tokens(json.loads(r["raw"]))
        except ValueError:
            got = None
        if got is None:
            bad += 1
            continue
        if not got[1] <= set(tokens):
            foreign += 1
        if "book" in got[0] and subs and r["recv_ns"] <= subs[0] + INITIAL_S * 10 ** 9:
            obj = json.loads(r["raw"])
            for it in (obj if isinstance(obj, list) else [obj]):
                if it.get("event_type") == "book":
                    early.add(it["asset_id"])
    return {"one session": stats["segments"] == 1 and COUNTERS["sessions"] == 1,
            "101": len(opens) == 1 and opens[0].get("status") == 101 and opens[0].get("extensions") is None,
            "subscribed": len(subs) == 1,
            "initial books": set(tokens) <= early,
            "heartbeat": stats["pongs"] >= 1 and stats["pings"] >= 2,
            "conforming": bad == 0 and foreign == 0,
            "whole file": not rep["torn"] and rep["bad"] == 0 and bool(rows) and rows[-1].get("event") == "end"}


def mode_prestart():
    """CANON hard rule 14's proof, through the service's own functions: one listing page, one gamma batch, two CLOB
    documents and two reward documents, one stream session of 25 s on the two markets' four tokens; the processes;
    the neighbours' base rates. Prints counts, statuses, verdicts and token ids only."""
    floor_check()
    with open(os.path.abspath(__file__), "rb") as fh:
        own = sha256_bytes(fh.read())
    out("file %s sha256 %s" % (os.path.abspath(__file__), own))
    proxies = sorted(k for k in os.environ if k.lower() in ("http_proxy", "https_proxy", "all_proxy"))
    out("free %d bytes at %s; proxy variables in the environment: %d" % (free_bytes(), DISK_PATH, len(proxies)))
    procs = {"service": processes_with(SERVICE_ARGV)}
    out("processes under the service's argv: %r" % procs["service"])
    assert procs["service"] == [], "prestart: an instance of the service already runs"
    archive_hold()
    p = int(time.time())
    rates = base_rates(p)
    for kind in ("recorder", "pairbook"):
        r = rates[kind]
        out("base rate %s: %d units, %d read, %d failing" % (kind, r["slots"], r["m"], r["f"]))
    fa = p_false_alarm_both(rates, NEIGHBOR_UNITS_MAX)
    out("G-NEIGHBORS' false failure at the base rates over %d intervals and %d windows: %s" % (
        NEIGHBOR_UNITS_MAX["recorder"], NEIGHBOR_UNITS_MAX["pairbook"], "unread" if fa is None else decimals(fa, 10)))
    lines = []
    fetch = LiveFetch(lines.append)
    page = loads_exact(fetch.listing(LISTING_FIRST))
    assert isinstance(page, dict) and isinstance(page.get("data"), list) and page["data"], "prestart: a listing page"
    rows, conflicts, unkeyed = listing_rows([compact_row(r) for r in page["data"]])
    ranked, _dropped = ranking(rows, conflicts, unkeyed)
    assert len(ranked) >= 2, "prestart: fewer than two ranked rows on the first page"
    cids = [cid for cid, _row in ranked[:2]]
    docs = docs_by_condition(loads_exact(fetch.gamma(cids)), cids)
    d0 = day_of(p)
    verdicts, tokens = [], []
    for cid in cids:
        raw = fetch.clob(cid)
        assert raw is not None, "prestart: no CLOB document for %s" % cid
        cdoc = loads_exact(raw)
        toks = cdoc.get("tokens") if isinstance(cdoc, dict) else None
        assert isinstance(toks, list) and len(toks) == 2, "prestart: %s carries no two tokens" % cid
        tokens += [toks[0]["token_id"], toks[1]["token_id"]]
        verdicts.append({"condition_id": cid, "gamma": gamma_verdict(docs.get(cid, []), d0) or "pass",
                         "clob": clob_verdict(cdoc, cid) or "pass"})
    polls = []
    for cid in cids:
        res = http_get(CLOB_REWARDS_URL.format(condition_id=cid), timeout=POLL_TIMEOUT_S)
        polls.append(res)
        assert poll_rows(res, cid) == 1, "prestart: the reward document of %s not served with its row: %s" % (
            cid, res["status"])
    assert COUNTERS["requests"] == 6, "prestart: %d requests" % COUNTERS["requests"]
    reqs = []
    for r in lines + [dict(x, kind="rewards", key=c, **{"try": 0}) for x, c in zip(polls, cids)]:
        try:
            json.loads(r["raw"])
            pj = True
        except ValueError:
            pj = False
        reqs.append({"kind": r["kind"], "url": r["url"], "headers": [["Accept", ACCEPT], ["User-Agent", UA]],
                     "status": r["status"], "bytes": r["bytes"], "sha256": r["sha256"], "parses_json": pj,
                     "elapsed_ns": None if r["recv_mono_ns"] is None else r["recv_mono_ns"] - r["send_mono_ns"]})
    for v in verdicts:
        out("market %s: gamma verdict %s, CLOB verdict %s" % (v["condition_id"], v["gamma"], v["clob"]))
    for r in reqs:
        out("request %s %s: status %s, %d bytes, sha256 %s, JSON %s, %s ns" % (r["kind"], r["url"], r["status"],
                                                                            r["bytes"], r["sha256"], r["parses_json"],
                                                                            r["elapsed_ns"]))
    for name in ("prestart", "prestart-2"):
        d = os.path.join(WORK, name)
        if not os.path.exists(d):
            break
    else:
        raise AssertionError("prestart: prestart and prestart-2 both exist")
    os.makedirs(d)
    path = os.path.join(d, "stream.jsonl.gz")
    stats = asyncio.run(prestart_session(path, tokens, 25))
    checks = session_checks(path, tokens, stats)
    for k, v in checks.items():
        out("P-START %-14s %s" % (k, v))
    out("the session: %d frames, %d frame bytes, %d pongs, %d pings, %d stored bytes, largest gap %s ns" % (
        stats["frames"], stats["frame_bytes"], stats["pongs"], stats["pings"], stats["stored_bytes"], stats["max_gap_ns"]))
    doc = {"mode": "prestart", "p_wall": p, "file_sha256": own, "processes": procs, "proxy_variables": len(proxies),
           "base_rates": rates, "requests": reqs, "walk": {"condition_ids": cids, "verdicts": verdicts},
           "stream": {"tokens": tokens, "stats": stats, "checks": checks},
           "counters": {"requests": COUNTERS["requests"], "sessions": COUNTERS["sessions"]}}
    assert_keys(doc, PRESTART_JSON_KEYS, "prestart.json")
    forbid(doc, "prestart.json")
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
    """Kept whatever a report prints: the state, the logs, the request-path proof, the proofs and the resume."""
    return tree == WORK and (rel == "state.json" or rel.startswith("logs/") or rel.startswith("prestart")
                             or rel.startswith("proof/") or rel.startswith("resume/"))


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

# ---- the self-test: literals, loopback servers and temporary trees under the work tree ----------------------------


class _Venue(http.server.BaseHTTPRequestHandler):
    """A venue on 127.0.0.1: the listing's pages by cursor, gamma batches by condition id, CLOB documents and reward
    documents by condition id, a 503 once for each path in fail_once, a 403 under /refused."""
    venue = {}
    seen = []

    def do_GET(self):
        _Venue.seen.append((self.requestline, sorted((k.lower(), v) for k, v in self.headers.items())))
        u = urllib.parse.urlsplit(self.path)
        q = urllib.parse.parse_qs(u.query)
        v = _Venue.venue
        code, body = 404, b'{"error":"not found"}'
        if self.path in v.get("fail_once", set()):
            v["fail_once"].discard(self.path)
            code, body = 503, b"busy"
        elif u.path == "/rewards/markets/current":
            c = q.get("next_cursor", [""])[0]
            if c in v.get("listing", {}):
                code, body = 200, v["listing"][c]
        elif u.path == "/markets" and "condition_ids" in q:
            docs = [d for cid in q["condition_ids"] for d in v.get("gamma", {}).get(cid, [])]
            code, body = 200, json.dumps(docs).encode()
        elif u.path.startswith("/markets/"):
            cid = u.path.split("/")[-1]
            if cid in v.get("clob", {}):
                code, body = 200, json.dumps(v["clob"][cid]).encode()
        elif u.path.startswith("/rewards/markets/"):
            cid = u.path.split("/")[-1]
            rows = [] if cid in v.get("unrewarded", ()) else [{"condition_id": cid, "market_competitiveness": 1.5}]
            code, body = 200, json.dumps({"data": rows, "next_cursor": "LTE=", "limit": 100,
                                          "count": len(rows)}).encode()
        elif u.path.startswith("/refused"):
            code, body = 403, b"error code: 1010\n"
        elif u.path == "/empty":
            code, body = 200, b"{}"
        self.send_response(code)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


def synth_book(tok, cond):
    return {"event_type": "book", "asset_id": tok, "market": cond, "timestamp": "1793000000000", "hash": "ab" * 20,
            "bids": [{"price": "0.48", "size": "10"}], "asks": [{"price": "0.52", "size": "10"}]}


def synth_change(toks, cond, ms):
    return {"event_type": "price_change", "market": cond, "timestamp": str(ms),
            "price_changes": [{"asset_id": t, "price": "0.5", "size": "1", "side": "BUY", "hash": "cd" * 20,
                               "best_bid": "0.49", "best_ask": "0.51"} for t in toks]}


async def loopback_ws(state, close_first_after=None):
    """A market channel on 127.0.0.1: the subscription read, every token's book sent as one list frame, a price
    change every 5 ms on the markets in turn; PONG to PING; the first connection closed by the venue after
    `close_first_after` seconds."""

    async def handler(ws):
        state["connections"] += 1
        k = state["connections"]
        state["headers"].append(sorted((n.lower(), v) for n, v in ws.request.headers.raw_items()))
        msg = await ws.recv()
        state["subs"].append(msg)
        toks = json.loads(msg)["assets_ids"]
        pairs = [toks[i:i + 2] for i in range(0, len(toks), 2)]
        await ws.send(json.dumps([synth_book(t, "0x%064x" % (i // 2)) for i, t in enumerate(toks)]))

        async def sender():
            n = 0
            while True:
                await asyncio.sleep(0.005)
                n += 1
                m = n % len(pairs)
                await ws.send(json.dumps(synth_change(pairs[m], "0x%064x" % m, 1793000000000 + n)))

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


def synth_venue(d0):
    """Thirteen listing rows on two pages, their gamma and CLOB documents: every verdict of section 1 once."""
    cid = {c: "0x" + h * 64 for c, h in zip("abcdefghjkmnp", "abcdef1234567")}
    end_ok, end_soon = "2027-01-01T04:59:00Z", utc(d0 + END_MIN_S - 1)

    def row(c, rate, ms=20, sp=4.5):
        return {"condition_id": cid[c], "rewards_config": [{"asset_address": "0x1", "start_date": "2026-10-27",
                                                            "end_date": "2500-12-31", "rate_per_day": rate,
                                                            "total_rewards": 0, "id": 0}],
                "rewards_max_spread": sp, "rewards_min_size": ms, "native_daily_rate": rate, "total_daily_rate": rate}

    page1 = [row("b", 100), row("a", 100), row("c", 50), row("d", 40), row("e", 30), row("a", 100)]
    page2 = [row("f", 20), row("g", 10.5), row("h", 0), row("j", 7), dict(row("j", 7), rewards_min_size=21),
             {"condition_id": None}, row("k", 5), row("m", 4), row("n", 3, sp=0), row("p", 2)]
    listing = {"MA==": json.dumps({"data": page1, "next_cursor": "Mg==", "limit": 6, "count": 6}).encode(),
               "Mg==": json.dumps({"data": page2, "next_cursor": "LTE=", "limit": 10, "count": 10}).encode()}

    def gdoc(c, end=end_ok, **kw):
        d = {"conditionId": cid[c], "endDate": end, "events": [{"id": "1", "startTime": None}]}
        d.update(kw)
        return d

    gamma = {cid["a"]: [gdoc("a")], cid["b"]: [gdoc("b")], cid["c"]: [gdoc("c", end_soon)], cid["d"]: [gdoc("d")],
             cid["e"]: [gdoc("e")], cid["f"]: [gdoc("f", events=[{"startTime": utc(d0 + 3600)}])],
             cid["g"]: [gdoc("g")], cid["k"]: [gdoc("k"), gdoc("k")], cid["m"]: [gdoc("m")],
             cid["p"]: [gdoc("p", gameStartTime="2026-11-01 12:00:00+00")]}

    def cdoc(c, i, **kw):
        d = {"condition_id": cid[c], "active": True, "closed": False, "archived": False, "accepting_orders": True,
             "enable_order_book": True, "tokens": [{"token_id": str(1000 + 2 * i), "outcome": "Yes"},
                                                   {"token_id": str(1001 + 2 * i), "outcome": "No"}],
             "game_start_time": None, "seconds_delay": 0, "tags": ["Politics"], "market_slug": "m-" + c,
             "neg_risk": False}
        d.update(kw)
        return d

    clob = {cid["a"]: cdoc("a", 0), cid["b"]: cdoc("b", 1), cid["d"]: cdoc("d", 3, tags=["Politics", " SPORTS "]),
            cid["g"]: cdoc("g", 6), cid["m"]: cdoc("m", 8, seconds_delay=1)}
    return cid, {"listing": listing, "gamma": gamma, "clob": clob}


def mode_selftest():
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    # the schedule, against integers computed outside this file
    ok(day_of(1793145600) == 1793145600 and day_of(1793232000 - 1) == 1793145600 and day_of(1793232000) == 1793232000,
       "day_of: 2026-10-28 00:00:00 UTC is 1793145600, the next day 1793232000")
    ok(first_slot(1793150000) == (1793149200, True) and first_slot(1793150080) == (1793149200, True)
       and first_slot(1793150081) == (1793150100, False) and first_slot(1793150097) == (1793150100, True),
       "first_slot: the current slot until S+880, then the next, late after its open at S-5")
    ok(selection_plan(1793150000, set()) == ([1793145600], 1793231100)
       and selection_plan(1793231100, {1793145600}) == ([1793232000], 1793317500)
       and selection_plan(1793231099, {1793145600}) == ([], 1793231100)
       and selection_plan(1793231200, {1793145600, 1793232000}) == ([], 1793317500),
       "selection_plan: today at once, tomorrow from 23:45:00 UTC, the next instant the plan changes")
    sch = slot_schedule(1793149200)
    ok(sch["open"] == 1793149195 and sch["close"] == 1793150105 and sch["json_at"] == 1793150110
       and sch["poll_last"] == 1793150100, "slot_schedule: the stream S-5 to S+905, the summary at S+910")
    pi = poll_instants(sch, 150)
    ok(len(pi) == 450 and pi[0] == (1793149230000, 0, 0) and pi[1] == (1793149231800, 0, 1)
       and pi[149] == (1793149498200, 0, 149) and pi[150] == (1793149530000, 1, 0) and pi[-1] == (1793150098200, 2, 149)
       and [x[0] for x in pi] == sorted(x[0] for x in pi),
       "poll_instants: 150 markets, three rounds 300 s apart, 1.8 s between polls, the last at S+898.2")
    ok(SLOT_FILE_RE.fullmatch("1793149200.0.stream.jsonl.gz") and SLOT_FILE_RE.fullmatch("1793149200.12.slot.json")
       and not SLOT_FILE_RE.fullmatch("1793149200.stream.jsonl.gz") and SELECT_FILE_RE.fullmatch("select.0.json")
       and SELECT_FILE_RE.fullmatch("select.3.replies.jsonl.gz"), "the store's file names")
    # the rule's pure parts
    d0 = 1793145600
    ok(iso_seconds("2026-11-12T00:00:00Z") == 1794441600 and iso_seconds("2026-12-01T04:59:59.999Z") == 1796101199.999
       and iso_seconds("2026-11-12T03:00:00+03:00") == 1794441600 and iso_seconds("2026-11-12T00:00:00") is None
       and iso_seconds("soon") is None and iso_seconds(None) is None and iso_seconds("") is None,
       "iso_seconds: a zone required, Z and offsets read, fractions kept")
    g = {"conditionId": "x", "endDate": "2026-11-12T00:00:00Z", "events": [{"startTime": None}]}
    ok(d0 + END_MIN_S == 1794441600 and gamma_verdict([g], d0) is None
       and gamma_verdict([dict(g, endDate="2026-11-11T23:59:59Z")], d0) == "ends within 14 days of the day's end",
       "gamma_verdict: an end at D0 + 15 days passes, a second earlier does not")
    ok(gamma_verdict([], d0) == "no gamma document" and gamma_verdict([g, g], d0) == "two gamma documents"
       and gamma_verdict([dict(g, endDate=None)], d0) == "end date unreadable"
       and gamma_verdict([dict(g, gameStartTime="2026-11-01 12:00:00+00")], d0) == "game start time"
       and gamma_verdict([dict(g, events="x")], d0) == "events unreadable"
       and gamma_verdict([dict(g, events=[{"startTime": "later"}])], d0) == "event start unreadable",
       "gamma_verdict: every other reason named")
    ok(gamma_verdict([dict(g, events=[{"startTime": utc(d0 - DAY)}])], d0) == "event start near the day"
       and gamma_verdict([dict(g, events=[{"startTime": utc(d0 - DAY - 1)}])], d0) is None
       and gamma_verdict([dict(g, events=[{"startTime": utc(d0 + 2 * DAY - 1)}])], d0) == "event start near the day"
       and gamma_verdict([dict(g, events=[{"startTime": utc(d0 + 2 * DAY)}])], d0) is None,
       "gamma_verdict: an event start in [D0 - 1 day, D0 + 2 days) excludes, either edge exact")
    ok(gamma_verdict([dict(g, events=[{"startTime": None, "endDate": utc(d0 + DAY - 1)}])], d0) == "event end near the day"
       and gamma_verdict([dict(g, events=[{"endDate": utc(d0 + 2 * DAY)}, {"endDate": "2027-01-01T00:00:00Z"}])], d0) is None
       and gamma_verdict([dict(g, events=[{"endDate": "2027-01-01T00:00:00Z"}, {"endDate": utc(d0)}])], d0)
       == "event end near the day" and gamma_verdict([dict(g, events=[{"endDate": "soon"}])], d0) == "event end unreadable",
       "gamma_verdict: so does an event end in the band, on any of the market's events")
    c = {"condition_id": "x", "active": True, "closed": False, "archived": False, "accepting_orders": True,
         "enable_order_book": True, "tokens": [{"token_id": "1"}, {"token_id": "2"}], "game_start_time": None,
         "seconds_delay": 0, "tags": ["Politics", "Elections"]}
    ok(clob_verdict(c, "x") is None and clob_verdict(dict(c, seconds_delay=None, tags=None), "x") is None,
       "clob_verdict: an open market of two tokens, no game, no delay, no excluded tag passes")
    ok(clob_verdict("unreadable", "x") == "CLOB document unreadable" and clob_verdict(c, "y") == "CLOB document of another market"
       and clob_verdict(dict(c, active=False), "x") == "active not true" and clob_verdict(dict(c, closed=True), "x") == "closed not false"
       and clob_verdict(dict(c, accepting_orders=None), "x") == "accepting_orders not true"
       and clob_verdict(dict(c, tokens=c["tokens"][:1]), "x") == "not two tokens"
       and clob_verdict(dict(c, tokens=[{"token_id": "1"}, {"token_id": "1"}]), "x") == "token ids"
       and clob_verdict(dict(c, tokens=[{"token_id": "1"}, {"token_id": "0x2"}]), "x") == "token ids"
       and clob_verdict(dict(c, game_start_time="2026-11-01"), "x") == "game start time"
       and clob_verdict(dict(c, seconds_delay=3), "x") == "seconds delay"
       and clob_verdict(dict(c, tags="Sports"), "x") == "tags unreadable",
       "clob_verdict: every other reason named")
    ok(clob_verdict(dict(c, tags=["Politics", " Crypto "]), "x") == "tag crypto"
       and clob_verdict(dict(c, tags=["Stocks", "Hit Price"]), "x") == "tag hit price"
       and clob_verdict(dict(c, tags=["Golden Joystick", "Games"]), "x") is None and len(EXCLUDED_TAGS) == 31,
       "clob_verdict: 31 excluded tags, matched whole after case and space are dropped")
    rows_, conf, unk = listing_rows([compact_row(x) for x in [{"condition_id": "a", "x": 1}, {"condition_id": "a", "x": 1},
                                                              {"condition_id": "b", "x": 1}, {"condition_id": "b", "x": 2},
                                                              {"condition_id": None}, "row"]])
    ok(sorted(rows_) == ["a", "b"] and conf == {"b"} and unk == 2,
       "listing_rows: identical rows once, differing rows a conflict, rows without a string id unkeyed")
    lr = {"condition_id": "0x" + "a" * 64, "total_daily_rate": Decimal("2"), "rewards_min_size": 20,
          "rewards_max_spread": Decimal("4.5")}
    ok(listing_verdict(lr) is None and listing_verdict(dict(lr, condition_id="0xA")) == "condition id"
       and listing_verdict(dict(lr, total_daily_rate=0)) == "total_daily_rate not positive"
       and listing_verdict(dict(lr, rewards_min_size=None)) == "no rewards_min_size"
       and listing_verdict(dict(lr, rewards_max_spread=True)) == "no rewards_max_spread",
       "listing_verdict: a valid id and three positive numbers")
    rk, dr = ranking({"0x" + "b" * 64: dict(lr, condition_id="0x" + "b" * 64),
                      "0x" + "a" * 64: lr, "0x" + "c" * 64: dict(lr, condition_id="0x" + "c" * 64,
                                                                total_daily_rate=Decimal("2.0000001")),
                      "0x" + "d" * 64: dict(lr, condition_id="0x" + "d" * 64, total_daily_rate=0)},
                     {"0x" + "e" * 64}, 1)
    ok([x[0][2] for x in rk] == ["c", "a", "b"] and dict(dr) == {"condition id": 1, "total_daily_rate not positive": 1},
       "ranking: by rate descending in exact decimals, ties by condition id ascending")
    # the walk, on literals: blocks, the CLOB request only after the gamma checks, the k-th member ends it
    calls = []
    rk2 = [("0x%064x" % i, {"total_daily_rate": 10 - i, "rewards_min_size": 20, "rewards_max_spread": 4.5})
           for i in range(7)]

    def fg(cids):
        calls.append(("gamma", len(cids)))
        return {c: [{"conditionId": c, "endDate": "2027-01-01T00:00:00Z" if int(c, 16) != 1 else "2026-11-01T00:00:00Z"}]
                for c in cids}

    def fc(cid):
        calls.append(("clob", int(cid, 16)))
        if int(cid, 16) == 2:
            return None
        return {"condition_id": cid, "active": True, "closed": False, "archived": False, "accepting_orders": True,
                "enable_order_book": True, "tokens": [{"token_id": "1"}, {"token_id": "2"}], "seconds_delay": 0,
                "tags": ["Sports"] if int(cid, 16) == 3 else []}

    mem, wrows, reas, cov = walk(rk2, d0, fg, fc, k=2, walk_max=6, batch=2)
    ok([m["rank"] for m in mem] == [0, 4] and [r[2] for r in wrows] == ["member", "ends within 14 days of the day's end",
                                                                       "no CLOB document", "tag sports", "member"]
       and calls == [("gamma", 2), ("clob", 0), ("gamma", 2), ("clob", 2), ("clob", 3), ("gamma", 2), ("clob", 4)]
       and cov == 6 and reas["member"] == 2,
       "walk: gamma by blocks of the batch, CLOB only after gamma passes, stopping at the k-th member")
    calls.clear()
    mem, wrows, reas, cov = walk(rk2, d0, fg, fc, k=9, walk_max=3, batch=2)
    ok(len(wrows) == 3 and cov == 3 and calls[-1] == ("clob", 2), "walk: never past walk_max")
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    try:
        # the request, on a loopback listener, with every proxy variable removed from this process
        removed = [k for k in list(os.environ) if k.lower() in ("http_proxy", "https_proxy", "all_proxy", "no_proxy")]
        for k in removed:
            del os.environ[k]
        out("  proxy variables removed: %d" % len(removed))
        req = build_request("http" + ":" + "//example.invalid/")
        ok(req.get_method() == "GET" and sorted((k.lower(), v) for k, v in req.header_items()) ==
           [("accept", "application/json"), ("user-agent", UA)], "build_request: GET, Accept and this file's User-Agent")
        cid, venue = synth_venue(d0)
        _Venue.venue = venue
        srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _Venue)
        th = threading.Thread(target=srv.serve_forever, daemon=True)
        th.start()
        port = srv.server_address[1]
        base = "http" + ":" + "//127.0.0.1:%d" % port
        before = COUNTERS["requests"]
        r = http_get(base + "/empty")
        line, hdrs = _Venue.seen[-1]
        ok(line.startswith("GET /empty ") and hdrs == sorted([
            ("accept", "application/json"), ("accept-encoding", "identity"), ("connection", "close"),
            ("host", "127.0.0.1:%d" % port), ("user-agent", UA)]), "the wire: exactly five header fields")
        ok(r["status"] == 200 and r["bytes"] == 2 and r["sha256"] == "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a"
           and r["recv_mono_ns"] >= r["send_mono_ns"] and r["send_wall_ns"] <= r["recv_wall_ns"],
           "http_get records 200, 2 bytes, the body's SHA-256 and its stamps")
        r = http_get(base + "/refused")
        ok(r["status"] == 403 and r["bytes"] == 17 and r["reason"] == "http_error" and r["recv_wall_ns"] is not None,
           "a refusal is a stored reply with its status")
        ok(COUNTERS["requests"] - before == 2, "two loopback requests counted")
        urls = {"listing": base + "/rewards/markets/current?next_cursor={cursor}", "gamma": base + "/markets?{query}",
                "clob": base + "/markets/{condition_id}", "rewards": base + "/rewards/markets/{condition_id}"}
        # the selection, end to end on the loopback venue: two pages, one gamma batch, a 503 once
        venue["fail_once"] = {"/markets/" + cid["b"]}
        sleeps = []
        root = os.path.join(tmp, "root")
        rec = attempt_day(d0, root, urls=urls, sleep=sleeps.append, k=3)
        ok(rec["ok"] and [m["condition_id"] for m in rec["members"]] == [cid["a"], cid["b"], cid["g"]]
           and [m["rank"] for m in rec["members"]] == [0, 1, 6] and rec["members"][2]["rate"] == "10.5"
           and rec["members"][0]["token_ids"] == ["1000", "1001"] and rec["members"][0]["outcomes"] == ["Yes", "No"],
           "the selection: the first three that pass, in rank order, a rate kept as its own text")
        ok([w[2] for w in rec["walk"]] == ["member", "member", "ends within 14 days of the day's end", "tag sports",
                                           "no CLOB document", "event start near the day", "member"]
           and rec["walked"] == 7 and rec["rule"]["covered"] == 10,
           "the walk disclosed in rank order, stopping at the third member")
        ok(rec["listing"] == {"pages": 2, "rows": 16, "distinct": 13, "conflicts": 1, "ranked": 10,
                              "dropped": {"condition id": 1, "conflicting rows": 1, "rewards_max_spread not positive": 1,
                                          "total_daily_rate not positive": 1}},
           "the listing: 16 rows, 13 ids, one conflict, one unkeyed, two not positive, 10 ranked")
        ok(rec["replies"]["requests"] == 9 and rec["replies"]["lines"] == 9 and sleeps.count(RETRY_S[0]) == 1
           and sleeps.count(REQUEST_GAP_S) == 8,
           "nine requests: two pages, one gamma batch, five CLOB documents and one retry after a 503")
        ddir = os.path.join(root, str(d0))
        sf = StoredFetch(select_paths(ddir, 0)[1])
        again = run_rule(sf, d0, k=3)
        ok(all(again[x] == rec[x] for x in ("members", "walk", "reasons", "listing", "walked")) and sf.exhausted()
           and sf.pos == 8, "the stored replies alone re-derive the same selection, every request read, each its last try")
        ok(load_selection(ddir)["attempt"] == 0 and next_attempt(ddir) == 1, "load_selection: the day's first ok attempt")
        bad = StoredFetch(select_paths(ddir, 0)[1])
        try:
            bad.gamma([cid["a"]])
            caught = False
        except AssertionError:
            caught = True
        ok(caught, "a stored reply answers only the request the attempt made, in its order")
        venue["listing"]["Mg=="] = b"oops"
        rec2 = attempt_day(d0, root, urls=urls, sleep=sleeps.append, k=3)
        ok(not rec2["ok"] and rec2["attempt"] == 1 and rec2["reason"] == "listing page Mg==: not JSON"
           and rec2["members"] is None and load_selection(ddir)["attempt"] == 0,
           "a failed attempt is written with its reason and leaves the day's first ok attempt in force")
        del venue["listing"]["Mg=="]
        rec3 = attempt_day(d0 + DAY, root, urls=urls, sleep=sleeps.append, k=3)
        ok(not rec3["ok"] and rec3["reason"] == "listing page Mg==: status 404" and len(rec3["walk"] or []) == 0
           and load_selection(os.path.join(root, str(d0 + DAY))) is None, "a 404 on a listing page fails the attempt")
        tries = []

        def flaky(url):
            tries.append(url)
            return {"url": url, "status": 500, "send_wall_ns": 1, "send_mono_ns": 1, "recv_mono_ns": 2, "recv_wall_ns": 2,
                    "bytes": 0, "sha256": sha256_bytes(b""), "raw": "", "reason": "http_error"}

        kept = []
        lf = LiveFetch(kept.append, urls=urls, getter=flaky, sleep=lambda s: None)
        try:
            lf.listing(LISTING_FIRST)
            caught = False
        except SelectionError:
            caught = True
        ok(caught and len(tries) == REQUEST_TRIES == 3 and len(kept) == 3 and [x["try"] for x in kept] == [0, 1, 2],
           "a 5xx is tried three times, every try kept, and then fails the attempt")
        # the polls and the slot, end to end: the loopback venue's reward documents and its market channel
        ok(poll_rows({"status": 200, "raw": json.dumps({"data": [{"condition_id": "x"}]})}, "x") == 1
           and poll_rows({"status": 200, "raw": json.dumps({"data": []})}, "x") == 0
           and poll_rows({"status": 200, "raw": json.dumps({"data": [{"condition_id": "y"}]})}, "x") is None
           and poll_rows({"status": 200, "raw": json.dumps({"data": [{"condition_id": "x"}] * 2})}, "x") is None
           and poll_rows({"status": 429, "raw": ""}, "x") is None and poll_rows({"status": 200, "raw": "x"}, "x") is None
           and poll_rows({"status": 200, "raw": json.dumps({"data": {}})}, "x") is None
           and poll_served({"status": 200, "raw": json.dumps({"data": []})}, "x"),
           "poll_rows: 200 and a page of at most one row, of the polled market; a page without its row is served")

        async def run_one(close_first_after, span, stop_after=None):
            state = {"connections": 0, "headers": [], "subs": [], "pings": 0}
            server = await loopback_ws(state, close_first_after)
            port_ = server.sockets[0].getsockname()[1]
            wsu = "ws" + ":" + "//127.0.0.1:%d/ws/market" % port_
            STOP_FLAG.clear()
            STOP_EVENT[0] = asyncio.Event()
            book = Book(root, urls=urls, k=3)
            book.free = lambda: STREAM_FLOOR
            book.load(d0)
            now = time.time()
            book.selections[day_of(now + 2)] = book.selections[d0]
            s_ = int(now) + 2
            sched = {"S": s_, "open": s_ - 1, "close": s_ + span, "json_at": s_ + span + 0.5, "poll_last": s_ + span,
                     "rounds_ms": [200, 1200], "span_ms": 600}
            if stop_after is not None:
                asyncio.get_running_loop().call_later(stop_after, request_stop)
            sj = await run_slot(book, sched, ws_url=wsu, kw=connect_kwargs(proxy=None), ping_s=0.3, backoff=(0.1,),
                                poll_url=urls["rewards"], join_last=s_ + span)
            server.close()
            await server.wait_closed()
            STOP_EVENT[0] = None
            return state, sj

        venue["unrewarded"] = {cid["g"]}
        state, sj = asyncio.run(run_one(0.8, 2.2))
        ddir_s = os.path.join(root, str(day_of(sj["S"])))
        paths = slot_paths(ddir_s, sj["S"], 0)
        ok(state["connections"] == 2 and sj["stream"]["segments"] == 2 and sj["index"] == 0 and sj["markets"] == 3
           and sj["tokens"] == 6, "a slot: a close by the venue, then one reconnect, three markets, six tokens")
        ok(all(x == subscription(["1000", "1001", "1002", "1003", "1012", "1013"]) for x in state["subs"])
           and state["subs"][0] == '{"assets_ids":["1000","1001","1002","1003","1012","1013"],"type":"market"}',
           "the subscription: the documented frame, compact, both tokens of every member in rank order")
        ok(sorted(k for k, _v in state["headers"][0]) == ["connection", "host", "sec-websocket-key", "sec-websocket-version",
                                                          "upgrade", "user-agent"] and dict(state["headers"][0])["user-agent"] == UA,
           "the handshake: six header fields, this file's User-Agent, no extension offered")
        ok(sj["stream"]["pings"] >= 4 and sj["stream"]["pongs"] >= 2 and state["pings"] >= sj["stream"]["pongs"],
           "the heartbeat: PING on its period, PONG stored")
        ok(sj["rewards"]["scheduled"] == 6 and sj["rewards"]["polled"] == 6 and sj["rewards"]["served"] == 6
           and sj["rewards"]["rows"] == 4 and sj["rewards"]["status_counts"] == {"200": 6}
           and sj["rewards"]["file"] == "%d.0.rewards.jsonl.gz" % sj["S"],
           "the polls: two rounds of three markets, every one served and stored, a market without its row twice")
        ok(sj["selection"] == {"day": d0, "attempt": 0, "sha256": sha256_file(select_paths(ddir, 0)[0])}
           and not sj["stopped"] and sj["error"] is None and os.path.isfile(paths["slot.json"]),
           "the summary names the day's selection by attempt and SHA-256")
        rep = {"torn": False, "bad": 0}
        rows = list(stream_rows(paths["stream.jsonl.gz"], rep))
        evs = [r["event"] for r in rows if "event" in r]
        ok(not rep["torn"] and rep["bad"] == 0 and evs[:3] == ["connect", "open", "subscribe"] and evs[-1] == "end"
           and evs.count("close") == 2 and evs.count("connect") == 2,
           "the stream file: connect, open, subscribe, frames, close, the same again, end")
        closes = [r for r in rows if r.get("event") == "close"]
        ok(closes[0]["reason"] == "closed" and closes[0]["code"] == 1011 and closes[1]["reason"] == "end",
           "the venue's close is recorded with its code, the slot's end as end")
        fr = [r for r in rows if "raw" in r]
        ok(len(fr) == sj["stream"]["frames"] and all(frozenset(r) == FRAME_KEYS for r in fr)
           and fr[0]["raw"].startswith('[{"event_type": "book"'),
           "every frame a line of recv_ns, mono_ns and the frame verbatim; the first the six books")
        why, sst = slot_unit(sj["S"], paths["stream.jsonl.gz"], sj, ["1000", "1001", "1002", "1003", "1012", "1013"])
        ok(sst["frames"] == sj["stream"]["frames"] and sst["nonconforming"] == 0 and sst["foreign"] == 0
           and sst["subscribes"] == 2 and "initial books" not in why and "count" not in why
           and sst["initial_tokens"] == 6 and dict(sst["types"])["book"] >= 6,
           "the unit reads the slot back: every frame conforms, every token's book, both sessions")
        ok(why == ["short"], "a slot of a few seconds reads short, and nothing else")
        nr = rewards_unit(paths["rewards.jsonl.gz"], sj, load_selection(ddir)["members"])
        ok(nr == {"scheduled": 6, "lines": 6, "served": 6, "rows": 4, "mismatched": 0, "unreadable": 0,
                  "statuses": {"200": 6}}, "rewards_unit reads the six polls back, each of the market its index names")
        ok(slot_index(ddir_s, sj["S"]) == 1, "a second process in the slot writes index 1")
        t1 = time.time()
        state, sj2 = asyncio.run(run_one(None, 30, stop_after=2.5))
        rep = {"torn": False, "bad": 0}
        rows = list(stream_rows(os.path.join(root, str(day_of(sj2["S"])), sj2["stream"]["file"]), rep))
        ok(time.time() - t1 < 8 and not rep["torn"] and rows[-1]["event"] == "end" and sj2["stopped"]
           and [r for r in rows if r.get("event") == "close"][0]["reason"] == "stop",
           "a stop closes the session at once, the file whole, the summary written stopped")
        STOP_FLAG.clear()
        halted = []
        for coro_of in (lambda b: run_slot(b, slot_schedule(1793149200)), lambda b: b.ensure(d0 + 2 * DAY)):
            book_f = Book(root, urls=urls, k=3)
            book_f.free = lambda: RESOURCE_FLOOR - 1
            asyncio.run(guarded(book_f, coro_of(book_f), "floor"))
            recs = read_runtime(os.path.join(root, "runtime.jsonl"))
            halted.append(len(book_f.halt) == 1 and "below the floor" in book_f.halt[0] and stopping()
                          and recs[-1]["event"] == "halt" and not os.path.isdir(os.path.join(root, str(d0 + 2 * DAY))))
            STOP_FLAG.clear()
        ok(halted == [True, True], "free space below 2,200,000,000 bytes at a slot or a selection halts the service")
        srv.shutdown()
        srv.server_close()
        # the writer: a sync flush makes a cut file readable to its last flush; the slot maximum cuts
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
            with open(p, "rb") as src:
                fh.write(src.read() + b"\x00")
        rep = {"torn": False, "bad": 0}
        ok(len(list(stream_rows(q, rep))) == 61 and rep["torn"], "bytes past the trailer read torn")
        w = StreamWriter(os.path.join(tmp, "cap.jsonl.gz"), slot_max=200, flush_s=0)
        w.frame("".join(sha256_bytes(b"%d" % i) for i in range(40)))
        ok(w.cut, "the slot maximum cuts the stream")
        w.close()
        w = StreamWriter(os.path.join(tmp, "bin.jsonl.gz"))
        w.frame(b"\x00\xff")
        w.close()
        rep = {"torn": False, "bad": 0}
        ok(list(stream_rows(os.path.join(tmp, "bin.jsonl.gz"), rep))[0]["raw_b64"] == "AP8=",
           "a binary frame is stored as base64, verbatim")
        ok(stream_off_reason(False, 3, 10 ** 10, 0) == "no selection" and stream_off_reason(True, 0, 10 ** 10, 0) == "empty set"
           and stream_off_reason(True, 3, STREAM_FLOOR - 1, 0) == "floor"
           and stream_off_reason(True, 3, STREAM_FLOOR, STREAM_CAP) == "cap"
           and stream_off_reason(True, 3, STREAM_FLOOR, STREAM_CAP - 1) is None,
           "the stream opens only with a selection of members, free at or above the floor, the store below the cap")
        sroot = os.path.join(tmp, "sroot")
        os.makedirs(os.path.join(sroot, "1793145600"))
        for name, size in (("1793149200.0.stream.jsonl.gz", 7), ("1793149200.1.stream.jsonl.gz", 5),
                           ("1793149200.0.rewards.jsonl.gz", 100), ("select.0.json", 50)):
            with open(os.path.join(sroot, "1793145600", name), "wb") as fh:
                fh.write(b"x" * size)
        ok(stream_bytes_total(sroot) == 12, "the cap counts the stream files alone, read again at every slot")
        # the unit, on synthetic slots: every reason it names
        s_ = 1793149200
        toks = ["11", "12", "13", "14"]
        ns = 10 ** 9

        def synth(name, sub_at, frames, end_at, close_ok=True, extra=None, declared=None, st_extra=None):
            d = os.path.join(tmp, name)
            os.makedirs(d)
            lines_ = [{"recv_ns": sub_at - 10 ** 6, "mono_ns": 1, "event": "connect", "seg": 0},
                      {"recv_ns": sub_at, "mono_ns": 2, "event": "subscribe", "seg": 0, "tokens": 4}]
            lines_ += frames
            if close_ok:
                lines_.append({"recv_ns": end_at, "mono_ns": 3, "event": "close", "seg": 0, "reason": "end", "code": None})
                lines_.append({"recv_ns": end_at + 1, "mono_ns": 4, "event": "end", "frames": len(frames)})
            body = "".join(json.dumps(x) + "\n" for x in lines_).encode()
            path = os.path.join(d, "s.jsonl.gz")
            with open(path, "wb") as fh:
                fh.write(gzip.compress(body, mtime=0))
            st = new_stream_stats()
            st.update({"opened": True, "file": "s.jsonl.gz", "frames": len(frames) if declared is None else declared})
            st.update(st_extra or {})
            sj_ = {"S": s_, "day": day_of(s_), "index": 0, "pid": 1, "task_wall_ns": 0, "joined_late": False,
                   "stopped": False, "selection": None, "markets": 2, "tokens": 4, "stream": st, "rewards": {},
                   "closed_wall_ns": 0, "error": None}
            sj_.update(extra or {})
            return slot_unit(s_, path, sj_, toks)

        books = [{"recv_ns": (s_ - 5) * ns + 10 ** 8, "mono_ns": 0, "raw": json.dumps([synth_book(x, "0xc") for x in toks])}]
        steady = [{"recv_ns": (s_ - 4 + k) * ns, "mono_ns": 0,
                   "raw": json.dumps(synth_change(toks[:2] if k % 2 else toks[2:], "0xc", (s_ - 4 + k) * 1000))}
                  for k in range(909)]
        why, sst = synth("good", (s_ - 5) * ns, books + steady, (s_ + 905) * ns)
        ok(why == [] and sst["frames"] == 910 and sst["max_gap_ns"] == ns and sst["lag_ms"]["median"] == 0
           and sst["subscribe_offset_ms"] == -5000 and sst["last_close_offset_ms"] == 905000,
           "a slot streamed from S-5 to S+905: complete, its largest gap 1 s")
        why, _s = synth("late", (s_ + 1) * ns, [dict(books[0], recv_ns=(s_ + 1) * ns + 1)] + steady[6:], (s_ + 905) * ns)
        ok(why == ["late subscribe"], "a subscribe after S reads late subscribe, and nothing else")
        why, _s = synth("nobook", (s_ - 5) * ns, steady, (s_ + 905) * ns)
        ok(why == ["initial books"], "no book of every token within 10 s of it reads initial books")
        holed = books + [x for x in steady if not ((s_ + 100) * ns <= x["recv_ns"] <= (s_ + 116) * ns)]
        why, _s = synth("gap", (s_ - 5) * ns, holed, (s_ + 905) * ns)
        ok(why == ["gap"], "18 s without a frame reads gap")
        why, _s = synth("torn", (s_ - 5) * ns, books + steady, (s_ + 905) * ns, close_ok=False)
        ok(why == ["no end line", "short"], "a file without its end line and its close reads so")
        why, _s = synth("early", (s_ - 5) * ns, books + steady[:890], (s_ + 890) * ns)
        ok(why == ["short"], "a stream whose last close is before S+900 reads short")
        odd = books + steady + [{"recv_ns": (s_ + 904) * ns + 1, "mono_ns": 0, "raw": '{"event_type": "new_market", "asset_id": "11"}'},
                                {"recv_ns": (s_ + 904) * ns + 2, "mono_ns": 0, "raw": json.dumps(synth_book("99", "0xd"))}]
        why, _s = synth("odd", (s_ - 5) * ns, odd, (s_ + 905) * ns, declared=len(odd) - 1)
        ok(why == ["nonconforming frames", "foreign tokens", "count"],
           "an undocumented event type, a token not subscribed and a count off its summary are named")
        why, _s = synth("joined", (s_ - 5) * ns, books + steady, (s_ + 905) * ns, extra={"joined_late": True, "error": "x"},
                        st_extra={"cut": True})
        ok(why == ["joined late", "error", "cut"], "a slot joined late, with an error, or cut is no unit")
        off = new_stream_stats()
        off["off_reason"] = "floor"
        ok(slot_unit(s_, os.path.join(tmp, "none"), {"S": s_, "day": 0, "index": 0, "pid": 1, "task_wall_ns": 0,
                                                     "joined_late": False, "stopped": False, "selection": None,
                                                     "markets": 0, "tokens": 0, "stream": off, "rewards": {},
                                                     "closed_wall_ns": 0, "error": None}, toks)[0] == ["no stream (floor)"]
           and slot_unit(s_, os.path.join(tmp, "none"), None, toks)[0] == ["slot json"],
           "a slot whose stream did not open names why; a missing summary reads so")
        ok(frame_tokens([synth_book("11", "0xc")]) == (["book"], {"11"}, None)
           and frame_tokens(synth_change(["11", "12"], "0xc", 5))[1:] == ({"11", "12"}, 5)
           and frame_tokens({"event_type": "tick_size_change", "asset_id": "11"}) == (["tick_size_change"], {"11"}, None)
           and frame_tokens({"event_type": "last_trade_price", "asset_id": "12"})[1] == {"12"}
           and frame_tokens([]) is None and frame_tokens({"event_type": "book"}) is None
           and frame_tokens({"event_type": "price_change", "price_changes": []}) is None and frame_tokens(7) is None,
           "frame_tokens: the four documented types and their token ids, nothing else")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    # the audit policy, as a pure function, and the hook itself
    man = RECORDER + "/btc-updown-5m/1793149200/manifest.json"
    win = PAIRBOOK + "/1793149200/window.json"
    ok(policy("serve", "open", (ROOT + "/1793145600/1793149200.0.stream.jsonl.gz", "xb", 0)) is None
       and policy("serve", "open", (WORK + "/x", "wb", 0)) is not None and policy("serve", "open", ("/tmp/x", "wb", 0)) is not None,
       "serve writes under the reward book's root and nowhere else")
    ok(policy("serve", "subprocess.Popen", ("systemctl",)) is not None and policy("serve", "os.fork", ()) is not None
       and policy("unit", "subprocess.Popen", ("systemctl",)) is None, "serve starts no process; the systemd reads may")
    ok(policy("prove", "open", (man, "rb", 0)) is None and policy("prestart", "open", (man, "rb", 0)) is None
       and policy("prove", "open", (man.replace("manifest.json", "quotes.jsonl.gz"), "rb", 0)) is not None
       and policy("prove", "open", (RECORDER + "/runtime.jsonl", "rb", 0)) is not None
       and policy("serve", "open", (man, "rb", 0)) is not None and policy("prove", "open", (man, "r+b", 0)) is not None,
       "under the recorder's root only a manifest, read only, by prestart and prove")
    ok(policy("prove", "open", (win, "rb", 0)) is None and policy("prestart", "open", (win, "rb", 0)) is None
       and policy("prove", "open", (win.replace("window.json", "stream.jsonl.gz"), "rb", 0)) is not None
       and policy("prove", "open", (PAIRBOOK + "/runtime.jsonl", "rb", 0)) is not None
       and policy("serve", "open", (win, "rb", 0)) is not None,
       "under the pair book's root only a window's window.json, read only, by prestart and prove")
    ok(policy("still", "open", (ARCHIVE_LEDGER, "rb", 0)) is None and policy("final", "open", (ARCHIVE_LEDGER, "rb", 0)) is None
       and policy("prove", "open", (ARCHIVE_LEDGER, "rb", 0)) is not None
       and policy("still", "open", (ARCHIVE_STATE + "/runs/1/set.json", "rb", 0)) is not None
       and policy("still", "open", (CHAINBOOK + "/runtime.jsonl", "rb", 0)) is not None,
       "the archive's ledger read by still and final alone; nothing of the chain book")
    ok(all(policy(m, ev, (r,)) is not None for m in ("prove", "prestart", "still") for ev in ("os.listdir", "os.scandir")
           for r in (RECORDER + "/btc-updown-5m", PAIRBOOK, ARCHIVE_STATE, CHAINBOOK)),
       "no neighbour's root is ever listed")
    ok(policy("prove", "open", (ROOT + "/runtime.jsonl", "rb", 0)) is None
       and policy("prove", "open", (ROOT + "/runtime.jsonl", "wb", 0)) is not None
       and policy("prestart", "open", (ROOT + "/runtime.jsonl", "rb", 0)) is not None
       and policy("prove", "os.scandir", (ROOT,)) is None and policy("unit", "os.scandir", (ROOT,)) is not None,
       "the reward book's root is written by serve alone, read and listed by the modes that judge it")
    ok(policy("reclaim", "open", (FORENSICS + "/x", "xb", 0)) is None
       and policy("reclaim", "open", (FORENSICS + "/x", "wb", 0)) is not None,
       "the forensic store takes new files by exclusive create alone")
    MODE[0] = "selftest"
    for p in (RECORDER + "/runtime.jsonl", PAIRBOOK + "/runtime.jsonl", ARCHIVE_LEDGER, ROOT + "/runtime.jsonl"):
        try:
            open(p, "rb")
            refused = False
        except GuardError:
            refused = True
        except OSError:
            refused = False
        ok(refused and REFUSED[-1][1] == p, "the hook refuses %s before it is opened" % p)
    REFUSED.clear()
    # the readings and their error rates, against fractions computed outside this file
    ok([read_g_stream(u) for u in ([True] * 4, [True, True, True, False], [True, True, False, False], [True] * 3)]
       == ["PASS", "PASS", "FAIL", "UNDECIDABLE"], "G-STREAM: 4 and 3 of 4, 2 of 4, fewer than 4")
    ok([read_g_rewards(4, 1800, 1782), read_g_rewards(4, 1800, 1781), read_g_rewards(3, 1800, 1800),
        read_g_rewards(4, 0, 0)] == ["PASS", "FAIL", "UNDECIDABLE", "UNDECIDABLE"],
       "G-REWARDS: 1,782 of 1,800 served is 99 in 100, 1,781 is not")
    ok([read_neighbors(r) for r in ([("recorder", True, True)] * 8 + [("pairbook", True, True)] * 3,
                                    [("recorder", True, True)] * 8 + [("pairbook", True, True)] * 2,
                                    [("recorder", True, False)], [("recorder", False, False)] * 20)]
       == ["HOLD", "UNDECIDABLE", "BROKEN", "UNDECIDABLE"], "G-NEIGHBORS: a counted failure breaks it; HOLD needs 8 and 3")
    ok(recorder_units(1793149195, 1793152805) == list(range(1793149200, 1793152500 + 1, 300))
       and pairbook_units(1793149195, 1793152805) == [1793149200, 1793150100, 1793151000, 1793151900],
       "the neighbours' units inside a span: 12 intervals and 4 windows over four slots")
    ok(p_fail_at_least(4, 2, Fraction(1, 100)) == Fraction(59203, 100000000)
       and p_fail_at_least(4, 2, Fraction(1, 4)) == Fraction(67, 256) and p_fail_at_least(4, 2, Fraction(1, 2)) == Fraction(11, 16),
       "G-STREAM's false failure at 1 in 100 and its power at 1 in 4 and 1 in 2")
    ok(1800 - 1782 + 1 == 19 and decimals(p_fail_at_least(1800, 19, Fraction(1, 200)), 10) == "0.0023617556"
       and decimals(p_fail_at_least(1800, 19, Fraction(1, 100)), 10) == "0.4377542261"
       and decimals(p_fail_at_least(1800, 19, Fraction(1, 50)), 10) == "0.9993511588",
       "G-REWARDS' false failure at 1 poll in 200 and its power at 1 in 100 and 1 in 50")
    ok(p_fail_at_least(11, 1, Fraction(1, 4)) == Fraction(4017157, 4194304)
       and p_fail_at_least(11, 1, Fraction(1, 2)) == Fraction(2047, 2048),
       "G-NEIGHBORS' power at its least count, 11 units, at 1 in 4 and 1 in 2")
    ok(p_false_alarm(0, 2016, 12) == 0 and p_false_alarm(1, 2016, 12) == 1 - Fraction(2015, 2016) ** 12
       and p_false_alarm(0, 0, 4) is None, "the neighbours' false alarm, exact")
    ok(p_false_alarm_both({"recorder": {"m": 2016, "f": 0}, "pairbook": {"m": 672, "f": 3}}, NEIGHBOR_UNITS_MAX)
       == 1 - Fraction(669, 672) ** 5 and NEIGHBOR_UNITS_MAX == {"recorder": 16, "pairbook": 5}
       and p_false_alarm_both({"recorder": {"m": 0, "f": 0}, "pairbook": {"m": 672, "f": 3}}, NEIGHBOR_UNITS_MAX) is None,
       "G-NEIGHBORS' false failure at both base rates over 16 intervals and 5 windows")
    clk = [0.0]
    seq = ["activating", "activating", "inactive"]
    st_, waited = archive_hold(state_of=lambda: seq.pop(0), clock=lambda: clk[0],
                               sleep=lambda x: clk.__setitem__(0, clk[0] + x))
    ok(st_ == "inactive" and waited == 2 * HOLD_STEP_S and archive_hold(state_of=lambda: "failed")[0] == "failed",
       "the archive's hold: every 10 s until its service is not running")
    clk = [0.0]
    try:
        archive_hold(state_of=lambda: "active", clock=lambda: clk[0], sleep=lambda x: clk.__setitem__(0, clk[0] + x))
        caught = False
    except AssertionError as exc:
        caught = "BLOCKED" in str(exc) and clk[0] == HOLD_MAX_S + HOLD_STEP_S
    ok(caught, "the archive's hold stops BLOCKED past 7,200 s")
    ok(decimals(Fraction(1, 3), 4) == "0.3333" and decimals(Fraction(2, 3), 4) == "0.6667"
       and decimals(Fraction(9804887, 2), 0) == "4902444" and decimals(Fraction(7, 1000), 2) == "0.01",
       "decimals: half up, whole numbers included")
    b = {"recorder": {"MainPID": "10", "NRestarts": "2", "ActiveState": "active"},
         "pairbook": {"MainPID": "20", "NRestarts": "3", "ActiveState": "active"}}
    nb = {"recorder": b["recorder"], "pairbook": {"MainPID": "22", "NRestarts": "5", "ActiveState": "active"}}
    chain = [{"stopped": "20", "NRestarts": 4, "pid": 21}, {"stopped": "21", "NRestarts": 5, "pid": 22}]
    ok(still_reading(b, b, []) == (True, "unchanged") and still_reading(b, nb, chain)[0]
       and not still_reading(b, nb, chain[:1])[0] and not still_reading(b, dict(nb, recorder={"MainPID": "11"}), chain)[0],
       "G-STILL: unchanged, or the pair book moved by the archive's chain of restarts alone")
    good = ("\x00".join(SERVICE_ARGV) + "\x00").encode()
    ok(same_service(good, SERVICE_ARGV) and not same_service(("bash\x00-c\x00" + " ".join(SERVICE_ARGV) + "\x00").encode(),
                                                            SERVICE_ARGV)
       and not same_service(good + b"--x\x00", SERVICE_ARGV), "same_service: the exact argv, never a substring")
    ok(not (SELECT_KEYS | SLOT_JSON_KEYS | STREAM_KEYS | REWARDS_JSON_KEYS | PROOF_JSON_KEYS | PRESTART_JSON_KEYS
            | RESUME_JSON_KEYS) & FORBIDDEN_KEYS and "rate" in MEMBER_KEYS and "rate" in FORBIDDEN_KEYS,
       "no summary's key is forbidden; a member's rate stays in the store")
    try:
        forbid({"x": [{"y": {"market_competitiveness": 1}}]}, "t")
        caught = False
    except AssertionError:
        caught = True
    ok(caught, "a forbidden key at any depth fails the output's check")
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
    urls_ = sorted({c.value for c in ast.walk(tree) if isinstance(c, ast.Constant) and isinstance(c.value, str)
                    and sep in c.value})
    ok(urls_ == sorted(URLS.values()), "exactly five endpoints in the file's text")
    ok(websockets.__version__ == "17.1", "websockets 17.1, the recorder's")
    ok(MALLOC_TUNED, "glibc took the mmap threshold of 128 KiB and two arenas")
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz33-reward-book-capture.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    MODE[0] = mode
    rc = 0
    if mode == "serve":
        assert not rest, "serve takes no argument"
        rc = mode_serve()
    elif mode in ("prove", "resume"):
        assert len(rest) == 1 and rest[0].isdigit(), "%s A" % mode
        rc = (mode_prove if mode == "prove" else mode_resume)(int(rest[0]))
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
                 "restart": mode_restart, "final": mode_final, "prestart": mode_prestart, "load": mode_load,
                 "stopped": mode_stopped}
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    if mode != "serve":
        out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
        out("opens refused: %d; manifest opens %d; window opens %d; ledger opens %d; requests %d, stream sessions %d" % (
            len(REFUSED), OPENS["manifest.json"], OPENS["window.json"], OPENS["ledger.jsonl"], COUNTERS["requests"],
            COUNTERS["sessions"]))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
