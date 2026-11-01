#!/usr/bin/env python3
# tz39-advisor-checks.py - TZ-39's checker: the fingerprint, the host gate, the number, G-RULE, COPY, G-RENDER, the readings
# after the unit's restart - UNIT-NEW and G-FIRST - and the marks. Standard library only. It starts and stops no unit, signals no
# process and sends no request of its own (G-RENDER runs the service copy's bot, which reads Binance's public market), and it
# never reads or prints the bot's token or the pinned chat, a coin, a price or a size. Exits: 0 every assert held; 1 a failed
# assert, named; 3 NOT YET.
import ast, bisect, calendar, contextlib, datetime as dt, hashlib, importlib.util, io, json, math, os, re, shutil, subprocess, \
    sys, time

WORK = '/root/tz39-work'
WT = WORK + '/wt'
STATE = WORK + '/state.json'
SCRATCH = WORK + '/render-state'
PRIMARY = '/root/btc-5m-twap'
FORENSICS = '/root/btc-forensics'
SVC = '/root/adv3-bot-svc'
BOTDIR = '/var/lib/adv3-bot'
PY = '/root/tz04a-env/venv/bin/python'
ARGV = [PY, '-B', '-u', SVC + '/adv3-bot.py', '--serve']
BOT = 'adv3-bot.service'
CAPTURES = ('btc-recorder.service', 'btc-pairbook.service', 'btc-rewardbook.service')
TZ_FILE = 'CryptoTZ/TZ-39-advisor-checks.md'
NUMBER = 'TZ-39-'
BRANCH = 'tz-39-advisor-checks'
MAP_REV = '2026-10-31-c'
ANCHORS = {'A1': '229a944f2d51', 'A2': '6c5089330629',
           'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable',
           'A4': '437b45ea196b', 'A5': '0f6c90451cbd', 'A6': '729f0bcdbee3'}
DERIVED = {'A2': 'research/twap-divergence.py', 'A4': 'BTC-EXECUTOR-INSTRUCTIONS.md',
           'A5': 'research/recorder/recorder.py', 'A6': 'research/pfair.py'}
H = {'adv3_old': 'd73a657ef31decad276b858c4ec9672dce1c1c5cec36f0bb1c5b3378838224a8',
     'adv3_new': 'c19572dccf30a505342ca334e42c7ec347a5d29db4db20887229d2a8c7b48e31',
     'bot_old': '3a044d50f51b16563b99bf1514ef92f35a9795b1fcc377aea6be4c23a31f7af2',
     'bot_new': 'ca989b6fe487d41181b32312418d6acda1e9c64fbf5cfbb3f041d54826dd108f',
     'selftest_old': 'ef4ffc44e6f8bcdd5685fc1db9090957890c6e2ab762cdad8ae9826b18cf1395',
     'selftest_new': '09d2ba9a8361ec5ebc7f5934ebb818d1a685bb16fb3f32b7da94409d9516cc0e',
     'rule': 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169',
     'unit': '82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66'}
TZ38 = ('CryptoReports/TZ-38-adv3-pit-validation-report.md', 'f4a0ac3f643ac99dd08f20c8c8c43bf1e98e51b2954592d1456a59ae98030528')
# G-RULE's tables: (changed, added, removed) definitions and assignments of each file against origin/main's
ADV3_DEFS = ({'card_lines', 'message', 'trust_lines'}, {'assessment', 'changes'}, set())
ADV3_RULE = ('signs', 'signal', 'strength', 'true_range', 'unit', 'open_at', 'hold', 'close_at', 'simulate', 'states', 'ranking',
             'simulate_strong', 'stats', 'funding_of')
ADV3_ASG = (set(), {'PIT', 'LADDER'}, set())
BOT_DEFS = ({'Telegram', 'handle', 'hello', 'make', 'plan_parts', 'probe', 'route', 'selftest', 'serve'},
            {'alerted', 'alerts_of', 'append', 'base_record', 'candidate_lines', 'candidates', 'check', 'check_record', 'compose',
             'done_after', 'due', 'event_lines', 'follow', 'followed_lines', 'forming_candles', 'hhmm', 'item_lines',
             'journal_records', 'journal_scan', 'latest_slot', 'live_report', 'next_at', 'offers', 'quiet_line', 'ranked', 'slot_at',
             'slot_key', 'slot_parse', 'slot_text', 'strong_shares', 'top_n', 'weak_lines', 'weakened', 'zone_lines', 'zones_left'},
            {'journal'})
BOT_ASG = ({'(STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, CROWD, Z_CAP, LIQ_DAYS)', 'HELP'},
           {'(SIDE, DOT)', 'ASSESS', 'BATUMI', 'CARD_KEYS', 'FOOTER', 'LIST_MAX', 'SLOTS'}, {'DAILY'})
# this TZ's numbers: the allocation's limits, the list's length, the two checks' instants, the rung
STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, RISK_MAX, RISK_ALL, LIST_MAX, RUNG = 14.0, 5.0, 0.001, 1.0, 5.0, 7, 1
SLOTS = (('signal', dt.time(0, 10)), ('fact', dt.time(12, 10)))
MEM_FLOOR, DISK_FLOOR = 130_981_888, 7_400_000_000
ROWS, FROZEN = 58, 55
FIRST_BOUND = 900
RENDER_CASES = ('сигнал', 'сигнал топ 7', 'сигнал 10000 топ 3', 'сигнал 15000 топ 5', 'оценка', 'помощь', 'привет')
RENDER_KINDS = ['request', 'request', 'alloc', 'alloc', 'assess', 'check', 'check']
TRUST = ('Оценка доверия', 'Надёжность системы: <b>1/5</b>', 'Уверенность в сделках:', 'STRONG обоснован: <b>нет</b>',
         'Качество данных: <b>низкое</b>', 'Ожидаемая R на сделку: <b>не установлена</b>', 'Инвалидация: у каждой карточки')
METHOD = ('Оценка доверия', 'Надёжность системы', 'Форвард с 28.10', 'история 2020–2026', 'Открытые STRONG-сделки')
TRUST_KEYS = {'system', 'strong_justified', 'served', 'cards', 'quality', 'fresh', 'complete', 'expectancy_established'}
CARD = re.compile(r'^[🟢🔴] <b>[A-Z0-9]+ · (LONG|SHORT)</b>', re.M)
CONF = re.compile(r'^Уверенность: <b>([0-5])/5</b> — ', re.M)
DAY = dt.timedelta(days=1)


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


def maybe_sha(path):
    return sha256_file(path) if os.path.exists(path) else None


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


# ---- pure readings: each takes what the modes read and returns its checks -----------------------------------------

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


def tree_checks(label, old_src, new_src, defs, asg, rule=()):
    """Two of a file's syntax trees: the definitions that changed, were added and were removed are exactly defs'; every other
    definition - rule's among them, named - is identical; the assignments differ exactly as asg names."""
    (od, oa), (nd, na) = top_level(old_src), top_level(new_src)
    changed = {k for k in od if k in nd and od[k] != nd[k]}
    same = [k for k in od if k in nd and od[k] == nd[k]]
    return {
        '%s: the definitions changed are exactly %s, added %s, removed %s' % (label, sorted(defs[0]), sorted(defs[1]), sorted(defs[2])):
            (changed, set(nd) - set(od), set(od) - set(nd)) == defs,
        '%s: the %d others identical by AST%s' % (label, len(set(od) - defs[0] - defs[2]),
                                                  ', the %d rule functions among them' % len(rule) if rule else ''):
            set(same) == set(od) - defs[0] - defs[2] and all(k in same for k in rule),
        '%s: the assignments changed are exactly %s, added %s, removed %s' % (label, sorted(asg[0]), sorted(asg[1]), sorted(asg[2])):
            ({k for k in oa if k in na and oa[k] != na[k]}, set(na) - set(oa), set(oa) - set(na)) == asg,
    }


def report_sections(text):
    """{heading: {first cell: [the other cells]}} of every '#### ' section's table rows, a cell's backticks stripped."""
    out_, name = {}, None
    for line in text.split('\n'):
        if line.startswith('#### '):
            name = line[5:].strip()
            out_[name] = {}
        elif name and line.startswith('| ') and not line.startswith('|---'):
            cells = [c.strip().strip('`') for c in line.strip().strip('|').split('|')]
            out_[name].setdefault(cells[0], cells[1:])
    return out_


