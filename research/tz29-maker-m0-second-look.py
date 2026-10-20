#!/usr/bin/env python3
"""TZ-29 - M0's second look: do the makers of btc-updown-5m earn, at settlement and with the 20% rebate, on the
fills inside [T0, T0 + 240), over TZ-23's 4,032 markets and the next 4,032 that qualify after them?

    fingerprint       contract section 1 steps 3 and 4, asserted: the map's revision, anchors and rows
    selftest          every rule of this file, on literals and on temporary trees under the work tree
    still             the recorder's and the pair book's MainPID, NRestarts and ActiveState: the first run
                      records them, the second compares (G-STILL)
    scratch OWN       the UUID directories beside OWN, this session's, each named live or earlier
    archive           the pair book archive's ledger, read and printed, beside the tags origin carries
    rehearse          the whole path on TZ-23's rehearsal span, every request held to the idle stretch
                      (G-REHEARSAL)
    replay            the first look, from the forensic store, scored again by TZ-23's score (G-REPLAY)
    fetch             the second set - the first 4,032 qualifying markets with T0 > 1791241800 - and
                      their taker fills, every request held to the idle stretch (G-SET)
    constants         label-free: the second look's sums, by TZ-23's build_constants, and both looks'
                      V, Sh, thresholds and power, on disk
    score             the labels of both looks, read once, and M0's reading over both
    reclaim TREE...   section 9

It loads research/tz23-maker-m0.py from beside itself, executed from the bytes whose SHA-256 it asserts,
and calls TZ-23's functions for the walk, the documents, the fills of a chunk, every sum, the thresholds
and the score: it writes no second implementation of any of them. Its requests are TZ-23's, to
gamma-api.polymarket.com and data-api.polymarket.com through TZ-23's http_json and its two headers, each
walk and each chunk started only inside seconds 15 to 470 of a 900-second window and never near or
during the pair book archive's run; and git against origin. Under /var/lib/btc-recorder,
/var/lib/btc-chainbook and /var/lib/btc-pairbook it opens and lists nothing, and under
/var/lib/btc-pairbook-archive it opens ledger.jsonl alone, for reading, in mode archive: an audit hook
refuses everything else there. It writes under /root/tz29-work/ and, in `reclaim`, new files in
/root/btc-forensics/ by exclusive create. It prints sums over a set and no price, size or outcome of any
single fill or market. Exit 0: every assert of the mode held. Exit 1: an assert failed, and its message
names it. Run it with the recorder's interpreter, /root/tz04a-env.

Written for CryptoTZ/TZ-29-maker-m0-second-look.md. The TZ is the specification.
"""

import concurrent.futures
import hashlib
import json
import os
import re
import resource
import shutil
import subprocess
import sys
import time
import types

if not __debug__:
    sys.stderr.write("tz29: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

HERE = os.path.dirname(os.path.abspath(__file__))
TZ23_NAME = "tz23-maker-m0.py"
TZ23_SHA256 = "6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f"


def load_tz23(path):
    """TZ-23's instrument, executed from the very bytes whose SHA-256 is asserted. It installs its audit hook,
    sets the main thread's decimal precision to 60 digits and tunes glibc's malloc."""
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

MAP_REVISION = "2026-10-19-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 37, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"`?([0-9a-f]{64}|self-reference[^|]*?)`? \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)

LAST_FIRST = 1791241800      # M0's first look's last member, 2026-10-05 23:10 UTC (TZ-23)
START2 = LAST_FIRST + 300    # the second look's walk starts at the next five-minute market
N_SET = 4032                 # TZ-23's N_SET: two whole weeks of five-minute markets
START_AT = START2 + (N_SET - 1) * 300 + 3900    # 2026-10-20 00:15:00 UTC: no mode reads the second set before
WALK_TRIES = 25              # a walk stopped on a market too recent to be resolved is walked again,
WALK_RETRY_S = 300           # 300 s later, at most 24 times more
FETCH_BUDGET_S = 7200        # a fetch projected past this after its first 30 chunks is BLOCKED
WINDOW_S = 900               # the pair book's window: its stream from T+595 to T+905, window.json at T+910
IDLE = (15, 590)             # its idle stretch: a request starts at second 15 or later and ends by 590
CHUNK_BUDGET_S = 120         # a chunk or a walk starts no later than second 470
ARCHIVE_UNIT = "btc-pairbook-archive.service"
ARCHIVE_TIMER = "btc-pairbook-archive.timer"
ARCHIVE_CALENDAR_S = 10820   # the archive's calendar run, 03:00:20 UTC
ARCHIVE_LEAD_S = 60          # nothing starts from budget + 60 s before it to 60 s after it
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")
HOLD_MAX_S = 7200            # one window and an archive's run fit in it many times over
MEM_FLOOR = 177135616        # MemAvailable: twice the largest peak of any mode, constants' (TZ-29 section 0.4)

WORK = "/root/tz29-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/label-ledger.jsonl"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
BRANCH = "tz-29-maker-m0-second-look"
UNITS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service"}
CAPTURE_ROOTS = ("/var/lib/btc-recorder", "/var/lib/btc-chainbook", "/var/lib/btc-pairbook")
ARCHIVE_STATE = "/var/lib/btc-pairbook-archive"
ARCHIVE_LEDGER = ARCHIVE_STATE + "/ledger.jsonl"
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}

# The first look in the forensic store, each file by its size and SHA-256 in TZ-23's report (its 2.13 and 2.14)
STORE = FORENSICS + "/tz23-work--set--"
FIRST = {"set": (STORE + "set.json", 2314799,
                 "a04226f0ec324400fa493f8101b24becf2e0609e614e60aa11d6adeacae76303"),
         "fills": (STORE + "tz23-fills.jsonl.gz", 36870673,
                   "4f20400e20913dec4bff8cd715f03934dc1bde0933214258414afd55cdf55a64"),
         "members": (STORE + "tz23-members.csv", 2444450,
                     "cf269016781bca698eb0d707e5aea3ce5dfefc15d8a068b4deb85a03ec229a61"),
         "constants": (STORE + "tz23-constants.json", 2114,
                       "1b28df4382ed926ad92d514cb9bbfd6764e15a90b3e4c39618115db5e30217d5"),
         "scored": (STORE + "tz23-scored.csv", 464610,
                    "12002203479ac5634c509c4f4306b42159e74d10cf987839fad6ec7022bdb988"),
         "reading": (STORE + "tz23-reading.json", 1915,
                     "fdad516faaa3abfa7cc70134d19caa2be562d636235b464506a971893aef4043")}
# and its figures, as TZ-23's report prints them (its 2.7 and 2.9)
FIRST_FIGURES = {"members": 4032, "ups": 2023, "first": 1788530400, "last": LAST_FIRST,
                 "member_list_sha": "699cab9aa3f540b6cdfe2ae8a295b1fa4bca96921238106dad4b243bc4ecce4f",
                 "V": D("69635266807.031814646570"), "sh": D("129225737.554660"),
                 "S": D("272424.11263025802271516797439628522"), "reading": "UNDECIDABLE"}
# TZ-23's rehearsal files, by its report (its 2.5 and 2.13): the venue's record of the 144 markets, byte for byte
REHEARSAL_FILES = {"set.json": "83a53bd3fb13829173282487833ef0398280d358377e0f09d0beb414c7829cbc",
                   "rehearsal-fills.jsonl.gz": "3ce50a85f84068a4cac15ece53d2ea1b16184b9080d69228b0baae8f887c8116",
                   "rehearsal-members.csv": "2676af1dee730001abf560555c1c0eb9b88901209a94598dcb966495e20131d1",
                   "rehearsal-constants.json": "9f521a23b3a5b48ac7569f68a9c42bf6da1bb8ef09f5a71c0c8e091fbf5098e3",
                   "rehearsal-scored.csv": "d31eb18fa58f8a26f12979f733fcead3b2482a480ba97a17c1145c1eef99bda2",
                   "rehearsal-reading.json": "4cdf1a1179c0d58f048d091e0a719951cb3af38c822d49a2e9343bea5f502d1f"}
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
LIVE_S = 60                  # a directory born this soon after a claude process started is that process's

