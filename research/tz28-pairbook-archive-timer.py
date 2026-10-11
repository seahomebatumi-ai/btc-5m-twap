#!/usr/bin/env python3
"""TZ-28 - the pair book's archive on a timer: TZ-27's set, proofs, removal and restart, run unattended once a day
by btc-pairbook-archive.timer, every request inside the pair book's idle stretch.

    run               the unit's one mode, ExecStart of btc-pairbook-archive.service: a new set as of now, or the
                      pending one resumed; upload, verify, delete, restart and resume through TZ-27's own functions,
                      each under TZ-27's own section 2; one record a step in /var/lib/btc-pairbook-archive/
                      ledger.jsonl. Exit 0 complete or empty; 75 deferred - nothing removed, the next run resumes it;
                      1 halted - the run disables its own timer; 2 not started
    fingerprint       map section 0 against the primary checkout
    selftest          every rule of this file, on literals, temporary stores, a simulated pair book and a loopback
                      server only
    tz27-release      G-TZ27: the Release on tz-27-pairbook-streams against TZ-27's set.json in the forensic store,
                      by the API with no token
    path              P-PATH: the run's own request path, with no token and held to the idle stretch, on
                      tz-01a-dataset's asset: the API and a download
    path-token        B-PATH-TOKEN, the Boss's block and nobody else's: the run's credential reads the repository,
                      with push, and the TZ-27 Release; nothing prints it
    installed         G-INSTALL: the service's three files, the two units and the empty state directory
    mark NAME         enable or retry: an instant and the archive's two units into state.json; start-svc: TZ-27's
    timer             G-TIMER: the timer as installed and enabled, and its next calendar elapse
    first             the first run after the enable mark, re-read: G-TRIGGER, G-RUN and the run's own readings;
                      exit 3 NOT YET
    final             G-UNIT, G-STILL and G-TIMER; the store and the next stop, projected
    still, started, scratch OWN, reclaim TREE...   TZ-27's own modes, unchanged

TZ-27's instrument, research/tz27-pairbook-archive.py, is loaded from beside this file and asserted by its SHA-256;
it installs its own audit hook, and every mode here sets that hook's mode and work tree before it acts. Every
request goes through TZ-27's GitHub class and build_request. No mode decompresses a stream file or prints a price,
a size, a side, a book's hash or an outcome. Run it with /root/tz04a-env, the pair book's interpreter; it needs the
standard library alone.

Written for CryptoTZ/TZ-28-pairbook-archive-timer.md. The TZ is the specification.
"""

import ast
import datetime
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
import urllib.parse

