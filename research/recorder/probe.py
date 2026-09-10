#!/usr/bin/env python3
"""TZ-04a Tier B probe: measure what the order book costs, without committing disk to it.

S5 is subscribed for exactly 60 minutes, following the market roll. Every frame is counted and
its byte length added to a running total, and the payload is then discarded - except during one
single interval, the first fully covered by the probe, whose frames are written to
`clob.jsonl.gz` in that interval's directory.

Read-only: the `market` channel is public and unauthenticated. No key, signer or order path.

Run:  python3 probe.py
"""

import asyncio
import json
import os
import statistics
import sys
import time

import websockets

import config
import recorder

PROBE_S = 3600
COUNTERS_PATH = os.path.join(config.ROOT, "tier-b-probe.json")


class Probe:
    def __init__(self):
        self.start = None
        self.end = None
        self.retained_t0 = None
        self.retained_fh = None
        self.frames = 0
        self.bytes = 0
        self.by_type = {}
        self.per_market = {}        # T0 -> {"frames": n, "bytes": n}
        self.markets = {}           # T0 -> [token_id, token_id]
        self.subscribed = set()

    # ---- market roll -------------------------------------------------------------

    async def tokens_for(self, t0):
        if t0 in self.markets:
            return self.markets[t0]
        url = config.GAMMA_MARKET_BY_SLUG.format(slug=config.slug_for(t0))
        for _ in range(4):
            try:
                doc = json.loads(await asyncio.to_thread(recorder.fetch, url))
                market = doc[0] if isinstance(doc, list) else doc
                tokens = json.loads(market["clobTokenIds"])
                self.markets[t0] = tokens
                return tokens
            except Exception:
                await asyncio.sleep(2)
        recorder.log("probe: no token ids for %d" % t0)
        self.markets[t0] = []
        return []

    async def roll(self, ws):
        """Subscribe each live market as it opens and drop it as it closes."""
        while time.time() < self.end:
            now = time.time()
            live = int(now // config.INTERVAL_S) * config.INTERVAL_S
            want = set(await self.tokens_for(live))
            add = want - self.subscribed
            drop = self.subscribed - want
            if add:
                await ws.send(json.dumps({"assets_ids": sorted(add), "operation": "subscribe"}))
                self.subscribed |= add
                recorder.log("probe: subscribed market %d" % live)
            if drop:
                await ws.send(json.dumps({"assets_ids": sorted(drop),
                                          "operation": "unsubscribe"}))
                self.subscribed -= drop
            # Prefetch the next market's tokens so the roll is not blocked on an HTTP call.
            await self.tokens_for(live + config.INTERVAL_S)
            await asyncio.sleep(1)

    # ---- retained interval -------------------------------------------------------

    def retained_window(self):
        """The first interval whose whole [T0-90, T0+330] window lies inside the probe."""
        t0 = (int(self.start // config.INTERVAL_S) + 1) * config.INTERVAL_S
        while t0 - config.PRE_S < self.start:
            t0 += config.INTERVAL_S
        return t0

    def retain(self, line, ts):
        t0 = self.retained_t0
        if not (t0 - config.PRE_S <= ts <= t0 + config.POST_S):
            return
        if self.retained_fh is None:
            path = config.interval_dir(t0)
            os.makedirs(path, exist_ok=True)
            self.retained_fh = open(os.path.join(path, "clob.jsonl"), "at",
                                    encoding="utf-8", buffering=1)
        self.retained_fh.write(line)

    # ---- run ---------------------------------------------------------------------

    async def pump(self, ws):
        while time.time() < self.end:
            try:
                raw = await asyncio.wait_for(ws.recv(), timeout=max(1.0, self.end - time.time()))
            except asyncio.TimeoutError:
                return
            if isinstance(raw, bytes):
                raw = raw.decode("utf-8", "replace")
            if not raw or raw.strip() in ("PING", "PONG"):
                continue
            recv_ns, mono_ns = recorder.now_pair()
            nbytes = len(raw.encode("utf-8"))
            self.frames += 1
            self.bytes += nbytes
            try:
                doc = json.loads(raw)
                first = doc[0] if isinstance(doc, list) and doc else doc
                etype = first.get("event_type", "unknown") if isinstance(first, dict) else "unknown"
            except Exception:
                etype = "unparsed"
            slot = self.by_type.setdefault(etype, {"frames": 0, "bytes": 0})
            slot["frames"] += 1
            slot["bytes"] += nbytes

            ts = recv_ns / 1e9
            live = int(ts // config.INTERVAL_S) * config.INTERVAL_S
            per = self.per_market.setdefault(live, {"frames": 0, "bytes": 0})
            per["frames"] += 1
            per["bytes"] += nbytes

            self.retain(json.dumps({"recv_ns": recv_ns, "mono_ns": mono_ns, "raw": raw},
                                   ensure_ascii=False, separators=(",", ":")) + "\n", ts)

    async def ping(self, ws):
        try:
            while True:
                await asyncio.sleep(config.CLOB_PING_S)
                await ws.send("PING")
        except Exception:
            return

    def finish(self):
        if self.retained_fh is not None:
            self.retained_fh.close()
        path = config.interval_dir(self.retained_t0)
        src = os.path.join(path, "clob.jsonl")
        retained = {"T0_epoch": self.retained_t0, "frames": 0, "raw_bytes": 0,
                    "gzipped_bytes": 0}
        if os.path.exists(src):
            with open(src, "rb") as fh:
                data = fh.read()
            retained["frames"] = data.count(b"\n")
            retained["raw_bytes"] = len(data)
            recorder.gzip_file(src, src + ".gz")
            os.remove(src)
            retained["gzipped_bytes"] = os.path.getsize(src + ".gz")

        # Only whole intervals, so the per-interval figures are not diluted by the partial
        # slots at the two ends of the probe.
        whole = {t0: v for t0, v in self.per_market.items()
                 if t0 >= self.start and t0 + config.INTERVAL_S <= self.end}
        frames = sorted(v["frames"] for v in whole.values())
        byts = sorted(v["bytes"] for v in whole.values())
        doc = {
            "probe_start_epoch": self.start,
            "probe_end_epoch": self.end,
            "probe_seconds": PROBE_S,
            "clob_ws_url": config.CLOB_WS_URL,
            "frames_total": self.frames,
            "bytes_total": self.bytes,
            "by_event_type": self.by_type,
            "markets_subscribed": len(self.markets),
            "whole_intervals": len(whole),
            "frames_per_interval": {
                "mean": statistics.fmean(frames) if frames else None,
                "median": statistics.median(frames) if frames else None,
                "max": max(frames) if frames else None,
            },
            "raw_bytes_per_interval": {
                "mean": statistics.fmean(byts) if byts else None,
                "median": statistics.median(byts) if byts else None,
                "max": max(byts) if byts else None,
            },
            "per_interval": {str(k): v for k, v in sorted(whole.items())},
            "retained_interval": retained,
        }
        with open(COUNTERS_PATH, "wt", encoding="utf-8") as fh:
            fh.write(json.dumps(doc, sort_keys=True, indent=2) + "\n")
        recorder.log("probe: %d frames, %d bytes, retained %s"
                     % (self.frames, self.bytes, retained))
        return doc

    async def main(self):
        self.start = time.time()
        self.end = self.start + PROBE_S
        self.retained_t0 = self.retained_window()
        recorder.log("probe: 60 minutes from %d, retaining interval %d"
                     % (self.start, self.retained_t0))
        while time.time() < self.end:
            try:
                async with websockets.connect(config.CLOB_WS_URL, open_timeout=20,
                                              ping_interval=None, max_size=None) as ws:
                    tokens = await self.tokens_for(
                        int(time.time() // config.INTERVAL_S) * config.INTERVAL_S)
                    await ws.send(json.dumps({"assets_ids": tokens, "type": "market",
                                              "initial_dump": True}))
                    self.subscribed = set(tokens)
                    tasks = [asyncio.create_task(self.ping(ws)),
                             asyncio.create_task(self.roll(ws))]
                    try:
                        await self.pump(ws)
                    finally:
                        for task in tasks:
                            task.cancel()
            except Exception as exc:
                recorder.log("probe: socket drop %r" % (exc,))
                await asyncio.sleep(2)
        # At 60 minutes, unsubscribe and stop. Do not resubscribe.
        self.finish()
        return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(Probe().main()))
