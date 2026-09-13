#!/usr/bin/env python3
"""TZ-08a: out-of-sample scoring of `p_fair` against the TZ-07a section 8 gate.

The pricer merged at `fb5c426` is scored on the 400 intervals TZ-08 formed and published -
disjoint in time from the 400 that produced `SD_SCALE` - against the gate TZ-07a section 8
fixed before any of this data existed. Phase 1 can only disqualify: a passing gate is not an
edge.

This file is a driver. It holds the window constant, the member-list assertions, the V2
sample rule, the disclosure table and the report tables, and no formula and no threshold.
Everything else is called: `pfair.py` prices; `tz06-calibration.py` forms the set, runs P and
V3, and holds the calibration arithmetic with its own `MAX_FAILING_BINS`;
`tz07a-variance-time.py` holds the corrected composition, `lambda_hat` and M6's disconnect
rule; `tz07b-settlement-dispersion.py` measures `Lambda`. The one frozen file this TZ changes
is `tz06-calibration.py`, extended by keyword-only parameters under TZ-08a section 5, and V1
is what proves the extension changed nothing.

G3 is reported and not judged. No committed code carries its bound and section 2.2 forbids
introducing one, so `lambda_hat` is printed exactly as the instrument returns it and the
Architect applies TZ-07a section 8 to that table.

Read-only over the capture: nothing under `/var/lib/btc-recorder/` is written, moved or
deleted, and `quotes.jsonl.gz` is never opened.

Run:  python3 -B tz08a-out-of-sample.py --out <directory>

writes `tz08a-results.json`, `tz08a-tables.md` and `tz08a-observations.csv` into the
directory. None of the three carries a wall-clock time or a path, so two runs compare by `cmp`.
"""

import collections
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import pfair                                                               # noqa: E402
from pfair import MS, config                                               # noqa: E402
from analyze import load_manifests                                         # noqa: E402


