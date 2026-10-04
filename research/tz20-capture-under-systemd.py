#!/usr/bin/env python3
"""TZ-20 - the capture under systemd: every check the TZ fixes, one mode per run.

    state            section 0.2   the host before anything is installed or started
    path-recorder    section 3.3   one live request per endpoint through the recorder's own functions
    path-chainbook   section 3.3   the same through the chain book's own http_get
    mark NAME        section 3.4   records an instant and both units' MainPID in instants.json
    unit N           G-UNIT        both units running from systemd, N restarts each
    start            G-START       the two new start records and the recorded gap
    cb               G-CB          the first two qualifying chain book windows
    rec              G-REC         the first six qualifying recorder intervals
    restart-cb       G-RESTART-C   one SIGTERM to the chain book, and systemd's restart
    restart-rec      G-RESTART-R   one SIGTERM to the recorder, and systemd's restart
    final            section 3.5   both units at the end of the session
    reclaim TREE...  section 9     copies into the forensic store what a committed report names by hash

Under the two capture roots it opens the two top-level runtime.jsonl files, the manifest.json of
G-REC's six intervals and the window.json of G-CB's two windows, read-only, and nothing else: an
audit hook refuses any other open there. It writes /root/tz20-work/instants.json, and in `reclaim`
new files under /root/btc-forensics/ by exclusive create; nothing else. It prints no price,
size, spread, mid, book level or outcome. Exit 0: every assert of the mode held. Exit 1: an assert
failed, and its message names it. Exit 3: NOT YET, with the instant to run the mode again.

Written for CryptoTZ/TZ-20-capture-under-systemd.md. The TZ is the specification.
"""

import hashlib
import json
import math
import os
import re
import subprocess
import sys
import time
import urllib.error

if not __debug__:
    sys.stderr.write("tz20: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

REC_UNIT = "btc-recorder.service"
CB_UNIT = "btc-chainbook.service"
REC_ARGV = ["/root/tz04a-env/venv/bin/python", "-B", "-u", "recorder.py"]
CB_FILE = "/root/tz18a-svc/tz18a-chainbook-capture.py"
CB_ARGV = ["/root/tz01-env/venv/bin/python", "-B", "-u", CB_FILE, "--serve"]
REC_CWD = "/root/btc-recorder-svc/research/recorder"
REC_ROOT = "/var/lib/btc-recorder"
REC_RUNTIME = REC_ROOT + "/runtime.jsonl"
REC_SERIES = REC_ROOT + "/btc-updown-5m"
CB_ROOT = "/var/lib/btc-chainbook"
CB_RUNTIME = CB_ROOT + "/runtime.jsonl"
INSTANTS = "/root/tz20-work/instants.json"
UNIT_DIR = "/etc/systemd/system"
FORENSICS = "/root/btc-forensics"
REPORTS = "/root/btc-5m-twap/CryptoReports"
RECLAIMABLE = ("/root/tz16a-work", "/root/tz19-work", "/root/tz20-work")
REC_MEMORY_MAX = 536870912      # MemoryMax=512M in btc-recorder.service
CB_MEMORY_MAX = 201326592       # MemoryMax=192M in btc-chainbook.service

SHA_RECORDER = "4216c04673ced76b5b2ac60ef57c9abedc46f9b9"
CB_COMMIT = "ca4bbc1dd583cbb62f3c0c985938d229b526ce7e"
CB_FILE_SHA = "e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae"
CB_HEADERS = [["Accept", "application/json"], ["User-Agent", "btc-5m-twap-tz18a"]]

# The state TZ-19's report read on 2026-10-03 (its sections 3.2 and 3.3).
OLD_REC_NEWLINES = 60690
OLD_REC_START_NS = 1789206785264516934
OLD_REC_LAST_NS = 1790940944342950552
OLD_CB_RECORDS = 4
OLD_CB_PID = 2699889
OLD_CB_STOP_NS = 1791017775066372007
# The old recorder's last frame lies after the window of 1790940900 opened and before the window
# of 1790941200 would have opened: that directory was never created.
GAP_LO_NS = 1790940810 * 10 ** 9
GAP_HI_NS = 1790941110 * 10 ** 9

REC_UNITS = 6
REC_COMPLETE_MIN = 4
REC_LEAD_S = 60
REC_DEADLINE_S = 3900
CB_UNITS = 2
CB_CHECKPOINTS = 7
CB_COMPLETE_MIN = 13
CB_LEAD_S = 60
CB_DEADLINE_S = 965
RESTART_GAP_NS = 60 * 10 ** 9
KILL_SLACK_NS = 5 * 10 ** 9

OPENS = []


def _allowed(path):
    """The only files this instrument opens under the two capture roots."""
    if path in (REC_RUNTIME, CB_RUNTIME):
        return True
    head, name = os.path.split(path)
    parent, interval = os.path.split(head)
    if name == "manifest.json" and parent == REC_SERIES and interval.isdigit():
        return True
    if name == "window.json" and parent == CB_ROOT and interval.isdigit():
        return True
    return False


def _audit(event, args):
    """V13 - under either capture root only the named files are opened, and only to read."""
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
                raise RuntimeError("V13: open refused under a capture root: %s %r" % (path, mode))
            OPENS.append(path)


sys.addaudithook(_audit)


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(seconds):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(seconds))


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def read_jsonl(path):
    """Every parseable record, the torn-line count, and the newline count, in file order."""
    with open(path, "rb") as fh:
        raw = fh.read()
    recs, torn = [], 0
    for line in raw.split(b"\n"):
        if not line.strip():
            continue
        try:
            recs.append(json.loads(line))
        except ValueError:
            torn += 1
    return recs, torn, raw.count(b"\n"), raw.endswith(b"\n")


