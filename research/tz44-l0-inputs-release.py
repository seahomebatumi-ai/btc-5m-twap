#!/usr/bin/env python3
"""TZ-44 - L0's inputs off the host: one Release of the reward book's days before the reserve - every file of a day's
directory but its streams: its selections with their replies, its slot records and its reward polls - and of the 34
files of TZ-43's fetch/ and days/, its set.json and its reading.json, as the forensic store holds them.

    fingerprint       contract section 1 steps 3 and 4, asserted: the map's revision, anchors and rows
    number            CANON hard rule 2: no other TZ-44 specification or report on origin/main
    selftest          every rule of this file, on literals, on temporary trees and on a loopback GitHub
    still             the four units' MainPID, NRestarts and ActiveState: the first run records them, the second
                      compares, the pair book archive's own restarts read from its ledger (G-STILL)
    scratch OWN       the UUID directories beside OWN, this session's, each named live or earlier
    pack              G-SOURCE - TZ-43's 34 files by the bytes and SHA-256 its report names - then G-PACK: one tar a
                      day of the store's day directory but its streams and but every file of stored replies that
                      carries a body the venue did not serve as JSON under status 200; the manifest and the set; a
                      second run asserts every output unchanged (DETERMINISM)
    upload            B-UPLOAD, the Boss's block: the Release on tz-44-l0-inputs at this file's commit, and the set's
                      assets, through TZ-27's own client, every request held
    verify            G-TAG, G-UPLOAD and G-DOWNLOAD, with no token: the tag on origin, the API's record of every
                      asset and a full download of each
    geoblock          the venue's own reading of the host's address, printed: blocked, country, region - never the
                      address
    reclaim TREE...   section 9

It loads TZ-27's instrument, research/tz27-pairbook-archive.py, from beside itself by its SHA-256, and sends every
GitHub request through TZ-27's client - build_request, GitHub, upload_set, verify_release, credential - each one held
to the pair book's idle stretch and away from both archives' runs. TZ-27's audit hook is installed then; this file's
own refuses every open, listing, request and process TZ-44 section 2 does not give the running mode: under
/var/lib/btc-rewardbook/ it lets pack list the twelve day directories and read their selections, slot records and
reward polls, and nothing else - no stream file, no day from 2026-11-09, no file of the store's root. It writes under
/root/tz44-work/ and, in reclaim, new files in /root/btc-forensics/ by exclusive create. It prints names, counts,
bytes and hashes, never a file's content. An error page can carry the address it was served to, so a file of stored
replies is published only where every body in it is a JSON document the venue served under status 200. Exit 0: every
assert of the mode held. Exit 1: an assert failed, and its message names it. Run it with the recorder's interpreter,
/root/tz04a-env.

Written for CryptoTZ/TZ-44-l0-inputs-release.md. The TZ is the specification.
"""

import collections
import ctypes
import datetime
import gzip
import hashlib
import json
import os
import re
import resource
import shutil
import socket
import stat
import subprocess
import sys
import tarfile
import time
import types
import urllib.error
import urllib.parse
import urllib.request
import zlib

if not __debug__:
    sys.stderr.write("tz44: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)


def _malloc_tune():
    """glibc's mmap threshold at 128 KiB and two arenas, as TZ-23's, TZ-33's and TZ-43's instruments fix them."""
    try:
        libc = ctypes.CDLL("libc.so.6")
        return libc.mallopt(-3, 131072) == 1 and libc.mallopt(-8, 2) == 1
    except OSError:
        return False


MALLOC_TUNED = _malloc_tune()
HERE = os.path.dirname(os.path.abspath(__file__))

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------------

MAP_REVISION = "2026-11-12-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "437b45ea196b", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 59, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"(?:`([0-9a-f]{64})`|[^|]*) \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)
NUMBER = "TZ-44-"
OWN_TZ = "CryptoTZ/TZ-44-l0-inputs-release.md"

DAY = 86400
SLOT = 900
FIRST_D0 = 1793145600        # 2026-10-28 00:00:00 UTC: the reward book's first day (TZ-33)
LAST_D0 = 1794096000         # 2026-11-08 00:00:00 UTC: the last day before the reserve
RESERVE_D0 = 1794182400      # 2026-11-09 00:00:00 UTC: every day from it is reserved for L0's next gate
DAYS = tuple(range(FIRST_D0, LAST_D0 + DAY, DAY))
MEMBER_KINDS = ("select", "slot", "rewards")
KINDS = ("select", "slot", "rewards", "stream", "other")
DAY_MAX_BYTES = 200000000    # a day's members above this BLOCK: twelve times TZ-33's 16.3 MB a day
UNIT_BUDGET_S = 60           # the 34 sources, one unit of pack, are held for this many seconds
UNIT_BASE_S = 30             # a day, one unit of pack, is held for this many seconds and for its members' bytes at
SCAN_RATE = 500000           # this many stored bytes a second: its scan of the replies, its archive and its hashes
SCANNED = ".jsonl.gz"        # a member of stored replies: scanned, and published only where no line withholds it
RATE_FLOOR = 2000000         # bytes a second a transfer is budgeted at, TZ-28's
MARGIN_S = 5                 # seconds every request is budgeted beyond its bytes, TZ-28's
IDLE = (15, 590)             # the pair book's idle stretch: a unit starts at second 15 or later, ends by 590
CALENDAR = ((5420, "the reward book archive's calendar run at 01:30:20 UTC"),
            (10820, "the pair book archive's calendar run at 03:00:20 UTC"))
CALENDAR_LEAD_S = 60
RUNNING = ("active", "activating", "deactivating", "reloading", "refreshing")
HOLD_MAX_S = 7200
MEM_FLOOR = 98319394         # MemAvailable: twice the host peak modelled for the Architect's bound on any mode's
#                              peak, 41,000,000, at the ratio TZ-37 measured, 58,953,728 / 49,168,384 (section 0.4)
MEM_RETRY_S = 60             # a MemAvailable read below the floor is read again this much later,
MEM_READS = 5                # five reads at most
DISK_FLOOR = 7400000000      # free bytes on /dev/vda2 once a day's archive is written: the reward book's
#                              STREAM_FLOOR, 7,300,000,000, and one slot of its streams at the cut, 100,000,000
DISK_GATE = 7800000000       # free bytes at a mode's start: DISK_FLOOR and 400,000,000 for what this session may
#                              still write then, its archives and their copies (section 0.4)

TAG = "tz-44-l0-inputs"
MANIFEST = "tz44-manifest.json"
ARCHIVE_FMT = "rewardbook-inputs-%d.tar"
UA = "btc-5m-twap-tz44"
GEO_URL = "https://polymarket.com/api/geoblock"
GEO_HOST = "polymarket.com"
GEO_HEADERS = {"User-Agent": UA, "Accept": "application/json"}
GEO_TIMEOUT_S = 30
GEO_READ_MAX = 65536
CONTENT_TYPE = "application/octet-stream"

# TZ-43's work files, as its report's section 2.6 names them: path in its tree, bytes, SHA-256
TZ43_REPORT = "CryptoReports/TZ-43-l0-our-quote-report.md"
TZ43_MEMBERS = (1793404800, 1793491200, 1793577600, 1793664000, 1793750400, 1793836800, 1794009600, 1794096000)
TZ43_FILES = (
    ("fetch/1793404800.json", 55310, "5f56487e44aadcba1df2bc1316a889605baf83a4fcafc965b5ee4a18a6fec9b2"),
    ("fetch/1793404800.polls.jsonl", 4990923, "53ae4e79d354b3f8b35d497654159162b9c2290deb0d69b6f62b79c3fe8c1d71"),
    ("fetch/1793491200.json", 55330, "55f95448c4ba6abe1d1b154ff0e014ef190ffb7be861a7f6cb1a3bcddec7a1bd"),
    ("fetch/1793491200.polls.jsonl", 5010687, "1aac9148f26b55664b248be60b62394defc1b117b63bcd952c632bf96b3ebf54"),
    ("fetch/1793577600.json", 55447, "8589729bfe267feb57208833064bc71006e592e22edd8290d70bbc2b4474d9b5"),
    ("fetch/1793577600.polls.jsonl", 5027379, "19d765c78c93e9d4175328615ae3dc27b3e2f0c1dd7f6084eeab672a9e56427c"),
    ("fetch/1793664000.json", 55449, "1405b48ac2459f052b5b36dea8e85dd6cb0e112b49ac21030955d96f890eec02"),
    ("fetch/1793664000.polls.jsonl", 5014920, "4a5ef449ed6b1d2bf1378b817671b9bb3cac477c5a9fa6e5068d9673b24977cb"),
    ("fetch/1793750400.json", 55543, "1ed8768bd80b54220c0437e15fc424943a8829b716d7ba70f2b586f5ae14099c"),
    ("fetch/1793750400.polls.jsonl", 4967708, "f06145aa32845b9f3a65b8616e5842218b03869a3fc18d5a4bf1aaaa57fec920"),
    ("fetch/1793836800.json", 55625, "7d502a56ad2a4a3f95150bbcfc8c52c1190f2b977d9d1a72e2e1c4b3c2f5ba25"),
    ("fetch/1793836800.polls.jsonl", 5055307, "7918f3b6629489fcff4fd22cdb049a89e1e1ef63b86738c73ec680e17e5eff5d"),
    ("fetch/1794009600.json", 55639, "29e17ecde5f5d705e297bdc2be7e5e150aa50d06c3ac66ba9b1c4c13225b5708"),
    ("fetch/1794009600.polls.jsonl", 5037697, "91582ccfb9145559277d196f61e804e6be205d0b18d6168a1db6975711d6cf15"),
    ("fetch/1794096000.json", 55660, "a3ebc56744facb5c00f862c1f5d70a564672b68b5cc276398f32ae7f1bc0c552"),
    ("fetch/1794096000.polls.jsonl", 5047340, "7b0d86338359fbb4d5f4f7b54c6f36e0d45f2ed5c4d6d5731358c8e4e3099a82"),
    ("days/1793404800.json", 145864, "d93f998fba7795f30379c06e2058c55f4eba9d0c340536a3d5a4d1636b765ee6"),
    ("days/1793404800.slots.txt", 47260, "ec4494031d22891f22ec2822287c0127c4f96f39dac1337f3980419813052400"),
    ("days/1793491200.json", 147006, "50e19969a8196ef3fe8b069056b75bb3ff5f5ba1c41a9ad70a48bd7e88ebaaae"),
    ("days/1793491200.slots.txt", 47077, "5a7169dbcdb3186b588e2bd77ef5017dc792f1ead7cc8d2b9c11a55cee90f763"),
    ("days/1793577600.json", 146744, "93c76d1594b1edef03e192c02cc67b0264e43ca4b77b6d49939845f5876dc57c"),
    ("days/1793577600.slots.txt", 46799, "aae9a59997c591b90672bec21ea2489e2f7e654eba03590bc8d1ff411a186e1c"),
    ("days/1793664000.json", 147691, "a80c3d721fce47537ff927c42b989cd4409d25b7c3a1e2c4e024a2463d48c54d"),
    ("days/1793664000.slots.txt", 46785, "dc9dff0e13153ee045ada2cb805c9567ce9bb4b490f88c40aa0821442fe8660b"),
    ("days/1793750400.json", 155059, "4f9ca91d2798fb9f7b496e98baa02d4fe9f6efb5f60f979540f682fb7fdadfa9"),
    ("days/1793750400.slots.txt", 47105, "71101c5d670141ce064c671824d5c8c8c1615ffce4801b1a422baa3df4281cdc"),
    ("days/1793836800.json", 149722, "e7266b1d2d05e1191095e9cd184e6bb15571ea7380fa1e4f51db90a5342e200d"),
    ("days/1793836800.slots.txt", 46750, "ec5792be99ff4169b4574b3a8ce04855ad7a5fcd51aba1b51baf4cc9d8ce44e5"),
    ("days/1794009600.json", 146104, "f3018bb242bff3b1d7483622cd4065074cc42faa90b1e8357d223c2796a6dfd5"),
    ("days/1794009600.slots.txt", 46914, "a0fdb71edc318fb7e41989c1aca3b591c9b3e4db39274e87588354639725c1e6"),
    ("days/1794096000.json", 144626, "910ed69e85ab28dc81a334538d229a66ba17107260325c1afe5eae95de02e91f"),
    ("days/1794096000.slots.txt", 46970, "00caaab0888d85779398751281da3e9219cfdf9742c77b5914499cf0c4421436"),
    ("reading.json", 9377, "175d366101cd825437a1cd393aa57642965f7ffb9fe831746c2d9b2187d50be1"),
    ("set.json", 6175, "904f1b9b8244a15fe48549e39ffc879f68ad31de6963a41c05f5afc607edf0f7"),
)

