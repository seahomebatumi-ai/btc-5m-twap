# TZ-44 — L0's inputs off the host: one Release of the reward book's days to 2026-11-08 and of TZ-43's work files; the venue's own reading of the host's address — REPORT

**Status: every gate PASS. L0's inputs are off the host.**

- **The Release:** id `443961874`, on the lightweight tag `tz-44-l0-inputs`, at the instrument's commit `ab0a8be170786ee9b4c9bfd18ed5a522db669932`. It is published and not the latest. It holds **47 assets, `229,053,786` bytes**: 12 day archives (`186,490,880` bytes), TZ-43's 34 work files (`42,169,992` bytes) and the manifest (`392,914` bytes).
- **G-UPLOAD PASS: 47 of 47** assets by name, bytes, state and digest. **G-DOWNLOAD PASS: 47 of 47** anonymous downloads, `229053786` bytes. **G-TAG PASS:** `tz-44-l0-inputs` at `ab0a8be170786ee9b4c9bfd18ed5a522db669932`, lightweight (`logs/70-verify.log`).
- **G-SOURCE PASS: 34 of 34** equal to TZ-43's report, `42169992` bytes, at both `pack` runs.
- **G-PACK PASS: 12 days of 12.** 2,238 members, `184,746,447` bytes of members, `186,490,880` bytes of archives. **No file of replies withheld: 0 files, 0 bytes.** Streams 0 and other names 0, none opened. Days over their budget: 0.
- **G-RESERVE PASS** at both runs. The store was opened 3,357 times — once for each of the 2,238 members kept and once for each of the 1,119 files of replies scanned — and listed 12 times, once a day. Nothing else under `/var/lib/btc-rewardbook` was opened or listed.
- **DETERMINISM PASS: 14 of 14 outputs unchanged.**
- **The geoblock, as printed** (`logs/50-geoblock.log`). It gates nothing:
  `GEOBLOCK READ: https://polymarket.com/api/geoblock, status 200, 66 bytes in 0.18 s; blocked True, country 'PL', region '14'; reply keys ['blocked', 'country', 'ip', 'region']`
  The venue reads the capture host as **blocked**. The reply's `ip` was neither printed nor written.
- **The advisor's `commit.txt`** reads `4e6db2d16dda3da14957120d636f537dfc0bcc87`, equal to the head map §3 names, at both host gates.
- **G-STILL PASS:** the four units were unchanged from 07:35:40 to 08:06:24 UTC.
- **The classifier refused no block.** B-RECLAIM-SCRATCH's `reclaim` and its four single-tree `rm -rf` ran in the session unrefused. **B-UPLOAD was the Boss's by its own text.** It was handed over at 07:37:43 UTC, the Boss ran it at 08:02:52 UTC, and it completed in one run, `exit=0`. B-RECLAIM-OWN is §9.

Run on 2026-11-13, from 07:33:33 UTC (§0.0) to the end of §9. Logs are under `/root/tz44-work/logs/` and were copied by §9 into `/root/btc-forensics/` as `tz44-work--logs--<name>`.

---

## 0. Fingerprint

