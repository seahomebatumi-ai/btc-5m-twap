#!/usr/bin/env python3
"""TZ-49 - the live host, TZ-48 corrected by map section 7 items 181 to 183: the server in Sofia reached from the
capture host over SSH, root's password login turned off first, the venue's geoblock read over IPv4 alone, IPv4 alone
carried by this process, the host's own swap adopted and its system journal bounded, and the venue's network path and
latency, its memory and its disk read from it before any key exists. The live host is named by its host name's first
label and by its SSH host key, the key pinned at TZ-47's first connection.

On the capture host, from /root/tz49-work, under /root/tz04a-env:
    fingerprint       map section 0 against the primary checkout
    number            CANON hard rule 2: of the number TZ-49, this TZ's file alone under CryptoTZ/, no report
    refs              origin's refs by kind; no branch of this TZ yet
    room              free space of /var/lib and the reward book's stream files by their directory entries alone,
                      and the margin over its stream floor and PEAK (map section 7 item 175); no threshold
    methods LABEL     the authentication methods the live host's sshd offers root, read from outside, before or
                      after B-SSH; after it G-SSH's K6, exit 4 on FAIL
    scratch OWN       the UUID directories beside this session's own, each named live or earlier
    reclaim TREE...   section 9: the work tree's files into the forensic store; an earlier session's directory
                      checked reclaimable
On the live host, from /root/tz49-work, under its system python3:
    host LABEL        the live host gate and the host's facts, before or after B-CONFIGURE; G-SPEC, exit 4 on FAIL
    geoblock          G-GEO: the venue's geoblock read from this host's address over IPv4 alone, IPv6's state
                      printed beside it; exit 1 BLOCKED where blocked or unread
    files             B-SSH's and B-CONFIGURE's files and B-SSH itself into files/, from this file's constants
    sshd              G-SSH's K1 to K5 after B-SSH: the drop-in and sshd's configuration in force; exit 4 on FAIL
    net               G-NET: the CLOB's root and time over HTTPS and its market websocket's handshake; exit 4 on FAIL
    latency           G-LAT: the time to the first byte of the CLOB's /time over one kept connection; exit 4 on FAIL
                      or UNDECIDABLE
    disk              the root file system's write rate with fsync, and its fsync latency; no threshold
    verify            G-SWAP and G-LOG after B-CONFIGURE; exit 4 on FAIL
On either host:
    selftest          every rule of this file, on literals, temporary trees under the work tree and loopback servers

IPv4 alone, in this process (map section 7 item 181): every socket it opens is AF_INET, every name is resolved in
AF_INET alone, and its audit hook refuses an AF_INET6 socket and a lookup in any other family - no IPv6 socket is
opened by any mode. No mode places, signs or cancels an order, holds or reads a key of any venue, or makes an
authenticated request. No mode prints an address of either host: of the geoblock's reply it prints blocked, country,
region and whether the address the venue saw is the connection's own; of IPv6 its counts and classes. No mode opens a
file of a capture's store or of the advisor's credentials. The standard library alone.

Written for CryptoTZ/TZ-49-live-host-ipv4-keys.md. The TZ is the specification.
"""

import base64
import datetime
import hashlib
import http.client
import http.server
import json
import os
import re
import resource
import shutil
import socket
import ssl
import subprocess
import sys
import threading
import time

if not __debug__:
    sys.stderr.write("tz49: refuses to run with asserts disabled (-O); every check is an assert\n")
    raise SystemExit(2)

PYFILE = "tz49-live-host.py"

# ---- the TZ's constants: none of them is measured by this run -----------------------------------------------

MAP_REVISION = "2026-11-19-a"
ANCHORS = {"A1": "229a944f2d51", "A2": "6c5089330629",
           "A3": "0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable",
           "A4": "6ac6e10aeabc", "A5": "0f6c90451cbd", "A6": "729f0bcdbee3"}
ANCHOR_FILES = {"A2": "research/twap-divergence.py", "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
                "A5": "research/recorder/recorder.py", "A6": "research/pfair.py"}
MAP_ROWS = {"frozen": 62, "tracked": 2, "reported": 1}
ROW = re.compile(r"^\| `([^`]+)` \| ([0-9,]+|—) \| ([0-9,]+|—) \| (frozen|tracked|reported) \| "
                 r"(?:`([0-9a-f]{64})`|[^|]*) \|$", re.M)
ANCHOR_ROW = re.compile(r"^\| `(A[0-9])` — [^|]*\| `([^`]+)` \|$", re.M)
NUMBER = "TZ-49-"
OWN_TZ = "CryptoTZ/TZ-49-live-host-ipv4-keys.md"
BRANCH = "tz-49-live-host-ipv4-keys"

PRIMARY = "/root/btc-5m-twap"
WORK = "/root/tz49-work"
WT = WORK + "/wt"
TMP = WORK + "/selftest-tmp"
FILES = WORK + "/files"
FORENSICS = "/root/btc-forensics"
RB = "/var/lib/btc-rewardbook"
RB_ARCHIVE_SVC = "btc-rewardbook-archive.service"
ARCHIVE_READS, ARCHIVE_WAIT_S = 30, 60
CAPTURE_MARK = "/var/lib/btc-recorder"     # map section 6, host identity: on the capture host alone
PROTECTED = ("/var/lib/btc-recorder", "/var/lib/btc-chainbook", "/var/lib/btc-pairbook", RB,
             "/var/lib/btc-rewardbook-archive", "/var/lib/btc-pairbook-archive", "/var/lib/adv3-bot", "/etc/adv3-bot")
LIVE_HOSTNAME = "vs-2348"                  # the host name's first label; the rest is its provider's domain
LIVE_HOST_KEY = ("ssh-ed25519", "SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw")   # TZ-47 report section 2.2
LIVE_ALIAS = "live-host"                    # root's ~/.ssh/config alias on the capture host; it alone holds the address
HOST_KEY_DIR = "/etc/ssh"                   # its host keys' public halves, ssh_host_*_key.pub
CAPTURE_DISK = "/var/lib"
LIVE_DISK = "/"
IPV4 = re.compile(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}")

UA = "btc-5m-twap-tz49"
HEADERS = (("User-Agent", UA), ("Accept", "application/json"))
GEO_HOST, GEO_PATH = "polymarket.com", "/api/geoblock"
CLOB_HOST, OK_PATH, TIME_PATH = "clob.polymarket.com", "/", "/time"
WS_HOST, WS_PATH = "ws-subscriptions-clob.polymarket.com", "/ws/market"
WS_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
TIMEOUT_S, READ_MAX = 10, 65536
TRIES, TRY_GAP_S = 3, 30
EDGE_N, EDGE_GAP_S, EDGE_TIMEOUT_S = 60, 0.5, 2
LAT_WARM, LAT_N, LAT_GAP_S, LAT_BUDGET_S = 5, 600, 0.75, 540
LAT_VALID_MIN = 570          # G-LAT reads UNDECIDABLE below 95 in 100 valid replies
TTFB_MAX_NS = 100000000      # G-LAT: twice the replays' one-way latency of 50 ms
ORIGIN_CACHE = ("DYNAMIC", "BYPASS", "MISS", "EXPIRED")    # cf-cache-status values of a reply the origin served

SPEC_MEM_MIN = 1800000000    # G-SPEC: nine tenths of the 2 GB sold
SPEC_DISK_MIN = 18000000000  # ... and of the 20 GB sold

SWAP_PATH = "/swap.img"                     # the host's own swap file, adopted: no swap file is written (item 182)
SWAP_UNIT = "swap.img.swap"                 # the unit systemd's fstab generator makes of its fstab line
SWAP_BYTES = 1073741824
FSTAB_FIELDS = ("/swap.img", "none", "swap", "sw", "0", "0")
FSTAB_SOURCE = "/etc/fstab"
SWAPPINESS = 10
JOURNALD_DROPIN = "/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf"
SYSCTL_DROPIN = "/etc/sysctl.d/zz-btc-5m-twap-swap.conf"
SSHD_DROPIN = "/etc/ssh/sshd_config.d/00-btc-5m-twap.conf"
JOURNALD_TEXT = ("# btc-5m-twap, TZ-49: the live host's system journal, bounded. Installed byte for byte as\n"
                 "# /etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf from research/tz49-live-host.py; "
                 "named to sort\n"
                 "# after every other drop-in, cap.conf and syslog.conf among them, so its values win. Sizes in "
                 "journald's\n"
                 "# units of 1,024 bytes.\n"
                 "[Journal]\n"
                 "Storage=persistent\n"
                 "SystemMaxUse=512M\n"
                 "SystemKeepFree=2G\n"
                 "SystemMaxFileSize=64M\n"
                 "RuntimeMaxUse=64M\n"
                 "ForwardToSyslog=no\n")
SYSCTL_TEXT = ("# btc-5m-twap, TZ-49: the live host swaps only under memory pressure. Installed byte for byte as\n"
               "# /etc/sysctl.d/zz-btc-5m-twap-swap.conf from research/tz49-live-host.py; named to sort last.\n"
               "vm.swappiness = 10\n")
SSHD_TEXT = ("# btc-5m-twap, TZ-49: root by key alone. Installed byte for byte as\n"
             "# /etc/ssh/sshd_config.d/00-btc-5m-twap.conf from research/tz49-live-host.py; named to sort\n"
             "# before every other drop-in, because sshd keeps the first value it reads of a keyword.\n"
             "PasswordAuthentication no\n"
             "KbdInteractiveAuthentication no\n"
             "PermitRootLogin prohibit-password\n")
JOURNALD_SHA256 = "91c7364c9ee1dec70c1651e7c976546d86a46f95b39ea8dd369ef83589439200"
SYSCTL_SHA256 = "3b31709b0c1c7026c71013150868a982296a36daa7b3635fd9eabe4929331a04"
SSHD_SHA256 = "94fff8f1f044b31d393eecf24700dabc5b7316c70a37d0f3984cbc5957563624"
BSSH_TEXT = r"""# B-SSH, TZ-49 section 0.7: root by key alone, under a guard.
# Written by research/tz49-live-host.py files; run on the live host as bash /root/tz49-work/files/b-ssh.sh.
# Every step is gated on the one before it.
cd /root/tz49-work || exit 1
{
  date -u +%FT%T.%NZ
  D=/etc/ssh/sshd_config.d/00-btc-5m-twap.conf
  ls -la /etc/ssh/sshd_config.d
  grep -nE '^[[:space:]]*(Include|PermitRootLogin|PasswordAuthentication|KbdInteractiveAuthentication)[[:space:]]' \
    /etc/ssh/sshd_config
  test ! -e "$D" &&
    printf '%s  %s\n' 94fff8f1f044b31d393eecf24700dabc5b7316c70a37d0f3984cbc5957563624 files/sshd.conf |
      sha256sum -c --strict - &&
    systemd-run --quiet --collect --unit=tz49-ssh-revert --on-active=300 --timer-property=AccuracySec=1s \
      /bin/sh -c "rm -f $D; systemctl reload ssh.service" &&
    echo "guard armed: 300 s from now the drop-in is removed and sshd reloaded, unless a new connection stops it" &&
    install -m 0644 files/sshd.conf "$D" &&
    sshd -t &&
    { ! systemctl is-active --quiet ssh.service || systemctl reload ssh.service; } &&
    sshd -T > sshd-T.txt &&
    grep -E '^(port|permitrootlogin|pubkeyauthentication|passwordauthentication|kbdinteractiveauthentication) ' \
      sshd-T.txt &&
    grep -qx 'passwordauthentication no' sshd-T.txt &&
    grep -qx 'kbdinteractiveauthentication no' sshd-T.txt &&
    grep -qx 'pubkeyauthentication yes' sshd-T.txt
  r=$?
  if [ "$r" != 0 ] && systemctl is-active --quiet tz49-ssh-revert.timer; then
    rm -f "$D"
    systemctl reload ssh.service
    systemctl stop tz49-ssh-revert.timer
    echo "reverted at once: the drop-in removed, sshd reloaded, the guard stopped"
  fi
  echo "B-SSH exit=$r"
} >> logs/43-B-SSH.log 2>&1
tail -n 30 logs/43-B-SSH.log
"""
BSSH_SHA256 = "906a6cb2685aea2575eff6538906aa02a21d9591a6d9aa3505f84b644693ede1"
SSHD_IN_FORCE = (("passwordauthentication", "no"), ("kbdinteractiveauthentication", "no"),
                 ("permitrootlogin", "without-password"), ("pubkeyauthentication", "yes"))
#   sshd -T prints prohibit-password as without-password: the first name OpenSSH 9.6's table holds for the value
METHODS_ONLY = ["publickey"]
JOURNAL_MAX_USE = 536870912                 # SystemMaxUse=512M, as journald's own MAX_USE field carries it
USAGE_ID = "ec387f577b844b8fa948f33cad9a75e6"   # journald's usage message, SD_MESSAGE_JOURNAL_USAGE in systemd 255
SYSLOG = "/var/log/syslog"
PROBE_TAG = "tz49-probe"
PROBE_WAIT_S = 10
RTF_UP, RTF_REJECT = 0x0001, 0x0200         # the route flags of /proc/net/ipv6_route

DISK_TEST_BYTES, DISK_CHUNK = 268435456, 1048576
FSYNC_N, FSYNC_BYTES = 200, 4096

STREAM_FLOOR = 7300000000    # research/tz33-reward-book-capture.py line 190
PEAK = 445535636             # fourteen slots of 31,823,974 bytes (TZ-46; map section 6)
MARGIN_WATCH = 1000000000    # map section 7 item 175
SESSION_WRITES = 50000000    # this session's writes on the capture host, at most
CAPTURE_FLOOR = STREAM_FLOOR + PEAK + SESSION_WRITES                       # 7,795,535,636
JOURNAL_KEEP_FREE = 2147483648                                             # SystemKeepFree=2G, DISK_KEEP_FREE
LIVE_WORK_MAX = 100000000
LIVE_FLOOR = DISK_TEST_BYTES + JOURNAL_KEEP_FREE + LIVE_WORK_MAX            # 2,515,919,104: no swap file written
RECLAIM_FLOOR = STREAM_FLOOR + 100000000
MEM_FLOOR = 72439812         # MemAvailable at a mode's start: twice 36,219,906, the host peak modelled (section 0.4)
MEM_READS, MEM_WAIT_S = 5, 60

UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
DAY_RE = re.compile(r"[0-9]{10}")
RB_STREAM_RE = re.compile(r"([0-9]{10})\.([0-9]+)\.stream\.jsonl\.gz")
STAMP_RE = re.compile(r"[A-Z][a-z]{2} ([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}) UTC")
HEADER_RE = re.compile(r"# (/[^ ]+)")
SETTING_RE = re.compile(r"([A-Za-z]+)=(.*)")
SHOW_ENV = {"TZ": "UTC", "LC_ALL": "C", "SYSTEMD_COLORS": "0", "SYSTEMD_PAGER": ""}
LIVE_S = 60

