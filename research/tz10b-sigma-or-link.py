#!/usr/bin/env python3
"""TZ-10b: `sigma` or the link - the discriminating measurement.

Phase 1 answered no. TZ-08a's G3 failed at `tau` 60 and 30 on a settlement residual with a
sharp centre and a heavy tail, and two explanations survive: the conditional law is
heavy-tailed and `Phi` is the wrong link, or the law is Gaussian given the volatility in force
and the pricer's estimate of that volatility lags the move. A Student's `t` is itself a scale
mixture of normals, so the unconditional residual cannot separate them. This file measures the
residual conditionally - standardized by the pricer's own `sigma`, by the successor interval's,
and by the realised scale of the very window that generates it - and reports the two readings
TZ-10b section 4 fixed before any of it was seen. It fits no pricer and adopts no link.

This file is a driver. It holds the set assertions, the `sigma_post` qualification rule, the V2
sample, the strata, the regression and the report tables, and no formula of the model and no
threshold of the verdict. `Y(a, tau)`, the anchor enumeration and the horizon come from
`tz07b-settlement-dispersion.py`; M6's disconnect rule from `tz07a-variance-time.py` through it;
set formation from `tz06-calibration.scoring_set`, through TZ-08a's own `the_set`;
`corrected_sd`, `phi`, `log_phi`, `TAUS`, the one-second grid and the realised-sigma estimator
from `pfair.py`; the stream reader from `analyze.py`. `lambda_hat` is TZ-07a's own search, run
with the `log_phi` likelihood section 3.2 requires.

Outcomes are read in exactly the two places TZ-10b section 2 names: inside the committed
`tz06-calibration.qualification`, which set formation calls, and in `m2_labels`, for
`lambda_hat` alone. No other statistic here reads one.

Read-only over the capture: nothing under `/var/lib/btc-recorder/` is written, moved or deleted,
and `quotes.jsonl.gz` is never opened. The only files written are the four outputs, into a
directory asserted to lie outside the capture. The only subprocesses are `git` and
`selftest-pfair.py`, each a fixed argument list with no shell.

Run:  python3 -B tz10b-sigma-or-link.py --out <directory>

writes `tz10b-results.json`, `tz10b-tables.md` and `tz10b-observations.csv`, none of which
carries a wall-clock time or a path, so two runs compare by `cmp`; and `tz10b-host.json`, the
run's own reads of the host at its start and end, which differ from run to run by construction.
"""

import array
import ast
import collections
import hashlib
import importlib.util
import json
import os
import statistics
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import pfair                                                               # noqa: E402
from pfair import D, MS, config                                            # noqa: E402
from analyze import RUNTIME_PATH, load_manifests, venue                    # noqa: E402


