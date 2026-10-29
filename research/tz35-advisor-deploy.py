#!/usr/bin/env python3
# tz35-advisor-deploy.py - TZ-35's checker: the fingerprint, the host gate, the number, the scratch and reclaim of
# earlier trees, and every reading of the deployment proof of adv3-bot.service (TZ-35 section 4). Standard library
# only. It starts, stops and signals no unit and no process, sends no request, and never prints the bot's token or a
# chat id. Exits: 0 every assert held; 1 a failed assert, named; 3 NOT YET.
import datetime as dt, hashlib, json, os, re, shutil, stat, subprocess, sys, time

PRIMARY = '/root/btc-5m-twap'
WORK = '/root/tz35-work'
WT = WORK + '/wt'
STATE = WORK + '/state.json'
REPORTS = PRIMARY + '/CryptoReports'
FORENSICS = '/root/btc-forensics'
SVC = '/root/adv3-bot-svc'
ROOT = '/var/lib/adv3-bot'
UNIT = 'adv3-bot.service'
UNIT_FILE = '/etc/systemd/system/adv3-bot.service'
ETC = '/etc/adv3-bot'
TOKEN_FILE = ETC + '/token'
CHAT_FILE = ETC + '/chat-id'
PY = '/root/tz04a-env/venv/bin/python'
ARGV = [PY, '-B', '-u', SVC + '/adv3-bot.py', '--serve']
BRANCH = 'tz-35-advisor-bot'
NUMBER = 'TZ-35-'
TZ_FILE = 'CryptoTZ/TZ-35-advisor-bot.md'
CAPTURE = ('btc-recorder.service', 'btc-pairbook.service', 'btc-rewardbook.service')
ARCHIVE = 'btc-pairbook-archive.service'
LEDGER = '/var/lib/btc-pairbook-archive/ledger.jsonl'
DEFERRED_RUN = 1793260762      # the pair book's archive's set deferred on 2026-10-29 (map section 7 item 128)
RECORDER = '/var/lib/btc-recorder'
REVISION = '2026-10-29-a'
ANCHORS = {'A1': '229a944f2d51', 'A2': '6c5089330629',
           'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable',
           'A4': '437b45ea196b', 'A5': '0f6c90451cbd', 'A6': '729f0bcdbee3'}
DERIVED = {'A2': 'research/twap-divergence.py', 'A4': 'BTC-EXECUTOR-INSTRUCTIONS.md',
           'A5': 'research/recorder/recorder.py', 'A6': 'research/pfair.py'}
ROWS, FROZEN, TRACKED, REPORTED = 49, 46, 2, 1
# TZ-35 Appendix A: the files the service copy and the installed unit must equal
SHA = {'advisor/adv3.py': '7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb',
       'advisor/adv3-bot.py': 'e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb',
       'deploy/systemd/adv3-bot.service': '82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66'}
RULE = 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169'
HOST_SHA = 'e3975b5da44c5328adf3bf3914634cd878842c73'
VDA_SIZE = 31612203008
MEM_FLOOR = 170344448          # twice the largest peak of any mode this TZ runs, adv3.py --history's 85,172,224
DISK_FLOOR = 7400000000        # the reward book's STREAM_FLOOR, 7,300,000,000, and this TZ's 100,000,000
LOAD_MAX = 0.05
LOAD_MIN_S = 300
RESTART_MAX_S = 60
DAILY_WAIT_S = 420              # a first attempt, its one retry 300 s later, and the fetch
RUN_WAIT_S = 1200              # the archive timer's OnActiveSec=600 after a reload, and 600 s for a hand-over
STILL_DEADLINE_S = 4200
TOKEN_RE = re.compile(r'[0-9]{5,16}:[A-Za-z0-9_-]{30,64}')
UUID = re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
HASHTOKEN = re.compile(r'[0-9a-f]{16,64}')
LIVE_S = 60
LOG_RE = re.compile(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})Z (.*)')


class NotYet(Exception):
    pass


def out(*parts):
    print(*parts, flush=True)


