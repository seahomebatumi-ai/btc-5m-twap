#!/usr/bin/env python3
"""TZ-07a: the oracle feed's variance-time curve, the corrected sigma, and the maker terms.

M1 measures how the feed's variance actually grows with the lag it is read at, over the same
400 members TZ-06 scored. M2's answer is frozen into `pfair.py` as literals and this file
asserts that what is in the file is what was measured. M3 recomputes TZ-06's tables with the
corrected `sd` - in sample, on the set that produced the finding, and therefore confirming
nothing. M4 reads the venue's maker terms out of the `gamma.json` documents already on disk.

Nothing here is a formula of its own. `pfair.py` holds the model, `analyze.py` holds the only
stream reader, and `tz06-calibration.py` holds set formation and the calibration arithmetic;
all three are imported and none is modified. Read-only over the capture: nothing under
`/var/lib/btc-recorder/` is written, moved or deleted.

Run:  python3 -B tz07a-variance-time.py              > results.json
      python3 -B tz07a-variance-time.py --tables     > tables.md
      python3 -B tz07a-variance-time.py --emit-g     # the M2 literals, for pfair.py
"""

import collections
import decimal
import importlib.util
import json
import math
import os
import statistics
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RECORDER = os.path.join(HERE, "recorder")
sys.path.insert(0, HERE)

import pfair                                                               # noqa: E402
from pfair import D, MS, config                                            # noqa: E402
from analyze import load_manifests, venue                                  # noqa: E402


def _load(name, filename):
    """Import a module whose filename carries a hyphen, so it cannot be `import`ed by name."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Set formation, the calibration arithmetic and the perturbation helpers are TZ-06's. They are
# called, never re-implemented: section 3 requires the member list to be re-derived by the same
# five conditions, and V4 requires this file to leave that one unmodified.
tz06 = _load("tz06calibration", "tz06-calibration.py")

NS = 10 ** 9

# TZ-07a section 3. The lag grid is the Architect's and is not extended or trimmed here.
LAGS = (1, 2, 5, 10, 20, 30, 50, 60, 80, 100, 140, 180, 200, 240, 300)

# TZ-07a section 3: the grid runs over [T0 - 300, T0 + 300], inclusive, so 601 points.
GRID_LO = -pfair.RUNUP_S
GRID_HI = config.INTERVAL_S
GRID_POINTS = GRID_HI - GRID_LO + 1

# TZ-07a section 4. The horizons the far branch reads, one per gated tau at or above 60.
G_LAGS = tuple(tau - 40 for tau in pfair.GATED_TAUS if tau >= pfair.SETTLEMENT_S)

# TZ-07a section 4: the literals carry six significant digits.
G_SIG_DIGITS = 6

# TZ-07a section 7, V2. The same twenty members and the same factor TZ-06 V4 used.
V2_MEMBERS = tz06.V4_MEMBERS

# TZ-07a section 7, V4. TZ-06 section 2.8's six Brier values and its P, to be reproduced
# exactly by the unmodified pipeline. Six printed decimals, as the report printed them.
TZ06_BRIER = {240: "0.210741", 180: "0.165723", 120: "0.125644",
              90: "0.086705", 60: "0.053946", 30: "0.010501"}
TZ06_P_AGREE = 397

# TZ-07a section 8, G3. The search interval and tolerance are fixed by the Architect; this
# file runs lambda-hat as a section 5 diagnostic only, with no threshold attached.
LAMBDA_LO, LAMBDA_HI, LAMBDA_TOL = 0.5, 3.0, 1e-9

# TZ-07a section 8. The out-of-sample set opens after the last member of the TZ-06 set.
TZ08_AFTER_T0 = 1789166400

# TZ-07a section 6. The only keys read out of `gamma.json`, and the only ones that may be.
GAMMA_MARKET_KEYS = ("conditionId", "slug")
GAMMA_REWARDS_KEYS = ("rewardsMinSize", "rewardsMaxSpread")
GAMMA_CLOB_KEYS = ("rewardsAmount", "rewardsDailyRate", "startDate", "endDate")


# ---- the member set, TZ-06 section 4 re-derived -----------------------------------

def members_and_manifests():
    """The 400 TZ-06 members, re-derived by TZ-06's own five conditions. Never transcribed."""
    manifests = load_manifests()
    rows, full = tz06.scoring_set(manifests)
    members = [r["T0"] for r in rows if r["member"]]
    assert full, "section 3: only %d of %d intervals qualify; the set is TZ-06's and is not " \
                 "re-cut here" % (len(members), tz06.SET_SIZE)
    return members, manifests, rows


