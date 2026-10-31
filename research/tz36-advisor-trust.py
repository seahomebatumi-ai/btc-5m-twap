#!/usr/bin/env python3
# tz36-advisor-trust.py - TZ-36's checker: the fingerprint, the host gate, the number, G-RULE, COPY, G-RENDER, the
# readings after the unit's restart, and the marks. Standard library only. It starts and stops no unit, signals no
# process and sends no request of its own (G-RENDER runs the service copy's adv3.py, which reads Binance's public
# market), and it never reads or prints the bot's token or the pinned chat. Exits: 0 every assert held; 1 a failed
# assert, named; 3 NOT YET.
import ast, calendar, datetime as dt, hashlib, json, os, re, shutil, subprocess, sys, time

WORK = '/root/tz36-work'
WT = WORK + '/wt'
STATE = WORK + '/state.json'
PRIMARY = '/root/btc-5m-twap'
FORENSICS = '/root/btc-forensics'
SVC = '/root/adv3-bot-svc'
BOTDIR = '/var/lib/adv3-bot'
PY = '/root/tz04a-env/venv/bin/python'
ARGV = [PY, '-B', '-u', SVC + '/adv3-bot.py', '--serve']
BOT = 'adv3-bot.service'
CAPTURES = ('btc-recorder.service', 'btc-pairbook.service', 'btc-rewardbook.service')
TZ_FILE = 'CryptoTZ/TZ-36-advisor-trust-block.md'
NUMBER = 'TZ-36-'
MAP_REV = '2026-10-29-b'
ANCHORS = {'A1': '229a944f2d51', 'A2': '6c5089330629',
           'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable',
           'A4': '437b45ea196b', 'A5': '0f6c90451cbd', 'A6': '729f0bcdbee3'}
DERIVED = {'A2': 'research/twap-divergence.py', 'A4': 'BTC-EXECUTOR-INSTRUCTIONS.md',
           'A5': 'research/recorder/recorder.py', 'A6': 'research/pfair.py'}
H = {'adv3_old': '7f2863a5b433ed7008c8f44af4f9c59d724d0c016c2c317f451158899c4f9adb',
     'adv3_new': 'd73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8',
     'bot': 'e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb',
     'rule': 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169',
     'unit': '82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66'}
RULE_FUNCS = ('signs', 'signal', 'strength', 'true_range', 'unit', 'open_at', 'hold', 'close_at', 'simulate', 'states',
              'ranking', 'simulate_strong', 'stats', 'funding_of')
CHANGED = {'card', 'card_lines', 'facts_checks', 'history', 'message', 'report'}
ADDED = {'book_line', 'forward_book', 'signed', 'trust', 'trust_lines'}
MEM_FLOOR, DISK_FLOOR = 170_344_448, 7_400_000_000
ROWS, FROZEN = 55, 52
MARKERS = ('Оценка доверия', 'Надёжность системы: <b>1/5</b>', 'Уверенность в сделках:', 'STRONG обоснован: <b>нет</b>',
           'Качество данных: <b>низкое</b>', 'Ожидаемая R на сделку: <b>не установлена</b>',
           'Инвалидация: у каждой карточки', 'Форвард с 28.10', 'Все сигналы: входов', 'STRONG: входов')
CARD = re.compile(r'^[🟢🔴] <b>[A-Z0-9]+ · (LONG|SHORT)</b>', re.M)


class Failed(Exception):
    pass


class NotYet(Exception):
    pass


def out(*parts):
    print(*parts, flush=True)


def sh(args, **kw):
    p = subprocess.run(args, capture_output=True, text=True, **kw)
    return p.returncode, p.stdout, p.stderr


def read(path, mode='r'):
    with open(path, mode, **({} if 'b' in mode else {'encoding': 'utf-8'})) as fh:
        return fh.read()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    return sha256_bytes(read(path, 'rb'))


def load_state():
    return json.loads(read(STATE)) if os.path.exists(STATE) else {}


def save_state(state):
    tmp = STATE + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(state, indent=1, sort_keys=True) + '\n')
    os.replace(tmp, STATE)


def verdict(name, checks):
    n = sum(1 for v in checks.values() if v)
    for k, v in checks.items():
        out(('ok   ' if v else 'FAIL ') + k)
    out('READING %s: %s - %d of %d' % (name, 'PASS' if n == len(checks) else 'FAIL', n, len(checks)))
    if n != len(checks):
        raise Failed(name)


def show(unit, *props):
    args = ['systemctl', 'show', unit] + [a for p in props for a in ('-p', p)]
    rc, so, se = sh(args, env=dict(os.environ, TZ='UTC'))
    assert rc == 0, se
    return dict(line.split('=', 1) for line in so.splitlines() if '=' in line)


