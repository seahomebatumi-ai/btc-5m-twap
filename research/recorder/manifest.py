"""TZ-04a per-interval manifest.

The manifest is a pure function of the files already sitting in an interval directory. That is
what makes V5 a real test: `build()` reads only the directory, so rebuilding it later must
reproduce the same bytes. Nothing is carried in from recorder memory - the recorder writes its
own state (git sha, disconnects, clock samples) into `runtime.jsonl` inside the directory
before the manifest is built.
"""

import gzip
import json
import os
import sys

import config

MANIFEST_NAME = "manifest.json"
RUNTIME_NAME = "runtime.jsonl"


def _read_lines(path):
    """Yield the parsed capture lines of a .jsonl or .jsonl.gz file."""
    if not os.path.exists(path):
        return
    opener = gzip.open if path.endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)


def _stream_path(dirpath, stream):
    gz = os.path.join(dirpath, stream + ".jsonl.gz")
    return gz if os.path.exists(gz) else os.path.join(dirpath, stream + ".jsonl")


def _stream_stats(dirpath, stream):
    """Counts and byte totals for one stream, read back off disk.

    `raw_bytes` is the uncompressed capture file and `stored_bytes` is what the directory
    actually occupies. V7 wants both, so both are measured here rather than estimated.
    """
    path = _stream_path(dirpath, stream)
    recv, raw_bytes = [], 0
    if os.path.exists(path):
        opener = gzip.open if path.endswith(".gz") else open
        with opener(path, "rt", encoding="utf-8") as fh:
            for line in fh:
                raw_bytes += len(line.encode("utf-8"))
                line = line.strip()
                if line:
                    recv.append(json.loads(line)["recv_ns"])
    stored = os.path.getsize(path) if os.path.exists(path) else 0
    if not recv:
        return {"messages": 0, "first_recv_ns": None, "last_recv_ns": None,
                "max_inter_message_gap_ms": None, "raw_bytes": raw_bytes,
                "stored_bytes": stored}
    ordered = sorted(recv)
    gaps = [b - a for a, b in zip(ordered, ordered[1:])]
    return {
        "messages": len(ordered),
        "first_recv_ns": ordered[0],
        "last_recv_ns": ordered[-1],
        "max_inter_message_gap_ms": (max(gaps) / 1e6) if gaps else None,
        "raw_bytes": raw_bytes,
        "stored_bytes": stored,
    }


def _runtime(dirpath):
    path = os.path.join(dirpath, RUNTIME_NAME)
    out = []
    if os.path.exists(path):
        with open(path, "rt", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    out.append(json.loads(line))
    return out


def resolved_outcome(market):
    """The winning outcome once the venue has settled the market, else None.

    Before settlement `outcomePrices` carries live quotes such as ["0.685", "0.315"], which are
    truthy and must not be mistaken for a result. A market counts as settled only when it is
    closed and its prices are exactly one "1" and the rest "0". Both `outcomes` and
    `outcomePrices` arrive as JSON-encoded strings.
    """
    if not isinstance(market, dict) or not market.get("closed"):
        return None
    prices, outcomes = market.get("outcomePrices"), market.get("outcomes")
    try:
        prices = json.loads(prices) if isinstance(prices, str) else prices
        outcomes = json.loads(outcomes) if isinstance(outcomes, str) else outcomes
    except ValueError:
        return None
    if not prices or not outcomes or len(prices) != len(outcomes):
        return None
    winners = [o for o, p in zip(outcomes, prices) if str(p) in ("1", "1.0")]
    losers = [o for o, p in zip(outcomes, prices) if str(p) in ("0", "0.0")]
    if len(winners) != 1 or len(winners) + len(losers) != len(prices):
        return None
    return winners[0]


def _resolution_present(dirpath):
    """True when resolution.json holds a settled market carrying the venue's own outcome."""
    path = os.path.join(dirpath, "resolution.json")
    if not os.path.exists(path):
        return False
    try:
        with open(path, "rt", encoding="utf-8") as fh:
            doc = json.load(fh)
    except ValueError:
        return False
    market = doc[0] if isinstance(doc, list) else doc
    return resolved_outcome(market) is not None


def _gamma_present(dirpath):
    path = os.path.join(dirpath, "gamma.json")
    if not os.path.exists(path):
        return False
    try:
        with open(path, "rt", encoding="utf-8") as fh:
            doc = json.load(fh)
    except ValueError:
        return False
    market = doc[0] if isinstance(doc, list) else doc
    return isinstance(market, dict) and bool(market.get("conditionId"))


def build(dirpath):
    """The manifest for one interval directory, from that directory alone."""
    t0 = int(os.path.basename(os.path.normpath(dirpath)))
    window = [t0 - config.PRE_S, t0 + config.POST_S]

    streams = {s: _stream_stats(dirpath, s) for s in config.STREAM_FILES}

    runtime = _runtime(dirpath)
    disconnects = sorted(
        ({"start_recv_ns": r["start_recv_ns"], "end_recv_ns": r["end_recv_ns"],
          "reason": r.get("reason", "")} for r in runtime if r.get("kind") == "disconnect"),
        key=lambda r: (r["start_recv_ns"], r["end_recv_ns"]),
    )
    clock = sorted(
        ({"recv_ns": r["recv_ns"], "server": r["server"], "offset_ms": r["offset_ms"],
          "rtt_ms": r["rtt_ms"]} for r in runtime if r.get("kind") == "clock"),
        key=lambda r: (r["recv_ns"], r["server"]),
    )
    shas = sorted({r["sha"] for r in runtime if r.get("kind") == "recorder"})

    gamma_ok = _gamma_present(dirpath)
    resolution_ok = _resolution_present(dirpath)

    # TZ-04a section 4: `complete` is zero disconnects on S1 and S3 across the whole window,
    # with S6 and S7 both present. S1-S4 share one socket, so any disconnect touches both.
    complete = (not disconnects) and gamma_ok and resolution_ok

    offsets = [abs(c["offset_ms"]) for c in clock]
    return {
        "T0_epoch": t0,
        "window_epoch": window,
        "streams": streams,
        "disconnects": disconnects,
        "disconnect_count": len(disconnects),
        "disconnected_ms": sum((d["end_recv_ns"] - d["start_recv_ns"]) / 1e6
                               for d in disconnects),
        "recorder_git_sha": shas[0] if len(shas) == 1 else shas,
        "clock_offset_samples": clock,
        "clock_offset_abs_max_ms": max(offsets) if offsets else None,
        "gamma_present": gamma_ok,
        "resolution_present": resolution_ok,
        "complete": complete,
    }


def dumps(doc):
    """The one serialisation used everywhere, so a rebuild is byte-comparable."""
    return json.dumps(doc, sort_keys=True, indent=2) + "\n"


def write(dirpath):
    doc = build(dirpath)
    path = os.path.join(dirpath, MANIFEST_NAME)
    tmp = path + ".tmp"
    with open(tmp, "wt", encoding="utf-8") as fh:
        fh.write(dumps(doc))
    os.replace(tmp, path)
    return doc


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: manifest.py <interval-directory>")
    sys.stdout.write(dumps(build(sys.argv[1])))
