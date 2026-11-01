#!/usr/bin/env python3
# tz40-advisor-strong.py - TZ-40's checker: the fingerprint, the host gate, the number, G-RULE, COPY, G-RENDER, the readings
# after the unit's restart - UNIT-NEW and G-FIRST - and the marks. Standard library only. It starts and stops no unit, signals no
# process and sends no request of its own (G-RENDER runs the service copy's bot, which reads Binance's public market), and it
# never reads or prints the bot's token or the pinned chat, a coin, a price or a size. It writes one file of the unit's record,
# /var/lib/adv3-bot/check-done: at the kill mark the slot before the day's signal check, so that the new process replays that
# check at its start, and at the rollback mark the kill mark's value again where the new process never moved it.
# Exits: 0 every assert held; 1 a failed assert, named; 3 NOT YET.
import ast, bisect, calendar, contextlib, datetime as dt, hashlib, importlib.util, io, json, math, os, re, shutil, subprocess, \
    sys, time

WORK = '/root/tz40-work'
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
TZ_FILE = 'CryptoTZ/TZ-40-strong-every-rank.md'
NUMBER = 'TZ-40-'
BRANCH = 'tz-40-strong-every-rank'
MAP_REV = '2026-11-01-a'
ANCHORS = {'A1': '229a944f2d51', 'A2': '6c5089330629',
           'A3': '0-complete / 1-student-5tau-not-disqualified / 2-no-edge-4tau-240-undecidable',
           'A4': '437b45ea196b', 'A5': '0f6c90451cbd', 'A6': '729f0bcdbee3'}
DERIVED = {'A2': 'research/twap-divergence.py', 'A4': 'BTC-EXECUTOR-INSTRUCTIONS.md',
           'A5': 'research/recorder/recorder.py', 'A6': 'research/pfair.py'}
H = {'adv3_old': 'c19572dccf30a505342ca334e42c7ec347a5d29db4db20887229d2a8c7b48e31',
     'adv3_new': '81ef0112d3fe4b86566e51a51aab924d9776ff37a927e65982ecb0bb7c1f34e1',
     'bot_old': 'ca989b6fe487d41181b32312418d6acda1e9c64fbf5cfbb3f041d54826dd108f',
     'bot_new': '9e622daf2e8a5ec3e93f15c7f56e7cf859547fbd3771daad75bc6532adb2b9d1',
     'selftest_old': '09d2ba9a8361ec5ebc7f5934ebb818d1a685bb16fb3f32b7da94409d9516cc0e',
     'selftest_new': '6f29b82f2b2ca82cd2ff4bbb370e032354dbb4743497330530777429b3af7398',
     'rule': 'ee206e7ce6649329bc8e03f15e32edde51800cd597b549298b89d916b90ef169',
     'unit': '82acd8e44a6e35c4e572f35197ab9861d231b0c647979e8d9dff2105bf5f7e66'}
TZ38 = ('CryptoReports/TZ-38-adv3-pit-validation-report.md', 'f4a0ac3f643ac99dd08f20c8c8c43bf1e98e51b2954592d1456a59ae98030528')
# G-RULE's tables: (changed, added, removed) definitions and assignments of each file against origin/main's
ADV3_DEFS = ({'assessment', 'card_lines', 'message'}, set(), set())
ADV3_RULE = ('signs', 'signal', 'strength', 'true_range', 'unit', 'open_at', 'hold', 'close_at', 'simulate', 'states', 'ranking',
             'simulate_strong', 'stats', 'funding_of', 'report', 'card', 'trust')
ADV3_ASG = ({'PIT'}, {'BEYOND', 'BEYOND_TAG'}, set())
BOT_DEFS = ({'Telegram', 'alerts_of', 'candidate_lines', 'candidates', 'check', 'check_record', 'compose', 'event_lines', 'handle',
             'item_lines', 'offers', 'plan_parts', 'selftest', 'top_n'},
            {'TooMany', 'alloc_fields', 'plan_strong', 'strong_all', 'volumes'}, set())
BOT_SAME = ('plan', 'ranked', 'route', 'Data', 'liquidity', 'follow', 'journal_scan', 'due', 'done_after', 'serve', 'main')
BOT_ASG = ({'CARD_KEYS', 'HELP'}, {'PACE'}, set())
# this TZ's numbers: the allocation's limits, the list's length, the two checks' instants, the rung, the pause between parts
STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, RISK_MAX, RISK_ALL, LIST_MAX, RUNG, PACE, STRONG_Z = 14.0, 5.0, 0.001, 1.0, 5.0, 7, 1, 1.1, 1.0
SLOTS = (('signal', dt.time(0, 10)), ('fact', dt.time(12, 10)))
MEM_FLOOR, DISK_FLOOR = 140_037_206, 7_400_000_000
ROWS, FROZEN = 59, 56
FIRST_BOUND = 900
TZ39_FIRST = '2026-11-01 signal'
RENDER_CASES = ('сигнал', 'сигнал топ 7', 'сигнал 10000 топ 3', 'сигнал 15000 топ 5', 'оценка', 'помощь', 'привет')
RENDER_KINDS = ['request', 'request', 'alloc', 'alloc', 'assess', 'check', 'check']
TRUST = ('Оценка доверия', 'Надёжность системы: <b>1/5</b>', 'Уверенность в сделках:', 'STRONG обоснован: <b>нет</b>',
         'Качество данных: <b>низкое</b>', 'Ожидаемая R на сделку: <b>не установлена</b>', 'Инвалидация: у каждой карточки')
METHOD = ('Оценка доверия', 'Надёжность системы', 'Форвард с 28.10', 'история 2020–2026', 'Открытые STRONG-сделки')
TRUST_KEYS = {'system', 'strong_justified', 'served', 'cards', 'quality', 'fresh', 'complete', 'expectancy_established'}
CARD = re.compile(r'^[🟢🔴] <b>([A-Z0-9]+) · (LONG|SHORT)</b>', re.M)
CONF = re.compile(r'^Уверенность: <b>([0-5])/5</b> — ', re.M)
EXTRA_HEAD = '<b>Дополнительные STRONG-кандидаты</b>'
TAG = ' · вне ТОП-3'
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
                                                  ', the %d this checker names among them' % len(rule) if rule else ''):
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
    median and its share of lists in profit, the size of G, and - TZ-40 - E6's mean R a trade of STRONG with three places and with
    seven; each cell read as a number."""
    sec = report_sections(text)
    pick = lambda prefix: next(v for k, v in sec.items() if k.startswith(prefix))
    e1, e2, e4, e5, e6, sets = pick('E1 '), pick('E2 '), pick('E4 '), pick('E5 '), pick('E6 '), pick('The sets ')
    f = lambda s: float(s.replace(',', ''))
    return {'base': {'mfe': {n: f(e4['mfe +%dR' % n][0]) for n in (1, 2, 3)}, 'mean_R_G': f(e1['mean_R'][0]),
                     'trades_G': int(f(e1['trades'][0])), 'p_G': f(e1['p_t_up'][0]), 'contracts_G': int(f(sets['G'][0]))},
            'strong': {'mfe': {n: f(e4['mfe +%dR' % n][1]) for n in (1, 2, 3)}, 'p_G': f(e2['p_t_up'][0]),
                       'mean_R_lists': f(e5['0.5'][1]), 'lists': int(f(e5['lists'][0])),
                       'lists_positive': f(e5['share_mean_R_positive'][0]), 'top5_share': f(e4['top5_share'][1]),
                       'mean_R_P3': f(e6['mean_R'][0]), 'mean_R_P7': f(e6['mean_R'][2])}}


def html_balanced(text):
    return all(text.count('<%s>' % t) == text.count('</%s>' % t) for t in ('b', 'i'))


def own_order(rows, coins):
    """The rule's order by this checker's own reading: every coin with a LONG or SHORT signal, a strength and a unit, by |z| from
    the largest, ties in the coins' order."""
    act = [c for c in coins if (rows.get(c) or {}).get('signal') in (1, -1) and rows[c].get('z') is not None and rows[c].get('U')]
    return sorted(act, key=lambda c: -abs(rows[c]['z']))


