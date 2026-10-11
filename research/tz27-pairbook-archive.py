#!/usr/bin/env python3
"""TZ-27 - the pair book's streams, moved verbatim to a Release before the store's cap stops them.

    inventory TAG A   G-SET: every stream file, by the service's own predicate, of every window the pair
                      book had closed by the epoch A; each file read as bytes for its SHA-256 and never
                      decompressed; frozen into archive/set.json, the Release's limits asserted
    tagged            the set's tag on origin: its commit, the branch head, into state.json
    upload            B-UPLOAD, the Boss's block and nobody else's: the Release on the tag and one asset per
                      file of the set, streamed from the store and hashed as it is sent, under the token the
                      primary checkout's remote URL carries, or else the one gh holds; nothing prints either
    verify            G-UPLOAD and G-DOWNLOAD with no token: the Release's assets against the set by name,
                      bytes, state and digest; then every asset downloaded and hashed, nothing stored; exit 3
                      is NOT YET, until 120 s after upload's completion record
    delete            G-DELETE: each file of the verified set hashed again, then removed; nothing else
    removed           after B-DELETE, where the Boss ran delete: the set's files gone, as delete recorded them
    restart           G-RESTART, G-COUNTER and G-UNIT, from the service's own record, after B-KILL-SVC
    resume            G-RESUME: the restart's own window streamed; exit 3 is NOT YET
    started           after B-START-SVC, a FAIL's fallback: the pair book running again
    final             G-UNIT and G-STILL; the store's streams, free space and the next stop, projected
    path              P-PATH: the token-free path, proven on tz-01a-dataset's asset: the API and a download
    fingerprint       map section 0 against the primary checkout
    selftest          every rule of this file, on literals, a temporary store and a loopback server only
    still             the recorder's unit: the first run records it, a later run compares (G-STILL)
    mark NAME         an instant and the pair book's unit, into state.json
    scratch OWN       the UUID directories beside OWN, this session's directory: live or earlier
    reclaim TREE...   section 9

Every mode runs from its work tree, /root/tzNN-work, the current directory. It requests api.github.com,
uploads.github.com and github.com, and the address github.com redirects a download to, and nothing else;
upload alone sends a credential, and never across a redirect. A stream file is read as bytes for its SHA-256 and its upload, and nothing it says is read; no
mode prints a price, a size, a side, a book's hash or an outcome. An audit hook enforces section 2 of the
TZ. Exit 0: every assert held. Exit 1: an assert or a BLOCK, named. Exit 3: NOT YET. Run it with
/root/tz04a-env, the pair book's interpreter; it needs the standard library alone.

Written for CryptoTZ/TZ-27-pairbook-archive.md. The TZ is the specification.
"""

import ast
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
from fractions import Fraction

