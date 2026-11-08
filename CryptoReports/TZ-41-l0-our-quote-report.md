# TZ-41 — L0, our quote on the venue's reward markets — REPORT

**Status: BLOCKED at §3.6, G-SET.** `I fetch` stopped on its own assert. It formed **7 members** of the 8 the set needs, from the candidates 2026-10-31 to 2026-11-07. **One candidate, 2026-11-06, is not a member:** its slot `1793949300` (07:15 UTC) fails the stream rule with "a gap above 15 s". That pushed the walk to 2026-11-08, a day that has not ended: `AssertionError: BLOCKED: day 1794096000 (2026-11-08T00:00:00Z) has not ended; the set needs it`. TZ-41 §1 names this case: "`fetch` … stops BLOCKED … at once where a non-member pushes the walk to a day not yet ended … Begun on 2026-11-08, the run absorbs no non-member". §3.6 lets only a network failure run again, so this BLOCK is final.

- **L0's reading: none.** No day was replayed, no money was computed and `score` did not run. Without the set, `replay` (§3.7), `rescore` (§3.8) and `score` (§3.9) had no PASS to stand on, and §3 sends the run to §3.10, §3.11 and §9.
- **G-REHEARSAL: PASS**, on the third and last try §3.5 allows. 451 lines, SHA-256 `1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd`, equal to the Architect's. The first two tries failed on the network: six attempts each, the last `HTTP 503`. The cause was GitHub's own incident, "Increase in timeouts for some unauthenticated users", 10:36:05 to 12:32:35 UTC (§6).
- **G-SET: BLOCKED** (above). 8 candidates considered: 7 members, 1 non-member with its reason. The walk reached the ninth candidate, 2026-11-08, and stopped.
- **G-BOOK and DETERMINISM: not run.**
- **The instrument's commit on `origin`:** `cca11090695ae824c94a6f097959d93355ce3986`, read there at `2026-11-08T10:41:57.957360176Z`. The read ledger's first line is `rehearse` at 10:44:20 UTC, and its first `fetch` line is at 12:46:07 UTC; both come after the commit.
- **G-STILL: PASS.** The recorder, the pair book, the reward book and the advisor are unchanged from 10:42:27 to 12:47:21 UTC.
- **The classifier refused one block:** B-RECLAIM-SCRATCH's `reclaim`, as "[Irreversible Local Destruction]". It was handed over unchanged and the Boss ran it at 11:18:19 UTC; verified from its log and by `test -e` (§5, V16 and V18).
- **The reward book's store was read** by `I fetch`, for the 8 candidate days 2026-10-31 to 2026-11-07, as §2 item 3 allows. No price, size, rate, competitiveness or outcome of any member is printed here (§2 item 10). The per-member files it wrote under `/root/tz41-work/fetch/` went with the tree (§6).

---

## 0. Fingerprint

`I0 fingerprint` (`logs/02-fingerprint.log`, 10:40:26 UTC) and `I fingerprint` (`logs/12-fingerprint.log`, 10:41:35 UTC) both printed:

```
FINGERPRINT PASS: revision 2026-11-01-b; anchors 6 of 6, 4 re-derived; rows 60: frozen 57 of 57 equal, tracked 2, reported 1
```

**Revision string:** `2026-11-01-b`, equal to TZ-41's header. **Anchors:**

| anchor | map | re-derived |
|---|---|---|
| `A1` — observation set | `229a944f2d51` | — |
| `A2` — collector | `6c5089330629` | `research/twap-divergence.py` sha256[:12] `6c5089330629`, equal |
| `A3` — phase | `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable` | — |
| `A4` — executor contract | `437b45ea196b` | `BTC-EXECUTOR-INSTRUCTIONS.md` sha256[:12] `437b45ea196b`, equal |
| `A5` — recorder | `0f6c90451cbd` | `research/recorder/recorder.py` sha256[:12] `0f6c90451cbd`, equal |
| `A6` — pricer | `729f0bcdbee3` | `research/pfair.py` sha256[:12] `729f0bcdbee3`, equal |

**The map's §0 table, every row as the instrument printed it** from the primary checkout at `main` `2eeb26c`. The two runs printed identical rows.

| path | lines | bytes | state | SHA-256 |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 2033 | 536884 | reported | `1396fa805e9eb72cc36f449c60698822f8d4c2e5314fdd6856f030e07fc46472` |
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

**The executor model** is the model TZ-41's header names. The session's own record, read by `get_session`, gives that model for `configured_model`, `session_context.model` and `external_metadata.last_served_model` alike.

---

## 1. Input

**Read, and not re-collected:**

- **The TZ:** `CryptoTZ/TZ-41-l0-our-quote.md`, as `main` carries it since `0ec452e`.
- **The instrument:** Appendix A, extracted by §0.1's script into `stage/` and again into the worktree, `research/tz41-l0-our-quote.py`. Both extractions read 3054 lines, 152763 bytes, `e4867068a5d1620d5deab981f68c1ae60b97d364ab00f31895a8e402d479ce16`.
- **The map:** `SYSTEM-MAP.md`, read by `fingerprint` in full and by the Executor in the sections TZ-41's header names (§6).
- **The reward book archive's ledger:** `/var/lib/btc-rewardbook-archive/ledger.jsonl`, 43871 bytes, SHA-256 `80744c1cb1359bf7f0ef20cc70f8af00b95dcd0acecdbc781428efc35e07e802`, 115 complete records. It read the same at both of `I archive`'s reads. Its 18 complete runs' `set.json` were each asserted by its set record's SHA-256.
- **The rehearsal's four Release assets** of `rewardbook-streams-1793263627`, downloaded anonymously at 12:45:34 to 12:45:37 UTC, each by its bytes and SHA-256, then replayed and removed:

  | asset | bytes | SHA-256 |
  |---|---|---|
  | `1793232000-1793232000.0.stream.jsonl.gz` | 11579610 | `bafa2d5e0ed6293ab1a4a8466431db62100413766eac72c5c6a13d18a591271f` |
  | `1793232000-1793232900.0.stream.jsonl.gz` | 10715152 | `46076896c752257334186cf66c256d6c76685dccd274dbd7f6ab9d1b5917e370` |
  | `1793232000-1793233800.0.stream.jsonl.gz` | 11443056 | `2881148ced021d3c865fdc976183de94869fbe4876f9e70d3b6747394834a4a9` |
  | `1793232000-1793234700.0.stream.jsonl.gz` | 13592154 | `ca030bcb13717dd12c41d485f8abf83c1f8c4ac92fbef2625cbd6a6aecca9496` |

- **The reward book's store,** `/var/lib/btc-rewardbook/<D0>/`, by `I fetch` alone, from 12:46:07 to 12:46:26 UTC, for `D0` `1793404800` to `1794009600` (2026-10-31 to 2026-11-07). It read each day's listing, its first `ok` selection and its replies, its 96 `slot.json`, and, for the 7 members, their 96 reward files. **No stream file under the store was opened.** No other day was opened or listed.