def _load(name, filename):
    """Import a module whose filename carries a hyphen, so it cannot be `import`ed by name."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# TZ-07b loads TZ-07a, which loads TZ-06, so both come through it: loading either a second
# time would be two module objects and two copies of one set.
tz07b = _load("tz07bsettlementdispersion", "tz07b-settlement-dispersion.py")
tz07a = tz07b.tz07a
tz06 = tz07a.tz06

# TZ-08a section 3: the set opens after the last TZ-06 member.
AFTER_T0 = 1789166400

# TZ-08a section 3: the set TZ-08 formed and published, re-derived here and asserted equal.
# It is never shrunk, re-ordered or re-selected.
SET_SHA256 = "3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762"
SET_UNITS_CONSIDERED = 433
SET_NON_MEMBERS = 33
SET_NON_MEMBER_REASONS = ["disconnect"]
SET_FIRST_MEMBER = 1789166700
SET_LAST_MEMBER = 1789296300

# TZ-08a section 3 and section 7 V1: the TZ-06 member list, by the unmodified code path.
TZ06_SHA256 = "6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9"

# TZ-08a section 2.1 and section 7 V5: `pfair.py` as frozen, at run start and at run end.
PFAIR_SHA256 = "cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f"

# TZ-08a section 7 V2: the sample size. Which members fill it is the rule in `v2_sample`.
V2_SAMPLE = 120

# TZ-08a section 7 V7, from System Map section 7 item 22: the Architect's prediction of
# `lambda_hat`, written before this set existed. Printed beside it; nothing passes or fails.
PREDICTED_LAMBDA = {240: "0.999", 180: "0.946", 120: "0.945", 90: "0.761", 60: "0.787",
                    30: "1.012"}

# TZ-08a section 4: every tau the pricer serves and the gate does not score is computed and
# reported with no threshold. That is `10`.
DIAGNOSTIC_TAUS = tuple(tau for tau in pfair.TAUS if tau not in pfair.GATED_TAUS)

# The model's output, as TZ-07a V2 judged it and TZ-08a section 7 V2 names it.
OUTPUT = ("state", "sd_corrected", "p_fair_corrected")

# Section 6: one row per observation, TZ-06's forensics columns plus the corrected pair.
CSV_HEADER = ["T0", "tau", "K", "S_t", "m_r", "sigma_live", "sigma_pre", "state", "sd",
              "p_fair", "sd_corrected", "p_fair_corrected", "label"]


# ---- section 2.1 and V5: the pricer does not move ---------------------------------

def pfair_sha(when):
    """`pfair.py` against its frozen hash. Asserted, so a drifted pricer scores nothing."""
    with open(os.path.join(HERE, "pfair.py"), "rb") as fh:
        got = hashlib.sha256(fh.read()).hexdigest()
    assert got == PFAIR_SHA256, "section 2.1: pfair.py at %s is %s, frozen at %s" % (
        when, got, PFAIR_SHA256)
    return got


# ---- section 3 and V4: the set ----------------------------------------------------

def the_set(manifests):
    """Section 3: TZ-08's set re-derived by the committed code, and every assertion on it.

    All of this runs before anything is scored. The walk stops at the 400th member, so the set
    is a prefix of the ordered universe and no directory written since TZ-08's run can move it.
    """
    rows, full = tz06.scoring_set(manifests, after=AFTER_T0)
    members = [r["T0"] for r in rows if r["member"]]
    outside = [r for r in rows if not r["member"]]
    rows06, full06 = tz06.scoring_set(manifests)
    members06 = [r["T0"] for r in rows06 if r["member"]]
    doc = {
        "rule": "the first %d qualifying units, in T0 order, with T0 > %d"
                % (tz06.SET_SIZE, AFTER_T0),
        "units_considered": len(rows), "members": len(members), "non_members": len(outside),
        "non_member_reasons": dict(sorted(collections.Counter(
            " + ".join(r["reasons"]) for r in outside).items())),
        "first_unit": rows[0]["T0"], "last_unit": rows[-1]["T0"],
        "first_member": members[0], "last_member": members[-1],
        "member_list_sha256": tz07b.member_list_sha(members),
        "member_list_form": "the sorted T0 list as decimal ASCII, joined by newlines, "
                            "no trailing newline",
        "tz06_members": len(members06),
        "tz06_member_list_sha256": tz07b.member_list_sha(members06),
        "intersection_with_tz06": len(set(members) & set(members06)),
    }
    assert full and len(members) == tz06.SET_SIZE, \
        "section 3: %d members of %d; the set is never shrunk" % (len(members), tz06.SET_SIZE)
    assert doc["member_list_sha256"] == SET_SHA256, \
        "section 3: the member list hashes to %s, published %s" % (
            doc["member_list_sha256"], SET_SHA256)
    assert len(rows) == SET_UNITS_CONSIDERED, \
        "section 3: %d units considered, %d published" % (len(rows), SET_UNITS_CONSIDERED)
    assert [r["T0"] for r in rows] == list(range(SET_FIRST_MEMBER, SET_LAST_MEMBER + 1,
                                                 config.INTERVAL_S)), \
        "section 3: the units considered are not every grid slot from %d to %d" % (
            SET_FIRST_MEMBER, SET_LAST_MEMBER)
    assert len(outside) == SET_NON_MEMBERS, \
        "section 3: %d non-members, %d published" % (len(outside), SET_NON_MEMBERS)
    assert all(r["reasons"] == SET_NON_MEMBER_REASONS for r in outside), \
        "section 3: a non-member fails on something other than disconnect: %s" % (
            doc["non_member_reasons"])
    assert (members[0], members[-1]) == (SET_FIRST_MEMBER, SET_LAST_MEMBER), \
        "section 3: members run %d to %d" % (members[0], members[-1])
    assert min(members) > AFTER_T0, "section 3: min(T0) %d is not after %d" % (
        min(members), AFTER_T0)
    assert doc["intersection_with_tz06"] == 0, \
        "section 3: %d members are also TZ-06 members" % doc["intersection_with_tz06"]
    assert full06 and doc["tz06_member_list_sha256"] == TZ06_SHA256, \
        "section 3: the TZ-06 list hashes to %s, published %s" % (
            doc["tz06_member_list_sha256"], TZ06_SHA256)
    return rows, members, doc


# ---- V1: the section 5 edit changes nothing ---------------------------------------

def v1():
    """Section 7 V1: `tz06-calibration.py`, as edited, run with no argument on the TZ-06 window.

    The six Brier values and P it must reproduce are TZ-07a's committed copies of TZ-06
    section 2.8, so none is re-typed here; the member-list hash is section 3's.
    """
    out = subprocess.run([sys.executable, "-B", "tz06-calibration.py"], cwd=HERE,
                         capture_output=True, text=True)
    assert out.returncode == 0, "V1: tz06-calibration.py exited %d: %s" % (
        out.returncode, out.stderr.strip().splitlines()[-1:])
    doc = json.loads(out.stdout)
    assert doc["gate"]["evaluated"], "V1: the TZ-06 pipeline did not evaluate its gate"
    expected = {int(tau): value for tau, value in tz07a.TZ06_BRIER.items()}
    observed = {int(tau): "%.6f" % value
                for tau, value in doc["gate"]["G1"]["brier_p_fair"].items()}
    members = [r["T0"] for r in doc["rows"] if r["member"]]
    result = {
        "command": "python3 -B tz06-calibration.py",
        "brier_expected": expected, "brier_observed": observed,
        "brier_values": len(expected),
        "brier_reproduced_to_six_decimals": sum(1 for tau in expected
                                                if observed.get(tau) == expected[tau]),
        "P_agree": doc["P_precondition"]["agree"], "P_n": doc["P_precondition"]["n"],
        "P_agree_expected": tz07a.TZ06_P_AGREE,
        "members": len(members), "member_list_sha256": tz07b.member_list_sha(members),
    }
    assert result["brier_reproduced_to_six_decimals"] == len(expected), \
        "V1: Brier %s, expected %s" % (observed, expected)
    assert (result["P_agree"], result["P_n"]) == (tz07a.TZ06_P_AGREE, tz06.SET_SIZE), \
        "V1: P %d of %d, expected %d of %d" % (result["P_agree"], result["P_n"],
                                               tz07a.TZ06_P_AGREE, tz06.SET_SIZE)
    assert result["member_list_sha256"] == TZ06_SHA256, \
        "V1: the TZ-06 member list hashes to %s" % result["member_list_sha256"]
    return result


# ---- V2: causality of the corrected pricer ----------------------------------------

def m6_members(members, manifests):
    """The members carrying a recorded disconnect, read the way TZ-07a M6 reads the manifests.

    M6 excludes a second that falls inside a disconnect recorded by the member's own manifest
    or its predecessor's. `recorded` is every member one of those two manifests records a
    disconnect for, which is what TZ-07a's own M6 disclosure counts; `excluding` is the subset
    whose grid M6 actually drops a second of, by `tz07a.excluded_seconds`. The sample takes
    the wider list, so it holds every member under either reading.
    """
    recorded = [t0 for t0 in members
                if (manifests.get(t0) or {}).get("disconnect_count")
                or (manifests.get(t0 - config.INTERVAL_S) or {}).get("disconnect_count")]
    excluding = [t0 for t0 in members if tz07a.excluded_seconds(t0, manifests)]
    assert set(excluding) <= set(recorded), \
        "M6 drops seconds of %s, whose manifests record no disconnect" % (
            sorted(set(excluding) - set(recorded)))
    return recorded, excluding


def v2_sample(members, recorded):
    """Section 7 V2's sample: every member in `recorded`, filled out from the rest in T0 order."""
    assert len(recorded) <= V2_SAMPLE, \
        "V2: %d members carry a disconnect, more than the %d the sample holds" % (
            len(recorded), V2_SAMPLE)
    held = set(recorded)
    rest = [t0 for t0 in members if t0 not in held]
    return sorted(recorded + rest[:V2_SAMPLE - len(recorded)])


