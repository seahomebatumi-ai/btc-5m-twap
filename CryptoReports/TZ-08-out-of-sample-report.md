# TZ-08 — Out-of-sample scoring of `p_fair` against the TZ-07a §8 gate — REPORT

**Status: BLOCKED at §7 V2, before any score exists.** As written, V2 cannot pass on this feed,
because its test and its negative control perturb the same report. Every `chainlink` report
in the 400 members' merged streams is stamped on a whole second: 281,114 of 281,114. So at 710 of
the 720 observations in the V2 sample, one report is stamped exactly at the checkpoint instant.
By TZ-06 §3's own definition of `S_t` (`timestamp <= (T0 + t) * 1000`), that is the report the
pricer reads. V2's first sentence calls it an observation "timestamped at or after the checkpoint",
which must leave the output bit-identical when perturbed. Its second sentence calls it "the last
readable report", which must change the output when perturbed. Applied as written, V2's test holds on
**10 of 720** observations and on **0 of 120** members. V2 ends "Both counts, or BLOCKED".
Contract §6 forbids editing a test to make it pass, and contract §2 forbids substituting a
reasonable alternative.

No score of any kind was computed:

- no branch `tz-08-out-of-sample` was created;
- `research/tz06-calibration.py` was not edited, and `research/tz08-out-of-sample.py` was not
  written;
- no `Brier`, no bin, no `λ̂`, no `Λ`, no `TZ-06 P`, no `TZ-06 V3`, and no observations file;
- V1 was not run, because it needs the §5 edit, which was not made.

`quotes.jsonl.gz` was never opened. Nothing was written under `/var/lib/btc-recorder/`. The live
recorder, pid `228592` on `4216c04`, was not signalled or restarted. This report was written from
the separate worktree `/root/tz07b-work/wt-report`, so the checkout the recorder runs from was never
switched.

Executor model: **Opus** (`claude-opus-5`), as the TZ requires.

---

## 0. Fingerprint

Read from `origin/main` = `8656f729a80aac138b42901d0e72b95a35afb273`, fast-forwarded into the
worktree above, on 2026-09-13.

**Map revision required:** `2026-09-13-b`. **Read:** `2026-09-13-b`.

**Map provenance:** `git log -1 --format=%H -- SYSTEM-MAP.md` gives
`9064dbdac2fab062deddbd283a1074531e249efa`. It begins with `9064dbd`, as §0 requires.

| anchor | required by TZ-08 §0 | read from map §0 |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` |
| `A2` — collector | `6c5089330629` | `6c5089330629` |
| `A3` — phase | `0-complete / 1-open / 2-not-started` | `0-complete / 1-open / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` | `9fd1c7de0f74` |
| `A6` — pricer | `cb72abb8dd8a` | `cb72abb8dd8a` |

### Fingerprint table

The table covers every row of the map's §0 table, computed on the clean `main` checkout at run
start. The table's single authorized change, to `research/tz06-calibration.py`, was not made, so its
hash before and after is the same value.

| path | lines | bytes | state | SHA-256 | matches map |
|---|---|---|---|---|---|
| `SYSTEM-MAP.md` | 396 | 40,605 | reported | `00bf58174de8bd83de4d2be31b531b1273ba716d2b510cba664f4780d8db52b8` | — |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11,128 | frozen | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` | yes |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` | yes |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` | yes |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` | — |
| `research/pfair.py` | 281 | 12,499 | frozen | `cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` | yes |
| `research/selftest-pfair.py` | 306 | 15,647 | frozen | `97de9782d319c82ee6a7d81ddbd8e00d590d85ffe2daa41abe3d71ae92712c94` | yes |
| `research/tz06-calibration.py` | 569 | 26,548 | frozen | `a6aaed94964775f34a9b26dba448ff0f998f32ad952e244bff834b67439ef123` | yes — before and after |
| `research/tz07a-variance-time.py` | 619 | 28,219 | frozen | `4321637751a3b847fa7e59309555b802dcc9d5ba68c7407a8ec20ab76c1b3d5e` | yes |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` | yes |
| `research/recorder/recorder.py` | 608 | 25,658 | frozen | `9fd1c7de0f749f8179dc092207b46528e42fd6563ce53d1c245cc74cf5439f03` | yes |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` | yes |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` | yes |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` | yes |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` | yes |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` | yes |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` | — |

All 14 `frozen` rows match. Two further files TZ-08 names:

