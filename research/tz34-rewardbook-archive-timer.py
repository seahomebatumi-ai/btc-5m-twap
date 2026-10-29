#!/usr/bin/env python3
"""TZ-34 - the reward book's archive on a timer: the stream files of its closed slots moved verbatim to a Release
once a day by btc-rewardbook-archive.timer, through TZ-27's proofs and TZ-28's idle stretch and ledger, every
request and every removal inside the pair book's idle stretch.

    run               the unit's one mode, ExecStart of btc-rewardbook-archive.service: a new set as of now, or the
                      pending one resumed; the upload and the verify through TZ-27's and TZ-28's own functions, then
                      each file hashed again and removed while the reward book is not about to read its store's
                      sizes; one record a step in /var/lib/btc-rewardbook-archive/ledger.jsonl. Exit 0 complete or
                      empty; 75 deferred - the next run resumes it; 1 halted - the run disables its own timer; 2 not
                      started
    fingerprint       map section 0 against the primary checkout
    selftest          every rule of this file, on literals, temporary stores, a simulated reward book and a loopback
                      server only
    path              P-PATH, TZ-28's own: the run's request path with no token, held to the idle stretch
    path-token        P-TOKEN, TZ-28's own and the Boss's alone: the run's credential reads the repository, with push
    installed         G-INSTALL: the service's four files, the two units and the empty state directory
    mark NAME         enable, retry or stop: an instant and the archive's two units into state.json
    timer             G-TIMER: the timer as installed and enabled, and its next calendar elapse
    first             the first run after the enable mark, re-read: G-TRIGGER, G-RUN and the run's own readings;
                      exit 3 NOT YET
    final             G-TIMER and G-STILL; the store and the next stop, projected
    still             the recorder, the pair book and the reward book: the first run records them, a later run
                      compares (G-STILL)
    stopped           after K-34: the timer disabled, no run in progress
    scratch OWN, reclaim TREE...   TZ-27's own modes, unchanged

TZ-28's instrument, research/tz28-pairbook-archive-timer.py, is loaded from beside this file and asserted by its
SHA-256; it loads TZ-27's from beside itself the same way, and TZ-27's audit hook is installed then. This file points
that hook at the reward book's store and adds its own for the rest of TZ-34 section 2. No mode decompresses a stream
file, and none opens a rewards file or a selection; none prints a price, a size, a side, a book's hash, a rate or an
outcome. Run it with /root/tz04a-env; it needs the standard library alone.

Written for CryptoTZ/TZ-34-rewardbook-archive-timer.md. The TZ is the specification.
"""

import ast
import fcntl
import hashlib
import http.server
import json
import os
import re
import resource
import shutil
import subprocess
import sys
import threading
import time
import types
from fractions import Fraction

