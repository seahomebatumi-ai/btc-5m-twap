#!/usr/bin/env python3
"""TZ-46 - the capture's room: the reward book's archive every three hours, the pair book stopped after its last
archive run, the forensic store's copies of what a public Release holds removed, and the room above the reward
book's stream floor read before and after.

    fingerprint       map section 0 against the primary checkout
    number            CANON hard rule 2: of the number TZ-46, this TZ's file alone under CryptoTZ/, no report
    selftest          every rule of this file, on literals, temporary trees and a loopback server only
    still             the four units: the first call records them, a later one reads G-STILL
    scratch OWN       the UUID directories beside this session's own, each named live or earlier
    room LABEL        the disk, before or after: free space, both stores' stream and other bytes, the forensic
                      store and both archives' recent runs; after, G-ROOM, exit 4 where it reads FAIL
    forensics         every file of the forensic store that a public Release holds by bytes and SHA-256, each
                      proved by the Release's own record and a full anonymous download: forensics-plan.json
    forensics-remove  each planned file hashed again and removed: G-FORENSIC
    mark NAME         an instant and the units' states into state.json: pairoff, timer, retry, revert
    band NAME         exit 0 inside the band its block waits for, 3 outside it: pairoff or timer
    pairwait          until the pair book archive's run begun by B-PAIR-OFF ends: exit 0, 75 deferred, else 1
    pair              G-PAIR: that run, its tag, and the pair book and its archive's timer stopped and disabled
    timer             G-TIMER: the reward book archive's timer as installed and as systemd reads it
    first             that archive's first run on the new calendar: G-TRIGGER, G-RUN, G-TAG and G-NEXT;
                      exit 3 NOT YET
    reclaim TREE...   section 9: every file a committed report names by hash into the forensic store

No mode opens a stream, rewards or selection file of the reward book, or any file of the pair book's store: of
either store it reads the names and sizes of its directory entries, and of the reward book's also its slot records
and runtime.jsonl, which the reserve excepts. No mode prints a price, a size, a side, a book's hash, a rate, a
competitiveness or an outcome. No request carries a credential, and none goes to a host but GitHub's. No mode
changes a unit: the TZ's blocks do. Run it with /root/tz04a-env; it needs the standard library alone.

Written for CryptoTZ/TZ-46-capture-room.md. The TZ is the specification.
"""

import datetime
import hashlib
import http.client
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
import urllib.error
import urllib.parse
import urllib.request

if not __debug__:
    sys.stderr.write("tz46: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

HERE = os.path.dirname(os.path.abspath(__file__))
PYFILE = "tz46-capture-room.py"

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------------

MAP_REVISION = "2026-11-16-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 61, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"(?:`([0-9a-f]{64})`|[^|]*) \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)
NUMBER = "TZ-46-"
OWN_TZ = "CryptoTZ/TZ-46-capture-room.md"

PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
WORK = "/root/tz46-work"
WT = WORK + "/wt"
TMP = WORK + "/selftest-tmp"
STATE = WORK + "/state.json"
PLAN = WORK + "/forensics-plan.json"
REMOVED = WORK + "/forensics-removed.jsonl"
FORENSICS = "/root/btc-forensics"
RB = "/var/lib/btc-rewardbook"
RB_ARCH = "/var/lib/btc-rewardbook-archive"
RB_ASVC = "/root/btc-rewardbook-archive-svc"
PB = "/var/lib/btc-pairbook"
PB_ARCH = "/var/lib/btc-pairbook-archive"
PB_ASVC = "/root/btc-pairbook-archive-svc"
RECORDER = "/var/lib/btc-recorder"
CHAINBOOK = "/var/lib/btc-chainbook"
DISK_PATH = "/var/lib"
UNIT_DIR = "/etc/systemd/system"
TIMER_REL = "deploy/systemd/btc-rewardbook-archive.timer"
TIMER_SHA256 = "7b0804285af6987340838bd59573897d013cf97edc5d4132cda7f3f9ba3e3824"       # Appendix A's timer
OLD_TIMER_SHA256 = "bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f"   # TZ-34's, map section 0
TZ33_REL = "research/tz33-reward-book-capture.py"
TZ33_SHA256 = "a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670"
UNITS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service",
         "rewardbook": "btc-rewardbook.service", "advisor": "adv3-bot.service"}
RB_SVC, RB_TIMER = "btc-rewardbook-archive.service", "btc-rewardbook-archive.timer"
PB_SVC, PB_TIMER = "btc-pairbook-archive.service", "btc-pairbook-archive.timer"
PB_ARGV = ("/root/tz04a-env/venv/bin/python", "-B", "-u", "/root/btc-pairbook-svc/tz26-nesting-b3-capture.py",
           "serve")
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")
TERMINAL = ("complete", "empty", "halt", "deferred")

REPO = "seahomebatumi-ai/btc-5m-twap"
API_BASE, WEB_BASE = "https://api.github.com", "https://github.com"
UA = "btc-5m-twap-tz46"
API_VERSION = "2022-11-28"
API_TIMEOUT_S, DOWNLOAD_TIMEOUT_S, DOWNLOAD_ATTEMPTS = 60, 300, 3
API_MAX = 40                 # API requests a run of `forensics` makes at most: GitHub allows one address 60 an hour
RELEASES_PER_PAGE = 20       # a page of Releases carries every asset's record: twenty keep one page's parse small
HOSTS = ("api.github.com", "github.com", "127.0.0.1")
PLAN_MIN = {"tz-44-l0-inputs": 13}    # map section 7 item 167: the twelve archives and the manifest its Release holds

DAY, SLOT = 86400, 900
CALENDAR = "*-*-* 01/3:30:20 UTC"
CAL_FIRST_S, CAL_STEP_S = 5420, 10800    # 01:30:20 UTC, then every third hour: eight elapses a day
TIMER_BAND = (3920, 4820)                # B-TIMER: from 25 to 10 minutes before an elapse, as seconds of its step
TIMER_DAY = (36320, 69620)               # ... from 10:05:20 to 19:20:20 UTC
PAIR_DAY = (27000, 68400)                # B-PAIR-OFF: from 07:30:00 to 19:00:00 UTC
SLOT_JSON_AT, SETTLE_S, DECIDE_S = 910, 60, 6
NEXT_AFTER_S, NEXT_SETTLE_S = 900, 30
FIRST_LATE_S = 600           # G-TRIGGER: no run begun 600 s after the first elapse reads FAIL
PAIRWAIT_START_S, PAIRWAIT_MAX_S, PAIRWAIT_STEP_S = 120, 3600, 30
STREAM_FLOOR = 7300000000    # research/tz33-reward-book-capture.py line 190
HEAVIEST_SLOT = 31823974     # stored stream bytes of the heaviest slot of L0's eight days (TZ-45 section 0.4)
PEAK_SLOTS = 14              # the most slots of stream the store holds between two runs every three hours
PEAK = PEAK_SLOTS * HEAVIEST_SLOT
ROOM_MIN = 2000000000        # G-ROOM
DRIFTS = (43500000, 187760570)    # map section 6: bytes a day beside the streams, TZ-26's base and the fastest
DISK_FLOOR = 2300000000      # every mode's free-space floor: the reward book's halt floor and 100,000,000
RECLAIM_FLOOR = STREAM_FLOOR + 100000000    # reclaim's floor after each copy: the stream floor and one slot at the cut
MEM_FLOOR = 133073162        # MemAvailable at a mode's start: twice 66,536,581, the host peak modelled (section 0.4)
MEM_READS, MEM_WAIT_S = 5, 60

