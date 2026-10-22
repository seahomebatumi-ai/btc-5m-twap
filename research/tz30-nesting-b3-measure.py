#!/usr/bin/env python3
"""TZ-30 - B3's measurement: can a violation of the nested pair's containment be captured by a taker - through
the 150 ms taker delay, at depth, both legs together, with the strikes known live?

    fingerprint       contract section 1 steps 3 and 4, asserted: the map's revision, anchors and rows
    selftest          every rule of this file, on literals and on temporary trees under the work tree
    still             the recorder's and the pair book's MainPID, NRestarts and ActiveState, and at the second
                      run the archive's own restarts between the two (G-STILL)
    scratch OWN       the UUID directories beside OWN, this session's, each named live or earlier
    archive           the pair book archive's ledger and the set.json of every run, read and printed, and
                      the asset of every stream file the archive has moved (G-ASSETS)
    rehearse          the capture rule over TZ-27's 51 windows with the published strikes, every unit held to
                      the idle stretch, against the Architect's figures (G-REHEARSAL)
    fetch             the 936 candidates 1791706500 to 1792548000, once the archive has moved them: window.json
                      and both settled documents of each, by TZ-24's set rule, and TZ-30 section 1's conditions
    strikes           the strikes of each candidate, live, from the recorder's twap60; the set (G-SET)
    score             the members' streams replayed, every unit held to the idle stretch: G-REBUILD and B3's
                      reading
    rescore           every sixteenth member replayed again, from a second download: determinism
    reclaim TREE...   section 9

It loads research/tz24-nesting-b2.py, executed from the bytes whose SHA-256 it asserts, and through it
research/tz14-quote-inventory.py, whose bytes it asserts first: TZ-24's set rule, documents, identities, pair,
payoff, costs, class and stored-reply reader, and TZ-14's fee, touch and book parser, are the ones every step
calls. Mode strikes loads research/pfair.py and the recorder's config, manifest and analyze the same way and
never TZ-24, whose audit hook refuses the recorder's root. Its requests are TZ-24's to gamma-api.polymarket.com,
through TZ-24's http_json and its two headers; downloads of Release assets from github.com, with
User-Agent: btc-5m-twap-tz30; and git against origin. An audit hook refuses every open, listing, request and
process TZ-30 section 2 does not give the running mode. It writes under /root/tz30-work/ and, in reclaim, new
files in /root/btc-forensics/ by exclusive create. It prints sums over a set, and of a single window its
figures inside the work tree alone. Exit 0: every assert of the mode held. Exit 1: an assert failed, and its
message names it. Run it with the research interpreter, /root/tz01-env.

Written for CryptoTZ/TZ-30-nesting-b3-measure.md. The TZ is the specification.
"""

import datetime
import gzip
import hashlib
import http.client
import json
import os
import re
import resource
import shutil
import subprocess
import sys
import time
import types
import urllib.error
import urllib.parse
import urllib.request
from decimal import Decimal as D, getcontext, ROUND_HALF_EVEN, localcontext

if not __debug__:
    sys.stderr.write("tz30: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

getcontext().prec = 60
HERE = os.path.dirname(os.path.abspath(__file__))

# ---- the TZ's constants: none of them is measured by this run --------------------------------------------

MAP_REVISION = "2026-10-20-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 38, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"`?([0-9a-f]{64}|self-reference[^|]*?)`? \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)

# the frozen files this instrument executes, each by map section 0's SHA-256, relative to research/
FROZEN = {"tz24-nesting-b2.py": "4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b",
          "tz14-quote-inventory.py": "978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02",
          "pfair.py": "729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68",
          "recorder/analyze.py": "eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d",
          "recorder/config.py": "8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d",
          "recorder/manifest.py": "79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045"}

WINDOW = 900
FIRST_T = 1791706500         # the first window after TZ-27's 51, the Architect's exploration (section 1)
NEED = 768                   # members: 8 blocks of 96, one day of windows each
BLOCKS = 8
BLOCK_N = 96
THETA = D("10")              # USDC a block: CAPTURE where every block reaches it, NO CAPTURE where none does
NONMEMBER_MAX = 168          # the walk is BLOCKED past this many non-members before the 768th member
LAST_T = FIRST_T + (NEED + NONMEMBER_MAX - 1) * WINDOW   # 1792548000: the candidates' last window, 936 in all
ARCHIVE_WAIT_UNTIL = 1792562400    # 2026-10-21 06:00:00 UTC: fetch waits for the archive to reach LAST_T until then
SPAN = (605, 895)            # the detection span, host seconds after T: [T + 605, T + 895)
MIN_SIZE = D("5")            # the venue's minimum order, asserted in both documents of every member
Q_CAP = D("1000")            # net shares an attempt buys at most
TICK = D("0.01")             # touch_of's tick for the strategy's touch; bid5 and ask5 do not depend on it
VARIANTS = (("primary", 50, 150, "shares"), ("L0", 0, 150, "shares"), ("L25", 25, 150, "shares"),
            ("L100", 100, 150, "shares"), ("L250", 250, 150, "shares"), ("nodelay", 50, 0, "shares"),
            ("top", 50, 150, "top"))      # (name, one-way latency ms, taker delay ms, how the buy fee is paid)
STRIKE_WITHIN_MS = 2000      # a strike's report is published at most 2 s after its boundary
STRIKE_RECV_S = 605          # and received by the host by T + 605, the detection span's start
SUBSCRIBE_BY_S = 600         # the stream subscribed by T + 600
LAST_FRAME_S = 900           # and its last frame at or after T + 900
GAP_MAX_NS = 15 * 10 ** 9    # with no gap between frames above 15 s
REBUILD_EQUAL_MIN = D("0.98")      # G-REBUILD: the rebuilt touch equals the stored reply's at 98% of compared
REBUILD_COMPARED_MIN = D("0.90")   # replies, and at least 90% of the members' served replies are compared
RESCORE_EVERY = 16           # rescore replays members 0, 16, 32, ...: 48 of 768
SCORE_CPU_MAX = 3190         # processor seconds score's replays may take, projected after its first 24 units
RESCORE_CPU_MAX = 210        # and rescore's
PROJECT_AFTER = 24
UNIT_BUDGET_S = 40           # a unit's budget beside its download: replay, books and deletion
DL_RATE = 2000000            # bytes a second a download is budgeted at, TZ-28's
DL_TRIES = 6
FETCH_BUDGET_S = 120         # TZ-24's walk projected past this after 20 requests is BLOCKED
GAMMA_TRIES = 4              # a gamma request cut short (IncompleteRead) is asked again, at most 3 times more
IDLE = (15, 590)             # the pair book's idle stretch: a unit starts at second 15 or later, ends by 590
ARCHIVE_UNIT = "btc-pairbook-archive.service"
ARCHIVE_TIMER = "btc-pairbook-archive.timer"
ARCHIVE_CALENDAR_S = 10820   # the archive's calendar run, 03:00:20 UTC
ARCHIVE_LEAD_S = 60          # nothing starts from budget + 60 s before it to 60 s after it
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")
HOLD_MAX_S = 7200
MEM_FLOOR = 116711424        # MemAvailable: TZ-30 section 0.4, twice the largest peak the Architect measured
DISK_FLOOR = 4800000000      # free bytes on /dev/vda2: TZ-30 section 0.4

UA = "btc-5m-twap-tz30"
DL_HEADERS = {"User-Agent": UA, "Accept": "application/octet-stream"}
REPO = "seahomebatumi-ai/btc-5m-twap"
DL_URL = "https://github.com/" + REPO + "/releases/download/%s/%s"
DL_HOSTS = ("github.com", "release-assets.githubusercontent.com", "objects.githubusercontent.com")
GAMMA_HOST = "gamma-api.polymarket.com"
ASSET_RE = re.compile(r"([0-9]{10})-(stream(?:\.[1-9][0-9]*)?\.jsonl\.gz)")
STREAM_FILE_RE = re.compile(r"stream(?:\.[1-9][0-9]*)?\.jsonl\.gz")

# the rehearsal: TZ-27's 51 windows, its set.json in the forensic store (TZ-27's report), and the Architect's
# figures over them from an independent implementation in exact rational arithmetic (TZ-30 section 4.1)
REHEARSAL_TS = tuple(range(1791660600, 1791705600 + 1, WINDOW))
TZ27_TAG = "tz-27-pairbook-streams"
TZ27_SET = "/root/btc-forensics/tz27-work--archive--set.json"
TZ27_SET_SHA = "ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd"
REF = {"lines": 357, "digest": "402b378a274613153410aa068abaaa798d68d4770a22239a07442ba42411bade",
       "totals": {"primary": [125, "-95.936018771005"], "L0": [139, "-23.646658648482"],
                  "L25": [132, "-50.344323117306"], "L100": [113, "-117.369164961585"],
                  "L250": [91, "-169.125533904780"], "nodelay": [166, "-0.893613644133"],
                  "top": [143, "-100.148749740000"]}}

WORK = "/root/tz30-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/label-ledger.jsonl"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
BRANCH = "tz-30-nesting-b3-measure"
UNITS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service"}
PAIRBOOK = "/var/lib/btc-pairbook"
RECORDER = "/var/lib/btc-recorder"
CHAINBOOK = "/var/lib/btc-chainbook"
ARCHIVE_STATE = "/var/lib/btc-pairbook-archive"
ARCHIVE_LEDGER = ARCHIVE_STATE + "/ledger.jsonl"
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
LIVE_S = 60

# ---- the frozen files, executed from their asserted bytes ------------------------------------------------

_MODS = {}


def verified(rel, base=None):
    path = os.path.join(base or HERE, rel)
    with open(path, "rb") as fh:
        raw = fh.read()
    got = hashlib.sha256(raw).hexdigest()
    assert got == FROZEN[rel], "%s sha256 %s, map section 0 %s" % (path, got, FROZEN[rel])
    return path, raw


def exec_frozen(name, rel):
    path, raw = verified(rel)
    mod = types.ModuleType(name)
    mod.__file__ = path
    sys.modules[name] = mod
    exec(compile(raw, path, "exec"), mod.__dict__)
    return mod


def tz24():
    """TZ-24's instrument from its asserted bytes. It installs its audit hook - every open under the recorder's
    root refused - sets the main thread's 60 digits and loads TZ-14 from beside itself on first use, whose
    bytes, with pfair's and the recorder's three, are asserted here before."""
    if "tz24" not in _MODS:
        assert "pfair" not in sys.modules, "tz24 and the strikes' modules are never loaded in one process"
        for rel in ("tz14-quote-inventory.py", "pfair.py", "recorder/analyze.py", "recorder/config.py",
                    "recorder/manifest.py"):
            verified(rel)
        _MODS["tz24"] = exec_frozen("tz24nestingb2", "tz24-nesting-b2.py")
    return _MODS["tz24"]


def tz14():
    if "tz14" not in _MODS:
        _MODS["tz14"] = tz24().tz14()
    return _MODS["tz14"]


def strike_modules(allow_tz24=False):
    """The recorder's config, manifest and analyze and the pricer's file, each from its asserted bytes, in that
    order: analyze.reports, the only stream reader, and pfair.price_to_beat, the strike's one rule. Where TZ-24
    is loaded - the self-test alone - they are the ones TZ-14 imported, whose bytes tz24() asserted."""
    assert allow_tz24 or "tz24" not in _MODS, "the strikes are never read in a process that loaded TZ-24"
    rec = os.path.join(HERE, "recorder")
    for p in (HERE, rec):
        if p not in sys.path:
            sys.path.insert(0, p)
    for name, rel in (("config", "recorder/config.py"), ("manifest", "recorder/manifest.py"),
                      ("analyze", "recorder/analyze.py"), ("pfair", "pfair.py")):
        if name not in sys.modules:
            exec_frozen(name, rel)
    return sys.modules["config"], sys.modules["analyze"], sys.modules["pfair"]

# ---- the audit hook: TZ-30 section 2's reads, writes, requests and processes -----------------------------


MODE = [None]
REFUSED = []
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
PB_WINDOW = re.compile(r"/var/lib/btc-pairbook/([0-9]{10})/(window\.json|books\.jsonl\.gz)")
RECORDER_TWAP = re.compile(r"/var/lib/btc-recorder/btc-updown-5m/([0-9]{10})/twap60\.jsonl\.gz")
ARCHIVE_SET = re.compile(r"/var/lib/btc-pairbook-archive/runs/([0-9]{10})/set\.json")
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


def policy(mode, event, args):
    """None where TZ-30 section 2 allows the event in this mode; otherwise the reason it is refused."""
    if event == "urllib.Request":
        host = urllib.parse.urlsplit(args[0]).hostname if args and isinstance(args[0], str) else None
        if mode in ("rehearse", "score", "rescore") and host in DL_HOSTS:
            return None
        if mode in ("rehearse", "fetch") and host == GAMMA_HOST:
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
        if any(_under(p, r) for r in (RECORDER, CHAINBOOK, PAIRBOOK, ARCHIVE_STATE)):
            return "a listing under a capture root or the archive's state"
        return None
    wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
    w = _writing(wm, fl)
    if _under(p, CHAINBOOK):
        return "an open under the chain book's root"
    if _under(p, RECORDER):
        if mode == "strikes" and not w and RECORDER_TWAP.fullmatch(p):
            return None
        return "an open under the recorder's root"
    if _under(p, PAIRBOOK):
        m = PB_WINDOW.fullmatch(p)
        if w or m is None or int(m.group(1)) < FIRST_T:
            return "an open under the pair book's root"
        if m.group(2) == "window.json" and mode in ("fetch", "score", "rescore"):
            return None
        if m.group(2) == "books.jsonl.gz" and mode in ("score", "rescore"):
            return None
        return "%s in mode %s" % (m.group(2), mode)
    if _under(p, ARCHIVE_STATE):
        if not w and mode in ("archive", "fetch") and (p == ARCHIVE_LEDGER or ARCHIVE_SET.fullmatch(p)):
            return None
        if not w and mode == "still" and p == ARCHIVE_LEDGER:
            return None
        return "an open under the archive's state"
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
    if why is not None:
        REFUSED.append((event, str(args[0]) if args else ""))
        raise GuardError("%s refused in mode %s, %s: %r" % (event, MODE[0], why, args[0] if args else None))


sys.addaudithook(_audit)

# ---- small helpers ----------------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))


def fx(x):
    """A Decimal as fixed-point text, never in exponent form."""
    return format(x, "f")


def q12(x):
    """A Decimal rounded half-even to 12 places, as fixed-point text, without a sign on zero."""
    with localcontext() as ctx:
        ctx.prec = 120
        s = format(D(x).quantize(D("1e-12"), rounding=ROUND_HALF_EVEN), "f")
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


def _dec(o):
    if isinstance(o, D):
        return fx(o)
    raise TypeError(type(o))


def dumps(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=_dec) + "\n"


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh, parse_float=D)


def load_state():
    return load_json(STATE) if os.path.exists(STATE) else {}


def save_state(st):
    write_atomic(STATE, (json.dumps(st, sort_keys=True, indent=1, default=_dec) + "\n").encode("utf-8"))


def mem_available():
    with open("/proc/meminfo", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) * 1024
    raise AssertionError("no MemAvailable")


