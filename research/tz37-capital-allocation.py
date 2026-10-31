#!/usr/bin/env python3
# tz37-capital-allocation.py - TZ-37's checker: the fingerprint, the host gate, the number, G-RULE, COPY, G-RENDER, the
# readings after the unit's restart, and the marks. Standard library only. It starts and stops no
# unit, signals no process and sends no request of its own (G-RENDER runs the service copy's bot, which reads
# Binance's public market), and it never reads or prints the bot's token or the pinned chat. Exits: 0 every assert
# held; 1 a failed assert, named; 3 NOT YET.
import ast, calendar, contextlib, hashlib, importlib.util, io, json, math, os, re, shutil, subprocess, sys, time

WORK = '/root/tz37-work'
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
TZ_FILE = 'CryptoTZ/TZ-37-capital-allocation.md'
NUMBER = 'TZ-37-'
BRANCH = 'tz-37-capital-allocation'
MAP_REV = '2026-10-31-a'
ANCHORS = {'A1': '229a944f2d51', 'A2': '6c5089330629',
           'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable',
           'A4': '437b45ea196b', 'A5': '0f6c90451cbd', 'A6': '729f0bcdbee3'}
DERIVED = {'A2': 'research/twap-divergence.py', 'A4': 'BTC-EXECUTOR-INSTRUCTIONS.md',
           'A5': 'research/recorder/recorder.py', 'A6': 'research/pfair.py'}
H = {'adv3': 'd73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8',
     'selftest': 'ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395',
     'bot_old': 'e65de91c7b49c6f932db91e568a5956c005e63119c1cf6fb8724ffb0438d1dcb',
     'bot_new': '3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2',
     'rule': 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169',
     'unit': '82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66'}
BOT_CHANGED = {'selftest', 'handle', 'journal'}
BOT_ADDED = {'plan_parts', 'correlation', 'numbers', 'returns_of', 'liquidity', 'plan', 'route'}
BOT_REMOVED = {'parse'}
BOT_SAME = ('Data', 'Telegram', 'chunks', 'find_chat', 'hello', 'log', 'main', 'make', 'malloc_tune', 'probe', 'put', 'read', 'serve')
BOT_CONST = ({'HELP'}, {'HEAD', '(STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS)', 'TOPN', 'OPEN'}, {'CMD'})
STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, RISK_MAX, RISK_ALL = 11.1, 5.0, 0.001, 1.0, 5.0
MEM_FLOOR, DISK_FLOOR = 130_981_888, 7_400_000_000
ROWS, FROZEN = 56, 53
RENDER_CASES = ('сигнал', 'сигнал 10000 топ 3', 'сигнал 15000 топ 5', 'сигнал 10000', 'помощь', 'привет')
RENDER_KINDS = ['request', 'alloc', 'alloc', 'alloc']
TRUST = ('Оценка доверия', 'Надёжность системы: <b>1/5</b>', 'Уверенность в сделках:', 'STRONG обоснован: <b>нет</b>',
         'Качество данных: <b>низкое</b>', 'Ожидаемая R на сделку: <b>не установлена</b>', 'Инвалидация: у каждой карточки')
BOOK = ('Форвард с 28.10', 'Все сигналы: входов', 'STRONG: входов')
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


def sh_try(args, **kw):
    """sh, where a command the host lacks is a reading of its own and not a crash: (127, '', why)."""
    try:
        return sh(args, **kw)
    except OSError as e:
        return 127, '', repr(e)


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
    stat_text = read('/proc/%s/stat' % pid)
    fields = stat_text[stat_text.rindex(')') + 2:].split()
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
    """{name: ast.dump} of a module's functions and classes, and of its assignments keyed by their targets."""
    defs, asg = {}, {}
    for n in ast.parse(src).body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            defs[n.name] = ast.dump(n)
        elif isinstance(n, ast.Assign):
            asg[','.join(ast.unparse(t) for t in n.targets)] = ast.dump(n)
    return defs, asg


def bot_checks(old_src, new_src):
    """G-RULE's last three checks: the two adv3-bot.py files differ in exactly the definitions and constants TZ-37 names."""
    (od, oa), (nd, na) = top_level(old_src), top_level(new_src)
    changed = {k for k in od if k in nd and od[k] != nd[k]}
    return {
        'the functions and classes that changed are exactly %s' % sorted(BOT_CHANGED): changed == BOT_CHANGED,
        'the added are exactly %s and the removed are %s' % (sorted(BOT_ADDED), sorted(BOT_REMOVED)):
            set(nd) - set(od) == BOT_ADDED and set(od) - set(nd) == BOT_REMOVED,
        'the %d others are identical by AST and the constants differ as named' % len(BOT_SAME):
            all(k in od and k in nd and od[k] == nd[k] for k in BOT_SAME)
            and ({k for k in oa if k in na and oa[k] != na[k]}, set(na) - set(oa), set(oa) - set(na)) == BOT_CONST,
    }