def v2(sample):
    """Section 7 V2: perturbation, never truncation, on the corrected pricer.

    The perturbation is `tz06.perturb_after`, unmodified: every `chainlink` and `twap60` report
    with `ts > ts_ms`. The negative control perturbs the `chainlink` report `tz06.last_readable`
    returns, `ts <= ts_ms`. That the control's subject lies outside the perturbation set is
    asserted per observation from what `perturb_after` actually changed - not from a second
    copy of its predicate - before any count is taken.

    `Phi` saturates at live scale, so the control is judged on `state`, `sd_corrected` and
    `p_fair_corrected` together; the count moved on `p_fair_corrected` alone and the saturated
    count are reported so the two figures reconcile.
    """
    n = identical = moved = moved_p = saturated = disjoint = at_instant = 0
    members_identical = members_moved = 0
    touched_s3 = touched_s1 = 0
    fewest = None
    leaks, inert = [], []
    for t0 in sample:
        s1 = pfair.reports(t0, config.S1_STREAM)
        s3 = pfair.merged_stream(t0, config.S3_STREAM)
        member_identical = member_moved = True
        for tau in pfair.GATED_TAUS:
            n += 1
            at = (t0 + config.INTERVAL_S - tau) * MS
            p1, p3 = tz06.perturb_after(s1, at), tz06.perturb_after(s3, at)
            subject = tz06.last_readable(s3, at)
            perturbed = {i for i in range(len(s3)) if p3[i] != s3[i]}
            assert subject is not None and subject not in perturbed, \
                "V2: T0 %d tau %d: the control's report %s is inside the perturbation set" % (
                    t0, tau, subject)
            disjoint += 1
            at_instant += s3[subject][0] == at
            touched_s3 += len(perturbed)
            touched_s1 += sum(1 for i in range(len(s1)) if p1[i] != s1[i])
            fewest = len(perturbed) if fewest is None else min(fewest, len(perturbed))

            base = tz07a.corrected_observations(t0, s1, s3, taus=(tau,))[0]
            future = tz07a.corrected_observations(t0, p1, p3, taus=(tau,))[0]
            control = tz07a.corrected_observations(t0, s1, tz06.perturb_one(s3, subject),
                                                   taus=(tau,))[0]
            same = all(future[k] == base[k] for k in OUTPUT)
            did_move = any(control[k] != base[k] for k in OUTPUT)
            identical += same
            moved += did_move
            moved_p += control["p_fair_corrected"] != base["p_fair_corrected"]
            saturated += base["p_fair_corrected"] in (0.0, 1.0)
            member_identical = member_identical and same
            member_moved = member_moved and did_move
            if not same:
                leaks.append({"T0": t0, "tau": tau})
            if not did_move:
                inert.append({"T0": t0, "tau": tau})
        members_identical += member_identical
        members_moved += member_moved
    doc = {
        "members": len(sample), "taus": list(pfair.GATED_TAUS), "observations": n,
        "factor": str(tz06.PERTURBATION),
        "perturbation": "tz06-calibration.perturb_after, every chainlink and twap60 report "
                        "with ts > ts_ms",
        "negative_control": "tz06-calibration.perturb_one on the chainlink report "
                            "tz06-calibration.last_readable returns, ts <= ts_ms",
        "disjoint_observations": disjoint,
        "control_subject_stamped_at_the_checkpoint_instant": at_instant,
        "chainlink_reports_perturbed_total": touched_s3,
        "twap60_reports_perturbed_total": touched_s1,
        "fewest_chainlink_reports_perturbed_in_one_observation": fewest,
        "bit_identical_observations": identical,
        "bit_identical_members_all_six_taus": members_identical,
        "leaking_observations": leaks,
        "negative_control_moved_observations": moved,
        "negative_control_moved_members_all_six_taus": members_moved,
        "negative_control_moved_p_fair_corrected_alone": moved_p,
        "negative_control_inert": inert,
        "saturated_observations": saturated,
    }
    assert disjoint == n, "V2: %d of %d observations disjoint" % (disjoint, n)
    assert (identical, members_identical) == (n, len(sample)), \
        "V2: bit-identical %d of %d observations, %d of %d members" % (
            identical, n, members_identical, len(sample))
    assert (moved, members_moved) == (n, len(sample)), \
        "V2: the control moved %d of %d observations, %d of %d members" % (
            moved, n, members_moved, len(sample))
    return doc


