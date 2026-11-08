#!/usr/bin/env python3
"""TZ-41 - L0, our quote on the venue's reward markets: does a two-sided quote of ours, each side one tick inside the
touch and alone at its price, simulated on the reward book's streams, collect more in liquidity rewards and maker
rebates than its fills lose?

    fingerprint       contract section 1 steps 3 and 4, asserted: the map's revision, anchors and rows
    number            CANON hard rule 2: no other TZ-41 specification or report on origin/main
    selftest          every rule of this file, on literals, on synthetic streams and on temporary trees
    still             the five units' MainPID, NRestarts and ActiveState: the first run records them, the second
                      compares, the pair book archive's own restarts read from its ledger (G-STILL)
    scratch OWN       the UUID directories beside OWN, this session's, each named live or earlier
    archive           the reward book archive's ledger and the set.json of every complete run, read and printed
    rehearse          the replay over four of the archive's first assets under fixed parameters, every unit held,
                      against the Architect's independent replay (G-REHEARSAL)
    fetch             the candidate days from 2026-10-31, once the archive has moved them: each day's selection,
                      slot records, polls and fee schedules, the members' documents, and the set (G-SET)
    replay            every member day's slots downloaded, replayed and removed, every unit held; the days' money
                      on disk (G-BOOK)
    rescore           the set's first day replayed again, from a second download (DETERMINISM)
    score             L0's reading from the replay's day files
    reclaim TREE...   section 9

Its own code is the whole of L0's arithmetic - the replay of a day's streams, every member market's book rebuilt, our
quote placed, queued, filled and cancelled at venue time, its reward share by the venue's published formula, its
rebate and its fills marked to the market - and the reward book's record, the downloads held to the pair book's idle
stretch and G-STILL. Its requests: gamma-api.polymarket.com, the members' documents, in fetch alone; downloads of
Release assets from github.com; and git against origin. An audit hook refuses every open, listing, request and process
TZ-41 section 2 does not give the running mode. It writes under /root/tz41-work/ and, in reclaim, new files in
/root/btc-forensics/ by exclusive create. Exit 0: every assert of the mode held. Exit 1: an assert failed, and its
message names it. Run it with the recorder's interpreter, /root/tz04a-env.

Written for CryptoTZ/TZ-41-l0-our-quote.md. The TZ is the specification.
"""

import bisect
import collections
import ctypes
import datetime
import decimal
import gzip
import hashlib
import heapq
import http.client
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
from decimal import Decimal as D
from fractions import Fraction as Fr

if not __debug__:
    sys.stderr.write("tz41: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)


def _malloc_tune():
    """glibc's mmap threshold at 128 KiB and two arenas, as TZ-23's and TZ-33's instruments fix them."""
    try:
        libc = ctypes.CDLL("libc.so.6")
        return libc.mallopt(-3, 131072) == 1 and libc.mallopt(-8, 2) == 1
    except OSError:
        return False


MALLOC_TUNED = _malloc_tune()
HERE = os.path.dirname(os.path.abspath(__file__))

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------------

MAP_REVISION = "2026-11-01-b"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 57, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"(?:`([0-9a-f]{64})`|[^|]*) \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)
NUMBER = "TZ-41-"

DAY = 86400
SLOT = 900
SLOTS_A_DAY = 96
FIRST_D0 = 1793404800        # 2026-10-31 00:00:00 UTC: the first candidate day, after every read of the exploration
NEED = 8                     # member days: the reading's eight blocks
NONMEMBER_MAX = 6            # the walk is BLOCKED past six non-member days before the eighth member
LAST_D0 = FIRST_D0 + (NEED + NONMEMBER_MAX - 1) * DAY    # 1794528000, 2026-11-13: the fourteenth candidate
GAP_MAX_NS = 15 * 10 ** 9    # no gap between received frames of a slot above 15 s
WAIT_MAX_S = 10800           # fetch waits at most three hours for the archive to reach a candidate day

# The quoting rule (TZ-41 section 1): one tick inside each side of the touch, where the touch is five ticks wide or
# more; the reward band; the position cap in minimum-size clips; the one-way latency.
LATENCY_MS = 50
CAP_CLIPS = 1
SPREAD_TICKS = 5
# (name, rule, first in its level's queue, a crossing order a taker, the competitors' score): the first two are
# gated - pess, every assumption against us, for EARN; opt, every assumption for us, for NO EARN - central barred.
VARIANTS = (("pess", "alone", False, True, "pess"), ("opt", "alone", True, False, "opt"),
            ("central", "alone", False, True, "venue"))
GATED = ("pess", "opt")
THETA = D("10")              # USDC a day: EARN where every pess day reaches it, NO EARN where no opt day does
BOOK_EQUAL_MIN = Fr(99, 100) # G-BOOK: the rebuilt touch equals the venue's own at 99 in 100 of its book frames
REPLAY_CPU_MAX = 3000        # processor seconds the set's replay may take, projected after its first 24 units
RESCORE_CPU_MAX = 300
REHEARSAL_CPU_MAX = 120
PROJECT_AFTER = 24
UNIT_BUDGET_S = 45           # a unit's budget beside its download: replay and deletion
DL_RATE = 2000000            # bytes a second a download is budgeted at, TZ-28's
DL_TRIES = 6
DOC_BUDGET_S = 120           # a document request's budget in the idle stretch
STORE_BUDGET_S = 60          # a candidate day's read of the store's files, its selection, slots and polls
DOC_CHUNK = 50               # condition ids a gamma request carries: TZ-33's batch
IDLE = (15, 590)             # the pair book's idle stretch: a unit starts at second 15 or later, ends by 590
CALENDAR = ((5420, "the reward book archive's calendar run at 01:30:20 UTC"),
            (10820, "the pair book archive's calendar run at 03:00:20 UTC"))
CALENDAR_LEAD_S = 60
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")
HOLD_MAX_S = 7200
MEM_FLOOR = 143592894        # MemAvailable: twice the largest peak of any mode the Architect measured, modelled at
#                              the host's ratio TZ-37 measured, 58,953,728 / 49,168,384 (section 0.4)
MEM_RETRY_S = 60             # a MemAvailable read below the floor is read again this much later,
MEM_READS = 5                # five reads at most
DISK_FLOOR = 7400000000      # free bytes on /dev/vda2 once a unit's download lands: the reward book's STREAM_FLOOR,
#                              7,300,000,000, and one slot of its streams at the cut, 100,000,000 (section 0.4)
DISK_GATE = 7800000000       # free bytes at a mode's start: DISK_FLOOR and this session's tree twice over (section 0.4)

UA = "btc-5m-twap-tz41"
DL_HEADERS = {"User-Agent": UA, "Accept": "application/octet-stream"}
GAMMA_HEADERS = {"User-Agent": UA, "Accept": "application/json"}
REPO = "seahomebatumi-ai/btc-5m-twap"
DL_URL = "https://github.com/" + REPO + "/releases/download/%s/%s"
DL_HOSTS = ("github.com", "release-assets.githubusercontent.com", "objects.githubusercontent.com")
GAMMA_HOST = "gamma-api.polymarket.com"
GAMMA_URL = "https://gamma-api.polymarket.com/markets?%s"
ASSET_RE = re.compile(r"([0-9]{10})-(([0-9]{10})\.([0-9]+)\.stream\.jsonl\.gz)")
SLOT_FILE_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.(stream\.jsonl\.gz|rewards\.jsonl\.gz|slot\.json)")
SELECT_FILE_RE = re.compile(r"select\.([0-9]+)\.(json|replies\.jsonl\.gz)")
CID_RE = re.compile(r"0x[0-9a-f]{64}")
TOKEN_RE = re.compile(r"[0-9]{1,100}")
SHA_RE = re.compile(r"[0-9a-f]{64}")

# G-REHEARSAL: four of the reward book archive's first Release's assets, their bytes and SHA-256 as TZ-34's report
# printed them, replayed as one stand-in hour under fixed parameters (TZ-41 section 4.1)
REHEARSAL_TAG = "rewardbook-streams-1793263627"
REHEARSAL_D0 = 1793232000
REHEARSAL_ASSETS = (
    ("1793232000-1793232000.0.stream.jsonl.gz", 11579610, "bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f"),
    ("1793232000-1793232900.0.stream.jsonl.gz", 10715152, "46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370"),
    ("1793232000-1793233800.0.stream.jsonl.gz", 11443056, "2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9"),
    ("1793232000-1793234700.0.stream.jsonl.gz", 13592154, "ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496"))
REHEARSAL_PARAMS = {"ms": 5000, "vu": 90, "rate": Fr(100), "fee": Fr(0)}   # 50 shares, 4.5 cents, 100 a day, no fee
REF = {"lines": 451, "digest": "1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd"}

WORK = "/root/tz41-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/read-ledger.jsonl"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
BRANCH = "tz-41-l0-our-quote"
RB_ROOT = "/var/lib/btc-rewardbook"
RB_ARCHIVE = "/var/lib/btc-rewardbook-archive"
RB_LEDGER = RB_ARCHIVE + "/ledger.jsonl"
PB_ARCHIVE = "/var/lib/btc-pairbook-archive"
PB_LEDGER = PB_ARCHIVE + "/ledger.jsonl"
RECORDER = "/var/lib/btc-recorder"
PAIRBOOK = "/var/lib/btc-pairbook"
CHAINBOOK = "/var/lib/btc-chainbook"
ADVISOR = "/var/lib/adv3-bot"
ADVISOR_ETC = "/etc/adv3-bot"
UNITS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service", "rewardbook": "btc-rewardbook.service",
         "advisor": "adv3-bot.service"}
ARCHIVES = {"pairbook": ("btc-pairbook-archive.service", "btc-pairbook-archive.timer"),
            "rewardbook": ("btc-rewardbook-archive.service", "btc-rewardbook-archive.timer")}
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
LIVE_S = 60
PYFILE = "tz41-l0-our-quote.py"

# ---- the audit hook: TZ-41 section 2's reads, writes, requests and processes -----------------------------

MODE = [None]
REFUSED = []
COUNTS = collections.Counter()
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
RB_SET = re.compile(re.escape(RB_ARCHIVE) + r"/runs/([0-9]{10})/set\.json")
RB_DAY = re.compile(re.escape(RB_ROOT) + r"/([0-9]{10})")
RB_FILE = re.compile(re.escape(RB_ROOT) + r"/([0-9]{10})/([0-9]{10}\.[0-9]+\.(?:slot\.json|rewards\.jsonl\.gz)|"
                     r"select\.[0-9]+\.(?:json|replies\.jsonl\.gz))")
PROCESSES = {"git", "systemctl", "stat"}
SELFTEST_HOSTS = ("127.0.0.1",)


class GuardError(RuntimeError):
    pass


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


def _path(p):
    if isinstance(p, bytes):
        p = os.fsdecode(p)
    return os.path.abspath(p) if isinstance(p, str) else None


def day_in_span(d0):
    return FIRST_D0 <= d0 <= LAST_D0 and (d0 - FIRST_D0) % DAY == 0


def policy(mode, event, args):
    """None where TZ-41 section 2 allows the event in this mode; otherwise the reason it is refused."""
    if event == "urllib.Request":
        host = urllib.parse.urlsplit(args[0]).hostname if args and isinstance(args[0], str) else None
        if mode in ("rehearse", "replay", "rescore") and host in DL_HOSTS:
            return None
        if mode == "fetch" and host == GAMMA_HOST:
            return None
        if mode == "selftest" and host in SELFTEST_HOSTS:
            return None
        return "a request to %s" % host
    if event == "subprocess.Popen":
        exe = args[0] if args and args[0] else (args[1][0] if len(args) > 1 and args[1] else "")
        exe = os.path.basename(os.fsdecode(exe) if isinstance(exe, bytes) else str(exe))
        return None if exe in PROCESSES else "a process %s" % exe
    p = _path(args[0]) if args else None
    if p is None:
        return None
    if event in ("os.listdir", "os.scandir"):
        if any(_under(p, r) for r in (RECORDER, CHAINBOOK, PAIRBOOK, PB_ARCHIVE, RB_ARCHIVE, ADVISOR, ADVISOR_ETC)):
            return "a listing under a capture root or an archive's state"
        if _under(p, RB_ROOT):
            m = RB_DAY.fullmatch(p)
            if mode == "fetch" and m is not None and day_in_span(int(m.group(1))):
                return None
            return "a listing under the reward book's root"
        return None
    wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
    w = _writing(wm, fl)
    if any(_under(p, r) for r in (RECORDER, CHAINBOOK, PAIRBOOK, ADVISOR, ADVISOR_ETC)):
        return "an open under a capture root or the advisor's"
    if _under(p, RB_ROOT):
        m = RB_FILE.fullmatch(p)
        if not w and mode == "fetch" and m is not None and day_in_span(int(m.group(1))):
            return None
        return "an open under the reward book's root"
    if _under(p, RB_ARCHIVE):
        if not w and mode in ("archive", "fetch", "still") and (p == RB_LEDGER or RB_SET.fullmatch(p)):
            return None
        return "an open under the reward book archive's state"
    if _under(p, PB_ARCHIVE):
        if not w and mode == "still" and p == PB_LEDGER:
            return None
        return "an open under the pair book archive's state"
    if _under(p, FORENSICS):
        if w:
            return None if mode == "reclaim" and _exclusive(wm, fl) else "a write into the forensic store"
        return None
    if w and not _under(p, WORK):
        return "a write outside the work tree"
    return None


def _audit(event, args):
    if event not in ("open", "os.listdir", "os.scandir", "urllib.Request", "subprocess.Popen"):
        return
    why = policy(MODE[0], event, args)
    if why is None and event == "open" and _under(_path(args[0]) or "", RB_ROOT):
        COUNTS["reward book opens"] += 1
    if why is not None:
        REFUSED.append((event, str(args[0]) if args else ""))
        raise GuardError("%s refused in mode %s, %s: %r" % (event, MODE[0], why, args[0] if args else None))


sys.addaudithook(_audit)

# ---- small helpers ----------------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return datetime.datetime.fromtimestamp(float(t), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


C50 = decimal.Context(prec=50)        # every reward term and sum at 50 significant digits
Q12 = D("0.000000000001")


def q12(x):
    """A figure for print, half-even to 12 places; every sum and comparison is made on the exact figure."""
    if isinstance(x, Fr):
        x = C50.divide(D(x.numerator), D(x.denominator))
    s = format(D(x).quantize(Q12, rounding=decimal.ROUND_HALF_EVEN), "f")
    return "0.000000000000" if s.lstrip("-") == "0.000000000000" else s


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
    """The first run writes; a later run must produce the same bytes (contract section 6)."""
    if os.path.exists(path):
        got = sha256_file(path)
        assert got == sha256_bytes(data), "determinism: %s differs from the first run" % path
        out("unchanged %s sha256 %s" % (path, got))
        return got
    write_atomic(path, data)
    out("wrote %s %d bytes sha256 %s" % (path, len(data), sha256_bytes(data)))
    return sha256_bytes(data)


def dumps(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=_dec) + "\n"


def _dec(o):
    if isinstance(o, D):
        return format(o, "f")
    if isinstance(o, Fr):
        return "%d/%d" % (o.numerator, o.denominator)
    raise TypeError(type(o))


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh, parse_float=D)


def load_state():
    return load_json(STATE) if os.path.exists(STATE) else {}


def save_state(st):
    write_atomic(STATE, (json.dumps(st, sort_keys=True, indent=1, default=_dec) + "\n").encode("utf-8"))


def mem_available():
    with open("/proc/meminfo", encoding="ascii") as fh:
        for ln in fh:
            if ln.startswith("MemAvailable:"):
                return int(ln.split()[1]) * 1024
    raise AssertionError("no MemAvailable in /proc/meminfo")


def free_bytes(path="/var/lib"):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def memory_gate(reads):
    """MemAvailable at a mode's reads, in order: the first, and one every MEM_RETRY_S after it while every read before
    fell below MEM_FLOOR, MEM_READS at most (map section 7 item 137). The last decides: (passes, it). Pure."""
    assert 1 <= len(reads) <= MEM_READS and all(r < MEM_FLOOR for r in reads[:-1]), reads
    return reads[-1] >= MEM_FLOOR, reads[-1]


def floor_check(read=None, sleep=None, freef=None):
    """Before a mode that reads the venue, the archive's Releases or the set: glibc's two settings, the memory floor -
    a read below it read again every MEM_RETRY_S, MEM_READS reads at most, the last deciding - and the disk floor."""
    read, sleep, freef = read or mem_available, sleep or time.sleep, freef or free_bytes
    assert MALLOC_TUNED, "BLOCKED: glibc did not take the mmap threshold and the arena count"
    reads, free = [read()], freef()
    out("MemAvailable %d bytes, floor %d; free %d bytes, floor %d" % (reads[0], MEM_FLOOR, free, DISK_GATE))
    while reads[-1] < MEM_FLOOR and len(reads) < MEM_READS:
        sleep(MEM_RETRY_S)
        reads.append(read())
        out("MemAvailable read %d of %d at most, %d s after a read below the floor: %d bytes" % (
            len(reads), MEM_READS, MEM_RETRY_S, reads[-1]))
    passes, final = memory_gate(reads)
    assert passes, "BLOCKED: MemAvailable %d bytes at read %d, every read below %d" % (final, len(reads), MEM_FLOOR)
    assert free >= DISK_GATE, "BLOCKED: %d bytes free, below %d" % (free, DISK_GATE)


def show(unit, props):
    args = ["systemctl", "show", unit]
    for prop in props:
        args += ["-p", prop]
    cp = subprocess.run(args, capture_output=True, text=True, env=dict(os.environ, **SHOW_ENV))
    assert cp.returncode == 0, "systemctl show %s: %s" % (unit, cp.stderr.strip())
    return dict(line.split("=", 1) for line in cp.stdout.split("\n") if "=" in line)


def git(*args, tree=WT):
    cp = subprocess.run(["git", "-C", tree] + list(args), capture_output=True, text=True)
    assert cp.returncode == 0, "git %s: %s" % (" ".join(args), cp.stderr.strip())
    return cp.stdout.strip()


def is_active(unit):
    cp = subprocess.run(["systemctl", "is-active", unit], capture_output=True, text=True)
    return cp.stdout.strip()

# ---- the clock: the pair book's idle stretch and both archives' runs -----------------------------------------