if not __debug__:
    sys.stderr.write("tz28: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(1)

HERE = os.path.dirname(os.path.abspath(__file__))
SELF_NAME = "tz28-pairbook-archive-timer.py"
TZ27_NAME = "tz27-pairbook-archive.py"
TZ27_SHA256 = "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673"


def load_tz27(path):
    """TZ-27's instrument, executed from the very bytes whose SHA-256 is asserted. It installs its audit hook."""
    with open(path, "rb") as fh:
        raw = fh.read()
    got = hashlib.sha256(raw).hexdigest()
    assert got == TZ27_SHA256, "%s sha256 %s, required %s" % (path, got, TZ27_SHA256)
    mod = types.ModuleType("tz27")
    mod.__file__ = path
    sys.modules["tz27"] = mod
    exec(compile(raw, path, "exec"), mod.__dict__)
    return mod


tz27 = load_tz27(os.path.join(HERE, TZ27_NAME))
out = tz27.out

# ---- the TZ's constants: none of them is measured by this run -----------------------------------

MAP_REVISION = "2026-10-11-b"
MAP_ROWS = {"frozen": 34, "tracked": 2, "reported": 1}

STATE = "/var/lib/btc-pairbook-archive"
ASVC = "/root/btc-pairbook-archive-svc"
ARCHIVE = "btc-pairbook-archive.service"
TIMER = "btc-pairbook-archive.timer"
UNIT_DIR = "/etc/systemd/system"
RUN_ARGV = (tz27.PYTHON, "-B", "-u", ASVC + "/" + SELF_NAME, "run")
CALENDAR = "*-*-* 03:00:20 UTC"
CALENDAR_S = 3 * 3600 + 20       # the calendar elapse, seconds after 00:00 UTC
ACTIVE_S = 600                   # OnActiveSec: the first run, 600 s after the timer starts
TIMEOUT_S = 21600                # TimeoutStartSec of the service
ARCHIVE_MEMORY_MAX = 134217728   # MemoryMax=128M
EXIT_DEFERRED = 75
EXIT_NOT_STARTED = 2

WINDOW = tz27.WINDOW
IDLE = (15, 590)                 # every request starts at second 15 or later of a window, and is due to end by 590
RATE_FLOOR = 2000000             # bytes a second a transfer is budgeted at (TZ-28 section 1)
MARGIN_S = 5                     # seconds every request is budgeted beyond its bytes
KILL_BAND = (15, 470)            # the restart's SIGTERM: TZ-27's B-KILL-SVC band
RESTART_READ_S = 30              # the service's records are read 30 s after the SIGTERM, then every 10 s
RESTART_WAIT_S = 120             # until 120 s after it
DEFER_LIMIT = 3                  # the third deferral of one set halts the archive
DISK_FLOOR = 2001000000          # the recorder's floor, 2,000,000,000, plus 1,000,000 a run writes at most
RUN_MEM_FLOOR = 106086400        # MemAvailable: twice the run's measured peak (TZ-28 section 0.4)
PRE_DELETE = ("set", "upload", "verify")
TERMINAL = ("complete", "empty", "halt")

TAG_PREFIX = "pairbook-streams-"
TAG_RE = re.compile(r"pairbook-streams-[0-9]{10}")
IDLE_MAX_BYTES = (IDLE[1] - IDLE[0] - MARGIN_S) * RATE_FLOOR    # the largest file one idle stretch can carry

# G-TZ27: TZ-27's Release and its set, by the report of that TZ
TAG27 = "tz-27-pairbook-streams"
RELEASE27_ID = 409534533
SET27_PATH = "/root/btc-forensics/tz27-work--archive--set.json"
SET27_SHA256 = "ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd"
SET27_BYTES = 16570
SET27_N = 51
SET27_TOTAL = 678739504

LEDGER_KEYS = frozenset(("event", "run", "wall_ns"))
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
STAMP_RE = re.compile(r"[A-Z][a-z]{2} ([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}) UTC")

# ---- the clock: the idle stretch, the restart's band and the calendar -------------------------------


def phase_of(t):
    return int(t) % WINDOW


def budget_s(nbytes):
    """The seconds a request is held to: MARGIN_S, and its bytes at RATE_FLOOR, rounded up."""
    return MARGIN_S + -(-int(nbytes) // RATE_FLOOR)


def idle_wait(env, budget):
    """Until a second of the window at which a request of `budget` seconds starts at IDLE[0] or later and is due
    to end by IDLE[1]: the pair book's idle stretch, from its window.json at T+910 to its stream at T'+595."""
    assert 0 < budget <= IDLE[1] - IDLE[0], "a request budgeted %d s fits no idle stretch" % budget
    while True:
        now = env.time()
        p = phase_of(now)
        if IDLE[0] <= p <= IDLE[1] - budget:
            return now
        wait = IDLE[0] - p if p < IDLE[0] else WINDOW - p + IDLE[0]
        env.sleep(max(wait - (now - int(now)), 0.05))


def band_wait(env):
    """Until a second inside KILL_BAND of the window."""
    while True:
        now = env.time()
        p = phase_of(now)
        if KILL_BAND[0] <= p <= KILL_BAND[1]:
            return now
        wait = KILL_BAND[0] - p if p < KILL_BAND[0] else WINDOW - p + KILL_BAND[0]
        env.sleep(max(wait - (now - int(now)), 0.05))


def transfer_ok(t):
    """G-IDLE on one recorded request: (started inside the stretch its budget allows, ended by IDLE[1] of the
    window it started in)."""
    s = t["start_ns"] // 10 ** 9
    w0 = s // WINDOW * WINDOW
    return (IDLE[0] <= s - w0 <= IDLE[1] - t["budget_s"]), t["end_ns"] <= (w0 + IDLE[1]) * 10 ** 9


def next_calendar(now):
    """The first instant after now at 03:00:20 UTC."""
    d = int(now) // 86400 * 86400 + CALENDAR_S
    return d if d > now else d + 86400


def stamp_of(text):
    """An epoch from systemctl's own stamp, printed under TZ=UTC; None where it prints none."""
    m = STAMP_RE.fullmatch((text or "").strip())
    if m is None:
        return None
    dt = datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc)
    return int(dt.timestamp())


def show_utc(unit, props):
    """systemctl show, every stamp printed in UTC and C locale."""
    args = ["systemctl", "show", unit]
    for prop in props:
        args += ["-p", prop]
    cp = subprocess.run(args, capture_output=True, text=True, env=dict(os.environ, **SHOW_ENV))
    assert cp.returncode == 0, "systemctl show %s: %s" % (unit, cp.stderr.strip())
    return dict(line.split("=", 1) for line in cp.stdout.split("\n") if "=" in line)

# ---- the run's record ------------------------------------------------------------------------------


class Ledger:
    """ledger.jsonl: one line a step of every run, appended and never rewritten."""

    def __init__(self, state):
        self.path = os.path.join(state, "ledger.jsonl")
        self.recs = self.read()

    def read(self):
        if not os.path.exists(self.path):
            return []
        with open(self.path, encoding="utf-8") as fh:
            return [json.loads(ln) for ln in fh if ln.strip()]

    def write(self, env, rec):
        rec = dict(rec, wall_ns=env.time_ns())
        assert LEDGER_KEYS <= frozenset(rec), "a ledger record without %r" % sorted(LEDGER_KEYS - frozenset(rec))
        tz27.forbid(rec, "ledger.jsonl")
        with open(self.path, "ab") as fh:
            fh.write((json.dumps(rec, sort_keys=True) + "\n").encode("utf-8"))
        self.recs.append(rec)
        out("L %s" % json.dumps(rec, sort_keys=True))
        return rec


def halted(recs):
    """True where the last halt is not followed by a clear, which only a TZ writes."""
    flags = [r["event"] for r in recs if r.get("event") in ("halt", "clear")]
    return bool(flags) and flags[-1] == "halt"


def pending(recs):
    """The run of the last start record, where that run has no terminal record; else None."""
    starts = [r for r in recs if r.get("event") == "start"]
    if not starts:
        return None
    a = starts[-1]["run"]
    return None if any(r.get("run") == a and r.get("event") in TERMINAL for r in recs) else a


def events(recs, a, name):
    return [r for r in recs if r.get("run") == a and r.get("event") == name]


def jsonl_append(path, rec, what):
    tz27.forbid(rec, what)
    with open(path, "ab") as fh:
        fh.write((json.dumps(rec, sort_keys=True) + "\n").encode("utf-8"))


def jsonl_read(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return [json.loads(ln) for ln in fh if ln.strip()]


# ---- what the run touches outside its own files ------------------------------------------------------


class Env:
    """The clock, systemd, the store and GitHub, as the unit's run meets them."""

    def __init__(self, work=STATE):
        self.root, self.state, self.work = tz27.ROOT, STATE, work
        self.wait_min, self.gap_s = tz27.WAIT_MIN_S, tz27.UPLOAD_GAP_S
        self.api, self.uploads, self.web = tz27.API_BASE, tz27.UPLOAD_BASE, tz27.WEB_BASE
        self.invocation = os.environ.get("INVOCATION_ID")
        self.commit, self.file_sha = None, None

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

    def show(self, unit, props):
        return tz27.systemctl_show(unit, props)

    def kill(self):
        return subprocess.run(["systemctl", "kill", "--signal=SIGTERM", tz27.UNIT]).returncode

    def unit_reads(self, n):
        return tz27.unit_reads(n)

    def disable_timer(self):
        return subprocess.run(["systemctl", "disable", "--now", TIMER]).returncode

    def credential(self):
        return tz27.credential()

    def free(self):
        return tz27.free_bytes()

    def mem(self):
        return tz27.mem_available()


def release_request(tag, commit, name, body):
    """The Release's creation: on the tag, at the commit the run's code is from, published, never the latest."""
    return {"tag_name": tag, "target_commitish": commit, "name": name, "body": body, "draft": False,
            "prerelease": False, "make_latest": "false"}


class Gh28(tz27.GitHub):
    """TZ-27's GitHub, every request held to the idle stretch and timed into the run's record."""

    def __init__(self, env, token=None, record=None):
        super().__init__(token, env.api, env.uploads, env.web)
        self.env, self.record, self.sizes = env, record, {}
        self.gap_s = env.gap_s

    def _timed(self, kind, name, nbytes, fn):
        budget = budget_s(nbytes)
        idle_wait(self.env, budget)
        t0, ok = self.env.time_ns(), False
        try:
            res = fn()
            ok = True
            return res
        finally:
            if self.record is not None:
                self.record({"kind": kind, "name": name, "bytes": int(nbytes), "budget_s": budget, "start_ns": t0,
                             "end_ns": self.env.time_ns(), "ok": ok})

    def _json(self, method, url, body=None):
        path, parent = urllib.parse.urlsplit(url).path, super()._json
        return self._timed("api", "%s %s" % (method, path), 0, lambda: parent(method, url, body))

    def upload(self, rid, name, path, nbytes):
        parent = super().upload
        return self._timed("upload", name, nbytes, lambda: parent(rid, name, path, nbytes))

    def download(self, url):
        name = urllib.parse.unquote(url.rsplit("/", 1)[-1])
        nbytes, parent = self.sizes.get(name, 0), super().download
        return self._timed("download", name, nbytes, lambda: parent(url))

    def create_release(self, tag, name, body):
        assert self.token is not None and self.env.commit is not None
        self.pace()
        status, doc, _h = self._json("POST", "%s/repos/%s/releases" % (self.api, tz27.REPO),
                                     release_request(tag, self.env.commit, name, body))
        assert status == 201 and isinstance(doc, dict), "create release %s: status %r" % (tag, status)
        return doc

# ---- the set -----------------------------------------------------------------------------------------


def set_document(tag, a, root, assets, windows, deferred):
    """TZ-27's set document under this TZ's tag, which TZ-27's own tag rule does not cover, and with every file
    small enough for one idle stretch."""
    names = [x["asset"] for x in assets]
    assert TAG_RE.fullmatch(tag) and tz27.TAG_RE.fullmatch(tag) is None, "a tag named %r" % tag
    assert assets, "no stream file of a closed window"
    assert len(set(names)) == len(names), "two assets share a name"
    assert all(tz27.ASSET_RE.fullmatch(n) for n in names), "an asset name outside %s" % tz27.ASSET_RE.pattern
    assert len(assets) <= tz27.RUN_MAX_ASSETS, "%d assets, above %d" % (len(assets), tz27.RUN_MAX_ASSETS)
    big = [x["asset"] for x in assets if x["bytes"] > IDLE_MAX_BYTES]
    assert not big, "files above the %d bytes one idle stretch carries: %r" % (IDLE_MAX_BYTES, big[:3])
    doc = {"tag": tag, "as_of": a, "root": root, "repo": tz27.REPO, "assets": assets, "assets_n": len(assets),
           "bytes_total": sum(x["bytes"] for x in assets), "first_T": assets[0]["T"], "last_T": assets[-1]["T"],
           "windows": windows, "deferred": deferred}
    tz27.assert_keys(doc, tz27.SET_KEYS, "set.json")
    for x in assets:
        tz27.assert_keys(x, tz27.SET_ASSET_KEYS, "set.json asset")
        assert tz27.SHA_RE.fullmatch(x["sha256"])
    for w in windows:
        tz27.assert_keys(w, tz27.SET_WINDOW_KEYS, "set.json window")
    return doc


def release_text(doc, commit):
    name = "%s: the pair book's streams, windows %d to %d" % (doc["tag"], doc["first_T"], doc["last_T"])
    body = ("Verbatim stream files of btc-pairbook.service (research/tz26-nesting-b3-capture.py), one asset per file, "
            "named <T>-<file>: the market websocket's frames for the four books of btc-updown-15m-{T} and "
            "btc-updown-5m-{T+600}, T+595 to T+905. %d files, %d bytes, windows %d to %d, taken as of %d by "
            "btc-pairbook-archive.service at commit %s (research/tz28-pairbook-archive-timer.py, TZ-28). Reserved "
            "for B3's measurement: no TZ reads them before M0's second look has reported (CANON PART II). Each "
            "asset's SHA-256 is its digest here." % (doc["assets_n"], doc["bytes_total"], doc["first_T"],
                                                     doc["last_T"], doc["as_of"], commit))
    return name, body


def window_json(root, T):
    path = os.path.join(root, str(T), "window.json")
    if not os.path.exists(path):
        return None
    with open(path, "rb") as fh:
        wj = json.loads(fh.read())
    s = wj.get("stream") if isinstance(wj.get("stream"), dict) else {}
    out("window %d: pid %s, documents %s; stream opened %s, off_reason %s, files %s, segments %s, frames %s, "
        "stored_bytes %s" % (T, wj.get("pid"), wj.get("documents_ok"), s.get("opened"), s.get("off_reason"),
                             s.get("files"), s.get("segments"), s.get("frames"), s.get("stored_bytes")))
    return wj

# ---- the run: its phases -------------------------------------------------------------------------------


def floors(env):
    mem, free = env.mem(), env.free()
    out("MemAvailable %d bytes, floor %d; free %d bytes, floor %d" % (mem, RUN_MEM_FLOOR, free, DISK_FLOOR))
    assert mem >= RUN_MEM_FLOOR, "MemAvailable %d bytes, below %d" % (mem, RUN_MEM_FLOOR)
    assert free >= DISK_FLOOR, "free %d bytes, below %d" % (free, DISK_FLOOR)


def new_set(env, led, a, rdir):
    tz27.MODE[0] = "inventory"
    assets, windows, deferred, open_n = tz27.inventory(env.root, a)
    for w in windows:
        out("W %d %s %-8s stream files %d, %d bytes, taken %d" % (w["T"], tz27.utc(w["T"]), w["disposition"],
                                                               w["streams"], w["stream_bytes"], w["taken"]))
    counts = {"windows_considered": len(windows), "open": open_n, "deferred": deferred,
              "closed": sum(1 for w in windows if w["disposition"] == "closed"),
              "unclosed": sum(1 for w in windows if w["disposition"] == "unclosed")}
    if not assets:
        led.write(env, dict({"event": "empty", "run": a}, **counts))
        return None
    doc = set_document(TAG_PREFIX + str(a), a, env.root, assets, windows, deferred)
    for x in assets:
        out("S %s %d %s" % (x["asset"], x["bytes"], x["sha256"]))
    raw = tz27.json_bytes(doc)
    with open(os.path.join(rdir, "set.json"), "wb") as fh:
        fh.write(raw)
    led.write(env, dict({"event": "set", "run": a, "tag": doc["tag"], "sha256": tz27.sha256_bytes(raw),
                         "assets_n": doc["assets_n"], "bytes_total": doc["bytes_total"], "first_T": doc["first_T"],
                         "last_T": doc["last_T"]}, **counts))
    return doc


def load_set(led, a, rdir):
    """The pending run's set, asserted by the SHA-256 its set record carries; None where it has none yet."""
    recs = events(led.recs, a, "set")
    if not recs:
        return None
    with open(os.path.join(rdir, "set.json"), "rb") as fh:
        raw = fh.read()
    assert tz27.sha256_bytes(raw) == recs[-1]["sha256"], "set.json is not the set its record names"
    return json.loads(raw)


def transfers_logger(rdir):
    path = os.path.join(rdir, "transfers.jsonl")
    return lambda rec: jsonl_append(path, rec, "transfers.jsonl")


def upload_phase(env, led, a, rdir, doc):
    tz27.MODE[0] = "upload"
    tok, source = env.credential()
    out("credential: %s" % source)
    gh = Gh28(env, tok, transfers_logger(rdir))
    rel = gh.release_by_tag(doc["tag"])
    created = rel is None
    if created:
        rel = gh.create_release(doc["tag"], *release_text(doc, env.commit))
        out("created the Release on %s, id %s" % (doc["tag"], rel.get("id")))
    assert rel.get("tag_name") == doc["tag"] and rel.get("draft") is False, "the Release is not published on the tag"
    path = os.path.join(rdir, "upload.jsonl")

    def log(rec):
        rec = dict(rec, at=tz27.utc(env.time()))
        jsonl_append(path, rec, "upload.jsonl")
        out("U %s" % json.dumps(rec, sort_keys=True))

    sent, held = tz27.upload_set(gh, rel, doc, env.root, log, wait_min=env.wait_min)
    log({"action": "complete", "assets": sent + held, "sent": sent, "held": held, "release_id": int(rel["id"]),
         "credential": source, "wall_ns": env.time_ns()})
    led.write(env, {"event": "upload", "run": a, "release_id": int(rel["id"]), "created": created, "sent": sent,
                    "held": held, "credential": source})


def verify_phase(env, led, a, rdir, doc):
    tz27.MODE[0] = "verify"
    records = jsonl_read(os.path.join(rdir, "upload.jsonl"))
    assert records and records[-1].get("action") == "complete" and records[-1].get("assets") == doc["assets_n"], \
        "verify: upload has not completed the set"
    ready_ns = records[-1]["wall_ns"] + tz27.UPLOAD_SETTLE_S * 10 ** 9
    while tz27.upload_ready(records, doc["assets_n"], env.time_ns()) is not None:
        env.sleep((ready_ns - env.time_ns()) / 1e9 + 0.5)
    anon = Gh28(env, None, transfers_logger(rdir))
    anon.sizes = {x["asset"]: x["bytes"] for x in doc["assets"]}
    rel, rows, missing, extra = tz27.verify_release(anon, doc["tag"], doc)
    for r in rows:
        out("V %s id %s state %s api %s bytes %s digest %s url %s download %s" % (
            r["asset"], r["id"], r["state"], r["api_ok"], r["api_bytes"], r["digest"], r["url_ok"], r["download_ok"]))
    checks = tz27.release_reading(rel, doc["tag"], rows, missing, extra)
    for k, v in checks.items():
        out("G-UPLOAD/G-DOWNLOAD %-52s %s" % (k, v))
    assert all(checks.values()), "VERIFY FAIL: %r; missing %r; beyond %r" % (
        sorted(k for k, v in checks.items() if not v), missing[:5], extra[:5])
    vdoc = {"tag": doc["tag"], "release_id": int(rel["id"]), "set_sha256": tz27.sha256_bytes(tz27.json_bytes(doc)),
            "assets": rows, "assets_n": len(rows), "bytes_total": sum(r["download_bytes"] for r in rows)}
    tz27.assert_keys(vdoc, tz27.VERIFY_KEYS, "verify.json")
    for r in rows:
        tz27.assert_keys(r, tz27.VERIFY_ROW_KEYS, "verify.json row")
    vraw = tz27.json_bytes(vdoc)
    with open(os.path.join(rdir, "verify.json"), "wb") as fh:
        fh.write(vraw)
    led.write(env, {"event": "verify", "run": a, "release_id": int(rel["id"]), "assets_n": len(rows),
                    "bytes_total": vdoc["bytes_total"], "verify_sha256": tz27.sha256_bytes(vraw)})
    return tz27.sha256_bytes(vraw)


def delete_phase(env, led, a, rdir, doc, vsha):
    tz27.MODE[0] = "delete"
    with open(os.path.join(rdir, "verify.json"), "rb") as fh:
        assert tz27.sha256_bytes(fh.read()) == vsha, "delete: verify.json is not this run's"
    path = os.path.join(rdir, "delete.jsonl")

    def log(row):
        jsonl_append(path, row, "delete.jsonl")
        out("X %s %d %s removed" % (row["asset"], row["bytes"], row["sha256"]))

    done = {r["asset"] for r in jsonl_read(path)}
    free_before = env.free()
    _rows, removed, freed, already = tz27.delete_set(env.root, doc, done, int(env.time()), log)
    checks, gone, kept = tz27.removed_reading(env.root, doc, {r["asset"] for r in jsonl_read(path)})
    for k, v in checks.items():
        out("G-DELETE %-36s %s" % (k, v))
    assert all(checks.values()), "REMOVED FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    led.write(env, {"event": "delete", "run": a, "removed": removed, "already": already, "freed": freed,
                    "gone": gone, "windows_kept": kept, "free_before": free_before, "free_after": env.free()})