**Not read:** no member day's stream asset was downloaded (`replay` did not run), and no member's gamma document was requested (the walk stopped before `documents`). No request went to `gamma-api.polymarket.com`.

---

## 2. The blocker and its evidence — no measurements

**The blocker.** TZ-41 §1 (the set) admits a candidate as a member only where each of its 96 slots qualifies, among other rules with "no gap above 15 s within a file or between two". The candidates are "the UTC days from 2026-10-31 … in order", and "the members are the first 8". §1 (When) fixes the run's start "from 2026-11-08 07:30:00 UTC". It says `fetch` "stops BLOCKED … at once where a non-member pushes the walk to a day not yet ended", and "Begun on 2026-11-08, the run absorbs no non-member". This run began on 2026-11-08 at 10:39:53 UTC. The candidate of 2026-11-06 is not a member, so the eighth member would be 2026-11-08, which ends at 2026-11-09 00:00 UTC. `fetch` asserted that, as Appendix A line 1803 is written. §3.6 lets `I fetch` run again only after a network failure, so this BLOCK is final.

**Evidence — `logs/60-fetch.log`.** Below are its candidate lines and its last lines, verbatim. Its 14 `wrote …` lines are left out of this quote, for the reason in §6 item 9. The log itself is kept by name in the forensic store.

```
[2026-11-08T12:46:07Z] read ledger: {"at": "2026-11-08T12:46:07Z", "at_ns": 1794141967730411770, "file_sha256": "e4867068a5d1620d5deab981f68c1ae60b97d364ab00f31895a8e402d479ce16", "head": "cca11090695ae824c94a6f097959d93355ce3986", "mode": "fetch"}
[2026-11-08T12:46:07Z] MemAvailable 227803136 bytes, floor 143592894; free 9978109952 bytes, floor 7800000000
[2026-11-08T12:46:10Z] candidate 1793404800 (2026-10-31T00:00:00Z): MEMBER 1 of 8 - 150 markets, 96 slots, 96 stream files, 750313689 bytes; polls 43200 served of 43200, 255 without a row
[2026-11-08T12:46:13Z] candidate 1793491200 (2026-11-01T00:00:00Z): MEMBER 2 of 8 - 150 markets, 96 slots, 96 stream files, 875810624 bytes; polls 43200 served of 43200, 71 without a row
[2026-11-08T12:46:16Z] candidate 1793577600 (2026-11-02T00:00:00Z): MEMBER 3 of 8 - 150 markets, 96 slots, 96 stream files, 962538163 bytes; polls 43199 served of 43200, 562 without a row
[2026-11-08T12:46:18Z] candidate 1793664000 (2026-11-03T00:00:00Z): MEMBER 4 of 8 - 150 markets, 96 slots, 96 stream files, 706996816 bytes; polls 43200 served of 43200, 1382 without a row
[2026-11-08T12:46:21Z] candidate 1793750400 (2026-11-04T00:00:00Z): MEMBER 5 of 8 - 150 markets, 96 slots, 96 stream files, 748765594 bytes; polls 43200 served of 43200, 2690 without a row
[2026-11-08T12:46:24Z] candidate 1793836800 (2026-11-05T00:00:00Z): MEMBER 6 of 8 - 150 markets, 96 slots, 96 stream files, 1236249189 bytes; polls 43199 served of 43200, 169 without a row
[2026-11-08T12:46:24Z] candidate 1793923200 (2026-11-06T00:00:00Z): not a member - slot 1793949300 (2026-11-06T07:15:00Z): stream: a gap above 15 s
[2026-11-08T12:46:26Z] candidate 1794009600 (2026-11-07T00:00:00Z): MEMBER 7 of 8 - 150 markets, 96 slots, 96 stream files, 1636900793 bytes; polls 43198 served of 43200, 1334 without a row
Traceback (most recent call last):
  File "/root/tz41-work/wt/research/tz41-l0-our-quote.py", line 3054, in <module>
    main(sys.argv[1:])
  File "/root/tz41-work/wt/research/tz41-l0-our-quote.py", line 2542, in main
    table[mode]()
  File "/root/tz41-work/wt/research/tz41-l0-our-quote.py", line 1803, in mode_fetch
    assert time.time() >= d0 + DAY, "BLOCKED: day %d (%s) has not ended; the set needs it" % (d0, utc(d0))
           ^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: BLOCKED: day 1794096000 (2026-11-08T00:00:00Z) has not ended; the set needs it
exit=1
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
| `1793923200` | 2026-11-06 | **not a member** — slot `1793949300` (07:15 UTC): "stream: a gap above 15 s" (`slot_problem`, Appendix A lines 631 to 633: the slot record's `max_gap_ns` above `15 × 10⁹`) |
| `1794009600` | 2026-11-07 | member 7 |
| `1794096000` | 2026-11-08 | not considered: the day had not ended at 12:46:26 UTC — **BLOCKED** |

**The archive is not the cause.** Its assets reached slot `1794099600` (2026-11-08 01:00 UTC) at both of `I archive`'s reads, 10:44:08 and 12:48:00 UTC. That is 773 slots at or after `1793404800`: every slot of the 8 candidate days and 5 of 2026-11-08's. 18 complete runs, none halted, every run's tag on `origin`.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-41-l0-our-quote`, on `origin` |
| commit | `cca11090695ae824c94a6f097959d93355ce3986`, parent `2eeb26c` (`origin/main` at the worktree's creation), one file |
| on `origin` | `2026-11-08T10:41:57.957360176Z`: `ls-remote` printed `cca11090695ae824c94a6f097959d93355ce3986 refs/heads/tz-41-l0-our-quote`, equal to the worktree's `HEAD` |
| push | `git -C /root/tz41-work/wt push -u origin tz-41-l0-our-quote` through the URL's own credential (`gh`'s route not needed), `exit=0` |
| pull request | #42, <https://github.com/seahomebatumi-ai/btc-5m-twap/pull/42>, against `main`, open, head `cca1109`. Not merged by the Executor |
| Release | none: TZ-41 creates no Release (§2 item 11) |
| report | this file, the one path pushed to `main` |

**Contract §4.2's separation self-check** ran after the push and the pull request, and before this report's commit (V14):

```
$ git rev-list origin/main | grep -c cca11090695ae824c94a6f097959d93355ce3986
0
$ git diff --name-only origin/main origin/tz-41-l0-our-quote
research/tz41-l0-our-quote.py
$ git ls-tree -r --name-only origin/main | grep -E '\.parquet|\.zip'
(exit=1)
```

`git diff --numstat origin/main origin/tz-41-l0-our-quote`: `3054 0 research/tz41-l0-our-quote.py`. `--name-status`: `A research/tz41-l0-our-quote.py` (V3).

---

## 4. Gate — L0