def own_strong(rows, order):
    """STRONG at every rank by this checker's own reading: four signs agreeing with the side and |z| at least 1."""
    return [c for c in order if rows[c].get('sum') == 4 * rows[c]['signal'] and abs(rows[c]['z']) >= STRONG_Z]


def own_stop_pct(row):
    """The stop's distance in percent of the entry a card offers, by RULE-ADV-3's display rules read here: the stop C - k*U; LONG
    above the zone a limit at its top, else at market while more than 0.25*U above the stop, else no entry; SHORT mirrored.
    None where no entry is offered."""
    k, C, U = row['signal'], row['close'], row['U']
    S, P = C - k * U, row.get('mark') or C
    if k > 0:
        entry = C + 0.25 * U if P > C + 0.25 * U else P if P > S + 0.25 * U else None
    else:
        entry = C - 0.25 * U if P < C - 0.25 * U else P if P < S - 0.25 * U else None
    return None if entry is None else 100 * abs(entry - S) / entry


def plan_invariants(p, rep, liq, budget, n, risk):
    """The allocation's limits (TZ-40), read from a plan (the bot's own plan_strong) and the report and liquidity it was made from,
    against this checker's own order, STRONG and stops. The limits are this TZ's: stop 14 %, minimum 5 USDT, liquidity 0.1 %, risk
    1 % a trade and 5 % in all for the placed, the average risk for each of the more."""
    rows = rep['rows']
    order = own_order(rows, list(rows))
    strong = own_strong(rows, order)
    passing = [c for c in strong if rep['marks_ok'] and own_stop_pct(rows[c]) is not None and own_stop_pct(rows[c]) <= STOP_MAX]
    items, more = p['items'], p.get('more') or []
    placed, extra = [it['card']['coin'] for it in items], [it['card']['coin'] for it in more]
    named = [r[0] for r in p['rejected']]
    small = {r[0] for r in p['rejected'] if r[2] == 'позиция меньше 5 USDT'}
    trades = items + more
    return {
        'the placed are the first n STRONG coins at any rank that pass the limits, the more the rest that pass, both in rank order':
            placed == [c for c in passing[:n] if c not in small] and extra == [c for c in passing[n:] if c not in small],
        'every STRONG coin is placed, among the more or named with a reason, once': sorted(placed + extra + named) == sorted(strong),
        'every trade has an entry and a stop within 14 % of it, on current prices': (
            all(it['card']['entry'] is not None and it['card']['stop_pct'] <= STOP_MAX
                and abs(it['card']['stop_pct'] - own_stop_pct(rows[it['card']['coin']])) < 1e-9 for it in trades) and (rep['marks_ok'] or not trades)),
        'each placed loss at its stop within 1 % of the budget and all within 5 %; each of the more within the average risk': (
            all(it['loss_exact'] <= budget * RISK_MAX / 100 + 1e-9 for it in items)
            and sum(it['loss_exact'] for it in items) <= budget * RISK_ALL / 100 + 1e-9
            and all(it['loss_exact'] <= budget * risk / 100 + 1e-9 for it in more)),
        'whole positions of at least 5 USDT, the placed together within the budget, free the budget less them': (
            all(float(it['notional']).is_integer() and MIN_NOTIONAL <= it['notional'] <= budget for it in trades)
            and p['allocated'] == sum(it['notional'] for it in items) <= budget and p['free'] == budget - p['allocated']),
        'leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap': all(
            it['leverage'] == min(20, math.floor(1 / (1.5 * it['card']['stop_pct'] / 100 + 0.01)))
            and it['margin'] * it['leverage'] >= it['notional']
            and ((not liq.get(it['card']['coin'])) or it['notional'] <= LIQ_FRAC * liq[it['card']['coin']]) for it in trades),
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
    before is alerted, and each candidate is a STRONG coin that passes the plan's limits - placed or among the more - that did not
    pass them at the check before."""
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
    placed = [(it['card']['coin'], it['card']['side']) for it in run['plan']['items'] + (run['plan'].get('more') or [])]
    cand = [(a['coin'], a['side']) for a in rec['alerts'] if a['kind'] == 'candidate']
    return sorted(got) == sorted(want) and cand == [x for x in placed if x not in prev_passing]


def card_blocks(text):
    """The card blocks of a message - each from its header line to the blank line after it - as (coin, header line, block text)."""
    out_ = []
    for block in text.split('\n\n'):
        m = CARD.match(block)
        if m:
            out_.append((m.group(1), block.split('\n')[0], block))
    return out_


def list_ok(text, rep, n_of):
    """A list message («сигнал», «сигнал топ N», the signal check) against this checker's own order and STRONG: the rule's first
    n_of coins ranked k of n_of, then every STRONG coin beyond them under the extra heading ranked by its place beyond the list;
    ★ STRONG on a card exactly where the coin is STRONG at any rank, «вне ТОП-3» exactly where such a card's rank is beyond 3;
    every card its basis, its invalidation and one confidence line reading the rung 1 or 0; the footnote once where a tag shows."""
    rows = rep['rows']
    order = own_order(rows, list(rows))
    strong = own_strong(rows, order)
    rank = {c: k for k, c in enumerate(order, 1)}
    want = order[:n_of] + [c for c in order[n_of:] if c in strong]
    blocks = card_blocks(text)
    coins = [c for c, _h, _b in blocks]
    tags = [c for c, h, _b in blocks if h.endswith(TAG)]
    head_ok = all(('★ STRONG' in h) == (c in strong) and h.endswith(TAG) == (c in strong and rank[c] > 3) for c, h, _b in blocks)
    basis_ok = all(('ранг %d из %d' % (rank[c], n_of) if rank[c] <= n_of else 'ранг %d — за ТОП-%d' % (rank[c], n_of)) in b
                   for c, _h, b in blocks)
    each = all(b.count('Основание: сумма знаков') == 1 and b.count('Инвалидация: цена') == 1 and len(CONF.findall(b)) == 1
               and int(CONF.findall(b)[0]) in (0, RUNG) for _c, _h, b in blocks)
    extra_ok = ((EXTRA_HEAD in text) == bool(want[n_of:])) and (not want[n_of:] or text.index(EXTRA_HEAD) < text.index(
        '%s <b>%s · ' % ({1: '🟢', -1: '🔴'}[rows[want[n_of]]['signal']], want[n_of])))
    return coins == want and head_ok and basis_ok and each and extra_ok and (text.count(BEYOND_LINE) == (1 if tags else 0))


BEYOND_LINE = '★ STRONG вне ТОП-3 — четыре знака совпадают и |z| ≥ 1'


def render_checks(texts, calc, runs, kinds, records, log, same, expect):
    """G-RENDER: what the service copy's bot sent for each command (texts, by command, each a list of parts), the reports the list
    commands were made from (calc['lists']), the plan the checker recomputed from the report and liquidity each allocation reply
    was made from (calc), the two checks run on live data (runs), the scratch journal's kinds and records, the bot's log, whether the
    bot's own record is as before, and the bot module's constants (expect); counts and labels only."""
    whole = lambda parts: '\n'.join(parts)
    sig, top7, ass = whole(texts[RENDER_CASES[0]]), whole(texts[RENDER_CASES[1]]), whole(texts[RENDER_CASES[4]])
    allocs = [c for c in RENDER_CASES if c in calc]
    lists = calc.get('lists') or {}
    usdt, num = expect['usdt'], expect['num']
    inv = {c: plan_invariants(calc[c]['plan'], calc[c]['rep'], calc[c]['liq'], calc[c]['budget'], calc[c]['n'], calc[c]['risk'])
           for c in allocs}

    def fields(c):
        p, t = calc[c]['plan'], whole(texts[c])
        more = p.get('more') or []
        head = ('не доказанная' in t and 'Бюджет %s USDT' % num(p['budget'], 6) in t and 'Размещено %s USDT' % usdt(p['allocated']) in t
                and ('Свободно %s USDT' % usdt(p['free']) in t or 'свободно %s USDT' % usdt(p['free']) in t) and 'Оценка доверия' not in t
                and 'STRONG на любом месте рейтинга' in t and 'больше 3 сделок не будет' not in t)
        if not p['items']:
            return head and 'Подходящих сделок нет' in t and not more
        k, m = len(p['items']), len(more)
        total = p['loss'] + sum(it['loss'] for it in more)
        exact = p['loss_exact'] + sum(it['loss_exact'] for it in more)
        more_ok = (EXTRA_HEAD in t) == bool(more) and (not more or (
            'сверх запрошенных %d, в «Итог» не входят' % p['n'] in t and t.count('вне распределения — одна сделка') == m
            and 'Вместе с основными потеря на стопах — %s USDT' % usdt(total) in t
            and ('больше лимита 5%' in t) == (exact > p['budget'] * RISK_ALL / 100 + 1e-9)))
        return (head and more_ok and 'Подходящих сделок: %d из %d запрошенных' % (k, p['n']) in t
                and all(t.count(x) == k + m for x in ('Капитал:', 'Потеря на стопе:', '⛔ Стоп:', 'Инвалидация: цена', 'Качество: z'))
                and t.count('🎯') == 3 * (k + m) and t.count('размеры — формула Архитектора, не доказана') == k + m
                and 'Потеря на стопах %s USDT' % usdt(p['loss']) in t and 'маржа %s USDT' % usdt(p['margin']) in t)

    sg, fa = runs.get('signal'), runs.get('fact')

    def run_shape(r, kind):
        rec, sent = r['rec'], r['sent']
        alerts = rec['alerts']
        loud = bool(alerts)
        flags = all(q == rec['quiet'] for _t, q in sent) and rec['quiet'] == (not loud) and len(sent) >= 1
        text = whole(t for t, _q in sent)
        rows = r['rep']['rows']
        order = own_order(rows, list(rows))
        strong = own_strong(rows, order)
        if rec['one_line']:
            shape = (not loud and len(sent) == 1 and '\n' not in text and text.startswith('✓ ') and rec['cards'] == []
                     and (kind == 'fact' and not rec['zones_left'] or kind == 'signal' and not r['changes'] and r['same'] and not rec['weakened']))
        elif kind == 'signal':
            want = order[:3] + [c for c in order[3:] if c in strong]
            shape = ('STRONG-канд' in text and 'Сделки по карточкам бота' in text and not any(m in text for m in METHOD)
                     and [c['coin'] for c in rec['cards']] == want and list_ok(text, r['rep'], 3)
                     and (loud or r['changes'] or not r['same'] or bool(rec['weakened'])) and (('🔔 <b>События</b>' in text) == loud)
                     and (('ℹ️ Ослабление' in text) == bool(rec['weakened'])))
        else:
            shape = (('🔔 <b>События</b>' in text) == loud and (loud or bool(rec['zones_left'])) and CARD.findall(text) == []
                     and [(c['coin'], c['side']) for c in rec['cards']] == [(a['coin'], a['side']) for a in alerts if a['kind'] == 'candidate'])
        return flags and shape and all(html_balanced(t) for t, _q in sent)

    def record_ok(r, kind):
        rec, p = r['rec'], r['plan']
        rows = r['rep']['rows']
        order = own_order(rows, list(rows))
        return (rec['kind'] == 'check' and rec['slot'].endswith(' ' + kind) and len(rec['state']) == 42 and TRUST_KEYS <= set(rec['trust'])
                and rec['rule'] == H['rule'] and rec['close_of'] == r['rep']['close_of']
                and rec['passing'] == [[it['card']['coin'], it['card']['side']] for it in p['items'] + (p.get('more') or [])]
                and rec['strong_all'] == own_strong(rows, order) and isinstance(rec['alloc'].get('more'), list)
                and len(rec['alloc']['more']) == len(p.get('more') or []) and all('extra' in c for c in rec['cards'])
                and all(rec['state'][c]['rank'] == k for k, c in enumerate(order, 1)))

    ok_inv = lambda key: all(v[key] for v in inv.values())
    c5 = RENDER_CASES[3]
    return {
        'every command and both checks answered, no traceback and no failed request in the bot\'s log':
            all(texts[k] for k in RENDER_CASES) and sg is not None and fa is not None and 'Traceback' not in log and 'failed' not in log,
        'the markup is balanced in every part of every message (b, i)': all(html_balanced(t) for ps in texts.values() for t in ps),
        '«сигнал»: the TOP-3 ranked k of 3, then every STRONG coin beyond them, extra; ★ STRONG and «вне ТОП-3» exactly where they '
        'belong; each card its basis, invalidation and confidence, the rung 1 or 0; no methodology':
            RENDER_CASES[0] in lists and list_ok(sig, lists[RENDER_CASES[0]], 3) and not any(m in sig for m in METHOD)
            and 'на чём держится уверенность' in sig,
        '«сигнал топ 7»: the first seven ranked k of 7, then every STRONG coin beyond them, extra, with the same labels and lines':
            RENDER_CASES[1] in lists and list_ok(top7, lists[RENDER_CASES[1]], 7) and 'ТОП-7 по силе тренда' in top7,
        '«оценка»: the rung and the next readings, the six ratings, the forward record; STRONG at the lists\' median, never the 42\'s; '
        'STRONG beyond the TOP-3 not the measured strategy, E6\'s +0,51 R against +0,80':
            all(k in ass for k in TRUST + ('рубеж 1 из 5', 'после закрытия 28.10.2027', 'после закрытия 31.10.2027', 'Форвард с 28.10',
                                           '★ STRONG вне ТОП-3 — те же условия', 'дал +0,51 R на сделку против +0,80 на трёх'))
            and '+0,22 R' in ass and '+0,04 R' in ass and '0,55' not in ass,
        'the bot\'s constants are this TZ\'s: 14 % a stop, 5 USDT, 0.1 % of the volume, 1 % and 5 % of risk, three places, 0.1 % a side, '
        'a list of 7, checks at 00:10 and 12:10 UTC, the rung 1, 1.1 s between parts, |z| 1 for STRONG':
            expect['consts'] == (STOP_MAX, MIN_NOTIONAL, LIQ_FRAC, RISK_MAX, RISK_ALL, 3, 0.001, LIST_MAX, SLOTS, RUNG, PACE, STRONG_Z),
        'each allocation reply is the bot\'s own plan_parts of plan_strong over the report and liquidity it was made from':
            len(allocs) == 2 and all(whole(texts[c]) == whole(calc[c]['parts']) for c in allocs),
        'plan: the placed are the first n STRONG coins at any rank that pass the limits, the more the rest that pass, in rank order':
            ok_inv('the placed are the first n STRONG coins at any rank that pass the limits, the more the rest that pass, both in rank order'),
        'plan: every STRONG coin is placed, among the more or named with a reason, once':
            ok_inv('every STRONG coin is placed, among the more or named with a reason, once'),
        'plan: every trade has an entry and a stop within 14 % of it, on current prices':
            ok_inv('every trade has an entry and a stop within 14 % of it, on current prices'),
        'plan: each placed loss within 1 % of the budget and all within 5 %, each of the more within the average risk':
            ok_inv('each placed loss at its stop within 1 % of the budget and all within 5 %; each of the more within the average risk'),
        'plan: whole positions of at least 5 USDT, the placed together within the budget, free the budget less them':
            ok_inv('whole positions of at least 5 USDT, the placed together within the budget, free the budget less them'),
        'plan: leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap':
            ok_inv('leverage the rule\'s formula and at most 20, the margin covering the position, a position within its liquidity cap'),
        'the Boss\'s fields in each allocation reply - budget, count, allocated, free, for each trade capital, leverage, margin, loss, stop, '
        'targets, invalidation and its confidence with the note that the sizes are unproven, the more under their own heading with the '
        'loss of all together against 5 % - and no six ratings': len(allocs) == 2 and all(fields(c) for c in allocs),
        '«сигнал 15000 топ 5» places at most five, the other STRONG that pass among the more, and says nothing of three':
            c5 in calc and len(calc[c5]['plan']['items']) <= 5 and 'больше 3 сделок не будет' not in whole(texts[c5]),
        '«помощь» and an unknown text answer HELP and nothing else': texts[RENDER_CASES[5]] == [expect['help']] == texts[RENDER_CASES[6]],
        'the signal check: quiet exactly when it holds no alert, one line only where it finds nothing, else the close\'s TOP-3 and the '
        'STRONG beyond it, the candidates and the offered trades': sg is not None and run_shape(sg, 'signal'),
        'the fact check: quiet exactly when it holds no alert, one line where it finds neither an alert nor a zone left, no card but '
        'a new candidate\'s': fa is not None and run_shape(fa, 'fact'),
        'the alerts of both checks are the exits of the offered trades by this checker\'s own walk, each once, and the new candidates':
            sg is not None and fa is not None and alert_checks(sg, sg['cs'], sg['prev_passing']) and alert_checks(fa, fa['cs'], fa['prev_passing'])
            and not ({(a['kind'], a['coin'], a['side'], a['close_of']) for a in sg['rec']['alerts'] if a['kind'] != 'candidate'}
                     & {(a['kind'], a['coin'], a['side'], a['close_of']) for a in fa['rec']['alerts'] if a['kind'] != 'candidate'}),
        'the check records: their slots, every coin\'s state ranked, the six ratings, the coins that pass, the STRONG at every rank, the '
        'more, each card\'s extra': sg is not None and fa is not None and record_ok(sg, 'signal') and record_ok(fa, 'fact'),
        'the scratch journal holds, after the bot\'s own records, request, request, alloc, alloc, assess, check, check':
            kinds == RENDER_KINDS and all(r.get('cards') is not None for r in records),
        'the bot\'s own journal, offset, daily-sent and check-done are as before the run': same is True,
    }


def unit_checks(which, pre, now):
    """UNIT-NEW and UNIT-OLD's nine readings after a restart: now is what the modes read; pre is the snapshot of the kill mark, which
    names the check-done the new process must read at its start."""
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
        'the log shows the new process serving from check-done %s' % pre['read_done']: now['serving'] and now['read'] == pre['read_done'],
        'no traceback in the log since the mark': not now['traceback'],
        'the three capture units unchanged, each active': all(
            now['caps'][u]['ActiveState'] == 'active' and now['caps'][u]['MainPID'] == pre['caps'][u]['MainPID']
            and now['caps'][u]['NRestarts'] == pre['caps'][u]['NRestarts'] for u in CAPTURES),
    }


def first_checks(pre, recs, done_text, log, pid, tail_ok):
    """G-FIRST: the new process's first check - the day's signal check, replayed at its start because the kill mark set check-done
    to the slot before it - from the journal's records stamped after the kill mark, the check-done file and service.log's lines
    since the mark."""
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
        'it holds the 42 coins\' state, the six ratings, its alerts, the coins that pass, the STRONG at every rank and the more, each card '
        'its extra; quiet exactly without an alert': (
            len(r.get('state') or {}) == 42 and TRUST_KEYS <= set(r.get('trust') or {}) and isinstance(r.get('alerts'), list)
            and isinstance(r.get('passing'), list) and isinstance(r.get('strong_all'), list)
            and isinstance((r.get('alloc') or {}).get('more'), list) and all('extra' in c for c in r.get('cards') or [])
            and r.get('quiet') == (not r.get('alerts'))),
        'check-done names the slot it covers: %s' % want_done: done_text == want_done,
        'the log since the mark: the new process serving from check-done %s, the check sent, no check failed and no traceback' % pre['read_done']: (
            ('serving the pinned chat: pid %d ' % pid in log and 'check-done %s' % pre['read_done'] in log) and 'check sent: %s signal' % day in log
            and 'check failed' not in log and 'Traceback' not in log),
        'the journal ends in a newline and every line since the mark parses': tail_ok,
    }


def slot_instant(text):
    """The instant of a slot 'YYYY-MM-DD signal|fact' as epoch seconds, or None."""
    try:
        day, kind = text.split()
        at = dict(SLOTS)[kind]
        return calendar.timegm(dt.datetime.combine(dt.date.fromisoformat(day), at).timetuple())
    except (ValueError, KeyError, AttributeError):
        return None


def slot_order(text):
    day, kind = text.split()
    return day, [k for k, _ in SLOTS].index(kind)


def latest_slot_text(t):
    """The last slot whose instant is at or before the epoch second t, read here: 00:10 and 12:10 UTC."""
    d = dt.datetime.fromtimestamp(t, dt.timezone.utc)
    for kind, at in reversed(SLOTS):
        if d.time() >= at:
            return '%s %s' % (d.date(), kind)
    return '%s %s' % (d.date() - DAY, SLOTS[-1][0])


def replay_text(t):
    """The slot the kill mark writes to check-done: the one before the UTC day's signal check, the day before's fact - so that
    the new process's schedule owes, and runs at its start, the day's signal check."""
    return '%s %s' % (dt.datetime.fromtimestamp(t, dt.timezone.utc).date() - DAY, SLOTS[-1][0])


def clock_checks(recs, done_text):
    """H7, that the clock fires (map §2.7): the journal's check records from TZ-39's first name strictly later slots, each once;
    every one after TZ-39's first - at least one - stamped at or after its slot's instant; and check-done names the last one's slot,
    or that day's fact where the last is a signal check stamped at or after 12:10 UTC. (checks, the delays in seconds)."""
    checks_ = [r for r in recs if r.get('kind') == 'check']
    slots = [r.get('slot') for r in checks_]
    later = checks_[1:]
    delays = []
    for r in later:
        at = slot_instant(r.get('slot') or '')
        try:
            delays.append(dt.datetime.fromisoformat(r['utc']).timestamp() - at)
        except (KeyError, TypeError, ValueError):
            delays.append(None)
    last = checks_[-1] if checks_ else {}
    covered = None
    if last.get('slot', '').endswith(' signal'):
        day = last['slot'].split()[0]
        covered = '%s fact' % day if dt.datetime.fromisoformat(last['utc']).timestamp() >= slot_instant('%s fact' % day) else None
    ok_slots = all(slot_instant(x or '') is not None for x in slots)
    return {
        'H7 the check records from TZ-39\'s first, %s, name strictly later slots, each once' % TZ39_FIRST: (
            bool(slots) and slots[0] == TZ39_FIRST and ok_slots
            and all(slot_order(a) < slot_order(b) for a, b in zip(slots, slots[1:]))),
        'H7 every check after TZ-39\'s first - at least one - stamped at or after its slot\'s instant': (
            bool(later) and all(x is not None and x >= 0 for x in delays)),
        'H7 check-done names the last check\'s slot, or the fact slot its signal check covered': (
            done_text is not None and done_text in (last.get('slot'), covered)),
    }, delays


def served_from(text, pid):
    """The check-done a process logged at its start - 'serving the pinned chat: pid <pid> offset <n> check-done <slot>' - or None."""
    m = None
    for m in re.finditer(r'serving the pinned chat: pid %d offset \d+ check-done (\d{4}-\d{2}-\d{2} (?:signal|fact)|-)$' % pid, text, re.M):
        pass
    return m.group(1) if m else None


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
    checks['H5 adv3.py and adv3-bot.py are TZ-39\'s'] = (
        sha256_file(SVC + '/adv3.py') == H['adv3_old'] and sha256_file(SVC + '/adv3-bot.py') == H['bot_old'])
    checks['H5 the installed unit file is TZ-35\'s'] = sha256_file('/etc/systemd/system/adv3-bot.service') == H['unit']
    checks['H5 commit.txt is 40 hex characters and a newline'] = re.fullmatch(r'[0-9a-f]{40}\n', read(SVC + '/commit.txt')) is not None
    jtext = read(BOTDIR + '/journal.jsonl')
    done_text = read(BOTDIR + '/check-done').strip() if os.path.exists(BOTDIR + '/check-done') else None
    checks['H6 the record holds a journal of whole lines and a check-done naming a slot'] = (
        jtext.endswith('\n') and done_text is not None and slot_instant(done_text) is not None)
    recs, _ok = records_since(jtext, 0)
    clock, delays = clock_checks(recs, done_text)
    checks.update(clock)
    out('check records: %d; slots %s; delays after their instants, seconds: %s; check-done %s' % (
        sum(r.get('kind') == 'check' for r in recs), ' '.join(r['slot'].replace(' signal', ' s').replace(' fact', ' f') for r in recs
                                                         if r.get('kind') == 'check' and isinstance(r.get('slot'), str)),
        ' '.join('-' if x is None else '%.0f' % x for x in delays), done_text or '-'))
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
    checks.update(tree_checks('adv3-bot.py', git_show('advisor/adv3-bot.py'), read(WT + '/advisor/adv3-bot.py'), BOT_DEFS, BOT_ASG, BOT_SAME))
    checks['the branch\'s adv3.py, adv3-bot.py and selftest-adv3.py are Appendix A\'s'] = (
        sha256_file(WT + '/advisor/adv3.py'), sha256_file(WT + '/advisor/adv3-bot.py'), sha256_file(WT + '/advisor/selftest-adv3.py')) == (
        H['adv3_new'], H['bot_new'], H['selftest_new'])
    verdict('RULE', checks)


def snapshot():
    """What a mark records: the instant, the bot's and the captures' units, the record's check count and lines, and check-done."""
    text = read(BOTDIR + '/journal.jsonl')
    return {'t': time.time(), 'bot': show(BOT, 'MainPID', 'NRestarts', 'ActiveState'),
            'caps': {u: show(u, 'MainPID', 'NRestarts', 'ActiveState') for u in CAPTURES},
            'checks': count_kind(text, 'check'), 'lines': text.count('\n'),
            'check_done': read(BOTDIR + '/check-done').strip() if os.path.exists(BOTDIR + '/check-done') else None}


def put_done(text):
    """check-done replaced in one rename, as the bot's own put writes it."""
    tmp = BOTDIR + '/check-done.tz40'
    with open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, BOTDIR + '/check-done')


