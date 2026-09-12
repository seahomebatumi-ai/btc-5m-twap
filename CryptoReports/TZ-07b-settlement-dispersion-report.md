# TZ-07b — the dispersion of the settlement quantity, measured directly, and the scale frozen from it

**Executor report.** Executed on the capture host (Vultr VPS, Warsaw) on 2026-09-12, model
**Opus**, as the TZ requires. Scratch and outputs in `/root/tz07b-work/`, outside the
repository.

---

## 0. Fingerprint

### 0.1 The anchors read from `SYSTEM-MAP.md` on `origin/main`

| anchor | required by the TZ | read from the map | match |
|---|---|---|---|
| System Map revision | `2026-09-13-a` | `2026-09-13-a` | yes |
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` | yes |
| `A2` — collector | `6c5089330629` | `6c5089330629` | yes |
| `A3` — phase | `0-complete / 1-open / 2-not-started` | `0-complete / 1-open / 2-not-started` | yes |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` | yes |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` | yes |
| `A6` — pricer | `9bd4213a60a3` | `9bd4213a60a3` | yes |

Read at `origin/main` = `cd2d1d4`, in a worktree outside the primary working tree. **The
fingerprint gate passes.**

### 0.2 Every file the map's §0 table lists, before any work

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 364 | 33,309 | reported | `09f71ca07e1b2329f21bccd1523ed4607b122af5c54a2ba20e83fb3239fb9dac` | self-reference |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | yes |
| `research/pfair.py` | 275 | 12,150 | frozen | `9bd4213a60a3a25657d5ab8e507f7fc2205147b15e676cf47544a8bea8c7a8c1` | yes |
| `research/selftest-pfair.py` | 327 | 17,060 | frozen | `ea3750df706d4375f42cb42f9d06e73268225f1eb79e216185329ca169d73da6` | yes |
| `research/tz06-calibration.py` | 569 | 26,548 | frozen | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` | yes |
| `research/tz07a-variance-time.py` | 636 | 29,039 | frozen | `18c259523ee0b7ca60ec70dd6a5cbe401a2bb71420ccdfa1f0ff517c9e242cb4` | yes |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | yes |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | yes |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | yes |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | yes |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | yes |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | yes |

**Every frozen row matched before any work began.**

### 0.3 After the change — the three files §6 authorizes, and the one file §4 adds

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `research/pfair.py` | 281 | 12,499 | `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` |
| `research/selftest-pfair.py` | 306 | 15,647 | `97de9782d319c82ee6a7d81ddbd8e00d590d85ffe2daa41abe3d71ae92712c94` |
| `research/tz07a-variance-time.py` | 619 | 28,219 | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` |
| `research/tz07b-settlement-dispersion.py` (new) | 515 | 24,926 | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` |

`research/tz06-calibration.py` is **unmodified** and still hashes to
`a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123`, read back by V4 from the
file it ran. No other frozen row moved; §3 of this report's Publication section proves the
branch carries exactly these four paths and nothing else.

### 0.4 The host gate

| check | required | observed | verdict |
|---|---|---|---|
| `/var/lib/btc-recorder/` | exists, holds interval directories | exists; **721** interval directories under `btc-updown-5m/` when the gate was read, 723 at the close of the run | pass |
| the recorder process | running, newest `runtime.jsonl` start record carries sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | running, pid **228592**; newest start record `{"kind": "recorder", "recv_ns": 1789206785264516934, "sha": "4216c04673ced76b5b2ac60ef57c9abedc46f9b9"}` | pass |
| the filesystem holding that path | device `/dev/vda2`, total exactly `31,612,203,008` bytes | `/dev/vda2`, `31612203008` bytes | pass |

**The host gate passes.** This is the capture host.

The recorder's working directory is the primary working tree
(`/root/btc-5m-twap/research/recorder`), so no branch was ever checked out there. Every step of
this execution ran in `git worktree`s under `/root/tz07b-work/`, and Tier A and Tier C were not
interrupted at any point.