> **EARN** where `pess`'s money reaches `θ = 10` USDC on every one of the 8 days; **NO EARN** where `opt`'s stays below `θ` on every one; **UNDECIDABLE** otherwise, and where both hold. (TZ-41 §1, §4.5)

**Not read.** No set exists, so no day's money exists, and no deciding number can be printed. Nothing was tuned, and no gate was reinterpreted.

---

## 5. Validation — the checks that ran, in TZ-41 §7's numbering

Every figure below is quoted from the log named, and every check here is an assert of the instrument or an explicit exit.

**§0.0, the instant** (`logs/00-instant.log`): `now 1794134408 2026-11-08T10:40:08Z, second of the day 38408`, `inside=0`. The session's own read before `mkdir`: `now 1794134393 2026-11-08T10:39:53Z, second of the day 38393`, `inside=0`. `mkdir /root/tz41-work /root/tz41-work/logs` printed `exit=0`.

**V1 — fingerprint, at §0.2 and §3.1:** `FINGERPRINT PASS`, twice (§0). Peaks `33243136` and `33390592` bytes.

**V2 — the host gate, at §0.3** (`logs/03-host-gate.log`, 10:40:47 UTC) **and §3.11** (`logs/96-host-gate-again.log`, 12:47:35 UTC). 11 of 11 at each:

| check | §0.3 | §3.11 |
|---|---|---|
| H1 — one `manifest.json` | `/var/lib/btc-recorder/btc-updown-5m/1789488300/manifest.json` | the same |
| H2 — source and size | `/dev/vda2` `31612203008` | the same |
| H2 — `grep -c e3975b5…` | `3` | `3` |
| H3 — interpreter | `3.12.3` | `3.12.3` |
| H4 — three files | `43871` ledger, `32516` set.json, `110512` pair book ledger | the same |
| H5 — recorder | active, enabled, pid `2388318`, `NRestarts` `0` | the same |
| H5 — pair book | active, enabled, pid `602266`, `NRestarts` `27` | the same |
| H5 — reward book | active, enabled, pid `3137952`, `NRestarts` `1` | the same |
| H5 — advisor | active, enabled, pid `284419`, `NRestarts` `5` | the same |
| memory gate | read 1 at 10:40:56: `457277440` ≥ `143592894` | read 1 at 12:47:44: `451350528` |
| disk gate | avail `10302300160` ≥ `7800000000` | avail `9939939328` |

The rest of the log is printed and gates nothing:

- **Boots:** one since 2026-08-02 07:24:34 UTC.
- **Memory:** `nproc` `1`; `MemTotal` `978640 kB`; `MemAvailable` `255696 kB` at the first read and `258492 kB` at the second.
- **The consumer:** `telemetry-watch.service` `disabled` (exit 1) and `inactive` (exit 3) at both reads.
- **Paths:** `/root/tz40-work` absent; the six code trees present.
- **Forensic store:** `2390` files at both reads (map §3's `2,370`, then TZ-42's §9 `2,370 → 2,390`).
- **Worktrees:** the primary checkout and `/root/btc-recorder-svc` at §0.3; at §3.11 also this TZ's `/root/tz41-work/wt`.
- **`du -sb`:** reward book `795330216` then `989757415`; pair book `498621770` then `603426012`; reward book archive `3258819` at both.
- **Timers:** the reward book archive next at 2026-11-09 01:30:20 UTC (last 2026-11-08 01:30:20); the pair book archive next at 03:00:20 (last 2026-11-08 03:00:20); `apt-daily-upgrade` last 2026-11-08 06:46:48, next 2026-11-09 06:57:01; `apt-daily` next 2026-11-08 12:28:44.

**systemd's records since 2026-11-01**, the last 80 lines that `grep` matched. Both archives ran on their calendars on 2026-11-07 and 2026-11-08, and the pair book's archive restarted the pair book inside its band each time (`NRestarts` 26 at 03:04:10 on 11-07, 27 at 03:06:38 on 11-08). On 2026-11-06 a unit of another project, `crypto-deploy.service`, reloaded systemd ten times from 18:33:04 to 18:33:08 UTC. 600 s later, at 18:43:09, the pair book's archive ran off its calendar and restarted the pair book (`NRestarts` 25, 18:50:26). 1,800 s later, at 19:03:09, the reward book's archive ran off its calendar as run `1793991789`, 71 files (map §7 items 115 and 129). The same window also holds the reward book archive's start of 12:53:09 UTC on 2026-11-06, finished 13:01:25. That is run `1793928620`'s completion: the calendar run of that morning had deferred in its verify.

**The package history:** `unattended-upgrade` at 2026-11-04 06:33:35 to 06:33:45, 2026-11-05 06:33:58 to 06:34:12 and 2026-11-06 06:16:05 to 06:16:07 UTC. The reward book archive's off-calendar runs `1793775818` (2026-11-04 07:03:38) and `1793862240` (2026-11-05 07:04:00) began about 1,800 s after the first two. The journal lines of those two mornings fall before the 80-line tail.

**§0.5 — refs and the number.**

