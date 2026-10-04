#!/usr/bin/env python3
"""TZ-21 - the recorder's memory, bounded: every check the TZ fixes, one mode per run.

    state            section 3.2  both units, both recorder trees, every copy of the three files
    synth            G-SYNTH      the old and the new recorder on synthetic histories, by slice
    equiv            G-EQUIV      the old and the new recorder on a snapshot of runtime.jsonl
    path             G-PATH       one live request per endpoint through the new recorder's functions
    mark NAME        section 3.5  an instant, with each unit's MainPID and NRestarts, in state.json
    restart          G-RESTART    one SIGTERM to the recorder, and systemd's start of the new code
    rec              G-REC        the first five qualifying intervals the new code captured, and
                                  every interval it closed before them
    final            G-FINAL      the recorder at the end of the session, then
                     G-CB-STILL   the chain book, untouched from `state` to the end
    revert           K-21         the recorder back on 4216c04 after the revert block
    reclaim TREE...  section 9    copies into the forensic store what a report names by hash

Under the recorder's capture root it opens the top-level runtime.jsonl, and a manifest.json or a
runtime.jsonl inside an interval directory G-REC compares, read-only; under the chain book's root,
nothing. An audit hook refuses any other open there and any open there for writing. It writes
under /root/tz21-work/ and, in `reclaim`, new files under /root/btc-forensics/ by exclusive
create; nothing else. The one file it removes is its own G-EQUIV snapshot, once that mode has
passed and the snapshot is shown to be the first bytes of the file it copied. It prints no
price, size, spread, mid, book level or outcome. Exit 0: every assert of the mode held. Exit 1:
an assert failed, and its message names it. Exit 3: NOT YET, with the instant to run the mode
again. Run it with the recorder's interpreter, /root/tz04a-env.

Written for CryptoTZ/TZ-21-recorder-memory.md. The TZ is the specification.
"""

import hashlib
import importlib.util
import json
import math
import os
import random
import re
import resource
import subprocess
import sys
import time
import urllib.error

if not __debug__:
    sys.stderr.write("tz21: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

REC_UNIT = "btc-recorder.service"
CB_UNIT = "btc-chainbook.service"
REC_ARGV = ["/root/tz04a-env/venv/bin/python", "-B", "-u", "recorder.py"]
CB_ARGV = ["/root/tz01-env/venv/bin/python", "-B", "-u",
           "/root/tz18a-svc/tz18a-chainbook-capture.py", "--serve"]
SVC = "/root/btc-recorder-svc"
REC_CWD = SVC + "/research/recorder"
PRIMARY = "/root/btc-5m-twap"
OLD_DIR = PRIMARY + "/research/recorder"
WORK = "/root/tz21-work"
WT = WORK + "/wt"
NEW_DIR = WT + "/research/recorder"
STATE = WORK + "/state.json"
SCRATCH = WORK + "/scratch"
REC_ROOT = "/var/lib/btc-recorder"
REC_RUNTIME = REC_ROOT + "/runtime.jsonl"
REC_SERIES = REC_ROOT + "/btc-updown-5m"
CB_ROOT = "/var/lib/btc-chainbook"
UNIT_DIR = "/etc/systemd/system"
CGROUP = "/sys/fs/cgroup/system.slice/"
FORENSICS = "/root/btc-forensics"
REPORTS = PRIMARY + "/CryptoReports"

OLD_SHA = "4216c04673ced76b5b2ac60ef57c9abedc46f9b9"
OLD_FILES = {
    "recorder.py": "9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03",
    "config.py": "8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d",
    "manifest.py": "79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045",
}
NEW_FILES = dict(OLD_FILES)
NEW_FILES["recorder.py"] = "0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7"
MEMORY_MAX = {REC_UNIT: "536870912", CB_UNIT: "201326592"}   # TZ-20's ceilings, unchanged here

KEEP_S = 7200                # RUNTIME_KEEP_S in the new recorder.py
HELD_MAX = 2000              # records the new recorder may hold after any load or prune
SYNTH_FAST_MIN = 600
SYNTH_SLOW_MIN = 60
EQUIV_STEP = 25
EQUIV_FAST_MIN = 12
EQUIV_SLOW_MIN = 200
EQUIV_RECORDS_MAX = 120000   # the most runtime records the TZ's cost bound is stated at
EQUIV_BUDGET_S = 3000        # G-EQUIV's compute budget; a run projected past it is BLOCKED
EQUIV_PROBE = 10             # slow windows timed before the projection
MEM_FLOOR = 110000000        # MemAvailable below which synth and equiv do not start
REC_UNITS = 5
REC_COMPLETE_MIN = 3
REC_LEAD_S = 60
REC_DEADLINE_S = 3900
REC_BACK_S = 3900            # how far before the restart an interval the new code closed can open
RESTART_GAP_NS = 60 * 10 ** 9
KILL_SLACK_NS = 5 * 10 ** 9
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")

OPENS = []
REC_MEMBERS = set()          # the intervals G-REC compares, once mode_rec has formed them


def _allowed(path):
    """The only files this instrument opens under a capture root."""
    if path == REC_RUNTIME:
        return True
    head, name = os.path.split(path)
    parent, interval = os.path.split(head)
    return (parent == REC_SERIES and interval.isdigit() and int(interval) in REC_MEMBERS
            and name in ("manifest.json", "runtime.jsonl"))


def _audit(event, args):
    """V12 - under either capture root only the named files are opened, and only to read."""
    if event != "open" or not args or not isinstance(args[0], str):
        return
    path = os.path.abspath(args[0])
    for root in (REC_ROOT, CB_ROOT):
        if path == root or path.startswith(root + "/"):
            mode = args[1] if len(args) > 1 else None
            flags = args[2] if len(args) > 2 else 0
            writing = (isinstance(mode, str) and any(c in mode for c in "wax+")) or \
                (isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT
                                                     | os.O_APPEND | os.O_TRUNC))
            if not _allowed(path) or writing:
                raise RuntimeError("V12: open refused under a capture root: %s %r" % (path, mode))
            OPENS.append(path)


sys.addaudithook(_audit)


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(seconds):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(seconds))