if not __debug__:
    sys.stderr.write("tz34: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(1)

HERE = os.path.dirname(os.path.abspath(__file__))
SELF_NAME = "tz34-rewardbook-archive-timer.py"
TZ28_NAME = "tz28-pairbook-archive-timer.py"
TZ28_SHA256 = "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4"
TZ27_NAME = "tz27-pairbook-archive.py"
TZ27_SHA256 = "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673"
TZ33_NAME = "tz33-reward-book-capture.py"
TZ33_SHA256 = "a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670"


def load_tz28(path):
    """TZ-28's instrument, executed from the very bytes whose SHA-256 is asserted. It loads TZ-27's from beside
    itself by TZ-27's SHA-256, and TZ-27's audit hook is installed then."""
    with open(path, "rb") as fh:
        raw = fh.read()
    got = hashlib.sha256(raw).hexdigest()
    assert got == TZ28_SHA256, "%s sha256 %s, required %s" % (path, got, TZ28_SHA256)
    mod = types.ModuleType("tz28")
    mod.__file__ = path
    sys.modules["tz28"] = mod
    exec(compile(raw, path, "exec"), mod.__dict__)
    return mod


tz28 = load_tz28(os.path.join(HERE, TZ28_NAME))
tz27 = tz28.tz27
assert tz28.TZ27_SHA256 == TZ27_SHA256 and tz27.__file__ == os.path.join(HERE, TZ27_NAME), "TZ-27's file"
out = tz27.out

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------------

MAP_REVISION = "2026-10-28-a"
MAP_ROWS = {"frozen": 43, "tracked": 2, "reported": 1}

ROOT = "/var/lib/btc-rewardbook"             # the reward book's store (TZ-33 section 1)
PAIRBOOK = "/var/lib/btc-pairbook"
PAIR_STATE = "/var/lib/btc-pairbook-archive"
PAIR_LEDGER = PAIR_STATE + "/ledger.jsonl"
STATE = "/var/lib/btc-rewardbook-archive"
ASVC = "/root/btc-rewardbook-archive-svc"
ARCHIVE = "btc-rewardbook-archive.service"
TIMER = "btc-rewardbook-archive.timer"
REWARD_UNIT = "btc-rewardbook.service"
PAIR_ARCHIVE = "btc-pairbook-archive.service"
PAIR_TIMER = "btc-pairbook-archive.timer"
UNITS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service", "rewardbook": REWARD_UNIT}
UNIT_DIR = "/etc/systemd/system"
RUN_ARGV = (tz27.PYTHON, "-B", "-u", ASVC + "/" + SELF_NAME, "run")
CALENDAR = "*-*-* 01:30:20 UTC"
CALENDAR_S = 1 * 3600 + 30 * 60 + 20       # the calendar elapse, seconds after 00:00 UTC
ACTIVE_S = 1800                            # OnActiveSec: the first run, 1,800 s after the timer starts
TIMEOUT_S = 21600                          # TimeoutStartSec of the service
ARCHIVE_MEMORY_MAX = 134217728             # MemoryMax=128M
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")

# the reward book's own, restated from research/tz33-reward-book-capture.py and asserted against its text by the
# self-test: lines 114, 120, 133 to 135, 143, 168, 169, 171, 173, 190 to 192, 227 and 228
REWARD_SVC = "/root/btc-rewardbook-svc"
REWARD_ARGV = (tz27.PYTHON, "-B", "-u", REWARD_SVC + "/" + TZ33_NAME, "serve")
DAY = 86400
SLOT = 900
OPEN_BEFORE = 5
SLOT_JSON_AT = 910
LAUNCH_LEAD = 1
STREAM_FLOOR = 7300000000
STREAM_CAP = 4000000000
SLOT_STREAM_MAX = 100000000
DAY_RE = re.compile(r"[0-9]{10}")
SLOT_FILE_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.(stream\.jsonl\.gz|rewards\.jsonl\.gz|slot\.json)")
RESTATED = {"ROOT": ROOT, "SVC": REWARD_SVC, "SERVICE_ARGV": REWARD_ARGV, "DAY": DAY, "SLOT": SLOT,
            "OPEN_BEFORE": OPEN_BEFORE, "SLOT_JSON_AT": SLOT_JSON_AT, "LAUNCH_LEAD": LAUNCH_LEAD,
            "STREAM_FLOOR": STREAM_FLOOR, "STREAM_CAP": STREAM_CAP, "SLOT_STREAM_MAX": SLOT_STREAM_MAX,
            "DAY_RE": DAY_RE.pattern, "SLOT_FILE_RE": SLOT_FILE_RE.pattern}

# this TZ's own
SETTLE_S = 60                     # a slot is taken once its slot.json was due at least 60 s before A
DECIDE_S = OPEN_BEFORE + LAUNCH_LEAD    # the reward book decides a slot's stream at S - 6
SELECT_AGE_S = 5                  # the day's selection recorded at least 5 s before a removal
START_AGE_S = 10                  # the reward book's process started at least 10 s before a removal
QUIET_STEP_S = 1
QUIET_MAX_S = 1800                # the removals wait at most this in all for the reward book's quiet, then defer
HOLD_STEP_S = 10
HOLD_MAX_S = 1800                 # a phase waits at most this while the pair book's archive runs, then defers
NEXT_AFTER_S = 900                # G-NEXT: the slots decided from the first removal to 900 s after the last
NEXT_SETTLE_S = 30                # read 30 s after each one's slot.json is due
DISK_FLOOR = 2002000000           # the recorder's floor, 2,000,000,000, plus 2,000,000 a run writes at most
RUN_MEM_FLOOR = 73121792          # MemAvailable: twice the run's measured peak (TZ-34 section 0.4)
PRE_DELETE = ("set", "upload", "verify")

TAG_PREFIX = "rewardbook-streams-"
TAG_RE = re.compile(r"rewardbook-streams-[0-9]{10}")
ASSET_RE = re.compile(r"([0-9]{10})-(([0-9]{10})\.([0-9]+)\.stream\.jsonl\.gz)")
STREAM_PATH_RE = re.compile(r"[0-9]{10}/[0-9]{10}\.[0-9]+\.stream\.jsonl\.gz")
SLOT_JSON_PATH_RE = re.compile(r"[0-9]{10}/[0-9]{10}\.[0-9]+\.slot\.json")

SET_KEYS = frozenset(("tag", "as_of", "root", "repo", "assets", "assets_n", "bytes_total", "first_S", "last_S",
                      "slots", "deferred"))
SET_ASSET_KEYS = frozenset(("T", "S", "k", "file", "asset", "bytes", "sha256"))
SET_SLOT_KEYS = frozenset(("S", "disposition", "streams", "stream_bytes", "taken"))
DELETE_ROW_KEYS = frozenset(("asset", "T", "S", "k", "file", "bytes", "sha256", "start_ns", "removed_wall_ns"))

# ---- TZ-27's hook, pointed at the reward book's store; and this file's own -------------------------------------
#
# TZ-27's policy reads its module's ROOT at every event: rebound here, before any mode acts, it guards the reward
# book's store as TZ-27 section 2 guarded the pair book's - read by its READ_MODES, listed by its LIST_MODES, never
# written, a file removed only in mode delete and only where the run names it - and the pair book's store, which it
# no longer names, is refused by policy34 below.

tz27.ROOT = ROOT
assert tz27.ROOT == ROOT and tz28.tz27 is tz27

REFUSED34 = []


def _rel(p, root):
    return p[len(root) + 1:] if p.startswith(root + "/") else ""


def policy34(mode, event, args):
    """None where TZ-34 section 2 allows the event in this mode, beside TZ-27's hook; otherwise the reason."""
    p = tz27._path(args[0]) if args else None
    if event == "open":
        if p is None:
            return None
        wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
        w = tz27._writing(wm, fl)
        if tz27._under(p, PAIRBOOK):
            return "the pair book's store"
        if tz27._under(p, PAIR_STATE):
            if p == PAIR_LEDGER and not w and mode == "still":
                return None
            return "the pair book's archive"
        if tz27._under(p, ROOT):
            if w:
                return "a write under the reward book's store"
            rel = _rel(p, ROOT)
            if STREAM_PATH_RE.fullmatch(rel):
                return None if mode in ("inventory", "upload", "delete") else "a stream file read in mode %s" % mode
            if SLOT_JSON_PATH_RE.fullmatch(rel):
                return None if mode == "final" else "a slot.json read in mode %s" % mode
            if rel == "runtime.jsonl":
                return None if mode in ("delete", "final") else "runtime.jsonl read in mode %s" % mode
            return "a file of the reward book's store this TZ never reads"
        return None
    if event in ("os.listdir", "os.scandir"):
        if p is None:
            return None
        if tz27._under(p, PAIRBOOK) or tz27._under(p, PAIR_STATE):
            return "a listing under the pair book's store or its archive"
        if tz27._under(p, ROOT):
            return None if mode in ("inventory", "delete", "final") else "a listing under the reward book's store"
        return None
    if event in tz27.CHANGE_EVENTS:
        paths = [p]
        if event in ("os.rename", "os.link", "os.symlink") and len(args) > 1:
            paths.append(tz27._path(args[1]))
        for q in paths:
            if q is None:
                continue
            if tz27._under(q, PAIRBOOK) or tz27._under(q, PAIR_STATE):
                return "a change under the pair book's store or its archive"
            if tz27._under(q, ROOT):
                if (event == "os.remove" and mode == "delete" and q in tz27.ALLOWED_REMOVE
                        and STREAM_PATH_RE.fullmatch(_rel(q, ROOT))):
                    continue
                return "a change under the reward book's store"
        return None
    return None


def _audit34(event, args):
    if event not in tz27.HOOKED:
        return
    why = policy34(tz27.MODE[0], event, args)
    if why is not None:
        REFUSED34.append((event, str(args[0]) if args else ""))
        raise tz27.GuardError("%s refused in mode %s, %s: %r" % (event, tz27.MODE[0], why, args[0] if args else None))


sys.addaudithook(_audit34)

# ---- the reward book's store, by its own names --------------------------------------------------------------


def day_of(t):
    return int(t) // DAY * DAY


def day_dirs(root):
    """The day directories under root - ten digits, a multiple of 86,400 - in order."""
    with os.scandir(root) as it:
        names = [d.name for d in it if d.is_dir(follow_symlinks=False) and DAY_RE.fullmatch(d.name)]
    for n in names:
        assert int(n) % DAY == 0, "a day directory named %r" % n
    return sorted(int(n) for n in names)


def slot_files(names, d0):
    """A day directory's slot files by slot: {S: {"streams": [(k, name)], "closed": bool}}; every slot in its day."""
    by = {}
    for n in names:
        m = SLOT_FILE_RE.fullmatch(n)
        if m is None:
            continue
        s, k, kind = int(m.group(1)), int(m.group(2)), m.group(3)
        assert s % SLOT == 0 and day_of(s) == d0, "%s in the day directory %d" % (n, d0)
        e = by.setdefault(s, {"streams": [], "closed": False})
        if kind == "stream.jsonl.gz":
            e["streams"].append((k, n))
        elif kind == "slot.json":
            e["closed"] = True
    return by


def inventory(root, a, max_assets=tz27.RUN_MAX_ASSETS):
    """The set as of the epoch a: every stream file of every slot that holds a slot.json and whose slot.json was due
    at least SETTLE_S before a - S + 910 + 60 <= a - in order of S and of the file's index; the first max_assets
    taken, each read as bytes for its SHA-256, its size and mtime equal before and after. The slots considered are the
    slots due by a that hold a stream file, each closed or unclosed; a slot due after a is counted as open, a slot due
    by a with no stream file as streamless, and neither is listed, so the set is a function of a alone."""
    slots, files, open_n, streamless = [], [], 0, 0
    for d0 in day_dirs(root):
        by = slot_files(tz27.window_names(root, d0), d0)
        for s in sorted(by):
            if s + SLOT_JSON_AT + SETTLE_S > a:
                open_n += 1
                continue
            streams = sorted(by[s]["streams"])
            if not streams:
                streamless += 1
                continue
            sizes = [os.stat(os.path.join(root, str(d0), n), follow_symlinks=False).st_size for _k, n in streams]
            disp = "closed" if by[s]["closed"] else "unclosed"
            slots.append({"S": s, "disposition": disp, "streams": len(streams), "stream_bytes": sum(sizes),
                          "taken": 0})
            if disp == "closed":
                files.extend((d0, s, k, n) for k, n in streams)
    taken, assets = files[:max_assets], []
    for d0, s, k, n in taken:
        p = os.path.join(root, str(d0), n)
        before = os.stat(p, follow_symlinks=False)
        h, nbytes = tz27.sha256_file(p)
        after = os.stat(p, follow_symlinks=False)
        assert before.st_size == nbytes == after.st_size and before.st_mtime_ns == after.st_mtime_ns, \
            "%s changed while it was read" % p
        assets.append({"T": d0, "S": s, "k": k, "file": n, "asset": "%d-%s" % (d0, n), "bytes": nbytes, "sha256": h})
    for e in slots:
        e["taken"] = sum(1 for _d, s, _k, _n in taken if s == e["S"])
    return assets, slots, len(files) - len(taken), open_n, streamless


def stream_bytes_view(root):
    """The service's own stream_bytes_total (research/tz33-reward-book-capture.py lines 1279 to 1291), restated:
    the bytes of every stream file under root, by directory entries alone."""
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


def set_document(tag, a, root, assets, slots, deferred):
    """The set under this TZ's tag, which neither TZ-27's nor TZ-28's tag rule covers, every file small enough for one
    idle stretch."""
    names = [x["asset"] for x in assets]
    assert TAG_RE.fullmatch(tag) and tz27.TAG_RE.fullmatch(tag) is None and tz28.TAG_RE.fullmatch(tag) is None, \
        "a tag named %r" % tag
    assert assets, "no stream file of a closed slot"
    assert len(set(names)) == len(names), "two assets share a name"
    for x in assets:
        m = ASSET_RE.fullmatch(x["asset"])
        assert m is not None and int(m.group(1)) == x["T"] == day_of(x["S"]) and m.group(2) == x["file"] \
            and int(m.group(3)) == x["S"] and int(m.group(4)) == x["k"], "an asset named %r" % x["asset"]
    assert len(assets) <= tz27.RUN_MAX_ASSETS, "%d assets, above %d" % (len(assets), tz27.RUN_MAX_ASSETS)
    big = [x["asset"] for x in assets if x["bytes"] > tz28.IDLE_MAX_BYTES]
    assert not big, "files above the %d bytes one idle stretch carries: %r" % (tz28.IDLE_MAX_BYTES, big[:3])
    doc = {"tag": tag, "as_of": a, "root": root, "repo": tz27.REPO, "assets": assets, "assets_n": len(assets),
           "bytes_total": sum(x["bytes"] for x in assets), "first_S": assets[0]["S"], "last_S": assets[-1]["S"],
           "slots": slots, "deferred": deferred}
    tz27.assert_keys(doc, SET_KEYS, "set.json")
    for x in assets:
        tz27.assert_keys(x, SET_ASSET_KEYS, "set.json asset")
        assert tz27.SHA_RE.fullmatch(x["sha256"])
    for e in slots:
        tz27.assert_keys(e, SET_SLOT_KEYS, "set.json slot")
    return doc


def release_text(doc, commit):
    name = "%s: the reward book's streams, slots %d to %d" % (doc["tag"], doc["first_S"], doc["last_S"])
    body = ("Verbatim stream files of btc-rewardbook.service (research/tz33-reward-book-capture.py), one asset per "
            "file, named <D0>-<S>.<k>.stream.jsonl.gz: the CLOB market websocket's frames for both tokens of each UTC "
            "day's 150 reward markets, S-5 to S+905. %d files, %d bytes, slots %d to %d, taken as of %d by "
            "btc-rewardbook-archive.service at commit %s (research/tz34-rewardbook-archive-timer.py, TZ-34). Reserved "
            "for L0's measurement: until it, no TZ extracts a price, a size, a side, a book's hash, a rate, a "
            "competitiveness or an outcome from them (CANON PART II). Each asset's SHA-256 is its digest here." % (
                doc["assets_n"], doc["bytes_total"], doc["first_S"], doc["last_S"], doc["as_of"], commit))
    return name, body


def slot_names(root, s):
    """The slot.json names of slot s in its day directory, by index."""
    d0 = day_of(s)
    if not os.path.isdir(os.path.join(root, str(d0))):
        return []
    found = []
    for n in tz27.window_names(root, d0):
        m = SLOT_FILE_RE.fullmatch(n)
        if m is not None and int(m.group(1)) == s and m.group(3) == "slot.json":
            found.append((int(m.group(2)), n))
    return sorted(found)


def removed_reading(root, doc, done):
    """G-DELETE read back, removing nothing: every file of the set absent, its removal recorded, and each of its
    slots still holding its slot.json."""
    slots = sorted({x["S"] for x in doc["assets"]})
    gone = [x for x in doc["assets"] if not os.path.lexists(os.path.join(root, str(x["T"]), x["file"]))]
    kept = [s for s in slots if slot_names(root, s)]
    return {"every file of the set absent": len(gone) == doc["assets_n"],
            "each removal recorded": all(x["asset"] in done for x in doc["assets"]),
            "each slot keeps its slot.json": kept == slots}, len(gone), len(kept)


def projection(bytes_total, first_s, last_s, counter, free, now):
    """The streams' rate over the set's span, and the instants at which the reward book's cap and floor stop them
    again; printed, never gated."""
    rate = Fraction(bytes_total * 86400, last_s - first_s + SLOT)
    cap_days = Fraction(STREAM_CAP - counter) / rate if counter < STREAM_CAP else Fraction(0)
    rows = [("the cap", cap_days)]
    for base in tz27.BASE_DRAINS:
        d = Fraction(free - STREAM_FLOOR) / (rate + base) if free > STREAM_FLOOR else Fraction(0)
        rows.append(("the floor, base %d bytes a day" % base, d))
    return rate, [(what, d, now + int(d * 86400)) for what, d in rows]


def removal_span(row):
    """A removal as G-IDLE reads a request: its start, its end and its budget."""
    return {"start_ns": row["start_ns"], "end_ns": row["removed_wall_ns"], "budget_s": tz28.budget_s(row["bytes"])}

# ---- the reward book, read: its quiet before a removal, its slots after it, and G-STILL ------------------------


def quiet(recs, pids, now):
    """None where a removal may start at `now`; else why it waits. The reward book sums its store's stream files at a
    slot's decision, S - 6 - later only while the day's selection is missing - and at a process's start: the day of
    the slot it streams has its selection recorded at least SELECT_AGE_S ago, and no process runs under its argv but
    the one whose start record is at least START_AGE_S old."""
    d0 = day_of(now)
    sel = [r for r in recs if r.get("event") == "select" and r.get("day") == d0 and r.get("ok") is True]
    if not sel or sel[0].get("wall_ns", 0) > (now - SELECT_AGE_S) * 10 ** 9:
        return "the selection of day %d not recorded %d s before" % (d0, SELECT_AGE_S)
    if pids:
        starts = [r for r in recs if r.get("event") == "start"]
        if not starts or sorted(pids) != [starts[-1].get("pid")]:
            return "a process of the reward book, %r, without its start record" % sorted(pids)
        if starts[-1].get("wall_ns", 0) > (now - START_AGE_S) * 10 ** 9:
            return "the reward book's process started less than %d s before" % START_AGE_S
    return None


def next_slots(first_ns, last_ns):
    """The slots whose decision instant S - 6 lies from the run's first removal to NEXT_AFTER_S after its last: those
    the reward book decided while the run removed files, and the first it decided after."""
    s = -(-(first_ns + DECIDE_S * 10 ** 9) // (SLOT * 10 ** 9)) * SLOT
    found = []
    while (s - DECIDE_S) * 10 ** 9 < last_ns + NEXT_AFTER_S * 10 ** 9:
        found.append(s)
        s += SLOT
    return found


def next_verdict(sjs, errors, pid0):
    """One slot across the removal, from its slot.json files [(k, doc)] and the error records of its task: FAIL where
    its task left an error record or no slot.json; PASS where the process the run began beside streamed it with no
    reason to keep it off; UNDECIDABLE where it stayed off for a reason the run does not act on, or another process
    ran it."""
    if errors:
        return "FAIL", "an error record of its task: %s" % str(errors[0].get("error"))[:160]
    if not sjs:
        return "FAIL", "no slot.json"
    why = []
    for k, sj in sjs:
        st = sj.get("stream") if isinstance(sj.get("stream"), dict) else {}
        if (str(sj.get("pid")) == str(pid0) and st.get("opened") is True and st.get("off_reason") is None
                and sj.get("error") is None and sj.get("stopped") is False):
            return "PASS", "index %d streamed by %s" % (k, pid0)
        why.append("index %d: pid %s, opened %s, off %s, stopped %s, error %s" % (
            k, sj.get("pid"), st.get("opened"), st.get("off_reason"), sj.get("stopped"), sj.get("error")))
    return "UNDECIDABLE", "; ".join(why)


def next_reading(verdicts):
    """The worst over the slots: FAIL, else UNDECIDABLE, else PASS."""
    vs = [v for v, _w in verdicts]
    return "FAIL" if "FAIL" in vs else ("UNDECIDABLE" if "UNDECIDABLE" in vs or not vs else "PASS")


def trigger_reading(trg, mark_s, s0, last_trigger):
    """G-TRIGGER, pure: the run's own trigger where systemd set it - TRIGGER_UNIT this timer, its elapse at least
    ACTIVE_S after the enable mark, less 2 s for whole-second stamps, and the run's first record within 60 s after it -
    else the timer's LastTriggerUSec read the same way. (PASS, the evidence read, the trigger's second.)"""
    if trg and trg.get("unit") is not None:
        t = int(trg.get("realtime_usec") or 0) // 10 ** 6
        return (trg["unit"] == TIMER and t >= mark_s + ACTIVE_S - 2 and t <= s0 <= t + 60), "TRIGGER_UNIT %s" % (
            trg["unit"],), t
    t = last_trigger
    return (t is not None and t >= mark_s + ACTIVE_S - 2 and t <= s0 <= t + 60), "LastTriggerUSec", t


def still_reading(before, now, restarts):
    """G-STILL from two reads and the pair book's archive's restart records between them: PASS where the recorder and
    the reward book are unchanged and the pair book is unchanged or moved by that archive's own restarts alone - a
    chain of records from the recorded MainPID to the current one, NRestarts one higher at each, the unit active.
    Pure: it reads nothing but its arguments."""
    if now == before:
        return True, "unchanged"
    if now["recorder"] != before["recorder"]:
        return False, "the recorder changed"
    if now["rewardbook"] != before["rewardbook"]:
        return False, "the reward book changed"
    b, n = before["pairbook"], now["pairbook"]
    pid, count = b["MainPID"], int(b["NRestarts"])
    for r in restarts:
        if str(r.get("stopped")) != pid or str(r.get("NRestarts")) != str(count + 1):
            return False, "a restart record that does not follow %s at NRestarts %d: %r" % (pid, count, r)
        pid, count = str(r.get("pid")), count + 1
    if restarts and pid == n["MainPID"] and str(count) == n["NRestarts"] and n["ActiveState"] == "active":
        return True, "the pair book moved by its archive's own restarts alone: %d" % len(restarts)
    return False, "the pair book changed, %d restart records of its archive since the first read" % len(restarts)

# ---- what the run touches outside its own files -------------------------------------------------------------


class Env:
    """The clock, systemd, the reward book's store and record, and GitHub, as the unit's run meets them."""

    def __init__(self, work=STATE):
        self.root, self.state, self.work = ROOT, STATE, work
        self.wait_min, self.gap_s = tz27.WAIT_MIN_S, tz27.UPLOAD_GAP_S
        self.api, self.uploads, self.web = tz27.API_BASE, tz27.UPLOAD_BASE, tz27.WEB_BASE
        self.invocation = os.environ.get("INVOCATION_ID")
        self.trigger = {"unit": os.environ.get("TRIGGER_UNIT"),
                        "realtime_usec": os.environ.get("TRIGGER_TIMER_REALTIME_USEC"),
                        "monotonic_usec": os.environ.get("TRIGGER_TIMER_MONOTONIC_USEC")}
        self.commit, self.file_sha = None, None
        self._rt = (None, [])

    def identity(self):
        """The commit the service's files are from, and this file's SHA-256."""
        with open(os.path.join(ASVC, "commit.txt"), encoding="utf-8") as fh:
            self.commit = fh.read().strip()
        assert re.fullmatch(r"[0-9a-f]{40}", self.commit), "commit.txt %r" % self.commit
        self.file_sha = tz27.sha256_file(os.path.abspath(__file__))[0]

    def time(self):
        return time.time()

    def time_ns(self):
        return time.time_ns()

    def sleep(self, s):
        time.sleep(max(0.0, s))

    def disable_timer(self):
        return subprocess.run(["systemctl", "disable", "--now", TIMER]).returncode

    def credential(self):
        return tz27.credential()

    def free(self):
        return tz27.free_bytes()

    def mem(self):
        return tz27.mem_available()

    def archive_active(self):
        return tz27.systemctl_show(PAIR_ARCHIVE, ["ActiveState"]).get("ActiveState") in RUNNING

    def reward_unit(self):
        kv = tz27.systemctl_show(REWARD_UNIT, ["MainPID", "NRestarts", "ActiveState"])
        return {k: kv.get(k) for k in ("MainPID", "NRestarts", "ActiveState")}

    def runtime(self):
        """The reward book's runtime.jsonl, its complete lines, read again only where the file changed; none where it
        does not exist, so that a removal waits for it."""
        path = os.path.join(self.root, "runtime.jsonl")
        try:
            st = os.stat(path)
        except FileNotFoundError:
            return []
        key = (st.st_size, st.st_mtime_ns)
        if self._rt[0] != key:
            with open(path, "rb") as fh:
                raw = fh.read()
            self._rt = (key, [json.loads(ln) for ln in raw.split(b"\n")[:-1] if ln.strip()])
        return self._rt[1]

    def reward_pids(self):
        return tz27.processes_with(REWARD_ARGV)


def safe_unit(env):
    try:
        return env.reward_unit()
    except Exception as exc:
        return {"unread": "%s: %s" % (type(exc).__name__, str(exc)[:120])}

# ---- the run: its phases -------------------------------------------------------------------------------------


class HoldTimeout(Exception):
    pass


class QuietTimeout(Exception):
    pass


def floors(env):
    mem, free = env.mem(), env.free()
    out("MemAvailable %d bytes, floor %d; free %d bytes, floor %d" % (mem, RUN_MEM_FLOOR, free, DISK_FLOOR))
    assert mem >= RUN_MEM_FLOOR, "MemAvailable %d bytes, below %d" % (mem, RUN_MEM_FLOOR)
    assert free >= DISK_FLOOR, "free %d bytes, below %d" % (free, DISK_FLOOR)


def new_set(env, led, a, rdir):
    tz27.MODE[0] = "inventory"
    assets, slots, deferred, open_n, streamless = inventory(env.root, a)
    for e in slots:
        out("SLOT %d %s %-8s stream files %d, %d bytes, taken %d" % (e["S"], tz27.utc(e["S"]), e["disposition"],
                                                                     e["streams"], e["stream_bytes"], e["taken"]))
    counts = {"slots_considered": len(slots), "open": open_n, "streamless": streamless, "deferred": deferred,
              "closed": sum(1 for e in slots if e["disposition"] == "closed"),
              "unclosed": sum(1 for e in slots if e["disposition"] == "unclosed")}
    if not assets:
        led.write(env, dict({"event": "empty", "run": a}, **counts))
        return None
    doc = set_document(TAG_PREFIX + str(a), a, env.root, assets, slots, deferred)
    for x in assets:
        out("S %s %d %s" % (x["asset"], x["bytes"], x["sha256"]))
    raw = tz27.json_bytes(doc)
    with open(os.path.join(rdir, "set.json"), "wb") as fh:
        fh.write(raw)
    led.write(env, dict({"event": "set", "run": a, "tag": doc["tag"], "sha256": tz27.sha256_bytes(raw),
                         "assets_n": doc["assets_n"], "bytes_total": doc["bytes_total"], "first_S": doc["first_S"],
                         "last_S": doc["last_S"]}, **counts))
    return doc


def hold(env, led, a, phase):
    """While the pair book's archive runs, wait; HoldTimeout after HOLD_MAX_S."""
    tz27.MODE[0] = "hold"
    waited = 0
    while env.archive_active():
        if waited >= HOLD_MAX_S:
            raise HoldTimeout("the pair book's archive still runs after %d s before %s" % (waited, phase))
        env.sleep(HOLD_STEP_S)
        waited += HOLD_STEP_S
    if waited:
        led.write(env, {"event": "hold", "run": a, "phase": phase, "waited_s": waited})
        out("held %d s before %s: the pair book's archive ran" % (waited, phase))
    return waited


def upload_phase(env, led, a, rdir, doc):
    tz27.MODE[0] = "upload"
    tok, source = env.credential()
    out("credential: %s" % source)
    gh = tz28.Gh28(env, tok, tz28.transfers_logger(rdir))
    rel = gh.release_by_tag(doc["tag"])
    created = rel is None
    if created:
        rel = gh.create_release(doc["tag"], *release_text(doc, env.commit))
        out("created the Release on %s, id %s" % (doc["tag"], rel.get("id")))
    assert rel.get("tag_name") == doc["tag"] and rel.get("draft") is False, "the Release is not published on the tag"
    path = os.path.join(rdir, "upload.jsonl")

    def log(rec):
        rec = dict(rec, at=tz27.utc(env.time()))
        tz28.jsonl_append(path, rec, "upload.jsonl")
        out("U %s" % json.dumps(rec, sort_keys=True))

    sent, held = tz27.upload_set(gh, rel, doc, env.root, log, wait_min=env.wait_min)
    log({"action": "complete", "assets": sent + held, "sent": sent, "held": held, "release_id": int(rel["id"]),
         "credential": source, "wall_ns": env.time_ns()})
    led.write(env, {"event": "upload", "run": a, "release_id": int(rel["id"]), "created": created, "sent": sent,
                    "held": held, "credential": source})


def removal_wait(env, nbytes, waited):
    """Until a second of the pair book's idle stretch at which a removal of nbytes may start and the reward book is
    quiet; QuietTimeout once QUIET_MAX_S of waiting has passed in the phase."""
    while True:
        now = tz28.idle_wait(env, tz28.budget_s(nbytes))
        why = quiet(env.runtime(), env.reward_pids(), now)
        if why is None:
            return
        if waited[0] >= QUIET_MAX_S:
            raise QuietTimeout("the removals waited %d s: %s" % (waited[0], why))
        if waited[0] % 60 == 0:
            out("removal waits: %s" % why)
        env.sleep(QUIET_STEP_S)
        waited[0] += QUIET_STEP_S


def remove_set(env, doc, done, log, waited):
    """Each file of the set, in order - its slot closed and due, its bytes hashed again equal to the set's - removed
    inside the idle stretch while the reward book is quiet, read again after the hash and right before the unlink,
    logged at once, and its day directory's other entries left as they were. A file already absent counts only where
    the run's own log records its removal."""
    rows, removed, freed, already = [], 0, 0, 0
    for x in doc["assets"]:
        p = os.path.join(env.root, str(x["T"]), x["file"])
        names = tz27.window_names(env.root, x["T"])
        assert slot_files(names, x["T"]).get(x["S"], {}).get("closed") and \
            x["S"] + SLOT_JSON_AT + SETTLE_S <= env.time(), "slot %d is not closed" % x["S"]
        if x["file"] not in names:
            assert x["asset"] in done, "%s is absent and no removal of it is recorded" % p
            already += 1
            continue
        while True:
            removal_wait(env, x["bytes"], waited)
            t0 = env.time_ns()
            h, n = tz27.sha256_file(p)
            assert (h, n) == (x["sha256"], x["bytes"]), "%s is %d bytes, SHA-256 %s: not the set's" % (p, n, h)
            if quiet(env.runtime(), env.reward_pids(), env.time()) is None:
                break
        ap = os.path.abspath(p)
        tz27.ALLOWED_REMOVE.add(ap)
        try:
            os.remove(p)
        finally:
            tz27.ALLOWED_REMOVE.discard(ap)
        tz27.bump("removed")
        assert not os.path.lexists(p), "%s is still there" % p
        lost = sorted(set(names) - set(tz27.window_names(env.root, x["T"])) - {x["file"]})
        assert not lost, "day %d lost more than %s: %r" % (x["T"], x["file"], lost[:5])
        removed += 1
        freed += n
        row = {"asset": x["asset"], "T": x["T"], "S": x["S"], "k": x["k"], "file": x["file"], "bytes": n, "sha256": h,
               "start_ns": t0, "removed_wall_ns": env.time_ns()}
        tz27.assert_keys(row, DELETE_ROW_KEYS, "delete.jsonl row")
        log(row)
        rows.append(row)
    return rows, removed, freed, already


def delete_phase(env, led, a, rdir, doc, vsha):
    tz27.MODE[0] = "delete"
    with open(os.path.join(rdir, "verify.json"), "rb") as fh:
        assert tz27.sha256_bytes(fh.read()) == vsha, "delete: verify.json is not this run's"
    path = os.path.join(rdir, "delete.jsonl")

    def log(row):
        tz28.jsonl_append(path, row, "delete.jsonl")
        out("X %s %d %s removed at second %d" % (row["asset"], row["bytes"], row["sha256"],
                                                tz28.phase_of(row["removed_wall_ns"] // 10 ** 9)))

    done = {r["asset"] for r in tz28.jsonl_read(path)}
    free_before = env.free()
    waited = [0]
    _rows, removed, freed, already = remove_set(env, doc, done, log, waited)
    checks, gone, kept = removed_reading(env.root, doc, {r["asset"] for r in tz28.jsonl_read(path)})
    for k, v in checks.items():
        out("G-DELETE %-36s %s" % (k, v))
    assert all(checks.values()), "REMOVED FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    led.write(env, {"event": "delete", "run": a, "removed": removed, "already": already, "freed": freed, "gone": gone,
                    "slots_kept": kept, "free_before": free_before, "free_after": env.free(), "quiet_s": waited[0]})


def final_phase(env, led, a, rdir, doc, reward0):
    tz27.MODE[0] = "final"
    trs = tz28.jsonl_read(os.path.join(rdir, "transfers.jsonl"))
    rms = tz28.jsonl_read(os.path.join(rdir, "delete.jsonl"))
    acts = [tz28.transfer_ok(t) for t in trs] + [tz28.transfer_ok(removal_span(r)) for r in rms]
    counter, free = stream_bytes_view(env.root), env.free()
    rate, rows = projection(doc["bytes_total"], doc["first_S"], doc["last_S"], counter, free, int(env.time()))
    for what, d, when in rows:
        out("at the set's rate %s stops the streams in %s days, at %s" % (what, tz27.decimals(d, 2), tz27.utc(when)))
    held = sum(r.get("waited_s", 0) for r in tz28.events(led.recs, a, "hold"))
    led.write(env, {"event": "complete", "run": a, "assets_n": doc["assets_n"], "bytes_total": doc["bytes_total"],
                    "requests": len(trs), "removals": len(rms), "started_outside": sum(1 for s, _e in acts if not s),
                    "ended_outside": sum(1 for _s, e in acts if not e), "store_stream_bytes": counter,
                    "free_bytes": free, "rate_per_day": int(rate), "stops": [[w, int(t)] for w, _d, t in rows],
                    "held_s": held, "rewardbook_at_start": reward0, "rewardbook_at_end": safe_unit(env),
                    "peak_rss": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024})


def run(env):
    """One run: the pending set resumed, or a new one as of now; exit 0, EXIT_DEFERRED or 1."""
    tz27.WORK[0], tz27.MODE[0] = env.work, "run"
    led = tz28.Ledger(env.state)
    if tz28.halted(led.recs):
        last = [r for r in led.recs if r.get("event") == "halt"][-1]
        out("HALTED since run %s, %s: %s; nothing done" % (last.get("run"), last.get("phase"), last.get("reason")))
        tz27.MODE[0] = "final"
        rc = env.disable_timer()
        led.write(env, {"event": "refused", "run": last.get("run"), "exit": rc})
        return 1
    a = tz28.pending(led.recs)
    resumed = a is not None
    if not resumed:
        a = max([int(env.time())] + [r["run"] + 1 for r in led.recs if r.get("event") == "start"])
    rdir = os.path.join(env.state, "runs", str(a))
    os.makedirs(rdir, exist_ok=True)
    reward0 = safe_unit(env)
    led.write(env, {"event": "start", "run": a, "resumed": resumed, "commit": env.commit, "file_sha256": env.file_sha,
                    "tz28_sha256": TZ28_SHA256, "tz27_sha256": TZ27_SHA256, "invocation": env.invocation,
                    "trigger": env.trigger, "phase_at": tz28.phase_of(env.time()), "rewardbook": reward0})
    phase = "set"
    try:
        floors(env)
        doc = tz28.load_set(led, a, rdir)
        if doc is None:
            doc = new_set(env, led, a, rdir)
            if doc is None:
                out("EMPTY: no stream file of a closed slot as of %d" % a)
                return 0
        if not tz28.events(led.recs, a, "delete"):
            phase = "upload"
            hold(env, led, a, phase)
            upload_phase(env, led, a, rdir, doc)
            phase = "verify"
            hold(env, led, a, phase)
            vsha = tz28.verify_phase(env, led, a, rdir, doc)
            phase = "delete"
            delete_phase(env, led, a, rdir, doc, vsha)
        phase = "final"
        final_phase(env, led, a, rdir, doc, reward0)
        out("COMPLETE: run %d, %d files, %d bytes, Release %s" % (a, doc["assets_n"], doc["bytes_total"], doc["tag"]))
        return 0
    except tz27.GuardError as exc:
        return tz28.halt(env, led, a, phase, "GuardError: %s" % exc)
    except Exception as exc:
        reason = "%s: %s" % (type(exc).__name__, str(exc))
        if phase not in PRE_DELETE and not isinstance(exc, QuietTimeout):
            return tz28.halt(env, led, a, phase, reason)
        n = len(tz28.events(led.recs, a, "deferred")) + 1
        if n >= tz28.DEFER_LIMIT:
            return tz28.halt(env, led, a, phase, "deferral %d of %d: %s" % (n, tz28.DEFER_LIMIT, reason))
        led.write(env, {"event": "deferred", "run": a, "phase": phase, "reason": reason[:400], "count": n})
        out("DEFERRED in %s, %d of %d: %s; the next run resumes this set" % (phase, n, tz28.DEFER_LIMIT, reason[:400]))
        return tz28.EXIT_DEFERRED


def mode_run():
    cwd = os.getcwd()
    assert cwd == STATE, "run: from %s, not %s" % (cwd, STATE)
    assert os.path.abspath(__file__) == ASVC + "/" + SELF_NAME, "run: this file is not the service's copy"
    assert os.environ.get("INVOCATION_ID"), "run: only %s runs this mode" % ARCHIVE
    env = Env()
    env.identity()
    tz27.WORK[0], tz27.MODE[0] = STATE, "run"
    lock = open(os.path.join(STATE, "run.lock"), "ab")
    try:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        out("NOT STARTED: another run holds %s/run.lock" % STATE)
        return tz28.EXIT_NOT_STARTED
    out("run: pid %d, commit %s, file sha256 %s, invocation %s" % (os.getpid(), env.commit, env.file_sha,
                                                                   env.invocation))
    return run(env)

# ---- the deployment's readings: the session's modes ---------------------------------------------------------


def mode_fingerprint():
    primary = tz27.PRIMARY
    with open(os.path.join(primary, "SYSTEM-MAP.md"), "rb") as fh:
        raw = fh.read()
    txt = raw.decode("utf-8")
    rev = re.findall(r"^\*\*Revision string:\*\* `([^`]+)`$", txt, re.M)
    assert rev == [MAP_REVISION], "map revision %r, required %s" % (rev, MAP_REVISION)
    found = dict(tz27.ANCHOR_ROW.findall(txt))
    assert found == tz27.ANCHORS, "anchors %r" % found
    for k, rel in sorted(tz27.ANCHOR_FILES.items()):
        h = tz27.sha256_file(os.path.join(primary, rel))[0][:12]
        assert h == tz27.ANCHORS[k], "re-derived %s %s, the map %s" % (k, h, tz27.ANCHORS[k])
        out("re-derived %s %s sha256[:12] %s equal" % (k, rel, h))
    rows = tz27.ROW.findall(txt)
    states = {k: sum(1 for r in rows if r[3] == k) for k in MAP_ROWS}
    assert states == MAP_ROWS and len(rows) == sum(MAP_ROWS.values()), "rows %r" % states
    for path, lines, nbytes, state, sha in rows:
        with open(os.path.join(primary, path), "rb") as fh:
            blob = fh.read()
        got = (blob.count(b"\n"), len(blob), tz27.sha256_bytes(blob))
        if state == "frozen":
            want = (int(lines.replace(",", "")), int(nbytes.replace(",", "")), sha)
            assert got == want, "frozen row %s: %r, the map %r" % (path, got, want)
        out("%-44s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), tz27.sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"],
                         states["reported"]))


def units_now():
    now = {}
    for key, unit in sorted(UNITS.items()):
        kv = tz27.systemctl_show(unit, ["MainPID", "NRestarts", "ActiveState", "MemoryCurrent", "MemoryPeak"])
        now[key] = {k: kv.get(k) for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, MemoryCurrent %s, MemoryPeak %s" % (unit, now[key], kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    for unit in (PAIR_TIMER, PAIR_ARCHIVE, TIMER, ARCHIVE):
        try:
            kv = tz27.systemctl_show(unit, ["ActiveState", "SubState", "UnitFileState", "Result"])
        except AssertionError as exc:
            kv = {"unread": str(exc)[:120]}
        out("%s %s" % (unit, kv))
    return now


def pair_restarts(since_ns):
    """The pair book's archive's restart records since an instant, in order, from its own ledger."""
    with open(PAIR_LEDGER, "rb") as fh:
        raw = fh.read()
    recs = [json.loads(ln) for ln in raw.split(b"\n")[:-1] if ln.strip()]
    return [r for r in recs if r.get("event") == "restart" and r.get("wall_ns", 0) >= since_ns]


def mode_still():
    """G-STILL: the first run records the three capture units; a later run compares. A FAIL runs no block."""
    st = tz27.load_state()
    now = units_now()
    if "still34" not in st:
        st["still34"] = {"at": tz27.utc(time.time()), "at_ns": time.time_ns(), "units": now}
        tz27.save_state(st)
        out("still: recorded")
        return True
    restarts = pair_restarts(st["still34"]["at_ns"])
    for r in restarts:
        out("the pair book's archive's restart record %s: run %s, window %s, pid %s after %s, NRestarts %s" % (
            tz27.utc(r["wall_ns"] / 1e9), r.get("run"), r.get("W"), r.get("pid"), r.get("stopped"), r.get("NRestarts")))
    ok, why = still_reading(st["still34"]["units"], now, restarts)
    out("G-STILL %s: %s since %s" % ("PASS" if ok else "FAIL", why, st["still34"]["at"]))
    return ok


def git_out(*args):
    cp = subprocess.run(["git"] + list(args), capture_output=True, text=True)
    assert cp.returncode == 0, "git %s: exit %d" % (" ".join(args), cp.returncode)
    return cp.stdout.strip()


def mode_installed():
    """G-INSTALL: what B-INSTALL put on the host, against the branch's worktree."""
    wt = tz27.wpath("wt")
    head, up = git_out("-C", wt, "rev-parse", "HEAD"), git_out("-C", wt, "rev-parse", "@{u}")
    with open(os.path.join(ASVC, "commit.txt"), encoding="utf-8") as fh:
        commit = fh.read().strip()
    files = {}
    for name in (SELF_NAME, TZ28_NAME, TZ27_NAME):
        files[name] = (tz27.sha256_file(os.path.join(ASVC, name))[0],
                       tz27.sha256_file(os.path.join(wt, "research", name))[0])
    units = {}
    for name in (ARCHIVE, TIMER):
        with open(os.path.join(UNIT_DIR, name), "rb") as a_:
            installed = a_.read()
        with open(os.path.join(wt, "deploy", "systemd", name), "rb") as b_:
            units[name] = installed == b_.read()
    st = os.stat(STATE)
    svc = tz28.show_utc(ARCHIVE, ["LoadState", "ActiveState", "UnitFileState", "FragmentPath", "Type", "Restart",
                                  "MemoryMax", "TimeoutStartUSec", "WorkingDirectory", "ExecStart", "Nice"])
    tmr = tz28.show_utc(TIMER, ["LoadState", "ActiveState", "UnitFileState", "FragmentPath"])
    argv = "argv[]=%s ;" % " ".join(RUN_ARGV)
    checks = {"commit.txt the branch head, pushed": commit == head == up,
              "the service's copy of this file the branch's": files[SELF_NAME][0] == files[SELF_NAME][1],
              "the service's copy of TZ-28's file, %s" % TZ28_SHA256[:12]: files[TZ28_NAME][0] == files[TZ28_NAME][1]
              == TZ28_SHA256,
              "the service's copy of TZ-27's file, %s" % TZ27_SHA256[:12]: files[TZ27_NAME][0] == files[TZ27_NAME][1]
              == TZ27_SHA256,
              "the two units byte for byte": all(units.values()),
              "the state directory, root's, 0700, empty": os.path.isdir(STATE) and st.st_uid == 0
              and (st.st_mode & 0o777) == 0o700 and not os.listdir(STATE),
              "the service loaded, inactive, static": (svc["LoadState"], svc["ActiveState"], svc["UnitFileState"])
              == ("loaded", "inactive", "static"),
              "the service a oneshot, Restart=no, Nice=19, 128M, 6h, its argv and directory": svc["Type"] == "oneshot"
              and svc["Restart"] == "no" and svc["Nice"] == "19" and svc["MemoryMax"] == str(ARCHIVE_MEMORY_MAX)
              and svc["TimeoutStartUSec"] == "6h" and svc["WorkingDirectory"] == STATE and argv in svc["ExecStart"]
              and svc["FragmentPath"] == UNIT_DIR + "/" + ARCHIVE,
              "the timer loaded, inactive, disabled": (tmr["LoadState"], tmr["ActiveState"], tmr["UnitFileState"],
                                                       tmr["FragmentPath"]) == ("loaded", "inactive", "disabled",
                                                                                UNIT_DIR + "/" + TIMER)}
    for name, (a_, b_) in sorted(files.items()):
        out("%s/%s sha256 %s; the branch's %s" % (ASVC, name, a_, b_))
    out("commit.txt %s; the branch head %s, its upstream %s" % (commit, head, up))
    for k, v in checks.items():
        out("G-INSTALL %-76s %s" % (k, v))
    assert all(checks.values()), "G-INSTALL FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    out("G-INSTALL PASS: %d of %d" % (len(checks), len(checks)))


def mode_mark(name):
    assert name in ("enable", "retry", "stop"), "mark %r" % name
    st = tz27.load_state()
    marks = st.setdefault("marks34", {})
    assert name not in marks, "mark %s already taken" % name
    tmr = tz28.show_utc(TIMER, ["ActiveState", "UnitFileState"])
    svc = tz28.show_utc(ARCHIVE, ["ActiveState", "Result"])
    marks[name] = {"ns": time.time_ns(), "timer": tmr, "service": svc}
    tz27.save_state(st)
    out("mark %s at %s, second %d of its window: the timer %r, the service %r" % (
        name, tz27.utc(marks[name]["ns"] / 1e9), tz28.phase_of(marks[name]["ns"] // 10 ** 9), tmr, svc))


def next_calendar(now):
    """The first instant after now at 01:30:20 UTC."""
    d = int(now) // 86400 * 86400 + CALENDAR_S
    return d if d > now else d + 86400


def timer_reading(now):
    kv = tz28.show_utc(TIMER, ["LoadState", "ActiveState", "SubState", "UnitFileState", "FragmentPath", "Unit",
                               "TimersCalendar", "TimersMonotonic", "NextElapseUSecRealtime", "AccuracyUSec",
                               "LastTriggerUSec", "ActiveEnterTimestamp"])
    nxt = tz28.stamp_of(kv.get("NextElapseUSecRealtime"))
    checks = {"loaded": kv["LoadState"] == "loaded",
              "active": kv["ActiveState"] == "active" and kv["SubState"] in ("waiting", "running"),
              "enabled": kv["UnitFileState"] == "enabled",
              "fragment": kv["FragmentPath"] == UNIT_DIR + "/" + TIMER,
              "its unit": kv["Unit"] == ARCHIVE,
              "the calendar": ("OnCalendar=%s ;" % CALENDAR) in kv["TimersCalendar"],
              "1,800 s after it starts": "OnActiveUSec=30min" in kv["TimersMonotonic"],
              "accuracy 1 s": kv["AccuracyUSec"] == "1s",
              "the next calendar elapse": nxt == next_calendar(now)}
    return kv, checks, nxt


def mode_timer():
    now = time.time()
    kv, checks, nxt = timer_reading(now)
    out("the timer: %r" % kv)
    for k, v in checks.items():
        out("G-TIMER %-24s %s" % (k, v))
    assert all(checks.values()), "G-TIMER FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    out("G-TIMER PASS: the next calendar run at %s, the run after the start at %s" % (
        tz27.utc(nxt), tz27.utc((tz28.stamp_of(kv.get("ActiveEnterTimestamp")) or 0) + ACTIVE_S)))


def read_slot(root, s):
    """Every slot.json of slot s: [(k, doc)]."""
    found = []
    for k, n in slot_names(root, s):
        with open(os.path.join(root, str(day_of(s)), n), "rb") as fh:
            found.append((k, json.loads(fh.read())))
    return found


def read_runtime(root):
    with open(os.path.join(root, "runtime.jsonl"), "rb") as fh:
        raw = fh.read()
    return [json.loads(ln) for ln in raw.split(b"\n")[:-1] if ln.strip()]


def slot_line(s, sjs):
    parts = []
    for k, sj in sjs:
        st = sj.get("stream") if isinstance(sj.get("stream"), dict) else {}
        parts.append("index %d pid %s joined_late %s stopped %s opened %s off %s segments %s frames %s max_gap_ns %s "
                     "stored_bytes %s error %s" % (k, sj.get("pid"), sj.get("joined_late"), sj.get("stopped"),
                                                   st.get("opened"), st.get("off_reason"), st.get("segments"),
                                                   st.get("frames"), st.get("max_gap_ns"), st.get("stored_bytes"),
                                                   sj.get("error")))
    return "slot %d %s: %s" % (s, tz27.utc(s), "; ".join(parts) if parts else "no slot.json")


def store_left(root, doc):
    """After the run, the store against the set: every stream file left of a slot due by A; of those the files of a
    slot the set records closed, which only its deferral may leave, and the files of a slot it does not record, which
    nothing may leave; and the set's slots whose slot.json is no longer as the set recorded it."""
    a = doc["as_of"]
    disp = {e["S"]: e["disposition"] for e in doc["slots"]}
    left, closed_left, unknown, seen = [], [], [], {}
    for d0 in day_dirs(root):
        for s, e in sorted(slot_files(tz27.window_names(root, d0), d0).items()):
            seen[s] = "closed" if e["closed"] else "unclosed"
            if s + SLOT_JSON_AT + SETTLE_S > a:
                continue
            for _k, n in sorted(e["streams"]):
                left.append(n)
                if s not in disp:
                    unknown.append(n)
                elif disp[s] == "closed":
                    closed_left.append(n)
    flipped = sorted(s for s, d in disp.items() if seen.get(s) != d)
    return left, closed_left, unknown, flipped


def set_reading(doc, raw, sets, closed_left, unknown, flipped):
    """G-SET, pure: one set record, set.json its SHA-256, the document this TZ's rule rebuilds from it equal to it, its
    deferral the closed slots' files not taken, at most that many files of closed slots left, none of a slot it does
    not record, and every slot's slot.json as recorded."""
    rebuilt = set_document(doc["tag"], doc["as_of"], doc["root"], doc["assets"], doc["slots"], doc["deferred"])
    owed = sum(e["streams"] - e["taken"] for e in doc["slots"] if e["disposition"] == "closed")
    taken = sum(e["taken"] for e in doc["slots"])
    return (len(sets) == 1 and tz27.sha256_bytes(raw) == sets[0]["sha256"] and rebuilt == doc
            and owed == doc["deferred"] and taken == doc["assets_n"] and len(closed_left) <= doc["deferred"]
            and not unknown and not flipped)


def mode_first():
    """The first run after the enable mark, re-read from its records, the store, the reward book's record, systemd and
    the Release: exit 3 while it has not ended or G-NEXT's slots are not yet due."""
    tz27.MODE[0] = "final"
    st = tz27.load_state()
    mark = st.get("marks34", {}).get("enable")
    assert mark is not None, "first: no enable mark"
    svc = tz28.show_utc(ARCHIVE, ["ActiveState", "Result", "ExecMainStatus", "ExecMainStartTimestamp",
                                  "ExecMainExitTimestamp", "InvocationID"])
    recs = tz28.Ledger(STATE).recs
    a, mine = tz28.first_run(recs, mark["ns"])
    if a is None or svc["ActiveState"] in RUNNING:
        out("NOT YET: %s; the service %s" % ("no run since the mark" if a is None else "run %d" % a,
                                              svc["ActiveState"]))
        return 3
    terms = [r["event"] for r in mine if r["event"] in tz28.TERMINAL]
    rdir = os.path.join(STATE, "runs", str(a))
    drecs = tz28.jsonl_read(os.path.join(rdir, "delete.jsonl"))
    slots = next_slots(drecs[0]["start_ns"], drecs[-1]["removed_wall_ns"]) if drecs else []
    if terms and terms[-1] == "complete" and slots and time.time() < slots[-1] + SLOT_JSON_AT + NEXT_SETTLE_S:
        out("NOT YET: run %d complete; G-NEXT's last slot %d is due at %s" % (
            a, slots[-1], tz27.utc(slots[-1] + SLOT_JSON_AT + NEXT_SETTLE_S)))
        return 3
    for r in mine:
        out("R %s" % json.dumps(r, sort_keys=True))
    out("run %d: %d records, %s" % (a, len(mine), [r["event"] for r in mine]))
    if not terms:
        last = mine[-1]["event"]
        out("READING G-RUN: %s - the run's last record %s, in its phase %r" % (
            "DEFERRED" if last == "deferred" else "INTERRUPTED", last, mine[-1].get("phase")))
        return 1
    last = terms[-1]
    readings = {}
    tmr = tz28.show_utc(TIMER, ["LastTriggerUSec", "ActiveEnterTimestamp"])
    last_trig, enter = tz28.stamp_of(tmr.get("LastTriggerUSec")), tz28.stamp_of(tmr.get("ActiveEnterTimestamp"))
    s0 = mine[0]["wall_ns"] // 10 ** 9
    readings["G-TRIGGER"], source, trig = trigger_reading(mine[0].get("trigger"), mark["ns"] // 10 ** 9, s0, last_trig)
    out("G-TRIGGER, by %s: the enable mark %s, the timer started %s, the run's trigger %s - %s s after the mark plus "
        "%d - the run's first record %s; the timer's last trigger %s" % (
            source, tz27.utc(mark["ns"] / 1e9), tz27.utc(enter or 0), tz27.utc(trig or 0),
            None if trig is None else trig - mark["ns"] // 10 ** 9 - ACTIVE_S, ACTIVE_S, tz27.utc(s0),
            tz27.utc(last_trig or 0)))
    readings["G-RUN"] = last == "complete" and svc["Result"] == "success" and svc["ExecMainStatus"] == "0"
    out("G-RUN: the run %s; the service's last invocation %s, Result %s, ExecMainStatus %s, %s to %s" % (
        last, svc["InvocationID"], svc["Result"], svc["ExecMainStatus"], svc["ExecMainStartTimestamp"],
        svc["ExecMainExitTimestamp"]))
    if last == "complete":
        with open(os.path.join(rdir, "set.json"), "rb") as fh:
            raw = fh.read()
        sets = [r for r in mine if r["event"] == "set"]
        doc = json.loads(raw)
        left, closed_left, unknown, flipped = store_left(ROOT, doc)
        for e in doc["slots"]:
            out("SLOT %d %s %-8s stream files %d, %d bytes, taken %d" % (e["S"], tz27.utc(e["S"]), e["disposition"],
                                                                         e["streams"], e["stream_bytes"], e["taken"]))
        for x in doc["assets"]:
            out("S %s %d %s" % (x["asset"], x["bytes"], x["sha256"]))
        readings["G-SET"] = set_reading(doc, raw, sets, closed_left, unknown, flipped)
        out("G-SET: %d files, %d bytes, slots %d to %d, as of %d, deferred %d; set.json sha256 %s; the store after "
            "the run holds %d stream files of slots due by A - %d of slots the set records closed, %d of slots it "
            "does not record; slots whose slot.json is not as recorded %r" % (
                doc["assets_n"], doc["bytes_total"], doc["first_S"], doc["last_S"], doc["as_of"], doc["deferred"],
                tz27.sha256_bytes(raw), len(left), len(closed_left), len(unknown), flipped))
        rel, rows, missing, extra = tz27.verify_release(tz27.GitHub(), doc["tag"], doc, download=False)
        up = tz27.release_reading(rel, doc["tag"], rows, missing, extra)
        obj, peeled = tz27.ls_remote_tag(doc["tag"])
        readings["G-UPLOAD"] = all(v for k, v in up.items() if not k.startswith("every download")) and \
            obj == mine[0]["commit"] and peeled is None
        out("G-UPLOAD: Release %s, %d of %d assets by name, bytes, state and digest, %d missing, %d beyond; the tag "
            "%s at %s" % (None if rel is None else rel.get("id"), sum(r["api_ok"] for r in rows), doc["assets_n"],
                          len(missing), len(extra), doc["tag"], obj))
        vrec = [r for r in mine if r["event"] == "verify"][-1]
        with open(os.path.join(rdir, "verify.json"), "rb") as fh:
            vraw = fh.read()
        vdoc = json.loads(vraw)
        readings["G-DOWNLOAD"] = tz27.sha256_bytes(vraw) == vrec["verify_sha256"] and vdoc["assets_n"] == \
            doc["assets_n"] and all(r["download_ok"] and r["download_sha256"] == r["sha256"] for r in vdoc["assets"])
        out("G-DOWNLOAD: verify.json sha256 %s, %d of %d downloads equal, %d bytes" % (
            tz27.sha256_bytes(vraw), sum(r["download_ok"] for r in vdoc["assets"]), doc["assets_n"],
            vdoc["bytes_total"]))
        done = {r["asset"] for r in drecs}
        aby, vby, dby = {r["asset"]: r for r in rows}, {r["asset"]: r for r in vdoc["assets"]}, \
            {r["asset"]: r for r in drecs}
        for x in doc["assets"]:
            out("ROW %s %d %s digest %s download %s removed %s" % (
                x["asset"], x["bytes"], x["sha256"], aby.get(x["asset"], {}).get("digest"),
                vby.get(x["asset"], {}).get("download_sha256"), dby.get(x["asset"], {}).get("sha256")))
        dchecks, gone, kept = removed_reading(ROOT, doc, done)
        readings["G-DELETE"] = all(dchecks.values())
        out("G-DELETE: %r; %d gone, %d removals recorded, %d slots keep their slot.json" % (dchecks, gone, len(done),
                                                                                         kept))
        trs = tz28.jsonl_read(os.path.join(rdir, "transfers.jsonl"))
        for t in trs:
            s, e = tz28.transfer_ok(t)
            out("T %s %s: %d bytes, budget %d s, second %d, %.1f s, inside %s %s" % (
                t["kind"], t["name"], t["bytes"], t["budget_s"], tz28.phase_of(t["start_ns"] // 10 ** 9),
                (t["end_ns"] - t["start_ns"]) / 1e9, s, e))
        for r in drecs:
            s, e = tz28.transfer_ok(removal_span(r))
            out("X %s: %d bytes, second %d, %.3f s, inside %s %s" % (
                r["asset"], r["bytes"], tz28.phase_of(r["start_ns"] // 10 ** 9),
                (r["removed_wall_ns"] - r["start_ns"]) / 1e9, s, e))
        acts = [tz28.transfer_ok(t) for t in trs] + [tz28.transfer_ok(removal_span(r)) for r in drecs]
        readings["G-IDLE"] = bool(trs) and bool(drecs) and all(s and e for s, e in acts)
        out("G-IDLE: %d requests and %d removals, %d started outside, %d ended outside" % (
            len(trs), len(drecs), sum(1 for s, _e in acts if not s), sum(1 for _s, e in acts if not e)))
        rt = read_runtime(ROOT)
        pid0 = (mine[0].get("rewardbook") or {}).get("MainPID")
        verdicts = []
        for s in slots:
            errs = [r for r in rt if r.get("event") == "error" and r.get("what") == "slot %d" % s]
            v, why = next_verdict(read_slot(ROOT, s), errs, pid0)
            verdicts.append((v, why))
            out("G-NEXT slot %d %s, decided at %s: %s - %s" % (s, tz27.utc(s), tz27.utc(s - DECIDE_S), v, why))
        reading = next_reading(verdicts)
        readings["G-NEXT"] = reading != "FAIL"
        out("READING G-NEXT: %s over %d slots, the reward book's process at the run's start %s" % (
            reading, len(slots), pid0))
        span = (mine[0]["wall_ns"] // 10 ** 9, mine[-1]["wall_ns"] // 10 ** 9)
        s = (span[0] + OPEN_BEFORE) // SLOT * SLOT
        while s - OPEN_BEFORE <= span[1]:
            out("ACROSS %s" % slot_line(s, read_slot(ROOT, s)))
            s += SLOT
        for r in mine:
            if r["event"] == "hold":
                out("HOLD %d s before %s" % (r["waited_s"], r["phase"]))
        out("the run's own record: %s" % json.dumps(mine[-1], sort_keys=True))
    for k, v in readings.items():
        out("READING %-11s %s" % (k, "PASS" if v else "FAIL"))
    bad = sorted(k for k, v in readings.items() if not v)
    assert not bad, "FIRST FAIL: %r" % bad
    out("FIRST PASS: %d of %d" % (len(readings), len(readings)))
    return 0


def mode_final():
    tz27.MODE[0] = "final"
    now = time.time()
    kv, checks, nxt = timer_reading(now)
    for k, v in checks.items():
        out("G-TIMER %-24s %s" % (k, v))
    assert all(checks.values()), "G-TIMER FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    tz27.MODE[0] = "still"
    still = mode_still()
    tz27.MODE[0] = "final"
    recs = tz28.Ledger(STATE).recs
    counter, free = stream_bytes_view(ROOT), tz27.free_bytes()
    days = day_dirs(ROOT)
    out("the store: %d day directories, %d to %d; its stream files %d bytes; free %d bytes" % (
        len(days), days[0] if days else 0, days[-1] if days else 0, counter, free))
    done = [r for r in recs if r.get("event") == "complete"]
    if done:
        sets = [r for r in recs if r.get("event") == "set" and r["run"] == done[-1]["run"]][-1]
        rate, rows = projection(sets["bytes_total"], sets["first_S"], sets["last_S"], counter, free, int(now))
        out("the last set's rate: %s bytes a day" % tz27.decimals(rate, 0))
        for what, d, when in rows:
            out("at that rate %s stops the streams in %s days, at %s" % (what, tz27.decimals(d, 2), tz27.utc(when)))
    out("the next run at %s; the ledger %d records" % (tz27.utc(nxt), len(recs)))
    assert still, "FINAL: G-STILL FAIL"
    out("FINAL PASS")


def mode_stopped():
    """After K-34: the timer disabled and inactive, no run in progress; the ledger's last records."""
    tmr = tz28.show_utc(TIMER, ["ActiveState", "UnitFileState"])
    svc = tz28.show_utc(ARCHIVE, ["ActiveState", "Result"])
    recs = tz28.Ledger(STATE).recs if os.path.exists(os.path.join(STATE, "ledger.jsonl")) else []
    for r in recs[-3:]:
        out("L %s" % json.dumps(r, sort_keys=True))
    checks = {"the timer disabled and inactive": (tmr["UnitFileState"], tmr["ActiveState"]) == ("disabled", "inactive"),
              "no run in progress": svc["ActiveState"] in ("inactive", "failed")}
    for k, v in checks.items():
        out("STOPPED %-34s %s" % (k, v))
    assert all(checks.values()), "STOPPED FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    out("STOPPED PASS: the timer %r, the service %r" % (tmr, svc))

# ---- the self-test: literals, temporary stores, a simulated reward book and a loopback server only ----------------


class FakeEnv(Env):
    """The run's world in a temporary directory: a clock that moves only when the run sleeps, a reward book's record
    the test writes, the pair book's archive running where told, and GitHub on 127.0.0.1."""

    def __init__(self, work, root, state, base, t0, token):
        self.root, self.state, self.work = root, state, work
        self.wait_min, self.gap_s = 0, 0.0
        self.api = self.uploads = self.web = base
        self.invocation, self.commit, self.file_sha = "selftest", "c" * 40, "f" * 64
        self.trigger = {"unit": None, "realtime_usec": None, "monotonic_usec": None}
        self.clock, self.token, self.cred_ok = float(t0), token, True
        self.disabled, self.busy_until, self.on_sleep = 0, None, None
        self.recs, self.pids, self.pids_fn = [], [3137952], None

    def time(self):
        return self.clock

    def time_ns(self):
        return int(round(self.clock * 1e9))

    def sleep(self, s):
        self.clock += max(0.0, s)
        if self.on_sleep is not None:
            self.on_sleep(self)

    def disable_timer(self):
        self.disabled += 1
        return 0

    def credential(self):
        if not self.cred_ok:
            raise AssertionError("UPLOAD REFUSED: no credential (selftest)")
        return self.token, "the selftest's"

    def free(self):
        return 9600000000

    def mem(self):
        return 300000000

    def archive_active(self):
        return self.busy_until is not None and self.clock < self.busy_until

    def reward_unit(self):
        return {"MainPID": str(self.pids[0]) if self.pids else "0", "NRestarts": "1", "ActiveState": "active"}

    def runtime(self):
        return list(self.recs)

    def reward_pids(self):
        return self.pids_fn(self) if self.pids_fn is not None else list(self.pids)


def tz33_text():
    path = os.path.join(HERE, TZ33_NAME)
    with open(path, "rb") as fh:
        raw = fh.read()
    assert hashlib.sha256(raw).hexdigest() == TZ33_SHA256, "%s is not the reward book's frozen file" % path
    return raw.decode("utf-8")


def tz33_values(tree, names):
    """The module-level assignments of names in TZ-33's text, executed in file order: their values."""
    ns = {"re": re, "os": os}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                and node.targets[0].id in names:
            exec(compile(ast.Module(body=[node], type_ignores=[]), TZ33_NAME, "exec"), ns)
    return {k: (ns[k].pattern if isinstance(ns[k], re.Pattern) else ns[k]) for k in names if k in ns}


def tz33_function(tree, name):
    """One of TZ-33's functions, executed from its own text beside the regexes it reads."""
    ns = {"re": re, "os": os}
    ns.update({k: re.compile(v) for k, v in tz33_values(tree, ("DAY_RE", "SLOT_FILE_RE")).items()})
    node = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name][0]
    exec(compile(ast.Module(body=[node], type_ignores=[]), TZ33_NAME, "exec"), ns)
    return ns[name]


def mode_selftest():
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    sep = ":" + "//"
    D0 = 1793145600                      # 2026-10-28 00:00:00 UTC
    D1 = D0 + DAY
    # the calendar, the names and the clock, against integers computed outside this file
    ok(next_calendar(D0) == D0 + 5420 and next_calendar(D0 + 5419) == D0 + 5420 and next_calendar(D0 + 5420)
       == D1 + 5420 and CALENDAR_S == 5420, "the calendar: 01:30:20 UTC, the next after now")
    ok(TAG_RE.fullmatch("rewardbook-streams-1793235620") is not None
       and tz27.TAG_RE.fullmatch("rewardbook-streams-1793235620") is None
       and tz28.TAG_RE.fullmatch("rewardbook-streams-1793235620") is None
       and TAG_RE.fullmatch("pairbook-streams-1793235620") is None, "this TZ's tags, which TZ-27's and TZ-28's rules "
       "do not cover, and theirs, which this TZ's does not")
    ok(ASSET_RE.fullmatch("1793145600-1793187900.0.stream.jsonl.gz") is not None
       and ASSET_RE.fullmatch("1793145600-1793187900.12.stream.jsonl.gz") is not None
       and ASSET_RE.fullmatch("1793145600-1793187900.0.rewards.jsonl.gz") is None
       and ASSET_RE.fullmatch("1793145600-1793187900.0.slot.json") is None
       and tz27.ASSET_RE.fullmatch("1793145600-1793187900.0.stream.jsonl.gz") is None, "the asset names")
    ok(day_of(D0) == D0 and day_of(D1 - 1) == D0 and day_of(D1) == D1 and DECIDE_S == 6
       and 128 * 2 ** 20 == ARCHIVE_MEMORY_MAX and 6 * 3600 == TIMEOUT_S and 30 * 60 == ACTIVE_S,
       "the day, the decision at S - 6, 128M, 6h and 30min in bytes and seconds")
    ok(next_slots((D1 + 600) * 10 ** 9, (D1 + 700) * 10 ** 9) == [D1 + 900]
       and next_slots((D1 + 894) * 10 ** 9, (D1 + 894) * 10 ** 9) == [D1 + 900]
       and next_slots((D1 + 895) * 10 ** 9, (D1 + 1000) * 10 ** 9) == [D1 + 1800]
       and next_slots((D1 + 500) * 10 ** 9, (D1 + 1000) * 10 ** 9) == [D1 + 900, D1 + 1800],
       "G-NEXT's slots: decided from the first removal to 900 s after the last")
    # the reward book's quiet before a removal
    sel = {"event": "select", "day": D1, "ok": True, "wall_ns": (D1 - 900) * 10 ** 9}
    st0 = {"event": "start", "pid": 3137952, "wall_ns": (D1 - 3600) * 10 ** 9}
    t = D1 + 3615
    ok(quiet([sel, st0], [3137952], t) is None and quiet([st0], [3137952], t) is not None
       and quiet([dict(sel, ok=False), st0], [3137952], t) is not None
       and quiet([dict(sel, wall_ns=(t - 4) * 10 ** 9), st0], [3137952], t) is not None
       and quiet([sel, st0], [3137952, 3200000], t) is not None
       and quiet([sel, st0, {"event": "start", "pid": 3200000, "wall_ns": (t - 9) * 10 ** 9}], [3200000], t)
       is not None
       and quiet([sel, st0, {"event": "start", "pid": 3200000, "wall_ns": (t - 10) * 10 ** 9}], [3200000], t)
       is None and quiet([sel], [], t) is None
       and quiet([dict(sel, day=D0), st0], [3137952], t) is not None,
       "a removal waits for the day's selection 5 s old and for a process with its start record 10 s old")
    # G-NEXT's verdicts on literal records
    good = {"pid": 3137952, "stopped": False, "error": None, "stream": {"opened": True, "off_reason": None}}
    ok(next_verdict([(0, good)], [], "3137952")[0] == "PASS"
       and next_verdict([], [], "3137952")[0] == "FAIL"
       and next_verdict([(0, good)], [{"error": "FileNotFoundError: x"}], "3137952")[0] == "FAIL"
       and next_verdict([(0, dict(good, stopped=True)), (1, dict(good, pid=3200000))], [], "3137952")[0]
       == "UNDECIDABLE"
       and next_verdict([(0, dict(good, stream={"opened": False, "off_reason": "floor"}))], [], "3137952")[0]
       == "UNDECIDABLE"
       and next_reading([("PASS", ""), ("UNDECIDABLE", "")]) == "UNDECIDABLE"
       and next_reading([("PASS", ""), ("FAIL", "")]) == "FAIL" and next_reading([("PASS", "")]) == "PASS"
       and next_reading([]) == "UNDECIDABLE",
       "G-NEXT: a slot without its slot.json or with an error record fails; the worst over the slots reads")
    # G-STILL's chain
    u = {"recorder": {"MainPID": "2388318", "NRestarts": "0", "ActiveState": "active"},
         "pairbook": {"MainPID": "3121425", "NRestarts": "11", "ActiveState": "active"},
         "rewardbook": {"MainPID": "3137952", "NRestarts": "1", "ActiveState": "active"}}
    moved = dict(u, pairbook={"MainPID": "3300002", "NRestarts": "13", "ActiveState": "active"})
    chain = [{"stopped": "3121425", "pid": "3300001", "NRestarts": 12},
             {"stopped": "3300001", "pid": "3300002", "NRestarts": 13}]
    m0 = D1 + 3600
    ok([trigger_reading(t, m0, s0_, lt)[0] for t, s0_, lt in (
        ({"unit": TIMER, "realtime_usec": str((m0 + 1800) * 10 ** 6)}, m0 + 1801, m0 + 9000),
        ({"unit": TIMER, "realtime_usec": str((m0 + 1798) * 10 ** 6)}, m0 + 1798, None),
        ({"unit": TIMER, "realtime_usec": str((m0 + 1797) * 10 ** 6)}, m0 + 1797, None),
        ({"unit": "btc-pairbook-archive.timer", "realtime_usec": str((m0 + 1800) * 10 ** 6)}, m0 + 1800, None),
        ({"unit": TIMER, "realtime_usec": str((m0 + 1800) * 10 ** 6)}, m0 + 1861, None),
        ({"unit": None}, m0 + 1800, m0 + 1800), (None, m0 + 3500, m0 + 3499), ({"unit": None}, m0 + 1800, m0 + 1805),
        ({"unit": None}, m0 + 1800, None))]
       == [True, True, False, False, False, True, True, False, False],
       "G-TRIGGER: the run's own trigger where systemd set it, else the timer's last; 1,800 s after the mark less 2")
    ok(still_reading(u, u, [])[0] and still_reading(u, moved, chain)[0]
       and not still_reading(u, moved, chain[:1])[0]
       and not still_reading(u, dict(moved, rewardbook=dict(u["rewardbook"], MainPID="3300009")), chain)[0]
       and not still_reading(u, dict(u, recorder=dict(u["recorder"], NRestarts="1")), [])[0],
       "G-STILL: the recorder and the reward book unchanged, the pair book unchanged or moved by its archive's chain")
    # both hooks, under the modes the run gives them
    s0 = ROOT + "/%d/%d.0.stream.jsonl.gz" % (D1, D1 + 900)
    j0 = ROOT + "/%d/%d.0.slot.json" % (D1, D1 + 900)
    r0 = ROOT + "/%d/%d.0.rewards.jsonl.gz" % (D1, D1 + 900)
    q0 = ROOT + "/%d/select.0.json" % D1

    def allow(mode, event, args, removable=frozenset()):
        return tz27.policy(mode, event, args, STATE, set(removable)) is None and policy34(mode, event, args) is None \
            if event != "os.remove" else (_allow_remove(mode, args, removable))

    def _allow_remove(mode, args, removable):
        saved = set(tz27.ALLOWED_REMOVE)
        tz27.ALLOWED_REMOVE.clear()
        tz27.ALLOWED_REMOVE.update(removable)
        try:
            return tz27.policy(mode, "os.remove", args, STATE, set(removable)) is None and \
                policy34(mode, "os.remove", args) is None
        finally:
            tz27.ALLOWED_REMOVE.clear()
            tz27.ALLOWED_REMOVE.update(saved)

    ok([allow(m, "open", (s0, "rb", 0)) for m in ("inventory", "upload", "delete", "verify", "final", "hold", "run")]
       == [True, True, True, False, False, False, False]
       and not any(allow(m, "open", (s0, fm, 0)) for m in ("inventory", "upload", "delete", "final")
                   for fm in ("wb", "ab", "r+b", "xb")),
       "a stream file is read by the set, the upload and the removal alone, and written by no mode")
    ok(not any(allow(m, "open", (p, "rb", 0)) for m in ("inventory", "upload", "delete", "final", "still")
               for p in (r0, q0, ROOT + "/service.log", ROOT + "/service.pid"))
       and allow("final", "open", (j0, "rb", 0)) and not allow("inventory", "open", (j0, "rb", 0))
       and allow("delete", "open", (ROOT + "/runtime.jsonl", "rb", 0))
       and allow("final", "open", (ROOT + "/runtime.jsonl", "rb", 0))
       and not allow("upload", "open", (ROOT + "/runtime.jsonl", "rb", 0)),
       "no rewards file or selection is read; slot.json by final alone; runtime.jsonl by delete and final")
    ok(allow("delete", "os.remove", (s0, None), {s0}) and not allow("delete", "os.remove", (s0, None))
       and not allow("upload", "os.remove", (s0, None), {s0}) and not allow("delete", "os.remove", (j0, None), {j0})
       and not allow("delete", "os.rename", (s0, STATE + "/x"), {s0})
       and allow("inventory", "os.scandir", (ROOT,)) and allow("final", "os.scandir", (ROOT + "/%d" % D1,))
       and not allow("upload", "os.scandir", (ROOT,)),
       "a stream file removed only by the removal, only where the run names it; the store listed by three modes")
    ok(not any(allow(m, ev, args) for m in ("inventory", "upload", "delete", "final", "still", "selftest")
               for ev, args in (("open", (PAIRBOOK + "/1793187000/window.json", "rb", 0)),
                                ("os.scandir", (PAIRBOOK,)), ("open", (PAIR_STATE + "/runs/1/set.json", "rb", 0))))
       and allow("still", "open", (PAIR_LEDGER, "rb", 0)) and not allow("final", "open", (PAIR_LEDGER, "rb", 0))
       and not allow("upload", "open", (PAIR_LEDGER, "rb", 0))
       and not allow("still", "open", (PAIR_LEDGER, "ab", 0))
       and not allow("final", "open", (tz27.RECORDER + "/runtime.jsonl", "rb", 0))
       and not allow("inventory", "subprocess.Popen", ("systemctl",)) and allow("hold", "subprocess.Popen", ("x",))
       and not allow("delete", "subprocess.Popen", ("systemctl",))
       and allow("run", "open", (STATE + "/ledger.jsonl", "ab", 0))
       and not allow("run", "open", (tz27.FORENSICS + "/x", "xb", 0)),
       "nothing of the pair book's store, its archive's ledger read by still alone, no process in the set or the "
       "removal, the run writes under its state alone")
    # the units, as this file reads them
    for unit, want in ((ARCHIVE, ["Type=oneshot", "WorkingDirectory=" + STATE, "ExecStart=" + " ".join(RUN_ARGV),
                                  "Restart=no", "TimeoutStartSec=%d" % TIMEOUT_S, "Nice=19", "MemoryMax=128M",
                                  "StandardOutput=append:%s/archive.log" % STATE,
                                  "StandardError=append:%s/archive.log" % STATE]),
                       (TIMER, ["OnCalendar=" + CALENDAR, "OnActiveSec=%d" % ACTIVE_S, "AccuracySec=1s",
                                "Unit=" + ARCHIVE, "WantedBy=timers.target"])):
        with open(os.path.join(os.path.dirname(HERE), "deploy", "systemd", unit), encoding="utf-8") as fh:
            lines = [ln for ln in fh.read().split("\n") if ln and not ln.startswith("#") and not ln.startswith("[")]
        ok(all(x in lines for x in want), "%s: %d of its lines as this file runs them" % (unit, len(want)))
    # the reward book's own constants and its own sum, read from its text
    tree = ast.parse(tz33_text())
    vals = tz33_values(tree, ("ROOT", "SVC", "PYTHON", "SERVICE_FILE", "SERVICE_ARGV", "DAY", "SLOT", "OPEN_BEFORE",
                              "SLOT_JSON_AT", "LAUNCH_LEAD", "STREAM_FLOOR", "STREAM_CAP", "SLOT_STREAM_MAX",
                              "DAY_RE", "SLOT_FILE_RE"))
    ok({k: vals[k] for k in RESTATED} == RESTATED and vals["PYTHON"] == tz27.PYTHON,
       "the reward book's %d constants this file restates, equal to its text's" % len(RESTATED))
    total33 = tz33_function(tree, "stream_bytes_total")
    # the run on temporary stores, a simulated reward book and the loopback server
    for k in [k for k in list(os.environ) if k.lower() in ("http_proxy", "https_proxy", "all_proxy", "no_proxy")]:
        del os.environ[k]
    tmp = tz27.wpath("selftest-tmp")
    if os.path.lexists(tmp):
        shutil.rmtree(tmp)
    tok = "ghp_" + "Ab3" * 12
    Fake = tz27._FakeGitHub
    Fake.releases.clear()
    Fake.assets.clear()
    Fake.hits.clear()
    Fake.refuse_once.clear()
    Fake.omit_digest[0] = False
    Fake.token = tok
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Fake)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    base = "http" + sep + "127.0.0.1:%d" % srv.server_address[1]
    Fake.web = base
    blobs = {}

    def put(root, s, name, nbytes):
        d = os.path.join(root, str(day_of(s)))
        os.makedirs(d, exist_ok=True)
        data = (hashlib.sha256(name.encode()).digest() * (nbytes // 32 + 1))[:nbytes]
        with open(os.path.join(d, name), "wb") as fh:
            fh.write(data)
        blobs[name] = data

    def slot(root, s, streams, closed=True):
        for k_, nb in enumerate(streams):
            if nb is not None:
                put(root, s, "%d.%d.stream.jsonl.gz" % (s, k_), nb)
            put(root, s, "%d.%d.rewards.jsonl.gz" % (s, k_), 300)
            if closed:
                put(root, s, "%d.%d.slot.json" % (s, k_), 200)

    def world(name, t0):
        root, state = os.path.join(tmp, name, "store"), os.path.join(tmp, name, "state")
        os.makedirs(root)
        os.makedirs(state)
        env = FakeEnv(tz27.WORK[0], root, state, base, t0, tok)
        for d in range(D0, D1 + 10 * DAY, DAY):
            env.recs.append({"event": "select", "day": d, "ok": True, "wall_ns": (d - 900) * 10 ** 9})
        env.recs.append({"event": "start", "pid": 3137952, "wall_ns": (D0 + 41400) * 10 ** 9})
        put(root, D0, "select.0.json", 500)
        return env

    def evs(env):
        return [r["event"] for r in tz28.Ledger(env.state).recs]

    try:
        # 1. a whole run: closed slots, a slot of two processes, a slot whose stream stayed off, an unclosed slot
        # and two open ones; the pair book's archive running at the upload phase
        env = world("one", D1 + 3600 + 20)
        slot(env.root, D1 - 1800, [70001])
        slot(env.root, D1 - 900, [50000, 33333])
        slot(env.root, D1, [None])
        slot(env.root, D1 + 900, [40000], closed=False)
        slot(env.root, D1 + 1800, [44444])
        slot(env.root, D1 + 2700, [55555])
        slot(env.root, D1 + 3600, [123], closed=False)
        ok(stream_bytes_view(env.root) == total33(env.root) == 70001 + 50000 + 33333 + 40000 + 44444 + 55555 + 123,
           "this file's sum of the store's streams equals the reward book's own, run from its text")
        env.busy_until = env.clock + 1000
        rc = run(env)
        led = tz28.Ledger(env.state).recs
        a = led[0]["run"]
        ok(rc == 0 and evs(env) == ["start", "set", "hold", "upload", "verify", "delete", "complete"]
           and a == D1 + 3620, "a run: every step recorded, in order, exit 0")
        setr = tz28.events(led, a, "set")[0]
        ok(setr["assets_n"] == 4 and setr["bytes_total"] == 197778 and setr["first_S"] == D1 - 1800
           and setr["last_S"] == D1 + 1800 and setr["tag"] == "rewardbook-streams-%d" % a
           and (setr["slots_considered"], setr["closed"], setr["unclosed"], setr["open"], setr["streamless"],
                setr["deferred"]) == (4, 3, 1, 2, 1, 0),
           "the set: every stream file of a closed slot due 60 s before A, under this TZ's tag")
        hr = tz28.events(led, a, "hold")[0]
        ok(hr["phase"] == "upload" and hr["waited_s"] == 1000, "the upload held while the pair book's archive ran")
        rel = Fake.releases["rewardbook-streams-%d" % a]
        held = sorted(v["name"] for v in Fake.assets.values() if v["rid"] == rel["id"])
        want = ["%d-%d.0.stream.jsonl.gz" % (D0, D1 - 1800), "%d-%d.0.stream.jsonl.gz" % (D0, D1 - 900),
                "%d-%d.1.stream.jsonl.gz" % (D0, D1 - 900), "%d-%d.0.stream.jsonl.gz" % (D1, D1 + 1800)]
        ok(held == sorted(want) and all(v["data"] == blobs[v["name"][11:]] for v in Fake.assets.values()
                                        if v["rid"] == rel["id"]),
           "the Release holds the set's four files, byte for byte")
        left = sorted(os.listdir(os.path.join(env.root, str(D1))))
        ok(sorted(os.listdir(os.path.join(env.root, str(D0)))) == sorted(
            ["%d.0.rewards.jsonl.gz" % (D1 - 1800), "%d.0.slot.json" % (D1 - 1800),
             "%d.0.rewards.jsonl.gz" % (D1 - 900), "%d.0.slot.json" % (D1 - 900), "%d.1.rewards.jsonl.gz" % (D1 - 900),
             "%d.1.slot.json" % (D1 - 900), "select.0.json"])
           and "%d.0.stream.jsonl.gz" % (D1 + 900) in left and "%d.0.stream.jsonl.gz" % (D1 + 2700) in left
           and "%d.0.stream.jsonl.gz" % (D1 + 3600) in left and "%d.0.stream.jsonl.gz" % (D1 + 1800) not in left
           and "%d.0.slot.json" % (D1 + 1800) in left,
           "the store: the set's files gone; slot.json, rewards, selections, the unclosed and the open streams kept")
        rdir = os.path.join(env.state, "runs", str(a))
        trs = tz28.jsonl_read(os.path.join(rdir, "transfers.jsonl"))
        rms = tz28.jsonl_read(os.path.join(rdir, "delete.jsonl"))
        comp = tz28.events(led, a, "complete")[0]
        ok(len([t for t in trs if t["kind"] == "upload"]) == 4 and len([t for t in trs if t["kind"] == "download"])
           == 4 and len(rms) == 4 and all(all(tz28.transfer_ok(t)) for t in trs)
           and all(all(tz28.transfer_ok(removal_span(r))) for r in rms)
           and comp["started_outside"] == 0 and comp["ended_outside"] == 0 and comp["removals"] == 4
           and all(h[2] == tz27.UA for h in Fake.hits)
           and all(h[3] is None for h in Fake.hits if "/releases/download/" in h[1] or h[1].startswith("/blob/")),
           "every request and every removal inside the idle stretch; reads with no token, every request TZ-27's")
        with open(os.path.join(env.state, "runs", str(a), "set.json"), "rb") as fh:
            raw1 = fh.read()
        doc1, sets1 = json.loads(raw1), tz28.events(led, a, "set")
        sl = store_left(env.root, doc1)
        ok(sl == (["%d.0.stream.jsonl.gz" % (D1 + 900)], [], [], []) and set_reading(doc1, raw1, sets1, *sl[1:]),
           "G-SET read on the store: the unclosed slot's stream left alone, nothing of a closed or unrecorded slot")
        put(env.root, D1 + 900, "%d.0.slot.json" % (D1 + 900), 200)
        put(env.root, D1 - 2700, "%d.0.stream.jsonl.gz" % (D1 - 2700), 10)
        sl2 = store_left(env.root, doc1)
        ok(sl2[2:] == (["%d.0.stream.jsonl.gz" % (D1 - 2700)], [D1 + 900]) and not set_reading(doc1, raw1, sets1,
                                                                                               *sl2[1:])
           and not set_reading(doc1, raw1, sets1 + sets1, *sl[1:])
           and not set_reading(dict(doc1, deferred=1), raw1, sets1, *sl[1:]),
           "G-SET fails on a stream of a slot it does not record, a slot.json not as recorded, two sets, a deferral")
        os.remove(os.path.join(env.root, str(day_of(D1 + 900)), "%d.0.slot.json" % (D1 + 900)))
        os.remove(os.path.join(env.root, str(day_of(D1 - 2700)), "%d.0.stream.jsonl.gz" % (D1 - 2700)))
        ok(comp["store_stream_bytes"] == 40000 + 55555 + 123 == stream_bytes_view(env.root)
           and tz28.events(led, a, "delete")[0]["freed"] == 197778
           and comp["rewardbook_at_end"]["MainPID"] == "3137952",
           "the store's streams after the run: the unclosed and the open slots' alone")
        # 2. the next run takes the slot that came due after the first run's A; the run after it finds none: empty
        env.clock += 300
        ok(run(env) == 0 and evs(env)[-1] == "complete", "the next run completes")
        set2 = [r for r in tz28.Ledger(env.state).recs if r["event"] == "set"][-1]
        ok(set2["assets_n"] == 1 and set2["bytes_total"] == 55555 and set2["first_S"] == set2["last_S"] == D1 + 2700
           and (set2["slots_considered"], set2["closed"], set2["unclosed"], set2["open"], set2["streamless"])
           == (3, 1, 2, 0, 4), "the next run takes the slot due after the first run's A, and only it")
        env.clock += 10
        ok(run(env) == 0 and evs(env)[-2:] == ["start", "empty"]
           and (tz28.Ledger(env.state).recs[-1]["slots_considered"], tz28.Ledger(env.state).recs[-1]["unclosed"])
           == (2, 2), "a run with no stream file of a closed slot records empty, exit 0")
        # 3. a refused credential defers, and the next run resumes the same set
        env3 = world("defer", D1 + 3600 + 588)
        slot(env3.root, D1 + 900, [1000])
        env3.cred_ok = False
        rc3 = run(env3)
        a3 = tz28.Ledger(env3.state).recs[0]["run"]
        ok(rc3 == tz28.EXIT_DEFERRED and evs(env3) == ["start", "set", "deferred"]
           and os.path.exists(os.path.join(env3.root, str(D1), "%d.0.stream.jsonl.gz" % (D1 + 900))),
           "a refused credential: deferred, exit 75, nothing removed")
        env3.cred_ok = True
        env3.clock += 86400
        ok(run(env3) == 0 and [r["run"] for r in tz28.Ledger(env3.state).recs if r["event"] == "start"] == [a3, a3]
           and evs(env3)[-1] == "complete", "the next run resumes the deferred set and completes it")
        trs3 = tz28.jsonl_read(os.path.join(env3.state, "runs", str(a3), "transfers.jsonl"))
        ok(tz28.phase_of(trs3[0]["start_ns"] // 10 ** 9) == 15 and all(all(tz28.transfer_ok(t)) for t in trs3),
           "a request due at second 588 waits for the next idle stretch")
        # 4. three deferrals halt the archive; a halted archive refuses until a clear
        env4 = world("halt", D1 + 3 * 86400 + 20)
        slot(env4.root, D1 + 900, [1000])
        env4.cred_ok = False
        rcs = [run(env4) for _k in range(3)]
        ok(rcs == [tz28.EXIT_DEFERRED, tz28.EXIT_DEFERRED, 1] and evs(env4)[-2:] == ["halt", "timer-disabled"]
           and env4.disabled == 1, "the third deferral of one set halts, and the run disables its timer")
        env4.cred_ok = True
        ok(run(env4) == 1 and evs(env4)[-1] == "refused" and env4.disabled == 2
           and os.path.exists(os.path.join(env4.root, str(D1), "%d.0.stream.jsonl.gz" % (D1 + 900))),
           "a halted archive refuses the next run, and removes nothing")
        tz28.jsonl_append(os.path.join(env4.state, "ledger.jsonl"), {"event": "clear", "run": None, "wall_ns": 0}, "x")
        env4.clock += 60
        ok(run(env4) == 0 and evs(env4)[-1] == "complete", "after a clear the next run takes a new set")
        # 5. a flipped bit in one asset fails the verify: deferred, nothing removed; mended, the next run completes
        env5 = world("verify", D1 + 5 * 86400 + 20)
        slot(env5.root, D1 + 900, [5000, 6000])

        def corrupt(e):
            if e.on_sleep is corrupt:
                e.on_sleep = None
                k_ = sorted(Fake.assets)[-1]
                good_ = Fake.assets[k_]["data"]
                Fake.assets[k_]["data"] = good_[:-1] + bytes([good_[-1] ^ 1])
                corrupt.saved = (k_, good_)

        env5.on_sleep = corrupt
        ok(run(env5) == tz28.EXIT_DEFERRED and evs(env5)[-1] == "deferred"
           and "VERIFY FAIL" in tz28.Ledger(env5.state).recs[-1]["reason"]
           and os.path.exists(os.path.join(env5.root, str(D1), "%d.1.stream.jsonl.gz" % (D1 + 900))),
           "a flipped bit in one asset: VERIFY FAIL, deferred, nothing removed")
        k5, good5 = corrupt.saved
        Fake.assets[k5]["data"] = good5
        ok(run(env5) == 0 and evs(env5)[-1] == "complete", "the asset mended, the next run verifies and completes")
        # 6. the day's selection missing at the removal: the removals wait for it, 5 s after its record
        env6 = world("select", D1 + DAY + 3600 + 20)
        slot(env6.root, D1 + DAY + 900, [7000])
        env6.recs = [r for r in env6.recs if r.get("day") != D1 + DAY]
        late = (D1 + DAY + 3600 + 20 + 600) * 10 ** 9

        def appear(e):
            if e.time_ns() >= late and not [r for r in e.recs if r.get("day") == D1 + DAY]:
                e.recs.append({"event": "select", "day": D1 + DAY, "ok": True, "wall_ns": late})

        env6.on_sleep = appear
        ok(run(env6) == 0 and evs(env6)[-1] == "complete", "the removal waited for the day's selection and completed")
        r6 = tz28.jsonl_read(os.path.join(env6.state, "runs", str(D1 + DAY + 3620), "delete.jsonl"))[0]
        ok(r6["start_ns"] >= late + 5 * 10 ** 9 and all(tz28.transfer_ok(removal_span(r6))),
           "the first removal 5 s or more after the selection's record, inside the idle stretch")
        # 7. the selection never recorded: the removals defer after QUIET_MAX_S; recorded, the next run completes
        env7 = world("quiet", D1 + 2 * DAY + 3600 + 20)
        slot(env7.root, D1 + 2 * DAY + 900, [7000, 8000])
        env7.recs = [r for r in env7.recs if r.get("day") != D1 + 2 * DAY]
        ok(run(env7) == tz28.EXIT_DEFERRED and tz28.Ledger(env7.state).recs[-1]["phase"] == "delete"
           and "QuietTimeout" in tz28.Ledger(env7.state).recs[-1]["reason"]
           and os.path.exists(os.path.join(env7.root, str(D1 + 2 * DAY),
                                           "%d.0.stream.jsonl.gz" % (D1 + 2 * DAY + 900))),
           "the selection never recorded: the run defers in its removal, nothing removed")
        env7.recs.append({"event": "select", "day": D1 + 2 * DAY, "ok": True, "wall_ns": (D1 + 2 * DAY) * 10 ** 9})
        env7.clock += 3600
        ok(day_of(env7.clock) == D1 + 2 * DAY and run(env7) == 0 and evs(env7)[-1] == "complete"
           and evs(env7).count("verify") == 2,
           "the next run resumes the set - its uploads held, verified again - and completes the removal")
        # 8. a removal deferred half-way: the files removed recorded, the rest removed by the next run
        env8 = world("partial", D1 + 3 * DAY + 3600 + 20)
        slot(env8.root, D1 + 3 * DAY + 900, [1000, 2000, 3000])
        p8 = os.path.join(env8.state, "runs", str(D1 + 3 * DAY + 3620), "delete.jsonl")
        env8.pids_fn = lambda e: [3300000] if len(tz28.jsonl_read(p8)) >= 2 else [3137952]
        rc8 = run(env8)
        ok(rc8 == tz28.EXIT_DEFERRED and len(tz28.jsonl_read(p8)) == 2
           and "QuietTimeout" in tz28.Ledger(env8.state).recs[-1]["reason"],
           "a new process without its start record: the removals wait, then defer with two of three files removed")
        env8.pids_fn = None
        env8.clock += 3600
        ok(run(env8) == 0 and len(tz28.jsonl_read(p8)) == 3
           and tz28.events(tz28.Ledger(env8.state).recs, D1 + 3 * DAY + 3620, "delete")[-1]["already"] == 2,
           "the next run resumes: two removals already recorded, the third removed")
        # 9. a file changed after the verify: the removal finds it is not the set's, and the archive halts
        env9 = world("changed", D1 + 4 * DAY + 3600 + 20)
        slot(env9.root, D1 + 4 * DAY + 900, [4000])
        env9.recs.append({"event": "select", "day": D1 + 4 * DAY, "ok": True, "wall_ns": 0})
        p9 = os.path.join(env9.root, str(D1 + 4 * DAY), "%d.0.stream.jsonl.gz" % (D1 + 4 * DAY + 900))

        def grow(e):
            if e.on_sleep is grow and tz28.events(tz28.Ledger(e.state).recs, D1 + 4 * DAY + 3620, "upload"):
                e.on_sleep = None
                with open(p9, "ab") as fh:
                    fh.write(b"x")

        env9.on_sleep = grow
        ok(run(env9) == 1 and evs(env9)[-2:] == ["halt", "timer-disabled"]
           and "not the set's" in tz28.Ledger(env9.state).recs[-2]["reason"] and os.path.exists(p9),
           "a stream file changed after its verify: the removal refuses it and the archive halts")
        # 10. the pair book's archive running past HOLD_MAX_S: the run defers before its upload
        env10 = world("hold", D1 + 5 * DAY + 3600 + 20)
        slot(env10.root, D1 + 5 * DAY + 900, [3000])
        env10.busy_until = env10.clock + HOLD_MAX_S + 100
        ok(run(env10) == tz28.EXIT_DEFERRED and "HoldTimeout" in tz28.Ledger(env10.state).recs[-1]["reason"]
           and tz28.Ledger(env10.state).recs[-1]["phase"] == "upload" and not Fake.releases.get(
               "rewardbook-streams-%d" % (D1 + 5 * DAY + 3620)),
           "a hold past 1,800 s defers the run before any request")
        ok(not [h for h in Fake.hits if h[3] not in (None, "Bearer " + tok)],
           "the loopback server saw no credential but the run's")
    finally:
        srv.shutdown()
        srv.server_close()
    shutil.rmtree(tmp)
    ok(not os.path.lexists(tmp), "the temporary stores removed")
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            mods |= {x.name.split(".")[0] for x in node.names}
        elif isinstance(node, ast.ImportFrom):
            mods.add((node.module or "").split(".")[0])
    ok(mods <= set(sys.stdlib_module_names), "imports: the standard library alone")
    ok(not [c_ for c_ in ast.walk(tree) if isinstance(c_, ast.Constant) and isinstance(c_.value, str)
            and sep in c_.value], "no endpoint in this file's text: every request is TZ-27's")
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz34-rewardbook-archive-timer.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    rc = 0
    if mode == "run":
        assert not rest, "run takes no argument"
        rc = mode_run()
    else:
        cwd = os.getcwd()
        assert tz27.WORK_RE.fullmatch(cwd), "run from a work tree /root/tzNN-work, not %s" % cwd
        tz27.WORK[0], tz27.MODE[0] = cwd, mode
        if mode == "mark":
            assert len(rest) == 1, "mark NAME"
            mode_mark(rest[0])
        elif mode == "scratch":
            assert len(rest) == 1, "scratch OWN"
            tz27.mode_scratch(rest[0])
        elif mode == "reclaim":
            tz27.mode_reclaim(rest)
        elif mode == "still":
            assert not rest, "still takes no argument"
            rc = 0 if mode_still() else 1
        elif mode == "first":
            assert not rest, "first takes no argument"
            rc = mode_first()
        else:
            table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "path": tz28.mode_path,
                     "path-token": tz28.mode_path_token, "installed": mode_installed, "timer": mode_timer,
                     "final": mode_final, "stopped": mode_stopped}
            assert mode in table and not rest, "unknown mode %r" % (argv,)
            table[mode]()
    out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
    out("opens refused: %d by TZ-27's hook, %d by this file's; store opens %d; requests %d, uploads %d, downloads %d "
        "(%d bytes); files removed %d" % (len(tz27.REFUSED), len(REFUSED34), tz27.STORE_OPENS[0],
                                          tz27.COUNTERS["requests"], tz27.COUNTERS["uploads"],
                                          tz27.COUNTERS["downloads"], tz27.COUNTERS["download_bytes"],
                                          tz27.COUNTERS["removed"]))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