# ---- the audit hook: TZ-29 section 2's reads and writes ------------------------------------------------

MODE = [None]
REFUSED = []
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC


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
    """None where TZ-29 section 2 allows the event in this mode; otherwise the reason it is refused."""
    p = _path(args[0]) if args else None
    if p is None:
        return None
    if event in ("os.listdir", "os.scandir"):
        if any(_under(p, r) for r in CAPTURE_ROOTS + (ARCHIVE_STATE,)):
            return "a listing under a capture root or the archive's state"
        return None
    w = _writing(args[1] if len(args) > 1 else None, args[2] if len(args) > 2 else None)
    if any(_under(p, r) for r in CAPTURE_ROOTS):
        return "an open under a capture root"
    if _under(p, ARCHIVE_STATE):
        return None if mode == "archive" and p == ARCHIVE_LEDGER and not w else "an open under the archive's state"
    if _under(p, FORENSICS) and w:
        ex = _exclusive(args[1] if len(args) > 1 else None, args[2] if len(args) > 2 else None)
        return None if mode == "reclaim" and ex else "a write into the forensic store"
    if w and not _under(p, WORK):
        return "a write outside the work tree"
    return None


def _audit(event, args):
    if event not in ("open", "os.listdir", "os.scandir"):
        return
    why = policy(MODE[0], event, args)
    if why is not None:
        REFUSED.append((event, str(args[0]) if args else ""))
        raise GuardError("%s refused in mode %s, %s: %r" % (event, MODE[0], why, args[0] if args else None))


sys.addaudithook(_audit)

# ---- small helpers ----------------------------------------------------------------------------------------


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh, parse_float=D)


def load_state():
    return load_json(STATE) if os.path.exists(STATE) else {}


def save_state(st):
    tz23.write_atomic(STATE, (json.dumps(st, sort_keys=True, indent=1, default=tz23._dec) + "\n").encode("utf-8"))


def floor_check():
    """Before a mode that reads the venue or a set: glibc's two settings, and the memory floor."""
    assert tz23.MALLOC_TUNED, "BLOCKED: glibc did not take the mmap threshold and the arena count"
    avail = tz23.mem_available()
    out("MemAvailable %d bytes, floor %d" % (avail, MEM_FLOOR))
    assert avail >= MEM_FLOOR, "BLOCKED: MemAvailable %d bytes, below %d" % (avail, MEM_FLOOR)


def show(unit, props):
    """systemctl show, every stamp printed in UTC and the C locale."""
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


def groups_of(s):
    return [[(m["t0"], m["doc"]) for m in s["members"][i:i + tz23.CHUNK]]
            for i in range(0, len(s["members"]), tz23.CHUNK)]

# ---- the clock: the pair book's idle stretch and the archive's run -------------------------------------------


def archive_state():
    cp = subprocess.run(["systemctl", "is-active", ARCHIVE_UNIT], capture_output=True, text=True)
    return cp.stdout.strip()


def quiet(now, budget, state_of=archive_state):
    """None where a request of `budget` seconds may start at `now`; otherwise why it may not: it must start inside
    the pair book's idle stretch and end by its second 590, and never near or during the archive's run."""
    p = int(now) % WINDOW_S
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
    """Until a request of `budget` seconds may start; returns that instant and the seconds waited. A hold longer
    than HOLD_MAX_S - an archive's run that does not end - is BLOCKED."""
    t0 = clock()
    while True:
        now = clock()
        why = quiet(now, budget, state_of)
        if why is None:
            return now, now - t0
        assert now - t0 <= HOLD_MAX_S, "BLOCKED: held %.0f s, the last reason %s" % (now - t0, why)
        sleep(5.0)