# ---- the audit hook: TZ-49 section 2 as a pure function, and the hook that applies it -------------------------

MODE = [None]
REFUSED = []
RESOLVED = set()
COUNTS = {"lookups": 0, "requests": 0, "handshakes": 0, "tcp connects": 0}
NET = {"geoblock": (GEO_HOST,), "net": (CLOB_HOST, WS_HOST), "latency": (CLOB_HOST,), "selftest": ("127.0.0.1",)}
EXECS = {"number": ("git",), "refs": ("git",), "room": ("systemctl",), "scratch": ("stat",), "reclaim": ("git", "stat"),
         "methods": ("ssh",), "host": ("systemctl", "timedatectl", "journalctl", "sshd", "systemd-analyze"),
         "sshd": ("sshd",), "verify": ("systemctl", "journalctl", "logger", "systemd-analyze")}
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
CHANGE_EVENTS = ("os.remove", "os.rename", "os.rmdir", "os.mkdir", "os.truncate", "os.chmod", "os.chown",
                 "os.utime", "os.link", "os.symlink", "shutil.rmtree", "shutil.copyfile")
HOOKED = ("open", "os.listdir", "os.scandir", "socket.__new__", "socket.getaddrinfo", "socket.connect",
          "subprocess.Popen") + CHANGE_EVENTS


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


def policy(mode, event, args):
    """None where TZ-49 section 2 allows the event in this mode; otherwise why it is refused. Pure but for the
    addresses this process resolved from an allowed name. IPv4 alone (map section 7 item 181): a socket of any
    family but AF_INET, a lookup in any family but AF_INET and a connection to anything but an IPv4 address are
    refused in every mode."""
    if event == "socket.__new__":
        fam = args[1] if len(args) > 1 else None
        return None if fam == socket.AF_INET else "a socket of family %r: IPv4 alone" % (fam,)
    if event == "socket.getaddrinfo":
        host = args[0] if args else None
        if isinstance(host, bytes):
            host = host.decode("ascii", "replace")
        fam = args[2] if len(args) > 2 else None
        if fam != socket.AF_INET:
            return "a lookup of %r in family %r: IPv4 alone" % (host, fam)
        return None if host in RESOLVED or host in NET.get(mode, ()) else "a lookup of %r" % (host,)
    if event == "socket.connect":
        addr = args[1] if len(args) > 1 else None
        ok = isinstance(addr, tuple) and len(addr) == 2 and isinstance(addr[0], str) \
            and IPV4.fullmatch(addr[0]) is not None and (addr[0] in RESOLVED or addr[0] in NET.get(mode, ()))
        return None if ok else "a connection to %r" % (addr,)
    if event == "subprocess.Popen":
        exe = args[0] if args and args[0] else (args[1][0] if len(args) > 1 and args[1] else None)
        name = os.path.basename(os.fsdecode(exe)) if exe is not None else None
        return None if name in EXECS.get(mode, ()) else "running %r" % (name,)
    p = _path(args[0]) if args else None
    if p is None:
        return None
    if event == "open":
        wm, fl = (args[1] if len(args) > 1 else None), (args[2] if len(args) > 2 else None)
        if any(_under(p, r) for r in PROTECTED):
            return "an open under a capture's store or the advisor's credentials"
        if _writing(wm, fl):
            if _under(p, FORENSICS):
                return None if mode == "reclaim" and _exclusive(wm, fl) else "a write into the forensic store"
            if not _under(p, WORK):
                return "a write outside the work tree"
        return None
    if event in ("os.listdir", "os.scandir"):
        if _under(p, RB):
            return None if mode == "room" else "a listing of the reward book's store"
        return "a listing under a capture's store" if any(_under(p, r) for r in PROTECTED) else None
    paths = [p]
    if event in ("os.rename", "os.link", "os.symlink", "shutil.copyfile") and len(args) > 1:
        paths.append(_path(args[1]))
    for q in paths:
        if q is not None and not _under(q, WORK):
            return "a change outside the work tree"
    return None


def _audit(event, args):
    if event not in HOOKED:
        return
    why = policy(MODE[0], event, args)
    if why is not None:
        REFUSED.append((event, MODE[0]))
        raise GuardError("%s refused in mode %s: %s" % (event, MODE[0], why))


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


def read_text(path, default=None):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return default


def meminfo(text):
    """The fields of /proc/meminfo in bytes. Pure."""
    found = {}
    for line in text.split("\n"):
        f = line.split()
        if len(f) >= 2 and f[0].endswith(":") and f[1].isdigit():
            found[f[0][:-1]] = int(f[1]) * (1024 if len(f) > 2 and f[2] == "kB" else 1)
    return found


def mem_available():
    return meminfo(read_text("/proc/meminfo", ""))["MemAvailable"]


def fs_bytes(path):
    """Total, available and free bytes of the file system holding `path`."""
    st = os.statvfs(path)
    return st.f_blocks * st.f_frsize, st.f_bavail * st.f_frsize, st.f_bfree * st.f_frsize


def floors(disk, disk_floor, read=mem_available, sleep=time.sleep, statf=fs_bytes):
    """At a mode's start: MemAvailable read up to five times 60 s apart, the first at or above MEM_FLOOR passing;
    the available bytes of `disk` at or above disk_floor."""
    for k in range(1, MEM_READS + 1):
        m = read()
        out("MemAvailable read %d: %d bytes, floor %d" % (k, m, MEM_FLOOR))
        if m >= MEM_FLOOR:
            break
        assert k < MEM_READS, "BLOCKED: MemAvailable below %d at %d reads" % (MEM_FLOOR, MEM_READS)
        sleep(MEM_WAIT_S)
    avail = statf(disk)[1]
    out("available on %s: %d bytes, floor %d" % (disk, avail, disk_floor))
    assert avail >= disk_floor, "BLOCKED: %d bytes available on %s, below %d" % (avail, disk, disk_floor)
    return avail


def run(argv, timeout=20):
    """A command under TZ=UTC and the C locale: (exit, stdout, stderr)."""
    cp = subprocess.run(argv, capture_output=True, text=True, timeout=timeout, env=dict(os.environ, **SHOW_ENV))
    return cp.returncode, cp.stdout, cp.stderr


def show(unit, props):
    """systemctl show: {property: value}."""
    args = ["systemctl", "show", unit]
    for p in props:
        args += ["-p", p]
    rc, so, se = run(args)
    assert rc == 0, "systemctl show %s: %s" % (unit, se.strip())
    kv = {}
    for line in so.split("\n"):
        if "=" in line:
            k, v = line.split("=", 1)
            kv[k] = v
    return kv


def stamp_of(text):
    """An epoch from systemctl's own stamp printed under TZ=UTC; None where it prints none."""
    m = STAMP_RE.fullmatch((text or "").strip())
    if m is None:
        return None
    dt = datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc)
    return int(dt.timestamp())


def git(*args, tree=PRIMARY):
    rc, so, se = run(["git", "-C", tree] + list(args), timeout=120)
    assert rc == 0, "git %s: %s" % (" ".join(args), se.strip()[:300])
    return so.strip()


def nearest_rank(vals, p):
    """The p-th percentile of sorted values by nearest rank: the ceil(p n / 100)-th smallest. Pure."""
    assert vals and 0 < p <= 100
    k = -(-p * len(vals) // 100)
    return vals[max(k, 1) - 1]


def ms(ns):
    return "%.3f" % (ns / 1e6)


def record(kind, obj):
    out("RECORD %s %s" % (kind, json.dumps(obj, sort_keys=True, separators=(",", ":"))))


def is_capture_host():
    return os.path.isdir(CAPTURE_MARK)


def first_label(name):
    """A host name to its first dot: vs-2348 of vs-2348 and of vs-2348.<a provider's domain>. Pure."""
    return name.split(".", 1)[0]


def short_hostname():
    """This host's name, its first label alone: no mode prints its provider's domain (TZ-47's report, section 3
    item 1)."""
    return first_label(socket.gethostname())


def host_keys():
    """This host's SSH host keys by type and fingerprint, from every ssh_host_*_key.pub file of /etc/ssh, sorted."""
    names = sorted(os.listdir(HOST_KEY_DIR)) if os.path.isdir(HOST_KEY_DIR) else []
    found = []
    for n in names:
        if n.startswith("ssh_host_") and n.endswith("_key.pub"):
            found += key_fingerprints(read_text(os.path.join(HOST_KEY_DIR, n), "") or "")
    return sorted(found)


def is_live_host():
    return (short_hostname() == LIVE_HOSTNAME and LIVE_HOST_KEY in host_keys()
            and not os.path.exists(CAPTURE_MARK))

# ---- the network: IPv4 alone, every request with this TZ's agent --------------------------------------------


def resolve(host, port=443):
    """The IPv4 addresses of `host`, sorted; each is the only address a later connection may use."""
    infos = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
    addrs = sorted({ai[4][0] for ai in infos})
    RESOLVED.update(addrs)
    COUNTS["lookups"] += 1
    return addrs


def connect4(addr, port, timeout):
    """A TCP connection to the IPv4 address `addr`: its socket AF_INET by construction, and no lookup made."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(timeout)
        s.connect((addr, port))
    except BaseException:
        s.close()
        raise
    return s


def https_conn(host, addr, timeout=TIMEOUT_S, context=None):
    """An HTTPS connection to `host`, its certificate checked against the name, its socket to `addr` alone."""
    c = http.client.HTTPSConnection(host, 443, timeout=timeout, context=context or ssl.create_default_context())
    c._create_connection = lambda address, timeout=None, source_address=None: connect4(addr, address[1], timeout)
    return c


def plain_conn(addr, port, timeout):
    """An HTTP connection to the IPv4 address `addr` - the self-test's loopback server - through connect4."""
    c = http.client.HTTPConnection(addr, port, timeout=timeout)
    c._create_connection = lambda address, timeout=None, source_address=None: connect4(addr, address[1], timeout)
    return c


def err_of(exc):
    """An error as printed: its type, errno and the C library's message - never an address. Pure."""
    no, msg = getattr(exc, "errno", None), getattr(exc, "strerror", None)
    return "%s errno %s: %s" % (type(exc).__name__, no, msg) if no is not None else type(exc).__name__


def request(conn, path):
    """One GET of `path` over `conn`, every header this TZ's: (status, headers, body, time to the first byte in ns,
    fresh, the connection's own source address). Fresh: the exchange opened the connection, so its time holds the
    handshakes. A body longer than READ_MAX closes the connection."""
    fresh = conn.sock is None
    t0 = time.perf_counter_ns()
    conn.request("GET", path, headers=dict(HEADERS))
    src = conn.sock.getsockname()[0] if conn.sock is not None else None
    resp = conn.getresponse()
    t1 = time.perf_counter_ns()
    body = resp.read(READ_MAX)
    if not resp.isclosed():
        conn.close()
    COUNTS["requests"] += 1
    return resp.status, {k.lower(): v for k, v in resp.getheaders()}, body, t1 - t0, fresh, src


def pop_of(ray):
    """The Cloudflare data centre a reply came through: the IATA code after the cf-ray header's last dash. Pure."""
    code = ray.rsplit("-", 1)[1] if isinstance(ray, str) and "-" in ray else ""
    return code if re.fullmatch(r"[A-Z]{3}", code) else ""


def edge_probe(addr, port, n, gap_s, clock=time.perf_counter_ns, sleep=time.sleep):
    """The time of n TCP handshakes with `addr`, gap_s apart, each socket closed at once; None for a failed one."""
    times = []
    for i in range(n):
        if i:
            sleep(gap_s)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(EDGE_TIMEOUT_S)
        t0 = clock()
        try:
            s.connect((addr, port))
            times.append(clock() - t0)
        except OSError:
            times.append(None)
        finally:
            s.close()
        COUNTS["tcp connects"] += 1
    return times


def probe(make_conn, path, warm, n, gap_s, budget_s, clock=time.perf_counter_ns, wall=time.time, sleep=time.sleep):
    """`path` requested warm + n times over one kept connection, one every gap_s from the first, none begun after
    budget_s: each sample its index, warm and fresh flags, status, time to the first byte, the Cloudflare data
    centre, the cache status, whether the body is ten digits, the venue's seconds and this host's at the reply."""
    conn = make_conn()
    samples = []
    start = clock()
    try:
        for i in range(warm + n):
            now = clock()
            if now - start > budget_s * 1e9:
                break
            due = start + int(i * gap_s * 1e9)
            if due > now:
                sleep((due - now) / 1e9)
            s = {"i": i, "warm": i < warm, "fresh": conn.sock is None, "status": None, "ttfb_ns": None, "pop": "",
                 "cache": "", "body_ok": False, "venue_s": None, "host_s": None, "error": None}
            try:
                status, hdrs, body, ttfb, fresh, _src = request(conn, path)
                s.update(status=status, ttfb_ns=ttfb, fresh=fresh, pop=pop_of(hdrs.get("cf-ray")),
                         cache=(hdrs.get("cf-cache-status") or "").upper())
                txt = body.decode("ascii", "replace").strip()
                if re.fullmatch(r"[0-9]{10}", txt):
                    s.update(body_ok=True, venue_s=int(txt), host_s=int(wall()))
            except (OSError, http.client.HTTPException) as exc:
                s["error"] = type(exc).__name__
                conn.close()
            samples.append(s)
    finally:
        conn.close()
    return samples


def ws_key():
    return base64.b64encode(os.urandom(16)).decode("ascii")


def ws_accept(key):
    return base64.b64encode(hashlib.sha1((key + WS_GUID).encode("ascii")).digest()).decode("ascii")


def ws_request(host, path, key):
    return ("GET %s HTTP/1.1\r\nHost: %s\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: %s\r\n"
            "Sec-WebSocket-Version: 13\r\nUser-Agent: %s\r\n\r\n" % (path, host, key, UA)).encode("ascii")


def ws_head(sock, cap=16384):
    """The status code and the headers of a reply's head read from `sock`."""
    buf = b""
    while b"\r\n\r\n" not in buf and len(buf) < cap:
        chunk = sock.recv(4096)
        if not chunk:
            break
        buf += chunk
    lines = buf.split(b"\r\n\r\n", 1)[0].decode("latin-1").split("\r\n")
    m = re.match(r"HTTP/1\.[01] ([0-9]{3})", lines[0]) if lines else None
    hdrs = {}
    for ln in lines[1:]:
        if ":" in ln:
            k, v = ln.split(":", 1)
            hdrs[k.strip().lower()] = v.strip()
    return (int(m.group(1)) if m else None), hdrs


def ws_handshake(sock, host, path):
    """A websocket opening handshake over a connected socket, closed at once with status 1000 where it succeeds:
    (status, whether the reply's accept key is the one this key asks for, the reply's headers). No subscription."""
    key = ws_key()
    sock.sendall(ws_request(host, path, key))
    code, hdrs = ws_head(sock)
    ok = code == 101 and hdrs.get("sec-websocket-accept") == ws_accept(key) \
        and hdrs.get("upgrade", "").lower() == "websocket"
    if code == 101:
        mask, payload = os.urandom(4), (1000).to_bytes(2, "big")
        sock.sendall(bytes([0x88, 0x80 | len(payload)]) + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(payload)))
    COUNTS["handshakes"] += 1
    return code, ok, hdrs

