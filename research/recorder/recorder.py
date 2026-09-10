#!/usr/bin/env python3
"""TZ-04a Tier A recorder: continuous read-only capture of S1-S4, S6 and S7.

Read-only by construction. There is no order path, no CLOB authentication, no wallet, key,
signer or credential anywhere in this file, and no pricing arithmetic: frames are routed by
topic and written byte-for-byte as received.

Run:  python3 recorder.py            # runs until a section 4 floor is reached
"""

import asyncio
import gzip
import json
import os
import shutil
import socket
import struct
import subprocess
import sys
import time

import websockets

import config
import manifest

GRACE_S = 3                 # let in-flight frames land before a window's files are closed
S6_FETCH_OFFSET_S = 5       # the market is live a moment after T0
S7_DEADLINE_S = 900         # stop polling for the venue's outcome at T0 + 900
S7_POLL_S = 15
RECV_TIMEOUT_S = 30         # no frame for this long means the socket is dead


def log(msg):
    sys.stderr.write("%s %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), msg))
    sys.stderr.flush()


def now_pair():
    """The two clocks every captured line carries."""
    return time.time_ns(), time.monotonic_ns()


def git_sha():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        out = subprocess.run(["git", "-C", here, "rev-parse", "HEAD"],
                             capture_output=True, text=True, timeout=10)
        return out.stdout.strip() if out.returncode == 0 else "unknown"
    except Exception:
        return "unknown"


def sntp_offset(host, timeout=5):
    """One SNTP round trip. Returns (offset_seconds, round_trip_seconds)."""
    pkt = b"\x1b" + 47 * b"\0"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    try:
        t1 = time.time()
        sock.sendto(pkt, (host, 123))
        data, _ = sock.recvfrom(48)
        t4 = time.time()
    finally:
        sock.close()
    fields = struct.unpack("!12I", data)
    t2 = fields[8] + fields[9] / 2 ** 32 - 2208988800
    t3 = fields[10] + fields[11] / 2 ** 32 - 2208988800
    return ((t2 - t1) + (t3 - t4)) / 2, (t4 - t1) - (t3 - t2)


def disk_free_bytes():
    return shutil.disk_usage(config.ROOT).free


def tree_bytes(root):
    total = 0
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            try:
                total += os.lstat(os.path.join(dirpath, name)).st_size
            except OSError:
                pass
    return total


def gzip_file(src, dst):
    """Compress with a zeroed header so the same input always gives the same bytes."""
    with open(src, "rb") as fin, open(dst, "wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, compresslevel=9, mtime=0) as fout:
            shutil.copyfileobj(fin, fout)


def fetch(url, timeout=15):
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": config.USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


class Recorder:
    def __init__(self):
        self.writers = {}            # (t0, stream) -> file handle
        self.live = set()            # intervals with a lifecycle task running
        self.done = set()            # intervals already closed; never reopened
        self.stopping = False
        self.stop_reason = None
        self.sha = git_sha()
        self.runtime_path = os.path.join(config.ROOT, "runtime.jsonl")
        self.runtime = []            # in-memory mirror, for the per-interval slices
        self.connected_since = None

    # ---- runtime log -------------------------------------------------------------

    def record(self, rec):
        self.runtime.append(rec)
        with open(self.runtime_path, "at", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, sort_keys=True) + "\n")

    # ---- resource floors ---------------------------------------------------------

    def check_floors(self, where):
        """TZ-04a section 4. Two independent stops, whichever is reached first."""
        free = disk_free_bytes()
        used = tree_bytes(config.ROOT)
        if free < config.FREE_SPACE_FLOOR_BYTES:
            self.halt("free-space floor reached at %s: %d bytes free, floor is %d"
                      % (where, free, config.FREE_SPACE_FLOOR_BYTES))
            return False
        if used >= config.SELF_CAP_BYTES:
            self.halt("self-cap reached at %s: %d bytes captured, cap is %d"
                      % (where, used, config.SELF_CAP_BYTES))
            return False
        return True

    def halt(self, reason):
        if self.stopping:
            return
        self.stopping = True
        self.stop_reason = reason
        log("!!! STOP " + reason)
        log("!!! no new interval is opened; open intervals finish and are closed cleanly")
        log("!!! nothing is deleted - retention is an Architect decision (TZ-04a section 4)")
        self.record({"kind": "halt", "recv_ns": time.time_ns(), "reason": reason})

    # ---- capture -----------------------------------------------------------------

    def writer(self, t0, stream):
        key = (t0, stream)
        fh = self.writers.get(key)
        if fh is not None:
            return fh
        if t0 in self.done or (self.stopping and t0 not in self.live):
            return None
        path = config.interval_dir(t0)
        os.makedirs(path, exist_ok=True)
        fh = open(os.path.join(path, stream + ".jsonl"), "at", encoding="utf-8", buffering=1)
        self.writers[key] = fh
        return fh

    def store(self, raw, recv_ns, mono_ns):
        try:
            topic = json.loads(raw).get("topic")
        except Exception:
            return
        entry = config.TIER_A.get(topic)
        if entry is None:
            return
        stream = entry[1]
        # The line format is fixed by TZ-04a section 4: these three keys and nothing else.
        line = json.dumps({"recv_ns": recv_ns, "mono_ns": mono_ns, "raw": raw},
                          ensure_ascii=False, separators=(",", ":")) + "\n"
        for t0 in config.intervals_for(recv_ns / 1e9):
            fh = self.writer(t0, stream)
            if fh is not None:
                fh.write(line)

    # ---- interval lifecycle ------------------------------------------------------

    async def run_interval(self, t0):
        self.live.add(t0)
        path = config.interval_dir(t0)
        os.makedirs(path, exist_ok=True)
        try:
            await self.fetch_s6(t0, path)
            await sleep_until(t0 + config.POST_S + GRACE_S)
            for stream in config.STREAM_FILES:
                fh = self.writers.pop((t0, stream), None)
                if fh is not None:
                    fh.close()
            self.done.add(t0)
            for stream in config.STREAM_FILES:
                src = os.path.join(path, stream + ".jsonl")
                if os.path.exists(src):
                    gzip_file(src, src + ".gz")
                    os.remove(src)
            await self.fetch_s7(t0, path)
            self.write_runtime_slice(t0, path)
            doc = manifest.write(path)
            log("closed %d complete=%s msgs=%s" % (
                t0, doc["complete"],
                {s: doc["streams"][s]["messages"] for s in config.STREAM_FILES}))
            self.check_floors("close of interval %d" % t0)
        except Exception as exc:            # a bad interval must not take the run down
            log("interval %d failed to close: %r" % (t0, exc))
        finally:
            self.live.discard(t0)

    async def fetch_s6(self, t0, path):
        await sleep_until(t0 + S6_FETCH_OFFSET_S)
        url = config.GAMMA_MARKET_BY_SLUG.format(slug=config.slug_for(t0))
        for _ in range(5):
            try:
                body = await asyncio.to_thread(fetch, url)
                # Stored whole and unparsed, exactly as the venue returned it.
                with open(os.path.join(path, "gamma.json"), "wb") as fh:
                    fh.write(body)
                return
            except Exception:
                await asyncio.sleep(3)
        log("S6 fetch failed for %d" % t0)

    async def fetch_s7(self, t0, path):
        url = config.GAMMA_MARKET_BY_SLUG.format(slug=config.slug_for(t0))
        deadline = t0 + S7_DEADLINE_S
        while time.time() < deadline:
            try:
                body = await asyncio.to_thread(fetch, url)
                doc = json.loads(body)
                market = doc[0] if isinstance(doc, list) else doc
                meta = (market.get("events") or [{}])[0].get("eventMetadata")
                if market.get("closed") and market.get("outcomePrices") and meta:
                    with open(os.path.join(path, "resolution.json"), "wb") as fh:
                        fh.write(body)
                    return
            except Exception:
                pass
            await asyncio.sleep(S7_POLL_S)
        log("S7 unresolved at deadline for %d" % t0)

    def write_runtime_slice(self, t0, path):
        """The recorder state this interval's manifest needs, copied into the directory.

        Without this the manifest could not be rebuilt from the directory alone and V5 would
        be testing nothing.
        """
        lo = (t0 - config.PRE_S) * 10 ** 9
        hi = (t0 + config.POST_S) * 10 ** 9
        out = [{"kind": "recorder", "recv_ns": lo, "sha": self.sha}]
        for rec in self.runtime:
            if rec.get("kind") == "disconnect":
                if rec["start_recv_ns"] <= hi and rec["end_recv_ns"] >= lo:
                    out.append(rec)
            elif rec.get("kind") == "clock":
                if lo <= rec["recv_ns"] <= hi:
                    out.append(rec)
        with open(os.path.join(path, manifest.RUNTIME_NAME), "wt", encoding="utf-8") as fh:
            for rec in out:
                fh.write(json.dumps(rec, sort_keys=True) + "\n")

    async def scheduler(self):
        while True:
            if not self.stopping:
                for t0 in config.intervals_for(time.time()):
                    if t0 not in self.live and t0 not in self.done:
                        asyncio.create_task(self.run_interval(t0))
            elif not self.live:
                return
            await asyncio.sleep(1)

    # ---- clock -------------------------------------------------------------------

    async def clock_sampler(self):
        while True:
            for host in config.NTP_SERVERS:
                try:
                    off, rtt = await asyncio.to_thread(sntp_offset, host)
                    self.record({"kind": "clock", "recv_ns": time.time_ns(), "server": host,
                                 "offset_ms": off * 1000.0, "rtt_ms": rtt * 1000.0})
                except Exception:
                    pass
            await asyncio.sleep(config.NTP_SAMPLE_S)

    # ---- socket ------------------------------------------------------------------

    async def rtds(self):
        subs = [{"topic": t, "type": "*", "filters": f}
                for t, (f, _s) in config.TIER_A.items()]
        message = json.dumps({"action": "subscribe", "subscriptions": subs})
        down_since = 0          # a startup gap is a disconnect from the beginning of time
        while not (self.stopping and not self.live):
            try:
                async with websockets.connect(config.RTDS_URL, open_timeout=20,
                                              ping_interval=None, max_size=None) as ws:
                    await ws.send(message)
                    up_ns = time.time_ns()
                    self.record({"kind": "disconnect", "start_recv_ns": down_since,
                                 "end_recv_ns": up_ns,
                                 "reason": "startup" if down_since == 0 else "reconnect"})
                    log("RTDS connected")
                    pinger = asyncio.create_task(self.ping(ws))
                    try:
                        while True:
                            raw = await asyncio.wait_for(ws.recv(), timeout=RECV_TIMEOUT_S)
                            if isinstance(raw, bytes):
                                raw = raw.decode("utf-8", "replace")
                            if not raw or raw.strip() in ("PONG", "PING"):
                                continue
                            recv_ns, mono_ns = now_pair()
                            self.store(raw, recv_ns, mono_ns)
                    finally:
                        pinger.cancel()
            except Exception as exc:
                log("RTDS drop: %r" % (exc,))
            down_since = time.time_ns()
            await asyncio.sleep(2)

    async def ping(self, ws):
        try:
            while True:
                await asyncio.sleep(config.RTDS_PING_S)
                await ws.send("PING")
        except Exception:
            return

    async def main(self):
        os.makedirs(config.ROOT, exist_ok=True)
        log("recorder sha=%s root=%s" % (self.sha, config.ROOT))
        self.record({"kind": "start", "recv_ns": time.time_ns(), "sha": self.sha})
        # TZ-04a section 4: both floors are checked before the first frame is written.
        free, used = disk_free_bytes(), tree_bytes(config.ROOT)
        log("pre-run floors: free=%d (floor %d) captured=%d (cap %d)"
            % (free, config.FREE_SPACE_FLOOR_BYTES, used, config.SELF_CAP_BYTES))
        if not self.check_floors("start-up"):
            log("refusing to start: a section 4 floor is already breached")
            return 1
        side = [asyncio.create_task(self.rtds()), asyncio.create_task(self.clock_sampler())]
        try:
            await self.scheduler()      # returns only once a floor stopped the run
        finally:
            for task in side:
                task.cancel()
            await asyncio.gather(*side, return_exceptions=True)
        log("stopped: %s" % (self.stop_reason or "scheduler exit"))
        return 0


async def sleep_until(epoch_s):
    delay = epoch_s - time.time()
    if delay > 0:
        await asyncio.sleep(delay)


if __name__ == "__main__":
    sys.exit(asyncio.run(Recorder().main()))