DIR_RE = re.compile(r"[0-9]{10}")
RB_STREAM_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.stream\.jsonl\.gz")
RB_SLOT_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.slot\.json")
SHA_RE = re.compile(r"[0-9a-f]{64}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
STAMP_RE = re.compile(r"[A-Z][a-z]{2} ([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}) UTC")
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
LIVE_S = 60

# ---- the audit hook: TZ-46 section 2 as a pure function, and the hook that applies it -------------------------

MODE = [None]
ALLOWED_REMOVE = set()
REFUSED = []
COUNTS = {"requests": 0, "downloads": 0, "download_bytes": 0, "removed": 0, "reward book opens": 0}
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
CHANGE_EVENTS = ("os.remove", "os.rename", "os.rmdir", "os.mkdir", "os.truncate", "os.chmod", "os.chown",
                 "os.utime", "os.link", "os.symlink", "shutil.rmtree", "shutil.move", "shutil.copyfile")
HOOKED = ("open", "os.listdir", "os.scandir", "socket.getaddrinfo") + CHANGE_EVENTS


class GuardError(RuntimeError):
    pass


def _under(p, root):
    return p == root or p.startswith(root + "/")


def _path(p):
    if isinstance(p, bytes):
        p = os.fsdecode(p)
    return os.path.abspath(p) if isinstance(p, str) else None


def _writing(wmode, flags):
    if isinstance(wmode, str):
        return bool(set(wmode) & set("wax+"))
    return isinstance(flags, int) and bool(flags & WRITE_FLAGS)


def _exclusive(wmode, flags):
    if isinstance(wmode, str):
        return "x" in wmode
    return isinstance(flags, int) and bool(flags & os.O_EXCL)


def policy(mode, event, args, allowed):
    """None where TZ-46 section 2 allows the event in this mode; otherwise why it is refused. Pure."""
    if event == "socket.getaddrinfo":
        host = args[0] if args else None
        if isinstance(host, bytes):
            host = host.decode("ascii", "replace")
        ok = host in HOSTS or (isinstance(host, str) and host.endswith(".githubusercontent.com"))
        return None if ok else "a connection to %r" % (host,)
    p = _path(args[0]) if args else None
    if p is None:
        return None
    if event == "open":
        wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
        w = _writing(wm, fl)
        if _under(p, RECORDER) or _under(p, CHAINBOOK) or _under(p, PB):
            return "an open under another capture's store"
        if _under(p, RB):
            if w:
                return "a write under the reward book's store"
            ok = RB_SLOT_RE.fullmatch(os.path.basename(p)) is not None or p == RB + "/runtime.jsonl"
            return None if ok else "an open of the reward book's %s" % os.path.basename(p)
        if _under(p, FORENSICS) and w:
            return None if mode == "reclaim" and _exclusive(wm, fl) else "a write into the forensic store"
        if w and not _under(p, WORK):
            return "a write outside the work tree"
        return None
    if event in ("os.listdir", "os.scandir"):
        return "a listing under another capture's root" if _under(p, RECORDER) or _under(p, CHAINBOOK) else None
    paths = [p]
    if event in ("os.rename", "os.link", "os.symlink", "shutil.move", "shutil.copyfile") and len(args) > 1:
        paths.append(_path(args[1]))
    for q in paths:
        if q is None:
            continue
        if event == "os.remove" and mode == "forensics-remove" and q in allowed and _under(q, FORENSICS):
            continue
        if not _under(q, WORK):
            return "a change outside the work tree"
    return None


def _audit(event, args):
    if event not in HOOKED:
        return
    why = policy(MODE[0], event, args, ALLOWED_REMOVE)
    if why is not None:
        REFUSED.append((event, str(args[0]) if args else ""))
        raise GuardError("%s refused in mode %s, %s: %r" % (event, MODE[0], why, args[0] if args else None))
    if event == "open" and args:
        p = _path(args[0])
        if p is not None and _under(p, RB):
            COUNTS["reward book opens"] += 1


sys.addaudithook(_audit)

# ---- small helpers ------------------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return datetime.datetime.fromtimestamp(float(t), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path, chunk=1 << 20):
    """The SHA-256 and the byte count of a file read as bytes."""
    h, n = hashlib.sha256(), 0
    with open(path, "rb") as fh:
        for b in iter(lambda: fh.read(chunk), b""):
            h.update(b)
            n += len(b)
    return h.hexdigest(), n


def json_bytes(obj):
    return (json.dumps(obj, sort_keys=True, indent=1) + "\n").encode("utf-8")


def free_bytes():
    st = os.statvfs(DISK_PATH)
    return st.f_bavail * st.f_frsize


def mem_available():
    with open("/proc/meminfo", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) * 1024
    raise AssertionError("no MemAvailable")


def floors(read=mem_available, sleep=time.sleep, freef=free_bytes):
    """At a mode's start: MemAvailable read up to five times 60 s apart, the first at or above MEM_FLOOR passing;
    free space at or above DISK_FLOOR."""
    for k in range(1, MEM_READS + 1):
        m = read()
        out("MemAvailable read %d: %d bytes, floor %d" % (k, m, MEM_FLOOR))
        if m >= MEM_FLOOR:
            break
        assert k < MEM_READS, "BLOCKED: MemAvailable below %d at %d reads" % (MEM_FLOOR, MEM_READS)
        sleep(MEM_WAIT_S)
    f = freef()
    out("free %d bytes, floor %d" % (f, DISK_FLOOR))
    assert f >= DISK_FLOOR, "BLOCKED: free %d bytes, below %d" % (f, DISK_FLOOR)
    return f


def load_state(path=STATE):
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save_state(st, path=STATE):
    with open(path + ".new", "w", encoding="utf-8") as fh:
        json.dump(st, fh, sort_keys=True, indent=1)
        fh.write("\n")
    os.replace(path + ".new", path)


def show(unit, props):
    """systemctl show under TZ=UTC and the C locale: {property: value}, a repeated property's values joined."""
    args = ["systemctl", "show", unit]
    for p in props:
        args += ["-p", p]
    cp = subprocess.run(args, capture_output=True, text=True, env=dict(os.environ, **SHOW_ENV))
    assert cp.returncode == 0, "systemctl show %s: %s" % (unit, cp.stderr.strip())
    kv = {}
    for line in cp.stdout.split("\n"):
        if "=" in line:
            k, v = line.split("=", 1)
            kv[k] = v if k not in kv else kv[k] + "\n" + v
    return kv


def stamp_of(text):
    """An epoch from systemctl's own stamp printed under TZ=UTC; None where it prints none."""
    m = STAMP_RE.fullmatch((text or "").strip())
    if m is None:
        return None
    dt = datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc)
    return int(dt.timestamp())


def git(*args, tree=PRIMARY):
    cp = subprocess.run(["git", "-C", tree] + list(args), capture_output=True, text=True)
    assert cp.returncode == 0, "git %s: %s" % (" ".join(args), cp.stderr.strip()[:300])
    return cp.stdout.strip()


def ledger(path):
    """A ledger's complete lines, parsed, and the bytes of a line still being written."""
    with open(path, "rb") as fh:
        raw = fh.read()
    parts = raw.split(b"\n")
    return [json.loads(ln) for ln in parts[:-1] if ln.strip()], parts[-1]


def processes_with(argv):
    """Every process whose command line is argv exactly, field for field."""
    found = []
    for pid in sorted((p for p in os.listdir("/proc") if p.isdigit()), key=int):
        try:
            with open("/proc/%s/cmdline" % pid, "rb") as fh:
                fields = fh.read().split(b"\0")
        except OSError:
            continue
        if fields and fields[-1] == b"":
            fields = fields[:-1]
        try:
            if [f.decode("utf-8") for f in fields] == list(argv):
                found.append(int(pid))
        except UnicodeDecodeError:
            continue
    return found


def ls_remote_tag(tag):
    """The object a tag names on origin, and its peeled commit where it is annotated."""
    lines = git("ls-remote", "origin", "refs/tags/%s" % tag, "refs/tags/%s^{}" % tag).split("\n")
    rows = dict(reversed(ln.split("\t")) for ln in lines if "\t" in ln)
    return rows.get("refs/tags/%s" % tag), rows.get("refs/tags/%s^{}" % tag)

# ---- the clock: the new calendar and the blocks' bands --------------------------------------------------------


def next_calendar(now):
    """The first elapse of `*-*-* 01/3:30:20 UTC` strictly after now: 01:30:20 UTC and every 10,800 s after it."""
    d0 = int(now) // DAY * DAY
    for k in range(8):
        t = d0 + CAL_FIRST_S + k * CAL_STEP_S
        if t > now:
            return t
    return d0 + DAY + CAL_FIRST_S


def is_calendar(t):
    return int(t) == t and (int(t) % DAY - CAL_FIRST_S) % CAL_STEP_S == 0 and int(t) % DAY >= CAL_FIRST_S


def band_reading(name, now, rb_state, pb_state):
    """(True, why) where the band B-PAIR-OFF or B-TIMER waits for holds at `now`, given both archives' services'
    ActiveState; else (False, why). Pure."""
    s = int(now) % DAY
    if rb_state in RUNNING or pb_state in RUNNING:
        return False, "an archive runs: the reward book's %s, the pair book's %s" % (rb_state, pb_state)
    if name == "pairoff":
        ok = PAIR_DAY[0] <= s <= PAIR_DAY[1]
        return ok, "second %d of the day, the band %d to %d" % (s, PAIR_DAY[0], PAIR_DAY[1])
    assert name == "timer", "band %r" % name
    r = s % CAL_STEP_S
    ok = TIMER_DAY[0] <= s <= TIMER_DAY[1] and TIMER_BAND[0] <= r <= TIMER_BAND[1]
    return ok, "second %d of the day, %d of its step; the next elapse %s" % (s, r, utc(next_calendar(now)))

# ---- the stores, by their directory entries alone -------------------------------------------------------------


def is_stream(kind, name):
    """A stream file by the store's own names: the reward book's <S>.<k>.stream.jsonl.gz, as its stream_bytes_total
    counts them (research/tz33-reward-book-capture.py lines 1279 to 1291), or the pair book's stream*.jsonl.gz, as
    its own does (research/tz26-nesting-b3-capture.py lines 794 to 806)."""
    if kind == "rb":
        return name.endswith(".stream.jsonl.gz") and RB_STREAM_RE.fullmatch(name) is not None
    assert kind == "pb", "kind %r" % kind
    return name.startswith("stream") and name.endswith(".jsonl.gz")


def store_view(root, kind):
    """A capture's store by directory entries alone: its stream files and every other file, counts and bytes, and
    the stream bytes of each numbered directory. Nothing is opened."""
    v = {"streams_n": 0, "streams_bytes": 0, "other_n": 0, "other_bytes": 0, "dirs": 0, "by_dir": {}}
    if not os.path.isdir(root):
        return v
    with os.scandir(root) as it:
        entries = sorted(it, key=lambda e: e.name)
    for e in entries:
        if e.is_dir(follow_symlinks=False) and DIR_RE.fullmatch(e.name):
            v["dirs"] += 1
            with os.scandir(e.path) as it2:
                files = sorted(it2, key=lambda x: x.name)
            for f in files:
                if not f.is_file(follow_symlinks=False):
                    continue
                size = f.stat(follow_symlinks=False).st_size
                if is_stream(kind, f.name):
                    v["streams_n"] += 1
                    v["streams_bytes"] += size
                    v["by_dir"][int(e.name)] = v["by_dir"].get(int(e.name), 0) + size
                else:
                    v["other_n"] += 1
                    v["other_bytes"] += size
        elif e.is_file(follow_symlinks=False):
            v["other_n"] += 1
            v["other_bytes"] += e.stat(follow_symlinks=False).st_size
    return v


def forensic_files(root, hashed=True):
    """Every regular file under root but links and empty files, in path order: {path, bytes, sha256}."""
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for name in sorted(filenames):
            p = os.path.join(dirpath, name)
            if os.path.islink(p) or not os.path.isfile(p) or os.path.getsize(p) == 0:
                continue
            if hashed:
                h, n = sha256_file(p)
                found.append({"path": p, "bytes": n, "sha256": h})
            else:
                found.append({"path": p, "bytes": os.path.getsize(p), "sha256": None})
    return found


def tree_count(root):
    n = b = 0
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            p = os.path.join(dirpath, name)
            if not os.path.islink(p) and os.path.isfile(p):
                n += 1
                b += os.path.getsize(p)
    return n, b

# ---- GitHub, anonymous: every header fixed --------------------------------------------------------------------


def build_request(url, accept="application/vnd.github+json"):
    """The one builder of every request: Accept, this file's User-Agent and the API version; never a credential."""
    return urllib.request.Request(url, method="GET", headers={"Accept": accept, "User-Agent": UA,
                                                               "X-GitHub-Api-Version": API_VERSION})


def get_json(url):
    """One API request, no retry: (status, document)."""
    COUNTS["requests"] += 1
    assert COUNTS["requests"] <= API_MAX, "BLOCKED: more than %d API requests" % API_MAX
    try:
        with urllib.request.urlopen(build_request(url), timeout=API_TIMEOUT_S) as resp:
            raw = resp.read()
            return int(resp.status), json.loads(raw) if raw else None
    except urllib.error.HTTPError as exc:
        return int(exc.code), None


def download(url):
    """A download streamed into SHA-256 and a byte count, nothing stored: (status, bytes, sha256)."""
    COUNTS["downloads"] += 1
    h, n = hashlib.sha256(), 0
    with urllib.request.urlopen(build_request(url, "application/octet-stream"), timeout=DOWNLOAD_TIMEOUT_S) as resp:
        status = int(resp.status)
        for b in iter(lambda: resp.read(1 << 20), b""):
            h.update(b)
            n += len(b)
    COUNTS["download_bytes"] += n
    return status, n, h.hexdigest()


