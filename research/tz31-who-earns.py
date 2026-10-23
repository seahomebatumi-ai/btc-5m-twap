#!/usr/bin/env python3
"""TZ-31 - W0, who earns: do the makers and the takers who earned most on btc-updown-5m markets M0 has read,
named before this TZ by the Architect, earn at least half a tick a share at settlement - the makers with the 20%
rebate, the takers after the fee - on the first qualifying markets no TZ has read?

    fingerprint       contract section 1 steps 3 and 4, asserted: the map's revision, anchors and rows
    selftest          every rule of this file, on literals and on temporary trees under the work tree
    still             the recorder's and the pair book's MainPID, NRestarts and ActiveState: the first run
                      records them, the second compares, the archive's own restarts read from its ledger
                      (G-STILL)
    scratch OWN       the UUID directories beside OWN, this session's, each named live or earlier
    archive           the pair book archive's ledger, read and printed, beside the tags origin carries
    rehearse          the whole path on the Architect's rehearsal span, every request held to the idle
                      stretch, against the Architect's independent figures (G-REHEARSAL)
    fetch             the set and both feeds of its fills, every request held to the idle stretch (G-SET)
    constants         label-free: each group's sums by member, V, Sh, thresholds and power, on disk
    score             the labels, read once, and each group's reading
    reclaim TREE...   section 9

It loads research/tz23-maker-m0.py from beside itself, executed from the bytes whose SHA-256 it asserts,
and calls TZ-23's functions for the walk, the documents, every request for fills, every position, cost and
rebate, the thresholds, the power and the reading: it writes no second implementation of any of them. Its
requests are TZ-23's, to gamma-api.polymarket.com and data-api.polymarket.com through TZ-23's http_json and
its two headers, each walk and each chunk started only inside seconds 15 to 470 of a 900-second window and
never near or during the pair book archive's run; and git against origin. Under /var/lib/btc-recorder,
/var/lib/btc-chainbook and /var/lib/btc-pairbook it opens and lists nothing, and under
/var/lib/btc-pairbook-archive it opens ledger.jsonl alone, for reading, in modes archive and still: an audit
hook refuses everything else there. It writes under /root/tz31-work/ and, in `reclaim`, new files in
/root/btc-forensics/ by exclusive create. It prints sums over a set - a group's, a wallet's, a band's - and no
price, size or outcome of any single fill or market. Exit 0: every assert of the mode held. Exit 1: an
assert failed, and its message names it. Run it with the recorder's interpreter, /root/tz04a-env.

Written for CryptoTZ/TZ-31-who-earns.md. The TZ is the specification.
"""

import collections
import concurrent.futures
import gzip
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
    sys.stderr.write("tz31: refuses to run with asserts disabled (-O); every check is an assert\n")
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

MAP_REVISION = "2026-10-22-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 39, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"`?([0-9a-f]{64}|self-reference[^|]*?)`? \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)

M0_LAST = 1792451400         # M0's last member, 2026-10-19 23:10 UTC (TZ-29): no TZ has read a later one
START = M0_LAST + 300        # 1792451700, 2026-10-19 23:15 UTC: the set's walk starts here
N_SET = 1008                 # three and a half days of five-minute markets
START_AT = START + (N_SET - 1) * 300 + 3900    # no mode reads the set before the last member's resolution age
SET_INSTANT = "2026-10-23T12:15:00Z"          # START_AT, as the self-test asserts
FORMATION = (1792192500, 1792451400)    # the 864 markets the Architect named the groups on, all read by M0
REHEARSAL = (1792408500, 144)           # the formation's last 144 markets: G-REHEARSAL's span
FILL_CHUNK = 3               # members a chunk of fills: both feeds of three markets in memory at once
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
MEM_FLOOR = 172064768        # MemAvailable: twice the largest peak of any mode (TZ-31 section 0.4)

ALPHA = D("0.005")           # each answer's false-reading probability, for each group
DELTA = tz23.DELTA           # half a tick a share, TZ-23's and M0's bar
LIFE_BANDS = ("pre", "w0", "w1", "w2", "w3", "last")    # every fill before T0 + 300; "post" is after the reading
FLIP = {"B": "S", "S": "B"}
REBATE_RATE = tz23.FEE_SCHEDULE["rebateRate"]
GROUP_ORDER = ("makers", "takers")
GROUP_SIZE = 10
# The two groups, named by the Architect on FORMATION (TZ-31 section 1): the makers by the largest S / sqrt(V) among the
# wallets with a maker fill in at least 648 of its 864 markets, gated; the takers by the largest S among those with a
# taker fill in at least 432, barred from every reading. Each wallet as the venue's proxy_wallet prints it.
GROUPS = {
    "makers": {"role": "maker", "gated": True, "lambda": D("0.00099017"), "wallets": (
        "0x32c4922da31d9f90232ea40748846e5ccc48b175", "0xf548517cbefe7636bef51ee31a1817f021e7c20e",
        "0xbfa0ed0c199c00aec969d822818f789ca35acd6d", "0x373b2d17d78c27bbdbcb034dae71d26b8094c855",
        "0x1dd2a69e73ba444ecd5d87f0073d51a670ad51c2", "0x809f275254e21f720a4e6c50c28c669c721f2ef0",
        "0x18c18e0c8c3154360b4f730ec8b9d8013ceb2183", "0x764fd57b0b885cbeada5a119cdf0a113ee4ec347",
        "0xf79dccd12edb1e599dc3f9bff979b95987609fe9", "0xd8f1fbe130e2b33f32633bf568a08b85058e74a9")},
    "takers": {"role": "taker", "gated": False, "lambda": D("0.00022256"), "wallets": (
        "0xd84403efd50b49a1d8a7181627e00307e6ea5908", "0x129246beaac356e104c397f0985c11b7469be5a6",
        "0x41e2e1ccf1e4940029af02259a31c6b89b9fa354", "0xeebde7a0e019a63e6b476eb425505b7b3e6eba30",
        "0x5a06acbaee263540a16a0109d584f6672101ffa2", "0x20d2309cd92b797ae7ca175ed828ed8a27fbe29d",
        "0x3c58ef422754ff22c7e806336feba0064d8b776b", "0x14ea1c239393f7c1ad68c72e34e250e0679583b5",
        "0x19b3823092892c026517fd0ff58df4889abe0b9b", "0x5e2b9261b0c4f697b55bf921ff2bc227183d9101")},
}
# The projection: each group's V and Sh at the set's size, at the formation's rates, and the Architect's independent
# threshold and power at them (TZ-31 section 1)
PROJ = {"makers": (D("18528280.704135900604"), D("2085206.453030"),
                   {"thr": D("8026.39675309200283047593171014597323349"), "power": (D("0.9624"), D("0.9625"))}),
        "takers": (D("366723215.042597362222"), D("2567699.904176"),
                   {"thr": D("35708.8558101879212986317691272476559876"), "power": (D("0.0225"), D("0.0226"))})}
