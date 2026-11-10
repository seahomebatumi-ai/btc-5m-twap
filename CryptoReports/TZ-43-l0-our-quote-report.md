# TZ-43 — L0, our quote on the venue's reward markets — REPORT

**Status: L0 reads UNDECIDABLE** (TZ-43 §4.5). Every gate before the reading passed.
- **`pess`** makes every assumption the stream cannot settle against us. It reached `θ = 10` USDC on **2 of the 8 days**; **its least day was 2026-11-07, `−77.856494508104` USDC**.
- **`opt`** makes every one for us. It was at or above `θ` on **all 8 days**; **its most was 2026-11-03, `622.046581446444` USDC**.
- So **EARN does not hold** — a `pess` day is below `θ` — and **NO EARN does not hold** — no `opt` day is below it.

Every day's money and its four parts, as `I score` printed them, in USDC. Each is a sum over the day's 150 members. **The marks are a proxy**: each member's position at the day's end is valued at the day's last midpoint, or at its outcome where its document reads it resolved.

| day | `pess` money | reward paid | reward before the 1-pUSD minimum | rebate | marks (proxy) |
|---|---|---|---|---|---|
| 2026-10-31 | `-11.259858540405` | `84.146601459595` | `99.927429049452` | `0.000000000000` | `-95.406460000000` |
| 2026-11-01 | `68.086470405581` | `80.195760405581` | `102.765165164257` | `0.000000000000` | `-12.109290000000` |
| 2026-11-02 | `-43.567466943315` | `44.546298056685` | `62.659029655028` | `0.000000000000` | `-88.113765000000` |
| 2026-11-03 | `1.949199283554` | `43.398049283554` | `60.962654370802` | `0.000000000000` | `-41.448850000000` |
| 2026-11-04 | `-47.702356068026` | `124.993498931974` | `142.645042948209` | `0.000000000000` | `-172.695855000000` |
| 2026-11-05 | `-49.808415665403` | `65.629349334597` | `80.080676216214` | `0.000000000000` | `-115.437765000000` |
| 2026-11-07 | **`-77.856494508104`** | `54.195040491896` | `71.996911033030` | `0.000000000000` | `-132.051535000000` |
| 2026-11-08 | `114.083108169877` | `90.640538169877` | `102.306046964609` | `0.000000000000` | `23.442570000000` |

| day | `opt` money | reward paid | reward before the 1-pUSD minimum | rebate | marks (proxy) |
|---|---|---|---|---|---|
| 2026-10-31 | `247.480311217417` | `346.144227879917` | `346.144227879917` | `2.623473337500` | `-101.287390000000` |
| 2026-11-01 | `370.592462656468` | `388.095510624093` | `388.095510624093` | `4.135402032375` | `-21.638450000000` |
| 2026-11-02 | `138.836970989877` | `235.013901637627` | `235.013901637627` | `12.158299352250` | `-108.335230000000` |
| 2026-11-03 | **`622.046581446444`** | `679.069607963544` | `679.069607963544` | `22.993428482900` | `-80.016455000000` |
| 2026-11-04 | `404.880926272849` | `487.841499369674` | `487.841499369674` | `71.904901903175` | `-154.865475000000` |
| 2026-11-05 | `232.893728616666` | `282.698784149066` | `282.698784149066` | `59.654989467600` | `-109.460045000000` |
| 2026-11-07 | `396.813963990171` | `569.624515167621` | `569.624515167621` | `33.386053822550` | `-206.196605000000` |
| 2026-11-08 | `466.729797195475` | `399.400720179450` | `399.400720179450` | `59.790012016025` | `7.539065000000` |

- **G-REHEARSAL: PASS**, on its first try: 451 lines, SHA-256 `1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd`, the Architect's.
- **G-SET: PASS.** 9 candidates considered, 8 members — 2026-10-31 to 2026-11-05, 2026-11-07 and 2026-11-08 — and 1 non-member, **2026-11-06**: slot `1793949300` (07:15 UTC), "stream: a gap above 15 s", the stall TZ-41 met. That is 1,200 member-days, 464 distinct markets and 768 stream files of 8,696,625,516 bytes.
- **G-BOOK: PASS**: the rebuilt touch equal to the venue's own book frame at **60,078 of 60,089** frames, `0.999817`, against `0.99`.
- **DETERMINISM: PASS**, **24 of 24** slot lines equal from a second download.
- **The instrument's commit on `origin`:** `ab0f3873a66eb302225c3849da362bfe301e93df`, read there at **`2026-11-10T07:54:46.835116063Z`**. The read ledger's first line, `rehearse`, is at 07:57:42 UTC, and its first `fetch` line at 08:00:39 UTC; both come after the commit.
- **G-STILL: PASS.** The recorder, the pair book, the reward book and the advisor were unchanged from 07:55:42 to 09:04:34 UTC.
- **The classifier refused one block:** B-RECLAIM-SCRATCH's `reclaim`, as "[Irreversible Local Destruction]". The Executor handed it over unchanged, the Boss ran it at 07:58:24 UTC, and it was verified from its log and by `test -e` (V16, V18). B-RECLAIM-OWN was not refused: the Executor ran each of its lines.
- **No single member's, fill's or poll's price, size, rate, competitiveness or outcome is printed here** (TZ-43 §2 item 10). Every figure is a sum over a day's members or over the set.

---

## 0. Fingerprint

`I0 fingerprint` (`logs/02-fingerprint.log`, 07:52:36 UTC) and `I fingerprint` (`logs/12-fingerprint.log`, 07:54:09 UTC) both printed:

```
FINGERPRINT PASS: revision 2026-11-08-a; anchors 6 of 6, 4 re-derived; rows 60: frozen 57 of 57 equal, tracked 2, reported 1
```

The two logs print the same rows; only their stamps and the peak line differ.

**Revision string:** `2026-11-08-a`, the revision TZ-43's header requires. **Anchors:**

| anchor | map | re-derived |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | — |
| `A2` — collector | `6c5089330629` | `research/twap-divergence.py` sha256[:12] `6c5089330629`, equal |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | — |
| `A4` — executor contract | `437b45ea196b` | `BTC-EXECUTOR-INSTRUCTIONS.md` sha256[:12] `437b45ea196b`, equal |
| `A5` — recorder | `0f6c90451cbd` | `research/recorder/recorder.py` sha256[:12] `0f6c90451cbd`, equal |
| `A6` — pricer | `729f0bcdbee3` | `research/pfair.py` sha256[:12] `729f0bcdbee3`, equal |

**The map's §0 table, every row as the instrument printed it** from the primary checkout at `main` `12fb07b`:

| path | lines | bytes | state | SHA-256 |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 2047 | 548314 | reported | `b8a0d7a056889e4840018b951dba8c5994413be198ecfa35ee89f12eb5f492dc` |
| `BTC-EXECUTOR-INSTRUCTIONS.md` | 234 | 11128 | frozen equal | `437b45ea196b9f0191f55e560321dd86f65699e386be56273d1a557e2266fb3b` |
| `research/twap-divergence.py` | 1135 | 50928 | frozen equal | `6c50893306292c74160c6c93e983d781225ad9a8cdd4fad725d8972deb31d473` |
| `research/selftest-twap-divergence.py` | 376 | 16736 | frozen equal | `ed22e52f6dc52b6f4a81d753e7a3371d12deab8197084dd5fc122c9ee41a094a` |
| `research/tz02-distribution.py` | 334 | 14511 | tracked | `f2ecd5c935a0d24f3bd5acff8d4eb282f8786dfbc617edb36de106880e294bc4` |
| `research/pfair.py` | 441 | 19357 | frozen equal | `729f0bcdbee3a6297783827353b7d1dc9aa9755217eaae36fa2cd6515873fb68` |
| `research/selftest-pfair.py` | 619 | 32559 | frozen equal | `b4420feb96027fc7aafef49f65388cf5add10e4b7464c9ddb91540584c7a83aa` |
| `research/tz06-calibration.py` | 577 | 27138 | frozen equal | `715b4ae0eb0ac1b5f4e2416bbcefceca3e6e82cb0a4472ba64bd74be5aae4e6f` |
| `research/tz07a-variance-time.py` | 623 | 28414 | frozen equal | `513e808811e630629b5b0df0a455cb94387b856b6b3e5ea691307c55e832c771` |
| `research/tz07b-settlement-dispersion.py` | 515 | 24926 | frozen equal | `424e07344d7401f6531cf1e9aa405edd1f4f82167bfc04169cfeb49dc2a988fc` |
| `research/tz08a-out-of-sample.py` | 745 | 38822 | frozen equal | `37001deff180bf2d18df93b2b8828840ca6ce6dc8f63cd797419d6b62dd57e5c` |
| `research/tz09-disk-inventory.py` | 894 | 41004 | frozen equal | `b2dabb6a2b196b86fba10517e9767170ee9fcd1639dc1fb946d02f45c9bc49b6` |
| `research/tz10b-sigma-or-link.py` | 1224 | 61018 | frozen equal | `406b6d1145f2a9aa2c23000eb0c5fd92c7aa8d6c2f6651908e68b24f2d77a088` |
| `research/tz11a-student-link.py` | 1231 | 64732 | frozen equal | `0f0525852e07c0dfc732f40e0545efea65e54085064e3d2814925465caf7c839` |
| `research/tz12-sized-gate.py` | 1157 | 61637 | frozen equal | `d2769c201932e2a6153ade06aca9aa6fab99016c4f7eabf5d6363a50f931c999` |
| `research/tz13-sized-gate-test3.py` | 1074 | 53901 | frozen equal | `a67b00c95974614e3c0e486b4d3a1b5109756a6d2a00832a8b9acb49c63fc3fd` |
| `research/tz14-quote-inventory.py` | 2124 | 109972 | frozen equal | `978ee4ff992730101e4b5133694b14942cd8cd750269ba1d26c9f077368c4a02` |
| `research/tz15-phase2-gate.py` | 1517 | 73799 | frozen equal | `66ac0ae0fdd2a4227fd39f1c014f1587a035fbc8e1e0007b5017a1d90dc56aa3` |
| `research/tz16a-phase2-decisive-gate.py` | 2198 | 111192 | frozen equal | `3cae67ee7a2174c244c0f9e8b786b4dac56351f41a54d6c9ece992d85c77a125` |
| `research/tz17-settlement-chain.py` | 1102 | 38622 | frozen equal | `e18834241760fe0bdf23fe1ccfd3fed855b75f56a614825c450964de0d28ca92` |
| `research/tz18a-chainbook-capture.py` | 1683 | 69517 | frozen equal | `e9cb9b478fe40e53c5109f1cc79b1cf9255c75e2ca32221f0df8b116f9579bae` |
| `research/tz20-capture-under-systemd.py` | 771 | 36528 | frozen equal | `104c93cee02820e6409777189ecc67ab20e4848f096108791b1ceeda094414a7` |
| `research/tz21-recorder-memory.py` | 1284 | 59009 | frozen equal | `d6d2dc195809f2160fda7856980d8ccfbf0006ba0836943ff789c877f9d5795f` |
| `research/tz23-maker-m0.py` | 1184 | 54885 | frozen equal | `6b3ace2c568129783b849c1edea02177be1adbad679a7a57c7d1dee00a3fe34f` |
| `research/tz24-nesting-b2.py` | 1535 | 76142 | frozen equal | `4e4022e65ecd14ed0df4b8eb583a03a348212a1c5c5b44a1785d8bf2ad943e5b` |
| `research/tz26-nesting-b3-capture.py` | 2492 | 118466 | frozen equal | `caed70d9c388c4d114cf65ade164cde7bb0c2d966e847234ce5a05613e9211ec` |
| `research/tz27-pairbook-archive.py` | 2078 | 106284 | frozen equal | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` |
| `research/tz28-pairbook-archive-timer.py` | 1438 | 74576 | frozen equal | `46a019d65eac961572d3260b5a3a8eaf3c0c173327bb984a3b51f88834ee23e4` |
| `research/tz29-maker-m0-second-look.py` | 1225 | 68959 | frozen equal | `18defff93d08c13ea4638a518c88a3fec5541fcf53fb6827451e727f2204d905` |
| `research/tz30-nesting-b3-measure.py` | 2518 | 131119 | frozen equal | `93dbbf1c4f84553a7bc041387ef92c3c0d8747c384d383b4fcd0b247fcd131ab` |
| `research/tz31-who-earns.py` | 1523 | 84775 | frozen equal | `7073188c8fbaa19568e8c6e4d6379e40ea57cf2a1341ebde0ea6a08f2c544765` |
| `research/tz32-our-quoting.py` | 2576 | 138209 | frozen equal | `6ec367e6ed995b315063d2d808dd6a3995878011afd76abfbb7b106b645a9c61` |
| `research/tz33-reward-book-capture.py` | 3542 | 175160 | frozen equal | `a276bbb9cce7c09b06a774f2decff9d19085fd75b70a9f595d06f40faa19e670` |
| `research/tz34-rewardbook-archive-timer.py` | 1791 | 99388 | frozen equal | `1d8aa514f6d3509f709b3349fba5b603fc80ecafc11e3f4a5d03a2e853539f72` |
| `research/tz35-advisor-deploy.py` | 802 | 42049 | frozen equal | `d50787db5113c3f748806a60a3e71211b665cb5235296e43d0e9a747a529e6f5` |
| `research/tz36-advisor-trust.py` | 582 | 32925 | frozen equal | `a0fb9d53afe435d37354862eb8fd299256bf551fdbdb25a5c828d2cc7376d4f5` |
| `research/tz37-capital-allocation.py` | 808 | 51269 | frozen equal | `eec1f30b971ed1d6db31e27eb0c321276c1b107a1654e013996d023b1a6a04eb` |
| `research/tz38-adv3-pit-validation.py` | 1782 | 90181 | frozen equal | `579474b65329662f7bed735994381241a928a2c65a726cec3f933dc7afd4427b` |
| `research/tz39-advisor-checks.py` | 1139 | 73892 | frozen equal | `18294b0916d77b226083a18f9521f06e2fddb423bbc947a2e1100fd42b2980f3` |
| `research/tz40-advisor-strong.py` | 1436 | 95474 | frozen equal | `4403b27185f7e9aaa090dedfca457af6c4f70b6b020f0d2fcd9f9fbb96b6054b` |
| `research/recorder/recorder.py` | 651 | 27821 | frozen equal | `0f6c90451cbd56c808392048e8c4e69ac177fc0237cadaefd4ab8bf579d252f7` |
| `research/recorder/config.py` | 112 | 4773 | frozen equal | `8111dfe473ee694fbe295cabd5fb47a8c9e56ac032ffebf42fd0167964e6181d` |
| `research/recorder/manifest.py` | 254 | 10002 | frozen equal | `79c99010a1c3e035a982a8c64dcf92afaf3ec956e3c3c4a2d354345dedb14045` |
| `research/recorder/analyze.py` | 813 | 34705 | frozen equal | `eb595cad79b089eea594d840d9d2f892ae857279a58e9f3d4a5036174aeff20d` |
| `research/recorder/probe.py` | 227 | 9324 | frozen equal | `50b8c269f671c09652a34a5acf3e1af1b398fb811b4d8afe704192c79e3a41c2` |
| `research/recorder/selftest.py` | 573 | 30591 | frozen equal | `c3d9d75d55c1c8a5035b95cd86a35983d9be0fa46a80c582589bafcc0e0a9a90` |
| `deploy/systemd/btc-recorder.service` | 23 | 707 | frozen equal | `3cd713fb0cca21851075820f631b64aee5f4f5808a4881c69749e253d42788a1` |
| `deploy/systemd/btc-chainbook.service` | 22 | 724 | frozen equal | `a7b042fee8f87d41da9937e46d4fb5bbb3424e17972bf1c3a71de1ebbd42bfb2` |
| `deploy/systemd/btc-pairbook.service` | 22 | 761 | frozen equal | `ba02fe4175b961c387ea8066eb084704e69efc7fd0a48d8f623a0198334f8dd8` |
| `deploy/systemd/btc-pairbook-archive.service` | 17 | 794 | frozen equal | `2e7fd45382af3da3b2ec29ced8d69870ef3d4481da4c6f327b90fc6cb5af78e7` |
| `deploy/systemd/btc-pairbook-archive.timer` | 13 | 417 | frozen equal | `07581f4f331fbf9d2a1113cac42a2872d65ac69a872991bff7d2bda235eac913` |
| `deploy/systemd/btc-rewardbook.service` | 23 | 817 | frozen equal | `7691720c7b2261a606af54bfa20b5068b89455ea54512c55dde861d6d8063bec` |
| `deploy/systemd/btc-rewardbook-archive.service` | 17 | 810 | frozen equal | `a9abb1f092b3fb8359d37ea88df00dca8557d0f0482d04c12f0fbdd32601e33f` |
| `deploy/systemd/btc-rewardbook-archive.timer` | 13 | 428 | frozen equal | `bf5af0252c420d8db1579b82e5da21472cdb6bc871fa8035ecf6f1edc9720a0f` |
| `deploy/systemd/adv3-bot.service` | 27 | 863 | frozen equal | `82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66` |
| `advisor/RULE-ADV-3.txt` | 33 | 3203 | frozen equal | `ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169` |
| `advisor/adv3.py` | 895 | 51834 | frozen equal | `81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1` |
| `advisor/adv3-bot.py` | 1869 | 126909 | frozen equal | `9e622daf2e8a5ec3e93f15c7f56e7cf859547fbd3771daad75bc6532adb2b9d1` |
| `advisor/selftest-adv3.py` | 256 | 19111 | frozen equal | `6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398` |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` |