def mode_mark(name):
    """A mark: the snapshot, kept in state.json. kill refuses unless check-done names the latest slot - the running process owes no
    check - and then writes check-done to the slot before the UTC day's signal check, so that the new process replays that check
    at its start (G-FIRST); the old process holds its slot in memory and never reads the file again. rollback writes the kill mark's
    check-done back where the new process never moved it from the replay slot. kill2 writes nothing and records the check-done the
    old code will read at its start, a slot it may owe and run then."""
    assert name in ('deploy', 'kill', 'rollback', 'kill2'), name
    st = load_state()
    snap = snapshot()
    if name == 'kill':
        latest = latest_slot_text(snap['t'])
        assert snap['check_done'] == latest, 'a check is owed: check-done %s, the latest slot %s' % (snap['check_done'], latest)
        snap['read_done'] = replay_text(snap['t'])
        put_done(snap['read_done'])
        assert read(BOTDIR + '/check-done').strip() == snap['read_done'], 'check-done not written'
    if name == 'kill2':
        snap['read_done'] = snap['check_done']
    if name == 'rollback' and 'kill' in st.get('marks', {}):
        kill = st['marks']['kill']
        snap['restored'] = snap['check_done'] == kill['read_done']
        if snap['restored']:
            put_done(kill['check_done'])
            assert read(BOTDIR + '/check-done').strip() == kill['check_done'], 'check-done not restored'
    st.setdefault('marks', {})[name] = snap
    save_state(st)
    out('mark %s at %s: bot pid %s NRestarts %s, %d check records, check-done %s%s' % (
        name, time.strftime('%FT%TZ', time.gmtime(snap['t'])), snap['bot']['MainPID'], snap['bot']['NRestarts'], snap['checks'],
        snap['check_done'] or '-', (' -> %s, replayed by the new process at its start' % snap['read_done']) if name == 'kill'
        else (' -> restored to %s' % st['marks']['kill']['check_done']) if snap.get('restored') else ''))


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