def proc_argvs():
    found = {}
    for name in os.listdir("/proc"):
        if not name.isdigit():
            continue
        try:
            with open("/proc/%s/cmdline" % name, "rb") as fh:
                raw = fh.read()
        except OSError:
            continue
        fields = raw.split(b"\0")
        if fields and fields[-1] == b"":
            fields = fields[:-1]
        found[int(name)] = fields
    return found


def recorder_like(found):
    """tz10b.recorder_pids's rule: every process with an argument ending in recorder.py."""
    return sorted(p for p, a in found.items() if any(x.endswith(b"recorder.py") for x in a))


def chainbook_like(found):
    return sorted(p for p, a in found.items()
                  if any(x.endswith(b"tz18a-chainbook-capture.py") for x in a))


PROPS = ("ActiveState", "SubState", "UnitFileState", "FragmentPath", "ControlGroup",
         "MainPID", "NRestarts", "Result", "ExecMainStartTimestamp", "MemoryMax",
         "MemoryCurrent", "MemoryPeak")


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


def main_pid(unit):
    try:
        return int(show(unit).get("MainPID") or 0)
    except AssertionError:
        return 0


def check_unit(unit, argv, cwd, restarts, memory_max):
    """G-UNIT for one unit. Returns the MainPID. Memory in use is printed, not gated."""
    props = show(unit)
    out("U %s %s" % (unit, json.dumps(props, sort_keys=True)))
    assert props.get("ActiveState") == "active", "G-UNIT %s: ActiveState %r" % (
        unit, props.get("ActiveState"))
    assert props.get("SubState") == "running", "G-UNIT %s: SubState %r" % (
        unit, props.get("SubState"))
    assert props.get("UnitFileState") == "enabled", "G-UNIT %s: UnitFileState %r" % (
        unit, props.get("UnitFileState"))
    assert props.get("FragmentPath") == UNIT_DIR + "/" + unit, "G-UNIT %s: FragmentPath %r" % (
        unit, props.get("FragmentPath"))
    assert props.get("ControlGroup") == "/system.slice/" + unit, "G-UNIT %s: ControlGroup %r" % (
        unit, props.get("ControlGroup"))
    assert props.get("NRestarts") == str(restarts), "G-UNIT %s: NRestarts %r, expected %d" % (
        unit, props.get("NRestarts"), restarts)
    assert props.get("MemoryMax") == str(memory_max), "G-UNIT %s: MemoryMax %r, expected %d" % (
        unit, props.get("MemoryMax"), memory_max)
    pid = int(props.get("MainPID") or 0)
    assert pid > 0, "G-UNIT %s: no MainPID" % unit
    with open("/proc/%d/cmdline" % pid, "rb") as fh:
        fields = fh.read().split(b"\0")
    if fields and fields[-1] == b"":
        fields = fields[:-1]
    got = [f.decode("utf-8") for f in fields]
    assert got == argv, "G-UNIT %s: pid %d argv %r is not %r" % (unit, pid, got, argv)
    if cwd is not None:
        here = os.readlink("/proc/%d/cwd" % pid)
        assert here == cwd, "G-UNIT %s: pid %d cwd %r is not %r" % (unit, pid, here, cwd)
    with open("/proc/%d/cgroup" % pid) as fh:
        lines = fh.read().splitlines()
    paths = [line.split(":", 2)[2] for line in lines if line.count(":") >= 2]
    assert "/system.slice/" + unit in paths, "G-UNIT %s: pid %d cgroups %r" % (unit, pid, paths)
    assert not any(p.startswith("/user.slice") for p in paths), \
        "G-UNIT %s: pid %d is inside a user slice: %r" % (unit, pid, paths)
    out("G-UNIT %s: pid %d, argv equal, cgroup %s, NRestarts %d, MemoryMax %d; memory in use %s, "
        "peak %s (recorded)" % (unit, pid, "/system.slice/" + unit, restarts, memory_max,
                                props.get("MemoryCurrent"), props.get("MemoryPeak")))
    return pid