def html_balanced(text):
    return all(text.count('<%s>' % t) == text.count('</%s>' % t) for t in ('b', 'i'))


def plan_invariants(p, rep, liq, budget, n):
    """The allocation's limits, read from a plan (the bot's own) and the report and liquidity it was made from. The limits
    are this checker's, the TZ's: stop 11.1 %, minimum 5 USDT, liquidity 0.1 %, risk 1 % a trade and 5 % in all, three places."""
    items = p['items']
    coins = [it['card']['coin'] for it in items]
    strong = [c for c in rep['top'] if c in rep['strong']]
    named = [r[0] for r in p['rejected']]
    return {
        'only STRONG coins of the report, in rank order, at most n and at most three, none added to fill': (
            set(coins) <= set(strong) and coins == [c for c in strong if c in coins] and len(coins) <= min(n, 3)),
        'every STRONG coin is in the plan or named with a reason, once': sorted(coins + named) == sorted(strong),
        'every position has an entry and a stop within 11.1 % of it, on current prices': (
            all(it['card']['entry'] is not None and it['card']['stop_pct'] <= STOP_MAX for it in items)
            and (rep['marks_ok'] or not items)),
        'each loss at its stop within 1 % of the budget, all together within 5 %': (
            all(it['loss_exact'] <= budget * RISK_MAX / 100 + 1e-9 for it in items)
            and sum(it['loss_exact'] for it in items) <= budget * RISK_ALL / 100 + 1e-9),
        'whole positions of at least 5 USDT, together within the budget, free the budget less them': (
            all(float(it['notional']).is_integer() and it['notional'] >= MIN_NOTIONAL for it in items)
            and p['allocated'] == sum(it['notional'] for it in items) <= budget and p['free'] == budget - p['allocated']),
        'leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap': all(
            it['leverage'] == min(20, math.floor(1 / (1.5 * it['card']['stop_pct'] / 100 + 0.01)))
            and it['margin'] * it['leverage'] >= it['notional']
            and ((not liq.get(it['card']['coin'])) or it['notional'] <= LIQ_FRAC * liq[it['card']['coin']]) for it in items),
    }