def proc_argv(pid):
    try:
        with open('/proc/%s/cmdline' % pid, 'rb') as fh:
            parts = fh.read().split(b'\0')
    except OSError:
        return None
    return [p.decode() for p in parts[:-1]] if parts and parts[-1] == b'' else [p.decode() for p in parts]


def procs(argv):
    return sorted(int(p) for p in os.listdir('/proc') if p.isdigit() and proc_argv(p) == argv)


def proc_start(pid):
    """The process's start as epoch seconds, from /proc/<pid>/stat (field 22) and the boot time."""
    stat = read('/proc/%s/stat' % pid)
    fields = stat[stat.rindex(')') + 2:].split()
    ticks = int(fields[19])
    btime = next(int(line.split()[1]) for line in read('/proc/stat').splitlines() if line.startswith('btime '))
    return btime + ticks / os.sysconf('SC_CLK_TCK')


# ---- pure readings: each takes what the modes read and returns its checks -----------------------------------

def parse_map(text):
    """(revision, {anchor: value}, rows) of SYSTEM-MAP.md section 0; a row is (path, lines, bytes, state, sha)."""
    rev = re.search(r'\*\*Revision string:\*\* `([^`]+)`', text).group(1)
    anchors = dict(re.findall(r'^\| `(A\d)` — [^|]*\| `([^`]+)` \|$', text, re.M))
    rows = []
    for line in text[text.index('### Fingerprint table'):].split('\n')[1:]:
        if line.startswith('## ') or line.startswith('### '):
            break
        m = re.match(r'^\| `([^`]+)` \| ([^|]+) \| ([^|]+) \| (frozen|tracked|reported) \| ([^|]+) \|$', line)
        if m:
            num = lambda s: None if s.strip() == '—' else int(s.replace(',', ''))
            sha = re.search(r'`([0-9a-f]{64})`', m.group(5))
            rows.append((m.group(1), num(m.group(2)), num(m.group(3)), m.group(4), sha.group(1) if sha else None))
    return rev, anchors, rows


def top_level(src):
    """{name: ast.dump} of a module's functions, and of its assignments keyed by their targets."""
    fns, asg = {}, {}
    for n in ast.parse(src).body:
        if isinstance(n, ast.FunctionDef):
            fns[n.name] = ast.dump(n)
        elif isinstance(n, ast.Assign):
            asg[','.join(ast.unparse(t) for t in n.targets)] = ast.dump(n)
    return fns, asg


def rule_checks(old_src, new_src):
    """G-RULE's first five checks: the two adv3.py files differ in exactly the functions and constants TZ-36 names."""
    (of, oa), (nf, na) = top_level(old_src), top_level(new_src)
    return {
        'the functions that changed are exactly %s' % sorted(CHANGED):
            {k for k in of if k in nf and of[k] != nf[k]} == CHANGED,
        'the functions added are exactly %s' % sorted(ADDED): set(nf) - set(of) == ADDED,
        'no function removed': set(of) - set(nf) == set(),
        'the %d rule functions are identical by AST' % len(RULE_FUNCS):
            all(k in of and k in nf and of[k] == nf[k] for k in RULE_FUNCS),
        'the constants: FACTS changed, RELIABILITY and STRONG_JUSTIFIED added, nothing else':
            {k for k in oa if k in na and oa[k] != na[k]} == {'FACTS'} and set(oa) - set(na) == set()
            and set(na) - set(oa) == {'(RELIABILITY, STRONG_JUSTIFIED)'},
    }


def render_checks(msg, rc, err, rep, rc_json, err_json, close_day):
    """G-RENDER: the live message and the live report of the service copy; counts and labels only."""
    n = len(CARD.findall(msg))
    checks = {
        'the message run exits 0 with no traceback': rc == 0 and 'Traceback' not in err and msg.strip() != '',
        'the message holds the forward book, the six ratings and their lines': all(k in msg for k in MARKERS),
        'every card (%d) holds its basis and its invalidation' % n:
            msg.count('Основание: сумма знаков') == n and msg.count('Инвалидация: цена') == n and n <= 3,
        'the message fits three Telegram parts': len(msg) < 12000,
        'the report run exits 0 with no traceback': rc_json == 0 and 'Traceback' not in err_json and rep is not None,
    }
    if rep is None:
        return checks
    book, tr = rep.get('book', {}), rep.get('trust', {})
    checks.update({
        'the report is the frozen rule\'s, of 42 coins': rep.get('rule') == H['rule'] and len(rep.get('rows', {})) == 42,
        'the ratings: system 1, STRONG not justified, the data fresh, a trade 0 or 1, one for each card':
            tr.get('system') == 1 and tr.get('strong_justified') is False and tr.get('fresh') is True
            and set(tr.get('cards', {})) == set(rep['top'])
            and set(tr.get('cards', {}).values()) <= {0, 1},
        'the books: opened is closed plus open, the total is the two parts\' sum': all(
            b['opened'] == b['closed'] + b['open'] and abs(b['total_R'] - (b['closed_R'] + b['open_R'])) < 1e-9
            for b in book.values()) and set(book) == {'base', 'strong'},
        'the forward days are the closes from 2026-10-28 to the report\'s': all(
            b['days'] == close_day for b in book.values()),
        'each card carries a rank 1 to 3 and a sum of signs of 2 to 4 in size': all(
            cd.get('rank') in (1, 2, 3) and cd.get('sum') is not None and 2 <= abs(cd['sum']) <= 4 for cd in rep['cards']),
    })
    return checks


