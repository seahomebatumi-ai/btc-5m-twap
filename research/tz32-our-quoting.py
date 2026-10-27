#!/usr/bin/env python3
"""TZ-32 - W1, our quoting: does a quote of ours at the touch of the five-minute leg, simulated on the pair book's
streams with queue position, the 150 ms taker delay and our own cancels, keep the named makers' edge?

    fingerprint       contract section 1 steps 3 and 4, asserted: the map's revision, anchors and rows
    selftest          every rule of this file, on literals, on synthetic streams and on temporary trees
    still             the recorder's and the pair book's MainPID, NRestarts and ActiveState: the first run
                      records them, the second compares, the archive's own restarts read from its ledger
                      (G-STILL)
    scratch OWN       the UUID directories beside OWN, this session's, each named live or earlier
    archive           the pair book archive's ledger and the set.json of every run, read and printed, and the
                      asset of every stream file the archive has moved
    rehearse          the quoting rule over TZ-27's 51 windows, every unit held to the idle stretch, against the
                      Architect's independent replay (G-REHEARSAL)
    fetch             the candidates from 1792754100, once the archive has moved them: window.json and the
                      five-minute leg's settled document of each, and the set (G-SET)
    replay            label-free: every member's streams downloaded, replayed and removed, every unit held to the
                      idle stretch; the constants, thresholds and power on disk (G-BOOK)
    rescore           every sixteenth member replayed again, from a second download (DETERMINISM)
    score             the labels, read once, and W1's reading
    reclaim TREE...   section 9

It loads research/tz23-maker-m0.py from beside itself, executed from the bytes whose SHA-256 it asserts, and calls
TZ-23's functions for the documents' rule, every request for them, every position, cost and rebate, the thresholds,
the power, the reading and the labels: it writes no second implementation of any of them. Its own code is the replay
of a window's streams - the leg's Up book rebuilt, each match read from the venue's own book frame, our quotes placed,
queued, filled and cancelled at venue time - and the archive's record, the downloads, the units held to the idle
stretch and G-STILL, written again for its own hook. Its requests are TZ-23's to gamma-api.polymarket.com, through
TZ-23's http_json and its two headers; downloads of Release assets from github.com, with User-Agent:
btc-5m-twap-tz32; and git against origin. An audit hook refuses every open, listing, request and process TZ-32
section 2 does not give the running mode. It writes under /root/tz32-work/ and, in reclaim, new files in
/root/btc-forensics/ by exclusive create. It prints sums over a set, and of a single window its figures inside the work
tree alone. Exit 0: every assert of the mode held. Exit 1: an assert failed, and its message names it. Run it with
the recorder's interpreter, /root/tz04a-env.

Written for CryptoTZ/TZ-32-our-quoting.md. The TZ is the specification.
"""

import collections
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
import types
import urllib.error
import urllib.parse
import urllib.request

if not __debug__:
    sys.stderr.write("tz32: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

HERE = os.path.dirname(os.path.abspath(__file__))
TZ23_NAME = "tz23-maker-m0.py"
TZ23_SHA256 = "6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f"


def load_tz23(path):
    """TZ-23's instrument, executed from the very bytes whose SHA-256 is asserted. It installs its audit hook - every
    open under the recorder's and the chain book's roots refused - sets the main thread's decimal precision to 60
    digits and tunes glibc's malloc."""
    with open(path, "rb") as fh:
        raw = fh.read()
    got = hashlib.sha256(raw).hexdigest()
    assert got == TZ23_SHA256, "%s sha256 %s, required %s" % (path, got, TZ23_SHA256)
    mod = types.ModuleType("tz23")
    mod.__file__ = path
    sys.modules["tz23"] = mod
    exec(compile(raw, path, "exec"), mod.__dict__)
    return mod


tz23 = load_tz23(os.path.join(HERE, TZ23_NAME))
D = tz23.D
out, utc, fx, dumps = tz23.out, tz23.utc, tz23.fx, tz23.dumps

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------

MAP_REVISION = "2026-10-23-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 40, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"`?([0-9a-f]{64}|self-reference[^|]*?)`? \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)

WINDOW = 900
W0_LAST = 1792753800         # W0's last member, 2026-10-23 11:10 UTC (TZ-31): no fill of a later market has been read
FIRST_T = 1792754100         # the first window whose five-minute leg, FIRST_T + 600, opens after W0_LAST
NEED = 288                   # members: three days of windows, one leg a window
NONMEMBER_MAX = 62           # the walk is BLOCKED past this many non-members before the 288th member
LAST_T = FIRST_T + (NEED + NONMEMBER_MAX - 1) * WINDOW     # 1793068200: the candidates' last window, 350 in all
ARCHIVE_WAIT_UNTIL = 1793080800    # 2026-10-27 06:00:00 UTC: fetch waits for the archive to reach LAST_T until then
LEG = 600                    # a window's five-minute leg opens at T + 600 and closes at T + 900
MIN_SIZE = 5                 # the venue's minimum order, asserted in every member's document
# The quoting rule (TZ-32 section 1): host seconds after the leg's open, the price band in thousandths, the
# position cap and the order's size in hundredths of a share
PARAMS = {"start": 0, "stop": 295, "p_lo": 50, "p_hi": 950, "x_cap": 2000, "size": 500}
# (name, one-way latency ms, first in its level's queue, departures from the level in proportion, an order that
# crosses ours a taker after the delay): the first two are gated - behind, every assumption against us, for W1-EARN;
# front, every assumption for us, for W1-NO-EARN - and the rest barred from every reading
VARIANTS = (("behind", 50, False, False, True), ("front", 50, True, False, False), ("prop", 50, False, True, True),
            ("behind_nocross", 50, False, False, False), ("front_cross", 50, True, False, True),
            ("L0", 0, False, False, True), ("L100", 100, False, False, True), ("L250", 250, False, False, True),
            ("front_L0", 0, True, False, False))
GATED = ("behind", "front")
ALPHA = D("0.005")           # each answer's false-reading probability
DELTA = tz23.DELTA           # half a tick a share, TZ-23's and W0's bar
LAMBDA = {"behind": D("0.014605"), "front": D("0.016557")}    # fixed before any member is read: TZ-32 section 1
BOOK_EQUAL_MIN = D("0.99")   # G-BOOK: the rebuilt touch equals the venue's own book frame's at 99% of match frames
RESCORE_EVERY = 16           # rescore replays members 0, 16, 32, ...: 18 of 288
REPLAY_CPU_MAX = 3000        # processor seconds the replays may take, projected after their first 24 units
RESCORE_CPU_MAX = 300
REHEARSAL_CPU_MAX = 240
PROJECT_AFTER = 24           # a replay or the rehearsal projects its processor time after its first 24 units,
RESCORE_PROJECT_AFTER = 6    # the rescore, of 18, after its first 6
UNIT_BUDGET_S = 45           # a unit's budget beside its download: replay and deletion
DL_RATE = 2000000            # bytes a second a download is budgeted at, TZ-28's
DL_TRIES = 6
WALK_BUDGET_S = 120          # a request for documents starts no later than second 470
DOC_CHUNK = 20               # TZ-23's chunk: twenty slugs a request
IDLE = (15, 590)             # the pair book's idle stretch: a unit starts at second 15 or later, ends by 590
ARCHIVE_UNIT = "btc-pairbook-archive.service"
ARCHIVE_TIMER = "btc-pairbook-archive.timer"
ARCHIVE_CALENDAR_S = 10820   # the archive's calendar run, 03:00:20 UTC
ARCHIVE_LEAD_S = 60          # nothing starts from budget + 60 s before it to 60 s after it
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")
HOLD_MAX_S = 7200
MEM_FLOOR = 81928192         # MemAvailable: twice the largest peak of any mode the Architect measured (TZ-32 section 0.4)
DISK_FLOOR = 5400000000      # free bytes on /dev/vda2: the pair book's STREAM_FLOOR and this session's (TZ-32 section 0.4)

UA = "btc-5m-twap-tz32"
DL_HEADERS = {"User-Agent": UA, "Accept": "application/octet-stream"}
REPO = "seahomebatumi-ai/btc-5m-twap"
DL_URL = "https://github.com/" + REPO + "/releases/download/%s/%s"
DL_HOSTS = ("github.com", "release-assets.githubusercontent.com", "objects.githubusercontent.com")
GAMMA_HOST = "gamma-api.polymarket.com"
ASSET_RE = re.compile(r"([0-9]{10})-(stream(?:\.[1-9][0-9]*)?\.jsonl\.gz)")
STREAM_FILE_RE = re.compile(r"stream(?:\.[1-9][0-9]*)?\.jsonl\.gz")
SUBSCRIBE_BY_S = 600         # the stream subscribed by T + 600
LAST_FRAME_S = 900           # and its last frame at or after T + 900
GAP_MAX_NS = 15 * 10 ** 9    # with no gap between frames above 15 s

# the rehearsal: TZ-27's 51 windows, its set.json in the forensic store (TZ-27's report), and the Architect's lines
# over them from an independent replay (TZ-32 section 4.1)
REHEARSAL_TS = tuple(range(1791660600, 1791705600 + 1, WINDOW))
TZ27_TAG = "tz-27-pairbook-streams"
TZ27_SET = "/root/btc-forensics/tz27-work--archive--set.json"
TZ27_SET_SHA = "ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd"
REF = {"lines": 135900, "digest": "52b1c637a51d6b7af3c29ba3aadd75a5e2f0d39410969ee15b61155a4fc3ac60", "totals": {
    # fills, shares, X, C, R, V and S over the 51 windows, the labels the legs' settled documents state: 23 Up
    "behind": [7219, "29749.980000000000", "148.620000000000", "186.702990000000", "73.284744755460",
               "14541.894000000000", "-314.048245244540"],
    "front": [26214, "99744.330000000000", "52.850000000000", "88.478290000000", "244.042849013460",
              "14316.016700000000", "-16.225440986540"],
    "prop": [10076, "38817.950000000000", "108.130000000000", "150.934090000000", "94.534436869460",
             "15627.275900000000", "-301.729653130540"],
    "behind_nocross": [7188, "29598.260000000000", "141.500000000000", "176.187790000000", "72.852862339460",
                       "14476.772200000000", "-307.324927660540"],
    "front_cross": [26232, "99839.700000000000", "46.180000000000", "85.580190000000", "244.315285023460",
                    "13867.026400000000", "-9.624904976540"],
    "L0": [9236, "37841.480000000000", "120.560000000000", "246.148810000000", "92.467183565260",
           "13402.157600000000", "-295.291626434740"],
    "L100": [6410, "26551.630000000000", "172.350000000000", "117.943900000000", "65.091487813800",
             "15468.213300000000", "-264.942412186200"],
    "L250": [6636, "28849.690000000000", "57.350000000000", "-59.683100000000", "71.022929390000",
             "16803.875300000000", "-242.283970610000"],
    "front_L0": [32813, "126600.190000000000", "81.090000000000", "153.311610000000", "311.240369556060",
                 "13631.537300000000", "17.878759556060"]}}

WORK = "/root/tz32-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/label-ledger.jsonl"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
BRANCH = "tz-32-our-quoting"
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

# ---- the audit hook: TZ-32 section 2's reads, writes, requests and processes -----------------------------

MODE = [None]
REFUSED = []
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
PB_WINDOW = re.compile(r"/var/lib/btc-pairbook/([0-9]{10})/window\.json")
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
    """None where TZ-32 section 2 allows the event in this mode; otherwise the reason it is refused."""
    if event == "urllib.Request":
        host = urllib.parse.urlsplit(args[0]).hostname if args and isinstance(args[0], str) else None
        if mode in ("rehearse", "replay", "rescore") and host in DL_HOSTS:
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
    if _under(p, CHAINBOOK) or _under(p, RECORDER):
        return "an open under the recorder's or the chain book's root"
    if _under(p, PAIRBOOK):
        m = PB_WINDOW.fullmatch(p)
        if not w and m is not None and FIRST_T <= int(m.group(1)) <= LAST_T and mode == "fetch":
            return None
        return "an open under the pair book's root"
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


def q12(x):
    """A figure for print, half-even to 12 places; every sum and comparison is made on the exact figure."""
    s = fx(D(x).quantize(D("0.000000000001")))
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


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh, parse_float=D)


def load_state():
    return load_json(STATE) if os.path.exists(STATE) else {}


def save_state(st):
    write_atomic(STATE, (json.dumps(st, sort_keys=True, indent=1, default=tz23._dec) + "\n").encode("utf-8"))


def free_bytes(path=WORK):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def floor_check():
    """Before a mode that reads the venue, the archive's Releases or a set: glibc's two settings, the memory and the
    disk floor."""
    assert tz23.MALLOC_TUNED, "BLOCKED: glibc did not take the mmap threshold and the arena count"
    avail, free = tz23.mem_available(), free_bytes()
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
    """Every run whose ledger holds a complete record: its set.json, asserted by the SHA-256 its set record carries,
    its tag, assets and counts against that record."""
    runs, order = {}, []
    for r in recs:
        a = r.get("run")
        if a not in runs:
            runs[a] = []
            order.append(a)
        runs[a].append(r)
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


def ledger_summary(recs):
    """The archive's runs from its own records: each run's events, set, restart and terminal record, and whether it
    began on the calendar; whether the archive is halted."""
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
            parts.append("restart: window %s, pid %s after %s, NRestarts %s" % (
                r.get("W"), r.get("pid"), r.get("stopped"), r.get("NRestarts")))
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

# ---- the set: TZ-32 section 1's rules for a window -------------------------------------------------------------


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


def leg_problem(w, t, doc):
    """The first rule the window's five-minute leg fails, or None: its settled document by TZ-23's qualify, unchanged,
    orderMinSize 5, and its condition and tokens those window.json carries for the leg."""
    if doc is None:
        return "document: absent"
    why = tz23.qualify(t + LEG, doc)
    if why is not None:
        return "document: %s" % why
    v = doc.get("orderMinSize")
    if isinstance(v, bool) or not isinstance(v, (int, D)) or D(v) != MIN_SIZE:
        return "document: order size"
    mk = (w.get("markets") or {}).get("m5") if isinstance(w, dict) else None
    if not isinstance(mk, dict) or mk.get("slug") != "btc-updown-5m-%d" % (t + LEG):
        return "window.json: the leg's slug"
    if not (mk.get("conditionId") == doc["conditionId"] and loads_maybe(mk.get("clobTokenIds")) ==
            json.loads(doc["clobTokenIds"]) and loads_maybe(mk.get("outcomes")) == ["Up", "Down"]):
        return "window.json: the leg's condition or tokens"
    return None