def line_count(path):
    """The lines of a file, read one at a time: a year's journal is never held whole."""
    with open(path, encoding='utf-8') as fh:
        return sum(1 for _line in fh)


def lines_after(path, k):
    """The records of a journal's lines after its first k, each parsed, read one at a time."""
    with open(path, encoding='utf-8') as fh:
        return [json.loads(line) for n, line in enumerate(fh) if n >= k]


def render_run(mod, data, now):
    """G-RENDER's pipeline on a loaded bot and a Data: the commands answered through the bot's handle, then the signal check and
    the fact check through its check, each appended to its STATE's journal; Telegram a stand-in, the reports, volumes and forming
    candles the bot read captured - the list commands' reports kept in calc['lists'] - and each allocation's plan recomputed by the
    bot's plan_strong from the very report and volumes its reply was made from. (texts, calc, runs, records, log, expect)."""
    base_lines = line_count(mod.STATE + '/journal.jsonl')

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
                if cmd and cmd[0] == 'signal' and len(seen) == m0 + 1:
                    calc.setdefault('lists', {})[case] = seen[-1]
                if cmd and cmd[0] == 'alloc' and len(seen) == m0 + 1:
                    _k, budget, n, risk = cmd
                    rep = mod.top_n(seen[-1], mod.adv3.TOP_N)
                    p = mod.plan_strong(rep, data.cs, budget, n, risk, dict(liqs))
                    calc[case] = {'rep': rep, 'liq': dict(liqs), 'plan': p, 'budget': budget, 'n': n, 'risk': risk,
                                  'parts': mod.plan_parts(rep, p)}
            for kind in ('signal', 'fact'):
                scan = mod.journal_scan()
                n0, m0 = len(cap.sent), len(seen)
                liqs.clear()
                formed.clear()
                rec = mod.check(cap, data, (now.date(), kind), now)
                mod.append(rec)
                rep = mod.top_n(seen[m0], mod.adv3.TOP_N)
                p = mod.plan_strong(rep, data.cs, mod.adv3.DEPOSIT, mod.adv3.TOP_N, mod.adv3.RISK, dict(liqs))
                prev, rows = scan[2], rep['rows']
                runs[kind] = {'rec': rec, 'sent': cap.sent[n0:], 'scan': scan, 'rep': rep, 'plan': p, 'forming': dict(formed),
                              'last': dt.date.fromisoformat(rep['close_of']), 'cs': data.cs,
                              'prev_passing': {(c, s) for c, s in (prev or {}).get('passing') or []},
                              'changes': any(rows[c].get('signal') != rows[c].get('prev')
                                             and (rows[c].get('signal') in (1, -1) or rows[c].get('prev') in (1, -1)) for c in mod.adv3.COINS),
                              'same': prev is not None and prev.get('top') == rep['top'] and prev.get('strong') == rep['strong']
                              and all((prev.get('signals') or {}).get(c) == rows[c].get('signal') for c in rep['top'])
                              and isinstance(prev.get('strong_all'), list)
                              and sorted(prev['strong_all']) == sorted(own_strong(rows, own_order(rows, list(rows))))}
    finally:
        mod.live_report, mod.liquidity, mod.forming_candles = real_lr, real_liq, real_form
    records = lines_after(mod.STATE + '/journal.jsonl', base_lines)
    m = mod.adv3
    expect = {'help': mod.HELP, 'usdt': m.usdt, 'num': m.num,
              'consts': (mod.STOP_MAX, mod.MIN_NOTIONAL, mod.LIQ_FRAC, m.RISK_MAX, m.RISK_ALL, m.TOP_N, m.COST, mod.LIST_MAX, mod.SLOTS,
                         m.RELIABILITY, mod.PACE, m.STRONG_Z)}
    return texts, calc, runs, records, buf.getvalue(), expect