def unit_checks(which, pre, now):
    """The readings after a restart: now is what the modes read; pre is the snapshot of the mark before the kill."""
    want_sha = H['adv3_new'] if which == 'new' else H['adv3_old']
    return {
        'the unit is active, running and enabled': (now['bot']['ActiveState'], now['bot']['SubState'],
                                                    now['bot']['UnitFileState']) == ('active', 'running', 'enabled'),
        'a new MainPID, one restart more': int(now['bot']['MainPID']) not in (0, int(pre['bot']['MainPID']))
        and int(now['bot']['NRestarts']) == int(pre['bot']['NRestarts']) + 1,
        'the process started after the kill mark and within 90 s of it': pre['t'] <= now['start'] <= pre['t'] + 90,
        'the process runs the unit\'s exact argv, alone': now['argv'] == ARGV and now['procs'] == [int(now['bot']['MainPID'])],
        'the service copy is %s\'s adv3.py, the process started after the copy' % which:
            now['sha_adv3'] == want_sha and now['start'] > now['copy_t'],
        'the service copy\'s bot and the unit file are unchanged': now['sha_bot'] == H['bot'] and now['sha_unit'] == H['unit'],
        'the day\'s message was not sent again: daily-sent and the journal\'s daily records as before': (
            now['daily'] == pre['daily'] and now['journal'] == pre['journal']),
        'the log shows the new process serving and no daily sent, no traceback, since the mark': (
            now['serving'] and not now['daily_line'] and not now['traceback']),
        'the three capture units unchanged, each active': all(
            now['caps'][u]['ActiveState'] == 'active' and now['caps'][u]['MainPID'] == pre['caps'][u]['MainPID']
            and now['caps'][u]['NRestarts'] == pre['caps'][u]['NRestarts'] for u in CAPTURES),
    }


def log_since(text, t0, pid):
    """From service.log: whether the process pid logged 'serving', whether a daily was sent, whether a traceback
    appeared, in the lines stamped at or after t0 (epoch seconds)."""
    serving = daily = tb = since_ok = False
    for line in text.splitlines():
        m = re.match(r'^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})Z (.*)$', line)
        if not m:
            tb = tb or ('Traceback' in line and since_ok)
            continue
        stamp = calendar.timegm(time.strptime(m.group(1), '%Y-%m-%dT%H:%M:%S'))
        since_ok = stamp >= t0 - 1
        if since_ok:
            serving = serving or m.group(2).startswith('serving the pinned chat: pid %d ' % pid)
            daily = daily or m.group(2).startswith('daily sent')
            tb = tb or 'Traceback' in m.group(2)
    return serving, daily, tb


# ---- the modes -------------------------------------------------------------------------------------------------

def mode_fingerprint():
    text = read(PRIMARY + '/SYSTEM-MAP.md')
    rev, anchors, rows = parse_map(text)
    checks = {'revision ' + MAP_REV: rev == MAP_REV}
    for a, want in ANCHORS.items():
        checks['anchor ' + a] = anchors.get(a) == want
    for a, path in DERIVED.items():
        checks['%s re-derived from %s' % (a, path)] = sha256_file(PRIMARY + '/' + path)[:12] == anchors.get(a)
    states = {}
    for path, lines, nbytes, state, sha in rows:
        states[state] = states.get(state, 0) + 1
        if path == 'SYSTEM-MAP.md':
            b = read(PRIMARY + '/' + path, 'rb')
            out('reported %d lines %d bytes %s %s' % (b.count(b'\n'), len(b), sha256_bytes(b), path))
            continue
        b = read(PRIMARY + '/' + path, 'rb')
        got = (b.count(b'\n'), len(b), sha256_bytes(b))
        out('%-8s %d lines %d bytes %s %s' % (state, got[0], got[1], got[2], path))
        if state == 'frozen':
            checks['frozen ' + path] = got == (lines, nbytes, sha)
    checks['the table holds %d rows, %d frozen, 2 tracked, 1 reported' % (ROWS, FROZEN)] = (
        len(rows) == ROWS and states == {'frozen': FROZEN, 'tracked': 2, 'reported': 1})
    verdict('FINGERPRINT', checks)