def loads_maybe(v):
    """A field window.json carries verbatim from the venue's document, JSON text inside JSON, parsed; anything else
    as it is (TZ-24's rule)."""
    if isinstance(v, str):
        try:
            return json.loads(v)
        except ValueError:
            return None
    return v


def window_json(t, root=PAIRBOOK):
    with open(os.path.join(root, str(t), "window.json"), "rb") as fh:
        return json.loads(fh.read())


def docs_of(ts, holdf=hold):
    """The settled documents of the five-minute legs of windows ts, TZ-23's gamma_docs in requests of twenty, each
    started inside the idle stretch; by window."""
    by = {}
    for i in range(0, len(ts), DOC_CHUNK):
        chunk = ts[i:i + DOC_CHUNK]
        holdf(WALK_BUDGET_S)
        got = tz23.gamma_docs([t + LEG for t in chunk])
        for t in chunk:
            by[t] = got.get("btc-updown-5m-%d" % (t + LEG))
    return by

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

# ---- the replay: one window's streams, W1's quoting rule (TZ-32 section 1) ----------------------------------

MS_NS = 10 ** 6
PRICE_UNIT = 1000          # a price as an integer of thousandths: the venue prints at most three decimals
SIZE_UNIT = 100            # a book size as an integer of hundredths: the venue prints at most two decimals
TAKER_DELAY_NS = 150 * MS_NS     # the venue's crypto taker delay (CANON section 1.1): a crossing order waits this long
SEND, CANCEL, CROSS = 0, 1, 2
_PRICE = re.compile(r"(0|[1-9][0-9]*)(?:\.([0-9]{1,3}))?")
_SIZE = re.compile(r"(0|[1-9][0-9]*)(?:\.([0-9]{1,2}))?")


_PRICES, _SIZES = {}, {}


def price_int(s):
    """A price's text as an integer of thousandths, exactly; any other text is a failed assert. Each text is parsed
    once and remembered."""
    v = _PRICES.get(s)
    if v is None:
        m = _PRICE.fullmatch(s)
        assert m, "a price %r" % (s,)
        v = _PRICES[s] = int(m.group(1)) * PRICE_UNIT + int((m.group(2) or "").ljust(3, "0"))
    return v


def size_int(s):
    """A book size's text as an integer of hundredths, exactly; any other text is a failed assert. Each text is parsed
    once and remembered, at most 2 ** 16 of them, and forgotten at each window's start."""
    v = _SIZES.get(s)
    if v is None:
        m = _SIZE.fullmatch(s)
        assert m, "a size %r" % (s,)
        v = int(m.group(1)) * SIZE_UNIT + int((m.group(2) or "").ljust(2, "0"))
        if len(_SIZES) < 1 << 16:
            _SIZES[s] = v
    return v


class Order:
    __slots__ = ("side", "p", "s", "q", "state", "done_at", "xing")

    def __init__(self, side, p, s):
        self.side, self.p, self.s, self.q = side, p, s, None
        self.state = "sent"            # sent, then resting, then filled, cancelled or refused
        self.done_at = None            # the venue instant it left the book or was refused
        self.xing = False              # a crossing order is held against it


class Variant:
    """One way of placing the same quotes, replayed beside the others on the same books."""

    def __init__(self, name, L_ms, front=False, prop=False, cross=True):
        self.name, self.L, self.front, self.prop, self.cross = name, L_ms * MS_NS, front, prop, cross
        self.pend, self.seq, self.fills, self.resting = [], 0, [], []
        self.live = {"b": None, "a": None}
        self.n = {"sent": 0, "cancels": 0, "refused": 0, "crossings": 0}
        self.unknown, self.x_known = [], 0

    def fill(self, vt, side, p, f, kind):
        self.fills.append((vt, side, p, f, kind))
        heapq.heappush(self.unknown, (vt, f if side == "b" else -f))

    def known_x(self, h):
        """Up shares, in hundredths, of every fill the host has learned of by h: a fill reaches it L after the venue
        makes it."""
        u = self.unknown
        while u and u[0][0] + self.L <= h:
            self.x_known += heapq.heappop(u)[1]
        return self.x_known

    def _push(self, tau, kind, o, c=0):
        self.seq += 1
        heapq.heappush(self.pend, (tau, self.seq, kind, o, c))

    def send(self, h, side, p, s):
        o = Order(side, p, s)
        self._push(h + self.L, SEND, o)
        self.n["sent"] += 1
        return o

    def cancel(self, h, o):
        self._push(h + self.L, CANCEL, o)
        self.n["cancels"] += 1


class Window:
    """One window's replay, frames in the order the pair book stored them: the five-minute leg's Up book rebuilt,
    every variant's orders placed, filled and cancelled at venue time, and each match's book frame compared with the
    book rebuilt to it (TZ-32 section 1)."""

    def __init__(self, T, params, variants):
        self.T, self.T0, self.pm, self.vs = T, T + 600, params, variants
        self.bids, self.asks = {}, {}
        self.seeded, self.stopped = False, False
        self.block, self.bvt, self.touch0 = [], None, (None, None)
        self.start_ns = (self.T0 + params["start"]) * 10 ** 9
        self.stop_ns = (self.T0 + params["stop"]) * 10 ** 9
        self.c = {"matches": 0, "two_sided": 0, "snapshots": 0, "snapshots_equal": 0, "touch_equal": 0, "sessions": 0,
                  "closes": 0}

    def best(self, side):
        bk = self.bids if side == "b" else self.asks
        if not bk:
            return None
        return max(bk) if side == "b" else min(bk)

    def advance(self, vt_ns):
        """Before a frame of the leg stamped vt_ns: a block of another stamp ends, unmatched; then every variant's
        events due before vt_ns take effect, in their own order, on the book as it stands."""
        if self.block and vt_ns != self.bvt:
            self.close_block(False)
        self.resolve(vt_ns)

    def resolve(self, vt_ns):
        """Every variant's events due before venue instant vt_ns, in the order of their instants: an order arrives -
        refused where it would cross, else resting behind the level's displayed size, or first in it at front - a
        cancel takes its order off, and a crossing order held for the taker delay fills what is left of its own."""
        for v in self.vs:
            P = v.pend
            if not P or P[0][0] >= vt_ns:
                continue
            while P and P[0][0] < vt_ns:
                tau, _seq, kind, o, c = heapq.heappop(P)
                if kind == SEND:
                    opp = self.best("a" if o.side == "b" else "b")
                    if opp is not None and (o.p >= opp if o.side == "b" else o.p <= opp):
                        o.state, o.done_at = "refused", tau
                        v.n["refused"] += 1
                        continue
                    o.q = 0 if v.front else (self.bids if o.side == "b" else self.asks).get(o.p, 0)
                    o.state = "resting"
                    v.resting.append(o)
                elif kind == CANCEL:
                    if o.state in ("sent", "resting"):
                        o.state, o.done_at = "cancelled", tau
                else:
                    o.xing = False
                    if o.state == "resting":
                        f = min(o.s, c)
                        o.s -= f
                        v.fill(tau, o.side, o.p, f, "x")
                        if o.s == 0:
                            o.state, o.done_at = "filled", tau
            v.resting = [o for o in v.resting if o.state == "resting"]

    def sweep(self, side, t0):
        """A match's consumption on `side` from the side's best level at the block's start, t0, outward: each level's
        decrease while every level before it was emptied; [(price, consumed)], the last possibly partial."""
        cur = self.bids if side == "b" else self.asks
        first, dec = {}, {}
        for sd, p, old, new in self.block:
            if sd != side:
                continue
            if p not in first:
                first[p] = old
            dec[p] = first[p] - new
        if dec.get(t0, 0) <= 0:
            return []
        levels = sorted((p for p in set(first) | set(cur) if (p <= t0 if side == "b" else p >= t0)),
                        reverse=(side == "b"))
        out = []
        for p in levels:
            pre = first[p] if p in first else cur.get(p, 0)
            if pre <= 0:
                continue
            c = dec.get(p, 0)
            if c <= 0:
                break
            out.append((p, c))
            if c < pre:
                break
        return out

    def cross_check(self, t):
        """Where the opposite side now reaches a resting order's price, the orders there would have been takers
        against it: one crossing event, at t plus the taker delay, for their displayed size, in a variant that
        counts them."""
        bb, ba = self.best("b"), self.best("a")
        for v in self.vs:
            if not v.cross:
                continue
            for o in v.resting:
                if o.state != "resting" or o.xing:
                    continue
                c = 0
                if o.side == "b" and ba is not None and ba <= o.p:
                    c = sum(s for p, s in self.asks.items() if p <= o.p)
                elif o.side == "a" and bb is not None and bb >= o.p:
                    c = sum(s for p, s in self.bids.items() if p >= o.p)
                if c > 0:
                    o.xing = True
                    v._push(t + TAKER_DELAY_NS, CROSS, o, c)
                    v.n["crossings"] += 1

    def close_block(self, match):
        """The entries sharing one venue stamp end. Where the Up token's book frame with that stamp closes them they
        are a match: every resting order its sweep reaches fills. Then every resting order's queue ahead is held at
        most at its level's displayed size, and the book is checked for crossings."""
        pre, took = {}, {}
        for sd, p, old, _new in self.block:
            pre.setdefault((sd, p), old)
        if match and self.block:
            hit = 0
            for side, t0 in (("b", self.touch0[0]), ("a", self.touch0[1])):
                if t0 is None:
                    continue
                sw = self.sweep(side, t0)
                if not sw:
                    continue
                hit += 1
                last = sw[-1][0]
                at = dict(sw)
                for p, c in sw:
                    took[(side, p)] = c
                for v in self.vs:
                    gone = False
                    for o in v.resting:
                        if o.side != side or o.state != "resting":
                            continue
                        f = 0
                        if (last <= o.p) if side == "b" else (last >= o.p):
                            tot = sum(c for p, c in sw if (p <= o.p if side == "b" else p >= o.p))
                            f = min(o.s, max(0, tot - o.q))
                        o.q = max(0, o.q - at.get(o.p, 0))
                        if f > 0:
                            o.s -= f
                            v.fill(self.bvt, side, o.p, f, "m")
                            if o.s == 0:
                                o.state, o.done_at, gone = "filled", self.bvt, True
                    if gone:
                        v.resting = [o for o in v.resting if o.state == "resting"]
            if hit:
                self.c["matches"] += 1
            if hit == 2:
                self.c["two_sided"] += 1
        for v in self.vs:
            for o in v.resting:
                lv = (self.bids if o.side == "b" else self.asks).get(o.p, 0)
                if v.prop and (o.side, o.p) in pre:
                    left = pre[(o.side, o.p)] - took.get((o.side, o.p), 0)
                    if left > lv and o.q > 0:
                        o.q = o.q * lv // left
                if lv < o.q:
                    o.q = lv
        t = self.bvt
        self.block, self.bvt = [], None
        self.cross_check(t)

    # -- the stream's items, as the replay hands them over --------------------------------------------------------

    def entries(self, vt_ns, ents):
        """The Up token's price_change entries of one frame: each sets or removes one level."""
        assert not self.block or vt_ns == self.bvt, "entries of another stamp inside a block"
        if not self.block:
            self.bvt = vt_ns
            self.touch0 = (self.best("b"), self.best("a"))
        for side, p, s in ents:
            bk = self.bids if side == "b" else self.asks
            old = bk.get(p, 0)
            if s == 0:
                bk.pop(p, None)
            else:
                bk[p] = s
            self.block.append((side, p, old, s))

    def book(self, vt_ns, bids, asks, seed):
        """A book frame of the Up token. A subscription's frame seeds the book; any other closes the block it shares
        a stamp with as a match, is compared with the book rebuilt to it, and replaces it."""
        if seed:
            if self.block:
                self.close_block(False)
            self.seeded = True
        else:
            self.c["snapshots"] += 1
            if self.block:
                self.close_block(vt_ns == self.bvt)
            if bids == self.bids and asks == self.asks:
                self.c["snapshots_equal"] += 1
                self.c["touch_equal"] += 1
            elif touch_of(bids, asks) == touch_of(self.bids, self.asks):
                self.c["touch_equal"] += 1
        self.bids, self.asks = bids, asks
        for v in self.vs:
            for o in v.resting:
                lv = (self.bids if o.side == "b" else self.asks).get(o.p, 0)
                if lv < o.q:
                    o.q = lv
        self.cross_check(vt_ns)

    def session(self, kind, h):
        """connect and subscribe empty the book until the subscription's frame; a close that is not the stream's end
        takes every live order off, the cancels reaching the venue at h + L."""
        if self.block:
            self.close_block(False)
        if kind in ("connect", "subscribe"):
            self.bids, self.asks, self.seeded = {}, {}, False
            if kind == "subscribe":
                self.c["sessions"] += 1
        elif kind == "close":
            self.c["closes"] += 1
            for v in self.vs:
                for side in ("b", "a"):
                    o = v.live[side]
                    if o is not None:
                        v.cancel(h, o)
                        v.live[side] = None

    def stop(self):
        """The host's timer at T0 + stop: every live order of every variant cancelled at that instant, the cancels
        reaching the venue L later; no quote after it."""
        for v in self.vs:
            for side in ("b", "a"):
                o = v.live[side]
                if o is not None:
                    v.cancel(self.stop_ns, o)
                    v.live[side] = None
        self.stopped = True

    def decide(self, h):
        """Every variant's quotes, after a frame of the leg's market reaches the host at h (TZ-32 section 1)."""
        pm = self.pm
        if self.stopped or not self.seeded or h < self.start_ns:
            return
        bb, ba = self.best("b"), self.best("a")
        for v in self.vs:
            x = None
            for side in ("b", "a"):
                o = v.live[side]
                if o is not None and o.done_at is not None and o.done_at + v.L <= h:
                    o = v.live[side] = None
                tgt = None
                if bb is not None and ba is not None:
                    tgt = bb if side == "b" else ba
                    if not pm["p_lo"] <= tgt <= pm["p_hi"]:
                        tgt = None
                if tgt is not None:
                    if x is None:
                        x = v.known_x(h)
                    if x >= pm["x_cap"] if side == "b" else x <= -pm["x_cap"]:
                        tgt = None
                if tgt is None:
                    if o is not None:
                        v.cancel(h, o)
                        v.live[side] = None
                elif o is None:
                    v.live[side] = v.send(h, side, tgt, pm["size"])
                elif o.p != tgt:
                    v.cancel(h, o)
                    v.live[side] = v.send(h, side, tgt, pm["size"])

    def finish(self):
        if self.block:
            self.close_block(False)
        self.resolve(1 << 62)