UPLOAD_ROOT = "/root"
WORK = UPLOAD_ROOT + "/tz44-work"
WT = WORK + "/wt"
OUT = WORK + "/out"
STATE = WORK + "/state.json"
SET_FILE = WORK + "/set.json"
UPLOAD_LOG = WORK + "/upload.jsonl"
TRANSFERS = WORK + "/transfers.jsonl"
VERIFY_FILE = WORK + "/verify.json"
PRIMARY = "/root/btc-5m-twap"
REPORTS = PRIMARY + "/CryptoReports"
FORENSICS = UPLOAD_ROOT + "/btc-forensics"
BRANCH = "tz-44-l0-inputs-release"
RB_ROOT = "/var/lib/btc-rewardbook"
RB_ARCHIVE = "/var/lib/btc-rewardbook-archive"
PB_ARCHIVE = "/var/lib/btc-pairbook-archive"
PB_LEDGER = PB_ARCHIVE + "/ledger.jsonl"
RECORDER = "/var/lib/btc-recorder"
PAIRBOOK = "/var/lib/btc-pairbook"
CHAINBOOK = "/var/lib/btc-chainbook"
ADVISOR = "/var/lib/adv3-bot"
ADVISOR_ETC = "/etc/adv3-bot"
UNITS = {"recorder": "btc-recorder.service", "pairbook": "btc-pairbook.service", "rewardbook": "btc-rewardbook.service",
         "advisor": "adv3-bot.service"}
ARCHIVES = {"pairbook": ("btc-pairbook-archive.service", "btc-pairbook-archive.timer"),
            "rewardbook": ("btc-rewardbook-archive.service", "btc-rewardbook-archive.timer")}
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TOKEN = re.compile(r"[0-9a-f]{16,64}")
SHA_RE = re.compile(r"[0-9a-f]{64}")
SHA40 = re.compile(r"[0-9a-f]{40}")
SLOT_FILE_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.(stream\.jsonl\.gz|rewards\.jsonl\.gz|slot\.json)")
SELECT_FILE_RE = re.compile(r"select\.([0-9]+)\.(json|replies\.jsonl\.gz)")
LIVE_S = 60
PYFILE = "tz44-l0-inputs-release.py"
TZ27_NAME = "tz27-pairbook-archive.py"
TZ27_SHA256 = "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673"

# ---- the audit hook: TZ-44 section 2's reads, writes, requests and processes -----------------------------

MODE = [None]
REFUSED = []
COUNTS = collections.Counter()
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
RB_DAY = re.compile(re.escape(RB_ROOT) + r"/([0-9]{10})")
RB_FILE = re.compile(re.escape(RB_ROOT) + r"/([0-9]{10})/([0-9]{10}\.[0-9]+\.(?:slot\.json|rewards\.jsonl\.gz)|"
                     r"select\.[0-9]+\.(?:json|replies\.jsonl\.gz))")
HOSTS = {"upload": ("api.github.com", "uploads.github.com"),
         "verify": ("api.github.com", "github.com", "release-assets.githubusercontent.com",
                    "objects.githubusercontent.com"),
         "geoblock": (GEO_HOST,),
         "selftest": ("127.0.0.1",)}
PROCESSES = {"git", "systemctl", "stat"}
UPLOAD_PROCESSES = {"gh"}
CLOSED = (RECORDER, CHAINBOOK, PAIRBOOK, ADVISOR, ADVISOR_ETC, RB_ARCHIVE)


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
    """None where TZ-44 section 2 allows the event in this mode; otherwise the reason it is refused. Pure."""
    if event == "urllib.Request":
        host = urllib.parse.urlsplit(args[0]).hostname if args and isinstance(args[0], str) else None
        return None if host in HOSTS.get(mode, ()) else "a request to %s" % host
    if event == "subprocess.Popen":
        exe = args[0] if args and args[0] else (args[1][0] if len(args) > 1 and args[1] else "")
        exe = os.path.basename(os.fsdecode(exe) if isinstance(exe, bytes) else str(exe))
        if exe in PROCESSES or (mode == "upload" and exe in UPLOAD_PROCESSES):
            return None
        return "a process %s" % exe
    p = _path(args[0]) if args else None
    if p is None:
        return None
    if event in ("os.listdir", "os.scandir"):
        if any(_under(p, r) for r in CLOSED + (PB_ARCHIVE,)):
            return "a listing under a capture root, the advisor's or an archive's state"
        if _under(p, RB_ROOT):
            m = RB_DAY.fullmatch(p)
            if mode == "pack" and m is not None and int(m.group(1)) in DAYS:
                return None
            return "a listing under the reward book's root"
        return None
    wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
    w = _writing(wm, fl)
    if any(_under(p, r) for r in CLOSED):
        return "an open under a capture root, the advisor's or the reward book archive's state"
    if _under(p, RB_ROOT):
        m = RB_FILE.fullmatch(p)
        if not w and mode == "pack" and m is not None and int(m.group(1)) in DAYS:
            return None
        return "an open under the reward book's root"
    if _under(p, PB_ARCHIVE):
        if not w and mode == "still" and p == PB_LEDGER:
            return None
        return "an open under the pair book archive's state"
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
    if event in ("open", "os.listdir", "os.scandir") and _under(_path(args[0]) or "", RB_ROOT):
        COUNTS["reward book opens" if event == "open" else "reward book listings"] += 1


sys.addaudithook(_audit)


def load_tz27(path):
    """TZ-27's instrument, executed from the very bytes whose SHA-256 is asserted; its own audit hook is installed
    then, and governs this process beside this file's."""
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
tz27.WORK[0] = WORK                  # TZ-27's hook: every write and change inside this TZ's work tree
tz27.CONTENT_TYPE = CONTENT_TYPE     # TZ-27's upload reads it at each call: no asset is labelled gzip
assert tz27.REPO == "seahomebatumi-ai/btc-5m-twap" and tz27.UPLOAD_SETTLE_S == 120, "TZ-27's constants"

# ---- small helpers ----------------------------------------------------------------------------------------


def out(msg):
    sys.stdout.write("[%s] %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stdout.flush()


def utc(t):
    return datetime.datetime.fromtimestamp(float(t), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


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
        out("unchanged %s %d bytes sha256 %s" % (path, len(data), got))
        return "unchanged"
    write_atomic(path, data)
    out("wrote %s %d bytes sha256 %s" % (path, len(data), sha256_bytes(data)))
    return "wrote"


def load_state():
    if not os.path.exists(STATE):
        return {}
    with open(STATE, encoding="utf-8") as fh:
        return json.load(fh)


def save_state(st):
    write_atomic(STATE, (json.dumps(st, sort_keys=True, indent=1) + "\n").encode("utf-8"))


def jsonl_append(path, rec):
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, sort_keys=True) + "\n")