def archives_state():
    return {k: is_active(svc) for k, (svc, _timer) in sorted(ARCHIVES.items())}


def quiet(now, budget, state_of=None):
    """None where a unit of `budget` seconds may start at `now`; otherwise why not: it starts inside the pair book's
    idle stretch and ends by its second 590, never near or during either archive's run."""
    state_of = state_of or archives_state
    p = int(now) % SLOT
    if not IDLE[0] <= p <= IDLE[1] - budget:
        return "second %d of the window" % p
    d = int(now) % DAY
    for at, what in CALENDAR:
        if at - budget - CALENDAR_LEAD_S <= d <= at + CALENDAR_LEAD_S:
            return what
    for k, st in sorted(state_of().items()):
        if st in RUNNING:
            return "the %s archive's service is %s" % (k, st)
    return None


def hold(budget, clock=None, sleep=None, state_of=None):
    """Until a unit of `budget` seconds may start; returns that instant and the seconds waited."""
    clock, sleep = clock or time.time, sleep or time.sleep
    assert budget <= IDLE[1] - IDLE[0], "a unit of %d s fits no idle stretch" % budget
    t0 = clock()
    while True:
        now = clock()
        why = quiet(now, budget, state_of)
        if why is None:
            return now, now - t0
        assert now - t0 <= HOLD_MAX_S, "BLOCKED: held %.0f s, the last reason %s" % (now - t0, why)
        sleep(1.0)

# ---- the reward book archive's record: its ledger, every complete run's set.json, every stream file's asset -------