def mode_host():
    checks = {}
    rc, so, _ = sh(['find', '/var/lib/btc-recorder', '-mindepth', '1', '-maxdepth', '3', '-name', 'manifest.json',
                    '-print', '-quit'])
    checks['H1 the recorder\'s manifest.json is found'] = rc == 0 and len(so.split()) == 1
    rc, so, _ = sh(['df', '-B1', '--output=source,size,avail', '/var/lib/btc-recorder'])
    src, size, avail = so.splitlines()[1].split()
    checks['H2 /dev/vda2 of 31612203008 bytes'] = (src, size) == ('/dev/vda2', '31612203008')
    rc, so, _ = sh(['grep', '-c', 'e3975b5da44c5328adf3bf3914634cd878842c73', '/var/lib/btc-recorder/runtime.jsonl'])
    checks['H2 the recorder\'s runtime record names e3975b5'] = rc == 0 and int(so) >= 1
    rc, so, _ = sh([PY, '-c', 'import sys; print(sys.version.split()[0])'])
    checks['H3 the venv interpreter is Python 3.12'] = rc == 0 and so.startswith('3.12.')
    units = {u: show(u, 'MainPID', 'NRestarts', 'ActiveState', 'SubState', 'UnitFileState') for u in CAPTURES + (BOT,)}
    for u in CAPTURES:
        checks['H4 %s active and enabled' % u] = (units[u]['ActiveState'], units[u]['UnitFileState']) == ('active', 'enabled')
    b = units[BOT]
    checks['H5 the bot is active, running and enabled'] = (b['ActiveState'], b['SubState'], b['UnitFileState']) == (
        'active', 'running', 'enabled')
    checks['H5 the bot\'s MainPID runs the unit\'s argv, alone'] = (
        int(b['MainPID']) > 0 and proc_argv(b['MainPID']) == ARGV and procs(ARGV) == [int(b['MainPID'])])
    checks['H5 the service copy holds adv3.py, adv3-bot.py and commit.txt only'] = (
        sorted(os.listdir(SVC)) == ['adv3-bot.py', 'adv3.py', 'commit.txt'])
    checks['H5 adv3.py is TZ-35\'s and adv3-bot.py is TZ-35\'s'] = (
        sha256_file(SVC + '/adv3.py') == H['adv3_old'] and sha256_file(SVC + '/adv3-bot.py') == H['bot'])
    checks['H5 the installed unit file is TZ-35\'s'] = sha256_file('/etc/systemd/system/adv3-bot.service') == H['unit']
    checks['H5 commit.txt is 40 hex characters and a newline'] = re.fullmatch(r'[0-9a-f]{40}\n', read(SVC + '/commit.txt')) is not None
    checks['H6 the record holds daily-sent and a journal of whole lines'] = (
        re.fullmatch(r'\d{4}-\d{2}-\d{2}\n?', read(BOTDIR + '/daily-sent')) is not None
        and read(BOTDIR + '/journal.jsonl', 'rb').endswith(b'\n'))
    mem = {k: int(v.split()[0]) for k, v in (l.split(':', 1) for l in read('/proc/meminfo').splitlines())}
    checks['memory gate: MemAvailable at least %d bytes' % MEM_FLOOR] = mem['MemAvailable'] * 1024 >= MEM_FLOOR
    checks['disk gate: /dev/vda2 free at least %d bytes' % DISK_FLOOR] = int(avail) >= DISK_FLOOR
    out('units:', json.dumps(units, sort_keys=True))
    out('MemAvailable %d bytes, /dev/vda2 free %s bytes' % (mem['MemAvailable'] * 1024, avail))
    verdict('HOST', checks)


def number_reading(names):
    return {'CryptoTZ/ holds %s and no other file of that number' % TZ_FILE:
            [n for n in names if n.startswith('CryptoTZ/' + NUMBER)] == [TZ_FILE],
            'CryptoReports/ holds no report of that number': not [n for n in names if n.startswith('CryptoReports/' + NUMBER)]}


def mode_number():
    rc, so, se = sh(['git', '-C', PRIMARY, 'ls-tree', '--name-only', 'origin/main', '--', 'CryptoTZ/', 'CryptoReports/'])
    assert rc == 0, se
    names = so.split('\n')
    for n in names:
        if n.startswith('CryptoTZ/' + NUMBER) or n.startswith('CryptoReports/' + NUMBER):
            out(n)
    verdict('NUMBER', number_reading(names))


