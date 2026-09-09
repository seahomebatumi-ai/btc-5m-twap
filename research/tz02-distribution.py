#!/usr/bin/env python3
"""TZ-02 - divergence distribution and opportunity rate.

Aggregates the TZ-01a observation set. Defines no new quantity: D = p_twap - p_naive
for each sigma variant, everything else is a count over that.

Reads  research/out/twap-divergence-observations.parquet
Writes research/out/tz02-summary.md  (or the path given as argv[1])
"""

import hashlib
import json
import sys
from collections import Counter

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

PARQUET = "research/out/twap-divergence-observations.parquet"
COLLECTOR = "research/twap-divergence.py"
COLLECTOR_SHA_TZ01A = "6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473"

TAUS = [240, 180, 120, 90, 60]
GATE_TAUS = [60, 90, 120, 180]
THRESHOLDS = [0.03, 0.05, 0.10, 0.15, 0.20, 0.30]
VARIANTS = ["pre", "live"]
DAYS = 730.0
WALL_LO, WALL_HI = 0.05, 0.95
GATE_T = 0.05
GATE_MIN_PER_DAY = 5.0

# Histogram: 200 buckets of width 0.01 spanning [-1.00, +1.00].
N_BUCKETS = 200


def bucket_edges(i):
    return (-1.00 + 0.01 * i, -1.00 + 0.01 * (i + 1))


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load():
    cols = ["interval_open_ts", "tau", "outcome_1s",
            "p_twap_pre", "p_naive_pre", "p_twap_live", "p_naive_live"]
    df = pq.read_table(PARQUET, columns=cols).to_pandas()
    for v in VARIANTS:
        df["D_" + v] = df["p_twap_" + v] - df["p_naive_" + v]
        df["trade_" + v] = (
            df["p_twap_" + v].between(WALL_LO, WALL_HI)
            & df["p_naive_" + v].between(WALL_LO, WALL_HI)
        )
    return df


def fmt_pct(x):
    return f"{100.0 * x:.3f}%"