def check_both(restarts):
    rec_pid = check_unit(REC_UNIT, REC_ARGV, REC_CWD, restarts, REC_MEMORY_MAX)
    cb_pid = check_unit(CB_UNIT, CB_ARGV, None, restarts, CB_MEMORY_MAX)
    found = proc_argvs()
    assert recorder_like(found) == [rec_pid], "G-UNIT: recorder processes %r, expected [%d]" % (
        recorder_like(found), rec_pid)
    assert chainbook_like(found) == [cb_pid], "G-UNIT: chain book processes %r, expected [%d]" % (
        chainbook_like(found), cb_pid)
    out("G-UNIT PASS: 2 of 2 units, sole instances %d and %d, NRestarts %d each" % (
        rec_pid, cb_pid, restarts))
    return rec_pid, cb_pid


def load_marks():
    with open(INSTANTS, encoding="utf-8") as fh:
        return json.load(fh)


def mark_ns(marks, name):
    assert name in marks, "mark %r was never recorded" % name
    return marks[name]["ns"]


def not_yet(again_s, what):
    out("NOT YET: %s; run this mode again at or after %s" % (what, utc(again_s)))
    sys.exit(3)


# ---------------------------------------------------------------------------------------------

def mode_state():
    found = proc_argvs()
    rl, cl = recorder_like(found), chainbook_like(found)
    out("S1 processes with an argument ending in recorder.py: %r" % rl)
    out("S2 processes with an argument ending in tz18a-chainbook-capture.py: %r" % cl)
    assert rl == [], "S1: a recorder process runs: %r" % rl
    assert cl == [], "S2: a chain book process runs: %r" % cl

    recs, torn, newlines, terminated = read_jsonl(REC_RUNTIME)
    starts = [r for r in recs if r.get("kind") == "start"]
    stops = [r for r in recs if r.get("kind") == "stop"]
    out("S3 %s: %d newlines, %d records, %d torn, %d start, %d stop, ends with a newline %s"
        % (REC_RUNTIME, newlines, len(recs), torn, len(starts), len(stops), terminated))
    out("S3 newest start %s" % json.dumps(starts[-1], sort_keys=True))
    out("S3 last record %s" % json.dumps(recs[-1], sort_keys=True))
    assert newlines == OLD_REC_NEWLINES, "S3: %d newlines, TZ-19 read %d" % (
        newlines, OLD_REC_NEWLINES)
    assert terminated, "S3: the recorder's runtime.jsonl does not end with a newline"
    assert starts[-1].get("recv_ns") == OLD_REC_START_NS, "S3: newest start %r" % starts[-1]
    assert starts[-1].get("sha") == SHA_RECORDER, "S3: newest start sha %r" % starts[-1]
    assert recs[-1].get("recv_ns") == OLD_REC_LAST_NS, "S3: last record %r" % recs[-1]

    cbr, cb_torn, _n, cb_terminated = read_jsonl(CB_RUNTIME)
    for i, r in enumerate(cbr, 1):
        out("S4 %d %s pid %s wall_ns %s %s" % (i, r.get("event"), r.get("pid"), r.get("wall_ns"),
                                             utc(r.get("wall_ns", 0) / 1e9)))
    assert cb_torn == 0 and cb_terminated, "S4: chain book runtime.jsonl torn %d" % cb_torn
    assert len(cbr) == OLD_CB_RECORDS, "S4: %d records, TZ-19 read %d" % (len(cbr),
                                                                        OLD_CB_RECORDS)
    last = cbr[-1]
    assert last.get("event") == "stop" and last.get("pid") == OLD_CB_PID \
        and last.get("wall_ns") == OLD_CB_STOP_NS, "S4: last record %r" % last

    for path in (UNIT_DIR + "/" + REC_UNIT, UNIT_DIR + "/" + CB_UNIT, "/root/btc-recorder-svc"):
        assert not os.path.lexists(path), "S5: %s exists" % path
        out("S5 %s absent" % path)
    got = sha256_file(CB_FILE)
    assert got == CB_FILE_SHA, "S6: %s sha256 %s" % (CB_FILE, got)
    with open("/root/tz18a-svc/commit.txt", "rb") as fh:
        commit = fh.read()
    assert commit == (CB_COMMIT + "\n").encode("ascii"), "S6: commit.txt %r" % commit
    out("S6 %s sha256 %s, commit.txt %s" % (CB_FILE, got, CB_COMMIT))
    for path in (REC_ARGV[0], CB_ARGV[0]):
        assert os.access(path, os.X_OK), "S7: %s is not executable" % path
        out("S7 %s executable" % path)
    out("STATE PASS: S1 to S7")