def _load(name, filename):
    """Import a module whose filename carries a hyphen, so it cannot be `import`ed by name."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# TZ-08a's driver loads TZ-07b, which loads TZ-07a, which loads TZ-06, so all four come through
# it: loading any of them a second time would be two module objects and two copies of one set.
tz08a = _load("tz08aoutofsample", "tz08a-out-of-sample.py")
tz07b = tz08a.tz07b
tz07a = tz08a.tz07a
tz06 = tz08a.tz06

# Section 3.0: the 800 are TZ-06's 400 and TZ-08a's 400, identified by these member-list hashes.
TZ06_SHA256 = "6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9"
TZ08A_SHA256 = "3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762"

# Section 3.0: TZ-07b's grid, [T0 - 300, T0 + 300] inclusive, and its anchor enumeration.
GRID_LO, GRID_HI, GRID_POINTS = tz07b.GRID_LO, tz07b.GRID_HI, tz07b.GRID_POINTS

# Section 3.0: `sigma_post` is read over the successor interval, [T0 + 300, T0 + 600].
POST_LO, POST_HI = config.INTERVAL_S, 2 * config.INTERVAL_S

# The three arms, in the order every table prints them. `hat` is the pricer's own `sigma`;
# `win` is labelled an upper bound wherever it appears, and no reading of section 4 uses it.
ARMS = ("hat", "post", "win")
ARM_NAMES = {"hat": "`sigma_hat`", "post": "`sigma_post`",
             "win": "`sigma_win` — upper bound"}

# Section 3.1: the robust scales are TZ-07b's, and so is the normal's tail beyond three.
MAD_TO_SIGMA = tz07b.MAD_TO_SIGMA
IQR_TO_SIGMA = tz07b.IQR_TO_SIGMA
TAIL_MULTIPLE = 3
NORMAL_TAIL = tz07b.NORMAL_TAIL[TAIL_MULTIPLE]

# Section 3.1: the `kappa` TZ-08a V9's readings imply - a published expectation, printed beside
# the measurement and never compared against.
KAPPA_PUBLISHED = {240: "1.22", 180: "1.28", 120: "1.43", 90: "1.69", 60: "2.27",
                   30: "3.45", 10: "5.26"}

# Section 3.3: deciles.
STRATA = 10

# Section 3.4: the regressors, named before any data was seen, in the order they are fitted,
# and the three windows they read, in seconds ending at the checkpoint.
REGRESSORS = ("log(sigma_60 / sigma_300)", "log sigma_hat",
              "|move over the last 30 s| / (sigma_hat * sqrt(30))", "tau")
SHORT_S, LONG_S, MOVE_S = 60, 300, 30

# Section 3.5: the observation the committed gate statistic hangs on.
M5_T0, M5_TAUS = 1789268400, (30, 10)

# Section 4.1: the verdict is read at the two taus the gate failed at.
VERDICT_TAUS = (60, 30)

# Section 4.4: the Architect's pre-registered prediction, printed beside what is measured.
PREDICTION = (("f(60)", "0.5", "0.7"), ("f(30)", "0.6", "0.8"),
              ("out-of-sample R2", "0.05", "0.15"))

# Section 7 V2: the first 20 TZ-06 members in T0 order, at all seven taus.
V2_MEMBERS = 20

# Section 7 V4: TZ-07b's `Lambda` on the TZ-06 400 and TZ-08a V8's `Lambda_oos` on the TZ-08a
# 400, each exactly as its committed report printed it.
TZ07B_LAMBDA = {240: "1.523760", 180: "1.496023", 120: "1.496277", 90: "1.479154",
                60: "1.444658", 30: "1.385806", 10: "1.211176"}
TZ08A_LAMBDA_OOS = {240: "1.593658", 180: "1.524721", 120: "1.389965", 90: "1.350836",
                    60: "1.315235", 30: "1.265287", 10: "1.112329"}

# Section 7 V7: TZ-08a's `lambda_hat` at tau = 30 on its 400, as V7 quotes it and as the TZ-08a
# report printed it. "Expected to agree past the sixth decimal" is read as a difference below
# 1e-6 - the report's section 6 gives the reason and prints both values in full.
V7_TAU = 30
TZ08A_LAMBDA_30_QUOTED = "2.0418"
TZ08A_LAMBDA_30_PRINTED = "2.041843"
V7_AGREEMENT = 1e-6

# Section 5.2 and V7: the self-test counts, the 104 already there and the six added.
SELFTEST_COUNTS = {"V5": 56, "TZ-07b section 6": 30, "TZ-10b section 5.2": 6,
                   "section 3 machinery": 18}

# Section 7 V6: the objects the TZ names, and the only names `pfair.py` may gain.
PFAIR_NAMED = ("SD_SCALE", "corrected_sd", "phi", "TAUS", "far_branch", "near_branch",
               "state_and_sd")
PFAIR_ADDED = ("LOG_PHI_CROSSOVER", "log_phi", "log_phi_asymptotic_branch",
               "log_phi_erfc_branch")

# Section 0 and V1: every read of free space during the run is asserted at or above this.
FLOOR_BYTES = 3000000000

# Section 5.1: one row per member per tau, at its checkpoint.
CSV_HEADER = ["T0", "set", "tau", "intersection", "label", "K", "S_t", "m_r", "state",
              "sigma_hat", "sigma_post", "sigma_win", "sd_hat", "sd_post", "sd_win",
              "z_hat", "z_post", "z_win", "log_phi_z_hat", "p_fair_hat", "Y", "r",
              "u_hat", "u_post", "u_win", "sigma_60", "sigma_300", "move_30"]


# ---- V1 and V8: the host, read at the start and at the end -----------------------

def free_bytes():
    """Available bytes on the filesystem holding the capture, as `df -B1` reports `Avail`."""
    st = os.statvfs(config.ROOT)
    return st.f_bavail * st.f_frsize


def recorder_pids():
    """Every process whose argument list runs `recorder.py`, read from `/proc`."""
    out = []
    for name in os.listdir("/proc"):
        if not name.isdigit():
            continue
        try:
            with open(os.path.join("/proc", name, "cmdline"), "rb") as fh:
                argv = fh.read().split(b"\0")
        except OSError:
            continue
        if any(arg.endswith(b"recorder.py") for arg in argv):
            out.append(int(name))
    return sorted(out)


def newest_start():
    """The newest `start` record in `runtime.jsonl`."""
    last = None
    with open(RUNTIME_PATH, encoding="utf-8") as fh:
        for line in fh:
            if '"kind": "start"' in line:
                last = json.loads(line)
    return last


def read_set(t0s):
    """SHA-256 over the name, size and modification time of every file in every interval
    directory this run reads - so a write to any of them between two reads changes it."""
    digest, files = hashlib.sha256(), 0
    for t0 in sorted(t0s):
        directory = config.interval_dir(t0)
        if not os.path.isdir(directory):
            continue
        for name in sorted(os.listdir(directory)):
            st = os.stat(os.path.join(directory, name))
            digest.update(("%d/%s %d %d\n" % (t0, name, st.st_size, st.st_mtime_ns)).encode())
            files += 1
    return digest.hexdigest(), files


def host_read(when, t0s):
    """V1's floor and V8's four facts, at one instant. Asserted, so a breach stops the run."""
    free = free_bytes()
    start = newest_start()
    digest, files = read_set(t0s)
    doc = {"when": when, "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "free_bytes": free, "recorder_pids": recorder_pids(),
           "newest_start_recv_ns": start["recv_ns"], "newest_start_sha": start["sha"],
           "interval_directories": len(os.listdir(os.path.join(config.ROOT, config.SERIES))),
           "read_set_sha256": digest, "read_set_files": files}
    assert free >= FLOOR_BYTES, "V1: %d bytes free at %s, below %d" % (free, when, FLOOR_BYTES)
    assert doc["recorder_pids"], "V8: no recorder process at %s" % when
    return doc


# ---- section 3.0 and V5: the sets --------------------------------------------------

def the_sets(manifests):
    """Both committed sets, re-derived by the committed code and asserted - never re-formed.

    TZ-08a's own `the_set` re-derives its 400 with every assertion TZ-08a made, the TZ-06
    member-list hash among them; the TZ-06 rows are formed once more here because V10
    discloses every unit that walk considered.
    """
    rows08, members08, _doc08 = tz08a.the_set(manifests)
    rows06, full06 = tz06.scoring_set(manifests)
    members06 = [r["T0"] for r in rows06 if r["member"]]
    sha06, sha08 = tz07b.member_list_sha(members06), tz07b.member_list_sha(members08)
    assert full06 and len(members06) == tz06.SET_SIZE, \
        "section 3.0: %d TZ-06 members; the set is never shrunk" % len(members06)
    assert sha06 == TZ06_SHA256 == tz08a.TZ06_SHA256, "V5: the TZ-06 list hashes to %s" % sha06
    assert sha08 == TZ08A_SHA256 == tz08a.SET_SHA256, "V5: the TZ-08a list hashes to %s" % sha08
    assert not set(members06) & set(members08), "section 3.0: the two sets overlap"
    doc = {}
    for name, rows, members, sha in (("TZ-06", rows06, members06, sha06),
                                     ("TZ-08a", rows08, members08, sha08)):
        outside = [r for r in rows if not r["member"]]
        doc[name] = {"units_considered": len(rows), "members": len(members),
                     "non_members": len(outside),
                     "non_member_reasons": dict(sorted(collections.Counter(
                         " + ".join(r["reasons"]) for r in outside).items())),
                     "first_unit": rows[0]["T0"], "last_unit": rows[-1]["T0"],
                     "first_member": members[0], "last_member": members[-1],
                     "member_list_sha256": sha}
    return rows06, members06, rows08, members08, doc


def post_qualification(t0, manifests):
    """Section 3.0's three conditions for the `sigma_post` arm: the reasons a member fails.

    The successor interval directory exists; its manifest is complete; and TZ-07a M6's rule,
    applied to the successor exactly as it is applied to any member, excludes no second of
    `[T0 + 300, T0 + 600]`. `excluded_seconds` reads the successor's own manifest and this
    member's, which are the two directories that span supplies.
    """
    successor = t0 + config.INTERVAL_S
    why = []
    if not os.path.isdir(config.interval_dir(successor)):
        why.append("no successor directory")
    doc = manifests.get(successor)
    if doc is None:
        why.append("no successor manifest")
    elif not doc["complete"]:
        why.append("successor manifest not complete")
    seconds = {successor + GRID_LO + i - t0 for i in tz07a.excluded_seconds(successor, manifests)}
    if any(POST_LO <= s <= POST_HI for s in seconds):
        why.append("disconnect inside [T0+300, T0+600]")
    return why


# ---- section 3.0: the three sigmas -------------------------------------------------

def grid_of(s3, t0):
    """TZ-07b's one-second grid over `[T0 - 300, T0 + 300]`, from `pfair.second_grid`."""
    grid = pfair.second_grid(s3, t0 + GRID_LO, t0 + GRID_HI)
    assert len(grid) == GRID_POINTS and all(v is not None for v in grid), \
        "interval %d: the grid is not whole" % t0
    return grid


def sigma_hat_of(grid, tau):
    """`sigma_hat`: TZ-07b's `sigma`, `pfair.realised_sigma` over `[T0 - 300, T0 + 300 - tau]`.

    It is the pricer's `sigma_live` at the checkpoint, which `measure_member` asserts
    observation by observation, and it is the quantity V2 tests.
    """
    return pfair.realised_sigma(grid[:GRID_POINTS - tau])


def sigma_win_of(grid, a, tau):
    """`sigma_win`: the same estimator over `[a, a + tau]`, the span that generates `Y`."""
    i = a - GRID_LO
    return pfair.realised_sigma(grid[i:i + tau + 1])


def sigma_post_of(t0):
    """`sigma_post`: the same estimator over the successor interval, `[T0 + 300, T0 + 600]`.

    The successor's stream is merged with this member's own directory exactly as
    `pfair.merged_stream` merges any interval with its predecessor.
    """
    s3 = pfair.merged_stream(t0 + config.INTERVAL_S, config.S3_STREAM)
    return pfair.realised_sigma(pfair.second_grid(s3, t0 + POST_LO, t0 + POST_HI))


# ---- M1's raw material: one member, every anchor, every arm -----------------------