The map is 2,047 lines, 548,314 bytes and `b8a0d7a0…`, which TZ-43 §10 states for revision `2026-11-08-a`. `advisor/adv3-bot.py` is still `9e622daf…`, so PR #41 was not merged before this run.

**The executor model** is the model TZ-43's header names. The session's own record, read by `get_session` before §0.0, gives that model for `configured_model`, `session_context.model` and `external_metadata.last_served_model` alike.

---

## 1. Input

**Read, and not re-collected:**

- **The TZ:** `CryptoTZ/TZ-43-l0-our-quote.md`, as `main` carries it since `12fb07b`: 3,774 lines, 255,055 bytes, SHA-256 `630777d239d4b532ac2bec6c651512ae00f84f471893d0348f1b4074dd64d056`.
- **The instrument:** Appendix A, extracted by §0.1's script into `stage/` and again into the worktree, `research/tz43-l0-our-quote.py`. Both extractions printed 3056 lines, 152905 bytes, `48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf` (`logs/01-stage.log`, `logs/11-worktree.log`).
- **The map:** `SYSTEM-MAP.md` revision `2026-11-08-a`, read by `fingerprint` in full and by the Executor in the sections TZ-43's header names (§6).
- **The reward book archive's ledger:** `/var/lib/btc-rewardbook-archive/ledger.jsonl`, read by `I archive` at §3.4 and §3.11, and by `I fetch` for the asset map. At both reads it was 48473 bytes, SHA-256 `16f6007d65e5daf6718912acaeebd7f2ccfcd63d44f668227939096ece45fa68`, with 127 complete records and 20 complete runs. Every complete run's `set.json` was asserted by its set record's SHA-256.
- **The rehearsal's four Release assets** of `rewardbook-streams-1793263627`, downloaded anonymously at 08:00:17 to 08:00:19 UTC, each checked by its bytes and SHA-256, then replayed and removed:

  | asset | bytes | SHA-256 |
  |---|---|---|
  | `1793232000-1793232000.0.stream.jsonl.gz` | 11579610 | `bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f` |
  | `1793232000-1793232900.0.stream.jsonl.gz` | 10715152 | `46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370` |
  | `1793232000-1793233800.0.stream.jsonl.gz` | 11443056 | `2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9` |
  | `1793232000-1793234700.0.stream.jsonl.gz` | 13592154 | `ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496` |

- **The reward book's store**, `/var/lib/btc-rewardbook/<D0>/`, by `I fetch` alone, from 08:00:39 to 08:01:00 UTC, for `D0` `1793404800` to `1794096000` (2026-10-31 to 2026-11-08). For each candidate day it read the day's listing, its first `ok` selection and that selection's replies, and its 96 `slot.json`; for the 8 members it also read their 96 reward files. That is `1,650` opens, printed as `reward book opens: 1650`: 8 members × (2 + 96 + 96) plus 2026-11-06's 2 + 96. **No stream file under the store was opened**, and no other day was opened or listed.
- **The members' gamma documents:** 20 requests to `gamma-api.polymarket.com/markets` from 08:01:02 UTC, under `User-Agent: btc-5m-twap-tz43`. That is 10 chunks of at most 50 condition ids, each asked open and closed, for 464 distinct markets. Every request was served on its first attempt, and every member's document was found exactly once.
- **The member days' stream assets:** `I replay` downloaded all 768 stream files of the 8 member days anonymously from the archive's Releases, 8,696,625,516 bytes, from 08:01:22 to 09:01:29 UTC. Each was checked by its bytes and SHA-256, with no retry, and removed after its unit. `I rescore` downloaded the first member day's first 24 slots again, 235,105,314 bytes, from 09:03:09 to 09:04:06 UTC, and removed them. `dl/` and `rehearsal-dl/` are empty.

**Not read:** no stream file stored on the host. No Release listing. No request to any host but `github.com` and the asset hosts it redirects to, `gamma-api.polymarket.com`, and `origin` through `git` and `gh`.

---

## 2. Measurements

### 2.1 The set — G-SET (`logs/60-fetch.log`)

`I fetch` ran once, from 08:00:39 UTC. The archive's assets already reached every candidate's last slot, so it did not wait. Each day's read and each document request was held to the pair book's idle stretch: it started at second 39 of window 08:00 and ended at second 62. Its lines, verbatim, except its 17 `wrote` lines, whose files, bytes and SHA-256 are in §2.6's table:

```
[2026-11-10T08:00:39Z] read ledger: {"at": "2026-11-10T08:00:39Z", "at_ns": 1794297639153409220, "file_sha256": "48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf", "head": "ab0f3873a66eb302225c3849da362bfe301e93df", "mode": "fetch"}
[2026-11-10T08:00:39Z] MemAvailable 217313280 bytes, floor 143592894; free 10504372224 bytes, floor 7800000000
[2026-11-10T08:00:41Z] candidate 1793404800 (2026-10-31T00:00:00Z): MEMBER 1 of 8 - 150 markets, 96 slots, 96 stream files, 750313689 bytes; polls 43200 served of 43200, 255 without a row
[2026-11-10T08:00:44Z] candidate 1793491200 (2026-11-01T00:00:00Z): MEMBER 2 of 8 - 150 markets, 96 slots, 96 stream files, 875810624 bytes; polls 43200 served of 43200, 71 without a row
[2026-11-10T08:00:47Z] candidate 1793577600 (2026-11-02T00:00:00Z): MEMBER 3 of 8 - 150 markets, 96 slots, 96 stream files, 962538163 bytes; polls 43199 served of 43200, 562 without a row
[2026-11-10T08:00:49Z] candidate 1793664000 (2026-11-03T00:00:00Z): MEMBER 4 of 8 - 150 markets, 96 slots, 96 stream files, 706996816 bytes; polls 43200 served of 43200, 1382 without a row
[2026-11-10T08:00:52Z] candidate 1793750400 (2026-11-04T00:00:00Z): MEMBER 5 of 8 - 150 markets, 96 slots, 96 stream files, 748765594 bytes; polls 43200 served of 43200, 2690 without a row
[2026-11-10T08:00:54Z] candidate 1793836800 (2026-11-05T00:00:00Z): MEMBER 6 of 8 - 150 markets, 96 slots, 96 stream files, 1236249189 bytes; polls 43199 served of 43200, 169 without a row
[2026-11-10T08:00:54Z] candidate 1793923200 (2026-11-06T00:00:00Z): not a member - slot 1793949300 (2026-11-06T07:15:00Z): stream: a gap above 15 s
[2026-11-10T08:00:57Z] candidate 1794009600 (2026-11-07T00:00:00Z): MEMBER 7 of 8 - 150 markets, 96 slots, 96 stream files, 1636900793 bytes; polls 43198 served of 43200, 1334 without a row
[2026-11-10T08:01:00Z] candidate 1794096000 (2026-11-08T00:00:00Z): MEMBER 8 of 8 - 150 markets, 96 slots, 96 stream files, 1779050648 bytes; polls 43199 served of 43200, 604 without a row
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed False, 48 documents, 422280 bytes, sha256 b4adb5a019fd6fc3dc474d2d57499f3ed2a10443c261aa395a52abf1aacce746, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed True, 2 documents, 15873 bytes, sha256 41bbf205e64d00f25ef7a1db513d018f03ebfc41bf5840219666ea78648343dc, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed False, 48 documents, 406682 bytes, sha256 83f2119a1da9a4f69086d558b3d6b146a1700ec22aaaebd610ec96616e857fc2, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed True, 2 documents, 16603 bytes, sha256 ca6c42a28683d65565506aabfa759d9bf837b7605cf8039d6b686907ff1084f3, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed False, 46 documents, 361163 bytes, sha256 ee6071fabf1c0825049a158ace013b735c3d79cae6a6791653411221e644b6e1, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed True, 4 documents, 37916 bytes, sha256 c2c9be56fffeac2b0a6dc9983008f6de593b8088aa6e18fc972ebb9a46dd5304, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed False, 46 documents, 363499 bytes, sha256 fba6ce4afb2d67548f7217fa854cc8c6ab3a8fb1aea841b47b982c205367505c, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed True, 4 documents, 37456 bytes, sha256 00a806993e7792e5174eddfb41c92a1edf66bee0f8a8e2b68417ccfd0b5daf56, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed False, 50 documents, 414679 bytes, sha256 24f4dd45b918947b861377d6edd781d7861497101ac9d4f3d22e6d75f0fc8566, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed True, 0 documents, 3 bytes, sha256 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed False, 48 documents, 385907 bytes, sha256 d753e45fd083143640d2d0fb63f15b4d58126378378029dbb95d7101c27fd6e8, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed True, 2 documents, 18670 bytes, sha256 d2882a1d50eeeb0336e5c1e06d3777c671a384243fc53577811b09d260120a1b, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed False, 47 documents, 389526 bytes, sha256 877439963346224c90a5a355a55d5c3dd6fa0ba3ffb71d9d1495ac02ba2cdb24, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed True, 3 documents, 19307 bytes, sha256 4a9d08fea1b7e4c605381a514d0a07eb6acc862c21e32c3274d525fdd9e7f121, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed False, 47 documents, 382365 bytes, sha256 9485d6b4d4e8c802e81feb1db71f63c617d00c4544b06bcff7ba7aaabeb46f96, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed True, 3 documents, 26252 bytes, sha256 20a5256b1b7e5fd1e08f697c46a1abde6a9264f4d20ac9601e4e63be46fa0081, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed False, 48 documents, 392522 bytes, sha256 b6f2816d74cf49efee577ec6130f11ff960586c3f9916a640cd5ac7998c578a2, retries 0
[2026-11-10T08:01:02Z] gamma request: 50 ids, closed True, 2 documents, 16188 bytes, sha256 fae9f362d7840c6a021e663e2c610cf8408160a4027b25f36c804dfb5d31fc02, retries 0
[2026-11-10T08:01:02Z] gamma request: 14 ids, closed False, 13 documents, 110757 bytes, sha256 e15a6a6893cadbb27584ca7c1cda911819ba5c8b03b7ab2f03f61c3f9304d3a3, retries 0
[2026-11-10T08:01:02Z] gamma request: 14 ids, closed True, 1 documents, 9507 bytes, sha256 2da33b0af143d5aa045f24f3e337f249fe2427a0af4a1d139b3a2d6745c512ed, retries 0
[2026-11-10T08:01:02Z] G-SET PASS: 8 members of 9 candidates considered, 1793404800 to 1794096000; 464 distinct markets, 23 resolved by their documents; 768 stream files, 8696625516 bytes; set.json sha256 904f1b9b8244a15fe48549e39ffc879f68ad31de6963a41c05f5afc607edf0f7
[2026-11-10T08:01:02Z] malloc tuned: True
[2026-11-10T08:01:02Z] peak memory of this run: 68464640 bytes
[2026-11-10T08:01:02Z] opens refused: 0; reward book opens: 1650
```

**Every candidate considered, in order:**

| candidate | day | verdict |
|---|---|---|
| `1793404800` | 2026-10-31 | member 1 |
| `1793491200` | 2026-11-01 | member 2 |
| `1793577600` | 2026-11-02 | member 3 |
| `1793664000` | 2026-11-03 | member 4 |
| `1793750400` | 2026-11-04 | member 5 |
| `1793836800` | 2026-11-05 | member 6 |
| `1793923200` | 2026-11-06 | **not a member** — slot `1793949300` (07:15 UTC): "stream: a gap above 15 s", as at TZ-41 (map §2.6, §7 item 148) |
| `1794009600` | 2026-11-07 | member 7 |
| `1794096000` | 2026-11-08 | member 8 |