def download_checked(url, attempts=DOWNLOAD_ATTEMPTS, backoff_s=10):
    """A download with up to `attempts` tries where the transfer breaks; a whole reply is never retried."""
    for k in range(1, attempts + 1):
        try:
            return download(url)
        except urllib.error.HTTPError as exc:
            return int(exc.code), 0, None
        except (urllib.error.URLError, OSError, http.client.HTTPException) as exc:
            out("download %s broke: %s, attempt %d of %d" % (url.rsplit("/", 1)[-1], type(exc).__name__, k, attempts))
            if k == attempts:
                return None, 0, None
        time.sleep(backoff_s * k)
    return None, 0, None


ASSET_KEYS = ("id", "name", "size", "state", "digest", "browser_download_url")


def slim_asset(a):
    return {k: a.get(k) for k in ASSET_KEYS}


def slim_release(rel):
    """A Release's record cut to what the plan reads: its id, tag, draft flag and its assets' own records."""
    return {"id": rel.get("id"), "tag_name": rel.get("tag_name"), "draft": rel.get("draft"),
            "assets": [slim_asset(a) for a in rel.get("assets") or []]}


def paged(url, per, keep):
    """Every item of a list endpoint, `per` a page until a shorter page, each cut by `keep` as its page arrives."""
    found, page = [], 1
    while True:
        status, doc = get_json("%s%sper_page=%d&page=%d" % (url, "&" if "?" in url else "?", per, page))
        assert status == 200 and isinstance(doc, list), "BLOCKED: %s page %d: status %r" % (url, page, status)
        found.extend(keep(x) for x in doc)
        if len(doc) < per:
            return found
        page += 1


def download_url(web, tag, name):
    return "%s/%s/releases/download/%s/%s" % (web, REPO, urllib.parse.quote(tag), urllib.parse.quote(name))

# ---- the forensic store against the Releases: pure --------------------------------------------------------------


def index_assets(rels):
    """(bytes, sha256) -> [(tag, release id, asset)] over every uploaded asset of a published Release whose record
    carries a SHA-256 digest, each list in order of tag and name. Pure."""
    idx = {}
    for rel in rels:
        if rel.get("draft") is not False or not isinstance(rel.get("tag_name"), str):
            continue
        for a in rel.get("assets") or []:
            d = a.get("digest") or ""
            if a.get("state") == "uploaded" and isinstance(a.get("size"), int) and d.startswith("sha256:") \
                    and SHA_RE.fullmatch(d[7:]):
                idx.setdefault((a["size"], d[7:]), []).append((rel["tag_name"], rel.get("id"), a))
    for v in idx.values():
        v.sort(key=lambda x: (x[0], str(x[2].get("name"))))
    return idx


def plan_rows(files, idx):
    """The forensic files some Release holds by bytes and SHA-256, each with its first candidate, and the count of
    those none holds. Pure."""
    held = [(f, idx[(f["bytes"], f["sha256"])][0]) for f in files if (f["bytes"], f["sha256"]) in idx]
    return held, len(files) - len(held)


def asset_ok(a, size, sha, url):
    """The Release's own record of one asset against a file: uploaded, its bytes, its digest, its URL. Pure."""
    return (isinstance(a, dict) and a.get("state") == "uploaded" and a.get("size") == size
            and a.get("digest") == "sha256:" + sha and a.get("browser_download_url") == url)

# ---- the readings: pure --------------------------------------------------------------------------------------


def room_reading(free, rb_streams):
    """G-ROOM, pure: the free space with the reward book's stream files gone - the bytes its archive gives back -
    less its stream floor and the most its store holds between two runs, against ROOM_MIN. (room, margin, PASS)."""
    room = free + rb_streams
    margin = room - STREAM_FLOOR - PEAK
    return room, margin, margin >= ROOM_MIN


def timer_checks(kv, now, installed_sha, pb):
    """G-TIMER, pure: the timer as systemd reads it under TZ=UTC, the installed file's SHA-256, and the pair book
    archive's timer."""
    cal, mono = kv.get("TimersCalendar") or "", kv.get("TimersMonotonic") or ""
    return {"loaded": kv.get("LoadState") == "loaded",
            "active, waiting or running": kv.get("ActiveState") == "active" and kv.get("SubState") in ("waiting",
                                                                                                   "running"),
            "enabled": kv.get("UnitFileState") == "enabled",
            "its fragment": kv.get("FragmentPath") == UNIT_DIR + "/" + RB_TIMER,
            "its unit": kv.get("Unit") == RB_SVC,
            "one calendar, every third hour from 01:30:20 UTC": cal.count("OnCalendar=") == 1
            and ("OnCalendar=%s ;" % CALENDAR) in cal,
            "no run on a start of the timer": "USec=" not in mono,
            "accuracy 1 s": kv.get("AccuracyUSec") == "1s",
            "the next elapse the calendar's": stamp_of(kv.get("NextElapseUSecRealtime")) == next_calendar(now),
            "installed byte for byte": installed_sha == TIMER_SHA256,
            "the pair book archive's timer stopped and disabled": pb.get("ActiveState") == "inactive"
            and pb.get("UnitFileState") == "disabled"}


def first_start(recs, since_ns):
    """The first start record at or after since_ns - a run begun then, or a pending set resumed then - its run, and
    that run's records from that start on: (run, start, records). Pure."""
    for i, r in enumerate(recs):
        if r.get("event") == "start" and r.get("wall_ns", 0) >= since_ns:
            return r.get("run"), r, [x for x in recs[i:] if x.get("run") == r.get("run")]
    return None, None, []


def run_state(mine):
    """A run's state from its records: 'running' where no terminal record follows its last start, else that
    record's event. Pure."""
    last = max(i for i, r in enumerate(mine) if r.get("event") == "start")
    terms = [r.get("event") for r in mine[last + 1:] if r.get("event") in TERMINAL]
    return terms[-1] if terms else "running"


def trigger_reading(trg, elapse, s0, last_trigger):
    """G-TRIGGER, pure: the trigger systemd handed the run, its first start record's - TRIGGER_UNIT this timer, its
    realtime from the elapse to 60 s after it, the record within 60 s after it - else the timer's LastTriggerUSec
    read the same way. (PASS, the evidence read, the trigger's second)."""
    if trg and trg.get("unit") is not None:
        t = int(trg.get("realtime_usec") or 0) // 10 ** 6
        return (trg["unit"] == RB_TIMER and elapse <= t <= elapse + 60 and t - 1 <= s0 <= t + 60), \
            "TRIGGER_UNIT %s" % trg["unit"], t
    t = last_trigger
    return (t is not None and elapse <= t <= elapse + 60 and t - 1 <= s0 <= t + 60), "LastTriggerUSec", t