def measure_member(t0, manifests, sigma_post, guard):
    """One member: `u` under each arm at every admissible anchor, and its seven checkpoint rows.

    The anchor walk is `tz07b.member_r`'s step for step - the same stream, grid, horizon,
    enumeration and M6 rule, with `Y` from `tz07b.residual` - and `r` is formed exactly as
    `member_r` forms it. Where `guard` is set, this member's `r` is asserted equal, value for
    value, to what `member_r` itself returns.

    `sigma_post` is `None` outside the intersection, and then only `sigma_hat` is measured. An
    anchor whose `sigma_win` is zero has no `u` in that arm - `Y` over a flat span is zero, and
    `0 / 0` is not a value - so it is counted in `undefined` and left out of that arm alone.
    """
    s1 = pfair.reports(t0, config.S1_STREAM)
    s3 = pfair.merged_stream(t0, config.S3_STREAM)
    keys = [ts for ts, _value in s3]
    grid = grid_of(s3, t0)
    pre = tz07a.excluded_prefix(tz07a.excluded_seconds(t0, manifests))
    priced = {row["tau"]: row for row in pfair.observations(t0, s1, s3)}
    reference = tz07b.member_r(t0, manifests) if guard else None
    arms = ARMS if sigma_post is not None else ("hat",)
    per_tau, checkpoints = {}, {}
    for tau in pfair.TAUS:
        sigma_hat = sigma_hat_of(grid, tau)
        assert sigma_hat == priced[tau]["sigma_live"], \
            "interval %d tau %d: sigma_hat is not the pricer's sigma_live" % (t0, tau)
        horizon = tz07b.horizon_sd(tau, sigma_hat)
        assert horizon > 0, "interval %d at tau %d has no scale to divide by" % (t0, tau)
        sd = {"hat": pfair.corrected_sd(tau, sigma_hat)}
        if sigma_post is not None:
            sd["post"] = pfair.corrected_sd(tau, sigma_post)
        values = {arm: array.array("d") for arm in arms}
        squares = {arm: D(0) for arm in arms}
        r_values, r_squares = array.array("d"), D(0)
        dropped, undefined, at_checkpoint = 0, [], None
        for a in range(GRID_LO, GRID_HI - tau + 1):
            i = a - GRID_LO
            if pre[i + tau + 1] - pre[i] > 0:
                dropped += 1
                continue
            y = tz07b.residual(s3, keys, t0, grid, a, tau)
            assert y is not None, "interval %d at tau %d anchor %d has no mean" % (t0, tau, a)
            r = y / horizon
            r_values.append(float(r))
            r_squares += r * r
            u = {"hat": y / sd["hat"]}
            if sigma_post is not None:
                u["post"] = y / sd["post"]
                sigma_win = sigma_win_of(grid, a, tau)
                if sigma_win > 0:
                    u["win"] = y / pfair.corrected_sd(tau, sigma_win)
                else:
                    undefined.append(a)
            for arm, value in u.items():
                values[arm].append(float(value))
                squares[arm] += value * value
            if a == GRID_HI - tau:
                at_checkpoint = {"Y": y, "r": r, "u": u}
        if reference is not None:
            ref = reference[tau]
            assert (ref["values"] == r_values and ref["sum_squares"] == r_squares
                    and ref["dropped"] == dropped
                    and ref["checkpoint"] == (at_checkpoint or {}).get("r")), \
                "interval %d tau %d: r is not tz07b.member_r's" % (t0, tau)
        per_tau[tau] = {"values": values, "squares": squares, "r_squares": r_squares,
                        "n": len(r_values), "dropped": dropped, "undefined": undefined}
        checkpoints[tau] = checkpoint_row(t0, tau, grid, priced[tau], sigma_hat, sigma_post,
                                          sd, at_checkpoint)
    return per_tau, checkpoints


def checkpoint_row(t0, tau, grid, priced, sigma_hat, sigma_post, sd, at_checkpoint):
    """The observation at `T0 + 300 - tau`: what M2, M4, M5 and the observations file read.

    `z` under each arm is `state / corrected_sd(tau, s)`, formed as TZ-08a forms it. `sigma_win`
    here is the checkpoint's own span, `[T0 + 300 - tau, T0 + 300]`, computed from the grid
    whether or not M6 drops that anchor: M2 scores observations, not anchors, as G3 did.
    """
    i = GRID_POINTS - 1 - tau
    sigma = {"hat": sigma_hat}
    sd = dict(sd)
    if sigma_post is not None:
        sigma["post"] = sigma_post
        sigma["win"] = sigma_win_of(grid, GRID_HI - tau, tau)
        if sigma["win"] > 0:
            sd["win"] = pfair.corrected_sd(tau, sigma["win"])
    z = {arm: float(priced["state"] / sd[arm]) for arm in sd}
    return {"T0": t0, "tau": tau, "K": priced["K"], "S_t": priced["S_t"], "m_r": priced["m_r"],
            "state": priced["state"], "sigma": sigma, "sd": sd, "z": z,
            "log_phi_z_hat": pfair.log_phi(z["hat"]),
            "p_fair_hat": pfair.p_fair(priced["state"], sd["hat"]),
            "sigma_short": pfair.realised_sigma(grid[i - SHORT_S:i + 1]),
            "sigma_long": pfair.realised_sigma(grid[i - LONG_S:i + 1]),
            "move": grid[i] - grid[i - MOVE_S],
            "Y": None if at_checkpoint is None else at_checkpoint["Y"],
            "r": None if at_checkpoint is None else at_checkpoint["r"],
            "u": {} if at_checkpoint is None else at_checkpoint["u"]}


# ---- M1: the shape, three ways ------------------------------------------------------

def pool(measured, members, tau, arm):
    """Every `u` of one arm at one tau over a list of members, and its Decimal sum of squares."""
    values, squares = array.array("d"), D(0)
    for t0 in members:
        row = measured[t0][tau]
        values.extend(row["values"][arm])
        squares += row["squares"][arm]
    return values, squares


def shape(values, squares):
    """Section 3.1 on one pool of `u`: `Lambda_u`, the two robust scales, `kappa`, the tail.

    `Lambda_u` is the uncentred root mean square in Decimal, as TZ-07b takes `Lambda`; the MAD
    and the quartiles are taken exactly as `tz07b.dispersion` takes them.
    """
    n = len(values)
    assert n, "an empty pool has no shape"
    lam = (squares / D(n)).sqrt()
    ordered = sorted(values)
    centre = statistics.median(ordered)
    mad = statistics.median(sorted(abs(v - centre) for v in ordered))
    q1, _median, q3 = statistics.quantiles(ordered, n=4, method="inclusive")
    robust = D(repr(mad)) / MAD_TO_SIGMA
    bound = float(TAIL_MULTIPLE * robust)
    return {"n": n, "lambda_u": lam, "mad_over_0_674490": robust,
            "iqr_over_1_348980": D(repr(q3 - q1)) / IQR_TO_SIGMA, "kappa": lam / robust,
            "tail_beyond_3_robust": sum(1 for v in values if abs(v) > bound) / n}


def m1(measured, intersection, members):
    """M1: the three arms over the intersection, and `sigma_hat` over the full 800, per tau."""
    out, inside = {}, set(intersection)
    for tau in pfair.TAUS:
        arms = {arm: shape(*pool(measured, intersection, tau, arm)) for arm in ARMS}
        full = shape(*pool(measured, members, tau, "hat"))
        dropped = {t0: measured[t0][tau]["dropped"] for t0 in members
                   if measured[t0][tau]["dropped"]}
        undefined = {t0: len(measured[t0][tau]["undefined"]) for t0 in intersection
                     if measured[t0][tau]["undefined"]}
        out[tau] = {
            "arms": arms, "full_800_sigma_hat": full,
            "anchors_possible_intersection": len(intersection) * (GRID_POINTS - tau),
            "anchors_dropped_intersection": sum(v for t0, v in dropped.items()
                                                if t0 in inside),
            "anchors_possible_800": len(members) * (GRID_POINTS - tau),
            "anchors_dropped_800": sum(dropped.values()),
            "members_contributing_a_drop": sorted(dropped),
            "sigma_win_undefined_anchors": sum(undefined.values()),
            "sigma_win_undefined_by_member": undefined,
            "kappa_published": KAPPA_PUBLISHED[tau],
        }
    return out


# ---- V4: the instrument reproduces the committed measurement ----------------------