def restart_phase(env, led, a, doc):
    tz27.MODE[0] = "restart"
    band_wait(env)
    kv = env.show(tz27.UNIT, ["MainPID", "NRestarts", "ActiveState"])
    assert kv.get("ActiveState") == "active", "the pair book is %r: not restarted" % kv.get("ActiveState")
    mark = {"ns": env.time_ns(), "MainPID": kv["MainPID"], "NRestarts": kv["NRestarts"],
            "ActiveState": kv["ActiveState"]}
    p = phase_of(mark["ns"] // 10 ** 9)
    assert KILL_BAND[0] <= p <= KILL_BAND[1], "the mark at second %d, outside the band" % p
    led.write(env, {"event": "mark", "run": a, "mark": mark, "phase": p})
    rc = env.kill()
    led.write(env, {"event": "kill", "run": a, "exit": rc, "phase": phase_of(env.time())})
    assert rc == 0, "systemctl kill: exit %r" % rc
    deadline = env.time() + RESTART_WAIT_S
    env.sleep(RESTART_READ_S)
    while True:
        recs = tz27.read_runtime(os.path.join(env.root, "runtime.jsonl"))
        checks, stop, start, _after = tz27.restart_reading(recs, mark)
        if all(checks.values()) or env.time() >= deadline:
            break
        env.sleep(10)
    for k, v in checks.items():
        out("G-RESTART %-30s %s" % (k, v))
    assert all(checks.values()), "G-RESTART FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    c, W, view, left = tz27.counter_reading(env.root, start, doc)
    for k, v in c.items():
        out("G-COUNTER %-40s %s" % (k, v))
    assert all(c.values()), "G-COUNTER FAIL: %r; left %r" % (sorted(k for k, v in c.items() if not v), left[:5])
    kvu, uchecks, pid = env.unit_reads(int(mark["NRestarts"]) + 1)
    uchecks = dict(uchecks, **{"the new start's process": pid == start.get("pid")})
    for k, v in uchecks.items():
        out("G-UNIT %-24s %s" % (k, v))
    assert all(uchecks.values()), "G-UNIT FAIL: %r" % sorted(k for k, v in uchecks.items() if not v)
    led.write(env, {"event": "restart", "run": a, "W": W, "pid": start["pid"], "stopped": stop["pid"],
                    "gap_ns": start["wall_ns"] - stop["wall_ns"], "stream_bytes": view,
                    "free_bytes": start.get("free_bytes"), "NRestarts": kvu.get("NRestarts")})
    return W, start["pid"]


def resume_phase(env, led, a, W, pid):
    tz27.MODE[0] = "resume"
    while True:
        reading, T, checks = tz27.resume_decision(W, pid, int(env.time()), lambda t: window_json(env.root, t))
        if reading != "NOT YET":
            break
        env.sleep(T + tz27.CLOSE_OFFSET + tz27.RESUME_AFTER_S - env.time() + 1)
    for k, v in checks.items():
        out("G-RESUME %-30s %s" % (k, v))
    led.write(env, {"event": "resume", "run": a, "reading": reading, "T": T})
    assert reading != "FAIL", "G-RESUME FAIL at window %d" % T


def final_phase(env, led, a, rdir, doc):
    tz27.MODE[0] = "final"
    trs = jsonl_read(os.path.join(rdir, "transfers.jsonl"))
    idle = [transfer_ok(t) for t in trs]
    counter, free = tz27.stream_bytes_view(env.root), env.free()
    rate, rows = tz27.projection(doc["bytes_total"], doc["first_T"], doc["last_T"], counter, free, int(env.time()))
    for what, d, when in rows:
        out("at the set's rate %s stops the streams in %s days, at %s" % (what, tz27.decimals(d, 2), tz27.utc(when)))
    led.write(env, {"event": "complete", "run": a, "assets_n": doc["assets_n"], "bytes_total": doc["bytes_total"],
                    "requests": len(trs), "started_outside": sum(1 for s, _e in idle if not s),
                    "ended_outside": sum(1 for _s, e in idle if not e), "store_stream_bytes": counter,
                    "free_bytes": free, "rate_per_day": int(rate), "stops": [[w, int(t)] for w, _d, t in rows],
                    "peak_rss": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024})


def halt(env, led, a, phase, reason):
    led.write(env, {"event": "halt", "run": a, "phase": phase, "reason": reason[:400]})
    tz27.MODE[0] = "final"
    rc = env.disable_timer()
    led.write(env, {"event": "timer-disabled", "run": a, "exit": rc})
    out("HALTED in %s: %s; the timer disabled, exit %r" % (phase, reason[:400], rc))
    return 1


def run(env):
    """One run: the pending set resumed, or a new one as of now; exit 0, EXIT_DEFERRED or 1."""
    tz27.WORK[0], tz27.MODE[0] = env.work, "run"
    led = Ledger(env.state)
    if halted(led.recs):
        last = [r for r in led.recs if r.get("event") == "halt"][-1]
        out("HALTED since run %s, %s: %s; nothing done" % (last.get("run"), last.get("phase"), last.get("reason")))
        tz27.MODE[0] = "final"
        rc = env.disable_timer()
        led.write(env, {"event": "refused", "run": last.get("run"), "exit": rc})
        return 1
    a = pending(led.recs)
    resumed = a is not None
    if not resumed:
        a = max([int(env.time())] + [r["run"] + 1 for r in led.recs if r.get("event") == "start"])
    rdir = os.path.join(env.state, "runs", str(a))
    os.makedirs(rdir, exist_ok=True)
    led.write(env, {"event": "start", "run": a, "resumed": resumed, "commit": env.commit, "file_sha256": env.file_sha,
                    "tz27_sha256": TZ27_SHA256, "invocation": env.invocation, "phase_at": phase_of(env.time())})
    phase = "set"
    try:
        floors(env)
        doc = load_set(led, a, rdir)
        if doc is None:
            doc = new_set(env, led, a, rdir)
            if doc is None:
                out("EMPTY: no stream file of a closed window as of %d" % a)
                return 0
        if not events(led.recs, a, "delete"):
            phase = "upload"
            upload_phase(env, led, a, rdir, doc)
            phase = "verify"
            vsha = verify_phase(env, led, a, rdir, doc)
            phase = "delete"
            delete_phase(env, led, a, rdir, doc, vsha)
        phase = "restart"
        if events(led.recs, a, "restart"):
            r = events(led.recs, a, "restart")[-1]
            W, pid = r["W"], r["pid"]
        else:
            W, pid = restart_phase(env, led, a, doc)
        phase = "resume"
        if not events(led.recs, a, "resume"):
            resume_phase(env, led, a, W, pid)
        phase = "final"
        final_phase(env, led, a, rdir, doc)
        out("COMPLETE: run %d, %d files, %d bytes, Release %s" % (a, doc["assets_n"], doc["bytes_total"],
                                                                 doc["tag"]))
        return 0
    except tz27.GuardError as exc:
        return halt(env, led, a, phase, "GuardError: %s" % exc)
    except Exception as exc:
        reason = "%s: %s" % (type(exc).__name__, str(exc))
        if phase not in PRE_DELETE:
            return halt(env, led, a, phase, reason)
        n = len(events(led.recs, a, "deferred")) + 1
        if n >= DEFER_LIMIT:
            return halt(env, led, a, phase, "deferral %d of %d: %s" % (n, DEFER_LIMIT, reason))
        led.write(env, {"event": "deferred", "run": a, "phase": phase, "reason": reason[:400], "count": n})
        out("DEFERRED in %s, %d of %d: %s; nothing removed, the next run resumes this set" % (
            phase, n, DEFER_LIMIT, reason[:400]))
        return EXIT_DEFERRED


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
        return EXIT_NOT_STARTED
    out("run: pid %d, commit %s, file sha256 %s, invocation %s" % (os.getpid(), env.commit, env.file_sha,
                                                                   env.invocation))
    return run(env)

# ---- the deployment's readings: the session's modes ------------------------------------------------------


def mode_fingerprint():
    tz27.MODE[0] = "fingerprint"
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


def mode_tz27_release():
    """G-TZ27: TZ-27's Release, read anonymously through the API, against the set.json TZ-27 froze."""
    tz27.MODE[0] = "tz27-release"
    tz27.floor_check()
    with open(SET27_PATH, "rb") as fh:
        raw = fh.read()
    assert len(raw) == SET27_BYTES and tz27.sha256_bytes(raw) == SET27_SHA256, "%s is not TZ-27's set" % SET27_PATH
    doc = json.loads(raw)
    assert doc["tag"] == TAG27 and doc["assets_n"] == SET27_N and doc["bytes_total"] == SET27_TOTAL, "TZ-27's set"
    rel, rows, missing, extra = tz27.verify_release(tz27.GitHub(), TAG27, doc, download=False)
    for r in rows:
        out("V %s id %s state %s bytes %s digest %s url %s: %s" % (r["asset"], r["id"], r["state"], r["api_bytes"],
                                                                  r["digest"], r["url_ok"], r["api_ok"]))
    checks = {k: v for k, v in tz27.release_reading(rel, TAG27, rows, missing, extra).items()
              if not k.startswith("every download")}
    checks["the Release TZ-27 created"] = rel is not None and rel.get("id") == RELEASE27_ID
    for k, v in checks.items():
        out("G-TZ27 %-52s %s" % (k, v))
    if missing or extra:
        out("missing %r; beyond the set %r" % (missing[:10], extra[:10]))
    assert all(checks.values()), "G-TZ27 FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    out("G-TZ27 PASS: Release %d on %s, %d of %d assets uploaded with the set's bytes and digest, nothing beyond "
        "the set; %d requests" % (RELEASE27_ID, TAG27, sum(r["api_ok"] for r in rows), SET27_N,
                                  tz27.COUNTERS["requests"]))