def walk(base, start, spans, need, form=None, holdf=hold, sleep=time.sleep):
    """TZ-23's form_set, started inside the idle stretch; a walk stopped on a market too recent to be resolved is
    walked again WALK_RETRY_S later, and any other stop is final."""
    form = form or tz23.form_set
    for k in range(WALK_TRIES):
        if not os.path.exists(os.path.join(base, "set.json")):
            t, _w = holdf(CHUNK_BUDGET_S)
            out("the walk starts at second %d of window %d" % (int(t) % WINDOW_S, int(t) // WINDOW_S * WINDOW_S))
        try:
            return form(base, start, spans, need)
        except AssertionError as e:
            if "too recent to be resolved" not in str(e) or k == WALK_TRIES - 1:
                raise
            out("the walk stopped (%s); walked again in %d s, %d of %d" % (e, WALK_RETRY_S, k + 1, WALK_TRIES - 1))
            sleep(WALK_RETRY_S)
    raise AssertionError("unreachable")


def fetch_held(base, s, timing, budget_s=FETCH_BUDGET_S, fetcher=None, holdf=hold, clock=time.time):
    """TZ-23's fetch_fills with each chunk held: every chunk not already in the cache is fetched by TZ-23's
    fetch_chunk, started where holdf allows, and its start and end are written to `timing`."""
    fetcher = fetcher or tz23.fetch_chunk
    cache = os.path.join(base, "cache")
    os.makedirs(cache, exist_ok=True)
    groups = groups_of(s)

    def one(group):
        if os.path.exists(tz23.chunk_path(cache, group[0][0])):
            return tz23.chunk_path(cache, group[0][0]), False, None
        start, waited = holdf(CHUNK_BUDGET_S)
        path, new = fetcher(cache, group)
        return path, new, {"first": group[0][0], "start_ns": int(start * 1e9), "end_ns": int(clock() * 1e9),
                           "waited_s": round(waited, 3)}

    t, done, fresh, busy = clock(), 0, 0, 0.0
    with concurrent.futures.ThreadPoolExecutor(max_workers=tz23.FETCH_WORKERS) as pool:
        futs = [pool.submit(one, g) for g in groups]
        try:
            for fut in futs:
                _path, new, rec = fut.result()
                done += 1
                if new:
                    fresh += 1
                    busy += (rec["end_ns"] - rec["start_ns"]) / 1e9
                    w = rec["start_ns"] // 10 ** 9 // WINDOW_S * WINDOW_S
                    rec.update({"window": w, "start_second": rec["start_ns"] / 1e9 - w,
                                "end_second": rec["end_ns"] / 1e9 - w,
                                "inside": rec["end_ns"] <= (w + IDLE[1]) * 10 ** 9})
                    with open(timing, "a", encoding="utf-8") as fh:
                        fh.write(json.dumps(rec, sort_keys=True) + "\n")
                    if fresh == 30:
                        proj = busy / fresh * len(groups) / tz23.FETCH_WORKERS
                        out("projected %.0f s of fetching for %d chunks after %d fetched; %.0f s of wall clock so "
                            "far" % (proj, len(groups), fresh, clock() - t))
                        assert proj <= budget_s, "BLOCKED: fetching projected at %.0f s, above %d" % (proj, budget_s)
                if done % 25 == 0 or done == len(groups):
                    out("chunks %d of %d, %.0f s" % (done, len(groups), clock() - t))
        except BaseException:
            for f in futs:
                f.cancel()
            raise
    return cache, groups


def timing_summary(path):
    """Every chunk fetched fresh: its start and end against the idle stretch of the window it started in."""
    recs = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            recs = [json.loads(ln) for ln in fh if ln.strip()]
    outside = [r for r in recs if not r["inside"]]
    if recs:
        out("chunks fetched fresh %d: inside the idle stretch %d, ending after second %d %d; longest %.1f s; "
            "waited %.0f s; windows %d, from %s to %s" % (
                len(recs), len(recs) - len(outside), IDLE[1], len(outside),
                max((r["end_ns"] - r["start_ns"]) / 1e9 for r in recs), sum(r["waited_s"] for r in recs),
                len({r["window"] for r in recs}), utc(min(r["window"] for r in recs)),
                utc(max(r["window"] for r in recs))))
    for r in outside:
        out("chunk %d started at second %.1f of window %d and ended at second %.1f" % (
            r["first"], r["start_second"], r["window"], r["end_second"]))
    return recs, outside

# ---- the first look, from the forensic store --------------------------------------------------------------


def verify_first(first=None):
    """The first look's six files in the forensic store, each its size and SHA-256 by TZ-23's report."""
    first = first or FIRST
    for key in sorted(first):
        path, nbytes, sha = first[key]
        got = (os.path.getsize(path), tz23.sha256_file(path))
        assert got == (nbytes, sha), "the first look's %s %s: %r, TZ-23's %r" % (key, path, got, (nbytes, sha))
        out("first look %-9s %s %d bytes sha256 %s equal" % (key, path, nbytes, sha))
    return len(first)


def first_look(first=None, figures=None):
    """The first look's set and constants, asserted on TZ-23's figures."""
    first, figures = first or FIRST, figures or FIRST_FIGURES
    s1, c1 = load_json(first["set"][0]), load_json(first["constants"][0])
    t1 = [m["t0"] for m in s1["members"]]
    assert len(t1) == figures["members"] and t1[0] == figures["first"] and t1[-1] == figures["last"], \
        "the first look's set: %d members, %r to %r" % (len(t1), t1[:1], t1[-1:])
    assert c1["member_list_sha"] == figures["member_list_sha"] == tz23.sha256_bytes(
        ("\n".join(map(str, t1)) + "\n").encode()), "the first look's member list"
    assert D(c1["gate"]["V"]) == figures["V"] and D(c1["gate"]["sh"]) == figures["sh"], "the first look's V and Sh"
    return s1, c1


def replay(base, first=None, figures=None):
    """G-REPLAY: TZ-23's score of the first look, run again on the forensic store's set, members and constants;
    its two outputs must be the store's, byte for byte, and its figures TZ-23's. The copies are removed after."""
    first, figures = first or FIRST, figures or FIRST_FIGURES
    s1, c1 = first_look(first, figures)
    os.makedirs(base, exist_ok=True)
    assert not os.listdir(base), "replay: %s is not empty" % base
    members = os.path.join(base, "tz23-members.csv")
    with open(first["members"][0], "rb") as src, open(members, "xb") as dst:
        shutil.copyfileobj(src, dst, 1 << 20)
    res = tz23.score(base, s1, c1, "tz23")
    checks = {}
    for key, name in (("scored", "tz23-scored.csv"), ("reading", "tz23-reading.json")):
        got = tz23.sha256_file(os.path.join(base, name))
        checks["%s equal to the store's" % name] = got == first[key][2]
        out("G-REPLAY %-18s sha256 %s, the store's %s" % (name, got, first[key][2]))
    checks["S equal to TZ-23's"] = res["S"] == figures["S"]
    checks["Up outcomes equal to TZ-23's"] = res["ups"] == figures["ups"]
    checks["reading equal to TZ-23's"] = res["reading"] == figures["reading"]
    for k, v in checks.items():
        out("G-REPLAY %-34s %s" % (k, v))
    for name in ("tz23-members.csv", "tz23-scored.csv", "tz23-reading.json"):
        os.remove(os.path.join(base, name))
    os.rmdir(base)
    return checks

# ---- the sum over both looks ------------------------------------------------------------------------------


def cumulative(cbase, c1, members1, s2, const2, members2):
    """Both looks as one sum: the members file is the first look's rows, then the second's, under the header both
    carry; V and Sh are the two looks' sums added; the thresholds and the power are TZ-23's gate_constants on them.
    Label-free: no outcome is read."""
    with open(members1, "rb") as fh:
        m1 = fh.read()
    with open(members2, "rb") as fh:
        m2 = fh.read()
    h1, rows1 = m1.split(b"\n", 1)
    h2, rows2 = m2.split(b"\n", 1)
    assert h1 == h2 == ",".join(tz23.COLS).encode("utf-8"), "the two members files' headers"
    t1 = [int(ln.split(b",", 1)[0]) for ln in rows1.split(b"\n") if ln]
    t2 = [int(ln.split(b",", 1)[0]) for ln in rows2.split(b"\n") if ln]
    assert t2 == [m["t0"] for m in s2["members"]] and t1 and t2 and t1[-1] < t2[0], "the two looks' order"
    body = h1 + b"\n" + rows1 + rows2
    assert body.count(b"\n") == 1 + len(t1) + len(t2), "the cumulative members file's lines"
    os.makedirs(cbase, exist_ok=True)
    msha = tz23.write_once(os.path.join(cbase, "cumulative-members.csv"), body)
    V = D(c1["gate"]["V"]) + D(const2["gate"]["V"])
    sh = D(c1["gate"]["sh"]) + D(const2["gate"]["sh"])
    t0s = t1 + t2
    look = lambda c, msh: {"members": c["members"], "first": c["first"], "last": c["last"],
                           "member_list_sha": c["member_list_sha"], "members_csv_sha": msh,
                           "fills_sha": c["fills_sha"], "considered": c["considered"],
                           "non_members": c["non_members"], "weekend_members": c["weekend_members"],
                           "V": D(c["gate"]["V"]), "sh": D(c["gate"]["sh"]), "window": c["totals"]["win"]}
    const = {"label": "cumulative", "members": len(t0s), "first": t0s[0], "last": t0s[-1],
             "member_list_sha": tz23.sha256_bytes(("\n".join(map(str, t0s)) + "\n").encode()),
             "looks": {"first": look(c1, tz23.sha256_bytes(m1)), "second": look(const2, tz23.sha256_bytes(m2))},
             "gate": tz23.gate_constants(V, sh), "members_csv_sha": msha}
    csha = tz23.write_once(os.path.join(cbase, "cumulative-constants.json"), dumps(const).encode("utf-8"))
    return const, msha, csha


def show_cumulative(const, msha, csha):
    g, f, s = const["gate"], const["looks"]["first"], const["looks"]["second"]
    for name, lk in (("first", f), ("second", s)):
        w = lk["window"]
        out("%s look: members %d, %d to %d, considered %d, non-members %d, weekend %d; window fills %d, shares %s, "
            "X %s, C %s, R %s; V %s" % (name, lk["members"], lk["first"], lk["last"], lk["considered"],
                                       len(lk["non_members"]), lk["weekend_members"], w["n"], fx(D(w["sh"])),
                                       fx(D(w["X"])), fx(D(w["C"])), fx(D(w["R"])), fx(lk["V"])))
    out("both looks: members %d, %d to %d, member list sha %s" % (const["members"], const["first"], const["last"],
                                                                   const["member_list_sha"]))
    out("both looks: V %s; Sh %s; lambda %s; L %s" % (fx(g["V"]), fx(g["sh"]), fx(g["lambda"]), fx(g["L"])))
    out("EARN at S >= %s (%s a share); NO EARN at S <= %s (%s a share)" % (
        fx(g["earn_at"]), fx(g["thr_per_share"]), fx(g["no_earn_at"]), fx(g["no_earn_per_share"])))
    out("power of either answer against the other's alternative, normal, variance V/4: %s" % fx(g["power"]))
    out("2 thr / Sh %s against delta %s: %s" % (fx(2 * g["thr_per_share"]), fx(g["delta"]),
                                                "UNDECIDABLE cannot occur" if 2 * g["thr_per_share"] <= g["delta"]
                                                else "UNDECIDABLE can occur"))
    out("wrote cumulative-members.csv sha256 %s and cumulative-constants.json sha256 %s" % (msha, csha))

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
        h = tz23.sha256_file(os.path.join(PRIMARY, rel))[:12]
        assert h == ANCHORS[k], "re-derived %s %s, the map %s" % (k, h, ANCHORS[k])
        out("re-derived %s %s sha256[:12] %s equal" % (k, rel, h))
    rows = ROW.findall(txt)
    states = {k: sum(1 for r in rows if r[3] == k) for k in MAP_ROWS}
    assert states == MAP_ROWS and len(rows) == sum(MAP_ROWS.values()), "rows %r" % states
    for path, lines, nbytes, state, sha in rows:
        with open(os.path.join(PRIMARY, path), "rb") as fh:
            blob = fh.read()
        got = (blob.count(b"\n"), len(blob), tz23.sha256_bytes(blob))
        if state == "frozen":
            want = (int(lines.replace(",", "")), int(nbytes.replace(",", "")), sha)
            assert got == want, "frozen row %s: %r, the map %r" % (path, got, want)
        out("%-44s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), tz23.sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"],
                         states["reported"]))


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
        st["still"] = {"at": utc(time.time()), "units": now}
        save_state(st)
        out("still: recorded")
        return
    same = now == st["still"]["units"]
    out("G-STILL %s: %s since %s" % ("PASS" if same else "FAIL", "unchanged" if same else "changed",
                                     st["still"]["at"]))


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