def mode_path_recorder():
    import asyncio
    sys.path.insert(0, REC_CWD)
    import config
    import recorder
    import websockets

    src = os.path.realpath(recorder.__file__)
    assert src == os.path.join(REC_CWD, "recorder.py"), "P0: recorder loaded from %s" % src
    assert os.path.realpath(config.__file__) == os.path.join(REC_CWD, "config.py"), \
        "P0: config loaded from %s" % config.__file__
    sha = recorder.git_sha()
    assert sha == SHA_RECORDER, "P0: git_sha() %r" % sha
    out("P0 recorder.py %s, git_sha %s, websockets %s, User-Agent %r"
        % (src, sha, websockets.__version__, config.USER_AGENT))

    now = int(time.time())
    t0 = now - now % config.INTERVAL_S
    if now - t0 < 30:
        t0 -= config.INTERVAL_S              # an interval open for at least 30 s
    url = config.GAMMA_MARKET_BY_SLUG.format(slug=config.slug_for(t0))
    try:
        body = recorder.fetch(url)
    except urllib.error.HTTPError as exc:
        raise AssertionError("P1: %s answered HTTP %d" % (url, exc.code))
    doc = json.loads(body)
    market = doc[0] if isinstance(doc, list) else doc
    ids = json.loads(market["clobTokenIds"])
    assert isinstance(ids, list) and len(ids) == 2 and all(ids), "P1: clobTokenIds %r" % (ids,)
    out("P1 %s: served, %d bytes, JSON, token ids %s" % (url, len(body), ids))

    book = config.CLOB_BOOK_BY_TOKEN.format(token_id=ids[0])
    status, text = recorder.fetch_status(book, recorder.QUOTE_TIMEOUT_S)
    assert status == 200, "P2: %s status %r" % (book, status)
    json.loads(text)
    out("P2 %s: status %d, %d bytes, JSON" % (book, status, len(text.encode("utf-8"))))

    answered = 0
    for host in config.NTP_SERVERS:
        try:
            ip, offset, rtt, accepted, rejected = recorder.sntp_best(host)
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
        # recorder.py lines 531-533 and 538-539, verbatim in effect: the same subscription
        # message from config.TIER_A, the same URL and the same connect arguments.
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
    out("PATH-RECORDER PASS: P0 to P4")


def mode_path_chainbook():
    import importlib.util
    got = sha256_file(CB_FILE)
    assert got == CB_FILE_SHA, "P5: %s sha256 %s" % (CB_FILE, got)
    spec = importlib.util.spec_from_file_location("tz18a_chainbook", CB_FILE)
    cb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cb)
    assert list(cb.SERVICE_ARGV) == CB_ARGV, "P5: SERVICE_ARGV %r" % (cb.SERVICE_ARGV,)
    req = cb.build_request(cb.GAMMA_MARKET_URL.format(slug="x"))
    out("P5 %s sha256 %s; build_request headers %s" % (CB_FILE, got, sorted(req.header_items())))

    now = int(time.time())
    t15 = now - now % 900 if now % 900 >= 30 else now - now % 900 - 900
    t5 = now - now % 300 if now % 300 >= 30 else now - now % 300 - 300
    slugs = ["btc-updown-15m-%d" % t15, "btc-updown-5m-%d" % t5]
    ids_of = {}
    for i, slug in enumerate(slugs):
        if i:
            time.sleep(cb.DOC_GAP_S)
        res = cb.http_get(cb.GAMMA_MARKET_URL.format(slug=slug))
        assert res["status"] == 200 and res["bytes"] > 0, "P6: %s status %r bytes %r reason %r" % (
            slug, res["status"], res["bytes"], res["reason"])
        ids, _labels, _verbatim = cb.token_ids_of(res["raw"])
        assert ids is not None, "P6: %s carries no two token ids" % slug
        ids_of[slug] = ids
        out("P6 document %s: status %d, %d bytes, sha256 %s, token ids %s"
            % (slug, res["status"], res["bytes"], res["sha256"], ids))
    for slug in slugs:
        res = cb.http_get(cb.CLOB_BOOK_URL.format(token_id=ids_of[slug][0]))
        assert res["status"] == 200 and res["bytes"] > 0, "P7: %s status %r reason %r" % (
            slug, res["status"], res["reason"])
        json.loads(res["raw"])
        out("P7 /book %s token %s: status %d, %d bytes, JSON"
            % (slug, ids_of[slug][0], res["status"], res["bytes"]))
    assert cb.COUNTERS["requests"] == 4, "P7: %d requests" % cb.COUNTERS["requests"]
    out("PATH-CHAINBOOK PASS: P5 to P7, 4 requests")