def session_env():
    env = Env(work=tz27.WORK[0])
    return env


def mode_path():
    """P-PATH: the run's own Gh28, with no token, on the asset whose bytes map 2.1 fixes: 3 requests."""
    tz27.MODE[0] = "path"
    tz27.floor_check()
    env = session_env()
    trs = []
    gh = Gh28(env, None, trs.append)
    gh.sizes[tz27.PATH_ASSET] = tz27.PATH_BYTES
    rel = gh.release_by_tag(tz27.PATH_TAG)
    assert rel is not None, "P-PATH: no release on %s" % tz27.PATH_TAG
    a = {x.get("name"): x for x in gh.assets(int(rel["id"]))}.get(tz27.PATH_ASSET)
    url = gh.download_url(tz27.PATH_TAG, tz27.PATH_ASSET)
    row = tz27.asset_row({"asset": tz27.PATH_ASSET, "bytes": tz27.PATH_BYTES, "sha256": tz27.PATH_SHA256}, a, url)
    out("P-PATH release %s id %s; asset %s state %s, %s bytes, digest %s, url %s" % (
        tz27.PATH_TAG, rel.get("id"), tz27.PATH_ASSET, row["state"], row["api_bytes"], row["digest"], row["url_ok"]))
    assert row["api_ok"], "P-PATH: the API's record of %s is not the map's" % tz27.PATH_ASSET
    status, n, h = tz27.download_checked(gh, url)
    out("P-PATH download: status %r, %d bytes, sha256 %s" % (status, n, h))
    assert status == 200 and n == tz27.PATH_BYTES and h == tz27.PATH_SHA256, "P-PATH: not the map's bytes"
    for t in trs:
        s, e = transfer_ok(t)
        out("T %s %s: %d bytes, budget %d s, second %d, %.1f s, inside %s %s" % (
            t["kind"], t["name"], t["bytes"], t["budget_s"], phase_of(t["start_ns"] // 10 ** 9),
            (t["end_ns"] - t["start_ns"]) / 1e9, s, e))
    assert len(trs) == 3 and all(all(transfer_ok(t)) for t in trs), "P-PATH: a request outside the idle stretch"
    out("READING P-PATH: served - 3 requests through the run's own path, each inside the idle stretch; the digest "
        "present and equal; %d bytes downloaded and equal" % n)


def mode_path_token():
    """B-PATH-TOKEN: the Boss's. The run's credential, as the run reads it; nothing prints it."""
    tz27.MODE[0] = "upload"
    tz27.floor_check()
    tok, source = tz27.credential()
    out("credential: %s" % source)
    assert source == "the primary checkout's remote URL", "P-TOKEN: the run reads the remote URL's credential, not %s" % (
        source,)
    env = session_env()
    gh = Gh28(env, tok, None)
    status, doc, _h = gh._json("GET", "%s/repos/%s" % (gh.api, tz27.REPO))
    perms = (doc or {}).get("permissions") if isinstance(doc, dict) else None
    out("repository: status %r, full_name %r, push %r" % (status, (doc or {}).get("full_name") if isinstance(doc, dict)
                                                           else None, (perms or {}).get("push")))
    assert status == 200 and doc.get("full_name") == tz27.REPO and (perms or {}).get("push") is True, \
        "P-TOKEN: the credential does not write this repository"
    rel = gh.release_by_tag(TAG27)
    assert rel is not None and rel.get("id") == RELEASE27_ID, "P-TOKEN: the Release on %s" % TAG27
    out("READING P-TOKEN: served - the credential from %s reads %s with push, and the Release %d; %d requests" % (
        source, tz27.REPO, RELEASE27_ID, tz27.COUNTERS["requests"]))


def git_out(*args):
    cp = subprocess.run(["git"] + list(args), capture_output=True, text=True)
    assert cp.returncode == 0, "git %s: exit %d" % (" ".join(args), cp.returncode)
    return cp.stdout.strip()


def mode_installed():
    """G-INSTALL: what B-INSTALL put on the host, against the branch's worktree."""
    tz27.MODE[0] = "installed"
    wt = tz27.wpath("wt")
    head, up = git_out("-C", wt, "rev-parse", "HEAD"), git_out("-C", wt, "rev-parse", "@{u}")
    with open(os.path.join(ASVC, "commit.txt"), encoding="utf-8") as fh:
        commit = fh.read().strip()
    files = {}
    for name in (SELF_NAME, TZ27_NAME):
        files[name] = (tz27.sha256_file(os.path.join(ASVC, name))[0],
                       tz27.sha256_file(os.path.join(wt, "research", name))[0])
    units = {}
    for name in (ARCHIVE, TIMER):
        with open(os.path.join(UNIT_DIR, name), "rb") as a_:
            installed = a_.read()
        with open(os.path.join(wt, "deploy", "systemd", name), "rb") as b_:
            units[name] = installed == b_.read()
    st = os.stat(STATE)
    svc = show_utc(ARCHIVE, ["LoadState", "ActiveState", "UnitFileState", "FragmentPath", "Type", "Restart",
                             "MemoryMax", "TimeoutStartUSec", "WorkingDirectory", "ExecStart"])
    tmr = show_utc(TIMER, ["LoadState", "ActiveState", "UnitFileState", "FragmentPath"])
    argv = "argv[]=%s ;" % " ".join(RUN_ARGV)
    checks = {"commit.txt the branch head, pushed": commit == head == up,
              "the service's copy of this file the branch's": files[SELF_NAME][0] == files[SELF_NAME][1],
              "the service's copy of TZ-27's file, %s" % TZ27_SHA256[:12]: files[TZ27_NAME][0] == files[TZ27_NAME][1]
              == TZ27_SHA256,
              "the two units byte for byte": all(units.values()),
              "the state directory, root's, 0700, empty": os.path.isdir(STATE) and st.st_uid == 0
              and (st.st_mode & 0o777) == 0o700 and not os.listdir(STATE),
              "the service loaded, inactive, static": (svc["LoadState"], svc["ActiveState"], svc["UnitFileState"])
              == ("loaded", "inactive", "static"),
              "the service a oneshot, Restart=no, 128M, 6h, its argv and directory": svc["Type"] == "oneshot"
              and svc["Restart"] == "no" and svc["MemoryMax"] == str(ARCHIVE_MEMORY_MAX)
              and svc["TimeoutStartUSec"] == "6h" and svc["WorkingDirectory"] == STATE and argv in svc["ExecStart"]
              and svc["FragmentPath"] == UNIT_DIR + "/" + ARCHIVE,
              "the timer loaded, inactive, disabled": (tmr["LoadState"], tmr["ActiveState"], tmr["UnitFileState"],
                                                       tmr["FragmentPath"]) == ("loaded", "inactive", "disabled",
                                                                                UNIT_DIR + "/" + TIMER)}
    for name, (a_, b_) in sorted(files.items()):
        out("%s/%s sha256 %s; the branch's %s" % (ASVC, name, a_, b_))
    out("commit.txt %s; the branch head %s, its upstream %s" % (commit, head, up))
    for k, v in checks.items():
        out("G-INSTALL %-66s %s" % (k, v))
    assert all(checks.values()), "G-INSTALL FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    out("G-INSTALL PASS: %d of %d" % (len(checks), len(checks)))


def mode_mark(name):
    if name == "start-svc":
        tz27.MODE[0] = "mark"
        return tz27.mode_mark(name)
    assert name in ("enable", "retry"), "mark %r" % name
    tz27.MODE[0] = "mark"
    st = tz27.load_state()
    marks = st.setdefault("marks28", {})
    assert name not in marks, "mark %s already taken" % name
    tmr = show_utc(TIMER, ["ActiveState", "UnitFileState"])
    svc = show_utc(ARCHIVE, ["ActiveState", "Result"])
    marks[name] = {"ns": time.time_ns(), "timer": tmr, "service": svc}
    tz27.save_state(st)
    out("mark %s at %s: the timer %r, the service %r" % (name, tz27.utc(marks[name]["ns"] / 1e9), tmr, svc))


def timer_reading(now):
    kv = show_utc(TIMER, ["LoadState", "ActiveState", "SubState", "UnitFileState", "FragmentPath", "Unit",
                          "TimersCalendar", "TimersMonotonic", "NextElapseUSecRealtime", "AccuracyUSec",
                          "LastTriggerUSec", "ActiveEnterTimestamp"])
    nxt = stamp_of(kv.get("NextElapseUSecRealtime"))
    checks = {"loaded": kv["LoadState"] == "loaded",
              "active": kv["ActiveState"] == "active" and kv["SubState"] in ("waiting", "running"),
              "enabled": kv["UnitFileState"] == "enabled",
              "fragment": kv["FragmentPath"] == UNIT_DIR + "/" + TIMER,
              "its unit": kv["Unit"] == ARCHIVE,
              "the calendar": ("OnCalendar=%s ;" % CALENDAR) in kv["TimersCalendar"],
              "600 s after it starts": "OnActiveUSec=10min" in kv["TimersMonotonic"],
              "accuracy 1 s": kv["AccuracyUSec"] == "1s",
              "the next calendar elapse": nxt == next_calendar(now)}
    return kv, checks, nxt


def mode_timer():
    tz27.MODE[0] = "timer"
    now = time.time()
    kv, checks, nxt = timer_reading(now)
    out("the timer: %r" % kv)
    for k, v in checks.items():
        out("G-TIMER %-24s %s" % (k, v))
    assert all(checks.values()), "G-TIMER FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    out("G-TIMER PASS: the next calendar run at %s, the run after the start at %s" % (
        tz27.utc(nxt), tz27.utc((stamp_of(kv.get("ActiveEnterTimestamp")) or 0) + ACTIVE_S)))