def next_slots(first_ns, last_ns):
    """The slots whose decision instant S - 6 lies from a run's first removal to 900 s after its last."""
    s = -(-(first_ns + DECIDE_S * 10 ** 9) // (SLOT * 10 ** 9)) * SLOT
    found = []
    while (s - DECIDE_S) * 10 ** 9 < last_ns + NEXT_AFTER_S * 10 ** 9:
        found.append(s)
        s += SLOT
    return found


def next_verdict(sjs, errors, pid0):
    """One slot across the removals, from its slot.json files [(k, doc)] and its task's error records: FAIL where an
    error record or no slot.json; PASS where the process the run began beside streamed it with no reason to keep it
    off; UNDECIDABLE otherwise. Pure."""
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
    vs = [v for v, _w in verdicts]
    return "FAIL" if "FAIL" in vs else ("UNDECIDABLE" if "UNDECIDABLE" in vs or not vs else "PASS")


def pair_reading(mine, tag_obj, commit, pb, tmr, svc, procs):
    """G-PAIR, pure: the pair book archive's run begun by B-PAIR-OFF complete - its set moved, the pair book
    restarted and resumed, every request inside the idle stretch - and its tag at the archive's commit; then the
    pair book stopped and disabled, no process of it left, and its archive's timer stopped and disabled."""
    ev = [r.get("event") for r in mine]
    comp = [r for r in mine if r.get("event") == "complete"]
    res = [r for r in mine if r.get("event") == "resume"]
    return {"the run complete": bool(mine) and run_state(mine) == "complete",
            "the pair book restarted and resumed by it": "restart" in ev and bool(res)
            and res[-1].get("reading") != "FAIL",
            "every request inside the idle stretch": bool(comp) and comp[-1].get("started_outside") == 0
            and comp[-1].get("ended_outside") == 0,
            "its tag at the archive's commit": tag_obj is not None and tag_obj == commit,
            "the pair book stopped and disabled": pb.get("ActiveState") in ("inactive", "failed")
            and pb.get("MainPID") == "0" and pb.get("UnitFileState") == "disabled",
            "no process of the pair book": not procs,
            "its archive's timer stopped and disabled": tmr.get("ActiveState") == "inactive"
            and tmr.get("UnitFileState") == "disabled",
            "its archive's service idle": svc.get("ActiveState") not in RUNNING}


def still_reading(before, now, restarts, stopped_ok):
    """G-STILL, pure: every unit but the pair book unchanged; the pair book unchanged, or moved by its archive's own
    restart records alone - a chain from the recorded MainPID, NRestarts one higher at each - and active, or, where
    stopped_ok, after that chain stopped: MainPID 0 and not active."""
    for k in sorted(now):
        if k != "pairbook" and now[k] != before.get(k):
            return False, "the %s changed" % k
    b, n = before["pairbook"], now["pairbook"]
    pid, count = b["MainPID"], int(b["NRestarts"])
    for r in restarts:
        if str(r.get("stopped")) != pid or str(r.get("NRestarts")) != str(count + 1):
            return False, "a restart record that does not follow %s at NRestarts %d: %r" % (pid, count, r)
        pid, count = str(r.get("pid")), count + 1
    if n == b and not restarts:
        return True, "unchanged"
    if stopped_ok and n["MainPID"] == "0" and n["ActiveState"] in ("inactive", "failed"):
        return True, "the pair book stopped by B-PAIR-OFF after %d restart records of its archive" % len(restarts)
    if restarts and pid == n["MainPID"] and str(count) == n["NRestarts"] and n["ActiveState"] == "active":
        return True, "the pair book moved by its archive's own restarts alone: %d" % len(restarts)
    return False, "the pair book changed, %d restart records of its archive since the first read" % len(restarts)


def number_reading(names, own):
    """NUMBER, CANON hard rule 2: CryptoTZ/ holds this TZ's file and no other of its number; CryptoReports/ no report
    of it. Pure."""
    tz = [n for n in names if n.startswith("CryptoTZ/" + NUMBER)]
    rp = [n for n in names if n.startswith("CryptoReports/" + NUMBER)]
    return tz == [own] and not rp, tz, rp

# ---- the modes ------------------------------------------------------------------------------------------------


def mode_fingerprint():
    with open(os.path.join(PRIMARY, "SYSTEM-MAP.md"), "rb") as fh:
        raw = fh.read()
    txt = raw.decode("utf-8")
    rev = re.findall(r"^\*\*Revision string:\*\* `([^`]+)`$", txt, re.M)
    assert rev == [MAP_REVISION], "map revision %r, required %s" % (rev, MAP_REVISION)
    found = dict(ANCHOR_ROW.findall(txt))
    assert found == ANCHORS, "anchors %r" % found
    for k, rel in sorted(ANCHOR_FILES.items()):
        h = sha256_file(os.path.join(PRIMARY, rel))[0][:12]
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


def mode_number():
    names = git("ls-tree", "--name-only", "origin/main", "--", "CryptoTZ/", "CryptoReports/").split("\n")
    head = git("rev-parse", "origin/main")
    ok, tz, rp = number_reading(names, OWN_TZ)
    out("origin/main %s: %d paths under CryptoTZ/ and CryptoReports/; of the number %s: %s and %s" % (
        head, len(names), NUMBER, tz, rp))
    out("NUMBER %s" % ("PASS - 2 of 2" if ok else "FAIL"))
    assert ok, "BLOCKED: of the number %s, CryptoTZ/ holds %s and CryptoReports/ %s" % (NUMBER, tz, rp)


def units_now():
    now = {}
    for key, unit in sorted(UNITS.items()):
        kv = show(unit, ["MainPID", "NRestarts", "ActiveState", "UnitFileState", "MemoryCurrent", "MemoryPeak"])
        now[key] = {k: kv.get(k) for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, UnitFileState %s, MemoryCurrent %s, MemoryPeak %s" % (
            unit, now[key], kv.get("UnitFileState"), kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    return now


def archives_now():
    found = {}
    for unit in (RB_TIMER, RB_SVC, PB_TIMER, PB_SVC):
        found[unit] = show(unit, ["ActiveState", "SubState", "UnitFileState", "Result", "NextElapseUSecRealtime",
                                  "LastTriggerUSec"])
        out("%s %s" % (unit, found[unit]))
    return found


def mode_still():
    st = load_state()
    now = units_now()
    archives_now()
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "at_ns": time.time_ns(), "units": now}
        save_state(st)
        out("still: recorded")
        return 0
    since = st["still"]["at_ns"]
    recs, _tail = ledger(PB_ARCH + "/ledger.jsonl")
    restarts = [r for r in recs if r.get("event") == "restart" and r.get("wall_ns", 0) >= since]
    for r in restarts:
        out("the pair book archive's restart record %s: run %s, pid %s after %s, NRestarts %s" % (
            utc(r["wall_ns"] / 1e9), r.get("run"), r.get("pid"), r.get("stopped"), r.get("NRestarts")))
    rrecs, _tail = ledger(RB_ARCH + "/ledger.jsonl")
    runs = sorted({r.get("run") for r in rrecs if r.get("wall_ns", 0) >= since and isinstance(r.get("run"), int)})
    out("the reward book archive's runs with records since the first read: %s" % runs)
    ok, why = still_reading(st["still"]["units"], now, restarts, "pairoff" in st.get("marks", {}))
    out("G-STILL %s: %s since %s" % ("PASS" if ok else "FAIL", why, st["still"]["at"]))
    return 0 if ok else 4


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
    return 0


def runs_line(recs, n=10):
    """The last n runs of an archive, from its ledger: terminal, set, free space and rate."""
    by = {}
    for r in recs:
        if isinstance(r.get("run"), int):
            by.setdefault(r["run"], []).append(r)
    lines = []
    for a in sorted(by)[-n:]:
        mine = by[a]
        c = ([r for r in mine if r.get("event") == "complete"] or [{}])[-1]
        d = ([r for r in mine if r.get("event") == "delete"] or [{}])[-1]
        st = run_state(mine) if any(r.get("event") == "start" for r in mine) else "no start"
        lines.append("run %d %s %s: %s files %s bytes; free before removal %s, after %s; store's streams at its end "
                     "%s; rate a day %s" % (a, utc(a), st, c.get("assets_n"), c.get("bytes_total"),
                                            d.get("free_before"), d.get("free_after"), c.get("store_stream_bytes"),
                                            c.get("rate_per_day")))
    return lines


def mode_room(label):
    assert label in ("before", "after"), "room %r" % label
    floors()
    free = free_bytes()
    rb, pb = store_view(RB, "rb"), store_view(PB, "pb")
    fz = tree_count(FORENSICS)
    out("free %d bytes on %s at %s" % (free, DISK_PATH, utc(time.time())))
    for name, v in (("the reward book's store", rb), ("the pair book's store", pb)):
        out("%s: %d directories; %d stream files, %d bytes; %d other files, %d bytes" % (
            name, v["dirs"], v["streams_n"], v["streams_bytes"], v["other_n"], v["other_bytes"]))
    for t in sorted(pb["by_dir"]):
        if label == "after":
            out("the pair book's window %d %s: %d bytes of stream" % (t, utc(t), pb["by_dir"][t]))
    out("the forensic store: %d files, %d bytes" % fz)
    for name, path in (("reward", RB_ARCH), ("pair", PB_ARCH)):
        recs, tail = ledger(path + "/ledger.jsonl")
        out("the %s book archive's ledger: %d records, %d bytes of a line still written" % (name, len(recs),
                                                                                           len(tail)))
        for line in runs_line(recs):
            out("  %s" % line)
    room, margin, ok = room_reading(free, rb["streams_bytes"])
    out("room: free %d + the reward book's stream files %d = %d; less its stream floor %d and the most its store "
        "holds between two runs, %d = %d slots of %d, the margin %d; with the pair book's %d stream files %d" % (
            free, rb["streams_bytes"], room, STREAM_FLOOR, PEAK, PEAK_SLOTS, HEAVIEST_SLOT, margin, pb["streams_n"],
            room + pb["streams_bytes"]))
    for d in DRIFTS:
        days = margin / d if margin > 0 else 0.0
        out("at %d bytes a day beside the streams the margin lasts %.1f days, to %s [modelled]" % (
            d, days, utc(time.time() + days * DAY)))
    doc = {"label": label, "at": utc(time.time()), "free": free, "reward": rb, "pair": pb,
           "forensics": {"files": fz[0], "bytes": fz[1]}, "room": room, "margin": margin}
    with open(os.path.join(WORK, "room-%s.json" % label), "wb") as fh:
        fh.write(json_bytes(doc))
    if label == "after":
        out("G-ROOM %s: the margin %d bytes, at least %d asked" % ("PASS" if ok else "FAIL", margin, ROOM_MIN))
        return 0 if ok else 4
    return 0


def mode_forensics(root=FORENSICS, api=API_BASE, web=WEB_BASE, plan_path=PLAN, state_path=STATE, least=None):
    floors()
    t0 = time.time()
    files = forensic_files(root)
    out("the forensic store %s: %d files, %d bytes, hashed in %.1f s" % (root, len(files),
                                                                       sum(f["bytes"] for f in files),
                                                                       time.time() - t0))
    rels = paged("%s/repos/%s/releases" % (api, REPO), RELEASES_PER_PAGE, slim_release)
    idx = index_assets(rels)
    out("the repository's Releases read anonymously: %d, %d assets with a digest" % (
        len(rels), sum(len(v) for v in idx.values())))
    held, kept = plan_rows(files, idx)
    out("files a Release holds by bytes and SHA-256: %d; held by none: %d" % (len(held), kept))
    exact, proven, rows = {}, {}, []
    for f, (tag, rid, a) in held:
        if rid not in exact:
            exact[rid] = {x.get("id"): x for x in paged("%s/repos/%s/releases/%d/assets" % (api, REPO, rid), 100,
                                                        slim_asset)}
        url = download_url(web, tag, a.get("name"))
        api_ok = asset_ok(exact[rid].get(a.get("id")), f["bytes"], f["sha256"], url)
        if api_ok and a.get("id") not in proven:
            proven[a.get("id")] = download_checked(url)
        status, n, h = proven.get(a.get("id"), (None, 0, None))
        dl_ok = api_ok and status == 200 and n == f["bytes"] and h == f["sha256"]
        row = {"path": f["path"], "bytes": f["bytes"], "sha256": f["sha256"], "tag": tag, "release_id": rid,
               "asset": a.get("name"), "asset_id": a.get("id"), "url": url, "api_ok": api_ok,
               "download_status": status, "download_bytes": n, "download_sha256": h, "download_ok": dl_ok}
        rows.append(row)
        out("P %s %d %s: %s of %s, asset %s, api %s, download %s %s" % (
            f["path"], f["bytes"], f["sha256"], a.get("name"), tag, a.get("id"), api_ok, status,
            "equal" if dl_ok else "NOT EQUAL"))
    planned = [r for r in rows if r["api_ok"] and r["download_ok"]]
    least = PLAN_MIN if least is None else least
    for tag, n in sorted(least.items()):
        got = sum(1 for r in planned if r["tag"] == tag)
        out("files proved against %s: %d, at least %d expected" % (tag, got, n))
        assert got >= n, "BLOCKED: %d files proved against %s, at least %d expected; no plan written" % (got, tag, n)
    doc = {"root": root, "files_n": len(files), "files_bytes": sum(f["bytes"] for f in files),
           "releases_n": len(rels), "rows": rows, "planned_n": len(planned),
           "planned_bytes": sum(r["bytes"] for r in planned), "requests": COUNTS["requests"],
           "downloads": COUNTS["downloads"], "download_bytes": COUNTS["download_bytes"]}
    raw = json_bytes(doc)
    with open(plan_path, "wb") as fh:
        fh.write(raw)
    st = load_state(state_path)
    st["forensics"] = {"at": utc(time.time()), "plan_sha256": sha256_bytes(raw), "planned_n": len(planned)}
    save_state(st, state_path)
    out("FORENSICS PLAN: %d files, %d bytes, each held by a public Release and proved; %d rows, %d not proved; "
        "%d API requests, %d downloads, %d bytes; forensics-plan.json sha256 %s" % (
            len(planned), doc["planned_bytes"], len(rows), len(rows) - len(planned), COUNTS["requests"],
            COUNTS["downloads"], COUNTS["download_bytes"], sha256_bytes(raw)))
    return 0


def mode_forensics_remove(root=FORENSICS, plan_path=PLAN, removed_path=REMOVED, state_path=STATE):
    floors()
    st = load_state(state_path)
    with open(plan_path, "rb") as fh:
        raw = fh.read()
    assert sha256_bytes(raw) == st.get("forensics", {}).get("plan_sha256"), "forensics-plan.json is not the plan"
    doc = json.loads(raw)
    planned = [r for r in doc["rows"] if r["api_ok"] and r["download_ok"]]
    assert len(planned) == doc["planned_n"] and all(_under(r["path"], root) for r in planned), "the plan's rows"
    done = set()
    if os.path.exists(removed_path):
        with open(removed_path, encoding="utf-8") as fh:
            done = {json.loads(ln)["path"] for ln in fh if ln.strip()}
    for r in planned:
        if r["path"] in done:
            assert not os.path.lexists(r["path"]), "%s recorded removed and present" % r["path"]
            continue
        assert sha256_file(r["path"]) == (r["sha256"], r["bytes"]), \
            "BLOCKED: %s is not the file the plan proved; nothing removed by this run" % r["path"]
    free0, freed = free_bytes(), 0
    for r in planned:
        p = r["path"]
        if p in done:
            continue
        assert sha256_file(p) == (r["sha256"], r["bytes"]), "%s changed" % p
        ALLOWED_REMOVE.add(p)
        try:
            os.remove(p)
        finally:
            ALLOWED_REMOVE.discard(p)
        COUNTS["removed"] += 1
        assert not os.path.lexists(p), "%s is still there" % p
        freed += r["bytes"]
        row = {"path": p, "bytes": r["bytes"], "sha256": r["sha256"], "tag": r["tag"], "release_id": r["release_id"],
               "asset": r["asset"], "asset_id": r["asset_id"], "download_sha256": r["download_sha256"],
               "removed_ns": time.time_ns()}
        with open(removed_path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(row, sort_keys=True) + "\n")
        out("X %s %d %s removed: %s of %s" % (p, r["bytes"], r["sha256"], r["asset"], r["tag"]))
    with open(removed_path, "a", encoding="utf-8"):
        pass
    with open(removed_path, encoding="utf-8") as fh:
        recorded = [json.loads(ln) for ln in fh if ln.strip()]
    left = forensic_files(root, hashed=False)
    checks = {"every planned file absent": all(not os.path.lexists(r["path"]) for r in planned),
              "every removal recorded once": sorted(x["path"] for x in recorded) == sorted(r["path"]
                                                                                        for r in planned),
              "the store less exactly the planned files": len(left) == doc["files_n"] - len(planned)}
    for k, v in checks.items():
        out("G-FORENSIC %-44s %s" % (k, v))
    assert all(checks.values()), "G-FORENSIC FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    out("G-FORENSIC PASS: %d of %d removed, %d bytes; this run %d files, %d bytes; free %d before, %d after" % (
        len(recorded), len(planned), sum(x["bytes"] for x in recorded), COUNTS["removed"], freed, free0,
        free_bytes()))
    return 0