---

## 1. Input

**Nothing was re-collected.** Every byte read was already on disk, written by the running
recorder. Nothing under `/var/lib/btc-recorder/` was written, moved or deleted.

| read | what | how |
|---|---|---|
| `manifest.json` | every interval directory's manifest | `analyze.load_manifests` |
| `chainlink.jsonl.gz` | each member's and each member's predecessor's oracle stream | `pfair.merged_stream` → `analyze.reports` |
| `twap60.jsonl.gz` | `K` for the V2 causality test only | `pfair.reports` |

**What was not read, by this TZ's §2.**

- **No outcome.** The new instrument opens no `resolution.json`, reads no `priceToBeat`, no
  resolved field, and constructs no label. `Y(a, tau)` is a functional of the oracle feed
  alone. No `Brier`, no bin table, no `λ̂` and no calibration statistic of any kind appears
  anywhere in this report — including in-sample ones labelled as such.
- **No order book.** The per-interval order-book capture is never opened, and the string §2
  forbids in the new file does not occur in `research/tz07b-settlement-dispersion.py` — a
  case-insensitive `grep -c` over it returns `0`.

The two regression subprocesses V4 requires are the exception the TZ itself mandates, and are
named plainly in §6 below.

---

## 2. Measurements

### 2.1 The set — §3

Re-derived by calling `tz06-calibration.scoring_set`, never transcribed.

| quantity | value |
|---|---|
| source | TZ-06 §4's five qualifying conditions, re-derived |
| units considered | **443** |
| members | **400** |
| first member `T0` | `1789035000` |
| last member `T0` | `1789166400` |
| **SHA-256 of the member list** | **`6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9`** |

The hashed form is **the sorted member `T0` list as decimal ASCII, joined by `\n`, with no
trailing newline**. Stated exactly so a later TZ can reproduce the value rather than guess the
encoding.

Fewer or more than 400 members is BLOCKED by assert inside the instrument; 400 were found.

### 2.2 M1 — the dispersion of the settlement quantity, V1

For each member: the merged `chainlink` step function, its one-second grid over
`[T0 - 300, T0 + 300]` — 601 points — and at each tau every integer anchor `a` with
`[a, a + tau]` inside that window. `sigma(tau)` is `pfair.realised_sigma` over the causal
window `[T0 - 300, T0 + (300 - tau)]`, the same `sigma_live` the pricer reads at that
checkpoint. `Λ(tau)` is the **raw, uncentred** root mean square of
`r = Y / (sigma * sqrt(H(tau)))`.

| `tau` | anchors/member | **taken** | dropped | possible | **`Λ(tau)`** | pooled mean of `r` | median member RMS | checkpoint-only RMS | `MAD/0.674490` | `IQR/1.348980` |
|---|---|---|---|---|---|---|---|---|---|---|
| 240 | 361 | 143,255 | 1,145 | 144,400 | **1.523760** | −0.131662 | 1.252129 | 1.818385 | 1.455760 | 1.461092 |
| 180 | 421 | 167,255 | 1,145 | 168,400 | **1.496023** | −0.099232 | 1.306113 | 1.752435 | 1.447335 | 1.448217 |
| 120 | 481 | 191,343 | 1,057 | 192,400 | **1.496277** | −0.075602 | 1.397806 | 1.728420 | 1.416085 | 1.414347 |
| 90 | 511 | 203,416 | 984 | 204,400 | **1.479154** | −0.055935 | 1.422683 | 1.537139 | 1.346664 | 1.344432 |
| 60 | 541 | 215,620 | 780 | 216,400 | **1.444658** | −0.040913 | 1.408067 | 1.649524 | 1.249064 | 1.249131 |
| 30 | 571 | 227,920 | 480 | 228,400 | **1.385806** | −0.023339 | 1.371009 | 1.443690 | 1.049153 | 1.050023 |
| 10 | 591 | 236,125 | 275 | 236,400 | **1.211176** | −0.012918 | 1.207897 | 1.264237 | 0.622386 | 0.622153 |

