#!/usr/bin/env python3
"""TZ-04a Tier A recorder: continuous read-only capture of S1-S4, S6 and S7.

TZ-05a adds Tier C to the same process: seven order-book snapshots per interval per token id,
issued as plain GETs to the public CLOB endpoint and stored exactly as returned. It also
applies TZ-05a section 5 R-b, which rejects an invalid SNTP reply at the point of reception.

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
S7_DEADLINE_S = 3600        # stop polling for the venue's outcome at T0 + 3600
S7_POLL_S = 15
RECV_TIMEOUT_S = 30         # no frame for this long means the socket is dead
NTP_BURST = 4               # SNTP queries per server per round; the lowest-delay reply is kept
QUOTE_TIMEOUT_S = 8         # shorter than the 20 s between the two closest Tier C checkpoints


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


class SntpRejected(Exception):
    """An SNTP reply that TZ-05a section 5 R-b forbids turning into an offset."""

    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


def sntp_reject_reason(fields, t3, host_now):
    """Why this reply must be rejected, or None when it may be used.

    TZ-05a section 5 R-b, in the order the TZ lists the conditions. The check is here, at
    reception, and not on the samples afterwards: a reply that fails it never becomes an
    offset and is counted as a rejection instead.
    """
    leap = (fields[0] >> 30) & 0x3
    stratum = (fields[0] >> 16) & 0xFF
    if leap == 3:
        return "leap-indicator-3"
    if stratum == 0:
        return "stratum-0"
    if stratum > 15:
        return "stratum-above-15"
    if fields[10] == 0 and fields[11] == 0:
        return "zero-transmit-timestamp"
    if abs(t3 - host_now) > config.SNTP_MAX_SKEW_S:
        return "transmit-timestamp-beyond-%ds" % config.SNTP_MAX_SKEW_S
    return None


def sntp_offset(host, timeout=5):
    """One SNTP round trip. Returns (offset_seconds, round_trip_seconds).

    Raises SntpRejected when the reply fails the R-b validation above.
    """
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
    reason = sntp_reject_reason(fields, t3, t4)
    if reason is not None:
        raise SntpRejected(reason)
    return ((t2 - t1) + (t3 - t4)) / 2, (t4 - t1) - (t3 - t2)


def best_sample(samples):
    """The standard NTP clock filter: of (offset, round_trip) pairs, keep the lowest delay.

    One SNTP reply is only accurate to half its round trip, so the lowest-delay reply of a
    burst is the one least contaminated by path asymmetry.
    """
    return min(samples, key=lambda s: s[1])


def sntp_best(host, burst=NTP_BURST):
    """A burst against one resolved address.

    Returns (ip, offset_s, rtt_s, accepted, rejected), where `rejected` maps each R-b reason
    to the number of replies it rejected. A burst whose every reply is rejected still returns,
    with `offset_s` and `rtt_s` None, so that the rejections are recorded rather than lost.
    """
    ip = socket.gethostbyname(host)
    samples, rejected = [], {}
    for _ in range(burst):
        try:
            samples.append(sntp_offset(ip))
        except SntpRejected as exc:
            rejected[exc.reason] = rejected.get(exc.reason, 0) + 1
        except Exception:
            pass
    if not samples:
        return ip, None, None, 0, rejected
    offset, rtt = best_sample(samples)
    return ip, offset, rtt, len(samples), rejected


def last_frame_ns(root):
    """The newest recv_ns any earlier process wrote, read back off disk; 0 when there is none.

    A restart's outage begins at the last frame actually captured, not at the moment the new
    process happens to start and not at the beginning of time.
    """
    base = os.path.join(root, config.SERIES)
    if not os.path.isdir(base):
        return 0
    newest = 0
    for name in sorted((n for n in os.listdir(base) if n.isdigit()), key=int)[-4:]:
        for stream in config.STREAM_FILES:
            for suffix in (".jsonl", ".jsonl.gz"):
                path = os.path.join(base, name, stream + suffix)
                if not os.path.exists(path):
                    continue
                opener = gzip.open if suffix.endswith(".gz") else open
                try:
                    with opener(path, "rt", encoding="utf-8") as fh:
                        for line in fh:
                            try:
                                newest = max(newest, json.loads(line)["recv_ns"])
                            except (ValueError, KeyError):
                                pass            # a line torn by the previous process's death
                except (OSError, EOFError):
                    pass
    return newest


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


def fetch_status(url, timeout=15):
    """One GET. Returns (http_status, body_text).

    TZ-05a section 3 stores a non-200 reply as received, with its status, so a 4xx or 5xx is
    a result here and not an exception. Only a read that produced no reply at all raises.
    """
    import urllib.error
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": config.USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as err:
        return err.code, err.read().decode("utf-8", "replace")


class Recorder:
    def __init__(self):
        self.writers = {}            # (t0, stream) -> file handle
        self.live = set()            # intervals with a lifecycle task running
        self.done = set()            # intervals already closed; never reopened
        self.stopping = False
        self.stop_reason = None
        self.sha = git_sha()
        self.runtime_path = os.path.join(config.ROOT, "runtime.jsonl")
        self.runtime = []            # every runtime record, including earlier processes'
        self.last_rx_ns = 0          # the last moment anything arrived on the socket

    # ---- runtime log -------------------------------------------------------------

    def load_runtime(self):
        """Earlier processes' records, so a slice spanning a restart is still whole."""
        if not os.path.exists(self.runtime_path):
            return
        with open(self.runtime_path, "rt", encoding="utf-8") as fh:
            for line in fh:
                try:
                    self.runtime.append(json.loads(line))
                except ValueError:
                    pass

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
            # Tier C reads the S6 document the line above captured, so it starts after it.
            # Its last checkpoint is T0 + 290, well inside the window closing at T0 + 333.
            quotes = asyncio.create_task(self.quotes(t0, path))
            await sleep_until(t0 + config.POST_S + GRACE_S)
            await asyncio.gather(quotes, return_exceptions=True)
            for stream in config.STREAM_FILES:
                fh = self.writers.pop((t0, stream), None)
                if fh is not None:
                    fh.close()
            self.done.add(t0)
            await self.close_interval(t0, path)
        except Exception as exc:            # a bad interval must not take the run down
            log("interval %d failed to close: %r" % (t0, exc))
        finally:
            self.live.discard(t0)

    async def close_interval(self, t0, path):
        for stream in config.STREAM_FILES + [config.QUOTES_STEM]:
            src = os.path.join(path, stream + ".jsonl")
            if os.path.exists(src):
                gzip_file(src, src + ".gz")
                os.remove(src)
        await self.fetch_s7(t0, path)
        self.write_runtime_slice(t0, path)
        doc = manifest.write(path)
        log("closed %d complete=%s quotes_complete=%s msgs=%s" % (
            t0, doc["complete"], doc["quotes_complete"],
            {s: doc["streams"][s]["messages"] for s in config.STREAM_FILES}))
        self.check_floors("close of interval %d" % t0)

    async def recover(self):
        """Close intervals an earlier process captured but never finished.

        A restart must not orphan data. A directory whose window has ended but which has no
        manifest is gzipped, given its S7 and its runtime slice, and closed like any other.
        Its S6 is never fetched late: a directory that missed it at the open stays without it.
        """
        base = os.path.join(config.ROOT, config.SERIES)
        if not os.path.isdir(base):
            return
        now = time.time()
        for name in sorted((n for n in os.listdir(base) if n.isdigit()), key=int):
            t0, path = int(name), os.path.join(base, name)
            if os.path.exists(os.path.join(path, manifest.MANIFEST_NAME)):
                continue
            if t0 + config.POST_S + GRACE_S > now:
                continue                    # window still open: the scheduler reopens it
            self.done.add(t0)
            log("recovering interval %d" % t0)
            asyncio.create_task(self.recover_one(t0, path))

    async def recover_one(self, t0, path):
        self.live.add(t0)
        try:
            await self.close_interval(t0, path)
        except Exception as exc:
            log("interval %d failed to recover: %r" % (t0, exc))
        finally:
            self.live.discard(t0)

    async def fetch_s6(self, t0, path):
        target = os.path.join(path, "gamma.json")
        if os.path.exists(target):
            return                          # captured at the open by an earlier process
        await sleep_until(t0 + S6_FETCH_OFFSET_S)
        url = config.GAMMA_MARKET_BY_SLUG.format(slug=config.slug_for(t0))
        for _ in range(5):
            try:
                body = await asyncio.to_thread(fetch, url)
                # Stored whole and unparsed, exactly as the venue returned it.
                with open(target, "wb") as fh:
                    fh.write(body)
                return
            except Exception:
                await asyncio.sleep(3)
        log("S6 fetch failed for %d" % t0)

    async def fetch_s7(self, t0, path):
        if manifest.resolution_present(path):
            return
        url = config.GAMMA_MARKET_BY_SLUG.format(slug=config.slug_for(t0))
        deadline = t0 + S7_DEADLINE_S
        while time.time() < deadline:
            try:
                body = await asyncio.to_thread(fetch, url)
                doc = json.loads(body)
                market = doc[0] if isinstance(doc, list) else doc
                meta = (market.get("events") or [{}])[0].get("eventMetadata")
                if manifest.resolved_outcome(market) is not None and meta:
                    with open(os.path.join(path, "resolution.json"), "wb") as fh:
                        fh.write(body)
                    return
            except Exception:
                pass
            await asyncio.sleep(S7_POLL_S)
        log("S7 unresolved at deadline for %d" % t0)

    # ---- Tier C ------------------------------------------------------------------

    def tokens_for(self, t0, path):
        """The market's token ids, read out of the S6 document this interval already holds.

        TZ-05a section 3 names the source: the Gamma document captured as S6, which carries
        `clobTokenIds` and `outcomes` as parallel JSON-encoded arrays. Nothing is fetched
        again for this, and nothing about the ids is interpreted here.
        """
        try:
            with open(os.path.join(path, "gamma.json"), "rt", encoding="utf-8") as fh:
                doc = json.load(fh)
        except (OSError, ValueError):
            return []
        market = doc[0] if isinstance(doc, list) else doc
        try:
            ids = json.loads(market["clobTokenIds"])
        except (KeyError, TypeError, ValueError):
            return []
        return [str(i) for i in ids] if isinstance(ids, list) else []

    async def one_quote(self, tau, token_id):
        """One checkpoint read, returned as the line that will be written for it.

        `recv_ns` is stamped when the reply lands, exactly as every other stream stamps it.
        A read that produced no reply is recorded with a null status and null body: TZ-05a
        section 3 forbids retrying it into the next checkpoint's slot and forbids inventing
        a value for it.
        """
        url = config.CLOB_BOOK_BY_TOKEN.format(token_id=token_id)
        try:
            status, body = await asyncio.to_thread(fetch_status, url, QUOTE_TIMEOUT_S)
        except Exception as exc:
            recv_ns, mono_ns = now_pair()
            rec = {"recv_ns": recv_ns, "mono_ns": mono_ns, "tau": tau, "token_id": token_id,
                   "status": None, "raw": None, "error": repr(exc)}
        else:
            recv_ns, mono_ns = now_pair()
            rec = {"recv_ns": recv_ns, "mono_ns": mono_ns, "tau": tau, "token_id": token_id,
                   "status": status, "raw": body}
        return json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n"

    async def quotes(self, t0, path):
        """TZ-05a section 3: seven checkpoints, one read per token id at each of them."""
        tokens = self.tokens_for(t0, path)
        if not tokens:
            log("interval %d has no token ids: Tier C reads nothing" % t0)
            return
        ahead = config.quote_checkpoints_ahead(t0, time.time())
        if len(ahead) < len(config.QUOTE_TAUS):
            log("interval %d: %d checkpoints had already passed and are not read"
                % (t0, len(config.QUOTE_TAUS) - len(ahead)))
        out = os.path.join(path, config.QUOTES_STEM + ".jsonl")
        with open(out, "at", encoding="utf-8", buffering=1) as fh:
            for tau, when in ahead:
                await sleep_until(when)
                lines = await asyncio.gather(
                    *(self.one_quote(tau, token_id) for token_id in tokens))
                for line in lines:
                    fh.write(line)

    def write_runtime_slice(self, t0, path):
        """The recorder state this interval's manifest needs, copied into the directory.

        Without this the manifest could not be rebuilt from the directory alone and V5 would
        be testing nothing. The sha is that of every process that captured part of the window.
        """
        lo = (t0 - config.PRE_S) * 10 ** 9
        hi = (t0 + config.POST_S) * 10 ** 9
        starts = sorted((r for r in self.runtime if r.get("kind") == "start"),
                        key=lambda r: r["recv_ns"])
        active = ([r for r in starts if r["recv_ns"] <= lo][-1:]
                  + [r for r in starts if lo < r["recv_ns"] <= hi])
        out = [{"kind": "recorder", "recv_ns": r["recv_ns"], "sha": r["sha"]} for r in active]
        if not out:
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
                    got = await asyncio.to_thread(sntp_best, host)
                except Exception:
                    got = None
                if got is not None:
                    ip, offset, rtt, replies, rejected = got
                    self.record({"kind": "clock", "recv_ns": time.time_ns(), "server": host,
                                 "ip": ip, "burst": replies,
                                 "offset_ms": None if offset is None else offset * 1000.0,
                                 "rtt_ms": None if rtt is None else rtt * 1000.0,
                                 "rejected": rejected,
                                 "rejected_count": sum(rejected.values())})
            await asyncio.sleep(config.NTP_SAMPLE_S)

    # ---- socket ------------------------------------------------------------------

    async def rtds(self):
        subs = [{"topic": t, "type": "*", "filters": f}
                for t, (f, _s) in config.TIER_A.items()]
        message = json.dumps({"action": "subscribe", "subscriptions": subs})
        # The start-up outage runs from the last frame any earlier process wrote to disk.
        down_since, detected, reason = last_frame_ns(config.ROOT), time.time_ns(), "startup"
        while not (self.stopping and not self.live):
            try:
                async with websockets.connect(config.RTDS_URL, open_timeout=20,
                                              ping_interval=None, max_size=None) as ws:
                    await ws.send(message)
                    up_ns = time.time_ns()
                    self.record({"kind": "disconnect", "start_recv_ns": down_since,
                                 "detected_recv_ns": detected, "end_recv_ns": up_ns,
                                 "reason": reason})
                    self.last_rx_ns = up_ns
                    log("RTDS connected")
                    pinger = asyncio.create_task(self.ping(ws))
                    try:
                        while True:
                            raw = await asyncio.wait_for(ws.recv(), timeout=RECV_TIMEOUT_S)
                            recv_ns, mono_ns = now_pair()
                            self.last_rx_ns = recv_ns
                            if isinstance(raw, bytes):
                                raw = raw.decode("utf-8", "replace")
                            if not raw or raw.strip() in ("PONG", "PING"):
                                continue
                            self.store(raw, recv_ns, mono_ns)
                    finally:
                        pinger.cancel()
            except Exception as exc:
                log("RTDS drop: %r" % (exc,))
            # The outage began at the last thing received, not when the silence was noticed.
            detected = time.time_ns()
            down_since = self.last_rx_ns or detected
            reason = "reconnect"
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
        self.load_runtime()
        log("recorder sha=%s root=%s" % (self.sha, config.ROOT))
        # TZ-04a section 4: both floors are checked before the first frame is written.
        free, used = disk_free_bytes(), tree_bytes(config.ROOT)
        self.record({"kind": "start", "recv_ns": time.time_ns(), "sha": self.sha,
                     "free_bytes": free, "captured_bytes": used})
        log("pre-run floors: free=%d (floor %d) captured=%d (cap %d)"
            % (free, config.FREE_SPACE_FLOOR_BYTES, used, config.SELF_CAP_BYTES))
        if not self.check_floors("start-up"):
            log("refusing to start: a section 4 floor is already breached")
            return 1
        await self.recover()
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