def mode_mark(name):
    assert name in ("start-rec", "start-cb", "kill-cb", "kill-rec"), "mark %r" % name
    os.makedirs(os.path.dirname(INSTANTS), exist_ok=True)
    marks = load_marks() if os.path.exists(INSTANTS) else {}
    assert name not in marks, "mark %r already recorded" % name
    marks[name] = {"ns": time.time_ns(), "rec_pid": main_pid(REC_UNIT),
                   "cb_pid": main_pid(CB_UNIT)}
    tmp = INSTANTS + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(marks, sort_keys=True) + "\n")
    os.replace(tmp, INSTANTS)
    out("MARK %s %s (%s)" % (name, json.dumps(marks[name], sort_keys=True),
                             utc(marks[name]["ns"] / 1e9)))


def mode_unit(restarts):
    check_both(int(restarts))


def new_recorder_records(since_ns):
    recs, torn, _n, _t = read_jsonl(REC_RUNTIME)
    starts = sorted((r for r in recs if r.get("kind") == "start"
                     and r.get("recv_ns", 0) >= since_ns), key=lambda r: r["recv_ns"])
    ups = sorted((r for r in recs if r.get("kind") == "disconnect"
                  and r.get("reason") == "startup"
                  and r.get("detected_recv_ns", 0) >= since_ns),
                 key=lambda r: r["detected_recv_ns"])
    halts = [r for r in recs if r.get("kind") == "halt" and r.get("recv_ns", 0) >= since_ns]
    return starts, ups, halts, torn


def mode_start():
    marks = load_marks()
    s_rec, s_cb = mark_ns(marks, "start-rec"), mark_ns(marks, "start-cb")
    starts, ups, halts, torn = new_recorder_records(s_rec)
    for r in starts + ups + halts:
        out("R %s" % json.dumps(r, sort_keys=True))
    assert len(starts) == 1, "G-START recorder: %d start records since the mark" % len(starts)
    st = starts[0]
    assert st.get("sha") == SHA_RECORDER, "G-START recorder: sha %r" % st.get("sha")
    assert len(ups) == 1, "G-START recorder: %d startup gaps since the mark" % len(ups)
    up = ups[0]
    assert GAP_LO_NS <= up["start_recv_ns"] < GAP_HI_NS, \
        "G-START recorder: the gap starts at %d, outside [%d, %d)" % (
            up["start_recv_ns"], GAP_LO_NS, GAP_HI_NS)
    assert st["recv_ns"] <= up["detected_recv_ns"] <= up["end_recv_ns"], \
        "G-START recorder: gap %r against start %d" % (up, st["recv_ns"])
    assert not halts, "G-START recorder: halt records %r" % halts
    out("G-START recorder: start %s sha %s, free %s, captured %s; the gap %s to %s, %.1f s"
        % (utc(st["recv_ns"] / 1e9), st["sha"], st.get("free_bytes"), st.get("captured_bytes"),
           utc(up["start_recv_ns"] / 1e9), utc(up["end_recv_ns"] / 1e9),
           (up["end_recv_ns"] - up["start_recv_ns"]) / 1e9))

    cbr, cb_torn, _n, _t = read_jsonl(CB_RUNTIME)
    new = [r for r in cbr if isinstance(r.get("wall_ns"), int) and r["wall_ns"] >= s_cb]
    for r in new:
        out("C %s" % json.dumps({k: r.get(k) for k in ("event", "pid", "wall_ns", "commit",
                                                         "file_sha256", "argv")}, sort_keys=True))
    assert cb_torn == 0, "G-START chain book: %d torn lines" % cb_torn
    assert len(new) == 1 and new[0].get("event") == "start", \
        "G-START chain book: records since the mark %r" % [r.get("event") for r in new]
    st = new[0]
    pid = main_pid(CB_UNIT)
    assert st.get("pid") == pid, "G-START chain book: start pid %r, MainPID %d" % (st.get("pid"), pid)
    assert st.get("commit") == CB_COMMIT, "G-START chain book: commit %r" % st.get("commit")
    assert st.get("file_sha256") == CB_FILE_SHA, "G-START chain book: file %r" % st.get("file_sha256")
    assert st.get("argv") == [CB_FILE, "--serve"], "G-START chain book: argv %r" % st.get("argv")
    cfg = st.get("config") or {}
    assert cfg.get("headers") == CB_HEADERS, "G-START chain book: headers %r" % cfg.get("headers")
    assert cfg.get("service_argv") == CB_ARGV, "G-START chain book: %r" % cfg.get("service_argv")
    out("G-START chain book: start %s pid %d commit %s" % (utc(st["wall_ns"] / 1e9), pid, CB_COMMIT))
    out("G-START PASS: 2 of 2")