def free_bytes(path=WORK):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def floor_check():
    """Before a mode that reads the venue, the archive's Releases or a set: the memory and the disk floor."""
    avail, free = mem_available(), free_bytes()
    out("MemAvailable %d bytes, floor %d; free %d bytes, floor %d" % (avail, MEM_FLOOR, free, DISK_FLOOR))
    assert avail >= MEM_FLOOR, "BLOCKED: MemAvailable %d bytes, below %d" % (avail, MEM_FLOOR)
    assert free >= DISK_FLOOR, "BLOCKED: %d bytes free, below %d" % (free, DISK_FLOOR)


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


def weekday(t):
    return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%a")

# ---- the clock: the pair book's idle stretch and the archive's run -------------------------------------------


def archive_state():
    cp = subprocess.run(["systemctl", "is-active", ARCHIVE_UNIT], capture_output=True, text=True)
    return cp.stdout.strip()


def quiet(now, budget, state_of=archive_state):
    """None where a unit of `budget` seconds may start at `now`; otherwise why not: it starts inside the pair
    book's idle stretch and ends by its second 590, never near or during the archive's run."""
    p = int(now) % WINDOW
    if not IDLE[0] <= p <= IDLE[1] - budget:
        return "second %d of the window" % p
    d = int(now) % 86400
    if ARCHIVE_CALENDAR_S - budget - ARCHIVE_LEAD_S <= d <= ARCHIVE_CALENDAR_S + ARCHIVE_LEAD_S:
        return "the archive's calendar run at 03:00:20 UTC"
    st = state_of()
    if st in RUNNING:
        return "the archive's service is %s" % st
    return None


def hold(budget, clock=time.time, sleep=time.sleep, state_of=archive_state):
    """Until a unit of `budget` seconds may start; returns that instant and the seconds waited."""
    assert budget <= IDLE[1] - IDLE[0], "a unit of %d s fits no idle stretch" % budget
    t0 = clock()
    while True:
        now = clock()
        why = quiet(now, budget, state_of)
        if why is None:
            return now, now - t0
        assert now - t0 <= HOLD_MAX_S, "BLOCKED: held %.0f s, the last reason %s" % (now - t0, why)
        sleep(1.0)

# ---- the archive's record: its ledger, every run's set.json, and the asset of every stream file -------------


def ledger_records(path=ARCHIVE_LEDGER):
    with open(path, "rb") as fh:
        raw = fh.read()
    lines = raw.split(b"\n")
    tail = lines.pop()
    return raw, [json.loads(ln) for ln in lines if ln.strip()], tail


def archived_sets(recs, state=ARCHIVE_STATE):
    """Every run whose ledger holds a complete record: its set.json, asserted by the SHA-256 its set record
    carries, its tag, assets and counts against that record."""
    runs, order = {}, []
    for r in recs:
        a = r.get("run")
        if a not in runs:
            runs[a] = []
            order.append(a)
        runs[a].append(r)
    found = []
    for a in order:
        ev = [r.get("event") for r in runs[a]]
        if "complete" not in ev:
            continue
        sets = [r for r in runs[a] if r.get("event") == "set"]
        assert sets and isinstance(a, int), "run %r: complete without a set record" % a
        path = os.path.join(state, "runs", str(a), "set.json")
        with open(path, "rb") as fh:
            raw = fh.read()
        sha = sha256_bytes(raw)
        assert sha == sets[-1]["sha256"], "run %d: set.json sha256 %s, its set record %s" % (a, sha,
                                                                                          sets[-1]["sha256"])
        doc = json.loads(raw)
        assert doc["tag"] == sets[-1]["tag"] and doc["assets_n"] == sets[-1]["assets_n"] == len(doc["assets"]) \
            and doc["bytes_total"] == sets[-1]["bytes_total"], "run %d: set.json against its set record" % a
        found.append({"run": a, "tag": doc["tag"], "sha256": sha, "doc": doc})
    return found


def asset_map(sets):
    """T -> {file: {tag, asset, bytes, sha256}}, every stream file once; a file in two sets is a failed assert."""
    m = {}
    for s in sets:
        for x in s["doc"]["assets"]:
            mt = ASSET_RE.fullmatch(x["asset"])
            assert mt and int(mt.group(1)) == x["T"] and mt.group(2) == x["file"], "an asset named %r" % x["asset"]
            row = m.setdefault(x["T"], {})
            assert x["file"] not in row, "window %d: %s in two sets" % (x["T"], x["file"])
            row[x["file"]] = {"tag": s["tag"], "asset": x["asset"], "bytes": x["bytes"], "sha256": x["sha256"]}
    return m

# ---- the window: TZ-30 section 1's stream conditions -------------------------------------------------------


def stream_problem(w, t, assets):
    """The first stream condition window.json `w` fails, or None: opened, not cut, not stopped, not joined late,
    subscribed by T + 600, its last frame at or after T + 900, no gap above 15 s, every file of it archived."""
    st = w.get("stream") if isinstance(w, dict) else None
    if not isinstance(st, dict):
        return "stream: none"
    if w.get("joined_late") is not False or w.get("stopped") is not False:
        return "stream: joined late or stopped"
    if st.get("opened") is not True or st.get("off_reason") is not None or not st.get("files"):
        return "stream: not opened"
    if st.get("cut") is not False:
        return "stream: cut"
    sub, last, gap = st.get("subscribed_wall_ns"), st.get("last_frame_wall_ns"), st.get("max_gap_ns")
    if not (type(sub) is int and sub <= (t + SUBSCRIBE_BY_S) * 10 ** 9):
        return "stream: subscribed late"
    if not (type(last) is int and last >= (t + LAST_FRAME_S) * 10 ** 9):
        return "stream: ended early"
    if not (type(gap) is int and gap <= GAP_MAX_NS):
        return "stream: a gap above 15 s"
    files = st["files"]
    if not (all(isinstance(f, str) and STREAM_FILE_RE.fullmatch(f) for f in files) and len(set(files)) == len(files)):
        return "stream: files"
    if sorted(assets.get(t, {})) != sorted(files):
        return "stream: not archived"
    return None


def window_json(t, root=PAIRBOOK):
    with open(os.path.join(root, str(t), "window.json"), "rb") as fh:
        return json.loads(fh.read())


def gamma_retry(docs_dir, slugs, tries=GAMMA_TRIES, sleep=time.sleep):
    """TZ-24's gamma_cached, asked again where the venue's reply was cut short - http.client's IncompleteRead,
    which TZ-24's http_json does not retry - 30 s apart, at most GAMMA_TRIES times in all."""
    for k in range(tries):
        try:
            return tz24().gamma_cached(docs_dir, slugs)
        except http.client.HTTPException as e:
            if k == tries - 1:
                raise AssertionError("BLOCKED: gamma %s, %d times" % (type(e).__name__, tries))
            out("gamma %s on %s; asked again in 30 s" % (type(e).__name__, slugs[0]))
            sleep(30)
    raise AssertionError("unreachable")


def cached_docs(docs_dir):
    """Every settled document TZ-24's cache holds, by slug: the bodies its requests stored, read back."""
    by = {}
    for name in sorted(os.listdir(docs_dir)):
        if name.endswith(".json.gz"):
            with gzip.open(os.path.join(docs_dir, name), "rb") as fh:
                for d in json.loads(fh.read(), parse_float=D):
                    assert d["slug"] not in by, "%s in two cache files" % d["slug"]
                    by[d["slug"]] = d
    return by


def order_size_problem(by, t):
    """orderMinSize of both settled documents: the venue's 5, or the reason the window is not a member."""
    for slug in (tz24().slug15(t), tz24().slug5(t + 600)):
        v = by[slug].get("orderMinSize")
        if isinstance(v, bool) or not isinstance(v, (int, D)) or D(v) != MIN_SIZE:
            return "order size: %s" % slug.rsplit("-", 2)[1]
    return None

# ---- the strikes, live: the recorder's twap60 at T and at T + 600 -------------------------------------------


def report_recv(path, ts_ms):
    """The earliest receive stamp of a line of `path` whose update frame is published at `ts_ms`, or None. Reads
    the line's recv_ns and the frame's type and timestamp, and no value: the value is analyze.reports'."""
    best = None
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                frame = json.loads(rec["raw"])
                ts = (frame.get("payload") or {}).get("timestamp")
            except (ValueError, KeyError, TypeError, AttributeError):
                continue
            if frame.get("type") == "update" and ts is not None and int(ts) == ts_ms and type(
                    rec.get("recv_ns")) is int:
                best = rec["recv_ns"] if best is None else min(best, rec["recv_ns"])
    return best


def strike_of(boundary, T, config, analyze, pfair):
    """A strike as the live strategy knows it: pfair.price_to_beat of the interval opening at `boundary`, from
    analyze.reports of its twap60; its report published within 2 s of the boundary and received by T + 605."""
    rows = analyze.reports(boundary, "twap60")
    k = pfair.price_to_beat(boundary, rows)
    if k is None:
        return None, "no report at or after %d" % boundary
    ts = min(ts for ts, _v in rows if ts >= boundary * analyze.MS)
    assert analyze.first_at_or_after(rows, ts) == k, "the strike's report"
    if ts - boundary * analyze.MS > STRIKE_WITHIN_MS:
        return None, "published %d ms after %d" % (ts - boundary * analyze.MS, boundary)
    recv = report_recv(os.path.join(config.interval_dir(boundary), "twap60.jsonl.gz"), ts)
    if recv is None or recv > (T + STRIKE_RECV_S) * 10 ** 9:
        return None, "received after T + %d" % STRIKE_RECV_S
    return {"value": k, "ts_ms": ts, "recv_ns": recv}, None

# ---- the replay: one window's stream, the capture rule of TZ-30 section 1 ----------------------------------


# A price_change frame of two entries, as the venue sends it and the pair book stores it, matched whole: its
# fields are runs of digits, hex or "BUY"/"SELL", where no escape can occur, so a line this pattern matches holds
# exactly the values json would read from it. Any other line is read by json.
_ENTRY = (r'\{\\"asset_id\\":\\"([0-9]+)\\", \\"price\\":\\"([0-9.]+)\\", \\"size\\":\\"([0-9.]+)\\", '
          r'\\"side\\":\\"(BUY|SELL)\\", \\"hash\\":\\"[0-9a-f]*\\", \\"best_bid\\":\\"[0-9.]+\\", '
          r'\\"best_ask\\":\\"([0-9.]+)\\"\}')
PC_LINE = re.compile(r'\{"recv_ns":([0-9]+),"mono_ns":-?[0-9]+,"raw":"\{\\"market\\":\\"(0x[0-9a-f]{64})\\", '
                     r'\\"price_changes\\":\[' + _ENTRY + ', ' + _ENTRY + r'\], \\"timestamp\\":\\"([0-9]+)\\", '
                     r'\\"event_type\\":\\"price_change\\"\}"\}\n?')


class Terms:
    """One price's terms, cached: TZ-24's two costs of a net share, the net shares a gross share gives with the fee
    collected in shares, and a sale's proceeds after the fee - each from tz14.fee_pp."""

    def __init__(self):
        self.c = {}

    def of(self, p):
        r = self.c.get(p)
        if r is None:
            top, shares = tz24().costs(p)
            f = tz14().fee_pp(p)
            r = (top, shares, D(1) - f / p, p - f)
            self.c[p] = r
        return r


class Var:
    __slots__ = ("name", "L", "delay", "top", "used_ask", "used_bid", "busy_until", "queries", "attempts",
                 "next_settle")

    def __init__(self, name, L, delay, conv):
        self.name, self.L, self.delay, self.top = name, L, delay, conv == "top"
        self.used_ask = {}       # (token, price) -> net shares bought there
        self.used_bid = {}       # (token, price) -> shares sold there
        self.busy_until = 0
        self.queries = []        # pending, in registration order
        self.attempts = []
        self.next_settle = 0


ZERO = D(0)
ONE = D(1)
MS_NS = 10 ** 6
_MISS = object()


class Lazy:
    """A generator's items, kept as they are drawn: item i, or None past the last."""
    __slots__ = ("it", "got")

    def __init__(self, it):
        self.it, self.got = it, []

    def at(self, i):
        while len(self.got) <= i:
            nxt = next(self.it, None)
            if nxt is None:
                return None
            self.got.append(nxt)
        return self.got[i]