# The Architect's independent figures for the rehearsal span (TZ-31 section 4.1)
REF = {"members": 144, "ups": 71, "groups": {
    "makers": {"n": 32911, "sh": D("414244.819465"), "X": D("-6778.530163"), "C": D("-6531.4184270423230341"),
               "R": D("957.39614134740118920440492969386"), "V": D("4897801.198403732397"),
               "P": D("2407.4304690423230341"), "S": D("3364.82661038972422330440492969386")},
    "takers": {"n": 8326, "sh": D("412423.876637"), "X": D("-831.786637"), "C": D("14859.1622011511058812"),
               "R": D("984.45142398558404651653052080920"), "V": D("60301555.497845147905"),
               "P": D("8245.6376908488941188"), "S": D("3323.3805709209738862173473959540")}}}

WORK = "/root/tz31-work"
WT = WORK + "/wt"
STATE = WORK + "/state.json"
LEDGER = WORK + "/label-ledger.jsonl"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
BRANCH = "tz-31-who-earns"
UNITS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service"}
CAPTURE_ROOTS = ("/var/lib/btc-recorder", "/var/lib/btc-chainbook", "/var/lib/btc-pairbook")
ARCHIVE_STATE = "/var/lib/btc-pairbook-archive"
ARCHIVE_LEDGER = ARCHIVE_STATE + "/ledger.jsonl"
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
WALLET = re.compile(r"0x[0-9a-f]{40}")
LIVE_S = 60                  # a directory born this soon after a claude process started is that process's

# ---- the audit hook: TZ-31 section 2's reads and writes ------------------------------------------------

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
    """None where TZ-31 section 2 allows the event in this mode; otherwise the reason it is refused."""
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
        return None if mode in ("archive", "still") and p == ARCHIVE_LEDGER and not w else \
            "an open under the archive's state"
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


def fill_groups_of(s):
    """The set's members in chunks of FILL_CHUNK, in T0 order: one chunk of fills each."""
    return [[(m["t0"], m["doc"]) for m in s["members"][i:i + FILL_CHUNK]]
            for i in range(0, len(s["members"]), FILL_CHUNK)]

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

# ---- the fills: both feeds of a chunk, and the makers' rows between them ------------------------------------


def split_feeds(full, taker):
    """The makers' rows of one market: its full feed less its takers' rows, as multisets of whole rows - every
    takers' row must be in the full feed. No Decimal arithmetic: it runs in the fetch's worker threads (map section 7
    item 99)."""
    left = collections.Counter(tuple(r) for r in full)
    for r in taker:
        k = tuple(r)
        assert left[k] > 0, "a takers' row not in the full feed: %r" % (r,)
        left[k] -= 1
    return sorted(list(k) for k, n in left.items() for _ in range(n))


def feed_check(taker, maker):
    """One market's transactions, those whose makers' and takers' sizes differ - the venue prints a maker's size at
    two decimals where a taker's carries six - and those with one side's rows alone. Summed in the main thread."""
    size = collections.defaultdict(lambda: [D(0), D(0)])
    for i, rows in ((0, taker), (1, maker)):
        for r in rows:
            size[r[6]][i] += D(r[3])
    differ = sum(1 for t, (a, b) in size.items() if a > 0 and b > 0 and a != b)
    one_side = sum(1 for t, (a, b) in size.items() if (a > 0) != (b > 0))
    return {"transactions": len(size), "sizes_differ": differ, "one_side_only": one_side}


def fetch_chunk2(cache, group):
    """Both feeds of up to FILL_CHUNK members by TZ-23's trades - the full feed (taker_only false) and the takers'
    (taker_only true), each row with its token, transaction and wallet - written once, atomically: a member's
    takers' rows and its makers', the full feed less the takers'."""
    path = tz23.chunk_path(cache, group[0][0])
    if os.path.exists(path):
        return path, False
    cids = [d["conditionId"] for _t, d in group]
    tokens = {d["conditionId"]: json.loads(d["clobTokenIds"]) for _t, d in group}
    full = tz23.trades(cids, "false", tokens, keep_tx=True)
    taker = tz23.trades(cids, "true", tokens, keep_tx=True)
    members = []
    for t, d in group:
        c = d["conditionId"]
        members.append({"t0": t, "condition": c, "taker": sorted(taker[c]), "maker": split_feeds(full[c], taker[c])})
    tz23.write_atomic(path, tz23.gz_bytes(dumps({"members": members})))
    return path, True


def member_rows2(cache, groups):
    """Every member's two sides, in T0 order, read back from the cache."""
    for g in groups:
        with gzip.open(tz23.chunk_path(cache, g[0][0]), "rt", encoding="utf-8") as fh:
            doc = json.load(fh)
        assert [m["t0"] for m in doc["members"]] == [t for t, _d in g], "chunk %d: its members" % g[0][0]
        for m, (t, d) in zip(doc["members"], g):
            assert m["condition"] == d["conditionId"], "chunk %d: member %d's condition" % (g[0][0], t)
            yield t, d, m


def fetch_held(base, s, timing, budget_s=FETCH_BUDGET_S, fetcher=None, holdf=hold, clock=time.time):
    """Every chunk not already in the cache fetched by `fetcher`, fetch_chunk2 by default, on TZ-23's two worker
    threads, each started where holdf allows, its start and end written to `timing`."""
    fetcher = fetcher or fetch_chunk2
    cache = os.path.join(base, "cache")
    os.makedirs(cache, exist_ok=True)
    groups = fill_groups_of(s)

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

# ---- a group's sums: TZ-23's aggregate on a wallet's own rows ------------------------------------------------


def own_rows(rows):
    """A wallet's own rows as TZ-23's aggregate reads a taker's: the side flipped, so that its maker_terms give the
    wallet's own position - BUY Up +s at p, SELL Up -s at p, BUY Down -s at 1 - p, SELL Down +s at 1 - p."""
    return [[r[0], FLIP[r[1]], r[2], r[3], r[4]] for r in rows]


def life_of(bands):
    """The sums over every fill before T0 + 300: TZ-23's bands pre, w0 to w3 and last."""
    z = tz23.zero()
    for name in LIFE_BANDS:
        for k in z:
            z[k] += bands[name][k]
    return z


def side_rows(m, role):
    return m["maker"] if role == "maker" else m["taker"]


def extra_of(role, R):
    """A group's own money beyond settlement: a maker's rebate, R itself; a taker's fee, R over the rebate rate,
    so 0.07 s p (1 - p), taken off."""
    return R if role == "maker" else -(R / REBATE_RATE)


BAND_NAMES = [n for n, _l, _h in tz23.BANDS]
COLS2 = ["t0"] + ["%s_%s" % (k, b) for b in ["life"] + BAND_NAMES for k in ("n", "sh", "X", "C", "R")]
WCOLS = ["t0", "wallet", "n", "sh", "X", "C", "R"]
PCOLS = ["t0"] + ["%s_%s" % (k, r) for r in ("maker", "taker") for k in ("n", "sh", "X", "C", "R")] + [
    "transactions", "sizes_differ", "one_side_only"]


def cells(agg):
    return [str(agg[k]) if k == "n" else fx(agg[k]) for k in ("n", "sh", "X", "C", "R")]