def mode_cb():
    marks = load_marks()
    s_cb = mark_ns(marks, "start-cb")
    cbr, _torn, _n, _t = read_jsonl(CB_RUNTIME)
    starts = [r for r in cbr if r.get("event") == "start"
              and isinstance(r.get("wall_ns"), int) and r["wall_ns"] >= s_cb]
    assert starts, "G-CB: no chain book start record since the mark"
    w0 = starts[0]["wall_ns"] / 1e9
    first = math.ceil((w0 + CB_LEAD_S - 625) / 900) * 900
    windows = [first + 900 * k for k in range(CB_UNITS)]
    paths = {t: "%s/%d/window.json" % (CB_ROOT, t) for t in windows}
    missing = [t for t in windows if not os.path.exists(paths[t])]
    if missing and time.time() < max(t + CB_DEADLINE_S for t in missing):
        not_yet(time.time() + 300, "windows %s pending, the last deadline %s"
                % (missing, utc(max(t + CB_DEADLINE_S for t in missing))))
    complete = docs = clean = present = 0
    for t in windows:
        if t in missing:
            out("G-CB window %d %s: no window.json by %s" % (t, utc(t), utc(t + CB_DEADLINE_S)))
            continue
        with open(paths[t], encoding="utf-8") as fh:
            wj = json.loads(fh.read())
        assert wj.get("T") == t, "G-CB: %s carries T %r" % (paths[t], wj.get("T"))
        present += 1
        complete += int(wj.get("checkpoints_complete") or 0)
        docs += 1 if wj.get("documents_ok") is True else 0
        clean += 1 if wj.get("missed") == 0 else 0
        out("G-CB window %d %s: documents_ok %s, checkpoints_complete %s of %d, missed %s, "
            "status_counts %s" % (t, utc(t), wj.get("documents_ok"), wj.get("checkpoints_complete"),
                                  CB_CHECKPOINTS, wj.get("missed"),
                                  json.dumps(wj.get("status_counts"), sort_keys=True)))
    ok = (present == CB_UNITS and docs == CB_UNITS and clean == CB_UNITS
          and complete >= CB_COMPLETE_MIN)
    out("G-CB %s: windows %d of %d, documents_ok %d of %d, missed 0 at %d of %d, "
        "checkpoints complete %d of %d, PASS at %d or more"
        % ("PASS" if ok else "FAIL", present, CB_UNITS, docs, CB_UNITS, clean, CB_UNITS,
           complete, CB_UNITS * CB_CHECKPOINTS, CB_COMPLETE_MIN))
    assert ok, "G-CB FAIL"