def feed_record(members):
    """Section 7 V2, on the record: whole-second stamps, and checkpoints with a report at the instant.

    Counted over each member's merged `chainlink` stream, the one the pricer reads, so a report
    in the overlap of two neighbouring members is counted once for each.
    """
    total = off_second = 0
    at_instant = {tau: 0 for tau in pfair.GATED_TAUS}
    for t0 in members:
        s3 = pfair.merged_stream(t0, config.S3_STREAM)
        stamps = {ts for ts, _value in s3}
        total += len(s3)
        off_second += sum(1 for ts, _value in s3 if ts % MS)
        for tau in pfair.GATED_TAUS:
            at_instant[tau] += (t0 + config.INTERVAL_S - tau) * MS in stamps
    return {"members": len(members),
            "chainlink_reports_in_merged_member_streams": total,
            "of_which_timestamp_not_a_multiple_of_1000_ms": off_second,
            "checkpoints": len(members) * len(pfair.GATED_TAUS),
            "checkpoints_with_a_chainlink_report_at_the_exact_instant":
                sum(at_instant.values()),
            "per_tau": at_instant}


# ---- section 6: what is scored ----------------------------------------------------

def corrected_scored(scored):
    """TZ-06's priced observations, each carried through `tz07a.corrected`.

    `tz07a.corrected` is `corrected_observations` applied to one row, so the corrected figures
    read the same `state` and `sigma_live` the pipeline priced, and the set is priced once.
    """
    out = []
    for member in scored:
        rows = []
        for row in member["observations"]:
            sd, p = tz07a.corrected(row)
            rows.append(dict(row, sd_corrected=sd, p_fair_corrected=p, label=member["label"]))
        out.append({"T0": member["T0"], "label": member["label"], "rows": rows})
    return out


def z_pairs(rows, sd_key):
    """Section 8 G3's input, `z = state / sd`, formed exactly as `tz07a.diagnostics` forms it.

    Needed only at the diagnostic tau, which `diagnostics` does not walk; at the six gated
    taus `score` asserts that this reproduces the instrument's `lambda_hat` exactly.
    """
    return [(float(r["state"] / r[sd_key]), r["label"]) for r in rows]


def score(doc06, scored_c):
    """G1, G2 and the scale statistic, for the corrected pricer and the uncorrected one.

    At the six gated taus all three come out of `tz07a.diagnostics`, which is `tz06.table_for`
    and `lambda_hat` for both estimators. The diagnostic tau gets the same two calls directly.
    """
    constant_brier = doc06["gate"]["G1"]["brier_constant"]
    diag = tz07a.diagnostics(scored_c, constant_brier)
    per_tau = {}
    for tau in pfair.TAUS:
        rows = [r for m in scored_c for r in m["rows"] if r["tau"] == tau]
        z_c, z_u = z_pairs(rows, "sd_corrected"), z_pairs(rows, "sd")
        if tau in diag:
            corrected, uncorrected = diag[tau]["corrected"], diag[tau]["uncorrected"]
            assert tz07a.lambda_hat(z_c) == corrected["lambda_hat"] \
                and tz07a.lambda_hat(z_u) == uncorrected["lambda_hat"], \
                "tau %d: the driver's z is not the instrument's" % tau
            pipeline_brier = doc06["gate"]["G1"]["brier_p_fair"][tau]
        else:
            corrected = dict(tz06.table_for(tau, rows, "p_fair_corrected", constant_brier),
                             lambda_hat=tz07a.lambda_hat(z_c))
            uncorrected = dict(tz06.table_for(tau, rows, "p_fair", constant_brier),
                               lambda_hat=tz07a.lambda_hat(z_u))
            pipeline_brier = doc06["V7_tau_10"]["table"]["brier"]
        assert uncorrected["brier"] == pipeline_brier, \
            "tau %d: the uncorrected Brier %r is not the pipeline's %r" % (
                tau, uncorrected["brier"], pipeline_brier)
        per_tau[tau] = {
            "tau": tau, "gated": tau in pfair.GATED_TAUS, "n": len(rows),
            "corrected": corrected, "uncorrected": uncorrected,
            "saturated_p_fair_corrected": sum(1 for r in rows
                                              if r["p_fair_corrected"] in (0.0, 1.0)),
            "saturated_p_fair_uncorrected": sum(1 for r in rows if r["p_fair"] in (0.0, 1.0)),
        }
    return per_tau