# ---- the readings: pure -------------------------------------------------------------------------------------


def number_reading(names, own):
    """NUMBER, CANON hard rule 2: CryptoTZ/ holds this TZ's file and no other of its number; CryptoReports/ no report
    of it. Pure."""
    tz = [n for n in names if n.startswith("CryptoTZ/" + NUMBER)]
    rp = [n for n in names if n.startswith("CryptoReports/" + NUMBER)]
    return tz == [own] and not rp, tz, rp


def refs_reading(text):
    """origin's refs counted by kind, and whether this TZ's branch is among them. Pure."""
    kinds, branch = {}, False
    for ln in text.split("\n"):
        if "\t" not in ln:
            continue
        ref = ln.split("\t", 1)[1].strip()
        branch = branch or ref == "refs/heads/" + BRANCH
        if ref in ("HEAD", "refs/heads/main"):
            k = ref
        elif ref.startswith("refs/heads/tz-"):
            k = "refs/heads/tz-*"
        elif ref.startswith("refs/pull/"):
            k = "refs/pull/*/" + ref.rsplit("/", 1)[1]
        elif ref.startswith("refs/tags/pairbook-streams-") or ref.startswith("refs/tags/rewardbook-streams-"):
            k = ref.split("-streams-", 1)[0] + "-streams-*" + ("^{}" if ref.endswith("^{}") else "")
        else:
            k = ref
        kinds[k] = kinds.get(k, 0) + 1
    return kinds, branch


def room_reading(avail, streams):
    """The room - available bytes and the reward book's stream files - and its margin over the stream floor and
    PEAK (map section 7 item 175). Pure."""
    room = avail + streams
    return room, room - STREAM_FLOOR - PEAK


def geo_fields(doc):
    """What may be printed of the venue's reply: blocked, country and region, and its keys' names - never the
    address it carries. Pure."""
    if not isinstance(doc, dict):
        return None
    return {"blocked": doc.get("blocked"), "country": doc.get("country"), "region": doc.get("region"),
            "keys": sorted(str(k) for k in doc)}


def geo_reading(status, doc):
    """One geoblock read: UNREAD unless status 200 and a reply whose blocked is a boolean and whose country is two
    capital letters; else BLOCKED where blocked is true, PASS where it is false. Pure."""
    f = geo_fields(doc)
    if status != 200 or f is None or not isinstance(f["blocked"], bool) \
            or not (isinstance(f["country"], str) and re.fullmatch(r"[A-Z]{2}", f["country"])):
        return "UNREAD"
    return "BLOCKED" if f["blocked"] else "PASS"


def v6_state(if_inet6, routes):
    """IPv6's state on this host, read from the kernel's own tables and never an address: the global addresses of
    /proc/net/if_inet6 by count and flags, and the default routes of /proc/net/ipv6_route by count, those usable -
    up and not a reject route - by count and device, and their next hops by class. Pure."""
    glob = [f for f in (ln.split() for ln in if_inet6.split("\n")) if len(f) >= 6 and f[3] == "00"]
    dflt = [f for f in (ln.split() for ln in routes.split("\n"))
            if len(f) >= 10 and f[0] == "0" * 32 and f[1] == "00" and re.fullmatch(r"[0-9a-fA-F]{8}", f[8])]
    usable = [f for f in dflt if int(f[8], 16) & RTF_UP and not int(f[8], 16) & RTF_REJECT]

    def hop(h):
        if set(h) == {"0"}:
            return "none"
        return "link-local" if h[:3].lower() in ("fe8", "fe9", "fea", "feb") else "other"

    return {"global addresses": len(glob), "their flags": sorted(f[4] for f in glob), "default routes": len(dflt),
            "usable": len(usable), "usable via": sorted("%s, next hop %s" % (f[9], hop(f[4])) for f in usable)}


def valid_sample(s):
    return (not s["warm"] and not s["fresh"] and s["error"] is None and s["status"] == 200 and s["body_ok"]
            and s["pop"] != "" and s["cache"] in ORIGIN_CACHE)


def lat_reading(samples, valid_min=LAT_VALID_MIN, ttfb_max_ns=TTFB_MAX_NS):
    """G-LAT. Pure. Counted: every sample after the warm-up. Valid: not fresh, no error, status 200, the body the
    venue's ten digits, a named Cloudflare data centre and a cache status the origin served. UNDECIDABLE below
    valid_min valid samples; else PASS where the nearest-rank median time to the first byte is at most
    ttfb_max_ns, FAIL above it."""
    counted = [s for s in samples if not s["warm"]]
    valid = [s for s in counted if valid_sample(s)]
    st = {"counted": len(counted), "valid": len(valid),
          "fresh": sum(1 for s in counted if s["fresh"]), "errors": sum(1 for s in counted if s["error"]),
          "non-200": sum(1 for s in counted if s["status"] not in (None, 200)),
          "cache other": sum(1 for s in counted if s["status"] == 200 and s["cache"] not in ORIGIN_CACHE)}
    t = sorted(s["ttfb_ns"] for s in valid)
    if t:
        for p in (5, 50, 95, 99):
            st["p%d" % p] = nearest_rank(t, p)
        st["max"] = t[-1]
        h = len(valid) // 2
        st["p50 first half"] = nearest_rank(sorted(s["ttfb_ns"] for s in valid[:h]), 50) if h else None
        st["p50 second half"] = nearest_rank(sorted(s["ttfb_ns"] for s in valid[h:]), 50)
        offs = [s["venue_s"] - s["host_s"] for s in valid]
        st["venue less host, s"] = (min(offs), max(offs))
    if len(valid) < valid_min:
        return "UNDECIDABLE", st
    return ("PASS" if st["p50"] <= ttfb_max_ns else "FAIL"), st


def net_reading(results):
    """G-NET: every check of `results` passed. Pure."""
    return bool(results) and all(results.values())


def spec_reading(mem_total, disk_total):
    """G-SPEC's two checks against what was sold. Pure."""
    checks = {"MemTotal at least %d" % SPEC_MEM_MIN: mem_total >= SPEC_MEM_MIN,
              "the root file system at least %d" % SPEC_DISK_MIN: disk_total >= SPEC_DISK_MIN}
    return all(checks.values()), checks


def live_gate(hostname, osrel, pyver, capture_paths, keys):
    """The live host gate's five checks: `hostname` the first label of the host's name, `keys` its SSH host keys by
    type and fingerprint. Pure."""
    checks = {"LH1 hostname %s" % LIVE_HOSTNAME: hostname == LIVE_HOSTNAME,
              "LH2 Ubuntu 24.04": osrel.get("ID") == "ubuntu" and osrel.get("VERSION_ID") == "24.04",
              "LH3 Python 3.12": tuple(pyver[:2]) == (3, 12),
              "LH4 not the capture host": not capture_paths,
              "LH5 the host key pinned at TZ-47's first connection": LIVE_HOST_KEY in keys}
    return all(checks.values()), checks


def os_release(text):
    found = {}
    for ln in text.split("\n"):
        if "=" in ln and not ln.startswith("#"):
            k, v = ln.split("=", 1)
            found[k.strip()] = v.strip().strip('"')
    return found


def proc_swaps(text):
    """The entries of /proc/swaps: (name, type, size KiB, used KiB). Pure."""
    rows = []
    for ln in text.split("\n")[1:]:
        f = ln.split()
        if len(f) >= 5 and f[2].isdigit() and f[3].isdigit():
            rows.append((f[0], f[1], int(f[2]), int(f[3])))
    return rows


def fstab_active(text):
    """The fields of every line of an fstab that is neither blank nor a comment. Pure."""
    return [tuple(ln.split()) for ln in text.split("\n") if ln.strip() and not ln.lstrip().startswith("#")]


def swap_reading(st, swaps, fstab_rows, swap_total, swappiness, sysctl, page, unit):
    """G-SWAP's seven checks on the host's own swap file. `st` its (regular, size, mode, uid) or None; `swaps`
    /proc/swaps' entries; `swap_total` SwapTotal in bytes; `sysctl` the drop-in's (SHA-256, mode) or None; `unit`
    systemctl show of the swap unit systemd made of the fstab line. Pure."""
    one = len(swaps) == 1
    checks = {"S1 %s, %d bytes, 0600, root's" % (SWAP_PATH, SWAP_BYTES):
                  st is not None and st == (True, SWAP_BYTES, 0o600, 0),
              "S2 one active swap, this file": one and swaps[0][0] == SWAP_PATH and swaps[0][1] == "file"
                  and swaps[0][2] * 1024 + page == SWAP_BYTES,
              "S3 one fstab line": [r for r in fstab_rows if r[:1] == (SWAP_PATH,) or r[2:3] == ("swap",)]
                  == [FSTAB_FIELDS],
              "S4 SwapTotal": one and swap_total == swaps[0][2] * 1024,
              "S5 vm.swappiness %d" % SWAPPINESS: swappiness == SWAPPINESS,
              "S6 the sysctl file": sysctl == (SYSCTL_SHA256, 0o644),
              "S7 %s active, made of %s" % (SWAP_UNIT, FSTAB_SOURCE): unit.get("ActiveState") == "active"
                  and unit.get("SourcePath") == FSTAB_SOURCE}
    return all(checks.values()), checks


def journal_usage(text, pid):
    """journald's own account of its limits: of the usage messages its process `pid` logged for the System
    Journal, in `journalctl -o json` text, the last one's instant in microseconds, MAX_USE, DISK_KEEP_FREE and
    message; None where it logged none. systemd 255 logs one at every start of journald, after "Journal started".
    Pure."""
    found = None
    for ln in text.split("\n"):
        try:
            e = json.loads(ln)
        except ValueError:
            continue
        if isinstance(e, dict) and e.get("MESSAGE_ID") == USAGE_ID and e.get("JOURNAL_NAME") == "System Journal" \
                and e.get("_PID") == str(pid):
            try:
                found = {"realtime_us": int(e["__REALTIME_TIMESTAMP"]), "max_use": int(e["MAX_USE"]),
                         "keep_free": int(e["DISK_KEEP_FREE"]), "message": e.get("MESSAGE")}
            except (KeyError, TypeError, ValueError):
                continue
    return found


def settings(text):
    """The Key=value lines of a configuration text, in order; comments, sections and blank lines left out. Pure."""
    return [tuple(m.groups()) for m in (SETTING_RE.fullmatch(ln.strip()) for ln in text.split("\n")) if m]


def effective_config(text):
    """`systemd-analyze cat-config` text: each key's last value and the file it comes from, files in the order
    journald reads them. A file's header is a line '# ' and its absolute path, alone. Pure."""
    found, current = {}, None
    for ln in text.split("\n"):
        m = HEADER_RE.fullmatch(ln.rstrip())
        if m:
            current = m.group(1)
            continue
        m = SETTING_RE.fullmatch(ln.strip())
        if m:
            found[m.group(1)] = (m.group(2), current)
    return found


def log_reading(dropin, dropin_mtime_us, usage, in_journal, in_syslog, rsyslog, sock, effective):
    """G-LOG's six checks. `dropin` the journald file's (SHA-256, mode) or None, `dropin_mtime_us` its change in
    microseconds; `usage` journal_usage's reading; `rsyslog` and `sock` systemctl show of rsyslog.service and
    syslog.socket; `effective` effective_config's reading. Pure."""
    off = (rsyslog.get("LoadState") == "not-found" or (
        rsyslog.get("ActiveState") == "inactive" and rsyslog.get("UnitFileState") in ("disabled", "masked"))) \
        and (sock.get("LoadState") == "not-found" or sock.get("ActiveState") == "inactive")
    checks = {"G1 the journald file": dropin == (JOURNALD_SHA256, 0o644),
              "G2 the running journald started after it": usage is not None and dropin_mtime_us is not None
                  and usage["realtime_us"] >= dropin_mtime_us,
              "G3 journald's own MAX_USE %d and DISK_KEEP_FREE %d" % (JOURNAL_MAX_USE, JOURNAL_KEEP_FREE):
                  usage is not None and usage["max_use"] == JOURNAL_MAX_USE
                  and usage["keep_free"] == JOURNAL_KEEP_FREE,
              "G4 the probe in the journal alone": in_journal is True and in_syslog is False,
              "G5 rsyslog and its socket off": off,
              "G6 every key of the journald file in force from it": all(
                  effective.get(k) == (v, JOURNALD_DROPIN) for k, v in settings(JOURNALD_TEXT))}
    return all(checks.values()), checks


def sshd_effective(text):
    """`sshd -T` text: each keyword and its value, the last line of a keyword kept. Pure."""
    found = {}
    for ln in text.split("\n"):
        f = ln.strip().split(None, 1)
        if len(f) == 2:
            found[f[0].lower()] = f[1].strip()
    return found


def ssh_reading(dropin, effective):
    """G-SSH's K1 to K5, on the live host: `dropin` the sshd drop-in's (SHA-256, mode) or None; `effective`
    sshd_effective's reading of `sshd -T`. Pure."""
    checks = {"K1 the sshd drop-in": dropin == (SSHD_SHA256, 0o644)}
    for i, (k, v) in enumerate(SSHD_IN_FORCE, 2):
        checks["K%d %s %s" % (i, k, v)] = effective.get(k) == v
    return all(checks.values()), checks


METHODS_RE = re.compile(r"Authentications that can continue: ([A-Za-z0-9@.,_-]+)")


def methods_of(text):
    """The lists of authentication methods an sshd offered, from `ssh -v` text: each list once, sorted - nothing
    else of the text, which carries the address. Pure."""
    return sorted(set(METHODS_RE.findall(text)))


def addr_class(h):
    """The class of a /proc/net address: any, loopback or other - never the address. Pure."""
    if set(h) == {"0"}:
        return "any"
    if len(h) == 8:
        return "loopback" if bytes.fromhex(h)[3] == 127 else "other"
    if h == "00000000000000000000000001000000":
        return "loopback"
    if len(h) == 32 and h[:24] == "0000000000000000FFFF0000":
        return "loopback" if bytes.fromhex(h[24:])[3] == 127 else "other"
    return "other"


def listening(text, proto):
    """The listening TCP sockets, or the bound UDP sockets, of a /proc/net table: (proto, class, port, inode). Pure."""
    rows = []
    for ln in text.split("\n")[1:]:
        f = ln.split()
        if len(f) < 10 or ":" not in f[1]:
            continue
        if f[3] != ("0A" if proto.startswith("tcp") else "07"):
            continue
        a, port = f[1].split(":")
        rows.append((proto, addr_class(a), int(port, 16), int(f[9])))
    return sorted(set(rows))