def build_constants2(base, s, cache, groups, label):
    """Label-free: for each group its members file - every member's sums over its life and by band - its wallets
    file, its fills file and its gate; the pool of all makers and all takers beside them. A second run must write
    the same bytes."""
    t0s = [m["t0"] for m in s["members"]]
    sel = {g: frozenset(GROUPS[g]["wallets"]) for g in GROUP_ORDER}
    lines = {g: [",".join(COLS2)] for g in GROUP_ORDER}
    wlines = {g: [",".join(WCOLS)] for g in GROUP_ORDER}
    plines = [",".join(PCOLS)]
    tot = {g: {"V": D(0), "life": tz23.zero(), "members_with_fills": 0, "wallets_seen": set()} for g in GROUP_ORDER}
    fills = {g: os.path.join(base, "%s-%s-fills.jsonl.gz" % (label, g)) for g in GROUP_ORDER}
    raws = {g: open(fills[g] + ".build", "wb") for g in GROUP_ORDER}
    gzs = {g: gzip.GzipFile(filename="", mode="wb", fileobj=raws[g], mtime=0) for g in GROUP_ORDER}
    try:
        for t0, d, m in member_rows2(cache, groups):
            pool = []
            for role in ("maker", "taker"):
                b, _w = tz23.aggregate(t0, own_rows(side_rows(m, role)))
                pool += cells(life_of(b))
            chk = feed_check(m["taker"], m["maker"])
            plines.append(",".join([str(t0)] + pool + [str(chk[k]) for k in (
                "transactions", "sizes_differ", "one_side_only")]))
            for g in GROUP_ORDER:
                role = GROUPS[g]["role"]
                rows = [r for r in side_rows(m, role) if r[7] in sel[g]]
                bands, _win = tz23.aggregate(t0, own_rows(rows))
                life = life_of(bands)
                tt = tot[g]
                tt["V"] += life["X"] * life["X"]
                for k in life:
                    tt["life"][k] += life[k]
                tt["members_with_fills"] += 1 if life["n"] else 0
                row = [str(t0)] + cells(life)
                for name in BAND_NAMES:
                    row += cells(bands[name])
                lines[g].append(",".join(row))
                byw = collections.defaultdict(list)
                for r in rows:
                    byw[r[7]].append(r)
                for w in sorted(byw):
                    wb, _ww = tz23.aggregate(t0, own_rows(byw[w]))
                    wlines[g].append(",".join([str(t0), w] + cells(life_of(wb))))
                    tt["wallets_seen"].add(w)
                gzs[g].write(dumps({"t0": t0, "rows": sorted(rows)}).encode("utf-8"))
    finally:
        for g in GROUP_ORDER:
            gzs[g].close()
            raws[g].close()
    paths = {}
    gate = {}
    for g in GROUP_ORDER:
        tmp = fills[g] + ".build"
        fsha = tz23.sha256_file(tmp)
        if os.path.exists(fills[g]):
            assert tz23.sha256_file(fills[g]) == fsha, "determinism: %s differs" % fills[g]
            os.remove(tmp)
            out("unchanged %s sha256 %s" % (fills[g], fsha))
        else:
            os.replace(tmp, fills[g])
        paths["%s-fills.jsonl.gz" % g] = (fills[g], fsha)
        for name, body in (("members.csv", lines[g]), ("wallets.csv", wlines[g])):
            pth = os.path.join(base, "%s-%s-%s" % (label, g, name))
            paths["%s-%s" % (g, name)] = (pth, tz23.write_once(pth, ("\n".join(body) + "\n").encode("utf-8")))
        tt, gc = tot[g], GROUPS[g]
        c = tz23.gate_constants(tt["V"], tt["life"]["sh"], lam=gc["lambda"], alpha=ALPHA, delta=DELTA)
        gate[g] = {"role": gc["role"], "gated": gc["gated"], "wallets": list(gc["wallets"]),
                   "wallets_with_fills": len(tt["wallets_seen"]),
                   "members_with_fills": tt["members_with_fills"], "life": tt["life"], "gate": c,
                   "members_csv_sha": paths["%s-members.csv" % g][1], "wallets_csv_sha": paths["%s-wallets.csv" % g][1],
                   "fills_sha": fsha}
    ppath = os.path.join(base, "%s-pool.csv" % label)
    paths["pool.csv"] = (ppath, tz23.write_once(ppath, ("\n".join(plines) + "\n").encode("utf-8")))
    nonm = [[t, st] for t, st in s["considered"] if st != "member"]
    const = {"label": label, "members": len(t0s), "first": t0s[0], "last": t0s[-1],
             "member_list_sha": tz23.sha256_bytes(("\n".join(map(str, t0s)) + "\n").encode()),
             "considered": len(s["considered"]), "non_members": nonm, "groups": gate,
             "pool_csv_sha": paths["pool.csv"][1]}
    cpath = os.path.join(base, "%s-constants.json" % label)
    paths["constants.json"] = (cpath, tz23.write_once(cpath, dumps(const).encode("utf-8")))
    return const, paths


def show_constants2(const, paths):
    out("members %d, considered %d, first %d %s, last %d %s; member list sha %s" % (
        const["members"], const["considered"], const["first"], utc(const["first"]), const["last"],
        utc(const["last"]), const["member_list_sha"]))
    for t, st in const["non_members"]:
        out("non-member %d %s: %s" % (t, utc(t), st))
    for g in GROUP_ORDER:
        gg, c, lf = const["groups"][g], const["groups"][g]["gate"], const["groups"][g]["life"]
        out("%s (%s rows of %d wallets, %d of them with a fill): members with a fill %d; fills %d, shares %s, "
            "X %s, C %s, R %s" % (g, gg["role"], len(gg["wallets"]), gg["wallets_with_fills"],
                                  gg["members_with_fills"], lf["n"], fx(lf["sh"]), fx(lf["X"]), fx(lf["C"]),
                                  fx(lf["R"])))
        out("%s: V %s; Sh %s; lambda %s; L %s; thr %s (%s a share)" % (
            g, fx(c["V"]), fx(c["sh"]), fx(c["lambda"]), q12(c["L"]), q12(c["thr"]),
            q12(c["thr_per_share"]) if "thr_per_share" in c else "-"))
        out("%s%s: W-EARN at S >= %s (%s a share); W-NO-EARN at S <= %s (%s a share); power of either answer "
            "against the other's alternative %s" % (
                g, "" if gg["gated"] else ", barred from every reading", q12(c["earn_at"]),
                q12(c["thr_per_share"]) if "thr_per_share" in c else "-", q12(c["no_earn_at"]),
                q12(c["no_earn_per_share"]) if "no_earn_per_share" in c else "-", fx(c["power"])))
    for name, (p, h) in sorted(paths.items()):
        out("wrote %s sha256 %s" % (p, h))


def q12(x):
    """A figure for print, half-even to 12 places; every sum and comparison is made on the exact figure."""
    return fx(x.quantize(D("0.000000000001")))