class Replay:
    """The replay of one window: every frame in order, every book rebuilt, every variant's attempts placed at venue
    time, and G-REBUILD's comparisons against the stored replies."""

    def __init__(self, T, legs, markets, counted, realized, won, rest=(), variants=VARIANTS, terms=None):
        self.T = T
        self.legs = legs                       # {"x": token, "y": token}
        self.mk = markets                      # token -> condition id, all four tokens
        self.toks = (legs["x"], legs["y"])
        self.markets = {markets[legs["x"]], markets[legs["y"]]}
        self.counted, self.realized, self.won = counted, realized, won
        self.terms = terms or Terms()
        self.book = {t: {"bids": {}, "asks": {}, "field": None, "seed": None, "amin": None} for t in self.toks}
        self.price = {}                        # a price's text -> its Decimal
        self.fields = {}                       # a best_ask's text -> its Decimal, None where 1 or more, or 0
        self.vs = [Var(*v) for v in variants]
        self.pending = 0
        self.due = {}                          # market -> the earliest instant a pending query of it waits for
        self.lag = {}                          # ms -> price_change frames received that long after their stamp
        self.lines = self.inconsistent = self.frames = self.skipped = 0
        self.span = ((T + SPAN[0]) * 10 ** 9, (T + SPAN[1]) * 10 ** 9)
        assert all(r["token"] in self.toks for r in rest), "G-REBUILD compares the two legs' books alone"
        self.rq = sorted(rest, key=lambda r: r["tau"])    # G-REBUILD's queries: token, tau, book, size, tick
        self.rb = {"queries": len(self.rq), "compared": 0, "equal": 0, "full": 0, "unseeded": 0, "unresolved": 0,
                   "unequal": []}

    # -- the books ------------------------------------------------------------------------------------------

    def min_ask(self, t):
        return self.book[t]["amin"]

    def ask_levels(self, v, t, prices):
        """(price, net shares left, net per gross) of a token's asks after variant v's own buys, ascending, each
        computed when it is first needed."""
        asks, used, top, tc = self.book[t]["asks"], v.used_ask, v.top, self.terms.c
        for p in prices:
            npg = ONE if top else (tc.get(p) or self.terms.of(p))[2]
            a = asks[p] * npg - used.get((t, p), ZERO)
            if a > 0:
                yield p, a, npg

    @staticmethod
    def ask5(lv):
        """tz14.touch_of's ask5 over the levels up to the first whose gross shares left reach the minimum size: the
        same answer as over every level, without touch_of's cumulative sums over the rest. None where none does."""
        i = 0
        while True:
            x = lv.at(i)
            if x is None:
                return None
            if x[1] / x[2] >= MIN_SIZE:
                break
            i += 1
        return tz14().touch_of({"bids": [], "asks": [(p, a / npg) for p, a, npg in lv.got[:i + 1]]}, MIN_SIZE,
                               TICK)["ask5"]

    def unit_cost(self, v, p):
        r = self.terms.of(p)
        return r[0] if v.top else r[1]

    # -- queries --------------------------------------------------------------------------------------------

    def do_query(self, v, q):
        a = v.attempts[q["k"]]
        t = self.legs[q["leg"]]
        if q["kind"] == "buy":
            got, n = [], ZERO
            asks, used = self.book[t]["asks"], v.used_ask
            for p in sorted(asks):
                if p > q["limit"] or n == a["q"]:
                    break
                npg = ONE if v.top else self.terms.of(p)[2]
                avail = asks[p] * npg - used.get((t, p), ZERO)
                if avail <= 0:
                    continue
                take = min(avail, a["q"] - n)
                got.append((p, take, take * self.unit_cost(v, p)))
                n += take
                used[(t, p)] = used.get((t, p), ZERO) + take
            a["fills"][q["leg"]] = got
        else:
            a["snap"][q["leg"]] = dict(self.book[t]["bids"])

    def settle(self, v):
        while v.next_settle < len(v.attempts):
            a = v.attempts[v.next_settle]
            if a["void"]:
                v.next_settle += 1
                continue
            fx_, fy = a["fills"]["x"], a["fills"]["y"]
            if fx_ is None or fy is None:
                return
            nx = sum((n for _p, n, _c in fx_), ZERO)
            ny = sum((n for _p, n, _c in fy), ZERO)
            m, e = min(nx, ny), abs(nx - ny)
            z = "x" if nx > ny else "y"
            if e > 0 and a["snap"][z] is None:
                return
            cm = ce = ZERO
            for fl in (fx_, fy):
                left = m
                for _p, n, c in fl:
                    t = min(n, left)
                    cm += c * t / n
                    left -= t
                    if n > t:
                        ce += c * (n - t) / n
            proceeds = sold = ZERO
            if e > 0:
                zt = self.legs[z]
                snap = a["snap"][z]
                for p in sorted(snap, reverse=True):
                    s = snap[p] - v.used_bid.get((zt, p), ZERO)
                    if s <= 0:
                        continue
                    t = min(s, e - sold)
                    proceeds += t * self.terms.of(p)[3]
                    sold += t
                    v.used_bid[(zt, p)] = v.used_bid.get((zt, p), ZERO) + t
                    if sold == e:
                        break
            held = e - sold
            wz = D(self.won[self.legs[z]]) if e > 0 else ZERO
            a.update({"nx": nx, "ny": ny, "m": m, "e": e, "sold": sold, "held": held, "cost": cm + ce,
                      "proceeds": proceeds, "settled": True,
                      "pnl": m * self.counted - cm - ce + proceeds + held * wz,
                      "pnl_realized": m * self.realized - cm - ce + proceeds + held * wz})
            v.next_settle += 1

    def resolve(self, m, ts_ns):
        d = self.due.get(m)
        if d is not None and d < ts_ns:
            due = None
            for v in self.vs:
                if not v.queries:
                    continue
                keep, blocked, done = [], False, False
                for q in v.queries:
                    if q["market"] == m and not blocked and q["tau"] < ts_ns:
                        self.do_query(v, q)
                        self.pending -= 1
                        done = True
                    else:
                        if q["market"] == m:
                            blocked = True
                            due = q["tau"] if due is None else min(due, q["tau"])
                        keep.append(q)
                v.queries = keep
                if done:
                    self.settle(v)
            if due is None:
                del self.due[m]
            else:
                self.due[m] = due
        if self.rq and self.rq[0]["tau"] < ts_ns:
            keep = []
            for r in self.rq:
                if r["tau"] < ts_ns and self.mk[r["token"]] == m:
                    self.compare(r)
                else:
                    keep.append(r)
            self.rq = keep

    def resolve_all(self):
        for v in self.vs:
            for q in v.queries:
                self.do_query(v, q)
            v.queries = []
            self.settle(v)
        self.pending = 0
        self.due = {}
        for r in self.rq:
            self.compare(r)
        self.rq = []

    def void_all(self):
        for v in self.vs:
            for q in v.queries:
                v.attempts[q["k"]]["void"] = True
            v.queries = []
            self.settle(v)
        self.pending = 0
        self.due = {}

    # -- G-REBUILD ------------------------------------------------------------------------------------------

    def compare(self, r):
        """A stored reply against the book rebuilt to its own timestamp: compared only where the token's book was
        seeded by a book frame of the current session at or before that timestamp."""
        bk = self.book[r["token"]]
        if bk["seed"] is None or bk["seed"] > r["tau"]:
            self.rb["unseeded"] += 1
            return
        mine = {"bids": list(bk["bids"].items()), "asks": list(bk["asks"].items())}
        theirs = r["book"]
        t14 = tz14()
        a = (t14.best_of(mine), t14.touch_of(mine, r["size"], r["tick"])["bid5"],
             t14.touch_of(mine, r["size"], r["tick"])["ask5"])
        b = (t14.best_of(theirs), t14.touch_of(theirs, r["size"], r["tick"])["bid5"],
             t14.touch_of(theirs, r["size"], r["tick"])["ask5"])
        self.rb["compared"] += 1
        if a == b:
            self.rb["equal"] += 1
        else:
            self.rb["unequal"].append(r["tau"] // MS_NS)
        if sorted(mine["bids"]) == sorted(theirs["bids"]) and sorted(mine["asks"]) == sorted(theirs["asks"]):
            self.rb["full"] += 1

    # -- the capture rule -----------------------------------------------------------------------------------

    def detect(self, rn):
        if not self.span[0] <= rn < self.span[1]:
            return
        bx, by = self.book[self.toks[0]], self.book[self.toks[1]]
        mx, my = self.min_ask(self.toks[0]), self.min_ask(self.toks[1])
        if bx["field"] != mx or by["field"] != my:
            self.inconsistent += 1
            return
        if mx is None or my is None:
            return
        tc = self.terms.c
        tx, ty = tc.get(mx) or self.terms.of(mx), tc.get(my) or self.terms.of(my)
        if tx[0] + ty[0] >= 1:           # below 1 with the fee on top, or no convention is below 1
            return
        sx = sy = None
        for v in self.vs:
            if rn < v.busy_until or v.queries or v.next_settle < len(v.attempts):
                continue
            if (tx[0] + ty[0] if v.top else tx[1] + ty[1]) >= 1:
                continue
            if sx is None:
                sx, sy = sorted(bx["asks"]), sorted(by["asks"])
            lx, ly = Lazy(self.ask_levels(v, self.toks[0], sx)), Lazy(self.ask_levels(v, self.toks[1], sy))
            ax, ay = self.ask5(lx), self.ask5(ly)
            if ax is None or ay is None:
                continue
            c = tz24().classify(ax, ay, 0, 0)
            if not (c["k_top"] < 1 if v.top else c["cls"] == "firm"):
                continue
            i = j = 0
            q = cost = ZERO
            lim = [None, None]
            lvx, lvy = lx.at(0), ly.at(0)
            rx, ry = lvx[1], lvy[1]
            while lvx is not None and lvy is not None and q < Q_CAP:
                mc = self.unit_cost(v, lvx[0]) + self.unit_cost(v, lvy[0])
                if mc >= 1:
                    break
                take = min(rx, ry, Q_CAP - q)
                q += take
                cost += take * mc
                lim = [lvx[0], lvy[0]]
                rx -= take
                ry -= take
                if rx == 0:
                    i += 1
                    lvx = lx.at(i)
                    if lvx is not None:
                        rx = lvx[1]
                if ry == 0:
                    j += 1
                    lvy = ly.at(j)
                    if lvy is not None:
                        ry = lvy[1]
            if q < MIN_SIZE:
                continue
            k = len(v.attempts)
            tm = rn + (v.L + v.delay) * MS_NS
            tu = tm + (2 * v.L + v.delay) * MS_NS
            v.attempts.append({"t": rn, "q": q, "detect": q - cost, "lim": lim, "fills": {"x": None, "y": None},
                               "snap": {"x": None, "y": None}, "void": False, "settled": False})
            for leg, lm in (("x", lim[0]), ("y", lim[1])):
                v.queries.append({"k": k, "kind": "buy", "leg": leg, "limit": lm, "market": self.mk[self.legs[leg]],
                                  "tau": tm})
            for leg in ("x", "y"):
                v.queries.append({"k": k, "kind": "snap", "leg": leg, "limit": None,
                                  "market": self.mk[self.legs[leg]], "tau": tu})
            self.pending += 4
            for mkt in (self.mk[self.legs["x"]], self.mk[self.legs["y"]]):
                if mkt not in self.due or tm < self.due[mkt]:
                    self.due[mkt] = tm
            v.busy_until = rn + (4 * v.L + 2 * v.delay) * MS_NS

    # -- the frames -----------------------------------------------------------------------------------------

    @staticmethod
    def field_of(s):
        p = D(s)
        return None if p >= 1 or p <= 0 else p

    def entry(self, tok, price, size, side, best_ask):
        """One price_change entry: the level set or removed, the token's best ask kept, the venue's own best ask."""
        bk = self.book.get(tok)
        if bk is None:
            return
        p = self.price.get(price)
        if p is None:
            p = self.price[price] = D(price)
        sz = D(size)
        if side == "BUY":
            if sz == 0:
                bk["bids"].pop(p, None)
            else:
                bk["bids"][p] = sz
        else:
            asks = bk["asks"]
            if sz == 0:
                if asks.pop(p, None) is not None and p == bk["amin"]:
                    bk["amin"] = min(asks) if asks else None
            else:
                asks[p] = sz
                a = bk["amin"]
                if a is None or p < a:
                    bk["amin"] = p
        f = self.fields.get(best_ask, _MISS)
        if f is _MISS:
            f = self.fields[best_ask] = self.field_of(best_ask)
        bk["field"] = f

    def side_of(self, levels):
        """A side of a book frame: every level by its price, a later one replacing an earlier, then those of size 0
        removed."""
        pc, side = self.price, {}
        for lv in levels:
            ps = lv["price"]
            p = pc.get(ps)
            if p is None:
                p = pc[ps] = D(ps)
            side[p] = D(lv["size"])
        for p in [p for p, sz in side.items() if sz == 0]:
            del side[p]
        return side

    def apply(self, it):
        if it.get("event_type") == "book":
            t = it["asset_id"]
            if t in self.book:
                bk = self.book[t]
                bk["bids"], bk["asks"] = self.side_of(it["bids"]), self.side_of(it["asks"])
                bk["amin"] = min(bk["asks"]) if bk["asks"] else None
                bk["field"] = bk["amin"]
                if bk["seed"] is None:
                    bk["seed"] = int(it["timestamp"]) * MS_NS
        else:
            for pc in it["price_changes"]:
                self.entry(pc["asset_id"], pc["price"], pc["size"], pc["side"], pc["best_ask"])

    def event(self, o):
        ev = o["event"]
        if ev == "connect":
            self.void_all()
        elif ev == "subscribe":
            self.void_all()
            for bk in self.book.values():
                bk.update({"bids": {}, "asks": {}, "field": None, "seed": None, "amin": None})
        elif ev == "close":
            if o.get("reason") == "end":
                self.resolve_all()
            else:
                self.void_all()

    def run(self, paths):
        markets = set(self.mk.values())
        mine = self.markets
        fast = PC_LINE.fullmatch
        resolve, entry, detect, ms, lag = self.resolve, self.entry, self.detect, MS_NS, self.lag
        for path in paths:
            with gzip.open(path, "rt", encoding="utf-8") as fh:
                for line in fh:
                    mt = fast(line)
                    if mt is not None:
                        self.frames += 1
                        g = mt.groups()
                        m = g[1]
                        if m in markets:
                            vt = int(g[12])
                            k = int(g[0]) // ms - vt
                            lag[k] = lag.get(k, 0) + 1
                            resolve(m, vt * ms)
                            entry(g[2], g[3], g[4], g[5], g[6])
                            entry(g[7], g[8], g[9], g[10], g[11])
                            if m in mine:
                                self.lines += 1
                                detect(int(g[0]))
                        continue
                    if not line.strip():
                        continue
                    o = json.loads(line)
                    if "event" in o:
                        self.event(o)
                        continue
                    raw = o.get("raw")
                    if raw is None or raw == "PONG":
                        self.skipped += 1
                        continue
                    try:
                        fr = json.loads(raw)
                    except ValueError:
                        self.skipped += 1
                        continue
                    self.frames += 1
                    changed = False
                    for it in (fr if isinstance(fr, list) else (fr,)):
                        if not isinstance(it, dict):
                            continue
                        if it.get("event_type") not in ("book", "price_change"):
                            continue
                        m = it.get("market")
                        if m not in markets:
                            continue
                        resolve(m, int(it["timestamp"]) * ms)
                        self.apply(it)
                        if m in mine:
                            changed = True
                    if changed:
                        self.lines += 1
                        detect(o["recv_ns"])
            self.void_all()
        self.rb["unresolved"] = len(self.rq)
        self.rq = []
        return self.results()

    def results(self):
        res = {}
        for v in self.vs:
            at = v.attempts
            done = [a for a in at if a["settled"]]
            res[v.name] = {"attempts": len(at), "void": sum(1 for a in at if a["void"]), "settled": len(done),
                           "q": sum((a["q"] for a in at), ZERO), "detect": sum((a["detect"] for a in at), ZERO),
                           "m": sum((a["m"] for a in done), ZERO), "e": sum((a["e"] for a in done), ZERO),
                           "sold": sum((a["sold"] for a in done), ZERO),
                           "held": sum((a["held"] for a in done), ZERO),
                           "pnl": sum((a["pnl"] for a in done), ZERO),
                           "pnl_realized": sum((a["pnl_realized"] for a in done), ZERO)}
        return res


def window_line(T, name, r, lines, inconsistent):
    """One variant of one window, in the Architect's reference's own format, every figure at 12 places."""
    return "%d %s %d %d %d %s %s %s %s %s %s %s %s %d %d" % (
        T, name, r["attempts"], r["void"], r["settled"], q12(r["q"]), q12(r["detect"]), q12(r["m"]), q12(r["e"]),
        q12(r["sold"]), q12(r["held"]), q12(r["pnl"]), q12(r["pnl_realized"]), lines, inconsistent)


def attempt_lines(T, rp):
    """Every attempt of every variant, for the forensic record of a single window."""
    rows = []
    for v in rp.vs:
        for k, a in enumerate(v.attempts):
            if a["settled"]:
                z = "x" if a["nx"] > a["ny"] else "y"
                rows.append("%d attempt %s %d %d q %s detect %s lim %s/%s nx %s ny %s m %s e %s sold %s held %s "
                            "cost %s proceeds %s pnl %s excess %s won %d" % (
                                T, v.name, k, a["t"], q12(a["q"]), q12(a["detect"]), a["lim"][0], a["lim"][1],
                                q12(a["nx"]), q12(a["ny"]), q12(a["m"]), q12(a["e"]), q12(a["sold"]),
                                q12(a["held"]), q12(a["cost"]), q12(a["proceeds"]), q12(a["pnl"]), z,
                                rp.won[rp.legs[z]] if a["e"] > 0 else 0))
            else:
                rows.append("%d attempt %s %d %d q %s detect %s lim %s/%s void" % (
                    T, v.name, k, a["t"], q12(a["q"]), q12(a["detect"]), a["lim"][0], a["lim"][1]))
    return rows

# ---- a member's terms: its pair, its payoffs and its legs ------------------------------------------------


def member_terms(m, d_hat):
    """The pair bought by the sign of D_hat, the payoff counted a share - 1 where it is dominated by the venue's
    readings, else what it paid - what it paid, each token's outcome, and the four tokens' markets."""
    z = tz24()
    r0, r600, r900 = D(m["R0"]), D(m["R600"]), D(m["R900"])
    pairs_hat = z.pairs_of(d_hat)
    assert len(pairs_hat) == 1, "D_hat zero: no trade"
    pair = pairs_hat[0]
    realized = z.payoff(pair, r0, r600, r900)
    counted = 1 if pair in z.pairs_of(r600 - r0) else realized
    mp = m["map"]
    up15, up5 = m["O15"] == "Up", m["O5"] == "Up"
    won = {mp["m15"]["Up"]: int(up15), mp["m15"]["Down"]: int(not up15),
           mp["m5"]["Up"]: int(up5), mp["m5"]["Down"]: int(not up5)}
    (mx_, ox), (my_, oy) = z.LEGS[pair]
    legs = {"x": mp[mx_][ox], "y": mp[my_][oy]}
    markets = {mp["m15"]["Up"]: mp["m15"]["condition"], mp["m15"]["Down"]: mp["m15"]["condition"],
               mp["m5"]["Up"]: mp["m5"]["condition"], mp["m5"]["Down"]: mp["m5"]["condition"]}
    assert len(set(markets)) == 4 and len(set(markets.values())) == 2, "four tokens of two markets"
    return pair, D(counted), D(realized), won, legs, markets


def rest_queries(m, legs, root=PAIRBOOK):
    """G-REBUILD's queries: every stored reply of the member's two legs that TZ-24's line_check reads valid, at its
    own timestamp, minimum size and tick; the counts of the rest by reason; the lines stored, every token's."""
    z = tz24()
    lines, why = z.read_books(root, m["T"])
    qs, bad = [], {}
    if lines is None:
        return qs, {why: 1}, 0
    for ln in lines:
        if not (isinstance(ln, dict) and ln.get("token_id") in legs.values()):
            continue
        p, info = z.line_check(ln, m["T"], m)
        if p is None and info["ts"] is None:
            p = "timestamp"
        if p is not None:
            bad[p] = bad.get(p, 0) + 1
            continue
        qs.append({"token": ln["token_id"], "tau": info["ts"] * MS_NS, "book": info["book"], "size": info["size"],
                   "tick": info["tick"]})
    return qs, bad, len(lines)

# ---- downloads: one Release asset, by its tag and name, verified by its bytes and SHA-256 ----------------------


def download(tag, asset, nbytes, sha, dest, url_of=None, tries=DL_TRIES, sleep=time.sleep):
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

# ---- the reading ------------------------------------------------------------------------------------------


def blocks_of(pnls):
    """The 8 blocks of 96 consecutive members and each block's sum, in member order."""
    assert len(pnls) == NEED, "%d members" % len(pnls)
    return [sum(pnls[b * BLOCK_N:(b + 1) * BLOCK_N], ZERO) for b in range(BLOCKS)]


def reading(sums, theta=THETA):
    """TZ-30 section 4.4: CAPTURE where every block reaches theta, NO CAPTURE where none does, else UNDECIDABLE."""
    assert len(sums) == BLOCKS
    if all(s >= theta for s in sums):
        return "CAPTURE"
    if all(s < theta for s in sums):
        return "NO CAPTURE"
    return "UNDECIDABLE"


def error_rates():
    """Each answer's false-reading probability, exact under independent blocks, and its power against blocks that
    each reach - or each miss - theta with probability 0.90, 0.95 and 0.99. No data enters."""
    fr = D(1) / D(2) ** BLOCKS
    return fr, {p: D(p) ** BLOCKS for p in ("0.90", "0.95", "0.99")}


def rebuild_reading(served, compared, equal):
    if served == 0 or D(compared) < REBUILD_COMPARED_MIN * served:
        return "FAIL"
    return "PASS" if compared and D(equal) >= REBUILD_EQUAL_MIN * compared else "FAIL"

# ---- units: one window held to the idle stretch, its streams downloaded, replayed and removed -----------------


def stream_index(name):
    m = re.fullmatch(r"stream(?:\.([1-9][0-9]*))?\.jsonl\.gz", name)
    assert m, "a stream file named %r" % name
    return int(m.group(1) or 0)


def run_unit(T, files, dl_dir, replay_fn, timing, holdf=hold, dl=download):
    """One window: started where `holdf` allows, its stream files downloaded and verified by bytes and SHA-256,
    replayed by `replay_fn`, and removed whatever the replay did; its start and end written to `timing`."""
    nbytes = sum(f["bytes"] for f in files)
    budget = 5 + -(-nbytes // DL_RATE) + UNIT_BUDGET_S
    start, waited = holdf(budget)
    free = free_bytes()
    assert free - nbytes >= DISK_FLOOR, "BLOCKED: %d bytes free, %d to download, the floor %d" % (free, nbytes,
                                                                                                  DISK_FLOOR)
    os.makedirs(dl_dir, exist_ok=True)
    paths, retries = [], 0
    t0 = time.time()
    try:
        for f in sorted(files, key=lambda f: stream_index(f["file"])):
            dest = os.path.join(dl_dir, f["asset"])
            _n, _secs, k = dl(f["tag"], f["asset"], f["bytes"], f["sha256"], dest)
            retries += k
            paths.append(dest)
        t1, c1 = time.time(), time.process_time()
        lines = replay_fn(paths)
        cpu = time.process_time() - c1
    finally:
        for p in paths:
            if os.path.exists(p):
                os.remove(p)
    end = time.time()
    W = int(start) // WINDOW * WINDOW
    rec = {"T": T, "window": W, "start_second": round(start - W, 3), "end_second": round(end - W, 3),
           "waited_s": round(waited, 3), "download_s": round(t1 - t0, 3), "replay_s": round(end - t1, 3),
           "cpu_s": round(cpu, 3), "bytes": nbytes, "retries": retries, "budget_s": budget,
           "inside": end <= W + IDLE[1]}
    with open(timing, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, sort_keys=True) + "\n")
    return lines, rec


def timing_summary(path):
    recs = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            recs = [json.loads(ln) for ln in fh if ln.strip()]
    outside = [r for r in recs if not r["inside"]]
    if recs:
        out("units %d: inside the idle stretch %d, ending after second %d %d; longest %.1f s, download %.1f s and "
            "replay %.1f s at most; %.0f s waited; %d bytes downloaded; retries %d; windows %s to %s" % (
                len(recs), len(recs) - len(outside), IDLE[1], len(outside),
                max(r["end_second"] - r["start_second"] for r in recs), max(r["download_s"] for r in recs),
                max(r["replay_s"] for r in recs), sum(r["waited_s"] for r in recs), sum(r["bytes"] for r in recs),
                sum(r["retries"] for r in recs), utc(min(r["window"] for r in recs)),
                utc(max(r["window"] for r in recs))))
    for r in outside:
        out("unit %d started at second %.1f of window %d and ended at second %.1f" % (
            r["T"], r["start_second"], r["window"], r["end_second"]))
    return recs, outside


def lag_quantiles(hist):
    """Of a histogram of whole milliseconds: the count, the nearest-rank 50th, 90th and 99th percentiles, the least
    and the largest, in integers alone."""
    n = sum(hist.values())
    if n == 0:
        return 0, None, None, None, None, None
    ks = sorted(hist)
    ranks = [-(-q * n // 100) for q in (50, 90, 99)]
    got, c = [], 0
    for k in ks:
        c += hist[k]
        while len(got) < 3 and c >= ranks[len(got)]:
            got.append(k)
    return n, got[0], got[1], got[2], ks[0], ks[-1]


def member_unit(m, paths, root=PAIRBOOK, rest_fn=rest_queries, strikes="live"):
    """A member's lines: its pair and payoffs, the seven variants in the reference's format, G-REBUILD's counts,
    the frames read, and every attempt."""
    T = m["T"]
    d_hat = D(m["D_hat"]) if strikes == "live" else D(m["D"])
    pair, counted, realized, won, legs, markets = member_terms(m, d_hat)
    rest, bad, nlines = rest_fn(m, legs, root) if rest_fn else ([], {}, 0)
    rp = Replay(T, legs, markets, counted, realized, won, rest)
    res = rp.run(paths)
    p = res["primary"]
    lines = ["%d member pair %s counted %s realized %s D %s D_hat %s" % (T, pair, counted, realized, m["D"], fx(d_hat))]
    lines += [window_line(T, name, res[name], rp.lines, rp.inconsistent) for name, *_ in VARIANTS]
    lines.append("%d pnl %s %s" % (T, fx(p["pnl"]), fx(p["pnl_realized"])))
    rb = rp.rb
    lines.append("%d rebuild lines %d valid %d compared %d equal %d full %d unseeded %d unresolved %d bad %s "
                 "unequal_ms %s" % (T, nlines, len(rest), rb["compared"], rb["equal"], rb["full"], rb["unseeded"],
                                    rb["unresolved"], json.dumps(bad, sort_keys=True, separators=(",", ":")),
                                    json.dumps(rb["unequal"][:8])))
    lines.append("%d frames %d skipped %d" % (T, rp.frames, rp.skipped))
    lines.append("%d lag frames %s p50 %s p90 %s p99 %s min %s max %s" % ((T,) + lag_quantiles(rp.lag)))
    lines += attempt_lines(T, rp)
    return lines


def parse_unit(T, text):
    """A member's unit file, read back: the primary variant's exact result, every variant's line, the rebuild
    counts. Asserts the file is the member's and whole."""
    rows = text.split("\n")
    assert rows[-1] == "" and rows[0].startswith("%d member " % T), "unit %d: not whole" % T
    got = {"variants": {}, "T": T}
    for ln in rows[:-1]:
        f = ln.split(" ")
        assert int(f[0]) == T, "unit %d: a line of %s" % (T, f[0])
        if f[1] in dict((v[0], 1) for v in VARIANTS):
            got["variants"][f[1]] = f
        elif f[1] == "pnl":
            got["pnl"], got["pnl_realized"] = D(f[2]), D(f[3])
        elif f[1] == "rebuild":
            kv = dict(zip(f[2:16:2], f[3:17:2]))
            got["rebuild"] = {k: int(kv[k]) for k in ("lines", "valid", "compared", "equal", "full", "unseeded",
                                                      "unresolved")}
        elif f[1] == "member":
            got["pair"], got["counted"] = f[3], D(f[5])
        elif f[1] == "lag":
            got["lag"] = {k: (None if v == "None" else int(v)) for k, v in zip(f[2::2], f[3::2])}
        elif f[1] == "attempt" and f[2] == "primary" and f[-1] != "void":
            kv = dict(zip(f[5::2], f[6::2]))
            got["held_cf"] = got.get("held_cf", ZERO) - D(kv["proceeds"]) + D(kv["sold"]) * int(kv["won"])
    assert len(got["variants"]) == len(VARIANTS) and "pnl" in got and "rebuild" in got and "lag" in got, \
        "unit %d: incomplete" % T
    return got

# ---- modes -----------------------------------------------------------------------------------------------------


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
    for rel, sha in sorted(FROZEN.items()):
        assert any(r[0] == "research/" + rel and r[3] == "frozen" and r[4] == sha for r in rows), \
            "%s: not the map's frozen row" % rel
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d; the %d files this instrument executes are frozen rows" % (
            MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"], states["reported"],
            len(FROZEN)))


def still_reading(before, now, recs, since_ns):
    """G-STILL: PASS where both units are unchanged; or where the recorder is unchanged, the pair book active, and
    every restart of it since `since_ns` is the archive's own - one ledger restart record a restart, each record's
    stopped pid the pid before it, the last record's pid and NRestarts the unit's now. FAIL otherwise."""
    if now == before:
        return "PASS", []
    pb0, pb1 = before["pairbook"], now["pairbook"]
    if now["recorder"] != before["recorder"] or pb1["ActiveState"] != "active":
        return "FAIL", []
    rs = [r for r in recs if r.get("event") == "restart" and type(r.get("wall_ns")) is int and r["wall_ns"] >= since_ns]
    if not rs or int(pb1["NRestarts"]) - int(pb0["NRestarts"]) != len(rs):
        return "FAIL", rs
    pid = pb0["MainPID"]
    for r in rs:
        if str(r.get("stopped")) != pid:
            return "FAIL", rs
        pid = str(r.get("pid"))
    return ("PASS" if pid == pb1["MainPID"] and str(rs[-1].get("NRestarts")) == pb1["NRestarts"] else "FAIL"), rs


def mode_still():
    st = load_state()
    now = {}
    for key, unit in sorted(UNITS.items()):
        kv = show(unit, ["MainPID", "NRestarts", "ActiveState", "MemoryCurrent", "MemoryPeak"])
        now[key] = {k: kv[k] for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, MemoryCurrent %s, MemoryPeak %s" % (unit, now[key], kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    for unit in (ARCHIVE_TIMER, ARCHIVE_UNIT):
        out("%s %s" % (unit, show(unit, ["ActiveState", "SubState", "UnitFileState", "Result"])))
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "at_ns": time.time_ns(), "units": now}
        save_state(st)
        out("still: recorded")
        return
    before = st["still"]["units"]
    recs = [] if now == before else ledger_records()[1]
    rd, rs = still_reading(before, now, recs, st["still"]["at_ns"])
    for r in rs:
        out("the archive's restart since %s: run %s, window %s, pid %s after %s, NRestarts %s, at %s" % (
            st["still"]["at"], r.get("run"), r.get("W"), r.get("pid"), r.get("stopped"), r.get("NRestarts"),
            utc(r["wall_ns"] / 1e9)))
    out("G-STILL %s: %s since %s" % (rd, "unchanged" if now == before else (
        "changed by the archive's own restarts alone" if rd == "PASS" else "changed"), st["still"]["at"]))


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


def ledger_summary(recs):
    """The archive's runs from its own records: each run's events, set, Release, removal, restart, resume and
    terminal record, and whether it began on the calendar; whether the archive is halted."""
    runs, order = {}, []
    for r in recs:
        a = r.get("run")
        if a not in runs:
            runs[a] = []
            order.append(a)
        runs[a].append(r)
    lines = []
    for a in order:
        rs = runs[a]
        ev = [r.get("event") for r in rs]
        term = [e for e in ev if e in ("complete", "empty", "halt")]
        sec = a % 86400 if isinstance(a, int) else None
        when = "calendar" if sec == ARCHIVE_CALENDAR_S else ("off-calendar, second %s of the day" % sec)
        parts = ["run %s %s, %s: %d records; terminal %s" % (a, utc(a) if isinstance(a, int) else "-", when, len(rs),
                                                            term[-1] if term else "none")]
        for r in [r for r in rs if r.get("event") == "set"][-1:]:
            parts.append("set %s: %s files, %s bytes, windows %s to %s" % (
                r.get("tag"), r.get("assets_n"), r.get("bytes_total"), r.get("first_T"), r.get("last_T")))
        for r in [r for r in rs if r.get("event") == "restart"][-1:]:
            parts.append("restart: window %s, pid %s after %s, NRestarts %s" % (r.get("W"), r.get("pid"),
                                                                              r.get("stopped"), r.get("NRestarts")))
        for r in [r for r in rs if r.get("event") == "complete"][-1:]:
            parts.append("complete: requests %s, started outside %s, ended outside %s, rate %s a day" % (
                r.get("requests"), r.get("started_outside"), r.get("ended_outside"), r.get("rate_per_day")))
        for r in rs:
            if r.get("event") in ("deferred", "halt", "refused", "timer-disabled"):
                parts.append("%s in %s: %s" % (r.get("event"), r.get("phase"), r.get("reason", r.get("exit"))))
        lines.append("; ".join(parts))
    flags = [r.get("event") for r in recs if r.get("event") in ("halt", "clear")]
    return {"runs": order, "lines": lines, "halted": bool(flags) and flags[-1] == "halt",
            "terminal": {a: [r.get("event") for r in runs[a] if r.get("event") in ("complete", "empty", "halt")]
                         for a in order}}


def mode_archive():
    """The archive's ledger read whole, every record printed; every complete run's set.json asserted by its set
    record; the asset map: every window it covers, its files and bytes, and every window missing (G-ASSETS)."""
    for unit in (ARCHIVE_TIMER, ARCHIVE_UNIT):
        out("%s %s" % (unit, show(unit, ["ActiveState", "SubState", "UnitFileState", "Result", "ExecMainStatus",
                                         "LastTriggerUSec", "NextElapseUSecRealtime"])))
    raw, recs, tail = ledger_records()
    out("ledger %s: %d bytes sha256 %s, %d complete records, %d bytes of a line still written" % (
        ARCHIVE_LEDGER, len(raw), sha256_bytes(raw), len(recs), len(tail)))
    for r in recs:
        out("L %s %s" % (utc(r["wall_ns"] / 1e9), json.dumps(r, sort_keys=True)))
    summ = ledger_summary(recs)
    for ln in summ["lines"]:
        out(ln)
    sets = archived_sets(recs)
    for s in sets:
        d = s["doc"]
        out("set of run %d: %s, %d assets, %d bytes, windows %d to %d, sha256 %s" % (
            s["run"], s["tag"], d["assets_n"], d["bytes_total"], d["first_T"], d["last_T"], s["sha256"]))
    amap = asset_map(sets)
    ts = sorted(amap)
    missing = [t for t in range(ts[0], ts[-1] + 1, WINDOW) if t not in amap]
    multi = [t for t in ts if len(amap[t]) > 1]
    tags = sorted(ln.split("\t")[1][len("refs/tags/"):] for ln in git(
        "ls-remote", "origin", "refs/tags/pairbook-streams-*", tree=PRIMARY).split("\n") if "\t" in ln)
    out("tags on origin %d; the sets' tags not on origin %s" % (len(tags), sorted({s["tag"] for s in sets} - set(tags))))
    out("runs %d; complete %d; without a terminal record %s; halted %s" % (
        len(summ["runs"]), len(sets), [a for a, t in summ["terminal"].items() if not t], summ["halted"]))
    out("G-ASSETS: %d windows %d to %d, %d stream files, %d bytes; windows with more than one file %s; windows "
        "missing between %s" % (len(ts), ts[0], ts[-1], sum(len(v) for v in amap.values()),
                                sum(x["bytes"] for v in amap.values() for x in v.values()), multi, missing))
    inside = [t for t in ts if FIRST_T <= t <= LAST_T]
    out("the candidates %d to %d: %d windows moved, %d bytes; %s" % (
        FIRST_T, LAST_T, len(inside), sum(x["bytes"] for t in inside for x in amap[t].values()),
        "every window to %d moved" % LAST_T if ts[-1] >= LAST_T else
        "moved to %d; fetch waits for the archive until %s" % (ts[-1], utc(ARCHIVE_WAIT_UNTIL))))
    return amap


def archived_to():
    """The asset map of every complete run, and the last window it reaches."""
    _raw, recs, _tail = ledger_records()
    amap = asset_map(archived_sets(recs))
    return amap, max(amap)


def wait_archive(clock=time.time, sleep=time.sleep, read=archived_to):
    """Until the archive has moved every window to LAST_T: its ledger read again every 60 s, BLOCKED at
    ARCHIVE_WAIT_UNTIL. Returns the asset map and the seconds waited."""
    t0 = clock()
    amap, last = read()
    said = None
    while last < LAST_T:
        now = clock()
        assert now < ARCHIVE_WAIT_UNTIL, "BLOCKED: the archive has moved windows to %d, below %d, at %s" % (
            last, LAST_T, utc(now))
        if said is None or now - said >= 1800:
            out("the archive has moved windows to %d; the candidates end at %d; its ledger read again every 60 s "
                "until %s" % (last, LAST_T, utc(ARCHIVE_WAIT_UNTIL)))
            said = now
        sleep(60)
        amap, last = read()
    return amap, clock() - t0


def mode_fetch():
    """The candidates: the 936 windows from FIRST_T to LAST_T, once the archive has moved every one of them, by
    TZ-24's set rule over the pair book's window.json and both settled documents - the walk held to the idle
    stretch - and then TZ-30's stream conditions and the documents' order size. No price of the store is read."""
    floor_check()
    z = tz24()
    amap, waited = wait_archive()
    out("the archive has moved windows to %d, at or after %d, after %.0f s waited" % (max(amap), LAST_T, waited))
    ts = list(range(FIRST_T, LAST_T + 1, WINDOW))
    base = os.path.join(WORK, "fetch")
    os.makedirs(base, exist_ok=True)
    if not os.path.exists(os.path.join(base, "set.json")):
        start, waited = hold(FETCH_BUDGET_S)
        out("the walk starts at second %d of window %d after %.0f s held; %d candidates %d to %d" % (
            int(start) % WINDOW, int(start) // WINDOW * WINDOW, waited, len(ts), ts[0], ts[-1]))
    s = z.form_set(base, PAIRBOOK, ts, gamma_retry, chainbook=True, budget_s=FETCH_BUDGET_S)
    assert [t for t, _st in s["considered"]] == ts, "fetch: TZ-24's walk considered other windows"
    by = cached_docs(os.path.join(base, "docs"))
    rows = []
    for t, status in s["considered"]:
        files = []
        if status == "member":
            w = window_json(t)
            why = stream_problem(w, t, amap) or order_size_problem(by, t)
            if why is None:
                files = [dict(amap[t][f], file=f) for f in w["stream"]["files"]]
                status = "candidate"
            else:
                status = why
        rows.append({"T": t, "status": status, "files": files})
    doc = {"first": ts[0], "last": ts[-1], "considered": rows, "tz24_set_sha": sha256_file(os.path.join(base,
                                                                                                         "set.json"))}
    write_once(os.path.join(base, "candidates.json"), dumps(doc).encode("utf-8"))
    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    out("FETCH: %d windows considered, %d to %d; by status %s" % (len(rows), ts[0], ts[-1],
                                                                 json.dumps(counts, sort_keys=True)))


def mode_strikes():
    """The strikes, live, of each candidate in order, and the set: the first NEED windows whose two strikes the
    recorder published and the host received in time (G-SET)."""
    floor_check()
    config, analyze, pfair = strike_modules()
    base = os.path.join(WORK, "fetch")
    cand = load_json(os.path.join(base, "candidates.json"))
    assert cand["tz24_set_sha"] == sha256_file(os.path.join(base, "set.json")), "strikes: not fetch's set"
    by = {m["T"]: m for m in load_json(os.path.join(base, "set.json"))["members"]}
    considered, members = [], []
    for c in cand["considered"]:
        if len(members) == NEED:
            break
        t, status = c["T"], c["status"]
        if status == "candidate":
            s0, why0 = strike_of(t, t, config, analyze, pfair)
            s6, why6 = strike_of(t + 600, t, config, analyze, pfair)
            if why0 or why6:
                status = "strike: " + (why0 or why6)
            elif s6["value"] == s0["value"]:
                status = "strike: D_hat zero"
            else:
                m = dict(by[t], files=c["files"], D_hat=fx(s6["value"] - s0["value"]),
                         strikes={"R0_hat": fx(s0["value"]), "R0_ts_ms": s0["ts_ms"], "R0_recv_ns": s0["recv_ns"],
                                  "R600_hat": fx(s6["value"]), "R600_ts_ms": s6["ts_ms"],
                                  "R600_recv_ns": s6["recv_ns"]})
                members.append(m)
                status = "member"
        considered.append([t, status])
        assert len(considered) - len(members) <= NONMEMBER_MAX, \
            "BLOCKED: %d non-members before the %dth member" % (len(considered) - len(members), NEED)
    assert len(members) == NEED, "BLOCKED: %d members among the %d candidates" % (len(members), len(considered))
    ts = [m["T"] for m in members]
    s = {"first_T": FIRST_T, "need": NEED, "considered": considered, "members": members,
         "member_list_sha": sha256_bytes(("\n".join(map(str, ts)) + "\n").encode())}
    path = os.path.join(WORK, "b3-set.json")
    sha = write_once(path, dumps(s).encode("utf-8"))
    st = load_state()
    st["set_sha"], st["set_at"] = sha, utc(time.time())
    save_state(st)
    agree = sum(1 for m in members if (D(m["D_hat"]) > 0) == (D(m["D"]) > 0))
    dev = sorted(abs(D(m["D_hat"]) - D(m["D"])) for m in members)
    lag = sorted(m["strikes"]["R600_recv_ns"] - m["strikes"]["R600_ts_ms"] * MS_NS for m in members)
    fr, pw = error_rates()
    out("G-SET PASS: %d members of %d considered, %d to %d, member list sha256 %s, %s sha256 %s" % (
        len(members), len(considered), ts[0], ts[-1], s["member_list_sha"], path, sha))
    for b in range(BLOCKS):
        blk = ts[b * BLOCK_N:(b + 1) * BLOCK_N]
        out("block %d: %d members, %d (%s) to %d (%s)" % (b + 1, len(blk), blk[0], utc(blk[0]), blk[-1], utc(blk[-1])))
    out("non-members %d: %s" % (len(considered) - len(members),
                               json.dumps(sorted([t, w] for t, w in considered if w != "member"))))
    days = {}
    for t in ts:
        days[weekday(t)] = days.get(weekday(t), 0) + 1
    out("members by weekday %s; pair A %d, B %d by D_hat" % (json.dumps(days, sort_keys=True),
                                                             sum(1 for m in members if D(m["D_hat"]) > 0),
                                                             sum(1 for m in members if D(m["D_hat"]) < 0)))
    out("barred: the sign of D_hat agrees with D's at %d of %d; |D_hat - D| median %s, max %s USD; the strike at "
        "T + 600 received a median %d ms, at most %d ms, after its publication" % (
            agree, len(members), fx(dev[(len(dev) - 1) // 2]), fx(dev[-1]), lag[(len(lag) - 1) // 2] // MS_NS,
            lag[-1] // MS_NS))
    out("each answer's false-reading probability %s under independent blocks; power %s" % (
        fx(fr), json.dumps({k: fx(v) for k, v in pw.items()}, sort_keys=True)))


def rehearsal_members(base):
    """TZ-27's 51 windows, their documents fetched through TZ-24's walk with no chain book, held to the idle
    stretch; every one a member with the venue's readings and tokens."""
    with open(TZ27_SET, "rb") as fh:
        raw = fh.read()
    assert sha256_bytes(raw) == TZ27_SET_SHA, "TZ-27's set.json in the forensic store"
    doc = json.loads(raw)
    assert doc["tag"] == TZ27_TAG and tuple(x["T"] for x in doc["assets"]) == REHEARSAL_TS and all(
        x["file"] == "stream.jsonl.gz" for x in doc["assets"]), "TZ-27's set: 51 windows, one file each"
    os.makedirs(base, exist_ok=True)
    if not os.path.exists(os.path.join(base, "set.json")):
        hold(FETCH_BUDGET_S)
    s = tz24().form_set(base, None, list(REHEARSAL_TS), gamma_retry, chainbook=False, budget_s=FETCH_BUDGET_S)
    assert len(s["members"]) == len(REHEARSAL_TS), "G-REHEARSAL: %d members of 51" % len(s["members"])
    files = {x["T"]: [dict(x, tag=TZ27_TAG)] for x in doc["assets"]}
    return s["members"], files


def mode_rehearse():
    floor_check()
    base = os.path.join(WORK, "rehearsal")
    members, files = rehearsal_members(base)
    lines, timing = [], os.path.join(base, "rehearsal-timing.jsonl")
    for m in members:
        unit, _rec = run_unit(m["T"], files[m["T"]], os.path.join(base, "streams"),
                              lambda paths: member_unit(m, paths, rest_fn=None, strikes="published"), timing)
        lines += [ln for ln in unit if ln.split(" ")[1] in dict((v[0], 1) for v in VARIANTS)]
    timing_summary(timing)
    body = ("\n".join(lines) + "\n").encode()
    sha = write_once(os.path.join(base, "rehearsal-lines.txt"), body)
    totals = {}
    for ln in lines:
        f = ln.split(" ")
        t = totals.setdefault(f[1], [0, ZERO])
        t[0] += int(f[2])
        t[1] += D(f[11])
    checks = {"lines": len(lines) == REF["lines"], "digest": sha == REF["digest"]}
    for name, (att, pnl) in sorted(totals.items()):
        want = REF["totals"].get(name)
        checks["totals " + name] = want == [att, q12(pnl)]
        out("G-REHEARSAL %-8s attempts %d, pnl %s; the Architect's %s" % (name, att, q12(pnl), want))
    out("G-REHEARSAL lines %d, the Architect's %d; sha256 %s, the Architect's %s" % (len(lines), REF["lines"], sha,
                                                                                    REF["digest"]))
    bad = sorted(k for k, v in checks.items() if not v)
    assert not bad, "G-REHEARSAL FAIL: %s" % bad
    out("G-REHEARSAL PASS: %d of %d - %d lines byte for byte and %d variants' totals equal to the Architect's" % (
        len(checks), len(checks), len(lines), len(totals)))


def the_set():
    path = os.path.join(WORK, "b3-set.json")
    st = load_state()
    sha = sha256_file(path)
    assert sha == st.get("set_sha"), "the set %s is not the one state.json records" % sha
    s = load_json(path)
    assert len(s["members"]) == NEED and s["first_T"] == FIRST_T, "the set"
    return s, sha


def score_units(members, udir, timing, cpu_max):
    """Every member's unit not already on disk; after the first PROJECT_AFTER of this run, the replays' processor
    time projected over every member's bytes, BLOCKED above cpu_max."""
    os.makedirs(udir, exist_ok=True)
    total = sum(f["bytes"] for m in members for f in m["files"])
    t0, done, cpu, nb = time.time(), 0, 0.0, 0
    out("units to replay %d, %d bytes of streams in all" % (len(members), total))
    for m in members:
        path = os.path.join(udir, "%d.txt" % m["T"])
        if os.path.exists(path):
            continue
        unit, rec = run_unit(m["T"], m["files"], os.path.join(WORK, "streams"),
                             lambda paths: member_unit(m, paths), timing)
        write_atomic(path, ("\n".join(unit) + "\n").encode("utf-8"))
        done += 1
        cpu += rec["cpu_s"]
        nb += rec["bytes"]
        if done == PROJECT_AFTER:
            proj = cpu / nb * total
            out("projected %.0f s of replay for %d bytes after %d units at %.4f s a megabyte" % (
                proj, total, done, cpu / nb * 1e6))
            assert proj <= cpu_max, "BLOCKED: replay projected at %.0f s, above %d" % (proj, cpu_max)
        if done % 24 == 0:
            out("units %d this run, %.0f s" % (done, time.time() - t0))


def mode_score():
    floor_check()
    s, sha = the_set()
    head = git("rev-parse", "HEAD")
    assert "origin/" + BRANCH in git("branch", "-r", "--contains", head).split(), \
        "score: HEAD %s is not on origin" % head
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(dumps({"at": utc(time.time()), "mode": "score", "head": head, "members": len(s["members"]),
                        "member_list_sha": s["member_list_sha"], "set_sha": sha}))
    udir = os.path.join(WORK, "score", "units")
    score_units(s["members"], udir, os.path.join(WORK, "score", "score-timing.jsonl"), SCORE_CPU_MAX)
    timing_summary(os.path.join(WORK, "score", "score-timing.jsonl"))
    rows, h = [], hashlib.sha256()
    wpath = os.path.join(WORK, "score", "b3-windows.txt")
    with open(wpath + ".new", "wb") as wfh:
        for m in s["members"]:
            with open(os.path.join(udir, "%d.txt" % m["T"]), "rb") as fh:
                data = fh.read()
            rows.append(parse_unit(m["T"], data.decode("utf-8")))
            h.update(data)
            wfh.write(data)
    wsha = h.hexdigest()
    if os.path.exists(wpath):
        os.remove(wpath + ".new")
        assert sha256_file(wpath) == wsha, "determinism: %s differs from the first run" % wpath
        out("unchanged %s sha256 %s" % (wpath, wsha))
    else:
        os.replace(wpath + ".new", wpath)
        out("wrote %s %d bytes sha256 %s" % (wpath, os.path.getsize(wpath), wsha))
    rb = {k: sum(r["rebuild"][k] for r in rows) for k in rows[0]["rebuild"]}
    g_rebuild = rebuild_reading(rb["valid"], rb["compared"], rb["equal"])
    out("G-REBUILD %s: stored replies %d, valid %d, compared %d (%s of valid), equal at the touch %d (%s of compared), "
        "every level equal %d; not compared: unseeded %d, unresolved %d" % (
            g_rebuild, rb["lines"], rb["valid"], rb["compared"], q12(D(rb["compared"]) / max(rb["valid"], 1)),
            rb["equal"], q12(D(rb["equal"]) / max(rb["compared"], 1)), rb["full"], rb["unseeded"], rb["unresolved"]))
    lg = [r["lag"] for r in rows if r["lag"]["frames"]]
    p50s, p99s = sorted(x["p50"] for x in lg), sorted(x["p99"] for x in lg)
    lagd = {"members": len(lg), "frames": sum(x["frames"] for x in lg), "p50_median": p50s[(len(p50s) - 1) // 2],
            "p99_median": p99s[(len(p99s) - 1) // 2], "p99_max": p99s[-1], "max": max(x["max"] for x in lg),
            "min": min(x["min"] for x in lg), "p99_above_1000": sum(1 for v in p99s if v > 1000)}
    out("the capture's lag, a price_change frame's host receipt less its venue stamp, over %d members and %d frames: "
        "the median member's median %d ms; its 99th percentile %d ms at the median member and %d ms at the worst, "
        "above 1,000 ms at %d members; the longest %d ms, the least %d ms" % (
            lagd["members"], lagd["frames"], lagd["p50_median"], lagd["p99_median"], lagd["p99_max"],
            lagd["p99_above_1000"], lagd["max"], lagd["min"]))
    pnls = [r["pnl"] for r in rows]
    sums = blocks_of(pnls)
    ts = [r["T"] for r in rows]
    for b, sm in enumerate(sums):
        out("block %d: %d to %d, S %s USDC, %s theta %s" % (b + 1, ts[b * BLOCK_N], ts[(b + 1) * BLOCK_N - 1], q12(sm),
                                                           "at or above" if sm >= THETA else "below", fx(THETA)))
    rd = reading(sums)
    diag = diagnostics(rows, sums)
    fr, pw = error_rates()
    doc = {"reading": rd if g_rebuild == "PASS" else None, "g_rebuild": g_rebuild, "rebuild": rb, "lag": lagd,
           "blocks": [{"first": ts[b * BLOCK_N], "last": ts[(b + 1) * BLOCK_N - 1], "S": sums[b],
                       "reached": sums[b] >= THETA} for b in range(BLOCKS)],
           "theta": THETA, "false_reading": fr, "power": pw, "windows_sha": wsha, "set_sha": sha, "barred": diag}
    write_once(os.path.join(WORK, "score", "b3-reading.json"), dumps(doc).encode("utf-8"))
    assert g_rebuild == "PASS", "G-REBUILD FAIL: the reading is not read"
    out("B3 READING: %s" % rd)


def diagnostics(rows, sums):
    """Barred from every reading: every variant's totals, the touch's ceiling, the band's bonus, the windows with
    an attempt, and each block without its single most influential member."""
    tot = {}
    for name, *_ in VARIANTS:
        f = [r["variants"][name] for r in rows]
        tot[name] = {"attempts": sum(int(x[2]) for x in f), "void": sum(int(x[3]) for x in f),
                     "q": sum((D(x[5]) for x in f), ZERO), "detect": sum((D(x[6]) for x in f), ZERO),
                     "m": sum((D(x[7]) for x in f), ZERO), "e": sum((D(x[8]) for x in f), ZERO),
                     "sold": sum((D(x[9]) for x in f), ZERO), "held": sum((D(x[10]) for x in f), ZERO),
                     "pnl": sum((D(x[11]) for x in f), ZERO), "pnl_realized": sum((D(x[12]) for x in f), ZERO),
                     "windows_with_attempts": sum(1 for x in f if int(x[2]) > 0)}
        t = tot[name]
        out("barred: %-8s attempts %d, void %d, windows with an attempt %d; shares sought %s, bought matched %s, "
            "excess %s of which sold %s, held %s; the touch's ceiling %s; P&L %s USDC, with the band's bonus %s" % (
                name, t["attempts"], t["void"], t["windows_with_attempts"], q12(t["q"]), q12(t["m"]), q12(t["e"]),
                q12(t["sold"]), q12(t["held"]), q12(t["detect"]), q12(t["pnl"]), q12(t["pnl_realized"])))
    loo = []
    for b in range(BLOCKS):
        blk = rows[b * BLOCK_N:(b + 1) * BLOCK_N]
        top = max(blk, key=lambda r: r["pnl"]) if sums[b] >= THETA else min(blk, key=lambda r: r["pnl"])
        rest = sums[b] - top["pnl"]
        loo.append({"block": b + 1, "T": top["T"], "pnl": top["pnl"], "S_without": rest,
                    "flips": (rest >= THETA) != (sums[b] >= THETA)})
        out("barred: block %d without its most influential member %d (%s USDC): S %s, %s" % (
            b + 1, top["T"], q12(top["pnl"]), q12(rest), "its side flips" if loo[-1]["flips"] else "its side holds"))
    hold = sum((r.get("held_cf", ZERO) for r in rows), ZERO)
    out("barred: primary's excess held to settlement instead of sold: P&L %s USDC" % q12(tot["primary"]["pnl"] + hold))
    out("barred: the reading with each block's most influential member removed: %s" % reading(
        [x["S_without"] for x in loo]))
    pn = sorted(r["pnl"] for r in rows)
    out("barred: per member P&L min %s, median %s, max %s; members above zero %d, below %d, at zero %d" % (
        q12(pn[0]), q12(pn[(len(pn) - 1) // 2]), q12(pn[-1]), sum(1 for x in pn if x > 0), sum(1 for x in pn if x < 0),
        sum(1 for x in pn if x == 0)))
    return {"totals": tot, "leave_one_out": loo}


def mode_rescore():
    """Every RESCORE_EVERY-th member from a second download and a second replay; each unit file byte for byte the
    score's."""
    floor_check()
    s, sha = the_set()
    head = git("rev-parse", "HEAD")
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(dumps({"at": utc(time.time()), "mode": "rescore", "head": head, "set_sha": sha}))
    chosen = s["members"][::RESCORE_EVERY]
    udir = os.path.join(WORK, "rescore", "units")
    score_units(chosen, udir, os.path.join(WORK, "rescore", "rescore-timing.jsonl"), RESCORE_CPU_MAX)
    timing_summary(os.path.join(WORK, "rescore", "rescore-timing.jsonl"))
    same = 0
    for m in chosen:
        a = sha256_file(os.path.join(WORK, "score", "units", "%d.txt" % m["T"]))
        b = sha256_file(os.path.join(udir, "%d.txt" % m["T"]))
        same += a == b
        if a != b:
            out("rescore: %d differs, %s against %s" % (m["T"], a, b))
    assert same == len(chosen), "DETERMINISM FAIL: %d of %d" % (same, len(chosen))
    out("DETERMINISM PASS: %d of %d members' unit files byte for byte the score's" % (same, len(chosen)))


def report_tokens():
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8", errors="replace") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    return tree == WORK and (rel in ("state.json", "label-ledger.jsonl", "b3-set.json") or rel.startswith("logs/"))


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
            owner = [p for p, s_, _a in procs if s_ - 1 <= b <= s_ + LIVE_S]
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

# ---- the self-test's window: a synthetic stream the Architect's reference has replayed -----------------------

SYN_T = 1792000800
SYN = {"m15": {"Up": "15001", "Down": "15002", "condition": "0x" + "a1" * 32},
       "m5": {"Up": "5001", "Down": "5002", "condition": "0x" + "b2" * 32}}


def _lv(levels):
    return [{"price": p, "size": s} for p, s in levels]


def _book(tok, cond, ts, bids, asks):
    """A book frame as the venue sends it: bids ascending, asks descending."""
    return {"event_type": "book", "asset_id": tok, "market": cond, "timestamp": str(ts), "hash": "h",
            "bids": _lv(sorted(bids, key=lambda z: D(z[0]))), "asks": _lv(sorted(asks, key=lambda z: -D(z[0])))}


def _pc(cond, ts, entries):
    """A price_change frame in the venue's own key order."""
    return {"market": cond, "price_changes": [{"asset_id": tok, "price": p, "size": s, "side": side, "hash": "0a1b",
                                               "best_bid": bb, "best_ask": ba} for tok, side, p, s, bb, ba in entries],
            "timestamp": str(ts), "event_type": "price_change"}


def synth_frames(T=SYN_T, mp=SYN):
    """Two stream files of one window: the first ends with no close, the second with the stream's end. Each entry
    is (host seconds after T, an event or a frame). The venue's timestamps are milliseconds after T * 1000."""
    c15, c5 = mp["m15"]["condition"], mp["m5"]["condition"]
    x, xc, yc, y = mp["m15"]["Up"], mp["m15"]["Down"], mp["m5"]["Up"], mp["m5"]["Down"]
    v = lambda s: T * 1000 + int(round(s * 1000))

    def books(s, xb, xa, yb, ya):
        return [_book(x, c15, v(s), xb, xa), _book(xc, c15, v(s), [("0.49", "100")], [("0.56", "200")]),
                _book(yc, c5, v(s), [("0.48", "100")], [("0.53", "300")]), _book(y, c5, v(s), yb, ya)]

    def session(t, b):
        return [(t, {"event": "connect", "seg": 0}), (t + 0.05, {"event": "open", "seg": 0, "status": 101}),
                (t + 0.1, {"event": "subscribe", "seg": 0}), (t + 0.224, b)]

    first = session(594.9, books(595.1, [("0.44", "200"), ("0.45", "50")],
                                 [("0.47", "20"), ("0.48", "100"), ("0.50", "500")],
                                 [("0.47", "100"), ("0.48", "100")], [("0.50", "50"), ("0.51", "300")])) + [
        (600.0, _pc(c5, v(599.99), [(yc, "BUY", "0.49", "10", "0.49", "0.53"), (y, "SELL", "0.51", "300", "0.48", "0.50")])),
        (610.0, _pc(c5, v(609.98), [(y, "SELL", "0.45", "30", "0.48", "0.45"), (yc, "BUY", "0.49", "10", "0.49", "0.53")])),
        (610.12, _pc(c5, v(610.10), [(y, "SELL", "0.45", "0", "0.48", "0.50"), (yc, "BUY", "0.49", "10", "0.49", "0.53")])),
        (610.17, _pc(c5, v(610.16), [(y, "BUY", "0.48", "120", "0.48", "0.50"), (yc, "SELL", "0.53", "300", "0.49", "0.53")])),
        (610.30, _pc(c15, v(610.28), [(x, "BUY", "0.46", "40", "0.46", "0.47"), (xc, "SELL", "0.54", "40", "0.49", "0.54")])),
        (610.38, _pc(c5, v(610.36), [(y, "SELL", "0.50", "40", "0.48", "0.50"), (yc, "BUY", "0.49", "10", "0.49", "0.53")])),
        (610.52, _pc(c15, v(610.50), [(x, "SELL", "0.49", "10", "0.46", "0.47"), (xc, "BUY", "0.49", "100", "0.49", "0.54")])),
        (611.00, _pc(c5, v(610.99), [(yc, "BUY", "0.49", "11", "0.49", "0.53"), (y, "SELL", "0.51", "300", "0.48", "0.50")])),
        (611.10, _pc(c15, v(611.08), [(xc, "BUY", "0.49", "101", "0.49", "0.54"), (x, "SELL", "0.50", "500", "0.46", "0.47")])),
        (612.00, _pc(c15, v(611.99), [(x, "BUY", "0.46", "15", "0.46", "0.47"), (xc, "BUY", "0.49", "101", "0.49", "0.54")])),
        (612.50, _pc(c5, v(612.49), [(y, "SELL", "0.40", "8", "0.48", "0.40"), (yc, "BUY", "0.49", "11", "0.49", "0.53")])),
        (620.00, {"event": "close", "seg": 0, "reason": "closed", "code": 1006})] + session(
        621.0, books(621.2, [("0.45", "50"), ("0.46", "40")], [("0.47", "20"), ("0.52", "100")],
                     [("0.48", "120")], [("0.44", "10"), ("0.50", "40")])) + [
        (621.5, _pc(c15, v(621.48), [(xc, "BUY", "0.49", "102", "0.49", "0.56"), (x, "SELL", "0.52", "100", "0.46", "0.47")])),
        (621.6, _pc(c5, v(621.58), [(yc, "BUY", "0.49", "12", "0.49", "0.53"), (y, "SELL", "0.50", "40", "0.48", "0.44")])),
        (622.0, _pc(c15, v(621.99), [(xc, "BUY", "0.49", "103", "0.49", "0.56"), (x, "BUY", "0.46", "41", "0.46", "0.47")])),
        (622.1, _pc(c5, v(622.09), [(yc, "BUY", "0.49", "13", "0.49", "0.53"), (y, "BUY", "0.48", "121", "0.48", "0.44")])),
        (623.0, _pc(c15, v(622.99), [(x, "SELL", "0.47", "20", "0.46", "0.46"), (xc, "BUY", "0.49", "104", "0.49", "0.56")])),
        (650.0, _pc(c5, v(649.99), [(yc, "BUY", "0.49", "14", "0.49", "0.53"), (y, "BUY", "0.48", "122", "0.48", "0.44")]))]
    second = session(700.0, books(700.2, [("0.30", "3")], [("0.47", "60"), ("0.49", "100")],
                                  [("0.48", "50")], [("0.46", "80"), ("0.60", "10")])) + [
        (700.42, _pc(c5, v(700.41), [(y, "SELL", "0.46", "40", "0.48", "0.46"), (yc, "BUY", "0.49", "15", "0.49", "0.53")])),
        (700.46, _pc(c15, v(700.45), [(x, "SELL", "0.47", "30", "0.30", "0.47"), (xc, "BUY", "0.49", "105", "0.49", "0.56")])),
        (700.51, _pc(c5, v(700.50), [(y, "SELL", "0.46", "0", "0.48", "0.60"), (yc, "BUY", "0.49", "15", "0.49", "0.53")])),
        (701.0, _pc(c15, v(700.99), [(xc, "BUY", "0.49", "105", "0.49", "0.56"), (x, "BUY", "0.30", "3", "0.30", "0.47")])),
        (701.1, _pc(c5, v(701.09), [(y, "SELL", "0.46", "70", "0.48", "0.46"), (yc, "BUY", "0.49", "15", "0.49", "0.53")])),
        (701.3, _pc(c15, v(701.29), [(x, "SELL", "0.47", "60", "0.30", "0.47"), (xc, "BUY", "0.49", "106", "0.49", "0.56")])),
        (701.4, _pc(c5, v(701.39), [(y, "SELL", "0.46", "0", "0.48", "0.60"), (yc, "BUY", "0.49", "16", "0.49", "0.53")])),
        (701.6, _pc(c15, v(701.59), [(xc, "BUY", "0.49", "107", "0.49", "0.56"), (x, "BUY", "0.31", "2", "0.31", "0.47")])),
        (701.7, _pc(c5, v(701.69), [(yc, "BUY", "0.49", "17", "0.49", "0.53"), (y, "BUY", "0.47", "5", "0.48", "0.60")])),
        (702.5, _pc(c15, v(702.49), [(xc, "BUY", "0.49", "108", "0.49", "0.56"), (x, "BUY", "0.32", "1", "0.32", "0.47")])),
        (702.6, _pc(c5, v(702.59), [(yc, "BUY", "0.49", "18", "0.49", "0.53"), (y, "BUY", "0.47", "6", "0.48", "0.60")])),
        (894.9, _pc(c5, v(894.89), [(y, "SELL", "0.40", "20", "0.48", "0.40"), (yc, "BUY", "0.49", "19", "0.49", "0.53")])),
        (895.0, {"event": "ping", "seg": 0}),
        (905.0, {"event": "close", "seg": 0, "reason": "end", "code": None}), (905.01, {"event": "end"})]
    return first, second


def synth_stream(dirpath, T=SYN_T, mp=SYN):
    """The two files of synth_frames, in the pair book's line format, deterministic gzip."""
    paths = []
    for name, rows in zip(("%d-stream.jsonl.gz" % T, "%d-stream.1.jsonl.gz" % T), synth_frames(T, mp)):
        lines = []
        for s, obj in rows:
            rn = (T * 1000 + int(round(s * 1000))) * MS_NS
            if "event" in obj:
                lines.append(json.dumps(dict({"recv_ns": rn, "mono_ns": rn}, **obj), separators=(",", ":")))
            else:
                lines.append(json.dumps({"recv_ns": rn, "mono_ns": rn,
                                         "raw": json.dumps(obj, separators=(", ", ":"))}, separators=(",", ":")))
        lines.append(json.dumps({"recv_ns": 0, "mono_ns": 0, "raw": "PONG"}, separators=(",", ":")))
        p = os.path.join(dirpath, name)
        with open(p, "wb") as fh:
            fh.write(gzip.compress(("\n".join(lines) + "\n").encode(), mtime=0))
        paths.append(p)
    return paths

# the seven lines the Architect's reference wrote over synth_stream's two files (TZ-30 section 4.1)
SYN_REF = (
    "1792000800 primary 6 1 5 171.119000000000 5.508807559060 96.122000000000 67.333000000000 31.845000000000 "
    "35.488000000000 18.540534385237 18.540534385237 32 2",
    "1792000800 L0 5 1 4 142.253000000000 5.110794699991 105.744000000000 28.845000000000 28.845000000000 "
    "0.000000000000 1.886621526168 1.886621526168 32 2",
    "1792000800 L25 5 1 4 142.253000000000 5.110794699991 105.744000000000 28.845000000000 28.845000000000 "
    "0.000000000000 1.886621526168 1.886621526168 32 2",
    "1792000800 L100 6 1 5 171.119000000000 5.509228226488 96.122000000000 67.333000000000 31.845000000000 "
    "35.488000000000 18.540534385237 18.540534385237 32 2",
    "1792000800 L250 5 1 4 142.253000000000 5.494603647967 28.768000000000 105.821000000000 31.845000000000 "
    "73.976000000000 36.347672380189 36.347672380189 32 2",
    "1792000800 nodelay 5 1 4 142.253000000000 5.110794699991 134.589000000000 0.000000000000 0.000000000000 "
    "0.000000000000 4.464478386168 4.464478386168 32 2",
    "1792000800 top 6 1 5 178.000000000000 5.974884000000 100.000000000000 70.000000000000 33.000000000000 "
    "37.000000000000 19.538590000000 19.538590000000 32 2")
SYN_D = {"R0": "100000.25", "R600": "100010.5", "R900": "100020.75", "D": "10.25", "O15": "Up", "O5": "Up"}


def syn_member(d_hat="10.25", r900="100020.75"):
    up15 = D(r900) >= D(SYN_D["R0"])
    up5 = D(r900) >= D(SYN_D["R600"])
    return {"T": SYN_T, "R0": SYN_D["R0"], "R600": SYN_D["R600"], "R900": r900, "D": SYN_D["D"],
            "O15": "Up" if up15 else "Down", "O5": "Up" if up5 else "Down", "D_hat": d_hat,
            "map": {m: dict(SYN[m]) for m in SYN}}


def mode_selftest():
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    tmp = os.path.join(WORK, "selftest-tmp")
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.makedirs(tmp)
    z, t14 = tz24(), tz14()
    # the frozen files, as loaded
    ok(z.__file__ == os.path.join(HERE, "tz24-nesting-b2.py") and sys.modules["tz24nestingb2"] is z,
       "TZ-24's instrument executed from its asserted bytes beside this file")
    ok(getcontext().prec == 60 and z.D is D and t14.D is D, "every sum at 60 digits, one Decimal")
    ok(t14.fee_pp(D("0.50")) == D("0.0175") and t14.fee_pp(D("0.85")) == D("0.008925") and
       t14.fee_pp(D("0.90")) == D("0.0063"), "TZ-14's fee at CANON section 1.1's three points")
    ok(z.LEGS == {"A": (("m15", "Up"), ("m5", "Down")), "B": (("m5", "Up"), ("m15", "Down"))} and
       z.pairs_of(D(1)) == ["A"] and z.pairs_of(D(-1)) == ["B"] and z.pairs_of(D(0)) == ["A", "B"],
       "TZ-24's legs and its dominated pair by the sign of D")
    # the terms of every price on the venue's finest grid, against TZ-24's own costs
    terms = Terms()
    bad = 0
    for i in range(1, 1000):
        p = D(i) / 1000
        top, shares, npg, sale = terms.of(p)
        f = t14.fee_pp(p)
        bad += not (top == p + f and shares == p / npg and npg == 1 - f / p and sale == p - f and
                    (top, shares) == z.costs(p))
    ok(bad == 0, "at 999 prices from 0.001 to 0.999: TZ-24's two costs, a net share's cost under the fee in shares "
                 "equal to the price over its net shares a gross share, and a sale's proceeds the price less the fee")
    c = z.classify(D("0.47"), D("0.45"), 0, 0)
    c2 = z.classify(D("0.50"), D("0.50"), 0, 0)
    ok(c["cls"] == "firm" and c["k_shares"] == terms.of(D("0.47"))[1] + terms.of(D("0.45"))[1] and
       c2["cls"] == "none", "classify at no skew: firm below 1 with the fee in shares, none above")
    # q12
    ok(q12(D("-0.0000000000001")) == "0.000000000000" and q12(D("1.0000000000005")) == "1.000000000000" and
       q12(D("1.0000000000015")) == "1.000000000002" and q12(D("-2.5")) == "-2.500000000000",
       "12 places, half to even, no sign on zero")
    # the replay over the synthetic window, against the Architect's reference
    paths = synth_stream(tmp)
    pair, counted, realized, won, legs, markets = member_terms(syn_member(), D("10.25"))
    ok(pair == "A" and counted == 1 and realized == 1 and legs == {"x": "15001", "y": "5002"} and
       won == {"15001": 1, "15002": 0, "5001": 1, "5002": 0}, "pair A by D_hat, counted 1, its legs and outcomes")
    mb = syn_member(d_hat="-3")
    pb = member_terms(mb, D("-3"))
    ok(pb[0] == "B" and pb[1] == z.payoff("B", D(mb["R0"]), D(mb["R600"]), D(mb["R900"])) == 1 and
       pb[4] == {"x": "5001", "y": "15002"}, "a wrong sign of D_hat buys B, and B is counted at what it paid")
    mband = syn_member(d_hat="-3", r900="100005")
    ok(member_terms(mband, D("-3"))[1] == 0, "B bought where A is dominated pays 0 inside the band, and counts 0")
    v = lambda s: (SYN_T * 1000 + int(round(s * 1000))) * MS_NS
    same = {"bids": [(D("0.44"), D("200")), (D("0.45"), D("50"))],
            "asks": [(D("0.47"), D("20")), (D("0.48"), D("100")), (D("0.50"), D("500"))]}
    rest = [{"token": "15001", "tau": v(610.25), "book": same, "size": D(5), "tick": D("0.01")},
            {"token": "5002", "tau": v(610.13), "book": {"bids": [(D("0.47"), D("100")), (D("0.48"), D("100"))],
                                                         "asks": [(D("0.50"), D("50")), (D("0.51"), D("300"))]},
             "size": D(5), "tick": D("0.01")},
            {"token": "15001", "tau": v(611.5), "book": same, "size": D(5), "tick": D("0.01")},
            {"token": "15001", "tau": v(620.5), "book": same, "size": D(5), "tick": D("0.01")},
            {"token": "5002", "tau": v(621.3), "book": {"bids": [(D("0.48"), D("120"))],
                                                        "asks": [(D("0.44"), D("10")), (D("0.50"), D("40"))]},
             "size": D(5), "tick": D("0.01")},
            {"token": "15001", "tau": v(904.0), "book": {"bids": [], "asks": []}, "size": D(5), "tick": D("0.01")}]
    fastn = slown = 0
    for pth in paths:
        with gzip.open(pth, "rt", encoding="utf-8") as fh:
            for line in fh:
                mt = PC_LINE.fullmatch(line)
                if mt is None:
                    slown += 1
                    continue
                o = json.loads(line)
                fr = json.loads(o["raw"])
                g = mt.groups()
                want = (str(o["recv_ns"]), fr["market"]) + tuple(
                    x for pc in fr["price_changes"] for x in (pc["asset_id"], pc["price"], pc["size"], pc["side"],
                                                              pc["best_ask"])) + (fr["timestamp"],)
                fastn += g == want and fr["event_type"] == "price_change" and len(fr["price_changes"]) == 2
    ok(fastn == 29 and slown == 18, "the fast path: 29 price_change lines read as json reads them, 18 other lines "
                                    "left to json")
    rp = Replay(SYN_T, legs, markets, counted, realized, won, rest)
    res = rp.run(paths)
    lines = tuple(window_line(SYN_T, name, res[name], rp.lines, rp.inconsistent) for name, *_ in VARIANTS)
    for ln in lines:
        out("      " + ln)
    ok(lines == SYN_REF, "the replay of the synthetic window: its seven lines equal the Architect's reference")
    ok(rp.lag == {10: 21, 20: 8} and lag_quantiles(rp.lag) == (29, 10, 20, 20, 10, 20) and
       lag_quantiles({}) == (0, None, None, None, None, None) and
       lag_quantiles({-3: 1, 5: 98, 4000: 1}) == (100, 5, 5, 5, -3, 4000),
       "the lag: each price_change frame's receipt less its venue stamp, 29 frames, nearest-rank percentiles")
    ok(rp.rb["queries"] == 6 and rp.rb["compared"] == 5 and rp.rb["equal"] == 3 and rp.rb["full"] == 3 and
       rp.rb["unseeded"] == 1 and rp.rb["unresolved"] == 0 and
       rp.rb["unequal"] == [v(611.5) // MS_NS, v(904.0) // MS_NS],
       "G-REBUILD: three replies equal at their own instants, two that differ found, one inside a gap not compared")
    # the reading
    fr, pw = error_rates()
    ok(fr == D("0.00390625") and pw["0.90"] == D("0.43046721") and pw["0.95"] == D("0.6634204312890625") and
       pw["0.99"] == D("0.9227446944279201"), "each answer at 2^-8, power 0.9^8, 0.95^8, 0.99^8")
    ok(reading([D(10)] * 8) == "CAPTURE" and reading([D("9.99")] * 8) == "NO CAPTURE" and
       reading([D(10)] * 7 + [D("9.99")]) == "UNDECIDABLE" and reading([D(-50)] * 7 + [D(11)]) == "UNDECIDABLE",
       "CAPTURE where every block reaches 10, NO CAPTURE where none does, UNDECIDABLE otherwise")
    sums = blocks_of([D(i % 3) for i in range(NEED)])
    ok(len(sums) == 8 and sums[0] == sum(D(i % 3) for i in range(96)) and
       sums[7] == sum(D(i % 3) for i in range(672, 768)), "8 blocks of 96 consecutive members")
    ok(rebuild_reading(100, 90, 89) == "PASS" and rebuild_reading(100, 89, 89) == "FAIL" and
       rebuild_reading(100, 100, 97) == "FAIL" and rebuild_reading(0, 0, 0) == "FAIL",
       "G-REBUILD at 90% compared and 98% equal, and FAIL on nothing")
    # the window's stream conditions
    amap = {SYN_T: {"stream.jsonl.gz": {}}}
    good = {"joined_late": False, "stopped": False, "stream": {
        "opened": True, "off_reason": None, "files": ["stream.jsonl.gz"], "cut": False,
        "subscribed_wall_ns": (SYN_T + 595) * 10 ** 9, "last_frame_wall_ns": (SYN_T + 905) * 10 ** 9,
        "max_gap_ns": 2 * 10 ** 9}}

    def bent(**kw):
        w = json.loads(json.dumps(good))
        for k, val in kw.items():
            (w["stream"] if k in w["stream"] else w)[k] = val
        return stream_problem(w, SYN_T, amap)

    ok(stream_problem(good, SYN_T, amap) is None and bent(cut=True) == "stream: cut" and
       bent(opened=False) == "stream: not opened" and bent(stopped=True) == "stream: joined late or stopped" and
       bent(subscribed_wall_ns=(SYN_T + 601) * 10 ** 9) == "stream: subscribed late" and
       bent(last_frame_wall_ns=(SYN_T + 899) * 10 ** 9) == "stream: ended early" and
       bent(max_gap_ns=15 * 10 ** 9 + 1) == "stream: a gap above 15 s" and
       bent(files=["stream.jsonl.gz", "stream.1.jsonl.gz"]) == "stream: not archived",
       "a member's stream: opened, whole, subscribed by T + 600, to T + 900, no gap above 15 s, every file archived")
    # the archive's record
    st = os.path.join(tmp, "archive")
    os.makedirs(os.path.join(st, "runs", "1792000020"))
    sdoc = {"tag": "pairbook-streams-1792000020", "assets_n": 2, "bytes_total": 30,
            "assets": [{"T": SYN_T, "file": "stream.jsonl.gz", "asset": "%d-stream.jsonl.gz" % SYN_T, "bytes": 10,
                        "sha256": "a" * 64},
                       {"T": SYN_T + 900, "file": "stream.jsonl.gz", "asset": "%d-stream.jsonl.gz" % (SYN_T + 900),
                        "bytes": 20, "sha256": "b" * 64}]}
    raw = json.dumps(sdoc).encode()
    with open(os.path.join(st, "runs", "1792000020", "set.json"), "wb") as fh:
        fh.write(raw)
    recs = [{"event": "start", "run": 1792000020}, {"event": "set", "run": 1792000020, "tag": sdoc["tag"],
                                                     "sha256": sha256_bytes(raw), "assets_n": 2, "bytes_total": 30},
            {"event": "complete", "run": 1792000020}, {"event": "start", "run": 1792000999}]
    sets = archived_sets(recs, st)
    am = asset_map(sets)
    ok(len(sets) == 1 and sorted(am) == [SYN_T, SYN_T + 900] and am[SYN_T]["stream.jsonl.gz"]["tag"] == sdoc["tag"],
       "a complete run's set.json by its set record's SHA-256; a run without a complete record is not a set")
    recs[1]["sha256"] = "c" * 64
    try:
        archived_sets(recs, st)
        caught = False
    except AssertionError:
        caught = True
    ok(caught, "a set.json other than its set record's is a failed assert")
    # the strikes, on a recorder tree of the self-test's own
    config, analyze, pfair = strike_modules(allow_tz24=True)
    root0 = config.ROOT
    config.ROOT = os.path.join(tmp, "recorder")
    try:
        def twap(t0, rows):
            d = config.interval_dir(t0)
            os.makedirs(d, exist_ok=True)
            body = "".join(json.dumps({"recv_ns": rv, "mono_ns": 0, "raw": json.dumps(
                {"type": "update", "payload": {"timestamp": ts, "full_accuracy_value": fav}})}) + "\n"
                           for ts, rv, fav in rows)
            with open(os.path.join(d, "twap60.jsonl.gz"), "wb") as fh:
                fh.write(gzip.compress(body.encode(), mtime=0))
        T = SYN_T
        twap(T, [((T - 1) * 1000, (T + 1) * 10 ** 9, "77000100000000000000000"),
                 (T * 1000 + 400, (T + 2) * 10 ** 9, "77000250000000000000000"),
                 (T * 1000 + 400, T * 10 ** 9 + 1500000000, "77000250000000000000000")])
        twap(T + 600, [((T + 600) * 1000 + 300, (T + 602) * 10 ** 9, "77010500000000000000000")])
        s0, w0 = strike_of(T, T, config, analyze, pfair)
        s6, w6 = strike_of(T + 600, T, config, analyze, pfair)
        ok(w0 is None and s0["value"] == D("77000.25") and s0["ts_ms"] == T * 1000 + 400 and
           s0["recv_ns"] == T * 10 ** 9 + 1500000000 and w6 is None and s6["value"] == D("77010.5"),
           "a strike: pfair's price to beat, its report's own time and the earliest line that carried it")
        twap(T + 600, [((T + 600) * 1000 + 300, (T + 606) * 10 ** 9, "77010500000000000000000")])
        ok(strike_of(T + 600, T, config, analyze, pfair)[1] == "received after T + 605",
           "a strike received after T + 605 is not known live")
        twap(T + 600, [((T + 600) * 1000 + 2001, (T + 603) * 10 ** 9, "77010500000000000000000")])
        ok(strike_of(T + 600, T, config, analyze, pfair)[1].startswith("published 2001 ms"),
           "a strike published more than 2 s after its boundary is not one")
        twap(T + 600, [((T + 599) * 1000, (T + 599) * 10 ** 9, "77010500000000000000000")])
        ok(strike_of(T + 600, T, config, analyze, pfair)[1].startswith("no report"), "no report at or after it")
    finally:
        config.ROOT = root0
    # downloads, against a server on this host's loopback
    import http.server
    import threading
    blob = b"stream bytes " * 1000
    hits = []

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            hits.append((self.path, self.headers.get("User-Agent")))
            if self.path.endswith("missing"):
                self.send_response(404)
                self.end_headers()
                return
            self.send_response(200)
            self.send_header("Content-Length", str(len(blob)))
            self.end_headers()
            self.wfile.write(blob)

        def log_message(self, *a):
            pass

    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    try:
        url_of = lambda t, a: "http://127.0.0.1:%d/%s/%s" % (srv.server_port, t, a)
        dest = os.path.join(tmp, "a.gz")
        r = download("tag", "asset", len(blob), sha256_bytes(blob), dest, url_of=url_of, sleep=lambda s: None)
        with open(dest, "rb") as fh:
            ok(r[0] == len(blob) and fh.read() == blob and hits[-1][1] == UA and not os.path.exists(dest + ".part"),
               "an asset downloaded whole, by its bytes and SHA-256, under btc-5m-twap-tz30")
        try:
            download("tag", "asset", len(blob), "0" * 64, os.path.join(tmp, "b.gz"), url_of=url_of, tries=2,
                     sleep=lambda s: None)
            caught = False
        except AssertionError as e:
            caught = "BLOCKED" in str(e) and not os.path.exists(os.path.join(tmp, "b.gz"))
        ok(caught, "an asset whose SHA-256 is not its set's is asked for again, then BLOCKED, and never kept")
    finally:
        srv.shutdown()
    # units: held, downloaded, replayed and removed
    t = [1792000800 + 600.0]

    def fake_dl(tag, asset, nbytes, sha, dest):
        shutil.copyfile(os.path.join(tmp, asset), dest)
        return nbytes, 0.0, 0

    timing = os.path.join(tmp, "timing.jsonl")
    files = [{"tag": "x", "asset": os.path.basename(p), "file": os.path.basename(p).split("-", 1)[1], "bytes": 1,
              "sha256": "a"} for p in paths]
    unit, rec = run_unit(SYN_T, files[::-1], os.path.join(tmp, "dl"),
                         lambda ps: member_unit(syn_member(), ps, rest_fn=None), timing,
                         holdf=lambda b: (t[0], 0.0), dl=fake_dl)
    got = parse_unit(SYN_T, "\n".join(unit) + "\n")
    ok(tuple(" ".join(got["variants"][name]) for name, *_ in VARIANTS) == SYN_REF and
       not os.listdir(os.path.join(tmp, "dl")) and rec["inside"] is False and rec["T"] == SYN_T,
       "a unit: its files in the pair book's order, replayed as the reference did, removed, its time recorded")
    try:
        run_unit(SYN_T, [dict(files[0], bytes=10 ** 15)], os.path.join(tmp, "dl"), lambda ps: [], timing,
                 holdf=lambda b: (t[0], 0.0), dl=fake_dl)
        caught = False
    except AssertionError as e:
        caught = str(e).startswith("BLOCKED") and "to download" in str(e) and not os.listdir(os.path.join(tmp, "dl"))
    ok(caught, "a unit whose files would take the disk below its floor is BLOCKED before its download")
    # the clock
    W = 1792458000
    idle = lambda s="inactive": (lambda: s)
    ok(quiet(W + 14, 60, idle()) is not None and quiet(W + 15, 60, idle()) is None and
       quiet(W + 530, 60, idle()) is None and quiet(W + 531, 60, idle()) is not None and
       quiet(W + 700, 60, idle()) is not None, "a unit of 60 s starts from second 15 to 530 of a window")
    cal = W // 86400 * 86400 + ARCHIVE_CALENDAR_S
    ok(quiet(cal - 5, 60, idle()) is not None and quiet(cal + 61, 60, idle()) is None and
       all(quiet(W + 100, 60, idle(s)) is not None for s in RUNNING) and quiet(W + 100, 60, idle("failed")) is None,
       "nothing starts near the archive's calendar run or while its service runs")
    clock = [W + 600.25]
    tt, waited = hold(60, clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s),
                      state_of=idle())
    ok(int(tt) == W + 915 and 314 <= waited <= 316, "held from second 600, a unit starts at second 15 of the next")
    # the candidates, and fetch's wait for the archive
    ok(LAST_T == 1792548000 and (LAST_T - FIRST_T) // WINDOW + 1 == NEED + NONMEMBER_MAX == 936 and
       ARCHIVE_WAIT_UNTIL == 1792562400, "the candidates: 936 windows, 1791706500 to 1792548000")
    for start, seen, want in ((ARCHIVE_WAIT_UNTIL - 300, [LAST_T - 900, LAST_T - 900, LAST_T], 120),
                              (ARCHIVE_WAIT_UNTIL - 30, [LAST_T - 900] * 5, None)):
        clk = [float(start)]
        try:
            _am, w2 = wait_archive(clock=lambda: clk[0], sleep=lambda s: clk.__setitem__(0, clk[0] + s),
                                   read=lambda: ({}, seen.pop(0)))
            got_w = w2
        except AssertionError as e:
            got_w = "BLOCKED" if str(e).startswith("BLOCKED") else str(e)
        ok(got_w == (want if want is not None else "BLOCKED"),
           "fetch waits for the archive, its ledger read every 60 s: %s" % (
               "it reaches the candidates' last window after 120 s" if want else "BLOCKED at 2026-10-21 06:00 UTC"))
    # G-STILL against the archive's own restarts
    u = lambda pid, n, a="active": {"MainPID": str(pid), "NRestarts": str(n), "ActiveState": a}
    rec = lambda w, pid, stopped, n: {"event": "restart", "run": 1792551620, "W": 1792551600, "pid": pid,
                                      "stopped": stopped, "NRestarts": str(n), "wall_ns": w}
    b0 = {"recorder": u(4148534, 2), "pairbook": u(1942330, 15)}
    one = {"recorder": u(4148534, 2), "pairbook": u(2000001, 16)}
    two = {"recorder": u(4148534, 2), "pairbook": u(2000002, 17)}
    r1, r2 = rec(11, 2000001, 1942330, 16), rec(12, 2000002, 2000001, 17)
    ok(still_reading(b0, b0, [], 10)[0] == "PASS" and still_reading(b0, one, [r1], 10)[0] == "PASS" and
       still_reading(b0, two, [r1, r2], 10)[0] == "PASS" and still_reading(b0, one, [], 10)[0] == "FAIL" and
       still_reading(b0, one, [rec(9, 2000001, 1942330, 16)], 10)[0] == "FAIL" and
       still_reading(b0, two, [r1], 10)[0] == "FAIL" and
       still_reading(b0, one, [rec(11, 2000001, 1942331, 16)], 10)[0] == "FAIL" and
       still_reading(b0, dict(one, recorder=u(4148535, 3)), [r1], 10)[0] == "FAIL" and
       still_reading(b0, dict(one, pairbook=u(2000001, 16, "failed")), [r1], 10)[0] == "FAIL",
       "G-STILL: unchanged, or the pair book changed by the archive's own restarts alone, each in its ledger in order")
    # the hook
    ok(policy("strikes", "open", (RECORDER + "/btc-updown-5m/1792000800/twap60.jsonl.gz", "rb", 0)) is None and
       policy("strikes", "open", (RECORDER + "/btc-updown-5m/1792000800/chainlink.jsonl.gz", "rb", 0)) is not None and
       policy("score", "open", (RECORDER + "/btc-updown-5m/1792000800/twap60.jsonl.gz", "rb", 0)) is not None and
       policy("strikes", "open", (RECORDER + "/runtime.jsonl", "rb", 0)) is not None,
       "the recorder's twap60 by mode strikes alone, and nothing else of the recorder")
    ok(policy("fetch", "open", (PAIRBOOK + "/1791706500/window.json", "rb", 0)) is None and
       policy("fetch", "open", (PAIRBOOK + "/1791706500/books.jsonl.gz", "rb", 0)) is not None and
       policy("score", "open", (PAIRBOOK + "/1791706500/books.jsonl.gz", "rb", 0)) is None and
       policy("score", "open", (PAIRBOOK + "/1791706500/stream.jsonl.gz", "rb", 0)) is not None and
       policy("score", "open", (PAIRBOOK + "/1791705600/window.json", "rb", 0)) is not None and
       policy("score", "open", (PAIRBOOK + "/1791706500/window.json", "wb", 0)) is not None and
       policy("score", "os.listdir", (PAIRBOOK,)) is not None,
       "the pair book's window.json and stored replies of the set's windows, read only; no stream file, no listing")
    ok(policy("archive", "open", (ARCHIVE_LEDGER, "rb", 0)) is None and
       policy("fetch", "open", (ARCHIVE_STATE + "/runs/1791774020/set.json", "rb", 0)) is None and
       policy("fetch", "open", (ARCHIVE_STATE + "/runs/1791774020/verify.json", "rb", 0)) is not None and
       policy("score", "open", (ARCHIVE_LEDGER, "rb", 0)) is not None and
       policy("still", "open", (ARCHIVE_LEDGER, "rb", 0)) is None and
       policy("still", "open", (ARCHIVE_STATE + "/runs/1791774020/set.json", "rb", 0)) is not None and
       policy("archive", "open", (ARCHIVE_LEDGER, "ab", os.O_WRONLY)) is not None,
       "the archive's ledger and set.json files read by archive and fetch, the ledger alone by still, nothing written")
    ok(policy("score", "open", (CHAINBOOK + "/1791241200/window.json", "rb", 0)) is not None and
       policy("reclaim", "open", (FORENSICS + "/x", "xb", 0)) is None and
       policy("reclaim", "open", (FORENSICS + "/x", "wb", 0)) is not None and
       policy("score", "open", ("/root/elsewhere", "wb", 0)) is not None,
       "nothing of the chain book; the forensic store by reclaim's exclusive create; no write outside the work tree")
    ok(policy("score", "urllib.Request", ("https://github.com/x/y", None, {}, "GET")) is None and
       policy("score", "urllib.Request", ("https://gamma-api.polymarket.com/markets", None, {}, "GET")) is not None
       and policy("fetch", "urllib.Request", ("https://gamma-api.polymarket.com/markets", None, {}, "GET")) is None
       and policy("strikes", "urllib.Request", ("https://github.com/x", None, {}, "GET")) is not None and
       policy("score", "subprocess.Popen", ("git", ["git"], None, None)) is None and
       policy("score", "subprocess.Popen", (None, ["kill", "1"], None, None)) is not None,
       "requests to the Releases by the replaying modes, to gamma by fetch and rehearse; git, systemctl, stat alone")
    shutil.rmtree(tmp)
    ok(not os.path.exists(tmp), "the self-test's tree removed")
    del REFUSED[:]
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz30-nesting-b3-measure.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "still": mode_still,
             "archive": mode_archive, "fetch": mode_fetch, "strikes": mode_strikes, "rehearse": mode_rehearse,
             "score": mode_score, "rescore": mode_rescore}
    if mode == "reclaim":
        mode_reclaim(rest)
    elif mode == "scratch":
        assert len(rest) == 1, "scratch OWN"
        mode_scratch(rest[0])
    else:
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
    tzo = _MODS["tz24"].REFUSED if "tz24" in _MODS else []
    out("refused: %d by this file's hook, %d by TZ-24's" % (len(REFUSED), len(tzo)))


if __name__ == "__main__":
    main(sys.argv[1:])