# ---- M6, the disconnect rule ------------------------------------------------------

def excluded_seconds(t0, manifests):
    """The seconds of this member's grid that fall inside a recorded disconnect.

    Section 3 M6: a second is excluded when it falls inside a disconnect event recorded in the
    manifest of the directory that supplies it - the member's own or its predecessor. The two
    directories' windows overlap and the four streams share one socket, so a drop recorded by
    either is a drop of the feed itself at that instant; the two lists are therefore read as
    one. A second is a point sample of the step function, so it falls inside `[start, end]`
    when the instant does.

    Disconnect spans are the recorder's own `recv_ns`; the grid's seconds are epoch seconds of
    the venue's clock. The map's §6 puts the measured offset between the two below 19 ms, which
    is four orders of magnitude inside the shortest outage the manifests record.

    Returns the set of grid indices `0 … 600`, not of epoch seconds.
    """
    spans = []
    for key in (t0, t0 - config.INTERVAL_S):
        doc = manifests.get(key)
        if doc is None:
            continue
        for rec in doc["disconnects"]:
            spans.append((rec["start_recv_ns"], rec["end_recv_ns"]))
    out = set()
    if not spans:
        return out
    for i in range(GRID_POINTS):
        instant = (t0 + GRID_LO + i) * NS
        for start, end in spans:
            if start <= instant <= end:
                out.add(i)
                break
    return out


def excluded_prefix(excluded):
    """`pre[i]` = how many of the grid indices below `i` are excluded, so a span is one subtraction."""
    pre = [0] * (GRID_POINTS + 1)
    for i in range(GRID_POINTS):
        pre[i + 1] = pre[i] + (1 if i in excluded else 0)
    return pre


# ---- M1, the variance-time curve --------------------------------------------------

def member_increments(grid, excluded):
    """Per lag: the pooled sum of squared increments, the count taken and the count dropped.

    Section 3: every overlapping increment `P(s + h) - P(s)` for `s = 0 … 600 - h`, with an
    increment dropped when its closed span `[s, s + h]` contains an excluded second. No value
    is carried across a gap the manifest records.
    """
    pre = excluded_prefix(excluded)
    out = {}
    for h in LAGS:
        total, taken, dropped = D(0), 0, 0
        for s in range(GRID_POINTS - h):
            if pre[s + h + 1] - pre[s] > 0:
                dropped += 1
                continue
            d = grid[s + h] - grid[s]
            total += d * d
            taken += 1
        out[h] = (total, taken, dropped)
    return out