**§0.0, the instant** (`logs/00-instant.log`; the session's first run of the line, 07:33:33 UTC, read `inside=0` too):

```
now 1794555218 2026-11-13T07:33:38Z, second of the day 27218
inside=0
```

`mkdir /root/tz44-work /root/tz44-work/logs` printed `exit=0`.

**§0.1, the instrument staged** (`logs/01-stage.log`). §3.1 printed the same two lines again for `/root/tz44-work/wt` (`logs/11-worktree.log`). V4: two lines per run, both runs.

```
/root/tz44-work/stage/research/tz44-l0-inputs-release.py 1616 90703 0b78807d9c5dec087138b0c9a329cb8c976157ab5c8a3fd4deee7cb31e89e190
/root/tz44-work/stage/research/tz27-pairbook-archive.py 2078 106284 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673
```

**Map revision read:** `2026-11-12-a`, equal to the TZ's header.

**Anchors read:** `A1` `229a944f2d51`, `A2` `6c5089330629`, `A3` `0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable`, `A4` `437b45ea196b`, `A5` `0f6c90451cbd`, `A6` `729f0bcdbee3`. All six equal the header's. `A2`, `A4`, `A5` and `A6` were re-derived as the first 12 hex characters of their files' SHA-256, each `equal`.

**V1:** `I0 fingerprint` (`logs/02-fingerprint.log`, 07:33:52 UTC) and `I fingerprint` from the worktree (`logs/12-fingerprint.log`, 07:34:55 UTC) each printed:

```
FINGERPRINT PASS: revision 2026-11-12-a; anchors 6 of 6, 4 re-derived; rows 62: frozen 59 of 59 equal, tracked 2, reported 1
```

The two logs are equal line for line, apart from timestamps and the peak.

The table below covers map §0's 62 rows, as the instrument read them in the primary checkout `/root/btc-5m-twap` at `783f31b` (`origin/main`):

| path | lines | bytes | state | SHA-256 |
|---|---|---|---|---|
| `SYSTEM-MAP.md` | 2082 | 588791 | reported | `58b771dfa21467d27fe0e9f18ed98502f2226203951f2f8c9a1dbb82070b275e` |
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
| `research/tz42-advisor-registry.py` | 2088 | 134077 | frozen equal | `b6c45490b2f86f5c4678c645041ef1556b1199a6bc814470de904aedf7f5105f` |
| `research/tz43-l0-our-quote.py` | 3056 | 152905 | frozen equal | `48c3550b3f9a990fa8bc43ad8464b181ec2eb0a086b3b6f3a0ceed52da4a30cf` |
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
| `advisor/adv3-bot.py` | 2548 | 157438 | frozen equal | `c3d9fff54f3585cfc4c33b5f7e1f93b390e62b03e0b4725fee2d6fdda6d04c11` |
| `advisor/selftest-adv3.py` | 256 | 19111 | frozen equal | `6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398` |
| `.gitignore` | 5 | 252 | tracked | `9e50e9f1e0e3245f71d6ccffa0e6c9259b784a4017f12ec54a88cc48580d1f0b` |

**V3: NUMBER PASS - 2 of 2, twice** — `I0 number` at 07:34:29 UTC (`logs/05-number.log`) and again after §3.1's fetch at 07:34:41 UTC (`logs/10-number.log`). Each read `origin/main 783f31b126bb25858c615670af40042d60f76186: 107 paths under CryptoTZ/ and CryptoReports/; of the number TZ-44-: ['CryptoTZ/TZ-44-l0-inputs-release.md'] and []`.

**Refs (§0.5, `logs/05-refs.log`, 07:34:29 UTC): 142 ref lines**, where the Architect read 139 on 2026-11-12. This is recorded, not BLOCKING:

- `HEAD` and `refs/heads/main` are at `783f31b126bb25858c615670af40042d60f76186`.
- Nineteen `tz-*` branches and forty-two pull heads.
- **51** `pairbook-streams-*` tags and **24** `rewardbook-streams-*` tags.
- The two annotated tags with their peeled lines.
- No `refs/heads/tz-44-l0-inputs-release` and no `refs/tags/tz-44-l0-inputs`.

The three lines beyond the Architect's 139 are three archive tags made since his read:

| tag | its `A`, as UTC | the run |
|---|---|---|
| `pairbook-streams-1794521401` | 2026-11-12 22:10:01 | off the calendar |
| `rewardbook-streams-1794522601` | 2026-11-12 22:30:01 | off the calendar |
| `rewardbook-streams-1794533420` | 2026-11-13 01:30:20 | the calendar's |

Both off-calendar runs came 600 s and 1,800 s after `crypto-deploy.service`'s eleven reloads of systemd at 21:59:57 to 22:00:01 UTC (§2.5 below). **`main`'s first-parent commits above `7f7d7b1`:** one, `783f31b126bb25858c615670af40042d60f76186` (2026-11-13T02:13:56+04:00, "Add files via upload"), adding `CryptoTZ/TZ-44-l0-inputs-release.md` and changing nothing else. §3.1's `git ls-remote origin` before the push (`logs/13-push.log`) printed the same 142 lines with no `tz-44` ref.

---

## 1. Input

**Nothing was re-collected.** No stream was opened and no venue document was fetched. The one request to the venue is §3.5's geoblock read.

| input | read by | what was read |
|---|---|---|
| `/var/lib/btc-rewardbook/<D0>/` for the twelve `D0` `1793145600` to `1794096000` (2026-10-28 to 2026-11-08) | `I pack`, twice | Each day directory was listed once. Every selection, reply file, slot record and poll file was opened once for reading — 2,238 members, `184,746,447` bytes — and every one of the 1,119 files of replies was scanned once more, a line at a time. No stream file existed in any of the twelve directories. No day from `1794182400` was opened, listed or named, and no file of the store's root was opened. The Executor's own commands touched the store only with §0.3's `stat` of the twelve directories and `du -sb`. |
| `/root/btc-forensics/tz43-work--*` — the 34 files of TZ-43's tree | `I pack` (G-SOURCE), `I upload` | `42,169,992` bytes, 34 of 34 equal to TZ-43's report's §2.6 rows |
| `CryptoReports/TZ-43-l0-our-quote-report.md` | `I pack` | `97435` bytes, sha256 `606b7ff6647ef71ce8e438f325f2259f7b114586af3ab1d468d0edc20ad626bd`; the rows of its 34 files found 34 of 34 |
| `SYSTEM-MAP.md` and the 62 files of its §0 table | `I0 fingerprint`, `I fingerprint` | §0 above |
| `research/tz27-pairbook-archive.py` | the instrument, loaded beside itself by its SHA-256 | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` |
| `/var/lib/btc-pairbook-archive/ledger.jsonl` | `I still` (and §0.3's `stat`) | the pair book's archive's restart records, for G-STILL |
| `CryptoReports/*.md` | `I reclaim` | hex tokens: 3,836 at B-RECLAIM-SCRATCH |
| `https://polymarket.com/api/geoblock` | `I geoblock`, once | §2.4 |

---

## 2. Measurements

### 2.1 The twelve days, as `I pack` printed them (`logs/40-pack.log`; equal in `logs/41-pack-again.log`, there `unchanged`)

Columns: names in the day's directory; of them `select.<a>.*`, `<S>.<k>.slot.json`, `<S>.<k>.rewards.jsonl.gz`, streams and other names (the last two never opened); members kept and their bytes; files of replies scanned; files withheld (bytes); the archive's bytes and SHA-256; the day's budget in seconds, the second of its window it began at, and its seconds.

| `D0` | day | names | select | slot | rewards | stream | other | members | member bytes | replies scanned | withheld | archive bytes | archive SHA-256 | budget s | from second | s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `1793145600` | 2026-10-28 | 104 | 2 | 51 | 51 | 0 | 0 | 104 | 9179661 | 52 | 0 (0 B) | 9256960 | `b268ef086a2d2d23afa6cb33b354eddd0d3589aca1621aa15901b6441667f9f6` | 49 | 390 | 0.71 |
| `1793232000` | 2026-10-29 | 194 | 2 | 96 | 96 | 0 | 0 | 194 | 15331354 | 97 | 0 (0 B) | 15482880 | `b214536add4d9b43cd6f634cd8c26cb92d9f82b0c6bd6508564a8b21a2529dc1` | 61 | 391 | 1.27 |
| `1793318400` | 2026-10-30 | 194 | 2 | 96 | 96 | 0 | 0 | 194 | 16232351 | 97 | 0 (0 B) | 16384000 | `e3189d4cf76f5acb2a14351610c7ea9dc1bd294e19cee310eef80b421b2b910f` | 63 | 392 | 1.30 |
| `1793404800` | 2026-10-31 | 194 | 2 | 96 | 96 | 0 | 0 | 194 | 16283583 | 97 | 0 (0 B) | 16445440 | `563a3ccf2df5e48641dff892de6f50d4421c071cd42ae7cbb147b3ed8b2f3c1f` | 63 | 394 | 1.37 |
| `1793491200` | 2026-11-01 | 194 | 2 | 96 | 96 | 0 | 0 | 194 | 16141113 | 97 | 0 (0 B) | 16291840 | `0614a35f95eb4fe7f9ad7f8689fc5f1876b811e6dc9fa6028e2a0a6e7da8b751` | 63 | 395 | 1.38 |
| `1793577600` | 2026-11-02 | 194 | 2 | 96 | 96 | 0 | 0 | 194 | 16444827 | 97 | 0 (0 B) | 16588800 | `67043eb13198b2c599b042b0385f06d925db74ff0f25e264e8555627dd987dbb` | 63 | 396 | 1.31 |
| `1793664000` | 2026-11-03 | 194 | 2 | 96 | 96 | 0 | 0 | 194 | 16408880 | 97 | 0 (0 B) | 16558080 | `92614b11fe80d5cca913c4633f2bcd0f96200ae0f0050ef2a74c68a491b67a45` | 63 | 398 | 1.46 |
| `1793750400` | 2026-11-04 | 194 | 2 | 96 | 96 | 0 | 0 | 194 | 15356050 | 97 | 0 (0 B) | 15513600 | `a8ec58f4cc250a12c63bcb743d7f0ddd03596e374990794a0c803167ad3e6442` | 61 | 399 | 1.32 |
| `1793836800` | 2026-11-05 | 194 | 2 | 96 | 96 | 0 | 0 | 194 | 15966551 | 97 | 0 (0 B) | 16117760 | `4179070b6d7add6a682f4d8f26664b2920b6113fe4119cf274b5460c437400e6` | 62 | 401 | 1.40 |
| `1793923200` | 2026-11-06 | 194 | 2 | 96 | 96 | 0 | 0 | 194 | 15577481 | 97 | 0 (0 B) | 15728640 | `ba31ef522351e3875dcd4e7ff1b7989787cc71515f82668972e037ba8612bf6f` | 62 | 402 | 1.22 |
| `1794009600` | 2026-11-07 | 194 | 2 | 96 | 96 | 0 | 0 | 194 | 15604496 | 97 | 0 (0 B) | 15759360 | `df1e1592fbdc9425ce3ba8fc7ed3eec99458081b63ddf1c04eecb6c1a7651d45` | 62 | 403 | 1.26 |
| `1794096000` | 2026-11-08 | 194 | 2 | 96 | 96 | 0 | 0 | 194 | 16220100 | 97 | 0 (0 B) | 16363520 | `0d8730b7a60cafaf47bf81ed5dcdc8bd8d68ca23ce9c86f70db06bbd02b1c2ec` | 63 | 405 | 1.44 |

**Every file withheld, by name, bytes and reason: none.** No line of any of the 1,119 files of replies carried a body other than a JSON object or array under status 200, and every file was a whole gzip file. Every day held one selection attempt, `select.<a>.json` with its `select.<a>.replies.jsonl.gz`. 2026-10-28, the store's first day, captured from 11:30:16 UTC, held 51 slots, and every other day held 96. **No excluded name exists on any day:** streams 0 and other names 0.

```
G-PACK PASS: 12 days of 12, 2238 members, 184746447 bytes of members, 186490880 bytes of archives; withheld 0 files of replies, 0 bytes; streams 0 and other names 0 never opened; 47 assets, 229053786 bytes; days over their budget 0; outputs {'wrote': 14}
```

The second run printed the same line, `outputs {'unchanged': 14}`.

### 2.2 The set — every asset by name, bytes and SHA-256

These are `pack`'s `S` lines, in upload order: the local hash of contract §5.1, beside `verify`'s record of each (`logs/70-verify.log`, its `V` and `D` lines). Each record: the API's `state` `uploaded`, its size the set's, its `digest` `sha256:` the set's, its download URL the tag's, and a full anonymous download whose bytes and SHA-256 equal the set's. **The manifest is row 47, `tz44-manifest.json`, SHA-256 `491dcaf037e15e26d25512b609afbe68655952f321d92fa8ef208ee966650c8b`.** `set.json` itself is `10780` bytes, sha256 `7bed9f17d3ffc2c1fffcf91a812d2aa71c677868389999df3a5744f37576fa37`.

| # | asset | bytes | SHA-256 (local, = the API's digest, = the download's) | asset id | `verify` |
|---|---|---|---|---|---|
| 1 | `rewardbook-inputs-1793145600.tar` | 9256960 | `b268ef086a2d2d23afa6cb33b354eddd0d3589aca1621aa15901b6441667f9f6` | 742815102 | API uploaded, digest equal; download equal |
| 2 | `rewardbook-inputs-1793232000.tar` | 15482880 | `b214536add4d9b43cd6f634cd8c26cb92d9f82b0c6bd6508564a8b21a2529dc1` | 742815172 | API uploaded, digest equal; download equal |
| 3 | `rewardbook-inputs-1793318400.tar` | 16384000 | `e3189d4cf76f5acb2a14351610c7ea9dc1bd294e19cee310eef80b421b2b910f` | 742815291 | API uploaded, digest equal; download equal |
| 4 | `rewardbook-inputs-1793404800.tar` | 16445440 | `563a3ccf2df5e48641dff892de6f50d4421c071cd42ae7cbb147b3ed8b2f3c1f` | 742815370 | API uploaded, digest equal; download equal |
| 5 | `rewardbook-inputs-1793491200.tar` | 16291840 | `0614a35f95eb4fe7f9ad7f8689fc5f1876b811e6dc9fa6028e2a0a6e7da8b751` | 742815436 | API uploaded, digest equal; download equal |
| 6 | `rewardbook-inputs-1793577600.tar` | 16588800 | `67043eb13198b2c599b042b0385f06d925db74ff0f25e264e8555627dd987dbb` | 742815512 | API uploaded, digest equal; download equal |
| 7 | `rewardbook-inputs-1793664000.tar` | 16558080 | `92614b11fe80d5cca913c4633f2bcd0f96200ae0f0050ef2a74c68a491b67a45` | 742815601 | API uploaded, digest equal; download equal |
| 8 | `rewardbook-inputs-1793750400.tar` | 15513600 | `a8ec58f4cc250a12c63bcb743d7f0ddd03596e374990794a0c803167ad3e6442` | 742815675 | API uploaded, digest equal; download equal |
| 9 | `rewardbook-inputs-1793836800.tar` | 16117760 | `4179070b6d7add6a682f4d8f26664b2920b6113fe4119cf274b5460c437400e6` | 742815751 | API uploaded, digest equal; download equal |
| 10 | `rewardbook-inputs-1793923200.tar` | 15728640 | `ba31ef522351e3875dcd4e7ff1b7989787cc71515f82668972e037ba8612bf6f` | 742815828 | API uploaded, digest equal; download equal |
| 11 | `rewardbook-inputs-1794009600.tar` | 15759360 | `df1e1592fbdc9425ce3ba8fc7ed3eec99458081b63ddf1c04eecb6c1a7651d45` | 742815888 | API uploaded, digest equal; download equal |
| 12 | `rewardbook-inputs-1794096000.tar` | 16363520 | `0d8730b7a60cafaf47bf81ed5dcdc8bd8d68ca23ce9c86f70db06bbd02b1c2ec` | 742815919 | API uploaded, digest equal; download equal |
| 13 | `tz43-fetch-1793404800.json` | 55310 | `5f56487e44aadcba1df2bc1316a889605baf83a4fcafc965b5ee4a18a6fec9b2` | 742816011 | API uploaded, digest equal; download equal |
| 14 | `tz43-fetch-1793404800.polls.jsonl` | 4990923 | `53ae4e79d354b3f8b35d497654159162b9c2290deb0d69b6f62b79c3fe8c1d71` | 742816068 | API uploaded, digest equal; download equal |
| 15 | `tz43-fetch-1793491200.json` | 55330 | `55f95448c4ba6abe1d1b154ff0e014ef190ffb7be861a7f6cb1a3bcddec7a1bd` | 742816109 | API uploaded, digest equal; download equal |
| 16 | `tz43-fetch-1793491200.polls.jsonl` | 5010687 | `1aac9148f26b55664b248be60b62394defc1b117b63bcd952c632bf96b3ebf54` | 742816152 | API uploaded, digest equal; download equal |
| 17 | `tz43-fetch-1793577600.json` | 55447 | `8589729bfe267feb57208833064bc71006e592e22edd8290d70bbc2b4474d9b5` | 742816189 | API uploaded, digest equal; download equal |
| 18 | `tz43-fetch-1793577600.polls.jsonl` | 5027379 | `19d765c78c93e9d4175328615ae3dc27b3e2f0c1dd7f6084eeab672a9e56427c` | 742816218 | API uploaded, digest equal; download equal |
| 19 | `tz43-fetch-1793664000.json` | 55449 | `1405b48ac2459f052b5b36dea8e85dd6cb0e112b49ac21030955d96f890eec02` | 742816263 | API uploaded, digest equal; download equal |
| 20 | `tz43-fetch-1793664000.polls.jsonl` | 5014920 | `4a5ef449ed6b1d2bf1378b817671b9bb3cac477c5a9fa6e5068d9673b24977cb` | 742816321 | API uploaded, digest equal; download equal |
| 21 | `tz43-fetch-1793750400.json` | 55543 | `1ed8768bd80b54220c0437e15fc424943a8829b716d7ba70f2b586f5ae14099c` | 742816379 | API uploaded, digest equal; download equal |
| 22 | `tz43-fetch-1793750400.polls.jsonl` | 4967708 | `f06145aa32845b9f3a65b8616e5842218b03869a3fc18d5a4bf1aaaa57fec920` | 742816445 | API uploaded, digest equal; download equal |
| 23 | `tz43-fetch-1793836800.json` | 55625 | `7d502a56ad2a4a3f95150bbcfc8c52c1190f2b977d9d1a72e2e1c4b3c2f5ba25` | 742816478 | API uploaded, digest equal; download equal |
| 24 | `tz43-fetch-1793836800.polls.jsonl` | 5055307 | `7918f3b6629489fcff4fd22cdb049a89e1e1ef63b86738c73ec680e17e5eff5d` | 742816529 | API uploaded, digest equal; download equal |
| 25 | `tz43-fetch-1794009600.json` | 55639 | `29e17ecde5f5d705e297bdc2be7e5e150aa50d06c3ac66ba9b1c4c13225b5708` | 742816581 | API uploaded, digest equal; download equal |
| 26 | `tz43-fetch-1794009600.polls.jsonl` | 5037697 | `91582ccfb9145559277d196f61e804e6be205d0b18d6168a1db6975711d6cf15` | 742816632 | API uploaded, digest equal; download equal |
| 27 | `tz43-fetch-1794096000.json` | 55660 | `a3ebc56744facb5c00f862c1f5d70a564672b68b5cc276398f32ae7f1bc0c552` | 742816680 | API uploaded, digest equal; download equal |
| 28 | `tz43-fetch-1794096000.polls.jsonl` | 5047340 | `7b0d86338359fbb4d5f4f7b54c6f36e0d45f2ed5c4d6d5731358c8e4e3099a82` | 742816730 | API uploaded, digest equal; download equal |
| 29 | `tz43-days-1793404800.json` | 145864 | `d93f998fba7795f30379c06e2058c55f4eba9d0c340536a3d5a4d1636b765ee6` | 742816771 | API uploaded, digest equal; download equal |
| 30 | `tz43-days-1793404800.slots.txt` | 47260 | `ec4494031d22891f22ec2822287c0127c4f96f39dac1337f3980419813052400` | 742816818 | API uploaded, digest equal; download equal |
| 31 | `tz43-days-1793491200.json` | 147006 | `50e19969a8196ef3fe8b069056b75bb3ff5f5ba1c41a9ad70a48bd7e88ebaaae` | 742816879 | API uploaded, digest equal; download equal |
| 32 | `tz43-days-1793491200.slots.txt` | 47077 | `5a7169dbcdb3186b588e2bd77ef5017dc792f1ead7cc8d2b9c11a55cee90f763` | 742816931 | API uploaded, digest equal; download equal |
| 33 | `tz43-days-1793577600.json` | 146744 | `93c76d1594b1edef03e192c02cc67b0264e43ca4b77b6d49939845f5876dc57c` | 742816979 | API uploaded, digest equal; download equal |
| 34 | `tz43-days-1793577600.slots.txt` | 46799 | `aae9a59997c591b90672bec21ea2489e2f7e654eba03590bc8d1ff411a186e1c` | 742817035 | API uploaded, digest equal; download equal |
| 35 | `tz43-days-1793664000.json` | 147691 | `a80c3d721fce47537ff927c42b989cd4409d25b7c3a1e2c4e024a2463d48c54d` | 742817084 | API uploaded, digest equal; download equal |
| 36 | `tz43-days-1793664000.slots.txt` | 46785 | `dc9dff0e13153ee045ada2cb805c9567ce9bb4b490f88c40aa0821442fe8660b` | 742817122 | API uploaded, digest equal; download equal |
| 37 | `tz43-days-1793750400.json` | 155059 | `4f9ca91d2798fb9f7b496e98baa02d4fe9f6efb5f60f979540f682fb7fdadfa9` | 742817176 | API uploaded, digest equal; download equal |
| 38 | `tz43-days-1793750400.slots.txt` | 47105 | `71101c5d670141ce064c671824d5c8c8c1615ffce4801b1a422baa3df4281cdc` | 742817228 | API uploaded, digest equal; download equal |
| 39 | `tz43-days-1793836800.json` | 149722 | `e7266b1d2d05e1191095e9cd184e6bb15571ea7380fa1e4f51db90a5342e200d` | 742817282 | API uploaded, digest equal; download equal |
| 40 | `tz43-days-1793836800.slots.txt` | 46750 | `ec5792be99ff4169b4574b3a8ce04855ad7a5fcd51aba1b51baf4cc9d8ce44e5` | 742817327 | API uploaded, digest equal; download equal |
| 41 | `tz43-days-1794009600.json` | 146104 | `f3018bb242bff3b1d7483622cd4065074cc42faa90b1e8357d223c2796a6dfd5` | 742817397 | API uploaded, digest equal; download equal |
| 42 | `tz43-days-1794009600.slots.txt` | 46914 | `a0fdb71edc318fb7e41989c1aca3b591c9b3e4db39274e87588354639725c1e6` | 742817476 | API uploaded, digest equal; download equal |
| 43 | `tz43-days-1794096000.json` | 144626 | `910ed69e85ab28dc81a334538d229a66ba17107260325c1afe5eae95de02e91f` | 742817521 | API uploaded, digest equal; download equal |
| 44 | `tz43-days-1794096000.slots.txt` | 46970 | `00caaab0888d85779398751281da3e9219cfdf9742c77b5914499cf0c4421436` | 742817562 | API uploaded, digest equal; download equal |
| 45 | `tz43-reading.json` | 9377 | `175d366101cd825437a1cd393aa57642965f7ffb9fe831746c2d9b2187d50be1` | 742817620 | API uploaded, digest equal; download equal |
| 46 | `tz43-set.json` | 6175 | `904f1b9b8244a15fe48549e39ffc879f68ad31de6963a41c05f5afc607edf0f7` | 742817656 | API uploaded, digest equal; download equal |
| 47 | `tz44-manifest.json` | 392914 | `491dcaf037e15e26d25512b609afbe68655952f321d92fa8ef208ee966650c8b` | 742817691 | API uploaded, digest equal; download equal |

The `verify` column is my own cross-reading of the two logs, 47 of 47. It is recorded, not asserted: the assertion is `verify`'s, §5.

Every TZ-43 asset `tz43-<path, / as ->` is the forensic file `tz43-work--<path, / as -->` of G-SOURCE, by the same bytes and SHA-256 (`logs/40-pack.log`, `G-SOURCE … equal`, 34 lines).

### 2.3 B-UPLOAD — who ran it and when (`logs/60-upload.log`, `logs/61-upload-wait.log`)

- **Handed over:** 2026-11-13T07:37:43Z (`61-upload-wait.log`), once, in Russian, as §3.6 words it.
- **Run by the Boss** in a root shell, the paste verbatim: `run begun` at `2026-11-13T08:02:52.540982605Z`, one run, `exit=0` — 25 min 9 s after the hand-over and inside the `21,600` s bound. `runs begun 1`, `exit lines 1 of 1`, `upload processes 0` at the last wait read, 08:05:00 UTC.
- **Its reads and its credential:**

```
[2026-11-13T08:02:52Z] MemAvailable 239050752 bytes, floor 98319394; free 9426665472 bytes, floor 7800000000
[2026-11-13T08:02:53Z] set 7bed9f17d3ffc2c1fffcf91a812d2aa71c677868389999df3a5744f37576fa37: 47 assets, 229053786 bytes, at commit ab0a8be170786ee9b4c9bfd18ed5a522db669932
[2026-11-13T08:02:53Z] credential: the primary checkout's remote URL
[2026-11-13T08:02:54Z] created the Release on tz-44-l0-inputs, id 443961874, target ab0a8be170786ee9b4c9bfd18ed5a522db669932
```

- **Then 47 `U` lines**, each `"action": "uploaded"`, 08:02:55 to 08:03:49 UTC, and the completion record `{"action": "complete", "assets": 47, … "created": true, "credential": "the primary checkout's remote URL", "held": 0, "release_id": 443961874, "sent": 47, …}`.
- **Its last lines:**

```
[2026-11-13T08:03:49Z] transfers so far 50: 0 started outside the idle stretch, 0 ended after its second 590; 0.0 s held
[2026-11-13T08:03:49Z] UPLOAD COMPLETE: Release 443961874 on tz-44-l0-inputs, 47 assets - 47 sent, 0 already held - 229053786 bytes
[2026-11-13T08:03:49Z] malloc tuned: True
[2026-11-13T08:03:49Z] peak memory of this run: 37629952 bytes
[2026-11-13T08:03:49Z] opens refused: 0, by TZ-27's hook: 0; reward book opens: 0, listings: 0
exit=0
```

`upload.jsonl` holds 48 lines, its last the `complete` record with `assets` 47. `transfers.jsonl` holds 99 lines after `verify`.

### 2.4 The venue's geoblock (`logs/50-geoblock.log`), once

```
2026-11-13T07:37:22.780206912Z
[2026-11-13T07:37:22Z] DNS polymarket.com: ['104.18.34.205', '172.64.153.51', '2606:4700:4408::ac40:9933', '2606:4700:440d::6812:22cd']
[2026-11-13T07:37:23Z] GEOBLOCK READ: https://polymarket.com/api/geoblock, status 200, 66 bytes in 0.18 s; blocked True, country 'PL', region '14'; reply keys ['blocked', 'country', 'ip', 'region']
[2026-11-13T07:37:23Z] malloc tuned: True
[2026-11-13T07:37:23Z] peak memory of this run: 37515264 bytes
[2026-11-13T07:37:23Z] opens refused: 0, by TZ-27's hook: 0; reward book opens: 0, listings: 0
exit=0
```

The DNS line lists the addresses `polymarket.com` resolves to, which are the venue's, not the host's. The reply's `ip` key is named and its value is neither printed nor written. **It gates nothing and decides nothing here.**

### 2.5 The host, at §0.3 and §3.9 (`logs/03-host-gate.log`, `logs/90-host-gate-again.log`)

| read | §0.3 | §3.9 |
|---|---|---|
| instant | 2026-11-13 07:34:03 UTC | 08:06:36 UTC |
| boot | `uptime -s` 2026-08-02 07:24:32; one boot listed, `48a803f0…`, first entry 2026-08-14 22:16:00 | the same |
| `nproc`; `MemTotal` | `1`; `978640 kB` | the same |
| `/proc/meminfo` `MemAvailable` / `SwapFree` | `262192 kB` / `2410148 kB` | `234100 kB` / `2305716 kB` |
| H1: `find` | `/var/lib/btc-recorder/btc-updown-5m/1794396600/manifest.json`, one path | the same |
| H2: `df` | `/dev/vda2 31612203008 9700261888`; `grep -c` `3` | `/dev/vda2 31612203008 9423151104`; `3` |
| H3 | `3.12.3` | `3.12.3` |
| H4 | 13 lines: `regular file /var/lib/btc-pairbook-archive/ledger.jsonl` and `directory /var/lib/btc-rewardbook/<D0>` for the twelve `D0` | the same 13 |
| memory gate | `MemAvailable read 1 07:34:15: 454987776` | `MemAvailable read 1 08:06:40: 380186624` (recorded, no threshold) |
| units | recorder pid `2388318` `NRestarts` `0` since 2026-10-23 06:08:56; pair book `1358376` `32` since 2026-11-13 03:05:24; reward book `3137952` `1` since 2026-10-28 12:56:29; advisor `284419` `5` since 2026-11-05 20:35:50; both archives' services `inactive`/`dead`, `Result=success`; both timers `active`/`waiting`; the chain book `disabled` | the same |
| timers | `apt-daily-upgrade.timer` last 2026-11-13 06:15:00, next 2026-11-14 06:11:25; `btc-rewardbook-archive.timer` last 01:30:20; `btc-pairbook-archive.timer` last 03:00:20; `apt-daily.timer` next 09:26:29 | the same |
| `telemetry-watch.service` | `disabled` (exit 1), `inactive` (exit 3) | the same |
| advisor `commit.txt` | `4e6db2d16dda3da14957120d636f537dfc0bcc87` | the same |
| `/root/tz43-work` | `exit=1` (gone) | `exit=1` |
| code trees | six of six `exit=0` | six of six |
| forensic store | `2487` files; `32` `tz43-work--fetch--`/`--days--` files | `2487`; `32` |
| worktrees | `/root/btc-5m-twap` `783f31b [main]`, `/root/btc-recorder-svc` `e3975b5 (detached HEAD)` | those two and `/root/tz44-work/wt` `ab0a8be [tz-44-l0-inputs-release]` |
| `du -sb` | rewardbook `630759076`, pairbook `1024964005`, forensics `396265017`, `/root/.claude-8j` `23557263` | `657890633`, `1071732672`, `396265017`, `23966413` |
| journal | `2.9G` | `2.9G` |

**Systemd's reload records and the package history since 2026-11-10** (printed, carrying no threshold):

- **The package manager's runs** were 2026-11-11 06:23:00 to 06:23:10 and 2026-11-12 06:20:56 to 06:21:36 UTC, among them `linux-generic` and `linux-image-generic` 6.8.0-147 → 6.8.0-149. Neither restarted a capture unit.
- **`crypto-deploy.service`, another project's unit, reloaded systemd eleven times on 2026-11-12, from 21:59:57 to 22:00:01 UTC.**
- **Off-calendar runs.** At 22:10:01 the pair book's archive ran off its calendar and ended `status=75/TEMPFAIL`, `Failed with result 'exit-code'`; its tag `pairbook-streams-1794521401` is on `origin`. At 22:30:01 the reward book's archive ran off its calendar and finished; its tag is `rewardbook-streams-1794522601`.
- **Calendar runs, both finished:** the reward book's archive at 2026-11-13 01:30:20 (tag `rewardbook-streams-1794533420`), and the pair book's archive at 03:00:20, which restarted the pair book to pid `1358376`, `NRestarts` `32`.

These are the same 600 s and 1,800 s after a start of each timer that map §7 items 115 and 129 record. No run of either archive fell inside this TZ's span.

**The scratch listing at §0.3** — the directory holding this session's own:
- `38f3be57-0238-5ea4-b9d4-f1eebc9ee01c`, this session's own.
- `4d2d9437-830e-42e6-a940-c4076e8879af`, 07:32.
- `50181f4d-39a8-5455-ad6a-3aaa95edd48a`, 07:31.
- `8e3e58b1-5f4a-46d7-8814-25078c677104`, 2026-11-10.
- `c78295f5-9a1d-4177-ac5a-b93cd56a49da`, 2026-11-08.
- `d4894963-361e-43df-9b59-1207e3b15362`, 07:30.
- `fd099d3c-2537-55ea-a4a0-314ac50cff1f`, 2026-11-10.

At §3.9 three were left: the session's own, `4d2d9437…` and `c78295f5…`.

### 2.6 Every free-space and `MemAvailable` read, with its instant and bound

| instant (UTC) | where | `MemAvailable` | bound | free bytes | bound |
|---|---|---|---|---|---|
| 07:34:03 / 07:34:15 | §0.3 host gate | `454987776` | `98319394` | `9700261888` | `8200000000` |
| 07:36:30 | `pack`, first run | `215879680` | `98319394` | `9683615744` | `7800000000` |
| 07:37:01 | `pack`, second run | `220917760` | `98319394` | `9496092672` | `7800000000` |
| 08:02:52 | `upload` | `239050752` | `98319394` | `9426665472` | `7800000000` |
| 08:05:06 | `verify` | `259362816` | `98319394` | `9423974400` | `7800000000` |
| 08:06:36 / 08:06:40 | §3.9 host gate again | `380186624` | recorded | `9423151104` | recorded |
| 08:06:45 | §3.9 closing reads | `422216 kB` (`/proc/meminfo`) | recorded | `9422970880` | recorded |

`pack` read free space before each day's archive against `7,400,000,000`, and every day passed. The first run read `9,683,615,744` at its start and wrote `186,490,880` bytes of archives. The lowest free space anywhere in the run was `9,422,970,880`.

### 2.7 Every mode's printed peak (V16; against §0.4's `49,159,697`)

| mode | log | peak bytes |
|---|---|---|
| `I0 fingerprint` | `02-fingerprint.log` | `36749312` |
| `I0 number` | `05-number.log` | `36352000` |
| `I0 number` | `10-number.log` | `36483072` |
| `I fingerprint` | `12-fingerprint.log` | `36487168` |
| `I selftest` | `20-selftest.log` | `37384192` |
| `I still` | `30-still.log` | `36749312` |
| `I scratch` | `31-scratch.log` | `36749312` |
| `I reclaim` (scratch) | `32-reclaim-scratch.log` | `36741120` |
| `I pack` | `40-pack.log` | `37924864` |
| `I pack` again | `41-pack-again.log` | `37990400` |
| `I geoblock` | `50-geoblock.log` | `37515264` |
| `I upload` (the Boss's run) | `60-upload.log` | `37629952` |
| `I verify` | `70-verify.log` | `37244928` |
| `I still` | `80-still.log` | `36605952` |
| `I reclaim` (own) | §9, the session | `36098048` |

Every peak sits under the Architect's bound `41,000,000` and under `49,159,697`. Every mode printed `malloc tuned: True` and `opens refused: 0, by TZ-27's hook: 0`. Only `pack` opened the reward book: `reward book opens: 3357, listings: 12` at each run, and `0, 0` at every other mode.

### 2.8 The transfers

- **`upload`:** `transfers so far 50: 0 started outside the idle stretch, 0 ended after its second 590; 0.0 s held`.
- **`verify`:** `transfers 99, upload's and verify's: 0 started outside the idle stretch, 0 ended after its second 590; 0.0 s held`.
- **`pack`:** `G-SOURCE` was held 0.0 s and began at second 390 of its window (first run) and 421 (second run). Each day was held 0.0 s and began at seconds 390 to 405 (first run).

### 2.9 Every file the run wrote, by SHA-256 (outside the branch worktree, at §3.9)

| path under `/root/tz44-work/` | bytes | SHA-256 |
|---|---|---|
| `logs/00-instant.log` | 70 | `a95318e0507cf24eefd48041529aa3ad6ce3b9bdaa3f22891fc5a5bf79d9f0c1` |
| `logs/01-stage.log` | 273 | `c80182c40e358abc85d6d0fe4b0517eff0bdc42b7bf30aa941bbe000b5f26a20` |
| `logs/02-fingerprint.log` | 11887 | `49906ca90db6318254b4217e5c12f762e9f249f8a3c721863b6b40d9387b9189` |
| `logs/03-host-gate.log` | 15600 | `8a17a2b6a86c087dd80c5161e22ba08b2cad0a3999437fc5f288d63447df2d8e` |
| `logs/05-number.log` | 443 | `28d2548372b583a7c4b60ce5f980ae42ca2089c55014be9046704de39e69be91` |
| `logs/05-refs.log` | 10500 | `13d9733cb4e323ba32298e3fcdfb8ebbb4967283f0c5026463c81d52f2417c5d` |
| `logs/10-number.log` | 481 | `7928e9da2070bc5677d0ab4e3952a7114a4695a0fcfc663c8689569205240e88` |
| `logs/11-worktree.log` | 471 | `85ac0ac752a1a3cea0f82bf2a850d39c60f5142ab3e6e0fc02832091fd1fed5e` |
| `logs/12-fingerprint.log` | 11887 | `dfbb036eb611c65b152a48fc7a9054663cbedbf2c0077be19be682f11f8ab5aa` |
| `logs/13-push.log` | 11113 | `09e433a6fd7bdbde9bb587c36baefa4bd927c6c4f9bddb7dd64cd260f967c111` |
| `logs/14-pr.log` | 94 | `96c3c93e644dfa56f073b5d6fa55672cbeab1d4de31e1a4ece1cdb9f6633086b` |
| `logs/20-selftest.log` | 7482 | `56359d61baef7f9394fd21c991d4eab44ab3e7623794636f03711ca8254134c8` |
| `logs/30-still.log` | 1459 | `77c9fb37f7404884a6ba7c11eec868e02f476e78723157ec8f0c2f14731411d1` |
| `logs/31-scratch.log` | 1371 | `ce15193e3cf8bad3dad2df6400c374feafe60302641f1e4c926f028005347721` |
| `logs/32-reclaim-scratch.log` | 657 | `69087da22998f0d616eb21dbf67b9e246467bc5ecd0a70c4b5a22a12aa4237d9` |
| `logs/40-pack.log` | 17443 | `62f5444eb0df51c78ce3146c89ad3248f768f4b45268adb392d0ba4dfb120b38` |
| `logs/41-pack-again.log` | 17571 | `d86636a9766b21a97f83af2835e14d1a1c3a8af558e334220479fcf446a24d3d` |
| `logs/50-geoblock.log` | 572 | `9e1f86272c8e87e97c95de194a4e4869ff7cccdc350b981940264bdffcd58446` |
| `logs/60-upload.log` | 17611 | `2032ef97e33f079fbfc5321bb4b4de69e93de544633dfba921c69dc79a21b191` |
| `logs/61-upload-wait.log` | 1451 | `acce8296e0efadf41f694e1b5a59b0964c6d75db3d3d241929486c437ee6b617` |
| `logs/70-verify.log` | 18311 | `9aa3e092f22568f73ea7f903724ab7b59a15936fff4596987a6c388981df5a09` |
| `logs/80-still.log` | 1495 | `8758dc0c010bdc54774810324832f50dc321e062f99760f621b24a638eb30a71` |
| `logs/90-host-gate-again.log` | 15342 | `b4057b4cb582038df3e583bd72c84bdcd89f2c8d1d41962265e5bf6e8bb7c17b` |
| `logs/91-closing.log` | 3273 | `19798bd5e9d31d593ee32abdbd8d777c38620a9cb254f50c88f07b448f809212` |
| `logs/92-selfcheck.log` | 221 | `5807b36ec3f5dd2788067160deff4593171015ae643981cc83d06d758e667b64` |
| `out/rewardbook-inputs-1793145600.tar` … `out/rewardbook-inputs-1794096000.tar` | §2.2, rows 1 to 12 | §2.2, rows 1 to 12 |
| `out/tz44-manifest.json` | 392914 | `491dcaf037e15e26d25512b609afbe68655952f321d92fa8ef208ee966650c8b` |
| `set.json` | 10780 | `7bed9f17d3ffc2c1fffcf91a812d2aa71c677868389999df3a5744f37576fa37` |
| `state.json` | 870 | `28293d9ef26742d6dead480fc601a1f4c90ba143b5b4d5e1c66922fa5f0d9e15` |
| `upload.jsonl` | 15435 | `75751de36ffc9ea2d30832fb3b39c2e923ccab3bbcd3a7fac6971569f0aca598` |
| `transfers.jsonl` | 18549 | `441e896c47556cdc179028cc25c892efbf265a50a957272264b34213352de0f1` |
| `verify.json` | 23345 | `f086c10c7a9c312110f8bd3caee072c294fe62edac1c1cd2e0cfc2bcee4e01d8` |
| `stage/research/tz44-l0-inputs-release.py` | 90703 | `0b78807d9c5dec087138b0c9a329cb8c976157ab5c8a3fd4deee7cb31e89e190` |
| `stage/research/tz27-pairbook-archive.py` | 106284 | `2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673` |

That is 45 files. The self-test's temporary tree `selftest-tmp/` was removed by the self-test itself (its 38th check). The worktree `wt/` holds exactly the pushed `HEAD` `ab0a8be`.

---

## 3. Publication

| item | value |
|---|---|
| branch | `tz-44-l0-inputs-release`, one commit `ab0a8be170786ee9b4c9bfd18ed5a522db669932` above `783f31b`, pushed 2026-11-13 07:35:18 UTC through the remote URL's own credential; `origin`'s branch at the worktree's `HEAD` (`logs/13-push.log`) |
| file | `research/tz44-l0-inputs-release.py`, 1616 lines, 90703 bytes, sha256 `0b78807d9c5dec087138b0c9a329cb8c976157ab5c8a3fd4deee7cb31e89e190`, byte for byte Appendix A |
| pull request | #44, https://github.com/seahomebatumi-ai/btc-5m-twap/pull/44 — not merged |
| Release | id `443961874`, tag `tz-44-l0-inputs`, lightweight, at `ab0a8be170786ee9b4c9bfd18ed5a522db669932`; `draft` `false`, `prerelease` `false`, `make_latest` `"false"`; 47 assets, `229053786` bytes |
| hashes | each asset's local SHA-256 (`pack`'s set), the API's `digest` and the anonymous download's SHA-256 — 47 of 47 equal, §2.2. `I verify` stands in for contract §5.1's `curl`, as TZ-44 §10 C8 says |
| tag on `origin` | `ab0a8be170786ee9b4c9bfd18ed5a522db669932	refs/tags/tz-44-l0-inputs`, no peeled line (`logs/91-closing.log`) |

**Contract §4.2's self-check, with TZ-44's two lines more** (`logs/92-selfcheck.log`, `C` = `ab0a8be170786ee9b4c9bfd18ed5a522db669932`), verbatim:

```
2026-11-13T08:06:50.373147472Z
From https://github.com/seahomebatumi-ai/btc-5m-twap
 * [new tag]         tz-44-l0-inputs -> tz-44-l0-inputs
0
research/tz44-l0-inputs-release.py
1616	0	research/tz44-l0-inputs-release.py
0
```

Reading it line by line:
- The implementation commit is on `origin/main` **0** times.
- The diff names `research/tz44-l0-inputs-release.py` alone, `1616` lines added and `0` removed.
- `grep -E '\.parquet|\.zip'` printed nothing.
- No `.tar` and no `tz44-manifest` is in either tree: `0`.

The report is the one path pushed to `main`.

---

## 4. Gate

TZ-44 §4, quoted in short. Each gate but G-STILL and GEO is an identity of bytes or counts:

| gate | PASS condition (TZ-44 §4) | read | result |
|---|---|---|---|
| **G-SOURCE** | each literal row found in the committed report, and each file a regular file of that row's bytes and SHA-256: 34 of 34 | `34 of 34`, `42169992` bytes, both runs | **PASS** |
| **G-PACK** | every name classified; every member read whole and stored verbatim but a file of replies a line of which withholds it; every stream and other name left out and never opened; 12 archives, the manifest and the set written | `12 days of 12`; 2,238 members; withheld 0; streams 0, other 0; 14 outputs | **PASS** |
| **G-RESERVE** | opens equal to the members kept and the files of replies scanned, listings to the days, and the hook refusing nothing | opens `3357` = `2238` + `1119`; listings `12`; refused `0` | **PASS** |
| **DETERMINISM** | the second run's bytes equal to the first's, 14 of 14 | `14 of 14 outputs unchanged` | **PASS** |
| **G-UPLOAD** | each asset in the API's record by name, its size the set's, `state` `uploaded`, its digest `sha256:` the set's, its download URL the tag's; none missing, none beyond the set; the Release published on the tag | `47 of 47` | **PASS** |
| **G-DOWNLOAD** | each downloaded anonymously, whole, its bytes and SHA-256 the set's | `47 of 47 downloads, 229053786 bytes` = `set.json`'s `229053786` | **PASS** |
| **G-TAG** | lightweight, at the pack's commit | `tz-44-l0-inputs` at `ab0a8be…`, peeled `None` | **PASS** |
| **G-STILL** | every unit's `MainPID`, `NRestarts` and `ActiveState` unchanged | `G-STILL PASS: unchanged since 2026-11-13T07:35:40Z` | **PASS** |
| **GEO** | printed, no threshold | `blocked True, country 'PL', region '14'` | printed |

The deciding numbers to three decimals: G-SOURCE `34.000` of `34`; G-PACK `12.000` of `12` days; DETERMINISM `14.000` of `14`; G-UPLOAD and G-DOWNLOAD `47.000` of `47`. Nothing was tuned, and no gate was reinterpreted. **None of them judges a market:** this TZ read no price, scored nothing and decides no track.

---

## 5. Validation — in TZ-44 §7's numbering

| # | check | read | asserted |
|---|---|---|---|
| V1 | `I0 fingerprint` and `I fingerprint` | `FINGERPRINT PASS: revision 2026-11-12-a; anchors 6 of 6, 4 re-derived; rows 62: frozen 59 of 59 equal, tracked 2, reported 1`, twice (`02`, `12`) | yes — the instrument stops at the first mismatch |
| V2 | host gate | §0.3: H1, H2 (source/size; `grep -c` 3), H3, H4, memory (`454987776` ≥ `98319394`), disk (`9700261888` ≥ `8200000000`) — **7 of 7**; §3.9: H1 to H4 — **5 of 5** — memory `380186624` and disk `9423151104` recorded | by the Executor against the TZ's literal conditions, from the logs (no instrument assert) |
| V3 | `I0 number` | `NUMBER PASS - 2 of 2`, twice (`05-number`, `10-number`) | yes |
| V4 | §0.1's script | two lines a run, both runs: `1616 90703 0b78807d…`, `2078 106284 2cba96bc…` (`01-stage`, `11-worktree`) | yes — the script's asserts |
| V5 | `I selftest` | `SELFTEST PASS: 38 checks`; 38 `ok` lines (`20-selftest`) | yes |
| V6 | G-SOURCE | `the rows of its 34 files found 34 of 34`; `G-SOURCE PASS: 34 of 34 equal to TZ-43's report, 42169992 bytes`, both runs | yes |
| V7 | G-PACK | §2.1: `12 days of 12`, each day's names by kind, members and bytes, files scanned, withheld `0`, its archive's bytes and SHA-256, no excluded name; `days over their budget 0`; `47 assets`; outputs `wrote` 14, then `unchanged` 14 | yes |
| V8 | G-RESERVE | `G-RESERVE PASS: the store opened 3357 times - once a member kept, 2238, and once a file of replies scanned, 1119 - and listed 12 times, one a day; no other open or listing under /var/lib/btc-rewardbook`, both runs | yes |
| V9 | DETERMINISM | `DETERMINISM PASS: 14 of 14 outputs unchanged` | yes |
| V10 | `I geoblock` | one `GEOBLOCK READ:` line, §2.4 | printed, gates nothing |
| V11 | B-UPLOAD | one run, `exit=0`; `credential: the primary checkout's remote URL`; `UPLOAD COMPLETE: Release 443961874 on tz-44-l0-inputs, 47 assets - 47 sent, 0 already held - 229053786 bytes`; `upload.jsonl`'s last line `complete`, `assets` 47; the transfers' line, §2.3 | yes — TZ-27's `upload_set` asserts each record |
| V12 | `I verify` | `G-UPLOAD PASS: 47 of 47 assets by name, bytes, state and digest; G-DOWNLOAD PASS: 47 of 47 downloads, 229053786 bytes; G-TAG PASS: tz-44-l0-inputs at ab0a8be170786ee9b4c9bfd18ed5a522db669932`; the bytes equal `set.json`'s `229053786`; `transfers 99 …` | yes; one run, 08:05:06 to 08:06:20 UTC |
| V13 | `I still`, §3.8 | `G-STILL PASS: unchanged since 2026-11-13T07:35:40Z` | yes |
| V14 | §4.2 self-check | `0`; the one file, `1616` added `0` removed; nothing; `0` — §3 | read by the Executor |
| V15 | the hook | `opens refused: 0, by TZ-27's hook: 0` at every mode, its closing lines printed on every exit; `reward book opens` `3357` at `pack` alone | yes |
| V16 | memory and disk | every peak, §2.7, under `49,159,697`; every floor read, §2.6, none passing below `98,319,394` or `7,800,000,000`; `malloc tuned: True` at every mode | yes, at `pack`, `upload`, `verify` |
| V17 | `reclaim` | B-RECLAIM-SCRATCH below; B-RECLAIM-OWN, §9 | yes |
| V18 | the removals | §9 | — |
| V19 | the classifier | **no block refused**, below | — |

### §3.3 — `I still`, `I scratch` and B-RECLAIM-SCRATCH (V17, V19)

`I still` at 07:35:40 UTC recorded the four units in `state.json` (`logs/30-still.log`):

```
[2026-11-13T07:35:40Z] adv3-bot.service {'MainPID': '284419', 'NRestarts': '5', 'ActiveState': 'active'}, MemoryCurrent 8175616, MemoryPeak 51396608
[2026-11-13T07:35:40Z] btc-pairbook.service {'MainPID': '1358376', 'NRestarts': '32', 'ActiveState': 'active'}, MemoryCurrent 2228224, MemoryPeak 66072576
[2026-11-13T07:35:40Z] btc-recorder.service {'MainPID': '2388318', 'NRestarts': '0', 'ActiveState': 'active'}, MemoryCurrent 13058048, MemoryPeak 391000064
[2026-11-13T07:35:40Z] btc-rewardbook.service {'MainPID': '3137952', 'NRestarts': '1', 'ActiveState': 'active'}, MemoryCurrent 14114816, MemoryPeak 78729216
```

The four were the same at `I still` 08:06:24 UTC (`logs/80-still.log`), `G-STILL PASS`.

`I scratch /tmp/claude-0/-root-btc-5m-twap` at 07:35:46 UTC (`logs/31-scratch.log`), verbatim:

```
[2026-11-13T07:35:46Z] running 630626 started 2026-11-08T07:15:37Z claude
[2026-11-13T07:35:46Z] running 630636 started 2026-11-08T07:15:39Z claude
[2026-11-13T07:35:46Z] running 630645 started 2026-11-08T07:15:40Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-13T07:35:46Z] running 630666 started 2026-11-08T07:15:42Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-13T07:35:46Z] running 1387349 started 2026-11-13T07:32:15Z /usr/lib/node_modules/@anthropic-ai/claude-code/bin/claude.exe
[2026-11-13T07:35:46Z] 4d2d9437-830e-42e6-a940-c4076e8879af born 2026-11-13T07:32:16Z: live, process [1387349]
[2026-11-13T07:35:46Z] 50181f4d-39a8-5455-ad6a-3aaa95edd48a born 2026-11-13T07:31:00Z: earlier
[2026-11-13T07:35:46Z] 8e3e58b1-5f4a-46d7-8814-25078c677104 born 2026-11-10T07:48:40Z: earlier
[2026-11-13T07:35:46Z] c78295f5-9a1d-4177-ac5a-b93cd56a49da born 2026-11-08T07:15:42Z: live, process [630626, 630636, 630645, 630666]
[2026-11-13T07:35:46Z] d4894963-361e-43df-9b59-1207e3b15362 born 2026-11-13T07:30:59Z: earlier
[2026-11-13T07:35:46Z] fd099d3c-2537-55ea-a4a0-314ac50cff1f born 2026-11-10T07:48:41Z: earlier
```

Four directories were named **earlier**:
- TZ-43's session's own, `fd099d3c…`.
- `8e3e58b1…`, live at TZ-43's run and no longer.
- Two born on 2026-11-13 at 07:30:59 and 07:31:00 UTC, a minute before this session's process: `d4894963…` and `50181f4d…`. No running process made them, and no report names them.

`c78295f5…` stays live, with the remote-control processes of 2026-11-08. `4d2d9437…` is live, born one second after this session's process. **The rule alone decided.**

**B-RECLAIM-SCRATCH, run by the Executor, not refused by the classifier** (`logs/32-reclaim-scratch.log`), every line:

```
2026-11-13T07:36:07.497153047Z
[2026-11-13T07:36:07Z] reclaim: 3836 report tokens; forensic store holds 2487 files
[2026-11-13T07:36:07Z] RECLAIM PASS: 10 files considered, 0 named by a report, 0 kept by name, 0 copied, 0 already held; forensic store 2487 -> 2487 files
[2026-11-13T07:36:07Z] malloc tuned: True
[2026-11-13T07:36:07Z] peak memory of this run: 36741120 bytes
[2026-11-13T07:36:07Z] opens refused: 0, by TZ-27's hook: 0; reward book opens: 0, listings: 0
exit=0
2026-11-13T07:36:23.889318285Z
exit=0
exit=1
2026-11-13T07:36:23.924281873Z
exit=0
exit=1
2026-11-13T07:36:23.945780648Z
exit=0
exit=1
2026-11-13T07:36:23.976011149Z
exit=0
exit=1
```

The `reclaim` named all four directories by their full paths, `/tmp/claude-0/-root-btc-5m-twap/<UUID>`. The four `rm -rf` and `test -e` pairs followed, in the order `50181f4d…`, `8e3e58b1…`, `d4894963…`, `fd099d3c…`, one tree each: `exit=0`, then `exit=1`. **The store's count after equals before plus the copies: 2487 → 2487.**

### §9 — B-RECLAIM-OWN (V17, V18)

**Run by the Executor in the session, after §3.9 and with this report drafted in `CryptoReports/`. The classifier refused no line.** Its output was written to no file. Every line follows, as the session printed it.

`cd /root/tz44-work && nice -n 19 /root/tz04a-env/venv/bin/python -B /root/tz44-work/wt/research/tz44-l0-inputs-release.py reclaim /root/tz44-work`:

```
[2026-11-13T08:13:05Z] reclaim: 3884 report tokens; forensic store holds 2487 files
[2026-11-13T08:13:05Z] reclaim: /root/tz44-work/wt skipped: no file but its HEAD's, and HEAD ab0a8be170786ee9b4c9bfd18ed5a522db669932 is its upstream's
[2026-11-13T08:13:05Z] R copied 7bed9f17d3ffc2c1fffcf91a812d2aa71c677868389999df3a5744f37576fa37 /root/btc-forensics/tz44-work--set.json
[2026-11-13T08:13:05Z] R copied 28293d9ef26742d6dead480fc601a1f4c90ba143b5b4d5e1c66922fa5f0d9e15 /root/btc-forensics/tz44-work--state.json
[2026-11-13T08:13:05Z] R copied 441e896c47556cdc179028cc25c892efbf265a50a957272264b34213352de0f1 /root/btc-forensics/tz44-work--transfers.jsonl
[2026-11-13T08:13:05Z] R copied 75751de36ffc9ea2d30832fb3b39c2e923ccab3bbcd3a7fac6971569f0aca598 /root/btc-forensics/tz44-work--upload.jsonl
[2026-11-13T08:13:05Z] R copied f086c10c7a9c312110f8bd3caee072c294fe62edac1c1cd2e0cfc2bcee4e01d8 /root/btc-forensics/tz44-work--verify.json
[2026-11-13T08:13:05Z] R copied a95318e0507cf24eefd48041529aa3ad6ce3b9bdaa3f22891fc5a5bf79d9f0c1 /root/btc-forensics/tz44-work--logs--00-instant.log
[2026-11-13T08:13:05Z] R copied c80182c40e358abc85d6d0fe4b0517eff0bdc42b7bf30aa941bbe000b5f26a20 /root/btc-forensics/tz44-work--logs--01-stage.log
[2026-11-13T08:13:05Z] R copied 49906ca90db6318254b4217e5c12f762e9f249f8a3c721863b6b40d9387b9189 /root/btc-forensics/tz44-work--logs--02-fingerprint.log
[2026-11-13T08:13:05Z] R copied 8a17a2b6a86c087dd80c5161e22ba08b2cad0a3999437fc5f288d63447df2d8e /root/btc-forensics/tz44-work--logs--03-host-gate.log
[2026-11-13T08:13:05Z] R copied 28d2548372b583a7c4b60ce5f980ae42ca2089c55014be9046704de39e69be91 /root/btc-forensics/tz44-work--logs--05-number.log
[2026-11-13T08:13:05Z] R copied 13d9733cb4e323ba32298e3fcdfb8ebbb4967283f0c5026463c81d52f2417c5d /root/btc-forensics/tz44-work--logs--05-refs.log
[2026-11-13T08:13:05Z] R copied 7928e9da2070bc5677d0ab4e3952a7114a4695a0fcfc663c8689569205240e88 /root/btc-forensics/tz44-work--logs--10-number.log
[2026-11-13T08:13:05Z] R copied 85ac0ac752a1a3cea0f82bf2a850d39c60f5142ab3e6e0fc02832091fd1fed5e /root/btc-forensics/tz44-work--logs--11-worktree.log
[2026-11-13T08:13:05Z] R copied dfbb036eb611c65b152a48fc7a9054663cbedbf2c0077be19be682f11f8ab5aa /root/btc-forensics/tz44-work--logs--12-fingerprint.log
[2026-11-13T08:13:05Z] R copied 09e433a6fd7bdbde9bb587c36baefa4bd927c6c4f9bddb7dd64cd260f967c111 /root/btc-forensics/tz44-work--logs--13-push.log
[2026-11-13T08:13:05Z] R copied 96c3c93e644dfa56f073b5d6fa55672cbeab1d4de31e1a4ece1cdb9f6633086b /root/btc-forensics/tz44-work--logs--14-pr.log
[2026-11-13T08:13:05Z] R copied 56359d61baef7f9394fd21c991d4eab44ab3e7623794636f03711ca8254134c8 /root/btc-forensics/tz44-work--logs--20-selftest.log
[2026-11-13T08:13:05Z] R copied 77c9fb37f7404884a6ba7c11eec868e02f476e78723157ec8f0c2f14731411d1 /root/btc-forensics/tz44-work--logs--30-still.log
[2026-11-13T08:13:05Z] R copied ce15193e3cf8bad3dad2df6400c374feafe60302641f1e4c926f028005347721 /root/btc-forensics/tz44-work--logs--31-scratch.log
[2026-11-13T08:13:05Z] R copied 69087da22998f0d616eb21dbf67b9e246467bc5ecd0a70c4b5a22a12aa4237d9 /root/btc-forensics/tz44-work--logs--32-reclaim-scratch.log
[2026-11-13T08:13:05Z] R copied 62f5444eb0df51c78ce3146c89ad3248f768f4b45268adb392d0ba4dfb120b38 /root/btc-forensics/tz44-work--logs--40-pack.log
[2026-11-13T08:13:05Z] R copied d86636a9766b21a97f83af2835e14d1a1c3a8af558e334220479fcf446a24d3d /root/btc-forensics/tz44-work--logs--41-pack-again.log
[2026-11-13T08:13:05Z] R copied 9e1f86272c8e87e97c95de194a4e4869ff7cccdc350b981940264bdffcd58446 /root/btc-forensics/tz44-work--logs--50-geoblock.log
[2026-11-13T08:13:05Z] R copied 2032ef97e33f079fbfc5321bb4b4de69e93de544633dfba921c69dc79a21b191 /root/btc-forensics/tz44-work--logs--60-upload.log
[2026-11-13T08:13:05Z] R copied acce8296e0efadf41f694e1b5a59b0964c6d75db3d3d241929486c437ee6b617 /root/btc-forensics/tz44-work--logs--61-upload-wait.log
[2026-11-13T08:13:05Z] R copied 9aa3e092f22568f73ea7f903724ab7b59a15936fff4596987a6c388981df5a09 /root/btc-forensics/tz44-work--logs--70-verify.log
[2026-11-13T08:13:05Z] R copied 8758dc0c010bdc54774810324832f50dc321e062f99760f621b24a638eb30a71 /root/btc-forensics/tz44-work--logs--80-still.log
[2026-11-13T08:13:05Z] R copied b4057b4cb582038df3e583bd72c84bdcd89f2c8d1d41962265e5bf6e8bb7c17b /root/btc-forensics/tz44-work--logs--90-host-gate-again.log
[2026-11-13T08:13:05Z] R copied 19798bd5e9d31d593ee32abdbd8d777c38620a9cb254f50c88f07b448f809212 /root/btc-forensics/tz44-work--logs--91-closing.log
[2026-11-13T08:13:05Z] R copied 5807b36ec3f5dd2788067160deff4593171015ae643981cc83d06d758e667b64 /root/btc-forensics/tz44-work--logs--92-selfcheck.log
[2026-11-13T08:13:05Z] R copied b268ef086a2d2d23afa6cb33b354eddd0d3589aca1621aa15901b6441667f9f6 /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793145600.tar
[2026-11-13T08:13:05Z] R copied b214536add4d9b43cd6f634cd8c26cb92d9f82b0c6bd6508564a8b21a2529dc1 /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793232000.tar
[2026-11-13T08:13:05Z] R copied e3189d4cf76f5acb2a14351610c7ea9dc1bd294e19cee310eef80b421b2b910f /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793318400.tar
[2026-11-13T08:13:05Z] R copied 563a3ccf2df5e48641dff892de6f50d4421c071cd42ae7cbb147b3ed8b2f3c1f /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793404800.tar
[2026-11-13T08:13:05Z] R copied 0614a35f95eb4fe7f9ad7f8689fc5f1876b811e6dc9fa6028e2a0a6e7da8b751 /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793491200.tar
[2026-11-13T08:13:05Z] R copied 67043eb13198b2c599b042b0385f06d925db74ff0f25e264e8555627dd987dbb /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793577600.tar
[2026-11-13T08:13:05Z] R copied 92614b11fe80d5cca913c4633f2bcd0f96200ae0f0050ef2a74c68a491b67a45 /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793664000.tar
[2026-11-13T08:13:05Z] R copied a8ec58f4cc250a12c63bcb743d7f0ddd03596e374990794a0c803167ad3e6442 /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793750400.tar
[2026-11-13T08:13:05Z] R copied 4179070b6d7add6a682f4d8f26664b2920b6113fe4119cf274b5460c437400e6 /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793836800.tar
[2026-11-13T08:13:06Z] R copied ba31ef522351e3875dcd4e7ff1b7989787cc71515f82668972e037ba8612bf6f /root/btc-forensics/tz44-work--out--rewardbook-inputs-1793923200.tar
[2026-11-13T08:13:06Z] R copied df1e1592fbdc9425ce3ba8fc7ed3eec99458081b63ddf1c04eecb6c1a7651d45 /root/btc-forensics/tz44-work--out--rewardbook-inputs-1794009600.tar
[2026-11-13T08:13:06Z] R copied 0d8730b7a60cafaf47bf81ed5dcdc8bd8d68ca23ce9c86f70db06bbd02b1c2ec /root/btc-forensics/tz44-work--out--rewardbook-inputs-1794096000.tar
[2026-11-13T08:13:06Z] R copied 491dcaf037e15e26d25512b609afbe68655952f321d92fa8ef208ee966650c8b /root/btc-forensics/tz44-work--out--tz44-manifest.json
[2026-11-13T08:13:06Z] R copied 2cba96bc9d41a46da1f04f4a3dc70aee707a0cc9bb4dc0dfa3c20bb0ad1ce673 /root/btc-forensics/tz44-work--stage--research--tz27-pairbook-archive.py
[2026-11-13T08:13:06Z] R copied 0b78807d9c5dec087138b0c9a329cb8c976157ab5c8a3fd4deee7cb31e89e190 /root/btc-forensics/tz44-work--stage--research--tz44-l0-inputs-release.py
[2026-11-13T08:13:06Z] RECLAIM PASS: 45 files considered, 45 named by a report, 0 kept by name, 45 copied, 0 already held; forensic store 2487 -> 2532 files
[2026-11-13T08:13:06Z] malloc tuned: True
[2026-11-13T08:13:06Z] peak memory of this run: 36098048 bytes
[2026-11-13T08:13:06Z] opens refused: 0, by TZ-27's hook: 0; reward book opens: 0, listings: 0
```

`cd /root/btc-5m-twap && git -C /root/btc-5m-twap worktree remove /root/tz44-work/wt; echo "exit=$?"`, without `--force`:

```
exit=0
```

`rm -rf /root/tz44-work; echo "exit=$?"`:

```
exit=0
```

The closing reads — `test -e /root/tz44-work; echo "exit=$?"`, `git worktree prune; git worktree list`, `find /root/btc-forensics -type f | wc -l` and `df -B1 --output=source,size,avail /var/lib/btc-recorder`:

```
exit=1
/root/btc-5m-twap       783f31b [main]
/root/btc-recorder-svc  e3975b5 (detached HEAD)
2532
Filesystem       1B-blocks      Avail
/dev/vda2      31612203008 9410662400
```

- **V17: the store's count after equals before plus the copies:** `2487 + 45 = 2532`. Every file named by this report's hash was copied, the twelve archives and the manifest among them. The two staged files were copied because the report names them by hash, `tz27-pairbook-archive.py` by `2cba96bc…`, map §0's `frozen` row. Nothing was kept by name alone: every log and `state.json` is also named by its hash in §2.9.
- **The Executor's own check of the copies:** each of the 45 files `/root/btc-forensics/tz44-work--*` was hashed with `sha256sum`, and **45 of 45** hashes are printed in this report. The forensic store reads `583,581,855` bytes by `du -sb`, from `396,265,017`.
- **V18:**
  - `git worktree remove` without `--force` printed `exit=0`.
  - `test -e /root/tz44-work` printed `exit=1`.
  - `git worktree list` names `/root/btc-5m-twap` and `/root/btc-recorder-svc` and nothing else.
  - B-RECLAIM-SCRATCH's four directories each read `exit=1` (§3.3).
- **What stays:**
  - The branch `tz-44-l0-inputs-release` stays on `origin` and as a local ref.
  - The Release and its tag stay.
  - The running units' code trees, the capture roots, both archives' state and the forensic store stay.
  - **TZ-44's session leaves** its own directory, `38f3be57-0238-5ea4-b9d4-f1eebc9ee01c`, with Claude Code's own copies of its background output under `tasks/`. It also leaves `4d2d9437-830e-42e6-a940-c4076e8879af`, born one second after the session's process. `c78295f5…` stays live, with the remote-control processes of 2026-11-08. The next TZ reclaims every directory its `scratch` names earlier.

---

## 6. What could not be implemented as written

Every departure, ambiguity and workaround. None moved a gate.

1. **Read-only steps before §0.0's check of the clock**, as contract §1 orders: `date -u`, `hostname`, `ls /root`, `git fetch origin` and `git merge --ff-only origin/main` (contract §1's pull, as a fetch and a fast-forward, from `4063e32` to `783f31b`), `git log`, `ls` and `wc -c` of the TZ and the map, and the reads of both.
2. **The map was read in the sections the header names**, not every line (map §7 item 139). That was §0 in full, §1's head and its refs record, §2.6, §3's lines on the forensic store, the worktrees and the sessions' directories, §6's named rows, and §7 items 130 to 161. **Appendix A was verified by its SHA-256** (§0.1, twice) and exercised by the self-test and every gate, not read line by line. Claude Code kept two long outputs of those map reads under its own project directory, `/root/.claude-8j/`, beside the transcript (map §7 item 118). They hold map text only.
3. **Lines the TZ's commands do not print were added to logs:**
   - An `exit=$?` line at the end of `01-stage`, `02-fingerprint`, `05-number`, `12-fingerprint`, `20-selftest`, `30-still`, `31-scratch`, `40-pack`, `41-pack-again` and `80-still`.
   - A `date -u +%FT%T.%NZ` line at the head of `10-number`, `11-worktree`, `13-push`, `14-pr`, `32-reclaim-scratch`, `50-geoblock`, `91-closing` and `92-selfcheck`.
   - **`05-refs.log` also carries, under a marker line, `main`'s first-parent commits above `7f7d7b1` with the paths each changed**, which §0.5 asks to be reported.
   - **`61-upload-wait.log`'s first line names the hand-over** (`hand-over 1 of B-UPLOAD's paste`) above its `date -u +%FT%TZ`.
4. **§3.6's wait block ran as a background command, not in the foreground.** The block was verbatim inside an outer loop of at most 40 runs, 40 × 540 s = 21,600 s, the TZ's bound. That way the session's turn could end and the Russian hand-over reach the Boss while the block waited. It appended to `61-upload-wait.log` as the TZ says. **Its third pass, at 08:04:48 UTC, printed `exit lines 0 of 1; runs begun 1; upload processes 0` beside an `exit=0` already in `60-upload.log`.** The block takes its count before its last 60 s sleep, and the run ended inside that sleep. The Executor ran the block once more, in the foreground, at 08:05:00 UTC, and it printed `exit lines 1 of 1; runs begun 1; upload processes 0`. B-UPLOAD ran once.
5. **142 refs at §0.5, where the Architect read 139.** The difference is three archive tags made since his read (§0): one of them is the pair book's archive's off-calendar run of 2026-11-12 22:10:01 UTC, which ended `status=75/TEMPFAIL` and is on `origin` as `pairbook-streams-1794521401`; the other two are the reward book archive's off-calendar run at 22:30:01 and its calendar run of 01:30:20. Both off-calendar runs followed `crypto-deploy.service`'s eleven reloads of systemd at 21:59:57 to 22:00:01 UTC. This is recorded, not BLOCKING, as §0.5 says.
6. **No file of replies was withheld**, where §1 said the files withheld "should be few". 0 is the store's count, printed. TZ-43's 5 polls not served are not, by this run, files of replies carrying another body. The rule that withholds is proved by the self-test's synthetic file alone (its checks, `logs/20-selftest.log`).
7. **Two of the four earlier directories that B-RECLAIM-SCRATCH removed are named by no report:** `d4894963-361e-43df-9b59-1207e3b15362` and `50181f4d-39a8-5455-ad6a-3aaa95edd48a`. They were born at 07:30:59 and 07:31:00 UTC on 2026-11-13, a minute before this session's process, and no running `claude` process made them. `scratch`'s rule named them earlier, and the TZ makes the rule alone decide.
8. **The classifier refused nothing this run** — not B-RECLAIM-SCRATCH's `reclaim`, which it refused to TZ-38 through TZ-43, and not B-RECLAIM-OWN's lines. The Executor tried B-RECLAIM-SCRATCH once, as §3 says, and it ran through. V19 has no block to report.
9. **V2's seven checks at §0.3, and five at §3.9, were read by the Executor from the logs against the TZ's literal conditions.** The host gate is shell commands, and no instrument asserts it.
10. **Reads no step names**, none under a forbidden root and none printing a member's content:
    - `git status --porcelain --ignored`, `git config` and `git log` of the worktree and the checkout, before the commit.
    - `gh pr view 43` and `ls .github`, to follow the last pull request's form. No template exists.
    - `grep`, `awk`, `sed`, `join`, `diff`, `stat` and `sha256sum` over this TZ's own logs and files, to build §0's, §2's and §5's tables. They printed only names, counts, bytes, instants and hashes, to the session and to no file.
    - `date -u -d @<A>` of the archive tags' names.
    - After §9: `sha256sum` of the 45 copies and `du -sb /root/btc-forensics`, the check §9 names for a paste.
11. **`I verify` stands in for contract §5.1's `curl`,** and the paste's `exit=` line for the Boss's confirmation, as TZ-44 §10 C8 states.
12. **B-RECLAIM-OWN ran in four calls of the session** — `reclaim`, `worktree remove`, `rm -rf`, and the closing reads — and not as one chain, each line as §9 writes it.
13. **The commit's author is `root <root@vultr.guest>`, the host's git default**, as for TZ-40 to TZ-43. The commit message and the pull request's text are the Executor's own.
14. **The report was drafted after §3.9 and before B-RECLAIM-OWN, and its §9, this section and two corrections were written after it.** The corrections were §0's count of `13-push.log`'s ref lines, first drafted as 139 and corrected to the 142 that log holds, and §2.7's last peak. The commit of this report, its push and any read after them are not in it.