# A price_change frame as the venue sends it and the pair book stores it, matched whole: two entries, each field a
# run of digits, hex or BUY/SELL, where no escape can occur (TZ-30's PC_LINE, its fields kept for the Up token).
_ENTRY = (r'\{\\"asset_id\\":\\"([0-9]+)\\", \\"price\\":\\"([0-9.]+)\\", \\"size\\":\\"([0-9.]+)\\", '
          r'\\"side\\":\\"(BUY|SELL)\\", \\"hash\\":\\"[0-9a-f]*\\", \\"best_bid\\":\\"[0-9.]+\\", '
          r'\\"best_ask\\":\\"[0-9.]+\\"\}')
PC_LINE = re.compile(r'\{"recv_ns":([0-9]+),"mono_ns":-?[0-9]+,"raw":"\{\\"market\\":\\"(0x[0-9a-f]{64})\\", '
                     r'\\"price_changes\\":\[' + _ENTRY + ', ' + _ENTRY + r'\], \\"timestamp\\":\\"([0-9]+)\\", '
                     r'\\"event_type\\":\\"price_change\\"\}"\}\n?')


def touch_of(bids, asks):
    """A book's touch: the best bid and its size, the best ask and its size, None for an empty side."""
    bb = max(bids) if bids else None
    ba = min(asks) if asks else None
    return bb, bids.get(bb), ba, asks.get(ba)


def side_of(levels):
    """A side of a book frame: every level by its price, a later one replacing an earlier, then those of size 0
    removed (TZ-30's rule)."""
    out = {}
    for lv in levels:
        out[price_int(lv["price"])] = size_int(lv["size"])
    return {p: s for p, s in out.items() if s}