def gate(doc06, per_tau):
    """G1 and G2 on the corrected pricer, from `tz06.table_for`'s own verdicts per tau and
    `tz06.MAX_FAILING_BINS`, aggregated as `tz06.build` aggregates them. G3 is not judged."""
    gated = pfair.GATED_TAUS
    g1 = {tau: per_tau[tau]["corrected"]["beats_constant"] for tau in gated}
    failing = {tau: per_tau[tau]["corrected"]["failing_bins"] for tau in gated}
    constant_brier = doc06["gate"]["G1"]["brier_constant"]
    return {
        "predictions": "the corrected pricer: pfair.corrected_sd on sigma_live",
        "G1": {"rule": doc06["gate"]["G1"]["rule"],
               "constant_c": doc06["gate"]["G1"]["constant_c"],
               "brier_constant": constant_brier,
               "brier_p_fair_corrected": {tau: per_tau[tau]["corrected"]["brier"]
                                          for tau in gated},
               "margin": {tau: constant_brier - per_tau[tau]["corrected"]["brier"]
                          for tau in gated},
               "per_tau": g1, "taus_beating_the_constant": sum(g1.values()),
               "taus": len(gated), "passes": all(g1.values())},
        "G2": {"rule": doc06["gate"]["G2"]["rule"],
               "eligible_bins_corrected": {tau: per_tau[tau]["corrected"]["eligible_bins"]
                                           for tau in gated},
               "failing_bins_corrected": failing,
               "total_failing": sum(failing.values()),
               "allowed": tz06.MAX_FAILING_BINS,
               "passes": sum(failing.values()) <= tz06.MAX_FAILING_BINS},
        "G3": {"judged": False,
               "reason": "no committed code carries G3's bound and TZ-08a section 2.2 forbids "
                         "introducing one; the Architect applies TZ-07a section 8 to the "
                         "scale-statistic table"},
    }


# ---- V8 and V9: the settlement quantity's dispersion, out of sample ----------------

def v8(members, manifests, sample):
    """Section 7 V8 and V9: the TZ-07b instrument, unmodified, on the 400 members.

    `tz07b.dispersion` is the instrument itself. `tz07b.check_frozen_literals` is not called:
    it asserts the literal equals the measurement, which holds by construction in sample and
    is exactly what this set is here to test. The ratio to the frozen literal is printed with
    no threshold and changes no constant.

    The instrument's shortcut - the bisected window handed to `time_weighted_mean` - is guarded
    by its own `slice_guard`, called here on every V2-sample member rather than on the first
    alone, because System Map section 7 item 24 requires a guard on a shortcut to sample across
    the scored set and to include the members carrying a disconnect by construction.
    """
    guards = [tz07b.slice_guard(t0, manifests) for t0 in sample]
    m1 = tz07b.dispersion(members, manifests)
    m1["SD_SCALE"] = {tau: pfair.SD_SCALE[tau] for tau in pfair.TAUS}
    m1["lambda_over_SD_SCALE"] = {tau: m1["per_tau"][tau]["lambda"] / pfair.SD_SCALE[tau]
                                  for tau in pfair.TAUS}
    guard = {"members": len(guards),
             "anchors_priced_twice": sum(g["anchors_priced_twice"] for g in guards),
             "identical_to_the_whole_stream": sum(g["identical_to_the_whole_stream"]
                                                  for g in guards)}
    return m1, guard


# ---- the document ------------------------------------------------------------------