def v4(measured, members06, members08):
    """On `r`, not on `u`: the RMS of `r` under `sigma_hat` is each committed table as printed.

    `RMS(u) * SD_SCALE[tau]` is printed beside it. `u = r / SD_SCALE[tau]` identically, so the
    two agree by construction, and a disagreement at six significant digits aborts the run.
    """
    out = {}
    for name, members, published in (("TZ-06", members06, TZ07B_LAMBDA),
                                     ("TZ-08a", members08, TZ08A_LAMBDA_OOS)):
        rows = {}
        for tau in pfair.TAUS:
            n = sum(measured[t0][tau]["n"] for t0 in members)
            rms_r = (sum((measured[t0][tau]["r_squares"] for t0 in members), D(0))
                     / D(n)).sqrt()
            rms_u = (pool(measured, members, tau, "hat")[1] / D(n)).sqrt()
            scaled = rms_u * pfair.SD_SCALE[tau]
            rows[tau] = {"anchors": n, "rms_r": rms_r, "rms_u": rms_u,
                         "rms_u_times_SD_SCALE": scaled, "published": published[tau],
                         "rms_r_as_printed": "%.6f" % rms_r,
                         "rms_r_6sd": tz07a.six_significant(rms_r),
                         "rms_u_times_SD_SCALE_6sd": tz07a.six_significant(scaled),
                         "relative_difference": abs(scaled / rms_r - 1)}
            assert rows[tau]["rms_r_as_printed"] == published[tau], \
                "V4: %s tau %d: RMS(r) %s, published %s" % (name, tau, rms_r, published[tau])
            assert rows[tau]["rms_r_6sd"] == rows[tau]["rms_u_times_SD_SCALE_6sd"], \
                "V4: %s tau %d: RMS(u)*SD_SCALE %s against RMS(r) %s" % (name, tau, scaled, rms_r)
        out[name] = rows
    return out


# ---- M2 and V11: lambda_hat, three ways, each with its influence ------------------

def m2_labels(members):
    """TZ-10b section 2's first named outcome read: the venue's resolution, for `lambda_hat` alone."""
    out = {}
    for t0 in members:
        info = venue(t0)
        assert info is not None and info["resolved_up"] is not None, \
            "member %d has no resolved outcome" % t0
        out[t0] = 1 if info["resolved_up"] else 0
    return out


def log_likelihood_tail(pairs, lam):
    """TZ-07a section 8's log-likelihood, over `log_phi` as section 3.2 requires.

        sum( y log Phi(z / lam) + (1 - y) log Phi(-z / lam) )

    `1 - Phi(x)` is `Phi(-x)`, so neither term subtracts from one and neither saturates.
    """
    total = 0.0
    for z, y in pairs:
        total += pfair.log_phi(z / lam) if y else pfair.log_phi(-z / lam)
    return total


def lambda_hat(pairs):
    """TZ-07a section 8's scale statistic, by TZ-07a's own search and its own constants.

    `tz07a.lambda_hat` reads its likelihood through the module name `log_likelihood`, which
    is bound to the `log(phi(...))` form for exactly the length of this call and restored
    after it, so the search, the interval, the tolerance and the returned fields are the
    committed ones and only the likelihood differs.
    """
    original = tz07a.log_likelihood
    tz07a.log_likelihood = log_likelihood_tail
    try:
        return tz07a.lambda_hat(pairs)
    finally:
        tz07a.log_likelihood = original


def with_influence(pairs, keys, tau):
    """`lambda_hat`, and V11: its value without its single most influential observation.

    The most influential observation is the one whose removal moves `lambda_hat` furthest,
    found by removing each in turn and searching again; on a tie, the first in `T0` order.
    """
    fit = lambda_hat(pairs)
    best = None
    for i in range(len(pairs)):
        without = lambda_hat(pairs[:i] + pairs[i + 1:])["lambda_hat"]
        shift = abs(without - fit["lambda_hat"])
        if best is None or shift > best[0]:
            best = (shift, i, without)
    shift, i, without = best
    return dict(fit, most_influential={"T0": keys[i], "tau": tau, "label": pairs[i][1],
                                       "z": pairs[i][0], "lambda_hat_without": without,
                                       "shift": without - fit["lambda_hat"]})


def m2(checkpoints, labels, groups):
    """M2 over every population, arm, set and tau. An observation with no `z` in an arm - a
    flat `sigma_win` span at the checkpoint - is left out of that arm and counted."""
    out = {}
    for population, arms, sets in groups:
        out[population] = {}
        for arm in arms:
            out[population][arm] = {}
            for set_name, members in sets:
                out[population][arm][set_name] = {}
                for tau in pfair.TAUS:
                    held = [t0 for t0 in members if arm in checkpoints[t0][tau]["z"]]
                    pairs = [(checkpoints[t0][tau]["z"][arm], labels[t0]) for t0 in held]
                    fit = with_influence(pairs, held, tau)
                    fit["observations_without_z"] = len(members) - len(held)
                    out[population][arm][set_name][tau] = fit
    return out


# ---- section 4: the two readings ----------------------------------------------------

def readings(m1_doc, m2_doc):
    """`f` from M1's `kappa` and `g` from M2's `lambda_hat`, over the intersection, per tau.

    Both are arithmetic on the reported numbers; the instrument carries no threshold and
    judges nothing. `g` is read on the pooled intersection, and also on each 400's share.
    """
    out = {}
    fits = m2_doc["intersection"]
    for tau in pfair.TAUS:
        k_hat = m1_doc[tau]["arms"]["hat"]["kappa"]
        k_post = m1_doc[tau]["arms"]["post"]["kappa"]
        g = {}
        for set_name in fits["hat"]:
            l_hat = fits["hat"][set_name][tau]["lambda_hat"]
            l_post = fits["post"][set_name][tau]["lambda_hat"]
            g[set_name] = {"lambda_hat": l_hat, "lambda_post": l_post,
                           "g": (abs(l_hat - 1) - abs(l_post - 1)) / abs(l_hat - 1)}
        out[tau] = {"kappa_hat": k_hat, "kappa_post": k_post,
                    "f": float((k_hat - k_post) / (k_hat - 1)), "g": g}
    return out


# ---- M3: where the heavy tail lives -------------------------------------------------