def replay(paths, w, cond, up_token, lag):
    """Every line of the window's stream files, in the order stored, into the Window `w`, the five-minute leg's
    market alone: the host's stop timer fires before the first line received at or after T0 + stop, and the end of
    each file takes every live order off as a close does. Returns the counts of lines read; `lag` gathers, for every
    price_change frame of the leg, its host receipt less its venue stamp in whole milliseconds."""
    n = {"lines": 0, "frames": 0, "leg_frames": 0, "skipped": 0}
    fast = PC_LINE.fullmatch
    last_h = 0
    _SIZES.clear()
    for path in paths:
        with gzip.open(path, "rt", encoding="utf-8") as fh:
            for line in fh:
                n["lines"] += 1
                mt = fast(line)
                if mt is not None:
                    n["frames"] += 1
                    g = mt.groups()
                    h = last_h = int(g[0])
                    if not w.stopped and h >= w.stop_ns:
                        w.stop()
                    if g[1] != cond:
                        continue
                    n["leg_frames"] += 1
                    ms = int(g[10])
                    vt = ms * MS_NS
                    lag[h // MS_NS - ms] = lag.get(h // MS_NS - ms, 0) + 1
                    ents = [("b" if g[j + 3] == "BUY" else "a", price_int(g[j + 1]), size_int(g[j + 2]))
                            for j in (2, 6) if g[j] == up_token]
                    assert len(ents) == 1, "a price_change frame of the leg without one Up entry"
                    w.advance(vt)
                    w.entries(vt, ents)
                    w.decide(h)
                    continue
                if not line.strip():
                    continue
                o = json.loads(line)
                h = o.get("recv_ns")
                assert type(h) is int, "a line without its host receipt"
                last_h = max(last_h, h)
                if not w.stopped and h >= w.stop_ns:
                    w.stop()
                if "event" in o:
                    ev = o["event"]
                    if ev in ("connect", "subscribe") or (ev == "close" and o.get("reason") != "end"):
                        w.session(ev, h)
                    continue
                raw = o.get("raw")
                if raw is None or raw == "PONG":
                    n["skipped"] += 1
                    continue
                try:
                    fr = json.loads(raw)
                except ValueError:
                    n["skipped"] += 1
                    continue
                n["frames"] += 1
                mine = False
                for it in (fr if isinstance(fr, list) else (fr,)):
                    if not isinstance(it, dict) or it.get("market") != cond:
                        continue
                    mine = True
                    et = it.get("event_type")
                    if et == "book":
                        if it.get("asset_id") != up_token:
                            continue
                        vt = int(it["timestamp"]) * MS_NS
                        w.advance(vt)
                        w.book(vt, side_of(it["bids"]), side_of(it["asks"]), isinstance(fr, list))
                    elif et == "price_change":
                        ms = int(it["timestamp"])
                        vt = ms * MS_NS
                        lag[h // MS_NS - ms] = lag.get(h // MS_NS - ms, 0) + 1
                        ents = [("b" if pc["side"] == "BUY" else "a", price_int(pc["price"]), size_int(pc["size"]))
                                for pc in it["price_changes"] if pc["asset_id"] == up_token]
                        w.advance(vt)
                        w.entries(vt, ents)
                if mine:
                    n["leg_frames"] += 1
                    w.decide(h)
        w.session("close", last_h)
    w.finish()
    return n

# ---- a member's money: TZ-23's aggregate on our own fills --------------------------------------------------------

FLIP = {"b": "S", "a": "B"}      # a fill of our bid is a taker selling Up into it; a fill of our ask, a taker buying
LIFE_BANDS = ("pre", "w0", "w1", "w2", "w3", "last", "post")
UNIT_BANDS = ("w0", "w1", "w2", "w3", "last")
E12 = D("0.000000000001")


def x12(x):
    """An exact figure as fixed-point text with exactly twelve decimals, the unit's one form of a number; a figure
    with more decimals is a failed assert."""
    q = x.quantize(E12)
    assert q == x, "a figure of more than twelve decimals: %s" % x
    s = fx(q)
    return s[1:] if s.startswith("-") and q == 0 else s


def own_rows(fills):
    """Our fills as TZ-23's aggregate reads a taker's row, in Up shares: its maker_terms on the taker's side give our
    own position - our bid filled, +s Up at p; our ask filled, -s Up at p - and its rebate 0.014 s p (1 - p)."""
    return [[vt // 10 ** 9, FLIP[side], "U", fx(D(f) / SIZE_UNIT), fx(D(p) / PRICE_UNIT)]
            for vt, side, p, f, _kind in fills]


def sums_of(t0, fills):
    """A variant's sums over a member, by band and over its life - every fill before T0 + 300; a fill outside
    [T0, T0 + 300) is a failed assert."""
    bands, _win = tz23.aggregate(t0, own_rows(fills))
    assert bands["pre"]["n"] == 0 and bands["post"]["n"] == 0, "a fill of ours outside [T0, T0 + 300)"
    life = tz23.zero()
    for name in LIFE_BANDS:
        for k in life:
            life[k] += bands[name][k]
    return life, bands


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


def make_variants():
    return [Variant(name, L, front=fr, prop=pr, cross=cr) for name, L, fr, pr, cr in VARIANTS]


def sums_line(z):
    return "n %d sh %s X %s C %s R %s" % (z["n"], x12(z["sh"]), x12(z["X"]), x12(z["C"]), x12(z["R"]))


def member_unit(m, paths):
    """A member's lines, label-free: every variant's messages and sums over the leg's life, by band and by the kind of
    fill, the book's match frames against the rebuilt book, the frames read, the lag, and every fill of every
    variant."""
    T = m["T"]
    w = Window(T, PARAMS, make_variants())
    lag = {}
    n = replay(paths, w, m["condition"], m["up"], lag)
    lines = ["%d member leg %d files %d bytes %d" % (T, T + LEG, len(m["files"]), sum(f["bytes"] for f in m["files"]))]
    for v in w.vs:
        life, bands = sums_of(T + LEG, v.fills)
        lines.append("%d variant %s sent %d cancels %d refused %d crossings %d %s" % (
            T, v.name, v.n["sent"], v.n["cancels"], v.n["refused"], v.n["crossings"], sums_line(life)))
        for b in UNIT_BANDS:
            lines.append("%d band %s %s %s" % (T, v.name, b, sums_line(bands[b])))
        for kind in ("m", "x"):
            kl, _kb = sums_of(T + LEG, [f for f in v.fills if f[4] == kind])
            lines.append("%d kind %s %s %s" % (T, v.name, kind, sums_line(kl)))
    c = w.c
    lines.append("%d book snapshots %d equal %d touch_equal %d matches %d two_sided %d sessions %d closes %d" % (
        T, c["snapshots"], c["snapshots_equal"], c["touch_equal"], c["matches"], c["two_sided"], c["sessions"],
        c["closes"]))
    lines.append("%d frames lines %d frames %d leg %d skipped %d" % (T, n["lines"], n["frames"], n["leg_frames"],
                                                                    n["skipped"]))
    lines.append("%d lag frames %s p50 %s p90 %s p99 %s min %s max %s" % ((T,) + lag_quantiles(lag)))
    for v in w.vs:
        for vt, side, p, f, kind in v.fills:
            lines.append("%d fill %s %d %s %d %d %s" % (T, v.name, vt // MS_NS, side, p, f, kind))
    return lines


def parse_sums(f, i):
    """Five fields of a sums_line starting at f[i]: n, sh, X, C, R."""
    assert f[i::2][:5] == ["n", "sh", "X", "C", "R"], "a sums field %r" % f[i:]
    return {"n": int(f[i + 1]), "sh": D(f[i + 3]), "X": D(f[i + 5]), "C": D(f[i + 7]), "R": D(f[i + 9])}


def parse_unit(T, text):
    """A member's unit file, read back: every variant's sums over the life, by band and by kind, the book's counts
    and the lag. Asserts the file is the member's and whole."""
    rows = text.split("\n")
    assert rows[-1] == "" and rows[0].startswith("%d member " % T), "unit %d: not whole" % T
    got = {"T": T, "variants": {}, "bands": {}, "kinds": {}}
    names = [v[0] for v in VARIANTS]
    for ln in rows[:-1]:
        f = ln.split(" ")
        assert int(f[0]) == T, "unit %d: a line of %s" % (T, f[0])
        if f[1] == "variant":
            assert f[3:11:2] == ["sent", "cancels", "refused", "crossings"], "unit %d: a variant line" % T
            z = parse_sums(f, 11)
            z.update({"sent": int(f[4]), "cancels": int(f[6]), "refused": int(f[8]), "crossings": int(f[10])})
            got["variants"][f[2]] = z
        elif f[1] == "band":
            got["bands"][(f[2], f[3])] = parse_sums(f, 4)
        elif f[1] == "kind":
            got["kinds"][(f[2], f[3])] = parse_sums(f, 4)
        elif f[1] == "book":
            kv = dict(zip(f[2::2], f[3::2]))
            got["book"] = {k: int(v) for k, v in kv.items()}
        elif f[1] == "lag":
            got["lag"] = {k: (None if v == "None" else int(v)) for k, v in zip(f[2::2], f[3::2])}
    assert sorted(got["variants"]) == sorted(names) and "book" in got and "lag" in got and \
        len(got["bands"]) == len(names) * len(UNIT_BANDS) and len(got["kinds"]) == 2 * len(names), \
        "unit %d: incomplete" % T
    return got

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
            "replay %.1f s at most; %.0f s waited; processor %.1f s; %d bytes downloaded; retries %d; windows %s to "
            "%s" % (len(recs), len(recs) - len(outside), IDLE[1], len(outside),
                    max(r["end_second"] - r["start_second"] for r in recs), max(r["download_s"] for r in recs),
                    max(r["replay_s"] for r in recs), sum(r["waited_s"] for r in recs),
                    sum(r["cpu_s"] for r in recs), sum(r["bytes"] for r in recs), sum(r["retries"] for r in recs),
                    utc(min(r["window"] for r in recs)), utc(max(r["window"] for r in recs))))
    for r in outside:
        out("unit %d started at second %.1f of window %d and ended at second %.1f" % (
            r["T"], r["start_second"], r["window"], r["end_second"]))
    return recs, outside


def replay_units(members, udir, timing, cpu_max, dl_dir, unit_fn=run_unit, project_after=PROJECT_AFTER):
    """Every member's unit not already on disk; after the first `project_after` of this run, the replays' processor
    time projected over every member's bytes, BLOCKED above cpu_max."""
    os.makedirs(udir, exist_ok=True)
    total = sum(f["bytes"] for m in members for f in m["files"])
    t0, done, cpu, nb = time.time(), 0, 0.0, 0
    out("units to replay %d, %d bytes of streams in all" % (len(members), total))
    for m in members:
        path = os.path.join(udir, "%d.txt" % m["T"])
        if os.path.exists(path):
            continue
        unit, rec = unit_fn(m["T"], m["files"], dl_dir, lambda paths, m=m: member_unit(m, paths), timing)
        write_atomic(path, ("\n".join(unit) + "\n").encode("utf-8"))
        done += 1
        cpu += rec["cpu_s"]
        nb += rec["bytes"]
        if done == project_after:
            proj = cpu / nb * total
            out("projected %.0f s of replay for %d bytes after %d units at %.4f s a megabyte" % (
                proj, total, done, cpu / nb * 1e6))
            assert proj <= cpu_max, "BLOCKED: replay projected at %.0f s, above %d" % (proj, cpu_max)
        if done % 24 == 0:
            out("units %d this run, %.0f s" % (done, time.time() - t0))


def concat_units(members, udir, path):
    """The members' unit files, read back in order and concatenated into `path`, written once: [parsed unit]."""
    rows, h, nlines = [], hashlib.sha256(), 0
    with open(path + ".new", "wb") as wfh:
        for m in members:
            with open(os.path.join(udir, "%d.txt" % m["T"]), "rb") as fh:
                data = fh.read()
            rows.append(parse_unit(m["T"], data.decode("utf-8")))
            h.update(data)
            nlines += data.count(b"\n")
            wfh.write(data)
    sha = h.hexdigest()
    if os.path.exists(path):
        os.remove(path + ".new")
        assert sha256_file(path) == sha, "determinism: %s differs from the first run" % path
        out("unchanged %s sha256 %s" % (path, sha))
    else:
        os.replace(path + ".new", path)
        out("wrote %s %d bytes sha256 %s" % (path, os.path.getsize(path), sha))
    return rows, sha, nlines

# ---- the gate: TZ-23's thresholds on each gated variant, and W1's reading -------------------------------------


def variant_sums(rows):
    """Over the members: each variant's fills, shares, X, C and R summed, V the sum of X squared, the members with a
    fill, and its messages."""
    tot = {}
    for name, *_ in VARIANTS:
        t = {"n": 0, "sh": D(0), "X": D(0), "C": D(0), "R": D(0), "V": D(0), "members_with_fills": 0, "sent": 0,
             "cancels": 0, "refused": 0, "crossings": 0}
        for r in rows:
            v = r["variants"][name]
            for k in ("n", "sh", "X", "C", "R", "sent", "cancels", "refused", "crossings"):
                t[k] += v[k]
            t["V"] += v["X"] * v["X"]
            t["members_with_fills"] += 1 if v["n"] else 0
        tot[name] = t
    return tot


def gate_of(name, t):
    return tz23.gate_constants(t["V"], t["sh"], lam=LAMBDA[name], alpha=ALPHA, delta=DELTA)


def book_reading(snapshots, touch_equal):
    """G-BOOK: PASS where the touch rebuilt from the leg's entries - the best bid and its size, the best ask and its
    size - equals the venue's own book frame's at no fewer than BOOK_EQUAL_MIN of the match frames read."""
    return "PASS" if snapshots > 0 and D(touch_equal) >= BOOK_EQUAL_MIN * snapshots else "FAIL"


def w1_reading(res):
    """W1's word from the two gated variants' own TZ-23 readings: W1-EARN where `behind` reaches its EARN bound,
    else W1-NO-EARN where `front` reaches its NO EARN bound, else UNDECIDABLE."""
    if res["behind"]["earn"]:
        return "W1-EARN"
    if res["front"]["no_earn"]:
        return "W1-NO-EARN"
    return "UNDECIDABLE"


def build_constants(s, rows, label, base):
    """Label-free: every variant's sums over the set, G-BOOK's counts, the capture's lag, and each gated variant's
    thresholds and power; the constants file written once."""
    tot = variant_sums(rows)
    bk = {k: sum(r["book"][k] for r in rows) for k in rows[0]["book"]}
    lg = [r["lag"] for r in rows if r["lag"]["frames"]]
    p50s, p99s = sorted(x["p50"] for x in lg), sorted(x["p99"] for x in lg)
    lagd = {"members": len(lg), "frames": sum(x["frames"] for x in lg), "p50_median": p50s[(len(p50s) - 1) // 2],
            "p99_median": p99s[(len(p99s) - 1) // 2], "p99_max": p99s[-1], "max": max(x["max"] for x in lg),
            "min": min(x["min"] for x in lg), "p99_above_1000": sum(1 for v in p99s if v > 1000)}
    gates = {g: gate_of(g, tot[g]) for g in GATED}
    const = {"label": label, "members": len(rows), "first": rows[0]["T"], "last": rows[-1]["T"],
             "member_list_sha": sha256_bytes(("\n".join(str(r["T"]) for r in rows) + "\n").encode()),
             "variants": tot, "gates": gates, "book": bk, "g_book": book_reading(bk["snapshots"], bk["touch_equal"]),
             "lag": lagd, "params": PARAMS, "variants_def": [list(v) for v in VARIANTS], "set_sha": s.get("sha")}
    path = os.path.join(base, "%s-constants.json" % label)
    sha = write_once(path, dumps(const).encode("utf-8"))
    return const, sha


def show_constants(const):
    out("members %d, first %d %s, last %d %s; member list sha256 %s" % (
        const["members"], const["first"], utc(const["first"]), const["last"], utc(const["last"]),
        const["member_list_sha"]))
    bk = const["book"]
    out("G-BOOK %s: match frames %d, the rebuilt touch equal to the venue's at %d (%s); every level equal at %d (%s), "
        "barred; matches read %d, two-sided %d; sessions %d, closes %d" % (
            const["g_book"], bk["snapshots"], bk["touch_equal"], q12(D(bk["touch_equal"]) / max(bk["snapshots"], 1)),
            bk["equal"], q12(D(bk["equal"]) / max(bk["snapshots"], 1)), bk["matches"], bk["two_sided"],
            bk["sessions"], bk["closes"]))
    lg = const["lag"]
    out("the capture's lag, a price_change frame's host receipt less its venue stamp, over %d members and %d frames of "
        "the leg: the median member's median %d ms; its 99th percentile %d ms at the median member and %d ms at the "
        "worst, above 1,000 ms at %d members; the longest %d ms, the least %d ms" % (
            lg["members"], lg["frames"], lg["p50_median"], lg["p99_median"], lg["p99_max"], lg["p99_above_1000"],
            lg["max"], lg["min"]))
    for name, *_ in VARIANTS:
        t = const["variants"][name]
        out("%s%s: sent %d, cancels %d, refused %d, crossings %d; members with a fill %d; fills %d, shares %s, X %s, "
            "C %s, R %s, V %s" % (name, "" if name in GATED else ", barred from every reading", t["sent"],
                                  t["cancels"], t["refused"], t["crossings"], t["members_with_fills"], t["n"],
                                  fx(t["sh"]), fx(t["X"]), fx(t["C"]), fx(t["R"]), fx(t["V"])))
    for g in GATED:
        c = const["gates"][g]
        out("%s: V %s; Sh %s; lambda %s; L %s; thr %s (%s a share)" % (
            g, fx(c["V"]), fx(c["sh"]), fx(c["lambda"]), q12(c["L"]), q12(c["thr"]),
            q12(c["thr_per_share"]) if "thr_per_share" in c else "-"))
        out("%s: EARN at S >= %s; NO EARN at S <= %s (%s a share); power %s" % (
            g, q12(c["earn_at"]), q12(c["no_earn_at"]),
            q12(c["no_earn_per_share"]) if "no_earn_per_share" in c else "-", fx(c["power"])))
    out("W1 reads W1-EARN on behind's EARN bound and W1-NO-EARN on front's NO EARN bound (TZ-32 section 4.5)")


def score_rows(s, rows, const, label, base):
    """The labels, read once from the set's own documents; each variant's money, by member and band; each gated
    variant's TZ-23 reading and W1's."""
    ups = {m["T"]: tz23.label_of(m["doc"]) for m in s["members"]}
    assert sorted(ups) == [r["T"] for r in rows], "score: the members are not the units'"
    res = {"label": label, "members": len(rows), "ups": sum(ups.values()), "variants": {}}
    lines = ["T,up," + ",".join("S_%s" % name for name, *_ in VARIANTS)]
    per = {name: [] for name, *_ in VARIANTS}
    for r in rows:
        up = ups[r["T"]]
        cells = [str(r["T"]), str(up)]
        for name, *_ in VARIANTS:
            v = r["variants"][name]
            m = v["X"] * up - v["C"] + v["R"]
            per[name].append(m)
            cells.append(fx(m))
        lines.append(",".join(cells))
    for name, *_ in VARIANTS:
        t = const["variants"][name]
        X, C, R, sh = D(t["X"]), D(t["C"]), D(t["R"]), D(t["sh"])
        settle = sum((r["variants"][name]["X"] * ups[r["T"]] for r in rows), D(0)) - C
        S = settle + R
        bands = {}
        for b in ("w0", "w1", "w2", "w3", "last"):
            bs = bsh = D(0)
            for r in rows:
                z = r["bands"][(name, b)]
                bs += z["X"] * ups[r["T"]] - z["C"] + z["R"]
                bsh += z["sh"]
            bands[b] = {"S": bs, "sh": bsh, "per_share": bs / bsh if bsh else None}
        kinds = {}
        for kd in ("m", "x"):
            ks = ksh = D(0)
            for r in rows:
                z = r["kinds"][(name, kd)]
                ks += z["X"] * ups[r["T"]] - z["C"] + z["R"]
                ksh += z["sh"]
            kinds[kd] = {"S": ks, "sh": ksh, "per_share": ks / ksh if ksh else None}
        pm = sorted(per[name])
        e = {"S": S, "settlement": settle, "rebate": R, "sh": sh, "per_share": S / sh if sh else None,
             "settlement_per_share": settle / sh if sh else None, "rebate_per_share": R / sh if sh else None,
             "bands": bands, "kinds": kinds, "member_min": pm[0], "member_median": pm[(len(pm) - 1) // 2],
             "member_max": pm[-1], "members_above": sum(1 for x in pm if x > 0),
             "members_below": sum(1 for x in pm if x < 0)}
        if name in GATED:
            c = const["gates"][name]
            word, earn, no_earn = tz23.reading(S, {"earn_at": D(c["earn_at"]), "no_earn_at": D(c["no_earn_at"])})
            e.update({"word": word, "earn": earn, "no_earn": no_earn, "margin_earn": S - D(c["earn_at"]),
                      "margin_no_earn": D(c["no_earn_at"]) - S})
        res["variants"][name] = e
    res["reading"] = w1_reading(res["variants"]) if const["g_book"] == "PASS" else None
    sc = os.path.join(base, "%s-scored.csv" % label)
    res["scored_sha"] = write_once(sc, ("\n".join(lines) + "\n").encode("utf-8"))
    rp = os.path.join(base, "%s-reading.json" % label)
    res["reading_sha"] = write_once(rp, dumps(res).encode("utf-8"))
    out("labels: %d members, %d Up" % (len(rows), res["ups"]))
    for name, *_ in VARIANTS:
        e = res["variants"][name]
        out("%s%s: S %s = settlement %s + rebate %s on %s shares; per share %s = %s + %s" % (
            name, "" if name in GATED else ", barred from every reading", q12(e["S"]), q12(e["settlement"]),
            q12(e["rebate"]), fx(e["sh"]), q12(e["per_share"]) if e["per_share"] is not None else "-",
            q12(e["settlement_per_share"]) if e["per_share"] is not None else "-",
            q12(e["rebate_per_share"]) if e["per_share"] is not None else "-"))
        if name in GATED:
            out("%s: %s; EARN %s (margin %s); NO EARN %s (margin %s)" % (
                name, e["word"], e["earn"], q12(e["margin_earn"]), e["no_earn"], q12(e["margin_no_earn"])))
        for b, z in e["bands"].items():
            if z["sh"]:
                out("barred: %s band %-4s shares %s, S %s, per share %s" % (name, b, fx(z["sh"]), q12(z["S"]),
                                                                           q12(z["per_share"])))
        for kd, z in e["kinds"].items():
            if z["sh"]:
                out("barred: %s fills %s shares %s, S %s, per share %s" % (
                    name, "at a match" if kd == "m" else "against a crossing order", fx(z["sh"]), q12(z["S"]),
                    q12(z["per_share"])))
        out("barred: %s per member S min %s, median %s, max %s; above zero %d, below %d" % (
            name, q12(e["member_min"]), q12(e["member_median"]), q12(e["member_max"]), e["members_above"],
            e["members_below"]))
    out("the score's files: %s sha256 %s; %s sha256 %s" % (sc, res["scored_sha"], rp, res["reading_sha"]))
    return res

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
    assert any(r[0] == "research/" + TZ23_NAME and r[3] == "frozen" and r[4] == TZ23_SHA256 for r in rows), \
        "%s: not the map's frozen row" % TZ23_NAME
    with open(os.path.join(PRIMARY, "research", TZ23_NAME), "rb") as fh:
        t23 = sha256_bytes(fh.read())
    assert t23 == TZ23_SHA256, "the primary checkout's %s sha256 %s" % (TZ23_NAME, t23)
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d; %s is the file this instrument loads, a frozen row" % (
            MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"], states["reported"],
            TZ23_NAME))


def still_reading(before, now, restarts):
    """G-STILL from the two reads and the archive's restart records between them, in order: PASS where both units
    are unchanged, or where the recorder is unchanged and the pair book's change is the archive's own restarts alone -
    a chain of records from the recorded MainPID to the current one, NRestarts one higher at each, the unit active.
    Pure: it reads nothing but its arguments."""
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
    st = load_state()
    now = {}
    for key, unit in sorted(UNITS.items()):
        kv = show(unit, ["MainPID", "NRestarts", "ActiveState", "MemoryCurrent", "MemoryPeak"])
        now[key] = {k: kv[k] for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, MemoryCurrent %s, MemoryPeak %s" % (unit, now[key], kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    for unit in (ARCHIVE_TIMER, ARCHIVE_UNIT):
        kv = show(unit, ["ActiveState", "SubState", "UnitFileState", "Result"])
        out("%s %s" % (unit, kv))
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "at_ns": time.time_ns(), "units": now}
        save_state(st)
        out("still: recorded")
        return
    _raw, recs, _tail = ledger_records()
    since = st["still"]["at_ns"]
    restarts = [r for r in recs if r.get("event") == "restart" and r.get("wall_ns", 0) >= since]
    for r in restarts:
        out("the archive's restart record %s: run %s, window %s, pid %s after %s, NRestarts %s" % (
            utc(r["wall_ns"] / 1e9), r.get("run"), r.get("W"), r.get("pid"), r.get("stopped"), r.get("NRestarts")))
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
    """The archive's own record, read whole: its complete lines, each printed, its runs summarized, every complete
    run's set.json asserted by its set record's SHA-256, and the windows its assets reach."""
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
    amap = asset_map(sets)
    for s in sets:
        ts = sorted(x["T"] for x in s["doc"]["assets"])
        out("set %s run %d sha256 %s: %d files, %d bytes, windows %s to %s" % (
            s["tag"], s["run"], s["sha256"], s["doc"]["assets_n"], s["doc"]["bytes_total"], ts[0] if ts else "-",
            ts[-1] if ts else "-"))
    after = sorted(t for t in amap if t >= FIRST_T)
    out("the archive's assets: %d windows, %d files, to window %d; at or after %d: %d windows, to %s" % (
        len(amap), sum(len(v) for v in amap.values()), max(amap), FIRST_T, len(after), after[-1] if after else "-"))
    tags = sorted(ln.split("\t")[1][len("refs/tags/"):] for ln in git(
        "ls-remote", "origin", "refs/tags/pairbook-streams-*", tree=PRIMARY).split("\n") if "\t" in ln)
    stags = [s["tag"] for s in sets]
    out("tags on origin %d: %s" % (len(tags), tags))
    out("complete runs' sets %d; their tags not on origin %s; halted %s; runs without a terminal record %s" % (
        len(stags), sorted(set(stags) - set(tags)), summ["halted"],
        [a for a, t in summ["terminal"].items() if not t]))


def rehearsal_members(base):
    """TZ-27's 51 windows, their legs' settled documents read by TZ-23's gamma_docs held to the idle stretch at every
    run, a later run's bytes the first's; every one a member, its condition and Up token its document's."""
    with open(TZ27_SET, "rb") as fh:
        raw = fh.read()
    assert sha256_bytes(raw) == TZ27_SET_SHA, "TZ-27's set.json in the forensic store"
    doc = json.loads(raw)
    assert doc["tag"] == TZ27_TAG and tuple(x["T"] for x in doc["assets"]) == REHEARSAL_TS and all(
        x["file"] == "stream.jsonl.gz" for x in doc["assets"]), "TZ-27's set: 51 windows, one file each"
    os.makedirs(base, exist_ok=True)
    got = docs_of(list(REHEARSAL_TS))
    by = {t: tz23.kept_doc(d) if d is not None else None for t, d in got.items()}
    write_once(os.path.join(base, "docs.json"), dumps({str(t): d for t, d in sorted(by.items())}).encode("utf-8"))
    members = []
    for x in doc["assets"]:
        t, d = x["T"], by.get(x["T"])
        why = tz23.qualify(t + LEG, d)
        assert why is None, "G-REHEARSAL: window %d's leg %s" % (t, why)
        tok = json.loads(d["clobTokenIds"])
        members.append({"T": t, "condition": d["conditionId"], "up": tok[0], "doc": d,
                        "files": [{"file": x["file"], "tag": TZ27_TAG, "asset": x["asset"], "bytes": x["bytes"],
                                   "sha256": x["sha256"]}]})
    return members


def rehearsal_figures(rows, ups):
    """The figures G-REHEARSAL compares beside the lines: each variant's fills, shares, X, C, R, V and S."""
    tot = variant_sums(rows)
    fig = {}
    for name, *_ in VARIANTS:
        t = tot[name]
        S = sum((r["variants"][name]["X"] * ups[r["T"]] for r in rows), D(0)) - t["C"] + t["R"]
        fig[name] = [t["n"], x12(t["sh"]), x12(t["X"]), x12(t["C"]), x12(t["R"]), x12(t["V"]), x12(S)]
    return fig


def mode_rehearse():
    floor_check()
    base = os.path.join(WORK, "rehearsal")
    members = rehearsal_members(base)
    udir, timing = os.path.join(base, "units"), os.path.join(base, "rehearsal-timing.jsonl")
    replay_units(members, udir, timing, REHEARSAL_CPU_MAX, os.path.join(WORK, "streams"))
    timing_summary(timing)
    rows, sha, nlines = concat_units(members, udir, os.path.join(base, "rehearsal-lines.txt"))
    ups = {m["T"]: tz23.label_of(m["doc"]) for m in members}
    fig = rehearsal_figures(rows, ups)
    checks = {"lines": nlines == REF["lines"], "digest": sha == REF["digest"]}
    for name, *_ in VARIANTS:
        checks["totals " + name] = fig[name] == REF["totals"].get(name)
        out("G-REHEARSAL %-8s %s; the Architect's %s" % (name, fig[name], REF["totals"].get(name)))
    out("G-REHEARSAL lines %d, the Architect's %d; sha256 %s, the Architect's %s" % (nlines, REF["lines"], sha,
                                                                                    REF["digest"]))
    bad = sorted(k for k, v in checks.items() if not v)
    assert not bad, "G-REHEARSAL FAIL: %s" % bad
    out("G-REHEARSAL PASS: %d of %d - %d lines byte for byte and %d variants' totals equal to the Architect's" % (
        len(checks), len(checks), nlines, len(VARIANTS)))


def mode_fetch():
    """The candidates from FIRST_T, once the archive has moved every one to LAST_T: each window's stream conditions
    from its window.json, then its leg's settled document by TZ-23's gamma_docs, held to the idle stretch, in
    requests of twenty and in order until NEED members (G-SET). No price of the store is read."""
    floor_check()
    amap, waited = wait_archive()
    out("the archive has moved windows to %d, at or after %d, after %.0f s waited" % (max(amap), LAST_T, waited))
    base = os.path.join(WORK, "set")
    os.makedirs(base, exist_ok=True)
    ts = list(range(FIRST_T, LAST_T + 1, WINDOW))
    wj, status = {}, {}
    for t in ts:
        try:
            wj[t] = window_json(t)
        except FileNotFoundError:
            wj[t] = None
        status[t] = stream_problem(wj[t], t, amap)
    considered, members, by = [], [], {}
    pending = [t for t in ts if status[t] is None]
    k = 0
    for t in ts:
        if len(members) == NEED:
            break
        if status[t] is None:
            if t not in by:
                chunk = pending[k:k + DOC_CHUNK]
                k += len(chunk)
                by.update(docs_of(chunk))
            why = leg_problem(wj[t], t, by.get(t))
            if why is None:
                d = by[t]
                tok = json.loads(d["clobTokenIds"])
                members.append({"T": t, "condition": d["conditionId"], "up": tok[0], "doc": tz23.kept_doc(d),
                                "files": [dict(amap[t][f], file=f) for f in wj[t]["stream"]["files"]]})
                status[t] = "member"
            else:
                status[t] = why
        considered.append([t, status[t]])
        assert len(considered) - len(members) <= NONMEMBER_MAX, \
            "BLOCKED: %d non-members before the %dth member" % (len(considered) - len(members), NEED)
    assert len(members) == NEED, "BLOCKED: %d members among the %d candidates" % (len(members), len(considered))
    mts = [m["T"] for m in members]
    s = {"first_T": FIRST_T, "need": NEED, "considered": considered, "members": members,
         "member_list_sha": sha256_bytes(("\n".join(map(str, mts)) + "\n").encode())}
    path = os.path.join(base, "w1-set.json")
    sha = write_once(path, dumps(s).encode("utf-8"))
    st = load_state()
    st["set_sha"], st["set_at"] = sha, utc(time.time())
    save_state(st)
    nb = sum(f["bytes"] for m in members for f in m["files"])
    out("G-SET PASS: %d members of %d considered, %d (%s) to %d (%s); %d stream files, %d bytes; member list sha256 "
        "%s; %s sha256 %s" % (len(members), len(considered), mts[0], utc(mts[0]), mts[-1], utc(mts[-1]),
                              sum(len(m["files"]) for m in members), nb, s["member_list_sha"], path, sha))
    out("document requests %d for %d windows" % (-(-k // DOC_CHUNK), k))
    out("non-members %d: %s" % (len(considered) - len(members),
                               json.dumps([[t, w] for t, w in considered if w != "member"])))
    days = {}
    for t in mts:
        d = time.strftime("%a", time.gmtime(t + LEG))
        days[d] = days.get(d, 0) + 1
    out("members by the weekday of their leg %s" % json.dumps(days, sort_keys=True))


def the_set():
    path = os.path.join(WORK, "set", "w1-set.json")
    st = load_state()
    sha = sha256_file(path)
    assert sha == st.get("set_sha"), "the set %s is not the one state.json records" % sha
    s = load_json(path)
    assert len(s["members"]) == NEED and s["first_T"] == FIRST_T, "the set"
    s["sha"] = sha
    return s


def mode_replay():
    """Label-free: every member's streams downloaded, replayed and removed, each unit held to the idle stretch; the
    units concatenated, and the constants - G-BOOK, the lag, every variant's sums, each gated variant's thresholds
    and power - written once, their SHA-256 in state.json."""
    floor_check()
    s = the_set()
    base = os.path.join(WORK, "replay")
    udir = os.path.join(base, "units")
    replay_units(s["members"], udir, os.path.join(base, "replay-timing.jsonl"), REPLAY_CPU_MAX,
                 os.path.join(WORK, "streams"))
    timing_summary(os.path.join(base, "replay-timing.jsonl"))
    rows, wsha, nlines = concat_units(s["members"], udir, os.path.join(base, "w1-units.txt"))
    out("units %d lines" % nlines)
    const, csha = build_constants(s, rows, "w1", base)
    show_constants(const)
    st = load_state()
    st["constants_sha"], st["units_sha"], st["constants_at"] = csha, wsha, utc(time.time())
    save_state(st)
    out("constants sha256 %s, units sha256 %s, in state.json" % (csha, wsha))


def mode_rescore():
    """Every RESCORE_EVERY-th member from a second download and a second replay; each unit file byte for byte the
    replay's (DETERMINISM)."""
    floor_check()
    s = the_set()
    chosen = s["members"][::RESCORE_EVERY]
    udir = os.path.join(WORK, "rescore", "units")
    replay_units(chosen, udir, os.path.join(WORK, "rescore", "rescore-timing.jsonl"), RESCORE_CPU_MAX,
                 os.path.join(WORK, "streams"), project_after=RESCORE_PROJECT_AFTER)
    timing_summary(os.path.join(WORK, "rescore", "rescore-timing.jsonl"))
    same = 0
    for m in chosen:
        a = sha256_file(os.path.join(WORK, "replay", "units", "%d.txt" % m["T"]))
        b = sha256_file(os.path.join(udir, "%d.txt" % m["T"]))
        same += a == b
        if a != b:
            out("rescore: %d differs, %s against %s" % (m["T"], a, b))
    assert same == len(chosen), "DETERMINISM FAIL: %d of %d" % (same, len(chosen))
    out("DETERMINISM PASS: %d of %d members' unit files byte for byte the replay's" % (same, len(chosen)))


def mode_score():
    floor_check()
    s = the_set()
    st = load_state()
    base = os.path.join(WORK, "replay")
    cpath = os.path.join(base, "w1-constants.json")
    assert sha256_file(cpath) == st.get("constants_sha"), "score: not the constants recorded"
    head = git("rev-parse", "HEAD")
    assert "origin/" + BRANCH in git("branch", "-r", "--contains", head).split(), \
        "score: HEAD %s is not on origin" % head
    const = load_json(cpath)
    assert const["member_list_sha"] == s["member_list_sha"] and const["set_sha"] == s["sha"], \
        "score: the constants are not the set's"
    rows, wsha, _n = concat_units(s["members"], os.path.join(base, "units"), os.path.join(base, "w1-units.txt"))
    assert wsha == st.get("units_sha"), "score: not the units recorded"
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(dumps({"at": utc(time.time()), "head": head, "members": len(rows),
                        "member_list_sha": s["member_list_sha"], "constants_sha": st["constants_sha"]}))
    res = score_rows(s, rows, const, "w1", base)
    if res["variants"]["behind"]["earn"] and res["variants"]["front"]["no_earn"]:
        out("both bounds hold: behind reaches EARN and front NO EARN; the reading is W1-EARN (TZ-32 section 4.5)")
    assert const["g_book"] == "PASS", "G-BOOK FAIL: the reading is not read"
    out("W1 READING: %s" % res["reading"])


def report_tokens():
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8", errors="replace") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    return tree == WORK and (rel in ("state.json", "label-ledger.jsonl") or rel.startswith("logs/"))


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

# ---- the self-test: literals, a synthetic window and temporary trees under the work tree -----------------------

SYN_T = 1792800000
SYN = {"m15": {"Up": "4001", "Down": "4002", "condition": "0x" + "a1" * 32},
       "m5": {"Up": "5001", "Down": "5002", "condition": "0x" + "b2" * 32}}


def _lv(levels):
    return [{"price": p, "size": s} for p, s in levels]


def _book(tok, cond, ts, bids, asks):
    """A book frame as the venue sends it: bids ascending, asks descending."""
    return {"market": cond, "asset_id": tok, "timestamp": str(ts), "hash": "0a", "event_type": "book",
            "bids": _lv(sorted(bids, key=lambda z: D(z[0]))), "asks": _lv(sorted(asks, key=lambda z: -D(z[0])))}


def _pc(cond, ts, entries):
    """A price_change frame in the venue's own key order: (token, side, price, size) entries, best bid and ask
    filler."""
    return {"market": cond, "price_changes": [{"asset_id": tok, "price": p, "size": s, "side": side, "hash": "0a1b",
                                               "best_bid": "0.5", "best_ask": "0.5"} for tok, side, p, s in entries],
            "timestamp": str(ts), "event_type": "price_change"}


def synth_frames(T=SYN_T, mp=SYN):
    """Two stream files of one window, every rule of TZ-32 section 1 met at least once: each entry is (host seconds
    after T, an event or a frame), the venue's stamps milliseconds after T * 1000."""
    c15, c5 = mp["m15"]["condition"], mp["m5"]["condition"]
    x, y, yc = mp["m15"]["Up"], mp["m5"]["Up"], mp["m5"]["Down"]
    v = lambda s: T * 1000 + int(round(s * 1000))

    def up(s, side, p, size):
        """A price_change of the leg: the Up entry and its Down mirror."""
        mirror = ("SELL" if side == "BUY" else "BUY", fx(1 - D(p)))
        return _pc(c5, v(s), [(y, side, p, size), (yc, mirror[0], mirror[1], size)])

    def other(s):
        return _pc(c15, v(s), [(x, "BUY", "0.40", "10"), (mp["m15"]["Down"], "SELL", "0.60", "10")])

    def books(s, yb, ya):
        return [_book(x, c15, v(s), [("0.40", "10")], [("0.60", "10")]),
                _book(mp["m15"]["Down"], c15, v(s), [("0.40", "10")], [("0.60", "10")]),
                _book(yc, c5, v(s), [("0.47", "1")], [("0.53", "1")]), _book(y, c5, v(s), yb, ya)]

    def session(t, b):
        return [(t, {"event": "connect", "seg": 0}), (t + 0.05, {"event": "open", "seg": 0, "status": 101}),
                (t + 0.1, {"event": "subscribe", "seg": 0}), (t + 0.3, b)]

    def bk(s, bids, asks):
        return _book(y, c5, v(s), bids, asks)

    first = session(594.9, books(595.15, [("0.47", "200"), ("0.48", "100")], [("0.53", "300"), ("0.52", "100")])) + [
        (599.000, up(598.990, "BUY", "0.46", "50")),
        (600.020, up(600.000, "SELL", "0.54", "40")),
        (601.020, up(601.000, "BUY", "0.48", "70")),
        (601.021, bk(601.000, [("0.48", "70"), ("0.47", "200"), ("0.46", "50")],
                     [("0.52", "100"), ("0.53", "300"), ("0.54", "40")])),
        (601.500, other(601.490)),
        (602.010, up(602.000, "BUY", "0.48", "0")),
        (602.011, up(602.000, "BUY", "0.47", "150")),
        (602.012, bk(602.000, [("0.47", "150"), ("0.46", "50")], [("0.52", "100"), ("0.53", "300"), ("0.54", "40")])),
        (603.000, up(602.990, "SELL", "0.52", "0")),
        (603.010, up(603.005, "BUY", "0.52", "25")),
        (603.100, up(603.090, "BUY", "0.46", "60")),
        (603.400, bk(603.300, [("0.52", "25"), ("0.47", "150"), ("0.46", "60")], [("0.53", "300"), ("0.54", "40")])),
        (605.000, up(604.995, "BUY", "0.52", "0")),
        (607.000, up(606.995, "BUY", "0.49", "40")),
        (607.020, up(607.010, "BUY", "0.49", "0")),
        (607.030, up(607.020, "SELL", "0.49", "15")),
        (607.300, up(607.290, "SELL", "0.49", "0")),
        (610.000, up(609.990, "BUY", "0.46", "61")),
        (610.200, up(610.190, "BUY", "0.47", "140")),
        (610.201, bk(610.190, [("0.47", "140"), ("0.46", "61")], [("0.53", "300"), ("0.54", "40")])),
        (610.400, up(610.390, "BUY", "0.46", "62")),
        (610.600, up(610.590, "BUY", "0.47", "130")),
        (610.601, bk(610.590, [("0.47", "130"), ("0.46", "62")], [("0.53", "300"), ("0.54", "40")])),
        (610.800, up(610.790, "BUY", "0.46", "63")),
        (611.000, up(610.990, "BUY", "0.47", "120")),
        (611.001, bk(610.990, [("0.47", "120"), ("0.46", "63")], [("0.53", "300"), ("0.54", "40")])),
        (611.200, up(611.190, "BUY", "0.46", "64")),
        (611.400, up(611.390, "BUY", "0.47", "110")),
        (611.401, bk(611.390, [("0.47", "110"), ("0.46", "64")], [("0.53", "300"), ("0.54", "40")])),
        (611.600, up(611.590, "BUY", "0.46", "65")),
        (620.000, up(619.990, "SELL", "0.96", "10")),
        (620.010, up(620.000, "SELL", "0.53", "0")),
        (620.020, up(620.010, "SELL", "0.54", "0")),
        (620.500, other(620.490)),
        (621.000, up(620.990, "SELL", "0.53", "20")),
        (650.000, {"event": "close", "seg": 0, "reason": "closed", "code": 1006})]
    second = session(651.0, books(651.25, [("0.45", "100"), ("0.46", "80")], [("0.55", "60"), ("0.54", "200")])) + [
        (651.500, up(651.490, "SELL", "0.54", "190")),
        (652.000, up(651.990, "SELL", "0.54", "150")),
        (652.001, bk(651.990, [("0.46", "80"), ("0.45", "100")], [("0.54", "150"), ("0.55", "60")])),
        (700.000, _pc(c5, v(699.990), [(y, "BUY", "0.46", "90"), (yc, "SELL", "0.54", "90"),
                                       (y, "BUY", "0.44", "30")])),
        (894.000, up(893.990, "BUY", "0.46", "95")),
        (895.0005, other(894.990)),
        (895.020, up(895.010, "BUY", "0.46", "0")),
        (895.100, up(895.090, "BUY", "0.45", "0")),
        (895.200, bk(895.090, [("0.44", "30")], [("0.54", "150"), ("0.55", "60")])),
        (905.000, {"event": "close", "seg": 0, "reason": "end", "code": None}), (905.010, {"event": "end"})]
    return first, second


def synth_stream(dirpath, T=SYN_T, mp=SYN):
    """The two files of synth_frames, in the pair book's line format, deterministic gzip; a PONG and a blank line
    in each."""
    paths = []
    for name, rows in zip(("%d-stream.jsonl.gz" % T, "%d-stream.1.jsonl.gz" % T), synth_frames(T, mp)):
        lines = []
        for s, obj in rows:
            rn = T * 10 ** 9 + int(round(s * 10 ** 7)) * 100
            if "event" in obj:
                lines.append(json.dumps(dict({"recv_ns": rn, "mono_ns": rn}, **obj), separators=(",", ":")))
            else:
                lines.append(json.dumps({"recv_ns": rn, "mono_ns": rn,
                                         "raw": json.dumps(obj, separators=(", ", ":"))}, separators=(",", ":")))
        lines.insert(3, json.dumps({"recv_ns": (T + 595) * 10 ** 9, "mono_ns": 0, "raw": "PONG"}, separators=(",", ":")))
        lines.insert(5, "")
        p = os.path.join(dirpath, name)
        with open(p, "wb") as fh:
            fh.write(gzip.compress(("\n".join(lines) + "\n").encode(), mtime=0))
        paths.append(p)
    return paths


# the Architect's reference over synth_stream's two files: its unit's lines and their SHA-256 (TZ-32 section 4.1)
SYN_LINES = 100
SYN_DIGEST = "6b179243c4feb9b0fcd76d45637e2a962626d8a8141a13e95dcddefb105ccd7e"
# the projection: each gated variant's V and Sh over the Architect's 302 windows of W0's span, every one read by W0,
# and the Architect's independent threshold and power at them scaled to 288 members (TZ-32 section 1)
PROJ_N = 302
PROJ = {"behind": (D("104180.3858"), D("210474.22"),
                   {"thr": D("544.1515737611919841909513296747519798286"), "power": (D("0.99822"), D("0.99823"))}),
        "front": (D("81071.5419"), D("737365.95"),
                  {"thr": D("480.0141253639412769515206627775781806438"), "power": (D("0.99999"), D("1.00001"))})}


def money_by_fill(fills, up):
    """The self-test's own arithmetic, written apart from TZ-23's: a fill of our bid at p for s shares pays
    s (up - p), of our ask s (p - up), and each the rebate 0.014 s p (1 - p); in Fractions, summed."""
    from fractions import Fraction
    tot = Fraction(0)
    for _vt, side, p, f, _kind in fills:
        s, pr = Fraction(f, 100), Fraction(p, 1000)
        tot += (s * (up - pr) if side == "b" else s * (pr - up)) + Fraction(14, 1000) * s * pr * (1 - pr)
    return tot


def mode_selftest():
    import random
    import threading
    import http.server
    from fractions import Fraction
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    def fails(fn):
        try:
            fn()
        except AssertionError:
            return True
        return False

    # TZ-23's file, as loaded, and the constants this file takes from it
    ok(tz23.__file__ == os.path.join(HERE, TZ23_NAME) and sys.modules["tz23"] is tz23,
       "TZ-23's instrument loaded from beside this file, from its asserted bytes")
    ok(tz23.MALLOC_TUNED, "glibc took the 128 KiB mmap threshold and the two arenas")
    ok(tz23.getcontext().prec == 60, "the main thread sums at 60 digits")
    ok(DELTA == D("0.005") and tz23.REBATE_COEF == D("0.014") and
       tz23.FEE_SCHEDULE == {"exponent": 1, "rate": D("0.07"), "takerOnly": True, "rebateRate": D("0.2")} and
       tz23.FEE_TYPE == "crypto_fees_v2", "half a tick a share; the fee 0.07 s p (1 - p), the rebate a fifth of it, as "
                                          "the documents must state")
    ok(tz23.HEADERS == {"User-Agent": "btc-5m-twap-m0/TZ-23", "Accept": "application/json"} and
       DL_HEADERS == {"User-Agent": "btc-5m-twap-tz32", "Accept": "application/octet-stream"},
       "every document request carries TZ-23's two headers, every download this file's")
    ok([b[0] for b in tz23.BANDS] == list(LIFE_BANDS) and tz23.BANDS[-2] == ("last", 240, 300) and
       UNIT_BANDS == LIFE_BANDS[1:-1], "a leg's life is TZ-23's bands w0 to last, [T0, T0 + 300)")
    # the set: its windows, its last candidate and the archive's run that moves it
    ok(FIRST_T % WINDOW == 0 and FIRST_T + LEG - WINDOW == W0_LAST and utc(FIRST_T) == "2026-10-23T11:15:00Z" and
       utc(FIRST_T + LEG) == "2026-10-23T11:25:00Z", "the first window is 2026-10-23 11:15 UTC, the one after the "
                                                    "window whose leg is W0's last member")
    cal = (LAST_T + 910 + 60) // 86400 * 86400 + ARCHIVE_CALENDAR_S
    cal = cal if cal >= LAST_T + 970 else cal + 86400
    ok(LAST_T == 1793068200 and utc(LAST_T) == "2026-10-27T02:30:00Z" and utc(cal) == "2026-10-27T03:00:20Z" and
       cal < ARCHIVE_WAIT_UNTIL and utc(ARCHIVE_WAIT_UNTIL) == "2026-10-27T06:00:00Z",
       "the candidates end at 2026-10-27 02:30 UTC, which the calendar run of 03:00:20 moves; fetch waits to 06:00")
    ok(NEED == 288 and RESCORE_EVERY == 16 and len(range(0, NEED, RESCORE_EVERY)) == 18,
       "288 members; the rescore replays 18 of them")
    # the venue's numbers as exact integers
    ok([price_int(x) for x in ("0.5", "0.505", "1", "0", "0.07")] == [500, 505, 1000, 0, 70] and
       [size_int(x) for x in ("12.34", "5", "0.1", "1000000")] == [1234, 500, 10, 100000000],
       "prices in thousandths and sizes in hundredths, exactly")
    ok(all(fails(lambda t=t: price_int(t)) for t in ("0.5051", "1e-3", "-0.5", ".5", "0.5 ")) and
       all(fails(lambda t=t: size_int(t)) for t in ("1.234", "1e2", "-1", "")),
       "any other text of a price or a size is a failed assert")
    ok(x12(D("1.5")) == "1.500000000000" and x12(D("-0")) == "0.000000000000" and
       x12(D("-2.25")) == "-2.250000000000" and fails(lambda: x12(D("1e-13"))),
       "a unit's figure has twelve decimals exactly, and a figure with more is a failed assert")
    # our money: TZ-23's aggregate on our flipped rows, against this file's own arithmetic
    T0 = SYN_T + LEG
    fl = [(T0 * 10 ** 9 + 5 * 10 ** 9, "b", 480, 500, "m"), ((T0 + 61) * 10 ** 9, "a", 520, 1234, "x"),
          ((T0 + 299) * 10 ** 9 + 999 * MS_NS, "b", 70, 1, "m"), ((T0 + 200) * 10 ** 9, "a", 955, 250, "m")]
    life, bands = sums_of(T0, fl)
    ok(life["n"] == 4 and life["sh"] == D("19.85") and life["X"] == D("5") - D("12.34") + D("0.01") - D("2.5") and
       life["C"] == D("2.4") - D("6.4168") + D("0.0007") - D("2.3875") and bands["w0"]["n"] == 1 and
       bands["w1"]["n"] == 1 and bands["last"]["n"] == 1 and bands["w3"]["n"] == 1,
       "own rows: our bid +s Up at p, our ask -s at p; each fill in its band of [T0, T0 + 300)")
    ok(all(Fraction(str(life["X"] * up - life["C"] + life["R"])) == money_by_fill(fl, up) for up in (0, 1)),
       "X up - C + R equals the fill-by-fill money with the rebate, at either outcome")
    ok(fails(lambda: sums_of(T0, [((T0 + 300) * 10 ** 9, "b", 500, 500, "m")])) and
       fails(lambda: sums_of(T0, [(T0 * 10 ** 9 - 1, "b", 500, 500, "m")])),
       "a fill of ours at T0 + 300 or before T0 is a failed assert")
    # the synthetic window, replayed, against the Architect's reference and against its own rules by hand
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    try:
        paths = synth_stream(tmp)
        mem = {"T": SYN_T, "condition": SYN["m5"]["condition"], "up": SYN["m5"]["Up"],
               "files": [{"bytes": os.path.getsize(p)} for p in paths]}
        lines = member_unit(mem, paths)
        body = ("\n".join(lines) + "\n").encode("utf-8")
        ok(len(lines) == SYN_LINES and sha256_bytes(body) == SYN_DIGEST,
           "the synthetic window's unit, %d lines, byte for byte the Architect's reference" % SYN_LINES)
        fills = {}
        for ln in lines:
            f = ln.split(" ")
            if f[1] == "fill":
                fills.setdefault(f[2], []).append((int(f[3]), f[4], int(f[5]), int(f[6]), f[7]))
        ms = SYN_T * 1000
        ok(fills["front"][0] == (ms + 601000, "b", 480, 500, "m") and "behind" in fills and
           fills["behind"] == [(ms + 602000, "b", 480, 500, "m")],
           "front, first in its queue, fills at the first sale into its bid; behind, after the 100 shares displayed "
           "ahead of it, fills only when a sweep of 120 takes the level and 50 beyond")
        ok((ms + 603155, "a", 520, 500, "x") in fills["L250"] and
           not any(k == "x" for _t, _s, _p, _f, k in fills["behind"] + fills["L100"] + fills["front"]),
           "a bid placed at 0.52 against our ask fills it 150 ms later where our cancel arrives after that, at 250 "
           "ms; at 50 and 100 ms the cancel arrives first; front counts no crossing")
        ok(sum(1 for t, s, _p, _f, _k in fills["front"] if s == "b") == 4 and
           sum(1 for t, s, _p, _f, _k in fills["front_L0"] if s == "b") == 4,
           "front stops bidding once its known position reaches 20 shares")
        ok((ms + 895090, "b", 460, 500, "m") in fills["L100"] and (ms + 895090, "b", 460, 500, "m") in fills["L250"]
           and all(t < ms + 895000 for t, *_r in fills["behind"] + fills["front"]),
           "the stop at T0 + 295 cancels every order; at 100 and 250 ms the cancel arrives after a sale at "
           "T0 + 295.090, at 50 ms before it")
        got = parse_unit(SYN_T, body.decode("utf-8"))
        ok(got["variants"]["behind"]["refused"] == 1 and got["variants"]["L0"]["refused"] == 0 and
           got["variants"]["L0"]["crossings"] == 1 and got["book"] == {
               "snapshots": 9, "equal": 9, "touch_equal": 9, "matches": 8, "two_sided": 0, "sessions": 2, "closes": 3},
           "a bid arriving 50 ms after the ask came down to its price is refused, at 0 ms it is not; 9 book frames, "
           "every one equal to the rebuilt book, 8 matches, 2 sessions, 3 closes")
        for name, *_r in VARIANTS:
            mine = [x for x in fills.get(name, [])]
            z = got["variants"][name]
            ok(Fraction(str(z["X"] - z["C"] + z["R"])) == money_by_fill([(t * MS_NS,) + tuple(r) for t, *r in mine], 1)
               and z["n"] == len(mine), "%s: the unit's sums are its fills' money" % name)
        # the json path and the fast path: the same frames, every one formatted out of the fast path's reach
        slow = os.path.join(tmp, "slow")
        os.makedirs(slow)
        sp = []
        for p in paths:
            with gzip.open(p, "rt", encoding="utf-8") as fh:
                rows = fh.read().split("\n")
            rows = [r.replace('\\", \\"', '\\",\\"') for r in rows]
            q = os.path.join(slow, os.path.basename(p))
            with open(q, "wb") as fh:
                fh.write(gzip.compress("\n".join(rows).encode(), mtime=0))
            sp.append(q)
        ok(not any(PC_LINE.fullmatch(r) for q in sp for r in gzip.open(q, "rt", encoding="utf-8")) and
           sha256_bytes(("\n".join(member_unit(dict(mem, files=[{"bytes": os.path.getsize(p)} for p in paths]),
                                               sp)) + "\n").encode()) == SYN_DIGEST,
           "the same frames read by the general path alone give the same unit, byte for byte")
        # a set of three synthetic members: constants label-free, the score against the fill-by-fill money
        units = os.path.join(tmp, "units")
        os.makedirs(units)
        members, docs = [], []
        good = {"slug": "", "outcomes": '["Up", "Down"]', "outcomePrices": '["1", "0"]', "closed": True,
                "feeType": tz23.FEE_TYPE, "feeSchedule": dict(tz23.FEE_SCHEDULE), "eventStartTime": "",
                "conditionId": SYN["m5"]["condition"], "clobTokenIds": '["5001", "5002"]'}
        for k in range(3):
            t = SYN_T + k * WINDOW
            d = os.path.join(tmp, "w%d" % k)
            os.makedirs(d)
            ps = synth_stream(d, T=t)
            m = {"T": t, "condition": SYN["m5"]["condition"], "up": SYN["m5"]["Up"],
                 "files": [{"bytes": os.path.getsize(p)} for p in ps],
                 "doc": dict(good, slug="btc-updown-5m-%d" % (t + LEG), eventStartTime=tz23.iso(t + LEG),
                             outcomePrices='["1", "0"]' if k != 1 else '["0", "1"]')}
            write_atomic(os.path.join(units, "%d.txt" % t), ("\n".join(member_unit(m, ps)) + "\n").encode())
            members.append(m)
        s = {"members": members, "sha": "0" * 64}
        rows, wsha, nl = concat_units(members, units, os.path.join(tmp, "x-units.txt"))
        ok(nl == 3 * SYN_LINES and len(rows) == 3, "three members' units read back, %d lines" % (3 * SYN_LINES))
        const, csha = build_constants(s, rows, "x", tmp)
        res = score_rows(s, rows, const, "x", tmp)
        for name, *_r in VARIANTS:
            want = Fraction(0)
            for m in members:
                up = tz23.label_of(m["doc"])
                with open(os.path.join(units, "%d.txt" % m["T"]), encoding="utf-8") as fh:
                    fz = [ln.split(" ") for ln in fh.read().split("\n") if " fill %s " % name in ln]
                want += money_by_fill([(int(f[3]) * MS_NS, f[4], int(f[5]), int(f[6]), f[7]) for f in fz], up)
            ok(Fraction(str(res["variants"][name]["S"])) == want and
               sum((z["S"] for z in res["variants"][name]["bands"].values()), D(0)) == res["variants"][name]["S"] and
               sum((z["S"] for z in res["variants"][name]["kinds"].values()), D(0)) == res["variants"][name]["S"],
               "%s: S over the synthetic set is its fills' money; the bands' and the kinds' sums add to it" % name)
        flipped = [dict(m, doc=dict(m["doc"], outcomePrices='["0", "1"]' if m["doc"]["outcomePrices"] == '["1", "0"]'
                                    else '["1", "0"]')) for m in members]
        os.makedirs(os.path.join(tmp, "f"))
        c2, csha2 = build_constants({"members": flipped, "sha": "0" * 64}, rows, "x", os.path.join(tmp, "f"))
        r2 = score_rows({"members": flipped, "sha": "0" * 64}, rows, c2, "x", os.path.join(tmp, "f"))
        ok(csha2 == csha and r2["variants"]["front"]["S"] != res["variants"]["front"]["S"],
           "the constants are byte-identical with every label flipped, and the score moves (negative control)")
        ok(build_constants(s, rows, "x", tmp)[1] == csha, "a second constants run finds its file unchanged")
        # units: held, downloaded in order, replayed and removed; a unit on disk is not replayed again
        calls = []

        def fake_dl(tag, asset, nbytes, sha, dest):
            calls.append(asset)
            shutil.copyfile(os.path.join(tmp, asset), dest)
            return nbytes, 0.0, 0

        files = [{"file": "stream.1.jsonl.gz", "tag": "t", "asset": "%d-stream.1.jsonl.gz" % SYN_T, "bytes": 1,
                  "sha256": ""}, {"file": "stream.jsonl.gz", "tag": "t", "asset": "%d-stream.jsonl.gz" % SYN_T,
                                  "bytes": 1, "sha256": ""}]
        clk = [SYN_T + 20.0]
        u, rec = run_unit(SYN_T, files, os.path.join(tmp, "dl"), lambda ps: member_unit(mem, ps),
                          os.path.join(tmp, "timing.jsonl"), holdf=lambda b: (clk[0], 0.0), dl=fake_dl)
        ok(calls == ["%d-stream.jsonl.gz" % SYN_T, "%d-stream.1.jsonl.gz" % SYN_T] and
           sha256_bytes(("\n".join(u) + "\n").encode()) == SYN_DIGEST and os.listdir(os.path.join(tmp, "dl")) == []
           and rec["T"] == SYN_T and rec["bytes"] == 2 and rec["budget_s"] == 5 + 1 + UNIT_BUDGET_S,
           "a unit downloads its files in stream order, replays them, removes them, and is timed")
        seen = []
        replay_units([dict(mem, files=files)], os.path.join(tmp, "ru"), os.path.join(tmp, "t2.jsonl"), 1, tmp,
                     unit_fn=lambda T, f, d, fn, tm: (seen.append(T) or (["%d member x" % T], {"cpu_s": 0,
                                                                                                "bytes": 1})))
        replay_units([dict(mem, files=files)], os.path.join(tmp, "ru"), os.path.join(tmp, "t2.jsonl"), 1, tmp,
                     unit_fn=lambda T, f, d, fn, tm: (seen.append(T) or (["%d member x" % T], {"cpu_s": 0,
                                                                                                "bytes": 1})))
        ok(seen == [SYN_T], "a unit already on disk is not replayed again")
        few = [dict(mem, T=SYN_T + k * WINDOW, files=[{"bytes": 10 ** 6}]) for k in range(RESCORE_EVERY + 2)]
        cnt6 = []
        ok(fails(lambda: replay_units(few, os.path.join(tmp, "rq"), os.path.join(tmp, "t4.jsonl"), 30, tmp,
                                      unit_fn=lambda T, f, d, fn, tm: (cnt6.append(T) or (
                                          ["%d member x" % T], {"cpu_s": 5.0, "bytes": 10 ** 6})),
                                      project_after=RESCORE_PROJECT_AFTER)) and len(cnt6) == RESCORE_PROJECT_AFTER,
           "the rescore's 18, projected above its bound, stop BLOCKED after the first %d" % RESCORE_PROJECT_AFTER)
        many = [dict(mem, T=SYN_T + k * WINDOW, files=[{"bytes": 10 ** 6}]) for k in range(PROJECT_AFTER + 5)]
        cnt = []
        ok(fails(lambda: replay_units(many, os.path.join(tmp, "rp"), os.path.join(tmp, "t3.jsonl"), 100, tmp,
                                      unit_fn=lambda T, f, d, fn, tm: (cnt.append(T) or (
                                          ["%d member x" % T], {"cpu_s": 5.0, "bytes": 10 ** 6})))) and
           len(cnt) == PROJECT_AFTER, "the replays projected above their bound stop BLOCKED after the first %d "
                                      "units" % PROJECT_AFTER)
        # downloads against a local server: whole and verified, retried, then BLOCKED
        root = os.path.join(tmp, "srv")
        os.makedirs(root)
        blob = os.urandom(70000)
        with open(os.path.join(root, "a.gz"), "wb") as fh:
            fh.write(blob)

        class H(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *a, **k):
                super().__init__(*a, directory=root, **k)

            def log_message(self, *a):
                pass

        srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), H)
        th = threading.Thread(target=srv.serve_forever, daemon=True)
        th.start()
        try:
            urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler({})))
            url = lambda t, a: "http://127.0.0.1:%d/%s" % (srv.server_address[1], a)
            dest = os.path.join(tmp, "got.gz")
            nb, _s, k = download("t", "a.gz", len(blob), sha256_bytes(blob), dest, url_of=url, sleep=lambda s: None)
            with open(dest, "rb") as fh:
                ok(nb == len(blob) and k == 0 and fh.read() == blob, "a download arrives whole, verified by its bytes "
                                                                     "and SHA-256")
            slept = []
            ok(fails(lambda: download("t", "a.gz", len(blob), "0" * 64, dest + "2", url_of=url,
                                      sleep=slept.append)) and len(slept) == DL_TRIES and
               not os.path.exists(dest + "2.part") and not os.path.exists(dest + "2"),
               "a download whose SHA-256 differs is tried %d times and stops BLOCKED, leaving nothing" % DL_TRIES)
            slept.clear()
            ok(fails(lambda: download("t", "missing.gz", 1, "0" * 64, dest + "3", url_of=url, sleep=slept.append))
               and len(slept) == DL_TRIES, "a missing asset is tried %d times and stops BLOCKED" % DL_TRIES)
        finally:
            srv.shutdown()
            srv.server_close()
            urllib.request.install_opener(None)
        # the archive's record: every complete run's set.json against its record, each stream file in one set
        st_root = os.path.join(tmp, "archive")
        recs = []
        for a, ts in ((1792724420, [1792722600]), (1792810820, [1792723500, 1792724400])):
            doc = {"tag": "pairbook-streams-%d" % a, "assets_n": len(ts), "bytes_total": 10 * len(ts),
                   "assets": [{"T": t, "file": "stream.jsonl.gz", "asset": "%d-stream.jsonl.gz" % t, "bytes": 10,
                               "sha256": "0" * 64} for t in ts]}
            raw = json.dumps(doc).encode()
            os.makedirs(os.path.join(st_root, "runs", str(a)))
            with open(os.path.join(st_root, "runs", str(a), "set.json"), "wb") as fh:
                fh.write(raw)
            recs += [{"event": "start", "run": a, "wall_ns": 1}, {"event": "set", "run": a, "wall_ns": 2,
                                                                  "tag": doc["tag"], "assets_n": len(ts),
                                                                  "bytes_total": 10 * len(ts),
                                                                  "sha256": sha256_bytes(raw)},
                     {"event": "complete", "run": a, "wall_ns": 3}]
        amap = asset_map(archived_sets(recs, state=st_root))
        ok(sorted(amap) == [1792722600, 1792723500, 1792724400] and
           amap[1792724400]["stream.jsonl.gz"]["tag"] == "pairbook-streams-1792810820" and
           archived_sets(recs[:-1], state=st_root)[-1]["run"] == 1792724420,
           "every complete run's set.json gives its windows' assets; a run without its complete record gives none")
        bad = [dict(r, sha256="1" * 64) if r["event"] == "set" else r for r in recs]
        ok(fails(lambda: archived_sets(bad, state=st_root)) and fails(lambda: asset_map(
            archived_sets(recs, state=st_root) * 2)), "a set.json whose SHA-256 is not its record's, or a stream file "
                                                     "in two sets, is a failed assert")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    # the archive's wait
    clock = [float(LAST_T)]
    reads = []

    def reader(last):
        def r():
            reads.append(clock[0])
            return {last: {}}, last
        return r

    _a, waited = wait_archive(clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s),
                              read=reader(LAST_T))
    ok(waited == 0 and len(reads) == 1, "fetch starts at once where the archive has moved every candidate")
    clock[0] = ARCHIVE_WAIT_UNTIL - 125.0
    ok(fails(lambda: wait_archive(clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s),
                                  read=reader(LAST_T - WINDOW))) and clock[0] >= ARCHIVE_WAIT_UNTIL,
       "an archive short of the last candidate is read every 60 s and stops BLOCKED at 2026-10-27 06:00 UTC")
    # the set's rules on literal window.json and documents
    t = FIRST_T
    st = {"opened": True, "off_reason": None, "files": ["stream.jsonl.gz"], "cut": False,
          "subscribed_wall_ns": (t + 595) * 10 ** 9, "last_frame_wall_ns": (t + 904) * 10 ** 9,
          "max_gap_ns": 3 * 10 ** 9}
    wj = {"joined_late": False, "stopped": False, "stream": st,
          "markets": {"m5": {"slug": "btc-updown-5m-%d" % (t + LEG), "conditionId": "0x" + "c" * 64,
                             "clobTokenIds": '["11", "22"]', "outcomes": '["Up", "Down"]'}}}
    have = {t: {"stream.jsonl.gz": {}}}
    cases = [({}, None), ({"joined_late": True}, "stream: joined late or stopped"),
             ({"stream": dict(st, opened=False)}, "stream: not opened"), ({"stream": dict(st, cut=True)}, "stream: cut"),
             ({"stream": dict(st, subscribed_wall_ns=(t + 600) * 10 ** 9 + 1)}, "stream: subscribed late"),
             ({"stream": dict(st, last_frame_wall_ns=(t + 900) * 10 ** 9 - 1)}, "stream: ended early"),
             ({"stream": dict(st, max_gap_ns=GAP_MAX_NS + 1)}, "stream: a gap above 15 s"),
             ({"stream": dict(st, files=["stream.jsonl.gz", "stream.1.jsonl.gz"])}, "stream: not archived")]
    ok(all(stream_problem(dict(wj, **chg), t, have) == want for chg, want in cases) and
       stream_problem(None, t, have) == "stream: none",
       "a window's stream: opened, not cut or stopped, subscribed by T + 600, its last frame at or after T + 900, no "
       "gap above 15 s, every file archived")
    doc = {"slug": "btc-updown-5m-%d" % (t + LEG), "outcomes": '["Up", "Down"]', "outcomePrices": '["0", "1"]',
           "closed": True, "feeType": tz23.FEE_TYPE, "feeSchedule": dict(tz23.FEE_SCHEDULE),
           "eventStartTime": tz23.iso(t + LEG), "conditionId": "0x" + "c" * 64, "clobTokenIds": '["11", "22"]',
           "orderMinSize": 5}
    ok(leg_problem(wj, t, doc) is None and leg_problem(wj, t, dict(doc, orderMinSize=D(10))) == "document: order size"
       and leg_problem(wj, t, dict(doc, conditionId="0x" + "d" * 64)) == "window.json: the leg's condition or tokens"
       and leg_problem(wj, t, dict(doc, clobTokenIds='["22", "11"]')) == "window.json: the leg's condition or tokens"
       and leg_problem(wj, t, dict(doc, feeSchedule={})) == "document: fee" and leg_problem(wj, t, None) ==
       "document: absent" and leg_problem(wj, t + WINDOW, dict(doc, eventStartTime=tz23.iso(t + WINDOW + LEG))) ==
       "window.json: the leg's slug", "a leg's document: TZ-23's qualify, minimum order 5, and the condition and "
                                     "tokens window.json carries for it")
    # the clock: the idle stretch, the archive's calendar run and its service
    W = 1792458000
    idle = lambda s="inactive": (lambda: s)
    ok(quiet(W + 14, 60, idle()) is not None and quiet(W + 15, 60, idle()) is None and
       quiet(W + 530, 60, idle()) is None and quiet(W + 531, 60, idle()) is not None and
       quiet(W + 700, 60, idle()) is not None, "a unit of 60 s starts from second 15 to 530 of a window")
    calw = W // 86400 * 86400 + ARCHIVE_CALENDAR_S
    ok(quiet(calw - 5, 60, idle()) is not None and quiet(calw + 61, 60, idle()) is None and
       all(quiet(W + 100, 60, idle(s)) is not None for s in RUNNING) and quiet(W + 100, 60, idle("failed")) is None,
       "nothing starts near the archive's calendar run or while its service runs")
    clock = [W + 600.25]
    t1, waited = hold(60, clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s), state_of=idle())
    ok(int(t1) == W + 900 + 15, "held from second 600, a unit starts at second 15 of the next window")
    # the gate: TZ-23's thresholds on this TZ's lambda, W1's table and G-BOOK
    for g in GATED:
        vf, sf, want = PROJ[g]
        c = tz23.gate_constants(vf * NEED / PROJ_N, sf * NEED / PROJ_N, lam=LAMBDA[g], alpha=ALPHA, delta=DELTA)
        ok(abs(c["thr"] - want["thr"]) < D("1e-20") and want["power"][0] < c["power"] < want["power"][1],
           "%s: at the projected V and Sh the threshold is %s and the power between %s and %s, the Architect's" % (
               g, fx(want["thr"]), want["power"][0], want["power"][1]))
    T_ = {"earn": True, "no_earn": False}
    F_ = {"earn": False, "no_earn": False}
    ok(w1_reading({"behind": T_, "front": dict(F_, no_earn=True)}) == "W1-EARN" and
       w1_reading({"behind": F_, "front": dict(F_, no_earn=True)}) == "W1-NO-EARN" and
       w1_reading({"behind": dict(F_, no_earn=True), "front": dict(F_, earn=True)}) == "UNDECIDABLE" and
       w1_reading({"behind": T_, "front": F_}) == "W1-EARN",
       "W1-EARN on behind's EARN bound, first; W1-NO-EARN on front's NO EARN bound; UNDECIDABLE otherwise")
    c = tz23.gate_constants(D(10 ** 4), D(10 ** 6), lam=LAMBDA["front"], alpha=ALPHA, delta=DELTA)
    th = {"earn_at": c["earn_at"], "no_earn_at": c["no_earn_at"]}
    ok(c["earn_at"] == c["thr"] and c["no_earn_at"] == DELTA * D(10 ** 6) - c["thr"] and c["thr"] < c["no_earn_at"]
       and [tz23.reading(x, th)[0] for x in (c["thr"] - 1, c["thr"], c["no_earn_at"] + 1)] ==
       ["NO EARN", "EARN", "EARN"], "TZ-23's reading on this TZ's lambda: EARN at S >= thr, NO EARN at "
                                   "S <= delta Sh - thr, EARN first where both hold")
    c2 = tz23.gate_constants(D(10 ** 9), D(10 ** 5), lam=LAMBDA["front"], alpha=ALPHA, delta=DELTA)
    th2 = {"earn_at": c2["earn_at"], "no_earn_at": c2["no_earn_at"]}
    ok(c2["no_earn_at"] < c2["thr"] and [tz23.reading(x, th2)[0] for x in (
        c2["no_earn_at"], c2["no_earn_at"] + 1, c2["thr"] - 1, c2["thr"])] ==
       ["NO EARN", "UNDECIDABLE", "UNDECIDABLE", "EARN"], "UNDECIDABLE between the bounds where they part")
    ok(book_reading(1000, 990) == "PASS" and book_reading(1000, 989) == "FAIL" and book_reading(0, 0) == "FAIL" and
       touch_of({480: 100, 470: 5}, {520: 7}) == (480, 100, 520, 7) and touch_of({}, {520: 7}) == (None, None, 520, 7),
       "G-BOOK: the rebuilt touch, each best price and its size, equal at 99 of every 100 match frames; a set with "
       "none fails")
    # G-STILL: unchanged, or the pair book moved by a chain of the archive's own restart records
    u0 = {"recorder": {"MainPID": "4148534", "NRestarts": "2", "ActiveState": "active"},
          "pairbook": {"MainPID": "2221487", "NRestarts": "19", "ActiveState": "active"}}
    u2 = {"recorder": dict(u0["recorder"]), "pairbook": {"MainPID": "30", "NRestarts": "21", "ActiveState": "active"}}
    chain = [{"event": "restart", "stopped": 2221487, "pid": 20, "NRestarts": "20"},
             {"event": "restart", "stopped": 20, "pid": 30, "NRestarts": "21"}]
    ok(still_reading(u0, json.loads(json.dumps(u0)), []) == (True, "unchanged") and
       still_reading(u0, u2, chain)[0] and not still_reading(u0, u2, chain[:1])[0] and
       not still_reading(u0, u2, chain[::-1])[0] and not still_reading(u0, u2, [])[0] and
       not still_reading(u0, dict(u2, recorder=dict(u0["recorder"], MainPID="1")), chain)[0],
       "G-STILL: unchanged, or the pair book moved by a chain of the archive's restart records; any other change fails")
    # the archive's ledger, summarized from literal records
    recs = [{"event": "start", "run": 1792378820, "wall_ns": 1}, {"event": "set", "run": 1792378820, "wall_ns": 2,
            "tag": "pairbook-streams-1792378820", "assets_n": 96, "bytes_total": 10, "first_T": 1792291500,
            "last_T": 1792377000}, {"event": "complete", "run": 1792378820, "wall_ns": 3},
            {"event": "start", "run": 1792045110, "wall_ns": 4},
            {"event": "halt", "run": 1792045110, "wall_ns": 6, "phase": "restart", "reason": "x"}]
    summ = ledger_summary(recs)
    ok(summ["runs"] == [1792378820, 1792045110] and "calendar" in summ["lines"][0] and
       "off-calendar, second 22710" in summ["lines"][1] and summ["halted"] and
       summ["terminal"] == {1792378820: ["complete"], 1792045110: ["halt"]},
       "the ledger's runs, terminals, calendar and halt")
    # the fingerprint's rows, on literal lines
    lines = ("| `research/tz23-maker-m0.py` | 1,184 | 54,885 | frozen | `%s` |\n"
             "| `SYSTEM-MAP.md` | — | — | reported | self-reference; report the value you compute |\n"
             "| `A6` — pricer | `729f0bcdbee3` |\n" % TZ23_SHA256)
    ok(ROW.findall(lines) == [("research/tz23-maker-m0.py", "1,184", "54,885", "frozen", TZ23_SHA256),
                              ("SYSTEM-MAP.md", "—", "—", "reported",
                               "self-reference; report the value you compute")] and
       dict(ANCHOR_ROW.findall(lines)) == {"A6": "729f0bcdbee3"}, "the map's rows and anchors parse")
    ok(reclaimable(WORK) and not reclaimable(FORENSICS) and not reclaimable("/tmp/x/" + "0" * 8 + "-0000-0000-0000-"
                                                                           + "0" * 12),
       "reclaim takes the work tree and refuses the forensic store and a directory outside a session's")
    # the audit hook: section 2's reads, writes, requests and processes, each refused before it happens
    pw = PAIRBOOK + "/%d/window.json" % FIRST_T
    ok(policy("fetch", "open", (pw, "rb", 0)) is None and
       policy("fetch", "open", (PAIRBOOK + "/%d/window.json" % (FIRST_T - WINDOW), "rb", 0)) is not None and
       policy("fetch", "open", (PAIRBOOK + "/%d/window.json" % (LAST_T + WINDOW), "rb", 0)) is not None and
       policy("fetch", "open", (PAIRBOOK + "/%d/stream.jsonl.gz" % FIRST_T, "rb", 0)) is not None and
       policy("replay", "open", (pw, "rb", 0)) is not None and policy("fetch", "open", (pw, "wb", 0)) is not None and
       policy("fetch", "os.listdir", (PAIRBOOK,)) is not None,
       "the pair book's root: window.json of a candidate read by fetch alone, nothing else opened, listed or written")
    ok(policy("archive", "open", (ARCHIVE_LEDGER, "rb", 0)) is None and
       policy("still", "open", (ARCHIVE_LEDGER, "rb", 0)) is None and
       policy("fetch", "open", (ARCHIVE_STATE + "/runs/1792724420/set.json", "rb", 0)) is None and
       policy("still", "open", (ARCHIVE_STATE + "/runs/1792724420/set.json", "rb", 0)) is not None and
       policy("score", "open", (ARCHIVE_LEDGER, "rb", 0)) is not None and
       policy("archive", "open", (ARCHIVE_LEDGER, "ab", os.O_WRONLY)) is not None and
       policy("archive", "open", (ARCHIVE_STATE + "/archive.log", "rb", 0)) is not None,
       "the archive's state: its ledger read by archive, fetch and still, its runs' set.json by archive and fetch, "
       "nothing written")
    ok(all(policy(m, "urllib.Request", ("https://github.com/x",)) is None for m in ("rehearse", "replay", "rescore"))
       and policy("fetch", "urllib.Request", ("https://github.com/x",)) is not None and
       all(policy(m, "urllib.Request", ("https://gamma-api.polymarket.com/markets",)) is None
           for m in ("rehearse", "fetch")) and
       policy("replay", "urllib.Request", ("https://gamma-api.polymarket.com/markets",)) is not None and
       policy("score", "urllib.Request", ("https://data-api.polymarket.com/v2/trades",)) is not None and
       policy("fetch", "urllib.Request", ("https://clob.polymarket.com/book",)) is not None,
       "downloads in rehearse, replay and rescore alone; documents in rehearse and fetch alone; nothing else")
    ok(policy("reclaim", "open", (FORENSICS + "/x", "xb", 0)) is None and
       policy("reclaim", "open", (FORENSICS + "/x", "wb", 0)) is not None and
       policy("score", "open", (FORENSICS + "/x", "xb", 0)) is not None and
       policy("score", "open", ("/root/elsewhere", "wb", 0)) is not None and
       policy("score", "open", (FORENSICS + "/x", "rb", 0)) is None and
       policy("score", "subprocess.Popen", ("/usr/bin/curl", ["curl"])) is not None and
       policy("score", "subprocess.Popen", ("git", ["git"])) is None,
       "the forensic store written by reclaim's exclusive create alone, nothing outside the work tree, and no "
       "process but git, systemctl and stat")
    MODE[0] = "selftest"
    refused = []
    for p in (PAIRBOOK + "/runtime.jsonl", ARCHIVE_LEDGER, CHAINBOOK + "/runtime.jsonl"):
        try:
            open(p, "rb")
            refused.append("opened")
        except GuardError:
            refused.append("tz32")
        except RuntimeError:
            refused.append("tz23")
        except OSError:
            refused.append("not refused")
    ok(refused == ["tz32", "tz32", "tz23"] and tz23.OPENS[-1] == CHAINBOOK + "/runtime.jsonl",
       "opens under the pair book's root and of the archive's ledger are refused by this hook, under the chain book's "
       "root by TZ-23's, each before it happens")
    tz23.OPENS.clear()
    del REFUSED[:]
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz32-our-quoting.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "still": mode_still,
             "archive": mode_archive, "rehearse": mode_rehearse, "fetch": mode_fetch, "replay": mode_replay,
             "rescore": mode_rescore, "score": mode_score}
    if mode == "reclaim":
        mode_reclaim(rest)
    elif mode == "scratch":
        assert len(rest) == 1, "scratch OWN"
        mode_scratch(rest[0])
    else:
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    out("malloc tuned: %s" % tz23.MALLOC_TUNED)
    out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
    out("opens refused: %d; under the recorder's and the chain book's roots by TZ-23's hook: %d" % (
        len(REFUSED), len(tz23.OPENS)))


if __name__ == "__main__":
    main(sys.argv[1:])