def git_show(path):
    rc, so, se = sh(['git', '-C', PRIMARY, 'show', 'origin/main:' + path])
    assert rc == 0, se
    return so


def mode_rule():
    checks = rule_checks(git_show('advisor/adv3.py'), read(WT + '/advisor/adv3.py'))
    checks['adv3-bot.py is main\'s, byte for byte'] = read(WT + '/advisor/adv3-bot.py', 'rb') == git_show('advisor/adv3-bot.py').encode()
    rule_txt = read(WT + '/advisor/RULE-ADV-3.txt', 'rb')
    checks['RULE-ADV-3.txt is main\'s and hashes to the RULE constant'] = (
        rule_txt == git_show('advisor/RULE-ADV-3.txt').encode() and sha256_bytes(rule_txt) == H['rule']
        and ("RULE = '%s'" % H['rule']) in read(WT + '/advisor/adv3.py'))
    verdict('RULE', checks)


def daily_records(text):
    """How many records of kind 'daily' a journal.jsonl text holds: the Boss's own requests add records of another
    kind, and a restart must add none of the first."""
    n = 0
    for line in text.splitlines():
        try:
            n += json.loads(line).get('kind') == 'daily'
        except ValueError:
            pass
    return n


def snapshot():
    """What a mark records: the instant, the bot's and the captures' units, the record's two figures."""
    st = {'t': time.time(), 'bot': show(BOT, 'MainPID', 'NRestarts', 'ActiveState'),
          'caps': {u: show(u, 'MainPID', 'NRestarts', 'ActiveState') for u in CAPTURES},
          'daily': read(BOTDIR + '/daily-sent').strip(), 'journal': daily_records(read(BOTDIR + '/journal.jsonl'))}
    return st


def mode_mark(name):
    assert name in ('deploy', 'kill', 'rollback', 'kill2'), name
    st = load_state()
    snap = snapshot()
    if name in ('kill', 'kill2'):
        today = time.strftime('%Y-%m-%d', time.gmtime())
        assert snap['daily'] == today, 'the day\'s message is not sent: daily-sent %s, today %s' % (snap['daily'], today)
    st.setdefault('marks', {})[name] = snap
    save_state(st)
    out('mark %s at %s: bot pid %s NRestarts %s, daily-sent %s, %d daily records' % (
        name, time.strftime('%FT%TZ', time.gmtime(snap['t'])), snap['bot']['MainPID'], snap['bot']['NRestarts'],
        snap['daily'], snap['journal']))


def mode_copy():
    rc, head, _ = sh(['git', '-C', WT, 'rev-parse', 'HEAD'])
    rc2, up, _ = sh(['git', '-C', WT, 'rev-parse', 'origin/tz-36-advisor-trust-block'])
    commit = read(SVC + '/commit.txt')
    verdict('COPY', {
        'the service copy holds adv3.py, adv3-bot.py and commit.txt only': sorted(os.listdir(SVC)) == ['adv3-bot.py', 'adv3.py', 'commit.txt'],
        'adv3.py is Appendix A\'s': sha256_file(SVC + '/adv3.py') == H['adv3_new'],
        'adv3-bot.py is unchanged': sha256_file(SVC + '/adv3-bot.py') == H['bot'],
        'commit.txt is the branch head and the worktree\'s HEAD': (
            re.fullmatch(r'[0-9a-f]{40}\n', commit) is not None and rc == 0 and rc2 == 0 and commit.strip() == head.strip() == up.strip()),
        'the branch\'s adv3.py equals the service copy\'s': read(WT + '/advisor/adv3.py', 'rb') == read(SVC + '/adv3.py', 'rb'),
    })


def mode_render():
    cmd = ['nice', '-n', '19', PY, '-B', SVC + '/adv3.py']
    p1 = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    p2 = subprocess.run(cmd + ['--json'], capture_output=True, text=True, timeout=600)
    try:
        rep = json.loads(p2.stdout)
    except ValueError:
        rep = None
    close_day = None
    if rep is not None:
        close_day = (dt.date.fromisoformat(rep['close_of']) - dt.date(2026, 10, 28)).days + 1
    out('message: %d characters, %d lines; report: %d bytes' % (len(p1.stdout), p1.stdout.count('\n'), len(p2.stdout)))
    verdict('RENDER', render_checks(p1.stdout, p1.returncode, p1.stderr, rep, p2.returncode, p2.stderr, close_day))