def render_print(texts, calc, runs, log):
    """What G-RENDER prints: sizes, counts and labels, never a coin, a price or a size."""
    lists = calc.get('lists') or {}
    strong = {c: len(own_strong(r['rows'], own_order(r['rows'], list(r['rows'])))) for c, r in lists.items()}
    allocs = [c for c in RENDER_CASES if c in calc]
    out('replies: %s; the bot\'s log: %d lines; STRONG at every rank: %s; per allocation, placed and more: %s' % (
        ', '.join('%d chars in %d parts' % (sum(map(len, texts[k])), len(texts[k])) for k in RENDER_CASES), log.count('\n'),
        ', '.join(str(v) for v in strong.values()) or '-',
        ', '.join('%d and %d' % (len(calc[c]['plan']['items']), len(calc[c]['plan'].get('more') or [])) for c in allocs)))
    for kind, r in runs.items():
        rec = r['rec']
        out('%s check: %s, %s, %d parts; alerts %s; offers read %d, followed %d; cards %d, of them extra %d; passing %d; STRONG at every '
            'rank %d; zones left %d; forming candles read %d' % (
                kind, 'quiet' if rec['quiet'] else 'loud', 'one line' if rec['one_line'] else 'full', len(r['sent']),
                json.dumps({k: sum(a['kind'] == k for a in rec['alerts']) for k in ('stop', 'signal', 'candidate')}, sort_keys=True),
                len(r['scan'][0]), len(rec['followed']), len(rec['cards']), sum(bool(c.get('extra')) for c in rec['cards']),
                len(rec['passing']), len(rec.get('strong_all') or []), len(rec['zones_left']), len(r['forming'])))


