#!/usr/bin/env python3
"""TZ-09: disk inventory, bounded reclamation and the retention rule.

System Map section 6 measures the filesystem filling at 0.84 to 1.00 GB/day while the recorder
writes 23,850,461 bytes/day. This script names the consumer in exact bytes, accounts for the
capture, the logs and the space held by unlinked open files, and prepares the reclamation of
this project's own scratch.

It measures and prints, and nothing else. It takes nothing away from any filesystem: R3's copies
and R4's deletions are shell commands the Executor runs and the report quotes verbatim. Every
file this script writes lands under `/root/tz09-work/`, and `write_out` asserts that before it
opens one - it is the only place the script opens a file for writing.

Read-only over the capture: `/var/lib/btc-recorder/**` is enumerated with `du`, `df`, `stat`
and `os.scandir`, `runtime.jsonl` is read, and M6's sample copies are hashed against their
originals. Nothing there is opened for writing, and no process is signalled.

Run:  python3 -B tz09-disk-inventory.py <subcommand> <name> [arguments]

  gate      <name>                         V1 host and resource gates, V9 fingerprint table
  snap      <name> [--drill <snap>]        M1, M2, M4, M5 and M7 at one instant
  show      <snap>                         print a snapshot already taken, measuring nothing
  v3        <name> <snap-a> <snap-b>       the ordering of every directory >= 100,000,000 bytes
  m3        <name> <snap-t0> <snap-t1>     M3 deltas, V4 window, V5 closure, the consumer rule
  m6        <name> <sample> <archive> <snap>   M6 sizes, ratio and projection
  r1        <name>                         R1 enumeration, R2 preservation, the R3 plan
  v6        <name> <r1>                    V6 source against destination, every preserved file
  df        <name>                         one timed `df` read
  state     <name>                         recorder pid, start sha, interval count, newest T0
  v7        <name> <state-a> <state-b>     V7, asserted
  v8        <name> <state-start> <state-end>   V8, asserted
  r5        <name> <df-before> <df-after>  R5, asserted
  retention <name> <m3> <df>               section 5.4: D, A, free space against A, days to F
  v10       <name> <json> ...              V10: free space at every instant named

Each subcommand writes `<name>.json` under `/root/tz09-work/` and prints Markdown. A free-space
read below 3,000,000,000 bytes writes what has been measured, marked blocked, and exits 3.
"""

import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))

# TZ-09 section 4 and section 6: the only directory this script writes into.
WORK = "/root/tz09-work"

CAPTURE = "/var/lib/btc-recorder"
INTERVALS = CAPTURE + "/btc-updown-5m"
RUNTIME = CAPTURE + "/runtime.jsonl"

# TZ-09 section 0, host gate, from System Map section 6.
DEVICE = "/dev/vda2"
DEVICE_TOTAL = 31_612_203_008
START_SHA = "4216c04673ced76b5b2ac60ef57c9abedc46f9b9"

# TZ-09 section 0, resource gate, in exact bytes.
FLOOR_START = 2_000_000_000
FLOOR_RUN = 3_000_000_000

# TZ-09 section 0, fingerprint gate, compared with System Map section 0.
MAP_REVISION = "2026-09-13-c"
ANCHORS = {
    "A1": "229a944f2d51",
    "A2": "6c5089330629",
    "A3": "0-complete / 1-answered-no / 2-not-started",
    "A4": "437b45ea196b",
    "A5": "9fd1c7de0f74",
    "A6": "cb72abb8dd8a",
}
# The artifact each hashed anchor names, System Map section 0. `A1` is the Release asset and is
# compared as a string only; `A3` is not a hash.
ANCHOR_FILES = {
    "A2": "research/twap-divergence.py",
    "A4": "BTC-EXECUTOR-INSTRUCTIONS.md",
    "A5": "research/recorder/recorder.py",
    "A6": "research/pfair.py",
}
TZ_FILE = "CryptoTZ/TZ-09-disk-inventory.md"

# TZ-09 section 3, M2.
TOP_DEPTH2 = ["/var", "/root", "/home", "/srv", "/opt", "/usr", "/tmp"]
REPORT_MIN = 100_000_000
DRILL_COUNT = 3

# This project's own paths, for M2's "not this project's". A path is this project's when it is
# one of these or lies under one.
PROJECT_PATHS = (
    "/var/lib/btc-recorder",
    "/root/btc-5m-twap",
    "/root/btc-forensics",
    "/root/tz01-env",
    "/root/tz01-out-archive",
    "/root/tz04a-env",
    "/root/tz04b-work",
    "/root/tz05a-work",
    "/root/tz06-work",
    "/root/tz07-work",
    "/root/tz07b-work",
    "/root/tz08-work",
    "/root/tz08a-work",
    "/root/tz09-work",
)

# TZ-09 section 3, M3 and M4.
WINDOW_MIN = 3_600
M4_THRESHOLD = 100_000_000
V5_THRESHOLD = 100_000_000
DAY = 86_400

# TZ-09 section 3, M5: System Map section 6's capture cost.
CAPTURE_RATE = 23_850_461

# TZ-09 section 3, M6.
SAMPLE_SIZE = 20

# TZ-09 section 4, in the order the specification fixes.
ALLOW_LIST = (
    "/root/tz01-out-archive",
    "/root/tz06-work",
    "/root/tz07-work",
    "/root/tz07b-work",
    "/root/tz08a-work",
)
ALWAYS_PRESERVED = (
    "/root/tz06-work/tz06-observations.csv",
    "/root/tz08a-work/tz08a-observations.csv",
)
FORENSICS = "/root/btc-forensics"
FLATTEN_BASE = "/root"