def read_csv(path, cols):
    with open(path, encoding="utf-8") as fh:
        rows = [ln.split(",") for ln in fh.read().splitlines()]
    assert rows[0] == cols, "%s: its header" % path
    return rows[1:]


WORDS = {"EARN": "W-EARN", "NO EARN": "W-NO-EARN", "UNDECIDABLE": "UNDECIDABLE"}


def score2(base, s, const, label):
    """The labels, read once from the set's own documents, and each group's reading by TZ-23's reading on this TZ's
    thresholds; beside them, barred from every reading, each wallet's, each band's and the pool's result."""
    docs = {m["t0"]: m["doc"] for m in s["members"]}
    ups = {t: tz23.label_of(d) for t, d in docs.items()}
    res = {"label": label, "members": len(docs), "ups": sum(ups.values()), "groups": {}}
    scored = {}
    for g in GROUP_ORDER:
        gg = const["groups"][g]
        role, c = gg["role"], gg["gate"]
        rows = read_csv(os.path.join(base, "%s-%s-members.csv" % (label, g)), COLS2)
        assert [int(r[0]) for r in rows] == [m["t0"] for m in s["members"]], "%s: members" % g
        ix = {k: i for i, k in enumerate(COLS2)}
        S = P = E = D(0)
        bands = {b: [D(0), D(0)] for b in BAND_NAMES}
        out_rows = ["t0,up,X,C,R,pnl"]
        for r in rows:
            t0 = int(r[0])
            up = ups[t0]
            X, C, R = D(r[ix["X_life"]]), D(r[ix["C_life"]]), D(r[ix["R_life"]])
            settle, extra = X * up - C, extra_of(role, R)
            S += settle + extra
            P += settle
            E += extra
            out_rows.append("%d,%d,%s,%s,%s,%s" % (t0, up, fx(X), fx(C), fx(R), fx(settle + extra)))
            for b in BAND_NAMES:
                bands[b][0] += D(r[ix["X_" + b]]) * up - D(r[ix["C_" + b]]) + extra_of(role, D(r[ix["R_" + b]]))
                bands[b][1] += D(r[ix["sh_" + b]])
        word, earn, no_earn = tz23.reading(S, {"earn_at": D(c["earn_at"]), "no_earn_at": D(c["no_earn_at"])})
        sh = D(c["sh"])
        wl = read_csv(os.path.join(base, "%s-%s-wallets.csv" % (label, g)), WCOLS)
        per_w = collections.defaultdict(lambda: [D(0), D(0), 0])
        for t0, w, n, shw, X, C, R in wl:
            up = ups[int(t0)]
            per_w[w][0] += D(X) * up - D(C) + extra_of(role, D(R))
            per_w[w][1] += D(shw)
            per_w[w][2] += 1
        res["groups"][g] = {
            "role": role, "gated": gg["gated"], "S": S, "settlement": P, "extra": E, "sh": sh,
            "reading": WORDS[word] if gg["gated"] else None, "w_earn": earn, "w_no_earn": no_earn,
            "per_share": S / sh if sh else None, "settlement_per_share": P / sh if sh else None,
            "extra_per_share": E / sh if sh else None, "margin_w_earn": S - D(c["earn_at"]),
            "margin_w_no_earn": D(c["no_earn_at"]) - S,
            "barred_wallets": {w: {"S": v[0], "sh": v[1], "members": v[2], "per_share": v[0] / v[1] if v[1] else None}
                               for w, v in sorted(per_w.items())},
            "barred_bands": {b: {"S": v[0], "sh": v[1], "per_share": v[0] / v[1] if v[1] else None}
                             for b, v in bands.items()}}
        scored[g] = ("\n".join(out_rows) + "\n").encode("utf-8")
    prow = read_csv(os.path.join(base, "%s-pool.csv" % label), PCOLS)
    pi = {k: i for i, k in enumerate(PCOLS)}
    pool = {}
    for role in ("maker", "taker"):
        S = sh = D(0)
        for r in prow:
            up = ups[int(r[0])]
            S += D(r[pi["X_" + role]]) * up - D(r[pi["C_" + role]]) + extra_of(role, D(r[pi["R_" + role]]))
            sh += D(r[pi["sh_" + role]])
        pool[role] = {"S": S, "sh": sh, "per_share": S / sh if sh else None}
    res["barred_pool"] = pool
    res["checks"] = {k: sum(int(r[pi[k]]) for r in prow) for k in ("transactions", "sizes_differ", "one_side_only")}
    paths = {}
    for g in GROUP_ORDER:
        p = os.path.join(base, "%s-%s-scored.csv" % (label, g))
        paths[g] = tz23.write_once(p, scored[g])
    rp = os.path.join(base, "%s-reading.json" % label)
    paths["reading"] = tz23.write_once(rp, dumps(res).encode("utf-8"))
    out("labels: %d members, %d Up" % (len(docs), res["ups"]))
    for g in GROUP_ORDER:
        r = res["groups"][g]
        out("%s: S %s = settlement %s + %s %s; per share %s = %s + %s" % (
            g, fx(r["S"]), fx(r["settlement"]), "rebate" if r["role"] == "maker" else "fee", fx(r["extra"]),
            q12(r["per_share"]), q12(r["settlement_per_share"]), q12(r["extra_per_share"])))
        out("%s%s: W-EARN %s (margin %s); W-NO-EARN %s (margin %s)" % (
            g, "" if r["gated"] else ", barred from every reading", r["w_earn"], q12(r["margin_w_earn"]),
            r["w_no_earn"], q12(r["margin_w_no_earn"])))
        for w, v in r["barred_wallets"].items():
            out("%s barred: wallet %s, %d members, shares %s, S %s, per share %s" % (
                g, w, v["members"], fx(v["sh"]), q12(v["S"]), q12(v["per_share"]) if v["per_share"] is not None
                else "-"))
        for b, v in r["barred_bands"].items():
            if v["sh"]:
                out("%s barred: band %-4s shares %s, S %s, per share %s" % (g, b, fx(v["sh"]), q12(v["S"]),
                                                                           q12(v["per_share"])))
    for role, v in pool.items():
        out("barred: every %s together: S %s on %s shares, %s a share" % (
            role, q12(v["S"]), fx(v["sh"]), q12(v["per_share"]) if v["per_share"] is not None else "-"))
    out("the feeds: %d transactions, makers' and takers' sizes differ at %d, one side only at %d" % (
        res["checks"]["transactions"], res["checks"]["sizes_differ"], res["checks"]["one_side_only"]))
    for g in GROUP_ORDER:
        out("wrote %s-%s-scored.csv sha256 %s" % (label, g, paths[g]))
    out("wrote %s-reading.json sha256 %s" % (label, paths["reading"]))
    return res

# ---- the archive's record --------------------------------------------------------------------------------


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
            parts.append("Release %s: sent %s, held %s, credential %s" % (r.get("release_id"), r.get("sent"),
                                                                         r.get("held"), r.get("credential")))
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
    with open(os.path.join(PRIMARY, "research", TZ23_NAME), "rb") as fh:
        t23 = tz23.sha256_bytes(fh.read())
    assert t23 == TZ23_SHA256, "the primary checkout's %s sha256 %s" % (TZ23_NAME, t23)
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), tz23.sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d; %s is the file this instrument loads" % (
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