if not __debug__:
    sys.stderr.write("tz27: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(1)

# ---- the endpoints, and nothing else: three string constants carry a scheme separator ----------

API_BASE = "https://api.github.com"
UPLOAD_BASE = "https://uploads.github.com"
WEB_BASE = "https://github.com"

# ---- the TZ's constants: none of them is measured by this run -----------------------------------

MAP_REVISION = "2026-10-11-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 33, "tracked": 2, "reported": 1}

REPO = "seahomebatumi-ai/btc-5m-twap"
UA = "btc-5m-twap-tz27"
API_VERSION = "2022-11-28"
ACCEPT_API = "application/vnd.github+json"
ACCEPT_BLOB = "application/octet-stream"
CONTENT_TYPE = "application/gzip"

ROOT = "/var/lib/btc-pairbook"
RECORDER = "/var/lib/btc-recorder"
CHAINBOOK = "/var/lib/btc-chainbook"
SVC = "/root/btc-pairbook-svc"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = "/root/btc-forensics"
DISK_PATH = "/var/lib"

UNIT = "btc-pairbook.service"
UNITS = {"recorder": "btc-recorder.service", "pairbook": UNIT, "chainbook": "btc-chainbook.service"}
PYTHON = "/root/tz04a-env/venv/bin/python"
SERVICE_FILE = SVC + "/tz26-nesting-b3-capture.py"
SERVICE_ARGV = (PYTHON, "-B", "-u", SERVICE_FILE, "serve")
MEMORY_MAX = 134217728       # MemoryMax=128M, the pair book unit's ceiling

# the service's own constants: research/tz26-nesting-b3-capture.py lines 109, 110, 117, 132 and 133
WINDOW = 900
DOC_OFFSET = 545
CLOSE_OFFSET = 910
STREAM_FLOOR = 4500000000
STREAM_CAP = 8000000000

# this TZ's own
SETTLE_S = 60                # a window is taken once its window.json was due at least 60 s before A
BAND = (15, 480)             # B-KILL-SVC's band: seconds into the 900 s window, both included
RESTART_MAX_S = 60
RESUME_AFTER_S = 30          # resume reads the restart's window 30 s after its window.json is due
UPLOAD_SETTLE_S = 120        # verify reads the Release 120 s after upload's completion record: the API's
                             # anonymous replies may be cached for 60 s
ASSET_MAX_BYTES = 2147483647     # each file of a Release under 2 GiB
RELEASE_MAX_ASSETS = 1000        # up to 1000 assets a Release
RUN_MAX_ASSETS = 400             # a run uploads at most 400: under 500 content-creating requests an hour
UPLOAD_GAP_S = 1.0               # at least 1 s between two content-creating requests: under 80 a minute
UPLOAD_ATTEMPTS = 4
DOWNLOAD_ATTEMPTS = 3
WAIT_MIN_S = 60                  # a refused upload waits at least this, at most WAIT_MAX_S
WAIT_MAX_S = 900
API_TIMEOUT_S = 60
UPLOAD_TIMEOUT_S = 300
DOWNLOAD_TIMEOUT_S = 120
MEM_FLOOR = 93454336         # MemAvailable floor: twice the self-test's peak (TZ-27 section 0.4)
BASE_DRAINS = (43500000, 187760570)   # bytes a day: map 6, TZ-26's base and the fastest window

# P-PATH: the one Release that exists, map section 2.1
PATH_TAG = "tz-01a-dataset"
PATH_ASSET = "twap-divergence-observations.parquet"
PATH_BYTES = 76818669
PATH_SHA256 = "229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b"

WORK_RE = re.compile(r"/root/tz[0-9]{2}[a-z]?-work")
TAG_RE = re.compile(r"tz-[0-9]{2}[a-z]?-pairbook-streams")
STREAM_NAME_RE = re.compile(r"stream(?:\.([1-9][0-9]*))?\.jsonl\.gz")
ASSET_RE = re.compile(r"[0-9]{10}-stream(?:\.[1-9][0-9]*)?\.jsonl\.gz")
CREDENTIAL_RE = re.compile(r"[A-Za-z0-9_]{20,255}")
SHA_RE = re.compile(r"[0-9a-f]{64}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
LIVE_S = 60

SET_KEYS = frozenset(("tag", "as_of", "root", "repo", "assets", "assets_n", "bytes_total", "first_T", "last_T",
                      "windows", "deferred"))
SET_ASSET_KEYS = frozenset(("T", "file", "asset", "bytes", "sha256"))
SET_WINDOW_KEYS = frozenset(("T", "disposition", "streams", "stream_bytes", "taken"))
VERIFY_KEYS = frozenset(("tag", "release_id", "set_sha256", "assets", "assets_n", "bytes_total"))
VERIFY_ROW_KEYS = frozenset(("asset", "id", "bytes", "sha256", "api_bytes", "state", "digest", "url_ok",
                             "api_ok", "download_bytes", "download_sha256", "download_ok"))
FORBIDDEN_KEYS = frozenset(("price", "prices", "bid", "bids", "ask", "asks", "mid", "midpoint", "size",
                            "sizes", "level", "levels", "book", "books", "spread", "raw", "priceToBeat",
                            "finalPrice", "best_bid", "best_ask", "amount", "quote", "quotes", "side",
                            "outcomePrices", "hash"))

MODE = [None]
WORK = [None]
COUNTERS = {"requests": 0, "uploads": 0, "downloads": 0, "download_bytes": 0, "removed": 0}
_LOCK = threading.Lock()


class GuardError(RuntimeError):
    pass


def bump(name, by=1):
    with _LOCK:
        COUNTERS[name] += by
        return COUNTERS[name]

# ---- the audit hook: TZ-27 section 2 as a pure function, and the hook that applies it ------------


WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
PROCESS_EVENTS = ("subprocess.Popen", "os.system", "os.exec", "os.spawn", "os.posix_spawn", "os.fork",
                  "os.forkpty")
CHANGE_EVENTS = ("os.remove", "os.rename", "os.rmdir", "os.mkdir", "os.truncate", "os.chmod", "os.chown",
                 "os.utime", "os.link", "os.symlink", "shutil.rmtree")
HOOKED = ("open", "os.listdir", "os.scandir") + CHANGE_EVENTS + PROCESS_EVENTS
READ_MODES = ("inventory", "upload", "delete", "restart", "resume", "started", "final")
LIST_MODES = ("inventory", "delete", "restart", "final")
NO_PROCESS = ("inventory", "delete")
REFUSED = []
ALLOWED_REMOVE = set()
STORE_OPENS = [0]


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


def _protected(p):
    return _under(p, RECORDER) or _under(p, CHAINBOOK)


def policy(mode, event, args, work, allowed):
    """None where section 2 allows the event in this mode; otherwise the reason it is refused."""
    if event in PROCESS_EVENTS:
        return "a process started by %s" % mode if mode in NO_PROCESS else None
    p = _path(args[0]) if args else None
    if event == "open":
        if p is None:
            return None
        wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
        w = _writing(wm, fl)
        if _protected(p):
            return "another capture's root"
        if _under(p, ROOT):
            if w:
                return "a write under the pair book's root"
            return None if mode in READ_MODES else "a read under the pair book's root"
        if _under(p, FORENSICS) and w:
            return None if mode == "reclaim" and _exclusive(wm, fl) else "a write into the forensic store"
        if w and not (work is not None and _under(p, work)):
            return "a write outside the work tree"
        return None
    if event in ("os.listdir", "os.scandir"):
        if p is None:
            return None
        if _protected(p):
            return "a listing under another capture's root"
        if _under(p, ROOT):
            return None if mode in LIST_MODES else "a listing under the pair book's root"
        return None
    if event in CHANGE_EVENTS:
        paths = [p]
        if event in ("os.rename", "os.link", "os.symlink") and len(args) > 1:
            paths.append(_path(args[1]))
        for q in paths:
            if q is None:
                continue
            if _under(q, ROOT):
                if event == "os.remove" and mode == "delete" and q in allowed:
                    continue
                return "a change under the pair book's root"
            if _protected(q) or _under(q, FORENSICS):
                return "a change under a protected root"
            if not (work is not None and _under(q, work)):
                return "a change outside the work tree"
        return None
    return None


def _audit(event, args):
    if event not in HOOKED:
        return
    why = policy(MODE[0], event, args, WORK[0], ALLOWED_REMOVE)
    if why is not None:
        REFUSED.append((event, str(args[0]) if args else ""))
        raise GuardError("%s refused in mode %s, %s: %r" % (event, MODE[0], why, args[0] if args else None))
    if event == "open" and args:
        p = _path(args[0])
        if p is not None and _under(p, ROOT):
            STORE_OPENS[0] += 1


sys.addaudithook(_audit)

# ---- small helpers -------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return datetime.datetime.fromtimestamp(float(t), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path, chunk=1 << 20):
    """The SHA-256 and the byte count of a file read as bytes; its pages are dropped from the cache after."""
    h, n = hashlib.sha256(), 0
    with open(path, "rb") as fh:
        for b in iter(lambda: fh.read(chunk), b""):
            h.update(b)
            n += len(b)
        try:
            os.posix_fadvise(fh.fileno(), 0, 0, os.POSIX_FADV_DONTNEED)
        except (AttributeError, OSError):
            pass
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


def floor_check():
    """Before a mode that reads the store, the network or the forensic store: the memory floor (0.4)."""
    avail = mem_available()
    out("MemAvailable %d bytes, floor %d" % (avail, MEM_FLOOR))
    assert avail >= MEM_FLOOR, "BLOCKED: MemAvailable %d bytes, below %d" % (avail, MEM_FLOOR)


def forbid(obj, what, depth=0):
    """No price, size, level, side or hash key leaves this instrument through an output file."""
    assert depth < 12, "%s nested too deep" % what
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert k not in FORBIDDEN_KEYS, "%s carries a forbidden key: %s" % (what, k)
            forbid(v, what, depth + 1)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            forbid(v, what, depth + 1)


def assert_keys(obj, allowed, what):
    assert frozenset(obj) == allowed, "%s key set %s, required %s" % (what, sorted(obj), sorted(allowed))
    forbid(obj, what)


def wpath(*parts):
    return os.path.join(WORK[0], *parts)


def load_state():
    p = wpath("state.json")
    if not os.path.exists(p):
        return {}
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def save_state(state):
    p = wpath("state.json")
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(state, sort_keys=True, indent=1) + "\n")
    os.replace(tmp, p)


def decimals(fr, places):
    scale = 10 ** places
    q, r = divmod(fr.numerator * scale, fr.denominator)
    if 2 * r >= fr.denominator:
        q += 1
    s = str(q).rjust(places + 1, "0")
    return s[:-places] + "." + s[-places:] if places else s


def phase_of(t):
    return int(t) % WINDOW


def in_band(t):
    return BAND[0] <= phase_of(t) <= BAND[1]

# ---- the store, by the service's own predicates -------------------------------------------------


def is_stream(name):
    """The service's stream-file predicate (research/tz26-nesting-b3-capture.py line 804)."""
    return name.startswith("stream") and name.endswith(".jsonl.gz")


def stream_index(name):
    """0 for stream.jsonl.gz, k for stream.k.jsonl.gz - next_stream_path's names (lines 750 to 756)."""
    m = STREAM_NAME_RE.fullmatch(name)
    assert m is not None, "a stream file named %r, not a name next_stream_path writes" % name
    return 0 if m.group(1) is None else int(m.group(1))


def window_dirs(root):
    """The numeric directories under root - the service's predicate, line 800 - each asserted to be a
    window: ten digits, a multiple of 900. In order of T."""
    with os.scandir(root) as it:
        names = [d.name for d in it if d.is_dir(follow_symlinks=False) and d.name.isdigit()]
    found = []
    for n in names:
        assert re.fullmatch(r"[0-9]{10}", n) and int(n) % WINDOW == 0, "a window directory named %r" % n
        found.append(int(n))
    return sorted(found)


def window_names(root, T):
    with os.scandir(os.path.join(root, str(T))) as it:
        return sorted(e.name for e in it)


def stream_bytes_view(root, upto=None):
    """The bytes of every stream file under root by directory entries alone - the service's own
    stream_bytes_total, lines 794 to 806 - over the windows T <= upto where upto is given."""
    total = 0
    for T in window_dirs(root):
        if upto is not None and T > upto:
            continue
        with os.scandir(os.path.join(root, str(T))) as it:
            for f in it:
                if is_stream(f.name):
                    total += f.stat(follow_symlinks=False).st_size
    return total


def inventory(root, a, max_assets=RUN_MAX_ASSETS, asset_max=ASSET_MAX_BYTES):
    """The set as of the epoch a: every stream file of every window whose window.json exists and was due at
    least SETTLE_S before a - T + 910 + 60 <= a - in order of T and of the file's index; the first
    max_assets taken, each read as bytes for its SHA-256, its size and mtime equal before and after.
    A window due after that is counted as open and listed nowhere, so the set is a function of a alone."""
    windows, files, open_n = [], [], 0
    for T in window_dirs(root):
        if T + CLOSE_OFFSET + SETTLE_S > a:
            open_n += 1
            continue
        names = window_names(root, T)
        streams = sorted((n for n in names if is_stream(n)), key=stream_index)
        sizes = [os.stat(os.path.join(root, str(T), n), follow_symlinks=False).st_size for n in streams]
        disp = "closed" if "window.json" in names else "unclosed"
        windows.append({"T": T, "disposition": disp, "streams": len(streams), "stream_bytes": sum(sizes),
                        "taken": 0})
        if disp == "closed":
            files.extend((T, n) for n in streams)
    taken, assets = files[:max_assets], []
    for T, n in taken:
        p = os.path.join(root, str(T), n)
        before = os.stat(p, follow_symlinks=False)
        h, nbytes = sha256_file(p)
        after = os.stat(p, follow_symlinks=False)
        assert before.st_size == nbytes == after.st_size and before.st_mtime_ns == after.st_mtime_ns, \
            "%s changed while it was read" % p
        assert nbytes <= asset_max, "%s holds %d bytes, above a Release asset's %d" % (p, nbytes, asset_max)
        assets.append({"T": T, "file": n, "asset": "%d-%s" % (T, n), "bytes": nbytes, "sha256": h})
    for w in windows:
        w["taken"] = sum(1 for T, _n in taken if T == w["T"])
    return assets, windows, len(files) - len(taken), open_n


def set_document(tag, a, root, assets, windows, deferred, max_assets=RUN_MAX_ASSETS):
    names = [x["asset"] for x in assets]
    assert TAG_RE.fullmatch(tag), "a tag named %r" % tag
    assert assets, "BLOCKED: no stream file of a closed window, nothing to archive"
    assert len(set(names)) == len(names), "two assets share a name"
    assert all(ASSET_RE.fullmatch(n) for n in names), "an asset name outside %s" % ASSET_RE.pattern
    assert len(assets) <= max_assets <= RELEASE_MAX_ASSETS, "%d assets, above %d" % (len(assets), max_assets)
    doc = {"tag": tag, "as_of": a, "root": root, "repo": REPO, "assets": assets, "assets_n": len(assets),
           "bytes_total": sum(x["bytes"] for x in assets), "first_T": assets[0]["T"], "last_T": assets[-1]["T"],
           "windows": windows, "deferred": deferred}
    assert_keys(doc, SET_KEYS, "set.json")
    for x in assets:
        assert_keys(x, SET_ASSET_KEYS, "set.json asset")
        assert SHA_RE.fullmatch(x["sha256"])
    for w in windows:
        assert_keys(w, SET_WINDOW_KEYS, "set.json window")
    return doc


def read_set(st):
    """set.json as inventory froze it, asserted by its SHA-256 in state.json."""
    s = st.get("set")
    assert s, "no set: inventory has not run"
    with open(wpath("archive", "set.json"), "rb") as fh:
        raw = fh.read()
    assert sha256_bytes(raw) == s["sha256"], "set.json is not the set inventory froze"
    return json.loads(raw), raw


def store_path(root, x):
    return os.path.join(root, str(x["T"]), x["file"])

# ---- the network: three hosts, every header fixed ------------------------------------------------


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """A request that carries a credential is never sent on to another URL: a redirect is an error."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def opener(follow):
    return urllib.request.build_opener() if follow else urllib.request.build_opener(_NoRedirect())


def build_request(method, url, token=None, accept=ACCEPT_API, data=None, ctype=None, length=None):
    """The one builder of every request: Accept, this file's User-Agent and the API version; the token,
    a body's type and its length only where given."""
    headers = {"Accept": accept, "User-Agent": UA, "X-GitHub-Api-Version": API_VERSION}
    if token is not None:
        headers["Authorization"] = "Bearer " + token
    if ctype is not None:
        headers["Content-Type"] = ctype
    if length is not None:
        headers["Content-Length"] = str(length)
    return urllib.request.Request(url, data=data, method=method, headers=headers)


def header_of(headers, name):
    for k, v in headers.items():
        if k.lower() == name.lower():
            return v
    return None


def call(op, req, timeout):
    """One request, no retry: (status, body, headers), or (None, b'', {}) where no status came back."""
    bump("requests")
    try:
        with op.open(req, timeout=timeout) as resp:
            return int(resp.status), resp.read(), dict(resp.headers)
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read()
        except Exception:
            body = b""
        return int(exc.code), body, dict(exc.headers or {})
    except (urllib.error.URLError, OSError, http.client.HTTPException) as exc:
        out("no reply: %s" % type(exc).__name__)
        return None, b"", {}


class HashingReader:
    """A file's bytes as they are sent, hashed and counted on the way."""

    def __init__(self, fh):
        self.fh, self.h, self.n = fh, hashlib.sha256(), 0

    def read(self, size=-1):
        b = self.fh.read(size)
        self.h.update(b)
        self.n += len(b)
        return b


class GitHub:
    """The Release endpoints this TZ needs. Anonymous where token is None; with a token every request goes
    through the opener that follows no redirect."""

    def __init__(self, token=None, api=API_BASE, uploads=UPLOAD_BASE, web=WEB_BASE):
        self.token, self.api, self.uploads, self.web = token, api, uploads, web
        self.op = opener(follow=token is None)
        self.last_write = 0.0
        self.gap_s = UPLOAD_GAP_S

    def _json(self, method, url, body=None):
        data = None if body is None else json.dumps(body).encode("utf-8")
        req = build_request(method, url, token=self.token, data=data,
                            ctype=None if body is None else "application/json")
        status, raw, hdr = call(self.op, req, API_TIMEOUT_S)
        try:
            doc = json.loads(raw) if raw else None
        except ValueError:
            doc = None
        return status, doc, hdr

    def pace(self):
        wait = self.last_write + self.gap_s - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        self.last_write = time.monotonic()

    def release_by_tag(self, tag):
        status, doc, _h = self._json("GET", "%s/repos/%s/releases/tags/%s" % (self.api, REPO, urllib.parse.quote(tag)))
        assert status in (200, 404), "release by tag %s: status %r" % (tag, status)
        return doc if status == 200 else None

    def create_release(self, tag, name, body):
        assert self.token is not None
        self.pace()
        status, doc, _h = self._json("POST", "%s/repos/%s/releases" % (self.api, REPO),
                                     {"tag_name": tag, "name": name, "body": body, "draft": False,
                                      "prerelease": False, "make_latest": "false"})
        assert status == 201 and isinstance(doc, dict), "create release %s: status %r %r" % (
            tag, status, (doc or {}).get("message") if isinstance(doc, dict) else None)
        return doc

    def assets(self, rid):
        found, page = [], 1
        while True:
            status, doc, _h = self._json("GET", "%s/repos/%s/releases/%d/assets?per_page=100&page=%d" % (
                self.api, REPO, rid, page))
            assert status == 200 and isinstance(doc, list), "assets of release %d page %d: status %r" % (rid, page, status)
            found.extend(doc)
            if len(doc) < 100:
                return found
            page += 1

    def delete_asset(self, aid):
        assert self.token is not None
        self.pace()
        status, _doc, _h = self._json("DELETE", "%s/repos/%s/releases/assets/%d" % (self.api, REPO, aid))
        assert status == 204, "delete asset %d: status %r" % (aid, status)

    def upload(self, rid, name, path, nbytes):
        """One asset, its body streamed from the file and hashed as it is sent."""
        assert self.token is not None
        self.pace()
        url = "%s/repos/%s/releases/%d/assets?name=%s" % (self.uploads, REPO, rid, urllib.parse.quote(name))
        with open(path, "rb") as fh:
            rd = HashingReader(fh)
            req = build_request("POST", url, token=self.token, data=rd, ctype=CONTENT_TYPE, length=nbytes)
            status, raw, hdr = call(self.op, req, UPLOAD_TIMEOUT_S)
            try:
                os.posix_fadvise(fh.fileno(), 0, 0, os.POSIX_FADV_DONTNEED)
            except (AttributeError, OSError):
                pass
        bump("uploads")
        try:
            doc = json.loads(raw) if raw else None
        except ValueError:
            doc = None
        return status, doc, hdr, rd.h.hexdigest(), rd.n

    def download_url(self, tag, name):
        return "%s/%s/releases/download/%s/%s" % (self.web, REPO, urllib.parse.quote(tag), urllib.parse.quote(name))

    def download(self, url):
        """A download streamed into SHA-256 and a byte count, nothing stored: (status, bytes, sha256)."""
        req = build_request("GET", url, accept=ACCEPT_BLOB)
        bump("requests")
        h, n = hashlib.sha256(), 0
        with self.op.open(req, timeout=DOWNLOAD_TIMEOUT_S) as resp:
            status = int(resp.status)
            for b in iter(lambda: resp.read(1 << 20), b""):
                h.update(b)
                n += len(b)
        bump("downloads")
        bump("download_bytes", n)
        return status, n, h.hexdigest()


def download_checked(gh, url, attempts=DOWNLOAD_ATTEMPTS, backoff_s=10):
    """A download with up to `attempts` tries where the transfer breaks; a whole reply is never retried."""
    for k in range(1, attempts + 1):
        try:
            return gh.download(url)
        except urllib.error.HTTPError as exc:
            if exc.code < 500 or k == attempts:
                return int(exc.code), 0, None
        except (urllib.error.URLError, OSError, http.client.HTTPException) as exc:
            out("download %s broke: %s, attempt %d of %d" % (url.rsplit("/", 1)[-1], type(exc).__name__, k, attempts))
            if k == attempts:
                return None, 0, None
        time.sleep(backoff_s * k)
    return None, 0, None


def asset_row(x, a, url):
    """The Release's own record of one asset of the set, against the set."""
    row = {"asset": x["asset"], "bytes": x["bytes"], "sha256": x["sha256"], "id": None, "api_bytes": None,
           "state": None, "digest": None, "url_ok": False, "api_ok": False, "download_bytes": None,
           "download_sha256": None, "download_ok": False}
    if a is not None:
        row.update({"id": a.get("id"), "api_bytes": a.get("size"), "state": a.get("state"),
                    "digest": a.get("digest"), "url_ok": a.get("browser_download_url") == url})
        row["api_ok"] = (row["state"] == "uploaded" and row["api_bytes"] == x["bytes"]
                         and row["digest"] == "sha256:" + x["sha256"] and row["url_ok"])
    return row


def verify_release(gh, tag, doc, download=True):
    """G-UPLOAD, then G-DOWNLOAD where G-UPLOAD holds: (release, rows, missing, extra)."""
    rel = gh.release_by_tag(tag)
    if rel is None:
        return None, [], [x["asset"] for x in doc["assets"]], []
    by = {a.get("name"): a for a in gh.assets(int(rel["id"]))}
    want = [x["asset"] for x in doc["assets"]]
    missing, extra = sorted(set(want) - set(by)), sorted(set(by) - set(want))
    rows = [asset_row(x, by.get(x["asset"]), gh.download_url(tag, x["asset"])) for x in doc["assets"]]
    if download and not missing and not extra and all(r["api_ok"] for r in rows):
        for r in rows:
            status, n, h = download_checked(gh, gh.download_url(tag, r["asset"]))
            r["download_bytes"], r["download_sha256"] = n, h
            r["download_ok"] = status == 200 and n == r["bytes"] and h == r["sha256"]
            out("D %s %s bytes %d sha256 %s" % (r["asset"], "equal" if r["download_ok"] else "DIFFERS", n, h))
    return rel, rows, missing, extra


def release_reading(rel, tag, rows, missing, extra):
    checks = {"release published on the tag": rel is not None and rel.get("tag_name") == tag
              and rel.get("draft") is False,
              "no asset missing": not missing, "no asset beyond the set": not extra,
              "every asset uploaded, its bytes and digest the set's": bool(rows) and all(r["api_ok"] for r in rows),
              "every download the set's bytes and SHA-256": bool(rows) and all(r["download_ok"] for r in rows)}
    return checks


def token_of(url):
    """The credential a remote URL carries - https, [user:]TOKEN@github.com/<REPO>[.git] - or None where it
    carries none. A remote that is not this repository over https stops the run; no message names a token."""
    u = urllib.parse.urlsplit(url.strip())
    path = u.path.rstrip("/")
    if path.endswith(".git"):
        path = path[:-4]
    assert u.scheme == "https" and u.hostname == "github.com" and path == "/" + REPO, \
        "the remote is not github.com/%s over https" % REPO
    tok = u.password if u.password else u.username
    return tok if tok is not None and CREDENTIAL_RE.fullmatch(tok) is not None else None


def credential():
    """B-UPLOAD's credential and where it came from: the primary checkout's remote URL, or else the token gh
    holds. Only upload calls this; no message names the token."""
    cp = subprocess.run(["git", "-C", PRIMARY, "remote", "get-url", "origin"], capture_output=True, text=True)
    assert cp.returncode == 0, "git remote get-url origin: exit %d" % cp.returncode
    tok = token_of(cp.stdout)
    if tok is not None:
        return tok, "the primary checkout's remote URL"
    exe = shutil.which("gh")
    if exe is not None:
        cp = subprocess.run([exe, "auth", "token", "--hostname", "github.com"], capture_output=True, text=True)
        tok = cp.stdout.strip()
        if cp.returncode == 0 and CREDENTIAL_RE.fullmatch(tok) is not None:
            return tok, "gh auth token"
    raise AssertionError("UPLOAD REFUSED: no credential - the remote URL carries none and gh holds none")


def wait_for(status, hdr, attempt, wait_min=WAIT_MIN_S):
    """How long a refused or broken upload waits before its next attempt, as GitHub's documentation asks of a
    secondary limit - retry-after, else x-ratelimit-reset where x-ratelimit-remaining is 0, else at least a
    minute, doubling with each attempt - bounded by WAIT_MAX_S; None where it must stop."""
    if status in (403, 429):
        w = int(header_of(hdr, "Retry-After") or 0)
        if header_of(hdr, "X-RateLimit-Remaining") == "0":
            w = max(w, int(header_of(hdr, "X-RateLimit-Reset") or 0) - int(time.time()))
        return min(max(w, wait_min * 2 ** (attempt - 1)), WAIT_MAX_S)
    if status is None or status >= 500:
        return 10 * attempt
    if status == 422:
        return 2
    return None


def matches(a, x):
    """An asset already in the Release that this run keeps: uploaded, the set's bytes, and the set's digest
    where the API gives one; verify then requires the digest."""
    return (a.get("state") == "uploaded" and a.get("size") == x["bytes"]
            and a.get("digest") in (None, "sha256:" + x["sha256"]))


def upload_set(gh, rel, doc, root, log, wait_min=WAIT_MIN_S):
    """Every asset of the set into the Release, in order: kept where it already matches, otherwise any
    asset under its name removed and the file sent again; at most UPLOAD_ATTEMPTS a file."""
    rid = int(rel["id"])
    have = {a.get("name"): a for a in gh.assets(rid)}
    beyond = sorted(set(have) - {x["asset"] for x in doc["assets"]})
    assert not beyond, "the Release holds assets outside the set: %r" % beyond[:5]
    sent = held = 0
    for x in doc["assets"]:
        a = have.get(x["asset"])
        if a is not None and matches(a, x):
            held += 1
            log({"asset": x["asset"], "action": "held", "id": a.get("id")})
            continue
        path = store_path(root, x)
        for attempt in range(1, UPLOAD_ATTEMPTS + 1):
            if a is not None:
                gh.delete_asset(int(a["id"]))
                log({"asset": x["asset"], "action": "removed from the Release", "id": a.get("id"),
                     "state": a.get("state")})
                a = None
            assert os.stat(path).st_size == x["bytes"], "%s is not the set's %d bytes" % (path, x["bytes"])
            status, doc_, hdr, sent_sha, sent_n = gh.upload(rid, x["asset"], path, x["bytes"])
            if status == 201 and isinstance(doc_, dict):
                assert sent_n == x["bytes"] and sent_sha == x["sha256"], \
                    "%s sent %d bytes, SHA-256 %s: not the set's" % (path, sent_n, sent_sha)
                assert doc_.get("name") == x["asset"] and doc_.get("size") == x["bytes"] \
                    and doc_.get("state") == "uploaded", "%s: the Release recorded %r" % (x["asset"], doc_)
                assert doc_.get("digest") in (None, "sha256:" + x["sha256"]), \
                    "%s: the Release's digest %r" % (x["asset"], doc_.get("digest"))
                sent += 1
                log({"asset": x["asset"], "action": "uploaded", "id": doc_.get("id"), "bytes": sent_n,
                     "sha256": sent_sha, "digest": doc_.get("digest")})
                break
            w = wait_for(status, hdr, attempt, wait_min)
            assert w is not None, "UPLOAD REFUSED: %s status %r" % (x["asset"], status)
            log({"asset": x["asset"], "action": "refused", "status": status, "attempt": attempt, "wait_s": w})
            out("%s: status %r, attempt %d of %d; waiting %d s" % (x["asset"], status, attempt, UPLOAD_ATTEMPTS, w))
            time.sleep(w)
            a = {b.get("name"): b for b in gh.assets(rid)}.get(x["asset"])
            if a is not None and matches(a, x):
                held += 1
                log({"asset": x["asset"], "action": "held", "id": a.get("id")})
                break
        else:
            raise AssertionError("UPLOAD INCOMPLETE at %s after %d attempts: run B-UPLOAD again" % (
                x["asset"], UPLOAD_ATTEMPTS))
    return sent, held


def delete_set(root, doc, done, now, log):
    """G-DELETE: each file of the set, in order - its window closed and its window.json there, the file's
    bytes hashed again equal to the set's - removed, logged at once, and its window's other entries left as
    they were. A file already absent counts only where this mode's own log records its removal."""
    rows, removed, freed, already = [], 0, 0, 0
    for x in doc["assets"]:
        p = store_path(root, x)
        names = window_names(root, x["T"])
        assert "window.json" in names and x["T"] + CLOSE_OFFSET + SETTLE_S <= now, \
            "window %d is not closed" % x["T"]
        if x["file"] not in names:
            assert x["asset"] in done, "%s is absent and no removal of it is recorded" % p
            already += 1
            continue
        h, n = sha256_file(p)
        assert (h, n) == (x["sha256"], x["bytes"]), "%s is %d bytes, SHA-256 %s: not the set's" % (p, n, h)
        ALLOWED_REMOVE.add(os.path.abspath(p))
        try:
            os.remove(p)
        finally:
            ALLOWED_REMOVE.discard(os.path.abspath(p))
        bump("removed")
        assert not os.path.lexists(p), "%s is still there" % p
        assert window_names(root, x["T"]) == [m for m in names if m != x["file"]], \
            "window %d lost more than %s" % (x["T"], x["file"])
        removed += 1
        freed += n
        row = {"asset": x["asset"], "T": x["T"], "file": x["file"], "bytes": n, "sha256": h,
               "removed_wall_ns": time.time_ns()}
        log(row)
        rows.append(row)
    return rows, removed, freed, already

# ---- the service's record ------------------------------------------------------------------------


def read_runtime(path):
    recs = []
    with open(path, "rb") as fh:
        for ln in fh.read().split(b"\n"):
            if ln.strip():
                recs.append(json.loads(ln))
    return recs


def restart_reading(recs, mark):
    """G-RESTART: the first stop record at or after the mark is the marked MainPID's, inside the band, and the
    record right after it is a start of another process within RESTART_MAX_S, on the code the last start
    before the mark ran."""
    before = [r for r in recs if r.get("wall_ns", 0) < mark["ns"] and r.get("event") == "start"]
    after = [r for r in recs if r.get("wall_ns", 0) >= mark["ns"]]
    k = next((i for i, r in enumerate(after) if r.get("event") == "stop"), None)
    stop, start = ({}, {}) if k is None else (after[k], after[k + 1] if k + 1 < len(after) else {})
    prev = before[-1] if before else {}
    checks = {"a stop of the marked process": stop.get("event") == "stop" and str(stop.get("pid")) == str(mark["MainPID"]),
              "stopped inside the band": stop.get("event") == "stop"
              and BAND[0] <= phase_of(stop.get("wall_ns", 0) // 10 ** 9) <= BAND[1] + 1,
              "a start of another process": start.get("event") == "start" and start.get("pid") != stop.get("pid"),
              "within 60 s": bool(stop) and bool(start)
              and 0 <= start.get("wall_ns", 0) - stop.get("wall_ns", 0) <= RESTART_MAX_S * 10 ** 9,
              "the same code": bool(prev) and start.get("commit") == prev.get("commit")
              and start.get("file_sha256") == prev.get("file_sha256")}
    return checks, stop, start, after


def counter_reading(root, start, doc):
    """G-COUNTER: the start record's stream_bytes, the counter the service compares with STREAM_CAP, equal to
    the stream bytes of every window closed before its start - T <= W - 900 for its window W - and below
    the cap; and no file of the set left."""
    s = start.get("wall_ns", 0) // 10 ** 9
    W = s // WINDOW * WINDOW
    view = stream_bytes_view(root, upto=W - WINDOW)
    left = [x["asset"] for x in doc["assets"] if os.path.lexists(store_path(root, x))]
    checks = {"started before its window's documents": s - W < DOC_OFFSET,
              "the counter equals the store": start.get("stream_bytes") == view,
              "the counter below the cap": view < STREAM_CAP,
              "no file of the set left": not left}
    return checks, W, view, left


def resume_reading(wj, pid):
    s = wj.get("stream") if isinstance(wj.get("stream"), dict) else {}
    return {"run by the restarted process": wj.get("pid") == pid,
            "the stream opened": s.get("opened") is True,
            "no reason to keep it off": s.get("off_reason") is None,
            "a stream file": bool(s.get("files"))}


def resume_decision(W, pid, now, read):
    """G-RESUME over the restarted process's window W, or W + 900 where W's documents were not served:
    ('NOT YET', T, None) before T's window.json is due plus RESUME_AFTER_S; otherwise (reading, T, checks),
    the reading PASS, FAIL, or UNDECIDABLE where neither window's documents were served. `read(T)` is the
    window's window.json, or None where it has none."""
    for k, T in enumerate((W, W + WINDOW)):
        if now < T + CLOSE_OFFSET + RESUME_AFTER_S:
            return "NOT YET", T, None
        wj = read(T)
        if wj is None:
            return "FAIL", T, {"window.json written": False}
        if wj.get("documents_ok") is not True:
            if k == 0:
                continue
            return "UNDECIDABLE", T, {"documents served": False}
        checks = resume_reading(wj, pid)
        return ("PASS" if all(checks.values()) else "FAIL"), T, checks
    raise AssertionError("unreachable")


def projection(bytes_total, first_T, last_T, counter, free, now):
    """The streams' rate over the set's span, and the instants at which the cap and the floor stop them
    again; printed, never gated."""
    span = last_T - first_T + WINDOW
    rate = Fraction(bytes_total * 86400, span)
    cap_days = Fraction(STREAM_CAP - counter) / rate if counter < STREAM_CAP else Fraction(0)
    rows = [("the cap", cap_days)]
    for base in BASE_DRAINS:
        d = Fraction(free - STREAM_FLOOR) / (rate + base) if free > STREAM_FLOOR else Fraction(0)
        rows.append(("the floor, base %d bytes a day" % base, d))
    return rate, [(what, d, now + int(d * 86400)) for what, d in rows]

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


def unit_reads(n_restarts):
    """G-UNIT: the pair book's unit as TZ-26 installed it, at n_restarts, or unread where None."""
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
              "argv": same_service(cmd, SERVICE_ARGV), "cwd": cwd == SVC,
              "cgroup": ("/system.slice/" + UNIT) in cg and "/user.slice" not in cg,
              "sole instance": processes_with(SERVICE_ARGV) == [pid]}
    if n_restarts is not None:
        checks["restarts"] = kv["NRestarts"] == str(n_restarts)
    return kv, checks, pid


def mode_unit(n_restarts):
    kv, checks, pid = unit_reads(n_restarts)
    for k, v in checks.items():
        out("G-UNIT %-16s %s" % (k, v))
    out("%s MainPID %d, NRestarts %s, MemoryMax %s, MemoryCurrent %s, MemoryPeak %s" % (
        UNIT, pid, kv["NRestarts"], kv["MemoryMax"], kv["MemoryCurrent"], kv["MemoryPeak"]))
    assert all(checks.values()), "G-UNIT FAIL: %r" % {k: v for k, v in checks.items() if not v}
    out("G-UNIT PASS%s" % ("" if n_restarts is None else " at %d restarts" % n_restarts))
    return pid


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
    assert name in ("kill-svc", "start-svc"), "mark %r" % name
    st = load_state()
    marks = st.setdefault("marks", {})
    assert name not in marks, "mark %s already taken" % name
    kv = systemctl_show(UNIT, ["MainPID", "NRestarts", "ActiveState"])
    marks[name] = {"ns": time.time_ns(), "unit": UNIT, "MainPID": kv.get("MainPID"), "NRestarts": kv.get("NRestarts"),
                   "ActiveState": kv.get("ActiveState")}
    save_state(st)
    out("mark %s at %s, %d s into its window: %s %r" % (name, utc(marks[name]["ns"] / 1e9),
                                                        phase_of(marks[name]["ns"] // 10 ** 9), UNIT, marks[name]))


def mode_path():
    """P-PATH: the Release API and a download, with no token, on the one asset whose bytes the map fixes."""
    floor_check()
    gh = GitHub()
    rel = gh.release_by_tag(PATH_TAG)
    assert rel is not None, "P-PATH: no release on %s" % PATH_TAG
    by = {a.get("name"): a for a in gh.assets(int(rel["id"]))}
    a = by.get(PATH_ASSET)
    url = gh.download_url(PATH_TAG, PATH_ASSET)
    x = {"asset": PATH_ASSET, "bytes": PATH_BYTES, "sha256": PATH_SHA256}
    row = asset_row(x, a, url)
    out("P-PATH release %s id %s; asset %s state %s, %s bytes, digest %s, url %s" % (
        PATH_TAG, rel.get("id"), PATH_ASSET, row["state"], row["api_bytes"], row["digest"], row["url_ok"]))
    assert row["api_ok"], "P-PATH: the API's record of %s is not the map's: %r" % (PATH_ASSET, row)
    status, n, h = download_checked(gh, url)
    out("P-PATH download: status %r, %d bytes, sha256 %s" % (status, n, h))
    assert status == 200 and n == PATH_BYTES and h == PATH_SHA256, "P-PATH: the download is not the map's bytes"
    out("READING P-PATH: served - %d requests, the digest field present and equal, %d bytes downloaded and equal" % (
        COUNTERS["requests"], n))


def mode_inventory(tag, a):
    assert TAG_RE.fullmatch(tag), "inventory: a tag named %r" % tag
    now = int(time.time())
    assert a <= now, "inventory: A %d is after now %d" % (a, now)
    floor_check()
    free = free_bytes()
    total = stream_bytes_view(ROOT)
    out("free %d bytes on %s; the store's stream files %d bytes, the cap %d" % (free, DISK_PATH, total, STREAM_CAP))
    assets, windows, deferred, open_n = inventory(ROOT, a)
    doc = set_document(tag, a, ROOT, assets, windows, deferred)
    for w in windows:
        out("W %d %s %-8s stream files %d, %d bytes, taken %d" % (
            w["T"], utc(w["T"]), w["disposition"], w["streams"], w["stream_bytes"], w["taken"]))
    for x in assets:
        out("S %s %d %s" % (x["asset"], x["bytes"], x["sha256"]))
    raw = json_bytes(doc)
    os.makedirs(wpath("archive"), exist_ok=True)
    path = wpath("archive", "set.json")
    st = load_state()
    if os.path.exists(path):
        with open(path, "rb") as fh:
            first = fh.read()
        assert first == raw, "inventory: the set as of %d differs from the first run's" % a
        assert st.get("set", {}).get("sha256") == sha256_bytes(raw), "inventory: state.json names another set"
        out("unchanged %s sha256 %s" % (path, sha256_bytes(raw)))
    else:
        with open(path, "xb") as fh:
            fh.write(raw)
        st["set"] = {"sha256": sha256_bytes(raw), "tag": tag, "as_of": a, "assets_n": doc["assets_n"],
                     "bytes_total": doc["bytes_total"], "first_T": doc["first_T"], "last_T": doc["last_T"]}
        save_state(st)
        out("wrote %s sha256 %s, %d bytes" % (path, sha256_bytes(raw), len(raw)))
    disp = {k: sum(1 for w in windows if w["disposition"] == k) for k in ("closed", "unclosed")}
    out("READING G-SET: %d files of %d windows, %d bytes, windows %d to %d, as of %d (%s); windows considered %d - "
        "closed %d, unclosed %d - and %d still open; deferred %d; the largest file %d bytes, the limit %d; assets %d, "
        "the limit %d" % (doc["assets_n"], sum(1 for w in windows if w["taken"]), doc["bytes_total"], doc["first_T"],
                          doc["last_T"], a, utc(a), len(windows), disp["closed"], disp["unclosed"], open_n, deferred,
                          max(x["bytes"] for x in assets), ASSET_MAX_BYTES, doc["assets_n"], RUN_MAX_ASSETS))


def ls_remote_tag(tag):
    """The tag object and the commit it peels to, from origin."""
    cp = subprocess.run(["git", "-C", PRIMARY, "ls-remote", "origin", "refs/tags/" + tag, "refs/tags/%s^{}" % tag],
                        capture_output=True, text=True)
    assert cp.returncode == 0, "git ls-remote: exit %d" % cp.returncode
    lines = [ln.split("\t") for ln in cp.stdout.strip().split("\n") if ln.strip()]
    got = {ref: sha for sha, ref in lines}
    return got.get("refs/tags/" + tag), got.get("refs/tags/%s^{}" % tag)


def mode_tagged():
    st = load_state()
    doc, _raw = read_set(st)
    tag = doc["tag"]
    head = subprocess.run(["git", "-C", wpath("wt"), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    up = subprocess.run(["git", "-C", wpath("wt"), "rev-parse", "@{u}"], capture_output=True, text=True).stdout.strip()
    obj, peeled = ls_remote_tag(tag)
    out("tag %s: object %s, commit %s; the branch head %s, its upstream %s" % (tag, obj, peeled, head, up))
    assert re.fullmatch(r"[0-9a-f]{40}", head or "") and head == up, "tagged: the branch head is not pushed"
    assert obj is not None and peeled == head and obj != head, "tagged: %s is not an annotated tag of the branch head" % tag
    st["tag"] = {"name": tag, "object": obj, "commit": peeled}
    save_state(st)
    out("TAGGED: %s -> %s" % (tag, peeled))


def release_text(doc):
    name = "%s: the pair book's streams, windows %d to %d" % (doc["tag"], doc["first_T"], doc["last_T"])
    body = ("Verbatim stream files of btc-pairbook.service (research/tz26-nesting-b3-capture.py), one asset per "
            "file, named <T>-<file>: the market websocket's frames for the four books of btc-updown-15m-{T} and "
            "btc-updown-5m-{T+600}, T+595 to T+905. %d files, %d bytes, windows %d to %d. Reserved for B3's "
            "measurement: no TZ reads them before M0's second look has reported (CANON PART II). Each asset's "
            "bytes and SHA-256 are listed in the report of the TZ that pushed this tag." % (
                doc["assets_n"], doc["bytes_total"], doc["first_T"], doc["last_T"]))
    return name, body


def mode_upload():
    """B-UPLOAD: the Boss's. Its credential is credential()'s, and nothing prints it."""
    st = load_state()
    doc, _raw = read_set(st)
    tg = st.get("tag")
    assert tg and tg["name"] == doc["tag"], "upload: the set's tag is not recorded by tagged"
    obj, peeled = ls_remote_tag(doc["tag"])
    assert obj == tg["object"] and peeled == tg["commit"], "upload: the tag on origin is not the recorded one"
    floor_check()
    tok, source = credential()
    out("credential: %s" % source)
    gh = GitHub(token=tok)
    rel = gh.release_by_tag(doc["tag"])
    if rel is None:
        name, body = release_text(doc)
        rel = gh.create_release(doc["tag"], name, body)
        out("created the Release on %s, id %s" % (doc["tag"], rel.get("id")))
    else:
        out("the Release on %s exists, id %s: resumed" % (doc["tag"], rel.get("id")))
    assert rel.get("tag_name") == doc["tag"] and rel.get("draft") is False, "upload: the Release is not published on the tag"
    log_path = wpath("archive", "upload.jsonl")

    def log(rec):
        rec = dict(rec, at=utc(time.time()))
        forbid(rec, "upload.jsonl")
        with open(log_path, "ab") as fh:
            fh.write((json.dumps(rec, sort_keys=True) + "\n").encode("utf-8"))
        out("U %s" % json.dumps(rec, sort_keys=True))

    sent, held = upload_set(gh, rel, doc, ROOT, log)
    log({"action": "complete", "assets": sent + held, "sent": sent, "held": held, "release_id": int(rel["id"]),
         "credential": source, "wall_ns": time.time_ns()})
    out("UPLOAD COMPLETE: %d of %d assets in the Release on %s, %d sent by this run, %d kept from an earlier one; %d bytes" % (
        sent + held, doc["assets_n"], doc["tag"], sent, held, doc["bytes_total"]))


def upload_records():
    path = wpath("archive", "upload.jsonl")
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return [json.loads(ln) for ln in fh if ln.strip()]


def upload_ready(records, assets_n, now_ns):
    """None where verify may read the Release: upload's last record is its completion, for every asset of the
    set, UPLOAD_SETTLE_S or more before now; otherwise why not yet."""
    done = [r for r in records if r.get("action") == "complete"]
    if not records or records[-1].get("action") != "complete":
        return "upload has not completed"
    if done[-1].get("assets") != assets_n:
        return "upload completed %r assets of %d" % (done[-1].get("assets"), assets_n)
    if now_ns < done[-1]["wall_ns"] + UPLOAD_SETTLE_S * 10 ** 9:
        return "upload completed at %s; verify reads the Release from %s" % (
            utc(done[-1]["wall_ns"] / 1e9), utc(done[-1]["wall_ns"] / 1e9 + UPLOAD_SETTLE_S))
    return None


def mode_verify():
    st = load_state()
    doc, raw = read_set(st)
    tg = st.get("tag")
    assert tg and tg["name"] == doc["tag"], "verify: no tag recorded"
    assert ls_remote_tag(doc["tag"]) == (tg["object"], tg["commit"]), "verify: the tag on origin moved"
    why = upload_ready(upload_records(), doc["assets_n"], time.time_ns())
    if why is not None:
        out("NOT YET: %s" % why)
        return 3
    st["verify"] = {"pass": False, "at": utc(time.time())}
    save_state(st)
    floor_check()
    gh = GitHub()
    rel, rows, missing, extra = verify_release(gh, doc["tag"], doc)
    for r in rows:
        out("V %s id %s state %s api %s bytes %s digest %s url %s" % (
            r["asset"], r["id"], r["state"], r["api_ok"], r["api_bytes"], r["digest"], r["url_ok"]))
    checks = release_reading(rel, doc["tag"], rows, missing, extra)
    for k, v in checks.items():
        out("G-UPLOAD/G-DOWNLOAD %-52s %s" % (k, v))
    if missing or extra:
        out("missing %r; beyond the set %r" % (missing[:10], extra[:10]))
    assert all(checks.values()), "VERIFY FAIL: %r" % {k: v for k, v in checks.items() if not v}
    vdoc = {"tag": doc["tag"], "release_id": int(rel["id"]), "set_sha256": sha256_bytes(raw), "assets": rows,
            "assets_n": len(rows), "bytes_total": sum(r["download_bytes"] for r in rows)}
    assert_keys(vdoc, VERIFY_KEYS, "verify.json")
    for r in rows:
        assert_keys(r, VERIFY_ROW_KEYS, "verify.json row")
    vraw = json_bytes(vdoc)
    path = wpath("archive", "verify.json")
    with open(path, "wb") as fh:
        fh.write(vraw)
    st["verify"] = {"pass": True, "set_sha256": sha256_bytes(raw), "verify_sha256": sha256_bytes(vraw),
                    "release_id": int(rel["id"]), "assets_n": len(rows), "at": utc(time.time())}
    save_state(st)
    out("wrote %s sha256 %s" % (path, sha256_bytes(vraw)))
    out("VERIFY PASS: %d of %d assets by name, bytes, state and digest; %d of %d downloads equal, %d bytes" % (
        sum(r["api_ok"] for r in rows), doc["assets_n"], sum(r["download_ok"] for r in rows), doc["assets_n"],
        vdoc["bytes_total"]))
    return 0


def mode_delete():
    st = load_state()
    doc, raw = read_set(st)
    v = st.get("verify")
    assert v and v["pass"] is True and v["set_sha256"] == sha256_bytes(raw), "delete: the set is not verified"
    with open(wpath("archive", "verify.json"), "rb") as fh:
        assert sha256_bytes(fh.read()) == v["verify_sha256"], "delete: verify.json is not the verified one"
    floor_check()
    log_path = wpath("archive", "delete.jsonl")
    done = delete_log()
    free_before = free_bytes()

    def log(r):
        forbid(r, "delete.jsonl")
        with open(log_path, "ab") as fh:
            fh.write((json.dumps(r, sort_keys=True) + "\n").encode("utf-8"))
        out("X %s %d %s removed" % (r["asset"], r["bytes"], r["sha256"]))

    rows, removed, freed, already = delete_set(ROOT, doc, done, int(time.time()), log)
    free_after = free_bytes()
    st["delete"] = {"removed": removed + already, "bytes": sum(x["bytes"] for x in doc["assets"]),
                    "at": utc(time.time())}
    save_state(st)
    out("free %d bytes before, %d after: %+d; the store's stream files now %d bytes" % (
        free_before, free_after, free_after - free_before, stream_bytes_view(ROOT)))
    out("DELETE PASS: %d of %d files removed, %d by this run (%d bytes) and %d by an earlier one; every window kept "
        "its other entries" % (removed + already, doc["assets_n"], removed, freed, already))


def delete_log():
    path = wpath("archive", "delete.jsonl")
    if not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8") as fh:
        return {json.loads(ln)["asset"] for ln in fh if ln.strip()}


def removed_reading(root, doc, done):
    """G-DELETE read back, removing nothing: every file of the set absent, its removal recorded by delete,
    and each of its windows still holding its window.json."""
    windows = sorted({x["T"] for x in doc["assets"]})
    gone = [x for x in doc["assets"] if not os.path.lexists(store_path(root, x))]
    kept = [T for T in windows if os.path.exists(os.path.join(root, str(T), "window.json"))]
    return {"every file of the set absent": len(gone) == doc["assets_n"],
            "each removal recorded by delete": all(x["asset"] in done for x in doc["assets"]),
            "each window keeps its window.json": kept == windows}, len(gone), len(kept)


def mode_removed():
    st = load_state()
    doc, _raw = read_set(st)
    done = delete_log()
    checks, gone, kept = removed_reading(ROOT, doc, done)
    for k, v in checks.items():
        out("G-DELETE %-36s %s" % (k, v))
    assert all(checks.values()), "REMOVED FAIL: %r" % {k: v for k, v in checks.items() if not v}
    out("REMOVED PASS: %d of %d files gone, %d removals recorded, %d windows kept" % (
        gone, doc["assets_n"], len(done), kept))


def mode_restart():
    st = load_state()
    doc, _raw = read_set(st)
    mark = st.get("marks", {}).get("kill-svc")
    assert mark is not None, "restart: no kill-svc mark"
    recs = read_runtime(ROOT + "/runtime.jsonl")
    checks, stop, start, after = restart_reading(recs, mark)
    for r in after[:4]:
        out("record %s pid %s at %s, %d s into its window" % (r.get("event"), r.get("pid"), utc(r["wall_ns"] / 1e9),
                                                              phase_of(r["wall_ns"] // 10 ** 9)))
    for k, v in checks.items():
        out("G-RESTART %-30s %s" % (k, v))
    assert all(checks.values()), "G-RESTART FAIL: %r" % {k: v for k, v in checks.items() if not v}
    out("G-RESTART PASS: the stop of %s, the start of %s %.3f s later" % (
        stop["pid"], start["pid"], (start["wall_ns"] - stop["wall_ns"]) / 1e9))
    c, W, view, left = counter_reading(ROOT, start, doc)
    out("the start record: stream_bytes %s, free_bytes %s; its window %d (%s); the store's streams of the windows "
        "closed before it %d bytes" % (start.get("stream_bytes"), start.get("free_bytes"), W, utc(W), view))
    for k, v in c.items():
        out("G-COUNTER %-40s %s" % (k, v))
    assert all(c.values()), "G-COUNTER FAIL: %r; left %r" % ({k: v for k, v in c.items() if not v}, left[:5])
    out("G-COUNTER PASS: %d bytes, below the cap %d" % (view, STREAM_CAP))
    mode_unit(int(mark["NRestarts"]) + 1)
    st["restart"] = {"W": W, "pid": start["pid"], "stream_bytes": view, "free_bytes": start.get("free_bytes"),
                     "start_wall_ns": start["wall_ns"]}
    save_state(st)


def read_window_json(T):
    path = os.path.join(ROOT, str(T), "window.json")
    if not os.path.exists(path):
        return None
    with open(path, "rb") as fh:
        wj = json.loads(fh.read())
    s = wj.get("stream") if isinstance(wj.get("stream"), dict) else {}
    out("window %d: pid %s, documents %s; stream opened %s, off_reason %s, files %s, segments %s, frames %s, "
        "stored_bytes %s, cut %s" % (T, wj.get("pid"), wj.get("documents_ok"), s.get("opened"), s.get("off_reason"),
                                     s.get("files"), s.get("segments"), s.get("frames"), s.get("stored_bytes"),
                                     s.get("cut")))
    return wj


def mode_resume():
    st = load_state()
    r = st.get("restart")
    assert r is not None, "resume: restart has not passed"
    reading, T, checks = resume_decision(r["W"], r["pid"], int(time.time()), read_window_json)
    if reading == "NOT YET":
        out("NOT YET: window %d's window.json is due at %s; resume reads it from %s" % (
            T, utc(T + CLOSE_OFFSET), utc(T + CLOSE_OFFSET + RESUME_AFTER_S)))
        return 3
    for k, v in checks.items():
        out("G-RESUME %-30s %s" % (k, v))
    out("READING G-RESUME: %s, window %d" % (reading, T))
    assert reading != "FAIL", "G-RESUME FAIL: %r" % {k: v for k, v in checks.items() if not v}
    return 0


def mode_started():
    st = load_state()
    mark = st.get("marks", {}).get("start-svc")
    assert mark is not None, "started: no start-svc mark"
    pid = mode_unit(None)
    recs = read_runtime(ROOT + "/runtime.jsonl")
    last = recs[-1] if recs else {}
    ok = last.get("event") == "start" and last.get("pid") == pid and last.get("wall_ns", 0) >= mark["ns"]
    out("the last record: %s of pid %s at %s" % (last.get("event"), last.get("pid"), utc(last.get("wall_ns", 0) / 1e9)))
    assert ok, "STARTED FAIL: the record does not end with a start of %d after the mark" % pid
    out("STARTED PASS: pid %d" % pid)


def mode_final():
    st = load_state()
    doc, _raw = read_set(st)
    marks = st.get("marks", {})
    n = int(marks["kill-svc"]["NRestarts"]) + 1 if "kill-svc" in marks and "start-svc" not in marks else None
    mode_unit(n)
    mode_still()
    kv = systemctl_show(UNIT, ["ControlGroup", "MemoryCurrent", "MemoryPeak"])
    out("%s MemoryCurrent %s, MemoryPeak %s" % (UNIT, kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    counter = stream_bytes_view(ROOT)
    free = free_bytes()
    dirs = window_dirs(ROOT)
    out("the store: %d window directories, %d to %d; its stream files %d bytes; free %d bytes" % (
        len(dirs), dirs[0] if dirs else 0, dirs[-1] if dirs else 0, counter, free))
    rate, rows = projection(doc["bytes_total"], doc["first_T"], doc["last_T"], counter, free, int(time.time()))
    out("the set's rate: %s bytes a day over windows %d to %d" % (decimals(rate, 0), doc["first_T"], doc["last_T"]))
    for what, d, when in rows:
        out("at that rate %s stops the streams in %s days, at %s" % (what, decimals(d, 2), utc(when)))
    out("FINAL PASS")


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
    """Kept whatever a report prints: the state, the logs and the archive's four files."""
    return tree == WORK[0] and (rel == "state.json" or rel.startswith("logs/") or rel.startswith("archive/"))


def pristine(tree):
    cp = subprocess.run(["git", "-C", tree, "status", "--porcelain", "--ignored"], capture_output=True, text=True)
    assert cp.returncode == 0 and cp.stdout == "", "reclaim: %s holds %r" % (tree, cp.stdout[:400])
    head = subprocess.run(["git", "-C", tree, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    up = subprocess.run(["git", "-C", tree, "rev-parse", "@{u}"], capture_output=True, text=True)
    assert up.returncode == 0 and up.stdout.strip() == head, \
        "reclaim: %s is at %s, its upstream at %r" % (tree, head, up.stdout.strip())
    out("reclaim: %s skipped: no file but its HEAD's, and HEAD %s is its upstream's" % (tree, head))


def reclaimable(tree):
    if tree == WORK[0]:
        return True
    return (tree.startswith("/tmp/") and os.path.isdir(tree) and not os.path.islink(tree)
            and UUID.fullmatch(os.path.basename(tree)) is not None
            and "btc-5m-twap" in os.path.basename(os.path.dirname(tree)))


def mode_reclaim(trees):
    assert trees and all(reclaimable(t) for t in trees), "reclaim: %r" % (trees,)
    procs = proc_start_times()
    for t in trees:
        if t != WORK[0]:
            b = birth(t)
            assert not [p for p, s, _a in procs if s - 1 <= b <= s + LIVE_S], "reclaim: %s belongs to a running process" % t
    tokens = report_tokens()
    lengths = sorted({len(t) for t in tokens})
    before = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    out("reclaim: %d report tokens; forensic store holds %d files" % (len(tokens), before))
    considered_n = named = kept = copied = held = 0
    wt = wpath("wt")
    for tree in trees:
        if tree == WORK[0] and os.path.isdir(wt):
            pristine(wt)
        for dirpath, dirnames, filenames in os.walk(tree):
            dirnames[:] = sorted(d for d in dirnames if os.path.join(dirpath, d) != wt)
            for name in sorted(filenames):
                path = os.path.join(dirpath, name)
                if os.path.islink(path) or not os.path.isfile(path):
                    continue
                considered_n += 1
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
                    got = sha256_file(dest)[0]
                    assert got == h, "reclaim: %s exists with sha256 %s, source %s" % (dest, got, h)
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest)[0] == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, %d already held; "
        "forensic store %d -> %d files" % (considered_n, named, kept, copied, held, before, after))

# ---- the self-test: literals, a temporary store and a loopback server only -----------------------


class _FakeGitHub(http.server.BaseHTTPRequestHandler):
    """The four Release endpoints, the upload host and the download redirect, on 127.0.0.1."""
    lock = threading.Lock()
    releases = {}        # tag -> release
    assets = {}          # id -> {"name", "rid", "data", "state", "digest"}
    next_id = [100]
    token = None
    web = None
    hits = []
    omit_digest = [False]
    refuse_once = []     # names whose next upload is answered 429 once

    def log_message(self, *a):
        pass

    def _send(self, status, obj=None, headers=None, raw=None):
        body = raw if raw is not None else (b"" if obj is None else json.dumps(obj).encode("utf-8"))
        self.send_response(status)
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _authed(self):
        return self.headers.get("Authorization") == "Bearer %s" % _FakeGitHub.token

    def _asset_json(self, aid):
        a = _FakeGitHub.assets[aid]
        tag = [t for t, r in _FakeGitHub.releases.items() if r["id"] == a["rid"]][0]
        return {"id": aid, "name": a["name"], "size": len(a["data"]), "state": a["state"],
                "digest": None if _FakeGitHub.omit_digest[0] else a["digest"],
                "browser_download_url": "%s/%s/releases/download/%s/%s" % (_FakeGitHub.web, REPO, tag, a["name"])}

    def do_GET(self):
        u = urllib.parse.urlsplit(self.path)
        _FakeGitHub.hits.append(("GET", u.path, self.headers.get("User-Agent"), self.headers.get("Authorization")))
        with _FakeGitHub.lock:
            m = re.fullmatch(r"/repos/%s/releases/tags/(.+)" % re.escape(REPO), u.path)
            if m:
                r = _FakeGitHub.releases.get(urllib.parse.unquote(m.group(1)))
                return self._send(200, r) if r else self._send(404, {"message": "Not Found"})
            m = re.fullmatch(r"/repos/%s/releases/([0-9]+)/assets" % re.escape(REPO), u.path)
            if m:
                q = urllib.parse.parse_qs(u.query)
                per, page = int(q["per_page"][0]), int(q["page"][0])
                ids = sorted(a for a, v in _FakeGitHub.assets.items() if v["rid"] == int(m.group(1)))
                return self._send(200, [self._asset_json(a) for a in ids[(page - 1) * per:page * per]])
            m = re.fullmatch(r"/%s/releases/download/([^/]+)/([^/]+)" % re.escape(REPO), u.path)
            if m:
                tag, name = urllib.parse.unquote(m.group(1)), urllib.parse.unquote(m.group(2))
                rid = _FakeGitHub.releases[tag]["id"]
                aid = [a for a, v in _FakeGitHub.assets.items() if v["rid"] == rid and v["name"] == name][0]
                return self._send(302, headers={"Location": "/blob/%d" % aid})
            m = re.fullmatch(r"/blob/([0-9]+)", u.path)
            if m:
                return self._send(200, raw=_FakeGitHub.assets[int(m.group(1))]["data"])
            if u.path == "/redirect":
                return self._send(302, headers={"Location": "/blob/0"})
        return self._send(404, {"message": "Not Found"})

    def do_POST(self):
        u = urllib.parse.urlsplit(self.path)
        n = int(self.headers.get("Content-Length") or 0)
        data = self.rfile.read(n)
        _FakeGitHub.hits.append(("POST", u.path, self.headers.get("User-Agent"), self.headers.get("Authorization")))
        if not self._authed():
            return self._send(401, {"message": "Bad credentials"})
        with _FakeGitHub.lock:
            if u.path == "/repos/%s/releases" % REPO:
                body = json.loads(data)
                if body["tag_name"] in _FakeGitHub.releases:
                    return self._send(422, {"message": "already_exists"})
                rid = _FakeGitHub.next_id[0]
                _FakeGitHub.next_id[0] += 1
                _FakeGitHub.releases[body["tag_name"]] = {"id": rid, "tag_name": body["tag_name"], "name": body["name"],
                                                          "body": body["body"], "draft": body["draft"],
                                                          "prerelease": body["prerelease"]}
                return self._send(201, _FakeGitHub.releases[body["tag_name"]])
            m = re.fullmatch(r"/repos/%s/releases/([0-9]+)/assets" % re.escape(REPO), u.path)
            if m:
                name = urllib.parse.parse_qs(u.query)["name"][0]
                assert self.headers.get("Content-Type") == CONTENT_TYPE and len(data) == n
                if name in _FakeGitHub.refuse_once:
                    _FakeGitHub.refuse_once.remove(name)
                    return self._send(429, {"message": "slow down"}, headers={"Retry-After": "0"})
                rid = int(m.group(1))
                if any(v["rid"] == rid and v["name"] == name for v in _FakeGitHub.assets.values()):
                    return self._send(422, {"message": "already_exists"})
                aid = _FakeGitHub.next_id[0]
                _FakeGitHub.next_id[0] += 1
                _FakeGitHub.assets[aid] = {"name": name, "rid": rid, "data": data, "state": "uploaded",
                                           "digest": "sha256:" + hashlib.sha256(data).hexdigest()}
                return self._send(201, self._asset_json(aid))
        return self._send(404, {"message": "Not Found"})

    def do_DELETE(self):
        u = urllib.parse.urlsplit(self.path)
        _FakeGitHub.hits.append(("DELETE", u.path, self.headers.get("User-Agent"), self.headers.get("Authorization")))
        if not self._authed():
            return self._send(401, {"message": "Bad credentials"})
        with _FakeGitHub.lock:
            m = re.fullmatch(r"/repos/%s/releases/assets/([0-9]+)" % re.escape(REPO), u.path)
            if m and int(m.group(1)) in _FakeGitHub.assets:
                del _FakeGitHub.assets[int(m.group(1))]
                return self._send(204)
        return self._send(404, {"message": "Not Found"})


def mode_selftest():
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    sep = ":" + "//"
    # the band, the window and the service's names, against integers computed outside this file
    T = 1791660600
    ok([in_band(T + 14), in_band(T + 15), in_band(T + 480), in_band(T + 481), in_band(T + 900 + 15)]
       == [False, True, True, False, True] and phase_of(1791664664) == 464,
       "the band: seconds 15 to 480 of the 900 s window, both included; TZ-26's kill at second 464")
    ok([is_stream(x) for x in ("stream.jsonl.gz", "stream.1.jsonl.gz", "stream.12.jsonl.gz", "books.jsonl.gz",
                               "window.json", "documents.jsonl", "streams.txt")] == [True, True, True, False, False, False, False]
       and [stream_index(x) for x in ("stream.jsonl.gz", "stream.1.jsonl.gz", "stream.12.jsonl.gz")] == [0, 1, 12],
       "the service's stream predicate and next_stream_path's names")
    try:
        stream_index("stream-x.jsonl.gz")
        odd = False
    except AssertionError:
        odd = True
    ok(odd, "a stream file outside next_stream_path's names stops the run")
    ok(ASSET_RE.fullmatch("1791660600-stream.jsonl.gz") is not None and ASSET_RE.fullmatch("1791660600-stream.1.jsonl.gz")
       is not None and ASSET_RE.fullmatch("1791660600_stream.jsonl.gz") is None and TAG_RE.fullmatch("tz-27-pairbook-streams")
       is not None and TAG_RE.fullmatch("tz-27-pairbook") is None and WORK_RE.fullmatch("/root/tz27-work") is not None
       and WORK_RE.fullmatch("/root/tz27-work/x") is None, "asset, tag and work-tree names")
    # the audit policy, as a pure function
    w, allowed = "/root/tz27-work", {ROOT + "/1791660600/stream.jsonl.gz"}
    s0 = ROOT + "/1791660600/stream.jsonl.gz"
    ok(policy("inventory", "open", (s0, "rb", 0), w, set()) is None and policy("upload", "open", (s0, "rb", 0), w, set())
       is None and policy("verify", "open", (s0, "rb", 0), w, set()) is not None
       and policy("path", "open", (s0, "rb", 0), w, set()) is not None,
       "the store is read by the modes that need its bytes, and by no other")
    ok(all(policy(m, "open", (s0, fm, 0), w, allowed) is not None for m in ("inventory", "upload", "delete", "selftest")
           for fm in ("wb", "ab", "r+b", "xb")), "nothing is written under the pair book's root, in any mode")
    ok(policy("delete", "os.remove", (s0, None), w, allowed) is None
       and policy("delete", "os.remove", (ROOT + "/1791660600/window.json", None), w, allowed) is not None
       and policy("inventory", "os.remove", (s0, None), w, allowed) is not None
       and policy("delete", "os.rename", (s0, w + "/x"), w, allowed) is not None
       and policy("delete", "shutil.rmtree", (ROOT + "/1791660600", None), w, allowed) is not None,
       "only delete removes, only a file it has verified, and nothing is moved or removed whole")
    ok(all(policy(m, ev, (p, "rb", 0), w, set()) is not None for m in ("inventory", "delete", "final")
           for ev in ("open", "os.scandir") for p in (RECORDER + "/runtime.jsonl", CHAINBOOK + "/runtime.jsonl")),
       "nothing under the recorder's or the chain book's root is opened or listed")
    ok(policy("inventory", "os.scandir", (ROOT,), w, set()) is None and policy("upload", "os.scandir", (ROOT,), w, set())
       is not None and policy("verify", "os.listdir", (ROOT + "/1791660600",), w, set()) is not None,
       "the store is listed by inventory, delete, restart and final alone")
    ok(policy("upload", "open", (w + "/archive/upload.jsonl", "ab", 0), w, set()) is None
       and policy("upload", "open", ("/tmp/x", "wb", 0), w, set()) is not None
       and policy("reclaim", "open", (FORENSICS + "/x", "xb", 0), w, set()) is None
       and policy("reclaim", "open", (FORENSICS + "/x", "wb", 0), w, set()) is not None
       and policy("verify", "os.remove", (FORENSICS + "/x", None), w, set()) is not None,
       "writes go to the work tree, and to the forensic store by reclaim's exclusive create alone")
    ok(policy("inventory", "subprocess.Popen", ("git",), w, set()) is not None and policy("delete", "os.fork", (), w, set())
       is not None and policy("upload", "subprocess.Popen", ("git",), w, set()) is None,
       "inventory and delete start no process")
    for p in (RECORDER + "/runtime.jsonl", CHAINBOOK + "/runtime.jsonl", ROOT + "/runtime.jsonl"):
        try:
            open(p, "rb")
            refused = False
        except GuardError:
            refused = True
        except OSError:
            refused = False
        ok(refused and REFUSED[-1][1] == p, "the hook refuses %s before it is opened" % p)
    try:
        os.remove(ROOT + "/1791660600/stream.jsonl.gz")
        refused = False
    except GuardError:
        refused = True
    except OSError:
        refused = False
    ok(refused and REFUSED[-1][0] == "os.remove", "the hook refuses a removal under the pair book's root outside delete")
    REFUSED.clear()
    # a temporary store under the work tree: four windows - two closed, one unclosed, one open - and two strays
    tmp = wpath("selftest-tmp")
    if os.path.lexists(tmp):
        shutil.rmtree(tmp)
    store = os.path.join(tmp, "store")
    blobs = {}

    def put(T_, name, nbytes):
        d = os.path.join(store, str(T_))
        os.makedirs(d, exist_ok=True)
        data = (hashlib.sha256(("%d/%s" % (T_, name)).encode()).digest() * (nbytes // 32 + 1))[:nbytes]
        with open(os.path.join(d, name), "wb") as fh:
            fh.write(data)
        blobs[(T_, name)] = data

    for T_, files in ((1791660600, [("stream.jsonl.gz", 70001), ("window.json", 300), ("books.jsonl.gz", 900),
                                    ("documents.jsonl", 500)]),
                      (1791661500, [("stream.jsonl.gz", 50000), ("stream.1.jsonl.gz", 33333), ("window.json", 301)]),
                      (1791662400, [("stream.jsonl.gz", 40000), ("documents.jsonl", 10)]),
                      (1791663300, [("stream.jsonl.gz", 1234), ("documents.jsonl", 10)])):
        for name, nb in files:
            put(T_, name, nb)
    os.makedirs(os.path.join(store, "lost+found"), exist_ok=True)
    with open(os.path.join(store, "runtime.jsonl"), "wb") as fh:
        fh.write(b"{}\n")
    a = 1791663300 + 100
    assets, windows, deferred, open_n = inventory(store, a)
    want = [(1791660600, "stream.jsonl.gz"), (1791661500, "stream.jsonl.gz"), (1791661500, "stream.1.jsonl.gz")]
    ok([(x["T"], x["file"]) for x in assets] == want
       and all(x["sha256"] == hashlib.sha256(blobs[(x["T"], x["file"])]).hexdigest() and x["bytes"] == len(blobs[(x["T"], x["file"])])
               for x in assets) and deferred == 0,
       "inventory: the stream files of the closed windows, in order, each the bytes written")
    ok([(w_["T"], w_["disposition"], w_["streams"], w_["stream_bytes"], w_["taken"]) for w_ in windows] ==
       [(1791660600, "closed", 1, 70001, 1), (1791661500, "closed", 2, 83333, 2), (1791662400, "unclosed", 1, 40000, 0)]
       and open_n == 1, "inventory: closed, unclosed without window.json, and the open window counted and not listed")
    ok([(x["T"], x["file"]) for x in inventory(store, 1791661500 + 969)[0]] == [(1791660600, "stream.jsonl.gz")]
       and [(x["T"], x["file"]) for x in inventory(store, 1791661500 + 970)[0]] == want,
       "a window is taken from T+970, 60 s after its window.json was due")
    two, _w2, d2, _o2 = inventory(store, a, max_assets=2)
    ok([(x["T"], x["file"]) for x in two] == want[:2] and d2 == 1, "the first max_assets taken, the rest deferred and counted")
    try:
        inventory(store, a, asset_max=60000)
        big = False
    except AssertionError:
        big = True
    ok(big, "a file above a Release asset's limit stops the run")
    ok(stream_bytes_view(store) == 70001 + 50000 + 33333 + 40000 + 1234
       and stream_bytes_view(store, upto=1791661500) == 70001 + 50000 + 33333,
       "stream_bytes_view: the service's counter, whole and over the windows closed before a start")
    doc = set_document("tz-27-pairbook-streams", a, store, assets, windows, deferred)
    put(1791664200, "stream.jsonl.gz", 99)
    put(1791663300, "stream.jsonl.gz", 2345)
    again = set_document("tz-27-pairbook-streams", a, store, *inventory(store, a)[:3])
    ok(doc["assets_n"] == 3 and doc["bytes_total"] == 153334 and doc["first_T"] == 1791660600
       and doc["last_T"] == 1791661500 and json_bytes(doc) == json_bytes(again),
       "the set document, and a second run byte-identical while the open windows grow")
    try:
        set_document("tz-27-pairbook-streams", a, store, [], windows, 0)
        empty = False
    except AssertionError:
        empty = True
    ok(empty, "an empty set stops the run: nothing to archive")
    os.makedirs(os.path.join(store, "123"))
    try:
        window_dirs(store)
        stray = False
    except AssertionError:
        stray = True
    os.rmdir(os.path.join(store, "123"))
    ok(stray, "a numeric directory that is not a window stops the run")
    # the token: read from a remote URL, never named in a message
    tok = "ghp_" + "Ab3" * 12
    ok(token_of("https" + sep + "%s@github.com/%s.git\n" % (tok, REPO)) == tok
       and token_of("https" + sep + "x-access-token:%s@github.com/%s" % (tok, REPO)) == tok
       and token_of("https" + sep + "github.com/%s.git" % REPO) is None
       and token_of("https" + sep + "short@github.com/%s.git" % REPO) is None,
       "token_of: both forms of the remote, and None where it carries no credential")
    msgs = []
    for bad in ("https" + sep + "%s@example.com/%s.git" % (tok, REPO), "https" + sep + "%s@github.com/other/repo.git" % tok,
                "http" + sep + "%s@github.com/%s.git" % (tok, REPO)):
        try:
            token_of(bad)
            msgs.append(None)
        except AssertionError as exc:
            msgs.append(str(exc))
    ok(all(m is not None and tok not in m for m in msgs), "a remote on another host, repository or scheme stops the "
       "run, and no message names the token")
    ok(set(build_request("GET", "https" + sep + "x/y").header_items()) == {
        ("Accept", ACCEPT_API), ("User-agent", UA), ("X-github-api-version", API_VERSION)}
       and dict(build_request("POST", "https" + sep + "x/y", token=tok, data=b"ab", ctype=CONTENT_TYPE,
                              length=2).header_items())
       == {"Accept": ACCEPT_API, "User-agent": UA, "X-github-api-version": API_VERSION, "Authorization": "Bearer " + tok,
           "Content-type": CONTENT_TYPE, "Content-length": "2"}, "every header of every request, fixed")
    recs_up = [{"action": "uploaded"}, {"action": "complete", "assets": 3, "wall_ns": 1791670000 * 10 ** 9}]
    ok(upload_ready([], 3, 1791670500 * 10 ** 9) == "upload has not completed"
       and upload_ready(recs_up[:1], 3, 1791670500 * 10 ** 9) == "upload has not completed"
       and upload_ready(recs_up + [{"action": "uploaded"}], 3, 1791670500 * 10 ** 9) == "upload has not completed"
       and upload_ready(recs_up, 4, 1791670500 * 10 ** 9).startswith("upload completed 3 assets")
       and upload_ready(recs_up, 3, (1791670000 + 119) * 10 ** 9).startswith("upload completed at")
       and upload_ready(recs_up, 3, (1791670000 + 120) * 10 ** 9) is None,
       "verify reads the Release only after upload's completion record for the whole set, and 120 s after it")
    ok([wait_for(429, {"Retry-After": "5"}, 1), wait_for(429, {}, 2), wait_for(403, {"retry-after": "200"}, 3),
        wait_for(403, {"x-ratelimit-remaining": "0", "x-ratelimit-reset": str(int(time.time()) + 4000)}, 1),
        wait_for(None, {}, 2), wait_for(502, {}, 3), wait_for(422, {}, 1), wait_for(401, {}, 1), wait_for(404, {}, 1)]
       == [60, 120, 240, 900, 20, 30, 2, None, None],
       "a refused upload waits as the reply asks, at least a minute doubling, bounded; 401 and 404 stop")
    # the loopback server: upload, resume, verify and its failures
    for k in [k for k in list(os.environ) if k.lower() in ("http_proxy", "https_proxy", "all_proxy", "no_proxy")]:
        del os.environ[k]
    _FakeGitHub.token = tok
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _FakeGitHub)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    base = "http" + sep + "127.0.0.1:%d" % srv.server_address[1]
    _FakeGitHub.web = base
    tag = "tz-27-pairbook-streams"
    try:
        gh = GitHub(token=tok, api=base, uploads=base, web=base)
        gh.gap_s = 0.0
        anon = GitHub(api=base, uploads=base, web=base)

        def vr(download=True):
            mark = len(_FakeGitHub.hits)
            rel_, rows, missing, extra = verify_release(anon, tag, doc, download)
            return release_reading(rel_, tag, rows, missing, extra), rows, _FakeGitHub.hits[mark:]

        st_, _b, _h = call(gh.op, build_request("GET", base + "/redirect", token=tok), 5)
        ok(st_ == 302 and not [h for h in _FakeGitHub.hits if h[1] == "/blob/0"],
           "a request carrying the token follows no redirect")
        ok(gh.release_by_tag(tag) is None, "no Release before the first upload")
        name, body = release_text(doc)
        rel = gh.create_release(tag, name, body)
        logs = []
        sent, held = upload_set(gh, rel, doc, store, logs.append)
        ok((sent, held) == (3, 0) and [r["action"] for r in logs] == ["uploaded"] * 3
           and all(h[2] == UA for h in _FakeGitHub.hits), "upload: three sent, every request under this file's User-Agent")
        logs.clear()
        ok(upload_set(gh, rel, doc, store, logs.append) == (0, 3), "upload again: the three kept, nothing sent")
        aid1 = [i for i, v in _FakeGitHub.assets.items() if v["name"] == doc["assets"][1]["asset"]][0]
        _FakeGitHub.assets[aid1]["state"] = "starter"
        aid2 = [i for i, v in _FakeGitHub.assets.items() if v["name"] == doc["assets"][2]["asset"]][0]
        del _FakeGitHub.assets[aid2]
        _FakeGitHub.refuse_once.append(doc["assets"][2]["asset"])
        logs.clear()
        ok(upload_set(gh, rel, doc, store, logs.append, wait_min=0) == (2, 1)
           and [r["action"] for r in logs] == ["held", "removed from the Release", "uploaded", "refused", "uploaded"],
           "upload resumes: a partial asset removed and sent again, a refusal waited out, the rest kept")
        c, rows, hits = vr()
        ok(all(c.values()) and all(r["download_ok"] and r["download_sha256"] == r["sha256"] for r in rows)
           and len([h for h in hits if h[1].startswith("/blob/")]) == 3 and all(h[3] is None for h in hits),
           "verify: every asset by name, bytes, state and digest, three downloads equal, no token sent")
        k0 = [i for i, v in _FakeGitHub.assets.items() if v["name"] == doc["assets"][0]["asset"]][0]
        good = _FakeGitHub.assets[k0]["data"]
        _FakeGitHub.assets[k0]["data"] = good[:-1] + bytes([good[-1] ^ 1])
        c, rows, _hits = vr()
        ok(not c["every download the set's bytes and SHA-256"] and rows[0]["download_ok"] is False
           and rows[1]["download_ok"] is True, "verify: one flipped bit in one asset's bytes reads FAIL")
        _FakeGitHub.assets[k0]["data"] = good
        _FakeGitHub.omit_digest[0] = True
        c, rows, hits = vr()
        ok(not c["every asset uploaded, its bytes and digest the set's"] and all(r["download_bytes"] is None for r in rows)
           and not [h for h in hits if h[1].startswith("/blob/")],
           "verify: an asset without a digest reads FAIL, and nothing is downloaded")
        _FakeGitHub.omit_digest[0] = False
        _FakeGitHub.assets[999] = {"name": "1791662400-stream.jsonl.gz", "rid": rel["id"], "data": b"x",
                                   "state": "uploaded", "digest": "sha256:" + hashlib.sha256(b"x").hexdigest()}
        ok(not vr(False)[0]["no asset beyond the set"], "verify: an asset beyond the set reads FAIL")
        try:
            upload_set(gh, rel, doc, store, logs.append)
            beyond = False
        except AssertionError:
            beyond = True
        ok(beyond, "upload refuses a Release holding an asset beyond the set")
        del _FakeGitHub.assets[999]
        kept = _FakeGitHub.assets.pop(aid1 if aid1 in _FakeGitHub.assets else
                                      [i for i, v in _FakeGitHub.assets.items() if v["name"] == doc["assets"][1]["asset"]][0])
        ok(not vr(False)[0]["no asset missing"], "verify: a missing asset reads FAIL")
        logs.clear()
        ok(upload_set(gh, rel, doc, store, logs.append) == (1, 2) and all(vr()[0].values()),
           "upload sends the missing asset again, and verify then reads PASS")
        ok(kept["data"] == blobs[(1791661500, "stream.jsonl.gz")], "the asset removed was the file's bytes")
        other = "ghp_" + "Zz9" * 12
        ok(call(GitHub(token=other, api=base).op, build_request("POST", base + "/repos/%s/releases" % REPO, token=other,
                                                                data=b"{}", ctype="application/json"), 5)[0] == 401,
           "the loopback server refuses a wrong token, as the venue of every upload would")
    finally:
        srv.shutdown()
        srv.server_close()
    # delete: refuses a changed file before it removes anything; removes the set and nothing else
    dlog = []
    path0 = store_path(store, doc["assets"][0])
    with open(path0, "r+b") as fh:
        fh.write(b"Z")
    try:
        delete_set(store, doc, set(), a + 10, dlog.append)
        changed = False
    except AssertionError:
        changed = True
    ok(changed and all(os.path.exists(store_path(store, x)) for x in doc["assets"]),
       "delete: a file changed since the set stops the run, and nothing is removed")
    with open(path0, "r+b") as fh:
        fh.write(blobs[(1791660600, "stream.jsonl.gz")][:1])
    try:
        delete_set(store, doc, set(), 1791661500 + 969, dlog.append)
        early = False
    except AssertionError:
        early = True
    ok(early and all(os.path.exists(store_path(store, x)) for x in doc["assets"][1:])
       and [r["asset"] for r in dlog] == [doc["assets"][0]["asset"]],
       "delete: a window not closed by the instant given stops the run there, each removal before it logged")
    for x in doc["assets"][:1]:
        if not os.path.exists(store_path(store, x)):
            put(x["T"], x["file"], x["bytes"])
    dlog.clear()
    ok(not removed_reading(store, doc, set())[0]["every file of the set absent"], "removed reads FAIL before delete")
    rows, removed, freed, already = delete_set(store, doc, set(), a + 10, dlog.append)
    ok(all(removed_reading(store, doc, {r["asset"] for r in rows})[0].values()) and dlog == rows
       and not removed_reading(store, doc, set())[0]["each removal recorded by delete"],
       "removed reads PASS after delete, and FAIL where a removal is not recorded")
    ok(removed == 3 and freed == 153334 and already == 0 and [r["asset"] for r in rows] == [x["asset"] for x in doc["assets"]]
       and window_names(store, 1791660600) == ["books.jsonl.gz", "documents.jsonl", "window.json"]
       and window_names(store, 1791661500) == ["window.json"]
       and window_names(store, 1791662400) == ["documents.jsonl", "stream.jsonl.gz"]
       and window_names(store, 1791663300) == ["documents.jsonl", "stream.jsonl.gz"],
       "delete: the three files of the set, and every other entry kept")
    ok(stream_bytes_view(store) == 40000 + 2345 + 99 and stream_bytes_view(store, upto=1791661500) == 0,
       "the counter a restart reads afterwards: the windows not in the set")
    ok(delete_set(store, doc, {x["asset"] for x in doc["assets"]}, a + 10, dlog.append)[1:] == (0, 0, 3),
       "delete again: each absent file counted where this mode recorded its removal")
    try:
        delete_set(store, doc, set(), a + 10, dlog.append)
        unrecorded = False
    except AssertionError:
        unrecorded = True
    ok(unrecorded, "delete: an absent file with no recorded removal stops the run")
    # the service's record, read: G-RESTART, G-COUNTER and G-RESUME on literals
    mark = {"ns": (1791664200 + 459) * 10 ** 9, "MainPID": "746785", "NRestarts": "1"}
    recs = [{"event": "start", "pid": 746785, "wall_ns": 1791660606 * 10 ** 9, "commit": "e8b4", "file_sha256": "caed"},
            {"event": "stop", "pid": 746785, "wall_ns": (1791664200 + 464) * 10 ** 9},
            {"event": "start", "pid": 752775, "wall_ns": (1791664200 + 469) * 10 ** 9 + 480000000, "commit": "e8b4",
             "file_sha256": "caed", "stream_bytes": 0}]
    checks, stop, start, _after = restart_reading(recs, mark)
    ok(all(checks.values()) and stop["pid"] == 746785 and start["pid"] == 752775, "G-RESTART on TZ-26's own records")
    late = [dict(recs[0]), dict(recs[1], wall_ns=(1791664200 + 490) * 10 ** 9), dict(recs[2])]
    slow = [dict(recs[0]), dict(recs[1]), dict(recs[2], wall_ns=(1791664200 + 525) * 10 ** 9)]
    other_code = [dict(recs[0]), dict(recs[1]), dict(recs[2], file_sha256="beef")]
    ok(not restart_reading(late, mark)[0]["stopped inside the band"] and not restart_reading(slow, mark)[0]["within 60 s"]
       and not restart_reading(other_code, mark)[0]["the same code"]
       and not restart_reading(recs[:2], mark)[0]["a start of another process"]
       and not restart_reading(recs[:1], mark)[0]["a stop of the marked process"],
       "G-RESTART reads FAIL outside the band, after 60 s, on other code, without a start and without a stop")
    err = [dict(recs[0]), {"event": "error", "pid": 746785, "wall_ns": (1791664200 + 461) * 10 ** 9}, dict(recs[1]),
           dict(recs[2])]
    ok(all(restart_reading(err, mark)[0].values()), "G-RESTART reads the first stop after the mark, past an error record")
    c, W, view, left = counter_reading(store, {"wall_ns": (1791662400 + 470) * 10 ** 9, "stream_bytes": 0}, doc)
    ok(all(c.values()) and W == 1791662400 and view == 0 and left == [],
       "G-COUNTER: a start in window W counts the windows up to W - 900, and the set is gone")
    c2 = counter_reading(store, {"wall_ns": (1791663300 + 470) * 10 ** 9, "stream_bytes": 0}, doc)[0]
    c3 = counter_reading(store, {"wall_ns": (1791663300 + 600) * 10 ** 9, "stream_bytes": 40000}, doc)[0]
    ok(not c2["the counter equals the store"] and c3["the counter equals the store"]
       and not c3["started before its window's documents"], "G-COUNTER reads FAIL on a counter that is not the store's, "
       "and on a start after its window's documents")
    good_wj = {"pid": 7, "documents_ok": True, "stream": {"opened": True, "off_reason": None, "files": ["stream.jsonl.gz"]}}
    no_docs = {"pid": 7, "documents_ok": False, "stream": {"opened": False, "off_reason": "documents", "files": []}}
    capped = {"pid": 7, "documents_ok": True, "stream": {"opened": False, "off_reason": "cap", "files": []}}
    W0 = 1791664200
    ok([resume_decision(W0, 7, W0 + 939, {W0: good_wj}.get)[0], resume_decision(W0, 7, W0 + 940, {W0: good_wj}.get)[:2],
        resume_decision(W0, 7, W0 + 940, {W0: capped}.get)[0], resume_decision(W0, 7, W0 + 940, {}.get)[0],
        resume_decision(W0, 7, W0 + 940, {W0: no_docs}.get)[:2],
        resume_decision(W0, 7, W0 + 1840, {W0: no_docs, W0 + 900: good_wj}.get)[:2],
        resume_decision(W0, 7, W0 + 1840, {W0: no_docs, W0 + 900: no_docs}.get)[0]]
       == ["NOT YET", ("PASS", W0), "FAIL", "FAIL", ("NOT YET", W0 + 900), ("PASS", W0 + 900), "UNDECIDABLE"],
       "G-RESUME: the restart's window from T+940; the next window where its documents were not served")
    ok(all(resume_reading({"pid": 7, "stream": {"opened": True, "off_reason": None, "files": ["stream.jsonl.gz"]}}, 7).values())
       and not all(resume_reading({"pid": 7, "stream": {"opened": False, "off_reason": "cap", "files": []}}, 7).values())
       and not all(resume_reading({"pid": 8, "stream": {"opened": True, "off_reason": None, "files": ["s"]}}, 7).values()),
       "G-RESUME: the restart's window streamed by the restarted process; the cap or another process reads FAIL")
    rate, rows_ = projection(1224503448 * 2, 1791660600, 1791660600 + 191 * 900, 0, 12931072000, 1791664700)
    ok(rate == 1224503448 and rows_[0][1] == Fraction(8000000000, 1224503448)
       and rows_[1][1] == Fraction(12931072000 - 4500000000, 1224503448 + 43500000)
       and rows_[2][1] == Fraction(12931072000 - 4500000000, 1224503448 + 187760570),
       "the projection: two days of streams at TZ-26's measured rate, the cap and the floor at both bases")
    ok(decimals(Fraction(1, 3), 2) == "0.33" and decimals(Fraction(2, 3), 2) == "0.67" and decimals(Fraction(5, 2), 0) == "3",
       "decimals: half up")
    shutil.rmtree(tmp)
    ok(not os.path.lexists(tmp), "the temporary store removed")
    # this file's own syntax: its imports and its endpoints
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            mods |= {a_.name.split(".")[0] for a_ in node.names}
        elif isinstance(node, ast.ImportFrom):
            mods.add((node.module or "").split(".")[0])
    ok(mods <= set(sys.stdlib_module_names), "imports: the standard library alone")
    urls = sorted({c_.value for c_ in ast.walk(tree) if isinstance(c_, ast.Constant) and isinstance(c_.value, str)
                   and sep in c_.value})
    ok(urls == sorted([API_BASE, UPLOAD_BASE, WEB_BASE]), "exactly three endpoints in the file's text")
    out("%d of %d checks passed" % (n[0], n[0]))


def main(argv):
    if not argv:
        sys.exit("usage: tz27-pairbook-archive.py MODE [ARG...]")
    mode, rest = argv[0], argv[1:]
    cwd = os.getcwd()
    assert WORK_RE.fullmatch(cwd), "run from a work tree /root/tzNN-work, not %s" % cwd
    WORK[0] = cwd
    MODE[0] = mode
    rc = 0
    if mode == "inventory":
        assert len(rest) == 2 and rest[1].isdigit(), "inventory TAG A"
        mode_inventory(rest[0], int(rest[1]))
    elif mode == "mark":
        assert len(rest) == 1, "mark NAME"
        mode_mark(rest[0])
    elif mode == "scratch":
        assert len(rest) == 1, "scratch OWN"
        mode_scratch(rest[0])
    elif mode == "reclaim":
        mode_reclaim(rest)
    elif mode == "resume":
        assert not rest, "resume takes no argument"
        rc = mode_resume()
    elif mode == "verify":
        assert not rest, "verify takes no argument"
        rc = mode_verify()
    else:
        table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "still": mode_still, "path": mode_path,
                 "tagged": mode_tagged, "upload": mode_upload, "delete": mode_delete,
                 "removed": mode_removed,
                 "restart": mode_restart, "started": mode_started, "final": mode_final}
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
    out("opens refused: %d; store opens %d; requests %d, uploads %d, downloads %d (%d bytes); files removed %d" % (
        len(REFUSED), STORE_OPENS[0], COUNTERS["requests"], COUNTERS["uploads"], COUNTERS["downloads"],
        COUNTERS["download_bytes"], COUNTERS["removed"]))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