def mode_unit(which):
    assert which in ('new', 'old'), which
    st = load_state()
    mark = 'kill' if which == 'new' else 'kill2'
    pre = st['marks'][mark]
    copy_t = st['marks']['deploy' if which == 'new' else 'rollback']['t']
    bot = show(BOT, 'MainPID', 'NRestarts', 'ActiveState', 'SubState', 'UnitFileState')
    pid = int(bot['MainPID'])
    if pid in (0, int(pre['bot']['MainPID'])) or bot['ActiveState'] != 'active':
        if time.time() - pre['t'] < 100:
            raise NotYet()
    caps = {u: show(u, 'MainPID', 'NRestarts', 'ActiveState') for u in CAPTURES}
    start = proc_start(pid) if pid else 0.0
    serving, daily_line, tb = log_since(read(BOTDIR + '/service.log'), pre['t'], pid)
    now = {'bot': bot, 'caps': caps, 'start': start, 'copy_t': copy_t, 'argv': proc_argv(pid) if pid else None,
           'procs': procs(ARGV), 'sha_adv3': sha256_file(SVC + '/adv3.py'), 'sha_bot': sha256_file(SVC + '/adv3-bot.py'),
           'sha_unit': sha256_file('/etc/systemd/system/adv3-bot.service'),
           'daily': read(BOTDIR + '/daily-sent').strip(), 'journal': daily_records(read(BOTDIR + '/journal.jsonl')),
           'serving': serving, 'daily_line': daily_line, 'traceback': tb}
    checks = unit_checks(which, pre, now)
    if which == 'old':
        checks['two restarts more than before the first kill'] = int(bot['NRestarts']) == int(st['marks']['kill']['bot']['NRestarts']) + 2
    out('bot: pid %d NRestarts %s started %s; captures: %s' % (pid, bot['NRestarts'], time.strftime('%FT%TZ', time.gmtime(start)),
        json.dumps({u: [c['MainPID'], c['NRestarts']] for u, c in caps.items()}, sort_keys=True)))
    verdict('UNIT-' + which.upper(), checks)


def kept_files():
    """The work tree's files a report keeps by name: state.json, history.json, the two files B-DEPLOY saves, and every
    file under logs/; relative to WORK, sorted."""
    names = ['state.json', 'history.json', 'adv3.before', 'commit.before']
    for d, _s, fs in os.walk(WORK + '/logs'):
        names += [os.path.relpath(os.path.join(d, f), WORK) for f in fs]
    return sorted(n for n in names if os.path.isfile(os.path.join(WORK, n)))


def mode_keep():
    """B-RECLAIM-OWN's copy: every kept file into the forensic store as tz36-work--<path with - for />, by exclusive
    create and verified whole; the branch worktree must hold nothing but its pushed HEAD."""
    rc, so, _ = sh(['git', '-C', WT, 'status', '--porcelain', '--ignored'])
    assert rc == 0 and so == '', 'keep: %s holds %r' % (WT, so[:400])
    head = sh(['git', '-C', WT, 'rev-parse', 'HEAD'])[1].strip()
    up = sh(['git', '-C', WT, 'rev-parse', '@{u}'])[1].strip()
    assert head and up == head, 'keep: %s at %s, upstream %r' % (WT, head, up)
    count = lambda: sum(len(f) for _d, _s, f in os.walk(FORENSICS))
    before, copied, held = count(), 0, 0
    for rel in kept_files():
        path = WORK + '/' + rel
        h = sha256_file(path)
        dest = FORENSICS + '/tz36-work--' + rel.replace('/', '--')
        if os.path.exists(dest):
            assert sha256_file(dest) == h, 'keep: %s exists with another hash' % dest
            held += 1
            out('K held   %s %s' % (h, dest))
            continue
        with open(path, 'rb') as src, open(dest, 'xb') as dst:
            shutil.copyfileobj(src, dst, 1 << 20)
        assert sha256_file(dest) == h, 'keep: %s did not copy whole' % dest
        copied += 1
        out('K copied %s %s' % (h, dest))
    after = count()
    assert after == before + copied, 'keep: store %d, expected %d' % (after, before + copied)
    out('KEEP PASS: %d files kept, %d copied, %d already held; forensic store %d -> %d files; worktree at %s, its upstream\'s'
        % (copied + held, copied, held, before, after, head))


def mode_stopped():
    bot = show(BOT, 'ActiveState', 'UnitFileState')
    verdict('STOPPED', {'the unit is inactive or failed, and disabled': bot['ActiveState'] in ('inactive', 'failed')
                        and bot['UnitFileState'] == 'disabled', 'no process runs under the unit\'s argv': procs(ARGV) == []})


# ---- the self-test: the pure readings on stand-ins, each with a negative control -----------------------------