def first_run(recs, since_ns):
    """The run of the first start record at or after since_ns, and every record of that run."""
    starts = [r for r in recs if r.get("event") == "start" and r["wall_ns"] >= since_ns]
    if not starts:
        return None, []
    a = starts[0]["run"]
    return a, [r for r in recs if r.get("run") == a]


def mode_first():
    """The first run after the enable mark, re-read from its records, the store, the service's record, systemd and
    the Release: exit 3 while it has not ended."""
    tz27.MODE[0] = "final"
    st = tz27.load_state()
    mark = st.get("marks28", {}).get("enable")
    assert mark is not None, "first: no enable mark"
    svc = show_utc(ARCHIVE, ["ActiveState", "Result", "ExecMainStatus", "ExecMainStartTimestamp",
                             "ExecMainExitTimestamp", "InvocationID"])
    recs = Ledger(STATE).recs
    a, mine = first_run(recs, mark["ns"])
    if a is None or svc["ActiveState"] in ("activating", "active", "deactivating"):
        out("NOT YET: %s; the service %s" % ("no run since the mark" if a is None else "run %d" % a,
                                              svc["ActiveState"]))
        return 3
    for r in mine:
        out("R %s" % json.dumps(r, sort_keys=True))
    out("run %d: %d records, %s" % (a, len(mine), [r["event"] for r in mine]))
    terms = [r["event"] for r in mine if r["event"] in TERMINAL]
    if not terms:
        last = mine[-1]["event"]
        out("READING G-RUN: %s - the run's last record %s, in its phase %r" % (
            "DEFERRED" if last == "deferred" else "INTERRUPTED", last, mine[-1].get("phase")))
        return 1
    last = terms[-1]
    readings = {}
    tmr = show_utc(TIMER, ["LastTriggerUSec", "ActiveEnterTimestamp"])
    trig, enter = stamp_of(tmr.get("LastTriggerUSec")), stamp_of(tmr.get("ActiveEnterTimestamp"))
    s0 = mine[0]["wall_ns"] // 10 ** 9
    readings["G-TRIGGER"] = (trig is not None and enter is not None and abs(trig - (enter + ACTIVE_S)) <= 2
                             and trig <= s0 <= trig + 60)
    out("G-TRIGGER: the timer started %s, triggered %s, the run's first record %s" % (
        tz27.utc(enter or 0), tz27.utc(trig or 0), tz27.utc(s0)))
    readings["G-RUN"] = last == "complete" and svc["Result"] == "success" and svc["ExecMainStatus"] == "0"
    out("G-RUN: the run %s; the service's last invocation %s, Result %s, ExecMainStatus %s, %s to %s" % (
        last, svc["InvocationID"], svc["Result"], svc["ExecMainStatus"], svc["ExecMainStartTimestamp"],
        svc["ExecMainExitTimestamp"]))
    if last == "complete":
        rdir = os.path.join(STATE, "runs", str(a))
        with open(os.path.join(rdir, "set.json"), "rb") as fh:
            raw = fh.read()
        sets = [r for r in mine if r["event"] == "set"]
        doc = json.loads(raw)
        readings["G-SET"] = len(sets) == 1 and tz27.sha256_bytes(raw) == sets[0]["sha256"] and \
            set_document(doc["tag"], doc["as_of"], doc["root"], doc["assets"], doc["windows"], doc["deferred"]) == doc
        for w in doc["windows"]:
            out("W %d %s %-8s stream files %d, %d bytes, taken %d" % (w["T"], tz27.utc(w["T"]), w["disposition"],
                                                                   w["streams"], w["stream_bytes"], w["taken"]))
        for x in doc["assets"]:
            out("S %s %d %s" % (x["asset"], x["bytes"], x["sha256"]))
        out("G-SET: %d files, %d bytes, windows %d to %d, as of %d, deferred %d; set.json sha256 %s" % (
            doc["assets_n"], doc["bytes_total"], doc["first_T"], doc["last_T"], doc["as_of"], doc["deferred"],
            tz27.sha256_bytes(raw)))
        rel, rows, missing, extra = tz27.verify_release(tz27.GitHub(), doc["tag"], doc, download=False)
        up = tz27.release_reading(rel, doc["tag"], rows, missing, extra)
        obj, peeled = tz27.ls_remote_tag(doc["tag"])
        started = [r for r in mine if r["event"] == "start"]
        readings["G-UPLOAD"] = all(v for k, v in up.items() if not k.startswith("every download")) and \
            obj == started[0]["commit"] and peeled is None
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
        drecs = jsonl_read(os.path.join(rdir, "delete.jsonl"))
        done = {r["asset"] for r in drecs}
        aby, vby = {r["asset"]: r for r in rows}, {r["asset"]: r for r in vdoc["assets"]}
        dby = {r["asset"]: r for r in drecs}
        for x in doc["assets"]:
            out("ROW %s %d %s digest %s download %s removed %s" % (
                x["asset"], x["bytes"], x["sha256"], aby.get(x["asset"], {}).get("digest"),
                vby.get(x["asset"], {}).get("download_sha256"), dby.get(x["asset"], {}).get("sha256")))
        dchecks, gone, kept = tz27.removed_reading(tz27.ROOT, doc, done)
        readings["G-DELETE"] = all(dchecks.values())
        out("G-DELETE: %r; %d gone, %d removals recorded, %d windows kept" % (dchecks, gone, len(done), kept))
        mk = [r for r in mine if r["event"] == "mark"][-1]["mark"]
        rr = tz27.read_runtime(tz27.ROOT + "/runtime.jsonl")
        rchecks, stop, start, _after = tz27.restart_reading(rr, mk)
        readings["G-RESTART"] = all(rchecks.values())
        out("G-RESTART: %r; the stop of %s at second %d, the start of %s %.3f s later" % (
            rchecks, stop.get("pid"), phase_of(stop.get("wall_ns", 0) // 10 ** 9), start.get("pid"),
            (start.get("wall_ns", 0) - stop.get("wall_ns", 0)) / 1e9))
        cchecks, W, view, _left = tz27.counter_reading(tz27.ROOT, start, doc)
        readings["G-COUNTER"] = all(cchecks.values()) and start.get("stream_bytes") == view
        out("G-COUNTER: %r; stream_bytes %s, the store's windows up to %d %d bytes" % (
            cchecks, start.get("stream_bytes"), W - WINDOW, view))
        kvu, uchecks, pid = tz27.unit_reads(int(mk["NRestarts"]) + 1)
        readings["G-UNIT"] = all(uchecks.values()) and pid == start.get("pid")
        out("G-UNIT: %r; MainPID %d" % (uchecks, pid))
        reading, T, _c = tz27.resume_decision(W, start.get("pid"), int(time.time()),
                                              lambda t: window_json(tz27.ROOT, t))
        readings["G-RESUME"] = reading in ("PASS", "UNDECIDABLE")
        out("READING G-RESUME: %s, window %d" % (reading, T))
        trs = jsonl_read(os.path.join(rdir, "transfers.jsonl"))
        for t in trs:
            s, e = transfer_ok(t)
            out("T %s %s: %d bytes, budget %d s, second %d, %.1f s, inside %s %s" % (
                t["kind"], t["name"], t["bytes"], t["budget_s"], phase_of(t["start_ns"] // 10 ** 9),
                (t["end_ns"] - t["start_ns"]) / 1e9, s, e))
        readings["G-IDLE"] = bool(trs) and all(all(transfer_ok(t)) for t in trs)
        out("G-IDLE: %d requests, %d started outside, %d ended outside" % (
            len(trs), sum(1 for t in trs if not transfer_ok(t)[0]), sum(1 for t in trs if not transfer_ok(t)[1])))
        comp = mine[-1]
        out("the run's own record: %s" % json.dumps(comp, sort_keys=True))
    for k, v in readings.items():
        out("READING %-11s %s" % (k, "PASS" if v else "FAIL"))
    bad = sorted(k for k, v in readings.items() if not v)
    assert not bad, "FIRST FAIL: %r" % bad
    out("FIRST PASS: %d of %d" % (len(readings), len(readings)))
    return 0


def mode_final():
    tz27.MODE[0] = "final"
    recs = Ledger(STATE).recs
    marks = [r for r in recs if r.get("event") == "mark"]
    st = tz27.load_state()
    n = int(marks[-1]["mark"]["NRestarts"]) + 1 if marks and "start-svc" not in st.get("marks", {}) else None
    tz27.mode_unit(n)
    tz27.mode_still()
    now = time.time()
    kv, checks, nxt = timer_reading(now)
    for k, v in checks.items():
        out("G-TIMER %-24s %s" % (k, v))
    assert all(checks.values()), "G-TIMER FAIL: %r" % sorted(k for k, v in checks.items() if not v)
    counter, free = tz27.stream_bytes_view(tz27.ROOT), tz27.free_bytes()
    dirs = tz27.window_dirs(tz27.ROOT)
    out("the store: %d window directories, %d to %d; its stream files %d bytes; free %d bytes" % (
        len(dirs), dirs[0] if dirs else 0, dirs[-1] if dirs else 0, counter, free))
    done = [r for r in recs if r.get("event") == "complete"]
    if done:
        sets = [r for r in recs if r.get("event") == "set" and r["run"] == done[-1]["run"]][-1]
        rate, rows = tz27.projection(sets["bytes_total"], sets["first_T"], sets["last_T"], counter, free, int(now))
        out("the last set's rate: %s bytes a day" % tz27.decimals(rate, 0))
        for what, d, when in rows:
            out("at that rate %s stops the streams in %s days, at %s" % (what, tz27.decimals(d, 2), tz27.utc(when)))
    out("the next run at %s; the ledger %d records" % (tz27.utc(nxt), len(recs)))
    out("FINAL PASS")

# ---- the self-test: literals, temporary stores, a simulated pair book and a loopback server only --------------


class FakeEnv(Env):
    """The run's world in a temporary directory: a clock that moves only when the run sleeps, a pair book that
    restarts on a SIGTERM and writes its records, and GitHub on 127.0.0.1."""

    def __init__(self, work, root, state, base, t0, token):
        self.root, self.state, self.work = root, state, work
        self.wait_min, self.gap_s = 0, 0.0
        self.api = self.uploads = self.web = base
        self.invocation, self.commit, self.file_sha = "selftest", "c" * 40, "f" * 64
        self.clock, self.token, self.cred_ok = float(t0), token, True
        self.pid, self.nrestarts, self.kills, self.disabled = 815823, 2, 0, 0
        self.skew, self.on_sleep, self.active = 0, None, "active"

    def time(self):
        return self.clock

    def time_ns(self):
        return int(round(self.clock * 1e9))

    def sleep(self, s):
        self.clock += max(0.0, s)
        if self.on_sleep is not None:
            self.on_sleep(self)

    def show(self, unit, props):
        return {"MainPID": str(self.pid), "NRestarts": str(self.nrestarts), "ActiveState": self.active}

    def record(self, rec):
        with open(os.path.join(self.root, "runtime.jsonl"), "ab") as fh:
            fh.write((json.dumps(rec, sort_keys=True) + "\n").encode("utf-8"))

    def kill(self):
        t = self.clock
        W = int(t + 5.6) // WINDOW * WINDOW
        self.record({"event": "stop", "pid": self.pid, "wall_ns": int((t + 0.2) * 1e9)})
        self.pid, self.nrestarts, self.kills = self.pid + 1, self.nrestarts + 1, self.kills + 1
        self.record({"event": "start", "pid": self.pid, "wall_ns": int((t + 5.6) * 1e9), "commit": "e8b4",
                     "file_sha256": "caed", "free_bytes": 12931072000,
                     "stream_bytes": tz27.stream_bytes_view(self.root, upto=W - WINDOW) + self.skew})
        d = os.path.join(self.root, str(W))
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "window.json"), "w", encoding="utf-8") as fh:
            json.dump({"pid": self.pid, "documents_ok": True, "stream": {"opened": True, "off_reason": None,
                                                                         "files": ["stream.jsonl.gz"]}}, fh)
        return 0

    def unit_reads(self, n):
        checks = {"active": True, "argv": True, "sole instance": True, "restarts": self.nrestarts == n}
        return {"NRestarts": str(self.nrestarts)}, checks, self.pid

    def disable_timer(self):
        self.disabled += 1
        return 0

    def credential(self):
        if not self.cred_ok:
            raise AssertionError("UPLOAD REFUSED: no credential (selftest)")
        return self.token, "the selftest's"

    def free(self):
        return 12931072000

    def mem(self):
        return 300000000


