# TZ-09 — Disk inventory, bounded reclamation and the retention rule

**Canonical filename: `CryptoTZ/TZ-09-disk-inventory.md`.** Report:
`CryptoReports/TZ-09-disk-inventory-report.md`. Branch: `tz-09-disk-inventory`.
**Model: Opus.** This TZ deletes files on the host the live capture runs on; it is in the
data-loss class.

---

## 0. Gates — compare before any work

**System Map revision required:** `2026-09-13-c`.

| anchor | required |
|---|---|
| `A1` — observation set | `229a944f2d51` |
| `A2` — collector | `6c5089330629` |
| `A3` — phase | `0-complete / 1-answered-no / 2-not-started` |
| `A4` — executor contract | `437b45ea196b` |
| `A5` — recorder | `9fd1c7de0f74` |
| `A6` — pricer | `cb72abb8dd8a` |

**Host gate — all three, or this is not the capture host and the run is BLOCKED.** Derived from
System Map §6.

1. `/var/lib/btc-recorder/` exists and holds interval directories.
2. The recorder process is running and the newest `runtime.jsonl` start record carries sha
   `4216c04673ced76b5b2ac60ef57c9abedc46f9b9`.
3. The filesystem holding it is `/dev/vda2`, total `31,612,203,008` bytes.

**Resource gate, exact bytes, derived from System Map §6.**

- Free space at run start below `2,000,000,000` bytes → **BLOCKED** before any work.
- Free space below `3,000,000,000` bytes at any read during the run → stop immediately, write the
  report with everything measured so far, mark it **BLOCKED**, delete nothing. `3,000,000,000` is
  the `2,000,000,000` floor plus one day at the 1.00 GB/day drain §6 measures.

Mismatch on any gate → BLOCKED, and no measurement, copy or deletion is performed.

---

## 1. Why this exists

System Map §6 measures the filesystem filling at 0.84 to 1.00 GB/day while the recorder writes
`23,850,461` bytes/day. About `815,000,000` bytes/day is written by something that has never been
identified, and the floor is 4.6 to 5.7 days away. The capture is the unread input to Phase 2 and
cannot be re-created.

This TZ names the consumer in exact bytes, reclaims only this project's own re-derivable scratch,
and fixes the retention rule. **It installs nothing.**

---

## 2. Scope — what this TZ must not do

- **No file under `/var/lib/btc-recorder/**` is moved, compressed, truncated, rewritten or
  deleted.** Read-only enumeration of that tree — `du`, `df`, `stat`, `ls`, `find`, and reading
  `runtime.jsonl` — is **exempt from this prohibition and is required by M5 and V7**. M6 copies
  twenty interval directories out of it and touches neither the originals nor their mtimes.
- **Nothing outside the §4 allow-list is deleted, moved or truncated.** In particular nothing under
  `/var/log`, `/var/www`, `/var/lib`, `/home`, `/srv`, `/opt`, `/etc`, `/usr`, and nothing
  belonging to `crypto-auto`, `my_real_estate_bot` or `seahome_webapp.git`. This holds even where a
  measurement names one of them as the consumer: naming it is this TZ's whole job, and acting on it
  is the next TZ's.
- **`/root/tz04a-env/` is the interpreter the running recorder is executing from.** It is not
  scratch. It is not touched under any circumstance.
- **No process is signalled, stopped, restarted or reniced.** `kill` is refused by the sandbox in
  any form; if something must be stopped, the report hands the Boss two exact commands and verifies
  the outcome from `ps` and the log rather than from his report.
- **No systemd unit, timer, cron entry, logrotate rule or other scheduled job is created, edited or
  enabled.** Automation is out of scope by decision: an automatic deleter on a shared production
  host is written only after the consumer has a name, and then in its own TZ.
- No package is installed, no configuration file is edited, nothing in `research/recorder/**` is
  changed, no model statistic is computed and the pricer is not read.

---

## 3. Measurement