def sha256_file(path):
    """A file's SHA-256, read a mebibyte at a time, so no file is ever held whole."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_text(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def scan_runtime(path, keep=lambda rec: False):
    """One pass over a runtime.jsonl, one line in memory at a time: only the records `keep`
    accepts, in file order, the count of each kind, the torn-line count, the newline count and
    whether the file ends with a newline."""
    kept, kinds, torn, newlines, last = [], {}, 0, 0, b""
    with open(path, "rb") as fh:
        for line in fh:
            newlines += 1 if line.endswith(b"\n") else 0
            last = line
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except ValueError:
                torn += 1
                continue
            kind = rec.get("kind") if isinstance(rec, dict) else None
            kinds[kind] = kinds.get(kind, 0) + 1
            if keep(rec):
                kept.append(rec)
    return kept, kinds, torn, newlines, last.endswith(b"\n")


def is_start(rec):
    return isinstance(rec, dict) and rec.get("kind") == "start"


def head_of(tree):
    cp = subprocess.run(["git", "-C", tree, "rev-parse", "HEAD"], capture_output=True, text=True)
    assert cp.returncode == 0, "git rev-parse in %s exited %d" % (tree, cp.returncode)
    return cp.stdout.strip()


def clean(tree):
    cp = subprocess.run(["git", "-C", tree, "status", "--porcelain"], capture_output=True,
                        text=True)
    assert cp.returncode == 0, "git status in %s exited %d" % (tree, cp.returncode)
    return cp.stdout == ""


def files_equal(directory, files, label):
    for name, want in sorted(files.items()):
        got = sha256_file(os.path.join(directory, name))
        assert got == want, "%s: %s/%s sha256 %s, expected %s" % (label, directory, name, got,
                                                                  want)
    out("%s: %s, %d of %d files equal" % (label, directory, len(files), len(files)))


def not_yet(again_s, what):
    out("NOT YET: %s; run this mode again at or after %s" % (what, utc(again_s)))
    out("opens under the capture roots: %d" % len(OPENS))
    sys.exit(3)


# ---- systemd, /proc and the control group -------------------------------------------------

PROPS = ("ActiveState", "SubState", "UnitFileState", "FragmentPath", "ControlGroup", "MainPID",
         "NRestarts", "Result", "ExecMainStartTimestamp", "MemoryMax", "MemoryCurrent",
         "MemoryPeak")
MEM_FILES = ("memory.current", "memory.peak", "memory.max", "memory.swap.current",
             "memory.swap.peak", "memory.swap.max")
STAT_KEYS = ("anon", "file", "kernel", "kernel_stack", "pagetables", "sock", "shmem",
             "slab_reclaimable", "slab_unreclaimable")


def show(unit):
    cp = subprocess.run(["systemctl", "show", unit] + ["--property=" + p for p in PROPS],
                        capture_output=True, text=True)
    assert cp.returncode == 0, "systemctl show %s exited %d: %s" % (unit, cp.returncode,
                                                                    cp.stderr.strip())
    props = {}
    for line in cp.stdout.splitlines():
        key, _, value = line.partition("=")
        props[key] = value
    return props


def proc_argv(pid):
    with open("/proc/%d/cmdline" % pid, "rb") as fh:
        fields = fh.read().split(b"\0")
    if fields and fields[-1] == b"":
        fields = fields[:-1]
    return fields


def proc_argvs():
    found = {}
    for name in os.listdir("/proc"):
        if not name.isdigit():
            continue
        try:
            found[int(name)] = proc_argv(int(name))
        except OSError:
            continue
    return found


def recorder_like(found):
    """tz10b.recorder_pids's rule: every process with an argument ending in recorder.py."""
    return sorted(p for p, a in found.items() if any(x.endswith(b"recorder.py") for x in a))


def chainbook_like(found):
    return sorted(p for p, a in found.items()
                  if any(x.endswith(b"tz18a-chainbook-capture.py") for x in a))


def cgroup_paths(pid):
    with open("/proc/%d/cgroup" % pid) as fh:
        lines = fh.read().splitlines()
    return [line.split(":", 2)[2] for line in lines if line.count(":") >= 2]


def check_unit(unit, argv, cwd, restarts):
    """G-UNIT for one unit: TZ-20 section 4.1's checks, at TZ-20's MemoryMax. `restarts` None
    reads NRestarts without asserting it. Returns (MainPID, NRestarts)."""
    props = show(unit)
    out("U %s %s" % (unit, json.dumps(props, sort_keys=True)))
    for key, want in (("ActiveState", "active"), ("SubState", "running"),
                      ("UnitFileState", "enabled"), ("FragmentPath", UNIT_DIR + "/" + unit),
                      ("ControlGroup", "/system.slice/" + unit), ("MemoryMax", MEMORY_MAX[unit])):
        assert props.get(key) == want, "G-UNIT %s: %s %r, expected %r" % (unit, key,
                                                                         props.get(key), want)
    n = int(props.get("NRestarts") or -1)
    assert n >= 0, "G-UNIT %s: NRestarts %r" % (unit, props.get("NRestarts"))
    if restarts is not None:
        assert n == restarts, "G-UNIT %s: NRestarts %d, expected %d" % (unit, n, restarts)
    pid = int(props.get("MainPID") or 0)
    assert pid > 0, "G-UNIT %s: no MainPID" % unit
    got = [f.decode("utf-8") for f in proc_argv(pid)]
    assert got == argv, "G-UNIT %s: pid %d argv %r is not %r" % (unit, pid, got, argv)
    if cwd is not None:
        here = os.readlink("/proc/%d/cwd" % pid)
        assert here == cwd, "G-UNIT %s: pid %d cwd %r is not %r" % (unit, pid, here, cwd)
    paths = cgroup_paths(pid)
    assert "/system.slice/" + unit in paths, "G-UNIT %s: pid %d cgroups %r" % (unit, pid, paths)
    assert not any(p.startswith("/user.slice") for p in paths), \
        "G-UNIT %s: pid %d is inside a user slice: %r" % (unit, pid, paths)
    out("G-UNIT %s: pid %d, argv equal, cgroup /system.slice/%s, NRestarts %d, MemoryMax %s"
        % (unit, pid, unit, n, MEMORY_MAX[unit]))
    return pid, n


def sole_recorder(rec_pid):
    found = recorder_like(proc_argvs())
    assert found == [rec_pid], "recorder processes %r, expected [%d]" % (found, rec_pid)
    out("sole instance: recorder %d" % rec_pid)


def sole_chainbook(cb_pid):
    found = chainbook_like(proc_argvs())
    assert found == [cb_pid], "chain book processes %r, expected [%d]" % (found, cb_pid)
    out("sole instance: chain book %d" % cb_pid)


def meminfo():
    """The host's memory as /proc/meminfo states it, in bytes, recorded and not gated."""
    got = {}
    for line in read_text("/proc/meminfo").splitlines():
        key, _, rest = line.partition(":")
        if key in ("MemTotal", "MemAvailable", "SwapTotal", "SwapFree"):
            got[key] = int(rest.split()[0]) * 1024
    out("H /proc/meminfo %s" % json.dumps(got, sort_keys=True))
    return got


def memory(unit):
    """The unit's control-group memory files as the kernel writes them, recorded and not gated."""
    base = CGROUP + unit + "/"
    got = {}
    for name in MEM_FILES:
        path = base + name
        got[name] = read_text(path).strip() if os.path.exists(path) else None
    stat = {}
    if os.path.exists(base + "memory.stat"):
        for line in read_text(base + "memory.stat").splitlines():
            key, _, value = line.partition(" ")
            if key in STAT_KEYS:
                stat[key] = int(value)
    got["memory.stat"] = stat
    out("M %s %s" % (unit, json.dumps(got, sort_keys=True)))
    return got


# ---- state.json ----------------------------------------------------------------------------

def load_state():
    with open(STATE, encoding="utf-8") as fh:
        return json.load(fh)


def save_state(state):
    tmp = STATE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(state, sort_keys=True) + "\n")
    os.replace(tmp, STATE)


# ---- the two recorders ---------------------------------------------------------------------