**Totals: 1,384,934 anchors taken, 5,866 dropped, of 1,390,800 possible.** The
checkpoint-only column is computed from the single anchor `a = 300 - tau`, and at every tau
all **400** members contributed that anchor.

**None of these columns carries a threshold.** The bolded column is the one §5 freezes; every
other column is a diagnostic the TZ asked to exist so that a later finding about shape rather
than scale already has its data.

#### The empirical tails against the normal's

| `tau` | `P(|r| > Λ)` | normal | `P(|r| > 2Λ)` | normal | `P(|r| > 3Λ)` | normal |
|---|---|---|---|---|---|---|
| 240 | 0.2946 | 0.3173 | 0.0424 | 0.0455 | 0.0055 | 0.0027 |
| 180 | 0.3007 | 0.3173 | 0.0450 | 0.0455 | 0.0059 | 0.0027 |
| 120 | 0.3045 | 0.3173 | 0.0475 | 0.0455 | 0.0050 | 0.0027 |
| 90 | 0.2959 | 0.3173 | 0.0502 | 0.0455 | 0.0055 | 0.0027 |
| 60 | 0.2834 | 0.3173 | 0.0540 | 0.0455 | 0.0076 | 0.0027 |
| 30 | 0.2551 | 0.3173 | 0.0579 | 0.0455 | 0.0119 | 0.0027 |
| 10 | 0.2048 | 0.3173 | 0.0590 | 0.0455 | 0.0190 | 0.0027 |

Reported and not interpreted, as the TZ requires. Two features are stated as measured and
nothing is concluded from them here. The centre is lighter than the normal's and the far tail
heavier, at every tau, and the gap widens monotonically as `tau` falls — at `tau = 10` the
three-sigma fraction is seven times the normal's while the one-sigma fraction is two thirds of
it. And the robust readings agree with each other to the third decimal at every tau
(`MAD/0.674490` against `IQR/1.348980`) while both sit below `Λ`, by 4% at `tau = 240` and by
49% at `tau = 10`. The TZ fixed the estimator before the numbers existed and this report does
not revisit that choice; it records that the data to see a shape question already exists.

#### The disconnect rule, imported

The drops above are TZ-07a M6's rule, imported from `research/tz07a-variance-time.py` by
`importlib` and not reimplemented: an anchor is dropped when any second of `[a, a + tau]` lies
inside a disconnect recorded by the member's own or its predecessor's manifest.

**15 members** contributed at least one dropped anchor — `1789035900`, `1789043100`,
`1789050300`, `1789057500`, `1789064700`, `1789071900`, `1789073100`, `1789080300`,
`1789102500`, `1789128300`, `1789131600`, `1789138800`, `1789141800`, `1789149000`,
`1789162500`. These are exactly the fifteen TZ-07a §2.2 named, and the per-tau drop counts at
`tau` 240, 180, 60, 30 and 10 — 1,145 / 1,145 / 780 / 480 / 275 — are identical to TZ-07a's
per-lag drops at `h` 240, 180, 60, 30 and 10, because an anchor's closed span and an
increment's closed span are the same interval. The rule is the same rule, and the counts show
it.

### 2.3 M2 — the freeze, §5

Written into `research/pfair.py` as literals, to six significant digits, exactly as M1's `Λ`
column reads them:

```python
SD_SCALE = {240: D("1.52376"), 180: D("1.49602"), 120: D("1.49628"), 90: D("1.47915"),
            60: D("1.44466"), 30: D("1.38581"), 10: D("1.21118")}


def corrected_sd(tau, sigma):
    assert tau in SD_SCALE, "tau = %s has no measured scale; TZ-07b measured %s" % (
        tau, sorted(SD_SCALE))
    if tau < SETTLEMENT_S:
        h = D(tau) ** 3 / D(TAU_CUBED_DIVISOR)
    else:
        h = D(tau - 40)
    return SD_SCALE[tau] * sigma * h.sqrt()
```