One non-member before the eighth member, against the bound of 6. Begun on 2026-11-10, the walk absorbed it at 2026-11-08, as TZ-43 §1 says.

**The members:** 8 days of 150 markets each, 1,200 member-days, 464 distinct markets. Each day has 96 slots and 96 stream files, one file a slot, so there are 768 stream files and 8,696,625,516 bytes. Each day's polls total `43,198` to `43,200` served of `43,200`; between `71` and `2,690` a day held no row. **The documents:** 20 requests, every one served on its first try. Each of the 464 markets' documents was found exactly once, open or closed. 23 read closed with prices exactly 0 and 1, and are marked at their outcome.

### 2.2 L0 — every day's money by variant (`logs/90-score.log`)

`I score` (09:04:17 UTC), every line verbatim but the 8 G-BOOK day lines and G-BOOK's own line, which §2.3 quotes. Each money line is a sum over the day's 150 members; `central`'s lines and every total are barred from the reading (TZ-43 §4.5).

```
[2026-11-10T09:04:17Z] power: every pess day at or above 10 with probability 0.90 each: 0.430467210000
[2026-11-10T09:04:17Z] power: every pess day at or above 10 with probability 0.95 each: 0.663420431289
[2026-11-10T09:04:17Z] power: every pess day at or above 10 with probability 0.99 each: 0.922744694428
[2026-11-10T09:04:17Z] false reading: 2^-8 = 0.003906250000 for each answer, under independent days
[2026-11-10T09:04:18Z] day 1793404800 pess    total -11.259858540405 = paid 84.146601459595 of reward 99.927429049452 on 23 of 150 markets + rebate 0.000000000000 + marks -95.406460000000; fills 486, 15619.890000000000 shares, 1488.910000000000 against crossing orders; scored 334.714928964054 h; marks {'mid': 145, 'outcome': 5}
[2026-11-10T09:04:18Z] day 1793404800 opt     total 247.480311217417 = paid 346.144227879917 of reward 346.144227879917 on 46 of 150 markets + rebate 2.623473337500 + marks -101.287390000000; fills 448, 14985.160000000000 shares, 0.000000000000 against crossing orders; scored 340.180182209859 h; marks {'mid': 145, 'outcome': 5}
[2026-11-10T09:04:18Z] day 1793404800 central total 25.917423028518 = paid 118.212396591018 of reward 131.914862604307 on 34 of 150 markets + rebate 3.111486437500 + marks -95.406460000000; fills 486, 15619.890000000000 shares, 1488.910000000000 against crossing orders; scored 334.714928964054 h; marks {'mid': 145, 'outcome': 5}, barred
[2026-11-10T09:04:18Z] day 1793491200 pess    total 68.086470405581 = paid 80.195760405581 of reward 102.765165164257 on 20 of 150 markets + rebate 0.000000000000 + marks -12.109290000000; fills 589, 17590.430000000000 shares, 1415.180000000000 against crossing orders; scored 359.429767110781 h; marks {'mid': 146, 'outcome': 4}
[2026-11-10T09:04:18Z] day 1793491200 opt     total 370.592462656468 = paid 388.095510624093 of reward 388.095510624093 on 46 of 150 markets + rebate 4.135402032375 + marks -21.638450000000; fills 505, 16382.800000000000 shares, 0.000000000000 against crossing orders; scored 362.452400964682 h; marks {'mid': 146, 'outcome': 4}
[2026-11-10T09:04:18Z] day 1793491200 central total 122.639936890892 = paid 129.766708408517 of reward 146.006358728144 on 40 of 150 markets + rebate 4.982518482375 + marks -12.109290000000; fills 589, 17590.430000000000 shares, 1415.180000000000 against crossing orders; scored 359.429767110781 h; marks {'mid': 146, 'outcome': 4}, barred
[2026-11-10T09:04:18Z] day 1793577600 pess    total -43.567466943315 = paid 44.546298056685 of reward 62.659029655028 on 17 of 150 markets + rebate 0.000000000000 + marks -88.113765000000; fills 377, 12639.580000000000 shares, 1510.880000000000 against crossing orders; scored 332.266932832460 h; marks {'mid': 144, 'outcome': 6}
[2026-11-10T09:04:18Z] day 1793577600 opt     total 138.836970989877 = paid 235.013901637627 of reward 235.013901637627 on 40 of 150 markets + rebate 12.158299352250 + marks -108.335230000000; fills 314, 11421.680000000000 shares, 0.000000000000 against crossing orders; scored 327.908175583011 h; marks {'mid': 144, 'outcome': 6}
[2026-11-10T09:04:18Z] day 1793577600 central total 0.991470900804 = paid 75.734589790204 of reward 92.200690995205 on 28 of 150 markets + rebate 13.370646110600 + marks -88.113765000000; fills 377, 12639.580000000000 shares, 1510.880000000000 against crossing orders; scored 332.266932832460 h; marks {'mid': 144, 'outcome': 6}, barred
[2026-11-10T09:04:18Z] day 1793664000 pess    total 1.949199283554 = paid 43.398049283554 of reward 60.962654370802 on 18 of 150 markets + rebate 0.000000000000 + marks -41.448850000000; fills 561, 25403.650000000000 shares, 2886.330000000000 against crossing orders; scored 464.073027371840 h; marks {'mid': 147, 'outcome': 3}
[2026-11-10T09:04:18Z] day 1793664000 opt     total 622.046581446444 = paid 679.069607963544 of reward 679.069607963544 on 40 of 150 markets + rebate 22.993428482900 + marks -80.016455000000; fills 497, 22335.750000000000 shares, 0.000000000000 against crossing orders; scored 466.111084338412 h; marks {'mid': 147, 'outcome': 3}
[2026-11-10T09:04:18Z] day 1793664000 central total 62.414020390504 = paid 77.587801130079 of reward 95.354195414498 on 27 of 150 markets + rebate 26.275069260425 + marks -41.448850000000; fills 561, 25403.650000000000 shares, 2886.330000000000 against crossing orders; scored 464.073027371840 h; marks {'mid': 147, 'outcome': 3}, barred
[2026-11-10T09:04:18Z] day 1793750400 pess    total -47.702356068026 = paid 124.993498931974 of reward 142.645042948209 on 46 of 150 markets + rebate 0.000000000000 + marks -172.695855000000; fills 1126, 49636.780000000000 shares, 5307.600000000000 against crossing orders; scored 485.631716691339 h; marks {'mid': 136, 'outcome': 14}
[2026-11-10T09:04:18Z] day 1793750400 opt     total 404.880926272849 = paid 487.841499369674 of reward 487.841499369674 on 71 of 150 markets + rebate 71.904901903175 + marks -154.865475000000; fills 987, 44231.760000000000 shares, 0.000000000000 against crossing orders; scored 483.669727160904 h; marks {'mid': 136, 'outcome': 14}
[2026-11-10T09:04:18Z] day 1793750400 central total 143.547471486761 = paid 234.910710304511 of reward 249.030904173399 on 60 of 150 markets + rebate 81.332616182250 + marks -172.695855000000; fills 1126, 49636.780000000000 shares, 5307.600000000000 against crossing orders; scored 485.631716691339 h; marks {'mid': 136, 'outcome': 14}, barred
[2026-11-10T09:04:18Z] day 1793836800 pess    total -49.808415665403 = paid 65.629349334597 of reward 80.080676216214 on 23 of 150 markets + rebate 0.000000000000 + marks -115.437765000000; fills 860, 40126.560000000000 shares, 6775.710000000000 against crossing orders; scored 483.284270157200 h; marks {'mid': 148, 'outcome': 2}
[2026-11-10T09:04:18Z] day 1793836800 opt     total 232.893728616666 = paid 282.698784149066 of reward 282.698784149066 on 44 of 150 markets + rebate 59.654989467600 + marks -109.460045000000; fills 744, 33747.900000000000 shares, 0.000000000000 against crossing orders; scored 477.221115745014 h; marks {'mid': 148, 'outcome': 2}
[2026-11-10T09:04:18Z] day 1793836800 central total 60.162086167084 = paid 105.250380812259 of reward 118.214454129310 on 31 of 150 markets + rebate 70.349470354825 + marks -115.437765000000; fills 860, 40126.560000000000 shares, 6775.710000000000 against crossing orders; scored 483.284270157200 h; marks {'mid': 148, 'outcome': 2}, barred
[2026-11-10T09:04:18Z] day 1794009600 pess    total -77.856494508104 = paid 54.195040491896 of reward 71.996911033030 on 18 of 150 markets + rebate 0.000000000000 + marks -132.051535000000; fills 739, 34276.130000000000 shares, 5230.450000000000 against crossing orders; scored 535.571627212910 h; marks {'mid': 148, 'outcome': 2}
[2026-11-10T09:04:18Z] day 1794009600 opt     total 396.813963990171 = paid 569.624515167621 of reward 569.624515167621 on 45 of 150 markets + rebate 33.386053822550 + marks -206.196605000000; fills 648, 28280.450000000000 shares, 0.000000000000 against crossing orders; scored 553.953522664299 h; marks {'mid': 148, 'outcome': 2}
[2026-11-10T09:04:18Z] day 1794009600 central total 15.774147361451 = paid 107.224324654276 of reward 121.373261264960 on 30 of 150 markets + rebate 40.601357707175 + marks -132.051535000000; fills 739, 34276.130000000000 shares, 5230.450000000000 against crossing orders; scored 535.571627212910 h; marks {'mid': 148, 'outcome': 2}, barred
[2026-11-10T09:04:18Z] day 1794096000 pess    total 114.083108169877 = paid 90.640538169877 of reward 102.306046964609 on 24 of 150 markets + rebate 0.000000000000 + marks 23.442570000000; fills 964, 44038.990000000000 shares, 7731.230000000000 against crossing orders; scored 526.758892861768 h; marks {'mid': 150}
[2026-11-10T09:04:18Z] day 1794096000 opt     total 466.729797195475 = paid 399.400720179450 of reward 399.400720179450 on 42 of 150 markets + rebate 59.790012016025 + marks 7.539065000000; fills 824, 34283.400000000000 shares, 0.000000000000 against crossing orders; scored 529.124062170695 h; marks {'mid': 150}
[2026-11-10T09:04:18Z] day 1794096000 central total 255.835627987480 = paid 155.120973385455 of reward 165.399871510893 on 29 of 150 markets + rebate 77.272084602025 + marks 23.442570000000; fills 964, 44038.990000000000 shares, 7731.230000000000 against crossing orders; scored 526.758892861768 h; marks {'mid': 150}, barred
[2026-11-10T09:04:18Z] pess days at or above 10: 2 of 8, the least -77.856494508104; opt days below it: 0 of 8, the most 622.046581446444
[2026-11-10T09:04:18Z] pess: over the 8 days -46.075813866239, a day -5.759476733280
[2026-11-10T09:04:18Z] opt: over the 8 days 2880.274742385367, a day 360.034342798171
[2026-11-10T09:04:18Z] central: over the 8 days 687.282184213495, a day 85.910273026687, barred
[2026-11-10T09:04:18Z] wrote /root/tz43-work/reading.json 9377 bytes sha256 175d366101cd825437a1cd393aa57642965f7ffb9fe831746c2d9b2187d50be1
[2026-11-10T09:04:18Z] L0 UNDECIDABLE: EARN False, NO EARN False; reading.json sha256 175d366101cd825437a1cd393aa57642965f7ffb9fe831746c2d9b2187d50be1
```

**How to read a line:**
- "paid … of reward …" is the reward after and before the venue's 1-pUSD minimum. `pess` and `central` pay a member's day only where it reaches 1. `opt` pays the day's sum where it reaches 1, so its "paid" equals its reward.
- "on N of 150 markets" counts the members whose own day reached 1.
- "fills" counts our fills; "shares" is their size; "against crossing orders" is the part filled by crossing orders taken as takers, which `opt` never counts.
- "scored h" is the hours our quotes scored, summed over the members.
- "marks" counts the members valued at their day's last midpoint, a proxy, and those valued at their outcome. No member was valued by liquidation into its book.
- **The totals and mean days are barred**, as is `central`'s every line: `pess` over the 8 days `-46.076`, a day `-5.759`; `opt` `2880.275`, a day `360.034`; `central` `687.282`, a day `85.910`.

`I score` again (`logs/91-score-again.log`, 09:04:28 UTC) printed the same lines. Its stamps, its read-ledger line, its floor read and its peak differ, and in place of `wrote` it printed `unchanged /root/tz43-work/reading.json sha256 175d366101cd825437a1cd393aa57642965f7ffb9fe831746c2d9b2187d50be1`.

### 2.3 G-BOOK by day (`logs/70-replay.log`, and again in `logs/71-replay-again.log` and `logs/90-score.log`)

| day | book frames | rebuilt touch equal | every level equal (barred) | matches | subscribes | closes |
|---|---|---|---|---|---|---|
| 2026-10-31 `1793404800` | 6737 | 6733 | 6718 | 6684 | 3 | 3 |
| 2026-11-01 `1793491200` | 5973 | 5970 | 5965 | 5891 | 7 | 7 |
| 2026-11-02 `1793577600` | 5291 | 5291 | 5284 | 5228 | 1 | 1 |
| 2026-11-03 `1793664000` | 5748 | 5748 | 5745 | 5703 | 4 | 4 |
| 2026-11-04 `1793750400` | 11711 | 11711 | 11701 | 11666 | 1 | 1 |
| 2026-11-05 `1793836800` | 10368 | 10368 | 10351 | 10339 | 2 | 2 |
| 2026-11-07 `1794009600` | 6772 | 6769 | 6756 | 6748 | 3 | 3 |
| 2026-11-08 `1794096000` | 7489 | 7488 | 7467 | 7456 | 1 | 1 |
| **8 days** | **60089** | **60078** | 59987 | 59715 | 22 | 22 |

```
[2026-11-10T09:01:29Z] G-BOOK PASS: the rebuilt touch equal to the venue's book frame at 60078 of 60089 frames, at least 99/100 required; barred: every level equal at 59987
```

The rebuilt touch equals the venue's own at `60078 / 60089 = 0.999817` of the frames, against `0.99`. The 22 subscribes and 22 closes are the stream's own reconnects inside the member days, and each close cancels our live quotes at its host instant (TZ-43 §1, rule 5).

### 2.4 The units — the timing files' summary lines