def mode_render():
    """G-RENDER: the service copy's bot answers the commands and runs both checks on live data, its Telegram a stand-in, its
    STATE a scratch directory holding a copy of the bot's own journal, so the trades its cards offered are the real ones. Its
    process's peak resident set and its time are printed (map §7 item 145): the mode is its own wrapper."""
    t0, c0 = time.time(), time.process_time()
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
    same = own == own_files()
    render_print(texts, calc, runs, log)
    import resource
    out('PEAK %d bytes resident; %.2f s of wall, %.2f s of processor' % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024,
                                                                       time.time() - t0, time.process_time() - c0))
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
    serving, text, tb = log_since(read(BOTDIR + '/service.log'), pre['t'], pid)
    now = {'bot': bot, 'caps': caps, 'start': start, 'copy_t': copy_t, 'argv': proc_argv(pid) if pid else None, 'procs': procs(ARGV),
           'sha_adv3': sha256_file(SVC + '/adv3.py'), 'sha_bot': sha256_file(SVC + '/adv3-bot.py'),
           'sha_unit': sha256_file('/etc/systemd/system/adv3-bot.service'), 'serving': serving, 'read': served_from(text, pid),
           'traceback': tb}
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
    out('first check: %s, %s, %d messages; alerts %s; followed %d; cards %d, of them extra %d; passing %d; STRONG at every rank %d; '
        'check-done %s' % (
            'quiet' if r.get('quiet') else 'loud', 'one line' if r.get('one_line') else 'full', len(r.get('message_ids') or []),
            json.dumps({k: sum(a.get('kind') == k for a in r.get('alerts') or []) for k in ('stop', 'signal', 'candidate')}, sort_keys=True),
            len(r.get('followed') or []), len(r.get('cards') or []), sum(bool(c.get('extra')) for c in r.get('cards') or []),
            len(r.get('passing') or []), len(r.get('strong_all') or []), done_text or '-'))
    verdict('FIRST', first_checks(pre, recs, done_text, text, pid, tail_ok))


def kept_files():
    """The work tree's files a report keeps by name: state.json, the three files B-DEPLOY saves, and every file under logs/;
    relative to WORK, sorted."""
    names = ['state.json', 'adv3.before', 'bot.before', 'commit.before']
    for d, _s, fs in os.walk(WORK + '/logs'):
        names += [os.path.relpath(os.path.join(d, f), WORK) for f in fs]
    return sorted(n for n in names if os.path.isfile(os.path.join(WORK, n)))