def curve(members, manifests):
    """M1 over the 400 members: the pooled `g(h)`, the per-member median, and M6's counts."""
    pooled = {h: [D(0), 0, 0] for h in LAGS}
    per_member = {h: [] for h in LAGS}
    touched, dropped_members = 0, []
    own_disconnect, predecessor_disconnect = [], []
    for t0 in members:
        if (manifests.get(t0) or {}).get("disconnect_count"):
            own_disconnect.append(t0)
        if (manifests.get(t0 - config.INTERVAL_S) or {}).get("disconnect_count"):
            predecessor_disconnect.append(t0)
        s3 = pfair.merged_stream(t0, config.S3_STREAM)
        grid = pfair.second_grid(s3, t0 + GRID_LO, t0 + GRID_HI)
        assert len(grid) == GRID_POINTS, "interval %d gave %d grid points" % (t0, len(grid))
        assert all(v is not None for v in grid), \
            "interval %d has no chainlink report at or before T0-300" % t0
        excluded = excluded_seconds(t0, manifests)
        stats = member_increments(grid, excluded)
        if any(stats[h][2] for h in LAGS):
            touched += 1
            dropped_members.append(t0)
        for h in LAGS:
            total, taken, drop = stats[h]
            pooled[h][0] += total
            pooled[h][1] += taken
            pooled[h][2] += drop
        # The member's own g(h), for the robustness reading. A member whose feed never moved
        # over the whole 601 seconds has no ratio; none is invented for it.
        own_one = stats[1][0] / D(stats[1][1]) if stats[1][1] else None
        for h in LAGS:
            total, taken, _drop = stats[h]
            if taken and own_one:
                per_member[h].append((total / D(taken * h)) / own_one)

    sigma_sq = {h: pooled[h][0] / D(pooled[h][1] * h) for h in LAGS}
    assert sigma_sq[1] > 0, "the pooled one-second variance is zero; there is no ratio to take"
    g_pooled = {h: sigma_sq[h] / sigma_sq[1] for h in LAGS}
    g_median = {h: statistics.median(sorted(per_member[h])) if per_member[h] else None
                for h in LAGS}
    return {
        "members": len(members),
        "grid": {"window": "[T0-300, T0+300]", "points": GRID_POINTS},
        "lags": list(LAGS),
        "per_lag": {h: {"increments_taken": pooled[h][1],
                        "increments_dropped": pooled[h][2],
                        "increments_possible": len(members) * (GRID_POINTS - h),
                        "sum_squared_increments": pooled[h][0],
                        "sigma_h_squared": sigma_sq[h],
                        "g_pooled": g_pooled[h],
                        "g_median_of_members": g_median[h],
                        "members_with_a_ratio": len(per_member[h])}
                    for h in LAGS},
        "M6": {"rule": "an increment whose closed span [s, s+h] contains a second inside a "
                       "disconnect recorded by the member's own or its predecessor's manifest "
                       "is dropped",
               "members_whose_own_manifest_records_a_disconnect": len(own_disconnect),
               "members_whose_predecessor_manifest_records_one": len(predecessor_disconnect),
               "of_those_whose_outage_misses_the_grid_window": len(predecessor_disconnect)
               - touched,
               "members_contributing_a_dropped_increment": touched,
               "their_T0s": dropped_members,
               "dropped_total": sum(pooled[h][2] for h in LAGS),
               "taken_total": sum(pooled[h][1] for h in LAGS)},
        "g_pooled": g_pooled,
        "g_median": g_median,
    }


def six_significant(value):
    """`value` rounded to six significant digits, as a Decimal - the form M2 freezes."""
    return +decimal.Context(prec=G_SIG_DIGITS,
                            rounding=decimal.ROUND_HALF_EVEN).create_decimal(value)


def emit_g(g_pooled):
    """The M2 literals exactly as they are written into `pfair.py`."""
    body = ", ".join("%d: D(\"%s\")" % (h, six_significant(g_pooled[h])) for h in G_LAGS)
    return "G_RATIO = {%s}\n" % body


def check_frozen_literals(g_pooled):
    """The literals in `pfair.py` are the measured curve. A pricer whose constants drift is not frozen."""
    checks = []
    for h in G_LAGS:
        want = six_significant(g_pooled[h])
        got = pfair.G_RATIO[h]
        assert got == want, "pfair.G_RATIO[%d] is %s; M1 measures %s" % (h, got, want)
        checks.append({"lag": h, "measured_6sd": want, "in_pfair": got, "equal": True})
    assert sorted(pfair.G_RATIO) == sorted(G_LAGS), \
        "pfair.G_RATIO carries %s; the far-branch horizons are %s" % (
            sorted(pfair.G_RATIO), sorted(G_LAGS))
    return checks


# ---- the corrected pricer, composed from pfair.py ---------------------------------

def corrected(row):
    """One observation repriced with the corrected `sd`. `state` and `sigma` are untouched."""
    sd = pfair.corrected_sd(row["tau"], row["sigma_live"])
    return sd, pfair.p_fair(row["state"], sd)


def corrected_observations(t0, s1, s3, taus=pfair.GATED_TAUS):
    """Every gated observation for one member, under the corrected estimator."""
    out = []
    for row in pfair.observations(t0, s1, s3, taus=taus):
        sd, p = corrected(row)
        out.append(dict(row, sd_corrected=sd, p_fair_corrected=p))
    return out


# ---- M3, in-sample diagnostics ----------------------------------------------------