def jsonl_read(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return [json.loads(ln) for ln in fh if ln.strip()]


def mem_available():
    with open("/proc/meminfo", encoding="ascii") as fh:
        for ln in fh:
            if ln.startswith("MemAvailable:"):
                return int(ln.split()[1]) * 1024
    raise AssertionError("no MemAvailable in /proc/meminfo")


def free_bytes(path="/var/lib"):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def memory_gate(reads):
    """MemAvailable at a mode's reads, in order: the first, and one every MEM_RETRY_S after it while every read before
    fell below MEM_FLOOR, MEM_READS at most (map section 7 item 137). The last decides: (passes, it). Pure."""
    assert 1 <= len(reads) <= MEM_READS and all(r < MEM_FLOOR for r in reads[:-1]), reads
    return reads[-1] >= MEM_FLOOR, reads[-1]


def floor_check(read=None, sleep=None, freef=None):
    """Before a mode that reads the store, the forensic store or the network: glibc's two settings, the memory floor -
    a read below it read again every MEM_RETRY_S, MEM_READS reads at most, the last deciding - and the disk gate."""
    read, sleep, freef = read or mem_available, sleep or time.sleep, freef or free_bytes
    assert MALLOC_TUNED, "BLOCKED: glibc did not take the mmap threshold and the arena count"
    reads, free = [read()], freef()
    out("MemAvailable %d bytes, floor %d; free %d bytes, floor %d" % (reads[0], MEM_FLOOR, free, DISK_GATE))
    while reads[-1] < MEM_FLOOR and len(reads) < MEM_READS:
        sleep(MEM_RETRY_S)
        reads.append(read())
        out("MemAvailable read %d of %d at most, %d s after a read below the floor: %d bytes" % (
            len(reads), MEM_READS, MEM_RETRY_S, reads[-1]))
    passes, final = memory_gate(reads)
    assert passes, "BLOCKED: MemAvailable %d bytes at read %d, every read below %d" % (final, len(reads), MEM_FLOOR)
    assert free >= DISK_GATE, "BLOCKED: %d bytes free, below %d" % (free, DISK_GATE)


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


def is_active(unit):
    cp = subprocess.run(["systemctl", "is-active", unit], capture_output=True, text=True)
    return cp.stdout.strip()

# ---- the clock: the pair book's idle stretch and both archives' runs -----------------------------------------


def archives_state():
    return {k: is_active(svc) for k, (svc, _timer) in sorted(ARCHIVES.items())}


def budget_s(nbytes):
    """The seconds a request or a unit is held for: MARGIN_S, and its bytes at RATE_FLOOR, rounded up (TZ-28's)."""
    return MARGIN_S + -(-int(nbytes) // RATE_FLOOR)


def quiet(now, budget, state_of=None):
    """None where a unit of `budget` seconds may start at `now`; otherwise why not: it starts inside the pair book's
    idle stretch and ends by its second 590, never near or during either archive's run (TZ-43's rule)."""
    state_of = state_of or archives_state
    p = int(now) % SLOT
    if not IDLE[0] <= p <= IDLE[1] - budget:
        return "second %d of the window" % p
    d = int(now) % DAY
    for at, what in CALENDAR:
        if at - budget - CALENDAR_LEAD_S <= d <= at + CALENDAR_LEAD_S:
            return what
    for k, st in sorted(state_of().items()):
        if st in RUNNING:
            return "the %s archive's service is %s" % (k, st)
    return None


def hold(budget, clock=None, sleep=None, state_of=None):
    """Until a unit of `budget` seconds may start; returns that instant and the seconds waited."""
    clock, sleep = clock or time.time, sleep or time.sleep
    assert budget <= IDLE[1] - IDLE[0], "a unit of %d s fits no idle stretch" % budget
    t0 = clock()
    while True:
        now = clock()
        why = quiet(now, budget, state_of)
        if why is None:
            return now, now - t0
        assert now - t0 <= HOLD_MAX_S, "BLOCKED: held %.0f s, the last reason %s" % (now - t0, why)
        sleep(1.0)

# ---- GitHub: TZ-27's client, every request held ------------------------------------------------------------


class Gh44(tz27.GitHub):
    """TZ-27's GitHub, every request held by `held` - the pair book's idle stretch, away from both archives' runs -
    and recorded; the Release created on its tag at the instrument's commit, published, never the latest."""

    def __init__(self, token=None, record=None, held=None, commit=None, api=None, uploads=None, web=None):
        super().__init__(token, api or tz27.API_BASE, uploads or tz27.UPLOAD_BASE, web or tz27.WEB_BASE)
        self.record, self.held, self.commit, self.sizes = record, held or hold, commit, {}

    def _timed(self, kind, name, nbytes, fn):
        budget = budget_s(nbytes)
        _at, waited = self.held(budget)
        t0, ok = time.time_ns(), False
        try:
            res = fn()
            ok = True
            return res
        finally:
            if self.record is not None:
                self.record({"kind": kind, "name": name, "bytes": int(nbytes), "budget_s": budget,
                             "waited_s": round(waited, 3), "start_ns": t0, "end_ns": time.time_ns(), "ok": ok})

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
        assert self.token is not None and SHA40.fullmatch(self.commit or ""), "create_release: token and commit"
        self.pace()
        status, doc, _h = self._json("POST", "%s/repos/%s/releases" % (self.api, tz27.REPO),
                                     {"tag_name": tag, "target_commitish": self.commit, "name": name, "body": body,
                                      "draft": False, "prerelease": False, "make_latest": "false"})
        assert status == 201 and isinstance(doc, dict), "create release %s: status %r" % (tag, status)
        return doc


def release_text(doc, commit):
    name = "%s: L0's inputs - the reward book's days %s to %s and TZ-43's work files" % (
        doc["tag"], utc(FIRST_D0)[:10], utc(LAST_D0)[:10])
    body = ("Every file of /var/lib/btc-rewardbook/<D0>/ but its streams, for the %d UTC days %d to %d - each day's "
            "selections with their replies, its slot records and its reward polls, stored verbatim - one tar a day, "
            "rewardbook-inputs-<D0>.tar, its members named <D0>/<file>; and the %d files of TZ-43's fetch/ and days/, "
            "its set.json and its reading.json, as /root/btc-forensics/ holds them, each asset the bytes TZ-43's "
            "report names under its path in TZ-43's tree, tz43-<path> with - for /. %s lists every asset and every "
            "member by its bytes and SHA-256, and each TZ-43 file's path and forensic name. A file of stored replies "
            "is left out, and named there with its bytes and the line that withheld it, where a line of it carries a "
            "body the venue did not serve as a JSON document under status 200: an error page can carry the address "
            "it was served to. The streams are the rewardbook-streams-* Releases'. Every day from %d (2026-11-09) is "
            "reserved for L0's next gate and is not here. %d assets, %d bytes, made by research/%s at commit %s "
            "(TZ-44). Each asset's SHA-256 is its "
            "digest here." % (len(DAYS), FIRST_D0, LAST_D0, len(TZ43_FILES), MANIFEST, RESERVE_D0, doc["assets_n"],
                              doc["bytes_total"], PYFILE, commit))
    return name, body


def tag_reading(obj, peeled, commit):
    """G-TAG: the tag on origin is lightweight and names the instrument's commit. Pure."""
    return obj is not None and obj == commit and peeled is None

# ---- the pack: TZ-43's files checked, one tar a day, the manifest and the set ---------------------------------


def forensic_name(path):
    """The name TZ-43's reclaim gave a file of its tree in the forensic store."""
    return "tz43-work--" + path.replace("/", "--")


def asset_name(path):
    """The Release's name of a file of TZ-43's tree: one hyphen between parts, so the venue of the bytes keeps it."""
    return "tz43-" + path.replace("/", "-")


def classify(d0, name):
    """A name of the day directory d0: select, slot or rewards - a member - or stream or other, never opened. A slot's
    file under another day's directory is a failed assert. Pure."""
    if SELECT_FILE_RE.fullmatch(name):
        return "select"
    m = SLOT_FILE_RE.fullmatch(name)
    if m is None:
        return "other"
    s = int(m.group(1))
    assert d0 <= s < d0 + DAY and s % SLOT == 0, "BLOCKED: %s under %d is a slot of another day" % (name, d0)
    return {"stream.jsonl.gz": "stream", "rewards.jsonl.gz": "rewards", "slot.json": "slot"}[m.group(3)]


def literal_rows_missing(text, files=None):
    """The literals of TZ43_FILES not printed in TZ-43's report as its section 2.6 table prints them. Pure."""
    files = TZ43_FILES if files is None else files
    return [p for p, n, h in files if ("| `%s` | %d | `%s` |" % (p, n, h)) not in text]


def check_sources(root=None, files=None):
    """G-SOURCE: each of TZ-43's files in the forensic store, a regular file of the bytes and SHA-256 its report
    names."""
    root, files = FORENSICS if root is None else root, TZ43_FILES if files is None else files
    rows, bad = [], []
    for path, nbytes, sha in files:
        name = forensic_name(path)
        p = os.path.join(root, name)
        st = os.lstat(p)
        assert stat.S_ISREG(st.st_mode), "BLOCKED: %s is not a regular file" % p
        h = sha256_file(p)
        good = st.st_size == nbytes and h == sha
        out("G-SOURCE %s %d bytes sha256 %s %s" % (name, st.st_size, h, "equal" if good else "DIFFERS"))
        if not good:
            bad.append(name)
        rows.append({"asset": asset_name(path), "source": name, "path": path, "bytes": st.st_size, "sha256": h})
    assert not bad, "BLOCKED: G-SOURCE %d of %d differ from TZ-43's report: %s" % (len(bad), len(files), bad)
    return rows


def member_info(arcname, size, mtime):
    ti = tarfile.TarInfo(arcname)
    ti.size, ti.mtime, ti.mode, ti.type = size, mtime, 0o644, tarfile.REGTYPE
    ti.uid = ti.gid = 0
    ti.uname = ti.gname = ""
    return ti


def day_budget(member_bytes):
    """The seconds a day's unit is held for: UNIT_BASE_S, and its members' bytes at SCAN_RATE, rounded up. Pure."""
    return UNIT_BASE_S + -(-int(member_bytes) // SCAN_RATE)


def body_reason(rec):
    """Why one stored reply keeps its file out of the Release, or None. A body is published only where the venue
    served it as a JSON document under status 200: any other body - an error page among them - can carry the address
    it was served to. Pure."""
    if not isinstance(rec, dict):
        return "not a record"
    raw = rec.get("raw")
    if raw is None or raw == "":
        return None
    if rec.get("status") != 200:
        return "a body under status %s" % (rec.get("status") if isinstance(rec.get("status"), int) else "of no number")
    if not isinstance(raw, str):
        return "a body that is not text"
    try:
        doc = json.loads(raw)
    except (ValueError, RecursionError):
        return "a status-200 body that is not JSON"
    return None if isinstance(doc, (dict, list)) else "a status-200 body that is not a JSON document"


def withhold_reason(path):
    """Why a file of stored replies is left out of the Release, or None where every line of it is a record whose
    body, where it has one, is a JSON document the venue served under status 200. One read, a line at a time; the
    reason names a line by its number and never by its content."""
    try:
        with gzip.open(path, "rb") as fh:
            for k, ln in enumerate(fh, 1):
                if not ln.strip():
                    continue
                try:
                    rec = json.loads(ln)
                except (ValueError, RecursionError):
                    return "line %d: not JSON" % k
                why = body_reason(rec)
                if why is not None:
                    return "line %d: %s" % (k, why)
    except (OSError, EOFError, zlib.error) as exc:
        return "not a whole gzip file: %s" % type(exc).__name__
    return None


def list_day(root, d0):
    """A day directory's names, listed once: its members by name and bytes, every other name by its bytes and kind -
    a stream or a stray name, never opened - the members' bytes and the names counted by kind."""
    ddir = os.path.join(root, str(d0))
    assert os.path.isdir(ddir) and not os.path.islink(ddir), "BLOCKED: %s is not a directory" % ddir
    names = sorted(os.listdir(ddir))
    kinds = {n: classify(d0, n) for n in names}
    members, excluded, total = [], [], 0
    for n in names:
        st = os.lstat(os.path.join(ddir, n))
        if kinds[n] in MEMBER_KINDS:
            assert stat.S_ISREG(st.st_mode), "BLOCKED: %s/%s is not a regular file" % (ddir, n)
            members.append((n, st.st_size))
            total += st.st_size
        else:
            excluded.append({"name": n, "bytes": st.st_size, "kind": kinds[n]})
    assert members, "BLOCKED: %s holds no member" % ddir
    assert total <= DAY_MAX_BYTES, "BLOCKED: %s holds %d bytes of members, above %d" % (ddir, total, DAY_MAX_BYTES)
    return {"members": members, "excluded": excluded, "total": total,
            "counts": {k: sum(1 for n in names if kinds[n] == k) for k in KINDS}}


def pack_day(root, d0, outdir, listing=None, freef=None):
    """One day's archive, outdir/rewardbook-inputs-<D0>.tar: every member of root/<D0>/ in name order, stored verbatim
    as <D0>/<name>, its mtime D0, mode 644, owner 0 - but a file of stored replies one of whose lines withholds it,
    named with its bytes and that line and left out. Written once; a later run must build the same bytes. Returns
    (its manifest entry, wrote or unchanged)."""
    ddir = os.path.join(root, str(d0))
    lst = listing or list_day(root, d0)
    need = lst["total"] + 2 * tarfile.BLOCKSIZE * (len(lst["members"]) + 1) + tarfile.RECORDSIZE
    free = (freef or free_bytes)()
    assert free - need >= DISK_FLOOR, "BLOCKED: %d bytes free, %d needed, the floor %d" % (free, need, DISK_FLOOR)
    kept, withheld, scanned = [], [], 0
    for n, size in lst["members"]:
        why = None
        if n.endswith(SCANNED):
            scanned += 1
            why = withhold_reason(os.path.join(ddir, n))
        if why is None:
            kept.append((n, size))
        else:
            withheld.append({"name": n, "bytes": size, "reason": why})
    assert kept, "BLOCKED: %s: every member withheld" % ddir
    name = ARCHIVE_FMT % d0
    part, final = os.path.join(outdir, name + ".part"), os.path.join(outdir, name)
    rows = []
    with open(part, "wb") as fh:
        with tarfile.open(fileobj=fh, mode="w", format=tarfile.USTAR_FORMAT) as tf:
            for n, size in kept:
                with open(os.path.join(ddir, n), "rb") as src:
                    assert os.fstat(src.fileno()).st_size == size, "BLOCKED: %s/%s changed size" % (ddir, n)
                    rd = tz27.HashingReader(src)
                    tf.addfile(member_info("%d/%s" % (d0, n), size, d0), rd)
                    assert rd.n == size and src.read(1) == b"", "BLOCKED: %s/%s changed while read" % (ddir, n)
                rows.append({"name": "%d/%s" % (d0, n), "bytes": size, "sha256": rd.h.hexdigest()})
    sha, nbytes = sha256_file(part), os.stat(part).st_size
    if os.path.exists(final):
        got = sha256_file(final)
        assert got == sha, "determinism: %s sha256 %s, this run's %s" % (final, got, sha)
        os.remove(part)
        state = "unchanged"
    else:
        os.rename(part, final)
        state = "wrote"
    return {"D0": d0, "date": utc(d0)[:10], "archive": name, "bytes": nbytes, "sha256": sha, "members_n": len(rows),
            "member_bytes": sum(size for _n, size in kept), "scanned_n": scanned, "withheld_n": len(withheld),
            "withheld_bytes": sum(w["bytes"] for w in withheld), "counts": lst["counts"], "members": rows,
            "withheld": withheld, "excluded": lst["excluded"]}, state


def manifest_doc(commit, file_sha, days, sources, report_sha):
    return {"tag": TAG, "made_by": "research/" + PYFILE, "commit": commit, "file_sha256": file_sha, "store": RB_ROOT,
            "first_D0": FIRST_D0, "last_D0": LAST_D0, "reserve_from_D0": RESERVE_D0, "days": days,
            "tz43": {"report": TZ43_REPORT, "report_sha256": report_sha, "files": sources}}


def set_doc(days, sources, manifest_bytes, manifest_sha):
    """The Release's set, in upload order: the day archives, TZ-43's files, the manifest. Each entry's T and file
    place it under UPLOAD_ROOT for TZ-27's upload_set (store_path)."""
    out_t = os.path.relpath(OUT, UPLOAD_ROOT)
    src_t = os.path.relpath(FORENSICS, UPLOAD_ROOT)
    assets = [{"T": out_t, "file": d["archive"], "asset": d["archive"], "bytes": d["bytes"], "sha256": d["sha256"]}
              for d in days]
    assets += [{"T": src_t, "file": s["source"], "asset": s["asset"], "bytes": s["bytes"], "sha256": s["sha256"]}
               for s in sources]
    assets.append({"T": out_t, "file": MANIFEST, "asset": MANIFEST, "bytes": manifest_bytes, "sha256": manifest_sha})
    names = [x["asset"] for x in assets]
    assert len(set(names)) == len(names), "two assets of one name"
    return {"tag": TAG, "assets": assets, "assets_n": len(assets), "bytes_total": sum(x["bytes"] for x in assets)}


def read_set(st):
    p = st.get("pack")
    assert p, "no set: pack has not run"
    with open(SET_FILE, "rb") as fh:
        raw = fh.read()
    assert sha256_bytes(raw) == p["set_sha256"], "set.json is not the set pack wrote"
    return json.loads(raw), raw

# ---- the venue's geoblock: what may be printed of its reply ----------------------------------------------------


def geo_fields(doc):
    """What the report may print of the venue's reply: blocked, country and region, and the reply's key names - never
    the address it carries. Pure."""
    if not isinstance(doc, dict):
        return None
    return {"blocked": doc.get("blocked"), "country": doc.get("country"), "region": doc.get("region"),
            "keys": sorted(str(k) for k in doc)}

# ---- the session's modes ------------------------------------------------------------------------------------


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
        out("%-48s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"],
                         states["reported"]))


def number_reading(names, own):
    """NUMBER, CANON hard rule 2: CryptoTZ/ holds this TZ's file and no other of its number; CryptoReports/ no report
    of it. Pure."""
    tz = [n for n in names if n.startswith("CryptoTZ/" + NUMBER)]
    rp = [n for n in names if n.startswith("CryptoReports/" + NUMBER)]
    return tz == [own] and not rp, tz, rp


def mode_number():
    names = git("ls-tree", "--name-only", "origin/main", "--", "CryptoTZ/", "CryptoReports/", tree=PRIMARY).split("\n")
    head = git("rev-parse", "origin/main", tree=PRIMARY)
    ok, tz, rp = number_reading(names, OWN_TZ)
    out("origin/main %s: %d paths under CryptoTZ/ and CryptoReports/; of the number %s: %s and %s" % (
        head, len(names), NUMBER, tz, rp))
    out("NUMBER %s" % ("PASS - 2 of 2" if ok else "FAIL"))
    assert ok, "BLOCKED: of the number %s, CryptoTZ/ holds %s and CryptoReports/ %s" % (NUMBER, tz, rp)


def ledger_records(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    lines = raw.split(b"\n")
    tail = lines.pop()
    return raw, [json.loads(ln) for ln in lines if ln.strip()], tail


def still_reading(before, now, restarts):
    """G-STILL from two reads and the pair book archive's restart records between them, in order: PASS where every
    unit is unchanged, or where every unit but the pair book is unchanged and its change is that archive's own
    restarts alone - a chain from the recorded MainPID to the current one, NRestarts one higher at each, the unit
    active. Pure."""
    if now == before:
        return True, "unchanged"
    for k in sorted(now):
        if k != "pairbook" and now[k] != before.get(k):
            return False, "the %s changed" % k
    b, n = before["pairbook"], now["pairbook"]
    pid, count = b["MainPID"], int(b["NRestarts"])
    for r in restarts:
        if str(r.get("stopped")) != pid or str(r.get("NRestarts")) != str(count + 1):
            return False, "a restart record that does not follow %s at NRestarts %d: %r" % (pid, count, r)
        pid, count = str(r.get("pid")), count + 1
    if restarts and pid == n["MainPID"] and str(count) == n["NRestarts"] and n["ActiveState"] == "active":
        return True, "changed by the pair book archive's own restarts alone: %d" % len(restarts)
    return False, "the pair book changed, %d restart records of its archive since the first read" % len(restarts)


def mode_still():
    st = load_state()
    now = {}
    for key, unit in sorted(UNITS.items()):
        kv = show(unit, ["MainPID", "NRestarts", "ActiveState", "MemoryCurrent", "MemoryPeak"])
        now[key] = {k: kv[k] for k in ("MainPID", "NRestarts", "ActiveState")}
        out("%s %s, MemoryCurrent %s, MemoryPeak %s" % (unit, now[key], kv.get("MemoryCurrent"), kv.get("MemoryPeak")))
    for key, (svc, timer) in sorted(ARCHIVES.items()):
        for unit in (timer, svc):
            out("%s %s" % (unit, show(unit, ["ActiveState", "SubState", "UnitFileState", "Result"])))
    if "still" not in st:
        st["still"] = {"at": utc(time.time()), "at_ns": time.time_ns(), "units": now}
        save_state(st)
        out("still: recorded")
        return
    _raw, recs, _tail = ledger_records(PB_LEDGER)
    since = st["still"]["at_ns"]
    restarts = [r for r in recs if r.get("event") == "restart" and r.get("wall_ns", 0) >= since]
    for r in restarts:
        out("the pair book archive's restart record %s: run %s, window %s, pid %s after %s, NRestarts %s" % (
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


def mode_pack():
    """G-SOURCE, then G-PACK: the 34 sources as one held unit, each day as one, held for its members' bytes; the
    manifest and the set written once; a second run asserts all of it unchanged (DETERMINISM)."""
    floor_check()
    commit, up = git("rev-parse", "HEAD"), git("rev-parse", "@{u}")
    assert SHA40.fullmatch(commit) and commit == up, "BLOCKED: the branch head %s is not its upstream's %s" % (
        commit, up)
    file_sha = sha256_file(os.path.join(HERE, PYFILE))
    with open(os.path.join(PRIMARY, TZ43_REPORT), "rb") as fh:
        report = fh.read()
    missing = literal_rows_missing(report.decode("utf-8"))
    assert not missing, "BLOCKED: rows not in TZ-43's report: %s" % missing
    out("TZ-43's report %s, %d bytes, sha256 %s: the rows of its %d files found %d of %d" % (
        TZ43_REPORT, len(report), sha256_bytes(report), len(TZ43_FILES), len(TZ43_FILES) - len(missing),
        len(TZ43_FILES)))
    at, waited = hold(UNIT_BUDGET_S)
    t0 = time.time()
    sources = check_sources()
    out("G-SOURCE PASS: %d of %d equal to TZ-43's report, %d bytes; held %.1f s, from second %d, %.2f s" % (
        len(sources), len(TZ43_FILES), sum(s["bytes"] for s in sources), waited, int(at) % SLOT, time.time() - t0))
    os.makedirs(OUT, exist_ok=True)
    days, states, over = [], collections.Counter(), 0
    for d0 in DAYS:
        listing = list_day(RB_ROOT, d0)
        budget = day_budget(listing["total"])
        at, waited = hold(budget)
        t0 = time.time()
        entry, state = pack_day(RB_ROOT, d0, OUT, listing)
        took = time.time() - t0
        over += 1 if took > budget else 0
        states[state] += 1
        c = entry["counts"]
        out("day %d (%s): %d names - select %d, slot %d, rewards %d, stream %d and other %d never opened; %s %d "
            "members, %d bytes, of %d files of replies scanned; withheld %d, %d bytes; %s %d bytes sha256 %s; budget "
            "%d s, held %.1f s, from second %d, %.2f s" % (
                d0, entry["date"], sum(c.values()), c["select"], c["slot"], c["rewards"], c["stream"], c["other"],
                entry["archive"], entry["members_n"], entry["member_bytes"], entry["scanned_n"], entry["withheld_n"],
                entry["withheld_bytes"], state, entry["bytes"], entry["sha256"], budget, waited, int(at) % SLOT, took))
        for x in entry["withheld"]:
            out("  withheld %s, %d bytes: %s" % (x["name"], x["bytes"], x["reason"]))
        for x in entry["excluded"]:
            out("  excluded %s %s, %d bytes, never opened" % (x["kind"], x["name"], x["bytes"]))
        days.append(entry)
    report_sha = sha256_bytes(report)
    mraw = tz27.json_bytes(manifest_doc(commit, file_sha, days, sources, report_sha))
    states[write_once(os.path.join(OUT, MANIFEST), mraw)] += 1
    doc = set_doc(days, sources, len(mraw), sha256_bytes(mraw))
    raw = tz27.json_bytes(doc)
    states[write_once(SET_FILE, raw)] += 1
    st = load_state()
    st["pack"] = {"commit": commit, "file_sha256": file_sha, "set_sha256": sha256_bytes(raw),
                  "manifest_sha256": sha256_bytes(mraw), "assets_n": doc["assets_n"], "bytes_total": doc["bytes_total"]}
    save_state(st)
    for x in doc["assets"]:
        out("S %s %d %s" % (x["asset"], x["bytes"], x["sha256"]))
    members, scanned = sum(d["members_n"] for d in days), sum(d["scanned_n"] for d in days)
    out("G-PACK PASS: %d days of %d, %d members, %d bytes of members, %d bytes of archives; withheld %d files of "
        "replies, %d bytes; streams %d and other names %d never opened; %d assets, %d bytes; days over their budget "
        "%d; outputs %s" % (
            len(days), len(DAYS), members, sum(d["member_bytes"] for d in days), sum(d["bytes"] for d in days),
            sum(d["withheld_n"] for d in days), sum(d["withheld_bytes"] for d in days),
            sum(d["counts"]["stream"] for d in days), sum(d["counts"]["other"] for d in days), doc["assets_n"],
            doc["bytes_total"], over, dict(sorted(states.items()))))
    assert COUNTS["reward book opens"] == members + scanned and COUNTS["reward book listings"] == len(DAYS), \
        "BLOCKED: the store opened %d times and listed %d, for %d members, %d files scanned and %d days" % (
            COUNTS["reward book opens"], COUNTS["reward book listings"], members, scanned, len(DAYS))
    out("G-RESERVE PASS: the store opened %d times - once a member kept, %d, and once a file of replies scanned, %d "
        "- and listed %d times, one a day; no other open or listing under %s" % (
            COUNTS["reward book opens"], members, scanned, COUNTS["reward book listings"], RB_ROOT))
    if states["unchanged"] == len(DAYS) + 2:
        out("DETERMINISM PASS: %d of %d outputs unchanged" % (states["unchanged"], len(DAYS) + 2))


def upload_logger():
    def log(rec):
        rec = dict(rec, at=utc(time.time()), wall_ns=rec.get("wall_ns", time.time_ns()))
        tz27.forbid(rec, "upload.jsonl")
        jsonl_append(UPLOAD_LOG, rec)
        out("U %s" % json.dumps(rec, sort_keys=True))
    return log


def transfer_logger():
    return lambda rec: jsonl_append(TRANSFERS, rec)


def transfer_summary(recs):
    """The transfers' places in their windows: (count, started outside the idle stretch, ended after its second 590
    or in a later window, seconds waited). Pure."""
    outside = late = 0
    for r in recs:
        s0, s1 = r["start_ns"] / 1e9, r["end_ns"] / 1e9
        outside += 0 if IDLE[0] <= int(s0) % SLOT <= IDLE[1] else 1
        late += 0 if int(s1) - int(s1) % SLOT == int(s0) - int(s0) % SLOT and int(s1) % SLOT <= IDLE[1] else 1
    return len(recs), outside, late, round(sum(r["waited_s"] for r in recs), 1)


def branch_on_origin():
    lines = [ln.split("\t") for ln in git("ls-remote", "origin", "refs/heads/" + BRANCH, tree=PRIMARY).split("\n")
             if "\t" in ln]
    return lines[0][0] if len(lines) == 1 else None


def mode_upload():
    """B-UPLOAD, the Boss's block: the credential, the Release on TAG at the pack's commit, the set's assets."""
    floor_check()
    st = load_state()
    doc, raw = read_set(st)
    commit = st["pack"]["commit"]
    assert git("rev-parse", "HEAD") == commit, "BLOCKED: the worktree's HEAD is not the pack's commit %s" % commit
    assert branch_on_origin() == commit, "BLOCKED: origin's %s is not the pack's commit %s" % (BRANCH, commit)
    for x in doc["assets"]:
        p = tz27.store_path(UPLOAD_ROOT, x)
        assert os.path.isfile(p) and os.stat(p).st_size == x["bytes"], "BLOCKED: %s is not the set's %d bytes" % (
            p, x["bytes"])
    out("set %s: %d assets, %d bytes, at commit %s" % (sha256_bytes(raw), doc["assets_n"], doc["bytes_total"], commit))
    tok, source = tz27.credential()
    out("credential: %s" % source)
    log = upload_logger()
    gh = Gh44(token=tok, record=transfer_logger(), commit=commit)
    try:
        rel = gh.release_by_tag(TAG)
        created = rel is None
        if created:
            rel = gh.create_release(TAG, *release_text(doc, commit))
            out("created the Release on %s, id %s, target %s" % (TAG, rel.get("id"), rel.get("target_commitish")))
        assert rel.get("tag_name") == TAG and rel.get("draft") is False, "the Release is not published on the tag"
        sent, held = tz27.upload_set(gh, rel, doc, UPLOAD_ROOT, log)
        log({"action": "complete", "assets": sent + held, "sent": sent, "held": held, "release_id": int(rel["id"]),
             "created": created, "credential": source, "wall_ns": time.time_ns()})
    finally:    # printed on every exit of the upload, a refusal's and a failed assert's included
        n, outside, late, waited = transfer_summary(jsonl_read(TRANSFERS))
        out("transfers so far %d: %d started outside the idle stretch, %d ended after its second %d; %.1f s held" % (
            n, outside, late, IDLE[1], waited))
    out("UPLOAD COMPLETE: Release %s on %s, %d assets - %d sent, %d already held - %d bytes" % (
        rel["id"], TAG, sent + held, sent, held, doc["bytes_total"]))


def mode_verify():
    """G-TAG, G-UPLOAD and G-DOWNLOAD, with no token, 120 s or more after the upload's completion record."""
    floor_check()
    st = load_state()
    doc, raw = read_set(st)
    commit = st["pack"]["commit"]
    recs = jsonl_read(UPLOAD_LOG)
    why = tz27.upload_ready(recs, doc["assets_n"], time.time_ns())
    if why is not None and recs and recs[-1].get("action") == "complete":
        time.sleep(max(0.0, (recs[-1]["wall_ns"] + tz27.UPLOAD_SETTLE_S * 10 ** 9 - time.time_ns()) / 1e9 + 0.5))
        why = tz27.upload_ready(recs, doc["assets_n"], time.time_ns())
    assert why is None, "BLOCKED: %s" % why
    anon = Gh44(token=None, record=transfer_logger())
    anon.sizes = {x["asset"]: x["bytes"] for x in doc["assets"]}
    try:
        rel, rows, missing, extra = tz27.verify_release(anon, TAG, doc)
        for r in rows:
            out("V %s id %s state %s api %s bytes %s digest %s url %s download %s" % (
                r["asset"], r["id"], r["state"], r["api_ok"], r["api_bytes"], r["digest"], r["url_ok"],
                r["download_ok"]))
        checks = tz27.release_reading(rel, TAG, rows, missing, extra)
        obj, peeled = tz27.ls_remote_tag(TAG)
        out("tag %s on origin: %s, peeled %s; the pack's commit %s; the Release's target %s" % (
            TAG, obj, peeled, commit, (rel or {}).get("target_commitish")))
        checks["the tag on origin lightweight, at the pack's commit"] = tag_reading(obj, peeled, commit)
        for k, v in checks.items():
            out("G-TAG/G-UPLOAD/G-DOWNLOAD %-56s %s" % (k, v))
        assert all(checks.values()), "VERIFY FAIL: %r; missing %r; beyond %r" % (
            sorted(k for k, v in checks.items() if not v), missing[:5], extra[:5])
        vdoc = {"tag": TAG, "release_id": int(rel["id"]), "set_sha256": sha256_bytes(raw), "commit": commit,
                "assets": rows, "assets_n": len(rows), "bytes_total": sum(r["download_bytes"] for r in rows)}
        write_once(VERIFY_FILE, tz27.json_bytes(vdoc))
    finally:    # printed on every exit of the proof, a failed download's and a failed assert's included
        n, outside, late, waited = transfer_summary(jsonl_read(TRANSFERS))
        out("transfers %d, upload's and verify's: %d started outside the idle stretch, %d ended after its second %d; "
            "%.1f s held" % (n, outside, late, IDLE[1], waited))
    out("G-UPLOAD PASS: %d of %d assets by name, bytes, state and digest; G-DOWNLOAD PASS: %d of %d downloads, "
        "%d bytes; G-TAG PASS: %s at %s" % (sum(r["api_ok"] for r in rows), doc["assets_n"],
                                           sum(r["download_ok"] for r in rows), doc["assets_n"], vdoc["bytes_total"],
                                           TAG, commit))


def mode_geoblock():
    """One read of the venue's geoblock endpoint from the host, printed and gating nothing; the address its reply
    carries is never printed or written."""
    try:
        addrs = sorted({ai[4][0] for ai in socket.getaddrinfo(GEO_HOST, 443, type=socket.SOCK_STREAM)})
        out("DNS %s: %s" % (GEO_HOST, addrs))
    except OSError as exc:
        out("DNS %s: %s %s" % (GEO_HOST, type(exc).__name__, getattr(exc, "errno", None)))
    req = urllib.request.Request(GEO_URL, headers=dict(GEO_HEADERS), method="GET")
    status, body, where = None, b"", None
    t0 = time.time()
    try:
        with tz27.opener(follow=False).open(req, timeout=GEO_TIMEOUT_S) as resp:
            status, body = int(resp.status), resp.read(GEO_READ_MAX)
    except urllib.error.HTTPError as exc:
        status = int(exc.code)
        loc = exc.headers.get("Location") if exc.headers is not None else None
        where = urllib.parse.urlsplit(loc).hostname if loc else None
    except Exception as exc:     # the read gates nothing: every failure is printed by its kind alone
        out("GEOBLOCK no reply: %s" % type(exc).__name__)
    try:
        doc = json.loads(body) if body else None
    except ValueError:
        doc = None
    f = geo_fields(doc)
    out("GEOBLOCK READ: %s, status %s%s, %d bytes in %.2f s; blocked %r, country %r, region %r; reply keys %s" % (
        GEO_URL, status, (", redirect to host %s" % where) if where else "", len(body), time.time() - t0,
        f and f["blocked"], f and f["country"], f and f["region"], f and f["keys"]))


def report_tokens():
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith(".md"):
            with open(os.path.join(REPORTS, name), encoding="utf-8", errors="replace") as fh:
                tokens.update(TOKEN.findall(fh.read()))
    return tokens


def by_name(tree, rel):
    return tree == WORK and (rel == "state.json" or rel.startswith("logs/"))


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
                size, free = os.path.getsize(path), free_bytes()
                assert free - size >= DISK_FLOOR, "BLOCKED: reclaim: %d bytes free, %s is %d, the floor %d" % (
                    free, path, size, DISK_FLOOR)
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest) == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, %d already held; "
        "forensic store %d -> %d files" % (considered, named, kept, copied, held, before, after))


def main(argv):
    if not argv:
        sys.exit("usage: %s MODE [ARG...]" % PYFILE)
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    tz27.MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "number": mode_number, "selftest": mode_selftest, "still": mode_still,
             "pack": mode_pack, "upload": mode_upload, "verify": mode_verify, "geoblock": mode_geoblock}
    try:
        if mode == "reclaim":
            mode_reclaim(rest)
        elif mode == "scratch":
            assert len(rest) == 1, "scratch OWN"
            mode_scratch(rest[0])
        else:
            assert mode in table and not rest, "unknown mode %r" % (argv,)
            table[mode]()
    finally:    # printed on every exit, a BLOCK's and a failed assert's included
        out("malloc tuned: %s" % MALLOC_TUNED)
        out("peak memory of this run: %d bytes" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
        out("opens refused: %d, by TZ-27's hook: %d; reward book opens: %d, listings: %d" % (
            len(REFUSED), len(tz27.REFUSED), COUNTS["reward book opens"], COUNTS["reward book listings"]))

# ---- the self-test: literals, temporary trees under the work tree and a loopback GitHub -----------------------


def mode_selftest():
    import http.server
    import threading
    n = [0]

    def ok(cond, what):
        assert cond, "selftest: " + what
        n[0] += 1
        out("  ok  " + what)

    def fails(fn, exc=AssertionError):
        try:
            fn()
        except exc:
            return True
        return False

    tmp = os.path.join(WORK, "selftest-tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    # the constants
    ok(MALLOC_TUNED, "glibc took the 128 KiB mmap threshold and the two arenas")
    ok(len(DAYS) == 12 and DAYS[0] == FIRST_D0 and DAYS[-1] == LAST_D0 and RESERVE_D0 == LAST_D0 + DAY and
       utc(FIRST_D0) == "2026-10-28T00:00:00Z" and utc(LAST_D0) == "2026-11-08T00:00:00Z" and
       utc(RESERVE_D0) == "2026-11-09T00:00:00Z" and all(d % DAY == 0 for d in DAYS),
       "twelve UTC days, 2026-10-28 to 2026-11-08, the last the day before the reserve's first, 2026-11-09")
    paths = [p for p, _n, _h in TZ43_FILES]
    want = sorted(["fetch/%d.json" % d for d in TZ43_MEMBERS] + ["fetch/%d.polls.jsonl" % d for d in TZ43_MEMBERS] +
                  ["days/%d.json" % d for d in TZ43_MEMBERS] + ["days/%d.slots.txt" % d for d in TZ43_MEMBERS] +
                  ["set.json", "reading.json"])
    ok(len(TZ43_FILES) == 34 and sorted(paths) == want and len(set(paths)) == 34 and
       all(SHA_RE.fullmatch(h) and n > 0 for _p, n, h in TZ43_FILES) and set(TZ43_MEMBERS) <= set(DAYS) and
       sum(n for _p, n, _h in TZ43_FILES) == 42169992,
       "TZ-43's 34 files: fetch/ and days/ of its 8 member days, set.json and reading.json, 42,169,992 bytes")
    ok(forensic_name("fetch/1793404800.json") == "tz43-work--fetch--1793404800.json" and
       forensic_name("set.json") == "tz43-work--set.json" and len({forensic_name(p) for p in paths}) == 34 and
       asset_name("fetch/1793404800.polls.jsonl") == "tz43-fetch-1793404800.polls.jsonl" and
       asset_name("reading.json") == "tz43-reading.json" and len({asset_name(p) for p in paths}) == 34 and
       all("--" not in asset_name(p) and re.fullmatch(r"[a-z0-9][a-z0-9.-]*", asset_name(p)) for p in paths),
       "each file's name in the forensic store, as TZ-43's reclaim made it, and in the Release, one hyphen apart")
    ok(UA == "btc-5m-twap-tz44" and GEO_HEADERS == {"User-Agent": UA, "Accept": "application/json"} and
       tz27.UA == "btc-5m-twap-tz27" and tz27.CONTENT_TYPE == "application/octet-stream" and tz27.WORK[0] == WORK,
       "the geoblock read under this TZ's agent; GitHub's under TZ-27's, every asset octet-stream; TZ-27's work tree")
    lo = MEM_FLOOR - 1
    ok(MEM_FLOOR == 2 * -(-41000000 * 58953728 // 49168384) == 98319394 and DISK_FLOOR == 7400000000 and
       DISK_GATE == 7800000000, "the floors: memory 98,319,394 bytes, disk 7,400,000,000 after a write and "
       "7,800,000,000 at a mode's start")
    ok(memory_gate([MEM_FLOOR]) == (True, MEM_FLOOR) and memory_gate([lo, lo, MEM_FLOOR]) == (True, MEM_FLOOR) and
       memory_gate([lo] * 5) == (False, lo) and fails(lambda: memory_gate([MEM_FLOOR, lo])) and
       fails(lambda: memory_gate([lo] * 6)),
       "the memory gate: a read at the floor or above passes; below it the next read decides, five reads at most")
    reads, slept = iter([lo, lo - 7, MEM_FLOOR + 3]), []
    floor_check(read=lambda: next(reads), sleep=slept.append, freef=lambda: DISK_GATE)
    reads2, slept2 = iter([lo] * 5), []
    ok(slept == [MEM_RETRY_S] * 2 and
       fails(lambda: floor_check(read=lambda: next(reads2), sleep=slept2.append, freef=lambda: DISK_GATE)) and
       slept2 == [MEM_RETRY_S] * 4 and
       fails(lambda: floor_check(read=lambda: MEM_FLOOR, sleep=slept2.append, freef=lambda: DISK_GATE - 1)),
       "floor_check reads again every 60 s while below its floor and BLOCKS after five; it BLOCKS below the disk gate")
    # the hook
    d1, dr = RB_ROOT + "/%d" % FIRST_D0, RB_ROOT + "/%d" % RESERVE_D0
    ok(policy("pack", "os.listdir", (d1,)) is None and
       policy("pack", "os.listdir", (RB_ROOT + "/%d" % LAST_D0,)) is None and
       policy("pack", "os.listdir", (dr,)) is not None and policy("pack", "os.listdir", (RB_ROOT,)) is not None
       and policy("upload", "os.listdir", (d1,)) is not None and policy("pack", "os.scandir", (d1,)) is None,
       "pack alone lists a day directory, of the twelve only: not the store's root, not a day from 2026-11-09")
    ok(policy("pack", "open", (d1 + "/select.0.json", "rb", 0)) is None and
       policy("pack", "open", (d1 + "/select.1.replies.jsonl.gz", "rb", 0)) is None and
       policy("pack", "open", (d1 + "/1793149200.0.slot.json", "rb", 0)) is None and
       policy("pack", "open", (d1 + "/1793149200.1.rewards.jsonl.gz", "rb", 0)) is None and
       policy("pack", "open", (d1 + "/1793149200.0.stream.jsonl.gz", "rb", 0)) is not None and
       policy("pack", "open", (dr + "/select.0.json", "rb", 0)) is not None and
       policy("pack", "open", (RB_ROOT + "/runtime.jsonl", "rb", 0)) is not None and
       policy("pack", "open", (RB_ROOT + "/service.log", "rb", 0)) is not None and
       policy("pack", "open", (d1 + "/select.0.json", "wb", 0)) is not None and
       policy("verify", "open", (d1 + "/select.0.json", "rb", 0)) is not None,
       "pack alone reads a day's selections, slot records and polls; never a stream, a reserved day, the root or a "
       "write")
    ok(policy("upload", "urllib.Request", ("https://api.github.com/repos/x",)) is None and
       policy("upload", "urllib.Request", ("https://uploads.github.com/repos/x",)) is None and
       policy("upload", "urllib.Request", ("https://github.com/x",)) is not None and
       policy("verify", "urllib.Request", ("https://github.com/x/releases/download/t/a",)) is None and
       policy("verify", "urllib.Request", ("https://release-assets.githubusercontent.com/x",)) is None and
       policy("verify", "urllib.Request", ("https://objects.githubusercontent.com/x",)) is None and
       policy("verify", "urllib.Request", ("https://uploads.github.com/x",)) is not None and
       policy("geoblock", "urllib.Request", (GEO_URL,)) is None and
       policy("geoblock", "urllib.Request", ("https://www.polymarket.com/api/geoblock",)) is not None and
       policy("geoblock", "urllib.Request", ("https://clob.polymarket.com/x",)) is not None and
       policy("pack", "urllib.Request", ("https://api.github.com/x",)) is not None and
       policy("still", "urllib.Request", ("https://api.github.com/x",)) is not None,
       "requests: upload to GitHub's API and upload host, verify to the API and the download hosts, geoblock to "
       "polymarket.com alone; no other mode reaches the network")
    ok(policy("pack", "subprocess.Popen", ("git", ["git"], None, None)) is None and
       policy("still", "subprocess.Popen", ("/usr/bin/systemctl", ["systemctl"], None, None)) is None and
       policy("upload", "subprocess.Popen", ("/usr/bin/gh", ["gh"], None, None)) is None and
       policy("verify", "subprocess.Popen", ("/usr/bin/gh", ["gh"], None, None)) is not None and
       policy("pack", "subprocess.Popen", ("/usr/bin/curl", ["curl"], None, None)) is not None,
       "processes: git, systemctl and stat; gh in upload alone, for TZ-27's credential")
    ok(policy("reclaim", "open", (FORENSICS + "/x", "xb", 0)) is None and
       policy("reclaim", "open", (FORENSICS + "/x", "wb", 0)) is not None and
       policy("pack", "open", (FORENSICS + "/x", "xb", 0)) is not None and
       policy("pack", "open", (FORENSICS + "/tz43-work--set.json", "rb", 0)) is None and
       policy("pack", "open", ("/root/elsewhere", "wb", 0)) is not None and
       policy("pack", "open", (OUT + "/x.part", "wb", 0)) is None and
       policy("still", "open", (PB_LEDGER, "rb", 0)) is None and
       policy("pack", "open", (PB_LEDGER, "rb", 0)) is not None and
       policy("still", "open", (RB_ARCHIVE + "/ledger.jsonl", "rb", 0)) is not None and
       policy("pack", "open", (RECORDER + "/runtime.jsonl", "rb", 0)) is not None and
       policy("pack", "open", (ADVISOR_ETC + "/token", "rb", 0)) is not None and
       policy("pack", "os.listdir", (PAIRBOOK,)) is not None,
       "writes: the work tree, and the forensic store by reclaim's exclusive create; the captures and the advisor shut")
    # the clock
    base = 1794400000 - 1794400000 % DAY + 10 * 3600     # a 10:00 UTC
    idle = {"pairbook": "inactive", "rewardbook": "inactive"}
    ok(quiet(base + 14, 60, lambda: idle) is not None and quiet(base + 15, 60, lambda: idle) is None and
       quiet(base + 530, 60, lambda: idle) is None and quiet(base + 531, 60, lambda: idle) is not None and
       quiet(base - 10 * 3600 + 5420, 5, lambda: idle) is not None and
       quiet(base - 10 * 3600 + 5481, 5, lambda: idle) is None and
       quiet(base - 10 * 3600 + 10850, 5, lambda: idle) is not None and
       quiet(base - 10 * 3600 + 10881, 5, lambda: idle) is None and
       quiet(base + 15, 5, lambda: {"pairbook": "active", "rewardbook": "inactive"}) is not None and
       budget_s(0) == 5 and budget_s(2000000) == 6 and budget_s(2000001) == 7 and budget_s(200000000) == 105,
       "a unit starts at second 15 of a window or later and ends by 590, away from both calendar runs and from a "
       "running archive; its budget 5 s and its bytes at 2,000,000 a second")
    clock = [base + 600.0]
    t, waited = hold(5, clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s),
                     state_of=lambda: idle)
    ok(int(t) % SLOT == 15 and round(waited) == 315 and
       fails(lambda: hold(5, clock=lambda: clock[0], sleep=lambda s: clock.__setitem__(0, clock[0] + s),
                          state_of=lambda: {"pairbook": "active", "rewardbook": "inactive"})),
       "hold waits for the next idle stretch, and BLOCKS after 7,200 s of a running archive")
    # the readings
    ok(number_reading([OWN_TZ, "CryptoTZ/TZ-43-l0-our-quote.md"], OWN_TZ)[0] and
       not number_reading([OWN_TZ, "CryptoTZ/TZ-44-other.md"], OWN_TZ)[0] and
       not number_reading([OWN_TZ, "CryptoReports/TZ-44-l0-inputs-release-report.md"], OWN_TZ)[0] and
       not number_reading([], OWN_TZ)[0], "NUMBER: this TZ's file alone of its number, and no report of it")
    u = {"MainPID": "5", "NRestarts": "1", "ActiveState": "active"}
    v = {"MainPID": "9", "NRestarts": "2", "ActiveState": "active"}
    bef = {"recorder": u, "pairbook": u, "rewardbook": u, "advisor": u}
    aft = dict(bef, pairbook=v)
    ok(still_reading(bef, dict(bef), []) == (True, "unchanged") and
       still_reading(bef, aft, [{"stopped": "5", "NRestarts": "2", "pid": "9"}])[0] and
       not still_reading(bef, aft, [])[0] and not still_reading(bef, dict(bef, recorder=v), [])[0] and
       not still_reading(bef, aft, [{"stopped": "4", "NRestarts": "2", "pid": "9"}])[0],
       "G-STILL: unchanged, or the pair book moved by its archive's own restarts alone")
    t0_ = 1794391200
    rec = lambda a, b: {"start_ns": int(a * 1e9), "end_ns": int(b * 1e9), "waited_s": 1.5}
    ok(transfer_summary([rec(t0_ + 15, t0_ + 20), rec(t0_ + 14, t0_ + 20), rec(t0_ + 580, t0_ + 591),
                         rec(t0_ + 580, t0_ + 905)]) == (4, 1, 2, 6.0),
       "a transfer's place: started at second 15 to 590 of its window, ended in it by 590")
    ok(tag_reading("a" * 40, None, "a" * 40) and not tag_reading("a" * 40, "b" * 40, "a" * 40) and
       not tag_reading("b" * 40, None, "a" * 40) and not tag_reading(None, None, "a" * 40),
       "G-TAG: a lightweight tag at the instrument's commit")
    gf = geo_fields({"blocked": True, "ip": "192.0.2.7", "country": "PL", "region": "14"})
    ok(gf == {"blocked": True, "country": "PL", "region": "14", "keys": ["blocked", "country", "ip", "region"]} and
       "192.0.2.7" not in json.dumps(gf) and geo_fields(None) is None and geo_fields([1]) is None,
       "the geoblock reply: blocked, country and region printed, the address never")
    ok(reclaimable(WORK) and not reclaimable("/tmp") and not reclaimable("/root/tz43-work") and
       not reclaimable("/tmp/x/" + "0" * 8 + "-0000-0000-0000-" + "0" * 12),
       "reclaim: this TZ's tree, or a UUID directory beside a btc-5m-twap session's, and nothing else")
    # the store's names
    d0 = FIRST_D0
    ok(classify(d0, "select.0.json") == "select" and classify(d0, "select.12.replies.jsonl.gz") == "select" and
       classify(d0, "%d.0.slot.json" % (d0 + 900)) == "slot" and
       classify(d0, "%d.1.rewards.jsonl.gz" % (d0 + 85500)) == "rewards" and
       classify(d0, "%d.0.stream.jsonl.gz" % d0) == "stream" and classify(d0, "runtime.jsonl") == "other" and
       classify(d0, "select.0.json.tmp") == "other" and classify(d0, "x") == "other" and
       fails(lambda: classify(d0, "%d.0.slot.json" % (d0 + DAY))) and
       fails(lambda: classify(d0, "%d.0.slot.json" % (d0 + 450))),
       "a day's names: selections, slot records and polls are members; streams and every other name are not; a slot "
       "of another day or off the 900 s grid is a failed assert")
    txt = "\n".join("| `%s` | %d | `%s` |" % row for row in TZ43_FILES[:33])
    ok(literal_rows_missing(txt) == [TZ43_FILES[33][0]] and literal_rows_missing(txt + "\n| `set.json` | 6175 | `%s` |"
                                                                                % TZ43_FILES[33][2]) == [],
       "each literal is found only as TZ-43's report prints its row")
    # a synthetic store: one day, its members, a stream and a stray name
    store, outd, outd2 = os.path.join(tmp, "store"), os.path.join(tmp, "out"), os.path.join(tmp, "out2")
    for p in (outd, outd2):
        os.makedirs(p)
    ddir = os.path.join(store, str(d0))
    os.makedirs(ddir)
    def gz_lines(recs):
        return gzip.compress("".join(json.dumps(r) + "\n" for r in recs).encode("utf-8"), mtime=0)

    page = "<html><span id=cf-footer-ip>203.0.113.7</span></html>"
    served = [{"status": 200, "raw": json.dumps({"data": [{"condition_id": "0x01"}]})}, {"status": None, "raw": ""},
              {"status": 200, "raw": "[]"}, {"status": 503, "raw": None}]
    ok(all(body_reason(r) is None for r in served) and body_reason({"status": 200}) is None and
       body_reason({"status": 502, "raw": page}) == "a body under status 502" and
       body_reason({"status": None, "raw": page}) == "a body under status of no number" and
       body_reason({"status": 200, "raw": page}) == "a status-200 body that is not JSON" and
       body_reason({"status": 200, "raw": "7"}) == "a status-200 body that is not a JSON document" and
       body_reason({"status": 200, "raw": 7}) == "a body that is not text" and body_reason([1]) == "not a record",
       "a stored reply's body is published only where the venue served it as a JSON document under status 200")
    blobs = {"select.0.json": b'{"day": 1}\n', "select.0.replies.jsonl.gz": gz_lines(served * 300),
             "%d.0.slot.json" % (d0 + 41400): b'{"S": 1}\n', "%d.0.rewards.jsonl.gz" % (d0 + 41400): gz_lines(served),
             "%d.1.slot.json" % (d0 + 46800): b'{"S": 2}\n',
             "%d.1.rewards.jsonl.gz" % (d0 + 46800): gz_lines(served[:1])}
    held_back = {"%d.0.rewards.jsonl.gz" % (d0 + 42300): gz_lines(served + [{"status": 502, "raw": page}]),
                 "%d.0.rewards.jsonl.gz" % (d0 + 43200): gz_lines([{"status": 200, "raw": page}]),
                 "%d.0.rewards.jsonl.gz" % (d0 + 44100): gz_lines(served * 50)[:-9],
                 "select.1.replies.jsonl.gz": b"no gzip stream at all\n" + gz_lines(served)}
    others = {"%d.0.stream.jsonl.gz" % (d0 + 41400): b"STREAM-BYTES" * 100, "notes.txt": b"OTHER-BYTES"}
    for k, v in list(blobs.items()) + list(held_back.items()) + list(others.items()):
        with open(os.path.join(ddir, k), "wb") as fh:
            fh.write(v)
    why = {k: withhold_reason(os.path.join(ddir, k)) for k in sorted(held_back)}
    ok(all(withhold_reason(os.path.join(ddir, k)) is None for k in blobs if k.endswith(SCANNED)) and
       [why[k] for k in sorted(held_back)] == ["line 5: a body under status 502",
                                                "line 1: a status-200 body that is not JSON",
                                                "not a whole gzip file: EOFError",
                                                "not a whole gzip file: BadGzipFile"] and
       not any("203.0.113.7" in w or "cf-footer-ip" in w for w in why.values()),
       "a file of replies is withheld by its first line that carries another body, or where it is no whole gzip file, "
       "and the reason names a line's number, never its content")
    ok(day_budget(0) == UNIT_BASE_S == 30 and day_budget(1) == 31 and day_budget(16300000) == 63 and
       day_budget(DAY_MAX_BYTES) == 430 <= IDLE[1] - IDLE[0] and SCAN_RATE == 500000,
       "a day's unit is held for 30 s and its members' bytes at 500,000 a second, 430 s at the day's bound")
    e1, s1 = pack_day(store, d0, outd, freef=lambda: DISK_FLOOR + 10 ** 7)
    e2, s2 = pack_day(store, d0, outd2, freef=lambda: DISK_FLOOR + 10 ** 7)
    e3, s3 = pack_day(store, d0, outd, freef=lambda: DISK_FLOOR + 10 ** 7)
    with open(os.path.join(outd, ARCHIVE_FMT % d0), "rb") as fh:
        tar_bytes = fh.read()
    with tarfile.open(os.path.join(outd, ARCHIVE_FMT % d0)) as tf:
        got = {m.name: (m.mtime, m.uid, m.gid, m.mode, m.isreg(), tf.extractfile(m).read()) for m in tf.getmembers()}
    ok(s1 == s2 == "wrote" and s3 == "unchanged" and e1["sha256"] == e2["sha256"] == e3["sha256"] and
       e1 == e3 and len(tar_bytes) == e1["bytes"] and sha256_bytes(tar_bytes) == e1["sha256"] and
       not os.path.exists(os.path.join(outd, ARCHIVE_FMT % d0 + ".part")),
       "a day's archive: the same bytes from two trees and from a second run, written once, no part left")
    ok(sorted(got) == sorted("%d/%s" % (d0, k) for k in blobs) and
       all(got["%d/%s" % (d0, k)][5] == v for k, v in blobs.items()) and
       all(g[:5] == (d0, 0, 0, 0o644, True) for g in got.values()) and
       [r["name"] for r in e1["members"]] == sorted("%d/%s" % (d0, k) for k in blobs) and
       all(r["sha256"] == sha256_bytes(blobs[r["name"].split("/", 1)[1]]) and
           r["bytes"] == len(blobs[r["name"].split("/", 1)[1]]) for r in e1["members"]),
       "every member stored verbatim under <D0>/<name>, in name order, its mtime D0, mode 644, owner 0, and its "
       "bytes and SHA-256 in the manifest's entry")
    ok(b"STREAM-BYTES" not in tar_bytes and b"OTHER-BYTES" not in tar_bytes and
       e1["counts"] == {"select": 3, "slot": 2, "rewards": 5, "stream": 1, "other": 1} and
       sorted((x["kind"], x["name"], x["bytes"]) for x in e1["excluded"]) ==
       [("other", "notes.txt", 11), ("stream", "%d.0.stream.jsonl.gz" % (d0 + 41400), 1200)],
       "the stream and the stray name are listed by their bytes and never stored")
    ok(e1["members_n"] == len(blobs) == 6 and e1["scanned_n"] == 7 and e1["withheld_n"] == 4 and
       e1["member_bytes"] == sum(len(v) for v in blobs.values()) and
       e1["withheld_bytes"] == sum(len(v) for v in held_back.values()) and
       [(w["name"], w["bytes"], w["reason"]) for w in e1["withheld"]] ==
       [(k, len(held_back[k]), why[k]) for k in sorted(held_back)] and
       not any(("%d/%s" % (d0, k)) in got for k in held_back) and
       not any(v in tar_bytes for v in held_back.values()),
       "a withheld file is in no archive: the entry names it by its bytes and its reason, and counts the files scanned")
    ok(fails(lambda: pack_day(store, d0, outd2, freef=lambda: DISK_FLOOR)) and
       fails(lambda: pack_day(store, d0 + DAY, outd2, freef=lambda: DISK_FLOOR + 10 ** 7)),
       "a day BLOCKS where its archive would leave free space under the floor, and where its directory is absent")
    # the sources and the set, on synthetic files
    srcd = os.path.join(tmp, "forensics")
    os.makedirs(srcd)
    fake = []
    for i, p in enumerate(("fetch/1793404800.json", "set.json")):
        data = ("synthetic %d\n" % i).encode("utf-8")
        with open(os.path.join(srcd, forensic_name(p)), "wb") as fh:
            fh.write(data)
        fake.append((p, len(data), sha256_bytes(data)))
    rows = check_sources(srcd, tuple(fake))
    with open(os.path.join(srcd, forensic_name("set.json")), "ab") as fh:
        fh.write(b"!")
    ok([r["asset"] for r in rows] == ["tz43-fetch-1793404800.json", "tz43-set.json"] and
       [r["source"] for r in rows] == ["tz43-work--fetch--1793404800.json", "tz43-work--set.json"] and
       fails(lambda: check_sources(srcd, tuple(fake))),
       "G-SOURCE: each file equal to its row, and one byte more is a BLOCK")
    sdoc = set_doc([e1], rows, 99, "f" * 64)
    ok(sdoc["assets_n"] == 4 and [x["asset"] for x in sdoc["assets"]] == [ARCHIVE_FMT % d0,
                                                                         "tz43-fetch-1793404800.json",
                                                                         "tz43-set.json", MANIFEST] and
       tz27.store_path(UPLOAD_ROOT, sdoc["assets"][0]) == os.path.join(OUT, ARCHIVE_FMT % d0) and
       tz27.store_path(UPLOAD_ROOT, sdoc["assets"][1]) == os.path.join(FORENSICS, "tz43-work--fetch--1793404800.json")
       and sdoc["bytes_total"] == e1["bytes"] + rows[0]["bytes"] + rows[1]["bytes"] + 99,
       "the set: the archives, TZ-43's files from the forensic store and the manifest, each found by TZ-27's "
       "store_path")
    mdoc = manifest_doc("c" * 40, "f" * 64, [e1], rows, "e" * 64)
    ok(tz27.json_bytes(mdoc) == tz27.json_bytes(manifest_doc("c" * 40, "f" * 64, [e1], rows, "e" * 64)) and
       mdoc["reserve_from_D0"] == RESERVE_D0 and mdoc["tz43"]["report"] == TZ43_REPORT,
       "the manifest: the same bytes from the same inputs")
    # the loopback GitHub: TZ-27's own stand-in, our client, our set
    for k in [k for k in list(os.environ) if k.lower() in ("http_proxy", "https_proxy", "all_proxy", "no_proxy")]:
        del os.environ[k]
    tok = "ghp_" + "Ab3" * 12
    Fake = tz27._FakeGitHub
    Fake.releases.clear()
    Fake.assets.clear()
    Fake.hits.clear()
    Fake.refuse_once.clear()
    Fake.omit_digest[0] = False
    Fake.token = tok
    bodies = []
    orig_post = Fake.do_POST

    def do_post(handler):
        if handler.path.endswith("/releases"):
            n_ = int(handler.headers.get("Content-Length") or 0)
            raw_ = handler.rfile.read(n_)
            bodies.append(json.loads(raw_))
            import io
            handler.rfile = io.BytesIO(raw_)
        return orig_post(handler)

    Fake.do_POST = do_post
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Fake)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    sep = ":" + "//"
    lb = "http" + sep + "127.0.0.1:%d" % srv.server_address[1]
    Fake.web = lb
    try:
        root = os.path.join(tmp, "up")
        os.makedirs(os.path.join(root, "a"))
        files = {"one.tar": os.urandom(3000), "tz43-set.json": b'{"x": 1}\n', MANIFEST: b"{}\n"}
        assets = []
        for name, data in files.items():
            with open(os.path.join(root, "a", name), "wb") as fh:
                fh.write(data)
            assets.append({"T": "a", "file": name, "asset": name, "bytes": len(data), "sha256": sha256_bytes(data)})
        doc = {"tag": TAG, "assets": assets, "assets_n": 3, "bytes_total": sum(x["bytes"] for x in assets)}
        trs, logs = [], []
        nowait = lambda budget: (time.time(), 0.0)
        gh = Gh44(token=tok, record=trs.append, held=nowait, commit="c" * 40, api=lb, uploads=lb, web=lb)
        gh.gap_s = 0.0
        rel = gh.create_release(TAG, *release_text(doc, "c" * 40))
        sent, held_n = tz27.upload_set(gh, rel, doc, root, logs.append, wait_min=0)
        anon = Gh44(token=None, record=trs.append, held=nowait, api=lb, uploads=lb, web=lb)
        anon.sizes = {x["asset"]: x["bytes"] for x in assets}
        rel2, vrows, missing, extra = tz27.verify_release(anon, TAG, doc)
        checks = tz27.release_reading(rel2, TAG, vrows, missing, extra)
        ok(bodies and bodies[-1]["tag_name"] == TAG and bodies[-1]["target_commitish"] == "c" * 40 and
           bodies[-1]["draft"] is False and bodies[-1]["make_latest"] == "false" and sent == 3 and held_n == 0 and
           all(checks.values()) and len(vrows) == 3 and all(r["download_ok"] for r in vrows),
           "loopback: the Release on the tag at the commit, three assets sent, and every one proved by the API's "
           "record and a full download with no token")
        ok(all(h[2] == tz27.UA for h in Fake.hits) and
           all(h[3] is None for h in Fake.hits if "/releases/download/" in h[1] or h[1].startswith("/blob/")) and
           len([t for t in trs if t["kind"] == "upload"]) == 3 and
           len([t for t in trs if t["kind"] == "download"]) == 3 and all(t["ok"] for t in trs),
           "every request under TZ-27's agent, every read with no token, every transfer held and recorded")
        sent2, held2 = tz27.upload_set(gh, rel, doc, root, logs.append, wait_min=0)
        aid = [a for a, x in Fake.assets.items() if x["name"] == "one.tar"][0]
        Fake.assets[aid]["data"] = b"x" + Fake.assets[aid]["data"][1:]
        rel3, vrows3, m3, x3 = tz27.verify_release(anon, TAG, doc)
        checks3 = tz27.release_reading(rel3, TAG, vrows3, m3, x3)
        ok(sent2 == 0 and held2 == 3 and not checks3["every download the set's bytes and SHA-256"] and
           not all(checks3.values()),
           "a second upload holds all three; a changed byte served is a failed download")
    finally:
        Fake.do_POST = orig_post
        srv.shutdown()
        srv.server_close()
    shutil.rmtree(tmp)
    ok(not os.path.exists(tmp) and not REFUSED, "the temporary tree removed; no open, listing, request or process "
                                               "refused by this file's hook")
    out("SELFTEST PASS: %d checks" % n[0])


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except GuardError as exc:
        out("refused: %s" % exc)
        raise