def ledger_records(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    lines = raw.split(b"\n")
    tail = lines.pop()
    return raw, [json.loads(ln) for ln in lines if ln.strip()], tail


def runs_of(recs):
    runs, order = {}, []
    for r in recs:
        a = r.get("run")
        if a not in runs:
            runs[a] = []
            order.append(a)
        runs[a].append(r)
    return runs, order


def archived_sets(recs, state=None):
    """Every run whose ledger holds a complete record: its set.json, asserted by the SHA-256 its last set record
    carries, its tag, assets and counts against that record."""
    state = state or RB_ARCHIVE
    runs, order = runs_of(recs)
    found = []
    for a in order:
        if "complete" not in [r.get("event") for r in runs[a]]:
            continue
        sets = [r for r in runs[a] if r.get("event") == "set"]
        assert sets and isinstance(a, int), "run %r: complete without a set record" % a
        with open(os.path.join(state, "runs", str(a), "set.json"), "rb") as fh:
            raw = fh.read()
        sha = sha256_bytes(raw)
        assert sha == sets[-1]["sha256"], "run %d: set.json sha256 %s, its set record %s" % (a, sha, sets[-1]["sha256"])
        doc = json.loads(raw)
        assert doc["tag"] == sets[-1]["tag"] and doc["assets_n"] == sets[-1]["assets_n"] == len(doc["assets"]) \
            and doc["bytes_total"] == sets[-1]["bytes_total"], "run %d: set.json against its set record" % a
        found.append({"run": a, "tag": doc["tag"], "sha256": sha, "doc": doc})
    return found


def asset_map(sets):
    """(D0, file) -> {tag, asset, bytes, sha256}, every stream file once; a file in two sets is a failed assert."""
    m = {}
    for s in sets:
        for x in s["doc"]["assets"]:
            mt = ASSET_RE.fullmatch(x["asset"])
            assert mt and int(mt.group(1)) == x["T"] and mt.group(2) == x["file"] and int(mt.group(3)) == x["S"] \
                and int(mt.group(4)) == x["k"] and x["T"] == x["S"] // DAY * DAY, "an asset named %r" % x["asset"]
            key = (x["T"], x["file"])
            assert key not in m, "%s in two sets" % x["asset"]
            m[key] = {"tag": s["tag"], "asset": x["asset"], "bytes": x["bytes"], "sha256": x["sha256"]}
    return m


def archived_to(state=None):
    """The asset map of every complete run and the last slot its assets reach."""
    state = state or RB_ARCHIVE
    _raw, recs, _tail = ledger_records(os.path.join(state, "ledger.jsonl"))
    amap = asset_map(archived_sets(recs, state))
    last = max(int(ASSET_RE.fullmatch(v["asset"]).group(3)) for v in amap.values()) if amap else 0
    return amap, last


def ledger_summary(recs):
    """The archive's runs from its own records: each run's set and terminal record, and whether it began on the
    calendar; whether the archive is halted."""
    runs, order = runs_of(recs)
    lines = []
    for a in order:
        rs = runs[a]
        ev = [r.get("event") for r in rs]
        term = [e for e in ev if e in ("complete", "empty", "halt")]
        sec = a % DAY if isinstance(a, int) else None
        when = "calendar" if sec == CALENDAR[0][0] else ("off-calendar, second %s of the day" % sec)
        parts = ["run %s %s, %s: %d records; terminal %s" % (a, utc(a) if isinstance(a, int) else "-", when, len(rs),
                                                            term[-1] if term else "none")]
        for r in [r for r in rs if r.get("event") == "set"][-1:]:
            parts.append("set %s: %s files, %s bytes, slots %s to %s" % (
                r.get("tag"), r.get("assets_n"), r.get("bytes_total"), r.get("first_S"), r.get("last_S")))
        for r in rs:
            if r.get("event") in ("deferred", "halt", "refused", "timer-disabled"):
                parts.append("%s in %s: %s" % (r.get("event"), r.get("phase"), r.get("reason", r.get("exit"))))
        lines.append("; ".join(parts))
    flags = [r.get("event") for r in recs if r.get("event") in ("halt", "clear")]
    return {"runs": order, "lines": lines, "halted": bool(flags) and flags[-1] == "halt",
            "terminal": {a: [r.get("event") for r in runs[a] if r.get("event") in ("complete", "empty", "halt")]
                         for a in order}}

# ---- the reward book's store: a day's selection, slot records and polls (fetch alone reads them) -----------------


def day_dir(d0, root=None):
    return os.path.join(root or RB_ROOT, str(d0))


def selection_of(d0, root=None):
    """The day's first ok attempt and its replies' bytes, asserted against its record (TZ-33's load_selection rule),
    with the SHA-256 of its select.<a>.json; None where the day holds none."""
    ddir = day_dir(d0, root)
    if not os.path.isdir(ddir):
        return None
    a = 0
    while True:
        jp, rp = (os.path.join(ddir, "select.%d.json" % a), os.path.join(ddir, "select.%d.replies.jsonl.gz" % a))
        if not os.path.exists(jp):
            if os.path.exists(rp):
                a += 1
                continue
            return None
        with open(jp, "rb") as fh:
            jraw = fh.read()
        rec = json.loads(jraw)
        if rec.get("ok") is True:
            with open(rp, "rb") as fh:
                rraw = fh.read()
            assert sha256_bytes(rraw) == rec["replies"]["sha256"], "%s: replies differ from their record" % rp
            return {"attempt": a, "rec": rec, "sha256": sha256_bytes(jraw), "replies": rraw}
        a += 1


def slot_records(d0, root=None):
    """S -> [slot.json of k = 0, 1, ...] for every slot of the day the store holds a record of, by its listing."""
    by = {}
    for name in sorted(os.listdir(day_dir(d0, root))):
        m = SLOT_FILE_RE.fullmatch(name)
        if m is None or m.group(3) != "slot.json":
            continue
        s, k = int(m.group(1)), int(m.group(2))
        with open(os.path.join(day_dir(d0, root), name), "rb") as fh:
            by.setdefault(s, {})[k] = json.loads(fh.read())
    return {s: [v[k] for k in sorted(v)] for s, v in by.items()}


def slot_problem(s, recs, sel_sha, n_members, assets, d0):
    """The first rule slot s fails, or None: its records consecutive from k = 0, each of the day's selection and
    every member, its stream opened and not cut, the first subscribed by S, the last's last frame at or after S + 900,
    no gap above 15 s within a file or between two, and every stream file in the archive's assets."""
    if not recs:
        return "no slot record"
    files = []
    for k, sj in enumerate(recs):
        if sj.get("S") != s or sj.get("index") != k or sj.get("day") != d0:
            return "records: index %d" % k
        if (sj.get("selection") or {}).get("sha256") != sel_sha or sj.get("markets") != n_members:
            return "records: another selection"
        if sj.get("error") is not None:
            return "records: an error"
        st = sj.get("stream") or {}
        if st.get("opened") is not True or st.get("off_reason") is not None or st.get("file") is None:
            return "stream: not opened"
        if st.get("cut") is not False:
            return "stream: cut"
        if st.get("file") != "%d.%d.stream.jsonl.gz" % (s, k):
            return "stream: its file"
        g = st.get("max_gap_ns")
        if not (type(g) is int and g <= GAP_MAX_NS):
            return "stream: a gap above 15 s"
        a, b = st.get("first_frame_wall_ns"), st.get("last_frame_wall_ns")
        if not (type(a) is int and type(b) is int and a <= b):
            return "stream: no frame"
        files.append((a, b, st["file"]))
    sub = (recs[0].get("stream") or {}).get("subscribed_wall_ns")
    if recs[0].get("joined_late") is not False or not (type(sub) is int and sub <= s * 10 ** 9):
        return "stream: subscribed late"
    if files[-1][1] < (s + SLOT) * 10 ** 9:
        return "stream: ended early"
    for (_a0, b0, _f0), (a1, _b1, _f1) in zip(files, files[1:]):
        if a1 - b0 > GAP_MAX_NS:
            return "stream: a gap above 15 s between files"
    for _a, _b, f in files:
        if (d0, f) not in assets:
            return "stream: not archived"
    return None


def fee_of(doc):
    """A member's maker rebate coefficient, the fee rate times the rebate rate, from its gamma document as the
    selection stored it: 0 where fees are not enabled or the schedule is not the venue's taker-only form."""
    if not isinstance(doc, dict) or doc.get("feesEnabled") is not True:
        return Fr(0)
    fs = doc.get("feeSchedule")
    if not isinstance(fs, dict) or fs.get("takerOnly") is not True or str(fs.get("exponent")) != "1":
        return Fr(0)
    return Fr(str(fs.get("rate"))) * Fr(str(fs.get("rebateRate")))


def gamma_docs_of(replies):
    """conditionId -> [documents] of every served gamma reply an attempt stored, numbers as Decimals of their text."""
    by = {}
    with gzip.open(__import__("io").BytesIO(replies), "rt", encoding="utf-8") as fh:
        for ln in fh:
            if not ln.strip():
                continue
            r = json.loads(ln)
            if r.get("kind") != "gamma" or r.get("status") != 200:
                continue
            for d in json.loads(r["raw"], parse_float=D):
                if isinstance(d, dict) and isinstance(d.get("conditionId"), str):
                    by.setdefault(d["conditionId"], []).append(d)
    return by


def members_of(sel):
    """The day's members as the replay takes them: condition id, its first token, the minimum size in hundredths of
    a share, the maximum spread in half-thousandths, the selection's daily rate and the rebate coefficient."""
    docs = gamma_docs_of(sel["replies"])
    out_ = []
    for m in sel["rec"]["members"]:
        cid, toks = m["condition_id"], m["token_ids"]
        assert CID_RE.fullmatch(cid) and len(toks) == 2 and all(TOKEN_RE.fullmatch(t) for t in toks), cid
        ms, vu = Fr(m["min_size"]) * 100, Fr(m["max_spread"]) * 20
        assert ms.denominator == 1 and vu.denominator == 1 and ms >= 0 and vu >= 0, "%s: size or spread" % cid
        fees = {fee_of(x) for x in docs.get(cid, [])}
        assert len(fees) == 1, "%s: %d fee terms in the selection's documents" % (cid, len(fees))
        out_.append({"cid": cid, "tok": toks[0], "ms": int(ms), "vu": int(vu), "rate": Fr(m["rate"]),
                     "fee": fees.pop()})
    return out_


def polls_of(d0, recs_by_slot, root=None):
    """Every served poll of the day's slots, in the order received: (recv_ns, condition id, row), row None where the
    page held no row, else (the daily rate, the competitiveness), each the Fraction of its decimal text - the rate the
    sum over the row's reward configurations in force on the poll's UTC date, from start_date to end_date."""
    polls, counts = [], collections.Counter()
    for s in sorted(recs_by_slot):
        for sj in recs_by_slot[s]:
            f = (sj.get("rewards") or {}).get("file")
            if f is None:
                continue
            with gzip.open(os.path.join(day_dir(d0, root), f), "rt", encoding="utf-8") as fh:
                for ln in fh:
                    if not ln.strip():
                        continue
                    r = json.loads(ln)
                    counts["polls"] += 1
                    if r.get("status") != 200 or r.get("raw") is None:
                        counts["unserved"] += 1
                        continue
                    data = json.loads(r["raw"], parse_float=D).get("data")
                    row = None
                    if data:
                        d = data[0]
                        day = utc(r["recv_wall_ns"] // 10 ** 9)[:10]
                        rate = sum((Fr(str(c["rate_per_day"])) for c in d["rewards_config"]
                                    if (c.get("start_date") is None or str(c["start_date"])[:10] <= day) and
                                    (c.get("end_date") is None or day <= str(c["end_date"])[:10])), Fr(0))
                        row = (rate, Fr(str(d["market_competitiveness"])))
                    else:
                        counts["no row"] += 1
                    polls.append((r["recv_wall_ns"], sys.intern(r["condition_id"]), row))
    polls.sort(key=lambda p: (p[0], p[1]))
    return polls, counts

# ---- the replay: one UTC day of the reward book's streams, our quote on every member (TZ-41 section 1) -------------

MS_NS = 10 ** 6
S_NS = 10 ** 9
PRICE_UNIT = 1000            # a price as an integer of thousandths
SIZE_UNIT = 100              # a size as an integer of hundredths of a share
STALE_NS = S_NS              # a market's pending order events are resolved once any line's host instant passes them by 1 s
INSIDE = (200, 1800)         # the qualifying midpoint, in half-thousandths, inside [0.10, 0.90]: one side scores a third
SEND, CANCEL = 0, 1
ZERO = (0, 1)
NEVER = 1 << 62

_PRICE = re.compile(r"(0|[1-9][0-9]*)(?:\.([0-9]{1,3}))?")
_SIZE = re.compile(r"(0|[1-9][0-9]*)(?:\.([0-9]{1,2}))?")
_PRICES, _SIZES = {}, {}


def price_int(s):
    v = _PRICES.get(s)
    if v is None:
        m = _PRICE.fullmatch(s)
        assert m, "a price %r" % (s,)
        v = _PRICES[s] = int(m.group(1)) * PRICE_UNIT + int((m.group(2) or "").ljust(3, "0"))
    return v


def size_int(s):
    v = _SIZES.get(s)
    if v is None:
        m = _SIZE.fullmatch(s)
        assert m, "a size %r" % (s,)
        v = int(m.group(1)) * SIZE_UNIT + int((m.group(2) or "").ljust(2, "0"))
        if len(_SIZES) < 1 << 16:
            _SIZES[s] = v
    return v


# A price_change frame as the venue sends it and the reward book stores it, matched whole: two entries, each field a
# run of digits, hex or BUY/SELL, where no escape can occur (TZ-30's and TZ-32's PC_LINE).
_ENTRY = (r'\{\\"asset_id\\":\\"([0-9]+)\\", \\"price\\":\\"([0-9.]+)\\", \\"size\\":\\"([0-9.]+)\\", '
          r'\\"side\\":\\"(BUY|SELL)\\", \\"hash\\":\\"[0-9a-f]*\\", \\"best_bid\\":\\"[0-9.]+\\", '
          r'\\"best_ask\\":\\"[0-9.]+\\"\}')
PC_LINE = re.compile(r'\{"recv_ns":([0-9]+),"mono_ns":-?[0-9]+,"raw":"\{\\"market\\":\\"(0x[0-9a-f]{64})\\", '
                     r'\\"price_changes\\":\[' + _ENTRY + ', ' + _ENTRY + r'\], \\"timestamp\\":\\"([0-9]+)\\", '
                     r'\\"event_type\\":\\"price_change\\"\}"\}\n?')


class Order:
    __slots__ = ("side", "p", "s", "q", "state", "done_at", "xc", "fill_vt")

    def __init__(self, side, p, s):
        self.side, self.p, self.s, self.q = side, p, s, None
        self.state = "sent"        # sent, resting, filled, cancelled, refused
        self.done_at = None        # the venue instant it left the book or was refused
        self.xc = 0                # the crossing size already counted against it
        self.fill_vt = None        # the venue instant of its last fill


class Spec:
    """A variant (TZ-41 section 1): its rule, its queue place, the crossing orders, the competitors' score."""
    __slots__ = ("name", "rule", "front", "takers", "denom", "L")

    def __init__(self, name, rule, front, takers, denom):
        assert rule in ("alone", "touch") and denom in ("pess", "opt", "venue"), (rule, denom)
        self.name, self.rule, self.front, self.takers, self.denom = name, rule, front, takers, denom
        self.L = LATENCY_MS * MS_NS


SPECS = tuple(Spec(*v) for v in VARIANTS)


class MV:
    """One market in one variant: our orders, their events, our fills, the host's knowledge, the reward."""
    __slots__ = ("sp", "live", "resting", "pend", "fills", "unknown", "x_known", "x", "cost", "rew", "share", "t",
                 "acc", "n", "scored_ns", "touch")

    def __init__(self, sp):
        self.sp = sp
        self.live = {"b": None, "a": None}
        self.resting = []
        self.pend = []
        self.fills = []
        self.unknown = []
        self.x_known = 0
        self.x = 0                 # hundredths of a share of the market's first token, + long
        self.cost = 0              # thousandths x hundredths: a bid filled at p costs +p f, an ask -p f
        self.rew = D(0)
        self.share = ZERO
        self.t = None              # the last instant the variant's clock reached
        self.acc = 0               # nanoseconds at the share in force, not yet added to the reward
        self.n = {"sent": 0, "cancels": 0, "refused": 0, "crossings": 0, "fills": 0}
        self.scored_ns = 0
        self.touch = None          # the qualifying touch of its last share; None: any entry can move it


class Market:
    __slots__ = ("cid", "tok", "ms", "vu", "fee", "rate", "ven", "bids", "asks", "bp", "ap", "block", "bvt",
                 "touch0", "seeded", "mvs", "c", "shadow", "dirty", "dtouch", "wake", "tick", "lastmid")

    def __init__(self, m, specs):
        self.cid, self.tok, self.ms, self.vu, self.fee = m["cid"], m["tok"], m["ms"], m["vu"], m["fee"]
        self.rate = (m["rate"].numerator, m["rate"].denominator)
        self.ven = (None, 1)       # the venue's score of every maker, x 12 over vu^2 * 100: none before a poll
        self.bids, self.asks, self.bp, self.ap = {}, {}, [], []
        self.block, self.bvt, self.touch0 = [], None, (None, None)
        self.seeded = False
        self.mvs = [MV(sp) for sp in specs]
        self.c = {"snapshots": 0, "touch_equal": 0, "book_equal": 0, "matches": 0}
        self.shadow = None
        self.dirty = False
        self.dtouch = None         # the touch the quoting rule last decided on
        self.wake = 0              # the first host instant the host learns of a fill, a refusal or a cancel
        self.tick = 10             # thousandths: the seed's tick_size, 0.01 until one is read
        self.lastmid = None        # twice the last midpoint of a two-sided book, in thousandths: the day's mark

    # -- the book ---------------------------------------------------------------------------------------------
    def set_level(self, side, p, s):
        bk, pl = (self.bids, self.bp) if side == "b" else (self.asks, self.ap)
        old = bk.get(p, 0)
        if s:
            if not old:
                bisect.insort(pl, p)
            bk[p] = s
        elif old:
            del bk[p]
            del pl[bisect.bisect_left(pl, p)]
        return old

    def replace(self, bids, asks):
        self.bids, self.asks = bids, asks
        self.bp, self.ap = sorted(bids), sorted(asks)

    def best(self, side):
        if side == "b":
            return self.bp[-1] if self.bp else None
        return self.ap[0] if self.ap else None

    def qual_best(self, side, ours):
        """The best displayed level whose size reaches the minimum size, or our own qualifying order's price."""
        ms = self.ms
        if side == "b":
            for p in reversed(self.bp):
                if self.bids[p] >= ms:
                    return p if ours is None or p > ours else ours
            return ours
        for p in self.ap:
            if self.asks[p] >= ms:
                return p if ours is None or p < ours else ours
        return ours

    def others(self, mid_u):
        """A and B: the displayed levels of at least the minimum size inside the band around mid_u, each side's sum
        of d^2 times size, over vu^2 * 100."""
        vu, ms = self.vu, self.ms
        A = 0
        lo = mid_u - vu                          # a bid scores where 2p > mid_u - vu
        i = len(self.bp) - 1
        while i >= 0:
            p = self.bp[i]
            if 2 * p <= lo:
                break
            s = self.bids[p]
            if s >= ms:
                d = vu - (mid_u - 2 * p)
                A += d * d * s
            i -= 1
        B = 0
        hi = mid_u + vu
        for p in self.ap:
            if 2 * p >= hi:
                break
            s = self.asks[p]
            if s >= ms:
                d = vu - (2 * p - mid_u)
                B += d * d * s
        return A, B

    def liquidation(self, x):
        """Thousandths x hundredths: the proceeds of selling x > 0 into the bids, or minus the cost of buying -x from
        the asks, the remainder beyond the book at 0 or at 1."""
        if x == 0:
            return 0
        if x > 0:
            left, val = x, 0
            for p in reversed(self.bp):
                f = min(left, self.bids[p])
                val += f * p
                left -= f
                if not left:
                    break
            return val
        left, val = -x, 0
        for p in self.ap:
            f = min(left, self.asks[p])
            val -= f * p
            left -= f
            if not left:
                break
        return val - left * PRICE_UNIT


def envelope(A, B, inside):
    """The competitors' score, x 12 over vu^2 * 100, from the displayed sides' sums A and B: (hi, lo), the most and
    the least the levels can score, split among makers in any way (TZ-41 section 1, the reward)."""
    m, M = min(A, B), max(A, B)
    if inside:
        return 4 * (2 * m + M), max(3 * (A + B), 4 * M)
    return 12 * m, 0


class Day:
    """The replay of one day's streams and polls (TZ-41 section 1). Members: dicts with cid, tok (the market's first
    token), ms (minimum size, hundredths), vu (maximum spread, half-thousandths), fee (Fraction: the fee rate times the
    rebate rate) and rate (the selection's daily rate, Fraction)."""

    def __init__(self, d0, members, specs=SPECS):
        self.d0, self.specs = d0, specs
        self.mk = [Market(m, specs) for m in members]
        self.by_cid = {M.cid: M for M in self.mk}
        assert len(self.by_cid) == len(self.mk), "a member twice"
        self.idx = {M.cid: i for i, M in enumerate(self.mk)}
        self.stale = []            # (tau, seq, market index)
        self.seq = 0
        self.live = False          # decisions, fills and rewards run from the day's first slot instant
        self.c = {"lines": 0, "frames": 0, "fast": 0, "skipped": 0, "polls": 0, "switches": 0, "subscribes": 0,
                  "closes": 0}

    # -- rewards ------------------------------------------------------------------------------------------------
    def integrate(self, M, t):
        for mv in M.mvs:
            self.integrate_one(M, mv, t)

    def integrate_one(self, M, mv, t):
        """The variant's clock advanced to t where t is later: the time passes at the share and the rate in force."""
        if mv.t is None:
            mv.t = t
        elif t > mv.t:
            mv.acc += t - mv.t
            mv.t = t

    def flush(self, M, mv):
        """The time at the share and the rate in force added to the reward: rate * share * dt / 86,400 s, a Decimal
        quotient at 50 significant digits, summed in order - before either changes."""
        if mv.acc:
            num, den = mv.share
            if num:
                rn, rd = M.rate
                if rn:
                    mv.rew = C50.add(mv.rew, C50.divide(D(rn * num * mv.acc), D(rd * den * DAY * S_NS)))
                mv.scored_ns += mv.acc
            mv.acc = 0

    def set_share(self, M, mv, sh):
        if sh != mv.share:
            self.flush(M, mv)
            mv.share = sh

    def refresh(self, M, ents=None, t=None):
        """Every variant's clock advanced to host instant t, then its share recomputed - or, given a frame's entries,
        only the shares an entry can move: a variant's with resting orders whose entries reach its band or its
        qualifying touch."""
        cache = {}
        for mv in M.mvs:
            if t is not None:
                self.integrate_one(M, mv, t)
            if ents is not None:
                if not mv.resting:
                    continue
                tch = mv.touch
                if tch is not None:
                    qb, qa = tch
                    lo, hi = qb + qa - M.vu, qb + qa + M.vu
                    for side, p, _s in ents:
                        if (2 * p > lo or p >= qb) if side == "b" else (2 * p < hi or p <= qa):
                            break
                    else:
                        continue
            self.set_share(M, mv, self.share_of(M, mv, cache))

    def share_of(self, M, mv, cache):
        """Our share of the market's score at this instant, as (numerator, denominator); (0, 1) where we score
        nothing. `cache` keeps, for one book state, each set of our resting orders' parts."""
        if not M.seeded or not mv.resting:
            mv.touch = None
            return ZERO
        key = tuple((o.side, o.p, o.s) for o in mv.resting)
        parts = cache.get(key)
        if parts is None:
            parts = cache[key] = self.parts_of(M, mv.resting)
        if parts is None:
            mv.touch = None
            return ZERO
        touch, Q, hi, lo = parts
        mv.touch = touch
        if Q == 0:
            return ZERO
        vn, vd = M.ven
        den = mv.sp.denom
        if vn is None:
            O_n, O_d = (lo if den == "opt" else hi), 1
        elif den == "pess":
            O_n, O_d = (hi, 1) if hi * vd >= vn else (vn, vd)
        elif den == "opt":
            O_n, O_d = (lo, 1) if lo * vd <= vn else (vn, vd)
        else:
            O_n, O_d = vn, vd
        return (Q * O_d, Q * O_d + O_n)

    def parts_of(self, M, resting):
        """For one set of our resting orders on the book as it stands: the qualifying touch, our score Q and the
        competitors' hi and lo, all x 12 over vu^2 * 100; None where no qualifying touch exists."""
        ms, vu = M.ms, M.vu
        ob = oa = None
        for o in resting:
            if o.s >= ms:
                if o.side == "b":
                    ob = o.p if ob is None or o.p > ob else ob
                else:
                    oa = o.p if oa is None or o.p < oa else oa
        if ob is None and oa is None:
            return None
        qb, qa = M.qual_best("b", ob), M.qual_best("a", oa)
        if qb is None or qa is None or qb >= qa:
            return None
        mid_u = qb + qa
        q1 = q2 = 0
        for o in resting:
            if o.s < ms:
                continue
            su = (mid_u - 2 * o.p) if o.side == "b" else (2 * o.p - mid_u)
            if 0 <= su < vu:
                d = vu - su
                if o.side == "b":
                    q1 += d * d * o.s
                else:
                    q2 += d * d * o.s
        inside = INSIDE[0] <= mid_u <= INSIDE[1]
        Q = 4 * max(3 * min(q1, q2), max(q1, q2)) if inside else 12 * min(q1, q2)
        if Q == 0:
            return ((qb, qa), 0, 0, 0)
        hi, lo = envelope(*M.others(mid_u), inside)
        return ((qb, qa), Q, hi, lo)

    # -- our orders' events ---------------------------------------------------------------------------------------
    def push(self, mi, mv, tau, kind, o):
        self.seq += 1
        heapq.heappush(mv.pend, (tau, self.seq, kind, o))
        heapq.heappush(self.stale, (tau, self.seq, mi))

    def resolve(self, M, before):
        """Every variant's events of M due before `before`, in their order; the reward integrated to each."""
        for mv in M.mvs:
            P = mv.pend
            while P and P[0][0] < before:
                tau, _s, kind, o = heapq.heappop(P)
                self.integrate_one(M, mv, tau)
                if kind == SEND:
                    opp = M.best("a" if o.side == "b" else "b")
                    if opp is not None and (o.p >= opp if o.side == "b" else o.p <= opp):
                        o.state, o.done_at = "refused", tau
                        mv.n["refused"] += 1
                        if tau + mv.sp.L < M.wake:
                            M.wake = tau + mv.sp.L
                    else:
                        o.q = 0 if mv.sp.front else (M.bids if o.side == "b" else M.asks).get(o.p, 0)
                        o.state = "resting"
                        mv.resting.append(o)
                elif o.state in ("sent", "resting"):
                    o.state, o.done_at = "cancelled", tau
                    if tau + mv.sp.L < M.wake:
                        M.wake = tau + mv.sp.L
                    mv.resting = [x for x in mv.resting if x.state == "resting"]
                self.set_share(M, mv, self.share_of(M, mv, {}))

    def resolve_stale(self, h):
        S = self.stale
        lim = h - STALE_NS
        while S and S[0][0] < lim:
            tau, _s, mi = heapq.heappop(S)
            M = self.mk[mi]
            if M.block:
                self.close_block(M, False)
            self.resolve(M, tau + 1)

    # -- fills ----------------------------------------------------------------------------------------------------
    def fill(self, M, mv, o, vt, f, kind):
        M.dirty = True
        if vt + mv.sp.L < M.wake:
            M.wake = vt + mv.sp.L
        o.s -= f
        o.fill_vt = vt
        mv.fills.append((vt, o.side, o.p, f, kind))
        dx = f if o.side == "b" else -f
        mv.x += dx
        mv.cost += dx * o.p
        heapq.heappush(mv.unknown, (vt, dx))
        mv.n["fills"] += 1
        if o.s == 0:
            o.state, o.done_at = "filled", vt

    def known_x(self, mv, h):
        u = mv.unknown
        while u and u[0][0] + mv.sp.L <= h:
            mv.x_known += heapq.heappop(u)[1]
        return mv.x_known

    def sweep(self, M, side, t0):
        """A match's sweep of one side from its touch before the block: [(price, size taken)], best first, through
        the last level it reached."""
        cur = M.bids if side == "b" else M.asks
        first, dec = {}, {}
        for sd, p, old, new in M.block:
            if sd != side:
                continue
            if p not in first:
                first[p] = old
            dec[p] = first[p] - new
        if t0 is None or dec.get(t0, 0) <= 0:
            return []
        levels = sorted((p for p in set(first) | set(cur) if (p <= t0 if side == "b" else p >= t0)),
                        reverse=(side == "b"))
        sw = []
        for p in levels:
            pre = first[p] if p in first else cur.get(p, 0)
            if pre <= 0:
                continue
            c = dec.get(p, 0)
            if c <= 0:
                break
            sw.append((p, c))
            if c < pre:
                break
        return sw

    def close_block(self, M, match):
        """A block of entries with one venue stamp ends; where the venue's book frame of the same stamp followed it,
        a match: every resting order the sweep reached fills beyond its queue place."""
        if match and M.block:
            hit = 0
            for side, t0 in (("b", M.touch0[0]), ("a", M.touch0[1])):
                sw = self.sweep(M, side, t0)
                if not sw:
                    continue
                hit += 1
                last = sw[-1][0]
                at = dict(sw)
                for mv in M.mvs:
                    for o in mv.resting:
                        if o.side != side or o.state != "resting":
                            continue
                        f = 0
                        if (last <= o.p) if side == "b" else (last >= o.p):
                            tot = sum(c for p, c in sw if (p <= o.p if side == "b" else p >= o.p))
                            f = min(o.s, max(0, tot - o.q))
                        o.q = max(0, o.q - at.get(o.p, 0))
                        if f > 0:
                            self.fill(M, mv, o, M.bvt, f, "m")
                    mv.resting = [x for x in mv.resting if x.state == "resting"]
            if hit:
                M.c["matches"] += 1
        for mv in M.mvs:
            for o in mv.resting:
                lv = (M.bids if o.side == "b" else M.asks).get(o.p, 0)
                if lv < o.q:
                    o.q = lv
        t = M.bvt
        M.block, M.bvt = [], None
        self.cross(M, t)

    def cross(self, M, vt):
        """Where the opposite side reaches a resting order's price with no match, the orders there would have met
        ours: in a variant that counts them takers, our order fills at once for their size not yet counted."""
        bb, ba = M.best("b"), M.best("a")
        for mv in M.mvs:
            if not mv.sp.takers:
                continue
            gone = False
            for o in mv.resting:
                if o.state != "resting":
                    continue
                if o.side == "b":
                    c = sum(s for p, s in M.asks.items() if p <= o.p) if ba is not None and ba <= o.p else 0
                else:
                    c = sum(s for p, s in M.bids.items() if p >= o.p) if bb is not None and bb >= o.p else 0
                if c > o.xc:
                    f = min(o.s, c - o.xc)
                    mv.n["crossings"] += 1
                    self.fill(M, mv, o, vt, f, "x")
                    gone = gone or o.state != "resting"
                o.xc = c
            if gone:
                mv.resting = [x for x in mv.resting if x.state == "resting"]

    # -- the quoting rule -------------------------------------------------------------------------------------------
    def decide(self, M, h):
        """The quoting rule after a frame of the market reaches the host at h. Where the touch is the one it last
        decided on and the host has learned nothing since, it would decide the same, and returns."""
        if not (self.live and M.seeded):
            return
        bb, ba = M.best("b"), M.best("a")
        if (bb, ba) == M.dtouch and h < M.wake:
            return
        M.dtouch = (bb, ba)
        mi = self.idx[M.cid]
        for mv in M.mvs:
            cap = CAP_CLIPS * M.ms
            L = mv.sp.L
            x = None
            tb = ta = None
            if bb is not None and ba is not None:
                if mv.sp.rule == "alone":
                    if ba - bb >= SPREAD_TICKS * M.tick:
                        tb, ta = bb + M.tick, ba - M.tick
                else:
                    tb, ta = bb, ba
            band = tb is not None and ta - tb < M.vu and M.ms > 0
            for side in ("b", "a"):
                o = mv.live[side]
                if o is not None and o.done_at is not None and o.done_at + L <= h:
                    o = mv.live[side] = None
                tgt = None
                if band:
                    tgt = tb if side == "b" else ta
                    if not 0 < tgt < PRICE_UNIT:
                        tgt = None
                if tgt is not None:
                    if x is None:
                        x = self.known_x(mv, h)
                    if x >= cap if side == "b" else x <= -cap:
                        tgt = None
                stale = (o is not None and o.state == "resting" and o.fill_vt is not None and o.fill_vt + L <= h
                         and o.s < M.ms)
                if tgt is None:
                    if o is not None:
                        self.push(mi, mv, h + L, CANCEL, o)
                        mv.n["cancels"] += 1
                        mv.live[side] = None
                elif o is None:
                    n = Order(side, tgt, M.ms)
                    mv.live[side] = n
                    self.push(mi, mv, h + L, SEND, n)
                    mv.n["sent"] += 1
                elif o.p != tgt or stale:
                    self.push(mi, mv, h + L, CANCEL, o)
                    mv.n["cancels"] += 1
                    n = Order(side, tgt, M.ms)
                    mv.live[side] = n
                    self.push(mi, mv, h + L, SEND, n)
                    mv.n["sent"] += 1
        w = NEVER
        for mv in M.mvs:
            L = mv.sp.L
            for o in mv.live.values():
                if o is None:
                    continue
                for t in (o.done_at, o.fill_vt):
                    if t is not None and t + L < w:
                        w = t + L
            if mv.unknown and mv.unknown[0][0] + L < w:
                w = mv.unknown[0][0] + L
        M.wake = w

    # -- the stream ---------------------------------------------------------------------------------------------
    def session(self, ev, h, reason):
        """A session event of the live stream: every market's book cleared at a connect or subscribe; at a close
        other than the slot's end, every live order of ours cancelled."""
        if ev == "subscribe":
            self.c["subscribes"] += 1
        elif ev == "close" and reason != "end":
            self.c["closes"] += 1
        for M in self.mk:
            if M.block:
                self.close_block(M, False)
            self.resolve(M, h)
            self.integrate(M, h)
        if ev in ("connect", "subscribe"):
            for M in self.mk:
                M.replace({}, {})
                M.seeded = False
                self.refresh(M, None, h)
        elif ev == "close" and reason != "end":
            for mi, M in enumerate(self.mk):
                for mv in M.mvs:
                    for side in ("b", "a"):
                        o = mv.live[side]
                        if o is not None:
                            self.push(mi, mv, h + mv.sp.L, CANCEL, o)
                            mv.n["cancels"] += 1
                            mv.live[side] = None

    def poll(self, t, cid, row):
        """A served reward poll of a member: its daily rate and the venue's figure from then on; a page with no row
        stops the reward (rate 0)."""
        M = self.by_cid.get(cid)
        if M is None:
            return
        if self.live:
            if M.block:
                self.close_block(M, False)
            self.resolve(M, t)
            self.integrate(M, t)
            for mv in M.mvs:
                self.flush(M, mv)
        if row is None:
            M.rate, M.ven = (0, 1), (None, 1)
        else:
            rate, comp = row
            M.rate = (rate.numerator, rate.denominator)
            v = comp * rate * M.vu * M.vu * SIZE_UNIT * 12
            M.ven = (v.numerator, v.denominator)
        self.c["polls"] += 1
        if self.live:
            self.refresh(M, None, t)

    def frame_items(self, fr, h, shadow):
        seed = isinstance(fr, list)
        touched = []
        for it in (fr if seed else (fr,)):
            if not isinstance(it, dict):
                continue
            M = self.by_cid.get(it.get("market"))
            if M is None:
                continue
            et = it.get("event_type")
            if et == "book":
                if it.get("asset_id") != M.tok:
                    continue
                bids = {}
                for lv in it["bids"]:
                    bids[price_int(lv["price"])] = size_int(lv["size"])
                asks = {}
                for lv in it["asks"]:
                    asks[price_int(lv["price"])] = size_int(lv["size"])
                bids = {p: s for p, s in bids.items() if s}
                asks = {p: s for p, s in asks.items() if s}
                ts = it.get("tick_size")
                if seed and ts in ("0.1", "0.01", "0.001"):
                    M.tick = price_int(ts)
                if shadow:
                    M.shadow = [bids, asks, True]
                    continue
                vt = int(it["timestamp"]) * MS_NS
                if M.block and vt != M.bvt:
                    self.close_block(M, False)
                self.resolve(M, vt)
                if seed:
                    if M.block:
                        self.close_block(M, False)
                    M.seeded = True
                else:
                    M.c["snapshots"] += 1
                    if M.block:
                        self.close_block(M, vt == M.bvt)
                    bb, ba = M.best("b"), M.best("a")
                    nb = max(bids) if bids else None
                    na = min(asks) if asks else None
                    if (bb, M.bids.get(bb), ba, M.asks.get(ba)) == (nb, bids.get(nb), na, asks.get(na)):
                        M.c["touch_equal"] += 1
                    if M.bids == bids and M.asks == asks:
                        M.c["book_equal"] += 1
                M.replace(bids, asks)
                for mv in M.mvs:
                    for o in mv.resting:
                        lv = (M.bids if o.side == "b" else M.asks).get(o.p, 0)
                        if lv < o.q:
                            o.q = lv
                self.cross(M, vt)
                touched.append((M, None))
            elif et == "tick_size_change":
                ts = it.get("new_tick_size")
                if it.get("asset_id") == M.tok and ts in ("0.1", "0.01", "0.001"):
                    M.tick = price_int(ts)
                    M.dtouch = None
            elif et == "price_change":
                ents = [(("b" if pc["side"] == "BUY" else "a"), price_int(pc["price"]), size_int(pc["size"]))
                        for pc in it["price_changes"] if pc.get("asset_id") == M.tok]
                if not ents:
                    continue
                if shadow:
                    self.shadow_apply(M, ents)
                    continue
                touched.append(self.entries(M, int(it["timestamp"]) * MS_NS, ents))
        return touched

    def shadow_apply(self, M, ents):
        sh = M.shadow
        if sh is None or not sh[2]:
            return
        for side, p, s in ents:
            bk = sh[0] if side == "b" else sh[1]
            if s:
                bk[p] = s
            else:
                bk.pop(p, None)

    def entries(self, M, vt, ents):
        if M.block and vt != M.bvt:
            self.close_block(M, False)
        self.resolve(M, vt)
        if not M.block:
            M.bvt = vt
            M.touch0 = (M.best("b"), M.best("a"))
        for side, p, s in ents:
            old = M.set_level(side, p, s)
            M.block.append((side, p, old, s))
        return (M, ents)

    def pc_fast(self, g, shadow):
        """A price_change line matched whole by PC_LINE: the same as frame_items on its parsed frame."""
        M = self.by_cid.get(g[1])
        if M is None:
            return None
        ents = [("b" if g[j + 3] == "BUY" else "a", price_int(g[j + 1]), size_int(g[j + 2])) for j in (2, 6)
                if g[j] == M.tok]
        if not ents:
            return None
        if shadow:
            self.shadow_apply(M, ents)
            return None
        return self.entries(M, int(g[10]) * MS_NS, ents)

    def after(self, tm, h):
        """After a frame of a market: the quoting rule, then the shares it can have moved."""
        M, ents = tm
        if M.bp and M.ap:
            M.lastmid = M.bp[-1] + M.ap[0]
        self.decide(M, h)
        if M.dirty:
            M.dirty = False
            self.refresh(M, None, h)
        else:
            self.refresh(M, ents, h)

    def switch(self, S_ns):
        """The slot's instant: every market's book becomes the one the new slot's file has built to it."""
        self.c["switches"] += 1
        for M in self.mk:
            if M.block:
                self.close_block(M, False)
            self.resolve(M, S_ns)
            self.integrate(M, S_ns)
            sh = M.shadow
            M.shadow = None
            if sh is None:
                M.replace({}, {})
                M.seeded = False
            else:
                M.replace(sh[0], sh[1])
                M.seeded = sh[2]
            for mv in M.mvs:
                for o in mv.resting:
                    lv = (M.bids if o.side == "b" else M.asks).get(o.p, 0)
                    if lv < o.q:
                        o.q = lv
            if M.seeded:
                self.cross(M, S_ns)
        self.live = True
        for M in self.mk:
            if M.bp and M.ap:
                M.lastmid = M.bp[-1] + M.ap[0]
            M.dtouch = None
            self.decide(M, S_ns)
            self.refresh(M, None, S_ns)

    def at_host(self, h, shadow, switched, S_ns, polls):
        if not shadow and not switched:
            self.switch(S_ns)
        if not shadow:
            while polls and polls[0][0] <= h:
                t, cid, row = polls.popleft()
                self.poll(t, cid, row)
            self.resolve_stale(h)
        return switched or not shadow

    def feed_slot(self, S, paths, polls):
        """Every line of slot S's stream files, in the order stored: lines received before S build each market's
        next book; from S to S + 900 they run the day; later lines belong to the next slot's file. `polls`: a deque
        of the day's served polls (recv_ns, condition id, row) in order, consumed from the front."""
        S_ns, E_ns = S * S_NS, (S + SLOT) * S_NS
        switched = False
        for M in self.mk:
            M.shadow = None
        for path in paths:
            with gzip.open(path, "rt", encoding="utf-8") as fh:
                for line in fh:
                    self.c["lines"] += 1
                    mt = PC_LINE.fullmatch(line)
                    if mt is not None:
                        g = mt.groups()
                        h = int(g[0])
                        if h >= E_ns:
                            continue
                        shadow = h < S_ns
                        switched = self.at_host(h, shadow, switched, S_ns, polls)
                        self.c["frames"] += 1
                        self.c["fast"] += 1
                        tm = self.pc_fast(g, shadow)
                        if tm is not None:
                            self.after(tm, h)
                        continue
                    if not line.strip():
                        continue
                    o = json.loads(line)
                    h = o.get("recv_ns")
                    assert type(h) is int, "a line without its host receipt"
                    if h >= E_ns:
                        continue
                    shadow = h < S_ns
                    switched = self.at_host(h, shadow, switched, S_ns, polls)
                    if "event" in o:
                        ev = o["event"]
                        if ev in ("connect", "subscribe", "close"):
                            if shadow:
                                if ev != "close":
                                    for M in self.mk:
                                        M.shadow = [{}, {}, False]
                            else:
                                self.session(ev, h, o.get("reason"))
                        continue
                    raw = o.get("raw")
                    if raw is None or raw == "PONG":
                        self.c["skipped"] += 1
                        continue
                    try:
                        fr = json.loads(raw)
                    except ValueError:
                        self.c["skipped"] += 1
                        continue
                    self.c["frames"] += 1
                    touched = self.frame_items(fr, h, shadow)
                    if not shadow:
                        for tm in touched:
                            self.after(tm, h)
        if not switched:
            self.switch(S_ns)
        while polls and polls[0][0] < E_ns:
            t, cid, row = polls.popleft()
            self.poll(t, cid, row)

    def finish(self, end_ns, outcomes):
        """The day's end: every event and reward integrated to it, every position valued at the market's last
        midpoint of the day - or at its outcome, where `outcomes` holds one (thousandths a share of the first token)
        - or, where the market never showed a two-sided book, by liquidation into the book as it stands."""
        rows = []
        for M in self.mk:
            if M.block:
                self.close_block(M, False)
            self.resolve(M, end_ns)
            self.integrate(M, end_ns)
            for mv in M.mvs:
                self.flush(M, mv)
            mark = outcomes.get(M.cid)
            how = "outcome"
            if mark is None and M.lastmid is not None:
                mark, how = Fr(M.lastmid, 2), "mid"
            for mv in M.mvs:
                if mark is not None:
                    val = mv.x * Fr(mark)
                else:
                    val, how = Fr(M.liquidation(mv.x)), "book"
                reb = sum((M.fee * f * p * (PRICE_UNIT - p) for _vt, _sd, p, f, _k in mv.fills), Fr(0)) \
                    / (SIZE_UNIT * PRICE_UNIT * PRICE_UNIT)
                pnl = (val - mv.cost) / (SIZE_UNIT * PRICE_UNIT)
                rows.append({"cid": M.cid, "variant": mv.sp.name, "rew": mv.rew, "reb": reb, "pnl": pnl, "x": mv.x,
                             "cost": mv.cost, "mark": how, "fills": len(mv.fills),
                             "fill_hu": sum(f for _a, _b, _c, f, _d in mv.fills),
                             "crossed_hu": sum(f for _a, _b, _c, f, k in mv.fills if k == "x"),
                             "scored_ns": mv.scored_ns, "n": dict(mv.n)})
        return rows

# ---- the set: the candidate days in order, each a member or not by TZ-41 section 1's rules --------------------------

RESCORE_SLOTS = 24           # the rescore replays the set's first day's first 24 slots (TZ-41 section 4.4)
DAY_FILE_KEYS = ("cid", "variant", "rew", "reb", "pnl", "x", "cost", "mark", "fills", "fill_hu", "crossed_hu",
                 "scored_ns", "n")


def fr_text(x):
    x = Fr(x)
    return "%d/%d" % (x.numerator, x.denominator)


def fr_of(s):
    n, d = s.split("/")
    return Fr(int(n), int(d))


def wait_archive(d0, t_start, clock=None, sleep=None, read=None):
    """Until the reward book archive's assets reach the last slot of day d0: its ledger read again every 60 s,
    BLOCKED once WAIT_MAX_S have passed since `t_start`. Returns the asset map."""
    clock, sleep, read = clock or time.time, sleep or time.sleep, read or archived_to
    amap, last = read()
    said = None
    need = d0 + DAY - SLOT
    while last < need:
        now = clock()
        assert now - t_start <= WAIT_MAX_S, "BLOCKED: the archive's assets reach slot %d, below %d, at %s" % (
            last, need, utc(now))
        if said is None or now - said >= 1800:
            out("the archive's assets reach slot %d (%s); day %d needs %d; its ledger read again every 60 s" % (
                last, utc(last) if last else "-", d0, need))
            said = now
        sleep(60)
        amap, last = read()
    return amap


def day_verdict(d0, amap, root=None):
    """One candidate day: (None, its record, its polls) where it is a member, else (the first reason it is not,
    None, None) - no selection; a slot without its records or failing a rule, the first such slot named."""
    sel = selection_of(d0, root)
    if sel is None:
        return "no selection", None, None
    members = members_of(sel)
    if not members:
        return "a selection of no market", None, None
    recs = slot_records(d0, root)
    slots = []
    for S in range(d0, d0 + DAY, SLOT):
        why = slot_problem(S, recs.get(S, []), sel["sha256"], len(members), amap, d0)
        if why is not None:
            return "slot %d (%s): %s" % (S, utc(S), why), None, None
        files = []
        for sj in recs[S]:
            a = amap[(d0, sj["stream"]["file"])]
            files.append({"file": sj["stream"]["file"], "tag": a["tag"], "asset": a["asset"], "bytes": a["bytes"],
                          "sha256": a["sha256"]})
        slots.append({"S": S, "files": files})
    polls, counts = polls_of(d0, {S: recs[S] for S in range(d0, d0 + DAY, SLOT)}, root)
    rec = {"d0": d0, "selection": {"attempt": sel["attempt"], "sha256": sel["sha256"], "members": len(members)},
           "members": [dict(m, rate=fr_text(m["rate"]), fee=fr_text(m["fee"])) for m in members], "slots": slots,
           "polls": {"n": len(polls), "polls": counts["polls"], "unserved": counts["unserved"],
                     "no_row": counts["no row"]}}
    return None, rec, polls


def polls_text(polls):
    return "".join(json.dumps([t, cid, None if row is None else [fr_text(row[0]), fr_text(row[1])]],
                              separators=(",", ":")) + "\n" for t, cid, row in polls)


class PollFile:
    """A member day's polls file read in order, one line at a time: the front poll as `[0]`, `popleft()`, truth while
    a poll is left, and iteration over the rest - a deque's interface, so that a day's polls are never all held."""

    def __init__(self, path):
        self.fh = open(path, encoding="utf-8")
        self.head = None
        self._advance()

    def _advance(self):
        ln = self.fh.readline() if self.fh is not None else ""
        if not ln:
            self.head = None
            if self.fh is not None:
                self.fh.close()
                self.fh = None
            return
        t, cid, row = json.loads(ln)
        self.head = (t, sys.intern(cid), None if row is None else (fr_of(row[0]), fr_of(row[1])))

    def __bool__(self):
        return self.head is not None

    def __getitem__(self, i):
        assert i == 0 and self.head is not None, "PollFile: only the front poll"
        return self.head

    def popleft(self):
        assert self.head is not None, "PollFile: no poll left"
        h = self.head
        self._advance()
        return h

    def __iter__(self):
        while self.head is not None:
            yield self.popleft()


def polls_read(path):
    return PollFile(path)


def members_read(rec):
    return [dict(m, rate=fr_of(m["rate"]), fee=fr_of(m["fee"])) for m in rec["members"]]


def gamma_get(query, tries=DL_TRIES, sleep=None):
    sleep = sleep or time.sleep
    url = GAMMA_URL % query
    last = None
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers=GAMMA_HEADERS, method="GET")
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
                assert r.status == 200, "HTTP %d" % r.status
            return json.loads(body, parse_float=D), len(body), sha256_bytes(body), k
        except urllib.error.HTTPError as e:
            last = "HTTP %d" % e.code
            if e.code not in (429, 500, 502, 503, 504):
                break
        except (urllib.error.URLError, http.client.HTTPException, TimeoutError, ConnectionError, OSError,
                ValueError) as e:
            last = "%s %s" % (type(e).__name__, e)
        sleep(min(60.0, 5.0 * 2 ** k))
    raise AssertionError("BLOCKED: gamma %s: %d attempts, the last %s" % (query[:80], tries, last))


def outcome_of(doc, tok):
    """The first token's outcome in thousandths, 1000 or 0, where the document reads the market closed with prices of
    exactly 0 and 1; otherwise None."""
    if doc.get("closed") is not True:
        return None
    try:
        prices, toks = json.loads(doc.get("outcomePrices")), json.loads(doc.get("clobTokenIds"))
    except (TypeError, ValueError):
        return None
    if sorted(map(str, prices)) != ["0", "1"] or len(toks) != 2 or tok not in toks:
        return None
    return PRICE_UNIT if str(prices[toks.index(tok)]) == "1" else 0


def documents(toks, holdf=None, get=None):
    """Every member's gamma document, read open and closed, DOC_CHUNK condition ids a request, each request held to
    the idle stretch; each member's document found exactly once, and only its outcome kept. Returns ({cid: outcome},
    requests)."""
    holdf, get = holdf or hold, get or gamma_get
    cids = sorted(toks)
    found, reqs = {}, []
    for i in range(0, len(cids), DOC_CHUNK):
        chunk = cids[i:i + DOC_CHUNK]
        for closed in (False, True):
            q = [("limit", 2 * DOC_CHUNK)] + [("condition_ids", c) for c in chunk] + (
                [("closed", "true")] if closed else [])
            holdf(DOC_BUDGET_S)
            docs, n, sha, k = get(urllib.parse.urlencode(q))
            assert isinstance(docs, list) and len(docs) <= len(chunk), "gamma: %d documents for %d ids" % (
                len(docs), len(chunk))
            reqs.append({"ids": len(chunk), "closed": closed, "bytes": n, "sha256": sha, "docs": len(docs),
                         "retries": k})
            for d in docs:
                cid = d.get("conditionId")
                assert cid in toks and cid not in found, "gamma: a document of %r" % cid
                found[cid] = outcome_of(d, toks[cid])
            del docs
    missing = sorted(set(cids) - set(found))
    assert not missing, "BLOCKED: no gamma document of %d members: %s" % (len(missing), missing[:3])
    return {c: found[c] for c in cids}, reqs


def mode_fetch():
    """The set (TZ-41 section 3.6): the candidate days in order from FIRST_D0, each read from the reward book's store
    and the archive's record once the archive has moved it, until NEED members; the members' documents; every
    candidate disclosed."""
    floor_check()
    os.makedirs(os.path.join(WORK, "fetch"), exist_ok=True)
    sp = os.path.join(WORK, "set.json")
    if os.path.exists(sp):
        s = load_json(sp)
        for d0 in s["members"]:
            got = sha256_file(os.path.join(WORK, "fetch", "%d.json" % d0))
            assert got == s["days"][str(d0)]["sha256"], "the set's day %d differs from its record" % d0
        out("the set is on disk: %s sha256 %s, %d members, every day's record unchanged" % (
            sp, sha256_file(sp), len(s["members"])))
        return
    assert time.time() >= FIRST_D0 + NEED * DAY, "BLOCKED: before the eighth candidate day has ended"
    t_start = time.time()
    considered, member_days, days = [], [], {}
    d0 = FIRST_D0
    while len(member_days) < NEED:
        assert d0 <= LAST_D0, "BLOCKED: %d non-member days before the eighth member, the bound %d" % (
            len(considered) - len(member_days), NONMEMBER_MAX)
        assert time.time() >= d0 + DAY, "BLOCKED: day %d (%s) has not ended; the set needs it" % (d0, utc(d0))
        amap = wait_archive(d0, t_start)
        hold(STORE_BUDGET_S)
        why, rec, polls = day_verdict(d0, amap)
        considered.append({"d0": d0, "member": why is None, "reason": why})
        if why is None:
            ptxt = polls_text(polls).encode("utf-8")
            rec["polls"]["sha256"] = write_once(os.path.join(WORK, "fetch", "%d.polls.jsonl" % d0), ptxt)
            body = dumps(rec).encode("utf-8")
            days[str(d0)] = {"sha256": write_once(os.path.join(WORK, "fetch", "%d.json" % d0), body),
                             "bytes": sum(f["bytes"] for s in rec["slots"] for f in s["files"]),
                             "files": sum(len(s["files"]) for s in rec["slots"]),
                             "members": len(rec["members"])}
            member_days.append(d0)
            out("candidate %d (%s): MEMBER %d of %d - %d markets, %d slots, %d stream files, %d bytes; polls %d "
                "served of %d, %d without a row" % (
                    d0, utc(d0), len(member_days), NEED, len(rec["members"]), len(rec["slots"]), days[str(d0)]["files"],
                    days[str(d0)]["bytes"], rec["polls"]["n"], rec["polls"]["polls"], rec["polls"]["no_row"]))
        else:
            out("candidate %d (%s): not a member - %s" % (d0, utc(d0), why))
        rec = polls = ptxt = body = None    # one day's polls held at a time
        d0 += DAY
    toks = {}
    for d in member_days:
        for m in load_json(os.path.join(WORK, "fetch", "%d.json" % d))["members"]:
            assert toks.get(m["cid"], m["tok"]) == m["tok"], "%s: two first tokens" % m["cid"]
            toks[m["cid"]] = m["tok"]
    outcomes, reqs = documents(toks)
    for r in reqs:
        out("gamma request: %d ids, closed %s, %d documents, %d bytes, sha256 %s, retries %d" % (
            r["ids"], r["closed"], r["docs"], r["bytes"], r["sha256"], r["retries"]))
    s = {"first_d0": FIRST_D0, "need": NEED, "considered": considered, "members": member_days, "days": days,
         "markets": len(toks), "outcomes": {c: v for c, v in sorted(outcomes.items()) if v is not None},
         "requests": reqs}
    sha = write_once(sp, dumps(s).encode("utf-8"))
    out("G-SET PASS: %d members of %d candidates considered, %d to %d; %d distinct markets, %d resolved by their "
        "documents; %d stream files, %d bytes; set.json sha256 %s" % (
            len(member_days), len(considered), member_days[0], member_days[-1], len(toks), len(s["outcomes"]),
            sum(v["files"] for v in days.values()), sum(v["bytes"] for v in days.values()), sha))


def day_inputs(d0):
    """A member day's record and its polls, the polls file asserted by the SHA-256 its record carries."""
    rec = load_json(os.path.join(WORK, "fetch", "%d.json" % d0))
    path = os.path.join(WORK, "fetch", "%d.polls.jsonl" % d0)
    assert sha256_file(path) == rec["polls"]["sha256"], "day %d: its polls differ from its record" % d0
    return rec, polls_read(path)


def the_set():
    s = load_json(os.path.join(WORK, "set.json"))
    assert len(s["members"]) == NEED, "the set holds %d members" % len(s["members"])
    for d0 in s["members"]:
        got = sha256_file(os.path.join(WORK, "fetch", "%d.json" % d0))
        assert got == s["days"][str(d0)]["sha256"], "the set's day %d differs from its record" % d0
    return s

# ---- downloads: one Release asset, by its tag and name, verified by its bytes and SHA-256 ----------------------


def download(tag, asset, nbytes, sha, dest, url_of=None, tries=DL_TRIES, sleep=None):
    sleep = sleep or time.sleep
    url = (url_of or (lambda t, a: DL_URL % (urllib.parse.quote(t), urllib.parse.quote(a))))(tag, asset)
    last = None
    for k in range(tries):
        t0 = time.time()
        try:
            req = urllib.request.Request(url, headers=DL_HEADERS, method="GET")
            h, n = hashlib.sha256(), 0
            with urllib.request.urlopen(req, timeout=120) as r, open(dest + ".part", "wb") as fh:
                assert r.status == 200, "HTTP %d" % r.status
                while True:
                    b = r.read(1 << 20)
                    if not b:
                        break
                    h.update(b)
                    fh.write(b)
                    n += len(b)
            if n == nbytes and h.hexdigest() == sha:
                os.replace(dest + ".part", dest)
                return n, time.time() - t0, k
            last = "%d bytes sha256 %s, the set's %d %s" % (n, h.hexdigest(), nbytes, sha)
        except urllib.error.HTTPError as e:
            last = "HTTP %d" % e.code
            if e.code not in (403, 404, 429, 500, 502, 503, 504):
                break
        except (urllib.error.URLError, http.client.HTTPException, TimeoutError, ConnectionError, OSError) as e:
            last = "%s %s" % (type(e).__name__, e)
        if os.path.exists(dest + ".part"):
            os.remove(dest + ".part")
        sleep(min(60.0, 5.0 * 2 ** k))
    raise AssertionError("BLOCKED: %s/%s: %d attempts, the last %s" % (tag, asset, tries, last))

# ---- units: one slot held to the idle stretch, its streams downloaded, replayed and removed -------------------------


def run_unit(S, files, dl_dir, feed, timing, holdf=None, dl=None):
    """One slot: started where `holdf` allows, its stream files downloaded in index order and verified by bytes and
    SHA-256, fed to the day by `feed(paths)`, and removed whatever the replay did; its record appended to `timing`."""
    holdf, dl = holdf or hold, dl or download
    nbytes = sum(f["bytes"] for f in files)
    budget = 5 + -(-nbytes // DL_RATE) + UNIT_BUDGET_S
    start, waited = holdf(budget)
    free = free_bytes()
    assert free - nbytes >= DISK_FLOOR, "BLOCKED: %d bytes free, %d to download, the floor %d" % (
        free, nbytes, DISK_FLOOR)
    os.makedirs(dl_dir, exist_ok=True)
    paths, retries = [], 0
    t0 = time.time()
    try:
        for f in sorted(files, key=lambda f: int(SLOT_FILE_RE.fullmatch(f["file"]).group(2))):
            dest = os.path.join(dl_dir, f["asset"])
            _n, _secs, k = dl(f["tag"], f["asset"], f["bytes"], f["sha256"], dest)
            retries += k
            paths.append(dest)
        t1, c1 = time.time(), time.process_time()
        feed(paths)
        cpu = time.process_time() - c1
    finally:
        for p in paths:
            if os.path.exists(p):
                os.remove(p)
    end = time.time()
    W = int(start) // SLOT * SLOT
    rec = {"S": S, "window": W, "start_second": round(start - W, 3), "end_second": round(end - W, 3),
           "waited_s": round(waited, 3), "download_s": round(t1 - t0, 3), "replay_s": round(end - t1, 3),
           "cpu_s": round(cpu, 3), "bytes": nbytes, "retries": retries, "budget_s": budget,
           "inside": end <= W + IDLE[1]}
    with open(timing, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, sort_keys=True) + "\n")
    return rec


def timing_summary(path):
    recs = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            recs = [json.loads(ln) for ln in fh if ln.strip()]
    outside = [r for r in recs if not r["inside"]]
    if recs:
        out("units %d: inside the idle stretch %d, ending after second %d %d; longest %.1f s, download %.1f s and "
            "replay %.1f s at most; %.0f s waited; processor %.1f s; %d bytes downloaded; retries %d; windows %s to "
            "%s" % (len(recs), len(recs) - len(outside), IDLE[1], len(outside),
                    max(r["end_second"] - r["start_second"] for r in recs), max(r["download_s"] for r in recs),
                    max(r["replay_s"] for r in recs), sum(r["waited_s"] for r in recs),
                    sum(r["cpu_s"] for r in recs), sum(r["bytes"] for r in recs), sum(r["retries"] for r in recs),
                    utc(min(r["window"] for r in recs)), utc(max(r["window"] for r in recs))))
    for r in outside:
        out("unit %d started at second %.1f of window %d and ended at second %.1f" % (
            r["S"], r["start_second"], r["window"], r["end_second"]))
    return recs, outside


def slot_line(day, S):
    """A slot's record once the day has run to its end: the stream's counts, and each variant's sums over the
    members with a SHA-256 of every member's state - its position, cost, fills and reward."""
    c = day.c
    parts = ["%d lines %d frames %d fast %d skipped %d polls %d subscribes %d closes %d" % (
        S, c["lines"], c["frames"], c["fast"], c["skipped"], c["polls"], c["subscribes"], c["closes"])]
    for M in day.mk:
        for mv in M.mvs:
            day.flush(M, mv)
    for vi, sp in enumerate(day.specs):
        h = hashlib.sha256()
        nf = fhu = x = cost = 0
        rew = D(0)
        for M in day.mk:
            mv = M.mvs[vi]
            h.update(("%s %d %d %d %s\n" % (M.cid, mv.x, mv.cost, len(mv.fills), format(mv.rew, "f"))).encode())
            nf += len(mv.fills)
            fhu += sum(f for _a, _b, _c, f, _d in mv.fills)
            x += mv.x
            cost += mv.cost
            rew = C50.add(rew, mv.rew)
        parts.append("%s fills %d hu %d x %d cost %d rew %s state %s" % (sp.name, nf, fhu, x, cost, format(rew, "f"),
                                                                        h.hexdigest()[:16]))
    return " | ".join(parts)


def book_counts(day):
    book = {k: sum(M.c[k] for M in day.mk) for k in ("snapshots", "touch_equal", "book_equal", "matches")}
    book.update(subscribes=day.c["subscribes"], closes=day.c["closes"])
    return book


def day_rows_text(d0, rows, day):
    book = book_counts(day)
    doc = {"d0": d0, "counts": dict(day.c), "book": book,
           "rows": [{k: (format(r[k], "f") if k == "rew" else fr_text(r[k]) if k in ("reb", "pnl") else r[k])
                     for k in DAY_FILE_KEYS} for r in rows]}
    return dumps(doc).encode("utf-8")


def replay_day(d0, rec, polls, outcomes, dl_dir, timing, slots=None, holdf=None, dl=None, on_unit=None):
    """One member day replayed slot by slot; returns its slot lines and, where every slot ran, its rows."""
    day = Day(d0, members_read(rec))
    lines = []
    for s in rec["slots"][:slots]:
        u = run_unit(s["S"], s["files"], dl_dir, lambda paths, S=s["S"]: day.feed_slot(S, paths, polls), timing,
                     holdf, dl)
        lines.append(slot_line(day, s["S"]))
        if on_unit is not None:
            on_unit(u)
    if slots is not None and slots < len(rec["slots"]):
        return lines, None, day
    return lines, day.finish((d0 + DAY) * S_NS, {c: v for c, v in outcomes.items()}), day


class Projection:
    """After the first `after` units of this run, the replays' processor time projected over `total` bytes,
    BLOCKED above `cpu_max`."""

    def __init__(self, total, cpu_max, after=PROJECT_AFTER):
        self.total, self.cpu_max, self.after = total, cpu_max, after
        self.n, self.cpu, self.nb = 0, 0.0, 0

    def __call__(self, u):
        self.n += 1
        self.cpu += u["cpu_s"]
        self.nb += u["bytes"]
        if self.n == self.after:
            proj = self.cpu / self.nb * self.total
            out("projected %.0f s of replay for %d bytes after %d units at %.4f s a megabyte" % (
                proj, self.total, self.n, self.cpu / self.nb * 1e6))
            assert proj <= self.cpu_max, "BLOCKED: replay projected at %.0f s, above %d" % (proj, self.cpu_max)


def mode_replay():
    """Every member day not yet on disk, slot by slot (TZ-41 section 3.7); then G-BOOK over the days on disk."""
    floor_check()
    s = the_set()
    ddir = os.path.join(WORK, "days")
    os.makedirs(ddir, exist_ok=True)
    timing = os.path.join(WORK, "timing-replay.jsonl")
    todo = [d0 for d0 in s["members"] if not os.path.exists(os.path.join(ddir, "%d.json" % d0))]
    total = sum(s["days"][str(d0)]["bytes"] for d0 in todo)
    out("days to replay %d of %d, %d bytes of streams" % (len(todo), NEED, total))
    proj = Projection(total, REPLAY_CPU_MAX)
    for d0 in todo:
        rec, polls = day_inputs(d0)
        t0 = time.time()
        lines, rows, day = replay_day(d0, rec, polls, s["outcomes"], os.path.join(WORK, "dl"), timing, on_unit=proj)
        assert all(t >= (d0 + DAY) * S_NS for t, _c, _r in polls), "day %d: a poll left before its end" % d0
        st = write_once(os.path.join(ddir, "%d.slots.txt" % d0), ("\n".join(lines) + "\n").encode("utf-8"))
        sd = write_once(os.path.join(ddir, "%d.json" % d0), day_rows_text(d0, rows, day))
        out("day %d (%s) replayed in %.0f s: %d slots, %d lines; slots sha256 %s, day sha256 %s" % (
            d0, utc(d0), time.time() - t0, len(lines), day.c["lines"], st, sd))
        rec = polls = lines = rows = day = None    # one day held at a time
    timing_summary(timing)
    g_book(s)


def g_book(s):
    tot = collections.Counter()
    for d0 in s["members"]:
        b = load_json(os.path.join(WORK, "days", "%d.json" % d0))["book"]
        tot.update(b)
        out("day %d: book frames %d, the rebuilt touch equal at %d, every level equal at %d; matches %d; "
            "subscribes %d, closes %d" % (d0, b["snapshots"], b["touch_equal"], b["book_equal"], b["matches"],
                                          b["subscribes"], b["closes"]))
    ok = tot["snapshots"] > 0 and Fr(tot["touch_equal"], tot["snapshots"]) >= BOOK_EQUAL_MIN
    out("G-BOOK %s: the rebuilt touch equal to the venue's book frame at %d of %d frames, at least %s required; "
        "barred: every level equal at %d" % ("PASS" if ok else "FAIL", tot["touch_equal"], tot["snapshots"],
                                            BOOK_EQUAL_MIN, tot["book_equal"]))
    return ok


def mode_rescore():
    """DETERMINISM (TZ-41 section 4.4): the set's first day's first RESCORE_SLOTS slots replayed again from a second
    download; their lines equal the replay's."""
    floor_check()
    s = the_set()
    d0 = s["members"][0]
    with open(os.path.join(WORK, "days", "%d.slots.txt" % d0), encoding="utf-8") as fh:
        first = fh.read().split("\n")[:RESCORE_SLOTS]
    rec, polls = day_inputs(d0)
    total = sum(f["bytes"] for sl in rec["slots"][:RESCORE_SLOTS] for f in sl["files"])
    proj = Projection(total, RESCORE_CPU_MAX, after=6)
    lines, _rows, _day = replay_day(d0, rec, polls, s["outcomes"], os.path.join(WORK, "dl"),
                                    os.path.join(WORK, "timing-rescore.jsonl"), slots=RESCORE_SLOTS, on_unit=proj)
    write_once(os.path.join(WORK, "rescore.txt"), ("\n".join(lines) + "\n").encode("utf-8"))
    same = sum(1 for a, b in zip(lines, first) if a == b)
    out("DETERMINISM %s: %d of %d slot lines of day %d equal to the replay's" % (
        "PASS" if same == RESCORE_SLOTS == len(lines) else "FAIL", same, RESCORE_SLOTS, d0))

# ---- the reading: each day's money by variant, and L0's reading (TZ-41 section 4.5) ---------------------------------


def day_money(rows, name):
    """A day's money for one variant: the reward with the venue's 1-pUSD minimum, the rebate and the marks.
    pess and central pay a member's reward only where it reaches 1 on the day, opt the day's sum where it reaches 1;
    pess counts no rebate."""
    rs = [r for r in rows if r["variant"] == name]
    rew = [D(r["rew"]) for r in rs]
    if name == "opt":
        tot = sum(rew, D(0))
        paid = tot if tot >= 1 else D(0)
    else:
        paid = sum((x for x in rew if x >= 1), D(0))
    reb = sum((fr_of(r["reb"]) for r in rs), Fr(0)) if name != "pess" else Fr(0)
    pnl = sum((fr_of(r["pnl"]) for r in rs), Fr(0))
    total = Fr(paid) + reb + pnl
    return {"reward": sum(rew, D(0)), "paid": paid, "rebate": reb, "marks": pnl, "total": total,
            "markets": len(rs), "paying": sum(1 for x in rew if x >= 1), "fills": sum(r["fills"] for r in rs),
            "shares": Fr(sum(r["fill_hu"] for r in rs), SIZE_UNIT),
            "crossed": Fr(sum(r["crossed_hu"] for r in rs), SIZE_UNIT),
            "scored_h": Fr(sum(r["scored_ns"] for r in rs), 3600 * S_NS),
            "marks_by": dict(collections.Counter(r["mark"] for r in rs))}


def l0_reading(pess_days, opt_days, theta=THETA):
    """EARN where every pess day reaches theta, NO EARN where no opt day does, UNDECIDABLE otherwise; each false
    reading at most 2^-8 over eight independent days (TZ-41 section 4.5). Pure."""
    assert len(pess_days) == len(opt_days) == NEED
    earn = all(t >= theta for t in pess_days)
    no_earn = all(t < theta for t in opt_days)
    word = "EARN" if earn and not no_earn else "NO EARN" if no_earn and not earn else "UNDECIDABLE"
    return word, earn, no_earn


def power(q, n=NEED):
    return Fr(q) ** n


def mode_score():
    floor_check()
    s = the_set()
    rows_by = {d0: load_json(os.path.join(WORK, "days", "%d.json" % d0))["rows"] for d0 in s["members"]}
    for name, q in (("0.90", Fr(9, 10)), ("0.95", Fr(19, 20)), ("0.99", Fr(99, 100))):
        out("power: every pess day at or above %s with probability %s each: %s" % (THETA, name, q12(power(q))))
    out("false reading: 2^-%d = %s for each answer, under independent days" % (NEED, q12(Fr(1, 2 ** NEED))))
    book = g_book(s)
    res = {"days": {}, "variants": {}}
    for d0 in s["members"]:
        res["days"][str(d0)] = {name: day_money(rows_by[d0], name) for name, *_r in VARIANTS}
        for name, *_r in VARIANTS:
            e = res["days"][str(d0)][name]
            out("day %d %-7s total %s = paid %s of reward %s on %d of %d markets + rebate %s + marks %s; fills %d, "
                "%s shares, %s against crossing orders; scored %s h; marks %s%s" % (
                    d0, name, q12(e["total"]), q12(e["paid"]), q12(e["reward"]), e["paying"], e["markets"],
                    q12(e["rebate"]), q12(e["marks"]), e["fills"], q12(e["shares"]), q12(e["crossed"]),
                    q12(e["scored_h"]), e["marks_by"], "" if name in GATED else ", barred"))
    pess = [res["days"][str(d0)]["pess"]["total"] for d0 in s["members"]]
    opt = [res["days"][str(d0)]["opt"]["total"] for d0 in s["members"]]
    word, earn, no_earn = l0_reading(pess, opt)
    out("pess days at or above %s: %d of %d, the least %s; opt days below it: %d of %d, the most %s" % (
        THETA, sum(1 for t in pess if t >= THETA), NEED, q12(min(pess)), sum(1 for t in opt if t < THETA), NEED,
        q12(max(opt))))
    for name, *_r in VARIANTS:
        tot = sum((res["days"][str(d0)][name]["total"] for d0 in s["members"]), Fr(0))
        res["variants"][name] = {"total": tot, "per_day": tot / NEED}
        out("%s: over the %d days %s, a day %s%s" % (name, NEED, q12(tot), q12(tot / NEED),
                                                     "" if name in GATED else ", barred"))
    res["reading"] = word if book else None
    res["g_book"] = "PASS" if book else "FAIL"
    sha = write_once(os.path.join(WORK, "reading.json"), dumps(res).encode("utf-8"))
    out("L0 %s: EARN %s, NO EARN %s; reading.json sha256 %s" % (word if book else "not read, G-BOOK FAIL", earn,
                                                               no_earn, sha))

# ---- G-REHEARSAL: four of the archive's first assets, replayed as one stand-in hour (TZ-41 section 4.1) ----------------


def rehearsal_members(path, params=REHEARSAL_PARAMS):
    """The markets of the first seed after the first subscribe of `path`, in order of first appearance, each with
    its first book item's token as its first token, under the rehearsal's fixed parameters."""
    seen, order = {}, []
    subscribed = False
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            o = json.loads(line)
            if o.get("event") == "subscribe":
                subscribed = True
                continue
            raw = o.get("raw")
            if not subscribed or raw is None or not raw.startswith("["):
                continue
            for it in json.loads(raw):
                if isinstance(it, dict) and it.get("event_type") == "book" and it.get("market") not in seen:
                    seen[it["market"]] = it["asset_id"]
                    order.append(it["market"])
            break
    assert order, "%s: no seed after a subscribe" % path
    return [{"cid": c, "tok": seen[c], "ms": params["ms"], "vu": params["vu"], "rate": params["rate"],
             "fee": params["fee"]} for c in order]


def compare_lines(rows, book):
    """The figures G-REHEARSAL and the self-test compare with the Architect's independent replay: per member and
    variant, in the members' order, every figure at twelve places or as an integer; then the book's counts."""
    lines = []
    for r in rows:
        n = r["n"]
        lines.append("%s %s rew %s reb %s pnl %s x %d cost %d fills %d hu %d crossed %d scored_ns %d sent %d "
                     "cancels %d refused %d crossings %d mark %s" % (
                         r["cid"], r["variant"], q12(r["rew"]), q12(r["reb"]), q12(r["pnl"]), r["x"], r["cost"],
                         r["fills"], r["fill_hu"], r["crossed_hu"], r["scored_ns"], n["sent"], n["cancels"],
                         n["refused"], n["crossings"], r["mark"]))
    lines.append("book snapshots %d touch_equal %d book_equal %d matches %d subscribes %d closes %d" % tuple(
        book[k] for k in ("snapshots", "touch_equal", "book_equal", "matches", "subscribes", "closes")))
    return lines


def replay_paths(d0, members, slot_paths, end_s, polls=None):
    """A stand-in day: every slot's local files, in order; its rows at end_s and the book's counts."""
    day = Day(d0, members)
    pq = collections.deque(polls or ())
    for S, paths in slot_paths:
        day.feed_slot(S, paths, pq)
    rows = day.finish(end_s * S_NS, {})
    return rows, book_counts(day), day


def mode_rehearse():
    floor_check()
    dl_dir = os.path.join(WORK, "rehearsal-dl")
    os.makedirs(dl_dir, exist_ok=True)
    timing = os.path.join(WORK, "timing-rehearsal.jsonl")
    paths, c0 = [], time.process_time()
    try:
        for name, nbytes, sha in REHEARSAL_ASSETS:
            dest = os.path.join(dl_dir, name)
            start, waited = hold(5 + -(-nbytes // DL_RATE) + 5)
            assert free_bytes() - nbytes >= DISK_FLOOR, "BLOCKED: the disk floor"
            n, secs, k = download(REHEARSAL_TAG, name, nbytes, sha, dest)
            out("downloaded %s: %d bytes in %.1f s, sha256 %s, retries %d, held %.0f s" % (name, n, secs, sha, k,
                                                                                          waited))
            paths.append(dest)
        members = rehearsal_members(paths[0])
        c1 = time.process_time()
        slots = [(int(ASSET_RE.fullmatch(p.rsplit("/", 1)[1]).group(3)), [p]) for p in paths]
        start, waited = hold(UNIT_BUDGET_S)
        rows, book, day = replay_paths(REHEARSAL_D0, members, slots, REHEARSAL_D0 + 4 * SLOT)
        cpu = time.process_time() - c1
        assert cpu <= REHEARSAL_CPU_MAX, "BLOCKED: the rehearsal's replay took %.0f s" % cpu
    finally:
        for p in paths:
            if os.path.exists(p):
                os.remove(p)
    lines = compare_lines(rows, book)
    body = ("\n".join(lines) + "\n").encode("utf-8")
    write_once(os.path.join(WORK, "rehearsal.txt"), body)
    out("rehearsal: %d markets, %d lines of stream, %.1f s of processor, held %.0f s; %d lines sha256 %s" % (
        len(members), day.c["lines"], cpu, waited, len(lines), sha256_bytes(body)))
    same = len(lines) == REF["lines"] and sha256_bytes(body) == REF["digest"]
    out("G-REHEARSAL %s: %d lines sha256 %s against the Architect's %d lines sha256 %s" % (
        "PASS" if same else "FAIL", len(lines), sha256_bytes(body), REF["lines"], REF["digest"]))

# ---- the session's modes ------------------------------------------------------------------------------------


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
        out("%-48s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"],
                         states["reported"]))


def number_reading(names, own):
    """NUMBER, CANON hard rule 2: CryptoTZ/ holds this TZ's file and no other of its number; CryptoReports/ no report
    of it. Pure."""
    tz = [n for n in names if n.startswith("CryptoTZ/" + NUMBER)]
    rp = [n for n in names if n.startswith("CryptoReports/" + NUMBER)]
    return tz == [own] and not rp, tz, rp


def mode_number():
    names = git("ls-tree", "--name-only", "origin/main", "--", "CryptoTZ/", "CryptoReports/", tree=PRIMARY).split("\n")
    head = git("rev-parse", "origin/main", tree=PRIMARY)
    ok, tz, rp = number_reading(names, "CryptoTZ/TZ-41-l0-our-quote.md")
    out("origin/main %s: %d paths under CryptoTZ/ and CryptoReports/; of the number %s: %s and %s" % (
        head, len(names), NUMBER, tz, rp))
    out("NUMBER %s" % ("PASS - 2 of 2" if ok else "FAIL"))
    assert ok, "BLOCKED: of the number %s, CryptoTZ/ holds %s and CryptoReports/ %s" % (NUMBER, tz, rp)


def still_reading(before, now, restarts):
    """G-STILL from two reads and the pair book archive's restart records between them, in order: PASS where every
    unit is unchanged, or where every unit but the pair book is unchanged and its change is that archive's own
    restarts alone - a chain from the recorded MainPID to the current one, NRestarts one higher at each, the unit
    active. Pure."""
    if now == before:
        return True, "unchanged"
    for k in sorted(now):
        if k != "pairbook" and now[k] != before.get(k):
            return False, "the %s changed" % k
    b, n = before["pairbook"], now["pairbook"]
    pid, count = b["MainPID"], int(b["NRestarts"])
    for r in restarts:
        if str(r.get("stopped")) != pid or str(r.get("NRestarts")) != str(count + 1):
            return False, "a restart record that does not follow %s at NRestarts %d: %r" % (pid, count, r)
        pid, count = str(r.get("pid")), count + 1
    if restarts and pid == n["MainPID"] and str(count) == n["NRestarts"] and n["ActiveState"] == "active":
        return True, "changed by the pair book archive's own restarts alone: %d" % len(restarts)
    return False, "the pair book changed, %d restart records of its archive since the first read" % len(restarts)


def mode_still():
    st = load_state()
    now = {}
    for key, unit in sorted(UNITS.items()):
        kv = show(unit, ["MainPID", "NRestarts", "ActiveState", "MemoryCurrent", "MemoryPeak"])
        now[key] = {k: kv[k] for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, MemoryCurrent %s, MemoryPeak %s" % (unit, now[key], kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    for key, (svc, timer) in sorted(ARCHIVES.items()):
        for unit in (timer, svc):
            out("%s %s" % (unit, show(unit, ["ActiveState", "SubState", "UnitFileState", "Result"])))
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "at_ns": time.time_ns(), "units": now}
        save_state(st)
        out("still: recorded")
        return
    _raw, recs, _tail = ledger_records(PB_LEDGER)
    since = st["still"]["at_ns"]
    restarts = [r for r in recs if r.get("event") == "restart" and r.get("wall_ns", 0) >= since]
    for r in restarts:
        out("the pair book archive's restart record %s: run %s, window %s, pid %s after %s, NRestarts %s" % (
            utc(r["wall_ns"] / 1e9), r.get("run"), r.get("W"), r.get("pid"), r.get("stopped"), r.get("NRestarts")))
    _raw, rrecs, _tail = ledger_records(RB_LEDGER)
    runs = sorted({r.get("run") for r in rrecs if r.get("wall_ns", 0) >= since and isinstance(r.get("run"), int)})
    out("the reward book archive's runs with records since the first read: %s" % runs)
    ok, why = still_reading(st["still"]["units"], now, restarts)
    out("G-STILL %s: %s since %s" % ("PASS" if ok else "FAIL", why, st["still"]["at"]))


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


def mode_archive():
    """The reward book archive's own record, read whole: its complete lines, its runs summarized, every complete
    run's set.json asserted by its set record's SHA-256, and the slots its assets reach."""
    svc, timer = ARCHIVES["rewardbook"]
    for unit in (timer, svc):
        out("%s %s" % (unit, show(unit, ["ActiveState", "SubState", "UnitFileState", "Result", "ExecMainStatus",
                                         "LastTriggerUSec", "NextElapseUSecRealtime"])))
    raw, recs, tail = ledger_records(RB_LEDGER)
    out("ledger %s: %d bytes sha256 %s, %d complete records, %d bytes of a line still written" % (
        RB_LEDGER, len(raw), sha256_bytes(raw), len(recs), len(tail)))
    for r in recs:
        out("L %s %s" % (utc(r["wall_ns"] / 1e9) if isinstance(r.get("wall_ns"), int) else "-",
                         json.dumps(r, sort_keys=True)))
    summ = ledger_summary(recs)
    for ln in summ["lines"]:
        out(ln)
    sets = archived_sets(recs)
    amap = asset_map(sets)
    for s in sets:
        ss = sorted(x["S"] for x in s["doc"]["assets"])
        out("set %s run %d sha256 %s: %d files, %d bytes, slots %s to %s" % (
            s["tag"], s["run"], s["sha256"], s["doc"]["assets_n"], s["doc"]["bytes_total"], ss[0] if ss else "-",
            ss[-1] if ss else "-"))
    slots = sorted({int(ASSET_RE.fullmatch(v["asset"]).group(3)) for v in amap.values()})
    after = [s for s in slots if s >= FIRST_D0]
    out("the archive's assets: %d files of %d slots, to slot %s; at or after %d: %d slots, to %s" % (
        len(amap), len(slots), slots[-1] if slots else "-", FIRST_D0, len(after), after[-1] if after else "-"))
    tags = sorted(ln.split("\t")[1][len("refs/tags/"):] for ln in git(
        "ls-remote", "origin", "refs/tags/rewardbook-streams-*", tree=PRIMARY).split("\n") if "\t" in ln)
    stags = [s["tag"] for s in sets]
    out("tags on origin %d: %s" % (len(tags), tags))
    out("complete runs' sets %d; their tags not on origin %s; halted %s; runs without a terminal record %s" % (
        len(stags), sorted(set(stags) - set(tags)), summ["halted"],
        [a for a, t in summ["terminal"].items() if not t]))
    assert REHEARSAL_TAG in stags, "BLOCKED: the rehearsal's set %s is not a complete run's" % REHEARSAL_TAG
    held = {(x["asset"], x["bytes"], x["sha256"]) for s in sets if s["tag"] == REHEARSAL_TAG
            for x in s["doc"]["assets"]}
    assert all(a in held for a in REHEARSAL_ASSETS), "BLOCKED: the rehearsal's assets differ from its set"
    out("the rehearsal's four assets are in set %s, bytes and SHA-256 equal" % REHEARSAL_TAG)


def report_tokens():
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8", errors="replace") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    return tree == WORK and (rel in ("state.json", "read-ledger.jsonl") or rel.startswith("logs/"))


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
            owner = [p for p, s, _a in procs if s - 1 <= b <= s + LIVE_S]
            assert not owner, "reclaim: %s belongs to the running process %s" % (t, owner)
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
        "forensic store %d -> %d files" % (considered, named, kept, copied, held, before, after))