| path | lines | bytes | SHA-256 |
|---|---|---|---|
| `CryptoTZ/TZ-07a-variance-time.md` (§4.1, §9 item 6) | 251 | 14,260 | `0e4852301c493ed7e4cb98d8d880a2c6b42b55f01811976ca9131fc62e61c4e3` |
| `CryptoTZ/TZ-08-out-of-sample.md` | 283 | 14,465 | `bacb45ec2c0a3ed824972fe0b536a99f5ef3bad68e78a5c07fbf0c1a09d77d00` |

**`pfair.py` against its frozen hash (§2.1, §9 item 8).** It read
`cb72abb8dd8a460908d0b4cd50da472ddd1c72b57be35b4cf90303503d47e01f` at run start and again
immediately before this report was committed.

---

## 1. Host gate and resource floor

| check | required | observed |
|---|---|---|
| `/var/lib/btc-recorder/` exists and holds interval directories | yes | yes. `btc-updown-5m/` held 916 directories at run start and 917 at the end; the first is `1789033800` |
| recorder running, newest `runtime.jsonl` start record sha | `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` | pid `228592`, `/root/tz04a-env/venv/bin/python -B -u recorder.py`, started 2026-09-12 09:53:04. The newest start record is `recv_ns` `1789206785264516934`, sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` |
| filesystem | `/dev/vda2`, total `31,612,203,008` bytes | `/dev/vda2`, total `31,612,203,008` bytes |
| free space at run start | at least `2,000,000,000` bytes | `6,617,538,560` bytes, and `6,616,801,280` at the end |

All three host checks pass, and so does the floor.

---

## 2. The §9 conditions evaluated before the stop

Set formation used the committed code unmodified, by calling `tz06-calibration.qualification`.
That function opens each unit's `manifest.json` and `resolution.json`, as TZ-06 §4 conditions 1–3
require. TZ-08 §2 permits reading outcome documents. No outcome value left the qualification call.

| §9 | condition | result |
|---|---|---|
| 1 | map revision, anchors, map provenance | pass: `2026-09-13-b`, 6 of 6 anchors, `9064dbd` |
| 2 | host gate | pass: 3 of 3 |
| 3 | free space | pass: `6,617,538,560` ≥ `2,000,000,000` |
| 4 | at least 400 qualifying units after `1789166400` | pass. **400** qualify among the first **433** units considered, which is every directory from `1789166700` to `1789296300`. There are 433 grid slots in that span and each has a directory. The **33** non-members all fail on `disconnect`, and nothing fails for any other reason. The first member is `1789166700` and the last is `1789296300` |
| 5 | disjointness, three assertions | pass: 3 of 3. The TZ-06 list was re-derived by calling `tz06-calibration.scoring_set` with no argument: 400 members, SHA-256 `6d94a346a47a04a1a0849968effd9023d7585fe628b304ba2ae7a15953ee67f9`, equal to §3's value. The TZ-08 list's intersection with it is 0, and `min(T0)` is `1789166700` > `1789166400` |
| 6 | TZ-07a readable; §8 against the code | readable (§0 above). My reading of §8 against `tz06-calibration.py` and `tz07a-variance-time.py` found no behaviour that contradicts §8. This is **recorded, not asserted**, because no gate run was made. See §5 for what the code does not implement |
| 7 | V1 | **not run.** It exercises the §5 edit, which was not made |
| 8 | `pfair.py` hash | pass at both checks (§0) |
| 9 | a third repository path | none. The only path this run adds is this report |
| 10 | `TZ-06 P`, `TZ-06 V3` floors | **not computed.** Both are calibration-adjacent, and the stop comes first |
| 11 | a read forbidden by §2 | none |

**TZ-08 member-list SHA-256**, in §3's form (the sorted `T0` list as decimal ASCII, joined by
newlines, with no trailing newline), computed with `tz07b-settlement-dispersion.member_list_sha`:
`3b17729c050e5fbf8fed1bd0877d5dd5c229370609cd672c84eeed1ddc3d5762`.

---

## 3. The blocker

TZ-08 §7 V2 reads, at lines 199–201:

> Perturb every observation timestamped at or after the checkpoint: output bit-identical, 120 of
> 120. Negative control: perturbing the last readable report changes the output, 120 of 120. Both
> counts, or BLOCKED.

The pricer reads `S_t` as "the last `chainlink` report with `timestamp <= (T0 + t) * 1000`" (TZ-06
§3, line 108). The code implements exactly that: `pfair.py:271` calls `last_at_or_before`, and
`analyze.py:136` compares with `ts <= ts_ms`. A report stamped exactly at the checkpoint instant is
therefore the value the model reads. It is both "timestamped at … the checkpoint" and "the last
readable report", so V2 requires one perturbation of one report to leave the output unchanged and to
change it. On this feed that report exists at almost every checkpoint, because the feed stamps on
whole seconds and every checkpoint `T0 + 300 − tau` is a whole second.

The earlier causality checks were worded differently. TZ-06 V4 (line 183) and TZ-07a V2 (line 193)
both perturb reports "timestamped **after** the checkpoint instant". The committed helper
implements that wording: `tz06-calibration.perturb_after` multiplies `ts > ts_ms`
(`tz06-calibration.py:221`), and `last_readable` picks the last `ts <= ts_ms` (line 233). These are
the functions §5 would have me call. TZ-08 V2's "at or after" is not what they do.

Neither reading lets the run continue:

- **As written:** the check fails. The test holds on 10 of 720 observations and 0 of 120 members,
  and V2's own last sentence makes that BLOCKED.
- **Calling the existing strict-after helper:** that replaces the Architect's wording with the
  earlier one. Contract §6 says "a test is never edited to make it pass … both stop the run and
  both require a new TZ". Contract §2 says the Executor does "not repair a defective TZ, guess the
  intent, or substitute a reasonable alternative".

**Which condition this is.** TZ-08 §9 declares its eleven conditions exhaustive, and V2 is not
among them. §7 V2 names its own BLOCKED outcome, however, and contract §9 names "the TZ is
unsatisfiable or self-contradictory" and "a test goes red". This stop rests on §7 V2's last
sentence together with contract §6 and §9. The §9 list and §7 V2 disagree about whether the list is
exhaustive, and I have not resolved that disagreement; I am reporting it.

The stop comes before any score, as TZ-08 §9 requires of a BLOCKED run. That point is also where
the conflict is first reached: V2 cannot be run without the V2 sample, and it has no bearing on a
score.

---

## 4. Evidence

The counts below come from two scratch scripts outside the repository, in `/root/tz08-work/`. Both
import the committed `research/` code from the `main` worktree unmodified, and both print counts
only. **They are recorded, not asserted**, because they are the evidence for a stop and not checks
of a delivered pipeline.

| file | bytes | SHA-256 |
|---|---|---|
| `probe-v2.py` | 4,653 | `b5902fee3fa0a6013f0cd4b48ed3db4db46cf464479ecad07a42c2638c79d078` |
| `probe-v2.json` | — | `36e8fa1efae7143b75a71e388b02680670f3f966d56a3d73ed2287ab5d3ed2dc` |
| `probe-set.py` | 2,345 | `b8a912ae0002d51a28299e9c55f091edc5f7ce2565d69d4692048cf99b74c4df` |
| `probe-set.json` | — | `42e488b686e685bdf9b293351b03940bff060b2cb160e94dd4361cee1418eb65` |

One field in `probe-v2.json` is wrong: `reasons` reads `{"disconnect": 0}` because of a comparison
bug in my own scratch code, which compared a list to a tuple. The non-member reasons in §2 come from
`probe-set.json` (`{"disconnect": 33}`). No other field is affected.

### E1 — the feed stamps on whole seconds

In the `pfair.merged_stream` `chainlink` streams of the 400 TZ-08 members, **281,114** reports were
read and **0** carry a `timestamp` that is not a multiple of 1,000 ms.

Below are three raw frames around the first member's `tau = 240` checkpoint:
`T0 = 1789166700`, `t = 60`, instant `1789166760000`. They come from `1789166700/chainlink.jsonl.gz`.

```
{"recv_ns":1789166760593717546,…,"raw":"{…\"payload\":{\"full_accuracy_value\":\"77081118869750000000000\",\"symbol\":\"btc/usd\",\"timestamp\":1789166759000,\"value\":77081.11886975},…\"type\":\"update\"}"}
{"recv_ns":1789166761273680753,…,"raw":"{…\"payload\":{\"full_accuracy_value\":\"77080847694366620000000\",\"symbol\":\"btc/usd\",\"timestamp\":1789166760000,\"value\":77080.84769436662},…\"type\":\"update\"}"}
{"recv_ns":1789166762807456957,…,"raw":"{…\"payload\":{\"full_accuracy_value\":\"77080854447131150000000\",\"symbol\":\"btc/usd\",\"timestamp\":1789166761000,\"value\":77080.85444713115},…\"type\":\"update\"}"}
```

The middle report, `timestamp` `1789166760000`, is the one `S_t` reads at that checkpoint. The
frames also carry the recorder's `recv_ns`. The model does not read it (TZ-06 §3), and this report
draws no conclusion from it.

### E2 — how often a report sits exactly at the checkpoint, over all 400 members

| tau | 240 | 180 | 120 | 90 | 60 | 30 | total |
|---|---|---|---|---|---|---|---|
| checkpoints with a `chainlink` report at the exact instant | 386 | 396 | 391 | 388 | 393 | 393 | **2,347 of 2,400** |

### E3 — V2 applied as written

I built the sample by V2's own construction rule: every member of the 400 "that carries a recorded
disconnect", filled out from the remainder in `T0` order. For the first part I read "carries a
recorded disconnect" as the member's own manifest or its predecessor's recording one; the second is
where TZ-07a M6 finds a member's outages. **22** members qualify through the predecessor's manifest.
None qualifies through its own, because TZ-06 §4 condition 1 already excludes those. **98** further
members come from the remainder in `T0` order, the last of them `1789202100`.

That gives **120** members. Each is priced at the six gated taus with
`tz07a-variance-time.corrected_observations`, the `SD_SCALE` pricer, for **720** observations.

| count | value |
|---|---|
| observations with a `chainlink` report stamped exactly at the checkpoint instant | **710 of 720** |
| of those, observations where `tz06-calibration.last_readable` (the negative control's subject) returns that report | **710 of 710** |
| observations bit-identical on `state`, `sd_corrected` and `p_fair_corrected`, after every `chainlink` and `twap60` report with `timestamp >= checkpoint` is multiplied by `tz06-calibration.PERTURBATION` (`1.0001`) | **10 of 720** |
| members bit-identical at all six taus | **0 of 120** |

The count of bit-identical observations, 10, equals the count of observations with no report at the
instant. The probe did not check whether they are the same ten observations, so I do not claim that.

---

## 5. Found in the same reading — not the blocker

These are facts about the TZ as it meets the committed code. None of them caused the stop, and no
remedy is proposed.

1. **§4.2 and §6 item 3 ask `tz07a-variance-time.py` for "the scale statistic and its standard
   error".** The code computes no standard error.
   - `lambda_hat` returns `lambda_hat`, `ll_at_lambda_hat`, `ll_at_one`, `likelihood_ratio`,
     `chi_square_1df_p` and `n` (`tz07a-variance-time.py:282–302`).
   - A search of `research/*.py` and `research/recorder/*.py` for "standard error", `std_err`,
     `fisher`, `hessian` and `curvature` returns nothing.
   - TZ-07a §8 itself names no standard error. §5 forbids a formula in the new driver and does not
     authorize any change to `tz07a-variance-time.py`.
   - As written, therefore, §6 item 3's standard error and the distance from 1 in standard errors
     have no permitted source.
2. **G3's bound is implemented by no committed code.** `LAMBDA_LO`, `LAMBDA_HI` and `LAMBDA_TOL` are
   the only G3 constants in `tz07a-variance-time.py` (line 79), and the comment above them says the
   file runs `λ̂` "as a section 5 diagnostic only, with no threshold attached". §2.2 forbids
   introducing a threshold into code. G3's verdict could therefore only be read in the report
   against the quoted §8, not computed by "the code that already implements" it, as §4.2 puts it.
   G2's allowance, by contrast, is in code: `tz06-calibration.MAX_FAILING_BINS = 2`.
3. **§5 asks each new keyword-only parameter to default to "the literal presently in the file".**
   The member count has such a literal: `SET_SIZE = 400`, already the default of `scoring_set`'s
   `need`. The window's lower bound has none, because `scoring_set` opens at
   `min(int(name) for name in os.listdir(...))` (`tz06-calibration.py:94`), which is an expression
   rather than a literal.

---

## 6. Publication and scope of the stop

- **Branch, implementation commit, pull request:** none. No implementation exists.
- **Report:** this file, committed straight to `main` from `/root/tz07b-work/wt-report`.
- **Separation self-check, contract §4.2.** The first two lines do not apply: there is no
  implementation commit and no `tz-08-out-of-sample` branch, and `git ls-remote --heads origin`
  lists `refs/heads/main` only. The third line prints nothing:

  ```
  $ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
  $ echo $?
  1
  ```

- **Capture:** read-only.
  - Opened: `manifest.json` and `resolution.json` of the units considered, through TZ-06 §4's
    qualification; `chainlink` streams of the 400 members and their predecessors; `twap60` of the 120
    V2 members.
  - Never opened: `quotes.jsonl.gz`, `binance`, `twap30` and `gamma.json`.
- **Not produced:** no label was scored, and no calibration statistic of any kind was computed.
- **Scratch:** `/root/tz08-work/` holds copies of the specifications and code read from
  `origin/main`, the two probes and their outputs. It is outside the repository.