def key_fingerprints(text):
    """The type and SHA256 fingerprint of each key line of an authorized_keys file, in ssh-keygen's form; never a
    key's comment. Pure."""
    found = []
    for ln in text.split("\n"):
        f = ln.split()
        for i, w in enumerate(f[:-1]):
            if w.startswith("ssh-") or w.startswith("ecdsa-") or w.startswith("sk-"):
                try:
                    blob = base64.b64decode(f[i + 1], validate=True)
                except ValueError:
                    break
                found.append((w, "SHA256:" + base64.b64encode(hashlib.sha256(blob).digest()).decode().rstrip("=")))
                break
    return found


def reclaimable(tree):
    if tree == WORK:
        return True
    return (tree.startswith("/tmp/") and os.path.isdir(tree) and not os.path.islink(tree)
            and UUID.fullmatch(os.path.basename(tree)) is not None
            and "btc-5m-twap" in os.path.basename(os.path.dirname(tree)))

# ---- the capture host's modes -------------------------------------------------------------------------------


def mode_fingerprint():
    assert is_capture_host(), "BLOCKED: fingerprint runs on the capture host"
    with open(os.path.join(PRIMARY, "SYSTEM-MAP.md"), "rb") as fh:
        raw = fh.read()
    txt = raw.decode("utf-8")
    rev = re.findall(r"^\*\*Revision string:\*\* `([^`]+)`$", txt, re.M)
    assert rev == [MAP_REVISION], "BLOCKED: map revision %r, required %s" % (rev, MAP_REVISION)
    found = dict(ANCHOR_ROW.findall(txt))
    assert found == ANCHORS, "BLOCKED: anchors %r" % found
    for k, rel in sorted(ANCHOR_FILES.items()):
        h = sha256_file(os.path.join(PRIMARY, rel))[0][:12]
        assert h == ANCHORS[k], "BLOCKED: re-derived %s %s, the map %s" % (k, h, ANCHORS[k])
        out("re-derived %s %s sha256[:12] %s equal" % (k, rel, h))
    rows = ROW.findall(txt)
    states = {k: sum(1 for r in rows if r[3] == k) for k in MAP_ROWS}
    assert states == MAP_ROWS and len(rows) == sum(MAP_ROWS.values()), "BLOCKED: rows %r" % states
    for path, lines, nbytes, state, sha in rows:
        with open(os.path.join(PRIMARY, path), "rb") as fh:
            blob = fh.read()
        got = (blob.count(b"\n"), len(blob), sha256_bytes(blob))
        if state == "frozen":
            want = (int(lines.replace(",", "")), int(nbytes.replace(",", "")), sha)
            assert got == want, "BLOCKED: frozen row %s: %r, the map %r" % (path, got, want)
        out("%-48s %6d lines %8d bytes %s %s%s" % (path, got[0], got[1], got[2], state,
                                                  " equal" if state == "frozen" else ""))
    out("SYSTEM-MAP.md %d lines %d bytes sha256 %s" % (raw.count(b"\n"), len(raw), sha256_bytes(raw)))
    out("FINGERPRINT PASS: revision %s; anchors 6 of 6, 4 re-derived; rows %d: frozen %d of %d equal, tracked %d, "
        "reported %d" % (MAP_REVISION, len(rows), states["frozen"], MAP_ROWS["frozen"], states["tracked"],
                         states["reported"]))
    return 0


def mode_number():
    assert is_capture_host(), "BLOCKED: number runs on the capture host"
    names = git("ls-tree", "--name-only", "origin/main", "--", "CryptoTZ/", "CryptoReports/").split("\n")
    ok, tz, rp = number_reading(names, OWN_TZ)
    out("origin/main %s: %d paths under CryptoTZ/ and CryptoReports/; of the number %s: %s and %s" % (
        git("rev-parse", "origin/main"), len(names), NUMBER, tz, rp))
    out("NUMBER %s" % ("PASS - 2 of 2" if ok else "FAIL"))
    assert ok, "BLOCKED: of the number %s, CryptoTZ/ holds %s and CryptoReports/ %s" % (NUMBER, tz, rp)
    return 0


def mode_refs():
    assert is_capture_host(), "BLOCKED: refs runs on the capture host"
    text = git("ls-remote", "origin")
    kinds, branch = refs_reading(text)
    for ln in text.split("\n"):
        if ln.endswith("\tHEAD") or ln.endswith("\trefs/heads/main"):
            out("REF %s" % ln)
    for k in sorted(kinds):
        out("REFS %-40s %d" % (k, kinds[k]))
    out("REFS %d lines; refs/heads/%s %s" % (sum(kinds.values()), BRANCH, "PRESENT" if branch else "absent"))
    assert not branch, "BLOCKED: refs/heads/%s exists on origin already" % BRANCH
    return 0


def rb_streams(root=RB):
    """The reward book's stream files by their directory entries alone: (bytes, files, day directories)."""
    total = files = 0
    with os.scandir(root) as it:
        days = sorted(e.name for e in it if e.is_dir(follow_symlinks=False) and DAY_RE.fullmatch(e.name))
    for d in days:
        with os.scandir(os.path.join(root, d)) as it:
            for e in it:
                if e.is_file(follow_symlinks=False) and RB_STREAM_RE.fullmatch(e.name):
                    total += e.stat(follow_symlinks=False).st_size
                    files += 1
    return total, files, len(days)


def mode_room(sleep=time.sleep):
    """The room, read while the reward book's archive is not running (map section 3, the units): its service read
    up to thirty times 60 s apart; still running at the last read, the room is not read."""
    assert is_capture_host(), "BLOCKED: room runs on the capture host"
    for k in range(1, ARCHIVE_READS + 1):
        state = show(RB_ARCHIVE_SVC, ["ActiveState"]).get("ActiveState")
        out("%s read %d: %s" % (RB_ARCHIVE_SVC, k, state))
        if state == "inactive":
            break
        if k == ARCHIVE_READS:
            out("ROOM not read: the reward book's archive was running at %d reads" % ARCHIVE_READS)
            return 0
        sleep(ARCHIVE_WAIT_S)
    avail = floors(CAPTURE_DISK, CAPTURE_FLOOR)
    streams, files, days = rb_streams()
    room, margin = room_reading(avail, streams)
    out("ROOM: %d bytes available on %s; the reward book's stream files %d bytes in %d files under %d day "
        "directories; the room %d; its margin over STREAM_FLOOR %d and PEAK %d: %d bytes%s" % (
            avail, CAPTURE_DISK, streams, files, days, room, STREAM_FLOOR, PEAK, margin,
            "" if margin >= MARGIN_WATCH else " - BELOW %d (map section 7 item 175)" % MARGIN_WATCH))
    return 0


def mode_methods(label):
    """The authentication methods the live host's sshd offers root, read from outside by one connection that offers
    no key and can answer no prompt: printed before B-SSH, G-SSH's K6 after it. Of ssh's text, which carries the
    address, nothing is printed but the methods."""
    assert label in ("before", "after"), "methods takes before or after"
    assert is_capture_host(), "BLOCKED: methods runs on the capture host"
    try:
        rc, so, se = run(["ssh", "-T", "-v", "-o", "BatchMode=yes", "-o", "ConnectTimeout=20", "-o",
                          "PubkeyAuthentication=no", "-o", "PreferredAuthentications=password,keyboard-interactive",
                          "-o", "NumberOfPasswordPrompts=0", LIVE_ALIAS, "true"], timeout=60)
    except subprocess.TimeoutExpired:
        rc, so, se = None, "", ""
    found = methods_of(so + "\n" + se)
    out("METHODS %s B-SSH: the methods the live host's sshd offers root, from outside: %s; ssh exit %s" % (
        label, found, "none, past 60 s" if rc is None else rc))
    record("methods-" + label, {"exit": rc, "methods": found})
    if label == "before":
        return 0
    ok = found == METHODS_ONLY
    out("G-SSH K6 %s alone, from outside: %s" % (",".join(METHODS_ONLY), "PASS" if ok else "FAIL"))
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
    rc, so, se = run(["stat", "-c", "%W", path])
    assert rc == 0, se
    return int(so.strip())


def mode_scratch(own):
    """Lists the UUID directories beside `own`, this session's, and names each live or earlier."""
    assert is_capture_host(), "BLOCKED: scratch runs on the capture host"
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


def pristine(tree):
    rc, so, _se = run(["git", "-C", tree, "status", "--porcelain", "--ignored"])
    assert rc == 0 and so == "", "reclaim: %s holds %r" % (tree, so[:400])
    head = git("rev-parse", "HEAD", tree=tree)
    up = git("rev-parse", "@{u}", tree=tree)
    assert up == head, "reclaim: %s is at %s, its upstream at %s" % (tree, head, up)
    out("reclaim: %s skipped: no file but its HEAD's, and HEAD %s is its upstream's" % (tree, head))


def tree_count(root):
    n = 0
    for _d, _s, files in os.walk(root):
        n += len(files)
    return n


def mode_reclaim(trees):
    """The work tree's every file but the worktree's into the forensic store, each by exclusive create and its
    SHA-256 checked; an earlier session's directory checked reclaimable and not live, nothing of it copied."""
    assert is_capture_host(), "BLOCKED: reclaim runs on the capture host"
    assert trees and all(reclaimable(t) for t in trees), "reclaim: %r" % (trees,)
    procs = proc_start_times()
    for t in trees:
        if t != WORK:
            b = birth(t)
            owner = [p for p, s, _a in procs if s - 1 <= b <= s + LIVE_S]
            assert not owner, "reclaim: %s belongs to the running process %s" % (t, owner)
    before = tree_count(FORENSICS)
    considered = copied = held = 0
    for tree in trees:
        if tree != WORK:
            n = sum(len(f) for _d, _s, f in os.walk(tree))
            out("reclaim: %s, an earlier session's directory of %d files: nothing of it is kept" % (tree, n))
            continue
        if os.path.isdir(WT):
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
                dest = os.path.join(FORENSICS, os.path.basename(tree) + "--" + rel.replace("/", "--"))
                if os.path.exists(dest):
                    assert sha256_file(dest)[0] == h, "reclaim: %s exists with another sha256" % dest
                    held += 1
                    out("R held   %s %s" % (h, dest))
                    continue
                size, avail = os.path.getsize(path), fs_bytes(FORENSICS)[1]
                assert avail - size >= RECLAIM_FLOOR, "BLOCKED: reclaim: %d bytes available, %s is %d" % (
                    avail, path, size)
                with open(path, "rb") as src, open(dest, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest)[0] == h, "reclaim: %s did not copy whole" % dest
                copied += 1
                out("R copied %s %s" % (h, dest))
    after = tree_count(FORENSICS)
    assert after == before + copied, "reclaim: store %d, expected %d" % (after, before + copied)
    out("RECLAIM PASS: %d files considered, %d copied, %d already held; the forensic store %d -> %d files" % (
        considered, copied, held, before, after))
    return 0

# ---- the live host's modes ----------------------------------------------------------------------------------


def assert_live():
    assert is_live_host(), "BLOCKED: this mode runs on the live host %s and nowhere else" % LIVE_HOSTNAME


def sysctl_lines():
    """Every line of a sysctl file that sets vm.swappiness, with its file."""
    files = ["/etc/sysctl.conf"]
    for d in ("/etc/sysctl.d", "/run/sysctl.d", "/usr/local/lib/sysctl.d", "/usr/lib/sysctl.d", "/lib/sysctl.d"):
        if os.path.isdir(d) and not os.path.islink(d):
            files += [os.path.join(d, n) for n in sorted(os.listdir(d)) if n.endswith(".conf")]
    found = []
    for f in files:
        for ln in (read_text(f, "") or "").split("\n"):
            s = ln.strip()
            if "swappiness" in s and not s.startswith("#") and not s.startswith(";"):
                found.append("%s: %s" % (f, s))
    return found


def socket_owners():
    """inode -> the name of a process holding the socket, read from /proc/*/fd."""
    owners = {}
    for pid in (p for p in os.listdir("/proc") if p.isdigit()):
        try:
            comm = read_text("/proc/%s/comm" % pid, "?").strip()
            for fd in os.listdir("/proc/%s/fd" % pid):
                link = os.readlink("/proc/%s/fd/%s" % (pid, fd))
                if link.startswith("socket:["):
                    owners.setdefault(int(link[8:-1]), comm)
        except OSError:
            continue
    return owners


def sshd_lines(keys):
    """Every line of sshd's own files that sets one of `keys` or includes other files, with its file and line
    number, in the order sshd reads its main file: what sshd -T would apply, read statically."""
    files = ["/etc/ssh/sshd_config"]
    d = "/etc/ssh/sshd_config.d"
    if os.path.isdir(d):
        files += [os.path.join(d, n) for n in sorted(os.listdir(d)) if n.endswith(".conf")]
    found = []
    for f in files:
        for n, ln in enumerate((read_text(f, "") or "").split("\n"), 1):
            w = ln.strip().split()
            if w and (w[0].lower() in keys or w[0].lower() == "include"):
                found.append("%s:%d: %s" % (f, n, ln.strip()))
    return found


def swap_file_state(path):
    """(regular, size, mode bits, uid) of a file, or None where it is absent."""
    try:
        st = os.lstat(path)
    except OSError:
        return None
    return (os.path.isfile(path) and not os.path.islink(path), st.st_size, st.st_mode & 0o7777, st.st_uid)


def top_rss(n=10):
    rows = []
    for pid in (p for p in os.listdir("/proc") if p.isdigit()):
        st = meminfo(read_text("/proc/%s/status" % pid, "") or "")
        name = [ln.split(None, 1)[1].strip() for ln in (read_text("/proc/%s/status" % pid, "") or "").split("\n")
                if ln.startswith("Name:")]
        if "VmRSS" in st:
            rows.append((st["VmRSS"], int(pid), name[0] if name else "?"))
    return sorted(rows, reverse=True)[:n]


def var_log():
    """/var/log's files: apparent and on-disk bytes, and the eight largest on disk."""
    files, app, disk = [], 0, 0
    for d, _s, names in os.walk("/var/log"):
        for name in names:
            p = os.path.join(d, name)
            try:
                st = os.lstat(p)
            except OSError:
                continue
            app += st.st_size
            disk += st.st_blocks * 512
            files.append((st.st_blocks * 512, os.path.relpath(p, "/var/log")))
    return app, disk, sorted(files, reverse=True)[:8], len(files)


