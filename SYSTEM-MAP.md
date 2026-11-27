# SYSTEM MAP — btc-5m-twap

**Revision 2026-11-27-a.** Written by the Architect; the Executor never edits it. This is a
**state** document: what exists right now. It holds no mission and no history; the only rules it
holds are those its open items and its closed items' decisions impose on later TZs (§7).

- The CANON (Architect's project instructions, not in this repository) holds the mission, the
  fair-value model, the measured facts and the phase gates.
- `BTC-EXECUTOR-INSTRUCTIONS.md` holds how the Executor works.
- **This map never restates a CANON §1.2 formula.**
- **History is in the reports.** What each TZ did, measured and found is its report on `main` (§1
  lists every one); how this map's own figures moved is in its earlier revisions, the last of them with
  history in it `2026-11-17-a`, `git show 5ef5ee2:SYSTEM-MAP.md`. A figure here is the current one, and the
  report it comes from is named beside it.

---

## 0. Fingerprint gate

Every TZ header states the required revision string and the anchors below. The Executor compares
before doing any work; a mismatch is BLOCKED.

**Revision string:** `2026-11-27-a`

| anchor | value |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` |
| `A4` — executor contract | `6ac6e10aeabc` |
| `A5` — recorder | `0f6c90451cbd` |
| `A6` — pricer | `729f0bcdbee3` |

Anchors are the first 12 hex characters of the SHA-256 of the named artifact, except `A3`.
`A5` is `research/recorder/recorder.py`, the code the live capture runs. `A6` is
`research/pfair.py`, the only implementation of the model: **any TZ that scores a pricer states
`A6`, so what was scored is never in doubt.**

**How each anchor moved, pull request by pull request, is history:** revision `2026-11-17-a`'s §0 carries it, and
§1 below names each merge's report. Since then no anchor has moved; `A4` is `6ac6e10aeabc` since revision
`2026-11-17-a`, when the contract's §1 step 2 came to read §0 and every section, row and item a TZ's header names
(§7 item 174).

### Fingerprint table

Every report states `wc -l` and `sha256sum` for each row. `frozen` rows must match the hash
printed here or the run is BLOCKED. `tracked` rows are reported with no expectation.

| path | lines | bytes | state | SHA-256 |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | — | — | reported | self-reference; report the value you compute |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 235 | 11,255 | frozen | `6ac6e10aeabc3bf83926c509e6d5f868998918f34e32e7e3882e95aad83e2617` |
| `research/twap-divergence.py` | 1,135 | 50,928 | frozen | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` |
| `research/selftest-twap-divergence.py` | 376 | 16,736 | frozen | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` |
| `research/tz02-distribution.py` | 334 | 14,511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` |
| `research/pfair.py` | 441 | 19,357 | frozen | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` |
| `research/selftest-pfair.py` | 619 | 32,559 | frozen | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` |
| `research/tz06-calibration.py` | 577 | 27,138 | frozen | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` |
| `research/tz07a-variance-time.py` | 623 | 28,414 | frozen | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` |
| `research/tz07b-settlement-dispersion.py` | 515 | 24,926 | frozen | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` |
| `research/tz08a-out-of-sample.py` | 745 | 38,822 | frozen | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` |
| `research/tz09-disk-inventory.py` | 894 | 41,004 | frozen | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` |
| `research/tz10b-sigma-or-link.py` | 1,224 | 61,018 | frozen | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` |
| `research/tz11a-student-link.py` | 1,231 | 64,732 | frozen | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` |
| `research/tz12-sized-gate.py` | 1,157 | 61,637 | frozen | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` |
| `research/tz13-sized-gate-test3.py` | 1,074 | 53,901 | frozen | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` |
| `research/tz14-quote-inventory.py` | 2,124 | 109,972 | frozen | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` |
| `research/tz15-phase2-gate.py` | 1,517 | 73,799 | frozen | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` |
| `research/tz16a-phase2-decisive-gate.py` | 2,198 | 111,192 | frozen | `3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125` |
| `research/tz17-settlement-chain.py` | 1,102 | 38,622 | frozen | `e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92` |
| `research/tz18a-chainbook-capture.py` | 1,683 | 69,517 | frozen | `e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae` |
| `research/tz20-capture-under-systemd.py` | 771 | 36,528 | frozen | `104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7` |
| `research/tz21-recorder-memory.py` | 1,284 | 59,009 | frozen | `d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f` |
| `research/tz23-maker-m0.py` | 1,184 | 54,885 | frozen | `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` |
| `research/tz24-nesting-b2.py` | 1,535 | 76,142 | frozen | `4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b` |
| `research/tz26-nesting-b3-capture.py` | 2,492 | 118,466 | frozen | `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec` |
| `research/tz27-pairbook-archive.py` | 2,078 | 106,284 | frozen | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` |
| `research/tz28-pairbook-archive-timer.py` | 1,438 | 74,576 | frozen | `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4` |
| `research/tz29-maker-m0-second-look.py` | 1,225 | 68,959 | frozen | `18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905` |
| `research/tz30-nesting-b3-measure.py` | 2,518 | 131,119 | frozen | `93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab` |
| `research/tz31-who-earns.py` | 1,523 | 84,775 | frozen | `7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765` |
| `research/tz32-our-quoting.py` | 2,576 | 138,209 | frozen | `6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61` |
| `research/tz33-reward-book-capture.py` | 3,542 | 175,160 | frozen | `a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670` |
| `research/tz34-rewardbook-archive-timer.py` | 1,791 | 99,388 | frozen | `1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72` |
| `research/tz35-advisor-deploy.py` | 802 | 42,049 | frozen | `d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5` |
| `research/tz36-advisor-trust.py` | 582 | 32,925 | frozen | `a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5` |
| `research/tz37-capital-allocation.py` | 808 | 51,269 | frozen | `eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb` |
| `research/tz38-adv3-pit-validation.py` | 1,782 | 90,181 | frozen | `579474b65329662f7bed735994381241a928a2c65a726cec3f933dc7afd4427b` |
| `research/tz39-advisor-checks.py` | 1,139 | 73,892 | frozen | `18294b0916d77b226083a18f9521f06e2fddb423bbc947a2e1100fd42b2980f3` |
| `research/tz40-advisor-strong.py` | 1,436 | 95,474 | frozen | `4403b27185f7e9aaa090dedfca457af6c4f70b6b020f0d2fcd9f9fbb96b6054b` |
| `research/tz42-advisor-registry.py` | 2,088 | 134,077 | frozen | `b6c45490b2f86f5c4678c645041ef1556b1199a6bc814470de904aedf7f5105f` |
| `research/tz43-l0-our-quote.py` | 3,056 | 152,905 | frozen | `48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf` |
| `research/tz44-l0-inputs-release.py` | 1,616 | 90,703 | frozen | `0b78807d9c5dec087138b0c9a329cb8c976157ab5c8a3fd4deee7cb31e89e190` |
| `research/tz45-l0-rule-w.py` | 4,299 | 233,655 | frozen | `4720e78573e54b1325dd24af7c30e0de59bfb4c1879d309a23fa6bab6b32d2d4` |
| `research/tz46-capture-room.py` | 1,644 | 88,254 | frozen | `363b269c462d14da1656feb7bad92fec43adb1593209131fe5ca6e5c9f6755f6` |
| `research/tz49-live-host.py` | 2,127 | 113,254 | frozen | `efcc5ead077b396fe18d243f3c65fa9824baca56e6db5312058971e0dfe6049b` |
| `research/tz53-l1-account.py` | 3,324 | 188,378 | frozen | `e4b72d0e285f1d8736a056012d3c9056f7f103e8e899742e10e488932c910c94` |
| `research/tz54-liq-guard.py` | 3,323 | 188,349 | frozen | `fd8f8c21d3dc5c36655a6948ce593a03d06ca8f783955ea7d18df5a57ea0e4bf` |
| `research/tz55-liq-guard-v2.py` | 3,323 | 188,383 | frozen | `1f7e9e8393ec3efda564a2ee0ff8356228f1ab2e435acad5f6f4729a9870bf35` |
| `docs/l1-sign.html` | 218 | 11,846 | frozen | `f1d92e7dd8a8cd15b7b96b86b357ebf80db4e10844b3fc269e92cef0aecba528` |
| `research/recorder/recorder.py` | 651 | 27,821 | frozen | `0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7` |
| `research/recorder/config.py` | 112 | 4,773 | frozen | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` |
| `research/recorder/manifest.py` | 254 | 10,002 | frozen | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` |
| `research/recorder/analyze.py` | 813 | 34,705 | frozen | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` |
| `research/recorder/probe.py` | 227 | 9,324 | frozen | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` |
| `research/recorder/selftest.py` | 573 | 30,591 | frozen | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` |
| `deploy/systemd/btc-recorder.service` | 23 | 707 | frozen | `3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1` |
| `deploy/systemd/btc-chainbook.service` | 22 | 724 | frozen | `a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2` |
| `deploy/systemd/btc-pairbook.service` | 22 | 761 | frozen | `ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8` |
| `deploy/systemd/btc-pairbook-archive.service` | 17 | 794 | frozen | `2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7` |
| `deploy/systemd/btc-pairbook-archive.timer` | 13 | 417 | frozen | `07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913` |
| `deploy/systemd/btc-rewardbook.service` | 23 | 817 | frozen | `7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec` |
| `deploy/systemd/btc-rewardbook-archive.service` | 17 | 810 | frozen | `a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f` |
| `deploy/systemd/btc-rewardbook-archive.timer` | 12 | 435 | frozen | `7b0804285af6987340838bd59573897d013cf97edc5d4132cda7f3f9ba3e3824` |
| `deploy/systemd/adv3-bot.service` | 27 | 863 | frozen | `82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66` |
| `deploy/systemd/l1-bot.service` | 29 | 1,014 | frozen | `a6305d0e7a220ea88f5a4d2be612cac35f3dbe527d7c3b7ed12fd7c47f956266` |
| `engine/l1-bot.py` | 3,656 | 188,968 | frozen | `98851b3c0df447ed7c846edfbf18b9ea1611d12228a4d9a3c1fda3b4f22da214` |
| `deploy/systemd/liq-guard.service` | 30 | 1,086 | frozen | `11bff792d802cbf1abe9ee4f496c24517cce0e63a0dbf6aa49f277b7cdc55157` |
| `guard/liq-guard.py` | 2,772 | 148,628 | frozen | `6b851f3f93578dadcb683d33969b4d235daf2c852dbdce74c66e978946ec840a` |
| `advisor/RULE-ADV-3.txt` | 33 | 3,203 | frozen | `ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169` |
| `advisor/adv3.py` | 895 | 51,834 | frozen | `81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1` |
| `advisor/adv3-bot.py` | 2,548 | 157,438 | frozen | `c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11` |
| `advisor/selftest-adv3.py` | 256 | 19,111 | frozen | `6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398` |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` |

Hashes are of the file as committed on `main` at revision date, verified by the Architect against
`origin/main` — not copied from a report. Changing a `frozen` row requires a TZ that authorizes
it and a new map revision. **The six recorder files are frozen because the live capture runs
them**: an unauthorized edit is a change to a running instrument. **`pfair.py` is frozen because
every score this project will ever quote comes out of it** — both links and the four measured
tables. `tz07a-variance-time.py`, `tz07b-settlement-dispersion.py`, `tz08a-out-of-sample.py`,
`tz09-disk-inventory.py`, `tz10b-sigma-or-link.py`, `tz11a-student-link.py`, `tz12-sized-gate.py`
and `tz13-sized-gate-test3.py` are frozen because a committed measurement came out of each — for
`tz12-sized-gate.py` that is `SIGMA_LOG_NU`, the member-bootstrap spread of `log ν̂`, and the sized
gate; for `tz13-sized-gate-test3.py`, the first verdict under it; for `tz14-quote-inventory.py`, the
first read of the book — and it also holds **the only implementation of CANON §1.1's taker fee,
`fee_pp`, and of the executable touch, `touch_of`**, so every later TZ imports them from it and none
writes them again. `tz15-phase2-gate.py` is frozen for Phase 2's first reading, and because it holds
**the only implementation of the exact Poisson-binomial tail, `pb_upper`, its critical count, `crit`,
and the after-fee selection, `select`**, which a later TZ imports and never writes again.
`tz16a-phase2-decisive-gate.py` is frozen for Phase 2's first decisive look, and because it holds
**the only implementation of the look's arithmetic — `up`, `low`, `critical_upper`, `critical_lower`,
`look_constants`, `read_look`, `dependence` and `residual_dependence`** — which TZ-16a §4.2 requires the
second look to import and never write again.
`tz17-settlement-chain.py` is frozen for the backup track's first answer, B0, and because it holds
**the first committed request outside the recorder that the venue's edge serves** — `Accept:
application/json` and a `User-Agent` of its own, where Python's default agent is refused (§6).
**`tz18a-chainbook-capture.py` is frozen because the chain book service runs its copy byte for byte**
— an unauthorized edit is a change to a running instrument, as for the recorder — and for B1's
answer; its `build_request` is the second such request, `User-Agent: btc-5m-twap-tz18a`.
`tz06-calibration.py` is frozen at
its post-PR-#9 hash: it carries `after` and `need`, and at their defaults the run is the one TZ-06
ran. **The nine unit files are frozen because systemd holds them**: `/etc/systemd/system/` holds each byte for
byte, as every host gate asserts with `cmp`, so an unauthorized edit is a change to a running unit's definition —
or, for the chain book's, disabled since TZ-26, to its fallback's; each archive's service is started by its timer
alone.
`tz20-capture-under-systemd.py` is frozen for the deployment proof that came out of it, and
`tz21-recorder-memory.py` for TZ-21's: the bounded recorder serves every slice the old code served, byte for byte.
`tz23-maker-m0.py` is frozen for M0's first look, and because it holds **the only implementation of the makers' side
of a taker fill, `maker_terms`, the 20% rebate, `rebate`, a member's sums by band, `aggregate`, the anytime-valid
thresholds, `gate_constants`, and the reading, `reading`**, with the set rule, `qualify` and `candidates` — which M0's
second look imports and never writes again (§5).
`tz24-nesting-b2.py` is frozen for B2's reading, VIOLATION, and because it holds **the only implementation of the
nested pair's arithmetic — the dominated pair of a window, `pairs_of`, its settlement payoff, `payoff`, a leg's cost
after the taker fee under both ways the venue could collect it, `costs`, the firm and loose classes, `classify`, and
the reading, `reading_of`, with NONE's alternative `theta1` and its `power`** — which B3's measurement imports and
never writes again (§5).
**`tz26-nesting-b3-capture.py` is frozen because the pair book's unit runs its copy byte for byte** — an
unauthorized edit is a change to a running instrument, as for the recorder — and for B3's capture; its
`build_request` is the third request the venue's edge serves, `User-Agent: btc-5m-twap-tz26`, and its store's
layout — `next_stream_path`'s names, `stream_bytes_total`'s count, `stream_off_reason`'s floor and cap — is what
TZ-27 reads that store by (§2.5).
**`tz27-pairbook-archive.py` is frozen for the archive it carried out, and because TZ-28's and TZ-34's instruments load it
byte for byte, asserted by its SHA-256, and both archives' timers run it:** its set rule, `inventory`, its proofs,
`upload_set`, `verify_release` and `delete_set`, and its readings of the restart, `restart_reading`, `counter_reading` and
`resume_decision`, are the pair book's archive's, its proofs and its audit hook the reward book's archive's too, and are
written nowhere else — an unauthorized edit is a change to a running instrument.
**`tz28-pairbook-archive-timer.py` is frozen because both archives' timers run its copy byte for byte** — the pair book's
as its `run`, the reward book's through TZ-34's, which loads it by its SHA-256 — an unauthorized edit is a change to a
running instrument — and for the deployment it carried: its `run` loads `tz27-pairbook-archive.py` from beside itself by
its SHA-256, and its idle stretch, `idle_wait`, its ledger and its resume rule are both archives' and are written nowhere
else.
`tz29-maker-m0-second-look.py` is frozen for M0's reading over both looks, NO EARN, which closed the maker track for
its window (§4, §5): the first look read from the forensic store, the sum over both looks and the fetch held to the
idle stretch are written in it and nowhere else.
`tz30-nesting-b3-measure.py` is frozen for B3's reading, NO CAPTURE, which closed the backup track (§4, §5): the replay of
a window's streams at venue time, the capture rule, every book rebuilt against the stored replies and the reading over
eight blocks are written in it and nowhere else.
`tz31-who-earns.py` is frozen for W0's reading, W-EARN, which opened W1 (§4, §5): the makers' rows of a market — its
full feed less its takers' rows, as multisets — each wallet's own position from its rows with their side flipped, the two
named groups' sums over each market's life and the fetch held to the idle stretch are written in it and nowhere else.
`tz32-our-quoting.py` is frozen for W1's reading, W1-NO-EARN, which closed the W track (§4, §5): the replay of a
five-minute leg's streams at venue time — its Up book rebuilt from the stored frames, a match read from the Up token's
own book frame of the same stamp, our quotes queued at their level, filled by a match's sweep or, once the 150 ms
taker delay has passed, by an order that crosses them, refused where they would cross, cancelled through a one-way
latency — under nine variants is written in it and nowhere else.
**`tz33-reward-book-capture.py` is frozen because the reward book's unit runs its copy byte for byte** — an unauthorized
edit is a change to a running instrument — and for L0's capture: its selection rule, `run_rule` through `LiveFetch` or
`StoredFetch`, its slot schedule and its store's layout — the names under `/var/lib/btc-rewardbook/<D0>/`, the stream
files' sum taken again at every slot's decision, the floor and the cap that keep a slot's stream off — are what L0's
measurement and the reward book's archive read that store by (§2.6), and its `build_request` is the fourth request the
venue's edge serves, `User-Agent: btc-5m-twap-tz33`.
**`tz34-rewardbook-archive-timer.py` is frozen because the reward book's archive's timer runs its copy byte for byte**
— an unauthorized edit is a change to a running instrument — and for the deployment it carried: its `run` loads
`tz28-pairbook-archive-timer.py`, and through it `tz27-pairbook-archive.py`, from beside itself by their SHA-256; its set
of a store's closed slots, `inventory`, its removal while the reward book is quiet, `quiet`, `removal_wait` and
`remove_set`, and its readings — G-TRIGGER, G-SET, G-NEXT and G-STILL as pure functions — are written in it and nowhere
else.
`research/tz35-advisor-deploy.py` is frozen for the deployment it carried: `number`, the check CANON hard rule 2 asks of
a TZ's §0.5, and its readings of the advisor's unit — `props`, `unit`, `daily`, `load`, `restart`, `still` and `stopped` —
are written in it and nowhere else. **`advisor/adv3.py` and `advisor/adv3-bot.py` are frozen because the advisor's unit
runs its copies byte for byte** — an unauthorized edit is a change to a running instrument — and because `adv3.py` is
ADV-3's only implementation (CANON PART VII); `advisor/RULE-ADV-3.txt` is frozen because the rule is, its SHA-256 carried
as `RULE` inside `adv3.py`; and `advisor/selftest-adv3.py` with the code it tests.
`research/tz38-adv3-pit-validation.py` is frozen for the exploration it carried and because it holds **the only
implementations of the PIT and market records' readings — `admissible`, `rule_pass`, `strong_pass`, `monthly`,
`monthly_sum`, `read_series` and `power`** (CANON PART VII), which the reading's TZ imports by hash and never writes again.
`research/tz39-advisor-checks.py` is frozen for the deployment it carried: its readings of the advisor's checks — `sign_sum`, `walk`, `alert_checks`, `render_checks`, `unit_checks` and `first_checks` — are written in it and nowhere else.
`research/tz40-advisor-strong.py` is frozen for the deployment it carried: its readings of the views — `own_order`, `own_strong`, `own_stop_pct`, `plan_invariants` and `render_checks` — and of the replay — `latest_slot_text`, `replay_text`, `clock_checks` and `first_checks` — are written in it and nowhere else.
`research/tz42-advisor-registry.py` is frozen for the deployment it carried: its readings of the registry — `own_chain`, `own_seed`, `own_walk`, `replay` and `registry_checks` — of the positions and the model — `own_entry`, `own_stop_pct`, `own_lev`, `pos_ok`, `alloc_checks`, `opens_checks` and `model_checks` — and of the unit — `clock_checks`, `unit_checks`, `first_checks` and `render_checks` — are written in it and nowhere else.
`research/tz43-l0-our-quote.py` is frozen for the reading it carried: L0's set, replay and reading — `slot_problem`, `members_of`, `polls_of`, `Day`, `day_money` and `l0_reading` — are written in it and nowhere else.
`research/tz46-capture-room.py` is frozen for the deployment it carried: its readings of the room, the forensic store and the timers — `room_reading`, `index_assets`, `plan_rows`, `timer_checks`, `trigger_reading`, `next_verdict`, `pair_reading` and `still_reading` — are written in it and nowhere else. **`deploy/systemd/btc-rewardbook-archive.timer` is TZ-46's since PR #46's merge**: `OnCalendar=*-*-* 01/3:30:20 UTC`, no `OnActiveSec` (§2.6).
`research/tz49-live-host.py` is frozen for the deployment it carried: its readings of the live host — `geo_reading`, `v6_state`, `spec_reading`, `live_gate`, `swap_reading`, `log_reading`, `ssh_reading` and `lat_reading` — and its audit hook's IPv4 rules, `policy`, are written in it and nowhere else; **the live host's three drop-ins are its constants' bytes**, `SSHD_TEXT`, `JOURNALD_TEXT` and `SYSCTL_TEXT` (§6, live host).
`docs/l1-sign.html` is frozen for the deployment it carries: **the owner's signing page of L1**, TZ-50's Appendix B byte for byte, served by GitHub Pages from `main`'s `docs/` at `https://seahomebatumi-ai.github.io/btc-5m-twap/l1-sign.html` — Pages turned on by TZ-50's Executor at 06:24:19 UTC on 2026-11-20, and the page read there at these bytes (TZ-50's G-PAGE). It builds one Deposit Wallet batch from its link's fragment — `authorizeSessionSigner` or `revokeSessionSigner` called on the wallet, or `approve` of `1` pUSD on pUSD to the standard or the V2 exchange — and has MetaMask sign it as the owner on Polygon; it makes no request of its own, and no field of a link can name another contract, spender or amount. A change to it is a new page in a new TZ.
**`engine/l1-bot.py` and `deploy/systemd/l1-bot.service` are frozen because L1's unit runs their copies byte for byte on the live host** — an unauthorized edit is a change to a running instrument that holds the Boss's money — and because `l1-bot.py` is the unit's only implementation: rule W's targets and the day's selection it takes by name from `research/tz45-l0-rule-w.py` and `research/tz33-reward-book-capture.py`, by their SHA-256, and writes neither again (`load_frozen`). `research/tz53-l1-account.py` is frozen for the deployment it carried: TZ-52's instrument under TZ-53's names, its deployment checks on both hosts.
**`guard/liq-guard.py` and `deploy/systemd/liq-guard.service` are frozen because the liquidation guard's unit runs their copies byte for byte on the capture host** — an unauthorized edit is a change to a running instrument that watches the Boss's own money — and because `liq-guard.py` is the guard's only implementation: its readings of a position — `parse_positions`, `distance_pct`, `crossed`, `step`, `bracket_for`, `margin_hint`, and since TZ-55 `gain_pct`, `roe_pct`, `next_record`, `profit_step` and `topup_seen` — of its key — `key_reading` — and of its settings — `settings_of` — are written in it and nowhere else. `research/tz54-liq-guard.py` and `research/tz55-liq-guard-v2.py` are frozen for the deployments they carried: TZ-53's checker under TZ-54's and TZ-55's names, their capture-host modes alone.

**This revision's table holds 74 rows — 71 `frozen`, 2 `tracked`, 1 `reported`**, unchanged from revision `2026-11-22-a`, which shipped with TZ-55's verdict and the merge of pull request #53 and replaced two `frozen` rows — `guard/liq-guard.py` and `deploy/systemd/liq-guard.service`, the guard's second version — and added one, `research/tz55-liq-guard-v2.py`, each at TZ-55 §0.1's SHA-256, read by the Architect at the branch's head `7a9593b`. **Revision `2026-11-27-a` ships with TZ-56 and moves no row:** it records L1's stop on its loss limit, the K and H tracks and what K0 rests on (§5, §6, §7 items 199 to 203). A TZ's fingerprint expects revision `2026-11-27-a`, 74 rows, 71 `frozen`, 2 `tracked` and 1 `reported`; the Architect read every row's file at `fd2bec0`, the head of `main` on 2026-11-22 and still on 2026-11-27, 73 file rows of 73 equal to this table's lines, bytes and SHA-256.

---

## 1. Repository

`github.com/seahomebatumi-ai/btc-5m-twap` — **public**, and it must stay so: both archives verify every asset
anonymously (§7 item 128). It holds text alone: no dataset, archive or binary has ever entered git history.

| path | contents |
|---|---|
| `CryptoTZ/` | specifications, Architect → Boss upload — 65 files, `TZ-01` … `TZ-55`, and `TZ-56-k0-favourite.md`, K0's, with this revision's upload; then TZ-57, H0's (§5); no `TZ-22` and no `TZ-25` was ever issued |
| `CryptoReports/` | reports, Executor → straight to `main` — 65 files, one for every TZ number |
| `research/` | measurement code, the pricer and the units' code, Executor → branch + PR — 53 files with PR #53's merge, 6 of them `research/recorder/` |
| `deploy/systemd/` | the units, installed byte for byte under `/etc/systemd/system/` — 11 files: eight services — `l1-bot.service`, L1's unit on the live host, and `liq-guard.service`, the liquidation guard on the capture host, among them — and three timers (§3) |
| `advisor/` | the advisor (CANON PART VII): `RULE-ADV-3.txt`, `adv3.py`, `adv3-bot.py`, `selftest-adv3.py` |
| `docs/` | **the owner's signing page of L1**, `l1-sign.html`, Architect → Boss upload with TZ-50, served by GitHub Pages from `main`, turned on by TZ-50 (§0, the page) — 1 file |
| `engine/` | the live engine — `engine/l1-bot.py`, **L1's unit**, with PR #51's merge (§3, the units) |
| `guard/` | **the liquidation guard** (CANON PART VII) — `guard/liq-guard.py`, its second version with PR #53's merge (§3, the units) |
| root | `SYSTEM-MAP.md`, `BTC-EXECUTOR-INSTRUCTIONS.md`, `.gitignore` |

**Files on `main` at `73a9ba9`: 203 paths, `18,922,612` bytes**, counted by the Architect with `git ls-tree -r -l` on
2026-11-22 — 65 under `CryptoReports/`, 65 under `CryptoTZ/`, 52 under `research/`, 11 under `deploy/`, 4 under
`advisor/`, 1 under `docs/`, 1 under `engine/`, 1 under `guard/` and 3 at the root; PR #53's merge replaces
`guard/liq-guard.py` and `deploy/systemd/liq-guard.service` and adds `research/tz55-liq-guard-v2.py`, `188,383` bytes,
with this map; none ends in
`.parquet`, `.zip`, `.gz`, `.jsonl` or
`.csv`. No copy of this map is kept
anywhere but here: the Architect reads it from the repository (CANON PART III).

**Refs on `origin`, read with `git ls-remote` on 2026-11-22, after TZ-55 (§7 item 55): 219 lines.** `HEAD` and
`refs/heads/main` at `73a9ba93f881436dbe4d0b787471afc32c88b3e0`, TZ-55's report, above `037bca1`, its upload,
`af529f1`, revision `2026-11-21-e`, and `c7c1b5b`, PR #52's merge; then `839d768`, TZ-54's report, above `0b2e935`, its
upload, `aeaca24`, PR #51's merge, and `613254a`, revision `2026-11-21-d`; then `9a20234`, TZ-53's report, above `04f0a15`, its upload,
`14b6bc4`, revision `2026-11-21-c`, and `dc0b34e`, revision `2026-11-21-b`; then `9a02905`, TZ-52's report, above
`0a73d30`, its upload, and `b2b01e1`, revision `2026-11-21-a`; then `b941123`, TZ-51's report, above `4b1e2b8`, its upload, and
`6f12492`, revision `2026-11-20-b`; then `39f22d9`, TZ-50's report, above `a9a6c82`, `b07d7bb` and
`c40b6a4`, its page's upload — the page at the root first, then removed and put at `docs/` — `2781624`, its TZ, and
`401a816`, revision `2026-11-20-a`; then `234a6e8`, PR #47's merge. **29 branches**: `tz-55-liq-guard-v2`, PR #53's head `7a9593b`, open at this read and merged with
this revision; `tz-54-liq-guard`, PR #52's head `8a98166`, merged with revision `2026-11-21-e`; `tz-53-l1-unit`, PR #51's head `3a2e6f2`, merged with revision `2026-11-21-d`; `tz-52-l1-round-trip`, PR #50's head `1719ff4`, never merged, its pull request closed unmerged by TZ-53 — `tz-51-l1-account-round-trip-rerun`, PR #49's head `bfbb104`, its pull request closed
unmerged by TZ-52 — `tz-50-l1-account-round-trip`,
PR #48's head `0774d7e`, never merged, its pull request closed unmerged by the repository's owner — and 23, each its
pull request's head, kept after its merge: `tz-23-maker-m0`, `tz-24-nesting-b2`, `tz-26-nesting-b3-capture`, `tz-27-pairbook-archive`,
`tz-28-pairbook-archive-timer`, `tz-29-maker-m0-second-look`, `tz-30-nesting-b3-measure`, `tz-31-who-earns`,
`tz-32-our-quoting`, `tz-33-reward-book-capture`, `tz-34-rewardbook-archive-timer`, `tz-35-advisor-bot`,
`tz-36-advisor-trust-block`, `tz-37-capital-allocation`, `tz-38-adv3-pit-validation`, `tz-39-advisor-checks`,
`tz-40-strong-every-rank`, `tz-42-advisor-registry`, `tz-43-l0-our-quote`, `tz-44-l0-inputs-release`,
`tz-45-l0-rule-w`, `tz-46-capture-room` and `tz-49-live-host-ipv4-keys`; every earlier branch is deleted. **52
`refs/pull/N/head`**, `1` to `32` and `34` to `53` — no `33` was ever a pull request's number — and one
`refs/pull/53/merge`, PR #53's while it is open: every commit an artifact
names is served there (the table below). **135 tag lines:** `tz-01a-dataset`, annotated, `d3251aa` peeling to
`ea9290b92b9fa50c22d0560d5d01dfa392af44df`; `tz-27-pairbook-streams`, annotated,
`e299d4e45f48b7efaa8cb18bd54b139fc0627630` peeling to `bce5a85be7850a33f95192265b916cc9c5e0aaf1`, the Release
`409534533`; each with its peeled line; `tz-44-l0-inputs`, lightweight at `ab0a8be170786ee9b4c9bfd18ed5a522db669932`,
the Release `443961874`; `tz-45-l0-rule-w-inputs`, lightweight at `01756f665893096ab38ae10dfbe58f074f8fb648`, the
Release `446880816`; **59 `pairbook-streams-<A>`**, lightweight at `d8194fd5b6374140b0052a0aa7b0c10fe7ee6ac3`, one a
run of the pair book's archive that took a new set, the last `1794925184` (§2.5); and **70 `rewardbook-streams-<A>`**,
lightweight at `6a615257277d3c94dafd4d39783499560a344648`, one a run of the reward book's archive that took a new set,
the last `1795332620` (§2.6) — **eight more a day** (§7 item 177). A run that resumes a set adds none. The head of
`main` is never a gate; commits are named where they matter.

**Commits the host runs or a tag stands on:** `e3975b5` — `research/recorder/` as the recorder's unit runs it, PR
#22's head; `ca4bbc1` — the chain book's code, PR #19's head; `e8b46a8` — the pair book's, PR #25's; `d8194fd` — the
pair book's archive's, PR #27's, every `pairbook-streams-*` tag's; `2dcd70e` — the reward book's, PR #32's; `6a61525`
— the reward book's archive's, PR #34's, every `rewardbook-streams-*` tag's; `4e6db2d` — the advisor's bot's, PR
#41's; `3a2e6f2` — L1's unit's, PR #51's head, whose files the live host runs from `/root/l1-bot-svc` (§3); `7a9593b` — the
liquidation guard's second version, PR #53's head, whose files the capture host runs from `/root/liq-guard-svc` (§3); `ea9290b` — the observation set's tag; `bce5a85`, `ab0a8be`, `01756f6` — the three other Releases' tags.

### Every TZ, its report and its pull request

The report is the record of the TZ: what it did, measured and found. Path `CryptoReports/<name>-report.md`; the
specification `CryptoTZ/<name>.md`. A pull request was merged unless the row says otherwise.

| TZ | name | reading, by the report's own status line | pull request — head |
|---|---|---|---|
| TZ-01 | `TZ-01-twap-divergence` | Gate A PASS, Gate B PASS — **withdrawn**, scored against §2.2's labels | — |
| TZ-01a | `TZ-01a-twap-divergence-corrected` | Gate A FAIL, Gate B PASS — **withdrawn**; its dataset is §2.1's | — |
| TZ-02 | `TZ-02-divergence-distribution` | Gate A2 PASS — **withdrawn** | — |
| TZ-03 | `TZ-03-repo-hygiene` | executed as written | #1 — `d9e58e8` |
| TZ-04 | `TZ-04-market-recorder` | BLOCKED: a disk floor from assumption (§7 item 6) | — |
| TZ-04a | `TZ-04a-market-recorder-corrected` | BLOCKED: 200 consecutive intervals (§7 item 8) | — |
| TZ-04b | `TZ-04b-market-recorder-scoring` | **Phase 0 closed**, 200 of 200 | #2 — `3895356`, the recorder it scored; #3 — `ee2f632`, merged after its verdict |
| TZ-05 | `TZ-05-quote-capture` | BLOCKED: one session cannot deploy and measure (§7 item 11) | #4 — `0e13a5c`, closed |
| TZ-05a | `TZ-05a-quote-capture-deploy` | Tier C deployed | #5 — `4216c04` |
| TZ-06 | `TZ-06-pfair-calibration` | the Phase 1 pipeline; the normal link not disqualified by its gate | #6 — `5ed667a` |
| TZ-07 | `TZ-07-variance-time` | BLOCKED: the fingerprint could not be performed | — |
| TZ-07a | `TZ-07a-variance-time` | the feed's variance–time curve; its correction superseded | #7 — `c44af68` |
| TZ-07b | `TZ-07b-settlement-dispersion` | the settlement quantity's dispersion; `SD_SCALE` | #8 — `26bbb61` |
| TZ-08 | `TZ-08-out-of-sample` | BLOCKED at V2 before any score | — |
| TZ-08a | `TZ-08a-out-of-sample` | the normal link FAILS G3 at `tau` 60 and 30 | #9 — `e2625ea` |
| TZ-09 | `TZ-09-disk-inventory` | the host's disk inventoried; the consumer named (§6) | #10 — `e45f38e` |
| TZ-10 | `TZ-10-sigma-or-link` | BLOCKED at its self-tests | — |
| TZ-10a | `TZ-10a-sigma-or-link` | BLOCKED at V2 | — |
| TZ-10b | `TZ-10b-sigma-or-link` | the heavy tail is not a lagging `sigma` | #11 — `d34606e` |
| TZ-11 | `TZ-11-student-link-and-domain` | BLOCKED at §5.2 item 5 | — |
| TZ-11a | `TZ-11a-student-link-and-domain` | the Student link fitted and frozen; closed by its own unsized gate | #12 — `2746518` |
| TZ-12 | `TZ-12-sized-gate` | the sized gate's error rates, measured exactly | #13 — `6dc0e24` |
| TZ-13 | `TZ-13-sized-gate-test3` | the Student link **not disqualified** at `tau` 240 … 60 | #14 — `7ef9723` |
| TZ-14 | `TZ-14-quote-inventory` | the book, inventoried over 1,200 intervals | #15 — `ffef5cd` |
| TZ-15 | `TZ-15-phase2-gate` | Phase 2's first gate UNDECIDABLE at five `tau` | #16 — `f7f171a` |
| TZ-16 | `TZ-16-phase2-decisive-gate` | BLOCKED at its input assertion | — |
| TZ-16a | `TZ-16a-phase2-decisive-gate` | **NO EDGE** at `tau` 180, 120, 90, 60; UNDECIDABLE at 240, final | #20 — `5076b43` |
| TZ-17 | `TZ-17-settlement-chain` | **B0 PASS**, 200 of 200 | #17 — `8f1bc93` |
| TZ-18 | `TZ-18-chainbook-capture-deploy` | G-DEPLOY FAIL, every request refused | #18 — `8caa0b4`, closed unmerged |
| TZ-18a | `TZ-18a-chainbook-capture-redeploy` | **B1 PASS**: the chain book deployed | #19 — `ca4bbc1` |
| TZ-19 | `TZ-19-phase2-second-look` | BLOCKED at its host gate: the recorder had stopped | — |
| TZ-20 | `TZ-20-capture-under-systemd` | PASS: both captures as system units | #21 — `0956da1` |
| TZ-21 | `TZ-21-recorder-memory` | PASS: the recorder's memory bounded | #22 — `e3975b5` |
| TZ-23 | `TZ-23-maker-m0` | M0's first look UNDECIDABLE | #23 — `7f5ae3f` |
| TZ-24 | `TZ-24-nesting-b2` | **B2 VIOLATION** | #24 — `6f045cf` |
| TZ-26 | `TZ-26-nesting-b3-capture` | PASS: the pair book deployed | #25 — `e8b46a8` |
| TZ-27 | `TZ-27-pairbook-archive` | PASS: the first streams moved to a Release | #26 — `bce5a85` |
| TZ-28 | `TZ-28-pairbook-archive-timer` | PASS: the pair book's archive on a timer | #27 — `d8194fd` |
| TZ-29 | `TZ-29-maker-m0-second-look` | **M0 NO EARN** over both looks | #28 — `f6425f7` |
| TZ-30 | `TZ-30-nesting-b3-measure` | **B3 NO CAPTURE** | #29 — `fcd9ca5` |
| TZ-31 | `TZ-31-who-earns` | **W0 W-EARN** | #30 — `404288f` |
| TZ-32 | `TZ-32-our-quoting` | **W1 W1-NO-EARN** | #31 — `b601f75` |
| TZ-33 | `TZ-33-reward-book-capture` | PASS: the reward book deployed | #32 — `2dcd70e` |
| TZ-34 | `TZ-34-rewardbook-archive-timer` | PASS: the reward book's archive on a timer | #34 — `6a61525` |
| TZ-35 | `TZ-35-advisor-bot` | PASS: the advisor's bot deployed | #35 — `6c74b62` |
| TZ-36 | `TZ-36-advisor-trust-block` | PASS: the card's basis and invalidation | #36 — `4446289` |
| TZ-37 | `TZ-37-capital-allocation` | PASS: the budget view | #37 — `6d70c6a` |
| TZ-38 | `TZ-38-adv3-pit-validation` | the PIT procedure, explored in sample; moves no rung | #38 — `8f37199` |
| TZ-39 | `TZ-39-advisor-checks` | PASS: two checks a day | #39 — `fc68758` |
| TZ-40 | `TZ-40-strong-every-rank` | PASS: STRONG at every rank | #40 — `433ce13` |
| TZ-41 | `TZ-41-l0-our-quote` | BLOCKED at G-SET before any reading | #42 — `cca1109`, closed unmerged |
| TZ-42 | `TZ-42-advisor-registry` | PASS: the registry and the Boss's model | #41 — `4e6db2d` |
| TZ-43 | `TZ-43-l0-our-quote` | **L0 UNDECIDABLE** | #43 — `ab0f387` |
| TZ-44 | `TZ-44-l0-inputs-release` | PASS: L0's inputs in a public Release | #44 — `ab0a8be` |
| TZ-45 | `TZ-45-l0-rule-w` | **L0's rule W EARN** | #45 — `01756f6` |
| TZ-46 | `TZ-46-capture-room` | PASS: the capture keeps its room | #46 — `c9d1071` |
| TZ-47 | `TZ-47-live-host` | BLOCKED at §0.6: LH1, the live host's name compared whole (§7 item 180) | — |
| TZ-48 | `TZ-48-live-host-rerun` | BLOCKED at §0.6: G-GEO UNREAD — IPv4 `BG`, not blocked; IPv6 no working path on the host (§7 item 181) | — |
| TZ-49 | `TZ-49-live-host-ipv4-keys` | **KEEP: the live host prepared** — G-GEO PASS over IPv4 alone, `BG`; root by key alone; its own swap adopted, its journal bounded; G-LAT PASS, `28.148` ms one way | #47 — `9515874` |
| TZ-50 | `TZ-50-l1-account-round-trip` | BLOCKED at §3.7, B-OWNER: its `Tty` opened `/dev/tty` `"r+"`, unseekable, before any question (§7 item 189); before it every gate PASS — G-GEO `BG`, G-ENV, G-PAGE, G-KEY made | #48 — `0774d7e`, closed unmerged by the repository's owner |
| TZ-51 | `TZ-51-l1-account-round-trip-rerun` | BLOCKED at §3.7, G-APPROVE: the venue's relayer approves an exchange at MaxUint256 alone (§7 items 190 and 191); before it G-AUTH PASS — the session key authorized for the bot's wallet — and every gate PASS | #49 — `bfbb104`, closed unmerged by TZ-52 |
| TZ-52 | `TZ-52-l1-round-trip` | BLOCKED at §3.9, G-RT: **the venue took the session key's order live, in `127` ms**, then answered its read by id with `null`, which the instrument did not handle; `cancel_all` cancelled it (§7 item 192); before it G-READY 7 of 7, `11.10` pUSD, both allowances the maximum; the bot's chat pinned | #50 — `1719ff4`, closed unmerged by TZ-53 |
| TZ-53 | `TZ-53-l1-unit` | **G-DEPLOY PASS:** L1's unit installed and running on the live host since 08:37:35 UTC on 2026-11-21; before it started, its own code proved its order path and its stop — G-PROVE 8 of 8 on CTF and negative-risk, the Boss's «Стоп» in `7.1` s, G-HOLD exit `3` with no request | #51 — `3a2e6f2` |
| TZ-54 | `TZ-54-liq-guard` | **G-DEPLOY PASS:** the liquidation guard installed and running on the capture host since 18:30:43 UTC on 2026-11-21; before it started, its own code proved its request paths — G-PROVE 10 of 10, the key read-only and bound to the host's address, what it sees confirmed by the Boss («да» after 76 s), its test alarm acknowledged after 92 s — and G-LIVE read `179` polls, none failed | #52 — `8a98166` |
| TZ-55 | `TZ-55-liq-guard-v2` | **G-DEPLOY PASS:** the guard's second version installed and running on the capture host since 10:01:40 UTC on 2026-11-22; G-PROVE 11 of 11 — what it sees and how its two examples look confirmed by the Boss, its test alarm acknowledged after 61 s; the positions unwatched `1,133.939` s while he answered; G-LIVE read `176` polls, none failed | #53 — `7a9593b` |

**Sixteen reports are BLOCKED reports** by their status lines — TZ-04, TZ-04a, TZ-05, TZ-07, TZ-08, TZ-10, TZ-10a,
TZ-11, TZ-16, TZ-19, TZ-41, TZ-47, TZ-48, TZ-50, TZ-51 and TZ-52 — eleven with no pull request, TZ-05's, TZ-41's,
TZ-50's, TZ-51's and TZ-52's closed unmerged, so none moved a `research/` file. A report is never edited (CANON hard rule 4).

---

## 2. Data

### 2.1 The observation set — the only dataset that exists

| field | value |
|---|---|
| location | Release `TZ-01a validated observation set`, tag `tz-01a-dataset`, public |
| asset | `twap-divergence-observations.parquet` |
| size | 76,818,669 bytes |
| SHA-256 | `229a944f2d5111c3e68b1fa0630f8e8658356147f9669d18665e575b60f3716b` |
| rows | 1,051,170 — 210,234 intervals × 5 checkpoints |
| checkpoints | `tau` ∈ {240, 180, 120, 90, 60} seconds remaining |
| window | 2024-09 … 2026-08, 730 days |
| source | `data.binance.vision`, spot `BTCUSDT`, 1-second klines, 63,072,000 bars, each monthly archive checksum-verified |
| gaps | 0 missing bars, 0 forward-fills; 210,240 intervals found, 210,234 used |

Anyone can fetch and verify it with no token:
`curl -sL https://github.com/seahomebatumi-ai/btc-5m-twap/releases/download/tz-01a-dataset/twap-divergence-observations.parquet | sha256sum`

**Columns (25).** Keys `interval_open_ts`, `month`, `tau`, `t`. Inputs `K`, `S_t`, `naive_move`,
`twap_so_far`, `state`. Volatility `sigma_pre`, `sigma_live`, `sd_remaining_pre`,
`sd_remaining_live`. Prices `p_twap_pre`, `p_naive_pre`, `p_twap_live`, `p_naive_live`.
Settlement proxies `twap_1s`, `twap_30s`, `twap_60s`, `outcome_1s`, `outcome_30s`, `outcome_60s`.
Integrity `n_missing_bars`, `prior_filled_bars`.

**The price data and the integrity accounting remain valid.** The `p_twap_*` columns implement
the superseded `p_interval` model and the `outcome_*` columns are invalid labels — see §2.2. This
set is Binance data and can no longer supply a label to anything.

### 2.2 The outcome labels are invalid — withdrawn 2026-09-10

`outcome_1s`, `outcome_30s` and `outcome_60s` are all **full-interval averages** of Binance
prices compared against the interval open, at 1 / 30 / 60-second sampling.

**No Polymarket settlement rule has ever had that shape.** Before 2026-08-07 the venue compared a
single close against a single open. Since 2026-08-07 it compares two readings of a Chainlink
trailing-TWAP feed — one at the close, one at the open — with a 30-second lookback until
2026-08-14 and 60 seconds after it.

The three labels are therefore withdrawn, along with every score computed against them. They stay
in the Parquet file for forensics and are never used again. The 4.147% disagreement between
`outcome_1s` and `outcome_60s` is a fact about two invalid labels and carries no information.

Correct labels are the venue's own resolutions, captured per interval as `resolution.json`. TZ-04b
read 200 of them and TZ-06 read 400.

### 2.3 The recorder — `btc-recorder.service`: Tier A since 2026-09-10 10:21:09 UTC, Tier C since 2026-09-12 09:53:05 UTC

**The process:** pid `1555954`, `NRestarts` `0`, active since 2026-11-14 06:11:41 UTC — the package manager's
restart (§7 item 176) — running `research/recorder/recorder.py` at `e3975b5`, `0f6c9045…` (`A5`), in the detached
worktree `/root/btc-recorder-svc`, under `/root/tz04a-env` (§3, §6). Its stop is K-20R,
`systemctl disable --now btc-recorder.service`. Read-only at every venue: no order path, no credential.

**The store**, `/var/lib/btc-recorder/`, outside the repository: one directory per five-minute interval `T0`, holding
the streams `twap60`, `twap30`, `chainlink` and `binance`, one gzipped file each; `gamma.json`, the market document
at `T0 + 5`; `resolution.json`, the venue's settled document, polled from `T0 + 333` every 15 s; `quotes.jsonl.gz`,
**Tier C** — the `/book` of both tokens at `tau` 240, 180, 120, 90, 60, 30 and 10, fourteen replies, each verbatim
with its HTTP status; and `manifest.json`. In the root, `runtime.jsonl` and `recorder.log`. Reports carry the venue
payload's own `timestamp` in milliseconds and `full_accuracy_value` at full precision. **The manifest exception:** a
manifest carries the capture's own accounting — message counts, gaps, disconnects, clock offsets, `complete`,
`quotes_complete`, and each Tier C read's `tau`, token, status and offset — and no price, size, fill or outcome
(`research/recorder/manifest.py`, the return at lines 217 to 233), so a TZ barred from every other file of the capture
may still read manifests. `1,657,840,396` bytes by `du -sb` at TZ-46's close.

**Its bounds** (`research/recorder/config.py` lines 21 and 22; `recorder.py` `check_floors`, lines 291 to 303), read
at start-up and at the close of every interval: below `2,000,000,000` bytes free, or once the apparent bytes of its
own tree reach `4,000,000,000`, it opens no interval, closes the open ones and exits `0`, which its unit does not
restart (§7 item 179). **The `527` intervals `1790941200` … `1791099000`, 2026-10-02 11:40 to 2026-10-04 07:39 UTC,
were never captured** — RTDS keeps no history (CANON §1.1); every restart since is a recorded gap of seconds.

**Its footprint:** `33,632,842` bytes a day on disk and `26,784,064` apparent (TZ-09); Tier C `6,293.6` bytes an
interval stored and `61,971.6` raw (TZ-14). The feeds publish at 1 Hz (TZ-06); the venue's resolution reaches the
recorder a median of `318` s after the close (TZ-04b). What the book showed over 1,200 intervals — the worst price
first, the touch at the minimum size, the book emptying toward the close — is §4's, from TZ-14.

**What has been read of it** is §5's table: the Phase 0 to Phase 2 sets, the last TZ-16a's 2,400 members to `T0`
`1790452200`. **No TZ has read a quote of a later interval**; TZ-30 read `twap60` of B3's walked candidates for the
strikes. TZ-16a's reserve is released (CANON §1.5), so no span of this capture is held for a reading.

### 2.4 What is not in the data

**Nothing in the repository is a capture**: no Chainlink tick, Polymarket quote, book, fill or fee-paid figure is in
git history, and none ever will be. **Settlement readings are, where an audit route needs them:** TZ-17's report prints
the venue's published price to beat at every boundary of its 200 windows. On the host, the oracle feed, the books of
the five-minute market at seven checkpoints, the nested pair's books and streams and the reward markets' books,
trades and reward polls all exist (§2.3, §2.5, §2.6); in Releases, the observation set and every archived stream.

### 2.5 The fifteen-minute market, the chain book and the pair book — both captures stopped

**What the nesting is** (§4, from TZ-17 and TZ-18): the fifteen-minute market opening at `T` and the five-minute
market opening at `T` publish the same price-to-beat literal, both families name one resolution source, and the
reading a market settles on, `finalPrice`, is the next market's `priceToBeat` as the same literal. **Where the reading
at `T+600` is at or above the reading at `T`, every state that resolves `btc-updown-5m-{T+600}` Up resolves
`btc-updown-15m-{T}` Up**, and symmetrically below. TZ-17's 801 settled documents are held by hash in
`/root/btc-forensics/`; at the venue their readings are stable and their bytes are not (§7 item 100).

**The chain book — disabled since 2026-10-10 19:30:06 UTC (TZ-26).** `btc-chainbook.service`, its code
`/root/tz18a-svc/tz18a-chainbook-capture.py`, `e9cb9b47…` at `ca4bbc1`, under `/root/tz01-env`; its stop K-20C. Its
store, `/var/lib/btc-chainbook/`, `43,108,667` bytes by `du -sb` at TZ-46's close: for each 900-second window `T`, the
documents of `btc-updown-15m-{T}` and `btc-updown-5m-{T+600}` at `T+625`, four `/book` reads — both tokens of both
markets, released together — at seven checkpoints from `T+655` to `T+885`, and `window.json` at `T+905`; its windows
run from 2026-09-23 17:39:50 UTC to `1791659700`. TZ-18's 32 windows `1790117100` … `1790145000` hold two `403`
documents each and no book; **the `90` windows `1791018000` … `1791098100` are lost** (TZ-19, TZ-20 reports). **Reserved
from its first byte, on Tier C's terms** (TZ-18 §9): no TZ but one that scores it extracts a value from a body stored
under `/var/lib/btc-chainbook/`, a book reply or a market document, and no other report prints a price, size, spread,
mid, book level or outcome from one; a deployment proof reads each stored line's status, byte count, SHA-256 and times,
and whether its body parses, and nothing else; `window.json` and `runtime.jsonl` are excepted. **B2 read every window
to `1791241200`; the later ones are unread.** **The interlock:** while the chain book ran, one five-minute interval in
three, `T0 ≡ 600 (mod 900)`, carried its load, from 2026-09-23 17:39:50 to 2026-10-10 19:30:06 UTC; a TZ that reads
Tier C over such intervals carries TZ-16a's interlock, which read HOLD over 297 exposed intervals (TZ-16a report).

**The pair book — stopped and disabled by TZ-46 on 2026-11-17 at 14:45:47 UTC, its archive's timer at 14:45:46.**
`btc-pairbook.service` ran `/root/btc-pairbook-svc/tz26-nesting-b3-capture.py`, `caed70d9…`, `commit.txt` `e8b46a8…`,
under `/root/tz04a-env`, from 2026-10-10 19:30:06 UTC; its stop K-26. For each window `T` it fetched the two documents
from `T+545`, streamed the CLOB market websocket for the four tokens from `T+595` to `T+905` — every frame one line,
verbatim, with its receive stamps, in `<T>/stream.jsonl.gz`, `stream.1.jsonl.gz` and on for a second process — kept
the chain book's seven checkpoints in `books.jsonl.gz`, and wrote `window.json` at `T+910`. **Its bounds**, its code's:
no stream below `4,500,000,000` bytes free or once the stream files reach `8,000,000,000`, summed once at a process's
start (§7 item 106); a window's stream cut at `100,000,000`; a halt, exit `1`, below `2,200,000,000` free or past
`200,000,000` bytes one process writes outside its streams. **Its archive**, `btc-pairbook-archive.timer` and the
oneshot `btc-pairbook-archive.service`, code `/root/btc-pairbook-archive-svc/` at `d8194fd`, state
`/var/lib/btc-pairbook-archive/` — its ledger and each run's records under `runs/<A>/`, `32,154,911` bytes — moved the
stream files of closed windows to one Release a run on `pairbook-streams-<A>`, each proved by the Release's digest and
a full anonymous download before its removal, every request inside the pair book's idle stretch, seconds 15 to 590 of
a window, and restarted the pair book once a run. **Its last run**, `A` `1794925184`, TZ-46's B-PAIR-OFF: the 46
stream files of `1794883500` … `1794924000`, `1,151,737,742` bytes, to Release `448733841`. **Its residual:** the
windows `1794924900` and `1794925800`, `42,468,017` bytes of stream, stay unarchived in its store, `146,635,542` bytes
by `du -sb` at TZ-46's close. Its code, its archive's code and state and its store are kept as data (§3).

**Reserved from its first byte, on Tier C's terms — on the host and in every Release asset made from it:** no TZ but
one that scores it extracts a price, size, side, book hash or outcome from a body stored under `/var/lib/btc-pairbook/`
or from such an asset, and no other report prints one; `window.json`, `runtime.jsonl` and `service.log` carry counts,
times and token ids and are excepted. A file's bytes and SHA-256 are not its content: the archive hashed and moved the
stream files and decompressed none. **What has been read** is §5's table: every window after `1793013300` is unread,
and so are the 34 windows `1792723500` … `1792753200`. **A TZ that runs it again** removes `OnActiveSec` from its
archive's timer before enabling it (§7 item 166), lets the next set take the two residual windows, and names the
question that needs the capture: every track that read it is closed (CANON PART II).

### 2.6 The reward book — L0's and L1's capture, running since 2026-10-28 11:30:16 UTC; its streams archived every three hours since 2026-11-17

**The process:** `btc-rewardbook.service`, pid `1556307`, `NRestarts` `0`, active since 2026-11-14 06:11:44 UTC — the
package manager's restart (§7 item 176) — running `/root/btc-rewardbook-svc/tz33-reward-book-capture.py`,
`a276bbb9…`, `commit.txt` `2dcd70e…`, under `/root/tz04a-env`; its stop K-33,
`systemctl disable --now btc-rewardbook.service`.

**Each UTC day `D`** it selects 150 reward markets by TZ-33 §1's rule, from `D0 − 900` and again 60 s after a failed
attempt: the venue's reward listing ranked by daily rate, each candidate's gamma document — an end at least 15 days
after `D0`, no game, no event starting or ending in `[D0 − 1 day, D0 + 2 days)` — and its CLOB document — open,
accepting orders, two tokens, no delay, and none of 31 tags of sports and esports, crypto assets, stocks, commodities
and currencies, and the weather. **Each 900-s slot `S`** it streams the CLOB market websocket for both tokens of every
member from `S − 5` to `S + 905` — consecutive slots overlap by 10 s, so the stream has no idle stretch — and polls
each member's reward document three times, from `S + 30`, `S + 330` and `S + 630`, each round spread over 270 s;
`slot.json` at `S + 910`. **Its store**, under `/var/lib/btc-rewardbook/<D0>/`: `<S>.<k>.stream.jsonl.gz`, one gzip
member with a sync flush at least every 10 s, one line a frame — `recv_ns`, `mono_ns` and `raw` — and one a session
event; `<S>.<k>.rewards.jsonl.gz`, one line a poll with the reply verbatim; `<S>.<k>.slot.json`; and a day's
`select.<a>.replies.jsonl.gz` and `select.<a>.json`; in the root `runtime.jsonl`, `service.pid` and `service.log`. `k` is
`1` and on for a second process in one slot. `367,704,114` bytes by `du -sb` at TZ-46's close.

**Its bounds** (`research/tz33-reward-book-capture.py` lines 189 to 193): no stream opens for a slot below
`7,300,000,000` bytes free (`STREAM_FLOOR`) or once the stream files sum to `4,000,000,000` (`STREAM_CAP`) — **summed
from their directory entries at every slot's decision, so a file removed lowers it at the next slot without a restart**;
a slot's stream is cut at `100,000,000` stored bytes; and it halts, exit `1`, below `2,200,000,000` free at its start, a
slot's start or a selection (`RESOURCE_FLOOR`), or past `1,000,000,000` bytes one process writes outside its streams
(`WRITE_CAP`) — **a halt is not restarted** (`RestartPreventExitStatus=1 2 3`; §7 item 178).

**Its archive — every three hours since TZ-46.** `btc-rewardbook-archive.timer`, `OnCalendar=*-*-* 01/3:30:20 UTC`,
eight elapses a day from 01:30:20, `AccuracySec=1s`, **no `OnActiveSec`**, so no reload starts a run, installed and
restarted at 16:05:49 UTC on 2026-11-17; the oneshot `btc-rewardbook-archive.service`, code
`/root/btc-rewardbook-archive-svc/` at `6a61525`, state `/var/lib/btc-rewardbook-archive/` — its ledger and each run's
records under `runs/<A>/`, `6,032,107` bytes. A run takes every stream file of every slot whose `slot.json` was due at
least 60 s before its start, at most 400, uploads them to one Release on the lightweight tag `rewardbook-streams-<A>`,
one asset `<D0>-<S>.<k>.stream.jsonl.gz` a file, proves each by the Release's own digest and a full anonymous download,
hashes each again and removes it — every request and every removal inside the pair book's idle stretch by the clock,
every removal while the reward book is quiet — and restarts nothing: the store's sum is read live at every slot.
**A run at `hh:30:20` takes the slots to `hh:00`, so the store between two runs holds at most fourteen slots — `PEAK`,
`445,535,636` bytes at the heaviest slot of L0's eight days, `31,823,974` [modelled]** — and a deferred run costs three
hours of the store. Its first run on this calendar, `1794933020` at 16:30:20 UTC, took 5 files, `71,537,680` bytes, to
Release `448903582`, the reward book streaming on (TZ-46 report); **each of the twenty-four elapses since, to 16:30:20 UTC on
2026-11-20, made its tag, `1794943820` … `1795192220`, 10,800 s apart** (`git ls-remote`, the Architect, 2026-11-20
17:04 UTC). **Every run makes one Release and one tag** (§7
item 177); its stop K-34, `systemctl disable --now btc-rewardbook-archive.timer`; a halt is cleared only by a TZ that
appends a `clear` record. A member day's asset is `<D0>-<S>.<k>.stream.jsonl.gz` under the tag of the archive's first
run at or after `S + 970`.

**Reserved from its first byte** (TZ-33 §1) — **on the host and in every Release asset made from it — and by day.**
The days to 2026-11-13 are read: L0's nine candidates of 2026-10-31 to 2026-11-08 and TZ-45's five members of
2026-11-09 to 2026-11-13, beside the Architect's explorations (§5); they are an exploration's from now on and can gate
nothing (CANON PART VI). **Every day from 2026-11-14, `D0` at or above `1794614400`, stays reserved:** until a committed
TZ fixes a gate on it, no TZ and no session of the Architect extracts a price, size, side, book hash, rate,
competitiveness or outcome from a body stored under `/var/lib/btc-rewardbook/` for such a day or from an asset of one,
and no report prints one. A deployment proof reads of a stored reply its status, byte count, SHA-256 and times, whether
its body parses, and of a reward reply its shape and its row's `condition_id`; of a stream frame its JSON shape, its
event types, its token ids and the venue's `timestamp`; of a selection its counts, its verdicts and its condition and
token ids — `select.<a>.json` also carries each member's rate, minimum size and maximum spread, which no mode prints.
`slot.json`, `runtime.jsonl` and `service.log` carry counts, times and token ids and are excepted. Nothing of it enters
git history. **Every TZ after TZ-33 reads `du -sb /var/lib/btc-rewardbook` beside `df`.**

**Incidents measured, which a walk over its days absorbs** (CANON hard rule 8): on 2026-11-06 slot `1793949300` held no
frame for `251.8` s while the unit's own `PING` went out every 10 s, then the socket closed and reopened within 1 s — a
stall of the venue's socket or of the path to it (TZ-41 report); on 2026-11-11 the slot of 02:00 UTC ended 57 s early
(TZ-45 report); from 21:15 UTC on 2026-11-13 eleven slots opened no stream on the disk's floor (§7 item 170); and on
2026-11-14 at 06:11:44 UTC the package manager's restart split a slot across two processes (§7 item 176).

**L0 on it** (§4, §5): TZ-43 read the first rule UNDECIDABLE on 2026-10-31 to 2026-11-08 (its inputs public in
`tz-44-l0-inputs`, re-derived by the Architect, §7 item 162); TZ-45 read **rule W EARN** on 2026-11-09 to 2026-11-13,
each day replayed over its longest run of whole slots, its inputs public in `tz-45-l0-rule-w-inputs`, re-derived by the
Architect two ways. **Rule W, as TZ-45 §1 fixed it, is L1's rule:** on each market of the day's selection whose
minimum size is at most 20 shares, and while the last poll's competitiveness figure is at most `1`: where the
displayed touch `bb`, `ba` leaves room — `ba − bb ≥ w + 2` ticks, `w` the largest multiple of the tick that is at most
`0.9` of twice the maximum spread and below it — a bid at `tb`, `(bb + ba − w) / 2` floored to the tick grid, and an
ask at `ta = tb + w`, each of the minimum size, placed only where neither stands more than `0.10` inside the touch
(`tb − bb ≤ 0.10` and `ba − ta ≤ 0.10`), and cancelled otherwise; a position cap of one such size; post-only; a 50 ms
one-way latency; nothing where the touch is narrower; and the market left for the rest of the day from the first
served poll whose row carries other terms than its selection's (§7 item 155). **The replay that read EARN proves no
income** (CANON PART II): it holds the book fixed while our quote stands in it.

### 2.7 The advisor's record — `/var/lib/adv3-bot/`, written by `adv3-bot.service` since 2026-10-29 14:38:10 UTC

**The process:** pid `1555970`, `NRestarts` `0`, active since 2026-11-14 06:11:41 UTC — the package manager's restart
— running `/root/adv3-bot-svc/adv3-bot.py --serve`, TZ-42's code: `adv3.py` `81ef0112…`, `adv3-bot.py` `c3d9fff5…`,
`commit.txt` `4e6db2d…`, under `/root/tz04a-env`; its stop K-35, `systemctl disable --now adv3-bot.service`. Its
rollback is `bot.before`, `9e622daf…`, and `commit.before` in the forensic store (§3); a rollback moves the
registry's two files aside.

**What it reads and writes.** It reads `fapi.binance.com`'s closed daily, 5-minute and 1-minute candles, funding,
premium index and funding intervals of the Boss's 42 perpetuals, and the Boss's one pinned Telegram chat; it holds no
exchange key. It writes only under `/var/lib/adv3-bot/`: `offset`, the last Telegram update answered; `daily-sent`,
read by no code since TZ-39; `check-done`, the last of the two daily checks done; `registry.jsonl` and
`registry-state.json`, the registry of its STRONG signals; `journal.jsonl`, one record a message sent — kinds `check`,
`request`, `registry`, `ranking` and `assess`, and the `daily` and `alloc` records of earlier code, which the
registry's seed alone reads; and `service.log`. The token and the pinned chat are under `/etc/adv3-bot/` — `token`, the
Boss's, and `chat-id`, both `600`, root's — which no command prints, hashes or copies.

**What it does** (CANON PART VII, the Boss's model of 2026-11-05): two checks a day by its own loop, **00:10 and 15:07
UTC** (04:10 and 19:07 in Batumi), each walking every open signal before opening the model's new ones, loud only for a
new signal or an end and one quiet line otherwise; the views «сигнал», «реестр», «рейтинг [N]», «оценка» and
«помощь». **The registry** — `registry.jsonl`, append-only, one event a line, `seed`, `open`, `fill`, `target`,
`stop`, `exit` or `expire`, each with its place `n`, its instant and `prev`, the SHA-256 of the line before it, `0` ×
64 for the first; `registry-state.json`, written in one rename — holds every signal from its issue to its end, walked on
5-minute candles and its first minutes on 1-minute ones; it was seeded on 2026-11-05 at 20:36:06 UTC with 10 events
and 4 legacy signals. **It is the bot's model at `200,000` USDT, not the Boss's account and not a measurement: it moves
no rung.** The journal is a record of what was sent, never the forward record's source: CANON PART VII re-derives the
rule's trades from Binance's archive, whose daily files of 2026-10-28 are absent (§7 items 135 and 147).

**Unread since TZ-42's replay of 2026-11-05:** no report has read the bot's `check` records or its registry since —
the next advisor TZ's host gate reads them (§7 item 161).

---

## 3. Code

What each file is, and what it alone implements; why a file is `frozen`, and the functions a later TZ imports from
it and never writes again, are §0's notes beneath the table. How a file came to be is its TZ's report (§1).

| file | role |
|---|---|
| `research/twap-divergence.py` | the collector of §2.1's observation set; the only implementation of the superseded `p_interval` arithmetic |
| `research/selftest-twap-divergence.py` | its analytic self-tests |
| `research/tz02-distribution.py` | aggregation over the observation set; reads the Parquet columns only (§7 item 1) |
| `research/pfair.py` | **the pricer — the only implementation of the CANON §1.2 model, in any language** — and the quantities it is fed: the merged stream, the time-weighted mean, the one-second grid, the realised-sigma estimator, `settlement_mean`; `SD_SCALE` and `corrected_sd`; the Student link `log_t_cdf`, `t_cdf`, `student_sd`, `p_fair_student` and the tables `ADMIT`, `LINK_NU`, `LINK_SCALE`, one literal per `tau`, an unmeasured `tau` raising; `log_phi`. Its reader is `analyze.py`'s |
| `research/selftest-pfair.py` | its 116 analytic self-tests, every fixed expectation at a realistic `K` |
| `research/tz06-calibration.py` | the Phase 1 pipeline: set formation `scoring_set` and `build`, with `after` and `need`, the gate tables; carries no formula (§7 item 28) |
| `research/tz07a-variance-time.py` | the variance–time instrument and its disconnect rule |
| `research/tz07b-settlement-dispersion.py` | the settlement-dispersion instrument: `Y(a, tau)` and the `Λ` table `pfair.py` carries |
| `research/tz08a-out-of-sample.py` | the out-of-sample driver; no threshold of its own |
| `research/tz09-disk-inventory.py` | the disk inventory; it cannot delete |
| `research/tz10b-sigma-or-link.py` | the sigma-or-link instrument, and helpers later instruments import: `free_bytes`, `recorder_pids`, `newest_start`, `read_set`, `grid_of`, `sigma_hat_of`, `m2_labels` |
| `research/tz11a-student-link.py` | the Student-link instrument: `the_sets`, `walk_member`, `fit_student`, `checkpoint_row` |
| `research/tz12-sized-gate.py` | the sized gate itself and `SIGMA_LOG_NU`, `SIGMA_LOG_NU_CENSORED` |
| `research/tz13-sized-gate-test3.py` | the sized gate applied once, to test 3 |
| `research/tz14-quote-inventory.py` | the quote machinery every later TZ imports: `the_set`, `quote_lines`, `book_of`, `best_of`, `touch_of`, `documents`, and **`fee_pp`, the only implementation of CANON §1.1's taker fee**. **Importing it** writes three thread-count environment variables, loads `tz12-sized-gate.py`, and installs an audit hook on every open under the capture root that cannot be removed |
| `research/tz15-phase2-gate.py` | Phase 2's first gate; `pb_upper`, `crit`, `select` |
| `research/tz16a-phase2-decisive-gate.py` | Phase 2's decisive look and its arithmetic: `up`, `low`, `critical_upper`, `critical_lower`, `look_constants`, `read_look`, `dependence`, `residual_dependence`, `interlock_reading` |
| `research/tz17-settlement-chain.py` | the settlement chain's fetch, the first committed request the venue's edge serves (`User-Agent` `btc-5m-twap-tz17`) |
| `research/tz18a-chainbook-capture.py` | the chain book: instrument and service code, `build_request` with `btc-5m-twap-tz18a` |
| `research/tz20-capture-under-systemd.py` | TZ-20's deployment proof of both units |
| `research/tz21-recorder-memory.py` | TZ-21's proof that the bounded recorder serves every slice the old one served |
| `research/tz23-maker-m0.py` | M0's instrument: `qualify`, `candidates`, `maker_terms`, `rebate`, `aggregate`, `gate_constants`, `reading` |
| `research/tz24-nesting-b2.py` | B2's instrument: `pairs_of`, `payoff`, `costs`, `classify`, `reading_of`, `theta1`, `power` |
| `research/tz26-nesting-b3-capture.py` | the pair book: `serve`, the unit's code; `build_request` with `btc-5m-twap-tz26`; the store's names, `stream_bytes_total`, `stream_off_reason` |
| `research/tz27-pairbook-archive.py` | the archive's functions both timers run: `inventory`, `upload_set`, `verify_release`, `delete_set`, `restart_reading`, `counter_reading`, `resume_decision`; `credential()` falls back to `gh auth token` where the remote URL carries none (§7 item 114) |
| `research/tz28-pairbook-archive-timer.py` | `run`, the pair book's archive's service code, loading `tz27` by SHA-256; `idle_wait`, the ledger and the resume rule, both archives' |
| `research/tz29-maker-m0-second-look.py` | M0's second look |
| `research/tz30-nesting-b3-measure.py` | B3's measurement: the replay of a window's streams at venue time |
| `research/tz31-who-earns.py` | W0's instrument: the makers' rows of a market and the named groups' sums |
| `research/tz32-our-quoting.py` | W1's instrument: a five-minute leg replayed with our quotes queued, filled, refused and cancelled under nine variants |
| `research/tz33-reward-book-capture.py` | the reward book: `serve`, the unit's code, refusing any other command line, an untuned glibc or a second instance; `run_rule` through `LiveFetch` or `StoredFetch`; the slot schedule; the store's layout and bounds; `build_request` with `btc-5m-twap-tz33` |
| `research/tz34-rewardbook-archive-timer.py` | `run`, the reward book's archive's service code, loading `tz28` and through it `tz27` by SHA-256; `inventory`, `quiet`, `removal_wait`, `remove_set` |
| `research/tz35-advisor-deploy.py` | TZ-35's checker: `number`, CANON hard rule 2's check, and its readings of the advisor's unit |
| `research/tz36-advisor-trust.py`, `research/tz37-capital-allocation.py`, `research/tz39-advisor-checks.py`, `research/tz40-advisor-strong.py`, `research/tz42-advisor-registry.py` | the advisor's deployments' checkers, each its TZ's readings of the bot (§0's notes) |
| `research/tz38-adv3-pit-validation.py` | the PIT and market records' readings: `admissible`, `rule_pass`, `strong_pass`, `monthly`, `monthly_sum`, `read_series`, `power` (CANON PART VII) |
| `research/tz43-l0-our-quote.py` | L0's set, replay and reading: `slot_problem`, `members_of`, `polls_of`, `Day`, `day_money`, `l0_reading` |
| `research/tz44-l0-inputs-release.py` | TZ-44's instrument: L0's inputs packed and published, `pack_day` |
| `research/tz45-l0-rule-w.py` | rule W's replay and reading (§2.6), over TZ-43's engine |
| `research/tz46-capture-room.py` | TZ-46's instrument: `room_reading`, `index_assets`, `plan_rows`, `timer_checks`, `trigger_reading`, `next_verdict`, `pair_reading`, `still_reading`; its `MEM_FLOOR` `133,073,162` (§6, memory) |
| `engine/l1-bot.py` | **L1's unit**: `serve`, `ready`, `prove`, `clear-stop`, `status`, `unit`, `selftest`, `sdk-selftest`; rule W's targets and the day's selection taken by name from `tz45-l0-rule-w.py` and `tz33-reward-book-capture.py` beside it, by their SHA-256 (`load_frozen`); its orders known by the wallet's open orders, never by a read by id |
| `research/tz53-l1-account.py` | TZ-53's checker: TZ-52's instrument under TZ-53's names — its deployment checks on both hosts |
| `guard/liq-guard.py` | **the liquidation guard, its second version** (CANON PART VII; TZ-55): `secrets`, `find-chat`, `prove`, `serve`, `status`, `scan`, `selftest`; the Boss's USDⓈ-M positions read every `5` s through a Binance key that can read alone, its permissions read at every start and every `6` h; **liquidation** — three stages of his, a high-priority notice and two emergency calls, each with the margin to his target, `5`% by default, and a live Telegram card; **his work** — an acknowledged call or «✋ Я в деле» silences that position's calls for `10` min, margin added seen and confirmed, a call again at the timeout and at the last line; **gains** — a record from `7`% beyond the entry and each next, retreats of a third and a half of the peak, kept in `memory.json`; every message opening with its side's colour and sent through its side's Pushover application; its own blindness and a dead-man's ping; standard library only, every connection IPv4; 127 self-test checks |
| `research/tz54-liq-guard.py`, `research/tz55-liq-guard-v2.py` | TZ-54's and TZ-55's checkers: TZ-53's checker under their names — their capture-host modes alone |
| `research/tz49-live-host.py` | TZ-49's instrument: the live host's readings — `geo_reading`, `v6_state`, `spec_reading`, `live_gate`, `swap_reading`, `log_reading`, `ssh_reading`, `lat_reading` — and the audit hook's IPv4 rules, `policy`; the texts of the live host's three drop-ins; its `MEM_FLOOR` `72,439,812` (§6, memory) |
| `research/recorder/recorder.py` | the live capture, Tier A and Tier C in one process; since `0f6c9045…` it keeps two hours of runtime records (§7 item 90) |
| `research/recorder/config.py` | every constant the capture uses, each traced to the TZ that fixed it |
| `research/recorder/manifest.py` | the per-interval manifest, a pure function of the interval directory |
| `research/recorder/analyze.py` | the TZ-04b analyzer and the only stream reader: `reports`, `last_at_or_before`, `first_at_or_after`, `venue`, `published_equal`, `scoring_set` (§7 item 17) |
| `research/recorder/probe.py` | the Tier B order-book probe, run once |
| `research/recorder/selftest.py` | the recorder's 115 self-tests |
| `advisor/RULE-ADV-3.txt` | ADV-3's text, frozen 2026-10-28 16:14 UTC, its SHA-256 carried as `RULE` in `adv3.py` |
| `advisor/adv3.py` | **ADV-3's only implementation**, standard library only: the candles from Binance's archive or `fapi.binance.com`, the signal, `z`, TOP-3, STRONG, the trades and their R; the report, the cards and the message; `--history` and `--compare` |
| `advisor/adv3-bot.py` | ADV-3's Telegram side and the unit's code: `--serve`, `--probe`, `--find-chat`, `--hello`; the registry, the model and its overrides, the five views, the two checks; 135 self-test checks |
| `advisor/selftest-adv3.py` | ADV-3's self-tests, no network |
| `.gitignore` | `research/out/**` is ignored but `twap-divergence-summary.md` and `twap-divergence-contamination.md` |

**`research/tz18-chainbook-capture.py` is not on `main` and never will be:** PR #18's head `8caa0b4`, closed
unmerged, held by hash in `/root/btc-forensics/` (§7 item 77). **`research/tz41-l0-our-quote.py`** is PR #42's head
`cca1109`, closed unmerged. **`research/tz50-l1-account.py`** is PR #48's head `0774d7e`, never merged — its `Tty` opens
the terminal `"r+"` (§7 item 189) — and TZ-51 closes the pull request unmerged.

### The units

| unit | file on `main` | state on the host | runs | stop |
|---|---|---|---|---|
| `btc-recorder.service` | `deploy/systemd/btc-recorder.service` | **enabled, running** | `/root/tz04a-env/venv/bin/python -B -u recorder.py` in `/root/btc-recorder-svc/research/recorder`; `Restart=always`, `RestartSec=5`, `RestartPreventExitStatus=0`, `StartLimitIntervalSec=3600`, `StartLimitBurst=5`, `MemoryMax=512M`, output to `recorder.log` | K-20R |
| `btc-chainbook.service` | `deploy/systemd/btc-chainbook.service` | disabled, stopped since 2026-10-10 | `/root/tz01-env/venv/bin/python -B -u /root/tz18a-svc/tz18a-chainbook-capture.py --serve`; `RestartPreventExitStatus=1 2 3`, `MemoryMax=192M` | K-20C |
| `btc-pairbook.service` | `deploy/systemd/btc-pairbook.service` | **disabled, stopped since 2026-11-17 14:45:47 UTC** | `/root/tz04a-env/venv/bin/python -B -u /root/btc-pairbook-svc/tz26-nesting-b3-capture.py serve`; `Restart=always`, `RestartPreventExitStatus=1 2 3`, `MemoryMax=128M` | K-26 |
| `btc-pairbook-archive.timer` and `.service` | `deploy/systemd/btc-pairbook-archive.{timer,service}` | **the timer disabled and stopped since 2026-11-17 14:45:46 UTC**, its file keeping `OnCalendar=*-*-* 03:00:20 UTC` and `OnActiveSec=600` | the service a oneshot, `Restart=no`, `TimeoutStartSec=21600`, `Nice=19`, `MemoryMax=128M`, in `/var/lib/btc-pairbook-archive` | K-28 |
| `btc-rewardbook.service` | `deploy/systemd/btc-rewardbook.service` | **enabled, running** | `/root/tz04a-env/venv/bin/python -B -u /root/btc-rewardbook-svc/tz33-reward-book-capture.py serve`; `Restart=always`, `RestartSec=5`, `RestartPreventExitStatus=1 2 3`, `StartLimitIntervalSec=3600`, `StartLimitBurst=5`, `Nice=10`, `MemoryMax=192M` | K-33 |
| `btc-rewardbook-archive.timer` and `.service` | `deploy/systemd/btc-rewardbook-archive.{timer,service}` | **the timer enabled**, TZ-46's file since 16:05:49 UTC on 2026-11-17: `OnCalendar=*-*-* 01/3:30:20 UTC`, `AccuracySec=1s`, no `OnActiveSec` | the service a oneshot, `Restart=no`, `TimeoutStartSec=21600`, `Nice=19`, `MemoryMax=128M`, in `/var/lib/btc-rewardbook-archive` | K-34 |
| `adv3-bot.service` | `deploy/systemd/adv3-bot.service` | **enabled, running** | `/root/tz04a-env/venv/bin/python -B -u /root/adv3-bot-svc/adv3-bot.py --serve` in `/root/adv3-bot-svc`; `Restart=always`, `RestartSec=30`, `RestartPreventExitStatus=3 4`, `StartLimitIntervalSec=3600`, `StartLimitBurst=5`, `Nice=10`, `MemoryMax=128M`, `NoNewPrivileges=yes`, `PrivateTmp=yes`, `ProtectSystem=strict` with `ReadWritePaths=/var/lib/adv3-bot` | K-35 |
| `l1-bot.service` — **on the live host** | `deploy/systemd/l1-bot.service` | **enabled, stopped since 01:45 UTC on 2026-11-22 on its own loss limit**, its stop record standing, so a start exits `3` (CANON §1.5; read by the Architect from the venue's public trades and the wallet's positions, the unit's journal not read; §7 item 200); it ran from 08:37:35 UTC on 2026-11-21 (TZ-53) | `/root/l1-env/bin/python -B -u /root/l1-bot-svc/l1-bot.py serve` in `/root/l1-bot-svc`; `Restart=on-failure`, `RestartSec=30`, `RestartPreventExitStatus=2 3`, `StartLimitIntervalSec=3600`, `StartLimitBurst=5`, `MemoryMax=384M`, `NoNewPrivileges=yes`, `PrivateTmp=yes`, `ProtectSystem=strict` with `ReadWritePaths=/var/lib/l1-bot`; output to `/var/lib/l1-bot/service.log` | «Стоп» in its Telegram chat; `systemctl disable --now`; the session key's revocation, B-REVOKE (TZ-51 §4.11) |
| `liq-guard.service` | `deploy/systemd/liq-guard.service` | **enabled, running — the second version** since 10:01:40 UTC on 2026-11-22, MainPID `2825760` and `NRestarts` `0` at TZ-55's close; the first version ran from 18:30:43 UTC on 2026-11-21 to TZ-55's stop at 09:42:46 UTC (§7 item 195) | `/root/tz04a-env/venv/bin/python -B -u /root/liq-guard-svc/liq-guard.py serve` in `/root/liq-guard-svc`; `Type=notify`, `WatchdogSec=300`, `TimeoutStartSec=120`, `Restart=always`, `RestartSec=15`, `RestartPreventExitStatus=2`, `StartLimitIntervalSec=0`, `MemoryMax=96M`, `UMask=0077`, `NoNewPrivileges=yes`, `PrivateTmp=yes`, `ProtectSystem=strict` with `ReadWritePaths=/var/lib/liq-guard`; output to `/var/lib/liq-guard/service.log`, `0600` | `systemctl disable --now`; the key's deletion in Binance's API Management |

Every unit file is installed byte for byte under `/etc/systemd/system/`, as every host gate asserts with `cmp`; each
stop is `systemctl disable --now <unit>`, and an archive's stop lets a run in progress end. **A TZ that restarts or
stops a capture, or reads or changes its store, first reads `systemctl is-active` of that capture's archive service
and works only while it reads `inactive`** — the pair book's rule since TZ-28, kept for either archive by §7 item 166.

### The trees on the host

**Data, never scratch — no TZ removes or edits one but the TZ that names it with its reason:**

| tree | what it is |
|---|---|
| `/root/btc-recorder-svc` | the detached worktree the recorder's unit runs, at `e3975b5`; no `git worktree remove` touches it |
| `/root/tz18a-svc/` | the chain book's code, `tz18a-chainbook-capture.py` `e9cb9b47…` |
| `/root/btc-pairbook-svc/` | the pair book's code, `tz26-nesting-b3-capture.py` `caed70d9…`, `commit.txt` `e8b46a8…` |
| `/root/btc-pairbook-archive-svc/`, `/var/lib/btc-pairbook-archive/` | the pair book's archive's code — its file `46a019d6…`, TZ-27's `2cba96bc…`, `commit.txt` `d8194fd…` — and its state |
| `/root/btc-rewardbook-svc/` | the reward book's code, `tz33-reward-book-capture.py` `a276bbb9…`, `commit.txt` `2dcd70e…` |
| `/root/btc-rewardbook-archive-svc/`, `/var/lib/btc-rewardbook-archive/` | the reward book's archive's code — its file `1d8aa514…`, TZ-28's `46a019d6…`, TZ-27's `2cba96bc…`, `commit.txt` `6a61525…` — and its state |
| `/root/adv3-bot-svc/`, `/var/lib/adv3-bot/`, `/etc/adv3-bot/` | the advisor's code, record and credentials (§2.7) |
| `/root/liq-guard-svc/`, `/var/lib/liq-guard/`, `/etc/liq-guard/` | the liquidation guard's code, record and credentials (§3, the units): `/root/liq-guard-svc/` `0700`, the second version's `liq-guard.py` and its unit file's copy, each `0600`; `/var/lib/liq-guard/` `0700` — `prove.json`, `state.json`, `memory.json` — the gains' memory, a position's prices among them — `journal/` and `service.log`, each `0600`; `/etc/liq-guard/` `0700` — `binance-key`, `binance-secret`, `pushover-user`, `pushover-token`, `pushover-long`, `pushover-short`, `tg-token`, `tg-chat` and `hc-url`, each `0600`, root's |
| `/var/lib/btc-recorder/`, `/var/lib/btc-chainbook/`, `/var/lib/btc-pairbook/`, `/var/lib/btc-rewardbook/` | the four stores (§2) |
| `/root/tz01-env/` | the research interpreter, Python 3.12.3 with `numpy` 2.5.3 (§6, language) |
| `/root/tz04a-env/` | the units' interpreter, Python 3.12.3 with `websockets` 17.1 |
| `/root/btc-forensics/` | **the forensic store**: every file a committed report names by hash that no public Release holds, and each TZ's state and logs, kept by name — `2,744` files since TZ-52's §9 (CANON hard rule 15; §7 item 167) |
| `/root/.ssh/live-host` and its `.pub`, the `Host live-host` block of `/root/.ssh/config`, its pinned key in `/root/.ssh/known_hosts` | **the Executor's access to the live host**, made by TZ-47 and kept: the alias alone carries the live host's address, which no file of the repository and no log holds (§6, live host) |

**The primary checkout `/root/btc-5m-twap` carries no running code.** **On the live host, data and never scratch —
L1's:** `/root/l1-env/`, `/etc/l1-bot/`, `/root/l1-bot-svc/` and `/var/lib/l1-bot/` (§6, live host); the empty
`/tmp/l1-bot-selftest/` the engine's self-tests left is the next live-host TZ's to remove (§7 item 193). **The worktrees registered at TZ-52's end are
two:** the primary checkout and `/root/btc-recorder-svc`. **Session directories** under
`/tmp/claude-0/-root-btc-5m-twap/`, as TZ-54's `scratch` read them: its own `39c2d6bf-…`; two live beside it,
`0736470b-…` and `6f0f41a7-…`, made by the `claude` processes started at 18:51 UTC on 2026-11-20; and six earlier, each
reclaimed and gone by its B-RECLAIM-SCRATCH (TZ-54 report §2.5) — each live one the next TZ's to reclaim once no
running `claude` process made it. The remote-control `claude` processes, under tmux session `crypto-rc`
— `Crypto Auto VPS` in `/root/crypto-auto` and `BTC-5M-TWAP-VPS`, which spawns the Executor's sessions — are no TZ's,
and no TZ touches them (§6, harness). Outputs go to `research/out/**`, git-ignored.

---

## 4. What is validated, and by what

Each claim stands as stated and for nothing more; its numbers, sets and re-derivations are in the report named.
Phase 0 and Phase 1 can only disqualify; nothing here is an edge (CANON §1.5).

| claim | report | state |
|---|---|---|
| the venue settles on the 60-second trailing-TWAP feed, the close's reading against the open's; the interval-average and the pre-August snapshot readings are wrong, 175 and 181 of 200 | TZ-04b, TZ-06 | stands — the only artifact validated against the venue's settlement |
| the price to beat is the feed's first reading at or after the open, with a ~1% failure rate every later result carries | TZ-04b, TZ-06 | stands |
| the causal reading is causal, by perturbation | TZ-01a, TZ-06, TZ-07a | stands |
| the oracle feed supports reconstructing the settlement average; the pipeline reproduces | TZ-06, TZ-07a, TZ-07b | stands |
| the feed's variance grows faster than the lag; the settlement quantity's dispersion, `Λ`, measured on the variable `sd` divides | TZ-07a, TZ-07b | stands as measurements of the feed; TZ-07a's correction superseded by TZ-07b |
| the normal link: not disqualified by TZ-06's gate; G1 and G2 pass out of sample; **G3 fails at `tau` 60 and 30** | TZ-06, TZ-08a | Phase 1 answers no for the normal link |
| the settlement residual is not Gaussian, less so the smaller `tau`; the tail is not a lagging `sigma`, survives conditioning on the realised scale error, is not forecastable from causal inputs, and sits in the low-`sigma_hat` deciles | TZ-08a, TZ-10b | stands; `g` withdrawn as a reading |
| the residual is Student-shaped, and inside the domain the shape transfers from weekday to weekday; the Student pricer closed by its own unsized gate | TZ-11a | stands; not re-judged |
| the gate's own error rates, measured exactly; `SIGMA_LOG_NU` | TZ-12 | stands |
| **the Student pricer is NOT DISQUALIFIED at `tau` 240, 180, 120, 90 and 60 under the sized gate**, undecidable at 30 and 10 | TZ-13 | stands — which confirms nothing |
| Tier C captures the book at seven checkpoints without loss; the reply puts the worst price first; the book empties toward the close; the executable touch is the quoted one at the minimum size `5`; the tick falls to `0.001` in the wings; the two tokens are one book; the fee schedule is CANON §1.1's | TZ-05a, TZ-14 | stands as facts of the venue and the capture |
| Phase 2's first gate UNDECIDABLE at five `tau`; the outcomes tracked the market's prices rather than the pricer's | TZ-15 | stands; a finding, not a reading |
| **Phase 2: NO EDGE at `tau` 180, 120, 90 and 60; UNDECIDABLE at 240**, its second look withdrawn; the market's mid beats the pricer on the Brier score | TZ-16a | stands — Phase 2 closed for the taker |
| the fifteen-minute market opens on the five-minute market's reading and settles on the same chain; the settlement reading at a boundary is one published number, 1,000 of 1,000 by literal | TZ-17, TZ-18 | stands — B0 closed |
| the chain book records both books at one instant, within `28.43` ms; a second capture leaves Tier C intact, and the chain book did at a finer grain, HOLD | TZ-18a, TZ-16a | stands — B1 closed |
| both captures run as systemd system units, outside every session | TZ-20 | stands |
| the recorder's memory was unbounded and is bounded; the bounded recorder serves every slice the old one served | TZ-20, TZ-21 | stands |
| M0's first look UNDECIDABLE; **over both looks NO EARN** — the makers kept under half a tick a share inside `[T0, T0 + 240)`, rebate included | TZ-23, TZ-29 | stands — the maker track closed for its window |
| the maker rebate is 20% of the taker fee, measured against the venue's payouts | TZ-29 | stands as a measurement of the venue's terms |
| **B2: the nested pair broke the containment on stored books after both fees at 7 of 1,079 windows** | TZ-24 | stands — VIOLATION |
| the pair book streams the four books of each nested pair as a system unit; its streams leave the host byte for byte, daily, unattended | TZ-26, TZ-27, TZ-28 | stood while it ran; stopped by TZ-46 |
| **B3: a taker cannot capture the violations through the venue's delay** | TZ-30 | stands — NO CAPTURE, the backup track closed |
| **W0: the ten named makers kept earning on markets no one had read**, `0.828` c a share | TZ-31 | stands — W-EARN |
| **W1: a quote of ours at the touch keeps under half a tick a share even first in every queue**, all of it rebate, and loses behind it | TZ-32 | stands — W1-NO-EARN, the W track closed |
| the reward book streams the books and trades of each day's 150 reward markets and polls their reward documents, as a system unit | TZ-33 | stands |
| the reward book's streams leave the host by its archive's timer; every three hours since TZ-46 | TZ-34, TZ-46 | stands |
| **L0's first rule UNDECIDABLE** on 2026-10-31 to 2026-11-08; its inputs public, its money re-derived by the Architect, 24 of 24 variant-days | TZ-43, TZ-44 | stands — closes nothing, admits nothing |
| **L0's rule W EARN** on 2026-11-09 to 2026-11-13, every day's least `28.7` to `123.4` USDC, re-derived by the Architect two ways from public bytes | TZ-45 | stands — opens L1, proves no income |
| the venue reads the capture host's address `blocked`, `PL` | TZ-44 | stands as a measurement of that address (§6) |
| the capture keeps its room: the pair book stopped, the reward book's archive every three hours, the forensic copies a Release holds removed | TZ-46 | stands; the host's states are its logs, measured and not re-derived (CANON hard rule 16) |
| the live host in Sofia prepared: IPv4 alone in the process and the venue reading its address `BG`, not blocked; root by key alone; its own swap adopted and its journal bounded; a one-way bound of `28.148` ms to the venue's CLOB | TZ-49 | stands; every log of the run is quoted whole in its report — the Architect re-built 32 of them from it to the SHA-256 their forensic copies carry, and re-derived G-LAT from its 605 request lines |
| the advisor's bot runs ADV-3 from its appendix's bytes, as a system unit, in the Boss's one chat; its card, its budget view, its two checks a day, STRONG at every rank, its registry and the Boss's model | TZ-35, TZ-36, TZ-37, TZ-39, TZ-40, TZ-42 | stands for each deployment and its shapes on one day's data (§7 item 161) |
| ADV-3 on every Binance USDⓈ-M USDT perpetual that traded: the rule on the contracts the Boss did not pick, STRONG on random lists | TZ-38 | stands as an exploration that moves no rung (CANON PART VII) |
| the venue's maker-rewards terms are readable from our capture | TZ-07a, TZ-14 | NARROWED: per-market terms only, no daily rate (§6, maker incentives) |
| the TWAP model beats the endpoint model · divergence is abundant · inversions are the rare tail | TZ-02 | WITHDRAWN — all scored against §2.2's labels |

---

## 5. Phase state

The gates and their readings are CANON PART II's; this is where each stands, with its report.

| phase or step | state |
|---|---|
| Phase 0 — the settlement rule | **closed 2026-09-11, yes** — TZ-04b, 200 of 200 |
| Phase 1 — `p_fair` calibrated against true-rule labels | **answered 2026-09-18** — the normal link disqualified at `tau` 60 and 30 (TZ-08a); the Student link not disqualified at `tau` 240 … 60, undecidable at 30 and 10 (TZ-13) |
| Phase 2 — the market price against `p_fair`, executable | **closed for the taker, 2026-10-04** — NO EDGE at `tau` 180, 120, 90, 60, UNDECIDABLE at 240, its second look withdrawn unrun (TZ-16a) |
| Phase 3 — capturable | **reached by the L track alone, and lost there:** L0's rule W read EARN in a replay (TZ-45) and L1's live fills did not keep it (CANON §1.5); the K and H tracks reach it only by their own gates |
| Phase 4 — live, minimum size, fixed loss | **L1 ran and stopped on its fixed loss, 2026-11-22**; the next live step is the K or the H track's, behind its own gate |
| B0, B1, B2, B3 — the nested pair | B0 yes (TZ-17); B1 yes (TZ-18a); B2 VIOLATION (TZ-24); **B3 NO CAPTURE (TZ-30): the backup track is closed** |
| M0, M1, M2 — the makers' pool | **M0 NO EARN over both looks (TZ-23, TZ-29); M1 and M2 do not open** |
| W0, W1, W2 — who earns | W0 W-EARN (TZ-31); **W1 W1-NO-EARN (TZ-32); W2 does not open: the W track is closed** |
| L0 — our quote on reward markets, replayed | first rule UNDECIDABLE (TZ-43); **rule W EARN (TZ-45)** |
| **L1 — live, at minimum size, a fixed loss** | **closed, 2026-11-22 — stopped on its fixed loss.** Rule W live from the live host in Sofia, TZ-53's unit, from 08:37 UTC on 2026-11-21 to 01:45 UTC on 2026-11-22: 17 fills on 8 markets, `−25.25` pUSD at the touch and `−16.1` at the venue's prices, `0.48` of rewards the venue computed and had not paid; better-priced traders took its quotes (CANON §1.5). Its steps before it, each a TZ: the capture's room (TZ-46), the live host (TZ-49), the account and its order path (TZ-50 to TZ-52), the unit (TZ-53). Its measurement against the replay does not run: the live fills answered first |
| L2 — more markets and size | **does not open**: the L track is closed |
| **K0 — the favourite held to settlement, Kalshi and Polymarket** | **opens — TZ-56:** Kalshi's binary markets closing 2026-11-16 to 2026-11-21 and Polymarket's CTF (`v1`) markets ending on the same days and closed by 12:00 UTC on 2026-11-23 (§7 item 203), a two-stage random draw of 5,000 members a venue, read by two exact betting tests a venue at `1/400` each; public data alone, no money; its inputs leave in the Release `tz-56-k0-inputs` (CANON PART II, the K track) |
| K1, K2 — a Kalshi account, then live | behind K0's EARN on Kalshi (CANON PART II) |
| **H0 — taking the quotes that stand far from the traded price** | **opens — TZ-57, after TZ-56:** the reward book's recorded days 2026-11-18 to 2026-11-20, a taking rule and its race fixed before any of the three is read (CANON PART II, the H track) |
| the advisor (CANON PART VII) | Gate H and Gate S NOT DISQUALIFIED, 2026-10-28; delivered by the bot since 2026-10-29 (§2.7); **the rule's forward record read once after the close of 2027-10-28; the PIT and market records after the close of 2027-10-31**; its rating `1/5` |

### What has been read — the sets no later gate may use

A set is "no one has read" only where every artifact that read or printed an outcome of it is outside it (§7 item
96). **A gate fixed after its set was read was not fixed before the data** (CANON PART VI).

| source | read | unread |
|---|---|---|
| the recorder's Tier A and Tier C | the Phase 0 to Phase 2 sets, `T0` `1789033800` … `1790452200` — TZ-04b, TZ-06, TZ-08a, TZ-10b, TZ-11a, TZ-12, TZ-13, TZ-14, TZ-15, TZ-16a, each set in its report; `twap60` of B3's candidates (TZ-30) | every quote after `1790452200` |
| five-minute markets' documents and fills, from the venue | the labels to `1792451400` (TZ-23, TZ-29), the fills of M0's 8,064 markets, the formation's 864 and W0's 1,008 to `1792753800` (TZ-31); the settled documents of W1's legs to `btc-updown-5m-1793023800` (TZ-32) | every fill of a market with `T0 > 1792753800`; every settled document of a leg after `btc-updown-5m-1793023800` |
| the chain book | every window to `1791241200` (TZ-24) | every window after `1791241200` |
| the pair book's streams and books | TZ-27's 51 windows `1791660600` … `1791705600` and `1792137600` … `1792722600` (the Architect, for TZ-30 and TZ-32); `1791706500` … `1792403100` (TZ-30); `1792754100` … `1793013300` (TZ-32) | the 34 windows `1792723500` … `1792753200`, and every window after `1793013300` |
| Binance's public trades | 2026-10-23 to 2026-10-26, by the Architect after W1 | every trade after 2026-10-26 23:59:59 UTC |
| the reward book's days | 2026-10-28 to 2026-11-13: the Architect's explorations and TZ-33's runs, L0's nine candidates (TZ-41, TZ-43) and TZ-45's five members; **2026-11-21 and 2026-11-22: the public trades of L1's eight markets, read by the Architect for L1's loss** — those markets' days hold L1's own quotes and are explored, in no gate's set (CANON PART II, the L track) | **every other day from 2026-11-14, `D0` ≥ `1794614400`: reserved** (§2.6); **2026-11-18 to 2026-11-20 are H0's (TZ-57)** |
| L1's unit's own record — its orders, fills, positions and equity, and the venue's payouts to our address | TZ-53's prove, four orders, none filled; 2026-11-21 and 2026-11-22: the bot's wallet's public trades and positions and the venue's earnings read, by the Architect for L1's loss (CANON §1.5) | the unit's journal and stop record, read by no one |
| **Kalshi's markets — listings, trades, series** | **closing 2026-11-12:** the Architect's explorations of 2026-11-22 — the day's whole listing, the trades of about 1,500 drawn markets and their series' fees — and the counts of the listings of 2026-11-08 to 2026-11-15 (CANON §1.8); re-read 2026-11-27 — the day's listing, the trades of the rehearsal's 103 draws and the cutoff; TZ-56's rehearsal reads 2026-11-12 again | **every market closing 2026-11-16 to 2026-11-21: reserved for K0 (TZ-56)** — no TZ and no session of the Architect reads a listing, a trade, a price or a result of one before TZ-56's `frame`; every market closing on 2026-11-13 to 2026-11-15 and from 2026-11-22, unread |
| **Polymarket's markets outside the reward book — listings, documents, public fills** | ending 2026-08-01 to 2026-10-31 at the snapshots of 08-01, 08-15 and 09-01, and **ending 2026-11-12** — its whole keyset listing and the fills of about 1,300 drawn markets, the Architect's of 2026-11-22 (CANON §1.8), re-read 2026-11-27 with the fills of the rehearsal's 179 draws; the counts alone — pages and markets — of the keyset listings of the markets ending 2026-11-06 to 2026-11-11 and on 2026-11-13, read 2026-11-27; L1's eight markets' fills of 2026-11-21 and 11-22 | **every market ending 2026-11-16 to 2026-11-21: reserved for K0 (TZ-56)**, as Kalshi's |
| the venue's reward configurations | the Architect's snapshot of 2026-10-27 — 14,089 configurations, 1,726 books, 1,723 documents — excluded from L0's sets by time | — |
| ADV-3 | the history to the close of 2026-10-27 (Gate H, Gate S; TZ-38's exploration) | the forward records, by any reading — the rule's and the PIT record's from the close of 2026-10-28, the market record's from 2026-10-31; running figures decide nothing |

**Other assets' markets are not a shortcut:** the pricer's domain threshold is in USD/s and its link tables are the
BTC feed's, so each asset would need its own Phase 0 and Phase 1, and same-window outcomes across assets move
together.

---

## 6. Environment

The host's measured capacity and the venue's measured limits. **Every resource or capacity threshold a TZ states is
stated in exact units and derived from this section** (CANON hard rule 9); each figure names the report or the read
it comes from, and the readings before it are in that report and in revision `2026-11-17-a`.

| item | value |
|---|---|
| host | Vultr VPS (Warsaw); the Executor runs Claude Code CLI **on the VPS itself**. A cloud Claude Code session is not this host and cannot execute anything that touches the capture. **It cannot place an order:** the venue reads its address `blocked` (venue geoblock, below). |
| **host identity, for TZ host gates** | `/var/lib/btc-recorder/` exists and holds interval directories · its `runtime.jsonl` holds `start` records carrying sha `4216c04673ced76b5b2ac60ef57c9abedc46f9b9` and, since TZ-21's restart, `e3975b5da44c5328adf3bf3914634cd878842c73` · the filesystem holding it is `/dev/vda2`, total `31,612,203,008` bytes. All three, or it is not the capture host. **Whether a capture process runs is not identity:** it is a state each host gate states for itself (§7 item 86). |
| language | Python 3.12. **The research interpreter is `/root/tz01-env/venv/bin/python`** — Python 3.12.3 with `numpy` 2.5.3; the system `python3` has no `numpy`. Every running unit and both archives run `/root/tz04a-env/venv/bin/python` — Python 3.12.3 with `websockets` 17.1 — and the disabled chain book `/root/tz01-env`. Neither environment is scratch, and no TZ removes either. |
| stack | Parquet storage, pandas/pyarrow, DuckDB for aggregation; `decimal.Decimal` at 60 digits for every price |
| auth | CLI subscription auth; `ANTHROPIC_API_KEY` must not be set |
| git remote | HTTPS with the repository token embedded in the remote URL. Since 2026-10-20 every git request prints `warning: redirecting to https://github.com/seahomebatumi-ai/btc-5m-twap.git/`; pushes went through the URL's own credential on 2026-10-28, 10-29 and 10-31 (TZ-33, TZ-34, TZ-37 reports), and through `credential.helper=!gh auth git-credential` where it failed (TZ-29, TZ-30): **a TZ keeps `gh`'s route as its fallback** and touches no token (§7 item 114). |
| egress | **`api.elections.kalshi.com` is measured from this host by no TZ: TZ-56's probe is the first request (§7 item 202).** DNS and TCP/443 open to `ws-live-data.polymarket.com`, `gamma-api.polymarket.com`, `clob.polymarket.com`, `ws-subscriptions-clob.polymarket.com`, `docs.polymarket.com`, `data-api.polymarket.com`, `polymarket.com`, `fapi.binance.com`, `data.binance.vision`, `api.telegram.org` and GitHub; since TZ-54 `api.binance.com`, `api.pushover.net` and `hc-ping.com`, each served to the liquidation guard. **No trading credential of any kind is held, and every venue is read anonymously.** Beside the repository's credential: the advisor's bot token, the Boss's, at `/etc/adv3-bot/token` (§2.7), and since TZ-54 the liquidation guard's under `/etc/liq-guard/` — **a Binance key that can read alone, bound to this host's IPv4 address**, read `enableReading True`, `ipRestrict True` and every other permission `False` by TZ-54's G-KEY; Pushover's user key and the guard's three application tokens — «Сторож», «Сторож LONG» and «Сторож SHORT» since TZ-55; its Telegram bot's token and chat; and the dead-man's address (§3, the trees). `fapi.binance.com` answers HTTP 451 to the Architect's own sessions, so an audit of the advisor reads Binance's archive. |
| **venue edge — the `User-Agent`** | `gamma-api.polymarket.com` and `clob.polymarket.com` answer **HTTP 403, body `error code: 1010`**, to `urllib`'s default `User-Agent` and serve any other; `Accept: application/json` alone does not help (TZ-18, TZ-18a; the Architect, 2026-09-22 and 09-23). The agents served there: `btc-5m-twap-tz17`, `-tz18a`, `-tz26`, on the websocket handshake too, and `-tz33`; and `-tz44` at `polymarket.com`. **Every request a TZ fixes names its `User-Agent`.** |
| **venue geoblock — measured from the host, 2026-11-13, TZ-44** | `GET https://polymarket.com/api/geoblock` with `User-Agent` `btc-5m-twap-tz44` and `Accept` `application/json`, one request: status `200`, 66 bytes, keys `blocked`, `country`, `ip`, `region` — **`blocked` `True`, `country` `PL`, `region` `14`**. The venue's documentation lists Poland among the countries from which orders may only close positions, on its website and through its API alike; names `eu-west-1` as the closest region it does not restrict, its own servers in `eu-west-2`; restricts Ireland, the Netherlands, Japan and South Korea on its website alone; and lists Georgia nowhere [read by the Architect on 2026-11-12 and 2026-11-13 at `docs.polymarket.com/api-reference/geoblock`; not measured]. **No order of ours can open from this host.** A live step runs from another address, and the TZ that deploys it measures that address by the same read before anything else (§7 item 163). The reply's `ip` is never printed, written or published. |
| **live host** | **xServer (XServer OÜ), a VPS in Sofia, Bulgaria**, bought by the Boss on 2026-11-18 — **kept: TZ-49 read KEEP on 2026-11-19, before the end of its refund, 2026-11-24** — the host L1's orders are to come from (CANON PART IV). TZ-49's `host before` and `host after`, 13:56:44 and 14:08:34 UTC on 2026-11-19: Ubuntu 24.04.5 LTS, kernel 6.8.0-138-generic x86_64, Python 3.12.3 as `/usr/bin/python3`; one processor, an Intel Xeon Gold 6248R at 3.00 GHz, under VMware; `MemTotal` `1,944,465,408` bytes; `/` on `/dev/mapper/lvm-root`, ext4, `20,779,339,776` bytes, `16,987,521,024` to `16,987,779,072` available across TZ-49's reads; booted 2026-11-18 16:57:40 UTC, the boot TZ-48 read. **As TZ-49 left it:** the image's own swap, `/swap.img`, `1,048,572` KiB active — `1,073,741,824` bytes with its header, `0600`, root's — from its own `fstab` line, `swap.img.swap` active from `/etc/fstab`, none of it used, and `vm.swappiness` `10` from `/etc/sysctl.d/zz-btc-5m-twap-swap.conf`, `60` and set in no file before; the journal bounded by `/etc/systemd/journald.conf.d/zz-btc-5m-twap-limits.conf`, sorted after the provider's `cap.conf` — `SystemMaxUse` `512M`, `SystemKeepFree` `2G`, `SystemMaxFileSize` and `RuntimeMaxUse` `64M`, `Storage` `persistent` and `ForwardToSyslog` `no`, every key in force from it, journald's own message `max 512.0M` — the journal `42.2M`; rsyslog disabled and stopped, and its socket stopped; `sshd` by `/etc/ssh/sshd_config.d/00-btc-5m-twap.conf`, sorted before the provider's `01-xserver.conf` and read at `sshd_config`'s `Include`, its line 12, before that file's own `PermitRootLogin yes` at line 42: `passwordauthentication no`, `kbdinteractiveauthentication no`, `permitrootlogin without-password` and `pubkeyauthentication yes`, and a connection that offers no key is offered `publickey` alone — **root by key alone** (§7 item 183); timesyncd synchronized, offsets `−1.783` and `+1.852` ms; `unattended-upgrades` enabled, `Automatic-Reboot` unset; `/var/log/btmp` `6,012,928` bytes on disk at `host after`, `36,864` more in 710 s; TCP port 22 on any address of both families and the resolver on loopback. Its `/etc/sysctl.d` holds, beside Ubuntu's own files, `10-bufferbloat.conf`, `99-cloudimg-ipv6.conf` and `99-gaming.conf`, the last written at 15:11 UTC on 2026-11-18 with the provider's `cap.conf`; none was read, and none sets `vm.swappiness`. **Its commands print in Russian** (§7 item 185). **Of this project it holds** those three drop-ins, each byte for byte from `research/tz49-live-host.py`'s constants, and root's one authorized key, the Executor's; **and, since TZ-50 and TZ-51,** `/root/l1-env`, the venue's client `polymarket-client` `0.20.0` installed from the 35 pinned wheels, `55,492,611` bytes; `/etc/l1-bot/`, `0700`, root's, holding `session-key`, `0600`, 67 bytes — **authorized by the owner's signature for the bot's wallet at 18:35 UTC on 2026-11-20** (TZ-51 report §2.1) — and the owner's `relayer-key`, the bot's `telegram-token` and its `chat-id`, pinned by TZ-52, each `0600`; and `/var/lib/l1-bot/`, `0700`, holding `account.json` and TZ-51's instrument, for B-REVOKE — TZ-52's removed by TZ-53. **Since TZ-53, 2026-11-21, L1's unit runs there** (§3, the units): `/root/l1-bot-svc/`, `0700`, holding `l1-bot.py`, the two frozen files it takes rule W and the selection from, and its unit file's copy, each `0600`; `/etc/systemd/system/l1-bot.service`, enabled; and under `/var/lib/l1-bot/` its prove record `prove-1.json`, its state, its stop history `stops/`, its journal, selections and polls, and `service.log` (§7 item 193). TZ-52 placed and cancelled the key's first order, TZ-53's prove four more, none filled, and the unit quotes since 08:37:38 UTC (§7 item 192). The wallet's pUSD allowances to both exchanges are the maximum the venue set (§7 item 190). **The Boss reaches it by `ssh live-host` as root on the capture host, or by the provider's console, where his root password still works;** he gave no SSH key of his own at TZ-51, and root's one key is the Executor's. |
| **live host identity, for TZ host gates** | the first label of its host name, `vs-2348` — never the full name, its provider's DNS record, which publishes its address (§7 item 180); its ED25519 host key `SHA256:Y14Iy6okVrEz76M/JsR9hLre/54PtMAGXd6ZKDe4ZJw` among its three SSH host keys, pinned under the alias `live-host` at TZ-47's first connection; Ubuntu 24.04; Python 3.12; neither `/var/lib/btc-recorder` nor `/root/btc-5m-twap` present — TZ-48's and TZ-49's LH1 to LH5, 5 of 5 each. **Access:** the Executor, on the capture host as root, by its own key `/root/.ssh/live-host`, `SHA256:1xbA0Mhjj0NDXcLaefl9D8run7ZKh/oo0xUOmc06Qzo`, through the alias in root's `~/.ssh/config`, `BatchMode=yes`; no Claude Code on the live host (TZ-48 §1.2); **root logs in by key alone since TZ-49**, the Executor's key its one authorized key. |
| **live host — the venue's geoblock, measured 2026-11-19, TZ-48 and TZ-49, and 2026-11-20, TZ-50** | `GET https://polymarket.com/api/geoblock` with `Accept` `application/json`, over IPv4: **TZ-49, IPv4 alone in the process** — `User-Agent` `btc-5m-twap-tz49`, 13:56:54 UTC, one read — status `200`, **`blocked` `False`, `country` `BG`**, `region` `22`, and the address the venue saw the connection's own; TZ-48's read, `btc-5m-twap-tz48`, the same; **TZ-50's, `btc-5m-twap-tz50`, 06:22:21 UTC on 2026-11-20, the same** (its report §2.3). **IPv6, from the kernel's tables, no IPv6 socket opened:** one global address, flags `80`, and two default routes, neither usable — no IPv6 route up that is not a reject route (TZ-49); TZ-48's three IPv6 connections each raised `OSError` at once, so no IPv6 request of the host has reached the venue (§7 item 181). The venue's documentation names Bulgaria and Georgia nowhere among its blocked and close-only countries [read by the Architect at `docs.polymarket.com/api-reference/geoblock` on 2026-11-19; not measured]. |
| **live host — the venue's CLOB from Sofia, measured 2026-11-19, TZ-49** | Over IPv4 alone, `User-Agent` `btc-5m-twap-tz49`: `clob.polymarket.com` resolves to two Cloudflare addresses and answers through its Sofia data centre, `SOF` — the root `"OK"`, `/time` ten digits, cache `DYNAMIC`, the venue's seconds less the host's `0`; `ws-subscriptions-clob.polymarket.com` resolves to four addresses that carry no `cf-ray`, and the market websocket's handshake answers `101` with a valid accept key. **60 TCP handshakes** with the CLOB's edge, 0.5 s apart: 60 completed, median `0.917` ms, 95th percentile `1.354` ms, maximum `1.933` ms. **`/time` over one kept connection**, 600 counted after 5 warm-up, one every 0.75 s from 14:00:19 UTC: 600 valid, every one through `SOF`; the time to the first byte p5 `53.804`, p50 `56.296`, p95 `63.941`, p99 `90.518` and max `225.146` ms, the halves' medians `56.628` and `55.950` ms; the venue's seconds less the host's `−1` to `0` — **a one-way bound of `28.148` ms, half the median: G-LAT PASS against 50, so L1's replay keeps its 50 ms** (TZ-49 report §2.4 and §2.5, G-LAT re-derived by the Architect from its 605 lines). **Its disk:** 256 MiB written and synced at `1,209,487,627` bytes a second; 200 appends of 4 KiB, each with `fsync`, a median of `0.501` ms, a 99th percentile of `1.005` ms and a maximum of `1.716` ms (TZ-49 report §2.6). |
| **disk** | One writable filesystem `/dev/vda2`, total `31,612,203,008` bytes; `/var/lib`, `/root`, `/var/log` and `/var/www` all on it. **At TZ-46's close, 17:02:02 UTC on 2026-11-17: `10,607,034,368` bytes free**, `8,710,725,632` at 14:17:52 before its removals. **The room** — free space and the reward book's stream files — `10,653,932,210`; **its margin over `STREAM_FLOOR` and `PEAK`, `2,908,396,574` bytes** (TZ-46 report §2.1; §7 item 175). **TZ-50's read, 06:21:25 UTC on 2026-11-20:** `10,454,573,056` bytes free on `/var/lib`, the room `10,542,952,913`, **its margin `2,797,417,277`** (TZ-50 report §2.4), TZ-49's `2,874,778,827` at 13:55:53 UTC on 2026-11-19; `10,477,932,544` free at TZ-50's closing reads and `10,492,223,488` after its §9; the reward book's store `447,566,349` bytes at its §0.3 and `404,065,191` at its closing reads, the archive's run of 07:30:20 UTC between them. The lowest free reading recorded: `6,874,419,200` bytes at 01:36:02 UTC on 2026-11-14, in the reward book archive's record before its removal, the night after the floor stopped the streams (§7 item 170). The trees at 17:02: `/usr` `4,547,965,470`; `/var/log` `3,973,819,096`, the journal `2.9G`, near journald's default cap; `/root` `3,247,637,408`; `/var/lib` `2,680,271,463` — the recorder `1,657,840,396`, the reward book `367,704,114`, the pair book `146,635,542`, the chain book `43,108,667`, the pair book's archive `32,154,911`, the reward book's archive `6,032,107`; the forensic store `355,893,557` at 2,532 files, before TZ-46's §9 copied 35 more; `/root/tz01-env` `517,113,206`; another project's `/root/PROJECT_GAMING_PS5` `672,410,091` (TZ-46 report §2.2). **Every TZ that touches the host reads `df` and `du -sb` of the stores it touches, and prints the margin** (§7 item 175). |
| **disk floors and caps, as each code reads them** | **The recorder:** `2,000,000,000` bytes free and `4,000,000,000` apparent bytes of its own tree, at start-up and every interval's close; either stops it, exit `0`, not restarted (§2.3; §7 item 179). **The reward book:** `STREAM_FLOOR` `7,300,000,000` free and `STREAM_CAP` `4,000,000,000` of stream files, at every slot's decision; `100,000,000` stored bytes a slot; `RESOURCE_FLOOR` `2,200,000,000` free at its start, a slot's start or a selection, and `WRITE_CAP` `1,000,000,000` bytes one process writes outside its streams — either halts it, exit `1`, not restarted (§2.6; §7 item 178). **`PEAK`**, the most the reward book's store holds between two archive runs, `445,535,636` bytes — fourteen slots at L0's heaviest, `31,823,974` [modelled] (TZ-46). **The pair book, stopped:** `4,500,000,000` free and `8,000,000,000` of streams, read once a process (§2.5). **A floor a TZ states is stated in exact bytes and derived from this row and the next** (§7 item 6). |
| **capture cost, measured** | **The recorder:** `33,632,842` bytes a day on disk and `26,784,064` apparent, measured against the filesystem by TZ-09 — its own write rate, not the rate the filesystem fills at. **The reward book's streams:** `1,016,070,120` bytes a day over TZ-33's first four slots, a Wednesday midday, `96.0` frames a second and about `121` stored bytes a frame; `1,006,278,726` over TZ-34's first set, Wednesday 11:30 to Thursday 08:45 UTC; the heaviest slot of L0's eight days `31,823,974`. **Its other files:** `16.3` MB a day (TZ-33) and `14.6` MB a day over TZ-46's `9,850` s. **The advisor:** its journal `144,355` bytes at TZ-42's close, a `check` record `6,778` to `7,066` bytes, two a day (TZ-42). |
| **headroom — measured on total free space, and conditional** | **Beside the streams this project's stores grow about `50,000,000` bytes a day** — the reward book's other files and the recorder's — and the host's other tenants at no rate this project has measured: everything else about `43,500,000` bytes a day across TZ-26's session, and `187,760,570` at the fastest window any TZ has read, TZ-16a's two preflight reads 16,750.8 s apart on 2026-09-27, net of that session's own trees — the one quoted, because windows on a shared host fix neither end of the rate (§7 items 25 and 29). **At TZ-46's margin that is about two months at `43,500,000` a day and 15.5 days at `187,760,570`** [modelled]. **It is conditional on `telemetry-watch.service` staying disabled:** its measured active drain is `2,361,691,000` bytes a day (the consumer, below), and every TZ re-reads `df`, `du` and `systemctl is-enabled` in its own §0 and states all three. |
| **the consumer** | `/root/PROJECT_GAMING_PS5/netaudit/telemetry/captures`, another project's tree, written by its `telemetry-watch.service`. Active, free space fell `2,361,691,000` bytes a day, about `1,700,000,000` of it that project's (TZ-10b, 2026-09-14); since TZ-11 every read has found the unit `disabled` (exit 1) and `inactive` (exit 3) — the last at TZ-46's host gate on 2026-11-17 — the tree growing a few megabytes a day, `672,410,091` bytes at TZ-46. No TZ touches it. |
| **price to beat** | published by Gamma only after settlement, at `events[0].eventMetadata.priceToBeat`, and captured per interval in `resolution.json`; a live pricer reconstructs it from the feed. **Beside it, `finalPrice` is the reading the market settled on, and it equals the next market's `priceToBeat` as the same literal** — 600 of 600 (TZ-18) — so a label can be read from either document. |
| **resolution endpoint** | `GET https://gamma-api.polymarket.com/markets/slug/btc-updown-5m-{T0}`, polled from `T0+333` every 15 s; the same path serves `btc-updown-15m-{T}`; `/markets?slug=…&closed=true` serves up to twenty documents in one request. **A settled document's readings are stable, and its bytes are not** (§7 item 100): a stored body is re-verified from the venue by its readings, never by its hash. |
| **CLOB websocket — the market channel** | `wss://ws-subscriptions-clob.polymarket.com/ws/market`, public, no credential. The handshake is answered `101` under a non-default `User-Agent`; the subscribe frame is `{"assets_ids": [...], "type": "market"}`; the text frame `PING`, sent every 10 s, is answered `PONG`. After the subscribe one list frame holds a `book` of every subscribed token, then four event types and no other: `book`, `price_change`, `last_trade_price` and `tick_size_change`. Every `price_change` frame names one market and carries one entry for each of its two tokens, each `asset_id`, `price`, `size`, `side`, `hash`, `best_bid`, `best_ask`; `best_ask` `"1"` and `best_bid` `"0"` stand for an empty side; prices carry at most three decimals and sizes two. A book rebuilt from the stream equals the `/book` reply at the touch, 300 of 300 on the ETH nested pair (the Architect, 2026-10-20). **Lag**, a `price_change` frame's receipt less its venue stamp: a median of `11` to `24` ms; a 99th percentile by window from `46` to `5,201` ms on the nested pair (TZ-26, TZ-30) and `59` to `96` ms on the reward book's first slots (TZ-33); `recv_ns` is stamped when the event loop takes the frame, so a host-side stall cannot be told from venue batching. The reward book opens one session a slot, 910 s long; a socket silent for `251.8` s is measured once (§2.6). |
| **CLOB order book, REST** | `GET https://clob.polymarket.com/book?token_id={token_id}` — public, unauthenticated; the reply puts the worst price first on both sides, so a reader takes `max` over bids and `min` over asks (TZ-14) |
| **venue constants, measured TZ-05a and TZ-14** | **tick size** `0.01`, falling to `0.001` inside an interval as the price reaches the wings — not a constant of the interval · **minimum order size `5`** on the five-minute markets · **fee schedule** `{"exponent": 1, "rate": 0.07, "rebateRate": 0.2, "takerOnly": true}`, `feeType` `crypto_fees_v2` · outcome mapping from the outcome strings, `outcomes[i] == "Up"` against `clobTokenIds[i]`, never from position · **how the taker fee is collected** — in USDC beside the price, or in shares — is read by no TZ · **from 2026-11-24 the BTC Up/Down markets trade on Polymarket Protocol V2** — a V2 market's gamma document carries `version` `"v2"` and `positionIds`, `outcomes[i]` against `positionIds[i]` — read, not measured (§7 item 186). |
| **taker delay, crypto** | `150` ms since 2026-09-04 14:00 UTC — the venue's changelog, read by the Architect through its entries of 2026-10-21; measured by no TZ (§7 item 87). During the hold a marketable order "is pending and cannot be canceled"; **a post-only order that would match immediately "is rejected instead of executed"** (the venue's order-lifecycle page, read 2026-10-23). |
| **public fills — Data API v2** | `GET https://data-api.polymarket.com/v2/trades?condition=…&taker_only=…&limit=1000`, no credentials, at most 20 condition ids a request and 1,000 rows a page; `taker_only=true` serves each fill once on its taker side, `false` adds the maker rows, each with its own `proxy_wallet`; rows under `0.01` share are never served. **The cursor carries no filter:** every request re-sends `condition` and `taker_only` beside `next_cursor`. `/v2/trades` and gamma `/markets` each take 300 requests in 10 s. v1 is retired since 2026-10-24. Measured by TZ-23, TZ-29 and TZ-31 and the Architect. |
| **Kalshi's public API — read by the Architect, 2026-11-22 and 2026-11-27, from his session** | `https://api.elections.kalshi.com/trade-api/v2`, no credential, every reply served gzip on `Accept-Encoding: gzip`. **`GET /markets`** with `min_close_ts`, `max_close_ts` and `mve_filter=exclude`, `1,000` a page by `cursor`, latest close first: the listing of the markets closing on 2026-11-12, with an hour past both ends, was 103 pages, `102,796` markets, `92,700` of them closing in the day, every one `binary` and `finalized` — `28,563` resolved yes or no and traded — and each market's `close_time`, `result`, `status`, `volume_fp` and `event_ticker`, its series the ticker's part before the first hyphen (517 series that day); about `208,000,000` bytes a day uncompressed and `6,100,000` as kept. **`GET /markets/trades`** by `ticker`, `min_ts` and `max_ts`: each trade's `taker_outcome_side`, `yes_price_dollars` and `no_price_dollars` summing to 1, `count_fp`, `created_time` to the microsecond and `is_block_trade`. **`GET /series/{ticker}`**: `fee_type` and `fee_multiplier` — of the `16,775` series `GET /series` listed, `16,580` `quadratic` at 1, `159` `quadratic_with_maker_fees` at 1, `18` `quadratic` at 0.5, `14` at 0; the taker's fee `round up(M × 0.07 × C × P × (1 − P))` to a centicent (its fee schedule, effective 2026-07-07, read). **`GET /series/fee_changes?show_historical=true`** listed 107 changes, the last of 2026-09-03; **`GET /events/fee_changes`** none. **`GET /historical/cutoff`**: markets and trades before 2026-09-22 only through `/historical/*`. **Its rate limit:** a read of trades costs `50` of a `600` bucket (`x-ratelimit-*`), a refusal `429` with `x-ratelimit-reset` about `2.8` s; about `2.5` requests a second sustained over 982 requests, 47 of them refused once. **Re-read 2026-11-27:** the cutoff `2026-09-28` for markets and trades — six days later in five; 2026-11-12's listing, `28,563` rows, and the trades of the rehearsal's draws unchanged. **The listing's pages a day**, markets closing 2026-11-08 to 2026-11-15: `138`, `119`, `110`, `104`, `103`, `112`, `109` and `135` — the Sundays the largest. |
| **Polymarket's gamma and Data API outside the reward book — read by the Architect, 2026-11-22 and 2026-11-27** | **gamma `/markets` refuses an `offset` past about `5,000` (`422`, `offset too large, use /markets/keyset`)**; `GET /markets/keyset` with `closed=true`, `end_date_min` and `end_date_max`, `100` a page by `after_cursor`, each market with its events and their series: the markets ending on 2026-11-12, with an hour past both ends, were 263 pages, `26,237` markets, `23,122` ending in the day, `317` of them at `["0.5", "0.5"]` and `22,805` resolved to one outcome; about `191,000,000` bytes a day uncompressed and `12,800,000` as kept. **`volume`, `volumeNum` and `volumeClob` are absent on `14,111` of the `24,577` closed markets ending from 00:00 on 2026-11-12 to 00:00 on 2026-11-13, both ends included** — `1,272` of them crypto Up/Down markets; of 25 such markets sampled, 3 had fills, all three crypto Up/Down — so no frame filters Polymarket's markets by volume (§7 item 201). **A closed market's `feeSchedule` carries the venue's current terms:** the five-minute BTC markets of 2026-11-12 read `rate` `0.01` on 2026-11-22, where TZ-14 measured `0.07` before the change of 2026-11-20 (§7 item 201). Data API v2's fills of a condition come newest first across pages; a fill's `outcome` text can differ from gamma's by punctuation while its `token_id` is the outcome's (`Ragin Cajuns` against `Ragin' Cajuns`). **Re-read 2026-11-27: every document carries `version`.** 2026-11-12's listing, all `26,237` `v1` on 2026-11-22, was `288` pages and `28,777` markets on 2026-11-27 — `2,532` `v2`, the Protocol V2 pilot, and `8` more `v1`, closed from 2026-11-25 (§7 item 203). **The listing's pages a day**, markets ending 2026-11-06 to 2026-11-13 but 2026-11-12: `347`, `987`, `887`, `270`, `250`, `245` and `271` — the Saturday and the Sunday the largest. |
| **reference prices — RTDS is legacy** | the venue's changelog of 2026-09-15 marks RTDS legacy for reference prices and opens PolyBolt, `wss://ws-live-v2.polymarket.com/ws`, whose `price.crypto.twap` carries the Chainlink TWAP prices — **with CLOB API credentials required**. RTDS still serves the recorder's four topics; **the recorder's settlement feed rests on a legacy socket**, and a move is a TZ of its own. |
| **RTDS's fast prices, read live by the Architect on 2026-10-27** | `crypto_prices` `btcusdt` publishes one price a second, its payload stamped on the whole second and the message about `130` to `150` ms after it; `crypto_prices_chainlink` one a second, stamped on the second before. A price sampled once a second cannot withdraw a quote inside the 150 ms taker delay. |
| **maker incentives** | Makers pay no fee; the Crypto maker rebate is 20% of each market's taker fees, paid daily in pUSD, fee-curve weighted, a `1` pUSD minimum payout — **measured against the venue's payouts on 2026-10-20** at four wallet-days: the operative field is `rebateRate` (TZ-29; CANON §1.1). **Liquidity rewards** are configured per market — `rewardsMinSize`, `rewardsMaxSpread`, `rewardsDailyRate` — scored once a minute, paid at midnight UTC (CANON §1.7); none on the five-minute BTC markets since August's programme. **A market's terms move between days and inside a day, and the venue serves no history of them** (§7 item 155). **What the venue pays an address of ours is measured by no one** — L1's measurement. **From 2026-11-20 23:59 UTC** the maker rebate is a tier of 30-day maker weighted volume — `0` under `200,000` USD — and the BTC five- and fifteen-minute taker coefficient `0.05`; liquidity rewards unchanged — read, not measured (§7 item 187). |
| host is shared | unrelated production services live on the same filesystem — `crypto-auto`, `my_real_estate_bot`, `seahome_webapp.git`, `/var/www`, `/var/log`, and `crypto-deploy.service` and `crypto-announce.service`, units of another project, whose bursts of `systemctl daemon-reload` came before runs of the archives off their calendars (§7 item 115). No TZ touches any of them. The recorder never deletes anything it did not write. |
| capture path | `/var/lib/btc-recorder/**`, `/var/lib/btc-chainbook/**`, `/var/lib/btc-pairbook/**` (§2.5) and `/var/lib/btc-rewardbook/**` (§2.6) — all outside the repository by design, so no capture can reach git history |
| **process supervision** | Every long-lived process is a systemd system unit in `system.slice`, enabled for boot, with its own restart policy and stop (§3, the units; CANON hard rule 14). **Root's `Linger` is `no` and `KillUserProcesses` is commented out** (TZ-19 report §3.2): a process started from a login session, `nohup`, `setsid` or a tmux pane ends with root's last session. **Running at TZ-50's host gate, 06:21:18 UTC on 2026-11-20, and at its closing reads, 08:03:08 UTC:** the recorder, pid `1555954`, the reward book, pid `1556307`, and the advisor, pid `1555970`, each `NRestarts` `0` since the package manager's restart of 06:11:41 to 06:11:44 UTC on 2026-11-14; the reward book's archive's timer, its next elapse on the three-hour calendar. **Disabled:** the chain book, the pair book and the pair book's archive's timer. **The liquidation guard runs since 18:30:43 UTC on 2026-11-21**; its second version since 10:01:40 UTC on 2026-11-22, pid `2825760` at TZ-55's close. **`NRestarts` counts since a unit's last start, never a lifetime** (§7 item 136): a stop and start — the package manager's, a boot, a hand — resets it. **The package manager restarts the units:** `unattended-upgrade`, `apt-daily-upgrade.timer` near 06:00 to 06:30 UTC, restarted both captures on 2026-10-22 and 10-23 and the recorder, the reward book and the advisor on 2026-11-14 (§7 items 120 and 176). One boot since 2026-08-02 07:24:34 UTC (TZ-29 to TZ-31), and the archives' timers active since 2026-10-11 and 2026-10-29 at TZ-46's first read show none since; a boot restarts every enabled unit. |
| **memory** | **The host**, `free -b`: `1,002,127,360` bytes of memory; swap `3,250,581,504`, `632,320,000` to `953,434,112` used at the TZs' reads since 2026-11-01, the least at TZ-49's §3.9. **One processor.** `MemAvailable` across the TZs' reads since 2026-10-31: from `136,404,992` (TZ-37's printed read) to `562,360,320` (TZ-46); TZ-49's `239,890,432` to `271,249,408`; TZ-50's `249,425,920` to `281,980,928`; with the liquidation guard running, TZ-54's `221,118,464` (`215,936 kB`) to `246,251,520` and TZ-55's `218,279,936` to `242,495,488`. **The live host:** `MemTotal` `1,944,465,408`, `MemAvailable` `1,455,759,360` to `1,492,766,720` across TZ-50's reads, `1,497,681,920` to `1,513,070,592` across TZ-49's, swap `1,073,737,728` and none of it used. **The units**, each control group's charge, page cache included: `MemoryMax` `512M` for the recorder, `192M` for the reward book, `128M` for the advisor and each archive's service; the measured `MemoryPeak` the recorder's `316,174,336` (TZ-36), the reward book's `78,729,216` (TZ-36), the advisor's `51,396,608` (TZ-42), the liquidation guard's `21,970,944` (TZ-54) and its second version's `28,340,224` (TZ-55), under its `MemoryMax` `96M`, the reward book archive's run `58.5M` in the journal (TZ-46). **`memory.current` and `memory.peak` include page cache**, so a ceiling is sized from `anon`, `kernel` and swap over days, never from `memory.peak` (§7 items 88 and 137). **A memory floor** is twice the larger of the measured host peak of the same code and the Architect's peak modelled at the ratio of its own method — TZ-37's `1.199` (§7 items 131 and 156); **the ratio of the host's peak to the Architect's belongs to the method that measured it** (TZ-42). Recent floors: TZ-44 `98,319,394`; TZ-46 `133,073,162`, twice `66,536,581`, its host peak modelled, its largest mode `forensics` `45,858,816` on the host; TZ-49 `72,439,812`, twice `36,219,906`, modelled from the Architect's `30,208,000` for its `latency` — on the live host that mode peaked at `30,519,296`, `1.010` times the Architect's, and the run's 23 peaks on both hosts from `26,546,176` to it; TZ-50 `85,051,706` and, for the client's modes, `275,045,368`, its host peaks `33,968,128` to `42,151,936` and `75,837,440` to `96,661,504` (its report §2.6); TZ-56 `136,636,736`, twice ⌈`56,979,456` × `1.199`⌉, its `rehearse` over 2026-11-12's two listings the largest of its modes at their bounds. glibc's mmap threshold fixed at 128 KiB and two arenas keep a long-lived process's resident size flat (TZ-33). |
| **RTDS session limit, measured 2026-09-10** | the server closes every websocket `7,200` s after it opens, `1001 Going away`, timer restarting on each new connection. Undocumented. **No TZ may require an unbroken socket for longer than this.** **From 2026-11-30 00:00 UTC** a price subscription names its provider, and one Chainlink serves — the TWAP topics among them — needs a Chainlink API key — read, not measured (§7 item 188). |
| clock | NTP-disciplined; SNTP replies validated at reception since `4216c04`. Maximum absolute offset over TZ-05a's window `18.789` ms; **over TZ-14's 1,200 intervals `33.946` ms**, no interval above 50. An offset above 50 ms invalidates a latency claim; it is not a membership condition for anything. |
| **sandbox limit — network** | calls that read the git token and send it to `api.github.com` are refused; `git` push and pull work. Release creation and asset upload cannot be done from inside the Architect's session — they are the host's, or the Boss's block, verified by anonymous download. **The Architect's session is not the Executor's and is not constant:** a TZ never depends on the Architect's reach, and a check it cannot perform becomes a BLOCK condition (CANON hard rule 13). On 2026-11-17 the Architect's shell downloaded Release assets anonymously; GitHub's API for the repository and a Release's HTML pages were refused by its proxy (`403`), and attaching the repository with a credential was refused by the harness. On 2026-11-19 the Architect's session read the repository and pull request #47's refs by `git` alone; GitHub's GraphQL and REST APIs for the repository answered `403`, its access not attached to the session. |
| **GitHub Releases — the archives' destination** | GitHub's documentation, read 2026-10-10 and 10-11: up to `1,000` assets a Release; each file under 2 GiB, `2,147,483,648` bytes; no limit on a Release's total size or bandwidth; unauthenticated API requests `60` an hour from one address; content-creating requests `80` a minute and `500` an hour, a refusal `403` or `429` with `retry-after` or `x-ratelimit-reset`. **The API's record of an asset carries its digest**, `sha256:…`; an asset downloads anonymously at `https://github.com/seahomebatumi-ai/btc-5m-twap/releases/download/<tag>/<asset>`, answered `302` to `release-assets.githubusercontent.com`; an anonymous reply may be cached for 60 s. **The host's rates:** uploads about `9,297,801` to `10.2` million bytes a second, downloads about `13` to `14` million (TZ-27, TZ-28); the archives budget a transfer at `2,000,000` bytes a second. At TZ-46's `forensics`, the API served 93 Releases and 5,496 assets anonymously in 6 requests at 20 a page. **The archives verify anonymously, so the repository stays public** (§7 item 128). **Every run of the reward book's archive makes one Release and one tag — eight a day** (§7 item 177). |
| **sandbox limit — destructive actions** | Claude Code's permission classifier on the host refuses, on some days and not on others, `kill`, `rm -rf` of a tree, `systemctl enable --now`, `systemctl kill`, a `reclaim`, a `cp`/`mv` deploy chain and a read right after a refusal — "[Unauthorized Persistence]", "[Production Deploy]", "[Irreversible Local Destruction]", "[Interfere With Workloads]", "[Auto-Mode Bypass]" or no reason — and Claude Code's own safety check refuses a loop of removals over shell variables before it runs; refusal is not predictable (§7 item 138). **TZ-46 was refused nothing:** `systemctl disable --now`, `install`, `daemon-reload`, `systemctl restart`, `systemctl start --no-block` and `reclaim` with its `rm -rf` and `git worktree remove` all ran in the session. **Nor was TZ-49**, over `ssh` on the live host: `systemd-run`, `install` and `systemctl reload ssh.service`, `systemctl stop` of a timer, `sysctl -p`, `systemctl restart systemd-journald`, `systemctl disable --now rsyslog.service` and `rm -rf`, and on the capture host `reclaim`, `rm -rf` and `git worktree remove`. **Nor was TZ-50**: B-ENV's `pip`, `gh api -X POST` of Pages, `reclaim`, `rm -rf` on both hosts and `git worktree remove`. **Any TZ that must stop, signal, deploy or remove keeps the fallback: it hands the Boss ONE paste for the whole sequence, beside the Executor's own attempt, and verifies the outcome from the logs, `test -e`, `sha256sum`, `systemctl show` and its own modes, never from his account** (§7 items 124, 138, 140 and 144). |
| **harness — background output** | Claude Code keeps its own copy of each background command's output under the session's directory, `/tmp/claude-0/-root-btc-5m-twap/<session>/tasks/`, beside the scratchpad; the next TZ's B-RECLAIM-SCRATCH removes it with that directory once no running `claude` process made it (§7 items 91 and 95). **What a session prints, Claude Code keeps** in its transcript under the sessions' configuration directory, `/root/.claude-8j`, so a TZ's print prohibitions bind the Executor's own reads (§7 item 118). **The Executor's session is spawned by a remote-control `claude` process** — `claude remote-control --name BTC-5M-TWAP-VPS --spawn=same-dir`, under tmux session `crypto-rc` — and runs as `claude.exe --print --sdk-url …`; it makes two directories at its start and one more at each restart of its container, which loses its background waits; the remote-control processes, `1738600`, `1738611` and `1738619`, run since 10:28:51 to 10:28:53 UTC on 2026-11-15, and the two directories born with them read live (TZ-49 report §2.11); **a block handed to the Boss runs in his login and ends with it** (§7 item 124) — **but one that waits for him outside his terminal runs in a tmux server of its own**, as TZ-51's B-OWNER does, `tmux -L btc-l1`, which outlives a dropped connection and ends with the paste or at `timeout`'s bound; its TZ reads the server gone and removes its socket (§7 item 189). **The map is read in parts:** the contract's §1 step 2 reads §0 and what the TZ's header names (§7 item 174). |

Not decided by any TZ and therefore not present: the Parquet decision journal and any deployment of the engine. The
capture units are the recorder's, TZ-20's, and the reward book's, TZ-33's; the pair book's, TZ-26's, and the chain
book's are disabled; the reward book's archive's timer is TZ-46's file on TZ-34's service, and the pair book's
archive's timer is disabled; the advisor's bot's unit is TZ-35's and the liquidation guard's TZ-54's, neither of which captures anything. **Capture retention is fixed:**
nothing captured is deleted but by an archive's proven move to a Release or a TZ that names it; a TZ's
`/root/tz<NN>-work/` is reclaimed by its own last step, except what a committed artifact names by hash and no public
Release holds, which is copied to `/root/btc-forensics/` first (CANON hard rule 15).

---

## 7. Open defects

**Open and watched items**, newest first, as revision `2026-11-18-a` wrote them, with a state note where a later
fact moved one, item 184, found auditing TZ-48, item 185, auditing TZ-49, items 186 to 188, writing TZ-50, and items 189
and 190, auditing TZ-50, item 191, auditing TZ-51, which moved item 190, and item 192, auditing TZ-52 — items 181 to 183 closed by TZ-49;
items 184, 186, 187, 190 and 192 moved by revision `2026-11-21-c`, writing TZ-53; items 193 and 194, auditing TZ-53; items 195 to 197, auditing TZ-54, item 197 closed and items 195, 196 and 198 moved or added auditing TZ-55; items 199 to 203, writing TZ-56;
then **every closed item whose decision binds
a later TZ**, by its number, with the rule it leaves; then the closed items that leave none. A closed item's
whole account — the defect, the run that showed it, the ruling — is in revision `2026-11-17-a`
(`git show 5ef5ee2:SYSTEM-MAP.md`) and in the report it names. **A TZ cites an item by its number here, and the
Executor reads every item a TZ's header names, in full** (contract §1 step 2).

### Open and watched

| # | defect | disposition |
|---|---|---|
| 203 | **Polymarket's listing of a day moves after the day.** Gamma's keyset listing of the markets ending 2026-11-12, read on 2026-11-22, held `26,237` markets, every document `version` `v1`; read again on 2026-11-27 it held `28,777`: `2,532` `v2` documents — the Protocol V2 pilot, its soak-test series `polyv2-soak-…` and its pilot listings `polyv2…`, every one closed on 2026-11-12 and none listed on 2026-11-22 — and `8` more `v1` markets, closed from 2026-11-25 to 2026-11-27, two weeks after their end. A frame read at another time is another frame, and a rehearsal's counts move with it. Found by the Architect re-reading the rehearsal's day for TZ-56. | **open, for TZ-56:** its Polymarket frame keeps a market only where its document is `v1` and it closed by a fixed instant — `2026-11-23 12:00:00 UTC` for the set, `2026-11-27 00:00:00 UTC` for the rehearsal's day — and G-REHEARSAL compares no count those two rules leave to the venue, `late` and `version`. **A later frame of Polymarket's fixes its own instant the same way.** |
| 202 | **Kalshi's API from the capture host is measured by no one.** The Architect's session reads it (§6, Kalshi's public API); Kalshi's member agreement restricts members located in Poland, Bulgaria and Ukraine among 55 jurisdictions (CANON PART II, the candidates), and whether its public data answers an address in Poland is unread. | **open, for TZ-56:** its probe makes one request per endpoint first and BLOCKS on any refusal, printing the venue's words; nothing of K0's days is read before it passes. |
| 201 | **Gamma's documents of closed markets are not records of their terms.** Their `feeSchedule` carries the venue's current rates (§6), and on 2026-11-12 `14,111` of `24,577` closed markets carried no volume field, `1,272` of them crypto Up/Down markets that traded. Found by the Architect writing TZ-56. | **decided, TZ-56:** a Polymarket reading counts the fee its market's document states at the run, named so, and a Kalshi reading its series' fee at the run; no Polymarket frame filters by volume; a market is drawn and its fills read. |
| 200 | **L1 stopped on its fixed loss at 01:45 UTC on 2026-11-22, and its unit's defects** (CANON §1.5, from the venue's public trades and the wallet's positions; the unit's journal not read): a fill read from the venue's trades list once and at once, so partial fills not yet listed went unrecorded — the venue lists 13 fills of 2026-11-21 where the unit counted 11, and its holdings, its equity and its position cap ran wrong, 25 shares held against a cap of 20; and a market leaving the day's selection never quoted again, not even to close, while it counted against the eight positions. The positions are held to settlement, the Boss's to sell or hold. | **closed for L1, binding the next live unit** (CANON PART IV): a fill is known by the order's matched size in the wallet's open orders and by the balances, the trades list read again until it lists the trade; every position keeps its exit; a live unit's every read of the venue is proved against the venue's lag (CANON PART VI). Items 176, 178, 186, 187 and 194, written for L1's measurement, bind a later live step only where its TZ names them. |
| 199 | **This map ran behind the CANON from L1's stop to this revision:** revision `2026-11-22-a`, written for TZ-55's verdict hours after the stop, still read L1's unit running and L1 open. Found by the Architect writing TZ-56. | **closed by this revision.** |
| 198 | **The guard's prove accepts an answer a little past its `900` s** — `ask` tests the wait before each long poll of `25` s, so an answer read in a poll begun before `900` s is taken, up to about `925` s; TZ-55's G-LOOK read PASS at `901` s (its report §6 item 2), against TZ-55 §1.7's "within `900` s". The code is the Architect's, the words were wrong. **And its prove leaves the positions unwatched while the Boss answers** — `1,133.939` s at TZ-55, fifteen minutes of it on G-LOOK — because one poller of the bot runs at a time. | **Open, watched.** A later guard TZ states the wait as the code runs it; and **its prove reads the positions and rings their stages itself through its waits**, so that no answer leaves them unwatched. |
| 196 | **The guard's second version — the Boss's specification, 21:28 UTC on 2026-11-21, decided by the Architect and built by TZ-55.** His points: a profit alert once the price is `7`% beyond the entry, green for a long and red for a short; the margin hint aimed at `5`% from the price; three stages of liquidation alerts; an acknowledged alert meaning he is at work, with no call to distract him; and the alerts redesigned. | **Built: TZ-55, 2026-11-22.** The decisions are TZ-55 §1's; the Boss confirmed the examples' look at G-LOOK. **No alert can know the top:** the gain alerts mark records and retreats and claim nothing of what comes next. The guard still never trades, adds margin or holds a key that can (CANON PART VII). |
| 195 | **The dead-man's address was added after TZ-54's report**, outside any TZ — relayed by the Boss at 21:28 UTC on 2026-11-21. | **Read by TZ-55:** `hc-url` `kept` by its `secrets`, `0600`; the first version's `status` read `dead_man True`; G-HC answered `OK`, and the prove kept it quiet through its waits — `17` pings. **What healthchecks.io does when the host dies — its period, grace and the Pushover integration's priority — is the Boss's account and read by no TZ.** |
| 194 | **L1's loss limit counts each held position at the touch, so a fill moves the equity it reads at once** — by the size times the distance from our price to the best bid that remains, the touch's half-width or more where the taker swept the book. Seen at TZ-53's audit, in the Boss's Telegram screenshot of the unit's first fill on 2026-11-21: its first fill alone moved that equity by about a tenth of the limit, no loss realized [one fill; no price of it is printed here]. With up to `8` markets holding a minimum size each, marks alone can reach `25` pUSD and stop the unit on a day it has realized none of it; a stop holds until `clear-stop` on the host. Found by the Architect auditing TZ-53. | **open, for L1's measurement TZ, which decides before its days:** whether the limit stays at the touch — the liquidation value, the Boss's risk as CANON PART IV fixes it — or is read at the reward band's midpoint with the touch's difference counted apart, and what a stop costs its days; any change is new code's prove, in that TZ. Until then the limit stands. |
| 193 | **L1's unit's small defects, found at TZ-53's audit** — none changes an order or a stop. (1) The unit's gzip files, `select/<D0>.replies.jsonl.gz` and `polls/<day>.jsonl.gz`, are written `0644`, where TZ-53 §2 item 4 said `0600`, and systemd's `service.log` is `0644` — each inside `/var/lib/l1-bot/`, `0700`, root's (TZ-53 report §6 item 5). (2) The engine's self-tests remove their own trees and not `/tmp/l1-bot-selftest/` itself, left empty on the live host (item 4). (3) The unit's first start sent the Boss a day's report for 2026-11-20, a day it did not run, all zeros; and the drill's stop message printed the equity as unread. Found by TZ-53's Executor and by the Architect from the Boss's chat. | **open, for the next revision of `engine/l1-bot.py`:** its gzip writers open `0600`, its self-tests remove `TEST_ROOT` too, and no day before its first start is reported; the next TZ on the live host removes `/tmp/l1-bot-selftest/`. |
| 192 | **The CLOB answered a just-placed order's read by id with `null` (TZ-52, 2026-11-20).** The session key's post-only buy for the bot's wallet read `live` in `127` ms; `get_order` by its id a moment later was answered `null`, which the client refuses to parse (`UnexpectedResponseError`) and `roundtrip_flow` did not catch; its `finally` ran `cancel_all`, `canceled` `1`, `not_canceled` `0`, and `mode_roundtrip`, which writes its record only after the flow returns, wrote none (TZ-52 report §1 and §2.1). Whether a read by id serves a Deposit Wallet's order at all, or lags the engine, was not read; the self-tests' stand-in answered `404` alone. Found by TZ-52's run. | **decided, for L1's unit TZ:** the unit knows its orders by the wallet's open-orders list read by its key, and its fills by its trades and its balance, never by a read by id alone; every read after a write tolerates the venue's `null` or absence within a stated bound and prints the venue's raw answer; a flow's record is written on every exit; the stand-ins answer `null` where the venue was measured answering it. The order path's decisive part is measured — the placement live, the cancellation served; its read-back is proved by the unit's own code before the unit starts (CANON hard rule 14). *State at revision `2026-11-21-c`: TZ-53's unit and its prove carry it — no read by id; its self-tests' stand-in answers `null` to one and asserts that none is made (TZ-53 §1.4 and §1.5).* *State at revision `2026-11-21-d`: measured — TZ-53's prove saw each order in the wallet's open orders within `5` and `2` reads and gone within `2`, on CTF and negative-risk markets (TZ-53 report §2.3).* |
| 191 | **A refusal of the venue was logged without its words, and a step rested on a venue behaviour never measured (TZ-51).** `approve_flow` logged the relayer's `400` and not its message, so the cause was read only by a probe outside the TZ; and a bounded approval through the relayer was the Architect's assumption, with no fallback decided before the run. Found by TZ-51's run. | **closed by rule, TZ-52:** every refusal of the venue is printed in its own words, its hexadecimal strings and UUIDs masked (`said`); the self-tests' stand-ins refuse what the venue was measured refusing; a step that rests on a venue behaviour not yet measured names in its TZ, before the run, what the run does if the venue refuses it. |
| 189 | **The Boss's terminal was never a terminal before he used it (TZ-50).** TZ-50's `Tty`, its Appendix A line 1446, opened `/dev/tty` with `"r+"` in text mode; Python's `"r+"` builds a `BufferedRandom`, which needs a seekable file, and a terminal never is one, so `io.UnsupportedOperation: File or stream is not seekable.` stopped B-OWNER's first mode on both of the Boss's runs, 07:55:10 and 08:00:57 UTC on 2026-11-20, before any question — nothing typed, signed, sent or spent (TZ-50's report §1). Its self-tests, `135` and `31` checks, drove every one of the Boss's modes through `FakeTty`, a stand-in, and the hook's pure decision on the terminal's open; none opened a terminal. Re-derived by the Architect under Python 3.12.3. Found by TZ-50's Executor; its class named by the Architect auditing it. | **open, for TZ-51 and every later TZ — the rule:** **a mode that asks the Boss anything is run by its instrument's self-test at a real pseudo-terminal, on the host that runs it** — a child process whose controlling terminal is a new pseudo-terminal, its `/dev/tty` that terminal and its log a pipe, the parent typing each answer once the screen shows its question — never through a stand-in alone; a hidden answer asserted never echoed and absent from the log; and the Architect runs that test on a copy with the defect put back and records that it fails. **A block of the Boss's that waits for him outside his terminal — a signature in another app of his phone — runs in a tmux server of its own on the capture host**, `tmux -L <name> -f /dev/null -u new-session -A -s <session>`, so that a dropped connection leaves its question standing and the same line attaches again; bounded by `timeout --foreground`, its server read gone and its socket removed by the TZ's own closing step. TZ-51 carries both (its §1.0 and §1.10). |
| 190 | **The venue's relayer approves an exchange at MaxUint256 alone — measured, TZ-51, 2026-11-20.** TZ-51's `approve` asked the owner to sign a Deposit Wallet batch of `approve(exchange, 1,000,000)` for each exchange whose pUSD allowance was above `1` pUSD — both stood at the maximum polymarket.com set when it enabled trading — and the relayer refused each of four signed batches with `400`, `call blocked: call[0] blocked: approve to exchange 0x… must be MaxUint256`, read by a probe outside the TZ (TZ-51 report §1, §2.2 and §3 item 1). The venue's documentation lists `approve(spender, amount)` among a wallet batch's permitted calls and does not state the rule. The bound TZ-50's audit set, `1` pUSD an exchange, cannot be set through the venue's route; an approval of a lower amount is refused, whoever signs it. | **decided, TZ-52:** the allowances stay at the venue's maximum, and an approval, where one is ever short, asks for MaxUint256; G-APPROVE and G-READY read each at least one order's cost. What a stolen session key could spend is then the wallet's balance: the bot's wallet holds what the Boss entrusts to L1, and L1's unit TZ fixes its loss limit and revises CANON PART IV, whose bound of `1` pUSD binds an allowance the owner signs — no TZ of this project signs one below the maximum. *State at revision `2026-11-21-c`: CANON `2026-11-21-a` PART IV revised — the allowances at the venue's maximum; L1's risk the wallet's balance, from `80` to `150` pUSD at its unit's first start, read by G-READY, and the unit's loss limit, `25` pUSD below its start equity (TZ-53 §1.2).* |
| 185 | **The live host's commands print in Russian.** TZ-49's B-SSH and B-CONFIGURE printed `ls -la` with Russian month names — `ноя`, `июл`, `мар`, `авг`, `окт` — and its §3.9 printed `date` as `Чт 19 ноя 2026 14:08:51 UTC`, where the capture host prints `Thu Nov 19 01:55:47 PM UTC 2026`: the live host's locale is not the capture host's [its `LANG` not read]. No reading of TZ-49 parsed a localized field — its instrument parsed `/proc`, files, `systemctl show`, `timedatectl show`, `sshd -T` and the journal's JSON — so every gate stands. Found by the Architect auditing TZ-49. | **open, for every later TZ on the live host and for L1's unit:** a command whose output is parsed runs under `LC_ALL=C`, and its block says so; the next TZ on the live host prints its `locale` once. |
| 186 | **Polymarket Protocol V2 reaches the markets this project reads** [read by the Architect from `docs.polymarket.com/migrate/polymarket-v2/overview`, `/sdk-integrations` and `/trading/place-orders`, 2026-11-19 and 2026-11-20; not measured]. Phase 1 from Monday 2026-11-23, 08:30 Eastern: BNB, DOGE, HYPE, SOL, XRP and ZEC Up/Down at five and fifteen minutes, and three temperature markets; **Phase 2 from Tuesday 2026-11-24: BTC and ETH Up/Down at five minutes, fifteen and four hours, other crypto, the remaining weather, commodities, finance and minor sports**; Phase 3 from Tuesday 2026-12-01: soccer, American and college football, basketball, tennis, esports and social counts. A V2 market's book returns `version` `"v2"`; its orders trade its `positionIds`, signed under domain version `"3"` for the V2 exchange `0xe3333700cA9d93003F00f0F71f8515005F6c00Aa`, and need pUSD approved to it; a CTF market's, version `"2"` for the standard exchange `0xE111180000d2663C0091e4f400237545B87B996B` — the venue's table, and the client `0.20.0`'s `exchange_v3` and `standard_exchange`, which chooses by an asset ID's reserved bits. **Many of rule W's reward markets move in Phases 2 and 3.** Whether the reward book's capture (TZ-33) records a V2 market's books, under which IDs, and whether rule W's selection and replay read them, is read by no one. Found by the Architect writing TZ-50. | **open, for L1's measurement TZ — re-scoped by revision `2026-11-21-c`, writing TZ-53:** before it is written, a TZ reads, on a day after 2026-12-01 and by the streams' identities and counts alone — no price, size, rate, competitiveness or outcome of a reserved day (§5, the reward book's days) — whether the reward book records V2 markets' books whole and whether rule W's selection and replay read them. **L1's unit reads neither:** its books come from the venue's market channel, its orders sign each market's own version, and it quotes a kind only once its prove's round trip on that kind has read PASS — a V2 kind is proved by new code's prove, in a TZ of its own (TZ-53 §1.6). |
| 187 | **The venue's fees and rebates change at 2026-11-20 23:59 UTC** [read by the Architect from the venue's changelog of 2026-11-16 and `docs.polymarket.com/programs/fee-and-rebate-changes-november-2026`, 2026-11-19 and 2026-11-20; not measured]. Taker coefficients by category — `0.05` for BTC five- and fifteen-minute Up/Down, `0.01` for all other crypto, geopolitics free; **maker rebates leave the daily market-wide pools for tiers of 30-day maker weighted volume, `shares × price × (1 − price)` summed: none under `200,000` USD, then `3`, `7`, `10` and `15%` of the taker fees a maker's fills generate**; liquidity rewards unchanged. **L1's quote, far under `200,000` USD, earns no rebate**: its income is the liquidity rewards alone. TZ-45's EARN stands: its `pess` variants, which its reading took, carry the rebate at `0` [its report, `logs/80-score.log`]. Found by the Architect writing TZ-50. | **open, for L1's unit TZ and its measurement:** no rebate is counted in a P&L of L1 unless the venue's payouts to our address show one; CANON §1.1 and §1.7 carry the new terms from revision `2026-11-20-a`. *State at revision `2026-11-21-c`: TZ-53's day report shows the venue's payouts as paid and counts no rebate it did not pay (TZ-53 §1.7).* |
| 188 | **RTDS, now PolyBolt, asks for a Chainlink API key from 2026-11-30 00:00 UTC** [read by the Architect from the venue's changelog of 2026-11-16, 2026-11-20; not measured]: every price subscription names its provider, and one Chainlink serves — the TWAP topics `btc-recorder` subscribes to among them — sends a Chainlink API key. `btc-recorder` sends neither, so from that instant its RTDS stream may stop; no open question of this project reads it — every track it served is closed (CANON PART II). Found by the Architect writing TZ-50. | **watched:** the first TZ on the capture host after 2026-11-30 reads whether the recorder's RTDS stream still records, and the Architect decides then whether the recorder keeps running; nothing of L1 depends on it. |
| 184 | **Telegram is L1's control panel — the Boss's specification of 2026-11-19, decided here.** His words: "Telegram will become the control panel: reports will be delivered there, and there will be a "stop" button, like in the advisory bot. But Telegram itself does not place orders." No file held it before this revision: no TZ, no row of this map and no line of CANON `2026-11-16-a` names a control path for L1, and TZ-47's and TZ-48's §2 forbid touching any Telegram token. | **open, for L1's unit TZ, which builds it — decided:** L1's unit reports through **a Telegram bot of its own**, not the advisor's — one token serves one poller of `getUpdates`, and the advisor runs on the capture host — its token on the live host in a file of its own under `/etc/`, `600`, root's, written by the Boss alone and never printed, hashed or copied, its chat pinned as the advisor's is (§2.7), answering that chat alone. **Reports:** each start and stop, every fill, each day's rewards and rebates as the venue paid them beside the replay's, its position, its marks and its loss against the limit its TZ fixes, and every geoblock read that is not PASS. **One command acts, «Стоп», a button of its reply keyboard:** the unit cancels every open order of its key, writes a stop record that holds across restarts and boots until it is cleared on the host, and exits with a status its unit does not restart; the loss limit and a geoblock read of `blocked` stop it the same way. «Статус» reads and changes nothing. **No message places, sizes, prices or moves an order, or starts the unit:** a start is made on the host — by a TZ's block or the Boss's paste — and the session key's revocation from the Boss's own device stays the last stop of every order path (CANON PART IV). The stop's round trip — the button pressed, every open order cancelled, the unit down — is proved at the minimum size before rule W quotes its first day. **TZ-51 writes the bot's token and pins its chat, by the Boss's `/start` alone, and sends it one message — the round trip's report; it starts no poller** — TZ-50's part, which BLOCKED before it (item 189). *State at revision `2026-11-21-c`: built by TZ-53 (its §1.3) — the reply keyboard «Стоп» and «Статус», the stops and reports above; the day's replay beside the venue's payouts is L1's measurement's, which needs the capture's day whole, not the unit's.* *State at revision `2026-11-21-d`: proved and running — G-STOP, the Boss's «Стоп» in `7.1` s, every order cancelled and read gone; G-HOLD, a start under systemd with the stop record standing, exit `3` and no request (TZ-53).* |
| 179 | **The recorder stops itself at its self-cap, and its unit does not restart it.** `check_floors` stops it once the apparent bytes of its own tree reach `SELF_CAP_BYTES`, `4,000,000,000` (`research/recorder/config.py` line 22; `recorder.py` lines 291 to 303), read at the close of every interval: it opens no interval, closes the open ones and exits `0`, which `RestartPreventExitStatus=0` leaves down, and a start above the cap refuses. Its tree held `1,657,840,396` bytes by `du -sb` at TZ-46's close and grows `26,784,064` apparent bytes a day (TZ-09): the cap falls about 2027-02-12 [modelled]. Found by the Architect writing revision `2026-11-18-a`. | **Watch:** no open track reads the recorder (CANON PART II). A TZ that needs it past that date, or frees room by its store (item 175), first moves its closed intervals to Releases by an archive's proofs, as the pair book's and the reward book's archives move theirs (CANON hard rule 7); nothing captured is deleted but so (§6). |
| 178 | **The reward book halts on its write cap, and a halt is not restarted.** `account` adds every byte one process writes but its stream files and raises `FloorStop` past `WRITE_CAP`, `1,000,000,000` (`research/tz33-reward-book-capture.py` lines 193 and 418 to 423); `guarded` turns it into a `halt` record and a stop, the service returns `1`, and `RestartPreventExitStatus=1 2 3` keeps it down. The count is the process's own and is printed only in its `stop` record. The process running since 2026-11-14 06:11:44 UTC, pid `1556307`, reaches it about 2027-01-14 at TZ-33's `16.3` MB a day and about 2027-01-21 at TZ-46's `14.6` [modelled]. Found by the Architect writing revision `2026-11-18-a`. | **open, before L1's measurement days:** the TZ that fixes those days places them where no halt can fall — a restart of the unit at a slot's boundary, and the package manager's (item 176), start a new count — or first measures the count, as the byte counts of the files the process wrote outside its streams since its `start` record. |
| 177 | **Every run of the reward book's archive now adds a Release and a tag — eight a day.** At TZ-46's audit `origin` carried 168 refs, 33 of them `rewardbook-streams-*`; at eight a day those tags pass 300 within five weeks, and a TZ that prints every ref line, as TZ-46's §0.5 and §3.1 did, 162 lines each time, prints them all. | **open:** a later TZ's refs read prints counts by prefix and every line that differs from the last audit's, never every tag; a mode that lists the Releases derives its request bound from the tags' count at 20 a page (TZ-46's `forensics`: 93 Releases, 6 requests). *State at revision `2026-11-20-b`: TZ-50's `refs` printed counts by kind, 189 lines; 196 lines, 57 of them `rewardbook-streams-*` tags, at the Architect's read of 17:04 UTC on 2026-11-20.* |
| 176 | **The package manager restarts the captures.** `unattended-upgrade` upgraded `libc6` from 06:11:34 to 06:11:40 UTC on 2026-11-14, and the recorder, the reward book and the advisor entered `active` from 06:11:41 to 06:11:44 UTC (TZ-46's report, §1) — by every sign needrestart's restarts: `/etc/needrestart/conf.d/` holds its README alone, and the first 20 lines of `needrestart.conf`, as TZ-46's host gate printed them, name no unit of this project [the rest of the file and the journal not read]. A restart splits the slot it falls in across two processes; that slot's gap decides whether it is whole, and a day is kept by its longest run (CANON hard rule 8). | **open, before L1's measurement days:** a TZ keeps needrestart from restarting this project's units — one drop-in under `/etc/needrestart/conf.d/` naming them, read before and after, nothing of another project changed — or L1's measurement fixes before its days what such a restart costs. `apt-daily-upgrade.timer` fires about 06:00 to 06:30 UTC. |
| 175 | **The room's horizon, measured at TZ-46's close.** The margin over `STREAM_FLOOR` and `PEAK` was `2,908,396,574` bytes at 17:02 UTC on 2026-11-17. Beside the streams this project's stores grow about `50,000,000` bytes a day — the reward book's other files `14.6` MB a day over TZ-46's session against TZ-33's `16.3`, the recorder's `33,632,842` (§6, capture cost) — and the disk's other tenants at no rate this project has measured: about two months at `43,500,000` a day and 15.5 days at the fastest drain §6 records, `187,760,570` [modelled]. | **Watch:** every TZ that touches the host prints the margin — free space and the reward book's stream files, less `7,300,000,000` and `445,535,636`. *State at revision `2026-11-20-b`: TZ-50's margin `2,797,417,277` at 06:21:25 UTC on 2026-11-20 (TZ-50 report §2.4).* **Below `1,000,000,000`, or before L1's measurement days where it would fall below that inside them, a TZ frees more.** The next lever is `STREAM_FLOOR`, whose derivation named the pair book's room (TZ-33 §1), now stopped — a lower floor in the reward book's frozen code costs one restart onto new code; then the recorder's store, `1,657,840,396` bytes at TZ-46's close, a capture of its own. |
| 161 | **What TZ-42's PASS did not establish is still unread.** That the 00:10 and 15:07 UTC checks fire on the unit's own clock under this code: no report has read the bot's `check` records since the replay of 2026-11-05 20:36:06 UTC — TZ-41's and TZ-43's host gates read the unit, pid `284419` and `NRestarts` `5` on 2026-11-08 and 2026-11-10, and not its journal. That Telegram shows the command menu: `getMyCommands` returned 0 commands before the restart, and none has read it after. That a new signal is opened, sized and announced on a live day: none was on 2026-11-05, and the self-test's synthetic market alone proves it. And the registry is on the host alone: its coins, prices and candles are printed in no report, so the Architect has re-derived no signal of it. | open: **the next advisor TZ's host gate reads H7 over every `check` record from the replay — each slot once, stamped at or after its instant, 00:10 and 15:07 UTC — and the registry's chain from its genesis, and its probe reads `getMyCommands`**; until then the Boss's own chat is the evidence that the checks arrive. A reading of the registry's outcomes, where one is ever wanted, publishes the registry and the candles it was walked on as a Release (CANON hard rule 16). |
| 147 | **Binance's archive holds no daily file of 2026-10-28**, the first close of the advisor's forward record (CANON PART VII): the daily klines files of BTCUSDT and ETHUSDT for that day answer `404` and none of the 42 coins has a candle of that day in the archive, read 2026-11-01, while 2026-10-27, 10-29 and 10-31 are served; October's monthly file is not yet out. A re-derivation of a close after 2026-10-27 from the archive's daily files carries a hole on the forward record's first day — the Architect's check of TZ-40's day bridged it by interpolation and read the same two STRONG coins as the host's live data. | open: **a TZ that re-derives a forward record or an audited close from the archive reads October 2026 from its monthly file, and BLOCKS where a day of the record is absent from it** — a forward record read on a filled hole is not the record. |
| 139 | **The map is read in sections.** TZ-37's Executor read the map's §0, the start of §1, §2.7, the end of §3, §6's rows and §7 items 125 to 137, and its fingerprint rows in full, against contract §1 step 2's "in full": the map is `1,971` lines and `478,552` bytes. The reads before §0.0's `mkdir` — the listing, `git log`, `hostname`, `uptime -s`, `ls -d` of four paths, `df`, `systemctl is-active` — were read-only. | open: **a TZ's header names the map sections it rests on, and the fingerprint reads every row**; contract §1 step 2's wording is amended in the next TZ that may move anchor `A4`. *State at revision `2026-11-18-a`: the contract's §1 step 2 was amended with `A4`'s move in revision `2026-11-17-a` (item 174); the rule stands.* |
| 138 | **The harness's permission classifier refused three of TZ-37's blocks to its Executor, and the Boss ran each:** B-RECLAIM-SCRATCH's `reclaim` (no explanation), B-DEPLOY's copy chain (no explanation) and B-KILL's `systemctl kill` ("[Production Deploy]"), each before it ran, where TZ-36's Executor ran all three forms; the Boss's runs came 26, 8 and 2 minutes after the refusals, and the Executor appended UNIT-NEW's timed reads to his B-KILL paste so that §3.5's schedule held. Every outcome was verified from the logs, `test -e`, `sha256sum`, `systemctl show` and the checker's own modes, never from his account. His terminal wrote an OSC 133 marker (`ESC ] 133 ; C BEL`) at the start of the first log a paste appended to; no reading parses a log's first line. The classifier has now refused `kill`, `rm -rf`, `enable --now`, `reclaim` and a `cp`/`mv` chain, and let each of them through on other days (§6). TZ-38's `reclaim` was refused again, as "[Irreversible Local Destruction]", and the Boss ran it 19 minutes later. | open: **a TZ that deploys, signals or removes gives the Boss ONE paste for the whole sequence — the copy, the signal and the timed reads of the unit, in order, each gated on the one before it — beside the Executor's own attempt, and a refused block is handed over unchanged**; CANON hard rule 14 states it. |
| 137 | **The host's `MemAvailable` ran below a floor derived from a peak (TZ-36).** The printed read at TZ-36's §0.3 was `158,494,720` bytes, the gate's `189,366,272` in the same seconds, the closing read's `197,439,488`; TZ-35's reads ran from `263,163,904` to `363,487,232` (item 131). The floor, `170,344,448`, is twice the Architect's `85,172,224` peak, not a headroom: the host has `1,002,127,360` bytes, one processor and `849,932,288` bytes of swap in use. | open: **a TZ states which read its memory floor is asserted on, and reads it again before blocking on a first read below it** (TZ-36 did, and passed); TZ-22 sizes the units against `memory.stat`, not peaks (item 88). |
| 136 | **The advisor's unit was stopped and started three times on 2026-10-30, by no TZ:** 09:04:03, 09:21:35 and 09:23:02 UTC, the shape of a manual stop and start (`Stopping … Deactivated successfully … Started`), new pids `3402846`, `3404640` and `3404850`, `daily-sent 2026-10-30` at each and no daily sent again; the code was TZ-35's (the service copy's and the unit file's hashes equal at TZ-36's host gate). `NRestarts` read `0` at TZ-36's gate where TZ-35 left `1`. Who ran them is not readable to the session; two scratch directories were born at 09:04:06 and 09:04:08 UTC. | open: **`NRestarts` is a count since the unit's last start, never a lifetime count** (§6, process supervision: a stop and start resets it); a TZ's host gate reads the service copy's hashes, not the count. |
| 135 | **Binance's public archive holds no daily file for 2026-10-28.** For all 42 perpetuals the daily files of 2026-10-27, 2026-10-29 and 2026-10-30 are served and 2026-10-28's answers `404`, 42 of 42 on each of the four days, read by the Architect on 2026-10-31 at 07:18 UTC and again at the audit; for BTCUSDT the 1h, 4h, 5m and 1m files of 2026-10-28 answer `404` too. 2026-10-30's file, not yet served at the first read, was served at the second. CANON PART VII has an Executor re-derive the forward record from the archive, and its first day is the missing one. | open: **the forward record's reading takes 2026-10-28 from `fapi.binance.com`** — the same closed candles as the archive on every day both hold (TZ-35's G-SAME, 546 of 546) — **and first reads whether the archive has published it**; the PIT and market records' readings (CANON PART VII) take it the same way, for the positions their first November carries from the closes of 2026-10-28 to 2026-10-31. |
| 131 | **The host's peaks run above the Architect's measurement of the same code (TZ-34).** The Architect measured TZ-34's modes under Python 3.12.3: the run `36,327,424` to `36,560,896` bytes, `first` `34,308,096` to `34,754,560`, `fingerprint` `38,481,920` to `38,789,120`, `still`, `timer`, `final`, `stopped`, `installed` and `mark` `32,129,024` to `32,976,896`, `selftest` up to `60,338,176`. On the host the same bytes peaked at `39,477,248` for the run, `37,810,176` to `40,452,096` for the session's modes and `61,313,024` for `selftest`. Every floor held — `MemAvailable` never read below `263,163,904` — but the run's own floor, `73,121,792`, is `1.85` times its host peak, not twice. TZ-35 took its floor from the larger, `170,344,448` bytes, twice the Architect's `85,172,224` for `adv3.py --history`, whose host peak then read `72,032,256`. | open: **a TZ that derives a memory floor from a peak takes the larger of the Architect's measurement and the host's last measured peak of the same code** (§6, memory). |
| 129 | **B-ENABLE's `enable` (TZ-34) set off no run of the pair book's archive**, where item 115 expects one 600 s after every reload. TZ-34's B-INSTALL `daemon-reload` at 07:49:22 UTC set off the run of 07:59:22, and its B-ENABLE `enable --now` at 08:17:05, 18 minutes after that run, set off none: `list-timers` read the next elapse 2026-10-30 03:00:20 UTC at 08:17:38 and at 09:32:14. TZ-33's B-ENABLE, 4 h 46 min after the run before it, set one off. **TZ-35's two reloads set off none either:** its B-INSTALL `daemon-reload` at 14:35:11 UTC and its B-ENABLE `enable --now` at 14:38:10, the pair book's archive `failed` since its deferral of 08:02:57 (item 128); `list-timers` read that archive's next elapse 2026-10-30 03:00:20 UTC at 14:35:17, 14:44:39 and 14:57:01. **The same reloads re-armed the reward book's archive's `OnActiveSec=1800`:** its next elapse read 15:05:11 after the first and 15:08:10 after the second, and its tag `rewardbook-streams-1793286490` stands, a run begun at 15:08:10 UTC — a reload's, not its calendar's. Which reloads re-arm `OnActiveSec` is not measured. | open: **a TZ's timeline states a run 600 s after each of its reloads as possible, not certain, and its gates count the archive's runs from its ledger and its tags, never from the reloads** (item 115); **the same holds for the reward book's archive, 1,800 s after a reload**, whose runs restart nothing but move its streams and add a tag. The next TZ that touches the host reads run `1793286490` from that archive's ledger. **Moot since TZ-46** (item 166): neither archive's timer is started by a reload. |
| 128 | **The repository served no Release without a token for about an hour, on 2026-10-29.** TZ-34's `path` read `tz-01a-dataset`'s Release anonymously at 07:48:27–30 UTC; the pair book's archive's run of 07:59:22 exited `75`, deferred, at 08:02:57, by every sign for this cause — its reason in an `archive.log` TZ-34 could not open; TZ-34's first run uploaded its 86 assets with the credential and deferred in its anonymous verify at 08:51:11, `release_by_tag` reading `404`; a diagnostic `path` at 08:53:42 found no Release; the Boss stated that he had set the repository public again, and `path` was served at 09:00:51. Both archives depend on it: each verifies every asset through the API's record and a full download without a token, and the third deferral of one set halts its archive and disables its timer. | open: **the repository stays public** — a private repository defers every run of both archives. The pair book's archive's set `1793260762`, deferral `1`, is resumed by its calendar run of 2026-10-30 03:00:20 UTC, which the next TZ that touches the host reads from that archive's ledger; TZ-35 read its four records unchanged at 14:15, 14:23 and 14:56 UTC, the service `failed`, `Result=exit-code`. |
| 120 | **The package manager restarts both capture units.** `unattended-upgrade` stopped and started the recorder and the pair book at 2026-10-22 06:14:07–10 and 2026-10-23 06:08:56–58 UTC (TZ-31 report §2.9). A stop and start resets `NRestarts`, so this map's counters are not lifetime counts, and a G-STILL whose span holds such a run reads FAIL with no fault of the TZ; the window a restart falls in loses its stream. | open: recorded (§6, process supervision); **a G-STILL names the cause from both units' journal**, which TZ-32 §3.11 reads. |
| 115 | **The archive runs off its calendar with no boot.** Six times: 2026-10-15 06:18:30, 2026-10-17 08:35:37, 2026-10-19 21:54:19, 2026-10-20 11:23:37 and 2026-10-21 21:39:04 UTC — read from the ledger by TZ-30 — and 2026-10-22 06:24:08, `1792650248`, read from its tag; each the timer's 600 s elapse after a start of the timer, where `journalctl --list-boots` shows one boot since 2026-08-02 07:24:34 UTC. TZ-30's host gate found the timer's journal since 2026-10-14 empty, and the package manager's history quiet near all but 2026-10-15's, whose `unattended-upgrade` runs ended from 06:09:16 UTC, 46 s after that run's start less 600 s. No TZ ran at any of them. Each restarted the pair book inside its band and completed, so none cost a window; the cause was then unknown. | **measured, 2026-10-28: a reload of systemd — `daemon-reload`, or the one `systemctl enable` and `disable` make — re-arms the timer's `OnActiveSec=600`.** TZ-33's B-INSTALL reloaded at 06:34:32 UTC, the timer's next elapse read 06:44:32 at 06:42:20, and run `1793169873` began at 06:44:33; its B-ENABLE's `enable --now` at 11:30:15.68 set off run `1793187616` at 11:40:16. TZ-31 had read the same 600 s after `crypto-deploy.service`'s bursts of `daemon-reload` and after the package manager's restart. Each run restarts the pair book inside its band and costs no window, and **TZ-30 to TZ-33's G-STILL counted the pair book's restarts the archive's ledger records as its own.** open: every TZ that installs, enables or disables a unit sets off a run 600 s later and states it in its own timeline (item 125); a TZ that touches the archive's timer drops `OnActiveSec` or keeps it for this reason in its own text, and a new timer — the reward book's archive's — does not take it unexamined. TZ-34 examined it and kept `OnActiveSec=1800`; and not every reload sets a run off — TZ-34's `enable` set off none (item 129). TZ-46 removed it from the reward book's archive's timer and disabled the pair book's archive's timer (item 166). |
| 114 | **TZ-29's push through `gh`'s stored login.** `git push -u origin` failed — `fatal: could not read Username for 'https://github.com'` — and the branch and the report were pushed through `credential.helper=!gh auth git-credential` to the same repository, `score`'s check that `origin` carries `HEAD` passing. **The Executor's diagnosis, the token in `origin`'s URL "most likely revoked or expired", is not established:** the archive's run of 2026-10-20 03:00:20 UTC uploaded and verified 20 assets with that same credential, 85 minutes before the failed push, and every git request now prints `warning: redirecting to https://github.com/seahomebatumi-ai/btc-5m-twap.git/`, which no earlier report shows — a redirect drops a credential embedded in a URL. **Its advice, that the Boss replace or remove the token, is not followed:** with no token in the URL the archive falls back to `gh auth token` (`research/tz27-pairbook-archive.py` `credential()`, lines 725 to 739), never proven under systemd. | open: TZ-30 pushed through `gh auth git-credential`, as TZ-29 did, and the archive's runs still upload under the URL's token — the credential of its latest three `upload` records, to 2026-10-22 03:01:03 UTC, is "the primary checkout's remote URL"; TZ-31 pushes the same way; nothing touches the token. |
| 113 | **Reconnects without transfers.** Window `1791731700`, TZ-28's G-RESUME window, streamed in 2 segments with no request of the archive inside its seconds 595 to 905, and window `1791725400` streamed in 2 before TZ-28 ran. Item 109's idle stretch is therefore not proven to remove the reconnect it was built against; one processor, and frames stamped when the pair book's event loop takes them (§6, CLOB websocket). | open, for B3: **B3's measurement reads every window's segments, whatever the archive or a TZ did**; and a TZ that makes heavy requests from the host holds them to the idle stretch and times each into its record, as TZ-29 does its fetch. *State at revision `2026-11-18-a`: B3 is closed and the pair book stopped; both archives still hold their requests to its idle stretch by the clock (item 109).* |
| 101 | **The chain book's record has two limits.** It holds 6 incomplete windows in B2's span, 5 of them besides the stop window `1791017100` — `1790193600`, `1790328600`, `1790550900`, `1790820900` and `1790833500`, their reason unread, as TZ-24 §2 item 3 required — so B2's set held 1,079 members, not the 1,084 TZ-24 §1 recorded. And seven snapshots a window, 20 to 60 s apart, cannot show how long a violation lasts or how many fall between checkpoints. Neither is a defect: the chain book records what TZ-18a fixed. | open, and answered by B3's capture, which runs since 2026-10-10 19:30:06 UTC (TZ-26): every change of the four books from `T+595` to `T+905` beside the same seven checkpoints; B3's measurement re-reads completeness over its whole set first. |
| 90 | **The recorder writes a restart's gap only if its first RTDS connection succeeds.** `rtds()` takes the `startup` gap's start from `last_frame_ns` before its first connection (line 535 at `4216c04`) and writes the record on the first success; a failure replaces both — the start becomes the failure's own instant and the reason `reconnect` (lines 560–566) — so after a restart whose first connection fails, the outage from the last frame to that failure is in no record, and a window that ends inside it can read `complete`. No restart has met it; found by the Architect writing TZ-21, whose G-RESTART would read FAIL on it. | open: fix in the next TZ that changes `recorder.py` after TZ-21 — keep the gap's start until a frame has been received — with a self-test of a failed first connection. |
| 28 | `tz06-calibration.build`'s set-size assert message names `SET_SIZE` where the run may now pass a different `need`. Disclosed by TZ-08a §11 item 4; exact at the default, which every run to date has used. | open. Fix in the next TZ that touches that file; do not edit the committed report. |
| 17 | **`analyze.py`'s `V5_determinism` fell from 215 of 215 to 0 of 215.** Rebuilding a 2026-09-10 manifest with today's `manifest.py` adds the two keys TZ-05a introduced; every field the old manifests carry rebuilds identically. | open. Repaired by rule in the next TZ that touches `analyze.py`: a determinism check compares a rebuild against a rebuild, never against an artifact written under an older schema. |
| 1 | `research/tz02-distribution.py` records the collector-hash comparison into `checks["collector_sha_matches"]` but never asserts it. The run completes on a mismatch. | open. Fix in the next TZ that touches that file; do not edit the committed report. |

### Closed — the rules they leave

| # | the rule it leaves |
|---|---|
| 197 | **A guard's unit file keeps `UMask=0077`.** The first version's `service.log` read `0644` (TZ-54 report §6 item 10); TZ-55's `UMask=0077` and B-DEPLOY's `chmod` closed it — `service.log` and `memory.json` `-rw-------` at its close. |
| 183 | **Root on the live host logs in by key alone**, since TZ-49: `/etc/ssh/sshd_config.d/00-btc-5m-twap.conf`, sorted before the provider's `01-xserver.conf`, sets `PasswordAuthentication no`, `KbdInteractiveAuthentication no` and `PermitRootLogin prohibit-password`, read at `sshd_config`'s `Include`, its line 12, before that file's own `PermitRootLogin yes` at line 42; G-SSH 6 of 6, `publickey` alone from outside. **A change to `sshd` is armed against itself:** a transient guard restores the last state unless a new connection by the key confirms the change, and a block that fails after arming it restores it at once. The Boss reaches the host by `ssh live-host` as root on the capture host, or by the provider's console. |
| 182 | **A configuring block reads what the host already carries before it adds anything, and a gate asks for the state the block leaves, never a path it assumed.** TZ-49 adopted the image's `/swap.img`, already `0600` and root's, wrote no swap file, set `vm.swappiness` `10` from its own drop-in and bounded the journal by a drop-in sorted after the provider's `cap.conf`: G-SWAP 7 of 7, G-LOG 6 of 6. |
| 181 | **A gate reads the paths an order can take, and a refund is decided on what the venue read.** IPv4 alone, carried by the process: every socket of the live host's instruments and of L1's unit `AF_INET`, every name resolved in `AF_INET` alone, the audit hook refusing an `AF_INET6` socket and a lookup in any other family, and IPv6's state printed from the kernel's tables with no IPv6 socket opened — TZ-49's `policy`. L1's unit reads the geoblock over IPv4 at every start and stops on `blocked` (item 184). TZ-49: G-GEO PASS, `BG`; the hook refused nothing in any live mode. |
| 180 | **A host gate compares only what a read of that host printed, in the form it printed it, and a host name by its first label** — never the full name, its provider's DNS record, which publishes the address. TZ-47 BLOCKED on it, its LH1 against `vs-2348.` and the provider's domain; TZ-48's LH1 to LH5 read 5 of 5. |
| 174 | **A TZ's header names every map section, row and item its run rests on** (item 141); the Executor reads §0 and those in full, and any other passage where the TZ cites it — contract §1 step 2, `A4` `6ac6e10aeabc` since revision `2026-11-17-a`. |
| 172 | **L1's choice of markets leaves, before any order, a market whose question names a dated event that can fall inside the day**, by a rule its TZ fixes: the selection leaves a market by its end date and its tags, not by the date of an event its question names (TZ-45's audit). |
| 171 | **An instrument sums money in rationals or under a 50-digit `Decimal` context (`C50`)**, never under the default 28 digits (TZ-45's `day_money`). |
| 170 | **Before L1's measurement days the capture keeps every slot's stream**, because L1 compares the venue's payouts with a replay of the same days; what frees room is measured, never assumed, and nothing of another project is touched. Resolved by TZ-46; watched by item 175. |
| 169 | **L1's steps, each a TZ of its own, in order:** the capture's room (done, TZ-46); the live host — the venue's geoblock read from its address before any key exists (done, TZ-49, the host prepared), then one order's round trip at the minimum size from it (CANON PART IV) — TZ-50, BLOCKED at the Boss's terminal (item 189), and TZ-51; rule W live as a unit, its whole loss fixed in its TZ — TZ-53, G-DEPLOY PASS, running since 2026-11-21; and its measurement, fixed before its days, of the venue's payouts to our address against the replay of the same days. |
| 167 | **A TZ's `reclaim` copies no file whose bytes a public Release holds by the SHA-256 its report names, and names the Release instead** (CANON hard rule 15); a forensic copy a Release holds is removed only once the Release's record and a full anonymous download prove it (TZ-46's B-FORENSICS). |
| 166 | **A TZ's clock rule keeps a unit of work away from a *running* archive, not from the calendars alone.** No enabled timer of this project carries `OnActiveSec`, so no reload starts a run; the pair book's archive's disabled timer keeps `OnActiveSec=600` in its file — **a TZ that enables it removes that line first.** |
| 165 | **A wait block reads every count it prints after its last sleep, in one command**, and a TZ says in its text whether a wait may run in the background inside a loop of the Executor's own. |
| 164 | **A rule explored on a set already read is fixed in a TZ's own text before any day it is gated on is read, and gated on those days alone** (CANON PART VI); a replay's EARN opens a live step of a fixed loss and proves no income, because the replay cannot see an order our own quote calls out. |
| 163 | **No order of ours can open from the capture host** (§6, venue geoblock); a live step runs from an address the venue does not restrict, and the TZ that deploys it reads that address the same way before anything else; the capture is not touched by it. |
| 160 | **A deployment TZ's `deploy` mark reads the memory and disk floors again itself**, so a session resumed hours after its host gate deploys on a floor read in the same minute; a bot logs `setMyCommands`' success as well as its refusal. |
| 159 | **A TZ that replaces a `frozen` row is not uploaded while another uploaded TZ waits to run**; where it must be, its verdict names the report its merge and its revision wait for, and every revision shipped in between carries the pull request's row as open (CANON hard rule 17). **A host gate that reads the advisor reads the service copy's `commit.txt` against the head it expects.** |
| 157 | **An instrument prints one summary line for every timing file its TZ's §8 names.** |
| 156 | **A memory floor is twice the larger of the measured host peak and the peak modelled at TZ-37's ratio, `1.199`**; for a mode that holds a set the modelled one is not slack (item 131; §6, memory). |
| 155 | **A market's reward terms move between days and inside a day, and the venue serves no history of them:** a day's terms are what a capture stored that day, and a quoting rule reads a market's minimum size and maximum spread from each served poll's row, never from the day's selection (CANON §1.7); rule W leaves a market for the day at the first poll whose terms differ (§2.6). |
| 154 | **A TZ whose reading rests on an input the repository and its Releases do not hold publishes that input as a Release in its own run** (CANON hard rule 16). |
| 151 | **An instrument prints its peak, its `malloc tuned` line and its counts of opens in a `finally`, on every exit**, so a mode that BLOCKs still yields them. |
| 150 | **A TZ's `scratch` lists the directory that holds the session's own, `$(dirname "$(dirname "$S")")`**, and its B-RECLAIM-SCRATCH reclaims every directory its `scratch` names earlier. |
| 149 | **A resumable step reads "at least 600 s apart", and its last try may wait, at most 6 h, until GitHub's status page reads an incident of unauthenticated traffic resolved; every download stays anonymous** (TZ-43 §3.5). |
| 148 | **A walk whose next candidate has not ended starts from a band late enough to absorb a non-member for each incident the capture has shown**, and a rule is never bent to the day that failed (CANON hard rule 8). A change to TZ-33's capture that reconnects a socket silent for 8 s is a later TZ's, never inside a set's span. |
| 145 | **A TZ that times a mode for its host peak runs it under the wrapper inside the paste as well**, so a refused block still yields the peak item 131 asks for. |
| 144 | **A paste's own reads are the gate's reads** — the Executor verifies them from the logs it wrote, and a TZ asks for no re-read of the same modes after a paste; a read needed later is a step of the paste. |
| 143 | **A band that must be clear of the package manager's morning run opens at 07:30 UTC**; a block that must start earlier waits, in its own text, until `systemctl list-timers apt-daily-upgrade.timer` shows its elapse past and `systemctl is-active apt-daily-upgrade.service` reads `inactive`. |
| 141 | **A TZ's header names the map sections its C8 row cites, copied from that row.** |
| 140 | **A block handed to the Boss holds back only the steps that read what it changes:** a TZ names them, and the Executor runs the others meanwhile. |
| 132 | **No TZ makes a step of the Boss's a precondition of `EXECUTE`.** A credential or any other hands-on step of his sits inside the run at the point that needs it: the Executor hands its exact command over there once, in plain words, waits for its result with a bound the TZ states — reading a credential's file by its mode, owner, size and type alone — and BLOCKS at the bound; no host gate reads it. |
| 127 | **A TZ's §0.5 BLOCKs where `CryptoTZ/` on `main` holds another file whose name begins with its own `TZ-NN-`, or `CryptoReports/` a report whose name does** (CANON hard rule 2). |
| 125 | A TZ that reloads systemd states each archive's possible run in its own timeline (item 115) — **moot since TZ-46** (item 166): no enabled timer of this project is started by a reload. |
| 124 | **A block handed to the Boss (1) is handed over only once its band is open, so its own wait is seconds; (2) is one command line, every destructive step chained by `&&` to the assertion it depends on; and (3) appends its output to its log under a `date -u` line, never overwriting it.** |
| 123 | **A mode that holds the set is measured at the set's size before its floor is fixed.** |
| 121 | **TZ-32's G-BOOK, kept by TZ-43's and TZ-45's, compares the touch — each best price and its size — at no fewer than 99 in 100 match frames**, and prints the every-level count beside it, barred. |
| 119 | **No `reclaim`'s output is filtered.** |
| 118 | **A TZ's print prohibitions bind the Executor's own reads** — no file of the work tree is printed, whole or in part, but by a command the TZ names (§6, harness). |
| 116 | **A projection names every quantity it depends on.** |
| 110 | **A TZ that asks for a unit's files names the read in its §2, or asks for nothing beyond what §2 allows.** |
| 109 | **Every request an archive makes starts at second 15 or later of a 900-s window and is budgeted to end by second 590, its bytes at `2,000,000` a second and 5 s beside them, and each is timed into the run's record**; a request that does not fit waits for the next window. Both archives' code holds it by the clock (`idle_wait`), the pair book stopped or not. |
| 107 | **A count of files a mode removes names the store it counts.** |
| 106 | **A bound a TZ states on a store is stated as its code evaluates it — when it is read and from what — and a TZ that changes the store re-reads the bound the way the code does; a deadline is taken from the first bound that stops what the deadline protects.** |
| 105 | **Every figure a TZ's §8 asks for is printed by its instrument, and a population an instrument reads is printed whole, each unit with why it did or did not count.** |
| 104 | **A block timed to a band waits for that band in its own text**, so whoever runs it — Executor or Boss — cannot run it outside the band (CANON hard rule 14). |
| 102 | **A report quotes verbatim the output of every check run after B-RECLAIM-OWN, and B-RECLAIM-SCRATCH reads "one `I reclaim` naming every earlier directory".** |
| 100 | **A venue property is recorded with the instant it was read at; a stored venue body is re-verified by the values it carries, never by its hash; and a TZ that needs the bodies keeps them as served.** |
| 99 | **An instrument does no `Decimal` arithmetic in a worker thread unless that worker sets its own context, and its self-test asserts the precision in the thread that does the sums.** |
| 98 | **A TZ names `S` as "the scratchpad directory the session's system prompt names", and the fingerprint is a mode of the TZ's instrument, and it asserts.** |
| 97 | **A peak that grows with the population is measured at the population's size, or bounded per member and extrapolated** — C4's upper bound applied to memory. |
| 96 | **A set's exclusions are derived from every artifact that read or printed an outcome** — §5's table and every report — never from one table; a figure is quoted as its instrument printed it. |
| 95 | **The next TZ's B-RECLAIM-SCRATCH removes a finished session's directory, and with it the harness's copy of its background output, once no running `claude` process made it** (§6, harness). |
| 94 | **No shell command opens or lists anything under a capture root but those the TZ's §2 names.** |
| 93 | **A memory floor is twice the largest peak of the instrument's modes, its margin stated, and each mode that reads the venue or the capture re-reads `MemAvailable` at its start** — the peak taken as items 131 and 156 say. |
| 92 | **Every read a Validation row asks for is quoted from the mode's own print statements before the TZ is sent** (C7; item 84). |
| 91 | **A TZ's `scratch` names each directory live — born from 1 s before to 60 s after the start of a running process whose `argv[0]` is `claude` or ends in `/claude.exe` — or earlier, and its `reclaim` refuses a live one**; a finished session's pair is reclaimed by the next TZ. |
| 89 | **A TZ creates its work tree before its host gate, so every output lands in it; its `reclaim` copies nothing of a worktree that holds exactly its pushed `HEAD`, which `git worktree remove` then removes without `--force`.** |
| 88 | **A memory ceiling is derived from the measured peak of the process it bounds, and only once that process's memory is bounded** (CANON hard rule 9); the recorder's and the chain book's ceilings are TZ-20's assumption, and no unit's has been sized against `memory.stat` (item 137). |
| 87 | **A venue mechanic a track depends on is re-read from the venue in the TZ that depends on it.** |
| 86 | **Host identity is fixed facts of the host — paths, filesystem, records; whether a process runs is a state each host gate states for itself** (CANON PART III; §6). |
| 85 | **Every long-lived process runs as a systemd system unit**, never under a login session, `nohup`, `setsid` or a terminal multiplexer, its restart policy and its stop fixed in the TZ that deploys it (CANON hard rule 14). |
| 84 | **A run order commits the instrument before the first run whose output a Validation row compares; every read a TZ asks to be reported is one its run mode prints; a readiness condition is stated on the set rule's own count, or named a necessary condition beside the sufficient one asserted on the members; and a TZ that forbids the code after its label read to raise provides, inside the instrument, a rehearsal of that code on an already-scored span with synthetic labels.** |
| 83 | **After a TZ's label read, nothing its data can trip raises** — every later quantity is total, and where it is undefined the report says why; and **a behaviour a self-test asserts lives in a pure function the self-test calls with literals.** |
| 82 | **A value quoted from a report is quoted only from a figure its instrument printed** — the printing function read and named — never from one the report's author composed; where the instrument wrote the quantity to a file located by hash, the check is equality with that file's value (CANON PART VI C2). |
| 81 | **A hunk map is stated at `-U0`**; what the host holds is read on the host by the TZ that states it. |
| 80 | **An as-of instant is never earlier than an event its stopping condition observed** — the check's clock is rounded up, not down — and the proof runs only once the clock is past it. |
| 79 | **After any new commit, every figure a report states about its artifact is recomputed from the head it names; every run whose outcome a TZ fixes has a V-row.** |
| 78 | **A clause that reads BLOCKED binds whatever caused the failure, the Executor's own code included**; a TZ that wants a defect fixable inside the session says so, before its first venue request only, and requires the copy and R0 repeated on the new commit and both commits disclosed. |
| 77 | **A TZ's prohibitions bind every request of the session, the Executor's own included** — a diagnosis the TZ does not provide for is a BLOCKED report, never a request — and no pass computes a gated statistic before the commit that computes it is pushed. |
| 76 | **The prohibition list is intersected with every output the body requires by content class — a price, a label, an outcome, a settled document — as well as by path** (CANON PART VI C1); **an identity check on a process is equality with the exact argv.** |
| 75 | **A TZ that starts a long-lived process first issues one live request per endpoint through the process's own request function, asserted served and parsed, fixes every header of it, and names the process's stop on every FAIL** (CANON hard rule 14); **evidence that the venue serves a request is cited with the whole request — method, URL and every header.** |
| 74 | **A figure a report states about its own data is computed from that data by the instrument, never written from memory**; a process-identity condition matches the whole command line exactly. |
| 73 | **Every count and every "not yet" this map or the CANON states is re-read at each revision from the artifact it describes, and one that was not re-read is deleted rather than carried.** |
| 72 | **Every assertion a Validation row fixes names the runs on which it must hold; a count of files on the host is read by the TZ that states it, never carried from a report; a literal handed to an exact comparison is written in the type the comparison uses.** |
| 71 | **A gate that assumes independence across units measures the dependence on the null's own residual**, on a set whose labels are already read and before any label it judges is read, and derives its critical values under that dependence; the direction a dependence moves a reading is derived, never asserted. |
| 70 | **An audit requirement names the route by which each input reaches the Architect; where none exists, the report prints what the re-derivation needs.** |
| 69 | **A gate whose two answers each close its question reads each from its own exact test**, each at a false-reading probability fixed before any label is read; power sizes the set before any label is read and decides nothing after one is (CANON PART II). |
| 68 | **A venue constant is recorded with the instant or the population it was read over, and is never written as a constant of the market unless a measurement along the market's own time axis says so.** |
| 67 | **Epochs are the authority, and every membership and span is re-derived from them; a total printed beside a breakdown is computed from that breakdown by the instrument that prints both, and asserted equal to it.** |
| 66 | **CANON PART VI C5 is performed literally** — every count anywhere in a row re-derived from the section that defines it — and **every check a Validation row calls asserted has a numbered step in the run order.** |
| 65 | **A constant a TZ selects from a population statistic is fixed by a prior, named pass or by a literal, never by the pass it governs** — or the TZ states that every branch is computed and the choice made after. |
| 64 | **A statistic over a population on which its quantity can be undefined states whether an undefined value leaves the denominator, and prints the count of undefined units beside it.** |
| 63 | **A TZ that scores out of sample prints the instant its scoring commit reached `origin` beside the instant of its first outcome read.** |
| 62 | **Every cost is computed at the population's upper bound**, a filtered population at its unfiltered size, over the union of C6's populations, every fail-fast bound derived term by term beside it (CANON PART VI C4). |
| 60 | **Power qualifies a silence, never a failure** (CANON PART II). |
| 59 | **Every behaviour a TZ attributes to a committed function is quoted from its body** (CANON PART VI C7). |
| 58 | **A count of qualifying units is produced only by the committed set-formation code, named by function in the sentence that states the count**; a directory listing, a file count and a calendar filter are never that instrument. |
| 57 | **A replicate whose fitted parameter lands on a search bound is censored, not averaged.** |
| 56 | **A gate that compares an estimated probability against a floor states the replicate count that makes one standard error small against the floor's margin, and a reading whose confidence interval straddles the floor is UNDECIDABLE.** |
| 55 | **The map's branch list is read with `git ls-remote` at each revision; every `/root/tz<NN>-work/` a TZ leaves behind is named in the next TZ's retention section until `test -e` shows it gone; and no statement about a regime is written without the measurement that makes it.** |
| 54 | **A TZ that scores out of sample states that no pass reads a test-set label until the commit that scores it is pushed; smoke passes run on the fit set.** |
| 53 | **Every count a C5 line states names, beside it, the table or line of the artifact it was counted from.** |
| 52 | **A cost bound is derived from the maximum of the population it bounds, never from a mean.** |
| 51 | **A TZ whose rule filters a scored population states, in the gate, what each statistic reads when the filtered population cannot support it.** |
| 50 | **Nothing eligible reads UNDECIDABLE** (item 49). |
| 49 | **A gate states, before any label it judges is read, its false-failure probability — family-wise over every `tau` and set — and its power against a named alternative; a gate without that power reads UNDECIDABLE** (CANON PART II). |
| 48 | **Every count a Validation section states is re-derived from the sets §3 defines, and every statistic names its population** (CANON PART VI C5 and C6). |
| 47 | **Every check whose cost grows with the data states its cost; above `3,600` s of single-session compute it is sampled or becomes its own TZ** (CANON PART VI C4). |
| 46 | **For every file a TZ calls additive, the replaced committed lines are named** (CANON PART VI C3). |
| 45 | **An expectation whose value depends on a quantity the same TZ measures is forbidden; it is written as an inequality** (CANON PART VI C2). |
| 44 | **A TZ's §2 prohibition list is diffed against every path and entry point its own body names before it is sent** (CANON PART VI C1). |
| 43 | **A TZ that requires a committed function to run with a substituted dependency authorizes an additive keyword parameter on that function, named in its scope section, whose default reproduces the committed behaviour byte for byte**; substitution at run time is never the design. |
| 42 | **A numeric expectation is an inequality on a named quantity with an explicit bound and explicit units**; a phrase about decimal places never appears in a `## Validation` section. |
| 41 | **A statistic measured over more than one set is reported per set before it is reported pooled.** |
| 40 | **A statistic a verdict table reads is bounded on the set it is read over, and a ratio is used only where its denominator is bounded away from zero by the gate's own construction**; otherwise it is a diagnostic, said so in the row that defines it. |
| 39 | **A prohibition in a scope section is checked against every committed entry point the TZ calls before the TZ is sent, and a TZ that names a committed function states its signature as the file has it.** |
| 38 | **A TZ that names a committed measurement as a reproduction target writes the exact expression that produced it and the identity linking it to what the instrument computes.** |
| 37 | **A fixed literal is computed from an implementation independent of the one under test, at a precision better than its tolerance by at least a decade**, the reference named and the margin stated. |
| 36 | **A causality check names the causal quantity it tests — never a realised outcome — and its exempt quantities; a perturbation boundary is "strictly after the last instant the tested quantity may read", carried into every later TZ that reuses the check.** |
| 35 | **A TZ's scope section names every repository path its body requires it to change, and any `frozen` row it moves by path.** |
| 34 | **A self-test for a replacement implementation never uses the implementation it replaces as its reference in the region that motivated the replacement.** |
| 33 | **A fixed numeric expectation is computed before it is written, never bounded by eye, and the TZ states how it was cross-checked.** |
| 32 | **A proof that code cannot perform an action enumerates its delegation paths — `subprocess`, `shell=True`, external binaries — as well as the in-language APIs.** |
| 31 | **A preservation rule states what an aggregate hash over several files names; where it names nothing, deleting any member is authorized only by a TZ that says so in exact counts.** |
| 30 | **A window that must characterise an intermittent consumer is at least as long as that consumer's measured idle-to-active period, or the TZ states that its figure is a lower bound.** |
| 29 | **A rate measurement of a shared resource subtracts the measuring run's own footprint from what it attributes, and reports that footprint separately.** |
| 27 | **A fitted statistic a gate bounds is reported together with its value recomputed without its single most influential observation.** |
| 26 | **A specification that fixes a likelihood over `Phi` fixes its tail-accurate `log Phi` in the same section.** |
| 25 | **A headroom figure is derived from the measured rate of change of free space over a stated wall-clock window, never from any one process's write rate** (§6, headroom). |
| 24 | **A guard on an implementation shortcut samples across the scored set and includes the pathological members by construction.** |
| 23 | **A scope prohibition names, in its own section, the checks exempt from it.** |
| 22 | **A scale estimator is justified by a distributional assumption, and the report that freezes the estimator reports the check of that assumption.** |
| 21 | **A summary table reporting two estimators reports eligibility per estimator.** |
| 20 | **Every `tau` a gate scores carries a measured constant.** |
| 19 | **A correction is measured on the exact random variable it divides, never substituted from a proxy horizon.** |
| 18 | **After every upload the Architect reads `origin/main` and confirms the file that landed before `EXECUTE` is sent.** |
| 15 | **Every calibration gate carries a scale statistic and a shape statistic, both fixed before any data is seen.** |
| 14 | **Section numbers are asserted unique in the pre-delivery change list.** |
| 13 | **Membership is re-derived by the Architect from epochs rather than read from the report.** |
| 11 | **Deployment and measurement are separate TZs wherever wall-clock time must pass between them** (CANON hard rule 11). |
| 9 | **A text search cannot prove the absence of a capability;** the standing carrier is the merge-base diff plus the absence of any CLOB authentication path. |
| 8 | **A requirement is a count of qualifying units, never an unbroken run** (CANON hard rule 8). |
| 7 | **A re-execution never reuses a report path** (CANON hard rule 4). |
| 6 | **Every resource floor is stated in exact bytes derived from §6** (CANON hard rule 9). |
| 3 | **An implementation reaches `main` only by a merge after a verdict** — the contract's §4.1 and its §4.2 self-check. |
| 2 | **A committed report is never amended** — the contract's §3.2 and §5.2; both versions stay in history. |

**Closed, leaving no rule beyond the CANON's or the report's:** items 173, 168, 162, 158, 153, 152, 146, 142, 134, 133, 130, 126, 122, 117, 112, 111, 108, 103, 61, 16, 12, 10, 5, 4.

---

## 8. What does not exist yet

No validated link — Phase 1 can only fail to disqualify one — no measured edge for a taker or a maker on the
five-minute market, and **no income measured**: L0's EARN on rule W was a replay's, and L1, rule W live, stopped on its
fixed loss in seventeen hours (CANON §1.5; §7 item 200). **No order of ours is open:** L1's unit is stopped on the live
host, its stop record standing; the recorder and the reward book read, and the advisor's bot holds no exchange key and
reads nothing of the Boss's account. **The liquidation guard reads the Boss's own Binance positions** on the capture host
since TZ-54, by a key that can read alone, and trades nothing; its second version runs since TZ-55, 2026-11-22.

**Not built, and each a TZ of its own:** K0's reading (TZ-56) and H0's (TZ-57); a live step of either track behind its
own gate (CANON PART II).