def build():
    pfair_at_start = pfair_sha("run start")
    manifests = load_manifests()

    # Section 3 and V4, then V1 and V2: everything that stops the run comes before any score.
    rows, members, set_doc = the_set(manifests)
    regression = v1()
    recorded, excluding = m6_members(members, manifests)
    sample = v2_sample(members, recorded)
    causality = v2(sample)
    causality["sample_rule"] = (
        "every member whose own manifest or whose predecessor's records a disconnect - the two "
        "manifests TZ-07a M6 reads - then the remaining members in T0 order until %d; listed "
        "in T0 order" % V2_SAMPLE)
    causality["sample_members_carrying_a_recorded_disconnect"] = len(recorded)
    causality["sample_members_whose_grid_M6_drops_a_second_of"] = len(excluding)
    causality["sample_filled_from_the_remainder"] = V2_SAMPLE - len(recorded)
    causality["sample"] = sample
    record = feed_record(members)

    # Section 4: TZ-06 P and V3 on this set, by the unmodified code path, with the floors that
    # code carries. P's is `P_REQUIRED`. V3 carries none, and none is invented here.
    doc06, scored = tz06.build(after=AFTER_T0)
    assert doc06["rows"] == rows, "the pipeline formed a set other than the one asserted"
    p_doc = doc06["P_precondition"]
    assert p_doc["passes"] and doc06["gate"]["evaluated"], \
        "section 9 item 9: TZ-06 P %d of %d, below the floor of %d" % (
            p_doc["agree"], p_doc["n"], p_doc["required"])

    scored_c = corrected_scored(scored)
    per_tau = score(doc06, scored_c)
    verdicts = gate(doc06, per_tau)
    prediction = {tau: {"predicted": PREDICTED_LAMBDA[tau],
                        "lambda_hat": per_tau[tau]["corrected"]["lambda_hat"]["lambda_hat"],
                        "difference": per_tau[tau]["corrected"]["lambda_hat"]["lambda_hat"]
                        - float(PREDICTED_LAMBDA[tau])}
                  for tau in pfair.GATED_TAUS}
    dispersion, guard = v8(members, manifests, sample)
    csv = csv_text(scored_c)
    pfair_at_end = pfair_sha("run end")

    doc = {
        "tz": "TZ-08a",
        "pfair_sha256": {"frozen": PFAIR_SHA256, "run_start": pfair_at_start,
                         "run_end": pfair_at_end},
        "set": set_doc,
        "disclosure": rows,
        "V1_regression": regression,
        "V2_causality": causality,
        "V2_on_the_record": record,
        "TZ06_P": p_doc,
        "TZ06_V3": doc06["V3_K_reconstruction"],
        "gate": verdicts,
        "per_tau": per_tau,
        "G3_constants": {"LAMBDA_LO": tz07a.LAMBDA_LO, "LAMBDA_HI": tz07a.LAMBDA_HI,
                         "LAMBDA_TOL": tz07a.LAMBDA_TOL},
        "V7_prediction": prediction,
        "V8_dispersion": dispersion,
        "V8_slice_guard": guard,
        "observations_file": {"lines": len(csv.splitlines()),
                              "bytes": len(csv.encode("utf-8")),
                              "sha256": hashlib.sha256(csv.encode("utf-8")).hexdigest()},
    }
    return doc, csv


def csv_text(scored_c):
    """Section 6's observations file: one row per observation, in T0 then tau order."""
    lines = [",".join(CSV_HEADER)]
    for member in scored_c:
        for row in member["rows"]:
            lines.append(",".join([
                str(row["T0"]), str(row["tau"]), str(row["K"]), str(row["S_t"]),
                "" if row["m_r"] is None else str(row["m_r"]), str(row["sigma_live"]),
                str(row["sigma_pre"]), str(row["state"]), str(row["sd"]), repr(row["p_fair"]),
                str(row["sd_corrected"]), repr(row["p_fair_corrected"]), str(row["label"])]))
    return "\n".join(lines) + "\n"


# ---- output --------------------------------------------------------------------------

def tau_name(tau):
    return "%d" % tau if tau in pfair.GATED_TAUS else "%d (diagnostic)" % tau


def disclosure(rows):
    out = ["| # | T0 | open (UTC) | member | reason not a member |", "|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        out.append("| %d | %d | %s | %s | %s |" % (
            i, r["T0"], time.strftime("%Y-%m-%d %H:%M", time.gmtime(r["T0"])),
            r["member"] or "—", " + ".join(r["reasons"]) or "—"))
    return out