def pit_from_report(text):
    """adv3.PIT as TZ-38's report prints it (§2.7): E4's reach shares and STRONG's top-5 share, E1's rule on G, E2's p, E5's
    median and its share of lists in profit, the size of G - each cell read as a number."""
    sec = report_sections(text)
    pick = lambda prefix: next(v for k, v in sec.items() if k.startswith(prefix))
    e1, e2, e4, e5, sets = pick('E1 '), pick('E2 '), pick('E4 '), pick('E5 '), pick('The sets ')
    f = lambda s: float(s.replace(',', ''))
    return {'base': {'mfe': {n: f(e4['mfe +%dR' % n][0]) for n in (1, 2, 3)}, 'mean_R_G': f(e1['mean_R'][0]),
                     'trades_G': int(f(e1['trades'][0])), 'p_G': f(e1['p_t_up'][0]), 'contracts_G': int(f(sets['G'][0]))},
            'strong': {'mfe': {n: f(e4['mfe +%dR' % n][1]) for n in (1, 2, 3)}, 'p_G': f(e2['p_t_up'][0]),
                       'mean_R_lists': f(e5['0.5'][1]), 'lists': int(f(e5['lists'][0])),
                       'lists_positive': f(e5['share_mean_R_positive'][0]), 'top5_share': f(e4['top5_share'][1])}}


def html_balanced(text):
    return all(text.count('<%s>' % t) == text.count('</%s>' % t) for t in ('b', 'i'))