def ledger_summary(recs):
    """The archive's runs, from its own records: each run's events, its set, its terminal record and whether it
    began on the calendar; whether the archive is halted. Pure: it reads nothing but `recs`."""
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
        last = lambda name: [r for r in rs if r.get("event") == name][-1:]
        sec = a % 86400 if isinstance(a, int) else None
        when = "calendar" if sec == ARCHIVE_CALENDAR_S else ("off-calendar, second %s of the day" % sec)
        parts = ["run %s %s, %s: %d records %s; terminal %s" % (a, utc(a) if isinstance(a, int) else "-", when,
                                                                len(rs), ev, term[-1] if term else "none")]
        for r in last("set"):
            parts.append("set %s: %s files, %s bytes, windows %s to %s of %s considered" % (
                r.get("tag"), r.get("assets_n"), r.get("bytes_total"), r.get("first_T"), r.get("last_T"),
                r.get("windows_considered")))
        for r in last("upload"):
            parts.append("Release %s: sent %s, held %s" % (r.get("release_id"), r.get("sent"), r.get("held")))
        for r in last("delete"):
            parts.append("removed %s, freed %s bytes, free after %s" % (r.get("removed"), r.get("freed"),
                                                                       r.get("free_after")))
        for r in last("restart"):
            parts.append("restart: window %s, pid %s after %s, NRestarts %s" % (r.get("W"), r.get("pid"),
                                                                              r.get("stopped"), r.get("NRestarts")))
        for r in last("resume"):
            parts.append("resume %s at window %s" % (r.get("reading"), r.get("T")))
        for r in last("complete"):
            parts.append("complete: requests %s, started outside %s, ended outside %s, store %s bytes, free %s, "
                         "rate %s a day" % (r.get("requests"), r.get("started_outside"), r.get("ended_outside"),
                                            r.get("store_stream_bytes"), r.get("free_bytes"), r.get("rate_per_day")))
        for r in rs:
            if r.get("event") in ("deferred", "halt", "refused", "timer-disabled"):
                parts.append("%s in %s: %s" % (r.get("event"), r.get("phase"), r.get("reason", r.get("exit"))))
        lines.append("; ".join(parts))
    flags = [r.get("event") for r in recs if r.get("event") in ("halt", "clear")]
    sets = [r for r in recs if r.get("event") == "set"]
    gaps = [[p.get("last_T"), q.get("first_T")] for p, q in zip(sets, sets[1:])
            if isinstance(p.get("last_T"), int) and q.get("first_T") != p["last_T"] + 900]
    return {"runs": order, "lines": lines, "halted": bool(flags) and flags[-1] == "halt",
            "terminal": {a: [r.get("event") for r in runs[a] if r.get("event") in ("complete", "empty", "halt")]
                         for a in order},
            "tags": [r.get("tag") for r in sets], "assets": sum(r.get("assets_n") or 0 for r in sets),
            "bytes": sum(r.get("bytes_total") or 0 for r in sets), "gaps": gaps}


def mode_archive():
    """The archive's own record, read whole: its complete lines, each printed, and its runs summarized."""
    for unit in (ARCHIVE_TIMER, ARCHIVE_UNIT):
        out("%s %s" % (unit, show(unit, ["ActiveState", "SubState", "UnitFileState", "Result", "ExecMainStatus",
                                         "LastTriggerUSec", "NextElapseUSecRealtime"])))
    with open(ARCHIVE_LEDGER, "rb") as fh:
        raw = fh.read()
    lines = raw.split(b"\n")
    tail = lines.pop()
    recs = [json.loads(ln) for ln in lines if ln.strip()]
    out("ledger %s: %d bytes sha256 %s, %d complete records, %d bytes of a line still written" % (
        ARCHIVE_LEDGER, len(raw), tz23.sha256_bytes(raw), len(recs), len(tail)))
    for r in recs:
        out("L %s %s" % (utc(r["wall_ns"] / 1e9), json.dumps(r, sort_keys=True)))
    summ = ledger_summary(recs)
    for ln in summ["lines"]:
        out(ln)
    tags = sorted(ln.split("\t")[1][len("refs/tags/"):] for ln in git(
        "ls-remote", "origin", "refs/tags/pairbook-streams-*", tree=PRIMARY).split("\n") if "\t" in ln)
    out("tags on origin %d: %s" % (len(tags), tags))
    out("the ledger's sets %d, %d files, %d bytes; their tags not on origin %s; tags on origin without a set %s" % (
        len(summ["tags"]), summ["assets"], summ["bytes"], sorted(set(summ["tags"]) - set(tags)),
        sorted(set(tags) - set(summ["tags"]))))
    out("runs %d; without a terminal record %s; windows skipped between consecutive sets %s; halted %s" % (
        len(summ["runs"]), [a for a, t in summ["terminal"].items() if not t], summ["gaps"], summ["halted"]))


