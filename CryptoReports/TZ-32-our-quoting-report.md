# TZ-32 report — W1, our quoting: does a quote of ours, simulated on the pair book's streams with queue position, the taker delay and our own cancels, keep the named makers' edge?

**W1 READING: W1-NO-EARN.** The set has 288 members, `1792754100` (2026-10-23 11:15 UTC) to `1793013300` (2026-10-26
11:15 UTC). On their five-minute legs, the quoting rule's fills before `T0 + 300` give these sums:

- **`front`**, every assumption that cannot be measured made for us: first in every queue, never met by a crossing
  order. **`S` = `506.689` USDC on `Sh` = `642,581.620000000000` shares, `0.079` c a share.** That is
  `−1,186.672` at settlement (`−0.185` c a share) and `+1,693.361` of rebate
  (`+0.264` c a share). **Its NO EARN holds:** `S <= δ · Sh − thr` = `2,726.942`
  (`0.424` c a share), with a margin of `+2,220.253` (`+0.346` c a share).
- **`behind`**, every such assumption made against us. **`S` = `−2,271.140` USDC on `Sh` = `194,269.530000000000`
  shares, `−1.169` c a share.** That is `−2,792.574` at settlement (`−1.437` c a
  share) and `+521.434` of rebate (`+0.268` c a share). **Its EARN does not hold:** it
  needed `S >= thr` = `525.780` (`0.271` c a share), and its margin is `−2,796.920`
  (`−1.440` c a share).

`behind`'s EARN fails, so §4.5's first row does not apply. `front`'s NO EARN holds, so its second row gives
**W1-NO-EARN**. Each answer was tested at `α = 0.005` by TZ-23's Ville bound, with `δ = 0.005` and `λ`
`0.014605` (`behind`) and `0.016557` (`front`), both fixed before any member was read.

TZ-32 §1 item 3: **W1-NO-EARN closes W1 for this rule.** Even with every assumption for it, a quote at the touch kept
less than half a tick a share on these 288 legs, rebate included. The named makers' edge is not the touch's to take. It
says nothing of another rule, another latency or another leg (§4.5).

**Barred from the reading, and printed by the instrument.** `front`'s `S` also lies above `front`'s own EARN bound,
`485.966`, by `+20.723`. So TZ-23's `reading` names `front`'s own word EARN in
`logs/80-score-1.log`, but §4.5 reads no EARN of `front`. `behind`'s `S` lies below `behind`'s own NO EARN bound,
`445.568`, and §4.5 reads no NO EARN of `behind` either. The rebate is `0.264` to `0.271` c a share in
every variant, and the settlement part is negative in every variant. `S` a share by variant: `front_L0` `0.151` c, `front_cross`
`0.079` c, `L0` `−0.798` c, `prop` `−0.940` c, `behind_nocross`
`−1.169` c, `L100` `−1.324` c and `L250` `−1.489` c. Labels: 136 Up of 288.

**The power at the set's own `V` and `Sh`** was printed by `replay` before any label: `0.998569448148551` for W1-EARN
and `1.0` for W1-NO-EARN, against `0.998` and above `0.99999` projected. Per member, `behind`'s `V` was
`0.899` times the projection's and its `Sh` `0.968` times; `front`'s were
`1.037` and `0.914` times. No row of §4.5 reads a power.

**Every gate before the reading passed.**
- G-REHEARSAL **PASS, 11 of 11**: TZ-27's 51 windows, 135,900 unit lines byte for byte the Architect's
  (`52b1c637…`), and the nine variants' totals equal.
- G-SET **PASS**: 288 members of **289 candidates considered, 1 non-member** — `1792923300`, a gap above 15 s in its
  stream. The members run `1792754100` … `1793013300`, member list `4c10c0a17532403890ebecd2146c4b0be42d830506e83363ccc0805c9a16a99d`.
- G-BOOK **PASS**: the rebuilt touch equalled the venue's own at **417,728 of 418,535 match
  frames, 99.81%**, against 99 in 100.
- DETERMINISM **PASS, 18 of 18**: every sixteenth member's unit, from a second download and a second replay, byte for
  byte the replay's.
- Self-test **74 of 74**. The replay ran twice, **2 of 2** files `unchanged`. The score ran twice, **2 of 2** files
  `unchanged`, with **2** ledger lines. All 288 units, the rehearsal's 51 and the rescore's 18 started and ended
  inside the pair book's idle stretch.
- G-STILL **PASS**: the recorder `2388318`, `NRestarts` 0, and the pair book `2943176`, `NRestarts` 8, both `active`
  and unchanged from 06:58:32 to 07:46:49 UTC.

**The set's labels were first read at 2026-10-27 07:46:36 UTC**, the first ledger line's `at`. That was after the
instrument's commit `b601f75` was on `origin`, at 06:58:07.251 UTC by `ls-remote`. It was also after the constants
`5f4f43c3…` and the units `bad6b50a…` were on disk with their SHA-256 in `state.json`: first recorded at 07:38:33
UTC, and again by the second `replay` at 07:38:45, which is `state.json`'s `constants_at`.

**The run:** 2026-10-27 06:55 to 07:54 UTC, on the capture host. It started 3 h 35 min after §3.6's instant,
and the archive had already moved the last candidate: its calendar run of 03:00:20 UTC completed at 03:15:41. So
`fetch` waited 0 s, and its 06:00:00 UTC deadline never came into play (§6 item 2). No command was refused by the
session's classifier. The Boss ran nothing.

---

## 0. Fingerprint

Read before any work, against `SYSTEM-MAP.md` in the primary checkout `/root/btc-5m-twap` at `main`
`45f112cde92d09bfbe003e8b24c1567dbb60ef18`:

| item | required by TZ-32 | read |
|---|---|---|
| revision | `2026-10-23-a` | `2026-10-23-a` |
| `A1` — observation set | `229a944f2d51` | `229a944f2d51` |
| `A2` — collector | `6c5089330629` | `6c5089330629`, re-derived from `research/twap-divergence.py` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | equal |
| `A4` — executor contract | `437b45ea196b` | `437b45ea196b`, re-derived from `BTC-EXECUTOR-INSTRUCTIONS.md` |
| `A5` — recorder | `0f6c90451cbd` | `0f6c90451cbd`, re-derived from `research/recorder/recorder.py` |
| `A6` — pricer | `729f0bcdbee3` | `729f0bcdbee3`, re-derived from `research/pfair.py` |

The executor model the TZ names is Opus; this session ran on Opus. TZ-32 reads no pricer and scores none; `A6` is
stated so that what was not scored is not in doubt.

### 0.1 The 43 rows of the map's §0 table, and the map (V1) — `logs/02-fingerprint.log`, verbatim