def log_likelihood(pairs, lam):
    """`sum( y log Phi(z/lam) + (1-y) log(1 - Phi(z/lam)) )`, section 8 G3."""
    total = 0.0
    for z, y in pairs:
        p = pfair.phi(z / lam)
        q = p if y else 1.0 - p
        if q <= 0.0:
            return float("-inf")
        total += math.log(q)
    return total


def lambda_hat(pairs):
    """Section 8 G3's `lambda-hat`: ternary search over [0.5, 3.0] to 1e-9.

    Reported here as a section 5 diagnostic with no threshold. The same definition is the one
    TZ-08 will apply out of sample.
    """
    lo, hi = LAMBDA_LO, LAMBDA_HI
    while hi - lo > LAMBDA_TOL:
        a = lo + (hi - lo) / 3.0
        b = hi - (hi - lo) / 3.0
        if log_likelihood(pairs, a) < log_likelihood(pairs, b):
            lo = a
        else:
            hi = b
    lam = (lo + hi) / 2.0
    ll_hat, ll_one = log_likelihood(pairs, lam), log_likelihood(pairs, 1.0)
    ratio = 2.0 * (ll_hat - ll_one)
    return {"lambda_hat": lam, "ll_at_lambda_hat": ll_hat, "ll_at_one": ll_one,
            "likelihood_ratio": ratio,
            "chi_square_1df_p": math.erfc(math.sqrt(max(ratio, 0.0) / 2.0)),
            "n": len(pairs)}


def diagnostics(scored, constant_brier):
    """Section 5: TZ-06's tables recomputed with the corrected `sd`, beside the uncorrected.

    Every number this returns is in sample on the 400 members that produced the finding.
    """
    out = {}
    for tau in pfair.GATED_TAUS:
        rows = [r for m in scored for r in m["rows"] if r["tau"] == tau]
        labels = {id(r): r["label"] for r in rows}
        pairs_u = [(r["p_fair"], labels[id(r)]) for r in rows]
        pairs_c = [(r["p_fair_corrected"], labels[id(r)]) for r in rows]
        z_u = [(float(r["state"] / r["sd"]), labels[id(r)]) for r in rows]
        z_c = [(float(r["state"] / r["sd_corrected"]), labels[id(r)]) for r in rows]
        out[tau] = {
            "tau": tau, "n": len(rows),
            "uncorrected": dict(tz06.table_for(tau, [dict(r, label=labels[id(r)]) for r in rows],
                                               "p_fair", constant_brier),
                                lambda_hat=lambda_hat(z_u)),
            "corrected": dict(tz06.table_for(tau, [dict(r, label=labels[id(r)]) for r in rows],
                                             "p_fair_corrected", constant_brier),
                              lambda_hat=lambda_hat(z_c)),
            "sd_ratio_median": statistics.median(
                sorted(r["sd_corrected"] / r["sd"] for r in rows)),
        }
    return out


# ---- V2, causality of the corrected pricer ----------------------------------------

def v2(members):
    """Perturbation, never truncation: the future cannot move the corrected output, the last
    readable report must.

    The control is judged on `state`, `sd` and `p_fair` together, which is what section 7 V2
    names. `Phi` saturates at live scale - beyond about eight sigma `p_fair` is exactly 1.0 as
    a double - so a control judged on `p_fair` alone would under-count a reader that is read.
    `saturated_observations` is reported so the two figures reconcile.
    """
    identical = moved = considered = saturated = 0
    moved_p_only = 0
    leaks, inert = [], []
    for t0 in members[:V2_MEMBERS]:
        s1 = pfair.reports(t0, config.S1_STREAM)
        s3 = pfair.merged_stream(t0, config.S3_STREAM)
        for tau in pfair.GATED_TAUS:
            considered += 1
            at = (t0 + config.INTERVAL_S - tau) * MS
            base = corrected_observations(t0, s1, s3, taus=(tau,))[0]
            future = corrected_observations(t0, tz06.perturb_after(s1, at),
                                            tz06.perturb_after(s3, at), taus=(tau,))[0]
            same = (future["p_fair_corrected"] == base["p_fair_corrected"]
                    and future["state"] == base["state"]
                    and future["sd_corrected"] == base["sd_corrected"])
            identical += same
            if not same:
                leaks.append({"T0": t0, "tau": tau, "base": base["p_fair_corrected"],
                              "perturbed": future["p_fair_corrected"]})
            saturated += base["p_fair_corrected"] in (0.0, 1.0)
            control = corrected_observations(
                t0, s1, tz06.perturb_one(s3, tz06.last_readable(s3, at)), taus=(tau,))[0]
            did_move = ((control["state"], control["sd_corrected"],
                         control["p_fair_corrected"])
                        != (base["state"], base["sd_corrected"], base["p_fair_corrected"]))
            moved += did_move
            moved_p_only += control["p_fair_corrected"] != base["p_fair_corrected"]
            if not did_move:
                inert.append({"T0": t0, "tau": tau})
    return {"members": len(members[:V2_MEMBERS]), "taus": list(pfair.GATED_TAUS),
            "comparisons": considered,
            "bit_identical_under_future_perturbation": identical,
            "leaks": considered - identical, "leaking_observations": leaks,
            "negative_control_moved_state_sd_p_fair": moved,
            "negative_control_moved_p_fair_alone": moved_p_only,
            "negative_control_inert": inert,
            "saturated_observations": saturated,
            "factor": str(tz06.PERTURBATION)}