- `I0 number` (`logs/05-number.log`): `origin/main 2eeb26c21ff3d0a35273a2ad300d03a1be2f8490: 103 paths under CryptoTZ/ and CryptoReports/; of the number TZ-41-: ['CryptoTZ/TZ-41-l0-our-quote.md'] and []`, then **`NUMBER PASS - 2 of 2`**.
- §3.1's `I0 number` after `git fetch` (`logs/10-number.log`, 10:41:29): the same line and `NUMBER PASS - 2 of 2`.
- `git ls-remote origin` (`logs/05-refs.log`, 10:41:11): **129 ref lines**, against the Architect's 113 of 2026-11-04 — recorded, not blocking:

  | refs | count |
  |---|---|
  | `HEAD` and `refs/heads/main` | at `2eeb26c` |
  | `tz-*` branches | 18 (the Architect's 17, plus `tz-42-advisor-registry` at `4e6db2d`) |
  | pull heads | 40, plus `refs/pull/41/merge` |
  | `pairbook-streams-*` tags | 46 |
  | `rewardbook-streams-*` tags | 18 |
  | annotated tags | 2, with their 2 peeled lines |

  `main` carries revision `2026-11-01-b`. `refs/heads/tz-41-l0-our-quote` did not exist before the push.
- **`main`'s first-parent commits above `494f10f`:**

  | commit | date (UTC) | what | path |
  |---|---|---|---|
  | `0ec452e` | 2026-11-04 18:22:45 | upload | `A CryptoTZ/TZ-41-l0-our-quote.md` |
  | `4ac4169` | 2026-11-05 16:47:15 | upload | `A CryptoTZ/TZ-42-advisor-registry.md` |
  | `2eeb26c` | 2026-11-05 20:50:15 | TZ-42 report | `A CryptoReports/TZ-42-advisor-registry-report.md` |

  §3.1's `ls-remote` before the push is in `logs/13-push.log`.

**V3 — the file:** 1 of 1 hash asserted at §0.1 and at §3.1, 3054 lines, 152763 bytes (`logs/01-stage.log`, `logs/11-worktree.log`). The branch's diff names exactly one path, `A`, 3054 lines (§3).

**V4 — the self-test** (`logs/20-selftest.log`, 10:42:20): **`SELFTEST PASS: 42 checks`**, peak `34177024` bytes. `/root/tz41-work/selftest-tmp` was absent afterwards (`test -e` exit 1).

**V5 — the archive's record, at §3.4** (`logs/40-archive.log`, 10:44:08) **and §3.11** (`logs/97-archive-again.log`, 12:48:00). Identical at both reads:

- the ledger at 43871 bytes, `80744c1c…`, 115 complete records and 0 bytes of a line still written;
- 18 complete runs and 18 sets; the assets reach slot `1794099600`, 773 slots at or after `1793404800`;
- 18 tags on `origin`, none missing; halted `False`; no run without a terminal record;
- "the rehearsal's four assets are in set rewardbook-streams-1793263627, bytes and SHA-256 equal".

The runs, as `I archive` printed them:

| run | started (UTC) | calendar | files | bytes | note |
|---|---|---|---|---|---|
| `1793263627` | 10-29 08:47:07 | off | 86 | 890975956 | deferred in verify, then complete |
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
| `1793775818` | 11-04 07:03:38 | off | 23 | 154883747 | after the package manager's run |
| `1793842220` | 11-05 01:30:20 | on | 73 | 604227513 | |
| `1793862240` | 11-05 07:04:00 | off | 23 | 307460576 | after the package manager's run |
| `1793928620` | 11-06 01:30:20 | on | 73 | 959342877 | deferred in verify, then complete at 13:01:25 |
| `1793991789` | 11-06 19:03:09 | off | 71 | 1086535575 | after `crypto-deploy.service`'s reloads |
| `1794015020` | 11-07 01:30:20 | on | 25 | 416674608 | |
| `1794101420` | 11-08 01:30:20 | on | 96 | 1639742990 | |

**V6 — G-REHEARSAL** (`logs/50-rehearse.log`, three runs under their `date -u` lines):

| try | started (UTC) | outcome |
|---|---|---|
| 1 | 10:44:20 | `AssertionError: BLOCKED: rewardbook-streams-1793263627/1793232000-1793232000.0.stream.jsonl.gz: 6 attempts, the last HTTP 503`, `exit=1`, about 11:00:20; nothing downloaded |
| 2 | 11:11:02, 640 s after try 1 ended | the same assertion, `exit=1`, by 11:28:14; nothing downloaded |
| 3 | 12:45:33, after GitHub resolved its incident at 12:32:35 (§6) | the four assets in 0.9, 0.9, 0.9 and 1.3 s, retries 0, held 0 s; then the lines below |

Try 3's last lines:

```
[2026-11-08T12:45:44Z] rehearsal: 150 markets, 387633 lines of stream, 5.8 s of processor, held 0 s; 451 lines sha256 1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd
[2026-11-08T12:45:44Z] G-REHEARSAL PASS: 451 lines sha256 1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd against the Architect's 451 lines sha256 1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd
```

`rehearsal.txt`: 103261 bytes, `1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd`. Processor `5.8` s, against §6's bound `6` and the `120` that blocks. Peak `50839552` bytes.

**V7 — G-SET: BLOCKED** (§2). 8 candidates considered with their verdicts, and 7 members, each with its markets, slots, files, bytes and polls as quoted in §2. No document request was made and no member was resolved.

**V8, V9, V10: not run.** `replay`, `rescore` and `score` need G-SET's PASS. The read ledger has 4 lines (V10's own part):

```
{"at": "2026-11-08T10:44:20Z", "at_ns": 1794134660755166343, "file_sha256": "e4867068a5d1620d5deab981f68c1ae60b97d364ab00f31895a8e402d479ce16", "head": "cca11090695ae824c94a6f097959d93355ce3986", "mode": "rehearse"}
{"at": "2026-11-08T11:11:02Z", "at_ns": 1794136262463448592, "file_sha256": "e4867068a5d1620d5deab981f68c1ae60b97d364ab00f31895a8e402d479ce16", "head": "cca11090695ae824c94a6f097959d93355ce3986", "mode": "rehearse"}
{"at": "2026-11-08T12:45:33Z", "at_ns": 1794141933848862324, "file_sha256": "e4867068a5d1620d5deab981f68c1ae60b97d364ab00f31895a8e402d479ce16", "head": "cca11090695ae824c94a6f097959d93355ce3986", "mode": "rehearse"}
{"at": "2026-11-08T12:46:07Z", "at_ns": 1794141967730411770, "file_sha256": "e4867068a5d1620d5deab981f68c1ae60b97d364ab00f31895a8e402d479ce16", "head": "cca11090695ae824c94a6f097959d93355ce3986", "mode": "fetch"}
```

The instrument's commit was on `origin` at 10:41:57.957 UTC, before every line, and before the first `fetch` line by 4,449 s.

**V11 — G-STILL:** `I still` recorded the units at 10:42:27 (`logs/30-still.log`) and compared them at 12:47:21 (`logs/95-still.log`):

```
[2026-11-08T12:47:21Z] adv3-bot.service {'MainPID': '284419', 'NRestarts': '5', 'ActiveState': 'active'}, MemoryCurrent 5468160, MemoryPeak 51396608
[2026-11-08T12:47:21Z] btc-pairbook.service {'MainPID': '602266', 'NRestarts': '27', 'ActiveState': 'active'}, MemoryCurrent 14012416, MemoryPeak 41590784
[2026-11-08T12:47:21Z] btc-recorder.service {'MainPID': '2388318', 'NRestarts': '0', 'ActiveState': 'active'}, MemoryCurrent 38350848, MemoryPeak 362307584
[2026-11-08T12:47:21Z] btc-rewardbook.service {'MainPID': '3137952', 'NRestarts': '1', 'ActiveState': 'active'}, MemoryCurrent 17928192, MemoryPeak 78729216
[2026-11-08T12:47:21Z] the reward book archive's runs with records since the first read: []
[2026-11-08T12:47:21Z] G-STILL PASS: unchanged since 2026-11-08T10:42:27Z
```

At 10:42:27 the same `MainPID`, `NRestarts` and `ActiveState`. `MemoryCurrent` read `6828032`, `18202624`, `16334848` and `15110144`, with the same peaks. Both archives' timers were `active`/`waiting` and their services `inactive`/`dead` at both reads.

**V12 — the hook:** `opens refused: 0` at every mode that reached its end:

- `fingerprint` ×2, `number` ×2, `selftest`, `still` ×2, `scratch`, `archive` ×2, `rehearse` (try 3), and the Boss's `reclaim`.
- `reward book opens: 0` at each of those.