All sizes in exact bytes. Every reading carries a UTC timestamp to the second.

**M1 — baseline.** `df -B1` for `/dev/vda2`: total, used, available. Inodes total and used.

**M2 — size inventory.** `du -x -B1 --max-depth=1 /`, then `--max-depth=2` for `/var`, `/root`,
`/home`, `/srv`, `/opt`, `/usr`, `/tmp`. Report every directory at or above `100,000,000` bytes,
descending. For the three largest subtrees that are not this project's, drill to `--max-depth=3`.

**M3 — rate inventory. This is the deciding measurement.** Run the whole M2 command set twice,
the two runs separated by **not less than `3,600` seconds of wall clock**. Report per directory:
bytes at `t0`, bytes at `t1`, the delta, and the delta scaled to bytes/day. Sort by delta,
descending. Report `df` available at both instants and its fall.

**A directory is named the consumer when its delta alone exceeds half the fall in `df` available
over the same window.** If none does, the report says the consumer is not identified and gives the
five largest deltas.

**M4 — space held by unlinked open files.** Compare `df` used against the M2 total for `/`. If they
differ by more than `100,000,000` bytes, enumerate the deleted-but-open files from `/proc/*/fd`,
each with pid, process name and size in exact bytes, and report the total. **Nothing is killed.**

**M5 — capture accounting.** `du -x -B1 --max-depth=2 /var/lib/btc-recorder/`; the interval
directory count; the count holding a `quotes.jsonl.gz`; and the tree's own growth over the M3
window, scaled to bytes/day and compared against §6's `23,850,461`. State the difference.

**M6 — compressibility, for the retention decision only.** Copy the **twenty oldest** interval
directories to `/root/tz09-work/sample/`, archive that copy with `tar` plus `zstd -19` (or `xz -9`
if `zstd` is absent), report exact bytes before and after and the ratio, then delete the copy and
the archive. Project the saving over the whole capture at that ratio, in exact bytes.
**This authorizes no archiving.**

**M7 — log accounting, read-only.** `journalctl --disk-usage` if `systemd-journald` is present;
`/var/log` at `--max-depth=2`; the ten largest individual files under `/var/log` with exact bytes
and mtimes. Nothing there is deleted, rotated or vacuumed.

---

## 4. Reclamation — the allow-list, and nothing else

**These five paths are the only deletion candidates that exist for this TZ:**

- `/root/tz01-out-archive/`
- `/root/tz06-work/`
- `/root/tz07-work/`
- `/root/tz07b-work/`
- `/root/tz08a-work/`

In this order, and the order is part of the specification.

**R1 — enumerate.** Every regular file in the five trees, with exact size and SHA-256. Report the
count and the total bytes per tree.

**R2 — preservation by hash.** For each file, search `SYSTEM-MAP.md` and every file in
`CryptoReports/` on `main` for that file's SHA-256. **Any hit preserves the file**, and the report
names the artifact that holds the hash. Preserved unconditionally, hash search or not:
`/root/tz06-work/tz06-observations.csv` and `/root/tz08a-work/tz08a-observations.csv`.

**R3 — consolidate.** Create `/root/btc-forensics/` and copy every preserved file into it as
`<source-directory-name>--<filename>`. Recompute SHA-256 at the destination and assert equality
with the source. **One mismatch → BLOCKED, and nothing is deleted.**

**R4 — delete.** Only once every R3 assertion has held. One command per absolute path, five
commands, each preceded by that tree's exact byte total and followed by a fresh `df` read.

**R5 — account for it.** Free space immediately before R4 and immediately after, in exact bytes,
and the difference. Assert the difference is not negative.

**No committed script deletes anything.** `research/tz09-disk-inventory.py` measures and prints;
R3 and R4 are shell commands the Executor runs, and the report quotes each verbatim with its
output.

---

## 5. The retention rule — fixed here

1. **The capture is never deleted.** No interval directory under `/var/lib/btc-recorder/` is
   removed, truncated or rewritten, by any TZ, any script or any scheduled job. Every committed
   measurement's units stay re-derivable, and Tier C is the unread input to Phase 2.