def sh(args):
    cp = subprocess.run(args, capture_output=True, text=True)
    return cp.returncode, cp.stdout, cp.stderr


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for block in iter(lambda: fh.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def utc(t):
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ')


def show(unit, *props):
    rc, so, se = sh(['systemctl', 'show', unit] + [x for p in props for x in ('-p', p)])
    assert rc == 0, f'systemctl show {unit}: {se.strip()}'
    return dict(line.split('=', 1) for line in so.splitlines() if '=' in line)


def load_state():
    if not os.path.exists(STATE):
        return {}
    with open(STATE, encoding='utf-8') as fh:
        return json.load(fh)


def save_state(state):
    tmp = STATE + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(state, fh, indent=1, sort_keys=True)
        fh.write('\n')
    os.replace(tmp, STATE)


def verdict(name, checks):
    for k, v in checks.items():
        out(f'{name} {k:<64} {"PASS" if v else "FAIL"}')
    bad = [k for k, v in checks.items() if not v]
    out(f'READING {name}: {"PASS" if not bad else "FAIL"} - {len(checks) - len(bad)} of {len(checks)}')
    assert not bad, f'{name} FAIL: {bad}'


# ---- /proc ---------------------------------------------------------------------------------------------------

def proc_argv(pid):
    try:
        with open(f'/proc/{pid}/cmdline', 'rb') as fh:
            parts = fh.read().split(b'\0')
    except OSError:
        return None
    return [p.decode('utf-8', 'replace') for p in parts[:-1]] if parts and parts[-1] == b'' else None


def procs(argv):
    return sorted(int(p) for p in os.listdir('/proc') if p.isdigit() and proc_argv(p) == argv)


def _btime():
    with open('/proc/stat', encoding='utf-8') as fh:
        return int([ln for ln in fh.read().split('\n') if ln.startswith('btime ')][0].split()[1])


def _stat_fields(pid):
    with open(f'/proc/{pid}/stat', encoding='utf-8') as fh:
        return fh.read().rsplit(')', 1)[1].split()


def proc_start(pid):
    return _btime() + int(_stat_fields(pid)[19]) / os.sysconf('SC_CLK_TCK')


def proc_cpu(pid):
    f = _stat_fields(pid)
    return (int(f[11]) + int(f[12])) / os.sysconf('SC_CLK_TCK')


def proc_status(pid):
    with open(f'/proc/{pid}/status', encoding='utf-8') as fh:
        return dict(line.split(':', 1) for line in fh.read().splitlines() if ':' in line)


def claude_starts():
    found = []
    for pid in sorted((p for p in os.listdir('/proc') if p.isdigit()), key=int):
        argv = proc_argv(pid)
        if not argv:
            continue
        try:
            start = proc_start(pid)
        except OSError:
            continue
        if argv[0] == 'claude' or argv[0].endswith('/claude.exe'):
            found.append((int(pid), start, argv[0]))
    return found


# ---- pure readings: each takes what the modes read and returns its checks ----------------------------------------

def parse_map(text):
    """(revision, anchors, rows) from SYSTEM-MAP.md's section 0; a row is (path, lines, bytes, state, sha256)."""
    head = text[:text.index('### Fingerprint table')]
    m = re.search(r'\*\*Revision string:\*\* `([^`]+)`', head)
    anchors = dict(re.findall(r'^\| `(A\d)` — [^|\n]+\| `([^`\n]+)` \|$', head, re.M))
    sec = text[text.index('### Fingerprint table'):]
    sec = sec[:sec.index('\n\nHashes are of the file')]
    rows = []
    for path, lines, size, state, sha in re.findall(
            r'^\| `([^`]+)` \| ([^|\n]+) \| ([^|\n]+) \| (frozen|tracked|reported) \| ([^|\n]+) \|$', sec, re.M):
        num = lambda x: int(x.strip().replace(',', '')) if x.strip().replace(',', '').isdigit() else None
        rows.append((path, num(lines), num(size), state, sha.strip().strip('`')))
    return (m.group(1) if m else None), anchors, rows


def log_lines(text):
    """[(UTC second as an epoch, message)] of service.log's own lines; traceback lines belong to the line above."""
    got = []
    for line in text.splitlines():
        m = LOG_RE.fullmatch(line)
        if m:
            t = dt.datetime.strptime(m.group(1), '%Y-%m-%dT%H:%M:%S').replace(tzinfo=dt.timezone.utc).timestamp()
            got.append((int(t), m.group(2)))
    return got


def journal_records(text):
    """Every journal line parsed; a torn last line - a kill mid-write - is counted and left out."""
    lines = text.split('\n')
    recs, torn = [], 0
    for k, line in enumerate(lines):
        if not line:
            continue
        try:
            recs.append(json.loads(line))
        except ValueError:
            assert k == len(lines) - 1, f'journal line {k + 1} does not parse'
            torn += 1
    return recs, torn


def daily_checks(log, recs, pid, t0, today):
    """G-DAILY and G-REPLY: the first process's start, its daily for the close of the day before, and its answer."""
    d1 = str(today - dt.timedelta(days=1))
    after = [x for t, x in log if t >= int(t0) - 1]
    dailies = [r for r in recs if r.get('kind') == 'daily']
    r = dailies[0] if len(dailies) == 1 else {}
    g = {
        'the service logged its start under the unit MainPID': sum(
            x.startswith(f'serving the pinned chat: pid {pid} ') for x in after) == 1,
        'its candles refreshed to the close of the day before, 42 of 42 served': (
            f'candles refreshed to the close of {d1} | missing -' in after),
        'its daily sent once, for the close of the day before': after.count(f'daily sent for the close of {d1}') == 1,
        'exactly one daily record, made today': len(dailies) == 1 and str(r.get('utc', ''))[:10] == str(today),
        'the record: the close of the day before, rule ADV-3': r.get('close_of') == d1 and r.get('rule') == RULE,
        'the record: 10,000 USDT, 0.5% a trade': r.get('deposit') == 10000.0 and r.get('risk_pct') == 0.5,
        'the record: Telegram message ids': bool(r.get('message_ids')) and all(
            isinstance(x, int) for x in r.get('message_ids', [])),
        'the record: 42 signals, at most 3 cards, STRONG among TOP-3': len(r.get('signals', {})) == 42 and len(
            r.get('cards', [])) == len(r.get('top', [])) <= 3 and set(r.get('strong', [])) <= set(r.get('top', [])),
    }
    reply = {'the service answered the pinned chat': any(
        x == 'help sent' or x.startswith('request answered for the close of') for x in after)}
    return g, reply


def restart_checks(log, recs, old_pid, new_pid, new_start, t_kill, nrestarts, active, today):
    """G-RESTART and G-ONCE: a new process, started by systemd after the kill, that sends no second daily."""
    after = [x for t, x in log if t >= int(t_kill)]
    g = {
        'a new MainPID': new_pid > 0 and new_pid != old_pid,
        'started after the kill and at most 60 s later': t_kill < new_start <= t_kill + RESTART_MAX_S,
        'NRestarts 1': nrestarts == '1',
        'active and running': active,
        'the new process logged its start, the daily read as sent today': any(
            x.startswith(f'serving the pinned chat: pid {new_pid} ') and x.endswith(f'daily-sent {today}')
            for x in after),
    }
    once = {
        'still exactly one daily record for today': sum(
            1 for r in recs if r.get('kind') == 'daily' and str(r.get('utc', ''))[:10] == str(today)) == 1,
        'no daily sent after the kill': not any(x.startswith('daily sent') for x in after),
    }
    return g, once


def still_checks(before, after, ledger_before, ledger_after):
    """G-STILL: the recorder and the reward book untouched; the pair book moved by the archive's own restarts alone."""
    g = {}
    for u in ('btc-recorder.service', 'btc-rewardbook.service'):
        b, a = before[u], after[u]
        g[f'{u} kept MainPID, NRestarts and active'] = (a['MainPID'] == b['MainPID'] and a['NRestarts'] == b['NRestarts']
                                                        and a['ActiveState'] == 'active')
    b, a = before['btc-pairbook.service'], after['btc-pairbook.service']
    dn, dl = int(a['NRestarts']) - int(b['NRestarts']), ledger_after - ledger_before
    g['btc-pairbook.service active, restarted only by the archive'] = (
        a['ActiveState'] == 'active' and dn == dl >= 0 and (dn > 0 or a['MainPID'] == b['MainPID']))
    return g


def live_or_earlier(birth, starts):
    """The running claude processes whose start lies within 1 s before to 60 s after a directory's birth."""
    return [pid for pid, s, _a in starts if s - 1 <= birth <= s + LIVE_S]


def reclaimable(tree):
    if tree == WORK:
        return True
    return (tree.startswith('/tmp/') and os.path.isdir(tree) and not os.path.islink(tree)
            and UUID.fullmatch(os.path.basename(tree)) is not None
            and 'btc-5m-twap' in os.path.basename(os.path.dirname(tree)))


def by_name(tree, rel):
    """Kept whatever a report prints: the state, the logs and the history."""
    return tree == WORK and (rel == 'state.json' or rel.startswith('logs/') or rel == 'history.json')


def number_reading(names):
    """NUMBER, map section 7 item 127's repair: CryptoTZ/ holds this TZ's file and no other file of its number, and
    CryptoReports/ no report of that number, so a number used twice stops both specifications before any work."""
    return {'CryptoTZ/ holds TZ-35-advisor-bot.md and no other TZ-35- file': [
                n for n in names if n.startswith('CryptoTZ/' + NUMBER)] == [TZ_FILE],
            'CryptoReports/ holds no TZ-35- report': not any(n.startswith('CryptoReports/' + NUMBER) for n in names)}


def ledger_events(text, run):
    """One run's records in the pair book's archive's ledger text, as (event, deferral count, UTC), and the count of
    lines that do not parse - a run may be writing its last one."""
    got, bad = [], 0
    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except ValueError:
            bad += 1
            continue
        if r.get('run') == run:
            got.append((r.get('event'), r.get('count'), utc(int(r.get('wall_ns') or 0) / 1e9)))
    return got, bad


# ---- the modes -------------------------------------------------------------------------------------------------

def mode_fingerprint():
    with open(PRIMARY + '/SYSTEM-MAP.md', 'rb') as fh:
        raw = fh.read()
    rev, anchors, rows = parse_map(raw.decode('utf-8'))
    out('map', raw.count(b'\n'), 'lines', len(raw), 'bytes, SHA-256', sha256_bytes(raw), '- revision', rev)
    assert rev == REVISION, f'revision {rev!r}'
    assert anchors == ANCHORS, f'anchors {anchors!r}'
    for k, rel in DERIVED.items():
        got = sha256_file(os.path.join(PRIMARY, rel))[:12]
        out(f'anchor {k} {rel} {got}')
        assert got == ANCHORS[k], f'anchor {k}'
    counts = {'frozen': 0, 'tracked': 0, 'reported': 0}
    for path, lines, size, state, sha in rows:
        with open(os.path.join(PRIMARY, path), 'rb') as fh:
            data = fh.read()
        got = (data.count(b'\n'), len(data), sha256_bytes(data))
        counts[state] += 1
        if state == 'frozen':
            assert got == (lines, size, sha), f'frozen {path}: {got} against {(lines, size, sha)}'
        out(f'{state:<8} {path:<46} {got[0]:>6} {got[1]:>8} {got[2]}{"  equal" if state == "frozen" else ""}')
    assert len(rows) == ROWS and counts == {'frozen': FROZEN, 'tracked': TRACKED, 'reported': REPORTED}, counts
    out(f'FINGERPRINT PASS: revision {REVISION}; anchors 6 of 6, 4 re-derived; {len(rows)} rows, {FROZEN} of '
        f'{FROZEN} frozen equal, {TRACKED} tracked, {REPORTED} reported')


def mode_host():
    checks = {}
    rc, so, _ = sh(['find', RECORDER, '-mindepth', '1', '-maxdepth', '3', '-name', 'manifest.json', '-print', '-quit'])
    checks['H1 a recorder manifest exists'] = rc == 0 and len(so.split()) == 1
    rc, so, _ = sh(['df', '-B1', '--output=source,size,avail', RECORDER])
    f = so.splitlines()[1].split() if rc == 0 and len(so.splitlines()) > 1 else ['', '0', '0']
    avail = int(f[2])
    checks['H2 the filesystem is /dev/vda2 of 31,612,203,008 bytes'] = f[0] == '/dev/vda2' and int(f[1]) == VDA_SIZE
    rc, so, _ = sh(['grep', '-c', HOST_SHA, RECORDER + '/runtime.jsonl'])
    checks['H2 the recorder runtime names e3975b5'] = so.strip().isdigit() and int(so) >= 1
    rc, so, _ = sh([PY, '-c', 'import sys; print(sys.version.split()[0])'])
    checks['H3 /root/tz04a-env runs Python 3.12'] = rc == 0 and so.startswith('3.12.')
    units = {}
    for u in CAPTURE:
        units[u] = show(u, 'MainPID', 'NRestarts', 'ActiveState', 'UnitFileState')
        checks[f'H4 {u} active and enabled'] = (units[u]['ActiveState'] == 'active'
                                                 and units[u]['UnitFileState'] == 'enabled')
    rc, _, _ = sh(['systemctl', 'cat', UNIT])
    checks['H5 no adv3-bot unit, file, copy or root'] = rc != 0 and not any(
        os.path.lexists(p) for p in (UNIT_FILE, SVC, ROOT))
    checks['H5 no process under the service argv'] = procs(ARGV) == []
    ok = False
    try:
        se, st = os.lstat(ETC), os.lstat(TOKEN_FILE)
        if (stat.S_ISDIR(se.st_mode) and stat.S_IMODE(se.st_mode) == 0o700 and se.st_uid == 0 and stat.S_ISREG(st.st_mode)
                and stat.S_IMODE(st.st_mode) == 0o600 and st.st_uid == 0 and 0 < st.st_size <= 200):
            with open(TOKEN_FILE, encoding='ascii', errors='replace') as fh:
                body = fh.read()
            ok = body.endswith('\n') and body.count('\n') == 1 and TOKEN_RE.fullmatch(body[:-1]) is not None
    except OSError:
        ok = False
    checks['H6 /etc/adv3-bot 700 and its token 600, one line of a bot token'] = ok
    with open('/proc/meminfo', encoding='utf-8') as fh:
        mem = {k: int(v.split()[0]) * 1024 for k, v in (ln.split(':', 1) for ln in fh.read().splitlines())}
    checks['the memory gate: MemAvailable at least 170,344,448 bytes'] = mem['MemAvailable'] >= MEM_FLOOR
    checks['the disk gate: /dev/vda2 free at least 7,400,000,000 bytes'] = avail >= DISK_FLOOR
    ledger = ledger_restarts()
    out('printed: MemAvailable', mem['MemAvailable'], 'MemTotal', mem['MemTotal'], 'SwapFree', mem['SwapFree'],
        '| free bytes', avail, '| archive ledger restart records', ledger, '| chat-id present',
        os.path.exists(CHAT_FILE))
    for u in CAPTURE:
        out('printed:', u, ' '.join(f'{k}={v}' for k, v in sorted(units[u].items())))
    a = show(ARCHIVE, 'ActiveState', 'Result')
    out('printed:', ARCHIVE, ' '.join(f'{k}={v}' for k, v in sorted(a.items())))
    deferred_run()
    state = load_state()
    state['host'] = {'ns': time.time_ns(), 'units': units, 'ledger_restarts': ledger, 'free_bytes': avail,
                     'mem_available': mem['MemAvailable']}
    save_state(state)
    verdict('HOST', checks)


def ledger_restarts():
    with open(LEDGER, encoding='utf-8') as fh:
        return sum(1 for line in fh if '"event": "restart"' in line)


def deferred_run():
    """Printed, gating nothing: the deferred set's records in the pair book's archive's ledger (map section 7 item
    128) - event names, deferral counts and times alone."""
    with open(LEDGER, encoding='utf-8') as fh:
        held, torn = ledger_events(fh.read(), DEFERRED_RUN)
    out('printed: the archive ledger, run', DEFERRED_RUN, 'records', held, '| lines that do not parse', torn)


def mode_number():
    rc, so, se = sh(['git', '-C', PRIMARY, 'ls-tree', '--name-only', 'origin/main', '--', 'CryptoTZ/', 'CryptoReports/'])
    assert rc == 0, f'git ls-tree: {se.strip()}'
    names = so.splitlines()
    head = sh(['git', '-C', PRIMARY, 'rev-parse', 'origin/main'])[1].strip()
    out('printed: origin/main', head, '|', len(names), 'paths under CryptoTZ/ and CryptoReports/ | of the number',
        NUMBER, [n for n in names if n.split('/', 1)[-1].startswith(NUMBER)])
    verdict('NUMBER', number_reading(names))


def mode_scratch(own):
    parent = os.path.dirname(own)
    starts = claude_starts()
    for pid, t, a0 in starts:
        out('running %d started %s %s' % (pid, utc(t), a0))
    for name in sorted(os.listdir(parent)):
        path = os.path.join(parent, name)
        if path == own or not UUID.fullmatch(name) or not os.path.isdir(path):
            continue
        rc, so, se = sh(['stat', '-c', '%W', path])
        assert rc == 0, se
        owner = live_or_earlier(int(so.strip()), starts)
        out('%s born %s: %s' % (name, utc(int(so.strip())), ('live, process %s' % owner) if owner else 'earlier'))


def mode_reclaim(trees):
    assert trees and all(reclaimable(t) for t in trees), 'reclaim: %r' % (trees,)
    starts = claude_starts()
    for t in trees:
        if t != WORK:
            rc, so, se = sh(['stat', '-c', '%W', t])
            assert rc == 0 and not live_or_earlier(int(so.strip()), starts), 'reclaim: %s belongs to a running process' % t
    tokens = set()
    for name in sorted(os.listdir(REPORTS)):
        if name.endswith('.md'):
            with open(os.path.join(REPORTS, name), encoding='utf-8', errors='replace') as fh:
                tokens.update(HASHTOKEN.findall(fh.read()))
    lengths = sorted({len(t) for t in tokens})
    before = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    out('reclaim: %d report tokens; forensic store holds %d files' % (len(tokens), before))
    considered = named = kept = copied = held = 0
    for tree in trees:
        if tree == WORK and os.path.isdir(WT):
            rc, so, _ = sh(['git', '-C', WT, 'status', '--porcelain', '--ignored'])
            assert rc == 0 and so == '', 'reclaim: %s holds %r' % (WT, so[:400])
            head = sh(['git', '-C', WT, 'rev-parse', 'HEAD'])[1].strip()
            up = sh(['git', '-C', WT, 'rev-parse', '@{u}'])[1].strip()
            assert head and up == head, 'reclaim: %s at %s, upstream %r' % (WT, head, up)
            out('reclaim: %s skipped: no file but its HEAD\'s, and HEAD %s is its upstream\'s' % (WT, head))
        for dirpath, dirnames, filenames in os.walk(tree):
            dirnames[:] = sorted(d for d in dirnames if os.path.join(dirpath, d) != WT)
            for name in sorted(filenames):
                path = os.path.join(dirpath, name)
                if os.path.islink(path) or not os.path.isfile(path):
                    continue
                considered += 1
                rel = os.path.relpath(path, tree)
                h = sha256_file(path)
                is_named = any(h[:k] in tokens for k in lengths)
                is_kept = by_name(tree, rel)
                if not (is_named or is_kept):
                    continue
                named += 1 if is_named else 0
                kept += 1 if is_kept and not is_named else 0
                dest = os.path.join(FORENSICS, os.path.basename(tree) + '--' + rel.replace('/', '--'))
                if os.path.exists(dest):
                    assert sha256_file(dest) == h, 'reclaim: %s exists with another hash' % dest
                    held += 1
                    out('R held   %s %s' % (h, dest))
                    continue
                with open(path, 'rb') as src, open(dest, 'xb') as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                assert sha256_file(dest) == h, 'reclaim: %s did not copy whole' % dest
                copied += 1
                out('R copied %s %s' % (h, dest))
    after = sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    assert after == before + copied, 'reclaim: store %d, expected %d' % (after, before + copied)
    out('RECLAIM PASS: %d files considered, %d named by a report, %d kept by name, %d copied, %d already held; '
        'forensic store %d -> %d files' % (considered, named, kept, copied, held, before, after))


def mode_mark(name):
    state = load_state()
    rec = {'ns': time.time_ns(), 'mono_ns': time.monotonic_ns()}
    if sh(['systemctl', 'cat', UNIT])[0] == 0:
        rec['unit'] = show(UNIT, 'MainPID', 'NRestarts', 'ActiveState')
    state.setdefault('marks', {})
    assert name not in state['marks'], f'mark {name} taken already'
    state['marks'][name] = rec
    save_state(state)
    out('mark', name, utc(rec['ns'] / 1e9), json.dumps(rec.get('unit', {}), sort_keys=True))


def mode_copy():
    names = sorted(os.listdir(SVC))
    head = sh(['git', '-C', WT, 'rev-parse', 'HEAD'])[1].strip()
    branch = sh(['git', '-C', WT, 'rev-parse', 'origin/' + BRANCH])[1].strip()
    with open(SVC + '/commit.txt', encoding='ascii') as fh:
        commit = fh.read()
    checks = {
        'the copy holds adv3.py, adv3-bot.py and commit.txt alone': names == ['adv3-bot.py', 'adv3.py', 'commit.txt'],
        'adv3.py equal to Appendix A': sha256_file(SVC + '/adv3.py') == SHA['advisor/adv3.py'],
        'adv3-bot.py equal to Appendix A': sha256_file(SVC + '/adv3-bot.py') == SHA['advisor/adv3-bot.py'],
        'commit.txt the branch head, 40 hex and a newline': re.fullmatch(r'[0-9a-f]{40}\n', commit) is not None
                                                           and commit[:-1] == head == branch,
    }
    verdict('COPY', checks)


def mode_props():
    """PROPS: the installed unit's own settings as systemd reads them, before it is started."""
    p = show(UNIT, 'LoadState', 'ActiveState', 'UnitFileState', 'FragmentPath', 'MemoryMax', 'Nice', 'ProtectSystem',
             'NoNewPrivileges', 'PrivateTmp', 'Restart', 'ReadWritePaths', 'RestartPreventExitStatus', 'RestartUSec')
    out('printed:', ' '.join(f'{k}={v}' for k, v in sorted(p.items())))
    checks = {
        'LoadState loaded': p.get('LoadState') == 'loaded',
        'ActiveState inactive': p.get('ActiveState') == 'inactive',
        'UnitFileState disabled': p.get('UnitFileState') == 'disabled',
        'FragmentPath /etc/systemd/system/adv3-bot.service': p.get('FragmentPath') == UNIT_FILE,
        'MemoryMax 134217728': p.get('MemoryMax') == '134217728',
        'Nice 10': p.get('Nice') == '10',
        'ProtectSystem strict': p.get('ProtectSystem') == 'strict',
        'NoNewPrivileges yes': p.get('NoNewPrivileges') == 'yes',
        'PrivateTmp yes': p.get('PrivateTmp') == 'yes',
        'Restart always': p.get('Restart') == 'always',
        'ReadWritePaths /var/lib/adv3-bot': p.get('ReadWritePaths') == ROOT,
    }
    verdict('PROPS', checks)


def mode_unit(n):
    p = show(UNIT, 'Id', 'ActiveState', 'SubState', 'UnitFileState', 'FragmentPath', 'ControlGroup', 'MemoryMax',
             'Nice', 'NRestarts', 'MainPID', 'ProtectSystem', 'NoNewPrivileges', 'Restart', 'ReadWritePaths',
             'RestartPreventExitStatus', 'RestartUSec')
    out('printed:', ' '.join(f'{k}={v}' for k, v in sorted(p.items())))
    pid = int(p.get('MainPID') or 0)
    argv = proc_argv(pid) if pid else None
    try:
        cwd = os.readlink(f'/proc/{pid}/cwd')
        with open(f'/proc/{pid}/cgroup', encoding='utf-8') as fh:
            cg = fh.read()
        nnp = proc_status(pid).get('NoNewPrivs', '').strip()
    except OSError:
        cwd, cg, nnp = None, '', ''
    checks = {
        'ActiveState active': p.get('ActiveState') == 'active',
        'SubState running': p.get('SubState') == 'running',
        'UnitFileState enabled': p.get('UnitFileState') == 'enabled',
        'FragmentPath /etc/systemd/system/adv3-bot.service': p.get('FragmentPath') == UNIT_FILE,
        'ControlGroup /system.slice/adv3-bot.service': p.get('ControlGroup') == '/system.slice/adv3-bot.service',
        'MemoryMax 134217728': p.get('MemoryMax') == '134217728',
        'Nice 10': p.get('Nice') == '10',
        f'NRestarts {n}': p.get('NRestarts') == str(n),
        'ProtectSystem strict': p.get('ProtectSystem') == 'strict',
        'NoNewPrivileges yes': p.get('NoNewPrivileges') == 'yes',
        'Restart always': p.get('Restart') == 'always',
        'ReadWritePaths /var/lib/adv3-bot': p.get('ReadWritePaths') == ROOT,
        'the MainPID runs the exact argv': argv == ARGV,
        'its cwd /root/adv3-bot-svc': cwd == SVC,
        'its cgroup the unit, outside every user slice': '/system.slice/adv3-bot.service' in cg and '/user.slice' not in cg,
        'its NoNewPrivs 1': nnp == '1',
        'the MainPID the only process under the argv': procs(ARGV) == [pid],
        'the installed unit equal to Appendix A': sha256_file(UNIT_FILE) == SHA['deploy/systemd/adv3-bot.service'],
    }
    verdict(f'G-UNIT-{n}', checks)


def mode_daily():
    state = load_state()
    t0 = state['marks']['start']['ns'] / 1e9
    pid = int(show(UNIT, 'MainPID')['MainPID'])
    with open(ROOT + '/service.log', encoding='utf-8', errors='replace') as fh:
        log = log_lines(fh.read())
    path = ROOT + '/journal.jsonl'
    text = open(path, encoding='utf-8').read() if os.path.exists(path) else ''
    recs, torn = journal_records(text)
    today = dt.datetime.now(dt.timezone.utc).date()
    after = [x for t, x in log if t >= int(t0) - 1]
    if not any(x.startswith('daily sent') for x in after) and time.time() < t0 + DAILY_WAIT_S:
        out('NOT YET: no daily line yet, %.0f s after the start' % (time.time() - t0))
        raise NotYet()
    for x in after:
        if 'failed' in x:
            out('printed, a failure the service logged:', x)
    out('printed: journal records', len(recs), 'torn', torn, '| log lines since the start', len(after))
    g, reply = daily_checks(log, recs, pid, t0, today)
    d = [r for r in recs if r.get('kind') == 'daily']
    if d:
        out('printed: the daily record - top', d[0].get('top'), 'strong', d[0].get('strong'), 'cards',
            [(c.get('coin'), c.get('side'), c.get('mode')) for c in d[0].get('cards', [])])
    verdict('G-DAILY', g)
    verdict('G-REPLY', reply)


def mode_load():
    pid = int(show(UNIT, 'MainPID')['MainPID'])
    cpu, wall = proc_cpu(pid), time.time() - proc_start(pid)
    m = show(UNIT, 'MemoryCurrent', 'MemoryPeak', 'MemorySwapCurrent')
    s = proc_status(pid)
    out('printed:', ' '.join(f'{k}={v}' for k, v in sorted(m.items())), '|',
        ' '.join(f'{k}={s.get(k, "").strip()}' for k in ('VmRSS', 'VmHWM', 'VmSwap', 'Threads')))
    out(f'printed: processor {cpu:.2f} s over {wall:.1f} s of wall time since the process started')
    verdict('G-LOAD', {f'at least {LOAD_MIN_S} s since the start': wall >= LOAD_MIN_S,
                       f'processor at most {LOAD_MAX} of the core': cpu / wall <= LOAD_MAX})


def mode_restart():
    state = load_state()
    k = state['marks']['kill']
    p = show(UNIT, 'MainPID', 'NRestarts', 'ActiveState', 'SubState')
    new = int(p['MainPID'] or 0)
    with open(ROOT + '/service.log', encoding='utf-8', errors='replace') as fh:
        log = log_lines(fh.read())
    with open(ROOT + '/journal.jsonl', encoding='utf-8') as fh:
        recs, torn = journal_records(fh.read())
    today = dt.datetime.now(dt.timezone.utc).date()
    g, once = restart_checks(log, recs, int(k['unit']['MainPID']), new, proc_start(new) if new else 0,
                             k['ns'] / 1e9, p['NRestarts'], p['ActiveState'] == 'active' and p['SubState'] == 'running',
                             today)
    out('printed: old MainPID', k['unit']['MainPID'], 'new', new, 'started', utc(proc_start(new)) if new else '-')
    verdict('G-RESTART', g)
    verdict('G-ONCE', once)


def still_wait(last, arch, started_us, now_ns, mono_ns):
    """NOT YET while the archive runs, or while no run of it has started since the last reload of systemd and fewer
    than RUN_WAIT_S have passed - its timer may elapse 600 s after a reload (map section 7 items 115 and 129); past
    STILL_DEADLINE_S it decides on what exists. (wait, a run started after the reload, seconds since the reload)."""
    elapsed = (now_ns - last['ns']) / 1e9
    ran = started_us * 1000 > last['mono_ns']
    busy = arch in ('active', 'activating', 'reloading', 'deactivating')
    return (busy or not ran and elapsed < RUN_WAIT_S) and elapsed < STILL_DEADLINE_S, ran, elapsed


def mode_still():
    state = load_state()
    last = max((state['marks'][m] for m in ('install', 'start', 'stop') if m in state['marks']), key=lambda r: r['ns'])
    a = show(ARCHIVE, 'ActiveState', 'ExecMainStartTimestampMonotonic')
    arch, started_us = a.get('ActiveState', ''), int(a.get('ExecMainStartTimestampMonotonic') or 0)
    wait, ran, elapsed = still_wait(last, arch, started_us, time.time_ns(), time.monotonic_ns())
    if wait:
        out('NOT YET: archive %s, a run since the last reload %s, %.0f s after it' % (arch, ran, elapsed))
        raise NotYet()
    after = {u: show(u, 'MainPID', 'NRestarts', 'ActiveState', 'UnitFileState') for u in CAPTURE}
    before = state['host']['units']
    ledger = ledger_restarts()
    for u in CAPTURE:
        out('printed:', u, 'before', json.dumps(before[u], sort_keys=True), 'after', json.dumps(after[u], sort_keys=True))
    out('printed: the archive ledger restart records', state['host']['ledger_restarts'], '->', ledger, '| archive', arch,
        '| a run since the last reload', ran, '| %.0f s after it' % elapsed)
    deferred_run()
    g = still_checks(before, after, state['host']['ledger_restarts'], ledger)
    if arch in ('active', 'activating', 'reloading', 'deactivating'):
        out('READING G-STILL: UNDECIDABLE - the archive still runs at the deadline')
        return
    if not all(g.values()):
        since = int(state['host']['ns'] / 1e9) - 5
        rc, so, _ = sh(['journalctl', '-u', CAPTURE[0], '-u', CAPTURE[1], '-u', CAPTURE[2], '--since', f'@{since}',
                        '--no-pager', '-o', 'short-iso'])
        out('printed, the capture units\' journal since the host gate:\n' + so)
    verdict('G-STILL', g)


def mode_stopped():
    p = show(UNIT, 'ActiveState', 'UnitFileState')
    checks = {'the unit inactive or failed': p.get('ActiveState') in ('inactive', 'failed'),
              'the unit disabled': p.get('UnitFileState') == 'disabled',
              'no process under the service argv': procs(ARGV) == []}
    verdict('STOPPED', checks)


def mode_selftest():
    n = []

    def ok(cond, name):
        n.append(name)
        assert cond, name

    sample = ('**Revision string:** `2026-10-28-a`\n\n| `A1` — observation set | `229a944f2d51` |\n'
              '| `A3` — phase | `0-complete / 1-x` |\n\n### Fingerprint table\n\n| path | lines | bytes | state | SHA-256 |\n'
              '|---|---|---|---|---|\n| `SYSTEM-MAP.md` | — | — | reported | self-reference; report the value you compute |\n'
              '| `a.py` | 1,135 | 50,928 | frozen | `' + 'a' * 64 + '` |\n| `.gitignore` | 5 | 252 | tracked | `' + 'b' * 64
              + '` |\n\nHashes are of the file as committed')
    rev, an, rows = parse_map(sample)
    ok(rev == '2026-10-28-a' and an == {'A1': '229a944f2d51', 'A3': '0-complete / 1-x'}, 'parse_map: revision, anchors')
    ok(rows == [('SYSTEM-MAP.md', None, None, 'reported', 'self-reference; report the value you compute'),
                ('a.py', 1135, 50928, 'frozen', 'a' * 64), ('.gitignore', 5, 252, 'tracked', 'b' * 64)],
       'parse_map: three rows, commas read')
    log = log_lines('2026-10-29T07:00:01Z serving the pinned chat: pid 42 offset 0 daily-sent -\nTraceback (most\n'
                    '2026-10-29T07:00:03Z candles refreshed to the close of 2026-10-28 | missing -\n'
                    '2026-10-29T07:00:04Z daily sent for the close of 2026-10-28\n2026-10-29T07:00:05Z help sent\n')
    ok([x for _, x in log][1:] == ['candles refreshed to the close of 2026-10-28 | missing -',
                                   'daily sent for the close of 2026-10-28', 'help sent'] and len(log) == 4,
       'log_lines: four own lines, the traceback dropped')
    t0 = dt.datetime(2026, 10, 29, 7, 0, 0, tzinfo=dt.timezone.utc).timestamp()
    rec = {'utc': '2026-10-29T07:00:04+00:00', 'kind': 'daily', 'rule': RULE, 'close_of': '2026-10-28',
           'deposit': 10000.0, 'risk_pct': 0.5, 'top': ['A', 'B', 'C'], 'strong': ['A'], 'message_ids': [5],
           'signals': {str(i): 1 for i in range(42)}, 'cards': [{}, {}, {}]}
    recs, torn = journal_records(json.dumps(rec) + '\n{"utc": "2026-10-29T07:0')
    ok(len(recs) == 1 and torn == 1, 'journal_records: a torn last line counted and left out')
    try:
        journal_records('{"a": 1\n{"b": 2}\n')
        ok(False, 'journal_records: a torn inner line refused')
    except AssertionError:
        ok(True, 'journal_records: a torn inner line refused')
    g, reply = daily_checks(log, recs, 42, t0, dt.date(2026, 10, 29))
    ok(all(g.values()) and len(g) == 8 and all(reply.values()), 'daily_checks: 8 of 8 and the reply on a good day')
    g, _ = daily_checks(log, recs + [dict(rec)], 42, t0, dt.date(2026, 10, 29))
    ok(not g['exactly one daily record, made today'], 'daily_checks: a second daily record fails')
    g, _ = daily_checks(log, recs, 43, t0, dt.date(2026, 10, 29))
    ok(not g['the service logged its start under the unit MainPID'], 'daily_checks: another pid fails')
    short = [(t, x.replace('missing -', 'missing EGLD')) for t, x in log]
    g, _ = daily_checks(short, recs, 42, t0, dt.date(2026, 10, 29))
    ok(not g['its candles refreshed to the close of the day before, 42 of 42 served'],
       'daily_checks: a coin not served fails')
    log2 = log + [(int(t0) + 100, 'serving the pinned chat: pid 50 offset 3 daily-sent 2026-10-29')]
    g, once = restart_checks(log2, recs, 42, 50, t0 + 95, t0 + 60, '1', True, dt.date(2026, 10, 29))
    ok(all(g.values()) and all(once.values()), 'restart_checks: a clean restart passes')
    g, once = restart_checks(log2 + [(int(t0) + 101, 'daily sent for the close of 2026-10-28')], recs, 42, 50,
                             t0 + 95, t0 + 60, '1', True, dt.date(2026, 10, 29))
    ok(not once['no daily sent after the kill'], 'restart_checks: a second daily after the kill fails')
    g, _ = restart_checks(log2, recs, 42, 50, t0 + 125, t0 + 60, '1', True, dt.date(2026, 10, 29))
    ok(not g['started after the kill and at most 60 s later'], 'restart_checks: a restart 65 s late fails')
    u = lambda pid, n: {'MainPID': str(pid), 'NRestarts': str(n), 'ActiveState': 'active'}
    before = {'btc-recorder.service': u(1, 0), 'btc-pairbook.service': u(2, 9), 'btc-rewardbook.service': u(3, 1)}
    ok(all(still_checks(before, before, 5, 5).values()), 'still_checks: nothing moved passes')
    moved = dict(before, **{'btc-pairbook.service': u(7, 10)})
    ok(all(still_checks(before, moved, 5, 6).values()), 'still_checks: one archive restart passes')
    ok(not all(still_checks(before, moved, 5, 5).values()), 'still_checks: a pair book restart without a record fails')
    ok(not all(still_checks(before, dict(before, **{'btc-recorder.service': u(9, 0)}), 5, 5).values()),
       'still_checks: a recorder restart fails')
    ok(TOKEN_RE.fullmatch('123456789:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw') is not None
       and TOKEN_RE.fullmatch('123456789:short') is None and TOKEN_RE.fullmatch('abc:' + 'A' * 35) is None,
       'the token shape: a bot token and two others')
    starts = [(10, 1000.0, 'claude'), (11, 5000.0, '/x/claude.exe')]
    ok(live_or_earlier(5030, starts) == [11] and live_or_earlier(4998, starts) == [] and live_or_earlier(999, starts) == [10],
       'live_or_earlier: born 1 s before to 60 s after a start')
    ok(by_name(WORK, 'logs/03-host.log') and by_name(WORK, 'history.json') and not by_name(WORK, 'stage/x')
       and not by_name('/tmp/x', 'state.json'), 'by_name: the state, the logs and the history of the work tree')
    ok(not reclaimable('/root/other') and reclaimable(WORK), 'reclaimable: the work tree and nothing else outside /tmp')
    last = {'ns': 10 ** 18, 'mono_ns': 5 * 10 ** 12}
    s_ = 10 ** 9
    ok(still_wait(last, 'inactive', 0, last['ns'] + 700 * s_, 0)[0]
       and still_wait(last, 'active', 5 * 10 ** 9 + 1, last['ns'] + 2000 * s_, 0)[0]
       and not still_wait(last, 'inactive', 5 * 10 ** 9 + 1, last['ns'] + 700 * s_, 0)[0]
       and not still_wait(last, 'inactive', 0, last['ns'] + 1300 * s_, 0)[0]
       and not still_wait(last, 'active', 0, last['ns'] + 4300 * s_, 0)[0],
       'still_wait: waits for the run a reload sets off, and no longer than its bounds')
    ok(ARGV == ['/root/tz04a-env/venv/bin/python', '-B', '-u', '/root/adv3-bot-svc/adv3-bot.py', '--serve'],
       'the service argv is the unit\'s ExecStart')
    names = ['CryptoReports/TZ-34-rewardbook-archive-timer-report.md', 'CryptoTZ/TZ-34-rewardbook-archive-timer.md',
             'CryptoTZ/TZ-35-advisor-bot.md', 'CryptoTZ/TZ-35a-other.md']
    ok(all(number_reading(names).values()) and not all(number_reading(names + ['CryptoTZ/TZ-35-other.md']).values())
       and not all(number_reading(names + ['CryptoReports/TZ-35-advisor-bot-report.md']).values())
       and not all(number_reading(names[:2]).values()),
       'number_reading: its one file passes; a second TZ-35- file, a TZ-35- report or none fails')
    text = ('{"event": "start", "run": 1793260762, "wall_ns": 1793260762000000000}\n'
            '{"event": "deferred", "run": 1793260762, "count": 1, "wall_ns": 1793260977000000000}\n\n'
            '{"event": "start", "run": 1793242820, "wall_ns": 1793242820000000000}\n{"event": "comp')
    held, torn = ledger_events(text, DEFERRED_RUN)
    ok([e for e, _c, _t in held] == ['start', 'deferred'] and held[1][1] == 1 and torn == 1
       and held[0][2] == '2026-10-29T07:59:22.000000Z', 'ledger_events: one run\'s records, a torn line counted')
    out(f'SELFTEST PASS: {len(n)} of {len(n)} checks passed')


def main(argv):
    if not argv:
        sys.exit('usage: tz35-advisor-deploy.py MODE [ARG...]')
    mode, rest = argv[0], argv[1:]
    table = {'fingerprint': mode_fingerprint, 'host': mode_host, 'copy': mode_copy, 'props': mode_props, 'daily': mode_daily,
             'load': mode_load, 'restart': mode_restart, 'still': mode_still, 'stopped': mode_stopped,
             'selftest': mode_selftest, 'number': mode_number}
    try:
        if mode == 'scratch':
            assert len(rest) == 1, 'scratch OWN'
            mode_scratch(rest[0])
        elif mode == 'reclaim':
            mode_reclaim(rest)
        elif mode == 'mark':
            assert len(rest) == 1 and rest[0] in ('install', 'start', 'kill', 'stop'), 'mark install|start|kill|stop'
            mode_mark(rest[0])
        elif mode == 'unit':
            assert len(rest) == 1 and rest[0] in ('0', '1'), 'unit 0|1'
            mode_unit(int(rest[0]))
        else:
            assert mode in table and not rest, 'unknown mode %r' % (argv,)
            table[mode]()
    except NotYet:
        return 3
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