# ---- V4, the TZ-06 regression -----------------------------------------------------

def v4():
    """TZ-06's pipeline, unmodified, still reproducing section 2.8's Briers and its P."""
    out = subprocess.run([sys.executable, "-B", "tz06-calibration.py"],
                         cwd=HERE, capture_output=True, text=True)
    doc = json.loads(out.stdout) if out.returncode == 0 else None
    got, p_agree = None, None
    if doc is not None and doc["gate"]["evaluated"]:
        got = {int(tau): "%.6f" % value
               for tau, value in doc["gate"]["G1"]["brier_p_fair"].items()}
        p_agree = doc["P_precondition"]["agree"]
    sha = subprocess.run(["sha256sum", "tz06-calibration.py"], cwd=HERE,
                         capture_output=True, text=True).stdout.split()[0]
    return {"command": "python3 -B tz06-calibration.py", "exit_status": out.returncode,
            "tz06_calibration_sha256": sha,
            "expected_brier": TZ06_BRIER, "observed_brier": got,
            "brier_reproduces": got == {int(k): v for k, v in TZ06_BRIER.items()},
            "expected_P_agree": TZ06_P_AGREE, "observed_P_agree": p_agree,
            "P_reproduces": p_agree == TZ06_P_AGREE,
            "stderr_tail": out.stderr.strip().splitlines()[-1:]}


# ---- V5, the self-tests -----------------------------------------------------------

def v5():
    """`selftest-pfair.py`, run and counted - never transcribed."""
    out = subprocess.run([sys.executable, "-B", "selftest-pfair.py"],
                         cwd=HERE, capture_output=True, text=True)
    counts = {}
    for line in out.stdout.splitlines():
        if line.endswith("checks passed") and ":" in line:
            name, rest = line.split(":", 1)
            counts[name.strip()] = int(rest.split()[0])
    return {"command": "python3 -B selftest-pfair.py", "exit_status": out.returncode,
            "V5_checks_passed": counts.get("V5"),
            "machinery_checks_passed": counts.get("section 3 machinery"),
            "TZ_07a_checks_passed": counts.get("TZ-07a section 4"),
            "stderr_tail": out.stderr.strip().splitlines()[-1:]}


# ---- V8, how much test data exists ------------------------------------------------

def v8(manifests):
    """Section 7 V8: the interval directories past the TZ-06 set, and how many qualify."""
    root = os.path.join(config.ROOT, config.SERIES)
    after = sorted(int(name) for name in os.listdir(root) if int(name) > TZ08_AFTER_T0)
    qualifying, reasons = [], collections.Counter()
    for t0 in after:
        why = tz06.qualification(t0, manifests)
        if why:
            reasons["+".join(why)] += 1
        else:
            qualifying.append(t0)
    return {"after_T0": TZ08_AFTER_T0, "directories_on_disk": len(after),
            "first_T0": after[0] if after else None,
            "last_T0": after[-1] if after else None,
            "satisfying_TZ_06_section_4": len(qualifying),
            "required_by_section_8": tz06.SET_SIZE,
            "short_by": max(tz06.SET_SIZE - len(qualifying), 0),
            "non_qualifying_reason_counts": dict(sorted(reasons.items()))}