def ledger_records():
    """The archive's ledger, its complete lines; opened in modes archive and still alone (section 2 item 4)."""
    with open(ARCHIVE_LEDGER, "rb") as fh:
        raw = fh.read()
    lines = raw.split(b"\n")
    tail = lines.pop()
    return raw, [json.loads(ln) for ln in lines if ln.strip()], tail


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
    """The archive's own record, read whole: its complete lines, each printed, and its runs summarized."""
    for unit in (ARCHIVE_TIMER, ARCHIVE_UNIT):
        out("%s %s" % (unit, show(unit, ["ActiveState", "SubState", "UnitFileState", "Result", "ExecMainStatus",
                                         "LastTriggerUSec", "NextElapseUSecRealtime"])))
    raw, recs, tail = ledger_records()
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


def figures(const, res):
    """The figures G-REHEARSAL compares: the members, the Up count, and each group's sums over the span."""
    got = {"members": const["members"], "ups": res["ups"], "groups": {}}
    for g in GROUP_ORDER:
        lf, c, r = const["groups"][g]["life"], const["groups"][g]["gate"], res["groups"][g]
        got["groups"][g] = {"n": lf["n"], "sh": lf["sh"], "X": lf["X"], "C": lf["C"], "R": lf["R"], "V": c["V"],
                            "P": r["settlement"], "S": r["S"]}
    return got


def compare_ref(got, ref=None):
    """Every figure against the Architect's, exactly: a list of (name, equal)."""
    ref = ref or REF
    checks = [("members", got["members"] == ref["members"]), ("ups", got["ups"] == ref["ups"])]
    for g in GROUP_ORDER:
        for k in ("n", "sh", "X", "C", "R", "V", "P", "S"):
            checks.append(("%s %s" % (g, k), got["groups"][g][k] == ref["groups"][g][k]))
    return checks


def mode_rehearse():
    floor_check()
    base = os.path.join(WORK, "rehearsal")
    s = walk(base, REHEARSAL[0], (), REHEARSAL[1])
    assert len(s["members"]) == REF["members"] and len(s["considered"]) == REF["members"], \
        "G-REHEARSAL: %d members of %d considered" % (len(s["members"]), len(s["considered"]))
    cache, groups = fetch_held(base, s, os.path.join(base, "rehearsal-timing.jsonl"), budget_s=10 ** 9)
    timing_summary(os.path.join(base, "rehearsal-timing.jsonl"))
    const, paths = build_constants2(base, s, cache, groups, "rehearsal")
    show_constants2(const, paths)
    res = score2(base, s, const, "rehearsal")
    got = figures(const, res)
    checks = compare_ref(got)
    for name, eq in checks:
        g, _sp, k = name.partition(" ")
        a = got["groups"][g][k] if k else got[name]
        b = REF["groups"][g][k] if k else REF[name]
        out("G-REHEARSAL %-12s instrument %s, the Architect's %s, %s" % (name, a, b, "equal" if eq else "DIFFERENT"))
    bad = [n for n, eq in checks if not eq]
    assert not bad, "G-REHEARSAL FAIL: %s" % bad
    out("G-REHEARSAL PASS: %d of %d figures equal to the Architect's" % (len(checks), len(checks)))


def the_set():
    base = os.path.join(WORK, "set")
    s = load_json(os.path.join(base, "set.json"))
    return base, s, os.path.join(base, "cache"), fill_groups_of(s)


def mode_fetch():
    now = time.time()
    assert now >= START_AT, "BLOCKED: %s is before %s, TZ-31's instant" % (utc(now), utc(START_AT))
    floor_check()
    base = os.path.join(WORK, "set")
    os.makedirs(base, exist_ok=True)
    s = walk(base, START, tz23.EXCLUDED, N_SET)
    t0s = [m["t0"] for m in s["members"]]
    assert s["start"] == START and s["need"] == N_SET and len(t0s) == N_SET, "G-SET: %d members" % len(t0s)
    assert s["considered"][0][0] == START and t0s[0] > M0_LAST, "G-SET: the walk did not start at %d" % START
    cache, groups = fetch_held(base, s, os.path.join(base, "fetch-timing.jsonl"))
    n = sum(1 for _ in member_rows2(cache, groups))
    assert n == N_SET, "G-SET: %d members read back" % n
    timing_summary(os.path.join(base, "fetch-timing.jsonl"))
    out("G-SET PASS: %d members, %d considered, %d to %d, %d chunks, every chunk read back" % (
        N_SET, len(s["considered"]), t0s[0], t0s[-1], len(groups)))


def mode_constants():
    floor_check()
    base, s, cache, groups = the_set()
    assert len(s["members"]) == N_SET and s["start"] == START, "the set"
    const, paths = build_constants2(base, s, cache, groups, "tz31")
    show_constants2(const, paths)
    st = load_state()
    st["constants_sha"], st["constants_at"] = paths["constants.json"][1], utc(time.time())
    save_state(st)


def mode_score():
    floor_check()
    base, s, _cache, _groups = the_set()
    cpath = os.path.join(base, "tz31-constants.json")
    st = load_state()
    assert tz23.sha256_file(cpath) == st.get("constants_sha"), "score: not the constants recorded"
    head = git("rev-parse", "HEAD")
    assert "origin/" + BRANCH in git("branch", "-r", "--contains", head).split(), \
        "score: HEAD %s is not on origin" % head
    const = load_json(cpath)
    t0s = [m["t0"] for m in s["members"]]
    assert tz23.sha256_bytes(("\n".join(map(str, t0s)) + "\n").encode()) == const["member_list_sha"], \
        "score: the members are not the constants' members"
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(dumps({"at": utc(time.time()), "head": head, "members": const["members"],
                        "member_list_sha": const["member_list_sha"]}))
    res = score2(base, s, const, "tz31")
    r = res["groups"]["makers"]
    if r["w_earn"] and r["w_no_earn"]:
        out("both bounds hold: the reading is W-EARN, and half a tick a share is rejected too (TZ-23 section 4.3)")
    out("W0 READING, THE MAKERS: %s" % r["reading"])


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