def mode_mark(name):
    assert name in ("pairoff", "timer", "retry", "revert"), "mark %r" % name
    st = load_state()
    marks = st.setdefault("marks", {})
    assert name not in marks, "mark %s already taken" % name
    marks[name] = {"ns": time.time_ns(), "units": units_now(), "archives": archives_now()}
    save_state(st)
    out("mark %s at %s" % (name, utc(marks[name]["ns"] / 1e9)))
    return 0


def mode_band(name):
    now = time.time()
    rb, pb = show(RB_SVC, ["ActiveState"]).get("ActiveState"), show(PB_SVC, ["ActiveState"]).get("ActiveState")
    ok, why = band_reading(name, now, rb, pb)
    out("band %s %s: %s" % (name, "OPEN" if ok else "closed", why))
    return 0 if ok else 3


def mode_pairwait():
    """Until the pair book archive's run begun after this mode's start - or resumed - reaches a terminal record and
    its service is idle: exit 0 complete or empty, 75 deferred, 1 halted, not begun within 120 s or still running
    after 3,600 s."""
    st = load_state()
    assert "pairoff" in st.get("marks", {}), "pairwait: no pairoff mark"
    t0 = time.time_ns()
    deadline = time.time() + PAIRWAIT_MAX_S
    while True:
        recs, _tail = ledger(PB_ARCH + "/ledger.jsonl")
        starts = [r for r in recs if r.get("event") == "start" and r.get("wall_ns", 0) >= t0 - 5 * 10 ** 9]
        svc = show(PB_SVC, ["ActiveState", "Result", "ExecMainStatus"])
        if starts:
            a = starts[-1]["run"]
            mine = [r for r in recs if r.get("run") == a]
            state = run_state(mine)
            if svc.get("ActiveState") not in RUNNING:
                for r in mine:
                    out("R %s" % json.dumps(r, sort_keys=True))
                out("PAIRWAIT run %d: %s; the service %s, Result %s, ExecMainStatus %s" % (
                    a, "INTERRUPTED" if state == "running" else state, svc.get("ActiveState"), svc.get("Result"),
                    svc.get("ExecMainStatus")))
                return {"complete": 0, "empty": 0, "deferred": 75}.get(state, 1)
        elif time.time_ns() > t0 + PAIRWAIT_START_S * 10 ** 9:
            out("PAIRWAIT: no run begun within %d s; the service %s" % (PAIRWAIT_START_S, svc))
            return 1
        if time.time() > deadline:
            out("PAIRWAIT: still running after %d s; the service %s" % (PAIRWAIT_MAX_S, svc))
            return 1
        time.sleep(PAIRWAIT_STEP_S)


def mode_pair():
    st = load_state()
    mark = st.get("marks", {}).get("pairoff")
    assert mark is not None, "pair: no pairoff mark"
    recs, _tail = ledger(PB_ARCH + "/ledger.jsonl")
    a, _start, mine = first_start(recs, mark["ns"])
    for r in mine:
        out("R %s" % json.dumps(r, sort_keys=True))
    with open(PB_ASVC + "/commit.txt", encoding="utf-8") as fh:
        commit = fh.read().strip()
    tag = "pairbook-streams-%d" % a if a is not None else None
    obj, peeled = ls_remote_tag(tag) if tag else (None, None)
    pb = show(UNITS["pairbook"], ["MainPID", "NRestarts", "ActiveState", "SubState", "UnitFileState", "Result"])
    tmr = show(PB_TIMER, ["ActiveState", "SubState", "UnitFileState", "NextElapseUSecRealtime"])
    svc = show(PB_SVC, ["ActiveState", "Result", "ExecMainStatus"])
    procs = processes_with(PB_ARGV)
    out("the run begun or resumed after the pairoff mark: %s; the tag %s at %s, peeled %s; the archive's commit %s" % (
        a, tag, obj, peeled, commit))
    out("the pair book %s; its archive's timer %s; its archive's service %s; processes of the pair book %s" % (
        pb, tmr, svc, procs))
    view = store_view(PB, "pb")
    for t in sorted(view["by_dir"]):
        out("RESIDUAL window %d %s: %d bytes of stream" % (t, utc(t), view["by_dir"][t]))
    out("the pair book's store: %d stream files, %d bytes, in %d windows; %d other files, %d bytes" % (
        view["streams_n"], view["streams_bytes"], len(view["by_dir"]), view["other_n"], view["other_bytes"]))
    checks = pair_reading(mine, obj, commit, pb, tmr, svc, procs)
    for k, v in checks.items():
        out("G-PAIR %-46s %s" % (k, v))
    bad = sorted(k for k, v in checks.items() if not v)
    out("G-PAIR %s" % ("PASS: %d of %d" % (len(checks), len(checks)) if not bad else "FAIL: %r" % bad))
    return 0 if not bad else 4


def mode_timer():
    now = time.time()
    kv = show(RB_TIMER, ["LoadState", "ActiveState", "SubState", "UnitFileState", "FragmentPath", "Unit",
                         "TimersCalendar", "TimersMonotonic", "NextElapseUSecRealtime", "NextElapseUSecMonotonic",
                         "AccuracyUSec", "LastTriggerUSec", "ActiveEnterTimestamp"])
    pb = show(PB_TIMER, ["ActiveState", "UnitFileState"])
    installed = sha256_file(UNIT_DIR + "/" + RB_TIMER)[0]
    out("the timer: %r; installed sha256 %s; the pair book archive's timer %r" % (kv, installed, pb))
    checks = timer_checks(kv, now, installed, pb)
    for k, v in checks.items():
        out("G-TIMER %-52s %s" % (k, v))
    bad = sorted(k for k, v in checks.items() if not v)
    assert not bad, "G-TIMER FAIL: %r" % bad
    out("G-TIMER PASS: %d of %d; the next run at %s" % (len(checks), len(checks), utc(next_calendar(now))))
    return 0