def read_ledger(mode):
    """The read ledger: one line a mode that reads the store, the archive's Releases or the set, with this file's
    SHA-256 and the work tree's HEAD."""
    with open(os.path.join(HERE, PYFILE), "rb") as fh:
        mine = sha256_bytes(fh.read())
    head = git("rev-parse", "HEAD") if os.path.isdir(WT) else None
    rec = {"mode": mode, "at": utc(time.time()), "at_ns": time.time_ns(), "file_sha256": mine, "head": head}
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, sort_keys=True) + "\n")
    out("read ledger: %s" % json.dumps(rec, sort_keys=True))


def main(argv):
    if not argv:
        sys.exit("usage: %s MODE [ARG...]" % PYFILE)
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "number": mode_number, "selftest": mode_selftest,
             "still": mode_still, "archive": mode_archive, "rehearse": mode_rehearse, "fetch": mode_fetch,
             "replay": mode_replay, "rescore": mode_rescore, "score": mode_score}
    if mode in ("rehearse", "fetch", "replay", "rescore", "score"):
        read_ledger(mode)
    if mode == "reclaim":
        mode_reclaim(rest)
    elif mode == "scratch":
        assert len(rest) == 1, "scratch OWN"
        mode_scratch(rest[0])
    else:
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    out("malloc tuned: %s" % MALLOC_TUNED)
    out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
    out("opens refused: %d; reward book opens: %d" % (len(REFUSED), COUNTS["reward book opens"]))