# ---- M4 / V9, the maker programme's published terms --------------------------------

def gamma_terms(t0):
    """Section 6's key list, read out of one `gamma.json` by that list and by nothing else.

    No key outside `GAMMA_MARKET_KEYS`, `GAMMA_REWARDS_KEYS` and `GAMMA_CLOB_KEYS` is touched,
    and no price-bearing field is read. An absent key is reported absent.
    """
    path = os.path.join(config.interval_dir(t0), "gamma.json")
    if not os.path.exists(path):
        return {"present": False}
    with open(path, "rt", encoding="utf-8") as fh:
        try:
            doc = json.load(fh)
        except ValueError:
            return {"present": False, "parse_error": True}
    market = doc[0] if isinstance(doc, list) else doc
    if not isinstance(market, dict):
        return {"present": False}
    out = {"present": True}
    for key in GAMMA_MARKET_KEYS:
        out[key] = market.get(key)
    rewards = market.get("rewards")
    out["rewards_key_absent"] = "rewards" not in market
    out["rewards_present"] = rewards is not None
    if not isinstance(rewards, dict):
        return out
    for key in GAMMA_REWARDS_KEYS:
        out[key] = rewards.get(key)
    clob = rewards.get("clobRewards")
    out["clobRewards_present"] = clob is not None
    if isinstance(clob, list):
        out["clobRewards"] = [{key: entry.get(key) for key in GAMMA_CLOB_KEYS}
                              for entry in clob if isinstance(entry, dict)]
    return out


def v9(members):
    """Section 6, as counts only. No threshold, no gate and no strategy conclusion."""
    rows = [gamma_terms(t0) for t0 in members]
    present = [r for r in rows if r.get("present")]
    with_rewards = [r for r in present if r.get("rewards_present")]
    absent = sum(1 for r in present if r.get("rewards_key_absent"))
    daily = collections.Counter()
    for r in with_rewards:
        for entry in r.get("clobRewards") or []:
            daily[(json.dumps(entry.get("rewardsDailyRate")), json.dumps(entry.get("startDate")),
                   json.dumps(entry.get("endDate")))] += 1
    return {
        "key_list": ["conditionId", "slug", "rewards.rewardsMinSize",
                     "rewards.rewardsMaxSpread", "rewards.clobRewards[].rewardsAmount",
                     "rewards.clobRewards[].rewardsDailyRate",
                     "rewards.clobRewards[].startDate", "rewards.clobRewards[].endDate"],
        "members": len(members),
        "gamma_documents_present": len(present),
        "conditionId_present": sum(1 for r in present if r.get("conditionId") is not None),
        "slug_present": sum(1 for r in present if r.get("slug") is not None),
        "rewards_block_non_null": len(with_rewards),
        "rewards_block_absent_or_null": len(present) - len(with_rewards),
        "rewards_key_absent_entirely": absent,
        "rewards_key_present_but_null": len(present) - len(with_rewards) - absent,
        "rewardsMinSize_values": dict(sorted(collections.Counter(
            json.dumps(r.get("rewardsMinSize")) for r in with_rewards).items())),
        "rewardsMaxSpread_values": dict(sorted(collections.Counter(
            json.dumps(r.get("rewardsMaxSpread")) for r in with_rewards).items())),
        "rewardsAmount_values": dict(sorted(collections.Counter(
            json.dumps(e.get("rewardsAmount")) for r in with_rewards
            for e in (r.get("clobRewards") or [])).items())),
        "rewardsDailyRate_by_date_range": {"%s | %s | %s" % k: v
                                           for k, v in sorted(daily.items())},
    }


# ---- the document ------------------------------------------------------------------