def lambda_rows(per_tau, name):
    out = ["| tau | `lambda_hat` | `ll_at_lambda_hat` | `ll_at_one` | `likelihood_ratio` | "
           "`chi_square_1df_p` | `n` |", "|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        lam = per_tau[tau][name]["lambda_hat"]
        out.append("| %s | %.6f | %.6f | %.6f | %.6f | %.6g | %d |" % (
            tau_name(tau), lam["lambda_hat"], lam["ll_at_lambda_hat"], lam["ll_at_one"],
            lam["likelihood_ratio"], lam["chi_square_1df_p"], lam["n"]))
    return out


def tables(doc):
    s, g, per = doc["set"], doc["gate"], doc["per_tau"]
    out = ["## The set, every unit considered", "",
           "%s. %d units considered, %d members, %d non-members (%s). Members %d to %d. "
           "Member-list SHA-256 `%s`." % (
               s["rule"], s["units_considered"], s["members"], s["non_members"],
               ", ".join("%s: %d" % kv for kv in s["non_member_reasons"].items()),
               s["first_member"], s["last_member"], s["member_list_sha256"]), ""]
    out += disclosure(doc["disclosure"])

    g1 = g["G1"]
    out += ["", "## G1 — the corrected pricer", "",
            "`c` = %.6f, the observed Up rate over the %d · `Brier(c)` = %.6f" % (
                g1["constant_c"], s["members"], g1["brier_constant"]), "",
            "| tau | n | `Brier(p_fair)` | `Brier(c)` | `Brier(c) - Brier(p_fair)` | "
            "`Brier(p_fair) < Brier(c)` |", "|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        c = per[tau]["corrected"]
        out.append("| %s | %d | %.6f | %.6f | %+.6f | %s |" % (
            tau_name(tau), c["n"], c["brier"], c["brier_constant"],
            c["brier_constant"] - c["brier"], "yes" if c["beats_constant"] else "no"))

    g2 = g["G2"]
    out += ["", "## G2 — eligible and failing bins, per estimator", "",
            "| tau | eligible, corrected | failing, corrected | eligible, uncorrected | "
            "failing, uncorrected |", "|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        c, u = per[tau]["corrected"], per[tau]["uncorrected"]
        out.append("| %s | %d | %d | %d | %d |" % (
            tau_name(tau), c["eligible_bins"], c["failing_bins"], u["eligible_bins"],
            u["failing_bins"]))
    out += ["", "Corrected, across the six gated taus: %d failing of %d eligible; "
            "`MAX_FAILING_BINS` = %d." % (g2["total_failing"],
                                          sum(g2["eligible_bins_corrected"].values()),
                                          g2["allowed"])]
    for name in ("corrected", "uncorrected"):
        for tau in pfair.TAUS:
            t = per[tau][name]
            out += ["", "### tau = %s, %s" % (tau_name(tau), name), "",
                    "n = %d · observed Up rate %.4f · Brier %.6f · Brier(constant) %.6f · "
                    "saturated `p_fair` %d" % (
                        t["n"], t["observed_up_rate"], t["brier"], t["brier_constant"],
                        per[tau]["saturated_p_fair_" + name]), ""]
            out += tz06.BIN_HEAD + tz06.bin_rows(t)

    out += ["", "## The scale statistic, corrected pricer — not judged here", ""]
    out += lambda_rows(per, "corrected")
    out += ["", "## The scale statistic, uncorrected pricer — no threshold", ""]
    out += lambda_rows(per, "uncorrected")
    k = doc["G3_constants"]
    out += ["", "`LAMBDA_LO` = %r · `LAMBDA_HI` = %r · `LAMBDA_TOL` = %r" % (
        k["LAMBDA_LO"], k["LAMBDA_HI"], k["LAMBDA_TOL"])]

    p, v3 = doc["TZ06_P"], doc["TZ06_V3"]
    res = p["reconstruction_residual_usd"]
    out += ["", "## TZ-06 P and TZ-06 V3", "",
            "| check | n | count | floor the code carries | median abs residual (USD) | "
            "worst (USD) | worst at T0 |", "|---|---|---|---|---|---|---|",
            "| TZ-06 P | %d | %d agree | %d | %s | %s | %d |" % (
                p["n"], p["agree"], p["required"], res["median_abs"], res["worst_abs"],
                res["worst_at_T0"]),
            "| TZ-06 V3 | %d | %d equal at published precision | none | %s | %s | %d |" % (
                v3["n"], v3["equal_at_published_precision"], v3["median_abs_residual_usd"],
                v3["worst_residual_usd"], v3["worst_at_T0"]), "",
            "P disagreeing intervals: %s" % (
                ", ".join("%d (label %d, m_close - K %s)" % (d["T0"], d["label"],
                                                             d["m_close_minus_K"])
                          for d in p["disagreeing_intervals"]) or "none"),
            "P agree when compared as doubles: %d · P median signed residual (USD): %s · "
            "V3 strict Decimal equal: %d" % (p["agree_when_compared_as_doubles"],
                                             res["median_signed"], v3["strict_decimal_equal"])]

    v1 = doc["V1_regression"]
    out += ["", "## V1", "", "| tau | expected | observed | equal |", "|---|---|---|---|"]
    for tau in sorted(v1["brier_expected"], reverse=True):
        out.append("| %d | %s | %s | %s |" % (
            tau, v1["brier_expected"][tau], v1["brier_observed"][tau],
            "yes" if v1["brier_expected"][tau] == v1["brier_observed"][tau] else "no"))
    out += ["", "Brier reproduced %d of %d · P %d of %d · member list `%s`" % (
        v1["brier_reproduced_to_six_decimals"], v1["brier_values"], v1["P_agree"], v1["P_n"],
        v1["member_list_sha256"])]

    v2 = doc["V2_causality"]
    rec = doc["V2_on_the_record"]
    out += ["", "## V2", "", "| count | value |", "|---|---|"]
    for key in ("members", "observations", "sample_members_carrying_a_recorded_disconnect",
                "sample_members_whose_grid_M6_drops_a_second_of",
                "sample_filled_from_the_remainder", "disjoint_observations",
                "bit_identical_observations", "bit_identical_members_all_six_taus",
                "negative_control_moved_observations",
                "negative_control_moved_members_all_six_taus",
                "negative_control_moved_p_fair_corrected_alone", "saturated_observations",
                "control_subject_stamped_at_the_checkpoint_instant",
                "chainlink_reports_perturbed_total", "twap60_reports_perturbed_total",
                "fewest_chainlink_reports_perturbed_in_one_observation"):
        out.append("| `%s` | %s |" % (key, v2[key]))
    for key in ("chainlink_reports_in_merged_member_streams",
                "of_which_timestamp_not_a_multiple_of_1000_ms", "checkpoints",
                "checkpoints_with_a_chainlink_report_at_the_exact_instant"):
        out.append("| `%s` | %s |" % (key, rec[key]))
    out += ["", "Checkpoints with a report at the exact instant, per tau: %s" % ", ".join(
        "%d: %d" % (tau, rec["per_tau"][tau]) for tau in pfair.GATED_TAUS),
        "", "Sample (%d, T0 order): %s" % (len(v2["sample"]),
                                            ", ".join(str(t) for t in v2["sample"]))]

    out += ["", "## V7 — the pre-registered prediction, no threshold", "",
            "| tau | predicted | `lambda_hat` | difference (`lambda_hat` - predicted) |",
            "|---|---|---|---|"]
    for tau in pfair.GATED_TAUS:
        row = doc["V7_prediction"][tau]
        out.append("| %d | %s | %.4f | %+.4f |" % (tau, row["predicted"], row["lambda_hat"],
                                                   row["difference"]))

    m1, guard = doc["V8_dispersion"], doc["V8_slice_guard"]
    out += ["", "## V8 — `Lambda` out of sample, no threshold", "",
            "| tau | anchors/member | possible | taken | dropped | `Lambda_oos` | `SD_SCALE` | "
            "`Lambda_oos / SD_SCALE` | pooled mean of `r` | median member RMS | "
            "checkpoint-only RMS |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        row = m1["per_tau"][tau]
        out.append("| %d | %d | %d | %d | %d | %.6f | %s | %.6f | %+.6f | %.6f | %.6f |" % (
            tau, row["anchors_per_member"], row["anchors_possible"], row["anchors_taken"],
            row["anchors_dropped"], row["lambda"], m1["SD_SCALE"][tau],
            m1["lambda_over_SD_SCALE"][tau], row["pooled_mean_of_r"],
            row["median_member_rms"], row["checkpoint_only_rms"]))
    out += ["", "Anchors taken %d, dropped %d, by %d members: %s" % (
        m1["anchors_taken_total"], m1["anchors_dropped_total"],
        m1["members_contributing_a_dropped_anchor"],
        ", ".join(str(t) for t in m1["their_T0s"]) or "none"),
        "Slice guard: %d members, %d anchors priced twice, %d identical to the whole stream" % (
            guard["members"], guard["anchors_priced_twice"],
            guard["identical_to_the_whole_stream"])]

    out += ["", "## V9 — tails and robust scale, no threshold", "",
            "| tau | `Lambda_oos` | `P(|r| > Lambda)` | normal | `P(|r| > 2 Lambda)` | normal | "
            "`P(|r| > 3 Lambda)` | normal | `MAD/0.674490` | / `Lambda` | `IQR/1.348980` | "
            "/ `Lambda` |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for tau in pfair.TAUS:
        row = m1["per_tau"][tau]
        tails, normal = row["tail_fractions"], row["normal_tail_fractions"]
        out.append("| %d | %.6f | %.4f | %s | %.4f | %s | %.4f | %s | %.6f | %.4f | %.6f | "
                   "%.4f |" % (
                       tau, row["lambda"], tails[1], normal[1], tails[2], normal[2], tails[3],
                       normal[3], row["mad_over_0_674490"],
                       row["mad_over_0_674490"] / row["lambda"], row["iqr_over_1_348980"],
                       row["iqr_over_1_348980"] / row["lambda"]))

    f = doc["observations_file"]
    out += ["", "## Observations file", "",
            "%d lines · %d bytes · SHA-256 `%s`" % (f["lines"], f["bytes"], f["sha256"])]
    return "\n".join(out) + "\n"


def main(argv):
    if argv[1:2] != ["--out"] or len(argv) != 3:
        sys.stderr.write("usage: python3 -B tz08a-out-of-sample.py --out <directory>\n")
        return 2
    target = argv[2]
    doc, csv = build()
    outputs = {"tz08a-results.json": json.dumps(doc, sort_keys=True, indent=2, default=str) + "\n",
               "tz08a-tables.md": tables(doc),
               "tz08a-observations.csv": csv}
    for name, text in outputs.items():
        with open(os.path.join(target, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