# ---- the self-test: literals, a synthetic day and temporary trees under the work tree ------------------------------

SYN_D0 = 1792800000          # 2026-10-24 00:00:00 UTC: a synthetic day, two slots
SYN = {"A": {"cid": "0x" + "a1" * 32, "tok": "1001", "other": "1002", "ms": 2000, "vu": 90, "rate": Fr(100),
             "fee": Fr(1, 80)},
       "B": {"cid": "0x" + "b2" * 32, "tok": "2001", "other": "2002", "ms": 5000, "vu": 70, "rate": Fr(50),
             "fee": Fr(0)}}


def _side(levels):
    return [{"price": p, "size": s} for p, s in levels]


def _book(m, ts, bids, asks, tick="0.01", tok=None):
    return {"market": m["cid"], "asset_id": tok or m["tok"], "timestamp": str(ts), "hash": "ab" * 20,
            "bids": _side(bids), "asks": _side(asks), "tick_size": tick, "event_type": "book",
            "last_trade_price": "0.5"}


def _pc(m, ts, side, price, size):
    """A price_change frame of market m: the first token's entry and its mirror on the other token, in the venue's
    key order and separators."""
    mirror = format(D(1) - D(price), "f").rstrip("0").rstrip(".") if D(price) != 0 else "1"
    other = "SELL" if side == "BUY" else "BUY"
    return {"market": m["cid"], "price_changes": [
        {"asset_id": m["tok"], "price": price, "size": size, "side": side, "hash": "cd" * 20, "best_bid": "0.4",
         "best_ask": "0.46"},
        {"asset_id": m["other"], "price": mirror, "size": size, "side": other, "hash": "ef" * 20, "best_bid": "0.54",
         "best_ask": "0.6"}], "timestamp": str(ts), "event_type": "price_change"}