def read_slot(root, s):
    """Every slot.json of slot s, by index: [(k, doc)]."""
    d = os.path.join(root, str(s // DAY * DAY))
    found = []
    if os.path.isdir(d):
        for n in sorted(os.listdir(d)):
            m = RB_SLOT_RE.fullmatch(n)
            if m is not None and int(m.group(1)) == s:
                with open(os.path.join(d, n), "rb") as fh:
                    found.append((int(m.group(2)), json.loads(fh.read())))
    return sorted(found, key=lambda x: x[0])


def mode_first():
    """The reward book archive's first run on the new calendar, re-read: exit 3 while it has not ended or G-NEXT's
    slots are not yet due; on a deferral, READING G-RUN: DEFERRED and exit 3 until B-RETRY's run ends."""
    st = load_state()
    mark = st.get("marks", {}).get("timer")
    assert mark is not None, "first: no timer mark"
    elapse = next_calendar(mark["ns"] / 1e9)
    now = time.time()
    recs, _tail = ledger(RB_ARCH + "/ledger.jsonl")
    for r in recs:
        if r.get("event") == "start" and mark["ns"] <= r.get("wall_ns", 0) < (elapse - 1) * 10 ** 9:
            out("a run begun before the first elapse: %s at %s" % (r.get("run"), utc(r["wall_ns"] / 1e9)))
    a, start, mine = first_start(recs, (elapse - 1) * 10 ** 9)
    svc = show(RB_SVC, ["ActiveState", "Result", "ExecMainStatus", "ExecMainStartTimestamp", "ExecMainExitTimestamp"])
    if a is None:
        if now < elapse + FIRST_LATE_S:
            out("NOT YET: no run since %s, the first elapse; the service %s" % (utc(elapse), svc.get("ActiveState")))
            return 3
        out("READING G-TRIGGER: FAIL - no run begun by %s" % utc(elapse + FIRST_LATE_S))
        return 1
    state = run_state(mine)
    if state == "running" or svc.get("ActiveState") in RUNNING:
        out("NOT YET: run %d %s; the service %s" % (a, state, svc.get("ActiveState")))
        return 3
    for r in mine:
        out("R %s" % json.dumps(r, sort_keys=True))
    defers = sum(1 for r in mine if r.get("event") == "deferred")
    if state == "deferred":
        out("READING G-RUN: DEFERRED - run %d, deferral %d" % (a, defers))
        return 3
    drecs = []
    dpath = os.path.join(RB_ARCH, "runs", str(a), "delete.jsonl")
    if os.path.exists(dpath):
        with open(dpath, encoding="utf-8") as fh:
            drecs = [json.loads(ln) for ln in fh if ln.strip()]
    slots = next_slots(drecs[0]["start_ns"], drecs[-1]["removed_wall_ns"]) if drecs else []
    if state == "complete" and slots and now < slots[-1] + SLOT_JSON_AT + NEXT_SETTLE_S:
        out("NOT YET: run %d complete; G-NEXT's last slot %d is due at %s" % (
            a, slots[-1], utc(slots[-1] + SLOT_JSON_AT + NEXT_SETTLE_S)))
        return 3
    readings = {}
    tmr = show(RB_TIMER, ["LastTriggerUSec"])
    s0 = start["wall_ns"] // 10 ** 9
    readings["G-TRIGGER"], source, trig = trigger_reading(start.get("trigger"), elapse, s0,
                                                          stamp_of(tmr.get("LastTriggerUSec")))
    out("G-TRIGGER, by %s: the elapse %s, the trigger %s, the run's start record %s, %s" % (
        source, utc(elapse), utc(trig or 0), utc(s0), "a pending set resumed" if start.get("resumed") else "a new set"))
    comp = ([r for r in mine if r.get("event") == "complete"] or [{}])[-1]
    readings["G-RUN"] = (state == "complete" and defers <= 1 and not any(r.get("event") == "halt" for r in mine)
                         and svc.get("Result") == "success" and svc.get("ExecMainStatus") == "0"
                         and comp.get("started_outside") == 0 and comp.get("ended_outside") == 0)
    out("G-RUN: run %d %s, %d deferrals; the service Result %s, ExecMainStatus %s, %s to %s; %s requests and %s "
        "removals, %s started and %s ended outside the idle stretch; %s files, %s bytes" % (
            a, state, defers, svc.get("Result"), svc.get("ExecMainStatus"), svc.get("ExecMainStartTimestamp"),
            svc.get("ExecMainExitTimestamp"), comp.get("requests"), comp.get("removals"), comp.get("started_outside"),
            comp.get("ended_outside"), comp.get("assets_n"), comp.get("bytes_total")))
    with open(RB_ASVC + "/commit.txt", encoding="utf-8") as fh:
        commit = fh.read().strip()
    tag = "rewardbook-streams-%d" % a
    obj, peeled = ls_remote_tag(tag)
    readings["G-TAG"] = state == "complete" and obj == commit and peeled is None
    out("G-TAG: %s at %s, peeled %s; the archive's commit %s" % (tag, obj, peeled, commit))
    pid0 = (start.get("rewardbook") or {}).get("MainPID")
    rt, _tail = ledger(RB + "/runtime.jsonl")
    verdicts = []
    for s in slots:
        errs = [r for r in rt if r.get("event") == "error" and r.get("what") == "slot %d" % s]
        v, why = next_verdict(read_slot(RB, s), errs, pid0)
        verdicts.append((v, why))
        out("G-NEXT slot %d %s, decided at %s: %s - %s" % (s, utc(s), utc(s - DECIDE_S), v, why))
    reading = next_reading(verdicts)
    readings["G-NEXT"] = reading != "FAIL" and bool(slots)
    out("READING G-NEXT: %s over %d slots, the reward book's process at the run's start %s" % (reading, len(slots),
                                                                                              pid0))
    for k, v in readings.items():
        out("READING %-10s %s" % (k, "PASS" if v else "FAIL"))
    bad = sorted(k for k, v in readings.items() if not v)
    out("FIRST %s" % ("PASS: %d of %d" % (len(readings), len(readings)) if not bad else "FAIL: %r" % bad))
    return 0 if not bad else 1


def report_tokens():
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8", errors="replace") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    return tree == WORK and (rel in ("state.json", "forensics-plan.json", "forensics-removed.jsonl",
                                     "room-before.json", "room-after.json") or rel.startswith("logs/"))


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
    before = tree_count(FORENSICS)[0]
    out("reclaim: %d report tokens; the forensic store holds %d files" % (len(tokens), before))
    considered = named = kept = copied = held = 0
    for tree in trees:
        if tree == WORK and os.path.isdir(WT):
            pristine(WT)
        for dirpath, dirnames, filenames in os.walk(tree):
            dirnames[:] = sorted(d for d in dirnames if os.path.join(dirpath, d) not in (WT, TMP))
            for name in sorted(filenames):
                path = os.path.join(dirpath, name)
                if os.path.islink(path) or not os.path.isfile(path):
                    continue
                considered += 1
                rel = os.path.relpath(path, tree)
                h = sha256_file(path)[0]
                is_named = any(h[:k] in tokens for k in lengths)
                is_kept = by_name(tree, rel)
                if not (is_named or is_kept):
                    continue
                named += 1 if is_named else 0
                kept += 1 if is_kept and not is_named else 0
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--" + rel.replace("/", "--"))
                if os.path.exists(dest):
                    assert sha256_file(dest)[0] == h, "reclaim: %s exists with another sha256" % dest
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                size, free = os.path.getsize(path), free_bytes()
                assert free - size >= RECLAIM_FLOOR, "BLOCKED: reclaim: %d bytes free, %s is %d" % (free, path, size)
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest)[0] == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = tree_count(FORENSICS)[0]
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, %d already held; "
        "the forensic store %d -> %d files" % (considered, named, kept, copied, held, before, after))
    return 0

# ---- the self-test: literals, temporary trees under the work tree and a loopback server -----------------------