2. **Archiving, if it is ever done, is its own TZ and is reversible.** It may only compress
   intervals older than the oldest member of any set a committed report scores; it verifies the
   archive by extracting and comparing the SHA-256 of every member file **before** any original is
   removed; and it states the byte saving M6 measured.
3. **Scratch retention.** A TZ's `/root/tz<NN>-work/` tree is reclaimed by the next TZ that runs
   after that TZ's report is on `main`, except for files whose SHA-256 a committed artifact names,
   which live in `/root/btc-forensics/`. Standing rule from here on: **every TZ that writes scratch
   outside the repository states in its own report which of its outputs a committed artifact names
   by hash; everything else is reclaimable the moment the report is committed.**
4. **The floor and the alarm, in exact bytes.** Hard floor `F = 2,000,000,000` bytes free: below
   it no TZ runs. Alarm level `A = F + 3 × D`, where `D` is the total drain in bytes/day that M3
   measures. The report states `D` and `A` in exact bytes, states free space against `A`, and gives
   the days to `F` at `D`. Three days is the interval one TZ cycle takes; it is not a round number
   chosen for its shape.

---

## 6. The change authorized — exactly two paths

- `research/tz09-disk-inventory.py` — new. Branch plus PR.
- `CryptoReports/TZ-09-disk-inventory-report.md` — straight to `main`.

`git diff --name-only $(git merge-base HEAD origin/main) HEAD` on the branch lists the first and
nothing else. Any other repository path touched → BLOCKED.

---

## 7. Validation

Each check states its count and whether it is asserted in code or read in the shell.

- **V1 — gates.** The three host checks and the resource gate, with observed values.
- **V2 — the committed script cannot delete.** Its source contains none of `os.remove`,
  `os.unlink`, `os.rmdir`, `shutil.rmtree`, `shutil.move`, `os.truncate`, `os.rename`; and every
  `open(..., "w")` in it targets a path under `/root/tz09-work/`. Quote the grep and its output
  verbatim.
- **V3 — inventory stability.** M2 re-run immediately: the ordering of every directory above
  `100,000,000` bytes is unchanged. Report both orderings.
- **V4 — window.** Both M3 timestamps and their difference in seconds; not less than `3,600`.
- **V5 — accounting closure.** `(fall in df available) − (sum of directory deltas) − (change in
  unlinked-open bytes)`, in exact bytes. No threshold; the residual is reported and, if it exceeds
  `100,000,000` bytes, the report says so and does not explain it away.
- **V6 — preservation.** Count of preserved files; source SHA-256 equals destination SHA-256 on
  every one. **Any inequality is BLOCKED and nothing is deleted.**
- **V7 — the capture is untouched.** Interval directory count and the recorder's pid, read
  immediately before R4 and immediately after: the pid is unchanged and the count has not fallen.
- **V8 — the recorder survived.** At run end: same pid, same start-record sha, and the newest
  interval directory's `T0` is greater than at run start.
- **V9 — fingerprint table.** Line counts and SHA-256 for `SYSTEM-MAP.md` and every file its
  fingerprint table lists, read at run start from `origin/main`.
- **V10 — free space, exact bytes**, at: run start, M3 `t0`, M3 `t1`, immediately before R4,
  immediately after R4, and run end.

---

## 8. The report

Section order is §3, §4, §5, §7, then publication. **The first paragraph states, in this order:**
the consumer named with its bytes/day, or "not identified" with the five largest deltas; free space
at run end; `D`; `A`; and the days to `F` at `D`. Everything else follows.

Where a measurement contradicts a System Map row, the report says which row and by how much. It
proposes no repair: the Architect writes those.

---

## 9. Publication

Branch `tz-09-disk-inventory`, pushed, pull request opened and left unmerged. The report goes
straight to `main`. Only the Boss merges, after the Architect's verdict. No Release.