def _line(h, frame=None, event=None, **kw):
    if event is not None:
        return json.dumps(dict({"recv_ns": h, "mono_ns": h - 10 ** 9, "event": event}, **kw), separators=(",", ":"))
    raw = frame if isinstance(frame, str) else json.dumps(frame, separators=(", ", ":"))
    return json.dumps({"recv_ns": h, "mono_ns": h - 10 ** 9, "raw": raw}, separators=(",", ":"))


def synth_lines(S, first):
    """Slot S's synthetic stream (TZ-41 section 4.1): host instants in ms after S, venue stamps 20 ms before."""
    A, B = SYN["A"], SYN["B"]
    ms = lambda off: S * 1000 + off
    hn = lambda off: (S * 1000 + off) * MS_NS
    out_ = [_line(hn(-5000), event="connect", seg=0), _line(hn(-4900), event="open", seg=0),
            _line(hn(-4800), event="subscribe", seg=0, tokens=4)]
    if first:
        seed = [_book(A, ms(-4020), [("0.4", "100"), ("0.38", "500")], [("0.46", "100"), ("0.48", "300")]),
                _book(A, ms(-4020), [("0.52", "300")], [("0.6", "100")], tok=A["other"]),
                _book(B, ms(-4020), [("0.6", "200")], [("0.62", "200")]),
                _book(B, ms(-4020), [("0.38", "200")], [("0.4", "200")], tok=B["other"])]
        out_.append(_line(hn(-4000), seed))
        steps = [(1000, _pc(A, ms(1000), "BUY", "0.39", "50")),
                 (10000, _pc(A, ms(10000), "BUY", "0.4", "70")),
                 (10010, _book(A, ms(10000), [("0.4", "70"), ("0.39", "50"), ("0.38", "500")],
                               [("0.46", "100"), ("0.48", "300")])),
                 (10011, _book(A, ms(10000), [("0.52", "300")], [("0.6", "70")], tok=A["other"])),
                 (10020, {"market": A["cid"], "asset_id": A["tok"], "price": "0.4", "size": "30", "fee_rate_bps": "0",
                          "side": "SELL", "timestamp": str(ms(10000)), "event_type": "last_trade_price"}),
                 (20000, _pc(A, ms(20000), "SELL", "0.47", "10")),
                 (30000, _pc(A, ms(30000), "SELL", "0.41", "50")),
                 (40000, _pc(A, ms(40000), "SELL", "0.41", "0")),
                 (50000, _pc(A, ms(50000), "BUY", "0.45", "10")),
                 (60000, _pc(A, ms(60000), "BUY", "0.45", "0")),
                 (60050, _pc(A, ms(60050), "BUY", "0.45", "5")),
                 (60200, _pc(A, ms(60200), "BUY", "0.45", "0")),
                 (61000, _pc(B, ms(61000), "SELL", "0.62", "150")),
                 (62000, _pc(B, ms(62000), "SELL", "0.66", "100")),
                 (62100, _pc(B, ms(62100), "SELL", "0.62", "0"))]
        for off, fr in steps:
            out_.append(_line(hn(off + 20), fr))
        out_.append(_line(hn(70020), event="close", code=1006, reason="closed", seg=0))
        out_ += [_line(hn(71000), event="connect", seg=1), _line(hn(71100), event="open", seg=1),
                 _line(hn(71200), event="subscribe", seg=1, tokens=4)]
        out_.append(_line(hn(72000), [
            _book(A, ms(71980), [("0.4", "70"), ("0.39", "50"), ("0.38", "500")],
                  [("0.46", "100"), ("0.47", "10"), ("0.48", "300")]),
            _book(B, ms(71980), [("0.6", "200")], [("0.66", "100")])]))
        out_.append(_line(hn(80020), "PONG"))
        out_.append(_line(hn(100020), _pc(B, ms(100000), "SELL", "0.65", "30")))
        out_.append(_line(hn(110020), _pc(B, ms(110000), "SELL", "0.65", "0")))
        out_.append(_line(hn(110030), _book(B, ms(110000), [("0.6", "200")], [("0.66", "100")])))
        out_.append(_line(hn(900500), _pc(A, ms(900480), "BUY", "0.4", "999")))
        out_.append(_line(hn(905000), event="close", code=1000, reason="end", seg=1))
    else:
        out_.append(_line(hn(-4000), [
            _book(A, ms(-4020), [("0.4", "80"), ("0.39", "50"), ("0.38", "500")],
                  [("0.46", "100"), ("0.47", "10"), ("0.48", "300")]),
            _book(B, ms(-4020), [("0.6", "200")], [("0.66", "100")])]))
        out_.append(_line(hn(-2000), _pc(A, ms(-2020), "BUY", "0.4", "90")))
        steps = [(20, _pc(A, ms(20), "BUY", "0.4", "85")),
                 (300000, {"market": A["cid"], "asset_id": A["tok"], "old_tick_size": "0.01",
                           "new_tick_size": "0.001", "timestamp": str(ms(300000)), "event_type": "tick_size_change"}),
                 (300100, _pc(A, ms(300100), "BUY", "0.39", "60")),
                 (600000, _pc(B, ms(600000), "BUY", "0.59", "40")),
                 (700000, _pc(B, ms(700000), "BUY", "0.63", "20"))]
        for off, fr in steps:
            out_.append(_line(hn(off + 20), fr))
        out_.append(_line(hn(905000), event="close", code=1000, reason="end", seg=0))
    return out_