`I replay` (`logs/70-replay.log`, from 08:01:22 to 09:01:29 UTC):

```
[2026-11-10T09:01:29Z] units 768: inside the idle stretch 768, ending after second 590 0; longest 15.1 s, download 11.2 s and replay 5.3 s at most; 1521 s waited; processor 1247.2 s; 8696625516 bytes downloaded; retries 0; windows 2026-11-10T08:00:00Z to 2026-11-10T09:00:00Z
```

**No unit ended after second 590**, so the instrument listed none. By window, from `timing-replay.jsonl` (slots, seconds and bytes):

| window (UTC) | units | first start, second | last end, second |
|---|---|---|---|
| 08:00 | 196 | 82.6 | 536.2 |
| 08:15 | 244 | 15.2 | 536.4 |
| 08:30 | 183 | 15.4 | 534.5 |
| 08:45 | 127 | 15.6 | 533.4 |
| 09:00 | 18 | 15.4 | 89.1 |

The projection after the first 24 units:

```
[2026-11-10T08:02:19Z] projected 1250 s of replay for 8696625516 bytes after 24 units at 0.1437 s a megabyte
```

That is 1,250 s against the `3,000` that blocks and §6's bound of `2,363`. The whole replay took `1247.2` s of processor for 8,696,625,516 bytes, `0.1434` s a megabyte.

`I rescore` (`logs/80-rescore.log`, from 09:03:09 UTC) prints no summary line of its own (§6). From `timing-rescore.jsonl`:
- 24 units in window 09:00, from second 189.6 to second 246.2, every one inside the idle stretch and none ending after second 590;
- longest 3.8 s, download 1.2 s and replay 2.9 s at most, 0 s waited, retries 0;
- processor 33.8 s for 235,105,314 bytes.

Its projection after its first 6 units:

```
[2026-11-10T09:03:24Z] projected 34 s of replay for 235105314 bytes after 6 units at 0.1427 s a megabyte
```

That is 34 s, against the `300` that blocks and §6's bound of `74`.

**Wall clock:** from §0.0's clock line at 07:51:58 UTC to §3.11's last read at 09:05:15 UTC, 1 h 13 min. The replay alone took 60 min, of which its units waited 1,521 s for the idle stretch.

### 2.5 The replay's day files (`logs/70-replay.log`)

| day | replayed in | lines of stream | `days/<D0>.slots.txt` SHA-256 | `days/<D0>.json` SHA-256 |
|---|---|---|---|---|
| 2026-10-31 | 194 s | 6185533 | `ec4494031d22891f22ec2822287c0127c4f96f39dac1337f3980419813052400` | `d93f998fba7795f30379c06e2058c55f4eba9d0c340536a3d5a4d1636b765ee6` |
| 2026-11-01 | 252 s | 7392178 | `5a7169dbcdb3186b588e2bd77ef5017dc792f1ead7cc8d2b9c11a55cee90f763` | `50e19969a8196ef3fe8b069056b75bb3ff5f5ba1c41a9ad70a48bd7e88ebaaae` |
| 2026-11-02 | 607 s | 8196551 | `aae9a59997c591b90672bec21ea2489e2f7e654eba03590bc8d1ff411a186e1c` | `93c76d1594b1edef03e192c02cc67b0264e43ca4b77b6d49939845f5876dc57c` |
| 2026-11-03 | 179 s | 5837753 | `dc9dff0e13153ee045ada2cb805c9567ce9bb4b490f88c40aa0821442fe8660b` | `a80c3d721fce47537ff927c42b989cd4409d25b7c3a1e2c4e024a2463d48c54d` |
| 2026-11-04 | 572 s | 6417117 | `71101c5d670141ce064c671824d5c8c8c1615ffce4801b1a422baa3df4281cdc` | `4f9ca91d2798fb9f7b496e98baa02d4fe9f6efb5f60f979540f682fb7fdadfa9` |
| 2026-11-05 | 285 s | 10335071 | `ec5792be99ff4169b4574b3a8ce04855ad7a5fcd51aba1b51baf4cc9d8ce44e5` | `e7266b1d2d05e1191095e9cd184e6bb15571ea7380fa1e4f51db90a5342e200d` |
| 2026-11-07 | 746 s | 13623109 | `a0fdb71edc318fb7e41989c1aca3b591c9b3e4db39274e87588354639725c1e6` | `f3018bb242bff3b1d7483622cd4065074cc42faa90b1e8357d223c2796a6dfd5` |
| 2026-11-08 | 771 s | 15448742 | `00caaab0888d85779398751281da3e9219cfdf9742c77b5914499cf0c4421436` | `910ed69e85ab28dc81a334538d229a66ba17107260325c1afe5eae95de02e91f` |

"Replayed in" includes the units' holds for the idle stretch. Each day's two files were written once (`write_once`). The second `I replay` replayed no day and printed "days to replay 0 of 8".

### 2.6 Every file the run wrote

Seventy files under `/root/tz43-work/`, by bytes and SHA-256, read at 09:05 UTC after §3.11. The branch worktree `wt/` is not listed: it held exactly its pushed `HEAD` (§9 below). `dl/` and `rehearsal-dl/` are empty, and `selftest-tmp/` was removed by the self-test.

| file | bytes | SHA-256 |
|---|---|---|
| `stage/research/tz43-l0-our-quote.py` | 152905 | `48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf` |
| `state.json` | 495 | `31257121ffbab162f73b03a14643623198ea38c4c1285bba8c0c294f22122ce9` |
| `read-ledger.jsonl` | 1498 | `257ac840d8a5c6bd60579e0def9107465bbb409b59e2f15cb526583923eeb874` |
| `rehearsal.txt` | 103261 | `1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd` |
| `set.json` | 6175 | `904f1b9b8244a15fe48549e39ffc879f68ad31de6963a41c05f5afc607edf0f7` |
| `fetch/1793404800.json` | 55310 | `5f56487e44aadcba1df2bc1316a889605baf83a4fcafc965b5ee4a18a6fec9b2` |
| `fetch/1793404800.polls.jsonl` | 4990923 | `53ae4e79d354b3f8b35d497654159162b9c2290deb0d69b6f62b79c3fe8c1d71` |
| `fetch/1793491200.json` | 55330 | `55f95448c4ba6abe1d1b154ff0e014ef190ffb7be861a7f6cb1a3bcddec7a1bd` |
| `fetch/1793491200.polls.jsonl` | 5010687 | `1aac9148f26b55664b248be60b62394defc1b117b63bcd952c632bf96b3ebf54` |
| `fetch/1793577600.json` | 55447 | `8589729bfe267feb57208833064bc71006e592e22edd8290d70bbc2b4474d9b5` |
| `fetch/1793577600.polls.jsonl` | 5027379 | `19d765c78c93e9d4175328615ae3dc27b3e2f0c1dd7f6084eeab672a9e56427c` |
| `fetch/1793664000.json` | 55449 | `1405b48ac2459f052b5b36dea8e85dd6cb0e112b49ac21030955d96f890eec02` |
| `fetch/1793664000.polls.jsonl` | 5014920 | `4a5ef449ed6b1d2bf1378b817671b9bb3cac477c5a9fa6e5068d9673b24977cb` |
| `fetch/1793750400.json` | 55543 | `1ed8768bd80b54220c0437e15fc424943a8829b716d7ba70f2b586f5ae14099c` |
| `fetch/1793750400.polls.jsonl` | 4967708 | `f06145aa32845b9f3a65b8616e5842218b03869a3fc18d5a4bf1aaaa57fec920` |
| `fetch/1793836800.json` | 55625 | `7d502a56ad2a4a3f95150bbcfc8c52c1190f2b977d9d1a72e2e1c4b3c2f5ba25` |
| `fetch/1793836800.polls.jsonl` | 5055307 | `7918f3b6629489fcff4fd22cdb049a89e1e1ef63b86738c73ec680e17e5eff5d` |
| `fetch/1794009600.json` | 55639 | `29e17ecde5f5d705e297bdc2be7e5e150aa50d06c3ac66ba9b1c4c13225b5708` |
| `fetch/1794009600.polls.jsonl` | 5037697 | `91582ccfb9145559277d196f61e804e6be205d0b18d6168a1db6975711d6cf15` |
| `fetch/1794096000.json` | 55660 | `a3ebc56744facb5c00f862c1f5d70a564672b68b5cc276398f32ae7f1bc0c552` |
| `fetch/1794096000.polls.jsonl` | 5047340 | `7b0d86338359fbb4d5f4f7b54c6f36e0d45f2ed5c4d6d5731358c8e4e3099a82` |
| `days/1793404800.json` | 145864 | `d93f998fba7795f30379c06e2058c55f4eba9d0c340536a3d5a4d1636b765ee6` |
| `days/1793404800.slots.txt` | 47260 | `ec4494031d22891f22ec2822287c0127c4f96f39dac1337f3980419813052400` |
| `days/1793491200.json` | 147006 | `50e19969a8196ef3fe8b069056b75bb3ff5f5ba1c41a9ad70a48bd7e88ebaaae` |
| `days/1793491200.slots.txt` | 47077 | `5a7169dbcdb3186b588e2bd77ef5017dc792f1ead7cc8d2b9c11a55cee90f763` |
| `days/1793577600.json` | 146744 | `93c76d1594b1edef03e192c02cc67b0264e43ca4b77b6d49939845f5876dc57c` |
| `days/1793577600.slots.txt` | 46799 | `aae9a59997c591b90672bec21ea2489e2f7e654eba03590bc8d1ff411a186e1c` |
| `days/1793664000.json` | 147691 | `a80c3d721fce47537ff927c42b989cd4409d25b7c3a1e2c4e024a2463d48c54d` |
| `days/1793664000.slots.txt` | 46785 | `dc9dff0e13153ee045ada2cb805c9567ce9bb4b490f88c40aa0821442fe8660b` |
| `days/1793750400.json` | 155059 | `4f9ca91d2798fb9f7b496e98baa02d4fe9f6efb5f60f979540f682fb7fdadfa9` |
| `days/1793750400.slots.txt` | 47105 | `71101c5d670141ce064c671824d5c8c8c1615ffce4801b1a422baa3df4281cdc` |
| `days/1793836800.json` | 149722 | `e7266b1d2d05e1191095e9cd184e6bb15571ea7380fa1e4f51db90a5342e200d` |
| `days/1793836800.slots.txt` | 46750 | `ec5792be99ff4169b4574b3a8ce04855ad7a5fcd51aba1b51baf4cc9d8ce44e5` |
| `days/1794009600.json` | 146104 | `f3018bb242bff3b1d7483622cd4065074cc42faa90b1e8357d223c2796a6dfd5` |
| `days/1794009600.slots.txt` | 46914 | `a0fdb71edc318fb7e41989c1aca3b591c9b3e4db39274e87588354639725c1e6` |
| `days/1794096000.json` | 144626 | `910ed69e85ab28dc81a334538d229a66ba17107260325c1afe5eae95de02e91f` |
| `days/1794096000.slots.txt` | 46970 | `00caaab0888d85779398751281da3e9219cfdf9742c77b5914499cf0c4421436` |
| `reading.json` | 9377 | `175d366101cd825437a1cd393aa57642965f7ffb9fe831746c2d9b2187d50be1` |
| `rescore.txt` | 11614 | `90bd9c8b0a85f3f55aef88674a3431ed7644cef621869e25b6c90f32b9ff9385` |
| `timing-replay.jsonl` | 172505 | `4300297dc853f03edd7edc3e70482715acc951dd3fc325df52d2b18ba3e64c65` |
| `timing-rescore.jsonl` | 5398 | `a938e1b1010252604ae1e85f5371623721d7953b85f38c5b763355fd5453674c` |
| `logs/00-instant.log` | 70 | `93ca8e4b234b74f921564e8a405dd506807067d332e5d28de45496156844f639` |
| `logs/01-stage.log` | 136 | `faf1dbaa37386aa7e8810b1662b471a14b21009a82de135a808dbaf8079295b7` |
| `logs/02-fingerprint.log` | 11498 | `c79ffb527bf298ec4d923e3ba2c7a6c13d08b641403a49a18c6f84b8886816c0` |
| `logs/03-host-gate.log` | 10351 | `5047f7b8ce68af120e2273b74a7af5795fdda544097ff135976765283ae78e24` |
| `logs/05-number.log` | 405 | `2c38971a0746ead31bcddbc7a45fe9b7138a39b3a79444dadd7702fee46a136b` |
| `logs/05-refs.log` | 9889 | `ca97c716706f22d59ff41bc88f2cf1891573a981d98f6ae6bbfca3558f56cf8c` |
| `logs/10-number.log` | 412 | `49ea472313144593d62a429797ee3371254023b6135809a99a12164f33110175` |
| `logs/11-worktree.log` | 296 | `c20411347d9ca19614be301de3bdf91d1e9c7a41e9a4ad942354e0e5e5fc6071` |
| `logs/12-fingerprint.log` | 11498 | `df3d56839f284316e7b9749fe3abb3d640bf02b2ddf1d1f63bc461c293312933` |
| `logs/13-push.log` | 10940 | `48219a86fbc350811d7f1746e31edb7646d2c6698688e37e7070a78bc08633d6` |
| `logs/14-pr.log` | 63 | `c09b22bc5711f2d827c8de5ff856825a904f03c566d3225441c0014b3233370d` |
| `logs/20-selftest.log` | 6988 | `d7185deee0d095f8b7fbaeb87d171f31c6834121ccda831bcae75551e62d2af6` |
| `logs/30-still.log` | 1426 | `0ae793dd45d1678ac121ee8acc54cec7c7d139dd10b4f4ee92edc7cd4c264af6` |
| `logs/31-scratch.log` | 1241 | `0c7af015ab5c734cf2ddb3615f4d9bd50fc70788c5d5da195b37fa43d360772c` |
| `logs/32-reclaim-scratch.log` | 525 | `fa4647b3c53d5971af6b4f8e01b92dacf603ffe56d139892bbf6301fe50a9be0` |
| `logs/32a-reclaim-scratch-refused.log` | 773 | `9a4d2d1365e3598939863593268a4836bc6517833b90c9723a215e0cb4af4d88` |
| `logs/40-archive.log` | 64915 | `161b3c5407cc58cdb93fe7dc6815614e1dc363d4c95fab50742b52719377ef53` |
| `logs/50-rehearse.log` | 1899 | `c290f8ad6f456a6a9d59764f6854fc33c63949a0a324b5ecec19b4b4bdf8055e` |
| `logs/60-fetch.log` | 8506 | `d2cbf48aac07fae8eda5ff16888ffcda9e604ce0c46756d2ccf9a2767d894d99` |
| `logs/70-replay.log` | 6970 | `7c2402c07d859898a227de058b8d3f6e0c80971db069bad7d89d863a95356fb8` |
| `logs/71-replay-again.log` | 2321 | `c24910c79df907bb0c92796c5786c580429beb2980eac8ed241f4d7edc71946a` |
| `logs/80-rescore.log` | 915 | `a666e7e576958002449205ac1600f6a0bb3e958975ad56730fb5e5f63084df1e` |
| `logs/90-score.log` | 11050 | `1707d544dea9092231ef1791a09a4e9fdb7451d8c4526503d2c7334a5aefcc6d` |
| `logs/91-score-again.log` | 11043 | `0c84a9f734f395e703b6e7393349a4393a47b4e702d8ef8aa1403bbe396adda8` |
| `logs/95-still.log` | 1553 | `f27ad6ad2d82ae55c84397e2a66851ba68825d14633232a8c53146404497da42` |
| `logs/96-host-gate-again.log` | 10167 | `b1052d91a0b7dec5b3c0cbd6fa36aa2b1525b0943f721795efe6e90155164ba7` |
| `logs/97-archive-again.log` | 64915 | `3227b1516d9dfb49b7ee48b2b48bbeea88a600a50a10055bc5ff2fab60610021` |
| `logs/98-closing.log` | 3486 | `3010f3a80fed5dc71353a79330768ff55ec9509d070f137aa1c275686900e37e` |
| `logs/99-separation.log` | 566 | `0da9f7314153036ac106f56d0dadb7ef574d33a19c5d8067a04a60e63876fe82` |