`G_RATIO` and the previous body of `corrected_sd` are **removed, not kept alongside**.
`c44af68` holds them in history. A `tau` with no measured scale raises; nothing is
extrapolated.

| `tau` | `H(tau)` | `sqrt(H(tau))` | `SD_SCALE[tau]` | `corrected_sd / sigma` |
|---|---|---|---|---|
| 240 | 200 | 14.142136 | `1.52376` | 21.549221 |
| 180 | 140 | 11.832160 | `1.49602` | 17.701147 |
| 120 | 80 | 8.944272 | `1.49628` | 13.383135 |
| 90 | 50 | 7.071068 | `1.47915` | 10.459170 |
| 60 | 20 | 4.472136 | `1.44466` | 6.460716 |
| 30 | 2.5 | 1.581139 | `1.38581` | 2.191158 |
| 10 | 0.0925925… | 0.304290 | `1.21118` | 0.368550 |

The instrument asserts, per tau and **before it prints anything**, that the literal in
`pfair.py` equals its own measurement rounded to six significant digits, and aborts if it does
not. Seven of seven matched on the run that produced this report.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-07b-settlement-dispersion`, cut from `main` at `cd2d1d4` |
| implementation commit | `26bbb61aed774a88355dd5204d8b69fda9135a68` |
| pull request | **[#8](https://github.com/seahomebatumi-ai/btc-5m-twap/pull/8)** |
| files on the branch | `research/tz07b-settlement-dispersion.py` (new), `research/pfair.py`, `research/selftest-pfair.py`, `research/tz07a-variance-time.py` |
| Release tag / asset | **none.** This TZ produces no artifact over ~1 MB and requires none. |
| report | this file, straight to `main` |

No dataset, archive or binary entered git history.

### 3.1 The §4.2 separation self-check, verbatim

```
$ git rev-list origin/main | grep -c 26bbb61aed774a88355dd5204d8b69fda9135a68
0

$ git diff --name-only origin/main origin/tz-07b-settlement-dispersion
research/pfair.py
research/selftest-pfair.py
research/tz07a-variance-time.py
research/tz07b-settlement-dispersion.py