def mode_rehearse():
    floor_check()
    base = os.path.join(WORK, "rehearsal")
    s = walk(base, tz23.REHEARSAL[0], (), tz23.REHEARSAL[1])
    assert len(s["members"]) == tz23.REF["members"] and len(s["considered"]) == tz23.REF["members"], \
        "G-REHEARSAL: %d members of %d considered" % (len(s["members"]), len(s["considered"]))
    cache, groups = fetch_held(base, s, os.path.join(base, "rehearsal-timing.jsonl"), budget_s=10 ** 9)
    timing_summary(os.path.join(base, "rehearsal-timing.jsonl"))
    const, paths = tz23.build_constants(base, s, cache, groups, "rehearsal")
    tz23.show_constants(const, paths)
    res = tz23.score(base, s, const, "rehearsal")
    w = const["totals"]["win"]
    got = {"members": const["members"], "ups": res["ups"], "n": w["n"], "sh": w["sh"], "X": w["X"], "C": w["C"],
           "R": w["R"], "V": const["gate"]["V"], "XU": res["XU"], "S": res["S"]}
    checks = {}
    for k in tz23.REF:
        checks["figure " + k] = got[k] == tz23.REF[k]
        out("G-REHEARSAL %-7s instrument %s, the Architect's %s, %s" % (k, got[k], tz23.REF[k],
                                                                       "equal" if got[k] == tz23.REF[k] else
                                                                       "DIFFERENT"))
    for name, want in sorted(REHEARSAL_FILES.items()):
        h = tz23.sha256_file(os.path.join(base, name))
        checks["file " + name] = h == want
        out("G-REHEARSAL %-24s sha256 %s, TZ-23's %s, %s" % (name, h, want, "equal" if h == want else "DIFFERENT"))
    bad = sorted(k for k, v in checks.items() if not v)
    assert not bad, "G-REHEARSAL FAIL: %s" % bad
    out("G-REHEARSAL PASS: %d of %d - %d figures and %d files equal to TZ-23's" % (
        len(checks), len(checks), len(tz23.REF), len(REHEARSAL_FILES)))


def mode_replay():
    floor_check()
    verify_first()
    checks = replay(os.path.join(WORK, "replay"))
    bad = sorted(k for k, v in checks.items() if not v)
    assert not bad, "G-REPLAY FAIL: %s" % bad
    out("G-REPLAY PASS: 6 of 6 stored files equal, %d of %d checks" % (len(checks), len(checks)))


def second_set():
    base = os.path.join(WORK, "set")
    s = load_json(os.path.join(base, "set.json"))
    return base, s, os.path.join(base, "cache"), groups_of(s)


def mode_fetch():
    now = time.time()
    assert now >= START_AT, "BLOCKED: %s is before %s, TZ-29's instant" % (utc(now), utc(START_AT))
    floor_check()
    base = os.path.join(WORK, "set")
    os.makedirs(base, exist_ok=True)
    s = walk(base, START2, tz23.EXCLUDED, N_SET)
    t0s = [m["t0"] for m in s["members"]]
    assert s["start"] == START2 and s["need"] == N_SET and len(t0s) == N_SET, "G-SET: %d members" % len(t0s)
    assert s["considered"][0][0] == START2 and t0s[0] > LAST_FIRST, "G-SET: the walk did not start at %d" % START2
    cache, groups = fetch_held(base, s, os.path.join(base, "fetch-timing.jsonl"))
    n = sum(1 for _ in tz23.member_rows(cache, groups))
    assert n == N_SET, "G-SET: %d members read back" % n
    timing_summary(os.path.join(base, "fetch-timing.jsonl"))
    out("G-SET PASS: %d members, %d considered, %d to %d, %d chunks, every chunk read back" % (
        N_SET, len(s["considered"]), t0s[0], t0s[-1], len(groups)))


def mode_constants():
    floor_check()
    verify_first()
    s1, c1 = first_look()
    base, s2, cache, groups = second_set()
    assert len(s2["members"]) == N_SET and s2["start"] == START2, "the second set"
    const2, paths2 = tz23.build_constants(base, s2, cache, groups, "tz29")
    tz23.show_constants(const2, paths2)
    const, msha, csha = cumulative(os.path.join(WORK, "cumulative"), c1, FIRST["members"][0], s2, const2,
                                   paths2["members.csv"][0])
    show_cumulative(const, msha, csha)
    st = load_state()
    st["constants_sha"], st["constants_at"] = csha, utc(time.time())
    save_state(st)


def mode_score():
    floor_check()
    verify_first()
    s1, _c1 = first_look()
    _base, s2, _cache, _groups = second_set()
    cbase = os.path.join(WORK, "cumulative")
    cpath = os.path.join(cbase, "cumulative-constants.json")
    st = load_state()
    assert tz23.sha256_file(cpath) == st.get("constants_sha"), "score: not the constants recorded"
    head = git("rev-parse", "HEAD")
    assert "origin/" + BRANCH in git("branch", "-r", "--contains", head).split(), \
        "score: HEAD %s is not on origin" % head
    const = load_json(cpath)
    s = {"members": s1["members"] + s2["members"]}
    t0s = [m["t0"] for m in s["members"]]
    assert tz23.sha256_bytes(("\n".join(map(str, t0s)) + "\n").encode()) == const["member_list_sha"], \
        "score: the members are not the constants' members"
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(dumps({"at": utc(time.time()), "head": head, "members": const["members"],
                        "member_list_sha": const["member_list_sha"]}))
    res = tz23.score(cbase, s, const, "cumulative")
    with open(os.path.join(cbase, "cumulative-scored.csv"), "rb") as fh:
        scored = fh.read().split(b"\n")
    with open(FIRST["scored"][0], "rb") as fh:
        first_scored = fh.read().split(b"\n")
    assert scored[:N_SET + 1] == first_scored[:N_SET + 1], "score: the first look's rows are not TZ-23's"
    out("the first look's %d rows of the scored file equal TZ-23's, byte for byte" % N_SET)
    r1 = load_json(FIRST["reading"][0])
    S1, P1, R1, U1 = D(r1["S"]), D(r1["P"]), D(r1["R"]), r1["ups"]
    sh2 = D(const["looks"]["second"]["sh"])
    S2, P2, R2 = res["S"] - S1, res["P"] - P1, res["R"] - R1
    out("the first look, TZ-23's: S %s = settlement %s + rebate %s, %d Up" % (fx(S1), fx(P1), fx(R1), U1))
    out("the second look, by difference, barred from every reading: S %s = settlement %s + rebate %s, %d Up; "
        "per share %s = %s + %s" % (fx(S2), fx(P2), fx(R2), res["ups"] - U1, fx(S2 / sh2), fx(P2 / sh2),
                                    fx(R2 / sh2)))
    if res["earn"] and res["no_earn"]:
        out("both bounds hold: the reading is EARN, and half a tick a share is rejected too (TZ-23 section 4.3)")
    out("M0 READING, OVER BOTH LOOKS: %s" % res["reading"])


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
                h = tz23.sha256_file(path)
                is_named = any(h[:k] in tokens for k in lengths)
                is_kept = by_name(tree, rel)
                if not (is_named or is_kept):
                    continue
                named += 1 if is_named else 0
                kept += 1 if is_kept and not is_named else 0
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--" + rel.replace("/", "--"))
                if os.path.exists(dest):
                    got = tz23.sha256_file(dest)
                    assert got == h, "reclaim: %s exists with sha256 %s, source %s" % (dest, got, h)
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert tz23.sha256_file(dest) == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, %d already held; "
        "forensic store %d -> %d files" % (considered, named, kept, copied, held, before, after))

# ---- the self-test: literals and temporary trees under the work tree -----------------------------------------