class _FakeGitHub(http.server.BaseHTTPRequestHandler):
    """GitHub's list endpoints and downloads for the self-test, from the class's `rels` and `blobs`."""
    rels, blobs, seen = [], {}, []

    def log_message(self, *args):
        pass

    def do_GET(self):
        u = urllib.parse.urlsplit(self.path)
        q = dict(urllib.parse.parse_qsl(u.query))
        type(self).seen.append((self.headers.get("User-Agent"), self.headers.get("Authorization"), u.path))
        page, per = int(q.get("page", "1")), int(q.get("per_page", "30"))
        body, ctype = None, "application/json"
        if u.path == "/repos/%s/releases" % REPO:
            body = json.dumps(self.rels[(page - 1) * per:page * per]).encode()
        m = re.fullmatch(r"/repos/%s/releases/([0-9]+)/assets" % re.escape(REPO), u.path)
        if m:
            rel = [r for r in self.rels if r["id"] == int(m.group(1))]
            assets = rel[0]["assets"] if rel else []
            body = json.dumps(assets[(page - 1) * per:page * per]).encode()
        if u.path.startswith("/%s/releases/download/" % REPO):
            body, ctype = self.blobs.get(urllib.parse.unquote(u.path)), "application/octet-stream"
        if body is None:
            self.send_response(404)
            self.end_headers()
            return
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def mode_selftest():
    checks = []

    def ok(cond, what):
        assert cond, "SELFTEST FAIL: %s" % what
        checks.append(what)
        out("ok %d %s" % (len(checks), what))

    if os.path.exists(TMP):
        shutil.rmtree(TMP)
    os.makedirs(TMP)
    d0 = 1794873600                                   # 2026-11-17 00:00:00 UTC
    # the calendar and the bands
    day = [d0 + CAL_FIRST_S + k * CAL_STEP_S for k in range(8)]
    ok([time.strftime("%H:%M:%S", time.gmtime(t)) for t in day] == ["01:30:20", "04:30:20", "07:30:20", "10:30:20",
                                                                    "13:30:20", "16:30:20", "19:30:20", "22:30:20"]
       and all(is_calendar(t) for t in day) and is_calendar(d0 - 5380) and not is_calendar(d0 + 5421)
       and not is_calendar(d0 + 1820),
       "the eight elapses of a day are systemd's iterations of *-*-* 01/3:30:20 UTC")
    ok(next_calendar(d0) == d0 + 5420 and next_calendar(d0 + 5420) == d0 + 16220
       and next_calendar(d0 + 81020) == d0 + DAY + 5420 and next_calendar(d0 + 37819.5) == d0 + 37820,
       "the next elapse is strictly after the instant, across midnight too")
    tb = lambda s, rb="inactive", pb="inactive": band_reading("timer", d0 + s, rb, pb)[0]
    ok(tb(36320) and tb(37220) and tb(69620) and not tb(36319) and not tb(37221) and not tb(25520)
       and not tb(80120) and not tb(36500, rb="activating") and not tb(36500, pb="active") and tb(36500, rb="failed"),
       "B-TIMER's band: 25 to 10 minutes before an elapse, 10:05:20 to 19:20:20 UTC, neither archive running")
    pbnd = lambda s, rb="inactive", pb="inactive": band_reading("pairoff", d0 + s, rb, pb)[0]
    ok(pbnd(27000) and pbnd(68400) and not pbnd(26999) and not pbnd(68401) and not pbnd(40000, pb="activating")
       and not pbnd(40000, rb="active"), "B-PAIR-OFF's band: 07:30:00 to 19:00:00 UTC, neither archive running")
    # G-TIMER on literals
    now = d0 + 36400
    kv = {"LoadState": "loaded", "ActiveState": "active", "SubState": "waiting", "UnitFileState": "enabled",
          "FragmentPath": "/etc/systemd/system/btc-rewardbook-archive.timer", "Unit": RB_SVC,
          "TimersCalendar": "{ OnCalendar=*-*-* 01/3:30:20 UTC ; next_elapse=Tue 2026-11-17 10:30:20 UTC }",
          "NextElapseUSecRealtime": "Tue 2026-11-17 10:30:20 UTC", "AccuracyUSec": "1s"}
    pbt = {"ActiveState": "inactive", "UnitFileState": "disabled"}
    good = timer_checks(kv, now, TIMER_SHA256, pbt)
    variants = [dict(kv, TimersMonotonic="{ OnActiveUSec=30min ; next_elapse=1h }"),
                dict(kv, TimersCalendar=kv["TimersCalendar"] + "\n{ OnCalendar=*-*-* 01:30:20 UTC ; next_elapse=x }"),
                dict(kv, NextElapseUSecRealtime="Wed 2026-11-18 01:30:20 UTC"), dict(kv, UnitFileState="disabled"),
                dict(kv, AccuracyUSec="1min"), dict(kv, Unit="other.service")]
    ok(all(good.values()) and len(good) == 11 and not any(all(timer_checks(v, now, TIMER_SHA256, pbt).values())
                                                          for v in variants)
       and not all(timer_checks(kv, now, OLD_TIMER_SHA256, pbt).values())
       and not all(timer_checks(kv, now, TIMER_SHA256, {"ActiveState": "active", "UnitFileState": "enabled"}).values()),
       "G-TIMER: 11 checks; a run on a start, a second calendar, another elapse, the unit disabled, another accuracy, "
       "another unit, TZ-34's file or the pair book archive's timer enabled each read FAIL")
    ok(stamp_of("Tue 2026-11-17 10:30:20 UTC") == d0 + 37820 and stamp_of("n/a") is None and stamp_of("") is None,
       "systemctl's stamps under TZ=UTC")
    # G-TRIGGER
    e = d0 + 37820
    trg = {"unit": RB_TIMER, "realtime_usec": str((e + 1) * 10 ** 6), "monotonic_usec": "1"}
    ok(trigger_reading(trg, e, e + 1, None)[0] and not trigger_reading(dict(trg, unit=RB_SVC), e, e + 1, None)[0]
       and not trigger_reading(dict(trg, realtime_usec=str((e - 1800) * 10 ** 6)), e, e - 1799, None)[0]
       and not trigger_reading(trg, e, e + 70, None)[0] and trigger_reading({"unit": None}, e, e, e)[0]
       and not trigger_reading({"unit": None}, e, e, None)[0],
       "G-TRIGGER: the timer's own trigger at the elapse; another unit, a trigger 1,800 s early, a late record and "
       "no trigger at all each read FAIL; LastTriggerUSec where systemd set none")
    # the runs of a ledger
    recs = [{"event": "start", "run": 5, "wall_ns": 100}, {"event": "complete", "run": 5, "wall_ns": 110},
            {"event": "start", "run": 9, "wall_ns": 200}, {"event": "deferred", "run": 9, "wall_ns": 210},
            {"event": "start", "run": 9, "wall_ns": 300}]
    a9, s9, m9 = first_start(recs, 150)
    a9b, s9b, m9b = first_start(recs, 250)
    ok(first_start(recs, 0)[0] == 5 and (a9, s9["wall_ns"], len(m9)) == (9, 200, 3) and run_state(m9) == "running"
       and run_state(m9[:2]) == "deferred" and run_state(recs[:2]) == "complete"
       and (a9b, s9b["wall_ns"], len(m9b)) == (9, 300, 1) and first_start(recs, 301)[0] is None,
       "a ledger's first start since an instant - a pending set resumed counts by its new start - and a run's "
       "state from its last start")
    # G-NEXT
    ok(next_slots(1000 * 10 ** 9, 1000 * 10 ** 9) == [1800] and next_slots(890 * 10 ** 9, 900 * 10 ** 9) == [900, 1800]
       and next_reading([("PASS", ""), ("UNDECIDABLE", "")]) == "UNDECIDABLE" and next_reading([]) == "UNDECIDABLE",
       "G-NEXT's slots across the removals, and its reading the worst")
    sj = {"pid": 77, "stream": {"opened": True, "off_reason": None}, "error": None, "stopped": False}
    ok(next_verdict([(0, sj)], [], "77")[0] == "PASS" and next_verdict([], [], "77")[0] == "FAIL"
       and next_verdict([(0, sj)], [{"error": "x"}], "77")[0] == "FAIL"
       and next_verdict([(0, dict(sj, stream={"opened": False, "off_reason": "floor"}))], [], "77")[0] == "UNDECIDABLE"
       and next_verdict([(0, sj)], [], "78")[0] == "UNDECIDABLE", "G-NEXT's verdict of one slot")
    # G-STILL
    u = {"recorder": {"MainPID": "1", "NRestarts": "0", "ActiveState": "active"},
         "pairbook": {"MainPID": "10", "NRestarts": "5", "ActiveState": "active"},
         "rewardbook": {"MainPID": "2", "NRestarts": "0", "ActiveState": "active"},
         "advisor": {"MainPID": "3", "NRestarts": "0", "ActiveState": "active"}}
    rs = [{"stopped": "10", "pid": "11", "NRestarts": "6"}]
    stopped = dict(u, pairbook={"MainPID": "0", "NRestarts": "6", "ActiveState": "inactive"})
    moved = dict(u, pairbook={"MainPID": "11", "NRestarts": "6", "ActiveState": "active"})
    ok(still_reading(u, u, [], False)[0] and still_reading(u, moved, rs, False)[0]
       and still_reading(u, stopped, rs, True)[0] and still_reading(u, stopped, [], True)[0]
       and not still_reading(u, stopped, rs, False)[0]
       and not still_reading(u, dict(u, recorder={"MainPID": "4", "NRestarts": "1", "ActiveState": "active"}), [], True)[0]
       and not still_reading(u, moved, [{"stopped": "9", "pid": "11", "NRestarts": "6"}], True)[0]
       and not still_reading(u, moved, [], False)[0],
       "G-STILL: unchanged; moved by its archive's restarts; stopped after B-PAIR-OFF alone; anything else FAIL")
    # G-PAIR
    run = [{"event": "start", "run": 7}, {"event": "set", "run": 7}, {"event": "delete", "run": 7},
           {"event": "restart", "run": 7}, {"event": "resume", "run": 7, "reading": "PASS"},
           {"event": "complete", "run": 7, "started_outside": 0, "ended_outside": 0}]
    off = {"MainPID": "0", "ActiveState": "inactive", "UnitFileState": "disabled"}
    toff = {"ActiveState": "inactive", "UnitFileState": "disabled"}
    sidle = {"ActiveState": "inactive"}
    gp = pair_reading(run, "c" * 40, "c" * 40, off, toff, sidle, [])
    bads = [pair_reading(run[:-1] + [{"event": "deferred", "run": 7}], "c" * 40, "c" * 40, off, toff, sidle, []),
            pair_reading(run, "d" * 40, "c" * 40, off, toff, sidle, []),
            pair_reading(run, "c" * 40, "c" * 40, dict(off, UnitFileState="enabled"), toff, sidle, []),
            pair_reading(run, "c" * 40, "c" * 40, off, toff, sidle, [4242]),
            pair_reading(run, "c" * 40, "c" * 40, off, dict(toff, UnitFileState="enabled"), sidle, []),
            pair_reading(run[:3] + run[5:], "c" * 40, "c" * 40, off, toff, sidle, []),
            pair_reading(run[:5] + [dict(run[5], started_outside=1)], "c" * 40, "c" * 40, off, toff, sidle, []),
            pair_reading(run, "c" * 40, "c" * 40, off, toff, {"ActiveState": "activating"}, [])]
    ok(all(gp.values()) and len(gp) == 8 and not any(all(b.values()) for b in bads),
       "G-PAIR: 8 checks; a deferred run, another tag, the pair book enabled or running, its timer enabled, no "
       "restart, a request outside the idle stretch or the service running each read FAIL")
    # G-ROOM
    base = STREAM_FLOOR + PEAK + ROOM_MIN
    ok(PEAK == 445535636 and room_reading(base - 10, 10) == (base, ROOM_MIN, True)
       and not room_reading(base - 11, 10)[2], "G-ROOM at its bound, and a byte below it")
    # NUMBER, reclaim's predicates, the timer file and the reward book's floor
    names = ["CryptoTZ/TZ-45-l0-rule-w.md", OWN_TZ, "CryptoReports/TZ-45-l0-rule-w-report.md"]
    ok(number_reading(names, OWN_TZ)[0] and not number_reading(names + ["CryptoTZ/TZ-46-other.md"], OWN_TZ)[0]
       and not number_reading(names + ["CryptoReports/TZ-46-capture-room-report.md"], OWN_TZ)[0],
       "NUMBER: this TZ's file alone of its number, and no report")
    ok(by_name(WORK, "logs/01.log") and by_name(WORK, "forensics-plan.json") and not by_name(WORK, "wt/x")
       and reclaimable(WORK) and not reclaimable("/root") and not reclaimable("/tmp/x"),
       "reclaim keeps by name the state, the plan, the removals, both room files and the logs")
    tfile = os.path.join(os.path.dirname(HERE), TIMER_REL)
    with open(tfile, "rb") as fh:
        traw = fh.read()
    tl = traw.decode("utf-8").split("\n")
    ok(sha256_bytes(traw) == TIMER_SHA256 and "OnCalendar=" + CALENDAR in tl and "AccuracySec=1s" in tl
       and "Unit=" + RB_SVC in tl and not any(x.startswith(("OnActiveSec", "OnBootSec", "OnStartupSec",
                                                             "OnUnitActiveSec", "OnUnitInactiveSec", "Persistent"))
                                              for x in tl),
       "the branch's timer: its SHA-256, one calendar, accuracy 1 s, its unit, no monotonic trigger")
    with open(os.path.join(os.path.dirname(HERE), TZ33_REL), "rb") as fh:
        t33 = fh.read()
    ok(sha256_bytes(t33) == TZ33_SHA256 and t33.split(b"\n")[189].startswith(b"STREAM_FLOOR = %d " % STREAM_FLOOR),
       "STREAM_FLOOR is the reward book's own, line 190 of its file as its unit runs it")
    # the hook's decisions
    al = {FORENSICS + "/a"}
    pol = lambda mode, ev, args: policy(mode, ev, args, al) is None
    ok(pol("room", "open", (WORK + "/room-after.json", "wb", 0)) and not pol("room", "open", ("/root/x", "w", 0))
       and pol("first", "open", (RB + "/1794873600/1794873600.0.slot.json", "rb", 0))
       and pol("first", "open", (RB + "/runtime.jsonl", "rb", 0))
       and not pol("first", "open", (RB + "/1794873600/1794873600.0.stream.jsonl.gz", "rb", 0))
       and not pol("first", "open", (RB + "/1794873600/1794873600.0.rewards.jsonl.gz", "rb", 0))
       and not pol("first", "open", (RB + "/1794873600/select.0.json", "rb", 0))
       and not pol("first", "open", (RB + "/runtime.jsonl", "ab", 0))
       and not pol("pair", "open", (PB + "/1794873600/window.json", "rb", 0))
       and not pol("room", "open", (RECORDER + "/runtime.jsonl", "rb", 0))
       and not pol("room", "os.scandir", (RECORDER,)) and pol("room", "os.scandir", (RB,))
       and pol("room", "os.scandir", (PB,)),
       "the hook: writes in the work tree alone; of the reward book its slot records and runtime.jsonl read, nothing "
       "else opened; nothing of the pair book or the recorder opened")
    ok(pol("forensics-remove", "os.remove", (FORENSICS + "/a", None))
       and not pol("forensics-remove", "os.remove", (FORENSICS + "/b", None))
       and not pol("forensics", "os.remove", (FORENSICS + "/a", None))
       and not pol("forensics-remove", "os.remove", (RB + "/1794873600/1794873600.0.slot.json", None))
       and pol("reclaim", "open", (FORENSICS + "/tz46-work--state.json", "xb", 0))
       and not pol("reclaim", "open", (FORENSICS + "/tz46-work--state.json", "wb", 0))
       and not pol("forensics", "open", (FORENSICS + "/a", "ab", 0)) and pol("forensics", "open", (FORENSICS + "/a", "rb", 0))
       and pol("selftest", "shutil.rmtree", (TMP, None)) and not pol("selftest", "shutil.rmtree", (FORENSICS, None)),
       "the hook: a forensic file removed only by forensics-remove and only where planned; the store written only "
       "by reclaim's exclusive create")
    ok(pol("forensics", "socket.getaddrinfo", ("api.github.com", 443)) and
       pol("forensics", "socket.getaddrinfo", ("release-assets.githubusercontent.com", 443))
       and not pol("forensics", "socket.getaddrinfo", ("clob.polymarket.com", 443))
       and not pol("forensics", "socket.getaddrinfo", ("fapi.binance.com", 443)),
       "the hook: GitHub's hosts alone are reached")
    # the stores by their directory entries
    rbt, pbt2 = os.path.join(TMP, "rb"), os.path.join(TMP, "pb")
    for p, n in ((rbt + "/1794873600/1794873600.0.stream.jsonl.gz", 100), (rbt + "/1794873600/1794873600.1.stream.jsonl.gz", 7),
                 (rbt + "/1794873600/1794873600.0.slot.json", 3), (rbt + "/1794873600/1794873600.0.rewards.jsonl.gz", 5),
                 (rbt + "/1794873600/select.0.json", 11), (rbt + "/runtime.jsonl", 13),
                 (pbt2 + "/1794873600/stream.jsonl.gz", 50), (pbt2 + "/1794873600/stream.1.jsonl.gz", 9),
                 (pbt2 + "/1794873600/window.json", 2), (pbt2 + "/1794874500/books.jsonl.gz", 4)):
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as fh:
            fh.write(b"x" * n)
    v1, v2 = store_view(rbt, "rb"), store_view(pbt2, "pb")
    ok((v1["streams_n"], v1["streams_bytes"], v1["other_n"], v1["other_bytes"], v1["dirs"]) == (2, 107, 4, 32, 1)
       and (v2["streams_n"], v2["streams_bytes"], v2["other_n"], v2["other_bytes"], v2["dirs"]) == (2, 59, 2, 6, 2)
       and v2["by_dir"] == {1794873600: 59}, "both stores' stream and other files by their own names")
    # the forensic store against a loopback GitHub
    fz = os.path.join(TMP, "forensics")
    files = {"a.tar": b"A" * 3000, "b.json": b"B" * 70, "c.log": b"C" * 9, "sub/d.copy": b"A" * 3000,
             "e.empty": b"", "f.bin": b"F" * 40, "g.bin": b"G" * 41, "h.bin": b"H" * 42}
    for name, data in files.items():
        os.makedirs(os.path.dirname(os.path.join(fz, name)), exist_ok=True)
        with open(os.path.join(fz, name), "wb") as fh:
            fh.write(data)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _FakeGitHub)
    port = srv.server_address[1]
    base = "http://127.0.0.1:%d" % port
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    dig = lambda b: "sha256:" + sha256_bytes(b)

    def asset(aid, tag, name, data, state="uploaded", digest=None):
        return {"id": aid, "name": name, "size": len(data), "state": state, "digest": digest or dig(data),
                "browser_download_url": download_url(base, tag, name)}
    _FakeGitHub.rels = [{"id": 1, "tag_name": "tz-44-l0-inputs", "draft": False,
                         "assets": [asset(11, "tz-44-l0-inputs", "a.tar", files["a.tar"]),
                                    asset(12, "tz-44-l0-inputs", "f.bin", files["f.bin"], state="starter")]},
                        {"id": 2, "tag_name": "rewardbook-streams-1", "draft": False,
                         "assets": [asset(21, "rewardbook-streams-1", "b.json", files["b.json"], digest=dig(b"other")),
                                    asset(22, "rewardbook-streams-1", "g.bin", files["g.bin"]),
                                    asset(23, "rewardbook-streams-1", "h.bin", files["h.bin"])]},
                        {"id": 3, "tag_name": "draft", "draft": True,
                         "assets": [asset(31, "draft", "c.log", files["c.log"])]}]
    _FakeGitHub.rels += [{"id": 100 + k, "tag_name": "pairbook-streams-%d" % k, "draft": False, "assets": []}
                         for k in range(120)]
    _FakeGitHub.blobs = {"/%s/releases/download/tz-44-l0-inputs/a.tar" % REPO: files["a.tar"],
                         "/%s/releases/download/rewardbook-streams-1/g.bin" % REPO: b"G" * 40 + b"g",
                         "/%s/releases/download/rewardbook-streams-1/h.bin" % REPO: files["h.bin"]}
    _FakeGitHub.seen = []
    plan, removed, sp = os.path.join(TMP, "plan.json"), os.path.join(TMP, "removed.jsonl"), os.path.join(TMP, "st.json")
    COUNTS.update({"requests": 0, "downloads": 0, "download_bytes": 0, "removed": 0})
    try:
        short = False
        try:
            mode_forensics(fz, base, base, plan, sp, least={"tz-44-l0-inputs": 3})
        except AssertionError as exc:
            short = "no plan written" in str(exc)
        ok(short and not os.path.exists(plan) and not os.path.exists(sp),
           "forensics: fewer files proved against a named Release than expected is BLOCKED, and no plan is written")
        COUNTS.update({"requests": 0, "downloads": 0, "download_bytes": 0, "removed": 0})
        mode_forensics(fz, base, base, plan, sp, least={"tz-44-l0-inputs": 2})
        with open(plan, "rb") as fh:
            pdoc = json.loads(fh.read())
        got = sorted((os.path.relpath(r["path"], fz), r["api_ok"], r["download_ok"]) for r in pdoc["rows"])
        ok(got == [("a.tar", True, True), ("g.bin", True, False), ("h.bin", True, True), ("sub/d.copy", True, True)]
           and pdoc["planned_n"] == 3 and pdoc["files_n"] == 7 and pdoc["releases_n"] == 123
           and COUNTS["downloads"] == 3 and COUNTS["requests"] == 9,
           "forensics: a file and its copy held by one asset, downloaded once; a digest of other bytes, an asset not "
           "uploaded, a draft and an empty file left; a download of other bytes not planned; 7 pages, 2 asset lists")
        ok(all(ua == UA and auth is None for ua, auth, _p in _FakeGitHub.seen),
           "every request names this file's User-Agent and carries no credential")
        with open(os.path.join(fz, "h.bin"), "ab") as fh:
            fh.write(b"!")
        blocked = False
        MODE[0] = "forensics-remove"
        try:
            mode_forensics_remove(fz, plan, removed, sp)
        except AssertionError as exc:
            blocked = "nothing removed" in str(exc)
        ok(blocked and all(os.path.exists(os.path.join(fz, n)) for n in ("a.tar", "sub/d.copy", "h.bin"))
           and not os.path.exists(removed), "a planned file changed after its proof: BLOCKED, nothing removed")
        with open(os.path.join(fz, "h.bin"), "wb") as fh:
            fh.write(files["h.bin"])
        mode_forensics_remove(fz, plan, removed, sp)
        left = sorted(os.path.relpath(f["path"], fz) for f in forensic_files(fz, hashed=False))
        ok(left == ["b.json", "c.log", "f.bin", "g.bin"] and os.path.exists(os.path.join(fz, "e.empty"))
           and COUNTS["removed"] == 3, "forensics-remove: the three proved files gone, every other file kept")
        COUNTS["removed"] = 0
        mode_forensics_remove(fz, plan, removed, sp)
        with open(removed, encoding="utf-8") as fh:
            rows = [json.loads(ln) for ln in fh if ln.strip()]
        ok(COUNTS["removed"] == 0 and len(rows) == 3, "forensics-remove again removes nothing and records nothing twice")
        guarded = False
        MODE[0] = "forensics"
        try:
            os.remove(os.path.join(FORENSICS, "never-there"))
        except GuardError:
            guarded = True
        ok(guarded, "the hook refuses a removal in the real forensic store outside forensics-remove")
    finally:
        MODE[0] = "selftest"
        srv.shutdown()
        srv.server_close()
    shutil.rmtree(TMP)
    ok(not os.path.exists(TMP), "the temporary trees removed")
    out("SELFTEST PASS: %d checks" % len(checks))
    return 0


def main(argv):
    if not argv:
        sys.exit("usage: %s MODE [ARG...]" % PYFILE)
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "number": mode_number, "selftest": mode_selftest,
             "still": mode_still, "forensics": mode_forensics, "forensics-remove": mode_forensics_remove,
             "pairwait": mode_pairwait, "pair": mode_pair, "timer": mode_timer, "first": mode_first}
    one = {"scratch": mode_scratch, "room": mode_room, "mark": mode_mark, "band": mode_band}
    rc = 1
    try:
        if mode == "reclaim":
            rc = mode_reclaim(rest)
        elif mode in one:
            assert len(rest) == 1, "%s takes one argument" % mode
            rc = one[mode](rest[0])
        else:
            assert mode in table and not rest, "unknown mode %r" % (argv,)
            rc = table[mode]()
    finally:    # printed on every exit, a BLOCK's and a failed assert's included
        out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
        out("opens refused: %d; reward book opens: %d; API requests %d, downloads %d, %d bytes; files removed %d" % (
            len(REFUSED), COUNTS["reward book opens"], COUNTS["requests"], COUNTS["downloads"],
            COUNTS["download_bytes"], COUNTS["removed"]))
    return rc or 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