def mode_selftest():
    done = []

    def ok(cond, name):
        done.append(name)
        assert cond, name

    mp = ('**Revision string:** `%s`\n\n| anchor | value |\n|---|---|\n| `A1` — observation set | `229a944f2d51` |\n'
          '| `A3` — phase | `x / y` |\n\n### Fingerprint table\n\n| path | lines | bytes | state | SHA-256 |\n|---|---|---|---|---|\n'
          '| `SYSTEM-MAP.md` | — | — | reported | self-reference |\n| `a/b.py` | 1,135 | 50,928 | frozen | `%s` |\n'
          '| `c.py` | 7 | 8 | tracked | `%s` |\n\n---\n\n## 1. Repository\n| `z.py` | 1 | 1 | frozen | `%s` |\n') % (
        MAP_REV, 'a' * 64, 'b' * 64, 'c' * 64)
    rev, anchors, rows = parse_map(mp)
    ok(rev == MAP_REV and anchors == {'A1': '229a944f2d51', 'A3': 'x / y'}, 'parse_map: the revision and the anchors')
    ok(rows == [('SYSTEM-MAP.md', None, None, 'reported', None), ('a/b.py', 1135, 50928, 'frozen', 'a' * 64),
                ('c.py', 7, 8, 'tracked', 'b' * 64)], 'parse_map: the table\'s rows, thousands separators read, the next section left out')
    old = 'RULE = 1\nFACTS = {1: 2}\ndef a():\n    return 1\ndef b():\n    return 2\n'
    new_ok = old.replace('{1: 2}', '{1: 2, 3: 4}').replace('return 2', 'return 3') + 'def c():\n    return 0\n'
    saved = (RULE_FUNCS, CHANGED, ADDED)
    globals().update(RULE_FUNCS=('a',), CHANGED={'b'}, ADDED={'c'})
    try:
        good = rule_checks(old, new_ok.replace('RULE = 1', 'RULE = 1\nRELIABILITY, STRONG_JUSTIFIED = 1, False'))
        ok(all(good.values()), 'rule_checks: exactly the named functions and constants differ')
        bad = rule_checks(old, new_ok.replace('return 1', 'return 9').replace('RULE = 1', 'RULE = 1\nRELIABILITY, STRONG_JUSTIFIED = 1, False'))
        ok(not all(bad.values()) and not bad[[k for k in bad if 'identical by AST' in k][0]], 'rule_checks: a changed rule function reads FAIL')
        bad2 = rule_checks(old, new_ok)
        ok(not all(bad2.values()), 'rule_checks: constants not added read FAIL')
    finally:
        globals().update(RULE_FUNCS=saved[0], CHANGED=saved[1], ADDED=saved[2])
    msg = '\n'.join(MARKERS + ('🟢 <b>XMR · LONG</b>', 'Основание: сумма знаков +4', 'Инвалидация: цена ≤ 1'))
    book = {'opened': 5, 'closed': 2, 'open': 3, 'closed_R': -1.5, 'open_R': 0.5, 'total_R': -1.0, 'days': 4}
    rep = {'rule': H['rule'], 'rows': {str(i): 0 for i in range(42)}, 'top': ['XMR'],
           'trust': {'system': 1, 'strong_justified': False, 'fresh': True, 'cards': {'XMR': 1}},
           'book': {'base': dict(book), 'strong': dict(book)}, 'cards': [{'rank': 1, 'sum': 4}]}
    ok(all(render_checks(msg, 0, '', rep, 0, '', 4).values()), 'render_checks: a whole message and report read PASS')
    ok(not render_checks(msg.replace('Оценка доверия', ''), 0, '', rep, 0, '', 4)['the message holds the forward book, the six ratings and their lines'],
       'render_checks: a missing rating block reads FAIL')
    ok(not all(render_checks(msg + '\n🔴 <b>BTC · SHORT</b>', 0, '', rep, 0, '', 4).values()), 'render_checks: a card without its basis reads FAIL')
    broken = dict(rep, book={'base': dict(book, total_R=-2.0), 'strong': dict(book)})
    ok(not all(render_checks(msg, 0, '', broken, 0, '', 4).values()), 'render_checks: a book whose total is not its parts\' sum reads FAIL')
    ok(not all(render_checks(msg, 0, '', rep, 0, '', 5).values()), 'render_checks: forward days not equal to the closes since 2026-10-28 read FAIL')
    pre = {'t': 1000.0, 'bot': {'MainPID': '10', 'NRestarts': '1'}, 'daily': '2026-10-31', 'journal': 7,
           'caps': {u: {'MainPID': str(i), 'NRestarts': '0', 'ActiveState': 'active'} for i, u in enumerate(CAPTURES, 20)}}
    now = {'bot': {'MainPID': '11', 'NRestarts': '2', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'},
           'caps': dict(pre['caps']), 'start': 1035.0, 'copy_t': 990.0, 'argv': ARGV, 'procs': [11], 'sha_adv3': H['adv3_new'],
           'sha_bot': H['bot'], 'sha_unit': H['unit'], 'daily': '2026-10-31', 'journal': 7, 'serving': True, 'daily_line': False,
           'traceback': False}
    ok(all(unit_checks('new', pre, now).values()) and len(unit_checks('new', pre, now)) == 9, 'unit_checks: a clean restart reads 9 of 9')
    for key, val, label in (('daily', '2026-11-01', 'a daily-sent changed'), ('journal', 8, 'a message sent again'),
                            ('start', 1200.0, 'a process started 200 s after the kill'), ('sha_adv3', H['adv3_old'], 'the old adv3.py'),
                            ('daily_line', True, 'a daily line since the mark'), ('procs', [11, 12], 'a second process under the argv')):
        ok(not all(unit_checks('new', pre, dict(now, **{key: val})).values()), 'unit_checks: %s reads FAIL' % label)
    moved = {u: dict(c, NRestarts='1') for u, c in pre['caps'].items()}
    ok(not all(unit_checks('new', pre, dict(now, caps=moved)).values()), 'unit_checks: a capture unit restarted reads FAIL')
    ok(all(unit_checks('old', pre, dict(now, sha_adv3=H['adv3_old'])).values()), 'unit_checks: the rollback reads the old adv3.py')
    log = ('2026-10-31T06:00:01Z daily sent for the close of 2026-10-30\n2026-10-31T09:00:00Z serving the pinned chat: pid 11 offset 5 daily-sent 2026-10-31\n'
           'Traceback (most recent call last):\n')
    t = calendar.timegm(time.strptime('2026-10-31T08:59:59', '%Y-%m-%dT%H:%M:%S'))
    jl = '{"kind": "daily", "x": 1}\n{"kind": "request"}\nnot json\n{"kind": "daily"}\n'
    ok(daily_records(jl) == 2 and daily_records('') == 0, 'daily_records: the daily kind counted, requests and a broken line left out')
    ok(log_since(log, t, 11) == (True, False, True), 'log_since: serving found, the earlier daily left out, a later traceback found')
    ok(log_since(log, t, 12) == (False, False, True), 'log_since: another pid does not serve')
    ok(all(number_reading(['CryptoTZ/' + 'TZ-36-advisor-trust-block.md', 'CryptoTZ/TZ-35-x.md']).values()), 'number: the one file reads PASS')
    ok(not all(number_reading(['CryptoTZ/TZ-36-advisor-trust-block.md', 'CryptoTZ/TZ-36-other.md']).values()), 'number: two files of the number read FAIL')
    ok(not all(number_reading(['CryptoTZ/TZ-36-advisor-trust-block.md', 'CryptoReports/TZ-36-x-report.md']).values()), 'number: a report of the number reads FAIL')
    import tempfile
    saved_work = WORK
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(tmp + '/logs/sub')
        for rel in ('state.json', 'history.json', 'adv3.before', 'logs/01-a.log', 'logs/sub/02-b.log', 'wt-not-kept.txt', 'stage-not-kept.txt'):
            with open(tmp + '/' + rel, 'w') as fh:
                fh.write(rel)
        globals().update(WORK=tmp)
        try:
            kept = kept_files()
        finally:
            globals().update(WORK=saved_work)
    ok(kept == ['adv3.before', 'history.json', 'logs/01-a.log', 'logs/sub/02-b.log', 'state.json'],
       'kept_files: the named files and the logs, nothing else, commit.before absent where not written')
    out('SELFTEST PASS: %d of %d checks passed' % (len(done), len(done)))


def main(argv):
    if not argv:
        sys.exit('usage: tz36-advisor-trust.py MODE [ARG]')
    mode, rest = argv[0], argv[1:]
    table = {'fingerprint': mode_fingerprint, 'host': mode_host, 'number': mode_number, 'rule': mode_rule,
             'copy': mode_copy, 'render': mode_render, 'keep': mode_keep, 'stopped': mode_stopped,
             'selftest': mode_selftest}
    try:
        if mode == 'mark':
            assert len(rest) == 1, 'mark deploy|kill|rollback|kill2'
            mode_mark(rest[0])
        elif mode == 'unit':
            assert len(rest) == 1, 'unit new|old'
            mode_unit(rest[0])
        else:
            assert mode in table and not rest, 'unknown mode %r' % (argv,)
            table[mode]()
    except NotYet:
        out('NOT YET')
        return 3
    except Failed:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