The two failed `rehearse` tries and `fetch` ended on an assert, before `main` prints those two counts. So `fetch`'s count of the store's opens was not printed (§6).

**V13 — memory and disk.** `malloc tuned: True` at every mode that reached its end.

| mode | peak (bytes) |
|---|---|
| `fingerprint` | `33243136`, `33390592` |
| `number` | `31170560`, `32194560` |
| `selftest` | `34177024` |
| `still` | `31404032`, `31948800` |
| `scratch` | `31424512` |
| `archive` | `32604160`, `32980992` |
| `rehearse` (try 3) | `50839552` |
| `reclaim` (the Boss's) | `33722368` |

Every peak is under the modelled `71796447`. The failed tries and `fetch` printed none.

The floors' reads, at each mode that reads the store, a Release or the set — every one passed on its first read:

| mode | `MemAvailable` (floor `143592894`) | free (floor `7800000000`) |
|---|---|---|
| rehearse 1, 10:44:20 | `252858368` | `10272899072` |
| rehearse 2, 11:11:02 | `236806144` | `10207150080` |
| rehearse 3, 12:45:33 | `211079168` | `9979240448` |
| fetch, 12:46:07 | `227803136` | `9978109952` |

`free -b` at §3.11: `1002127360` total, available `361156608`; swap `3250581504`, `858517504` used.

**V14 — the separation self-check:** §3.

**V15 — §3.11's closing reads** (`logs/98-closing.log`):

- `systemctl show` of the six units, read as at G-STILL, and both archive services `inactive`. `MemoryPeak`: recorder `362307584`, pair book `41590784`, reward book `78729216`, advisor `51396608`.
- The capture units' journal of the last 24 h: the pair book's archive restart of 03:06:33 to 03:06:38 UTC alone.
- `du -sb /root/tz41-work`: `49621240`.
- `state.json` and the read ledger, printed (above).
- `wc -l` of the three timing files: "No such file or directory" for each. `replay` and `rescore` did not run, and `rehearse` writes no timing file (§6).

**V16 and V17 — reclaim and removals: below.**

**V18 — the classifier:**

| block | refused at | reason | handed over | the Boss ran it | verified by |
|---|---|---|---|---|---|
| B-RECLAIM-SCRATCH's `reclaim` | about 10:43 UTC, before it ran | "[Irreversible Local Destruction]" | §3.3's paste, unchanged in form, every earlier directory's path written in | 11:18:19.224911490 UTC | `logs/32-reclaim-scratch.log` and nine `test -e` reads of the Executor's own |

`logs/32a-reclaim-scratch-refused.log` records the refusal: nothing ran, the log was absent, the store held 2390 files, and 13 directories were under the scratch parent.

### §3.3 — `I scratch` and B-RECLAIM-SCRATCH (V16, V17)

`I scratch /tmp/claude-0/-root-btc-5m-twap/671824f6-69c4-539d-95a5-49d150ddfb52` (`logs/31-scratch.log`, 10:42:27):

```
running 630626 started 2026-11-08T07:15:37Z claude
running 630636 started 2026-11-08T07:15:39Z claude
running 630645 started 2026-11-08T07:15:40Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 630666 started 2026-11-08T07:15:42Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
running 631231 started 2026-11-08T07:20:32Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
04a2fee5-32e8-58fa-ac2a-39fcd1a0c22a born 2026-11-05T16:48:27Z: earlier
1463af1a-6ae6-40f1-8ebd-9da441c91d00 born 2026-11-08T07:14:24Z: earlier
1757478d-7992-4de0-9586-07061c8d9d71 born 2026-11-01T19:08:00Z: earlier
238335b9-cf23-414a-8e8f-ad4705c4d19e born 2026-10-30T13:16:00Z: earlier
2b99e374-8562-4f80-a179-14946219b7c1 born 2026-11-06T20:06:12Z: earlier
3fffc996-af98-504e-be5f-36b76aad2f63 born 2026-11-01T19:08:01Z: earlier
4b8e83bc-9b2f-462a-980d-02f5bb70ea9f born 2026-11-05T16:48:25Z: earlier
778f691a-9a26-58fa-b5ce-6a69e8c490f2 born 2026-11-06T20:06:13Z: earlier
b8a9aeef-53ea-5f04-8271-b0ad687b05ac born 2026-11-08T07:14:25Z: earlier
c78295f5-9a1d-4177-ac5a-b93cd56a49da born 2026-11-08T07:15:42Z: live, process [630626, 630636, 630645, 630666]
c82149c8-0336-4f7c-89f2-cbb58ba0ea88 born 2026-11-08T07:20:32Z: live, process [631231]
ef9a2cdd-af05-47da-a09b-73d08d196779 born 2026-11-08T07:09:12Z: earlier
```

B-RECLAIM-SCRATCH named the nine earlier directories other than `238335b9…` (§6 item 4). Its log, `logs/32-reclaim-scratch.log`, written by the Boss's run, every line unfiltered. The first line carries his terminal's OSC 133 marker, `ESC ] 133 ; C BEL`, written by his shell:

```
]133;C2026-11-08T11:18:19.224911490Z
[2026-11-08T11:18:19Z] reclaim: 3701 report tokens; forensic store holds 2390 files
[2026-11-08T11:18:19Z] RECLAIM PASS: 1 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 2390 -> 2390 files
[2026-11-08T11:18:19Z] malloc tuned: True
[2026-11-08T11:18:19Z] peak memory of this run: 33722368 bytes
[2026-11-08T11:18:19Z] opens refused: 0; reward book opens: 0
exit=0
2026-11-08T11:18:19.488228758Z
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
exit=0
exit=1
```

The nine `rm -rf` printed `exit=0` and each `test -e` `exit=1`. **The Executor's own reads at 11:18:54 UTC:** `test -e` of each of the nine printed `exit=1`. The parent then held `238335b9…`, this session's `671824f6…` and the two live directories `c78295f5…` and `c82149c8…`. The forensic store held `2390` files.

### §9 — B-RECLAIM-OWN (V16, V17)

The Executor ran B-RECLAIM-OWN after this report's draft, from 12:54:00 UTC; none of its lines was refused. Its output was written to no file and is quoted here verbatim from the session, every line:

```
$ cd /root/tz41-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz41-work/wt/research/tz41-l0-our-quote.py reclaim /root/tz41-work
[2026-11-08T12:54:00Z] reclaim: 3735 report tokens; forensic store holds 2390 files
[2026-11-08T12:54:01Z] reclaim: /root/tz41-work/wt skipped: no file but its HEAD's, and HEAD cca11090695ae824c94a6f097959d93355ce3986 is its upstream's
[2026-11-08T12:54:01Z] R copied 71b934830f83940f6f9546256cfa88818575c182a2030a9e6abdecff29390114 /root/btc-forensics/tz41-work--read-ledger.jsonl
[2026-11-08T12:54:01Z] R copied 1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd /root/btc-forensics/tz41-work--rehearsal.txt
[2026-11-08T12:54:01Z] R copied f7f6f65bbf9fa693c2c0ab54ccedba16197017d8b0e373705dc5f9a83c4a4360 /root/btc-forensics/tz41-work--state.json
[2026-11-08T12:54:01Z] R copied b35f2f6432fcf87c3a7ab938a0b89e259e2da1d5bc202d5bf45058951da40ffd /root/btc-forensics/tz41-work--logs--00-instant.log
[2026-11-08T12:54:01Z] R copied e6d21682d309d4de6d1df608b0c200bcfbaaeabf59d1c56e88519c9c0f4fbc18 /root/btc-forensics/tz41-work--logs--01-stage.log
[2026-11-08T12:54:01Z] R copied b57d7d2d2ca7dac2af2ea28b20c440f8532688c6d74f9ace3a92f2019cdc60ba /root/btc-forensics/tz41-work--logs--02-fingerprint.log
[2026-11-08T12:54:01Z] R copied 5716ee66ca1fc664ae1a7653af4c3ad172add37e4b35205a3cf83b31a0779e48 /root/btc-forensics/tz41-work--logs--03-host-gate.log
[2026-11-08T12:54:01Z] R copied 6bfa9aa714dc6ae76c26cb7bb6aaf62d21fecf996d0c1a980e7420345b76cd3a /root/btc-forensics/tz41-work--logs--05-number.log
[2026-11-08T12:54:01Z] R copied e583e29543e9ad8f99c86b045404307270f1c8f27c06dece1a4b2fd9d158a36c /root/btc-forensics/tz41-work--logs--05-refs.log
[2026-11-08T12:54:01Z] R copied 677ccd387bba1bca4a81e9244363d3466eba04d37052da447a4ec040e942ea8e /root/btc-forensics/tz41-work--logs--10-number.log
[2026-11-08T12:54:01Z] R copied 9438cf7d1331b8eb31b98d6f3a84006bbd2a16a1a6e08112277df63997f0ca57 /root/btc-forensics/tz41-work--logs--11-worktree.log
[2026-11-08T12:54:01Z] R copied 4b43f1eca83345d3fc9ea0801e6f27839c8e915430e72bcbcc9e1d895e188d6b /root/btc-forensics/tz41-work--logs--12-fingerprint.log
[2026-11-08T12:54:01Z] R copied b7ee6bad2360cd4341a62955f9397977e312b1d10086a702ea2bca15d1a01bb1 /root/btc-forensics/tz41-work--logs--13-push.log
[2026-11-08T12:54:01Z] R copied bc246a1da35c33b5a12efff3504d2aa8dd72369b9f13c1ee7537cef11add40c7 /root/btc-forensics/tz41-work--logs--14-pr.log
[2026-11-08T12:54:01Z] R copied 21b9016aa42364859071e18bf0769af5cbb61bf75922517db6c3c47291cf19c0 /root/btc-forensics/tz41-work--logs--20-selftest.log
[2026-11-08T12:54:01Z] R copied b0c4c1e81457c8f19c903721f9646b9f40be46621334ab092ac0defbc01d7330 /root/btc-forensics/tz41-work--logs--30-still.log
[2026-11-08T12:54:01Z] R copied 136fa753b39a9ee46c46ddc12bdd83c7793233d1c6afc404a31f1eeb5d58fb76 /root/btc-forensics/tz41-work--logs--31-scratch.log
[2026-11-08T12:54:01Z] R copied 9d08f70572daff3d86dd510c44ff2abd717ee9a3ebddce24450aeb593ca7a572 /root/btc-forensics/tz41-work--logs--32-reclaim-scratch.log
[2026-11-08T12:54:01Z] R copied 188093da3b762da5d5a92a8c1e72587caedb10fa8a106ac6098f4f5b7c2ce442 /root/btc-forensics/tz41-work--logs--32a-reclaim-scratch-refused.log
[2026-11-08T12:54:01Z] R copied e4237ec86786285b00789ee98ee33d2521cd3bd9354d5213417240561e679617 /root/btc-forensics/tz41-work--logs--40-archive.log
[2026-11-08T12:54:01Z] R copied 87059153912aa02d310b8319dc6951964117c9639f6b82bd803ca3bc62900e99 /root/btc-forensics/tz41-work--logs--50-rehearse.log
[2026-11-08T12:54:01Z] R copied add3f3f9a2aa17408565f4df59524752997ce4fb47388d07e69a02252e299924 /root/btc-forensics/tz41-work--logs--60-fetch.log
[2026-11-08T12:54:01Z] R copied 5b4130680900984514951e43053f8a52f6b3bfdec32763eb980dc333c64e1aa3 /root/btc-forensics/tz41-work--logs--95-still.log
[2026-11-08T12:54:01Z] R copied c8bdfe510dafd0ae79e685a3e456674991acccaac593ac259b519df82b85ba62 /root/btc-forensics/tz41-work--logs--96-host-gate-again.log
[2026-11-08T12:54:01Z] R copied a132dc7c3803c147addb3146676b708f72793d3a41911ff95f8e697de89dbecf /root/btc-forensics/tz41-work--logs--97-archive-again.log
[2026-11-08T12:54:01Z] R copied cb21cda3d6b1754668d1b6629f6d68ead3cf05557d8445e039a39a1b501dfdb7 /root/btc-forensics/tz41-work--logs--98-closing.log
[2026-11-08T12:54:01Z] R copied e4867068a5d1620d5deab981f68c1ae60b97d364ab00f31895a8e402d479ce16 /root/btc-forensics/tz41-work--stage--research--tz41-l0-our-quote.py
[2026-11-08T12:54:01Z] RECLAIM PASS: 41 files considered, 27 named by a report, 0 kept by name, 27 copied, 0 already held; forensic store 2390 -> 2417 files
[2026-11-08T12:54:01Z] malloc tuned: True
[2026-11-08T12:54:01Z] peak memory of this run: 34332672 bytes
[2026-11-08T12:54:01Z] opens refused: 0; reward book opens: 0
$ cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz41-work/wt; echo "exit=$?"
exit=0
$ rm -rf /root/tz41-work; echo "exit=$?"
exit=0
$ test -e /root/tz41-work; echo "exit=$?"
exit=1
$ git -C /root/btc-5m-twap worktree prune; git -C /root/btc-5m-twap worktree list
/root/btc-5m-twap       2eeb26c [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
$ find /root/btc-forensics -type f | wc -l
2417
$ df -B1 --output=source,size,avail /var/lib/btc-recorder
Filesystem       1B-blocks      Avail
/dev/vda2      31612203008 9975246848
```

**What this shows:**

- **The 41 files:** the 27 below, all named by this report's draft, and the 14 `fetch/` files, which it does not name (§6 item 9). Every log, `state.json` and `read-ledger.jsonl` is among the 27 named, so none counted as "kept by name".
- **The worktree** held exactly its pushed `HEAD`. `git worktree remove` ran without `--force`, exit `0`.
- **The store:** 2,417 = 2,390 + 27 copies. The Executor then ran `sha256sum /root/btc-forensics/tz41-work--*`: 27 files, each hash among this report's.
- **What stays:** the branch `tz-41-l0-our-quote` stays on `origin` and as a local ref at `cca1109`. The running units' code trees, the capture roots, both archives' state and the forensic store are kept.

**Every file the run wrote in its tree**, by bytes and SHA-256:

- **Kept by name or named here:** the staged instrument, `state.json`, `read-ledger.jsonl`, `rehearsal.txt` and every log.

  | file | bytes | SHA-256 |
  |---|---|---|
  | `stage/research/tz41-l0-our-quote.py` | 152763 | `e4867068a5d1620d5deab981f68c1ae60b97d364ab00f31895a8e402d479ce16` |
  | `state.json` | 495 | `f7f6f65bbf9fa693c2c0ab54ccedba16197017d8b0e373705dc5f9a83c4a4360` |
  | `read-ledger.jsonl` | 861 | `71b934830f83940f6f9546256cfa88818575c182a2030a9e6abdecff29390114` |
  | `rehearsal.txt` | 103261 | `1ab40f4b2a9b4f263e92959dc78a67dc9583731889cce70b22edad59091944cd` |
  | `logs/00-instant.log` | 70 | `b35f2f6432fcf87c3a7ab938a0b89e259e2da1d5bc202d5bf45058951da40ffd` |
  | `logs/01-stage.log` | 136 | `e6d21682d309d4de6d1df608b0c200bcfbaaeabf59d1c56e88519c9c0f4fbc18` |
  | `logs/02-fingerprint.log` | 11498 | `b57d7d2d2ca7dac2af2ea28b20c440f8532688c6d74f9ace3a92f2019cdc60ba` |
  | `logs/03-host-gate.log` | 14072 | `5716ee66ca1fc664ae1a7653af4c3ad172add37e4b35205a3cf83b31a0779e48` |
  | `logs/05-number.log` | 405 | `6bfa9aa714dc6ae76c26cb7bb6aaf62d21fecf996d0c1a980e7420345b76cd3a` |
  | `logs/05-refs.log` | 9781 | `e583e29543e9ad8f99c86b045404307270f1c8f27c06dece1a4b2fd9d158a36c` |
  | `logs/10-number.log` | 450 | `677ccd387bba1bca4a81e9244363d3466eba04d37052da447a4ec040e942ea8e` |
  | `logs/11-worktree.log` | 850 | `9438cf7d1331b8eb31b98d6f3a84006bbd2a16a1a6e08112277df63997f0ca57` |
  | `logs/12-fingerprint.log` | 11498 | `4b43f1eca83345d3fc9ea0801e6f27839c8e915430e72bcbcc9e1d895e188d6b` |
  | `logs/13-push.log` | 10124 | `b7ee6bad2360cd4341a62955f9397977e312b1d10086a702ea2bca15d1a01bb1` |
  | `logs/14-pr.log` | 95 | `bc246a1da35c33b5a12efff3504d2aa8dd72369b9f13c1ee7537cef11add40c7` |
  | `logs/20-selftest.log` | 6988 | `21b9016aa42364859071e18bf0769af5cbb61bf75922517db6c3c47291cf19c0` |
  | `logs/30-still.log` | 1426 | `b0c4c1e81457c8f19c903721f9646b9f40be46621334ab092ac0defbc01d7330` |
  | `logs/31-scratch.log` | 1906 | `136fa753b39a9ee46c46ddc12bdd83c7793233d1c6afc404a31f1eeb5d58fb76` |
  | `logs/32-reclaim-scratch.log` | 608 | `9d08f70572daff3d86dd510c44ff2abd717ee9a3ebddce24450aeb593ca7a572` |
  | `logs/32a-reclaim-scratch-refused.log` | 358 | `188093da3b762da5d5a92a8c1e72587caedb10fa8a106ac6098f4f5b7c2ce442` |
  | `logs/40-archive.log` | 58899 | `e4237ec86786285b00789ee98ee33d2521cd3bd9354d5213417240561e679617` |
  | `logs/50-rehearse.log` | 4188 | `87059153912aa02d310b8319dc6951964117c9639f6b82bd803ca3bc62900e99` |
  | `logs/60-fetch.log` | 4568 | `add3f3f9a2aa17408565f4df59524752997ce4fb47388d07e69a02252e299924` |
  | `logs/95-still.log` | 1553 | `5b4130680900984514951e43053f8a52f6b3bfdec32763eb980dc333c64e1aa3` |
  | `logs/96-host-gate-again.log` | 14084 | `c8bdfe510dafd0ae79e685a3e456674991acccaac593ac259b519df82b85ba62` |
  | `logs/97-archive-again.log` | 58899 | `a132dc7c3803c147addb3146676b708f72793d3a41911ff95f8e697de89dbecf` |
  | `logs/98-closing.log` | 2963 | `cb21cda3d6b1754668d1b6629f6d68ead3cf05557d8445e039a39a1b501dfdb7` |

- **Not named here:** the 14 files `I fetch` wrote under `fetch/` — 7 days' `<D0>.json`, 55310 to 55639 bytes, and `<D0>.polls.jsonl`, 4967708 to 5055307 bytes. Their bytes and SHA-256 are in `logs/60-fetch.log`'s `wrote` lines (§6 item 9).
- **Never written:** `rehearsal-dl/` held no file after each try; `dl/`, `days/`, `set.json`, `reading.json`, `rescore.txt` and the three timing files were never written.

---

## 6. What could not be implemented as written

1. **G-SET BLOCKED, by the TZ's own rule** (§2). A run begun on 2026-11-08 absorbs no non-member, and 2026-11-06 is one. As a consequence, §3.7 to §3.9, V8 to V10, G-BOOK, DETERMINISM and L0 did not run. This report suggests no fix (contract §9).
2. **GitHub's incident, and the rehearsal's tries.**
   - **The incident:** GitHub's status page carried "Increase in timeouts for some unauthenticated users", created 2026-11-08 10:36:05 UTC and resolved 12:32:35 UTC.
   - **Its updates, as read:** 11:16:19 "degraded performance primarily for unauthenticated users"; 11:20:57 "API Requests is experiencing degraded performance"; 11:50:49 "identified a problematic component"; 11:56:20 "mitigated … monitoring"; 12:29:30 monitoring; 12:32:35 resolved.
   - **The two failed tries:** every download this TZ makes is anonymous, so its first two `rehearse` tries failed on the network. Each made six attempts, the last `HTTP 503`; this is §3.5's resumable case. The second try ran 640 s after the first.
   - **The third try, delayed:** §3.5 makes a third failure BLOCKED. The Executor therefore ran the third try only once GitHub read the incident resolved, at 12:45:33 UTC, about 4,640 s after the second failure rather than 600 s. Its four downloads took 0.9 to 1.3 s with no retry. TZ-41 fixes the spacing as "600 s apart" and no upper bound; the Executor read 600 s as the least.
   - **How the status was read:** five times, at about 11:19, 11:25, 11:45, 12:15 and 12:45 UTC, by the session's own web-fetch tool against `www.githubstatus.com` and its public status API. These are reads by Claude Code's tool, not requests from the host, and no host process made them; §2 item 7 binds the host's requests.
   - **Wait announcements:** the waits between those reads were set by epoch and two were misconverted, so the session announced 11:45, 12:05, 12:35 and 13:05 for reads made at 11:25, 11:45, 12:15 and 12:45.
   - **Diagnostics while try 1 held** — none prints a member's figure or a stream's content:
     - read-only `ps`, `ss`, `/proc/<pid>/wchan`, `ls -la` of `rehearsal-dl/`, `getent hosts` of the three download hosts and `env | grep -i proxy` (none set);
     - a `grep` of `research/tz32-our-quoting.py`, `tz30-nesting-b3-measure.py` and `tz27-pairbook-archive.py` for their download headers, the same form as Appendix A's;
     - one `git ls-remote origin refs/heads/tz-41-l0-our-quote`, served in 0.4 s — a `git` request against `origin`, inside §2 item 7, that no step names.
3. **§0.0 before this run.** The Boss's first `EXECUTE TZ-41` came at 07:21:59 UTC. The clock line printed `inside=1`, so nothing was made or written, and the Executor told the Boss in one Russian line that the band opens at 07:30:00 UTC. This run is the second `EXECUTE`, begun afresh at 10:39:53 UTC. The session's reads before §0.0, in both turns: `git checkout main`, `git pull`, `git fetch`, `git log`, `ls`, the TZ, the map in sections, `date -u`, and the memory files of the session.
4. **`238335b9-cf23-414a-8e8f-ad4705c4d19e` was named earlier, and was left untouched.** §3.3 calls it "live and no TZ's, and is never touched". The remote-control processes it was born with are gone: the running ones started at 2026-11-08 07:15:37 UTC, with their own directory `c78295f5…`. So `I scratch` named it earlier. TZ-41's specific "never touched" was read as governing over the general rule, as TZ-42's Executor read the same words. B-RECLAIM-SCRATCH named the other nine.
5. **The nine directories removed.** TZ-42's two are `04a2fee5…` (its scratchpad) and `4b8e83bc…`. The rest no report names: `1757478d…` and `3fffc996…`, born with the remote-control processes of 2026-11-01 19:07:55 UTC; `2b99e374…` and `778f691a…`, born 2026-11-06 20:06 UTC; and `ef9a2cdd…`, `1463af1a…` and `b8a9aeef…`, born 2026-11-08 07:09 to 07:14 UTC, before the running processes. Map §3's expected pair from TZ-40, `981b3989…` and `e19b6910…`, was already gone: TZ-42's report records its own B-RECLAIM-SCRATCH removing them.
6. **The classifier and the safety check.** The classifier refused B-RECLAIM-SCRATCH's `reclaim` (V18). The Executor then printed the paste's text with a shell loop, without running it. Claude Code's built-in safety check stopped that print before it ran, because the text held `rm -rf` on shell variables. The paste was then written out by hand with literal paths, in §3.3's form, and handed over in Russian.
7. **§0.3's last line lists the session's own directory, not its parent.** `S` is the scratchpad `/tmp/claude-0/-root-btc-5m-twap/671824f6-69c4-539d-95a5-49d150ddfb52/scratchpad`, so `ls -la "$(dirname "$S")"` lists the session's directory (`scratchpad`, `tasks`). The TZ's prose speaks of "the directory that holds the session's own". The line ran verbatim. The UUID directories beside the session's own are `I scratch`'s, which takes the same `$(dirname "$S")` as OWN and lists its parent.
8. **Logs.** Names and contents beyond §3's table:
   - `logs/32a-reclaim-scratch-refused.log`, the refusal's record — a name §3's table does not carry.
   - `logs/05-refs.log` has, appended under a `date -u` line, `git log --first-parent --name-status 494f10f..origin/main` for §0.5's commits.
   - `logs/50-rehearse.log` holds three runs: the first without, and the next two under, a `date -u` line.
   - `rehearse` writes no `timing-rehearsal.jsonl`: `mode_rehearse` names the path and writes nothing to it, Appendix A lines 2219 to 2245. §3.11's `wc -l` printed "No such file" for it, as for the replay's and rescore's files, which never existed.
9. **The `fetch/` files are not named here by hash.**
   - **What they hold:** the 14 files `I fetch` wrote under `/root/tz41-work/fetch/` carry every member's rate, minimum size, maximum spread and rebate coefficient, and every poll's rate and competitiveness (§2 item 10).
   - **What naming them would do:** a report that prints their SHA-256 would make §9's `reclaim` copy them into the forensic store.
   - **Why not:** a BLOCKED report carries no partial measurements (contract §9), and no reading uses these files. Their sources stay on the host under `/var/lib/btc-rewardbook/<D0>/`, which the reward book's archive does not move.
   - **The record:** their names, bytes and SHA-256 are in `logs/60-fetch.log`'s `wrote` lines, a file kept by name. §2 quotes that log without those lines, and the files went with the tree.
10. **What the BLOCK left unprinted.** `fetch` ended on its BLOCK assert before printing its peak, `malloc tuned` and its counts of refused opens and of the store's opens. So V12's "`reward book opens` above `0` at `fetch` alone" and V13's peak for `fetch` were not printed. The failed `rehearse` tries printed no peak either.
11. **The map was read in sections:** §0 in full, §1's start and its refs records, §2.5's end, §2.6, §3's end, §6's rows and §7 items 115 to 147. These hold every section TZ-41's header names (map §7 items 139 and 141). `fingerprint` reads every row.
12. **Appendix A was read in its constants, its hook, the clock, the archive's record, the store's readers, the replay's core, the set, the downloads, the units, the reading, the rehearsal and the session's modes.** The synthetic day and most of the self-test's body were not read; the file is verified by hash at both extractions.
13. **The commit's author is the host's git default,** `root <root@vultr.guest>`, as for TZ-40 (map §7 item 146).
14. **The refs:** 129 lines against the Architect's 113 of 2026-11-04 — TZ-42's branch, pull head and merge ref, and the archives' tags since (§5). TZ-41 records such a difference without blocking.
15. **Contract §8's section order** is kept, with §2 holding the blocker and its evidence in place of measurements, as a BLOCKED report requires. The run's other gates and reads are reported, because TZ-41 §3 sends a BLOCK after §3.1 on to §3.10, §3.11 and §9. TZ-41 §7 and §9 ask the report to show what those ran, and here the TZ governs over contract §9's "nothing else".