def build():
    members, manifests, rows = members_and_manifests()
    m1 = curve(members, manifests)
    literals = check_frozen_literals(m1["g_pooled"])

    scored = []
    for t0 in members:
        s1 = pfair.reports(t0, config.S1_STREAM)
        s3 = pfair.merged_stream(t0, config.S3_STREAM)
        info = venue(t0)
        label = 1 if info["resolved_up"] else 0
        obs = corrected_observations(t0, s1, s3)
        for row in obs:
            row["label"] = label
        scored.append({"T0": t0, "label": label, "rows": obs})

    labels = [m["label"] for m in scored]
    up_rate = sum(labels) / len(labels)
    constant_brier = tz06.brier([(up_rate, y) for y in labels])

    doc = {
        "set": {"source": "TZ-06 section 4, re-derived by tz06-calibration.scoring_set",
                "units_considered": len(rows), "members": len(members),
                "first_T0": members[0], "last_T0": members[-1],
                "observed_up_rate": up_rate, "brier_constant": constant_brier},
        "V1_curve": m1,
        "V2_causality": v2(members),
        "V4_regression": v4(),
        "V5_self_tests": v5(),
        "V6_disconnect_rule": m1["M6"],
        "V7_in_sample_diagnostics": {
            "warning": "IN SAMPLE on the 400 members that produced the finding. These numbers "
                       "are a fit diagnostic, they confirm nothing, and they support nothing.",
            "G_RATIO_as_written": {h: pfair.G_RATIO[h] for h in sorted(pfair.G_RATIO)},
            "literals_match_measurement": literals,
            "per_tau": diagnostics(scored, constant_brier)},
        "V8_test_data_available": v8(manifests),
        "V9_maker_terms": v9(members),
    }
    return doc


# ---- output --------------------------------------------------------------------------

def curve_table(doc):
    m1 = doc["V1_curve"]
    out = ["### V1 — the variance–time curve, %d members" % m1["members"], "",
           "| h (s) | increments taken | dropped | `sigma_h^2` | `g(h)` pooled | `g(h)` median of members |",
           "|---|---|---|---|---|---|"]
    for h in m1["lags"]:
        row = m1["per_lag"][h]
        out.append("| %d | %d | %d | %s | %s | %s |" % (
            h, row["increments_taken"], row["increments_dropped"],
            "%.6g" % row["sigma_h_squared"], "%.6f" % row["g_pooled"],
            "—" if row["g_median_of_members"] is None else "%.6f" % row["g_median_of_members"]))
    return out


def diag_tables(doc):
    out = ["", "### V7 — in-sample diagnostics — **in sample, and they confirm nothing**", "",
           "| tau | Brier uncorrected | Brier corrected | eligible bins | failing bins "
           "unc. | failing bins corr. | `λ̂` unc. | `λ̂` corr. | median sd ratio |",
           "|---|---|---|---|---|---|---|---|---|"]
    for tau in pfair.GATED_TAUS:
        row = doc["V7_in_sample_diagnostics"]["per_tau"][tau]
        u, c = row["uncorrected"], row["corrected"]
        out.append("| %d | %.6f | %.6f | %d | %d | %d | %.4f | %.4f | %.4f |" % (
            tau, u["brier"], c["brier"], c["eligible_bins"], u["failing_bins"],
            c["failing_bins"], u["lambda_hat"]["lambda_hat"], c["lambda_hat"]["lambda_hat"],
            row["sd_ratio_median"]))
    head = ["| bin | n | mean prediction | observed Up | central 99% region | eligible | verdict |",
            "|---|---|---|---|---|---|---|"]
    for tau in pfair.GATED_TAUS:
        row = doc["V7_in_sample_diagnostics"]["per_tau"][tau]
        for name in ("uncorrected", "corrected"):
            table = row[name]
            out += ["", "#### tau = %d, %s — in sample" % (tau, name), "",
                    "n = %d · Brier %.6f · Brier(constant) %.6f · `λ̂` %.4f"
                    % (table["n"], table["brier"], table["brier_constant"],
                       table["lambda_hat"]["lambda_hat"]), ""] + head + tz06.bin_rows(table)
    return out


def tables(doc):
    return "\n".join(curve_table(doc) + diag_tables(doc)) + "\n"


def main(argv):
    if argv[1:] == ["--emit-g"]:
        members, manifests, _rows = members_and_manifests()
        sys.stdout.write(emit_g(curve(members, manifests)["g_pooled"]))
        return 0
    doc = build()
    if argv[1:] == ["--tables"]:
        sys.stdout.write(tables(doc))
        return 0
    sys.stdout.write(json.dumps(doc, sort_keys=True, indent=2, default=str) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