def synth_day(dirpath, d0=SYN_D0, slow=False):
    """The synthetic day's two stream files under `dirpath`; with `slow`, every line written with a space after
    each colon, out of PC_LINE's reach, so that only the JSON path reads it."""
    paths = []
    for k, S in enumerate((d0, d0 + SLOT)):
        lines = synth_lines(S, k == 0)
        if slow:
            lines = [json.dumps(json.loads(ln), separators=(", ", ": ")) for ln in lines]
        p = os.path.join(dirpath, "%d.0.stream.jsonl.gz" % S)
        with open(p, "wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=9, mtime=0) as fh:
            fh.write(("\n".join(lines) + "\n").encode("utf-8"))
        paths.append((S, [p]))
    return paths


def synth_polls(d0=SYN_D0):
    A, B = SYN["A"]["cid"], SYN["B"]["cid"]
    t = lambda s: (d0 + s) * S_NS
    return [(t(5), A, (Fr(100), Fr(2))), (t(35), B, (Fr(50), Fr(1, 2))), (t(65), A, None), (t(80), A, (Fr(120), Fr(3))),
            (t(930), A, (Fr(120), Fr(3))), (t(931), B, (Fr(50), Fr(1, 2)))]


def synth_members():
    return [{k: m[k] for k in ("cid", "tok", "ms", "vu", "rate", "fee")} for m in (SYN["A"], SYN["B"])]


# the Architect's reference over the synthetic day: its lines and their SHA-256 (TZ-41 section 4.1)
SYN_REF = {"lines": 7, "digest": "04e6917ef2efbe42590a82967ef4e590033adefef27d41b8a278021330bd157b"}


def mode_selftest():
    import http.server
    import threading
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    def fails(fn, exc=AssertionError):
        try:
            fn()
        except exc:
            return True
        return False

    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    # the constants
    ok(MALLOC_TUNED, "glibc took the 128 KiB mmap threshold and the two arenas")
    ok(utc(FIRST_D0) == "2026-10-31T00:00:00Z" and utc(LAST_D0) == "2026-11-13T00:00:00Z" and NEED == 8 and
       NONMEMBER_MAX == 6 and (LAST_D0 - FIRST_D0) // DAY + 1 == NEED + NONMEMBER_MAX,
       "candidates from 2026-10-31, at most 14 days to 2026-11-13, for 8 members")
    ok([v[0] for v in VARIANTS] == ["pess", "opt", "central"] and GATED == ("pess", "opt") and
       [s.name for s in SPECS] == ["pess", "opt", "central"] and all(s.L == 50 * MS_NS for s in SPECS) and
       (SPECS[0].front, SPECS[0].takers, SPECS[0].denom) == (False, True, "pess") and
       (SPECS[1].front, SPECS[1].takers, SPECS[1].denom) == (True, False, "opt") and
       (SPECS[2].front, SPECS[2].takers, SPECS[2].denom) == (False, True, "venue"),
       "three variants of one rule: pess behind and met by crossing orders, opt first and never, central the venue's")
    ok(THETA == D("10") and power(Fr(9, 10)) == Fr(43046721, 100000000) and
       q12(power(Fr(19, 20))) == "0.663420431289" and q12(power(Fr(99, 100))) == "0.922744694428" and
       Fr(1, 2 ** NEED) == Fr(1, 256) and Fr(1, 256) < Fr(5, 1000),
       "power 0.430467, 0.663420 and 0.922745 at 0.90, 0.95 and 0.99; each false reading 1/256, under 0.005")
    ok(DL_HEADERS == {"User-Agent": "btc-5m-twap-tz41", "Accept": "application/octet-stream"} and
       GAMMA_HEADERS == {"User-Agent": "btc-5m-twap-tz41", "Accept": "application/json"},
       "every request carries the TZ's two headers")
    lo = MEM_FLOOR - 1
    ok(MEM_FLOOR == 143592894 and memory_gate([MEM_FLOOR]) == (True, MEM_FLOOR) and
       memory_gate([lo, lo, MEM_FLOOR]) == (True, MEM_FLOOR) and memory_gate([lo] * 5) == (False, lo) and
       fails(lambda: memory_gate([MEM_FLOOR, lo])) and fails(lambda: memory_gate([lo] * 6)),
       "the memory gate: a read at the floor or above passes; below it the next read decides, five reads at most")
    reads, slept = iter([lo, lo - 7, MEM_FLOOR + 3, lo]), []
    floor_check(read=lambda: next(reads), sleep=slept.append, freef=lambda: DISK_GATE)
    reads2, slept2 = iter([lo] * 5), []
    ok(slept == [MEM_RETRY_S] * 2 and (MEM_RETRY_S, MEM_READS) == (60, 5) and
       fails(lambda: floor_check(read=lambda: next(reads2), sleep=slept2.append, freef=lambda: DISK_GATE)) and
       slept2 == [MEM_RETRY_S] * 4 and
       fails(lambda: floor_check(read=lambda: MEM_FLOOR, sleep=slept2.append, freef=lambda: DISK_GATE - 1)),
       "floor_check reads MemAvailable again every 60 s while below its floor, passes at the first read at it or "
       "above, BLOCKS where five reads are below; it BLOCKS below the disk gate")
    # the venue's numbers as exact integers
    ok([price_int(x) for x in ("0.5", "0.505", "1", "0", "0.07")] == [500, 505, 1000, 0, 70] and
       [size_int(x) for x in ("12.34", "5", "0.1", "1000000")] == [1234, 500, 10, 100000000],
       "prices in thousandths and sizes in hundredths, exactly")
    ok(all(fails(lambda t=t: price_int(t)) for t in ("0.5051", "1e-3", "-0.5", ".5", "0.5 ")) and
       all(fails(lambda t=t: size_int(t)) for t in ("1.234", "1e2", "-1", "")),
       "any other text of a price or a size is a failed assert")
    # the competitors' bounds against every split of the displayed sides among two and three makers
    def f12(a, b, inside):
        return 4 * max(3 * min(a, b), max(a, b)) if inside else 12 * min(a, b)
    worst = []
    for A_, B_ in ((4, 4), (3, 9), (12, 4), (6, 1), (0, 5), (8, 8)):
        for inside in (True, False):
            sums = set()
            for a1 in range(A_ + 1):
                for b1 in range(B_ + 1):
                    for a2 in range(A_ - a1 + 1):
                        for b2 in range(B_ - b1 + 1):
                            sums.add(f12(a1, b1, inside) + f12(a2, b2, inside) +
                                     f12(A_ - a1 - a2, B_ - b1 - b2, inside))
            hi, lo = envelope(A_, B_, inside)
            worst.append((max(sums) == hi, min(sums) == lo))
    ok(all(a and b for a, b in worst), "the competitors' most and least, x 12, equal the extremes over every split "
                                       "of six pairs of sides among three makers, inside [0.10, 0.90] and outside")
    # one share by hand: market A's book, our bid at 0.41 and ask at 0.45, 20 shares each
    m = Market(dict(SYN["A"]), SPECS)
    m.replace({400: 10000, 380: 50000}, {460: 10000, 480: 30000})
    m.seeded = True
    o_b, o_a = Order("b", 410, 2000), Order("a", 450, 2000)
    for mv in m.mvs:
        mv.resting = [o_b, o_a]
    dd = Day(SYN_D0, [])
    # mid 0.43; our distances 0.02, v 0.045: S = (25/45)^2; the book's 0.40 and 0.46 at 0.03: S = (15/45)^2
    sh = [Fr(*dd.share_of(m, mv, {})) for mv in m.mvs]
    q_ours = Fr(25, 45) ** 2 * 20
    A1 = B1 = Fr(15, 45) ** 2 * 100
    ok(sh[0] == q_ours / (q_ours + (2 * A1 + B1) / 3) and sh[1] == q_ours / (q_ours + (A1 + B1) / 4) and
       sh[2] == sh[0], "a share by hand: ours 20 (5/9)^2; the book's sides 100 (1/3)^2 each; pess against "
                       "(2A + B)/3, opt against (A + B)/4, the venue's before its first poll pess's")
    m.ven = ((Fr(2) * Fr(100) * m.vu * m.vu * SIZE_UNIT * 12).numerator, 1)
    sh = [Fr(*dd.share_of(m, mv, {})) for mv in m.mvs]
    ok(sh[0] == q_ours / (q_ours + 200) and sh[1] == q_ours / (q_ours + (A1 + B1) / 4) and
       sh[2] == q_ours / (q_ours + 200), "after a poll of competitiveness 2 at rate 100, the venue's 200: pess and "
                                          "central against it, opt against the book's least")
    # the synthetic day, against the Architect's reference and against its own rules by hand
    paths = synth_day(tmp)
    rows, book, day = replay_paths(SYN_D0, synth_members(), paths, SYN_D0 + 2 * SLOT, polls=synth_polls())
    lines = compare_lines(rows, book)
    body = ("\n".join(lines) + "\n").encode("utf-8")
    ok(len(lines) == SYN_REF["lines"] and sha256_bytes(body) == SYN_REF["digest"],
       "the synthetic day, %d lines, byte for byte the Architect's independent replay" % SYN_REF["lines"])
    f = {(M.cid[2:4], mv.sp.name): [(t // MS_NS - SYN_D0 * 1000, s, p, q, k) for t, s, p, q, k in mv.fills]
         for M in day.mk for mv in M.mvs}
    ok(f[("a1", "pess")] == [(10000, "b", 410, 2000, "m"), (50000, "a", 450, 1000, "x")] and
       f[("a1", "opt")] == [(10000, "b", 410, 2000, "m")] and f[("a1", "central")] == f[("a1", "pess")],
       "A: a sale of 30 at 0.40 fills our bid of 20 at 0.41, first; one minimum size long, no bid follows, so the ask "
       "placed at 0.41 meets none; a bid placed at 0.45 fills pess's and central's ask as a crossing order, never opt's")
    ok(f[("b2", "pess")] == f[("b2", "opt")] == [(110000, "a", 640, 3000, "m")],
       "B: once a 0.65 ask narrows the touch to five ticks and moves our ask to 0.64, a purchase of the 30 at 0.65 "
       "fills ours, 30 of 50")
    r = {(x["cid"][2:4], x["variant"]): x for x in rows}
    ok(r[("a1", "pess")]["n"]["refused"] == 1 and r[("a1", "opt")]["n"]["refused"] == 1 and
       r[("a1", "pess")]["x"] == 1000 and r[("a1", "pess")]["cost"] == 370000 and
       r[("a1", "pess")]["pnl"] == Fr(3, 5) and r[("a1", "pess")]["reb"] == Fr(73130, 80 * 10000),
       "A: an ask arriving after a bid of 0.45 came up is refused; pess long 10 at a cost of 3.70, marked at the "
       "day's last mid 0.43 for 0.60, its rebate 7.313 / 80")
    ok(r[("b2", "pess")]["pnl"] == Fr(-3, 20) and r[("b2", "pess")]["mark"] == "mid" and
       r[("a1", "pess")]["scored_ns"] == 1777770000000 and r[("a1", "opt")]["scored_ns"] == 1777720000000,
       "B: short 30 at 0.64 marked at 0.645; A scored 1,777.77 s of the 1,800 under pess and 1,777.72 under opt, "
       "unseeded from the close to the seed")
    ok(book == {"snapshots": 2, "touch_equal": 2, "book_equal": 2, "matches": 2, "subscribes": 1, "closes": 1} and
       day.c["polls"] == 6 and day.c["switches"] == 2 and day.c["skipped"] == 1,
       "2 book frames, both equal to the rebuilt book, 2 matches; 1 subscribe and 1 close inside the day, the "
       "slots' own before their instants not counted; 6 polls; the PONG skipped")
    slow = os.path.join(tmp, "slow")
    os.makedirs(slow)
    rows2, book2, day2 = replay_paths(SYN_D0, synth_members(), synth_day(slow, slow=True), SYN_D0 + 2 * SLOT,
                                      polls=synth_polls())
    ok(compare_lines(rows2, book2) == lines and day2.c["fast"] == 0 and day.c["fast"] == 19,
       "the same lines through the JSON path alone: the fast path read 19 frames, the slow 0")
    rows3, book3, _d3 = replay_paths(SYN_D0, synth_members(), paths, SYN_D0 + 2 * SLOT, polls=synth_polls())
    ok(compare_lines(rows3, book3) == lines, "a second replay of the same files: the same lines")
    # the day's money and L0's reading
    lit = [{"variant": v, "rew": "%s" % rw, "reb": "1/10", "pnl": "-1/2", "fills": 1, "fill_hu": 500,
            "crossed_hu": 0, "scored_ns": 3600 * S_NS, "mark": "mid", "cid": c}
           for v in ("pess", "opt", "central") for c, rw in (("x", "0.6"), ("y", "1.5"), ("z", "0.9"))]
    mp, mo, mc = (day_money(lit, v) for v in ("pess", "opt", "central"))
    ok(mp["total"] == Fr(3, 2) - Fr(3, 2) and mo["total"] == Fr(3) + Fr(3, 10) - Fr(3, 2) and
       mc["total"] == Fr(3, 2) + Fr(3, 10) - Fr(3, 2) and mp["paying"] == 1,
       "the 1-pUSD minimum: pess and central pay only a member's day at 1 or more, opt the day's sum; pess counts "
       "no rebate")
    T = THETA
    ok(l0_reading([T] * 8, [T] * 8) == ("EARN", True, False) and
       l0_reading([T] * 7 + [T - D("0.000001")], [T + 1] * 8) == ("UNDECIDABLE", False, False) and
       l0_reading([T - 1] * 8, [T - D("0.000001")] * 8) == ("NO EARN", False, True) and
       l0_reading([T] * 8, [T - 1] * 8) == ("UNDECIDABLE", True, True),
       "EARN at every pess day at 10 or more; NO EARN at every opt day below; both or neither UNDECIDABLE")
    # the slot rules
    good = {"S": SYN_D0, "index": 0, "day": SYN_D0, "selection": {"sha256": "s"}, "markets": 2, "error": None,
            "joined_late": False, "stream": {"opened": True, "off_reason": None, "file": "%d.0.stream.jsonl.gz" % SYN_D0,
                                             "cut": False, "max_gap_ns": GAP_MAX_NS, "subscribed_wall_ns":
                                                 SYN_D0 * S_NS - 1, "first_frame_wall_ns": SYN_D0 * S_NS,
                                             "last_frame_wall_ns": (SYN_D0 + SLOT) * S_NS}}
    am = {(SYN_D0, "%d.0.stream.jsonl.gz" % SYN_D0): {}}
    sp_ = lambda **kw: slot_problem(SYN_D0, [dict(good, **kw)], "s", 2, am, SYN_D0)
    st_ = lambda **kw: sp_(stream=dict(good["stream"], **kw))
    ok(sp_() is None and sp_(index=1) == "records: index 0" and sp_(markets=3) == "records: another selection" and
       sp_(error="x") == "records: an error" and st_(cut=True) == "stream: cut" and
       st_(max_gap_ns=GAP_MAX_NS + 1) == "stream: a gap above 15 s" and
       st_(subscribed_wall_ns=SYN_D0 * S_NS + 1) == "stream: subscribed late" and
       st_(last_frame_wall_ns=(SYN_D0 + SLOT) * S_NS - 1) == "stream: ended early" and
       slot_problem(SYN_D0, [good], "s", 2, {}, SYN_D0) == "stream: not archived" and
       slot_problem(SYN_D0, [], "s", 2, am, SYN_D0) == "no slot record",
       "a slot qualifies with its records whole, subscribed by S, to S + 900, no gap above 15 s, archived")
    g2 = dict(good, index=1, stream=dict(good["stream"], file="%d.1.stream.jsonl.gz" % SYN_D0,
                                          first_frame_wall_ns=(SYN_D0 + 20) * S_NS))
    g1 = dict(good, stream=dict(good["stream"], last_frame_wall_ns=(SYN_D0 + 4) * S_NS))
    am2 = dict(am)
    am2[(SYN_D0, "%d.1.stream.jsonl.gz" % SYN_D0)] = {}
    ok(slot_problem(SYN_D0, [g1, g2], "s", 2, am2, SYN_D0) == "stream: a gap above 15 s between files" and
       slot_problem(SYN_D0, [g1, dict(g2, stream=dict(g2["stream"], first_frame_wall_ns=(SYN_D0 + 19) * S_NS))],
                    "s", 2, am2, SYN_D0) is None, "two files: a gap above 15 s between them fails, 15 s does not")
    # the archive's record on a temporary tree
    state = os.path.join(tmp, "archive")
    os.makedirs(os.path.join(state, "runs", "1793263627"))
    doc = {"tag": "rewardbook-streams-1793263627", "assets_n": 1, "bytes_total": 7, "assets": [
        {"T": 1793232000, "S": 1793232000, "k": 0, "file": "1793232000.0.stream.jsonl.gz",
         "asset": "1793232000-1793232000.0.stream.jsonl.gz", "bytes": 7, "sha256": "aa" * 32}]}
    raw = json.dumps(doc).encode()
    with open(os.path.join(state, "runs", "1793263627", "set.json"), "wb") as fh:
        fh.write(raw)
    recs = [{"run": 1793263627, "event": "set", "sha256": sha256_bytes(raw), "tag": doc["tag"], "assets_n": 1,
             "bytes_total": 7, "wall_ns": 1}, {"run": 1793263627, "event": "complete", "wall_ns": 2},
            {"run": 1793300000, "event": "set", "sha256": "bb" * 32, "tag": "x", "assets_n": 0, "bytes_total": 0,
             "wall_ns": 3}]
    sets = archived_sets(recs, state)
    ok(len(sets) == 1 and asset_map(sets) == {(1793232000, "1793232000.0.stream.jsonl.gz"): {
        "tag": doc["tag"], "asset": doc["assets"][0]["asset"], "bytes": 7, "sha256": "aa" * 32}},
       "a complete run's set.json, asserted by its set record's SHA-256, maps its file; a run with no complete "
       "record maps nothing")
    ok(fails(lambda: asset_map(sets + sets)) and
       fails(lambda: archived_sets([dict(recs[0], sha256="cc" * 32), recs[1]], state)),
       "a file in two sets, or a set.json other than its record's, is a failed assert")
    # the store's readers on a temporary day
    store = os.path.join(tmp, "store")
    dday = os.path.join(store, str(SYN_D0))
    os.makedirs(dday)
    A, B = SYN["A"], SYN["B"]
    gdocs = [{"conditionId": c["cid"], "feesEnabled": c is A,
              "feeSchedule": {"rate": 0.05, "rebateRate": 0.25, "takerOnly": True, "exponent": 1}} for c in (A, B)]
    rep = (json.dumps({"kind": "gamma", "status": 200, "raw": json.dumps(gdocs)}) + "\n").encode()
    rgz = os.path.join(dday, "select.0.replies.jsonl.gz")
    with open(rgz, "wb") as raw_, gzip.GzipFile(fileobj=raw_, mode="wb", mtime=0) as fh:
        fh.write(rep)
    selrec = {"ok": True, "replies": {"sha256": sha256_file(rgz)}, "members": [
        {"condition_id": c["cid"], "token_ids": [c["tok"], c["other"]], "min_size": str(Fr(c["ms"], 100)),
         "max_spread": str(D(c["vu"]) / 20), "rate": str(c["rate"])} for c in (A, B)]}
    with open(os.path.join(dday, "select.0.json"), "w") as fh:
        fh.write(json.dumps(selrec))
    sel = selection_of(SYN_D0, store)
    mem = members_of(sel)
    ok(sel["attempt"] == 0 and [(x["cid"], x["tok"], x["ms"], x["vu"], x["rate"], x["fee"]) for x in mem] == [
        (A["cid"], "1001", 2000, 90, Fr(100), Fr(1, 80)), (B["cid"], "2001", 5000, 70, Fr(50), Fr(0))],
       "the selection's members: first token, size and spread as integers, the rate, and the rebate coefficient "
       "0.05 x 0.25 where fees are enabled, 0 where not")
    os.remove(os.path.join(dday, "select.0.json"))
    with open(os.path.join(dday, "select.0.json"), "w") as fh:
        fh.write(json.dumps(dict(selrec, ok=False)))
    ok(selection_of(SYN_D0, store) is None, "a day whose only attempt is not ok has no selection")
    pz = os.path.join(dday, "%d.0.rewards.jsonl.gz" % SYN_D0)
    prow = lambda c, rate, comp, more=(): json.dumps({"data": [{"condition_id": c, "market_competitiveness": comp,
                                                              "rewards_config": [{"rate_per_day": rate}] +
                                                              list(more)}]})
    cfgs = ({"rate_per_day": 999, "start_date": "1970-01-02", "end_date": "2500-12-31"},
            {"rate_per_day": 0.5, "start_date": "1969-12-31", "end_date": "1970-01-01"})
    lines_p = [{"recv_wall_ns": 7, "condition_id": B["cid"], "status": 200, "raw": prow(B["cid"], 50, 0.5)},
               {"recv_wall_ns": 5, "condition_id": A["cid"], "status": 200, "raw": prow(A["cid"], 100, 2.25, cfgs)},
               {"recv_wall_ns": 6, "condition_id": A["cid"], "status": 503, "raw": None},
               {"recv_wall_ns": 8, "condition_id": A["cid"], "status": 200, "raw": json.dumps({"data": []})}]
    with open(pz, "wb") as raw_, gzip.GzipFile(fileobj=raw_, mode="wb", mtime=0) as fh:
        fh.write(("\n".join(json.dumps(x) for x in lines_p) + "\n").encode())
    pls, cnt = polls_of(SYN_D0, {SYN_D0: [{"rewards": {"file": os.path.basename(pz)}}]}, store)
    ok(pls == [(5, A["cid"], (Fr(201, 2), Fr(9, 4))), (7, B["cid"], (Fr(50), Fr(1, 2))), (8, A["cid"], None)] and
       cnt == {"polls": 4, "unserved": 1, "no row": 1},
       "the polls in order received: rate and competitiveness exact from their text, the rate summed over the "
       "configurations in force on the poll's date; an unserved poll dropped, a page with no row kept as the end of "
       "the reward")
    pf_path = os.path.join(tmp, "polls.jsonl")
    with open(pf_path, "w", encoding="utf-8") as fh:
        fh.write(polls_text(pls))
    pf = polls_read(pf_path)
    seen = [bool(pf), pf[0]]
    first = pf.popleft()
    ok(isinstance(pf, PollFile) and seen == [True, pls[0]] and first == pls[0] and pf[0] == pls[1] and
       list(pf) == pls[1:] and not pf and pf.fh is None and fails(lambda: pf.popleft()) and
       fails(lambda: polls_read(pf_path)[1]),
       "a day's polls read back from their file one line at a time, as a deque: the front, popleft, the rest in "
       "order, the file closed at its end")
    # the documents: an outcome only where a market reads closed with prices exactly 0 and 1
    dc = lambda closed, prices: {"closed": closed, "outcomePrices": json.dumps(prices),
                                 "clobTokenIds": json.dumps(["1001", "1002"])}
    ok(outcome_of(dc(True, ["1", "0"]), "1001") == 1000 and outcome_of(dc(True, ["1", "0"]), "1002") == 0 and
       outcome_of(dc(True, ["0.5", "0.5"]), "1001") is None and outcome_of(dc(False, ["1", "0"]), "1001") is None,
       "the first token's outcome, 1 or 0, from a closed document's prices; none otherwise")
    calls = []

    def fake_get(q):
        qs = urllib.parse.parse_qs(q)
        calls.append(qs)
        ids = qs["condition_ids"]
        closed = qs.get("closed") == ["true"]
        docs = [dict(dc(closed, ["0", "1"]), conditionId=i) for i in ids if i.endswith("1") == closed]
        return docs, 10, "dd" * 32, 0
    toks = {"0x" + "%063x1" % k if k % 2 else "0x" + "%063x2" % k: "1001" for k in range(60)}
    oc, reqs = documents(toks, holdf=lambda b: (0, 0), get=fake_get)
    ok(len(calls) == 4 and len(reqs) == 4 and all(len(c["condition_ids"]) <= DOC_CHUNK for c in calls) and
       sum(1 for v in oc.values() if v == 0) == 30 and sum(1 for v in oc.values() if v is None) == 30,
       "60 members in chunks of 50, each read open and closed: 30 closed at 0 for the first token, 30 open")
    ok(fails(lambda: documents(toks, holdf=lambda b: (0, 0), get=lambda q: ([], 2, "ee" * 32, 0))),
       "a member whose document neither request returns is a failed assert")
    # the clock
    st_idle = lambda: {"pairbook": "inactive", "rewardbook": "inactive"}
    ok(quiet(SYN_D0 + 900 * 10 + 15, 45, st_idle) is None and
       quiet(SYN_D0 + 900 * 10 + 14, 45, st_idle) == "second 14 of the window" and
       quiet(SYN_D0 + 900 * 10 + 546, 45, st_idle) == "second 546 of the window" and
       quiet(SYN_D0 + 900 * 4 + 20, 45, st_idle) is None and
       quiet(SYN_D0 + 5430, 20, st_idle) == CALENDAR[0][1] and
       quiet(SYN_D0 + 10820 + 10, 20, st_idle) == CALENDAR[1][1] and
       quiet(SYN_D0 + 900 * 10 + 15, 45, lambda: {"pairbook": "activating"}) is not None,
       "a unit starts from second 15 and ends by 590, clear of both archives' calendar runs and of their services")
    clk = [float(SYN_D0 + 900 * 10 + 580)]
    t_, w_ = hold(45, clock=lambda: clk[0], sleep=lambda s: clk.__setitem__(0, clk[0] + s), state_of=st_idle)
    ok(t_ == SYN_D0 + 900 * 11 + 15 and w_ == 335, "held from second 580 to the next window's second 15")
    # the reading's purity: G-STILL and NUMBER
    u = {"recorder": {"MainPID": "1", "NRestarts": "0", "ActiveState": "active"},
         "pairbook": {"MainPID": "2", "NRestarts": "3", "ActiveState": "active"},
         "rewardbook": {"MainPID": "4", "NRestarts": "1", "ActiveState": "active"},
         "advisor": {"MainPID": "5", "NRestarts": "0", "ActiveState": "active"}}
    u2 = json.loads(json.dumps(u))
    u2["pairbook"] = {"MainPID": "9", "NRestarts": "4", "ActiveState": "active"}
    u3 = json.loads(json.dumps(u2))
    u3["rewardbook"]["MainPID"] = "6"
    ok(still_reading(u, u, [])[0] and still_reading(u, u2, [{"stopped": "2", "NRestarts": "4", "pid": "9"}])[0] and
       not still_reading(u, u2, [])[0] and not still_reading(u, u3, [{"stopped": "2", "NRestarts": "4", "pid": "9"}])[0],
       "G-STILL: unchanged, or the pair book moved by its archive's restarts alone; any other change fails")
    names = ["CryptoTZ/TZ-40-strong-every-rank.md", "CryptoTZ/TZ-41-l0-our-quote.md", "CryptoReports/TZ-40-x-report.md"]
    ok(number_reading(names, "CryptoTZ/TZ-41-l0-our-quote.md")[0] and
       not number_reading(names + ["CryptoTZ/TZ-41-other.md"], "CryptoTZ/TZ-41-l0-our-quote.md")[0] and
       not number_reading(names + ["CryptoReports/TZ-41-l0-our-quote-report.md"],
                          "CryptoTZ/TZ-41-l0-our-quote.md")[0], "NUMBER: this file alone of its number, no report")
    # the hook
    ok(policy("fetch", "open", (RB_ROOT + "/%d/select.0.json" % FIRST_D0, "rb")) is None and
       policy("fetch", "open", (RB_ROOT + "/%d/select.0.json" % (FIRST_D0 - DAY), "rb")) is not None and
       policy("replay", "open", (RB_ROOT + "/%d/select.0.json" % FIRST_D0, "rb")) is not None and
       policy("fetch", "open", (RB_ROOT + "/%d/%d.0.stream.jsonl.gz" % (FIRST_D0, FIRST_D0), "rb")) is not None and
       policy("fetch", "os.listdir", (RB_ROOT + "/%d" % FIRST_D0,)) is None and
       policy("fetch", "os.listdir", (RB_ROOT,)) is not None and
       policy("archive", "open", (RB_LEDGER, "rb")) is None and policy("score", "open", (RB_LEDGER, "rb")) is not None
       and policy("still", "open", (PB_LEDGER, "rb")) is None and
       policy("replay", "urllib.Request", ("https://github.com/x",)) is None and
       policy("fetch", "urllib.Request", ("https://github.com/x",)) is not None and
       policy("fetch", "urllib.Request", ("https://gamma-api.polymarket.com/markets?x",)) is None and
       policy("replay", "urllib.Request", ("https://clob.polymarket.com/x",)) is not None and
       policy("replay", "open", (RECORDER + "/x", "rb")) is not None and
       policy("replay", "open", ("/root/elsewhere", "wb")) is not None and
       policy("reclaim", "open", (FORENSICS + "/x", "xb")) is None and
       policy("reclaim", "open", (FORENSICS + "/x", "wb")) is not None and
       policy("replay", "subprocess.Popen", ("curl", ["curl"])) is not None,
       "the hook: the store's day files to fetch alone and for the span's days, never a stream; each archive's "
       "record to its modes; Release downloads, gamma and nothing else; no write outside the work tree but the "
       "forensic store's exclusive creates; no process but git, systemctl and stat")
    # downloads on the loopback: a good asset, a corrupt reply retried, a 404 given up
    blob = b"stream bytes" * 1000
    hits = collections.Counter()

    class H(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_GET(self):
            hits[self.path] += 1
            if self.path == "/t/bad" and hits[self.path] == 1:
                body = b"x" * len(blob)
            elif self.path in ("/t/good", "/t/bad"):
                body = blob
            else:
                self.send_response(404)
                self.end_headers()
                return
            self.send_response(200)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    try:
        url_of = lambda t, a: "http://127.0.0.1:%d/%s/%s" % (srv.server_port, t, a)
        dest = os.path.join(tmp, "dl")
        n1 = download("t", "good", len(blob), sha256_bytes(blob), dest, url_of=url_of, sleep=lambda s: None)
        n2 = download("t", "bad", len(blob), sha256_bytes(blob), dest + "2", url_of=url_of, sleep=lambda s: None)
        ok(n1[0] == n2[0] == len(blob) and n1[2] == 0 and n2[2] == 1 and sha256_file(dest) == sha256_bytes(blob) and
           not os.path.exists(dest + "2.part"), "a download verified by bytes and SHA-256; a corrupt reply retried")
        ok(fails(lambda: download("t", "gone", 1, "ff" * 32, dest + "3", url_of=url_of, sleep=lambda s: None)) and
           hits["/t/gone"] == DL_TRIES, "a 404, as a repository not serving its Releases answers, is tried %d times, "
                                        "then BLOCKED" % DL_TRIES)
    finally:
        srv.shutdown()
        srv.server_close()
    # a unit removes its files whatever the replay does, and the projection blocks
    fake = lambda t, a, nb, sha, dst: (open(dst, "wb").close(), (0, 0.0, 0))[1]
    tim = os.path.join(tmp, "timing.jsonl")
    fl = [{"file": "%d.0.stream.jsonl.gz" % SYN_D0, "tag": "t", "asset": "a0", "bytes": 1, "sha256": "x"}]
    ok(fails(lambda: run_unit(SYN_D0, fl, os.path.join(tmp, "u"), lambda p: 1 / 0, tim, holdf=lambda b: (0.0, 0),
                              dl=fake), ZeroDivisionError) and not os.listdir(os.path.join(tmp, "u")),
       "a unit whose replay fails leaves no file behind")
    pj = Projection(10 ** 9, 100, after=2)
    pj({"cpu_s": 1.0, "bytes": 10 ** 6})
    ok(fails(lambda: pj({"cpu_s": 1.0, "bytes": 10 ** 6})), "a replay projected above its bound stops BLOCKED")
    shutil.rmtree(tmp)
    out("SELFTEST PASS: %d checks" % n[0])


if __name__ == "__main__":
    main(sys.argv[1:])