def render_checks(texts, calc, plain, kinds, records, log, same, expect):
    """G-RENDER: what the service copy's bot sent for each command (texts, by command), the plan the checker recomputed from
    the report and liquidity each allocation reply was made from (calc, by command), the plain report, the scratch journal's kinds and
    records, the bot's log, whether the bot's own record is as before, and what the bot module holds (expect); counts and labels only."""
    sig, hlp, hi = texts[RENDER_CASES[0]], texts[RENDER_CASES[4]], texts[RENDER_CASES[5]]
    whole = lambda parts: '\n'.join(parts)
    allocs = [c for c in RENDER_CASES if c in calc]
    usdt = expect['usdt']
    inv = {c: plan_invariants(calc[c]['plan'], calc[c]['rep'], calc[c]['liq'], calc[c]['budget'], calc[c]['n']) for c in allocs}

    def fields(c):
        p, t = calc[c]['plan'], whole(texts[c])
        head = ('не доказанная' in t and 'Бюджет %s USDT' % expect['num'](p['budget'], 6) in t and 'Размещено %s USDT' % usdt(p['allocated']) in t
                and ('Свободно %s USDT' % usdt(p['free']) in t or 'свободно %s USDT' % usdt(p['free']) in t))
        if not p['items']:
            return head and 'Подходящих сделок нет' in t
        k = len(p['items'])
        return (head and 'Подходящих сделок: %d из %d запрошенных' % (k, p['n']) in t
                and all(t.count(m) == k for m in ('Капитал:', 'плечо', 'Потеря на стопе:', '⛔ Стоп:', 'Инвалидация: цена', 'Качество: z')) and t.count('маржа') == k + 1
                and t.count('🎯') == 3 * k and 'Потеря на стопах %s USDT' % usdt(p['loss']) in t and 'маржа %s USDT' % usdt(p['margin']) in t)

    n = len(CARD.findall(whole(sig)))
    sixth = RENDER_CASES[3]
    return {
        'every command answered, no traceback and no failed request in the bot\'s log':
            all(texts[k] for k in RENDER_CASES) and 'Traceback' not in log and 'request failed' not in log,
        'the markup is balanced in every message (b, i)': all(html_balanced(t) for ps in texts.values() for t in ps),
        '«сигнал»: the six ratings and the forward book, at most three cards, each with its basis and invalidation, in at most three parts':
            all(k in whole(sig) for k in TRUST + BOOK) and n <= 3 and whole(sig).count('Основание: сумма знаков') == n
            and whole(sig).count('Инвалидация: цена') == n and len(sig) <= 3,
        'the allocation\'s constants are the TZ\'s: 11.1 % a stop, 5 USDT, 0.1 % of the volume, 1 % and 5 % of risk, three places, 0.1 % a side':
            expect['consts'] == (STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, RISK_MAX, RISK_ALL, 3, 0.001),
        'each allocation reply is the bot\'s own plan_parts of the report and liquidity it was made from':
            len(allocs) == 3 and all(texts[c] == calc[c]['parts'] for c in allocs),
        'plan: only STRONG coins of the report, in rank order, at most n and at most three, none added to fill':
            all(v['only STRONG coins of the report, in rank order, at most n and at most three, none added to fill'] for v in inv.values()),
        'plan: every STRONG coin is in the plan or named with a reason, once':
            all(v['every STRONG coin is in the plan or named with a reason, once'] for v in inv.values()),
        'plan: every position has an entry and a stop within 11.1 % of it, on current prices':
            all(v['every position has an entry and a stop within 11.1 % of it, on current prices'] for v in inv.values()),
        'plan: each loss at its stop within 1 % of the budget, all together within 5 %':
            all(v['each loss at its stop within 1 % of the budget, all together within 5 %'] for v in inv.values()),
        'plan: whole positions of at least 5 USDT, together within the budget, free the budget less them':
            all(v['whole positions of at least 5 USDT, together within the budget, free the budget less them'] for v in inv.values()),
        'plan: leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap':
            all(v['leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap'] for v in inv.values()),
        'the Boss\'s fields are in every allocation reply: budget, qualifying count, allocated, free, and for each trade capital, leverage, margin, loss at the stop, stop, targets, invalidation, and the note that the sizes are unproven':
            len(allocs) == 3 and all(fields(c) for c in allocs),
        '«сигнал 10000» is the three-trade view and «сигнал 15000 топ 5» says that STRONG is at most three':
            len(allocs) == 3 and 'до 3 сделок' in whole(texts[sixth]) and calc[sixth]['n'] == 3 and calc[sixth]['budget'] == 10000.0
            and 'больше 3 сделок не будет' in whole(texts[RENDER_CASES[2]]) and 'Бюджет 15 000 USDT' in whole(texts[RENDER_CASES[2]]),
        '«помощь» and an unknown text answer HELP and nothing else': hlp == [expect['help']] and hi == [expect['help']],
        'the scratch journal holds, in order, request, alloc, alloc, alloc, each allocation record with its plan\'s figures': kinds == RENDER_KINDS and len(allocs) == 3 and all(
            r['alloc']['allocated'] == calc[c]['plan']['allocated'] and r['alloc']['free'] == calc[c]['plan']['free']
            and [i['coin'] for i in r['alloc']['items']] == [it['card']['coin'] for it in calc[c]['plan']['items']]
            for r, c in zip(records[1:], allocs)),
        'the bot\'s own journal and daily-sent are as before the run': same is True,
    }