def mode_keep():
    """B-RECLAIM-OWN's copy: every kept file into the forensic store as tz40-work--<path with - for />, by exclusive create and
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
        dest = FORENSICS + '/tz40-work--' + rel.replace('/', '--')
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
           '#### E6 — STRONG with 3, 5 and 7 places\n\n| field | top3 | top5 | top7 |\n|---|---|---|---|\n| `trades` | 265 | 449 | 620 |\n'
           '| `mean_R` | 0.7962 | 0.5491 | 0.5084 |\n\n| variant | bucket | trades |\n|---|---|---|\n| top3 | `1-3` | 265 |\n\n'
           '#### The sets and the frozen FACTS\n\n| `G` | 570 |\n')
    want = {'base': {'mfe': {1: 0.2318, 2: 0.1257, 3: 0.0759}, 'mean_R_G': 0.0403, 'trades_G': 19002, 'p_G': 0.0735, 'contracts_G': 570},
            'strong': {'mfe': {1: 0.4717, 2: 0.2906, 3: 0.1887}, 'p_G': 0.11, 'mean_R_lists': 0.2195, 'lists': 500, 'lists_positive': 0.86,
                       'top5_share': 0.9875, 'mean_R_P3': 0.7962, 'mean_R_P7': 0.5084}}
    ok(pit_from_report(rpt) == want, 'pit_from_report: every figure read from its section and row, E6\'s three places and seven among them')
    ok(pit_from_report(rpt.replace('| 0.5 | 37.7116 | 0.2195 |', '| 0.5 | 37.7116 | 0.2196 |')) != want
       and pit_from_report(rpt.replace('| 0.7962 | 0.5491 | 0.5084 |', '| 0.7962 | 0.5491 | 0.5085 |')) != want,
       'pit_from_report: a changed cell, E5\'s or E6\'s, reads another PIT')
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
    rows_o = {'A': {'signal': 1, 'z': 2.0, 'sum': 4, 'U': 1.0}, 'B': {'signal': -1, 'z': -3.0, 'sum': -4, 'U': 1.0},
              'C': {'signal': 1, 'z': 2.0, 'sum': 2, 'U': 1.0}, 'D': {'signal': 0, 'z': 9.0, 'sum': 0, 'U': 1.0},
              'E': {'signal': 1, 'z': 0.9, 'sum': 4, 'U': 1.0}, 'F': {'signal': -1, 'z': None, 'sum': None, 'U': 1.0}, 'G': {'signal': None}}
    ord_o = own_order(rows_o, list(rows_o))
    ok(ord_o == ['B', 'A', 'C', 'E'] and own_strong(rows_o, ord_o) == ['B', 'A'],
       'own_order and own_strong: by |z| with ties in the coins\' order, out of the market and without a strength left out; STRONG four '
       'agreeing signs and |z| at least 1')
    r_l = {'signal': 1, 'close': 100.0, 'U': 8.0}
    ok(abs(own_stop_pct(dict(r_l, mark=101.0)) - 100 * 9 / 101) < 1e-12 and abs(own_stop_pct(dict(r_l, mark=103.0)) - 100 * 10 / 102) < 1e-12
       and own_stop_pct(dict(r_l, mark=93.5)) is None and abs(own_stop_pct(dict(r_l, mark=97.0)) - 100 * 5 / 97) < 1e-12
       and abs(own_stop_pct(dict(r_l, signal=-1, mark=97.0)) - 100 * 10 / 98) < 1e-12 and abs(own_stop_pct(dict(r_l, mark=None)) - 8.0) < 1e-12,
       'own_stop_pct: at market inside the zone, a limit at its top above it, none near the stop, at market below the zone clear of it; '
       'a short mirrored; no mark, the close')
    t_k = calendar.timegm(time.strptime('2026-11-03T09:00:00', '%Y-%m-%dT%H:%M:%S'))
    ok([latest_slot_text(t_k), latest_slot_text(t_k + 4 * 3600), latest_slot_text(t_k - 9 * 3600 + 1), replay_text(t_k), replay_text(t_k + 6 * 3600)]
       == ['2026-11-03 signal', '2026-11-03 fact', '2026-11-02 fact', '2026-11-02 fact', '2026-11-02 fact'],
       'latest_slot_text and replay_text: 09:00 the day\'s signal, 13:00 its fact, 00:00:01 the day before\'s fact; the replay the day before\'s fact')
    srv = ('2026-11-03T09:01:00Z serving the pinned chat: pid 11 offset 9 check-done 2026-11-02 fact\n'
           '2026-11-03T09:01:01Z serving the pinned chat: pid 12 offset 9 check-done -')
    ok(served_from(srv, 11) == '2026-11-02 fact' and served_from(srv, 12) == '-' and served_from(srv, 13) is None,
       'served_from: the check-done a process logged at its start, \'-\' for none, None for a pid that did not serve')
    mk = lambda slot, utc: {'kind': 'check', 'slot': slot, 'utc': utc}
    good_c = [{'kind': 'daily', 'utc': '2026-11-01T06:00:00+00:00'}, mk('2026-11-01 signal', '2026-11-01T06:51:46+00:00'),
              mk('2026-11-01 fact', '2026-11-01T12:10:09+00:00'), mk('2026-11-02 signal', '2026-11-02T00:10:12+00:00'),
              {'kind': 'request', 'utc': '2026-11-02T08:00:00+00:00'}, mk('2026-11-02 fact', '2026-11-02T12:15:30+00:00')]
    ck_, dl_ = clock_checks(good_c, '2026-11-02 fact')
    ok(all(ck_.values()) and len(ck_) == 3 and [round(x) for x in dl_] == [9, 12, 330],
       'clock_checks: TZ-39\'s first, then slots each once, each stamped after its instant - a retry\'s 330 s among them - and check-done '
       'the last: 3 of 3')
    covered = good_c[:4] + [mk('2026-11-03 signal', '2026-11-03T12:20:00+00:00')]
    ok(all(clock_checks(covered, '2026-11-03 fact')[0].values()) and all(clock_checks(covered, '2026-11-03 signal')[0].values()),
       'clock_checks: a signal check that ended after 12:10 covers its day\'s fact in check-done')
    for label, recs_, done_ in (('a slot twice', good_c + [mk('2026-11-02 fact', '2026-11-02T12:20:00+00:00')], '2026-11-02 fact'),
                                ('a check stamped before its slot', good_c[:3] + [mk('2026-11-02 signal', '2026-11-02T00:09:00+00:00')], '2026-11-02 signal'),
                                ('no check after TZ-39\'s first', good_c[:2], '2026-11-01 signal'),
                                ('another first', good_c[2:], '2026-11-02 fact'),
                                ('a check-done not the last', good_c, '2026-11-02 signal'),
                                ('no check-done', good_c, None)):
        ok(not all(clock_checks(recs_, done_)[0].values()), 'clock_checks: %s reads FAIL' % label)
    pre = {'t': 1000.0, 'bot': {'MainPID': '10', 'NRestarts': '2'}, 'read_done': '2026-11-02 fact',
           'caps': {u: {'MainPID': str(i), 'NRestarts': '0', 'ActiveState': 'active'} for i, u in enumerate(CAPTURES, 20)}}
    now = {'bot': {'MainPID': '11', 'NRestarts': '3', 'ActiveState': 'active', 'SubState': 'running', 'UnitFileState': 'enabled'},
           'caps': dict(pre['caps']), 'start': 1035.0, 'copy_t': 990.0, 'argv': ARGV, 'procs': [11], 'sha_adv3': H['adv3_new'],
           'sha_bot': H['bot_new'], 'sha_unit': H['unit'], 'serving': True, 'read': '2026-11-02 fact', 'traceback': False}
    ok(all(unit_checks('new', pre, now).values()) and len(unit_checks('new', pre, now)) == 9, 'unit_checks: a clean restart reads 9 of 9')
    for key, val, label in (('read', '2026-11-03 signal', 'a process that read another check-done'), ('start', 1200.0, 'a process started 200 s after the kill'),
                            ('sha_bot', H['bot_old'], 'the old bot'), ('sha_adv3', H['adv3_old'], 'the old adv3.py'),
                            ('traceback', True, 'a traceback since the mark'), ('procs', [11, 12], 'a second process under the argv'),
                            ('serving', False, 'no serving line of the new pid')):
        ok(not all(unit_checks('new', pre, dict(now, **{key: val})).values()), 'unit_checks: %s reads FAIL' % label)
    moved = {u: dict(cc, NRestarts='1') for u, cc in pre['caps'].items()}
    ok(not all(unit_checks('new', pre, dict(now, caps=moved)).values()), 'unit_checks: a capture unit restarted reads FAIL')
    ok(all(unit_checks('old', pre, dict(now, sha_bot=H['bot_old'], sha_adv3=H['adv3_old'])).values()), 'unit_checks: the rollback reads the old files')
    t0 = calendar.timegm(time.strptime('2026-11-02T14:00:00', '%Y-%m-%dT%H:%M:%S'))
    pre_f = dict(pre, t=float(t0), read_done='2026-11-01 fact')
    rec = {'utc': '2026-11-02T14:00:50+00:00', 'kind': 'check', 'slot': '2026-11-02 signal', 'close_of': '2026-11-01', 'rule': H['rule'],
           'message_ids': [5, 6], 'state': {str(k): {} for k in range(42)}, 'trust': {k: 0 for k in TRUST_KEYS}, 'alerts': [], 'passing': [],
           'strong_all': [], 'alloc': {'more': []}, 'cards': [{'coin': 'BTC', 'extra': False}], 'quiet': True}
    log_f = ('2026-11-02T14:00:35Z serving the pinned chat: pid 11 offset 9 check-done 2026-11-01 fact\n'
             '2026-11-02T14:00:50Z check sent: 2026-11-02 signal for the close of 2026-11-01 | alerts 0 | quiet | full')
    good = first_checks(pre_f, [rec], '2026-11-02 fact', log_f, 11, True)
    ok(all(good.values()) and len(good) == 7, 'first_checks: the replayed signal check after a 14:00 restart reads 7 of 7, check-done covering 12:10')
    ok(all(first_checks(dict(pre_f, t=float(t0 - 4 * 3600)), [rec], '2026-11-02 signal', log_f.replace('14:00:35', '10:00:35'), 11, True).values()),
       'first_checks: a 10:00 restart wants check-done at the signal slot')
    for label, args in (('no check record', ([], '2026-11-02 fact', log_f, 11, True)),
                        ('two check records', ([rec, rec], '2026-11-02 fact', log_f, 11, True)),
                        ('another slot', ([dict(rec, slot='2026-11-02 fact')], '2026-11-02 fact', log_f, 11, True)),
                        ('no message ids', ([dict(rec, message_ids=[])], '2026-11-02 fact', log_f, 11, True)),
                        ('a loud check without an alert', ([dict(rec, quiet=False)], '2026-11-02 fact', log_f, 11, True)),
                        ('a record without the STRONG at every rank', ([{k: v for k, v in rec.items() if k != 'strong_all'}], '2026-11-02 fact', log_f, 11, True)),
                        ('a card without its extra', ([dict(rec, cards=[{'coin': 'BTC'}])], '2026-11-02 fact', log_f, 11, True)),
                        ('check-done at the signal after 12:10', ([rec], '2026-11-02 signal', log_f, 11, True)),
                        ('a failed check in the log', ([rec], '2026-11-02 fact', log_f + '\ncheck failed: x', 11, True)),
                        ('a start from another check-done', ([rec], '2026-11-02 fact', log_f.replace('check-done 2026-11-01 fact', 'check-done -'), 11, True)),
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
    ok(all(number_reading([TZ_FILE, 'CryptoTZ/TZ-39-x.md']).values()), 'number: the one file reads PASS')
    ok(not all(number_reading([TZ_FILE, 'CryptoTZ/TZ-40-other.md']).values()) and not all(number_reading([TZ_FILE, 'CryptoReports/TZ-40-x-report.md']).values()),
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
    real_sleep = time.sleep
    with tempfile.TemporaryDirectory() as tmp:
        saved = list(sys.path)
        sys.path.insert(0, stage)
        try:
            bot = load_module('advbot_selftest', stage + '/adv3-bot.py')
        finally:
            sys.path[:] = saved
        bot.STATE = tmp
        real_fapi = bot.adv3.fapi
        time.sleep = lambda x: None
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
            time.sleep = real_sleep
    kinds = [r['kind'] for r in records]
    args = dict(texts=texts, calc=calc, runs=runs, kinds=kinds, records=records, log=blog, same=True, expect=expect)
    good = render_checks(**args)
    al = {k: [(x['kind'], x['touch']) for x in runs[k]['rec']['alerts']] for k in runs}
    ok(all(good.values()) and len(good) == 22, 'render_checks: the stage\'s bot on a synthetic market reads 22 of 22 - %s' % [k for k, v in good.items() if not v])
    ok(('stop', False) in al['signal'] and ('signal', False) in al['signal'] and ('candidate', False) in al['signal'] and al['fact'] == [('stop', True)],
       'the synthetic market meets every alert: a stop on a closed candle, an exit by signal and new candidates at the signal check, a forming candle '
       'through a stop at the fact check')
    c3 = RENDER_CASES[2]
    ok(len(calc[c3]['plan']['items']) == 3 and len(calc[c3]['plan']['more']) == 9 and EXTRA_HEAD in '\n'.join(texts[RENDER_CASES[0]])
       and len(runs['signal']['rec']['cards']) == 12 and sum(c['extra'] for c in runs['signal']['rec']['cards']) == 9,
       'the synthetic market shows STRONG at every rank: twelve STRONG, the default allocation three placed and nine more, «сигнал» '
       'and the signal check nine extra cards')

    def bad(**kw):
        a_ = dict(args)
        a_.update(kw)
        return not all(render_checks(**a_).values())

    sig, top7 = texts[RENDER_CASES[0]], texts[RENDER_CASES[1]]
    sig_t = '\n'.join(sig)
    ok(bad(log='Traceback (most recent call last):') and bad(log='check failed: x'), 'render_checks: a traceback or a failure in the bot\'s log reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: []})), 'render_checks: a command with no answer reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[5]: ['<b>HELP']})), 'render_checks: unbalanced markup reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [sig_t + '\nОценка доверия']})), 'render_checks: a «сигнал» carrying the six ratings reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [re.sub(CONF, 'X: ', sig_t, count=1)]})), 'render_checks: a card without its confidence reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [sig_t.replace('Уверенность: <b>1/5</b>', 'Уверенность: <b>3/5</b>', 1)]})),
       'render_checks: a confidence that is not the rung reads FAIL')
    cut = sig_t[:sig_t.index(EXTRA_HEAD)] + sig_t[sig_t.index('<b>Остальные сигналы</b>'):]
    ok(bad(texts=dict(texts, **{RENDER_CASES[0]: [cut]})), 'render_checks: a «сигнал» without its STRONG beyond the TOP-3 reads FAIL')
    untag = sig_t.replace(TAG + '\n', '\n', 1)
    ok(untag != sig_t and bad(texts=dict(texts, **{RENDER_CASES[0]: [untag]})), 'render_checks: a STRONG card beyond the TOP-3 without its tag reads FAIL')
    unstar = re.sub(r'(?m)^([🟢🔴] <b>[A-Z0-9]+ · (?:LONG|SHORT)</b>) · ★ STRONG$', r'\1', '\n'.join(top7), count=1)
    ok(unstar != '\n'.join(top7) and bad(texts=dict(texts, **{RENDER_CASES[1]: [unstar]})), 'render_checks: a STRONG card of the list without its ★ reads FAIL')
    ok(bad(texts=dict(texts, **{RENDER_CASES[4]: [texts[RENDER_CASES[4]][0].replace('+0,22 R', '+0,55 R')]}))
       and bad(texts=dict(texts, **{RENDER_CASES[4]: [texts[RENDER_CASES[4]][0].replace('дал +0,51 R', 'дал +0,61 R')]})),
       'render_checks: an assessment quoting the 42\'s STRONG figure, or another E6 figure, reads FAIL')
    ok(bad(expect=dict(expect, consts=(11.1,) + expect['consts'][1:])) and bad(expect=dict(expect, consts=expect['consts'][:7] + (10,) + expect['consts'][8:]))
       and bad(expect=dict(expect, consts=expect['consts'][:10] + (0.0,) + expect['consts'][11:])),
       'render_checks: another stop limit, another list length or no pause between parts reads FAIL')
    ok(bad(texts=dict(texts, **{c3: [calc[c3]['parts'][0] + ' ']})), 'render_checks: an allocation reply that is not the plan\'s own reads FAIL')
    p = calc[c3]['plan']
    worse = dict(p, items=[dict(p['items'][0], card=dict(p['items'][0]['card'], stop_pct=14.5))] + p['items'][1:])
    ok(bad(calc=dict(calc, **{c3: dict(calc[c3], plan=worse)})), 'render_checks: a stop beyond 14 % in a plan reads FAIL')
    heavy = dict(p, items=[dict(p['items'][0], loss_exact=p['budget'] * 0.0101)] + p['items'][1:])
    ok(bad(calc=dict(calc, **{c3: dict(calc[c3], plan=heavy)})), 'render_checks: a loss at a stop beyond 1 % of the budget reads FAIL')
    fat = dict(p, more=[dict(p['more'][0], loss_exact=p['budget'] * p['risk'] / 100 * 1.01)] + p['more'][1:])
    ok(bad(calc=dict(calc, **{c3: dict(calc[c3], plan=fat)})), 'render_checks: one of the more beyond the average risk reads FAIL')
    lost = dict(p, more=p['more'][1:])
    ok(bad(calc=dict(calc, **{c3: dict(calc[c3], plan=lost)})), 'render_checks: a STRONG coin that passes and is neither placed nor among the more reads FAIL')
    swapped = dict(p, items=p['items'][:2] + p['more'][:1], more=p['items'][2:] + p['more'][1:])
    ok(bad(calc=dict(calc, **{c3: dict(calc[c3], plan=swapped)})), 'render_checks: a coin beyond the first n placed before one within them reads FAIL')
    sg = runs['signal']
    flipped = dict(sg, rec=dict(sg['rec'], quiet=not sg['rec']['quiet']))
    ok(bad(runs=dict(runs, signal=flipped)), 'render_checks: a check whose quiet flag disagrees with its alerts reads FAIL')
    dropped = dict(sg, rec=dict(sg['rec'], alerts=[a for a in sg['rec']['alerts'] if a['kind'] != 'signal']))
    ok(bad(runs=dict(runs, signal=dropped)), 'render_checks: an exit the walk finds and the check does not alert reads FAIL')
    fa = runs['fact']
    again = dict(fa, rec=dict(fa['rec'], alerts=fa['rec']['alerts'] + [a for a in sg['rec']['alerts'] if a['kind'] == 'stop']))
    ok(bad(runs=dict(runs, fact=again)), 'render_checks: an alert sent twice across the checks reads FAIL')
    ok(bad(runs=dict(runs, fact=dict(fa, rec=dict(fa['rec'], cards=list(sg['rec']['cards']))))), 'render_checks: a fact check offering the close\'s cards reads FAIL')
    ok(bad(runs=dict(runs, signal=dict(sg, rec=dict(sg['rec'], strong_all=sg['rec']['strong_all'][:-1])))),
       'render_checks: a check record whose STRONG at every rank is not the checker\'s reads FAIL')
    ok(bad(kinds=kinds[:-1]) and bad(kinds=['check'] + kinds[1:]), 'render_checks: a journal that lacks a record or has another kind reads FAIL')
    ok(bad(same=False), 'render_checks: the bot\'s own record changed reads FAIL')
    out('SELFTEST PASS: %d of %d checks passed' % (len(done), len(done)))


def main(argv):
    if not argv:
        sys.exit('usage: tz40-advisor-strong.py MODE [ARG]')
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