def load_recorder(directory, name, files):
    """recorder.py from one directory under its own module name, every file hash-asserted first.
    config and manifest are imported once and shared: they are byte-identical in both copies."""
    files_equal(directory, files, "load %s" % name)
    if directory not in sys.path:
        sys.path.insert(0, directory)
    spec = importlib.util.spec_from_file_location(name, os.path.join(directory, "recorder.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for dep in ("config", "manifest"):
        loaded = os.path.realpath(sys.modules[dep].__file__)
        assert sha256_file(loaded) == files[dep + ".py"], "%s loaded from %s" % (dep, loaded)
    return mod


def instance(mod, runtime_path, sha):
    """A Recorder of `mod` reading `runtime_path`; nothing else of it runs. `sha` is the start
    record a window with no start before it would name: the same string for both copies."""
    rec = mod.Recorder()
    rec.runtime_path = runtime_path
    rec.sha = sha
    return rec


def slice_bytes(rec, t0, directory):
    os.makedirs(directory, exist_ok=True)
    rec.write_runtime_slice(t0, directory)
    with open(os.path.join(directory, "runtime.jsonl"), "rb") as fh:
        return fh.read()


def window_of(t0):
    return (t0 - 90) * 10 ** 9, (t0 + 330) * 10 ** 9


# ---- G-SYNTH ---------------------------------------------------------------------------------

SYN_BASE = 1791000000        # a synthetic epoch on the 300 s grid


def syn_clock(t_ns, i, rng):
    return {"kind": "clock", "recv_ns": t_ns, "server": ("108.61.73.243", "pool.ntp.org")[i % 2],
            "ip": "193.70.94.%d" % (i % 250), "burst": 4,
            "offset_ms": rng.uniform(-30.0, 30.0), "rtt_ms": rng.uniform(0.5, 100.0),
            "rejected": {}, "rejected_count": 0}


def syn_events(t_from, t_to, rng, first=0):
    """(write_ns, record) in write order: a clock sample every 30 s, a reconnect every 7,200 s."""
    events, i = [], first
    t = t_from
    while t < t_to:
        t_ns = t * 10 ** 9 + rng.randrange(10 ** 9)
        events.append((t_ns, syn_clock(t_ns, i, rng)))
        if (t - SYN_BASE) % 7200 == 3570:
            end = t_ns + 2 * 10 ** 9
            events.append((end, {"kind": "disconnect", "start_recv_ns": t_ns - 10 ** 9,
                                 "detected_recv_ns": t_ns + 10 ** 9, "end_recv_ns": end,
                                 "reason": "reconnect"}))
        i += 1
        t += 30
    return events, i


class Pair:
    """An old and a new recorder process, each writing its own copy of one runtime.jsonl."""

    def __init__(self, old_mod, new_mod, base, now_ns):
        self.base = base
        for side in ("old", "new"):
            os.makedirs(os.path.join(base, side), exist_ok=True)
        self.old = instance(old_mod, os.path.join(base, "old", "runtime.jsonl"), "s" * 40)
        self.new = instance(new_mod, os.path.join(base, "new", "runtime.jsonl"), "s" * 40)
        self.old.load_runtime()
        self.new.load_runtime(now_ns=now_ns)
        self.fast = self.slow = self.held = 0
        self.check_held()

    def record(self, rec):
        self.old.record(dict(rec))
        self.new.record(dict(rec))

    def check_held(self):
        self.held = max(self.held, len(self.new.runtime))
        assert len(self.new.runtime) <= HELD_MAX, "G-SYNTH: the new recorder holds %d records" % (
            len(self.new.runtime))

    def compare(self, t0, now_ns, prune=True):
        lo, _hi = window_of(t0)
        fast = lo >= self.new.runtime_from_ns
        a = slice_bytes(self.old, t0, os.path.join(self.base, "slice-old"))
        b = slice_bytes(self.new, t0, os.path.join(self.base, "slice-new"))
        assert a == b, "G-SYNTH: window %d differs (%s path)" % (t0, "fast" if fast else "slow")
        if fast:
            self.fast += 1
        else:
            self.slow += 1
        if prune:
            self.new.prune_runtime(now_ns=now_ns)
            self.check_held()

    def files_equal(self):
        with open(self.old.runtime_path, "rb") as fa, open(self.new.runtime_path, "rb") as fb:
            assert fa.read() == fb.read(), "G-SYNTH: the two runtime files differ"


def write_raw(path, lines):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        for line in lines:
            fh.write(line)


def run_live(pair, events, t0_from, t0_to, rng, delays, old_every=0):
    """Replays `events` and closes every window T0 in [t0_from, t0_to) at T0 + a delay, in time
    order, as close_interval does: the slice, then the prune. Every `old_every`-th close also
    slices a window a day older, which the new recorder serves from disk."""
    closes = []
    for k, t0 in enumerate(range(t0_from, t0_to, 300)):
        closes.append(((t0 + delays[k % len(delays)]) * 10 ** 9, t0))
    queue = sorted([(t, 0, r) for t, r in events] + [(t, 1, t0) for t, t0 in closes],
                   key=lambda e: (e[0], e[1]))
    n = 0
    for t_ns, kind, item in queue:
        if kind == 0:
            pair.record(item)
        else:
            pair.compare(item, t_ns)
            n += 1
            if old_every and n % old_every == 0:
                pair.compare(item - 86400, t_ns, prune=False)
    return n


def mode_synth():
    avail = meminfo()["MemAvailable"]
    assert avail >= MEM_FLOOR, "BLOCKED: MemAvailable %d bytes, below the floor of %d" % (
        avail, MEM_FLOOR)
    old = load_recorder(OLD_DIR, "recorder_old", OLD_FILES)
    new = load_recorder(NEW_DIR, "recorder_new", NEW_FILES)
    assert new.RUNTIME_KEEP_S == KEEP_S, "G-SYNTH: RUNTIME_KEEP_S %r" % new.RUNTIME_KEEP_S
    assert not hasattr(old.Recorder, "prune_runtime"), "G-SYNTH: the old copy is not 4216c04's"
    rng = random.Random(21)
    base = os.path.join(SCRATCH, "synth-%d" % time.time_ns())    # a fresh tree for every run
    os.makedirs(base)
    delays = (333, 633, 1833, 3633, 348, 3333)
    totals = {"fast": 0, "slow": 0, "held": 0, "old_held": 0}

    def tally(p):
        totals["fast"] += p.fast
        totals["slow"] += p.slow
        totals["held"] = max(totals["held"], p.held)
        totals["old_held"] = max(totals["old_held"], len(p.old.runtime))

    # 1. steady: three days already on disk, a process starts, two days run, windows close late
    #    and out of order, and a day-old window is sliced at every tenth close.
    s1 = os.path.join(base, "steady")
    t_start = SYN_BASE + 3 * 86400
    pre, i = syn_events(SYN_BASE, t_start, rng)
    start = {"kind": "start", "recv_ns": t_start * 10 ** 9, "sha": "a" * 40,
             "free_bytes": 1, "captured_bytes": 1}
    lines = [json.dumps(r, sort_keys=True) + "\n" for _t, r in pre]
    for side in ("old", "new"):
        write_raw(os.path.join(s1, side, "runtime.jsonl"), lines)
    del pre, lines
    pair = Pair(old, new, s1, t_start * 10 ** 9 + 5 * 10 ** 8)
    pair.record(start)
    live, i = syn_events(t_start, t_start + 2 * 86400, rng, i)
    n1 = run_live(pair, live, t_start + 300, t_start + 2 * 86400 - 3900, rng, delays, 10)
    pair.files_equal()
    out("G-SYNTH steady: %d closes, %d fast and %d slow slices equal; held at most %d records, "
        "the old recorder %d" % (n1, pair.fast, pair.slow, pair.held, len(pair.old.runtime)))
    last_frame = live[-1][0]
    tally(pair)
    del pair, live

    # 2. an outage of 158,581 s, then a restart: both recover the two windows open at the crash
    #    and the one before them, from disk, then run three hours.
    crash = t_start + 2 * 86400
    restart = crash + 158581
    t_restart = restart * 10 ** 9
    pair2 = Pair(old, new, s1, t_restart)
    pair2.record({"kind": "start", "recv_ns": t_restart, "sha": "b" * 40, "free_bytes": 1,
                  "captured_bytes": 1})
    for t0 in (crash - crash % 300 - 300, crash - crash % 300, crash - crash % 300 - 600):
        pair2.compare(t0, t_restart + 10 ** 9)
    pair2.record({"kind": "disconnect", "start_recv_ns": last_frame,
                  "detected_recv_ns": t_restart + 10 ** 9, "end_recv_ns": t_restart + 3 * 10 ** 9,
                  "reason": "startup"})
    later, i = syn_events(restart + 3, restart + 3 * 3600 + 3, rng, i)
    t0_first = restart - restart % 300 + 300
    n2 = run_live(pair2, later, t0_first, restart + 3 * 3600 - 3900, rng, delays, 4)
    for t0 in range(crash - crash % 300 - 1500, crash - crash % 300 + 300, 300):
        pair2.compare(t0, (restart + 3 * 3600) * 10 ** 9, prune=False)
    pair2.files_equal()
    out("G-SYNTH outage: %d recovered and %d live closes, %d fast and %d slow slices equal; held "
        "at most %d records" % (3, n2, pair2.fast, pair2.slow, pair2.held))
    tear_paths = (pair2.old.runtime_path, pair2.new.runtime_path)
    tally(pair2)
    del pair2, later

    # 3. a torn tail: the old process dies mid-line, the next start lands on the same line, and the
    #    windows on both sides of it are sliced by both.
    tear = restart + 3 * 3600 + 3
    for path in tear_paths:
        write_raw(path, ['{"kind": "clock", "recv_ns": %d, "ser' % (tear * 10 ** 9)])
    t_ns3 = (tear + 600) * 10 ** 9
    pair3 = Pair(old, new, s1, t_ns3)
    pair3.record({"kind": "start", "recv_ns": t_ns3, "sha": "c" * 40, "free_bytes": 1,
                  "captured_bytes": 1})
    more, i = syn_events(tear + 601, tear + 601 + 2 * 3600, rng, i)
    n3 = run_live(pair3, more, tear - tear % 300 + 900, tear + 601 + 2 * 3600 - 3900, rng,
                  delays, 3)
    for t0 in range(tear - tear % 300 - 900, tear - tear % 300 + 900, 300):
        pair3.compare(t0, (tear + 601 + 2 * 3600) * 10 ** 9, prune=False)
    _kept, _kinds, torn, _n, _t = scan_runtime(pair3.new.runtime_path)
    assert torn == 1, "G-SYNTH: the torn tail left %d torn lines" % torn
    pair3.files_equal()
    out("G-SYNTH torn tail: %d closes, %d fast and %d slow slices equal" % (n3, pair3.fast,
                                                                              pair3.slow))
    tally(pair3)
    del pair3, more

    # 4. ten days of one process: what it holds stays bounded while the old copy grows.
    s4 = os.path.join(base, "days")
    t4 = SYN_BASE
    pair4 = Pair(old, new, s4, t4 * 10 ** 9)
    pair4.record({"kind": "start", "recv_ns": t4 * 10 ** 9, "sha": "d" * 40, "free_bytes": 1,
                  "captured_bytes": 1})
    # The events are generated a day at a time, so only one day of them is ever held; the days
    # draw from the generator in the same order a single call would, so every value is the same.
    days = [(t4 + 1 + d * 86400, min(t4 + 1 + (d + 1) * 86400, t4 + 10 * 86400))
            for d in range(10)]
    queue, j, k = [], 0, 0
    for t0 in range(t4 + 300, t4 + 10 * 86400 - 3900, 300):
        close_ns = (t0 + 333) * 10 ** 9
        while True:
            if j == len(queue):
                if not days:
                    break
                queue, i = syn_events(days[0][0], days[0][1], rng, i)
                days.pop(0)
                j = 0
                continue
            if queue[j][0] > close_ns:
                break
            pair4.record(queue[j][1])
            j += 1
        k += 1
        if k % 12 == 0:
            pair4.compare(t0, close_ns)
        else:
            pair4.new.prune_runtime(now_ns=close_ns)
            pair4.check_held()
    while days:                     # the draws the days not reached take, as one call made them
        _rest, i = syn_events(days[0][0], days[0][1], rng, i)
        days.pop(0)
    pair4.files_equal()
    assert len(pair4.old.runtime) >= 9 * 2880, "G-SYNTH: the old copy holds %d" % (
        len(pair4.old.runtime))
    out("G-SYNTH ten days: %d closes, %d slices equal; the new recorder held at most %d records, "
        "the old %d at the end" % (k, pair4.fast + pair4.slow, pair4.held, len(pair4.old.runtime)))
    tally(pair4)
    del pair4, queue

    # 5. negative controls: the comparison sees a record missing from memory on the fast path,
    #    and a record missing from the file on the slow path.
    s5 = os.path.join(base, "controls")
    t5 = SYN_BASE + 86400
    pre5, i = syn_events(SYN_BASE, t5, rng, i)
    lines5 = [json.dumps(r, sort_keys=True) + "\n" for _t, r in pre5]
    for side in ("old", "new"):
        write_raw(os.path.join(s5, side, "runtime.jsonl"), lines5)
    pair5 = Pair(old, new, s5, t5 * 10 ** 9)
    pair5.record({"kind": "start", "recv_ns": t5 * 10 ** 9, "sha": "e" * 40, "free_bytes": 1,
                  "captured_bytes": 1})
    tail5, i = syn_events(t5 + 1, t5 + 3600, rng, i)
    for _t, r in tail5:
        pair5.record(r)
    recent, aged = t5 + 1800 - (t5 + 1800) % 300, t5 - 43200 - (t5 - 43200) % 300
    pair5.compare(recent, (t5 + 3600) * 10 ** 9, prune=False)
    pair5.compare(aged, (t5 + 3600) * 10 ** 9, prune=False)
    held = pair5.new.runtime
    pair5.new.runtime = [r for r in held if r.get("kind") != "clock"]
    try:
        pair5.compare(recent, (t5 + 3600) * 10 ** 9, prune=False)
        nc1 = False
    except AssertionError:
        nc1 = True
    pair5.new.runtime = held
    with open(pair5.new.runtime_path, encoding="utf-8") as fh:
        kept_lines = fh.readlines()
    dropped = [ln for ln in kept_lines
               if not (json.loads(ln).get("kind") == "clock"
                       and (aged - 90) * 10 ** 9 <= json.loads(ln)["recv_ns"]
                       <= (aged + 330) * 10 ** 9)]
    with open(pair5.new.runtime_path, "w", encoding="utf-8") as fh:
        fh.writelines(dropped)
    try:
        pair5.compare(aged, (t5 + 3600) * 10 ** 9, prune=False)
        nc2 = False
    except AssertionError:
        nc2 = True
    assert nc1 and nc2, "G-SYNTH: a negative control was not detected (fast %s, slow %s)" % (
        nc1, nc2)
    out("G-SYNTH negative controls: a clock missing from memory on the fast path and from the "
        "file on the slow path are each detected, 2 of 2 (%d lines removed)"
        % (len(kept_lines) - len(dropped)))

    assert totals["fast"] >= SYNTH_FAST_MIN and totals["slow"] >= SYNTH_SLOW_MIN, \
        "G-SYNTH: only %d fast and %d slow slices" % (totals["fast"], totals["slow"])
    out("G-SYNTH PASS: %d slices equal, %d fast and %d slow; the new recorder held at most %d "
        "records, the old %d" % (totals["fast"] + totals["slow"], totals["fast"], totals["slow"],
                                 totals["held"], totals["old_held"]))


# ---- G-EQUIV --------------------------------------------------------------------------------

class Sink:
    """Takes what load_runtime appends and keeps a count and a digest of it, not the list."""

    def __init__(self):
        self.n = 0
        self._h = hashlib.sha256()

    def append(self, rec):
        self.n += 1
        self._h.update(json.dumps(rec, sort_keys=True).encode("utf-8") + b"\n")

    def digest(self):
        return self._h.hexdigest()


def equiv_windows(records, snap_s):
    """The windows G-EQUIV slices, every one ending before the snapshot: every EQUIV_STEP-th of
    the capture's span, every one the new recorder serves from memory, the first and the last
    window each disconnect overlaps, and every window within 600 s of a start record."""
    starts = sorted(r["recv_ns"] for r in records if r.get("kind") == "start")
    assert starts, "G-EQUIV: no start record"
    first = (starts[0] // 10 ** 9) - (starts[0] // 10 ** 9) % 300 + 300
    last = snap_s - 330
    last -= last % 300
    span = list(range(first, last + 1, 300))
    chosen = set(span[::EQUIV_STEP])
    chosen.update(t for t in span if (t - 90) * 10 ** 9 >= snap_s * 10 ** 9 - KEEP_S * 10 ** 9)
    for r in records:
        if r.get("kind") != "disconnect":
            continue
        a, c = r["start_recv_ns"] // 10 ** 9, r["end_recv_ns"] // 10 ** 9
        hit = [t for t in span if t - 90 <= c and t + 330 >= a]
        chosen.update(hit[:1] + hit[-1:])
    for s in starts:
        s //= 10 ** 9
        chosen.update(t for t in span if t - 90 <= s + 600 and t + 330 >= s - 600)
    return sorted(chosen), len(span)


def mode_equiv():
    avail = meminfo()["MemAvailable"]
    assert avail >= MEM_FLOOR, "BLOCKED: MemAvailable %d bytes, below the floor of %d" % (
        avail, MEM_FLOOR)
    old = load_recorder(OLD_DIR, "recorder_old", OLD_FILES)
    new = load_recorder(NEW_DIR, "recorder_new", NEW_FILES)
    assert new.RUNTIME_KEEP_S == KEEP_S, "G-EQUIV: RUNTIME_KEEP_S %r" % new.RUNTIME_KEEP_S
    base = os.path.join(SCRATCH, "equiv-%d" % time.time_ns())    # a fresh tree for every run
    os.makedirs(base)
    snap = os.path.join(base, "runtime.jsonl")
    snap_ns = time.time_ns()
    h, size = hashlib.sha256(), 0
    with open(REC_RUNTIME, "rb") as src, open(snap, "xb") as dst:
        for chunk in iter(lambda: src.read(1 << 20), b""):
            dst.write(chunk)
            h.update(chunk)
            size += len(chunk)
    digest = h.hexdigest()
    out("G-EQUIV snapshot of %s at %s: %d bytes, sha256 %s"
        % (REC_RUNTIME, utc(snap_ns / 1e9), size, digest))
    n = instance(new, snap, OLD_SHA)
    n.load_runtime(now_ns=snap_ns)
    assert len(n.runtime) <= HELD_MAX, "G-EQUIV: the new recorder holds %d" % len(n.runtime)
    # The old recorder's own load_runtime, into a sink that keeps the count and a digest of the
    # list it builds rather than the list; one parse of the snapshot must give the same two.
    o = instance(old, snap, OLD_SHA)
    o.runtime = Sink()
    o.load_runtime()
    parsed = Sink()

    def marks(rec):
        parsed.append(rec)
        return isinstance(rec, dict) and rec.get("kind") in ("start", "disconnect")
    starts_and_gaps, _kinds, torn, _newlines, _t = scan_runtime(snap, marks)
    assert (o.runtime.n, o.runtime.digest()) == (parsed.n, parsed.digest()), \
        "G-EQUIV: the old load holds %d records, the parse %d" % (o.runtime.n, parsed.n)
    old_held = o.runtime.n
    windows, span = equiv_windows(starts_and_gaps, snap_ns // 10 ** 9)
    # Every record any chosen window's old slice can select, in file order: every start, every
    # clock inside a chosen window, every disconnect overlapping one. The old code's own filter
    # then picks from these exactly what it picks from the whole list.
    chosen = set(windows)
    bounds = [window_of(t) for t in windows]

    def selectable(rec):
        if not isinstance(rec, dict):
            return True
        kind = rec.get("kind")
        if kind == "start":
            return True
        if kind == "clock":
            x = rec.get("recv_ns")
            if not isinstance(x, int):
                return True             # the old code meets it as it would in the whole list
            base = (x // 10 ** 9) - (x // 10 ** 9) % 300
            return any(t in chosen and window_of(t)[0] <= x <= window_of(t)[1]
                       for t in (base - 300, base, base + 300))
        if kind == "disconnect":
            a, c = rec.get("start_recv_ns"), rec.get("end_recv_ns")
            if not (isinstance(a, int) and isinstance(c, int)):
                return True
            return any(a <= hi and c >= lo for lo, hi in bounds)
        return False
    o.runtime, _kinds, _torn, _newlines, _t = scan_runtime(snap, selectable)
    out("G-EQUIV loaded: the old load holds %d records (%d torn lines skipped), count and digest "
        "equal to the parse; the old slices read the %d of them the chosen windows can select; "
        "the new recorder holds %d, from %s on" % (old_held, torn, len(o.runtime), len(n.runtime),
                                                   utc(n.runtime_from_ns / 1e9)))
    fast = slow = 0
    slow_total = sum(1 for t in windows if window_of(t)[0] < n.runtime_from_ns)
    t_start = time.monotonic()
    for t0 in windows:
        lo, _hi = window_of(t0)
        a = slice_bytes(o, t0, os.path.join(base, "slice-old"))
        b = slice_bytes(n, t0, os.path.join(base, "slice-new"))
        assert a == b, "G-EQUIV: window %d %s differs" % (t0, utc(t0))
        if lo >= n.runtime_from_ns:
            fast += 1
        else:
            slow += 1
            if slow == EQUIV_PROBE:
                spent = time.monotonic() - t_start
                projected = spent / (fast + slow) * len(windows)
                out("G-EQUIV projected %.0f s for %d windows, %d of them slow, after %.1f s"
                    % (projected, len(windows), slow_total, spent))
                if projected > EQUIV_BUDGET_S:
                    raise SystemExit("G-EQUIV BLOCKED: projected %.0f s against the budget of %d s"
                                     % (projected, EQUIV_BUDGET_S))
    out("G-EQUIV windows: %d of the span's %d, %s to %s, in %.1f s"
        % (len(windows), span, utc(windows[0]), utc(windows[-1]), time.monotonic() - t_start))
    assert fast >= EQUIV_FAST_MIN and slow >= EQUIV_SLOW_MIN, \
        "G-EQUIV: only %d fast and %d slow windows" % (fast, slow)
    # The capture appends and never rewrites, so the snapshot is the file's first `size` bytes
    # for good: shown here, then the copy goes, and anyone re-derives it from the capture.
    h, left = hashlib.sha256(), size
    with open(REC_RUNTIME, "rb") as fh:
        for chunk in iter(lambda: fh.read(min(left, 1 << 20)), b""):
            h.update(chunk)
            left -= len(chunk)
    assert left == 0 and h.hexdigest() == digest, \
        "G-EQUIV: %s no longer begins with the snapshot" % REC_RUNTIME
    os.remove(snap)
    out("G-EQUIV the snapshot is the first %d bytes of %s, sha256 %s; the copy is removed"
        % (size, REC_RUNTIME, digest))
    out("G-EQUIV PASS: %d windows equal, %d fast and %d slow; the new recorder holds %d records "
        "against the old %d" % (fast + slow, fast, slow, len(n.runtime), old_held))


# ---- G-PATH ---------------------------------------------------------------------------------

def mode_path():
    import asyncio
    head = load_state()["branch_head"]
    got = head_of(SVC)
    assert got == head, "P0: %s is at %s, the branch at %s" % (SVC, got, head)
    rec = load_recorder(REC_CWD, "recorder", NEW_FILES)
    import config
    import websockets
    src = os.path.realpath(rec.__file__)
    assert src == os.path.join(REC_CWD, "recorder.py"), "P0: recorder loaded from %s" % src
    sha = rec.git_sha()
    assert sha == head, "P0: git_sha() %r" % sha
    out("P0 recorder.py %s, git_sha %s, websockets %s, User-Agent %r"
        % (src, sha, websockets.__version__, config.USER_AGENT))

    now = int(time.time())
    t0 = now - now % config.INTERVAL_S
    if now - t0 < 30:
        t0 -= config.INTERVAL_S
    url = config.GAMMA_MARKET_BY_SLUG.format(slug=config.slug_for(t0))
    try:
        body = rec.fetch(url)
    except urllib.error.HTTPError as exc:
        raise AssertionError("P1: %s answered HTTP %d" % (url, exc.code))
    doc = json.loads(body)
    market = doc[0] if isinstance(doc, list) else doc
    ids = json.loads(market["clobTokenIds"])
    assert isinstance(ids, list) and len(ids) == 2 and all(ids), "P1: clobTokenIds %r" % (ids,)
    out("P1 %s: served, %d bytes, JSON, token ids %s" % (url, len(body), ids))

    book = config.CLOB_BOOK_BY_TOKEN.format(token_id=ids[0])
    status, text = rec.fetch_status(book, rec.QUOTE_TIMEOUT_S)
    assert status == 200, "P2: %s status %r" % (book, status)
    json.loads(text)
    out("P2 %s: status %d, %d bytes, JSON" % (book, status, len(text.encode("utf-8"))))

    answered = 0
    for host in config.NTP_SERVERS:
        try:
            ip, offset, rtt, accepted, rejected = rec.sntp_best(host)
        except Exception as exc:
            out("P3 SNTP %s: no reply (%s)" % (host, type(exc).__name__))
            continue
        if offset is None:
            out("P3 SNTP %s (%s): 0 accepted, rejected %s" % (host, ip, rejected))
            continue
        answered += 1
        out("P3 SNTP %s (%s): %d accepted, offset %.3f ms, rtt %.3f ms, rejected %s"
            % (host, ip, accepted, offset * 1000.0, rtt * 1000.0, rejected))
    assert answered >= 1, "P3: no SNTP server answered"

    async def rtds():
        # recorder.py's rtds(), in effect: the same subscription message from config.TIER_A,
        # the same URL and the same connect arguments.
        subs = [{"topic": t, "type": "*", "filters": f}
                for t, (f, _s) in config.TIER_A.items()]
        message = json.dumps({"action": "subscribe", "subscriptions": subs})
        topics, frames = set(), 0
        async with websockets.connect(config.RTDS_URL, open_timeout=20,
                                      ping_interval=None, max_size=None) as ws:
            await ws.send(message)
            deadline = time.monotonic() + 30
            while time.monotonic() < deadline and topics != set(config.TIER_A):
                try:
                    raw = await asyncio.wait_for(ws.recv(),
                                                 timeout=max(0.1, deadline - time.monotonic()))
                except asyncio.TimeoutError:
                    break
                if isinstance(raw, bytes):
                    raw = raw.decode("utf-8", "replace")
                if not raw or raw.strip() in ("PONG", "PING"):
                    continue
                frames += 1
                try:
                    topic = json.loads(raw).get("topic")
                except Exception:
                    continue
                if topic in config.TIER_A:
                    topics.add(topic)
        return topics, frames

    topics, frames = asyncio.run(rtds())
    out("P4 %s: %d frames in at most 30 s, topics %s" % (config.RTDS_URL, frames, sorted(topics)))
    need = {"crypto_prices_twap_sixty", "crypto_prices_chainlink"}
    assert need <= topics, "P4: topics %r lack %r" % (sorted(topics), sorted(need - topics))
    out("G-PATH PASS: P0 to P4")


# ---- state, marks, the restart, G-REC, the end ----------------------------------------------

def mode_state():
    assert not os.path.exists(STATE), "state: %s exists" % STATE
    head = head_of(WT)
    assert head != OLD_SHA, "S6: the branch is at %s" % head
    rec_pid, rec_n = check_unit(REC_UNIT, REC_ARGV, REC_CWD, None)
    cb_pid, cb_n = check_unit(CB_UNIT, CB_ARGV, None, None)
    sole_recorder(rec_pid)
    sole_chainbook(cb_pid)
    out("S1 S2 both units active: recorder pid %d NRestarts %d, chain book pid %d NRestarts %d"
        % (rec_pid, rec_n, cb_pid, cb_n))
    starts, kinds, torn, newlines, terminated = scan_runtime(REC_RUNTIME, is_start)
    assert starts, "S3: %s holds no start record" % REC_RUNTIME
    records = sum(kinds.values())
    starts.sort(key=lambda r: r["recv_ns"])
    out("S3 %s: %d newlines, %d records %s, %d torn, ends with a newline %s"
        % (REC_RUNTIME, newlines, records, json.dumps(kinds, sort_keys=True), torn, terminated))
    out("S3 newest start %s" % json.dumps(starts[-1], sort_keys=True))
    assert starts[-1].get("sha") == OLD_SHA, "S3: the newest start names %r" % starts[-1]
    assert records <= EQUIV_RECORDS_MAX, "S3: %d records, above the %d the TZ is costed at" % (
        records, EQUIV_RECORDS_MAX)
    got = head_of(SVC)
    assert got == OLD_SHA, "S4: %s is at %s" % (SVC, got)
    files_equal(REC_CWD, OLD_FILES, "S4 the unit's tree")
    assert clean(SVC), "S4: %s has local changes" % SVC
    files_equal(OLD_DIR, OLD_FILES, "S5 the primary checkout")
    files_equal(NEW_DIR, NEW_FILES, "S6 the branch")
    for path in (REC_ARGV[0], CB_ARGV[0]):
        assert os.access(path, os.X_OK), "S7: %s is not executable" % path
        out("S7 %s executable" % path)
    memory(REC_UNIT)
    memory(CB_UNIT)
    meminfo()
    os.makedirs(SCRATCH, exist_ok=True)
    save_state({"branch_head": head, "state_ns": time.time_ns(), "rec_pid": rec_pid,
                "rec_restarts": rec_n, "cb_pid": cb_pid, "cb_restarts": cb_n,
                "records": records, "marks": {}})
    out("STATE PASS: S1 to S7, the branch at %s" % head)


def mode_mark(name):
    assert name in ("kill-rec", "revert"), "mark %r" % name
    state = load_state()
    assert name not in state["marks"], "mark %r already recorded" % name
    rp, cp = show(REC_UNIT), show(CB_UNIT)
    state["marks"][name] = {"ns": time.time_ns(), "rec_pid": int(rp.get("MainPID") or 0),
                            "rec_restarts": int(rp.get("NRestarts") or 0),
                            "cb_pid": int(cp.get("MainPID") or 0),
                            "cb_restarts": int(cp.get("NRestarts") or 0)}
    save_state(state)
    out("MARK %s %s (%s)" % (name, json.dumps(state["marks"][name], sort_keys=True),
                             utc(state["marks"][name]["ns"] / 1e9)))


def records_since(since_ns):
    def keep(r):
        if not isinstance(r, dict):
            return False
        if r.get("kind") in ("start", "halt"):
            return r.get("recv_ns", 0) >= since_ns
        return (r.get("kind") == "disconnect" and r.get("reason") == "startup"
                and r.get("detected_recv_ns", 0) >= since_ns)
    recs, _kinds, torn, _n, _t = scan_runtime(REC_RUNTIME, keep)
    starts = sorted((r for r in recs if r["kind"] == "start"), key=lambda r: r["recv_ns"])
    ups = sorted((r for r in recs if r["kind"] == "disconnect"),
                 key=lambda r: r["detected_recv_ns"])
    halts = [r for r in recs if r["kind"] == "halt"]
    for r in starts + ups + halts:
        out("R %s" % json.dumps(r, sort_keys=True))
    return starts, ups, halts, torn


def check_restart(label, mark, sha, restarts, gap_from_ns, gap_max_ns):
    """One start record since the mark, on `sha`; no halt; a MainPID other than the mark's;
    NRestarts `restarts` (None: recorded). With gap_from_ns, also one startup gap detected since
    the mark, which began no earlier than gap_from_ns and lasted at most gap_max_ns; without it,
    the gaps are printed and not asserted."""
    starts, ups, halts, torn = records_since(mark["ns"])
    assert len(starts) == 1, "%s: %d start records since the mark" % (label, len(starts))
    st = starts[0]
    assert st.get("sha") == sha, "%s: the start record names %r" % (label, st.get("sha"))
    if gap_from_ns is not None:
        assert len(ups) == 1, "%s: %d startup gaps since the mark" % (label, len(ups))
        up = ups[0]
        assert gap_from_ns <= up["start_recv_ns"] <= st["recv_ns"] \
            <= up["detected_recv_ns"] <= up["end_recv_ns"], "%s: gap %r, start %d, bound %d" % (
                label, up, st["recv_ns"], gap_from_ns)
        gap = up["end_recv_ns"] - up["start_recv_ns"]
        assert 0 <= gap <= gap_max_ns, "%s: the gap is %d ns" % (label, gap)
        gaps = "the gap %s to %s, %.3f s" % (utc(up["start_recv_ns"] / 1e9),
                                            utc(up["end_recv_ns"] / 1e9), gap / 1e9)
    else:
        gaps = "%d startup gaps since the mark, recorded" % len(ups)
    assert not halts, "%s: halt records %r" % (label, halts)
    pid, n = check_unit(REC_UNIT, REC_ARGV, REC_CWD, restarts)
    assert pid != mark["rec_pid"], "%s: the same pid %d" % (label, pid)
    out("%s: pid %d replaced by %d, NRestarts %d; the start %s on %s; %s; %d torn"
        % (label, mark["rec_pid"], pid, n, utc(st["recv_ns"] / 1e9), sha, gaps, torn))
    return pid, st


def mode_restart():
    state = load_state()
    mark, head = state["marks"]["kill-rec"], state["branch_head"]
    assert head_of(SVC) == head, "G-RESTART: %s is not at the branch" % SVC
    pid, st = check_restart("G-RESTART", mark, head, mark["rec_restarts"] + 1,
                            mark["ns"] - KILL_SLACK_NS, RESTART_GAP_NS)
    sole_recorder(pid)
    memory(REC_UNIT)
    state["restart"] = {"pid": pid, "start_ns": st["recv_ns"],
                        "restarts": mark["rec_restarts"] + 1}
    save_state(state)
    cb = show(CB_UNIT)
    out("G-RESTART the chain book, recorded and judged by G-CB-STILL: pid %s, NRestarts %s"
        % (cb.get("MainPID"), cb.get("NRestarts")))
    out("G-RESTART PASS: the recorder runs the new code as pid %d" % pid)


def written_ns(rec):
    """The instant a record reached runtime.jsonl: each kind is written when its stamp is taken."""
    if rec.get("kind") == "disconnect":
        return rec.get("end_recv_ns", 0)
    return rec.get("recv_ns", 0)


def manifest_path(t):
    return "%s/%d/manifest.json" % (REC_SERIES, t)


def mode_rec():
    state = load_state()
    r, head = state["restart"], state["branch_head"]
    r0 = r["start_ns"] / 1e9
    first = math.ceil((r0 + REC_LEAD_S + 90) / 300) * 300
    members = [first + 300 * k for k in range(REC_UNITS)]
    missing = [t for t in members if not os.path.exists(manifest_path(t))]
    if missing and time.time() < max(t + REC_DEADLINE_S for t in missing):
        not_yet(time.time() + 300, "intervals %s pending, the last deadline %s"
                % (missing, utc(max(t + REC_DEADLINE_S for t in missing))))
    # Every interval the new code closed before the members: recovered at its start, or open
    # across the restart. Its manifest was written at or after the new start record.
    earlier = []
    t = int(r0 - REC_BACK_S) - int(r0 - REC_BACK_S) % 300
    while t < first:
        path = manifest_path(t)
        if os.path.exists(path) and os.stat(path).st_mtime_ns >= r["start_ns"]:
            earlier.append(t)
        t += 300
    present_members = [t for t in members if t not in missing]
    compared = earlier + present_members
    REC_MEMBERS.update(compared)
    old = load_recorder(OLD_DIR, "recorder_old", OLD_FILES)
    o = instance(old, REC_RUNTIME, head)
    windows = [window_of(t) for t in compared]

    def selectable(rec):
        """Every record the old slice of a compared interval can select, a superset of it: a
        start, a clock sample inside a compared window, a disconnect overlapping one. The old
        code's own filter then picks from them, in file order, as it picks from the whole file."""
        if not isinstance(rec, dict):
            return False
        kind = rec.get("kind")
        if kind == "start":
            return True
        if kind == "clock":
            return any(lo <= rec.get("recv_ns", -1) <= hi for lo, hi in windows)
        if kind == "disconnect":
            return any(rec.get("start_recv_ns", hi + 1) <= hi and rec.get("end_recv_ns", -1) >= lo
                       for lo, hi in windows)
        return False
    every, _kinds, _torn, _n, _t = scan_runtime(REC_RUNTIME, selectable)

    def same_slice(t):
        """The stored slice against the old recorder's, over the records written by then."""
        stored_path = "%s/%d/runtime.jsonl" % (REC_SERIES, t)
        mtime_ns = os.stat(stored_path).st_mtime_ns
        o.runtime = [x for x in every if written_ns(x) <= mtime_ns]
        mine = slice_bytes(o, t, os.path.join(SCRATCH, "rec"))
        with open(stored_path, "rb") as fh:
            return mine == fh.read()

    equal = 0
    for t in earlier:
        with open(manifest_path(t), encoding="utf-8") as fh:
            m = json.loads(fh.read())
        assert m.get("T0_epoch") == t, "G-REC: %s carries T0_epoch %r" % (manifest_path(t),
                                                                         m.get("T0_epoch"))
        same = same_slice(t)
        equal += 1 if same else 0
        out("G-REC earlier interval %d %s: closed by the new code, complete %s, disconnects %s, "
            "sha %s, slice equal to the old recorder's %s" % (t, utc(t), m.get("complete"),
                                                               m.get("disconnect_count"),
                                                               m.get("recorder_git_sha"), same))
    present = complete = quotes = shas = 0
    for t in members:
        if t in missing:
            out("G-REC interval %d %s: no manifest by %s" % (t, utc(t), utc(t + REC_DEADLINE_S)))
            continue
        with open(manifest_path(t), encoding="utf-8") as fh:
            m = json.loads(fh.read())
        assert m.get("T0_epoch") == t, "G-REC: %s carries T0_epoch %r" % (manifest_path(t),
                                                                         m.get("T0_epoch"))
        present += 1
        complete += 1 if m.get("complete") is True else 0
        quotes += 1 if m.get("quotes_complete") is True else 0
        shas += 1 if m.get("recorder_git_sha") == head else 0
        same = same_slice(t)
        equal += 1 if same else 0
        out("G-REC interval %d %s: complete %s, quotes_complete %s, disconnects %s, sha %s, "
            "slice equal to the old recorder's %s" % (t, utc(t), m.get("complete"),
                                                       m.get("quotes_complete"),
                                                       m.get("disconnect_count"),
                                                       m.get("recorder_git_sha"), same))
    ok = (present == REC_UNITS and quotes == REC_UNITS and shas == REC_UNITS
          and complete >= REC_COMPLETE_MIN and equal == len(compared))
    out("G-REC %s: manifests %d of %d, quotes_complete %d of %d, sha %d of %d, complete %d of %d "
        "(PASS at %d or more), slices equal %d of %d compared (%d earlier, %d members)"
        % ("PASS" if ok else "FAIL", present, REC_UNITS, quotes, REC_UNITS, shas, REC_UNITS,
           complete, REC_UNITS, REC_COMPLETE_MIN, equal, len(compared), len(earlier), present))
    assert ok, "G-REC FAIL"


def mode_final():
    state = load_state()
    r, head = state["restart"], state["branch_head"]
    pid, _n = check_unit(REC_UNIT, REC_ARGV, REC_CWD, r["restarts"])
    assert pid == r["pid"], "G-FINAL: the recorder's pid moved to %d" % pid
    assert head_of(SVC) == head, "G-FINAL: %s is not at the branch" % SVC
    files_equal(REC_CWD, NEW_FILES, "G-FINAL the unit's tree")
    starts, _kinds, torn, newlines, _t = scan_runtime(REC_RUNTIME, is_start)
    starts.sort(key=lambda x: x["recv_ns"])
    assert starts[-1]["recv_ns"] == r["start_ns"] and starts[-1]["sha"] == head, \
        "G-FINAL: the newest start %r" % starts[-1]
    out("G-FINAL %s: %d newlines, %d torn, newest start %s on %s"
        % (REC_RUNTIME, newlines, torn, utc(r["start_ns"] / 1e9), head))
    sole_recorder(pid)
    memory(REC_UNIT)
    memory(CB_UNIT)
    meminfo()
    out("G-FINAL PASS: recorder pid %d on %s" % (pid, head))
    cb_pid, _n = check_unit(CB_UNIT, CB_ARGV, None, state["cb_restarts"])
    assert cb_pid == state["cb_pid"], "G-CB-STILL: the chain book's pid moved from %d to %d" % (
        state["cb_pid"], cb_pid)
    sole_chainbook(cb_pid)
    out("G-CB-STILL PASS: the chain book ran as pid %d, NRestarts %d, from state to the end"
        % (cb_pid, state["cb_restarts"]))


def mode_revert():
    state = load_state()
    mark = state["marks"]["revert"]
    got = head_of(SVC)
    assert got == OLD_SHA, "K-21: %s is at %s" % (SVC, got)
    files_equal(REC_CWD, OLD_FILES, "K-21 the unit's tree")
    assert clean(SVC), "K-21: %s has local changes" % SVC
    # An explicit restart is not one of systemd's own, and a revert must not stop on the venue's
    # socket, so NRestarts and the startup gaps are recorded, not asserted.
    pid, _st = check_restart("K-21", mark, OLD_SHA, None, None, None)
    sole_recorder(pid)
    memory(REC_UNIT)
    out("REVERT PASS: the recorder runs 4216c04 again as pid %d" % pid)


# ---- section 9 ------------------------------------------------------------------------------

TOKEN = re.compile(r"(?<![0-9a-f])[0-9a-f]{16,64}(?![0-9a-f])")


def report_tokens():
    """Every run of 16 to 64 lowercase hex characters in a report under CryptoReports/."""
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            tokens.update(TOKEN.findall(read_text(os.path.join(REPORTS, name))))
    return tokens


def reclaimable(tree):
    """This TZ's tree, or an earlier session's directory beside this session's under /tmp."""
    if tree == WORK:
        return True
    return (tree.startswith("/tmp/") and os.path.isdir(tree) and not os.path.islink(tree)
            and UUID.fullmatch(os.path.basename(tree)) is not None
            and "btc-5m-twap" in os.path.basename(os.path.dirname(tree)))


def by_name(tree, rel):
    return tree == WORK and (rel == "state.json" or rel.startswith("logs/"))


def pristine(tree):
    """A worktree holding exactly its HEAD's tracked files, with HEAD on its upstream: git keeps
    every byte of it, so nothing in it is copied and `git worktree remove` needs no --force."""
    cp = subprocess.run(["git", "-C", tree, "status", "--porcelain", "--ignored"],
                        capture_output=True, text=True)
    assert cp.returncode == 0 and cp.stdout == "", "reclaim: %s holds %r" % (tree, cp.stdout[:400])
    head = head_of(tree)
    up = subprocess.run(["git", "-C", tree, "rev-parse", "@{u}"], capture_output=True, text=True)
    assert up.returncode == 0 and up.stdout.strip() == head, \
        "reclaim: %s is at %s, its upstream at %r" % (tree, head, up.stdout.strip())
    out("reclaim: %s skipped: no file but its HEAD's, and HEAD %s is its upstream's" % (tree, head))


def mode_reclaim(trees):
    assert trees and all(reclaimable(t) for t in trees), "reclaim: %r" % (trees,)
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
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--"
                                    + rel.replace("/", "--"))
                if os.path.exists(dest):
                    got = sha256_file(dest)
                    assert got == h, "reclaim: %s exists with sha256 %s, source %s" % (dest, got,
                                                                                       h)
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    for chunk in iter(lambda: src.read(1 << 20), b""):
                        dst.write(chunk)
                assert sha256_file(dest) == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, "
        "%d already held; forensic store %d -> %d files" % (considered, named, kept, copied, held,
                                                           before, after))


def main(argv):
    if not argv:
        sys.exit("usage: tz21-recorder-memory.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    table = {"state": mode_state, "synth": mode_synth, "equiv": mode_equiv, "path": mode_path,
             "restart": mode_restart, "rec": mode_rec, "final": mode_final,
             "revert": mode_revert}
    if mode == "mark":
        assert len(rest) == 1, "mark NAME"
        mode_mark(rest[0])
    elif mode == "reclaim":
        mode_reclaim(rest)
    else:
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    out("peak memory of this run: %d bytes" % (
        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
    out("opens under the capture roots: %d" % len(OPENS))


if __name__ == "__main__":
    main(sys.argv[1:])