def mode_host(label):
    assert label in ("before", "after"), "host takes before or after"
    osrel = os_release(read_text("/etc/os-release", ""))
    capture = [p for p in (CAPTURE_MARK, PRIMARY) if os.path.exists(p)]
    keys = host_keys()
    ok, checks = live_gate(short_hostname(), osrel, sys.version_info, capture, keys)
    for k, v in checks.items():
        out("%s: %s" % (k, "PASS" if v else "FAIL"))
    out("HOST its SSH host keys: %s" % keys)
    assert ok, "BLOCKED: the live host gate: %s" % [k for k, v in checks.items() if not v]
    if label == "before":
        floors(LIVE_DISK, LIVE_FLOOR)
    mi = meminfo(read_text("/proc/meminfo", ""))
    total, avail, free = fs_bytes(LIVE_DISK)
    vfs = os.statvfs(LIVE_DISK)
    mounts = [ln.split() for ln in read_text("/proc/self/mounts", "").split("\n") if ln.split()[1:2] == ["/"]]
    cpu = [ln.split(":", 1)[1].strip() for ln in read_text("/proc/cpuinfo", "").split("\n")
           if ln.startswith("model name")]
    btime = int([ln for ln in read_text("/proc/stat", "").split("\n") if ln.startswith("btime ")][0].split()[1])
    up = float(read_text("/proc/uptime", "0 0").split()[0])
    u = os.uname()
    out("HOST %s; %s; kernel %s %s; Python %s; processors %d, %s" % (
        short_hostname(), osrel.get("PRETTY_NAME"), u.release, u.machine, sys.version.split()[0],
        os.cpu_count(), cpu[0] if cpu else "?"))
    out("HOST vendor %r, product %r" % ((read_text("/sys/class/dmi/id/sys_vendor", "?") or "?").strip(),
                                        (read_text("/sys/class/dmi/id/product_name", "?") or "?").strip()))
    out("HOST booted %s, up %.0f s" % (utc(btime), up))
    out("MEMORY " + ", ".join("%s %d" % (k, mi.get(k, -1)) for k in (
        "MemTotal", "MemAvailable", "MemFree", "Buffers", "Cached", "SwapTotal", "SwapFree")))
    out("DISK / %s %s: total %d, available %d, free %d bytes; inodes %d, free %d" % (
        mounts[-1][0] if mounts else "?", mounts[-1][2] if mounts else "?", total, avail, free, vfs.f_files,
        vfs.f_favail))
    swaps = proc_swaps(read_text("/proc/swaps", ""))
    sw = swap_file_state(SWAP_PATH)
    out("SWAP /proc/swaps %s; %s (regular, bytes, mode, uid) %s; fstab lines of swap %s" % (
        swaps, SWAP_PATH, sw and (sw[0], sw[1], oct(sw[2]), sw[3]),
        [r for r in fstab_active(read_text("/etc/fstab", "")) if r[2:3] == ("swap",) or r[:1] == (SWAP_PATH,)]))
    out("SWAP %s %s" % (SWAP_UNIT, show(SWAP_UNIT, ["LoadState", "ActiveState", "SubState", "SourcePath"])))
    out("SWAP vm.swappiness %s; set in %s" % (read_text("/proc/sys/vm/swappiness", "?").strip(), sysctl_lines()))
    for d in ("/etc/systemd/journald.conf.d", "/run/systemd/journald.conf.d", "/usr/lib/systemd/journald.conf.d",
              "/usr/local/lib/systemd/journald.conf.d"):
        if os.path.isdir(d):
            out("JOURNALD %s: %s" % (d, sorted(os.listdir(d))))
    out("JOURNALD journald.conf, set: %s" % [ln.strip() for ln in read_text("/etc/systemd/journald.conf", "").split(
        "\n") if ln.strip() and not ln.strip().startswith("#")])
    rc, so, se = run(["systemd-analyze", "cat-config", "systemd/journald.conf"])
    out("JOURNALD in force, by `systemd-analyze cat-config` exit %d: %s" % (rc, effective_config(so)))
    rc, so, se = run(["journalctl", "--disk-usage", "--no-pager"])
    out("JOURNALD disk usage: %s" % (so.strip() or se.strip()))
    app, disk, largest, nfiles = var_log()
    out("LOGS /var/log: %d files, %d bytes apparent, %d on disk; the largest on disk %s" % (nfiles, app, disk,
                                                                                         largest))
    for unit in ("rsyslog.service", "syslog.socket", "systemd-journald.service", "systemd-timesyncd.service",
                 "chrony.service", "ssh.service", "ssh.socket", "unattended-upgrades.service", "apt-daily.timer",
                 "apt-daily-upgrade.timer"):
        kv = show(unit, ["LoadState", "ActiveState", "SubState", "UnitFileState"])
        out("UNIT %s %s" % (unit, kv))
    rc, so, se = run(["timedatectl", "show"])
    out("CLOCK %s" % {k: v for k, v in (ln.split("=", 1) for ln in so.split("\n") if "=" in ln)
                      if k in ("Timezone", "LocalRTC", "NTP", "NTPSynchronized", "CanNTP")})
    rc, so, se = run(["timedatectl", "timesync-status"])
    out("CLOCK timesync-status exit %d: %s" % (rc, " | ".join(ln.strip() for ln in (so or se).split("\n")
                                                              if ln.strip())))
    rc, so, se = run(["sshd", "-T"])
    keep = ("port", "permitrootlogin", "passwordauthentication", "pubkeyauthentication", "kbdinteractiveauthentication")
    out("SSHD -T exit %d: %s%s" % (rc, [ln for ln in so.split("\n") if ln.split(" ", 1)[0] in keep],
                                   "" if rc == 0 else "; " + se.strip()[:200]))
    out("SSHD set in its files, in the order sshd reads them: %s" % sshd_lines(keep))
    out("SSHD authorized keys of root: %s" % key_fingerprints(read_text("/root/.ssh/authorized_keys", "") or ""))
    owners = socket_owners()
    socks = []
    for proto in ("tcp", "tcp6", "udp", "udp6"):
        for p, cls, port, inode in listening(read_text("/proc/net/" + proto, "") or "", proto):
            socks.append("%s %s:%d %s" % (p, cls, port, owners.get(inode, "?")))
    out("SOCKETS listening or bound: %s" % sorted(set(socks)))
    out("NETWORK IPv6, never an address: %s" % v6_state(read_text("/proc/net/if_inet6", "") or "",
                                                        read_text("/proc/net/ipv6_route", "") or ""))
    out("PROCESSES by resident memory: %s" % ["%s %d %d" % (n, pid, rss) for rss, pid, n in top_rss()])
    reboot = []
    for n in sorted(os.listdir("/etc/apt/apt.conf.d")) if os.path.isdir("/etc/apt/apt.conf.d") else []:
        for ln in (read_text(os.path.join("/etc/apt/apt.conf.d", n), "") or "").split("\n"):
            if "Automatic-Reboot" in ln and not ln.strip().startswith("//"):
                reboot.append("%s: %s" % (n, ln.strip()))
    out("UPGRADES Automatic-Reboot set: %s" % (reboot or "nowhere - the package's default"))
    sok, sch = spec_reading(mi.get("MemTotal", 0), total)
    for k, v in sch.items():
        out("G-SPEC %s: %d, %s" % (k, mi.get("MemTotal", 0) if k.startswith("MemTotal") else total,
                                   "PASS" if v else "FAIL"))
    out("G-SPEC %s" % ("PASS: 2 of 2" if sok else "FAIL"))
    record("host-" + label, {"mem_total": mi.get("MemTotal"), "mem_available": mi.get("MemAvailable"),
                             "swap_total": mi.get("SwapTotal"), "disk_total": total, "disk_available": avail,
                             "swaps": swaps, "spec": sok})
    return 0 if sok else 4


def geo_read(sleep=time.sleep):
    """G-GEO over IPv4, the one family this process can open: the first read that is not UNREAD, at most TRIES
    reads TRY_GAP_S apart."""
    r = "UNREAD"
    for k in range(1, TRIES + 1):
        status = doc = own = err = None
        try:
            addrs = resolve(GEO_HOST)
            conn = https_conn(GEO_HOST, addrs[0])
            try:
                status, _h, body, ttfb, _fresh, src = request(conn, GEO_PATH)
            finally:
                conn.close()
            try:
                doc = json.loads(body)
            except ValueError:
                doc = None
            own = isinstance(doc, dict) and src is not None and doc.get("ip") == src
        except (OSError, http.client.HTTPException) as exc:
            err = err_of(exc)
        r = geo_reading(status, doc)
        f = geo_fields(doc)
        out("GEOBLOCK IPv4 read %d: https://%s%s, status %s; blocked %r, country %r, region %r; reply keys %s; the "
            "address the venue saw is this connection's own: %s%s - %s" % (
                k, GEO_HOST, GEO_PATH, status, f and f["blocked"], f and f["country"], f and f["region"],
                f and f["keys"], own, (", " + err) if err else "", r))
        if r != "UNREAD":
            return r
        if k < TRIES:
            sleep(TRY_GAP_S)
    return r


def mode_geoblock():
    """G-GEO over IPv4 alone, and IPv6's state beside it from the kernel's tables: no IPv6 socket is opened, so no
    request of this process can carry an address the venue has not read (map section 7 item 181)."""
    assert_live()
    g = geo_read()
    v6 = v6_state(read_text("/proc/net/if_inet6", "") or "", read_text("/proc/net/ipv6_route", "") or "")
    out("GEOBLOCK IPv6, beside G-GEO and read by no gate - this process opens no IPv6 socket: %s" % v6)
    out("G-GEO %s over IPv4 alone" % g)
    record("geoblock", {"ipv6": v6, "reading": g})
    assert g == "PASS", "BLOCKED: G-GEO %s - the venue %s this address" % (
        g, "blocks" if g == "BLOCKED" else "did not read")
    return 0


def net_try(name, fn, sleep=time.sleep):
    for k in range(1, TRIES + 1):
        try:
            ok, line = fn()
        except (OSError, http.client.HTTPException, ssl.SSLError) as exc:
            ok, line = False, type(exc).__name__
        out("%s read %d: %s - %s" % (name, k, line, "PASS" if ok else "FAIL"))
        if ok:
            return True
        if k < TRIES:
            sleep(TRY_GAP_S)
    return False


def mode_net():
    assert_live()
    clob, ws = resolve(CLOB_HOST), resolve(WS_HOST)
    out("DNS %s IPv4: %s; %s IPv4: %s" % (CLOB_HOST, clob, WS_HOST, ws))

    def root():
        conn = https_conn(CLOB_HOST, clob[0])
        try:
            st, h, body, t, _f, _s = request(conn, OK_PATH)
        finally:
            conn.close()
        pop = pop_of(h.get("cf-ray"))
        return st == 200 and body.strip() == b'"OK"' and pop != "", "GET https://%s%s: status %s, body %r, " \
            "data centre %r, %s ms" % (CLOB_HOST, OK_PATH, st, body[:20], pop, ms(t))

    def tim():
        conn = https_conn(CLOB_HOST, clob[0])
        try:
            st, h, body, t, _f, _s = request(conn, TIME_PATH)
        finally:
            conn.close()
        txt, pop, cache = body.decode("ascii", "replace").strip(), pop_of(h.get("cf-ray")), \
            (h.get("cf-cache-status") or "").upper()
        good = re.fullmatch(r"[0-9]{10}", txt) is not None
        off = (int(txt) - int(time.time())) if good else None
        return st == 200 and good and pop != "" and cache in ORIGIN_CACHE, "GET https://%s%s: status %s, ten " \
            "digits %s, data centre %r, cache %r, the venue's seconds less this host's %s" % (
                CLOB_HOST, TIME_PATH, st, good, pop, cache, off)

    def wsh():
        s = connect4(ws[0], 443, TIMEOUT_S)
        try:
            ss = ssl.create_default_context().wrap_socket(s, server_hostname=WS_HOST)
            try:
                code, good, h = ws_handshake(ss, WS_HOST, WS_PATH)
            finally:
                ss.close()
        finally:
            s.close()
        return good, "wss://%s%s handshake: status %s, accept key %s, data centre %r" % (
            WS_HOST, WS_PATH, code, "valid" if good else "not valid", pop_of(h.get("cf-ray")))

    results = {"N1 the CLOB's root": net_try("N1", root), "N2 the CLOB's time": net_try("N2", tim),
               "N3 the market websocket": net_try("N3", wsh)}
    g = net_reading(results)
    for k, v in results.items():
        out("G-NET %s: %s" % (k, "PASS" if v else "FAIL"))
    out("G-NET %s" % ("PASS: 3 of 3" if g else "FAIL"))
    times = edge_probe(clob[0], 443, EDGE_N, EDGE_GAP_S) if g else []
    ok_t = sorted(t for t in times if t is not None)
    out("EDGE %d TCP handshakes with %s:443, %.1f s apart, after G-NET's PASS alone: %d completed; median %s ms, "
        "p95 %s ms, max %s ms" % (len(times), CLOB_HOST, EDGE_GAP_S, len(ok_t),
                                  ms(nearest_rank(ok_t, 50)) if ok_t else "-",
                                  ms(nearest_rank(ok_t, 95)) if ok_t else "-", ms(ok_t[-1]) if ok_t else "-"))
    record("net", {"edge_ns": times, "results": results, "reading": g})
    return 0 if g else 4