HEX64 = re.compile(r"^[0-9a-f]{64}$")


class Blocked(Exception):
    """A free-space read fell below the floor that applies to it."""


RESULT = {}


# ---------------------------------------------------------------------------------------------
# Plumbing


def utc(t):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))


def write_out(name, text):
    """The only write in this script, and only under WORK."""
    path = os.path.realpath(os.path.join(WORK, name))
    assert path.startswith(WORK + "/"), path
    with open(path, "w") as fh:
        fh.write(text)


def dump(name, obj):
    write_out(name + ".json", json.dumps(obj, indent=1, sort_keys=True) + "\n")


def load(name):
    with open(os.path.join(WORK, name + ".json"), "rb") as fh:
        return json.load(fh)


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout


def git_show(path):
    return subprocess.run(["git", "-C", HERE, "show", "origin/main:" + path],
                          capture_output=True, check=True).stdout


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def n(x):
    return f"{x:,}"


def depth(path):
    return 0 if path == "/" else path.count("/")


def is_project(path):
    return any(path == p or path.startswith(p + "/") for p in PROJECT_PATHS)


# ---------------------------------------------------------------------------------------------
# Readings


def df_read(floor=FLOOR_RUN):
    """One `df -B1` read of the filesystem holding the capture, timestamped, floor enforced."""
    t = time.time()
    size = run(["df", "-B1", "--output=source,size,used,avail", CAPTURE]).splitlines()[1].split()
    inodes = run(["df", "--output=itotal,iused,iavail", CAPTURE]).splitlines()[1].split()
    reading = {
        "utc": utc(t), "epoch": t, "source": size[0], "total": int(size[1]),
        "used": int(size[2]), "avail": int(size[3]), "inodes_total": int(inodes[0]),
        "inodes_used": int(inodes[1]),
    }
    RESULT.setdefault("df_reads", []).append(reading)
    if reading["avail"] < floor:
        raise Blocked(f"free {n(reading['avail'])} bytes at {reading['utc']} is below "
                      f"{n(floor)}")
    return reading


def du(root, max_depth, apparent=False):
    """`du -x -B1`, verbatim. Exit status 1 is a file vanishing mid-walk; it is recorded."""
    cmd = ["du", "-x", "-B1", f"--max-depth={max_depth}"]
    if apparent:
        cmd.append("--apparent-size")
    cmd.append(root)
    t = time.time()
    proc = subprocess.run(cmd, capture_output=True, text=True)
    rows = []
    for line in proc.stdout.splitlines():
        size, path = line.split("\t", 1)
        rows.append([int(size), path])
    assert proc.returncode in (0, 1), (cmd, proc.returncode, proc.stderr)
    assert rows and rows[-1][1] == root, (cmd, rows[-1:] if rows else rows)
    return {"command": " ".join(cmd), "utc": utc(t), "seconds": round(time.time() - t, 3),
            "returncode": proc.returncode, "stderr": proc.stderr.splitlines(), "rows": rows}


def interval_dirs():
    names = [e.name for e in os.scandir(INTERVALS) if e.is_dir(follow_symlinks=False)]
    return sorted(int(x) for x in names if x.isdigit()), len(names)


def recorder_state():
    """The recorder process, the newest start record and the interval directory census."""
    t = time.time()
    procs = []
    for pid in os.listdir("/proc"):
        if not pid.isdigit():
            continue
        try:
            with open(f"/proc/{pid}/cmdline", "rb") as fh:
                argv = [a.decode() for a in fh.read().split(b"\0") if a]
            with open(f"/proc/{pid}/stat", "rb") as fh:
                starttime = int(fh.read().rsplit(b")", 1)[1].split()[19])
            cwd = os.readlink(f"/proc/{pid}/cwd")
        except OSError:
            continue
        if "recorder.py" in argv:
            procs.append({"pid": int(pid), "argv": argv, "cwd": cwd, "starttime": starttime})
    start = None
    with open(RUNTIME, "rb") as fh:
        for line in fh:
            if b'"kind": "start"' in line:
                start = json.loads(line)
    t0s, entries = interval_dirs()
    return {"utc": utc(t), "epoch": t, "processes": sorted(procs, key=lambda p: p["pid"]),
            "start_record": start, "interval_count": len(t0s), "scandir_entries": entries,
            "newest_t0": t0s[-1] if t0s else None, "oldest_t0": t0s[0] if t0s else None}


def deleted_open(root_dev):
    """M4: regular files on the root filesystem that are unlinked and still held open."""
    entries = []
    for pid in sorted(int(p) for p in os.listdir("/proc") if p.isdigit()):
        fd_dir = f"/proc/{pid}/fd"
        try:
            fds = sorted(os.listdir(fd_dir), key=int)
            with open(f"/proc/{pid}/comm", "rb") as fh:
                comm = fh.read().decode().strip()
        except OSError:
            continue
        for fd in fds:
            link = f"{fd_dir}/{fd}"
            try:
                target = os.readlink(link)
                if not target.endswith(" (deleted)"):
                    continue
                st = os.stat(link)
            except OSError:
                continue
            if st.st_dev != root_dev or not stat.S_ISREG(st.st_mode):
                continue
            entries.append({"pid": pid, "comm": comm, "fd": int(fd), "target": target,
                            "size": st.st_size, "allocated": st.st_blocks * 512,
                            "inode": st.st_ino})
    unique = {e["inode"]: e for e in entries}
    return {"entries": entries, "unique_files": len(unique),
            "total_size": sum(e["size"] for e in unique.values()),
            "total_allocated": sum(e["allocated"] for e in unique.values())}