```text
$ nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz32-work/stage/research/tz32-our-quoting.py fingerprint
[2026-10-27T06:56:49Z] re-derived A2 research/twap-divergence.py sha256[:12] 6c5089330629 equal
[2026-10-27T06:56:49Z] re-derived A4 BTC-EXECUTOR-INSTRUCTIONS.md sha256[:12] 437b45ea196b equal
[2026-10-27T06:56:49Z] re-derived A5 research/recorder/recorder.py sha256[:12] 0f6c90451cbd equal
[2026-10-27T06:56:49Z] re-derived A6 research/pfair.py sha256[:12] 729f0bcdbee3 equal
[2026-10-27T06:56:49Z] SYSTEM-MAP.md                                  1617 lines   385135 bytes 594b43669de612fc61f51cd80361c6c245b3941794fc7f067e045fa63f28f55f reported
[2026-10-27T06:56:49Z] BTC-EXECUTOR-INSTRUCTIONS.md                    234 lines    11128 bytes 437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b frozen equal
[2026-10-27T06:56:49Z] research/twap-divergence.py                    1135 lines    50928 bytes 6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473 frozen equal
[2026-10-27T06:56:49Z] research/selftest-twap-divergence.py            376 lines    16736 bytes ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a frozen equal
[2026-10-27T06:56:49Z] research/tz02-distribution.py                   334 lines    14511 bytes f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4 tracked
[2026-10-27T06:56:49Z] research/pfair.py                               441 lines    19357 bytes 729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68 frozen equal
[2026-10-27T06:56:49Z] research/selftest-pfair.py                      619 lines    32559 bytes b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa frozen equal
[2026-10-27T06:56:49Z] research/tz06-calibration.py                    577 lines    27138 bytes 715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f frozen equal
[2026-10-27T06:56:49Z] research/tz07a-variance-time.py                 623 lines    28414 bytes 513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771 frozen equal
[2026-10-27T06:56:49Z] research/tz07b-settlement-dispersion.py         515 lines    24926 bytes 424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc frozen equal
[2026-10-27T06:56:49Z] research/tz08a-out-of-sample.py                 745 lines    38822 bytes 37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c frozen equal
[2026-10-27T06:56:49Z] research/tz09-disk-inventory.py                 894 lines    41004 bytes b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6 frozen equal
[2026-10-27T06:56:49Z] research/tz10b-sigma-or-link.py                1224 lines    61018 bytes 406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088 frozen equal
[2026-10-27T06:56:49Z] research/tz11a-student-link.py                 1231 lines    64732 bytes 0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839 frozen equal
[2026-10-27T06:56:49Z] research/tz12-sized-gate.py                    1157 lines    61637 bytes d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999 frozen equal
[2026-10-27T06:56:49Z] research/tz13-sized-gate-test3.py              1074 lines    53901 bytes a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd frozen equal
[2026-10-27T06:56:49Z] research/tz14-quote-inventory.py               2124 lines   109972 bytes 978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02 frozen equal
[2026-10-27T06:56:49Z] research/tz15-phase2-gate.py                   1517 lines    73799 bytes 66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3 frozen equal
[2026-10-27T06:56:49Z] research/tz16a-phase2-decisive-gate.py         2198 lines   111192 bytes 3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125 frozen equal
[2026-10-27T06:56:49Z] research/tz17-settlement-chain.py              1102 lines    38622 bytes e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92 frozen equal
[2026-10-27T06:56:49Z] research/tz18a-chainbook-capture.py            1683 lines    69517 bytes e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae frozen equal
[2026-10-27T06:56:49Z] research/tz20-capture-under-systemd.py          771 lines    36528 bytes 104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7 frozen equal
[2026-10-27T06:56:49Z] research/tz21-recorder-memory.py               1284 lines    59009 bytes d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f frozen equal
[2026-10-27T06:56:49Z] research/tz23-maker-m0.py                      1184 lines    54885 bytes 6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f frozen equal
[2026-10-27T06:56:49Z] research/tz24-nesting-b2.py                    1535 lines    76142 bytes 4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b frozen equal
[2026-10-27T06:56:49Z] research/tz26-nesting-b3-capture.py            2492 lines   118466 bytes caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec frozen equal
[2026-10-27T06:56:49Z] research/tz27-pairbook-archive.py              2078 lines   106284 bytes 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673 frozen equal
[2026-10-27T06:56:49Z] research/tz28-pairbook-archive-timer.py        1438 lines    74576 bytes 46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4 frozen equal
[2026-10-27T06:56:49Z] research/tz29-maker-m0-second-look.py          1225 lines    68959 bytes 18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905 frozen equal
[2026-10-27T06:56:49Z] research/tz30-nesting-b3-measure.py            2518 lines   131119 bytes 93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab frozen equal
[2026-10-27T06:56:49Z] research/tz31-who-earns.py                     1523 lines    84775 bytes 7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765 frozen equal
[2026-10-27T06:56:49Z] research/recorder/recorder.py                   651 lines    27821 bytes 0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7 frozen equal
[2026-10-27T06:56:49Z] research/recorder/config.py                     112 lines     4773 bytes 8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d frozen equal
[2026-10-27T06:56:49Z] research/recorder/manifest.py                   254 lines    10002 bytes 79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045 frozen equal
[2026-10-27T06:56:49Z] research/recorder/analyze.py                    813 lines    34705 bytes eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d frozen equal
[2026-10-27T06:56:49Z] research/recorder/probe.py                      227 lines     9324 bytes 50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2 frozen equal
[2026-10-27T06:56:49Z] research/recorder/selftest.py                   573 lines    30591 bytes c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90 frozen equal
[2026-10-27T06:56:49Z] deploy/systemd/btc-recorder.service              23 lines      707 bytes 3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1 frozen equal
[2026-10-27T06:56:49Z] deploy/systemd/btc-chainbook.service             22 lines      724 bytes a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2 frozen equal
[2026-10-27T06:56:49Z] deploy/systemd/btc-pairbook.service              22 lines      761 bytes ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8 frozen equal
[2026-10-27T06:56:49Z] deploy/systemd/btc-pairbook-archive.service      17 lines      794 bytes 2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7 frozen equal
[2026-10-27T06:56:49Z] deploy/systemd/btc-pairbook-archive.timer        13 lines      417 bytes 07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913 frozen equal
[2026-10-27T06:56:49Z] .gitignore                                        5 lines      252 bytes 9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b tracked
[2026-10-27T06:56:49Z] SYSTEM-MAP.md 1617 lines 385135 bytes sha256 594b43669de612fc61f51cd80361c6c245b3941794fc7f067e045fa63f28f55f
[2026-10-27T06:56:49Z] FINGERPRINT PASS: revision 2026-10-23-a; anchors 6 of 6, 4 re-derived; rows 43: frozen 40 of 40 equal, tracked 2, reported 1; tz23-maker-m0.py is the file this instrument loads, a frozen row
[2026-10-27T06:56:49Z] malloc tuned: True
[2026-10-27T06:56:49Z] peak memory of this run: 36200448 bytes
[2026-10-27T06:56:49Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

`I fingerprint` from the worktree at §3.1 (`logs/12-fingerprint-wt.log`) printed the same 43 rows and the same map line,
and `FINGERPRINT PASS` again at 06:57:53 UTC, peak `36,229,120` bytes, `opens refused: 0`.

---

## 1. Input

### 1.1 What was read

| input | how | size, count, hash |
|---|---|---|
| `CryptoTZ/TZ-32-our-quoting.md` | §0.1's script, twice | Appendix A extracted: `research/tz32-our-quoting.py`, 2,576 lines, 138,209 bytes, `6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61` at both |
| `research/tz23-maker-m0.py` | `install` beside the staged copy; loaded by its bytes in every mode | `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` in the stage and in the worktree |
| `SYSTEM-MAP.md` and the 42 files of its table | `I fingerprint`, twice | §0.1 |
| TZ-27's `set.json` in the forensic store | `rehearse`; `stat` and `sha256sum` at §0.3, twice | `16570` bytes, `ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd` |
| TZ-27's 51 stream assets, `tz-27-pairbook-streams` | `rehearse`: downloaded anonymously, verified by bytes and SHA-256, replayed, removed | 51 files, `678,739,504` bytes |
| TZ-27's 51 legs' settled documents | `rehearse`, through TZ-23's `gamma_docs`, held to the idle stretch | `rehearsal/docs.json`, `27,592` bytes, `22f16a747624cbc497756d27ea7574485cba8b68ff95277ac4025041aa724afd` |
| the archive's ledger and every complete run's `set.json` | `archive` (twice), `fetch`, `still` | `64,237` bytes, `c066f771d34694fc73235bd28b0ff5088f7c00c9815562d3cbe97548cbba0635`, 270 records at the first `archive` read and at the second; 27 complete runs' sets |
| `window.json` of the 350 candidates `1792754100` … `1793068200` | `fetch` alone | all 350 read, no stream file opened; the walk considered 289 |
| the members' legs' settled documents | `fetch`, through TZ-23's `gamma_docs`, 15 requests held to the idle stretch | carried in `set/w1-set.json`, `271,517` bytes, `83af4226af064e85271e5c6b58d3e7d464a3729058775da69528d5ffab98d47e` |
| the members' 288 stream assets, from the archive's Releases | `replay`: downloaded anonymously, verified by bytes and SHA-256, replayed, removed, each unit held | 288 files, `5,050,052,883` bytes; 18 of them again by `rescore`, `312,885,963` bytes |
| the members' labels | `score`, twice, after the constants and the push | `136` Up of 288 |
| systemd and the journal | `systemctl show`, `is-active`, `is-enabled`, `list-timers`, `journalctl` | §2.5 to §2.7 |

**Nothing was re-collected.** No stream file under `/var/lib/btc-pairbook/` was opened by anything; the only file
there opened was `<T>/window.json` of a candidate, by `fetch`. Nothing under `/var/lib/btc-recorder/` or
`/var/lib/btc-chainbook/` was opened but by §0.3's `find` and `grep -c` (both runs) and B-RECLAIM-OWN's `df`.

### 1.2 The set (G-SET, V7) — `logs/61-fetch.log`, verbatim

```text
$ I fetch
[2026-10-27T07:03:35Z] MemAvailable 336871424 bytes, floor 81928192; free 11844763648 bytes, floor 5400000000
[2026-10-27T07:03:35Z] the archive has moved windows to 1793080800, at or after 1793068200, after 0 s waited
[2026-10-27T07:03:36Z] wrote /root/tz32-work/set/w1-set.json 271517 bytes sha256 83af4226af064e85271e5c6b58d3e7d464a3729058775da69528d5ffab98d47e
[2026-10-27T07:03:36Z] G-SET PASS: 288 members of 289 considered, 1792754100 (2026-10-23T11:15:00Z) to 1793013300 (2026-10-26T11:15:00Z); 288 stream files, 5050052883 bytes; member list sha256 4c10c0a17532403890ebecd2146c4b0be42d830506e83363ccc0805c9a16a99d; /root/tz32-work/set/w1-set.json sha256 83af4226af064e85271e5c6b58d3e7d464a3729058775da69528d5ffab98d47e
[2026-10-27T07:03:36Z] document requests 15 for 300 windows
[2026-10-27T07:03:36Z] non-members 1: [[1792923300, "stream: a gap above 15 s"]]
[2026-10-27T07:03:36Z] members by the weekday of their leg {"Fri": 51, "Mon": 46, "Sat": 96, "Sun": 95}
[2026-10-27T07:03:36Z] malloc tuned: True
[2026-10-27T07:03:36Z] peak memory of this run: 44986368 bytes
[2026-10-27T07:03:36Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

- **Candidates considered: 289** of the 350 `1792754100` … `1793068200`; the walk stopped at the 288th member.
- **Members: 288**, `1792754100` (2026-10-23 11:15 UTC) to `1793013300` (2026-10-26 11:15 UTC); their legs
  `btc-updown-5m-{T+600}`.
- **Non-members: 1** — `1792923300` (2026-10-25 07:15 UTC), *stream: a gap above 15 s*, TZ-30's stream rule. Because
  of it the set runs one window past the `1793012400` that §1 gave for the case where every candidate qualifies, and
  its member list is `4c10c0a17532403890ebecd2146c4b0be42d830506e83363ccc0805c9a16a99d`, not `3ec41ed9…`.
- **By the weekday of the leg:** Friday 51, Saturday 96, Sunday 95, Monday 46. §1's every-candidate case was 51, 96,
  96 and 45; the one non-member is a Sunday leg and the extra member a Monday leg.
- **Document requests: 15**, for 300 windows, in twenties, each held to the idle stretch; none after the 288th member.
- Every member's one stream file is in the archive's assets by its own name, size and SHA-256 (asserted by `fetch`);
  every member's document passes TZ-23's `qualify`, states `orderMinSize` `5`, and carries the condition and the two
  tokens `window.json` carries.
- `set/w1-set.json` `83af4226af064e85271e5c6b58d3e7d464a3729058775da69528d5ffab98d47e`, written once at 07:03:36 UTC
  and recorded in `state.json` as `set_sha`.

### 1.3 The rehearsal span

TZ-27's 51 windows `1791660600` … `1791705600`, one stream asset each on `tz-27-pairbook-streams`, every one read by
TZ-30's rehearsal and by the Architect's reference; their legs' 51 documents, 23 Up. Read by `rehearse` alone.

---

## 2. Measurements

### 2.1 The constants, label-free (§3.7) — `logs/70-replay-1.log`, verbatim

```text
$ I replay           # the first run
[2026-10-27T07:03:56Z] MemAvailable 318504960 bytes, floor 81928192; free 11844374528 bytes, floor 5400000000
[2026-10-27T07:03:56Z] units to replay 288, 5050052883 bytes of streams in all
[2026-10-27T07:06:23Z] projected 1062 s of replay for 5050052883 bytes after 24 units at 0.2104 s a megabyte
[2026-10-27T07:06:23Z] units 24 this run, 147 s
[2026-10-27T07:08:25Z] units 48 this run, 270 s
[2026-10-27T07:16:24Z] units 72 this run, 749 s
[2026-10-27T07:18:24Z] units 96 this run, 869 s
[2026-10-27T07:20:07Z] units 120 this run, 971 s
[2026-10-27T07:21:32Z] units 144 this run, 1057 s
[2026-10-27T07:23:11Z] units 168 this run, 1156 s
[2026-10-27T07:31:20Z] units 192 this run, 1644 s
[2026-10-27T07:32:42Z] units 216 this run, 1727 s
[2026-10-27T07:34:16Z] units 240 this run, 1821 s
[2026-10-27T07:36:31Z] units 264 this run, 1955 s
[2026-10-27T07:38:32Z] units 288 this run, 2077 s
[2026-10-27T07:38:32Z] units 288: inside the idle stretch 288, ending after second 590 0; longest 10.6 s, download 2.0 s and replay 8.8 s at most; 762 s waited; processor 989.9 s; 5050052883 bytes downloaded; retries 0; windows 2026-10-27T07:00:00Z to 2026-10-27T07:30:00Z
[2026-10-27T07:38:33Z] wrote /root/tz32-work/replay/w1-units.txt 47636864 bytes sha256 bad6b50a8d25fae2bf96f2df68ff8140ce6d4ec39ad74c83a7d15bfa631f5d60
[2026-10-27T07:38:33Z] units 930762 lines
[2026-10-27T07:38:33Z] wrote /root/tz32-work/replay/w1-constants.json 4308 bytes sha256 5f4f43c34e74d25eed283096a50803e9b37321a15408ee072411bc3375c1dac9
[2026-10-27T07:38:33Z] members 288, first 1792754100 2026-10-23T11:15:00Z, last 1793013300 2026-10-26T11:15:00Z; member list sha256 4c10c0a17532403890ebecd2146c4b0be42d830506e83363ccc0805c9a16a99d
[2026-10-27T07:38:33Z] G-BOOK PASS: match frames 418535, the rebuilt touch equal to the venue's at 417728 (0.998071845843); every level equal at 414284 (0.989843143345), barred; matches read 415916, two-sided 1553; sessions 390, closes 390
[2026-10-27T07:38:33Z] the capture's lag, a price_change frame's host receipt less its venue stamp, over 288 members and 37049296 frames of the leg: the median member's median 17 ms; its 99th percentile 106 ms at the median member and 5595 ms at the worst, above 1,000 ms at 6 members; the longest 5886 ms, the least 5 ms
[2026-10-27T07:38:33Z] behind: sent 193612, cancels 182999, refused 18145, crossings 27401; members with a fill 288; fills 50051, shares 194269.530000000000, X 167.930000000000, C 854.564000000000, R 521.433734504480, V 89287.551100000000000000000000
[2026-10-27T07:38:33Z] front: sent 273752, cancels 184772, refused 21988, crossings 0; members with a fill 288; fills 182324, shares 642581.620000000000, X -368.760000000000, C -557.367760000000, R 1693.361221636280, V 80188.929800000000000000000000
[2026-10-27T07:38:33Z] prop, barred from every reading: sent 204505, cancels 184230, refused 18988, crossings 23509; members with a fill 288; fills 69182, shares 259489.790000000000, X 243.210000000000, C 1110.262930000000, R 692.167703398500, V 91183.579500000000000000000000
[2026-10-27T07:38:33Z] behind_nocross, barred from every reading: sent 193513, cancels 182907, refused 18139, crossings 0; members with a fill 288; fills 49883, shares 193374.640000000000, X 163.060000000000, C 864.293300000000, R 518.975970040080, V 88906.302600000000000000000000
[2026-10-27T07:38:33Z] front_cross, barred from every reading: sent 273698, cancels 184726, refused 21972, crossings 14720; members with a fill 288; fills 182331, shares 642891.570000000000, X -354.910000000000, C -545.818660000000, R 1694.205895522280, V 80373.994300000000000000000000
[2026-10-27T07:38:33Z] L0, barred from every reading: sent 200058, cancels 183670, refused 8023, crossings 25019; members with a fill 288; fills 54273, shares 216663.720000000000, X 197.220000000000, C 892.480660000000, R 577.178807404640, V 74891.514800000000000000000000
[2026-10-27T07:38:33Z] L100, barred from every reading: sent 190886, cancels 183321, refused 26953, crossings 25270; members with a fill 288; fills 47545, shares 181281.890000000000, X 149.370000000000, C 746.653530000000, R 486.747294231940, V 96713.641700000000000000000000
[2026-10-27T07:38:33Z] L250, barred from every reading: sent 188391, cancels 184178, refused 43478, crossings 18839; members with a fill 288; fills 47216, shares 185308.940000000000, X 401.840000000000, C 802.075840000000, R 501.962608580160, V 113376.145200000000000000000000
[2026-10-27T07:38:33Z] front_L0, barred from every reading: sent 302274, cancels 180363, refused 9245, crossings 0; members with a fill 288; fills 226069, shares 802213.160000000000, X -85.840000000000, C -459.515200000000, R 2114.258555907120, V 79444.486800000000000000000000
[2026-10-27T07:38:33Z] behind: V 89287.551100000000000000000000; Sh 194269.530000000000; lambda 0.014605; L 5.298317366548; thr 525.779797496659 (0.002706444997 a share)
[2026-10-27T07:38:33Z] behind: EARN at S >= 525.779797496659; NO EARN at S <= 445.567852503341 (0.002293555003 a share); power 0.998569448148551
[2026-10-27T07:38:33Z] front: V 80188.929800000000000000000000; Sh 642581.620000000000; lambda 0.016557; L 5.298317366548; thr 485.965686576833 (0.000756270754 a share)
[2026-10-27T07:38:33Z] front: EARN at S >= 485.965686576833; NO EARN at S <= 2726.942413423167 (0.004243729246 a share); power 1.0
[2026-10-27T07:38:33Z] W1 reads W1-EARN on behind's EARN bound and W1-NO-EARN on front's NO EARN bound (TZ-32 section 4.5)
[2026-10-27T07:38:33Z] constants sha256 5f4f43c34e74d25eed283096a50803e9b37321a15408ee072411bc3375c1dac9, units sha256 bad6b50a8d25fae2bf96f2df68ff8140ce6d4ec39ad74c83a7d15bfa631f5d60, in state.json
[2026-10-27T07:38:33Z] malloc tuned: True
[2026-10-27T07:38:33Z] peak memory of this run: 53673984 bytes
[2026-10-27T07:38:33Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

Every variant over the set's 288 members, printed before any label was read:

| variant | role | sent | cancels | refused | crossings | members with a fill | fills | shares | `X` | `C` | `R` | `V` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `behind` | **gated: W1-EARN** | 193,612 | 182,999 | 18,145 | 27,401 | 288 | 50,051 | `194,269.530000000000` | `167.930000000000` | `854.564000000000` | `521.433734504480` | `89,287.551100000000000000000000` |
| `front` | **gated: W1-NO-EARN** | 273,752 | 184,772 | 21,988 | 0 | 288 | 182,324 | `642,581.620000000000` | `−368.760000000000` | `−557.367760000000` | `1,693.361221636280` | `80,188.929800000000000000000000` |
| `prop` | barred | 204,505 | 184,230 | 18,988 | 23,509 | 288 | 69,182 | `259,489.790000000000` | `243.210000000000` | `1,110.262930000000` | `692.167703398500` | `91,183.579500000000000000000000` |
| `behind_nocross` | barred | 193,513 | 182,907 | 18,139 | 0 | 288 | 49,883 | `193,374.640000000000` | `163.060000000000` | `864.293300000000` | `518.975970040080` | `88,906.302600000000000000000000` |
| `front_cross` | barred | 273,698 | 184,726 | 21,972 | 14,720 | 288 | 182,331 | `642,891.570000000000` | `−354.910000000000` | `−545.818660000000` | `1,694.205895522280` | `80,373.994300000000000000000000` |
| `L0` | barred | 200,058 | 183,670 | 8,023 | 25,019 | 288 | 54,273 | `216,663.720000000000` | `197.220000000000` | `892.480660000000` | `577.178807404640` | `74,891.514800000000000000000000` |
| `L100` | barred | 190,886 | 183,321 | 26,953 | 25,270 | 288 | 47,545 | `181,281.890000000000` | `149.370000000000` | `746.653530000000` | `486.747294231940` | `96,713.641700000000000000000000` |
| `L250` | barred | 188,391 | 184,178 | 43,478 | 18,839 | 288 | 47,216 | `185,308.940000000000` | `401.840000000000` | `802.075840000000` | `501.962608580160` | `113,376.145200000000000000000000` |
| `front_L0` | barred | 302,274 | 180,363 | 9,245 | 0 | 288 | 226,069 | `802,213.160000000000` | `−85.840000000000` | `−459.515200000000` | `2,114.258555907120` | `79,444.486800000000000000000000` |

`sent` counts the orders the rule sent, `cancels` its cancels, `refused` the post-only orders refused on arrival and
`crossings` the crossing events counted where the opposite side reached a resting quote, each due to fill it 150 ms
later if our cancel had not arrived; `X` is the net Up position over
the fills, `C` its cost, `R` the rebate and `V` the sum over members of `X` squared.

| gated variant | `V` | `Sh` | `λ` | `thr` | EARN at `S >=` | NO EARN at `S <=` | power, printed before any label |
|---|---|---|---|---|---|---|---|
| `behind` | `89,287.551100000000000000000000` | `194,269.530000000000` | `0.014605` | `525.779797496659` (`0.271` c a share) | `525.779797496659` | `445.567852503341` (`0.229` c a share) | `0.998569448148551` |
| `front` | `80,188.929800000000000000000000` | `642,581.620000000000` | `0.016557` | `485.965686576833` (`0.076` c a share) | `485.965686576833` | `2,726.942413423167` (`0.424` c a share) | `1.0` |

`L` = `ln(1/α)` = `5.298317366548` for both. The c-a-share figures are each bound over the variant's `Sh`, times 100, from the
printed figures at 60 digits; the instrument prints the per-share `thr` and NO EARN bound itself. Only `behind`'s EARN
bound and `front`'s NO EARN bound are read (§4.5); the other two bounds are printed by the instrument and read by nothing.

**The projection, and the set's own figures** (TZ-32 §1: "The projection rests on two quantities, the set's `V` and
`Sh` per member"). Both were printed with `thr` and the power before any label:

| variant | per member `V`, the 302's | per member `V`, the set's | ratio | per member `Sh`, the 302's | per member `Sh`, the set's | ratio | bound, projected | bound, the set's | power, projected | power, the set's |
|---|---|---|---|---|---|---|---|---|---|---|
| `behind` | `344.97` | `310.03` | `0.899` | `696.9` | `674.5` | `0.968` | `thr` `544.152` (`0.271` c) | `thr` `525.780` (`0.271` c a share) | `0.998` | `0.998569448148551` |
| `front` | `268.45` | `278.43` | `1.037` | `2,441.6` | `2,231.2` | `0.914` | `δ · Sh − thr` `3,035.903` (`0.432` c) | `δ · Sh − thr` `2,726.942` (`0.424` c a share) | `above 0.99999` | `1.0` |

The power is TZ-23's normal approximation at the largest variance the outcomes allow — against half a tick a share for
`behind`'s EARN, against nothing for `front`'s NO EARN. **No row of §4.5 reads a power.**

**G-BOOK** — PASS: over every book frame of the members' legs' Up token but a subscription's, **418,535
match frames, the rebuilt touch equal to the venue's own at 417,728 — `0.998071845843`, 99.81%**,
against the floor of 99 in 100; 807 differed. Barred: every level equal at 414,284
(`0.989843143345`, 98.98%). Matches read 415,916, two-sided 1,553; sessions
(subscriptions) 390, closes 390. TZ-27's 51 windows read `68,652` of `68,677` and the stand-in's 48 `67,282`
of `67,389` (§4's table).

**The capture's lag** — a `price_change` frame's host receipt less its venue stamp, over 288 members and
37,049,296 frames of the legs: the median member's median 17 ms; its 99th percentile 106 ms at
the median member and 5,595 ms at the worst, above 1,000 ms at 6 members; the longest
5,886 ms, the least 5 ms.

The units, concatenated: `replay/w1-units.txt`, 930,762 lines, 47,636,864 bytes,
`bad6b50a8d25fae2bf96f2df68ff8140ce6d4ec39ad74c83a7d15bfa631f5d60`; the constants `replay/w1-constants.json`, `5f4f43c34e74d25eed283096a50803e9b37321a15408ee072411bc3375c1dac9`. Both in `state.json` (§5.15).

### 2.2 The reading (§3.9) — `logs/80-score-1.log`, verbatim

```text
$ I score            # the first run
[2026-10-27T07:46:35Z] MemAvailable 316129280 bytes, floor 81928192; free 11680731136 bytes, floor 5400000000
[2026-10-27T07:46:36Z] unchanged /root/tz32-work/replay/w1-units.txt sha256 bad6b50a8d25fae2bf96f2df68ff8140ce6d4ec39ad74c83a7d15bfa631f5d60
[2026-10-27T07:46:36Z] wrote /root/tz32-work/replay/w1-scored.csv 45369 bytes sha256 c9c93f1160a5ffd2851a48ca918301749c189927851b665c731aa0a60896da14
[2026-10-27T07:46:36Z] wrote /root/tz32-work/replay/w1-reading.json 13761 bytes sha256 0f65737830d7b1e3218e4351c160cb82e3f8715e776e06b2d74d3d41dbb5baa7
[2026-10-27T07:46:36Z] labels: 288 members, 136 Up
[2026-10-27T07:46:36Z] behind: S -2271.140265495520 = settlement -2792.574000000000 + rebate 521.433734504480 on 194269.530000000000 shares; per share -0.011690666393 = -0.014374740084 + 0.002684073691
[2026-10-27T07:46:36Z] behind: NO EARN; EARN False (margin -2796.920062992179); NO EARN True (margin 2716.708117998861)
[2026-10-27T07:46:36Z] barred: behind band w0   shares 52570.290000000000, S -542.247259440000, per share -0.010314709305
[2026-10-27T07:46:36Z] barred: behind band w1   shares 43066.970000000000, S -309.293924192000, per share -0.007181696883
[2026-10-27T07:46:36Z] barred: behind band w2   shares 41719.690000000000, S -684.507976804000, per share -0.016407312154
[2026-10-27T07:46:36Z] barred: behind band w3   shares 38264.790000000000, S -406.933622586980, per share -0.010634675444
[2026-10-27T07:46:36Z] barred: behind band last shares 18647.790000000000, S -328.157482472540, per share -0.017597660767
[2026-10-27T07:46:36Z] barred: behind fills at a match shares 193276.950000000000, S -2281.385012979520, per share -0.011803709718
[2026-10-27T07:46:36Z] barred: behind fills against a crossing order shares 992.580000000000, S 10.244747484000, per share 0.010321331766
[2026-10-27T07:46:36Z] barred: behind per member S min -30.213465682000, median -6.989981214000, max 10.509095780000; above zero 31, below 257
[2026-10-27T07:46:36Z] front: S 506.688981636280 = settlement -1186.672240000000 + rebate 1693.361221636280 on 642581.620000000000 shares; per share 0.000788520813 = -0.001846726086 + 0.002635246899
[2026-10-27T07:46:36Z] front: EARN; EARN True (margin 20.723295059447); NO EARN True (margin 2220.253431786887)
[2026-10-27T07:46:36Z] barred: front band w0   shares 182743.940000000000, S 453.226440362000, per share 0.002480117482
[2026-10-27T07:46:36Z] barred: front band w1   shares 149817.470000000000, S 109.974903734000, per share 0.000734059277
[2026-10-27T07:46:36Z] barred: front band w2   shares 141996.420000000000, S 38.550968480000, per share 0.000271492538
[2026-10-27T07:46:36Z] barred: front band w3   shares 118814.570000000000, S -88.932233584720, per share -0.000748496027
[2026-10-27T07:46:36Z] barred: front band last shares 49209.220000000000, S -6.131097355000, per share -0.000124592451
[2026-10-27T07:46:36Z] barred: front fills at a match shares 642581.620000000000, S 506.688981636280, per share 0.000788520813
[2026-10-27T07:46:36Z] barred: front per member S min -23.880894314000, median 0.966514124000, max 44.491304678000; above zero 163, below 125
[2026-10-27T07:46:36Z] prop, barred from every reading: S -2439.015226601500 = settlement -3131.182930000000 + rebate 692.167703398500 on 259489.790000000000 shares; per share -0.009399272421 = -0.012066690293 + 0.002667417872
[2026-10-27T07:46:36Z] barred: prop band w0   shares 71396.710000000000, S -469.298509152000, per share -0.006573111130
[2026-10-27T07:46:36Z] barred: prop band w1   shares 60816.670000000000, S -468.469268652000, per share -0.007702974672
[2026-10-27T07:46:36Z] barred: prop band w2   shares 57835.460000000000, S -628.993596766000, per share -0.010875570053
[2026-10-27T07:46:36Z] barred: prop band w3   shares 48620.990000000000, S -491.113163122820, per share -0.010100846633
[2026-10-27T07:46:36Z] barred: prop band last shares 20819.960000000000, S -381.140688908680, per share -0.018306504379
[2026-10-27T07:46:36Z] barred: prop fills at a match shares 258764.830000000000, S -2447.513079389500, per share -0.009458445645
[2026-10-27T07:46:36Z] barred: prop fills against a crossing order shares 724.960000000000, S 8.497852788000, per share 0.011721822981
[2026-10-27T07:46:36Z] barred: prop per member S min -35.062444068000, median -7.567118862000, max 13.746379374000; above zero 19, below 269
[2026-10-27T07:46:36Z] behind_nocross, barred from every reading: S -2260.947329959920 = settlement -2779.923300000000 + rebate 518.975970040080 on 193374.640000000000 shares; per share -0.011692057086 = -0.014375842148 + 0.002683785061
[2026-10-27T07:46:36Z] barred: behind_nocross band w0   shares 52302.860000000000, S -522.229189960000, per share -0.009984715749
[2026-10-27T07:46:36Z] barred: behind_nocross band w1   shares 42888.460000000000, S -327.330748664000, per share -0.007632140409
[2026-10-27T07:46:36Z] barred: behind_nocross band w2   shares 41504.990000000000, S -670.955008306000, per share -0.016165646789
[2026-10-27T07:46:36Z] barred: behind_nocross band w3   shares 38047.840000000000, S -412.999244010980, per share -0.010854735617
[2026-10-27T07:46:36Z] barred: behind_nocross band last shares 18630.490000000000, S -327.433139018940, per share -0.017575122233
[2026-10-27T07:46:36Z] barred: behind_nocross fills at a match shares 193374.640000000000, S -2260.947329959920, per share -0.011692057086
[2026-10-27T07:46:36Z] barred: behind_nocross per member S min -30.889787954000, median -7.038688904000, max 11.189689006000; above zero 29, below 259
[2026-10-27T07:46:36Z] front_cross, barred from every reading: S 504.994555522280 = settlement -1189.211340000000 + rebate 1694.205895522280 on 642891.570000000000 shares; per share 0.000785505020 = -0.001849785245 + 0.002635290264
[2026-10-27T07:46:36Z] barred: front_cross band w0   shares 182855.810000000000, S 447.573933270000, per share 0.002447687789
[2026-10-27T07:46:36Z] barred: front_cross band w1   shares 149858.360000000000, S 118.082633016000, per share 0.000787961599
[2026-10-27T07:46:36Z] barred: front_cross band w2   shares 142052.960000000000, S 32.181236904000, per share 0.000226543938
[2026-10-27T07:46:36Z] barred: front_cross band w3   shares 118869.280000000000, S -83.549800694720, per share -0.000702871261
[2026-10-27T07:46:36Z] barred: front_cross band last shares 49255.160000000000, S -9.293446973000, per share -0.000188679663
[2026-10-27T07:46:36Z] barred: front_cross fills at a match shares 642461.140000000000, S 503.829383920280, per share 0.000784217679
[2026-10-27T07:46:36Z] barred: front_cross fills against a crossing order shares 430.430000000000, S 1.165171602000, per share 0.002706994406
[2026-10-27T07:46:36Z] barred: front_cross per member S min -23.880894314000, median 0.967451994000, max 44.491304678000; above zero 161, below 127
[2026-10-27T07:46:36Z] L0, barred from every reading: S -1728.211852595360 = settlement -2305.390660000000 + rebate 577.178807404640 on 216663.720000000000 shares; per share -0.007976470877 = -0.010640409294 + 0.002663938418
[2026-10-27T07:46:36Z] barred: L0 band w0   shares 57235.750000000000, S -471.509193576000, per share -0.008238018958
[2026-10-27T07:46:36Z] barred: L0 band w1   shares 46735.060000000000, S -95.236580068000, per share -0.002037797321
[2026-10-27T07:46:36Z] barred: L0 band w2   shares 46237.900000000000, S -606.014111108000, per share -0.013106436735
[2026-10-27T07:46:36Z] barred: L0 band w3   shares 43288.990000000000, S -330.427278212500, per share -0.007633055847
[2026-10-27T07:46:36Z] barred: L0 band last shares 23166.020000000000, S -225.024689630860, per share -0.009713567097
[2026-10-27T07:46:36Z] barred: L0 fills at a match shares 216036.290000000000, S -1726.010853325360, per share -0.007989448686
[2026-10-27T07:46:36Z] barred: L0 fills against a crossing order shares 627.430000000000, S -2.200999270000, per share -0.003507959884
[2026-10-27T07:46:36Z] barred: L0 per member S min -30.860727684000, median -5.211343954000, max 10.794599690000; above zero 55, below 233
[2026-10-27T07:46:36Z] L100, barred from every reading: S -2401.046235768060 = settlement -2887.793530000000 + rebate 486.747294231940 on 181281.890000000000 shares; per share -0.013244821288 = -0.015929851184 + 0.002685029896
[2026-10-27T07:46:36Z] barred: L100 band w0   shares 49129.740000000000, S -555.261835348000, per share -0.011301949397
[2026-10-27T07:46:36Z] barred: L100 band w1   shares 41204.550000000000, S -468.344409562000, per share -0.011366327494
[2026-10-27T07:46:36Z] barred: L100 band w2   shares 39481.990000000000, S -596.808698638000, per share -0.015115973097
[2026-10-27T07:46:36Z] barred: L100 band w3   shares 35580.350000000000, S -556.498579211780, per share -0.015640615655
[2026-10-27T07:46:36Z] barred: L100 band last shares 15885.260000000000, S -224.132713008280, per share -0.014109477151
[2026-10-27T07:46:36Z] barred: L100 fills at a match shares 178963.950000000000, S -2414.603440876060, per share -0.013492121966
[2026-10-27T07:46:36Z] barred: L100 fills against a crossing order shares 2317.940000000000, S 13.557205108000, per share 0.005848816237
[2026-10-27T07:46:36Z] barred: L100 per member S min -32.967654724000, median -8.110388908000, max 9.549321120000; above zero 30, below 258
[2026-10-27T07:46:36Z] L250, barred from every reading: S -2759.673231419840 = settlement -3261.635840000000 + rebate 501.962608580160 on 185308.940000000000 shares; per share -0.014892283294 = -0.017601071163 + 0.002708787868
[2026-10-27T07:46:36Z] barred: L250 band w0   shares 50219.150000000000, S -629.101394652000, per share -0.012527121519
[2026-10-27T07:46:36Z] barred: L250 band w1   shares 44578.710000000000, S -587.905810688000, per share -0.013188040001
[2026-10-27T07:46:36Z] barred: L250 band w2   shares 42297.420000000000, S -708.627073818000, per share -0.016753434933
[2026-10-27T07:46:36Z] barred: L250 band w3   shares 35588.960000000000, S -619.195526998900, per share -0.017398528280
[2026-10-27T07:46:36Z] barred: L250 band last shares 12624.700000000000, S -214.843425262940, per share -0.017017705392
[2026-10-27T07:46:36Z] barred: L250 fills at a match shares 133011.040000000000, S -2259.630837281240, per share -0.016988295387
[2026-10-27T07:46:36Z] barred: L250 fills against a crossing order shares 52297.900000000000, S -500.042394138600, per share -0.009561423960
[2026-10-27T07:46:36Z] barred: L250 per member S min -33.866260874000, median -9.194931254000, max 28.417225846000; above zero 12, below 276
[2026-10-27T07:46:36Z] front_L0, barred from every reading: S 1212.083755907120 = settlement -902.174800000000 + rebate 2114.258555907120 on 802213.160000000000 shares; per share 0.001510924797 = -0.001124607330 + 0.002635532127
[2026-10-27T07:46:36Z] barred: front_L0 band w0   shares 220080.520000000000, S 507.337784900000, per share 0.002305237124
[2026-10-27T07:46:36Z] barred: front_L0 band w1   shares 178776.890000000000, S 272.525677384000, per share 0.001524389855
[2026-10-27T07:46:36Z] barred: front_L0 band w2   shares 173051.460000000000, S 110.228497640000, per share 0.000636969475
[2026-10-27T07:46:36Z] barred: front_L0 band w3   shares 155213.080000000000, S 174.663890805440, per share 0.001125316828
[2026-10-27T07:46:36Z] barred: front_L0 band last shares 75091.210000000000, S 147.327905177680, per share 0.001961986032
[2026-10-27T07:46:36Z] barred: front_L0 fills at a match shares 802213.160000000000, S 1212.083755907120, per share 0.001510924797
[2026-10-27T07:46:36Z] barred: front_L0 per member S min -16.683740626000, median 2.577581820000, max 66.667199010000; above zero 188, below 100
[2026-10-27T07:46:36Z] the score's files: /root/tz32-work/replay/w1-scored.csv sha256 c9c93f1160a5ffd2851a48ca918301749c189927851b665c731aa0a60896da14; /root/tz32-work/replay/w1-reading.json sha256 0f65737830d7b1e3218e4351c160cb82e3f8715e776e06b2d74d3d41dbb5baa7
[2026-10-27T07:46:36Z] W1 READING: W1-NO-EARN
[2026-10-27T07:46:36Z] malloc tuned: True
[2026-10-27T07:46:36Z] peak memory of this run: 54984704 bytes
[2026-10-27T07:46:36Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

Every variant's `S`, its parts and `S` a share, and its per-member extremes — barred from every reading but `behind`'s
`S` for W1-EARN and `front`'s for W1-NO-EARN:

| variant | role | `S` | at settlement | rebate | shares | `S` a share | settlement a share | rebate a share | per member min | median | max | above 0 | below 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `behind` | gated | `−2,271.140` | `−2,792.574` | `521.434` | `194,269.530000000000` | `−1.169` c | `−1.437` c | `0.268` c | `−30.213` | `−6.990` | `10.509` | 31 | 257 |
| `front` | gated | `506.689` | `−1,186.672` | `1,693.361` | `642,581.620000000000` | `0.079` c | `−0.185` c | `0.264` c | `−23.881` | `0.967` | `44.491` | 163 | 125 |
| `prop` | barred | `−2,439.015` | `−3,131.183` | `692.168` | `259,489.790000000000` | `−0.940` c | `−1.207` c | `0.267` c | `−35.062` | `−7.567` | `13.746` | 19 | 269 |
| `behind_nocross` | barred | `−2,260.947` | `−2,779.923` | `518.976` | `193,374.640000000000` | `−1.169` c | `−1.438` c | `0.268` c | `−30.890` | `−7.039` | `11.190` | 29 | 259 |
| `front_cross` | barred | `504.995` | `−1,189.211` | `1,694.206` | `642,891.570000000000` | `0.079` c | `−0.185` c | `0.264` c | `−23.881` | `0.967` | `44.491` | 161 | 127 |
| `L0` | barred | `−1,728.212` | `−2,305.391` | `577.179` | `216,663.720000000000` | `−0.798` c | `−1.064` c | `0.266` c | `−30.861` | `−5.211` | `10.795` | 55 | 233 |
| `L100` | barred | `−2,401.046` | `−2,887.794` | `486.747` | `181,281.890000000000` | `−1.324` c | `−1.593` c | `0.269` c | `−32.968` | `−8.110` | `9.549` | 30 | 258 |
| `L250` | barred | `−2,759.673` | `−3,261.636` | `501.963` | `185,308.940000000000` | `−1.489` c | `−1.760` c | `0.271` c | `−33.866` | `−9.195` | `28.417` | 12 | 276 |
| `front_L0` | barred | `1,212.084` | `−902.175` | `2,114.259` | `802,213.160000000000` | `0.151` c | `−0.112` c | `0.264` c | `−16.684` | `2.578` | `66.667` | 188 | 100 |

Barred, each band's and each kind's — the bands of the leg's five minutes as TZ-23's `aggregate` cuts them, and the
fills at a match against those against a crossing order:

| variant | band or kind | shares | `S` | `S` a share |
|---|---|---|---|---|
| `behind` | band `w0` | `52,570.290000000000` | `−542.247` | `−1.031` c |
| `behind` | band `w1` | `43,066.970000000000` | `−309.294` | `−0.718` c |
| `behind` | band `w2` | `41,719.690000000000` | `−684.508` | `−1.641` c |
| `behind` | band `w3` | `38,264.790000000000` | `−406.934` | `−1.063` c |
| `behind` | band `last` | `18,647.790000000000` | `−328.157` | `−1.760` c |
| `behind` | fills at a match | `193,276.950000000000` | `−2,281.385` | `−1.180` c |
| `behind` | fills against a crossing order | `992.580000000000` | `10.245` | `1.032` c |
| `front` | band `w0` | `182,743.940000000000` | `453.226` | `0.248` c |
| `front` | band `w1` | `149,817.470000000000` | `109.975` | `0.073` c |
| `front` | band `w2` | `141,996.420000000000` | `38.551` | `0.027` c |
| `front` | band `w3` | `118,814.570000000000` | `−88.932` | `−0.075` c |
| `front` | band `last` | `49,209.220000000000` | `−6.131` | `−0.012` c |
| `front` | fills at a match | `642,581.620000000000` | `506.689` | `0.079` c |
| `prop` | band `w0` | `71,396.710000000000` | `−469.299` | `−0.657` c |
| `prop` | band `w1` | `60,816.670000000000` | `−468.469` | `−0.770` c |
| `prop` | band `w2` | `57,835.460000000000` | `−628.994` | `−1.088` c |
| `prop` | band `w3` | `48,620.990000000000` | `−491.113` | `−1.010` c |
| `prop` | band `last` | `20,819.960000000000` | `−381.141` | `−1.831` c |
| `prop` | fills at a match | `258,764.830000000000` | `−2,447.513` | `−0.946` c |
| `prop` | fills against a crossing order | `724.960000000000` | `8.498` | `1.172` c |
| `behind_nocross` | band `w0` | `52,302.860000000000` | `−522.229` | `−0.998` c |
| `behind_nocross` | band `w1` | `42,888.460000000000` | `−327.331` | `−0.763` c |
| `behind_nocross` | band `w2` | `41,504.990000000000` | `−670.955` | `−1.617` c |
| `behind_nocross` | band `w3` | `38,047.840000000000` | `−412.999` | `−1.085` c |
| `behind_nocross` | band `last` | `18,630.490000000000` | `−327.433` | `−1.758` c |
| `behind_nocross` | fills at a match | `193,374.640000000000` | `−2,260.947` | `−1.169` c |
| `front_cross` | band `w0` | `182,855.810000000000` | `447.574` | `0.245` c |
| `front_cross` | band `w1` | `149,858.360000000000` | `118.083` | `0.079` c |
| `front_cross` | band `w2` | `142,052.960000000000` | `32.181` | `0.023` c |
| `front_cross` | band `w3` | `118,869.280000000000` | `−83.550` | `−0.070` c |
| `front_cross` | band `last` | `49,255.160000000000` | `−9.293` | `−0.019` c |
| `front_cross` | fills at a match | `642,461.140000000000` | `503.829` | `0.078` c |
| `front_cross` | fills against a crossing order | `430.430000000000` | `1.165` | `0.271` c |
| `L0` | band `w0` | `57,235.750000000000` | `−471.509` | `−0.824` c |
| `L0` | band `w1` | `46,735.060000000000` | `−95.237` | `−0.204` c |
| `L0` | band `w2` | `46,237.900000000000` | `−606.014` | `−1.311` c |
| `L0` | band `w3` | `43,288.990000000000` | `−330.427` | `−0.763` c |
| `L0` | band `last` | `23,166.020000000000` | `−225.025` | `−0.971` c |
| `L0` | fills at a match | `216,036.290000000000` | `−1,726.011` | `−0.799` c |
| `L0` | fills against a crossing order | `627.430000000000` | `−2.201` | `−0.351` c |
| `L100` | band `w0` | `49,129.740000000000` | `−555.262` | `−1.130` c |
| `L100` | band `w1` | `41,204.550000000000` | `−468.344` | `−1.137` c |
| `L100` | band `w2` | `39,481.990000000000` | `−596.809` | `−1.512` c |
| `L100` | band `w3` | `35,580.350000000000` | `−556.499` | `−1.564` c |
| `L100` | band `last` | `15,885.260000000000` | `−224.133` | `−1.411` c |
| `L100` | fills at a match | `178,963.950000000000` | `−2,414.603` | `−1.349` c |
| `L100` | fills against a crossing order | `2,317.940000000000` | `13.557` | `0.585` c |
| `L250` | band `w0` | `50,219.150000000000` | `−629.101` | `−1.253` c |
| `L250` | band `w1` | `44,578.710000000000` | `−587.906` | `−1.319` c |
| `L250` | band `w2` | `42,297.420000000000` | `−708.627` | `−1.675` c |
| `L250` | band `w3` | `35,588.960000000000` | `−619.196` | `−1.740` c |
| `L250` | band `last` | `12,624.700000000000` | `−214.843` | `−1.702` c |
| `L250` | fills at a match | `133,011.040000000000` | `−2,259.631` | `−1.699` c |
| `L250` | fills against a crossing order | `52,297.900000000000` | `−500.042` | `−0.956` c |
| `front_L0` | band `w0` | `220,080.520000000000` | `507.338` | `0.231` c |
| `front_L0` | band `w1` | `178,776.890000000000` | `272.526` | `0.152` c |
| `front_L0` | band `w2` | `173,051.460000000000` | `110.228` | `0.064` c |
| `front_L0` | band `w3` | `155,213.080000000000` | `174.664` | `0.113` c |
| `front_L0` | band `last` | `75,091.210000000000` | `147.328` | `0.196` c |
| `front_L0` | fills at a match | `802,213.160000000000` | `1,212.084` | `0.151` c |

### 2.3 G-REHEARSAL (§3.5) — `logs/50-rehearse.log`, verbatim

```text
$ I rehearse
[2026-10-27T06:59:38Z] MemAvailable 360185856 bytes, floor 81928192; free 11859652608 bytes, floor 5400000000
[2026-10-27T07:00:15Z] wrote /root/tz32-work/rehearsal/docs.json 27592 bytes sha256 22f16a747624cbc497756d27ea7574485cba8b68ff95277ac4025041aa724afd
[2026-10-27T07:00:15Z] units to replay 51, 678739504 bytes of streams in all
[2026-10-27T07:01:51Z] projected 131 s of replay for 678739504 bytes after 24 units at 0.1925 s a megabyte
[2026-10-27T07:01:51Z] units 24 this run, 96 s
[2026-10-27T07:03:07Z] units 48 this run, 171 s
[2026-10-27T07:03:19Z] units 51: inside the idle stretch 51, ending after second 590 0; longest 6.5 s, download 1.9 s and replay 5.3 s at most; 0 s waited; processor 131.6 s; 678739504 bytes downloaded; retries 0; windows 2026-10-27T07:00:00Z to 2026-10-27T07:00:00Z
[2026-10-27T07:03:19Z] wrote /root/tz32-work/rehearsal/rehearsal-lines.txt 7008141 bytes sha256 52b1c637a51d6b7af3c29ba3aadd75a5e2f0d39410969ee15b61155a4fc3ac60
[2026-10-27T07:03:19Z] G-REHEARSAL behind   [7219, '29749.980000000000', '148.620000000000', '186.702990000000', '73.284744755460', '14541.894000000000', '-314.048245244540']; the Architect's [7219, '29749.980000000000', '148.620000000000', '186.702990000000', '73.284744755460', '14541.894000000000', '-314.048245244540']
[2026-10-27T07:03:19Z] G-REHEARSAL front    [26214, '99744.330000000000', '52.850000000000', '88.478290000000', '244.042849013460', '14316.016700000000', '-16.225440986540']; the Architect's [26214, '99744.330000000000', '52.850000000000', '88.478290000000', '244.042849013460', '14316.016700000000', '-16.225440986540']
[2026-10-27T07:03:19Z] G-REHEARSAL prop     [10076, '38817.950000000000', '108.130000000000', '150.934090000000', '94.534436869460', '15627.275900000000', '-301.729653130540']; the Architect's [10076, '38817.950000000000', '108.130000000000', '150.934090000000', '94.534436869460', '15627.275900000000', '-301.729653130540']
[2026-10-27T07:03:19Z] G-REHEARSAL behind_nocross [7188, '29598.260000000000', '141.500000000000', '176.187790000000', '72.852862339460', '14476.772200000000', '-307.324927660540']; the Architect's [7188, '29598.260000000000', '141.500000000000', '176.187790000000', '72.852862339460', '14476.772200000000', '-307.324927660540']
[2026-10-27T07:03:19Z] G-REHEARSAL front_cross [26232, '99839.700000000000', '46.180000000000', '85.580190000000', '244.315285023460', '13867.026400000000', '-9.624904976540']; the Architect's [26232, '99839.700000000000', '46.180000000000', '85.580190000000', '244.315285023460', '13867.026400000000', '-9.624904976540']
[2026-10-27T07:03:19Z] G-REHEARSAL L0       [9236, '37841.480000000000', '120.560000000000', '246.148810000000', '92.467183565260', '13402.157600000000', '-295.291626434740']; the Architect's [9236, '37841.480000000000', '120.560000000000', '246.148810000000', '92.467183565260', '13402.157600000000', '-295.291626434740']
[2026-10-27T07:03:19Z] G-REHEARSAL L100     [6410, '26551.630000000000', '172.350000000000', '117.943900000000', '65.091487813800', '15468.213300000000', '-264.942412186200']; the Architect's [6410, '26551.630000000000', '172.350000000000', '117.943900000000', '65.091487813800', '15468.213300000000', '-264.942412186200']
[2026-10-27T07:03:19Z] G-REHEARSAL L250     [6636, '28849.690000000000', '57.350000000000', '-59.683100000000', '71.022929390000', '16803.875300000000', '-242.283970610000']; the Architect's [6636, '28849.690000000000', '57.350000000000', '-59.683100000000', '71.022929390000', '16803.875300000000', '-242.283970610000']
[2026-10-27T07:03:19Z] G-REHEARSAL front_L0 [32813, '126600.190000000000', '81.090000000000', '153.311610000000', '311.240369556060', '13631.537300000000', '17.878759556060']; the Architect's [32813, '126600.190000000000', '81.090000000000', '153.311610000000', '311.240369556060', '13631.537300000000', '17.878759556060']
[2026-10-27T07:03:19Z] G-REHEARSAL lines 135900, the Architect's 135900; sha256 52b1c637a51d6b7af3c29ba3aadd75a5e2f0d39410969ee15b61155a4fc3ac60, the Architect's 52b1c637a51d6b7af3c29ba3aadd75a5e2f0d39410969ee15b61155a4fc3ac60
[2026-10-27T07:03:19Z] G-REHEARSAL PASS: 11 of 11 - 135900 lines byte for byte and 9 variants' totals equal to the Architect's
[2026-10-27T07:03:19Z] malloc tuned: True
[2026-10-27T07:03:19Z] peak memory of this run: 42799104 bytes
[2026-10-27T07:03:19Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

### 2.4 The archive's record (§3.4, V5) — `logs/40-archive.log`, verbatim

```text
$ I archive
[2026-10-27T06:59:25Z] btc-pairbook-archive.timer {'NextElapseUSecRealtime': 'Wed 2026-10-28 03:00:20 UTC', 'LastTriggerUSec': 'Tue 2026-10-27 06:25:40 UTC', 'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-27T06:59:25Z] btc-pairbook-archive.service {'Result': 'success', 'ExecMainStatus': '0', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-27T06:59:25Z] ledger /var/lib/btc-pairbook-archive/ledger.jsonl: 64237 bytes sha256 c066f771d34694fc73235bd28b0ff5088f7c00c9815562d3cbe97548cbba0635, 270 complete records, 0 bytes of a line still written
[2026-10-27T06:59:25Z] L 2026-10-11T15:18:12Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "2a4b998acb9f4883b26999bb278624bf", "phase_at": 192, "resumed": false, "run": 1791731892, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791731892810556801}
[2026-10-27T06:59:25Z] L 2026-10-11T15:18:13Z {"assets_n": 28, "bytes_total": 430047476, "closed": 79, "deferred": 0, "event": "set", "first_T": 1791706500, "last_T": 1791730800, "open": 0, "run": 1791731892, "sha256": "ec3983419485fa67317468917eb7b60e2d0e529be4334c7297831ff562471ad0", "tag": "pairbook-streams-1791731892", "unclosed": 0, "wall_ns": 1791731893762719408, "windows_considered": 79}
[2026-10-27T06:59:25Z] L 2026-10-11T15:18:57Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 409746510, "run": 1791731892, "sent": 28, "wall_ns": 1791731937181037882}
[2026-10-27T06:59:25Z] L 2026-10-11T15:21:30Z {"assets_n": 28, "bytes_total": 430047476, "event": "verify", "release_id": 409746510, "run": 1791731892, "verify_sha256": "032adfdbaea0b81d7ea5063eb43130c09396908f05d74be0f1818d2bb2342f64", "wall_ns": 1791732090814504593}
[2026-10-27T06:59:25Z] L 2026-10-11T15:21:31Z {"already": 0, "event": "delete", "free_after": 12969091072, "free_before": 12538937344, "freed": 430047476, "gone": 28, "removed": 28, "run": 1791731892, "wall_ns": 1791732091732399708, "windows_kept": 28}
[2026-10-27T06:59:25Z] L 2026-10-11T15:21:31Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "815823", "NRestarts": "2", "ns": 1791732091741955625}, "phase": 391, "run": 1791731892, "wall_ns": 1791732091741960838}
[2026-10-27T06:59:25Z] L 2026-10-11T15:21:31Z {"event": "kill", "exit": 0, "phase": 391, "run": 1791731892, "wall_ns": 1791732091746593097}
[2026-10-27T06:59:25Z] L 2026-10-11T15:22:01Z {"NRestarts": "3", "W": 1791731700, "event": "restart", "free_bytes": 12969062400, "gap_ns": 5548461176, "pid": 851381, "run": 1791731892, "stopped": 815823, "stream_bytes": 0, "wall_ns": 1791732121761569347}
[2026-10-27T06:59:25Z] L 2026-10-11T15:30:41Z {"T": 1791731700, "event": "resume", "reading": "PASS", "run": 1791731892, "wall_ns": 1791732641000772037}
[2026-10-27T06:59:25Z] L 2026-10-11T15:30:41Z {"assets_n": 28, "bytes_total": 430047476, "ended_outside": 0, "event": "complete", "free_bytes": 12949487616, "peak_rss": 36884480, "rate_per_day": 1474448489, "requests": 61, "run": 1791731892, "started_outside": 0, "stops": [["the cap", 1792200292], ["the floor, base 43500000 bytes a day", 1792213576], ["the floor, base 187760570 bytes a day", 1792171837]], "store_stream_bytes": 19346486, "wall_ns": 1791732641002785194}
[2026-10-27T06:59:25Z] L 2026-10-12T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "b458725447bd4a0c865999eab0a904ad", "phase_at": 20, "resumed": false, "run": 1791774020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791774020508107799}
[2026-10-27T06:59:25Z] L 2026-10-12T03:00:22Z {"assets_n": 46, "bytes_total": 794522712, "closed": 125, "deferred": 0, "event": "set", "first_T": 1791731700, "last_T": 1791772200, "open": 1, "run": 1791774020, "sha256": "c8f02de3fbed47c4cfa91e66d774427f20990f634d271237bf3c6f25887ffb99", "tag": "pairbook-streams-1791774020", "unclosed": 0, "wall_ns": 1791774022193879442, "windows_considered": 125}
[2026-10-27T06:59:25Z] L 2026-10-12T03:01:35Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 410101186, "run": 1791774020, "sent": 46, "wall_ns": 1791774095014644950}
[2026-10-27T06:59:25Z] L 2026-10-12T03:04:44Z {"assets_n": 46, "bytes_total": 794522712, "event": "verify", "release_id": 410101186, "run": 1791774020, "verify_sha256": "0f86d9494743193ae4dd5ddb59e37a08eebc8bb7318ea4d98def44406d025aec", "wall_ns": 1791774284631917592}
[2026-10-27T06:59:25Z] L 2026-10-12T03:04:46Z {"already": 0, "event": "delete", "free_after": 12960145408, "free_before": 12165431296, "freed": 794522712, "gone": 46, "removed": 46, "run": 1791774020, "wall_ns": 1791774286328338970, "windows_kept": 46}
[2026-10-27T06:59:25Z] L 2026-10-12T03:04:46Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "851381", "NRestarts": "3", "ns": 1791774286341020683}, "phase": 286, "run": 1791774020, "wall_ns": 1791774286341025663}
[2026-10-27T06:59:25Z] L 2026-10-12T03:04:46Z {"event": "kill", "exit": 0, "phase": 286, "run": 1791774020, "wall_ns": 1791774286345765034}
[2026-10-27T06:59:25Z] L 2026-10-12T03:05:16Z {"NRestarts": "4", "W": 1791774000, "event": "restart", "free_bytes": 12960112640, "gap_ns": 5455854888, "pid": 911226, "run": 1791774020, "stopped": 851381, "stream_bytes": 25646773, "wall_ns": 1791774316361306454}
[2026-10-27T06:59:25Z] L 2026-10-12T03:15:41Z {"T": 1791774000, "event": "resume", "reading": "PASS", "run": 1791774020, "wall_ns": 1791774941000362333}
[2026-10-27T06:59:25Z] L 2026-10-12T03:15:41Z {"assets_n": 46, "bytes_total": 794522712, "ended_outside": 0, "event": "complete", "free_bytes": 12948570112, "peak_rss": 37670912, "rate_per_day": 1658134355, "requests": 97, "run": 1791774020, "started_outside": 0, "stops": [["the cap", 1792189855], ["the floor, base 43500000 bytes a day", 1792203914], ["the floor, base 187760570 bytes a day", 1792170389]], "store_stream_bytes": 37220758, "wall_ns": 1791774941002570067}
[2026-10-27T06:59:25Z] L 2026-10-13T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "5e59db817b3d42ef91641fbb34bc17cc", "phase_at": 20, "resumed": false, "run": 1791860420, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791860420531436360}
[2026-10-27T06:59:25Z] L 2026-10-13T03:00:24Z {"assets_n": 96, "bytes_total": 1925987888, "closed": 221, "deferred": 0, "event": "set", "first_T": 1791773100, "last_T": 1791858600, "open": 1, "run": 1791860420, "sha256": "de9209f2e76e5c42bd1395ea6e9c17ab0fc4c497be6a9311cd1e07c101f9b777", "tag": "pairbook-streams-1791860420", "unclosed": 0, "wall_ns": 1791860424671646762, "windows_considered": 221}
[2026-10-27T06:59:25Z] L 2026-10-13T03:03:13Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 411210796, "run": 1791860420, "sent": 96, "wall_ns": 1791860593421247948}
[2026-10-27T06:59:25Z] L 2026-10-13T03:07:31Z {"assets_n": 96, "bytes_total": 1925987888, "event": "verify", "release_id": 411210796, "run": 1791860420, "verify_sha256": "a5969978f8bfb614451c41257e7eb70a13c12126932ef03d4cfbd2f2c41ad022", "wall_ns": 1791860851109946296}
[2026-10-27T06:59:25Z] L 2026-10-13T03:07:35Z {"already": 0, "event": "delete", "free_after": 12876316672, "free_before": 10949902336, "freed": 1925987888, "gone": 96, "removed": 96, "run": 1791860420, "wall_ns": 1791860855219206873, "windows_kept": 96}
[2026-10-27T06:59:25Z] L 2026-10-13T03:07:35Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "911226", "NRestarts": "4", "ns": 1791860855230756130}, "phase": 455, "run": 1791860420, "wall_ns": 1791860855230762191}
[2026-10-27T06:59:25Z] L 2026-10-13T03:07:35Z {"event": "kill", "exit": 0, "phase": 455, "run": 1791860420, "wall_ns": 1791860855235973960}
[2026-10-27T06:59:25Z] L 2026-10-13T03:08:05Z {"NRestarts": "5", "W": 1791860400, "event": "restart", "free_bytes": 12876300288, "gap_ns": 5561093708, "pid": 1027378, "run": 1791860420, "stopped": 911226, "stream_bytes": 23131514, "wall_ns": 1791860885252051875}
[2026-10-27T06:59:25Z] L 2026-10-13T03:15:41Z {"T": 1791860400, "event": "resume", "reading": "PASS", "run": 1791860420, "wall_ns": 1791861341000349433}
[2026-10-27T06:59:25Z] L 2026-10-13T03:15:41Z {"assets_n": 96, "bytes_total": 1925987888, "ended_outside": 0, "event": "complete", "free_bytes": 12857700352, "peak_rss": 37941248, "rate_per_day": 1925987888, "requests": 197, "run": 1791860420, "started_outside": 0, "stops": [["the cap", 1792218357], ["the floor, base 43500000 bytes a day", 1792227987], ["the floor, base 187760570 bytes a day", 1792202964]], "store_stream_bytes": 41556131, "wall_ns": 1791861341004126797}
[2026-10-27T06:59:25Z] L 2026-10-14T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "f4f5335f60584baeab0eabd568d20823", "phase_at": 20, "resumed": false, "run": 1791946820, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1791946820511249708}
[2026-10-27T06:59:25Z] L 2026-10-14T03:00:24Z {"assets_n": 96, "bytes_total": 2039544263, "closed": 317, "deferred": 0, "event": "set", "first_T": 1791859500, "last_T": 1791945000, "open": 1, "run": 1791946820, "sha256": "9c78ba5221e0bc8d9d8699d920e17c58d76b6052fce7c0e86af4948bdc38aa1e", "tag": "pairbook-streams-1791946820", "unclosed": 0, "wall_ns": 1791946824807088559, "windows_considered": 317}
[2026-10-27T06:59:25Z] L 2026-10-14T03:03:21Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 412296623, "run": 1791946820, "sent": 96, "wall_ns": 1791947001852058175}
[2026-10-27T06:59:25Z] L 2026-10-14T03:07:45Z {"assets_n": 96, "bytes_total": 2039544263, "event": "verify", "release_id": 412296623, "run": 1791946820, "verify_sha256": "086fc6331ec202ef5c6b56257a52cbc12673053f82408a3cd4b3cf203ae44c95", "wall_ns": 1791947265299596860}
[2026-10-27T06:59:25Z] L 2026-10-14T03:07:49Z {"already": 0, "event": "delete", "free_after": 12842123264, "free_before": 10802130944, "freed": 2039544263, "gone": 96, "removed": 96, "run": 1791946820, "wall_ns": 1791947269716703785, "windows_kept": 96}
[2026-10-27T06:59:25Z] L 2026-10-14T03:07:49Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1027378", "NRestarts": "5", "ns": 1791947269728675162}, "phase": 469, "run": 1791946820, "wall_ns": 1791947269728680763}
[2026-10-27T06:59:25Z] L 2026-10-14T03:07:49Z {"event": "kill", "exit": 0, "phase": 469, "run": 1791946820, "wall_ns": 1791947269733842747}
[2026-10-27T06:59:25Z] L 2026-10-14T03:08:19Z {"NRestarts": "6", "W": 1791946800, "event": "restart", "free_bytes": 12842098688, "gap_ns": 5560847791, "pid": 1155982, "run": 1791946820, "stopped": 1027378, "stream_bytes": 17222124, "wall_ns": 1791947299751305660}
[2026-10-27T06:59:25Z] L 2026-10-14T03:15:41Z {"T": 1791946800, "event": "resume", "reading": "PASS", "run": 1791946820, "wall_ns": 1791947741000324294}
[2026-10-27T06:59:25Z] L 2026-10-14T03:15:41Z {"assets_n": 96, "bytes_total": 2039544263, "ended_outside": 0, "event": "complete", "free_bytes": 12820799488, "peak_rss": 38072320, "rate_per_day": 2039544263, "requests": 197, "run": 1791946820, "started_outside": 0, "stops": [["the cap", 1792285007], ["the floor, base 43500000 bytes a day", 1792292869], ["the floor, base 187760570 bytes a day", 1792270515]], "store_stream_bytes": 38533208, "wall_ns": 1791947741004939814}
[2026-10-27T06:59:25Z] L 2026-10-15T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "08fd4972db8347a4897a6ecd018049e4", "phase_at": 20, "resumed": false, "run": 1792033220, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792033220507675615}
[2026-10-27T06:59:25Z] L 2026-10-15T03:00:25Z {"assets_n": 96, "bytes_total": 2103892072, "closed": 413, "deferred": 0, "event": "set", "first_T": 1791945900, "last_T": 1792031400, "open": 1, "run": 1792033220, "sha256": "3272c87234da82333365144d0c39bb0f75e895943e7e34ec7ff1e559c1ad8715", "tag": "pairbook-streams-1792033220", "unclosed": 0, "wall_ns": 1792033225025238523, "windows_considered": 413}
[2026-10-27T06:59:25Z] L 2026-10-15T03:03:26Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 413374764, "run": 1792033220, "sent": 96, "wall_ns": 1792033406364376177}
[2026-10-27T06:59:25Z] L 2026-10-15T03:07:54Z {"assets_n": 96, "bytes_total": 2103892072, "event": "verify", "release_id": 413374764, "run": 1792033220, "verify_sha256": "ff1dbc619728c35ab3732813ed23e83065603970c79ae62379097e59b1f13fa0", "wall_ns": 1792033674329218632}
[2026-10-27T06:59:25Z] L 2026-10-15T03:07:58Z {"already": 0, "event": "delete", "free_after": 12590329856, "free_before": 10485972992, "freed": 2103892072, "gone": 96, "removed": 96, "run": 1792033220, "wall_ns": 1792033678892316224, "windows_kept": 96}
[2026-10-27T06:59:25Z] L 2026-10-15T03:15:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1155982", "NRestarts": "6", "ns": 1792034115012851485}, "phase": 15, "run": 1792033220, "wall_ns": 1792034115012856996}
[2026-10-27T06:59:25Z] L 2026-10-15T03:15:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792033220, "wall_ns": 1792034115018137811}
[2026-10-27T06:59:25Z] L 2026-10-15T03:15:45Z {"NRestarts": "7", "W": 1792034100, "event": "restart", "free_bytes": 12572676096, "gap_ns": 5531970911, "pid": 1284485, "run": 1792033220, "stopped": 1155982, "stream_bytes": 29667971, "wall_ns": 1792034145058520440}
[2026-10-27T06:59:25Z] L 2026-10-15T03:30:41Z {"T": 1792034100, "event": "resume", "reading": "PASS", "run": 1792033220, "wall_ns": 1792035041000365330}
[2026-10-27T06:59:25Z] L 2026-10-15T03:30:41Z {"assets_n": 96, "bytes_total": 2103892072, "ended_outside": 0, "event": "complete", "free_bytes": 12548313088, "peak_rss": 38199296, "rate_per_day": 2103892072, "requests": 197, "run": 1792033220, "started_outside": 0, "stops": [["the cap", 1792361344], ["the floor, base 43500000 bytes a day", 1792358863], ["the floor, base 187760570 bytes a day", 1792338478]], "store_stream_bytes": 54308421, "wall_ns": 1792035041006683547}
[2026-10-27T06:59:25Z] L 2026-10-15T06:18:30Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "1fd2e68b26a04a328b7551cbafc2eabe", "phase_at": 210, "resumed": false, "run": 1792045110, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792045110608854708}
[2026-10-27T06:59:25Z] L 2026-10-15T06:18:31Z {"assets_n": 14, "bytes_total": 352241341, "closed": 427, "deferred": 0, "event": "set", "first_T": 1792032300, "last_T": 1792044000, "open": 0, "run": 1792045110, "sha256": "0337b76512886f5dd78d71cfb303a343631f73624e2eb539ed79ed7f32cc0b8e", "tag": "pairbook-streams-1792045110", "unclosed": 0, "wall_ns": 1792045111425201892, "windows_considered": 427}
[2026-10-27T06:59:25Z] L 2026-10-15T06:19:00Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 413477311, "run": 1792045110, "sent": 14, "wall_ns": 1792045140771279777}
[2026-10-27T06:59:25Z] L 2026-10-15T06:21:20Z {"assets_n": 14, "bytes_total": 352241341, "event": "verify", "release_id": 413477311, "run": 1792045110, "verify_sha256": "52fc16f3058d99f3207b8fe2e61473302a0f89a9e1a2e0f5c8eb71f413e8e379", "wall_ns": 1792045280782420614}
[2026-10-27T06:59:25Z] L 2026-10-15T06:21:21Z {"already": 0, "event": "delete", "free_after": 12826914816, "free_before": 12474617856, "freed": 352241341, "gone": 14, "removed": 14, "run": 1792045110, "wall_ns": 1792045281527345757, "windows_kept": 14}
[2026-10-27T06:59:25Z] L 2026-10-15T06:21:21Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1284485", "NRestarts": "7", "ns": 1792045281539516731}, "phase": 381, "run": 1792045110, "wall_ns": 1792045281539522189}
[2026-10-27T06:59:25Z] L 2026-10-15T06:21:21Z {"event": "kill", "exit": 0, "phase": 381, "run": 1792045110, "wall_ns": 1792045281543696309}
[2026-10-27T06:59:25Z] L 2026-10-15T06:21:51Z {"NRestarts": "8", "W": 1792044900, "event": "restart", "free_bytes": 12826902528, "gap_ns": 5495918230, "pid": 1312748, "run": 1792045110, "stopped": 1284485, "stream_bytes": 0, "wall_ns": 1792045311558979330}
[2026-10-27T06:59:25Z] L 2026-10-15T06:30:41Z {"T": 1792044900, "event": "resume", "reading": "PASS", "run": 1792045110, "wall_ns": 1792045841024547052}
[2026-10-27T06:59:25Z] L 2026-10-15T06:30:41Z {"assets_n": 14, "bytes_total": 352241341, "ended_outside": 0, "event": "complete", "free_bytes": 12813713408, "peak_rss": 37543936, "rate_per_day": 2415369195, "requests": 33, "run": 1792045110, "started_outside": 0, "stops": [["the cap", 1792331549], ["the floor, base 43500000 bytes a day", 1792337969], ["the floor, base 187760570 bytes a day", 1792321779]], "store_stream_bytes": 12817136, "wall_ns": 1792045841098825002}
[2026-10-27T06:59:25Z] L 2026-10-16T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "5fd01e0598954380beeca3f3ac4c3f62", "phase_at": 20, "resumed": false, "run": 1792119620, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792119620165748278}
[2026-10-27T06:59:25Z] L 2026-10-16T03:00:24Z {"assets_n": 82, "bytes_total": 1804368058, "closed": 509, "deferred": 0, "event": "set", "first_T": 1792044900, "last_T": 1792117800, "open": 1, "run": 1792119620, "sha256": "adc52d666ace24c2145e55ef9d62602717d7726c791319304613be33c58459b6", "tag": "pairbook-streams-1792119620", "unclosed": 0, "wall_ns": 1792119624014812901, "windows_considered": 509}
[2026-10-27T06:59:25Z] L 2026-10-16T03:02:57Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 414488168, "run": 1792119620, "sent": 82, "wall_ns": 1792119777429141022}
[2026-10-27T06:59:25Z] L 2026-10-16T03:07:24Z {"assets_n": 82, "bytes_total": 1804368058, "event": "verify", "release_id": 414488168, "run": 1792119620, "verify_sha256": "96164ee15cef51426beba1050e8a4f47856762d5800a75fe9966f68164302e2a", "wall_ns": 1792120044830268724}
[2026-10-27T06:59:25Z] L 2026-10-16T03:07:28Z {"already": 0, "event": "delete", "free_after": 12728901632, "free_before": 10924134400, "freed": 1804368058, "gone": 82, "removed": 82, "run": 1792119620, "wall_ns": 1792120048628416638, "windows_kept": 82}
[2026-10-27T06:59:25Z] L 2026-10-16T03:07:28Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1312748", "NRestarts": "8", "ns": 1792120048640224099}, "phase": 448, "run": 1792119620, "wall_ns": 1792120048640229054}
[2026-10-27T06:59:25Z] L 2026-10-16T03:07:28Z {"event": "kill", "exit": 0, "phase": 448, "run": 1792119620, "wall_ns": 1792120048645966122}
[2026-10-27T06:59:25Z] L 2026-10-16T03:07:58Z {"NRestarts": "9", "W": 1792119600, "event": "restart", "free_bytes": 12728885248, "gap_ns": 5420693633, "pid": 1420617, "run": 1792119620, "stopped": 1312748, "stream_bytes": 12133793, "wall_ns": 1792120078665650185}
[2026-10-27T06:59:25Z] L 2026-10-16T03:15:41Z {"T": 1792119600, "event": "resume", "reading": "PASS", "run": 1792119620, "wall_ns": 1792120541000363636}
[2026-10-27T06:59:25Z] L 2026-10-16T03:15:41Z {"assets_n": 82, "bytes_total": 1804368058, "ended_outside": 0, "event": "complete", "free_bytes": 12710682624, "peak_rss": 38199296, "rate_per_day": 2112430897, "requests": 169, "run": 1792119620, "started_outside": 0, "stops": [["the cap", 1792446508], ["the floor, base 43500000 bytes a day", 1792449588], ["the floor, base 187760570 bytes a day", 1792428951]], "store_stream_bytes": 30286238, "wall_ns": 1792120541008367106}
[2026-10-27T06:59:25Z] L 2026-10-17T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "df3acd4ed1af4d05bc9ec4fa5085ebee", "phase_at": 20, "resumed": false, "run": 1792206020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792206020485538925}
[2026-10-27T06:59:25Z] L 2026-10-17T03:00:24Z {"assets_n": 96, "bytes_total": 2048827436, "closed": 605, "deferred": 0, "event": "set", "first_T": 1792118700, "last_T": 1792204200, "open": 1, "run": 1792206020, "sha256": "0915abd5810c2b901012aa6d34388eabcc76d7be8b327d651632ac9335bbe188", "tag": "pairbook-streams-1792206020", "unclosed": 0, "wall_ns": 1792206024973916528, "windows_considered": 605}
[2026-10-27T06:59:25Z] L 2026-10-17T03:03:23Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 415548049, "run": 1792206020, "sent": 96, "wall_ns": 1792206203238800300}
[2026-10-27T06:59:25Z] L 2026-10-17T03:07:35Z {"assets_n": 96, "bytes_total": 2048827436, "event": "verify", "release_id": 415548049, "run": 1792206020, "verify_sha256": "747508e351bb13bb1aa11a99791ab87d1ea798e92c66dd1ec6126aad4f67f97c", "wall_ns": 1792206455599715552}
[2026-10-27T06:59:25Z] L 2026-10-17T03:07:40Z {"already": 0, "event": "delete", "free_after": 12725805056, "free_before": 10676551680, "freed": 2048827436, "gone": 96, "removed": 96, "run": 1792206020, "wall_ns": 1792206460092686139, "windows_kept": 96}
[2026-10-27T06:59:25Z] L 2026-10-17T03:07:40Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1420617", "NRestarts": "9", "ns": 1792206460108197241}, "phase": 460, "run": 1792206020, "wall_ns": 1792206460108202947}
[2026-10-27T06:59:25Z] L 2026-10-17T03:07:40Z {"event": "kill", "exit": 0, "phase": 460, "run": 1792206020, "wall_ns": 1792206460112982086}
[2026-10-27T06:59:25Z] L 2026-10-17T03:08:10Z {"NRestarts": "10", "W": 1792206000, "event": "restart", "free_bytes": 12725788672, "gap_ns": 5487288436, "pid": 1560378, "run": 1792206020, "stopped": 1420617, "stream_bytes": 10686101, "wall_ns": 1792206490133956812}
[2026-10-27T06:59:25Z] L 2026-10-17T03:15:41Z {"T": 1792206000, "event": "resume", "reading": "PASS", "run": 1792206020, "wall_ns": 1792206941000351565}
[2026-10-27T06:59:25Z] L 2026-10-17T03:15:41Z {"assets_n": 96, "bytes_total": 2048827436, "ended_outside": 0, "event": "complete", "free_bytes": 12715110400, "peak_rss": 38330368, "rate_per_day": 2048827436, "requests": 197, "run": 1792206020, "started_outside": 0, "stops": [["the cap", 1792543404], ["the floor, base 43500000 bytes a day", 1792546173], ["the floor, base 187760570 bytes a day", 1792524292]], "store_stream_bytes": 21346173, "wall_ns": 1792206941009261301}
[2026-10-27T06:59:25Z] L 2026-10-17T08:35:37Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "ab6b527c633847f79ce14ed1afdf3623", "phase_at": 337, "resumed": false, "run": 1792226137, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792226137790990342}
[2026-10-27T06:59:25Z] L 2026-10-17T08:35:38Z {"assets_n": 23, "bytes_total": 397545662, "closed": 628, "deferred": 0, "event": "set", "first_T": 1792205100, "last_T": 1792224900, "open": 0, "run": 1792226137, "sha256": "3db64b34a3949064d28cadc5a023e4402ebacc5cf7a2adab2fe09d13971312c4", "tag": "pairbook-streams-1792226137", "unclosed": 0, "wall_ns": 1792226138787331150, "windows_considered": 628}
[2026-10-27T06:59:25Z] L 2026-10-17T08:36:15Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 415679936, "run": 1792226137, "sent": 23, "wall_ns": 1792226175895145126}
[2026-10-27T06:59:25Z] L 2026-10-17T08:38:40Z {"assets_n": 23, "bytes_total": 397545662, "event": "verify", "release_id": 415679936, "run": 1792226137, "verify_sha256": "f26e295363dadaea4d9a2de3d5e86de06da641bf85ecec538e4a36b7e89de14f", "wall_ns": 1792226320606064836}
[2026-10-27T06:59:25Z] L 2026-10-17T08:38:41Z {"already": 0, "event": "delete", "free_after": 12799180800, "free_before": 12401537024, "freed": 397545662, "gone": 23, "removed": 23, "run": 1792226137, "wall_ns": 1792226321481880383, "windows_kept": 23}
[2026-10-27T06:59:25Z] L 2026-10-17T08:45:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1560378", "NRestarts": "10", "ns": 1792226715015188081}, "phase": 15, "run": 1792226137, "wall_ns": 1792226715015194823}
[2026-10-27T06:59:25Z] L 2026-10-17T08:45:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792226137, "wall_ns": 1792226715020774740}
[2026-10-27T06:59:25Z] L 2026-10-17T08:45:45Z {"NRestarts": "11", "W": 1792226700, "event": "restart", "free_bytes": 12783226880, "gap_ns": 5530075996, "pid": 1595407, "run": 1792226137, "stopped": 1560378, "stream_bytes": 15521838, "wall_ns": 1792226745041554142}
[2026-10-27T06:59:25Z] L 2026-10-17T09:00:41Z {"T": 1792226700, "event": "resume", "reading": "PASS", "run": 1792226137, "wall_ns": 1792227641000413386}
[2026-10-27T06:59:25Z] L 2026-10-17T09:00:41Z {"assets_n": 23, "bytes_total": 397545662, "ended_outside": 0, "event": "complete", "free_bytes": 12773187584, "peak_rss": 37543936, "rate_per_day": 1659321024, "requests": 51, "run": 1792226137, "started_outside": 0, "stops": [["the cap", 1792642879], ["the floor, base 43500000 bytes a day", 1792647417], ["the floor, base 187760570 bytes a day", 1792614631]], "store_stream_bytes": 25293180, "wall_ns": 1792227641009539425}
[2026-10-27T06:59:25Z] L 2026-10-18T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "15934402892b403b858ea4b973f03c89", "phase_at": 20, "resumed": false, "run": 1792292420, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792292420527428655}
[2026-10-27T06:59:25Z] L 2026-10-18T03:00:23Z {"assets_n": 73, "bytes_total": 1197040692, "closed": 701, "deferred": 0, "event": "set", "first_T": 1792225800, "last_T": 1792290600, "open": 1, "run": 1792292420, "sha256": "7ddfeae4a937bc90c14d8047d3ab843035a2be145d8d407738f9620b098c0b08", "tag": "pairbook-streams-1792292420", "unclosed": 0, "wall_ns": 1792292423275187616, "windows_considered": 701}
[2026-10-27T06:59:25Z] L 2026-10-18T03:02:20Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 416201489, "run": 1792292420, "sent": 73, "wall_ns": 1792292540828362894}
[2026-10-27T06:59:25Z] L 2026-10-18T03:05:48Z {"assets_n": 73, "bytes_total": 1197040692, "event": "verify", "release_id": 416201489, "run": 1792292420, "verify_sha256": "a3eb29ead036c8a97f023ecb53572112300e5b22defa9d984ba1887dcddf95e3", "wall_ns": 1792292748968235081}
[2026-10-27T06:59:25Z] L 2026-10-18T03:05:51Z {"already": 0, "event": "delete", "free_after": 12776620032, "free_before": 11579240448, "freed": 1197040692, "gone": 73, "removed": 73, "run": 1792292420, "wall_ns": 1792292751530232000, "windows_kept": 73}
[2026-10-27T06:59:25Z] L 2026-10-18T03:05:51Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1595407", "NRestarts": "11", "ns": 1792292751542647421}, "phase": 351, "run": 1792292420, "wall_ns": 1792292751542652085}
[2026-10-27T06:59:25Z] L 2026-10-18T03:05:51Z {"event": "kill", "exit": 0, "phase": 351, "run": 1792292420, "wall_ns": 1792292751546822604}
[2026-10-27T06:59:25Z] L 2026-10-18T03:06:21Z {"NRestarts": "12", "W": 1792292400, "event": "restart", "free_bytes": 12776607744, "gap_ns": 5504206730, "pid": 1692402, "run": 1792292420, "stopped": 1595407, "stream_bytes": 12437717, "wall_ns": 1792292781569460854}
[2026-10-27T06:59:25Z] L 2026-10-18T03:15:41Z {"T": 1792292400, "event": "resume", "reading": "PASS", "run": 1792292420, "wall_ns": 1792293341000328710}
[2026-10-27T06:59:25Z] L 2026-10-18T03:15:41Z {"assets_n": 73, "bytes_total": 1197040692, "ended_outside": 0, "event": "complete", "free_bytes": 12764577792, "peak_rss": 37937152, "rate_per_day": 1574190499, "requests": 151, "run": 1792292420, "started_outside": 0, "stops": [["the cap", 1792731097], ["the floor, base 43500000 bytes a day", 1792734747], ["the floor, base 187760570 bytes a day", 1792698607]], "store_stream_bytes": 24161003, "wall_ns": 1792293341010228074}
[2026-10-27T06:59:25Z] L 2026-10-19T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "b6aa8a5cde4c4cc392165b8f31b1bec0", "phase_at": 20, "resumed": false, "run": 1792378820, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792378820477080166}
[2026-10-27T06:59:25Z] L 2026-10-19T03:00:24Z {"assets_n": 96, "bytes_total": 1755430954, "closed": 797, "deferred": 0, "event": "set", "first_T": 1792291500, "last_T": 1792377000, "open": 1, "run": 1792378820, "sha256": "948f4d39cca953e07be1c1c561f5115f6200f5aa8330fe78434c058d6e607528", "tag": "pairbook-streams-1792378820", "unclosed": 0, "wall_ns": 1792378824458122339, "windows_considered": 797}
[2026-10-27T06:59:25Z] L 2026-10-19T03:03:08Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 416860290, "run": 1792378820, "sent": 96, "wall_ns": 1792378988043909754}
[2026-10-27T06:59:25Z] L 2026-10-19T03:07:11Z {"assets_n": 96, "bytes_total": 1755430954, "event": "verify", "release_id": 416860290, "run": 1792378820, "verify_sha256": "86b0b971d6eaeb1c8fd7dd87f44b2f739282eec95c52919b65b79ea293db2551", "wall_ns": 1792379231626951320}
[2026-10-27T06:59:25Z] L 2026-10-19T03:07:15Z {"already": 0, "event": "delete", "free_after": 12737359872, "free_before": 10981560320, "freed": 1755430954, "gone": 96, "removed": 96, "run": 1792378820, "wall_ns": 1792379235366652736, "windows_kept": 96}
[2026-10-27T06:59:25Z] L 2026-10-19T03:07:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1692402", "NRestarts": "12", "ns": 1792379235374600961}, "phase": 435, "run": 1792378820, "wall_ns": 1792379235374606661}
[2026-10-27T06:59:25Z] L 2026-10-19T03:07:15Z {"event": "kill", "exit": 0, "phase": 435, "run": 1792378820, "wall_ns": 1792379235379253859}
[2026-10-27T06:59:25Z] L 2026-10-19T03:07:45Z {"NRestarts": "13", "W": 1792378800, "event": "restart", "free_bytes": 12737351680, "gap_ns": 5404558972, "pid": 1814768, "run": 1792378820, "stopped": 1692402, "stream_bytes": 20988190, "wall_ns": 1792379265403200749}
[2026-10-27T06:59:25Z] L 2026-10-19T03:15:41Z {"T": 1792378800, "event": "resume", "reading": "PASS", "run": 1792378820, "wall_ns": 1792379741000400500}
[2026-10-27T06:59:25Z] L 2026-10-19T03:15:41Z {"assets_n": 96, "bytes_total": 1755430954, "ended_outside": 0, "event": "complete", "free_bytes": 12720193536, "peak_rss": 38592512, "rate_per_day": 1755430954, "requests": 197, "run": 1792378820, "started_outside": 0, "stops": [["the cap", 1792771618], ["the floor, base 43500000 bytes a day", 1792774544], ["the floor, base 187760570 bytes a day", 1792745234]], "store_stream_bytes": 38026457, "wall_ns": 1792379741011807328}
[2026-10-27T06:59:25Z] L 2026-10-19T21:54:19Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "7efdb0d05f6f4814b803f423a1351eae", "phase_at": 559, "resumed": false, "run": 1792446859, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792446859827562789}
[2026-10-27T06:59:25Z] L 2026-10-19T21:54:23Z {"assets_n": 76, "bytes_total": 1702929677, "closed": 873, "deferred": 0, "event": "set", "first_T": 1792377900, "last_T": 1792445400, "open": 1, "run": 1792446859, "sha256": "8491aab13dd6df082e8a4e847bd4e676a5edbeabd050e9a1767a79d7ecfb72d3", "tag": "pairbook-streams-1792446859", "unclosed": 0, "wall_ns": 1792446863665163186, "windows_considered": 873}
[2026-10-27T06:59:25Z] L 2026-10-19T22:02:33Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 417794290, "run": 1792446859, "sent": 76, "wall_ns": 1792447353191732798}
[2026-10-27T06:59:25Z] L 2026-10-19T22:09:37Z {"assets_n": 76, "bytes_total": 1702929677, "event": "verify", "release_id": 417794290, "run": 1792446859, "verify_sha256": "dfa62b04b0291467b86d37271e00e2242c0fea6b9e1caa987e7a9b31fafd3f6b", "wall_ns": 1792447777762252351}
[2026-10-27T06:59:25Z] L 2026-10-19T22:09:41Z {"already": 0, "event": "delete", "free_after": 12726702080, "free_before": 11023396864, "freed": 1702929677, "gone": 76, "removed": 76, "run": 1792446859, "wall_ns": 1792447781500420485, "windows_kept": 76}
[2026-10-27T06:59:25Z] L 2026-10-19T22:15:15Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1814768", "NRestarts": "13", "ns": 1792448115017795294}, "phase": 15, "run": 1792446859, "wall_ns": 1792448115017801355}
[2026-10-27T06:59:25Z] L 2026-10-19T22:15:15Z {"event": "kill", "exit": 0, "phase": 15, "run": 1792446859, "wall_ns": 1792448115024251292}
[2026-10-27T06:59:25Z] L 2026-10-19T22:15:45Z {"NRestarts": "14", "W": 1792448100, "event": "restart", "free_bytes": 12707540992, "gap_ns": 5638947193, "pid": 1915093, "run": 1792446859, "stopped": 1814768, "stream_bytes": 30931694, "wall_ns": 1792448145064395857}
[2026-10-27T06:59:25Z] L 2026-10-19T22:30:41Z {"T": 1792448100, "event": "resume", "reading": "PASS", "run": 1792446859, "wall_ns": 1792449041000625272}
[2026-10-27T06:59:25Z] L 2026-10-19T22:30:41Z {"assets_n": 76, "bytes_total": 1702929677, "ended_outside": 0, "event": "complete", "free_bytes": 12678688768, "peak_rss": 37539840, "rate_per_day": 2151069065, "requests": 157, "run": 1792446859, "started_outside": 0, "stops": [["the cap", 1792767956], ["the floor, base 43500000 bytes a day", 1792771035], ["the floor, base 187760570 bytes a day", 1792751174]], "store_stream_bytes": 60078470, "wall_ns": 1792449041020984137}
[2026-10-27T06:59:25Z] L 2026-10-20T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "39b80e28726849c6b2c7c78015f76beb", "phase_at": 20, "resumed": false, "run": 1792465220, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792465220508369328}
[2026-10-27T06:59:25Z] L 2026-10-20T03:00:21Z {"assets_n": 20, "bytes_total": 428604581, "closed": 893, "deferred": 0, "event": "set", "first_T": 1792446300, "last_T": 1792463400, "open": 1, "run": 1792465220, "sha256": "08a4bf67291e8988351d7b031e9a6250ded7ec726fb2a80a1c28559d6b827e6b", "tag": "pairbook-streams-1792465220", "unclosed": 0, "wall_ns": 1792465221560132886, "windows_considered": 893}
[2026-10-27T06:59:25Z] L 2026-10-20T03:01:05Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 417955485, "run": 1792465220, "sent": 20, "wall_ns": 1792465265840619699}
[2026-10-27T06:59:25Z] L 2026-10-20T03:03:38Z {"assets_n": 20, "bytes_total": 428604581, "event": "verify", "release_id": 417955485, "run": 1792465220, "verify_sha256": "1417b0845ea746c17a126d8311895714cd28b5cdbefbb3f27cc38e7b2d8a516a", "wall_ns": 1792465418377004134}
[2026-10-27T06:59:25Z] L 2026-10-20T03:03:39Z {"already": 0, "event": "delete", "free_after": 12736249856, "free_before": 12307550208, "freed": 428604581, "gone": 20, "removed": 20, "run": 1792465220, "wall_ns": 1792465419274331805, "windows_kept": 20}
[2026-10-27T06:59:25Z] L 2026-10-20T03:03:39Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1915093", "NRestarts": "14", "ns": 1792465419285640926}, "phase": 219, "run": 1792465220, "wall_ns": 1792465419285646173}
[2026-10-27T06:59:25Z] L 2026-10-20T03:03:39Z {"event": "kill", "exit": 0, "phase": 219, "run": 1792465220, "wall_ns": 1792465419290626015}
[2026-10-27T06:59:25Z] L 2026-10-20T03:04:09Z {"NRestarts": "15", "W": 1792465200, "event": "restart", "free_bytes": 12736208896, "gap_ns": 5521442701, "pid": 1942330, "run": 1792465220, "stopped": 1915093, "stream_bytes": 21234976, "wall_ns": 1792465449314599186}
[2026-10-27T06:59:25Z] L 2026-10-20T03:15:41Z {"T": 1792465200, "event": "resume", "reading": "PASS", "run": 1792465220, "wall_ns": 1792466141000339712}
[2026-10-27T06:59:25Z] L 2026-10-20T03:15:41Z {"assets_n": 20, "bytes_total": 428604581, "ended_outside": 0, "event": "complete", "free_bytes": 12714721280, "peak_rss": 37937152, "rate_per_day": 2057301988, "requests": 45, "run": 1792465220, "started_outside": 0, "stops": [["the cap", 1792800340], ["the floor, base 43500000 bytes a day", 1792803989], ["the floor, base 187760570 bytes a day", 1792782280]], "store_stream_bytes": 42260469, "wall_ns": 1792466141012853604}
[2026-10-27T06:59:25Z] L 2026-10-20T11:23:37Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "8b75ff2677d249a6a9fe69e50db1c2ae", "phase_at": 517, "resumed": false, "run": 1792495417, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792495417844843187}
[2026-10-27T06:59:25Z] L 2026-10-20T11:23:39Z {"assets_n": 34, "bytes_total": 764815296, "closed": 927, "deferred": 0, "event": "set", "first_T": 1792464300, "last_T": 1792494000, "open": 0, "run": 1792495417, "sha256": "e323ee33788d09b6cc52062cea9cd4914bc06d83a423f00e8704115f5ee8077e", "tag": "pairbook-streams-1792495417", "unclosed": 0, "wall_ns": 1792495419680991102, "windows_considered": 927}
[2026-10-27T06:59:25Z] L 2026-10-20T11:30:29Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 418317989, "run": 1792495417, "sent": 34, "wall_ns": 1792495829134879887}
[2026-10-27T06:59:25Z] L 2026-10-20T11:33:19Z {"assets_n": 34, "bytes_total": 764815296, "event": "verify", "release_id": 418317989, "run": 1792495417, "verify_sha256": "c2b18808ac9dd1fa1af41eb8e9b6f3b616698bb12dcfc8910b97f44dc91c36ac", "wall_ns": 1792495999645679199}
[2026-10-27T06:59:25Z] L 2026-10-20T11:33:21Z {"already": 0, "event": "delete", "free_after": 12638756864, "free_before": 11873771520, "freed": 764815296, "gone": 34, "removed": 34, "run": 1792495417, "wall_ns": 1792496001362671467, "windows_kept": 34}
[2026-10-27T06:59:25Z] L 2026-10-20T11:33:21Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1942330", "NRestarts": "15", "ns": 1792496001380557653}, "phase": 201, "run": 1792495417, "wall_ns": 1792496001380565155}
[2026-10-27T06:59:25Z] L 2026-10-20T11:33:21Z {"event": "kill", "exit": 0, "phase": 201, "run": 1792495417, "wall_ns": 1792496001386376172}
[2026-10-27T06:59:25Z] L 2026-10-20T11:33:51Z {"NRestarts": "16", "W": 1792495800, "event": "restart", "free_bytes": 12638744576, "gap_ns": 5668185588, "pid": 1997029, "run": 1792495417, "stopped": 1942330, "stream_bytes": 20135691, "wall_ns": 1792496031413213462}
[2026-10-27T06:59:25Z] L 2026-10-20T11:45:41Z {"T": 1792495800, "event": "resume", "reading": "PASS", "run": 1792495417, "wall_ns": 1792496741000411804}
[2026-10-27T06:59:25Z] L 2026-10-20T11:45:41Z {"assets_n": 34, "bytes_total": 764815296, "ended_outside": 0, "event": "complete", "free_bytes": 12627136512, "peak_rss": 37408768, "rate_per_day": 2159478482, "requests": 73, "run": 1792495417, "started_outside": 0, "stops": [["the cap", 1792815561], ["the floor, base 43500000 bytes a day", 1792815484], ["the floor, base 187760570 bytes a day", 1792795894]], "store_stream_bytes": 31416312, "wall_ns": 1792496741014150948}
[2026-10-27T06:59:25Z] L 2026-10-21T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "b930c6730bf241b99c68a735c088800c", "phase_at": 20, "resumed": false, "run": 1792551620, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792551620436317477}
[2026-10-27T06:59:25Z] L 2026-10-21T03:00:23Z {"assets_n": 62, "bytes_total": 1362902551, "closed": 989, "deferred": 0, "event": "set", "first_T": 1792494900, "last_T": 1792549800, "open": 1, "run": 1792551620, "sha256": "86c50466510f2054e4aa0455af33787059c1cc16b6a2f3dc81b5ef002ecb9ae5", "tag": "pairbook-streams-1792551620", "unclosed": 0, "wall_ns": 1792551623641943166, "windows_considered": 989}
[2026-10-27T06:59:25Z] L 2026-10-21T03:02:34Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 419096475, "run": 1792551620, "sent": 62, "wall_ns": 1792551754079483237}
[2026-10-27T06:59:25Z] L 2026-10-21T03:06:11Z {"assets_n": 62, "bytes_total": 1362902551, "event": "verify", "release_id": 419096475, "run": 1792551620, "verify_sha256": "fcd57c3250da0c73a0a463197880ede0b4caba30b2d3531b5e67c74d89101b77", "wall_ns": 1792551971026358089}
[2026-10-27T06:59:25Z] L 2026-10-21T03:06:13Z {"already": 0, "event": "delete", "free_after": 12585439232, "free_before": 11222228992, "freed": 1362902551, "gone": 62, "removed": 62, "run": 1792551620, "wall_ns": 1792551973979858662, "windows_kept": 62}
[2026-10-27T06:59:25Z] L 2026-10-21T03:06:13Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "1997029", "NRestarts": "16", "ns": 1792551973992391945}, "phase": 373, "run": 1792551620, "wall_ns": 1792551973992396231}
[2026-10-27T06:59:25Z] L 2026-10-21T03:06:13Z {"event": "kill", "exit": 0, "phase": 373, "run": 1792551620, "wall_ns": 1792551973997452972}
[2026-10-27T06:59:25Z] L 2026-10-21T03:06:44Z {"NRestarts": "17", "W": 1792551600, "event": "restart", "free_bytes": 12585414656, "gap_ns": 5552861113, "pid": 2076364, "run": 1792551620, "stopped": 1997029, "stream_bytes": 21344325, "wall_ns": 1792552004023624781}
[2026-10-27T06:59:25Z] L 2026-10-21T03:15:41Z {"T": 1792551600, "event": "resume", "reading": "PASS", "run": 1792551620, "wall_ns": 1792552541000652508}
[2026-10-27T06:59:25Z] L 2026-10-21T03:15:41Z {"assets_n": 62, "bytes_total": 1362902551, "ended_outside": 0, "event": "complete", "free_bytes": 12568043520, "peak_rss": 38330368, "rate_per_day": 2110300724, "requests": 129, "run": 1792551620, "started_outside": 0, "stops": [["the cap", 1792878503], ["the floor, base 43500000 bytes a day", 1792876191], ["the floor, base 187760570 bytes a day", 1792855874]], "store_stream_bytes": 38435764, "wall_ns": 1792552541015556785}
[2026-10-27T06:59:25Z] L 2026-10-21T21:39:04Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "ddf646820072487fbca10fe0ea1d6d9d", "phase_at": 544, "resumed": false, "run": 1792618744, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792618744805106316}
[2026-10-27T06:59:25Z] L 2026-10-21T21:39:08Z {"assets_n": 75, "bytes_total": 1697351287, "closed": 1064, "deferred": 0, "event": "set", "first_T": 1792550700, "last_T": 1792617300, "open": 0, "run": 1792618744, "sha256": "14628f1239ce9548ab9a88bfae0a8017382eac3a6c54f823b79c7acf8e9f2d70", "tag": "pairbook-streams-1792618744", "unclosed": 0, "wall_ns": 1792618748723134556, "windows_considered": 1064}
[2026-10-27T06:59:25Z] L 2026-10-21T21:47:16Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 420082380, "run": 1792618744, "sent": 75, "wall_ns": 1792619236058059430}
[2026-10-27T06:59:25Z] L 2026-10-21T21:51:01Z {"assets_n": 75, "bytes_total": 1697351287, "event": "verify", "release_id": 420082380, "run": 1792618744, "verify_sha256": "954d28907c55dac360cea2a28a7781c4ca0500ef6c8313c3c86a6853539dbbce", "wall_ns": 1792619461695303474}
[2026-10-27T06:59:25Z] L 2026-10-21T21:51:05Z {"already": 0, "event": "delete", "free_after": 12533227520, "free_before": 10835509248, "freed": 1697351287, "gone": 75, "removed": 75, "run": 1792618744, "wall_ns": 1792619465416013472, "windows_kept": 75}
[2026-10-27T06:59:25Z] L 2026-10-21T21:51:05Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2076364", "NRestarts": "17", "ns": 1792619465433993359}, "phase": 365, "run": 1792618744, "wall_ns": 1792619465433999513}
[2026-10-27T06:59:25Z] L 2026-10-21T21:51:05Z {"event": "kill", "exit": 0, "phase": 365, "run": 1792618744, "wall_ns": 1792619465439433263}
[2026-10-27T06:59:25Z] L 2026-10-21T21:51:35Z {"NRestarts": "18", "W": 1792619100, "event": "restart", "free_bytes": 12533202944, "gap_ns": 5745862259, "pid": 2192943, "run": 1792618744, "stopped": 2076364, "stream_bytes": 28722461, "wall_ns": 1792619495470455301}
[2026-10-27T06:59:25Z] L 2026-10-21T22:00:41Z {"T": 1792619100, "event": "resume", "reading": "PASS", "run": 1792618744, "wall_ns": 1792620041000434452}
[2026-10-27T06:59:25Z] L 2026-10-21T22:00:41Z {"assets_n": 75, "bytes_total": 1697351287, "ended_outside": 0, "event": "complete", "free_bytes": 12508360704, "peak_rss": 37806080, "rate_per_day": 2172609647, "requests": 155, "run": 1792618744, "started_outside": 0, "stops": [["the cap", 1792936072], ["the floor, base 43500000 bytes a day", 1792932264], ["the floor, base 187760570 bytes a day", 1792913182]], "store_stream_bytes": 53078752, "wall_ns": 1792620041014703750}
[2026-10-27T06:59:25Z] L 2026-10-22T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "2ead70f2934e426f9db2802c9f366424", "phase_at": 20, "resumed": false, "run": 1792638020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792638020509862222}
[2026-10-27T06:59:25Z] L 2026-10-22T03:00:21Z {"assets_n": 21, "bytes_total": 391495954, "closed": 1085, "deferred": 0, "event": "set", "first_T": 1792618200, "last_T": 1792636200, "open": 1, "run": 1792638020, "sha256": "bcccbdcea9b48dfb0ce8b98e2ce6eb1faeb741091d2f4b96a260cd633af8810d", "tag": "pairbook-streams-1792638020", "unclosed": 0, "wall_ns": 1792638021492965919, "windows_considered": 1085}
[2026-10-27T06:59:25Z] L 2026-10-22T03:01:03Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 420262131, "run": 1792638020, "sent": 21, "wall_ns": 1792638063331313560}
[2026-10-27T06:59:25Z] L 2026-10-22T03:03:31Z {"assets_n": 21, "bytes_total": 391495954, "event": "verify", "release_id": 420262131, "run": 1792638020, "verify_sha256": "c53531cd81ef4f93c4a7a970b2c0c542146e78ed84d309d0afb42f14ab7123c9", "wall_ns": 1792638211785126344}
[2026-10-27T06:59:25Z] L 2026-10-22T03:03:32Z {"already": 0, "event": "delete", "free_after": 12514353152, "free_before": 12122759168, "freed": 391495954, "gone": 21, "removed": 21, "run": 1792638020, "wall_ns": 1792638212641898392, "windows_kept": 21}
[2026-10-27T06:59:25Z] L 2026-10-22T03:03:32Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2192943", "NRestarts": "18", "ns": 1792638212654633160}, "phase": 212, "run": 1792638020, "wall_ns": 1792638212654637695}
[2026-10-27T06:59:25Z] L 2026-10-22T03:03:32Z {"event": "kill", "exit": 0, "phase": 212, "run": 1792638020, "wall_ns": 1792638212659732496}
[2026-10-27T06:59:25Z] L 2026-10-22T03:04:02Z {"NRestarts": "19", "W": 1792638000, "event": "restart", "free_bytes": 12514340864, "gap_ns": 5643787804, "pid": 2221487, "run": 1792638020, "stopped": 2192943, "stream_bytes": 27860091, "wall_ns": 1792638242689438971}
[2026-10-27T06:59:25Z] L 2026-10-22T03:15:41Z {"T": 1792638000, "event": "resume", "reading": "PASS", "run": 1792638020, "wall_ns": 1792638941000342309}
[2026-10-27T06:59:25Z] L 2026-10-22T03:15:41Z {"assets_n": 21, "bytes_total": 391495954, "ended_outside": 0, "event": "complete", "free_bytes": 12499591168, "peak_rss": 38195200, "rate_per_day": 1789695789, "requests": 47, "run": 1792638020, "started_outside": 0, "stops": [["the cap", 1793023110], ["the floor, base 43500000 bytes a day", 1793015968], ["the floor, base 187760570 bytes a day", 1792988463]], "store_stream_bytes": 42282498, "wall_ns": 1792638941017392845}
[2026-10-27T06:59:25Z] L 2026-10-22T06:24:08Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "bf696abbc7a746dea3a0966d716d3074", "phase_at": 548, "resumed": false, "run": 1792650248, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792650248784202770}
[2026-10-27T06:59:25Z] L 2026-10-22T06:24:09Z {"assets_n": 14, "bytes_total": 280783691, "closed": 1099, "deferred": 0, "event": "set", "first_T": 1792637100, "last_T": 1792648800, "open": 1, "run": 1792650248, "sha256": "6204f5ff7868ba1bc1a8e10697a44aa9a3b4ede37177620d9dbef69d51672bb0", "tag": "pairbook-streams-1792650248", "unclosed": 0, "wall_ns": 1792650249586883942, "windows_considered": 1099}
[2026-10-27T06:59:25Z] L 2026-10-22T06:24:34Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 420372582, "run": 1792650248, "sent": 14, "wall_ns": 1792650274824220554}
[2026-10-27T06:59:25Z] L 2026-10-22T06:30:32Z {"assets_n": 14, "bytes_total": 280783691, "event": "verify", "release_id": 420372582, "run": 1792650248, "verify_sha256": "ea788ba4bf4c34150b9250af70414689f3546b3a92564a84e1dfcf1b1d5e6a02", "wall_ns": 1792650632675548955}
[2026-10-27T06:59:25Z] L 2026-10-22T06:30:33Z {"already": 0, "event": "delete", "free_after": 12560494592, "free_before": 12279042048, "freed": 280783691, "gone": 14, "removed": 14, "run": 1792650248, "wall_ns": 1792650633320590752, "windows_kept": 14}
[2026-10-27T06:59:25Z] L 2026-10-22T06:30:33Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2241902", "NRestarts": "0", "ns": 1792650633339559233}, "phase": 33, "run": 1792650248, "wall_ns": 1792650633339564607}
[2026-10-27T06:59:25Z] L 2026-10-22T06:30:33Z {"event": "kill", "exit": 0, "phase": 33, "run": 1792650248, "wall_ns": 1792650633345250000}
[2026-10-27T06:59:25Z] L 2026-10-22T06:31:03Z {"NRestarts": "1", "W": 1792650600, "event": "restart", "free_bytes": 12560482304, "gap_ns": 5601500879, "pid": 2250075, "run": 1792650248, "stopped": 2241902, "stream_bytes": 10010022, "wall_ns": 1792650663375238922}
[2026-10-27T06:59:25Z] L 2026-10-22T06:45:41Z {"T": 1792650600, "event": "resume", "reading": "PASS", "run": 1792650248, "wall_ns": 1792651541015238752}
[2026-10-27T06:59:25Z] L 2026-10-22T06:45:41Z {"assets_n": 14, "bytes_total": 280783691, "ended_outside": 0, "event": "complete", "free_bytes": 12529709056, "peak_rss": 37797888, "rate_per_day": 1925373881, "requests": 33, "run": 1792650248, "started_outside": 0, "stops": [["the cap", 1793008800], ["the floor, base 43500000 bytes a day", 1793003908], ["the floor, base 187760570 bytes a day", 1792979852]], "store_stream_bytes": 38684086, "wall_ns": 1792651541166549306}
[2026-10-27T06:59:25Z] L 2026-10-23T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "1172b5c756384074a57a896b4356ec16", "phase_at": 20, "resumed": false, "run": 1792724420, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792724420512050478}
[2026-10-27T06:59:25Z] L 2026-10-23T03:00:24Z {"assets_n": 82, "bytes_total": 1595061931, "closed": 1181, "deferred": 0, "event": "set", "first_T": 1792649700, "last_T": 1792722600, "open": 1, "run": 1792724420, "sha256": "d0e560a3669a7231dea88f79bea44078c0e31e7cff8a374af08de1b5b280bf5c", "tag": "pairbook-streams-1792724420", "unclosed": 0, "wall_ns": 1792724424121884436, "windows_considered": 1181}
[2026-10-27T06:59:25Z] L 2026-10-23T03:03:06Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 421406556, "run": 1792724420, "sent": 82, "wall_ns": 1792724586787024019}
[2026-10-27T06:59:25Z] L 2026-10-23T03:07:00Z {"assets_n": 82, "bytes_total": 1595061931, "event": "verify", "release_id": 421406556, "run": 1792724420, "verify_sha256": "3e232f5ac1bfe06b39f3befa0e17f7f3e616fd37cc7ab297e6d27128a336c9a0", "wall_ns": 1792724820430388300}
[2026-10-27T06:59:25Z] L 2026-10-23T03:07:04Z {"already": 0, "event": "delete", "free_after": 12469579776, "free_before": 10874122240, "freed": 1595061931, "gone": 82, "removed": 82, "run": 1792724420, "wall_ns": 1792724824480858054, "windows_kept": 82}
[2026-10-27T06:59:25Z] L 2026-10-23T03:07:04Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2250075", "NRestarts": "1", "ns": 1792724824494779066}, "phase": 424, "run": 1792724420, "wall_ns": 1792724824494785255}
[2026-10-27T06:59:25Z] L 2026-10-23T03:07:04Z {"event": "kill", "exit": 0, "phase": 424, "run": 1792724420, "wall_ns": 1792724824500348742}
[2026-10-27T06:59:25Z] L 2026-10-23T03:07:34Z {"NRestarts": "2", "W": 1792724400, "event": "restart", "free_bytes": 12469559296, "gap_ns": 5549775487, "pid": 2371078, "run": 1792724420, "stopped": 2250075, "stream_bytes": 21412011, "wall_ns": 1792724854530097535}
[2026-10-27T06:59:25Z] L 2026-10-23T03:15:41Z {"T": 1792724400, "event": "resume", "reading": "PASS", "run": 1792724420, "wall_ns": 1792725341000373070}
[2026-10-27T06:59:25Z] L 2026-10-23T03:15:41Z {"assets_n": 82, "bytes_total": 1595061931, "ended_outside": 0, "event": "complete", "free_bytes": 12451762176, "peak_rss": 38195200, "rate_per_day": 1867389577, "requests": 169, "run": 1792724420, "started_outside": 0, "stops": [["the cap", 1793093683], ["the floor, base 43500000 bytes a day", 1793084876], ["the floor, base 187760570 bytes a day", 1793059638]], "store_stream_bytes": 38897268, "wall_ns": 1792725341016615809}
[2026-10-27T06:59:25Z] L 2026-10-24T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "368fabaad3cc46298eb66d93b3fc0918", "phase_at": 20, "resumed": false, "run": 1792810820, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792810820536220287}
[2026-10-27T06:59:25Z] L 2026-10-24T03:00:24Z {"assets_n": 96, "bytes_total": 1928035986, "closed": 1277, "deferred": 0, "event": "set", "first_T": 1792723500, "last_T": 1792809000, "open": 1, "run": 1792810820, "sha256": "d1416ac8255bd8004a8f1da09afde202f94a83d5029c27f14c032b4b3498eddc", "tag": "pairbook-streams-1792810820", "unclosed": 0, "wall_ns": 1792810824956999985, "windows_considered": 1277}
[2026-10-27T06:59:25Z] L 2026-10-24T03:03:18Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 422479928, "run": 1792810820, "sent": 96, "wall_ns": 1792810998516707176}
[2026-10-27T06:59:25Z] L 2026-10-24T03:07:41Z {"assets_n": 96, "bytes_total": 1928035986, "event": "verify", "release_id": 422479928, "run": 1792810820, "verify_sha256": "ebdbcf9c07a0e783fbe65286fd557bdf88b919c32dace5940b8db89666e5ec80", "wall_ns": 1792811261029724269}
[2026-10-27T06:59:25Z] L 2026-10-24T03:07:45Z {"already": 0, "event": "delete", "free_after": 12392730624, "free_before": 10464256000, "freed": 1928035986, "gone": 96, "removed": 96, "run": 1792810820, "wall_ns": 1792811265216553815, "windows_kept": 96}
[2026-10-27T06:59:25Z] L 2026-10-24T03:07:45Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2388406", "NRestarts": "0", "ns": 1792811265230052742}, "phase": 465, "run": 1792810820, "wall_ns": 1792811265230059000}
[2026-10-27T06:59:25Z] L 2026-10-24T03:07:45Z {"event": "kill", "exit": 0, "phase": 465, "run": 1792810820, "wall_ns": 1792811265235454280}
[2026-10-27T06:59:25Z] L 2026-10-24T03:08:15Z {"NRestarts": "1", "W": 1792810800, "event": "restart", "free_bytes": 12392722432, "gap_ns": 5722327940, "pid": 2510977, "run": 1792810820, "stopped": 2388406, "stream_bytes": 12774028, "wall_ns": 1792811295268034662}
[2026-10-27T06:59:25Z] L 2026-10-24T03:15:41Z {"T": 1792810800, "event": "resume", "reading": "PASS", "run": 1792810820, "wall_ns": 1792811741000368303}
[2026-10-27T06:59:25Z] L 2026-10-24T03:15:41Z {"assets_n": 96, "bytes_total": 1928035986, "ended_outside": 0, "event": "complete", "free_bytes": 12374351872, "peak_rss": 37285888, "rate_per_day": 1928035986, "requests": 197, "run": 1792810820, "started_outside": 0, "stops": [["the cap", 1793168866], ["the floor, base 43500000 bytes a day", 1793156824], ["the floor, base 187760570 bytes a day", 1793133295]], "store_stream_bytes": 30664569, "wall_ns": 1792811741023332704}
[2026-10-27T06:59:25Z] L 2026-10-24T13:55:09Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "8456202c5c2b4e009cdd3deb24d3258c", "phase_at": 609, "resumed": false, "run": 1792850109, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792850109786076142}
[2026-10-27T06:59:25Z] L 2026-10-24T13:55:11Z {"assets_n": 44, "bytes_total": 827830635, "closed": 1321, "deferred": 0, "event": "set", "first_T": 1792809900, "last_T": 1792848600, "open": 1, "run": 1792850109, "sha256": "edf4e1d7074f4c588c91769d35b856ab376667aadb5f856ba315f3dd154ecd17", "tag": "pairbook-streams-1792850109", "unclosed": 0, "wall_ns": 1792850111848635155, "windows_considered": 1321}
[2026-10-27T06:59:25Z] L 2026-10-24T14:01:35Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 422764661, "run": 1792850109, "sent": 44, "wall_ns": 1792850495510283483}
[2026-10-27T06:59:25Z] L 2026-10-24T14:04:34Z {"assets_n": 44, "bytes_total": 827830635, "event": "verify", "release_id": 422764661, "run": 1792850109, "verify_sha256": "0650520c900288449727d50990b8b2c668ed1a727569b07e94d6a8e925ae775c", "wall_ns": 1792850674086662648}
[2026-10-27T06:59:25Z] L 2026-10-24T14:04:35Z {"already": 0, "event": "delete", "free_after": 12403814400, "free_before": 11575771136, "freed": 827830635, "gone": 44, "removed": 44, "run": 1792850109, "wall_ns": 1792850675851801578, "windows_kept": 44}
[2026-10-27T06:59:25Z] L 2026-10-24T14:04:35Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2510977", "NRestarts": "1", "ns": 1792850675865864309}, "phase": 275, "run": 1792850109, "wall_ns": 1792850675865869493}
[2026-10-27T06:59:25Z] L 2026-10-24T14:04:35Z {"event": "kill", "exit": 0, "phase": 275, "run": 1792850109, "wall_ns": 1792850675869931549}
[2026-10-27T06:59:25Z] L 2026-10-24T14:05:05Z {"NRestarts": "2", "W": 1792850400, "event": "restart", "free_bytes": 12403781632, "gap_ns": 5690640365, "pid": 2568040, "run": 1792850109, "stopped": 2510977, "stream_bytes": 17845848, "wall_ns": 1792850705901163555}
[2026-10-27T06:59:25Z] L 2026-10-24T14:15:41Z {"T": 1792850400, "event": "resume", "reading": "PASS", "run": 1792850109, "wall_ns": 1792851341000417805}
[2026-10-27T06:59:25Z] L 2026-10-24T14:15:41Z {"assets_n": 44, "bytes_total": 827830635, "ended_outside": 0, "event": "complete", "free_bytes": 12393021440, "peak_rss": 37937152, "rate_per_day": 1806175930, "requests": 93, "run": 1792850109, "started_outside": 0, "stops": [["the cap", 1793232656], ["the floor, base 43500000 bytes a day", 1793220031], ["the floor, base 187760570 bytes a day", 1793193356]], "store_stream_bytes": 28666073, "wall_ns": 1792851341019472689}
[2026-10-27T06:59:25Z] L 2026-10-25T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "fd73f8981e3f42cfaf70a9b8f25d830d", "phase_at": 20, "resumed": false, "run": 1792897220, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792897220516868478}
[2026-10-27T06:59:25Z] L 2026-10-25T03:00:22Z {"assets_n": 52, "bytes_total": 684213553, "closed": 1373, "deferred": 0, "event": "set", "first_T": 1792849500, "last_T": 1792895400, "open": 1, "run": 1792897220, "sha256": "b0a814654d2ed487aa2618b9b3f01fb4a478d201fef2e908310878bda169e28c", "tag": "pairbook-streams-1792897220", "unclosed": 0, "wall_ns": 1792897222234268364, "windows_considered": 1373}
[2026-10-27T06:59:25Z] L 2026-10-25T03:01:41Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 423115525, "run": 1792897220, "sent": 52, "wall_ns": 1792897301171562428}
[2026-10-27T06:59:25Z] L 2026-10-25T03:04:34Z {"assets_n": 52, "bytes_total": 684213553, "event": "verify", "release_id": 423115525, "run": 1792897220, "verify_sha256": "4fe141ae1015865a49e2546e5617457243c34c23e3632bb12effcc2ef314ae5a", "wall_ns": 1792897474734873344}
[2026-10-27T06:59:25Z] L 2026-10-25T03:04:36Z {"already": 0, "event": "delete", "free_after": 12398997504, "free_before": 11714547712, "freed": 684213553, "gone": 52, "removed": 52, "run": 1792897220, "wall_ns": 1792897476206137588, "windows_kept": 52}
[2026-10-27T06:59:25Z] L 2026-10-25T03:04:36Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2568040", "NRestarts": "2", "ns": 1792897476227728149}, "phase": 276, "run": 1792897220, "wall_ns": 1792897476227733847}
[2026-10-27T06:59:25Z] L 2026-10-25T03:04:36Z {"event": "kill", "exit": 0, "phase": 276, "run": 1792897220, "wall_ns": 1792897476234541107}
[2026-10-27T06:59:25Z] L 2026-10-25T03:05:06Z {"NRestarts": "3", "W": 1792897200, "event": "restart", "free_bytes": 12398968832, "gap_ns": 5574774462, "pid": 2636308, "run": 1792897220, "stopped": 2568040, "stream_bytes": 18017660, "wall_ns": 1792897506267483744}
[2026-10-27T06:59:25Z] L 2026-10-25T03:15:41Z {"T": 1792897200, "event": "resume", "reading": "PASS", "run": 1792897220, "wall_ns": 1792898141000384238}
[2026-10-27T06:59:25Z] L 2026-10-25T03:15:41Z {"assets_n": 52, "bytes_total": 684213553, "ended_outside": 0, "event": "complete", "free_bytes": 12369510400, "peak_rss": 37986304, "rate_per_day": 1263163482, "requests": 109, "run": 1792897220, "started_outside": 0, "stops": [["the cap", 1793442670], ["the floor, base 43500000 bytes a day", 1793418493], ["the floor, base 187760570 bytes a day", 1793366756]], "store_stream_bytes": 39000874, "wall_ns": 1792898141020149805}
[2026-10-27T06:59:25Z] L 2026-10-25T06:12:37Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "5f0b5b50202240b0a368fdb7385753e4", "phase_at": 757, "resumed": false, "run": 1792908757, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792908757823455684}
[2026-10-27T06:59:25Z] L 2026-10-25T06:12:38Z {"assets_n": 13, "bytes_total": 253766917, "closed": 1386, "deferred": 0, "event": "set", "first_T": 1792896300, "last_T": 1792907100, "open": 1, "run": 1792908757, "sha256": "7eebdd6b04decc80a3af5aae9bd6f5fe4e9d65312009813c20cbeeeb055e9956", "tag": "pairbook-streams-1792908757", "unclosed": 0, "wall_ns": 1792908758673665127, "windows_considered": 1386}
[2026-10-27T06:59:25Z] L 2026-10-25T06:15:41Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 423183376, "run": 1792908757, "sent": 13, "wall_ns": 1792908941831854357}
[2026-10-27T06:59:25Z] L 2026-10-25T06:17:56Z {"assets_n": 13, "bytes_total": 253766917, "event": "verify", "release_id": 423183376, "run": 1792908757, "verify_sha256": "0468c622a805a6a5a95013fd197958481265df5cad918b62cac0220759cb9460", "wall_ns": 1792909076991922059}
[2026-10-27T06:59:25Z] L 2026-10-25T06:17:57Z {"already": 0, "event": "delete", "free_after": 12356149248, "free_before": 12102332416, "freed": 253766917, "gone": 13, "removed": 13, "run": 1792908757, "wall_ns": 1792909077569720131, "windows_kept": 13}
[2026-10-27T06:59:25Z] L 2026-10-25T06:17:57Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2636308", "NRestarts": "3", "ns": 1792909077587302843}, "phase": 177, "run": 1792908757, "wall_ns": 1792909077587309269}
[2026-10-27T06:59:25Z] L 2026-10-25T06:17:57Z {"event": "kill", "exit": 0, "phase": 177, "run": 1792908757, "wall_ns": 1792909077592207777}
[2026-10-27T06:59:25Z] L 2026-10-25T06:18:27Z {"NRestarts": "4", "W": 1792908900, "event": "restart", "free_bytes": 12356128768, "gap_ns": 5898872430, "pid": 2656081, "run": 1792908757, "stopped": 2636308, "stream_bytes": 27687165, "wall_ns": 1792909107623874142}
[2026-10-27T06:59:25Z] L 2026-10-25T06:30:41Z {"T": 1792908900, "event": "resume", "reading": "PASS", "run": 1792908757, "wall_ns": 1792909841046168656}
[2026-10-27T06:59:25Z] L 2026-10-25T06:30:41Z {"assets_n": 13, "bytes_total": 253766917, "ended_outside": 0, "event": "complete", "free_bytes": 12336185344, "peak_rss": 37670912, "rate_per_day": 1873971079, "requests": 31, "run": 1792908757, "started_outside": 0, "stops": [["the cap", 1793276493], ["the floor, base 43500000 bytes a day", 1793262934], ["the floor, base 187760570 bytes a day", 1793238228]], "store_stream_bytes": 47503532, "wall_ns": 1792909841265299503}
[2026-10-27T06:59:25Z] L 2026-10-25T12:21:15Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "dc4d9cdb8bbc40fcb21d71738c9e0f76", "phase_at": 375, "resumed": false, "run": 1792930875, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792930875795008413}
[2026-10-27T06:59:25Z] L 2026-10-25T12:21:16Z {"assets_n": 25, "bytes_total": 388358906, "closed": 1411, "deferred": 0, "event": "set", "first_T": 1792908000, "last_T": 1792929600, "open": 0, "run": 1792930875, "sha256": "43fc78ead3153cabe72af98e43296e815cee4b043f94ebe4090f7922410a631a", "tag": "pairbook-streams-1792930875", "unclosed": 0, "wall_ns": 1792930876950147849, "windows_considered": 1411}
[2026-10-27T06:59:25Z] L 2026-10-25T12:21:56Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 423384980, "run": 1792930875, "sent": 25, "wall_ns": 1792930916701631274}
[2026-10-27T06:59:25Z] L 2026-10-25T12:30:18Z {"assets_n": 25, "bytes_total": 388358906, "event": "verify", "release_id": 423384980, "run": 1792930875, "verify_sha256": "7199d414fc19a791728517428d7aa0d7dca6a5ec10b5ed52508d6ead222ce23b", "wall_ns": 1792931418332756731}
[2026-10-27T06:59:25Z] L 2026-10-25T12:30:19Z {"already": 0, "event": "delete", "free_after": 11952427008, "free_before": 11563986944, "freed": 388358906, "gone": 25, "removed": 25, "run": 1792930875, "wall_ns": 1792931419236539924, "windows_kept": 25}
[2026-10-27T06:59:25Z] L 2026-10-25T12:30:19Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2656081", "NRestarts": "4", "ns": 1792931419267712344}, "phase": 19, "run": 1792930875, "wall_ns": 1792931419267721228}
[2026-10-27T06:59:25Z] L 2026-10-25T12:30:19Z {"event": "kill", "exit": 0, "phase": 19, "run": 1792930875, "wall_ns": 1792931419275521251}
[2026-10-27T06:59:25Z] L 2026-10-25T12:30:49Z {"NRestarts": "5", "W": 1792931400, "event": "restart", "free_bytes": 11952394240, "gap_ns": 5694910716, "pid": 2699540, "run": 1792930875, "stopped": 2656081, "stream_bytes": 7657936, "wall_ns": 1792931449311119152}
[2026-10-27T06:59:25Z] L 2026-10-25T12:45:41Z {"T": 1792931400, "event": "resume", "reading": "PASS", "run": 1792930875, "wall_ns": 1792932341001387430}
[2026-10-27T06:59:25Z] L 2026-10-25T12:45:41Z {"assets_n": 25, "bytes_total": 388358906, "ended_outside": 0, "event": "complete", "free_bytes": 11957125120, "peak_rss": 37806080, "rate_per_day": 1491298199, "requests": 55, "run": 1792930875, "started_outside": 0, "stops": [["the cap", 1793394584], ["the floor, base 43500000 bytes a day", 1793352132], ["the floor, base 187760570 bytes a day", 1793316065]], "store_stream_bytes": 21497767, "wall_ns": 1792932341025563566}
[2026-10-27T06:59:25Z] L 2026-10-26T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "8584c3696bc84beabdeb1ca499b0e544", "phase_at": 20, "resumed": false, "run": 1792983620, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1792983620518055251}
[2026-10-27T06:59:25Z] L 2026-10-26T03:00:22Z {"assets_n": 58, "bytes_total": 916704432, "closed": 1469, "deferred": 0, "event": "set", "first_T": 1792930500, "last_T": 1792981800, "open": 1, "run": 1792983620, "sha256": "913dcdd8413b728691f2b650fe3c8976364914ee1eba3522c2f53ca369fb30ab", "tag": "pairbook-streams-1792983620", "unclosed": 0, "wall_ns": 1792983622740093015, "windows_considered": 1469}
[2026-10-27T06:59:25Z] L 2026-10-26T03:01:59Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 423817688, "run": 1792983620, "sent": 58, "wall_ns": 1792983719703134830}
[2026-10-27T06:59:25Z] L 2026-10-26T03:05:06Z {"assets_n": 58, "bytes_total": 916704432, "event": "verify", "release_id": 423817688, "run": 1792983620, "verify_sha256": "4b8501bdacf1d679fcf00c98c268442a402f9bd7827fb91eb72f02718bd8c26f", "wall_ns": 1792983906710622900}
[2026-10-27T06:59:25Z] L 2026-10-26T03:05:08Z {"already": 0, "event": "delete", "free_after": 11946442752, "free_before": 11029581824, "freed": 916704432, "gone": 58, "removed": 58, "run": 1792983620, "wall_ns": 1792983908696914608, "windows_kept": 58}
[2026-10-27T06:59:25Z] L 2026-10-26T03:05:08Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2699540", "NRestarts": "5", "ns": 1792983908710249772}, "phase": 308, "run": 1792983620, "wall_ns": 1792983908710256069}
[2026-10-27T06:59:25Z] L 2026-10-26T03:05:08Z {"event": "kill", "exit": 0, "phase": 308, "run": 1792983620, "wall_ns": 1792983908715303657}
[2026-10-27T06:59:25Z] L 2026-10-26T03:05:38Z {"NRestarts": "6", "W": 1792983600, "event": "restart", "free_bytes": 11946414080, "gap_ns": 5581774411, "pid": 2770458, "run": 1792983620, "stopped": 2699540, "stream_bytes": 34024644, "wall_ns": 1792983938750063669}
[2026-10-27T06:59:25Z] L 2026-10-26T03:15:41Z {"T": 1792983600, "event": "resume", "reading": "PASS", "run": 1792983620, "wall_ns": 1792984541000323969}
[2026-10-27T06:59:25Z] L 2026-10-26T03:15:41Z {"assets_n": 58, "bytes_total": 916704432, "ended_outside": 0, "event": "complete", "free_bytes": 11918241792, "peak_rss": 38457344, "rate_per_day": 1517303887, "requests": 121, "run": 1792983620, "started_outside": 0, "stops": [["the cap", 1793436542], ["the floor, base 43500000 bytes a day", 1793395185], ["the floor, base 187760570 bytes a day", 1793360442]], "store_stream_bytes": 62219890, "wall_ns": 1792984541019791682}
[2026-10-27T06:59:25Z] L 2026-10-27T03:00:20Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "8161f6f84e374a81b8f15f552dc1068f", "phase_at": 20, "resumed": false, "run": 1793070020, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1793070020507215151}
[2026-10-27T06:59:25Z] L 2026-10-27T03:00:24Z {"assets_n": 96, "bytes_total": 1959815400, "closed": 1565, "deferred": 0, "event": "set", "first_T": 1792982700, "last_T": 1793068200, "open": 1, "run": 1793070020, "sha256": "b22b04717c264733efb4e6c54b17a4f04b4cf497307ce7cbc1dbccf79af6f045", "tag": "pairbook-streams-1793070020", "unclosed": 0, "wall_ns": 1793070024927704156, "windows_considered": 1565}
[2026-10-27T06:59:25Z] L 2026-10-27T03:03:17Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 424990406, "run": 1793070020, "sent": 96, "wall_ns": 1793070197305284031}
[2026-10-27T06:59:25Z] L 2026-10-27T03:07:33Z {"assets_n": 96, "bytes_total": 1959815400, "event": "verify", "release_id": 424990406, "run": 1793070020, "verify_sha256": "82492ce24756e9521e51c44fddb037b5b1262569d863842f5ed9b7c10f33a3aa", "wall_ns": 1793070453989840156}
[2026-10-27T06:59:25Z] L 2026-10-27T03:07:38Z {"already": 0, "event": "delete", "free_after": 11929825280, "free_before": 9969586176, "freed": 1959815400, "gone": 96, "removed": 96, "run": 1793070020, "wall_ns": 1793070458155442541, "windows_kept": 96}
[2026-10-27T06:59:25Z] L 2026-10-27T03:07:38Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2770458", "NRestarts": "6", "ns": 1793070458167802631}, "phase": 458, "run": 1793070020, "wall_ns": 1793070458167808262}
[2026-10-27T06:59:25Z] L 2026-10-27T03:07:38Z {"event": "kill", "exit": 0, "phase": 458, "run": 1793070020, "wall_ns": 1793070458172966556}
[2026-10-27T06:59:25Z] L 2026-10-27T03:08:08Z {"NRestarts": "7", "W": 1793070000, "event": "restart", "free_bytes": 11929817088, "gap_ns": 5629591291, "pid": 2926125, "run": 1793070020, "stopped": 2770458, "stream_bytes": 10259353, "wall_ns": 1793070488206267927}
[2026-10-27T06:59:25Z] L 2026-10-27T03:15:41Z {"T": 1793070000, "event": "resume", "reading": "PASS", "run": 1793070020, "wall_ns": 1793070941000352253}
[2026-10-27T06:59:25Z] L 2026-10-27T03:15:41Z {"assets_n": 96, "bytes_total": 1959815400, "ended_outside": 0, "event": "complete", "free_bytes": 11909517312, "peak_rss": 38588416, "rate_per_day": 1959815400, "requests": 197, "run": 1793070020, "started_outside": 0, "stops": [["the cap", 1793422282], ["the floor, base 43500000 bytes a day", 1793390502], ["the floor, base 187760570 bytes a day", 1793369036]], "store_stream_bytes": 30511083, "wall_ns": 1793070941021327906}
[2026-10-27T06:59:25Z] L 2026-10-27T06:25:40Z {"commit": "d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3", "event": "start", "file_sha256": "46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4", "invocation": "f2bbe464ea6247ffb7a7ae64fd87e298", "phase_at": 640, "resumed": false, "run": 1793082340, "tz27_sha256": "2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673", "wall_ns": 1793082340818570166}
[2026-10-27T06:59:25Z] L 2026-10-27T06:25:41Z {"assets_n": 14, "bytes_total": 263576978, "closed": 1579, "deferred": 0, "event": "set", "first_T": 1793069100, "last_T": 1793080800, "open": 1, "run": 1793082340, "sha256": "d07b63c400f76c84cf3740cf4ab57fb6d510480db18bcb1ba7e6e318dcb214ab", "tag": "pairbook-streams-1793082340", "unclosed": 0, "wall_ns": 1793082341727016687, "windows_considered": 1579}
[2026-10-27T06:59:25Z] L 2026-10-27T06:30:40Z {"created": true, "credential": "the primary checkout's remote URL", "event": "upload", "held": 0, "release_id": 425100926, "run": 1793082340, "sent": 14, "wall_ns": 1793082640899717863}
[2026-10-27T06:59:25Z] L 2026-10-27T06:32:57Z {"assets_n": 14, "bytes_total": 263576978, "event": "verify", "release_id": 425100926, "run": 1793082340, "verify_sha256": "f766063a22195b34d8aa9816143aae40abb263926a0efa18b2579a74e2e3b1cb", "wall_ns": 1793082777388141465}
[2026-10-27T06:59:25Z] L 2026-10-27T06:32:57Z {"already": 0, "event": "delete", "free_after": 11901890560, "free_before": 11638247424, "freed": 263576978, "gone": 14, "removed": 14, "run": 1793082340, "wall_ns": 1793082777972102921, "windows_kept": 14}
[2026-10-27T06:59:25Z] L 2026-10-27T06:32:57Z {"event": "mark", "mark": {"ActiveState": "active", "MainPID": "2926125", "NRestarts": "7", "ns": 1793082777983388190}, "phase": 177, "run": 1793082340, "wall_ns": 1793082777983393335}
[2026-10-27T06:59:25Z] L 2026-10-27T06:32:57Z {"event": "kill", "exit": 0, "phase": 177, "run": 1793082340, "wall_ns": 1793082777988317237}
[2026-10-27T06:59:25Z] L 2026-10-27T06:33:28Z {"NRestarts": "8", "W": 1793082600, "event": "restart", "free_bytes": 11901857792, "gap_ns": 5575284878, "pid": 2943176, "run": 1793082340, "stopped": 2926125, "stream_bytes": 21923757, "wall_ns": 1793082808020709846}
[2026-10-27T06:59:25Z] L 2026-10-27T06:45:41Z {"T": 1793082600, "event": "resume", "reading": "PASS", "run": 1793082340, "wall_ns": 1793083541000323947}
[2026-10-27T06:59:25Z] L 2026-10-27T06:45:41Z {"assets_n": 14, "bytes_total": 263576978, "ended_outside": 0, "event": "complete", "free_bytes": 11874836480, "peak_rss": 38199296, "rate_per_day": 1807384992, "requests": 33, "run": 1793082340, "started_outside": 0, "stops": [["the cap", 1793463626], ["the floor, base 43500000 bytes a day", 1793427801], ["the floor, base 187760570 bytes a day", 1793402909]], "store_stream_bytes": 49061527, "wall_ns": 1793083541019844382}
[2026-10-27T06:59:25Z] run 1791731892 2026-10-11T15:18:12Z, off-calendar, second 55092 of the day: 10 records; terminal complete; set pairbook-streams-1791731892: 28 files, 430047476 bytes, windows 1791706500 to 1791730800; restart: window 1791731700, pid 851381 after 815823, NRestarts 3; complete: requests 61, started outside 0, ended outside 0, rate 1474448489 a day
[2026-10-27T06:59:25Z] run 1791774020 2026-10-12T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1791774020: 46 files, 794522712 bytes, windows 1791731700 to 1791772200; restart: window 1791774000, pid 911226 after 851381, NRestarts 4; complete: requests 97, started outside 0, ended outside 0, rate 1658134355 a day
[2026-10-27T06:59:25Z] run 1791860420 2026-10-13T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1791860420: 96 files, 1925987888 bytes, windows 1791773100 to 1791858600; restart: window 1791860400, pid 1027378 after 911226, NRestarts 5; complete: requests 197, started outside 0, ended outside 0, rate 1925987888 a day
[2026-10-27T06:59:25Z] run 1791946820 2026-10-14T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1791946820: 96 files, 2039544263 bytes, windows 1791859500 to 1791945000; restart: window 1791946800, pid 1155982 after 1027378, NRestarts 6; complete: requests 197, started outside 0, ended outside 0, rate 2039544263 a day
[2026-10-27T06:59:25Z] run 1792033220 2026-10-15T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792033220: 96 files, 2103892072 bytes, windows 1791945900 to 1792031400; restart: window 1792034100, pid 1284485 after 1155982, NRestarts 7; complete: requests 197, started outside 0, ended outside 0, rate 2103892072 a day
[2026-10-27T06:59:25Z] run 1792045110 2026-10-15T06:18:30Z, off-calendar, second 22710 of the day: 10 records; terminal complete; set pairbook-streams-1792045110: 14 files, 352241341 bytes, windows 1792032300 to 1792044000; restart: window 1792044900, pid 1312748 after 1284485, NRestarts 8; complete: requests 33, started outside 0, ended outside 0, rate 2415369195 a day
[2026-10-27T06:59:25Z] run 1792119620 2026-10-16T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792119620: 82 files, 1804368058 bytes, windows 1792044900 to 1792117800; restart: window 1792119600, pid 1420617 after 1312748, NRestarts 9; complete: requests 169, started outside 0, ended outside 0, rate 2112430897 a day
[2026-10-27T06:59:25Z] run 1792206020 2026-10-17T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792206020: 96 files, 2048827436 bytes, windows 1792118700 to 1792204200; restart: window 1792206000, pid 1560378 after 1420617, NRestarts 10; complete: requests 197, started outside 0, ended outside 0, rate 2048827436 a day
[2026-10-27T06:59:25Z] run 1792226137 2026-10-17T08:35:37Z, off-calendar, second 30937 of the day: 10 records; terminal complete; set pairbook-streams-1792226137: 23 files, 397545662 bytes, windows 1792205100 to 1792224900; restart: window 1792226700, pid 1595407 after 1560378, NRestarts 11; complete: requests 51, started outside 0, ended outside 0, rate 1659321024 a day
[2026-10-27T06:59:25Z] run 1792292420 2026-10-18T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792292420: 73 files, 1197040692 bytes, windows 1792225800 to 1792290600; restart: window 1792292400, pid 1692402 after 1595407, NRestarts 12; complete: requests 151, started outside 0, ended outside 0, rate 1574190499 a day
[2026-10-27T06:59:25Z] run 1792378820 2026-10-19T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792378820: 96 files, 1755430954 bytes, windows 1792291500 to 1792377000; restart: window 1792378800, pid 1814768 after 1692402, NRestarts 13; complete: requests 197, started outside 0, ended outside 0, rate 1755430954 a day
[2026-10-27T06:59:25Z] run 1792446859 2026-10-19T21:54:19Z, off-calendar, second 78859 of the day: 10 records; terminal complete; set pairbook-streams-1792446859: 76 files, 1702929677 bytes, windows 1792377900 to 1792445400; restart: window 1792448100, pid 1915093 after 1814768, NRestarts 14; complete: requests 157, started outside 0, ended outside 0, rate 2151069065 a day
[2026-10-27T06:59:25Z] run 1792465220 2026-10-20T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792465220: 20 files, 428604581 bytes, windows 1792446300 to 1792463400; restart: window 1792465200, pid 1942330 after 1915093, NRestarts 15; complete: requests 45, started outside 0, ended outside 0, rate 2057301988 a day
[2026-10-27T06:59:25Z] run 1792495417 2026-10-20T11:23:37Z, off-calendar, second 41017 of the day: 10 records; terminal complete; set pairbook-streams-1792495417: 34 files, 764815296 bytes, windows 1792464300 to 1792494000; restart: window 1792495800, pid 1997029 after 1942330, NRestarts 16; complete: requests 73, started outside 0, ended outside 0, rate 2159478482 a day
[2026-10-27T06:59:25Z] run 1792551620 2026-10-21T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792551620: 62 files, 1362902551 bytes, windows 1792494900 to 1792549800; restart: window 1792551600, pid 2076364 after 1997029, NRestarts 17; complete: requests 129, started outside 0, ended outside 0, rate 2110300724 a day
[2026-10-27T06:59:25Z] run 1792618744 2026-10-21T21:39:04Z, off-calendar, second 77944 of the day: 10 records; terminal complete; set pairbook-streams-1792618744: 75 files, 1697351287 bytes, windows 1792550700 to 1792617300; restart: window 1792619100, pid 2192943 after 2076364, NRestarts 18; complete: requests 155, started outside 0, ended outside 0, rate 2172609647 a day
[2026-10-27T06:59:25Z] run 1792638020 2026-10-22T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792638020: 21 files, 391495954 bytes, windows 1792618200 to 1792636200; restart: window 1792638000, pid 2221487 after 2192943, NRestarts 19; complete: requests 47, started outside 0, ended outside 0, rate 1789695789 a day
[2026-10-27T06:59:25Z] run 1792650248 2026-10-22T06:24:08Z, off-calendar, second 23048 of the day: 10 records; terminal complete; set pairbook-streams-1792650248: 14 files, 280783691 bytes, windows 1792637100 to 1792648800; restart: window 1792650600, pid 2250075 after 2241902, NRestarts 1; complete: requests 33, started outside 0, ended outside 0, rate 1925373881 a day
[2026-10-27T06:59:25Z] run 1792724420 2026-10-23T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792724420: 82 files, 1595061931 bytes, windows 1792649700 to 1792722600; restart: window 1792724400, pid 2371078 after 2250075, NRestarts 2; complete: requests 169, started outside 0, ended outside 0, rate 1867389577 a day
[2026-10-27T06:59:25Z] run 1792810820 2026-10-24T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792810820: 96 files, 1928035986 bytes, windows 1792723500 to 1792809000; restart: window 1792810800, pid 2510977 after 2388406, NRestarts 1; complete: requests 197, started outside 0, ended outside 0, rate 1928035986 a day
[2026-10-27T06:59:25Z] run 1792850109 2026-10-24T13:55:09Z, off-calendar, second 50109 of the day: 10 records; terminal complete; set pairbook-streams-1792850109: 44 files, 827830635 bytes, windows 1792809900 to 1792848600; restart: window 1792850400, pid 2568040 after 2510977, NRestarts 2; complete: requests 93, started outside 0, ended outside 0, rate 1806175930 a day
[2026-10-27T06:59:25Z] run 1792897220 2026-10-25T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792897220: 52 files, 684213553 bytes, windows 1792849500 to 1792895400; restart: window 1792897200, pid 2636308 after 2568040, NRestarts 3; complete: requests 109, started outside 0, ended outside 0, rate 1263163482 a day
[2026-10-27T06:59:25Z] run 1792908757 2026-10-25T06:12:37Z, off-calendar, second 22357 of the day: 10 records; terminal complete; set pairbook-streams-1792908757: 13 files, 253766917 bytes, windows 1792896300 to 1792907100; restart: window 1792908900, pid 2656081 after 2636308, NRestarts 4; complete: requests 31, started outside 0, ended outside 0, rate 1873971079 a day
[2026-10-27T06:59:25Z] run 1792930875 2026-10-25T12:21:15Z, off-calendar, second 44475 of the day: 10 records; terminal complete; set pairbook-streams-1792930875: 25 files, 388358906 bytes, windows 1792908000 to 1792929600; restart: window 1792931400, pid 2699540 after 2656081, NRestarts 5; complete: requests 55, started outside 0, ended outside 0, rate 1491298199 a day
[2026-10-27T06:59:25Z] run 1792983620 2026-10-26T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1792983620: 58 files, 916704432 bytes, windows 1792930500 to 1792981800; restart: window 1792983600, pid 2770458 after 2699540, NRestarts 6; complete: requests 121, started outside 0, ended outside 0, rate 1517303887 a day
[2026-10-27T06:59:25Z] run 1793070020 2026-10-27T03:00:20Z, calendar: 10 records; terminal complete; set pairbook-streams-1793070020: 96 files, 1959815400 bytes, windows 1792982700 to 1793068200; restart: window 1793070000, pid 2926125 after 2770458, NRestarts 7; complete: requests 197, started outside 0, ended outside 0, rate 1959815400 a day
[2026-10-27T06:59:25Z] run 1793082340 2026-10-27T06:25:40Z, off-calendar, second 23140 of the day: 10 records; terminal complete; set pairbook-streams-1793082340: 14 files, 263576978 bytes, windows 1793069100 to 1793080800; restart: window 1793082600, pid 2943176 after 2926125, NRestarts 8; complete: requests 33, started outside 0, ended outside 0, rate 1807384992 a day
[2026-10-27T06:59:25Z] set pairbook-streams-1791731892 run 1791731892 sha256 ec3983419485fa67317468917eb7b60e2d0e529be4334c7297831ff562471ad0: 28 files, 430047476 bytes, windows 1791706500 to 1791730800
[2026-10-27T06:59:25Z] set pairbook-streams-1791774020 run 1791774020 sha256 c8f02de3fbed47c4cfa91e66d774427f20990f634d271237bf3c6f25887ffb99: 46 files, 794522712 bytes, windows 1791731700 to 1791772200
[2026-10-27T06:59:25Z] set pairbook-streams-1791860420 run 1791860420 sha256 de9209f2e76e5c42bd1395ea6e9c17ab0fc4c497be6a9311cd1e07c101f9b777: 96 files, 1925987888 bytes, windows 1791773100 to 1791858600
[2026-10-27T06:59:25Z] set pairbook-streams-1791946820 run 1791946820 sha256 9c78ba5221e0bc8d9d8699d920e17c58d76b6052fce7c0e86af4948bdc38aa1e: 96 files, 2039544263 bytes, windows 1791859500 to 1791945000
[2026-10-27T06:59:25Z] set pairbook-streams-1792033220 run 1792033220 sha256 3272c87234da82333365144d0c39bb0f75e895943e7e34ec7ff1e559c1ad8715: 96 files, 2103892072 bytes, windows 1791945900 to 1792031400
[2026-10-27T06:59:25Z] set pairbook-streams-1792045110 run 1792045110 sha256 0337b76512886f5dd78d71cfb303a343631f73624e2eb539ed79ed7f32cc0b8e: 14 files, 352241341 bytes, windows 1792032300 to 1792044000
[2026-10-27T06:59:25Z] set pairbook-streams-1792119620 run 1792119620 sha256 adc52d666ace24c2145e55ef9d62602717d7726c791319304613be33c58459b6: 82 files, 1804368058 bytes, windows 1792044900 to 1792117800
[2026-10-27T06:59:25Z] set pairbook-streams-1792206020 run 1792206020 sha256 0915abd5810c2b901012aa6d34388eabcc76d7be8b327d651632ac9335bbe188: 96 files, 2048827436 bytes, windows 1792118700 to 1792204200
[2026-10-27T06:59:25Z] set pairbook-streams-1792226137 run 1792226137 sha256 3db64b34a3949064d28cadc5a023e4402ebacc5cf7a2adab2fe09d13971312c4: 23 files, 397545662 bytes, windows 1792205100 to 1792224900
[2026-10-27T06:59:25Z] set pairbook-streams-1792292420 run 1792292420 sha256 7ddfeae4a937bc90c14d8047d3ab843035a2be145d8d407738f9620b098c0b08: 73 files, 1197040692 bytes, windows 1792225800 to 1792290600
[2026-10-27T06:59:25Z] set pairbook-streams-1792378820 run 1792378820 sha256 948f4d39cca953e07be1c1c561f5115f6200f5aa8330fe78434c058d6e607528: 96 files, 1755430954 bytes, windows 1792291500 to 1792377000
[2026-10-27T06:59:25Z] set pairbook-streams-1792446859 run 1792446859 sha256 8491aab13dd6df082e8a4e847bd4e676a5edbeabd050e9a1767a79d7ecfb72d3: 76 files, 1702929677 bytes, windows 1792377900 to 1792445400
[2026-10-27T06:59:25Z] set pairbook-streams-1792465220 run 1792465220 sha256 08a4bf67291e8988351d7b031e9a6250ded7ec726fb2a80a1c28559d6b827e6b: 20 files, 428604581 bytes, windows 1792446300 to 1792463400
[2026-10-27T06:59:25Z] set pairbook-streams-1792495417 run 1792495417 sha256 e323ee33788d09b6cc52062cea9cd4914bc06d83a423f00e8704115f5ee8077e: 34 files, 764815296 bytes, windows 1792464300 to 1792494000
[2026-10-27T06:59:25Z] set pairbook-streams-1792551620 run 1792551620 sha256 86c50466510f2054e4aa0455af33787059c1cc16b6a2f3dc81b5ef002ecb9ae5: 62 files, 1362902551 bytes, windows 1792494900 to 1792549800
[2026-10-27T06:59:25Z] set pairbook-streams-1792618744 run 1792618744 sha256 14628f1239ce9548ab9a88bfae0a8017382eac3a6c54f823b79c7acf8e9f2d70: 75 files, 1697351287 bytes, windows 1792550700 to 1792617300
[2026-10-27T06:59:25Z] set pairbook-streams-1792638020 run 1792638020 sha256 bcccbdcea9b48dfb0ce8b98e2ce6eb1faeb741091d2f4b96a260cd633af8810d: 21 files, 391495954 bytes, windows 1792618200 to 1792636200
[2026-10-27T06:59:25Z] set pairbook-streams-1792650248 run 1792650248 sha256 6204f5ff7868ba1bc1a8e10697a44aa9a3b4ede37177620d9dbef69d51672bb0: 14 files, 280783691 bytes, windows 1792637100 to 1792648800
[2026-10-27T06:59:25Z] set pairbook-streams-1792724420 run 1792724420 sha256 d0e560a3669a7231dea88f79bea44078c0e31e7cff8a374af08de1b5b280bf5c: 82 files, 1595061931 bytes, windows 1792649700 to 1792722600
[2026-10-27T06:59:25Z] set pairbook-streams-1792810820 run 1792810820 sha256 d1416ac8255bd8004a8f1da09afde202f94a83d5029c27f14c032b4b3498eddc: 96 files, 1928035986 bytes, windows 1792723500 to 1792809000
[2026-10-27T06:59:25Z] set pairbook-streams-1792850109 run 1792850109 sha256 edf4e1d7074f4c588c91769d35b856ab376667aadb5f856ba315f3dd154ecd17: 44 files, 827830635 bytes, windows 1792809900 to 1792848600
[2026-10-27T06:59:25Z] set pairbook-streams-1792897220 run 1792897220 sha256 b0a814654d2ed487aa2618b9b3f01fb4a478d201fef2e908310878bda169e28c: 52 files, 684213553 bytes, windows 1792849500 to 1792895400
[2026-10-27T06:59:25Z] set pairbook-streams-1792908757 run 1792908757 sha256 7eebdd6b04decc80a3af5aae9bd6f5fe4e9d65312009813c20cbeeeb055e9956: 13 files, 253766917 bytes, windows 1792896300 to 1792907100
[2026-10-27T06:59:25Z] set pairbook-streams-1792930875 run 1792930875 sha256 43fc78ead3153cabe72af98e43296e815cee4b043f94ebe4090f7922410a631a: 25 files, 388358906 bytes, windows 1792908000 to 1792929600
[2026-10-27T06:59:25Z] set pairbook-streams-1792983620 run 1792983620 sha256 913dcdd8413b728691f2b650fe3c8976364914ee1eba3522c2f53ca369fb30ab: 58 files, 916704432 bytes, windows 1792930500 to 1792981800
[2026-10-27T06:59:25Z] set pairbook-streams-1793070020 run 1793070020 sha256 b22b04717c264733efb4e6c54b17a4f04b4cf497307ce7cbc1dbccf79af6f045: 96 files, 1959815400 bytes, windows 1792982700 to 1793068200
[2026-10-27T06:59:25Z] set pairbook-streams-1793082340 run 1793082340 sha256 d07b63c400f76c84cf3740cf4ab57fb6d510480db18bcb1ba7e6e318dcb214ab: 14 files, 263576978 bytes, windows 1793069100 to 1793080800
[2026-10-27T06:59:25Z] the archive's assets: 1528 windows, 1528 files, to window 1793080800; at or after 1792754100: 364 windows, to 1793080800
[2026-10-27T06:59:26Z] tags on origin 27: ['pairbook-streams-1791731892', 'pairbook-streams-1791774020', 'pairbook-streams-1791860420', 'pairbook-streams-1791946820', 'pairbook-streams-1792033220', 'pairbook-streams-1792045110', 'pairbook-streams-1792119620', 'pairbook-streams-1792206020', 'pairbook-streams-1792226137', 'pairbook-streams-1792292420', 'pairbook-streams-1792378820', 'pairbook-streams-1792446859', 'pairbook-streams-1792465220', 'pairbook-streams-1792495417', 'pairbook-streams-1792551620', 'pairbook-streams-1792618744', 'pairbook-streams-1792638020', 'pairbook-streams-1792650248', 'pairbook-streams-1792724420', 'pairbook-streams-1792810820', 'pairbook-streams-1792850109', 'pairbook-streams-1792897220', 'pairbook-streams-1792908757', 'pairbook-streams-1792930875', 'pairbook-streams-1792983620', 'pairbook-streams-1793070020', 'pairbook-streams-1793082340']
[2026-10-27T06:59:26Z] complete runs' sets 27; their tags not on origin []; halted False; runs without a terminal record []
[2026-10-27T06:59:26Z] malloc tuned: True
[2026-10-27T06:59:26Z] peak memory of this run: 43024384 bytes
[2026-10-27T06:59:26Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

The second read at §3.11, `logs/91-archive-2.log`, is identical line for line to the first once the stamps are removed, but for its peak memory, `42,627,072` bytes against `43,024,384`: the ledger `64,237` bytes, `c066f771d34694fc73235bd28b0ff5088f7c00c9815562d3cbe97548cbba0635`, 270 complete records, at both. No run of the archive started during this TZ.

**Since map §2.5's account** (19 runs to 2026-10-23 03:00:20 UTC): eight runs, all `complete`, none with a request
started or ended outside the idle stretch, no window skipped between sets, every set's tag on `origin`, the archive not
halted. Four on the calendar — `1792810820` (2026-10-24, 96 files, windows `1792723500` … `1792809000`), `1792897220`
(2026-10-25, 52 files), `1792983620` (2026-10-26, 58 files) and `1793070020` (2026-10-27, 96 files, windows
`1792982700` … `1793068200`, `1,959,815,400` bytes) — and four off it (below). The assets reach window `1793080800`;
**364 windows at or after `1792754100`, contiguous, the last candidate `1793068200` among them**, moved by the calendar
run of 2026-10-27 03:00:20 UTC, `complete` at 03:15:41. So `fetch` waited 0 s for the archive.

**Each run off the calendar, set beside §0.3's boots, the timer's journal, systemd's records and the package history**
(map §7 item 115). The boots: one, since 2026-08-02 07:24:34 UTC. The timer's journal since 2026-10-22:
`-- No entries --`. §0.3's `tail -n 80` of systemd's records reaches back only to 2026-10-25 06:17:57, so one further
`journalctl` read, `logs/62-offcalendar-journal.log` (§6 item 4), took PID 1's records in the twenty minutes before each:

| run | start, UTC | the last `daemon-reload` before it, in PID 1's records | gap |
|---|---|---|---|
| `1792850109` | 2026-10-24 13:55:09 | a burst of ten `systemctl daemon-reload`s requested by `crypto-deploy.service`, 13:45:03 to 13:45:08, finished 13:45:08 | 601 s |
| `1792908757` | 2026-10-25 06:12:37 | a burst of ten reloads by `crypto-deploy.service`, 06:02:33 to 06:02:37, finished 06:02:37 | 600 s |
| `1792930875` | 2026-10-25 12:21:15 | a burst of ten reloads by `crypto-deploy.service`, 12:11:12 to 12:11:15, finished 12:11:15 | 600 s |
| `1793082340` | 2026-10-27 06:25:40 | two reloads requested by `apt-daily-upgrade.service`, 06:15:39 to 06:15:40, during `unattended-upgrade` of libbrotli1 and nginx | 600 s |

Each started 600 s, the timer's `OnActiveSec`, after the last reload of a burst. `crypto-deploy.service` also started
every five minutes in these spans without a reload, and none of those starts was followed by a run. The package
upgrade of 2026-10-27 restarted neither capture unit. No TZ ran at any of these instants, and each run restarted the
pair book once inside its band and completed. This is a coincidence of printed records, not a measured cause.

`logs/62-offcalendar-journal.log`, verbatim:

```text
2026-10-27T07:04:06.667707337Z
$ journalctl _PID=1 -o short-iso --since '2026-10-24 13:40:00' --until '2026-10-24 14:00:00' --no-pager | grep -E 'Reload|btc-pairbook|btc-recorder|apt-daily|unattended|crypto-deploy'
2026-10-24T13:45:00+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-24T13:45:03+00:00 vultr systemd[1]: Reloading requested from client PID 2565457 ('systemctl') (unit crypto-deploy.service)...
2026-10-24T13:45:03+00:00 vultr systemd[1]: Reloading...
2026-10-24T13:45:04+00:00 vultr systemd[1]: Reloading finished in 522 ms.
2026-10-24T13:45:04+00:00 vultr systemd[1]: Reloading requested from client PID 2565510 ('systemctl') (unit crypto-deploy.service)...
2026-10-24T13:45:04+00:00 vultr systemd[1]: Reloading...
2026-10-24T13:45:04+00:00 vultr systemd[1]: Reloading finished in 464 ms.
2026-10-24T13:45:04+00:00 vultr systemd[1]: Reloading requested from client PID 2565583 ('systemctl') (unit crypto-deploy.service)...
2026-10-24T13:45:04+00:00 vultr systemd[1]: Reloading...
2026-10-24T13:45:05+00:00 vultr systemd[1]: Reloading finished in 486 ms.
2026-10-24T13:45:05+00:00 vultr systemd[1]: Reloading requested from client PID 2565644 ('systemctl') (unit crypto-deploy.service)...
2026-10-24T13:45:05+00:00 vultr systemd[1]: Reloading...
2026-10-24T13:45:05+00:00 vultr systemd[1]: Reloading finished in 490 ms.
2026-10-24T13:45:05+00:00 vultr systemd[1]: Starting apt-daily.service - Daily apt download activities...
2026-10-24T13:45:06+00:00 vultr systemd[1]: Reloading requested from client PID 2565703 ('systemctl') (unit crypto-deploy.service)...
2026-10-24T13:45:06+00:00 vultr systemd[1]: Reloading...
2026-10-24T13:45:06+00:00 vultr systemd[1]: Reloading finished in 466 ms.
2026-10-24T13:45:06+00:00 vultr systemd[1]: Reloading requested from client PID 2565764 ('systemctl') (unit crypto-deploy.service)...
2026-10-24T13:45:06+00:00 vultr systemd[1]: Reloading...
2026-10-24T13:45:07+00:00 vultr systemd[1]: Reloading finished in 458 ms.
2026-10-24T13:45:07+00:00 vultr systemd[1]: Reloading requested from client PID 2565827 ('systemctl') (unit crypto-deploy.service)...
2026-10-24T13:45:07+00:00 vultr systemd[1]: Reloading...
2026-10-24T13:45:07+00:00 vultr systemd[1]: Reloading finished in 265 ms.
2026-10-24T13:45:07+00:00 vultr systemd[1]: Reloading requested from client PID 2565898 ('systemctl') (unit crypto-deploy.service)...
2026-10-24T13:45:07+00:00 vultr systemd[1]: Reloading...
2026-10-24T13:45:07+00:00 vultr systemd[1]: Reloading finished in 414 ms.
2026-10-24T13:45:07+00:00 vultr systemd[1]: Reloading requested from client PID 2565963 ('systemctl') (unit crypto-deploy.service)...
2026-10-24T13:45:07+00:00 vultr systemd[1]: Reloading...
2026-10-24T13:45:08+00:00 vultr systemd[1]: Reloading finished in 406 ms.
2026-10-24T13:45:08+00:00 vultr systemd[1]: Reloading requested from client PID 2566045 ('systemctl') (unit crypto-deploy.service)...
2026-10-24T13:45:08+00:00 vultr systemd[1]: Reloading...
2026-10-24T13:45:08+00:00 vultr systemd[1]: Reloading finished in 463 ms.
2026-10-24T13:45:09+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-24T13:45:09+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-24T13:45:09+00:00 vultr systemd[1]: crypto-deploy.service: Consumed 1.792s CPU time, 50.5M memory peak, 0B memory swap peak.
2026-10-24T13:45:17+00:00 vultr systemd[1]: apt-daily.service: Deactivated successfully.
2026-10-24T13:45:17+00:00 vultr systemd[1]: Finished apt-daily.service - Daily apt download activities.
2026-10-24T13:45:17+00:00 vultr systemd[1]: apt-daily.service: Consumed 7.544s CPU time, 74.9M memory peak, 0B memory swap peak.
2026-10-24T13:50:00+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-24T13:50:01+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-24T13:50:01+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-24T13:55:00+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-24T13:55:01+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-24T13:55:01+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-24T13:55:09+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
$ journalctl _PID=1 -o short-iso --since '2026-10-25 05:55:00' --until '2026-10-25 06:20:00' --no-pager | grep -E 'Reload|btc-pairbook|btc-recorder|apt-daily|unattended|crypto-deploy'
2026-10-25T05:57:30+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-25T05:57:31+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-25T05:57:31+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-25T06:02:30+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-25T06:02:33+00:00 vultr systemd[1]: Reloading requested from client PID 2652755 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T06:02:33+00:00 vultr systemd[1]: Reloading...
2026-10-25T06:02:34+00:00 vultr systemd[1]: Reloading finished in 277 ms.
2026-10-25T06:02:34+00:00 vultr systemd[1]: Reloading requested from client PID 2652808 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T06:02:34+00:00 vultr systemd[1]: Reloading...
2026-10-25T06:02:34+00:00 vultr systemd[1]: Reloading finished in 256 ms.
2026-10-25T06:02:34+00:00 vultr systemd[1]: Reloading requested from client PID 2652862 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T06:02:34+00:00 vultr systemd[1]: Reloading...
2026-10-25T06:02:34+00:00 vultr systemd[1]: Reloading finished in 428 ms.
2026-10-25T06:02:34+00:00 vultr systemd[1]: Reloading requested from client PID 2652916 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T06:02:34+00:00 vultr systemd[1]: Reloading...
2026-10-25T06:02:35+00:00 vultr systemd[1]: Reloading finished in 416 ms.
2026-10-25T06:02:35+00:00 vultr systemd[1]: Reloading requested from client PID 2652971 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T06:02:35+00:00 vultr systemd[1]: Reloading...
2026-10-25T06:02:35+00:00 vultr systemd[1]: Reloading finished in 396 ms.
2026-10-25T06:02:35+00:00 vultr systemd[1]: Reloading requested from client PID 2653027 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T06:02:35+00:00 vultr systemd[1]: Reloading...
2026-10-25T06:02:36+00:00 vultr systemd[1]: Reloading finished in 256 ms.
2026-10-25T06:02:36+00:00 vultr systemd[1]: Reloading requested from client PID 2653081 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T06:02:36+00:00 vultr systemd[1]: Reloading...
2026-10-25T06:02:36+00:00 vultr systemd[1]: Reloading finished in 246 ms.
2026-10-25T06:02:36+00:00 vultr systemd[1]: Reloading requested from client PID 2653135 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T06:02:36+00:00 vultr systemd[1]: Reloading...
2026-10-25T06:02:36+00:00 vultr systemd[1]: Reloading finished in 267 ms.
2026-10-25T06:02:36+00:00 vultr systemd[1]: Reloading requested from client PID 2653190 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T06:02:36+00:00 vultr systemd[1]: Reloading...
2026-10-25T06:02:37+00:00 vultr systemd[1]: Reloading finished in 305 ms.
2026-10-25T06:02:37+00:00 vultr systemd[1]: Reloading requested from client PID 2653246 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T06:02:37+00:00 vultr systemd[1]: Reloading...
2026-10-25T06:02:37+00:00 vultr systemd[1]: Reloading finished in 345 ms.
2026-10-25T06:02:37+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-25T06:02:37+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-25T06:02:37+00:00 vultr systemd[1]: crypto-deploy.service: Consumed 1.839s CPU time, 47.5M memory peak, 0B memory swap peak.
2026-10-25T06:07:30+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-25T06:07:31+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-25T06:07:31+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-25T06:12:30+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-25T06:12:31+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-25T06:12:31+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-25T06:12:37+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-25T06:17:31+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-25T06:17:32+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-25T06:17:32+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-25T06:17:57+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2636308 (python) on client request.
2026-10-25T06:17:57+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-25T06:17:57+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 5min 49.959s CPU time, 89.8M memory peak, 34.9M memory swap peak.
2026-10-25T06:18:03+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 4.
2026-10-25T06:18:03+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
$ journalctl _PID=1 -o short-iso --since '2026-10-25 12:05:00' --until '2026-10-25 12:25:00' --no-pager | grep -E 'Reload|btc-pairbook|btc-recorder|apt-daily|unattended|crypto-deploy'
2026-10-25T12:06:04+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-25T12:06:05+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-25T12:06:05+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-25T12:11:05+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading requested from client PID 2696226 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading finished in 323 ms.
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading requested from client PID 2696281 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading finished in 255 ms.
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading requested from client PID 2696335 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading finished in 366 ms.
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading requested from client PID 2696393 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading finished in 271 ms.
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading requested from client PID 2696448 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading finished in 259 ms.
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading requested from client PID 2696501 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading finished in 264 ms.
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading requested from client PID 2696555 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading finished in 270 ms.
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading requested from client PID 2696615 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading finished in 263 ms.
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading requested from client PID 2696668 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:15+00:00 vultr systemd[1]: Reloading finished in 259 ms.
2026-10-25T12:11:15+00:00 vultr systemd[1]: Reloading requested from client PID 2696721 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:15+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:15+00:00 vultr systemd[1]: Reloading finished in 257 ms.
2026-10-25T12:11:15+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-25T12:11:15+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-25T12:11:15+00:00 vultr systemd[1]: crypto-deploy.service: Consumed 4.712s CPU time, 249.9M memory peak, 0B memory swap peak.
2026-10-25T12:16:05+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-25T12:16:05+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-25T12:16:05+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-25T12:21:05+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-25T12:21:05+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-25T12:21:05+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-25T12:21:15+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
$ journalctl _PID=1 -o short-iso --since '2026-10-27 06:10:00' --until '2026-10-27 06:35:00' --no-pager | grep -E 'Reload|btc-pairbook|btc-recorder|apt-daily|unattended|crypto-deploy'
2026-10-27T06:10:30+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-27T06:10:31+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-27T06:10:31+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-27T06:15:30+00:00 vultr systemd[1]: Starting apt-daily-upgrade.service - Daily apt upgrade and clean activities...
2026-10-27T06:15:30+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-27T06:15:31+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-27T06:15:31+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading requested from client PID 2941531 ('systemctl') (unit apt-daily-upgrade.service)...
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading...
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading finished in 323 ms.
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading requested from client PID 2941589 ('systemctl') (unit apt-daily-upgrade.service)...
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading...
2026-10-27T06:15:40+00:00 vultr systemd[1]: Reloading finished in 413 ms.
2026-10-27T06:15:45+00:00 vultr systemd[1]: apt-daily-upgrade.service: Deactivated successfully.
2026-10-27T06:15:45+00:00 vultr systemd[1]: Finished apt-daily-upgrade.service - Daily apt upgrade and clean activities.
2026-10-27T06:15:45+00:00 vultr systemd[1]: apt-daily-upgrade.service: Consumed 10.514s CPU time, 351.9M memory peak, 204.0K memory swap peak.
2026-10-27T06:20:30+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-27T06:20:31+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-27T06:20:31+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-27T06:25:30+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-27T06:25:31+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-27T06:25:31+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-27T06:25:40+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-27T06:30:31+00:00 vultr systemd[1]: Starting crypto-deploy.service - Crypto assistant: install vps/ from main...
2026-10-27T06:30:32+00:00 vultr systemd[1]: crypto-deploy.service: Deactivated successfully.
2026-10-27T06:30:32+00:00 vultr systemd[1]: Finished crypto-deploy.service - Crypto assistant: install vps/ from main.
2026-10-27T06:32:57+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2926125 (python) on client request.
2026-10-27T06:32:58+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-27T06:32:58+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 6min 4.362s CPU time, 120.7M memory peak, 32.1M memory swap peak.
2026-10-27T06:33:03+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 8.
2026-10-27T06:33:03+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
$ journalctl -u btc-recorder.service -u btc-pairbook.service -o short-iso --since 2026-10-23 --no-pager | grep -E "Started|Stopp|Deactivated|restart" 
2026-10-23T03:07:04+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-23T03:07:09+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 2.
2026-10-23T03:07:09+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-23T06:08:56+00:00 vultr systemd[1]: Stopping btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed...
2026-10-23T06:08:56+00:00 vultr systemd[1]: Stopping btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C...
2026-10-23T06:08:56+00:00 vultr systemd[1]: btc-recorder.service: Deactivated successfully.
2026-10-23T06:08:56+00:00 vultr systemd[1]: Stopped btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C.
2026-10-23T06:08:56+00:00 vultr systemd[1]: Started btc-recorder.service - btc-5m-twap recorder, Tier A and Tier C.
2026-10-23T06:08:58+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-23T06:08:58+00:00 vultr systemd[1]: Stopped btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-23T06:08:58+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-24T03:07:45+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-24T03:07:50+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 1.
2026-10-24T03:07:50+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-24T14:04:36+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-24T14:04:41+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 2.
2026-10-24T14:04:41+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-25T03:04:36+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-25T03:04:41+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 3.
2026-10-25T03:04:41+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-25T06:17:57+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-25T06:18:03+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 4.
2026-10-25T06:18:03+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-25T12:30:19+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-25T12:30:24+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 5.
2026-10-25T12:30:24+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-26T03:05:08+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-26T03:05:14+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 6.
2026-10-26T03:05:14+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-27T03:07:38+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-27T03:07:43+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 7.
2026-10-27T03:07:43+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-27T06:32:58+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-27T06:33:03+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 8.
2026-10-27T06:33:03+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
```

### 2.5 The units, at both reads (§3.3, §3.10; V11)

```text
$ I still            # §3.3
[2026-10-27T06:58:32Z] btc-pairbook.service {'MainPID': '2943176', 'NRestarts': '8', 'ActiveState': 'active'}, MemoryCurrent 19156992, MemoryPeak 67203072
[2026-10-27T06:58:32Z] btc-recorder.service {'MainPID': '2388318', 'NRestarts': '0', 'ActiveState': 'active'}, MemoryCurrent 15949824, MemoryPeak 302202880
[2026-10-27T06:58:32Z] btc-pairbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-27T06:58:32Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-27T06:58:32Z] still: recorded
[2026-10-27T06:58:32Z] malloc tuned: True
[2026-10-27T06:58:32Z] peak memory of this run: 35287040 bytes
[2026-10-27T06:58:32Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
$ I still            # §3.10
[2026-10-27T07:46:49Z] btc-pairbook.service {'MainPID': '2943176', 'NRestarts': '8', 'ActiveState': 'active'}, MemoryCurrent 23711744, MemoryPeak 67203072
[2026-10-27T07:46:49Z] btc-recorder.service {'MainPID': '2388318', 'NRestarts': '0', 'ActiveState': 'active'}, MemoryCurrent 126550016, MemoryPeak 302202880
[2026-10-27T07:46:49Z] btc-pairbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-10-27T07:46:49Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-10-27T07:46:49Z] G-STILL PASS: unchanged since 2026-10-27T06:58:32Z
[2026-10-27T07:46:49Z] malloc tuned: True
[2026-10-27T07:46:49Z] peak memory of this run: 34897920 bytes
[2026-10-27T07:46:49Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

**G-STILL PASS: unchanged since 06:58:32 UTC** — the recorder `2388318`, `NRestarts` 0, and the pair book `2943176`, `NRestarts` 8, both `active` at both reads, and no `restart` record in the archive's ledger after §3.3's read. §3.11's `systemctl show` at 07:47:14 UTC (`logs/92-closing.log`, §5.15): the recorder `MemoryCurrent` `15,835,136`, `MemoryPeak` `302,202,880`; the pair book `MemoryCurrent` `2,117,632`, `MemoryPeak` `67,203,072`; the archive's service `inactive`. The pair book's `NRestarts` 8 is the archive's: its ledger's restart records since the package manager's stop and start of 2026-10-23 06:08:56 UTC (TZ-31 report §2.9) chain from pid `2388406` through `2510977`, `2568040`, `2636308`, `2656081`, `2699540`, `2770458` and `2926125` to `2943176`, `NRestarts` 1 to 8, each the restart of one run (§2.4). The recorder has not restarted since 2026-10-23 06:08:56 UTC.

### 2.6 Free space and memory

| instant (UTC) | read | value | bound |
|---|---|---|---|
| 06:57:01 | `df` `/dev/vda2` avail (§0.3) | `11,880,419,328` | `5,400,000,000` |
| 06:57:01 | `MemAvailable` (§0.3) | `277,108` kB = `283,758,592` | `81,928,192` |
| 07:47:00 | `df` `/dev/vda2` avail (§3.11) | `11,680,505,856` | `5,400,000,000` |
| 07:47:00 | `MemAvailable` (§3.11) | `297,808` kB = `304,955,392` | `81,928,192` |
| 06:59:38 | `MemAvailable` and free space (`rehearse`) | `360,185,856`; `11,859,652,608` | `81,928,192`; `5,400,000,000` |
| 07:03:35 | `MemAvailable` and free space (`fetch`) | `336,871,424`; `11,844,763,648` | `81,928,192`; `5,400,000,000` |
| 07:03:56 | `MemAvailable` and free space (`replay 1`) | `318,504,960`; `11,844,374,528` | `81,928,192`; `5,400,000,000` |
| 07:38:44 | `MemAvailable` and free space (`replay 2`) | `338,636,800`; `11,706,097,664` | `81,928,192`; `5,400,000,000` |
| 07:38:51 | `MemAvailable` and free space (`rescore`) | `316,993,536`; `11,706,048,512` | `81,928,192`; `5,400,000,000` |
| 07:46:35 | `MemAvailable` and free space (`score 1`) | `316,129,280`; `11,680,731,136` | `81,928,192`; `5,400,000,000` |
| 07:46:36 | `MemAvailable` and free space (`score 2`) | `301,121,536`; `11,680,649,216` | `81,928,192`; `5,400,000,000` |
| 07:47:14 | `free -b` available (§3.11) | `466,350,080` | — |
| 07:52:27 | `df` avail, after B-RECLAIM-OWN | `11,746,095,104` | — |

### 2.7 Memory peaks (V13)

| mode | log | peak bytes | the Architect's measured peak (§0.4) | ratio | below the floor `81,928,192` | malloc tuned |
|---|---|---|---|---|---|---|
| `fingerprint (I0)` | `02` | `36,200,448` | — | — | yes | True |
| `fingerprint (I)` | `12` | `36,229,120` | — | — | yes | True |
| `selftest` | `20` | `36,728,832` | `31,637,504` | 1.161 | yes | True |
| `still` | `30` | `35,287,040` | — | — | yes | True |
| `scratch` | `31` | `35,155,968` | — | — | yes | True |
| `reclaim (B-RECLAIM-SCRATCH)` | `32` | `36,216,832` | — | — | yes | True |
| `archive` | `40` | `43,024,384` | — | — | yes | True |
| `rehearse` | `50` | `42,799,104` | `36,417,536` | 1.175 | yes | True |
| `fetch` | `61` | `44,986,368` | `31,617,024` | 1.423 | yes | True |
| `replay, first run` | `70` | `53,673,984` | `40,157,184` | 1.337 | yes | True |
| `replay, second run` | `71` | `54,702,080` | `32,890,880` | 1.663 | yes | True |
| `rescore` | `72` | `47,656,960` | `40,423,424` | 1.179 | yes | True |
| `score, first run` | `80` | `54,984,704` | `32,927,744` | 1.670 | yes | True |
| `score, second run` | `81` | `54,980,608` | `32,927,744` | 1.670 | yes | True |
| `still` | `85` | `34,897,920` | — | — | yes | True |
| `archive` | `91` | `42,627,072` | — | — | yes | True |

### 2.8 The timing files (§8)

Each unit's start and end is a line of its run's timing file, printed by the instrument as summary lines:

| run | units | inside the idle stretch | ending after second 590 | longest | download, at most | replay, at most | waited | processor | bytes | retries |
|---|---|---|---|---|---|---|---|---|---|---|
| `rehearse` | 51 | 51 | 0 | 6.5 s | 1.9 s | 5.3 s | 0 s | 131.6 s | `678,739,504` | 0 |
| `replay` | 288 | 288 | 0 | 10.6 s | 2.0 s | 8.8 s | 762 s | 989.9 s | `5,050,052,883` | 0 |
| `rescore` | 18 | 18 | 0 | 7.3 s | 2.1 s | 5.2 s | 381 s | 58.5 s | `312,885,963` | 0 |

**No unit ended after second 590**, and none started before second 15: across the three timing files' 51, 288 and 18 lines the earliest start was second 15.682, 15.067 and 15.2 and the latest end second 199.032, 535.118 and 534.15. No unit started within the archive's calendar guard, and the archive's service read `inactive` at every start.

---

## 3. Publication

| step | outcome |
|---|---|
| branch | `tz-32-our-quoting`, one commit `b601f756edea59adf536d7ef05226d6f06bcef13` above `origin/main` `45f112c`, adding `research/tz32-our-quoting.py` alone |
| push | through `gh`'s stored login, `credential.helper=!gh auth git-credential` (TZ-32 §3.1), `exit=0`; `origin` carried it at **2026-10-27 06:58:07.251338044 UTC** by `ls-remote`, equal to the worktree's `HEAD` |
| pull request | **#31**, `https://github.com/seahomebatumi-ai/btc-5m-twap/pull/31`, open, head `b601f75`, not merged |
| Release | none: TZ-32 §2 item 12 |
| report | this file, straight to `main` in one commit, pushed through the same login |

`logs/10-branch.log`, `logs/13-commit.log`, `logs/14-push.log` and `logs/15-pr.log`, verbatim:

```text
2026-10-27T06:57:44.951181668Z
$ git -C /root/btc-5m-twap fetch origin
exit=0
$ git -C /root/btc-5m-twap worktree add -b tz-32-our-quoting /root/tz32-work/wt origin/main
Preparing worktree (new branch 'tz-32-our-quoting')
branch 'tz-32-our-quoting' set up to track 'origin/main'.
HEAD is now at 45f112c Update SYSTEM-MAP.md
exit=0
2026-10-27T06:58:00.091301941Z
?? research/tz32-our-quoting.py
add exit=0
commit exit=0
b601f75 TZ-32: W1, our quoting - research/tz32-our-quoting.py
45f112c Update SYSTEM-MAP.md
b601f756edea59adf536d7ef05226d6f06bcef13 root <root@vultr.guest> Tue Oct 27 06:58:00 2026 +0000

 research/tz32-our-quoting.py | 2576 ++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 2576 insertions(+)
A	research/tz32-our-quoting.py
remote: 
remote: Create a pull request for 'tz-32-our-quoting' on GitHub by visiting:        
remote:      https://github.com/seahomebatumi-ai/btc-5m-twap/pull/new/tz-32-our-quoting        
remote: 
To https://github.com/seahomebatumi-ai/btc-5m-twap.git
 * [new branch]      tz-32-our-quoting -> tz-32-our-quoting
exit=0
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new branch]      tz-32-our-quoting -> origin/tz-32-our-quoting
exit=0
branch 'tz-32-our-quoting' set up to track 'origin/tz-32-our-quoting'.
exit=0
2026-10-27T06:58:07.251338044Z
b601f756edea59adf536d7ef05226d6f06bcef13	refs/heads/tz-32-our-quoting
b601f756edea59adf536d7ef05226d6f06bcef13
2026-10-27T06:58:18.827445700Z
https://github.com/seahomebatumi-ai/btc-5m-twap/pull/31
exit=0
```

### 3.1 Contract §4.2's separation self-check (V14) — `logs/93-separation.log`, verbatim

Run after the push and the pull request and before this report's commit:

```text
2026-10-27T07:47:21Z
$ git rev-list origin/main | grep -c b601f756edea59adf536d7ef05226d6f06bcef13
0
$ git diff --name-only origin/main origin/tz-32-our-quoting
research/tz32-our-quoting.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
exit=1
$ git diff --name-status --numstat origin/main origin/tz-32-our-quoting
A	research/tz32-our-quoting.py
2576	0	research/tz32-our-quoting.py
{"headRefOid":"b601f756edea59adf536d7ef05226d6f06bcef13","mergedAt":null,"number":31,"state":"OPEN","url":"https://github.com/seahomebatumi-ai/btc-5m-twap/pull/31"}
```

The first line prints `0`: the implementation commit is not on `main`. The branch's diff against `origin/main` names
exactly one path, `A`, 2,576 lines. No `.parquet` or `.zip` is on `main`.

### 3.2 The refs (§0.5) — `logs/05-refs.log`, verbatim

```text
2026-10-27T06:57:28.769414637Z
$ git ls-remote origin
45f112cde92d09bfbe003e8b24c1567dbb60ef18	HEAD
45f112cde92d09bfbe003e8b24c1567dbb60ef18	refs/heads/main
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8	refs/heads/tz-23-maker-m0
6f045cffc3601b589d3b8b7a6a9af6f73991e18b	refs/heads/tz-24-nesting-b2
e8b46a85d61e1a17841962846f6d3012046c2d70	refs/heads/tz-26-nesting-b3-capture
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/heads/tz-27-pairbook-archive
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/heads/tz-28-pairbook-archive-timer
f6425f713034724210dc120d2108bcfad63cadc6	refs/heads/tz-29-maker-m0-second-look
fcd9ca566e9b948f0426707e7c3b5684f7f03b04	refs/heads/tz-30-nesting-b3-measure
404288fb03ffd3619b2183f121d45688def8fba8	refs/heads/tz-31-who-earns
d9e58e8febd8548221598eed137cf40d31496047	refs/pull/1/head
e45f38e89b5ee18e64a16a654b341d74fadcac26	refs/pull/10/head
d34606ee9a592e51293eaad0996c7cae3b84dfcd	refs/pull/11/head
274651805c765bb977c635d75fd1ebdb2c8f550a	refs/pull/12/head
6dc0e24ae1542f98789967bf48057268731a2030	refs/pull/13/head
7ef972397a12bce0cc76b1f58ceda3e5caa43cdc	refs/pull/14/head
ffef5cd822e2e47ce1edd8fff706471a441e9a5f	refs/pull/15/head
f7f171a2e1e8b4b3eafa810f5022f1ca1c5a65b1	refs/pull/16/head
8f1bc93e454275ddb3f0e060bed3bb9f2f9cf31b	refs/pull/17/head
8caa0b41d5cdf9e74e92b11d4317d59a2ee7b567	refs/pull/18/head
ca4bbc1dd583cbb62f3c0c985938d229b526ce7e	refs/pull/19/head
3895356aff853f2fcb1b030b1502acb95b16f0a5	refs/pull/2/head
5076b4305c7800fc7eed0cd3fe05d9577d1b6cf7	refs/pull/20/head
0956da12bd26decbef0fd643b6f223102c7788ba	refs/pull/21/head
e3975b5da44c5328adf3bf3914634cd878842c73	refs/pull/22/head
7f5ae3fe343e0e41f2b3d3d79ccda40e869e9da8	refs/pull/23/head
6f045cffc3601b589d3b8b7a6a9af6f73991e18b	refs/pull/24/head
e8b46a85d61e1a17841962846f6d3012046c2d70	refs/pull/25/head
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/pull/26/head
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/pull/27/head
f6425f713034724210dc120d2108bcfad63cadc6	refs/pull/28/head
fcd9ca566e9b948f0426707e7c3b5684f7f03b04	refs/pull/29/head
ee2f6327390ef4d0c6169d1fba1a2ed4ae936dc3	refs/pull/3/head
404288fb03ffd3619b2183f121d45688def8fba8	refs/pull/30/head
0e13a5c76dfa2469ff25b3b0dd282872decf6f25	refs/pull/4/head
4216c04673ced76b5b2ac60ef57c9abedc46f9b9	refs/pull/5/head
5ed667afd1b53f036b9f938fcce13c0d709cd77f	refs/pull/6/head
c44af687203d14d5d485d4297c04cfb827096af9	refs/pull/7/head
26bbb61aed774a88355dd5204d8b69fda9135a68	refs/pull/8/head
e2625ea2b5473c311d59a48f32540ce39d58e591	refs/pull/9/head
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1791731892
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1791774020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1791860420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1791946820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792033220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792045110
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792119620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792206020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792226137
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792292420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792378820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792446859
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792465220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792495417
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792551620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792618744
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792638020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792650248
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792724420
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792810820
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792850109
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792897220
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792908757
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792930875
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1792983620
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793070020
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3	refs/tags/pairbook-streams-1793082340
d3251aa2bd312409f7b096bfd5968f3bedbd1be5	refs/tags/tz-01a-dataset
ea9290b92b9fa50c22d0560d5d01dfa392af44df	refs/tags/tz-01a-dataset^{}
e299d4e45f48b7efaa8cb18bd54b139fc0627630	refs/tags/tz-27-pairbook-streams
bce5a85be7850a33f95192265b916cc9c5e0aaf1	refs/tags/tz-27-pairbook-streams^{}
exit=0
$ git ls-remote origin | wc -l
71
$ git rev-list --first-parent 7e08b79..origin/main, each with its paths
45f112cde92d09bfbe003e8b24c1567dbb60ef18 2026-10-24T10:46:08+04:00 𝒜𝒱777𝒮𝒜 Update SYSTEM-MAP.md
M	SYSTEM-MAP.md
ade6d9c3db95555dd2f39352ebe50dbd11f6dcc3 2026-10-24T10:44:02+04:00 𝒜𝒱777𝒮𝒜 Add files via upload
A	CryptoTZ/TZ-32-our-quoting.md
$ main carries revision
Revision 2026-10-23-a
$ git ls-remote origin refs/heads/tz-32-our-quoting
exit=0
```

Read at 06:57:28 UTC, before §3.1's push: **71 ref lines** against the map's 63 and §0.5's projection of 67 after the
archive's four calendar runs of 2026-10-24 to 2026-10-27. The eight new lines are eight lightweight
`pairbook-streams-*` tags, one a run of the archive: four calendar runs — `1792810820`, `1792897220`, `1792983620`,
`1793070020` — and four off the calendar — `1792850109`, `1792908757`, `1792930875`, `1793082340` (§2.5). Recorded, not
BLOCKING, as §0.5 allows. `main` carries revision `2026-10-23-a`, and `refs/heads/tz-32-our-quoting` did not exist. The
upload above `7e08b79` is two commits on `main`'s first-parent line: `ade6d9c3db95555dd2f39352ebe50dbd11f6dcc3`
(2026-10-24 06:44:02 UTC, "Add files via upload", `A CryptoTZ/TZ-32-our-quoting.md`) and
`45f112cde92d09bfbe003e8b24c1567dbb60ef18` (2026-10-24 06:46:08 UTC, "Update SYSTEM-MAP.md", `M SYSTEM-MAP.md`).

---

## 4. Gate

| gate | quoted from TZ-32 §4 | deciding number | reading |
|---|---|---|---|
| **G-REHEARSAL** | §4.1's 11 checks equal, exactly | 11 of 11 equal | **PASS** |
| **G-SET** | 288 members, at most 62 non-members before the 288th | 288 members; 1 non-member | **PASS** |
| **G-BOOK** | the rebuilt touch equal to the venue's own at no fewer than 99 in 100 match frames | `417,728` of `418,535`, `0.998071845843` | **PASS** |
| **DETERMINISM** | each of 18 unit files byte for byte the replay's | 18 of 18 | **PASS** |
| **W1** | §4.5: `behind`'s `S >= thr` → W1-EARN; else `front`'s `S <= δ · Sh − thr` → W1-NO-EARN; otherwise UNDECIDABLE | `behind`'s `S` `−2,271.140` against `thr` `525.780`; `front`'s `S` `506.689` against `δ · Sh − thr` `2,726.942` | **W1-NO-EARN** |
| **G-STILL** | unchanged, or the pair book moved by the archive's own restarts alone | both units unchanged, 0 restart records since §3.3 | **PASS** |

W1-NO-EARN rests on `front`'s margin of `+2,220.253` USDC, `+0.346` c a share. W1-EARN
was missed by `−2,796.920` USDC, `−1.440` c a share. Nothing was tuned, and no gate was
reinterpreted.

---

## 5. Validation

### 5.1 V1 — fingerprint (asserted)

`FINGERPRINT PASS` at §0.2 (06:56:49 UTC, from the stage) and at §3.1 (06:57:53, from the worktree). Revision
`2026-10-23-a`; anchors 6 of 6, 4 re-derived; 43 rows, 40 of 40 `frozen` equal, 2 `tracked`, 1 `reported`. §0.1 holds
the lines.

### 5.2 V2 — the host gate (checked by the Executor against the printed values, not asserted by a script; any failure would have been BLOCKED) — `logs/03-host-gate.log`, verbatim

```text
Tue Oct 27 06:57:01 AM UTC 2026
1793084221
1
MemTotal:         978640 kB
MemAvailable:     277108 kB
SwapTotal:       3174396 kB
SwapFree:        2844808 kB
2026-08-02 07:24:32
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
 -5 23a31fad2f064f04b9e138eac29658f3 Sat 2026-06-20 18:48:10 UTC Fri 2026-06-26 14:13:44 UTC
 -4 a38e17445ce341bc8b877be9d3d4f648 Fri 2026-06-26 14:13:52 UTC Tue 2026-07-14 16:15:10 UTC
 -3 5f4d18a6ba8041bd80e7d1e192c5ee28 Tue 2026-07-14 16:15:20 UTC Fri 2026-07-17 01:01:21 UTC
 -2 b1b399c70c6e4dcc934755f70a2ca231 Fri 2026-07-17 01:01:43 UTC Fri 2026-07-24 14:55:46 UTC
 -1 285d6962c92c407d837d1ce329b93aa4 Fri 2026-07-24 14:55:54 UTC Sun 2026-08-02 07:23:49 UTC
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-02 07:24:34 UTC Tue 2026-10-27 06:57:01 UTC
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11880419328
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
3
3.12.3
16570 /root/btc-forensics/tz27-work--archive--set.json
ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd  /root/btc-forensics/tz27-work--archive--set.json
64237 /var/lib/btc-pairbook-archive/ledger.jsonl
MainPID=2388318
Result=success
NRestarts=0
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC

MainPID=2943176
Result=success
NRestarts=8
Id=btc-pairbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Tue 2026-10-27 06:33:03 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-pairbook-archive.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=

Result=success
Id=btc-pairbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-11 15:08:11 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-chainbook.service
ActiveState=inactive
SubState=dead
UnitFileState=disabled
ActiveEnterTimestamp=

MainPID=0
Result=success
NRestarts=0
Id=crypto-deploy.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=

MainPID=2696817
Result=success
NRestarts=0
Id=crypto-announce.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-25 12:11:15 UTC
NEXT                            LEFT LAST                              PASSED UNIT                       ACTIVATES
Tue 2026-10-27 08:38:21 UTC 1h 41min Tue 2026-10-27 03:28:17 UTC 3h 28min ago apt-daily.timer            apt-daily.service
Wed 2026-10-28 03:00:20 UTC      20h Tue 2026-10-27 06:25:40 UTC    31min ago btc-pairbook-archive.timer btc-pairbook-archive.service
Wed 2026-10-28 06:03:24 UTC      23h Tue 2026-10-27 06:15:30 UTC    41min ago apt-daily-upgrade.timer    apt-daily-upgrade.service

3 timers listed.
-- No entries --
2026-10-25T06:17:57+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2636308 (python) on client request.
2026-10-25T06:17:57+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-25T06:17:57+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 5min 49.959s CPU time, 89.8M memory peak, 34.9M memory swap peak.
2026-10-25T06:18:03+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 4.
2026-10-25T06:18:03+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-25T06:30:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-25T06:30:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-25T06:30:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 4.030s CPU time.
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading requested from client PID 2696226 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading finished in 323 ms.
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading requested from client PID 2696281 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading finished in 255 ms.
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading requested from client PID 2696335 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading finished in 366 ms.
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading requested from client PID 2696393 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading finished in 271 ms.
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading requested from client PID 2696448 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading finished in 259 ms.
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading requested from client PID 2696501 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading finished in 264 ms.
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading requested from client PID 2696555 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading finished in 270 ms.
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading requested from client PID 2696615 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading finished in 263 ms.
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading requested from client PID 2696668 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:15+00:00 vultr systemd[1]: Reloading finished in 259 ms.
2026-10-25T12:11:15+00:00 vultr systemd[1]: Reloading requested from client PID 2696721 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:15+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:15+00:00 vultr systemd[1]: Reloading finished in 257 ms.
2026-10-25T12:21:15+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-25T12:30:19+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2656081 (python) on client request.
2026-10-25T12:30:19+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-25T12:30:19+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 8min 17.110s CPU time, 38.9M memory peak, 35.2M memory swap peak.
2026-10-25T12:30:24+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 5.
2026-10-25T12:30:24+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-25T12:45:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-25T12:45:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-25T12:45:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 6.375s CPU time.
2026-10-26T03:00:20+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-26T03:05:08+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2699540 (python) on client request.
2026-10-26T03:05:08+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-26T03:05:08+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 19min 19.734s CPU time, 83.7M memory peak, 38.2M memory swap peak.
2026-10-26T03:05:14+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 6.
2026-10-26T03:05:14+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-26T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-26T03:15:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-26T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 13.941s CPU time.
2026-10-27T03:00:20+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-27T03:07:38+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2770458 (python) on client request.
2026-10-27T03:07:38+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-27T03:07:38+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 39min 18.113s CPU time, 128.0M memory peak, 39.1M memory swap peak.
2026-10-27T03:07:43+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 7.
2026-10-27T03:07:43+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-27T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-27T03:15:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-27T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 29.161s CPU time.
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading requested from client PID 2941531 ('systemctl') (unit apt-daily-upgrade.service)...
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading...
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading finished in 323 ms.
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading requested from client PID 2941589 ('systemctl') (unit apt-daily-upgrade.service)...
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading...
2026-10-27T06:15:40+00:00 vultr systemd[1]: Reloading finished in 413 ms.
2026-10-27T06:25:40+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-27T06:32:57+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2926125 (python) on client request.
2026-10-27T06:32:58+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-27T06:32:58+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 6min 4.362s CPU time, 120.7M memory peak, 32.1M memory swap peak.
2026-10-27T06:33:03+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 8.
2026-10-27T06:33:03+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-27T06:45:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-27T06:45:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-27T06:45:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 4.137s CPU time.
Start-Date: 2026-10-20  06:28:11
Commandline: /usr/bin/unattended-upgrade
Upgrade: libxtst6:amd64 (2:1.2.3-1.1build1, 2:1.2.3-1.1ubuntu0.1)
End-Date: 2026-10-20  06:28:11
Start-Date: 2026-10-21  06:12:47
Commandline: /usr/bin/unattended-upgrade
Upgrade: tzdata:amd64 (2026c-0ubuntu0.24.04.1, 2026e-0ubuntu0.24.04.1)
End-Date: 2026-10-21  06:12:48
Start-Date: 2026-10-21  06:12:51
Commandline: /usr/bin/unattended-upgrade
Upgrade: python3-jwt:amd64 (2.7.0-1ubuntu0.3, 2.7.0-1ubuntu0.4)
End-Date: 2026-10-21  06:12:52
Start-Date: 2026-10-22  06:14:05
Commandline: /usr/bin/unattended-upgrade
Upgrade: liblzma5:amd64 (5.6.1+really5.4.5-1ubuntu0.3, 5.6.1+really5.4.5-1ubuntu0.4), xz-utils:amd64 (5.6.1+really5.4.5-1ubuntu0.3, 5.6.1+really5.4.5-1ubuntu0.4)
End-Date: 2026-10-22  06:14:06
Start-Date: 2026-10-22  06:14:16
Commandline: /usr/bin/unattended-upgrade
Upgrade: ca-certificates:amd64 (20260601~24.04.1, 20260816ubuntu0.24.04.1)
End-Date: 2026-10-22  06:14:19
Start-Date: 2026-10-23  06:08:55
Commandline: /usr/bin/unattended-upgrade
Upgrade: zlib1g-dev:amd64 (1:1.3.dfsg-3.1ubuntu2.2, 1:1.3.dfsg-3.1ubuntu2.3), zlib1g:amd64 (1:1.3.dfsg-3.1ubuntu2.2, 1:1.3.dfsg-3.1ubuntu2.3)
End-Date: 2026-10-23  06:08:55
Start-Date: 2026-10-23  06:09:02
Commandline: /usr/bin/unattended-upgrade
Upgrade: distro-info-data:amd64 (0.72-0ubuntu0.24.04.1, 2026.10.12-0ubuntu0.24.04.1)
End-Date: 2026-10-23  06:09:03
Start-Date: 2026-10-23  06:09:07
Commandline: /usr/bin/unattended-upgrade
Upgrade: libnss3:amd64 (2:3.98-1ubuntu0.2, 2:3.98-1ubuntu0.3)
End-Date: 2026-10-23  06:09:08
Start-Date: 2026-10-27  06:15:35
Commandline: /usr/bin/unattended-upgrade
Upgrade: libbrotli1:amd64 (1.1.0-2build2, 1.1.0-2ubuntu0.1)
End-Date: 2026-10-27  06:15:35
Start-Date: 2026-10-27  06:15:39
Commandline: /usr/bin/unattended-upgrade
Upgrade: nginx:amd64 (1.24.0-2ubuntu7.18, 1.24.0-2ubuntu7.19), nginx-common:amd64 (1.24.0-2ubuntu7.18, 1.24.0-2ubuntu7.19)
End-Date: 2026-10-27  06:15:42
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
e8b46a85d61e1a17841962846f6d3012046c2d70
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
/root/tz31-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
/root/btc-pairbook-archive-svc exit=0
/var/lib/btc-pairbook-archive exit=0
1997
/root/btc-5m-twap       45f112c [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
103403632	/var/lib/btc-pairbook
9168178	/var/lib/btc-pairbook-archive
111671370	/root/.claude
645038947	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/f2adac1e-d4b2-5417-b2ba-a166434774bb/scratchpad
total 32
drwx------  8 root root 4096 Oct 27 06:55 .
drwx------ 32 root root 4096 Oct 27 06:55 ..
drwx------  3 root root 4096 Oct 23 12:20 19ca9482-c685-4646-b5db-a89314b67236
drwx------  3 root root 4096 Oct 27 06:55 236f3e7a-57cc-45b7-9aea-18e9a8ad59b9
drwx------  3 root root 4096 Oct 24 07:58 6e88615c-345d-5a08-be99-6375cc1a1073
drwx------  4 root root 4096 Oct 23 12:20 917cd7ac-51fd-50da-a0d7-5b331470eff3
drwx------  4 root root 4096 Oct 27 06:55 f2adac1e-d4b2-5417-b2ba-a166434774bb
drwx------  3 root root 4096 Oct 24 07:58 f9a43b8e-0bb7-4a08-8e42-59eed8909833
```

| check | required | read | |
|---|---|---|---|
| **H1** | `find` prints exactly one path | `/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json` | PASS |
| **H2** | source `/dev/vda2`, size `31612203008`; `grep -c` at least `1` | `/dev/vda2`, `31612203008`; `3` | PASS |
| **H3** | `3.12.` | `3.12.3` | PASS |
| **H4** | `16570` bytes, `ec71b1a7…` | `16570`, `ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd` | PASS |
| **memory** | `MemAvailable` at least `81,928,192` | `277,108` kB = `283,758,592` | PASS |
| **disk** | `avail` at least `5,400,000,000` | `11,880,419,328` | PASS |

The rest, printed with no threshold: one boot since 2026-08-02 07:24:34 UTC; the archive's ledger `64,237` bytes; the
recorder `2388318`, `NRestarts` 0, `active` since 2026-10-23 06:08:56 UTC; the pair book `2943176`, `NRestarts` 8,
`active` since 2026-10-27 06:33:03; the archive's service `inactive`, its timer `active`/`waiting`, last triggered
06:25:40 and next at 2026-10-28 03:00:20; the chain book `inactive`, `disabled`; `crypto-deploy.service` `inactive`,
`static`; `crypto-announce.service` `active`; `telemetry-watch.service` `disabled` (exit 1) and `inactive` (exit 3);
the code trees at `e3975b5…`, `e8b46a8…` and `d8194fd…`, as map §3 says; `/root/tz31-work` absent and the five code
and state trees present; the forensic store `1,997` files, map §3's count; two worktrees, map §3's two; `du -sb`
`/var/lib/btc-pairbook` `103,403,632`, `/var/lib/btc-pairbook-archive` `9,168,178`, `/root/.claude` `111,671,370`,
`/root/PROJECT_GAMING_PS5` `645,038,947`. §0.3's second run (§3.11) is in §5.15.

### 5.3 V3 — the file (asserted)

At §0.1, `logs/01-stage.log`, verbatim:

```text
/root/tz32-work/stage/research/tz32-our-quoting.py 2576 138209 6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61
exit=0
$ install -m 0644 /root/btc-5m-twap/research/tz23-maker-m0.py /root/tz32-work/stage/research/
exit=0
6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f  /root/tz32-work/stage/research/tz23-maker-m0.py
```

At §3.1, `logs/11-wt-stage.log`, verbatim:

```text
/root/tz32-work/wt/research/tz32-our-quoting.py 2576 138209 6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61
exit=0
6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f  /root/tz32-work/wt/research/tz23-maker-m0.py
```

One of one hash asserted at each, with its lines and bytes; TZ-23's file `6b3ace2c…` at each. The branch's diff against
`origin/main` names exactly one path, `A research/tz32-our-quoting.py`, 2,576 lines (§3.1).

### 5.4 V4 — the self-test (asserted): **74 of 74** — `logs/20-selftest.log`, verbatim

```text
$ I selftest
[2026-10-27T06:58:24Z]   ok  TZ-23's instrument loaded from beside this file, from its asserted bytes
[2026-10-27T06:58:24Z]   ok  glibc took the 128 KiB mmap threshold and the two arenas
[2026-10-27T06:58:24Z]   ok  the main thread sums at 60 digits
[2026-10-27T06:58:24Z]   ok  half a tick a share; the fee 0.07 s p (1 - p), the rebate a fifth of it, as the documents must state
[2026-10-27T06:58:24Z]   ok  every document request carries TZ-23's two headers, every download this file's
[2026-10-27T06:58:24Z]   ok  a leg's life is TZ-23's bands w0 to last, [T0, T0 + 300)
[2026-10-27T06:58:24Z]   ok  the first window is 2026-10-23 11:15 UTC, the one after the window whose leg is W0's last member
[2026-10-27T06:58:24Z]   ok  the candidates end at 2026-10-27 02:30 UTC, which the calendar run of 03:00:20 moves; fetch waits to 06:00
[2026-10-27T06:58:24Z]   ok  288 members; the rescore replays 18 of them
[2026-10-27T06:58:24Z]   ok  prices in thousandths and sizes in hundredths, exactly
[2026-10-27T06:58:24Z]   ok  any other text of a price or a size is a failed assert
[2026-10-27T06:58:24Z]   ok  a unit's figure has twelve decimals exactly, and a figure with more is a failed assert
[2026-10-27T06:58:24Z]   ok  own rows: our bid +s Up at p, our ask -s at p; each fill in its band of [T0, T0 + 300)
[2026-10-27T06:58:24Z]   ok  X up - C + R equals the fill-by-fill money with the rebate, at either outcome
[2026-10-27T06:58:24Z]   ok  a fill of ours at T0 + 300 or before T0 is a failed assert
[2026-10-27T06:58:24Z]   ok  the synthetic window's unit, 100 lines, byte for byte the Architect's reference
[2026-10-27T06:58:24Z]   ok  front, first in its queue, fills at the first sale into its bid; behind, after the 100 shares displayed ahead of it, fills only when a sweep of 120 takes the level and 50 beyond
[2026-10-27T06:58:24Z]   ok  a bid placed at 0.52 against our ask fills it 150 ms later where our cancel arrives after that, at 250 ms; at 50 and 100 ms the cancel arrives first; front counts no crossing
[2026-10-27T06:58:24Z]   ok  front stops bidding once its known position reaches 20 shares
[2026-10-27T06:58:24Z]   ok  the stop at T0 + 295 cancels every order; at 100 and 250 ms the cancel arrives after a sale at T0 + 295.090, at 50 ms before it
[2026-10-27T06:58:24Z]   ok  a bid arriving 50 ms after the ask came down to its price is refused, at 0 ms it is not; 9 book frames, every one equal to the rebuilt book, 8 matches, 2 sessions, 3 closes
[2026-10-27T06:58:24Z]   ok  behind: the unit's sums are its fills' money
[2026-10-27T06:58:24Z]   ok  front: the unit's sums are its fills' money
[2026-10-27T06:58:24Z]   ok  prop: the unit's sums are its fills' money
[2026-10-27T06:58:24Z]   ok  behind_nocross: the unit's sums are its fills' money
[2026-10-27T06:58:24Z]   ok  front_cross: the unit's sums are its fills' money
[2026-10-27T06:58:24Z]   ok  L0: the unit's sums are its fills' money
[2026-10-27T06:58:24Z]   ok  L100: the unit's sums are its fills' money
[2026-10-27T06:58:24Z]   ok  L250: the unit's sums are its fills' money
[2026-10-27T06:58:24Z]   ok  front_L0: the unit's sums are its fills' money
[2026-10-27T06:58:24Z]   ok  the same frames read by the general path alone give the same unit, byte for byte
[2026-10-27T06:58:24Z] wrote /root/tz32-work/selftest-tmp/x-units.txt 27039 bytes sha256 588acda5327850b55ffe2b6a5bb76b451eb707e883dd3320e4b101f896b496be
[2026-10-27T06:58:24Z]   ok  three members' units read back, 300 lines
[2026-10-27T06:58:24Z] wrote /root/tz32-work/selftest-tmp/x-constants.json 3939 bytes sha256 b5e48302cb9c45acf02281f6730a43f7b912d5239fb79a2ab1d5c9cc2303d7bc
[2026-10-27T06:58:24Z] wrote /root/tz32-work/selftest-tmp/x-scored.csv 543 bytes sha256 0f83860d58c8eb731c8dd25ead13d5b6242b81d8656312ac856d0835f480ebf0
[2026-10-27T06:58:24Z] wrote /root/tz32-work/selftest-tmp/x-reading.json 9510 bytes sha256 0b44bc4281c6f277cd22953617dc2cc315115c1e3bac7a7f295ae19ca07d0c60
[2026-10-27T06:58:24Z] labels: 3 members, 2 Up
[2026-10-27T06:58:24Z] behind: S 2.852416000000 = settlement 2.800000000000 + rebate 0.052416000000 on 15.000000000000 shares; per share 0.190161066667 = 0.186666666667 + 0.003494400000
[2026-10-27T06:58:24Z] behind: UNDECIDABLE; EARN False (margin -360.058717894722); NO EARN False (margin -365.688549894722)
[2026-10-27T06:58:24Z] barred: behind band w0   shares 15.000000000000, S 2.852416000000, per share 0.190161066667
[2026-10-27T06:58:24Z] barred: behind fills at a match shares 15.000000000000, S 2.852416000000, per share 0.190161066667
[2026-10-27T06:58:24Z] barred: behind per member S min -2.382528000000, median 2.617472000000, max 2.617472000000; above zero 2, below 1
[2026-10-27T06:58:24Z] front: S 10.011513000000 = settlement 9.750000000000 + rebate 0.261513000000 on 75.000000000000 shares; per share 0.133486840000 = 0.130000000000 + 0.003486840000
[2026-10-27T06:58:24Z] front: UNDECIDABLE; EARN False (margin -311.390156614508); NO EARN False (margin -331.038182614508)
[2026-10-27T06:58:24Z] barred: front band w0   shares 75.000000000000, S 10.011513000000, per share 0.133486840000
[2026-10-27T06:58:24Z] barred: front fills at a match shares 75.000000000000, S 10.011513000000, per share 0.133486840000
[2026-10-27T06:58:24Z] barred: front per member S min -6.662829000000, median 8.337171000000, max 8.337171000000; above zero 2, below 1
[2026-10-27T06:58:24Z] prop, barred from every reading: S 2.852416000000 = settlement 2.800000000000 + rebate 0.052416000000 on 15.000000000000 shares; per share 0.190161066667 = 0.186666666667 + 0.003494400000
[2026-10-27T06:58:24Z] barred: prop band w0   shares 15.000000000000, S 2.852416000000, per share 0.190161066667
[2026-10-27T06:58:24Z] barred: prop fills at a match shares 15.000000000000, S 2.852416000000, per share 0.190161066667
[2026-10-27T06:58:24Z] barred: prop per member S min -2.382528000000, median 2.617472000000, max 2.617472000000; above zero 2, below 1
[2026-10-27T06:58:24Z] behind_nocross, barred from every reading: S 2.852416000000 = settlement 2.800000000000 + rebate 0.052416000000 on 15.000000000000 shares; per share 0.190161066667 = 0.186666666667 + 0.003494400000
[2026-10-27T06:58:24Z] barred: behind_nocross band w0   shares 15.000000000000, S 2.852416000000, per share 0.190161066667
[2026-10-27T06:58:24Z] barred: behind_nocross fills at a match shares 15.000000000000, S 2.852416000000, per share 0.190161066667
[2026-10-27T06:58:24Z] barred: behind_nocross per member S min -2.382528000000, median 2.617472000000, max 2.617472000000; above zero 2, below 1
[2026-10-27T06:58:24Z] front_cross, barred from every reading: S 10.011513000000 = settlement 9.750000000000 + rebate 0.261513000000 on 75.000000000000 shares; per share 0.133486840000 = 0.130000000000 + 0.003486840000
[2026-10-27T06:58:24Z] barred: front_cross band w0   shares 75.000000000000, S 10.011513000000, per share 0.133486840000
[2026-10-27T06:58:24Z] barred: front_cross fills at a match shares 75.000000000000, S 10.011513000000, per share 0.133486840000
[2026-10-27T06:58:24Z] barred: front_cross per member S min -6.662829000000, median 8.337171000000, max 8.337171000000; above zero 2, below 1
[2026-10-27T06:58:24Z] L0, barred from every reading: S 2.852416000000 = settlement 2.800000000000 + rebate 0.052416000000 on 15.000000000000 shares; per share 0.190161066667 = 0.186666666667 + 0.003494400000
[2026-10-27T06:58:24Z] barred: L0 band w0   shares 15.000000000000, S 2.852416000000, per share 0.190161066667
[2026-10-27T06:58:24Z] barred: L0 fills at a match shares 15.000000000000, S 2.852416000000, per share 0.190161066667
[2026-10-27T06:58:24Z] barred: L0 per member S min -2.382528000000, median 2.617472000000, max 2.617472000000; above zero 2, below 1
[2026-10-27T06:58:24Z] L100, barred from every reading: S 6.004580000000 = settlement 5.900000000000 + rebate 0.104580000000 on 30.000000000000 shares; per share 0.200152666667 = 0.196666666667 + 0.003486000000
[2026-10-27T06:58:24Z] barred: L100 band w0   shares 15.000000000000, S 2.852416000000, per share 0.190161066667
[2026-10-27T06:58:24Z] barred: L100 band last shares 15.000000000000, S 3.152164000000, per share 0.210144266667
[2026-10-27T06:58:24Z] barred: L100 fills at a match shares 30.000000000000, S 6.004580000000, per share 0.200152666667
[2026-10-27T06:58:24Z] barred: L100 per member S min -4.665140000000, median 5.334860000000, max 5.334860000000; above zero 2, below 1
[2026-10-27T06:58:24Z] L250, barred from every reading: S 3.856996000000 = settlement 3.700000000000 + rebate 0.156996000000 on 45.000000000000 shares; per share 0.085711022222 = 0.082222222222 + 0.003488800000
[2026-10-27T06:58:24Z] barred: L250 band w0   shares 30.000000000000, S 0.704832000000, per share 0.023494400000
[2026-10-27T06:58:24Z] barred: L250 band last shares 15.000000000000, S 3.152164000000, per share 0.210144266667
[2026-10-27T06:58:24Z] barred: L250 fills at a match shares 30.000000000000, S 6.004580000000, per share 0.200152666667
[2026-10-27T06:58:24Z] barred: L250 fills against a crossing order shares 15.000000000000, S -2.147584000000, per share -0.143172266667
[2026-10-27T06:58:24Z] barred: L250 per member S min -2.047668000000, median 2.952332000000, max 2.952332000000; above zero 2, below 1
[2026-10-27T06:58:24Z] front_L0, barred from every reading: S 9.861618000000 = settlement 9.600000000000 + rebate 0.261618000000 on 75.000000000000 shares; per share 0.131488240000 = 0.128000000000 + 0.003488240000
[2026-10-27T06:58:24Z] barred: front_L0 band w0   shares 75.000000000000, S 9.861618000000, per share 0.131488240000
[2026-10-27T06:58:24Z] barred: front_L0 fills at a match shares 75.000000000000, S 9.861618000000, per share 0.131488240000
[2026-10-27T06:58:24Z] barred: front_L0 per member S min -6.712794000000, median 8.287206000000, max 8.287206000000; above zero 2, below 1
[2026-10-27T06:58:24Z] the score's files: /root/tz32-work/selftest-tmp/x-scored.csv sha256 0f83860d58c8eb731c8dd25ead13d5b6242b81d8656312ac856d0835f480ebf0; /root/tz32-work/selftest-tmp/x-reading.json sha256 0b44bc4281c6f277cd22953617dc2cc315115c1e3bac7a7f295ae19ca07d0c60
[2026-10-27T06:58:24Z]   ok  behind: S over the synthetic set is its fills' money; the bands' and the kinds' sums add to it
[2026-10-27T06:58:24Z]   ok  front: S over the synthetic set is its fills' money; the bands' and the kinds' sums add to it
[2026-10-27T06:58:24Z]   ok  prop: S over the synthetic set is its fills' money; the bands' and the kinds' sums add to it
[2026-10-27T06:58:24Z]   ok  behind_nocross: S over the synthetic set is its fills' money; the bands' and the kinds' sums add to it
[2026-10-27T06:58:24Z]   ok  front_cross: S over the synthetic set is its fills' money; the bands' and the kinds' sums add to it
[2026-10-27T06:58:24Z]   ok  L0: S over the synthetic set is its fills' money; the bands' and the kinds' sums add to it
[2026-10-27T06:58:24Z]   ok  L100: S over the synthetic set is its fills' money; the bands' and the kinds' sums add to it
[2026-10-27T06:58:24Z]   ok  L250: S over the synthetic set is its fills' money; the bands' and the kinds' sums add to it
[2026-10-27T06:58:24Z]   ok  front_L0: S over the synthetic set is its fills' money; the bands' and the kinds' sums add to it
[2026-10-27T06:58:24Z] wrote /root/tz32-work/selftest-tmp/f/x-constants.json 3939 bytes sha256 b5e48302cb9c45acf02281f6730a43f7b912d5239fb79a2ab1d5c9cc2303d7bc
[2026-10-27T06:58:24Z] wrote /root/tz32-work/selftest-tmp/f/x-scored.csv 552 bytes sha256 ec5c0a1d070ebfc678b6af04a4403578c19a3d79baec45f372552b634c84d8d5
[2026-10-27T06:58:24Z] wrote /root/tz32-work/selftest-tmp/f/x-reading.json 9585 bytes sha256 beb370b22e97ab5159d856db776c59179df96df09accf3daa224d50598d30014
[2026-10-27T06:58:24Z] labels: 3 members, 1 Up
[2026-10-27T06:58:24Z] behind: S -2.147584000000 = settlement -2.200000000000 + rebate 0.052416000000 on 15.000000000000 shares; per share -0.143172266667 = -0.146666666667 + 0.003494400000
[2026-10-27T06:58:24Z] behind: UNDECIDABLE; EARN False (margin -365.058717894722); NO EARN False (margin -360.688549894722)
[2026-10-27T06:58:24Z] barred: behind band w0   shares 15.000000000000, S -2.147584000000, per share -0.143172266667
[2026-10-27T06:58:24Z] barred: behind fills at a match shares 15.000000000000, S -2.147584000000, per share -0.143172266667
[2026-10-27T06:58:24Z] barred: behind per member S min -2.382528000000, median -2.382528000000, max 2.617472000000; above zero 1, below 2
[2026-10-27T06:58:24Z] front: S -4.988487000000 = settlement -5.250000000000 + rebate 0.261513000000 on 75.000000000000 shares; per share -0.066513160000 = -0.070000000000 + 0.003486840000
[2026-10-27T06:58:24Z] front: UNDECIDABLE; EARN False (margin -326.390156614508); NO EARN False (margin -316.038182614508)
[2026-10-27T06:58:24Z] barred: front band w0   shares 75.000000000000, S -4.988487000000, per share -0.066513160000
[2026-10-27T06:58:24Z] barred: front fills at a match shares 75.000000000000, S -4.988487000000, per share -0.066513160000
[2026-10-27T06:58:24Z] barred: front per member S min -6.662829000000, median -6.662829000000, max 8.337171000000; above zero 1, below 2
[2026-10-27T06:58:24Z] prop, barred from every reading: S -2.147584000000 = settlement -2.200000000000 + rebate 0.052416000000 on 15.000000000000 shares; per share -0.143172266667 = -0.146666666667 + 0.003494400000
[2026-10-27T06:58:24Z] barred: prop band w0   shares 15.000000000000, S -2.147584000000, per share -0.143172266667
[2026-10-27T06:58:24Z] barred: prop fills at a match shares 15.000000000000, S -2.147584000000, per share -0.143172266667
[2026-10-27T06:58:24Z] barred: prop per member S min -2.382528000000, median -2.382528000000, max 2.617472000000; above zero 1, below 2
[2026-10-27T06:58:24Z] behind_nocross, barred from every reading: S -2.147584000000 = settlement -2.200000000000 + rebate 0.052416000000 on 15.000000000000 shares; per share -0.143172266667 = -0.146666666667 + 0.003494400000
[2026-10-27T06:58:24Z] barred: behind_nocross band w0   shares 15.000000000000, S -2.147584000000, per share -0.143172266667
[2026-10-27T06:58:24Z] barred: behind_nocross fills at a match shares 15.000000000000, S -2.147584000000, per share -0.143172266667
[2026-10-27T06:58:24Z] barred: behind_nocross per member S min -2.382528000000, median -2.382528000000, max 2.617472000000; above zero 1, below 2
[2026-10-27T06:58:24Z] front_cross, barred from every reading: S -4.988487000000 = settlement -5.250000000000 + rebate 0.261513000000 on 75.000000000000 shares; per share -0.066513160000 = -0.070000000000 + 0.003486840000
[2026-10-27T06:58:24Z] barred: front_cross band w0   shares 75.000000000000, S -4.988487000000, per share -0.066513160000
[2026-10-27T06:58:24Z] barred: front_cross fills at a match shares 75.000000000000, S -4.988487000000, per share -0.066513160000
[2026-10-27T06:58:24Z] barred: front_cross per member S min -6.662829000000, median -6.662829000000, max 8.337171000000; above zero 1, below 2
[2026-10-27T06:58:24Z] L0, barred from every reading: S -2.147584000000 = settlement -2.200000000000 + rebate 0.052416000000 on 15.000000000000 shares; per share -0.143172266667 = -0.146666666667 + 0.003494400000
[2026-10-27T06:58:24Z] barred: L0 band w0   shares 15.000000000000, S -2.147584000000, per share -0.143172266667
[2026-10-27T06:58:24Z] barred: L0 fills at a match shares 15.000000000000, S -2.147584000000, per share -0.143172266667
[2026-10-27T06:58:24Z] barred: L0 per member S min -2.382528000000, median -2.382528000000, max 2.617472000000; above zero 1, below 2
[2026-10-27T06:58:24Z] L100, barred from every reading: S -3.995420000000 = settlement -4.100000000000 + rebate 0.104580000000 on 30.000000000000 shares; per share -0.133180666667 = -0.136666666667 + 0.003486000000
[2026-10-27T06:58:24Z] barred: L100 band w0   shares 15.000000000000, S -2.147584000000, per share -0.143172266667
[2026-10-27T06:58:24Z] barred: L100 band last shares 15.000000000000, S -1.847836000000, per share -0.123189066667
[2026-10-27T06:58:24Z] barred: L100 fills at a match shares 30.000000000000, S -3.995420000000, per share -0.133180666667
[2026-10-27T06:58:24Z] barred: L100 per member S min -4.665140000000, median -4.665140000000, max 5.334860000000; above zero 1, below 2
[2026-10-27T06:58:24Z] L250, barred from every reading: S -1.143004000000 = settlement -1.300000000000 + rebate 0.156996000000 on 45.000000000000 shares; per share -0.025400088889 = -0.028888888889 + 0.003488800000
[2026-10-27T06:58:24Z] barred: L250 band w0   shares 30.000000000000, S 0.704832000000, per share 0.023494400000
[2026-10-27T06:58:24Z] barred: L250 band last shares 15.000000000000, S -1.847836000000, per share -0.123189066667
[2026-10-27T06:58:24Z] barred: L250 fills at a match shares 30.000000000000, S -3.995420000000, per share -0.133180666667
[2026-10-27T06:58:24Z] barred: L250 fills against a crossing order shares 15.000000000000, S 2.852416000000, per share 0.190161066667
[2026-10-27T06:58:24Z] barred: L250 per member S min -2.047668000000, median -2.047668000000, max 2.952332000000; above zero 1, below 2
[2026-10-27T06:58:24Z] front_L0, barred from every reading: S -5.138382000000 = settlement -5.400000000000 + rebate 0.261618000000 on 75.000000000000 shares; per share -0.068511760000 = -0.072000000000 + 0.003488240000
[2026-10-27T06:58:24Z] barred: front_L0 band w0   shares 75.000000000000, S -5.138382000000, per share -0.068511760000
[2026-10-27T06:58:24Z] barred: front_L0 fills at a match shares 75.000000000000, S -5.138382000000, per share -0.068511760000
[2026-10-27T06:58:24Z] barred: front_L0 per member S min -6.712794000000, median -6.712794000000, max 8.287206000000; above zero 1, below 2
[2026-10-27T06:58:24Z] the score's files: /root/tz32-work/selftest-tmp/f/x-scored.csv sha256 ec5c0a1d070ebfc678b6af04a4403578c19a3d79baec45f372552b634c84d8d5; /root/tz32-work/selftest-tmp/f/x-reading.json sha256 beb370b22e97ab5159d856db776c59179df96df09accf3daa224d50598d30014
[2026-10-27T06:58:24Z]   ok  the constants are byte-identical with every label flipped, and the score moves (negative control)
[2026-10-27T06:58:24Z] unchanged /root/tz32-work/selftest-tmp/x-constants.json sha256 b5e48302cb9c45acf02281f6730a43f7b912d5239fb79a2ab1d5c9cc2303d7bc
[2026-10-27T06:58:24Z]   ok  a second constants run finds its file unchanged
[2026-10-27T06:58:24Z]   ok  a unit downloads its files in stream order, replays them, removes them, and is timed
[2026-10-27T06:58:24Z] units to replay 1, 2 bytes of streams in all
[2026-10-27T06:58:24Z] units to replay 1, 2 bytes of streams in all
[2026-10-27T06:58:24Z]   ok  a unit already on disk is not replayed again
[2026-10-27T06:58:24Z] units to replay 18, 18000000 bytes of streams in all
[2026-10-27T06:58:24Z] projected 90 s of replay for 18000000 bytes after 6 units at 5.0000 s a megabyte
[2026-10-27T06:58:24Z]   ok  the rescore's 18, projected above its bound, stop BLOCKED after the first 6
[2026-10-27T06:58:24Z] units to replay 29, 29000000 bytes of streams in all
[2026-10-27T06:58:24Z] projected 145 s of replay for 29000000 bytes after 24 units at 5.0000 s a megabyte
[2026-10-27T06:58:24Z]   ok  the replays projected above their bound stop BLOCKED after the first 24 units
[2026-10-27T06:58:24Z]   ok  a download arrives whole, verified by its bytes and SHA-256
[2026-10-27T06:58:24Z]   ok  a download whose SHA-256 differs is tried 6 times and stops BLOCKED, leaving nothing
[2026-10-27T06:58:24Z]   ok  a missing asset is tried 6 times and stops BLOCKED
[2026-10-27T06:58:25Z]   ok  every complete run's set.json gives its windows' assets; a run without its complete record gives none
[2026-10-27T06:58:25Z]   ok  a set.json whose SHA-256 is not its record's, or a stream file in two sets, is a failed assert
[2026-10-27T06:58:25Z]   ok  fetch starts at once where the archive has moved every candidate
[2026-10-27T06:58:25Z] the archive has moved windows to 1793067300; the candidates end at 1793068200; its ledger read again every 60 s until 2026-10-27T06:00:00Z
[2026-10-27T06:58:25Z]   ok  an archive short of the last candidate is read every 60 s and stops BLOCKED at 2026-10-27 06:00 UTC
[2026-10-27T06:58:25Z]   ok  a window's stream: opened, not cut or stopped, subscribed by T + 600, its last frame at or after T + 900, no gap above 15 s, every file archived
[2026-10-27T06:58:25Z]   ok  a leg's document: TZ-23's qualify, minimum order 5, and the condition and tokens window.json carries for it
[2026-10-27T06:58:25Z]   ok  a unit of 60 s starts from second 15 to 530 of a window
[2026-10-27T06:58:25Z]   ok  nothing starts near the archive's calendar run or while its service runs
[2026-10-27T06:58:25Z]   ok  held from second 600, a unit starts at second 15 of the next window
[2026-10-27T06:58:25Z]   ok  behind: at the projected V and Sh the threshold is 544.1515737611919841909513296747519798286 and the power between 0.99822 and 0.99823, the Architect's
[2026-10-27T06:58:25Z]   ok  front: at the projected V and Sh the threshold is 480.0141253639412769515206627775781806438 and the power between 0.99999 and 1.00001, the Architect's
[2026-10-27T06:58:25Z]   ok  W1-EARN on behind's EARN bound, first; W1-NO-EARN on front's NO EARN bound; UNDECIDABLE otherwise
[2026-10-27T06:58:25Z]   ok  TZ-23's reading on this TZ's lambda: EARN at S >= thr, NO EARN at S <= delta Sh - thr, EARN first where both hold
[2026-10-27T06:58:25Z]   ok  UNDECIDABLE between the bounds where they part
[2026-10-27T06:58:25Z]   ok  G-BOOK: the rebuilt touch, each best price and its size, equal at 99 of every 100 match frames; a set with none fails
[2026-10-27T06:58:25Z]   ok  G-STILL: unchanged, or the pair book moved by a chain of the archive's restart records; any other change fails
[2026-10-27T06:58:25Z]   ok  the ledger's runs, terminals, calendar and halt
[2026-10-27T06:58:25Z]   ok  the map's rows and anchors parse
[2026-10-27T06:58:25Z]   ok  reclaim takes the work tree and refuses the forensic store and a directory outside a session's
[2026-10-27T06:58:25Z]   ok  the pair book's root: window.json of a candidate read by fetch alone, nothing else opened, listed or written
[2026-10-27T06:58:25Z]   ok  the archive's state: its ledger read by archive, fetch and still, its runs' set.json by archive and fetch, nothing written
[2026-10-27T06:58:25Z]   ok  downloads in rehearse, replay and rescore alone; documents in rehearse and fetch alone; nothing else
[2026-10-27T06:58:25Z]   ok  the forensic store written by reclaim's exclusive create alone, nothing outside the work tree, and no process but git, systemctl and stat
[2026-10-27T06:58:25Z]   ok  opens under the pair book's root and of the archive's ledger are refused by this hook, under the chain book's root by TZ-23's, each before it happens
[2026-10-27T06:58:25Z] 74 of 74 checks passed
[2026-10-27T06:58:25Z] malloc tuned: True
[2026-10-27T06:58:25Z] peak memory of this run: 36728832 bytes
[2026-10-27T06:58:25Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

### 5.5 V5 — the archive's record (recorded, not asserted, gating nothing)

§2.4 holds both reads. Ledger, runs, sets, the windows the assets reach and the tags: printed at 06:59:25 UTC and again
at §3.11; `exit=0` both times.

### 5.6 V6 — G-REHEARSAL (asserted): **11 of 11**

135,900 lines and their SHA-256 `52b1c637a51d6b7af3c29ba3aadd75a5e2f0d39410969ee15b61155a4fc3ac60`, equal to the
Architect's, and 9 of 9 variants' totals equal to `REF` (§2.3).

### 5.7 V7 — G-SET (asserted)

288 members of 289 candidates considered; 1 non-member with its reason; 15 document requests; the members by weekday
(§1.2).

### 5.8 V8 — the replay, twice (asserted)

Every unit inside the idle stretch: 288 of 288, none ending after second 590 (§2.8). The projection after 24 units: `1,062` s of processor at `0.2104` s a megabyte, against `3,000` s. G-BOOK PASS, `417,728` of `418,535` match frames (§2.1). The second run printed `unchanged` for `replay/w1-units.txt` and `replay/w1-constants.json`: **2 of 2**.

The second run, `logs/71-replay-2.log`, verbatim:

```text
$ I replay           # the second run
[2026-10-27T07:38:44Z] MemAvailable 338636800 bytes, floor 81928192; free 11706097664 bytes, floor 5400000000
[2026-10-27T07:38:44Z] units to replay 288, 5050052883 bytes of streams in all
[2026-10-27T07:38:44Z] units 288: inside the idle stretch 288, ending after second 590 0; longest 10.6 s, download 2.0 s and replay 8.8 s at most; 762 s waited; processor 989.9 s; 5050052883 bytes downloaded; retries 0; windows 2026-10-27T07:00:00Z to 2026-10-27T07:30:00Z
[2026-10-27T07:38:45Z] unchanged /root/tz32-work/replay/w1-units.txt sha256 bad6b50a8d25fae2bf96f2df68ff8140ce6d4ec39ad74c83a7d15bfa631f5d60
[2026-10-27T07:38:45Z] units 930762 lines
[2026-10-27T07:38:45Z] unchanged /root/tz32-work/replay/w1-constants.json sha256 5f4f43c34e74d25eed283096a50803e9b37321a15408ee072411bc3375c1dac9
[2026-10-27T07:38:45Z] members 288, first 1792754100 2026-10-23T11:15:00Z, last 1793013300 2026-10-26T11:15:00Z; member list sha256 4c10c0a17532403890ebecd2146c4b0be42d830506e83363ccc0805c9a16a99d
[2026-10-27T07:38:45Z] G-BOOK PASS: match frames 418535, the rebuilt touch equal to the venue's at 417728 (0.998071845843); every level equal at 414284 (0.989843143345), barred; matches read 415916, two-sided 1553; sessions 390, closes 390
[2026-10-27T07:38:45Z] the capture's lag, a price_change frame's host receipt less its venue stamp, over 288 members and 37049296 frames of the leg: the median member's median 17 ms; its 99th percentile 106 ms at the median member and 5595 ms at the worst, above 1,000 ms at 6 members; the longest 5886 ms, the least 5 ms
[2026-10-27T07:38:45Z] behind: sent 193612, cancels 182999, refused 18145, crossings 27401; members with a fill 288; fills 50051, shares 194269.530000000000, X 167.930000000000, C 854.564000000000, R 521.433734504480, V 89287.551100000000000000000000
[2026-10-27T07:38:45Z] front: sent 273752, cancels 184772, refused 21988, crossings 0; members with a fill 288; fills 182324, shares 642581.620000000000, X -368.760000000000, C -557.367760000000, R 1693.361221636280, V 80188.929800000000000000000000
[2026-10-27T07:38:45Z] prop, barred from every reading: sent 204505, cancels 184230, refused 18988, crossings 23509; members with a fill 288; fills 69182, shares 259489.790000000000, X 243.210000000000, C 1110.262930000000, R 692.167703398500, V 91183.579500000000000000000000
[2026-10-27T07:38:45Z] behind_nocross, barred from every reading: sent 193513, cancels 182907, refused 18139, crossings 0; members with a fill 288; fills 49883, shares 193374.640000000000, X 163.060000000000, C 864.293300000000, R 518.975970040080, V 88906.302600000000000000000000
[2026-10-27T07:38:45Z] front_cross, barred from every reading: sent 273698, cancels 184726, refused 21972, crossings 14720; members with a fill 288; fills 182331, shares 642891.570000000000, X -354.910000000000, C -545.818660000000, R 1694.205895522280, V 80373.994300000000000000000000
[2026-10-27T07:38:45Z] L0, barred from every reading: sent 200058, cancels 183670, refused 8023, crossings 25019; members with a fill 288; fills 54273, shares 216663.720000000000, X 197.220000000000, C 892.480660000000, R 577.178807404640, V 74891.514800000000000000000000
[2026-10-27T07:38:45Z] L100, barred from every reading: sent 190886, cancels 183321, refused 26953, crossings 25270; members with a fill 288; fills 47545, shares 181281.890000000000, X 149.370000000000, C 746.653530000000, R 486.747294231940, V 96713.641700000000000000000000
[2026-10-27T07:38:45Z] L250, barred from every reading: sent 188391, cancels 184178, refused 43478, crossings 18839; members with a fill 288; fills 47216, shares 185308.940000000000, X 401.840000000000, C 802.075840000000, R 501.962608580160, V 113376.145200000000000000000000
[2026-10-27T07:38:45Z] front_L0, barred from every reading: sent 302274, cancels 180363, refused 9245, crossings 0; members with a fill 288; fills 226069, shares 802213.160000000000, X -85.840000000000, C -459.515200000000, R 2114.258555907120, V 79444.486800000000000000000000
[2026-10-27T07:38:45Z] behind: V 89287.551100000000000000000000; Sh 194269.530000000000; lambda 0.014605; L 5.298317366548; thr 525.779797496659 (0.002706444997 a share)
[2026-10-27T07:38:45Z] behind: EARN at S >= 525.779797496659; NO EARN at S <= 445.567852503341 (0.002293555003 a share); power 0.998569448148551
[2026-10-27T07:38:45Z] front: V 80188.929800000000000000000000; Sh 642581.620000000000; lambda 0.016557; L 5.298317366548; thr 485.965686576833 (0.000756270754 a share)
[2026-10-27T07:38:45Z] front: EARN at S >= 485.965686576833; NO EARN at S <= 2726.942413423167 (0.004243729246 a share); power 1.0
[2026-10-27T07:38:45Z] W1 reads W1-EARN on behind's EARN bound and W1-NO-EARN on front's NO EARN bound (TZ-32 section 4.5)
[2026-10-27T07:38:45Z] constants sha256 5f4f43c34e74d25eed283096a50803e9b37321a15408ee072411bc3375c1dac9, units sha256 bad6b50a8d25fae2bf96f2df68ff8140ce6d4ec39ad74c83a7d15bfa631f5d60, in state.json
[2026-10-27T07:38:45Z] malloc tuned: True
[2026-10-27T07:38:45Z] peak memory of this run: 54702080 bytes
[2026-10-27T07:38:45Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

### 5.9 V9 — DETERMINISM (asserted): **18 of 18** — `logs/72-rescore.log`, verbatim

```text
$ I rescore
[2026-10-27T07:38:51Z] MemAvailable 316993536 bytes, floor 81928192; free 11706048512 bytes, floor 5400000000
[2026-10-27T07:38:51Z] units to replay 18, 312885963 bytes of streams in all
[2026-10-27T07:45:41Z] projected 59 s of replay for 312885963 bytes after 6 units at 0.1872 s a megabyte
[2026-10-27T07:46:27Z] units 18: inside the idle stretch 18, ending after second 590 0; longest 7.3 s, download 2.1 s and replay 5.2 s at most; 381 s waited; processor 58.5 s; 312885963 bytes downloaded; retries 0; windows 2026-10-27T07:30:00Z to 2026-10-27T07:45:00Z
[2026-10-27T07:46:27Z] DETERMINISM PASS: 18 of 18 members' unit files byte for byte the replay's
[2026-10-27T07:46:27Z] malloc tuned: True
[2026-10-27T07:46:27Z] peak memory of this run: 47656960 bytes
[2026-10-27T07:46:27Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

### 5.10 V10 — the score, twice (asserted)

The reading **W1-NO-EARN** (§2.2). The second run printed `unchanged` for `replay/w1-scored.csv` and `replay/w1-reading.json` — **2 of 2**, and for the units' concatenation besides — and W1 READING `W1-NO-EARN` again. The label ledger holds **2 lines**, at `2026-10-27T07:46:36Z` and `2026-10-27T07:46:37Z`, both naming `HEAD` `b601f756edea59adf536d7ef05226d6f06bcef13`. **The first label read of the set, `2026-10-27 07:46:36` UTC, came after the instrument's commit reached `origin`, 06:58:07.251 UTC by §3.1's `ls-remote`, and after the constants' `state.json` record**: `constants_sha` `5f4f43c34e74d25eed283096a50803e9b37321a15408ee072411bc3375c1dac9` and `units_sha` `bad6b50a8d25fae2bf96f2df68ff8140ce6d4ec39ad74c83a7d15bfa631f5d60`, first recorded by the first `replay` at 07:38:33 and again by the second at 07:38:45, which is `state.json`'s `constants_at` (map §7 item 63).

The second run, `logs/81-score-2.log`, verbatim:

```text
$ I score            # the second run
[2026-10-27T07:46:36Z] MemAvailable 301121536 bytes, floor 81928192; free 11680649216 bytes, floor 5400000000
[2026-10-27T07:46:37Z] unchanged /root/tz32-work/replay/w1-units.txt sha256 bad6b50a8d25fae2bf96f2df68ff8140ce6d4ec39ad74c83a7d15bfa631f5d60
[2026-10-27T07:46:37Z] unchanged /root/tz32-work/replay/w1-scored.csv sha256 c9c93f1160a5ffd2851a48ca918301749c189927851b665c731aa0a60896da14
[2026-10-27T07:46:37Z] unchanged /root/tz32-work/replay/w1-reading.json sha256 0f65737830d7b1e3218e4351c160cb82e3f8715e776e06b2d74d3d41dbb5baa7
[2026-10-27T07:46:37Z] labels: 288 members, 136 Up
[2026-10-27T07:46:37Z] behind: S -2271.140265495520 = settlement -2792.574000000000 + rebate 521.433734504480 on 194269.530000000000 shares; per share -0.011690666393 = -0.014374740084 + 0.002684073691
[2026-10-27T07:46:37Z] behind: NO EARN; EARN False (margin -2796.920062992179); NO EARN True (margin 2716.708117998861)
[2026-10-27T07:46:37Z] barred: behind band w0   shares 52570.290000000000, S -542.247259440000, per share -0.010314709305
[2026-10-27T07:46:37Z] barred: behind band w1   shares 43066.970000000000, S -309.293924192000, per share -0.007181696883
[2026-10-27T07:46:37Z] barred: behind band w2   shares 41719.690000000000, S -684.507976804000, per share -0.016407312154
[2026-10-27T07:46:37Z] barred: behind band w3   shares 38264.790000000000, S -406.933622586980, per share -0.010634675444
[2026-10-27T07:46:37Z] barred: behind band last shares 18647.790000000000, S -328.157482472540, per share -0.017597660767
[2026-10-27T07:46:37Z] barred: behind fills at a match shares 193276.950000000000, S -2281.385012979520, per share -0.011803709718
[2026-10-27T07:46:37Z] barred: behind fills against a crossing order shares 992.580000000000, S 10.244747484000, per share 0.010321331766
[2026-10-27T07:46:37Z] barred: behind per member S min -30.213465682000, median -6.989981214000, max 10.509095780000; above zero 31, below 257
[2026-10-27T07:46:37Z] front: S 506.688981636280 = settlement -1186.672240000000 + rebate 1693.361221636280 on 642581.620000000000 shares; per share 0.000788520813 = -0.001846726086 + 0.002635246899
[2026-10-27T07:46:37Z] front: EARN; EARN True (margin 20.723295059447); NO EARN True (margin 2220.253431786887)
[2026-10-27T07:46:37Z] barred: front band w0   shares 182743.940000000000, S 453.226440362000, per share 0.002480117482
[2026-10-27T07:46:37Z] barred: front band w1   shares 149817.470000000000, S 109.974903734000, per share 0.000734059277
[2026-10-27T07:46:37Z] barred: front band w2   shares 141996.420000000000, S 38.550968480000, per share 0.000271492538
[2026-10-27T07:46:37Z] barred: front band w3   shares 118814.570000000000, S -88.932233584720, per share -0.000748496027
[2026-10-27T07:46:37Z] barred: front band last shares 49209.220000000000, S -6.131097355000, per share -0.000124592451
[2026-10-27T07:46:37Z] barred: front fills at a match shares 642581.620000000000, S 506.688981636280, per share 0.000788520813
[2026-10-27T07:46:37Z] barred: front per member S min -23.880894314000, median 0.966514124000, max 44.491304678000; above zero 163, below 125
[2026-10-27T07:46:37Z] prop, barred from every reading: S -2439.015226601500 = settlement -3131.182930000000 + rebate 692.167703398500 on 259489.790000000000 shares; per share -0.009399272421 = -0.012066690293 + 0.002667417872
[2026-10-27T07:46:37Z] barred: prop band w0   shares 71396.710000000000, S -469.298509152000, per share -0.006573111130
[2026-10-27T07:46:37Z] barred: prop band w1   shares 60816.670000000000, S -468.469268652000, per share -0.007702974672
[2026-10-27T07:46:37Z] barred: prop band w2   shares 57835.460000000000, S -628.993596766000, per share -0.010875570053
[2026-10-27T07:46:37Z] barred: prop band w3   shares 48620.990000000000, S -491.113163122820, per share -0.010100846633
[2026-10-27T07:46:37Z] barred: prop band last shares 20819.960000000000, S -381.140688908680, per share -0.018306504379
[2026-10-27T07:46:37Z] barred: prop fills at a match shares 258764.830000000000, S -2447.513079389500, per share -0.009458445645
[2026-10-27T07:46:37Z] barred: prop fills against a crossing order shares 724.960000000000, S 8.497852788000, per share 0.011721822981
[2026-10-27T07:46:37Z] barred: prop per member S min -35.062444068000, median -7.567118862000, max 13.746379374000; above zero 19, below 269
[2026-10-27T07:46:37Z] behind_nocross, barred from every reading: S -2260.947329959920 = settlement -2779.923300000000 + rebate 518.975970040080 on 193374.640000000000 shares; per share -0.011692057086 = -0.014375842148 + 0.002683785061
[2026-10-27T07:46:37Z] barred: behind_nocross band w0   shares 52302.860000000000, S -522.229189960000, per share -0.009984715749
[2026-10-27T07:46:37Z] barred: behind_nocross band w1   shares 42888.460000000000, S -327.330748664000, per share -0.007632140409
[2026-10-27T07:46:37Z] barred: behind_nocross band w2   shares 41504.990000000000, S -670.955008306000, per share -0.016165646789
[2026-10-27T07:46:37Z] barred: behind_nocross band w3   shares 38047.840000000000, S -412.999244010980, per share -0.010854735617
[2026-10-27T07:46:37Z] barred: behind_nocross band last shares 18630.490000000000, S -327.433139018940, per share -0.017575122233
[2026-10-27T07:46:37Z] barred: behind_nocross fills at a match shares 193374.640000000000, S -2260.947329959920, per share -0.011692057086
[2026-10-27T07:46:37Z] barred: behind_nocross per member S min -30.889787954000, median -7.038688904000, max 11.189689006000; above zero 29, below 259
[2026-10-27T07:46:37Z] front_cross, barred from every reading: S 504.994555522280 = settlement -1189.211340000000 + rebate 1694.205895522280 on 642891.570000000000 shares; per share 0.000785505020 = -0.001849785245 + 0.002635290264
[2026-10-27T07:46:37Z] barred: front_cross band w0   shares 182855.810000000000, S 447.573933270000, per share 0.002447687789
[2026-10-27T07:46:37Z] barred: front_cross band w1   shares 149858.360000000000, S 118.082633016000, per share 0.000787961599
[2026-10-27T07:46:37Z] barred: front_cross band w2   shares 142052.960000000000, S 32.181236904000, per share 0.000226543938
[2026-10-27T07:46:37Z] barred: front_cross band w3   shares 118869.280000000000, S -83.549800694720, per share -0.000702871261
[2026-10-27T07:46:37Z] barred: front_cross band last shares 49255.160000000000, S -9.293446973000, per share -0.000188679663
[2026-10-27T07:46:37Z] barred: front_cross fills at a match shares 642461.140000000000, S 503.829383920280, per share 0.000784217679
[2026-10-27T07:46:37Z] barred: front_cross fills against a crossing order shares 430.430000000000, S 1.165171602000, per share 0.002706994406
[2026-10-27T07:46:37Z] barred: front_cross per member S min -23.880894314000, median 0.967451994000, max 44.491304678000; above zero 161, below 127
[2026-10-27T07:46:37Z] L0, barred from every reading: S -1728.211852595360 = settlement -2305.390660000000 + rebate 577.178807404640 on 216663.720000000000 shares; per share -0.007976470877 = -0.010640409294 + 0.002663938418
[2026-10-27T07:46:37Z] barred: L0 band w0   shares 57235.750000000000, S -471.509193576000, per share -0.008238018958
[2026-10-27T07:46:37Z] barred: L0 band w1   shares 46735.060000000000, S -95.236580068000, per share -0.002037797321
[2026-10-27T07:46:37Z] barred: L0 band w2   shares 46237.900000000000, S -606.014111108000, per share -0.013106436735
[2026-10-27T07:46:37Z] barred: L0 band w3   shares 43288.990000000000, S -330.427278212500, per share -0.007633055847
[2026-10-27T07:46:37Z] barred: L0 band last shares 23166.020000000000, S -225.024689630860, per share -0.009713567097
[2026-10-27T07:46:37Z] barred: L0 fills at a match shares 216036.290000000000, S -1726.010853325360, per share -0.007989448686
[2026-10-27T07:46:37Z] barred: L0 fills against a crossing order shares 627.430000000000, S -2.200999270000, per share -0.003507959884
[2026-10-27T07:46:37Z] barred: L0 per member S min -30.860727684000, median -5.211343954000, max 10.794599690000; above zero 55, below 233
[2026-10-27T07:46:37Z] L100, barred from every reading: S -2401.046235768060 = settlement -2887.793530000000 + rebate 486.747294231940 on 181281.890000000000 shares; per share -0.013244821288 = -0.015929851184 + 0.002685029896
[2026-10-27T07:46:37Z] barred: L100 band w0   shares 49129.740000000000, S -555.261835348000, per share -0.011301949397
[2026-10-27T07:46:37Z] barred: L100 band w1   shares 41204.550000000000, S -468.344409562000, per share -0.011366327494
[2026-10-27T07:46:37Z] barred: L100 band w2   shares 39481.990000000000, S -596.808698638000, per share -0.015115973097
[2026-10-27T07:46:37Z] barred: L100 band w3   shares 35580.350000000000, S -556.498579211780, per share -0.015640615655
[2026-10-27T07:46:37Z] barred: L100 band last shares 15885.260000000000, S -224.132713008280, per share -0.014109477151
[2026-10-27T07:46:37Z] barred: L100 fills at a match shares 178963.950000000000, S -2414.603440876060, per share -0.013492121966
[2026-10-27T07:46:37Z] barred: L100 fills against a crossing order shares 2317.940000000000, S 13.557205108000, per share 0.005848816237
[2026-10-27T07:46:37Z] barred: L100 per member S min -32.967654724000, median -8.110388908000, max 9.549321120000; above zero 30, below 258
[2026-10-27T07:46:37Z] L250, barred from every reading: S -2759.673231419840 = settlement -3261.635840000000 + rebate 501.962608580160 on 185308.940000000000 shares; per share -0.014892283294 = -0.017601071163 + 0.002708787868
[2026-10-27T07:46:37Z] barred: L250 band w0   shares 50219.150000000000, S -629.101394652000, per share -0.012527121519
[2026-10-27T07:46:37Z] barred: L250 band w1   shares 44578.710000000000, S -587.905810688000, per share -0.013188040001
[2026-10-27T07:46:37Z] barred: L250 band w2   shares 42297.420000000000, S -708.627073818000, per share -0.016753434933
[2026-10-27T07:46:37Z] barred: L250 band w3   shares 35588.960000000000, S -619.195526998900, per share -0.017398528280
[2026-10-27T07:46:37Z] barred: L250 band last shares 12624.700000000000, S -214.843425262940, per share -0.017017705392
[2026-10-27T07:46:37Z] barred: L250 fills at a match shares 133011.040000000000, S -2259.630837281240, per share -0.016988295387
[2026-10-27T07:46:37Z] barred: L250 fills against a crossing order shares 52297.900000000000, S -500.042394138600, per share -0.009561423960
[2026-10-27T07:46:37Z] barred: L250 per member S min -33.866260874000, median -9.194931254000, max 28.417225846000; above zero 12, below 276
[2026-10-27T07:46:37Z] front_L0, barred from every reading: S 1212.083755907120 = settlement -902.174800000000 + rebate 2114.258555907120 on 802213.160000000000 shares; per share 0.001510924797 = -0.001124607330 + 0.002635532127
[2026-10-27T07:46:37Z] barred: front_L0 band w0   shares 220080.520000000000, S 507.337784900000, per share 0.002305237124
[2026-10-27T07:46:37Z] barred: front_L0 band w1   shares 178776.890000000000, S 272.525677384000, per share 0.001524389855
[2026-10-27T07:46:37Z] barred: front_L0 band w2   shares 173051.460000000000, S 110.228497640000, per share 0.000636969475
[2026-10-27T07:46:37Z] barred: front_L0 band w3   shares 155213.080000000000, S 174.663890805440, per share 0.001125316828
[2026-10-27T07:46:37Z] barred: front_L0 band last shares 75091.210000000000, S 147.327905177680, per share 0.001961986032
[2026-10-27T07:46:37Z] barred: front_L0 fills at a match shares 802213.160000000000, S 1212.083755907120, per share 0.001510924797
[2026-10-27T07:46:37Z] barred: front_L0 per member S min -16.683740626000, median 2.577581820000, max 66.667199010000; above zero 188, below 100
[2026-10-27T07:46:37Z] the score's files: /root/tz32-work/replay/w1-scored.csv sha256 c9c93f1160a5ffd2851a48ca918301749c189927851b665c731aa0a60896da14; /root/tz32-work/replay/w1-reading.json sha256 0f65737830d7b1e3218e4351c160cb82e3f8715e776e06b2d74d3d41dbb5baa7
[2026-10-27T07:46:37Z] W1 READING: W1-NO-EARN
[2026-10-27T07:46:37Z] malloc tuned: True
[2026-10-27T07:46:37Z] peak memory of this run: 54980608 bytes
[2026-10-27T07:46:37Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

The label ledger, `label-ledger.jsonl`, both lines (§3.11's `cat`, §5.15):

```text
{"at":"2026-10-27T07:46:36Z","constants_sha":"5f4f43c34e74d25eed283096a50803e9b37321a15408ee072411bc3375c1dac9","head":"b601f756edea59adf536d7ef05226d6f06bcef13","member_list_sha":"4c10c0a17532403890ebecd2146c4b0be42d830506e83363ccc0805c9a16a99d","members":288}
{"at":"2026-10-27T07:46:37Z","constants_sha":"5f4f43c34e74d25eed283096a50803e9b37321a15408ee072411bc3375c1dac9","head":"b601f756edea59adf536d7ef05226d6f06bcef13","member_list_sha":"4c10c0a17532403890ebecd2146c4b0be42d830506e83363ccc0805c9a16a99d","members":288}
```

### 5.11 V11 — G-STILL (asserted): **PASS** (§2.5)

### 5.12 V12 — the hooks (asserted at every mode)

Every mode printed `opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0`: `fingerprint`
twice, `selftest`, `still` twice, `scratch`, B-RECLAIM-SCRATCH's `reclaim`, `archive` twice, `rehearse`, `fetch`,
`replay` twice, `rescore` and `score` twice — 16 runs in the logs (`02`, `12`, `20`, `30`, `31`, `32`, `40`, `50`, `61`, `70`, `71`, `72`, `80`, `81`, `85`, `91`), each quoted in this
report — and B-RECLAIM-OWN's `reclaim` (§5.17).

### 5.13 V13 — memory (printed)

§2.7: every mode's peak against §0.4's floor, `81,928,192`; `malloc tuned: True` at every mode.

### 5.14 V14 — contract §4.2's self-check

§3.1: run after the push and the pull request and before this report's commit.

### 5.15 V15 — §3.11's closing reads

§0.3's block again, `logs/90-host-gate-2.log`, verbatim:

```text
Tue Oct 27 07:47:00 AM UTC 2026
1793087220
1
MemTotal:         978640 kB
MemAvailable:     297808 kB
SwapTotal:       3174396 kB
SwapFree:        2762536 kB
2026-08-02 07:24:32
IDX BOOT ID                          FIRST ENTRY                 LAST ENTRY
 -5 23a31fad2f064f04b9e138eac29658f3 Sat 2026-06-20 18:48:10 UTC Fri 2026-06-26 14:13:44 UTC
 -4 a38e17445ce341bc8b877be9d3d4f648 Fri 2026-06-26 14:13:52 UTC Tue 2026-07-14 16:15:10 UTC
 -3 5f4d18a6ba8041bd80e7d1e192c5ee28 Tue 2026-07-14 16:15:20 UTC Fri 2026-07-17 01:01:21 UTC
 -2 b1b399c70c6e4dcc934755f70a2ca231 Fri 2026-07-17 01:01:43 UTC Fri 2026-07-24 14:55:46 UTC
 -1 285d6962c92c407d837d1ce329b93aa4 Fri 2026-07-24 14:55:54 UTC Sun 2026-08-02 07:23:49 UTC
  0 48a803f03549473383be5baecf790d4e Sun 2026-08-02 07:24:34 UTC Tue 2026-10-27 07:47:00 UTC
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11680505856
/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json
3
3.12.3
16570 /root/btc-forensics/tz27-work--archive--set.json
ec71b1a7ce7db37ff29a49156006541dd5729c1df2c829c481eb64181228e4dd  /root/btc-forensics/tz27-work--archive--set.json
64237 /var/lib/btc-pairbook-archive/ledger.jsonl
MainPID=2388318
Result=success
NRestarts=0
Id=btc-recorder.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Fri 2026-10-23 06:08:56 UTC

MainPID=2943176
Result=success
NRestarts=8
Id=btc-pairbook.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Tue 2026-10-27 06:33:03 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-pairbook-archive.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=

Result=success
Id=btc-pairbook-archive.timer
ActiveState=active
SubState=waiting
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-11 15:08:11 UTC

MainPID=0
Result=success
NRestarts=0
Id=btc-chainbook.service
ActiveState=inactive
SubState=dead
UnitFileState=disabled
ActiveEnterTimestamp=

MainPID=0
Result=success
NRestarts=0
Id=crypto-deploy.service
ActiveState=inactive
SubState=dead
UnitFileState=static
ActiveEnterTimestamp=

MainPID=2696817
Result=success
NRestarts=0
Id=crypto-announce.service
ActiveState=active
SubState=running
UnitFileState=enabled
ActiveEnterTimestamp=Sun 2026-10-25 12:11:15 UTC
NEXT                         LEFT LAST                              PASSED UNIT                       ACTIVATES
Tue 2026-10-27 08:38:21 UTC 51min Tue 2026-10-27 03:28:17 UTC 4h 18min ago apt-daily.timer            apt-daily.service
Wed 2026-10-28 03:00:20 UTC   19h Tue 2026-10-27 06:25:40 UTC 1h 21min ago btc-pairbook-archive.timer btc-pairbook-archive.service
Wed 2026-10-28 06:03:24 UTC   22h Tue 2026-10-27 06:15:30 UTC 1h 31min ago apt-daily-upgrade.timer    apt-daily-upgrade.service

3 timers listed.
-- No entries --
2026-10-25T06:17:57+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2636308 (python) on client request.
2026-10-25T06:17:57+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-25T06:17:57+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 5min 49.959s CPU time, 89.8M memory peak, 34.9M memory swap peak.
2026-10-25T06:18:03+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 4.
2026-10-25T06:18:03+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-25T06:30:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-25T06:30:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-25T06:30:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 4.030s CPU time.
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading requested from client PID 2696226 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading finished in 323 ms.
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading requested from client PID 2696281 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:12+00:00 vultr systemd[1]: Reloading finished in 255 ms.
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading requested from client PID 2696335 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading finished in 366 ms.
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading requested from client PID 2696393 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading finished in 271 ms.
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading requested from client PID 2696448 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:13+00:00 vultr systemd[1]: Reloading finished in 259 ms.
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading requested from client PID 2696501 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading finished in 264 ms.
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading requested from client PID 2696555 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading finished in 270 ms.
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading requested from client PID 2696615 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading finished in 263 ms.
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading requested from client PID 2696668 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:14+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:15+00:00 vultr systemd[1]: Reloading finished in 259 ms.
2026-10-25T12:11:15+00:00 vultr systemd[1]: Reloading requested from client PID 2696721 ('systemctl') (unit crypto-deploy.service)...
2026-10-25T12:11:15+00:00 vultr systemd[1]: Reloading...
2026-10-25T12:11:15+00:00 vultr systemd[1]: Reloading finished in 257 ms.
2026-10-25T12:21:15+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-25T12:30:19+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2656081 (python) on client request.
2026-10-25T12:30:19+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-25T12:30:19+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 8min 17.110s CPU time, 38.9M memory peak, 35.2M memory swap peak.
2026-10-25T12:30:24+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 5.
2026-10-25T12:30:24+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-25T12:45:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-25T12:45:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-25T12:45:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 6.375s CPU time.
2026-10-26T03:00:20+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-26T03:05:08+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2699540 (python) on client request.
2026-10-26T03:05:08+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-26T03:05:08+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 19min 19.734s CPU time, 83.7M memory peak, 38.2M memory swap peak.
2026-10-26T03:05:14+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 6.
2026-10-26T03:05:14+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-26T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-26T03:15:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-26T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 13.941s CPU time.
2026-10-27T03:00:20+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-27T03:07:38+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2770458 (python) on client request.
2026-10-27T03:07:38+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-27T03:07:38+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 39min 18.113s CPU time, 128.0M memory peak, 39.1M memory swap peak.
2026-10-27T03:07:43+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 7.
2026-10-27T03:07:43+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-27T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-27T03:15:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-27T03:15:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 29.161s CPU time.
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading requested from client PID 2941531 ('systemctl') (unit apt-daily-upgrade.service)...
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading...
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading finished in 323 ms.
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading requested from client PID 2941589 ('systemctl') (unit apt-daily-upgrade.service)...
2026-10-27T06:15:39+00:00 vultr systemd[1]: Reloading...
2026-10-27T06:15:40+00:00 vultr systemd[1]: Reloading finished in 413 ms.
2026-10-27T06:25:40+00:00 vultr systemd[1]: Starting btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release...
2026-10-27T06:32:57+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2926125 (python) on client request.
2026-10-27T06:32:58+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-27T06:32:58+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 6min 4.362s CPU time, 120.7M memory peak, 32.1M memory swap peak.
2026-10-27T06:33:03+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 8.
2026-10-27T06:33:03+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-27T06:45:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Deactivated successfully.
2026-10-27T06:45:41+00:00 vultr systemd[1]: Finished btc-pairbook-archive.service - btc-5m-twap pair book archive, the stream files of closed windows to a Release.
2026-10-27T06:45:41+00:00 vultr systemd[1]: btc-pairbook-archive.service: Consumed 4.137s CPU time.
Start-Date: 2026-10-20  06:28:11
Commandline: /usr/bin/unattended-upgrade
Upgrade: libxtst6:amd64 (2:1.2.3-1.1build1, 2:1.2.3-1.1ubuntu0.1)
End-Date: 2026-10-20  06:28:11
Start-Date: 2026-10-21  06:12:47
Commandline: /usr/bin/unattended-upgrade
Upgrade: tzdata:amd64 (2026c-0ubuntu0.24.04.1, 2026e-0ubuntu0.24.04.1)
End-Date: 2026-10-21  06:12:48
Start-Date: 2026-10-21  06:12:51
Commandline: /usr/bin/unattended-upgrade
Upgrade: python3-jwt:amd64 (2.7.0-1ubuntu0.3, 2.7.0-1ubuntu0.4)
End-Date: 2026-10-21  06:12:52
Start-Date: 2026-10-22  06:14:05
Commandline: /usr/bin/unattended-upgrade
Upgrade: liblzma5:amd64 (5.6.1+really5.4.5-1ubuntu0.3, 5.6.1+really5.4.5-1ubuntu0.4), xz-utils:amd64 (5.6.1+really5.4.5-1ubuntu0.3, 5.6.1+really5.4.5-1ubuntu0.4)
End-Date: 2026-10-22  06:14:06
Start-Date: 2026-10-22  06:14:16
Commandline: /usr/bin/unattended-upgrade
Upgrade: ca-certificates:amd64 (20260601~24.04.1, 20260816ubuntu0.24.04.1)
End-Date: 2026-10-22  06:14:19
Start-Date: 2026-10-23  06:08:55
Commandline: /usr/bin/unattended-upgrade
Upgrade: zlib1g-dev:amd64 (1:1.3.dfsg-3.1ubuntu2.2, 1:1.3.dfsg-3.1ubuntu2.3), zlib1g:amd64 (1:1.3.dfsg-3.1ubuntu2.2, 1:1.3.dfsg-3.1ubuntu2.3)
End-Date: 2026-10-23  06:08:55
Start-Date: 2026-10-23  06:09:02
Commandline: /usr/bin/unattended-upgrade
Upgrade: distro-info-data:amd64 (0.72-0ubuntu0.24.04.1, 2026.10.12-0ubuntu0.24.04.1)
End-Date: 2026-10-23  06:09:03
Start-Date: 2026-10-23  06:09:07
Commandline: /usr/bin/unattended-upgrade
Upgrade: libnss3:amd64 (2:3.98-1ubuntu0.2, 2:3.98-1ubuntu0.3)
End-Date: 2026-10-23  06:09:08
Start-Date: 2026-10-27  06:15:35
Commandline: /usr/bin/unattended-upgrade
Upgrade: libbrotli1:amd64 (1.1.0-2build2, 1.1.0-2ubuntu0.1)
End-Date: 2026-10-27  06:15:35
Start-Date: 2026-10-27  06:15:39
Commandline: /usr/bin/unattended-upgrade
Upgrade: nginx:amd64 (1.24.0-2ubuntu7.18, 1.24.0-2ubuntu7.19), nginx-common:amd64 (1.24.0-2ubuntu7.18, 1.24.0-2ubuntu7.19)
End-Date: 2026-10-27  06:15:42
disabled
exit=1
inactive
exit=3
e3975b5da44c5328adf3bf3914634cd878842c73
e8b46a85d61e1a17841962846f6d3012046c2d70
d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3
/root/tz31-work exit=1
/root/tz18a-svc exit=0
/root/btc-recorder-svc exit=0
/root/btc-pairbook-svc exit=0
/root/btc-pairbook-archive-svc exit=0
/var/lib/btc-pairbook-archive exit=0
1997
/root/btc-5m-twap       45f112c [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
/root/tz32-work/wt      b601f75 [tz-32-our-quoting]
177140753	/var/lib/btc-pairbook
9168178	/var/lib/btc-pairbook-archive
112854874	/root/.claude
645283047	/root/PROJECT_GAMING_PS5
/tmp/claude-0/-root-btc-5m-twap/f2adac1e-d4b2-5417-b2ba-a166434774bb/scratchpad
total 16
drwx------  4 root root 4096 Oct 27 06:59 .
drwx------ 32 root root 4096 Oct 27 06:55 ..
drwx------  3 root root 4096 Oct 27 06:55 236f3e7a-57cc-45b7-9aea-18e9a8ad59b9
drwx------  4 root root 4096 Oct 27 06:55 f2adac1e-d4b2-5417-b2ba-a166434774bb
```

The rest of §3.11, `logs/92-closing.log`, verbatim:

```text
2026-10-27T07:47:14.793311013Z
$ TZ=UTC systemctl show btc-recorder.service btc-pairbook.service btc-pairbook-archive.service -p MainPID -p NRestarts -p ActiveState -p MemoryCurrent -p MemoryPeak
MainPID=2388318
NRestarts=0
MemoryCurrent=15835136
MemoryPeak=302202880
ActiveState=active

MainPID=2943176
NRestarts=8
MemoryCurrent=2117632
MemoryPeak=67203072
ActiveState=active

MainPID=0
NRestarts=0
MemoryCurrent=[not set]
MemoryPeak=[not set]
ActiveState=inactive
$ journalctl -u btc-recorder.service -u btc-pairbook.service -o short-iso --since -24h --no-pager | tail -n 60
2026-10-27T03:07:38+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2770458 (python) on client request.
2026-10-27T03:07:38+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-27T03:07:38+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 39min 18.113s CPU time, 128.0M memory peak, 39.1M memory swap peak.
2026-10-27T03:07:43+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 7.
2026-10-27T03:07:43+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
2026-10-27T06:32:57+00:00 vultr systemd[1]: btc-pairbook.service: Sent signal SIGTERM to main process 2926125 (python) on client request.
2026-10-27T06:32:58+00:00 vultr systemd[1]: btc-pairbook.service: Deactivated successfully.
2026-10-27T06:32:58+00:00 vultr systemd[1]: btc-pairbook.service: Consumed 6min 4.362s CPU time, 120.7M memory peak, 32.1M memory swap peak.
2026-10-27T06:33:03+00:00 vultr systemd[1]: btc-pairbook.service: Scheduled restart job, restart counter is at 8.
2026-10-27T06:33:03+00:00 vultr systemd[1]: Started btc-pairbook.service - btc-5m-twap pair book, the nested pair's four books streamed.
$ free -b
               total        used        free      shared  buff/cache   available
Mem:      1002127360   535777280   111120384       53248   504221696   466350080
Swap:     3250581504   478494720  2772086784
$ du -sb /root/tz32-work /root/.claude
121481924	/root/tz32-work
112861091	/root/.claude
$ cat /root/tz32-work/state.json /root/tz32-work/label-ledger.jsonl
{
 "constants_at": "2026-10-27T07:38:45Z",
 "constants_sha": "5f4f43c34e74d25eed283096a50803e9b37321a15408ee072411bc3375c1dac9",
 "set_at": "2026-10-27T07:03:36Z",
 "set_sha": "83af4226af064e85271e5c6b58d3e7d464a3729058775da69528d5ffab98d47e",
 "still": {
  "at": "2026-10-27T06:58:32Z",
  "at_ns": 1793084312323917420,
  "units": {
   "pairbook": {
    "ActiveState": "active",
    "MainPID": "2943176",
    "NRestarts": "8"
   },
   "recorder": {
    "ActiveState": "active",
    "MainPID": "2388318",
    "NRestarts": "0"
   }
  }
 },
 "units_sha": "bad6b50a8d25fae2bf96f2df68ff8140ce6d4ec39ad74c83a7d15bfa631f5d60"
}
{"at":"2026-10-27T07:46:36Z","constants_sha":"5f4f43c34e74d25eed283096a50803e9b37321a15408ee072411bc3375c1dac9","head":"b601f756edea59adf536d7ef05226d6f06bcef13","member_list_sha":"4c10c0a17532403890ebecd2146c4b0be42d830506e83363ccc0805c9a16a99d","members":288}
{"at":"2026-10-27T07:46:37Z","constants_sha":"5f4f43c34e74d25eed283096a50803e9b37321a15408ee072411bc3375c1dac9","head":"b601f756edea59adf536d7ef05226d6f06bcef13","member_list_sha":"4c10c0a17532403890ebecd2146c4b0be42d830506e83363ccc0805c9a16a99d","members":288}
```

### 5.16 V16 — B-RECLAIM-SCRATCH, and the directories beside this session

`I scratch`, `logs/31-scratch.log`, verbatim:

```text
$ I scratch /tmp/claude-0/-root-btc-5m-twap
[2026-10-27T06:58:32Z] running 2875240 started 2026-10-26T18:11:45Z claude
[2026-10-27T06:58:32Z] running 2875250 started 2026-10-26T18:11:47Z claude
[2026-10-27T06:58:32Z] running 2945054 started 2026-10-27T06:55:18Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-10-27T06:58:32Z] 19ca9482-c685-4646-b5db-a89314b67236 born 2026-10-23T12:20:35Z: earlier
[2026-10-27T06:58:32Z] 236f3e7a-57cc-45b7-9aea-18e9a8ad59b9 born 2026-10-27T06:55:19Z: live, process [2945054]
[2026-10-27T06:58:32Z] 6e88615c-345d-5a08-be99-6375cc1a1073 born 2026-10-24T07:58:19Z: earlier
[2026-10-27T06:58:32Z] 917cd7ac-51fd-50da-a0d7-5b331470eff3 born 2026-10-23T12:20:37Z: earlier
[2026-10-27T06:58:32Z] f9a43b8e-0bb7-4a08-8e42-59eed8909833 born 2026-10-24T07:58:17Z: earlier
[2026-10-27T06:58:32Z] malloc tuned: True
[2026-10-27T06:58:32Z] peak memory of this run: 35155968 bytes
[2026-10-27T06:58:32Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
```

Four directories **earlier** — TZ-31's pair `917cd7ac…` and `19ca9482…`, which map §3 named, and `6e88615c…` and
`f9a43b8e…`, born 2026-10-24 07:58:19 and 07:58:17 UTC by sessions no report names — and one **live**, `236f3e7a…`, born
with this session's process `2945054`. This session's own directory, `f2adac1e…`, is not listed. The two `claude`
processes started 2026-10-26 18:11:45/47 UTC made no directory beside it.

B-RECLAIM-SCRATCH, `logs/32-reclaim-scratch.log` and `logs/33-rm-scratch.log`, verbatim — no command refused by the
session's classifier:

```text
$ I reclaim /tmp/claude-0/-root-btc-5m-twap/19ca9482-c685-4646-b5db-a89314b67236 /tmp/claude-0/-root-btc-5m-twap/6e88615c-345d-5a08-be99-6375cc1a1073 /tmp/claude-0/-root-btc-5m-twap/917cd7ac-51fd-50da-a0d7-5b331470eff3 /tmp/claude-0/-root-btc-5m-twap/f9a43b8e-0bb7-4a08-8e42-59eed8909833
[2026-10-27T06:58:55Z] reclaim: 2904 report tokens; forensic store holds 1997 files
[2026-10-27T06:58:55Z] RECLAIM PASS: 5 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 1997 -> 1997 files
[2026-10-27T06:58:55Z] malloc tuned: True
[2026-10-27T06:58:55Z] peak memory of this run: 36216832 bytes
[2026-10-27T06:58:55Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/19ca9482-c685-4646-b5db-a89314b67236
exit=0
exit=1
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/6e88615c-345d-5a08-be99-6375cc1a1073
exit=0
exit=1
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/917cd7ac-51fd-50da-a0d7-5b331470eff3
exit=0
exit=1
$ rm -rf /tmp/claude-0/-root-btc-5m-twap/f9a43b8e-0bb7-4a08-8e42-59eed8909833
exit=0
exit=1
2026-10-27T06:59:20.346979971Z
```

### 5.17 V16 and V17 — B-RECLAIM-OWN, verbatim from the session

Its output was written to no file (§9). Every line it printed, unfiltered:

```text
$ cd /root/tz32-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz32-work/wt/research/tz32-our-quoting.py reclaim /root/tz32-work; echo "exit=$?"
[2026-10-27T07:52:17Z] reclaim: 3085 report tokens; forensic store holds 1997 files
[2026-10-27T07:52:17Z] reclaim: /root/tz32-work/wt skipped: no file but its HEAD's, and HEAD b601f756edea59adf536d7ef05226d6f06bcef13 is its upstream's
[2026-10-27T07:52:17Z] R copied 1ae5202006cd013017832a9d927926fb801706b1a9469da8d0812c531d60ada9 /root/btc-forensics/tz32-work--label-ledger.jsonl
[2026-10-27T07:52:17Z] R copied c0ed88e96e129f078b062ae7cc44e51f95944b77fb964074a3c85457dc82f026 /root/btc-forensics/tz32-work--state.json
[2026-10-27T07:52:17Z] R copied 2b7fa7b5104f12ff5b33bb84fc6431f483b80b62b1345ef0bc5a54e53444f106 /root/btc-forensics/tz32-work--logs--00-mkdir.log
[2026-10-27T07:52:17Z] R copied eb7a9f179899a8b29d7fbcf872d8fa5251a962fcc09835af577c2eafb4e0ebc2 /root/btc-forensics/tz32-work--logs--00-startup-main.log
[2026-10-27T07:52:17Z] R copied 417d90e00114a53e2c6cb711eea6bfa6cb097dcab9296a5dfbf86da9aea79d13 /root/btc-forensics/tz32-work--logs--01-stage.log
[2026-10-27T07:52:17Z] R copied 66519d79a22603471e36a74ee9b30df16929a8d9bb91bfe16e745c4c2a749b89 /root/btc-forensics/tz32-work--logs--02-fingerprint.log
[2026-10-27T07:52:17Z] R copied 7924a0d68f475a770fe7fd22360d747be6203bfea406f1256bc16413006df972 /root/btc-forensics/tz32-work--logs--03-host-gate.log
[2026-10-27T07:52:17Z] R copied 8500c5a6cf3d63ea0cf00f3a4c34e172e3d152507f36247cb186cc0c734dcd76 /root/btc-forensics/tz32-work--logs--05-refs.log
[2026-10-27T07:52:17Z] R copied b2b97a8f9ead5ab8696a8a89115ee7b372c98dbae8b0611572f273bc4f4a70e6 /root/btc-forensics/tz32-work--logs--10-branch.log
[2026-10-27T07:52:17Z] R copied 88f980d7c7444b3ff764a87dd4b0fd25237bcc8b86fc58fae6531a46b95af895 /root/btc-forensics/tz32-work--logs--11-wt-stage.log
[2026-10-27T07:52:17Z] R copied b4253677d979dea8f667632736ed882ef70901f814edbc6a014577e381ae566c /root/btc-forensics/tz32-work--logs--12-fingerprint-wt.log
[2026-10-27T07:52:17Z] R copied 59cf747a80e99639a1a75324a1643d6eab92fea1c70b1bbf50d14785e501654d /root/btc-forensics/tz32-work--logs--13-commit.log
[2026-10-27T07:52:17Z] R copied 51684b898e87c143287178f8a3338487c66d9ee9b5a71dc68e627d787a07d897 /root/btc-forensics/tz32-work--logs--14-push.log
[2026-10-27T07:52:17Z] R copied 02fa0ebc9310c820cf6923ea2ce8305c17e171be8e0ead5e5081bcf299d6befb /root/btc-forensics/tz32-work--logs--15-pr.log
[2026-10-27T07:52:17Z] R copied 72a6e8768b6f9e613ce9aa2c06b2d8ad85222f5eb5edc07fccbd08f8aee49315 /root/btc-forensics/tz32-work--logs--20-selftest.log
[2026-10-27T07:52:17Z] R copied 34ffbc972903b0e2ea3d017a4261f1daf68a1c2333a83358900a11277b716ded /root/btc-forensics/tz32-work--logs--30-still.log
[2026-10-27T07:52:17Z] R copied 2c77ea219e3ce3b74bbb021e720d60d0d9d4f77a7ccb8c6f75647a5d5b1ddbb9 /root/btc-forensics/tz32-work--logs--31-scratch.log
[2026-10-27T07:52:17Z] R copied f4395b9a9983a2f12298229934ee72fff0b742321872c9e49bd45fbb78330c10 /root/btc-forensics/tz32-work--logs--32-reclaim-scratch.log
[2026-10-27T07:52:17Z] R copied fb3533a4a2b840af4e96fad68fc06f2d568e7c3c95ceca91895174292ed6b1d9 /root/btc-forensics/tz32-work--logs--33-rm-scratch.log
[2026-10-27T07:52:17Z] R copied 9b507ef1e6cd5893934741cfead6af43a3b9f8cd2235ee2f26487383010da83d /root/btc-forensics/tz32-work--logs--40-archive.log
[2026-10-27T07:52:17Z] R copied 60ede41a3c45151aa5590d058becd8b7fab3c5e159d9e813aef380ff1d26841e /root/btc-forensics/tz32-work--logs--50-rehearse.log
[2026-10-27T07:52:17Z] R copied d48d3cfee0b612ddd807b98a8100c9de6de1ab084ab3a193829bdea4c974e4d3 /root/btc-forensics/tz32-work--logs--60-instant.log
[2026-10-27T07:52:17Z] R copied 4979e913e2bd1278410ed28358707565e696ec6a480e481400448b68233c9645 /root/btc-forensics/tz32-work--logs--61-fetch.log
[2026-10-27T07:52:17Z] R copied f673f31930d6e67b29c8b1aefe9f524e85d9fcb7dd4522ca042b199ddd390b2a /root/btc-forensics/tz32-work--logs--62-offcalendar-journal.log
[2026-10-27T07:52:17Z] R copied 146f641974f6dd544efe98e1644515e2a3d7c3ed4eb7bc5480a0e6a6675df1e7 /root/btc-forensics/tz32-work--logs--70-replay-1.log
[2026-10-27T07:52:17Z] R copied fdbb3659bff4a1bdae31be2d2015031fa2429ac11040a15a3842d67a802a9581 /root/btc-forensics/tz32-work--logs--71-replay-2.log
[2026-10-27T07:52:17Z] R copied f5ba485755c8423264d2009c96ee0d670a530e071457a5532e4ca30c3d1a3ffa /root/btc-forensics/tz32-work--logs--72-rescore.log
[2026-10-27T07:52:17Z] R copied e41e958d0c4a5afc7b1110dd1aaea32ec589548aa9cd0b348e549292691cee11 /root/btc-forensics/tz32-work--logs--80-score-1.log
[2026-10-27T07:52:17Z] R copied 83e63d537201ef679209a7dc013de3fb22c1f376e15d272112fb0a840a28ca8e /root/btc-forensics/tz32-work--logs--81-score-2.log
[2026-10-27T07:52:17Z] R copied 39b81267d285fe5c56c32361529a5ccb4e33b68ca2c44ed3f87367a9a4d9d28a /root/btc-forensics/tz32-work--logs--85-still-2.log
[2026-10-27T07:52:17Z] R copied dde64e9c8f433e723e7a466128c6c816a81c095d701d7f488b02cf4d8d2ff840 /root/btc-forensics/tz32-work--logs--90-host-gate-2.log
[2026-10-27T07:52:17Z] R copied 4986ceb82be86110e2cebbff350d8512264cabafde6f69482aff21dd06afbdae /root/btc-forensics/tz32-work--logs--91-archive-2.log
[2026-10-27T07:52:17Z] R copied 78bff1c7a06f7704b18f3c9c65b2d80a0e26ee618b1172fd08b09edfd9af2747 /root/btc-forensics/tz32-work--logs--92-closing.log
[2026-10-27T07:52:17Z] R copied 6b4f499ffd81fa5fd27d5bd03d04173e84eb14a35d0af51b65351f3ca1616ca5 /root/btc-forensics/tz32-work--logs--93-separation.log
[2026-10-27T07:52:17Z] R copied 3938213ed1d8af922db71cfba0805f8d0e1e0eb53a9a1bbc303c97946cb7e1e3 /root/btc-forensics/tz32-work--logs--94-files-written.log
[2026-10-27T07:52:17Z] R copied 22f16a747624cbc497756d27ea7574485cba8b68ff95277ac4025041aa724afd /root/btc-forensics/tz32-work--rehearsal--docs.json
[2026-10-27T07:52:17Z] R copied 52b1c637a51d6b7af3c29ba3aadd75a5e2f0d39410969ee15b61155a4fc3ac60 /root/btc-forensics/tz32-work--rehearsal--rehearsal-lines.txt
[2026-10-27T07:52:17Z] R copied f4e064cb5d9ec248fd03ce1bc0a1c6dae5d5e3cf9adf570e63e07ad0fd4d532b /root/btc-forensics/tz32-work--rehearsal--rehearsal-timing.jsonl
[2026-10-27T07:52:17Z] R copied e58c5bc8ea7228f8015808677c452b645fc80edb4d27a21308b26dd94410d804 /root/btc-forensics/tz32-work--replay--replay-timing.jsonl
[2026-10-27T07:52:17Z] R copied 5f4f43c34e74d25eed283096a50803e9b37321a15408ee072411bc3375c1dac9 /root/btc-forensics/tz32-work--replay--w1-constants.json
[2026-10-27T07:52:17Z] R copied 0f65737830d7b1e3218e4351c160cb82e3f8715e776e06b2d74d3d41dbb5baa7 /root/btc-forensics/tz32-work--replay--w1-reading.json
[2026-10-27T07:52:17Z] R copied c9c93f1160a5ffd2851a48ca918301749c189927851b665c731aa0a60896da14 /root/btc-forensics/tz32-work--replay--w1-scored.csv
[2026-10-27T07:52:17Z] R copied bad6b50a8d25fae2bf96f2df68ff8140ce6d4ec39ad74c83a7d15bfa631f5d60 /root/btc-forensics/tz32-work--replay--w1-units.txt
[2026-10-27T07:52:18Z] R copied 22d64901d7ed2347931861a66cec97c5647a1d58e979967214cb61a09b5e9a3c /root/btc-forensics/tz32-work--rescore--rescore-timing.jsonl
[2026-10-27T07:52:18Z] R copied 83af4226af064e85271e5c6b58d3e7d464a3729058775da69528d5ffab98d47e /root/btc-forensics/tz32-work--set--w1-set.json
[2026-10-27T07:52:18Z] R copied 6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f /root/btc-forensics/tz32-work--stage--research--tz23-maker-m0.py
[2026-10-27T07:52:18Z] R copied 6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61 /root/btc-forensics/tz32-work--stage--research--tz32-our-quoting.py
[2026-10-27T07:52:18Z] RECLAIM PASS: 416 files considered, 46 named by a report, 1 kept by name, 47 copied, 0 already held; forensic store 1997 -> 2044 files
[2026-10-27T07:52:18Z] malloc tuned: True
[2026-10-27T07:52:18Z] peak memory of this run: 37302272 bytes
[2026-10-27T07:52:18Z] opens refused: 0; under the recorder's and the chain book's roots by TZ-23's hook: 0
exit=0
$ git -C /root/btc-5m-twap worktree remove /root/tz32-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz32-work; echo "exit=$?"
exit=0
$ test -e /root/tz32-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       45f112c [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
2044
$ df -B1 --output=source,size,avail /var/lib/btc-recorder; date -u +%FT%TZ
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 11746095104
2026-10-27T07:52:27Z
```

**V16:** `RECLAIM PASS` — 416 files considered, 46 named by a report, 1 kept by name (`logs/94-files-written.log`,
whose hash no report printed), **47 copied**, 0 already held; the forensic store **1,997 → 2,044**, after = before +
copied. The branch worktree was skipped as pristine at its pushed `HEAD` `b601f75`; the unit files and
`/root/tz32-work/report/` were not named and went with the tree. Each of the 47 copies was hashed again from the
store after the block and equals the hash its `R copied` line prints.

**V17:** `git worktree remove` without `--force`, `exit=0`; `rm -rf /root/tz32-work`, `exit=0`; `test -e`, `exit=1`;
`git worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else. B-RECLAIM-SCRATCH's four
directories each read `exit=1` at `test -e` (§5.16). No command of either block was refused by the session's
classifier, and the Boss ran none. The branch `tz-32-our-quoting` stays on `origin` and as a local ref.

---

## 6. What could not be implemented as written

1. **Contract §1's pull and the first reads ran before §0.0's `mkdir`**, as in every TZ since TZ-21. They were `git
   fetch` and `git merge --ff-only origin/main` (local `main` `37e78e9` → `45f112c`), reading the TZ, the map and the
   contract, the Executor's own notes, one `date -u`, and one `git diff` of the map between `7e08b79` and `45f112c`
   (a committed file) printed to the session. **The `mkdir` itself printed `exit=0` to the session**, before `logs/`
   existed. `logs/00-mkdir.log` records it after the fact, with its output as printed, and `logs/00-startup-main.log`
   records `main` as it stood.
2. **The run began at 06:55 UTC, 55 minutes after `fetch`'s deadline of 06:00:00 UTC.** That deadline binds only while
   the archive's ledger falls short of `1793068200`: `wait_archive` asserts `now < ARCHIVE_WAIT_UNTIL` inside its
   loop alone (Appendix A lines 508 to 524). The calendar run of 03:00:20 UTC had moved the windows to `1793068200` and
   completed at 03:15:41, so `fetch` read the ledger once and waited 0 s. §3.6's "no earlier than" was met. This is
   recorded so that the time is not taken as an oversight.
3. **The set differs from §1's every-candidate case.** One candidate, `1792923300`, failed TZ-30's stream rule with a
   gap above 15 s. So the members run one window further, to `1793013300`. The member list is `4c10c0a1…`, not
   `3ec41ed9…`, and the weekdays are 51, 96, 95 and 46, not 51, 96, 96 and 45. §1 says that list is "recorded and
   asserted by nothing", and G-SET allows 62 non-members.
4. **One read no step names:** `logs/62-offcalendar-journal.log`, `journalctl` reads of PID 1's records in the twenty
   minutes before each off-calendar run, and of both capture units' starts and stops since 2026-10-23. It was needed
   because §0.3's `tail -n 80` did not reach the runs of 2026-10-24 and 2026-10-25 06:12 (§2.4). `journalctl` is among
   §2 item 5's permitted reads, and nothing under a capture root was opened.
5. **The refs: 71 lines against §0.5's 67.** Four of the archive's eight new runs ran off the calendar (§2.4, §3.2).
   This is recorded, as §0.5 allows.
6. **Memory peaks above the Architect's measured ones.** `score` peaked at `54,984,704` bytes against the Architect's
   `32,927,744` (1.670×), `replay` at `53,673,984` and `54,702,080` against `40,157,184` and `32,890,880`, and `fetch`
   at `44,986,368` against `31,617,024` (§2.7). The largest is above half of §0.4's floor, the Architect's largest
   peak doubled. The floor itself held at every read: `MemAvailable` never fell below `283,758,592` (§2.6). The
   Architect measured over the stand-in's 48 windows, and `score` and `replay`'s concatenation hold every member's
   parsed unit at once.
7. **`state.json`'s `constants_at` is the second `replay`'s instant**, 07:38:45 UTC. Both runs preceded the first
   label read, 07:46:36. This is the instrument's behaviour, as in TZ-29 and TZ-31.
8. **B-RECLAIM-SCRATCH removed two directories that no report or map names:** `6e88615c-345d-5a08-be99-6375cc1a1073`
   and `f9a43b8e-0bb7-4a08-8e42-59eed8909833`, born 2026-10-24 07:58:19 and 07:58:17 UTC. `I scratch` named both
   earlier, and §9's rule removes every directory it names earlier. The first has the same UUID as a directory
   TZ-30's B-RECLAIM-SCRATCH removed (TZ-30 report); a directory of that name was made again on 2026-10-24.
   The `reclaim` over all four copied nothing.
9. **The report was assembled by a script** from a hand-written template and the logs. The script substituted each
   quoted log verbatim. The tables and most prose figures came from the logs through a second script that asserted
   each pattern exactly once. The rest were typed by hand and checked by a third script against the logs and the TZ:
   244 numbers, 36 clock times and every hex token. The numbers it did not find were four section numbers, the
   computed ratio `1.670` and `283,758,592` = `277,108` kB × 1,024. The times it did not find were the upload's two
   commit times, converted from `+04:00`. The template and the scripts lived in `/root/tz32-work/report/`. No report
   names their hashes, so they went with the tree. **`logs/94-files-written.log` does not list itself**; its hash is in
   B-RECLAIM-OWN's output.
10. **The archive's runs off its calendar** (§2.4) are not this TZ's and moved no gate. They are recorded because §3.4
    and map §7 item 115 ask for them to be set beside systemd's records.
11. **B-RECLAIM-OWN ran in four calls of the session:** `I reclaim`, then `git worktree remove`, then `rm -rf`, then
    the last four lines together, to which the Executor added `date -u` to stamp the `df`. Its output was written to
    no file by the block. To quote it whole, the Executor copied the session's output into one text file in the
    session's scratchpad, §0.0's one exception, and pasted that file into §5.17. §5.17 prints each call's command
    line above its output.

Nothing else.

### 6.1 Every file the run wrote, by SHA-256 (§8) — `logs/94-files-written.log`, verbatim

The unit files are excepted, as §8 allows: the replay's 288, the rescore's 18 and the rehearsal's 51.
`replay/w1-units.txt` and `rehearsal/rehearsal-lines.txt` carry their bytes in order.

```text
2026-10-27T07:47:39Z
1ae5202006cd013017832a9d927926fb801706b1a9469da8d0812c531d60ada9 524 ./label-ledger.jsonl
2b7fa7b5104f12ff5b33bb84fc6431f483b80b62b1345ef0bc5a54e53444f106 99 ./logs/00-mkdir.log
eb7a9f179899a8b29d7fbcf872d8fa5251a962fcc09835af577c2eafb4e0ebc2 530 ./logs/00-startup-main.log
417d90e00114a53e2c6cb711eea6bfa6cb097dcab9296a5dfbf86da9aea79d13 350 ./logs/01-stage.log
66519d79a22603471e36a74ee9b30df16929a8d9bb91bfe16e745c4c2a749b89 8412 ./logs/02-fingerprint.log
7924a0d68f475a770fe7fd22360d747be6203bfea406f1256bc16413006df972 14784 ./logs/03-host-gate.log
8500c5a6cf3d63ea0cf00f3a4c34e172e3d152507f36247cb186cc0c734dcd76 5412 ./logs/05-refs.log
b2b97a8f9ead5ab8696a8a89115ee7b372c98dbae8b0611572f273bc4f4a70e6 331 ./logs/10-branch.log
88f980d7c7444b3ff764a87dd4b0fd25237bcc8b86fc58fae6531a46b95af895 243 ./logs/11-wt-stage.log
b4253677d979dea8f667632736ed882ef70901f814edbc6a014577e381ae566c 8412 ./logs/12-fingerprint-wt.log
59cf747a80e99639a1a75324a1643d6eab92fea1c70b1bbf50d14785e501654d 423 ./logs/13-commit.log
51684b898e87c143287178f8a3338487c66d9ee9b5a71dc68e627d787a07d897 668 ./logs/14-push.log
02fa0ebc9310c820cf6923ea2ce8305c17e171be8e0ead5e5081bcf299d6befb 94 ./logs/15-pr.log
72a6e8768b6f9e613ce9aa2c06b2d8ad85222f5eb5edc07fccbd08f8aee49315 23039 ./logs/20-selftest.log
34ffbc972903b0e2ea3d017a4261f1daf68a1c2333a83358900a11277b716ded 866 ./logs/30-still.log
2c77ea219e3ce3b74bbb021e720d60d0d9d4f77a7ccb8c6f75647a5d5b1ddbb9 992 ./logs/31-scratch.log
f4395b9a9983a2f12298229934ee72fff0b742321872c9e49bd45fbb78330c10 458 ./logs/32-reclaim-scratch.log
fb3533a4a2b840af4e96fad68fc06f2d568e7c3c95ceca91895174292ed6b1d9 399 ./logs/33-rm-scratch.log
9b507ef1e6cd5893934741cfead6af43a3b9f8cd2235ee2f26487383010da83d 93798 ./logs/40-archive.log
60ede41a3c45151aa5590d058becd8b7fab3c5e159d9e813aef380ff1d26841e 4450 ./logs/50-rehearse.log
d48d3cfee0b612ddd807b98a8100c9de6de1ab084ab3a193829bdea4c974e4d3 186 ./logs/60-instant.log
4979e913e2bd1278410ed28358707565e696ec6a480e481400448b68233c9645 1193 ./logs/61-fetch.log
f673f31930d6e67b29c8b1aefe9f524e85d9fcb7dd4522ca042b199ddd390b2a 22323 ./logs/62-offcalendar-journal.log
146f641974f6dd544efe98e1644515e2a3d7c3ed4eb7bc5480a0e6a6675df1e7 5876 ./logs/70-replay-1.log
fdbb3659bff4a1bdae31be2d2015031fa2429ac11040a15a3842d67a802a9581 5158 ./logs/71-replay-2.log
f5ba485755c8423264d2009c96ee0d670a530e071457a5532e4ca30c3d1a3ffa 877 ./logs/72-rescore.log
e41e958d0c4a5afc7b1110dd1aaea32ec589548aa9cd0b348e549292691cee11 12154 ./logs/80-score-1.log
83e63d537201ef679209a7dc013de3fb22c1f376e15d272112fb0a840a28ca8e 12138 ./logs/81-score-2.log
39b81267d285fe5c56c32361529a5ccb4e33b68ca2c44ed3f87367a9a4d9d28a 902 ./logs/85-still-2.log
dde64e9c8f433e723e7a466128c6c816a81c095d701d7f488b02cf4d8d2ff840 14508 ./logs/90-host-gate-2.log
4986ceb82be86110e2cebbff350d8512264cabafde6f69482aff21dd06afbdae 93798 ./logs/91-archive-2.log
78bff1c7a06f7704b18f3c9c65b2d80a0e26ee618b1172fd08b09edfd9af2747 3342 ./logs/92-closing.log
6b4f499ffd81fa5fd27d5bd03d04173e84eb14a35d0af51b65351f3ca1616ca5 570 ./logs/93-separation.log
22f16a747624cbc497756d27ea7574485cba8b68ff95277ac4025041aa724afd 27592 ./rehearsal/docs.json
52b1c637a51d6b7af3c29ba3aadd75a5e2f0d39410969ee15b61155a4fc3ac60 7008141 ./rehearsal/rehearsal-lines.txt
f4e064cb5d9ec248fd03ce1bc0a1c6dae5d5e3cf9adf570e63e07ad0fd4d532b 11444 ./rehearsal/rehearsal-timing.jsonl
e58c5bc8ea7228f8015808677c452b645fc80edb4d27a21308b26dd94410d804 64833 ./replay/replay-timing.jsonl
5f4f43c34e74d25eed283096a50803e9b37321a15408ee072411bc3375c1dac9 4308 ./replay/w1-constants.json
0f65737830d7b1e3218e4351c160cb82e3f8715e776e06b2d74d3d41dbb5baa7 13761 ./replay/w1-reading.json
c9c93f1160a5ffd2851a48ca918301749c189927851b665c731aa0a60896da14 45369 ./replay/w1-scored.csv
bad6b50a8d25fae2bf96f2df68ff8140ce6d4ec39ad74c83a7d15bfa631f5d60 47636864 ./replay/w1-units.txt
22d64901d7ed2347931861a66cec97c5647a1d58e979967214cb61a09b5e9a3c 4018 ./rescore/rescore-timing.jsonl
83af4226af064e85271e5c6b58d3e7d464a3729058775da69528d5ffab98d47e 271517 ./set/w1-set.json
6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f 54885 ./stage/research/tz23-maker-m0.py
6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61 138209 ./stage/research/tz32-our-quoting.py
c0ed88e96e129f078b062ae7cc44e51f95944b77fb964074a3c85457dc82f026 621 ./state.json
unit files, excepted by §8:
replay/units 288 files 47636864 bytes
rescore/units 18 files 2678061 bytes
rehearsal/units 51 files 7008141 bytes
not listed: ./wt (the branch worktree, pristine at its pushed HEAD), ./report (the report's template and assembly script), ./logs/94-files-written.log (this file)
streams/ entries: 0
selftest-tmp exit=1
```