def unit_checks(which, pre, now):
    """The readings after a restart: now is what the modes read; pre is the snapshot of the mark before the kill."""
    want_bot = H['bot_new'] if which == 'new' else H['bot_old']
    return {
        'the unit is active, running and enabled': (now['bot']['ActiveState'], now['bot']['SubState'],
                                                    now['bot']['UnitFileState']) == ('active', 'running', 'enabled'),
        'a new MainPID, one restart more': int(now['bot']['MainPID']) not in (0, int(pre['bot']['MainPID']))
        and int(now['bot']['NRestarts']) == int(pre['bot']['NRestarts']) + 1,
        'the process started after the kill mark and within 90 s of it': pre['t'] <= now['start'] <= pre['t'] + 90,
        'the process runs the unit\'s exact argv, alone': now['argv'] == ARGV and now['procs'] == [int(now['bot']['MainPID'])],
        'the service copy\'s adv3-bot.py is the %s one, and the process started after the copy' % which:
            now['sha_bot'] == want_bot and now['start'] > now['copy_t'],
        'the service copy\'s adv3.py and the unit file are unchanged': now['sha_adv3'] == H['adv3'] and now['sha_unit'] == H['unit'],
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


def memory_gate(first, second):
    """The memory gate: MemAvailable at the first read, and at the second, 60 s later, taken only where the first fell
    below MEM_FLOOR; the second decides. Returns (passes, the read that decided)."""
    final = first if first >= MEM_FLOOR or second is None else second
    return final >= MEM_FLOOR, final


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


def meminfo():
    return {k: int(v.split()[0]) * 1024 for k, v in (l.split(':', 1) for l in read('/proc/meminfo').splitlines())}


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
    checks['H5 adv3.py is TZ-36\'s and adv3-bot.py is TZ-35\'s'] = (
        sha256_file(SVC + '/adv3.py') == H['adv3'] and sha256_file(SVC + '/adv3-bot.py') == H['bot_old'])
    checks['H5 the installed unit file is TZ-35\'s'] = sha256_file('/etc/systemd/system/adv3-bot.service') == H['unit']
    checks['H5 commit.txt is 40 hex characters and a newline'] = re.fullmatch(r'[0-9a-f]{40}\n', read(SVC + '/commit.txt')) is not None
    checks['H6 the record holds daily-sent and a journal of whole lines'] = (
        re.fullmatch(r'\d{4}-\d{2}-\d{2}\n?', read(BOTDIR + '/daily-sent')) is not None
        and read(BOTDIR + '/journal.jsonl', 'rb').endswith(b'\n'))
    first = meminfo()['MemAvailable']
    second = None
    if first < MEM_FLOOR:
        out('MemAvailable %d bytes, below %d: read again after 60 s' % (first, MEM_FLOOR))
        time.sleep(60)
        second = meminfo()['MemAvailable']
    passes, final = memory_gate(first, second)
    checks['memory gate: MemAvailable at least %d bytes, a first read below it read again after 60 s' % MEM_FLOOR] = passes
    checks['disk gate: /dev/vda2 free at least %d bytes' % DISK_FLOOR] = int(avail) >= DISK_FLOOR
    out('units:', json.dumps(units, sort_keys=True))
    out('MemAvailable first %d bytes, second %s, deciding %d; /dev/vda2 free %s bytes' % (
        first, 'not read' if second is None else second, final, avail))
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
    same = {}
    for key, path in (('adv3', 'advisor/adv3.py'), ('selftest', 'advisor/selftest-adv3.py'),
                      ('unit', 'deploy/systemd/adv3-bot.service')):
        b = read(WT + '/' + path, 'rb')
        same[key] = b == git_show(path).encode() and sha256_bytes(b) == H[key]
    rule_txt = read(WT + '/advisor/RULE-ADV-3.txt', 'rb')
    checks = {
        'adv3.py is main\'s, byte for byte, and hashes to TZ-36\'s': same['adv3'],
        'selftest-adv3.py is main\'s, byte for byte, and hashes to TZ-36\'s': same['selftest'],
        'RULE-ADV-3.txt is main\'s, hashes to the RULE constant and is adv3.py\'s':
            rule_txt == git_show('advisor/RULE-ADV-3.txt').encode() and sha256_bytes(rule_txt) == H['rule']
            and ("RULE = '%s'" % H['rule']) in read(WT + '/advisor/adv3.py'),
        'the unit file is main\'s, byte for byte, and hashes to TZ-35\'s': same['unit'],
    }
    checks.update(bot_checks(git_show('advisor/adv3-bot.py'), read(WT + '/advisor/adv3-bot.py')))
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
    rc2, up, _ = sh(['git', '-C', WT, 'rev-parse', 'origin/' + BRANCH])
    commit = read(SVC + '/commit.txt')
    verdict('COPY', {
        'the service copy holds adv3.py, adv3-bot.py and commit.txt only': sorted(os.listdir(SVC)) == ['adv3-bot.py', 'adv3.py', 'commit.txt'],
        'adv3.py is unchanged, TZ-36\'s': sha256_file(SVC + '/adv3.py') == H['adv3'],
        'adv3-bot.py is Appendix A\'s': sha256_file(SVC + '/adv3-bot.py') == H['bot_new'],
        'commit.txt is the branch head and the worktree\'s HEAD': (
            re.fullmatch(r'[0-9a-f]{40}\n', commit) is not None and rc == 0 and rc2 == 0 and commit.strip() == head.strip() == up.strip()),
        'the branch\'s adv3-bot.py equals the service copy\'s': read(WT + '/advisor/adv3-bot.py', 'rb') == read(SVC + '/adv3-bot.py', 'rb'),
    })


def mode_render():
    saved = list(sys.path)
    sys.path.insert(0, SVC)
    try:
        spec = importlib.util.spec_from_file_location('advbot', SVC + '/adv3-bot.py')
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    scratch = WORK + '/render-state'
    os.makedirs(scratch, exist_ok=True)
    mod.STATE = scratch
    own = (sha256_file(BOTDIR + '/journal.jsonl'), sha256_file(BOTDIR + '/daily-sent'))

    class Cap(mod.Telegram):
        def __init__(self):
            super().__init__('123456:SECRET', 777)
            self.texts = []

        def call(self, method, http_timeout=30, **params):
            self.texts.append(params['text'])
            return {'message_id': len(self.texts)}

    cap, data, texts, calc, seen, liqs = Cap(), mod.Data(), {}, {}, [], {}
    real_make, real_liq = mod.make, mod.liquidity

    def make_seen(d, deposit, risk):
        out_ = real_make(d, deposit, risk)
        seen.append(out_[0])
        return out_

    def liq_seen(coin, now_ms):
        liqs[coin] = real_liq(coin, now_ms)
        return liqs[coin]

    mod.make, mod.liquidity = make_seen, liq_seen
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            for case in RENDER_CASES:
                n0, m0 = len(cap.texts), len(seen)
                liqs.clear()
                mod.handle(cap, data, case)
                texts[case] = cap.texts[n0:]
                cmd = mod.route(case)
                if cmd and cmd[0] == 'alloc' and len(seen) == m0 + 1:
                    _kind, budget, n, risk = cmd
                    p = mod.plan(seen[-1], data.cs, budget, n, risk, dict(liqs))
                    calc[case] = {'rep': seen[-1], 'liq': dict(liqs), 'plan': p, 'budget': budget, 'n': n, 'risk': risk,
                                  'parts': mod.plan_parts(seen[-1], p)}
    finally:
        mod.make, mod.liquidity = real_make, real_liq
    records = []
    if os.path.exists(scratch + '/journal.jsonl'):
        records = [json.loads(line) for line in read(scratch + '/journal.jsonl').splitlines()]
    same = own == (sha256_file(BOTDIR + '/journal.jsonl'), sha256_file(BOTDIR + '/daily-sent'))
    out('replies: %s; the bot\'s log: %d lines; STRONG coins of the report: %d; trades placed: %s' % (
        ', '.join('%d chars in %d parts' % (sum(map(len, texts[k])), len(texts[k])) for k in RENDER_CASES), buf.getvalue().count('\n'),
        len(seen[0]['strong']) if seen else -1, ', '.join(str(len(calc[c]['plan']['items'])) for c in calc)))
    expect = {'help': mod.HELP, 'usdt': mod.adv3.usdt, 'num': mod.adv3.num,
              'consts': (mod.STOP_MAX, mod.MIN_NOTIONAL, mod.LIQ_FRAC, mod.adv3.RISK_MAX, mod.adv3.RISK_ALL, mod.adv3.TOP_N, mod.adv3.COST)}
    verdict('RENDER', render_checks(texts, calc, seen[0] if seen else None, [r['kind'] for r in records], records, buf.getvalue(), same, expect))


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
    """The work tree's files a report keeps by name: state.json, the two files B-DEPLOY saves, and every file under
    logs/; relative to WORK, sorted."""
    names = ['state.json', 'bot.before', 'commit.before']
    for d, _s, fs in os.walk(WORK + '/logs'):
        names += [os.path.relpath(os.path.join(d, f), WORK) for f in fs]
    return sorted(n for n in names if os.path.isfile(os.path.join(WORK, n)))


def mode_keep():
    """B-RECLAIM-OWN's copy: every kept file into the forensic store as tz37-work--<path with - for />, by exclusive
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
        dest = FORENSICS + '/tz37-work--' + rel.replace('/', '--')
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
    old = ('X = 1\nHELP = 1\ndef a():\n    return 1\ndef b():\n    return 2\nclass K:\n    def m(self):\n        return 1\n'
           'class T:\n    x = 1\nCMD = 5\n')
    new_ok = ('X = 1\nHELP = 2\ndef a():\n    return 1\ndef b():\n    return 3\nclass K:\n    def m(self):\n        return 1\n'
              'class T:\n    x = 2\nnewfn = 0\ndef c():\n    return 0\n')
    saved = (BOT_CHANGED, BOT_ADDED, BOT_REMOVED, BOT_SAME, BOT_CONST)
    globals().update(BOT_CHANGED={'b', 'T'}, BOT_ADDED={'c'}, BOT_REMOVED=set(), BOT_SAME=('a', 'K'),
                     BOT_CONST=({'HELP'}, {'newfn'}, {'CMD'}))
    try:
        good = bot_checks(old, new_ok)
        ok(all(good.values()) and len(good) == 3, 'bot_checks: exactly the named definitions and constants differ, 3 of 3')
        ok(not all(bot_checks(old, new_ok.replace('def a():\n    return 1', 'def a():\n    return 9')).values()),
           'bot_checks: a changed function that should be the same reads FAIL')
        ok(not all(bot_checks(old, new_ok.replace('class T:\n    x = 2', 'class T:\n    x = 1')).values()),
           'bot_checks: a function that should have changed and did not reads FAIL')
        ok(not all(bot_checks(old, new_ok + 'def d():\n    return 0\n').values()), 'bot_checks: an extra function reads FAIL')
        ok(not all(bot_checks(old, new_ok.replace('X = 1', 'X = 2')).values()), 'bot_checks: a changed constant not named reads FAIL')
    finally:
        globals().update(BOT_CHANGED=saved[0], BOT_ADDED=saved[1], BOT_REMOVED=saved[2], BOT_SAME=saved[3], BOT_CONST=saved[4])
    # ---- G-RENDER on stand-ins: a plan, the replies made from it, and the reports around them
    usdt = lambda x: f'{round(x):,}'.replace(',', ' ')
    num = lambda x, sig=3: f'{x:,.0f}'.replace(',', ' ')
    expect = {'help': 'HELP', 'usdt': usdt, 'num': num, 'consts': (STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, RISK_MAX, RISK_ALL, 3, 0.001)}

    def item(coin, side, stop, notional, margin, loss, exact, capped=False):
        return {'card': {'coin': coin, 'side': side, 'entry': 100.0, 'stop_pct': stop}, 'notional': notional,
                'leverage': min(20, math.floor(1 / (1.5 * stop / 100 + 0.01))), 'margin': margin, 'loss': loss, 'loss_exact': exact, 'capped': capped}

    def make_plan(budget, n, items, rejected):
        alloc = sum(i['notional'] for i in items)
        return {'budget': budget, 'n': n, 'items': items, 'rejected': rejected, 'allocated': alloc, 'free': budget - alloc,
                'margin': sum(i['margin'] for i in items), 'loss': sum(i['loss'] for i in items), 'loss_exact': sum(i['loss_exact'] for i in items)}

    def render(p, extra=''):
        first = ['Бюджет %s USDT · до %d сделок' % (num(p['budget']), p['n']), 'Подходящих сделок: %d из %d запрошенных' % (len(p['items']), p['n'])
                 if p['items'] else 'Подходящих сделок нет',
                 'Размещено %s USDT · маржа %s USDT' % (usdt(p['allocated']), usdt(p['margin'])),
                 'Потеря на стопах %s USDT' % usdt(p['loss']), 'Свободно %s USDT' % usdt(p['free']), extra]
        for it in p['items']:
            first += ['Качество: z +2', '⛔ Стоп: 1', '🎯 1', '🎯 2', '🎯 3', 'Капитал: %s USDT · плечо %d× изол. · маржа %s USDT' % (usdt(it['notional']), it['leverage'], usdt(it['margin'])),
                      'Потеря на стопе: %s USDT' % usdt(it['loss']), 'Инвалидация: цена ≤ 1']
        return ['\n'.join(first), '\n'.join(TRUST + ('Размеры — формула, не доказанная',))]

    rep = {'top': ['ETH', 'SOL', 'XRP', 'BTC'], 'strong': ['ETH', 'SOL', 'XRP'], 'marks_ok': True}
    p1 = make_plan(10000.0, 3, [item('ETH', 1, 8.0, 609, 87, 50, 49.938), item('XRP', 1, 10.0, 300, 50, 31, 30.6)], [('SOL', 'SHORT', 'стоп 13,0% дальше 11,1%')])
    p2 = make_plan(15000.0, 5, [item('ETH', 1, 8.0, 900, 129, 74, 73.8)], [('SOL', 'SHORT', 'стоп 13,0% дальше 11,1%'), ('XRP', 'LONG', 'стоп 12,0% дальше 11,1%')])
    p3 = make_plan(10000.0, 3, [], [('ETH', 'LONG', 'стоп 12,0% дальше 11,1%'), ('SOL', 'SHORT', 'стоп 13,0% дальше 11,1%'), ('XRP', 'LONG', 'стоп 14,0% дальше 11,1%')])
    c1, c2, c3 = RENDER_CASES[1], RENDER_CASES[2], RENDER_CASES[3]
    calc = {c1: {'rep': rep, 'liq': {}, 'plan': p1, 'budget': 10000.0, 'n': 3, 'parts': render(p1)},
            c2: {'rep': rep, 'liq': {}, 'plan': p2, 'budget': 15000.0, 'n': 5, 'parts': render(p2, 'STRONG бывает только в ТОП-3: больше 3 сделок не будет')},
            c3: {'rep': rep, 'liq': {}, 'plan': p3, 'budget': 10000.0, 'n': 3, 'parts': render(p3)}}
    plain = ['\n'.join(list(TRUST + BOOK) + ['🟢 <b>BTC · LONG</b>', 'Основание: сумма знаков +4', 'Инвалидация: цена ≤ 1'])]
    texts = {RENDER_CASES[0]: plain, c1: calc[c1]['parts'], c2: calc[c2]['parts'], c3: calc[c3]['parts'], RENDER_CASES[4]: ['HELP'], RENDER_CASES[5]: ['HELP']}
    records = [{'kind': 'request'}] + [{'kind': 'alloc', 'alloc': {'allocated': calc[c]['plan']['allocated'], 'free': calc[c]['plan']['free'],
                                                                'items': [{'coin': it['card']['coin']} for it in calc[c]['plan']['items']]}} for c in (c1, c2, c3)]
    good = render_checks(texts, calc, rep, RENDER_KINDS, records, '', True, expect)
    ok(all(good.values()) and len(good) == 16, 'render_checks: whole replies and plans read 16 of 16')

    def bad(**kw):
        a = dict(texts=texts, calc=calc, plain=rep, kinds=RENDER_KINDS, records=records, log='', same=True, expect=expect)
        a.update(kw)
        return not all(render_checks(a['texts'], a['calc'], a['plain'], a['kinds'], a['records'], a['log'], a['same'], a['expect']).values())

    def with_item(case, **changes):
        p = calc[case]['plan']
        its = [dict(p['items'][0], **changes)] + p['items'][1:]
        q = make_plan(p['budget'], p['n'], its, p['rejected'])
        return dict(calc, **{case: dict(calc[case], plan=q, parts=render(q), )}), dict(texts, **{case: render(q)})

    ok(bad(log='Traceback (most recent call last):') and bad(log='request failed'), 'render_checks: a traceback or a failed request in the bot\'s log reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: []})), 'render_checks: a command with no answer reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[4]: ['<b>HELP']})), 'render_checks: unbalanced markup reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [plain[0].replace('Оценка доверия', '')]})), 'render_checks: a «сигнал» without its rating block reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [plain[0] + '\n🔴 <b>SOL · SHORT</b>']})), 'render_checks: a card without its basis reads FAIL')
    ok(bad(expect=dict(expect, consts=(12.0,) + expect['consts'][1:])), 'render_checks: another stop limit than 11.1 % reads FAIL')
    ok(bad(texts=dict(texts, **{c1: [calc[c1]['parts'][0] + ' ', calc[c1]['parts'][1]]})), 'render_checks: a reply that is not the plan\'s own reads FAIL')
    ok(bad(texts=dict(texts, **{c1: [calc[c1]['parts'][0].replace('Капитал:', 'Объём:', 1), calc[c1]['parts'][1]]}), calc=dict(calc, **{c1: dict(calc[c1], parts=[calc[c1]['parts'][0].replace('Капитал:', 'Объём:', 1), calc[c1]['parts'][1]])})),
       'render_checks: a trade without its capital line reads FAIL')
    for label, case, changes in (('a coin that is not STRONG in the plan', c1, {'card': {'coin': 'BTC', 'side': 1, 'entry': 100.0, 'stop_pct': 8.0}}),
                                 ('a stop beyond 11.1 %', c1, {'card': {'coin': 'ETH', 'side': 1, 'entry': 100.0, 'stop_pct': 11.2}}),
                                 ('a position without an entry', c1, {'card': {'coin': 'ETH', 'side': 1, 'entry': None, 'stop_pct': 8.0}}),
                                 ('a loss at the stop beyond 1 % of the budget', c1, {'loss_exact': 100.5}),
                                 ('a position under 5 USDT', c1, {'notional': 4}),
                                 ('a position that is not whole', c1, {'notional': 609.5}),
                                 ('a leverage that is not the rule\'s', c1, {'leverage': 12}),
                                 ('a margin that does not cover the leverage', c1, {'margin': 80}),
                                 ('a position beyond its liquidity cap', c1, {'notional': 609})):
        cc, tt = with_item(case, **changes)
        if 'liquidity' in label:
            cc = dict(cc, **{case: dict(cc[case], liq={'ETH': 100_000.0})})
        ok(bad(calc=cc, texts=tt), 'render_checks: %s reads FAIL' % label)
    q = make_plan(10000.0, 3, [item('ETH', 1, 8.0, 609, 87, 50, 49.938), item('XRP', 1, 10.0, 300, 50, 31, 90.0), item('SOL', 1, 8.0, 609, 87, 50, 95.0)], [])
    ok(bad(calc=dict(calc, **{c1: dict(calc[c1], plan=q, parts=render(q))}), texts=dict(texts, **{c1: render(q)})), 'render_checks: all losses together beyond 5 % of the budget read FAIL')
    q = make_plan(10000.0, 3, [item('ETH', 1, 8.0, 609, 87, 50, 49.938)], [])
    ok(bad(calc=dict(calc, **{c1: dict(calc[c1], plan=q, parts=render(q))}), texts=dict(texts, **{c1: render(q)})), 'render_checks: a STRONG coin neither placed nor named reads FAIL')
    unproven = lambda case: [calc[case]['parts'][0], calc[case]['parts'][1].replace('не доказанная', 'доказанная')]
    ok(bad(calc=dict(calc, **{c1: dict(calc[c1], parts=unproven(c1))}), texts=dict(texts, **{c1: unproven(c1)})), 'render_checks: a reply without the note that the sizes are unproven reads FAIL')
    ok(bad(calc=dict(calc, **{c3: dict(calc[c3], n=5)})), 'render_checks: «сигнал 10000» that is not the three-trade view reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[4]: ['HELP', 'more']})), 'render_checks: an unknown text answered by more than HELP reads FAIL')
    ok(bad(kinds=RENDER_KINDS[:-1]) and bad(kinds=['alloc'] + RENDER_KINDS[1:]), 'render_checks: a journal that lacks a record or has another kind reads FAIL')
    ok(bad(same=False), 'render_checks: the bot\'s own journal changed reads FAIL')
    pre = {'t': 1000.0, 'bot': {'MainPID': '10', 'NRestarts': '1'}, 'daily': '2026-10-31', 'journal': 7,
           'caps': {u: {'MainPID': str(i), 'NRestarts': '0', 'ActiveState': 'active'} for i, u in enumerate(CAPTURES, 20)}}
    now = {'bot': {'MainPID': '11', 'NRestarts': '2', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'},
           'caps': dict(pre['caps']), 'start': 1035.0, 'copy_t': 990.0, 'argv': ARGV, 'procs': [11], 'sha_adv3': H['adv3'],
           'sha_bot': H['bot_new'], 'sha_unit': H['unit'], 'daily': '2026-10-31', 'journal': 7, 'serving': True,
           'daily_line': False, 'traceback': False}
    ok(all(unit_checks('new', pre, now).values()) and len(unit_checks('new', pre, now)) == 9, 'unit_checks: a clean restart reads 9 of 9')
    for key, val, label in (('daily', '2026-11-01', 'a daily-sent changed'), ('journal', 8, 'a message sent again'),
                            ('start', 1200.0, 'a process started 200 s after the kill'), ('sha_bot', H['bot_old'], 'the old bot'),
                            ('sha_adv3', 'x', 'another adv3.py'), ('daily_line', True, 'a daily line since the mark'),
                            ('procs', [11, 12], 'a second process under the argv')):
        ok(not all(unit_checks('new', pre, dict(now, **{key: val})).values()), 'unit_checks: %s reads FAIL' % label)
    moved = {u: dict(c, NRestarts='1') for u, c in pre['caps'].items()}
    ok(not all(unit_checks('new', pre, dict(now, caps=moved)).values()), 'unit_checks: a capture unit restarted reads FAIL')
    ok(all(unit_checks('old', pre, dict(now, sha_bot=H['bot_old'])).values()), 'unit_checks: the rollback reads the old bot')
    log = ('2026-10-31T06:00:01Z daily sent for the close of 2026-10-30\n2026-10-31T09:00:00Z serving the pinned chat: pid 11 offset 5 daily-sent 2026-10-31\n'
           'Traceback (most recent call last):\n')
    t = calendar.timegm(time.strptime('2026-10-31T08:59:59', '%Y-%m-%dT%H:%M:%S'))
    jl = '{"kind": "daily", "x": 1}\n{"kind": "request"}\nnot json\n{"kind": "daily"}\n'
    ok(daily_records(jl) == 2 and daily_records('') == 0, 'daily_records: the daily kind counted, requests and a broken line left out')
    ok(log_since(log, t, 11) == (True, False, True), 'log_since: serving found, the earlier daily left out, a later traceback found')
    ok(log_since(log, t, 12) == (False, False, True), 'log_since: another pid does not serve')
    ok(memory_gate(MEM_FLOOR, None) == (True, MEM_FLOOR) and memory_gate(MEM_FLOOR - 1, MEM_FLOOR) == (True, MEM_FLOOR)
       and memory_gate(MEM_FLOOR - 1, MEM_FLOOR - 2) == (False, MEM_FLOOR - 2) and memory_gate(MEM_FLOOR - 1, None) == (False, MEM_FLOOR - 1),
       'memory_gate: a first read at the floor passes, a first read below it is decided by the second')
    ok(all(number_reading(['CryptoTZ/' + 'TZ-37-capital-allocation.md', 'CryptoTZ/TZ-36-x.md']).values()), 'number: the one file reads PASS')
    ok(not all(number_reading(['CryptoTZ/TZ-37-capital-allocation.md', 'CryptoTZ/TZ-37-other.md']).values()), 'number: two files of the number read FAIL')
    ok(not all(number_reading(['CryptoTZ/TZ-37-capital-allocation.md', 'CryptoReports/TZ-37-x-report.md']).values()), 'number: a report of the number reads FAIL')
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(tmp + '/logs/sub')
        for rel in ('state.json', 'bot.before', 'logs/01-a.log', 'logs/sub/02-b.log', 'wt-not-kept.txt', 'history.json'):
            with open(tmp + '/' + rel, 'w') as fh:
                fh.write(rel)
        saved_work = WORK
        globals().update(WORK=tmp)
        try:
            kept = kept_files()
        finally:
            globals().update(WORK=saved_work)
    ok(kept == ['bot.before', 'logs/01-a.log', 'logs/sub/02-b.log', 'state.json'],
       'kept_files: the named files and the logs, nothing else, commit.before absent where not written')
    out('SELFTEST PASS: %d of %d checks passed' % (len(done), len(done)))


def main(argv):
    if not argv:
        sys.exit('usage: tz37-capital-allocation.py MODE [ARG]')
    mode, rest = argv[0], argv[1:]
    table = {'fingerprint': mode_fingerprint, 'host': mode_host, 'number': mode_number, 'rule': mode_rule,
             'copy': mode_copy, 'render': mode_render, 'keep': mode_keep, 'stopped': mode_stopped, 'selftest': mode_selftest}
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