$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
(no output)
```

The first line prints `0`: the implementation is not on `main`. **Merge is deployment, only the
Boss merges, and only after the Architect's verdict.**

---

## 4. Gate

**TZ-07b sets no gate of its own, and moves nothing in the one that exists.**

The TZ's §8 states that TZ-07a §8 stands verbatim, that this TZ moves nothing in it — not the
set rule, not the scored taus, not G1, not G2, not G3's tolerance — and that it is
**deliberately not restated**, because a gate restated is a gate that can drift. This report
honours that: the gate is not quoted, not paraphrased and not summarised here. It is committed
in `CryptoTZ/TZ-07a-variance-time.md` on `main`, where TZ-08 will read it.

The single thing this TZ changes is **which estimator TZ-08 scores**: the `SD_SCALE` constants
§5 freezes, not `G_RATIO`.

What this TZ does have is a pass condition, and it is not a threshold: **V1, V2, V3 or V4
failing is BLOCKED, not a finding.** None failed. Every one of the six checks is a count
derived from the run, and each count is in §5 below.

**TZ-08's trigger, from V6 and from nothing else:** TZ-08 is issued when 400 intervals with
`T0 > 1789166400` qualify. At the moment of this run **253** qualify, of 280 directories on
disk — **147 short**. TZ-08 is not issued, and this report does not issue it.

---

## 5. Validation

Every check below is an `assert` inside the script that produces the numbers, and aborts the
run when it is false. Where something is recorded and not asserted, it says so.

### V1 — the dispersion — **asserted**

The full table is §2.2. **1,384,934 anchors taken, 5,866 dropped, of 1,390,800 possible**, over
400 members at seven taus, with every diagnostic §4 lists and none of them carrying a
threshold.

Asserts that abort the run: the grid is 601 points and has no hole at `T0 - 300` for every
member; `sigma(tau)` is strictly positive for every member and tau, so there is a scale to
divide by; every admissible anchor produced a mean; and no tau finished with zero anchors.

**The V1 guard — asserted, 175 of 175.** M1 takes 1.39 million time-weighted means, and each
would otherwise rescan a stream of about 1,200 reports. The window is therefore `bisect`ed
before the call, so `pfair.time_weighted_mean` is handed the reports it would have read out of
the whole stream and no others — an argument narrowed, not a formula rewritten. Because an
argument narrowed wrongly is a silent wrong answer, the equality is asserted rather than
argued: on the first member, at every tau, 25 anchors spread across the grid are priced twice,
once through the bounded slice and once through the whole merged stream, and required to agree
exactly. **175 of 175 identical.** This guard is the Executor's, not the Architect's; it guards
an implementation decision, it is not a validation check the TZ asked for, and it is named here
and in §6 for that reason.

### V2 — causality of the corrected pricer — **asserted by count, 120 of 120 and 120 of 120**

The first 20 members × the six gated taus, run through TZ-07a's own V2 instrument against the
newly corrected pricer. Perturbation, never truncation.

| quantity | count |
|---|---|
| comparisons | **120** |
| bit-identical `state`, `sd` and `p_fair` under perturbation of **every** `chainlink` and `twap60` report after the checkpoint instant, factor `1.0001` | **120 of 120** |
| leaks | **0** |
| negative control on the last readable report moved the model output taken as a whole | **120 of 120** |
| — of which it moved `p_fair` alone | 113 |
| saturated observations (`p_fair` exactly 0.0 or 1.0 as a double) | 7 |

The control is judged on `state`, `sd` and `p_fair` together, which is what the TZ names.
`Phi` saturates at live scale, so a control judged on `p_fair` alone would under-count a reader
that is genuinely read: 7 saturated observations account for the whole of the gap between 120
and 113, and the two figures reconcile exactly.

### V3 — determinism — **asserted by `cmp`, two runs byte-identical**

```
run 1 start 2026-09-12T21:57:26Z   exit 0   end 2026-09-12T21:59:01Z
run 2 start 2026-09-12T21:59:01Z   exit 0   end 2026-09-12T22:00:39Z
cmp run-1.json run-2.json          IDENTICAL
7f661c78cbeee11eb3cb62e1d9038d2772d7d66c479cc1d75d38077f617a7185  run-1.json
7f661c78cbeee11eb3cb62e1d9038d2772d7d66c479cc1d75d38077f617a7185  run-2.json
```

A third, earlier full run — made before the two above, on the same code — is byte-identical to
both; `cmp` confirms it. The recorder wrote two further interval directories during the window
(721 at the start of the work, 723 at the end) and the artifact did not move, which is the
point of the next paragraph.

**The compared artifact is a pure function of the closed 400-member set.** It carries no count
of anything still growing: **V6 is a separate invocation (`--v6`) and is not part of it**, and
the two regression blocks record only the counts V4 compares, never a directory listing.

### V4 — regression, two files — **asserted, 6 of 6 · P 397 · 15 of 15**

**`research/tz06-calibration.py`, unmodified.** Run as a subprocess from the file on the
branch, which still hashes to
`a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` — the map's frozen value.
Exit status `0`.

| quantity | expected | observed |
|---|---|---|
| TZ-06 §2.8's `Brier(p_fair)` values reproduced **to all six decimals** | 6 | **6 of 6** |
| P, the reconstructed close TWAP agreeing in sign with the venue | 397 | **397** of 400 |

The six values themselves are deliberately **not printed here**: §2 of this TZ forbids a
calibration statistic anywhere in this report, so V4 is carried out as a count of exact
matches. The comparison itself is against TZ-06's published values, made inside the script, and
a mismatch would have been visible as a count below six.

**`research/tz07a-variance-time.py`, with only §6.3's removal applied.** Run as a subprocess.
Exit status `0` — the removal cost nothing and the file still runs with `G_RATIO` gone from the
pricer.

| quantity | expected | observed |
|---|---|---|
| TZ-07a §2.1's fifteen pooled `g(h)`, at six significant digits | 15 | **15 of 15** |

All fifteen lags `1, 2, 5, 10, 20, 30, 50, 60, 80, 100, 140, 180, 200, 240, 300` reproduce.

### V5 — self-tests — **asserted, 104 of 104**

`selftest-pfair.py` passes whole; exit status `0`.

| family | count | expected |
|---|---|---|
| `v5_*` — the TZ-06 §6 model checks | **56** | 56, unchanged |
| `section 3 machinery` | **18** | 18, unchanged |
| `tz07b_*` — new, counted on its own | **30** | — |
| **total** | **104 of 104** | |

**Deleted by name, and for one reason only.** The four checks below encode the superseded
composition. §6.2 authorizes their deletion **because the specification they encode is
superseded, and for no other reason. No test was deleted or edited because it failed** — all
four were passing against the old constants when this run began.

- `tz07a_the_near_branch_is_untouched`
- `tz07a_the_correction_at_the_boundary`
- `tz07a_the_correction_on_the_far_branch`
- `tz07a_the_table_is_a_table_of_literals`

That the four are gone is not asserted from the test output but from the file's own source: the
instrument reads `selftest-pfair.py` and aborts if any of the four names still occurs in it.
**0 of 4 still present.**

**The `tz07b_*` family that replaces them**, 30 checks in four groups, every fixed expectation
at `K = 100000.25`, `S_T = 100037.52`, `M_R = 99987.12` and `sigma = 3.25` — live scale, never
zero:

| group | what it asserts | §6.2 item |
|---|---|---|
| `tz07b_the_table_is_a_table_of_literals` | `sorted(SD_SCALE) == sorted(pfair.TAUS)`, `10` included; every value a `Decimal`; every value exactly six significant digits; an unmeasured `tau` raises | 1, 2, 7 |
| `tz07b_the_horizon_at_the_boundary` | `H(60)` is 20 computed on the far branch **and** on the near branch; `corrected_sd(60, s)` is `SD_SCALE[60] * s * sqrt(20)` | 3 |
| `tz07b_the_scale_is_the_only_change` | `corrected_sd(tau, sigma) / (sigma * sqrt(H(tau)))` is `SD_SCALE[tau]` to a relative `1e-55` at all seven keys; linearity in `sigma` to the same tolerance; `state` untouched | 5, 6 |
| `tz07b_more_time_is_more_dispersion` | `corrected_sd` is **strictly increasing in `tau`** across the seven keys at fixed `sigma`, and positive at every one | 4 |

`sigma * sqrt(H(tau))` is never written out in the tests: it is taken from
`pfair.state_and_sd`, which already returns exactly that product as the uncorrected `sd` on
both branches. There is one implementation of the horizon and the tests read it rather than
restating it.

### V6 — how much test data exists — **recorded from a separate invocation, not asserted**

`python3 -B tz07b-settlement-dispersion.py --v6`, run on its own and deliberately outside the
determinism artifact, because it counts something still growing. TZ-07a's own helper is called;
the question and TZ-06 §4's five conditions are unchanged.

| quantity | value at the moment of the run |
|---|---|
| interval directories with `T0 > 1789166400` | **280** |
| first / last such `T0` | `1789166700` / `1789250400` |
| **satisfying TZ-06 §4's five conditions** | **253** |
| short of the 400 TZ-08 needs | **147** |
| non-qualifying: `disconnect` | 24 |
| non-qualifying: no manifest and no S7 document | 3 |

Recorded, not asserted — there is no count this check could fail against, and the TZ attaches
none. At one interval per 300 s the remaining 147 take about 12 hours of capture, subject to
the same qualification rate.

---

## 6. What could not be implemented as written

Every deviation, ambiguity and workaround, named plainly.

**1. V4 runs two pipelines that read outcomes, and §2 says no outcome is read.** §2 puts
`resolution.json`, the resolved documents and `priceToBeat` out of scope; §7 V4 requires
re-running `tz06-calibration.py` and `tz07a-variance-time.py`, both of which read the venue's
resolutions internally, as they always have. I read the two sections as governing different
things: **the new instrument reads no outcome for M1 or M2** — it opens no settled document at
all — and **no calibration statistic appears in this report**, which is what §2's second
sentence protects. The regression subprocesses read what they were always built to read, and
their results are carried out of the instrument as counts of exact matches only. Nothing is
reported from them that §2 forbids. This is a reading of the TZ, not a repair of it, and it is
disclosed here so the Architect can overrule it.

**2. The bounded slice inside `mean_over`, and the guard that covers it.** `pfair.time_weighted_mean`
scans its whole `rows` argument from the start. At 1.39 million calls over streams of about
1,200 reports that is roughly 1.7 billion wasted comparisons, so the window is `bisect`ed and
the function is handed the reports it would have read — the seed it would have picked, up to
the first report at or after the close, which it breaks on without reading. **No formula was
rewritten and `pfair.py` was not touched for this.** The equality is asserted on a sample
rather than argued: 175 of 175 in V1's guard, above. The guard is the Executor's own and is not
one of the Architect's checks; it is counted separately and never folded into V1's count.

**3. `corrected_sd` carries a docstring that §5's code block does not show.** Every executable
statement is exactly as §5 writes it — the assert, the two branches, the return. A docstring
and the comment block above `SD_SCALE` were written to match the rest of the file, which
documents every function. No behaviour differs from the block as specified.

**4. Two private literals of the four deleted self-tests were deleted with them.**
`CORRECTED_SD_AT_LIVE_SCALE` — five hand-written expectations derived from `G_RATIO` — and
`SD_LITERAL_TOLERANCE` were used by the four deleted checks and by nothing else. Leaving them
would have left a table of superseded constants in the test file, which is precisely the trap
§5 removes from the pricer. §6.2 authorizes deleting the four checks; I read their private
literals as part of them. The 56 `v5_*` and 18 machinery checks reference neither and are
untouched, as their unchanged counts show.

**5. `tz07a-variance-time.py` keeps its `--emit-g` path, which now emits a superseded form.**
`emit_g` formats the string `G_RATIO = {...}` from its own measurement; it reads nothing from
the pricer, so the file runs. §6.3 says only the cross-check and the `G_RATIO_as_written`
output key are removed and that every other line stays byte-identical, so `emit_g` stays. It is
named here because a reader running `--emit-g` will get a table the pricer no longer has a
place for. That is what the TZ instructs, and I did not extend the removal to cover it.

**6. Nothing else.** The fingerprint gate passed, the host gate passed, no frozen row outside
§6's three moved, no test was edited to make it pass, no gate was reinterpreted, no threshold
was chosen by the Executor, and no publication step is outstanding. The `## Validation` section
is the Architect's and was run, not designed.

---

**A closing note on scope, and on what this report does not claim.** This TZ measured a scale
and froze it. It scored nothing. `SD_SCALE` has never been tested out of sample, and the
`Λ` column above is a fit on the same 400 members that produced the finding it repairs — which
is exactly why the TZ forbids a calibration statistic here. Whether the repaired estimator is
calibrated is TZ-08's question, against the gate TZ-07a §8 fixed and this TZ did not move.