def mode_rec():
    marks = load_marks()
    s_rec = mark_ns(marks, "start-rec")
    starts, _ups, _halts, _torn = new_recorder_records(s_rec)
    assert starts, "G-REC: no recorder start record since the mark"
    r0 = starts[0]["recv_ns"] / 1e9
    first = math.ceil((r0 + REC_LEAD_S + 90) / 300) * 300
    members = [first + 300 * k for k in range(REC_UNITS)]
    paths = {t: "%s/%d/manifest.json" % (REC_SERIES, t) for t in members}
    missing = [t for t in members if not os.path.exists(paths[t])]
    if missing and time.time() < max(t + REC_DEADLINE_S for t in missing):
        not_yet(time.time() + 300, "intervals %s pending, the last deadline %s"
                % (missing, utc(max(t + REC_DEADLINE_S for t in missing))))
    present = complete = quotes = shas = 0
    for t in members:
        if t in missing:
            out("G-REC interval %d %s: no manifest by %s" % (t, utc(t), utc(t + REC_DEADLINE_S)))
            continue
        with open(paths[t], encoding="utf-8") as fh:
            m = json.loads(fh.read())
        assert m.get("T0_epoch") == t, "G-REC: %s carries T0_epoch %r" % (paths[t],
                                                                         m.get("T0_epoch"))
        present += 1
        complete += 1 if m.get("complete") is True else 0
        quotes += 1 if m.get("quotes_complete") is True else 0
        shas += 1 if m.get("recorder_git_sha") == SHA_RECORDER else 0
        out("G-REC interval %d %s: complete %s, quotes_complete %s, disconnects %s, "
            "gamma_present %s, resolution_present %s, clock |offset| max %s ms, sha %s"
            % (t, utc(t), m.get("complete"), m.get("quotes_complete"), m.get("disconnect_count"),
               m.get("gamma_present"), m.get("resolution_present"),
               m.get("clock_offset_abs_max_ms"), m.get("recorder_git_sha")))
    ok = (present == REC_UNITS and quotes == REC_UNITS and shas == REC_UNITS
          and complete >= REC_COMPLETE_MIN)
    out("G-REC %s: manifests %d of %d, quotes_complete %d of %d, sha %d of %d, "
        "complete %d of %d, PASS at %d or more"
        % ("PASS" if ok else "FAIL", present, REC_UNITS, quotes, REC_UNITS, shas, REC_UNITS,
           complete, REC_UNITS, REC_COMPLETE_MIN))
    assert ok, "G-REC FAIL"


def mode_restart_cb():
    marks = load_marks()
    s_cb, k = mark_ns(marks, "start-cb"), mark_ns(marks, "kill-cb")
    old_pid = marks["kill-cb"]["cb_pid"]
    cbr, torn, _n, _t = read_jsonl(CB_RUNTIME)
    new = [r for r in cbr if isinstance(r.get("wall_ns"), int) and r["wall_ns"] >= s_cb]
    events = [(r.get("event"), r.get("pid"), r.get("wall_ns")) for r in new]
    out("G-RESTART-C records since start-cb: %s" % events)
    assert torn == 0, "G-RESTART-C: %d torn lines" % torn
    assert [e[0] for e in events] == ["start", "stop", "start"], "G-RESTART-C: %r" % events
    a, b, c = new
    assert a.get("pid") == b.get("pid") == old_pid, "G-RESTART-C: killed pid %r" % old_pid
    assert c.get("pid") != old_pid, "G-RESTART-C: the same pid restarted"
    assert b["wall_ns"] >= k, "G-RESTART-C: stop record before the mark"
    gap = c["wall_ns"] - b["wall_ns"]
    assert 0 <= gap <= RESTART_GAP_NS, "G-RESTART-C: %d ns between stop and start" % gap
    assert c.get("commit") == CB_COMMIT and c.get("file_sha256") == CB_FILE_SHA, \
        "G-RESTART-C: the restarted start record %r" % c
    pid = check_unit(CB_UNIT, CB_ARGV, None, 1, CB_MEMORY_MAX)
    assert c.get("pid") == pid, "G-RESTART-C: start pid %r, MainPID %d" % (c.get("pid"), pid)
    out("G-RESTART-C PASS: stop of %d at %s with counters %s; start of %d %.1f s later"
        % (old_pid, utc(b["wall_ns"] / 1e9), json.dumps(b.get("counters"), sort_keys=True),
           pid, gap / 1e9))