def m2(drill=None):
    """M2: `/` at depth 1, the seven at depth 2, and the three largest foreign subtrees at 3."""
    commands = [du("/", 1)]
    missing = [p for p in TOP_DEPTH2 if not os.path.isdir(p)]
    commands += [du(p, 2) for p in TOP_DEPTH2 if os.path.isdir(p)]
    if drill is None:
        candidates = {}
        for c in commands[1:]:
            for size, path in c["rows"]:
                if depth(path) == 2 and not is_project(path):
                    candidates[path] = size
        drill = sorted(candidates, key=lambda p: (-candidates[p], p))[:DRILL_COUNT]
    missing += [p for p in drill if not os.path.isdir(p)]
    commands += [du(p, 3) for p in drill if os.path.isdir(p)]
    # One value per directory: commands run from general to specific, so the last one to report
    # a path is the most specific one that covers it.
    canonical = {}
    for c in commands:
        for size, path in c["rows"]:
            canonical[path] = size
    return {"commands": commands, "missing": missing, "drill": drill, "canonical": canonical,
            "root_total": commands[0]["rows"][-1][0]}


def ordering(canonical):
    big = [p for p, size in canonical.items() if size >= REPORT_MIN]
    return sorted(big, key=lambda p: (-canonical[p], p))


def largest_files(root, count):
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for name in filenames:
            path = os.path.join(dirpath, name)
            try:
                st = os.lstat(path)
            except OSError:
                continue
            if stat.S_ISREG(st.st_mode):
                files.append({"path": path, "size": st.st_size,
                              "allocated": st.st_blocks * 512, "mtime": utc(st.st_mtime)})
    return sorted(files, key=lambda f: (-f["size"], f["path"]))[:count]


# ---------------------------------------------------------------------------------------------
# Subcommands