def mode_latency():
    assert_live()
    floors(LIVE_DISK, LIVE_WORK_MAX)
    addr = resolve(CLOB_HOST)[0]
    out("LATENCY https://%s%s over one kept IPv4 connection: %d warm-up and %d counted requests, one every %.2f s, "
        "none begun after %d s" % (CLOB_HOST, TIME_PATH, LAT_WARM, LAT_N, LAT_GAP_S, LAT_BUDGET_S))
    samples = probe(lambda: https_conn(CLOB_HOST, addr), TIME_PATH, LAT_WARM, LAT_N, LAT_GAP_S, LAT_BUDGET_S)
    for s in samples:
        out("S %d %s%s status %s ttfb_us %s pop %s cache %s body %s venue-host %s%s" % (
            s["i"], "warm" if s["warm"] else "count", " fresh" if s["fresh"] else "", s["status"],
            s["ttfb_ns"] // 1000 if s["ttfb_ns"] is not None else "-", s["pop"] or "-", s["cache"] or "-",
            "ok" if s["body_ok"] else "no", (s["venue_s"] - s["host_s"]) if s["body_ok"] else "-",
            (" error " + s["error"]) if s["error"] else ""))
    reading, st = lat_reading(samples)
    pops = {}
    for s in samples:
        if valid_sample(s):
            pops[s["pop"]] = pops.get(s["pop"], 0) + 1
    out("LATENCY counted %d, valid %d (fresh %d, errors %d, non-200 %d, cache not the origin's %d); data centres %s" %
        (st["counted"], st["valid"], st["fresh"], st["errors"], st["non-200"], st["cache other"], pops))
    if st["valid"]:
        out("LATENCY time to the first byte, ms: p5 %s, p50 %s, p95 %s, p99 %s, max %s; p50 of the first half %s, "
            "of the second %s; the venue's seconds less this host's %s" % (
                ms(st["p5"]), ms(st["p50"]), ms(st["p95"]), ms(st["p99"]), ms(st["max"]),
                ms(st["p50 first half"]) if st["p50 first half"] is not None else "-", ms(st["p50 second half"]),
                st["venue less host, s"]))
        out("LATENCY one-way bound, half the median: %s ms, against 50.000 ms" % ms(st["p50"] // 2))
    out("G-LAT %s" % reading)
    record("latency", {"reading": reading, "stats": st})
    return 0 if reading == "PASS" else 4


def write_rate(path, total, chunk, clock=time.perf_counter_ns):
    """The nanoseconds to write `total` bytes of random data in `chunk`s to a new file and fsync it; the file is
    removed."""
    buf = os.urandom(chunk)
    t0 = clock()
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        left = total
        while left > 0:
            left -= os.write(fd, buf[:min(chunk, left)])
        os.fsync(fd)
    finally:
        os.close(fd)
    t1 = clock()
    os.remove(path)
    return t1 - t0


def fsync_times(path, n, size, clock=time.perf_counter_ns):
    """n writes of `size` bytes appended to a new file, each followed by fsync: their nanoseconds; the file removed."""
    buf, times = os.urandom(size), []
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        for _ in range(n):
            t0 = clock()
            assert os.write(fd, buf) == size, "a short write"
            os.fsync(fd)
            times.append(clock() - t0)
    finally:
        os.close(fd)
    os.remove(path)
    return times


def mode_disk():
    assert_live()
    a0 = floors(LIVE_DISK, LIVE_FLOOR)
    ns = write_rate(WORK + "/disk-test.bin", DISK_TEST_BYTES, DISK_CHUNK)
    out("DISK write %d bytes in %d chunks and fsync: %s ms, %d bytes a second" % (
        DISK_TEST_BYTES, DISK_TEST_BYTES // DISK_CHUNK, ms(ns), DISK_TEST_BYTES * 1000000000 // ns))
    t = sorted(fsync_times(WORK + "/fsync-test.bin", FSYNC_N, FSYNC_BYTES))
    out("DISK %d appends of %d bytes, each with fsync: p50 %s ms, p99 %s ms, max %s ms" % (
        FSYNC_N, FSYNC_BYTES, ms(nearest_rank(t, 50)), ms(nearest_rank(t, 99)), ms(t[-1])))
    a1 = fs_bytes(LIVE_DISK)[1]
    out("DISK available before %d, after %d bytes; the test files removed: %s" % (
        a0, a1, not os.path.exists(WORK + "/disk-test.bin") and not os.path.exists(WORK + "/fsync-test.bin")))
    record("disk", {"write_ns": ns, "write_bytes": DISK_TEST_BYTES, "fsync_ns": t})
    return 0


def mode_files():
    assert_live()
    floors(LIVE_DISK, LIVE_FLOOR)
    assert not os.path.exists(FILES), "BLOCKED: %s exists" % FILES
    os.mkdir(FILES)
    for name, text, want in (("sshd.conf", SSHD_TEXT, SSHD_SHA256), ("journald.conf", JOURNALD_TEXT, JOURNALD_SHA256),
                             ("sysctl.conf", SYSCTL_TEXT, SYSCTL_SHA256), ("b-ssh.sh", BSSH_TEXT, BSSH_SHA256)):
        data = text.encode("utf-8")
        assert sha256_bytes(data) == want, "%s is not the text this TZ fixed" % name
        with open(os.path.join(FILES, name), "xb") as fh:
            fh.write(data)
        h, n = sha256_file(os.path.join(FILES, name))
        assert h == want, name
        out("FILES %s %d lines %d bytes sha256 %s" % (name, data.count(b"\n"), n, h))
    return 0


def mode_sshd():
    """G-SSH's K1 to K5 after B-SSH: the drop-in as installed, and the configuration sshd applies, by sshd -T."""
    assert_live()
    dropin = file_state(SSHD_DROPIN)
    rc, so, se = run(["sshd", "-T"])
    eff = sshd_effective(so)
    out("SSHD %s %s; sshd -T exit %d: %s%s" % (
        SSHD_DROPIN, dropin and (dropin[0], oct(dropin[1])), rc, ["%s %s" % (k, eff.get(k)) for k, _v in SSHD_IN_FORCE],
        "" if rc == 0 else "; " + se.strip()[:200]))
    out("SSHD set in its files, in the order sshd reads them: %s" % sshd_lines([k for k, _v in SSHD_IN_FORCE]))
    ok, checks = ssh_reading(dropin, eff if rc == 0 else {})
    for k, v in checks.items():
        out("G-SSH %s: %s" % (k, "PASS" if v else "FAIL"))
    out("G-SSH on the live host %s" % ("PASS: 5 of 5" if ok else "FAIL"))
    record("sshd", {"in force": {k: eff.get(k) for k, _v in SSHD_IN_FORCE}, "reading": ok})
    return 0 if ok else 4


def file_state(path):
    """(SHA-256, mode bits) of a regular file, or None."""
    try:
        st = os.lstat(path)
    except OSError:
        return None
    return (sha256_file(path)[0], st.st_mode & 0o7777) if os.path.isfile(path) and not os.path.islink(path) else None


def syslog_holds(needle, path=SYSLOG, tail=1 << 20):
    """Whether the last `tail` bytes of the syslog file hold `needle`; False where the file is absent."""
    try:
        with open(path, "rb") as fh:
            fh.seek(0, os.SEEK_END)
            fh.seek(max(0, fh.tell() - tail))
            return needle.encode("ascii") in fh.read()
    except FileNotFoundError:
        return False


def mode_verify(sleep=time.sleep):
    assert_live()
    sw = swap_file_state(SWAP_PATH)
    swaps = proc_swaps(read_text("/proc/swaps", ""))
    rows = fstab_active(read_text("/etc/fstab", ""))
    total = meminfo(read_text("/proc/meminfo", "")).get("SwapTotal")
    swappiness = int(read_text("/proc/sys/vm/swappiness", "-1").strip())
    sysctl = file_state(SYSCTL_DROPIN)
    page = os.sysconf("SC_PAGE_SIZE")
    unit = show(SWAP_UNIT, ["LoadState", "ActiveState", "SubState", "SourcePath"])
    out("SWAP %s %s; /proc/swaps %s; fstab's swap lines %s; SwapTotal %s; vm.swappiness %d; %s %s; page %d; %s %s" % (
        SWAP_PATH, sw and (sw[0], sw[1], oct(sw[2]), sw[3]), swaps,
        [r for r in rows if r[:1] == (SWAP_PATH,) or r[2:3] == ("swap",)], total, swappiness, SYSCTL_DROPIN,
        sysctl and (sysctl[0], oct(sysctl[1])), page, SWAP_UNIT, unit))
    sok, sch = swap_reading(sw, swaps, rows, total, swappiness, sysctl, page, unit)
    for k, v in sch.items():
        out("G-SWAP %s: %s" % (k, "PASS" if v else "FAIL"))
    out("G-SWAP %s" % ("PASS: 7 of 7" if sok else "FAIL"))
    dropin = file_state(JOURNALD_DROPIN)
    mtime_us = os.lstat(JOURNALD_DROPIN).st_mtime_ns // 1000 if dropin is not None else None
    jd = show("systemd-journald.service", ["ActiveState", "ActiveEnterTimestamp", "MainPID"])
    pid = jd.get("MainPID")
    rc, so, se = run(["journalctl", "-b", "--no-pager", "-o", "json", "-t", "systemd-journald", "_PID=%s" % pid])
    usage = journal_usage(so, pid)
    out("JOURNALD %s %s, changed %s us; journald %s since %s, pid %s; its usage message %s" % (
        JOURNALD_DROPIN, dropin and (dropin[0], oct(dropin[1])), mtime_us, jd.get("ActiveState"),
        jd.get("ActiveEnterTimestamp"), pid, usage))
    nonce = "%s-%s" % (PROBE_TAG, os.urandom(8).hex())
    rc, so, se = run(["logger", "-t", PROBE_TAG, "--", nonce])
    assert rc == 0, "logger: %s" % se.strip()
    in_journal = False
    for _k in range(PROBE_WAIT_S):
        rc, so, se = run(["journalctl", "-b", "--no-pager", "-o", "cat", "-t", PROBE_TAG])
        if nonce in so:
            in_journal = True
            break
        sleep(1)
    in_syslog = syslog_holds(nonce)
    rs = show("rsyslog.service", ["LoadState", "ActiveState", "UnitFileState"])
    sk = show("syslog.socket", ["LoadState", "ActiveState", "UnitFileState"])
    rc, so, se = run(["journalctl", "--disk-usage", "--no-pager"])
    out("JOURNALD the probe %s: in the journal %s, in %s %s; rsyslog %s; syslog.socket %s; %s" % (
        nonce, in_journal, SYSLOG, in_syslog, rs, sk, so.strip()))
    rc, so, se = run(["systemd-analyze", "cat-config", "systemd/journald.conf"])
    eff = effective_config(so)
    out("JOURNALD in force, by `systemd-analyze cat-config` exit %d: %s" % (rc, eff))
    lok, lch = log_reading(dropin, mtime_us, usage, in_journal, in_syslog, rs, sk, eff)
    for k, v in lch.items():
        out("G-LOG %s: %s" % (k, "PASS" if v else "FAIL"))
    out("G-LOG %s" % ("PASS: 6 of 6" if lok else "FAIL"))
    record("verify", {"swap": sok, "log": lok})
    return 0 if sok and lok else 4

# ---- the self-test: literals, temporary trees under the work tree and loopback servers ----------------------


class _FakeClob(http.server.BaseHTTPRequestHandler):
    """The CLOB's /time for the self-test: ten digits, a cf-ray of a named data centre and a cache status."""
    protocol_version = "HTTP/1.1"
    cache, close, agents = "DYNAMIC", False, []

    def log_message(self, *args):
        pass

    def do_GET(self):
        _FakeClob.agents.append(self.headers.get("User-Agent"))
        body = b"1795020548"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("cf-ray", "a5c8777a1d416392-SOF")
        self.send_header("cf-cache-status", _FakeClob.cache)
        if _FakeClob.close:
            self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(body)


def _fake_ws(server, good, seen):
    """One websocket handshake answered on a loopback socket: the right accept key or a wrong one; the client's
    request and its close frame recorded."""
    conn, _a = server.accept()
    with conn:
        conn.settimeout(5)
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += conn.recv(4096)
        head = buf.decode("latin-1")
        seen["request"] = head
        key = [ln.split(":", 1)[1].strip() for ln in head.split("\r\n") if ln.lower().startswith("sec-websocket-key")]
        acc = ws_accept(key[0]) if good else ws_accept("x" + key[0])
        conn.sendall(("HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n"
                      "Sec-WebSocket-Accept: %s\r\ncf-ray: 0123456789abcdef-SOF\r\n\r\n" % acc).encode("ascii"))
        try:
            seen["frame"] = conn.recv(16)
        except OSError:
            seen["frame"] = b""


def mode_selftest():
    results = []

    def ok(cond, what):
        results.append((bool(cond), what))
        out("%s %s" % ("ok  " if cond else "FAIL", what))

    if os.path.exists(TMP):
        shutil.rmtree(TMP)
    os.mkdir(TMP)
    try:
        v = list(range(1, 101))
        ok(nearest_rank(v, 5) == 5 and nearest_rank(v, 50) == 50 and nearest_rank(v, 95) == 95
           and nearest_rank(v, 99) == 99 and nearest_rank(v, 100) == 100 and nearest_rank(list(range(600)), 50) == 299,
           "nearest rank: 5, 50, 95, 99 and 100 of 1..100; of 600 values the median is the 300th smallest")

        def smp(i, t, **kw):
            s = {"i": i, "warm": False, "fresh": False, "status": 200, "ttfb_ns": t, "pop": "SOF", "cache": "DYNAMIC",
                 "body_ok": True, "venue_s": 1795020548, "host_s": 1795020548, "error": None}
            s.update(kw)
            return s

        at = [smp(i, 100000000 if i % 2 else 99000000) for i in range(600)]
        at[0]["ttfb_ns"] = 100000000
        r, st = lat_reading([smp(-1, 5, warm=True)] + at)
        ok(r == "PASS" and st["p50"] == 100000000 and st["counted"] == 600 and st["valid"] == 600,
           "G-LAT PASS where the median is 100,000,000 ns exactly; the warm-up not counted")
        above = [dict(s, ttfb_ns=s["ttfb_ns"] + 1) for s in at]
        ok(lat_reading(above)[0] == "FAIL", "G-LAT FAIL where the median is 100,000,001 ns")
        few = at[:569] + [smp(569 + i, 1, cache="HIT") for i in range(31)]
        r, st = lat_reading(few)
        ok(r == "UNDECIDABLE" and st["valid"] == 569 and st["cache other"] == 31,
           "G-LAT UNDECIDABLE at 569 valid of 600: a cached reply is not the origin's")
        bad = [smp(0, 1, fresh=True), smp(1, 1, status=503), smp(2, 1, body_ok=False), smp(3, 1, pop=""),
               smp(4, 1, error="TimeoutError"), smp(5, 1, cache="")]
        ok(not any(valid_sample(s) for s in bad) and valid_sample(smp(6, 1)),
           "a fresh, a 503, a body not ten digits, no data centre, an error and no cache status: none valid")
        ok(ms(100000000) == "100.000" and ms(100000000 // 2) == "50.000" and pop_of("a5c8777a1d416392-SOF") == "SOF"
           and pop_of("nodash") == "" and pop_of("x-sofia") == "" and pop_of(None) == "",
           "milliseconds to three decimals; the data centre from a cf-ray header, and none from a malformed one")
        g = {"blocked": False, "country": "BG", "ip": "192.0.2.1", "region": "22"}
        ok(geo_reading(200, g) == "PASS" and geo_reading(200, dict(g, blocked=True)) == "BLOCKED"
           and geo_reading(403, g) == "UNREAD" and geo_reading(200, dict(g, blocked="false")) == "UNREAD"
           and geo_reading(200, dict(g, country="BGR")) == "UNREAD" and geo_reading(200, None) == "UNREAD"
           and geo_reading(200, {"country": "BG"}) == "UNREAD" and geo_reading(None, None) == "UNREAD",
           "G-GEO: PASS, BLOCKED, and UNREAD on a 403, a string, three letters, no body, no blocked and no reply")
        ok("ip" not in geo_fields(g) and "192.0.2.1" not in json.dumps(geo_fields(g)) and geo_fields(g)["keys"] ==
           ["blocked", "country", "ip", "region"], "the geoblock's printed fields carry its keys and never the address")
        ok(err_of(OSError(101, "Network is unreachable")) == "OSError errno 101: Network is unreachable"
           and err_of(ConnectionRefusedError(111, "Connection refused"))
           == "ConnectionRefusedError errno 111: Connection refused"
           and err_of(TimeoutError("timed out")) == "TimeoutError"
           and err_of(http.client.RemoteDisconnected("closed")) == "RemoteDisconnected",
           "an error printed by its type, errno and the C library's message, or its type alone")
        if6 = ("20010db8000000000000000000000001 02 40 00 80     eth0\n"
               "fe80000000000000025056fffe8a1234 02 40 20 80     eth0\n"
               "00000000000000000000000000000001 01 80 10 80       lo\n")
        rt = ("20010db8000000000000000000000000 40 00000000000000000000000000000000 00 "
              "00000000000000000000000000000000 00000100 00000001 00000000 00000001     eth0\n"
              "00000000000000000000000000000000 00 00000000000000000000000000000000 00 "
              "00000000000000000000000000000000 ffffffff 00000001 00000000 00200200       lo\n")
        gw = ("00000000000000000000000000000000 00 00000000000000000000000000000000 00 "
              "fe800000000000000000000000000001 00000400 00000001 00000000 00450003     eth0\n")
        s0, s1 = v6_state(if6, rt), v6_state(if6, rt + gw)
        ok(s0 == {"global addresses": 1, "their flags": ["80"], "default routes": 1, "usable": 0, "usable via": []}
           and s1["default routes"] == 2 and s1["usable"] == 1 and s1["usable via"] == ["eth0, next hop link-local"]
           and v6_state("", "") == {"global addresses": 0, "their flags": [], "default routes": 0, "usable": 0,
                                    "usable via": []}
           and not any(x in json.dumps([s0, s1]) for x in ("20010db8", "fe80", "2001", "eth0, next hop fe")),
           "IPv6's state: one global address; a reject route is no usable default, a gateway route is; no address")
        ok(spec_reading(1800000000, 18000000000)[0] and not spec_reading(1799999999, 18000000000)[0]
           and not spec_reading(1800000000, 17999999999)[0], "G-SPEC at its bounds, and a byte under each")
        osr = os_release('PRETTY_NAME="Ubuntu 24.04.5 LTS"\nID=ubuntu\nVERSION_ID="24.04"\n')
        key = [("ecdsa-sha2-nistp256", "SHA256:e"), LIVE_HOST_KEY, ("ssh-rsa", "SHA256:r")]
        ok(live_gate(LIVE_HOSTNAME, osr, (3, 12, 3), [], key)[0]
           and not live_gate("vultr", osr, (3, 12, 3), [], key)[0]
           and not live_gate(LIVE_HOSTNAME, dict(osr, VERSION_ID="26.04"), (3, 12, 3), [], key)[0]
           and not live_gate(LIVE_HOSTNAME, osr, (3, 14, 0), [], key)[0]
           and not live_gate(LIVE_HOSTNAME, osr, (3, 12, 3), [CAPTURE_MARK], key)[0]
           and not live_gate(LIVE_HOSTNAME, osr, (3, 12, 3), [], [("ssh-ed25519", "SHA256:other")])[0]
           and not live_gate(LIVE_HOSTNAME, osr, (3, 12, 3), [], [])[0]
           and live_gate(LIVE_HOSTNAME, osr, (3, 12, 3), [], [LIVE_HOST_KEY])[0],
           "the live host gate: five checks, each failing alone; the pinned key among the host's keys, or alone")
        ok(first_label("vs-2348.provider.example") == LIVE_HOSTNAME and first_label("vs-2348") == LIVE_HOSTNAME
           and first_label("vs-23480.provider.example") != LIVE_HOSTNAME and first_label("vs-2348x") != LIVE_HOSTNAME,
           "the host name's first label: vs-2348 with and without its provider's domain, and no other name")
        swaps1 = ("Filename\tType\tSize\tUsed\tPriority\n"
                  "/swap.img                               file\t\t1048572\t\t0\t\t-2\n")
        ok(proc_swaps(swaps1) == [("/swap.img", "file", 1048572, 0)] and proc_swaps("Filename Type\n") == [],
           "/proc/swaps parsed: the host's own file of 1,048,572 KiB; a header alone is no swap")
        fst = "# /etc/fstab\nUUID=abc / ext4 defaults 0 1\n\n/swap.img none swap sw 0 0\n#/old none swap sw 0 0\n"
        ok(fstab_active(fst) == [("UUID=abc", "/", "ext4", "defaults", "0", "1"), FSTAB_FIELDS],
           "fstab: comments and blank lines left out")
        unit = {"LoadState": "loaded", "ActiveState": "active", "SubState": "active", "SourcePath": "/etc/fstab"}
        good = ((True, SWAP_BYTES, 0o600, 0), proc_swaps(swaps1), fstab_active(fst), 1048572 * 1024, 10,
                (SYSCTL_SHA256, 0o644), 4096, unit)
        ok(swap_reading(*good)[0], "G-SWAP PASS on literals: the host's own file, one swap, one fstab line, "
           "SwapTotal, swappiness, the sysctl file, its unit made of fstab")
        old = "Filename\tType\tSize\tUsed\tPriority\n/swapfile file 1048572 0 -2\n"
        variants = [((True, SWAP_BYTES, 0o644, 0),) + good[1:], (None,) + good[1:],
                    good[:1] + (proc_swaps(swaps1 + "/dev/vda3 partition 1000 0 -3\n"),) + good[2:],
                    good[:1] + (proc_swaps(swaps1.replace("1048572", "1048576")),) + good[2:],
                    good[:1] + (proc_swaps(old),) + good[2:],
                    good[:2] + (fstab_active(fst + "/swap.img none swap sw 0 0\n"),) + good[3:],
                    good[:2] + (fstab_active(fst + "/swapfile none swap sw 0 0\n"),) + good[3:],
                    good[:2] + (fstab_active(fst.replace("sw 0 0", "defaults 0 0")),) + good[3:],
                    good[:3] + (1048572 * 1024 + 4096,) + good[4:], good[:4] + (60,) + good[5:],
                    good[:5] + ((SYSCTL_SHA256, 0o600),) + good[6:], good[:5] + (None,) + good[6:],
                    good[:7] + (dict(unit, ActiveState="inactive"),),
                    good[:7] + (dict(unit, SourcePath="/etc/systemd/system/swap.img.swap"),)]
        ok(all(not swap_reading(*a)[0] for a in variants) and len(variants) == 14,
           "G-SWAP FAIL on fourteen wrong readings, each alone: /swapfile, the path TZ-48 assumed, among them")

        def ent(pid, us, name="System Journal", mid=USAGE_ID, mx="536870912", kf="2147483648"):
            return json.dumps({"MESSAGE_ID": mid, "JOURNAL_NAME": name, "_PID": str(pid), "MAX_USE": mx,
                               "DISK_KEEP_FREE": kf, "__REALTIME_TIMESTAMP": str(us), "MESSAGE": "%s is 8.0M" % name})
        jtext = "\n".join([ent(100, 1795020000000001, mx="209715200"),
                           ent(200, 1795020600100000, name="Runtime Journal"),
                           json.dumps({"MESSAGE": "Journal started", "_PID": "200"}), ent(200, 1795020600223456),
                           "not json", ent(200, 1795020600300000, mid="x" * 32, mx="1")])
        u = journal_usage(jtext, 200)
        ok(u is not None and u["realtime_us"] == 1795020600223456 and u["max_use"] == 536870912
           and u["keep_free"] == 2147483648 and journal_usage(jtext, 100)["max_use"] == 209715200
           and journal_usage(jtext, 300) is None,
           "journald's usage message: the System Journal's of this process alone, the last one; none of another")
        cap = "/etc/systemd/journald.conf.d/cap.conf"
        cat = ("# /etc/systemd/journald.conf\n#  Entries in this file show the compile time defaults.\n[Journal]\n"
               "#Storage=auto\n\n# %s\n[Journal]\nSystemMaxUse=200M\n\n# /usr/lib/systemd/journald.conf.d/syslog.conf\n"
               "# /etc/ if the original file is shipped\n[Journal]\nForwardToSyslog=yes\n\n# %s\n%s" % (
                   cap, JOURNALD_DROPIN, JOURNALD_TEXT))
        eff = effective_config(cat)
        before = effective_config(cat.split("# " + JOURNALD_DROPIN)[0])
        ok(eff["ForwardToSyslog"] == ("no", JOURNALD_DROPIN) and eff["SystemMaxUse"] == ("512M", JOURNALD_DROPIN)
           and before["ForwardToSyslog"] == ("yes", "/usr/lib/systemd/journald.conf.d/syslog.conf")
           and before["SystemMaxUse"] == ("200M", cap),
           "the merged configuration: each key's last value and its file, ours after cap.conf and syslog.conf; a "
           "comment beginning '# /' no header")
        rs_off = {"LoadState": "loaded", "ActiveState": "inactive", "UnitFileState": "disabled"}
        sk_off = {"LoadState": "loaded", "ActiveState": "inactive", "UnitFileState": "static"}
        lg = ((JOURNALD_SHA256, 0o644), 1795020599700000, u, True, False, rs_off, sk_off, eff)
        nf = {"LoadState": "not-found"}
        ok(log_reading(*lg)[0] and log_reading(*(lg[:5] + (nf, nf, eff)))[0],
           "G-LOG PASS on literals, rsyslog disabled or not installed")
        lv = [((JOURNALD_SHA256, 0o600),) + lg[1:], lg[:1] + (1795020600223457,) + lg[2:],
              lg[:2] + (dict(u, max_use=536870913),) + lg[3:], lg[:2] + (dict(u, keep_free=0),) + lg[3:],
              lg[:2] + (None,) + lg[3:], lg[:3] + (False,) + lg[4:], lg[:4] + (True,) + lg[5:],
              lg[:5] + (dict(rs_off, ActiveState="active"),) + lg[6:],
              lg[:5] + (dict(rs_off, UnitFileState="enabled"),) + lg[6:],
              lg[:6] + (dict(sk_off, ActiveState="active"),) + lg[7:],
              lg[:7] + (before,), lg[:7] + (dict(eff, SystemMaxUse=("200M", cap)),)]
        ok(all(not log_reading(*a)[0] for a in lv) and len(lv) == 12,
           "G-LOG FAIL on twelve wrong readings, each alone: cap.conf's bound in force among them")
        ok(sha256_bytes(JOURNALD_TEXT.encode()) == JOURNALD_SHA256 and sha256_bytes(SYSCTL_TEXT.encode())
           == SYSCTL_SHA256 and sha256_bytes(SSHD_TEXT.encode()) == SSHD_SHA256 and len(JOURNALD_TEXT.encode()) == 448
           and len(SYSCTL_TEXT.encode()) == 210 and len(SSHD_TEXT.encode()) == 340
           and sha256_bytes(BSSH_TEXT.encode()) == BSSH_SHA256 and len(BSSH_TEXT.encode()) == 1746,
           "the four files: their SHA-256 and bytes")
        ok(settings(JOURNALD_TEXT) == [("Storage", "persistent"), ("SystemMaxUse", "512M"), ("SystemKeepFree", "2G"),
                                       ("SystemMaxFileSize", "64M"), ("RuntimeMaxUse", "64M"),
                                       ("ForwardToSyslog", "no")] and JOURNALD_TEXT.count("[Journal]") == 1
           and [ln for ln in SYSCTL_TEXT.split("\n") if ln and not ln.startswith("#")] == ["vm.swappiness = 10"]
           and [ln.split(None, 1) for ln in SSHD_TEXT.split("\n") if ln and not ln.startswith("#")] == [
               ["PasswordAuthentication", "no"], ["KbdInteractiveAuthentication", "no"],
               ["PermitRootLogin", "prohibit-password"]]
           and SSHD_DROPIN in BSSH_TEXT and SSHD_SHA256 in BSSH_TEXT and "--on-active=300" in BSSH_TEXT
           and "--unit=tz49-ssh-revert" in BSSH_TEXT and BSSH_TEXT.count("logs/43-B-SSH.log") == 2,
           "the journald file sets six keys under [Journal]; the sysctl file one; the sshd file three; B-SSH names "
           "the drop-in, its SHA-256, its guard and its log")
        tb = ("port 22\npermitrootlogin yes\npubkeyauthentication yes\npasswordauthentication yes\n"
              "kbdinteractiveauthentication no\nlistenaddress [::]:22\nlistenaddress 0.0.0.0:22\n")
        ta = tb.replace("permitrootlogin yes", "permitrootlogin without-password").replace(
            "passwordauthentication yes", "passwordauthentication no")
        e_a, d_ok = sshd_effective(ta), (SSHD_SHA256, 0o644)
        ok(e_a["permitrootlogin"] == "without-password" and e_a["listenaddress"] == "0.0.0.0:22"
           and ssh_reading(d_ok, e_a)[0] and len(ssh_reading(d_ok, e_a)[1]) == 5
           and not ssh_reading(d_ok, sshd_effective(tb))[0],
           "G-SSH on the live host PASS on sshd -T as OpenSSH 9.6 prints it after the drop-in, FAIL before it")
        sv = [(None, e_a), ((SSHD_SHA256, 0o600), e_a), (d_ok, dict(e_a, passwordauthentication="yes")),
              (d_ok, dict(e_a, kbdinteractiveauthentication="yes")), (d_ok, dict(e_a, permitrootlogin="yes")),
              (d_ok, dict(e_a, pubkeyauthentication="no")), (d_ok, {})]
        ok(all(not ssh_reading(*a)[0] for a in sv) and len(sv) == 7,
           "G-SSH FAIL on seven wrong readings, each alone: no sshd -T among them")
        vtext = ("OpenSSH_9.6p1 Ubuntu-3ubuntu13.20, OpenSSL 3.0.13 30 Jan 2024\n"
                 "debug1: Connecting to 192.0.2.7 [192.0.2.7] port 22.\n"
                 "debug1: Authentications that can continue: publickey\n"
                 "debug1: No more authentication methods to try.\nroot@192.0.2.7: Permission denied (publickey).\n")
        ok(methods_of(vtext) == ["publickey"] and "192.0.2.7" not in json.dumps(methods_of(vtext))
           and methods_of(vtext.replace("continue: publickey", "continue: publickey,password") * 2)
           == ["publickey,password"] and methods_of("debug1: Connecting to 192.0.2.7 port 22.\n") == [],
           "the methods an sshd offered, from ssh -v's text: each list once, and never the address")
        p = os.path.join(TMP, "swap-stand-in")
        with open(p, "xb") as fh:
            fh.write(b"\0" * 4096)
        os.chmod(p, 0o600)
        ok(swap_file_state(p) == (True, 4096, 0o600, os.getuid()) and swap_file_state(p + ".absent") is None,
           "a swap file's state: regular, bytes, mode, owner; None where it is absent")
        ok(number_reading(["CryptoTZ/TZ-48-live-host-rerun.md", OWN_TZ], OWN_TZ)[0]
           and not number_reading(["CryptoTZ/TZ-48-live-host-rerun.md"], OWN_TZ)[0]
           and number_reading(["CryptoTZ/TZ-48-live-host-rerun.md", OWN_TZ,
                               "CryptoReports/TZ-48-live-host-rerun-report.md"], OWN_TZ)[0]
           and not number_reading([OWN_TZ, "CryptoTZ/TZ-49-other.md"], OWN_TZ)[0]
           and not number_reading([OWN_TZ, "CryptoReports/TZ-49-live-host-ipv4-keys-report.md"], OWN_TZ)[0],
           "NUMBER: this TZ's file alone, TZ-48's files beside it; absent, a second of the number, a report of it")
        refs = ("a\tHEAD\nb\trefs/heads/main\nc\trefs/heads/tz-46-capture-room\nd\trefs/pull/46/head\n"
                "e\trefs/tags/rewardbook-streams-1795073420\nf\trefs/tags/pairbook-streams-1794925184\n"
                "g\trefs/tags/tz-27-pairbook-streams\nh\trefs/tags/tz-27-pairbook-streams^{}\n")
        kinds, br = refs_reading(refs)
        ok(not br and kinds["refs/heads/tz-*"] == 1 and kinds["refs/tags/rewardbook-streams-*"] == 1
           and kinds["refs/tags/tz-27-pairbook-streams^{}"] == 1 and sum(kinds.values()) == 8
           and refs_reading(refs + "i\trefs/heads/tz-49-live-host-ipv4-keys\n")[1],
           "refs by kind, eight lines; this TZ's branch found where it exists")
        ok(room_reading(10000000000, 100000000) == (10100000000, 10100000000 - 7300000000 - 445535636)
           and CAPTURE_FLOOR == 7795535636 and LIVE_FLOOR == 2515919104 and PEAK == 14 * 31823974,
           "the room and its margin; the floors 7,795,535,636 and 2,515,919,104; PEAK fourteen slots")
        tcp = ("  sl  local_address rem_address   st tx_queue rx_queue tr tm->when retrnsmt   uid  timeout inode\n"
               "   0: 00000000:0016 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 1001\n"
               "   1: 3500007F:0035 00000000:0000 0A 00000000:00000000 00:00000000 00000000   991        0 1002\n"
               "   2: 0A0200C0:0016 0B0200C0:C350 01 00000000:00000000 00:00000000 00000000     0        0 1003\n")
        ok(listening(tcp, "tcp") == [("tcp", "any", 22, 1001), ("tcp", "loopback", 53, 1002)]
           and addr_class("00000000000000000000000001000000") == "loopback" and addr_class("0A0200C0") == "other",
           "listening sockets: ports and classes, an established one left out, no address printed")
        blob = base64.b64encode(b"\x00\x00\x00\x0bssh-ed25519" + b"\x00" * 36).decode()
        fp = key_fingerprints("ssh-ed25519 %s someone@example\n# comment\nfrom=\"x\" ssh-rsa %s y\n" % (blob, blob))
        ok(len(fp) == 2 and fp[0][0] == "ssh-ed25519" and fp[0][1].startswith("SHA256:")
           and "someone" not in json.dumps(fp),
           "authorized keys: type and SHA256 fingerprint, options skipped, comments never printed")
        gh = "github.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOMqqnkVzrm0SdG6UOoqKLsabgH5C9okWi0dh2l9GKJl\n"
        ok(key_fingerprints(gh) == [("ssh-ed25519", "SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU")],
           "a key's fingerprint as OpenSSH prints it: GitHub's published Ed25519 key and its published fingerprint")
        ok(reclaimable(WORK) and not reclaimable("/root") and not reclaimable("/tmp/x")
           and not reclaimable("/tmp/claude-0/-root-other/1b2c3d4e-0000-0000-0000-000000000000"),
           "reclaim's predicate: the work tree; nothing outside /tmp or beside another project's sessions")
        ok(policy("selftest", "open", (WORK + "/x", "w", 0)) is None
           and policy("selftest", "open", ("/tmp/x", "w", 0)) is not None
           and policy("room", "open", (RB + "/1795000000/1.1.stream.jsonl.gz", "r", 0)) is not None
           and policy("host", "open", ("/etc/adv3-bot/token", "r", 0)) is not None
           and policy("room", "os.scandir", (RB,)) is None and policy("host", "os.scandir", (RB,)) is not None
           and policy("host", "os.scandir", ("/var/lib/btc-recorder",)) is not None
           and policy("reclaim", "open", (FORENSICS + "/a", "xb", 0)) is None
           and policy("reclaim", "open", (FORENSICS + "/a", "wb", 0)) is not None
           and policy("disk", "os.remove", (WORK + "/disk-test.bin",)) is None
           and policy("disk", "os.remove", (SWAP_PATH,)) is not None
           and policy("files", "open", (SSHD_DROPIN, "w", 0)) is not None,
           "the hook's files: writes under the work tree alone; no store or credential opened; the reward book "
           "listed by room alone; the forensic store by reclaim's exclusive create alone")
        A4, S = socket.AF_INET, socket.SOCK_STREAM
        ok(policy("geoblock", "socket.getaddrinfo", (GEO_HOST, 443, A4, S, 6)) is None
           and policy("geoblock", "socket.getaddrinfo", (CLOB_HOST, 443, A4, S, 6)) is not None
           and policy("latency", "socket.getaddrinfo", (GEO_HOST, 443, A4, S, 6)) is not None
           and policy("net", "socket.getaddrinfo", (WS_HOST, 443, A4, S, 6)) is None
           and policy("host", "socket.getaddrinfo", (CLOB_HOST, 443, A4, S, 6)) is not None
           and policy("verify", "socket.connect", (None, ("192.0.2.1", 443))) is not None
           and policy("selftest", "socket.connect", (None, ("127.0.0.1", 1))) is None,
           "the hook's network: each mode's hosts alone, and no connection to an address it did not resolve")
        RESOLVED.add("2001:db8::1")
        try:
            v6_connect = policy("net", "socket.connect", (None, ("2001:db8::1", 443, 0, 0)))
        finally:
            RESOLVED.discard("2001:db8::1")
        modes = ("geoblock", "net", "latency", "host", "files", "sshd", "verify", "methods", "selftest")
        ok(all(policy(m, "socket.__new__", (None, socket.AF_INET6, S, 0)) is not None
               and policy(m, "socket.__new__", (None, socket.AF_INET6, socket.SOCK_DGRAM, 0)) is not None
               and policy(m, "socket.__new__", (None, socket.AF_UNIX, S, 0)) is not None
               and policy(m, "socket.__new__", (None, A4, S, 0)) is None for m in modes)
           and policy("geoblock", "socket.getaddrinfo", (GEO_HOST, 443, socket.AF_INET6, S, 6)) is not None
           and policy("geoblock", "socket.getaddrinfo", (GEO_HOST, 443, 0, S, 6)) is not None
           and policy("geoblock", "socket.getaddrinfo", (GEO_HOST, 443)) is not None and v6_connect is not None,
           "IPv4 alone, in every mode: an AF_INET6 or AF_UNIX socket, a lookup in AF_INET6 or AF_UNSPEC and a "
           "connection to an IPv6 address refused, a resolved one included; an AF_INET socket allowed")
        ok(policy("host", "subprocess.Popen", (None, ["sshd", "-T"], None, None)) is None
           and policy("host", "subprocess.Popen", (None, ["swapon"], None, None)) is not None
           and policy("verify", "subprocess.Popen", (None, ["logger", "x"], None, None)) is None
           and policy("latency", "subprocess.Popen", (None, ["curl"], None, None)) is not None
           and policy("files", "subprocess.Popen", (None, ["install"], None, None)) is not None
           and policy("methods", "subprocess.Popen", (None, ["ssh", "-T"], None, None)) is None
           and policy("sshd", "subprocess.Popen", (None, ["sshd", "-T"], None, None)) is None
           and policy("sshd", "subprocess.Popen", (None, ["systemctl", "reload"], None, None)) is not None
           and policy("geoblock", "subprocess.Popen", (None, ["ssh"], None, None)) is not None,
           "the hook's commands: each mode's read-only commands alone; nothing changes the host but the blocks")
        try:
            with open("/tmp/tz49-selftest-forbidden", "w") as fh:
                fh.write("x")
            refused = False
        except GuardError:
            refused = True
        ok(refused and not os.path.exists("/tmp/tz49-selftest-forbidden"), "the hook refuses, live, a write "
           "outside the work tree")
        live = []
        for attempt in (lambda: socket.socket(socket.AF_INET6, socket.SOCK_STREAM),
                        lambda: socket.getaddrinfo("127.0.0.1", 443, socket.AF_INET6, socket.SOCK_STREAM),
                        lambda: socket.getaddrinfo("127.0.0.1", 443)):
            try:
                got = attempt()
                if hasattr(got, "close"):
                    got.close()
                live.append(False)
            except GuardError:
                live.append(True)
        ok(live == [True, True, True], "the hook refuses, live, an AF_INET6 socket, a lookup in AF_INET6 and one in "
           "AF_UNSPEC")
        srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _FakeClob)
        th = threading.Thread(target=srv.serve_forever, daemon=True)
        th.start()
        try:
            port = srv.server_address[1]
            make = lambda: plain_conn("127.0.0.1", port, 5)
            _FakeClob.cache, _FakeClob.close, _FakeClob.agents = "DYNAMIC", False, []
            sm = probe(make, TIME_PATH, 2, 30, 0.01, 30)
            r, st = lat_reading(sm, valid_min=29)
            ok(len(sm) == 32 and sm[0]["fresh"] and not any(s["fresh"] for s in sm[1:]) and r == "PASS"
               and st["valid"] == 30 and set(_FakeClob.agents) == {UA} and len(_FakeClob.agents) == 32,
               "the probe over one kept loopback connection: the first exchange fresh, 30 counted, every request "
               "with this TZ's agent")
            _FakeClob.close = True
            sm = probe(make, TIME_PATH, 2, 10, 0.01, 30)
            ok(all(s["fresh"] for s in sm) and lat_reading(sm, valid_min=1)[0] == "UNDECIDABLE",
               "a server that closes every connection: every exchange fresh, G-LAT UNDECIDABLE")
            _FakeClob.close, _FakeClob.cache = False, "HIT"
            sm = probe(make, TIME_PATH, 0, 5, 0.01, 30)
            ok(lat_reading(sm, valid_min=1)[0] == "UNDECIDABLE", "a cached reply: G-LAT UNDECIDABLE")
            _FakeClob.cache = "DYNAMIC"
            sm = probe(make, TIME_PATH, 0, 50, 0.05, 0.5)
            ok(len(sm) < 50, "no request begun after the budget")
            conn = make()
            st0, h, body, t, fresh, src = request(conn, TIME_PATH)
            fam = conn.sock.family if conn.sock is not None else None
            conn.close()
            ok(st0 == 200 and body == b"1795020548" and fresh and src == "127.0.0.1" and fam == socket.AF_INET
               and h.get("cf-ray") == "a5c8777a1d416392-SOF", "a request through connect4: status, body, headers, "
               "fresh and the connection's own source address")
        finally:
            srv.shutdown()
            srv.server_close()
        times = edge_probe("127.0.0.1", port, 3, 0.0)
        ok(len(times) == 3 and all(t is None for t in times), "TCP handshakes with a closed port: each None")
        for good_key in (True, False):
            ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ls.bind(("127.0.0.1", 0))
            ls.listen(1)
            seen = {}
            th = threading.Thread(target=_fake_ws, args=(ls, good_key, seen), daemon=True)
            th.start()
            c = connect4("127.0.0.1", ls.getsockname()[1], 5)
            code, valid, hdrs = ws_handshake(c, WS_HOST, WS_PATH)
            c.close()
            th.join(5)
            ls.close()
            if good_key:
                ok(code == 101 and valid and "User-Agent: %s\r\n" % UA in seen["request"]
                   and seen["request"].startswith("GET %s HTTP/1.1\r\nHost: %s\r\n" % (WS_PATH, WS_HOST))
                   and seen.get("frame", b"")[:2] == b"\x88\x82" and pop_of(hdrs.get("cf-ray")) == "SOF",
                   "the websocket handshake: 101, its accept key valid, this TZ's agent, closed with a masked "
                   "frame of status 1000")
            else:
                ok(code == 101 and not valid, "a wrong accept key: the handshake not valid")
        p = os.path.join(TMP, "rate.bin")
        ns = write_rate(p, 4 * DISK_CHUNK, DISK_CHUNK)
        ft = fsync_times(p, 5, FSYNC_BYTES)
        ok(ns > 0 and len(ft) == 5 and all(t > 0 for t in ft) and not os.path.exists(p),
           "the disk's write rate and fsync times on a stand-in of 4 MiB and 5 appends, its file removed")
        mi = meminfo("MemTotal:        2014412 kB\nMemAvailable:    1700000 kB\nHugePages_Total:       0\n")
        ok(mi == {"MemTotal": 2014412 * 1024, "MemAvailable": 1700000 * 1024, "HugePages_Total": 0},
           "meminfo in bytes, a count left a count")
        ok(stamp_of("Wed 2026-11-18 10:11:08 UTC") == 1794996668 and stamp_of("") is None and stamp_of("n/a") is None,
           "systemctl's stamp under TZ=UTC")
    finally:
        shutil.rmtree(TMP)
    n_ok = sum(1 for good_, _w in results if good_)
    out("SELFTEST %s: %d checks, %d passed" % ("PASS" if n_ok == len(results) else "FAIL", len(results), n_ok))
    assert n_ok == len(results), "SELFTEST FAIL: %s" % [w for good_, w in results if not good_]
    return 0


def main(argv):
    if not argv:
        sys.exit("usage: %s MODE [ARG...]" % PYFILE)
    mode, rest = argv[0], argv[1:]
    assert os.getcwd() == WORK, "run from %s, not %s" % (WORK, os.getcwd())
    MODE[0] = mode
    table = {"fingerprint": mode_fingerprint, "number": mode_number, "refs": mode_refs, "room": mode_room,
             "geoblock": mode_geoblock, "files": mode_files, "sshd": mode_sshd, "net": mode_net,
             "latency": mode_latency, "disk": mode_disk, "verify": mode_verify, "selftest": mode_selftest}
    one = {"scratch": mode_scratch, "methods": mode_methods, "host": mode_host}
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
        out("refused by the hook: %d; lookups %d, requests %d, handshakes %d, TCP connects %d" % (
            len(REFUSED), COUNTS["lookups"], COUNTS["requests"], COUNTS["handshakes"], COUNTS["tcp connects"]))
    return rc or 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