def m3(measured, checkpoints, intersection, m1_doc):
    """Deciles of two stratifiers over the intersection's members, `kappa` within each, per tau.

    A decile is a tenth of the members ranked by the stratifier, ties in `T0` order: member
    `k` of `N` falls in stratum `floor(10 k / N)`. Every anchor of a member goes with it.
    """
    stratifiers = (
        ("sigma_hat", "causal",
         lambda cp: cp["sigma"]["hat"]),
        ("log(sigma_post / sigma_hat)", "non-causal, diagnostic only",
         lambda cp: (cp["sigma"]["post"] / cp["sigma"]["hat"]).ln()))
    out = {}
    for name, kind, key in stratifiers:
        out[name] = {"kind": kind, "per_tau": {}}
        for tau in pfair.TAUS:
            order = sorted(intersection, key=lambda t0: (key(checkpoints[t0][tau]), t0))
            strata = [[] for _ in range(STRATA)]
            for rank, t0 in enumerate(order):
                strata[rank * STRATA // len(order)].append(t0)
            rows = []
            for k, members in enumerate(strata):
                s = shape(*pool(measured, members, tau, "hat"))
                rows.append({"stratum": k + 1, "members": len(members), "anchors": s["n"],
                             "from": key(checkpoints[members[0]][tau]),
                             "to": key(checkpoints[members[-1]][tau]),
                             "kappa": s["kappa"], "tail_beyond_3_robust":
                             s["tail_beyond_3_robust"]})
            weight = sum(r["anchors"] for r in rows)
            out[name]["per_tau"][tau] = {
                "strata": rows,
                "kappa_size_weighted_mean": sum(r["kappa"] * r["anchors"] for r in rows)
                / D(weight),
                "kappa_median_of_strata": statistics.median(sorted(r["kappa"] for r in rows)),
                "kappa_pooled": m1_doc[tau]["arms"]["hat"]["kappa"]}
    return out


# ---- M4: is the scale error knowable in advance? -----------------------------------

def m4_row(cp):
    """Section 3.4's response and four causal regressors for one observation, in Decimal."""
    s_hat = cp["sigma"]["hat"]
    assert cp["sigma_short"] > 0 and cp["sigma_long"] > 0, \
        "T0 %d tau %d: a flat window has no log" % (cp["T0"], cp["tau"])
    x = ((cp["sigma_short"] / cp["sigma_long"]).ln(), s_hat.ln(),
         abs(cp["move"]) / (s_hat * D(MOVE_S).sqrt()), D(cp["tau"]))
    return x, (cp["sigma"]["post"] / s_hat).ln()


def ols(rows):
    """Ordinary least squares with an intercept: the normal equations in 60-digit Decimal,
    solved by Gauss-Jordan elimination with partial pivoting."""
    k = len(rows[0][0]) + 1
    xtx = [[D(0)] * k for _ in range(k)]
    xty = [D(0)] * k
    for x, y in rows:
        v = (D(1),) + tuple(x)
        for p in range(k):
            xty[p] += v[p] * y
            for q in range(k):
                xtx[p][q] += v[p] * v[q]
    m = [xtx[p] + [xty[p]] for p in range(k)]
    for col in range(k):
        pivot = max(range(col, k), key=lambda r: abs(m[r][col]))
        m[col], m[pivot] = m[pivot], m[col]
        assert m[col][col] != 0, "M4: the design matrix is singular"
        for r in range(k):
            if r != col:
                factor = m[r][col] / m[col][col]
                for c in range(col, k + 1):
                    m[r][c] -= factor * m[col][c]
    return [m[p][k] / m[p][p] for p in range(k)]


def predict(beta, x):
    return beta[0] + sum(b * v for b, v in zip(beta[1:], x))


def m4(checkpoints, fit_members, test_members):
    """Fitted on the TZ-06 share of the intersection, evaluated on the TZ-08a share. No model is
    adopted; out-of-sample `R2` is taken against the in-sample mean and may be negative."""
    fit = [m4_row(checkpoints[t0][tau]) for t0 in fit_members for tau in pfair.TAUS]
    test = [m4_row(checkpoints[t0][tau]) for t0 in test_members for tau in pfair.TAUS]
    beta = ols(fit)
    mean_in = sum((y for _x, y in fit), D(0)) / D(len(fit))
    sse_in = sum(((y - predict(beta, x)) ** 2 for x, y in fit), D(0))
    sst_in = sum(((y - mean_in) ** 2 for _x, y in fit), D(0))
    sse_out = sum(((y - predict(beta, x)) ** 2 for x, y in test), D(0))
    sst_out = sum(((y - mean_in) ** 2 for _x, y in test), D(0))
    return {"regressors": list(REGRESSORS), "intercept": beta[0],
            "coefficients": dict(zip(REGRESSORS, beta[1:])),
            "n_fit": len(fit), "n_test": len(test), "mean_response_in_sample": mean_in,
            "mean_response_out_of_sample": sum((y for _x, y in test), D(0)) / D(len(test)),
            "r2_in_sample": 1 - sse_in / sst_in, "r2_out_of_sample": 1 - sse_out / sst_out}


# ---- M5: the observation the gate hangs on -----------------------------------------

def m5(checkpoints, labels):
    out = {}
    for tau in M5_TAUS:
        cp = checkpoints[M5_T0][tau]
        out[tau] = {"T0": M5_T0, "tau": tau, "sigma": cp["sigma"], "Y": cp["Y"], "u": cp["u"],
                    "state": cp["state"], "z_hat": cp["z"]["hat"], "p_fair_hat": cp["p_fair_hat"],
                    "log_phi_z_hat": cp["log_phi_z_hat"], "resolved_up": labels[M5_T0]}
    return out


# ---- V2: causality of the causal arm ----------------------------------------------

def v2(members06):
    """The denominator, and only it: `sigma_hat` and `corrected_sd(tau, sigma_hat)` bit-identical
    when every `chainlink` report stamped strictly after the checkpoint instant is perturbed by
    the committed `tz06.perturb_after`; moved by `tz06.perturb_one` on `tz06.last_readable`.

    The control's subject is asserted outside the perturbation set, from what `perturb_after`
    actually changed, and every observation is asserted to perturb at least one report.
    """
    sample = members06[:V2_MEMBERS]
    n = same_sigma = same_sd = moved_sigma = moved_sd = at_instant = 0
    fewest = None
    for t0 in sample:
        s3 = pfair.merged_stream(t0, config.S3_STREAM)
        base_grid = grid_of(s3, t0)
        for tau in pfair.TAUS:
            n += 1
            at = (t0 + config.INTERVAL_S - tau) * MS
            future = tz06.perturb_after(s3, at)
            subject = tz06.last_readable(s3, at)
            perturbed = {i for i in range(len(s3)) if future[i] != s3[i]}
            assert subject is not None and subject not in perturbed and perturbed, \
                "V2: T0 %d tau %d: the perturbation and the control overlap or are empty" % (
                    t0, tau)
            fewest = len(perturbed) if fewest is None else min(fewest, len(perturbed))
            at_instant += s3[subject][0] == at
            base = sigma_hat_of(base_grid, tau)
            after = sigma_hat_of(grid_of(future, t0), tau)
            control = sigma_hat_of(grid_of(tz06.perturb_one(s3, subject), t0), tau)
            same_sigma += after == base
            same_sd += pfair.corrected_sd(tau, after) == pfair.corrected_sd(tau, base)
            moved_sigma += control != base
            moved_sd += pfair.corrected_sd(tau, control) != pfair.corrected_sd(tau, base)
    doc = {"sample": sample, "members": len(sample), "taus": list(pfair.TAUS),
           "checkpoints": n, "factor": str(tz06.PERTURBATION),
           "perturbation": "tz06-calibration.perturb_after on the merged chainlink stream: "
                           "every report with ts > T0 + (300 - tau), in ms",
           "negative_control": "tz06-calibration.perturb_one on the report "
                               "tz06-calibration.last_readable returns, ts <= that instant",
           "sigma_hat_bit_identical": same_sigma, "corrected_sd_bit_identical": same_sd,
           "control_moved_sigma_hat": moved_sigma, "control_moved_corrected_sd": moved_sd,
           "control_subject_stamped_at_the_checkpoint_instant": at_instant,
           "fewest_reports_perturbed_in_one_checkpoint": fewest}
    assert (same_sigma, same_sd) == (n, n), \
        "V2: sigma_hat bit-identical %d of %d, corrected_sd %d of %d" % (same_sigma, n, same_sd, n)
    assert (moved_sigma, moved_sd) == (n, n), \
        "V2: the control moved sigma_hat %d of %d, corrected_sd %d of %d" % (
            moved_sigma, n, moved_sd, n)
    return doc


# ---- V6: pfair.py additive only -----------------------------------------------------

def git(*args):
    out = subprocess.run(["git"] + list(args), cwd=HERE, capture_output=True, text=True)
    assert out.returncode == 0, "git %s exited %d: %s" % (" ".join(args), out.returncode,
                                                         out.stderr.strip())
    return out.stdout


def top_level(source):
    """Every top-level function and assignment of a module, by name, as its exact source text."""
    out = {}
    for node in ast.parse(source).body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            names = [node.name]
        elif isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
        else:
            continue
        for name in names:
            out[name] = ast.get_source_segment(source, node)
    return out


def v6():
    """The diff against the merge base is insertions only, for both files TZ-10b may change,
    and every top-level object either file held before is byte-identical after."""
    base = git("merge-base", "HEAD", "main").strip()
    head = git("rev-parse", "HEAD").strip()
    assert not git("status", "--porcelain", "--", "pfair.py", "selftest-pfair.py",
                   "tz10b-sigma-or-link.py").strip(), "V6: the run is not of committed files"
    files = {}
    for name in ("pfair.py", "selftest-pfair.py"):
        body = [line for line in git("diff", "--unified=0", base, "HEAD", "--", name).splitlines()
                if not line.startswith(("---", "+++"))]
        removed = [line for line in body if line.startswith("-")]
        added = [line for line in body if line.startswith("+")]
        assert added and not removed, "V6: %s removes %d lines" % (name, len(removed))
        before = top_level(git("show", "%s:research/%s" % (base, name)))
        with open(os.path.join(HERE, name), encoding="utf-8") as fh:
            after = top_level(fh.read())
        changed = sorted(n for n in before if after.get(n) != before[n])
        assert not changed, "V6: %s changes %s" % (name, changed)
        files[name] = {"lines_added": len(added), "lines_removed": len(removed),
                       "objects_before": len(before), "objects_byte_identical": len(before),
                       "objects_added": sorted(set(after) - set(before))}
    assert all(n in top_level(git("show", "%s:research/pfair.py" % base)) for n in PFAIR_NAMED)
    assert files["pfair.py"]["objects_added"] == sorted(PFAIR_ADDED), \
        "V6: pfair.py gains %s" % files["pfair.py"]["objects_added"]
    return {"merge_base": base, "head": head, "files": files, "named": list(PFAIR_NAMED),
            "pfair_diff": git("diff", base, "HEAD", "--", "pfair.py")}


# ---- V7: log_phi ------------------------------------------------------------------------

def v7_selftests():
    """`selftest-pfair.py`, run and counted - never transcribed. Each item aborts that run."""
    out = subprocess.run([sys.executable, "-B", "selftest-pfair.py"], cwd=HERE,
                         capture_output=True, text=True)
    assert out.returncode == 0, "V7: selftest-pfair.py exited %d: %s" % (
        out.returncode, out.stderr.strip().splitlines()[-1:])
    counts, lines, inside = {}, [], False
    for line in out.stdout.splitlines():
        if line.endswith("checks passed") and ":" in line:
            label, rest = line.split(":", 1)
            counts[label.strip()] = int(rest.split()[0])
        if line.startswith("tz10b_"):
            inside = True
        elif line.startswith("machinery_"):
            inside = False
        if inside:
            lines.append(line)
    assert counts == SELFTEST_COUNTS, "V7: the self-tests count %s" % counts
    return {"command": "python3 -B selftest-pfair.py", "exit_status": out.returncode,
            "counts": counts, "total": sum(counts.values()), "tz10b_output": lines}


def v7_lambda(checkpoints, labels, members08, fit):
    """`lambda_hat` at tau = 30 on TZ-08a's 400 under `sigma_hat`: as TZ-08a computed it, with
    `log(phi(...))`, and as M2 computes it, with `log_phi`."""
    pairs = [(checkpoints[t0][V7_TAU]["z"]["hat"], labels[t0]) for t0 in members08]
    assert tz07a.log_likelihood.__name__ == "log_likelihood", "V7: the likelihood is not restored"
    code = tz07a.lambda_hat(pairs)
    doc = {"tau": V7_TAU, "n": len(pairs),
           "tz07a_lambda_hat_log_of_phi": code["lambda_hat"],
           "tz07a_ll_at_one_log_of_phi": code["ll_at_one"],
           "lambda_hat_log_phi": fit["lambda_hat"], "ll_at_one_log_phi": fit["ll_at_one"],
           "difference": fit["lambda_hat"] - code["lambda_hat"],
           "quoted_by_TZ_10b": TZ08A_LAMBDA_30_QUOTED,
           "printed_by_TZ_08a": TZ08A_LAMBDA_30_PRINTED, "agreement": V7_AGREEMENT}
    assert "%.4f" % code["lambda_hat"] == TZ08A_LAMBDA_30_QUOTED \
        and "%.6f" % code["lambda_hat"] == TZ08A_LAMBDA_30_PRINTED, \
        "V7: TZ-08a's lambda_hat does not reproduce: %r" % code["lambda_hat"]
    assert abs(doc["difference"]) < V7_AGREEMENT, \
        "V7: log_phi moves lambda_hat by %r" % doc["difference"]
    return doc


# ---- the document ------------------------------------------------------------------

def build():
    manifests = load_manifests()
    rows06, members06, rows08, members08, set_doc = the_sets(manifests)
    members = members06 + members08
    reads = {t0 + d for t0 in members for d in (-config.INTERVAL_S, 0, config.INTERVAL_S)}
    host = [host_read("run start", reads)]

    # Everything that stops the run on a defect of the instrument comes before any measurement.
    causality = v2(members06)
    additive = v6()
    selftests = v7_selftests()

    set06 = set(members06)
    post_rows, sigma_post = [], {}
    for t0 in members:
        why = post_qualification(t0, manifests)
        post_rows.append({"T0": t0, "set": "TZ-06" if t0 in set06 else "TZ-08a",
                          "qualifies": not why, "reasons": why})
        if not why:
            sigma_post[t0] = sigma_post_of(t0)
    intersection = [t0 for t0 in members if t0 in sigma_post]
    inter06 = [t0 for t0 in intersection if t0 in set06]
    inter08 = [t0 for t0 in intersection if t0 not in set06]
    assert M5_T0 in sigma_post, "M5: T0 %d is outside the intersection" % M5_T0

    # System Map section 7 item 24: the guard samples across the set and holds, by
    # construction, every member whose grid M6 drops a second of.
    excluding = tz08a.m6_members(members06, manifests)[1] \
        + tz08a.m6_members(members08, manifests)[1]
    guard = sorted(set(members06[:V2_MEMBERS]) | set(excluding))

    measured, checkpoints = {}, {}
    for t0 in members:
        measured[t0], checkpoints[t0] = measure_member(t0, manifests, sigma_post.get(t0),
                                                       t0 in guard)
    labels = m2_labels(members)

    m1_doc = m1(measured, intersection, members)
    reproduction = v4(measured, members06, members08)
    m2_doc = m2(checkpoints, labels, (
        ("intersection", ARMS, (("TZ-06", inter06), ("TZ-08a", inter08),
                                ("pooled", intersection))),
        ("full", ("hat",), (("TZ-06", members06), ("TZ-08a", members08),
                            ("pooled", members)))))
    lam30 = v7_lambda(checkpoints, labels, members08, m2_doc["full"]["hat"]["TZ-08a"][V7_TAU])
    m3_doc = m3(measured, checkpoints, intersection, m1_doc)
    m4_doc = m4(checkpoints, inter06, inter08)
    m5_doc = m5(checkpoints, labels)
    reading = readings(m1_doc, m2_doc)
    csv = csv_text(members, set(members06), sigma_post, checkpoints, labels)

    host.append(host_read("run end", reads))
    start, end = host
    assert end["recorder_pids"] == start["recorder_pids"], "V8: the recorder pid changed"
    assert end["newest_start_sha"] == start["newest_start_sha"] \
        and end["newest_start_recv_ns"] == start["newest_start_recv_ns"], \
        "V8: the recorder restarted during the run"
    assert end["interval_directories"] >= start["interval_directories"], \
        "V8: the interval count fell"
    assert end["read_set_sha256"] == start["read_set_sha256"], \
        "V8: a file this run reads changed during the run"

    doc = {
        "tz": "TZ-10b",
        "sets": set_doc,
        "disclosure_TZ_06": rows06,
        "disclosure_TZ_08a": rows08,
        "sigma_post_arm": {"rule": "successor directory exists, its manifest is complete, and "
                                   "M6 excludes no second of [T0+300, T0+600]",
                           "members": len(members), "qualifying": len(intersection),
                           "non_qualifying": len(members) - len(intersection),
                           "reasons": dict(sorted(collections.Counter(
                               " + ".join(r["reasons"]) for r in post_rows
                               if r["reasons"]).items())),
                           "rows": post_rows},
        "intersection": {"members": len(intersection), "TZ-06": len(inter06),
                         "TZ-08a": len(inter08),
                         "member_list_sha256": tz07b.member_list_sha(intersection)},
        "guard": {"members": len(guard), "of_which_M6_drops_a_second": len(set(excluding)),
                  "rule": "the first %d TZ-06 members and every member whose grid M6 drops "
                          "a second of" % V2_MEMBERS},
        "M1": m1_doc, "M2": m2_doc, "M3": m3_doc, "M4": m4_doc, "M5": m5_doc,
        "readings": reading,
        "V2": causality, "V4": reproduction, "V6": additive,
        "V7": {"self_tests": selftests, "lambda_hat_tau_30": lam30},
        "observations_file": {"lines": len(csv.splitlines()),
                              "bytes": len(csv.encode("utf-8")),
                              "sha256": hashlib.sha256(csv.encode("utf-8")).hexdigest()},
    }
    return doc, csv, {"reads": host, "read_set_directories": len(reads)}


def cell(value):
    if value is None:
        return ""
    if isinstance(value, float):
        return repr(value)
    return str(value)


def csv_text(members, tz06_members, sigma_post, checkpoints, labels):
    """Section 5.1's observations file: one row per member per tau, in T0 then tau order."""
    lines = [",".join(CSV_HEADER)]
    for t0 in members:
        for tau in pfair.TAUS:
            cp = checkpoints[t0][tau]
            s, sd, z, u = cp["sigma"], cp["sd"], cp["z"], cp["u"]
            lines.append(",".join(cell(v) for v in (
                t0, "TZ-06" if t0 in tz06_members else "TZ-08a", tau,
                1 if t0 in sigma_post else 0, labels[t0], cp["K"], cp["S_t"], cp["m_r"],
                cp["state"], s["hat"], s.get("post"), s.get("win"), sd["hat"], sd.get("post"),
                sd.get("win"), z["hat"], z.get("post"), z.get("win"), cp["log_phi_z_hat"],
                cp["p_fair_hat"], cp["Y"], cp["r"], u.get("hat"), u.get("post"), u.get("win"),
                cp["sigma_short"], cp["sigma_long"], cp["move"])))
    return "\n".join(lines) + "\n"


# ---- output --------------------------------------------------------------------------

def f6(value):
    return "%.6f" % value


def m1_tables(doc):
    out = []
    for arm in ARMS:
        out += ["", "#### M1, %s, over the intersection" % ARM_NAMES[arm], "",
                "| tau | anchors | `Lambda_u` | `MAD/0.674490` | `IQR/1.348980` | **`kappa`** | "
                "`kappa` published (TZ-08a V9) | `P(\\|u\\| > 3 MAD/0.674490)` | normal |",
                "|---|---|---|---|---|---|---|---|---|"]
        for tau in pfair.TAUS:
            s = doc["M1"][tau]["arms"][arm]
            out.append("| %d | %d | %s | %s | %s | **%.4f** | %s | %.4f | %s |" % (
                tau, s["n"], f6(s["lambda_u"]), f6(s["mad_over_0_674490"]),
                f6(s["iqr_over_1_348980"]), s["kappa"], doc["M1"][tau]["kappa_published"],
                s["tail_beyond_3_robust"], NORMAL_TAIL))
    out += ["", "#### M1, `sigma_hat` over the full 800", "",
            "| tau | anchors | `Lambda_u` | `MAD/0.674490` | `IQR/1.348980` | **`kappa`** | "
            "`P(\\|u\\| > 3 MAD/0.674490)` |", "|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        s = doc["M1"][tau]["full_800_sigma_hat"]
        out.append("| %d | %d | %s | %s | %s | **%.4f** | %.4f |" % (
            tau, s["n"], f6(s["lambda_u"]), f6(s["mad_over_0_674490"]),
            f6(s["iqr_over_1_348980"]), s["kappa"], s["tail_beyond_3_robust"]))
    out += ["", "#### M1, anchors", "",
            "| tau | possible, intersection | dropped by M6, intersection | possible, 800 | "
            "dropped by M6, 800 | `sigma_win` undefined | members contributing a drop |",
            "|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        row = doc["M1"][tau]
        out.append("| %d | %d | %d | %d | %d | %d | %d |" % (
            tau, row["anchors_possible_intersection"], row["anchors_dropped_intersection"],
            row["anchors_possible_800"], row["anchors_dropped_800"],
            row["sigma_win_undefined_anchors"], len(row["members_contributing_a_drop"])))
    drops = sorted({t0 for tau in pfair.TAUS for t0 in doc["M1"][tau]["members_contributing_a_drop"]})
    undefined = {}
    for tau in pfair.TAUS:
        for t0, count in doc["M1"][tau]["sigma_win_undefined_by_member"].items():
            undefined["%d at tau %d" % (t0, tau)] = count
    out += ["", "Members contributing a dropped anchor (%d): %s" % (
        len(drops), ", ".join(str(t) for t in drops) or "none"),
        "", "`sigma_win` undefined — a flat span, `Y = 0` over `sigma = 0`: %s" % (
            ", ".join("%s: %d anchors" % kv for kv in undefined.items()) or "none")]
    return out


def lambda_table(fits, title):
    out = ["", "#### %s" % title, "",
           "| tau | n | `lambda_hat` | `ll_at_lambda_hat` | `ll_at_one` | LR | p | most influential "
           "(T0, label, z) | `lambda_hat` without it | shift |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        f = fits[tau]
        mi = f["most_influential"]
        out.append("| %d | %d | %.6f | %.6f | %.6f | %.6f | %.6g | %d, %d, %.4f | %.6f | %+.6f |" % (
            tau, f["n"], f["lambda_hat"], f["ll_at_lambda_hat"], f["ll_at_one"],
            f["likelihood_ratio"], f["chi_square_1df_p"], mi["T0"], mi["label"], mi["z"],
            mi["lambda_hat_without"], mi["shift"]))
    return out


def tables(doc):
    s = doc["sets"]
    out = ["## Sets", ""]
    for name in ("TZ-06", "TZ-08a"):
        d = s[name]
        out.append("- %s: %d units considered (%d … %d), %d members (%d … %d), %d non-members "
                   "(%s); member list `%s`" % (
                       name, d["units_considered"], d["first_unit"], d["last_unit"],
                       d["members"], d["first_member"], d["last_member"], d["non_members"],
                       ", ".join("%s: %d" % kv for kv in d["non_member_reasons"].items()),
                       d["member_list_sha256"]))
    p, i = doc["sigma_post_arm"], doc["intersection"]
    out += ["- `sigma_post` arm: %d of %d qualify, %d do not (%s)" % (
        p["qualifying"], p["members"], p["non_qualifying"],
        ", ".join("%s: %d" % kv for kv in p["reasons"].items())),
        "- intersection: %d members, %d TZ-06 and %d TZ-08a; member list `%s`" % (
            i["members"], i["TZ-06"], i["TZ-08a"], i["member_list_sha256"])]

    out += ["", "## M1", ""] + m1_tables(doc)

    out += ["", "## M2"]
    for arm in ARMS:
        for set_name in ("TZ-06", "TZ-08a", "pooled"):
            fits = doc["M2"]["intersection"][arm][set_name]
            title = "M2, %s, intersection, %s" % (ARM_NAMES[arm], set_name)
            missing = sum(fits[tau]["observations_without_z"] for tau in pfair.TAUS)
            if missing:
                title += " — %d observations with no `z`" % missing
            out += lambda_table(fits, title)
    for set_name in ("TZ-06", "TZ-08a", "pooled"):
        out += lambda_table(doc["M2"]["full"]["hat"][set_name],
                            "M2, `sigma_hat`, full sets, %s" % set_name)

    out += ["", "## Readings", "", "| tau | `kappa_hat` | `kappa_post` | **`f`** | "
            "`lambda_hat`, pooled | `lambda_post`, pooled | **`g`, pooled** | `g`, TZ-06 | "
            "`g`, TZ-08a |", "|---|---|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        r = doc["readings"][tau]
        out.append("| %s | %.4f | %.4f | **%.4f** | %.6f | %.6f | **%.4f** | %.4f | %.4f |" % (
            ("**%d**" % tau) if tau in VERDICT_TAUS else str(tau), r["kappa_hat"],
            r["kappa_post"], r["f"], r["g"]["pooled"]["lambda_hat"],
            r["g"]["pooled"]["lambda_post"], r["g"]["pooled"]["g"], r["g"]["TZ-06"]["g"],
            r["g"]["TZ-08a"]["g"]))

    out += ["", "## M3"]
    for name, block in doc["M3"].items():
        out += ["", "#### M3, deciles of %s — %s" % (name, block["kind"]), "",
                "| tau | pooled `kappa` | size-weighted mean of stratum `kappa` | median of "
                "stratum `kappa` | stratum `kappa`, 1 … 10 | stratum tail, 1 … 10 |",
                "|---|---|---|---|---|---|"]
        for tau in pfair.TAUS:
            t = block["per_tau"][tau]
            out.append("| %d | %.4f | %.4f | %.4f | %s | %s |" % (
                tau, t["kappa_pooled"], t["kappa_size_weighted_mean"],
                t["kappa_median_of_strata"],
                " / ".join("%.3f" % r["kappa"] for r in t["strata"]),
                " / ".join("%.4f" % r["tail_beyond_3_robust"] for r in t["strata"])))
        out += ["", "Strata bounds and sizes, per tau (members, anchors, from … to):", ""]
        for tau in pfair.TAUS:
            out.append("- tau %d: %s" % (tau, "; ".join(
                "%d: %d, %d, %.6g … %.6g" % (r["stratum"], r["members"], r["anchors"],
                                             r["from"], r["to"])
                for r in block["per_tau"][tau]["strata"])))

    m = doc["M4"]
    out += ["", "## M4", "",
            "Fitted on %d observations (TZ-06 share of the intersection), evaluated on %d "
            "(TZ-08a share). Response `log(sigma_post / sigma_hat)`; mean %.6f in sample, "
            "%.6f out of sample." % (m["n_fit"], m["n_test"], m["mean_response_in_sample"],
                                      m["mean_response_out_of_sample"]), "",
            "| term | coefficient |", "|---|---|", "| intercept | %.6g |" % m["intercept"]]
    for name in REGRESSORS:
        out.append("| %s | %.6g |" % (name.replace("|", "\\|"), m["coefficients"][name]))
    out += ["", "In-sample `R2` **%.4f** · out-of-sample `R2` **%.4f**" % (
        m["r2_in_sample"], m["r2_out_of_sample"])]

    out += ["", "## M5", "",
            "| tau | `sigma_hat` | `sigma_post` | `sigma_win` | `Y` | `u` hat | `u` post | "
            "`u` win | `state` | `z` | `p_fair` | `log_phi(z)` | resolved |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for tau in M5_TAUS:
        r = doc["M5"][tau]
        u = r["u"]
        out.append("| %d | %.6f | %.6f | %.6f | %s | %s | %s | %s | %.6f | %.6f | %r | %.6f | %s |" % (
            tau, r["sigma"]["hat"], r["sigma"]["post"], r["sigma"]["win"],
            "—" if r["Y"] is None else "%.6f" % r["Y"],
            *("—" if u.get(a) is None else "%.6f" % u[a] for a in ARMS),
            r["state"], r["z_hat"], r["p_fair_hat"], r["log_phi_z_hat"],
            "Up" if r["resolved_up"] else "Down"))

    out += ["", "## V2", "", "| count | value |", "|---|---|"]
    for key in ("members", "checkpoints", "sigma_hat_bit_identical",
                "corrected_sd_bit_identical", "control_moved_sigma_hat",
                "control_moved_corrected_sd", "control_subject_stamped_at_the_checkpoint_instant",
                "fewest_reports_perturbed_in_one_checkpoint"):
        out.append("| `%s` | %s |" % (key, doc["V2"][key]))
    out += ["", "Sample: %s" % ", ".join(str(t) for t in doc["V2"]["sample"])]

    out += ["", "## V4", "", "| set | tau | anchors | `RMS(r)` | published | `RMS(u)` | "
            "`RMS(u) · SD_SCALE` | relative difference |", "|---|---|---|---|---|---|---|---|"]
    for name, rows in doc["V4"].items():
        for tau in pfair.TAUS:
            r = rows[tau]
            out.append("| %s | %d | %d | %.9f | %s | %.9f | %.9f | %.2e |" % (
                name, tau, r["anchors"], r["rms_r"], r["published"], r["rms_u"],
                r["rms_u_times_SD_SCALE"], r["relative_difference"]))

    v6 = doc["V6"]
    out += ["", "## V6", "", "merge base `%s` · head `%s`" % (v6["merge_base"], v6["head"]), "",
            "| file | lines added | lines removed | top-level objects before | byte-identical "
            "after | objects added |", "|---|---|---|---|---|---|"]
    for name, f in v6["files"].items():
        out.append("| `%s` | %d | %d | %d | %d | %s |" % (
            name, f["lines_added"], f["lines_removed"], f["objects_before"],
            f["objects_byte_identical"], ", ".join("`%s`" % n for n in f["objects_added"])))
    out += ["", "```diff", v6["pfair_diff"].rstrip("\n"), "```"]

    v7 = doc["V7"]
    out += ["", "## V7", "", "Self-test counts: %s · total %d · exit %d" % (
        ", ".join("%s %d" % kv for kv in v7["self_tests"]["counts"].items()),
        v7["self_tests"]["total"], v7["self_tests"]["exit_status"]), "", "```"]
    out += v7["self_tests"]["tz10b_output"] + ["```", ""]
    lam = v7["lambda_hat_tau_30"]
    out += ["| quantity | value |", "|---|---|",
            "| `lambda_hat`, `log(phi)` — TZ-08a's computation | %.10f |" % lam[
                "tz07a_lambda_hat_log_of_phi"],
            "| `lambda_hat`, `log_phi` | %.10f |" % lam["lambda_hat_log_phi"],
            "| difference | %.3e |" % lam["difference"],
            "| `ll_at_one`, `log(phi)` · `log_phi` | %r · %.6f |" % (
                lam["tz07a_ll_at_one_log_of_phi"], lam["ll_at_one_log_phi"]),
            "| quoted by TZ-10b · printed by TZ-08a | %s · %s |" % (
                lam["quoted_by_TZ_10b"], lam["printed_by_TZ_08a"])]

    out += ["", "## V10 — the TZ-06 walk", ""] + disclosure(doc["disclosure_TZ_06"])
    out += ["", "## V10 — the TZ-08a walk", ""] + disclosure(doc["disclosure_TZ_08a"])
    out += ["", "## V10 — the `sigma_post` arm", "",
            "| # | T0 | set | qualifies | reason |", "|---|---|---|---|---|"]
    for n, r in enumerate(doc["sigma_post_arm"]["rows"], 1):
        out.append("| %d | %d | %s | %s | %s |" % (n, r["T0"], r["set"],
                                                   "yes" if r["qualifies"] else "no",
                                                   " + ".join(r["reasons"]) or "—"))
    f = doc["observations_file"]
    out += ["", "## Observations file", "",
            "%d lines · %d bytes · SHA-256 `%s`" % (f["lines"], f["bytes"], f["sha256"])]
    return "\n".join(out) + "\n"


def disclosure(rows):
    out = ["| # | T0 | open (UTC) | member | reason not a member |", "|---|---|---|---|---|"]
    for n, r in enumerate(rows, 1):
        out.append("| %d | %d | %s | %s | %s |" % (
            n, r["T0"], time.strftime("%Y-%m-%d %H:%M", time.gmtime(r["T0"])),
            r["member"] or "—", " + ".join(r["reasons"]) or "—"))
    return out


def main(argv):
    if argv[1:2] != ["--out"] or len(argv) != 3:
        sys.stderr.write("usage: python3 -B tz10b-sigma-or-link.py --out <directory>\n")
        return 2
    target = os.path.realpath(argv[2])
    capture = os.path.realpath(config.ROOT)
    assert os.path.isdir(target), "no directory %s" % target
    assert not (target + os.sep).startswith(capture + os.sep), \
        "V8: %s is inside the capture" % target
    doc, csv, host = build()
    outputs = {"tz10b-results.json": json.dumps(doc, sort_keys=True, indent=2, default=str) + "\n",
               "tz10b-tables.md": tables(doc),
               "tz10b-observations.csv": csv,
               "tz10b-host.json": json.dumps(host, sort_keys=True, indent=2) + "\n"}
    for name, text in outputs.items():
        with open(os.path.join(target, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