The `fetch/` and `days/` files, `set.json`, `reading.json`, `rehearsal.txt` and `rescore.txt` carry member figures (TZ-43 §2 item 10). They were printed by no command but the instrument's modes and the hash and size commands. Their only copies outside the work tree are §9's byte-for-byte copies into the forensic store.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-43-l0-our-quote`, on `origin` |
| commit | `ab0f3873a66eb302225c3849da362bfe301e93df`, parent `12fb07b` (`origin/main` when the worktree was made), one file |
| on `origin` | at `2026-11-10T07:54:46.835116063Z`, `ls-remote` printed `ab0f3873a66eb302225c3849da362bfe301e93df refs/heads/tz-43-l0-our-quote`, equal to the worktree's `HEAD` (`logs/13-push.log`) |
| push | `git -C /root/tz43-work/wt push -u origin tz-43-l0-our-quote`, started `2026-11-10T07:54:37.191466368Z`, through the URL's own credential (`gh`'s route not needed), `exit=0` |
| pull request | #43, <https://github.com/seahomebatumi-ai/btc-5m-twap/pull/43>, against `main`, opened by `gh pr create` (`logs/14-pr.log`). Not merged by the Executor |
| Release | none: TZ-43 creates no Release (§2 item 11) |
| report | this file, the one path pushed to `main` |

**Contract §4.2's separation self-check**, run after the push and the pull request and before this report's commit (V14):

```
2026-11-10T09:05:15.371320945Z
fetch exit=0
12fb07b5735bf25de2cd79dae53b8807411de04a
ab0f3873a66eb302225c3849da362bfe301e93df
$ git rev-list origin/main | grep -c ab0f3873a66eb302225c3849da362bfe301e93df
0
$ git diff --name-only origin/main origin/tz-43-l0-our-quote
research/tz43-l0-our-quote.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
(exit=1)
$ git diff --numstat origin/main origin/tz-43-l0-our-quote
3056	0	research/tz43-l0-our-quote.py
$ git diff --name-status origin/main origin/tz-43-l0-our-quote
A	research/tz43-l0-our-quote.py
```

That is `logs/99-separation.log`, verbatim. The first two hashes are `origin/main` and `origin/tz-43-l0-our-quote` after a fresh fetch. The implementation commit is not on `main`, the branch's diff names the one implementation file, and `main` carries no `.parquet` or `.zip`.

---

## 4. Gate — L0

> | condition, on each day's money of `pess` and `opt` over the set's 8 days | reading |
> |---|---|
> | every `pess` day at or above `θ = 10` USDC, and some `opt` day at or above it | **EARN** |
> | every `opt` day below `θ`, and some `pess` day below it | **NO EARN** |
> | otherwise | **UNDECIDABLE** |
>
> (TZ-43 §4.5)

**The deciding numbers, to three decimals:**

- **EARN:** the least `pess` day is **`−77.856`** USDC (2026-11-07), below `θ = 10.000`. `pess` reached `θ` on 2 of 8 days, 2026-11-01 (`68.086`) and 2026-11-08 (`114.083`), so the first condition fails.
- **NO EARN:** the most `opt` day is **`622.047`** USDC (2026-11-03). `opt` was below `θ` on 0 of 8 days, its least `138.837` (2026-11-02), so the second condition fails.
- **Reading: UNDECIDABLE**, as `I score` printed it: `L0 UNDECIDABLE: EARN False, NO EARN False`.

G-BOOK passed, so `score` read the reading (§4.3).

**Printed before any money was read:**
- EARN's power is `0.430467210000`, `0.663420431289` and `0.922744694428` where each `pess` day reaches `θ` with probability `0.90`, `0.95` and `0.99`.
- Each answer's false reading is `2⁻⁸ = 0.003906250000` under independent days.

No row reads a power. Nothing was tuned to reach the gate, and no gate was reinterpreted. **The marks are a proxy**: each member's position at the day's end is valued at its outcome where its document reads it resolved — 23 markets — and otherwise at the day's last midpoint of its two-sided book (TZ-43 §1).

---

## 5. Validation — in TZ-43 §7's numbering

Every figure below is quoted from the log named. Every check here is an assert of the instrument or an explicit exit, except where a line says it is a printed fact.

**§0.0, the instant.** The session's own read before `mkdir` printed `now 1794297118 2026-11-10T07:51:58Z, second of the day 28318` and `inside=0`. `mkdir /root/tz43-work /root/tz43-work/logs` printed `exit=0`. The clock line again into `logs/00-instant.log`: `now 1794297135 2026-11-10T07:52:15Z, second of the day 28335`, `inside=0`.

**V1 — fingerprint, at §0.2 and §3.1:** `FINGERPRINT PASS`, twice (§0). Peaks `33636352` and `33505280` bytes.

**V2 — the host gate, at §0.3** (`logs/03-host-gate.log`, 07:52:56 UTC) **and §3.11** (`logs/96-host-gate-again.log`, 09:04:47 UTC). 11 of 11 at each:

| check | §0.3 | §3.11 |
|---|---|---|
| H1 — one `manifest.json` | `/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json` | the same |
| H2 — source and size | `/dev/vda2` `31612203008` | `/dev/vda2` `31612203008` |
| H2 — `grep -c e3975b5…` | `3` | `3` |
| H3 — interpreter | `3.12.3` | `3.12.3` |
| H4 — three files | `48473` reward book archive's ledger, `32516` its first run's `set.json`, `115272` pair book archive's ledger | the same three sizes |
| H5 — recorder | active, enabled, pid `2388318`, `NRestarts` `0` | the same |
| H5 — pair book | active, enabled, pid `883760`, `NRestarts` `29` | the same |
| H5 — reward book | active, enabled, pid `3137952`, `NRestarts` `1` | the same |
| H5 — advisor | active, enabled, pid `284419`, `NRestarts` `5` | the same |
| memory gate | read 1 at 07:52:59: `331935744` ≥ `143592894` | read 1 at 09:04:50: `314875904` |
| disk gate | avail `10555289600` ≥ `7800000000` | avail `10328178688` |

The rest of each log is printed and gates nothing:

- **Boots:** one, since 2026-08-02 07:24:32 UTC (`uptime -s`); `journalctl --list-boots` lists the single boot `48a803f0…`.
- **Memory at §0.3:** `nproc` `1`; `MemTotal` `978640 kB`, `MemAvailable` `262048 kB`, `SwapTotal` `3174396 kB`, `SwapFree` `2376820 kB`.
- **The consumer:** `telemetry-watch.service` `disabled` (exit 1) and `inactive` (exit 3). The same at §3.11.
- **Paths:** `/root/tz41-work` and `/root/tz42-work` absent (exit 1); the six code trees present (exit 0). The same at §3.11.
- **The forensic store:** `2417` files at §0.3, map §3's count. `2417` at §3.11 too: B-RECLAIM-SCRATCH copied nothing.
- **Worktrees:** at §0.3 the primary checkout at `12fb07b` and `/root/btc-recorder-svc` at `e3975b5`, map §3's two. At §3.11 there was also this TZ's `/root/tz43-work/wt` at `ab0f387` `[tz-43-l0-our-quote]`.
- **`du -sb`:** reward book `567265163`, pair book `449646166`, reward book archive's state `3846633` at §0.3. At §3.11: reward book `628646730`, pair book `553319128`, the archive's state `3846633`.
- **Timers at §0.3:** the reward book archive's next at 2026-11-11 01:30:20 UTC (last 2026-11-10 01:30:20); the pair book archive's next at 2026-11-11 03:00:20 (last 2026-11-10 03:00:20); `apt-daily-upgrade` last 2026-11-10 06:37:05, next 2026-11-11 06:22:52; `apt-daily` last 2026-11-09 21:15:30, next 2026-11-10 13:48:22.
- **systemd's records since 2026-11-08** hold no `Reload` line. The reward book's archive started at 01:30:20 UTC on 2026-11-08, 11-09 and 11-10 and finished at 01:37:14, 01:37:21 and 01:36:47. The pair book's archive started at 03:00:20 each day and restarted the pair book inside its band: pid `470149` stopped at 03:06:33 on 11-08 (restart counter 27), `602266` at 03:06:42 on 11-09 (28), and `751579` at 03:15:15 on 11-10 (29); it finished at 03:15:41, 03:15:41 and 03:30:41. **Every run of either archive since TZ-41 ran on its calendar** (map §7 items 115 and 129).
- **The package history:** its last entries are `unattended-upgrade` at 2026-11-04 06:33:35 to 06:33:45, 2026-11-05 06:33:58 to 06:34:12 and 2026-11-06 06:16:05 to 06:16:07 UTC. It records no upgrade since; `apt-daily-upgrade.timer` last fired at 2026-11-10 06:37:05.
- **The directory that holds the session's own** (§0.3's last line, listing `$(dirname "$(dirname "$S")")`, `S` = `/tmp/claude-0/-root-btc-5m-twap/fd099d3c-2537-55ea-a4a0-314ac50cff1f/scratchpad`) held six UUID directories at §0.3: `238335b9…` (2026-10-30 13:16), `671824f6…` (2026-11-08 07:20), `8e3e58b1…` (2026-11-10 07:48), `c78295f5…` (2026-11-08 07:15), `c82149c8…` (2026-11-08 07:20) and this session's `fd099d3c…` (2026-11-10 07:48). At §3.11 it held three: `8e3e58b1…`, `c78295f5…` and `fd099d3c…`. The three that B-RECLAIM-SCRATCH removed were gone (§3.3 below).
- **§3.11 against §0.3:** `diff` of the two logs differs only in the instants, `MemAvailable` (`252804 kB`), `SwapFree` (`2306736 kB`), `df`'s avail, the timers' time left, the worktree line, `du` of the two stores and the directory listing. **The units' `systemctl show` lines, the journal of systemd since 2026-11-08 and the package history are identical**, so no unit was restarted and nothing was reloaded or upgraded during the run.

**§0.5 — refs and the number.**

- `I0 number` (`logs/05-number.log`, 07:53:21 UTC): `origin/main 12fb07b5735bf25de2cd79dae53b8807411de04a: 105 paths under CryptoTZ/ and CryptoReports/; of the number TZ-43-: ['CryptoTZ/TZ-43-l0-our-quote.md'] and []`, then **`NUMBER PASS - 2 of 2`**.
- §3.1's `I0 number` after `git fetch origin` (`logs/10-number.log`, 07:53:50 UTC): the same line and **`NUMBER PASS - 2 of 2`**.
- `git ls-remote origin` (`logs/05-refs.log`, 07:53 UTC): **134 ref lines**, against the Architect's 132 of 2026-11-08 13:24 UTC. TZ-43 §0.5 records such a difference without blocking:

  | refs | count |
  |---|---|
  | `HEAD` and `refs/heads/main` | 1 and 1, at `12fb07b` |
  | `tz-*` branches | 18: the Architect's 19 less `tz-41-l0-our-quote`, which `origin` no longer carries; `tz-42-advisor-registry` at `4e6db2d` |
  | pull heads | 41, `refs/pull/42/head` still at `cca1109` |
  | pull merge refs | 1, `refs/pull/41/merge` at `785fe68`; PR #42's is gone |
  | `pairbook-streams-*` tags | 48: 46 and the calendar runs of 2026-11-09 and 2026-11-10 |
  | `rewardbook-streams-*` tags | 20: 18 and the calendar runs of 2026-11-09 and 2026-11-10 |
  | annotated tags | 2, with their 2 peeled lines |

  `main` carries revision `2026-11-08-a`. `refs/heads/tz-43-l0-our-quote` did not exist before the push. §3.1's `ls-remote` before the push (`logs/13-push.log`) printed the same 134 lines.
- **`main`'s first-parent commits above `e2458af`** (appended to `logs/05-refs.log` under a `date -u` line):

  | commit | date (UTC) | what | path |
  |---|---|---|---|
  | `183a022` | 2026-11-08 13:53:44 | upload, "Update SYSTEM-MAP.md" | `M SYSTEM-MAP.md` |
  | `12fb07b` | 2026-11-08 13:54:24 | upload, "Add files via upload" | `A CryptoTZ/TZ-43-l0-our-quote.md` |

**V3 — the file:** 1 of 1 hash asserted at §0.1 and at §3.1, 3056 lines, 152905 bytes (`logs/01-stage.log`, `logs/11-worktree.log`). The commit `ab0f387` holds one path, and `git diff --numstat origin/main HEAD` printed `3056 0 research/tz43-l0-our-quote.py` (`logs/13-push.log`). At the end, after §3.11, `logs/99-separation.log` printed `3056 0 research/tz43-l0-our-quote.py` for `--numstat` and `A research/tz43-l0-our-quote.py` for `--name-status` against `origin/main` `12fb07b`.

**V4 — the self-test** (`logs/20-selftest.log`, 07:55:19 UTC): **`SELFTEST PASS: 42 checks`**, 42 `ok` lines, peak `34422784` bytes. `/root/tz43-work/selftest-tmp` was absent afterwards (`test -e` exit 1).

**V5 — the archive's record, at §3.4** (`logs/40-archive.log`, 07:57:20 UTC) **and §3.11** (`logs/97-archive-again.log`, 09:05:00 UTC):

- the ledger: at §3.4, 48473 bytes, `16f6007d65e5daf6718912acaeebd7f2ccfcd63d44f668227939096ece45fa68`, 127 complete records and 0 bytes of a line still being written; at §3.11 the same, 48473 bytes, `16f6007d…`, 127 records. No run of the archive had begun between the two reads, and the two logs differ only in their stamps and their peaks;
- 20 complete runs and 20 sets. The assets reach slot `1794272400` (2026-11-10 01:00 UTC): 1208 files of 1207 slots, 965 slots at or after `1793404800`;
- 20 tags on `origin`, no complete run's tag missing; halted `False`; no run without a terminal record;
- "the rehearsal's four assets are in set rewardbook-streams-1793263627, bytes and SHA-256 equal".

The runs, as `I archive` printed them, each run off the calendar beside §0.3's reads of systemd:

| run | started (UTC) | calendar | files | bytes | note |
|---|---|---|---|---|---|
| `1793263627` | 10-29 08:47:07 | off | 86 | 890975956 | TZ-34's first run; deferred in verify, then complete |
| `1793286490` | 10-29 15:08:10 | off | 25 | 311356103 | |
| `1793306720` | 10-29 20:45:20 | off | 22 | 214907420 | |
| `1793321975` | 10-30 00:59:35 | off | 17 | 170618975 | |
| `1793323820` | 10-30 01:30:20 | on | 2 | 21768368 | |
| `1793357934` | 10-30 10:58:54 | off | 38 | 396718353 | |
| `1793410220` | 10-31 01:30:20 | on | 58 | 630678090 | |
| `1793496620` | 11-01 01:30:20 | on | 96 | 728577330 | |
| `1793583020` | 11-02 01:30:20 | on | 96 | 880493103 | |
| `1793669420` | 11-03 01:30:20 | on | 96 | 964839522 | |
| `1793755820` | 11-04 01:30:20 | on | 96 | 700449067 | |
| `1793775818` | 11-04 07:03:38 | off | 23 | 154883747 | about 1,800 s after the package manager's run |
| `1793842220` | 11-05 01:30:20 | on | 73 | 604227513 | |
| `1793862240` | 11-05 07:04:00 | off | 23 | 307460576 | about 1,800 s after the package manager's run |
| `1793928620` | 11-06 01:30:20 | on | 73 | 959342877 | deferred in verify, then complete |
| `1793991789` | 11-06 19:03:09 | off | 71 | 1086535575 | 1,800 s after `crypto-deploy.service`'s reloads (TZ-41 report) |
| `1794015020` | 11-07 01:30:20 | on | 25 | 416674608 | |
| `1794101420` | 11-08 01:30:20 | on | 96 | 1639742990 | |
| `1794187820` | 11-09 01:30:20 | on | 96 | 1776573596 | new since TZ-41 |
| `1794274220` | 11-10 01:30:20 | on | 96 | 1251430567 | new since TZ-41 |

The two runs since TZ-41 began on the calendar, and §0.3's systemd records hold no reload since 2026-11-08. Their ledger records give `free_before` `8251629568` and `8004841472` bytes and `free_after` `10028630016` and `9256689664`.

**V6 — G-REHEARSAL** (`logs/50-rehearse.log`, one try, from 07:57:42 UTC). The four downloads at 08:00:17 to 08:00:19 UTC, held `153` s for the first (from second 762 of window 07:45 to second 15 of window 08:00), then 1.1, 0.8, 0.9 and 1.0 s, retries 0. Its last lines:

```
[2026-11-10T08:00:25Z] rehearsal: 150 markets, 387633 lines of stream, 5.6 s of processor, held 0 s; 451 lines sha256 1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd
[2026-11-10T08:00:25Z] G-REHEARSAL PASS: 451 lines sha256 1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd against the Architect's 451 lines sha256 1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd
```

`rehearsal.txt`: 103261 bytes, `1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd`. Processor `5.6` s, against §6's bound `6` and the `120` that blocks. Peak `50393088` bytes. `rehearsal-dl/` held no file afterwards.

**V7 — G-SET: PASS** (`logs/60-fetch.log`), quoted in §2.1: 9 candidates considered with their verdicts, 8 members, each with its markets, slots, files, bytes and polls; 20 document requests; 464 distinct markets, 23 resolved by their documents. Peak `68464640` bytes.

**V8 — the replay, twice** (`logs/70-replay.log`, 08:01:22 to 09:01:29 UTC; `logs/71-replay-again.log`, 09:03:01 UTC):
- **Units:** all 768 were inside the idle stretch, 0 ended after second 590, so none is listed (§2.4).
- **Projection:** 1,250 s after the first 24 units, against `3,000` (§2.4).
- **Day files:** every day's two files were written once (§2.5).
- **G-BOOK PASS**, 60,078 of 60,089 (§2.3).
- **The second run** replayed no day ("days to replay 0 of 8, 0 bytes of streams") and printed the same G-BOOK lines and the same timing summary.
- **Peaks:** `56725504` and `32735232` bytes.

**V9 — DETERMINISM** (`logs/80-rescore.log`):

```
[2026-11-10T09:04:06Z] wrote /root/tz43-work/rescore.txt 11614 bytes sha256 90bd9c8b0a85f3f55aef88674a3431ed7644cef621869e25b6c90f32b9ff9385
[2026-11-10T09:04:06Z] DETERMINISM PASS: 24 of 24 slot lines of day 1793404800 equal to the replay's
```

**24 of 24**: the first member day's first 24 slots were downloaded a second time and replayed from the day's start, and each slot's line equals the replay's byte for byte. Peak `52293632` bytes.

**V10 — the score, twice** (`logs/90-score.log`, `logs/91-score-again.log`):
- **The reading:** UNDECIDABLE (§4).
- **`reading.json`:** written at the first run, `175d3661…`, and `unchanged` at the second.
- **The read ledger** (`read-ledger.jsonl`, 7 lines, printed by `logs/98-closing.log`), one line for each mode that read the store, a Release or the set:

```
{"at": "2026-11-10T07:57:42Z", "at_ns": 1794297462914564015, "file_sha256": "48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf", "head": "ab0f3873a66eb302225c3849da362bfe301e93df", "mode": "rehearse"}
{"at": "2026-11-10T08:00:39Z", "at_ns": 1794297639153409220, "file_sha256": "48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf", "head": "ab0f3873a66eb302225c3849da362bfe301e93df", "mode": "fetch"}
{"at": "2026-11-10T08:01:22Z", "at_ns": 1794297682535460897, "file_sha256": "48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf", "head": "ab0f3873a66eb302225c3849da362bfe301e93df", "mode": "replay"}
{"at": "2026-11-10T09:03:01Z", "at_ns": 1794301381622811473, "file_sha256": "48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf", "head": "ab0f3873a66eb302225c3849da362bfe301e93df", "mode": "replay"}
{"at": "2026-11-10T09:03:09Z", "at_ns": 1794301389531728401, "file_sha256": "48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf", "head": "ab0f3873a66eb302225c3849da362bfe301e93df", "mode": "rescore"}
{"at": "2026-11-10T09:04:17Z", "at_ns": 1794301457976052784, "file_sha256": "48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf", "head": "ab0f3873a66eb302225c3849da362bfe301e93df", "mode": "score"}
{"at": "2026-11-10T09:04:28Z", "at_ns": 1794301468343100985, "file_sha256": "48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf", "head": "ab0f3873a66eb302225c3849da362bfe301e93df", "mode": "score"}
```

Every line carries the instrument's SHA-256 `48c3550b…` and the worktree's `HEAD` `ab0f387`.

**The instrument's commit reached `origin` before the first read.** It was on `origin` at **`2026-11-10T07:54:46.835116063Z`** (§3). The read ledger's first line, `rehearse`, is 175 s later, at 07:57:42 UTC. Its first `fetch` line is 352 s later, at 08:00:39 UTC.

**V11 — G-STILL: PASS.** `I still` recorded the units at 07:55:42 UTC (`logs/30-still.log`, §3.3 below) and compared them at 09:04:34 UTC (`logs/95-still.log`):

```
[2026-11-10T09:04:34Z] adv3-bot.service {'MainPID': '284419', 'NRestarts': '5', 'ActiveState': 'active'}, MemoryCurrent 5369856, MemoryPeak 51396608
[2026-11-10T09:04:34Z] btc-pairbook.service {'MainPID': '883760', 'NRestarts': '29', 'ActiveState': 'active'}, MemoryCurrent 1646592, MemoryPeak 48111616
[2026-11-10T09:04:34Z] btc-recorder.service {'MainPID': '2388318', 'NRestarts': '0', 'ActiveState': 'active'}, MemoryCurrent 118386688, MemoryPeak 375353344
[2026-11-10T09:04:34Z] btc-rewardbook.service {'MainPID': '3137952', 'NRestarts': '1', 'ActiveState': 'active'}, MemoryCurrent 13426688, MemoryPeak 78729216
[2026-11-10T09:04:34Z] btc-pairbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-10T09:04:34Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-11-10T09:04:34Z] btc-rewardbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-10T09:04:34Z] btc-rewardbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-11-10T09:04:34Z] the reward book archive's runs with records since the first read: []
[2026-11-10T09:04:34Z] G-STILL PASS: unchanged since 2026-11-10T07:55:42Z
```

The four units kept their `MainPID`, `NRestarts` and `ActiveState`. Neither archive ran, and the pair book's archive wrote no restart record. The capture units' journal of the last 24 h (§3.11, V15) holds only the pair book archive's calendar restart at 03:15:15 UTC, before the run.

**The four units at both reads, memory included:**

| unit | pid, `NRestarts` | `MemoryCurrent` at 07:55:42 | at 09:04:34 | `MemoryPeak` |
|---|---|---|---|---|
| `btc-recorder.service` | `2388318`, `0` | `22937600` | `118386688` | `375353344` |
| `btc-pairbook.service` | `883760`, `29` | `18141184` | `1646592` | `48111616` |
| `btc-rewardbook.service` | `3137952`, `1` | `14868480` | `13426688` | `78729216` |
| `adv3-bot.service` | `284419`, `5` | `6303744` | `5369856` | `51396608` |

**V12 — the hook:**
- **`opens refused: 0`** at every mode run, 18 of 18 before B-RECLAIM-OWN, each printed in its `finally` lines: `fingerprint` ×2, `number` ×2, `selftest`, `still` ×2, `scratch`, the Boss's `reclaim`, `archive` ×2, `rehearse`, `fetch`, `replay` ×2, `rescore` and `score` ×2.
- **`reward book opens`:** `1650` at `fetch` and `0` at every other mode.

B-RECLAIM-OWN's `reclaim` printed `opens refused: 0; reward book opens: 0` as well: 19 of 19 mode runs in all.

**V13 — memory and disk.** `malloc tuned: True` at every mode run, 19 of 19 with B-RECLAIM-OWN's `reclaim`. The peaks:

| mode | peak (bytes) |
|---|---|
| `fingerprint` | `33636352`, `33505280` |
| `number` | `31014912`, `31408128` |
| `selftest` | `34422784` |
| `still` | `31404032`, `32190464` |
| `scratch` | `31424512` |
| `reclaim` (the Boss's, B-RECLAIM-SCRATCH) | `33652736` |
| `archive` | `32997376`, `33128448` |
| `rehearse` | `50393088` |
| `fetch` | `68464640` |
| `replay` | `56725504`, `32735232` |
| `rescore` | `52293632` |
| `score` | `36450304`, `36446208` |
| `reclaim` (B-RECLAIM-OWN) | `34795520` |

Every peak is under the modelled `71796447`. The largest, `fetch`'s `68464640`, is `1.143` times the Architect's `59,887,616` for these bytes, which is under the `1.199` the floor models (§6 item 9).

**The floors' reads.** Every mode that reads the store, a Release or the set read the floors at its start, and every read passed at its first try:

| mode | instant (UTC) | `MemAvailable` (floor `143592894`) | free (floor `7800000000`) |
|---|---|---|---|
| `rehearse` | 07:57:42 | `228012032` | `10519879680` |
| `fetch` | 08:00:39 | `217313280` | `10504372224` |
| `replay` | 08:01:22 | `353366016` | `10462830592` |
| `replay` again | 09:03:01 | `198000640` | `10330320896` |
| `rescore` | 09:03:09 | `180871168` | `10330202112` |
| `score` | 09:04:17 | `214360064` | `10328895488` |
| `score` again | 09:04:28 | `210153472` | `10328645632` |

The host gate's own reads were `331935744` at 07:52:59 and `314875904` at 09:04:50, `df` avail `10555289600` and `10328178688`. `free -b` at §3.11: `1002127360` total, available `352038912`; swap `3250581504`, `921763840` used. The self-test's `MemAvailable` lines at 07:55:19 are its own literals around the floor, not reads of the host. Each unit read free space before its download, and none came near `DISK_FLOOR` `7400000000`; the lowest mode read was `10328645632`.

**V14 — the separation self-check:** §3.

**V15 — §3.11's closing reads** (`logs/96-host-gate-again.log`, `logs/97-archive-again.log`, `logs/98-closing.log`):
- **Host gate again:** 11 of 11 (V2).
- **Archive again:** as at §3.4 (V5).
- **`systemctl show` of the six units:** the four capture and advisor units as at G-STILL, with `MemoryCurrent` recorder `10887168`, pair book `1708032`, reward book `12664832` and advisor `671744`; both archive services `inactive`, `MainPID=0`.
- **The capture units' journal of the last 24 h:** five lines, the pair book archive's restart at 03:15:15 to 03:15:20 UTC (pid `751579` stopped, restart counter 29).
- **`free -b`:** as above.
- **`du -sb /root/tz43-work`:** `56848937`.
- **`state.json` and the read ledger:** printed, as quoted in V10 and §3.3.
- **`wc -l`:** `768 timing-replay.jsonl`, `24 timing-rescore.jsonl`, `792 total`.

**V16 and V17 — the reclaims and the removals:** B-RECLAIM-SCRATCH in §3.3 below, B-RECLAIM-OWN in §9 below.

**V18 — the classifier:**

| block | refused at | reason | handed over | the Boss ran it | verified by |
|---|---|---|---|---|---|
| B-RECLAIM-SCRATCH's `reclaim` | 07:56 UTC, before it ran | "[Irreversible Local Destruction]" | §3.3's paste, unchanged, with the three earlier directories' paths written in, in Russian, at about 07:57 UTC | `2026-11-10T07:58:24.028252868Z` | `logs/32-reclaim-scratch.log` and the Executor's own `test -e` of each directory at 07:59:26 UTC |

`logs/32a-reclaim-scratch-refused.log` records the refusal at `2026-11-10T07:56:24.784585224Z`: the attempted line, `32-reclaim-scratch.log` absent (exit 1), the forensic store at 2417 files, six directories under the scratch parent, and the three earlier ones present (exit 0 each). No other block or line was refused. B-RECLAIM-OWN's `reclaim`, `git worktree remove`, `rm -rf` and reads were run by the Executor, and none was refused.

### §3.3 — `I still`, `I scratch` and B-RECLAIM-SCRATCH (V16, V17)

`I still` (`logs/30-still.log`, 07:55:42 UTC) recorded in `state.json`:

```
[2026-11-10T07:55:42Z] adv3-bot.service {'MainPID': '284419', 'NRestarts': '5', 'ActiveState': 'active'}, MemoryCurrent 6303744, MemoryPeak 51396608
[2026-11-10T07:55:42Z] btc-pairbook.service {'MainPID': '883760', 'NRestarts': '29', 'ActiveState': 'active'}, MemoryCurrent 18141184, MemoryPeak 48111616
[2026-11-10T07:55:42Z] btc-recorder.service {'MainPID': '2388318', 'NRestarts': '0', 'ActiveState': 'active'}, MemoryCurrent 22937600, MemoryPeak 375353344
[2026-11-10T07:55:42Z] btc-rewardbook.service {'MainPID': '3137952', 'NRestarts': '1', 'ActiveState': 'active'}, MemoryCurrent 14868480, MemoryPeak 78729216
[2026-11-10T07:55:42Z] btc-pairbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-10T07:55:42Z] btc-pairbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-11-10T07:55:42Z] btc-rewardbook-archive.timer {'Result': 'success', 'ActiveState': 'active', 'SubState': 'waiting', 'UnitFileState': 'enabled'}
[2026-11-10T07:55:42Z] btc-rewardbook-archive.service {'Result': 'success', 'ActiveState': 'inactive', 'SubState': 'dead', 'UnitFileState': 'static'}
[2026-11-10T07:55:42Z] still: recorded
```

`I scratch /tmp/claude-0/-root-btc-5m-twap/fd099d3c-2537-55ea-a4a0-314ac50cff1f` (`logs/31-scratch.log`, 07:55:43 UTC):

```
[2026-11-10T07:55:43Z] running 630626 started 2026-11-08T07:15:37Z claude
[2026-11-10T07:55:43Z] running 630636 started 2026-11-08T07:15:39Z claude
[2026-11-10T07:55:43Z] running 630645 started 2026-11-08T07:15:40Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-10T07:55:43Z] running 630666 started 2026-11-08T07:15:42Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-10T07:55:43Z] running 906576 started 2026-11-10T07:48:39Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-10T07:55:43Z] 238335b9-cf23-414a-8e8f-ad4705c4d19e born 2026-10-30T13:16:00Z: earlier
[2026-11-10T07:55:43Z] 671824f6-69c4-539d-95a5-49d150ddfb52 born 2026-11-08T07:20:34Z: earlier
[2026-11-10T07:55:43Z] 8e3e58b1-5f4a-46d7-8814-25078c677104 born 2026-11-10T07:48:40Z: live, process [906576]
[2026-11-10T07:55:43Z] c78295f5-9a1d-4177-ac5a-b93cd56a49da born 2026-11-08T07:15:42Z: live, process [630626, 630636, 630645, 630666]
[2026-11-10T07:55:43Z] c82149c8-0336-4f7c-89f2-cbb58ba0ea88 born 2026-11-08T07:20:32Z: earlier
```

**Three directories earlier, two live.** `238335b9…` and TZ-41's own `671824f6…` are as map §3 expected. `c82149c8…`, live at TZ-41's run, is earlier now: the process `631231` it was born with no longer runs. `c78295f5…` is still live, with the remote-control processes of 2026-11-08 07:15 UTC. `8e3e58b1…` was born 1 s after this session's process `906576` started; it is the directory beside the session's own that map §6 (harness) describes.

B-RECLAIM-SCRATCH named the three earlier directories, every one `scratch` named earlier, as §3.3's rule says (map §7 item 150). Its log, `logs/32-reclaim-scratch.log`, was written by the Boss's run. Every line is quoted below, unfiltered. The first line carries his terminal's OSC 133 marker, `ESC ] 133 ; C BEL`, written by his shell:

```
]133;C2026-11-10T07:58:24.028252868Z
[2026-11-10T07:58:24Z] reclaim: 3735 report tokens; forensic store holds 2417 files
[2026-11-10T07:58:24Z] RECLAIM PASS: 15 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 2417 -> 2417 files
[2026-11-10T07:58:24Z] malloc tuned: True
[2026-11-10T07:58:24Z] peak memory of this run: 33652736 bytes
[2026-11-10T07:58:24Z] opens refused: 0; reward book opens: 0
exit=0
2026-11-10T07:58:24.319615505Z
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
```

The three `rm -rf` printed `exit=0` and each `test -e` `exit=1`. **The Executor's own reads at 07:59:26 UTC:** `test -e` of each of the three printed `exit=1`. The parent then held `8e3e58b1…`, `c78295f5…` and this session's `fd099d3c…`, and the forensic store held `2417` files.

### §9 — B-RECLAIM-OWN (V16, V17)

The Executor ran B-RECLAIM-OWN after §3.11, with this report drafted, from 09:11:06 UTC; none of its lines was refused. Its output was written to no file and is quoted here verbatim from the session, every line:

```
$ cd /root/tz43-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz43-work/wt/research/tz43-l0-our-quote.py reclaim /root/tz43-work
[2026-11-10T09:11:06Z] reclaim: 3836 report tokens; forensic store holds 2417 files
[2026-11-10T09:11:06Z] reclaim: /root/tz43-work/wt skipped: no file but its HEAD's, and HEAD ab0f3873a66eb302225c3849da362bfe301e93df is its upstream's
[2026-11-10T09:11:06Z] R copied 257ac840d8a5c6bd60579e0def9107465bbb409b59e2f15cb526583923eeb874 /root/btc-forensics/tz43-work--read-ledger.jsonl
[2026-11-10T09:11:06Z] R copied 175d366101cd825437a1cd393aa57642965f7ffb9fe831746c2d9b2187d50be1 /root/btc-forensics/tz43-work--reading.json
[2026-11-10T09:11:06Z] R copied 1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd /root/btc-forensics/tz43-work--rehearsal.txt
[2026-11-10T09:11:06Z] R copied 90bd9c8b0a85f3f55aef88674a3431ed7644cef621869e25b6c90f32b9ff9385 /root/btc-forensics/tz43-work--rescore.txt
[2026-11-10T09:11:06Z] R copied 904f1b9b8244a15fe48549e39ffc879f68ad31de6963a41c05f5afc607edf0f7 /root/btc-forensics/tz43-work--set.json
[2026-11-10T09:11:06Z] R copied 31257121ffbab162f73b03a14643623198ea38c4c1285bba8c0c294f22122ce9 /root/btc-forensics/tz43-work--state.json
[2026-11-10T09:11:06Z] R copied 4300297dc853f03edd7edc3e70482715acc951dd3fc325df52d2b18ba3e64c65 /root/btc-forensics/tz43-work--timing-replay.jsonl
[2026-11-10T09:11:06Z] R copied a938e1b1010252604ae1e85f5371623721d7953b85f38c5b763355fd5453674c /root/btc-forensics/tz43-work--timing-rescore.jsonl
[2026-11-10T09:11:06Z] R copied d93f998fba7795f30379c06e2058c55f4eba9d0c340536a3d5a4d1636b765ee6 /root/btc-forensics/tz43-work--days--1793404800.json
[2026-11-10T09:11:06Z] R copied ec4494031d22891f22ec2822287c0127c4f96f39dac1337f3980419813052400 /root/btc-forensics/tz43-work--days--1793404800.slots.txt
[2026-11-10T09:11:06Z] R copied 50e19969a8196ef3fe8b069056b75bb3ff5f5ba1c41a9ad70a48bd7e88ebaaae /root/btc-forensics/tz43-work--days--1793491200.json
[2026-11-10T09:11:06Z] R copied 5a7169dbcdb3186b588e2bd77ef5017dc792f1ead7cc8d2b9c11a55cee90f763 /root/btc-forensics/tz43-work--days--1793491200.slots.txt
[2026-11-10T09:11:06Z] R copied 93c76d1594b1edef03e192c02cc67b0264e43ca4b77b6d49939845f5876dc57c /root/btc-forensics/tz43-work--days--1793577600.json
[2026-11-10T09:11:06Z] R copied aae9a59997c591b90672bec21ea2489e2f7e654eba03590bc8d1ff411a186e1c /root/btc-forensics/tz43-work--days--1793577600.slots.txt
[2026-11-10T09:11:06Z] R copied a80c3d721fce47537ff927c42b989cd4409d25b7c3a1e2c4e024a2463d48c54d /root/btc-forensics/tz43-work--days--1793664000.json
[2026-11-10T09:11:06Z] R copied dc9dff0e13153ee045ada2cb805c9567ce9bb4b490f88c40aa0821442fe8660b /root/btc-forensics/tz43-work--days--1793664000.slots.txt
[2026-11-10T09:11:06Z] R copied 4f9ca91d2798fb9f7b496e98baa02d4fe9f6efb5f60f979540f682fb7fdadfa9 /root/btc-forensics/tz43-work--days--1793750400.json
[2026-11-10T09:11:06Z] R copied 71101c5d670141ce064c671824d5c8c8c1615ffce4801b1a422baa3df4281cdc /root/btc-forensics/tz43-work--days--1793750400.slots.txt
[2026-11-10T09:11:06Z] R copied e7266b1d2d05e1191095e9cd184e6bb15571ea7380fa1e4f51db90a5342e200d /root/btc-forensics/tz43-work--days--1793836800.json
[2026-11-10T09:11:06Z] R copied ec5792be99ff4169b4574b3a8ce04855ad7a5fcd51aba1b51baf4cc9d8ce44e5 /root/btc-forensics/tz43-work--days--1793836800.slots.txt
[2026-11-10T09:11:06Z] R copied f3018bb242bff3b1d7483622cd4065074cc42faa90b1e8357d223c2796a6dfd5 /root/btc-forensics/tz43-work--days--1794009600.json
[2026-11-10T09:11:06Z] R copied a0fdb71edc318fb7e41989c1aca3b591c9b3e4db39274e87588354639725c1e6 /root/btc-forensics/tz43-work--days--1794009600.slots.txt
[2026-11-10T09:11:06Z] R copied 910ed69e85ab28dc81a334538d229a66ba17107260325c1afe5eae95de02e91f /root/btc-forensics/tz43-work--days--1794096000.json
[2026-11-10T09:11:06Z] R copied 00caaab0888d85779398751281da3e9219cfdf9742c77b5914499cf0c4421436 /root/btc-forensics/tz43-work--days--1794096000.slots.txt
[2026-11-10T09:11:06Z] R copied 5f56487e44aadcba1df2bc1316a889605baf83a4fcafc965b5ee4a18a6fec9b2 /root/btc-forensics/tz43-work--fetch--1793404800.json
[2026-11-10T09:11:06Z] R copied 53ae4e79d354b3f8b35d497654159162b9c2290deb0d69b6f62b79c3fe8c1d71 /root/btc-forensics/tz43-work--fetch--1793404800.polls.jsonl
[2026-11-10T09:11:06Z] R copied 55f95448c4ba6abe1d1b154ff0e014ef190ffb7be861a7f6cb1a3bcddec7a1bd /root/btc-forensics/tz43-work--fetch--1793491200.json
[2026-11-10T09:11:06Z] R copied 1aac9148f26b55664b248be60b62394defc1b117b63bcd952c632bf96b3ebf54 /root/btc-forensics/tz43-work--fetch--1793491200.polls.jsonl
[2026-11-10T09:11:06Z] R copied 8589729bfe267feb57208833064bc71006e592e22edd8290d70bbc2b4474d9b5 /root/btc-forensics/tz43-work--fetch--1793577600.json
[2026-11-10T09:11:06Z] R copied 19d765c78c93e9d4175328615ae3dc27b3e2f0c1dd7f6084eeab672a9e56427c /root/btc-forensics/tz43-work--fetch--1793577600.polls.jsonl
[2026-11-10T09:11:06Z] R copied 1405b48ac2459f052b5b36dea8e85dd6cb0e112b49ac21030955d96f890eec02 /root/btc-forensics/tz43-work--fetch--1793664000.json
[2026-11-10T09:11:06Z] R copied 4a5ef449ed6b1d2bf1378b817671b9bb3cac477c5a9fa6e5068d9673b24977cb /root/btc-forensics/tz43-work--fetch--1793664000.polls.jsonl
[2026-11-10T09:11:06Z] R copied 1ed8768bd80b54220c0437e15fc424943a8829b716d7ba70f2b586f5ae14099c /root/btc-forensics/tz43-work--fetch--1793750400.json
[2026-11-10T09:11:06Z] R copied f06145aa32845b9f3a65b8616e5842218b03869a3fc18d5a4bf1aaaa57fec920 /root/btc-forensics/tz43-work--fetch--1793750400.polls.jsonl
[2026-11-10T09:11:06Z] R copied 7d502a56ad2a4a3f95150bbcfc8c52c1190f2b977d9d1a72e2e1c4b3c2f5ba25 /root/btc-forensics/tz43-work--fetch--1793836800.json
[2026-11-10T09:11:06Z] R copied 7918f3b6629489fcff4fd22cdb049a89e1e1ef63b86738c73ec680e17e5eff5d /root/btc-forensics/tz43-work--fetch--1793836800.polls.jsonl
[2026-11-10T09:11:06Z] R copied 29e17ecde5f5d705e297bdc2be7e5e150aa50d06c3ac66ba9b1c4c13225b5708 /root/btc-forensics/tz43-work--fetch--1794009600.json
[2026-11-10T09:11:06Z] R copied 91582ccfb9145559277d196f61e804e6be205d0b18d6168a1db6975711d6cf15 /root/btc-forensics/tz43-work--fetch--1794009600.polls.jsonl
[2026-11-10T09:11:06Z] R copied a3ebc56744facb5c00f862c1f5d70a564672b68b5cc276398f32ae7f1bc0c552 /root/btc-forensics/tz43-work--fetch--1794096000.json
[2026-11-10T09:11:06Z] R copied 7b0d86338359fbb4d5f4f7b54c6f36e0d45f2ed5c4d6d5731358c8e4e3099a82 /root/btc-forensics/tz43-work--fetch--1794096000.polls.jsonl
[2026-11-10T09:11:06Z] R copied 93ca8e4b234b74f921564e8a405dd506807067d332e5d28de45496156844f639 /root/btc-forensics/tz43-work--logs--00-instant.log
[2026-11-10T09:11:06Z] R copied faf1dbaa37386aa7e8810b1662b471a14b21009a82de135a808dbaf8079295b7 /root/btc-forensics/tz43-work--logs--01-stage.log
[2026-11-10T09:11:06Z] R copied c79ffb527bf298ec4d923e3ba2c7a6c13d08b641403a49a18c6f84b8886816c0 /root/btc-forensics/tz43-work--logs--02-fingerprint.log
[2026-11-10T09:11:06Z] R copied 5047f7b8ce68af120e2273b74a7af5795fdda544097ff135976765283ae78e24 /root/btc-forensics/tz43-work--logs--03-host-gate.log
[2026-11-10T09:11:06Z] R copied 2c38971a0746ead31bcddbc7a45fe9b7138a39b3a79444dadd7702fee46a136b /root/btc-forensics/tz43-work--logs--05-number.log
[2026-11-10T09:11:06Z] R copied ca97c716706f22d59ff41bc88f2cf1891573a981d98f6ae6bbfca3558f56cf8c /root/btc-forensics/tz43-work--logs--05-refs.log
[2026-11-10T09:11:06Z] R copied 49ea472313144593d62a429797ee3371254023b6135809a99a12164f33110175 /root/btc-forensics/tz43-work--logs--10-number.log
[2026-11-10T09:11:06Z] R copied c20411347d9ca19614be301de3bdf91d1e9c7a41e9a4ad942354e0e5e5fc6071 /root/btc-forensics/tz43-work--logs--11-worktree.log
[2026-11-10T09:11:06Z] R copied df3d56839f284316e7b9749fe3abb3d640bf02b2ddf1d1f63bc461c293312933 /root/btc-forensics/tz43-work--logs--12-fingerprint.log
[2026-11-10T09:11:06Z] R copied 48219a86fbc350811d7f1746e31edb7646d2c6698688e37e7070a78bc08633d6 /root/btc-forensics/tz43-work--logs--13-push.log
[2026-11-10T09:11:06Z] R copied c09b22bc5711f2d827c8de5ff856825a904f03c566d3225441c0014b3233370d /root/btc-forensics/tz43-work--logs--14-pr.log
[2026-11-10T09:11:06Z] R copied d7185deee0d095f8b7fbaeb87d171f31c6834121ccda831bcae75551e62d2af6 /root/btc-forensics/tz43-work--logs--20-selftest.log
[2026-11-10T09:11:06Z] R copied 0ae793dd45d1678ac121ee8acc54cec7c7d139dd10b4f4ee92edc7cd4c264af6 /root/btc-forensics/tz43-work--logs--30-still.log
[2026-11-10T09:11:06Z] R copied 0c7af015ab5c734cf2ddb3615f4d9bd50fc70788c5d5da195b37fa43d360772c /root/btc-forensics/tz43-work--logs--31-scratch.log
[2026-11-10T09:11:06Z] R copied fa4647b3c53d5971af6b4f8e01b92dacf603ffe56d139892bbf6301fe50a9be0 /root/btc-forensics/tz43-work--logs--32-reclaim-scratch.log
[2026-11-10T09:11:06Z] R copied 9a4d2d1365e3598939863593268a4836bc6517833b90c9723a215e0cb4af4d88 /root/btc-forensics/tz43-work--logs--32a-reclaim-scratch-refused.log
[2026-11-10T09:11:06Z] R copied 161b3c5407cc58cdb93fe7dc6815614e1dc363d4c95fab50742b52719377ef53 /root/btc-forensics/tz43-work--logs--40-archive.log
[2026-11-10T09:11:06Z] R copied c290f8ad6f456a6a9d59764f6854fc33c63949a0a324b5ecec19b4b4bdf8055e /root/btc-forensics/tz43-work--logs--50-rehearse.log
[2026-11-10T09:11:06Z] R copied d2cbf48aac07fae8eda5ff16888ffcda9e604ce0c46756d2ccf9a2767d894d99 /root/btc-forensics/tz43-work--logs--60-fetch.log
[2026-11-10T09:11:06Z] R copied 7c2402c07d859898a227de058b8d3f6e0c80971db069bad7d89d863a95356fb8 /root/btc-forensics/tz43-work--logs--70-replay.log
[2026-11-10T09:11:06Z] R copied c24910c79df907bb0c92796c5786c580429beb2980eac8ed241f4d7edc71946a /root/btc-forensics/tz43-work--logs--71-replay-again.log
[2026-11-10T09:11:06Z] R copied a666e7e576958002449205ac1600f6a0bb3e958975ad56730fb5e5f63084df1e /root/btc-forensics/tz43-work--logs--80-rescore.log
[2026-11-10T09:11:06Z] R copied 1707d544dea9092231ef1791a09a4e9fdb7451d8c4526503d2c7334a5aefcc6d /root/btc-forensics/tz43-work--logs--90-score.log
[2026-11-10T09:11:06Z] R copied 0c84a9f734f395e703b6e7393349a4393a47b4e702d8ef8aa1403bbe396adda8 /root/btc-forensics/tz43-work--logs--91-score-again.log
[2026-11-10T09:11:06Z] R copied f27ad6ad2d82ae55c84397e2a66851ba68825d14633232a8c53146404497da42 /root/btc-forensics/tz43-work--logs--95-still.log
[2026-11-10T09:11:06Z] R copied b1052d91a0b7dec5b3c0cbd6fa36aa2b1525b0943f721795efe6e90155164ba7 /root/btc-forensics/tz43-work--logs--96-host-gate-again.log
[2026-11-10T09:11:06Z] R copied 3227b1516d9dfb49b7ee48b2b48bbeea88a600a50a10055bc5ff2fab60610021 /root/btc-forensics/tz43-work--logs--97-archive-again.log
[2026-11-10T09:11:06Z] R copied 3010f3a80fed5dc71353a79330768ff55ec9509d070f137aa1c275686900e37e /root/btc-forensics/tz43-work--logs--98-closing.log
[2026-11-10T09:11:06Z] R copied 0da9f7314153036ac106f56d0dadb7ef574d33a19c5d8067a04a60e63876fe82 /root/btc-forensics/tz43-work--logs--99-separation.log
[2026-11-10T09:11:06Z] R copied 48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf /root/btc-forensics/tz43-work--stage--research--tz43-l0-our-quote.py
[2026-11-10T09:11:06Z] RECLAIM PASS: 70 files considered, 70 named by a report, 0 kept by name, 70 copied, 0 already held; forensic store 2417 -> 2487 files
[2026-11-10T09:11:06Z] malloc tuned: True
[2026-11-10T09:11:06Z] peak memory of this run: 34795520 bytes
[2026-11-10T09:11:06Z] opens refused: 0; reward book opens: 0
$ cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz43-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz43-work; echo "exit=$?"
exit=0
$ test -e /root/tz43-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       12fb07b [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
2487
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks       Avail
/dev/vda2      31612203008 10327752704
```

**What this shows:**
- **The 70 files:** every file the run wrote in its tree but the worktree's, each named by this report's SHA-256 (§2.6), so none counted as "kept by name". Every log, `state.json` and `read-ledger.jsonl` is among the 70.
- **The worktree** held exactly its pushed `HEAD` `ab0f387`, its upstream's; `git worktree remove` ran without `--force`, exit `0`.
- **The removal:** `test -e /root/tz43-work` printed exit `1`. The worktrees registered are the primary checkout and `/root/btc-recorder-svc`, and nothing else.
- **The store:** 2,487 = 2,417 + 70 copies. The Executor then hashed the 70 copies `/root/btc-forensics/tz43-work--*`, and each hash is among this report's, 70 of 70.
- **What stays:** the branch `tz-43-l0-our-quote` stays on `origin` and as a local ref at `ab0f387`. The running units' code trees, the capture roots, both archives' state and the forensic store are kept.

---

## 6. What could not be implemented as written

1. **Contract §1, and the reads before §0.0.**
   - Contract §1 step 1 ran as `git fetch origin` and `git pull --ff-only origin main`, the primary checkout already on `main`. That moved `main` from `e2458af` to `12fb07b`.
   - Before §0.0's clock line the session ran read-only steps: `git log`, `git branch -a`, `ls`, `hostname`, `uptime`, one `date -u` (07:49:44 UTC, inside the band), `get_session`, and reads of the TZ, the map in sections, the contract, TZ-41's report and the session's memory files. Nothing was written.
2. **Two uploads, not one.** TZ-43's header has the Boss upload "in one upload" this file and revision `2026-11-08-a`. `main` carries them as two commits 40 s apart: `183a022` (the map, 13:53:44 UTC) and `12fb07b` (the TZ, 13:54:24 UTC). Both are on `main` before the run, and §0.2 and §0.5 read them; nothing was blocked or changed.
3. **The refs: 134 lines against the Architect's 132** (§5, §0.5). `refs/heads/tz-41-l0-our-quote` is gone from `origin`, and its commit `cca1109` is still served as `refs/pull/42/head`. PR #42's merge ref is gone, which is consistent with TZ-41's verdict closing it. Each archive has two new tags, its calendar runs of 2026-11-09 and 2026-11-10. TZ-43 §0.5 records such a difference without blocking.
4. **The classifier refused B-RECLAIM-SCRATCH's `reclaim`** ("[Irreversible Local Destruction]"), as in every TZ since TZ-37 (V18).
   - **Handed over:** the Executor handed §3.3's paste over once, unchanged, with the three paths written in by hand, in Russian.
   - **Run:** the Boss ran it at 07:58:24 UTC, about two minutes later. The Executor verified it from its log and by its own `test -e`.
   - **Meanwhile:** §3.4 ran while the paste waited, as §3.3 allows.
   - **A push that did not go out:** the session also tried one push notification to the Boss's phone through Claude Code's own tool. It was not sent ("Remote Control inactive"). It is not a request from the host.
5. **Logs beyond §3's table:**
   - `logs/32a-reclaim-scratch-refused.log`, the refusal's record.
   - `logs/99-separation.log`, which holds contract §4.2's self-check (V14); §3's table names no log for it.
   - `logs/05-refs.log` has `main`'s first-parent commits above `e2458af` appended under a `date -u` line, for §0.5's commit list.
   - Most logs end with an `exit=` line that the Executor's command appended after the mode's own output.
6. **Reads the session printed outside `logs/`.** None printed a member's, fill's or poll's figure (§2 item 10). They were:
   - **Verification after the Boss's paste:** three `test -e`, `ls` of the scratch parent, and `find /root/btc-forensics -type f | wc -l`.
   - **The replay's and the rescore's progress:** line counts, the last records and per-window sums of `timing-replay.jsonl` and `timing-rescore.jsonl`, files of slots, seconds and bytes.
   - **Small files and listings:** `cat` of `state.json` and `read-ledger.jsonl`; `ls -la` of the work tree and of `fetch/`, which print names and sizes; `free -b`.
   - **Hashes and sizes:** `sha256sum` and `stat` of every file of the work tree (§2.6).
   - **Log reads for this report:** reprints and `grep`s of lines of `logs/` — the fingerprint rows, the archive's runs, `fetch`'s lines, the refs, the floors, the peaks and the hook's counts — and `logs/90-score.log`'s money lines reformatted as the tables at this report's head.
   - **Comparisons:** `diff`s of the two fingerprint logs, the two host-gate logs, the two archive logs and the two score logs.
   - **Before B-RECLAIM-OWN:** `git status --porcelain --ignored` and `git rev-parse HEAD @{u}` in the worktree, and a check that this draft names every file's SHA-256 and holds no condition id.

   All are hash, size or count commands, or reads of files §2 item 10 lets be printed. TZ-43 §0.0 sends every command's output to `logs/`, and these went to the session.
7. **The map was read in sections:** §0 in full, §1's refs records and its pull-request rows, §2.5 from the pair book on, §2.6, §3's code table and its end, §6's rows, and §7 items 115 to 152. These hold every section TZ-43's header names (map §7 items 139 and 141); `fingerprint` reads every row. **Appendix A was read in full**, and verified by hash at both extractions.
8. **The commit's author is the host's git default,** `root <root@vultr.guest>`, as for TZ-40 and TZ-41 (map §7 items 146 and 152).
9. **`fetch` peaked at `68,464,640` bytes on the host.** That is `1.143` times the Architect's `59,887,616` for these bytes at the set's full size. It is under the modelled host peak `71,796,447` and under the `1.199` ratio the floor models (§0.4; map §7 item 131's pattern). The floor, `143,592,894`, is `2.097` times this peak, and no `MemAvailable` read fell below it (V13).
10. **`rescore` prints no timing summary line**, where TZ-43 §8 asks for "the timing files' summary lines". `mode_rescore` calls no `timing_summary`, so the rescore's summary in §2.4 is the Executor's own read of `timing-rescore.jsonl`, a file of slots, seconds and bytes. The replay's summary line is the instrument's.
11. **The self-test's `MemAvailable` lines** in `logs/20-selftest.log` are its own literals around the floor, from `floor_check`'s test (Appendix A lines 2723 to 2731). They are not reads of the host, and V13 counts none of them.
12. **The report was drafted while the run went on.**
    - **During the replay:** §0 and the static parts of §1, §3 and §5 were written while the replay ran, with marked gaps. Each gap was filled from the logs.
    - **Before B-RECLAIM-OWN:** the draft held every file's SHA-256 that it now holds, and every figure but B-RECLAIM-OWN's own.
    - **After it:** the Executor added B-RECLAIM-OWN's output and the counts it gives, and reworded sentences that changed no figure and no hash: the executor-model line, §2.1's note on the `wrote` lines, §2.4's wall-clock line, this section's items 6 and 12, and the B-RECLAIM-OWN lines of the opening, V12, V13 and V18.
13. **A read after B-RECLAIM-OWN:** `sha256sum` of the 70 copies `/root/btc-forensics/tz43-work--*`, each hash matched against this report, 70 of 70. §9 names that read for a run of the Boss's; the Executor made it although it ran the block itself, and printed only the count.