def mode_selftest():
    import random
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    # TZ-23's file, as loaded, and the constants this file takes from it
    ok(tz23.__file__ == os.path.join(HERE, TZ23_NAME) and sys.modules["tz23"] is tz23,
       "TZ-23's instrument loaded from beside this file, from its asserted bytes")
    ok(tz23.MALLOC_TUNED, "glibc took the 128 KiB mmap threshold and the two arenas")
    ok(tz23.getcontext().prec == 60, "the main thread sums at 60 digits")
    ok((tz23.N_SET, tz23.STEP, tz23.CHUNK, tz23.RESOLVED_AFTER_S, tz23.WALK_SLACK, tz23.FETCH_WORKERS) ==
       (N_SET, 300, 20, 3900, 2016, 2), "TZ-23's set size, step, chunk, resolution age, slack and workers")
    ok((tz23.ALPHA, tz23.DELTA, tz23.LAMBDA) == (D("0.005"), D("0.005"), D("0.000021932")),
       "TZ-23's alpha, delta and lambda, the second look's by TZ-23 section 1")
    ok(tz23.HEADERS == {"User-Agent": "btc-5m-twap-m0/TZ-23", "Accept": "application/json"},
       "every request carries TZ-23's two headers")
    # the second look's set, its walk and its instant
    ok(START2 == 1791242100 and utc(START2) == "2026-10-05T23:15:00Z", "the walk starts at 2026-10-05 23:15 UTC")
    ok(START_AT == 1792455300 and utc(START_AT) == "2026-10-20T00:15:00Z" and
       START_AT == START2 + (N_SET - 1) * tz23.STEP + tz23.RESOLVED_AFTER_S,
       "no set is read before 2026-10-20 00:15 UTC, the 4,032nd member's resolution age")
    ok(tz23.next_open(START2, tz23.EXCLUDED) == START2 and not tz23.excluded(START2, tz23.EXCLUDED),
       "no excluded span reaches the second look")
    good = {"slug": "", "outcomes": '["Up", "Down"]', "outcomePrices": '["1", "0"]', "closed": True,
            "feeType": tz23.FEE_TYPE, "feeSchedule": dict(tz23.FEE_SCHEDULE), "eventStartTime": "",
            "conditionId": "0x" + "cd" * 32, "clobTokenIds": '["11", "22"]'}

    def fake_docs(t0s, asked=None):
        if asked is not None:
            asked.extend(t0s)
        return {"btc-updown-5m-%d" % t: dict(good, slug="btc-updown-5m-%d" % t, eventStartTime=tz23.iso(t))
                for t in t0s}

    ok(START2 + (N_SET - 1) * tz23.STEP == 1792451400 and utc(1792451400) == "2026-10-19T23:10:00Z",
       "every candidate qualifying, the 4,032nd member is 1792451400, 2026-10-19 23:10 UTC")
    asked = []
    cons, mem = tz23.candidates(START2, tz23.EXCLUDED, 50, lambda ts: fake_docs(ts, asked))
    ok(len(mem) == 50 and mem[0][0] == START2 and mem[-1][0] == START2 + 49 * 300 and len(cons) == 50 and
       len(asked) == 50, "TZ-23's walk from 1791242100 takes 50 qualifying members in 50 documents")
    ok(asked == [t for t, _st in cons] and min(asked) > LAST_FIRST,
       "the walk requests no document at or below 1791241800 and none after the need-th member")
    ok(tz23.segments([t for t, _d in mem]) == {"3": 50}, "every second-look member reads segment 3")
    # the walk again, 300 s later, on a market too recent to be resolved; any other stop is final
    calls, slept = [], []

    def form_stops(times, msg):
        def form(base, start, spans, need):
            calls.append(start)
            if len(calls) <= times:
                raise AssertionError(msg)
            return {"start": start}
        return form

    r = walk("/nonexistent", START2, (), N_SET, form=form_stops(2, "BLOCKED: the walk reached x, too recent to "
                                                                   "be resolved"),
             holdf=lambda b: (0, 0), sleep=slept.append)
    ok(r == {"start": START2} and len(calls) == 3 and slept == [WALK_RETRY_S, WALK_RETRY_S],
       "a walk stopped twice on a market too recent is walked a third time, 300 s after each stop")
    calls.clear()
    try:
        walk("/nonexistent", START2, (), N_SET, form=form_stops(1, "BLOCKED: 6049 considered for 4031 members"),
             holdf=lambda b: (0, 0), sleep=slept.append)
        stopped = False
    except AssertionError:
        stopped = True
    ok(stopped and len(calls) == 1, "a walk stopped on its slack is not walked again")
    # the clock: the idle stretch, the archive's calendar run and its service
    W = 1792458000
    idle = lambda st="inactive": (lambda: st)
    ok(quiet(W + 14, CHUNK_BUDGET_S, idle()) is not None and quiet(W + 15, CHUNK_BUDGET_S, idle()) is None and
       quiet(W + 470, CHUNK_BUDGET_S, idle()) is None and quiet(W + 471, CHUNK_BUDGET_S, idle()) is not None,
       "a chunk starts from second 15 to 470 of a window and at no other second")
    ok(quiet(W + 600, CHUNK_BUDGET_S, idle()) is not None and quiet(W + 899, CHUNK_BUDGET_S, idle()) is not None,
       "nothing starts while the pair book streams, seconds 595 to 905")
    cal = W // 86400 * 86400 + ARCHIVE_CALENDAR_S
    ok(cal % WINDOW_S == 20, "the archive's calendar run is at second 20 of its window")
    ok(quiet(cal - 5, CHUNK_BUDGET_S, idle()) is not None and quiet(cal + 40, CHUNK_BUDGET_S, idle()) is not None
       and quiet(cal + 61, CHUNK_BUDGET_S, idle()) is None,
       "nothing starts from 03:00:15 to 03:01:20 UTC; at 03:01:21 a chunk may start")
    ok(all(quiet(W + 100, CHUNK_BUDGET_S, idle(st)) is not None for st in RUNNING) and
       quiet(W + 100, CHUNK_BUDGET_S, idle("failed")) is None,
       "nothing starts while the archive's service runs; a failed one does not hold")
    clock = [W + 600.25]
    t, waited = hold(CHUNK_BUDGET_S, clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s),
                     state_of=idle())
    ok(int(t) % WINDOW_S == 15 and int(t) == W + 900 + 15 and 314 <= waited <= 320,
       "held from second 600, a chunk starts at second 15 of the next window")
    clock = [W + 100.0]
    try:
        hold(CHUNK_BUDGET_S, clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s),
             state_of=idle("activating"))
        stuck = False
    except AssertionError as e:
        stuck = "BLOCKED: held" in str(e) and clock[0] - (W + 100) <= HOLD_MAX_S + 5
    ok(stuck, "an archive's run that never ends holds a chunk 7,200 s and then stops it BLOCKED")
    # the fetch, held, on a fake chunk fetcher: each fresh chunk timed, a cached chunk fetched again by nothing
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    try:
        os.makedirs(tmp)
        s = {"members": [{"t0": START2 + 300 * i, "doc": dict(good, conditionId="0x%064x" % (i + 1))}
                         for i in range(45)]}
        fetched = []

        def fake_fetch(cache, group):
            fetched.append(group[0][0])
            path = tz23.chunk_path(cache, group[0][0])
            tz23.write_atomic(path, tz23.gz_bytes(dumps({"members": [
                {"t0": t, "condition": d["conditionId"], "rows": []} for t, d in group]})))
            return path, True

        timing = os.path.join(tmp, "timing.jsonl")
        clk = [float(W + 20)]
        cache, groups = fetch_held(tmp, s, timing, fetcher=fake_fetch, holdf=lambda b: (clk[0], 0.0),
                                   clock=lambda: clk[0])
        recs, outside = timing_summary(timing)
        ok(len(groups) == 3 and sorted(fetched) == [START2, START2 + 6000, START2 + 12000] and len(recs) == 3
           and not outside, "45 members are 3 chunks, each fetched once and timed inside the idle stretch")
        fetched.clear()
        fetch_held(tmp, s, timing, fetcher=fake_fetch, holdf=lambda b: (clk[0], 0.0), clock=lambda: clk[0])
        ok(fetched == [] and len(timing_summary(timing)[0]) == 3, "a cached chunk is fetched again by nothing")
        ok(sum(1 for _ in tz23.member_rows(cache, groups)) == 45, "every chunk reads back to its members")
        big = {"members": [{"t0": START2 + 300 * i, "doc": dict(good, conditionId="0x%064x" % (i + 1))}
                           for i in range(800)]}

        import threading
        gate = threading.Event()

        def slow_fetch(step, held_from=None):
            def f(cache, group):
                if held_from is not None and (group[0][0] - START2) // 6000 >= held_from:
                    gate.wait(30)
                clk[0] += step
                return fake_fetch(cache, group)
            return f

        fetched.clear()
        threading.Timer(5.0, gate.set).start()
        try:
            fetch_held(os.path.join(tmp, "slow"), big, os.path.join(tmp, "slow.jsonl"),
                       fetcher=slow_fetch(1000.0, held_from=32), holdf=lambda b: (clk[0], 0.0), clock=lambda: clk[0])
            blocked = False
        except AssertionError as e:
            blocked = "BLOCKED: fetching projected" in str(e)
        ok(blocked and 32 <= len(fetched) <= 34, "a fetch projected above 7,200 s of fetching stops BLOCKED at its "
                                                  "30th chunk: at most the two chunks running end, and the six "
                                                  "queued never start")
        fetched.clear()
        fetch_held(os.path.join(tmp, "fast"), big, os.path.join(tmp, "fast.jsonl"), fetcher=slow_fetch(10.0),
                   holdf=lambda b: (clk[0], 0.0), clock=lambda: clk[0])
        ok(len(fetched) == 40, "a fetch projected under it fetches all 40 chunks")
        # both looks as one sum: equal to TZ-23's build_constants over the union, the fills file aside
        rng = random.Random(29)

        def look(t0s, k):
            docs = [dict(good, slug="btc-updown-5m-%d" % t, eventStartTime=tz23.iso(t), conditionId="0x%064x" % (
                k * 1000 + i + 1), outcomePrices=('["1", "0"]' if rng.random() < 0.5 else '["0", "1"]'))
                    for i, t in enumerate(t0s)]
            rows = {t: sorted([[t + rng.randrange(-30, 330), rng.choice("BS"), rng.choice("UD"),
                                tz23.fx(D(rng.randrange(1, 500000)) / 100), tz23.fx(D(rng.randrange(1, 999)) / 1000)]
                               for _ in range(rng.randrange(0, 40))]) for t in t0s}
            return docs, rows

        def build(base, docs, rows, label):
            cache = os.path.join(base, "cache")
            os.makedirs(cache)
            st = {"start": docs[0]["eventStartTime"], "need": len(docs),
                  "considered": [[int(d["slug"].rsplit("-", 1)[1]), "member"] for d in docs],
                  "members": [{"t0": int(d["slug"].rsplit("-", 1)[1]), "doc": tz23.kept_doc(d)} for d in docs]}
            groups = groups_of(st)
            for g in groups:
                tz23.write_atomic(tz23.chunk_path(cache, g[0][0]), tz23.gz_bytes(dumps({"members": [
                    {"t0": t, "condition": d["conditionId"], "rows": rows[t]} for t, d in g]})))
            const, paths = tz23.build_constants(base, st, cache, groups, label)
            return st, const, paths

        ta = [1788530400 + 300 * i for i in range(23)]
        tb = [START2 + 300 * i for i in range(27)]
        da, ra = look(ta, 1)
        db, rb = look(tb, 2)
        sa, ca, pa = build(os.path.join(tmp, "a"), da, ra, "tz23")
        sb, cb, pb = build(os.path.join(tmp, "b"), db, rb, "tz29")
        su, cu, pu = build(os.path.join(tmp, "u"), da + db, {**ra, **rb}, "u")
        const, msha, csha = cumulative(os.path.join(tmp, "c"), ca, pa["members.csv"][0], sb, cb, pb["members.csv"][0])
        with open(pu["members.csv"][0], "rb") as fh:
            union_members = fh.read()
        ok(msha == tz23.sha256_bytes(union_members),
           "the cumulative members file is byte for byte TZ-23's build_constants over the union")
        ok(D(const["gate"]["V"]) == cu["gate"]["V"] and D(const["gate"]["sh"]) == cu["gate"]["sh"] and
           all(D(const["gate"][k]) == cu["gate"][k] for k in ("thr", "earn_at", "no_earn_at")),
           "both looks' V, Sh and thresholds equal TZ-23's build_constants over the union")
        ok(const["member_list_sha"] == cu["member_list_sha"] and const["members"] == cu["members"] == 50,
           "the cumulative member list is the union's")
        su_score = {"members": sa["members"] + sb["members"]}
        res_c = tz23.score(os.path.join(tmp, "c"), su_score, load_json(os.path.join(tmp, "c",
                                                                                    "cumulative-constants.json")),
                           "cumulative")
        res_u = tz23.score(os.path.join(tmp, "u"), su, cu, "u")
        with open(os.path.join(tmp, "c", "cumulative-scored.csv"), "rb") as fh:
            sc_c = fh.read()
        with open(os.path.join(tmp, "u", "u-scored.csv"), "rb") as fh:
            sc_u = fh.read()
        ok(sc_c == sc_u and all(res_c[k] == res_u[k] for k in ("S", "P", "R", "XU", "ups", "reading", "earn",
                                                                "no_earn")),
           "the score over both looks equals TZ-23's score over the union, file and figures")
        res_a = tz23.score(os.path.join(tmp, "a"), sa, ca, "tz23")
        with open(os.path.join(tmp, "a", "tz23-scored.csv"), "rb") as fh:
            sc_a = fh.read().split(b"\n")
        ok(sc_c.split(b"\n")[:len(ta) + 1] == sc_a[:len(ta) + 1],
           "the first look's rows of the scored file over both looks are its own scored rows")
        res_b = tz23.score(os.path.join(tmp, "b"), sb, cb, "tz29")
        ok(res_c["S"] == res_a["S"] + res_b["S"] and res_c["ups"] == res_a["ups"] + res_b["ups"],
           "S over both looks is the first look's S plus the second's, exactly")
        # label-free: the cumulative constants file with every label of both looks flipped
        flip = lambda docs: [dict(d, outcomePrices=('["0", "1"]' if d["outcomePrices"] == '["1", "0"]'
                                                    else '["1", "0"]')) for d in docs]
        sa2, ca2, pa2 = build(os.path.join(tmp, "a2"), flip(da), ra, "tz23")
        sb2, cb2, pb2 = build(os.path.join(tmp, "b2"), flip(db), rb, "tz29")
        const2, msha2, csha2 = cumulative(os.path.join(tmp, "c2"), ca2, pa2["members.csv"][0], sb2, cb2,
                                          pb2["members.csv"][0])
        ok(csha2 == csha and msha2 == msha, "the cumulative constants file is byte-identical with every label flipped")
        res_c2 = tz23.score(os.path.join(tmp, "c2"), {"members": sa2["members"] + sb2["members"]},
                            load_json(os.path.join(tmp, "c2", "cumulative-constants.json")), "cumulative")
        ok(res_c2["S"] != res_c["S"], "the score moves when the labels flip (negative control)")
        again = cumulative(os.path.join(tmp, "c"), ca, pa["members.csv"][0], sb, cb, pb["members.csv"][0])
        ok(again[1:] == (msha, csha), "a second cumulative run finds both files unchanged")
        # G-REPLAY on a store made here: a first look built and scored, then replayed from its files
        store = {"set": os.path.join(tmp, "a", "set.json"), "fills": pa["fills.jsonl.gz"][0],
                 "members": pa["members.csv"][0], "constants": pa["constants.json"][0],
                 "scored": os.path.join(tmp, "a", "tz23-scored.csv"), "reading": os.path.join(tmp, "a",
                                                                                          "tz23-reading.json")}
        with open(store["set"], "w", encoding="utf-8") as fh:
            fh.write(dumps(sa))
        first = {k: (p, os.path.getsize(p), tz23.sha256_file(p)) for k, p in store.items()}
        figures = {"members": len(ta), "ups": res_a["ups"], "first": ta[0], "last": ta[-1],
                   "member_list_sha": ca["member_list_sha"], "V": ca["gate"]["V"], "sh": ca["gate"]["sh"],
                   "S": res_a["S"], "reading": res_a["reading"]}
        ok(verify_first(first) == 6, "the store's six files verify by size and SHA-256")
        checks = replay(os.path.join(tmp, "replay"), first, figures)
        ok(all(checks.values()) and len(checks) == 5 and not os.path.exists(os.path.join(tmp, "replay")),
           "G-REPLAY passes 5 of 5 on a faithful store, and leaves no copy behind")
        with open(store["members"], "r+b") as fh:
            b0 = fh.read(1)
            fh.seek(0)
            fh.write(b"9" if b0 != b"9" else b"8")
        try:
            verify_first(first)
            caught = False
        except AssertionError:
            caught = True
        ok(caught, "a store file with one byte changed fails verify (negative control)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    # the projection, both looks at the first look's rates, against the Architect's independent 80-digit figures
    g = tz23.gate_constants(2 * FIRST_FIGURES["V"], 2 * FIRST_FIGURES["sh"])
    ok(abs(g["thr"] - D("623389.475150266978894322547225")) < D("1e-20"),
       "at twice the first look's V the threshold is 623,389.475150, the Architect's figure")
    ok(D("0.0024120") < g["thr_per_share"] < D("0.0024121") and D("0.0025879") < g["no_earn_per_share"] <
       D("0.0025880") and 2 * g["thr_per_share"] < tz23.DELTA,
       "at the first look's rates EARN needs 0.2412 c a share and NO EARN 0.2588 c: UNDECIDABLE cannot occur")
    ok(D("0.9998") < g["power"] < D("0.9999"), "the projected power is 0.99983")
    g1 = tz23.gate_constants(FIRST_FIGURES["V"], FIRST_FIGURES["sh"])
    ok(g1["earn_at"] == D("432484.391198789259040750892225374110125738788601942422313849"),
       "the first look's own EARN bound is TZ-23's, to every printed digit")
    # the archive's ledger, summarized from literal records
    recs = [{"event": "start", "run": 1792378820, "wall_ns": 1}, {"event": "set", "run": 1792378820, "wall_ns": 2,
            "tag": "pairbook-streams-1792378820", "assets_n": 96, "bytes_total": 10, "first_T": 1792291500,
            "last_T": 1792377000, "windows_considered": 96}, {"event": "complete", "run": 1792378820, "wall_ns": 3,
            "requests": 1, "started_outside": 0, "ended_outside": 0, "store_stream_bytes": 0, "free_bytes": 1,
            "rate_per_day": 1}, {"event": "start", "run": 1792045110, "wall_ns": 4},
            {"event": "set", "run": 1792045110, "wall_ns": 5, "tag": "pairbook-streams-1792045110", "assets_n": 1,
             "bytes_total": 1, "first_T": 1792378800, "last_T": 1792378800, "windows_considered": 1},
            {"event": "halt", "run": 1792045110, "wall_ns": 6, "phase": "restart", "reason": "x"}]
    summ = ledger_summary(recs)
    ok(summ["runs"] == [1792378820, 1792045110] and "calendar" in summ["lines"][0] and
       "off-calendar, second 22710" in summ["lines"][1] and summ["halted"] and
       summ["terminal"] == {1792378820: ["complete"], 1792045110: ["halt"]} and summ["assets"] == 97 and
       summ["gaps"] == [[1792377000, 1792378800]], "the ledger's runs, terminals, calendar, halt and gaps")
    ok(not ledger_summary(recs + [{"event": "clear", "run": None, "wall_ns": 7}])["halted"],
       "a clear after a halt reads not halted")
    # the fingerprint's rows, on literal lines
    lines = ("| `research/tz23-maker-m0.py` | 1,184 | 54,885 | frozen | `%s` |\n"
             "| `SYSTEM-MAP.md` | — | — | reported | self-reference; report the value you compute |\n"
             "| `A6` — pricer | `729f0bcdbee3` |\n" % TZ23_SHA256)
    ok(ROW.findall(lines) == [("research/tz23-maker-m0.py", "1,184", "54,885", "frozen", TZ23_SHA256),
                              ("SYSTEM-MAP.md", "—", "—", "reported",
                               "self-reference; report the value you compute")] and
       dict(ANCHOR_ROW.findall(lines)) == {"A6": "729f0bcdbee3"}, "the map's rows and anchors parse")
    # reclaim's paths
    ok(reclaimable(WORK) and not reclaimable(FORENSICS) and not reclaimable("/tmp/x/" + "0" * 8 + "-0000-0000-0000-"
                                                                           + "0" * 12),
       "reclaim takes the work tree and refuses the forensic store and a directory outside a session's")
    # the audit hook: section 2's refusals happen before the open
    MODE[0] = "selftest"
    refused = []
    for p in ("/var/lib/btc-pairbook/runtime.jsonl", ARCHIVE_LEDGER, "/var/lib/btc-chainbook/runtime.jsonl"):
        try:
            open(p, "rb")
            refused.append("opened")
        except GuardError:
            refused.append("tz29")
        except RuntimeError:
            refused.append("tz23")
        except OSError:
            refused.append("not refused")
    ok(refused == ["tz29", "tz29", "tz23"], "opens under the pair book's root and of the archive's ledger outside "
                                            "mode archive are refused by this hook, under the chain book's root by "
                                            "TZ-23's, each before it happens")
    try:
        open("/var/lib/btc-recorder/runtime.jsonl", "rb")
        rec_refused = False
    except RuntimeError:
        rec_refused = True
    except OSError:
        rec_refused = False
    ok(rec_refused and tz23.OPENS[-1] == "/var/lib/btc-recorder/runtime.jsonl",
       "TZ-23's own hook still refuses the recorder's root")
    tz23.OPENS.clear()
    ok(policy("archive", "open", (ARCHIVE_LEDGER, "rb", 0)) is None and
       policy("archive", "open", (ARCHIVE_LEDGER, "ab", os.O_WRONLY)) is not None and
       policy("archive", "open", (ARCHIVE_STATE + "/archive.log", "rb", 0)) is not None and
       policy("archive", "os.listdir", (ARCHIVE_STATE,)) is not None,
       "mode archive reads ledger.jsonl and nothing else of the archive's state, and writes nothing there")
    ok(policy("reclaim", "open", (FORENSICS + "/x", "xb", 0)) is None and
       policy("reclaim", "open", (FORENSICS + "/x", "wb", 0)) is not None and
       policy("score", "open", (FORENSICS + "/x", "xb", 0)) is not None and
       policy("score", "open", ("/root/elsewhere", "wb", 0)) is not None and
       policy("score", "open", (FORENSICS + "/x", "rb", 0)) is None,
       "the forensic store is written by reclaim's exclusive create alone, and nothing outside the work tree")
    del REFUSED[:]
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz29-maker-m0-second-look.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "still": mode_still,
             "archive": mode_archive, "rehearse": mode_rehearse, "replay": mode_replay, "fetch": mode_fetch,
             "constants": mode_constants, "score": mode_score}
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