def mode_restart_rec():
    marks = load_marks()
    s_rec, k = mark_ns(marks, "start-rec"), mark_ns(marks, "kill-rec")
    old_pid = marks["kill-rec"]["rec_pid"]
    starts, ups, halts, torn = new_recorder_records(s_rec)
    for r in starts + ups:
        out("R %s" % json.dumps(r, sort_keys=True))
    assert len(starts) == 2, "G-RESTART-R: %d start records since start-rec" % len(starts)
    second = starts[1]
    assert second["recv_ns"] >= k, "G-RESTART-R: the second start precedes the mark"
    assert second.get("sha") == SHA_RECORDER, "G-RESTART-R: sha %r" % second.get("sha")
    assert len(ups) == 2, "G-RESTART-R: %d startup gaps since start-rec" % len(ups)
    up = ups[1]
    assert k - KILL_SLACK_NS <= up["start_recv_ns"] <= second["recv_ns"], \
        "G-RESTART-R: the gap starts at %d, mark %d, start %d" % (up["start_recv_ns"], k,
                                                                 second["recv_ns"])
    gap = up["end_recv_ns"] - up["start_recv_ns"]
    assert 0 <= gap <= RESTART_GAP_NS, "G-RESTART-R: the gap is %d ns" % gap
    assert not halts, "G-RESTART-R: halt records %r" % halts
    pid = check_unit(REC_UNIT, REC_ARGV, REC_CWD, 1, REC_MEMORY_MAX)
    assert pid != old_pid, "G-RESTART-R: the same pid %d" % pid
    out("G-RESTART-R PASS: pid %d replaced by %d; the gap %s to %s, %.1f s, recorded"
        % (old_pid, pid, utc(up["start_recv_ns"] / 1e9), utc(up["end_recv_ns"] / 1e9), gap / 1e9))


def mode_final():
    rec_pid, cb_pid = check_both(1)
    marks = load_marks()
    s_rec, s_cb = mark_ns(marks, "start-rec"), mark_ns(marks, "start-cb")
    recs, torn, newlines, _t = read_jsonl(REC_RUNTIME)
    kinds = {}
    for r in recs:
        if r.get("recv_ns", r.get("detected_recv_ns", 0)) >= s_rec:
            kinds[r.get("kind")] = kinds.get(r.get("kind"), 0) + 1
    starts = [r for r in recs if r.get("kind") == "start"]
    assert starts[-1].get("sha") == SHA_RECORDER, "FINAL: newest start sha %r" % starts[-1]
    cbr, cb_torn, _n2, _t2 = read_jsonl(CB_RUNTIME)
    events = [r.get("event") for r in cbr if isinstance(r.get("wall_ns"), int)
              and r["wall_ns"] >= s_cb]
    out("FINAL recorder runtime.jsonl: %d newlines, %d torn; since start-rec %s"
        % (newlines, torn, json.dumps(kinds, sort_keys=True)))
    out("FINAL chain book runtime.jsonl: %d records, %d torn; since start-cb %s"
        % (len(cbr), cb_torn, events))
    out("FINAL PASS: recorder pid %d, chain book pid %d, newest recorder start sha %s"
        % (rec_pid, cb_pid, SHA_RECORDER))


TOKEN = re.compile(r"(?<![0-9a-f])[0-9a-f]{16,64}(?![0-9a-f])")


def report_tokens():
    """Every run of 16 to 64 lowercase hex characters in a committed report."""
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    """Files kept whatever the reports print: TZ-16a's label ledger, and this TZ's own record."""
    if tree == "/root/tz16a-work":
        return rel == "label-ledger.jsonl"
    if tree == "/root/tz20-work":
        return rel == "instants.json" or rel.startswith("logs/")
    return False


def mode_reclaim(trees):
    assert trees and all(t in RECLAIMABLE for t in trees), "reclaim: %r" % (trees,)
    tokens = report_tokens()
    lengths = sorted({len(t) for t in tokens})
    before = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    out("reclaim: %d report tokens; forensic store holds %d files" % (len(tokens), before))
    considered = named = kept = copied = held = 0
    for tree in trees:
        if not os.path.isdir(tree):
            out("reclaim %s: absent" % tree)
            continue
        for dirpath, dirnames, filenames in os.walk(tree):
            dirnames.sort()
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
                with open(path, "rb") as fh:
                    data = fh.read()
                with open(dest, "xb") as fh:
                    fh.write(data)
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
        sys.exit("usage: tz20-capture-under-systemd.py MODE [ARG]")
    mode, rest = argv[0], argv[1:]
    table = {
        "state": mode_state, "path-recorder": mode_path_recorder,
        "path-chainbook": mode_path_chainbook, "start": mode_start, "cb": mode_cb,
        "rec": mode_rec, "restart-cb": mode_restart_cb, "restart-rec": mode_restart_rec,
        "final": mode_final,
    }
    if mode == "mark":
        assert len(rest) == 1, "mark NAME"
        mode_mark(rest[0])
    elif mode == "unit":
        assert len(rest) == 1, "unit N"
        mode_unit(rest[0])
    elif mode == "reclaim":
        mode_reclaim(rest)
    else:
        assert mode in table and not rest, "unknown mode %r" % (argv,)
        table[mode]()
    out("opens under the capture roots: %d" % len(OPENS))


if __name__ == "__main__":
    main(sys.argv[1:])