def cmd_gate(name):
    out = RESULT
    df = df_read(floor=FLOOR_START)
    out["df"] = df
    if df["avail"] < FLOOR_RUN:
        raise Blocked(f"free {n(df['avail'])} bytes at run start is below {n(FLOOR_RUN)}")

    state = recorder_state()
    out["state"] = state
    host = {
        "H1 capture directory holds interval directories":
            os.path.isdir(CAPTURE) and state["interval_count"] > 0,
        "H2 recorder running, newest start record carries the sha":
            len(state["processes"]) == 1 and state["start_record"] is not None
            and state["start_record"]["sha"] == START_SHA,
        "H3 filesystem is the device, at its total":
            df["source"] == DEVICE and df["total"] == DEVICE_TOTAL,
    }
    out["host"] = host

    map_text = git_show("SYSTEM-MAP.md").decode()
    revision = re.search(r"\*\*Revision string:\*\* `([^`]+)`", map_text).group(1)
    anchors = dict(re.findall(r"^\| `(A\d)` — [^|]+\| `([^`]+)` \|$", map_text, flags=re.M))
    out["revision"] = revision
    out["anchors"] = anchors

    rows = re.findall(r"^\| `([^`]+)` \| ([\d,—]+) \| ([\d,—]+) \| (\w+) \| (.+?) \|$",
                      map_text, flags=re.M)
    table = []
    for path, lines, nbytes, state_word, expected in rows:
        data = git_show(path)
        row = {"path": path, "state": state_word, "lines": data.count(b"\n"),
               "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
        if state_word == "frozen":
            row["expected_sha256"] = expected.strip("`")
            row["expected_lines"] = int(lines.replace(",", ""))
            row["expected_bytes"] = int(nbytes.replace(",", ""))
            row["match"] = (row["sha256"] == row["expected_sha256"]
                            and row["lines"] == row["expected_lines"]
                            and row["bytes"] == row["expected_bytes"])
        table.append(row)
    out["fingerprint"] = table
    by_path = {r["path"]: r["sha256"] for r in table}
    anchor_files = {a: by_path.get(p) or hashlib.sha256(git_show(p)).hexdigest()
                    for a, p in ANCHOR_FILES.items()}
    out["anchor_files"] = {a: {"path": ANCHOR_FILES[a], "sha256": s}
                           for a, s in anchor_files.items()}
    tz = git_show(TZ_FILE)
    out["tz_file"] = {"path": TZ_FILE, "lines": tz.count(b"\n"), "bytes": len(tz),
                      "sha256": hashlib.sha256(tz).hexdigest()}
    out["origin_main"] = run(["git", "-C", HERE, "rev-parse", "origin/main"]).strip()
    dump(name, out)

    print(f"## gate `{name}`\n")
    print(f"df at {df['utc']}: source `{df['source']}`, total `{n(df['total'])}`, "
          f"used `{n(df['used'])}`, available `{n(df['avail'])}`\n")
    print(f"recorder: {[(p['pid'], p['cwd']) for p in state['processes']]}; newest start "
          f"record sha `{state['start_record']['sha']}`, recv_ns "
          f"`{state['start_record']['recv_ns']}`; {state['interval_count']} interval "
          f"directories, newest T0 `{state['newest_t0']}`\n")
    for k, v in host.items():
        print(f"- {k}: **{v}**")
    print(f"\nrevision `{revision}` against `{MAP_REVISION}`; origin/main `{out['origin_main']}`\n")
    print("| anchor | map | TZ-09 | equal | file SHA-256 prefix |\n|---|---|---|---|---|")
    for a in sorted(ANCHORS):
        prefix = anchor_files[a][:12] if a in anchor_files else "—"
        print(f"| `{a}` | `{anchors.get(a)}` | `{ANCHORS[a]}` | {anchors.get(a) == ANCHORS[a]} "
              f"| `{prefix}` |")
    print("\n| path | lines | bytes | state | SHA-256 | matches the map |\n|---|---|---|---|---|---|")
    for r in table:
        print(f"| `{r['path']}` | {n(r['lines'])} | {n(r['bytes'])} | {r['state']} | "
              f"`{r['sha256']}` | {r.get('match', '—')} |")
    tzf = out["tz_file"]
    print(f"\n`{TZ_FILE}`: {tzf['lines']} lines, {n(tzf['bytes'])} bytes, `{tzf['sha256']}`")

    for k, v in host.items():
        assert v, k
    assert revision == MAP_REVISION, revision
    assert anchors == ANCHORS, anchors
    for a, s in anchor_files.items():
        assert s[:12] == ANCHORS[a], (a, s)
    frozen = [r for r in table if r["state"] == "frozen"]
    assert frozen and all(r["match"] for r in frozen), [r["path"] for r in frozen
                                                        if not r["match"]]
    print(f"\nV1 host gate 3 of 3; V9 frozen rows {sum(r['match'] for r in frozen)} of "
          f"{len(frozen)} matching; anchors {len(ANCHORS)} of {len(ANCHORS)}")


def cmd_snap(name, drill_from=None):
    out = RESULT
    out["df"] = df_read()
    drill = load(drill_from)["m2"]["drill"] if drill_from else None
    out["m2"] = m2(drill)
    out["m4"] = deleted_open(os.stat("/").st_dev)
    out["m4"]["df_used_minus_du_root"] = out["df"]["used"] - out["m2"]["root_total"]
    out["m5"] = {
        "tree": du(CAPTURE, 2),
        "tree_apparent": du(CAPTURE, 0, apparent=True),
        "intervals_apparent": du(INTERVALS, 0, apparent=True),
    }
    t0s, entries = interval_dirs()
    quotes = sum(os.path.isfile(os.path.join(INTERVALS, str(t), "quotes.jsonl.gz"))
                 for t in t0s)
    out["m5"].update({"interval_count": len(t0s), "scandir_entries": entries,
                      "with_quotes": quotes, "oldest_t0": t0s[0], "newest_t0": t0s[-1]})
    journal = subprocess.run(["journalctl", "--disk-usage"], capture_output=True, text=True)
    out["m7"] = {
        "journalctl": (journal.stdout + journal.stderr).strip(),
        "journalctl_returncode": journal.returncode,
        "var_log": du("/var/log", 2),
        "largest_files": largest_files("/var/log", 10),
    }
    out["state"] = recorder_state()
    out["df_after"] = df_read()
    dump(name, out)
    print_snap(name, out)


def cmd_show(name):
    """Print a snapshot already taken, without measuring anything again."""
    print_snap(name, load(name))


def print_snap(name, out):
    df, m2_, m4, m5, m7 = out["df"], out["m2"], out["m4"], out["m5"], out["m7"]
    print(f"## snapshot `{name}`\n")
    print(f"M1 df at {df['utc']}: total `{n(df['total'])}`, used `{n(df['used'])}`, available "
          f"`{n(df['avail'])}`; inodes total `{n(df['inodes_total'])}`, used "
          f"`{n(df['inodes_used'])}`. After the set, {out['df_after']['utc']}: available "
          f"`{n(out['df_after']['avail'])}`\n")
    print("M2 commands:\n")
    for c in m2_["commands"]:
        print(f"- `{c['command']}` at {c['utc']}, {c['seconds']} s, exit {c['returncode']}, "
              f"{len(c['rows'])} rows, {len(c['stderr'])} stderr lines")
    print(f"\nmissing: {m2_['missing']}; drilled to depth 3: {m2_['drill']}\n")
    print("| # | directory | bytes |\n|---|---|---|")
    for i, p in enumerate(ordering(m2_["canonical"]), 1):
        print(f"| {i} | `{p}` | {n(m2_['canonical'][p])} |")
    print(f"\nM4: df used `{n(df['used'])}` minus du `/` total `{n(m2_['root_total'])}` = "
          f"`{n(m4['df_used_minus_du_root'])}`; exceeds {n(M4_THRESHOLD)}: "
          f"{abs(m4['df_used_minus_du_root']) > M4_THRESHOLD}. Unlinked-open: "
          f"{len(m4['entries'])} descriptors, {m4['unique_files']} files, size "
          f"`{n(m4['total_size'])}`, allocated `{n(m4['total_allocated'])}`\n")
    if m4["entries"]:
        print("| pid | process | fd | file | size | allocated |\n|---|---|---|---|---|---|")
        for e in m4["entries"]:
            print(f"| {e['pid']} | `{e['comm']}` | {e['fd']} | `{e['target']}` | "
                  f"{n(e['size'])} | {n(e['allocated'])} |")
        print()
    print(f"M5: {m5['interval_count']} interval directories ({m5['scandir_entries']} entries), "
          f"{m5['with_quotes']} holding `quotes.jsonl.gz`, T0 `{m5['oldest_t0']}` … "
          f"`{m5['newest_t0']}`; tree `{n(m5['tree']['rows'][-1][0])}` on disk, "
          f"`{n(m5['tree_apparent']['rows'][-1][0])}` apparent\n")
    # The depth-2 listing is one row per interval directory; the rows above it print in full and
    # the interval rows as a summary. The JSON carries every row.
    print("| directory | bytes |\n|---|---|")
    for size, path in m5["tree"]["rows"]:
        if depth(path) <= depth(INTERVALS):
            print(f"| `{path}` | {n(size)} |")
    sizes = sorted(size for size, path in m5["tree"]["rows"] if depth(path) > depth(INTERVALS))
    largest = sorted(((size, path) for size, path in m5["tree"]["rows"]
                      if depth(path) > depth(INTERVALS)), key=lambda r: (-r[0], r[1]))[:5]
    print(f"\n{len(sizes)} interval directory rows: sum `{n(sum(sizes))}`, smallest "
          f"`{n(sizes[0])}`, median `{n(sizes[len(sizes) // 2])}`, largest `{n(sizes[-1])}`. "
          f"The five largest: " + ", ".join(f"`{os.path.basename(p)}` {n(s)}"
                                            for s, p in largest))
    print(f"\nM7: `journalctl --disk-usage` → `{m7['journalctl']}`\n")
    print("| directory | bytes |\n|---|---|")
    for size, path in sorted(m7["var_log"]["rows"], key=lambda r: (-r[0], r[1])):
        print(f"| `{path}` | {n(size)} |")
    print("\n| file | bytes | allocated | mtime |\n|---|---|---|---|")
    for f in m7["largest_files"]:
        print(f"| `{f['path']}` | {n(f['size'])} | {n(f['allocated'])} | {f['mtime']} |")


def cmd_v3(name, a, b):
    sa, sb = load(a), load(b)
    oa, ob = ordering(sa["m2"]["canonical"]), ordering(sb["m2"]["canonical"])
    dump(name, {"a": a, "b": b, "ordering_a": oa, "ordering_b": ob, "equal": oa == ob})
    print(f"## V3 `{a}` against `{b}`\n")
    print(f"| # | `{a}` | bytes | `{b}` | bytes |\n|---|---|---|---|---|")
    for i in range(max(len(oa), len(ob))):
        pa = oa[i] if i < len(oa) else "—"
        pb = ob[i] if i < len(ob) else "—"
        print(f"| {i + 1} | `{pa}` | {n(sa['m2']['canonical'].get(pa, 0))} | `{pb}` | "
              f"{n(sb['m2']['canonical'].get(pb, 0))} |")
    assert oa == ob, "V3: the ordering changed"
    print(f"\nV3: {len(oa)} of {len(oa)} directories in the same position")


def cmd_m3(name, t0_name, t1_name):
    t0, t1 = load(t0_name), load(t1_name)
    assert t0["m2"]["drill"] == t1["m2"]["drill"], "M3: the two runs are not one command set"
    start0, start1 = t0["df"]["epoch"], t1["df"]["epoch"]
    end0 = t0["df_after"]["epoch"]
    window = start1 - start0
    clear = start1 - end0
    fall = t0["df"]["avail"] - t1["df"]["avail"]
    c0, c1 = t0["m2"]["canonical"], t1["m2"]["canonical"]
    rows = []
    for path in sorted(set(c0) | set(c1)):
        b0, b1 = c0.get(path), c1.get(path)
        delta = (b1 or 0) - (b0 or 0)
        rows.append({"path": path, "t0": b0, "t1": b1, "delta": delta,
                     "per_day": round(delta * DAY / window)})
    rows.sort(key=lambda r: (-r["delta"], r["path"]))
    half = fall / 2
    satisfying = [r["path"] for r in rows if r["delta"] > half]
    named = [p for p in satisfying
             if not any(q != p and q.startswith(p.rstrip("/") + "/") for q in satisfying)]
    root_delta = t1["m2"]["root_total"] - t0["m2"]["root_total"]
    unlinked_change = t1["m4"]["total_allocated"] - t0["m4"]["total_allocated"]
    residual = fall - root_delta - unlinked_change
    cap0 = t0["m5"]["tree"]["rows"][-1][0]
    cap1 = t1["m5"]["tree"]["rows"][-1][0]
    capa0 = t0["m5"]["tree_apparent"]["rows"][-1][0]
    capa1 = t1["m5"]["tree_apparent"]["rows"][-1][0]
    drain = round(fall * DAY / window)
    out = {
        "t0": {"utc": t0["df"]["utc"], "epoch": start0, "avail": t0["df"]["avail"],
               "set_finished_utc": t0["df_after"]["utc"]},
        "t1": {"utc": t1["df"]["utc"], "epoch": start1, "avail": t1["df"]["avail"],
               "set_finished_utc": t1["df_after"]["utc"]},
        "window_seconds": window, "window_after_t0_set_seconds": clear, "fall": fall,
        "drain_per_day": drain, "rows": rows, "satisfying": satisfying, "named": named,
        "v5": {"fall": fall, "root_delta": root_delta, "unlinked_change": unlinked_change,
               "residual": residual},
        "m5": {"t0": cap0, "t1": cap1, "delta": cap1 - cap0,
               "per_day": round((cap1 - cap0) * DAY / window),
               "apparent_t0": capa0, "apparent_t1": capa1, "apparent_delta": capa1 - capa0,
               "apparent_per_day": round((capa1 - capa0) * DAY / window)},
    }
    out["m5"]["difference_from_map"] = out["m5"]["per_day"] - CAPTURE_RATE
    out["m5"]["apparent_difference_from_map"] = out["m5"]["apparent_per_day"] - CAPTURE_RATE
    dump(name, out)

    print(f"## M3 `{t0_name}` → `{t1_name}`\n")
    print(f"V4: t0 `{out['t0']['utc']}` (set finished {out['t0']['set_finished_utc']}), t1 "
          f"`{out['t1']['utc']}` (set finished {out['t1']['set_finished_utc']}); window "
          f"`{window:.3f}` s start to start, `{clear:.3f}` s from the end of the t0 set\n")
    print(f"df available `{n(t0['df']['avail'])}` → `{n(t1['df']['avail'])}`, fall "
          f"`{n(fall)}` bytes, `{n(drain)}` bytes/day. Half the fall: `{half:,.1f}`\n")
    moved = [r for r in rows if r["delta"] != 0]
    print(f"{len(rows)} directories measured, {len(moved)} with a non-zero delta:\n")
    print("| directory | bytes at t0 | bytes at t1 | delta | delta, bytes/day |\n"
          "|---|---|---|---|---|")
    for r in moved:
        b0 = "absent" if r["t0"] is None else n(r["t0"])
        b1 = "absent" if r["t1"] is None else n(r["t1"])
        print(f"| `{r['path']}` | {b0} | {b1} | {n(r['delta'])} | {n(r['per_day'])} |")
    print(f"\nDirectories whose delta alone exceeds half the fall: {satisfying}")
    print(f"Deepest of them: {named}\n")
    v5 = out["v5"]
    print(f"V5: fall `{n(fall)}` − du `/` delta `{n(root_delta)}` − unlinked-open allocated "
          f"change `{n(unlinked_change)}` = residual `{n(residual)}` bytes; exceeds "
          f"{n(V5_THRESHOLD)}: {abs(residual) > V5_THRESHOLD}\n")
    m5 = out["m5"]
    print(f"M5 growth: on disk `{n(m5['t0'])}` → `{n(m5['t1'])}`, `{n(m5['delta'])}` bytes, "
          f"`{n(m5['per_day'])}` bytes/day, `{n(m5['difference_from_map'])}` against the map's "
          f"`{n(CAPTURE_RATE)}`; apparent `{n(m5['apparent_delta'])}` bytes, "
          f"`{n(m5['apparent_per_day'])}` bytes/day, `{n(m5['apparent_difference_from_map'])}` "
          f"against it")
    assert window >= WINDOW_MIN and clear >= WINDOW_MIN, ("V4", window, clear)
    print(f"\nV4: {window:.3f} >= {WINDOW_MIN}, and {clear:.3f} >= {WINDOW_MIN}")


def cmd_m6(name, sample, archive, snap_name):
    snap = load(snap_name)
    t0s, _ = interval_dirs()
    oldest = t0s[:SAMPLE_SIZE]
    got = sorted(int(e.name) for e in os.scandir(sample) if e.is_dir(follow_symlinks=False))
    assert got == oldest, ("M6: the sample is not the twenty oldest", got, oldest)
    files = identical = 0
    for t in oldest:
        for entry in sorted(os.scandir(os.path.join(sample, str(t))), key=lambda e: e.name):
            files += 1
            original = os.path.join(INTERVALS, str(t), entry.name)
            identical += sha256_file(entry.path) == sha256_file(original)
    assert identical == files, ("M6: copy differs from original", identical, files)
    before = du(sample, 0)["rows"][-1][0]
    before_apparent = du(sample, 0, apparent=True)["rows"][-1][0]
    st = os.stat(archive)
    after, after_allocated = st.st_size, st.st_blocks * 512
    capture = dict((p, s) for s, p in snap["m5"]["tree"]["rows"])[INTERVALS]
    capture_apparent = snap["m5"]["intervals_apparent"]["rows"][-1][0]
    out = {
        "sample": sample, "archive": archive, "members": oldest, "files": files,
        "files_identical_to_originals": identical, "with_quotes": sum(
            os.path.isfile(os.path.join(sample, str(t), "quotes.jsonl.gz")) for t in oldest),
        "before_disk": before, "before_apparent": before_apparent,
        "archive_bytes": after, "archive_allocated": after_allocated,
        "ratio_disk": after_allocated / before, "ratio_apparent": after / before_apparent,
        "capture_intervals_disk": capture, "capture_intervals_apparent": capture_apparent,
        "projected_saving_disk": capture * (before - after_allocated) // before,
        "projected_saving_apparent": capture_apparent * (before_apparent - after)
        // before_apparent,
    }
    dump(name, out)
    print(f"## M6 `{name}`\n")
    print(f"sample: the {len(oldest)} oldest interval directories, T0 `{oldest[0]}` … "
          f"`{oldest[-1]}`, {files} files, {identical} of {files} byte-identical to their "
          f"originals by SHA-256, {out['with_quotes']} holding `quotes.jsonl.gz`\n")
    print("| quantity | bytes |\n|---|---|")
    print(f"| sample, on disk (`du -B1`) | {n(before)} |")
    print(f"| sample, apparent | {n(before_apparent)} |")
    print(f"| archive, size | {n(after)} |")
    print(f"| archive, allocated | {n(after_allocated)} |")
    print(f"| capture intervals, on disk, at `{snap_name}` | {n(capture)} |")
    print(f"| capture intervals, apparent, at `{snap_name}` | {n(capture_apparent)} |")
    print(f"| projected saving, on disk | {n(out['projected_saving_disk'])} |")
    print(f"| projected saving, apparent | {n(out['projected_saving_apparent'])} |")
    print(f"\nratio archive / sample: on disk `{out['ratio_disk']:.6f}`, apparent "
          f"`{out['ratio_apparent']:.6f}`")


def cmd_r1(name):
    inventory = []
    trees = []
    for root in ALLOW_LIST:
        assert os.path.isdir(root) and not os.path.islink(root), root
        count = total = allocated = 0
        other = {}
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames.sort()
            for entry in sorted(filenames) + [d for d in dirnames
                                              if os.path.islink(os.path.join(dirpath, d))]:
                path = os.path.join(dirpath, entry)
                st = os.lstat(path)
                if stat.S_ISREG(st.st_mode):
                    count += 1
                    total += st.st_size
                    allocated += st.st_blocks * 512
                    inventory.append({"tree": root, "path": path, "size": st.st_size,
                                      "sha256": sha256_file(path)})
                else:
                    kind = "symlink" if stat.S_ISLNK(st.st_mode) else oct(stat.S_IFMT(
                        st.st_mode))
                    other[kind] = other.get(kind, 0) + 1
        trees.append({"tree": root, "files": count, "bytes": total, "allocated": allocated,
                      "du": du(root, 0)["rows"][-1][0], "non_regular": other})

    # `--full-tree`: without it `ls-tree` resolves paths against the working directory, which is
    # `research/`, and would list no report at all.
    tree = run(["git", "-C", HERE, "ls-tree", "-r", "--full-tree", "--name-only", "origin/main"])
    reports = sorted(p for p in tree.splitlines() if p.startswith("CryptoReports/"))
    assert reports, "R2: no report found on origin/main"
    artifacts = ["SYSTEM-MAP.md"] + reports
    texts = {a: git_show(a).decode().lower() for a in artifacts}
    # A report may name a file by its hash abbreviated - `2570ed2ea4e6c48d...` - and section 5.3
    # keeps every file whose SHA-256 a committed artifact names. A run of at least eight hex
    # characters closed by an ellipsis names the file whose hash it begins.
    abbreviated = {a: set(re.findall(r"(?<![0-9a-f])([0-9a-f]{8,63})(?:\.\.\.|…)", texts[a]))
                   for a in artifacts}
    for f in inventory:
        assert HEX64.match(f["sha256"])
        f["named_by"] = [a for a in artifacts if f["sha256"] in texts[a]]
        f["named_abbreviated"] = [a for a in artifacts if a not in f["named_by"] and any(
            f["sha256"].startswith(run) for run in abbreviated[a])]
        f["unconditional"] = f["path"] in ALWAYS_PRESERVED
        f["preserved"] = bool(f["named_by"] or f["named_abbreviated"]) or f["unconditional"]
        f["prefix12_only"] = [a for a in artifacts if not f["preserved"]
                              and f["sha256"][:12] in texts[a]]
    for p in ALWAYS_PRESERVED:
        assert any(f["path"] == p for f in inventory), ("unconditional file absent", p)

    plan = []
    for f in inventory:
        if f["preserved"]:
            rel = os.path.relpath(f["path"], FLATTEN_BASE)
            directory, filename = os.path.split(rel)
            f["destination"] = os.path.join(FORENSICS,
                                            directory.replace("/", "--") + "--" + filename)
            plan.append(f)
    destinations = [f["destination"] for f in plan]
    assert len(set(destinations)) == len(destinations), "R3: two files flatten to one name"
    out = {"artifacts": artifacts, "trees": trees, "files": inventory}
    dump(name, out)
    write_out(name + "-plan.tsv", "".join(f"{f['path']}\t{f['destination']}\n" for f in plan))

    print(f"## R1 and R2 `{name}`\n")
    print(f"Searched {len(artifacts)} artifacts on origin/main: `SYSTEM-MAP.md` and "
          f"{len(artifacts) - 1} files in `CryptoReports/`.\n")
    print("| tree | regular files | bytes | allocated | `du -B1` | non-regular | preserved |\n"
          "|---|---|---|---|---|---|---|")
    for t in trees:
        kept = sum(f["preserved"] for f in inventory if f["tree"] == t["tree"])
        print(f"| `{t['tree']}/` | {t['files']} | {n(t['bytes'])} | {n(t['allocated'])} | "
              f"{n(t['du'])} | {t['non_regular'] or '—'} | {kept} |")
    print(f"\n| total | {len(inventory)} | {n(sum(t['bytes'] for t in trees))} | "
          f"{n(sum(t['allocated'] for t in trees))} | {n(sum(t['du'] for t in trees))} | | "
          f"{len(plan)} |\n")
    print("Preserved:\n\n| source | bytes | SHA-256 | named by | destination |\n"
          "|---|---|---|---|---|")
    for f in plan:
        why = ", ".join([f"`{a}`" for a in f["named_by"]]
                        + [f"`{a}`, abbreviated" for a in f["named_abbreviated"]]) or "—"
        if f["unconditional"]:
            why += " · unconditional, R2"
        print(f"| `{f['path']}` | {n(f['size'])} | `{f['sha256']}` | {why} | "
              f"`{os.path.basename(f['destination'])}` |")
    prefix = [f for f in inventory if f["prefix12_only"]]
    print(f"\nFiles whose 12-character prefix, and not whose full hash, appears in an artifact: "
          f"{len(prefix)}")
    for f in prefix:
        print(f"- `{f['path']}` `{f['sha256'][:12]}` in {f['prefix12_only']}")
    print("\nEvery regular file:\n\n| file | bytes | SHA-256 | preserved |\n|---|---|---|---|")
    for f in inventory:
        print(f"| `{f['path']}` | {n(f['size'])} | `{f['sha256']}` | {f['preserved']} |")


def cmd_v6(name, r1_name):
    plan = [f for f in load(r1_name)["files"] if f["preserved"]]
    rows = []
    for f in plan:
        src = sha256_file(f["path"])
        dst = sha256_file(f["destination"]) if os.path.isfile(f["destination"]) else None
        rows.append({"source": f["path"], "destination": f["destination"], "recorded": f["sha256"],
                     "source_now": src, "destination_now": dst,
                     "equal": src == dst == f["sha256"]})
    present = sorted(os.path.join(FORENSICS, x) for x in os.listdir(FORENSICS))
    expected = sorted(f["destination"] for f in plan)
    dump(name, {"rows": rows, "present": present, "expected": expected})
    print(f"## V6 `{name}`\n\n| destination | SHA-256 at source | SHA-256 at destination | "
          f"equal |\n|---|---|---|---|")
    for r in rows:
        print(f"| `{os.path.basename(r['destination'])}` | `{r['source_now']}` | "
              f"`{r['destination_now']}` | {r['equal']} |")
    equal = sum(r["equal"] for r in rows)
    print(f"\nV6: {equal} of {len(rows)} preserved files equal at source and destination; "
          f"`{FORENSICS}/` holds {len(present)} entries against {len(expected)} expected")
    assert equal == len(rows), "V6: a preserved copy differs from its source"
    assert present == expected, "V6: the forensics directory is not exactly the plan"


def cmd_df(name):
    RESULT["df"] = df_read()
    dump(name, RESULT)
    d = RESULT["df"]
    print(f"df `{name}` at {d['utc']}: used `{n(d['used'])}`, available `{n(d['avail'])}`")


def cmd_state(name):
    RESULT["df"] = df_read()
    RESULT["state"] = recorder_state()
    dump(name, RESULT)
    s = RESULT["state"]
    print(f"state `{name}` at {s['utc']}: recorder {[p['pid'] for p in s['processes']]}, start "
          f"sha `{s['start_record']['sha']}`, {s['interval_count']} interval directories, "
          f"newest T0 `{s['newest_t0']}`; available `{n(RESULT['df']['avail'])}`")


def _pid(state):
    procs = state["state"]["processes"]
    assert len(procs) == 1, procs
    return procs[0]["pid"], procs[0]["starttime"]


def cmd_v7(name, a, b):
    sa, sb = load(a), load(b)
    pa, pb = _pid(sa), _pid(sb)
    ca, cb = sa["state"]["interval_count"], sb["state"]["interval_count"]
    dump(name, {"pid": [pa, pb], "count": [ca, cb]})
    print(f"V7: pid {pa[0]} (start tick {pa[1]}) → {pb[0]} (start tick {pb[1]}); interval "
          f"directories {ca} → {cb}")
    assert pa == pb, "V7: the recorder's pid changed"
    assert cb >= ca, "V7: the interval directory count fell"
    print("V7: 2 of 2")


def cmd_v8(name, a, b):
    sa, sb = load(a), load(b)
    pa, pb = _pid(sa), _pid(sb)
    ha, hb = sa["state"]["start_record"], sb["state"]["start_record"]
    ta, tb = sa["state"]["newest_t0"], sb["state"]["newest_t0"]
    dump(name, {"pid": [pa, pb], "start": [ha, hb], "newest_t0": [ta, tb]})
    print(f"V8: pid {pa[0]} → {pb[0]}; start sha `{ha['sha']}` → `{hb['sha']}` (recv_ns "
          f"{ha['recv_ns']} → {hb['recv_ns']}); newest T0 `{ta}` → `{tb}`")
    assert pa == pb, "V8: the recorder's pid changed"
    assert ha == hb and hb["sha"] == START_SHA, "V8: the start record changed"
    assert tb > ta, "V8: no newer interval directory"
    print("V8: 3 of 3")


def cmd_r5(name, a, b):
    da, db = load(a)["df"], load(b)["df"]
    diff = db["avail"] - da["avail"]
    dump(name, {"before": da, "after": db, "difference": diff})
    print(f"R5: available `{n(da['avail'])}` at {da['utc']} → `{n(db['avail'])}` at "
          f"{db['utc']}; difference `{n(diff)}` bytes")
    assert diff >= 0, "R5: free space fell across R4"
    print("R5: not negative, asserted")


def cmd_retention(name, m3_name, df_name):
    m3 = load(m3_name)
    free = load(df_name)["df"]
    drain = m3["drain_per_day"]
    alarm = FLOOR_START + 3 * drain
    days = (free["avail"] - FLOOR_START) / drain if drain > 0 else None
    out = {"F": FLOOR_START, "D": drain, "A": alarm, "free": free["avail"],
           "free_utc": free["utc"], "free_minus_A": free["avail"] - alarm, "days_to_F": days}
    dump(name, out)
    print(f"F `{n(FLOOR_START)}`; D `{n(drain)}` bytes/day; A = F + 3 × D = `{n(alarm)}`; "
          f"free `{n(free['avail'])}` at {free['utc']}, `{n(free['avail'] - alarm)}` against A; "
          f"days to F at D: " + (f"`{days:.2f}`" if days is not None else "undefined, D <= 0"))


def cmd_v10(name, *names):
    rows = []
    for x in names:
        d = load(x)["df"]
        rows.append({"name": x, "utc": d["utc"], "avail": d["avail"], "used": d["used"]})
    dump(name, rows)
    print("| instant | UTC | available | used |\n|---|---|---|---|")
    for r in rows:
        print(f"| `{r['name']}` | {r['utc']} | {n(r['avail'])} | {n(r['used'])} |")


COMMANDS = {
    "gate": cmd_gate, "snap": cmd_snap, "show": cmd_show, "v3": cmd_v3, "m3": cmd_m3, "m6": cmd_m6,
    "r1": cmd_r1, "v6": cmd_v6, "df": cmd_df, "state": cmd_state, "v7": cmd_v7, "v8": cmd_v8,
    "r5": cmd_r5, "retention": cmd_retention, "v10": cmd_v10,
}


def main(argv):
    command, name, rest = argv[1], argv[2], argv[3:]
    if command == "snap" and rest[:1] == ["--drill"]:
        rest = [rest[1]]
    try:
        COMMANDS[command](name, *rest)
    except Blocked as exc:
        RESULT["blocked"] = str(exc)
        dump(name, RESULT)
        print(f"BLOCKED: {exc}")
        return 2 if command == "gate" and "run start" not in str(exc) else 3
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