def mode_selftest():
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    sep = ":" + "//"
    # the clock, against integers computed outside this file
    ok([budget_s(0), budget_s(1), budget_s(2000000), budget_s(2000001), budget_s(100000000)] == [5, 6, 6, 7, 55]
       and IDLE_MAX_BYTES == 1140000000, "the budget: 5 s and the bytes at 2,000,000 a second, rounded up")
    ok(next_calendar(1791720000) == 1791774020 and next_calendar(1791774019) == 1791774020
       and next_calendar(1791774020) == 1791860420, "the calendar: 03:00:20 UTC, the next after now")
    ok(stamp_of("Mon 2026-10-12 03:00:20 UTC") == 1791774020 and stamp_of("n/a") is None and stamp_of("") is None
       and stamp_of("Mon 2026-10-12 03:00:20 CEST") is None, "systemctl's stamps, read in UTC alone")
    T = 1791747000
    ok([transfer_ok({"start_ns": (T + p) * 10 ** 9, "end_ns": (T + q) * 10 ** 9, "budget_s": b})
        for p, q, b in ((15, 20, 5), (14, 20, 5), (585, 590, 5), (586, 590, 5), (15, 591, 5), (540, 600, 55))]
       == [(True, True), (False, True), (True, True), (False, True), (True, False), (False, False)],
       "G-IDLE: a request starts at second 15 to 590 less its budget, and ends by second 590")

    class Clock:
        def __init__(self, t):
            self.t, self.slept = float(t), []

        def time(self):
            return self.t

        def sleep(self, s):
            self.slept.append(s)
            self.t += s

    c = Clock(T + 585.25)
    idle_wait(c, 5)
    c2 = Clock(T + 3)
    idle_wait(c2, 55)
    c3 = Clock(T + 540)
    idle_wait(c3, 55)
    c4 = Clock(T + 471)
    band_wait(c4)
    c5 = Clock(T + 200)
    band_wait(c5)
    ok(phase_of(c.t) == 585 and c.slept == [] and phase_of(c2.t) == 15 and phase_of(c3.t) == 15
       and int(c3.t) == T + 900 + 15 and phase_of(c4.t) == 15 and int(c4.t) == T + 915 and c5.slept == [],
       "idle_wait and band_wait: now where the second allows, else the next allowed second")
    try:
        idle_wait(Clock(T), 576)
        big = False
    except AssertionError:
        big = True
    ok(big, "a request longer than the idle stretch stops the run")
    ok(TAG_RE.fullmatch("pairbook-streams-1791747020") and tz27.TAG_RE.fullmatch("pairbook-streams-1791747020") is None
       and TAG_RE.fullmatch("tz-27-pairbook-streams") is None, "this TZ's tags, which TZ-27's rule does not cover")
    rq = release_request("pairbook-streams-1791747020", "c" * 40, "n", "b")
    ok(rq["target_commitish"] == "c" * 40 and rq["draft"] is False and rq["make_latest"] == "false"
       and sorted(rq) == ["body", "draft", "make_latest", "name", "prerelease", "tag_name", "target_commitish"],
       "the Release is created at the run's commit, published, never the latest")
    recs = [{"event": "start", "run": 1}, {"event": "deferred", "run": 1}, {"event": "start", "run": 1}]
    ok(pending(recs) == 1 and pending(recs + [{"event": "complete", "run": 1}]) is None and pending([]) is None
       and halted(recs + [{"event": "halt", "run": 1}]) and not halted(recs + [{"event": "halt", "run": 1},
                                                                               {"event": "clear", "run": None}]),
       "the ledger: a run without a terminal record is resumed; a halt holds until a clear")
    # TZ-27's hook, under the modes the run gives it
    w, s0 = STATE, tz27.ROOT + "/1791747000/stream.jsonl.gz"
    P = tz27.policy
    ok(P("upload", "open", (w + "/ledger.jsonl", "ab", 0), w, set()) is None
       and P("verify", "open", (w + "/runs/1/verify.json", "wb", 0), w, set()) is None
       and P("verify", "open", ("/root/tz28-work/x", "wb", 0), w, set()) is not None
       and P("verify", "open", (s0, "rb", 0), w, set()) is not None
       and P("delete", "os.remove", (s0, None), w, {s0}) is None
       and P("restart", "os.remove", (s0, None), w, {s0}) is not None
       and P("inventory", "subprocess.Popen", ("systemctl",), w, set()) is not None
       and P("final", "subprocess.Popen", ("systemctl",), w, set()) is None
       and P("run", "open", (tz27.RECORDER + "/runtime.jsonl", "rb", 0), w, set()) is not None,
       "the run writes under its state alone, reads the store where TZ-27 did, and starts no process in "
       "inventory or delete")
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
    ok(128 * 2 ** 20 == ARCHIVE_MEMORY_MAX and 6 * 3600 == TIMEOUT_S, "128M and 6h in bytes and seconds")
    # the run on temporary stores, a simulated pair book and the loopback server
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

    def put(root, T_, name, nbytes):
        d = os.path.join(root, str(T_))
        os.makedirs(d, exist_ok=True)
        data = (hashlib.sha256(("%d/%s" % (T_, name)).encode()).digest() * (nbytes // 32 + 1))[:nbytes]
        with open(os.path.join(d, name), "wb") as fh:
            fh.write(data)
        blobs[(T_, name)] = data

    def closed(root, T_, streams):
        for k_, nb in enumerate(streams):
            put(root, T_, "stream.jsonl.gz" if k_ == 0 else "stream.%d.jsonl.gz" % k_, nb)
        put(root, T_, "books.jsonl.gz", 900)
        put(root, T_, "window.json", 300)

    def world(name, t0):
        root, state = os.path.join(tmp, name, "store"), os.path.join(tmp, name, "state")
        os.makedirs(root)
        os.makedirs(state)
        env = FakeEnv(tz27.WORK[0], root, state, base, t0, tok)
        env.record({"event": "start", "pid": env.pid, "wall_ns": int((t0 - 86400) * 1e9), "commit": "e8b4",
                    "file_sha256": "caed", "stream_bytes": 0})
        return env

    def evs(env):
        return [r["event"] for r in Ledger(env.state).recs]

    try:
        # 1. a whole run: three closed windows, one unclosed, one open
        env = world("one", T + 3600 + 80)
        closed(env.root, T, [70001])
        closed(env.root, T + 900, [50000, 33333])
        closed(env.root, T + 1800, [40000])
        put(env.root, T + 2700, "stream.jsonl.gz", 777)
        rc = run(env)
        led = Ledger(env.state).recs
        a = led[0]["run"]
        ok(rc == 0 and evs(env) == ["start", "set", "upload", "verify", "delete", "mark", "kill", "restart", "resume",
                                    "complete"] and a == T + 3680, "a run: every step recorded, in order, exit 0")
        setr = events(led, a, "set")[0]
        ok(setr["assets_n"] == 4 and setr["bytes_total"] == 193334 and setr["first_T"] == T
           and setr["last_T"] == T + 1800
           and setr["tag"] == "pairbook-streams-%d" % a and setr["open"] == 0 and setr["unclosed"] == 1,
           "the set: TZ-27's rule as of the run's start, under this TZ's tag")
        rel = Fake.releases["pairbook-streams-%d" % a]
        held = sorted(v["name"] for v in Fake.assets.values() if v["rid"] == rel["id"])
        ok(held == sorted(["%d-stream.jsonl.gz" % T, "%d-stream.jsonl.gz" % (T + 900),
                           "%d-stream.1.jsonl.gz" % (T + 900), "%d-stream.jsonl.gz" % (T + 1800)])
           and all(v["data"] == blobs[(int(v["name"][:10]), v["name"][11:])] for v in Fake.assets.values()),
           "the Release holds the set's four files, byte for byte")
        ok(sorted(os.listdir(os.path.join(env.root, str(T)))) == ["books.jsonl.gz", "window.json"]
           and sorted(os.listdir(os.path.join(env.root, str(T + 900)))) == ["books.jsonl.gz", "window.json"]
           and os.path.exists(os.path.join(env.root, str(T + 2700), "stream.jsonl.gz")),
           "the store: the set's files gone, every other entry kept")
        mk = events(led, a, "mark")[0]
        rs = events(led, a, "restart")[0]
        ok(env.kills == 1 and KILL_BAND[0] <= mk["phase"] <= KILL_BAND[1] and rs["W"] == T + 3600
           and rs["pid"] == 815824 and events(led, a, "resume")[0]["reading"] == "PASS",
           "the restart inside its band, its counter the store's, and the stream resumed")
        trs = jsonl_read(os.path.join(env.state, "runs", str(a), "transfers.jsonl"))
        comp = events(led, a, "complete")[0]
        ok(len([t for t in trs if t["kind"] == "upload"]) == 4 and len([t for t in trs if t["kind"] == "download"]) == 4
           and all(all(transfer_ok(t)) for t in trs) and comp["started_outside"] == 0 and comp["ended_outside"] == 0
           and all(h[2] == tz27.UA for h in Fake.hits)
           and all(h[3] is None for h in Fake.hits if "/releases/download/" in h[1] or h[1].startswith("/blob/")),
           "every request timed and inside the idle stretch; reads with no token, every request under TZ-27's agent")
        # 2. a second run with no closed window left: empty
        env.clock += 300
        rc2 = run(env)
        ok(rc2 == 0 and evs(env)[-2:] == ["start", "empty"], "a run with nothing closed records empty and exits 0")
        # 3. a refused credential defers, and the next run resumes the same set
        env3 = world("defer", T + 86400 + 3600 + 588)
        closed(env3.root, T, [1000])
        env3.cred_ok = False
        rc3 = run(env3)
        a3 = Ledger(env3.state).recs[0]["run"]
        ok(rc3 == EXIT_DEFERRED and evs(env3) == ["start", "set", "deferred"]
           and os.path.exists(os.path.join(env3.root, str(T), "stream.jsonl.gz")),
           "a refused credential: deferred, exit 75, nothing removed")
        env3.cred_ok = True
        env3.clock += 86400
        rc3b = run(env3)
        led3 = Ledger(env3.state).recs
        ok(rc3b == 0 and [r["run"] for r in led3 if r["event"] == "start"] == [a3, a3]
           and events(led3, a3, "start")[1]["resumed"] is True and evs(env3)[-1] == "complete",
           "the next run resumes the deferred set and completes it")
        trs3 = jsonl_read(os.path.join(env3.state, "runs", str(a3), "transfers.jsonl"))
        ok(phase_of(trs3[0]["start_ns"] // 10 ** 9) == 15 and all(all(transfer_ok(t)) for t in trs3),
           "a request due at second 588 waits for the next idle stretch")
        # 4. three deferrals halt the archive; a halted archive refuses until a clear
        env4 = world("halt", T + 3 * 86400 + 3600 + 20)
        closed(env4.root, T, [1000])
        env4.cred_ok = False
        rcs = [run(env4) for _k in range(3)]
        ok(rcs == [EXIT_DEFERRED, EXIT_DEFERRED, 1] and evs(env4)[-2:] == ["halt", "timer-disabled"]
           and env4.disabled == 1, "the third deferral of one set halts, and the run disables its timer")
        env4.cred_ok = True
        ok(run(env4) == 1 and evs(env4)[-1] == "refused" and env4.disabled == 2
           and os.path.exists(os.path.join(env4.root, str(T), "stream.jsonl.gz")),
           "a halted archive refuses the next run, and removes nothing")
        jsonl_append(os.path.join(env4.state, "ledger.jsonl"), {"event": "clear", "run": None, "wall_ns": 0}, "x")
        env4.clock += 60
        ok(run(env4) == 0 and evs(env4)[-1] == "complete", "after a clear the next run takes a new set")
        # 5. a corrupted asset fails the verify: deferred, nothing removed; mended, the next run completes
        env5 = world("verify", T + 5 * 86400 + 3600 + 20)
        closed(env5.root, T, [5000, 6000])

        def corrupt(e):
            if e.on_sleep is corrupt:
                e.on_sleep = None
                k = sorted(Fake.assets)[-1]
                good = Fake.assets[k]["data"]
                Fake.assets[k]["data"] = good[:-1] + bytes([good[-1] ^ 1])
                corrupt.saved = (k, good)

        env5.on_sleep = corrupt
        rc5 = run(env5)
        ok(rc5 == EXIT_DEFERRED and evs(env5)[-1] == "deferred"
           and "VERIFY FAIL" in Ledger(env5.state).recs[-1]["reason"]
           and os.path.exists(os.path.join(env5.root, str(T), "stream.1.jsonl.gz")),
           "a flipped bit in one asset: VERIFY FAIL, deferred, nothing removed")
        k5, good5 = corrupt.saved
        Fake.assets[k5]["data"] = good5
        ok(run(env5) == 0 and evs(env5)[-1] == "complete", "the asset mended, the next run verifies and completes")
        # 6. a failure after the removal halts: the files archived, the timer disabled
        env6 = world("counter", T + 6 * 86400 + 3600 + 20)
        closed(env6.root, T, [2000])
        env6.skew = 1
        rc6 = run(env6)
        led6 = Ledger(env6.state).recs
        ok(rc6 == 1 and [r["event"] for r in led6][-3:] == ["kill", "halt", "timer-disabled"]
           and "G-COUNTER FAIL" in led6[-2]["reason"] and env6.disabled == 1
           and not os.path.exists(os.path.join(env6.root, str(T), "stream.jsonl.gz")),
           "G-COUNTER FAIL after the removal: halted, the files already archived, the timer disabled")
        # 7. a pair book that is not running is not restarted
        env7 = world("down", T + 7 * 86400 + 3600 + 20)
        closed(env7.root, T, [2000])
        env7.active = "failed"
        ok(run(env7) == 1 and env7.kills == 0 and "not restarted" in Ledger(env7.state).recs[-2]["reason"],
           "a pair book not active: the archive halts after its removal and signals nothing")
        ok(not [h for h in Fake.hits if h[3] not in (None, "Bearer " + tok)],
           "the loopback server saw no credential but the run's")
    finally:
        srv.shutdown()
        srv.server_close()
    shutil.rmtree(tmp)
    ok(not os.path.lexists(tmp), "the temporary stores removed")
    # this file's own syntax: its imports, and no endpoint of its own
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
        sys.exit("usage: tz28-pairbook-archive-timer.py MODE [ARG...]")
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
        elif mode == "first":
            assert not rest, "first takes no argument"
            rc = mode_first()
        else:
            table = {"fingerprint": mode_fingerprint, "selftest": mode_selftest, "tz27-release": mode_tz27_release,
                     "path": mode_path, "path-token": mode_path_token, "installed": mode_installed,
                     "timer": mode_timer, "final": mode_final, "still": tz27.mode_still, "started": tz27.mode_started}
            assert mode in table and not rest, "unknown mode %r" % (argv,)
            if mode in ("still", "started"):
                tz27.MODE[0] = "started" if mode == "started" else "still"
            table[mode]()
    out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
    out("opens refused: %d; store opens %d; requests %d, uploads %d, downloads %d (%d bytes); files removed %d" % (
        len(tz27.REFUSED), tz27.STORE_OPENS[0], tz27.COUNTERS["requests"], tz27.COUNTERS["uploads"],
        tz27.COUNTERS["downloads"], tz27.COUNTERS["download_bytes"], tz27.COUNTERS["removed"]))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