def pnl_by_row(role, rows, won_up):
    """The self-test's own arithmetic, written apart from TZ-23's: one row's money at settlement, its rebate or its
    fee taken at the row - BUY a token at p pays s (won - p), SELL pays s (p - won) - summed."""
    tot = D(0)
    for r in rows:
        side, outcome, s, p = r[1], r[2], D(r[3]), D(r[4])
        won = won_up if outcome == "U" else 1 - won_up
        money = s * (won - p) if side == "B" else s * (p - won)
        fee = D("0.07") * s * p * (1 - p)
        tot += money + (fee * D("0.2") if role == "maker" else -fee)
    return tot


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
    ok((tz23.STEP, tz23.CHUNK, tz23.RESOLVED_AFTER_S, tz23.WALK_SLACK, tz23.FETCH_WORKERS) == (300, 20, 3900, 2016, 2),
       "TZ-23's step, document chunk, resolution age, slack and workers")
    ok(DELTA == D("0.005") and REBATE_RATE == D("0.2") and tz23.REBATE_COEF == D("0.014") and
       tz23.FEE_SCHEDULE == {"exponent": 1, "rate": D("0.07"), "takerOnly": True, "rebateRate": D("0.2")},
       "half a tick a share; the fee 0.07 s p (1 - p), the rebate a fifth of it, as the documents must state")
    ok(tz23.HEADERS == {"User-Agent": "btc-5m-twap-m0/TZ-23", "Accept": "application/json"},
       "every request carries TZ-23's two headers")
    ok(tz23.BANDS[0] == ("pre", None, 0) and tz23.BANDS[-2] == ("last", 240, 300) and
       tz23.BANDS[-1] == ("post", 300, None) and LIFE_BANDS == tuple(b for b in BAND_NAMES if b != "post"),
       "a market's life is every fill before T0 + 300: TZ-23's bands but post")
    # the set: its start, its instant and its walk
    ok(START == 1792451700 and utc(START) == "2026-10-19T23:15:00Z" and START == M0_LAST + 300,
       "the walk starts at 2026-10-19 23:15 UTC, the market after M0's last")
    ok(START_AT == START + (N_SET - 1) * tz23.STEP + tz23.RESOLVED_AFTER_S and utc(START_AT) == SET_INSTANT,
       "no set is read before %s, the last member's resolution age if every candidate qualifies" % SET_INSTANT)
    ok(tz23.next_open(START, tz23.EXCLUDED) == START and not tz23.excluded(START, tz23.EXCLUDED),
       "no excluded span reaches the set")
    ok(FORMATION[1] == M0_LAST and (FORMATION[1] - FORMATION[0]) // 300 + 1 == 864 and
       REHEARSAL[0] + (REHEARSAL[1] - 1) * 300 == M0_LAST,
       "the formation is M0's last 864 markets and the rehearsal its last 144")
    good = {"slug": "", "outcomes": '["Up", "Down"]', "outcomePrices": '["1", "0"]', "closed": True,
            "feeType": tz23.FEE_TYPE, "feeSchedule": dict(tz23.FEE_SCHEDULE), "eventStartTime": "",
            "conditionId": "0x" + "cd" * 32, "clobTokenIds": '["11", "22"]'}

    def fake_docs(t0s, asked=None):
        if asked is not None:
            asked.extend(t0s)
        return {"btc-updown-5m-%d" % t: dict(good, slug="btc-updown-5m-%d" % t, eventStartTime=tz23.iso(t))
                for t in t0s}

    asked = []
    cons, mem = tz23.candidates(START, tz23.EXCLUDED, 50, lambda ts: fake_docs(ts, asked))
    ok(len(mem) == 50 and mem[0][0] == START and mem[-1][0] == START + 49 * 300 and len(cons) == 50 and
       asked == [t for t, _st in cons] and min(asked) > M0_LAST,
       "TZ-23's walk from 1792451700 takes 50 members in 50 documents and requests none at or below M0's last")
    ok(len(fill_groups_of({"members": [{"t0": START + 300 * i, "doc": good} for i in range(N_SET)]})) ==
       -(-N_SET // FILL_CHUNK), "the set's members are %d chunks of fills" % -(-N_SET // FILL_CHUNK))
    # the groups, as named
    ok(all(WALLET.fullmatch(w) for g in GROUP_ORDER for w in GROUPS[g]["wallets"]) and
       all(len(set(GROUPS[g]["wallets"])) == len(GROUPS[g]["wallets"]) == GROUP_SIZE for g in GROUP_ORDER) and
       [(GROUPS[g]["role"], GROUPS[g]["gated"]) for g in GROUP_ORDER] == [("maker", True), ("taker", False)],
       "each group names %d distinct wallets: the makers' rows, gated; the takers', barred" % GROUP_SIZE)
    # the feeds: the makers' rows are the full feed less the takers'
    T = 1792500000
    tk = [[T + 10, "B", "U", "10", "0.6", "11", "0xaa", "0x" + "1" * 40]]
    mk = [[T + 10, "S", "U", "4", "0.6", "11", "0xaa", "0x" + "2" * 40],
          [T + 10, "B", "D", "6", "0.4", "22", "0xaa", "0x" + "3" * 40]]
    maker = split_feeds(mk + tk + [list(mk[0])], tk)
    diag = feed_check(tk, maker)
    ok(sorted(maker) == sorted(mk + [list(mk[0])]) and diag == {"transactions": 1, "sizes_differ": 1,
                                                               "one_side_only": 0},
       "the makers' rows are the full feed less the takers', as multisets; a transaction whose sizes differ counted")
    maker = split_feeds(mk + tk, tk)
    ok(sorted(maker) == sorted(mk) and feed_check(tk, maker)["sizes_differ"] == 0 and
       feed_check(tk, [])["one_side_only"] == 1, "sizes 4 + 6 against 10 are equal; a transaction with the takers' "
                                                  "rows alone is counted")
    try:
        split_feeds(mk, tk)
        caught = False
    except AssertionError:
        caught = True
    ok(caught, "a takers' row absent from the full feed is a failed assert")
    # a wallet's own position: TZ-23's maker_terms on the flipped side, against this file's own row arithmetic
    rows = [[T, "B", "U", "10", "0.6"], [T, "S", "U", "3", "0.7"], [T, "B", "D", "5", "0.25"],
            [T, "S", "D", "2", "0.9"]]
    b, _w = tz23.aggregate(T - 60, own_rows(rows))
    lf = life_of(b)
    ok(lf["X"] == D(10) - 3 - 5 + 2 and lf["C"] == D("6") - D("2.1") - D("3.75") + D("0.2") and
       lf["sh"] == D(20) and lf["n"] == 4, "own rows: BUY Up +s at p, SELL Up -s at p, BUY Down -s at 1 - p, SELL "
                                          "Down +s at 1 - p")
    for up in (0, 1):
        for role in ("maker", "taker"):
            ok(lf["X"] * up - lf["C"] + extra_of(role, lf["R"]) == pnl_by_row(role, rows, up),
               "%s, Up %d: X up - C plus the rebate or less the fee equals the row-by-row money" % (role, up))
    late = rows + [[T - 60 + 300, "B", "U", "100", "0.99"]]
    b2, _w = tz23.aggregate(T - 60, own_rows(late))
    ok(life_of(b2) == lf and b2["post"]["n"] == 1, "a fill at T0 + 300 is post: outside every life sum")
    # a synthetic set, built, scored, against the row-by-row arithmetic; label-free; deterministic
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    saved = {g: dict(GROUPS[g]) for g in GROUP_ORDER}
    try:
        os.makedirs(tmp)
        rng = random.Random(31)
        wallets = ["0x%040x" % (i + 1) for i in range(8)]
        GROUPS["makers"] = dict(saved["makers"], wallets=tuple(wallets[:3]))
        GROUPS["takers"] = dict(saved["takers"], wallets=tuple(wallets[2:5]))
        t0s = [START + 300 * i for i in range(23)]
        docs = [dict(good, slug="btc-updown-5m-%d" % t, eventStartTime=tz23.iso(t),
                     conditionId="0x%064x" % (i + 1), outcomePrices=('["1", "0"]' if rng.random() < 0.5 else
                                                                     '["0", "1"]')) for i, t in enumerate(t0s)]

        def synth_rows(t):
            def one():
                return [t + rng.randrange(-60, 330), rng.choice("BS"), rng.choice("UD"),
                        tz23.fx(D(rng.randrange(1, 50000)) / 100), tz23.fx(D(rng.randrange(1, 999)) / 1000),
                        rng.choice(["11", "22"]), "0x%064x" % rng.randrange(1, 10 ** 6), rng.choice(wallets)]
            return sorted(one() for _ in range(rng.randrange(0, 30))), sorted(one() for _ in range(rng.randrange(0, 30)))

        synth = {t: synth_rows(t) for t in t0s}

        def build(base, dd, label):
            cache = os.path.join(base, "cache")
            os.makedirs(cache)
            st = {"start": START, "need": len(dd), "considered": [[int(d["slug"].rsplit("-", 1)[1]), "member"]
                                                                  for d in dd],
                  "members": [{"t0": int(d["slug"].rsplit("-", 1)[1]), "doc": tz23.kept_doc(d)} for d in dd]}
            groups = fill_groups_of(st)
            for g in groups:
                tz23.write_atomic(tz23.chunk_path(cache, g[0][0]), tz23.gz_bytes(dumps({"members": [
                    {"t0": t, "condition": d["conditionId"], "taker": synth[t][0], "maker": synth[t][1]}
                    for t, d in g]})))
            const, paths = build_constants2(base, st, cache, groups, label)
            return st, const, paths

        sa, ca, pa = build(os.path.join(tmp, "a"), docs, "x")
        ra = score2(os.path.join(tmp, "a"), sa, ca, "x")
        for g, role, side in (("makers", "maker", 1), ("takers", "taker", 0)):
            want = post = D(0)
            for t, d in zip(t0s, docs):
                up = tz23.label_of(d)
                mine = [r for r in synth[t][side] if r[7] in GROUPS[g]["wallets"]]
                want += pnl_by_row(role, [r for r in mine if r[0] < t + 300], up)
                post += pnl_by_row(role, [r for r in mine if r[0] >= t + 300], up)
            ok(ra["groups"][g]["S"] == want and want != 0,
               "%s: S over the synthetic set equals the row-by-row money of every fill before T0 + 300" % g)
            wsum = sum((v["S"] for v in ra["groups"][g]["barred_wallets"].values()), D(0))
            ok(wsum == want and post != 0 and
               sum((v["S"] for v in ra["groups"][g]["barred_bands"].values()), D(0)) == want + post,
               "%s: the wallets' sums add to S, and the bands' to S with post beside it" % g)
        flip = [dict(d, outcomePrices=('["0", "1"]' if d["outcomePrices"] == '["1", "0"]' else '["1", "0"]'))
                for d in docs]
        sb, cb, pb = build(os.path.join(tmp, "b"), flip, "x")
        ok(pb["constants.json"][1] == pa["constants.json"][1] and all(
            pb[k][1] == pa[k][1] for k in pa), "every constants file is byte-identical with every label flipped")
        rb = score2(os.path.join(tmp, "b"), sb, cb, "x")
        ok(rb["groups"]["makers"]["S"] != ra["groups"]["makers"]["S"], "the score moves when the labels flip "
                                                                       "(negative control)")
        again = build_constants2(os.path.join(tmp, "a"), sa, os.path.join(tmp, "a", "cache"), fill_groups_of(sa), "x")
        ok(again[1] == pa, "a second constants run finds every file unchanged")
        # the readings: TZ-23's table, TZ-23's reading, on this TZ's lambda
        c = tz23.gate_constants(D(10 ** 10), D(10 ** 9), lam=GROUPS["makers"]["lambda"], alpha=ALPHA, delta=DELTA)
        th = {"earn_at": c["earn_at"], "no_earn_at": c["no_earn_at"]}
        ok(c["earn_at"] == c["thr"] and c["no_earn_at"] == DELTA * D(10 ** 9) - c["thr"] and c["thr"] < c["no_earn_at"]
           and [WORDS[tz23.reading(x, th)[0]] for x in (c["thr"] - 1, c["thr"], c["no_earn_at"] + 1)] ==
           ["W-NO-EARN", "W-EARN", "W-EARN"] and tz23.reading(c["thr"], th)[1:] == (True, True),
           "W-EARN at S >= thr, W-NO-EARN at S <= delta Sh - thr, W-EARN first where both hold")
        c2 = tz23.gate_constants(D(10 ** 14), D(10 ** 8), lam=GROUPS["makers"]["lambda"], alpha=ALPHA, delta=DELTA)
        th2 = {"earn_at": c2["earn_at"], "no_earn_at": c2["no_earn_at"]}
        ok(c2["no_earn_at"] < c2["thr"] and [WORDS[tz23.reading(x, th2)[0]] for x in (
            c2["no_earn_at"], c2["no_earn_at"] + 1, c2["thr"] - 1, c2["thr"])] ==
           ["W-NO-EARN", "UNDECIDABLE", "UNDECIDABLE", "W-EARN"], "UNDECIDABLE between the bounds where they part")
    finally:
        for g in GROUP_ORDER:
            GROUPS[g] = saved[g]
        shutil.rmtree(tmp, ignore_errors=True)
    # the projection: each group's V and Sh at the set's size, at the formation's rates, against the Architect's
    # independent figures
    for g in GROUP_ORDER:
        vf, sf, want = PROJ[g]
        c = tz23.gate_constants(vf * N_SET / 864, sf * N_SET / 864, lam=GROUPS[g]["lambda"], alpha=ALPHA, delta=DELTA)
        ok(abs(c["thr"] - want["thr"]) < D("1e-20") and want["power"][0] < c["power"] < want["power"][1],
           "%s: at the projected V and Sh the threshold is %s and the power between %s and %s, the Architect's" % (
               g, fx(want["thr"]), want["power"][0], want["power"][1]))
    # G-REHEARSAL's comparison
    got = {"members": REF["members"], "ups": REF["ups"],
           "groups": {g: dict(REF["groups"][g]) for g in GROUP_ORDER}}
    ok(all(eq for _n, eq in compare_ref(got)) and len(compare_ref(got)) == 2 + 8 * len(GROUP_ORDER),
       "the rehearsal's %d figures compare equal to themselves" % (2 + 8 * len(GROUP_ORDER)))
    got["groups"]["takers"]["S"] += D("1e-30")
    ok([nm for nm, eq in compare_ref(got) if not eq] == ["takers S"], "one figure off by 1e-30 fails alone")
    # the clock: the idle stretch, the archive's calendar run and its service
    W = 1792458000
    idle = lambda st="inactive": (lambda: st)
    ok(quiet(W + 14, CHUNK_BUDGET_S, idle()) is not None and quiet(W + 15, CHUNK_BUDGET_S, idle()) is None and
       quiet(W + 470, CHUNK_BUDGET_S, idle()) is None and quiet(W + 471, CHUNK_BUDGET_S, idle()) is not None,
       "a chunk starts from second 15 to 470 of a window and at no other second")
    ok(quiet(W + 600, CHUNK_BUDGET_S, idle()) is not None and quiet(W + 899, CHUNK_BUDGET_S, idle()) is not None,
       "nothing starts while the pair book streams, seconds 595 to 905")
    cal = W // 86400 * 86400 + ARCHIVE_CALENDAR_S
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
    # the walk again, 300 s later, on a market too recent to be resolved; any other stop is final
    calls, slept = [], []

    def form_stops(times, msg):
        def form(base, start, spans, need):
            calls.append(start)
            if len(calls) <= times:
                raise AssertionError(msg)
            return {"start": start}
        return form

    r = walk("/nonexistent", START, (), N_SET, form=form_stops(2, "BLOCKED: the walk reached x, too recent to be "
                                                                   "resolved"),
             holdf=lambda b: (0, 0), sleep=slept.append)
    ok(r == {"start": START} and len(calls) == 3 and slept == [WALK_RETRY_S, WALK_RETRY_S],
       "a walk stopped twice on a market too recent is walked a third time, 300 s after each stop")
    calls.clear()
    try:
        walk("/nonexistent", START, (), N_SET, form=form_stops(1, "BLOCKED: 3025 considered for 1007 members"),
             holdf=lambda b: (0, 0), sleep=slept.append)
        stopped = False
    except AssertionError:
        stopped = True
    ok(stopped and len(calls) == 1, "a walk stopped on its slack is not walked again")
    # the fetch, held, on a fake chunk fetcher: each fresh chunk timed, a cached chunk fetched again by nothing
    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    try:
        os.makedirs(tmp)
        s = {"members": [{"t0": START + 300 * i, "doc": dict(good, conditionId="0x%064x" % (i + 1))}
                         for i in range(14)]}
        fetched = []

        def fake_fetch(cache, group):
            fetched.append(group[0][0])
            path = tz23.chunk_path(cache, group[0][0])
            tz23.write_atomic(path, tz23.gz_bytes(dumps({"members": [
                {"t0": t, "condition": d["conditionId"], "taker": [], "maker": []} for t, d in group]})))
            return path, True

        timing = os.path.join(tmp, "timing.jsonl")
        clk = [float(W + 20)]
        cache, groups = fetch_held(tmp, s, timing, fetcher=fake_fetch, holdf=lambda b: (clk[0], 0.0),
                                   clock=lambda: clk[0])
        recs, outside = timing_summary(timing)
        span, n14 = FILL_CHUNK * 300, -(-14 // FILL_CHUNK)
        ok(len(groups) == n14 and sorted(fetched) == [START + span * k for k in range(n14)] and len(recs) == n14
           and [len(g) for g in groups] == [FILL_CHUNK] * (n14 - 1) + [14 - FILL_CHUNK * (n14 - 1)] and not outside,
           "14 members are %d chunks of at most %d, each fetched once and timed inside the idle stretch" % (
               n14, FILL_CHUNK))
        fetched.clear()
        fetch_held(tmp, s, timing, fetcher=fake_fetch, holdf=lambda b: (clk[0], 0.0), clock=lambda: clk[0])
        ok(fetched == [] and len(timing_summary(timing)[0]) == n14, "a cached chunk is fetched again by nothing")
        ok(sum(1 for _ in member_rows2(cache, groups)) == 14, "every chunk reads back to its members")
        big = {"members": [{"t0": START + 300 * i, "doc": dict(good, conditionId="0x%064x" % (i + 1))}
                           for i in range(200)]}
        nbig = -(-200 // FILL_CHUNK)

        import threading
        gate = threading.Event()

        def slow_fetch(step, held_from=None):
            def f(cache, group):
                if held_from is not None and (group[0][0] - START) // span >= held_from:
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
                                                  "30th chunk: at most the two chunks running end, and the %d "
                                                  "queued never start" % (nbig - 34))
        fetched.clear()
        fetch_held(os.path.join(tmp, "fast"), big, os.path.join(tmp, "fast.jsonl"), fetcher=slow_fetch(10.0),
                   holdf=lambda b: (clk[0], 0.0), clock=lambda: clk[0])
        ok(len(fetched) == nbig, "a fetch projected under it fetches all %d chunks" % nbig)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
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
    # G-STILL: unchanged, or the pair book's change the archive's own restarts alone
    u0 = {"recorder": {"MainPID": "4148534", "NRestarts": "2", "ActiveState": "active"},
          "pairbook": {"MainPID": "2221487", "NRestarts": "19", "ActiveState": "active"}}
    u2 = {"recorder": dict(u0["recorder"]), "pairbook": {"MainPID": "30", "NRestarts": "21", "ActiveState": "active"}}
    chain = [{"event": "restart", "stopped": 2221487, "pid": 20, "NRestarts": "20"},
             {"event": "restart", "stopped": 20, "pid": 30, "NRestarts": "21"}]
    ok(still_reading(u0, json.loads(json.dumps(u0)), []) == (True, "unchanged") and
       still_reading(u0, u2, chain)[0] and not still_reading(u0, u2, chain[:1])[0] and
       not still_reading(u0, u2, chain[::-1])[0] and not still_reading(u0, u2, [])[0] and
       not still_reading(u0, dict(u2, recorder=dict(u0["recorder"], MainPID="1")), chain)[0],
       "G-STILL: unchanged, or the pair book moved by a chain of the archive's restart records, each one NRestarts "
       "higher; a broken, reversed or missing chain or a changed recorder fails")
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
            refused.append("tz31")
        except RuntimeError:
            refused.append("tz23")
        except OSError:
            refused.append("not refused")
    ok(refused == ["tz31", "tz31", "tz23"], "opens under the pair book's root and of the archive's ledger outside "
                                            "modes archive and still are refused by this hook, under the chain "
                                            "book's root by TZ-23's, each before it happens")
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
       policy("still", "open", (ARCHIVE_LEDGER, "rb", 0)) is None and
       policy("score", "open", (ARCHIVE_LEDGER, "rb", 0)) is not None and
       policy("archive", "open", (ARCHIVE_LEDGER, "ab", os.O_WRONLY)) is not None and
       policy("archive", "open", (ARCHIVE_STATE + "/archive.log", "rb", 0)) is not None and
       policy("archive", "os.listdir", (ARCHIVE_STATE,)) is not None,
       "modes archive and still read ledger.jsonl and nothing else of the archive's state, and write nothing there; "
       "no other mode reads it")
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
        sys.exit("usage: tz31-who-earns.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "still": mode_still,
             "archive": mode_archive, "rehearse": mode_rehearse, "fetch": mode_fetch,
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