def plan_invariants(p, rep, liq, budget, n):
    """The allocation's limits, read from a plan (the bot's own) and the report and liquidity it was made from. The limits are
    this checker's, the TZ's: stop 14 %, minimum 5 USDT, liquidity 0.1 %, risk 1 % a trade and 5 % in all, three places."""
    items = p['items']
    coins = [it['card']['coin'] for it in items]
    strong = [c for c in rep['top'] if c in rep['strong']]
    named = [r[0] for r in p['rejected']]
    return {
        'only STRONG coins of the report, in rank order, at most n and at most three, none added to fill': (
            set(coins) <= set(strong) and coins == [c for c in strong if c in coins] and len(coins) <= min(n, 3)),
        'every STRONG coin is in the plan or named with a reason, once': sorted(coins + named) == sorted(strong),
        'every position has an entry and a stop within 14 % of it, on current prices': (
            all(it['card']['entry'] is not None and it['card']['stop_pct'] <= STOP_MAX for it in items) and (rep['marks_ok'] or not items)),
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


def sign_sum(days, closes, i):
    """The sum of the four signs at days[i], written here: the close against the last close at least 14, 28, 56 and 112 days
    before; None before the longest exists."""
    s = 0
    for L in (14, 28, 56, 112):
        j = bisect.bisect_right(days, days[i] - L * DAY) - 1
        if j < 0:
            return None
        s += (closes[i] > closes[j]) - (closes[i] < closes[j])
    return s


def walk(c, side, close_of, stop, last):
    """An offer's fate by this checker's own reading of the rule: from the day after its close, a candle reaching the stop ends
    it there; else a close whose sum of signs leaves the side - below +2 for a long, above -2 for a short - ends it at that close.
    ('stop' | 'signal' | 'open' | 'unknown', day)."""
    D = dt.date.fromisoformat(close_of)
    days = sorted(d for d in c if d <= last)
    if D not in c:
        return 'unknown', None
    closes = [c[d][3] for d in days]
    for i in range(days.index(D) + 1, len(days)):
        _o, h, l, _c = c[days[i]]
        if (l <= stop) if side > 0 else (h >= stop):
            return 'stop', str(days[i])
        s = sign_sum(days, closes, i)
        if s is None or (s < 2 if side > 0 else s > -2):
            return 'signal', str(days[i])
    return 'open', None


def alert_checks(run, cs, prev_passing):
    """One check's alerts read against this checker's own walk of every offer the journal held before it: each stop, touch and
    signal alert is an offer's first exit by the walk (or the forming candle through its stop), each such exit not alerted
    before is alerted, and each candidate is a STRONG coin the plan places that the check before did not."""
    offs, done, _prev = run['scan']
    rec, last, forming = run['rec'], run['last'], run['forming']
    want = []
    for key, off in offs.items():
        coin, side, close_of = key
        if (coin, side, close_of, 'stop') in done or (coin, side, close_of, 'signal') in done:
            continue
        state, day = walk(cs.get(coin) or {}, side, close_of, off['stop'], last)
        if state == 'open' and forming.get(coin):
            _o, h, l, _c = forming[coin]
            if (l <= off['stop']) if side > 0 else (h >= off['stop']):
                state, day = 'touch', str(last + DAY)
        if state in ('stop', 'touch', 'signal'):
            want.append(('stop' if state == 'touch' else state, coin, side, close_of, day, state == 'touch'))
    got = [(a['kind'], a['coin'], a['side'], a['close_of'], a['day'], a['touch']) for a in rec['alerts'] if a['kind'] != 'candidate']
    placed = [(it['card']['coin'], it['card']['side']) for it in run['plan']['items']]
    cand = [(a['coin'], a['side']) for a in rec['alerts'] if a['kind'] == 'candidate']
    return sorted(got) == sorted(want) and cand == [x for x in placed if x not in prev_passing]


def render_checks(texts, calc, runs, kinds, records, log, same, expect):
    """G-RENDER: what the service copy's bot sent for each command (texts, by command), the plan the checker recomputed from the
    report and liquidity each allocation reply was made from (calc), the two checks run on live data (runs), the scratch
    journal's kinds and records, the bot's log, whether the bot's own record is as before, and the bot module's constants
    (expect); counts and labels only."""
    whole = lambda parts: '\n'.join(parts)
    sig, top7, ass = whole(texts[RENDER_CASES[0]]), whole(texts[RENDER_CASES[1]]), whole(texts[RENDER_CASES[4]])
    allocs = [c for c in RENDER_CASES if c in calc]
    usdt = expect['usdt']
    inv = {c: plan_invariants(calc[c]['plan'], calc[c]['rep'], calc[c]['liq'], calc[c]['budget'], calc[c]['n']) for c in allocs}

    def fields(c):
        p, t = calc[c]['plan'], whole(texts[c])
        head = ('не доказанная' in t and 'Бюджет %s USDT' % expect['num'](p['budget'], 6) in t and 'Размещено %s USDT' % usdt(p['allocated']) in t
                and ('Свободно %s USDT' % usdt(p['free']) in t or 'свободно %s USDT' % usdt(p['free']) in t) and 'Оценка доверия' not in t)
        if not p['items']:
            return head and 'Подходящих сделок нет' in t
        k = len(p['items'])
        return (head and 'Подходящих сделок: %d из %d запрошенных' % (k, p['n']) in t
                and all(t.count(m) == k for m in ('Капитал:', 'Потеря на стопе:', '⛔ Стоп:', 'Инвалидация: цена', 'Качество: z'))
                and t.count('🎯') == 3 * k and t.count('размеры — формула Архитектора, не доказана') == k
                and 'Потеря на стопах %s USDT' % usdt(p['loss']) in t and 'маржа %s USDT' % usdt(p['margin']) in t)

    def cards_ok(text, most, n_of):
        heads = CARD.findall(text)
        conf = CONF.findall(text)
        return (len(heads) <= most and text.count('Основание: сумма знаков') == len(heads) == text.count('Инвалидация: цена')
                == len(conf) and all(int(v) in (0, RUNG) for v in conf) and all(('ранг %d из %d' % (k, n_of)) in text for k in range(1, len(heads) + 1)))

    strong7 = [block.split('\n')[0] for block in top7.split('\n\n') if CARD.match(block)]
    sg, fa = runs.get('signal'), runs.get('fact')

    def run_shape(r, kind):
        rec, sent = r['rec'], r['sent']
        alerts = rec['alerts']
        loud = bool(alerts)
        flags = all(q == rec['quiet'] for _t, q in sent) and rec['quiet'] == (not loud) and len(sent) >= 1
        text = whole(t for t, _q in sent)
        if rec['one_line']:
            shape = (not loud and len(sent) == 1 and '\n' not in text and text.startswith('✓ ') and rec['cards'] == []
                     and (kind == 'fact' and not rec['zones_left'] or kind == 'signal' and not r['changes'] and r['same'] and not rec['weakened']))
        elif kind == 'signal':
            shape = ('STRONG-канд' in text and 'Сделки по карточкам бота' in text and not any(m in text for m in METHOD)
                     and [c['coin'] for c in rec['cards']] == r['rep']['top'] and cards_ok(text, 3, 3)
                     and (loud or r['changes'] or not r['same'] or bool(rec['weakened'])) and (('🔔 <b>События</b>' in text) == loud)
                     and (('ℹ️ Ослабление' in text) == bool(rec['weakened'])))
        else:
            shape = (('🔔 <b>События</b>' in text) == loud and (loud or bool(rec['zones_left'])) and CARD.findall(text) == []
                     and [(c['coin'], c['side']) for c in rec['cards']] == [(a['coin'], a['side']) for a in alerts if a['kind'] == 'candidate'])
        return flags and shape and html_balanced(text)

    def record_ok(r, kind):
        rec = r['rec']
        return (rec['kind'] == 'check' and rec['slot'].endswith(' ' + kind) and len(rec['state']) == 42 and TRUST_KEYS <= set(rec['trust'])
                and rec['rule'] == H['rule'] and rec['close_of'] == r['rep']['close_of'] and rec['passing'] == [list(x) for x in
                [(it['card']['coin'], it['card']['side']) for it in r['plan']['items']]]
                and all(rec['state'][c]['rank'] is not None for c in r['rep']['top']))

    return {
        'every command and both checks answered, no traceback and no failed request in the bot\'s log':
            all(texts[k] for k in RENDER_CASES) and sg is not None and fa is not None and 'Traceback' not in log and 'failed' not in log,
        'the markup is balanced in every message (b, i)': all(html_balanced(t) for ps in texts.values() for t in ps),
        '«сигнал»: at most three cards, each with its basis, invalidation and confidence - the rung 1 or 0 - and no methodology':
            cards_ok(sig, 3, 3) and not any(m in sig for m in METHOD) and 'на чём держится уверенность' in sig,
        '«сигнал топ 7»: at most seven cards ranked of 7, each with its confidence, STRONG only among the first three':
            cards_ok(top7, 7, 7) and 'ТОП-7 по силе тренда' in top7 and not any('★ STRONG' in h for h in strong7[3:]),
        '«оценка»: the rung and the next readings, the six ratings, the forward record; STRONG at the lists\' median, never the 42\'s':
            all(k in ass for k in TRUST + ('рубеж 1 из 5', 'после закрытия 28.10.2027', 'после закрытия 31.10.2027', 'Форвард с 28.10'))
            and '+0,22 R' in ass and '+0,04 R' in ass and '0,55' not in ass,
        'the bot\'s constants are this TZ\'s: 14 % a stop, 5 USDT, 0.1 % of the volume, 1 % and 5 % of risk, three places, 0.1 % a side, '
        'a list of 7, checks at 00:10 and 12:10 UTC, the rung 1': expect['consts'] == (STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, RISK_MAX, RISK_ALL, 3,
                                                                                     0.001, LIST_MAX, SLOTS, RUNG),
        'each allocation reply is the bot\'s own plan_parts of the report and liquidity it was made from':
            len(allocs) == 2 and all(texts[c] == calc[c]['parts'] for c in allocs),
        'plan: only STRONG coins of the report, in rank order, at most n and at most three, none added to fill':
            all(v['only STRONG coins of the report, in rank order, at most n and at most three, none added to fill'] for v in inv.values()),
        'plan: every STRONG coin is in the plan or named with a reason, once':
            all(v['every STRONG coin is in the plan or named with a reason, once'] for v in inv.values()),
        'plan: every position has an entry and a stop within 14 % of it, on current prices':
            all(v['every position has an entry and a stop within 14 % of it, on current prices'] for v in inv.values()),
        'plan: each loss at its stop within 1 % of the budget, all together within 5 %':
            all(v['each loss at its stop within 1 % of the budget, all together within 5 %'] for v in inv.values()),
        'plan: whole positions of at least 5 USDT, together within the budget, free the budget less them':
            all(v['whole positions of at least 5 USDT, together within the budget, free the budget less them'] for v in inv.values()),
        'plan: leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap':
            all(v['leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap'] for v in inv.values()),
        'the Boss\'s fields in each allocation reply - budget, count, allocated, free, and for each trade capital, leverage, margin, loss, '
        'stop, targets, invalidation and its confidence with the note that the sizes are unproven - and no six ratings':
            len(allocs) == 2 and all(fields(c) for c in allocs),
        '«сигнал 15000 топ 5» says that STRONG is at most three': 'больше 3 сделок не будет' in whole(texts[RENDER_CASES[3]]),
        '«помощь» and an unknown text answer HELP and nothing else': texts[RENDER_CASES[5]] == [expect['help']] == texts[RENDER_CASES[6]],
        'the signal check: quiet exactly when it holds no alert, one line only where it finds nothing, else the close\'s cards, '
        'candidates and offered trades': sg is not None and run_shape(sg, 'signal'),
        'the fact check: quiet exactly when it holds no alert, one line where it finds neither an alert nor a zone left, no card but '
        'a new candidate\'s': fa is not None and run_shape(fa, 'fact'),
        'the alerts of both checks are the exits of the offered trades by this checker\'s own walk, each once, and the new candidates':
            sg is not None and fa is not None and alert_checks(sg, sg['cs'], sg['prev_passing']) and alert_checks(fa, fa['cs'], fa['prev_passing'])
            and not ({(a['kind'], a['coin'], a['side'], a['close_of']) for a in sg['rec']['alerts'] if a['kind'] != 'candidate'}
                     & {(a['kind'], a['coin'], a['side'], a['close_of']) for a in fa['rec']['alerts'] if a['kind'] != 'candidate'}),
        'the check records: their slots, every coin\'s state with the TOP-3 ranked, the six ratings, the placed coins':
            sg is not None and fa is not None and record_ok(sg, 'signal') and record_ok(fa, 'fact'),
        'the scratch journal holds, after the bot\'s own records, request, request, alloc, alloc, assess, check, check':
            kinds == RENDER_KINDS and all(r.get('cards') is not None for r in records),
        'the bot\'s own journal, offset and daily-sent are as before the run, and no check-done file was written': same is True,
    }


def unit_checks(which, pre, now):
    """UNIT-NEW and UNIT-OLD's nine readings after a restart: now is what the modes read; pre is the snapshot of the kill mark."""
    want = (H['adv3_new'], H['bot_new']) if which == 'new' else (H['adv3_old'], H['bot_old'])
    return {
        'the unit is active, running and enabled': (now['bot']['ActiveState'], now['bot']['SubState'],
                                                    now['bot']['UnitFileState']) == ('active', 'running', 'enabled'),
        'a new MainPID, one restart more': int(now['bot']['MainPID']) not in (0, int(pre['bot']['MainPID']))
        and int(now['bot']['NRestarts']) == int(pre['bot']['NRestarts']) + 1,
        'the process started after the kill mark and within 90 s of it': pre['t'] <= now['start'] <= pre['t'] + 90,
        'the process runs the unit\'s exact argv, alone': now['argv'] == ARGV and now['procs'] == [int(now['bot']['MainPID'])],
        'the service copy\'s adv3.py and adv3-bot.py are the %s ones, and the process started after the copy' % which:
            (now['sha_adv3'], now['sha_bot']) == want and now['start'] > now['copy_t'],
        'the unit file is unchanged': now['sha_unit'] == H['unit'],
        'no daily record since the mark': now['daily'] == pre['daily'],
        'the log shows the new process serving and no traceback since the mark': now['serving'] and not now['traceback'],
        'the three capture units unchanged, each active': all(
            now['caps'][u]['ActiveState'] == 'active' and now['caps'][u]['MainPID'] == pre['caps'][u]['MainPID']
            and now['caps'][u]['NRestarts'] == pre['caps'][u]['NRestarts'] for u in CAPTURES),
    }


def first_checks(pre, recs, done_text, log, pid, tail_ok):
    """G-FIRST: the new process's first check, from the journal's records stamped after the kill mark, the check-done file and
    service.log's lines since the mark."""
    t0 = dt.datetime.fromtimestamp(pre['t'], dt.timezone.utc)
    day = t0.date()
    checks_ = [r for r in recs if r.get('kind') == 'check']
    r = checks_[0] if checks_ else {}
    want_done = '%s %s' % (day, 'fact' if t0.time() >= SLOTS[1][1] else 'signal')
    return {
        'exactly one check record since the mark': len(checks_) == 1,
        'it is the day\'s signal check, of the close of the day before, under rule ee206e7c': (
            r.get('slot') == '%s signal' % day and r.get('close_of') == str(day - DAY) and r.get('rule') == H['rule']),
        'it was sent: its Telegram message ids': bool(r.get('message_ids')) and all(isinstance(x, int) for x in r.get('message_ids') or ['x']),
        'it holds the 42 coins\' state, the six ratings, its alerts and its placed coins, quiet exactly without an alert': (
            len(r.get('state') or {}) == 42 and TRUST_KEYS <= set(r.get('trust') or {}) and isinstance(r.get('alerts'), list)
            and isinstance(r.get('passing'), list) and r.get('quiet') == (not r.get('alerts'))),
        'check-done names the slot it covers: %s' % want_done: done_text == want_done,
        'the log since the mark: the new process serving from no check-done, the check sent, no check failed and no traceback': (
            ('serving the pinned chat: pid %d ' % pid in log and 'check-done -' in log) and 'check sent: %s signal' % day in log
            and 'check failed' not in log and 'Traceback' not in log),
        'the journal ends in a newline and every line since the mark parses': tail_ok,
    }


def log_since(text, t0, pid):
    """service.log's lines stamped at or after t0 less 1 s, a traceback's lines with them, and whether the process pid logged
    'serving' among them: (serving, the text, a traceback)."""
    keep, tb, serving, on = [], False, False, False
    for line in text.splitlines():
        m = re.match(r'^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})Z (.*)$', line)
        if m:
            on = calendar.timegm(time.strptime(m.group(1), '%Y-%m-%dT%H:%M:%S')) >= t0 - 1
            serving = serving or (on and m.group(2).startswith('serving the pinned chat: pid %d ' % pid))
        if on:
            keep.append(line)
            tb = tb or 'Traceback' in line
    return serving, '\n'.join(keep), tb


def records_since(text, t0):
    """The journal's records from the first stamped at or after t0 less 1 s, and whether the text ends in a newline with every
    line from that record on parsing."""
    recs, ok, on = [], text.endswith('\n') or text == '', False
    for line in text.splitlines():
        try:
            r = json.loads(line)
            t = dt.datetime.fromisoformat(r['utc']).timestamp()
        except (ValueError, KeyError, TypeError, AttributeError):
            ok = ok and not on
            continue
        on = on or t >= t0 - 1
        if on:
            recs.append(r)
    return recs, ok


def memory_gate(first, second):
    """The memory gate: MemAvailable at the first read, and at the second, 60 s later, taken only where the first fell
    below MEM_FLOOR; the second decides. Returns (passes, the read that decided)."""
    final = first if first >= MEM_FLOOR or second is None else second
    return final >= MEM_FLOOR, final


def count_kind(text, kind):
    """How many records of a kind a journal.jsonl text holds; a broken line left out."""
    n = 0
    for line in text.splitlines():
        try:
            n += json.loads(line).get('kind') == kind
        except (ValueError, AttributeError):
            pass
    return n


def number_reading(names):
    return {'CryptoTZ/ holds %s and no other file of that number' % TZ_FILE:
            [n for n in names if n.startswith('CryptoTZ/' + NUMBER)] == [TZ_FILE],
            'CryptoReports/ holds no report of that number': not [n for n in names if n.startswith('CryptoReports/' + NUMBER)]}


# ---- the modes ----------------------------------------------------------------------------------------------------

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
    rc, so, _ = sh(['find', '/var/lib/btc-recorder', '-mindepth', '1', '-maxdepth', '3', '-name', 'manifest.json', '-print', '-quit'])
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
    checks['H5 the bot is active, running and enabled'] = (b['ActiveState'], b['SubState'], b['UnitFileState']) == ('active', 'running', 'enabled')
    checks['H5 the bot\'s MainPID runs the unit\'s argv, alone'] = (
        int(b['MainPID']) > 0 and proc_argv(b['MainPID']) == ARGV and procs(ARGV) == [int(b['MainPID'])])
    checks['H5 the service copy holds adv3.py, adv3-bot.py and commit.txt only'] = sorted(os.listdir(SVC)) == ['adv3-bot.py', 'adv3.py', 'commit.txt']
    checks['H5 adv3.py is TZ-36\'s and adv3-bot.py is TZ-37\'s'] = (
        sha256_file(SVC + '/adv3.py') == H['adv3_old'] and sha256_file(SVC + '/adv3-bot.py') == H['bot_old'])
    checks['H5 the installed unit file is TZ-35\'s'] = sha256_file('/etc/systemd/system/adv3-bot.service') == H['unit']
    checks['H5 commit.txt is 40 hex characters and a newline'] = re.fullmatch(r'[0-9a-f]{40}\n', read(SVC + '/commit.txt')) is not None
    checks['H6 the record holds a journal of whole lines and no check-done file'] = (
        read(BOTDIR + '/journal.jsonl', 'rb').endswith(b'\n') and not os.path.exists(BOTDIR + '/check-done'))
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
    out('MemAvailable first %d bytes, second %s, deciding %d; /dev/vda2 free %s bytes' % (first, 'not read' if second is None else second, final, avail))
    verdict('HOST', checks)


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


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def mode_rule():
    rule_txt = read(WT + '/advisor/RULE-ADV-3.txt', 'rb')
    unit = read(WT + '/deploy/systemd/adv3-bot.service', 'rb')
    report = git_show(TZ38[0]).encode()
    pit = load_module('adv3_branch', WT + '/advisor/adv3.py').PIT
    checks = {
        'RULE-ADV-3.txt is main\'s, byte for byte, hashes to the RULE constant, and is the branch\'s adv3.py\'s':
            rule_txt == git_show('advisor/RULE-ADV-3.txt').encode() and sha256_bytes(rule_txt) == H['rule']
            and ("RULE = '%s'" % H['rule']) in read(WT + '/advisor/adv3.py'),
        'the unit file is main\'s, byte for byte, and hashes to TZ-35\'s': unit == git_show('deploy/systemd/adv3-bot.service').encode()
            and sha256_bytes(unit) == H['unit'],
    }
    checks.update(tree_checks('adv3.py', git_show('advisor/adv3.py'), read(WT + '/advisor/adv3.py'), ADV3_DEFS, ADV3_ASG, ADV3_RULE))
    checks['adv3.py\'s PIT is TZ-38\'s report as committed (%s…), cell for cell' % TZ38[1][:8]] = (
        sha256_bytes(report) == TZ38[1] and pit == pit_from_report(report.decode('utf-8')))
    checks.update(tree_checks('adv3-bot.py', git_show('advisor/adv3-bot.py'), read(WT + '/advisor/adv3-bot.py'), BOT_DEFS, BOT_ASG))
    checks['the branch\'s adv3.py, adv3-bot.py and selftest-adv3.py are Appendix A\'s'] = (
        sha256_file(WT + '/advisor/adv3.py'), sha256_file(WT + '/advisor/adv3-bot.py'), sha256_file(WT + '/advisor/selftest-adv3.py')) == (
        H['adv3_new'], H['bot_new'], H['selftest_new'])
    verdict('RULE', checks)


def snapshot():
    """What a mark records: the instant, the bot's and the captures' units, the record's daily and check counts and its files."""
    text = read(BOTDIR + '/journal.jsonl')
    return {'t': time.time(), 'bot': show(BOT, 'MainPID', 'NRestarts', 'ActiveState'),
            'caps': {u: show(u, 'MainPID', 'NRestarts', 'ActiveState') for u in CAPTURES},
            'daily': count_kind(text, 'daily'), 'checks': count_kind(text, 'check'), 'lines': text.count('\n'),
            'check_done': read(BOTDIR + '/check-done').strip() if os.path.exists(BOTDIR + '/check-done') else None}


def mode_mark(name):
    """A mark: the snapshot, kept in state.json. kill and kill2 refuse where the old code's message of the UTC day was not sent -
    daily-sent not today - so that a rollback's restart of the old code finds that message sent, as UNIT-OLD reads it."""
    assert name in ('deploy', 'kill', 'rollback', 'kill2'), name
    st = load_state()
    snap = snapshot()
    if name in ('kill', 'kill2'):
        today, sent = time.strftime('%Y-%m-%d', time.gmtime()), read(BOTDIR + '/daily-sent').strip()
        assert sent == today, 'the old code\'s message of the day is not sent: daily-sent %s, today %s' % (sent, today)
    st.setdefault('marks', {})[name] = snap
    save_state(st)
    out('mark %s at %s: bot pid %s NRestarts %s, %d daily and %d check records, check-done %s' % (
        name, time.strftime('%FT%TZ', time.gmtime(snap['t'])), snap['bot']['MainPID'], snap['bot']['NRestarts'], snap['daily'],
        snap['checks'], snap['check_done'] or '-'))


def mode_copy():
    rc, head, _ = sh(['git', '-C', WT, 'rev-parse', 'HEAD'])
    rc2, up, _ = sh(['git', '-C', WT, 'rev-parse', 'origin/' + BRANCH])
    commit = read(SVC + '/commit.txt')
    verdict('COPY', {
        'the service copy holds adv3.py, adv3-bot.py and commit.txt only': sorted(os.listdir(SVC)) == ['adv3-bot.py', 'adv3.py', 'commit.txt'],
        'adv3.py is Appendix A\'s': sha256_file(SVC + '/adv3.py') == H['adv3_new'],
        'adv3-bot.py is Appendix A\'s': sha256_file(SVC + '/adv3-bot.py') == H['bot_new'],
        'commit.txt is the branch head and the worktree\'s HEAD': (
            re.fullmatch(r'[0-9a-f]{40}\n', commit) is not None and rc == 0 and rc2 == 0 and commit.strip() == head.strip() == up.strip()),
        'the branch\'s two files equal the service copy\'s': all(read(WT + '/advisor/' + f, 'rb') == read(SVC + '/' + f, 'rb')
                                                               for f in ('adv3.py', 'adv3-bot.py')),
    })


def own_files():
    return tuple(maybe_sha(BOTDIR + '/' + f) for f in ('journal.jsonl', 'offset', 'daily-sent', 'check-done'))


def render_run(mod, data, now):
    """G-RENDER's pipeline on a loaded bot and a Data: the commands answered through the bot's handle, then the signal check and
    the fact check through its check, each appended to its STATE's journal; Telegram a stand-in, the reports, volumes and forming
    candles the bot read captured, and each allocation's plan recomputed by the bot's plan from the very report and volumes its
    reply was made from. (texts, calc, runs, records, log, expect)."""
    base_lines = read(mod.STATE + '/journal.jsonl').count('\n')

    class Cap(mod.Telegram):
        def __init__(self):
            super().__init__('123456:SECRET', 777)
            self.sent = []

        def call(self, method, http_timeout=30, **params):
            self.sent.append((params['text'], params.get('disable_notification', False)))
            return {'message_id': len(self.sent)}

    cap, texts, calc, seen, liqs, formed, runs = Cap(), {}, {}, [], {}, {}, {}
    real_lr, real_liq, real_form = mod.live_report, mod.liquidity, mod.forming_candles

    def lr_seen(d, deposit, risk):
        r = real_lr(d, deposit, risk)
        seen.append(r)
        return r

    def liq_seen(coin, now_ms):
        liqs[coin] = real_liq(coin, now_ms)
        return liqs[coin]

    def form_seen(coins, day):
        got = real_form(coins, day)
        formed.update(got)
        return got

    mod.live_report, mod.liquidity, mod.forming_candles = lr_seen, liq_seen, form_seen
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            for case in RENDER_CASES:
                n0, m0 = len(cap.sent), len(seen)
                liqs.clear()
                mod.handle(cap, data, case)
                texts[case] = [t for t, _q in cap.sent[n0:]]
                cmd = mod.route(case)
                if cmd and cmd[0] == 'alloc' and len(seen) == m0 + 1:
                    _k, budget, n, risk = cmd
                    rep = mod.top_n(seen[-1], mod.adv3.TOP_N)
                    p = mod.plan(rep, data.cs, budget, n, risk, dict(liqs))
                    calc[case] = {'rep': rep, 'liq': dict(liqs), 'plan': p, 'budget': budget, 'n': n, 'parts': mod.plan_parts(rep, p)}
            for kind in ('signal', 'fact'):
                scan = mod.journal_scan()
                n0, m0 = len(cap.sent), len(seen)
                liqs.clear()
                formed.clear()
                rec = mod.check(cap, data, (now.date(), kind), now)
                mod.append(rec)
                rep = mod.top_n(seen[m0], mod.adv3.TOP_N)
                p = mod.plan(rep, data.cs, mod.adv3.DEPOSIT, mod.adv3.TOP_N, mod.adv3.RISK, dict(liqs))
                prev, rows = scan[2], rep['rows']
                runs[kind] = {'rec': rec, 'sent': cap.sent[n0:], 'scan': scan, 'rep': rep, 'plan': p, 'forming': dict(formed),
                              'last': dt.date.fromisoformat(rep['close_of']), 'cs': data.cs,
                              'prev_passing': {(c, s) for c, s in (prev or {}).get('passing') or []},
                              'changes': any(rows[c].get('signal') != rows[c].get('prev')
                                             and (rows[c].get('signal') in (1, -1) or rows[c].get('prev') in (1, -1)) for c in mod.adv3.COINS),
                              'same': prev is not None and prev.get('top') == rep['top'] and prev.get('strong') == rep['strong']
                              and all((prev.get('signals') or {}).get(c) == rows[c].get('signal') for c in rep['top'])}
    finally:
        mod.live_report, mod.liquidity, mod.forming_candles = real_lr, real_liq, real_form
    records = [json.loads(line) for line in read(mod.STATE + '/journal.jsonl').splitlines()[base_lines:]]
    m = mod.adv3
    expect = {'help': mod.HELP, 'usdt': m.usdt, 'num': m.num,
              'consts': (mod.STOP_MAX, mod.MIN_NOTIONAL, mod.LIQ_FRAC, m.RISK_MAX, m.RISK_ALL, m.TOP_N, m.COST, mod.LIST_MAX, mod.SLOTS,
                         m.RELIABILITY)}
    return texts, calc, runs, records, buf.getvalue(), expect


def render_print(texts, calc, runs, seen_strong, log):
    """What G-RENDER prints: sizes, counts and labels, never a coin, a price or a size."""
    out('replies: %s; the bot\'s log: %d lines; STRONG coins: %d; trades placed per allocation: %s' % (
        ', '.join('%d chars in %d parts' % (sum(map(len, texts[k])), len(texts[k])) for k in RENDER_CASES), log.count('\n'),
        seen_strong, ', '.join(str(len(calc[c]['plan']['items'])) for c in calc)))
    for kind, r in runs.items():
        rec = r['rec']
        out('%s check: %s, %s, %d parts; alerts %s; offers read %d, followed %d; placed %d; zones left %d; forming candles read %d' % (
            kind, 'quiet' if rec['quiet'] else 'loud', 'one line' if rec['one_line'] else 'full', len(r['sent']),
            json.dumps({k: sum(a['kind'] == k for a in rec['alerts']) for k in ('stop', 'signal', 'candidate')}, sort_keys=True),
            len(r['scan'][0]), len(rec['followed']), len(rec['passing']), len(rec['zones_left']), len(r['forming'])))


def mode_render():
    """G-RENDER: the service copy's bot answers the commands and runs both checks on live data, its Telegram a stand-in, its
    STATE a scratch directory holding a copy of the bot's own journal, so the trades its cards offered are the real ones."""
    os.makedirs(SCRATCH, exist_ok=False)
    shutil.copyfile(BOTDIR + '/journal.jsonl', SCRATCH + '/journal.jsonl')
    own = own_files()
    saved = list(sys.path)
    sys.path.insert(0, SVC)
    try:
        mod = load_module('advbot', SVC + '/adv3-bot.py')
    finally:
        sys.path[:] = saved
    mod.STATE = SCRATCH
    texts, calc, runs, records, log, expect = render_run(mod, mod.Data(), dt.datetime.now(dt.timezone.utc))
    same = own == own_files() and own[3] is None
    render_print(texts, calc, runs, len(runs['signal']['rep']['strong']) if 'signal' in runs else -1, log)
    verdict('RENDER', render_checks(texts, calc, runs, [r['kind'] for r in records], records, log, same, expect))


def mode_unit(which):
    assert which in ('new', 'old'), which
    st = load_state()
    pre = st['marks']['kill' if which == 'new' else 'kill2']
    copy_t = st['marks']['deploy' if which == 'new' else 'rollback']['t']
    bot = show(BOT, 'MainPID', 'NRestarts', 'ActiveState', 'SubState', 'UnitFileState')
    pid = int(bot['MainPID'])
    if pid in (0, int(pre['bot']['MainPID'])) or bot['ActiveState'] != 'active':
        if time.time() - pre['t'] < 100:
            raise NotYet()
    caps = {u: show(u, 'MainPID', 'NRestarts', 'ActiveState') for u in CAPTURES}
    start = proc_start(pid) if pid else 0.0
    serving, _text, tb = log_since(read(BOTDIR + '/service.log'), pre['t'], pid)
    now = {'bot': bot, 'caps': caps, 'start': start, 'copy_t': copy_t, 'argv': proc_argv(pid) if pid else None, 'procs': procs(ARGV),
           'sha_adv3': sha256_file(SVC + '/adv3.py'), 'sha_bot': sha256_file(SVC + '/adv3-bot.py'),
           'sha_unit': sha256_file('/etc/systemd/system/adv3-bot.service'), 'daily': count_kind(read(BOTDIR + '/journal.jsonl'), 'daily'),
           'serving': serving, 'traceback': tb}
    checks = unit_checks(which, pre, now)
    if which == 'old':
        checks['two restarts more than before the first kill'] = int(bot['NRestarts']) == int(st['marks']['kill']['bot']['NRestarts']) + 2
    out('bot: pid %d NRestarts %s started %s; captures: %s' % (pid, bot['NRestarts'], time.strftime('%FT%TZ', time.gmtime(start)),
        json.dumps({u: [c['MainPID'], c['NRestarts']] for u, c in caps.items()}, sort_keys=True)))
    verdict('UNIT-' + which.upper(), checks)


def mode_first():
    st = load_state()
    pre = st['marks']['kill']
    pid = int(show(BOT, 'MainPID')['MainPID'])
    recs, tail_ok = records_since(read(BOTDIR + '/journal.jsonl'), pre['t'])
    if not [r for r in recs if r.get('kind') == 'check']:
        if time.time() - pre['t'] < FIRST_BOUND:
            raise NotYet()
    done_text = read(BOTDIR + '/check-done').strip() if os.path.exists(BOTDIR + '/check-done') else None
    _serving, text, _tb = log_since(read(BOTDIR + '/service.log'), pre['t'], pid)
    checks_ = [r for r in recs if r.get('kind') == 'check']
    r = checks_[0] if checks_ else {}
    out('first check: %s, %s, %d messages; alerts %s; followed %d; placed %d; check-done %s' % (
        'quiet' if r.get('quiet') else 'loud', 'one line' if r.get('one_line') else 'full', len(r.get('message_ids') or []),
        json.dumps({k: sum(a.get('kind') == k for a in r.get('alerts') or []) for k in ('stop', 'signal', 'candidate')}, sort_keys=True),
        len(r.get('followed') or []), len(r.get('passing') or []), done_text or '-'))
    verdict('FIRST', first_checks(pre, recs, done_text, text, pid, tail_ok))


def kept_files():
    """The work tree's files a report keeps by name: state.json, the three files B-DEPLOY saves, and every file under logs/;
    relative to WORK, sorted."""
    names = ['state.json', 'adv3.before', 'bot.before', 'commit.before']
    for d, _s, fs in os.walk(WORK + '/logs'):
        names += [os.path.relpath(os.path.join(d, f), WORK) for f in fs]
    return sorted(n for n in names if os.path.isfile(os.path.join(WORK, n)))


def mode_keep():
    """B-RECLAIM-OWN's copy: every kept file into the forensic store as tz39-work--<path with - for />, by exclusive create and
    verified whole; the branch worktree must hold nothing but its pushed HEAD."""
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
        dest = FORENSICS + '/tz39-work--' + rel.replace('/', '--')
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
    verdict('STOPPED', {'the unit is inactive or failed, and disabled': bot['ActiveState'] in ('inactive', 'failed') and bot['UnitFileState'] == 'disabled',
                        'no process runs under the unit\'s argv': procs(ARGV) == []})


# ---- the self-test: the pure readings on stand-ins and the render on the real bot with a synthetic market, each with its
# negative controls ----------------------------------------------------------------------------------------------------

def synthetic(bot):
    """A synthetic market of twelve coins for the stage's bot, Binance stood in for, and a journal of offers from earlier closes
    built so that a check meets a stop on a closed candle, an exit by signal and - at the fact check - a forming candle through the
    stop of the first card the signal check offers. (data, forming, now)."""
    a = bot.adv3
    dm = dt.date(2026, 6, 1)
    cs, funds = {}, {}
    for n, coin in enumerate(a.COINS[:12]):
        c, x = {}, 100.0 + n
        slope = (0.004 + 0.0015 * n) * (1 if n % 2 == 0 else -1)
        for i in range(160):
            x *= (1 + slope) * (1 + 0.004 * ((i * 7 + n) % 5 - 2))
            c[dm + dt.timedelta(days=i)] = (x, x * 1.02, x * 0.98, x)
        cs[coin] = c
        funds[coin] = lambda d: 0.0
    last = max(cs[a.COINS[0]])
    up, down = a.COINS[0], a.COINS[1]
    d5 = last - 5 * DAY
    old = [{'utc': '%sT06:00:00+00:00' % (d5 + DAY), 'kind': 'daily', 'close_of': str(d5), 'cards': [
        {'coin': up, 'side': 1, 'mode': 'market', 'close': cs[up][d5][3], 'U': cs[up][d5][3] * 0.001},
        {'coin': down, 'side': 1, 'mode': 'market', 'close': cs[down][d5][3], 'U': cs[down][d5][3] * 0.9}]}]
    with open(bot.STATE + '/journal.jsonl', 'w', encoding='utf-8') as fh:
        fh.write(''.join(json.dumps(r) + '\n' for r in old))
    marks = {c + 'USDT': (cs[c][last][3], 0.0001) for c in cs}
    forming = {}
    ms = lambda d: int(dt.datetime.combine(d, dt.time(0), tzinfo=dt.timezone.utc).timestamp() * 1000)

    def fake_fapi(path, **params):
        if path == '/fapi/v1/premiumIndex':
            return [{'symbol': k, 'markPrice': str(v[0]), 'lastFundingRate': '0.0001'} for k, v in marks.items()]
        if path == '/fapi/v1/fundingInfo':
            return []
        coin = params['symbol'][:-4]
        if params.get('limit') == 2:
            cl = cs[coin][last][3]
            o, h, l, c_ = forming.get(coin) or (cl, cl * 1.001, cl * 0.999, cl)
            return [[ms(last), '1', '1', '1', '1', '0', ms(last + DAY) - 1, '0'],
                    [ms(last + DAY), str(o), str(h), str(l), str(c_), '0', ms(last + 2 * DAY) - 1, '0']]
        return [[ms(last - k * DAY), '1', '1', '1', '1', '0', ms(last - k * DAY + DAY) - 1, '1e12'] for k in range(8)]

    class Stub:
        def __init__(self):
            self.cs, self.funds, self.missing = cs, funds, []

        def fresh(self):
            return self.cs, self.funds

    a.fapi = fake_fapi
    return Stub(), forming, dt.datetime.combine(last + DAY, dt.time(14, 0), tzinfo=dt.timezone.utc)


def mode_selftest():
    import tempfile
    done = []

    def ok(cond, name):
        done.append(name)
        assert cond, name

    mp = ('**Revision string:** `%s`\n\n| anchor | value |\n|---|---|\n| `A1` — observation set | `229a944f2d51` |\n'
          '| `A3` — phase | `x / y` |\n\n### Fingerprint table\n\n| path | lines | bytes | state | SHA-256 |\n|---|---|---|---|---|\n'
          '| `SYSTEM-MAP.md` | — | — | reported | self-reference |\n| `a/b.py` | 1,135 | 50,928 | frozen | `%s` |\n'
          '| `c.py` | 7 | 8 | tracked | `%s` |\n\n---\n\n## 1. Repository\n| `z.py` | 1 | 1 | frozen | `%s` |\n') % (MAP_REV, 'a' * 64, 'b' * 64, 'c' * 64)
    rev, anchors, rows = parse_map(mp)
    ok(rev == MAP_REV and anchors == {'A1': '229a944f2d51', 'A3': 'x / y'}, 'parse_map: the revision and the anchors')
    ok(rows == [('SYSTEM-MAP.md', None, None, 'reported', None), ('a/b.py', 1135, 50928, 'frozen', 'a' * 64), ('c.py', 7, 8, 'tracked', 'b' * 64)],
       'parse_map: the table\'s rows, thousands separators read, the next section left out')
    old = 'X = 1\nHELP = 1\ndef a():\n    return 1\ndef b():\n    return 2\nclass K:\n    def m(self):\n        return 1\nCMD = 5\ndef gone():\n    pass\n'
    new = 'X = 1\nHELP = 2\ndef a():\n    return 1\ndef b():\n    return 3\nclass K:\n    def m(self):\n        return 1\nNEWC = 0\ndef c():\n    return 0\n'
    good = tree_checks('f', old, new, ({'b'}, {'c'}, {'gone'}), ({'HELP'}, {'NEWC'}, {'CMD'}), ('a',))
    ok(all(good.values()) and len(good) == 3, 'tree_checks: exactly the named definitions and assignments differ, the rule\'s among the same, 3 of 3')
    for label, src, defs, asg, rule in (
            ('a definition that should be the same changed', new.replace('def a():\n    return 1', 'def a():\n    return 9'),
             ({'b'}, {'c'}, {'gone'}), ({'HELP'}, {'NEWC'}, {'CMD'}), ('a',)),
            ('a definition named changed that did not', new.replace('def b():\n    return 3', 'def b():\n    return 2'),
             ({'b'}, {'c'}, {'gone'}), ({'HELP'}, {'NEWC'}, {'CMD'}), ('a',)),
            ('an extra definition', new + 'def d():\n    return 0\n', ({'b'}, {'c'}, {'gone'}), ({'HELP'}, {'NEWC'}, {'CMD'}), ('a',)),
            ('an assignment changed and not named', new.replace('X = 1', 'X = 2'), ({'b'}, {'c'}, {'gone'}), ({'HELP'}, {'NEWC'}, {'CMD'}), ('a',)),
            ('a rule function that changed', new, ({'b'}, {'c'}, {'gone'}), ({'HELP'}, {'NEWC'}, {'CMD'}), ('b',))):
        ok(not all(tree_checks('f', old, src, defs, asg, rule).values()), 'tree_checks: %s reads FAIL' % label)
    rpt = ('#### E1 — x\n\n| field | value |\n|---|---|\n| `p_t_up` | 0.0735 |\n| `trades` | 19,002 |\n\n| field | pit_rule.block |\n|---|---|\n'
           '| `trades` | 19,002 |\n| `mean_R` | 0.0403 |\n\n#### E2 — y\n\n| `p_t_up` | 0.1100 |\n\n#### E4 — z\n\n| field | P_rule | P_strong.top3 |\n'
           '|---|---|---|\n| `mfe +1R` | 0.2318 | 0.4717 |\n| `mfe +2R` | 0.1257 | 0.2906 |\n| `mfe +3R` | 0.0759 | 0.1887 |\n| `top5_share` | 0.2401 | 0.9875 |\n\n'
           '#### E5 — w\n\n| quantile | total R | mean R a trade |\n|---|---|---|\n| 0.5 | 37.7116 | 0.2195 |\n\n| `lists` | 500 |\n| `share_mean_R_positive` | 0.8600 |\n\n'
           '#### The sets and the frozen FACTS\n\n| `G` | 570 |\n')
    want = {'base': {'mfe': {1: 0.2318, 2: 0.1257, 3: 0.0759}, 'mean_R_G': 0.0403, 'trades_G': 19002, 'p_G': 0.0735, 'contracts_G': 570},
            'strong': {'mfe': {1: 0.4717, 2: 0.2906, 3: 0.1887}, 'p_G': 0.11, 'mean_R_lists': 0.2195, 'lists': 500, 'lists_positive': 0.86,
                       'top5_share': 0.9875}}
    ok(pit_from_report(rpt) == want, 'pit_from_report: every figure read from its section and row, the thousands separator read')
    ok(pit_from_report(rpt.replace('| 0.5 | 37.7116 | 0.2195 |', '| 0.5 | 37.7116 | 0.2196 |')) != want, 'pit_from_report: a changed cell reads another PIT')
    d0 = dt.date(2026, 1, 1)
    closes = [100 * 1.01 ** i for i in range(150)] + [100 * 1.01 ** 149 * 0.998 ** k for k in range(1, 40)]
    c = {d0 + i * DAY: (cl, cl * 1.002, cl * 0.998, cl) for i, cl in enumerate(closes)}
    days = sorted(c)
    ok(sign_sum(days, closes, 120) == 4 and sign_sum(days, closes, 100) is None, 'sign_sum: four agreeing signs on a rising line, none before 112 days')
    exit_i = next(i for i in range(146, len(closes)) if sum((closes[i] > closes[i - L]) - (closes[i] < closes[i - L]) for L in (14, 28, 56, 112)) < 2)
    ok(walk(c, 1, str(d0 + 145 * DAY), 1.0, days[-1]) == ('signal', str(d0 + exit_i * DAY)), 'walk: a long ends at the close whose signs fall below +2')
    S0 = closes[145] * 0.999
    c2 = dict(c)
    c2[d0 + 147 * DAY] = (closes[146], closes[147] * 1.002, S0 * 0.99, closes[147])
    ok(walk(c2, 1, str(d0 + 145 * DAY), S0, days[-1]) == ('stop', str(d0 + 147 * DAY)) and walk(c, 1, str(d0 + 145 * DAY), S0, d0 + 149 * DAY)
       == ('open', None), 'walk: a candle reaching the stop ends it there; a series above it stays open')
    ok(walk(c, 1, str(days[-1]), 1.0, days[-1]) == ('open', None) and walk(c, 1, '2025-01-01', 1.0, days[-1]) == ('unknown', None),
       'walk: an offer of the last close is open; one with no candle of its close unknown')
    pre = {'t': 1000.0, 'bot': {'MainPID': '10', 'NRestarts': '2'}, 'daily': 7,
           'caps': {u: {'MainPID': str(i), 'NRestarts': '0', 'ActiveState': 'active'} for i, u in enumerate(CAPTURES, 20)}}
    now = {'bot': {'MainPID': '11', 'NRestarts': '3', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'},
           'caps': dict(pre['caps']), 'start': 1035.0, 'copy_t': 990.0, 'argv': ARGV, 'procs': [11], 'sha_adv3': H['adv3_new'],
           'sha_bot': H['bot_new'], 'sha_unit': H['unit'], 'daily': 7, 'serving': True, 'traceback': False}
    ok(all(unit_checks('new', pre, now).values()) and len(unit_checks('new', pre, now)) == 9, 'unit_checks: a clean restart reads 9 of 9')
    for key, val, label in (('daily', 8, 'a daily record since the mark'), ('start', 1200.0, 'a process started 200 s after the kill'),
                            ('sha_bot', H['bot_old'], 'the old bot'), ('sha_adv3', H['adv3_old'], 'the old adv3.py'),
                            ('traceback', True, 'a traceback since the mark'), ('procs', [11, 12], 'a second process under the argv'),
                            ('serving', False, 'no serving line of the new pid')):
        ok(not all(unit_checks('new', pre, dict(now, **{key: val})).values()), 'unit_checks: %s reads FAIL' % label)
    moved = {u: dict(cc, NRestarts='1') for u, cc in pre['caps'].items()}
    ok(not all(unit_checks('new', pre, dict(now, caps=moved)).values()), 'unit_checks: a capture unit restarted reads FAIL')
    ok(all(unit_checks('old', pre, dict(now, sha_bot=H['bot_old'], sha_adv3=H['adv3_old'])).values()), 'unit_checks: the rollback reads the old files')
    t0 = calendar.timegm(time.strptime('2026-11-02T14:00:00', '%Y-%m-%dT%H:%M:%S'))
    pre_f = dict(pre, t=float(t0))
    rec = {'utc': '2026-11-02T14:00:20+00:00', 'kind': 'check', 'slot': '2026-11-02 signal', 'close_of': '2026-11-01', 'rule': H['rule'],
           'message_ids': [5, 6], 'state': {str(k): {} for k in range(42)}, 'trust': {k: 0 for k in TRUST_KEYS}, 'alerts': [], 'passing': [],
           'quiet': True}
    log_f = ('2026-11-02T14:00:05Z serving the pinned chat: pid 11 offset 9 check-done -\n'
             '2026-11-02T14:00:20Z check sent: 2026-11-02 signal for the close of 2026-11-01 | alerts 0 | quiet | full')
    good = first_checks(pre_f, [rec], '2026-11-02 fact', log_f, 11, True)
    ok(all(good.values()) and len(good) == 7, 'first_checks: the first check after a 14:00 restart reads 7 of 7, check-done covering 12:10')
    ok(all(first_checks(dict(pre, t=float(t0 - 4 * 3600)), [rec], '2026-11-02 signal', log_f.replace('14:00:05', '10:00:05'), 11, True).values()),
       'first_checks: a 10:00 restart wants check-done at the signal slot')
    for label, args in (('no check record', ([], '2026-11-02 fact', log_f, 11, True)),
                        ('two check records', ([rec, rec], '2026-11-02 fact', log_f, 11, True)),
                        ('another slot', ([dict(rec, slot='2026-11-02 fact')], '2026-11-02 fact', log_f, 11, True)),
                        ('no message ids', ([dict(rec, message_ids=[])], '2026-11-02 fact', log_f, 11, True)),
                        ('a loud check without an alert', ([dict(rec, quiet=False)], '2026-11-02 fact', log_f, 11, True)),
                        ('check-done at the signal after 12:10', ([rec], '2026-11-02 signal', log_f, 11, True)),
                        ('a failed check in the log', ([rec], '2026-11-02 fact', log_f + '\ncheck failed: x', 11, True)),
                        ('another pid serving', ([rec], '2026-11-02 fact', log_f, 12, True)),
                        ('a broken journal', ([rec], '2026-11-02 fact', log_f, 11, False))):
        ok(not all(first_checks(pre_f, *args).values()), 'first_checks: %s reads FAIL' % label)
    log = ('2026-10-31T06:00:01Z daily sent for the close of 2026-10-30\n2026-10-31T09:00:00Z serving the pinned chat: pid 11 offset 5 check-done -\n'
           'Traceback (most recent call last):\n  File x\n2026-10-31T09:00:30Z check sent: 2026-10-31 signal')
    t = calendar.timegm(time.strptime('2026-10-31T08:59:59', '%Y-%m-%dT%H:%M:%S'))
    s_, text_, tb_ = log_since(log, t, 11)
    ok(s_ and tb_ and 'daily sent' not in text_ and 'check sent' in text_ and '  File x' in text_, 'log_since: the lines since t, a traceback\'s with them, serving found')
    ok(not log_since(log, t, 12)[0] and not log_since(log, t + 3600, 11)[2], 'log_since: another pid does not serve; a later start sees no traceback')
    jl = ('{"utc": "2026-10-31T06:00:00+00:00", "kind": "daily"}\n{"utc": "2026-10-31T09:00:30+00:00", "kind": "check"}\n')
    rs, okj = records_since(jl, calendar.timegm(time.strptime('2026-10-31T09:00:00', '%Y-%m-%dT%H:%M:%S')))
    ok([r['kind'] for r in rs] == ['check'] and okj, 'records_since: the records since t, the earlier left out, a whole journal')
    ok(not records_since(jl + 'broken\n', t)[1] and not records_since(jl.rstrip('\n'), t)[1] and records_since('broken\n' + jl, t + 30)[1],
       'records_since: a broken line after the mark or no final newline reads FAIL; one before the mark does not')
    ok(count_kind(jl + 'x\n{"kind": "daily"}\n', 'daily') == 2 and count_kind('', 'check') == 0, 'count_kind: the kind counted, a broken line left out')
    ok(memory_gate(MEM_FLOOR, None) == (True, MEM_FLOOR) and memory_gate(MEM_FLOOR - 1, MEM_FLOOR) == (True, MEM_FLOOR)
       and memory_gate(MEM_FLOOR - 1, MEM_FLOOR - 2) == (False, MEM_FLOOR - 2), 'memory_gate: a first read below the floor is decided by the second')
    ok(all(number_reading([TZ_FILE, 'CryptoTZ/TZ-38-x.md']).values()), 'number: the one file reads PASS')
    ok(not all(number_reading([TZ_FILE, 'CryptoTZ/TZ-39-other.md']).values()) and not all(number_reading([TZ_FILE, 'CryptoReports/TZ-39-x-report.md']).values()),
       'number: two files of the number, or a report of it, read FAIL')
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(tmp + '/logs/sub')
        for rel in ('state.json', 'bot.before', 'adv3.before', 'logs/01-a.log', 'logs/sub/02-b.log', 'render-state/journal.jsonl'.replace('/', '-'), 'x.txt'):
            with open(tmp + '/' + rel, 'w') as fh:
                fh.write(rel)
        saved_work = WORK
        globals().update(WORK=tmp)
        try:
            kept = kept_files()
        finally:
            globals().update(WORK=saved_work)
    ok(kept == ['adv3.before', 'bot.before', 'logs/01-a.log', 'logs/sub/02-b.log', 'state.json'], 'kept_files: the named files and the logs, nothing else')
    # ---- G-RENDER on the stage's own bot and a synthetic market ----------------------------------------------------
    here = os.path.dirname(os.path.abspath(__file__))
    stage = os.path.join(os.path.dirname(here), 'advisor')
    with tempfile.TemporaryDirectory() as tmp:
        saved = list(sys.path)
        sys.path.insert(0, stage)
        try:
            bot = load_module('advbot_selftest', stage + '/adv3-bot.py')
        finally:
            sys.path[:] = saved
        bot.STATE = tmp
        real_fapi = bot.adv3.fapi
        try:
            data, forming, now0 = synthetic(bot)
            rep0 = bot.top_n(bot.adv3.report(data.cs, data.funds, {c + 'USDT': (data.cs[c][max(data.cs[c])][3], 0.0001) for c in data.cs},
                                             10000.0, 0.5, int(now0.timestamp() * 1000)), 3)
            first = rep0['cards'][0]
            S = first['close'] - first['side'] * first['U']
            cl = first['close']
            forming[first['coin']] = (cl, max(cl, S * 1.01), min(cl, S * 0.99), cl)
            texts, calc, runs, records, blog, expect = render_run(bot, data, now0)
        finally:
            bot.adv3.fapi = real_fapi
    kinds = [r['kind'] for r in records]
    args = dict(texts=texts, calc=calc, runs=runs, kinds=kinds, records=records, log=blog, same=True, expect=expect)
    good = render_checks(**args)
    al = {k: [(x['kind'], x['touch']) for x in runs[k]['rec']['alerts']] for k in runs}
    ok(all(good.values()) and len(good) == 22, 'render_checks: the stage\'s bot on a synthetic market reads 22 of 22 - %s' % [k for k, v in good.items() if not v])
    ok(('stop', False) in al['signal'] and ('signal', False) in al['signal'] and ('candidate', False) in al['signal'] and al['fact'] == [('stop', True)],
       'the synthetic market meets every alert: a stop on a closed candle, an exit by signal and new candidates at the signal check, a forming candle '
       'through a stop at the fact check')

    def bad(**kw):
        a_ = dict(args)
        a_.update(kw)
        return not all(render_checks(**a_).values())

    sig, top7 = texts[RENDER_CASES[0]], texts[RENDER_CASES[1]]
    ok(bad(log='Traceback (most recent call last):') and bad(log='check failed: x'), 'render_checks: a traceback or a failure in the bot\'s log reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: []})), 'render_checks: a command with no answer reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[5]: ['<b>HELP']})), 'render_checks: unbalanced markup reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [sig[0] + '\nОценка доверия']})), 'render_checks: a «сигнал» carrying the six ratings reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [re.sub(CONF, 'X: ', sig[0], count=1)]})), 'render_checks: a card without its confidence reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [sig[0].replace('Уверенность: <b>1/5</b>', 'Уверенность: <b>3/5</b>', 1)]})),
       'render_checks: a confidence that is not the rung reads FAIL')
    four = re.sub(r'(?m)^([🟢🔴] <b>[A-Z0-9]+ · (?:LONG|SHORT)</b>)$', r'\1 · ★ STRONG', top7[0])
    ok(four != top7[0] and bad(texts=dict(texts, **{RENDER_CASES[1]: [four]})), 'render_checks: STRONG beyond the first three of the list reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[4]: [texts[RENDER_CASES[4]][0].replace('+0,22 R', '+0,55 R')]})),
       'render_checks: an assessment quoting the 42\'s STRONG figure reads FAIL')
    ok(bad(expect=dict(expect, consts=(11.1,) + expect['consts'][1:])) and bad(expect=dict(expect, consts=expect['consts'][:7] + (10,) + expect['consts'][8:])),
       'render_checks: another stop limit or another list length reads FAIL')
    c1 = RENDER_CASES[2]
    ok(bad(texts=dict(texts, **{c1: [calc[c1]['parts'][0] + ' ']})), 'render_checks: an allocation reply that is not the plan\'s own reads FAIL')
    p = calc[c1]['plan']
    if p['items']:
        worse = dict(p, items=[dict(p['items'][0], card=dict(p['items'][0]['card'], stop_pct=14.5))] + p['items'][1:])
        ok(bad(calc=dict(calc, **{c1: dict(calc[c1], plan=worse)})), 'render_checks: a stop beyond 14 % in a plan reads FAIL')
        heavy = dict(p, items=[dict(p['items'][0], loss_exact=p['budget'] * 0.0101)] + p['items'][1:])
        ok(bad(calc=dict(calc, **{c1: dict(calc[c1], plan=heavy)})), 'render_checks: a loss at a stop beyond 1 % of the budget reads FAIL')
    sg = runs['signal']
    flipped = dict(sg, rec=dict(sg['rec'], quiet=not sg['rec']['quiet']))
    ok(bad(runs=dict(runs, signal=flipped)), 'render_checks: a check whose quiet flag disagrees with its alerts reads FAIL')
    dropped = dict(sg, rec=dict(sg['rec'], alerts=[a for a in sg['rec']['alerts'] if a['kind'] != 'signal']))
    ok(bad(runs=dict(runs, signal=dropped)), 'render_checks: an exit the walk finds and the check does not alert reads FAIL')
    fa = runs['fact']
    again = dict(fa, rec=dict(fa['rec'], alerts=fa['rec']['alerts'] + [a for a in sg['rec']['alerts'] if a['kind'] == 'stop']))
    ok(bad(runs=dict(runs, fact=again)), 'render_checks: an alert sent twice across the checks reads FAIL')
    ok(bad(runs=dict(runs, fact=dict(fa, rec=dict(fa['rec'], cards=list(sg['rec']['cards']))))), 'render_checks: a fact check offering the close\'s cards reads FAIL')
    ok(bad(kinds=kinds[:-1]) and bad(kinds=['check'] + kinds[1:]), 'render_checks: a journal that lacks a record or has another kind reads FAIL')
    ok(bad(same=False), 'render_checks: the bot\'s own record changed reads FAIL')
    out('SELFTEST PASS: %d of %d checks passed' % (len(done), len(done)))


def main(argv):
    if not argv:
        sys.exit('usage: tz39-advisor-checks.py MODE [ARG]')
    mode, rest = argv[0], argv[1:]
    table = {'fingerprint': mode_fingerprint, 'host': mode_host, 'number': mode_number, 'rule': mode_rule, 'copy': mode_copy,
             'render': mode_render, 'first': mode_first, 'keep': mode_keep, 'stopped': mode_stopped, 'selftest': mode_selftest}
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