def table(rows, header):
    out = ["| " + " | ".join(header) + " |",
           "|" + "|".join("---" for _ in header) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "research/out/tz02-summary.md"
    df = load()
    n_all = len(df)
    n_intervals = df["interval_open_ts"].nunique()
    L = []
    W = L.append

    checks = {}

    W("# TZ-02 - divergence distribution, generated tables\n")
    W(f"Observations: {n_all:,}. Intervals: {n_intervals:,}. Window: {DAYS:.0f} days.\n")
    W(f"`D = p_twap - p_naive`, per sigma variant. Tradeable = both `p_twap` and "
      f"`p_naive` in [{WALL_LO}, {WALL_HI}].\n")

    # ---------------------------------------------------------------- check 5
    collector_sha = sha256_file(COLLECTOR)
    checks["collector_sha_matches"] = int(collector_sha == COLLECTOR_SHA_TZ01A)
    W("## Check 6.5 - collector unmodified\n")
    W(table([["TZ-01a report", f"`{COLLECTOR_SHA_TZ01A}`"],
             ["this run", f"`{collector_sha}`"],
             ["equal", collector_sha == COLLECTOR_SHA_TZ01A]],
            ["source", "sha256 of research/twap-divergence.py"]))
    W("")

    # ---------------------------------------------------------------- check 3
    # TZ-01a Gate A: inversions at tau in {120, 180}.
    W("## Check 6.3 - reconciliation with TZ-01a Gate A\n")
    recon_rows = []
    recon = {}
    for v in VARIANTS:
        pt, pn = df["p_twap_" + v], df["p_naive_" + v]
        inv = ((pn >= 0.85) & (pt <= 0.60)) | ((pn <= 0.15) & (pt >= 0.40))
        sub = inv & df["tau"].isin([120, 180])
        recon["sigma_" + v] = int(sub.sum())
        for tau in [120, 180]:
            recon_rows.append([f"sigma_{v}", tau, int((inv & (df["tau"] == tau)).sum())])
        recon_rows.append([f"sigma_{v}", "120+180", f"**{int(sub.sum())}**"])
    expected = {"sigma_pre": 86, "sigma_live": 137}
    checks["reconciliation"] = int(recon == expected)
    W(table(recon_rows, ["variant", "tau", "inversions"]))
    W(f"\nExpected from TZ-01a: {expected}. Reproduced: {recon}. "
      f"Match: {recon == expected}\n")
    assert recon == expected, f"reconciliation failed: {recon} != {expected}"

    # ------------------------------------------------------- measurement 1
    W("## Measurement 1 - sign split of D\n")
    for v in VARIANTS:
        rows = []
        d = df["D_" + v]
        for tau in TAUS:
            m = df["tau"] == tau
            n = int(m.sum())
            pos = int((m & (d > 0)).sum())
            neg = int((m & (d < 0)).sum())
            zero = n - pos - neg
            rows.append([tau, f"{n:,}", f"{pos:,}", fmt_pct(pos / n),
                         f"{neg:,}", fmt_pct(neg / n), f"{zero:,}",
                         f"{pos / neg:.3f}" if neg else "-"])
        pos = int((d > 0).sum()); neg = int((d < 0).sum()); zero = n_all - pos - neg
        rows.append(["**all**", f"{n_all:,}", f"**{pos:,}**", fmt_pct(pos / n_all),
                     f"**{neg:,}**", fmt_pct(neg / n_all), f"{zero:,}",
                     f"{pos / neg:.3f}" if neg else "-"])
        W(f"### `sigma_{v}`\n")
        W(table(rows, ["tau", "observations", "D > 0", "share", "D < 0", "share",
                       "D = 0", "pos/neg"]))
        W("")

    # ------------------------------------------------------- measurement 2
    W("## Measurement 2 - two-sided histogram of D, 0.01 buckets over [-1.00, +1.00]\n")
    conservation = []
    for v in VARIANTS:
        d = df["D_" + v].to_numpy()
        idx_all = np.floor((d + 1.0) * 100.0).astype(np.int64)
        out_of_range = int(((idx_all < 0) | (idx_all > N_BUCKETS)).sum())
        # D = +1.00 exactly lands on index 200; it belongs to the closed top bucket.
        idx_all = np.clip(idx_all, 0, N_BUCKETS - 1)
        cols = {}
        for tau in TAUS:
            m = (df["tau"] == tau).to_numpy()
            cols[tau] = np.bincount(idx_all[m], minlength=N_BUCKETS)
        total = np.bincount(idx_all, minlength=N_BUCKETS)
        rows = []
        for i in range(N_BUCKETS):
            if total[i] == 0:
                continue
            lo, hi = bucket_edges(i)
            rows.append([f"[{lo:+.2f}, {hi:+.2f})"] +
                        [f"{int(cols[tau][i]):,}" for tau in TAUS] +
                        [f"{int(total[i]):,}"])
        W(f"### `sigma_{v}`\n")
        W(f"Non-empty buckets: {len(rows)} of {N_BUCKETS}. "
          f"Observations outside [-1.00, +1.00]: {out_of_range}.\n")
        W(table(rows, ["bucket"] + [f"tau {t}" for t in TAUS] + ["all tau"]))
        W("")
        for tau in TAUS:
            n = int((df["tau"] == tau).sum())
            conservation.append([f"sigma_{v}", tau, f"{int(cols[tau].sum()):,}",
                                 f"{n:,}", int(cols[tau].sum()) == n])
        conservation.append([f"sigma_{v}", "all", f"{int(total.sum()):,}",
                             f"{n_all:,}", int(total.sum()) == n_all])
    checks["row_conservation"] = sum(1 for r in conservation if r[4])
    checks["row_conservation_total"] = len(conservation)
    W("### Check 6.2 - row conservation\n")
    W(table(conservation, ["variant", "tau", "sum of bucket counts",
                           "observation count", "equal"]))
    W("")
    assert all(r[4] for r in conservation), "row conservation failed"

    # ------------------------------------------- measurements 3, 4 and 5
    mono_checks = []

    def threshold_block(v, restrict_tradeable):
        d = df["D_" + v]
        keep = df["trade_" + v] if restrict_tradeable else pd.Series(True, index=df.index)
        rows = []
        prev = {}
        for tau in TAUS:
            m = df["tau"] == tau
            n_tau = int(m.sum())
            n_sub = int((m & keep).sum())
            for T in THRESHOLDS:
                for sign, sel in (("D >= +T", d >= T), ("D <= -T", d <= -T)):
                    c = int((m & keep & sel).sum())
                    denom = n_sub if restrict_tradeable else n_tau
                    rows.append([tau, f"{n_sub:,}" if restrict_tradeable else f"{n_tau:,}",
                                 f"{T:.2f}", sign, f"{c:,}",
                                 fmt_pct(c / denom) if denom else "-",
                                 fmt_pct(c / n_tau),
                                 f"{c / DAYS:.3f}"])
                    k = (tau, sign)
                    if k in prev:
                        mono_checks.append(prev[k] >= c)
                    prev[k] = c
        return rows

    hdr3 = ["tau", "observations", "T", "direction", "count", "% of tau obs",
            "% of all tau obs", "events/day"]
    hdr4 = ["tau", "tradeable obs", "T", "direction", "count", "% of tradeable",
            "% of all tau obs", "events/day"]

    W("## Measurement 3 - threshold table, all observations\n")
    for v in VARIANTS:
        W(f"### `sigma_{v}`\n")
        W(table(threshold_block(v, False), hdr3))
        W("")

    W("## Measurement 4 - threshold table, tradeable subset "
      f"(both p in [{WALL_LO}, {WALL_HI}])\n")
    for v in VARIANTS:
        n_sub = int(df["trade_" + v].sum())
        W(f"### `sigma_{v}` - tradeable observations: {n_sub:,} "
          f"({fmt_pct(n_sub / n_all)} of all)\n")
        W(table(threshold_block(v, True), hdr4))
        W("")

    checks["monotonicity"] = sum(1 for x in mono_checks if x)
    checks["monotonicity_total"] = len(mono_checks)
    assert all(mono_checks), "threshold monotonicity failed"

    # ------------------------------------------------------- measurement 5
    W("## Measurement 5 - calibration inside the divergence bands "
      "(tradeable subset, label `outcome_1s`)\n")
    for v in VARIANTS:
        d = df["D_" + v]
        keep = df["trade_" + v]
        rows = []
        for tau in TAUS:
            m = df["tau"] == tau
            for T in THRESHOLDS:
                for sign, sel in (("D >= +T", d >= T), ("D <= -T", d <= -T)):
                    band = m & keep & sel
                    c = int(band.sum())
                    if c == 0:
                        rows.append([tau, f"{T:.2f}", sign, "0", "-", "-", "-", "-", "-"])
                        continue
                    sub = df[band]
                    realised = float(sub["outcome_1s"].mean())
                    mt = float(sub["p_twap_" + v].mean())
                    mn = float(sub["p_naive_" + v].mean())
                    rows.append([tau, f"{T:.2f}", sign, f"{c:,}",
                                 f"{mt:.4f}", f"{mn:.4f}", f"{realised:.4f}",
                                 f"{abs(realised - mt):.4f}", f"{abs(realised - mn):.4f}"])
        W(f"### `sigma_{v}`\n")
        W(table(rows, ["tau", "T", "direction", "count", "mean p_twap", "mean p_naive",
                       "realised outcome_1s", "|realised - p_twap|",
                       "|realised - p_naive|"]))
        W("")

    # ------------------------------------------------------- measurement 6
    W(f"## Measurement 6 - overlap within an interval, measurement 4 at T = {GATE_T:.2f}\n")
    overlap_summary = {}
    for v in VARIANTS:
        qual = df["trade_" + v] & (df["D_" + v].abs() >= GATE_T)
        for label, taus in (("all five checkpoints", TAUS),
                            ("gate checkpoints {60, 90, 120, 180}", GATE_TAUS)):
            sel = qual & df["tau"].isin(taus)
            per_iv = df.loc[sel, "interval_open_ts"].value_counts()
            hist = Counter(per_iv.values.tolist())
            n_iv_any = int(len(per_iv))
            n_obs = int(sel.sum())
            n_iv_multi = int(sum(c for k, c in hist.items() if k > 1))
            n_obs_multi = int(sum(k * c for k, c in hist.items() if k > 1))
            rows = [[k, f"{hist.get(k, 0):,}", f"{k * hist.get(k, 0):,}"]
                    for k in sorted(hist)]
            W(f"### `sigma_{v}`, {label}\n")
            W(table(rows, ["qualifying checkpoints in the interval", "intervals",
                           "observations"]))
            W(f"\nQualifying observations: {n_obs:,}. Distinct intervals: {n_iv_any:,}. "
              f"Intervals with more than one qualifying checkpoint: {n_iv_multi:,}. "
              f"Observations sitting in those intervals: {n_obs_multi:,}. "
              f"Redundant observations removed by de-duplication: {n_obs - n_iv_any:,}.\n")
            overlap_summary[(v, label)] = dict(
                observations=n_obs, intervals=n_iv_any, intervals_multi=n_iv_multi,
                observations_multi=n_obs_multi, removed=n_obs - n_iv_any)

    # ------------------------------------------------------------ Gate A2
    W("## Gate A2\n")
    gate_rows = []
    gate_numbers = {}
    for v in VARIANTS:
        qual = df["trade_" + v] & df["tau"].isin(GATE_TAUS)
        d = df["D_" + v]
        for label, sel in (("either direction", qual & (d.abs() >= GATE_T)),
                           ("D >= +0.05 only", qual & (d >= GATE_T)),
                           ("D <= -0.05 only", qual & (d <= -GATE_T))):
            n_obs = int(sel.sum())
            n_iv = int(df.loc[sel, "interval_open_ts"].nunique())
            gate_rows.append([f"sigma_{v}", label, f"{n_obs:,}", f"{n_obs / DAYS:.3f}",
                              f"{n_iv:,}", f"**{n_iv / DAYS:.3f}**"])
            gate_numbers[(v, label)] = n_iv / DAYS
    W(table(gate_rows, ["variant", "direction", "qualifying observations",
                        "obs/day before de-dup", "distinct intervals",
                        "events/day after de-dup"]))
    deciding = max(gate_numbers[(v, "either direction")] for v in VARIANTS)
    best = max(VARIANTS, key=lambda v: gate_numbers[(v, "either direction")])
    verdict = "PASS" if deciding >= GATE_MIN_PER_DAY else "FAIL"
    W(f"\nDeciding number (best variant `sigma_{best}`, either direction, "
      f"de-duplicated per interval): **{deciding:.3f}** events per day "
      f"against the pre-committed **{GATE_MIN_PER_DAY:.1f}**. Verdict: **{verdict}**.\n")

    # -------------------------------------------------------------- checks
    W("## Check counts\n")
    W(table([[k, v] for k, v in checks.items()], ["check", "count"]))
    W("")

    text = "\n".join(L) + "\n"
    with open(out_path, "w") as fh:
        fh.write(text)

    summary = dict(observations=n_all, intervals=n_intervals, checks=checks,
                   reconciliation=recon,
                   gate={f"{v}|{lbl}": round(val, 6)
                         for (v, lbl), val in gate_numbers.items()},
                   deciding=round(deciding, 6), verdict=verdict,
                   collector_sha256=collector_sha)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
